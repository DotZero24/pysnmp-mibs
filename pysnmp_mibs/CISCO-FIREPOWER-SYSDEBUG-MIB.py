# SNMP MIB module (CISCO-FIREPOWER-SYSDEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/CISCO-FIREPOWER-SYSDEBUG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:39:52 2025
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprCommClientAdminState,
 CfprConditionRemoteInvRslt,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprNetworkSwitchId,
 CfprPolicyPolicyOwner,
 CfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm,
 CfprSysdebugAutoCoreFileExportTargetFsmStageName,
 CfprSysdebugAutoCoreFileExportTargetFsmTaskItem,
 CfprSysdebugAutoCoreFileExportTargetProto,
 CfprSysdebugBackupBehaviorInterval,
 CfprSysdebugBackupBehaviorProto,
 CfprSysdebugBackupFormat,
 CfprSysdebugCoreExportStatus,
 CfprSysdebugCoreFileAdminState,
 CfprSysdebugCoreFileOperState,
 CfprSysdebugCoreFsmCurrentFsm,
 CfprSysdebugCoreFsmStageName,
 CfprSysdebugCoreFsmTaskItem,
 CfprSysdebugEpLogAdminState,
 CfprSysdebugEpLogBackupAction,
 CfprSysdebugEpLogCapacity,
 CfprSysdebugEpLogType,
 CfprSysdebugExportStatus,
 CfprSysdebugLogControlDomainEnum,
 CfprSysdebugLogControlEpFsmCurrentFsm,
 CfprSysdebugLogControlEpFsmStageName,
 CfprSysdebugLogControlEpFsmTaskItem,
 CfprSysdebugLogControlLevel,
 CfprSysdebugLogExportPolicyFsmCurrentFsm,
 CfprSysdebugLogExportPolicyFsmStageName,
 CfprSysdebugLogExportPolicyFsmTaskItem,
 CfprSysdebugLogExportPolicyProto,
 CfprSysdebugMEpLogOperState,
 CfprSysdebugManualCoreFileExportTargetAdminState,
 CfprSysdebugManualCoreFileExportTargetFsmCurrentFsm,
 CfprSysdebugManualCoreFileExportTargetFsmStageName,
 CfprSysdebugManualCoreFileExportTargetFsmTaskItem,
 CfprSysdebugManualCoreFileExportTargetProto,
 CfprSysdebugTSCmdOptMajorType,
 CfprSysdebugTechSupportAdminState,
 CfprSysdebugTechSupportFsmCurrentFsm,
 CfprSysdebugTechSupportFsmStageName,
 CfprSysdebugTechSupportFsmTaskItem,
 CfprSysdebugTechSupportOperState,
 CfprSysfileExporterPostAction) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprCommClientAdminState",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprNetworkSwitchId",
    "CfprPolicyPolicyOwner",
    "CfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm",
    "CfprSysdebugAutoCoreFileExportTargetFsmStageName",
    "CfprSysdebugAutoCoreFileExportTargetFsmTaskItem",
    "CfprSysdebugAutoCoreFileExportTargetProto",
    "CfprSysdebugBackupBehaviorInterval",
    "CfprSysdebugBackupBehaviorProto",
    "CfprSysdebugBackupFormat",
    "CfprSysdebugCoreExportStatus",
    "CfprSysdebugCoreFileAdminState",
    "CfprSysdebugCoreFileOperState",
    "CfprSysdebugCoreFsmCurrentFsm",
    "CfprSysdebugCoreFsmStageName",
    "CfprSysdebugCoreFsmTaskItem",
    "CfprSysdebugEpLogAdminState",
    "CfprSysdebugEpLogBackupAction",
    "CfprSysdebugEpLogCapacity",
    "CfprSysdebugEpLogType",
    "CfprSysdebugExportStatus",
    "CfprSysdebugLogControlDomainEnum",
    "CfprSysdebugLogControlEpFsmCurrentFsm",
    "CfprSysdebugLogControlEpFsmStageName",
    "CfprSysdebugLogControlEpFsmTaskItem",
    "CfprSysdebugLogControlLevel",
    "CfprSysdebugLogExportPolicyFsmCurrentFsm",
    "CfprSysdebugLogExportPolicyFsmStageName",
    "CfprSysdebugLogExportPolicyFsmTaskItem",
    "CfprSysdebugLogExportPolicyProto",
    "CfprSysdebugMEpLogOperState",
    "CfprSysdebugManualCoreFileExportTargetAdminState",
    "CfprSysdebugManualCoreFileExportTargetFsmCurrentFsm",
    "CfprSysdebugManualCoreFileExportTargetFsmStageName",
    "CfprSysdebugManualCoreFileExportTargetFsmTaskItem",
    "CfprSysdebugManualCoreFileExportTargetProto",
    "CfprSysdebugTSCmdOptMajorType",
    "CfprSysdebugTechSupportAdminState",
    "CfprSysdebugTechSupportFsmCurrentFsm",
    "CfprSysdebugTechSupportFsmStageName",
    "CfprSysdebugTechSupportFsmTaskItem",
    "CfprSysdebugTechSupportOperState",
    "CfprSysfileExporterPostAction")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprSysdebugObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprSysdebugAutoCoreFileExportTargetTable_Object = MibTable
cfprSysdebugAutoCoreFileExportTargetTable = _CfprSysdebugAutoCoreFileExportTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1)
)
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetTable.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetEntry_Object = MibTableRow
cfprSysdebugAutoCoreFileExportTargetEntry = _CfprSysdebugAutoCoreFileExportTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1)
)
cfprSysdebugAutoCoreFileExportTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugAutoCoreFileExportTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetEntry.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetInstanceId_Type = CfprManagedObjectId
_CfprSysdebugAutoCoreFileExportTargetInstanceId_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetInstanceId = _CfprSysdebugAutoCoreFileExportTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 1),
    _CfprSysdebugAutoCoreFileExportTargetInstanceId_Type()
)
cfprSysdebugAutoCoreFileExportTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetInstanceId.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetDn_Type = CfprManagedObjectDn
_CfprSysdebugAutoCoreFileExportTargetDn_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetDn = _CfprSysdebugAutoCoreFileExportTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 2),
    _CfprSysdebugAutoCoreFileExportTargetDn_Type()
)
cfprSysdebugAutoCoreFileExportTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetDn.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetRn_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetRn_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetRn = _CfprSysdebugAutoCoreFileExportTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 3),
    _CfprSysdebugAutoCoreFileExportTargetRn_Type()
)
cfprSysdebugAutoCoreFileExportTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetRn.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetAdminState_Type = CfprCommClientAdminState
_CfprSysdebugAutoCoreFileExportTargetAdminState_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetAdminState = _CfprSysdebugAutoCoreFileExportTargetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 4),
    _CfprSysdebugAutoCoreFileExportTargetAdminState_Type()
)
cfprSysdebugAutoCoreFileExportTargetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetAdminState.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetDescr_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetDescr_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetDescr = _CfprSysdebugAutoCoreFileExportTargetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 5),
    _CfprSysdebugAutoCoreFileExportTargetDescr_Type()
)
cfprSysdebugAutoCoreFileExportTargetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetDescr.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetExportFailureReason_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetExportFailureReason_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetExportFailureReason = _CfprSysdebugAutoCoreFileExportTargetExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 6),
    _CfprSysdebugAutoCoreFileExportTargetExportFailureReason_Type()
)
cfprSysdebugAutoCoreFileExportTargetExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetExportFailureReason.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetExportStatus_Type = CfprSysdebugCoreExportStatus
_CfprSysdebugAutoCoreFileExportTargetExportStatus_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetExportStatus = _CfprSysdebugAutoCoreFileExportTargetExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 7),
    _CfprSysdebugAutoCoreFileExportTargetExportStatus_Type()
)
cfprSysdebugAutoCoreFileExportTargetExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetExportStatus.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmDescr_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmDescr_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmDescr = _CfprSysdebugAutoCoreFileExportTargetFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 8),
    _CfprSysdebugAutoCoreFileExportTargetFsmDescr_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmDescr.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmPrev_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmPrev_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmPrev = _CfprSysdebugAutoCoreFileExportTargetFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 9),
    _CfprSysdebugAutoCoreFileExportTargetFsmPrev_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmPrev.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmProgr_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetFsmProgr_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmProgr = _CfprSysdebugAutoCoreFileExportTargetFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 10),
    _CfprSysdebugAutoCoreFileExportTargetFsmProgr_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmProgr.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode = _CfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 11),
    _CfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr = _CfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 12),
    _CfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmRmtInvRslt = _CfprSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 13),
    _CfprSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmRmtInvRslt.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageDescr_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmStageDescr_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageDescr = _CfprSysdebugAutoCoreFileExportTargetFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 14),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageDescr_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageDescr.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStamp_Type = DateAndTime
_CfprSysdebugAutoCoreFileExportTargetFsmStamp_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStamp = _CfprSysdebugAutoCoreFileExportTargetFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 15),
    _CfprSysdebugAutoCoreFileExportTargetFsmStamp_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStamp.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStatus_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmStatus_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStatus = _CfprSysdebugAutoCoreFileExportTargetFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 16),
    _CfprSysdebugAutoCoreFileExportTargetFsmStatus_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStatus.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTry_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetFsmTry_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmTry = _CfprSysdebugAutoCoreFileExportTargetFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 17),
    _CfprSysdebugAutoCoreFileExportTargetFsmTry_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTry.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetHostname_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetHostname_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetHostname = _CfprSysdebugAutoCoreFileExportTargetHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 18),
    _CfprSysdebugAutoCoreFileExportTargetHostname_Type()
)
cfprSysdebugAutoCoreFileExportTargetHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetHostname.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetIntId_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetIntId_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetIntId = _CfprSysdebugAutoCoreFileExportTargetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 19),
    _CfprSysdebugAutoCoreFileExportTargetIntId_Type()
)
cfprSysdebugAutoCoreFileExportTargetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetIntId.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetName_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetName_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetName = _CfprSysdebugAutoCoreFileExportTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 20),
    _CfprSysdebugAutoCoreFileExportTargetName_Type()
)
cfprSysdebugAutoCoreFileExportTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetName.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetPath_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetPath_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetPath = _CfprSysdebugAutoCoreFileExportTargetPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 21),
    _CfprSysdebugAutoCoreFileExportTargetPath_Type()
)
cfprSysdebugAutoCoreFileExportTargetPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetPath.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetPolicyLevel_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetPolicyLevel_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetPolicyLevel = _CfprSysdebugAutoCoreFileExportTargetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 22),
    _CfprSysdebugAutoCoreFileExportTargetPolicyLevel_Type()
)
cfprSysdebugAutoCoreFileExportTargetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetPolicyLevel.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprSysdebugAutoCoreFileExportTargetPolicyOwner_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetPolicyOwner = _CfprSysdebugAutoCoreFileExportTargetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 23),
    _CfprSysdebugAutoCoreFileExportTargetPolicyOwner_Type()
)
cfprSysdebugAutoCoreFileExportTargetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetPolicyOwner.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetPort_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetPort_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetPort = _CfprSysdebugAutoCoreFileExportTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 24),
    _CfprSysdebugAutoCoreFileExportTargetPort_Type()
)
cfprSysdebugAutoCoreFileExportTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetPort.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetPostAction_Type = CfprSysfileExporterPostAction
_CfprSysdebugAutoCoreFileExportTargetPostAction_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetPostAction = _CfprSysdebugAutoCoreFileExportTargetPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 25),
    _CfprSysdebugAutoCoreFileExportTargetPostAction_Type()
)
cfprSysdebugAutoCoreFileExportTargetPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetPostAction.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetProto_Type = CfprSysdebugAutoCoreFileExportTargetProto
_CfprSysdebugAutoCoreFileExportTargetProto_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetProto = _CfprSysdebugAutoCoreFileExportTargetProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 1, 1, 26),
    _CfprSysdebugAutoCoreFileExportTargetProto_Type()
)
cfprSysdebugAutoCoreFileExportTargetProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetProto.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTable_Object = MibTable
cfprSysdebugAutoCoreFileExportTargetFsmTable = _CfprSysdebugAutoCoreFileExportTargetFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2)
)
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTable.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmEntry_Object = MibTableRow
cfprSysdebugAutoCoreFileExportTargetFsmEntry = _CfprSysdebugAutoCoreFileExportTargetFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1)
)
cfprSysdebugAutoCoreFileExportTargetFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugAutoCoreFileExportTargetFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmEntry.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmInstanceId_Type = CfprManagedObjectId
_CfprSysdebugAutoCoreFileExportTargetFsmInstanceId_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmInstanceId = _CfprSysdebugAutoCoreFileExportTargetFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 1),
    _CfprSysdebugAutoCoreFileExportTargetFsmInstanceId_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmInstanceId.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmDn_Type = CfprManagedObjectDn
_CfprSysdebugAutoCoreFileExportTargetFsmDn_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmDn = _CfprSysdebugAutoCoreFileExportTargetFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 2),
    _CfprSysdebugAutoCoreFileExportTargetFsmDn_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmDn.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmRn_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmRn_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmRn = _CfprSysdebugAutoCoreFileExportTargetFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 3),
    _CfprSysdebugAutoCoreFileExportTargetFsmRn_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmRn.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmCompletionTime_Type = DateAndTime
_CfprSysdebugAutoCoreFileExportTargetFsmCompletionTime_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmCompletionTime = _CfprSysdebugAutoCoreFileExportTargetFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 4),
    _CfprSysdebugAutoCoreFileExportTargetFsmCompletionTime_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmCompletionTime.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Type = CfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm
_CfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm = _CfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 5),
    _CfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmDescrData_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmDescrData_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmDescrData = _CfprSysdebugAutoCoreFileExportTargetFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 6),
    _CfprSysdebugAutoCoreFileExportTargetFsmDescrData_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmDescrData.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugAutoCoreFileExportTargetFsmFsmStatus_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmFsmStatus = _CfprSysdebugAutoCoreFileExportTargetFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 7),
    _CfprSysdebugAutoCoreFileExportTargetFsmFsmStatus_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmFsmStatus.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmProgress_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetFsmProgress_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmProgress = _CfprSysdebugAutoCoreFileExportTargetFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 8),
    _CfprSysdebugAutoCoreFileExportTargetFsmProgress_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmProgress.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmRmtErrCode = _CfprSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 9),
    _CfprSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmRmtErrCode.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmRmtErrDescr = _CfprSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 10),
    _CfprSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmRmtErrDescr.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugAutoCoreFileExportTargetFsmRmtRslt_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmRmtRslt = _CfprSysdebugAutoCoreFileExportTargetFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 2, 1, 11),
    _CfprSysdebugAutoCoreFileExportTargetFsmRmtRslt_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmRmtRslt.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageTable_Object = MibTable
cfprSysdebugAutoCoreFileExportTargetFsmStageTable = _CfprSysdebugAutoCoreFileExportTargetFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3)
)
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageTable.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageEntry_Object = MibTableRow
cfprSysdebugAutoCoreFileExportTargetFsmStageEntry = _CfprSysdebugAutoCoreFileExportTargetFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1)
)
cfprSysdebugAutoCoreFileExportTargetFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageEntry.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId = _CfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1, 1),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageDn_Type = CfprManagedObjectDn
_CfprSysdebugAutoCoreFileExportTargetFsmStageDn_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageDn = _CfprSysdebugAutoCoreFileExportTargetFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1, 2),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageDn_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageDn.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageRn_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmStageRn_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageRn = _CfprSysdebugAutoCoreFileExportTargetFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1, 3),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageRn_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageRn.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageDescrData_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmStageDescrData_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageDescrData = _CfprSysdebugAutoCoreFileExportTargetFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1, 4),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageDescrData_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageDescrData.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Type = DateAndTime
_CfprSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime = _CfprSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1, 5),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageName_Type = CfprSysdebugAutoCoreFileExportTargetFsmStageName
_CfprSysdebugAutoCoreFileExportTargetFsmStageName_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageName = _CfprSysdebugAutoCoreFileExportTargetFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1, 6),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageName_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageName.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageOrder_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetFsmStageOrder_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageOrder = _CfprSysdebugAutoCoreFileExportTargetFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1, 7),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageOrder_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageOrder.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageRetry_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetFsmStageRetry_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageRetry = _CfprSysdebugAutoCoreFileExportTargetFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1, 8),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageRetry_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageRetry.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmStageStageStatus = _CfprSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 3, 1, 9),
    _CfprSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmStageStageStatus.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTaskTable_Object = MibTable
cfprSysdebugAutoCoreFileExportTargetFsmTaskTable = _CfprSysdebugAutoCoreFileExportTargetFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 4)
)
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTaskTable.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTaskEntry_Object = MibTableRow
cfprSysdebugAutoCoreFileExportTargetFsmTaskEntry = _CfprSysdebugAutoCoreFileExportTargetFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 4, 1)
)
cfprSysdebugAutoCoreFileExportTargetFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTaskEntry.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId = _CfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 4, 1, 1),
    _CfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTaskDn_Type = CfprManagedObjectDn
_CfprSysdebugAutoCoreFileExportTargetFsmTaskDn_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmTaskDn = _CfprSysdebugAutoCoreFileExportTargetFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 4, 1, 2),
    _CfprSysdebugAutoCoreFileExportTargetFsmTaskDn_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTaskDn.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTaskRn_Type = SnmpAdminString
_CfprSysdebugAutoCoreFileExportTargetFsmTaskRn_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmTaskRn = _CfprSysdebugAutoCoreFileExportTargetFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 4, 1, 3),
    _CfprSysdebugAutoCoreFileExportTargetFsmTaskRn_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTaskRn.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmTaskCompletion = _CfprSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 4, 1, 4),
    _CfprSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTaskCompletion.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTaskFlags_Type = CfprFsmFlags
_CfprSysdebugAutoCoreFileExportTargetFsmTaskFlags_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmTaskFlags = _CfprSysdebugAutoCoreFileExportTargetFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 4, 1, 5),
    _CfprSysdebugAutoCoreFileExportTargetFsmTaskFlags_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTaskFlags.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTaskItem_Type = CfprSysdebugAutoCoreFileExportTargetFsmTaskItem
_CfprSysdebugAutoCoreFileExportTargetFsmTaskItem_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmTaskItem = _CfprSysdebugAutoCoreFileExportTargetFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 4, 1, 6),
    _CfprSysdebugAutoCoreFileExportTargetFsmTaskItem_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTaskItem.setStatus("current")
_CfprSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Type = Gauge32
_CfprSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Object = MibTableColumn
cfprSysdebugAutoCoreFileExportTargetFsmTaskSeqId = _CfprSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 4, 1, 7),
    _CfprSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Type()
)
cfprSysdebugAutoCoreFileExportTargetFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAutoCoreFileExportTargetFsmTaskSeqId.setStatus("current")
_CfprSysdebugBackupBehaviorTable_Object = MibTable
cfprSysdebugBackupBehaviorTable = _CfprSysdebugBackupBehaviorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5)
)
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorTable.setStatus("current")
_CfprSysdebugBackupBehaviorEntry_Object = MibTableRow
cfprSysdebugBackupBehaviorEntry = _CfprSysdebugBackupBehaviorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1)
)
cfprSysdebugBackupBehaviorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugBackupBehaviorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorEntry.setStatus("current")
_CfprSysdebugBackupBehaviorInstanceId_Type = CfprManagedObjectId
_CfprSysdebugBackupBehaviorInstanceId_Object = MibTableColumn
cfprSysdebugBackupBehaviorInstanceId = _CfprSysdebugBackupBehaviorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 1),
    _CfprSysdebugBackupBehaviorInstanceId_Type()
)
cfprSysdebugBackupBehaviorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorInstanceId.setStatus("current")
_CfprSysdebugBackupBehaviorDn_Type = CfprManagedObjectDn
_CfprSysdebugBackupBehaviorDn_Object = MibTableColumn
cfprSysdebugBackupBehaviorDn = _CfprSysdebugBackupBehaviorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 2),
    _CfprSysdebugBackupBehaviorDn_Type()
)
cfprSysdebugBackupBehaviorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorDn.setStatus("current")
_CfprSysdebugBackupBehaviorRn_Type = SnmpAdminString
_CfprSysdebugBackupBehaviorRn_Object = MibTableColumn
cfprSysdebugBackupBehaviorRn = _CfprSysdebugBackupBehaviorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 3),
    _CfprSysdebugBackupBehaviorRn_Type()
)
cfprSysdebugBackupBehaviorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorRn.setStatus("current")
_CfprSysdebugBackupBehaviorAction_Type = CfprSysdebugEpLogBackupAction
_CfprSysdebugBackupBehaviorAction_Object = MibTableColumn
cfprSysdebugBackupBehaviorAction = _CfprSysdebugBackupBehaviorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 4),
    _CfprSysdebugBackupBehaviorAction_Type()
)
cfprSysdebugBackupBehaviorAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorAction.setStatus("current")
_CfprSysdebugBackupBehaviorClearOnBackup_Type = TruthValue
_CfprSysdebugBackupBehaviorClearOnBackup_Object = MibTableColumn
cfprSysdebugBackupBehaviorClearOnBackup = _CfprSysdebugBackupBehaviorClearOnBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 5),
    _CfprSysdebugBackupBehaviorClearOnBackup_Type()
)
cfprSysdebugBackupBehaviorClearOnBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorClearOnBackup.setStatus("current")
_CfprSysdebugBackupBehaviorFormat_Type = CfprSysdebugBackupFormat
_CfprSysdebugBackupBehaviorFormat_Object = MibTableColumn
cfprSysdebugBackupBehaviorFormat = _CfprSysdebugBackupBehaviorFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 6),
    _CfprSysdebugBackupBehaviorFormat_Type()
)
cfprSysdebugBackupBehaviorFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorFormat.setStatus("current")
_CfprSysdebugBackupBehaviorHostname_Type = SnmpAdminString
_CfprSysdebugBackupBehaviorHostname_Object = MibTableColumn
cfprSysdebugBackupBehaviorHostname = _CfprSysdebugBackupBehaviorHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 7),
    _CfprSysdebugBackupBehaviorHostname_Type()
)
cfprSysdebugBackupBehaviorHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorHostname.setStatus("current")
_CfprSysdebugBackupBehaviorInterval_Type = CfprSysdebugBackupBehaviorInterval
_CfprSysdebugBackupBehaviorInterval_Object = MibTableColumn
cfprSysdebugBackupBehaviorInterval = _CfprSysdebugBackupBehaviorInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 8),
    _CfprSysdebugBackupBehaviorInterval_Type()
)
cfprSysdebugBackupBehaviorInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorInterval.setStatus("current")
_CfprSysdebugBackupBehaviorProto_Type = CfprSysdebugBackupBehaviorProto
_CfprSysdebugBackupBehaviorProto_Object = MibTableColumn
cfprSysdebugBackupBehaviorProto = _CfprSysdebugBackupBehaviorProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 9),
    _CfprSysdebugBackupBehaviorProto_Type()
)
cfprSysdebugBackupBehaviorProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorProto.setStatus("current")
_CfprSysdebugBackupBehaviorPwd_Type = SnmpAdminString
_CfprSysdebugBackupBehaviorPwd_Object = MibTableColumn
cfprSysdebugBackupBehaviorPwd = _CfprSysdebugBackupBehaviorPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 10),
    _CfprSysdebugBackupBehaviorPwd_Type()
)
cfprSysdebugBackupBehaviorPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorPwd.setStatus("current")
_CfprSysdebugBackupBehaviorRemotePath_Type = SnmpAdminString
_CfprSysdebugBackupBehaviorRemotePath_Object = MibTableColumn
cfprSysdebugBackupBehaviorRemotePath = _CfprSysdebugBackupBehaviorRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 11),
    _CfprSysdebugBackupBehaviorRemotePath_Type()
)
cfprSysdebugBackupBehaviorRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorRemotePath.setStatus("current")
_CfprSysdebugBackupBehaviorUser_Type = SnmpAdminString
_CfprSysdebugBackupBehaviorUser_Object = MibTableColumn
cfprSysdebugBackupBehaviorUser = _CfprSysdebugBackupBehaviorUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 5, 1, 12),
    _CfprSysdebugBackupBehaviorUser_Type()
)
cfprSysdebugBackupBehaviorUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugBackupBehaviorUser.setStatus("current")
_CfprSysdebugCoreTable_Object = MibTable
cfprSysdebugCoreTable = _CfprSysdebugCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6)
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreTable.setStatus("current")
_CfprSysdebugCoreEntry_Object = MibTableRow
cfprSysdebugCoreEntry = _CfprSysdebugCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1)
)
cfprSysdebugCoreEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugCoreInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreEntry.setStatus("current")
_CfprSysdebugCoreInstanceId_Type = CfprManagedObjectId
_CfprSysdebugCoreInstanceId_Object = MibTableColumn
cfprSysdebugCoreInstanceId = _CfprSysdebugCoreInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 1),
    _CfprSysdebugCoreInstanceId_Type()
)
cfprSysdebugCoreInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugCoreInstanceId.setStatus("current")
_CfprSysdebugCoreDn_Type = CfprManagedObjectDn
_CfprSysdebugCoreDn_Object = MibTableColumn
cfprSysdebugCoreDn = _CfprSysdebugCoreDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 2),
    _CfprSysdebugCoreDn_Type()
)
cfprSysdebugCoreDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreDn.setStatus("current")
_CfprSysdebugCoreRn_Type = SnmpAdminString
_CfprSysdebugCoreRn_Object = MibTableColumn
cfprSysdebugCoreRn = _CfprSysdebugCoreRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 3),
    _CfprSysdebugCoreRn_Type()
)
cfprSysdebugCoreRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreRn.setStatus("current")
_CfprSysdebugCoreAdminState_Type = CfprSysdebugCoreFileAdminState
_CfprSysdebugCoreAdminState_Object = MibTableColumn
cfprSysdebugCoreAdminState = _CfprSysdebugCoreAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 4),
    _CfprSysdebugCoreAdminState_Type()
)
cfprSysdebugCoreAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreAdminState.setStatus("current")
_CfprSysdebugCoreDescr_Type = SnmpAdminString
_CfprSysdebugCoreDescr_Object = MibTableColumn
cfprSysdebugCoreDescr = _CfprSysdebugCoreDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 5),
    _CfprSysdebugCoreDescr_Type()
)
cfprSysdebugCoreDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreDescr.setStatus("current")
_CfprSysdebugCoreFsmDescr_Type = SnmpAdminString
_CfprSysdebugCoreFsmDescr_Object = MibTableColumn
cfprSysdebugCoreFsmDescr = _CfprSysdebugCoreFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 6),
    _CfprSysdebugCoreFsmDescr_Type()
)
cfprSysdebugCoreFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmDescr.setStatus("current")
_CfprSysdebugCoreFsmPrev_Type = SnmpAdminString
_CfprSysdebugCoreFsmPrev_Object = MibTableColumn
cfprSysdebugCoreFsmPrev = _CfprSysdebugCoreFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 7),
    _CfprSysdebugCoreFsmPrev_Type()
)
cfprSysdebugCoreFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmPrev.setStatus("current")
_CfprSysdebugCoreFsmProgr_Type = Gauge32
_CfprSysdebugCoreFsmProgr_Object = MibTableColumn
cfprSysdebugCoreFsmProgr = _CfprSysdebugCoreFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 8),
    _CfprSysdebugCoreFsmProgr_Type()
)
cfprSysdebugCoreFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmProgr.setStatus("current")
_CfprSysdebugCoreFsmRmtInvErrCode_Type = Gauge32
_CfprSysdebugCoreFsmRmtInvErrCode_Object = MibTableColumn
cfprSysdebugCoreFsmRmtInvErrCode = _CfprSysdebugCoreFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 9),
    _CfprSysdebugCoreFsmRmtInvErrCode_Type()
)
cfprSysdebugCoreFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmRmtInvErrCode.setStatus("current")
_CfprSysdebugCoreFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSysdebugCoreFsmRmtInvErrDescr_Object = MibTableColumn
cfprSysdebugCoreFsmRmtInvErrDescr = _CfprSysdebugCoreFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 10),
    _CfprSysdebugCoreFsmRmtInvErrDescr_Type()
)
cfprSysdebugCoreFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmRmtInvErrDescr.setStatus("current")
_CfprSysdebugCoreFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugCoreFsmRmtInvRslt_Object = MibTableColumn
cfprSysdebugCoreFsmRmtInvRslt = _CfprSysdebugCoreFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 11),
    _CfprSysdebugCoreFsmRmtInvRslt_Type()
)
cfprSysdebugCoreFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmRmtInvRslt.setStatus("current")
_CfprSysdebugCoreFsmStageDescr_Type = SnmpAdminString
_CfprSysdebugCoreFsmStageDescr_Object = MibTableColumn
cfprSysdebugCoreFsmStageDescr = _CfprSysdebugCoreFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 12),
    _CfprSysdebugCoreFsmStageDescr_Type()
)
cfprSysdebugCoreFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageDescr.setStatus("current")
_CfprSysdebugCoreFsmStamp_Type = DateAndTime
_CfprSysdebugCoreFsmStamp_Object = MibTableColumn
cfprSysdebugCoreFsmStamp = _CfprSysdebugCoreFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 13),
    _CfprSysdebugCoreFsmStamp_Type()
)
cfprSysdebugCoreFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStamp.setStatus("current")
_CfprSysdebugCoreFsmStatus_Type = SnmpAdminString
_CfprSysdebugCoreFsmStatus_Object = MibTableColumn
cfprSysdebugCoreFsmStatus = _CfprSysdebugCoreFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 14),
    _CfprSysdebugCoreFsmStatus_Type()
)
cfprSysdebugCoreFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStatus.setStatus("current")
_CfprSysdebugCoreFsmTry_Type = Gauge32
_CfprSysdebugCoreFsmTry_Object = MibTableColumn
cfprSysdebugCoreFsmTry = _CfprSysdebugCoreFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 15),
    _CfprSysdebugCoreFsmTry_Type()
)
cfprSysdebugCoreFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTry.setStatus("current")
_CfprSysdebugCoreName_Type = SnmpAdminString
_CfprSysdebugCoreName_Object = MibTableColumn
cfprSysdebugCoreName = _CfprSysdebugCoreName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 16),
    _CfprSysdebugCoreName_Type()
)
cfprSysdebugCoreName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreName.setStatus("current")
_CfprSysdebugCoreOperState_Type = CfprSysdebugCoreFileOperState
_CfprSysdebugCoreOperState_Object = MibTableColumn
cfprSysdebugCoreOperState = _CfprSysdebugCoreOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 17),
    _CfprSysdebugCoreOperState_Type()
)
cfprSysdebugCoreOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreOperState.setStatus("current")
_CfprSysdebugCoreSize_Type = Gauge32
_CfprSysdebugCoreSize_Object = MibTableColumn
cfprSysdebugCoreSize = _CfprSysdebugCoreSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 18),
    _CfprSysdebugCoreSize_Type()
)
cfprSysdebugCoreSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreSize.setStatus("current")
_CfprSysdebugCoreSwitchId_Type = CfprNetworkSwitchId
_CfprSysdebugCoreSwitchId_Object = MibTableColumn
cfprSysdebugCoreSwitchId = _CfprSysdebugCoreSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 19),
    _CfprSysdebugCoreSwitchId_Type()
)
cfprSysdebugCoreSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreSwitchId.setStatus("current")
_CfprSysdebugCoreTs_Type = DateAndTime
_CfprSysdebugCoreTs_Object = MibTableColumn
cfprSysdebugCoreTs = _CfprSysdebugCoreTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 20),
    _CfprSysdebugCoreTs_Type()
)
cfprSysdebugCoreTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreTs.setStatus("current")
_CfprSysdebugCoreUri_Type = SnmpAdminString
_CfprSysdebugCoreUri_Object = MibTableColumn
cfprSysdebugCoreUri = _CfprSysdebugCoreUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 6, 1, 21),
    _CfprSysdebugCoreUri_Type()
)
cfprSysdebugCoreUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreUri.setStatus("current")
_CfprSysdebugCoreFileRepositoryTable_Object = MibTable
cfprSysdebugCoreFileRepositoryTable = _CfprSysdebugCoreFileRepositoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 7)
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreFileRepositoryTable.setStatus("current")
_CfprSysdebugCoreFileRepositoryEntry_Object = MibTableRow
cfprSysdebugCoreFileRepositoryEntry = _CfprSysdebugCoreFileRepositoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 7, 1)
)
cfprSysdebugCoreFileRepositoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugCoreFileRepositoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreFileRepositoryEntry.setStatus("current")
_CfprSysdebugCoreFileRepositoryInstanceId_Type = CfprManagedObjectId
_CfprSysdebugCoreFileRepositoryInstanceId_Object = MibTableColumn
cfprSysdebugCoreFileRepositoryInstanceId = _CfprSysdebugCoreFileRepositoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 7, 1, 1),
    _CfprSysdebugCoreFileRepositoryInstanceId_Type()
)
cfprSysdebugCoreFileRepositoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFileRepositoryInstanceId.setStatus("current")
_CfprSysdebugCoreFileRepositoryDn_Type = CfprManagedObjectDn
_CfprSysdebugCoreFileRepositoryDn_Object = MibTableColumn
cfprSysdebugCoreFileRepositoryDn = _CfprSysdebugCoreFileRepositoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 7, 1, 2),
    _CfprSysdebugCoreFileRepositoryDn_Type()
)
cfprSysdebugCoreFileRepositoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFileRepositoryDn.setStatus("current")
_CfprSysdebugCoreFileRepositoryRn_Type = SnmpAdminString
_CfprSysdebugCoreFileRepositoryRn_Object = MibTableColumn
cfprSysdebugCoreFileRepositoryRn = _CfprSysdebugCoreFileRepositoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 7, 1, 3),
    _CfprSysdebugCoreFileRepositoryRn_Type()
)
cfprSysdebugCoreFileRepositoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFileRepositoryRn.setStatus("current")
_CfprSysdebugCoreFsmTable_Object = MibTable
cfprSysdebugCoreFsmTable = _CfprSysdebugCoreFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8)
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTable.setStatus("current")
_CfprSysdebugCoreFsmEntry_Object = MibTableRow
cfprSysdebugCoreFsmEntry = _CfprSysdebugCoreFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1)
)
cfprSysdebugCoreFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugCoreFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmEntry.setStatus("current")
_CfprSysdebugCoreFsmInstanceId_Type = CfprManagedObjectId
_CfprSysdebugCoreFsmInstanceId_Object = MibTableColumn
cfprSysdebugCoreFsmInstanceId = _CfprSysdebugCoreFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 1),
    _CfprSysdebugCoreFsmInstanceId_Type()
)
cfprSysdebugCoreFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmInstanceId.setStatus("current")
_CfprSysdebugCoreFsmDn_Type = CfprManagedObjectDn
_CfprSysdebugCoreFsmDn_Object = MibTableColumn
cfprSysdebugCoreFsmDn = _CfprSysdebugCoreFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 2),
    _CfprSysdebugCoreFsmDn_Type()
)
cfprSysdebugCoreFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmDn.setStatus("current")
_CfprSysdebugCoreFsmRn_Type = SnmpAdminString
_CfprSysdebugCoreFsmRn_Object = MibTableColumn
cfprSysdebugCoreFsmRn = _CfprSysdebugCoreFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 3),
    _CfprSysdebugCoreFsmRn_Type()
)
cfprSysdebugCoreFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmRn.setStatus("current")
_CfprSysdebugCoreFsmCompletionTime_Type = DateAndTime
_CfprSysdebugCoreFsmCompletionTime_Object = MibTableColumn
cfprSysdebugCoreFsmCompletionTime = _CfprSysdebugCoreFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 4),
    _CfprSysdebugCoreFsmCompletionTime_Type()
)
cfprSysdebugCoreFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmCompletionTime.setStatus("current")
_CfprSysdebugCoreFsmCurrentFsm_Type = CfprSysdebugCoreFsmCurrentFsm
_CfprSysdebugCoreFsmCurrentFsm_Object = MibTableColumn
cfprSysdebugCoreFsmCurrentFsm = _CfprSysdebugCoreFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 5),
    _CfprSysdebugCoreFsmCurrentFsm_Type()
)
cfprSysdebugCoreFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmCurrentFsm.setStatus("current")
_CfprSysdebugCoreFsmDescrData_Type = SnmpAdminString
_CfprSysdebugCoreFsmDescrData_Object = MibTableColumn
cfprSysdebugCoreFsmDescrData = _CfprSysdebugCoreFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 6),
    _CfprSysdebugCoreFsmDescrData_Type()
)
cfprSysdebugCoreFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmDescrData.setStatus("current")
_CfprSysdebugCoreFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugCoreFsmFsmStatus_Object = MibTableColumn
cfprSysdebugCoreFsmFsmStatus = _CfprSysdebugCoreFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 7),
    _CfprSysdebugCoreFsmFsmStatus_Type()
)
cfprSysdebugCoreFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmFsmStatus.setStatus("current")
_CfprSysdebugCoreFsmProgress_Type = Gauge32
_CfprSysdebugCoreFsmProgress_Object = MibTableColumn
cfprSysdebugCoreFsmProgress = _CfprSysdebugCoreFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 8),
    _CfprSysdebugCoreFsmProgress_Type()
)
cfprSysdebugCoreFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmProgress.setStatus("current")
_CfprSysdebugCoreFsmRmtErrCode_Type = Gauge32
_CfprSysdebugCoreFsmRmtErrCode_Object = MibTableColumn
cfprSysdebugCoreFsmRmtErrCode = _CfprSysdebugCoreFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 9),
    _CfprSysdebugCoreFsmRmtErrCode_Type()
)
cfprSysdebugCoreFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmRmtErrCode.setStatus("current")
_CfprSysdebugCoreFsmRmtErrDescr_Type = SnmpAdminString
_CfprSysdebugCoreFsmRmtErrDescr_Object = MibTableColumn
cfprSysdebugCoreFsmRmtErrDescr = _CfprSysdebugCoreFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 10),
    _CfprSysdebugCoreFsmRmtErrDescr_Type()
)
cfprSysdebugCoreFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmRmtErrDescr.setStatus("current")
_CfprSysdebugCoreFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugCoreFsmRmtRslt_Object = MibTableColumn
cfprSysdebugCoreFsmRmtRslt = _CfprSysdebugCoreFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 8, 1, 11),
    _CfprSysdebugCoreFsmRmtRslt_Type()
)
cfprSysdebugCoreFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmRmtRslt.setStatus("current")
_CfprSysdebugCoreFsmStageTable_Object = MibTable
cfprSysdebugCoreFsmStageTable = _CfprSysdebugCoreFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9)
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageTable.setStatus("current")
_CfprSysdebugCoreFsmStageEntry_Object = MibTableRow
cfprSysdebugCoreFsmStageEntry = _CfprSysdebugCoreFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1)
)
cfprSysdebugCoreFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugCoreFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageEntry.setStatus("current")
_CfprSysdebugCoreFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSysdebugCoreFsmStageInstanceId_Object = MibTableColumn
cfprSysdebugCoreFsmStageInstanceId = _CfprSysdebugCoreFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1, 1),
    _CfprSysdebugCoreFsmStageInstanceId_Type()
)
cfprSysdebugCoreFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageInstanceId.setStatus("current")
_CfprSysdebugCoreFsmStageDn_Type = CfprManagedObjectDn
_CfprSysdebugCoreFsmStageDn_Object = MibTableColumn
cfprSysdebugCoreFsmStageDn = _CfprSysdebugCoreFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1, 2),
    _CfprSysdebugCoreFsmStageDn_Type()
)
cfprSysdebugCoreFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageDn.setStatus("current")
_CfprSysdebugCoreFsmStageRn_Type = SnmpAdminString
_CfprSysdebugCoreFsmStageRn_Object = MibTableColumn
cfprSysdebugCoreFsmStageRn = _CfprSysdebugCoreFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1, 3),
    _CfprSysdebugCoreFsmStageRn_Type()
)
cfprSysdebugCoreFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageRn.setStatus("current")
_CfprSysdebugCoreFsmStageDescrData_Type = SnmpAdminString
_CfprSysdebugCoreFsmStageDescrData_Object = MibTableColumn
cfprSysdebugCoreFsmStageDescrData = _CfprSysdebugCoreFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1, 4),
    _CfprSysdebugCoreFsmStageDescrData_Type()
)
cfprSysdebugCoreFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageDescrData.setStatus("current")
_CfprSysdebugCoreFsmStageLastUpdateTime_Type = DateAndTime
_CfprSysdebugCoreFsmStageLastUpdateTime_Object = MibTableColumn
cfprSysdebugCoreFsmStageLastUpdateTime = _CfprSysdebugCoreFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1, 5),
    _CfprSysdebugCoreFsmStageLastUpdateTime_Type()
)
cfprSysdebugCoreFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageLastUpdateTime.setStatus("current")
_CfprSysdebugCoreFsmStageName_Type = CfprSysdebugCoreFsmStageName
_CfprSysdebugCoreFsmStageName_Object = MibTableColumn
cfprSysdebugCoreFsmStageName = _CfprSysdebugCoreFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1, 6),
    _CfprSysdebugCoreFsmStageName_Type()
)
cfprSysdebugCoreFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageName.setStatus("current")
_CfprSysdebugCoreFsmStageOrder_Type = Gauge32
_CfprSysdebugCoreFsmStageOrder_Object = MibTableColumn
cfprSysdebugCoreFsmStageOrder = _CfprSysdebugCoreFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1, 7),
    _CfprSysdebugCoreFsmStageOrder_Type()
)
cfprSysdebugCoreFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageOrder.setStatus("current")
_CfprSysdebugCoreFsmStageRetry_Type = Gauge32
_CfprSysdebugCoreFsmStageRetry_Object = MibTableColumn
cfprSysdebugCoreFsmStageRetry = _CfprSysdebugCoreFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1, 8),
    _CfprSysdebugCoreFsmStageRetry_Type()
)
cfprSysdebugCoreFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageRetry.setStatus("current")
_CfprSysdebugCoreFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugCoreFsmStageStageStatus_Object = MibTableColumn
cfprSysdebugCoreFsmStageStageStatus = _CfprSysdebugCoreFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 9, 1, 9),
    _CfprSysdebugCoreFsmStageStageStatus_Type()
)
cfprSysdebugCoreFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmStageStageStatus.setStatus("current")
_CfprSysdebugCoreFsmTaskTable_Object = MibTable
cfprSysdebugCoreFsmTaskTable = _CfprSysdebugCoreFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 10)
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTaskTable.setStatus("current")
_CfprSysdebugCoreFsmTaskEntry_Object = MibTableRow
cfprSysdebugCoreFsmTaskEntry = _CfprSysdebugCoreFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 10, 1)
)
cfprSysdebugCoreFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugCoreFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTaskEntry.setStatus("current")
_CfprSysdebugCoreFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSysdebugCoreFsmTaskInstanceId_Object = MibTableColumn
cfprSysdebugCoreFsmTaskInstanceId = _CfprSysdebugCoreFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 10, 1, 1),
    _CfprSysdebugCoreFsmTaskInstanceId_Type()
)
cfprSysdebugCoreFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTaskInstanceId.setStatus("current")
_CfprSysdebugCoreFsmTaskDn_Type = CfprManagedObjectDn
_CfprSysdebugCoreFsmTaskDn_Object = MibTableColumn
cfprSysdebugCoreFsmTaskDn = _CfprSysdebugCoreFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 10, 1, 2),
    _CfprSysdebugCoreFsmTaskDn_Type()
)
cfprSysdebugCoreFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTaskDn.setStatus("current")
_CfprSysdebugCoreFsmTaskRn_Type = SnmpAdminString
_CfprSysdebugCoreFsmTaskRn_Object = MibTableColumn
cfprSysdebugCoreFsmTaskRn = _CfprSysdebugCoreFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 10, 1, 3),
    _CfprSysdebugCoreFsmTaskRn_Type()
)
cfprSysdebugCoreFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTaskRn.setStatus("current")
_CfprSysdebugCoreFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSysdebugCoreFsmTaskCompletion_Object = MibTableColumn
cfprSysdebugCoreFsmTaskCompletion = _CfprSysdebugCoreFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 10, 1, 4),
    _CfprSysdebugCoreFsmTaskCompletion_Type()
)
cfprSysdebugCoreFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTaskCompletion.setStatus("current")
_CfprSysdebugCoreFsmTaskFlags_Type = CfprFsmFlags
_CfprSysdebugCoreFsmTaskFlags_Object = MibTableColumn
cfprSysdebugCoreFsmTaskFlags = _CfprSysdebugCoreFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 10, 1, 5),
    _CfprSysdebugCoreFsmTaskFlags_Type()
)
cfprSysdebugCoreFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTaskFlags.setStatus("current")
_CfprSysdebugCoreFsmTaskItem_Type = CfprSysdebugCoreFsmTaskItem
_CfprSysdebugCoreFsmTaskItem_Object = MibTableColumn
cfprSysdebugCoreFsmTaskItem = _CfprSysdebugCoreFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 10, 1, 6),
    _CfprSysdebugCoreFsmTaskItem_Type()
)
cfprSysdebugCoreFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTaskItem.setStatus("current")
_CfprSysdebugCoreFsmTaskSeqId_Type = Gauge32
_CfprSysdebugCoreFsmTaskSeqId_Object = MibTableColumn
cfprSysdebugCoreFsmTaskSeqId = _CfprSysdebugCoreFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 10, 1, 7),
    _CfprSysdebugCoreFsmTaskSeqId_Type()
)
cfprSysdebugCoreFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugCoreFsmTaskSeqId.setStatus("current")
_CfprSysdebugEpTable_Object = MibTable
cfprSysdebugEpTable = _CfprSysdebugEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 11)
)
if mibBuilder.loadTexts:
    cfprSysdebugEpTable.setStatus("current")
_CfprSysdebugEpEntry_Object = MibTableRow
cfprSysdebugEpEntry = _CfprSysdebugEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 11, 1)
)
cfprSysdebugEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugEpEntry.setStatus("current")
_CfprSysdebugEpInstanceId_Type = CfprManagedObjectId
_CfprSysdebugEpInstanceId_Object = MibTableColumn
cfprSysdebugEpInstanceId = _CfprSysdebugEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 11, 1, 1),
    _CfprSysdebugEpInstanceId_Type()
)
cfprSysdebugEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugEpInstanceId.setStatus("current")
_CfprSysdebugEpDn_Type = CfprManagedObjectDn
_CfprSysdebugEpDn_Object = MibTableColumn
cfprSysdebugEpDn = _CfprSysdebugEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 11, 1, 2),
    _CfprSysdebugEpDn_Type()
)
cfprSysdebugEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugEpDn.setStatus("current")
_CfprSysdebugEpRn_Type = SnmpAdminString
_CfprSysdebugEpRn_Object = MibTableColumn
cfprSysdebugEpRn = _CfprSysdebugEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 11, 1, 3),
    _CfprSysdebugEpRn_Type()
)
cfprSysdebugEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugEpRn.setStatus("current")
_CfprSysdebugLogControlDestinationFileTable_Object = MibTable
cfprSysdebugLogControlDestinationFileTable = _CfprSysdebugLogControlDestinationFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileTable.setStatus("current")
_CfprSysdebugLogControlDestinationFileEntry_Object = MibTableRow
cfprSysdebugLogControlDestinationFileEntry = _CfprSysdebugLogControlDestinationFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12, 1)
)
cfprSysdebugLogControlDestinationFileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogControlDestinationFileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileEntry.setStatus("current")
_CfprSysdebugLogControlDestinationFileInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogControlDestinationFileInstanceId_Object = MibTableColumn
cfprSysdebugLogControlDestinationFileInstanceId = _CfprSysdebugLogControlDestinationFileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12, 1, 1),
    _CfprSysdebugLogControlDestinationFileInstanceId_Type()
)
cfprSysdebugLogControlDestinationFileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileInstanceId.setStatus("current")
_CfprSysdebugLogControlDestinationFileDn_Type = CfprManagedObjectDn
_CfprSysdebugLogControlDestinationFileDn_Object = MibTableColumn
cfprSysdebugLogControlDestinationFileDn = _CfprSysdebugLogControlDestinationFileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12, 1, 2),
    _CfprSysdebugLogControlDestinationFileDn_Type()
)
cfprSysdebugLogControlDestinationFileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileDn.setStatus("current")
_CfprSysdebugLogControlDestinationFileRn_Type = SnmpAdminString
_CfprSysdebugLogControlDestinationFileRn_Object = MibTableColumn
cfprSysdebugLogControlDestinationFileRn = _CfprSysdebugLogControlDestinationFileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12, 1, 3),
    _CfprSysdebugLogControlDestinationFileRn_Type()
)
cfprSysdebugLogControlDestinationFileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileRn.setStatus("current")
_CfprSysdebugLogControlDestinationFileBackupCount_Type = Gauge32
_CfprSysdebugLogControlDestinationFileBackupCount_Object = MibTableColumn
cfprSysdebugLogControlDestinationFileBackupCount = _CfprSysdebugLogControlDestinationFileBackupCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12, 1, 4),
    _CfprSysdebugLogControlDestinationFileBackupCount_Type()
)
cfprSysdebugLogControlDestinationFileBackupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileBackupCount.setStatus("current")
_CfprSysdebugLogControlDestinationFileDefaultLevel_Type = CfprSysdebugLogControlLevel
_CfprSysdebugLogControlDestinationFileDefaultLevel_Object = MibTableColumn
cfprSysdebugLogControlDestinationFileDefaultLevel = _CfprSysdebugLogControlDestinationFileDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12, 1, 5),
    _CfprSysdebugLogControlDestinationFileDefaultLevel_Type()
)
cfprSysdebugLogControlDestinationFileDefaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileDefaultLevel.setStatus("current")
_CfprSysdebugLogControlDestinationFileDefaultSize_Type = Gauge32
_CfprSysdebugLogControlDestinationFileDefaultSize_Object = MibTableColumn
cfprSysdebugLogControlDestinationFileDefaultSize = _CfprSysdebugLogControlDestinationFileDefaultSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12, 1, 6),
    _CfprSysdebugLogControlDestinationFileDefaultSize_Type()
)
cfprSysdebugLogControlDestinationFileDefaultSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileDefaultSize.setStatus("current")
_CfprSysdebugLogControlDestinationFileLevel_Type = CfprSysdebugLogControlLevel
_CfprSysdebugLogControlDestinationFileLevel_Object = MibTableColumn
cfprSysdebugLogControlDestinationFileLevel = _CfprSysdebugLogControlDestinationFileLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12, 1, 7),
    _CfprSysdebugLogControlDestinationFileLevel_Type()
)
cfprSysdebugLogControlDestinationFileLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileLevel.setStatus("current")
_CfprSysdebugLogControlDestinationFileSize_Type = Gauge32
_CfprSysdebugLogControlDestinationFileSize_Object = MibTableColumn
cfprSysdebugLogControlDestinationFileSize = _CfprSysdebugLogControlDestinationFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 12, 1, 8),
    _CfprSysdebugLogControlDestinationFileSize_Type()
)
cfprSysdebugLogControlDestinationFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationFileSize.setStatus("current")
_CfprSysdebugLogControlDestinationSyslogTable_Object = MibTable
cfprSysdebugLogControlDestinationSyslogTable = _CfprSysdebugLogControlDestinationSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 13)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationSyslogTable.setStatus("current")
_CfprSysdebugLogControlDestinationSyslogEntry_Object = MibTableRow
cfprSysdebugLogControlDestinationSyslogEntry = _CfprSysdebugLogControlDestinationSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 13, 1)
)
cfprSysdebugLogControlDestinationSyslogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogControlDestinationSyslogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationSyslogEntry.setStatus("current")
_CfprSysdebugLogControlDestinationSyslogInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogControlDestinationSyslogInstanceId_Object = MibTableColumn
cfprSysdebugLogControlDestinationSyslogInstanceId = _CfprSysdebugLogControlDestinationSyslogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 13, 1, 1),
    _CfprSysdebugLogControlDestinationSyslogInstanceId_Type()
)
cfprSysdebugLogControlDestinationSyslogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationSyslogInstanceId.setStatus("current")
_CfprSysdebugLogControlDestinationSyslogDn_Type = CfprManagedObjectDn
_CfprSysdebugLogControlDestinationSyslogDn_Object = MibTableColumn
cfprSysdebugLogControlDestinationSyslogDn = _CfprSysdebugLogControlDestinationSyslogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 13, 1, 2),
    _CfprSysdebugLogControlDestinationSyslogDn_Type()
)
cfprSysdebugLogControlDestinationSyslogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationSyslogDn.setStatus("current")
_CfprSysdebugLogControlDestinationSyslogRn_Type = SnmpAdminString
_CfprSysdebugLogControlDestinationSyslogRn_Object = MibTableColumn
cfprSysdebugLogControlDestinationSyslogRn = _CfprSysdebugLogControlDestinationSyslogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 13, 1, 3),
    _CfprSysdebugLogControlDestinationSyslogRn_Type()
)
cfprSysdebugLogControlDestinationSyslogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationSyslogRn.setStatus("current")
_CfprSysdebugLogControlDestinationSyslogDefaultLevel_Type = CfprSysdebugLogControlLevel
_CfprSysdebugLogControlDestinationSyslogDefaultLevel_Object = MibTableColumn
cfprSysdebugLogControlDestinationSyslogDefaultLevel = _CfprSysdebugLogControlDestinationSyslogDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 13, 1, 4),
    _CfprSysdebugLogControlDestinationSyslogDefaultLevel_Type()
)
cfprSysdebugLogControlDestinationSyslogDefaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationSyslogDefaultLevel.setStatus("current")
_CfprSysdebugLogControlDestinationSyslogLevel_Type = CfprSysdebugLogControlLevel
_CfprSysdebugLogControlDestinationSyslogLevel_Object = MibTableColumn
cfprSysdebugLogControlDestinationSyslogLevel = _CfprSysdebugLogControlDestinationSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 13, 1, 5),
    _CfprSysdebugLogControlDestinationSyslogLevel_Type()
)
cfprSysdebugLogControlDestinationSyslogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDestinationSyslogLevel.setStatus("current")
_CfprSysdebugLogControlDomainTable_Object = MibTable
cfprSysdebugLogControlDomainTable = _CfprSysdebugLogControlDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainTable.setStatus("current")
_CfprSysdebugLogControlDomainEntry_Object = MibTableRow
cfprSysdebugLogControlDomainEntry = _CfprSysdebugLogControlDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14, 1)
)
cfprSysdebugLogControlDomainEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogControlDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainEntry.setStatus("current")
_CfprSysdebugLogControlDomainInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogControlDomainInstanceId_Object = MibTableColumn
cfprSysdebugLogControlDomainInstanceId = _CfprSysdebugLogControlDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14, 1, 1),
    _CfprSysdebugLogControlDomainInstanceId_Type()
)
cfprSysdebugLogControlDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainInstanceId.setStatus("current")
_CfprSysdebugLogControlDomainDn_Type = CfprManagedObjectDn
_CfprSysdebugLogControlDomainDn_Object = MibTableColumn
cfprSysdebugLogControlDomainDn = _CfprSysdebugLogControlDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14, 1, 2),
    _CfprSysdebugLogControlDomainDn_Type()
)
cfprSysdebugLogControlDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainDn.setStatus("current")
_CfprSysdebugLogControlDomainRn_Type = SnmpAdminString
_CfprSysdebugLogControlDomainRn_Object = MibTableColumn
cfprSysdebugLogControlDomainRn = _CfprSysdebugLogControlDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14, 1, 3),
    _CfprSysdebugLogControlDomainRn_Type()
)
cfprSysdebugLogControlDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainRn.setStatus("current")
_CfprSysdebugLogControlDomainLevel_Type = CfprSysdebugLogControlLevel
_CfprSysdebugLogControlDomainLevel_Object = MibTableColumn
cfprSysdebugLogControlDomainLevel = _CfprSysdebugLogControlDomainLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14, 1, 4),
    _CfprSysdebugLogControlDomainLevel_Type()
)
cfprSysdebugLogControlDomainLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainLevel.setStatus("current")
_CfprSysdebugLogControlDomainLevelFlag_Type = TruthValue
_CfprSysdebugLogControlDomainLevelFlag_Object = MibTableColumn
cfprSysdebugLogControlDomainLevelFlag = _CfprSysdebugLogControlDomainLevelFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14, 1, 5),
    _CfprSysdebugLogControlDomainLevelFlag_Type()
)
cfprSysdebugLogControlDomainLevelFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainLevelFlag.setStatus("current")
_CfprSysdebugLogControlDomainName_Type = CfprSysdebugLogControlDomainEnum
_CfprSysdebugLogControlDomainName_Object = MibTableColumn
cfprSysdebugLogControlDomainName = _CfprSysdebugLogControlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14, 1, 6),
    _CfprSysdebugLogControlDomainName_Type()
)
cfprSysdebugLogControlDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainName.setStatus("current")
_CfprSysdebugLogControlDomainPersist_Type = TruthValue
_CfprSysdebugLogControlDomainPersist_Object = MibTableColumn
cfprSysdebugLogControlDomainPersist = _CfprSysdebugLogControlDomainPersist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14, 1, 7),
    _CfprSysdebugLogControlDomainPersist_Type()
)
cfprSysdebugLogControlDomainPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainPersist.setStatus("current")
_CfprSysdebugLogControlDomainReset_Type = TruthValue
_CfprSysdebugLogControlDomainReset_Object = MibTableColumn
cfprSysdebugLogControlDomainReset = _CfprSysdebugLogControlDomainReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 14, 1, 8),
    _CfprSysdebugLogControlDomainReset_Type()
)
cfprSysdebugLogControlDomainReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlDomainReset.setStatus("current")
_CfprSysdebugLogControlEpTable_Object = MibTable
cfprSysdebugLogControlEpTable = _CfprSysdebugLogControlEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpTable.setStatus("current")
_CfprSysdebugLogControlEpEntry_Object = MibTableRow
cfprSysdebugLogControlEpEntry = _CfprSysdebugLogControlEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1)
)
cfprSysdebugLogControlEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogControlEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpEntry.setStatus("current")
_CfprSysdebugLogControlEpInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogControlEpInstanceId_Object = MibTableColumn
cfprSysdebugLogControlEpInstanceId = _CfprSysdebugLogControlEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 1),
    _CfprSysdebugLogControlEpInstanceId_Type()
)
cfprSysdebugLogControlEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpInstanceId.setStatus("current")
_CfprSysdebugLogControlEpDn_Type = CfprManagedObjectDn
_CfprSysdebugLogControlEpDn_Object = MibTableColumn
cfprSysdebugLogControlEpDn = _CfprSysdebugLogControlEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 2),
    _CfprSysdebugLogControlEpDn_Type()
)
cfprSysdebugLogControlEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpDn.setStatus("current")
_CfprSysdebugLogControlEpRn_Type = SnmpAdminString
_CfprSysdebugLogControlEpRn_Object = MibTableColumn
cfprSysdebugLogControlEpRn = _CfprSysdebugLogControlEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 3),
    _CfprSysdebugLogControlEpRn_Type()
)
cfprSysdebugLogControlEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpRn.setStatus("current")
_CfprSysdebugLogControlEpFsmDescr_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmDescr_Object = MibTableColumn
cfprSysdebugLogControlEpFsmDescr = _CfprSysdebugLogControlEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 4),
    _CfprSysdebugLogControlEpFsmDescr_Type()
)
cfprSysdebugLogControlEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmDescr.setStatus("current")
_CfprSysdebugLogControlEpFsmPrev_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmPrev_Object = MibTableColumn
cfprSysdebugLogControlEpFsmPrev = _CfprSysdebugLogControlEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 5),
    _CfprSysdebugLogControlEpFsmPrev_Type()
)
cfprSysdebugLogControlEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmPrev.setStatus("current")
_CfprSysdebugLogControlEpFsmProgr_Type = Gauge32
_CfprSysdebugLogControlEpFsmProgr_Object = MibTableColumn
cfprSysdebugLogControlEpFsmProgr = _CfprSysdebugLogControlEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 6),
    _CfprSysdebugLogControlEpFsmProgr_Type()
)
cfprSysdebugLogControlEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmProgr.setStatus("current")
_CfprSysdebugLogControlEpFsmRmtInvErrCode_Type = Gauge32
_CfprSysdebugLogControlEpFsmRmtInvErrCode_Object = MibTableColumn
cfprSysdebugLogControlEpFsmRmtInvErrCode = _CfprSysdebugLogControlEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 7),
    _CfprSysdebugLogControlEpFsmRmtInvErrCode_Type()
)
cfprSysdebugLogControlEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmRmtInvErrCode.setStatus("current")
_CfprSysdebugLogControlEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprSysdebugLogControlEpFsmRmtInvErrDescr = _CfprSysdebugLogControlEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 8),
    _CfprSysdebugLogControlEpFsmRmtInvErrDescr_Type()
)
cfprSysdebugLogControlEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmRmtInvErrDescr.setStatus("current")
_CfprSysdebugLogControlEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugLogControlEpFsmRmtInvRslt_Object = MibTableColumn
cfprSysdebugLogControlEpFsmRmtInvRslt = _CfprSysdebugLogControlEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 9),
    _CfprSysdebugLogControlEpFsmRmtInvRslt_Type()
)
cfprSysdebugLogControlEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmRmtInvRslt.setStatus("current")
_CfprSysdebugLogControlEpFsmStageDescr_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmStageDescr_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageDescr = _CfprSysdebugLogControlEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 10),
    _CfprSysdebugLogControlEpFsmStageDescr_Type()
)
cfprSysdebugLogControlEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageDescr.setStatus("current")
_CfprSysdebugLogControlEpFsmStamp_Type = DateAndTime
_CfprSysdebugLogControlEpFsmStamp_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStamp = _CfprSysdebugLogControlEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 11),
    _CfprSysdebugLogControlEpFsmStamp_Type()
)
cfprSysdebugLogControlEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStamp.setStatus("current")
_CfprSysdebugLogControlEpFsmStatus_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmStatus_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStatus = _CfprSysdebugLogControlEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 12),
    _CfprSysdebugLogControlEpFsmStatus_Type()
)
cfprSysdebugLogControlEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStatus.setStatus("current")
_CfprSysdebugLogControlEpFsmTry_Type = Gauge32
_CfprSysdebugLogControlEpFsmTry_Object = MibTableColumn
cfprSysdebugLogControlEpFsmTry = _CfprSysdebugLogControlEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 13),
    _CfprSysdebugLogControlEpFsmTry_Type()
)
cfprSysdebugLogControlEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTry.setStatus("current")
_CfprSysdebugLogControlEpLevel_Type = CfprSysdebugLogControlLevel
_CfprSysdebugLogControlEpLevel_Object = MibTableColumn
cfprSysdebugLogControlEpLevel = _CfprSysdebugLogControlEpLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 14),
    _CfprSysdebugLogControlEpLevel_Type()
)
cfprSysdebugLogControlEpLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpLevel.setStatus("current")
_CfprSysdebugLogControlEpLevelFlag_Type = TruthValue
_CfprSysdebugLogControlEpLevelFlag_Object = MibTableColumn
cfprSysdebugLogControlEpLevelFlag = _CfprSysdebugLogControlEpLevelFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 15),
    _CfprSysdebugLogControlEpLevelFlag_Type()
)
cfprSysdebugLogControlEpLevelFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpLevelFlag.setStatus("current")
_CfprSysdebugLogControlEpPersist_Type = TruthValue
_CfprSysdebugLogControlEpPersist_Object = MibTableColumn
cfprSysdebugLogControlEpPersist = _CfprSysdebugLogControlEpPersist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 16),
    _CfprSysdebugLogControlEpPersist_Type()
)
cfprSysdebugLogControlEpPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpPersist.setStatus("current")
_CfprSysdebugLogControlEpReset_Type = TruthValue
_CfprSysdebugLogControlEpReset_Object = MibTableColumn
cfprSysdebugLogControlEpReset = _CfprSysdebugLogControlEpReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 15, 1, 17),
    _CfprSysdebugLogControlEpReset_Type()
)
cfprSysdebugLogControlEpReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpReset.setStatus("current")
_CfprSysdebugLogControlEpFsmTable_Object = MibTable
cfprSysdebugLogControlEpFsmTable = _CfprSysdebugLogControlEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTable.setStatus("current")
_CfprSysdebugLogControlEpFsmEntry_Object = MibTableRow
cfprSysdebugLogControlEpFsmEntry = _CfprSysdebugLogControlEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1)
)
cfprSysdebugLogControlEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogControlEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmEntry.setStatus("current")
_CfprSysdebugLogControlEpFsmInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogControlEpFsmInstanceId_Object = MibTableColumn
cfprSysdebugLogControlEpFsmInstanceId = _CfprSysdebugLogControlEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 1),
    _CfprSysdebugLogControlEpFsmInstanceId_Type()
)
cfprSysdebugLogControlEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmInstanceId.setStatus("current")
_CfprSysdebugLogControlEpFsmDn_Type = CfprManagedObjectDn
_CfprSysdebugLogControlEpFsmDn_Object = MibTableColumn
cfprSysdebugLogControlEpFsmDn = _CfprSysdebugLogControlEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 2),
    _CfprSysdebugLogControlEpFsmDn_Type()
)
cfprSysdebugLogControlEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmDn.setStatus("current")
_CfprSysdebugLogControlEpFsmRn_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmRn_Object = MibTableColumn
cfprSysdebugLogControlEpFsmRn = _CfprSysdebugLogControlEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 3),
    _CfprSysdebugLogControlEpFsmRn_Type()
)
cfprSysdebugLogControlEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmRn.setStatus("current")
_CfprSysdebugLogControlEpFsmCompletionTime_Type = DateAndTime
_CfprSysdebugLogControlEpFsmCompletionTime_Object = MibTableColumn
cfprSysdebugLogControlEpFsmCompletionTime = _CfprSysdebugLogControlEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 4),
    _CfprSysdebugLogControlEpFsmCompletionTime_Type()
)
cfprSysdebugLogControlEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmCompletionTime.setStatus("current")
_CfprSysdebugLogControlEpFsmCurrentFsm_Type = CfprSysdebugLogControlEpFsmCurrentFsm
_CfprSysdebugLogControlEpFsmCurrentFsm_Object = MibTableColumn
cfprSysdebugLogControlEpFsmCurrentFsm = _CfprSysdebugLogControlEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 5),
    _CfprSysdebugLogControlEpFsmCurrentFsm_Type()
)
cfprSysdebugLogControlEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmCurrentFsm.setStatus("current")
_CfprSysdebugLogControlEpFsmDescrData_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmDescrData_Object = MibTableColumn
cfprSysdebugLogControlEpFsmDescrData = _CfprSysdebugLogControlEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 6),
    _CfprSysdebugLogControlEpFsmDescrData_Type()
)
cfprSysdebugLogControlEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmDescrData.setStatus("current")
_CfprSysdebugLogControlEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugLogControlEpFsmFsmStatus_Object = MibTableColumn
cfprSysdebugLogControlEpFsmFsmStatus = _CfprSysdebugLogControlEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 7),
    _CfprSysdebugLogControlEpFsmFsmStatus_Type()
)
cfprSysdebugLogControlEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmFsmStatus.setStatus("current")
_CfprSysdebugLogControlEpFsmProgress_Type = Gauge32
_CfprSysdebugLogControlEpFsmProgress_Object = MibTableColumn
cfprSysdebugLogControlEpFsmProgress = _CfprSysdebugLogControlEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 8),
    _CfprSysdebugLogControlEpFsmProgress_Type()
)
cfprSysdebugLogControlEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmProgress.setStatus("current")
_CfprSysdebugLogControlEpFsmRmtErrCode_Type = Gauge32
_CfprSysdebugLogControlEpFsmRmtErrCode_Object = MibTableColumn
cfprSysdebugLogControlEpFsmRmtErrCode = _CfprSysdebugLogControlEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 9),
    _CfprSysdebugLogControlEpFsmRmtErrCode_Type()
)
cfprSysdebugLogControlEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmRmtErrCode.setStatus("current")
_CfprSysdebugLogControlEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmRmtErrDescr_Object = MibTableColumn
cfprSysdebugLogControlEpFsmRmtErrDescr = _CfprSysdebugLogControlEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 10),
    _CfprSysdebugLogControlEpFsmRmtErrDescr_Type()
)
cfprSysdebugLogControlEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmRmtErrDescr.setStatus("current")
_CfprSysdebugLogControlEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugLogControlEpFsmRmtRslt_Object = MibTableColumn
cfprSysdebugLogControlEpFsmRmtRslt = _CfprSysdebugLogControlEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 16, 1, 11),
    _CfprSysdebugLogControlEpFsmRmtRslt_Type()
)
cfprSysdebugLogControlEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmRmtRslt.setStatus("current")
_CfprSysdebugLogControlEpFsmStageTable_Object = MibTable
cfprSysdebugLogControlEpFsmStageTable = _CfprSysdebugLogControlEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageTable.setStatus("current")
_CfprSysdebugLogControlEpFsmStageEntry_Object = MibTableRow
cfprSysdebugLogControlEpFsmStageEntry = _CfprSysdebugLogControlEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1)
)
cfprSysdebugLogControlEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogControlEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageEntry.setStatus("current")
_CfprSysdebugLogControlEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogControlEpFsmStageInstanceId_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageInstanceId = _CfprSysdebugLogControlEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1, 1),
    _CfprSysdebugLogControlEpFsmStageInstanceId_Type()
)
cfprSysdebugLogControlEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageInstanceId.setStatus("current")
_CfprSysdebugLogControlEpFsmStageDn_Type = CfprManagedObjectDn
_CfprSysdebugLogControlEpFsmStageDn_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageDn = _CfprSysdebugLogControlEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1, 2),
    _CfprSysdebugLogControlEpFsmStageDn_Type()
)
cfprSysdebugLogControlEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageDn.setStatus("current")
_CfprSysdebugLogControlEpFsmStageRn_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmStageRn_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageRn = _CfprSysdebugLogControlEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1, 3),
    _CfprSysdebugLogControlEpFsmStageRn_Type()
)
cfprSysdebugLogControlEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageRn.setStatus("current")
_CfprSysdebugLogControlEpFsmStageDescrData_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmStageDescrData_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageDescrData = _CfprSysdebugLogControlEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1, 4),
    _CfprSysdebugLogControlEpFsmStageDescrData_Type()
)
cfprSysdebugLogControlEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageDescrData.setStatus("current")
_CfprSysdebugLogControlEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprSysdebugLogControlEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageLastUpdateTime = _CfprSysdebugLogControlEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1, 5),
    _CfprSysdebugLogControlEpFsmStageLastUpdateTime_Type()
)
cfprSysdebugLogControlEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageLastUpdateTime.setStatus("current")
_CfprSysdebugLogControlEpFsmStageName_Type = CfprSysdebugLogControlEpFsmStageName
_CfprSysdebugLogControlEpFsmStageName_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageName = _CfprSysdebugLogControlEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1, 6),
    _CfprSysdebugLogControlEpFsmStageName_Type()
)
cfprSysdebugLogControlEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageName.setStatus("current")
_CfprSysdebugLogControlEpFsmStageOrder_Type = Gauge32
_CfprSysdebugLogControlEpFsmStageOrder_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageOrder = _CfprSysdebugLogControlEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1, 7),
    _CfprSysdebugLogControlEpFsmStageOrder_Type()
)
cfprSysdebugLogControlEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageOrder.setStatus("current")
_CfprSysdebugLogControlEpFsmStageRetry_Type = Gauge32
_CfprSysdebugLogControlEpFsmStageRetry_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageRetry = _CfprSysdebugLogControlEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1, 8),
    _CfprSysdebugLogControlEpFsmStageRetry_Type()
)
cfprSysdebugLogControlEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageRetry.setStatus("current")
_CfprSysdebugLogControlEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugLogControlEpFsmStageStageStatus_Object = MibTableColumn
cfprSysdebugLogControlEpFsmStageStageStatus = _CfprSysdebugLogControlEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 17, 1, 9),
    _CfprSysdebugLogControlEpFsmStageStageStatus_Type()
)
cfprSysdebugLogControlEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmStageStageStatus.setStatus("current")
_CfprSysdebugLogControlEpFsmTaskTable_Object = MibTable
cfprSysdebugLogControlEpFsmTaskTable = _CfprSysdebugLogControlEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 18)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTaskTable.setStatus("current")
_CfprSysdebugLogControlEpFsmTaskEntry_Object = MibTableRow
cfprSysdebugLogControlEpFsmTaskEntry = _CfprSysdebugLogControlEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 18, 1)
)
cfprSysdebugLogControlEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogControlEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTaskEntry.setStatus("current")
_CfprSysdebugLogControlEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogControlEpFsmTaskInstanceId_Object = MibTableColumn
cfprSysdebugLogControlEpFsmTaskInstanceId = _CfprSysdebugLogControlEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 18, 1, 1),
    _CfprSysdebugLogControlEpFsmTaskInstanceId_Type()
)
cfprSysdebugLogControlEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTaskInstanceId.setStatus("current")
_CfprSysdebugLogControlEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprSysdebugLogControlEpFsmTaskDn_Object = MibTableColumn
cfprSysdebugLogControlEpFsmTaskDn = _CfprSysdebugLogControlEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 18, 1, 2),
    _CfprSysdebugLogControlEpFsmTaskDn_Type()
)
cfprSysdebugLogControlEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTaskDn.setStatus("current")
_CfprSysdebugLogControlEpFsmTaskRn_Type = SnmpAdminString
_CfprSysdebugLogControlEpFsmTaskRn_Object = MibTableColumn
cfprSysdebugLogControlEpFsmTaskRn = _CfprSysdebugLogControlEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 18, 1, 3),
    _CfprSysdebugLogControlEpFsmTaskRn_Type()
)
cfprSysdebugLogControlEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTaskRn.setStatus("current")
_CfprSysdebugLogControlEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSysdebugLogControlEpFsmTaskCompletion_Object = MibTableColumn
cfprSysdebugLogControlEpFsmTaskCompletion = _CfprSysdebugLogControlEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 18, 1, 4),
    _CfprSysdebugLogControlEpFsmTaskCompletion_Type()
)
cfprSysdebugLogControlEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTaskCompletion.setStatus("current")
_CfprSysdebugLogControlEpFsmTaskFlags_Type = CfprFsmFlags
_CfprSysdebugLogControlEpFsmTaskFlags_Object = MibTableColumn
cfprSysdebugLogControlEpFsmTaskFlags = _CfprSysdebugLogControlEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 18, 1, 5),
    _CfprSysdebugLogControlEpFsmTaskFlags_Type()
)
cfprSysdebugLogControlEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTaskFlags.setStatus("current")
_CfprSysdebugLogControlEpFsmTaskItem_Type = CfprSysdebugLogControlEpFsmTaskItem
_CfprSysdebugLogControlEpFsmTaskItem_Object = MibTableColumn
cfprSysdebugLogControlEpFsmTaskItem = _CfprSysdebugLogControlEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 18, 1, 6),
    _CfprSysdebugLogControlEpFsmTaskItem_Type()
)
cfprSysdebugLogControlEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTaskItem.setStatus("current")
_CfprSysdebugLogControlEpFsmTaskSeqId_Type = Gauge32
_CfprSysdebugLogControlEpFsmTaskSeqId_Object = MibTableColumn
cfprSysdebugLogControlEpFsmTaskSeqId = _CfprSysdebugLogControlEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 18, 1, 7),
    _CfprSysdebugLogControlEpFsmTaskSeqId_Type()
)
cfprSysdebugLogControlEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlEpFsmTaskSeqId.setStatus("current")
_CfprSysdebugLogControlModuleTable_Object = MibTable
cfprSysdebugLogControlModuleTable = _CfprSysdebugLogControlModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 19)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlModuleTable.setStatus("current")
_CfprSysdebugLogControlModuleEntry_Object = MibTableRow
cfprSysdebugLogControlModuleEntry = _CfprSysdebugLogControlModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 19, 1)
)
cfprSysdebugLogControlModuleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogControlModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogControlModuleEntry.setStatus("current")
_CfprSysdebugLogControlModuleInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogControlModuleInstanceId_Object = MibTableColumn
cfprSysdebugLogControlModuleInstanceId = _CfprSysdebugLogControlModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 19, 1, 1),
    _CfprSysdebugLogControlModuleInstanceId_Type()
)
cfprSysdebugLogControlModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlModuleInstanceId.setStatus("current")
_CfprSysdebugLogControlModuleDn_Type = CfprManagedObjectDn
_CfprSysdebugLogControlModuleDn_Object = MibTableColumn
cfprSysdebugLogControlModuleDn = _CfprSysdebugLogControlModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 19, 1, 2),
    _CfprSysdebugLogControlModuleDn_Type()
)
cfprSysdebugLogControlModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlModuleDn.setStatus("current")
_CfprSysdebugLogControlModuleRn_Type = SnmpAdminString
_CfprSysdebugLogControlModuleRn_Object = MibTableColumn
cfprSysdebugLogControlModuleRn = _CfprSysdebugLogControlModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 19, 1, 3),
    _CfprSysdebugLogControlModuleRn_Type()
)
cfprSysdebugLogControlModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlModuleRn.setStatus("current")
_CfprSysdebugLogControlModuleDefaultLevel_Type = CfprSysdebugLogControlLevel
_CfprSysdebugLogControlModuleDefaultLevel_Object = MibTableColumn
cfprSysdebugLogControlModuleDefaultLevel = _CfprSysdebugLogControlModuleDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 19, 1, 4),
    _CfprSysdebugLogControlModuleDefaultLevel_Type()
)
cfprSysdebugLogControlModuleDefaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlModuleDefaultLevel.setStatus("current")
_CfprSysdebugLogControlModuleLevel_Type = CfprSysdebugLogControlLevel
_CfprSysdebugLogControlModuleLevel_Object = MibTableColumn
cfprSysdebugLogControlModuleLevel = _CfprSysdebugLogControlModuleLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 19, 1, 5),
    _CfprSysdebugLogControlModuleLevel_Type()
)
cfprSysdebugLogControlModuleLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlModuleLevel.setStatus("current")
_CfprSysdebugLogControlModuleName_Type = SnmpAdminString
_CfprSysdebugLogControlModuleName_Object = MibTableColumn
cfprSysdebugLogControlModuleName = _CfprSysdebugLogControlModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 19, 1, 6),
    _CfprSysdebugLogControlModuleName_Type()
)
cfprSysdebugLogControlModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlModuleName.setStatus("current")
_CfprSysdebugLogControlModuleReset_Type = TruthValue
_CfprSysdebugLogControlModuleReset_Object = MibTableColumn
cfprSysdebugLogControlModuleReset = _CfprSysdebugLogControlModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 19, 1, 7),
    _CfprSysdebugLogControlModuleReset_Type()
)
cfprSysdebugLogControlModuleReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogControlModuleReset.setStatus("current")
_CfprSysdebugLogExportPolicyTable_Object = MibTable
cfprSysdebugLogExportPolicyTable = _CfprSysdebugLogExportPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyTable.setStatus("current")
_CfprSysdebugLogExportPolicyEntry_Object = MibTableRow
cfprSysdebugLogExportPolicyEntry = _CfprSysdebugLogExportPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1)
)
cfprSysdebugLogExportPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogExportPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyEntry.setStatus("current")
_CfprSysdebugLogExportPolicyInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogExportPolicyInstanceId_Object = MibTableColumn
cfprSysdebugLogExportPolicyInstanceId = _CfprSysdebugLogExportPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 1),
    _CfprSysdebugLogExportPolicyInstanceId_Type()
)
cfprSysdebugLogExportPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyInstanceId.setStatus("current")
_CfprSysdebugLogExportPolicyDn_Type = CfprManagedObjectDn
_CfprSysdebugLogExportPolicyDn_Object = MibTableColumn
cfprSysdebugLogExportPolicyDn = _CfprSysdebugLogExportPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 2),
    _CfprSysdebugLogExportPolicyDn_Type()
)
cfprSysdebugLogExportPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyDn.setStatus("current")
_CfprSysdebugLogExportPolicyRn_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyRn_Object = MibTableColumn
cfprSysdebugLogExportPolicyRn = _CfprSysdebugLogExportPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 3),
    _CfprSysdebugLogExportPolicyRn_Type()
)
cfprSysdebugLogExportPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyRn.setStatus("current")
_CfprSysdebugLogExportPolicyAdminState_Type = CfprCommClientAdminState
_CfprSysdebugLogExportPolicyAdminState_Object = MibTableColumn
cfprSysdebugLogExportPolicyAdminState = _CfprSysdebugLogExportPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 4),
    _CfprSysdebugLogExportPolicyAdminState_Type()
)
cfprSysdebugLogExportPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyAdminState.setStatus("current")
_CfprSysdebugLogExportPolicyDescr_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyDescr_Object = MibTableColumn
cfprSysdebugLogExportPolicyDescr = _CfprSysdebugLogExportPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 5),
    _CfprSysdebugLogExportPolicyDescr_Type()
)
cfprSysdebugLogExportPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyDescr.setStatus("current")
_CfprSysdebugLogExportPolicyFsmDescr_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmDescr_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmDescr = _CfprSysdebugLogExportPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 6),
    _CfprSysdebugLogExportPolicyFsmDescr_Type()
)
cfprSysdebugLogExportPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmDescr.setStatus("current")
_CfprSysdebugLogExportPolicyFsmPrev_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmPrev_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmPrev = _CfprSysdebugLogExportPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 7),
    _CfprSysdebugLogExportPolicyFsmPrev_Type()
)
cfprSysdebugLogExportPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmPrev.setStatus("current")
_CfprSysdebugLogExportPolicyFsmProgr_Type = Gauge32
_CfprSysdebugLogExportPolicyFsmProgr_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmProgr = _CfprSysdebugLogExportPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 8),
    _CfprSysdebugLogExportPolicyFsmProgr_Type()
)
cfprSysdebugLogExportPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmProgr.setStatus("current")
_CfprSysdebugLogExportPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprSysdebugLogExportPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmRmtInvErrCode = _CfprSysdebugLogExportPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 9),
    _CfprSysdebugLogExportPolicyFsmRmtInvErrCode_Type()
)
cfprSysdebugLogExportPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmRmtInvErrCode.setStatus("current")
_CfprSysdebugLogExportPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmRmtInvErrDescr = _CfprSysdebugLogExportPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 10),
    _CfprSysdebugLogExportPolicyFsmRmtInvErrDescr_Type()
)
cfprSysdebugLogExportPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprSysdebugLogExportPolicyFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugLogExportPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmRmtInvRslt = _CfprSysdebugLogExportPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 11),
    _CfprSysdebugLogExportPolicyFsmRmtInvRslt_Type()
)
cfprSysdebugLogExportPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmRmtInvRslt.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageDescr_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmStageDescr_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageDescr = _CfprSysdebugLogExportPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 12),
    _CfprSysdebugLogExportPolicyFsmStageDescr_Type()
)
cfprSysdebugLogExportPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageDescr.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStamp_Type = DateAndTime
_CfprSysdebugLogExportPolicyFsmStamp_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStamp = _CfprSysdebugLogExportPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 13),
    _CfprSysdebugLogExportPolicyFsmStamp_Type()
)
cfprSysdebugLogExportPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStamp.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStatus_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmStatus_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStatus = _CfprSysdebugLogExportPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 14),
    _CfprSysdebugLogExportPolicyFsmStatus_Type()
)
cfprSysdebugLogExportPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStatus.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTry_Type = Gauge32
_CfprSysdebugLogExportPolicyFsmTry_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmTry = _CfprSysdebugLogExportPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 15),
    _CfprSysdebugLogExportPolicyFsmTry_Type()
)
cfprSysdebugLogExportPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTry.setStatus("current")
_CfprSysdebugLogExportPolicyHostname_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyHostname_Object = MibTableColumn
cfprSysdebugLogExportPolicyHostname = _CfprSysdebugLogExportPolicyHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 16),
    _CfprSysdebugLogExportPolicyHostname_Type()
)
cfprSysdebugLogExportPolicyHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyHostname.setStatus("current")
_CfprSysdebugLogExportPolicyIntId_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyIntId_Object = MibTableColumn
cfprSysdebugLogExportPolicyIntId = _CfprSysdebugLogExportPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 17),
    _CfprSysdebugLogExportPolicyIntId_Type()
)
cfprSysdebugLogExportPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyIntId.setStatus("current")
_CfprSysdebugLogExportPolicyName_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyName_Object = MibTableColumn
cfprSysdebugLogExportPolicyName = _CfprSysdebugLogExportPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 18),
    _CfprSysdebugLogExportPolicyName_Type()
)
cfprSysdebugLogExportPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyName.setStatus("current")
_CfprSysdebugLogExportPolicyPasswordlessSsh_Type = TruthValue
_CfprSysdebugLogExportPolicyPasswordlessSsh_Object = MibTableColumn
cfprSysdebugLogExportPolicyPasswordlessSsh = _CfprSysdebugLogExportPolicyPasswordlessSsh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 19),
    _CfprSysdebugLogExportPolicyPasswordlessSsh_Type()
)
cfprSysdebugLogExportPolicyPasswordlessSsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyPasswordlessSsh.setStatus("current")
_CfprSysdebugLogExportPolicyPath_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyPath_Object = MibTableColumn
cfprSysdebugLogExportPolicyPath = _CfprSysdebugLogExportPolicyPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 20),
    _CfprSysdebugLogExportPolicyPath_Type()
)
cfprSysdebugLogExportPolicyPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyPath.setStatus("current")
_CfprSysdebugLogExportPolicyPolicyLevel_Type = Gauge32
_CfprSysdebugLogExportPolicyPolicyLevel_Object = MibTableColumn
cfprSysdebugLogExportPolicyPolicyLevel = _CfprSysdebugLogExportPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 21),
    _CfprSysdebugLogExportPolicyPolicyLevel_Type()
)
cfprSysdebugLogExportPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyPolicyLevel.setStatus("current")
_CfprSysdebugLogExportPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprSysdebugLogExportPolicyPolicyOwner_Object = MibTableColumn
cfprSysdebugLogExportPolicyPolicyOwner = _CfprSysdebugLogExportPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 22),
    _CfprSysdebugLogExportPolicyPolicyOwner_Type()
)
cfprSysdebugLogExportPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyPolicyOwner.setStatus("current")
_CfprSysdebugLogExportPolicyPostAction_Type = CfprSysfileExporterPostAction
_CfprSysdebugLogExportPolicyPostAction_Object = MibTableColumn
cfprSysdebugLogExportPolicyPostAction = _CfprSysdebugLogExportPolicyPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 23),
    _CfprSysdebugLogExportPolicyPostAction_Type()
)
cfprSysdebugLogExportPolicyPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyPostAction.setStatus("current")
_CfprSysdebugLogExportPolicyProto_Type = CfprSysdebugLogExportPolicyProto
_CfprSysdebugLogExportPolicyProto_Object = MibTableColumn
cfprSysdebugLogExportPolicyProto = _CfprSysdebugLogExportPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 24),
    _CfprSysdebugLogExportPolicyProto_Type()
)
cfprSysdebugLogExportPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyProto.setStatus("current")
_CfprSysdebugLogExportPolicyPwd_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyPwd_Object = MibTableColumn
cfprSysdebugLogExportPolicyPwd = _CfprSysdebugLogExportPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 25),
    _CfprSysdebugLogExportPolicyPwd_Type()
)
cfprSysdebugLogExportPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyPwd.setStatus("current")
_CfprSysdebugLogExportPolicyUser_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyUser_Object = MibTableColumn
cfprSysdebugLogExportPolicyUser = _CfprSysdebugLogExportPolicyUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 20, 1, 26),
    _CfprSysdebugLogExportPolicyUser_Type()
)
cfprSysdebugLogExportPolicyUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyUser.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTable_Object = MibTable
cfprSysdebugLogExportPolicyFsmTable = _CfprSysdebugLogExportPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTable.setStatus("current")
_CfprSysdebugLogExportPolicyFsmEntry_Object = MibTableRow
cfprSysdebugLogExportPolicyFsmEntry = _CfprSysdebugLogExportPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1)
)
cfprSysdebugLogExportPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogExportPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmEntry.setStatus("current")
_CfprSysdebugLogExportPolicyFsmInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogExportPolicyFsmInstanceId_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmInstanceId = _CfprSysdebugLogExportPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 1),
    _CfprSysdebugLogExportPolicyFsmInstanceId_Type()
)
cfprSysdebugLogExportPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmInstanceId.setStatus("current")
_CfprSysdebugLogExportPolicyFsmDn_Type = CfprManagedObjectDn
_CfprSysdebugLogExportPolicyFsmDn_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmDn = _CfprSysdebugLogExportPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 2),
    _CfprSysdebugLogExportPolicyFsmDn_Type()
)
cfprSysdebugLogExportPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmDn.setStatus("current")
_CfprSysdebugLogExportPolicyFsmRn_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmRn_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmRn = _CfprSysdebugLogExportPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 3),
    _CfprSysdebugLogExportPolicyFsmRn_Type()
)
cfprSysdebugLogExportPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmRn.setStatus("current")
_CfprSysdebugLogExportPolicyFsmCompletionTime_Type = DateAndTime
_CfprSysdebugLogExportPolicyFsmCompletionTime_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmCompletionTime = _CfprSysdebugLogExportPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 4),
    _CfprSysdebugLogExportPolicyFsmCompletionTime_Type()
)
cfprSysdebugLogExportPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmCompletionTime.setStatus("current")
_CfprSysdebugLogExportPolicyFsmCurrentFsm_Type = CfprSysdebugLogExportPolicyFsmCurrentFsm
_CfprSysdebugLogExportPolicyFsmCurrentFsm_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmCurrentFsm = _CfprSysdebugLogExportPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 5),
    _CfprSysdebugLogExportPolicyFsmCurrentFsm_Type()
)
cfprSysdebugLogExportPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmCurrentFsm.setStatus("current")
_CfprSysdebugLogExportPolicyFsmDescrData_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmDescrData_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmDescrData = _CfprSysdebugLogExportPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 6),
    _CfprSysdebugLogExportPolicyFsmDescrData_Type()
)
cfprSysdebugLogExportPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmDescrData.setStatus("current")
_CfprSysdebugLogExportPolicyFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugLogExportPolicyFsmFsmStatus_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmFsmStatus = _CfprSysdebugLogExportPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 7),
    _CfprSysdebugLogExportPolicyFsmFsmStatus_Type()
)
cfprSysdebugLogExportPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmFsmStatus.setStatus("current")
_CfprSysdebugLogExportPolicyFsmProgress_Type = Gauge32
_CfprSysdebugLogExportPolicyFsmProgress_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmProgress = _CfprSysdebugLogExportPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 8),
    _CfprSysdebugLogExportPolicyFsmProgress_Type()
)
cfprSysdebugLogExportPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmProgress.setStatus("current")
_CfprSysdebugLogExportPolicyFsmRmtErrCode_Type = Gauge32
_CfprSysdebugLogExportPolicyFsmRmtErrCode_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmRmtErrCode = _CfprSysdebugLogExportPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 9),
    _CfprSysdebugLogExportPolicyFsmRmtErrCode_Type()
)
cfprSysdebugLogExportPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmRmtErrCode.setStatus("current")
_CfprSysdebugLogExportPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmRmtErrDescr = _CfprSysdebugLogExportPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 10),
    _CfprSysdebugLogExportPolicyFsmRmtErrDescr_Type()
)
cfprSysdebugLogExportPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmRmtErrDescr.setStatus("current")
_CfprSysdebugLogExportPolicyFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugLogExportPolicyFsmRmtRslt_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmRmtRslt = _CfprSysdebugLogExportPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 21, 1, 11),
    _CfprSysdebugLogExportPolicyFsmRmtRslt_Type()
)
cfprSysdebugLogExportPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmRmtRslt.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageTable_Object = MibTable
cfprSysdebugLogExportPolicyFsmStageTable = _CfprSysdebugLogExportPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageTable.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageEntry_Object = MibTableRow
cfprSysdebugLogExportPolicyFsmStageEntry = _CfprSysdebugLogExportPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1)
)
cfprSysdebugLogExportPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogExportPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageEntry.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogExportPolicyFsmStageInstanceId_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageInstanceId = _CfprSysdebugLogExportPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1, 1),
    _CfprSysdebugLogExportPolicyFsmStageInstanceId_Type()
)
cfprSysdebugLogExportPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageInstanceId.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageDn_Type = CfprManagedObjectDn
_CfprSysdebugLogExportPolicyFsmStageDn_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageDn = _CfprSysdebugLogExportPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1, 2),
    _CfprSysdebugLogExportPolicyFsmStageDn_Type()
)
cfprSysdebugLogExportPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageDn.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageRn_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmStageRn_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageRn = _CfprSysdebugLogExportPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1, 3),
    _CfprSysdebugLogExportPolicyFsmStageRn_Type()
)
cfprSysdebugLogExportPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageRn.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmStageDescrData_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageDescrData = _CfprSysdebugLogExportPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1, 4),
    _CfprSysdebugLogExportPolicyFsmStageDescrData_Type()
)
cfprSysdebugLogExportPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageDescrData.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprSysdebugLogExportPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageLastUpdateTime = _CfprSysdebugLogExportPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1, 5),
    _CfprSysdebugLogExportPolicyFsmStageLastUpdateTime_Type()
)
cfprSysdebugLogExportPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageName_Type = CfprSysdebugLogExportPolicyFsmStageName
_CfprSysdebugLogExportPolicyFsmStageName_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageName = _CfprSysdebugLogExportPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1, 6),
    _CfprSysdebugLogExportPolicyFsmStageName_Type()
)
cfprSysdebugLogExportPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageName.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageOrder_Type = Gauge32
_CfprSysdebugLogExportPolicyFsmStageOrder_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageOrder = _CfprSysdebugLogExportPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1, 7),
    _CfprSysdebugLogExportPolicyFsmStageOrder_Type()
)
cfprSysdebugLogExportPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageOrder.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageRetry_Type = Gauge32
_CfprSysdebugLogExportPolicyFsmStageRetry_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageRetry = _CfprSysdebugLogExportPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1, 8),
    _CfprSysdebugLogExportPolicyFsmStageRetry_Type()
)
cfprSysdebugLogExportPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageRetry.setStatus("current")
_CfprSysdebugLogExportPolicyFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugLogExportPolicyFsmStageStageStatus_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmStageStageStatus = _CfprSysdebugLogExportPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 22, 1, 9),
    _CfprSysdebugLogExportPolicyFsmStageStageStatus_Type()
)
cfprSysdebugLogExportPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmStageStageStatus.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTaskTable_Object = MibTable
cfprSysdebugLogExportPolicyFsmTaskTable = _CfprSysdebugLogExportPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 23)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTaskTable.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTaskEntry_Object = MibTableRow
cfprSysdebugLogExportPolicyFsmTaskEntry = _CfprSysdebugLogExportPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 23, 1)
)
cfprSysdebugLogExportPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogExportPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTaskEntry.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogExportPolicyFsmTaskInstanceId_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmTaskInstanceId = _CfprSysdebugLogExportPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 23, 1, 1),
    _CfprSysdebugLogExportPolicyFsmTaskInstanceId_Type()
)
cfprSysdebugLogExportPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTaskInstanceId.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTaskDn_Type = CfprManagedObjectDn
_CfprSysdebugLogExportPolicyFsmTaskDn_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmTaskDn = _CfprSysdebugLogExportPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 23, 1, 2),
    _CfprSysdebugLogExportPolicyFsmTaskDn_Type()
)
cfprSysdebugLogExportPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTaskDn.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTaskRn_Type = SnmpAdminString
_CfprSysdebugLogExportPolicyFsmTaskRn_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmTaskRn = _CfprSysdebugLogExportPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 23, 1, 3),
    _CfprSysdebugLogExportPolicyFsmTaskRn_Type()
)
cfprSysdebugLogExportPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTaskRn.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSysdebugLogExportPolicyFsmTaskCompletion_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmTaskCompletion = _CfprSysdebugLogExportPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 23, 1, 4),
    _CfprSysdebugLogExportPolicyFsmTaskCompletion_Type()
)
cfprSysdebugLogExportPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTaskCompletion.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTaskFlags_Type = CfprFsmFlags
_CfprSysdebugLogExportPolicyFsmTaskFlags_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmTaskFlags = _CfprSysdebugLogExportPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 23, 1, 5),
    _CfprSysdebugLogExportPolicyFsmTaskFlags_Type()
)
cfprSysdebugLogExportPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTaskFlags.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTaskItem_Type = CfprSysdebugLogExportPolicyFsmTaskItem
_CfprSysdebugLogExportPolicyFsmTaskItem_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmTaskItem = _CfprSysdebugLogExportPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 23, 1, 6),
    _CfprSysdebugLogExportPolicyFsmTaskItem_Type()
)
cfprSysdebugLogExportPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTaskItem.setStatus("current")
_CfprSysdebugLogExportPolicyFsmTaskSeqId_Type = Gauge32
_CfprSysdebugLogExportPolicyFsmTaskSeqId_Object = MibTableColumn
cfprSysdebugLogExportPolicyFsmTaskSeqId = _CfprSysdebugLogExportPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 23, 1, 7),
    _CfprSysdebugLogExportPolicyFsmTaskSeqId_Type()
)
cfprSysdebugLogExportPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportPolicyFsmTaskSeqId.setStatus("current")
_CfprSysdebugLogExportStatusTable_Object = MibTable
cfprSysdebugLogExportStatusTable = _CfprSysdebugLogExportStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 24)
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportStatusTable.setStatus("current")
_CfprSysdebugLogExportStatusEntry_Object = MibTableRow
cfprSysdebugLogExportStatusEntry = _CfprSysdebugLogExportStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 24, 1)
)
cfprSysdebugLogExportStatusEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugLogExportStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugLogExportStatusEntry.setStatus("current")
_CfprSysdebugLogExportStatusInstanceId_Type = CfprManagedObjectId
_CfprSysdebugLogExportStatusInstanceId_Object = MibTableColumn
cfprSysdebugLogExportStatusInstanceId = _CfprSysdebugLogExportStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 24, 1, 1),
    _CfprSysdebugLogExportStatusInstanceId_Type()
)
cfprSysdebugLogExportStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportStatusInstanceId.setStatus("current")
_CfprSysdebugLogExportStatusDn_Type = CfprManagedObjectDn
_CfprSysdebugLogExportStatusDn_Object = MibTableColumn
cfprSysdebugLogExportStatusDn = _CfprSysdebugLogExportStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 24, 1, 2),
    _CfprSysdebugLogExportStatusDn_Type()
)
cfprSysdebugLogExportStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportStatusDn.setStatus("current")
_CfprSysdebugLogExportStatusRn_Type = SnmpAdminString
_CfprSysdebugLogExportStatusRn_Object = MibTableColumn
cfprSysdebugLogExportStatusRn = _CfprSysdebugLogExportStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 24, 1, 3),
    _CfprSysdebugLogExportStatusRn_Type()
)
cfprSysdebugLogExportStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportStatusRn.setStatus("current")
_CfprSysdebugLogExportStatusExportFailureReason_Type = SnmpAdminString
_CfprSysdebugLogExportStatusExportFailureReason_Object = MibTableColumn
cfprSysdebugLogExportStatusExportFailureReason = _CfprSysdebugLogExportStatusExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 24, 1, 4),
    _CfprSysdebugLogExportStatusExportFailureReason_Type()
)
cfprSysdebugLogExportStatusExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportStatusExportFailureReason.setStatus("current")
_CfprSysdebugLogExportStatusExportStatus_Type = CfprSysdebugExportStatus
_CfprSysdebugLogExportStatusExportStatus_Object = MibTableColumn
cfprSysdebugLogExportStatusExportStatus = _CfprSysdebugLogExportStatusExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 24, 1, 5),
    _CfprSysdebugLogExportStatusExportStatus_Type()
)
cfprSysdebugLogExportStatusExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportStatusExportStatus.setStatus("current")
_CfprSysdebugLogExportStatusSwitchId_Type = CfprNetworkSwitchId
_CfprSysdebugLogExportStatusSwitchId_Object = MibTableColumn
cfprSysdebugLogExportStatusSwitchId = _CfprSysdebugLogExportStatusSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 24, 1, 6),
    _CfprSysdebugLogExportStatusSwitchId_Type()
)
cfprSysdebugLogExportStatusSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugLogExportStatusSwitchId.setStatus("current")
_CfprSysdebugMEpLogTable_Object = MibTable
cfprSysdebugMEpLogTable = _CfprSysdebugMEpLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25)
)
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogTable.setStatus("current")
_CfprSysdebugMEpLogEntry_Object = MibTableRow
cfprSysdebugMEpLogEntry = _CfprSysdebugMEpLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1)
)
cfprSysdebugMEpLogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugMEpLogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogEntry.setStatus("current")
_CfprSysdebugMEpLogInstanceId_Type = CfprManagedObjectId
_CfprSysdebugMEpLogInstanceId_Object = MibTableColumn
cfprSysdebugMEpLogInstanceId = _CfprSysdebugMEpLogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1, 1),
    _CfprSysdebugMEpLogInstanceId_Type()
)
cfprSysdebugMEpLogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogInstanceId.setStatus("current")
_CfprSysdebugMEpLogDn_Type = CfprManagedObjectDn
_CfprSysdebugMEpLogDn_Object = MibTableColumn
cfprSysdebugMEpLogDn = _CfprSysdebugMEpLogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1, 2),
    _CfprSysdebugMEpLogDn_Type()
)
cfprSysdebugMEpLogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogDn.setStatus("current")
_CfprSysdebugMEpLogRn_Type = SnmpAdminString
_CfprSysdebugMEpLogRn_Object = MibTableColumn
cfprSysdebugMEpLogRn = _CfprSysdebugMEpLogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1, 3),
    _CfprSysdebugMEpLogRn_Type()
)
cfprSysdebugMEpLogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogRn.setStatus("current")
_CfprSysdebugMEpLogAdminState_Type = CfprSysdebugEpLogAdminState
_CfprSysdebugMEpLogAdminState_Object = MibTableColumn
cfprSysdebugMEpLogAdminState = _CfprSysdebugMEpLogAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1, 4),
    _CfprSysdebugMEpLogAdminState_Type()
)
cfprSysdebugMEpLogAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogAdminState.setStatus("current")
_CfprSysdebugMEpLogCapacity_Type = CfprSysdebugEpLogCapacity
_CfprSysdebugMEpLogCapacity_Object = MibTableColumn
cfprSysdebugMEpLogCapacity = _CfprSysdebugMEpLogCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1, 5),
    _CfprSysdebugMEpLogCapacity_Type()
)
cfprSysdebugMEpLogCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogCapacity.setStatus("current")
_CfprSysdebugMEpLogId_Type = Gauge32
_CfprSysdebugMEpLogId_Object = MibTableColumn
cfprSysdebugMEpLogId = _CfprSysdebugMEpLogId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1, 6),
    _CfprSysdebugMEpLogId_Type()
)
cfprSysdebugMEpLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogId.setStatus("current")
_CfprSysdebugMEpLogLastUpdate_Type = DateAndTime
_CfprSysdebugMEpLogLastUpdate_Object = MibTableColumn
cfprSysdebugMEpLogLastUpdate = _CfprSysdebugMEpLogLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1, 7),
    _CfprSysdebugMEpLogLastUpdate_Type()
)
cfprSysdebugMEpLogLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogLastUpdate.setStatus("current")
_CfprSysdebugMEpLogOperState_Type = CfprSysdebugMEpLogOperState
_CfprSysdebugMEpLogOperState_Object = MibTableColumn
cfprSysdebugMEpLogOperState = _CfprSysdebugMEpLogOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1, 8),
    _CfprSysdebugMEpLogOperState_Type()
)
cfprSysdebugMEpLogOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogOperState.setStatus("current")
_CfprSysdebugMEpLogType_Type = CfprSysdebugEpLogType
_CfprSysdebugMEpLogType_Object = MibTableColumn
cfprSysdebugMEpLogType = _CfprSysdebugMEpLogType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 25, 1, 9),
    _CfprSysdebugMEpLogType_Type()
)
cfprSysdebugMEpLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogType.setStatus("current")
_CfprSysdebugMEpLogPolicyTable_Object = MibTable
cfprSysdebugMEpLogPolicyTable = _CfprSysdebugMEpLogPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26)
)
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyTable.setStatus("current")
_CfprSysdebugMEpLogPolicyEntry_Object = MibTableRow
cfprSysdebugMEpLogPolicyEntry = _CfprSysdebugMEpLogPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1)
)
cfprSysdebugMEpLogPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugMEpLogPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyEntry.setStatus("current")
_CfprSysdebugMEpLogPolicyInstanceId_Type = CfprManagedObjectId
_CfprSysdebugMEpLogPolicyInstanceId_Object = MibTableColumn
cfprSysdebugMEpLogPolicyInstanceId = _CfprSysdebugMEpLogPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1, 1),
    _CfprSysdebugMEpLogPolicyInstanceId_Type()
)
cfprSysdebugMEpLogPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyInstanceId.setStatus("current")
_CfprSysdebugMEpLogPolicyDn_Type = CfprManagedObjectDn
_CfprSysdebugMEpLogPolicyDn_Object = MibTableColumn
cfprSysdebugMEpLogPolicyDn = _CfprSysdebugMEpLogPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1, 2),
    _CfprSysdebugMEpLogPolicyDn_Type()
)
cfprSysdebugMEpLogPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyDn.setStatus("current")
_CfprSysdebugMEpLogPolicyRn_Type = SnmpAdminString
_CfprSysdebugMEpLogPolicyRn_Object = MibTableColumn
cfprSysdebugMEpLogPolicyRn = _CfprSysdebugMEpLogPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1, 3),
    _CfprSysdebugMEpLogPolicyRn_Type()
)
cfprSysdebugMEpLogPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyRn.setStatus("current")
_CfprSysdebugMEpLogPolicyDescr_Type = SnmpAdminString
_CfprSysdebugMEpLogPolicyDescr_Object = MibTableColumn
cfprSysdebugMEpLogPolicyDescr = _CfprSysdebugMEpLogPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1, 4),
    _CfprSysdebugMEpLogPolicyDescr_Type()
)
cfprSysdebugMEpLogPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyDescr.setStatus("current")
_CfprSysdebugMEpLogPolicyIntId_Type = SnmpAdminString
_CfprSysdebugMEpLogPolicyIntId_Object = MibTableColumn
cfprSysdebugMEpLogPolicyIntId = _CfprSysdebugMEpLogPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1, 5),
    _CfprSysdebugMEpLogPolicyIntId_Type()
)
cfprSysdebugMEpLogPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyIntId.setStatus("current")
_CfprSysdebugMEpLogPolicyName_Type = SnmpAdminString
_CfprSysdebugMEpLogPolicyName_Object = MibTableColumn
cfprSysdebugMEpLogPolicyName = _CfprSysdebugMEpLogPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1, 6),
    _CfprSysdebugMEpLogPolicyName_Type()
)
cfprSysdebugMEpLogPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyName.setStatus("current")
_CfprSysdebugMEpLogPolicyPolicyLevel_Type = Gauge32
_CfprSysdebugMEpLogPolicyPolicyLevel_Object = MibTableColumn
cfprSysdebugMEpLogPolicyPolicyLevel = _CfprSysdebugMEpLogPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1, 7),
    _CfprSysdebugMEpLogPolicyPolicyLevel_Type()
)
cfprSysdebugMEpLogPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyPolicyLevel.setStatus("current")
_CfprSysdebugMEpLogPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprSysdebugMEpLogPolicyPolicyOwner_Object = MibTableColumn
cfprSysdebugMEpLogPolicyPolicyOwner = _CfprSysdebugMEpLogPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1, 8),
    _CfprSysdebugMEpLogPolicyPolicyOwner_Type()
)
cfprSysdebugMEpLogPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyPolicyOwner.setStatus("current")
_CfprSysdebugMEpLogPolicyType_Type = CfprSysdebugEpLogType
_CfprSysdebugMEpLogPolicyType_Object = MibTableColumn
cfprSysdebugMEpLogPolicyType = _CfprSysdebugMEpLogPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 26, 1, 9),
    _CfprSysdebugMEpLogPolicyType_Type()
)
cfprSysdebugMEpLogPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugMEpLogPolicyType.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetTable_Object = MibTable
cfprSysdebugManualCoreFileExportTargetTable = _CfprSysdebugManualCoreFileExportTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27)
)
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetTable.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetEntry_Object = MibTableRow
cfprSysdebugManualCoreFileExportTargetEntry = _CfprSysdebugManualCoreFileExportTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1)
)
cfprSysdebugManualCoreFileExportTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugManualCoreFileExportTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetEntry.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetInstanceId_Type = CfprManagedObjectId
_CfprSysdebugManualCoreFileExportTargetInstanceId_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetInstanceId = _CfprSysdebugManualCoreFileExportTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 1),
    _CfprSysdebugManualCoreFileExportTargetInstanceId_Type()
)
cfprSysdebugManualCoreFileExportTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetInstanceId.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetDn_Type = CfprManagedObjectDn
_CfprSysdebugManualCoreFileExportTargetDn_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetDn = _CfprSysdebugManualCoreFileExportTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 2),
    _CfprSysdebugManualCoreFileExportTargetDn_Type()
)
cfprSysdebugManualCoreFileExportTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetDn.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetRn_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetRn_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetRn = _CfprSysdebugManualCoreFileExportTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 3),
    _CfprSysdebugManualCoreFileExportTargetRn_Type()
)
cfprSysdebugManualCoreFileExportTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetRn.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetAdminState_Type = CfprSysdebugManualCoreFileExportTargetAdminState
_CfprSysdebugManualCoreFileExportTargetAdminState_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetAdminState = _CfprSysdebugManualCoreFileExportTargetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 4),
    _CfprSysdebugManualCoreFileExportTargetAdminState_Type()
)
cfprSysdebugManualCoreFileExportTargetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetAdminState.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetDescr_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetDescr_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetDescr = _CfprSysdebugManualCoreFileExportTargetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 5),
    _CfprSysdebugManualCoreFileExportTargetDescr_Type()
)
cfprSysdebugManualCoreFileExportTargetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetDescr.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetExportFailureReason_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetExportFailureReason_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetExportFailureReason = _CfprSysdebugManualCoreFileExportTargetExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 6),
    _CfprSysdebugManualCoreFileExportTargetExportFailureReason_Type()
)
cfprSysdebugManualCoreFileExportTargetExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetExportFailureReason.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetExportStatus_Type = CfprSysdebugCoreExportStatus
_CfprSysdebugManualCoreFileExportTargetExportStatus_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetExportStatus = _CfprSysdebugManualCoreFileExportTargetExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 7),
    _CfprSysdebugManualCoreFileExportTargetExportStatus_Type()
)
cfprSysdebugManualCoreFileExportTargetExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetExportStatus.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmDescr_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmDescr_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmDescr = _CfprSysdebugManualCoreFileExportTargetFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 8),
    _CfprSysdebugManualCoreFileExportTargetFsmDescr_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmDescr.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmPrev_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmPrev_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmPrev = _CfprSysdebugManualCoreFileExportTargetFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 9),
    _CfprSysdebugManualCoreFileExportTargetFsmPrev_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmPrev.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmProgr_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetFsmProgr_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmProgr = _CfprSysdebugManualCoreFileExportTargetFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 10),
    _CfprSysdebugManualCoreFileExportTargetFsmProgr_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmProgr.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrCode = _CfprSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 11),
    _CfprSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrCode.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr = _CfprSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 12),
    _CfprSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmRmtInvRslt = _CfprSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 13),
    _CfprSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmRmtInvRslt.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageDescr_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmStageDescr_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageDescr = _CfprSysdebugManualCoreFileExportTargetFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 14),
    _CfprSysdebugManualCoreFileExportTargetFsmStageDescr_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageDescr.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStamp_Type = DateAndTime
_CfprSysdebugManualCoreFileExportTargetFsmStamp_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStamp = _CfprSysdebugManualCoreFileExportTargetFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 15),
    _CfprSysdebugManualCoreFileExportTargetFsmStamp_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStamp.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStatus_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmStatus_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStatus = _CfprSysdebugManualCoreFileExportTargetFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 16),
    _CfprSysdebugManualCoreFileExportTargetFsmStatus_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStatus.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTry_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetFsmTry_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmTry = _CfprSysdebugManualCoreFileExportTargetFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 17),
    _CfprSysdebugManualCoreFileExportTargetFsmTry_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTry.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetHostname_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetHostname_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetHostname = _CfprSysdebugManualCoreFileExportTargetHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 18),
    _CfprSysdebugManualCoreFileExportTargetHostname_Type()
)
cfprSysdebugManualCoreFileExportTargetHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetHostname.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetIntId_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetIntId_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetIntId = _CfprSysdebugManualCoreFileExportTargetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 19),
    _CfprSysdebugManualCoreFileExportTargetIntId_Type()
)
cfprSysdebugManualCoreFileExportTargetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetIntId.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetName_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetName_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetName = _CfprSysdebugManualCoreFileExportTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 20),
    _CfprSysdebugManualCoreFileExportTargetName_Type()
)
cfprSysdebugManualCoreFileExportTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetName.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetPath_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetPath_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetPath = _CfprSysdebugManualCoreFileExportTargetPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 21),
    _CfprSysdebugManualCoreFileExportTargetPath_Type()
)
cfprSysdebugManualCoreFileExportTargetPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetPath.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetPolicyLevel_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetPolicyLevel_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetPolicyLevel = _CfprSysdebugManualCoreFileExportTargetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 22),
    _CfprSysdebugManualCoreFileExportTargetPolicyLevel_Type()
)
cfprSysdebugManualCoreFileExportTargetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetPolicyLevel.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprSysdebugManualCoreFileExportTargetPolicyOwner_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetPolicyOwner = _CfprSysdebugManualCoreFileExportTargetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 23),
    _CfprSysdebugManualCoreFileExportTargetPolicyOwner_Type()
)
cfprSysdebugManualCoreFileExportTargetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetPolicyOwner.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetPort_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetPort_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetPort = _CfprSysdebugManualCoreFileExportTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 24),
    _CfprSysdebugManualCoreFileExportTargetPort_Type()
)
cfprSysdebugManualCoreFileExportTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetPort.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetPostAction_Type = CfprSysfileExporterPostAction
_CfprSysdebugManualCoreFileExportTargetPostAction_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetPostAction = _CfprSysdebugManualCoreFileExportTargetPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 25),
    _CfprSysdebugManualCoreFileExportTargetPostAction_Type()
)
cfprSysdebugManualCoreFileExportTargetPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetPostAction.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetProto_Type = CfprSysdebugManualCoreFileExportTargetProto
_CfprSysdebugManualCoreFileExportTargetProto_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetProto = _CfprSysdebugManualCoreFileExportTargetProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 27, 1, 26),
    _CfprSysdebugManualCoreFileExportTargetProto_Type()
)
cfprSysdebugManualCoreFileExportTargetProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetProto.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTable_Object = MibTable
cfprSysdebugManualCoreFileExportTargetFsmTable = _CfprSysdebugManualCoreFileExportTargetFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28)
)
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTable.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmEntry_Object = MibTableRow
cfprSysdebugManualCoreFileExportTargetFsmEntry = _CfprSysdebugManualCoreFileExportTargetFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1)
)
cfprSysdebugManualCoreFileExportTargetFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugManualCoreFileExportTargetFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmEntry.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmInstanceId_Type = CfprManagedObjectId
_CfprSysdebugManualCoreFileExportTargetFsmInstanceId_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmInstanceId = _CfprSysdebugManualCoreFileExportTargetFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 1),
    _CfprSysdebugManualCoreFileExportTargetFsmInstanceId_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmInstanceId.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmDn_Type = CfprManagedObjectDn
_CfprSysdebugManualCoreFileExportTargetFsmDn_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmDn = _CfprSysdebugManualCoreFileExportTargetFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 2),
    _CfprSysdebugManualCoreFileExportTargetFsmDn_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmDn.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmRn_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmRn_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmRn = _CfprSysdebugManualCoreFileExportTargetFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 3),
    _CfprSysdebugManualCoreFileExportTargetFsmRn_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmRn.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmCompletionTime_Type = DateAndTime
_CfprSysdebugManualCoreFileExportTargetFsmCompletionTime_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmCompletionTime = _CfprSysdebugManualCoreFileExportTargetFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 4),
    _CfprSysdebugManualCoreFileExportTargetFsmCompletionTime_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmCompletionTime.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmCurrentFsm_Type = CfprSysdebugManualCoreFileExportTargetFsmCurrentFsm
_CfprSysdebugManualCoreFileExportTargetFsmCurrentFsm_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmCurrentFsm = _CfprSysdebugManualCoreFileExportTargetFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 5),
    _CfprSysdebugManualCoreFileExportTargetFsmCurrentFsm_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmCurrentFsm.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmDescrData_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmDescrData_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmDescrData = _CfprSysdebugManualCoreFileExportTargetFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 6),
    _CfprSysdebugManualCoreFileExportTargetFsmDescrData_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmDescrData.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugManualCoreFileExportTargetFsmFsmStatus_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmFsmStatus = _CfprSysdebugManualCoreFileExportTargetFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 7),
    _CfprSysdebugManualCoreFileExportTargetFsmFsmStatus_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmFsmStatus.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmProgress_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetFsmProgress_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmProgress = _CfprSysdebugManualCoreFileExportTargetFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 8),
    _CfprSysdebugManualCoreFileExportTargetFsmProgress_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmProgress.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmRmtErrCode_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetFsmRmtErrCode_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmRmtErrCode = _CfprSysdebugManualCoreFileExportTargetFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 9),
    _CfprSysdebugManualCoreFileExportTargetFsmRmtErrCode_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmRmtErrCode.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmRmtErrDescr = _CfprSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 10),
    _CfprSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmRmtErrDescr.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugManualCoreFileExportTargetFsmRmtRslt_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmRmtRslt = _CfprSysdebugManualCoreFileExportTargetFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 28, 1, 11),
    _CfprSysdebugManualCoreFileExportTargetFsmRmtRslt_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmRmtRslt.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageTable_Object = MibTable
cfprSysdebugManualCoreFileExportTargetFsmStageTable = _CfprSysdebugManualCoreFileExportTargetFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29)
)
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageTable.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageEntry_Object = MibTableRow
cfprSysdebugManualCoreFileExportTargetFsmStageEntry = _CfprSysdebugManualCoreFileExportTargetFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1)
)
cfprSysdebugManualCoreFileExportTargetFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugManualCoreFileExportTargetFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageEntry.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSysdebugManualCoreFileExportTargetFsmStageInstanceId_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageInstanceId = _CfprSysdebugManualCoreFileExportTargetFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1, 1),
    _CfprSysdebugManualCoreFileExportTargetFsmStageInstanceId_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageInstanceId.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageDn_Type = CfprManagedObjectDn
_CfprSysdebugManualCoreFileExportTargetFsmStageDn_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageDn = _CfprSysdebugManualCoreFileExportTargetFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1, 2),
    _CfprSysdebugManualCoreFileExportTargetFsmStageDn_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageDn.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageRn_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmStageRn_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageRn = _CfprSysdebugManualCoreFileExportTargetFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1, 3),
    _CfprSysdebugManualCoreFileExportTargetFsmStageRn_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageRn.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageDescrData_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmStageDescrData_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageDescrData = _CfprSysdebugManualCoreFileExportTargetFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1, 4),
    _CfprSysdebugManualCoreFileExportTargetFsmStageDescrData_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageDescrData.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Type = DateAndTime
_CfprSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime = _CfprSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1, 5),
    _CfprSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageName_Type = CfprSysdebugManualCoreFileExportTargetFsmStageName
_CfprSysdebugManualCoreFileExportTargetFsmStageName_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageName = _CfprSysdebugManualCoreFileExportTargetFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1, 6),
    _CfprSysdebugManualCoreFileExportTargetFsmStageName_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageName.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageOrder_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetFsmStageOrder_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageOrder = _CfprSysdebugManualCoreFileExportTargetFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1, 7),
    _CfprSysdebugManualCoreFileExportTargetFsmStageOrder_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageOrder.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageRetry_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetFsmStageRetry_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageRetry = _CfprSysdebugManualCoreFileExportTargetFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1, 8),
    _CfprSysdebugManualCoreFileExportTargetFsmStageRetry_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageRetry.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugManualCoreFileExportTargetFsmStageStageStatus_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmStageStageStatus = _CfprSysdebugManualCoreFileExportTargetFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 29, 1, 9),
    _CfprSysdebugManualCoreFileExportTargetFsmStageStageStatus_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmStageStageStatus.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTaskTable_Object = MibTable
cfprSysdebugManualCoreFileExportTargetFsmTaskTable = _CfprSysdebugManualCoreFileExportTargetFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 30)
)
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTaskTable.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTaskEntry_Object = MibTableRow
cfprSysdebugManualCoreFileExportTargetFsmTaskEntry = _CfprSysdebugManualCoreFileExportTargetFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 30, 1)
)
cfprSysdebugManualCoreFileExportTargetFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTaskEntry.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId = _CfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 30, 1, 1),
    _CfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTaskDn_Type = CfprManagedObjectDn
_CfprSysdebugManualCoreFileExportTargetFsmTaskDn_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmTaskDn = _CfprSysdebugManualCoreFileExportTargetFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 30, 1, 2),
    _CfprSysdebugManualCoreFileExportTargetFsmTaskDn_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTaskDn.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTaskRn_Type = SnmpAdminString
_CfprSysdebugManualCoreFileExportTargetFsmTaskRn_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmTaskRn = _CfprSysdebugManualCoreFileExportTargetFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 30, 1, 3),
    _CfprSysdebugManualCoreFileExportTargetFsmTaskRn_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTaskRn.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSysdebugManualCoreFileExportTargetFsmTaskCompletion_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmTaskCompletion = _CfprSysdebugManualCoreFileExportTargetFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 30, 1, 4),
    _CfprSysdebugManualCoreFileExportTargetFsmTaskCompletion_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTaskCompletion.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTaskFlags_Type = CfprFsmFlags
_CfprSysdebugManualCoreFileExportTargetFsmTaskFlags_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmTaskFlags = _CfprSysdebugManualCoreFileExportTargetFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 30, 1, 5),
    _CfprSysdebugManualCoreFileExportTargetFsmTaskFlags_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTaskFlags.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTaskItem_Type = CfprSysdebugManualCoreFileExportTargetFsmTaskItem
_CfprSysdebugManualCoreFileExportTargetFsmTaskItem_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmTaskItem = _CfprSysdebugManualCoreFileExportTargetFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 30, 1, 6),
    _CfprSysdebugManualCoreFileExportTargetFsmTaskItem_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTaskItem.setStatus("current")
_CfprSysdebugManualCoreFileExportTargetFsmTaskSeqId_Type = Gauge32
_CfprSysdebugManualCoreFileExportTargetFsmTaskSeqId_Object = MibTableColumn
cfprSysdebugManualCoreFileExportTargetFsmTaskSeqId = _CfprSysdebugManualCoreFileExportTargetFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 30, 1, 7),
    _CfprSysdebugManualCoreFileExportTargetFsmTaskSeqId_Type()
)
cfprSysdebugManualCoreFileExportTargetFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugManualCoreFileExportTargetFsmTaskSeqId.setStatus("current")
_CfprSysdebugTechSupFileRepositoryTable_Object = MibTable
cfprSysdebugTechSupFileRepositoryTable = _CfprSysdebugTechSupFileRepositoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 31)
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupFileRepositoryTable.setStatus("current")
_CfprSysdebugTechSupFileRepositoryEntry_Object = MibTableRow
cfprSysdebugTechSupFileRepositoryEntry = _CfprSysdebugTechSupFileRepositoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 31, 1)
)
cfprSysdebugTechSupFileRepositoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugTechSupFileRepositoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupFileRepositoryEntry.setStatus("current")
_CfprSysdebugTechSupFileRepositoryInstanceId_Type = CfprManagedObjectId
_CfprSysdebugTechSupFileRepositoryInstanceId_Object = MibTableColumn
cfprSysdebugTechSupFileRepositoryInstanceId = _CfprSysdebugTechSupFileRepositoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 31, 1, 1),
    _CfprSysdebugTechSupFileRepositoryInstanceId_Type()
)
cfprSysdebugTechSupFileRepositoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupFileRepositoryInstanceId.setStatus("current")
_CfprSysdebugTechSupFileRepositoryDn_Type = CfprManagedObjectDn
_CfprSysdebugTechSupFileRepositoryDn_Object = MibTableColumn
cfprSysdebugTechSupFileRepositoryDn = _CfprSysdebugTechSupFileRepositoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 31, 1, 2),
    _CfprSysdebugTechSupFileRepositoryDn_Type()
)
cfprSysdebugTechSupFileRepositoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupFileRepositoryDn.setStatus("current")
_CfprSysdebugTechSupFileRepositoryRn_Type = SnmpAdminString
_CfprSysdebugTechSupFileRepositoryRn_Object = MibTableColumn
cfprSysdebugTechSupFileRepositoryRn = _CfprSysdebugTechSupFileRepositoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 31, 1, 3),
    _CfprSysdebugTechSupFileRepositoryRn_Type()
)
cfprSysdebugTechSupFileRepositoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupFileRepositoryRn.setStatus("current")
_CfprSysdebugTechSupportTable_Object = MibTable
cfprSysdebugTechSupportTable = _CfprSysdebugTechSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32)
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportTable.setStatus("current")
_CfprSysdebugTechSupportEntry_Object = MibTableRow
cfprSysdebugTechSupportEntry = _CfprSysdebugTechSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1)
)
cfprSysdebugTechSupportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugTechSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportEntry.setStatus("current")
_CfprSysdebugTechSupportInstanceId_Type = CfprManagedObjectId
_CfprSysdebugTechSupportInstanceId_Object = MibTableColumn
cfprSysdebugTechSupportInstanceId = _CfprSysdebugTechSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 1),
    _CfprSysdebugTechSupportInstanceId_Type()
)
cfprSysdebugTechSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportInstanceId.setStatus("current")
_CfprSysdebugTechSupportDn_Type = CfprManagedObjectDn
_CfprSysdebugTechSupportDn_Object = MibTableColumn
cfprSysdebugTechSupportDn = _CfprSysdebugTechSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 2),
    _CfprSysdebugTechSupportDn_Type()
)
cfprSysdebugTechSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportDn.setStatus("current")
_CfprSysdebugTechSupportRn_Type = SnmpAdminString
_CfprSysdebugTechSupportRn_Object = MibTableColumn
cfprSysdebugTechSupportRn = _CfprSysdebugTechSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 3),
    _CfprSysdebugTechSupportRn_Type()
)
cfprSysdebugTechSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportRn.setStatus("current")
_CfprSysdebugTechSupportAdminState_Type = CfprSysdebugTechSupportAdminState
_CfprSysdebugTechSupportAdminState_Object = MibTableColumn
cfprSysdebugTechSupportAdminState = _CfprSysdebugTechSupportAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 4),
    _CfprSysdebugTechSupportAdminState_Type()
)
cfprSysdebugTechSupportAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportAdminState.setStatus("current")
_CfprSysdebugTechSupportCreationTS_Type = Unsigned64
_CfprSysdebugTechSupportCreationTS_Object = MibTableColumn
cfprSysdebugTechSupportCreationTS = _CfprSysdebugTechSupportCreationTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 5),
    _CfprSysdebugTechSupportCreationTS_Type()
)
cfprSysdebugTechSupportCreationTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCreationTS.setStatus("current")
_CfprSysdebugTechSupportDescr_Type = SnmpAdminString
_CfprSysdebugTechSupportDescr_Object = MibTableColumn
cfprSysdebugTechSupportDescr = _CfprSysdebugTechSupportDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 6),
    _CfprSysdebugTechSupportDescr_Type()
)
cfprSysdebugTechSupportDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportDescr.setStatus("current")
_CfprSysdebugTechSupportFsmDescr_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmDescr_Object = MibTableColumn
cfprSysdebugTechSupportFsmDescr = _CfprSysdebugTechSupportFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 7),
    _CfprSysdebugTechSupportFsmDescr_Type()
)
cfprSysdebugTechSupportFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmDescr.setStatus("current")
_CfprSysdebugTechSupportFsmPrev_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmPrev_Object = MibTableColumn
cfprSysdebugTechSupportFsmPrev = _CfprSysdebugTechSupportFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 8),
    _CfprSysdebugTechSupportFsmPrev_Type()
)
cfprSysdebugTechSupportFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmPrev.setStatus("current")
_CfprSysdebugTechSupportFsmProgr_Type = Gauge32
_CfprSysdebugTechSupportFsmProgr_Object = MibTableColumn
cfprSysdebugTechSupportFsmProgr = _CfprSysdebugTechSupportFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 9),
    _CfprSysdebugTechSupportFsmProgr_Type()
)
cfprSysdebugTechSupportFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmProgr.setStatus("current")
_CfprSysdebugTechSupportFsmRmtInvErrCode_Type = Gauge32
_CfprSysdebugTechSupportFsmRmtInvErrCode_Object = MibTableColumn
cfprSysdebugTechSupportFsmRmtInvErrCode = _CfprSysdebugTechSupportFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 10),
    _CfprSysdebugTechSupportFsmRmtInvErrCode_Type()
)
cfprSysdebugTechSupportFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmRmtInvErrCode.setStatus("current")
_CfprSysdebugTechSupportFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmRmtInvErrDescr_Object = MibTableColumn
cfprSysdebugTechSupportFsmRmtInvErrDescr = _CfprSysdebugTechSupportFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 11),
    _CfprSysdebugTechSupportFsmRmtInvErrDescr_Type()
)
cfprSysdebugTechSupportFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmRmtInvErrDescr.setStatus("current")
_CfprSysdebugTechSupportFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugTechSupportFsmRmtInvRslt_Object = MibTableColumn
cfprSysdebugTechSupportFsmRmtInvRslt = _CfprSysdebugTechSupportFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 12),
    _CfprSysdebugTechSupportFsmRmtInvRslt_Type()
)
cfprSysdebugTechSupportFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmRmtInvRslt.setStatus("current")
_CfprSysdebugTechSupportFsmStageDescr_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmStageDescr_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageDescr = _CfprSysdebugTechSupportFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 13),
    _CfprSysdebugTechSupportFsmStageDescr_Type()
)
cfprSysdebugTechSupportFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageDescr.setStatus("current")
_CfprSysdebugTechSupportFsmStamp_Type = DateAndTime
_CfprSysdebugTechSupportFsmStamp_Object = MibTableColumn
cfprSysdebugTechSupportFsmStamp = _CfprSysdebugTechSupportFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 14),
    _CfprSysdebugTechSupportFsmStamp_Type()
)
cfprSysdebugTechSupportFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStamp.setStatus("current")
_CfprSysdebugTechSupportFsmStatus_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmStatus_Object = MibTableColumn
cfprSysdebugTechSupportFsmStatus = _CfprSysdebugTechSupportFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 15),
    _CfprSysdebugTechSupportFsmStatus_Type()
)
cfprSysdebugTechSupportFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStatus.setStatus("current")
_CfprSysdebugTechSupportFsmTry_Type = Gauge32
_CfprSysdebugTechSupportFsmTry_Object = MibTableColumn
cfprSysdebugTechSupportFsmTry = _CfprSysdebugTechSupportFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 16),
    _CfprSysdebugTechSupportFsmTry_Type()
)
cfprSysdebugTechSupportFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTry.setStatus("current")
_CfprSysdebugTechSupportName_Type = SnmpAdminString
_CfprSysdebugTechSupportName_Object = MibTableColumn
cfprSysdebugTechSupportName = _CfprSysdebugTechSupportName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 17),
    _CfprSysdebugTechSupportName_Type()
)
cfprSysdebugTechSupportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportName.setStatus("current")
_CfprSysdebugTechSupportOperState_Type = CfprSysdebugTechSupportOperState
_CfprSysdebugTechSupportOperState_Object = MibTableColumn
cfprSysdebugTechSupportOperState = _CfprSysdebugTechSupportOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 18),
    _CfprSysdebugTechSupportOperState_Type()
)
cfprSysdebugTechSupportOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportOperState.setStatus("current")
_CfprSysdebugTechSupportSize_Type = Gauge32
_CfprSysdebugTechSupportSize_Object = MibTableColumn
cfprSysdebugTechSupportSize = _CfprSysdebugTechSupportSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 19),
    _CfprSysdebugTechSupportSize_Type()
)
cfprSysdebugTechSupportSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportSize.setStatus("current")
_CfprSysdebugTechSupportSwitchId_Type = CfprNetworkSwitchId
_CfprSysdebugTechSupportSwitchId_Object = MibTableColumn
cfprSysdebugTechSupportSwitchId = _CfprSysdebugTechSupportSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 20),
    _CfprSysdebugTechSupportSwitchId_Type()
)
cfprSysdebugTechSupportSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportSwitchId.setStatus("current")
_CfprSysdebugTechSupportTs_Type = DateAndTime
_CfprSysdebugTechSupportTs_Object = MibTableColumn
cfprSysdebugTechSupportTs = _CfprSysdebugTechSupportTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 21),
    _CfprSysdebugTechSupportTs_Type()
)
cfprSysdebugTechSupportTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportTs.setStatus("current")
_CfprSysdebugTechSupportUri_Type = SnmpAdminString
_CfprSysdebugTechSupportUri_Object = MibTableColumn
cfprSysdebugTechSupportUri = _CfprSysdebugTechSupportUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 32, 1, 22),
    _CfprSysdebugTechSupportUri_Type()
)
cfprSysdebugTechSupportUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportUri.setStatus("current")
_CfprSysdebugTechSupportCmdOptTable_Object = MibTable
cfprSysdebugTechSupportCmdOptTable = _CfprSysdebugTechSupportCmdOptTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33)
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptTable.setStatus("current")
_CfprSysdebugTechSupportCmdOptEntry_Object = MibTableRow
cfprSysdebugTechSupportCmdOptEntry = _CfprSysdebugTechSupportCmdOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1)
)
cfprSysdebugTechSupportCmdOptEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugTechSupportCmdOptInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptEntry.setStatus("current")
_CfprSysdebugTechSupportCmdOptInstanceId_Type = CfprManagedObjectId
_CfprSysdebugTechSupportCmdOptInstanceId_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptInstanceId = _CfprSysdebugTechSupportCmdOptInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 1),
    _CfprSysdebugTechSupportCmdOptInstanceId_Type()
)
cfprSysdebugTechSupportCmdOptInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptInstanceId.setStatus("current")
_CfprSysdebugTechSupportCmdOptDn_Type = CfprManagedObjectDn
_CfprSysdebugTechSupportCmdOptDn_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptDn = _CfprSysdebugTechSupportCmdOptDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 2),
    _CfprSysdebugTechSupportCmdOptDn_Type()
)
cfprSysdebugTechSupportCmdOptDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptDn.setStatus("current")
_CfprSysdebugTechSupportCmdOptRn_Type = SnmpAdminString
_CfprSysdebugTechSupportCmdOptRn_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptRn = _CfprSysdebugTechSupportCmdOptRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 3),
    _CfprSysdebugTechSupportCmdOptRn_Type()
)
cfprSysdebugTechSupportCmdOptRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptRn.setStatus("current")
_CfprSysdebugTechSupportCmdOptChassisCimcId_Type = Gauge32
_CfprSysdebugTechSupportCmdOptChassisCimcId_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptChassisCimcId = _CfprSysdebugTechSupportCmdOptChassisCimcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 4),
    _CfprSysdebugTechSupportCmdOptChassisCimcId_Type()
)
cfprSysdebugTechSupportCmdOptChassisCimcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptChassisCimcId.setStatus("current")
_CfprSysdebugTechSupportCmdOptChassisId_Type = Gauge32
_CfprSysdebugTechSupportCmdOptChassisId_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptChassisId = _CfprSysdebugTechSupportCmdOptChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 5),
    _CfprSysdebugTechSupportCmdOptChassisId_Type()
)
cfprSysdebugTechSupportCmdOptChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptChassisId.setStatus("current")
_CfprSysdebugTechSupportCmdOptChassisIomId_Type = Gauge32
_CfprSysdebugTechSupportCmdOptChassisIomId_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptChassisIomId = _CfprSysdebugTechSupportCmdOptChassisIomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 6),
    _CfprSysdebugTechSupportCmdOptChassisIomId_Type()
)
cfprSysdebugTechSupportCmdOptChassisIomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptChassisIomId.setStatus("current")
_CfprSysdebugTechSupportCmdOptCimcAdapterId_Type = Gauge32
_CfprSysdebugTechSupportCmdOptCimcAdapterId_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptCimcAdapterId = _CfprSysdebugTechSupportCmdOptCimcAdapterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 7),
    _CfprSysdebugTechSupportCmdOptCimcAdapterId_Type()
)
cfprSysdebugTechSupportCmdOptCimcAdapterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptCimcAdapterId.setStatus("current")
_CfprSysdebugTechSupportCmdOptFabExtId_Type = Gauge32
_CfprSysdebugTechSupportCmdOptFabExtId_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptFabExtId = _CfprSysdebugTechSupportCmdOptFabExtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 8),
    _CfprSysdebugTechSupportCmdOptFabExtId_Type()
)
cfprSysdebugTechSupportCmdOptFabExtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptFabExtId.setStatus("current")
_CfprSysdebugTechSupportCmdOptMajorOptType_Type = CfprSysdebugTSCmdOptMajorType
_CfprSysdebugTechSupportCmdOptMajorOptType_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptMajorOptType = _CfprSysdebugTechSupportCmdOptMajorOptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 9),
    _CfprSysdebugTechSupportCmdOptMajorOptType_Type()
)
cfprSysdebugTechSupportCmdOptMajorOptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptMajorOptType.setStatus("current")
_CfprSysdebugTechSupportCmdOptRackServerAdapterId_Type = Gauge32
_CfprSysdebugTechSupportCmdOptRackServerAdapterId_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptRackServerAdapterId = _CfprSysdebugTechSupportCmdOptRackServerAdapterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 10),
    _CfprSysdebugTechSupportCmdOptRackServerAdapterId_Type()
)
cfprSysdebugTechSupportCmdOptRackServerAdapterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptRackServerAdapterId.setStatus("current")
_CfprSysdebugTechSupportCmdOptRackServerId_Type = Gauge32
_CfprSysdebugTechSupportCmdOptRackServerId_Object = MibTableColumn
cfprSysdebugTechSupportCmdOptRackServerId = _CfprSysdebugTechSupportCmdOptRackServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 33, 1, 11),
    _CfprSysdebugTechSupportCmdOptRackServerId_Type()
)
cfprSysdebugTechSupportCmdOptRackServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportCmdOptRackServerId.setStatus("current")
_CfprSysdebugTechSupportFsmTable_Object = MibTable
cfprSysdebugTechSupportFsmTable = _CfprSysdebugTechSupportFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34)
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTable.setStatus("current")
_CfprSysdebugTechSupportFsmEntry_Object = MibTableRow
cfprSysdebugTechSupportFsmEntry = _CfprSysdebugTechSupportFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1)
)
cfprSysdebugTechSupportFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugTechSupportFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmEntry.setStatus("current")
_CfprSysdebugTechSupportFsmInstanceId_Type = CfprManagedObjectId
_CfprSysdebugTechSupportFsmInstanceId_Object = MibTableColumn
cfprSysdebugTechSupportFsmInstanceId = _CfprSysdebugTechSupportFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 1),
    _CfprSysdebugTechSupportFsmInstanceId_Type()
)
cfprSysdebugTechSupportFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmInstanceId.setStatus("current")
_CfprSysdebugTechSupportFsmDn_Type = CfprManagedObjectDn
_CfprSysdebugTechSupportFsmDn_Object = MibTableColumn
cfprSysdebugTechSupportFsmDn = _CfprSysdebugTechSupportFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 2),
    _CfprSysdebugTechSupportFsmDn_Type()
)
cfprSysdebugTechSupportFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmDn.setStatus("current")
_CfprSysdebugTechSupportFsmRn_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmRn_Object = MibTableColumn
cfprSysdebugTechSupportFsmRn = _CfprSysdebugTechSupportFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 3),
    _CfprSysdebugTechSupportFsmRn_Type()
)
cfprSysdebugTechSupportFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmRn.setStatus("current")
_CfprSysdebugTechSupportFsmCompletionTime_Type = DateAndTime
_CfprSysdebugTechSupportFsmCompletionTime_Object = MibTableColumn
cfprSysdebugTechSupportFsmCompletionTime = _CfprSysdebugTechSupportFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 4),
    _CfprSysdebugTechSupportFsmCompletionTime_Type()
)
cfprSysdebugTechSupportFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmCompletionTime.setStatus("current")
_CfprSysdebugTechSupportFsmCurrentFsm_Type = CfprSysdebugTechSupportFsmCurrentFsm
_CfprSysdebugTechSupportFsmCurrentFsm_Object = MibTableColumn
cfprSysdebugTechSupportFsmCurrentFsm = _CfprSysdebugTechSupportFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 5),
    _CfprSysdebugTechSupportFsmCurrentFsm_Type()
)
cfprSysdebugTechSupportFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmCurrentFsm.setStatus("current")
_CfprSysdebugTechSupportFsmDescrData_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmDescrData_Object = MibTableColumn
cfprSysdebugTechSupportFsmDescrData = _CfprSysdebugTechSupportFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 6),
    _CfprSysdebugTechSupportFsmDescrData_Type()
)
cfprSysdebugTechSupportFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmDescrData.setStatus("current")
_CfprSysdebugTechSupportFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugTechSupportFsmFsmStatus_Object = MibTableColumn
cfprSysdebugTechSupportFsmFsmStatus = _CfprSysdebugTechSupportFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 7),
    _CfprSysdebugTechSupportFsmFsmStatus_Type()
)
cfprSysdebugTechSupportFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmFsmStatus.setStatus("current")
_CfprSysdebugTechSupportFsmProgress_Type = Gauge32
_CfprSysdebugTechSupportFsmProgress_Object = MibTableColumn
cfprSysdebugTechSupportFsmProgress = _CfprSysdebugTechSupportFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 8),
    _CfprSysdebugTechSupportFsmProgress_Type()
)
cfprSysdebugTechSupportFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmProgress.setStatus("current")
_CfprSysdebugTechSupportFsmRmtErrCode_Type = Gauge32
_CfprSysdebugTechSupportFsmRmtErrCode_Object = MibTableColumn
cfprSysdebugTechSupportFsmRmtErrCode = _CfprSysdebugTechSupportFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 9),
    _CfprSysdebugTechSupportFsmRmtErrCode_Type()
)
cfprSysdebugTechSupportFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmRmtErrCode.setStatus("current")
_CfprSysdebugTechSupportFsmRmtErrDescr_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmRmtErrDescr_Object = MibTableColumn
cfprSysdebugTechSupportFsmRmtErrDescr = _CfprSysdebugTechSupportFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 10),
    _CfprSysdebugTechSupportFsmRmtErrDescr_Type()
)
cfprSysdebugTechSupportFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmRmtErrDescr.setStatus("current")
_CfprSysdebugTechSupportFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSysdebugTechSupportFsmRmtRslt_Object = MibTableColumn
cfprSysdebugTechSupportFsmRmtRslt = _CfprSysdebugTechSupportFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 34, 1, 11),
    _CfprSysdebugTechSupportFsmRmtRslt_Type()
)
cfprSysdebugTechSupportFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmRmtRslt.setStatus("current")
_CfprSysdebugTechSupportFsmStageTable_Object = MibTable
cfprSysdebugTechSupportFsmStageTable = _CfprSysdebugTechSupportFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35)
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageTable.setStatus("current")
_CfprSysdebugTechSupportFsmStageEntry_Object = MibTableRow
cfprSysdebugTechSupportFsmStageEntry = _CfprSysdebugTechSupportFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1)
)
cfprSysdebugTechSupportFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugTechSupportFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageEntry.setStatus("current")
_CfprSysdebugTechSupportFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSysdebugTechSupportFsmStageInstanceId_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageInstanceId = _CfprSysdebugTechSupportFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1, 1),
    _CfprSysdebugTechSupportFsmStageInstanceId_Type()
)
cfprSysdebugTechSupportFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageInstanceId.setStatus("current")
_CfprSysdebugTechSupportFsmStageDn_Type = CfprManagedObjectDn
_CfprSysdebugTechSupportFsmStageDn_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageDn = _CfprSysdebugTechSupportFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1, 2),
    _CfprSysdebugTechSupportFsmStageDn_Type()
)
cfprSysdebugTechSupportFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageDn.setStatus("current")
_CfprSysdebugTechSupportFsmStageRn_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmStageRn_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageRn = _CfprSysdebugTechSupportFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1, 3),
    _CfprSysdebugTechSupportFsmStageRn_Type()
)
cfprSysdebugTechSupportFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageRn.setStatus("current")
_CfprSysdebugTechSupportFsmStageDescrData_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmStageDescrData_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageDescrData = _CfprSysdebugTechSupportFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1, 4),
    _CfprSysdebugTechSupportFsmStageDescrData_Type()
)
cfprSysdebugTechSupportFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageDescrData.setStatus("current")
_CfprSysdebugTechSupportFsmStageLastUpdateTime_Type = DateAndTime
_CfprSysdebugTechSupportFsmStageLastUpdateTime_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageLastUpdateTime = _CfprSysdebugTechSupportFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1, 5),
    _CfprSysdebugTechSupportFsmStageLastUpdateTime_Type()
)
cfprSysdebugTechSupportFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageLastUpdateTime.setStatus("current")
_CfprSysdebugTechSupportFsmStageName_Type = CfprSysdebugTechSupportFsmStageName
_CfprSysdebugTechSupportFsmStageName_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageName = _CfprSysdebugTechSupportFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1, 6),
    _CfprSysdebugTechSupportFsmStageName_Type()
)
cfprSysdebugTechSupportFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageName.setStatus("current")
_CfprSysdebugTechSupportFsmStageOrder_Type = Gauge32
_CfprSysdebugTechSupportFsmStageOrder_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageOrder = _CfprSysdebugTechSupportFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1, 7),
    _CfprSysdebugTechSupportFsmStageOrder_Type()
)
cfprSysdebugTechSupportFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageOrder.setStatus("current")
_CfprSysdebugTechSupportFsmStageRetry_Type = Gauge32
_CfprSysdebugTechSupportFsmStageRetry_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageRetry = _CfprSysdebugTechSupportFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1, 8),
    _CfprSysdebugTechSupportFsmStageRetry_Type()
)
cfprSysdebugTechSupportFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageRetry.setStatus("current")
_CfprSysdebugTechSupportFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSysdebugTechSupportFsmStageStageStatus_Object = MibTableColumn
cfprSysdebugTechSupportFsmStageStageStatus = _CfprSysdebugTechSupportFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 35, 1, 9),
    _CfprSysdebugTechSupportFsmStageStageStatus_Type()
)
cfprSysdebugTechSupportFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmStageStageStatus.setStatus("current")
_CfprSysdebugTechSupportFsmTaskTable_Object = MibTable
cfprSysdebugTechSupportFsmTaskTable = _CfprSysdebugTechSupportFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 36)
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTaskTable.setStatus("current")
_CfprSysdebugTechSupportFsmTaskEntry_Object = MibTableRow
cfprSysdebugTechSupportFsmTaskEntry = _CfprSysdebugTechSupportFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 36, 1)
)
cfprSysdebugTechSupportFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugTechSupportFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTaskEntry.setStatus("current")
_CfprSysdebugTechSupportFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSysdebugTechSupportFsmTaskInstanceId_Object = MibTableColumn
cfprSysdebugTechSupportFsmTaskInstanceId = _CfprSysdebugTechSupportFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 36, 1, 1),
    _CfprSysdebugTechSupportFsmTaskInstanceId_Type()
)
cfprSysdebugTechSupportFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTaskInstanceId.setStatus("current")
_CfprSysdebugTechSupportFsmTaskDn_Type = CfprManagedObjectDn
_CfprSysdebugTechSupportFsmTaskDn_Object = MibTableColumn
cfprSysdebugTechSupportFsmTaskDn = _CfprSysdebugTechSupportFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 36, 1, 2),
    _CfprSysdebugTechSupportFsmTaskDn_Type()
)
cfprSysdebugTechSupportFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTaskDn.setStatus("current")
_CfprSysdebugTechSupportFsmTaskRn_Type = SnmpAdminString
_CfprSysdebugTechSupportFsmTaskRn_Object = MibTableColumn
cfprSysdebugTechSupportFsmTaskRn = _CfprSysdebugTechSupportFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 36, 1, 3),
    _CfprSysdebugTechSupportFsmTaskRn_Type()
)
cfprSysdebugTechSupportFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTaskRn.setStatus("current")
_CfprSysdebugTechSupportFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSysdebugTechSupportFsmTaskCompletion_Object = MibTableColumn
cfprSysdebugTechSupportFsmTaskCompletion = _CfprSysdebugTechSupportFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 36, 1, 4),
    _CfprSysdebugTechSupportFsmTaskCompletion_Type()
)
cfprSysdebugTechSupportFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTaskCompletion.setStatus("current")
_CfprSysdebugTechSupportFsmTaskFlags_Type = CfprFsmFlags
_CfprSysdebugTechSupportFsmTaskFlags_Object = MibTableColumn
cfprSysdebugTechSupportFsmTaskFlags = _CfprSysdebugTechSupportFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 36, 1, 5),
    _CfprSysdebugTechSupportFsmTaskFlags_Type()
)
cfprSysdebugTechSupportFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTaskFlags.setStatus("current")
_CfprSysdebugTechSupportFsmTaskItem_Type = CfprSysdebugTechSupportFsmTaskItem
_CfprSysdebugTechSupportFsmTaskItem_Object = MibTableColumn
cfprSysdebugTechSupportFsmTaskItem = _CfprSysdebugTechSupportFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 36, 1, 6),
    _CfprSysdebugTechSupportFsmTaskItem_Type()
)
cfprSysdebugTechSupportFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTaskItem.setStatus("current")
_CfprSysdebugTechSupportFsmTaskSeqId_Type = Gauge32
_CfprSysdebugTechSupportFsmTaskSeqId_Object = MibTableColumn
cfprSysdebugTechSupportFsmTaskSeqId = _CfprSysdebugTechSupportFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 36, 1, 7),
    _CfprSysdebugTechSupportFsmTaskSeqId_Type()
)
cfprSysdebugTechSupportFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugTechSupportFsmTaskSeqId.setStatus("current")
_CfprSysdebugAdaptorCoreStatsTable_Object = MibTable
cfprSysdebugAdaptorCoreStatsTable = _CfprSysdebugAdaptorCoreStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 37)
)
if mibBuilder.loadTexts:
    cfprSysdebugAdaptorCoreStatsTable.setStatus("current")
_CfprSysdebugAdaptorCoreStatsEntry_Object = MibTableRow
cfprSysdebugAdaptorCoreStatsEntry = _CfprSysdebugAdaptorCoreStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 37, 1)
)
cfprSysdebugAdaptorCoreStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSDEBUG-MIB", "cfprSysdebugAdaptorCoreStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysdebugAdaptorCoreStatsEntry.setStatus("current")
_CfprSysdebugAdaptorCoreStatsInstanceId_Type = CfprManagedObjectId
_CfprSysdebugAdaptorCoreStatsInstanceId_Object = MibTableColumn
cfprSysdebugAdaptorCoreStatsInstanceId = _CfprSysdebugAdaptorCoreStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 37, 1, 1),
    _CfprSysdebugAdaptorCoreStatsInstanceId_Type()
)
cfprSysdebugAdaptorCoreStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysdebugAdaptorCoreStatsInstanceId.setStatus("current")
_CfprSysdebugAdaptorCoreStatsDn_Type = CfprManagedObjectDn
_CfprSysdebugAdaptorCoreStatsDn_Object = MibTableColumn
cfprSysdebugAdaptorCoreStatsDn = _CfprSysdebugAdaptorCoreStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 37, 1, 2),
    _CfprSysdebugAdaptorCoreStatsDn_Type()
)
cfprSysdebugAdaptorCoreStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAdaptorCoreStatsDn.setStatus("current")
_CfprSysdebugAdaptorCoreStatsRn_Type = SnmpAdminString
_CfprSysdebugAdaptorCoreStatsRn_Object = MibTableColumn
cfprSysdebugAdaptorCoreStatsRn = _CfprSysdebugAdaptorCoreStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 37, 1, 3),
    _CfprSysdebugAdaptorCoreStatsRn_Type()
)
cfprSysdebugAdaptorCoreStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAdaptorCoreStatsRn.setStatus("current")
_CfprSysdebugAdaptorCoreStatsAdaptorId_Type = Gauge32
_CfprSysdebugAdaptorCoreStatsAdaptorId_Object = MibTableColumn
cfprSysdebugAdaptorCoreStatsAdaptorId = _CfprSysdebugAdaptorCoreStatsAdaptorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 37, 1, 4),
    _CfprSysdebugAdaptorCoreStatsAdaptorId_Type()
)
cfprSysdebugAdaptorCoreStatsAdaptorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAdaptorCoreStatsAdaptorId.setStatus("current")
_CfprSysdebugAdaptorCoreStatsExcessiveCore_Type = TruthValue
_CfprSysdebugAdaptorCoreStatsExcessiveCore_Object = MibTableColumn
cfprSysdebugAdaptorCoreStatsExcessiveCore = _CfprSysdebugAdaptorCoreStatsExcessiveCore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 37, 1, 5),
    _CfprSysdebugAdaptorCoreStatsExcessiveCore_Type()
)
cfprSysdebugAdaptorCoreStatsExcessiveCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAdaptorCoreStatsExcessiveCore.setStatus("current")
_CfprSysdebugAdaptorCoreStatsNumCore_Type = Gauge32
_CfprSysdebugAdaptorCoreStatsNumCore_Object = MibTableColumn
cfprSysdebugAdaptorCoreStatsNumCore = _CfprSysdebugAdaptorCoreStatsNumCore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 37, 1, 6),
    _CfprSysdebugAdaptorCoreStatsNumCore_Type()
)
cfprSysdebugAdaptorCoreStatsNumCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAdaptorCoreStatsNumCore.setStatus("current")
_CfprSysdebugAdaptorCoreStatsSlotId_Type = Gauge32
_CfprSysdebugAdaptorCoreStatsSlotId_Object = MibTableColumn
cfprSysdebugAdaptorCoreStatsSlotId = _CfprSysdebugAdaptorCoreStatsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 76, 37, 1, 7),
    _CfprSysdebugAdaptorCoreStatsSlotId_Type()
)
cfprSysdebugAdaptorCoreStatsSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysdebugAdaptorCoreStatsSlotId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-SYSDEBUG-MIB",
    **{"cfprSysdebugObjects": cfprSysdebugObjects,
       "cfprSysdebugAutoCoreFileExportTargetTable": cfprSysdebugAutoCoreFileExportTargetTable,
       "cfprSysdebugAutoCoreFileExportTargetEntry": cfprSysdebugAutoCoreFileExportTargetEntry,
       "cfprSysdebugAutoCoreFileExportTargetInstanceId": cfprSysdebugAutoCoreFileExportTargetInstanceId,
       "cfprSysdebugAutoCoreFileExportTargetDn": cfprSysdebugAutoCoreFileExportTargetDn,
       "cfprSysdebugAutoCoreFileExportTargetRn": cfprSysdebugAutoCoreFileExportTargetRn,
       "cfprSysdebugAutoCoreFileExportTargetAdminState": cfprSysdebugAutoCoreFileExportTargetAdminState,
       "cfprSysdebugAutoCoreFileExportTargetDescr": cfprSysdebugAutoCoreFileExportTargetDescr,
       "cfprSysdebugAutoCoreFileExportTargetExportFailureReason": cfprSysdebugAutoCoreFileExportTargetExportFailureReason,
       "cfprSysdebugAutoCoreFileExportTargetExportStatus": cfprSysdebugAutoCoreFileExportTargetExportStatus,
       "cfprSysdebugAutoCoreFileExportTargetFsmDescr": cfprSysdebugAutoCoreFileExportTargetFsmDescr,
       "cfprSysdebugAutoCoreFileExportTargetFsmPrev": cfprSysdebugAutoCoreFileExportTargetFsmPrev,
       "cfprSysdebugAutoCoreFileExportTargetFsmProgr": cfprSysdebugAutoCoreFileExportTargetFsmProgr,
       "cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode": cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode,
       "cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr": cfprSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr,
       "cfprSysdebugAutoCoreFileExportTargetFsmRmtInvRslt": cfprSysdebugAutoCoreFileExportTargetFsmRmtInvRslt,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageDescr": cfprSysdebugAutoCoreFileExportTargetFsmStageDescr,
       "cfprSysdebugAutoCoreFileExportTargetFsmStamp": cfprSysdebugAutoCoreFileExportTargetFsmStamp,
       "cfprSysdebugAutoCoreFileExportTargetFsmStatus": cfprSysdebugAutoCoreFileExportTargetFsmStatus,
       "cfprSysdebugAutoCoreFileExportTargetFsmTry": cfprSysdebugAutoCoreFileExportTargetFsmTry,
       "cfprSysdebugAutoCoreFileExportTargetHostname": cfprSysdebugAutoCoreFileExportTargetHostname,
       "cfprSysdebugAutoCoreFileExportTargetIntId": cfprSysdebugAutoCoreFileExportTargetIntId,
       "cfprSysdebugAutoCoreFileExportTargetName": cfprSysdebugAutoCoreFileExportTargetName,
       "cfprSysdebugAutoCoreFileExportTargetPath": cfprSysdebugAutoCoreFileExportTargetPath,
       "cfprSysdebugAutoCoreFileExportTargetPolicyLevel": cfprSysdebugAutoCoreFileExportTargetPolicyLevel,
       "cfprSysdebugAutoCoreFileExportTargetPolicyOwner": cfprSysdebugAutoCoreFileExportTargetPolicyOwner,
       "cfprSysdebugAutoCoreFileExportTargetPort": cfprSysdebugAutoCoreFileExportTargetPort,
       "cfprSysdebugAutoCoreFileExportTargetPostAction": cfprSysdebugAutoCoreFileExportTargetPostAction,
       "cfprSysdebugAutoCoreFileExportTargetProto": cfprSysdebugAutoCoreFileExportTargetProto,
       "cfprSysdebugAutoCoreFileExportTargetFsmTable": cfprSysdebugAutoCoreFileExportTargetFsmTable,
       "cfprSysdebugAutoCoreFileExportTargetFsmEntry": cfprSysdebugAutoCoreFileExportTargetFsmEntry,
       "cfprSysdebugAutoCoreFileExportTargetFsmInstanceId": cfprSysdebugAutoCoreFileExportTargetFsmInstanceId,
       "cfprSysdebugAutoCoreFileExportTargetFsmDn": cfprSysdebugAutoCoreFileExportTargetFsmDn,
       "cfprSysdebugAutoCoreFileExportTargetFsmRn": cfprSysdebugAutoCoreFileExportTargetFsmRn,
       "cfprSysdebugAutoCoreFileExportTargetFsmCompletionTime": cfprSysdebugAutoCoreFileExportTargetFsmCompletionTime,
       "cfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm": cfprSysdebugAutoCoreFileExportTargetFsmCurrentFsm,
       "cfprSysdebugAutoCoreFileExportTargetFsmDescrData": cfprSysdebugAutoCoreFileExportTargetFsmDescrData,
       "cfprSysdebugAutoCoreFileExportTargetFsmFsmStatus": cfprSysdebugAutoCoreFileExportTargetFsmFsmStatus,
       "cfprSysdebugAutoCoreFileExportTargetFsmProgress": cfprSysdebugAutoCoreFileExportTargetFsmProgress,
       "cfprSysdebugAutoCoreFileExportTargetFsmRmtErrCode": cfprSysdebugAutoCoreFileExportTargetFsmRmtErrCode,
       "cfprSysdebugAutoCoreFileExportTargetFsmRmtErrDescr": cfprSysdebugAutoCoreFileExportTargetFsmRmtErrDescr,
       "cfprSysdebugAutoCoreFileExportTargetFsmRmtRslt": cfprSysdebugAutoCoreFileExportTargetFsmRmtRslt,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageTable": cfprSysdebugAutoCoreFileExportTargetFsmStageTable,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageEntry": cfprSysdebugAutoCoreFileExportTargetFsmStageEntry,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId": cfprSysdebugAutoCoreFileExportTargetFsmStageInstanceId,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageDn": cfprSysdebugAutoCoreFileExportTargetFsmStageDn,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageRn": cfprSysdebugAutoCoreFileExportTargetFsmStageRn,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageDescrData": cfprSysdebugAutoCoreFileExportTargetFsmStageDescrData,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime": cfprSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageName": cfprSysdebugAutoCoreFileExportTargetFsmStageName,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageOrder": cfprSysdebugAutoCoreFileExportTargetFsmStageOrder,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageRetry": cfprSysdebugAutoCoreFileExportTargetFsmStageRetry,
       "cfprSysdebugAutoCoreFileExportTargetFsmStageStageStatus": cfprSysdebugAutoCoreFileExportTargetFsmStageStageStatus,
       "cfprSysdebugAutoCoreFileExportTargetFsmTaskTable": cfprSysdebugAutoCoreFileExportTargetFsmTaskTable,
       "cfprSysdebugAutoCoreFileExportTargetFsmTaskEntry": cfprSysdebugAutoCoreFileExportTargetFsmTaskEntry,
       "cfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId": cfprSysdebugAutoCoreFileExportTargetFsmTaskInstanceId,
       "cfprSysdebugAutoCoreFileExportTargetFsmTaskDn": cfprSysdebugAutoCoreFileExportTargetFsmTaskDn,
       "cfprSysdebugAutoCoreFileExportTargetFsmTaskRn": cfprSysdebugAutoCoreFileExportTargetFsmTaskRn,
       "cfprSysdebugAutoCoreFileExportTargetFsmTaskCompletion": cfprSysdebugAutoCoreFileExportTargetFsmTaskCompletion,
       "cfprSysdebugAutoCoreFileExportTargetFsmTaskFlags": cfprSysdebugAutoCoreFileExportTargetFsmTaskFlags,
       "cfprSysdebugAutoCoreFileExportTargetFsmTaskItem": cfprSysdebugAutoCoreFileExportTargetFsmTaskItem,
       "cfprSysdebugAutoCoreFileExportTargetFsmTaskSeqId": cfprSysdebugAutoCoreFileExportTargetFsmTaskSeqId,
       "cfprSysdebugBackupBehaviorTable": cfprSysdebugBackupBehaviorTable,
       "cfprSysdebugBackupBehaviorEntry": cfprSysdebugBackupBehaviorEntry,
       "cfprSysdebugBackupBehaviorInstanceId": cfprSysdebugBackupBehaviorInstanceId,
       "cfprSysdebugBackupBehaviorDn": cfprSysdebugBackupBehaviorDn,
       "cfprSysdebugBackupBehaviorRn": cfprSysdebugBackupBehaviorRn,
       "cfprSysdebugBackupBehaviorAction": cfprSysdebugBackupBehaviorAction,
       "cfprSysdebugBackupBehaviorClearOnBackup": cfprSysdebugBackupBehaviorClearOnBackup,
       "cfprSysdebugBackupBehaviorFormat": cfprSysdebugBackupBehaviorFormat,
       "cfprSysdebugBackupBehaviorHostname": cfprSysdebugBackupBehaviorHostname,
       "cfprSysdebugBackupBehaviorInterval": cfprSysdebugBackupBehaviorInterval,
       "cfprSysdebugBackupBehaviorProto": cfprSysdebugBackupBehaviorProto,
       "cfprSysdebugBackupBehaviorPwd": cfprSysdebugBackupBehaviorPwd,
       "cfprSysdebugBackupBehaviorRemotePath": cfprSysdebugBackupBehaviorRemotePath,
       "cfprSysdebugBackupBehaviorUser": cfprSysdebugBackupBehaviorUser,
       "cfprSysdebugCoreTable": cfprSysdebugCoreTable,
       "cfprSysdebugCoreEntry": cfprSysdebugCoreEntry,
       "cfprSysdebugCoreInstanceId": cfprSysdebugCoreInstanceId,
       "cfprSysdebugCoreDn": cfprSysdebugCoreDn,
       "cfprSysdebugCoreRn": cfprSysdebugCoreRn,
       "cfprSysdebugCoreAdminState": cfprSysdebugCoreAdminState,
       "cfprSysdebugCoreDescr": cfprSysdebugCoreDescr,
       "cfprSysdebugCoreFsmDescr": cfprSysdebugCoreFsmDescr,
       "cfprSysdebugCoreFsmPrev": cfprSysdebugCoreFsmPrev,
       "cfprSysdebugCoreFsmProgr": cfprSysdebugCoreFsmProgr,
       "cfprSysdebugCoreFsmRmtInvErrCode": cfprSysdebugCoreFsmRmtInvErrCode,
       "cfprSysdebugCoreFsmRmtInvErrDescr": cfprSysdebugCoreFsmRmtInvErrDescr,
       "cfprSysdebugCoreFsmRmtInvRslt": cfprSysdebugCoreFsmRmtInvRslt,
       "cfprSysdebugCoreFsmStageDescr": cfprSysdebugCoreFsmStageDescr,
       "cfprSysdebugCoreFsmStamp": cfprSysdebugCoreFsmStamp,
       "cfprSysdebugCoreFsmStatus": cfprSysdebugCoreFsmStatus,
       "cfprSysdebugCoreFsmTry": cfprSysdebugCoreFsmTry,
       "cfprSysdebugCoreName": cfprSysdebugCoreName,
       "cfprSysdebugCoreOperState": cfprSysdebugCoreOperState,
       "cfprSysdebugCoreSize": cfprSysdebugCoreSize,
       "cfprSysdebugCoreSwitchId": cfprSysdebugCoreSwitchId,
       "cfprSysdebugCoreTs": cfprSysdebugCoreTs,
       "cfprSysdebugCoreUri": cfprSysdebugCoreUri,
       "cfprSysdebugCoreFileRepositoryTable": cfprSysdebugCoreFileRepositoryTable,
       "cfprSysdebugCoreFileRepositoryEntry": cfprSysdebugCoreFileRepositoryEntry,
       "cfprSysdebugCoreFileRepositoryInstanceId": cfprSysdebugCoreFileRepositoryInstanceId,
       "cfprSysdebugCoreFileRepositoryDn": cfprSysdebugCoreFileRepositoryDn,
       "cfprSysdebugCoreFileRepositoryRn": cfprSysdebugCoreFileRepositoryRn,
       "cfprSysdebugCoreFsmTable": cfprSysdebugCoreFsmTable,
       "cfprSysdebugCoreFsmEntry": cfprSysdebugCoreFsmEntry,
       "cfprSysdebugCoreFsmInstanceId": cfprSysdebugCoreFsmInstanceId,
       "cfprSysdebugCoreFsmDn": cfprSysdebugCoreFsmDn,
       "cfprSysdebugCoreFsmRn": cfprSysdebugCoreFsmRn,
       "cfprSysdebugCoreFsmCompletionTime": cfprSysdebugCoreFsmCompletionTime,
       "cfprSysdebugCoreFsmCurrentFsm": cfprSysdebugCoreFsmCurrentFsm,
       "cfprSysdebugCoreFsmDescrData": cfprSysdebugCoreFsmDescrData,
       "cfprSysdebugCoreFsmFsmStatus": cfprSysdebugCoreFsmFsmStatus,
       "cfprSysdebugCoreFsmProgress": cfprSysdebugCoreFsmProgress,
       "cfprSysdebugCoreFsmRmtErrCode": cfprSysdebugCoreFsmRmtErrCode,
       "cfprSysdebugCoreFsmRmtErrDescr": cfprSysdebugCoreFsmRmtErrDescr,
       "cfprSysdebugCoreFsmRmtRslt": cfprSysdebugCoreFsmRmtRslt,
       "cfprSysdebugCoreFsmStageTable": cfprSysdebugCoreFsmStageTable,
       "cfprSysdebugCoreFsmStageEntry": cfprSysdebugCoreFsmStageEntry,
       "cfprSysdebugCoreFsmStageInstanceId": cfprSysdebugCoreFsmStageInstanceId,
       "cfprSysdebugCoreFsmStageDn": cfprSysdebugCoreFsmStageDn,
       "cfprSysdebugCoreFsmStageRn": cfprSysdebugCoreFsmStageRn,
       "cfprSysdebugCoreFsmStageDescrData": cfprSysdebugCoreFsmStageDescrData,
       "cfprSysdebugCoreFsmStageLastUpdateTime": cfprSysdebugCoreFsmStageLastUpdateTime,
       "cfprSysdebugCoreFsmStageName": cfprSysdebugCoreFsmStageName,
       "cfprSysdebugCoreFsmStageOrder": cfprSysdebugCoreFsmStageOrder,
       "cfprSysdebugCoreFsmStageRetry": cfprSysdebugCoreFsmStageRetry,
       "cfprSysdebugCoreFsmStageStageStatus": cfprSysdebugCoreFsmStageStageStatus,
       "cfprSysdebugCoreFsmTaskTable": cfprSysdebugCoreFsmTaskTable,
       "cfprSysdebugCoreFsmTaskEntry": cfprSysdebugCoreFsmTaskEntry,
       "cfprSysdebugCoreFsmTaskInstanceId": cfprSysdebugCoreFsmTaskInstanceId,
       "cfprSysdebugCoreFsmTaskDn": cfprSysdebugCoreFsmTaskDn,
       "cfprSysdebugCoreFsmTaskRn": cfprSysdebugCoreFsmTaskRn,
       "cfprSysdebugCoreFsmTaskCompletion": cfprSysdebugCoreFsmTaskCompletion,
       "cfprSysdebugCoreFsmTaskFlags": cfprSysdebugCoreFsmTaskFlags,
       "cfprSysdebugCoreFsmTaskItem": cfprSysdebugCoreFsmTaskItem,
       "cfprSysdebugCoreFsmTaskSeqId": cfprSysdebugCoreFsmTaskSeqId,
       "cfprSysdebugEpTable": cfprSysdebugEpTable,
       "cfprSysdebugEpEntry": cfprSysdebugEpEntry,
       "cfprSysdebugEpInstanceId": cfprSysdebugEpInstanceId,
       "cfprSysdebugEpDn": cfprSysdebugEpDn,
       "cfprSysdebugEpRn": cfprSysdebugEpRn,
       "cfprSysdebugLogControlDestinationFileTable": cfprSysdebugLogControlDestinationFileTable,
       "cfprSysdebugLogControlDestinationFileEntry": cfprSysdebugLogControlDestinationFileEntry,
       "cfprSysdebugLogControlDestinationFileInstanceId": cfprSysdebugLogControlDestinationFileInstanceId,
       "cfprSysdebugLogControlDestinationFileDn": cfprSysdebugLogControlDestinationFileDn,
       "cfprSysdebugLogControlDestinationFileRn": cfprSysdebugLogControlDestinationFileRn,
       "cfprSysdebugLogControlDestinationFileBackupCount": cfprSysdebugLogControlDestinationFileBackupCount,
       "cfprSysdebugLogControlDestinationFileDefaultLevel": cfprSysdebugLogControlDestinationFileDefaultLevel,
       "cfprSysdebugLogControlDestinationFileDefaultSize": cfprSysdebugLogControlDestinationFileDefaultSize,
       "cfprSysdebugLogControlDestinationFileLevel": cfprSysdebugLogControlDestinationFileLevel,
       "cfprSysdebugLogControlDestinationFileSize": cfprSysdebugLogControlDestinationFileSize,
       "cfprSysdebugLogControlDestinationSyslogTable": cfprSysdebugLogControlDestinationSyslogTable,
       "cfprSysdebugLogControlDestinationSyslogEntry": cfprSysdebugLogControlDestinationSyslogEntry,
       "cfprSysdebugLogControlDestinationSyslogInstanceId": cfprSysdebugLogControlDestinationSyslogInstanceId,
       "cfprSysdebugLogControlDestinationSyslogDn": cfprSysdebugLogControlDestinationSyslogDn,
       "cfprSysdebugLogControlDestinationSyslogRn": cfprSysdebugLogControlDestinationSyslogRn,
       "cfprSysdebugLogControlDestinationSyslogDefaultLevel": cfprSysdebugLogControlDestinationSyslogDefaultLevel,
       "cfprSysdebugLogControlDestinationSyslogLevel": cfprSysdebugLogControlDestinationSyslogLevel,
       "cfprSysdebugLogControlDomainTable": cfprSysdebugLogControlDomainTable,
       "cfprSysdebugLogControlDomainEntry": cfprSysdebugLogControlDomainEntry,
       "cfprSysdebugLogControlDomainInstanceId": cfprSysdebugLogControlDomainInstanceId,
       "cfprSysdebugLogControlDomainDn": cfprSysdebugLogControlDomainDn,
       "cfprSysdebugLogControlDomainRn": cfprSysdebugLogControlDomainRn,
       "cfprSysdebugLogControlDomainLevel": cfprSysdebugLogControlDomainLevel,
       "cfprSysdebugLogControlDomainLevelFlag": cfprSysdebugLogControlDomainLevelFlag,
       "cfprSysdebugLogControlDomainName": cfprSysdebugLogControlDomainName,
       "cfprSysdebugLogControlDomainPersist": cfprSysdebugLogControlDomainPersist,
       "cfprSysdebugLogControlDomainReset": cfprSysdebugLogControlDomainReset,
       "cfprSysdebugLogControlEpTable": cfprSysdebugLogControlEpTable,
       "cfprSysdebugLogControlEpEntry": cfprSysdebugLogControlEpEntry,
       "cfprSysdebugLogControlEpInstanceId": cfprSysdebugLogControlEpInstanceId,
       "cfprSysdebugLogControlEpDn": cfprSysdebugLogControlEpDn,
       "cfprSysdebugLogControlEpRn": cfprSysdebugLogControlEpRn,
       "cfprSysdebugLogControlEpFsmDescr": cfprSysdebugLogControlEpFsmDescr,
       "cfprSysdebugLogControlEpFsmPrev": cfprSysdebugLogControlEpFsmPrev,
       "cfprSysdebugLogControlEpFsmProgr": cfprSysdebugLogControlEpFsmProgr,
       "cfprSysdebugLogControlEpFsmRmtInvErrCode": cfprSysdebugLogControlEpFsmRmtInvErrCode,
       "cfprSysdebugLogControlEpFsmRmtInvErrDescr": cfprSysdebugLogControlEpFsmRmtInvErrDescr,
       "cfprSysdebugLogControlEpFsmRmtInvRslt": cfprSysdebugLogControlEpFsmRmtInvRslt,
       "cfprSysdebugLogControlEpFsmStageDescr": cfprSysdebugLogControlEpFsmStageDescr,
       "cfprSysdebugLogControlEpFsmStamp": cfprSysdebugLogControlEpFsmStamp,
       "cfprSysdebugLogControlEpFsmStatus": cfprSysdebugLogControlEpFsmStatus,
       "cfprSysdebugLogControlEpFsmTry": cfprSysdebugLogControlEpFsmTry,
       "cfprSysdebugLogControlEpLevel": cfprSysdebugLogControlEpLevel,
       "cfprSysdebugLogControlEpLevelFlag": cfprSysdebugLogControlEpLevelFlag,
       "cfprSysdebugLogControlEpPersist": cfprSysdebugLogControlEpPersist,
       "cfprSysdebugLogControlEpReset": cfprSysdebugLogControlEpReset,
       "cfprSysdebugLogControlEpFsmTable": cfprSysdebugLogControlEpFsmTable,
       "cfprSysdebugLogControlEpFsmEntry": cfprSysdebugLogControlEpFsmEntry,
       "cfprSysdebugLogControlEpFsmInstanceId": cfprSysdebugLogControlEpFsmInstanceId,
       "cfprSysdebugLogControlEpFsmDn": cfprSysdebugLogControlEpFsmDn,
       "cfprSysdebugLogControlEpFsmRn": cfprSysdebugLogControlEpFsmRn,
       "cfprSysdebugLogControlEpFsmCompletionTime": cfprSysdebugLogControlEpFsmCompletionTime,
       "cfprSysdebugLogControlEpFsmCurrentFsm": cfprSysdebugLogControlEpFsmCurrentFsm,
       "cfprSysdebugLogControlEpFsmDescrData": cfprSysdebugLogControlEpFsmDescrData,
       "cfprSysdebugLogControlEpFsmFsmStatus": cfprSysdebugLogControlEpFsmFsmStatus,
       "cfprSysdebugLogControlEpFsmProgress": cfprSysdebugLogControlEpFsmProgress,
       "cfprSysdebugLogControlEpFsmRmtErrCode": cfprSysdebugLogControlEpFsmRmtErrCode,
       "cfprSysdebugLogControlEpFsmRmtErrDescr": cfprSysdebugLogControlEpFsmRmtErrDescr,
       "cfprSysdebugLogControlEpFsmRmtRslt": cfprSysdebugLogControlEpFsmRmtRslt,
       "cfprSysdebugLogControlEpFsmStageTable": cfprSysdebugLogControlEpFsmStageTable,
       "cfprSysdebugLogControlEpFsmStageEntry": cfprSysdebugLogControlEpFsmStageEntry,
       "cfprSysdebugLogControlEpFsmStageInstanceId": cfprSysdebugLogControlEpFsmStageInstanceId,
       "cfprSysdebugLogControlEpFsmStageDn": cfprSysdebugLogControlEpFsmStageDn,
       "cfprSysdebugLogControlEpFsmStageRn": cfprSysdebugLogControlEpFsmStageRn,
       "cfprSysdebugLogControlEpFsmStageDescrData": cfprSysdebugLogControlEpFsmStageDescrData,
       "cfprSysdebugLogControlEpFsmStageLastUpdateTime": cfprSysdebugLogControlEpFsmStageLastUpdateTime,
       "cfprSysdebugLogControlEpFsmStageName": cfprSysdebugLogControlEpFsmStageName,
       "cfprSysdebugLogControlEpFsmStageOrder": cfprSysdebugLogControlEpFsmStageOrder,
       "cfprSysdebugLogControlEpFsmStageRetry": cfprSysdebugLogControlEpFsmStageRetry,
       "cfprSysdebugLogControlEpFsmStageStageStatus": cfprSysdebugLogControlEpFsmStageStageStatus,
       "cfprSysdebugLogControlEpFsmTaskTable": cfprSysdebugLogControlEpFsmTaskTable,
       "cfprSysdebugLogControlEpFsmTaskEntry": cfprSysdebugLogControlEpFsmTaskEntry,
       "cfprSysdebugLogControlEpFsmTaskInstanceId": cfprSysdebugLogControlEpFsmTaskInstanceId,
       "cfprSysdebugLogControlEpFsmTaskDn": cfprSysdebugLogControlEpFsmTaskDn,
       "cfprSysdebugLogControlEpFsmTaskRn": cfprSysdebugLogControlEpFsmTaskRn,
       "cfprSysdebugLogControlEpFsmTaskCompletion": cfprSysdebugLogControlEpFsmTaskCompletion,
       "cfprSysdebugLogControlEpFsmTaskFlags": cfprSysdebugLogControlEpFsmTaskFlags,
       "cfprSysdebugLogControlEpFsmTaskItem": cfprSysdebugLogControlEpFsmTaskItem,
       "cfprSysdebugLogControlEpFsmTaskSeqId": cfprSysdebugLogControlEpFsmTaskSeqId,
       "cfprSysdebugLogControlModuleTable": cfprSysdebugLogControlModuleTable,
       "cfprSysdebugLogControlModuleEntry": cfprSysdebugLogControlModuleEntry,
       "cfprSysdebugLogControlModuleInstanceId": cfprSysdebugLogControlModuleInstanceId,
       "cfprSysdebugLogControlModuleDn": cfprSysdebugLogControlModuleDn,
       "cfprSysdebugLogControlModuleRn": cfprSysdebugLogControlModuleRn,
       "cfprSysdebugLogControlModuleDefaultLevel": cfprSysdebugLogControlModuleDefaultLevel,
       "cfprSysdebugLogControlModuleLevel": cfprSysdebugLogControlModuleLevel,
       "cfprSysdebugLogControlModuleName": cfprSysdebugLogControlModuleName,
       "cfprSysdebugLogControlModuleReset": cfprSysdebugLogControlModuleReset,
       "cfprSysdebugLogExportPolicyTable": cfprSysdebugLogExportPolicyTable,
       "cfprSysdebugLogExportPolicyEntry": cfprSysdebugLogExportPolicyEntry,
       "cfprSysdebugLogExportPolicyInstanceId": cfprSysdebugLogExportPolicyInstanceId,
       "cfprSysdebugLogExportPolicyDn": cfprSysdebugLogExportPolicyDn,
       "cfprSysdebugLogExportPolicyRn": cfprSysdebugLogExportPolicyRn,
       "cfprSysdebugLogExportPolicyAdminState": cfprSysdebugLogExportPolicyAdminState,
       "cfprSysdebugLogExportPolicyDescr": cfprSysdebugLogExportPolicyDescr,
       "cfprSysdebugLogExportPolicyFsmDescr": cfprSysdebugLogExportPolicyFsmDescr,
       "cfprSysdebugLogExportPolicyFsmPrev": cfprSysdebugLogExportPolicyFsmPrev,
       "cfprSysdebugLogExportPolicyFsmProgr": cfprSysdebugLogExportPolicyFsmProgr,
       "cfprSysdebugLogExportPolicyFsmRmtInvErrCode": cfprSysdebugLogExportPolicyFsmRmtInvErrCode,
       "cfprSysdebugLogExportPolicyFsmRmtInvErrDescr": cfprSysdebugLogExportPolicyFsmRmtInvErrDescr,
       "cfprSysdebugLogExportPolicyFsmRmtInvRslt": cfprSysdebugLogExportPolicyFsmRmtInvRslt,
       "cfprSysdebugLogExportPolicyFsmStageDescr": cfprSysdebugLogExportPolicyFsmStageDescr,
       "cfprSysdebugLogExportPolicyFsmStamp": cfprSysdebugLogExportPolicyFsmStamp,
       "cfprSysdebugLogExportPolicyFsmStatus": cfprSysdebugLogExportPolicyFsmStatus,
       "cfprSysdebugLogExportPolicyFsmTry": cfprSysdebugLogExportPolicyFsmTry,
       "cfprSysdebugLogExportPolicyHostname": cfprSysdebugLogExportPolicyHostname,
       "cfprSysdebugLogExportPolicyIntId": cfprSysdebugLogExportPolicyIntId,
       "cfprSysdebugLogExportPolicyName": cfprSysdebugLogExportPolicyName,
       "cfprSysdebugLogExportPolicyPasswordlessSsh": cfprSysdebugLogExportPolicyPasswordlessSsh,
       "cfprSysdebugLogExportPolicyPath": cfprSysdebugLogExportPolicyPath,
       "cfprSysdebugLogExportPolicyPolicyLevel": cfprSysdebugLogExportPolicyPolicyLevel,
       "cfprSysdebugLogExportPolicyPolicyOwner": cfprSysdebugLogExportPolicyPolicyOwner,
       "cfprSysdebugLogExportPolicyPostAction": cfprSysdebugLogExportPolicyPostAction,
       "cfprSysdebugLogExportPolicyProto": cfprSysdebugLogExportPolicyProto,
       "cfprSysdebugLogExportPolicyPwd": cfprSysdebugLogExportPolicyPwd,
       "cfprSysdebugLogExportPolicyUser": cfprSysdebugLogExportPolicyUser,
       "cfprSysdebugLogExportPolicyFsmTable": cfprSysdebugLogExportPolicyFsmTable,
       "cfprSysdebugLogExportPolicyFsmEntry": cfprSysdebugLogExportPolicyFsmEntry,
       "cfprSysdebugLogExportPolicyFsmInstanceId": cfprSysdebugLogExportPolicyFsmInstanceId,
       "cfprSysdebugLogExportPolicyFsmDn": cfprSysdebugLogExportPolicyFsmDn,
       "cfprSysdebugLogExportPolicyFsmRn": cfprSysdebugLogExportPolicyFsmRn,
       "cfprSysdebugLogExportPolicyFsmCompletionTime": cfprSysdebugLogExportPolicyFsmCompletionTime,
       "cfprSysdebugLogExportPolicyFsmCurrentFsm": cfprSysdebugLogExportPolicyFsmCurrentFsm,
       "cfprSysdebugLogExportPolicyFsmDescrData": cfprSysdebugLogExportPolicyFsmDescrData,
       "cfprSysdebugLogExportPolicyFsmFsmStatus": cfprSysdebugLogExportPolicyFsmFsmStatus,
       "cfprSysdebugLogExportPolicyFsmProgress": cfprSysdebugLogExportPolicyFsmProgress,
       "cfprSysdebugLogExportPolicyFsmRmtErrCode": cfprSysdebugLogExportPolicyFsmRmtErrCode,
       "cfprSysdebugLogExportPolicyFsmRmtErrDescr": cfprSysdebugLogExportPolicyFsmRmtErrDescr,
       "cfprSysdebugLogExportPolicyFsmRmtRslt": cfprSysdebugLogExportPolicyFsmRmtRslt,
       "cfprSysdebugLogExportPolicyFsmStageTable": cfprSysdebugLogExportPolicyFsmStageTable,
       "cfprSysdebugLogExportPolicyFsmStageEntry": cfprSysdebugLogExportPolicyFsmStageEntry,
       "cfprSysdebugLogExportPolicyFsmStageInstanceId": cfprSysdebugLogExportPolicyFsmStageInstanceId,
       "cfprSysdebugLogExportPolicyFsmStageDn": cfprSysdebugLogExportPolicyFsmStageDn,
       "cfprSysdebugLogExportPolicyFsmStageRn": cfprSysdebugLogExportPolicyFsmStageRn,
       "cfprSysdebugLogExportPolicyFsmStageDescrData": cfprSysdebugLogExportPolicyFsmStageDescrData,
       "cfprSysdebugLogExportPolicyFsmStageLastUpdateTime": cfprSysdebugLogExportPolicyFsmStageLastUpdateTime,
       "cfprSysdebugLogExportPolicyFsmStageName": cfprSysdebugLogExportPolicyFsmStageName,
       "cfprSysdebugLogExportPolicyFsmStageOrder": cfprSysdebugLogExportPolicyFsmStageOrder,
       "cfprSysdebugLogExportPolicyFsmStageRetry": cfprSysdebugLogExportPolicyFsmStageRetry,
       "cfprSysdebugLogExportPolicyFsmStageStageStatus": cfprSysdebugLogExportPolicyFsmStageStageStatus,
       "cfprSysdebugLogExportPolicyFsmTaskTable": cfprSysdebugLogExportPolicyFsmTaskTable,
       "cfprSysdebugLogExportPolicyFsmTaskEntry": cfprSysdebugLogExportPolicyFsmTaskEntry,
       "cfprSysdebugLogExportPolicyFsmTaskInstanceId": cfprSysdebugLogExportPolicyFsmTaskInstanceId,
       "cfprSysdebugLogExportPolicyFsmTaskDn": cfprSysdebugLogExportPolicyFsmTaskDn,
       "cfprSysdebugLogExportPolicyFsmTaskRn": cfprSysdebugLogExportPolicyFsmTaskRn,
       "cfprSysdebugLogExportPolicyFsmTaskCompletion": cfprSysdebugLogExportPolicyFsmTaskCompletion,
       "cfprSysdebugLogExportPolicyFsmTaskFlags": cfprSysdebugLogExportPolicyFsmTaskFlags,
       "cfprSysdebugLogExportPolicyFsmTaskItem": cfprSysdebugLogExportPolicyFsmTaskItem,
       "cfprSysdebugLogExportPolicyFsmTaskSeqId": cfprSysdebugLogExportPolicyFsmTaskSeqId,
       "cfprSysdebugLogExportStatusTable": cfprSysdebugLogExportStatusTable,
       "cfprSysdebugLogExportStatusEntry": cfprSysdebugLogExportStatusEntry,
       "cfprSysdebugLogExportStatusInstanceId": cfprSysdebugLogExportStatusInstanceId,
       "cfprSysdebugLogExportStatusDn": cfprSysdebugLogExportStatusDn,
       "cfprSysdebugLogExportStatusRn": cfprSysdebugLogExportStatusRn,
       "cfprSysdebugLogExportStatusExportFailureReason": cfprSysdebugLogExportStatusExportFailureReason,
       "cfprSysdebugLogExportStatusExportStatus": cfprSysdebugLogExportStatusExportStatus,
       "cfprSysdebugLogExportStatusSwitchId": cfprSysdebugLogExportStatusSwitchId,
       "cfprSysdebugMEpLogTable": cfprSysdebugMEpLogTable,
       "cfprSysdebugMEpLogEntry": cfprSysdebugMEpLogEntry,
       "cfprSysdebugMEpLogInstanceId": cfprSysdebugMEpLogInstanceId,
       "cfprSysdebugMEpLogDn": cfprSysdebugMEpLogDn,
       "cfprSysdebugMEpLogRn": cfprSysdebugMEpLogRn,
       "cfprSysdebugMEpLogAdminState": cfprSysdebugMEpLogAdminState,
       "cfprSysdebugMEpLogCapacity": cfprSysdebugMEpLogCapacity,
       "cfprSysdebugMEpLogId": cfprSysdebugMEpLogId,
       "cfprSysdebugMEpLogLastUpdate": cfprSysdebugMEpLogLastUpdate,
       "cfprSysdebugMEpLogOperState": cfprSysdebugMEpLogOperState,
       "cfprSysdebugMEpLogType": cfprSysdebugMEpLogType,
       "cfprSysdebugMEpLogPolicyTable": cfprSysdebugMEpLogPolicyTable,
       "cfprSysdebugMEpLogPolicyEntry": cfprSysdebugMEpLogPolicyEntry,
       "cfprSysdebugMEpLogPolicyInstanceId": cfprSysdebugMEpLogPolicyInstanceId,
       "cfprSysdebugMEpLogPolicyDn": cfprSysdebugMEpLogPolicyDn,
       "cfprSysdebugMEpLogPolicyRn": cfprSysdebugMEpLogPolicyRn,
       "cfprSysdebugMEpLogPolicyDescr": cfprSysdebugMEpLogPolicyDescr,
       "cfprSysdebugMEpLogPolicyIntId": cfprSysdebugMEpLogPolicyIntId,
       "cfprSysdebugMEpLogPolicyName": cfprSysdebugMEpLogPolicyName,
       "cfprSysdebugMEpLogPolicyPolicyLevel": cfprSysdebugMEpLogPolicyPolicyLevel,
       "cfprSysdebugMEpLogPolicyPolicyOwner": cfprSysdebugMEpLogPolicyPolicyOwner,
       "cfprSysdebugMEpLogPolicyType": cfprSysdebugMEpLogPolicyType,
       "cfprSysdebugManualCoreFileExportTargetTable": cfprSysdebugManualCoreFileExportTargetTable,
       "cfprSysdebugManualCoreFileExportTargetEntry": cfprSysdebugManualCoreFileExportTargetEntry,
       "cfprSysdebugManualCoreFileExportTargetInstanceId": cfprSysdebugManualCoreFileExportTargetInstanceId,
       "cfprSysdebugManualCoreFileExportTargetDn": cfprSysdebugManualCoreFileExportTargetDn,
       "cfprSysdebugManualCoreFileExportTargetRn": cfprSysdebugManualCoreFileExportTargetRn,
       "cfprSysdebugManualCoreFileExportTargetAdminState": cfprSysdebugManualCoreFileExportTargetAdminState,
       "cfprSysdebugManualCoreFileExportTargetDescr": cfprSysdebugManualCoreFileExportTargetDescr,
       "cfprSysdebugManualCoreFileExportTargetExportFailureReason": cfprSysdebugManualCoreFileExportTargetExportFailureReason,
       "cfprSysdebugManualCoreFileExportTargetExportStatus": cfprSysdebugManualCoreFileExportTargetExportStatus,
       "cfprSysdebugManualCoreFileExportTargetFsmDescr": cfprSysdebugManualCoreFileExportTargetFsmDescr,
       "cfprSysdebugManualCoreFileExportTargetFsmPrev": cfprSysdebugManualCoreFileExportTargetFsmPrev,
       "cfprSysdebugManualCoreFileExportTargetFsmProgr": cfprSysdebugManualCoreFileExportTargetFsmProgr,
       "cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrCode": cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrCode,
       "cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr": cfprSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr,
       "cfprSysdebugManualCoreFileExportTargetFsmRmtInvRslt": cfprSysdebugManualCoreFileExportTargetFsmRmtInvRslt,
       "cfprSysdebugManualCoreFileExportTargetFsmStageDescr": cfprSysdebugManualCoreFileExportTargetFsmStageDescr,
       "cfprSysdebugManualCoreFileExportTargetFsmStamp": cfprSysdebugManualCoreFileExportTargetFsmStamp,
       "cfprSysdebugManualCoreFileExportTargetFsmStatus": cfprSysdebugManualCoreFileExportTargetFsmStatus,
       "cfprSysdebugManualCoreFileExportTargetFsmTry": cfprSysdebugManualCoreFileExportTargetFsmTry,
       "cfprSysdebugManualCoreFileExportTargetHostname": cfprSysdebugManualCoreFileExportTargetHostname,
       "cfprSysdebugManualCoreFileExportTargetIntId": cfprSysdebugManualCoreFileExportTargetIntId,
       "cfprSysdebugManualCoreFileExportTargetName": cfprSysdebugManualCoreFileExportTargetName,
       "cfprSysdebugManualCoreFileExportTargetPath": cfprSysdebugManualCoreFileExportTargetPath,
       "cfprSysdebugManualCoreFileExportTargetPolicyLevel": cfprSysdebugManualCoreFileExportTargetPolicyLevel,
       "cfprSysdebugManualCoreFileExportTargetPolicyOwner": cfprSysdebugManualCoreFileExportTargetPolicyOwner,
       "cfprSysdebugManualCoreFileExportTargetPort": cfprSysdebugManualCoreFileExportTargetPort,
       "cfprSysdebugManualCoreFileExportTargetPostAction": cfprSysdebugManualCoreFileExportTargetPostAction,
       "cfprSysdebugManualCoreFileExportTargetProto": cfprSysdebugManualCoreFileExportTargetProto,
       "cfprSysdebugManualCoreFileExportTargetFsmTable": cfprSysdebugManualCoreFileExportTargetFsmTable,
       "cfprSysdebugManualCoreFileExportTargetFsmEntry": cfprSysdebugManualCoreFileExportTargetFsmEntry,
       "cfprSysdebugManualCoreFileExportTargetFsmInstanceId": cfprSysdebugManualCoreFileExportTargetFsmInstanceId,
       "cfprSysdebugManualCoreFileExportTargetFsmDn": cfprSysdebugManualCoreFileExportTargetFsmDn,
       "cfprSysdebugManualCoreFileExportTargetFsmRn": cfprSysdebugManualCoreFileExportTargetFsmRn,
       "cfprSysdebugManualCoreFileExportTargetFsmCompletionTime": cfprSysdebugManualCoreFileExportTargetFsmCompletionTime,
       "cfprSysdebugManualCoreFileExportTargetFsmCurrentFsm": cfprSysdebugManualCoreFileExportTargetFsmCurrentFsm,
       "cfprSysdebugManualCoreFileExportTargetFsmDescrData": cfprSysdebugManualCoreFileExportTargetFsmDescrData,
       "cfprSysdebugManualCoreFileExportTargetFsmFsmStatus": cfprSysdebugManualCoreFileExportTargetFsmFsmStatus,
       "cfprSysdebugManualCoreFileExportTargetFsmProgress": cfprSysdebugManualCoreFileExportTargetFsmProgress,
       "cfprSysdebugManualCoreFileExportTargetFsmRmtErrCode": cfprSysdebugManualCoreFileExportTargetFsmRmtErrCode,
       "cfprSysdebugManualCoreFileExportTargetFsmRmtErrDescr": cfprSysdebugManualCoreFileExportTargetFsmRmtErrDescr,
       "cfprSysdebugManualCoreFileExportTargetFsmRmtRslt": cfprSysdebugManualCoreFileExportTargetFsmRmtRslt,
       "cfprSysdebugManualCoreFileExportTargetFsmStageTable": cfprSysdebugManualCoreFileExportTargetFsmStageTable,
       "cfprSysdebugManualCoreFileExportTargetFsmStageEntry": cfprSysdebugManualCoreFileExportTargetFsmStageEntry,
       "cfprSysdebugManualCoreFileExportTargetFsmStageInstanceId": cfprSysdebugManualCoreFileExportTargetFsmStageInstanceId,
       "cfprSysdebugManualCoreFileExportTargetFsmStageDn": cfprSysdebugManualCoreFileExportTargetFsmStageDn,
       "cfprSysdebugManualCoreFileExportTargetFsmStageRn": cfprSysdebugManualCoreFileExportTargetFsmStageRn,
       "cfprSysdebugManualCoreFileExportTargetFsmStageDescrData": cfprSysdebugManualCoreFileExportTargetFsmStageDescrData,
       "cfprSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime": cfprSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime,
       "cfprSysdebugManualCoreFileExportTargetFsmStageName": cfprSysdebugManualCoreFileExportTargetFsmStageName,
       "cfprSysdebugManualCoreFileExportTargetFsmStageOrder": cfprSysdebugManualCoreFileExportTargetFsmStageOrder,
       "cfprSysdebugManualCoreFileExportTargetFsmStageRetry": cfprSysdebugManualCoreFileExportTargetFsmStageRetry,
       "cfprSysdebugManualCoreFileExportTargetFsmStageStageStatus": cfprSysdebugManualCoreFileExportTargetFsmStageStageStatus,
       "cfprSysdebugManualCoreFileExportTargetFsmTaskTable": cfprSysdebugManualCoreFileExportTargetFsmTaskTable,
       "cfprSysdebugManualCoreFileExportTargetFsmTaskEntry": cfprSysdebugManualCoreFileExportTargetFsmTaskEntry,
       "cfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId": cfprSysdebugManualCoreFileExportTargetFsmTaskInstanceId,
       "cfprSysdebugManualCoreFileExportTargetFsmTaskDn": cfprSysdebugManualCoreFileExportTargetFsmTaskDn,
       "cfprSysdebugManualCoreFileExportTargetFsmTaskRn": cfprSysdebugManualCoreFileExportTargetFsmTaskRn,
       "cfprSysdebugManualCoreFileExportTargetFsmTaskCompletion": cfprSysdebugManualCoreFileExportTargetFsmTaskCompletion,
       "cfprSysdebugManualCoreFileExportTargetFsmTaskFlags": cfprSysdebugManualCoreFileExportTargetFsmTaskFlags,
       "cfprSysdebugManualCoreFileExportTargetFsmTaskItem": cfprSysdebugManualCoreFileExportTargetFsmTaskItem,
       "cfprSysdebugManualCoreFileExportTargetFsmTaskSeqId": cfprSysdebugManualCoreFileExportTargetFsmTaskSeqId,
       "cfprSysdebugTechSupFileRepositoryTable": cfprSysdebugTechSupFileRepositoryTable,
       "cfprSysdebugTechSupFileRepositoryEntry": cfprSysdebugTechSupFileRepositoryEntry,
       "cfprSysdebugTechSupFileRepositoryInstanceId": cfprSysdebugTechSupFileRepositoryInstanceId,
       "cfprSysdebugTechSupFileRepositoryDn": cfprSysdebugTechSupFileRepositoryDn,
       "cfprSysdebugTechSupFileRepositoryRn": cfprSysdebugTechSupFileRepositoryRn,
       "cfprSysdebugTechSupportTable": cfprSysdebugTechSupportTable,
       "cfprSysdebugTechSupportEntry": cfprSysdebugTechSupportEntry,
       "cfprSysdebugTechSupportInstanceId": cfprSysdebugTechSupportInstanceId,
       "cfprSysdebugTechSupportDn": cfprSysdebugTechSupportDn,
       "cfprSysdebugTechSupportRn": cfprSysdebugTechSupportRn,
       "cfprSysdebugTechSupportAdminState": cfprSysdebugTechSupportAdminState,
       "cfprSysdebugTechSupportCreationTS": cfprSysdebugTechSupportCreationTS,
       "cfprSysdebugTechSupportDescr": cfprSysdebugTechSupportDescr,
       "cfprSysdebugTechSupportFsmDescr": cfprSysdebugTechSupportFsmDescr,
       "cfprSysdebugTechSupportFsmPrev": cfprSysdebugTechSupportFsmPrev,
       "cfprSysdebugTechSupportFsmProgr": cfprSysdebugTechSupportFsmProgr,
       "cfprSysdebugTechSupportFsmRmtInvErrCode": cfprSysdebugTechSupportFsmRmtInvErrCode,
       "cfprSysdebugTechSupportFsmRmtInvErrDescr": cfprSysdebugTechSupportFsmRmtInvErrDescr,
       "cfprSysdebugTechSupportFsmRmtInvRslt": cfprSysdebugTechSupportFsmRmtInvRslt,
       "cfprSysdebugTechSupportFsmStageDescr": cfprSysdebugTechSupportFsmStageDescr,
       "cfprSysdebugTechSupportFsmStamp": cfprSysdebugTechSupportFsmStamp,
       "cfprSysdebugTechSupportFsmStatus": cfprSysdebugTechSupportFsmStatus,
       "cfprSysdebugTechSupportFsmTry": cfprSysdebugTechSupportFsmTry,
       "cfprSysdebugTechSupportName": cfprSysdebugTechSupportName,
       "cfprSysdebugTechSupportOperState": cfprSysdebugTechSupportOperState,
       "cfprSysdebugTechSupportSize": cfprSysdebugTechSupportSize,
       "cfprSysdebugTechSupportSwitchId": cfprSysdebugTechSupportSwitchId,
       "cfprSysdebugTechSupportTs": cfprSysdebugTechSupportTs,
       "cfprSysdebugTechSupportUri": cfprSysdebugTechSupportUri,
       "cfprSysdebugTechSupportCmdOptTable": cfprSysdebugTechSupportCmdOptTable,
       "cfprSysdebugTechSupportCmdOptEntry": cfprSysdebugTechSupportCmdOptEntry,
       "cfprSysdebugTechSupportCmdOptInstanceId": cfprSysdebugTechSupportCmdOptInstanceId,
       "cfprSysdebugTechSupportCmdOptDn": cfprSysdebugTechSupportCmdOptDn,
       "cfprSysdebugTechSupportCmdOptRn": cfprSysdebugTechSupportCmdOptRn,
       "cfprSysdebugTechSupportCmdOptChassisCimcId": cfprSysdebugTechSupportCmdOptChassisCimcId,
       "cfprSysdebugTechSupportCmdOptChassisId": cfprSysdebugTechSupportCmdOptChassisId,
       "cfprSysdebugTechSupportCmdOptChassisIomId": cfprSysdebugTechSupportCmdOptChassisIomId,
       "cfprSysdebugTechSupportCmdOptCimcAdapterId": cfprSysdebugTechSupportCmdOptCimcAdapterId,
       "cfprSysdebugTechSupportCmdOptFabExtId": cfprSysdebugTechSupportCmdOptFabExtId,
       "cfprSysdebugTechSupportCmdOptMajorOptType": cfprSysdebugTechSupportCmdOptMajorOptType,
       "cfprSysdebugTechSupportCmdOptRackServerAdapterId": cfprSysdebugTechSupportCmdOptRackServerAdapterId,
       "cfprSysdebugTechSupportCmdOptRackServerId": cfprSysdebugTechSupportCmdOptRackServerId,
       "cfprSysdebugTechSupportFsmTable": cfprSysdebugTechSupportFsmTable,
       "cfprSysdebugTechSupportFsmEntry": cfprSysdebugTechSupportFsmEntry,
       "cfprSysdebugTechSupportFsmInstanceId": cfprSysdebugTechSupportFsmInstanceId,
       "cfprSysdebugTechSupportFsmDn": cfprSysdebugTechSupportFsmDn,
       "cfprSysdebugTechSupportFsmRn": cfprSysdebugTechSupportFsmRn,
       "cfprSysdebugTechSupportFsmCompletionTime": cfprSysdebugTechSupportFsmCompletionTime,
       "cfprSysdebugTechSupportFsmCurrentFsm": cfprSysdebugTechSupportFsmCurrentFsm,
       "cfprSysdebugTechSupportFsmDescrData": cfprSysdebugTechSupportFsmDescrData,
       "cfprSysdebugTechSupportFsmFsmStatus": cfprSysdebugTechSupportFsmFsmStatus,
       "cfprSysdebugTechSupportFsmProgress": cfprSysdebugTechSupportFsmProgress,
       "cfprSysdebugTechSupportFsmRmtErrCode": cfprSysdebugTechSupportFsmRmtErrCode,
       "cfprSysdebugTechSupportFsmRmtErrDescr": cfprSysdebugTechSupportFsmRmtErrDescr,
       "cfprSysdebugTechSupportFsmRmtRslt": cfprSysdebugTechSupportFsmRmtRslt,
       "cfprSysdebugTechSupportFsmStageTable": cfprSysdebugTechSupportFsmStageTable,
       "cfprSysdebugTechSupportFsmStageEntry": cfprSysdebugTechSupportFsmStageEntry,
       "cfprSysdebugTechSupportFsmStageInstanceId": cfprSysdebugTechSupportFsmStageInstanceId,
       "cfprSysdebugTechSupportFsmStageDn": cfprSysdebugTechSupportFsmStageDn,
       "cfprSysdebugTechSupportFsmStageRn": cfprSysdebugTechSupportFsmStageRn,
       "cfprSysdebugTechSupportFsmStageDescrData": cfprSysdebugTechSupportFsmStageDescrData,
       "cfprSysdebugTechSupportFsmStageLastUpdateTime": cfprSysdebugTechSupportFsmStageLastUpdateTime,
       "cfprSysdebugTechSupportFsmStageName": cfprSysdebugTechSupportFsmStageName,
       "cfprSysdebugTechSupportFsmStageOrder": cfprSysdebugTechSupportFsmStageOrder,
       "cfprSysdebugTechSupportFsmStageRetry": cfprSysdebugTechSupportFsmStageRetry,
       "cfprSysdebugTechSupportFsmStageStageStatus": cfprSysdebugTechSupportFsmStageStageStatus,
       "cfprSysdebugTechSupportFsmTaskTable": cfprSysdebugTechSupportFsmTaskTable,
       "cfprSysdebugTechSupportFsmTaskEntry": cfprSysdebugTechSupportFsmTaskEntry,
       "cfprSysdebugTechSupportFsmTaskInstanceId": cfprSysdebugTechSupportFsmTaskInstanceId,
       "cfprSysdebugTechSupportFsmTaskDn": cfprSysdebugTechSupportFsmTaskDn,
       "cfprSysdebugTechSupportFsmTaskRn": cfprSysdebugTechSupportFsmTaskRn,
       "cfprSysdebugTechSupportFsmTaskCompletion": cfprSysdebugTechSupportFsmTaskCompletion,
       "cfprSysdebugTechSupportFsmTaskFlags": cfprSysdebugTechSupportFsmTaskFlags,
       "cfprSysdebugTechSupportFsmTaskItem": cfprSysdebugTechSupportFsmTaskItem,
       "cfprSysdebugTechSupportFsmTaskSeqId": cfprSysdebugTechSupportFsmTaskSeqId,
       "cfprSysdebugAdaptorCoreStatsTable": cfprSysdebugAdaptorCoreStatsTable,
       "cfprSysdebugAdaptorCoreStatsEntry": cfprSysdebugAdaptorCoreStatsEntry,
       "cfprSysdebugAdaptorCoreStatsInstanceId": cfprSysdebugAdaptorCoreStatsInstanceId,
       "cfprSysdebugAdaptorCoreStatsDn": cfprSysdebugAdaptorCoreStatsDn,
       "cfprSysdebugAdaptorCoreStatsRn": cfprSysdebugAdaptorCoreStatsRn,
       "cfprSysdebugAdaptorCoreStatsAdaptorId": cfprSysdebugAdaptorCoreStatsAdaptorId,
       "cfprSysdebugAdaptorCoreStatsExcessiveCore": cfprSysdebugAdaptorCoreStatsExcessiveCore,
       "cfprSysdebugAdaptorCoreStatsNumCore": cfprSysdebugAdaptorCoreStatsNumCore,
       "cfprSysdebugAdaptorCoreStatsSlotId": cfprSysdebugAdaptorCoreStatsSlotId}
)
