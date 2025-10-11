# SNMP MIB module (ADTRAN-SHDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-SHDSL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:20 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenEShdsl,
 adGenEShdslID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-SHDSL-MIB",
    "adGenEShdsl",
    "adGenEShdslID")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenEShdslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 59, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEShdslMIB.setRevisions(
        ("2019-10-11 00:00",
         "2012-09-24 00:00",
         "2012-09-13 00:00",
         "2012-07-31 00:00",
         "2012-07-11 00:00",
         "2011-08-22 00:00",
         "2011-06-02 13:38",
         "2011-04-26 15:16",
         "2011-04-25 09:25",
         "2011-04-18 00:00",
         "2011-04-13 14:28",
         "2011-04-04 15:21",
         "2011-03-29 14:20",
         "2011-03-24 00:00",
         "2011-02-22 00:00",
         "2010-02-12 00:00",
         "2007-04-06 00:00")
    )


# Types definitions



class AdEShdslUnitId(Integer32):
    """Custom type AdEShdslUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ltu", 1),
          ("ntu", 2),
          ("xru1", 3),
          ("xru2", 4),
          ("xru3", 5),
          ("xru4", 6),
          ("xru5", 7),
          ("xru6", 8),
          ("xru7", 9),
          ("xru8", 10))
    )





class AdEShdslUnitSide(Integer32):
    """Custom type AdEShdslUnitSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkSide", 1),
          ("customerSide", 2))
    )





class AdEShdslWirePair(Integer32):
    """Custom type AdEShdslWirePair based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wirePair1", 1),
          ("wirePair2", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdEShdslIndex_ObjectIdentity = ObjectIdentity
adEShdslIndex = _AdEShdslIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 1)
)
_AdEShdslIndexTable_Object = MibTable
adEShdslIndexTable = _AdEShdslIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adEShdslIndexTable.setStatus("current")
_AdEShdslIndexEntry_Object = MibTableRow
adEShdslIndexEntry = _AdEShdslIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 1, 1, 1)
)
adEShdslIndexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
)
if mibBuilder.loadTexts:
    adEShdslIndexEntry.setStatus("current")
_AdEShdslInvIndex_Type = AdEShdslUnitId
_AdEShdslInvIndex_Object = MibTableColumn
adEShdslInvIndex = _AdEShdslInvIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 1, 1, 1, 1),
    _AdEShdslInvIndex_Type()
)
adEShdslInvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvIndex.setStatus("current")
_AdEShdslSideIndex_Type = AdEShdslUnitSide
_AdEShdslSideIndex_Object = MibTableColumn
adEShdslSideIndex = _AdEShdslSideIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 1, 1, 1, 2),
    _AdEShdslSideIndex_Type()
)
adEShdslSideIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSideIndex.setStatus("current")
_AdEShdslWirePairIndex_Type = AdEShdslWirePair
_AdEShdslWirePairIndex_Object = MibTableColumn
adEShdslWirePairIndex = _AdEShdslWirePairIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 1, 1, 1, 3),
    _AdEShdslWirePairIndex_Type()
)
adEShdslWirePairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslWirePairIndex.setStatus("current")
_AdEShdslInventory_ObjectIdentity = ObjectIdentity
adEShdslInventory = _AdEShdslInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2)
)
_AdEShdslInventoryTable_Object = MibTable
adEShdslInventoryTable = _AdEShdslInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adEShdslInventoryTable.setStatus("current")
_AdEShdslInventoryEntry_Object = MibTableRow
adEShdslInventoryEntry = _AdEShdslInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1)
)
adEShdslInventoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
)
if mibBuilder.loadTexts:
    adEShdslInventoryEntry.setStatus("current")


class _AdEShdslInvVendorID_Type(OctetString):
    """Custom type adEShdslInvVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AdEShdslInvVendorID_Type.__name__ = "OctetString"
_AdEShdslInvVendorID_Object = MibTableColumn
adEShdslInvVendorID = _AdEShdslInvVendorID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 1),
    _AdEShdslInvVendorID_Type()
)
adEShdslInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvVendorID.setStatus("current")


class _AdEShdslInvVendorModelNumber_Type(OctetString):
    """Custom type adEShdslInvVendorModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_AdEShdslInvVendorModelNumber_Type.__name__ = "OctetString"
_AdEShdslInvVendorModelNumber_Object = MibTableColumn
adEShdslInvVendorModelNumber = _AdEShdslInvVendorModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 2),
    _AdEShdslInvVendorModelNumber_Type()
)
adEShdslInvVendorModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvVendorModelNumber.setStatus("current")


class _AdEShdslInvVendorSerialNumber_Type(OctetString):
    """Custom type adEShdslInvVendorSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )
    fixed_length = 25


_AdEShdslInvVendorSerialNumber_Type.__name__ = "OctetString"
_AdEShdslInvVendorSerialNumber_Object = MibTableColumn
adEShdslInvVendorSerialNumber = _AdEShdslInvVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 3),
    _AdEShdslInvVendorSerialNumber_Type()
)
adEShdslInvVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvVendorSerialNumber.setStatus("current")
_AdEShdslInvStandardVersion_Type = Integer32
_AdEShdslInvStandardVersion_Object = MibTableColumn
adEShdslInvStandardVersion = _AdEShdslInvStandardVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 4),
    _AdEShdslInvStandardVersion_Type()
)
adEShdslInvStandardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvStandardVersion.setStatus("current")


class _AdEShdslInvVendorListNumber_Type(OctetString):
    """Custom type adEShdslInvVendorListNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_AdEShdslInvVendorListNumber_Type.__name__ = "OctetString"
_AdEShdslInvVendorListNumber_Object = MibTableColumn
adEShdslInvVendorListNumber = _AdEShdslInvVendorListNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 5),
    _AdEShdslInvVendorListNumber_Type()
)
adEShdslInvVendorListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvVendorListNumber.setStatus("current")


class _AdEShdslInvVendorIssueNumber_Type(OctetString):
    """Custom type adEShdslInvVendorIssueNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AdEShdslInvVendorIssueNumber_Type.__name__ = "OctetString"
_AdEShdslInvVendorIssueNumber_Object = MibTableColumn
adEShdslInvVendorIssueNumber = _AdEShdslInvVendorIssueNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 6),
    _AdEShdslInvVendorIssueNumber_Type()
)
adEShdslInvVendorIssueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvVendorIssueNumber.setStatus("current")


class _AdEShdslInvVendorSoftwareVersion_Type(OctetString):
    """Custom type adEShdslInvVendorSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AdEShdslInvVendorSoftwareVersion_Type.__name__ = "OctetString"
_AdEShdslInvVendorSoftwareVersion_Object = MibTableColumn
adEShdslInvVendorSoftwareVersion = _AdEShdslInvVendorSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 7),
    _AdEShdslInvVendorSoftwareVersion_Type()
)
adEShdslInvVendorSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvVendorSoftwareVersion.setStatus("current")


class _AdEShdslInvEquipmentCode_Type(OctetString):
    """Custom type adEShdslInvEquipmentCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_AdEShdslInvEquipmentCode_Type.__name__ = "OctetString"
_AdEShdslInvEquipmentCode_Object = MibTableColumn
adEShdslInvEquipmentCode = _AdEShdslInvEquipmentCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 8),
    _AdEShdslInvEquipmentCode_Type()
)
adEShdslInvEquipmentCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvEquipmentCode.setStatus("current")


class _AdEShdslInvVendorOther_Type(OctetString):
    """Custom type adEShdslInvVendorOther based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_AdEShdslInvVendorOther_Type.__name__ = "OctetString"
_AdEShdslInvVendorOther_Object = MibTableColumn
adEShdslInvVendorOther = _AdEShdslInvVendorOther_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 9),
    _AdEShdslInvVendorOther_Type()
)
adEShdslInvVendorOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvVendorOther.setStatus("current")
_AdEShdslInvVendorEOCSoftwareVersion_Type = Integer32
_AdEShdslInvVendorEOCSoftwareVersion_Object = MibTableColumn
adEShdslInvVendorEOCSoftwareVersion = _AdEShdslInvVendorEOCSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 10),
    _AdEShdslInvVendorEOCSoftwareVersion_Type()
)
adEShdslInvVendorEOCSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvVendorEOCSoftwareVersion.setStatus("current")
_AdEShdslInvMfrDate_Type = DisplayString
_AdEShdslInvMfrDate_Object = MibTableColumn
adEShdslInvMfrDate = _AdEShdslInvMfrDate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 11),
    _AdEShdslInvMfrDate_Type()
)
adEShdslInvMfrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvMfrDate.setStatus("current")
_AdEShdslInvCircuitID_Type = DisplayString
_AdEShdslInvCircuitID_Object = MibTableColumn
adEShdslInvCircuitID = _AdEShdslInvCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 12),
    _AdEShdslInvCircuitID_Type()
)
adEShdslInvCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslInvCircuitID.setStatus("current")
_AdEShdslInvScratchPad_Type = DisplayString
_AdEShdslInvScratchPad_Object = MibTableColumn
adEShdslInvScratchPad = _AdEShdslInvScratchPad_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 13),
    _AdEShdslInvScratchPad_Type()
)
adEShdslInvScratchPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslInvScratchPad.setStatus("current")
_AdEShdslInvDspHwVersion_Type = DisplayString
_AdEShdslInvDspHwVersion_Object = MibTableColumn
adEShdslInvDspHwVersion = _AdEShdslInvDspHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 14),
    _AdEShdslInvDspHwVersion_Type()
)
adEShdslInvDspHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvDspHwVersion.setStatus("current")
_AdEShdslInvDspFwVersion_Type = DisplayString
_AdEShdslInvDspFwVersion_Object = MibTableColumn
adEShdslInvDspFwVersion = _AdEShdslInvDspFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 15),
    _AdEShdslInvDspFwVersion_Type()
)
adEShdslInvDspFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvDspFwVersion.setStatus("current")
_AdEShdslInvElementPresent_Type = TruthValue
_AdEShdslInvElementPresent_Object = MibTableColumn
adEShdslInvElementPresent = _AdEShdslInvElementPresent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 16),
    _AdEShdslInvElementPresent_Type()
)
adEShdslInvElementPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvElementPresent.setStatus("current")
_AdEShdslInvPhysicalLinkId_Type = Integer32
_AdEShdslInvPhysicalLinkId_Object = MibTableColumn
adEShdslInvPhysicalLinkId = _AdEShdslInvPhysicalLinkId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 2, 1, 1, 17),
    _AdEShdslInvPhysicalLinkId_Type()
)
adEShdslInvPhysicalLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslInvPhysicalLinkId.setStatus("current")
_AdEShdslProvisioning_ObjectIdentity = ObjectIdentity
adEShdslProvisioning = _AdEShdslProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3)
)
_AdEShdslProvTable_Object = MibTable
adEShdslProvTable = _AdEShdslProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adEShdslProvTable.setStatus("current")
_AdEShdslProvEntry_Object = MibTableRow
adEShdslProvEntry = _AdEShdslProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1)
)
adEShdslProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adEShdslProvEntry.setStatus("current")


class _AdEShdslProvWireInterfaceMode_Type(Integer32):
    """Custom type adEShdslProvWireInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoWire", 1),
          ("fourWire", 2))
    )


_AdEShdslProvWireInterfaceMode_Type.__name__ = "Integer32"
_AdEShdslProvWireInterfaceMode_Object = MibTableColumn
adEShdslProvWireInterfaceMode = _AdEShdslProvWireInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 1),
    _AdEShdslProvWireInterfaceMode_Type()
)
adEShdslProvWireInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvWireInterfaceMode.setStatus("current")
_AdEShdslProvMinLineRate_Type = Integer32
_AdEShdslProvMinLineRate_Object = MibTableColumn
adEShdslProvMinLineRate = _AdEShdslProvMinLineRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 2),
    _AdEShdslProvMinLineRate_Type()
)
adEShdslProvMinLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvMinLineRate.setStatus("current")
_AdEShdslProvMaxLineRate_Type = Integer32
_AdEShdslProvMaxLineRate_Object = MibTableColumn
adEShdslProvMaxLineRate = _AdEShdslProvMaxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 3),
    _AdEShdslProvMaxLineRate_Type()
)
adEShdslProvMaxLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvMaxLineRate.setStatus("current")


class _AdEShdslProvG9912Annex_Type(Integer32):
    """Custom type adEShdslProvG9912Annex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexB", 2),
          ("annexAorB", 3),
          ("efm", 4),
          ("annexAorEfm", 5),
          ("annexBorEfm", 6),
          ("annexAorBorEfm", 7))
    )


_AdEShdslProvG9912Annex_Type.__name__ = "Integer32"
_AdEShdslProvG9912Annex_Object = MibTableColumn
adEShdslProvG9912Annex = _AdEShdslProvG9912Annex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 4),
    _AdEShdslProvG9912Annex_Type()
)
adEShdslProvG9912Annex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvG9912Annex.setStatus("current")
_AdEShdslProvCurrCondTargetMargin_Type = Integer32
_AdEShdslProvCurrCondTargetMargin_Object = MibTableColumn
adEShdslProvCurrCondTargetMargin = _AdEShdslProvCurrCondTargetMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 5),
    _AdEShdslProvCurrCondTargetMargin_Type()
)
adEShdslProvCurrCondTargetMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvCurrCondTargetMargin.setStatus("current")
_AdEShdslProvWorstCaseTargetMargin_Type = Integer32
_AdEShdslProvWorstCaseTargetMargin_Object = MibTableColumn
adEShdslProvWorstCaseTargetMargin = _AdEShdslProvWorstCaseTargetMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 6),
    _AdEShdslProvWorstCaseTargetMargin_Type()
)
adEShdslProvWorstCaseTargetMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvWorstCaseTargetMargin.setStatus("current")


class _AdEShdslProvUsedTargetMargins_Type(Integer32):
    """Custom type adEShdslProvUsedTargetMargins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currCond", 1),
          ("worstCase", 2))
    )


_AdEShdslProvUsedTargetMargins_Type.__name__ = "Integer32"
_AdEShdslProvUsedTargetMargins_Object = MibTableColumn
adEShdslProvUsedTargetMargins = _AdEShdslProvUsedTargetMargins_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 7),
    _AdEShdslProvUsedTargetMargins_Type()
)
adEShdslProvUsedTargetMargins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslProvUsedTargetMargins.setStatus("current")


class _AdEShdslProvClockMode_Type(Integer32):
    """Custom type adEShdslProvClockMode based on Integer32"""
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
        *(("clockMode1", 1),
          ("clockMode2", 2),
          ("clockMode3a", 3),
          ("clockMode3b", 4))
    )


_AdEShdslProvClockMode_Type.__name__ = "Integer32"
_AdEShdslProvClockMode_Object = MibTableColumn
adEShdslProvClockMode = _AdEShdslProvClockMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 8),
    _AdEShdslProvClockMode_Type()
)
adEShdslProvClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvClockMode.setStatus("current")


class _AdEShdslProvLineProbing_Type(Integer32):
    """Custom type adEShdslProvLineProbing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableCurrCond", 2),
          ("enableWorseCase", 3),
          ("enableANFP", 4),
          ("enableMaxRate", 5),
          ("enableT1417", 6),
          ("enableG9912", 7),
          ("enableG9912nl", 8),
          ("disableLineProbeEnableExtFixed", 9),
          ("enableANFPWorstCase", 10),
          ("enableANFPCurrentCond", 11))
    )


_AdEShdslProvLineProbing_Type.__name__ = "Integer32"
_AdEShdslProvLineProbing_Object = MibTableColumn
adEShdslProvLineProbing = _AdEShdslProvLineProbing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 9),
    _AdEShdslProvLineProbing_Type()
)
adEShdslProvLineProbing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvLineProbing.setStatus("current")


class _AdEShdslProvConstellation_Type(Integer32):
    """Custom type adEShdslProvConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcpam16", 1),
          ("tcpam32", 2))
    )


_AdEShdslProvConstellation_Type.__name__ = "Integer32"
_AdEShdslProvConstellation_Object = MibTableColumn
adEShdslProvConstellation = _AdEShdslProvConstellation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 10),
    _AdEShdslProvConstellation_Type()
)
adEShdslProvConstellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvConstellation.setStatus("current")
_AdEShdslProvPowerBackoff_Type = Integer32
_AdEShdslProvPowerBackoff_Object = MibTableColumn
adEShdslProvPowerBackoff = _AdEShdslProvPowerBackoff_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 11),
    _AdEShdslProvPowerBackoff_Type()
)
adEShdslProvPowerBackoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvPowerBackoff.setStatus("current")
_AdEShdslProvName_Type = DisplayString
_AdEShdslProvName_Object = MibTableColumn
adEShdslProvName = _AdEShdslProvName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 12),
    _AdEShdslProvName_Type()
)
adEShdslProvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvName.setStatus("current")


class _AdEShdslProvSpanPower_Type(Integer32):
    """Custom type adEShdslProvSpanPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdEShdslProvSpanPower_Type.__name__ = "Integer32"
_AdEShdslProvSpanPower_Object = MibTableColumn
adEShdslProvSpanPower = _AdEShdslProvSpanPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 13),
    _AdEShdslProvSpanPower_Type()
)
adEShdslProvSpanPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvSpanPower.setStatus("current")


class _AdEShdslProvNIUloopback_Type(Integer32):
    """Custom type adEShdslProvNIUloopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdEShdslProvNIUloopback_Type.__name__ = "Integer32"
_AdEShdslProvNIUloopback_Object = MibTableColumn
adEShdslProvNIUloopback = _AdEShdslProvNIUloopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 14),
    _AdEShdslProvNIUloopback_Type()
)
adEShdslProvNIUloopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvNIUloopback.setStatus("current")
_AdEShdslProvConstellationCrossoverRate_Type = Integer32
_AdEShdslProvConstellationCrossoverRate_Object = MibTableColumn
adEShdslProvConstellationCrossoverRate = _AdEShdslProvConstellationCrossoverRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 15),
    _AdEShdslProvConstellationCrossoverRate_Type()
)
adEShdslProvConstellationCrossoverRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvConstellationCrossoverRate.setStatus("current")
_AdEShdslProvAnfp100KhzLoss_Type = Integer32
_AdEShdslProvAnfp100KhzLoss_Object = MibTableColumn
adEShdslProvAnfp100KhzLoss = _AdEShdslProvAnfp100KhzLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 16),
    _AdEShdslProvAnfp100KhzLoss_Type()
)
adEShdslProvAnfp100KhzLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvAnfp100KhzLoss.setStatus("current")
_AdEShdslProvAnfpTargetMargin_Type = Integer32
_AdEShdslProvAnfpTargetMargin_Object = MibTableColumn
adEShdslProvAnfpTargetMargin = _AdEShdslProvAnfpTargetMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 17),
    _AdEShdslProvAnfpTargetMargin_Type()
)
adEShdslProvAnfpTargetMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvAnfpTargetMargin.setStatus("current")


class _AdEShdslProvEmergencyFreeze_Type(Integer32):
    """Custom type adEShdslProvEmergencyFreeze based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdEShdslProvEmergencyFreeze_Type.__name__ = "Integer32"
_AdEShdslProvEmergencyFreeze_Object = MibTableColumn
adEShdslProvEmergencyFreeze = _AdEShdslProvEmergencyFreeze_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 18),
    _AdEShdslProvEmergencyFreeze_Type()
)
adEShdslProvEmergencyFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvEmergencyFreeze.setStatus("current")


class _AdEShdslProvExtendedFixedRateAndConstellation_Type(OctetString):
    """Custom type adEShdslProvExtendedFixedRateAndConstellation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AdEShdslProvExtendedFixedRateAndConstellation_Type.__name__ = "OctetString"
_AdEShdslProvExtendedFixedRateAndConstellation_Object = MibTableColumn
adEShdslProvExtendedFixedRateAndConstellation = _AdEShdslProvExtendedFixedRateAndConstellation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 19),
    _AdEShdslProvExtendedFixedRateAndConstellation_Type()
)
adEShdslProvExtendedFixedRateAndConstellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvExtendedFixedRateAndConstellation.setStatus("current")
_AdEShdslProvExtendedFixedLastError_Type = DisplayString
_AdEShdslProvExtendedFixedLastError_Object = MibTableColumn
adEShdslProvExtendedFixedLastError = _AdEShdslProvExtendedFixedLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 20),
    _AdEShdslProvExtendedFixedLastError_Type()
)
adEShdslProvExtendedFixedLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslProvExtendedFixedLastError.setStatus("current")


class _AdEShdslProvAnfp100KhzLossLetter_Type(Integer32):
    """Custom type adEShdslProvAnfp100KhzLossLetter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ultrashortU", 1),
          ("extrashortX", 2),
          ("shortS", 3),
          ("mediumM", 4),
          ("longL", 5))
    )


_AdEShdslProvAnfp100KhzLossLetter_Type.__name__ = "Integer32"
_AdEShdslProvAnfp100KhzLossLetter_Object = MibTableColumn
adEShdslProvAnfp100KhzLossLetter = _AdEShdslProvAnfp100KhzLossLetter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 21),
    _AdEShdslProvAnfp100KhzLossLetter_Type()
)
adEShdslProvAnfp100KhzLossLetter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvAnfp100KhzLossLetter.setStatus("current")
_AdEShdslProvAnfpMaxLineRate_Type = Integer32
_AdEShdslProvAnfpMaxLineRate_Object = MibTableColumn
adEShdslProvAnfpMaxLineRate = _AdEShdslProvAnfpMaxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 22),
    _AdEShdslProvAnfpMaxLineRate_Type()
)
adEShdslProvAnfpMaxLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvAnfpMaxLineRate.setStatus("current")
_AdEShdslProvSCIAlarmThresh_Type = Integer32
_AdEShdslProvSCIAlarmThresh_Object = MibTableColumn
adEShdslProvSCIAlarmThresh = _AdEShdslProvSCIAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 23),
    _AdEShdslProvSCIAlarmThresh_Type()
)
adEShdslProvSCIAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvSCIAlarmThresh.setStatus("current")


class _AdEShdslProvSCIAlarmSeverity_Type(Integer32):
    """Custom type adEShdslProvSCIAlarmSeverity based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdEShdslProvSCIAlarmSeverity_Type.__name__ = "Integer32"
_AdEShdslProvSCIAlarmSeverity_Object = MibTableColumn
adEShdslProvSCIAlarmSeverity = _AdEShdslProvSCIAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 1, 1, 24),
    _AdEShdslProvSCIAlarmSeverity_Type()
)
adEShdslProvSCIAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslProvSCIAlarmSeverity.setStatus("current")
_AdEShdslAlarmProvTable_Object = MibTable
adEShdslAlarmProvTable = _AdEShdslAlarmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2)
)
if mibBuilder.loadTexts:
    adEShdslAlarmProvTable.setStatus("current")
_AdEShdslAlarmProvEntry_Object = MibTableRow
adEShdslAlarmProvEntry = _AdEShdslAlarmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1)
)
adEShdslAlarmProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
)
if mibBuilder.loadTexts:
    adEShdslAlarmProvEntry.setStatus("current")
_AdEShdslAlarmProvLoopAttenThresh_Type = Integer32
_AdEShdslAlarmProvLoopAttenThresh_Object = MibTableColumn
adEShdslAlarmProvLoopAttenThresh = _AdEShdslAlarmProvLoopAttenThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 1),
    _AdEShdslAlarmProvLoopAttenThresh_Type()
)
adEShdslAlarmProvLoopAttenThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvLoopAttenThresh.setStatus("current")
_AdEShdslAlarmProvSNRMarginThresh_Type = Integer32
_AdEShdslAlarmProvSNRMarginThresh_Object = MibTableColumn
adEShdslAlarmProvSNRMarginThresh = _AdEShdslAlarmProvSNRMarginThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 2),
    _AdEShdslAlarmProvSNRMarginThresh_Type()
)
adEShdslAlarmProvSNRMarginThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvSNRMarginThresh.setStatus("current")
_AdEShdslAlarmProvESThresh_Type = Integer32
_AdEShdslAlarmProvESThresh_Object = MibTableColumn
adEShdslAlarmProvESThresh = _AdEShdslAlarmProvESThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 3),
    _AdEShdslAlarmProvESThresh_Type()
)
adEShdslAlarmProvESThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvESThresh.setStatus("current")
_AdEShdslAlarmProvSESThresh_Type = Integer32
_AdEShdslAlarmProvSESThresh_Object = MibTableColumn
adEShdslAlarmProvSESThresh = _AdEShdslAlarmProvSESThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 4),
    _AdEShdslAlarmProvSESThresh_Type()
)
adEShdslAlarmProvSESThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvSESThresh.setStatus("current")
_AdEShdslAlarmProvUASThresh_Type = Integer32
_AdEShdslAlarmProvUASThresh_Object = MibTableColumn
adEShdslAlarmProvUASThresh = _AdEShdslAlarmProvUASThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 5),
    _AdEShdslAlarmProvUASThresh_Type()
)
adEShdslAlarmProvUASThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvUASThresh.setStatus("current")
_AdEShdslAlarmProvCVCThresh_Type = Integer32
_AdEShdslAlarmProvCVCThresh_Object = MibTableColumn
adEShdslAlarmProvCVCThresh = _AdEShdslAlarmProvCVCThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 6),
    _AdEShdslAlarmProvCVCThresh_Type()
)
adEShdslAlarmProvCVCThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvCVCThresh.setStatus("current")
_AdEShdslAlarmProvLOSWSThresh_Type = Integer32
_AdEShdslAlarmProvLOSWSThresh_Object = MibTableColumn
adEShdslAlarmProvLOSWSThresh = _AdEShdslAlarmProvLOSWSThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 7),
    _AdEShdslAlarmProvLOSWSThresh_Type()
)
adEShdslAlarmProvLOSWSThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvLOSWSThresh.setStatus("current")


class _AdEShdslAlarmProvOSThresh_Type(Integer32):
    """Custom type adEShdslAlarmProvOSThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdEShdslAlarmProvOSThresh_Type.__name__ = "Integer32"
_AdEShdslAlarmProvOSThresh_Object = MibTableColumn
adEShdslAlarmProvOSThresh = _AdEShdslAlarmProvOSThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 8),
    _AdEShdslAlarmProvOSThresh_Type()
)
adEShdslAlarmProvOSThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvOSThresh.setStatus("current")
_AdEShdslAlarmProvES24HrThresh_Type = Integer32
_AdEShdslAlarmProvES24HrThresh_Object = MibTableColumn
adEShdslAlarmProvES24HrThresh = _AdEShdslAlarmProvES24HrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 9),
    _AdEShdslAlarmProvES24HrThresh_Type()
)
adEShdslAlarmProvES24HrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvES24HrThresh.setStatus("current")
_AdEShdslAlarmProvSES24HrThresh_Type = Integer32
_AdEShdslAlarmProvSES24HrThresh_Object = MibTableColumn
adEShdslAlarmProvSES24HrThresh = _AdEShdslAlarmProvSES24HrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 10),
    _AdEShdslAlarmProvSES24HrThresh_Type()
)
adEShdslAlarmProvSES24HrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvSES24HrThresh.setStatus("current")
_AdEShdslAlarmProvUAS24HrThresh_Type = Integer32
_AdEShdslAlarmProvUAS24HrThresh_Object = MibTableColumn
adEShdslAlarmProvUAS24HrThresh = _AdEShdslAlarmProvUAS24HrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 11),
    _AdEShdslAlarmProvUAS24HrThresh_Type()
)
adEShdslAlarmProvUAS24HrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvUAS24HrThresh.setStatus("current")
_AdEShdslAlarmProvCVC24HrThresh_Type = Integer32
_AdEShdslAlarmProvCVC24HrThresh_Object = MibTableColumn
adEShdslAlarmProvCVC24HrThresh = _AdEShdslAlarmProvCVC24HrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 12),
    _AdEShdslAlarmProvCVC24HrThresh_Type()
)
adEShdslAlarmProvCVC24HrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvCVC24HrThresh.setStatus("current")
_AdEShdslAlarmProvLOSWS24HrThresh_Type = Integer32
_AdEShdslAlarmProvLOSWS24HrThresh_Object = MibTableColumn
adEShdslAlarmProvLOSWS24HrThresh = _AdEShdslAlarmProvLOSWS24HrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 13),
    _AdEShdslAlarmProvLOSWS24HrThresh_Type()
)
adEShdslAlarmProvLOSWS24HrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvLOSWS24HrThresh.setStatus("current")


class _AdEShdslAlarmProvOS24HrThresh_Type(Integer32):
    """Custom type adEShdslAlarmProvOS24HrThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdEShdslAlarmProvOS24HrThresh_Type.__name__ = "Integer32"
_AdEShdslAlarmProvOS24HrThresh_Object = MibTableColumn
adEShdslAlarmProvOS24HrThresh = _AdEShdslAlarmProvOS24HrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 14),
    _AdEShdslAlarmProvOS24HrThresh_Type()
)
adEShdslAlarmProvOS24HrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvOS24HrThresh.setStatus("current")
_AdEShdslAlarmProvRetrains15MinThresh_Type = Integer32
_AdEShdslAlarmProvRetrains15MinThresh_Object = MibTableColumn
adEShdslAlarmProvRetrains15MinThresh = _AdEShdslAlarmProvRetrains15MinThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 15),
    _AdEShdslAlarmProvRetrains15MinThresh_Type()
)
adEShdslAlarmProvRetrains15MinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvRetrains15MinThresh.setStatus("current")
_AdEShdslAlarmProvHandshakeFailures15MinThresh_Type = Integer32
_AdEShdslAlarmProvHandshakeFailures15MinThresh_Object = MibTableColumn
adEShdslAlarmProvHandshakeFailures15MinThresh = _AdEShdslAlarmProvHandshakeFailures15MinThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 16),
    _AdEShdslAlarmProvHandshakeFailures15MinThresh_Type()
)
adEShdslAlarmProvHandshakeFailures15MinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvHandshakeFailures15MinThresh.setStatus("current")
_AdEShdslAlarmProvRetrains24HrThresh_Type = Integer32
_AdEShdslAlarmProvRetrains24HrThresh_Object = MibTableColumn
adEShdslAlarmProvRetrains24HrThresh = _AdEShdslAlarmProvRetrains24HrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 17),
    _AdEShdslAlarmProvRetrains24HrThresh_Type()
)
adEShdslAlarmProvRetrains24HrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvRetrains24HrThresh.setStatus("current")
_AdEShdslAlarmProvHandshakeFailures24HrThresh_Type = Integer32
_AdEShdslAlarmProvHandshakeFailures24HrThresh_Object = MibTableColumn
adEShdslAlarmProvHandshakeFailures24HrThresh = _AdEShdslAlarmProvHandshakeFailures24HrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 2, 1, 18),
    _AdEShdslAlarmProvHandshakeFailures24HrThresh_Type()
)
adEShdslAlarmProvHandshakeFailures24HrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslAlarmProvHandshakeFailures24HrThresh.setStatus("current")
_AdEShdslTestProvTable_Object = MibTable
adEShdslTestProvTable = _AdEShdslTestProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 3)
)
if mibBuilder.loadTexts:
    adEShdslTestProvTable.setStatus("current")
_AdEShdslTestProvEntry_Object = MibTableRow
adEShdslTestProvEntry = _AdEShdslTestProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 3, 1)
)
adEShdslTestProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
)
if mibBuilder.loadTexts:
    adEShdslTestProvEntry.setStatus("current")
_AdEShdslTestProvLoopbackTimeout_Type = Integer32
_AdEShdslTestProvLoopbackTimeout_Object = MibTableColumn
adEShdslTestProvLoopbackTimeout = _AdEShdslTestProvLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 3, 1, 1),
    _AdEShdslTestProvLoopbackTimeout_Type()
)
adEShdslTestProvLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestProvLoopbackTimeout.setStatus("current")


class _AdEShdslTestProvEnumeratedLoopbackTimeout_Type(Integer32):
    """Custom type adEShdslTestProvEnumeratedLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("timeoutDisabled", 1),
          ("timeout20Minutes", 2),
          ("timeout60Minutes", 3),
          ("timeout120Minutes", 4),
          ("timeout8Hours", 5),
          ("timeout24Hours", 6))
    )


_AdEShdslTestProvEnumeratedLoopbackTimeout_Type.__name__ = "Integer32"
_AdEShdslTestProvEnumeratedLoopbackTimeout_Object = MibTableColumn
adEShdslTestProvEnumeratedLoopbackTimeout = _AdEShdslTestProvEnumeratedLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 3, 3, 1, 2),
    _AdEShdslTestProvEnumeratedLoopbackTimeout_Type()
)
adEShdslTestProvEnumeratedLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestProvEnumeratedLoopbackTimeout.setStatus("current")
_AdEShdslStatus_ObjectIdentity = ObjectIdentity
adEShdslStatus = _AdEShdslStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4)
)
_AdEShdslStatusTable_Object = MibTable
adEShdslStatusTable = _AdEShdslStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adEShdslStatusTable.setStatus("current")
_AdEShdslStatusEntry_Object = MibTableRow
adEShdslStatusEntry = _AdEShdslStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1)
)
adEShdslStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
)
if mibBuilder.loadTexts:
    adEShdslStatusEntry.setStatus("current")


class _AdEShdslStatusCurrStatus_Type(Integer32):
    """Custom type adEShdslStatusCurrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 1),
          ("handshaking", 2),
          ("training", 3),
          ("linkUp", 4),
          ("alarmsPresent", 5),
          ("inTest", 6))
    )


_AdEShdslStatusCurrStatus_Type.__name__ = "Integer32"
_AdEShdslStatusCurrStatus_Object = MibTableColumn
adEShdslStatusCurrStatus = _AdEShdslStatusCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 1),
    _AdEShdslStatusCurrStatus_Type()
)
adEShdslStatusCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusCurrStatus.setStatus("current")
_AdEShdslStatusCurrLoopAtten_Type = Integer32
_AdEShdslStatusCurrLoopAtten_Object = MibTableColumn
adEShdslStatusCurrLoopAtten = _AdEShdslStatusCurrLoopAtten_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 2),
    _AdEShdslStatusCurrLoopAtten_Type()
)
adEShdslStatusCurrLoopAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusCurrLoopAtten.setStatus("current")
_AdEShdslStatusMinLoopAtten_Type = Integer32
_AdEShdslStatusMinLoopAtten_Object = MibTableColumn
adEShdslStatusMinLoopAtten = _AdEShdslStatusMinLoopAtten_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 3),
    _AdEShdslStatusMinLoopAtten_Type()
)
adEShdslStatusMinLoopAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusMinLoopAtten.setStatus("current")
_AdEShdslStatusMaxLoopAtten_Type = Integer32
_AdEShdslStatusMaxLoopAtten_Object = MibTableColumn
adEShdslStatusMaxLoopAtten = _AdEShdslStatusMaxLoopAtten_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 4),
    _AdEShdslStatusMaxLoopAtten_Type()
)
adEShdslStatusMaxLoopAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusMaxLoopAtten.setStatus("current")
_AdEShdslStatusCurrSNRMargin_Type = Integer32
_AdEShdslStatusCurrSNRMargin_Object = MibTableColumn
adEShdslStatusCurrSNRMargin = _AdEShdslStatusCurrSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 5),
    _AdEShdslStatusCurrSNRMargin_Type()
)
adEShdslStatusCurrSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusCurrSNRMargin.setStatus("current")
_AdEShdslStatusMinSNRMargin_Type = Integer32
_AdEShdslStatusMinSNRMargin_Object = MibTableColumn
adEShdslStatusMinSNRMargin = _AdEShdslStatusMinSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 6),
    _AdEShdslStatusMinSNRMargin_Type()
)
adEShdslStatusMinSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusMinSNRMargin.setStatus("current")
_AdEShdslStatusMaxSNRMargin_Type = Integer32
_AdEShdslStatusMaxSNRMargin_Object = MibTableColumn
adEShdslStatusMaxSNRMargin = _AdEShdslStatusMaxSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 7),
    _AdEShdslStatusMaxSNRMargin_Type()
)
adEShdslStatusMaxSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusMaxSNRMargin.setStatus("current")
_AdEShdslStatusES_Type = Integer32
_AdEShdslStatusES_Object = MibTableColumn
adEShdslStatusES = _AdEShdslStatusES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 8),
    _AdEShdslStatusES_Type()
)
adEShdslStatusES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusES.setStatus("current")
_AdEShdslStatusSES_Type = Integer32
_AdEShdslStatusSES_Object = MibTableColumn
adEShdslStatusSES = _AdEShdslStatusSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 9),
    _AdEShdslStatusSES_Type()
)
adEShdslStatusSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusSES.setStatus("current")
_AdEShdslStatusUAS_Type = Integer32
_AdEShdslStatusUAS_Object = MibTableColumn
adEShdslStatusUAS = _AdEShdslStatusUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 10),
    _AdEShdslStatusUAS_Type()
)
adEShdslStatusUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusUAS.setStatus("current")
_AdEShdslStatusCVC_Type = Integer32
_AdEShdslStatusCVC_Object = MibTableColumn
adEShdslStatusCVC = _AdEShdslStatusCVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 11),
    _AdEShdslStatusCVC_Type()
)
adEShdslStatusCVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusCVC.setStatus("current")
_AdEShdslStatusLOSWS_Type = Integer32
_AdEShdslStatusLOSWS_Object = MibTableColumn
adEShdslStatusLOSWS = _AdEShdslStatusLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 12),
    _AdEShdslStatusLOSWS_Type()
)
adEShdslStatusLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusLOSWS.setStatus("current")
_AdEShdslStatusOS_Type = Integer32
_AdEShdslStatusOS_Object = MibTableColumn
adEShdslStatusOS = _AdEShdslStatusOS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 13),
    _AdEShdslStatusOS_Type()
)
adEShdslStatusOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusOS.setStatus("current")


class _AdEShdslStatusResetStatistics_Type(Integer32):
    """Custom type adEShdslStatusResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdEShdslStatusResetStatistics_Type.__name__ = "Integer32"
_AdEShdslStatusResetStatistics_Object = MibTableColumn
adEShdslStatusResetStatistics = _AdEShdslStatusResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 14),
    _AdEShdslStatusResetStatistics_Type()
)
adEShdslStatusResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslStatusResetStatistics.setStatus("current")
_AdEShdslStatusMaxAttainableRate_Type = Integer32
_AdEShdslStatusMaxAttainableRate_Object = MibTableColumn
adEShdslStatusMaxAttainableRate = _AdEShdslStatusMaxAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 15),
    _AdEShdslStatusMaxAttainableRate_Type()
)
adEShdslStatusMaxAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusMaxAttainableRate.setStatus("current")
_AdEShdslStatusUpstreamPBO_Type = Integer32
_AdEShdslStatusUpstreamPBO_Object = MibTableColumn
adEShdslStatusUpstreamPBO = _AdEShdslStatusUpstreamPBO_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 16),
    _AdEShdslStatusUpstreamPBO_Type()
)
adEShdslStatusUpstreamPBO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusUpstreamPBO.setStatus("current")
_AdEShdslStatusDownstreamPBO_Type = Integer32
_AdEShdslStatusDownstreamPBO_Object = MibTableColumn
adEShdslStatusDownstreamPBO = _AdEShdslStatusDownstreamPBO_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 17),
    _AdEShdslStatusDownstreamPBO_Type()
)
adEShdslStatusDownstreamPBO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusDownstreamPBO.setStatus("current")
_AdEShdslStatusCurrRate_Type = Integer32
_AdEShdslStatusCurrRate_Object = MibTableColumn
adEShdslStatusCurrRate = _AdEShdslStatusCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 18),
    _AdEShdslStatusCurrRate_Type()
)
adEShdslStatusCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusCurrRate.setStatus("current")
_AdEShdslStatusRetrains_Type = Integer32
_AdEShdslStatusRetrains_Object = MibTableColumn
adEShdslStatusRetrains = _AdEShdslStatusRetrains_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 19),
    _AdEShdslStatusRetrains_Type()
)
adEShdslStatusRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusRetrains.setStatus("current")
_AdEShdslStatusHandshakeFailures_Type = Integer32
_AdEShdslStatusHandshakeFailures_Object = MibTableColumn
adEShdslStatusHandshakeFailures = _AdEShdslStatusHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 20),
    _AdEShdslStatusHandshakeFailures_Type()
)
adEShdslStatusHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusHandshakeFailures.setStatus("current")
_AdEShdslStatusCurrSNRMarginCurrTrain_Type = Integer32
_AdEShdslStatusCurrSNRMarginCurrTrain_Object = MibTableColumn
adEShdslStatusCurrSNRMarginCurrTrain = _AdEShdslStatusCurrSNRMarginCurrTrain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 21),
    _AdEShdslStatusCurrSNRMarginCurrTrain_Type()
)
adEShdslStatusCurrSNRMarginCurrTrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusCurrSNRMarginCurrTrain.setStatus("current")
_AdEShdslStatusMinSNRMarginCurrTrain_Type = Integer32
_AdEShdslStatusMinSNRMarginCurrTrain_Object = MibTableColumn
adEShdslStatusMinSNRMarginCurrTrain = _AdEShdslStatusMinSNRMarginCurrTrain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 22),
    _AdEShdslStatusMinSNRMarginCurrTrain_Type()
)
adEShdslStatusMinSNRMarginCurrTrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusMinSNRMarginCurrTrain.setStatus("current")
_AdEShdslStatusMaxSNRMarginCurrTrain_Type = Integer32
_AdEShdslStatusMaxSNRMarginCurrTrain_Object = MibTableColumn
adEShdslStatusMaxSNRMarginCurrTrain = _AdEShdslStatusMaxSNRMarginCurrTrain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 23),
    _AdEShdslStatusMaxSNRMarginCurrTrain_Type()
)
adEShdslStatusMaxSNRMarginCurrTrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusMaxSNRMarginCurrTrain.setStatus("current")
_AdEShdslStatusMinSNRMarginPrevTrain_Type = Integer32
_AdEShdslStatusMinSNRMarginPrevTrain_Object = MibTableColumn
adEShdslStatusMinSNRMarginPrevTrain = _AdEShdslStatusMinSNRMarginPrevTrain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 24),
    _AdEShdslStatusMinSNRMarginPrevTrain_Type()
)
adEShdslStatusMinSNRMarginPrevTrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusMinSNRMarginPrevTrain.setStatus("current")
_AdEShdslStatusMaxSNRMarginPrevTrain_Type = Integer32
_AdEShdslStatusMaxSNRMarginPrevTrain_Object = MibTableColumn
adEShdslStatusMaxSNRMarginPrevTrain = _AdEShdslStatusMaxSNRMarginPrevTrain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 25),
    _AdEShdslStatusMaxSNRMarginPrevTrain_Type()
)
adEShdslStatusMaxSNRMarginPrevTrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusMaxSNRMarginPrevTrain.setStatus("current")


class _AdEShdslStatusPhysicalLinkLabel_Type(DisplayString):
    """Custom type adEShdslStatusPhysicalLinkLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_AdEShdslStatusPhysicalLinkLabel_Type.__name__ = "DisplayString"
_AdEShdslStatusPhysicalLinkLabel_Object = MibTableColumn
adEShdslStatusPhysicalLinkLabel = _AdEShdslStatusPhysicalLinkLabel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 1, 1, 26),
    _AdEShdslStatusPhysicalLinkLabel_Type()
)
adEShdslStatusPhysicalLinkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusPhysicalLinkLabel.setStatus("current")
_AdEShdslStatusInfoTable_Object = MibTable
adEShdslStatusInfoTable = _AdEShdslStatusInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 2)
)
if mibBuilder.loadTexts:
    adEShdslStatusInfoTable.setStatus("current")
_AdEShdslStatusInfoEntry_Object = MibTableRow
adEShdslStatusInfoEntry = _AdEShdslStatusInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 2, 1)
)
adEShdslStatusInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adEShdslStatusInfoEntry.setStatus("current")
_AdEShdslStatusInfoRepeaterNumber_Type = Integer32
_AdEShdslStatusInfoRepeaterNumber_Object = MibTableColumn
adEShdslStatusInfoRepeaterNumber = _AdEShdslStatusInfoRepeaterNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 2, 1, 1),
    _AdEShdslStatusInfoRepeaterNumber_Type()
)
adEShdslStatusInfoRepeaterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusInfoRepeaterNumber.setStatus("current")


class _AdEShdslStatusInfoPairReversal_Type(OctetString):
    """Custom type adEShdslStatusInfoPairReversal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AdEShdslStatusInfoPairReversal_Type.__name__ = "OctetString"
_AdEShdslStatusInfoPairReversal_Object = MibTableColumn
adEShdslStatusInfoPairReversal = _AdEShdslStatusInfoPairReversal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 2, 1, 2),
    _AdEShdslStatusInfoPairReversal_Type()
)
adEShdslStatusInfoPairReversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusInfoPairReversal.setStatus("current")
_AdEShdslStatusInfoLoopAlarmStatus_Type = OctetString
_AdEShdslStatusInfoLoopAlarmStatus_Object = MibTableColumn
adEShdslStatusInfoLoopAlarmStatus = _AdEShdslStatusInfoLoopAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 2, 1, 3),
    _AdEShdslStatusInfoLoopAlarmStatus_Type()
)
adEShdslStatusInfoLoopAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusInfoLoopAlarmStatus.setStatus("current")
_AdEShdslStatusInfoTopology_Type = OctetString
_AdEShdslStatusInfoTopology_Object = MibTableColumn
adEShdslStatusInfoTopology = _AdEShdslStatusInfoTopology_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 2, 1, 4),
    _AdEShdslStatusInfoTopology_Type()
)
adEShdslStatusInfoTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusInfoTopology.setStatus("current")
_AdEShdslStatusIfTable_Object = MibTable
adEShdslStatusIfTable = _AdEShdslStatusIfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 3)
)
if mibBuilder.loadTexts:
    adEShdslStatusIfTable.setStatus("current")
_AdEShdslStatusIfEntry_Object = MibTableRow
adEShdslStatusIfEntry = _AdEShdslStatusIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 3, 1)
)
adEShdslStatusIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adEShdslStatusIfEntry.setStatus("current")


class _AdEShdslStatusIfTrainingMode_Type(Integer32):
    """Custom type adEShdslStatusIfTrainingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ltu", 1),
          ("ntu", 2))
    )


_AdEShdslStatusIfTrainingMode_Type.__name__ = "Integer32"
_AdEShdslStatusIfTrainingMode_Object = MibTableColumn
adEShdslStatusIfTrainingMode = _AdEShdslStatusIfTrainingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 4, 3, 1, 1),
    _AdEShdslStatusIfTrainingMode_Type()
)
adEShdslStatusIfTrainingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslStatusIfTrainingMode.setStatus("current")
_AdEShdslTest_ObjectIdentity = ObjectIdentity
adEShdslTest = _AdEShdslTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5)
)
_AdEShdslTestTable_Object = MibTable
adEShdslTestTable = _AdEShdslTestTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 1)
)
if mibBuilder.loadTexts:
    adEShdslTestTable.setStatus("current")
_AdEShdslTestEntry_Object = MibTableRow
adEShdslTestEntry = _AdEShdslTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 1, 1)
)
adEShdslTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
)
if mibBuilder.loadTexts:
    adEShdslTestEntry.setStatus("current")


class _AdEShdslTestLoopback_Type(Integer32):
    """Custom type adEShdslTestLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dualSidedLoopback", 1),
          ("networkTransparentLoopback", 2),
          ("networkNonTransparentLoopback", 3),
          ("customerTransparentLoopback", 4),
          ("customerNonTransparentLoopback", 5),
          ("noLoopback", 6))
    )


_AdEShdslTestLoopback_Type.__name__ = "Integer32"
_AdEShdslTestLoopback_Object = MibTableColumn
adEShdslTestLoopback = _AdEShdslTestLoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 1, 1, 1),
    _AdEShdslTestLoopback_Type()
)
adEShdslTestLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestLoopback.setStatus("current")


class _AdEShdslTestLoopdownAll_Type(Integer32):
    """Custom type adEShdslTestLoopdownAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loopdownAllNow", 1)
    )


_AdEShdslTestLoopdownAll_Type.__name__ = "Integer32"
_AdEShdslTestLoopdownAll_Object = MibTableColumn
adEShdslTestLoopdownAll = _AdEShdslTestLoopdownAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 1, 1, 2),
    _AdEShdslTestLoopdownAll_Type()
)
adEShdslTestLoopdownAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestLoopdownAll.setStatus("current")


class _AdEShdslTestinitMinMax_Type(Integer32):
    """Custom type adEShdslTestinitMinMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetMinMax", 1)
    )


_AdEShdslTestinitMinMax_Type.__name__ = "Integer32"
_AdEShdslTestinitMinMax_Object = MibTableColumn
adEShdslTestinitMinMax = _AdEShdslTestinitMinMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 1, 1, 3),
    _AdEShdslTestinitMinMax_Type()
)
adEShdslTestinitMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestinitMinMax.setStatus("current")
_AdEShdslTestRepeaterPoweringTable_Object = MibTable
adEShdslTestRepeaterPoweringTable = _AdEShdslTestRepeaterPoweringTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2)
)
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringTable.setStatus("current")
_AdEShdslTestRepeaterPoweringEntry_Object = MibTableRow
adEShdslTestRepeaterPoweringEntry = _AdEShdslTestRepeaterPoweringEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1)
)
adEShdslTestRepeaterPoweringEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringEntry.setStatus("current")


class _AdEShdslTestRepeaterPoweringState_Type(Integer32):
    """Custom type adEShdslTestRepeaterPoweringState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("manual", 2))
    )


_AdEShdslTestRepeaterPoweringState_Type.__name__ = "Integer32"
_AdEShdslTestRepeaterPoweringState_Object = MibTableColumn
adEShdslTestRepeaterPoweringState = _AdEShdslTestRepeaterPoweringState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 1),
    _AdEShdslTestRepeaterPoweringState_Type()
)
adEShdslTestRepeaterPoweringState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringState.setStatus("current")


class _AdEShdslTestRepeaterPoweringNumRepeaters_Type(Integer32):
    """Custom type adEShdslTestRepeaterPoweringNumRepeaters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdEShdslTestRepeaterPoweringNumRepeaters_Type.__name__ = "Integer32"
_AdEShdslTestRepeaterPoweringNumRepeaters_Object = MibTableColumn
adEShdslTestRepeaterPoweringNumRepeaters = _AdEShdslTestRepeaterPoweringNumRepeaters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 2),
    _AdEShdslTestRepeaterPoweringNumRepeaters_Type()
)
adEShdslTestRepeaterPoweringNumRepeaters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringNumRepeaters.setStatus("current")


class _AdEShdslTestRepeaterPoweringTimeout_Type(Integer32):
    """Custom type adEShdslTestRepeaterPoweringTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AdEShdslTestRepeaterPoweringTimeout_Type.__name__ = "Integer32"
_AdEShdslTestRepeaterPoweringTimeout_Object = MibTableColumn
adEShdslTestRepeaterPoweringTimeout = _AdEShdslTestRepeaterPoweringTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 3),
    _AdEShdslTestRepeaterPoweringTimeout_Type()
)
adEShdslTestRepeaterPoweringTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringTimeout.setStatus("current")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringTimeout.setUnits("minutes")


class _AdEShdslTestRepeaterPoweringTimeRemaining_Type(Integer32):
    """Custom type adEShdslTestRepeaterPoweringTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AdEShdslTestRepeaterPoweringTimeRemaining_Type.__name__ = "Integer32"
_AdEShdslTestRepeaterPoweringTimeRemaining_Object = MibTableColumn
adEShdslTestRepeaterPoweringTimeRemaining = _AdEShdslTestRepeaterPoweringTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 4),
    _AdEShdslTestRepeaterPoweringTimeRemaining_Type()
)
adEShdslTestRepeaterPoweringTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringTimeRemaining.setUnits("minutes")
_AdEShdslTestRepeaterPoweringSRU1Discovered_Type = TruthValue
_AdEShdslTestRepeaterPoweringSRU1Discovered_Object = MibTableColumn
adEShdslTestRepeaterPoweringSRU1Discovered = _AdEShdslTestRepeaterPoweringSRU1Discovered_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 5),
    _AdEShdslTestRepeaterPoweringSRU1Discovered_Type()
)
adEShdslTestRepeaterPoweringSRU1Discovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringSRU1Discovered.setStatus("current")
_AdEShdslTestRepeaterPoweringSRU2Discovered_Type = TruthValue
_AdEShdslTestRepeaterPoweringSRU2Discovered_Object = MibTableColumn
adEShdslTestRepeaterPoweringSRU2Discovered = _AdEShdslTestRepeaterPoweringSRU2Discovered_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 6),
    _AdEShdslTestRepeaterPoweringSRU2Discovered_Type()
)
adEShdslTestRepeaterPoweringSRU2Discovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringSRU2Discovered.setStatus("current")
_AdEShdslTestRepeaterPoweringSRU3Discovered_Type = TruthValue
_AdEShdslTestRepeaterPoweringSRU3Discovered_Object = MibTableColumn
adEShdslTestRepeaterPoweringSRU3Discovered = _AdEShdslTestRepeaterPoweringSRU3Discovered_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 7),
    _AdEShdslTestRepeaterPoweringSRU3Discovered_Type()
)
adEShdslTestRepeaterPoweringSRU3Discovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringSRU3Discovered.setStatus("current")
_AdEShdslTestRepeaterPoweringSRU4Discovered_Type = TruthValue
_AdEShdslTestRepeaterPoweringSRU4Discovered_Object = MibTableColumn
adEShdslTestRepeaterPoweringSRU4Discovered = _AdEShdslTestRepeaterPoweringSRU4Discovered_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 8),
    _AdEShdslTestRepeaterPoweringSRU4Discovered_Type()
)
adEShdslTestRepeaterPoweringSRU4Discovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringSRU4Discovered.setStatus("current")


class _AdEShdslTestRepeaterPoweringShortDetected_Type(Integer32):
    """Custom type adEShdslTestRepeaterPoweringShortDetected based on Integer32"""
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
        *(("none", 0),
          ("sru1", 1),
          ("sru2", 2),
          ("sru3", 3),
          ("sru4", 4))
    )


_AdEShdslTestRepeaterPoweringShortDetected_Type.__name__ = "Integer32"
_AdEShdslTestRepeaterPoweringShortDetected_Object = MibTableColumn
adEShdslTestRepeaterPoweringShortDetected = _AdEShdslTestRepeaterPoweringShortDetected_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 9),
    _AdEShdslTestRepeaterPoweringShortDetected_Type()
)
adEShdslTestRepeaterPoweringShortDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringShortDetected.setStatus("current")


class _AdEShdslTestRepeaterPoweringGroundFaultDetected_Type(Integer32):
    """Custom type adEShdslTestRepeaterPoweringGroundFaultDetected based on Integer32"""
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
        *(("none", 0),
          ("sru1", 1),
          ("sru2", 2),
          ("sru3", 3),
          ("sru4", 4))
    )


_AdEShdslTestRepeaterPoweringGroundFaultDetected_Type.__name__ = "Integer32"
_AdEShdslTestRepeaterPoweringGroundFaultDetected_Object = MibTableColumn
adEShdslTestRepeaterPoweringGroundFaultDetected = _AdEShdslTestRepeaterPoweringGroundFaultDetected_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 10),
    _AdEShdslTestRepeaterPoweringGroundFaultDetected_Type()
)
adEShdslTestRepeaterPoweringGroundFaultDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringGroundFaultDetected.setStatus("current")
_AdEShdslTestRepeaterPoweringLastErrorString_Type = DisplayString
_AdEShdslTestRepeaterPoweringLastErrorString_Object = MibTableColumn
adEShdslTestRepeaterPoweringLastErrorString = _AdEShdslTestRepeaterPoweringLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 2, 1, 11),
    _AdEShdslTestRepeaterPoweringLastErrorString_Type()
)
adEShdslTestRepeaterPoweringLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestRepeaterPoweringLastErrorString.setStatus("current")
_AdEShdslTestLoopLocatorLastErrorTable_Object = MibTable
adEShdslTestLoopLocatorLastErrorTable = _AdEShdslTestLoopLocatorLastErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 3)
)
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorLastErrorTable.setStatus("current")
_AdEShdslTestLoopLocatorLastErrorEntry_Object = MibTableRow
adEShdslTestLoopLocatorLastErrorEntry = _AdEShdslTestLoopLocatorLastErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 3, 1)
)
adEShdslTestLoopLocatorLastErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorLastErrorEntry.setStatus("current")
_AdEShdslTestLoopLocatorLastErrorString_Type = DisplayString
_AdEShdslTestLoopLocatorLastErrorString_Object = MibTableColumn
adEShdslTestLoopLocatorLastErrorString = _AdEShdslTestLoopLocatorLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 3, 1, 1),
    _AdEShdslTestLoopLocatorLastErrorString_Type()
)
adEShdslTestLoopLocatorLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorLastErrorString.setStatus("current")
_AdEShdslTestLoopLocatorTable_Object = MibTable
adEShdslTestLoopLocatorTable = _AdEShdslTestLoopLocatorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 4)
)
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorTable.setStatus("current")
_AdEShdslTestLoopLocatorEntry_Object = MibTableRow
adEShdslTestLoopLocatorEntry = _AdEShdslTestLoopLocatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 4, 1)
)
adEShdslTestLoopLocatorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
)
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorEntry.setStatus("current")


class _AdEShdslTestLoopLocatorState_Type(Integer32):
    """Custom type adEShdslTestLoopLocatorState based on Integer32"""
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


_AdEShdslTestLoopLocatorState_Type.__name__ = "Integer32"
_AdEShdslTestLoopLocatorState_Object = MibTableColumn
adEShdslTestLoopLocatorState = _AdEShdslTestLoopLocatorState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 4, 1, 1),
    _AdEShdslTestLoopLocatorState_Type()
)
adEShdslTestLoopLocatorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorState.setStatus("current")


class _AdEShdslTestLoopLocatorTimeout_Type(Integer32):
    """Custom type adEShdslTestLoopLocatorTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AdEShdslTestLoopLocatorTimeout_Type.__name__ = "Integer32"
_AdEShdslTestLoopLocatorTimeout_Object = MibTableColumn
adEShdslTestLoopLocatorTimeout = _AdEShdslTestLoopLocatorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 4, 1, 2),
    _AdEShdslTestLoopLocatorTimeout_Type()
)
adEShdslTestLoopLocatorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorTimeout.setStatus("current")
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorTimeout.setUnits("minutes")


class _AdEShdslTestLoopLocatorTimeRemaining_Type(Integer32):
    """Custom type adEShdslTestLoopLocatorTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AdEShdslTestLoopLocatorTimeRemaining_Type.__name__ = "Integer32"
_AdEShdslTestLoopLocatorTimeRemaining_Object = MibTableColumn
adEShdslTestLoopLocatorTimeRemaining = _AdEShdslTestLoopLocatorTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 5, 4, 1, 3),
    _AdEShdslTestLoopLocatorTimeRemaining_Type()
)
adEShdslTestLoopLocatorTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    adEShdslTestLoopLocatorTimeRemaining.setUnits("minutes")
_AdEShdslPerformance_ObjectIdentity = ObjectIdentity
adEShdslPerformance = _AdEShdslPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6)
)
_AdEShdslPerfCurrTable_Object = MibTable
adEShdslPerfCurrTable = _AdEShdslPerfCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1)
)
if mibBuilder.loadTexts:
    adEShdslPerfCurrTable.setStatus("current")
_AdEShdslPerfCurrEntry_Object = MibTableRow
adEShdslPerfCurrEntry = _AdEShdslPerfCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1)
)
adEShdslPerfCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
)
if mibBuilder.loadTexts:
    adEShdslPerfCurrEntry.setStatus("current")
_AdEShdslPerfCurr15MinES_Type = Integer32
_AdEShdslPerfCurr15MinES_Object = MibTableColumn
adEShdslPerfCurr15MinES = _AdEShdslPerfCurr15MinES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 1),
    _AdEShdslPerfCurr15MinES_Type()
)
adEShdslPerfCurr15MinES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinES.setStatus("current")
_AdEShdslPerfCurr15MinSES_Type = Integer32
_AdEShdslPerfCurr15MinSES_Object = MibTableColumn
adEShdslPerfCurr15MinSES = _AdEShdslPerfCurr15MinSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 2),
    _AdEShdslPerfCurr15MinSES_Type()
)
adEShdslPerfCurr15MinSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinSES.setStatus("current")
_AdEShdslPerfCurr15MinUAS_Type = Integer32
_AdEShdslPerfCurr15MinUAS_Object = MibTableColumn
adEShdslPerfCurr15MinUAS = _AdEShdslPerfCurr15MinUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 3),
    _AdEShdslPerfCurr15MinUAS_Type()
)
adEShdslPerfCurr15MinUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinUAS.setStatus("current")
_AdEShdslPerfCurr15MinCVC_Type = Integer32
_AdEShdslPerfCurr15MinCVC_Object = MibTableColumn
adEShdslPerfCurr15MinCVC = _AdEShdslPerfCurr15MinCVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 4),
    _AdEShdslPerfCurr15MinCVC_Type()
)
adEShdslPerfCurr15MinCVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinCVC.setStatus("current")
_AdEShdslPerfCurr15MinLOSWS_Type = Integer32
_AdEShdslPerfCurr15MinLOSWS_Object = MibTableColumn
adEShdslPerfCurr15MinLOSWS = _AdEShdslPerfCurr15MinLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 5),
    _AdEShdslPerfCurr15MinLOSWS_Type()
)
adEShdslPerfCurr15MinLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinLOSWS.setStatus("current")
_AdEShdslPerfCurr15MinOS_Type = Integer32
_AdEShdslPerfCurr15MinOS_Object = MibTableColumn
adEShdslPerfCurr15MinOS = _AdEShdslPerfCurr15MinOS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 6),
    _AdEShdslPerfCurr15MinOS_Type()
)
adEShdslPerfCurr15MinOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinOS.setStatus("current")
_AdEShdslPerfCurr24HrES_Type = Integer32
_AdEShdslPerfCurr24HrES_Object = MibTableColumn
adEShdslPerfCurr24HrES = _AdEShdslPerfCurr24HrES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 7),
    _AdEShdslPerfCurr24HrES_Type()
)
adEShdslPerfCurr24HrES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrES.setStatus("current")
_AdEShdslPerfCurr24HrSES_Type = Integer32
_AdEShdslPerfCurr24HrSES_Object = MibTableColumn
adEShdslPerfCurr24HrSES = _AdEShdslPerfCurr24HrSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 8),
    _AdEShdslPerfCurr24HrSES_Type()
)
adEShdslPerfCurr24HrSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrSES.setStatus("current")
_AdEShdslPerfCurr24HrUAS_Type = Integer32
_AdEShdslPerfCurr24HrUAS_Object = MibTableColumn
adEShdslPerfCurr24HrUAS = _AdEShdslPerfCurr24HrUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 9),
    _AdEShdslPerfCurr24HrUAS_Type()
)
adEShdslPerfCurr24HrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrUAS.setStatus("current")
_AdEShdslPerfCurr24HrCVC_Type = Integer32
_AdEShdslPerfCurr24HrCVC_Object = MibTableColumn
adEShdslPerfCurr24HrCVC = _AdEShdslPerfCurr24HrCVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 10),
    _AdEShdslPerfCurr24HrCVC_Type()
)
adEShdslPerfCurr24HrCVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrCVC.setStatus("current")
_AdEShdslPerfCurr24HrLOSWS_Type = Integer32
_AdEShdslPerfCurr24HrLOSWS_Object = MibTableColumn
adEShdslPerfCurr24HrLOSWS = _AdEShdslPerfCurr24HrLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 11),
    _AdEShdslPerfCurr24HrLOSWS_Type()
)
adEShdslPerfCurr24HrLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrLOSWS.setStatus("current")
_AdEShdslPerfCurr24HrOS_Type = Integer32
_AdEShdslPerfCurr24HrOS_Object = MibTableColumn
adEShdslPerfCurr24HrOS = _AdEShdslPerfCurr24HrOS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 12),
    _AdEShdslPerfCurr24HrOS_Type()
)
adEShdslPerfCurr24HrOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrOS.setStatus("current")
_AdEShdslPerf15MinValidIntervals_Type = Integer32
_AdEShdslPerf15MinValidIntervals_Object = MibTableColumn
adEShdslPerf15MinValidIntervals = _AdEShdslPerf15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 13),
    _AdEShdslPerf15MinValidIntervals_Type()
)
adEShdslPerf15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinValidIntervals.setStatus("current")
_AdEShdslPerf24HrValidIntervals_Type = Integer32
_AdEShdslPerf24HrValidIntervals_Object = MibTableColumn
adEShdslPerf24HrValidIntervals = _AdEShdslPerf24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 14),
    _AdEShdslPerf24HrValidIntervals_Type()
)
adEShdslPerf24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrValidIntervals.setStatus("current")
_AdEShdslPerfCurr15MinRetrains_Type = Integer32
_AdEShdslPerfCurr15MinRetrains_Object = MibTableColumn
adEShdslPerfCurr15MinRetrains = _AdEShdslPerfCurr15MinRetrains_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 15),
    _AdEShdslPerfCurr15MinRetrains_Type()
)
adEShdslPerfCurr15MinRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinRetrains.setStatus("current")
_AdEShdslPerfCurr15MinHandshakeFailures_Type = Integer32
_AdEShdslPerfCurr15MinHandshakeFailures_Object = MibTableColumn
adEShdslPerfCurr15MinHandshakeFailures = _AdEShdslPerfCurr15MinHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 16),
    _AdEShdslPerfCurr15MinHandshakeFailures_Type()
)
adEShdslPerfCurr15MinHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinHandshakeFailures.setStatus("current")
_AdEShdslPerfCurr24HrRetrains_Type = Integer32
_AdEShdslPerfCurr24HrRetrains_Object = MibTableColumn
adEShdslPerfCurr24HrRetrains = _AdEShdslPerfCurr24HrRetrains_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 17),
    _AdEShdslPerfCurr24HrRetrains_Type()
)
adEShdslPerfCurr24HrRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrRetrains.setStatus("current")
_AdEShdslPerfCurr24HrHandshakeFailures_Type = Integer32
_AdEShdslPerfCurr24HrHandshakeFailures_Object = MibTableColumn
adEShdslPerfCurr24HrHandshakeFailures = _AdEShdslPerfCurr24HrHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 18),
    _AdEShdslPerfCurr24HrHandshakeFailures_Type()
)
adEShdslPerfCurr24HrHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrHandshakeFailures.setStatus("current")
_AdEShdslPerfCurr15MinMinSNRMargin_Type = Integer32
_AdEShdslPerfCurr15MinMinSNRMargin_Object = MibTableColumn
adEShdslPerfCurr15MinMinSNRMargin = _AdEShdslPerfCurr15MinMinSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 19),
    _AdEShdslPerfCurr15MinMinSNRMargin_Type()
)
adEShdslPerfCurr15MinMinSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinMinSNRMargin.setStatus("current")
_AdEShdslPerfCurr15MinMaxSNRMargin_Type = Integer32
_AdEShdslPerfCurr15MinMaxSNRMargin_Object = MibTableColumn
adEShdslPerfCurr15MinMaxSNRMargin = _AdEShdslPerfCurr15MinMaxSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 20),
    _AdEShdslPerfCurr15MinMaxSNRMargin_Type()
)
adEShdslPerfCurr15MinMaxSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr15MinMaxSNRMargin.setStatus("current")
_AdEShdslPerfCurr24HrMinSNRMargin_Type = Integer32
_AdEShdslPerfCurr24HrMinSNRMargin_Object = MibTableColumn
adEShdslPerfCurr24HrMinSNRMargin = _AdEShdslPerfCurr24HrMinSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 21),
    _AdEShdslPerfCurr24HrMinSNRMargin_Type()
)
adEShdslPerfCurr24HrMinSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrMinSNRMargin.setStatus("current")
_AdEShdslPerfCurr24HrMaxSNRMargin_Type = Integer32
_AdEShdslPerfCurr24HrMaxSNRMargin_Object = MibTableColumn
adEShdslPerfCurr24HrMaxSNRMargin = _AdEShdslPerfCurr24HrMaxSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 1, 1, 22),
    _AdEShdslPerfCurr24HrMaxSNRMargin_Type()
)
adEShdslPerfCurr24HrMaxSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfCurr24HrMaxSNRMargin.setStatus("current")
_AdEShdslPerfPriorTable_Object = MibTable
adEShdslPerfPriorTable = _AdEShdslPerfPriorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2)
)
if mibBuilder.loadTexts:
    adEShdslPerfPriorTable.setStatus("current")
_AdEShdslPerfPriorEntry_Object = MibTableRow
adEShdslPerfPriorEntry = _AdEShdslPerfPriorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1)
)
adEShdslPerfPriorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
)
if mibBuilder.loadTexts:
    adEShdslPerfPriorEntry.setStatus("current")
_AdEShdslPerfPrior15MinES_Type = Integer32
_AdEShdslPerfPrior15MinES_Object = MibTableColumn
adEShdslPerfPrior15MinES = _AdEShdslPerfPrior15MinES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 1),
    _AdEShdslPerfPrior15MinES_Type()
)
adEShdslPerfPrior15MinES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior15MinES.setStatus("current")
_AdEShdslPerfPrior15MinSES_Type = Integer32
_AdEShdslPerfPrior15MinSES_Object = MibTableColumn
adEShdslPerfPrior15MinSES = _AdEShdslPerfPrior15MinSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 2),
    _AdEShdslPerfPrior15MinSES_Type()
)
adEShdslPerfPrior15MinSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior15MinSES.setStatus("current")
_AdEShdslPerfPrior15MinUAS_Type = Integer32
_AdEShdslPerfPrior15MinUAS_Object = MibTableColumn
adEShdslPerfPrior15MinUAS = _AdEShdslPerfPrior15MinUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 3),
    _AdEShdslPerfPrior15MinUAS_Type()
)
adEShdslPerfPrior15MinUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior15MinUAS.setStatus("current")
_AdEShdslPerfPrior15MinCVC_Type = Integer32
_AdEShdslPerfPrior15MinCVC_Object = MibTableColumn
adEShdslPerfPrior15MinCVC = _AdEShdslPerfPrior15MinCVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 4),
    _AdEShdslPerfPrior15MinCVC_Type()
)
adEShdslPerfPrior15MinCVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior15MinCVC.setStatus("current")
_AdEShdslPerfPrior15MinLOSWS_Type = Integer32
_AdEShdslPerfPrior15MinLOSWS_Object = MibTableColumn
adEShdslPerfPrior15MinLOSWS = _AdEShdslPerfPrior15MinLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 5),
    _AdEShdslPerfPrior15MinLOSWS_Type()
)
adEShdslPerfPrior15MinLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior15MinLOSWS.setStatus("current")
_AdEShdslPerfPrior15MinOS_Type = Integer32
_AdEShdslPerfPrior15MinOS_Object = MibTableColumn
adEShdslPerfPrior15MinOS = _AdEShdslPerfPrior15MinOS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 6),
    _AdEShdslPerfPrior15MinOS_Type()
)
adEShdslPerfPrior15MinOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior15MinOS.setStatus("current")
_AdEShdslPerfPrior24HrES_Type = Integer32
_AdEShdslPerfPrior24HrES_Object = MibTableColumn
adEShdslPerfPrior24HrES = _AdEShdslPerfPrior24HrES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 7),
    _AdEShdslPerfPrior24HrES_Type()
)
adEShdslPerfPrior24HrES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior24HrES.setStatus("current")
_AdEShdslPerfPrior24HrSES_Type = Integer32
_AdEShdslPerfPrior24HrSES_Object = MibTableColumn
adEShdslPerfPrior24HrSES = _AdEShdslPerfPrior24HrSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 8),
    _AdEShdslPerfPrior24HrSES_Type()
)
adEShdslPerfPrior24HrSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior24HrSES.setStatus("current")
_AdEShdslPerfPrior24HrUAS_Type = Integer32
_AdEShdslPerfPrior24HrUAS_Object = MibTableColumn
adEShdslPerfPrior24HrUAS = _AdEShdslPerfPrior24HrUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 9),
    _AdEShdslPerfPrior24HrUAS_Type()
)
adEShdslPerfPrior24HrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior24HrUAS.setStatus("current")
_AdEShdslPerfPrior24HrCVC_Type = Integer32
_AdEShdslPerfPrior24HrCVC_Object = MibTableColumn
adEShdslPerfPrior24HrCVC = _AdEShdslPerfPrior24HrCVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 10),
    _AdEShdslPerfPrior24HrCVC_Type()
)
adEShdslPerfPrior24HrCVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior24HrCVC.setStatus("current")
_AdEShdslPerfPrior24HrLOSWS_Type = Integer32
_AdEShdslPerfPrior24HrLOSWS_Object = MibTableColumn
adEShdslPerfPrior24HrLOSWS = _AdEShdslPerfPrior24HrLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 11),
    _AdEShdslPerfPrior24HrLOSWS_Type()
)
adEShdslPerfPrior24HrLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior24HrLOSWS.setStatus("current")
_AdEShdslPerfPrior24HrOS_Type = Integer32
_AdEShdslPerfPrior24HrOS_Object = MibTableColumn
adEShdslPerfPrior24HrOS = _AdEShdslPerfPrior24HrOS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 2, 1, 12),
    _AdEShdslPerfPrior24HrOS_Type()
)
adEShdslPerfPrior24HrOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerfPrior24HrOS.setStatus("current")
_AdEShdslPerfResetTable_Object = MibTable
adEShdslPerfResetTable = _AdEShdslPerfResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 3)
)
if mibBuilder.loadTexts:
    adEShdslPerfResetTable.setStatus("current")
_AdEShdslPerfResetEntry_Object = MibTableRow
adEShdslPerfResetEntry = _AdEShdslPerfResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 3, 1)
)
adEShdslPerfResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
)
if mibBuilder.loadTexts:
    adEShdslPerfResetEntry.setStatus("current")


class _AdEShdslPerfReset_Type(Integer32):
    """Custom type adEShdslPerfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdEShdslPerfReset_Type.__name__ = "Integer32"
_AdEShdslPerfReset_Object = MibTableColumn
adEShdslPerfReset = _AdEShdslPerfReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 3, 1, 1),
    _AdEShdslPerfReset_Type()
)
adEShdslPerfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslPerfReset.setStatus("current")
_AdEShdslPerf15MinIntTable_Object = MibTable
adEShdslPerf15MinIntTable = _AdEShdslPerf15MinIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4)
)
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntTable.setStatus("current")
_AdEShdslPerf15MinIntEntry_Object = MibTableRow
adEShdslPerf15MinIntEntry = _AdEShdslPerf15MinIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1)
)
adEShdslPerf15MinIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslPerf15MinIntNumber"),
)
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntEntry.setStatus("current")
_AdEShdslPerf15MinIntNumber_Type = Integer32
_AdEShdslPerf15MinIntNumber_Object = MibTableColumn
adEShdslPerf15MinIntNumber = _AdEShdslPerf15MinIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 1),
    _AdEShdslPerf15MinIntNumber_Type()
)
adEShdslPerf15MinIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntNumber.setStatus("current")
_AdEShdslPerf15MinIntES_Type = Integer32
_AdEShdslPerf15MinIntES_Object = MibTableColumn
adEShdslPerf15MinIntES = _AdEShdslPerf15MinIntES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 2),
    _AdEShdslPerf15MinIntES_Type()
)
adEShdslPerf15MinIntES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntES.setStatus("current")
_AdEShdslPerf15MinIntSES_Type = Integer32
_AdEShdslPerf15MinIntSES_Object = MibTableColumn
adEShdslPerf15MinIntSES = _AdEShdslPerf15MinIntSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 3),
    _AdEShdslPerf15MinIntSES_Type()
)
adEShdslPerf15MinIntSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntSES.setStatus("current")
_AdEShdslPerf15MinIntUAS_Type = Integer32
_AdEShdslPerf15MinIntUAS_Object = MibTableColumn
adEShdslPerf15MinIntUAS = _AdEShdslPerf15MinIntUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 4),
    _AdEShdslPerf15MinIntUAS_Type()
)
adEShdslPerf15MinIntUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntUAS.setStatus("current")
_AdEShdslPerf15MinIntCVC_Type = Integer32
_AdEShdslPerf15MinIntCVC_Object = MibTableColumn
adEShdslPerf15MinIntCVC = _AdEShdslPerf15MinIntCVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 5),
    _AdEShdslPerf15MinIntCVC_Type()
)
adEShdslPerf15MinIntCVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntCVC.setStatus("current")
_AdEShdslPerf15MinIntLOSWS_Type = Integer32
_AdEShdslPerf15MinIntLOSWS_Object = MibTableColumn
adEShdslPerf15MinIntLOSWS = _AdEShdslPerf15MinIntLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 6),
    _AdEShdslPerf15MinIntLOSWS_Type()
)
adEShdslPerf15MinIntLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntLOSWS.setStatus("current")
_AdEShdslPerf15MinIntOS_Type = Integer32
_AdEShdslPerf15MinIntOS_Object = MibTableColumn
adEShdslPerf15MinIntOS = _AdEShdslPerf15MinIntOS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 7),
    _AdEShdslPerf15MinIntOS_Type()
)
adEShdslPerf15MinIntOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntOS.setStatus("current")
_AdEShdslPerf15MinIntRetrains_Type = Integer32
_AdEShdslPerf15MinIntRetrains_Object = MibTableColumn
adEShdslPerf15MinIntRetrains = _AdEShdslPerf15MinIntRetrains_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 8),
    _AdEShdslPerf15MinIntRetrains_Type()
)
adEShdslPerf15MinIntRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntRetrains.setStatus("current")
_AdEShdslPerf15MinIntHandshakeFailures_Type = Integer32
_AdEShdslPerf15MinIntHandshakeFailures_Object = MibTableColumn
adEShdslPerf15MinIntHandshakeFailures = _AdEShdslPerf15MinIntHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 9),
    _AdEShdslPerf15MinIntHandshakeFailures_Type()
)
adEShdslPerf15MinIntHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntHandshakeFailures.setStatus("current")
_AdEShdslPerf15MinIntMinSNRMargin_Type = Integer32
_AdEShdslPerf15MinIntMinSNRMargin_Object = MibTableColumn
adEShdslPerf15MinIntMinSNRMargin = _AdEShdslPerf15MinIntMinSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 10),
    _AdEShdslPerf15MinIntMinSNRMargin_Type()
)
adEShdslPerf15MinIntMinSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntMinSNRMargin.setStatus("current")
_AdEShdslPerf15MinIntMaxSNRMargin_Type = Integer32
_AdEShdslPerf15MinIntMaxSNRMargin_Object = MibTableColumn
adEShdslPerf15MinIntMaxSNRMargin = _AdEShdslPerf15MinIntMaxSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 4, 1, 11),
    _AdEShdslPerf15MinIntMaxSNRMargin_Type()
)
adEShdslPerf15MinIntMaxSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf15MinIntMaxSNRMargin.setStatus("current")
_AdEShdslPerf24HrIntTable_Object = MibTable
adEShdslPerf24HrIntTable = _AdEShdslPerf24HrIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5)
)
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntTable.setStatus("current")
_AdEShdslPerf24HrIntEntry_Object = MibTableRow
adEShdslPerf24HrIntEntry = _AdEShdslPerf24HrIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1)
)
adEShdslPerf24HrIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslPerf24HrIntNumber"),
)
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntEntry.setStatus("current")
_AdEShdslPerf24HrIntNumber_Type = Integer32
_AdEShdslPerf24HrIntNumber_Object = MibTableColumn
adEShdslPerf24HrIntNumber = _AdEShdslPerf24HrIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 1),
    _AdEShdslPerf24HrIntNumber_Type()
)
adEShdslPerf24HrIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntNumber.setStatus("current")
_AdEShdslPerf24HrIntES_Type = Integer32
_AdEShdslPerf24HrIntES_Object = MibTableColumn
adEShdslPerf24HrIntES = _AdEShdslPerf24HrIntES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 2),
    _AdEShdslPerf24HrIntES_Type()
)
adEShdslPerf24HrIntES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntES.setStatus("current")
_AdEShdslPerf24HrIntSES_Type = Integer32
_AdEShdslPerf24HrIntSES_Object = MibTableColumn
adEShdslPerf24HrIntSES = _AdEShdslPerf24HrIntSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 3),
    _AdEShdslPerf24HrIntSES_Type()
)
adEShdslPerf24HrIntSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntSES.setStatus("current")
_AdEShdslPerf24HrIntUAS_Type = Integer32
_AdEShdslPerf24HrIntUAS_Object = MibTableColumn
adEShdslPerf24HrIntUAS = _AdEShdslPerf24HrIntUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 4),
    _AdEShdslPerf24HrIntUAS_Type()
)
adEShdslPerf24HrIntUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntUAS.setStatus("current")
_AdEShdslPerf24HrIntCVC_Type = Integer32
_AdEShdslPerf24HrIntCVC_Object = MibTableColumn
adEShdslPerf24HrIntCVC = _AdEShdslPerf24HrIntCVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 5),
    _AdEShdslPerf24HrIntCVC_Type()
)
adEShdslPerf24HrIntCVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntCVC.setStatus("current")
_AdEShdslPerf24HrIntLOSWS_Type = Integer32
_AdEShdslPerf24HrIntLOSWS_Object = MibTableColumn
adEShdslPerf24HrIntLOSWS = _AdEShdslPerf24HrIntLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 6),
    _AdEShdslPerf24HrIntLOSWS_Type()
)
adEShdslPerf24HrIntLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntLOSWS.setStatus("current")
_AdEShdslPerf24HrIntOS_Type = Integer32
_AdEShdslPerf24HrIntOS_Object = MibTableColumn
adEShdslPerf24HrIntOS = _AdEShdslPerf24HrIntOS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 7),
    _AdEShdslPerf24HrIntOS_Type()
)
adEShdslPerf24HrIntOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntOS.setStatus("current")
_AdEShdslPerf24HrIntRetrains_Type = Integer32
_AdEShdslPerf24HrIntRetrains_Object = MibTableColumn
adEShdslPerf24HrIntRetrains = _AdEShdslPerf24HrIntRetrains_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 8),
    _AdEShdslPerf24HrIntRetrains_Type()
)
adEShdslPerf24HrIntRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntRetrains.setStatus("current")
_AdEShdslPerf24HrIntHandshakeFailures_Type = Integer32
_AdEShdslPerf24HrIntHandshakeFailures_Object = MibTableColumn
adEShdslPerf24HrIntHandshakeFailures = _AdEShdslPerf24HrIntHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 9),
    _AdEShdslPerf24HrIntHandshakeFailures_Type()
)
adEShdslPerf24HrIntHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntHandshakeFailures.setStatus("current")
_AdEShdslPerf24HrIntMinSNRMargin_Type = Integer32
_AdEShdslPerf24HrIntMinSNRMargin_Object = MibTableColumn
adEShdslPerf24HrIntMinSNRMargin = _AdEShdslPerf24HrIntMinSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 10),
    _AdEShdslPerf24HrIntMinSNRMargin_Type()
)
adEShdslPerf24HrIntMinSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntMinSNRMargin.setStatus("current")
_AdEShdslPerf24HrIntMaxSNRMargin_Type = Integer32
_AdEShdslPerf24HrIntMaxSNRMargin_Object = MibTableColumn
adEShdslPerf24HrIntMaxSNRMargin = _AdEShdslPerf24HrIntMaxSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 5, 1, 11),
    _AdEShdslPerf24HrIntMaxSNRMargin_Type()
)
adEShdslPerf24HrIntMaxSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslPerf24HrIntMaxSNRMargin.setStatus("current")
_AdEShdslPerfPortResetTable_Object = MibTable
adEShdslPerfPortResetTable = _AdEShdslPerfPortResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 6)
)
if mibBuilder.loadTexts:
    adEShdslPerfPortResetTable.setStatus("current")
_AdEShdslPerfPortResetEntry_Object = MibTableRow
adEShdslPerfPortResetEntry = _AdEShdslPerfPortResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 6, 1)
)
adEShdslPerfPortResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adEShdslPerfPortResetEntry.setStatus("current")


class _AdEShdslPerfPortReset_Type(Integer32):
    """Custom type adEShdslPerfPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdEShdslPerfPortReset_Type.__name__ = "Integer32"
_AdEShdslPerfPortReset_Object = MibTableColumn
adEShdslPerfPortReset = _AdEShdslPerfPortReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 6, 6, 1, 1),
    _AdEShdslPerfPortReset_Type()
)
adEShdslPerfPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslPerfPortReset.setStatus("current")
_AdEShdslSpliceDetection_ObjectIdentity = ObjectIdentity
adEShdslSpliceDetection = _AdEShdslSpliceDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7)
)
_AdEShdslSpliceDetectionTable_Object = MibTable
adEShdslSpliceDetectionTable = _AdEShdslSpliceDetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 1)
)
if mibBuilder.loadTexts:
    adEShdslSpliceDetectionTable.setStatus("current")
_AdEShdslSpliceDetectionEntry_Object = MibTableRow
adEShdslSpliceDetectionEntry = _AdEShdslSpliceDetectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 1, 1)
)
adEShdslSpliceDetectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
)
if mibBuilder.loadTexts:
    adEShdslSpliceDetectionEntry.setStatus("current")
_AdEShdslSpliceDetectionSummary_Type = DisplayString
_AdEShdslSpliceDetectionSummary_Object = MibTableColumn
adEShdslSpliceDetectionSummary = _AdEShdslSpliceDetectionSummary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 1, 1, 1),
    _AdEShdslSpliceDetectionSummary_Type()
)
adEShdslSpliceDetectionSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSpliceDetectionSummary.setStatus("current")
_AdEShdslSpliceCounts_Type = DisplayString
_AdEShdslSpliceCounts_Object = MibTableColumn
adEShdslSpliceCounts = _AdEShdslSpliceCounts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 1, 1, 2),
    _AdEShdslSpliceCounts_Type()
)
adEShdslSpliceCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSpliceCounts.setStatus("current")
_AdEShdslSpliceDistances_Type = DisplayString
_AdEShdslSpliceDistances_Object = MibTableColumn
adEShdslSpliceDistances = _AdEShdslSpliceDistances_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 1, 1, 3),
    _AdEShdslSpliceDistances_Type()
)
adEShdslSpliceDistances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSpliceDistances.setStatus("current")


class _AdEShdslSpliceRestart_Type(Integer32):
    """Custom type adEShdslSpliceRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_AdEShdslSpliceRestart_Type.__name__ = "Integer32"
_AdEShdslSpliceRestart_Object = MibTableColumn
adEShdslSpliceRestart = _AdEShdslSpliceRestart_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 1, 1, 4),
    _AdEShdslSpliceRestart_Type()
)
adEShdslSpliceRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslSpliceRestart.setStatus("current")


class _AdEShdslSpliceDistanceType_Type(Integer32):
    """Custom type adEShdslSpliceDistanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meters", 1),
          ("feet", 2))
    )


_AdEShdslSpliceDistanceType_Type.__name__ = "Integer32"
_AdEShdslSpliceDistanceType_Object = MibTableColumn
adEShdslSpliceDistanceType = _AdEShdslSpliceDistanceType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 1, 1, 5),
    _AdEShdslSpliceDistanceType_Type()
)
adEShdslSpliceDistanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adEShdslSpliceDistanceType.setStatus("current")
_AdEShdslSpliceRate_Type = Integer32
_AdEShdslSpliceRate_Object = MibTableColumn
adEShdslSpliceRate = _AdEShdslSpliceRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 1, 1, 6),
    _AdEShdslSpliceRate_Type()
)
adEShdslSpliceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSpliceRate.setStatus("current")
_AdEShdslSpliceBadSpliceDetected_Type = TruthValue
_AdEShdslSpliceBadSpliceDetected_Object = MibTableColumn
adEShdslSpliceBadSpliceDetected = _AdEShdslSpliceBadSpliceDetected_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 1, 1, 7),
    _AdEShdslSpliceBadSpliceDetected_Type()
)
adEShdslSpliceBadSpliceDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSpliceBadSpliceDetected.setStatus("current")
_AdEShdslSpliceDet24HrIntTable_Object = MibTable
adEShdslSpliceDet24HrIntTable = _AdEShdslSpliceDet24HrIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 2)
)
if mibBuilder.loadTexts:
    adEShdslSpliceDet24HrIntTable.setStatus("current")
_AdEShdslSpliceDet24HrIntEntry_Object = MibTableRow
adEShdslSpliceDet24HrIntEntry = _AdEShdslSpliceDet24HrIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 2, 1)
)
adEShdslSpliceDet24HrIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSpliceDet24HrIntNumber"),
)
if mibBuilder.loadTexts:
    adEShdslSpliceDet24HrIntEntry.setStatus("current")
_AdEShdslSpliceDet24HrIntNumber_Type = Integer32
_AdEShdslSpliceDet24HrIntNumber_Object = MibTableColumn
adEShdslSpliceDet24HrIntNumber = _AdEShdslSpliceDet24HrIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 2, 1, 1),
    _AdEShdslSpliceDet24HrIntNumber_Type()
)
adEShdslSpliceDet24HrIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSpliceDet24HrIntNumber.setStatus("current")
_AdEShdslSplice24HrIntCounts_Type = DisplayString
_AdEShdslSplice24HrIntCounts_Object = MibTableColumn
adEShdslSplice24HrIntCounts = _AdEShdslSplice24HrIntCounts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 2, 1, 2),
    _AdEShdslSplice24HrIntCounts_Type()
)
adEShdslSplice24HrIntCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSplice24HrIntCounts.setStatus("current")
_AdEShdslSplice24HrIntDistances_Type = DisplayString
_AdEShdslSplice24HrIntDistances_Object = MibTableColumn
adEShdslSplice24HrIntDistances = _AdEShdslSplice24HrIntDistances_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 2, 1, 3),
    _AdEShdslSplice24HrIntDistances_Type()
)
adEShdslSplice24HrIntDistances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSplice24HrIntDistances.setStatus("current")
_AdEShdslSplice24HrIntRate_Type = Integer32
_AdEShdslSplice24HrIntRate_Object = MibTableColumn
adEShdslSplice24HrIntRate = _AdEShdslSplice24HrIntRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 2, 1, 4),
    _AdEShdslSplice24HrIntRate_Type()
)
adEShdslSplice24HrIntRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSplice24HrIntRate.setStatus("current")
_AdEShdslSpliceDet15MinCurrTable_Object = MibTable
adEShdslSpliceDet15MinCurrTable = _AdEShdslSpliceDet15MinCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 3)
)
if mibBuilder.loadTexts:
    adEShdslSpliceDet15MinCurrTable.setStatus("current")
_AdEShdslSpliceDet15MinCurrEntry_Object = MibTableRow
adEShdslSpliceDet15MinCurrEntry = _AdEShdslSpliceDet15MinCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 3, 1)
)
adEShdslSpliceDet15MinCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
)
if mibBuilder.loadTexts:
    adEShdslSpliceDet15MinCurrEntry.setStatus("current")
_AdEShdslSplice15MinCurrCounts_Type = DisplayString
_AdEShdslSplice15MinCurrCounts_Object = MibTableColumn
adEShdslSplice15MinCurrCounts = _AdEShdslSplice15MinCurrCounts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 3, 1, 1),
    _AdEShdslSplice15MinCurrCounts_Type()
)
adEShdslSplice15MinCurrCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSplice15MinCurrCounts.setStatus("current")
_AdEShdslSplice15MinCurrDistances_Type = DisplayString
_AdEShdslSplice15MinCurrDistances_Object = MibTableColumn
adEShdslSplice15MinCurrDistances = _AdEShdslSplice15MinCurrDistances_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 3, 1, 2),
    _AdEShdslSplice15MinCurrDistances_Type()
)
adEShdslSplice15MinCurrDistances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSplice15MinCurrDistances.setStatus("current")
_AdEShdslSplice15MinCurrRate_Type = Integer32
_AdEShdslSplice15MinCurrRate_Object = MibTableColumn
adEShdslSplice15MinCurrRate = _AdEShdslSplice15MinCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 3, 1, 3),
    _AdEShdslSplice15MinCurrRate_Type()
)
adEShdslSplice15MinCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSplice15MinCurrRate.setStatus("current")
_AdEShdslSpliceDet15MinIntTable_Object = MibTable
adEShdslSpliceDet15MinIntTable = _AdEShdslSpliceDet15MinIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 4)
)
if mibBuilder.loadTexts:
    adEShdslSpliceDet15MinIntTable.setStatus("current")
_AdEShdslSpliceDet15MinIntEntry_Object = MibTableRow
adEShdslSpliceDet15MinIntEntry = _AdEShdslSpliceDet15MinIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 4, 1)
)
adEShdslSpliceDet15MinIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslSpliceDet15MinIntNumber"),
)
if mibBuilder.loadTexts:
    adEShdslSpliceDet15MinIntEntry.setStatus("current")
_AdEShdslSpliceDet15MinIntNumber_Type = Integer32
_AdEShdslSpliceDet15MinIntNumber_Object = MibTableColumn
adEShdslSpliceDet15MinIntNumber = _AdEShdslSpliceDet15MinIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 4, 1, 1),
    _AdEShdslSpliceDet15MinIntNumber_Type()
)
adEShdslSpliceDet15MinIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSpliceDet15MinIntNumber.setStatus("current")
_AdEShdslSplice15MinIntCounts_Type = DisplayString
_AdEShdslSplice15MinIntCounts_Object = MibTableColumn
adEShdslSplice15MinIntCounts = _AdEShdslSplice15MinIntCounts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 4, 1, 2),
    _AdEShdslSplice15MinIntCounts_Type()
)
adEShdslSplice15MinIntCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSplice15MinIntCounts.setStatus("current")
_AdEShdslSplice15MinIntDistances_Type = DisplayString
_AdEShdslSplice15MinIntDistances_Object = MibTableColumn
adEShdslSplice15MinIntDistances = _AdEShdslSplice15MinIntDistances_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 4, 1, 3),
    _AdEShdslSplice15MinIntDistances_Type()
)
adEShdslSplice15MinIntDistances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSplice15MinIntDistances.setStatus("current")
_AdEShdslSplice15MinIntRate_Type = Integer32
_AdEShdslSplice15MinIntRate_Object = MibTableColumn
adEShdslSplice15MinIntRate = _AdEShdslSplice15MinIntRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 7, 4, 1, 4),
    _AdEShdslSplice15MinIntRate_Type()
)
adEShdslSplice15MinIntRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEShdslSplice15MinIntRate.setStatus("current")
_AdEShdslMibConformance_ObjectIdentity = ObjectIdentity
adEShdslMibConformance = _AdEShdslMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8)
)
_AdEShdslMibGroups_ObjectIdentity = ObjectIdentity
adEShdslMibGroups = _AdEShdslMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1)
)
_AdEShdslAlarmsPrefix_ObjectIdentity = ObjectIdentity
adEShdslAlarmsPrefix = _AdEShdslAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10)
)
_AdEShdslAlarms_ObjectIdentity = ObjectIdentity
adEShdslAlarms = _AdEShdslAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0)
)
_AdEShdslProductInfo_ObjectIdentity = ObjectIdentity
adEShdslProductInfo = _AdEShdslProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 11)
)

# Managed Objects groups

adGenEShdslIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 1)
)
adGenEShdslIndexGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adGenEShdslIndexGroup.setStatus("current")

adGenEShdslInvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 2)
)
adGenEShdslInvGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslInvVendorID"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvVendorModelNumber"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvVendorSerialNumber"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvStandardVersion"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvVendorListNumber"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvVendorIssueNumber"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvVendorSoftwareVersion"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvEquipmentCode"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvVendorOther"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvVendorEOCSoftwareVersion"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvMfrDate"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvCircuitID"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvScratchPad"))
)
if mibBuilder.loadTexts:
    adGenEShdslInvGroup.setStatus("current")

adGenEShdslProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 3)
)
adGenEShdslProvGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslProvWireInterfaceMode"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvMinLineRate"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvMaxLineRate"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvG9912Annex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvCurrCondTargetMargin"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvWorstCaseTargetMargin"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvUsedTargetMargins"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvClockMode"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvLineProbing"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvConstellation"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvPowerBackoff"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvLoopAttenThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvSNRMarginThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvESThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvSESThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvUASThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvCVCThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvLOSWSThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvOSThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslTestProvLoopbackTimeout"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvES24HrThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvSES24HrThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvUAS24HrThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvCVC24HrThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvLOSWS24HrThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslAlarmProvOS24HrThresh"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvName"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvSpanPower"),
        ("ADTRAN-SHDSL-MIB", "adEShdslProvNIUloopback"),
        ("ADTRAN-SHDSL-MIB", "adEShdslTestProvEnumeratedLoopbackTimeout"))
)
if mibBuilder.loadTexts:
    adGenEShdslProvGroup.setStatus("current")

adGenEShdslStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 4)
)
adGenEShdslStatusGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslStatusCurrStatus"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusCurrLoopAtten"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusMinLoopAtten"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusMaxLoopAtten"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusCurrSNRMargin"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusMinSNRMargin"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusMaxSNRMargin"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusSES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusUAS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusCVC"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusLOSWS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusOS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusResetStatistics"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusMaxAttainableRate"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusUpstreamPBO"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusDownstreamPBO"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusCurrRate"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusInfoRepeaterNumber"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusInfoPairReversal"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusInfoLoopAlarmStatus"),
        ("ADTRAN-SHDSL-MIB", "adEShdslStatusIfTrainingMode"))
)
if mibBuilder.loadTexts:
    adGenEShdslStatusGroup.setStatus("current")

adGenEShdslTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 5)
)
adGenEShdslTestGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslTestLoopback"),
        ("ADTRAN-SHDSL-MIB", "adEShdslTestLoopdownAll"),
        ("ADTRAN-SHDSL-MIB", "adEShdslTestinitMinMax"))
)
if mibBuilder.loadTexts:
    adGenEShdslTestGroup.setStatus("current")

adGenEShdslCurr15MinPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 6)
)
adGenEShdslCurr15MinPerfGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr15MinES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr15MinSES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr15MinUAS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr15MinCVC"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr15MinLOSWS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr15MinOS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf15MinValidIntervals"))
)
if mibBuilder.loadTexts:
    adGenEShdslCurr15MinPerfGroup.setStatus("current")

adGenEShdslCurr24HrPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 7)
)
adGenEShdslCurr24HrPerfGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr24HrES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr24HrSES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr24HrUAS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr24HrCVC"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr24HrLOSWS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfCurr24HrOS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf24HrValidIntervals"))
)
if mibBuilder.loadTexts:
    adGenEShdslCurr24HrPerfGroup.setStatus("current")

adGenEShdslPrior15MinPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 8)
)
adGenEShdslPrior15MinPerfGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior15MinES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior15MinSES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior15MinUAS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior15MinCVC"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior15MinLOSWS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior15MinOS"))
)
if mibBuilder.loadTexts:
    adGenEShdslPrior15MinPerfGroup.setStatus("current")

adGenEShdslPrior24HrPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 9)
)
adGenEShdslPrior24HrPerfGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior24HrES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior24HrSES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior24HrUAS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior24HrCVC"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior24HrLOSWS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPrior24HrOS"))
)
if mibBuilder.loadTexts:
    adGenEShdslPrior24HrPerfGroup.setStatus("current")

adGenEShdslInt15MinPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 10)
)
adGenEShdslInt15MinPerfGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslPerf15MinIntNumber"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf15MinIntES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf15MinIntSES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf15MinIntUAS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf15MinIntCVC"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf15MinIntLOSWS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf15MinIntOS"))
)
if mibBuilder.loadTexts:
    adGenEShdslInt15MinPerfGroup.setStatus("current")

adGenEShdslInt24HrPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 11)
)
adGenEShdslInt24HrPerfGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslPerf24HrIntNumber"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf24HrIntES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf24HrIntSES"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf24HrIntUAS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf24HrIntCVC"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf24HrIntLOSWS"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerf24HrIntOS"))
)
if mibBuilder.loadTexts:
    adGenEShdslInt24HrPerfGroup.setStatus("current")

adGenEShdslSpliceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 12)
)
adGenEShdslSpliceGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslSpliceDetectionSummary"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSpliceCounts"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSpliceDistances"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSpliceRestart"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSpliceDistanceType"))
)
if mibBuilder.loadTexts:
    adGenEShdslSpliceGroup.setStatus("current")

adGenEShdslInt24HrSpliceDetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 14)
)
adGenEShdslInt24HrSpliceDetGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslSpliceDet24HrIntNumber"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSplice24HrIntCounts"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSplice24HrIntDistances"))
)
if mibBuilder.loadTexts:
    adGenEShdslInt24HrSpliceDetGroup.setStatus("current")

adGenEShdslPerfResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 15)
)
adGenEShdslPerfResetGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslPerfReset"),
        ("ADTRAN-SHDSL-MIB", "adEShdslPerfPortReset"))
)
if mibBuilder.loadTexts:
    adGenEShdslPerfResetGroup.setStatus("current")


# Notification objects

adEShdslLossofSignalAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 2)
)
adEShdslLossofSignalAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLossofSignalAlmCLR.setStatus(
        "current"
    )

adEShdslLossofSignalAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 3)
)
adEShdslLossofSignalAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLossofSignalAlmACT.setStatus(
        "current"
    )

adEShdslLTULossofSyncWordAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 4)
)
adEShdslLTULossofSyncWordAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTULossofSyncWordAlmCLR.setStatus(
        "current"
    )

adEShdslLTULossofSyncWordAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 5)
)
adEShdslLTULossofSyncWordAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTULossofSyncWordAlmACT.setStatus(
        "current"
    )

adEShdslLTUCRCErrorAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 6)
)
adEShdslLTUCRCErrorAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUCRCErrorAlmCLR.setStatus(
        "current"
    )

adEShdslLTUCRCErrorAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 7)
)
adEShdslLTUCRCErrorAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUCRCErrorAlmACT.setStatus(
        "current"
    )

adEShdslLTUSNRMarginAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 8)
)
adEShdslLTUSNRMarginAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUSNRMarginAlmCLR.setStatus(
        "current"
    )

adEShdslLTUSNRMarginAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 9)
)
adEShdslLTUSNRMarginAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUSNRMarginAlmACT.setStatus(
        "current"
    )

adEShdslLTULoopAttenAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 10)
)
adEShdslLTULoopAttenAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTULoopAttenAlmCLR.setStatus(
        "current"
    )

adEShdslLTULoopAttenAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 11)
)
adEShdslLTULoopAttenAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTULoopAttenAlmACT.setStatus(
        "current"
    )

adEShdslNTULossofSyncWordAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 12)
)
adEShdslNTULossofSyncWordAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTULossofSyncWordAlmCLR.setStatus(
        "current"
    )

adEShdslNTULossofSyncWordAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 13)
)
adEShdslNTULossofSyncWordAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTULossofSyncWordAlmACT.setStatus(
        "current"
    )

adEShdslNTUCRCErrorAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 14)
)
adEShdslNTUCRCErrorAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUCRCErrorAlmCLR.setStatus(
        "current"
    )

adEShdslNTUCRCErrorAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 15)
)
adEShdslNTUCRCErrorAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUCRCErrorAlmACT.setStatus(
        "current"
    )

adEShdslNTUSNRMarginAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 16)
)
adEShdslNTUSNRMarginAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUSNRMarginAlmCLR.setStatus(
        "current"
    )

adEShdslNTUSNRMarginAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 17)
)
adEShdslNTUSNRMarginAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUSNRMarginAlmACT.setStatus(
        "current"
    )

adEShdslNTULoopAttenAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 18)
)
adEShdslNTULoopAttenAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTULoopAttenAlmCLR.setStatus(
        "current"
    )

adEShdslNTULoopAttenAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 19)
)
adEShdslNTULoopAttenAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTULoopAttenAlmACT.setStatus(
        "current"
    )

adEShdslLTUESThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 20)
)
adEShdslLTUESThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUESThreshCrossed.setStatus(
        "current"
    )

adEShdslLTUSESThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 21)
)
adEShdslLTUSESThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUSESThreshCrossed.setStatus(
        "current"
    )

adEShdslLTUUASThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 22)
)
adEShdslLTUUASThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUUASThreshCrossed.setStatus(
        "current"
    )

adEShdslLTUCVCThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 23)
)
adEShdslLTUCVCThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUCVCThreshCrossed.setStatus(
        "current"
    )

adEShdslLTULOSWSThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 24)
)
adEShdslLTULOSWSThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTULOSWSThreshCrossed.setStatus(
        "current"
    )

adEShdslLTUOSThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 25)
)
adEShdslLTUOSThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUOSThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUESThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 26)
)
adEShdslNTUESThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUESThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUSESThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 27)
)
adEShdslNTUSESThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUSESThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUUASThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 28)
)
adEShdslNTUUASThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUUASThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUCVCThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 29)
)
adEShdslNTUCVCThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUCVCThreshCrossed.setStatus(
        "current"
    )

adEShdslNTULOSWSThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 30)
)
adEShdslNTULOSWSThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTULOSWSThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUOSThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 31)
)
adEShdslNTUOSThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUOSThreshCrossed.setStatus(
        "current"
    )

adEShdslRemoteLossOfPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 32)
)
adEShdslRemoteLossOfPower.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslRemoteLossOfPower.setStatus(
        "current"
    )

adEShdslLTUES24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 33)
)
adEShdslLTUES24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUES24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslLTUSES24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 34)
)
adEShdslLTUSES24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUSES24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslLTUUAS24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 35)
)
adEShdslLTUUAS24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUUAS24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslLTUCVC24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 36)
)
adEShdslLTUCVC24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUCVC24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslLTULOSWS24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 37)
)
adEShdslLTULOSWS24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTULOSWS24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslLTUOS24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 38)
)
adEShdslLTUOS24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslLTUOS24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUES24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 39)
)
adEShdslNTUES24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUES24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUSES24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 40)
)
adEShdslNTUSES24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUSES24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUUAS24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 41)
)
adEShdslNTUUAS24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUUAS24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUCVC24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 42)
)
adEShdslNTUCVC24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUCVC24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslNTULOSWS24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 43)
)
adEShdslNTULOSWS24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTULOSWS24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslNTUOS24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 44)
)
adEShdslNTUOS24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslNTUOS24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenLossofSignalAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 45)
)
adEShdslRegenLossofSignalAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenLossofSignalAlmCLR.setStatus(
        "current"
    )

adEShdslRegenLossofSignalAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 46)
)
adEShdslRegenLossofSignalAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenLossofSignalAlmACT.setStatus(
        "current"
    )

adEShdslRegenLossofSyncWordAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 47)
)
adEShdslRegenLossofSyncWordAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenLossofSyncWordAlmCLR.setStatus(
        "current"
    )

adEShdslRegenLossofSyncWordAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 48)
)
adEShdslRegenLossofSyncWordAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenLossofSyncWordAlmACT.setStatus(
        "current"
    )

adEShdslRegenCRCErrorAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 49)
)
adEShdslRegenCRCErrorAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenCRCErrorAlmCLR.setStatus(
        "current"
    )

adEShdslRegenCRCErrorAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 50)
)
adEShdslRegenCRCErrorAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenCRCErrorAlmACT.setStatus(
        "current"
    )

adEShdslRegenSNRMarginAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 51)
)
adEShdslRegenSNRMarginAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenSNRMarginAlmCLR.setStatus(
        "current"
    )

adEShdslRegenSNRMarginAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 52)
)
adEShdslRegenSNRMarginAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenSNRMarginAlmACT.setStatus(
        "current"
    )

adEShdslRegenLoopAttenAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 53)
)
adEShdslRegenLoopAttenAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenLoopAttenAlmCLR.setStatus(
        "current"
    )

adEShdslRegenLoopAttenAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 54)
)
adEShdslRegenLoopAttenAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenLoopAttenAlmACT.setStatus(
        "current"
    )

adEShdslRegenESThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 55)
)
adEShdslRegenESThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenESThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenSESThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 56)
)
adEShdslRegenSESThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenSESThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenUASThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 57)
)
adEShdslRegenUASThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenUASThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenCVCThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 58)
)
adEShdslRegenCVCThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenCVCThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenLOSWSThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 59)
)
adEShdslRegenLOSWSThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenLOSWSThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenOSThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 60)
)
adEShdslRegenOSThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenOSThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenES24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 61)
)
adEShdslRegenES24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenES24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenSES24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 62)
)
adEShdslRegenSES24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenSES24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenUAS24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 63)
)
adEShdslRegenUAS24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenUAS24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenCVC24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 64)
)
adEShdslRegenCVC24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenCVC24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenLOSWS24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 65)
)
adEShdslRegenLOSWS24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenLOSWS24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslRegenOS24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 66)
)
adEShdslRegenOS24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslRegenOS24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslLoopbackEnabledCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 71)
)
adEShdslLoopbackEnabledCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslLoopbackEnabledCLR.setStatus(
        "current"
    )

adEShdslLoopbackEnabledACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 72)
)
adEShdslLoopbackEnabledACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslWirePairIndex"))
)
if mibBuilder.loadTexts:
    adEShdslLoopbackEnabledACT.setStatus(
        "current"
    )

adEShdslRetrains15MinThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 80)
)
adEShdslRetrains15MinThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslRetrains15MinThreshCrossed.setStatus(
        "current"
    )

adEShdslHandshakeFailures15MinThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 81)
)
adEShdslHandshakeFailures15MinThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslHandshakeFailures15MinThreshCrossed.setStatus(
        "current"
    )

adEShdslRetrains24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 82)
)
adEShdslRetrains24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslRetrains24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslHandshakeFailures24HrThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 83)
)
adEShdslHandshakeFailures24HrThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adEShdslHandshakeFailures24HrThreshCrossed.setStatus(
        "current"
    )

adEShdslBadSpliceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 84)
)
adEShdslBadSpliceDetected.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvPhysicalLinkId"))
)
if mibBuilder.loadTexts:
    adEShdslBadSpliceDetected.setStatus(
        "current"
    )

adEShdslSruShortDetectAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 85)
)
adEShdslSruShortDetectAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvPhysicalLinkId"))
)
if mibBuilder.loadTexts:
    adEShdslSruShortDetectAlmCLR.setStatus(
        "current"
    )

adEShdslSruShortDetectAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 86)
)
adEShdslSruShortDetectAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvPhysicalLinkId"))
)
if mibBuilder.loadTexts:
    adEShdslSruShortDetectAlmACT.setStatus(
        "current"
    )

adEShdslSruGroundFaultDetectAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 87)
)
adEShdslSruGroundFaultDetectAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvPhysicalLinkId"))
)
if mibBuilder.loadTexts:
    adEShdslSruGroundFaultDetectAlmCLR.setStatus(
        "current"
    )

adEShdslSruGroundFaultDetectAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 88)
)
adEShdslSruGroundFaultDetectAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslSideIndex"),
        ("ADTRAN-SHDSL-MIB", "adEShdslInvPhysicalLinkId"))
)
if mibBuilder.loadTexts:
    adEShdslSruGroundFaultDetectAlmACT.setStatus(
        "current"
    )

adEShdslSCIThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 10, 0, 89)
)
adEShdslSCIThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adEShdslSCIThreshCrossed.setStatus(
        "current"
    )


# Notifications groups

adGenEShdslEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 1, 8, 1, 13)
)
adGenEShdslEventGroup.setObjects(
      *(("ADTRAN-SHDSL-MIB", "adEShdslLossofSignalAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLossofSignalAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTULossofSyncWordAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTULossofSyncWordAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUCRCErrorAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUCRCErrorAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUSNRMarginAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUSNRMarginAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTULoopAttenAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTULoopAttenAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTULossofSyncWordAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTULossofSyncWordAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUCRCErrorAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUCRCErrorAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUSNRMarginAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUSNRMarginAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTULoopAttenAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTULoopAttenAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUESThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUSESThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUUASThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUCVCThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTULOSWSThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUOSThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUESThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUSESThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUUASThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUCVCThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTULOSWSThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUOSThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRemoteLossOfPower"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenLossofSignalAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenLossofSignalAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenLossofSyncWordAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenLossofSyncWordAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenCRCErrorAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenCRCErrorAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenSNRMarginAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenSNRMarginAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenLoopAttenAlmCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenLoopAttenAlmACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenESThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenSESThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenUASThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenCVCThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenLOSWSThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslRegenOSThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLoopbackEnabledCLR"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLoopbackEnabledACT"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUES24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUSES24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUUAS24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUCVC24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTULOSWS24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslLTUOS24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUES24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUSES24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUUAS24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUCVC24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTULOSWS24HrThreshCrossed"),
        ("ADTRAN-SHDSL-MIB", "adEShdslNTUOS24HrThreshCrossed"))
)
if mibBuilder.loadTexts:
    adGenEShdslEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-SHDSL-MIB",
    **{"AdEShdslUnitId": AdEShdslUnitId,
       "AdEShdslUnitSide": AdEShdslUnitSide,
       "AdEShdslWirePair": AdEShdslWirePair,
       "adEShdslIndex": adEShdslIndex,
       "adEShdslIndexTable": adEShdslIndexTable,
       "adEShdslIndexEntry": adEShdslIndexEntry,
       "adEShdslInvIndex": adEShdslInvIndex,
       "adEShdslSideIndex": adEShdslSideIndex,
       "adEShdslWirePairIndex": adEShdslWirePairIndex,
       "adEShdslInventory": adEShdslInventory,
       "adEShdslInventoryTable": adEShdslInventoryTable,
       "adEShdslInventoryEntry": adEShdslInventoryEntry,
       "adEShdslInvVendorID": adEShdslInvVendorID,
       "adEShdslInvVendorModelNumber": adEShdslInvVendorModelNumber,
       "adEShdslInvVendorSerialNumber": adEShdslInvVendorSerialNumber,
       "adEShdslInvStandardVersion": adEShdslInvStandardVersion,
       "adEShdslInvVendorListNumber": adEShdslInvVendorListNumber,
       "adEShdslInvVendorIssueNumber": adEShdslInvVendorIssueNumber,
       "adEShdslInvVendorSoftwareVersion": adEShdslInvVendorSoftwareVersion,
       "adEShdslInvEquipmentCode": adEShdslInvEquipmentCode,
       "adEShdslInvVendorOther": adEShdslInvVendorOther,
       "adEShdslInvVendorEOCSoftwareVersion": adEShdslInvVendorEOCSoftwareVersion,
       "adEShdslInvMfrDate": adEShdslInvMfrDate,
       "adEShdslInvCircuitID": adEShdslInvCircuitID,
       "adEShdslInvScratchPad": adEShdslInvScratchPad,
       "adEShdslInvDspHwVersion": adEShdslInvDspHwVersion,
       "adEShdslInvDspFwVersion": adEShdslInvDspFwVersion,
       "adEShdslInvElementPresent": adEShdslInvElementPresent,
       "adEShdslInvPhysicalLinkId": adEShdslInvPhysicalLinkId,
       "adEShdslProvisioning": adEShdslProvisioning,
       "adEShdslProvTable": adEShdslProvTable,
       "adEShdslProvEntry": adEShdslProvEntry,
       "adEShdslProvWireInterfaceMode": adEShdslProvWireInterfaceMode,
       "adEShdslProvMinLineRate": adEShdslProvMinLineRate,
       "adEShdslProvMaxLineRate": adEShdslProvMaxLineRate,
       "adEShdslProvG9912Annex": adEShdslProvG9912Annex,
       "adEShdslProvCurrCondTargetMargin": adEShdslProvCurrCondTargetMargin,
       "adEShdslProvWorstCaseTargetMargin": adEShdslProvWorstCaseTargetMargin,
       "adEShdslProvUsedTargetMargins": adEShdslProvUsedTargetMargins,
       "adEShdslProvClockMode": adEShdslProvClockMode,
       "adEShdslProvLineProbing": adEShdslProvLineProbing,
       "adEShdslProvConstellation": adEShdslProvConstellation,
       "adEShdslProvPowerBackoff": adEShdslProvPowerBackoff,
       "adEShdslProvName": adEShdslProvName,
       "adEShdslProvSpanPower": adEShdslProvSpanPower,
       "adEShdslProvNIUloopback": adEShdslProvNIUloopback,
       "adEShdslProvConstellationCrossoverRate": adEShdslProvConstellationCrossoverRate,
       "adEShdslProvAnfp100KhzLoss": adEShdslProvAnfp100KhzLoss,
       "adEShdslProvAnfpTargetMargin": adEShdslProvAnfpTargetMargin,
       "adEShdslProvEmergencyFreeze": adEShdslProvEmergencyFreeze,
       "adEShdslProvExtendedFixedRateAndConstellation": adEShdslProvExtendedFixedRateAndConstellation,
       "adEShdslProvExtendedFixedLastError": adEShdslProvExtendedFixedLastError,
       "adEShdslProvAnfp100KhzLossLetter": adEShdslProvAnfp100KhzLossLetter,
       "adEShdslProvAnfpMaxLineRate": adEShdslProvAnfpMaxLineRate,
       "adEShdslProvSCIAlarmThresh": adEShdslProvSCIAlarmThresh,
       "adEShdslProvSCIAlarmSeverity": adEShdslProvSCIAlarmSeverity,
       "adEShdslAlarmProvTable": adEShdslAlarmProvTable,
       "adEShdslAlarmProvEntry": adEShdslAlarmProvEntry,
       "adEShdslAlarmProvLoopAttenThresh": adEShdslAlarmProvLoopAttenThresh,
       "adEShdslAlarmProvSNRMarginThresh": adEShdslAlarmProvSNRMarginThresh,
       "adEShdslAlarmProvESThresh": adEShdslAlarmProvESThresh,
       "adEShdslAlarmProvSESThresh": adEShdslAlarmProvSESThresh,
       "adEShdslAlarmProvUASThresh": adEShdslAlarmProvUASThresh,
       "adEShdslAlarmProvCVCThresh": adEShdslAlarmProvCVCThresh,
       "adEShdslAlarmProvLOSWSThresh": adEShdslAlarmProvLOSWSThresh,
       "adEShdslAlarmProvOSThresh": adEShdslAlarmProvOSThresh,
       "adEShdslAlarmProvES24HrThresh": adEShdslAlarmProvES24HrThresh,
       "adEShdslAlarmProvSES24HrThresh": adEShdslAlarmProvSES24HrThresh,
       "adEShdslAlarmProvUAS24HrThresh": adEShdslAlarmProvUAS24HrThresh,
       "adEShdslAlarmProvCVC24HrThresh": adEShdslAlarmProvCVC24HrThresh,
       "adEShdslAlarmProvLOSWS24HrThresh": adEShdslAlarmProvLOSWS24HrThresh,
       "adEShdslAlarmProvOS24HrThresh": adEShdslAlarmProvOS24HrThresh,
       "adEShdslAlarmProvRetrains15MinThresh": adEShdslAlarmProvRetrains15MinThresh,
       "adEShdslAlarmProvHandshakeFailures15MinThresh": adEShdslAlarmProvHandshakeFailures15MinThresh,
       "adEShdslAlarmProvRetrains24HrThresh": adEShdslAlarmProvRetrains24HrThresh,
       "adEShdslAlarmProvHandshakeFailures24HrThresh": adEShdslAlarmProvHandshakeFailures24HrThresh,
       "adEShdslTestProvTable": adEShdslTestProvTable,
       "adEShdslTestProvEntry": adEShdslTestProvEntry,
       "adEShdslTestProvLoopbackTimeout": adEShdslTestProvLoopbackTimeout,
       "adEShdslTestProvEnumeratedLoopbackTimeout": adEShdslTestProvEnumeratedLoopbackTimeout,
       "adEShdslStatus": adEShdslStatus,
       "adEShdslStatusTable": adEShdslStatusTable,
       "adEShdslStatusEntry": adEShdslStatusEntry,
       "adEShdslStatusCurrStatus": adEShdslStatusCurrStatus,
       "adEShdslStatusCurrLoopAtten": adEShdslStatusCurrLoopAtten,
       "adEShdslStatusMinLoopAtten": adEShdslStatusMinLoopAtten,
       "adEShdslStatusMaxLoopAtten": adEShdslStatusMaxLoopAtten,
       "adEShdslStatusCurrSNRMargin": adEShdslStatusCurrSNRMargin,
       "adEShdslStatusMinSNRMargin": adEShdslStatusMinSNRMargin,
       "adEShdslStatusMaxSNRMargin": adEShdslStatusMaxSNRMargin,
       "adEShdslStatusES": adEShdslStatusES,
       "adEShdslStatusSES": adEShdslStatusSES,
       "adEShdslStatusUAS": adEShdslStatusUAS,
       "adEShdslStatusCVC": adEShdslStatusCVC,
       "adEShdslStatusLOSWS": adEShdslStatusLOSWS,
       "adEShdslStatusOS": adEShdslStatusOS,
       "adEShdslStatusResetStatistics": adEShdslStatusResetStatistics,
       "adEShdslStatusMaxAttainableRate": adEShdslStatusMaxAttainableRate,
       "adEShdslStatusUpstreamPBO": adEShdslStatusUpstreamPBO,
       "adEShdslStatusDownstreamPBO": adEShdslStatusDownstreamPBO,
       "adEShdslStatusCurrRate": adEShdslStatusCurrRate,
       "adEShdslStatusRetrains": adEShdslStatusRetrains,
       "adEShdslStatusHandshakeFailures": adEShdslStatusHandshakeFailures,
       "adEShdslStatusCurrSNRMarginCurrTrain": adEShdslStatusCurrSNRMarginCurrTrain,
       "adEShdslStatusMinSNRMarginCurrTrain": adEShdslStatusMinSNRMarginCurrTrain,
       "adEShdslStatusMaxSNRMarginCurrTrain": adEShdslStatusMaxSNRMarginCurrTrain,
       "adEShdslStatusMinSNRMarginPrevTrain": adEShdslStatusMinSNRMarginPrevTrain,
       "adEShdslStatusMaxSNRMarginPrevTrain": adEShdslStatusMaxSNRMarginPrevTrain,
       "adEShdslStatusPhysicalLinkLabel": adEShdslStatusPhysicalLinkLabel,
       "adEShdslStatusInfoTable": adEShdslStatusInfoTable,
       "adEShdslStatusInfoEntry": adEShdslStatusInfoEntry,
       "adEShdslStatusInfoRepeaterNumber": adEShdslStatusInfoRepeaterNumber,
       "adEShdslStatusInfoPairReversal": adEShdslStatusInfoPairReversal,
       "adEShdslStatusInfoLoopAlarmStatus": adEShdslStatusInfoLoopAlarmStatus,
       "adEShdslStatusInfoTopology": adEShdslStatusInfoTopology,
       "adEShdslStatusIfTable": adEShdslStatusIfTable,
       "adEShdslStatusIfEntry": adEShdslStatusIfEntry,
       "adEShdslStatusIfTrainingMode": adEShdslStatusIfTrainingMode,
       "adEShdslTest": adEShdslTest,
       "adEShdslTestTable": adEShdslTestTable,
       "adEShdslTestEntry": adEShdslTestEntry,
       "adEShdslTestLoopback": adEShdslTestLoopback,
       "adEShdslTestLoopdownAll": adEShdslTestLoopdownAll,
       "adEShdslTestinitMinMax": adEShdslTestinitMinMax,
       "adEShdslTestRepeaterPoweringTable": adEShdslTestRepeaterPoweringTable,
       "adEShdslTestRepeaterPoweringEntry": adEShdslTestRepeaterPoweringEntry,
       "adEShdslTestRepeaterPoweringState": adEShdslTestRepeaterPoweringState,
       "adEShdslTestRepeaterPoweringNumRepeaters": adEShdslTestRepeaterPoweringNumRepeaters,
       "adEShdslTestRepeaterPoweringTimeout": adEShdslTestRepeaterPoweringTimeout,
       "adEShdslTestRepeaterPoweringTimeRemaining": adEShdslTestRepeaterPoweringTimeRemaining,
       "adEShdslTestRepeaterPoweringSRU1Discovered": adEShdslTestRepeaterPoweringSRU1Discovered,
       "adEShdslTestRepeaterPoweringSRU2Discovered": adEShdslTestRepeaterPoweringSRU2Discovered,
       "adEShdslTestRepeaterPoweringSRU3Discovered": adEShdslTestRepeaterPoweringSRU3Discovered,
       "adEShdslTestRepeaterPoweringSRU4Discovered": adEShdslTestRepeaterPoweringSRU4Discovered,
       "adEShdslTestRepeaterPoweringShortDetected": adEShdslTestRepeaterPoweringShortDetected,
       "adEShdslTestRepeaterPoweringGroundFaultDetected": adEShdslTestRepeaterPoweringGroundFaultDetected,
       "adEShdslTestRepeaterPoweringLastErrorString": adEShdslTestRepeaterPoweringLastErrorString,
       "adEShdslTestLoopLocatorLastErrorTable": adEShdslTestLoopLocatorLastErrorTable,
       "adEShdslTestLoopLocatorLastErrorEntry": adEShdslTestLoopLocatorLastErrorEntry,
       "adEShdslTestLoopLocatorLastErrorString": adEShdslTestLoopLocatorLastErrorString,
       "adEShdslTestLoopLocatorTable": adEShdslTestLoopLocatorTable,
       "adEShdslTestLoopLocatorEntry": adEShdslTestLoopLocatorEntry,
       "adEShdslTestLoopLocatorState": adEShdslTestLoopLocatorState,
       "adEShdslTestLoopLocatorTimeout": adEShdslTestLoopLocatorTimeout,
       "adEShdslTestLoopLocatorTimeRemaining": adEShdslTestLoopLocatorTimeRemaining,
       "adEShdslPerformance": adEShdslPerformance,
       "adEShdslPerfCurrTable": adEShdslPerfCurrTable,
       "adEShdslPerfCurrEntry": adEShdslPerfCurrEntry,
       "adEShdslPerfCurr15MinES": adEShdslPerfCurr15MinES,
       "adEShdslPerfCurr15MinSES": adEShdslPerfCurr15MinSES,
       "adEShdslPerfCurr15MinUAS": adEShdslPerfCurr15MinUAS,
       "adEShdslPerfCurr15MinCVC": adEShdslPerfCurr15MinCVC,
       "adEShdslPerfCurr15MinLOSWS": adEShdslPerfCurr15MinLOSWS,
       "adEShdslPerfCurr15MinOS": adEShdslPerfCurr15MinOS,
       "adEShdslPerfCurr24HrES": adEShdslPerfCurr24HrES,
       "adEShdslPerfCurr24HrSES": adEShdslPerfCurr24HrSES,
       "adEShdslPerfCurr24HrUAS": adEShdslPerfCurr24HrUAS,
       "adEShdslPerfCurr24HrCVC": adEShdslPerfCurr24HrCVC,
       "adEShdslPerfCurr24HrLOSWS": adEShdslPerfCurr24HrLOSWS,
       "adEShdslPerfCurr24HrOS": adEShdslPerfCurr24HrOS,
       "adEShdslPerf15MinValidIntervals": adEShdslPerf15MinValidIntervals,
       "adEShdslPerf24HrValidIntervals": adEShdslPerf24HrValidIntervals,
       "adEShdslPerfCurr15MinRetrains": adEShdslPerfCurr15MinRetrains,
       "adEShdslPerfCurr15MinHandshakeFailures": adEShdslPerfCurr15MinHandshakeFailures,
       "adEShdslPerfCurr24HrRetrains": adEShdslPerfCurr24HrRetrains,
       "adEShdslPerfCurr24HrHandshakeFailures": adEShdslPerfCurr24HrHandshakeFailures,
       "adEShdslPerfCurr15MinMinSNRMargin": adEShdslPerfCurr15MinMinSNRMargin,
       "adEShdslPerfCurr15MinMaxSNRMargin": adEShdslPerfCurr15MinMaxSNRMargin,
       "adEShdslPerfCurr24HrMinSNRMargin": adEShdslPerfCurr24HrMinSNRMargin,
       "adEShdslPerfCurr24HrMaxSNRMargin": adEShdslPerfCurr24HrMaxSNRMargin,
       "adEShdslPerfPriorTable": adEShdslPerfPriorTable,
       "adEShdslPerfPriorEntry": adEShdslPerfPriorEntry,
       "adEShdslPerfPrior15MinES": adEShdslPerfPrior15MinES,
       "adEShdslPerfPrior15MinSES": adEShdslPerfPrior15MinSES,
       "adEShdslPerfPrior15MinUAS": adEShdslPerfPrior15MinUAS,
       "adEShdslPerfPrior15MinCVC": adEShdslPerfPrior15MinCVC,
       "adEShdslPerfPrior15MinLOSWS": adEShdslPerfPrior15MinLOSWS,
       "adEShdslPerfPrior15MinOS": adEShdslPerfPrior15MinOS,
       "adEShdslPerfPrior24HrES": adEShdslPerfPrior24HrES,
       "adEShdslPerfPrior24HrSES": adEShdslPerfPrior24HrSES,
       "adEShdslPerfPrior24HrUAS": adEShdslPerfPrior24HrUAS,
       "adEShdslPerfPrior24HrCVC": adEShdslPerfPrior24HrCVC,
       "adEShdslPerfPrior24HrLOSWS": adEShdslPerfPrior24HrLOSWS,
       "adEShdslPerfPrior24HrOS": adEShdslPerfPrior24HrOS,
       "adEShdslPerfResetTable": adEShdslPerfResetTable,
       "adEShdslPerfResetEntry": adEShdslPerfResetEntry,
       "adEShdslPerfReset": adEShdslPerfReset,
       "adEShdslPerf15MinIntTable": adEShdslPerf15MinIntTable,
       "adEShdslPerf15MinIntEntry": adEShdslPerf15MinIntEntry,
       "adEShdslPerf15MinIntNumber": adEShdslPerf15MinIntNumber,
       "adEShdslPerf15MinIntES": adEShdslPerf15MinIntES,
       "adEShdslPerf15MinIntSES": adEShdslPerf15MinIntSES,
       "adEShdslPerf15MinIntUAS": adEShdslPerf15MinIntUAS,
       "adEShdslPerf15MinIntCVC": adEShdslPerf15MinIntCVC,
       "adEShdslPerf15MinIntLOSWS": adEShdslPerf15MinIntLOSWS,
       "adEShdslPerf15MinIntOS": adEShdslPerf15MinIntOS,
       "adEShdslPerf15MinIntRetrains": adEShdslPerf15MinIntRetrains,
       "adEShdslPerf15MinIntHandshakeFailures": adEShdslPerf15MinIntHandshakeFailures,
       "adEShdslPerf15MinIntMinSNRMargin": adEShdslPerf15MinIntMinSNRMargin,
       "adEShdslPerf15MinIntMaxSNRMargin": adEShdslPerf15MinIntMaxSNRMargin,
       "adEShdslPerf24HrIntTable": adEShdslPerf24HrIntTable,
       "adEShdslPerf24HrIntEntry": adEShdslPerf24HrIntEntry,
       "adEShdslPerf24HrIntNumber": adEShdslPerf24HrIntNumber,
       "adEShdslPerf24HrIntES": adEShdslPerf24HrIntES,
       "adEShdslPerf24HrIntSES": adEShdslPerf24HrIntSES,
       "adEShdslPerf24HrIntUAS": adEShdslPerf24HrIntUAS,
       "adEShdslPerf24HrIntCVC": adEShdslPerf24HrIntCVC,
       "adEShdslPerf24HrIntLOSWS": adEShdslPerf24HrIntLOSWS,
       "adEShdslPerf24HrIntOS": adEShdslPerf24HrIntOS,
       "adEShdslPerf24HrIntRetrains": adEShdslPerf24HrIntRetrains,
       "adEShdslPerf24HrIntHandshakeFailures": adEShdslPerf24HrIntHandshakeFailures,
       "adEShdslPerf24HrIntMinSNRMargin": adEShdslPerf24HrIntMinSNRMargin,
       "adEShdslPerf24HrIntMaxSNRMargin": adEShdslPerf24HrIntMaxSNRMargin,
       "adEShdslPerfPortResetTable": adEShdslPerfPortResetTable,
       "adEShdslPerfPortResetEntry": adEShdslPerfPortResetEntry,
       "adEShdslPerfPortReset": adEShdslPerfPortReset,
       "adEShdslSpliceDetection": adEShdslSpliceDetection,
       "adEShdslSpliceDetectionTable": adEShdslSpliceDetectionTable,
       "adEShdslSpliceDetectionEntry": adEShdslSpliceDetectionEntry,
       "adEShdslSpliceDetectionSummary": adEShdslSpliceDetectionSummary,
       "adEShdslSpliceCounts": adEShdslSpliceCounts,
       "adEShdslSpliceDistances": adEShdslSpliceDistances,
       "adEShdslSpliceRestart": adEShdslSpliceRestart,
       "adEShdslSpliceDistanceType": adEShdslSpliceDistanceType,
       "adEShdslSpliceRate": adEShdslSpliceRate,
       "adEShdslSpliceBadSpliceDetected": adEShdslSpliceBadSpliceDetected,
       "adEShdslSpliceDet24HrIntTable": adEShdslSpliceDet24HrIntTable,
       "adEShdslSpliceDet24HrIntEntry": adEShdslSpliceDet24HrIntEntry,
       "adEShdslSpliceDet24HrIntNumber": adEShdslSpliceDet24HrIntNumber,
       "adEShdslSplice24HrIntCounts": adEShdslSplice24HrIntCounts,
       "adEShdslSplice24HrIntDistances": adEShdslSplice24HrIntDistances,
       "adEShdslSplice24HrIntRate": adEShdslSplice24HrIntRate,
       "adEShdslSpliceDet15MinCurrTable": adEShdslSpliceDet15MinCurrTable,
       "adEShdslSpliceDet15MinCurrEntry": adEShdslSpliceDet15MinCurrEntry,
       "adEShdslSplice15MinCurrCounts": adEShdslSplice15MinCurrCounts,
       "adEShdslSplice15MinCurrDistances": adEShdslSplice15MinCurrDistances,
       "adEShdslSplice15MinCurrRate": adEShdslSplice15MinCurrRate,
       "adEShdslSpliceDet15MinIntTable": adEShdslSpliceDet15MinIntTable,
       "adEShdslSpliceDet15MinIntEntry": adEShdslSpliceDet15MinIntEntry,
       "adEShdslSpliceDet15MinIntNumber": adEShdslSpliceDet15MinIntNumber,
       "adEShdslSplice15MinIntCounts": adEShdslSplice15MinIntCounts,
       "adEShdslSplice15MinIntDistances": adEShdslSplice15MinIntDistances,
       "adEShdslSplice15MinIntRate": adEShdslSplice15MinIntRate,
       "adEShdslMibConformance": adEShdslMibConformance,
       "adEShdslMibGroups": adEShdslMibGroups,
       "adGenEShdslIndexGroup": adGenEShdslIndexGroup,
       "adGenEShdslInvGroup": adGenEShdslInvGroup,
       "adGenEShdslProvGroup": adGenEShdslProvGroup,
       "adGenEShdslStatusGroup": adGenEShdslStatusGroup,
       "adGenEShdslTestGroup": adGenEShdslTestGroup,
       "adGenEShdslCurr15MinPerfGroup": adGenEShdslCurr15MinPerfGroup,
       "adGenEShdslCurr24HrPerfGroup": adGenEShdslCurr24HrPerfGroup,
       "adGenEShdslPrior15MinPerfGroup": adGenEShdslPrior15MinPerfGroup,
       "adGenEShdslPrior24HrPerfGroup": adGenEShdslPrior24HrPerfGroup,
       "adGenEShdslInt15MinPerfGroup": adGenEShdslInt15MinPerfGroup,
       "adGenEShdslInt24HrPerfGroup": adGenEShdslInt24HrPerfGroup,
       "adGenEShdslSpliceGroup": adGenEShdslSpliceGroup,
       "adGenEShdslEventGroup": adGenEShdslEventGroup,
       "adGenEShdslInt24HrSpliceDetGroup": adGenEShdslInt24HrSpliceDetGroup,
       "adGenEShdslPerfResetGroup": adGenEShdslPerfResetGroup,
       "adEShdslAlarmsPrefix": adEShdslAlarmsPrefix,
       "adEShdslAlarms": adEShdslAlarms,
       "adEShdslLossofSignalAlmCLR": adEShdslLossofSignalAlmCLR,
       "adEShdslLossofSignalAlmACT": adEShdslLossofSignalAlmACT,
       "adEShdslLTULossofSyncWordAlmCLR": adEShdslLTULossofSyncWordAlmCLR,
       "adEShdslLTULossofSyncWordAlmACT": adEShdslLTULossofSyncWordAlmACT,
       "adEShdslLTUCRCErrorAlmCLR": adEShdslLTUCRCErrorAlmCLR,
       "adEShdslLTUCRCErrorAlmACT": adEShdslLTUCRCErrorAlmACT,
       "adEShdslLTUSNRMarginAlmCLR": adEShdslLTUSNRMarginAlmCLR,
       "adEShdslLTUSNRMarginAlmACT": adEShdslLTUSNRMarginAlmACT,
       "adEShdslLTULoopAttenAlmCLR": adEShdslLTULoopAttenAlmCLR,
       "adEShdslLTULoopAttenAlmACT": adEShdslLTULoopAttenAlmACT,
       "adEShdslNTULossofSyncWordAlmCLR": adEShdslNTULossofSyncWordAlmCLR,
       "adEShdslNTULossofSyncWordAlmACT": adEShdslNTULossofSyncWordAlmACT,
       "adEShdslNTUCRCErrorAlmCLR": adEShdslNTUCRCErrorAlmCLR,
       "adEShdslNTUCRCErrorAlmACT": adEShdslNTUCRCErrorAlmACT,
       "adEShdslNTUSNRMarginAlmCLR": adEShdslNTUSNRMarginAlmCLR,
       "adEShdslNTUSNRMarginAlmACT": adEShdslNTUSNRMarginAlmACT,
       "adEShdslNTULoopAttenAlmCLR": adEShdslNTULoopAttenAlmCLR,
       "adEShdslNTULoopAttenAlmACT": adEShdslNTULoopAttenAlmACT,
       "adEShdslLTUESThreshCrossed": adEShdslLTUESThreshCrossed,
       "adEShdslLTUSESThreshCrossed": adEShdslLTUSESThreshCrossed,
       "adEShdslLTUUASThreshCrossed": adEShdslLTUUASThreshCrossed,
       "adEShdslLTUCVCThreshCrossed": adEShdslLTUCVCThreshCrossed,
       "adEShdslLTULOSWSThreshCrossed": adEShdslLTULOSWSThreshCrossed,
       "adEShdslLTUOSThreshCrossed": adEShdslLTUOSThreshCrossed,
       "adEShdslNTUESThreshCrossed": adEShdslNTUESThreshCrossed,
       "adEShdslNTUSESThreshCrossed": adEShdslNTUSESThreshCrossed,
       "adEShdslNTUUASThreshCrossed": adEShdslNTUUASThreshCrossed,
       "adEShdslNTUCVCThreshCrossed": adEShdslNTUCVCThreshCrossed,
       "adEShdslNTULOSWSThreshCrossed": adEShdslNTULOSWSThreshCrossed,
       "adEShdslNTUOSThreshCrossed": adEShdslNTUOSThreshCrossed,
       "adEShdslRemoteLossOfPower": adEShdslRemoteLossOfPower,
       "adEShdslLTUES24HrThreshCrossed": adEShdslLTUES24HrThreshCrossed,
       "adEShdslLTUSES24HrThreshCrossed": adEShdslLTUSES24HrThreshCrossed,
       "adEShdslLTUUAS24HrThreshCrossed": adEShdslLTUUAS24HrThreshCrossed,
       "adEShdslLTUCVC24HrThreshCrossed": adEShdslLTUCVC24HrThreshCrossed,
       "adEShdslLTULOSWS24HrThreshCrossed": adEShdslLTULOSWS24HrThreshCrossed,
       "adEShdslLTUOS24HrThreshCrossed": adEShdslLTUOS24HrThreshCrossed,
       "adEShdslNTUES24HrThreshCrossed": adEShdslNTUES24HrThreshCrossed,
       "adEShdslNTUSES24HrThreshCrossed": adEShdslNTUSES24HrThreshCrossed,
       "adEShdslNTUUAS24HrThreshCrossed": adEShdslNTUUAS24HrThreshCrossed,
       "adEShdslNTUCVC24HrThreshCrossed": adEShdslNTUCVC24HrThreshCrossed,
       "adEShdslNTULOSWS24HrThreshCrossed": adEShdslNTULOSWS24HrThreshCrossed,
       "adEShdslNTUOS24HrThreshCrossed": adEShdslNTUOS24HrThreshCrossed,
       "adEShdslRegenLossofSignalAlmCLR": adEShdslRegenLossofSignalAlmCLR,
       "adEShdslRegenLossofSignalAlmACT": adEShdslRegenLossofSignalAlmACT,
       "adEShdslRegenLossofSyncWordAlmCLR": adEShdslRegenLossofSyncWordAlmCLR,
       "adEShdslRegenLossofSyncWordAlmACT": adEShdslRegenLossofSyncWordAlmACT,
       "adEShdslRegenCRCErrorAlmCLR": adEShdslRegenCRCErrorAlmCLR,
       "adEShdslRegenCRCErrorAlmACT": adEShdslRegenCRCErrorAlmACT,
       "adEShdslRegenSNRMarginAlmCLR": adEShdslRegenSNRMarginAlmCLR,
       "adEShdslRegenSNRMarginAlmACT": adEShdslRegenSNRMarginAlmACT,
       "adEShdslRegenLoopAttenAlmCLR": adEShdslRegenLoopAttenAlmCLR,
       "adEShdslRegenLoopAttenAlmACT": adEShdslRegenLoopAttenAlmACT,
       "adEShdslRegenESThreshCrossed": adEShdslRegenESThreshCrossed,
       "adEShdslRegenSESThreshCrossed": adEShdslRegenSESThreshCrossed,
       "adEShdslRegenUASThreshCrossed": adEShdslRegenUASThreshCrossed,
       "adEShdslRegenCVCThreshCrossed": adEShdslRegenCVCThreshCrossed,
       "adEShdslRegenLOSWSThreshCrossed": adEShdslRegenLOSWSThreshCrossed,
       "adEShdslRegenOSThreshCrossed": adEShdslRegenOSThreshCrossed,
       "adEShdslRegenES24HrThreshCrossed": adEShdslRegenES24HrThreshCrossed,
       "adEShdslRegenSES24HrThreshCrossed": adEShdslRegenSES24HrThreshCrossed,
       "adEShdslRegenUAS24HrThreshCrossed": adEShdslRegenUAS24HrThreshCrossed,
       "adEShdslRegenCVC24HrThreshCrossed": adEShdslRegenCVC24HrThreshCrossed,
       "adEShdslRegenLOSWS24HrThreshCrossed": adEShdslRegenLOSWS24HrThreshCrossed,
       "adEShdslRegenOS24HrThreshCrossed": adEShdslRegenOS24HrThreshCrossed,
       "adEShdslLoopbackEnabledCLR": adEShdslLoopbackEnabledCLR,
       "adEShdslLoopbackEnabledACT": adEShdslLoopbackEnabledACT,
       "adEShdslRetrains15MinThreshCrossed": adEShdslRetrains15MinThreshCrossed,
       "adEShdslHandshakeFailures15MinThreshCrossed": adEShdslHandshakeFailures15MinThreshCrossed,
       "adEShdslRetrains24HrThreshCrossed": adEShdslRetrains24HrThreshCrossed,
       "adEShdslHandshakeFailures24HrThreshCrossed": adEShdslHandshakeFailures24HrThreshCrossed,
       "adEShdslBadSpliceDetected": adEShdslBadSpliceDetected,
       "adEShdslSruShortDetectAlmCLR": adEShdslSruShortDetectAlmCLR,
       "adEShdslSruShortDetectAlmACT": adEShdslSruShortDetectAlmACT,
       "adEShdslSruGroundFaultDetectAlmCLR": adEShdslSruGroundFaultDetectAlmCLR,
       "adEShdslSruGroundFaultDetectAlmACT": adEShdslSruGroundFaultDetectAlmACT,
       "adEShdslSCIThreshCrossed": adEShdslSCIThreshCrossed,
       "adEShdslProductInfo": adEShdslProductInfo,
       "adGenEShdslMIB": adGenEShdslMIB}
)
