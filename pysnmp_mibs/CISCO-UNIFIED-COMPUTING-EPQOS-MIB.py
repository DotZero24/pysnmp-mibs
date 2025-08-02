_M='cucsEpqosDefinitionFsmStageInstanceId'
_L='cucsEpqosDefinitionFsmInstanceId'
_K='cucsEpqosDefinitionDelTaskFsmStageInstanceId'
_J='cucsEpqosDefinitionDelTaskFsmInstanceId'
_I='cucsEpqosEgressInstanceId'
_H='cucsEpqosDefinitionFsmTaskInstanceId'
_G='cucsEpqosDefinitionDelTaskFsmTaskInstanceId'
_F='cucsEpqosDefinitionDelTaskInstanceId'
_E='cucsEpqosDefinitionInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-EPQOS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsConditionRemoteInvRslt,CucsEpqosDefinitionDelTaskFsmCurrentFsm,CucsEpqosDefinitionDelTaskFsmStageName,CucsEpqosDefinitionDelTaskFsmTaskItem,CucsEpqosDefinitionFsmCurrentFsm,CucsEpqosDefinitionFsmStageName,CucsEpqosDefinitionFsmTaskItem,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsPolicyPolicyOwner,CucsQosHostControl,CucsQosPriority=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsConditionRemoteInvRslt','CucsEpqosDefinitionDelTaskFsmCurrentFsm','CucsEpqosDefinitionDelTaskFsmStageName','CucsEpqosDefinitionDelTaskFsmTaskItem','CucsEpqosDefinitionFsmCurrentFsm','CucsEpqosDefinitionFsmStageName','CucsEpqosDefinitionFsmTaskItem','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsPolicyPolicyOwner','CucsQosHostControl','CucsQosPriority')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsEpqosObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,14))
_CucsEpqosDefinitionTable_Object=MibTable
cucsEpqosDefinitionTable=_CucsEpqosDefinitionTable_Object((1,3,6,1,4,1,9,9,719,1,14,1))
if mibBuilder.loadTexts:cucsEpqosDefinitionTable.setStatus(_A)
_CucsEpqosDefinitionEntry_Object=MibTableRow
cucsEpqosDefinitionEntry=_CucsEpqosDefinitionEntry_Object((1,3,6,1,4,1,9,9,719,1,14,1,1))
cucsEpqosDefinitionEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsEpqosDefinitionEntry.setStatus(_A)
_CucsEpqosDefinitionInstanceId_Type=CucsManagedObjectId
_CucsEpqosDefinitionInstanceId_Object=MibTableColumn
cucsEpqosDefinitionInstanceId=_CucsEpqosDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,1),_CucsEpqosDefinitionInstanceId_Type())
cucsEpqosDefinitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEpqosDefinitionInstanceId.setStatus(_A)
_CucsEpqosDefinitionDn_Type=CucsManagedObjectDn
_CucsEpqosDefinitionDn_Object=MibTableColumn
cucsEpqosDefinitionDn=_CucsEpqosDefinitionDn_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,2),_CucsEpqosDefinitionDn_Type())
cucsEpqosDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDn.setStatus(_A)
_CucsEpqosDefinitionRn_Type=SnmpAdminString
_CucsEpqosDefinitionRn_Object=MibTableColumn
cucsEpqosDefinitionRn=_CucsEpqosDefinitionRn_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,3),_CucsEpqosDefinitionRn_Type())
cucsEpqosDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionRn.setStatus(_A)
_CucsEpqosDefinitionDescr_Type=SnmpAdminString
_CucsEpqosDefinitionDescr_Object=MibTableColumn
cucsEpqosDefinitionDescr=_CucsEpqosDefinitionDescr_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,4),_CucsEpqosDefinitionDescr_Type())
cucsEpqosDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDescr.setStatus(_A)
_CucsEpqosDefinitionFsmDescr_Type=SnmpAdminString
_CucsEpqosDefinitionFsmDescr_Object=MibTableColumn
cucsEpqosDefinitionFsmDescr=_CucsEpqosDefinitionFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,5),_CucsEpqosDefinitionFsmDescr_Type())
cucsEpqosDefinitionFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmDescr.setStatus(_A)
_CucsEpqosDefinitionFsmPrev_Type=SnmpAdminString
_CucsEpqosDefinitionFsmPrev_Object=MibTableColumn
cucsEpqosDefinitionFsmPrev=_CucsEpqosDefinitionFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,6),_CucsEpqosDefinitionFsmPrev_Type())
cucsEpqosDefinitionFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmPrev.setStatus(_A)
_CucsEpqosDefinitionFsmProgr_Type=Gauge32
_CucsEpqosDefinitionFsmProgr_Object=MibTableColumn
cucsEpqosDefinitionFsmProgr=_CucsEpqosDefinitionFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,7),_CucsEpqosDefinitionFsmProgr_Type())
cucsEpqosDefinitionFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmProgr.setStatus(_A)
_CucsEpqosDefinitionFsmRmtInvErrCode_Type=Gauge32
_CucsEpqosDefinitionFsmRmtInvErrCode_Object=MibTableColumn
cucsEpqosDefinitionFsmRmtInvErrCode=_CucsEpqosDefinitionFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,8),_CucsEpqosDefinitionFsmRmtInvErrCode_Type())
cucsEpqosDefinitionFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmRmtInvErrCode.setStatus(_A)
_CucsEpqosDefinitionFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsEpqosDefinitionFsmRmtInvErrDescr_Object=MibTableColumn
cucsEpqosDefinitionFsmRmtInvErrDescr=_CucsEpqosDefinitionFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,9),_CucsEpqosDefinitionFsmRmtInvErrDescr_Type())
cucsEpqosDefinitionFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmRmtInvErrDescr.setStatus(_A)
_CucsEpqosDefinitionFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsEpqosDefinitionFsmRmtInvRslt_Object=MibTableColumn
cucsEpqosDefinitionFsmRmtInvRslt=_CucsEpqosDefinitionFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,10),_CucsEpqosDefinitionFsmRmtInvRslt_Type())
cucsEpqosDefinitionFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmRmtInvRslt.setStatus(_A)
_CucsEpqosDefinitionFsmStageDescr_Type=SnmpAdminString
_CucsEpqosDefinitionFsmStageDescr_Object=MibTableColumn
cucsEpqosDefinitionFsmStageDescr=_CucsEpqosDefinitionFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,11),_CucsEpqosDefinitionFsmStageDescr_Type())
cucsEpqosDefinitionFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageDescr.setStatus(_A)
_CucsEpqosDefinitionFsmStamp_Type=DateAndTime
_CucsEpqosDefinitionFsmStamp_Object=MibTableColumn
cucsEpqosDefinitionFsmStamp=_CucsEpqosDefinitionFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,12),_CucsEpqosDefinitionFsmStamp_Type())
cucsEpqosDefinitionFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStamp.setStatus(_A)
_CucsEpqosDefinitionFsmStatus_Type=SnmpAdminString
_CucsEpqosDefinitionFsmStatus_Object=MibTableColumn
cucsEpqosDefinitionFsmStatus=_CucsEpqosDefinitionFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,13),_CucsEpqosDefinitionFsmStatus_Type())
cucsEpqosDefinitionFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStatus.setStatus(_A)
_CucsEpqosDefinitionFsmTry_Type=Gauge32
_CucsEpqosDefinitionFsmTry_Object=MibTableColumn
cucsEpqosDefinitionFsmTry=_CucsEpqosDefinitionFsmTry_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,14),_CucsEpqosDefinitionFsmTry_Type())
cucsEpqosDefinitionFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTry.setStatus(_A)
_CucsEpqosDefinitionIntId_Type=SnmpAdminString
_CucsEpqosDefinitionIntId_Object=MibTableColumn
cucsEpqosDefinitionIntId=_CucsEpqosDefinitionIntId_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,15),_CucsEpqosDefinitionIntId_Type())
cucsEpqosDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionIntId.setStatus(_A)
_CucsEpqosDefinitionName_Type=SnmpAdminString
_CucsEpqosDefinitionName_Object=MibTableColumn
cucsEpqosDefinitionName=_CucsEpqosDefinitionName_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,16),_CucsEpqosDefinitionName_Type())
cucsEpqosDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionName.setStatus(_A)
_CucsEpqosDefinitionPolicyLevel_Type=Gauge32
_CucsEpqosDefinitionPolicyLevel_Object=MibTableColumn
cucsEpqosDefinitionPolicyLevel=_CucsEpqosDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,17),_CucsEpqosDefinitionPolicyLevel_Type())
cucsEpqosDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionPolicyLevel.setStatus(_A)
_CucsEpqosDefinitionPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsEpqosDefinitionPolicyOwner_Object=MibTableColumn
cucsEpqosDefinitionPolicyOwner=_CucsEpqosDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,14,1,1,18),_CucsEpqosDefinitionPolicyOwner_Type())
cucsEpqosDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionPolicyOwner.setStatus(_A)
_CucsEpqosDefinitionDelTaskTable_Object=MibTable
cucsEpqosDefinitionDelTaskTable=_CucsEpqosDefinitionDelTaskTable_Object((1,3,6,1,4,1,9,9,719,1,14,2))
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskTable.setStatus(_A)
_CucsEpqosDefinitionDelTaskEntry_Object=MibTableRow
cucsEpqosDefinitionDelTaskEntry=_CucsEpqosDefinitionDelTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,14,2,1))
cucsEpqosDefinitionDelTaskEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskEntry.setStatus(_A)
_CucsEpqosDefinitionDelTaskInstanceId_Type=CucsManagedObjectId
_CucsEpqosDefinitionDelTaskInstanceId_Object=MibTableColumn
cucsEpqosDefinitionDelTaskInstanceId=_CucsEpqosDefinitionDelTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,1),_CucsEpqosDefinitionDelTaskInstanceId_Type())
cucsEpqosDefinitionDelTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskInstanceId.setStatus(_A)
_CucsEpqosDefinitionDelTaskDn_Type=CucsManagedObjectDn
_CucsEpqosDefinitionDelTaskDn_Object=MibTableColumn
cucsEpqosDefinitionDelTaskDn=_CucsEpqosDefinitionDelTaskDn_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,2),_CucsEpqosDefinitionDelTaskDn_Type())
cucsEpqosDefinitionDelTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskDn.setStatus(_A)
_CucsEpqosDefinitionDelTaskRn_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskRn_Object=MibTableColumn
cucsEpqosDefinitionDelTaskRn=_CucsEpqosDefinitionDelTaskRn_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,3),_CucsEpqosDefinitionDelTaskRn_Type())
cucsEpqosDefinitionDelTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskRn.setStatus(_A)
_CucsEpqosDefinitionDelTaskDefIntId_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskDefIntId_Object=MibTableColumn
cucsEpqosDefinitionDelTaskDefIntId=_CucsEpqosDefinitionDelTaskDefIntId_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,4),_CucsEpqosDefinitionDelTaskDefIntId_Type())
cucsEpqosDefinitionDelTaskDefIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskDefIntId.setStatus(_A)
_CucsEpqosDefinitionDelTaskDescr_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskDescr_Object=MibTableColumn
cucsEpqosDefinitionDelTaskDescr=_CucsEpqosDefinitionDelTaskDescr_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,5),_CucsEpqosDefinitionDelTaskDescr_Type())
cucsEpqosDefinitionDelTaskDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskDescr.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmDescr_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmDescr_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmDescr=_CucsEpqosDefinitionDelTaskFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,6),_CucsEpqosDefinitionDelTaskFsmDescr_Type())
cucsEpqosDefinitionDelTaskFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmDescr.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmPrev_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmPrev_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmPrev=_CucsEpqosDefinitionDelTaskFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,7),_CucsEpqosDefinitionDelTaskFsmPrev_Type())
cucsEpqosDefinitionDelTaskFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmPrev.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmProgr_Type=Gauge32
_CucsEpqosDefinitionDelTaskFsmProgr_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmProgr=_CucsEpqosDefinitionDelTaskFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,8),_CucsEpqosDefinitionDelTaskFsmProgr_Type())
cucsEpqosDefinitionDelTaskFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmProgr.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmRmtInvErrCode_Type=Gauge32
_CucsEpqosDefinitionDelTaskFsmRmtInvErrCode_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtInvErrCode=_CucsEpqosDefinitionDelTaskFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,9),_CucsEpqosDefinitionDelTaskFsmRmtInvErrCode_Type())
cucsEpqosDefinitionDelTaskFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmRmtInvErrCode.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmRmtInvErrDescr_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr=_CucsEpqosDefinitionDelTaskFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,10),_CucsEpqosDefinitionDelTaskFsmRmtInvErrDescr_Type())
cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsEpqosDefinitionDelTaskFsmRmtInvRslt_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtInvRslt=_CucsEpqosDefinitionDelTaskFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,11),_CucsEpqosDefinitionDelTaskFsmRmtInvRslt_Type())
cucsEpqosDefinitionDelTaskFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmRmtInvRslt.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageDescr_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmStageDescr_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageDescr=_CucsEpqosDefinitionDelTaskFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,12),_CucsEpqosDefinitionDelTaskFsmStageDescr_Type())
cucsEpqosDefinitionDelTaskFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageDescr.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStamp_Type=DateAndTime
_CucsEpqosDefinitionDelTaskFsmStamp_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStamp=_CucsEpqosDefinitionDelTaskFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,13),_CucsEpqosDefinitionDelTaskFsmStamp_Type())
cucsEpqosDefinitionDelTaskFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStamp.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStatus_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmStatus_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStatus=_CucsEpqosDefinitionDelTaskFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,14),_CucsEpqosDefinitionDelTaskFsmStatus_Type())
cucsEpqosDefinitionDelTaskFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStatus.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTry_Type=Gauge32
_CucsEpqosDefinitionDelTaskFsmTry_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmTry=_CucsEpqosDefinitionDelTaskFsmTry_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,15),_CucsEpqosDefinitionDelTaskFsmTry_Type())
cucsEpqosDefinitionDelTaskFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTry.setStatus(_A)
_CucsEpqosDefinitionDelTaskIntId_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskIntId_Object=MibTableColumn
cucsEpqosDefinitionDelTaskIntId=_CucsEpqosDefinitionDelTaskIntId_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,16),_CucsEpqosDefinitionDelTaskIntId_Type())
cucsEpqosDefinitionDelTaskIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskIntId.setStatus(_A)
_CucsEpqosDefinitionDelTaskName_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskName_Object=MibTableColumn
cucsEpqosDefinitionDelTaskName=_CucsEpqosDefinitionDelTaskName_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,17),_CucsEpqosDefinitionDelTaskName_Type())
cucsEpqosDefinitionDelTaskName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskName.setStatus(_A)
_CucsEpqosDefinitionDelTaskDefDn_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskDefDn_Object=MibTableColumn
cucsEpqosDefinitionDelTaskDefDn=_CucsEpqosDefinitionDelTaskDefDn_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,18),_CucsEpqosDefinitionDelTaskDefDn_Type())
cucsEpqosDefinitionDelTaskDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskDefDn.setStatus(_A)
_CucsEpqosDefinitionDelTaskPolicyLevel_Type=Gauge32
_CucsEpqosDefinitionDelTaskPolicyLevel_Object=MibTableColumn
cucsEpqosDefinitionDelTaskPolicyLevel=_CucsEpqosDefinitionDelTaskPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,19),_CucsEpqosDefinitionDelTaskPolicyLevel_Type())
cucsEpqosDefinitionDelTaskPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskPolicyLevel.setStatus(_A)
_CucsEpqosDefinitionDelTaskPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsEpqosDefinitionDelTaskPolicyOwner_Object=MibTableColumn
cucsEpqosDefinitionDelTaskPolicyOwner=_CucsEpqosDefinitionDelTaskPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,14,2,1,20),_CucsEpqosDefinitionDelTaskPolicyOwner_Type())
cucsEpqosDefinitionDelTaskPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskPolicyOwner.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTaskTable_Object=MibTable
cucsEpqosDefinitionDelTaskFsmTaskTable=_CucsEpqosDefinitionDelTaskFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,14,3))
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTaskTable.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTaskEntry_Object=MibTableRow
cucsEpqosDefinitionDelTaskFsmTaskEntry=_CucsEpqosDefinitionDelTaskFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,14,3,1))
cucsEpqosDefinitionDelTaskFsmTaskEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTaskEntry.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsEpqosDefinitionDelTaskFsmTaskInstanceId_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskInstanceId=_CucsEpqosDefinitionDelTaskFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,14,3,1,1),_CucsEpqosDefinitionDelTaskFsmTaskInstanceId_Type())
cucsEpqosDefinitionDelTaskFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTaskInstanceId.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTaskDn_Type=CucsManagedObjectDn
_CucsEpqosDefinitionDelTaskFsmTaskDn_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskDn=_CucsEpqosDefinitionDelTaskFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,14,3,1,2),_CucsEpqosDefinitionDelTaskFsmTaskDn_Type())
cucsEpqosDefinitionDelTaskFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTaskDn.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTaskRn_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmTaskRn_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskRn=_CucsEpqosDefinitionDelTaskFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,14,3,1,3),_CucsEpqosDefinitionDelTaskFsmTaskRn_Type())
cucsEpqosDefinitionDelTaskFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTaskRn.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTaskCompletion_Type=CucsFsmCompletion
_CucsEpqosDefinitionDelTaskFsmTaskCompletion_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskCompletion=_CucsEpqosDefinitionDelTaskFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,14,3,1,4),_CucsEpqosDefinitionDelTaskFsmTaskCompletion_Type())
cucsEpqosDefinitionDelTaskFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTaskCompletion.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTaskFlags_Type=CucsFsmFlags
_CucsEpqosDefinitionDelTaskFsmTaskFlags_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskFlags=_CucsEpqosDefinitionDelTaskFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,14,3,1,5),_CucsEpqosDefinitionDelTaskFsmTaskFlags_Type())
cucsEpqosDefinitionDelTaskFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTaskFlags.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTaskItem_Type=CucsEpqosDefinitionDelTaskFsmTaskItem
_CucsEpqosDefinitionDelTaskFsmTaskItem_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskItem=_CucsEpqosDefinitionDelTaskFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,14,3,1,6),_CucsEpqosDefinitionDelTaskFsmTaskItem_Type())
cucsEpqosDefinitionDelTaskFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTaskItem.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTaskSeqId_Type=Gauge32
_CucsEpqosDefinitionDelTaskFsmTaskSeqId_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskSeqId=_CucsEpqosDefinitionDelTaskFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,14,3,1,7),_CucsEpqosDefinitionDelTaskFsmTaskSeqId_Type())
cucsEpqosDefinitionDelTaskFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTaskSeqId.setStatus(_A)
_CucsEpqosDefinitionFsmTaskTable_Object=MibTable
cucsEpqosDefinitionFsmTaskTable=_CucsEpqosDefinitionFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,14,4))
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTaskTable.setStatus(_A)
_CucsEpqosDefinitionFsmTaskEntry_Object=MibTableRow
cucsEpqosDefinitionFsmTaskEntry=_CucsEpqosDefinitionFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,14,4,1))
cucsEpqosDefinitionFsmTaskEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTaskEntry.setStatus(_A)
_CucsEpqosDefinitionFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsEpqosDefinitionFsmTaskInstanceId_Object=MibTableColumn
cucsEpqosDefinitionFsmTaskInstanceId=_CucsEpqosDefinitionFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,14,4,1,1),_CucsEpqosDefinitionFsmTaskInstanceId_Type())
cucsEpqosDefinitionFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTaskInstanceId.setStatus(_A)
_CucsEpqosDefinitionFsmTaskDn_Type=CucsManagedObjectDn
_CucsEpqosDefinitionFsmTaskDn_Object=MibTableColumn
cucsEpqosDefinitionFsmTaskDn=_CucsEpqosDefinitionFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,14,4,1,2),_CucsEpqosDefinitionFsmTaskDn_Type())
cucsEpqosDefinitionFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTaskDn.setStatus(_A)
_CucsEpqosDefinitionFsmTaskRn_Type=SnmpAdminString
_CucsEpqosDefinitionFsmTaskRn_Object=MibTableColumn
cucsEpqosDefinitionFsmTaskRn=_CucsEpqosDefinitionFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,14,4,1,3),_CucsEpqosDefinitionFsmTaskRn_Type())
cucsEpqosDefinitionFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTaskRn.setStatus(_A)
_CucsEpqosDefinitionFsmTaskCompletion_Type=CucsFsmCompletion
_CucsEpqosDefinitionFsmTaskCompletion_Object=MibTableColumn
cucsEpqosDefinitionFsmTaskCompletion=_CucsEpqosDefinitionFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,14,4,1,4),_CucsEpqosDefinitionFsmTaskCompletion_Type())
cucsEpqosDefinitionFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTaskCompletion.setStatus(_A)
_CucsEpqosDefinitionFsmTaskFlags_Type=CucsFsmFlags
_CucsEpqosDefinitionFsmTaskFlags_Object=MibTableColumn
cucsEpqosDefinitionFsmTaskFlags=_CucsEpqosDefinitionFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,14,4,1,5),_CucsEpqosDefinitionFsmTaskFlags_Type())
cucsEpqosDefinitionFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTaskFlags.setStatus(_A)
_CucsEpqosDefinitionFsmTaskItem_Type=CucsEpqosDefinitionFsmTaskItem
_CucsEpqosDefinitionFsmTaskItem_Object=MibTableColumn
cucsEpqosDefinitionFsmTaskItem=_CucsEpqosDefinitionFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,14,4,1,6),_CucsEpqosDefinitionFsmTaskItem_Type())
cucsEpqosDefinitionFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTaskItem.setStatus(_A)
_CucsEpqosDefinitionFsmTaskSeqId_Type=Gauge32
_CucsEpqosDefinitionFsmTaskSeqId_Object=MibTableColumn
cucsEpqosDefinitionFsmTaskSeqId=_CucsEpqosDefinitionFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,14,4,1,7),_CucsEpqosDefinitionFsmTaskSeqId_Type())
cucsEpqosDefinitionFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTaskSeqId.setStatus(_A)
_CucsEpqosEgressTable_Object=MibTable
cucsEpqosEgressTable=_CucsEpqosEgressTable_Object((1,3,6,1,4,1,9,9,719,1,14,5))
if mibBuilder.loadTexts:cucsEpqosEgressTable.setStatus(_A)
_CucsEpqosEgressEntry_Object=MibTableRow
cucsEpqosEgressEntry=_CucsEpqosEgressEntry_Object((1,3,6,1,4,1,9,9,719,1,14,5,1))
cucsEpqosEgressEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsEpqosEgressEntry.setStatus(_A)
_CucsEpqosEgressInstanceId_Type=CucsManagedObjectId
_CucsEpqosEgressInstanceId_Object=MibTableColumn
cucsEpqosEgressInstanceId=_CucsEpqosEgressInstanceId_Object((1,3,6,1,4,1,9,9,719,1,14,5,1,1),_CucsEpqosEgressInstanceId_Type())
cucsEpqosEgressInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEpqosEgressInstanceId.setStatus(_A)
_CucsEpqosEgressDn_Type=CucsManagedObjectDn
_CucsEpqosEgressDn_Object=MibTableColumn
cucsEpqosEgressDn=_CucsEpqosEgressDn_Object((1,3,6,1,4,1,9,9,719,1,14,5,1,2),_CucsEpqosEgressDn_Type())
cucsEpqosEgressDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosEgressDn.setStatus(_A)
_CucsEpqosEgressRn_Type=SnmpAdminString
_CucsEpqosEgressRn_Object=MibTableColumn
cucsEpqosEgressRn=_CucsEpqosEgressRn_Object((1,3,6,1,4,1,9,9,719,1,14,5,1,3),_CucsEpqosEgressRn_Type())
cucsEpqosEgressRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosEgressRn.setStatus(_A)
_CucsEpqosEgressBurst_Type=Gauge32
_CucsEpqosEgressBurst_Object=MibTableColumn
cucsEpqosEgressBurst=_CucsEpqosEgressBurst_Object((1,3,6,1,4,1,9,9,719,1,14,5,1,4),_CucsEpqosEgressBurst_Type())
cucsEpqosEgressBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosEgressBurst.setStatus(_A)
_CucsEpqosEgressHostControl_Type=CucsQosHostControl
_CucsEpqosEgressHostControl_Object=MibTableColumn
cucsEpqosEgressHostControl=_CucsEpqosEgressHostControl_Object((1,3,6,1,4,1,9,9,719,1,14,5,1,5),_CucsEpqosEgressHostControl_Type())
cucsEpqosEgressHostControl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosEgressHostControl.setStatus(_A)
_CucsEpqosEgressName_Type=SnmpAdminString
_CucsEpqosEgressName_Object=MibTableColumn
cucsEpqosEgressName=_CucsEpqosEgressName_Object((1,3,6,1,4,1,9,9,719,1,14,5,1,6),_CucsEpqosEgressName_Type())
cucsEpqosEgressName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosEgressName.setStatus(_A)
_CucsEpqosEgressPrio_Type=CucsQosPriority
_CucsEpqosEgressPrio_Object=MibTableColumn
cucsEpqosEgressPrio=_CucsEpqosEgressPrio_Object((1,3,6,1,4,1,9,9,719,1,14,5,1,7),_CucsEpqosEgressPrio_Type())
cucsEpqosEgressPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosEgressPrio.setStatus(_A)
_CucsEpqosEgressRate_Type=Gauge32
_CucsEpqosEgressRate_Object=MibTableColumn
cucsEpqosEgressRate=_CucsEpqosEgressRate_Object((1,3,6,1,4,1,9,9,719,1,14,5,1,8),_CucsEpqosEgressRate_Type())
cucsEpqosEgressRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosEgressRate.setStatus(_A)
_CucsEpqosEgressOperPrio_Type=CucsQosPriority
_CucsEpqosEgressOperPrio_Object=MibTableColumn
cucsEpqosEgressOperPrio=_CucsEpqosEgressOperPrio_Object((1,3,6,1,4,1,9,9,719,1,14,5,1,9),_CucsEpqosEgressOperPrio_Type())
cucsEpqosEgressOperPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosEgressOperPrio.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmTable_Object=MibTable
cucsEpqosDefinitionDelTaskFsmTable=_CucsEpqosDefinitionDelTaskFsmTable_Object((1,3,6,1,4,1,9,9,719,1,14,6))
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmTable.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmEntry_Object=MibTableRow
cucsEpqosDefinitionDelTaskFsmEntry=_CucsEpqosDefinitionDelTaskFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,14,6,1))
cucsEpqosDefinitionDelTaskFsmEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmEntry.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmInstanceId_Type=CucsManagedObjectId
_CucsEpqosDefinitionDelTaskFsmInstanceId_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmInstanceId=_CucsEpqosDefinitionDelTaskFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,1),_CucsEpqosDefinitionDelTaskFsmInstanceId_Type())
cucsEpqosDefinitionDelTaskFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmInstanceId.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmDn_Type=CucsManagedObjectDn
_CucsEpqosDefinitionDelTaskFsmDn_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmDn=_CucsEpqosDefinitionDelTaskFsmDn_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,2),_CucsEpqosDefinitionDelTaskFsmDn_Type())
cucsEpqosDefinitionDelTaskFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmDn.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmRn_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmRn_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmRn=_CucsEpqosDefinitionDelTaskFsmRn_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,3),_CucsEpqosDefinitionDelTaskFsmRn_Type())
cucsEpqosDefinitionDelTaskFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmRn.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmCompletionTime_Type=DateAndTime
_CucsEpqosDefinitionDelTaskFsmCompletionTime_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmCompletionTime=_CucsEpqosDefinitionDelTaskFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,4),_CucsEpqosDefinitionDelTaskFsmCompletionTime_Type())
cucsEpqosDefinitionDelTaskFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmCompletionTime.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmCurrentFsm_Type=CucsEpqosDefinitionDelTaskFsmCurrentFsm
_CucsEpqosDefinitionDelTaskFsmCurrentFsm_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmCurrentFsm=_CucsEpqosDefinitionDelTaskFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,5),_CucsEpqosDefinitionDelTaskFsmCurrentFsm_Type())
cucsEpqosDefinitionDelTaskFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmCurrentFsm.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmDescrData_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmDescrData_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmDescrData=_CucsEpqosDefinitionDelTaskFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,6),_CucsEpqosDefinitionDelTaskFsmDescrData_Type())
cucsEpqosDefinitionDelTaskFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmDescrData.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsEpqosDefinitionDelTaskFsmFsmStatus_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmFsmStatus=_CucsEpqosDefinitionDelTaskFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,7),_CucsEpqosDefinitionDelTaskFsmFsmStatus_Type())
cucsEpqosDefinitionDelTaskFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmFsmStatus.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmProgress_Type=Gauge32
_CucsEpqosDefinitionDelTaskFsmProgress_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmProgress=_CucsEpqosDefinitionDelTaskFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,8),_CucsEpqosDefinitionDelTaskFsmProgress_Type())
cucsEpqosDefinitionDelTaskFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmProgress.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmRmtErrCode_Type=Gauge32
_CucsEpqosDefinitionDelTaskFsmRmtErrCode_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtErrCode=_CucsEpqosDefinitionDelTaskFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,9),_CucsEpqosDefinitionDelTaskFsmRmtErrCode_Type())
cucsEpqosDefinitionDelTaskFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmRmtErrCode.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmRmtErrDescr_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmRmtErrDescr_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtErrDescr=_CucsEpqosDefinitionDelTaskFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,10),_CucsEpqosDefinitionDelTaskFsmRmtErrDescr_Type())
cucsEpqosDefinitionDelTaskFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmRmtErrDescr.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsEpqosDefinitionDelTaskFsmRmtRslt_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtRslt=_CucsEpqosDefinitionDelTaskFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,14,6,1,11),_CucsEpqosDefinitionDelTaskFsmRmtRslt_Type())
cucsEpqosDefinitionDelTaskFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmRmtRslt.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageTable_Object=MibTable
cucsEpqosDefinitionDelTaskFsmStageTable=_CucsEpqosDefinitionDelTaskFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,14,7))
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageTable.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageEntry_Object=MibTableRow
cucsEpqosDefinitionDelTaskFsmStageEntry=_CucsEpqosDefinitionDelTaskFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,14,7,1))
cucsEpqosDefinitionDelTaskFsmStageEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageEntry.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageInstanceId_Type=CucsManagedObjectId
_CucsEpqosDefinitionDelTaskFsmStageInstanceId_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageInstanceId=_CucsEpqosDefinitionDelTaskFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,14,7,1,1),_CucsEpqosDefinitionDelTaskFsmStageInstanceId_Type())
cucsEpqosDefinitionDelTaskFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageInstanceId.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageDn_Type=CucsManagedObjectDn
_CucsEpqosDefinitionDelTaskFsmStageDn_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageDn=_CucsEpqosDefinitionDelTaskFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,14,7,1,2),_CucsEpqosDefinitionDelTaskFsmStageDn_Type())
cucsEpqosDefinitionDelTaskFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageDn.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageRn_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmStageRn_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageRn=_CucsEpqosDefinitionDelTaskFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,14,7,1,3),_CucsEpqosDefinitionDelTaskFsmStageRn_Type())
cucsEpqosDefinitionDelTaskFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageRn.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageDescrData_Type=SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmStageDescrData_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageDescrData=_CucsEpqosDefinitionDelTaskFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,14,7,1,4),_CucsEpqosDefinitionDelTaskFsmStageDescrData_Type())
cucsEpqosDefinitionDelTaskFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageDescrData.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageLastUpdateTime_Type=DateAndTime
_CucsEpqosDefinitionDelTaskFsmStageLastUpdateTime_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime=_CucsEpqosDefinitionDelTaskFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,14,7,1,5),_CucsEpqosDefinitionDelTaskFsmStageLastUpdateTime_Type())
cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageName_Type=CucsEpqosDefinitionDelTaskFsmStageName
_CucsEpqosDefinitionDelTaskFsmStageName_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageName=_CucsEpqosDefinitionDelTaskFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,14,7,1,6),_CucsEpqosDefinitionDelTaskFsmStageName_Type())
cucsEpqosDefinitionDelTaskFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageName.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageOrder_Type=Gauge32
_CucsEpqosDefinitionDelTaskFsmStageOrder_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageOrder=_CucsEpqosDefinitionDelTaskFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,14,7,1,7),_CucsEpqosDefinitionDelTaskFsmStageOrder_Type())
cucsEpqosDefinitionDelTaskFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageOrder.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageRetry_Type=Gauge32
_CucsEpqosDefinitionDelTaskFsmStageRetry_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageRetry=_CucsEpqosDefinitionDelTaskFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,14,7,1,8),_CucsEpqosDefinitionDelTaskFsmStageRetry_Type())
cucsEpqosDefinitionDelTaskFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageRetry.setStatus(_A)
_CucsEpqosDefinitionDelTaskFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsEpqosDefinitionDelTaskFsmStageStageStatus_Object=MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageStageStatus=_CucsEpqosDefinitionDelTaskFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,14,7,1,9),_CucsEpqosDefinitionDelTaskFsmStageStageStatus_Type())
cucsEpqosDefinitionDelTaskFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionDelTaskFsmStageStageStatus.setStatus(_A)
_CucsEpqosDefinitionFsmTable_Object=MibTable
cucsEpqosDefinitionFsmTable=_CucsEpqosDefinitionFsmTable_Object((1,3,6,1,4,1,9,9,719,1,14,8))
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmTable.setStatus(_A)
_CucsEpqosDefinitionFsmEntry_Object=MibTableRow
cucsEpqosDefinitionFsmEntry=_CucsEpqosDefinitionFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,14,8,1))
cucsEpqosDefinitionFsmEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmEntry.setStatus(_A)
_CucsEpqosDefinitionFsmInstanceId_Type=CucsManagedObjectId
_CucsEpqosDefinitionFsmInstanceId_Object=MibTableColumn
cucsEpqosDefinitionFsmInstanceId=_CucsEpqosDefinitionFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,1),_CucsEpqosDefinitionFsmInstanceId_Type())
cucsEpqosDefinitionFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmInstanceId.setStatus(_A)
_CucsEpqosDefinitionFsmDn_Type=CucsManagedObjectDn
_CucsEpqosDefinitionFsmDn_Object=MibTableColumn
cucsEpqosDefinitionFsmDn=_CucsEpqosDefinitionFsmDn_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,2),_CucsEpqosDefinitionFsmDn_Type())
cucsEpqosDefinitionFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmDn.setStatus(_A)
_CucsEpqosDefinitionFsmRn_Type=SnmpAdminString
_CucsEpqosDefinitionFsmRn_Object=MibTableColumn
cucsEpqosDefinitionFsmRn=_CucsEpqosDefinitionFsmRn_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,3),_CucsEpqosDefinitionFsmRn_Type())
cucsEpqosDefinitionFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmRn.setStatus(_A)
_CucsEpqosDefinitionFsmCompletionTime_Type=DateAndTime
_CucsEpqosDefinitionFsmCompletionTime_Object=MibTableColumn
cucsEpqosDefinitionFsmCompletionTime=_CucsEpqosDefinitionFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,4),_CucsEpqosDefinitionFsmCompletionTime_Type())
cucsEpqosDefinitionFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmCompletionTime.setStatus(_A)
_CucsEpqosDefinitionFsmCurrentFsm_Type=CucsEpqosDefinitionFsmCurrentFsm
_CucsEpqosDefinitionFsmCurrentFsm_Object=MibTableColumn
cucsEpqosDefinitionFsmCurrentFsm=_CucsEpqosDefinitionFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,5),_CucsEpqosDefinitionFsmCurrentFsm_Type())
cucsEpqosDefinitionFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmCurrentFsm.setStatus(_A)
_CucsEpqosDefinitionFsmDescrData_Type=SnmpAdminString
_CucsEpqosDefinitionFsmDescrData_Object=MibTableColumn
cucsEpqosDefinitionFsmDescrData=_CucsEpqosDefinitionFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,6),_CucsEpqosDefinitionFsmDescrData_Type())
cucsEpqosDefinitionFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmDescrData.setStatus(_A)
_CucsEpqosDefinitionFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsEpqosDefinitionFsmFsmStatus_Object=MibTableColumn
cucsEpqosDefinitionFsmFsmStatus=_CucsEpqosDefinitionFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,7),_CucsEpqosDefinitionFsmFsmStatus_Type())
cucsEpqosDefinitionFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmFsmStatus.setStatus(_A)
_CucsEpqosDefinitionFsmProgress_Type=Gauge32
_CucsEpqosDefinitionFsmProgress_Object=MibTableColumn
cucsEpqosDefinitionFsmProgress=_CucsEpqosDefinitionFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,8),_CucsEpqosDefinitionFsmProgress_Type())
cucsEpqosDefinitionFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmProgress.setStatus(_A)
_CucsEpqosDefinitionFsmRmtErrCode_Type=Gauge32
_CucsEpqosDefinitionFsmRmtErrCode_Object=MibTableColumn
cucsEpqosDefinitionFsmRmtErrCode=_CucsEpqosDefinitionFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,9),_CucsEpqosDefinitionFsmRmtErrCode_Type())
cucsEpqosDefinitionFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmRmtErrCode.setStatus(_A)
_CucsEpqosDefinitionFsmRmtErrDescr_Type=SnmpAdminString
_CucsEpqosDefinitionFsmRmtErrDescr_Object=MibTableColumn
cucsEpqosDefinitionFsmRmtErrDescr=_CucsEpqosDefinitionFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,10),_CucsEpqosDefinitionFsmRmtErrDescr_Type())
cucsEpqosDefinitionFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmRmtErrDescr.setStatus(_A)
_CucsEpqosDefinitionFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsEpqosDefinitionFsmRmtRslt_Object=MibTableColumn
cucsEpqosDefinitionFsmRmtRslt=_CucsEpqosDefinitionFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,14,8,1,11),_CucsEpqosDefinitionFsmRmtRslt_Type())
cucsEpqosDefinitionFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmRmtRslt.setStatus(_A)
_CucsEpqosDefinitionFsmStageTable_Object=MibTable
cucsEpqosDefinitionFsmStageTable=_CucsEpqosDefinitionFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,14,9))
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageTable.setStatus(_A)
_CucsEpqosDefinitionFsmStageEntry_Object=MibTableRow
cucsEpqosDefinitionFsmStageEntry=_CucsEpqosDefinitionFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,14,9,1))
cucsEpqosDefinitionFsmStageEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageEntry.setStatus(_A)
_CucsEpqosDefinitionFsmStageInstanceId_Type=CucsManagedObjectId
_CucsEpqosDefinitionFsmStageInstanceId_Object=MibTableColumn
cucsEpqosDefinitionFsmStageInstanceId=_CucsEpqosDefinitionFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,14,9,1,1),_CucsEpqosDefinitionFsmStageInstanceId_Type())
cucsEpqosDefinitionFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageInstanceId.setStatus(_A)
_CucsEpqosDefinitionFsmStageDn_Type=CucsManagedObjectDn
_CucsEpqosDefinitionFsmStageDn_Object=MibTableColumn
cucsEpqosDefinitionFsmStageDn=_CucsEpqosDefinitionFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,14,9,1,2),_CucsEpqosDefinitionFsmStageDn_Type())
cucsEpqosDefinitionFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageDn.setStatus(_A)
_CucsEpqosDefinitionFsmStageRn_Type=SnmpAdminString
_CucsEpqosDefinitionFsmStageRn_Object=MibTableColumn
cucsEpqosDefinitionFsmStageRn=_CucsEpqosDefinitionFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,14,9,1,3),_CucsEpqosDefinitionFsmStageRn_Type())
cucsEpqosDefinitionFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageRn.setStatus(_A)
_CucsEpqosDefinitionFsmStageDescrData_Type=SnmpAdminString
_CucsEpqosDefinitionFsmStageDescrData_Object=MibTableColumn
cucsEpqosDefinitionFsmStageDescrData=_CucsEpqosDefinitionFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,14,9,1,4),_CucsEpqosDefinitionFsmStageDescrData_Type())
cucsEpqosDefinitionFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageDescrData.setStatus(_A)
_CucsEpqosDefinitionFsmStageLastUpdateTime_Type=DateAndTime
_CucsEpqosDefinitionFsmStageLastUpdateTime_Object=MibTableColumn
cucsEpqosDefinitionFsmStageLastUpdateTime=_CucsEpqosDefinitionFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,14,9,1,5),_CucsEpqosDefinitionFsmStageLastUpdateTime_Type())
cucsEpqosDefinitionFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageLastUpdateTime.setStatus(_A)
_CucsEpqosDefinitionFsmStageName_Type=CucsEpqosDefinitionFsmStageName
_CucsEpqosDefinitionFsmStageName_Object=MibTableColumn
cucsEpqosDefinitionFsmStageName=_CucsEpqosDefinitionFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,14,9,1,6),_CucsEpqosDefinitionFsmStageName_Type())
cucsEpqosDefinitionFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageName.setStatus(_A)
_CucsEpqosDefinitionFsmStageOrder_Type=Gauge32
_CucsEpqosDefinitionFsmStageOrder_Object=MibTableColumn
cucsEpqosDefinitionFsmStageOrder=_CucsEpqosDefinitionFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,14,9,1,7),_CucsEpqosDefinitionFsmStageOrder_Type())
cucsEpqosDefinitionFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageOrder.setStatus(_A)
_CucsEpqosDefinitionFsmStageRetry_Type=Gauge32
_CucsEpqosDefinitionFsmStageRetry_Object=MibTableColumn
cucsEpqosDefinitionFsmStageRetry=_CucsEpqosDefinitionFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,14,9,1,8),_CucsEpqosDefinitionFsmStageRetry_Type())
cucsEpqosDefinitionFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageRetry.setStatus(_A)
_CucsEpqosDefinitionFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsEpqosDefinitionFsmStageStageStatus_Object=MibTableColumn
cucsEpqosDefinitionFsmStageStageStatus=_CucsEpqosDefinitionFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,14,9,1,9),_CucsEpqosDefinitionFsmStageStageStatus_Type())
cucsEpqosDefinitionFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEpqosDefinitionFsmStageStageStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsEpqosObjects':cucsEpqosObjects,'cucsEpqosDefinitionTable':cucsEpqosDefinitionTable,'cucsEpqosDefinitionEntry':cucsEpqosDefinitionEntry,_E:cucsEpqosDefinitionInstanceId,'cucsEpqosDefinitionDn':cucsEpqosDefinitionDn,'cucsEpqosDefinitionRn':cucsEpqosDefinitionRn,'cucsEpqosDefinitionDescr':cucsEpqosDefinitionDescr,'cucsEpqosDefinitionFsmDescr':cucsEpqosDefinitionFsmDescr,'cucsEpqosDefinitionFsmPrev':cucsEpqosDefinitionFsmPrev,'cucsEpqosDefinitionFsmProgr':cucsEpqosDefinitionFsmProgr,'cucsEpqosDefinitionFsmRmtInvErrCode':cucsEpqosDefinitionFsmRmtInvErrCode,'cucsEpqosDefinitionFsmRmtInvErrDescr':cucsEpqosDefinitionFsmRmtInvErrDescr,'cucsEpqosDefinitionFsmRmtInvRslt':cucsEpqosDefinitionFsmRmtInvRslt,'cucsEpqosDefinitionFsmStageDescr':cucsEpqosDefinitionFsmStageDescr,'cucsEpqosDefinitionFsmStamp':cucsEpqosDefinitionFsmStamp,'cucsEpqosDefinitionFsmStatus':cucsEpqosDefinitionFsmStatus,'cucsEpqosDefinitionFsmTry':cucsEpqosDefinitionFsmTry,'cucsEpqosDefinitionIntId':cucsEpqosDefinitionIntId,'cucsEpqosDefinitionName':cucsEpqosDefinitionName,'cucsEpqosDefinitionPolicyLevel':cucsEpqosDefinitionPolicyLevel,'cucsEpqosDefinitionPolicyOwner':cucsEpqosDefinitionPolicyOwner,'cucsEpqosDefinitionDelTaskTable':cucsEpqosDefinitionDelTaskTable,'cucsEpqosDefinitionDelTaskEntry':cucsEpqosDefinitionDelTaskEntry,_F:cucsEpqosDefinitionDelTaskInstanceId,'cucsEpqosDefinitionDelTaskDn':cucsEpqosDefinitionDelTaskDn,'cucsEpqosDefinitionDelTaskRn':cucsEpqosDefinitionDelTaskRn,'cucsEpqosDefinitionDelTaskDefIntId':cucsEpqosDefinitionDelTaskDefIntId,'cucsEpqosDefinitionDelTaskDescr':cucsEpqosDefinitionDelTaskDescr,'cucsEpqosDefinitionDelTaskFsmDescr':cucsEpqosDefinitionDelTaskFsmDescr,'cucsEpqosDefinitionDelTaskFsmPrev':cucsEpqosDefinitionDelTaskFsmPrev,'cucsEpqosDefinitionDelTaskFsmProgr':cucsEpqosDefinitionDelTaskFsmProgr,'cucsEpqosDefinitionDelTaskFsmRmtInvErrCode':cucsEpqosDefinitionDelTaskFsmRmtInvErrCode,'cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr':cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr,'cucsEpqosDefinitionDelTaskFsmRmtInvRslt':cucsEpqosDefinitionDelTaskFsmRmtInvRslt,'cucsEpqosDefinitionDelTaskFsmStageDescr':cucsEpqosDefinitionDelTaskFsmStageDescr,'cucsEpqosDefinitionDelTaskFsmStamp':cucsEpqosDefinitionDelTaskFsmStamp,'cucsEpqosDefinitionDelTaskFsmStatus':cucsEpqosDefinitionDelTaskFsmStatus,'cucsEpqosDefinitionDelTaskFsmTry':cucsEpqosDefinitionDelTaskFsmTry,'cucsEpqosDefinitionDelTaskIntId':cucsEpqosDefinitionDelTaskIntId,'cucsEpqosDefinitionDelTaskName':cucsEpqosDefinitionDelTaskName,'cucsEpqosDefinitionDelTaskDefDn':cucsEpqosDefinitionDelTaskDefDn,'cucsEpqosDefinitionDelTaskPolicyLevel':cucsEpqosDefinitionDelTaskPolicyLevel,'cucsEpqosDefinitionDelTaskPolicyOwner':cucsEpqosDefinitionDelTaskPolicyOwner,'cucsEpqosDefinitionDelTaskFsmTaskTable':cucsEpqosDefinitionDelTaskFsmTaskTable,'cucsEpqosDefinitionDelTaskFsmTaskEntry':cucsEpqosDefinitionDelTaskFsmTaskEntry,_G:cucsEpqosDefinitionDelTaskFsmTaskInstanceId,'cucsEpqosDefinitionDelTaskFsmTaskDn':cucsEpqosDefinitionDelTaskFsmTaskDn,'cucsEpqosDefinitionDelTaskFsmTaskRn':cucsEpqosDefinitionDelTaskFsmTaskRn,'cucsEpqosDefinitionDelTaskFsmTaskCompletion':cucsEpqosDefinitionDelTaskFsmTaskCompletion,'cucsEpqosDefinitionDelTaskFsmTaskFlags':cucsEpqosDefinitionDelTaskFsmTaskFlags,'cucsEpqosDefinitionDelTaskFsmTaskItem':cucsEpqosDefinitionDelTaskFsmTaskItem,'cucsEpqosDefinitionDelTaskFsmTaskSeqId':cucsEpqosDefinitionDelTaskFsmTaskSeqId,'cucsEpqosDefinitionFsmTaskTable':cucsEpqosDefinitionFsmTaskTable,'cucsEpqosDefinitionFsmTaskEntry':cucsEpqosDefinitionFsmTaskEntry,_H:cucsEpqosDefinitionFsmTaskInstanceId,'cucsEpqosDefinitionFsmTaskDn':cucsEpqosDefinitionFsmTaskDn,'cucsEpqosDefinitionFsmTaskRn':cucsEpqosDefinitionFsmTaskRn,'cucsEpqosDefinitionFsmTaskCompletion':cucsEpqosDefinitionFsmTaskCompletion,'cucsEpqosDefinitionFsmTaskFlags':cucsEpqosDefinitionFsmTaskFlags,'cucsEpqosDefinitionFsmTaskItem':cucsEpqosDefinitionFsmTaskItem,'cucsEpqosDefinitionFsmTaskSeqId':cucsEpqosDefinitionFsmTaskSeqId,'cucsEpqosEgressTable':cucsEpqosEgressTable,'cucsEpqosEgressEntry':cucsEpqosEgressEntry,_I:cucsEpqosEgressInstanceId,'cucsEpqosEgressDn':cucsEpqosEgressDn,'cucsEpqosEgressRn':cucsEpqosEgressRn,'cucsEpqosEgressBurst':cucsEpqosEgressBurst,'cucsEpqosEgressHostControl':cucsEpqosEgressHostControl,'cucsEpqosEgressName':cucsEpqosEgressName,'cucsEpqosEgressPrio':cucsEpqosEgressPrio,'cucsEpqosEgressRate':cucsEpqosEgressRate,'cucsEpqosEgressOperPrio':cucsEpqosEgressOperPrio,'cucsEpqosDefinitionDelTaskFsmTable':cucsEpqosDefinitionDelTaskFsmTable,'cucsEpqosDefinitionDelTaskFsmEntry':cucsEpqosDefinitionDelTaskFsmEntry,_J:cucsEpqosDefinitionDelTaskFsmInstanceId,'cucsEpqosDefinitionDelTaskFsmDn':cucsEpqosDefinitionDelTaskFsmDn,'cucsEpqosDefinitionDelTaskFsmRn':cucsEpqosDefinitionDelTaskFsmRn,'cucsEpqosDefinitionDelTaskFsmCompletionTime':cucsEpqosDefinitionDelTaskFsmCompletionTime,'cucsEpqosDefinitionDelTaskFsmCurrentFsm':cucsEpqosDefinitionDelTaskFsmCurrentFsm,'cucsEpqosDefinitionDelTaskFsmDescrData':cucsEpqosDefinitionDelTaskFsmDescrData,'cucsEpqosDefinitionDelTaskFsmFsmStatus':cucsEpqosDefinitionDelTaskFsmFsmStatus,'cucsEpqosDefinitionDelTaskFsmProgress':cucsEpqosDefinitionDelTaskFsmProgress,'cucsEpqosDefinitionDelTaskFsmRmtErrCode':cucsEpqosDefinitionDelTaskFsmRmtErrCode,'cucsEpqosDefinitionDelTaskFsmRmtErrDescr':cucsEpqosDefinitionDelTaskFsmRmtErrDescr,'cucsEpqosDefinitionDelTaskFsmRmtRslt':cucsEpqosDefinitionDelTaskFsmRmtRslt,'cucsEpqosDefinitionDelTaskFsmStageTable':cucsEpqosDefinitionDelTaskFsmStageTable,'cucsEpqosDefinitionDelTaskFsmStageEntry':cucsEpqosDefinitionDelTaskFsmStageEntry,_K:cucsEpqosDefinitionDelTaskFsmStageInstanceId,'cucsEpqosDefinitionDelTaskFsmStageDn':cucsEpqosDefinitionDelTaskFsmStageDn,'cucsEpqosDefinitionDelTaskFsmStageRn':cucsEpqosDefinitionDelTaskFsmStageRn,'cucsEpqosDefinitionDelTaskFsmStageDescrData':cucsEpqosDefinitionDelTaskFsmStageDescrData,'cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime':cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime,'cucsEpqosDefinitionDelTaskFsmStageName':cucsEpqosDefinitionDelTaskFsmStageName,'cucsEpqosDefinitionDelTaskFsmStageOrder':cucsEpqosDefinitionDelTaskFsmStageOrder,'cucsEpqosDefinitionDelTaskFsmStageRetry':cucsEpqosDefinitionDelTaskFsmStageRetry,'cucsEpqosDefinitionDelTaskFsmStageStageStatus':cucsEpqosDefinitionDelTaskFsmStageStageStatus,'cucsEpqosDefinitionFsmTable':cucsEpqosDefinitionFsmTable,'cucsEpqosDefinitionFsmEntry':cucsEpqosDefinitionFsmEntry,_L:cucsEpqosDefinitionFsmInstanceId,'cucsEpqosDefinitionFsmDn':cucsEpqosDefinitionFsmDn,'cucsEpqosDefinitionFsmRn':cucsEpqosDefinitionFsmRn,'cucsEpqosDefinitionFsmCompletionTime':cucsEpqosDefinitionFsmCompletionTime,'cucsEpqosDefinitionFsmCurrentFsm':cucsEpqosDefinitionFsmCurrentFsm,'cucsEpqosDefinitionFsmDescrData':cucsEpqosDefinitionFsmDescrData,'cucsEpqosDefinitionFsmFsmStatus':cucsEpqosDefinitionFsmFsmStatus,'cucsEpqosDefinitionFsmProgress':cucsEpqosDefinitionFsmProgress,'cucsEpqosDefinitionFsmRmtErrCode':cucsEpqosDefinitionFsmRmtErrCode,'cucsEpqosDefinitionFsmRmtErrDescr':cucsEpqosDefinitionFsmRmtErrDescr,'cucsEpqosDefinitionFsmRmtRslt':cucsEpqosDefinitionFsmRmtRslt,'cucsEpqosDefinitionFsmStageTable':cucsEpqosDefinitionFsmStageTable,'cucsEpqosDefinitionFsmStageEntry':cucsEpqosDefinitionFsmStageEntry,_M:cucsEpqosDefinitionFsmStageInstanceId,'cucsEpqosDefinitionFsmStageDn':cucsEpqosDefinitionFsmStageDn,'cucsEpqosDefinitionFsmStageRn':cucsEpqosDefinitionFsmStageRn,'cucsEpqosDefinitionFsmStageDescrData':cucsEpqosDefinitionFsmStageDescrData,'cucsEpqosDefinitionFsmStageLastUpdateTime':cucsEpqosDefinitionFsmStageLastUpdateTime,'cucsEpqosDefinitionFsmStageName':cucsEpqosDefinitionFsmStageName,'cucsEpqosDefinitionFsmStageOrder':cucsEpqosDefinitionFsmStageOrder,'cucsEpqosDefinitionFsmStageRetry':cucsEpqosDefinitionFsmStageRetry,'cucsEpqosDefinitionFsmStageStageStatus':cucsEpqosDefinitionFsmStageStageStatus})