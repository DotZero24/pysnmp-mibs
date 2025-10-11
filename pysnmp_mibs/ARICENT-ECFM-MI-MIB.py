# SNMP MIB module (ARICENT-ECFM-MI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siaemic/ARICENT-ECFM-MI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:37 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpPortId",
    "LldpPortIdSubtype")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fsMIEcfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 160)
)
if mibBuilder.loadTexts:
    fsMIEcfmMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsMIEcfmOuiType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class FsMIEcfmMaintDomainNameType(TextualConvention, Integer32):
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



class FsMIEcfmMaintDomainName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )



class FsMIEcfmMaintAssocNameType(TextualConvention, Integer32):
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



class FsMIEcfmMaintAssocName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class FsMIEcfmMDLevel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class FsMIEcfmMDLevelOrNone(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class FsMIEcfmMpDirection(TextualConvention, Integer32):
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



class FsMIEcfmPortStatus(TextualConvention, Integer32):
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
        *(("psNoPortStateTLV", 0),
          ("psBlocked", 1),
          ("psUp", 2))
    )



class FsMIEcfmInterfaceStatus(TextualConvention, Integer32):
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
        *(("isNoInterfaceStatusTLV", 0),
          ("isUp", 1),
          ("isDown", 2),
          ("isTesting", 3),
          ("isUnknown", 4),
          ("isDormant", 5),
          ("isNotPresent", 6),
          ("isLowerLayerDown", 7))
    )



class FsMIEcfmHighestDefectPri(TextualConvention, Integer32):
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



class FsMIEcfmLowestAlarmPri(TextualConvention, Integer32):
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



class FsMIEcfmMepId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )



class FsMIEcfmMepIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )



class FsMIEcfmMhfCreation(TextualConvention, Integer32):
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



class FsMIEcfmIdPermission(TextualConvention, Integer32):
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



class FsMIEcfmCcmInterval(TextualConvention, Integer32):
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



class FsMIEcfmFngState(TextualConvention, Integer32):
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



class FsMIEcfmRelayActionFieldValue(TextualConvention, Integer32):
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



class FsMIEcfmIngressActionFieldValue(TextualConvention, Integer32):
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



class FsMIEcfmEgressActionFieldValue(TextualConvention, Integer32):
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



class FsMIEcfmRemoteMepState(TextualConvention, Integer32):
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
        *(("rMepIdle", 1),
          ("rMepStart", 2),
          ("rMepFailed", 3),
          ("rMepOk", 4))
    )



class FsMIEcfmIndexIntegerNextFree(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class FsMIEcfmMepDefects(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bUnUsedBit", 0),
          ("bDefRDICCM", 1),
          ("bDefMACstatus", 2),
          ("bDefRemoteCCM", 3),
          ("bDefErrorCCM", 4),
          ("bDefXconCCM", 5))
    )


class FsMIEcfmConfigErrors(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cfmLeak", 0),
          ("conflictingVids", 1),
          ("excessiveLevels", 2),
          ("overlappedLevels", 3))
    )


class FsMIEcfmTransmitStatus(TextualConvention, Integer32):
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
        *(("ready", 0),
          ("notReady", 1),
          ("transmit", 2))
    )



class FsMIEcfmSetTraps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("trapUnUsedBit", 0),
          ("trapRDICCM", 1),
          ("trapMACstatus", 2),
          ("trapRemoteCCM", 3),
          ("trapErrorCCM", 4),
          ("trapXconCCM", 5))
    )


# MIB Managed Objects in the order of their OIDs

_FsMIEcfmNotifications_ObjectIdentity = ObjectIdentity
fsMIEcfmNotifications = _FsMIEcfmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 160, 0)
)
_FsMIEcfmMIBObjects_ObjectIdentity = ObjectIdentity
fsMIEcfmMIBObjects = _FsMIEcfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1)
)
_FsMIEcfmContext_ObjectIdentity = ObjectIdentity
fsMIEcfmContext = _FsMIEcfmContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0)
)
_FsMIEcfmContextTable_Object = MibTable
fsMIEcfmContextTable = _FsMIEcfmContextTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1)
)
if mibBuilder.loadTexts:
    fsMIEcfmContextTable.setStatus("current")
_FsMIEcfmContextEntry_Object = MibTableRow
fsMIEcfmContextEntry = _FsMIEcfmContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1)
)
fsMIEcfmContextEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
)
if mibBuilder.loadTexts:
    fsMIEcfmContextEntry.setStatus("current")
_FsMIEcfmContextId_Type = Unsigned32
_FsMIEcfmContextId_Object = MibTableColumn
fsMIEcfmContextId = _FsMIEcfmContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 1),
    _FsMIEcfmContextId_Type()
)
fsMIEcfmContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmContextId.setStatus("current")


class _FsMIEcfmSystemControl_Type(Integer32):
    """Custom type fsMIEcfmSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsMIEcfmSystemControl_Type.__name__ = "Integer32"
_FsMIEcfmSystemControl_Object = MibTableColumn
fsMIEcfmSystemControl = _FsMIEcfmSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 2),
    _FsMIEcfmSystemControl_Type()
)
fsMIEcfmSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmSystemControl.setStatus("current")


class _FsMIEcfmModuleStatus_Type(Integer32):
    """Custom type fsMIEcfmModuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIEcfmModuleStatus_Type.__name__ = "Integer32"
_FsMIEcfmModuleStatus_Object = MibTableColumn
fsMIEcfmModuleStatus = _FsMIEcfmModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 3),
    _FsMIEcfmModuleStatus_Type()
)
fsMIEcfmModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmModuleStatus.setStatus("current")


class _FsMIEcfmDefaultMdDefLevel_Type(FsMIEcfmMDLevel):
    """Custom type fsMIEcfmDefaultMdDefLevel based on FsMIEcfmMDLevel"""
    defaultValue = 0


_FsMIEcfmDefaultMdDefLevel_Type.__name__ = "FsMIEcfmMDLevel"
_FsMIEcfmDefaultMdDefLevel_Object = MibTableColumn
fsMIEcfmDefaultMdDefLevel = _FsMIEcfmDefaultMdDefLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 4),
    _FsMIEcfmDefaultMdDefLevel_Type()
)
fsMIEcfmDefaultMdDefLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdDefLevel.setStatus("current")


class _FsMIEcfmDefaultMdDefMhfCreation_Type(FsMIEcfmMhfCreation):
    """Custom type fsMIEcfmDefaultMdDefMhfCreation based on FsMIEcfmMhfCreation"""
    defaultValue = 1


_FsMIEcfmDefaultMdDefMhfCreation_Type.__name__ = "FsMIEcfmMhfCreation"
_FsMIEcfmDefaultMdDefMhfCreation_Object = MibTableColumn
fsMIEcfmDefaultMdDefMhfCreation = _FsMIEcfmDefaultMdDefMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 5),
    _FsMIEcfmDefaultMdDefMhfCreation_Type()
)
fsMIEcfmDefaultMdDefMhfCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdDefMhfCreation.setStatus("current")


class _FsMIEcfmDefaultMdDefIdPermission_Type(FsMIEcfmIdPermission):
    """Custom type fsMIEcfmDefaultMdDefIdPermission based on FsMIEcfmIdPermission"""
    defaultValue = 1


_FsMIEcfmDefaultMdDefIdPermission_Type.__name__ = "FsMIEcfmIdPermission"
_FsMIEcfmDefaultMdDefIdPermission_Object = MibTableColumn
fsMIEcfmDefaultMdDefIdPermission = _FsMIEcfmDefaultMdDefIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 6),
    _FsMIEcfmDefaultMdDefIdPermission_Type()
)
fsMIEcfmDefaultMdDefIdPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdDefIdPermission.setStatus("current")
_FsMIEcfmMdTableNextIndex_Type = FsMIEcfmIndexIntegerNextFree
_FsMIEcfmMdTableNextIndex_Object = MibTableColumn
fsMIEcfmMdTableNextIndex = _FsMIEcfmMdTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 7),
    _FsMIEcfmMdTableNextIndex_Type()
)
fsMIEcfmMdTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMdTableNextIndex.setStatus("current")


class _FsMIEcfmLtrCacheStatus_Type(Integer32):
    """Custom type fsMIEcfmLtrCacheStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIEcfmLtrCacheStatus_Type.__name__ = "Integer32"
_FsMIEcfmLtrCacheStatus_Object = MibTableColumn
fsMIEcfmLtrCacheStatus = _FsMIEcfmLtrCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 8),
    _FsMIEcfmLtrCacheStatus_Type()
)
fsMIEcfmLtrCacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmLtrCacheStatus.setStatus("current")


class _FsMIEcfmLtrCacheClear_Type(TruthValue):
    """Custom type fsMIEcfmLtrCacheClear based on TruthValue"""
    defaultValue = 2


_FsMIEcfmLtrCacheClear_Type.__name__ = "TruthValue"
_FsMIEcfmLtrCacheClear_Object = MibTableColumn
fsMIEcfmLtrCacheClear = _FsMIEcfmLtrCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 9),
    _FsMIEcfmLtrCacheClear_Type()
)
fsMIEcfmLtrCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmLtrCacheClear.setStatus("current")


class _FsMIEcfmLtrCacheHoldTime_Type(Integer32):
    """Custom type fsMIEcfmLtrCacheHoldTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIEcfmLtrCacheHoldTime_Type.__name__ = "Integer32"
_FsMIEcfmLtrCacheHoldTime_Object = MibTableColumn
fsMIEcfmLtrCacheHoldTime = _FsMIEcfmLtrCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 10),
    _FsMIEcfmLtrCacheHoldTime_Type()
)
fsMIEcfmLtrCacheHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmLtrCacheHoldTime.setStatus("current")


class _FsMIEcfmLtrCacheSize_Type(Integer32):
    """Custom type fsMIEcfmLtrCacheSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsMIEcfmLtrCacheSize_Type.__name__ = "Integer32"
_FsMIEcfmLtrCacheSize_Object = MibTableColumn
fsMIEcfmLtrCacheSize = _FsMIEcfmLtrCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 11),
    _FsMIEcfmLtrCacheSize_Type()
)
fsMIEcfmLtrCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmLtrCacheSize.setStatus("current")


class _FsMIEcfmMipCcmDbStatus_Type(Integer32):
    """Custom type fsMIEcfmMipCcmDbStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIEcfmMipCcmDbStatus_Type.__name__ = "Integer32"
_FsMIEcfmMipCcmDbStatus_Object = MibTableColumn
fsMIEcfmMipCcmDbStatus = _FsMIEcfmMipCcmDbStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 12),
    _FsMIEcfmMipCcmDbStatus_Type()
)
fsMIEcfmMipCcmDbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMipCcmDbStatus.setStatus("current")


class _FsMIEcfmMipCcmDbClear_Type(TruthValue):
    """Custom type fsMIEcfmMipCcmDbClear based on TruthValue"""
    defaultValue = 2


_FsMIEcfmMipCcmDbClear_Type.__name__ = "TruthValue"
_FsMIEcfmMipCcmDbClear_Object = MibTableColumn
fsMIEcfmMipCcmDbClear = _FsMIEcfmMipCcmDbClear_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 13),
    _FsMIEcfmMipCcmDbClear_Type()
)
fsMIEcfmMipCcmDbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMipCcmDbClear.setStatus("current")


class _FsMIEcfmMipCcmDbSize_Type(Integer32):
    """Custom type fsMIEcfmMipCcmDbSize based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_FsMIEcfmMipCcmDbSize_Type.__name__ = "Integer32"
_FsMIEcfmMipCcmDbSize_Object = MibTableColumn
fsMIEcfmMipCcmDbSize = _FsMIEcfmMipCcmDbSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 14),
    _FsMIEcfmMipCcmDbSize_Type()
)
fsMIEcfmMipCcmDbSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMipCcmDbSize.setStatus("current")


class _FsMIEcfmMipCcmDbHoldTime_Type(Integer32):
    """Custom type fsMIEcfmMipCcmDbHoldTime based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 48),
    )


_FsMIEcfmMipCcmDbHoldTime_Type.__name__ = "Integer32"
_FsMIEcfmMipCcmDbHoldTime_Object = MibTableColumn
fsMIEcfmMipCcmDbHoldTime = _FsMIEcfmMipCcmDbHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 15),
    _FsMIEcfmMipCcmDbHoldTime_Type()
)
fsMIEcfmMipCcmDbHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMipCcmDbHoldTime.setStatus("current")
_FsMIEcfmMemoryFailureCount_Type = Unsigned32
_FsMIEcfmMemoryFailureCount_Object = MibTableColumn
fsMIEcfmMemoryFailureCount = _FsMIEcfmMemoryFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 16),
    _FsMIEcfmMemoryFailureCount_Type()
)
fsMIEcfmMemoryFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMemoryFailureCount.setStatus("current")
_FsMIEcfmBufferFailureCount_Type = Unsigned32
_FsMIEcfmBufferFailureCount_Object = MibTableColumn
fsMIEcfmBufferFailureCount = _FsMIEcfmBufferFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 17),
    _FsMIEcfmBufferFailureCount_Type()
)
fsMIEcfmBufferFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmBufferFailureCount.setStatus("current")
_FsMIEcfmUpCount_Type = Unsigned32
_FsMIEcfmUpCount_Object = MibTableColumn
fsMIEcfmUpCount = _FsMIEcfmUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 18),
    _FsMIEcfmUpCount_Type()
)
fsMIEcfmUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmUpCount.setStatus("current")
_FsMIEcfmDownCount_Type = Unsigned32
_FsMIEcfmDownCount_Object = MibTableColumn
fsMIEcfmDownCount = _FsMIEcfmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 19),
    _FsMIEcfmDownCount_Type()
)
fsMIEcfmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmDownCount.setStatus("current")
_FsMIEcfmNoDftCount_Type = Unsigned32
_FsMIEcfmNoDftCount_Object = MibTableColumn
fsMIEcfmNoDftCount = _FsMIEcfmNoDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 20),
    _FsMIEcfmNoDftCount_Type()
)
fsMIEcfmNoDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmNoDftCount.setStatus("current")
_FsMIEcfmRdiDftCount_Type = Unsigned32
_FsMIEcfmRdiDftCount_Object = MibTableColumn
fsMIEcfmRdiDftCount = _FsMIEcfmRdiDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 21),
    _FsMIEcfmRdiDftCount_Type()
)
fsMIEcfmRdiDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRdiDftCount.setStatus("current")
_FsMIEcfmMacStatusDftCount_Type = Unsigned32
_FsMIEcfmMacStatusDftCount_Object = MibTableColumn
fsMIEcfmMacStatusDftCount = _FsMIEcfmMacStatusDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 22),
    _FsMIEcfmMacStatusDftCount_Type()
)
fsMIEcfmMacStatusDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMacStatusDftCount.setStatus("current")
_FsMIEcfmRemoteCcmDftCount_Type = Unsigned32
_FsMIEcfmRemoteCcmDftCount_Object = MibTableColumn
fsMIEcfmRemoteCcmDftCount = _FsMIEcfmRemoteCcmDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 23),
    _FsMIEcfmRemoteCcmDftCount_Type()
)
fsMIEcfmRemoteCcmDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRemoteCcmDftCount.setStatus("current")
_FsMIEcfmErrorCcmDftCount_Type = Unsigned32
_FsMIEcfmErrorCcmDftCount_Object = MibTableColumn
fsMIEcfmErrorCcmDftCount = _FsMIEcfmErrorCcmDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 24),
    _FsMIEcfmErrorCcmDftCount_Type()
)
fsMIEcfmErrorCcmDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmErrorCcmDftCount.setStatus("current")
_FsMIEcfmXconDftCount_Type = Unsigned32
_FsMIEcfmXconDftCount_Object = MibTableColumn
fsMIEcfmXconDftCount = _FsMIEcfmXconDftCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 25),
    _FsMIEcfmXconDftCount_Type()
)
fsMIEcfmXconDftCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmXconDftCount.setStatus("current")


class _FsMIEcfmCrosscheckDelay_Type(Integer32):
    """Custom type fsMIEcfmCrosscheckDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 100),
    )


_FsMIEcfmCrosscheckDelay_Type.__name__ = "Integer32"
_FsMIEcfmCrosscheckDelay_Object = MibTableColumn
fsMIEcfmCrosscheckDelay = _FsMIEcfmCrosscheckDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 26),
    _FsMIEcfmCrosscheckDelay_Type()
)
fsMIEcfmCrosscheckDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmCrosscheckDelay.setStatus("current")
_FsMIEcfmMipDynamicEvaluationStatus_Type = TruthValue
_FsMIEcfmMipDynamicEvaluationStatus_Object = MibTableColumn
fsMIEcfmMipDynamicEvaluationStatus = _FsMIEcfmMipDynamicEvaluationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 27),
    _FsMIEcfmMipDynamicEvaluationStatus_Type()
)
fsMIEcfmMipDynamicEvaluationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMipDynamicEvaluationStatus.setStatus("current")


class _FsMIEcfmContextName_Type(DisplayString):
    """Custom type fsMIEcfmContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsMIEcfmContextName_Type.__name__ = "DisplayString"
_FsMIEcfmContextName_Object = MibTableColumn
fsMIEcfmContextName = _FsMIEcfmContextName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 28),
    _FsMIEcfmContextName_Type()
)
fsMIEcfmContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmContextName.setStatus("current")
_FsMIEcfmTrapControl_Type = FsMIEcfmSetTraps
_FsMIEcfmTrapControl_Object = MibTableColumn
fsMIEcfmTrapControl = _FsMIEcfmTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 29),
    _FsMIEcfmTrapControl_Type()
)
fsMIEcfmTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmTrapControl.setStatus("current")


class _FsMIEcfmTrapType_Type(Integer32):
    """Custom type fsMIEcfmTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trapRDICCM", 2),
          ("trapMACStatus", 3),
          ("trapRemoteCCM", 4),
          ("trapErroredCCM", 5),
          ("trapXConnCCM", 6))
    )


_FsMIEcfmTrapType_Type.__name__ = "Integer32"
_FsMIEcfmTrapType_Object = MibTableColumn
fsMIEcfmTrapType = _FsMIEcfmTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 30),
    _FsMIEcfmTrapType_Type()
)
fsMIEcfmTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmTrapType.setStatus("current")


class _FsMIEcfmTraceOption_Type(Integer32):
    """Custom type fsMIEcfmTraceOption based on Integer32"""
    defaultValue = 262144


_FsMIEcfmTraceOption_Type.__name__ = "Integer32"
_FsMIEcfmTraceOption_Object = MibTableColumn
fsMIEcfmTraceOption = _FsMIEcfmTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 31),
    _FsMIEcfmTraceOption_Type()
)
fsMIEcfmTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmTraceOption.setStatus("current")


class _FsMIEcfmGlobalCcmOffload_Type(Integer32):
    """Custom type fsMIEcfmGlobalCcmOffload based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIEcfmGlobalCcmOffload_Type.__name__ = "Integer32"
_FsMIEcfmGlobalCcmOffload_Object = MibTableColumn
fsMIEcfmGlobalCcmOffload = _FsMIEcfmGlobalCcmOffload_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 1, 1, 32),
    _FsMIEcfmGlobalCcmOffload_Type()
)
fsMIEcfmGlobalCcmOffload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmGlobalCcmOffload.setStatus("current")
_FsMIEcfmVlanTable_Object = MibTable
fsMIEcfmVlanTable = _FsMIEcfmVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 2)
)
if mibBuilder.loadTexts:
    fsMIEcfmVlanTable.setStatus("current")
_FsMIEcfmVlanEntry_Object = MibTableRow
fsMIEcfmVlanEntry = _FsMIEcfmVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 2, 1)
)
fsMIEcfmVlanEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmVlanVid"),
)
if mibBuilder.loadTexts:
    fsMIEcfmVlanEntry.setStatus("current")
_FsMIEcfmVlanVid_Type = VlanId
_FsMIEcfmVlanVid_Object = MibTableColumn
fsMIEcfmVlanVid = _FsMIEcfmVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 2, 1, 1),
    _FsMIEcfmVlanVid_Type()
)
fsMIEcfmVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmVlanVid.setStatus("current")
_FsMIEcfmVlanPrimaryVid_Type = VlanId
_FsMIEcfmVlanPrimaryVid_Object = MibTableColumn
fsMIEcfmVlanPrimaryVid = _FsMIEcfmVlanPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 2, 1, 2),
    _FsMIEcfmVlanPrimaryVid_Type()
)
fsMIEcfmVlanPrimaryVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmVlanPrimaryVid.setStatus("current")
_FsMIEcfmVlanRowStatus_Type = RowStatus
_FsMIEcfmVlanRowStatus_Object = MibTableColumn
fsMIEcfmVlanRowStatus = _FsMIEcfmVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 2, 1, 3),
    _FsMIEcfmVlanRowStatus_Type()
)
fsMIEcfmVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmVlanRowStatus.setStatus("current")
_FsMIEcfmDefaultMdTable_Object = MibTable
fsMIEcfmDefaultMdTable = _FsMIEcfmDefaultMdTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 3)
)
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdTable.setStatus("current")
_FsMIEcfmDefaultMdEntry_Object = MibTableRow
fsMIEcfmDefaultMdEntry = _FsMIEcfmDefaultMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 3, 1)
)
fsMIEcfmDefaultMdEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmDefaultMdPrimaryVid"),
)
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdEntry.setStatus("current")
_FsMIEcfmDefaultMdPrimaryVid_Type = VlanId
_FsMIEcfmDefaultMdPrimaryVid_Object = MibTableColumn
fsMIEcfmDefaultMdPrimaryVid = _FsMIEcfmDefaultMdPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 3, 1, 1),
    _FsMIEcfmDefaultMdPrimaryVid_Type()
)
fsMIEcfmDefaultMdPrimaryVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdPrimaryVid.setStatus("current")
_FsMIEcfmDefaultMdStatus_Type = TruthValue
_FsMIEcfmDefaultMdStatus_Object = MibTableColumn
fsMIEcfmDefaultMdStatus = _FsMIEcfmDefaultMdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 3, 1, 2),
    _FsMIEcfmDefaultMdStatus_Type()
)
fsMIEcfmDefaultMdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdStatus.setStatus("current")


class _FsMIEcfmDefaultMdLevel_Type(FsMIEcfmMDLevelOrNone):
    """Custom type fsMIEcfmDefaultMdLevel based on FsMIEcfmMDLevelOrNone"""
    defaultValue = -1


_FsMIEcfmDefaultMdLevel_Type.__name__ = "FsMIEcfmMDLevelOrNone"
_FsMIEcfmDefaultMdLevel_Object = MibTableColumn
fsMIEcfmDefaultMdLevel = _FsMIEcfmDefaultMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 3, 1, 3),
    _FsMIEcfmDefaultMdLevel_Type()
)
fsMIEcfmDefaultMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdLevel.setStatus("current")


class _FsMIEcfmDefaultMdMhfCreation_Type(FsMIEcfmMhfCreation):
    """Custom type fsMIEcfmDefaultMdMhfCreation based on FsMIEcfmMhfCreation"""
    defaultValue = 4


_FsMIEcfmDefaultMdMhfCreation_Type.__name__ = "FsMIEcfmMhfCreation"
_FsMIEcfmDefaultMdMhfCreation_Object = MibTableColumn
fsMIEcfmDefaultMdMhfCreation = _FsMIEcfmDefaultMdMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 3, 1, 4),
    _FsMIEcfmDefaultMdMhfCreation_Type()
)
fsMIEcfmDefaultMdMhfCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdMhfCreation.setStatus("current")


class _FsMIEcfmDefaultMdIdPermission_Type(FsMIEcfmIdPermission):
    """Custom type fsMIEcfmDefaultMdIdPermission based on FsMIEcfmIdPermission"""
    defaultValue = 5


_FsMIEcfmDefaultMdIdPermission_Type.__name__ = "FsMIEcfmIdPermission"
_FsMIEcfmDefaultMdIdPermission_Object = MibTableColumn
fsMIEcfmDefaultMdIdPermission = _FsMIEcfmDefaultMdIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 3, 1, 5),
    _FsMIEcfmDefaultMdIdPermission_Type()
)
fsMIEcfmDefaultMdIdPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmDefaultMdIdPermission.setStatus("current")
_FsMIEcfmMdTable_Object = MibTable
fsMIEcfmMdTable = _FsMIEcfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4)
)
if mibBuilder.loadTexts:
    fsMIEcfmMdTable.setStatus("current")
_FsMIEcfmMdEntry_Object = MibTableRow
fsMIEcfmMdEntry = _FsMIEcfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4, 1)
)
fsMIEcfmMdEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMdEntry.setStatus("current")


class _FsMIEcfmMdIndex_Type(Unsigned32):
    """Custom type fsMIEcfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMIEcfmMdIndex_Type.__name__ = "Unsigned32"
_FsMIEcfmMdIndex_Object = MibTableColumn
fsMIEcfmMdIndex = _FsMIEcfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4, 1, 1),
    _FsMIEcfmMdIndex_Type()
)
fsMIEcfmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMdIndex.setStatus("current")


class _FsMIEcfmMdFormat_Type(FsMIEcfmMaintDomainNameType):
    """Custom type fsMIEcfmMdFormat based on FsMIEcfmMaintDomainNameType"""
    defaultValue = 4


_FsMIEcfmMdFormat_Type.__name__ = "FsMIEcfmMaintDomainNameType"
_FsMIEcfmMdFormat_Object = MibTableColumn
fsMIEcfmMdFormat = _FsMIEcfmMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4, 1, 2),
    _FsMIEcfmMdFormat_Type()
)
fsMIEcfmMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMdFormat.setStatus("current")


class _FsMIEcfmMdName_Type(FsMIEcfmMaintDomainName):
    """Custom type fsMIEcfmMdName based on FsMIEcfmMaintDomainName"""
    defaultValue = OctetString("DEFAULT")


_FsMIEcfmMdName_Type.__name__ = "FsMIEcfmMaintDomainName"
_FsMIEcfmMdName_Object = MibTableColumn
fsMIEcfmMdName = _FsMIEcfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4, 1, 3),
    _FsMIEcfmMdName_Type()
)
fsMIEcfmMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMdName.setStatus("current")


class _FsMIEcfmMdMdLevel_Type(FsMIEcfmMDLevel):
    """Custom type fsMIEcfmMdMdLevel based on FsMIEcfmMDLevel"""
    defaultValue = 0


_FsMIEcfmMdMdLevel_Type.__name__ = "FsMIEcfmMDLevel"
_FsMIEcfmMdMdLevel_Object = MibTableColumn
fsMIEcfmMdMdLevel = _FsMIEcfmMdMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4, 1, 4),
    _FsMIEcfmMdMdLevel_Type()
)
fsMIEcfmMdMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMdMdLevel.setStatus("current")


class _FsMIEcfmMdMhfCreation_Type(FsMIEcfmMhfCreation):
    """Custom type fsMIEcfmMdMhfCreation based on FsMIEcfmMhfCreation"""
    defaultValue = 1


_FsMIEcfmMdMhfCreation_Type.__name__ = "FsMIEcfmMhfCreation"
_FsMIEcfmMdMhfCreation_Object = MibTableColumn
fsMIEcfmMdMhfCreation = _FsMIEcfmMdMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4, 1, 5),
    _FsMIEcfmMdMhfCreation_Type()
)
fsMIEcfmMdMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMdMhfCreation.setStatus("current")


class _FsMIEcfmMdMhfIdPermission_Type(FsMIEcfmIdPermission):
    """Custom type fsMIEcfmMdMhfIdPermission based on FsMIEcfmIdPermission"""
    defaultValue = 1


_FsMIEcfmMdMhfIdPermission_Type.__name__ = "FsMIEcfmIdPermission"
_FsMIEcfmMdMhfIdPermission_Object = MibTableColumn
fsMIEcfmMdMhfIdPermission = _FsMIEcfmMdMhfIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4, 1, 6),
    _FsMIEcfmMdMhfIdPermission_Type()
)
fsMIEcfmMdMhfIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMdMhfIdPermission.setStatus("current")
_FsMIEcfmMdMaTableNextIndex_Type = FsMIEcfmIndexIntegerNextFree
_FsMIEcfmMdMaTableNextIndex_Object = MibTableColumn
fsMIEcfmMdMaTableNextIndex = _FsMIEcfmMdMaTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4, 1, 7),
    _FsMIEcfmMdMaTableNextIndex_Type()
)
fsMIEcfmMdMaTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMdMaTableNextIndex.setStatus("current")
_FsMIEcfmMdRowStatus_Type = RowStatus
_FsMIEcfmMdRowStatus_Object = MibTableColumn
fsMIEcfmMdRowStatus = _FsMIEcfmMdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 4, 1, 8),
    _FsMIEcfmMdRowStatus_Type()
)
fsMIEcfmMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMdRowStatus.setStatus("current")
_FsMIEcfmMaTable_Object = MibTable
fsMIEcfmMaTable = _FsMIEcfmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5)
)
if mibBuilder.loadTexts:
    fsMIEcfmMaTable.setStatus("current")
_FsMIEcfmMaEntry_Object = MibTableRow
fsMIEcfmMaEntry = _FsMIEcfmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1)
)
fsMIEcfmMaEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaIndex"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMaEntry.setStatus("current")


class _FsMIEcfmMaIndex_Type(Unsigned32):
    """Custom type fsMIEcfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMIEcfmMaIndex_Type.__name__ = "Unsigned32"
_FsMIEcfmMaIndex_Object = MibTableColumn
fsMIEcfmMaIndex = _FsMIEcfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1, 1),
    _FsMIEcfmMaIndex_Type()
)
fsMIEcfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMaIndex.setStatus("current")
_FsMIEcfmMaPrimaryVlanId_Type = VlanIdOrNone
_FsMIEcfmMaPrimaryVlanId_Object = MibTableColumn
fsMIEcfmMaPrimaryVlanId = _FsMIEcfmMaPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1, 2),
    _FsMIEcfmMaPrimaryVlanId_Type()
)
fsMIEcfmMaPrimaryVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMaPrimaryVlanId.setStatus("current")
_FsMIEcfmMaFormat_Type = FsMIEcfmMaintAssocNameType
_FsMIEcfmMaFormat_Object = MibTableColumn
fsMIEcfmMaFormat = _FsMIEcfmMaFormat_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1, 3),
    _FsMIEcfmMaFormat_Type()
)
fsMIEcfmMaFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMaFormat.setStatus("current")
_FsMIEcfmMaName_Type = FsMIEcfmMaintAssocName
_FsMIEcfmMaName_Object = MibTableColumn
fsMIEcfmMaName = _FsMIEcfmMaName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1, 4),
    _FsMIEcfmMaName_Type()
)
fsMIEcfmMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMaName.setStatus("current")


class _FsMIEcfmMaMhfCreation_Type(FsMIEcfmMhfCreation):
    """Custom type fsMIEcfmMaMhfCreation based on FsMIEcfmMhfCreation"""
    defaultValue = 4


_FsMIEcfmMaMhfCreation_Type.__name__ = "FsMIEcfmMhfCreation"
_FsMIEcfmMaMhfCreation_Object = MibTableColumn
fsMIEcfmMaMhfCreation = _FsMIEcfmMaMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1, 5),
    _FsMIEcfmMaMhfCreation_Type()
)
fsMIEcfmMaMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMaMhfCreation.setStatus("current")


class _FsMIEcfmMaIdPermission_Type(FsMIEcfmIdPermission):
    """Custom type fsMIEcfmMaIdPermission based on FsMIEcfmIdPermission"""
    defaultValue = 5


_FsMIEcfmMaIdPermission_Type.__name__ = "FsMIEcfmIdPermission"
_FsMIEcfmMaIdPermission_Object = MibTableColumn
fsMIEcfmMaIdPermission = _FsMIEcfmMaIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1, 6),
    _FsMIEcfmMaIdPermission_Type()
)
fsMIEcfmMaIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMaIdPermission.setStatus("current")


class _FsMIEcfmMaCcmInterval_Type(FsMIEcfmCcmInterval):
    """Custom type fsMIEcfmMaCcmInterval based on FsMIEcfmCcmInterval"""
    defaultValue = 4


_FsMIEcfmMaCcmInterval_Type.__name__ = "FsMIEcfmCcmInterval"
_FsMIEcfmMaCcmInterval_Object = MibTableColumn
fsMIEcfmMaCcmInterval = _FsMIEcfmMaCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1, 7),
    _FsMIEcfmMaCcmInterval_Type()
)
fsMIEcfmMaCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMaCcmInterval.setStatus("current")
_FsMIEcfmMaNumberOfVids_Type = Unsigned32
_FsMIEcfmMaNumberOfVids_Object = MibTableColumn
fsMIEcfmMaNumberOfVids = _FsMIEcfmMaNumberOfVids_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1, 8),
    _FsMIEcfmMaNumberOfVids_Type()
)
fsMIEcfmMaNumberOfVids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMaNumberOfVids.setStatus("current")
_FsMIEcfmMaRowStatus_Type = RowStatus
_FsMIEcfmMaRowStatus_Object = MibTableColumn
fsMIEcfmMaRowStatus = _FsMIEcfmMaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 5, 1, 9),
    _FsMIEcfmMaRowStatus_Type()
)
fsMIEcfmMaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMaRowStatus.setStatus("current")
_FsMIEcfmMaMepListTable_Object = MibTable
fsMIEcfmMaMepListTable = _FsMIEcfmMaMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 6)
)
if mibBuilder.loadTexts:
    fsMIEcfmMaMepListTable.setStatus("current")
_FsMIEcfmMaMepListEntry_Object = MibTableRow
fsMIEcfmMaMepListEntry = _FsMIEcfmMaMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 6, 1)
)
fsMIEcfmMaMepListEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaMepListIdentifier"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMaMepListEntry.setStatus("current")
_FsMIEcfmMaMepListIdentifier_Type = FsMIEcfmMepId
_FsMIEcfmMaMepListIdentifier_Object = MibTableColumn
fsMIEcfmMaMepListIdentifier = _FsMIEcfmMaMepListIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 6, 1, 1),
    _FsMIEcfmMaMepListIdentifier_Type()
)
fsMIEcfmMaMepListIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMaMepListIdentifier.setStatus("current")
_FsMIEcfmMaMepListRowStatus_Type = RowStatus
_FsMIEcfmMaMepListRowStatus_Object = MibTableColumn
fsMIEcfmMaMepListRowStatus = _FsMIEcfmMaMepListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 6, 1, 2),
    _FsMIEcfmMaMepListRowStatus_Type()
)
fsMIEcfmMaMepListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMaMepListRowStatus.setStatus("current")
_FsMIEcfmMepTable_Object = MibTable
fsMIEcfmMepTable = _FsMIEcfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7)
)
if mibBuilder.loadTexts:
    fsMIEcfmMepTable.setStatus("current")
_FsMIEcfmMepEntry_Object = MibTableRow
fsMIEcfmMepEntry = _FsMIEcfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1)
)
fsMIEcfmMepEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMepEntry.setStatus("current")
_FsMIEcfmMepIdentifier_Type = FsMIEcfmMepId
_FsMIEcfmMepIdentifier_Object = MibTableColumn
fsMIEcfmMepIdentifier = _FsMIEcfmMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 1),
    _FsMIEcfmMepIdentifier_Type()
)
fsMIEcfmMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMepIdentifier.setStatus("current")
_FsMIEcfmMepIfIndex_Type = InterfaceIndexOrZero
_FsMIEcfmMepIfIndex_Object = MibTableColumn
fsMIEcfmMepIfIndex = _FsMIEcfmMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 2),
    _FsMIEcfmMepIfIndex_Type()
)
fsMIEcfmMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepIfIndex.setStatus("current")
_FsMIEcfmMepDirection_Type = FsMIEcfmMpDirection
_FsMIEcfmMepDirection_Object = MibTableColumn
fsMIEcfmMepDirection = _FsMIEcfmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 3),
    _FsMIEcfmMepDirection_Type()
)
fsMIEcfmMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepDirection.setStatus("current")


class _FsMIEcfmMepPrimaryVid_Type(Unsigned32):
    """Custom type fsMIEcfmMepPrimaryVid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FsMIEcfmMepPrimaryVid_Type.__name__ = "Unsigned32"
_FsMIEcfmMepPrimaryVid_Object = MibTableColumn
fsMIEcfmMepPrimaryVid = _FsMIEcfmMepPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 4),
    _FsMIEcfmMepPrimaryVid_Type()
)
fsMIEcfmMepPrimaryVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepPrimaryVid.setStatus("current")


class _FsMIEcfmMepActive_Type(TruthValue):
    """Custom type fsMIEcfmMepActive based on TruthValue"""
    defaultValue = 2


_FsMIEcfmMepActive_Type.__name__ = "TruthValue"
_FsMIEcfmMepActive_Object = MibTableColumn
fsMIEcfmMepActive = _FsMIEcfmMepActive_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 5),
    _FsMIEcfmMepActive_Type()
)
fsMIEcfmMepActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepActive.setStatus("current")


class _FsMIEcfmMepFngState_Type(FsMIEcfmFngState):
    """Custom type fsMIEcfmMepFngState based on FsMIEcfmFngState"""
    defaultValue = 1


_FsMIEcfmMepFngState_Type.__name__ = "FsMIEcfmFngState"
_FsMIEcfmMepFngState_Object = MibTableColumn
fsMIEcfmMepFngState = _FsMIEcfmMepFngState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 6),
    _FsMIEcfmMepFngState_Type()
)
fsMIEcfmMepFngState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepFngState.setStatus("current")


class _FsMIEcfmMepCciEnabled_Type(TruthValue):
    """Custom type fsMIEcfmMepCciEnabled based on TruthValue"""
    defaultValue = 2


_FsMIEcfmMepCciEnabled_Type.__name__ = "TruthValue"
_FsMIEcfmMepCciEnabled_Object = MibTableColumn
fsMIEcfmMepCciEnabled = _FsMIEcfmMepCciEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 7),
    _FsMIEcfmMepCciEnabled_Type()
)
fsMIEcfmMepCciEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepCciEnabled.setStatus("current")


class _FsMIEcfmMepCcmLtmPriority_Type(Unsigned32):
    """Custom type fsMIEcfmMepCcmLtmPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMIEcfmMepCcmLtmPriority_Type.__name__ = "Unsigned32"
_FsMIEcfmMepCcmLtmPriority_Object = MibTableColumn
fsMIEcfmMepCcmLtmPriority = _FsMIEcfmMepCcmLtmPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 8),
    _FsMIEcfmMepCcmLtmPriority_Type()
)
fsMIEcfmMepCcmLtmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepCcmLtmPriority.setStatus("current")
_FsMIEcfmMepMacAddress_Type = MacAddress
_FsMIEcfmMepMacAddress_Object = MibTableColumn
fsMIEcfmMepMacAddress = _FsMIEcfmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 9),
    _FsMIEcfmMepMacAddress_Type()
)
fsMIEcfmMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepMacAddress.setStatus("current")


class _FsMIEcfmMepLowPrDef_Type(FsMIEcfmLowestAlarmPri):
    """Custom type fsMIEcfmMepLowPrDef based on FsMIEcfmLowestAlarmPri"""
    defaultValue = 2


_FsMIEcfmMepLowPrDef_Type.__name__ = "FsMIEcfmLowestAlarmPri"
_FsMIEcfmMepLowPrDef_Object = MibTableColumn
fsMIEcfmMepLowPrDef = _FsMIEcfmMepLowPrDef_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 10),
    _FsMIEcfmMepLowPrDef_Type()
)
fsMIEcfmMepLowPrDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepLowPrDef.setStatus("current")


class _FsMIEcfmMepFngAlarmTime_Type(TimeInterval):
    """Custom type fsMIEcfmMepFngAlarmTime based on TimeInterval"""
    defaultValue = 250

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1000),
    )


_FsMIEcfmMepFngAlarmTime_Type.__name__ = "TimeInterval"
_FsMIEcfmMepFngAlarmTime_Object = MibTableColumn
fsMIEcfmMepFngAlarmTime = _FsMIEcfmMepFngAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 11),
    _FsMIEcfmMepFngAlarmTime_Type()
)
fsMIEcfmMepFngAlarmTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepFngAlarmTime.setStatus("current")


class _FsMIEcfmMepFngResetTime_Type(TimeInterval):
    """Custom type fsMIEcfmMepFngResetTime based on TimeInterval"""
    defaultValue = 1000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1000),
    )


_FsMIEcfmMepFngResetTime_Type.__name__ = "TimeInterval"
_FsMIEcfmMepFngResetTime_Object = MibTableColumn
fsMIEcfmMepFngResetTime = _FsMIEcfmMepFngResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 12),
    _FsMIEcfmMepFngResetTime_Type()
)
fsMIEcfmMepFngResetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepFngResetTime.setStatus("current")
_FsMIEcfmMepHighestPrDefect_Type = FsMIEcfmHighestDefectPri
_FsMIEcfmMepHighestPrDefect_Object = MibTableColumn
fsMIEcfmMepHighestPrDefect = _FsMIEcfmMepHighestPrDefect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 13),
    _FsMIEcfmMepHighestPrDefect_Type()
)
fsMIEcfmMepHighestPrDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepHighestPrDefect.setStatus("current")
_FsMIEcfmMepDefects_Type = FsMIEcfmMepDefects
_FsMIEcfmMepDefects_Object = MibTableColumn
fsMIEcfmMepDefects = _FsMIEcfmMepDefects_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 14),
    _FsMIEcfmMepDefects_Type()
)
fsMIEcfmMepDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDefects.setStatus("current")


class _FsMIEcfmMepErrorCcmLastFailure_Type(OctetString):
    """Custom type fsMIEcfmMepErrorCcmLastFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1522),
    )


_FsMIEcfmMepErrorCcmLastFailure_Type.__name__ = "OctetString"
_FsMIEcfmMepErrorCcmLastFailure_Object = MibTableColumn
fsMIEcfmMepErrorCcmLastFailure = _FsMIEcfmMepErrorCcmLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 15),
    _FsMIEcfmMepErrorCcmLastFailure_Type()
)
fsMIEcfmMepErrorCcmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepErrorCcmLastFailure.setStatus("current")


class _FsMIEcfmMepXconCcmLastFailure_Type(OctetString):
    """Custom type fsMIEcfmMepXconCcmLastFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1522),
    )


_FsMIEcfmMepXconCcmLastFailure_Type.__name__ = "OctetString"
_FsMIEcfmMepXconCcmLastFailure_Object = MibTableColumn
fsMIEcfmMepXconCcmLastFailure = _FsMIEcfmMepXconCcmLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 16),
    _FsMIEcfmMepXconCcmLastFailure_Type()
)
fsMIEcfmMepXconCcmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepXconCcmLastFailure.setStatus("current")
_FsMIEcfmMepCcmSequenceErrors_Type = Unsigned32
_FsMIEcfmMepCcmSequenceErrors_Object = MibTableColumn
fsMIEcfmMepCcmSequenceErrors = _FsMIEcfmMepCcmSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 17),
    _FsMIEcfmMepCcmSequenceErrors_Type()
)
fsMIEcfmMepCcmSequenceErrors.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepCcmSequenceErrors.setStatus("current")
_FsMIEcfmMepCciSentCcms_Type = Unsigned32
_FsMIEcfmMepCciSentCcms_Object = MibTableColumn
fsMIEcfmMepCciSentCcms = _FsMIEcfmMepCciSentCcms_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 18),
    _FsMIEcfmMepCciSentCcms_Type()
)
fsMIEcfmMepCciSentCcms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepCciSentCcms.setStatus("current")
_FsMIEcfmMepNextLbmTransId_Type = Unsigned32
_FsMIEcfmMepNextLbmTransId_Object = MibTableColumn
fsMIEcfmMepNextLbmTransId = _FsMIEcfmMepNextLbmTransId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 19),
    _FsMIEcfmMepNextLbmTransId_Type()
)
fsMIEcfmMepNextLbmTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepNextLbmTransId.setStatus("current")
_FsMIEcfmMepLbrIn_Type = Unsigned32
_FsMIEcfmMepLbrIn_Object = MibTableColumn
fsMIEcfmMepLbrIn = _FsMIEcfmMepLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 20),
    _FsMIEcfmMepLbrIn_Type()
)
fsMIEcfmMepLbrIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepLbrIn.setStatus("current")
_FsMIEcfmMepLbrInOutOfOrder_Type = Unsigned32
_FsMIEcfmMepLbrInOutOfOrder_Object = MibTableColumn
fsMIEcfmMepLbrInOutOfOrder = _FsMIEcfmMepLbrInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 21),
    _FsMIEcfmMepLbrInOutOfOrder_Type()
)
fsMIEcfmMepLbrInOutOfOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepLbrInOutOfOrder.setStatus("current")
_FsMIEcfmMepLbrBadMsdu_Type = Unsigned32
_FsMIEcfmMepLbrBadMsdu_Object = MibTableColumn
fsMIEcfmMepLbrBadMsdu = _FsMIEcfmMepLbrBadMsdu_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 22),
    _FsMIEcfmMepLbrBadMsdu_Type()
)
fsMIEcfmMepLbrBadMsdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepLbrBadMsdu.setStatus("current")
_FsMIEcfmMepLtmNextSeqNumber_Type = Unsigned32
_FsMIEcfmMepLtmNextSeqNumber_Object = MibTableColumn
fsMIEcfmMepLtmNextSeqNumber = _FsMIEcfmMepLtmNextSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 23),
    _FsMIEcfmMepLtmNextSeqNumber_Type()
)
fsMIEcfmMepLtmNextSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepLtmNextSeqNumber.setStatus("current")
_FsMIEcfmMepUnexpLtrIn_Type = Unsigned32
_FsMIEcfmMepUnexpLtrIn_Object = MibTableColumn
fsMIEcfmMepUnexpLtrIn = _FsMIEcfmMepUnexpLtrIn_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 24),
    _FsMIEcfmMepUnexpLtrIn_Type()
)
fsMIEcfmMepUnexpLtrIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepUnexpLtrIn.setStatus("current")
_FsMIEcfmMepLbrOut_Type = Unsigned32
_FsMIEcfmMepLbrOut_Object = MibTableColumn
fsMIEcfmMepLbrOut = _FsMIEcfmMepLbrOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 25),
    _FsMIEcfmMepLbrOut_Type()
)
fsMIEcfmMepLbrOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepLbrOut.setStatus("current")


class _FsMIEcfmMepTransmitLbmStatus_Type(FsMIEcfmTransmitStatus):
    """Custom type fsMIEcfmMepTransmitLbmStatus based on FsMIEcfmTransmitStatus"""
    defaultValue = 0


_FsMIEcfmMepTransmitLbmStatus_Type.__name__ = "FsMIEcfmTransmitStatus"
_FsMIEcfmMepTransmitLbmStatus_Object = MibTableColumn
fsMIEcfmMepTransmitLbmStatus = _FsMIEcfmMepTransmitLbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 26),
    _FsMIEcfmMepTransmitLbmStatus_Type()
)
fsMIEcfmMepTransmitLbmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmStatus.setStatus("current")
_FsMIEcfmMepTransmitLbmDestMacAddress_Type = MacAddress
_FsMIEcfmMepTransmitLbmDestMacAddress_Object = MibTableColumn
fsMIEcfmMepTransmitLbmDestMacAddress = _FsMIEcfmMepTransmitLbmDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 27),
    _FsMIEcfmMepTransmitLbmDestMacAddress_Type()
)
fsMIEcfmMepTransmitLbmDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmDestMacAddress.setStatus("current")
_FsMIEcfmMepTransmitLbmDestMepId_Type = FsMIEcfmMepIdOrZero
_FsMIEcfmMepTransmitLbmDestMepId_Object = MibTableColumn
fsMIEcfmMepTransmitLbmDestMepId = _FsMIEcfmMepTransmitLbmDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 28),
    _FsMIEcfmMepTransmitLbmDestMepId_Type()
)
fsMIEcfmMepTransmitLbmDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmDestMepId.setStatus("current")
_FsMIEcfmMepTransmitLbmDestIsMepId_Type = TruthValue
_FsMIEcfmMepTransmitLbmDestIsMepId_Object = MibTableColumn
fsMIEcfmMepTransmitLbmDestIsMepId = _FsMIEcfmMepTransmitLbmDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 29),
    _FsMIEcfmMepTransmitLbmDestIsMepId_Type()
)
fsMIEcfmMepTransmitLbmDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmDestIsMepId.setStatus("current")


class _FsMIEcfmMepTransmitLbmMessages_Type(Integer32):
    """Custom type fsMIEcfmMepTransmitLbmMessages based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsMIEcfmMepTransmitLbmMessages_Type.__name__ = "Integer32"
_FsMIEcfmMepTransmitLbmMessages_Object = MibTableColumn
fsMIEcfmMepTransmitLbmMessages = _FsMIEcfmMepTransmitLbmMessages_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 30),
    _FsMIEcfmMepTransmitLbmMessages_Type()
)
fsMIEcfmMepTransmitLbmMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmMessages.setStatus("current")


class _FsMIEcfmMepTransmitLbmDataTlv_Type(OctetString):
    """Custom type fsMIEcfmMepTransmitLbmDataTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_FsMIEcfmMepTransmitLbmDataTlv_Type.__name__ = "OctetString"
_FsMIEcfmMepTransmitLbmDataTlv_Object = MibTableColumn
fsMIEcfmMepTransmitLbmDataTlv = _FsMIEcfmMepTransmitLbmDataTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 31),
    _FsMIEcfmMepTransmitLbmDataTlv_Type()
)
fsMIEcfmMepTransmitLbmDataTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmDataTlv.setStatus("current")


class _FsMIEcfmMepTransmitLbmVlanPriority_Type(Integer32):
    """Custom type fsMIEcfmMepTransmitLbmVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMIEcfmMepTransmitLbmVlanPriority_Type.__name__ = "Integer32"
_FsMIEcfmMepTransmitLbmVlanPriority_Object = MibTableColumn
fsMIEcfmMepTransmitLbmVlanPriority = _FsMIEcfmMepTransmitLbmVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 32),
    _FsMIEcfmMepTransmitLbmVlanPriority_Type()
)
fsMIEcfmMepTransmitLbmVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmVlanPriority.setStatus("current")


class _FsMIEcfmMepTransmitLbmVlanDropEnable_Type(TruthValue):
    """Custom type fsMIEcfmMepTransmitLbmVlanDropEnable based on TruthValue"""
    defaultValue = 1


_FsMIEcfmMepTransmitLbmVlanDropEnable_Type.__name__ = "TruthValue"
_FsMIEcfmMepTransmitLbmVlanDropEnable_Object = MibTableColumn
fsMIEcfmMepTransmitLbmVlanDropEnable = _FsMIEcfmMepTransmitLbmVlanDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 33),
    _FsMIEcfmMepTransmitLbmVlanDropEnable_Type()
)
fsMIEcfmMepTransmitLbmVlanDropEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmVlanDropEnable.setStatus("current")


class _FsMIEcfmMepTransmitLbmResultOK_Type(TruthValue):
    """Custom type fsMIEcfmMepTransmitLbmResultOK based on TruthValue"""
    defaultValue = 1


_FsMIEcfmMepTransmitLbmResultOK_Type.__name__ = "TruthValue"
_FsMIEcfmMepTransmitLbmResultOK_Object = MibTableColumn
fsMIEcfmMepTransmitLbmResultOK = _FsMIEcfmMepTransmitLbmResultOK_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 34),
    _FsMIEcfmMepTransmitLbmResultOK_Type()
)
fsMIEcfmMepTransmitLbmResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmResultOK.setStatus("current")
_FsMIEcfmMepTransmitLbmSeqNumber_Type = Unsigned32
_FsMIEcfmMepTransmitLbmSeqNumber_Object = MibTableColumn
fsMIEcfmMepTransmitLbmSeqNumber = _FsMIEcfmMepTransmitLbmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 35),
    _FsMIEcfmMepTransmitLbmSeqNumber_Type()
)
fsMIEcfmMepTransmitLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLbmSeqNumber.setStatus("current")


class _FsMIEcfmMepTransmitLtmStatus_Type(FsMIEcfmTransmitStatus):
    """Custom type fsMIEcfmMepTransmitLtmStatus based on FsMIEcfmTransmitStatus"""
    defaultValue = 0


_FsMIEcfmMepTransmitLtmStatus_Type.__name__ = "FsMIEcfmTransmitStatus"
_FsMIEcfmMepTransmitLtmStatus_Object = MibTableColumn
fsMIEcfmMepTransmitLtmStatus = _FsMIEcfmMepTransmitLtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 36),
    _FsMIEcfmMepTransmitLtmStatus_Type()
)
fsMIEcfmMepTransmitLtmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLtmStatus.setStatus("current")


class _FsMIEcfmMepTransmitLtmFlags_Type(Bits):
    """Custom type fsMIEcfmMepTransmitLtmFlags based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        ("useFDBonly", 0)
    )

_FsMIEcfmMepTransmitLtmFlags_Type.__name__ = "Bits"
_FsMIEcfmMepTransmitLtmFlags_Object = MibTableColumn
fsMIEcfmMepTransmitLtmFlags = _FsMIEcfmMepTransmitLtmFlags_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 37),
    _FsMIEcfmMepTransmitLtmFlags_Type()
)
fsMIEcfmMepTransmitLtmFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLtmFlags.setStatus("current")
_FsMIEcfmMepTransmitLtmTargetMacAddress_Type = MacAddress
_FsMIEcfmMepTransmitLtmTargetMacAddress_Object = MibTableColumn
fsMIEcfmMepTransmitLtmTargetMacAddress = _FsMIEcfmMepTransmitLtmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 38),
    _FsMIEcfmMepTransmitLtmTargetMacAddress_Type()
)
fsMIEcfmMepTransmitLtmTargetMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLtmTargetMacAddress.setStatus("current")
_FsMIEcfmMepTransmitLtmTargetMepId_Type = FsMIEcfmMepIdOrZero
_FsMIEcfmMepTransmitLtmTargetMepId_Object = MibTableColumn
fsMIEcfmMepTransmitLtmTargetMepId = _FsMIEcfmMepTransmitLtmTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 39),
    _FsMIEcfmMepTransmitLtmTargetMepId_Type()
)
fsMIEcfmMepTransmitLtmTargetMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLtmTargetMepId.setStatus("current")
_FsMIEcfmMepTransmitLtmTargetIsMepId_Type = TruthValue
_FsMIEcfmMepTransmitLtmTargetIsMepId_Object = MibTableColumn
fsMIEcfmMepTransmitLtmTargetIsMepId = _FsMIEcfmMepTransmitLtmTargetIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 40),
    _FsMIEcfmMepTransmitLtmTargetIsMepId_Type()
)
fsMIEcfmMepTransmitLtmTargetIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLtmTargetIsMepId.setStatus("current")


class _FsMIEcfmMepTransmitLtmTtl_Type(Unsigned32):
    """Custom type fsMIEcfmMepTransmitLtmTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIEcfmMepTransmitLtmTtl_Type.__name__ = "Unsigned32"
_FsMIEcfmMepTransmitLtmTtl_Object = MibTableColumn
fsMIEcfmMepTransmitLtmTtl = _FsMIEcfmMepTransmitLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 41),
    _FsMIEcfmMepTransmitLtmTtl_Type()
)
fsMIEcfmMepTransmitLtmTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLtmTtl.setStatus("current")


class _FsMIEcfmMepTransmitLtmResult_Type(TruthValue):
    """Custom type fsMIEcfmMepTransmitLtmResult based on TruthValue"""
    defaultValue = 1


_FsMIEcfmMepTransmitLtmResult_Type.__name__ = "TruthValue"
_FsMIEcfmMepTransmitLtmResult_Object = MibTableColumn
fsMIEcfmMepTransmitLtmResult = _FsMIEcfmMepTransmitLtmResult_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 42),
    _FsMIEcfmMepTransmitLtmResult_Type()
)
fsMIEcfmMepTransmitLtmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLtmResult.setStatus("current")
_FsMIEcfmMepTransmitLtmSeqNumber_Type = Unsigned32
_FsMIEcfmMepTransmitLtmSeqNumber_Object = MibTableColumn
fsMIEcfmMepTransmitLtmSeqNumber = _FsMIEcfmMepTransmitLtmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 43),
    _FsMIEcfmMepTransmitLtmSeqNumber_Type()
)
fsMIEcfmMepTransmitLtmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLtmSeqNumber.setStatus("current")


class _FsMIEcfmMepTransmitLtmEgressIdentifier_Type(OctetString):
    """Custom type fsMIEcfmMepTransmitLtmEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsMIEcfmMepTransmitLtmEgressIdentifier_Type.__name__ = "OctetString"
_FsMIEcfmMepTransmitLtmEgressIdentifier_Object = MibTableColumn
fsMIEcfmMepTransmitLtmEgressIdentifier = _FsMIEcfmMepTransmitLtmEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 44),
    _FsMIEcfmMepTransmitLtmEgressIdentifier_Type()
)
fsMIEcfmMepTransmitLtmEgressIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepTransmitLtmEgressIdentifier.setStatus("current")
_FsMIEcfmMepRowStatus_Type = RowStatus
_FsMIEcfmMepRowStatus_Object = MibTableColumn
fsMIEcfmMepRowStatus = _FsMIEcfmMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 45),
    _FsMIEcfmMepRowStatus_Type()
)
fsMIEcfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepRowStatus.setStatus("current")


class _FsMIEcfmMepCcmOffload_Type(Integer32):
    """Custom type fsMIEcfmMepCcmOffload based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIEcfmMepCcmOffload_Type.__name__ = "Integer32"
_FsMIEcfmMepCcmOffload_Object = MibTableColumn
fsMIEcfmMepCcmOffload = _FsMIEcfmMepCcmOffload_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 7, 1, 46),
    _FsMIEcfmMepCcmOffload_Type()
)
fsMIEcfmMepCcmOffload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMepCcmOffload.setStatus("current")
_FsMIEcfmLtrTable_Object = MibTable
fsMIEcfmLtrTable = _FsMIEcfmLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8)
)
if mibBuilder.loadTexts:
    fsMIEcfmLtrTable.setStatus("current")
_FsMIEcfmLtrEntry_Object = MibTableRow
fsMIEcfmLtrEntry = _FsMIEcfmLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1)
)
fsMIEcfmLtrEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMepIdentifier"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmLtrSeqNumber"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmLtrReceiveOrder"),
)
if mibBuilder.loadTexts:
    fsMIEcfmLtrEntry.setStatus("current")


class _FsMIEcfmLtrSeqNumber_Type(Unsigned32):
    """Custom type fsMIEcfmLtrSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIEcfmLtrSeqNumber_Type.__name__ = "Unsigned32"
_FsMIEcfmLtrSeqNumber_Object = MibTableColumn
fsMIEcfmLtrSeqNumber = _FsMIEcfmLtrSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 1),
    _FsMIEcfmLtrSeqNumber_Type()
)
fsMIEcfmLtrSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmLtrSeqNumber.setStatus("current")


class _FsMIEcfmLtrReceiveOrder_Type(Unsigned32):
    """Custom type fsMIEcfmLtrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMIEcfmLtrReceiveOrder_Type.__name__ = "Unsigned32"
_FsMIEcfmLtrReceiveOrder_Object = MibTableColumn
fsMIEcfmLtrReceiveOrder = _FsMIEcfmLtrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 2),
    _FsMIEcfmLtrReceiveOrder_Type()
)
fsMIEcfmLtrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmLtrReceiveOrder.setStatus("current")


class _FsMIEcfmLtrTtl_Type(Unsigned32):
    """Custom type fsMIEcfmLtrTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIEcfmLtrTtl_Type.__name__ = "Unsigned32"
_FsMIEcfmLtrTtl_Object = MibTableColumn
fsMIEcfmLtrTtl = _FsMIEcfmLtrTtl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 3),
    _FsMIEcfmLtrTtl_Type()
)
fsMIEcfmLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrTtl.setStatus("current")
_FsMIEcfmLtrForwarded_Type = TruthValue
_FsMIEcfmLtrForwarded_Object = MibTableColumn
fsMIEcfmLtrForwarded = _FsMIEcfmLtrForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 4),
    _FsMIEcfmLtrForwarded_Type()
)
fsMIEcfmLtrForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrForwarded.setStatus("current")
_FsMIEcfmLtrTerminalMep_Type = TruthValue
_FsMIEcfmLtrTerminalMep_Object = MibTableColumn
fsMIEcfmLtrTerminalMep = _FsMIEcfmLtrTerminalMep_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 5),
    _FsMIEcfmLtrTerminalMep_Type()
)
fsMIEcfmLtrTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrTerminalMep.setStatus("current")


class _FsMIEcfmLtrLastEgressIdentifier_Type(OctetString):
    """Custom type fsMIEcfmLtrLastEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsMIEcfmLtrLastEgressIdentifier_Type.__name__ = "OctetString"
_FsMIEcfmLtrLastEgressIdentifier_Object = MibTableColumn
fsMIEcfmLtrLastEgressIdentifier = _FsMIEcfmLtrLastEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 6),
    _FsMIEcfmLtrLastEgressIdentifier_Type()
)
fsMIEcfmLtrLastEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrLastEgressIdentifier.setStatus("current")


class _FsMIEcfmLtrNextEgressIdentifier_Type(OctetString):
    """Custom type fsMIEcfmLtrNextEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsMIEcfmLtrNextEgressIdentifier_Type.__name__ = "OctetString"
_FsMIEcfmLtrNextEgressIdentifier_Object = MibTableColumn
fsMIEcfmLtrNextEgressIdentifier = _FsMIEcfmLtrNextEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 7),
    _FsMIEcfmLtrNextEgressIdentifier_Type()
)
fsMIEcfmLtrNextEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrNextEgressIdentifier.setStatus("current")
_FsMIEcfmLtrRelay_Type = FsMIEcfmRelayActionFieldValue
_FsMIEcfmLtrRelay_Object = MibTableColumn
fsMIEcfmLtrRelay = _FsMIEcfmLtrRelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 8),
    _FsMIEcfmLtrRelay_Type()
)
fsMIEcfmLtrRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrRelay.setStatus("current")
_FsMIEcfmLtrChassisIdSubtype_Type = LldpChassisIdSubtype
_FsMIEcfmLtrChassisIdSubtype_Object = MibTableColumn
fsMIEcfmLtrChassisIdSubtype = _FsMIEcfmLtrChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 9),
    _FsMIEcfmLtrChassisIdSubtype_Type()
)
fsMIEcfmLtrChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrChassisIdSubtype.setStatus("current")
_FsMIEcfmLtrChassisId_Type = LldpChassisId
_FsMIEcfmLtrChassisId_Object = MibTableColumn
fsMIEcfmLtrChassisId = _FsMIEcfmLtrChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 10),
    _FsMIEcfmLtrChassisId_Type()
)
fsMIEcfmLtrChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrChassisId.setStatus("current")
_FsMIEcfmLtrManAddressDomain_Type = TDomain
_FsMIEcfmLtrManAddressDomain_Object = MibTableColumn
fsMIEcfmLtrManAddressDomain = _FsMIEcfmLtrManAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 11),
    _FsMIEcfmLtrManAddressDomain_Type()
)
fsMIEcfmLtrManAddressDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrManAddressDomain.setStatus("current")
_FsMIEcfmLtrManAddress_Type = TAddress
_FsMIEcfmLtrManAddress_Object = MibTableColumn
fsMIEcfmLtrManAddress = _FsMIEcfmLtrManAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 12),
    _FsMIEcfmLtrManAddress_Type()
)
fsMIEcfmLtrManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrManAddress.setStatus("current")
_FsMIEcfmLtrIngress_Type = FsMIEcfmIngressActionFieldValue
_FsMIEcfmLtrIngress_Object = MibTableColumn
fsMIEcfmLtrIngress = _FsMIEcfmLtrIngress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 13),
    _FsMIEcfmLtrIngress_Type()
)
fsMIEcfmLtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrIngress.setStatus("current")
_FsMIEcfmLtrIngressMac_Type = MacAddress
_FsMIEcfmLtrIngressMac_Object = MibTableColumn
fsMIEcfmLtrIngressMac = _FsMIEcfmLtrIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 14),
    _FsMIEcfmLtrIngressMac_Type()
)
fsMIEcfmLtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrIngressMac.setStatus("current")
_FsMIEcfmLtrIngressPortIdSubtype_Type = LldpPortIdSubtype
_FsMIEcfmLtrIngressPortIdSubtype_Object = MibTableColumn
fsMIEcfmLtrIngressPortIdSubtype = _FsMIEcfmLtrIngressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 15),
    _FsMIEcfmLtrIngressPortIdSubtype_Type()
)
fsMIEcfmLtrIngressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrIngressPortIdSubtype.setStatus("current")
_FsMIEcfmLtrIngressPortId_Type = LldpPortId
_FsMIEcfmLtrIngressPortId_Object = MibTableColumn
fsMIEcfmLtrIngressPortId = _FsMIEcfmLtrIngressPortId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 16),
    _FsMIEcfmLtrIngressPortId_Type()
)
fsMIEcfmLtrIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrIngressPortId.setStatus("current")
_FsMIEcfmLtrEgress_Type = FsMIEcfmEgressActionFieldValue
_FsMIEcfmLtrEgress_Object = MibTableColumn
fsMIEcfmLtrEgress = _FsMIEcfmLtrEgress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 17),
    _FsMIEcfmLtrEgress_Type()
)
fsMIEcfmLtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrEgress.setStatus("current")
_FsMIEcfmLtrEgressMac_Type = MacAddress
_FsMIEcfmLtrEgressMac_Object = MibTableColumn
fsMIEcfmLtrEgressMac = _FsMIEcfmLtrEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 18),
    _FsMIEcfmLtrEgressMac_Type()
)
fsMIEcfmLtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrEgressMac.setStatus("current")
_FsMIEcfmLtrEgressPortIdSubtype_Type = LldpPortIdSubtype
_FsMIEcfmLtrEgressPortIdSubtype_Object = MibTableColumn
fsMIEcfmLtrEgressPortIdSubtype = _FsMIEcfmLtrEgressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 19),
    _FsMIEcfmLtrEgressPortIdSubtype_Type()
)
fsMIEcfmLtrEgressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrEgressPortIdSubtype.setStatus("current")
_FsMIEcfmLtrEgressPortId_Type = LldpPortId
_FsMIEcfmLtrEgressPortId_Object = MibTableColumn
fsMIEcfmLtrEgressPortId = _FsMIEcfmLtrEgressPortId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 20),
    _FsMIEcfmLtrEgressPortId_Type()
)
fsMIEcfmLtrEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrEgressPortId.setStatus("current")


class _FsMIEcfmLtrOrganizationSpecificTlv_Type(OctetString):
    """Custom type fsMIEcfmLtrOrganizationSpecificTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 1500),
    )


_FsMIEcfmLtrOrganizationSpecificTlv_Type.__name__ = "OctetString"
_FsMIEcfmLtrOrganizationSpecificTlv_Object = MibTableColumn
fsMIEcfmLtrOrganizationSpecificTlv = _FsMIEcfmLtrOrganizationSpecificTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 8, 1, 21),
    _FsMIEcfmLtrOrganizationSpecificTlv_Type()
)
fsMIEcfmLtrOrganizationSpecificTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtrOrganizationSpecificTlv.setStatus("current")
_FsMIEcfmMepDbTable_Object = MibTable
fsMIEcfmMepDbTable = _FsMIEcfmMepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9)
)
if mibBuilder.loadTexts:
    fsMIEcfmMepDbTable.setStatus("current")
_FsMIEcfmMepDbEntry_Object = MibTableRow
fsMIEcfmMepDbEntry = _FsMIEcfmMepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1)
)
fsMIEcfmMepDbEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMepIdentifier"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMepDbEntry.setStatus("current")
_FsMIEcfmMepDbRMepIdentifier_Type = FsMIEcfmMepId
_FsMIEcfmMepDbRMepIdentifier_Object = MibTableColumn
fsMIEcfmMepDbRMepIdentifier = _FsMIEcfmMepDbRMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 1),
    _FsMIEcfmMepDbRMepIdentifier_Type()
)
fsMIEcfmMepDbRMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbRMepIdentifier.setStatus("current")
_FsMIEcfmMepDbRMepState_Type = FsMIEcfmRemoteMepState
_FsMIEcfmMepDbRMepState_Object = MibTableColumn
fsMIEcfmMepDbRMepState = _FsMIEcfmMepDbRMepState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 2),
    _FsMIEcfmMepDbRMepState_Type()
)
fsMIEcfmMepDbRMepState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbRMepState.setStatus("current")
_FsMIEcfmMepDbRMepFailedOkTime_Type = TimeStamp
_FsMIEcfmMepDbRMepFailedOkTime_Object = MibTableColumn
fsMIEcfmMepDbRMepFailedOkTime = _FsMIEcfmMepDbRMepFailedOkTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 3),
    _FsMIEcfmMepDbRMepFailedOkTime_Type()
)
fsMIEcfmMepDbRMepFailedOkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbRMepFailedOkTime.setStatus("current")
_FsMIEcfmMepDbMacAddress_Type = MacAddress
_FsMIEcfmMepDbMacAddress_Object = MibTableColumn
fsMIEcfmMepDbMacAddress = _FsMIEcfmMepDbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 4),
    _FsMIEcfmMepDbMacAddress_Type()
)
fsMIEcfmMepDbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbMacAddress.setStatus("current")
_FsMIEcfmMepDbRdi_Type = TruthValue
_FsMIEcfmMepDbRdi_Object = MibTableColumn
fsMIEcfmMepDbRdi = _FsMIEcfmMepDbRdi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 5),
    _FsMIEcfmMepDbRdi_Type()
)
fsMIEcfmMepDbRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbRdi.setStatus("current")


class _FsMIEcfmMepDbPortStatusTlv_Type(FsMIEcfmPortStatus):
    """Custom type fsMIEcfmMepDbPortStatusTlv based on FsMIEcfmPortStatus"""
    defaultValue = 0


_FsMIEcfmMepDbPortStatusTlv_Type.__name__ = "FsMIEcfmPortStatus"
_FsMIEcfmMepDbPortStatusTlv_Object = MibTableColumn
fsMIEcfmMepDbPortStatusTlv = _FsMIEcfmMepDbPortStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 6),
    _FsMIEcfmMepDbPortStatusTlv_Type()
)
fsMIEcfmMepDbPortStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbPortStatusTlv.setStatus("current")


class _FsMIEcfmMepDbInterfaceStatusTlv_Type(FsMIEcfmInterfaceStatus):
    """Custom type fsMIEcfmMepDbInterfaceStatusTlv based on FsMIEcfmInterfaceStatus"""
    defaultValue = 0


_FsMIEcfmMepDbInterfaceStatusTlv_Type.__name__ = "FsMIEcfmInterfaceStatus"
_FsMIEcfmMepDbInterfaceStatusTlv_Object = MibTableColumn
fsMIEcfmMepDbInterfaceStatusTlv = _FsMIEcfmMepDbInterfaceStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 7),
    _FsMIEcfmMepDbInterfaceStatusTlv_Type()
)
fsMIEcfmMepDbInterfaceStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbInterfaceStatusTlv.setStatus("current")


class _FsMIEcfmMepDbChassisIdSubtype_Type(LldpChassisIdSubtype):
    """Custom type fsMIEcfmMepDbChassisIdSubtype based on LldpChassisIdSubtype"""
    defaultValue = 4


_FsMIEcfmMepDbChassisIdSubtype_Type.__name__ = "LldpChassisIdSubtype"
_FsMIEcfmMepDbChassisIdSubtype_Object = MibTableColumn
fsMIEcfmMepDbChassisIdSubtype = _FsMIEcfmMepDbChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 8),
    _FsMIEcfmMepDbChassisIdSubtype_Type()
)
fsMIEcfmMepDbChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbChassisIdSubtype.setStatus("current")
_FsMIEcfmMepDbChassisId_Type = LldpChassisId
_FsMIEcfmMepDbChassisId_Object = MibTableColumn
fsMIEcfmMepDbChassisId = _FsMIEcfmMepDbChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 9),
    _FsMIEcfmMepDbChassisId_Type()
)
fsMIEcfmMepDbChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbChassisId.setStatus("current")
_FsMIEcfmMepDbManAddressDomain_Type = TDomain
_FsMIEcfmMepDbManAddressDomain_Object = MibTableColumn
fsMIEcfmMepDbManAddressDomain = _FsMIEcfmMepDbManAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 10),
    _FsMIEcfmMepDbManAddressDomain_Type()
)
fsMIEcfmMepDbManAddressDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbManAddressDomain.setStatus("current")
_FsMIEcfmMepDbManAddress_Type = TAddress
_FsMIEcfmMepDbManAddress_Object = MibTableColumn
fsMIEcfmMepDbManAddress = _FsMIEcfmMepDbManAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 9, 1, 11),
    _FsMIEcfmMepDbManAddress_Type()
)
fsMIEcfmMepDbManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMepDbManAddress.setStatus("current")
_FsMIEcfmMipCcmDbTable_Object = MibTable
fsMIEcfmMipCcmDbTable = _FsMIEcfmMipCcmDbTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 10)
)
if mibBuilder.loadTexts:
    fsMIEcfmMipCcmDbTable.setStatus("current")
_FsMIEcfmMipCcmDbEntry_Object = MibTableRow
fsMIEcfmMipCcmDbEntry = _FsMIEcfmMipCcmDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 10, 1)
)
fsMIEcfmMipCcmDbEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMipCcmFid"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMipCcmSrcAddr"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMipCcmDbEntry.setStatus("current")


class _FsMIEcfmMipCcmFid_Type(Unsigned32):
    """Custom type fsMIEcfmMipCcmFid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIEcfmMipCcmFid_Type.__name__ = "Unsigned32"
_FsMIEcfmMipCcmFid_Object = MibTableColumn
fsMIEcfmMipCcmFid = _FsMIEcfmMipCcmFid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 10, 1, 1),
    _FsMIEcfmMipCcmFid_Type()
)
fsMIEcfmMipCcmFid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMipCcmFid.setStatus("current")
_FsMIEcfmMipCcmSrcAddr_Type = MacAddress
_FsMIEcfmMipCcmSrcAddr_Object = MibTableColumn
fsMIEcfmMipCcmSrcAddr = _FsMIEcfmMipCcmSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 10, 1, 2),
    _FsMIEcfmMipCcmSrcAddr_Type()
)
fsMIEcfmMipCcmSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMipCcmSrcAddr.setStatus("current")
_FsMIEcfmMipCcmIfIndex_Type = InterfaceIndex
_FsMIEcfmMipCcmIfIndex_Object = MibTableColumn
fsMIEcfmMipCcmIfIndex = _FsMIEcfmMipCcmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 10, 1, 3),
    _FsMIEcfmMipCcmIfIndex_Type()
)
fsMIEcfmMipCcmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmMipCcmIfIndex.setStatus("current")
_FsMIEcfmRemoteMepDbExTable_Object = MibTable
fsMIEcfmRemoteMepDbExTable = _FsMIEcfmRemoteMepDbExTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11)
)
if mibBuilder.loadTexts:
    fsMIEcfmRemoteMepDbExTable.setStatus("current")
_FsMIEcfmRemoteMepDbExEntry_Object = MibTableRow
fsMIEcfmRemoteMepDbExEntry = _FsMIEcfmRemoteMepDbExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1)
)
fsMIEcfmRemoteMepDbExEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMepIdentifier"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    fsMIEcfmRemoteMepDbExEntry.setStatus("current")
_FsMIEcfmRMepCcmSequenceNum_Type = Unsigned32
_FsMIEcfmRMepCcmSequenceNum_Object = MibTableColumn
fsMIEcfmRMepCcmSequenceNum = _FsMIEcfmRMepCcmSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 1),
    _FsMIEcfmRMepCcmSequenceNum_Type()
)
fsMIEcfmRMepCcmSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmRMepCcmSequenceNum.setStatus("current")
_FsMIEcfmRMepPortStatusDefect_Type = TruthValue
_FsMIEcfmRMepPortStatusDefect_Object = MibTableColumn
fsMIEcfmRMepPortStatusDefect = _FsMIEcfmRMepPortStatusDefect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 2),
    _FsMIEcfmRMepPortStatusDefect_Type()
)
fsMIEcfmRMepPortStatusDefect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepPortStatusDefect.setStatus("current")
_FsMIEcfmRMepInterfaceStatusDefect_Type = TruthValue
_FsMIEcfmRMepInterfaceStatusDefect_Object = MibTableColumn
fsMIEcfmRMepInterfaceStatusDefect = _FsMIEcfmRMepInterfaceStatusDefect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 3),
    _FsMIEcfmRMepInterfaceStatusDefect_Type()
)
fsMIEcfmRMepInterfaceStatusDefect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepInterfaceStatusDefect.setStatus("current")
_FsMIEcfmRMepCcmDefect_Type = TruthValue
_FsMIEcfmRMepCcmDefect_Object = MibTableColumn
fsMIEcfmRMepCcmDefect = _FsMIEcfmRMepCcmDefect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 4),
    _FsMIEcfmRMepCcmDefect_Type()
)
fsMIEcfmRMepCcmDefect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepCcmDefect.setStatus("current")
_FsMIEcfmRMepRDIDefect_Type = TruthValue
_FsMIEcfmRMepRDIDefect_Object = MibTableColumn
fsMIEcfmRMepRDIDefect = _FsMIEcfmRMepRDIDefect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 5),
    _FsMIEcfmRMepRDIDefect_Type()
)
fsMIEcfmRMepRDIDefect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepRDIDefect.setStatus("current")
_FsMIEcfmRMepMacAddress_Type = MacAddress
_FsMIEcfmRMepMacAddress_Object = MibTableColumn
fsMIEcfmRMepMacAddress = _FsMIEcfmRMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 6),
    _FsMIEcfmRMepMacAddress_Type()
)
fsMIEcfmRMepMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepMacAddress.setStatus("current")
_FsMIEcfmRMepRdi_Type = TruthValue
_FsMIEcfmRMepRdi_Object = MibTableColumn
fsMIEcfmRMepRdi = _FsMIEcfmRMepRdi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 7),
    _FsMIEcfmRMepRdi_Type()
)
fsMIEcfmRMepRdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepRdi.setStatus("current")


class _FsMIEcfmRMepPortStatusTlv_Type(FsMIEcfmPortStatus):
    """Custom type fsMIEcfmRMepPortStatusTlv based on FsMIEcfmPortStatus"""
    defaultValue = 0


_FsMIEcfmRMepPortStatusTlv_Type.__name__ = "FsMIEcfmPortStatus"
_FsMIEcfmRMepPortStatusTlv_Object = MibTableColumn
fsMIEcfmRMepPortStatusTlv = _FsMIEcfmRMepPortStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 8),
    _FsMIEcfmRMepPortStatusTlv_Type()
)
fsMIEcfmRMepPortStatusTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepPortStatusTlv.setStatus("current")


class _FsMIEcfmRMepInterfaceStatusTlv_Type(FsMIEcfmInterfaceStatus):
    """Custom type fsMIEcfmRMepInterfaceStatusTlv based on FsMIEcfmInterfaceStatus"""
    defaultValue = 0


_FsMIEcfmRMepInterfaceStatusTlv_Type.__name__ = "FsMIEcfmInterfaceStatus"
_FsMIEcfmRMepInterfaceStatusTlv_Object = MibTableColumn
fsMIEcfmRMepInterfaceStatusTlv = _FsMIEcfmRMepInterfaceStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 9),
    _FsMIEcfmRMepInterfaceStatusTlv_Type()
)
fsMIEcfmRMepInterfaceStatusTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepInterfaceStatusTlv.setStatus("current")


class _FsMIEcfmRMepChassisIdSubtype_Type(LldpChassisIdSubtype):
    """Custom type fsMIEcfmRMepChassisIdSubtype based on LldpChassisIdSubtype"""
    defaultValue = 4


_FsMIEcfmRMepChassisIdSubtype_Type.__name__ = "LldpChassisIdSubtype"
_FsMIEcfmRMepChassisIdSubtype_Object = MibTableColumn
fsMIEcfmRMepChassisIdSubtype = _FsMIEcfmRMepChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 10),
    _FsMIEcfmRMepChassisIdSubtype_Type()
)
fsMIEcfmRMepChassisIdSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepChassisIdSubtype.setStatus("current")
_FsMIEcfmRMepDbChassisId_Type = LldpChassisId
_FsMIEcfmRMepDbChassisId_Object = MibTableColumn
fsMIEcfmRMepDbChassisId = _FsMIEcfmRMepDbChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 11),
    _FsMIEcfmRMepDbChassisId_Type()
)
fsMIEcfmRMepDbChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepDbChassisId.setStatus("current")
_FsMIEcfmRMepManAddressDomain_Type = TDomain
_FsMIEcfmRMepManAddressDomain_Object = MibTableColumn
fsMIEcfmRMepManAddressDomain = _FsMIEcfmRMepManAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 12),
    _FsMIEcfmRMepManAddressDomain_Type()
)
fsMIEcfmRMepManAddressDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepManAddressDomain.setStatus("current")
_FsMIEcfmRMepManAddress_Type = TAddress
_FsMIEcfmRMepManAddress_Object = MibTableColumn
fsMIEcfmRMepManAddress = _FsMIEcfmRMepManAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 11, 1, 13),
    _FsMIEcfmRMepManAddress_Type()
)
fsMIEcfmRMepManAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRMepManAddress.setStatus("current")
_FsMIEcfmLtmTable_Object = MibTable
fsMIEcfmLtmTable = _FsMIEcfmLtmTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 12)
)
if mibBuilder.loadTexts:
    fsMIEcfmLtmTable.setStatus("current")
_FsMIEcfmLtmEntry_Object = MibTableRow
fsMIEcfmLtmEntry = _FsMIEcfmLtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 12, 1)
)
fsMIEcfmLtmEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMepIdentifier"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmLtmSeqNumber"),
)
if mibBuilder.loadTexts:
    fsMIEcfmLtmEntry.setStatus("current")


class _FsMIEcfmLtmSeqNumber_Type(Unsigned32):
    """Custom type fsMIEcfmLtmSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIEcfmLtmSeqNumber_Type.__name__ = "Unsigned32"
_FsMIEcfmLtmSeqNumber_Object = MibTableColumn
fsMIEcfmLtmSeqNumber = _FsMIEcfmLtmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 12, 1, 1),
    _FsMIEcfmLtmSeqNumber_Type()
)
fsMIEcfmLtmSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmLtmSeqNumber.setStatus("current")
_FsMIEcfmLtmTargetMacAddress_Type = MacAddress
_FsMIEcfmLtmTargetMacAddress_Object = MibTableColumn
fsMIEcfmLtmTargetMacAddress = _FsMIEcfmLtmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 12, 1, 2),
    _FsMIEcfmLtmTargetMacAddress_Type()
)
fsMIEcfmLtmTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtmTargetMacAddress.setStatus("current")


class _FsMIEcfmLtmTtl_Type(Unsigned32):
    """Custom type fsMIEcfmLtmTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIEcfmLtmTtl_Type.__name__ = "Unsigned32"
_FsMIEcfmLtmTtl_Object = MibTableColumn
fsMIEcfmLtmTtl = _FsMIEcfmLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 12, 1, 3),
    _FsMIEcfmLtmTtl_Type()
)
fsMIEcfmLtmTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmLtmTtl.setStatus("current")
_FsMIEcfmMepExTable_Object = MibTable
fsMIEcfmMepExTable = _FsMIEcfmMepExTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 13)
)
if mibBuilder.loadTexts:
    fsMIEcfmMepExTable.setStatus("current")
_FsMIEcfmMepExEntry_Object = MibTableRow
fsMIEcfmMepExEntry = _FsMIEcfmMepExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 13, 1)
)
fsMIEcfmMepExEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMepExEntry.setStatus("current")


class _FsMIEcfmXconnRMepId_Type(Unsigned32):
    """Custom type fsMIEcfmXconnRMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_FsMIEcfmXconnRMepId_Type.__name__ = "Unsigned32"
_FsMIEcfmXconnRMepId_Object = MibTableColumn
fsMIEcfmXconnRMepId = _FsMIEcfmXconnRMepId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 13, 1, 1),
    _FsMIEcfmXconnRMepId_Type()
)
fsMIEcfmXconnRMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmXconnRMepId.setStatus("current")


class _FsMIEcfmErrorRMepId_Type(Unsigned32):
    """Custom type fsMIEcfmErrorRMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_FsMIEcfmErrorRMepId_Type.__name__ = "Unsigned32"
_FsMIEcfmErrorRMepId_Object = MibTableColumn
fsMIEcfmErrorRMepId = _FsMIEcfmErrorRMepId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 13, 1, 2),
    _FsMIEcfmErrorRMepId_Type()
)
fsMIEcfmErrorRMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmErrorRMepId.setStatus("current")
_FsMIEcfmMepDefectRDICcm_Type = TruthValue
_FsMIEcfmMepDefectRDICcm_Object = MibTableColumn
fsMIEcfmMepDefectRDICcm = _FsMIEcfmMepDefectRDICcm_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 13, 1, 3),
    _FsMIEcfmMepDefectRDICcm_Type()
)
fsMIEcfmMepDefectRDICcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMepDefectRDICcm.setStatus("current")
_FsMIEcfmMepDefectMacStatus_Type = TruthValue
_FsMIEcfmMepDefectMacStatus_Object = MibTableColumn
fsMIEcfmMepDefectMacStatus = _FsMIEcfmMepDefectMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 13, 1, 4),
    _FsMIEcfmMepDefectMacStatus_Type()
)
fsMIEcfmMepDefectMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMepDefectMacStatus.setStatus("current")
_FsMIEcfmMepDefectRemoteCcm_Type = TruthValue
_FsMIEcfmMepDefectRemoteCcm_Object = MibTableColumn
fsMIEcfmMepDefectRemoteCcm = _FsMIEcfmMepDefectRemoteCcm_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 13, 1, 5),
    _FsMIEcfmMepDefectRemoteCcm_Type()
)
fsMIEcfmMepDefectRemoteCcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMepDefectRemoteCcm.setStatus("current")
_FsMIEcfmMepDefectErrorCcm_Type = TruthValue
_FsMIEcfmMepDefectErrorCcm_Object = MibTableColumn
fsMIEcfmMepDefectErrorCcm = _FsMIEcfmMepDefectErrorCcm_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 13, 1, 6),
    _FsMIEcfmMepDefectErrorCcm_Type()
)
fsMIEcfmMepDefectErrorCcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMepDefectErrorCcm.setStatus("current")
_FsMIEcfmMepDefectXconnCcm_Type = TruthValue
_FsMIEcfmMepDefectXconnCcm_Object = MibTableColumn
fsMIEcfmMepDefectXconnCcm = _FsMIEcfmMepDefectXconnCcm_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 13, 1, 7),
    _FsMIEcfmMepDefectXconnCcm_Type()
)
fsMIEcfmMepDefectXconnCcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMepDefectXconnCcm.setStatus("current")
_FsMIEcfmMdExTable_Object = MibTable
fsMIEcfmMdExTable = _FsMIEcfmMdExTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 14)
)
if mibBuilder.loadTexts:
    fsMIEcfmMdExTable.setStatus("current")
_FsMIEcfmMdExEntry_Object = MibTableRow
fsMIEcfmMdExEntry = _FsMIEcfmMdExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 14, 1)
)
fsMIEcfmMdExEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMdExEntry.setStatus("current")


class _FsMIEcfmMepArchiveHoldTime_Type(Integer32):
    """Custom type fsMIEcfmMepArchiveHoldTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_FsMIEcfmMepArchiveHoldTime_Type.__name__ = "Integer32"
_FsMIEcfmMepArchiveHoldTime_Object = MibTableColumn
fsMIEcfmMepArchiveHoldTime = _FsMIEcfmMepArchiveHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 14, 1, 1),
    _FsMIEcfmMepArchiveHoldTime_Type()
)
fsMIEcfmMepArchiveHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMepArchiveHoldTime.setStatus("current")
_FsMIEcfmMaExTable_Object = MibTable
fsMIEcfmMaExTable = _FsMIEcfmMaExTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 15)
)
if mibBuilder.loadTexts:
    fsMIEcfmMaExTable.setStatus("current")
_FsMIEcfmMaExEntry_Object = MibTableRow
fsMIEcfmMaExEntry = _FsMIEcfmMaExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 15, 1)
)
fsMIEcfmMaExEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMdIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMaIndex"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMaExEntry.setStatus("current")


class _FsMIEcfmMaCrosscheckStatus_Type(Integer32):
    """Custom type fsMIEcfmMaCrosscheckStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIEcfmMaCrosscheckStatus_Type.__name__ = "Integer32"
_FsMIEcfmMaCrosscheckStatus_Object = MibTableColumn
fsMIEcfmMaCrosscheckStatus = _FsMIEcfmMaCrosscheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 15, 1, 1),
    _FsMIEcfmMaCrosscheckStatus_Type()
)
fsMIEcfmMaCrosscheckStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmMaCrosscheckStatus.setStatus("current")
_FsMIEcfmStatsTable_Object = MibTable
fsMIEcfmStatsTable = _FsMIEcfmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16)
)
if mibBuilder.loadTexts:
    fsMIEcfmStatsTable.setStatus("current")
_FsMIEcfmStatsEntry_Object = MibTableRow
fsMIEcfmStatsEntry = _FsMIEcfmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1)
)
fsMIEcfmStatsEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmContextId"),
)
if mibBuilder.loadTexts:
    fsMIEcfmStatsEntry.setStatus("current")
_FsMIEcfmTxCfmPduCount_Type = Unsigned32
_FsMIEcfmTxCfmPduCount_Object = MibTableColumn
fsMIEcfmTxCfmPduCount = _FsMIEcfmTxCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 1),
    _FsMIEcfmTxCfmPduCount_Type()
)
fsMIEcfmTxCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmTxCfmPduCount.setStatus("current")
_FsMIEcfmTxCcmCount_Type = Unsigned32
_FsMIEcfmTxCcmCount_Object = MibTableColumn
fsMIEcfmTxCcmCount = _FsMIEcfmTxCcmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 2),
    _FsMIEcfmTxCcmCount_Type()
)
fsMIEcfmTxCcmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmTxCcmCount.setStatus("current")
_FsMIEcfmTxLbmCount_Type = Unsigned32
_FsMIEcfmTxLbmCount_Object = MibTableColumn
fsMIEcfmTxLbmCount = _FsMIEcfmTxLbmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 3),
    _FsMIEcfmTxLbmCount_Type()
)
fsMIEcfmTxLbmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmTxLbmCount.setStatus("current")
_FsMIEcfmTxLbrCount_Type = Unsigned32
_FsMIEcfmTxLbrCount_Object = MibTableColumn
fsMIEcfmTxLbrCount = _FsMIEcfmTxLbrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 4),
    _FsMIEcfmTxLbrCount_Type()
)
fsMIEcfmTxLbrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmTxLbrCount.setStatus("current")
_FsMIEcfmTxLtmCount_Type = Unsigned32
_FsMIEcfmTxLtmCount_Object = MibTableColumn
fsMIEcfmTxLtmCount = _FsMIEcfmTxLtmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 5),
    _FsMIEcfmTxLtmCount_Type()
)
fsMIEcfmTxLtmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmTxLtmCount.setStatus("current")
_FsMIEcfmTxLtrCount_Type = Unsigned32
_FsMIEcfmTxLtrCount_Object = MibTableColumn
fsMIEcfmTxLtrCount = _FsMIEcfmTxLtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 6),
    _FsMIEcfmTxLtrCount_Type()
)
fsMIEcfmTxLtrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmTxLtrCount.setStatus("current")
_FsMIEcfmTxFailedCount_Type = Unsigned32
_FsMIEcfmTxFailedCount_Object = MibTableColumn
fsMIEcfmTxFailedCount = _FsMIEcfmTxFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 7),
    _FsMIEcfmTxFailedCount_Type()
)
fsMIEcfmTxFailedCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmTxFailedCount.setStatus("current")
_FsMIEcfmRxCfmPduCount_Type = Unsigned32
_FsMIEcfmRxCfmPduCount_Object = MibTableColumn
fsMIEcfmRxCfmPduCount = _FsMIEcfmRxCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 8),
    _FsMIEcfmRxCfmPduCount_Type()
)
fsMIEcfmRxCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRxCfmPduCount.setStatus("current")
_FsMIEcfmRxCcmCount_Type = Unsigned32
_FsMIEcfmRxCcmCount_Object = MibTableColumn
fsMIEcfmRxCcmCount = _FsMIEcfmRxCcmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 9),
    _FsMIEcfmRxCcmCount_Type()
)
fsMIEcfmRxCcmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRxCcmCount.setStatus("current")
_FsMIEcfmRxLbmCount_Type = Unsigned32
_FsMIEcfmRxLbmCount_Object = MibTableColumn
fsMIEcfmRxLbmCount = _FsMIEcfmRxLbmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 10),
    _FsMIEcfmRxLbmCount_Type()
)
fsMIEcfmRxLbmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRxLbmCount.setStatus("current")
_FsMIEcfmRxLbrCount_Type = Unsigned32
_FsMIEcfmRxLbrCount_Object = MibTableColumn
fsMIEcfmRxLbrCount = _FsMIEcfmRxLbrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 11),
    _FsMIEcfmRxLbrCount_Type()
)
fsMIEcfmRxLbrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRxLbrCount.setStatus("current")
_FsMIEcfmRxLtmCount_Type = Unsigned32
_FsMIEcfmRxLtmCount_Object = MibTableColumn
fsMIEcfmRxLtmCount = _FsMIEcfmRxLtmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 12),
    _FsMIEcfmRxLtmCount_Type()
)
fsMIEcfmRxLtmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRxLtmCount.setStatus("current")
_FsMIEcfmRxLtrCount_Type = Unsigned32
_FsMIEcfmRxLtrCount_Object = MibTableColumn
fsMIEcfmRxLtrCount = _FsMIEcfmRxLtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 13),
    _FsMIEcfmRxLtrCount_Type()
)
fsMIEcfmRxLtrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRxLtrCount.setStatus("current")
_FsMIEcfmRxBadCfmPduCount_Type = Unsigned32
_FsMIEcfmRxBadCfmPduCount_Object = MibTableColumn
fsMIEcfmRxBadCfmPduCount = _FsMIEcfmRxBadCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 14),
    _FsMIEcfmRxBadCfmPduCount_Type()
)
fsMIEcfmRxBadCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmRxBadCfmPduCount.setStatus("current")
_FsMIEcfmFrwdCfmPduCount_Type = Unsigned32
_FsMIEcfmFrwdCfmPduCount_Object = MibTableColumn
fsMIEcfmFrwdCfmPduCount = _FsMIEcfmFrwdCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 15),
    _FsMIEcfmFrwdCfmPduCount_Type()
)
fsMIEcfmFrwdCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmFrwdCfmPduCount.setStatus("current")
_FsMIEcfmDsrdCfmPduCount_Type = Unsigned32
_FsMIEcfmDsrdCfmPduCount_Object = MibTableColumn
fsMIEcfmDsrdCfmPduCount = _FsMIEcfmDsrdCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 0, 16, 1, 16),
    _FsMIEcfmDsrdCfmPduCount_Type()
)
fsMIEcfmDsrdCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmDsrdCfmPduCount.setStatus("current")
_FsMIEcfmSystem_ObjectIdentity = ObjectIdentity
fsMIEcfmSystem = _FsMIEcfmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1)
)
_FsMIEcfmGlobalTrace_Type = TruthValue
_FsMIEcfmGlobalTrace_Object = MibScalar
fsMIEcfmGlobalTrace = _FsMIEcfmGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 1),
    _FsMIEcfmGlobalTrace_Type()
)
fsMIEcfmGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmGlobalTrace.setStatus("current")
_FsMIEcfmOui_Type = FsMIEcfmOuiType
_FsMIEcfmOui_Object = MibScalar
fsMIEcfmOui = _FsMIEcfmOui_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 2),
    _FsMIEcfmOui_Type()
)
fsMIEcfmOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmOui.setStatus("current")
_FsMIEcfmPortTable_Object = MibTable
fsMIEcfmPortTable = _FsMIEcfmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIEcfmPortTable.setStatus("current")
_FsMIEcfmPortEntry_Object = MibTableRow
fsMIEcfmPortEntry = _FsMIEcfmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1)
)
fsMIEcfmPortEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmPortIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIEcfmPortEntry.setStatus("current")
_FsMIEcfmPortIfIndex_Type = InterfaceIndex
_FsMIEcfmPortIfIndex_Object = MibTableColumn
fsMIEcfmPortIfIndex = _FsMIEcfmPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 1),
    _FsMIEcfmPortIfIndex_Type()
)
fsMIEcfmPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmPortIfIndex.setStatus("current")


class _FsMIEcfmPortLLCEncapStatus_Type(TruthValue):
    """Custom type fsMIEcfmPortLLCEncapStatus based on TruthValue"""
    defaultValue = 2


_FsMIEcfmPortLLCEncapStatus_Type.__name__ = "TruthValue"
_FsMIEcfmPortLLCEncapStatus_Object = MibTableColumn
fsMIEcfmPortLLCEncapStatus = _FsMIEcfmPortLLCEncapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 2),
    _FsMIEcfmPortLLCEncapStatus_Type()
)
fsMIEcfmPortLLCEncapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortLLCEncapStatus.setStatus("current")


class _FsMIEcfmPortModuleStatus_Type(Integer32):
    """Custom type fsMIEcfmPortModuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMIEcfmPortModuleStatus_Type.__name__ = "Integer32"
_FsMIEcfmPortModuleStatus_Object = MibTableColumn
fsMIEcfmPortModuleStatus = _FsMIEcfmPortModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 3),
    _FsMIEcfmPortModuleStatus_Type()
)
fsMIEcfmPortModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortModuleStatus.setStatus("current")
_FsMIEcfmPortTxCfmPduCount_Type = Unsigned32
_FsMIEcfmPortTxCfmPduCount_Object = MibTableColumn
fsMIEcfmPortTxCfmPduCount = _FsMIEcfmPortTxCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 4),
    _FsMIEcfmPortTxCfmPduCount_Type()
)
fsMIEcfmPortTxCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortTxCfmPduCount.setStatus("current")
_FsMIEcfmPortTxCcmCount_Type = Unsigned32
_FsMIEcfmPortTxCcmCount_Object = MibTableColumn
fsMIEcfmPortTxCcmCount = _FsMIEcfmPortTxCcmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 5),
    _FsMIEcfmPortTxCcmCount_Type()
)
fsMIEcfmPortTxCcmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortTxCcmCount.setStatus("current")
_FsMIEcfmPortTxLbmCount_Type = Unsigned32
_FsMIEcfmPortTxLbmCount_Object = MibTableColumn
fsMIEcfmPortTxLbmCount = _FsMIEcfmPortTxLbmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 6),
    _FsMIEcfmPortTxLbmCount_Type()
)
fsMIEcfmPortTxLbmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortTxLbmCount.setStatus("current")
_FsMIEcfmPortTxLbrCount_Type = Unsigned32
_FsMIEcfmPortTxLbrCount_Object = MibTableColumn
fsMIEcfmPortTxLbrCount = _FsMIEcfmPortTxLbrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 7),
    _FsMIEcfmPortTxLbrCount_Type()
)
fsMIEcfmPortTxLbrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortTxLbrCount.setStatus("current")
_FsMIEcfmPortTxLtmCount_Type = Unsigned32
_FsMIEcfmPortTxLtmCount_Object = MibTableColumn
fsMIEcfmPortTxLtmCount = _FsMIEcfmPortTxLtmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 8),
    _FsMIEcfmPortTxLtmCount_Type()
)
fsMIEcfmPortTxLtmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortTxLtmCount.setStatus("current")
_FsMIEcfmPortTxLtrCount_Type = Unsigned32
_FsMIEcfmPortTxLtrCount_Object = MibTableColumn
fsMIEcfmPortTxLtrCount = _FsMIEcfmPortTxLtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 9),
    _FsMIEcfmPortTxLtrCount_Type()
)
fsMIEcfmPortTxLtrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortTxLtrCount.setStatus("current")
_FsMIEcfmPortTxFailedCount_Type = Unsigned32
_FsMIEcfmPortTxFailedCount_Object = MibTableColumn
fsMIEcfmPortTxFailedCount = _FsMIEcfmPortTxFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 10),
    _FsMIEcfmPortTxFailedCount_Type()
)
fsMIEcfmPortTxFailedCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortTxFailedCount.setStatus("current")
_FsMIEcfmPortRxCfmPduCount_Type = Unsigned32
_FsMIEcfmPortRxCfmPduCount_Object = MibTableColumn
fsMIEcfmPortRxCfmPduCount = _FsMIEcfmPortRxCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 11),
    _FsMIEcfmPortRxCfmPduCount_Type()
)
fsMIEcfmPortRxCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortRxCfmPduCount.setStatus("current")
_FsMIEcfmPortRxCcmCount_Type = Unsigned32
_FsMIEcfmPortRxCcmCount_Object = MibTableColumn
fsMIEcfmPortRxCcmCount = _FsMIEcfmPortRxCcmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 12),
    _FsMIEcfmPortRxCcmCount_Type()
)
fsMIEcfmPortRxCcmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortRxCcmCount.setStatus("current")
_FsMIEcfmPortRxLbmCount_Type = Unsigned32
_FsMIEcfmPortRxLbmCount_Object = MibTableColumn
fsMIEcfmPortRxLbmCount = _FsMIEcfmPortRxLbmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 13),
    _FsMIEcfmPortRxLbmCount_Type()
)
fsMIEcfmPortRxLbmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortRxLbmCount.setStatus("current")
_FsMIEcfmPortRxLbrCount_Type = Unsigned32
_FsMIEcfmPortRxLbrCount_Object = MibTableColumn
fsMIEcfmPortRxLbrCount = _FsMIEcfmPortRxLbrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 14),
    _FsMIEcfmPortRxLbrCount_Type()
)
fsMIEcfmPortRxLbrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortRxLbrCount.setStatus("current")
_FsMIEcfmPortRxLtmCount_Type = Unsigned32
_FsMIEcfmPortRxLtmCount_Object = MibTableColumn
fsMIEcfmPortRxLtmCount = _FsMIEcfmPortRxLtmCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 15),
    _FsMIEcfmPortRxLtmCount_Type()
)
fsMIEcfmPortRxLtmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortRxLtmCount.setStatus("current")
_FsMIEcfmPortRxLtrCount_Type = Unsigned32
_FsMIEcfmPortRxLtrCount_Object = MibTableColumn
fsMIEcfmPortRxLtrCount = _FsMIEcfmPortRxLtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 16),
    _FsMIEcfmPortRxLtrCount_Type()
)
fsMIEcfmPortRxLtrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortRxLtrCount.setStatus("current")
_FsMIEcfmPortRxBadCfmPduCount_Type = Unsigned32
_FsMIEcfmPortRxBadCfmPduCount_Object = MibTableColumn
fsMIEcfmPortRxBadCfmPduCount = _FsMIEcfmPortRxBadCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 17),
    _FsMIEcfmPortRxBadCfmPduCount_Type()
)
fsMIEcfmPortRxBadCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortRxBadCfmPduCount.setStatus("current")
_FsMIEcfmPortFrwdCfmPduCount_Type = Unsigned32
_FsMIEcfmPortFrwdCfmPduCount_Object = MibTableColumn
fsMIEcfmPortFrwdCfmPduCount = _FsMIEcfmPortFrwdCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 18),
    _FsMIEcfmPortFrwdCfmPduCount_Type()
)
fsMIEcfmPortFrwdCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortFrwdCfmPduCount.setStatus("current")
_FsMIEcfmPortDsrdCfmPduCount_Type = Unsigned32
_FsMIEcfmPortDsrdCfmPduCount_Object = MibTableColumn
fsMIEcfmPortDsrdCfmPduCount = _FsMIEcfmPortDsrdCfmPduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 3, 1, 19),
    _FsMIEcfmPortDsrdCfmPduCount_Type()
)
fsMIEcfmPortDsrdCfmPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIEcfmPortDsrdCfmPduCount.setStatus("current")
_FsMIEcfmStackTable_Object = MibTable
fsMIEcfmStackTable = _FsMIEcfmStackTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fsMIEcfmStackTable.setStatus("current")
_FsMIEcfmStackEntry_Object = MibTableRow
fsMIEcfmStackEntry = _FsMIEcfmStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4, 1)
)
fsMIEcfmStackEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmStackIfIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmStackVlanIdOrNone"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmStackMdLevel"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmStackDirection"),
)
if mibBuilder.loadTexts:
    fsMIEcfmStackEntry.setStatus("current")
_FsMIEcfmStackIfIndex_Type = InterfaceIndex
_FsMIEcfmStackIfIndex_Object = MibTableColumn
fsMIEcfmStackIfIndex = _FsMIEcfmStackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4, 1, 1),
    _FsMIEcfmStackIfIndex_Type()
)
fsMIEcfmStackIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmStackIfIndex.setStatus("current")
_FsMIEcfmStackVlanIdOrNone_Type = VlanIdOrNone
_FsMIEcfmStackVlanIdOrNone_Object = MibTableColumn
fsMIEcfmStackVlanIdOrNone = _FsMIEcfmStackVlanIdOrNone_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4, 1, 2),
    _FsMIEcfmStackVlanIdOrNone_Type()
)
fsMIEcfmStackVlanIdOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmStackVlanIdOrNone.setStatus("current")
_FsMIEcfmStackMdLevel_Type = FsMIEcfmMDLevel
_FsMIEcfmStackMdLevel_Object = MibTableColumn
fsMIEcfmStackMdLevel = _FsMIEcfmStackMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4, 1, 3),
    _FsMIEcfmStackMdLevel_Type()
)
fsMIEcfmStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmStackMdLevel.setStatus("current")
_FsMIEcfmStackDirection_Type = FsMIEcfmMpDirection
_FsMIEcfmStackDirection_Object = MibTableColumn
fsMIEcfmStackDirection = _FsMIEcfmStackDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4, 1, 4),
    _FsMIEcfmStackDirection_Type()
)
fsMIEcfmStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmStackDirection.setStatus("current")
_FsMIEcfmStackMdIndex_Type = Unsigned32
_FsMIEcfmStackMdIndex_Object = MibTableColumn
fsMIEcfmStackMdIndex = _FsMIEcfmStackMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4, 1, 5),
    _FsMIEcfmStackMdIndex_Type()
)
fsMIEcfmStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmStackMdIndex.setStatus("current")
_FsMIEcfmStackMaIndex_Type = Unsigned32
_FsMIEcfmStackMaIndex_Object = MibTableColumn
fsMIEcfmStackMaIndex = _FsMIEcfmStackMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4, 1, 6),
    _FsMIEcfmStackMaIndex_Type()
)
fsMIEcfmStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmStackMaIndex.setStatus("current")
_FsMIEcfmStackMepId_Type = FsMIEcfmMepIdOrZero
_FsMIEcfmStackMepId_Object = MibTableColumn
fsMIEcfmStackMepId = _FsMIEcfmStackMepId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4, 1, 7),
    _FsMIEcfmStackMepId_Type()
)
fsMIEcfmStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmStackMepId.setStatus("current")
_FsMIEcfmStackMacAddress_Type = MacAddress
_FsMIEcfmStackMacAddress_Object = MibTableColumn
fsMIEcfmStackMacAddress = _FsMIEcfmStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 4, 1, 8),
    _FsMIEcfmStackMacAddress_Type()
)
fsMIEcfmStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmStackMacAddress.setStatus("current")
_FsMIEcfmConfigErrorListTable_Object = MibTable
fsMIEcfmConfigErrorListTable = _FsMIEcfmConfigErrorListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fsMIEcfmConfigErrorListTable.setStatus("current")
_FsMIEcfmConfigErrorListEntry_Object = MibTableRow
fsMIEcfmConfigErrorListEntry = _FsMIEcfmConfigErrorListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 5, 1)
)
fsMIEcfmConfigErrorListEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmConfigErrorListVid"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmConfigErrorListIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIEcfmConfigErrorListEntry.setStatus("current")
_FsMIEcfmConfigErrorListVid_Type = VlanId
_FsMIEcfmConfigErrorListVid_Object = MibTableColumn
fsMIEcfmConfigErrorListVid = _FsMIEcfmConfigErrorListVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 5, 1, 1),
    _FsMIEcfmConfigErrorListVid_Type()
)
fsMIEcfmConfigErrorListVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmConfigErrorListVid.setStatus("current")
_FsMIEcfmConfigErrorListIfIndex_Type = InterfaceIndex
_FsMIEcfmConfigErrorListIfIndex_Object = MibTableColumn
fsMIEcfmConfigErrorListIfIndex = _FsMIEcfmConfigErrorListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 5, 1, 2),
    _FsMIEcfmConfigErrorListIfIndex_Type()
)
fsMIEcfmConfigErrorListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmConfigErrorListIfIndex.setStatus("current")
_FsMIEcfmConfigErrorListErrorType_Type = FsMIEcfmConfigErrors
_FsMIEcfmConfigErrorListErrorType_Object = MibTableColumn
fsMIEcfmConfigErrorListErrorType = _FsMIEcfmConfigErrorListErrorType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 5, 1, 3),
    _FsMIEcfmConfigErrorListErrorType_Type()
)
fsMIEcfmConfigErrorListErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIEcfmConfigErrorListErrorType.setStatus("current")
_FsMIEcfmMipTable_Object = MibTable
fsMIEcfmMipTable = _FsMIEcfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fsMIEcfmMipTable.setStatus("current")
_FsMIEcfmMipEntry_Object = MibTableRow
fsMIEcfmMipEntry = _FsMIEcfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 6, 1)
)
fsMIEcfmMipEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMipIfIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMipMdLevel"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMipVid"),
)
if mibBuilder.loadTexts:
    fsMIEcfmMipEntry.setStatus("current")
_FsMIEcfmMipIfIndex_Type = InterfaceIndex
_FsMIEcfmMipIfIndex_Object = MibTableColumn
fsMIEcfmMipIfIndex = _FsMIEcfmMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 6, 1, 1),
    _FsMIEcfmMipIfIndex_Type()
)
fsMIEcfmMipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMipIfIndex.setStatus("current")


class _FsMIEcfmMipMdLevel_Type(Integer32):
    """Custom type fsMIEcfmMipMdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMIEcfmMipMdLevel_Type.__name__ = "Integer32"
_FsMIEcfmMipMdLevel_Object = MibTableColumn
fsMIEcfmMipMdLevel = _FsMIEcfmMipMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 6, 1, 2),
    _FsMIEcfmMipMdLevel_Type()
)
fsMIEcfmMipMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMipMdLevel.setStatus("current")
_FsMIEcfmMipVid_Type = VlanId
_FsMIEcfmMipVid_Object = MibTableColumn
fsMIEcfmMipVid = _FsMIEcfmMipVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 6, 1, 3),
    _FsMIEcfmMipVid_Type()
)
fsMIEcfmMipVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIEcfmMipVid.setStatus("current")
_FsMIEcfmMipActive_Type = TruthValue
_FsMIEcfmMipActive_Object = MibTableColumn
fsMIEcfmMipActive = _FsMIEcfmMipActive_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 6, 1, 4),
    _FsMIEcfmMipActive_Type()
)
fsMIEcfmMipActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMipActive.setStatus("current")
_FsMIEcfmMipRowStatus_Type = RowStatus
_FsMIEcfmMipRowStatus_Object = MibTableColumn
fsMIEcfmMipRowStatus = _FsMIEcfmMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 6, 1, 5),
    _FsMIEcfmMipRowStatus_Type()
)
fsMIEcfmMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmMipRowStatus.setStatus("current")
_FsMIEcfmDynMipPreventionTable_Object = MibTable
fsMIEcfmDynMipPreventionTable = _FsMIEcfmDynMipPreventionTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 7)
)
if mibBuilder.loadTexts:
    fsMIEcfmDynMipPreventionTable.setStatus("current")
_FsMIEcfmDynMipPreventionEntry_Object = MibTableRow
fsMIEcfmDynMipPreventionEntry = _FsMIEcfmDynMipPreventionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 7, 1)
)
fsMIEcfmDynMipPreventionEntry.setIndexNames(
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMipIfIndex"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMipMdLevel"),
    (0, "ARICENT-ECFM-MI-MIB", "fsMIEcfmMipVid"),
)
if mibBuilder.loadTexts:
    fsMIEcfmDynMipPreventionEntry.setStatus("current")


class _FsMIEcfmDynMipPreventionRowStatus_Type(RowStatus):
    """Custom type fsMIEcfmDynMipPreventionRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )


_FsMIEcfmDynMipPreventionRowStatus_Type.__name__ = "RowStatus"
_FsMIEcfmDynMipPreventionRowStatus_Object = MibTableColumn
fsMIEcfmDynMipPreventionRowStatus = _FsMIEcfmDynMipPreventionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 160, 1, 1, 7, 1, 1),
    _FsMIEcfmDynMipPreventionRowStatus_Type()
)
fsMIEcfmDynMipPreventionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIEcfmDynMipPreventionRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

fsMIEcfmFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 160, 0, 1)
)
fsMIEcfmFaultAlarm.setObjects(
      *(("ARICENT-ECFM-MI-MIB", "fsMIEcfmContextName"),
        ("ARICENT-ECFM-MI-MIB", "fsMIEcfmMepHighestPrDefect"))
)
if mibBuilder.loadTexts:
    fsMIEcfmFaultAlarm.setStatus(
        "current"
    )

fsEcfmMepDefectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 160, 0, 2)
)
fsEcfmMepDefectTrap.setObjects(
      *(("ARICENT-ECFM-MI-MIB", "fsMIEcfmContextName"),
        ("ARICENT-ECFM-MI-MIB", "fsMIEcfmTrapType"))
)
if mibBuilder.loadTexts:
    fsEcfmMepDefectTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ECFM-MI-MIB",
    **{"FsMIEcfmOuiType": FsMIEcfmOuiType,
       "FsMIEcfmMaintDomainNameType": FsMIEcfmMaintDomainNameType,
       "FsMIEcfmMaintDomainName": FsMIEcfmMaintDomainName,
       "FsMIEcfmMaintAssocNameType": FsMIEcfmMaintAssocNameType,
       "FsMIEcfmMaintAssocName": FsMIEcfmMaintAssocName,
       "FsMIEcfmMDLevel": FsMIEcfmMDLevel,
       "FsMIEcfmMDLevelOrNone": FsMIEcfmMDLevelOrNone,
       "FsMIEcfmMpDirection": FsMIEcfmMpDirection,
       "FsMIEcfmPortStatus": FsMIEcfmPortStatus,
       "FsMIEcfmInterfaceStatus": FsMIEcfmInterfaceStatus,
       "FsMIEcfmHighestDefectPri": FsMIEcfmHighestDefectPri,
       "FsMIEcfmLowestAlarmPri": FsMIEcfmLowestAlarmPri,
       "FsMIEcfmMepId": FsMIEcfmMepId,
       "FsMIEcfmMepIdOrZero": FsMIEcfmMepIdOrZero,
       "FsMIEcfmMhfCreation": FsMIEcfmMhfCreation,
       "FsMIEcfmIdPermission": FsMIEcfmIdPermission,
       "FsMIEcfmCcmInterval": FsMIEcfmCcmInterval,
       "FsMIEcfmFngState": FsMIEcfmFngState,
       "FsMIEcfmRelayActionFieldValue": FsMIEcfmRelayActionFieldValue,
       "FsMIEcfmIngressActionFieldValue": FsMIEcfmIngressActionFieldValue,
       "FsMIEcfmEgressActionFieldValue": FsMIEcfmEgressActionFieldValue,
       "FsMIEcfmRemoteMepState": FsMIEcfmRemoteMepState,
       "FsMIEcfmIndexIntegerNextFree": FsMIEcfmIndexIntegerNextFree,
       "FsMIEcfmMepDefects": FsMIEcfmMepDefects,
       "FsMIEcfmConfigErrors": FsMIEcfmConfigErrors,
       "FsMIEcfmTransmitStatus": FsMIEcfmTransmitStatus,
       "FsMIEcfmSetTraps": FsMIEcfmSetTraps,
       "fsMIEcfmMIB": fsMIEcfmMIB,
       "fsMIEcfmNotifications": fsMIEcfmNotifications,
       "fsMIEcfmFaultAlarm": fsMIEcfmFaultAlarm,
       "fsEcfmMepDefectTrap": fsEcfmMepDefectTrap,
       "fsMIEcfmMIBObjects": fsMIEcfmMIBObjects,
       "fsMIEcfmContext": fsMIEcfmContext,
       "fsMIEcfmContextTable": fsMIEcfmContextTable,
       "fsMIEcfmContextEntry": fsMIEcfmContextEntry,
       "fsMIEcfmContextId": fsMIEcfmContextId,
       "fsMIEcfmSystemControl": fsMIEcfmSystemControl,
       "fsMIEcfmModuleStatus": fsMIEcfmModuleStatus,
       "fsMIEcfmDefaultMdDefLevel": fsMIEcfmDefaultMdDefLevel,
       "fsMIEcfmDefaultMdDefMhfCreation": fsMIEcfmDefaultMdDefMhfCreation,
       "fsMIEcfmDefaultMdDefIdPermission": fsMIEcfmDefaultMdDefIdPermission,
       "fsMIEcfmMdTableNextIndex": fsMIEcfmMdTableNextIndex,
       "fsMIEcfmLtrCacheStatus": fsMIEcfmLtrCacheStatus,
       "fsMIEcfmLtrCacheClear": fsMIEcfmLtrCacheClear,
       "fsMIEcfmLtrCacheHoldTime": fsMIEcfmLtrCacheHoldTime,
       "fsMIEcfmLtrCacheSize": fsMIEcfmLtrCacheSize,
       "fsMIEcfmMipCcmDbStatus": fsMIEcfmMipCcmDbStatus,
       "fsMIEcfmMipCcmDbClear": fsMIEcfmMipCcmDbClear,
       "fsMIEcfmMipCcmDbSize": fsMIEcfmMipCcmDbSize,
       "fsMIEcfmMipCcmDbHoldTime": fsMIEcfmMipCcmDbHoldTime,
       "fsMIEcfmMemoryFailureCount": fsMIEcfmMemoryFailureCount,
       "fsMIEcfmBufferFailureCount": fsMIEcfmBufferFailureCount,
       "fsMIEcfmUpCount": fsMIEcfmUpCount,
       "fsMIEcfmDownCount": fsMIEcfmDownCount,
       "fsMIEcfmNoDftCount": fsMIEcfmNoDftCount,
       "fsMIEcfmRdiDftCount": fsMIEcfmRdiDftCount,
       "fsMIEcfmMacStatusDftCount": fsMIEcfmMacStatusDftCount,
       "fsMIEcfmRemoteCcmDftCount": fsMIEcfmRemoteCcmDftCount,
       "fsMIEcfmErrorCcmDftCount": fsMIEcfmErrorCcmDftCount,
       "fsMIEcfmXconDftCount": fsMIEcfmXconDftCount,
       "fsMIEcfmCrosscheckDelay": fsMIEcfmCrosscheckDelay,
       "fsMIEcfmMipDynamicEvaluationStatus": fsMIEcfmMipDynamicEvaluationStatus,
       "fsMIEcfmContextName": fsMIEcfmContextName,
       "fsMIEcfmTrapControl": fsMIEcfmTrapControl,
       "fsMIEcfmTrapType": fsMIEcfmTrapType,
       "fsMIEcfmTraceOption": fsMIEcfmTraceOption,
       "fsMIEcfmGlobalCcmOffload": fsMIEcfmGlobalCcmOffload,
       "fsMIEcfmVlanTable": fsMIEcfmVlanTable,
       "fsMIEcfmVlanEntry": fsMIEcfmVlanEntry,
       "fsMIEcfmVlanVid": fsMIEcfmVlanVid,
       "fsMIEcfmVlanPrimaryVid": fsMIEcfmVlanPrimaryVid,
       "fsMIEcfmVlanRowStatus": fsMIEcfmVlanRowStatus,
       "fsMIEcfmDefaultMdTable": fsMIEcfmDefaultMdTable,
       "fsMIEcfmDefaultMdEntry": fsMIEcfmDefaultMdEntry,
       "fsMIEcfmDefaultMdPrimaryVid": fsMIEcfmDefaultMdPrimaryVid,
       "fsMIEcfmDefaultMdStatus": fsMIEcfmDefaultMdStatus,
       "fsMIEcfmDefaultMdLevel": fsMIEcfmDefaultMdLevel,
       "fsMIEcfmDefaultMdMhfCreation": fsMIEcfmDefaultMdMhfCreation,
       "fsMIEcfmDefaultMdIdPermission": fsMIEcfmDefaultMdIdPermission,
       "fsMIEcfmMdTable": fsMIEcfmMdTable,
       "fsMIEcfmMdEntry": fsMIEcfmMdEntry,
       "fsMIEcfmMdIndex": fsMIEcfmMdIndex,
       "fsMIEcfmMdFormat": fsMIEcfmMdFormat,
       "fsMIEcfmMdName": fsMIEcfmMdName,
       "fsMIEcfmMdMdLevel": fsMIEcfmMdMdLevel,
       "fsMIEcfmMdMhfCreation": fsMIEcfmMdMhfCreation,
       "fsMIEcfmMdMhfIdPermission": fsMIEcfmMdMhfIdPermission,
       "fsMIEcfmMdMaTableNextIndex": fsMIEcfmMdMaTableNextIndex,
       "fsMIEcfmMdRowStatus": fsMIEcfmMdRowStatus,
       "fsMIEcfmMaTable": fsMIEcfmMaTable,
       "fsMIEcfmMaEntry": fsMIEcfmMaEntry,
       "fsMIEcfmMaIndex": fsMIEcfmMaIndex,
       "fsMIEcfmMaPrimaryVlanId": fsMIEcfmMaPrimaryVlanId,
       "fsMIEcfmMaFormat": fsMIEcfmMaFormat,
       "fsMIEcfmMaName": fsMIEcfmMaName,
       "fsMIEcfmMaMhfCreation": fsMIEcfmMaMhfCreation,
       "fsMIEcfmMaIdPermission": fsMIEcfmMaIdPermission,
       "fsMIEcfmMaCcmInterval": fsMIEcfmMaCcmInterval,
       "fsMIEcfmMaNumberOfVids": fsMIEcfmMaNumberOfVids,
       "fsMIEcfmMaRowStatus": fsMIEcfmMaRowStatus,
       "fsMIEcfmMaMepListTable": fsMIEcfmMaMepListTable,
       "fsMIEcfmMaMepListEntry": fsMIEcfmMaMepListEntry,
       "fsMIEcfmMaMepListIdentifier": fsMIEcfmMaMepListIdentifier,
       "fsMIEcfmMaMepListRowStatus": fsMIEcfmMaMepListRowStatus,
       "fsMIEcfmMepTable": fsMIEcfmMepTable,
       "fsMIEcfmMepEntry": fsMIEcfmMepEntry,
       "fsMIEcfmMepIdentifier": fsMIEcfmMepIdentifier,
       "fsMIEcfmMepIfIndex": fsMIEcfmMepIfIndex,
       "fsMIEcfmMepDirection": fsMIEcfmMepDirection,
       "fsMIEcfmMepPrimaryVid": fsMIEcfmMepPrimaryVid,
       "fsMIEcfmMepActive": fsMIEcfmMepActive,
       "fsMIEcfmMepFngState": fsMIEcfmMepFngState,
       "fsMIEcfmMepCciEnabled": fsMIEcfmMepCciEnabled,
       "fsMIEcfmMepCcmLtmPriority": fsMIEcfmMepCcmLtmPriority,
       "fsMIEcfmMepMacAddress": fsMIEcfmMepMacAddress,
       "fsMIEcfmMepLowPrDef": fsMIEcfmMepLowPrDef,
       "fsMIEcfmMepFngAlarmTime": fsMIEcfmMepFngAlarmTime,
       "fsMIEcfmMepFngResetTime": fsMIEcfmMepFngResetTime,
       "fsMIEcfmMepHighestPrDefect": fsMIEcfmMepHighestPrDefect,
       "fsMIEcfmMepDefects": fsMIEcfmMepDefects,
       "fsMIEcfmMepErrorCcmLastFailure": fsMIEcfmMepErrorCcmLastFailure,
       "fsMIEcfmMepXconCcmLastFailure": fsMIEcfmMepXconCcmLastFailure,
       "fsMIEcfmMepCcmSequenceErrors": fsMIEcfmMepCcmSequenceErrors,
       "fsMIEcfmMepCciSentCcms": fsMIEcfmMepCciSentCcms,
       "fsMIEcfmMepNextLbmTransId": fsMIEcfmMepNextLbmTransId,
       "fsMIEcfmMepLbrIn": fsMIEcfmMepLbrIn,
       "fsMIEcfmMepLbrInOutOfOrder": fsMIEcfmMepLbrInOutOfOrder,
       "fsMIEcfmMepLbrBadMsdu": fsMIEcfmMepLbrBadMsdu,
       "fsMIEcfmMepLtmNextSeqNumber": fsMIEcfmMepLtmNextSeqNumber,
       "fsMIEcfmMepUnexpLtrIn": fsMIEcfmMepUnexpLtrIn,
       "fsMIEcfmMepLbrOut": fsMIEcfmMepLbrOut,
       "fsMIEcfmMepTransmitLbmStatus": fsMIEcfmMepTransmitLbmStatus,
       "fsMIEcfmMepTransmitLbmDestMacAddress": fsMIEcfmMepTransmitLbmDestMacAddress,
       "fsMIEcfmMepTransmitLbmDestMepId": fsMIEcfmMepTransmitLbmDestMepId,
       "fsMIEcfmMepTransmitLbmDestIsMepId": fsMIEcfmMepTransmitLbmDestIsMepId,
       "fsMIEcfmMepTransmitLbmMessages": fsMIEcfmMepTransmitLbmMessages,
       "fsMIEcfmMepTransmitLbmDataTlv": fsMIEcfmMepTransmitLbmDataTlv,
       "fsMIEcfmMepTransmitLbmVlanPriority": fsMIEcfmMepTransmitLbmVlanPriority,
       "fsMIEcfmMepTransmitLbmVlanDropEnable": fsMIEcfmMepTransmitLbmVlanDropEnable,
       "fsMIEcfmMepTransmitLbmResultOK": fsMIEcfmMepTransmitLbmResultOK,
       "fsMIEcfmMepTransmitLbmSeqNumber": fsMIEcfmMepTransmitLbmSeqNumber,
       "fsMIEcfmMepTransmitLtmStatus": fsMIEcfmMepTransmitLtmStatus,
       "fsMIEcfmMepTransmitLtmFlags": fsMIEcfmMepTransmitLtmFlags,
       "fsMIEcfmMepTransmitLtmTargetMacAddress": fsMIEcfmMepTransmitLtmTargetMacAddress,
       "fsMIEcfmMepTransmitLtmTargetMepId": fsMIEcfmMepTransmitLtmTargetMepId,
       "fsMIEcfmMepTransmitLtmTargetIsMepId": fsMIEcfmMepTransmitLtmTargetIsMepId,
       "fsMIEcfmMepTransmitLtmTtl": fsMIEcfmMepTransmitLtmTtl,
       "fsMIEcfmMepTransmitLtmResult": fsMIEcfmMepTransmitLtmResult,
       "fsMIEcfmMepTransmitLtmSeqNumber": fsMIEcfmMepTransmitLtmSeqNumber,
       "fsMIEcfmMepTransmitLtmEgressIdentifier": fsMIEcfmMepTransmitLtmEgressIdentifier,
       "fsMIEcfmMepRowStatus": fsMIEcfmMepRowStatus,
       "fsMIEcfmMepCcmOffload": fsMIEcfmMepCcmOffload,
       "fsMIEcfmLtrTable": fsMIEcfmLtrTable,
       "fsMIEcfmLtrEntry": fsMIEcfmLtrEntry,
       "fsMIEcfmLtrSeqNumber": fsMIEcfmLtrSeqNumber,
       "fsMIEcfmLtrReceiveOrder": fsMIEcfmLtrReceiveOrder,
       "fsMIEcfmLtrTtl": fsMIEcfmLtrTtl,
       "fsMIEcfmLtrForwarded": fsMIEcfmLtrForwarded,
       "fsMIEcfmLtrTerminalMep": fsMIEcfmLtrTerminalMep,
       "fsMIEcfmLtrLastEgressIdentifier": fsMIEcfmLtrLastEgressIdentifier,
       "fsMIEcfmLtrNextEgressIdentifier": fsMIEcfmLtrNextEgressIdentifier,
       "fsMIEcfmLtrRelay": fsMIEcfmLtrRelay,
       "fsMIEcfmLtrChassisIdSubtype": fsMIEcfmLtrChassisIdSubtype,
       "fsMIEcfmLtrChassisId": fsMIEcfmLtrChassisId,
       "fsMIEcfmLtrManAddressDomain": fsMIEcfmLtrManAddressDomain,
       "fsMIEcfmLtrManAddress": fsMIEcfmLtrManAddress,
       "fsMIEcfmLtrIngress": fsMIEcfmLtrIngress,
       "fsMIEcfmLtrIngressMac": fsMIEcfmLtrIngressMac,
       "fsMIEcfmLtrIngressPortIdSubtype": fsMIEcfmLtrIngressPortIdSubtype,
       "fsMIEcfmLtrIngressPortId": fsMIEcfmLtrIngressPortId,
       "fsMIEcfmLtrEgress": fsMIEcfmLtrEgress,
       "fsMIEcfmLtrEgressMac": fsMIEcfmLtrEgressMac,
       "fsMIEcfmLtrEgressPortIdSubtype": fsMIEcfmLtrEgressPortIdSubtype,
       "fsMIEcfmLtrEgressPortId": fsMIEcfmLtrEgressPortId,
       "fsMIEcfmLtrOrganizationSpecificTlv": fsMIEcfmLtrOrganizationSpecificTlv,
       "fsMIEcfmMepDbTable": fsMIEcfmMepDbTable,
       "fsMIEcfmMepDbEntry": fsMIEcfmMepDbEntry,
       "fsMIEcfmMepDbRMepIdentifier": fsMIEcfmMepDbRMepIdentifier,
       "fsMIEcfmMepDbRMepState": fsMIEcfmMepDbRMepState,
       "fsMIEcfmMepDbRMepFailedOkTime": fsMIEcfmMepDbRMepFailedOkTime,
       "fsMIEcfmMepDbMacAddress": fsMIEcfmMepDbMacAddress,
       "fsMIEcfmMepDbRdi": fsMIEcfmMepDbRdi,
       "fsMIEcfmMepDbPortStatusTlv": fsMIEcfmMepDbPortStatusTlv,
       "fsMIEcfmMepDbInterfaceStatusTlv": fsMIEcfmMepDbInterfaceStatusTlv,
       "fsMIEcfmMepDbChassisIdSubtype": fsMIEcfmMepDbChassisIdSubtype,
       "fsMIEcfmMepDbChassisId": fsMIEcfmMepDbChassisId,
       "fsMIEcfmMepDbManAddressDomain": fsMIEcfmMepDbManAddressDomain,
       "fsMIEcfmMepDbManAddress": fsMIEcfmMepDbManAddress,
       "fsMIEcfmMipCcmDbTable": fsMIEcfmMipCcmDbTable,
       "fsMIEcfmMipCcmDbEntry": fsMIEcfmMipCcmDbEntry,
       "fsMIEcfmMipCcmFid": fsMIEcfmMipCcmFid,
       "fsMIEcfmMipCcmSrcAddr": fsMIEcfmMipCcmSrcAddr,
       "fsMIEcfmMipCcmIfIndex": fsMIEcfmMipCcmIfIndex,
       "fsMIEcfmRemoteMepDbExTable": fsMIEcfmRemoteMepDbExTable,
       "fsMIEcfmRemoteMepDbExEntry": fsMIEcfmRemoteMepDbExEntry,
       "fsMIEcfmRMepCcmSequenceNum": fsMIEcfmRMepCcmSequenceNum,
       "fsMIEcfmRMepPortStatusDefect": fsMIEcfmRMepPortStatusDefect,
       "fsMIEcfmRMepInterfaceStatusDefect": fsMIEcfmRMepInterfaceStatusDefect,
       "fsMIEcfmRMepCcmDefect": fsMIEcfmRMepCcmDefect,
       "fsMIEcfmRMepRDIDefect": fsMIEcfmRMepRDIDefect,
       "fsMIEcfmRMepMacAddress": fsMIEcfmRMepMacAddress,
       "fsMIEcfmRMepRdi": fsMIEcfmRMepRdi,
       "fsMIEcfmRMepPortStatusTlv": fsMIEcfmRMepPortStatusTlv,
       "fsMIEcfmRMepInterfaceStatusTlv": fsMIEcfmRMepInterfaceStatusTlv,
       "fsMIEcfmRMepChassisIdSubtype": fsMIEcfmRMepChassisIdSubtype,
       "fsMIEcfmRMepDbChassisId": fsMIEcfmRMepDbChassisId,
       "fsMIEcfmRMepManAddressDomain": fsMIEcfmRMepManAddressDomain,
       "fsMIEcfmRMepManAddress": fsMIEcfmRMepManAddress,
       "fsMIEcfmLtmTable": fsMIEcfmLtmTable,
       "fsMIEcfmLtmEntry": fsMIEcfmLtmEntry,
       "fsMIEcfmLtmSeqNumber": fsMIEcfmLtmSeqNumber,
       "fsMIEcfmLtmTargetMacAddress": fsMIEcfmLtmTargetMacAddress,
       "fsMIEcfmLtmTtl": fsMIEcfmLtmTtl,
       "fsMIEcfmMepExTable": fsMIEcfmMepExTable,
       "fsMIEcfmMepExEntry": fsMIEcfmMepExEntry,
       "fsMIEcfmXconnRMepId": fsMIEcfmXconnRMepId,
       "fsMIEcfmErrorRMepId": fsMIEcfmErrorRMepId,
       "fsMIEcfmMepDefectRDICcm": fsMIEcfmMepDefectRDICcm,
       "fsMIEcfmMepDefectMacStatus": fsMIEcfmMepDefectMacStatus,
       "fsMIEcfmMepDefectRemoteCcm": fsMIEcfmMepDefectRemoteCcm,
       "fsMIEcfmMepDefectErrorCcm": fsMIEcfmMepDefectErrorCcm,
       "fsMIEcfmMepDefectXconnCcm": fsMIEcfmMepDefectXconnCcm,
       "fsMIEcfmMdExTable": fsMIEcfmMdExTable,
       "fsMIEcfmMdExEntry": fsMIEcfmMdExEntry,
       "fsMIEcfmMepArchiveHoldTime": fsMIEcfmMepArchiveHoldTime,
       "fsMIEcfmMaExTable": fsMIEcfmMaExTable,
       "fsMIEcfmMaExEntry": fsMIEcfmMaExEntry,
       "fsMIEcfmMaCrosscheckStatus": fsMIEcfmMaCrosscheckStatus,
       "fsMIEcfmStatsTable": fsMIEcfmStatsTable,
       "fsMIEcfmStatsEntry": fsMIEcfmStatsEntry,
       "fsMIEcfmTxCfmPduCount": fsMIEcfmTxCfmPduCount,
       "fsMIEcfmTxCcmCount": fsMIEcfmTxCcmCount,
       "fsMIEcfmTxLbmCount": fsMIEcfmTxLbmCount,
       "fsMIEcfmTxLbrCount": fsMIEcfmTxLbrCount,
       "fsMIEcfmTxLtmCount": fsMIEcfmTxLtmCount,
       "fsMIEcfmTxLtrCount": fsMIEcfmTxLtrCount,
       "fsMIEcfmTxFailedCount": fsMIEcfmTxFailedCount,
       "fsMIEcfmRxCfmPduCount": fsMIEcfmRxCfmPduCount,
       "fsMIEcfmRxCcmCount": fsMIEcfmRxCcmCount,
       "fsMIEcfmRxLbmCount": fsMIEcfmRxLbmCount,
       "fsMIEcfmRxLbrCount": fsMIEcfmRxLbrCount,
       "fsMIEcfmRxLtmCount": fsMIEcfmRxLtmCount,
       "fsMIEcfmRxLtrCount": fsMIEcfmRxLtrCount,
       "fsMIEcfmRxBadCfmPduCount": fsMIEcfmRxBadCfmPduCount,
       "fsMIEcfmFrwdCfmPduCount": fsMIEcfmFrwdCfmPduCount,
       "fsMIEcfmDsrdCfmPduCount": fsMIEcfmDsrdCfmPduCount,
       "fsMIEcfmSystem": fsMIEcfmSystem,
       "fsMIEcfmGlobalTrace": fsMIEcfmGlobalTrace,
       "fsMIEcfmOui": fsMIEcfmOui,
       "fsMIEcfmPortTable": fsMIEcfmPortTable,
       "fsMIEcfmPortEntry": fsMIEcfmPortEntry,
       "fsMIEcfmPortIfIndex": fsMIEcfmPortIfIndex,
       "fsMIEcfmPortLLCEncapStatus": fsMIEcfmPortLLCEncapStatus,
       "fsMIEcfmPortModuleStatus": fsMIEcfmPortModuleStatus,
       "fsMIEcfmPortTxCfmPduCount": fsMIEcfmPortTxCfmPduCount,
       "fsMIEcfmPortTxCcmCount": fsMIEcfmPortTxCcmCount,
       "fsMIEcfmPortTxLbmCount": fsMIEcfmPortTxLbmCount,
       "fsMIEcfmPortTxLbrCount": fsMIEcfmPortTxLbrCount,
       "fsMIEcfmPortTxLtmCount": fsMIEcfmPortTxLtmCount,
       "fsMIEcfmPortTxLtrCount": fsMIEcfmPortTxLtrCount,
       "fsMIEcfmPortTxFailedCount": fsMIEcfmPortTxFailedCount,
       "fsMIEcfmPortRxCfmPduCount": fsMIEcfmPortRxCfmPduCount,
       "fsMIEcfmPortRxCcmCount": fsMIEcfmPortRxCcmCount,
       "fsMIEcfmPortRxLbmCount": fsMIEcfmPortRxLbmCount,
       "fsMIEcfmPortRxLbrCount": fsMIEcfmPortRxLbrCount,
       "fsMIEcfmPortRxLtmCount": fsMIEcfmPortRxLtmCount,
       "fsMIEcfmPortRxLtrCount": fsMIEcfmPortRxLtrCount,
       "fsMIEcfmPortRxBadCfmPduCount": fsMIEcfmPortRxBadCfmPduCount,
       "fsMIEcfmPortFrwdCfmPduCount": fsMIEcfmPortFrwdCfmPduCount,
       "fsMIEcfmPortDsrdCfmPduCount": fsMIEcfmPortDsrdCfmPduCount,
       "fsMIEcfmStackTable": fsMIEcfmStackTable,
       "fsMIEcfmStackEntry": fsMIEcfmStackEntry,
       "fsMIEcfmStackIfIndex": fsMIEcfmStackIfIndex,
       "fsMIEcfmStackVlanIdOrNone": fsMIEcfmStackVlanIdOrNone,
       "fsMIEcfmStackMdLevel": fsMIEcfmStackMdLevel,
       "fsMIEcfmStackDirection": fsMIEcfmStackDirection,
       "fsMIEcfmStackMdIndex": fsMIEcfmStackMdIndex,
       "fsMIEcfmStackMaIndex": fsMIEcfmStackMaIndex,
       "fsMIEcfmStackMepId": fsMIEcfmStackMepId,
       "fsMIEcfmStackMacAddress": fsMIEcfmStackMacAddress,
       "fsMIEcfmConfigErrorListTable": fsMIEcfmConfigErrorListTable,
       "fsMIEcfmConfigErrorListEntry": fsMIEcfmConfigErrorListEntry,
       "fsMIEcfmConfigErrorListVid": fsMIEcfmConfigErrorListVid,
       "fsMIEcfmConfigErrorListIfIndex": fsMIEcfmConfigErrorListIfIndex,
       "fsMIEcfmConfigErrorListErrorType": fsMIEcfmConfigErrorListErrorType,
       "fsMIEcfmMipTable": fsMIEcfmMipTable,
       "fsMIEcfmMipEntry": fsMIEcfmMipEntry,
       "fsMIEcfmMipIfIndex": fsMIEcfmMipIfIndex,
       "fsMIEcfmMipMdLevel": fsMIEcfmMipMdLevel,
       "fsMIEcfmMipVid": fsMIEcfmMipVid,
       "fsMIEcfmMipActive": fsMIEcfmMipActive,
       "fsMIEcfmMipRowStatus": fsMIEcfmMipRowStatus,
       "fsMIEcfmDynMipPreventionTable": fsMIEcfmDynMipPreventionTable,
       "fsMIEcfmDynMipPreventionEntry": fsMIEcfmDynMipPreventionEntry,
       "fsMIEcfmDynMipPreventionRowStatus": fsMIEcfmDynMipPreventionRowStatus}
)
