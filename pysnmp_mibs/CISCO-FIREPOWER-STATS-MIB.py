_Q='cfprStatsThresholdPolicyInstanceId'
_P='cfprStatsThresholdClassInstanceId'
_O='cfprStatsThrFloatValueInstanceId'
_N='cfprStatsThrFloatDefinitionInstanceId'
_M='cfprStatsThr64ValueInstanceId'
_L='cfprStatsThr64DefinitionInstanceId'
_K='cfprStatsThr32ValueInstanceId'
_J='cfprStatsThr32DefinitionInstanceId'
_I='cfprStatsHolderInstanceId'
_H='cfprStatsCollectionPolicyFsmTaskInstanceId'
_G='cfprStatsCollectionPolicyFsmStageInstanceId'
_F='cfprStatsCollectionPolicyFsmInstanceId'
_E='cfprStatsCollectionPolicyInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-STATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprConditionRemoteInvRslt,CfprConditionSeverity,CfprFsmCompletion,CfprFsmFlags,CfprFsmFsmStageStatus,CfprPolicyPolicyOwner,CfprStatsCollectionDomain,CfprStatsCollectionInterval,CfprStatsCollectionPolicyFsmCurrentFsm,CfprStatsCollectionPolicyFsmStageName,CfprStatsCollectionPolicyFsmTaskItem,CfprStatsReportingInterval,CfprStatsThr32DefinitionPropType,CfprStatsThr32ValuePropType,CfprStatsThr64DefinitionPropType,CfprStatsThr64ValuePropType,CfprStatsThrFloatDefinitionPropType,CfprStatsThrFloatValuePropType,CfprStatsThresholdDirection=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprConditionRemoteInvRslt','CfprConditionSeverity','CfprFsmCompletion','CfprFsmFlags','CfprFsmFsmStageStatus','CfprPolicyPolicyOwner','CfprStatsCollectionDomain','CfprStatsCollectionInterval','CfprStatsCollectionPolicyFsmCurrentFsm','CfprStatsCollectionPolicyFsmStageName','CfprStatsCollectionPolicyFsmTaskItem','CfprStatsReportingInterval','CfprStatsThr32DefinitionPropType','CfprStatsThr32ValuePropType','CfprStatsThr64DefinitionPropType','CfprStatsThr64ValuePropType','CfprStatsThrFloatDefinitionPropType','CfprStatsThrFloatValuePropType','CfprStatsThresholdDirection')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprStatsObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,73))
_CfprStatsCollectionPolicyTable_Object=MibTable
cfprStatsCollectionPolicyTable=_CfprStatsCollectionPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,73,1))
if mibBuilder.loadTexts:cfprStatsCollectionPolicyTable.setStatus(_A)
_CfprStatsCollectionPolicyEntry_Object=MibTableRow
cfprStatsCollectionPolicyEntry=_CfprStatsCollectionPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,73,1,1))
cfprStatsCollectionPolicyEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprStatsCollectionPolicyEntry.setStatus(_A)
_CfprStatsCollectionPolicyInstanceId_Type=CfprManagedObjectId
_CfprStatsCollectionPolicyInstanceId_Object=MibTableColumn
cfprStatsCollectionPolicyInstanceId=_CfprStatsCollectionPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,1),_CfprStatsCollectionPolicyInstanceId_Type())
cfprStatsCollectionPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyInstanceId.setStatus(_A)
_CfprStatsCollectionPolicyDn_Type=CfprManagedObjectDn
_CfprStatsCollectionPolicyDn_Object=MibTableColumn
cfprStatsCollectionPolicyDn=_CfprStatsCollectionPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,2),_CfprStatsCollectionPolicyDn_Type())
cfprStatsCollectionPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyDn.setStatus(_A)
_CfprStatsCollectionPolicyRn_Type=SnmpAdminString
_CfprStatsCollectionPolicyRn_Object=MibTableColumn
cfprStatsCollectionPolicyRn=_CfprStatsCollectionPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,3),_CfprStatsCollectionPolicyRn_Type())
cfprStatsCollectionPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyRn.setStatus(_A)
_CfprStatsCollectionPolicyCollectionInterval_Type=CfprStatsCollectionInterval
_CfprStatsCollectionPolicyCollectionInterval_Object=MibTableColumn
cfprStatsCollectionPolicyCollectionInterval=_CfprStatsCollectionPolicyCollectionInterval_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,4),_CfprStatsCollectionPolicyCollectionInterval_Type())
cfprStatsCollectionPolicyCollectionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyCollectionInterval.setStatus(_A)
_CfprStatsCollectionPolicyFsmDescr_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmDescr_Object=MibTableColumn
cfprStatsCollectionPolicyFsmDescr=_CfprStatsCollectionPolicyFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,5),_CfprStatsCollectionPolicyFsmDescr_Type())
cfprStatsCollectionPolicyFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmDescr.setStatus(_A)
_CfprStatsCollectionPolicyFsmPrev_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmPrev_Object=MibTableColumn
cfprStatsCollectionPolicyFsmPrev=_CfprStatsCollectionPolicyFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,6),_CfprStatsCollectionPolicyFsmPrev_Type())
cfprStatsCollectionPolicyFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmPrev.setStatus(_A)
_CfprStatsCollectionPolicyFsmProgr_Type=Gauge32
_CfprStatsCollectionPolicyFsmProgr_Object=MibTableColumn
cfprStatsCollectionPolicyFsmProgr=_CfprStatsCollectionPolicyFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,7),_CfprStatsCollectionPolicyFsmProgr_Type())
cfprStatsCollectionPolicyFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmProgr.setStatus(_A)
_CfprStatsCollectionPolicyFsmRmtInvErrCode_Type=Gauge32
_CfprStatsCollectionPolicyFsmRmtInvErrCode_Object=MibTableColumn
cfprStatsCollectionPolicyFsmRmtInvErrCode=_CfprStatsCollectionPolicyFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,8),_CfprStatsCollectionPolicyFsmRmtInvErrCode_Type())
cfprStatsCollectionPolicyFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmRmtInvErrCode.setStatus(_A)
_CfprStatsCollectionPolicyFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmRmtInvErrDescr_Object=MibTableColumn
cfprStatsCollectionPolicyFsmRmtInvErrDescr=_CfprStatsCollectionPolicyFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,9),_CfprStatsCollectionPolicyFsmRmtInvErrDescr_Type())
cfprStatsCollectionPolicyFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmRmtInvErrDescr.setStatus(_A)
_CfprStatsCollectionPolicyFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprStatsCollectionPolicyFsmRmtInvRslt_Object=MibTableColumn
cfprStatsCollectionPolicyFsmRmtInvRslt=_CfprStatsCollectionPolicyFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,10),_CfprStatsCollectionPolicyFsmRmtInvRslt_Type())
cfprStatsCollectionPolicyFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmRmtInvRslt.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageDescr_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmStageDescr_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageDescr=_CfprStatsCollectionPolicyFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,11),_CfprStatsCollectionPolicyFsmStageDescr_Type())
cfprStatsCollectionPolicyFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageDescr.setStatus(_A)
_CfprStatsCollectionPolicyFsmStamp_Type=DateAndTime
_CfprStatsCollectionPolicyFsmStamp_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStamp=_CfprStatsCollectionPolicyFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,12),_CfprStatsCollectionPolicyFsmStamp_Type())
cfprStatsCollectionPolicyFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStamp.setStatus(_A)
_CfprStatsCollectionPolicyFsmStatus_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmStatus_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStatus=_CfprStatsCollectionPolicyFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,13),_CfprStatsCollectionPolicyFsmStatus_Type())
cfprStatsCollectionPolicyFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStatus.setStatus(_A)
_CfprStatsCollectionPolicyFsmTry_Type=Gauge32
_CfprStatsCollectionPolicyFsmTry_Object=MibTableColumn
cfprStatsCollectionPolicyFsmTry=_CfprStatsCollectionPolicyFsmTry_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,14),_CfprStatsCollectionPolicyFsmTry_Type())
cfprStatsCollectionPolicyFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTry.setStatus(_A)
_CfprStatsCollectionPolicyId_Type=Gauge32
_CfprStatsCollectionPolicyId_Object=MibTableColumn
cfprStatsCollectionPolicyId=_CfprStatsCollectionPolicyId_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,15),_CfprStatsCollectionPolicyId_Type())
cfprStatsCollectionPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyId.setStatus(_A)
_CfprStatsCollectionPolicyName_Type=CfprStatsCollectionDomain
_CfprStatsCollectionPolicyName_Object=MibTableColumn
cfprStatsCollectionPolicyName=_CfprStatsCollectionPolicyName_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,16),_CfprStatsCollectionPolicyName_Type())
cfprStatsCollectionPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyName.setStatus(_A)
_CfprStatsCollectionPolicyReportingInterval_Type=CfprStatsReportingInterval
_CfprStatsCollectionPolicyReportingInterval_Object=MibTableColumn
cfprStatsCollectionPolicyReportingInterval=_CfprStatsCollectionPolicyReportingInterval_Object((1,3,6,1,4,1,9,9,826,1,73,1,1,17),_CfprStatsCollectionPolicyReportingInterval_Type())
cfprStatsCollectionPolicyReportingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyReportingInterval.setStatus(_A)
_CfprStatsCollectionPolicyFsmTable_Object=MibTable
cfprStatsCollectionPolicyFsmTable=_CfprStatsCollectionPolicyFsmTable_Object((1,3,6,1,4,1,9,9,826,1,73,2))
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTable.setStatus(_A)
_CfprStatsCollectionPolicyFsmEntry_Object=MibTableRow
cfprStatsCollectionPolicyFsmEntry=_CfprStatsCollectionPolicyFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,73,2,1))
cfprStatsCollectionPolicyFsmEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmEntry.setStatus(_A)
_CfprStatsCollectionPolicyFsmInstanceId_Type=CfprManagedObjectId
_CfprStatsCollectionPolicyFsmInstanceId_Object=MibTableColumn
cfprStatsCollectionPolicyFsmInstanceId=_CfprStatsCollectionPolicyFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,1),_CfprStatsCollectionPolicyFsmInstanceId_Type())
cfprStatsCollectionPolicyFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmInstanceId.setStatus(_A)
_CfprStatsCollectionPolicyFsmDn_Type=CfprManagedObjectDn
_CfprStatsCollectionPolicyFsmDn_Object=MibTableColumn
cfprStatsCollectionPolicyFsmDn=_CfprStatsCollectionPolicyFsmDn_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,2),_CfprStatsCollectionPolicyFsmDn_Type())
cfprStatsCollectionPolicyFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmDn.setStatus(_A)
_CfprStatsCollectionPolicyFsmRn_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmRn_Object=MibTableColumn
cfprStatsCollectionPolicyFsmRn=_CfprStatsCollectionPolicyFsmRn_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,3),_CfprStatsCollectionPolicyFsmRn_Type())
cfprStatsCollectionPolicyFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmRn.setStatus(_A)
_CfprStatsCollectionPolicyFsmCompletionTime_Type=DateAndTime
_CfprStatsCollectionPolicyFsmCompletionTime_Object=MibTableColumn
cfprStatsCollectionPolicyFsmCompletionTime=_CfprStatsCollectionPolicyFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,4),_CfprStatsCollectionPolicyFsmCompletionTime_Type())
cfprStatsCollectionPolicyFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmCompletionTime.setStatus(_A)
_CfprStatsCollectionPolicyFsmCurrentFsm_Type=CfprStatsCollectionPolicyFsmCurrentFsm
_CfprStatsCollectionPolicyFsmCurrentFsm_Object=MibTableColumn
cfprStatsCollectionPolicyFsmCurrentFsm=_CfprStatsCollectionPolicyFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,5),_CfprStatsCollectionPolicyFsmCurrentFsm_Type())
cfprStatsCollectionPolicyFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmCurrentFsm.setStatus(_A)
_CfprStatsCollectionPolicyFsmDescrData_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmDescrData_Object=MibTableColumn
cfprStatsCollectionPolicyFsmDescrData=_CfprStatsCollectionPolicyFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,6),_CfprStatsCollectionPolicyFsmDescrData_Type())
cfprStatsCollectionPolicyFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmDescrData.setStatus(_A)
_CfprStatsCollectionPolicyFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprStatsCollectionPolicyFsmFsmStatus_Object=MibTableColumn
cfprStatsCollectionPolicyFsmFsmStatus=_CfprStatsCollectionPolicyFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,7),_CfprStatsCollectionPolicyFsmFsmStatus_Type())
cfprStatsCollectionPolicyFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmFsmStatus.setStatus(_A)
_CfprStatsCollectionPolicyFsmProgress_Type=Gauge32
_CfprStatsCollectionPolicyFsmProgress_Object=MibTableColumn
cfprStatsCollectionPolicyFsmProgress=_CfprStatsCollectionPolicyFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,8),_CfprStatsCollectionPolicyFsmProgress_Type())
cfprStatsCollectionPolicyFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmProgress.setStatus(_A)
_CfprStatsCollectionPolicyFsmRmtErrCode_Type=Gauge32
_CfprStatsCollectionPolicyFsmRmtErrCode_Object=MibTableColumn
cfprStatsCollectionPolicyFsmRmtErrCode=_CfprStatsCollectionPolicyFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,9),_CfprStatsCollectionPolicyFsmRmtErrCode_Type())
cfprStatsCollectionPolicyFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmRmtErrCode.setStatus(_A)
_CfprStatsCollectionPolicyFsmRmtErrDescr_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmRmtErrDescr_Object=MibTableColumn
cfprStatsCollectionPolicyFsmRmtErrDescr=_CfprStatsCollectionPolicyFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,10),_CfprStatsCollectionPolicyFsmRmtErrDescr_Type())
cfprStatsCollectionPolicyFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmRmtErrDescr.setStatus(_A)
_CfprStatsCollectionPolicyFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprStatsCollectionPolicyFsmRmtRslt_Object=MibTableColumn
cfprStatsCollectionPolicyFsmRmtRslt=_CfprStatsCollectionPolicyFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,73,2,1,11),_CfprStatsCollectionPolicyFsmRmtRslt_Type())
cfprStatsCollectionPolicyFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmRmtRslt.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageTable_Object=MibTable
cfprStatsCollectionPolicyFsmStageTable=_CfprStatsCollectionPolicyFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,73,3))
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageTable.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageEntry_Object=MibTableRow
cfprStatsCollectionPolicyFsmStageEntry=_CfprStatsCollectionPolicyFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,73,3,1))
cfprStatsCollectionPolicyFsmStageEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageEntry.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageInstanceId_Type=CfprManagedObjectId
_CfprStatsCollectionPolicyFsmStageInstanceId_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageInstanceId=_CfprStatsCollectionPolicyFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,3,1,1),_CfprStatsCollectionPolicyFsmStageInstanceId_Type())
cfprStatsCollectionPolicyFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageInstanceId.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageDn_Type=CfprManagedObjectDn
_CfprStatsCollectionPolicyFsmStageDn_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageDn=_CfprStatsCollectionPolicyFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,73,3,1,2),_CfprStatsCollectionPolicyFsmStageDn_Type())
cfprStatsCollectionPolicyFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageDn.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageRn_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmStageRn_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageRn=_CfprStatsCollectionPolicyFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,73,3,1,3),_CfprStatsCollectionPolicyFsmStageRn_Type())
cfprStatsCollectionPolicyFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageRn.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageDescrData_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmStageDescrData_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageDescrData=_CfprStatsCollectionPolicyFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,73,3,1,4),_CfprStatsCollectionPolicyFsmStageDescrData_Type())
cfprStatsCollectionPolicyFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageDescrData.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageLastUpdateTime_Type=DateAndTime
_CfprStatsCollectionPolicyFsmStageLastUpdateTime_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageLastUpdateTime=_CfprStatsCollectionPolicyFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,73,3,1,5),_CfprStatsCollectionPolicyFsmStageLastUpdateTime_Type())
cfprStatsCollectionPolicyFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageLastUpdateTime.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageName_Type=CfprStatsCollectionPolicyFsmStageName
_CfprStatsCollectionPolicyFsmStageName_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageName=_CfprStatsCollectionPolicyFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,73,3,1,6),_CfprStatsCollectionPolicyFsmStageName_Type())
cfprStatsCollectionPolicyFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageName.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageOrder_Type=Gauge32
_CfprStatsCollectionPolicyFsmStageOrder_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageOrder=_CfprStatsCollectionPolicyFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,73,3,1,7),_CfprStatsCollectionPolicyFsmStageOrder_Type())
cfprStatsCollectionPolicyFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageOrder.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageRetry_Type=Gauge32
_CfprStatsCollectionPolicyFsmStageRetry_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageRetry=_CfprStatsCollectionPolicyFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,73,3,1,8),_CfprStatsCollectionPolicyFsmStageRetry_Type())
cfprStatsCollectionPolicyFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageRetry.setStatus(_A)
_CfprStatsCollectionPolicyFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprStatsCollectionPolicyFsmStageStageStatus_Object=MibTableColumn
cfprStatsCollectionPolicyFsmStageStageStatus=_CfprStatsCollectionPolicyFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,73,3,1,9),_CfprStatsCollectionPolicyFsmStageStageStatus_Type())
cfprStatsCollectionPolicyFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmStageStageStatus.setStatus(_A)
_CfprStatsCollectionPolicyFsmTaskTable_Object=MibTable
cfprStatsCollectionPolicyFsmTaskTable=_CfprStatsCollectionPolicyFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,73,4))
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTaskTable.setStatus(_A)
_CfprStatsCollectionPolicyFsmTaskEntry_Object=MibTableRow
cfprStatsCollectionPolicyFsmTaskEntry=_CfprStatsCollectionPolicyFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,73,4,1))
cfprStatsCollectionPolicyFsmTaskEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTaskEntry.setStatus(_A)
_CfprStatsCollectionPolicyFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprStatsCollectionPolicyFsmTaskInstanceId_Object=MibTableColumn
cfprStatsCollectionPolicyFsmTaskInstanceId=_CfprStatsCollectionPolicyFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,4,1,1),_CfprStatsCollectionPolicyFsmTaskInstanceId_Type())
cfprStatsCollectionPolicyFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTaskInstanceId.setStatus(_A)
_CfprStatsCollectionPolicyFsmTaskDn_Type=CfprManagedObjectDn
_CfprStatsCollectionPolicyFsmTaskDn_Object=MibTableColumn
cfprStatsCollectionPolicyFsmTaskDn=_CfprStatsCollectionPolicyFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,73,4,1,2),_CfprStatsCollectionPolicyFsmTaskDn_Type())
cfprStatsCollectionPolicyFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTaskDn.setStatus(_A)
_CfprStatsCollectionPolicyFsmTaskRn_Type=SnmpAdminString
_CfprStatsCollectionPolicyFsmTaskRn_Object=MibTableColumn
cfprStatsCollectionPolicyFsmTaskRn=_CfprStatsCollectionPolicyFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,73,4,1,3),_CfprStatsCollectionPolicyFsmTaskRn_Type())
cfprStatsCollectionPolicyFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTaskRn.setStatus(_A)
_CfprStatsCollectionPolicyFsmTaskCompletion_Type=CfprFsmCompletion
_CfprStatsCollectionPolicyFsmTaskCompletion_Object=MibTableColumn
cfprStatsCollectionPolicyFsmTaskCompletion=_CfprStatsCollectionPolicyFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,73,4,1,4),_CfprStatsCollectionPolicyFsmTaskCompletion_Type())
cfprStatsCollectionPolicyFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTaskCompletion.setStatus(_A)
_CfprStatsCollectionPolicyFsmTaskFlags_Type=CfprFsmFlags
_CfprStatsCollectionPolicyFsmTaskFlags_Object=MibTableColumn
cfprStatsCollectionPolicyFsmTaskFlags=_CfprStatsCollectionPolicyFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,73,4,1,5),_CfprStatsCollectionPolicyFsmTaskFlags_Type())
cfprStatsCollectionPolicyFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTaskFlags.setStatus(_A)
_CfprStatsCollectionPolicyFsmTaskItem_Type=CfprStatsCollectionPolicyFsmTaskItem
_CfprStatsCollectionPolicyFsmTaskItem_Object=MibTableColumn
cfprStatsCollectionPolicyFsmTaskItem=_CfprStatsCollectionPolicyFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,73,4,1,6),_CfprStatsCollectionPolicyFsmTaskItem_Type())
cfprStatsCollectionPolicyFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTaskItem.setStatus(_A)
_CfprStatsCollectionPolicyFsmTaskSeqId_Type=Gauge32
_CfprStatsCollectionPolicyFsmTaskSeqId_Object=MibTableColumn
cfprStatsCollectionPolicyFsmTaskSeqId=_CfprStatsCollectionPolicyFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,73,4,1,7),_CfprStatsCollectionPolicyFsmTaskSeqId_Type())
cfprStatsCollectionPolicyFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsCollectionPolicyFsmTaskSeqId.setStatus(_A)
_CfprStatsHolderTable_Object=MibTable
cfprStatsHolderTable=_CfprStatsHolderTable_Object((1,3,6,1,4,1,9,9,826,1,73,5))
if mibBuilder.loadTexts:cfprStatsHolderTable.setStatus(_A)
_CfprStatsHolderEntry_Object=MibTableRow
cfprStatsHolderEntry=_CfprStatsHolderEntry_Object((1,3,6,1,4,1,9,9,826,1,73,5,1))
cfprStatsHolderEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprStatsHolderEntry.setStatus(_A)
_CfprStatsHolderInstanceId_Type=CfprManagedObjectId
_CfprStatsHolderInstanceId_Object=MibTableColumn
cfprStatsHolderInstanceId=_CfprStatsHolderInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,5,1,1),_CfprStatsHolderInstanceId_Type())
cfprStatsHolderInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsHolderInstanceId.setStatus(_A)
_CfprStatsHolderDn_Type=CfprManagedObjectDn
_CfprStatsHolderDn_Object=MibTableColumn
cfprStatsHolderDn=_CfprStatsHolderDn_Object((1,3,6,1,4,1,9,9,826,1,73,5,1,2),_CfprStatsHolderDn_Type())
cfprStatsHolderDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsHolderDn.setStatus(_A)
_CfprStatsHolderRn_Type=SnmpAdminString
_CfprStatsHolderRn_Object=MibTableColumn
cfprStatsHolderRn=_CfprStatsHolderRn_Object((1,3,6,1,4,1,9,9,826,1,73,5,1,3),_CfprStatsHolderRn_Type())
cfprStatsHolderRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsHolderRn.setStatus(_A)
_CfprStatsHolderName_Type=SnmpAdminString
_CfprStatsHolderName_Object=MibTableColumn
cfprStatsHolderName=_CfprStatsHolderName_Object((1,3,6,1,4,1,9,9,826,1,73,5,1,4),_CfprStatsHolderName_Type())
cfprStatsHolderName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsHolderName.setStatus(_A)
_CfprStatsThr32DefinitionTable_Object=MibTable
cfprStatsThr32DefinitionTable=_CfprStatsThr32DefinitionTable_Object((1,3,6,1,4,1,9,9,826,1,73,6))
if mibBuilder.loadTexts:cfprStatsThr32DefinitionTable.setStatus(_A)
_CfprStatsThr32DefinitionEntry_Object=MibTableRow
cfprStatsThr32DefinitionEntry=_CfprStatsThr32DefinitionEntry_Object((1,3,6,1,4,1,9,9,826,1,73,6,1))
cfprStatsThr32DefinitionEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprStatsThr32DefinitionEntry.setStatus(_A)
_CfprStatsThr32DefinitionInstanceId_Type=CfprManagedObjectId
_CfprStatsThr32DefinitionInstanceId_Object=MibTableColumn
cfprStatsThr32DefinitionInstanceId=_CfprStatsThr32DefinitionInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,1),_CfprStatsThr32DefinitionInstanceId_Type())
cfprStatsThr32DefinitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionInstanceId.setStatus(_A)
_CfprStatsThr32DefinitionDn_Type=CfprManagedObjectDn
_CfprStatsThr32DefinitionDn_Object=MibTableColumn
cfprStatsThr32DefinitionDn=_CfprStatsThr32DefinitionDn_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,2),_CfprStatsThr32DefinitionDn_Type())
cfprStatsThr32DefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionDn.setStatus(_A)
_CfprStatsThr32DefinitionRn_Type=SnmpAdminString
_CfprStatsThr32DefinitionRn_Object=MibTableColumn
cfprStatsThr32DefinitionRn=_CfprStatsThr32DefinitionRn_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,3),_CfprStatsThr32DefinitionRn_Type())
cfprStatsThr32DefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionRn.setStatus(_A)
_CfprStatsThr32DefinitionDescr_Type=SnmpAdminString
_CfprStatsThr32DefinitionDescr_Object=MibTableColumn
cfprStatsThr32DefinitionDescr=_CfprStatsThr32DefinitionDescr_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,4),_CfprStatsThr32DefinitionDescr_Type())
cfprStatsThr32DefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionDescr.setStatus(_A)
_CfprStatsThr32DefinitionIntId_Type=SnmpAdminString
_CfprStatsThr32DefinitionIntId_Object=MibTableColumn
cfprStatsThr32DefinitionIntId=_CfprStatsThr32DefinitionIntId_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,5),_CfprStatsThr32DefinitionIntId_Type())
cfprStatsThr32DefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionIntId.setStatus(_A)
_CfprStatsThr32DefinitionName_Type=SnmpAdminString
_CfprStatsThr32DefinitionName_Object=MibTableColumn
cfprStatsThr32DefinitionName=_CfprStatsThr32DefinitionName_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,6),_CfprStatsThr32DefinitionName_Type())
cfprStatsThr32DefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionName.setStatus(_A)
_CfprStatsThr32DefinitionNormalValue_Type=Gauge32
_CfprStatsThr32DefinitionNormalValue_Object=MibTableColumn
cfprStatsThr32DefinitionNormalValue=_CfprStatsThr32DefinitionNormalValue_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,7),_CfprStatsThr32DefinitionNormalValue_Type())
cfprStatsThr32DefinitionNormalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionNormalValue.setStatus(_A)
_CfprStatsThr32DefinitionPolicyLevel_Type=Gauge32
_CfprStatsThr32DefinitionPolicyLevel_Object=MibTableColumn
cfprStatsThr32DefinitionPolicyLevel=_CfprStatsThr32DefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,8),_CfprStatsThr32DefinitionPolicyLevel_Type())
cfprStatsThr32DefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionPolicyLevel.setStatus(_A)
_CfprStatsThr32DefinitionPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStatsThr32DefinitionPolicyOwner_Object=MibTableColumn
cfprStatsThr32DefinitionPolicyOwner=_CfprStatsThr32DefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,9),_CfprStatsThr32DefinitionPolicyOwner_Type())
cfprStatsThr32DefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionPolicyOwner.setStatus(_A)
_CfprStatsThr32DefinitionPropId_Type=SnmpAdminString
_CfprStatsThr32DefinitionPropId_Object=MibTableColumn
cfprStatsThr32DefinitionPropId=_CfprStatsThr32DefinitionPropId_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,10),_CfprStatsThr32DefinitionPropId_Type())
cfprStatsThr32DefinitionPropId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionPropId.setStatus(_A)
_CfprStatsThr32DefinitionPropType_Type=CfprStatsThr32DefinitionPropType
_CfprStatsThr32DefinitionPropType_Object=MibTableColumn
cfprStatsThr32DefinitionPropType=_CfprStatsThr32DefinitionPropType_Object((1,3,6,1,4,1,9,9,826,1,73,6,1,11),_CfprStatsThr32DefinitionPropType_Type())
cfprStatsThr32DefinitionPropType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32DefinitionPropType.setStatus(_A)
_CfprStatsThr32ValueTable_Object=MibTable
cfprStatsThr32ValueTable=_CfprStatsThr32ValueTable_Object((1,3,6,1,4,1,9,9,826,1,73,7))
if mibBuilder.loadTexts:cfprStatsThr32ValueTable.setStatus(_A)
_CfprStatsThr32ValueEntry_Object=MibTableRow
cfprStatsThr32ValueEntry=_CfprStatsThr32ValueEntry_Object((1,3,6,1,4,1,9,9,826,1,73,7,1))
cfprStatsThr32ValueEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprStatsThr32ValueEntry.setStatus(_A)
_CfprStatsThr32ValueInstanceId_Type=CfprManagedObjectId
_CfprStatsThr32ValueInstanceId_Object=MibTableColumn
cfprStatsThr32ValueInstanceId=_CfprStatsThr32ValueInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,1),_CfprStatsThr32ValueInstanceId_Type())
cfprStatsThr32ValueInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsThr32ValueInstanceId.setStatus(_A)
_CfprStatsThr32ValueDn_Type=CfprManagedObjectDn
_CfprStatsThr32ValueDn_Object=MibTableColumn
cfprStatsThr32ValueDn=_CfprStatsThr32ValueDn_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,2),_CfprStatsThr32ValueDn_Type())
cfprStatsThr32ValueDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValueDn.setStatus(_A)
_CfprStatsThr32ValueRn_Type=SnmpAdminString
_CfprStatsThr32ValueRn_Object=MibTableColumn
cfprStatsThr32ValueRn=_CfprStatsThr32ValueRn_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,3),_CfprStatsThr32ValueRn_Type())
cfprStatsThr32ValueRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValueRn.setStatus(_A)
_CfprStatsThr32ValueDeescalating_Type=Gauge32
_CfprStatsThr32ValueDeescalating_Object=MibTableColumn
cfprStatsThr32ValueDeescalating=_CfprStatsThr32ValueDeescalating_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,4),_CfprStatsThr32ValueDeescalating_Type())
cfprStatsThr32ValueDeescalating.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValueDeescalating.setStatus(_A)
_CfprStatsThr32ValueDescr_Type=SnmpAdminString
_CfprStatsThr32ValueDescr_Object=MibTableColumn
cfprStatsThr32ValueDescr=_CfprStatsThr32ValueDescr_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,5),_CfprStatsThr32ValueDescr_Type())
cfprStatsThr32ValueDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValueDescr.setStatus(_A)
_CfprStatsThr32ValueDirection_Type=CfprStatsThresholdDirection
_CfprStatsThr32ValueDirection_Object=MibTableColumn
cfprStatsThr32ValueDirection=_CfprStatsThr32ValueDirection_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,6),_CfprStatsThr32ValueDirection_Type())
cfprStatsThr32ValueDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValueDirection.setStatus(_A)
_CfprStatsThr32ValueEscalating_Type=Gauge32
_CfprStatsThr32ValueEscalating_Object=MibTableColumn
cfprStatsThr32ValueEscalating=_CfprStatsThr32ValueEscalating_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,7),_CfprStatsThr32ValueEscalating_Type())
cfprStatsThr32ValueEscalating.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValueEscalating.setStatus(_A)
_CfprStatsThr32ValueIntId_Type=SnmpAdminString
_CfprStatsThr32ValueIntId_Object=MibTableColumn
cfprStatsThr32ValueIntId=_CfprStatsThr32ValueIntId_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,8),_CfprStatsThr32ValueIntId_Type())
cfprStatsThr32ValueIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValueIntId.setStatus(_A)
_CfprStatsThr32ValueName_Type=SnmpAdminString
_CfprStatsThr32ValueName_Object=MibTableColumn
cfprStatsThr32ValueName=_CfprStatsThr32ValueName_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,9),_CfprStatsThr32ValueName_Type())
cfprStatsThr32ValueName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValueName.setStatus(_A)
_CfprStatsThr32ValuePolicyLevel_Type=Gauge32
_CfprStatsThr32ValuePolicyLevel_Object=MibTableColumn
cfprStatsThr32ValuePolicyLevel=_CfprStatsThr32ValuePolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,10),_CfprStatsThr32ValuePolicyLevel_Type())
cfprStatsThr32ValuePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValuePolicyLevel.setStatus(_A)
_CfprStatsThr32ValuePolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStatsThr32ValuePolicyOwner_Object=MibTableColumn
cfprStatsThr32ValuePolicyOwner=_CfprStatsThr32ValuePolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,11),_CfprStatsThr32ValuePolicyOwner_Type())
cfprStatsThr32ValuePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValuePolicyOwner.setStatus(_A)
_CfprStatsThr32ValuePropType_Type=CfprStatsThr32ValuePropType
_CfprStatsThr32ValuePropType_Object=MibTableColumn
cfprStatsThr32ValuePropType=_CfprStatsThr32ValuePropType_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,12),_CfprStatsThr32ValuePropType_Type())
cfprStatsThr32ValuePropType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValuePropType.setStatus(_A)
_CfprStatsThr32ValueSeverity_Type=CfprConditionSeverity
_CfprStatsThr32ValueSeverity_Object=MibTableColumn
cfprStatsThr32ValueSeverity=_CfprStatsThr32ValueSeverity_Object((1,3,6,1,4,1,9,9,826,1,73,7,1,13),_CfprStatsThr32ValueSeverity_Type())
cfprStatsThr32ValueSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr32ValueSeverity.setStatus(_A)
_CfprStatsThr64DefinitionTable_Object=MibTable
cfprStatsThr64DefinitionTable=_CfprStatsThr64DefinitionTable_Object((1,3,6,1,4,1,9,9,826,1,73,8))
if mibBuilder.loadTexts:cfprStatsThr64DefinitionTable.setStatus(_A)
_CfprStatsThr64DefinitionEntry_Object=MibTableRow
cfprStatsThr64DefinitionEntry=_CfprStatsThr64DefinitionEntry_Object((1,3,6,1,4,1,9,9,826,1,73,8,1))
cfprStatsThr64DefinitionEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprStatsThr64DefinitionEntry.setStatus(_A)
_CfprStatsThr64DefinitionInstanceId_Type=CfprManagedObjectId
_CfprStatsThr64DefinitionInstanceId_Object=MibTableColumn
cfprStatsThr64DefinitionInstanceId=_CfprStatsThr64DefinitionInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,1),_CfprStatsThr64DefinitionInstanceId_Type())
cfprStatsThr64DefinitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionInstanceId.setStatus(_A)
_CfprStatsThr64DefinitionDn_Type=CfprManagedObjectDn
_CfprStatsThr64DefinitionDn_Object=MibTableColumn
cfprStatsThr64DefinitionDn=_CfprStatsThr64DefinitionDn_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,2),_CfprStatsThr64DefinitionDn_Type())
cfprStatsThr64DefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionDn.setStatus(_A)
_CfprStatsThr64DefinitionRn_Type=SnmpAdminString
_CfprStatsThr64DefinitionRn_Object=MibTableColumn
cfprStatsThr64DefinitionRn=_CfprStatsThr64DefinitionRn_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,3),_CfprStatsThr64DefinitionRn_Type())
cfprStatsThr64DefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionRn.setStatus(_A)
_CfprStatsThr64DefinitionDescr_Type=SnmpAdminString
_CfprStatsThr64DefinitionDescr_Object=MibTableColumn
cfprStatsThr64DefinitionDescr=_CfprStatsThr64DefinitionDescr_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,4),_CfprStatsThr64DefinitionDescr_Type())
cfprStatsThr64DefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionDescr.setStatus(_A)
_CfprStatsThr64DefinitionIntId_Type=SnmpAdminString
_CfprStatsThr64DefinitionIntId_Object=MibTableColumn
cfprStatsThr64DefinitionIntId=_CfprStatsThr64DefinitionIntId_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,5),_CfprStatsThr64DefinitionIntId_Type())
cfprStatsThr64DefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionIntId.setStatus(_A)
_CfprStatsThr64DefinitionName_Type=SnmpAdminString
_CfprStatsThr64DefinitionName_Object=MibTableColumn
cfprStatsThr64DefinitionName=_CfprStatsThr64DefinitionName_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,6),_CfprStatsThr64DefinitionName_Type())
cfprStatsThr64DefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionName.setStatus(_A)
_CfprStatsThr64DefinitionNormalValue_Type=Unsigned64
_CfprStatsThr64DefinitionNormalValue_Object=MibTableColumn
cfprStatsThr64DefinitionNormalValue=_CfprStatsThr64DefinitionNormalValue_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,7),_CfprStatsThr64DefinitionNormalValue_Type())
cfprStatsThr64DefinitionNormalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionNormalValue.setStatus(_A)
_CfprStatsThr64DefinitionPolicyLevel_Type=Gauge32
_CfprStatsThr64DefinitionPolicyLevel_Object=MibTableColumn
cfprStatsThr64DefinitionPolicyLevel=_CfprStatsThr64DefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,8),_CfprStatsThr64DefinitionPolicyLevel_Type())
cfprStatsThr64DefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionPolicyLevel.setStatus(_A)
_CfprStatsThr64DefinitionPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStatsThr64DefinitionPolicyOwner_Object=MibTableColumn
cfprStatsThr64DefinitionPolicyOwner=_CfprStatsThr64DefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,9),_CfprStatsThr64DefinitionPolicyOwner_Type())
cfprStatsThr64DefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionPolicyOwner.setStatus(_A)
_CfprStatsThr64DefinitionPropId_Type=SnmpAdminString
_CfprStatsThr64DefinitionPropId_Object=MibTableColumn
cfprStatsThr64DefinitionPropId=_CfprStatsThr64DefinitionPropId_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,10),_CfprStatsThr64DefinitionPropId_Type())
cfprStatsThr64DefinitionPropId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionPropId.setStatus(_A)
_CfprStatsThr64DefinitionPropType_Type=CfprStatsThr64DefinitionPropType
_CfprStatsThr64DefinitionPropType_Object=MibTableColumn
cfprStatsThr64DefinitionPropType=_CfprStatsThr64DefinitionPropType_Object((1,3,6,1,4,1,9,9,826,1,73,8,1,11),_CfprStatsThr64DefinitionPropType_Type())
cfprStatsThr64DefinitionPropType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64DefinitionPropType.setStatus(_A)
_CfprStatsThr64ValueTable_Object=MibTable
cfprStatsThr64ValueTable=_CfprStatsThr64ValueTable_Object((1,3,6,1,4,1,9,9,826,1,73,9))
if mibBuilder.loadTexts:cfprStatsThr64ValueTable.setStatus(_A)
_CfprStatsThr64ValueEntry_Object=MibTableRow
cfprStatsThr64ValueEntry=_CfprStatsThr64ValueEntry_Object((1,3,6,1,4,1,9,9,826,1,73,9,1))
cfprStatsThr64ValueEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprStatsThr64ValueEntry.setStatus(_A)
_CfprStatsThr64ValueInstanceId_Type=CfprManagedObjectId
_CfprStatsThr64ValueInstanceId_Object=MibTableColumn
cfprStatsThr64ValueInstanceId=_CfprStatsThr64ValueInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,1),_CfprStatsThr64ValueInstanceId_Type())
cfprStatsThr64ValueInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsThr64ValueInstanceId.setStatus(_A)
_CfprStatsThr64ValueDn_Type=CfprManagedObjectDn
_CfprStatsThr64ValueDn_Object=MibTableColumn
cfprStatsThr64ValueDn=_CfprStatsThr64ValueDn_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,2),_CfprStatsThr64ValueDn_Type())
cfprStatsThr64ValueDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValueDn.setStatus(_A)
_CfprStatsThr64ValueRn_Type=SnmpAdminString
_CfprStatsThr64ValueRn_Object=MibTableColumn
cfprStatsThr64ValueRn=_CfprStatsThr64ValueRn_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,3),_CfprStatsThr64ValueRn_Type())
cfprStatsThr64ValueRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValueRn.setStatus(_A)
_CfprStatsThr64ValueDeescalating_Type=Unsigned64
_CfprStatsThr64ValueDeescalating_Object=MibTableColumn
cfprStatsThr64ValueDeescalating=_CfprStatsThr64ValueDeescalating_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,4),_CfprStatsThr64ValueDeescalating_Type())
cfprStatsThr64ValueDeescalating.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValueDeescalating.setStatus(_A)
_CfprStatsThr64ValueDescr_Type=SnmpAdminString
_CfprStatsThr64ValueDescr_Object=MibTableColumn
cfprStatsThr64ValueDescr=_CfprStatsThr64ValueDescr_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,5),_CfprStatsThr64ValueDescr_Type())
cfprStatsThr64ValueDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValueDescr.setStatus(_A)
_CfprStatsThr64ValueDirection_Type=CfprStatsThresholdDirection
_CfprStatsThr64ValueDirection_Object=MibTableColumn
cfprStatsThr64ValueDirection=_CfprStatsThr64ValueDirection_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,6),_CfprStatsThr64ValueDirection_Type())
cfprStatsThr64ValueDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValueDirection.setStatus(_A)
_CfprStatsThr64ValueEscalating_Type=Unsigned64
_CfprStatsThr64ValueEscalating_Object=MibTableColumn
cfprStatsThr64ValueEscalating=_CfprStatsThr64ValueEscalating_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,7),_CfprStatsThr64ValueEscalating_Type())
cfprStatsThr64ValueEscalating.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValueEscalating.setStatus(_A)
_CfprStatsThr64ValueIntId_Type=SnmpAdminString
_CfprStatsThr64ValueIntId_Object=MibTableColumn
cfprStatsThr64ValueIntId=_CfprStatsThr64ValueIntId_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,8),_CfprStatsThr64ValueIntId_Type())
cfprStatsThr64ValueIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValueIntId.setStatus(_A)
_CfprStatsThr64ValueName_Type=SnmpAdminString
_CfprStatsThr64ValueName_Object=MibTableColumn
cfprStatsThr64ValueName=_CfprStatsThr64ValueName_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,9),_CfprStatsThr64ValueName_Type())
cfprStatsThr64ValueName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValueName.setStatus(_A)
_CfprStatsThr64ValuePolicyLevel_Type=Gauge32
_CfprStatsThr64ValuePolicyLevel_Object=MibTableColumn
cfprStatsThr64ValuePolicyLevel=_CfprStatsThr64ValuePolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,10),_CfprStatsThr64ValuePolicyLevel_Type())
cfprStatsThr64ValuePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValuePolicyLevel.setStatus(_A)
_CfprStatsThr64ValuePolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStatsThr64ValuePolicyOwner_Object=MibTableColumn
cfprStatsThr64ValuePolicyOwner=_CfprStatsThr64ValuePolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,11),_CfprStatsThr64ValuePolicyOwner_Type())
cfprStatsThr64ValuePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValuePolicyOwner.setStatus(_A)
_CfprStatsThr64ValuePropType_Type=CfprStatsThr64ValuePropType
_CfprStatsThr64ValuePropType_Object=MibTableColumn
cfprStatsThr64ValuePropType=_CfprStatsThr64ValuePropType_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,12),_CfprStatsThr64ValuePropType_Type())
cfprStatsThr64ValuePropType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValuePropType.setStatus(_A)
_CfprStatsThr64ValueSeverity_Type=CfprConditionSeverity
_CfprStatsThr64ValueSeverity_Object=MibTableColumn
cfprStatsThr64ValueSeverity=_CfprStatsThr64ValueSeverity_Object((1,3,6,1,4,1,9,9,826,1,73,9,1,13),_CfprStatsThr64ValueSeverity_Type())
cfprStatsThr64ValueSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThr64ValueSeverity.setStatus(_A)
_CfprStatsThrFloatDefinitionTable_Object=MibTable
cfprStatsThrFloatDefinitionTable=_CfprStatsThrFloatDefinitionTable_Object((1,3,6,1,4,1,9,9,826,1,73,10))
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionTable.setStatus(_A)
_CfprStatsThrFloatDefinitionEntry_Object=MibTableRow
cfprStatsThrFloatDefinitionEntry=_CfprStatsThrFloatDefinitionEntry_Object((1,3,6,1,4,1,9,9,826,1,73,10,1))
cfprStatsThrFloatDefinitionEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionEntry.setStatus(_A)
_CfprStatsThrFloatDefinitionInstanceId_Type=CfprManagedObjectId
_CfprStatsThrFloatDefinitionInstanceId_Object=MibTableColumn
cfprStatsThrFloatDefinitionInstanceId=_CfprStatsThrFloatDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,1),_CfprStatsThrFloatDefinitionInstanceId_Type())
cfprStatsThrFloatDefinitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionInstanceId.setStatus(_A)
_CfprStatsThrFloatDefinitionDn_Type=CfprManagedObjectDn
_CfprStatsThrFloatDefinitionDn_Object=MibTableColumn
cfprStatsThrFloatDefinitionDn=_CfprStatsThrFloatDefinitionDn_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,2),_CfprStatsThrFloatDefinitionDn_Type())
cfprStatsThrFloatDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionDn.setStatus(_A)
_CfprStatsThrFloatDefinitionRn_Type=SnmpAdminString
_CfprStatsThrFloatDefinitionRn_Object=MibTableColumn
cfprStatsThrFloatDefinitionRn=_CfprStatsThrFloatDefinitionRn_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,3),_CfprStatsThrFloatDefinitionRn_Type())
cfprStatsThrFloatDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionRn.setStatus(_A)
_CfprStatsThrFloatDefinitionDescr_Type=SnmpAdminString
_CfprStatsThrFloatDefinitionDescr_Object=MibTableColumn
cfprStatsThrFloatDefinitionDescr=_CfprStatsThrFloatDefinitionDescr_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,4),_CfprStatsThrFloatDefinitionDescr_Type())
cfprStatsThrFloatDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionDescr.setStatus(_A)
_CfprStatsThrFloatDefinitionIntId_Type=SnmpAdminString
_CfprStatsThrFloatDefinitionIntId_Object=MibTableColumn
cfprStatsThrFloatDefinitionIntId=_CfprStatsThrFloatDefinitionIntId_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,5),_CfprStatsThrFloatDefinitionIntId_Type())
cfprStatsThrFloatDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionIntId.setStatus(_A)
_CfprStatsThrFloatDefinitionName_Type=SnmpAdminString
_CfprStatsThrFloatDefinitionName_Object=MibTableColumn
cfprStatsThrFloatDefinitionName=_CfprStatsThrFloatDefinitionName_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,6),_CfprStatsThrFloatDefinitionName_Type())
cfprStatsThrFloatDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionName.setStatus(_A)
_CfprStatsThrFloatDefinitionNormalValue_Type=Integer32
_CfprStatsThrFloatDefinitionNormalValue_Object=MibTableColumn
cfprStatsThrFloatDefinitionNormalValue=_CfprStatsThrFloatDefinitionNormalValue_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,7),_CfprStatsThrFloatDefinitionNormalValue_Type())
cfprStatsThrFloatDefinitionNormalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionNormalValue.setStatus(_A)
_CfprStatsThrFloatDefinitionPolicyLevel_Type=Gauge32
_CfprStatsThrFloatDefinitionPolicyLevel_Object=MibTableColumn
cfprStatsThrFloatDefinitionPolicyLevel=_CfprStatsThrFloatDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,8),_CfprStatsThrFloatDefinitionPolicyLevel_Type())
cfprStatsThrFloatDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionPolicyLevel.setStatus(_A)
_CfprStatsThrFloatDefinitionPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStatsThrFloatDefinitionPolicyOwner_Object=MibTableColumn
cfprStatsThrFloatDefinitionPolicyOwner=_CfprStatsThrFloatDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,9),_CfprStatsThrFloatDefinitionPolicyOwner_Type())
cfprStatsThrFloatDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionPolicyOwner.setStatus(_A)
_CfprStatsThrFloatDefinitionPropId_Type=SnmpAdminString
_CfprStatsThrFloatDefinitionPropId_Object=MibTableColumn
cfprStatsThrFloatDefinitionPropId=_CfprStatsThrFloatDefinitionPropId_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,10),_CfprStatsThrFloatDefinitionPropId_Type())
cfprStatsThrFloatDefinitionPropId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionPropId.setStatus(_A)
_CfprStatsThrFloatDefinitionPropType_Type=CfprStatsThrFloatDefinitionPropType
_CfprStatsThrFloatDefinitionPropType_Object=MibTableColumn
cfprStatsThrFloatDefinitionPropType=_CfprStatsThrFloatDefinitionPropType_Object((1,3,6,1,4,1,9,9,826,1,73,10,1,11),_CfprStatsThrFloatDefinitionPropType_Type())
cfprStatsThrFloatDefinitionPropType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatDefinitionPropType.setStatus(_A)
_CfprStatsThrFloatValueTable_Object=MibTable
cfprStatsThrFloatValueTable=_CfprStatsThrFloatValueTable_Object((1,3,6,1,4,1,9,9,826,1,73,11))
if mibBuilder.loadTexts:cfprStatsThrFloatValueTable.setStatus(_A)
_CfprStatsThrFloatValueEntry_Object=MibTableRow
cfprStatsThrFloatValueEntry=_CfprStatsThrFloatValueEntry_Object((1,3,6,1,4,1,9,9,826,1,73,11,1))
cfprStatsThrFloatValueEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cfprStatsThrFloatValueEntry.setStatus(_A)
_CfprStatsThrFloatValueInstanceId_Type=CfprManagedObjectId
_CfprStatsThrFloatValueInstanceId_Object=MibTableColumn
cfprStatsThrFloatValueInstanceId=_CfprStatsThrFloatValueInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,1),_CfprStatsThrFloatValueInstanceId_Type())
cfprStatsThrFloatValueInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsThrFloatValueInstanceId.setStatus(_A)
_CfprStatsThrFloatValueDn_Type=CfprManagedObjectDn
_CfprStatsThrFloatValueDn_Object=MibTableColumn
cfprStatsThrFloatValueDn=_CfprStatsThrFloatValueDn_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,2),_CfprStatsThrFloatValueDn_Type())
cfprStatsThrFloatValueDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValueDn.setStatus(_A)
_CfprStatsThrFloatValueRn_Type=SnmpAdminString
_CfprStatsThrFloatValueRn_Object=MibTableColumn
cfprStatsThrFloatValueRn=_CfprStatsThrFloatValueRn_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,3),_CfprStatsThrFloatValueRn_Type())
cfprStatsThrFloatValueRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValueRn.setStatus(_A)
_CfprStatsThrFloatValueDeescalating_Type=Integer32
_CfprStatsThrFloatValueDeescalating_Object=MibTableColumn
cfprStatsThrFloatValueDeescalating=_CfprStatsThrFloatValueDeescalating_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,4),_CfprStatsThrFloatValueDeescalating_Type())
cfprStatsThrFloatValueDeescalating.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValueDeescalating.setStatus(_A)
_CfprStatsThrFloatValueDescr_Type=SnmpAdminString
_CfprStatsThrFloatValueDescr_Object=MibTableColumn
cfprStatsThrFloatValueDescr=_CfprStatsThrFloatValueDescr_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,5),_CfprStatsThrFloatValueDescr_Type())
cfprStatsThrFloatValueDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValueDescr.setStatus(_A)
_CfprStatsThrFloatValueDirection_Type=CfprStatsThresholdDirection
_CfprStatsThrFloatValueDirection_Object=MibTableColumn
cfprStatsThrFloatValueDirection=_CfprStatsThrFloatValueDirection_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,6),_CfprStatsThrFloatValueDirection_Type())
cfprStatsThrFloatValueDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValueDirection.setStatus(_A)
_CfprStatsThrFloatValueEscalating_Type=Integer32
_CfprStatsThrFloatValueEscalating_Object=MibTableColumn
cfprStatsThrFloatValueEscalating=_CfprStatsThrFloatValueEscalating_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,7),_CfprStatsThrFloatValueEscalating_Type())
cfprStatsThrFloatValueEscalating.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValueEscalating.setStatus(_A)
_CfprStatsThrFloatValueIntId_Type=SnmpAdminString
_CfprStatsThrFloatValueIntId_Object=MibTableColumn
cfprStatsThrFloatValueIntId=_CfprStatsThrFloatValueIntId_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,8),_CfprStatsThrFloatValueIntId_Type())
cfprStatsThrFloatValueIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValueIntId.setStatus(_A)
_CfprStatsThrFloatValueName_Type=SnmpAdminString
_CfprStatsThrFloatValueName_Object=MibTableColumn
cfprStatsThrFloatValueName=_CfprStatsThrFloatValueName_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,9),_CfprStatsThrFloatValueName_Type())
cfprStatsThrFloatValueName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValueName.setStatus(_A)
_CfprStatsThrFloatValuePolicyLevel_Type=Gauge32
_CfprStatsThrFloatValuePolicyLevel_Object=MibTableColumn
cfprStatsThrFloatValuePolicyLevel=_CfprStatsThrFloatValuePolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,10),_CfprStatsThrFloatValuePolicyLevel_Type())
cfprStatsThrFloatValuePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValuePolicyLevel.setStatus(_A)
_CfprStatsThrFloatValuePolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStatsThrFloatValuePolicyOwner_Object=MibTableColumn
cfprStatsThrFloatValuePolicyOwner=_CfprStatsThrFloatValuePolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,11),_CfprStatsThrFloatValuePolicyOwner_Type())
cfprStatsThrFloatValuePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValuePolicyOwner.setStatus(_A)
_CfprStatsThrFloatValuePropType_Type=CfprStatsThrFloatValuePropType
_CfprStatsThrFloatValuePropType_Object=MibTableColumn
cfprStatsThrFloatValuePropType=_CfprStatsThrFloatValuePropType_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,12),_CfprStatsThrFloatValuePropType_Type())
cfprStatsThrFloatValuePropType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValuePropType.setStatus(_A)
_CfprStatsThrFloatValueSeverity_Type=CfprConditionSeverity
_CfprStatsThrFloatValueSeverity_Object=MibTableColumn
cfprStatsThrFloatValueSeverity=_CfprStatsThrFloatValueSeverity_Object((1,3,6,1,4,1,9,9,826,1,73,11,1,13),_CfprStatsThrFloatValueSeverity_Type())
cfprStatsThrFloatValueSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThrFloatValueSeverity.setStatus(_A)
_CfprStatsThresholdClassTable_Object=MibTable
cfprStatsThresholdClassTable=_CfprStatsThresholdClassTable_Object((1,3,6,1,4,1,9,9,826,1,73,12))
if mibBuilder.loadTexts:cfprStatsThresholdClassTable.setStatus(_A)
_CfprStatsThresholdClassEntry_Object=MibTableRow
cfprStatsThresholdClassEntry=_CfprStatsThresholdClassEntry_Object((1,3,6,1,4,1,9,9,826,1,73,12,1))
cfprStatsThresholdClassEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cfprStatsThresholdClassEntry.setStatus(_A)
_CfprStatsThresholdClassInstanceId_Type=CfprManagedObjectId
_CfprStatsThresholdClassInstanceId_Object=MibTableColumn
cfprStatsThresholdClassInstanceId=_CfprStatsThresholdClassInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,12,1,1),_CfprStatsThresholdClassInstanceId_Type())
cfprStatsThresholdClassInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsThresholdClassInstanceId.setStatus(_A)
_CfprStatsThresholdClassDn_Type=CfprManagedObjectDn
_CfprStatsThresholdClassDn_Object=MibTableColumn
cfprStatsThresholdClassDn=_CfprStatsThresholdClassDn_Object((1,3,6,1,4,1,9,9,826,1,73,12,1,2),_CfprStatsThresholdClassDn_Type())
cfprStatsThresholdClassDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdClassDn.setStatus(_A)
_CfprStatsThresholdClassRn_Type=SnmpAdminString
_CfprStatsThresholdClassRn_Object=MibTableColumn
cfprStatsThresholdClassRn=_CfprStatsThresholdClassRn_Object((1,3,6,1,4,1,9,9,826,1,73,12,1,3),_CfprStatsThresholdClassRn_Type())
cfprStatsThresholdClassRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdClassRn.setStatus(_A)
_CfprStatsThresholdClassDescr_Type=SnmpAdminString
_CfprStatsThresholdClassDescr_Object=MibTableColumn
cfprStatsThresholdClassDescr=_CfprStatsThresholdClassDescr_Object((1,3,6,1,4,1,9,9,826,1,73,12,1,4),_CfprStatsThresholdClassDescr_Type())
cfprStatsThresholdClassDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdClassDescr.setStatus(_A)
_CfprStatsThresholdClassIntId_Type=SnmpAdminString
_CfprStatsThresholdClassIntId_Object=MibTableColumn
cfprStatsThresholdClassIntId=_CfprStatsThresholdClassIntId_Object((1,3,6,1,4,1,9,9,826,1,73,12,1,5),_CfprStatsThresholdClassIntId_Type())
cfprStatsThresholdClassIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdClassIntId.setStatus(_A)
_CfprStatsThresholdClassName_Type=SnmpAdminString
_CfprStatsThresholdClassName_Object=MibTableColumn
cfprStatsThresholdClassName=_CfprStatsThresholdClassName_Object((1,3,6,1,4,1,9,9,826,1,73,12,1,6),_CfprStatsThresholdClassName_Type())
cfprStatsThresholdClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdClassName.setStatus(_A)
_CfprStatsThresholdClassPolicyLevel_Type=Gauge32
_CfprStatsThresholdClassPolicyLevel_Object=MibTableColumn
cfprStatsThresholdClassPolicyLevel=_CfprStatsThresholdClassPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,73,12,1,7),_CfprStatsThresholdClassPolicyLevel_Type())
cfprStatsThresholdClassPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdClassPolicyLevel.setStatus(_A)
_CfprStatsThresholdClassPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStatsThresholdClassPolicyOwner_Object=MibTableColumn
cfprStatsThresholdClassPolicyOwner=_CfprStatsThresholdClassPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,73,12,1,8),_CfprStatsThresholdClassPolicyOwner_Type())
cfprStatsThresholdClassPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdClassPolicyOwner.setStatus(_A)
_CfprStatsThresholdClassStatsClassId_Type=SnmpAdminString
_CfprStatsThresholdClassStatsClassId_Object=MibTableColumn
cfprStatsThresholdClassStatsClassId=_CfprStatsThresholdClassStatsClassId_Object((1,3,6,1,4,1,9,9,826,1,73,12,1,9),_CfprStatsThresholdClassStatsClassId_Type())
cfprStatsThresholdClassStatsClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdClassStatsClassId.setStatus(_A)
_CfprStatsThresholdPolicyTable_Object=MibTable
cfprStatsThresholdPolicyTable=_CfprStatsThresholdPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,73,13))
if mibBuilder.loadTexts:cfprStatsThresholdPolicyTable.setStatus(_A)
_CfprStatsThresholdPolicyEntry_Object=MibTableRow
cfprStatsThresholdPolicyEntry=_CfprStatsThresholdPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,73,13,1))
cfprStatsThresholdPolicyEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cfprStatsThresholdPolicyEntry.setStatus(_A)
_CfprStatsThresholdPolicyInstanceId_Type=CfprManagedObjectId
_CfprStatsThresholdPolicyInstanceId_Object=MibTableColumn
cfprStatsThresholdPolicyInstanceId=_CfprStatsThresholdPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,73,13,1,1),_CfprStatsThresholdPolicyInstanceId_Type())
cfprStatsThresholdPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStatsThresholdPolicyInstanceId.setStatus(_A)
_CfprStatsThresholdPolicyDn_Type=CfprManagedObjectDn
_CfprStatsThresholdPolicyDn_Object=MibTableColumn
cfprStatsThresholdPolicyDn=_CfprStatsThresholdPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,73,13,1,2),_CfprStatsThresholdPolicyDn_Type())
cfprStatsThresholdPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdPolicyDn.setStatus(_A)
_CfprStatsThresholdPolicyRn_Type=SnmpAdminString
_CfprStatsThresholdPolicyRn_Object=MibTableColumn
cfprStatsThresholdPolicyRn=_CfprStatsThresholdPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,73,13,1,3),_CfprStatsThresholdPolicyRn_Type())
cfprStatsThresholdPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdPolicyRn.setStatus(_A)
_CfprStatsThresholdPolicyDescr_Type=SnmpAdminString
_CfprStatsThresholdPolicyDescr_Object=MibTableColumn
cfprStatsThresholdPolicyDescr=_CfprStatsThresholdPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,73,13,1,4),_CfprStatsThresholdPolicyDescr_Type())
cfprStatsThresholdPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdPolicyDescr.setStatus(_A)
_CfprStatsThresholdPolicyIntId_Type=SnmpAdminString
_CfprStatsThresholdPolicyIntId_Object=MibTableColumn
cfprStatsThresholdPolicyIntId=_CfprStatsThresholdPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,73,13,1,5),_CfprStatsThresholdPolicyIntId_Type())
cfprStatsThresholdPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdPolicyIntId.setStatus(_A)
_CfprStatsThresholdPolicyName_Type=SnmpAdminString
_CfprStatsThresholdPolicyName_Object=MibTableColumn
cfprStatsThresholdPolicyName=_CfprStatsThresholdPolicyName_Object((1,3,6,1,4,1,9,9,826,1,73,13,1,6),_CfprStatsThresholdPolicyName_Type())
cfprStatsThresholdPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdPolicyName.setStatus(_A)
_CfprStatsThresholdPolicyPolicyLevel_Type=Gauge32
_CfprStatsThresholdPolicyPolicyLevel_Object=MibTableColumn
cfprStatsThresholdPolicyPolicyLevel=_CfprStatsThresholdPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,73,13,1,7),_CfprStatsThresholdPolicyPolicyLevel_Type())
cfprStatsThresholdPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdPolicyPolicyLevel.setStatus(_A)
_CfprStatsThresholdPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStatsThresholdPolicyPolicyOwner_Object=MibTableColumn
cfprStatsThresholdPolicyPolicyOwner=_CfprStatsThresholdPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,73,13,1,8),_CfprStatsThresholdPolicyPolicyOwner_Type())
cfprStatsThresholdPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStatsThresholdPolicyPolicyOwner.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprStatsObjects':cfprStatsObjects,'cfprStatsCollectionPolicyTable':cfprStatsCollectionPolicyTable,'cfprStatsCollectionPolicyEntry':cfprStatsCollectionPolicyEntry,_E:cfprStatsCollectionPolicyInstanceId,'cfprStatsCollectionPolicyDn':cfprStatsCollectionPolicyDn,'cfprStatsCollectionPolicyRn':cfprStatsCollectionPolicyRn,'cfprStatsCollectionPolicyCollectionInterval':cfprStatsCollectionPolicyCollectionInterval,'cfprStatsCollectionPolicyFsmDescr':cfprStatsCollectionPolicyFsmDescr,'cfprStatsCollectionPolicyFsmPrev':cfprStatsCollectionPolicyFsmPrev,'cfprStatsCollectionPolicyFsmProgr':cfprStatsCollectionPolicyFsmProgr,'cfprStatsCollectionPolicyFsmRmtInvErrCode':cfprStatsCollectionPolicyFsmRmtInvErrCode,'cfprStatsCollectionPolicyFsmRmtInvErrDescr':cfprStatsCollectionPolicyFsmRmtInvErrDescr,'cfprStatsCollectionPolicyFsmRmtInvRslt':cfprStatsCollectionPolicyFsmRmtInvRslt,'cfprStatsCollectionPolicyFsmStageDescr':cfprStatsCollectionPolicyFsmStageDescr,'cfprStatsCollectionPolicyFsmStamp':cfprStatsCollectionPolicyFsmStamp,'cfprStatsCollectionPolicyFsmStatus':cfprStatsCollectionPolicyFsmStatus,'cfprStatsCollectionPolicyFsmTry':cfprStatsCollectionPolicyFsmTry,'cfprStatsCollectionPolicyId':cfprStatsCollectionPolicyId,'cfprStatsCollectionPolicyName':cfprStatsCollectionPolicyName,'cfprStatsCollectionPolicyReportingInterval':cfprStatsCollectionPolicyReportingInterval,'cfprStatsCollectionPolicyFsmTable':cfprStatsCollectionPolicyFsmTable,'cfprStatsCollectionPolicyFsmEntry':cfprStatsCollectionPolicyFsmEntry,_F:cfprStatsCollectionPolicyFsmInstanceId,'cfprStatsCollectionPolicyFsmDn':cfprStatsCollectionPolicyFsmDn,'cfprStatsCollectionPolicyFsmRn':cfprStatsCollectionPolicyFsmRn,'cfprStatsCollectionPolicyFsmCompletionTime':cfprStatsCollectionPolicyFsmCompletionTime,'cfprStatsCollectionPolicyFsmCurrentFsm':cfprStatsCollectionPolicyFsmCurrentFsm,'cfprStatsCollectionPolicyFsmDescrData':cfprStatsCollectionPolicyFsmDescrData,'cfprStatsCollectionPolicyFsmFsmStatus':cfprStatsCollectionPolicyFsmFsmStatus,'cfprStatsCollectionPolicyFsmProgress':cfprStatsCollectionPolicyFsmProgress,'cfprStatsCollectionPolicyFsmRmtErrCode':cfprStatsCollectionPolicyFsmRmtErrCode,'cfprStatsCollectionPolicyFsmRmtErrDescr':cfprStatsCollectionPolicyFsmRmtErrDescr,'cfprStatsCollectionPolicyFsmRmtRslt':cfprStatsCollectionPolicyFsmRmtRslt,'cfprStatsCollectionPolicyFsmStageTable':cfprStatsCollectionPolicyFsmStageTable,'cfprStatsCollectionPolicyFsmStageEntry':cfprStatsCollectionPolicyFsmStageEntry,_G:cfprStatsCollectionPolicyFsmStageInstanceId,'cfprStatsCollectionPolicyFsmStageDn':cfprStatsCollectionPolicyFsmStageDn,'cfprStatsCollectionPolicyFsmStageRn':cfprStatsCollectionPolicyFsmStageRn,'cfprStatsCollectionPolicyFsmStageDescrData':cfprStatsCollectionPolicyFsmStageDescrData,'cfprStatsCollectionPolicyFsmStageLastUpdateTime':cfprStatsCollectionPolicyFsmStageLastUpdateTime,'cfprStatsCollectionPolicyFsmStageName':cfprStatsCollectionPolicyFsmStageName,'cfprStatsCollectionPolicyFsmStageOrder':cfprStatsCollectionPolicyFsmStageOrder,'cfprStatsCollectionPolicyFsmStageRetry':cfprStatsCollectionPolicyFsmStageRetry,'cfprStatsCollectionPolicyFsmStageStageStatus':cfprStatsCollectionPolicyFsmStageStageStatus,'cfprStatsCollectionPolicyFsmTaskTable':cfprStatsCollectionPolicyFsmTaskTable,'cfprStatsCollectionPolicyFsmTaskEntry':cfprStatsCollectionPolicyFsmTaskEntry,_H:cfprStatsCollectionPolicyFsmTaskInstanceId,'cfprStatsCollectionPolicyFsmTaskDn':cfprStatsCollectionPolicyFsmTaskDn,'cfprStatsCollectionPolicyFsmTaskRn':cfprStatsCollectionPolicyFsmTaskRn,'cfprStatsCollectionPolicyFsmTaskCompletion':cfprStatsCollectionPolicyFsmTaskCompletion,'cfprStatsCollectionPolicyFsmTaskFlags':cfprStatsCollectionPolicyFsmTaskFlags,'cfprStatsCollectionPolicyFsmTaskItem':cfprStatsCollectionPolicyFsmTaskItem,'cfprStatsCollectionPolicyFsmTaskSeqId':cfprStatsCollectionPolicyFsmTaskSeqId,'cfprStatsHolderTable':cfprStatsHolderTable,'cfprStatsHolderEntry':cfprStatsHolderEntry,_I:cfprStatsHolderInstanceId,'cfprStatsHolderDn':cfprStatsHolderDn,'cfprStatsHolderRn':cfprStatsHolderRn,'cfprStatsHolderName':cfprStatsHolderName,'cfprStatsThr32DefinitionTable':cfprStatsThr32DefinitionTable,'cfprStatsThr32DefinitionEntry':cfprStatsThr32DefinitionEntry,_J:cfprStatsThr32DefinitionInstanceId,'cfprStatsThr32DefinitionDn':cfprStatsThr32DefinitionDn,'cfprStatsThr32DefinitionRn':cfprStatsThr32DefinitionRn,'cfprStatsThr32DefinitionDescr':cfprStatsThr32DefinitionDescr,'cfprStatsThr32DefinitionIntId':cfprStatsThr32DefinitionIntId,'cfprStatsThr32DefinitionName':cfprStatsThr32DefinitionName,'cfprStatsThr32DefinitionNormalValue':cfprStatsThr32DefinitionNormalValue,'cfprStatsThr32DefinitionPolicyLevel':cfprStatsThr32DefinitionPolicyLevel,'cfprStatsThr32DefinitionPolicyOwner':cfprStatsThr32DefinitionPolicyOwner,'cfprStatsThr32DefinitionPropId':cfprStatsThr32DefinitionPropId,'cfprStatsThr32DefinitionPropType':cfprStatsThr32DefinitionPropType,'cfprStatsThr32ValueTable':cfprStatsThr32ValueTable,'cfprStatsThr32ValueEntry':cfprStatsThr32ValueEntry,_K:cfprStatsThr32ValueInstanceId,'cfprStatsThr32ValueDn':cfprStatsThr32ValueDn,'cfprStatsThr32ValueRn':cfprStatsThr32ValueRn,'cfprStatsThr32ValueDeescalating':cfprStatsThr32ValueDeescalating,'cfprStatsThr32ValueDescr':cfprStatsThr32ValueDescr,'cfprStatsThr32ValueDirection':cfprStatsThr32ValueDirection,'cfprStatsThr32ValueEscalating':cfprStatsThr32ValueEscalating,'cfprStatsThr32ValueIntId':cfprStatsThr32ValueIntId,'cfprStatsThr32ValueName':cfprStatsThr32ValueName,'cfprStatsThr32ValuePolicyLevel':cfprStatsThr32ValuePolicyLevel,'cfprStatsThr32ValuePolicyOwner':cfprStatsThr32ValuePolicyOwner,'cfprStatsThr32ValuePropType':cfprStatsThr32ValuePropType,'cfprStatsThr32ValueSeverity':cfprStatsThr32ValueSeverity,'cfprStatsThr64DefinitionTable':cfprStatsThr64DefinitionTable,'cfprStatsThr64DefinitionEntry':cfprStatsThr64DefinitionEntry,_L:cfprStatsThr64DefinitionInstanceId,'cfprStatsThr64DefinitionDn':cfprStatsThr64DefinitionDn,'cfprStatsThr64DefinitionRn':cfprStatsThr64DefinitionRn,'cfprStatsThr64DefinitionDescr':cfprStatsThr64DefinitionDescr,'cfprStatsThr64DefinitionIntId':cfprStatsThr64DefinitionIntId,'cfprStatsThr64DefinitionName':cfprStatsThr64DefinitionName,'cfprStatsThr64DefinitionNormalValue':cfprStatsThr64DefinitionNormalValue,'cfprStatsThr64DefinitionPolicyLevel':cfprStatsThr64DefinitionPolicyLevel,'cfprStatsThr64DefinitionPolicyOwner':cfprStatsThr64DefinitionPolicyOwner,'cfprStatsThr64DefinitionPropId':cfprStatsThr64DefinitionPropId,'cfprStatsThr64DefinitionPropType':cfprStatsThr64DefinitionPropType,'cfprStatsThr64ValueTable':cfprStatsThr64ValueTable,'cfprStatsThr64ValueEntry':cfprStatsThr64ValueEntry,_M:cfprStatsThr64ValueInstanceId,'cfprStatsThr64ValueDn':cfprStatsThr64ValueDn,'cfprStatsThr64ValueRn':cfprStatsThr64ValueRn,'cfprStatsThr64ValueDeescalating':cfprStatsThr64ValueDeescalating,'cfprStatsThr64ValueDescr':cfprStatsThr64ValueDescr,'cfprStatsThr64ValueDirection':cfprStatsThr64ValueDirection,'cfprStatsThr64ValueEscalating':cfprStatsThr64ValueEscalating,'cfprStatsThr64ValueIntId':cfprStatsThr64ValueIntId,'cfprStatsThr64ValueName':cfprStatsThr64ValueName,'cfprStatsThr64ValuePolicyLevel':cfprStatsThr64ValuePolicyLevel,'cfprStatsThr64ValuePolicyOwner':cfprStatsThr64ValuePolicyOwner,'cfprStatsThr64ValuePropType':cfprStatsThr64ValuePropType,'cfprStatsThr64ValueSeverity':cfprStatsThr64ValueSeverity,'cfprStatsThrFloatDefinitionTable':cfprStatsThrFloatDefinitionTable,'cfprStatsThrFloatDefinitionEntry':cfprStatsThrFloatDefinitionEntry,_N:cfprStatsThrFloatDefinitionInstanceId,'cfprStatsThrFloatDefinitionDn':cfprStatsThrFloatDefinitionDn,'cfprStatsThrFloatDefinitionRn':cfprStatsThrFloatDefinitionRn,'cfprStatsThrFloatDefinitionDescr':cfprStatsThrFloatDefinitionDescr,'cfprStatsThrFloatDefinitionIntId':cfprStatsThrFloatDefinitionIntId,'cfprStatsThrFloatDefinitionName':cfprStatsThrFloatDefinitionName,'cfprStatsThrFloatDefinitionNormalValue':cfprStatsThrFloatDefinitionNormalValue,'cfprStatsThrFloatDefinitionPolicyLevel':cfprStatsThrFloatDefinitionPolicyLevel,'cfprStatsThrFloatDefinitionPolicyOwner':cfprStatsThrFloatDefinitionPolicyOwner,'cfprStatsThrFloatDefinitionPropId':cfprStatsThrFloatDefinitionPropId,'cfprStatsThrFloatDefinitionPropType':cfprStatsThrFloatDefinitionPropType,'cfprStatsThrFloatValueTable':cfprStatsThrFloatValueTable,'cfprStatsThrFloatValueEntry':cfprStatsThrFloatValueEntry,_O:cfprStatsThrFloatValueInstanceId,'cfprStatsThrFloatValueDn':cfprStatsThrFloatValueDn,'cfprStatsThrFloatValueRn':cfprStatsThrFloatValueRn,'cfprStatsThrFloatValueDeescalating':cfprStatsThrFloatValueDeescalating,'cfprStatsThrFloatValueDescr':cfprStatsThrFloatValueDescr,'cfprStatsThrFloatValueDirection':cfprStatsThrFloatValueDirection,'cfprStatsThrFloatValueEscalating':cfprStatsThrFloatValueEscalating,'cfprStatsThrFloatValueIntId':cfprStatsThrFloatValueIntId,'cfprStatsThrFloatValueName':cfprStatsThrFloatValueName,'cfprStatsThrFloatValuePolicyLevel':cfprStatsThrFloatValuePolicyLevel,'cfprStatsThrFloatValuePolicyOwner':cfprStatsThrFloatValuePolicyOwner,'cfprStatsThrFloatValuePropType':cfprStatsThrFloatValuePropType,'cfprStatsThrFloatValueSeverity':cfprStatsThrFloatValueSeverity,'cfprStatsThresholdClassTable':cfprStatsThresholdClassTable,'cfprStatsThresholdClassEntry':cfprStatsThresholdClassEntry,_P:cfprStatsThresholdClassInstanceId,'cfprStatsThresholdClassDn':cfprStatsThresholdClassDn,'cfprStatsThresholdClassRn':cfprStatsThresholdClassRn,'cfprStatsThresholdClassDescr':cfprStatsThresholdClassDescr,'cfprStatsThresholdClassIntId':cfprStatsThresholdClassIntId,'cfprStatsThresholdClassName':cfprStatsThresholdClassName,'cfprStatsThresholdClassPolicyLevel':cfprStatsThresholdClassPolicyLevel,'cfprStatsThresholdClassPolicyOwner':cfprStatsThresholdClassPolicyOwner,'cfprStatsThresholdClassStatsClassId':cfprStatsThresholdClassStatsClassId,'cfprStatsThresholdPolicyTable':cfprStatsThresholdPolicyTable,'cfprStatsThresholdPolicyEntry':cfprStatsThresholdPolicyEntry,_Q:cfprStatsThresholdPolicyInstanceId,'cfprStatsThresholdPolicyDn':cfprStatsThresholdPolicyDn,'cfprStatsThresholdPolicyRn':cfprStatsThresholdPolicyRn,'cfprStatsThresholdPolicyDescr':cfprStatsThresholdPolicyDescr,'cfprStatsThresholdPolicyIntId':cfprStatsThresholdPolicyIntId,'cfprStatsThresholdPolicyName':cfprStatsThresholdPolicyName,'cfprStatsThresholdPolicyPolicyLevel':cfprStatsThresholdPolicyPolicyLevel,'cfprStatsThresholdPolicyPolicyOwner':cfprStatsThresholdPolicyPolicyOwner})