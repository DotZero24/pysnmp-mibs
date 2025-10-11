# SNMP MIB module (LUM-GMPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-GMPLS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:29 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(lumGmplsMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumGmplsMIB",
    "lumModules")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 MgmtNameString) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "MgmtNameString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumGmplsMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 25)
)
if mibBuilder.loadTexts:
    lumGmplsMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2003-06-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class GmplsLinkType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("client", 1),
          ("trunc", 2))
    )



class GmplsLinkDirType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("rx", 1),
          ("tx", 2),
          ("biDi", 3),
          ("unused", 4),
          ("txRx", 5))
    )



class GmplsSwitchCapability(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              51,
              100,
              150,
              200)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("psc1", 1),
          ("psc2", 2),
          ("psc3", 3),
          ("psc4", 4),
          ("l2sc", 51),
          ("tdm", 100),
          ("lsc", 150),
          ("fsc", 200))
    )



class GmplsEncoding(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undef", 0),
          ("eth", 1),
          ("sdh", 2),
          ("fc", 3),
          ("multi", 4),
          ("lambda", 5))
    )



class GmplsEncodingStd(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              5,
              8,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("undef", 0),
          ("eth", 2),
          ("pdh", 3),
          ("sdh", 5),
          ("lambda", 8),
          ("fiber", 9),
          ("fc", 11))
    )



class GmplsConnectivity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undef", 0),
          ("tx", 1),
          ("bidir", 2),
          ("mismatch", 3),
          ("rx", 4))
    )



class GmplsLinkProtection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("extraTraffic", 1),
          ("unprotected", 2),
          ("shared", 4),
          ("dedecatedOneToOne", 8),
          ("dedecatedOnePlusOne", 16))
    )



class GmplsPayloadIdentifier(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              36,
              37,
              38,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              50)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("asynchE4", 5),
          ("asynchDS3T3", 6),
          ("asynchE3", 7),
          ("bitsynchE3", 8),
          ("bytesynchE3", 9),
          ("asynchDS2T2", 10),
          ("bitsynchDS2T2", 11),
          ("asynchE1", 13),
          ("bytesynchE1", 14),
          ("bytesynch31ByDS0", 15),
          ("asynchDS1T1", 16),
          ("bitsynchDS1T1", 17),
          ("bytesynchDS1T1", 18),
          ("vC11VC12", 19),
          ("ds1SFAsynch", 22),
          ("ds1ESFAsynch", 23),
          ("ds3M23Asynch", 24),
          ("ds3CBitParityAsynch", 25),
          ("vtLovc", 26),
          ("stsSpeHovc", 27),
          ("posNoScramble16BitCrc", 28),
          ("posNoScramble32BitCrc", 29),
          ("posScramble16BitCrc", 30),
          ("posScramble32BitCrc", 31),
          ("atm", 32),
          ("ethernet", 33),
          ("sdhSonet", 34),
          ("digitalwrapper", 36),
          ("lambda", 37),
          ("ansiEtsiPdh", 38),
          ("lapsSdh", 40),
          ("fddi", 41),
          ("dqdb", 42),
          ("fiberChannel3", 43),
          ("hdlc", 44),
          ("ethernetV2DixOnly", 45),
          ("ethernet802dot3Only", 46),
          ("ppp", 50))
    )



class GmplsDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forward", 0),
          ("bidirectional", 1))
    )



class GmplsPathComputation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicFull", 1),
          ("explicit", 2),
          ("dynamicPartial", 3))
    )



class GmplsNumberedType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unnum", 1),
          ("num", 2))
    )



class GmplsLabelRequestType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("atm", 2),
          ("frame", 3),
          ("general", 4))
    )



class GmplsBpsRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("undef", 0),
          ("eth10M", 1),
          ("e3", 2),
          ("ds3", 3),
          ("sts1", 4),
          ("eth100M", 5),
          ("fc133M", 6),
          ("e4", 7),
          ("stm1", 8),
          ("fc266M", 9),
          ("fc531M", 10),
          ("stm4", 11),
          ("gbe", 12),
          ("fc1062", 13),
          ("stm16", 14),
          ("stm64", 15),
          ("gbe10", 16),
          ("stm256", 17))
    )



class GmplsModel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("peer", 0),
          ("overlay", 1))
    )



class GmplsRouting(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undef", 0),
          ("nodeLevel", 1),
          ("interface", 2),
          ("label", 3),
          ("interfaceAndLabel", 4))
    )



# MIB Managed Objects in the order of their OIDs

_LumGmplsConfs_ObjectIdentity = ObjectIdentity
lumGmplsConfs = _LumGmplsConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1)
)
_LumGmplsGroups_ObjectIdentity = ObjectIdentity
lumGmplsGroups = _LumGmplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 1)
)
_LumGmplsCompl_ObjectIdentity = ObjectIdentity
lumGmplsCompl = _LumGmplsCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 2)
)
_LumGmplsMIBObjects_ObjectIdentity = ObjectIdentity
lumGmplsMIBObjects = _LumGmplsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2)
)
_GmplsGeneral_ObjectIdentity = ObjectIdentity
gmplsGeneral = _GmplsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 1)
)
_GmplsGeneralLastChangeTime_Type = DateAndTime
_GmplsGeneralLastChangeTime_Object = MibScalar
gmplsGeneralLastChangeTime = _GmplsGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 1, 1),
    _GmplsGeneralLastChangeTime_Type()
)
gmplsGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsGeneralLastChangeTime.setStatus("current")
_GmplsGeneralStateLastChangeTime_Type = DateAndTime
_GmplsGeneralStateLastChangeTime_Object = MibScalar
gmplsGeneralStateLastChangeTime = _GmplsGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 1, 2),
    _GmplsGeneralStateLastChangeTime_Type()
)
gmplsGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsGeneralStateLastChangeTime.setStatus("current")
_GmplsGeneralGmplsTelinkTableSize_Type = Unsigned32
_GmplsGeneralGmplsTelinkTableSize_Object = MibScalar
gmplsGeneralGmplsTelinkTableSize = _GmplsGeneralGmplsTelinkTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 1, 3),
    _GmplsGeneralGmplsTelinkTableSize_Type()
)
gmplsGeneralGmplsTelinkTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsGeneralGmplsTelinkTableSize.setStatus("current")
_GmplsGeneralGmplsPhyslinkTableSize_Type = Unsigned32
_GmplsGeneralGmplsPhyslinkTableSize_Object = MibScalar
gmplsGeneralGmplsPhyslinkTableSize = _GmplsGeneralGmplsPhyslinkTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 1, 4),
    _GmplsGeneralGmplsPhyslinkTableSize_Type()
)
gmplsGeneralGmplsPhyslinkTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsGeneralGmplsPhyslinkTableSize.setStatus("current")
_GmplsGeneralGmplsEroTableSize_Type = Unsigned32
_GmplsGeneralGmplsEroTableSize_Object = MibScalar
gmplsGeneralGmplsEroTableSize = _GmplsGeneralGmplsEroTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 1, 5),
    _GmplsGeneralGmplsEroTableSize_Type()
)
gmplsGeneralGmplsEroTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsGeneralGmplsEroTableSize.setStatus("current")
_GmplsGeneralGmplsTedTableSize_Type = Unsigned32
_GmplsGeneralGmplsTedTableSize_Object = MibScalar
gmplsGeneralGmplsTedTableSize = _GmplsGeneralGmplsTedTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 1, 6),
    _GmplsGeneralGmplsTedTableSize_Type()
)
gmplsGeneralGmplsTedTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsGeneralGmplsTedTableSize.setStatus("current")
_GmplsGeneralGmplsLspTableSize_Type = Unsigned32
_GmplsGeneralGmplsLspTableSize_Object = MibScalar
gmplsGeneralGmplsLspTableSize = _GmplsGeneralGmplsLspTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 1, 7),
    _GmplsGeneralGmplsLspTableSize_Type()
)
gmplsGeneralGmplsLspTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsGeneralGmplsLspTableSize.setStatus("current")
_GmplsPhysLinkList_ObjectIdentity = ObjectIdentity
gmplsPhysLinkList = _GmplsPhysLinkList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2)
)
_GmplsPhysLinkTable_Object = MibTable
gmplsPhysLinkTable = _GmplsPhysLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gmplsPhysLinkTable.setStatus("current")
_GmplsPhysLinkEntry_Object = MibTableRow
gmplsPhysLinkEntry = _GmplsPhysLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1)
)
gmplsPhysLinkEntry.setIndexNames(
    (0, "LUM-GMPLS-MIB", "gmplsPhysLinkIndex"),
)
if mibBuilder.loadTexts:
    gmplsPhysLinkEntry.setStatus("current")


class _GmplsPhysLinkIndex_Type(Unsigned32):
    """Custom type gmplsPhysLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsPhysLinkIndex_Type.__name__ = "Unsigned32"
_GmplsPhysLinkIndex_Object = MibTableColumn
gmplsPhysLinkIndex = _GmplsPhysLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 1),
    _GmplsPhysLinkIndex_Type()
)
gmplsPhysLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkIndex.setStatus("current")
_GmplsPhysLinkName_Type = MgmtNameString
_GmplsPhysLinkName_Object = MibTableColumn
gmplsPhysLinkName = _GmplsPhysLinkName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 2),
    _GmplsPhysLinkName_Type()
)
gmplsPhysLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkName.setStatus("current")


class _GmplsPhysLinkDescr_Type(DisplayString):
    """Custom type gmplsPhysLinkDescr based on DisplayString"""
    defaultValue = OctetString("")


_GmplsPhysLinkDescr_Type.__name__ = "DisplayString"
_GmplsPhysLinkDescr_Object = MibTableColumn
gmplsPhysLinkDescr = _GmplsPhysLinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 3),
    _GmplsPhysLinkDescr_Type()
)
gmplsPhysLinkDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsPhysLinkDescr.setStatus("deprecated")


class _GmplsPhysLinkLinkId_Type(Unsigned32):
    """Custom type gmplsPhysLinkLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsPhysLinkLinkId_Type.__name__ = "Unsigned32"
_GmplsPhysLinkLinkId_Object = MibTableColumn
gmplsPhysLinkLinkId = _GmplsPhysLinkLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 4),
    _GmplsPhysLinkLinkId_Type()
)
gmplsPhysLinkLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkLinkId.setStatus("current")
_GmplsPhysLinkType_Type = GmplsLinkType
_GmplsPhysLinkType_Object = MibTableColumn
gmplsPhysLinkType = _GmplsPhysLinkType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 5),
    _GmplsPhysLinkType_Type()
)
gmplsPhysLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkType.setStatus("current")
_GmplsPhysLinkOwner_Type = MgmtNameString
_GmplsPhysLinkOwner_Object = MibTableColumn
gmplsPhysLinkOwner = _GmplsPhysLinkOwner_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 6),
    _GmplsPhysLinkOwner_Type()
)
gmplsPhysLinkOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkOwner.setStatus("deprecated")


class _GmplsPhysLinkResourceType_Type(Unsigned32):
    """Custom type gmplsPhysLinkResourceType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsPhysLinkResourceType_Type.__name__ = "Unsigned32"
_GmplsPhysLinkResourceType_Object = MibTableColumn
gmplsPhysLinkResourceType = _GmplsPhysLinkResourceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 7),
    _GmplsPhysLinkResourceType_Type()
)
gmplsPhysLinkResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkResourceType.setStatus("current")


class _GmplsPhysLinkResourceId_Type(Unsigned32):
    """Custom type gmplsPhysLinkResourceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsPhysLinkResourceId_Type.__name__ = "Unsigned32"
_GmplsPhysLinkResourceId_Object = MibTableColumn
gmplsPhysLinkResourceId = _GmplsPhysLinkResourceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 8),
    _GmplsPhysLinkResourceId_Type()
)
gmplsPhysLinkResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkResourceId.setStatus("current")


class _GmplsPhysLinkEntityId_Type(Unsigned32):
    """Custom type gmplsPhysLinkEntityId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsPhysLinkEntityId_Type.__name__ = "Unsigned32"
_GmplsPhysLinkEntityId_Object = MibTableColumn
gmplsPhysLinkEntityId = _GmplsPhysLinkEntityId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 9),
    _GmplsPhysLinkEntityId_Type()
)
gmplsPhysLinkEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkEntityId.setStatus("current")
_GmplsPhysLinkDirection_Type = GmplsLinkDirType
_GmplsPhysLinkDirection_Object = MibTableColumn
gmplsPhysLinkDirection = _GmplsPhysLinkDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 10),
    _GmplsPhysLinkDirection_Type()
)
gmplsPhysLinkDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkDirection.setStatus("current")
_GmplsPhysLinkTeLinkCommand_Type = CommandString
_GmplsPhysLinkTeLinkCommand_Object = MibTableColumn
gmplsPhysLinkTeLinkCommand = _GmplsPhysLinkTeLinkCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 11),
    _GmplsPhysLinkTeLinkCommand_Type()
)
gmplsPhysLinkTeLinkCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkTeLinkCommand.setStatus("current")


class _GmplsPhysLinkTeState_Type(Integer32):
    """Custom type gmplsPhysLinkTeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("defined", 2))
    )


_GmplsPhysLinkTeState_Type.__name__ = "Integer32"
_GmplsPhysLinkTeState_Object = MibTableColumn
gmplsPhysLinkTeState = _GmplsPhysLinkTeState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 12),
    _GmplsPhysLinkTeState_Type()
)
gmplsPhysLinkTeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkTeState.setStatus("current")
_GmplsPhysLinkSwitchCapability_Type = GmplsSwitchCapability
_GmplsPhysLinkSwitchCapability_Object = MibTableColumn
gmplsPhysLinkSwitchCapability = _GmplsPhysLinkSwitchCapability_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 13),
    _GmplsPhysLinkSwitchCapability_Type()
)
gmplsPhysLinkSwitchCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkSwitchCapability.setStatus("current")
_GmplsPhysLinkEncoding_Type = GmplsEncoding
_GmplsPhysLinkEncoding_Object = MibTableColumn
gmplsPhysLinkEncoding = _GmplsPhysLinkEncoding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 14),
    _GmplsPhysLinkEncoding_Type()
)
gmplsPhysLinkEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkEncoding.setStatus("current")
_GmplsPhysLinkMinBitRate_Type = Unsigned32
_GmplsPhysLinkMinBitRate_Object = MibTableColumn
gmplsPhysLinkMinBitRate = _GmplsPhysLinkMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 15),
    _GmplsPhysLinkMinBitRate_Type()
)
gmplsPhysLinkMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkMinBitRate.setStatus("current")
_GmplsPhysLinkMaxBitRate_Type = Unsigned32
_GmplsPhysLinkMaxBitRate_Object = MibTableColumn
gmplsPhysLinkMaxBitRate = _GmplsPhysLinkMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 16),
    _GmplsPhysLinkMaxBitRate_Type()
)
gmplsPhysLinkMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkMaxBitRate.setStatus("current")
_GmplsPhysLinkInfoCommand_Type = CommandString
_GmplsPhysLinkInfoCommand_Object = MibTableColumn
gmplsPhysLinkInfoCommand = _GmplsPhysLinkInfoCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 2, 1, 1, 17),
    _GmplsPhysLinkInfoCommand_Type()
)
gmplsPhysLinkInfoCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsPhysLinkInfoCommand.setStatus("current")
_GmplsTeLinkList_ObjectIdentity = ObjectIdentity
gmplsTeLinkList = _GmplsTeLinkList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3)
)
_GmplsTeLinkTable_Object = MibTable
gmplsTeLinkTable = _GmplsTeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gmplsTeLinkTable.setStatus("current")
_GmplsTeLinkEntry_Object = MibTableRow
gmplsTeLinkEntry = _GmplsTeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1)
)
gmplsTeLinkEntry.setIndexNames(
    (0, "LUM-GMPLS-MIB", "gmplsTeLinkIndex"),
)
if mibBuilder.loadTexts:
    gmplsTeLinkEntry.setStatus("current")


class _GmplsTeLinkIndex_Type(Unsigned32):
    """Custom type gmplsTeLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTeLinkIndex_Type.__name__ = "Unsigned32"
_GmplsTeLinkIndex_Object = MibTableColumn
gmplsTeLinkIndex = _GmplsTeLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 1),
    _GmplsTeLinkIndex_Type()
)
gmplsTeLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkIndex.setStatus("current")
_GmplsTeLinkName_Type = MgmtNameString
_GmplsTeLinkName_Object = MibTableColumn
gmplsTeLinkName = _GmplsTeLinkName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 2),
    _GmplsTeLinkName_Type()
)
gmplsTeLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkName.setStatus("current")


class _GmplsTeLinkDescr_Type(DisplayString):
    """Custom type gmplsTeLinkDescr based on DisplayString"""
    defaultValue = OctetString("")


_GmplsTeLinkDescr_Type.__name__ = "DisplayString"
_GmplsTeLinkDescr_Object = MibTableColumn
gmplsTeLinkDescr = _GmplsTeLinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 3),
    _GmplsTeLinkDescr_Type()
)
gmplsTeLinkDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkDescr.setStatus("current")


class _GmplsTeLinkLocalLinkId_Type(Unsigned32):
    """Custom type gmplsTeLinkLocalLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTeLinkLocalLinkId_Type.__name__ = "Unsigned32"
_GmplsTeLinkLocalLinkId_Object = MibTableColumn
gmplsTeLinkLocalLinkId = _GmplsTeLinkLocalLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 4),
    _GmplsTeLinkLocalLinkId_Type()
)
gmplsTeLinkLocalLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkLocalLinkId.setStatus("current")


class _GmplsTeLinkRemoteId_Type(Unsigned32):
    """Custom type gmplsTeLinkRemoteId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GmplsTeLinkRemoteId_Type.__name__ = "Unsigned32"
_GmplsTeLinkRemoteId_Object = MibTableColumn
gmplsTeLinkRemoteId = _GmplsTeLinkRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 5),
    _GmplsTeLinkRemoteId_Type()
)
gmplsTeLinkRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkRemoteId.setStatus("current")


class _GmplsTeLinkTxLinkId_Type(Unsigned32):
    """Custom type gmplsTeLinkTxLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTeLinkTxLinkId_Type.__name__ = "Unsigned32"
_GmplsTeLinkTxLinkId_Object = MibTableColumn
gmplsTeLinkTxLinkId = _GmplsTeLinkTxLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 6),
    _GmplsTeLinkTxLinkId_Type()
)
gmplsTeLinkTxLinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTeLinkTxLinkId.setStatus("current")


class _GmplsTeLinkRxLinkId_Type(Unsigned32):
    """Custom type gmplsTeLinkRxLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTeLinkRxLinkId_Type.__name__ = "Unsigned32"
_GmplsTeLinkRxLinkId_Object = MibTableColumn
gmplsTeLinkRxLinkId = _GmplsTeLinkRxLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 7),
    _GmplsTeLinkRxLinkId_Type()
)
gmplsTeLinkRxLinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsTeLinkRxLinkId.setStatus("current")
_GmplsTeLinkRemoteIp_Type = DisplayString
_GmplsTeLinkRemoteIp_Object = MibTableColumn
gmplsTeLinkRemoteIp = _GmplsTeLinkRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 8),
    _GmplsTeLinkRemoteIp_Type()
)
gmplsTeLinkRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkRemoteIp.setStatus("current")


class _GmplsTeLinkAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type gmplsTeLinkAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_GmplsTeLinkAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_GmplsTeLinkAdminStatus_Object = MibTableColumn
gmplsTeLinkAdminStatus = _GmplsTeLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 9),
    _GmplsTeLinkAdminStatus_Type()
)
gmplsTeLinkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkAdminStatus.setStatus("current")
_GmplsTeLinkOperStatus_Type = BoardOrInterfaceOperStatus
_GmplsTeLinkOperStatus_Object = MibTableColumn
gmplsTeLinkOperStatus = _GmplsTeLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 10),
    _GmplsTeLinkOperStatus_Type()
)
gmplsTeLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkOperStatus.setStatus("deprecated")


class _GmplsTeLinkUsage_Type(Integer32):
    """Custom type gmplsTeLinkUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("resvd", 2),
          ("run", 3),
          ("tear", 4))
    )


_GmplsTeLinkUsage_Type.__name__ = "Integer32"
_GmplsTeLinkUsage_Object = MibTableColumn
gmplsTeLinkUsage = _GmplsTeLinkUsage_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 16),
    _GmplsTeLinkUsage_Type()
)
gmplsTeLinkUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkUsage.setStatus("current")
_GmplsTeLinkLspCommand_Type = CommandString
_GmplsTeLinkLspCommand_Object = MibTableColumn
gmplsTeLinkLspCommand = _GmplsTeLinkLspCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 17),
    _GmplsTeLinkLspCommand_Type()
)
gmplsTeLinkLspCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkLspCommand.setStatus("current")


class _GmplsTeLinkAvaliable_Type(Integer32):
    """Custom type gmplsTeLinkAvaliable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("occupied", 2))
    )


_GmplsTeLinkAvaliable_Type.__name__ = "Integer32"
_GmplsTeLinkAvaliable_Object = MibTableColumn
gmplsTeLinkAvaliable = _GmplsTeLinkAvaliable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 18),
    _GmplsTeLinkAvaliable_Type()
)
gmplsTeLinkAvaliable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkAvaliable.setStatus("current")


class _GmplsTeLinkRxAlarm_Type(Integer32):
    """Custom type gmplsTeLinkRxAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_GmplsTeLinkRxAlarm_Type.__name__ = "Integer32"
_GmplsTeLinkRxAlarm_Object = MibTableColumn
gmplsTeLinkRxAlarm = _GmplsTeLinkRxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 19),
    _GmplsTeLinkRxAlarm_Type()
)
gmplsTeLinkRxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkRxAlarm.setStatus("deprecated")


class _GmplsTeLinkTxAlarm_Type(Integer32):
    """Custom type gmplsTeLinkTxAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_GmplsTeLinkTxAlarm_Type.__name__ = "Integer32"
_GmplsTeLinkTxAlarm_Object = MibTableColumn
gmplsTeLinkTxAlarm = _GmplsTeLinkTxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 20),
    _GmplsTeLinkTxAlarm_Type()
)
gmplsTeLinkTxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkTxAlarm.setStatus("deprecated")


class _GmplsTeLinkLabels_Type(Unsigned32):
    """Custom type gmplsTeLinkLabels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTeLinkLabels_Type.__name__ = "Unsigned32"
_GmplsTeLinkLabels_Object = MibTableColumn
gmplsTeLinkLabels = _GmplsTeLinkLabels_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 21),
    _GmplsTeLinkLabels_Type()
)
gmplsTeLinkLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkLabels.setStatus("current")


class _GmplsTeLinkFreeLabels_Type(Unsigned32):
    """Custom type gmplsTeLinkFreeLabels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTeLinkFreeLabels_Type.__name__ = "Unsigned32"
_GmplsTeLinkFreeLabels_Object = MibTableColumn
gmplsTeLinkFreeLabels = _GmplsTeLinkFreeLabels_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 22),
    _GmplsTeLinkFreeLabels_Type()
)
gmplsTeLinkFreeLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkFreeLabels.setStatus("current")


class _GmplsTeLinkLabelUsageMask_Type(Unsigned32):
    """Custom type gmplsTeLinkLabelUsageMask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GmplsTeLinkLabelUsageMask_Type.__name__ = "Unsigned32"
_GmplsTeLinkLabelUsageMask_Object = MibTableColumn
gmplsTeLinkLabelUsageMask = _GmplsTeLinkLabelUsageMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 23),
    _GmplsTeLinkLabelUsageMask_Type()
)
gmplsTeLinkLabelUsageMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkLabelUsageMask.setStatus("current")
_GmplsTeLinkStatus_Type = GmplsConnectivity
_GmplsTeLinkStatus_Object = MibTableColumn
gmplsTeLinkStatus = _GmplsTeLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 24),
    _GmplsTeLinkStatus_Type()
)
gmplsTeLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkStatus.setStatus("current")
_GmplsTeLinkInfoCommand_Type = CommandString
_GmplsTeLinkInfoCommand_Object = MibTableColumn
gmplsTeLinkInfoCommand = _GmplsTeLinkInfoCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 25),
    _GmplsTeLinkInfoCommand_Type()
)
gmplsTeLinkInfoCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkInfoCommand.setStatus("current")


class _GmplsTeLinkAdmin_Type(Integer32):
    """Custom type gmplsTeLinkAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("locked", 2))
    )


_GmplsTeLinkAdmin_Type.__name__ = "Integer32"
_GmplsTeLinkAdmin_Object = MibTableColumn
gmplsTeLinkAdmin = _GmplsTeLinkAdmin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 26),
    _GmplsTeLinkAdmin_Type()
)
gmplsTeLinkAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkAdmin.setStatus("current")


class _GmplsTeLinkPresence_Type(Integer32):
    """Custom type gmplsTeLinkPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("missing", 2))
    )


_GmplsTeLinkPresence_Type.__name__ = "Integer32"
_GmplsTeLinkPresence_Object = MibTableColumn
gmplsTeLinkPresence = _GmplsTeLinkPresence_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 27),
    _GmplsTeLinkPresence_Type()
)
gmplsTeLinkPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkPresence.setStatus("current")


class _GmplsTeLinkAlarm_Type(Integer32):
    """Custom type gmplsTeLinkAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_GmplsTeLinkAlarm_Type.__name__ = "Integer32"
_GmplsTeLinkAlarm_Object = MibTableColumn
gmplsTeLinkAlarm = _GmplsTeLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 28),
    _GmplsTeLinkAlarm_Type()
)
gmplsTeLinkAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkAlarm.setStatus("current")
_GmplsTeLinkSummary_Type = DisplayString
_GmplsTeLinkSummary_Object = MibTableColumn
gmplsTeLinkSummary = _GmplsTeLinkSummary_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 29),
    _GmplsTeLinkSummary_Type()
)
gmplsTeLinkSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkSummary.setStatus("current")


class _GmplsTeLinkLinkType_Type(GmplsNumberedType):
    """Custom type gmplsTeLinkLinkType based on GmplsNumberedType"""
    defaultValue = 1


_GmplsTeLinkLinkType_Type.__name__ = "GmplsNumberedType"
_GmplsTeLinkLinkType_Object = MibTableColumn
gmplsTeLinkLinkType = _GmplsTeLinkLinkType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 30),
    _GmplsTeLinkLinkType_Type()
)
gmplsTeLinkLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkLinkType.setStatus("current")
_GmplsTeLinkConnectCommand_Type = CommandString
_GmplsTeLinkConnectCommand_Object = MibTableColumn
gmplsTeLinkConnectCommand = _GmplsTeLinkConnectCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 31),
    _GmplsTeLinkConnectCommand_Type()
)
gmplsTeLinkConnectCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkConnectCommand.setStatus("current")
_GmplsTeLinkPayload_Type = GmplsPayloadIdentifier
_GmplsTeLinkPayload_Object = MibTableColumn
gmplsTeLinkPayload = _GmplsTeLinkPayload_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 32),
    _GmplsTeLinkPayload_Type()
)
gmplsTeLinkPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkPayload.setStatus("current")


class _GmplsTeLinkMetric_Type(Unsigned32):
    """Custom type gmplsTeLinkMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GmplsTeLinkMetric_Type.__name__ = "Unsigned32"
_GmplsTeLinkMetric_Object = MibTableColumn
gmplsTeLinkMetric = _GmplsTeLinkMetric_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 33),
    _GmplsTeLinkMetric_Type()
)
gmplsTeLinkMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkMetric.setStatus("current")


class _GmplsTeLinkColor_Type(Unsigned32):
    """Custom type gmplsTeLinkColor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GmplsTeLinkColor_Type.__name__ = "Unsigned32"
_GmplsTeLinkColor_Object = MibTableColumn
gmplsTeLinkColor = _GmplsTeLinkColor_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 34),
    _GmplsTeLinkColor_Type()
)
gmplsTeLinkColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkColor.setStatus("current")


class _GmplsTeLinkSrlg_Type(Unsigned32):
    """Custom type gmplsTeLinkSrlg based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GmplsTeLinkSrlg_Type.__name__ = "Unsigned32"
_GmplsTeLinkSrlg_Object = MibTableColumn
gmplsTeLinkSrlg = _GmplsTeLinkSrlg_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 35),
    _GmplsTeLinkSrlg_Type()
)
gmplsTeLinkSrlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkSrlg.setStatus("current")


class _GmplsTeLinkModel_Type(GmplsModel):
    """Custom type gmplsTeLinkModel based on GmplsModel"""
    defaultValue = 0


_GmplsTeLinkModel_Type.__name__ = "GmplsModel"
_GmplsTeLinkModel_Object = MibTableColumn
gmplsTeLinkModel = _GmplsTeLinkModel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 36),
    _GmplsTeLinkModel_Type()
)
gmplsTeLinkModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkModel.setStatus("current")


class _GmplsTeLinkLocalIfIp_Type(DisplayString):
    """Custom type gmplsTeLinkLocalIfIp based on DisplayString"""
    defaultValue = OctetString("")


_GmplsTeLinkLocalIfIp_Type.__name__ = "DisplayString"
_GmplsTeLinkLocalIfIp_Object = MibTableColumn
gmplsTeLinkLocalIfIp = _GmplsTeLinkLocalIfIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 37),
    _GmplsTeLinkLocalIfIp_Type()
)
gmplsTeLinkLocalIfIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkLocalIfIp.setStatus("current")


class _GmplsTeLinkRemoteIfIp_Type(DisplayString):
    """Custom type gmplsTeLinkRemoteIfIp based on DisplayString"""
    defaultValue = OctetString("")


_GmplsTeLinkRemoteIfIp_Type.__name__ = "DisplayString"
_GmplsTeLinkRemoteIfIp_Object = MibTableColumn
gmplsTeLinkRemoteIfIp = _GmplsTeLinkRemoteIfIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 38),
    _GmplsTeLinkRemoteIfIp_Type()
)
gmplsTeLinkRemoteIfIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkRemoteIfIp.setStatus("current")


class _GmplsTeLinkPhysResourceId_Type(Unsigned32):
    """Custom type gmplsTeLinkPhysResourceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTeLinkPhysResourceId_Type.__name__ = "Unsigned32"
_GmplsTeLinkPhysResourceId_Object = MibTableColumn
gmplsTeLinkPhysResourceId = _GmplsTeLinkPhysResourceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 39),
    _GmplsTeLinkPhysResourceId_Type()
)
gmplsTeLinkPhysResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTeLinkPhysResourceId.setStatus("current")


class _GmplsTeLinkRemotePhysResourceId_Type(Unsigned32):
    """Custom type gmplsTeLinkRemotePhysResourceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GmplsTeLinkRemotePhysResourceId_Type.__name__ = "Unsigned32"
_GmplsTeLinkRemotePhysResourceId_Object = MibTableColumn
gmplsTeLinkRemotePhysResourceId = _GmplsTeLinkRemotePhysResourceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 3, 1, 1, 40),
    _GmplsTeLinkRemotePhysResourceId_Type()
)
gmplsTeLinkRemotePhysResourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsTeLinkRemotePhysResourceId.setStatus("current")
_GmplsLspList_ObjectIdentity = ObjectIdentity
gmplsLspList = _GmplsLspList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4)
)
_GmplsLspTable_Object = MibTable
gmplsLspTable = _GmplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1)
)
if mibBuilder.loadTexts:
    gmplsLspTable.setStatus("current")
_GmplsLspEntry_Object = MibTableRow
gmplsLspEntry = _GmplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1)
)
gmplsLspEntry.setIndexNames(
    (0, "LUM-GMPLS-MIB", "gmplsLspIndex"),
)
if mibBuilder.loadTexts:
    gmplsLspEntry.setStatus("current")


class _GmplsLspIndex_Type(Unsigned32):
    """Custom type gmplsLspIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsLspIndex_Type.__name__ = "Unsigned32"
_GmplsLspIndex_Object = MibTableColumn
gmplsLspIndex = _GmplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 1),
    _GmplsLspIndex_Type()
)
gmplsLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspIndex.setStatus("current")
_GmplsLspName_Type = MgmtNameString
_GmplsLspName_Object = MibTableColumn
gmplsLspName = _GmplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 2),
    _GmplsLspName_Type()
)
gmplsLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspName.setStatus("current")


class _GmplsLspDescr_Type(DisplayString):
    """Custom type gmplsLspDescr based on DisplayString"""
    defaultValue = OctetString("")


_GmplsLspDescr_Type.__name__ = "DisplayString"
_GmplsLspDescr_Object = MibTableColumn
gmplsLspDescr = _GmplsLspDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 3),
    _GmplsLspDescr_Type()
)
gmplsLspDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsLspDescr.setStatus("current")


class _GmplsLspLinkId_Type(Unsigned32):
    """Custom type gmplsLspLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsLspLinkId_Type.__name__ = "Unsigned32"
_GmplsLspLinkId_Object = MibTableColumn
gmplsLspLinkId = _GmplsLspLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 4),
    _GmplsLspLinkId_Type()
)
gmplsLspLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspLinkId.setStatus("current")


class _GmplsLspTunnelId_Type(Unsigned32):
    """Custom type gmplsLspTunnelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsLspTunnelId_Type.__name__ = "Unsigned32"
_GmplsLspTunnelId_Object = MibTableColumn
gmplsLspTunnelId = _GmplsLspTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 5),
    _GmplsLspTunnelId_Type()
)
gmplsLspTunnelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsLspTunnelId.setStatus("current")


class _GmplsLspExTunnelId_Type(Unsigned32):
    """Custom type gmplsLspExTunnelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsLspExTunnelId_Type.__name__ = "Unsigned32"
_GmplsLspExTunnelId_Object = MibTableColumn
gmplsLspExTunnelId = _GmplsLspExTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 6),
    _GmplsLspExTunnelId_Type()
)
gmplsLspExTunnelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsLspExTunnelId.setStatus("current")
_GmplsLspIngressIp_Type = DisplayString
_GmplsLspIngressIp_Object = MibTableColumn
gmplsLspIngressIp = _GmplsLspIngressIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 7),
    _GmplsLspIngressIp_Type()
)
gmplsLspIngressIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspIngressIp.setStatus("current")


class _GmplsLspIngressLinkId_Type(Unsigned32):
    """Custom type gmplsLspIngressLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsLspIngressLinkId_Type.__name__ = "Unsigned32"
_GmplsLspIngressLinkId_Object = MibTableColumn
gmplsLspIngressLinkId = _GmplsLspIngressLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 8),
    _GmplsLspIngressLinkId_Type()
)
gmplsLspIngressLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspIngressLinkId.setStatus("current")
_GmplsLspEgressIp_Type = DisplayString
_GmplsLspEgressIp_Object = MibTableColumn
gmplsLspEgressIp = _GmplsLspEgressIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 9),
    _GmplsLspEgressIp_Type()
)
gmplsLspEgressIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspEgressIp.setStatus("current")


class _GmplsLspEgressLinkId_Type(Unsigned32):
    """Custom type gmplsLspEgressLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsLspEgressLinkId_Type.__name__ = "Unsigned32"
_GmplsLspEgressLinkId_Object = MibTableColumn
gmplsLspEgressLinkId = _GmplsLspEgressLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 10),
    _GmplsLspEgressLinkId_Type()
)
gmplsLspEgressLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspEgressLinkId.setStatus("current")


class _GmplsLspUpLabel_Type(Unsigned32):
    """Custom type gmplsLspUpLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsLspUpLabel_Type.__name__ = "Unsigned32"
_GmplsLspUpLabel_Object = MibTableColumn
gmplsLspUpLabel = _GmplsLspUpLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 11),
    _GmplsLspUpLabel_Type()
)
gmplsLspUpLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspUpLabel.setStatus("current")
_GmplsLspUpstreamNeighbour_Type = DisplayString
_GmplsLspUpstreamNeighbour_Object = MibTableColumn
gmplsLspUpstreamNeighbour = _GmplsLspUpstreamNeighbour_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 12),
    _GmplsLspUpstreamNeighbour_Type()
)
gmplsLspUpstreamNeighbour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspUpstreamNeighbour.setStatus("current")
_GmplsLspDownstreamNeighbour_Type = DisplayString
_GmplsLspDownstreamNeighbour_Object = MibTableColumn
gmplsLspDownstreamNeighbour = _GmplsLspDownstreamNeighbour_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 13),
    _GmplsLspDownstreamNeighbour_Type()
)
gmplsLspDownstreamNeighbour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspDownstreamNeighbour.setStatus("current")


class _GmplsLspState_Type(Integer32):
    """Custom type gmplsLspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("setup", 0),
          ("path", 1),
          ("resv", 2),
          ("live", 3),
          ("error", 4),
          ("tear", 5),
          ("hwdeleted", 6))
    )


_GmplsLspState_Type.__name__ = "Integer32"
_GmplsLspState_Object = MibTableColumn
gmplsLspState = _GmplsLspState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 14),
    _GmplsLspState_Type()
)
gmplsLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspState.setStatus("current")


class _GmplsLspSessionId_Type(Unsigned32):
    """Custom type gmplsLspSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsLspSessionId_Type.__name__ = "Unsigned32"
_GmplsLspSessionId_Object = MibTableColumn
gmplsLspSessionId = _GmplsLspSessionId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 15),
    _GmplsLspSessionId_Type()
)
gmplsLspSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsLspSessionId.setStatus("current")


class _GmplsLspRole_Type(Integer32):
    """Custom type gmplsLspRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("head", 1),
          ("transit", 2),
          ("tail", 3))
    )


_GmplsLspRole_Type.__name__ = "Integer32"
_GmplsLspRole_Object = MibTableColumn
gmplsLspRole = _GmplsLspRole_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 16),
    _GmplsLspRole_Type()
)
gmplsLspRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspRole.setStatus("current")
_GmplsLspEroList_Type = DisplayString
_GmplsLspEroList_Object = MibTableColumn
gmplsLspEroList = _GmplsLspEroList_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 17),
    _GmplsLspEroList_Type()
)
gmplsLspEroList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspEroList.setStatus("deprecated")
_GmplsLspEncoding_Type = GmplsEncodingStd
_GmplsLspEncoding_Object = MibTableColumn
gmplsLspEncoding = _GmplsLspEncoding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 18),
    _GmplsLspEncoding_Type()
)
gmplsLspEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspEncoding.setStatus("current")
_GmplsLspSwitchingType_Type = GmplsSwitchCapability
_GmplsLspSwitchingType_Object = MibTableColumn
gmplsLspSwitchingType = _GmplsLspSwitchingType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 19),
    _GmplsLspSwitchingType_Type()
)
gmplsLspSwitchingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspSwitchingType.setStatus("current")
_GmplsLspLinkProtection_Type = GmplsLinkProtection
_GmplsLspLinkProtection_Object = MibTableColumn
gmplsLspLinkProtection = _GmplsLspLinkProtection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 20),
    _GmplsLspLinkProtection_Type()
)
gmplsLspLinkProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspLinkProtection.setStatus("current")
_GmplsLspGPid_Type = GmplsPayloadIdentifier
_GmplsLspGPid_Object = MibTableColumn
gmplsLspGPid = _GmplsLspGPid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 21),
    _GmplsLspGPid_Type()
)
gmplsLspGPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspGPid.setStatus("current")
_GmplsLspDirection_Type = GmplsDirection
_GmplsLspDirection_Object = MibTableColumn
gmplsLspDirection = _GmplsLspDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 22),
    _GmplsLspDirection_Type()
)
gmplsLspDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspDirection.setStatus("current")
_GmplsLspPathComputation_Type = GmplsPathComputation
_GmplsLspPathComputation_Object = MibTableColumn
gmplsLspPathComputation = _GmplsLspPathComputation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 23),
    _GmplsLspPathComputation_Type()
)
gmplsLspPathComputation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsLspPathComputation.setStatus("current")
_GmplsLspEroCommand_Type = CommandString
_GmplsLspEroCommand_Object = MibTableColumn
gmplsLspEroCommand = _GmplsLspEroCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 24),
    _GmplsLspEroCommand_Type()
)
gmplsLspEroCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspEroCommand.setStatus("current")
_GmplsLspPathCommand_Type = CommandString
_GmplsLspPathCommand_Object = MibTableColumn
gmplsLspPathCommand = _GmplsLspPathCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 25),
    _GmplsLspPathCommand_Type()
)
gmplsLspPathCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspPathCommand.setStatus("current")
_GmplsLspTearCommand_Type = CommandString
_GmplsLspTearCommand_Object = MibTableColumn
gmplsLspTearCommand = _GmplsLspTearCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 26),
    _GmplsLspTearCommand_Type()
)
gmplsLspTearCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspTearCommand.setStatus("current")
_GmplsLspListCommand_Type = CommandString
_GmplsLspListCommand_Object = MibTableColumn
gmplsLspListCommand = _GmplsLspListCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 27),
    _GmplsLspListCommand_Type()
)
gmplsLspListCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspListCommand.setStatus("current")
_GmplsLspInfoCommand_Type = CommandString
_GmplsLspInfoCommand_Object = MibTableColumn
gmplsLspInfoCommand = _GmplsLspInfoCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 28),
    _GmplsLspInfoCommand_Type()
)
gmplsLspInfoCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspInfoCommand.setStatus("current")
_GmplsLspReleaseCommand_Type = CommandString
_GmplsLspReleaseCommand_Object = MibTableColumn
gmplsLspReleaseCommand = _GmplsLspReleaseCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 29),
    _GmplsLspReleaseCommand_Type()
)
gmplsLspReleaseCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspReleaseCommand.setStatus("current")


class _GmplsLspDownLabel_Type(Unsigned32):
    """Custom type gmplsLspDownLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsLspDownLabel_Type.__name__ = "Unsigned32"
_GmplsLspDownLabel_Object = MibTableColumn
gmplsLspDownLabel = _GmplsLspDownLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 30),
    _GmplsLspDownLabel_Type()
)
gmplsLspDownLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspDownLabel.setStatus("current")
_GmplsLspLabelRequestType_Type = GmplsLabelRequestType
_GmplsLspLabelRequestType_Object = MibTableColumn
gmplsLspLabelRequestType = _GmplsLspLabelRequestType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 31),
    _GmplsLspLabelRequestType_Type()
)
gmplsLspLabelRequestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsLspLabelRequestType.setStatus("current")
_GmplsLspTSpecPeakRate_Type = GmplsBpsRate
_GmplsLspTSpecPeakRate_Object = MibTableColumn
gmplsLspTSpecPeakRate = _GmplsLspTSpecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 32),
    _GmplsLspTSpecPeakRate_Type()
)
gmplsLspTSpecPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsLspTSpecPeakRate.setStatus("current")
_GmplsLspTSpecAvgRate_Type = GmplsBpsRate
_GmplsLspTSpecAvgRate_Object = MibTableColumn
gmplsLspTSpecAvgRate = _GmplsLspTSpecAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 33),
    _GmplsLspTSpecAvgRate_Type()
)
gmplsLspTSpecAvgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsLspTSpecAvgRate.setStatus("current")
_GmplsLspLastErrorString_Type = DisplayString
_GmplsLspLastErrorString_Object = MibTableColumn
gmplsLspLastErrorString = _GmplsLspLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 34),
    _GmplsLspLastErrorString_Type()
)
gmplsLspLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspLastErrorString.setStatus("current")
_GmplsLspRouting_Type = GmplsRouting
_GmplsLspRouting_Object = MibTableColumn
gmplsLspRouting = _GmplsLspRouting_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 35),
    _GmplsLspRouting_Type()
)
gmplsLspRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspRouting.setStatus("current")
_GmplsLspCspfCommand_Type = CommandString
_GmplsLspCspfCommand_Object = MibTableColumn
gmplsLspCspfCommand = _GmplsLspCspfCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 36),
    _GmplsLspCspfCommand_Type()
)
gmplsLspCspfCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspCspfCommand.setStatus("current")
_GmplsLspSessionName_Type = DisplayString
_GmplsLspSessionName_Object = MibTableColumn
gmplsLspSessionName = _GmplsLspSessionName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 4, 1, 1, 37),
    _GmplsLspSessionName_Type()
)
gmplsLspSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLspSessionName.setStatus("current")
_GmplsTedList_ObjectIdentity = ObjectIdentity
gmplsTedList = _GmplsTedList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5)
)
_GmplsTedTable_Object = MibTable
gmplsTedTable = _GmplsTedTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1)
)
if mibBuilder.loadTexts:
    gmplsTedTable.setStatus("current")
_GmplsTedEntry_Object = MibTableRow
gmplsTedEntry = _GmplsTedEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1)
)
gmplsTedEntry.setIndexNames(
    (0, "LUM-GMPLS-MIB", "gmplsTedIndex"),
)
if mibBuilder.loadTexts:
    gmplsTedEntry.setStatus("current")


class _GmplsTedIndex_Type(Unsigned32):
    """Custom type gmplsTedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTedIndex_Type.__name__ = "Unsigned32"
_GmplsTedIndex_Object = MibTableColumn
gmplsTedIndex = _GmplsTedIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 1),
    _GmplsTedIndex_Type()
)
gmplsTedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedIndex.setStatus("current")
_GmplsTedName_Type = MgmtNameString
_GmplsTedName_Object = MibTableColumn
gmplsTedName = _GmplsTedName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 2),
    _GmplsTedName_Type()
)
gmplsTedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedName.setStatus("current")
_GmplsTedRouter_Type = MgmtNameString
_GmplsTedRouter_Object = MibTableColumn
gmplsTedRouter = _GmplsTedRouter_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 3),
    _GmplsTedRouter_Type()
)
gmplsTedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedRouter.setStatus("current")


class _GmplsTedLocalLinkId_Type(Unsigned32):
    """Custom type gmplsTedLocalLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTedLocalLinkId_Type.__name__ = "Unsigned32"
_GmplsTedLocalLinkId_Object = MibTableColumn
gmplsTedLocalLinkId = _GmplsTedLocalLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 4),
    _GmplsTedLocalLinkId_Type()
)
gmplsTedLocalLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedLocalLinkId.setStatus("current")
_GmplsTedRemoteIp_Type = DisplayString
_GmplsTedRemoteIp_Object = MibTableColumn
gmplsTedRemoteIp = _GmplsTedRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 5),
    _GmplsTedRemoteIp_Type()
)
gmplsTedRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedRemoteIp.setStatus("current")


class _GmplsTedRemoteLinkId_Type(Unsigned32):
    """Custom type gmplsTedRemoteLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTedRemoteLinkId_Type.__name__ = "Unsigned32"
_GmplsTedRemoteLinkId_Object = MibTableColumn
gmplsTedRemoteLinkId = _GmplsTedRemoteLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 6),
    _GmplsTedRemoteLinkId_Type()
)
gmplsTedRemoteLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedRemoteLinkId.setStatus("current")
_GmplsTedStatus_Type = GmplsConnectivity
_GmplsTedStatus_Object = MibTableColumn
gmplsTedStatus = _GmplsTedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 7),
    _GmplsTedStatus_Type()
)
gmplsTedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedStatus.setStatus("current")
_GmplsTedSwitchCapability_Type = GmplsSwitchCapability
_GmplsTedSwitchCapability_Object = MibTableColumn
gmplsTedSwitchCapability = _GmplsTedSwitchCapability_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 8),
    _GmplsTedSwitchCapability_Type()
)
gmplsTedSwitchCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedSwitchCapability.setStatus("current")
_GmplsTedEncoding_Type = GmplsEncodingStd
_GmplsTedEncoding_Object = MibTableColumn
gmplsTedEncoding = _GmplsTedEncoding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 9),
    _GmplsTedEncoding_Type()
)
gmplsTedEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedEncoding.setStatus("current")


class _GmplsTedMinBitRate_Type(Unsigned32):
    """Custom type gmplsTedMinBitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTedMinBitRate_Type.__name__ = "Unsigned32"
_GmplsTedMinBitRate_Object = MibTableColumn
gmplsTedMinBitRate = _GmplsTedMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 10),
    _GmplsTedMinBitRate_Type()
)
gmplsTedMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedMinBitRate.setStatus("current")


class _GmplsTedMaxBitRate_Type(Unsigned32):
    """Custom type gmplsTedMaxBitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTedMaxBitRate_Type.__name__ = "Unsigned32"
_GmplsTedMaxBitRate_Object = MibTableColumn
gmplsTedMaxBitRate = _GmplsTedMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 11),
    _GmplsTedMaxBitRate_Type()
)
gmplsTedMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedMaxBitRate.setStatus("current")


class _GmplsTedUnreserved_Type(Unsigned32):
    """Custom type gmplsTedUnreserved based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTedUnreserved_Type.__name__ = "Unsigned32"
_GmplsTedUnreserved_Object = MibTableColumn
gmplsTedUnreserved = _GmplsTedUnreserved_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 12),
    _GmplsTedUnreserved_Type()
)
gmplsTedUnreserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedUnreserved.setStatus("current")


class _GmplsTedProtectionType_Type(Unsigned32):
    """Custom type gmplsTedProtectionType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsTedProtectionType_Type.__name__ = "Unsigned32"
_GmplsTedProtectionType_Object = MibTableColumn
gmplsTedProtectionType = _GmplsTedProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 13),
    _GmplsTedProtectionType_Type()
)
gmplsTedProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedProtectionType.setStatus("current")


class _GmplsTedMetric_Type(Unsigned32):
    """Custom type gmplsTedMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GmplsTedMetric_Type.__name__ = "Unsigned32"
_GmplsTedMetric_Object = MibTableColumn
gmplsTedMetric = _GmplsTedMetric_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 14),
    _GmplsTedMetric_Type()
)
gmplsTedMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedMetric.setStatus("current")
_GmplsTedLocalIfIp_Type = MgmtNameString
_GmplsTedLocalIfIp_Object = MibTableColumn
gmplsTedLocalIfIp = _GmplsTedLocalIfIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 15),
    _GmplsTedLocalIfIp_Type()
)
gmplsTedLocalIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedLocalIfIp.setStatus("current")
_GmplsTedRemoteIfIp_Type = MgmtNameString
_GmplsTedRemoteIfIp_Object = MibTableColumn
gmplsTedRemoteIfIp = _GmplsTedRemoteIfIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 16),
    _GmplsTedRemoteIfIp_Type()
)
gmplsTedRemoteIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedRemoteIfIp.setStatus("current")
_GmplsTedType_Type = GmplsNumberedType
_GmplsTedType_Object = MibTableColumn
gmplsTedType = _GmplsTedType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 17),
    _GmplsTedType_Type()
)
gmplsTedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedType.setStatus("current")


class _GmplsTedColorClass_Type(Unsigned32):
    """Custom type gmplsTedColorClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GmplsTedColorClass_Type.__name__ = "Unsigned32"
_GmplsTedColorClass_Object = MibTableColumn
gmplsTedColorClass = _GmplsTedColorClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 18),
    _GmplsTedColorClass_Type()
)
gmplsTedColorClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedColorClass.setStatus("current")


class _GmplsTedSrlg_Type(Unsigned32):
    """Custom type gmplsTedSrlg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GmplsTedSrlg_Type.__name__ = "Unsigned32"
_GmplsTedSrlg_Object = MibTableColumn
gmplsTedSrlg = _GmplsTedSrlg_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 19),
    _GmplsTedSrlg_Type()
)
gmplsTedSrlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedSrlg.setStatus("current")
_GmplsTedInfoCommand_Type = CommandString
_GmplsTedInfoCommand_Object = MibTableColumn
gmplsTedInfoCommand = _GmplsTedInfoCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 20),
    _GmplsTedInfoCommand_Type()
)
gmplsTedInfoCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedInfoCommand.setStatus("current")


class _GmplsTedNoOfIscd_Type(Unsigned32):
    """Custom type gmplsTedNoOfIscd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GmplsTedNoOfIscd_Type.__name__ = "Unsigned32"
_GmplsTedNoOfIscd_Object = MibTableColumn
gmplsTedNoOfIscd = _GmplsTedNoOfIscd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 21),
    _GmplsTedNoOfIscd_Type()
)
gmplsTedNoOfIscd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedNoOfIscd.setStatus("current")
_GmplsTedFirstAnnounced_Type = DateAndTime
_GmplsTedFirstAnnounced_Object = MibTableColumn
gmplsTedFirstAnnounced = _GmplsTedFirstAnnounced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 22),
    _GmplsTedFirstAnnounced_Type()
)
gmplsTedFirstAnnounced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedFirstAnnounced.setStatus("current")
_GmplsTedLastRefresh_Type = DateAndTime
_GmplsTedLastRefresh_Object = MibTableColumn
gmplsTedLastRefresh = _GmplsTedLastRefresh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 23),
    _GmplsTedLastRefresh_Type()
)
gmplsTedLastRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedLastRefresh.setStatus("current")
_GmplsTedMinBitRateSym_Type = GmplsBpsRate
_GmplsTedMinBitRateSym_Object = MibTableColumn
gmplsTedMinBitRateSym = _GmplsTedMinBitRateSym_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 24),
    _GmplsTedMinBitRateSym_Type()
)
gmplsTedMinBitRateSym.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedMinBitRateSym.setStatus("current")
_GmplsTedMaxBitRateSym_Type = GmplsBpsRate
_GmplsTedMaxBitRateSym_Object = MibTableColumn
gmplsTedMaxBitRateSym = _GmplsTedMaxBitRateSym_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 25),
    _GmplsTedMaxBitRateSym_Type()
)
gmplsTedMaxBitRateSym.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedMaxBitRateSym.setStatus("current")
_GmplsTedUnreservedSym_Type = GmplsBpsRate
_GmplsTedUnreservedSym_Object = MibTableColumn
gmplsTedUnreservedSym = _GmplsTedUnreservedSym_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 5, 1, 1, 26),
    _GmplsTedUnreservedSym_Type()
)
gmplsTedUnreservedSym.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsTedUnreservedSym.setStatus("current")
_GmplsEroList_ObjectIdentity = ObjectIdentity
gmplsEroList = _GmplsEroList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 6)
)
_GmplsEroTable_Object = MibTable
gmplsEroTable = _GmplsEroTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 6, 1)
)
if mibBuilder.loadTexts:
    gmplsEroTable.setStatus("current")
_GmplsEroEntry_Object = MibTableRow
gmplsEroEntry = _GmplsEroEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 6, 1, 1)
)
gmplsEroEntry.setIndexNames(
    (0, "LUM-GMPLS-MIB", "gmplsEroIndex"),
)
if mibBuilder.loadTexts:
    gmplsEroEntry.setStatus("current")


class _GmplsEroIndex_Type(Unsigned32):
    """Custom type gmplsEroIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GmplsEroIndex_Type.__name__ = "Unsigned32"
_GmplsEroIndex_Object = MibTableColumn
gmplsEroIndex = _GmplsEroIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 6, 1, 1, 1),
    _GmplsEroIndex_Type()
)
gmplsEroIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsEroIndex.setStatus("current")
_GmplsEroName_Type = MgmtNameString
_GmplsEroName_Object = MibTableColumn
gmplsEroName = _GmplsEroName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 6, 1, 1, 2),
    _GmplsEroName_Type()
)
gmplsEroName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsEroName.setStatus("current")


class _GmplsEroType_Type(Integer32):
    """Custom type gmplsEroType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv4Label", 1),
          ("unnum", 2),
          ("unnumLabel", 3))
    )


_GmplsEroType_Type.__name__ = "Integer32"
_GmplsEroType_Object = MibTableColumn
gmplsEroType = _GmplsEroType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 6, 1, 1, 3),
    _GmplsEroType_Type()
)
gmplsEroType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsEroType.setStatus("current")
_GmplsEroAddress_Type = MgmtNameString
_GmplsEroAddress_Object = MibTableColumn
gmplsEroAddress = _GmplsEroAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 6, 1, 1, 4),
    _GmplsEroAddress_Type()
)
gmplsEroAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsEroAddress.setStatus("current")


class _GmplsEroInterfaceId_Type(Unsigned32):
    """Custom type gmplsEroInterfaceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GmplsEroInterfaceId_Type.__name__ = "Unsigned32"
_GmplsEroInterfaceId_Object = MibTableColumn
gmplsEroInterfaceId = _GmplsEroInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 6, 1, 1, 5),
    _GmplsEroInterfaceId_Type()
)
gmplsEroInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsEroInterfaceId.setStatus("current")


class _GmplsEroLabel_Type(Unsigned32):
    """Custom type gmplsEroLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GmplsEroLabel_Type.__name__ = "Unsigned32"
_GmplsEroLabel_Object = MibTableColumn
gmplsEroLabel = _GmplsEroLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 6, 1, 1, 6),
    _GmplsEroLabel_Type()
)
gmplsEroLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsEroLabel.setStatus("current")
_GmplsControl_ObjectIdentity = ObjectIdentity
gmplsControl = _GmplsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 7)
)


class _GmplsControlVerificationLevel_Type(Integer32):
    """Custom type gmplsControlVerificationLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("loose", 1),
          ("verifyHop", 2),
          ("verifyPath", 3),
          ("strict", 4))
    )


_GmplsControlVerificationLevel_Type.__name__ = "Integer32"
_GmplsControlVerificationLevel_Object = MibScalar
gmplsControlVerificationLevel = _GmplsControlVerificationLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 7, 1),
    _GmplsControlVerificationLevel_Type()
)
gmplsControlVerificationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsControlVerificationLevel.setStatus("current")


class _GmplsControlCCDelay_Type(Unsigned32):
    """Custom type gmplsControlCCDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_GmplsControlCCDelay_Type.__name__ = "Unsigned32"
_GmplsControlCCDelay_Object = MibScalar
gmplsControlCCDelay = _GmplsControlCCDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 7, 2),
    _GmplsControlCCDelay_Type()
)
gmplsControlCCDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsControlCCDelay.setStatus("current")


class _GmplsControlLspCleanupPolicy_Type(Integer32):
    """Custom type gmplsControlLspCleanupPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noClean", 0),
          ("cleanAtTear", 1),
          ("keepAtPathTear", 2),
          ("alwaysClean", 3))
    )


_GmplsControlLspCleanupPolicy_Type.__name__ = "Integer32"
_GmplsControlLspCleanupPolicy_Object = MibScalar
gmplsControlLspCleanupPolicy = _GmplsControlLspCleanupPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 7, 3),
    _GmplsControlLspCleanupPolicy_Type()
)
gmplsControlLspCleanupPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsControlLspCleanupPolicy.setStatus("current")
_GmplsControlOspfAreaId_Type = IpAddress
_GmplsControlOspfAreaId_Object = MibScalar
gmplsControlOspfAreaId = _GmplsControlOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 7, 4),
    _GmplsControlOspfAreaId_Type()
)
gmplsControlOspfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsControlOspfAreaId.setStatus("current")


class _GmplsControlRequestResvConfirm_Type(Integer32):
    """Custom type gmplsControlRequestResvConfirm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_GmplsControlRequestResvConfirm_Type.__name__ = "Integer32"
_GmplsControlRequestResvConfirm_Object = MibScalar
gmplsControlRequestResvConfirm = _GmplsControlRequestResvConfirm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 7, 5),
    _GmplsControlRequestResvConfirm_Type()
)
gmplsControlRequestResvConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsControlRequestResvConfirm.setStatus("current")


class _GmplsControlPathRefreshTimer_Type(Unsigned32):
    """Custom type gmplsControlPathRefreshTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_GmplsControlPathRefreshTimer_Type.__name__ = "Unsigned32"
_GmplsControlPathRefreshTimer_Object = MibScalar
gmplsControlPathRefreshTimer = _GmplsControlPathRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 7, 6),
    _GmplsControlPathRefreshTimer_Type()
)
gmplsControlPathRefreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsControlPathRefreshTimer.setStatus("current")


class _GmplsControlResvRefreshTimer_Type(Unsigned32):
    """Custom type gmplsControlResvRefreshTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_GmplsControlResvRefreshTimer_Type.__name__ = "Unsigned32"
_GmplsControlResvRefreshTimer_Object = MibScalar
gmplsControlResvRefreshTimer = _GmplsControlResvRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 7, 7),
    _GmplsControlResvRefreshTimer_Type()
)
gmplsControlResvRefreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmplsControlResvRefreshTimer.setStatus("current")
_LumentisGmplsNotifications_ObjectIdentity = ObjectIdentity
lumentisGmplsNotifications = _LumentisGmplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 8)
)
_GmplsNotifyPrefix_ObjectIdentity = ObjectIdentity
gmplsNotifyPrefix = _GmplsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 8, 0)
)

# Managed Objects groups

gmplsGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 1, 1)
)
gmplsGeneralGroup.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsGeneralLastChangeTime"),
        ("LUM-GMPLS-MIB", "gmplsGeneralStateLastChangeTime"),
        ("LUM-GMPLS-MIB", "gmplsGeneralGmplsTelinkTableSize"),
        ("LUM-GMPLS-MIB", "gmplsGeneralGmplsPhyslinkTableSize"),
        ("LUM-GMPLS-MIB", "gmplsGeneralGmplsEroTableSize"),
        ("LUM-GMPLS-MIB", "gmplsGeneralGmplsTedTableSize"),
        ("LUM-GMPLS-MIB", "gmplsGeneralGmplsLspTableSize"))
)
if mibBuilder.loadTexts:
    gmplsGeneralGroup.setStatus("current")

gmplsPhysLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 1, 2)
)
gmplsPhysLinkGroup.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsPhysLinkIndex"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkName"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkLinkId"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkType"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkResourceType"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkResourceId"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkEntityId"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkDirection"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkTeLinkCommand"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkTeState"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkSwitchCapability"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkEncoding"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkMinBitRate"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkMaxBitRate"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkInfoCommand"))
)
if mibBuilder.loadTexts:
    gmplsPhysLinkGroup.setStatus("current")

gmplsLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 1, 3)
)
gmplsLspGroup.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsLspIndex"),
        ("LUM-GMPLS-MIB", "gmplsLspName"),
        ("LUM-GMPLS-MIB", "gmplsLspDescr"),
        ("LUM-GMPLS-MIB", "gmplsLspLinkId"),
        ("LUM-GMPLS-MIB", "gmplsLspTunnelId"),
        ("LUM-GMPLS-MIB", "gmplsLspExTunnelId"),
        ("LUM-GMPLS-MIB", "gmplsLspIngressIp"),
        ("LUM-GMPLS-MIB", "gmplsLspIngressLinkId"),
        ("LUM-GMPLS-MIB", "gmplsLspEgressIp"),
        ("LUM-GMPLS-MIB", "gmplsLspEgressLinkId"),
        ("LUM-GMPLS-MIB", "gmplsLspUpLabel"),
        ("LUM-GMPLS-MIB", "gmplsLspUpstreamNeighbour"),
        ("LUM-GMPLS-MIB", "gmplsLspDownstreamNeighbour"),
        ("LUM-GMPLS-MIB", "gmplsLspState"),
        ("LUM-GMPLS-MIB", "gmplsLspRole"),
        ("LUM-GMPLS-MIB", "gmplsLspSessionId"),
        ("LUM-GMPLS-MIB", "gmplsLspEncoding"),
        ("LUM-GMPLS-MIB", "gmplsLspSwitchingType"),
        ("LUM-GMPLS-MIB", "gmplsLspLinkProtection"),
        ("LUM-GMPLS-MIB", "gmplsLspGPid"),
        ("LUM-GMPLS-MIB", "gmplsLspDirection"),
        ("LUM-GMPLS-MIB", "gmplsLspPathComputation"),
        ("LUM-GMPLS-MIB", "gmplsLspEroCommand"),
        ("LUM-GMPLS-MIB", "gmplsLspPathCommand"),
        ("LUM-GMPLS-MIB", "gmplsLspTearCommand"),
        ("LUM-GMPLS-MIB", "gmplsLspListCommand"),
        ("LUM-GMPLS-MIB", "gmplsLspInfoCommand"),
        ("LUM-GMPLS-MIB", "gmplsLspReleaseCommand"),
        ("LUM-GMPLS-MIB", "gmplsLspDownLabel"),
        ("LUM-GMPLS-MIB", "gmplsLspLabelRequestType"),
        ("LUM-GMPLS-MIB", "gmplsLspTSpecPeakRate"),
        ("LUM-GMPLS-MIB", "gmplsLspTSpecAvgRate"),
        ("LUM-GMPLS-MIB", "gmplsLspLastErrorString"),
        ("LUM-GMPLS-MIB", "gmplsLspRouting"),
        ("LUM-GMPLS-MIB", "gmplsLspCspfCommand"),
        ("LUM-GMPLS-MIB", "gmplsLspSessionName"))
)
if mibBuilder.loadTexts:
    gmplsLspGroup.setStatus("current")

gmplsTeLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 1, 5)
)
gmplsTeLinkGroup.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsTeLinkIndex"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkName"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkDescr"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkLocalLinkId"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkRemoteId"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkTxLinkId"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkRxLinkId"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkRemoteIp"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkAdminStatus"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkLspCommand"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkUsage"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkAvaliable"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkLabels"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkFreeLabels"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkLabelUsageMask"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkStatus"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkInfoCommand"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkAdmin"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkPresence"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkAlarm"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkSummary"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkLinkType"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkConnectCommand"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkPayload"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkMetric"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkColor"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkSrlg"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkModel"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkLocalIfIp"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkRemoteIfIp"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkPhysResourceId"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkRemotePhysResourceId"))
)
if mibBuilder.loadTexts:
    gmplsTeLinkGroup.setStatus("current")

gmplsTedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 1, 6)
)
gmplsTedGroup.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsTedIndex"),
        ("LUM-GMPLS-MIB", "gmplsTedName"),
        ("LUM-GMPLS-MIB", "gmplsTedRouter"),
        ("LUM-GMPLS-MIB", "gmplsTedLocalLinkId"),
        ("LUM-GMPLS-MIB", "gmplsTedRemoteIp"),
        ("LUM-GMPLS-MIB", "gmplsTedRemoteLinkId"),
        ("LUM-GMPLS-MIB", "gmplsTedStatus"),
        ("LUM-GMPLS-MIB", "gmplsTedLocalIfIp"),
        ("LUM-GMPLS-MIB", "gmplsTedRemoteIfIp"),
        ("LUM-GMPLS-MIB", "gmplsTedType"),
        ("LUM-GMPLS-MIB", "gmplsTedSwitchCapability"),
        ("LUM-GMPLS-MIB", "gmplsTedEncoding"),
        ("LUM-GMPLS-MIB", "gmplsTedMaxBitRate"),
        ("LUM-GMPLS-MIB", "gmplsTedMinBitRate"),
        ("LUM-GMPLS-MIB", "gmplsTedUnreserved"),
        ("LUM-GMPLS-MIB", "gmplsTedProtectionType"),
        ("LUM-GMPLS-MIB", "gmplsTedMetric"),
        ("LUM-GMPLS-MIB", "gmplsTedColorClass"),
        ("LUM-GMPLS-MIB", "gmplsTedSrlg"),
        ("LUM-GMPLS-MIB", "gmplsTedInfoCommand"),
        ("LUM-GMPLS-MIB", "gmplsTedNoOfIscd"),
        ("LUM-GMPLS-MIB", "gmplsTedFirstAnnounced"),
        ("LUM-GMPLS-MIB", "gmplsTedLastRefresh"),
        ("LUM-GMPLS-MIB", "gmplsTedMinBitRateSym"),
        ("LUM-GMPLS-MIB", "gmplsTedMaxBitRateSym"),
        ("LUM-GMPLS-MIB", "gmplsTedUnreservedSym"))
)
if mibBuilder.loadTexts:
    gmplsTedGroup.setStatus("current")

gmplsEroGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 1, 7)
)
gmplsEroGroup.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsEroIndex"),
        ("LUM-GMPLS-MIB", "gmplsEroName"),
        ("LUM-GMPLS-MIB", "gmplsEroType"),
        ("LUM-GMPLS-MIB", "gmplsEroAddress"),
        ("LUM-GMPLS-MIB", "gmplsEroInterfaceId"),
        ("LUM-GMPLS-MIB", "gmplsEroLabel"))
)
if mibBuilder.loadTexts:
    gmplsEroGroup.setStatus("current")

gmplsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 1, 8)
)
gmplsControlGroup.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsControlVerificationLevel"),
        ("LUM-GMPLS-MIB", "gmplsControlCCDelay"),
        ("LUM-GMPLS-MIB", "gmplsControlLspCleanupPolicy"),
        ("LUM-GMPLS-MIB", "gmplsControlOspfAreaId"),
        ("LUM-GMPLS-MIB", "gmplsControlRequestResvConfirm"),
        ("LUM-GMPLS-MIB", "gmplsControlPathRefreshTimer"),
        ("LUM-GMPLS-MIB", "gmplsControlResvRefreshTimer"))
)
if mibBuilder.loadTexts:
    gmplsControlGroup.setStatus("current")


# Notification objects

gmplsPhysLinkTxSignalStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 8, 0, 1)
)
gmplsPhysLinkTxSignalStatusDown.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsPhysLinkIndex"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkName"))
)
if mibBuilder.loadTexts:
    gmplsPhysLinkTxSignalStatusDown.setStatus(
        "current"
    )

gmplsPhysLinkTxSignalStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 2, 8, 0, 2)
)
gmplsPhysLinkTxSignalStatusUp.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsPhysLinkIndex"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkName"))
)
if mibBuilder.loadTexts:
    gmplsPhysLinkTxSignalStatusUp.setStatus(
        "current"
    )


# Notifications groups

gmplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 1, 4)
)
gmplsNotificationGroup.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsPhysLinkTxSignalStatusDown"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkTxSignalStatusUp"))
)
if mibBuilder.loadTexts:
    gmplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumGmplsBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24, 1, 2, 1)
)
lumGmplsBasicComplV1.setObjects(
      *(("LUM-GMPLS-MIB", "gmplsGeneralGroup"),
        ("LUM-GMPLS-MIB", "gmplsPhysLinkGroup"),
        ("LUM-GMPLS-MIB", "gmplsLspGroup"),
        ("LUM-GMPLS-MIB", "gmplsNotificationGroup"),
        ("LUM-GMPLS-MIB", "gmplsTeLinkGroup"),
        ("LUM-GMPLS-MIB", "gmplsTedGroup"),
        ("LUM-GMPLS-MIB", "gmplsEroGroup"),
        ("LUM-GMPLS-MIB", "gmplsControlGroup"))
)
if mibBuilder.loadTexts:
    lumGmplsBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-GMPLS-MIB",
    **{"GmplsLinkType": GmplsLinkType,
       "GmplsLinkDirType": GmplsLinkDirType,
       "GmplsSwitchCapability": GmplsSwitchCapability,
       "GmplsEncoding": GmplsEncoding,
       "GmplsEncodingStd": GmplsEncodingStd,
       "GmplsConnectivity": GmplsConnectivity,
       "GmplsLinkProtection": GmplsLinkProtection,
       "GmplsPayloadIdentifier": GmplsPayloadIdentifier,
       "GmplsDirection": GmplsDirection,
       "GmplsPathComputation": GmplsPathComputation,
       "GmplsNumberedType": GmplsNumberedType,
       "GmplsLabelRequestType": GmplsLabelRequestType,
       "GmplsBpsRate": GmplsBpsRate,
       "GmplsModel": GmplsModel,
       "GmplsRouting": GmplsRouting,
       "lumGmplsMIBModule": lumGmplsMIBModule,
       "lumGmplsConfs": lumGmplsConfs,
       "lumGmplsGroups": lumGmplsGroups,
       "gmplsGeneralGroup": gmplsGeneralGroup,
       "gmplsPhysLinkGroup": gmplsPhysLinkGroup,
       "gmplsLspGroup": gmplsLspGroup,
       "gmplsNotificationGroup": gmplsNotificationGroup,
       "gmplsTeLinkGroup": gmplsTeLinkGroup,
       "gmplsTedGroup": gmplsTedGroup,
       "gmplsEroGroup": gmplsEroGroup,
       "gmplsControlGroup": gmplsControlGroup,
       "lumGmplsCompl": lumGmplsCompl,
       "lumGmplsBasicComplV1": lumGmplsBasicComplV1,
       "lumGmplsMIBObjects": lumGmplsMIBObjects,
       "gmplsGeneral": gmplsGeneral,
       "gmplsGeneralLastChangeTime": gmplsGeneralLastChangeTime,
       "gmplsGeneralStateLastChangeTime": gmplsGeneralStateLastChangeTime,
       "gmplsGeneralGmplsTelinkTableSize": gmplsGeneralGmplsTelinkTableSize,
       "gmplsGeneralGmplsPhyslinkTableSize": gmplsGeneralGmplsPhyslinkTableSize,
       "gmplsGeneralGmplsEroTableSize": gmplsGeneralGmplsEroTableSize,
       "gmplsGeneralGmplsTedTableSize": gmplsGeneralGmplsTedTableSize,
       "gmplsGeneralGmplsLspTableSize": gmplsGeneralGmplsLspTableSize,
       "gmplsPhysLinkList": gmplsPhysLinkList,
       "gmplsPhysLinkTable": gmplsPhysLinkTable,
       "gmplsPhysLinkEntry": gmplsPhysLinkEntry,
       "gmplsPhysLinkIndex": gmplsPhysLinkIndex,
       "gmplsPhysLinkName": gmplsPhysLinkName,
       "gmplsPhysLinkDescr": gmplsPhysLinkDescr,
       "gmplsPhysLinkLinkId": gmplsPhysLinkLinkId,
       "gmplsPhysLinkType": gmplsPhysLinkType,
       "gmplsPhysLinkOwner": gmplsPhysLinkOwner,
       "gmplsPhysLinkResourceType": gmplsPhysLinkResourceType,
       "gmplsPhysLinkResourceId": gmplsPhysLinkResourceId,
       "gmplsPhysLinkEntityId": gmplsPhysLinkEntityId,
       "gmplsPhysLinkDirection": gmplsPhysLinkDirection,
       "gmplsPhysLinkTeLinkCommand": gmplsPhysLinkTeLinkCommand,
       "gmplsPhysLinkTeState": gmplsPhysLinkTeState,
       "gmplsPhysLinkSwitchCapability": gmplsPhysLinkSwitchCapability,
       "gmplsPhysLinkEncoding": gmplsPhysLinkEncoding,
       "gmplsPhysLinkMinBitRate": gmplsPhysLinkMinBitRate,
       "gmplsPhysLinkMaxBitRate": gmplsPhysLinkMaxBitRate,
       "gmplsPhysLinkInfoCommand": gmplsPhysLinkInfoCommand,
       "gmplsTeLinkList": gmplsTeLinkList,
       "gmplsTeLinkTable": gmplsTeLinkTable,
       "gmplsTeLinkEntry": gmplsTeLinkEntry,
       "gmplsTeLinkIndex": gmplsTeLinkIndex,
       "gmplsTeLinkName": gmplsTeLinkName,
       "gmplsTeLinkDescr": gmplsTeLinkDescr,
       "gmplsTeLinkLocalLinkId": gmplsTeLinkLocalLinkId,
       "gmplsTeLinkRemoteId": gmplsTeLinkRemoteId,
       "gmplsTeLinkTxLinkId": gmplsTeLinkTxLinkId,
       "gmplsTeLinkRxLinkId": gmplsTeLinkRxLinkId,
       "gmplsTeLinkRemoteIp": gmplsTeLinkRemoteIp,
       "gmplsTeLinkAdminStatus": gmplsTeLinkAdminStatus,
       "gmplsTeLinkOperStatus": gmplsTeLinkOperStatus,
       "gmplsTeLinkUsage": gmplsTeLinkUsage,
       "gmplsTeLinkLspCommand": gmplsTeLinkLspCommand,
       "gmplsTeLinkAvaliable": gmplsTeLinkAvaliable,
       "gmplsTeLinkRxAlarm": gmplsTeLinkRxAlarm,
       "gmplsTeLinkTxAlarm": gmplsTeLinkTxAlarm,
       "gmplsTeLinkLabels": gmplsTeLinkLabels,
       "gmplsTeLinkFreeLabels": gmplsTeLinkFreeLabels,
       "gmplsTeLinkLabelUsageMask": gmplsTeLinkLabelUsageMask,
       "gmplsTeLinkStatus": gmplsTeLinkStatus,
       "gmplsTeLinkInfoCommand": gmplsTeLinkInfoCommand,
       "gmplsTeLinkAdmin": gmplsTeLinkAdmin,
       "gmplsTeLinkPresence": gmplsTeLinkPresence,
       "gmplsTeLinkAlarm": gmplsTeLinkAlarm,
       "gmplsTeLinkSummary": gmplsTeLinkSummary,
       "gmplsTeLinkLinkType": gmplsTeLinkLinkType,
       "gmplsTeLinkConnectCommand": gmplsTeLinkConnectCommand,
       "gmplsTeLinkPayload": gmplsTeLinkPayload,
       "gmplsTeLinkMetric": gmplsTeLinkMetric,
       "gmplsTeLinkColor": gmplsTeLinkColor,
       "gmplsTeLinkSrlg": gmplsTeLinkSrlg,
       "gmplsTeLinkModel": gmplsTeLinkModel,
       "gmplsTeLinkLocalIfIp": gmplsTeLinkLocalIfIp,
       "gmplsTeLinkRemoteIfIp": gmplsTeLinkRemoteIfIp,
       "gmplsTeLinkPhysResourceId": gmplsTeLinkPhysResourceId,
       "gmplsTeLinkRemotePhysResourceId": gmplsTeLinkRemotePhysResourceId,
       "gmplsLspList": gmplsLspList,
       "gmplsLspTable": gmplsLspTable,
       "gmplsLspEntry": gmplsLspEntry,
       "gmplsLspIndex": gmplsLspIndex,
       "gmplsLspName": gmplsLspName,
       "gmplsLspDescr": gmplsLspDescr,
       "gmplsLspLinkId": gmplsLspLinkId,
       "gmplsLspTunnelId": gmplsLspTunnelId,
       "gmplsLspExTunnelId": gmplsLspExTunnelId,
       "gmplsLspIngressIp": gmplsLspIngressIp,
       "gmplsLspIngressLinkId": gmplsLspIngressLinkId,
       "gmplsLspEgressIp": gmplsLspEgressIp,
       "gmplsLspEgressLinkId": gmplsLspEgressLinkId,
       "gmplsLspUpLabel": gmplsLspUpLabel,
       "gmplsLspUpstreamNeighbour": gmplsLspUpstreamNeighbour,
       "gmplsLspDownstreamNeighbour": gmplsLspDownstreamNeighbour,
       "gmplsLspState": gmplsLspState,
       "gmplsLspSessionId": gmplsLspSessionId,
       "gmplsLspRole": gmplsLspRole,
       "gmplsLspEroList": gmplsLspEroList,
       "gmplsLspEncoding": gmplsLspEncoding,
       "gmplsLspSwitchingType": gmplsLspSwitchingType,
       "gmplsLspLinkProtection": gmplsLspLinkProtection,
       "gmplsLspGPid": gmplsLspGPid,
       "gmplsLspDirection": gmplsLspDirection,
       "gmplsLspPathComputation": gmplsLspPathComputation,
       "gmplsLspEroCommand": gmplsLspEroCommand,
       "gmplsLspPathCommand": gmplsLspPathCommand,
       "gmplsLspTearCommand": gmplsLspTearCommand,
       "gmplsLspListCommand": gmplsLspListCommand,
       "gmplsLspInfoCommand": gmplsLspInfoCommand,
       "gmplsLspReleaseCommand": gmplsLspReleaseCommand,
       "gmplsLspDownLabel": gmplsLspDownLabel,
       "gmplsLspLabelRequestType": gmplsLspLabelRequestType,
       "gmplsLspTSpecPeakRate": gmplsLspTSpecPeakRate,
       "gmplsLspTSpecAvgRate": gmplsLspTSpecAvgRate,
       "gmplsLspLastErrorString": gmplsLspLastErrorString,
       "gmplsLspRouting": gmplsLspRouting,
       "gmplsLspCspfCommand": gmplsLspCspfCommand,
       "gmplsLspSessionName": gmplsLspSessionName,
       "gmplsTedList": gmplsTedList,
       "gmplsTedTable": gmplsTedTable,
       "gmplsTedEntry": gmplsTedEntry,
       "gmplsTedIndex": gmplsTedIndex,
       "gmplsTedName": gmplsTedName,
       "gmplsTedRouter": gmplsTedRouter,
       "gmplsTedLocalLinkId": gmplsTedLocalLinkId,
       "gmplsTedRemoteIp": gmplsTedRemoteIp,
       "gmplsTedRemoteLinkId": gmplsTedRemoteLinkId,
       "gmplsTedStatus": gmplsTedStatus,
       "gmplsTedSwitchCapability": gmplsTedSwitchCapability,
       "gmplsTedEncoding": gmplsTedEncoding,
       "gmplsTedMinBitRate": gmplsTedMinBitRate,
       "gmplsTedMaxBitRate": gmplsTedMaxBitRate,
       "gmplsTedUnreserved": gmplsTedUnreserved,
       "gmplsTedProtectionType": gmplsTedProtectionType,
       "gmplsTedMetric": gmplsTedMetric,
       "gmplsTedLocalIfIp": gmplsTedLocalIfIp,
       "gmplsTedRemoteIfIp": gmplsTedRemoteIfIp,
       "gmplsTedType": gmplsTedType,
       "gmplsTedColorClass": gmplsTedColorClass,
       "gmplsTedSrlg": gmplsTedSrlg,
       "gmplsTedInfoCommand": gmplsTedInfoCommand,
       "gmplsTedNoOfIscd": gmplsTedNoOfIscd,
       "gmplsTedFirstAnnounced": gmplsTedFirstAnnounced,
       "gmplsTedLastRefresh": gmplsTedLastRefresh,
       "gmplsTedMinBitRateSym": gmplsTedMinBitRateSym,
       "gmplsTedMaxBitRateSym": gmplsTedMaxBitRateSym,
       "gmplsTedUnreservedSym": gmplsTedUnreservedSym,
       "gmplsEroList": gmplsEroList,
       "gmplsEroTable": gmplsEroTable,
       "gmplsEroEntry": gmplsEroEntry,
       "gmplsEroIndex": gmplsEroIndex,
       "gmplsEroName": gmplsEroName,
       "gmplsEroType": gmplsEroType,
       "gmplsEroAddress": gmplsEroAddress,
       "gmplsEroInterfaceId": gmplsEroInterfaceId,
       "gmplsEroLabel": gmplsEroLabel,
       "gmplsControl": gmplsControl,
       "gmplsControlVerificationLevel": gmplsControlVerificationLevel,
       "gmplsControlCCDelay": gmplsControlCCDelay,
       "gmplsControlLspCleanupPolicy": gmplsControlLspCleanupPolicy,
       "gmplsControlOspfAreaId": gmplsControlOspfAreaId,
       "gmplsControlRequestResvConfirm": gmplsControlRequestResvConfirm,
       "gmplsControlPathRefreshTimer": gmplsControlPathRefreshTimer,
       "gmplsControlResvRefreshTimer": gmplsControlResvRefreshTimer,
       "lumentisGmplsNotifications": lumentisGmplsNotifications,
       "gmplsNotifyPrefix": gmplsNotifyPrefix,
       "gmplsPhysLinkTxSignalStatusDown": gmplsPhysLinkTxSignalStatusDown,
       "gmplsPhysLinkTxSignalStatusUp": gmplsPhysLinkTxSignalStatusUp}
)
