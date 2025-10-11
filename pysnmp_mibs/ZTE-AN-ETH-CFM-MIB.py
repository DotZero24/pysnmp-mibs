# SNMP MIB module (ZTE-AN-ETH-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ETH-CFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:54 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnEthCfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60)
)
if mibBuilder.loadTexts:
    zxAnEthCfmMIB.setRevisions(
        ("2007-01-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class VlanIdOrNone(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



class VlanId(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class Dot1agCfmMaintDomainNameType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("dnsLikeName", 2),
          ("macAddressAndUint", 3),
          ("charString", 4))
    )



class Dot1agCfmMaintDomainName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class Dot1agCfmMaintAssocNameType(TextualConvention, Integer32):
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
        *(("primaryVid", 1),
          ("charString", 2),
          ("unsignedInt16", 3),
          ("rfc2865VpnId", 4))
    )



class Dot1agCfmMaintAssocName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class Dot1agCfmMDLevel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Dot1agCfmMpDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )



class Dot1agCfmHighestDefectPri(TextualConvention, Integer32):
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
        *(("none", 0),
          ("defRDICCM", 1),
          ("defMACstatus", 2),
          ("defRemoteCCM", 3),
          ("defErrorCCM", 4),
          ("defXconCCM", 5))
    )



class Dot1agCfmLowestAlarmPri(TextualConvention, Integer32):
    status = "current"
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
        *(("allDef", 1),
          ("macRemErrXcon", 2),
          ("remErrXcon", 3),
          ("errXcon", 4),
          ("xcon", 5),
          ("noXcon", 6))
    )



class Dot1agCfmSessionId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class Dot1agCfmMhfCreation(TextualConvention, Integer32):
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
        *(("defMHFnone", 1),
          ("defMHFdefault", 2),
          ("defMHFexplicit", 3),
          ("defMHFdefer", 4))
    )



class Dot1agCfmIdPermission(TextualConvention, Integer32):
    status = "current"
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
        *(("sendIdNone", 1),
          ("sendIdChassis", 2),
          ("sendIdManage", 3),
          ("sendIdChassisManage", 4),
          ("sendIdDefer", 5))
    )



class Dot1agCfmSpeed(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fastSpeed", 0),
          ("slowSpeed", 1))
    )



class Dot1agCfmCcmInterval(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("intervalInvalid", 0),
          ("interval300Hz", 1),
          ("interval10ms", 2),
          ("interval100ms", 3),
          ("interval1s", 4),
          ("interval10s", 5),
          ("interval1min", 6),
          ("interval10min", 7))
    )



class Dot1agCfmFngState(TextualConvention, Integer32):
    status = "current"
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
        *(("fngReset", 1),
          ("fngDefect", 2),
          ("fngReportDefect", 3),
          ("fngDefectReported", 4),
          ("fngDefectClearing", 5))
    )



class Dot1agCfmRelayActionFieldValue(TextualConvention, Integer32):
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
        *(("rlyHit", 1),
          ("rlyFdb", 2),
          ("rlyMpdb", 3))
    )



class Dot1agCfmIngressActionFieldValue(TextualConvention, Integer32):
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
        *(("ingOk", 1),
          ("ingDown", 2),
          ("ingBlocked", 3),
          ("ingVid", 4))
    )



class Dot1agCfmEgressActionFieldValue(TextualConvention, Integer32):
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
        *(("egrOK", 1),
          ("egrDown", 2),
          ("egrBlocked", 3),
          ("egrVid", 4))
    )



class Dot1afCfmIndexIntegerNextFree(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class Dot1agCfmMepDefects(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bDefRDICCM", 0),
          ("bDefMACstatus", 1),
          ("bDefRemoteCCM", 2),
          ("bDefErrorCCM", 3),
          ("bDefXconCCM", 4))
    )


class Dot1agCfmLbrTransId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class Dot1agCfmProtectType(TextualConvention, Integer32):
    status = "current"
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
        *(("maProtectNothing", 1),
          ("cfmMaProtectVlan", 2),
          ("cfmMaProtectTunnel", 3),
          ("cfmMaProtectPort", 4),
          ("cfmMaProtectLink", 5))
    )



class Dot1agCfmTunnel(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class Dot1agCfmClientLevel(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_Dot1agNotifications_ObjectIdentity = ObjectIdentity
dot1agNotifications = _Dot1agNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 0)
)
_Dot1agMIBObjects_ObjectIdentity = ObjectIdentity
dot1agMIBObjects = _Dot1agMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1)
)
_Dot1agCfmMd_ObjectIdentity = ObjectIdentity
dot1agCfmMd = _Dot1agCfmMd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1)
)
_Dot1agCfmMdTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMdTableNextIndex_Object = MibScalar
dot1agCfmMdTableNextIndex = _Dot1agCfmMdTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 1),
    _Dot1agCfmMdTableNextIndex_Type()
)
dot1agCfmMdTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMdTableNextIndex.setStatus("current")
_Dot1agCfmMdTable_Object = MibTable
dot1agCfmMdTable = _Dot1agCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmMdTable.setStatus("current")
_Dot1agCfmMdEntry_Object = MibTableRow
dot1agCfmMdEntry = _Dot1agCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1)
)
dot1agCfmMdEntry.setIndexNames(
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmMdEntry.setStatus("current")


class _Dot1agCfmMdIndex_Type(Unsigned32):
    """Custom type dot1agCfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Dot1agCfmMdIndex_Type.__name__ = "Unsigned32"
_Dot1agCfmMdIndex_Object = MibTableColumn
dot1agCfmMdIndex = _Dot1agCfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 1),
    _Dot1agCfmMdIndex_Type()
)
dot1agCfmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMdIndex.setStatus("current")


class _Dot1agCfmMdFormat_Type(Dot1agCfmMaintDomainNameType):
    """Custom type dot1agCfmMdFormat based on Dot1agCfmMaintDomainNameType"""
    defaultValue = 4


_Dot1agCfmMdFormat_Type.__name__ = "Dot1agCfmMaintDomainNameType"
_Dot1agCfmMdFormat_Object = MibTableColumn
dot1agCfmMdFormat = _Dot1agCfmMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 2),
    _Dot1agCfmMdFormat_Type()
)
dot1agCfmMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdFormat.setStatus("current")


class _Dot1agCfmMdName_Type(Dot1agCfmMaintDomainName):
    """Custom type dot1agCfmMdName based on Dot1agCfmMaintDomainName"""
    defaultValue = OctetString("DEFAULT")


_Dot1agCfmMdName_Type.__name__ = "Dot1agCfmMaintDomainName"
_Dot1agCfmMdName_Object = MibTableColumn
dot1agCfmMdName = _Dot1agCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 3),
    _Dot1agCfmMdName_Type()
)
dot1agCfmMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdName.setStatus("current")


class _Dot1agCfmMdMdLevel_Type(Dot1agCfmMDLevel):
    """Custom type dot1agCfmMdMdLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_Dot1agCfmMdMdLevel_Type.__name__ = "Dot1agCfmMDLevel"
_Dot1agCfmMdMdLevel_Object = MibTableColumn
dot1agCfmMdMdLevel = _Dot1agCfmMdMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 4),
    _Dot1agCfmMdMdLevel_Type()
)
dot1agCfmMdMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdMdLevel.setStatus("current")


class _Dot1agCfmMdMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmMdMhfCreation based on Dot1agCfmMhfCreation"""
    defaultValue = 1


_Dot1agCfmMdMhfCreation_Type.__name__ = "Dot1agCfmMhfCreation"
_Dot1agCfmMdMhfCreation_Object = MibTableColumn
dot1agCfmMdMhfCreation = _Dot1agCfmMdMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 5),
    _Dot1agCfmMdMhfCreation_Type()
)
dot1agCfmMdMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdMhfCreation.setStatus("current")


class _Dot1agCfmMdMhfIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type dot1agCfmMdMhfIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 1


_Dot1agCfmMdMhfIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_Dot1agCfmMdMhfIdPermission_Object = MibTableColumn
dot1agCfmMdMhfIdPermission = _Dot1agCfmMdMhfIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 6),
    _Dot1agCfmMdMhfIdPermission_Type()
)
dot1agCfmMdMhfIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdMhfIdPermission.setStatus("current")
_Dot1agCfmMdMaTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_Dot1agCfmMdMaTableNextIndex_Object = MibTableColumn
dot1agCfmMdMaTableNextIndex = _Dot1agCfmMdMaTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 7),
    _Dot1agCfmMdMaTableNextIndex_Type()
)
dot1agCfmMdMaTableNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdMaTableNextIndex.setStatus("current")
_Dot1agCfmMdRowStatus_Type = RowStatus
_Dot1agCfmMdRowStatus_Object = MibTableColumn
dot1agCfmMdRowStatus = _Dot1agCfmMdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 8),
    _Dot1agCfmMdRowStatus_Type()
)
dot1agCfmMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMdRowStatus.setStatus("current")
_Dot1agCfmMa_ObjectIdentity = ObjectIdentity
dot1agCfmMa = _Dot1agCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2)
)
_Dot1agCfmMaTable_Object = MibTable
dot1agCfmMaTable = _Dot1agCfmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmMaTable.setStatus("current")
_Dot1agCfmMaEntry_Object = MibTableRow
dot1agCfmMaEntry = _Dot1agCfmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1)
)
dot1agCfmMaEntry.setIndexNames(
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaEntry.setStatus("current")


class _Dot1agCfmMaIndex_Type(Unsigned32):
    """Custom type dot1agCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Dot1agCfmMaIndex_Type.__name__ = "Unsigned32"
_Dot1agCfmMaIndex_Object = MibTableColumn
dot1agCfmMaIndex = _Dot1agCfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 1),
    _Dot1agCfmMaIndex_Type()
)
dot1agCfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaIndex.setStatus("current")
_Dot1agCfmMaPrimaryVlanId_Type = VlanIdOrNone
_Dot1agCfmMaPrimaryVlanId_Object = MibTableColumn
dot1agCfmMaPrimaryVlanId = _Dot1agCfmMaPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 2),
    _Dot1agCfmMaPrimaryVlanId_Type()
)
dot1agCfmMaPrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMaPrimaryVlanId.setStatus("current")
_Dot1agCfmMaFormat_Type = Dot1agCfmMaintAssocNameType
_Dot1agCfmMaFormat_Object = MibTableColumn
dot1agCfmMaFormat = _Dot1agCfmMaFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 3),
    _Dot1agCfmMaFormat_Type()
)
dot1agCfmMaFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaFormat.setStatus("current")
_Dot1agCfmMaName_Type = Dot1agCfmMaintAssocName
_Dot1agCfmMaName_Object = MibTableColumn
dot1agCfmMaName = _Dot1agCfmMaName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 4),
    _Dot1agCfmMaName_Type()
)
dot1agCfmMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaName.setStatus("current")


class _Dot1agCfmMaMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type dot1agCfmMaMhfCreation based on Dot1agCfmMhfCreation"""
    defaultValue = 4


_Dot1agCfmMaMhfCreation_Type.__name__ = "Dot1agCfmMhfCreation"
_Dot1agCfmMaMhfCreation_Object = MibTableColumn
dot1agCfmMaMhfCreation = _Dot1agCfmMaMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 5),
    _Dot1agCfmMaMhfCreation_Type()
)
dot1agCfmMaMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaMhfCreation.setStatus("current")


class _Dot1agCfmMaIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type dot1agCfmMaIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 5


_Dot1agCfmMaIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_Dot1agCfmMaIdPermission_Object = MibTableColumn
dot1agCfmMaIdPermission = _Dot1agCfmMaIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 6),
    _Dot1agCfmMaIdPermission_Type()
)
dot1agCfmMaIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaIdPermission.setStatus("current")


class _Dot1agCfmMaCcmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type dot1agCfmMaCcmInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 4


_Dot1agCfmMaCcmInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_Dot1agCfmMaCcmInterval_Object = MibTableColumn
dot1agCfmMaCcmInterval = _Dot1agCfmMaCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 7),
    _Dot1agCfmMaCcmInterval_Type()
)
dot1agCfmMaCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaCcmInterval.setStatus("current")
_Dot1agCfmMaRowStatus_Type = RowStatus
_Dot1agCfmMaRowStatus_Object = MibTableColumn
dot1agCfmMaRowStatus = _Dot1agCfmMaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 8),
    _Dot1agCfmMaRowStatus_Type()
)
dot1agCfmMaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaRowStatus.setStatus("current")
_Dot1agCfmMASpeed_Type = Dot1agCfmSpeed
_Dot1agCfmMASpeed_Object = MibTableColumn
dot1agCfmMASpeed = _Dot1agCfmMASpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 9),
    _Dot1agCfmMASpeed_Type()
)
dot1agCfmMASpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMASpeed.setStatus("current")
_Dot1agCfmMAProtect_Type = Dot1agCfmProtectType
_Dot1agCfmMAProtect_Object = MibTableColumn
dot1agCfmMAProtect = _Dot1agCfmMAProtect_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 10),
    _Dot1agCfmMAProtect_Type()
)
dot1agCfmMAProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMAProtect.setStatus("current")
_Dot1agCfmMATunnel_Type = Dot1agCfmTunnel
_Dot1agCfmMATunnel_Object = MibTableColumn
dot1agCfmMATunnel = _Dot1agCfmMATunnel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 11),
    _Dot1agCfmMATunnel_Type()
)
dot1agCfmMATunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMATunnel.setStatus("current")
_Dot1agCfmMaVlanListTable_Object = MibTable
dot1agCfmMaVlanListTable = _Dot1agCfmMaVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmMaVlanListTable.setStatus("current")
_Dot1agCfmMaVlanListEntry_Object = MibTableRow
dot1agCfmMaVlanListEntry = _Dot1agCfmMaVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 2, 1)
)
dot1agCfmMaVlanListEntry.setIndexNames(
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaVlanListIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaVlanListEntry.setStatus("current")
_Dot1agCfmMaVlanListIdentifier_Type = VlanId
_Dot1agCfmMaVlanListIdentifier_Object = MibTableColumn
dot1agCfmMaVlanListIdentifier = _Dot1agCfmMaVlanListIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 2, 1, 1),
    _Dot1agCfmMaVlanListIdentifier_Type()
)
dot1agCfmMaVlanListIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaVlanListIdentifier.setStatus("current")
_Dot1agCfmMaVlanListRowStatus_Type = RowStatus
_Dot1agCfmMaVlanListRowStatus_Object = MibTableColumn
dot1agCfmMaVlanListRowStatus = _Dot1agCfmMaVlanListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 2, 1, 2),
    _Dot1agCfmMaVlanListRowStatus_Type()
)
dot1agCfmMaVlanListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaVlanListRowStatus.setStatus("current")
_Dot1agCfmMaMepListTable_Object = MibTable
dot1agCfmMaMepListTable = _Dot1agCfmMaMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dot1agCfmMaMepListTable.setStatus("current")
_Dot1agCfmMaMepListEntry_Object = MibTableRow
dot1agCfmMaMepListEntry = _Dot1agCfmMaMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 3, 1)
)
dot1agCfmMaMepListEntry.setIndexNames(
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaMepListSessionId"),
)
if mibBuilder.loadTexts:
    dot1agCfmMaMepListEntry.setStatus("current")
_Dot1agCfmMaMepListSessionId_Type = Dot1agCfmSessionId
_Dot1agCfmMaMepListSessionId_Object = MibTableColumn
dot1agCfmMaMepListSessionId = _Dot1agCfmMaMepListSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 3, 1, 1),
    _Dot1agCfmMaMepListSessionId_Type()
)
dot1agCfmMaMepListSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMaMepListSessionId.setStatus("current")
_Dot1agCfmMaMepListRowStatus_Type = RowStatus
_Dot1agCfmMaMepListRowStatus_Object = MibTableColumn
dot1agCfmMaMepListRowStatus = _Dot1agCfmMaMepListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 3, 1, 2),
    _Dot1agCfmMaMepListRowStatus_Type()
)
dot1agCfmMaMepListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMaMepListRowStatus.setStatus("current")
_Dot1agCfmMep_ObjectIdentity = ObjectIdentity
dot1agCfmMep = _Dot1agCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3)
)
_Dot1agCfmMepTable_Object = MibTable
dot1agCfmMepTable = _Dot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmMepTable.setStatus("current")
_Dot1agCfmMepEntry_Object = MibTableRow
dot1agCfmMepEntry = _Dot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1)
)
dot1agCfmMepEntry.setIndexNames(
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmSessionId"),
)
if mibBuilder.loadTexts:
    dot1agCfmMepEntry.setStatus("current")
_Dot1agCfmSessionId_Type = Dot1agCfmSessionId
_Dot1agCfmSessionId_Object = MibTableColumn
dot1agCfmSessionId = _Dot1agCfmSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 1),
    _Dot1agCfmSessionId_Type()
)
dot1agCfmSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmSessionId.setStatus("current")
_Dot1agCfmMepIfIndex_Type = InterfaceIndexOrZero
_Dot1agCfmMepIfIndex_Object = MibTableColumn
dot1agCfmMepIfIndex = _Dot1agCfmMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 2),
    _Dot1agCfmMepIfIndex_Type()
)
dot1agCfmMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepIfIndex.setStatus("current")
_Dot1agCfmMepDirection_Type = Dot1agCfmMpDirection
_Dot1agCfmMepDirection_Object = MibTableColumn
dot1agCfmMepDirection = _Dot1agCfmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 3),
    _Dot1agCfmMepDirection_Type()
)
dot1agCfmMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepDirection.setStatus("current")


class _Dot1agCfmMepPrimaryVid_Type(Unsigned32):
    """Custom type dot1agCfmMepPrimaryVid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Dot1agCfmMepPrimaryVid_Type.__name__ = "Unsigned32"
_Dot1agCfmMepPrimaryVid_Object = MibTableColumn
dot1agCfmMepPrimaryVid = _Dot1agCfmMepPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 4),
    _Dot1agCfmMepPrimaryVid_Type()
)
dot1agCfmMepPrimaryVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepPrimaryVid.setStatus("current")


class _Dot1agCfmMepActive_Type(TruthValue):
    """Custom type dot1agCfmMepActive based on TruthValue"""
    defaultValue = 2


_Dot1agCfmMepActive_Type.__name__ = "TruthValue"
_Dot1agCfmMepActive_Object = MibTableColumn
dot1agCfmMepActive = _Dot1agCfmMepActive_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 5),
    _Dot1agCfmMepActive_Type()
)
dot1agCfmMepActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepActive.setStatus("current")


class _Dot1agCfmMepFngState_Type(Dot1agCfmFngState):
    """Custom type dot1agCfmMepFngState based on Dot1agCfmFngState"""
    defaultValue = 1


_Dot1agCfmMepFngState_Type.__name__ = "Dot1agCfmFngState"
_Dot1agCfmMepFngState_Object = MibTableColumn
dot1agCfmMepFngState = _Dot1agCfmMepFngState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 6),
    _Dot1agCfmMepFngState_Type()
)
dot1agCfmMepFngState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepFngState.setStatus("current")


class _Dot1agCfmMepCciEnabled_Type(TruthValue):
    """Custom type dot1agCfmMepCciEnabled based on TruthValue"""
    defaultValue = 2


_Dot1agCfmMepCciEnabled_Type.__name__ = "TruthValue"
_Dot1agCfmMepCciEnabled_Object = MibTableColumn
dot1agCfmMepCciEnabled = _Dot1agCfmMepCciEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 7),
    _Dot1agCfmMepCciEnabled_Type()
)
dot1agCfmMepCciEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepCciEnabled.setStatus("current")


class _Dot1agCfmMepCcmLtmPriority_Type(Unsigned32):
    """Custom type dot1agCfmMepCcmLtmPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1agCfmMepCcmLtmPriority_Type.__name__ = "Unsigned32"
_Dot1agCfmMepCcmLtmPriority_Object = MibTableColumn
dot1agCfmMepCcmLtmPriority = _Dot1agCfmMepCcmLtmPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 8),
    _Dot1agCfmMepCcmLtmPriority_Type()
)
dot1agCfmMepCcmLtmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepCcmLtmPriority.setStatus("current")
_Dot1agCfmMepMacAddress_Type = MacAddress
_Dot1agCfmMepMacAddress_Object = MibTableColumn
dot1agCfmMepMacAddress = _Dot1agCfmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 9),
    _Dot1agCfmMepMacAddress_Type()
)
dot1agCfmMepMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepMacAddress.setStatus("current")


class _Dot1agCfmMepLowPrDef_Type(Dot1agCfmLowestAlarmPri):
    """Custom type dot1agCfmMepLowPrDef based on Dot1agCfmLowestAlarmPri"""
    defaultValue = 2


_Dot1agCfmMepLowPrDef_Type.__name__ = "Dot1agCfmLowestAlarmPri"
_Dot1agCfmMepLowPrDef_Object = MibTableColumn
dot1agCfmMepLowPrDef = _Dot1agCfmMepLowPrDef_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 10),
    _Dot1agCfmMepLowPrDef_Type()
)
dot1agCfmMepLowPrDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepLowPrDef.setStatus("current")
_Dot1agCfmMepHighestPrDefect_Type = Dot1agCfmHighestDefectPri
_Dot1agCfmMepHighestPrDefect_Object = MibTableColumn
dot1agCfmMepHighestPrDefect = _Dot1agCfmMepHighestPrDefect_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 11),
    _Dot1agCfmMepHighestPrDefect_Type()
)
dot1agCfmMepHighestPrDefect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepHighestPrDefect.setStatus("current")
_Dot1agCfmMepDefects_Type = Dot1agCfmMepDefects
_Dot1agCfmMepDefects_Object = MibTableColumn
dot1agCfmMepDefects = _Dot1agCfmMepDefects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 12),
    _Dot1agCfmMepDefects_Type()
)
dot1agCfmMepDefects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepDefects.setStatus("current")
_Dot1agCfmMepCciSentCcms_Type = Counter32
_Dot1agCfmMepCciSentCcms_Object = MibTableColumn
dot1agCfmMepCciSentCcms = _Dot1agCfmMepCciSentCcms_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 13),
    _Dot1agCfmMepCciSentCcms_Type()
)
dot1agCfmMepCciSentCcms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepCciSentCcms.setStatus("current")
_Dot1agCfmMepId_Type = Unsigned32
_Dot1agCfmMepId_Object = MibTableColumn
dot1agCfmMepId = _Dot1agCfmMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 14),
    _Dot1agCfmMepId_Type()
)
dot1agCfmMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepId.setStatus("current")
_Dot1agCfmMepMEPAttachType_Type = Unsigned32
_Dot1agCfmMepMEPAttachType_Object = MibTableColumn
dot1agCfmMepMEPAttachType = _Dot1agCfmMepMEPAttachType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 15),
    _Dot1agCfmMepMEPAttachType_Type()
)
dot1agCfmMepMEPAttachType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepMEPAttachType.setStatus("current")
_Dot1agCfmMepTunnelId_Type = Unsigned32
_Dot1agCfmMepTunnelId_Object = MibTableColumn
dot1agCfmMepTunnelId = _Dot1agCfmMepTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 16),
    _Dot1agCfmMepTunnelId_Type()
)
dot1agCfmMepTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTunnelId.setStatus("current")


class _Dot1agCfmMepLMFlage_Type(TruthValue):
    """Custom type dot1agCfmMepLMFlage based on TruthValue"""
    defaultValue = 2


_Dot1agCfmMepLMFlage_Type.__name__ = "TruthValue"
_Dot1agCfmMepLMFlage_Object = MibTableColumn
dot1agCfmMepLMFlage = _Dot1agCfmMepLMFlage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 17),
    _Dot1agCfmMepLMFlage_Type()
)
dot1agCfmMepLMFlage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepLMFlage.setStatus("current")


class _Dot1agCfmMepDMFlage_Type(TruthValue):
    """Custom type dot1agCfmMepDMFlage based on TruthValue"""
    defaultValue = 2


_Dot1agCfmMepDMFlage_Type.__name__ = "TruthValue"
_Dot1agCfmMepDMFlage_Object = MibTableColumn
dot1agCfmMepDMFlage = _Dot1agCfmMepDMFlage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 18),
    _Dot1agCfmMepDMFlage_Type()
)
dot1agCfmMepDMFlage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepDMFlage.setStatus("current")
_Dot1agCfmMepPortName_Type = DisplayString
_Dot1agCfmMepPortName_Object = MibTableColumn
dot1agCfmMepPortName = _Dot1agCfmMepPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 19),
    _Dot1agCfmMepPortName_Type()
)
dot1agCfmMepPortName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepPortName.setStatus("current")
_Dot1agCfmMepLbrIn_Type = Counter32
_Dot1agCfmMepLbrIn_Object = MibTableColumn
dot1agCfmMepLbrIn = _Dot1agCfmMepLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 20),
    _Dot1agCfmMepLbrIn_Type()
)
dot1agCfmMepLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrIn.setStatus("current")
_Dot1agCfmMepLbrInOutOfOrder_Type = Counter32
_Dot1agCfmMepLbrInOutOfOrder_Object = MibTableColumn
dot1agCfmMepLbrInOutOfOrder = _Dot1agCfmMepLbrInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 21),
    _Dot1agCfmMepLbrInOutOfOrder_Type()
)
dot1agCfmMepLbrInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrInOutOfOrder.setStatus("current")
_Dot1agCfmMepLbrBadMsdu_Type = Counter32
_Dot1agCfmMepLbrBadMsdu_Object = MibTableColumn
dot1agCfmMepLbrBadMsdu = _Dot1agCfmMepLbrBadMsdu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 22),
    _Dot1agCfmMepLbrBadMsdu_Type()
)
dot1agCfmMepLbrBadMsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrBadMsdu.setStatus("current")
_Dot1agCfmMepLtmNextSeqNumber_Type = Unsigned32
_Dot1agCfmMepLtmNextSeqNumber_Object = MibTableColumn
dot1agCfmMepLtmNextSeqNumber = _Dot1agCfmMepLtmNextSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 23),
    _Dot1agCfmMepLtmNextSeqNumber_Type()
)
dot1agCfmMepLtmNextSeqNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepLtmNextSeqNumber.setStatus("current")
_Dot1agCfmMepUnexpLtrIn_Type = Counter32
_Dot1agCfmMepUnexpLtrIn_Object = MibTableColumn
dot1agCfmMepUnexpLtrIn = _Dot1agCfmMepUnexpLtrIn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 24),
    _Dot1agCfmMepUnexpLtrIn_Type()
)
dot1agCfmMepUnexpLtrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepUnexpLtrIn.setStatus("current")
_Dot1agCfmMepLbrOut_Type = Counter32
_Dot1agCfmMepLbrOut_Object = MibTableColumn
dot1agCfmMepLbrOut = _Dot1agCfmMepLbrOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 25),
    _Dot1agCfmMepLbrOut_Type()
)
dot1agCfmMepLbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepLbrOut.setStatus("current")
_Dot1agCfmMepRowStatus_Type = RowStatus
_Dot1agCfmMepRowStatus_Object = MibTableColumn
dot1agCfmMepRowStatus = _Dot1agCfmMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 26),
    _Dot1agCfmMepRowStatus_Type()
)
dot1agCfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepRowStatus.setStatus("current")
_Dot1agCfmMepCcCheckFlag_Type = TruthValue
_Dot1agCfmMepCcCheckFlag_Object = MibTableColumn
dot1agCfmMepCcCheckFlag = _Dot1agCfmMepCcCheckFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 27),
    _Dot1agCfmMepCcCheckFlag_Type()
)
dot1agCfmMepCcCheckFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepCcCheckFlag.setStatus("current")
_Dot1agCfmMepComplexFlag_Type = TruthValue
_Dot1agCfmMepComplexFlag_Object = MibTableColumn
dot1agCfmMepComplexFlag = _Dot1agCfmMepComplexFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 28),
    _Dot1agCfmMepComplexFlag_Type()
)
dot1agCfmMepComplexFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepComplexFlag.setStatus("current")
_Dot1agCfmMepclientLevel_Type = Dot1agCfmClientLevel
_Dot1agCfmMepclientLevel_Object = MibTableColumn
dot1agCfmMepclientLevel = _Dot1agCfmMepclientLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 29),
    _Dot1agCfmMepclientLevel_Type()
)
dot1agCfmMepclientLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepclientLevel.setStatus("current")
_Dot1agCfmMepAISSendFlag_Type = TruthValue
_Dot1agCfmMepAISSendFlag_Object = MibTableColumn
dot1agCfmMepAISSendFlag = _Dot1agCfmMepAISSendFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 30),
    _Dot1agCfmMepAISSendFlag_Type()
)
dot1agCfmMepAISSendFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepAISSendFlag.setStatus("current")
_Dot1agCfmMepAISEnableFlag_Type = TruthValue
_Dot1agCfmMepAISEnableFlag_Object = MibTableColumn
dot1agCfmMepAISEnableFlag = _Dot1agCfmMepAISEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 31),
    _Dot1agCfmMepAISEnableFlag_Type()
)
dot1agCfmMepAISEnableFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepAISEnableFlag.setStatus("current")
_Dot1agCfmMepLCKEnableFlag_Type = TruthValue
_Dot1agCfmMepLCKEnableFlag_Object = MibTableColumn
dot1agCfmMepLCKEnableFlag = _Dot1agCfmMepLCKEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 32),
    _Dot1agCfmMepLCKEnableFlag_Type()
)
dot1agCfmMepLCKEnableFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepLCKEnableFlag.setStatus("current")
_Dot1agCfmMepTxFCf_Type = Counter32
_Dot1agCfmMepTxFCf_Object = MibTableColumn
dot1agCfmMepTxFCf = _Dot1agCfmMepTxFCf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 33),
    _Dot1agCfmMepTxFCf_Type()
)
dot1agCfmMepTxFCf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTxFCf.setStatus("current")
_Dot1agCfmMepRxFCb_Type = Counter32
_Dot1agCfmMepRxFCb_Object = MibTableColumn
dot1agCfmMepRxFCb = _Dot1agCfmMepRxFCb_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 34),
    _Dot1agCfmMepRxFCb_Type()
)
dot1agCfmMepRxFCb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepRxFCb.setStatus("current")
_Dot1agCfmMepTxFCb_Type = Counter32
_Dot1agCfmMepTxFCb_Object = MibTableColumn
dot1agCfmMepTxFCb = _Dot1agCfmMepTxFCb_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 35),
    _Dot1agCfmMepTxFCb_Type()
)
dot1agCfmMepTxFCb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTxFCb.setStatus("current")
_Dot1agCfmMepRxFCl_Type = Counter32
_Dot1agCfmMepRxFCl_Object = MibTableColumn
dot1agCfmMepRxFCl = _Dot1agCfmMepRxFCl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 36),
    _Dot1agCfmMepRxFCl_Type()
)
dot1agCfmMepRxFCl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepRxFCl.setStatus("current")
_Dot1agCfmMepNearLost_Type = Counter32
_Dot1agCfmMepNearLost_Object = MibTableColumn
dot1agCfmMepNearLost = _Dot1agCfmMepNearLost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 37),
    _Dot1agCfmMepNearLost_Type()
)
dot1agCfmMepNearLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepNearLost.setStatus("current")
_Dot1agCfmMepFarLost_Type = Counter32
_Dot1agCfmMepFarLost_Object = MibTableColumn
dot1agCfmMepFarLost = _Dot1agCfmMepFarLost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 38),
    _Dot1agCfmMepFarLost_Type()
)
dot1agCfmMepFarLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepFarLost.setStatus("current")
_Dot1agCfmMepDaly_Type = Counter32
_Dot1agCfmMepDaly_Object = MibTableColumn
dot1agCfmMepDaly = _Dot1agCfmMepDaly_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 39),
    _Dot1agCfmMepDaly_Type()
)
dot1agCfmMepDaly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDaly.setStatus("current")
_Dot1agCfmMepDalyAve_Type = Counter32
_Dot1agCfmMepDalyAve_Object = MibTableColumn
dot1agCfmMepDalyAve = _Dot1agCfmMepDalyAve_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 40),
    _Dot1agCfmMepDalyAve_Type()
)
dot1agCfmMepDalyAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDalyAve.setStatus("current")
_Dot1agCfmMepDalyChg_Type = Counter32
_Dot1agCfmMepDalyChg_Object = MibTableColumn
dot1agCfmMepDalyChg = _Dot1agCfmMepDalyChg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 41),
    _Dot1agCfmMepDalyChg_Type()
)
dot1agCfmMepDalyChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDalyChg.setStatus("current")
_Dot1agCfmMepDalyChgAve_Type = Counter32
_Dot1agCfmMepDalyChgAve_Object = MibTableColumn
dot1agCfmMepDalyChgAve = _Dot1agCfmMepDalyChgAve_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 42),
    _Dot1agCfmMepDalyChgAve_Type()
)
dot1agCfmMepDalyChgAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepDalyChgAve.setStatus("current")


class _Dot1agCfmMepTransmitLbmStatus_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLbmStatus based on TruthValue"""
    defaultValue = 1


_Dot1agCfmMepTransmitLbmStatus_Type.__name__ = "TruthValue"
_Dot1agCfmMepTransmitLbmStatus_Object = MibTableColumn
dot1agCfmMepTransmitLbmStatus = _Dot1agCfmMepTransmitLbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 43),
    _Dot1agCfmMepTransmitLbmStatus_Type()
)
dot1agCfmMepTransmitLbmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmStatus.setStatus("current")
_Dot1agCfmMepTransmitLbmDestMacAddress_Type = MacAddress
_Dot1agCfmMepTransmitLbmDestMacAddress_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestMacAddress = _Dot1agCfmMepTransmitLbmDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 44),
    _Dot1agCfmMepTransmitLbmDestMacAddress_Type()
)
dot1agCfmMepTransmitLbmDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestMacAddress.setStatus("current")
_Dot1agCfmMepTransmitLbmDestSessionId_Type = Unsigned32
_Dot1agCfmMepTransmitLbmDestSessionId_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestSessionId = _Dot1agCfmMepTransmitLbmDestSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 45),
    _Dot1agCfmMepTransmitLbmDestSessionId_Type()
)
dot1agCfmMepTransmitLbmDestSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestSessionId.setStatus("current")
_Dot1agCfmMepTransmitLbmDestIsSessionId_Type = TruthValue
_Dot1agCfmMepTransmitLbmDestIsSessionId_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestIsSessionId = _Dot1agCfmMepTransmitLbmDestIsSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 46),
    _Dot1agCfmMepTransmitLbmDestIsSessionId_Type()
)
dot1agCfmMepTransmitLbmDestIsSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestIsSessionId.setStatus("current")
_Dot1agCfmMepTransmitLbmDestMepId_Type = Unsigned32
_Dot1agCfmMepTransmitLbmDestMepId_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestMepId = _Dot1agCfmMepTransmitLbmDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 47),
    _Dot1agCfmMepTransmitLbmDestMepId_Type()
)
dot1agCfmMepTransmitLbmDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestMepId.setStatus("current")
_Dot1agCfmMepTransmitLbmDestIsMepId_Type = TruthValue
_Dot1agCfmMepTransmitLbmDestIsMepId_Object = MibTableColumn
dot1agCfmMepTransmitLbmDestIsMepId = _Dot1agCfmMepTransmitLbmDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 48),
    _Dot1agCfmMepTransmitLbmDestIsMepId_Type()
)
dot1agCfmMepTransmitLbmDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDestIsMepId.setStatus("current")


class _Dot1agCfmMepTransmitLbmMessages_Type(Integer32):
    """Custom type dot1agCfmMepTransmitLbmMessages based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Dot1agCfmMepTransmitLbmMessages_Type.__name__ = "Integer32"
_Dot1agCfmMepTransmitLbmMessages_Object = MibTableColumn
dot1agCfmMepTransmitLbmMessages = _Dot1agCfmMepTransmitLbmMessages_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 49),
    _Dot1agCfmMepTransmitLbmMessages_Type()
)
dot1agCfmMepTransmitLbmMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmMessages.setStatus("current")


class _Dot1agCfmMepTransmitLbmDataTlv_Type(OctetString):
    """Custom type dot1agCfmMepTransmitLbmDataTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_Dot1agCfmMepTransmitLbmDataTlv_Type.__name__ = "OctetString"
_Dot1agCfmMepTransmitLbmDataTlv_Object = MibTableColumn
dot1agCfmMepTransmitLbmDataTlv = _Dot1agCfmMepTransmitLbmDataTlv_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 50),
    _Dot1agCfmMepTransmitLbmDataTlv_Type()
)
dot1agCfmMepTransmitLbmDataTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmDataTlv.setStatus("current")


class _Dot1agCfmMepTransmitLbmVlanPriority_Type(Integer32):
    """Custom type dot1agCfmMepTransmitLbmVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1agCfmMepTransmitLbmVlanPriority_Type.__name__ = "Integer32"
_Dot1agCfmMepTransmitLbmVlanPriority_Object = MibTableColumn
dot1agCfmMepTransmitLbmVlanPriority = _Dot1agCfmMepTransmitLbmVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 51),
    _Dot1agCfmMepTransmitLbmVlanPriority_Type()
)
dot1agCfmMepTransmitLbmVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmVlanPriority.setStatus("current")


class _Dot1agCfmMepTransmitLbmVlanDropEnable_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLbmVlanDropEnable based on TruthValue"""
    defaultValue = 1


_Dot1agCfmMepTransmitLbmVlanDropEnable_Type.__name__ = "TruthValue"
_Dot1agCfmMepTransmitLbmVlanDropEnable_Object = MibTableColumn
dot1agCfmMepTransmitLbmVlanDropEnable = _Dot1agCfmMepTransmitLbmVlanDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 52),
    _Dot1agCfmMepTransmitLbmVlanDropEnable_Type()
)
dot1agCfmMepTransmitLbmVlanDropEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmVlanDropEnable.setStatus("current")


class _Dot1agCfmMepTransmitLbmResultOK_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLbmResultOK based on TruthValue"""
    defaultValue = 1


_Dot1agCfmMepTransmitLbmResultOK_Type.__name__ = "TruthValue"
_Dot1agCfmMepTransmitLbmResultOK_Object = MibTableColumn
dot1agCfmMepTransmitLbmResultOK = _Dot1agCfmMepTransmitLbmResultOK_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 53),
    _Dot1agCfmMepTransmitLbmResultOK_Type()
)
dot1agCfmMepTransmitLbmResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmResultOK.setStatus("current")
_Dot1agCfmMepTransmitLbmSeqNumber_Type = Unsigned32
_Dot1agCfmMepTransmitLbmSeqNumber_Object = MibTableColumn
dot1agCfmMepTransmitLbmSeqNumber = _Dot1agCfmMepTransmitLbmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 54),
    _Dot1agCfmMepTransmitLbmSeqNumber_Type()
)
dot1agCfmMepTransmitLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmSeqNumber.setStatus("current")


class _Dot1agCfmMepTransmitLtmStatus_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLtmStatus based on TruthValue"""
    defaultValue = 1


_Dot1agCfmMepTransmitLtmStatus_Type.__name__ = "TruthValue"
_Dot1agCfmMepTransmitLtmStatus_Object = MibTableColumn
dot1agCfmMepTransmitLtmStatus = _Dot1agCfmMepTransmitLtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 55),
    _Dot1agCfmMepTransmitLtmStatus_Type()
)
dot1agCfmMepTransmitLtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmStatus.setStatus("current")


class _Dot1agCfmMepTransmitLtmFlags_Type(Bits):
    """Custom type dot1agCfmMepTransmitLtmFlags based on Bits"""
    namedValues = NamedValues(
        ("useFDBonly", 0)
    )

_Dot1agCfmMepTransmitLtmFlags_Type.__name__ = "Bits"
_Dot1agCfmMepTransmitLtmFlags_Object = MibTableColumn
dot1agCfmMepTransmitLtmFlags = _Dot1agCfmMepTransmitLtmFlags_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 56),
    _Dot1agCfmMepTransmitLtmFlags_Type()
)
dot1agCfmMepTransmitLtmFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmFlags.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetMacAddress_Type = MacAddress
_Dot1agCfmMepTransmitLtmTargetMacAddress_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetMacAddress = _Dot1agCfmMepTransmitLtmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 57),
    _Dot1agCfmMepTransmitLtmTargetMacAddress_Type()
)
dot1agCfmMepTransmitLtmTargetMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetMacAddress.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetSessionId_Type = Unsigned32
_Dot1agCfmMepTransmitLtmTargetSessionId_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetSessionId = _Dot1agCfmMepTransmitLtmTargetSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 58),
    _Dot1agCfmMepTransmitLtmTargetSessionId_Type()
)
dot1agCfmMepTransmitLtmTargetSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetSessionId.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetIsSessionId_Type = TruthValue
_Dot1agCfmMepTransmitLtmTargetIsSessionId_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetIsSessionId = _Dot1agCfmMepTransmitLtmTargetIsSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 59),
    _Dot1agCfmMepTransmitLtmTargetIsSessionId_Type()
)
dot1agCfmMepTransmitLtmTargetIsSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetIsSessionId.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetMepId_Type = Unsigned32
_Dot1agCfmMepTransmitLtmTargetMepId_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetMepId = _Dot1agCfmMepTransmitLtmTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 60),
    _Dot1agCfmMepTransmitLtmTargetMepId_Type()
)
dot1agCfmMepTransmitLtmTargetMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetMepId.setStatus("current")
_Dot1agCfmMepTransmitLtmTargetIsMepId_Type = TruthValue
_Dot1agCfmMepTransmitLtmTargetIsMepId_Object = MibTableColumn
dot1agCfmMepTransmitLtmTargetIsMepId = _Dot1agCfmMepTransmitLtmTargetIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 61),
    _Dot1agCfmMepTransmitLtmTargetIsMepId_Type()
)
dot1agCfmMepTransmitLtmTargetIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTargetIsMepId.setStatus("current")


class _Dot1agCfmMepTransmitLtmTtl_Type(Unsigned32):
    """Custom type dot1agCfmMepTransmitLtmTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1agCfmMepTransmitLtmTtl_Type.__name__ = "Unsigned32"
_Dot1agCfmMepTransmitLtmTtl_Object = MibTableColumn
dot1agCfmMepTransmitLtmTtl = _Dot1agCfmMepTransmitLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 62),
    _Dot1agCfmMepTransmitLtmTtl_Type()
)
dot1agCfmMepTransmitLtmTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmTtl.setStatus("current")


class _Dot1agCfmMepTransmitLtmResult_Type(TruthValue):
    """Custom type dot1agCfmMepTransmitLtmResult based on TruthValue"""
    defaultValue = 1


_Dot1agCfmMepTransmitLtmResult_Type.__name__ = "TruthValue"
_Dot1agCfmMepTransmitLtmResult_Object = MibTableColumn
dot1agCfmMepTransmitLtmResult = _Dot1agCfmMepTransmitLtmResult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 63),
    _Dot1agCfmMepTransmitLtmResult_Type()
)
dot1agCfmMepTransmitLtmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmResult.setStatus("current")
_Dot1agCfmMepTransmitLtmSeqNumber_Type = Unsigned32
_Dot1agCfmMepTransmitLtmSeqNumber_Object = MibTableColumn
dot1agCfmMepTransmitLtmSeqNumber = _Dot1agCfmMepTransmitLtmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 64),
    _Dot1agCfmMepTransmitLtmSeqNumber_Type()
)
dot1agCfmMepTransmitLtmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmSeqNumber.setStatus("current")


class _Dot1agCfmMepTransmitLtmEgressIdentifier_Type(OctetString):
    """Custom type dot1agCfmMepTransmitLtmEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Dot1agCfmMepTransmitLtmEgressIdentifier_Type.__name__ = "OctetString"
_Dot1agCfmMepTransmitLtmEgressIdentifier_Object = MibTableColumn
dot1agCfmMepTransmitLtmEgressIdentifier = _Dot1agCfmMepTransmitLtmEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 65),
    _Dot1agCfmMepTransmitLtmEgressIdentifier_Type()
)
dot1agCfmMepTransmitLtmEgressIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmEgressIdentifier.setStatus("current")
_Dot1agCfmLtrTable_Object = MibTable
dot1agCfmLtrTable = _Dot1agCfmLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dot1agCfmLtrTable.setStatus("current")
_Dot1agCfmLtrEntry_Object = MibTableRow
dot1agCfmLtrEntry = _Dot1agCfmLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1)
)
dot1agCfmLtrEntry.setIndexNames(
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmSessionId"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmLtrSeqNumber"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmLtrReceiveOrder"),
)
if mibBuilder.loadTexts:
    dot1agCfmLtrEntry.setStatus("current")


class _Dot1agCfmLtrSeqNumber_Type(Unsigned32):
    """Custom type dot1agCfmLtrSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dot1agCfmLtrSeqNumber_Type.__name__ = "Unsigned32"
_Dot1agCfmLtrSeqNumber_Object = MibTableColumn
dot1agCfmLtrSeqNumber = _Dot1agCfmLtrSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 1),
    _Dot1agCfmLtrSeqNumber_Type()
)
dot1agCfmLtrSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmLtrSeqNumber.setStatus("current")


class _Dot1agCfmLtrReceiveOrder_Type(Unsigned32):
    """Custom type dot1agCfmLtrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot1agCfmLtrReceiveOrder_Type.__name__ = "Unsigned32"
_Dot1agCfmLtrReceiveOrder_Object = MibTableColumn
dot1agCfmLtrReceiveOrder = _Dot1agCfmLtrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 2),
    _Dot1agCfmLtrReceiveOrder_Type()
)
dot1agCfmLtrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmLtrReceiveOrder.setStatus("current")


class _Dot1agCfmLtrTtl_Type(Unsigned32):
    """Custom type dot1agCfmLtrTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1agCfmLtrTtl_Type.__name__ = "Unsigned32"
_Dot1agCfmLtrTtl_Object = MibTableColumn
dot1agCfmLtrTtl = _Dot1agCfmLtrTtl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 3),
    _Dot1agCfmLtrTtl_Type()
)
dot1agCfmLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrTtl.setStatus("current")
_Dot1agCfmLtrForwarded_Type = TruthValue
_Dot1agCfmLtrForwarded_Object = MibTableColumn
dot1agCfmLtrForwarded = _Dot1agCfmLtrForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 4),
    _Dot1agCfmLtrForwarded_Type()
)
dot1agCfmLtrForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrForwarded.setStatus("current")
_Dot1agCfmLtrTerminalMep_Type = TruthValue
_Dot1agCfmLtrTerminalMep_Object = MibTableColumn
dot1agCfmLtrTerminalMep = _Dot1agCfmLtrTerminalMep_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 5),
    _Dot1agCfmLtrTerminalMep_Type()
)
dot1agCfmLtrTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrTerminalMep.setStatus("current")


class _Dot1agCfmLtrLastEgressIdentifier_Type(OctetString):
    """Custom type dot1agCfmLtrLastEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Dot1agCfmLtrLastEgressIdentifier_Type.__name__ = "OctetString"
_Dot1agCfmLtrLastEgressIdentifier_Object = MibTableColumn
dot1agCfmLtrLastEgressIdentifier = _Dot1agCfmLtrLastEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 6),
    _Dot1agCfmLtrLastEgressIdentifier_Type()
)
dot1agCfmLtrLastEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrLastEgressIdentifier.setStatus("current")


class _Dot1agCfmLtrNextEgressIdentifier_Type(OctetString):
    """Custom type dot1agCfmLtrNextEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Dot1agCfmLtrNextEgressIdentifier_Type.__name__ = "OctetString"
_Dot1agCfmLtrNextEgressIdentifier_Object = MibTableColumn
dot1agCfmLtrNextEgressIdentifier = _Dot1agCfmLtrNextEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 7),
    _Dot1agCfmLtrNextEgressIdentifier_Type()
)
dot1agCfmLtrNextEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrNextEgressIdentifier.setStatus("current")
_Dot1agCfmLtrRelay_Type = Dot1agCfmRelayActionFieldValue
_Dot1agCfmLtrRelay_Object = MibTableColumn
dot1agCfmLtrRelay = _Dot1agCfmLtrRelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 8),
    _Dot1agCfmLtrRelay_Type()
)
dot1agCfmLtrRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrRelay.setStatus("current")
_Dot1agCfmLtrIngress_Type = Dot1agCfmIngressActionFieldValue
_Dot1agCfmLtrIngress_Object = MibTableColumn
dot1agCfmLtrIngress = _Dot1agCfmLtrIngress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 9),
    _Dot1agCfmLtrIngress_Type()
)
dot1agCfmLtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngress.setStatus("current")
_Dot1agCfmLtrIngressMac_Type = MacAddress
_Dot1agCfmLtrIngressMac_Object = MibTableColumn
dot1agCfmLtrIngressMac = _Dot1agCfmLtrIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 10),
    _Dot1agCfmLtrIngressMac_Type()
)
dot1agCfmLtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrIngressMac.setStatus("current")
_Dot1agCfmLtrEgress_Type = Dot1agCfmEgressActionFieldValue
_Dot1agCfmLtrEgress_Object = MibTableColumn
dot1agCfmLtrEgress = _Dot1agCfmLtrEgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 11),
    _Dot1agCfmLtrEgress_Type()
)
dot1agCfmLtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgress.setStatus("current")
_Dot1agCfmLtrEgressMac_Type = MacAddress
_Dot1agCfmLtrEgressMac_Object = MibTableColumn
dot1agCfmLtrEgressMac = _Dot1agCfmLtrEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 12),
    _Dot1agCfmLtrEgressMac_Type()
)
dot1agCfmLtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLtrEgressMac.setStatus("current")
_Dot1agCfmMepDbTable_Object = MibTable
dot1agCfmMepDbTable = _Dot1agCfmMepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbTable.setStatus("current")
_Dot1agCfmMepDbEntry_Object = MibTableRow
dot1agCfmMepDbEntry = _Dot1agCfmMepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1)
)
dot1agCfmMepDbEntry.setIndexNames(
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMepDbRSessionId"),
)
if mibBuilder.loadTexts:
    dot1agCfmMepDbEntry.setStatus("current")
_Dot1agCfmMepDbRSessionId_Type = Dot1agCfmSessionId
_Dot1agCfmMepDbRSessionId_Object = MibTableColumn
dot1agCfmMepDbRSessionId = _Dot1agCfmMepDbRSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 1),
    _Dot1agCfmMepDbRSessionId_Type()
)
dot1agCfmMepDbRSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRSessionId.setStatus("current")
_Dot1agCfmMepDbMacAddress_Type = MacAddress
_Dot1agCfmMepDbMacAddress_Object = MibTableColumn
dot1agCfmMepDbMacAddress = _Dot1agCfmMepDbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 2),
    _Dot1agCfmMepDbMacAddress_Type()
)
dot1agCfmMepDbMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepDbMacAddress.setStatus("current")
_Dot1agCfmMepDbRdi_Type = TruthValue
_Dot1agCfmMepDbRdi_Object = MibTableColumn
dot1agCfmMepDbRdi = _Dot1agCfmMepDbRdi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 3),
    _Dot1agCfmMepDbRdi_Type()
)
dot1agCfmMepDbRdi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRdi.setStatus("current")
_Dot1agCfmMepDbId_Type = Unsigned32
_Dot1agCfmMepDbId_Object = MibTableColumn
dot1agCfmMepDbId = _Dot1agCfmMepDbId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 4),
    _Dot1agCfmMepDbId_Type()
)
dot1agCfmMepDbId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepDbId.setStatus("current")
_Dot1agCfmMepDbRowStatus_Type = RowStatus
_Dot1agCfmMepDbRowStatus_Object = MibTableColumn
dot1agCfmMepDbRowStatus = _Dot1agCfmMepDbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 5),
    _Dot1agCfmMepDbRowStatus_Type()
)
dot1agCfmMepDbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepDbRowStatus.setStatus("current")
_Dot1agCfmLbrInfo_ObjectIdentity = ObjectIdentity
dot1agCfmLbrInfo = _Dot1agCfmLbrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 4)
)
_Dot1agCfmLbrTransId_Type = Dot1agCfmLbrTransId
_Dot1agCfmLbrTransId_Object = MibScalar
dot1agCfmLbrTransId = _Dot1agCfmLbrTransId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 4, 1),
    _Dot1agCfmLbrTransId_Type()
)
dot1agCfmLbrTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLbrTransId.setStatus("current")
_Dot1agCfmLbrPrintInfo_Type = DisplayString
_Dot1agCfmLbrPrintInfo_Object = MibScalar
dot1agCfmLbrPrintInfo = _Dot1agCfmLbrPrintInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 4, 2),
    _Dot1agCfmLbrPrintInfo_Type()
)
dot1agCfmLbrPrintInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agCfmLbrPrintInfo.setStatus("current")
_Dot1agCfmMipTable_Object = MibTable
dot1agCfmMipTable = _Dot1agCfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dot1agCfmMipTable.setStatus("current")
_Dot1agCfmMipEntry_Object = MibTableRow
dot1agCfmMipEntry = _Dot1agCfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5, 1)
)
dot1agCfmMipEntry.setIndexNames(
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMipSessionId"),
)
if mibBuilder.loadTexts:
    dot1agCfmMipEntry.setStatus("current")
_Dot1agCfmMipSessionId_Type = Unsigned32
_Dot1agCfmMipSessionId_Object = MibTableColumn
dot1agCfmMipSessionId = _Dot1agCfmMipSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5, 1, 1),
    _Dot1agCfmMipSessionId_Type()
)
dot1agCfmMipSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMipSessionId.setStatus("current")
_Dot1agCfmMipName_Type = DisplayString
_Dot1agCfmMipName_Object = MibTableColumn
dot1agCfmMipName = _Dot1agCfmMipName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5, 1, 2),
    _Dot1agCfmMipName_Type()
)
dot1agCfmMipName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmMipName.setStatus("current")
_Dot1agCfmMipPortName_Type = DisplayString
_Dot1agCfmMipPortName_Object = MibTableColumn
dot1agCfmMipPortName = _Dot1agCfmMipPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5, 1, 3),
    _Dot1agCfmMipPortName_Type()
)
dot1agCfmMipPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmMipPortName.setStatus("current")
_Dot1agCfmGloPara_ObjectIdentity = ObjectIdentity
dot1agCfmGloPara = _Dot1agCfmGloPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 4)
)
_Dot1agCfmGlobalIsEnable_Type = TruthValue
_Dot1agCfmGlobalIsEnable_Object = MibScalar
dot1agCfmGlobalIsEnable = _Dot1agCfmGlobalIsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 4, 4),
    _Dot1agCfmGlobalIsEnable_Type()
)
dot1agCfmGlobalIsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agCfmGlobalIsEnable.setStatus("current")

# Managed Objects groups


# Notification objects

dot1agCfmFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 60, 0, 1)
)
dot1agCfmFaultAlarm.setObjects(
    ("ZTE-AN-ETH-CFM-MIB", "dot1agCfmMepHighestPrDefect")
)
if mibBuilder.loadTexts:
    dot1agCfmFaultAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ETH-CFM-MIB",
    **{"InterfaceIndexOrZero": InterfaceIndexOrZero,
       "VlanIdOrNone": VlanIdOrNone,
       "VlanId": VlanId,
       "Dot1agCfmMaintDomainNameType": Dot1agCfmMaintDomainNameType,
       "Dot1agCfmMaintDomainName": Dot1agCfmMaintDomainName,
       "Dot1agCfmMaintAssocNameType": Dot1agCfmMaintAssocNameType,
       "Dot1agCfmMaintAssocName": Dot1agCfmMaintAssocName,
       "Dot1agCfmMDLevel": Dot1agCfmMDLevel,
       "Dot1agCfmMpDirection": Dot1agCfmMpDirection,
       "Dot1agCfmHighestDefectPri": Dot1agCfmHighestDefectPri,
       "Dot1agCfmLowestAlarmPri": Dot1agCfmLowestAlarmPri,
       "Dot1agCfmSessionId": Dot1agCfmSessionId,
       "Dot1agCfmMhfCreation": Dot1agCfmMhfCreation,
       "Dot1agCfmIdPermission": Dot1agCfmIdPermission,
       "Dot1agCfmSpeed": Dot1agCfmSpeed,
       "Dot1agCfmCcmInterval": Dot1agCfmCcmInterval,
       "Dot1agCfmFngState": Dot1agCfmFngState,
       "Dot1agCfmRelayActionFieldValue": Dot1agCfmRelayActionFieldValue,
       "Dot1agCfmIngressActionFieldValue": Dot1agCfmIngressActionFieldValue,
       "Dot1agCfmEgressActionFieldValue": Dot1agCfmEgressActionFieldValue,
       "Dot1afCfmIndexIntegerNextFree": Dot1afCfmIndexIntegerNextFree,
       "Dot1agCfmMepDefects": Dot1agCfmMepDefects,
       "Dot1agCfmLbrTransId": Dot1agCfmLbrTransId,
       "Dot1agCfmProtectType": Dot1agCfmProtectType,
       "Dot1agCfmTunnel": Dot1agCfmTunnel,
       "Dot1agCfmClientLevel": Dot1agCfmClientLevel,
       "zxAnEthCfmMIB": zxAnEthCfmMIB,
       "dot1agNotifications": dot1agNotifications,
       "dot1agCfmFaultAlarm": dot1agCfmFaultAlarm,
       "dot1agMIBObjects": dot1agMIBObjects,
       "dot1agCfmMd": dot1agCfmMd,
       "dot1agCfmMdTableNextIndex": dot1agCfmMdTableNextIndex,
       "dot1agCfmMdTable": dot1agCfmMdTable,
       "dot1agCfmMdEntry": dot1agCfmMdEntry,
       "dot1agCfmMdIndex": dot1agCfmMdIndex,
       "dot1agCfmMdFormat": dot1agCfmMdFormat,
       "dot1agCfmMdName": dot1agCfmMdName,
       "dot1agCfmMdMdLevel": dot1agCfmMdMdLevel,
       "dot1agCfmMdMhfCreation": dot1agCfmMdMhfCreation,
       "dot1agCfmMdMhfIdPermission": dot1agCfmMdMhfIdPermission,
       "dot1agCfmMdMaTableNextIndex": dot1agCfmMdMaTableNextIndex,
       "dot1agCfmMdRowStatus": dot1agCfmMdRowStatus,
       "dot1agCfmMa": dot1agCfmMa,
       "dot1agCfmMaTable": dot1agCfmMaTable,
       "dot1agCfmMaEntry": dot1agCfmMaEntry,
       "dot1agCfmMaIndex": dot1agCfmMaIndex,
       "dot1agCfmMaPrimaryVlanId": dot1agCfmMaPrimaryVlanId,
       "dot1agCfmMaFormat": dot1agCfmMaFormat,
       "dot1agCfmMaName": dot1agCfmMaName,
       "dot1agCfmMaMhfCreation": dot1agCfmMaMhfCreation,
       "dot1agCfmMaIdPermission": dot1agCfmMaIdPermission,
       "dot1agCfmMaCcmInterval": dot1agCfmMaCcmInterval,
       "dot1agCfmMaRowStatus": dot1agCfmMaRowStatus,
       "dot1agCfmMASpeed": dot1agCfmMASpeed,
       "dot1agCfmMAProtect": dot1agCfmMAProtect,
       "dot1agCfmMATunnel": dot1agCfmMATunnel,
       "dot1agCfmMaVlanListTable": dot1agCfmMaVlanListTable,
       "dot1agCfmMaVlanListEntry": dot1agCfmMaVlanListEntry,
       "dot1agCfmMaVlanListIdentifier": dot1agCfmMaVlanListIdentifier,
       "dot1agCfmMaVlanListRowStatus": dot1agCfmMaVlanListRowStatus,
       "dot1agCfmMaMepListTable": dot1agCfmMaMepListTable,
       "dot1agCfmMaMepListEntry": dot1agCfmMaMepListEntry,
       "dot1agCfmMaMepListSessionId": dot1agCfmMaMepListSessionId,
       "dot1agCfmMaMepListRowStatus": dot1agCfmMaMepListRowStatus,
       "dot1agCfmMep": dot1agCfmMep,
       "dot1agCfmMepTable": dot1agCfmMepTable,
       "dot1agCfmMepEntry": dot1agCfmMepEntry,
       "dot1agCfmSessionId": dot1agCfmSessionId,
       "dot1agCfmMepIfIndex": dot1agCfmMepIfIndex,
       "dot1agCfmMepDirection": dot1agCfmMepDirection,
       "dot1agCfmMepPrimaryVid": dot1agCfmMepPrimaryVid,
       "dot1agCfmMepActive": dot1agCfmMepActive,
       "dot1agCfmMepFngState": dot1agCfmMepFngState,
       "dot1agCfmMepCciEnabled": dot1agCfmMepCciEnabled,
       "dot1agCfmMepCcmLtmPriority": dot1agCfmMepCcmLtmPriority,
       "dot1agCfmMepMacAddress": dot1agCfmMepMacAddress,
       "dot1agCfmMepLowPrDef": dot1agCfmMepLowPrDef,
       "dot1agCfmMepHighestPrDefect": dot1agCfmMepHighestPrDefect,
       "dot1agCfmMepDefects": dot1agCfmMepDefects,
       "dot1agCfmMepCciSentCcms": dot1agCfmMepCciSentCcms,
       "dot1agCfmMepId": dot1agCfmMepId,
       "dot1agCfmMepMEPAttachType": dot1agCfmMepMEPAttachType,
       "dot1agCfmMepTunnelId": dot1agCfmMepTunnelId,
       "dot1agCfmMepLMFlage": dot1agCfmMepLMFlage,
       "dot1agCfmMepDMFlage": dot1agCfmMepDMFlage,
       "dot1agCfmMepPortName": dot1agCfmMepPortName,
       "dot1agCfmMepLbrIn": dot1agCfmMepLbrIn,
       "dot1agCfmMepLbrInOutOfOrder": dot1agCfmMepLbrInOutOfOrder,
       "dot1agCfmMepLbrBadMsdu": dot1agCfmMepLbrBadMsdu,
       "dot1agCfmMepLtmNextSeqNumber": dot1agCfmMepLtmNextSeqNumber,
       "dot1agCfmMepUnexpLtrIn": dot1agCfmMepUnexpLtrIn,
       "dot1agCfmMepLbrOut": dot1agCfmMepLbrOut,
       "dot1agCfmMepRowStatus": dot1agCfmMepRowStatus,
       "dot1agCfmMepCcCheckFlag": dot1agCfmMepCcCheckFlag,
       "dot1agCfmMepComplexFlag": dot1agCfmMepComplexFlag,
       "dot1agCfmMepclientLevel": dot1agCfmMepclientLevel,
       "dot1agCfmMepAISSendFlag": dot1agCfmMepAISSendFlag,
       "dot1agCfmMepAISEnableFlag": dot1agCfmMepAISEnableFlag,
       "dot1agCfmMepLCKEnableFlag": dot1agCfmMepLCKEnableFlag,
       "dot1agCfmMepTxFCf": dot1agCfmMepTxFCf,
       "dot1agCfmMepRxFCb": dot1agCfmMepRxFCb,
       "dot1agCfmMepTxFCb": dot1agCfmMepTxFCb,
       "dot1agCfmMepRxFCl": dot1agCfmMepRxFCl,
       "dot1agCfmMepNearLost": dot1agCfmMepNearLost,
       "dot1agCfmMepFarLost": dot1agCfmMepFarLost,
       "dot1agCfmMepDaly": dot1agCfmMepDaly,
       "dot1agCfmMepDalyAve": dot1agCfmMepDalyAve,
       "dot1agCfmMepDalyChg": dot1agCfmMepDalyChg,
       "dot1agCfmMepDalyChgAve": dot1agCfmMepDalyChgAve,
       "dot1agCfmMepTransmitLbmStatus": dot1agCfmMepTransmitLbmStatus,
       "dot1agCfmMepTransmitLbmDestMacAddress": dot1agCfmMepTransmitLbmDestMacAddress,
       "dot1agCfmMepTransmitLbmDestSessionId": dot1agCfmMepTransmitLbmDestSessionId,
       "dot1agCfmMepTransmitLbmDestIsSessionId": dot1agCfmMepTransmitLbmDestIsSessionId,
       "dot1agCfmMepTransmitLbmDestMepId": dot1agCfmMepTransmitLbmDestMepId,
       "dot1agCfmMepTransmitLbmDestIsMepId": dot1agCfmMepTransmitLbmDestIsMepId,
       "dot1agCfmMepTransmitLbmMessages": dot1agCfmMepTransmitLbmMessages,
       "dot1agCfmMepTransmitLbmDataTlv": dot1agCfmMepTransmitLbmDataTlv,
       "dot1agCfmMepTransmitLbmVlanPriority": dot1agCfmMepTransmitLbmVlanPriority,
       "dot1agCfmMepTransmitLbmVlanDropEnable": dot1agCfmMepTransmitLbmVlanDropEnable,
       "dot1agCfmMepTransmitLbmResultOK": dot1agCfmMepTransmitLbmResultOK,
       "dot1agCfmMepTransmitLbmSeqNumber": dot1agCfmMepTransmitLbmSeqNumber,
       "dot1agCfmMepTransmitLtmStatus": dot1agCfmMepTransmitLtmStatus,
       "dot1agCfmMepTransmitLtmFlags": dot1agCfmMepTransmitLtmFlags,
       "dot1agCfmMepTransmitLtmTargetMacAddress": dot1agCfmMepTransmitLtmTargetMacAddress,
       "dot1agCfmMepTransmitLtmTargetSessionId": dot1agCfmMepTransmitLtmTargetSessionId,
       "dot1agCfmMepTransmitLtmTargetIsSessionId": dot1agCfmMepTransmitLtmTargetIsSessionId,
       "dot1agCfmMepTransmitLtmTargetMepId": dot1agCfmMepTransmitLtmTargetMepId,
       "dot1agCfmMepTransmitLtmTargetIsMepId": dot1agCfmMepTransmitLtmTargetIsMepId,
       "dot1agCfmMepTransmitLtmTtl": dot1agCfmMepTransmitLtmTtl,
       "dot1agCfmMepTransmitLtmResult": dot1agCfmMepTransmitLtmResult,
       "dot1agCfmMepTransmitLtmSeqNumber": dot1agCfmMepTransmitLtmSeqNumber,
       "dot1agCfmMepTransmitLtmEgressIdentifier": dot1agCfmMepTransmitLtmEgressIdentifier,
       "dot1agCfmLtrTable": dot1agCfmLtrTable,
       "dot1agCfmLtrEntry": dot1agCfmLtrEntry,
       "dot1agCfmLtrSeqNumber": dot1agCfmLtrSeqNumber,
       "dot1agCfmLtrReceiveOrder": dot1agCfmLtrReceiveOrder,
       "dot1agCfmLtrTtl": dot1agCfmLtrTtl,
       "dot1agCfmLtrForwarded": dot1agCfmLtrForwarded,
       "dot1agCfmLtrTerminalMep": dot1agCfmLtrTerminalMep,
       "dot1agCfmLtrLastEgressIdentifier": dot1agCfmLtrLastEgressIdentifier,
       "dot1agCfmLtrNextEgressIdentifier": dot1agCfmLtrNextEgressIdentifier,
       "dot1agCfmLtrRelay": dot1agCfmLtrRelay,
       "dot1agCfmLtrIngress": dot1agCfmLtrIngress,
       "dot1agCfmLtrIngressMac": dot1agCfmLtrIngressMac,
       "dot1agCfmLtrEgress": dot1agCfmLtrEgress,
       "dot1agCfmLtrEgressMac": dot1agCfmLtrEgressMac,
       "dot1agCfmMepDbTable": dot1agCfmMepDbTable,
       "dot1agCfmMepDbEntry": dot1agCfmMepDbEntry,
       "dot1agCfmMepDbRSessionId": dot1agCfmMepDbRSessionId,
       "dot1agCfmMepDbMacAddress": dot1agCfmMepDbMacAddress,
       "dot1agCfmMepDbRdi": dot1agCfmMepDbRdi,
       "dot1agCfmMepDbId": dot1agCfmMepDbId,
       "dot1agCfmMepDbRowStatus": dot1agCfmMepDbRowStatus,
       "dot1agCfmLbrInfo": dot1agCfmLbrInfo,
       "dot1agCfmLbrTransId": dot1agCfmLbrTransId,
       "dot1agCfmLbrPrintInfo": dot1agCfmLbrPrintInfo,
       "dot1agCfmMipTable": dot1agCfmMipTable,
       "dot1agCfmMipEntry": dot1agCfmMipEntry,
       "dot1agCfmMipSessionId": dot1agCfmMipSessionId,
       "dot1agCfmMipName": dot1agCfmMipName,
       "dot1agCfmMipPortName": dot1agCfmMipPortName,
       "dot1agCfmGloPara": dot1agCfmGloPara,
       "dot1agCfmGlobalIsEnable": dot1agCfmGlobalIsEnable}
)
