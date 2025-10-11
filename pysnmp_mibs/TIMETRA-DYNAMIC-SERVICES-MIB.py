# SNMP MIB module (TIMETRA-DYNAMIC-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-DYNAMIC-SERVICES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:03:16 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxAuthPassword,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId,
 TmnxSubAcctSessionId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxAuthPassword",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId",
    "TmnxSubAcctSessionId")


# MODULE-IDENTITY

timetraDynSrvMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 84)
)
if mibBuilder.loadTexts:
    timetraDynSrvMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2013-05-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxDynSrvAcctStatsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("volumeTime", 1),
          ("time", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxDynSvcConformance_ObjectIdentity = ObjectIdentity
tmnxDynSvcConformance = _TmnxDynSvcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84)
)
_TmnxDynSvcCompliances_ObjectIdentity = ObjectIdentity
tmnxDynSvcCompliances = _TmnxDynSvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 1)
)
_TmnxDynSvcGroups_ObjectIdentity = ObjectIdentity
tmnxDynSvcGroups = _TmnxDynSvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2)
)
_TmnxDynSvc_ObjectIdentity = ObjectIdentity
tmnxDynSvc = _TmnxDynSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84)
)
_TmnxDynSvcObjs_ObjectIdentity = ObjectIdentity
tmnxDynSvcObjs = _TmnxDynSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1)
)
_TmnxDynSvcPlcyTable_Object = MibTable
tmnxDynSvcPlcyTable = _TmnxDynSvcPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyTable.setStatus("current")
_TmnxDynSvcPlcyEntry_Object = MibTableRow
tmnxDynSvcPlcyEntry = _TmnxDynSvcPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1)
)
tmnxDynSvcPlcyEntry.setIndexNames(
    (1, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyEntry.setStatus("current")
_TmnxDynSvcPlcyName_Type = TNamedItem
_TmnxDynSvcPlcyName_Object = MibTableColumn
tmnxDynSvcPlcyName = _TmnxDynSvcPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 1),
    _TmnxDynSvcPlcyName_Type()
)
tmnxDynSvcPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyName.setStatus("current")
_TmnxDynSvcPlcyRowStatus_Type = RowStatus
_TmnxDynSvcPlcyRowStatus_Object = MibTableColumn
tmnxDynSvcPlcyRowStatus = _TmnxDynSvcPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 2),
    _TmnxDynSvcPlcyRowStatus_Type()
)
tmnxDynSvcPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyRowStatus.setStatus("current")
_TmnxDynSvcPlcyLastCh_Type = TimeStamp
_TmnxDynSvcPlcyLastCh_Object = MibTableColumn
tmnxDynSvcPlcyLastCh = _TmnxDynSvcPlcyLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 3),
    _TmnxDynSvcPlcyLastCh_Type()
)
tmnxDynSvcPlcyLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyLastCh.setStatus("current")


class _TmnxDynSvcPlcyDescription_Type(TItemDescription):
    """Custom type tmnxDynSvcPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxDynSvcPlcyDescription_Object = MibTableColumn
tmnxDynSvcPlcyDescription = _TmnxDynSvcPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 4),
    _TmnxDynSvcPlcyDescription_Type()
)
tmnxDynSvcPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyDescription.setStatus("current")


class _TmnxDynSvcPlcyScriptPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcPlcyScriptPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyScriptPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcPlcyScriptPlcy_Object = MibTableColumn
tmnxDynSvcPlcyScriptPlcy = _TmnxDynSvcPlcyScriptPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 5),
    _TmnxDynSvcPlcyScriptPlcy_Type()
)
tmnxDynSvcPlcyScriptPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyScriptPlcy.setStatus("current")


class _TmnxDynSvcPlcyCliUser_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcPlcyCliUser based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyCliUser_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcPlcyCliUser_Object = MibTableColumn
tmnxDynSvcPlcyCliUser = _TmnxDynSvcPlcyCliUser_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 6),
    _TmnxDynSvcPlcyCliUser_Type()
)
tmnxDynSvcPlcyCliUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyCliUser.setStatus("current")


class _TmnxDynSvcPlcySapLimit_Type(Unsigned32):
    """Custom type tmnxDynSvcPlcySapLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_TmnxDynSvcPlcySapLimit_Type.__name__ = "Unsigned32"
_TmnxDynSvcPlcySapLimit_Object = MibTableColumn
tmnxDynSvcPlcySapLimit = _TmnxDynSvcPlcySapLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 7),
    _TmnxDynSvcPlcySapLimit_Type()
)
tmnxDynSvcPlcySapLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcySapLimit.setStatus("current")
_TmnxDynSvcPlcyApTable_Object = MibTable
tmnxDynSvcPlcyApTable = _TmnxDynSvcPlcyApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApTable.setStatus("current")
_TmnxDynSvcPlcyApEntry_Object = MibTableRow
tmnxDynSvcPlcyApEntry = _TmnxDynSvcPlcyApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1)
)
tmnxDynSvcPlcyApEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApIndex"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApEntry.setStatus("current")


class _TmnxDynSvcPlcyApIndex_Type(Unsigned32):
    """Custom type tmnxDynSvcPlcyApIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxDynSvcPlcyApIndex_Type.__name__ = "Unsigned32"
_TmnxDynSvcPlcyApIndex_Object = MibTableColumn
tmnxDynSvcPlcyApIndex = _TmnxDynSvcPlcyApIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 1),
    _TmnxDynSvcPlcyApIndex_Type()
)
tmnxDynSvcPlcyApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApIndex.setStatus("current")
_TmnxDynSvcPlcyApLastCh_Type = TimeStamp
_TmnxDynSvcPlcyApLastCh_Object = MibTableColumn
tmnxDynSvcPlcyApLastCh = _TmnxDynSvcPlcyApLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 2),
    _TmnxDynSvcPlcyApLastCh_Type()
)
tmnxDynSvcPlcyApLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApLastCh.setStatus("current")


class _TmnxDynSvcPlcyApName_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcPlcyApName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyApName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcPlcyApName_Object = MibTableColumn
tmnxDynSvcPlcyApName = _TmnxDynSvcPlcyApName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 3),
    _TmnxDynSvcPlcyApName_Type()
)
tmnxDynSvcPlcyApName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApName.setStatus("current")


class _TmnxDynSvcPlcyApStatsType_Type(TmnxDynSrvAcctStatsType):
    """Custom type tmnxDynSvcPlcyApStatsType based on TmnxDynSrvAcctStatsType"""
    defaultValue = 1


_TmnxDynSvcPlcyApStatsType_Type.__name__ = "TmnxDynSrvAcctStatsType"
_TmnxDynSvcPlcyApStatsType_Object = MibTableColumn
tmnxDynSvcPlcyApStatsType = _TmnxDynSvcPlcyApStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 4),
    _TmnxDynSvcPlcyApStatsType_Type()
)
tmnxDynSvcPlcyApStatsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApStatsType.setStatus("current")


class _TmnxDynSvcPlcyApUpdateInterval_Type(Unsigned32):
    """Custom type tmnxDynSvcPlcyApUpdateInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 259200),
    )


_TmnxDynSvcPlcyApUpdateInterval_Type.__name__ = "Unsigned32"
_TmnxDynSvcPlcyApUpdateInterval_Object = MibTableColumn
tmnxDynSvcPlcyApUpdateInterval = _TmnxDynSvcPlcyApUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 5),
    _TmnxDynSvcPlcyApUpdateInterval_Type()
)
tmnxDynSvcPlcyApUpdateInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApUpdateInterval.setUnits("minutes")


class _TmnxDynSvcPlcyApUpdateIvlJitter_Type(Integer32):
    """Custom type tmnxDynSvcPlcyApUpdateIvlJitter based on Integer32"""
    defaultValue = -10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, -10),
        ValueRangeConstraint(0, 3600),
    )


_TmnxDynSvcPlcyApUpdateIvlJitter_Type.__name__ = "Integer32"
_TmnxDynSvcPlcyApUpdateIvlJitter_Object = MibTableColumn
tmnxDynSvcPlcyApUpdateIvlJitter = _TmnxDynSvcPlcyApUpdateIvlJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 6),
    _TmnxDynSvcPlcyApUpdateIvlJitter_Type()
)
tmnxDynSvcPlcyApUpdateIvlJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApUpdateIvlJitter.setStatus("current")
_TmnxDynSvcRange_ObjectIdentity = ObjectIdentity
tmnxDynSvcRange = _TmnxDynSvcRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 3)
)


class _TmnxDynSvcRangeStart_Type(TmnxServId):
    """Custom type tmnxDynSvcRangeStart based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxDynSvcRangeStart_Type.__name__ = "TmnxServId"
_TmnxDynSvcRangeStart_Object = MibScalar
tmnxDynSvcRangeStart = _TmnxDynSvcRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 3, 1),
    _TmnxDynSvcRangeStart_Type()
)
tmnxDynSvcRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDynSvcRangeStart.setStatus("current")


class _TmnxDynSvcRangeEnd_Type(TmnxServId):
    """Custom type tmnxDynSvcRangeEnd based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxDynSvcRangeEnd_Type.__name__ = "TmnxServId"
_TmnxDynSvcRangeEnd_Object = MibScalar
tmnxDynSvcRangeEnd = _TmnxDynSvcRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 3, 2),
    _TmnxDynSvcRangeEnd_Type()
)
tmnxDynSvcRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDynSvcRangeEnd.setStatus("current")
_TmnxDynSvcSapTable_Object = MibTable
tmnxDynSvcSapTable = _TmnxDynSvcSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapTable.setStatus("current")
_TmnxDynSvcSapEntry_Object = MibTableRow
tmnxDynSvcSapEntry = _TmnxDynSvcSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1)
)
tmnxDynSvcSapEntry.setIndexNames(
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapEntry.setStatus("current")
_TmnxDynSvcSapAcctSessionId_Type = TmnxSubAcctSessionId
_TmnxDynSvcSapAcctSessionId_Object = MibTableColumn
tmnxDynSvcSapAcctSessionId = _TmnxDynSvcSapAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 1),
    _TmnxDynSvcSapAcctSessionId_Type()
)
tmnxDynSvcSapAcctSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctSessionId.setStatus("current")
_TmnxDynSvcSapAcctSessionIdCtrl_Type = TmnxSubAcctSessionId
_TmnxDynSvcSapAcctSessionIdCtrl_Object = MibTableColumn
tmnxDynSvcSapAcctSessionIdCtrl = _TmnxDynSvcSapAcctSessionIdCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 2),
    _TmnxDynSvcSapAcctSessionIdCtrl_Type()
)
tmnxDynSvcSapAcctSessionIdCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctSessionIdCtrl.setStatus("current")
_TmnxDynSvcSapPolicy_Type = TNamedItemOrEmpty
_TmnxDynSvcSapPolicy_Object = MibTableColumn
tmnxDynSvcSapPolicy = _TmnxDynSvcSapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 3),
    _TmnxDynSvcSapPolicy_Type()
)
tmnxDynSvcSapPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapPolicy.setStatus("current")
_TmnxDynSvcSapScriptsExecuted_Type = Counter32
_TmnxDynSvcSapScriptsExecuted_Object = MibTableColumn
tmnxDynSvcSapScriptsExecuted = _TmnxDynSvcSapScriptsExecuted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 4),
    _TmnxDynSvcSapScriptsExecuted_Type()
)
tmnxDynSvcSapScriptsExecuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapScriptsExecuted.setStatus("current")
_TmnxDynSvcSapScriptsSuccess_Type = Counter32
_TmnxDynSvcSapScriptsSuccess_Object = MibTableColumn
tmnxDynSvcSapScriptsSuccess = _TmnxDynSvcSapScriptsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 5),
    _TmnxDynSvcSapScriptsSuccess_Type()
)
tmnxDynSvcSapScriptsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapScriptsSuccess.setStatus("current")


class _TmnxDynSvcSapLastScriptAction_Type(Integer32):
    """Custom type tmnxDynSvcSapLastScriptAction based on Integer32"""
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
        *(("setup", 1),
          ("modify", 2),
          ("teardown", 3),
          ("commit", 4),
          ("revert", 5))
    )


_TmnxDynSvcSapLastScriptAction_Type.__name__ = "Integer32"
_TmnxDynSvcSapLastScriptAction_Object = MibTableColumn
tmnxDynSvcSapLastScriptAction = _TmnxDynSvcSapLastScriptAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 6),
    _TmnxDynSvcSapLastScriptAction_Type()
)
tmnxDynSvcSapLastScriptAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapLastScriptAction.setStatus("current")


class _TmnxDynSvcSapLastScriptTime_Type(DateAndTime):
    """Custom type tmnxDynSvcSapLastScriptTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxDynSvcSapLastScriptTime_Type.__name__ = "DateAndTime"
_TmnxDynSvcSapLastScriptTime_Object = MibTableColumn
tmnxDynSvcSapLastScriptTime = _TmnxDynSvcSapLastScriptTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 7),
    _TmnxDynSvcSapLastScriptTime_Type()
)
tmnxDynSvcSapLastScriptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapLastScriptTime.setStatus("current")
_TmnxDynSvcSapOrphaned_Type = TruthValue
_TmnxDynSvcSapOrphaned_Object = MibTableColumn
tmnxDynSvcSapOrphaned = _TmnxDynSvcSapOrphaned_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 8),
    _TmnxDynSvcSapOrphaned_Type()
)
tmnxDynSvcSapOrphaned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapOrphaned.setStatus("obsolete")
_TmnxDynSvcSapService_Type = TmnxServId
_TmnxDynSvcSapService_Object = MibTableColumn
tmnxDynSvcSapService = _TmnxDynSvcSapService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 9),
    _TmnxDynSvcSapService_Type()
)
tmnxDynSvcSapService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapService.setStatus("current")


class _TmnxDynSvcSapLastScriptParams_Type(OctetString):
    """Custom type tmnxDynSvcSapLastScriptParams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_TmnxDynSvcSapLastScriptParams_Type.__name__ = "OctetString"
_TmnxDynSvcSapLastScriptParams_Object = MibTableColumn
tmnxDynSvcSapLastScriptParams = _TmnxDynSvcSapLastScriptParams_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 10),
    _TmnxDynSvcSapLastScriptParams_Type()
)
tmnxDynSvcSapLastScriptParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapLastScriptParams.setStatus("current")
_TmnxDynSvcSapAcctTable_Object = MibTable
tmnxDynSvcSapAcctTable = _TmnxDynSvcSapAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctTable.setStatus("current")
_TmnxDynSvcSapAcctEntry_Object = MibTableRow
tmnxDynSvcSapAcctEntry = _TmnxDynSvcSapAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1)
)
tmnxDynSvcSapAcctEntry.setIndexNames(
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctIndex"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctEntry.setStatus("current")


class _TmnxDynSvcSapAcctIndex_Type(Unsigned32):
    """Custom type tmnxDynSvcSapAcctIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxDynSvcSapAcctIndex_Type.__name__ = "Unsigned32"
_TmnxDynSvcSapAcctIndex_Object = MibTableColumn
tmnxDynSvcSapAcctIndex = _TmnxDynSvcSapAcctIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1, 1),
    _TmnxDynSvcSapAcctIndex_Type()
)
tmnxDynSvcSapAcctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctIndex.setStatus("current")
_TmnxDynSvcSapAcctAcctStatus_Type = TmnxEnabledDisabled
_TmnxDynSvcSapAcctAcctStatus_Object = MibTableColumn
tmnxDynSvcSapAcctAcctStatus = _TmnxDynSvcSapAcctAcctStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1, 2),
    _TmnxDynSvcSapAcctAcctStatus_Type()
)
tmnxDynSvcSapAcctAcctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctAcctStatus.setStatus("current")
_TmnxDynSvcSapAcctStatsType_Type = TmnxDynSrvAcctStatsType
_TmnxDynSvcSapAcctStatsType_Object = MibTableColumn
tmnxDynSvcSapAcctStatsType = _TmnxDynSvcSapAcctStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1, 3),
    _TmnxDynSvcSapAcctStatsType_Type()
)
tmnxDynSvcSapAcctStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctStatsType.setStatus("current")
_TmnxDynSvcSapAcctAcctInterval_Type = Unsigned32
_TmnxDynSvcSapAcctAcctInterval_Object = MibTableColumn
tmnxDynSvcSapAcctAcctInterval = _TmnxDynSvcSapAcctAcctInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1, 4),
    _TmnxDynSvcSapAcctAcctInterval_Type()
)
tmnxDynSvcSapAcctAcctInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctAcctInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctAcctInterval.setUnits("minutes")
_TmnxDynSvcRootObjTable_Object = MibTable
tmnxDynSvcRootObjTable = _TmnxDynSvcRootObjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjTable.setStatus("current")
_TmnxDynSvcRootObjEntry_Object = MibTableRow
tmnxDynSvcRootObjEntry = _TmnxDynSvcRootObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1)
)
tmnxDynSvcRootObjEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjIndex"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjEntry.setStatus("current")
_TmnxDynSvcRootObjIndex_Type = Unsigned32
_TmnxDynSvcRootObjIndex_Object = MibTableColumn
tmnxDynSvcRootObjIndex = _TmnxDynSvcRootObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 1),
    _TmnxDynSvcRootObjIndex_Type()
)
tmnxDynSvcRootObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjIndex.setStatus("current")
_TmnxDynSvcRootObjInstance_Type = RowPointer
_TmnxDynSvcRootObjInstance_Object = MibTableColumn
tmnxDynSvcRootObjInstance = _TmnxDynSvcRootObjInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 2),
    _TmnxDynSvcRootObjInstance_Type()
)
tmnxDynSvcRootObjInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjInstance.setStatus("current")
_TmnxDynSvcRootObjOrphanTime_Type = TimeStamp
_TmnxDynSvcRootObjOrphanTime_Object = MibTableColumn
tmnxDynSvcRootObjOrphanTime = _TmnxDynSvcRootObjOrphanTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 3),
    _TmnxDynSvcRootObjOrphanTime_Type()
)
tmnxDynSvcRootObjOrphanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjOrphanTime.setStatus("current")
_TmnxDynSvcRootObjSnippetName_Type = DisplayString
_TmnxDynSvcRootObjSnippetName_Object = MibTableColumn
tmnxDynSvcRootObjSnippetName = _TmnxDynSvcRootObjSnippetName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 4),
    _TmnxDynSvcRootObjSnippetName_Type()
)
tmnxDynSvcRootObjSnippetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjSnippetName.setStatus("current")
_TmnxDynSvcRootObjSnippetInstance_Type = DisplayString
_TmnxDynSvcRootObjSnippetInstance_Object = MibTableColumn
tmnxDynSvcRootObjSnippetInstance = _TmnxDynSvcRootObjSnippetInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 5),
    _TmnxDynSvcRootObjSnippetInstance_Type()
)
tmnxDynSvcRootObjSnippetInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjSnippetInstance.setStatus("current")
_TmnxDynSvcStatsTable_Object = MibTable
tmnxDynSvcStatsTable = _TmnxDynSvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxDynSvcStatsTable.setStatus("current")
_TmnxDynSvcStatsEntry_Object = MibTableRow
tmnxDynSvcStatsEntry = _TmnxDynSvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7, 1)
)
tmnxDynSvcStatsEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsId"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcStatsEntry.setStatus("current")
_TmnxDynSvcStatsId_Type = Unsigned32
_TmnxDynSvcStatsId_Object = MibTableColumn
tmnxDynSvcStatsId = _TmnxDynSvcStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7, 1, 1),
    _TmnxDynSvcStatsId_Type()
)
tmnxDynSvcStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcStatsId.setStatus("current")
_TmnxDynSvcStatsDescr_Type = TItemDescription
_TmnxDynSvcStatsDescr_Object = MibTableColumn
tmnxDynSvcStatsDescr = _TmnxDynSvcStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7, 1, 2),
    _TmnxDynSvcStatsDescr_Type()
)
tmnxDynSvcStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcStatsDescr.setStatus("current")
_TmnxDynSvcStatsVal_Type = Counter32
_TmnxDynSvcStatsVal_Object = MibTableColumn
tmnxDynSvcStatsVal = _TmnxDynSvcStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7, 1, 3),
    _TmnxDynSvcStatsVal_Type()
)
tmnxDynSvcStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcStatsVal.setStatus("current")
_TmnxDynSvcSnippetTable_Object = MibTable
tmnxDynSvcSnippetTable = _TmnxDynSvcSnippetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetTable.setStatus("current")
_TmnxDynSvcSnippetEntry_Object = MibTableRow
tmnxDynSvcSnippetEntry = _TmnxDynSvcSnippetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1)
)
tmnxDynSvcSnippetEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetInstance"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetEntry.setStatus("current")


class _TmnxDynSvcSnippetName_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDynSvcSnippetName_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetName_Object = MibTableColumn
tmnxDynSvcSnippetName = _TmnxDynSvcSnippetName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1, 1),
    _TmnxDynSvcSnippetName_Type()
)
tmnxDynSvcSnippetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetName.setStatus("current")


class _TmnxDynSvcSnippetInstance_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TmnxDynSvcSnippetInstance_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetInstance_Object = MibTableColumn
tmnxDynSvcSnippetInstance = _TmnxDynSvcSnippetInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1, 2),
    _TmnxDynSvcSnippetInstance_Type()
)
tmnxDynSvcSnippetInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetInstance.setStatus("current")
_TmnxDynSvcSnippetRefCount_Type = Counter32
_TmnxDynSvcSnippetRefCount_Object = MibTableColumn
tmnxDynSvcSnippetRefCount = _TmnxDynSvcSnippetRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1, 3),
    _TmnxDynSvcSnippetRefCount_Type()
)
tmnxDynSvcSnippetRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefCount.setStatus("current")
_TmnxDynSvcSnippetDictLength_Type = Unsigned32
_TmnxDynSvcSnippetDictLength_Object = MibTableColumn
tmnxDynSvcSnippetDictLength = _TmnxDynSvcSnippetDictLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1, 4),
    _TmnxDynSvcSnippetDictLength_Type()
)
tmnxDynSvcSnippetDictLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetDictLength.setStatus("current")
_TmnxDynSvcSnippetRootObjTable_Object = MibTable
tmnxDynSvcSnippetRootObjTable = _TmnxDynSvcSnippetRootObjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRootObjTable.setStatus("current")
_TmnxDynSvcSnippetRootObjEntry_Object = MibTableRow
tmnxDynSvcSnippetRootObjEntry = _TmnxDynSvcSnippetRootObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 9, 1)
)
tmnxDynSvcSnippetRootObjEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetInstance"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRootObjIdx"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRootObjEntry.setStatus("current")
_TmnxDynSvcSnippetRootObjIdx_Type = Unsigned32
_TmnxDynSvcSnippetRootObjIdx_Object = MibTableColumn
tmnxDynSvcSnippetRootObjIdx = _TmnxDynSvcSnippetRootObjIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 9, 1, 1),
    _TmnxDynSvcSnippetRootObjIdx_Type()
)
tmnxDynSvcSnippetRootObjIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRootObjIdx.setStatus("current")
_TmnxDynSvcSnippetRootObjOid_Type = RowPointer
_TmnxDynSvcSnippetRootObjOid_Object = MibTableColumn
tmnxDynSvcSnippetRootObjOid = _TmnxDynSvcSnippetRootObjOid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 9, 1, 2),
    _TmnxDynSvcSnippetRootObjOid_Type()
)
tmnxDynSvcSnippetRootObjOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRootObjOid.setStatus("current")
_TmnxDynSvcSnippetRefTable_Object = MibTable
tmnxDynSvcSnippetRefTable = _TmnxDynSvcSnippetRefTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefTable.setStatus("current")
_TmnxDynSvcSnippetRefEntry_Object = MibTableRow
tmnxDynSvcSnippetRefEntry = _TmnxDynSvcSnippetRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10, 1)
)
tmnxDynSvcSnippetRefEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetInstance"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefIdx"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefEntry.setStatus("current")
_TmnxDynSvcSnippetRefIdx_Type = Unsigned32
_TmnxDynSvcSnippetRefIdx_Object = MibTableColumn
tmnxDynSvcSnippetRefIdx = _TmnxDynSvcSnippetRefIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10, 1, 1),
    _TmnxDynSvcSnippetRefIdx_Type()
)
tmnxDynSvcSnippetRefIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefIdx.setStatus("current")


class _TmnxDynSvcSnippetRefSnipName_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetRefSnipName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDynSvcSnippetRefSnipName_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetRefSnipName_Object = MibTableColumn
tmnxDynSvcSnippetRefSnipName = _TmnxDynSvcSnippetRefSnipName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10, 1, 2),
    _TmnxDynSvcSnippetRefSnipName_Type()
)
tmnxDynSvcSnippetRefSnipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefSnipName.setStatus("current")


class _TmnxDynSvcSnippetRefSnipInst_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetRefSnipInst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TmnxDynSvcSnippetRefSnipInst_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetRefSnipInst_Object = MibTableColumn
tmnxDynSvcSnippetRefSnipInst = _TmnxDynSvcSnippetRefSnipInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10, 1, 3),
    _TmnxDynSvcSnippetRefSnipInst_Type()
)
tmnxDynSvcSnippetRefSnipInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefSnipInst.setStatus("current")
_TmnxDynSvcSnippetResIdTable_Object = MibTable
tmnxDynSvcSnippetResIdTable = _TmnxDynSvcSnippetResIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdTable.setStatus("current")
_TmnxDynSvcSnippetResIdEntry_Object = MibTableRow
tmnxDynSvcSnippetResIdEntry = _TmnxDynSvcSnippetResIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11, 1)
)
tmnxDynSvcSnippetResIdEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetInstance"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdIdx"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdEntry.setStatus("current")
_TmnxDynSvcSnippetResIdIdx_Type = Unsigned32
_TmnxDynSvcSnippetResIdIdx_Object = MibTableColumn
tmnxDynSvcSnippetResIdIdx = _TmnxDynSvcSnippetResIdIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11, 1, 1),
    _TmnxDynSvcSnippetResIdIdx_Type()
)
tmnxDynSvcSnippetResIdIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdIdx.setStatus("current")


class _TmnxDynSvcSnippetResIdType_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetResIdType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDynSvcSnippetResIdType_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetResIdType_Object = MibTableColumn
tmnxDynSvcSnippetResIdType = _TmnxDynSvcSnippetResIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11, 1, 2),
    _TmnxDynSvcSnippetResIdType_Type()
)
tmnxDynSvcSnippetResIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdType.setStatus("current")


class _TmnxDynSvcSnippetResIdValue_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetResIdValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TmnxDynSvcSnippetResIdValue_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetResIdValue_Object = MibTableColumn
tmnxDynSvcSnippetResIdValue = _TmnxDynSvcSnippetResIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11, 1, 3),
    _TmnxDynSvcSnippetResIdValue_Type()
)
tmnxDynSvcSnippetResIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdValue.setStatus("current")
_TmnxDynSvcTimer_ObjectIdentity = ObjectIdentity
tmnxDynSvcTimer = _TmnxDynSvcTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 12)
)


class _TmnxDynSvcTimerAccSetupTimeout_Type(Unsigned32):
    """Custom type tmnxDynSvcTimerAccSetupTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_TmnxDynSvcTimerAccSetupTimeout_Type.__name__ = "Unsigned32"
_TmnxDynSvcTimerAccSetupTimeout_Object = MibScalar
tmnxDynSvcTimerAccSetupTimeout = _TmnxDynSvcTimerAccSetupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 12, 1),
    _TmnxDynSvcTimerAccSetupTimeout_Type()
)
tmnxDynSvcTimerAccSetupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDynSvcTimerAccSetupTimeout.setStatus("current")
_TmnxDynSvcPlcyAuthTable_Object = MibTable
tmnxDynSvcPlcyAuthTable = _TmnxDynSvcPlcyAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyAuthTable.setStatus("current")
_TmnxDynSvcPlcyAuthEntry_Object = MibTableRow
tmnxDynSvcPlcyAuthEntry = _TmnxDynSvcPlcyAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 13, 1)
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyAuthEntry.setStatus("current")
_TmnxDynSvcPlcyAuthLastCh_Type = TimeStamp
_TmnxDynSvcPlcyAuthLastCh_Object = MibTableColumn
tmnxDynSvcPlcyAuthLastCh = _TmnxDynSvcPlcyAuthLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 13, 1, 1),
    _TmnxDynSvcPlcyAuthLastCh_Type()
)
tmnxDynSvcPlcyAuthLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyAuthLastCh.setStatus("current")


class _TmnxDynSvcPlcyAuthRadiusSrvPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcPlcyAuthRadiusSrvPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyAuthRadiusSrvPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcPlcyAuthRadiusSrvPlcy_Object = MibTableColumn
tmnxDynSvcPlcyAuthRadiusSrvPlcy = _TmnxDynSvcPlcyAuthRadiusSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 13, 1, 2),
    _TmnxDynSvcPlcyAuthRadiusSrvPlcy_Type()
)
tmnxDynSvcPlcyAuthRadiusSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyAuthRadiusSrvPlcy.setStatus("current")


class _TmnxDynSvcPlcyAuthPassword_Type(TmnxAuthPassword):
    """Custom type tmnxDynSvcPlcyAuthPassword based on TmnxAuthPassword"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyAuthPassword_Type.__name__ = "TmnxAuthPassword"
_TmnxDynSvcPlcyAuthPassword_Object = MibTableColumn
tmnxDynSvcPlcyAuthPassword = _TmnxDynSvcPlcyAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 13, 1, 3),
    _TmnxDynSvcPlcyAuthPassword_Type()
)
tmnxDynSvcPlcyAuthPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyAuthPassword.setStatus("current")


class _TmnxDynSvcPlcyAuthLocalDb_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcPlcyAuthLocalDb based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyAuthLocalDb_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcPlcyAuthLocalDb_Object = MibTableColumn
tmnxDynSvcPlcyAuthLocalDb = _TmnxDynSvcPlcyAuthLocalDb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 13, 1, 4),
    _TmnxDynSvcPlcyAuthLocalDb_Type()
)
tmnxDynSvcPlcyAuthLocalDb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyAuthLocalDb.setStatus("current")
_TmnxDynSvcCaptureSapTable_Object = MibTable
tmnxDynSvcCaptureSapTable = _TmnxDynSvcCaptureSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapTable.setStatus("current")
_TmnxDynSvcCaptureSapEntry_Object = MibTableRow
tmnxDynSvcCaptureSapEntry = _TmnxDynSvcCaptureSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 14, 1)
)
tmnxDynSvcCaptureSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapEntry.setStatus("current")
_TmnxDynSvcCaptureSapLastCh_Type = TimeStamp
_TmnxDynSvcCaptureSapLastCh_Object = MibTableColumn
tmnxDynSvcCaptureSapLastCh = _TmnxDynSvcCaptureSapLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 14, 1, 1),
    _TmnxDynSvcCaptureSapLastCh_Type()
)
tmnxDynSvcCaptureSapLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapLastCh.setStatus("current")


class _TmnxDynSvcCaptureSapAdminState_Type(TmnxAdminState):
    """Custom type tmnxDynSvcCaptureSapAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxDynSvcCaptureSapAdminState_Type.__name__ = "TmnxAdminState"
_TmnxDynSvcCaptureSapAdminState_Object = MibTableColumn
tmnxDynSvcCaptureSapAdminState = _TmnxDynSvcCaptureSapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 14, 1, 2),
    _TmnxDynSvcCaptureSapAdminState_Type()
)
tmnxDynSvcCaptureSapAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapAdminState.setStatus("current")


class _TmnxDynSvcCaptureSapPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcCaptureSapPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcCaptureSapPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcCaptureSapPolicy_Object = MibTableColumn
tmnxDynSvcCaptureSapPolicy = _TmnxDynSvcCaptureSapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 14, 1, 3),
    _TmnxDynSvcCaptureSapPolicy_Type()
)
tmnxDynSvcCaptureSapPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapPolicy.setStatus("current")
_TmnxDynSvcCaptureSapStatsTable_Object = MibTable
tmnxDynSvcCaptureSapStatsTable = _TmnxDynSvcCaptureSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapStatsTable.setStatus("current")
_TmnxDynSvcCaptureSapStatsEntry_Object = MibTableRow
tmnxDynSvcCaptureSapStatsEntry = _TmnxDynSvcCaptureSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 15, 1)
)
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapStatsEntry.setStatus("current")
_TmnxDynSvcCSapStatsRxPackets_Type = Counter32
_TmnxDynSvcCSapStatsRxPackets_Object = MibTableColumn
tmnxDynSvcCSapStatsRxPackets = _TmnxDynSvcCSapStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 15, 1, 1),
    _TmnxDynSvcCSapStatsRxPackets_Type()
)
tmnxDynSvcCSapStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcCSapStatsRxPackets.setStatus("current")
_TmnxDynSvcCaptureSapDropTable_Object = MibTable
tmnxDynSvcCaptureSapDropTable = _TmnxDynSvcCaptureSapDropTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapDropTable.setStatus("current")
_TmnxDynSvcCaptureSapDropEntry_Object = MibTableRow
tmnxDynSvcCaptureSapDropEntry = _TmnxDynSvcCaptureSapDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 16, 1)
)
tmnxDynSvcCaptureSapDropEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcCSapDropIndex"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapDropEntry.setStatus("current")


class _TmnxDynSvcCSapDropIndex_Type(Unsigned32):
    """Custom type tmnxDynSvcCSapDropIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TmnxDynSvcCSapDropIndex_Type.__name__ = "Unsigned32"
_TmnxDynSvcCSapDropIndex_Object = MibTableColumn
tmnxDynSvcCSapDropIndex = _TmnxDynSvcCSapDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 16, 1, 1),
    _TmnxDynSvcCSapDropIndex_Type()
)
tmnxDynSvcCSapDropIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcCSapDropIndex.setStatus("current")


class _TmnxDynSvcCSapDropReason_Type(DisplayString):
    """Custom type tmnxDynSvcCSapDropReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxDynSvcCSapDropReason_Type.__name__ = "DisplayString"
_TmnxDynSvcCSapDropReason_Object = MibTableColumn
tmnxDynSvcCSapDropReason = _TmnxDynSvcCSapDropReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 16, 1, 2),
    _TmnxDynSvcCSapDropReason_Type()
)
tmnxDynSvcCSapDropReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcCSapDropReason.setStatus("current")
_TmnxDynSvcCSapDropCounter_Type = Counter32
_TmnxDynSvcCSapDropCounter_Object = MibTableColumn
tmnxDynSvcCSapDropCounter = _TmnxDynSvcCSapDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 16, 1, 3),
    _TmnxDynSvcCSapDropCounter_Type()
)
tmnxDynSvcCSapDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcCSapDropCounter.setStatus("current")
_TmnxDynSvcDataTriggerTable_Object = MibTable
tmnxDynSvcDataTriggerTable = _TmnxDynSvcDataTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxDynSvcDataTriggerTable.setStatus("current")
_TmnxDynSvcDataTriggerEntry_Object = MibTableRow
tmnxDynSvcDataTriggerEntry = _TmnxDynSvcDataTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 17, 1)
)
tmnxDynSvcDataTriggerEntry.setIndexNames(
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcDataTriggerEntry.setStatus("current")
_TmnxDynSvcDTriggerAcctSessionId_Type = TmnxSubAcctSessionId
_TmnxDynSvcDTriggerAcctSessionId_Object = MibTableColumn
tmnxDynSvcDTriggerAcctSessionId = _TmnxDynSvcDTriggerAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 17, 1, 1),
    _TmnxDynSvcDTriggerAcctSessionId_Type()
)
tmnxDynSvcDTriggerAcctSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcDTriggerAcctSessionId.setStatus("current")
_TmnxDynSvcDTriggerMacAddress_Type = MacAddress
_TmnxDynSvcDTriggerMacAddress_Object = MibTableColumn
tmnxDynSvcDTriggerMacAddress = _TmnxDynSvcDTriggerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 17, 1, 2),
    _TmnxDynSvcDTriggerMacAddress_Type()
)
tmnxDynSvcDTriggerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcDTriggerMacAddress.setStatus("current")
_TmnxDynSvcDTriggerIpAddressType_Type = InetAddressType
_TmnxDynSvcDTriggerIpAddressType_Object = MibTableColumn
tmnxDynSvcDTriggerIpAddressType = _TmnxDynSvcDTriggerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 17, 1, 3),
    _TmnxDynSvcDTriggerIpAddressType_Type()
)
tmnxDynSvcDTriggerIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcDTriggerIpAddressType.setStatus("current")


class _TmnxDynSvcDTriggerIpAddress_Type(InetAddress):
    """Custom type tmnxDynSvcDTriggerIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDynSvcDTriggerIpAddress_Type.__name__ = "InetAddress"
_TmnxDynSvcDTriggerIpAddress_Object = MibTableColumn
tmnxDynSvcDTriggerIpAddress = _TmnxDynSvcDTriggerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 17, 1, 4),
    _TmnxDynSvcDTriggerIpAddress_Type()
)
tmnxDynSvcDTriggerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcDTriggerIpAddress.setStatus("current")


class _TmnxDynSvcDTriggerState_Type(Integer32):
    """Custom type tmnxDynSvcDTriggerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pending", 1),
          ("accepted", 2),
          ("sapCreated", 3))
    )


_TmnxDynSvcDTriggerState_Type.__name__ = "Integer32"
_TmnxDynSvcDTriggerState_Object = MibTableColumn
tmnxDynSvcDTriggerState = _TmnxDynSvcDTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 17, 1, 5),
    _TmnxDynSvcDTriggerState_Type()
)
tmnxDynSvcDTriggerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcDTriggerState.setStatus("current")
_TmnxDynSvcLocalAuthDbTable_Object = MibTable
tmnxDynSvcLocalAuthDbTable = _TmnxDynSvcLocalAuthDbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxDynSvcLocalAuthDbTable.setStatus("current")
_TmnxDynSvcLocalAuthDbEntry_Object = MibTableRow
tmnxDynSvcLocalAuthDbEntry = _TmnxDynSvcLocalAuthDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 18, 1)
)
tmnxDynSvcLocalAuthDbEntry.setIndexNames(
    (1, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocAuthDbName"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcLocalAuthDbEntry.setStatus("current")
_TmnxDynSvcLocAuthDbName_Type = TNamedItem
_TmnxDynSvcLocAuthDbName_Object = MibTableColumn
tmnxDynSvcLocAuthDbName = _TmnxDynSvcLocAuthDbName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 18, 1, 1),
    _TmnxDynSvcLocAuthDbName_Type()
)
tmnxDynSvcLocAuthDbName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcLocAuthDbName.setStatus("current")
_TmnxDynSvcLocAuthDbRowStatus_Type = RowStatus
_TmnxDynSvcLocAuthDbRowStatus_Object = MibTableColumn
tmnxDynSvcLocAuthDbRowStatus = _TmnxDynSvcLocAuthDbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 18, 1, 2),
    _TmnxDynSvcLocAuthDbRowStatus_Type()
)
tmnxDynSvcLocAuthDbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocAuthDbRowStatus.setStatus("current")
_TmnxDynSvcLocAuthDbLastCh_Type = TimeStamp
_TmnxDynSvcLocAuthDbLastCh_Object = MibTableColumn
tmnxDynSvcLocAuthDbLastCh = _TmnxDynSvcLocAuthDbLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 18, 1, 3),
    _TmnxDynSvcLocAuthDbLastCh_Type()
)
tmnxDynSvcLocAuthDbLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcLocAuthDbLastCh.setStatus("current")


class _TmnxDynSvcLocAuthDbAdminState_Type(TmnxAdminState):
    """Custom type tmnxDynSvcLocAuthDbAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxDynSvcLocAuthDbAdminState_Type.__name__ = "TmnxAdminState"
_TmnxDynSvcLocAuthDbAdminState_Object = MibTableColumn
tmnxDynSvcLocAuthDbAdminState = _TmnxDynSvcLocAuthDbAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 18, 1, 4),
    _TmnxDynSvcLocAuthDbAdminState_Type()
)
tmnxDynSvcLocAuthDbAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocAuthDbAdminState.setStatus("current")


class _TmnxDynSvcLocAuthDbDescription_Type(TItemDescription):
    """Custom type tmnxDynSvcLocAuthDbDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDynSvcLocAuthDbDescription_Type.__name__ = "TItemDescription"
_TmnxDynSvcLocAuthDbDescription_Object = MibTableColumn
tmnxDynSvcLocAuthDbDescription = _TmnxDynSvcLocAuthDbDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 18, 1, 5),
    _TmnxDynSvcLocAuthDbDescription_Type()
)
tmnxDynSvcLocAuthDbDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocAuthDbDescription.setStatus("current")
_TmnxDynSvcLocalAuthDbUserTable_Object = MibTable
tmnxDynSvcLocalAuthDbUserTable = _TmnxDynSvcLocalAuthDbUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxDynSvcLocalAuthDbUserTable.setStatus("current")
_TmnxDynSvcLocalAuthDbUserEntry_Object = MibTableRow
tmnxDynSvcLocalAuthDbUserEntry = _TmnxDynSvcLocalAuthDbUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 19, 1)
)
tmnxDynSvcLocalAuthDbUserEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocAuthDbName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbUsrName"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcLocalAuthDbUserEntry.setStatus("current")


class _TmnxDynSvcLocADbUsrName_Type(DisplayString):
    """Custom type tmnxDynSvcLocADbUsrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxDynSvcLocADbUsrName_Type.__name__ = "DisplayString"
_TmnxDynSvcLocADbUsrName_Object = MibTableColumn
tmnxDynSvcLocADbUsrName = _TmnxDynSvcLocADbUsrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 19, 1, 1),
    _TmnxDynSvcLocADbUsrName_Type()
)
tmnxDynSvcLocADbUsrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbUsrName.setStatus("current")
_TmnxDynSvcLocADbUsrRowStatus_Type = RowStatus
_TmnxDynSvcLocADbUsrRowStatus_Object = MibTableColumn
tmnxDynSvcLocADbUsrRowStatus = _TmnxDynSvcLocADbUsrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 19, 1, 2),
    _TmnxDynSvcLocADbUsrRowStatus_Type()
)
tmnxDynSvcLocADbUsrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbUsrRowStatus.setStatus("current")
_TmnxDynSvcLocADbUsrLastCh_Type = TimeStamp
_TmnxDynSvcLocADbUsrLastCh_Object = MibTableColumn
tmnxDynSvcLocADbUsrLastCh = _TmnxDynSvcLocADbUsrLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 19, 1, 3),
    _TmnxDynSvcLocADbUsrLastCh_Type()
)
tmnxDynSvcLocADbUsrLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbUsrLastCh.setStatus("current")


class _TmnxDynSvcLocADbUsrAdminState_Type(TmnxAdminState):
    """Custom type tmnxDynSvcLocADbUsrAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxDynSvcLocADbUsrAdminState_Type.__name__ = "TmnxAdminState"
_TmnxDynSvcLocADbUsrAdminState_Object = MibTableColumn
tmnxDynSvcLocADbUsrAdminState = _TmnxDynSvcLocADbUsrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 19, 1, 4),
    _TmnxDynSvcLocADbUsrAdminState_Type()
)
tmnxDynSvcLocADbUsrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbUsrAdminState.setStatus("current")


class _TmnxDynSvcLocADbUsrDescription_Type(TItemDescription):
    """Custom type tmnxDynSvcLocADbUsrDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDynSvcLocADbUsrDescription_Type.__name__ = "TItemDescription"
_TmnxDynSvcLocADbUsrDescription_Object = MibTableColumn
tmnxDynSvcLocADbUsrDescription = _TmnxDynSvcLocADbUsrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 19, 1, 5),
    _TmnxDynSvcLocADbUsrDescription_Type()
)
tmnxDynSvcLocADbUsrDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbUsrDescription.setStatus("current")
_TmnxDynSvcLocalAuthDbSapTable_Object = MibTable
tmnxDynSvcLocalAuthDbSapTable = _TmnxDynSvcLocalAuthDbSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxDynSvcLocalAuthDbSapTable.setStatus("current")
_TmnxDynSvcLocalAuthDbSapEntry_Object = MibTableRow
tmnxDynSvcLocalAuthDbSapEntry = _TmnxDynSvcLocalAuthDbSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1)
)
tmnxDynSvcLocalAuthDbSapEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocAuthDbName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbUsrName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapIndex"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcLocalAuthDbSapEntry.setStatus("current")


class _TmnxDynSvcLocADbSapIndex_Type(Unsigned32):
    """Custom type tmnxDynSvcLocADbSapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxDynSvcLocADbSapIndex_Type.__name__ = "Unsigned32"
_TmnxDynSvcLocADbSapIndex_Object = MibTableColumn
tmnxDynSvcLocADbSapIndex = _TmnxDynSvcLocADbSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1, 1),
    _TmnxDynSvcLocADbSapIndex_Type()
)
tmnxDynSvcLocADbSapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapIndex.setStatus("current")
_TmnxDynSvcLocADbSapRowStatus_Type = RowStatus
_TmnxDynSvcLocADbSapRowStatus_Object = MibTableColumn
tmnxDynSvcLocADbSapRowStatus = _TmnxDynSvcLocADbSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1, 2),
    _TmnxDynSvcLocADbSapRowStatus_Type()
)
tmnxDynSvcLocADbSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapRowStatus.setStatus("current")
_TmnxDynSvcLocADbSapLastCh_Type = TimeStamp
_TmnxDynSvcLocADbSapLastCh_Object = MibTableColumn
tmnxDynSvcLocADbSapLastCh = _TmnxDynSvcLocADbSapLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1, 3),
    _TmnxDynSvcLocADbSapLastCh_Type()
)
tmnxDynSvcLocADbSapLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapLastCh.setStatus("current")


class _TmnxDynSvcLocADbSapSapId_Type(DisplayString):
    """Custom type tmnxDynSvcLocADbSapSapId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxDynSvcLocADbSapSapId_Type.__name__ = "DisplayString"
_TmnxDynSvcLocADbSapSapId_Object = MibTableColumn
tmnxDynSvcLocADbSapSapId = _TmnxDynSvcLocADbSapSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1, 4),
    _TmnxDynSvcLocADbSapSapId_Type()
)
tmnxDynSvcLocADbSapSapId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapSapId.setStatus("current")


class _TmnxDynSvcLocADbSapPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcLocADbSapPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcLocADbSapPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcLocADbSapPolicy_Object = MibTableColumn
tmnxDynSvcLocADbSapPolicy = _TmnxDynSvcLocADbSapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1, 5),
    _TmnxDynSvcLocADbSapPolicy_Type()
)
tmnxDynSvcLocADbSapPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapPolicy.setStatus("current")


class _TmnxDynSvcLocADbSapScriptParams1_Type(DisplayString):
    """Custom type tmnxDynSvcLocADbSapScriptParams1 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TmnxDynSvcLocADbSapScriptParams1_Type.__name__ = "DisplayString"
_TmnxDynSvcLocADbSapScriptParams1_Object = MibTableColumn
tmnxDynSvcLocADbSapScriptParams1 = _TmnxDynSvcLocADbSapScriptParams1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1, 6),
    _TmnxDynSvcLocADbSapScriptParams1_Type()
)
tmnxDynSvcLocADbSapScriptParams1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapScriptParams1.setStatus("current")


class _TmnxDynSvcLocADbSapScriptParams2_Type(DisplayString):
    """Custom type tmnxDynSvcLocADbSapScriptParams2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TmnxDynSvcLocADbSapScriptParams2_Type.__name__ = "DisplayString"
_TmnxDynSvcLocADbSapScriptParams2_Object = MibTableColumn
tmnxDynSvcLocADbSapScriptParams2 = _TmnxDynSvcLocADbSapScriptParams2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1, 7),
    _TmnxDynSvcLocADbSapScriptParams2_Type()
)
tmnxDynSvcLocADbSapScriptParams2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapScriptParams2.setStatus("current")


class _TmnxDynSvcLocADbSapScriptParams3_Type(DisplayString):
    """Custom type tmnxDynSvcLocADbSapScriptParams3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TmnxDynSvcLocADbSapScriptParams3_Type.__name__ = "DisplayString"
_TmnxDynSvcLocADbSapScriptParams3_Object = MibTableColumn
tmnxDynSvcLocADbSapScriptParams3 = _TmnxDynSvcLocADbSapScriptParams3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1, 8),
    _TmnxDynSvcLocADbSapScriptParams3_Type()
)
tmnxDynSvcLocADbSapScriptParams3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapScriptParams3.setStatus("current")


class _TmnxDynSvcLocADbSapScriptParams4_Type(DisplayString):
    """Custom type tmnxDynSvcLocADbSapScriptParams4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TmnxDynSvcLocADbSapScriptParams4_Type.__name__ = "DisplayString"
_TmnxDynSvcLocADbSapScriptParams4_Object = MibTableColumn
tmnxDynSvcLocADbSapScriptParams4 = _TmnxDynSvcLocADbSapScriptParams4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 20, 1, 9),
    _TmnxDynSvcLocADbSapScriptParams4_Type()
)
tmnxDynSvcLocADbSapScriptParams4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapScriptParams4.setStatus("current")
_TmnxDynSvcLocalAuthDbAcctTable_Object = MibTable
tmnxDynSvcLocalAuthDbAcctTable = _TmnxDynSvcLocalAuthDbAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 21)
)
if mibBuilder.loadTexts:
    tmnxDynSvcLocalAuthDbAcctTable.setStatus("current")
_TmnxDynSvcLocalAuthDbAcctEntry_Object = MibTableRow
tmnxDynSvcLocalAuthDbAcctEntry = _TmnxDynSvcLocalAuthDbAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 21, 1)
)
tmnxDynSvcLocalAuthDbAcctEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocAuthDbName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbUsrName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapIndex"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbAcctIndex"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcLocalAuthDbAcctEntry.setStatus("current")


class _TmnxDynSvcLocADbAcctIndex_Type(Unsigned32):
    """Custom type tmnxDynSvcLocADbAcctIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxDynSvcLocADbAcctIndex_Type.__name__ = "Unsigned32"
_TmnxDynSvcLocADbAcctIndex_Object = MibTableColumn
tmnxDynSvcLocADbAcctIndex = _TmnxDynSvcLocADbAcctIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 21, 1, 1),
    _TmnxDynSvcLocADbAcctIndex_Type()
)
tmnxDynSvcLocADbAcctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbAcctIndex.setStatus("current")
_TmnxDynSvcLocADbAcctRowStatus_Type = RowStatus
_TmnxDynSvcLocADbAcctRowStatus_Object = MibTableColumn
tmnxDynSvcLocADbAcctRowStatus = _TmnxDynSvcLocADbAcctRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 21, 1, 2),
    _TmnxDynSvcLocADbAcctRowStatus_Type()
)
tmnxDynSvcLocADbAcctRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbAcctRowStatus.setStatus("current")
_TmnxDynSvcLocADbAcctLastCh_Type = TimeStamp
_TmnxDynSvcLocADbAcctLastCh_Object = MibTableColumn
tmnxDynSvcLocADbAcctLastCh = _TmnxDynSvcLocADbAcctLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 21, 1, 3),
    _TmnxDynSvcLocADbAcctLastCh_Type()
)
tmnxDynSvcLocADbAcctLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbAcctLastCh.setStatus("current")


class _TmnxDynSvcLocADbAcctStatsType_Type(Integer32):
    """Custom type tmnxDynSvcLocADbAcctStatsType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("volumeTime", 2),
          ("time", 3))
    )


_TmnxDynSvcLocADbAcctStatsType_Type.__name__ = "Integer32"
_TmnxDynSvcLocADbAcctStatsType_Object = MibTableColumn
tmnxDynSvcLocADbAcctStatsType = _TmnxDynSvcLocADbAcctStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 21, 1, 4),
    _TmnxDynSvcLocADbAcctStatsType_Type()
)
tmnxDynSvcLocADbAcctStatsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbAcctStatsType.setStatus("current")


class _TmnxDynSvcLocADbAcctUpdateIvl_Type(Unsigned32):
    """Custom type tmnxDynSvcLocADbAcctUpdateIvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 259200),
    )


_TmnxDynSvcLocADbAcctUpdateIvl_Type.__name__ = "Unsigned32"
_TmnxDynSvcLocADbAcctUpdateIvl_Object = MibTableColumn
tmnxDynSvcLocADbAcctUpdateIvl = _TmnxDynSvcLocADbAcctUpdateIvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 21, 1, 5),
    _TmnxDynSvcLocADbAcctUpdateIvl_Type()
)
tmnxDynSvcLocADbAcctUpdateIvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbAcctUpdateIvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbAcctUpdateIvl.setUnits("minutes")
_TmnxDynSvcPlcyTableLastCh_Type = TimeStamp
_TmnxDynSvcPlcyTableLastCh_Object = MibScalar
tmnxDynSvcPlcyTableLastCh = _TmnxDynSvcPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 100),
    _TmnxDynSvcPlcyTableLastCh_Type()
)
tmnxDynSvcPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyTableLastCh.setStatus("current")
_TmnxDynSvcPlcyApTableLastCh_Type = TimeStamp
_TmnxDynSvcPlcyApTableLastCh_Object = MibScalar
tmnxDynSvcPlcyApTableLastCh = _TmnxDynSvcPlcyApTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 101),
    _TmnxDynSvcPlcyApTableLastCh_Type()
)
tmnxDynSvcPlcyApTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApTableLastCh.setStatus("current")
_TmnxDynSvcSapTableLastCh_Type = TimeStamp
_TmnxDynSvcSapTableLastCh_Object = MibScalar
tmnxDynSvcSapTableLastCh = _TmnxDynSvcSapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 102),
    _TmnxDynSvcSapTableLastCh_Type()
)
tmnxDynSvcSapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapTableLastCh.setStatus("current")
_TmnxDynSvcRootObjTableLastCh_Type = TimeStamp
_TmnxDynSvcRootObjTableLastCh_Object = MibScalar
tmnxDynSvcRootObjTableLastCh = _TmnxDynSvcRootObjTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 103),
    _TmnxDynSvcRootObjTableLastCh_Type()
)
tmnxDynSvcRootObjTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjTableLastCh.setStatus("current")
_TmnxDynSvcNonStoredRootObjCount_Type = Counter32
_TmnxDynSvcNonStoredRootObjCount_Object = MibScalar
tmnxDynSvcNonStoredRootObjCount = _TmnxDynSvcNonStoredRootObjCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 104),
    _TmnxDynSvcNonStoredRootObjCount_Type()
)
tmnxDynSvcNonStoredRootObjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcNonStoredRootObjCount.setStatus("current")
_TmnxDynSvcSnippetTableLastCh_Type = TimeStamp
_TmnxDynSvcSnippetTableLastCh_Object = MibScalar
tmnxDynSvcSnippetTableLastCh = _TmnxDynSvcSnippetTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 105),
    _TmnxDynSvcSnippetTableLastCh_Type()
)
tmnxDynSvcSnippetTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetTableLastCh.setStatus("current")
_TmnxDynSvcSnipRootObjTblLastCh_Type = TimeStamp
_TmnxDynSvcSnipRootObjTblLastCh_Object = MibScalar
tmnxDynSvcSnipRootObjTblLastCh = _TmnxDynSvcSnipRootObjTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 106),
    _TmnxDynSvcSnipRootObjTblLastCh_Type()
)
tmnxDynSvcSnipRootObjTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnipRootObjTblLastCh.setStatus("current")
_TmnxDynSvcSnippetRefTableLastCh_Type = TimeStamp
_TmnxDynSvcSnippetRefTableLastCh_Object = MibScalar
tmnxDynSvcSnippetRefTableLastCh = _TmnxDynSvcSnippetRefTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 107),
    _TmnxDynSvcSnippetRefTableLastCh_Type()
)
tmnxDynSvcSnippetRefTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefTableLastCh.setStatus("current")
_TmnxDynSvcSnippetResIdTblLastCh_Type = TimeStamp
_TmnxDynSvcSnippetResIdTblLastCh_Object = MibScalar
tmnxDynSvcSnippetResIdTblLastCh = _TmnxDynSvcSnippetResIdTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 108),
    _TmnxDynSvcSnippetResIdTblLastCh_Type()
)
tmnxDynSvcSnippetResIdTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdTblLastCh.setStatus("current")
_TmnxDynSvcStatsLastClearedTime_Type = TimeStamp
_TmnxDynSvcStatsLastClearedTime_Object = MibScalar
tmnxDynSvcStatsLastClearedTime = _TmnxDynSvcStatsLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 109),
    _TmnxDynSvcStatsLastClearedTime_Type()
)
tmnxDynSvcStatsLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcStatsLastClearedTime.setStatus("current")
_TmnxDynSvcPlcyAuthTableLastCh_Type = TimeStamp
_TmnxDynSvcPlcyAuthTableLastCh_Object = MibScalar
tmnxDynSvcPlcyAuthTableLastCh = _TmnxDynSvcPlcyAuthTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 110),
    _TmnxDynSvcPlcyAuthTableLastCh_Type()
)
tmnxDynSvcPlcyAuthTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyAuthTableLastCh.setStatus("current")
_TmnxDynSvcCaptureSapTableLastCh_Type = TimeStamp
_TmnxDynSvcCaptureSapTableLastCh_Object = MibScalar
tmnxDynSvcCaptureSapTableLastCh = _TmnxDynSvcCaptureSapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 111),
    _TmnxDynSvcCaptureSapTableLastCh_Type()
)
tmnxDynSvcCaptureSapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcCaptureSapTableLastCh.setStatus("current")
_TmnxDynSvcCSapStatsLastClearTime_Type = TimeStamp
_TmnxDynSvcCSapStatsLastClearTime_Object = MibScalar
tmnxDynSvcCSapStatsLastClearTime = _TmnxDynSvcCSapStatsLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 112),
    _TmnxDynSvcCSapStatsLastClearTime_Type()
)
tmnxDynSvcCSapStatsLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcCSapStatsLastClearTime.setStatus("current")
_TmnxDynSvcDataTriggerTableLastCh_Type = TimeStamp
_TmnxDynSvcDataTriggerTableLastCh_Object = MibScalar
tmnxDynSvcDataTriggerTableLastCh = _TmnxDynSvcDataTriggerTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 113),
    _TmnxDynSvcDataTriggerTableLastCh_Type()
)
tmnxDynSvcDataTriggerTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcDataTriggerTableLastCh.setStatus("current")
_TmnxDynSvcLocADbTableLastCh_Type = TimeStamp
_TmnxDynSvcLocADbTableLastCh_Object = MibScalar
tmnxDynSvcLocADbTableLastCh = _TmnxDynSvcLocADbTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 114),
    _TmnxDynSvcLocADbTableLastCh_Type()
)
tmnxDynSvcLocADbTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbTableLastCh.setStatus("current")
_TmnxDynSvcLocADbUsrTableLastCh_Type = TimeStamp
_TmnxDynSvcLocADbUsrTableLastCh_Object = MibScalar
tmnxDynSvcLocADbUsrTableLastCh = _TmnxDynSvcLocADbUsrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 115),
    _TmnxDynSvcLocADbUsrTableLastCh_Type()
)
tmnxDynSvcLocADbUsrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbUsrTableLastCh.setStatus("current")
_TmnxDynSvcLocADbSapTableLastCh_Type = TimeStamp
_TmnxDynSvcLocADbSapTableLastCh_Object = MibScalar
tmnxDynSvcLocADbSapTableLastCh = _TmnxDynSvcLocADbSapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 116),
    _TmnxDynSvcLocADbSapTableLastCh_Type()
)
tmnxDynSvcLocADbSapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbSapTableLastCh.setStatus("current")
_TmnxDynSvcLocADbAcctTableLastCh_Type = TimeStamp
_TmnxDynSvcLocADbAcctTableLastCh_Object = MibScalar
tmnxDynSvcLocADbAcctTableLastCh = _TmnxDynSvcLocADbAcctTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 117),
    _TmnxDynSvcLocADbAcctTableLastCh_Type()
)
tmnxDynSvcLocADbAcctTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcLocADbAcctTableLastCh.setStatus("current")
_TmnxDynSvcNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxDynSvcNotificationObjs = _TmnxDynSvcNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2)
)


class _TmnxDynSvcNotifDescription_Type(DisplayString):
    """Custom type tmnxDynSvcNotifDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDynSvcNotifDescription_Type.__name__ = "DisplayString"
_TmnxDynSvcNotifDescription_Object = MibScalar
tmnxDynSvcNotifDescription = _TmnxDynSvcNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2, 1),
    _TmnxDynSvcNotifDescription_Type()
)
tmnxDynSvcNotifDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDynSvcNotifDescription.setStatus("current")
_TmnxDynSvcNotifSapPortId_Type = TmnxPortID
_TmnxDynSvcNotifSapPortId_Object = MibScalar
tmnxDynSvcNotifSapPortId = _TmnxDynSvcNotifSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2, 2),
    _TmnxDynSvcNotifSapPortId_Type()
)
tmnxDynSvcNotifSapPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDynSvcNotifSapPortId.setStatus("current")
_TmnxDynSvcNotifSapEncapValue_Type = TmnxEncapVal
_TmnxDynSvcNotifSapEncapValue_Object = MibScalar
tmnxDynSvcNotifSapEncapValue = _TmnxDynSvcNotifSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2, 3),
    _TmnxDynSvcNotifSapEncapValue_Type()
)
tmnxDynSvcNotifSapEncapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDynSvcNotifSapEncapValue.setStatus("current")
_TmnxDynSvcNotifSapAcctSessionId_Type = TmnxSubAcctSessionId
_TmnxDynSvcNotifSapAcctSessionId_Object = MibScalar
tmnxDynSvcNotifSapAcctSessionId = _TmnxDynSvcNotifSapAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2, 4),
    _TmnxDynSvcNotifSapAcctSessionId_Type()
)
tmnxDynSvcNotifSapAcctSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDynSvcNotifSapAcctSessionId.setStatus("current")
_TmnxDynSvcNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxDynSvcNotifyPrefix = _TmnxDynSvcNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 84)
)
_TmnxDynSvcNotifications_ObjectIdentity = ObjectIdentity
tmnxDynSvcNotifications = _TmnxDynSvcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 84, 0)
)
tmnxDynSvcPlcyEntry.registerAugmentions(
    ("TIMETRA-DYNAMIC-SERVICES-MIB",
     "tmnxDynSvcPlcyAuthEntry")
)
tmnxDynSvcPlcyAuthEntry.setIndexNames(*tmnxDynSvcPlcyEntry.getIndexNames())
tmnxDynSvcCaptureSapEntry.registerAugmentions(
    ("TIMETRA-DYNAMIC-SERVICES-MIB",
     "tmnxDynSvcCaptureSapStatsEntry")
)
tmnxDynSvcCaptureSapStatsEntry.setIndexNames(*tmnxDynSvcCaptureSapEntry.getIndexNames())

# Managed Objects groups

tmnxDynSvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2, 1)
)
tmnxDynSvcGroup.setObjects(
      *(("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyRowStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyDescription"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyScriptPlcy"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyCliUser"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcySapLimit"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApName"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApStatsType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApUpdateInterval"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRangeStart"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRangeEnd"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctSessionId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctSessionIdCtrl"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapPolicy"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapScriptsExecuted"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapScriptsSuccess"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapLastScriptAction"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapLastScriptTime"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapOrphaned"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapService"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapLastScriptParams"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctAcctStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctStatsType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctAcctInterval"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApUpdateIvlJitter"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjInstance"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjOrphanTime"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjSnippetName"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjSnippetInstance"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNonStoredRootObjCount"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsDescr"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsVal"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefCount"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetDictLength"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRootObjOid"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefSnipName"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefSnipInst"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdValue"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnipRootObjTblLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdTblLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcTimerAccSetupTimeout"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsLastClearedTime"))
)
if mibBuilder.loadTexts:
    tmnxDynSvcGroup.setStatus("obsolete")

tmnxDynSvcV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2, 2)
)
tmnxDynSvcV14v0Group.setObjects(
      *(("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyRowStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyDescription"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyScriptPlcy"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyCliUser"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcySapLimit"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApName"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApStatsType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApUpdateInterval"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRangeStart"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRangeEnd"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctSessionId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctSessionIdCtrl"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapPolicy"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapScriptsExecuted"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapScriptsSuccess"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapLastScriptAction"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapLastScriptTime"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapService"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapLastScriptParams"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctAcctStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctStatsType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctAcctInterval"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApUpdateIvlJitter"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjInstance"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjOrphanTime"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjSnippetName"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjSnippetInstance"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNonStoredRootObjCount"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsDescr"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsVal"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefCount"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetDictLength"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRootObjOid"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefSnipName"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefSnipInst"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdValue"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnipRootObjTblLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdTblLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcTimerAccSetupTimeout"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsLastClearedTime"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyAuthLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyAuthRadiusSrvPlcy"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyAuthPassword"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyAuthLocalDb"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyAuthTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcCaptureSapLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcCaptureSapAdminState"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcCaptureSapPolicy"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcCaptureSapTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcCSapStatsRxPackets"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcCSapDropReason"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcCSapDropCounter"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcCSapStatsLastClearTime"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcDataTriggerTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcDTriggerAcctSessionId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcDTriggerMacAddress"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcDTriggerIpAddressType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcDTriggerIpAddress"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcDTriggerState"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbUsrTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbAcctTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocAuthDbRowStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocAuthDbLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocAuthDbAdminState"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocAuthDbDescription"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbUsrRowStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbUsrLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbUsrAdminState"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbUsrDescription"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapRowStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapSapId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapPolicy"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapScriptParams1"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapScriptParams2"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapScriptParams3"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbSapScriptParams4"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbAcctRowStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbAcctLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbAcctStatsType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcLocADbAcctUpdateIvl"))
)
if mibBuilder.loadTexts:
    tmnxDynSvcV14v0Group.setStatus("current")

tmnxDynSvcObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2, 98)
)
tmnxDynSvcObsoletedGroup.setObjects(
    ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapOrphaned")
)
if mibBuilder.loadTexts:
    tmnxDynSvcObsoletedGroup.setStatus("current")

tmnxDynSvcNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2, 99)
)
tmnxDynSvcNotifyObjsGroup.setObjects(
      *(("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapAcctSessionId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapPortId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapEncapValue"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifDescription"))
)
if mibBuilder.loadTexts:
    tmnxDynSvcNotifyObjsGroup.setStatus("current")


# Notification objects

tmnxDynSvcSapFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 84, 0, 1)
)
tmnxDynSvcSapFailed.setObjects(
      *(("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapAcctSessionId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapPortId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapEncapValue"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifDescription"))
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapFailed.setStatus(
        "current"
    )


# Notifications groups

tmnxDynSvcNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2, 100)
)
tmnxDynSvcNotifyGroup.setObjects(
    ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapFailed")
)
if mibBuilder.loadTexts:
    tmnxDynSvcNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxDynSvcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 1, 1)
)
tmnxDynSvcCompliance.setObjects(
    ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcGroup")
)
if mibBuilder.loadTexts:
    tmnxDynSvcCompliance.setStatus(
        "obsolete"
    )

tmnxDynSvcNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 1, 2)
)
tmnxDynSvcNotifyCompliance.setObjects(
    ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxDynSvcNotifyCompliance.setStatus(
        "current"
    )

tmnxDynSvcV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 1, 3)
)
tmnxDynSvcV14v0Compliance.setObjects(
      *(("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcV14v0Group"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcObsoletedGroup"))
)
if mibBuilder.loadTexts:
    tmnxDynSvcV14v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-DYNAMIC-SERVICES-MIB",
    **{"TmnxDynSrvAcctStatsType": TmnxDynSrvAcctStatsType,
       "timetraDynSrvMIBModule": timetraDynSrvMIBModule,
       "tmnxDynSvcConformance": tmnxDynSvcConformance,
       "tmnxDynSvcCompliances": tmnxDynSvcCompliances,
       "tmnxDynSvcCompliance": tmnxDynSvcCompliance,
       "tmnxDynSvcNotifyCompliance": tmnxDynSvcNotifyCompliance,
       "tmnxDynSvcV14v0Compliance": tmnxDynSvcV14v0Compliance,
       "tmnxDynSvcGroups": tmnxDynSvcGroups,
       "tmnxDynSvcGroup": tmnxDynSvcGroup,
       "tmnxDynSvcV14v0Group": tmnxDynSvcV14v0Group,
       "tmnxDynSvcObsoletedGroup": tmnxDynSvcObsoletedGroup,
       "tmnxDynSvcNotifyObjsGroup": tmnxDynSvcNotifyObjsGroup,
       "tmnxDynSvcNotifyGroup": tmnxDynSvcNotifyGroup,
       "tmnxDynSvc": tmnxDynSvc,
       "tmnxDynSvcObjs": tmnxDynSvcObjs,
       "tmnxDynSvcPlcyTable": tmnxDynSvcPlcyTable,
       "tmnxDynSvcPlcyEntry": tmnxDynSvcPlcyEntry,
       "tmnxDynSvcPlcyName": tmnxDynSvcPlcyName,
       "tmnxDynSvcPlcyRowStatus": tmnxDynSvcPlcyRowStatus,
       "tmnxDynSvcPlcyLastCh": tmnxDynSvcPlcyLastCh,
       "tmnxDynSvcPlcyDescription": tmnxDynSvcPlcyDescription,
       "tmnxDynSvcPlcyScriptPlcy": tmnxDynSvcPlcyScriptPlcy,
       "tmnxDynSvcPlcyCliUser": tmnxDynSvcPlcyCliUser,
       "tmnxDynSvcPlcySapLimit": tmnxDynSvcPlcySapLimit,
       "tmnxDynSvcPlcyApTable": tmnxDynSvcPlcyApTable,
       "tmnxDynSvcPlcyApEntry": tmnxDynSvcPlcyApEntry,
       "tmnxDynSvcPlcyApIndex": tmnxDynSvcPlcyApIndex,
       "tmnxDynSvcPlcyApLastCh": tmnxDynSvcPlcyApLastCh,
       "tmnxDynSvcPlcyApName": tmnxDynSvcPlcyApName,
       "tmnxDynSvcPlcyApStatsType": tmnxDynSvcPlcyApStatsType,
       "tmnxDynSvcPlcyApUpdateInterval": tmnxDynSvcPlcyApUpdateInterval,
       "tmnxDynSvcPlcyApUpdateIvlJitter": tmnxDynSvcPlcyApUpdateIvlJitter,
       "tmnxDynSvcRange": tmnxDynSvcRange,
       "tmnxDynSvcRangeStart": tmnxDynSvcRangeStart,
       "tmnxDynSvcRangeEnd": tmnxDynSvcRangeEnd,
       "tmnxDynSvcSapTable": tmnxDynSvcSapTable,
       "tmnxDynSvcSapEntry": tmnxDynSvcSapEntry,
       "tmnxDynSvcSapAcctSessionId": tmnxDynSvcSapAcctSessionId,
       "tmnxDynSvcSapAcctSessionIdCtrl": tmnxDynSvcSapAcctSessionIdCtrl,
       "tmnxDynSvcSapPolicy": tmnxDynSvcSapPolicy,
       "tmnxDynSvcSapScriptsExecuted": tmnxDynSvcSapScriptsExecuted,
       "tmnxDynSvcSapScriptsSuccess": tmnxDynSvcSapScriptsSuccess,
       "tmnxDynSvcSapLastScriptAction": tmnxDynSvcSapLastScriptAction,
       "tmnxDynSvcSapLastScriptTime": tmnxDynSvcSapLastScriptTime,
       "tmnxDynSvcSapOrphaned": tmnxDynSvcSapOrphaned,
       "tmnxDynSvcSapService": tmnxDynSvcSapService,
       "tmnxDynSvcSapLastScriptParams": tmnxDynSvcSapLastScriptParams,
       "tmnxDynSvcSapAcctTable": tmnxDynSvcSapAcctTable,
       "tmnxDynSvcSapAcctEntry": tmnxDynSvcSapAcctEntry,
       "tmnxDynSvcSapAcctIndex": tmnxDynSvcSapAcctIndex,
       "tmnxDynSvcSapAcctAcctStatus": tmnxDynSvcSapAcctAcctStatus,
       "tmnxDynSvcSapAcctStatsType": tmnxDynSvcSapAcctStatsType,
       "tmnxDynSvcSapAcctAcctInterval": tmnxDynSvcSapAcctAcctInterval,
       "tmnxDynSvcRootObjTable": tmnxDynSvcRootObjTable,
       "tmnxDynSvcRootObjEntry": tmnxDynSvcRootObjEntry,
       "tmnxDynSvcRootObjIndex": tmnxDynSvcRootObjIndex,
       "tmnxDynSvcRootObjInstance": tmnxDynSvcRootObjInstance,
       "tmnxDynSvcRootObjOrphanTime": tmnxDynSvcRootObjOrphanTime,
       "tmnxDynSvcRootObjSnippetName": tmnxDynSvcRootObjSnippetName,
       "tmnxDynSvcRootObjSnippetInstance": tmnxDynSvcRootObjSnippetInstance,
       "tmnxDynSvcStatsTable": tmnxDynSvcStatsTable,
       "tmnxDynSvcStatsEntry": tmnxDynSvcStatsEntry,
       "tmnxDynSvcStatsId": tmnxDynSvcStatsId,
       "tmnxDynSvcStatsDescr": tmnxDynSvcStatsDescr,
       "tmnxDynSvcStatsVal": tmnxDynSvcStatsVal,
       "tmnxDynSvcSnippetTable": tmnxDynSvcSnippetTable,
       "tmnxDynSvcSnippetEntry": tmnxDynSvcSnippetEntry,
       "tmnxDynSvcSnippetName": tmnxDynSvcSnippetName,
       "tmnxDynSvcSnippetInstance": tmnxDynSvcSnippetInstance,
       "tmnxDynSvcSnippetRefCount": tmnxDynSvcSnippetRefCount,
       "tmnxDynSvcSnippetDictLength": tmnxDynSvcSnippetDictLength,
       "tmnxDynSvcSnippetRootObjTable": tmnxDynSvcSnippetRootObjTable,
       "tmnxDynSvcSnippetRootObjEntry": tmnxDynSvcSnippetRootObjEntry,
       "tmnxDynSvcSnippetRootObjIdx": tmnxDynSvcSnippetRootObjIdx,
       "tmnxDynSvcSnippetRootObjOid": tmnxDynSvcSnippetRootObjOid,
       "tmnxDynSvcSnippetRefTable": tmnxDynSvcSnippetRefTable,
       "tmnxDynSvcSnippetRefEntry": tmnxDynSvcSnippetRefEntry,
       "tmnxDynSvcSnippetRefIdx": tmnxDynSvcSnippetRefIdx,
       "tmnxDynSvcSnippetRefSnipName": tmnxDynSvcSnippetRefSnipName,
       "tmnxDynSvcSnippetRefSnipInst": tmnxDynSvcSnippetRefSnipInst,
       "tmnxDynSvcSnippetResIdTable": tmnxDynSvcSnippetResIdTable,
       "tmnxDynSvcSnippetResIdEntry": tmnxDynSvcSnippetResIdEntry,
       "tmnxDynSvcSnippetResIdIdx": tmnxDynSvcSnippetResIdIdx,
       "tmnxDynSvcSnippetResIdType": tmnxDynSvcSnippetResIdType,
       "tmnxDynSvcSnippetResIdValue": tmnxDynSvcSnippetResIdValue,
       "tmnxDynSvcTimer": tmnxDynSvcTimer,
       "tmnxDynSvcTimerAccSetupTimeout": tmnxDynSvcTimerAccSetupTimeout,
       "tmnxDynSvcPlcyAuthTable": tmnxDynSvcPlcyAuthTable,
       "tmnxDynSvcPlcyAuthEntry": tmnxDynSvcPlcyAuthEntry,
       "tmnxDynSvcPlcyAuthLastCh": tmnxDynSvcPlcyAuthLastCh,
       "tmnxDynSvcPlcyAuthRadiusSrvPlcy": tmnxDynSvcPlcyAuthRadiusSrvPlcy,
       "tmnxDynSvcPlcyAuthPassword": tmnxDynSvcPlcyAuthPassword,
       "tmnxDynSvcPlcyAuthLocalDb": tmnxDynSvcPlcyAuthLocalDb,
       "tmnxDynSvcCaptureSapTable": tmnxDynSvcCaptureSapTable,
       "tmnxDynSvcCaptureSapEntry": tmnxDynSvcCaptureSapEntry,
       "tmnxDynSvcCaptureSapLastCh": tmnxDynSvcCaptureSapLastCh,
       "tmnxDynSvcCaptureSapAdminState": tmnxDynSvcCaptureSapAdminState,
       "tmnxDynSvcCaptureSapPolicy": tmnxDynSvcCaptureSapPolicy,
       "tmnxDynSvcCaptureSapStatsTable": tmnxDynSvcCaptureSapStatsTable,
       "tmnxDynSvcCaptureSapStatsEntry": tmnxDynSvcCaptureSapStatsEntry,
       "tmnxDynSvcCSapStatsRxPackets": tmnxDynSvcCSapStatsRxPackets,
       "tmnxDynSvcCaptureSapDropTable": tmnxDynSvcCaptureSapDropTable,
       "tmnxDynSvcCaptureSapDropEntry": tmnxDynSvcCaptureSapDropEntry,
       "tmnxDynSvcCSapDropIndex": tmnxDynSvcCSapDropIndex,
       "tmnxDynSvcCSapDropReason": tmnxDynSvcCSapDropReason,
       "tmnxDynSvcCSapDropCounter": tmnxDynSvcCSapDropCounter,
       "tmnxDynSvcDataTriggerTable": tmnxDynSvcDataTriggerTable,
       "tmnxDynSvcDataTriggerEntry": tmnxDynSvcDataTriggerEntry,
       "tmnxDynSvcDTriggerAcctSessionId": tmnxDynSvcDTriggerAcctSessionId,
       "tmnxDynSvcDTriggerMacAddress": tmnxDynSvcDTriggerMacAddress,
       "tmnxDynSvcDTriggerIpAddressType": tmnxDynSvcDTriggerIpAddressType,
       "tmnxDynSvcDTriggerIpAddress": tmnxDynSvcDTriggerIpAddress,
       "tmnxDynSvcDTriggerState": tmnxDynSvcDTriggerState,
       "tmnxDynSvcLocalAuthDbTable": tmnxDynSvcLocalAuthDbTable,
       "tmnxDynSvcLocalAuthDbEntry": tmnxDynSvcLocalAuthDbEntry,
       "tmnxDynSvcLocAuthDbName": tmnxDynSvcLocAuthDbName,
       "tmnxDynSvcLocAuthDbRowStatus": tmnxDynSvcLocAuthDbRowStatus,
       "tmnxDynSvcLocAuthDbLastCh": tmnxDynSvcLocAuthDbLastCh,
       "tmnxDynSvcLocAuthDbAdminState": tmnxDynSvcLocAuthDbAdminState,
       "tmnxDynSvcLocAuthDbDescription": tmnxDynSvcLocAuthDbDescription,
       "tmnxDynSvcLocalAuthDbUserTable": tmnxDynSvcLocalAuthDbUserTable,
       "tmnxDynSvcLocalAuthDbUserEntry": tmnxDynSvcLocalAuthDbUserEntry,
       "tmnxDynSvcLocADbUsrName": tmnxDynSvcLocADbUsrName,
       "tmnxDynSvcLocADbUsrRowStatus": tmnxDynSvcLocADbUsrRowStatus,
       "tmnxDynSvcLocADbUsrLastCh": tmnxDynSvcLocADbUsrLastCh,
       "tmnxDynSvcLocADbUsrAdminState": tmnxDynSvcLocADbUsrAdminState,
       "tmnxDynSvcLocADbUsrDescription": tmnxDynSvcLocADbUsrDescription,
       "tmnxDynSvcLocalAuthDbSapTable": tmnxDynSvcLocalAuthDbSapTable,
       "tmnxDynSvcLocalAuthDbSapEntry": tmnxDynSvcLocalAuthDbSapEntry,
       "tmnxDynSvcLocADbSapIndex": tmnxDynSvcLocADbSapIndex,
       "tmnxDynSvcLocADbSapRowStatus": tmnxDynSvcLocADbSapRowStatus,
       "tmnxDynSvcLocADbSapLastCh": tmnxDynSvcLocADbSapLastCh,
       "tmnxDynSvcLocADbSapSapId": tmnxDynSvcLocADbSapSapId,
       "tmnxDynSvcLocADbSapPolicy": tmnxDynSvcLocADbSapPolicy,
       "tmnxDynSvcLocADbSapScriptParams1": tmnxDynSvcLocADbSapScriptParams1,
       "tmnxDynSvcLocADbSapScriptParams2": tmnxDynSvcLocADbSapScriptParams2,
       "tmnxDynSvcLocADbSapScriptParams3": tmnxDynSvcLocADbSapScriptParams3,
       "tmnxDynSvcLocADbSapScriptParams4": tmnxDynSvcLocADbSapScriptParams4,
       "tmnxDynSvcLocalAuthDbAcctTable": tmnxDynSvcLocalAuthDbAcctTable,
       "tmnxDynSvcLocalAuthDbAcctEntry": tmnxDynSvcLocalAuthDbAcctEntry,
       "tmnxDynSvcLocADbAcctIndex": tmnxDynSvcLocADbAcctIndex,
       "tmnxDynSvcLocADbAcctRowStatus": tmnxDynSvcLocADbAcctRowStatus,
       "tmnxDynSvcLocADbAcctLastCh": tmnxDynSvcLocADbAcctLastCh,
       "tmnxDynSvcLocADbAcctStatsType": tmnxDynSvcLocADbAcctStatsType,
       "tmnxDynSvcLocADbAcctUpdateIvl": tmnxDynSvcLocADbAcctUpdateIvl,
       "tmnxDynSvcPlcyTableLastCh": tmnxDynSvcPlcyTableLastCh,
       "tmnxDynSvcPlcyApTableLastCh": tmnxDynSvcPlcyApTableLastCh,
       "tmnxDynSvcSapTableLastCh": tmnxDynSvcSapTableLastCh,
       "tmnxDynSvcRootObjTableLastCh": tmnxDynSvcRootObjTableLastCh,
       "tmnxDynSvcNonStoredRootObjCount": tmnxDynSvcNonStoredRootObjCount,
       "tmnxDynSvcSnippetTableLastCh": tmnxDynSvcSnippetTableLastCh,
       "tmnxDynSvcSnipRootObjTblLastCh": tmnxDynSvcSnipRootObjTblLastCh,
       "tmnxDynSvcSnippetRefTableLastCh": tmnxDynSvcSnippetRefTableLastCh,
       "tmnxDynSvcSnippetResIdTblLastCh": tmnxDynSvcSnippetResIdTblLastCh,
       "tmnxDynSvcStatsLastClearedTime": tmnxDynSvcStatsLastClearedTime,
       "tmnxDynSvcPlcyAuthTableLastCh": tmnxDynSvcPlcyAuthTableLastCh,
       "tmnxDynSvcCaptureSapTableLastCh": tmnxDynSvcCaptureSapTableLastCh,
       "tmnxDynSvcCSapStatsLastClearTime": tmnxDynSvcCSapStatsLastClearTime,
       "tmnxDynSvcDataTriggerTableLastCh": tmnxDynSvcDataTriggerTableLastCh,
       "tmnxDynSvcLocADbTableLastCh": tmnxDynSvcLocADbTableLastCh,
       "tmnxDynSvcLocADbUsrTableLastCh": tmnxDynSvcLocADbUsrTableLastCh,
       "tmnxDynSvcLocADbSapTableLastCh": tmnxDynSvcLocADbSapTableLastCh,
       "tmnxDynSvcLocADbAcctTableLastCh": tmnxDynSvcLocADbAcctTableLastCh,
       "tmnxDynSvcNotificationObjs": tmnxDynSvcNotificationObjs,
       "tmnxDynSvcNotifDescription": tmnxDynSvcNotifDescription,
       "tmnxDynSvcNotifSapPortId": tmnxDynSvcNotifSapPortId,
       "tmnxDynSvcNotifSapEncapValue": tmnxDynSvcNotifSapEncapValue,
       "tmnxDynSvcNotifSapAcctSessionId": tmnxDynSvcNotifSapAcctSessionId,
       "tmnxDynSvcNotifyPrefix": tmnxDynSvcNotifyPrefix,
       "tmnxDynSvcNotifications": tmnxDynSvcNotifications,
       "tmnxDynSvcSapFailed": tmnxDynSvcSapFailed}
)
