_K='cfprQosclassFcInstanceId'
_J='cfprQosclassEthClassifiedInstanceId'
_I='cfprQosclassEthBEInstanceId'
_H='cfprQosclassDefinitionFsmTaskInstanceId'
_G='cfprQosclassDefinitionFsmStageInstanceId'
_F='cfprQosclassDefinitionFsmInstanceId'
_E='cfprQosclassDefinitionInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-QOSCLASS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprConditionRemoteInvRslt,CfprFsmCompletion,CfprFsmFlags,CfprFsmFsmStageStatus,CfprPolicyPolicyOwner,CfprQosclassDefinitionFsmCurrentFsm,CfprQosclassDefinitionFsmStageName,CfprQosclassDefinitionFsmTaskItem,CfprQosclassEthBEAdminState,CfprQosclassEthBEDrop,CfprQosclassEthBEPriority,CfprQosclassEthClassifiedAdminState,CfprQosclassEthClassifiedDrop,CfprQosclassEthClassifiedPriority,CfprQosclassFcAdminState,CfprQosclassFcDrop,CfprQosclassFcPriority=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprConditionRemoteInvRslt','CfprFsmCompletion','CfprFsmFlags','CfprFsmFsmStageStatus','CfprPolicyPolicyOwner','CfprQosclassDefinitionFsmCurrentFsm','CfprQosclassDefinitionFsmStageName','CfprQosclassDefinitionFsmTaskItem','CfprQosclassEthBEAdminState','CfprQosclassEthBEDrop','CfprQosclassEthBEPriority','CfprQosclassEthClassifiedAdminState','CfprQosclassEthClassifiedDrop','CfprQosclassEthClassifiedPriority','CfprQosclassFcAdminState','CfprQosclassFcDrop','CfprQosclassFcPriority')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprQosclassObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,67))
_CfprQosclassDefinitionTable_Object=MibTable
cfprQosclassDefinitionTable=_CfprQosclassDefinitionTable_Object((1,3,6,1,4,1,9,9,826,1,67,1))
if mibBuilder.loadTexts:cfprQosclassDefinitionTable.setStatus(_A)
_CfprQosclassDefinitionEntry_Object=MibTableRow
cfprQosclassDefinitionEntry=_CfprQosclassDefinitionEntry_Object((1,3,6,1,4,1,9,9,826,1,67,1,1))
cfprQosclassDefinitionEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprQosclassDefinitionEntry.setStatus(_A)
_CfprQosclassDefinitionInstanceId_Type=CfprManagedObjectId
_CfprQosclassDefinitionInstanceId_Object=MibTableColumn
cfprQosclassDefinitionInstanceId=_CfprQosclassDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,1),_CfprQosclassDefinitionInstanceId_Type())
cfprQosclassDefinitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprQosclassDefinitionInstanceId.setStatus(_A)
_CfprQosclassDefinitionDn_Type=CfprManagedObjectDn
_CfprQosclassDefinitionDn_Object=MibTableColumn
cfprQosclassDefinitionDn=_CfprQosclassDefinitionDn_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,2),_CfprQosclassDefinitionDn_Type())
cfprQosclassDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionDn.setStatus(_A)
_CfprQosclassDefinitionRn_Type=SnmpAdminString
_CfprQosclassDefinitionRn_Object=MibTableColumn
cfprQosclassDefinitionRn=_CfprQosclassDefinitionRn_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,3),_CfprQosclassDefinitionRn_Type())
cfprQosclassDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionRn.setStatus(_A)
_CfprQosclassDefinitionDescr_Type=SnmpAdminString
_CfprQosclassDefinitionDescr_Object=MibTableColumn
cfprQosclassDefinitionDescr=_CfprQosclassDefinitionDescr_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,4),_CfprQosclassDefinitionDescr_Type())
cfprQosclassDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionDescr.setStatus(_A)
_CfprQosclassDefinitionFsmDescr_Type=SnmpAdminString
_CfprQosclassDefinitionFsmDescr_Object=MibTableColumn
cfprQosclassDefinitionFsmDescr=_CfprQosclassDefinitionFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,5),_CfprQosclassDefinitionFsmDescr_Type())
cfprQosclassDefinitionFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmDescr.setStatus(_A)
_CfprQosclassDefinitionFsmPrev_Type=SnmpAdminString
_CfprQosclassDefinitionFsmPrev_Object=MibTableColumn
cfprQosclassDefinitionFsmPrev=_CfprQosclassDefinitionFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,6),_CfprQosclassDefinitionFsmPrev_Type())
cfprQosclassDefinitionFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmPrev.setStatus(_A)
_CfprQosclassDefinitionFsmProgr_Type=Gauge32
_CfprQosclassDefinitionFsmProgr_Object=MibTableColumn
cfprQosclassDefinitionFsmProgr=_CfprQosclassDefinitionFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,7),_CfprQosclassDefinitionFsmProgr_Type())
cfprQosclassDefinitionFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmProgr.setStatus(_A)
_CfprQosclassDefinitionFsmRmtInvErrCode_Type=Gauge32
_CfprQosclassDefinitionFsmRmtInvErrCode_Object=MibTableColumn
cfprQosclassDefinitionFsmRmtInvErrCode=_CfprQosclassDefinitionFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,8),_CfprQosclassDefinitionFsmRmtInvErrCode_Type())
cfprQosclassDefinitionFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmRmtInvErrCode.setStatus(_A)
_CfprQosclassDefinitionFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprQosclassDefinitionFsmRmtInvErrDescr_Object=MibTableColumn
cfprQosclassDefinitionFsmRmtInvErrDescr=_CfprQosclassDefinitionFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,9),_CfprQosclassDefinitionFsmRmtInvErrDescr_Type())
cfprQosclassDefinitionFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmRmtInvErrDescr.setStatus(_A)
_CfprQosclassDefinitionFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprQosclassDefinitionFsmRmtInvRslt_Object=MibTableColumn
cfprQosclassDefinitionFsmRmtInvRslt=_CfprQosclassDefinitionFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,10),_CfprQosclassDefinitionFsmRmtInvRslt_Type())
cfprQosclassDefinitionFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmRmtInvRslt.setStatus(_A)
_CfprQosclassDefinitionFsmStageDescr_Type=SnmpAdminString
_CfprQosclassDefinitionFsmStageDescr_Object=MibTableColumn
cfprQosclassDefinitionFsmStageDescr=_CfprQosclassDefinitionFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,11),_CfprQosclassDefinitionFsmStageDescr_Type())
cfprQosclassDefinitionFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageDescr.setStatus(_A)
_CfprQosclassDefinitionFsmStamp_Type=DateAndTime
_CfprQosclassDefinitionFsmStamp_Object=MibTableColumn
cfprQosclassDefinitionFsmStamp=_CfprQosclassDefinitionFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,12),_CfprQosclassDefinitionFsmStamp_Type())
cfprQosclassDefinitionFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStamp.setStatus(_A)
_CfprQosclassDefinitionFsmStatus_Type=SnmpAdminString
_CfprQosclassDefinitionFsmStatus_Object=MibTableColumn
cfprQosclassDefinitionFsmStatus=_CfprQosclassDefinitionFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,13),_CfprQosclassDefinitionFsmStatus_Type())
cfprQosclassDefinitionFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStatus.setStatus(_A)
_CfprQosclassDefinitionFsmTry_Type=Gauge32
_CfprQosclassDefinitionFsmTry_Object=MibTableColumn
cfprQosclassDefinitionFsmTry=_CfprQosclassDefinitionFsmTry_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,14),_CfprQosclassDefinitionFsmTry_Type())
cfprQosclassDefinitionFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTry.setStatus(_A)
_CfprQosclassDefinitionIntId_Type=SnmpAdminString
_CfprQosclassDefinitionIntId_Object=MibTableColumn
cfprQosclassDefinitionIntId=_CfprQosclassDefinitionIntId_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,15),_CfprQosclassDefinitionIntId_Type())
cfprQosclassDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionIntId.setStatus(_A)
_CfprQosclassDefinitionName_Type=SnmpAdminString
_CfprQosclassDefinitionName_Object=MibTableColumn
cfprQosclassDefinitionName=_CfprQosclassDefinitionName_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,16),_CfprQosclassDefinitionName_Type())
cfprQosclassDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionName.setStatus(_A)
_CfprQosclassDefinitionPolicyLevel_Type=Gauge32
_CfprQosclassDefinitionPolicyLevel_Object=MibTableColumn
cfprQosclassDefinitionPolicyLevel=_CfprQosclassDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,17),_CfprQosclassDefinitionPolicyLevel_Type())
cfprQosclassDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionPolicyLevel.setStatus(_A)
_CfprQosclassDefinitionPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprQosclassDefinitionPolicyOwner_Object=MibTableColumn
cfprQosclassDefinitionPolicyOwner=_CfprQosclassDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,67,1,1,18),_CfprQosclassDefinitionPolicyOwner_Type())
cfprQosclassDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionPolicyOwner.setStatus(_A)
_CfprQosclassDefinitionFsmTable_Object=MibTable
cfprQosclassDefinitionFsmTable=_CfprQosclassDefinitionFsmTable_Object((1,3,6,1,4,1,9,9,826,1,67,2))
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTable.setStatus(_A)
_CfprQosclassDefinitionFsmEntry_Object=MibTableRow
cfprQosclassDefinitionFsmEntry=_CfprQosclassDefinitionFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,67,2,1))
cfprQosclassDefinitionFsmEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmEntry.setStatus(_A)
_CfprQosclassDefinitionFsmInstanceId_Type=CfprManagedObjectId
_CfprQosclassDefinitionFsmInstanceId_Object=MibTableColumn
cfprQosclassDefinitionFsmInstanceId=_CfprQosclassDefinitionFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,1),_CfprQosclassDefinitionFsmInstanceId_Type())
cfprQosclassDefinitionFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmInstanceId.setStatus(_A)
_CfprQosclassDefinitionFsmDn_Type=CfprManagedObjectDn
_CfprQosclassDefinitionFsmDn_Object=MibTableColumn
cfprQosclassDefinitionFsmDn=_CfprQosclassDefinitionFsmDn_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,2),_CfprQosclassDefinitionFsmDn_Type())
cfprQosclassDefinitionFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmDn.setStatus(_A)
_CfprQosclassDefinitionFsmRn_Type=SnmpAdminString
_CfprQosclassDefinitionFsmRn_Object=MibTableColumn
cfprQosclassDefinitionFsmRn=_CfprQosclassDefinitionFsmRn_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,3),_CfprQosclassDefinitionFsmRn_Type())
cfprQosclassDefinitionFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmRn.setStatus(_A)
_CfprQosclassDefinitionFsmCompletionTime_Type=DateAndTime
_CfprQosclassDefinitionFsmCompletionTime_Object=MibTableColumn
cfprQosclassDefinitionFsmCompletionTime=_CfprQosclassDefinitionFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,4),_CfprQosclassDefinitionFsmCompletionTime_Type())
cfprQosclassDefinitionFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmCompletionTime.setStatus(_A)
_CfprQosclassDefinitionFsmCurrentFsm_Type=CfprQosclassDefinitionFsmCurrentFsm
_CfprQosclassDefinitionFsmCurrentFsm_Object=MibTableColumn
cfprQosclassDefinitionFsmCurrentFsm=_CfprQosclassDefinitionFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,5),_CfprQosclassDefinitionFsmCurrentFsm_Type())
cfprQosclassDefinitionFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmCurrentFsm.setStatus(_A)
_CfprQosclassDefinitionFsmDescrData_Type=SnmpAdminString
_CfprQosclassDefinitionFsmDescrData_Object=MibTableColumn
cfprQosclassDefinitionFsmDescrData=_CfprQosclassDefinitionFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,6),_CfprQosclassDefinitionFsmDescrData_Type())
cfprQosclassDefinitionFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmDescrData.setStatus(_A)
_CfprQosclassDefinitionFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprQosclassDefinitionFsmFsmStatus_Object=MibTableColumn
cfprQosclassDefinitionFsmFsmStatus=_CfprQosclassDefinitionFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,7),_CfprQosclassDefinitionFsmFsmStatus_Type())
cfprQosclassDefinitionFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmFsmStatus.setStatus(_A)
_CfprQosclassDefinitionFsmProgress_Type=Gauge32
_CfprQosclassDefinitionFsmProgress_Object=MibTableColumn
cfprQosclassDefinitionFsmProgress=_CfprQosclassDefinitionFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,8),_CfprQosclassDefinitionFsmProgress_Type())
cfprQosclassDefinitionFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmProgress.setStatus(_A)
_CfprQosclassDefinitionFsmRmtErrCode_Type=Gauge32
_CfprQosclassDefinitionFsmRmtErrCode_Object=MibTableColumn
cfprQosclassDefinitionFsmRmtErrCode=_CfprQosclassDefinitionFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,9),_CfprQosclassDefinitionFsmRmtErrCode_Type())
cfprQosclassDefinitionFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmRmtErrCode.setStatus(_A)
_CfprQosclassDefinitionFsmRmtErrDescr_Type=SnmpAdminString
_CfprQosclassDefinitionFsmRmtErrDescr_Object=MibTableColumn
cfprQosclassDefinitionFsmRmtErrDescr=_CfprQosclassDefinitionFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,10),_CfprQosclassDefinitionFsmRmtErrDescr_Type())
cfprQosclassDefinitionFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmRmtErrDescr.setStatus(_A)
_CfprQosclassDefinitionFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprQosclassDefinitionFsmRmtRslt_Object=MibTableColumn
cfprQosclassDefinitionFsmRmtRslt=_CfprQosclassDefinitionFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,67,2,1,11),_CfprQosclassDefinitionFsmRmtRslt_Type())
cfprQosclassDefinitionFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmRmtRslt.setStatus(_A)
_CfprQosclassDefinitionFsmStageTable_Object=MibTable
cfprQosclassDefinitionFsmStageTable=_CfprQosclassDefinitionFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,67,3))
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageTable.setStatus(_A)
_CfprQosclassDefinitionFsmStageEntry_Object=MibTableRow
cfprQosclassDefinitionFsmStageEntry=_CfprQosclassDefinitionFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,67,3,1))
cfprQosclassDefinitionFsmStageEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageEntry.setStatus(_A)
_CfprQosclassDefinitionFsmStageInstanceId_Type=CfprManagedObjectId
_CfprQosclassDefinitionFsmStageInstanceId_Object=MibTableColumn
cfprQosclassDefinitionFsmStageInstanceId=_CfprQosclassDefinitionFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,67,3,1,1),_CfprQosclassDefinitionFsmStageInstanceId_Type())
cfprQosclassDefinitionFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageInstanceId.setStatus(_A)
_CfprQosclassDefinitionFsmStageDn_Type=CfprManagedObjectDn
_CfprQosclassDefinitionFsmStageDn_Object=MibTableColumn
cfprQosclassDefinitionFsmStageDn=_CfprQosclassDefinitionFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,67,3,1,2),_CfprQosclassDefinitionFsmStageDn_Type())
cfprQosclassDefinitionFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageDn.setStatus(_A)
_CfprQosclassDefinitionFsmStageRn_Type=SnmpAdminString
_CfprQosclassDefinitionFsmStageRn_Object=MibTableColumn
cfprQosclassDefinitionFsmStageRn=_CfprQosclassDefinitionFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,67,3,1,3),_CfprQosclassDefinitionFsmStageRn_Type())
cfprQosclassDefinitionFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageRn.setStatus(_A)
_CfprQosclassDefinitionFsmStageDescrData_Type=SnmpAdminString
_CfprQosclassDefinitionFsmStageDescrData_Object=MibTableColumn
cfprQosclassDefinitionFsmStageDescrData=_CfprQosclassDefinitionFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,67,3,1,4),_CfprQosclassDefinitionFsmStageDescrData_Type())
cfprQosclassDefinitionFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageDescrData.setStatus(_A)
_CfprQosclassDefinitionFsmStageLastUpdateTime_Type=DateAndTime
_CfprQosclassDefinitionFsmStageLastUpdateTime_Object=MibTableColumn
cfprQosclassDefinitionFsmStageLastUpdateTime=_CfprQosclassDefinitionFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,67,3,1,5),_CfprQosclassDefinitionFsmStageLastUpdateTime_Type())
cfprQosclassDefinitionFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageLastUpdateTime.setStatus(_A)
_CfprQosclassDefinitionFsmStageName_Type=CfprQosclassDefinitionFsmStageName
_CfprQosclassDefinitionFsmStageName_Object=MibTableColumn
cfprQosclassDefinitionFsmStageName=_CfprQosclassDefinitionFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,67,3,1,6),_CfprQosclassDefinitionFsmStageName_Type())
cfprQosclassDefinitionFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageName.setStatus(_A)
_CfprQosclassDefinitionFsmStageOrder_Type=Gauge32
_CfprQosclassDefinitionFsmStageOrder_Object=MibTableColumn
cfprQosclassDefinitionFsmStageOrder=_CfprQosclassDefinitionFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,67,3,1,7),_CfprQosclassDefinitionFsmStageOrder_Type())
cfprQosclassDefinitionFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageOrder.setStatus(_A)
_CfprQosclassDefinitionFsmStageRetry_Type=Gauge32
_CfprQosclassDefinitionFsmStageRetry_Object=MibTableColumn
cfprQosclassDefinitionFsmStageRetry=_CfprQosclassDefinitionFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,67,3,1,8),_CfprQosclassDefinitionFsmStageRetry_Type())
cfprQosclassDefinitionFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageRetry.setStatus(_A)
_CfprQosclassDefinitionFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprQosclassDefinitionFsmStageStageStatus_Object=MibTableColumn
cfprQosclassDefinitionFsmStageStageStatus=_CfprQosclassDefinitionFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,67,3,1,9),_CfprQosclassDefinitionFsmStageStageStatus_Type())
cfprQosclassDefinitionFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmStageStageStatus.setStatus(_A)
_CfprQosclassDefinitionFsmTaskTable_Object=MibTable
cfprQosclassDefinitionFsmTaskTable=_CfprQosclassDefinitionFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,67,4))
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTaskTable.setStatus(_A)
_CfprQosclassDefinitionFsmTaskEntry_Object=MibTableRow
cfprQosclassDefinitionFsmTaskEntry=_CfprQosclassDefinitionFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,67,4,1))
cfprQosclassDefinitionFsmTaskEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTaskEntry.setStatus(_A)
_CfprQosclassDefinitionFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprQosclassDefinitionFsmTaskInstanceId_Object=MibTableColumn
cfprQosclassDefinitionFsmTaskInstanceId=_CfprQosclassDefinitionFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,67,4,1,1),_CfprQosclassDefinitionFsmTaskInstanceId_Type())
cfprQosclassDefinitionFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTaskInstanceId.setStatus(_A)
_CfprQosclassDefinitionFsmTaskDn_Type=CfprManagedObjectDn
_CfprQosclassDefinitionFsmTaskDn_Object=MibTableColumn
cfprQosclassDefinitionFsmTaskDn=_CfprQosclassDefinitionFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,67,4,1,2),_CfprQosclassDefinitionFsmTaskDn_Type())
cfprQosclassDefinitionFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTaskDn.setStatus(_A)
_CfprQosclassDefinitionFsmTaskRn_Type=SnmpAdminString
_CfprQosclassDefinitionFsmTaskRn_Object=MibTableColumn
cfprQosclassDefinitionFsmTaskRn=_CfprQosclassDefinitionFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,67,4,1,3),_CfprQosclassDefinitionFsmTaskRn_Type())
cfprQosclassDefinitionFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTaskRn.setStatus(_A)
_CfprQosclassDefinitionFsmTaskCompletion_Type=CfprFsmCompletion
_CfprQosclassDefinitionFsmTaskCompletion_Object=MibTableColumn
cfprQosclassDefinitionFsmTaskCompletion=_CfprQosclassDefinitionFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,67,4,1,4),_CfprQosclassDefinitionFsmTaskCompletion_Type())
cfprQosclassDefinitionFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTaskCompletion.setStatus(_A)
_CfprQosclassDefinitionFsmTaskFlags_Type=CfprFsmFlags
_CfprQosclassDefinitionFsmTaskFlags_Object=MibTableColumn
cfprQosclassDefinitionFsmTaskFlags=_CfprQosclassDefinitionFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,67,4,1,5),_CfprQosclassDefinitionFsmTaskFlags_Type())
cfprQosclassDefinitionFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTaskFlags.setStatus(_A)
_CfprQosclassDefinitionFsmTaskItem_Type=CfprQosclassDefinitionFsmTaskItem
_CfprQosclassDefinitionFsmTaskItem_Object=MibTableColumn
cfprQosclassDefinitionFsmTaskItem=_CfprQosclassDefinitionFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,67,4,1,6),_CfprQosclassDefinitionFsmTaskItem_Type())
cfprQosclassDefinitionFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTaskItem.setStatus(_A)
_CfprQosclassDefinitionFsmTaskSeqId_Type=Gauge32
_CfprQosclassDefinitionFsmTaskSeqId_Object=MibTableColumn
cfprQosclassDefinitionFsmTaskSeqId=_CfprQosclassDefinitionFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,67,4,1,7),_CfprQosclassDefinitionFsmTaskSeqId_Type())
cfprQosclassDefinitionFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassDefinitionFsmTaskSeqId.setStatus(_A)
_CfprQosclassEthBETable_Object=MibTable
cfprQosclassEthBETable=_CfprQosclassEthBETable_Object((1,3,6,1,4,1,9,9,826,1,67,5))
if mibBuilder.loadTexts:cfprQosclassEthBETable.setStatus(_A)
_CfprQosclassEthBEEntry_Object=MibTableRow
cfprQosclassEthBEEntry=_CfprQosclassEthBEEntry_Object((1,3,6,1,4,1,9,9,826,1,67,5,1))
cfprQosclassEthBEEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprQosclassEthBEEntry.setStatus(_A)
_CfprQosclassEthBEInstanceId_Type=CfprManagedObjectId
_CfprQosclassEthBEInstanceId_Object=MibTableColumn
cfprQosclassEthBEInstanceId=_CfprQosclassEthBEInstanceId_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,1),_CfprQosclassEthBEInstanceId_Type())
cfprQosclassEthBEInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprQosclassEthBEInstanceId.setStatus(_A)
_CfprQosclassEthBEDn_Type=CfprManagedObjectDn
_CfprQosclassEthBEDn_Object=MibTableColumn
cfprQosclassEthBEDn=_CfprQosclassEthBEDn_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,2),_CfprQosclassEthBEDn_Type())
cfprQosclassEthBEDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBEDn.setStatus(_A)
_CfprQosclassEthBERn_Type=SnmpAdminString
_CfprQosclassEthBERn_Object=MibTableColumn
cfprQosclassEthBERn=_CfprQosclassEthBERn_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,3),_CfprQosclassEthBERn_Type())
cfprQosclassEthBERn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBERn.setStatus(_A)
_CfprQosclassEthBEAdminState_Type=CfprQosclassEthBEAdminState
_CfprQosclassEthBEAdminState_Object=MibTableColumn
cfprQosclassEthBEAdminState=_CfprQosclassEthBEAdminState_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,4),_CfprQosclassEthBEAdminState_Type())
cfprQosclassEthBEAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBEAdminState.setStatus(_A)
_CfprQosclassEthBEBwPercent_Type=Gauge32
_CfprQosclassEthBEBwPercent_Object=MibTableColumn
cfprQosclassEthBEBwPercent=_CfprQosclassEthBEBwPercent_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,5),_CfprQosclassEthBEBwPercent_Type())
cfprQosclassEthBEBwPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBEBwPercent.setStatus(_A)
_CfprQosclassEthBECos_Type=Gauge32
_CfprQosclassEthBECos_Object=MibTableColumn
cfprQosclassEthBECos=_CfprQosclassEthBECos_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,6),_CfprQosclassEthBECos_Type())
cfprQosclassEthBECos.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBECos.setStatus(_A)
_CfprQosclassEthBEDrop_Type=CfprQosclassEthBEDrop
_CfprQosclassEthBEDrop_Object=MibTableColumn
cfprQosclassEthBEDrop=_CfprQosclassEthBEDrop_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,7),_CfprQosclassEthBEDrop_Type())
cfprQosclassEthBEDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBEDrop.setStatus(_A)
_CfprQosclassEthBEMtu_Type=SnmpAdminString
_CfprQosclassEthBEMtu_Object=MibTableColumn
cfprQosclassEthBEMtu=_CfprQosclassEthBEMtu_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,8),_CfprQosclassEthBEMtu_Type())
cfprQosclassEthBEMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBEMtu.setStatus(_A)
_CfprQosclassEthBEMulticastOptimize_Type=TruthValue
_CfprQosclassEthBEMulticastOptimize_Object=MibTableColumn
cfprQosclassEthBEMulticastOptimize=_CfprQosclassEthBEMulticastOptimize_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,9),_CfprQosclassEthBEMulticastOptimize_Type())
cfprQosclassEthBEMulticastOptimize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBEMulticastOptimize.setStatus(_A)
_CfprQosclassEthBEName_Type=SnmpAdminString
_CfprQosclassEthBEName_Object=MibTableColumn
cfprQosclassEthBEName=_CfprQosclassEthBEName_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,10),_CfprQosclassEthBEName_Type())
cfprQosclassEthBEName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBEName.setStatus(_A)
_CfprQosclassEthBEPriority_Type=CfprQosclassEthBEPriority
_CfprQosclassEthBEPriority_Object=MibTableColumn
cfprQosclassEthBEPriority=_CfprQosclassEthBEPriority_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,11),_CfprQosclassEthBEPriority_Type())
cfprQosclassEthBEPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBEPriority.setStatus(_A)
_CfprQosclassEthBEWeight_Type=Gauge32
_CfprQosclassEthBEWeight_Object=MibTableColumn
cfprQosclassEthBEWeight=_CfprQosclassEthBEWeight_Object((1,3,6,1,4,1,9,9,826,1,67,5,1,12),_CfprQosclassEthBEWeight_Type())
cfprQosclassEthBEWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthBEWeight.setStatus(_A)
_CfprQosclassEthClassifiedTable_Object=MibTable
cfprQosclassEthClassifiedTable=_CfprQosclassEthClassifiedTable_Object((1,3,6,1,4,1,9,9,826,1,67,6))
if mibBuilder.loadTexts:cfprQosclassEthClassifiedTable.setStatus(_A)
_CfprQosclassEthClassifiedEntry_Object=MibTableRow
cfprQosclassEthClassifiedEntry=_CfprQosclassEthClassifiedEntry_Object((1,3,6,1,4,1,9,9,826,1,67,6,1))
cfprQosclassEthClassifiedEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprQosclassEthClassifiedEntry.setStatus(_A)
_CfprQosclassEthClassifiedInstanceId_Type=CfprManagedObjectId
_CfprQosclassEthClassifiedInstanceId_Object=MibTableColumn
cfprQosclassEthClassifiedInstanceId=_CfprQosclassEthClassifiedInstanceId_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,1),_CfprQosclassEthClassifiedInstanceId_Type())
cfprQosclassEthClassifiedInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedInstanceId.setStatus(_A)
_CfprQosclassEthClassifiedDn_Type=CfprManagedObjectDn
_CfprQosclassEthClassifiedDn_Object=MibTableColumn
cfprQosclassEthClassifiedDn=_CfprQosclassEthClassifiedDn_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,2),_CfprQosclassEthClassifiedDn_Type())
cfprQosclassEthClassifiedDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedDn.setStatus(_A)
_CfprQosclassEthClassifiedRn_Type=SnmpAdminString
_CfprQosclassEthClassifiedRn_Object=MibTableColumn
cfprQosclassEthClassifiedRn=_CfprQosclassEthClassifiedRn_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,3),_CfprQosclassEthClassifiedRn_Type())
cfprQosclassEthClassifiedRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedRn.setStatus(_A)
_CfprQosclassEthClassifiedAdminState_Type=CfprQosclassEthClassifiedAdminState
_CfprQosclassEthClassifiedAdminState_Object=MibTableColumn
cfprQosclassEthClassifiedAdminState=_CfprQosclassEthClassifiedAdminState_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,4),_CfprQosclassEthClassifiedAdminState_Type())
cfprQosclassEthClassifiedAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedAdminState.setStatus(_A)
_CfprQosclassEthClassifiedBwPercent_Type=Gauge32
_CfprQosclassEthClassifiedBwPercent_Object=MibTableColumn
cfprQosclassEthClassifiedBwPercent=_CfprQosclassEthClassifiedBwPercent_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,5),_CfprQosclassEthClassifiedBwPercent_Type())
cfprQosclassEthClassifiedBwPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedBwPercent.setStatus(_A)
_CfprQosclassEthClassifiedCos_Type=Gauge32
_CfprQosclassEthClassifiedCos_Object=MibTableColumn
cfprQosclassEthClassifiedCos=_CfprQosclassEthClassifiedCos_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,6),_CfprQosclassEthClassifiedCos_Type())
cfprQosclassEthClassifiedCos.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedCos.setStatus(_A)
_CfprQosclassEthClassifiedDrop_Type=CfprQosclassEthClassifiedDrop
_CfprQosclassEthClassifiedDrop_Object=MibTableColumn
cfprQosclassEthClassifiedDrop=_CfprQosclassEthClassifiedDrop_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,7),_CfprQosclassEthClassifiedDrop_Type())
cfprQosclassEthClassifiedDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedDrop.setStatus(_A)
_CfprQosclassEthClassifiedMtu_Type=SnmpAdminString
_CfprQosclassEthClassifiedMtu_Object=MibTableColumn
cfprQosclassEthClassifiedMtu=_CfprQosclassEthClassifiedMtu_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,8),_CfprQosclassEthClassifiedMtu_Type())
cfprQosclassEthClassifiedMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedMtu.setStatus(_A)
_CfprQosclassEthClassifiedMulticastOptimize_Type=TruthValue
_CfprQosclassEthClassifiedMulticastOptimize_Object=MibTableColumn
cfprQosclassEthClassifiedMulticastOptimize=_CfprQosclassEthClassifiedMulticastOptimize_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,9),_CfprQosclassEthClassifiedMulticastOptimize_Type())
cfprQosclassEthClassifiedMulticastOptimize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedMulticastOptimize.setStatus(_A)
_CfprQosclassEthClassifiedName_Type=SnmpAdminString
_CfprQosclassEthClassifiedName_Object=MibTableColumn
cfprQosclassEthClassifiedName=_CfprQosclassEthClassifiedName_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,10),_CfprQosclassEthClassifiedName_Type())
cfprQosclassEthClassifiedName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedName.setStatus(_A)
_CfprQosclassEthClassifiedPriority_Type=CfprQosclassEthClassifiedPriority
_CfprQosclassEthClassifiedPriority_Object=MibTableColumn
cfprQosclassEthClassifiedPriority=_CfprQosclassEthClassifiedPriority_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,11),_CfprQosclassEthClassifiedPriority_Type())
cfprQosclassEthClassifiedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedPriority.setStatus(_A)
_CfprQosclassEthClassifiedWeight_Type=Gauge32
_CfprQosclassEthClassifiedWeight_Object=MibTableColumn
cfprQosclassEthClassifiedWeight=_CfprQosclassEthClassifiedWeight_Object((1,3,6,1,4,1,9,9,826,1,67,6,1,12),_CfprQosclassEthClassifiedWeight_Type())
cfprQosclassEthClassifiedWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassEthClassifiedWeight.setStatus(_A)
_CfprQosclassFcTable_Object=MibTable
cfprQosclassFcTable=_CfprQosclassFcTable_Object((1,3,6,1,4,1,9,9,826,1,67,7))
if mibBuilder.loadTexts:cfprQosclassFcTable.setStatus(_A)
_CfprQosclassFcEntry_Object=MibTableRow
cfprQosclassFcEntry=_CfprQosclassFcEntry_Object((1,3,6,1,4,1,9,9,826,1,67,7,1))
cfprQosclassFcEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprQosclassFcEntry.setStatus(_A)
_CfprQosclassFcInstanceId_Type=CfprManagedObjectId
_CfprQosclassFcInstanceId_Object=MibTableColumn
cfprQosclassFcInstanceId=_CfprQosclassFcInstanceId_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,1),_CfprQosclassFcInstanceId_Type())
cfprQosclassFcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprQosclassFcInstanceId.setStatus(_A)
_CfprQosclassFcDn_Type=CfprManagedObjectDn
_CfprQosclassFcDn_Object=MibTableColumn
cfprQosclassFcDn=_CfprQosclassFcDn_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,2),_CfprQosclassFcDn_Type())
cfprQosclassFcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcDn.setStatus(_A)
_CfprQosclassFcRn_Type=SnmpAdminString
_CfprQosclassFcRn_Object=MibTableColumn
cfprQosclassFcRn=_CfprQosclassFcRn_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,3),_CfprQosclassFcRn_Type())
cfprQosclassFcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcRn.setStatus(_A)
_CfprQosclassFcAdminState_Type=CfprQosclassFcAdminState
_CfprQosclassFcAdminState_Object=MibTableColumn
cfprQosclassFcAdminState=_CfprQosclassFcAdminState_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,4),_CfprQosclassFcAdminState_Type())
cfprQosclassFcAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcAdminState.setStatus(_A)
_CfprQosclassFcBwPercent_Type=Gauge32
_CfprQosclassFcBwPercent_Object=MibTableColumn
cfprQosclassFcBwPercent=_CfprQosclassFcBwPercent_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,5),_CfprQosclassFcBwPercent_Type())
cfprQosclassFcBwPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcBwPercent.setStatus(_A)
_CfprQosclassFcCos_Type=Gauge32
_CfprQosclassFcCos_Object=MibTableColumn
cfprQosclassFcCos=_CfprQosclassFcCos_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,6),_CfprQosclassFcCos_Type())
cfprQosclassFcCos.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcCos.setStatus(_A)
_CfprQosclassFcDrop_Type=CfprQosclassFcDrop
_CfprQosclassFcDrop_Object=MibTableColumn
cfprQosclassFcDrop=_CfprQosclassFcDrop_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,7),_CfprQosclassFcDrop_Type())
cfprQosclassFcDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcDrop.setStatus(_A)
_CfprQosclassFcMtu_Type=SnmpAdminString
_CfprQosclassFcMtu_Object=MibTableColumn
cfprQosclassFcMtu=_CfprQosclassFcMtu_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,8),_CfprQosclassFcMtu_Type())
cfprQosclassFcMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcMtu.setStatus(_A)
_CfprQosclassFcName_Type=SnmpAdminString
_CfprQosclassFcName_Object=MibTableColumn
cfprQosclassFcName=_CfprQosclassFcName_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,9),_CfprQosclassFcName_Type())
cfprQosclassFcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcName.setStatus(_A)
_CfprQosclassFcPriority_Type=CfprQosclassFcPriority
_CfprQosclassFcPriority_Object=MibTableColumn
cfprQosclassFcPriority=_CfprQosclassFcPriority_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,10),_CfprQosclassFcPriority_Type())
cfprQosclassFcPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcPriority.setStatus(_A)
_CfprQosclassFcWeight_Type=Gauge32
_CfprQosclassFcWeight_Object=MibTableColumn
cfprQosclassFcWeight=_CfprQosclassFcWeight_Object((1,3,6,1,4,1,9,9,826,1,67,7,1,11),_CfprQosclassFcWeight_Type())
cfprQosclassFcWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQosclassFcWeight.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprQosclassObjects':cfprQosclassObjects,'cfprQosclassDefinitionTable':cfprQosclassDefinitionTable,'cfprQosclassDefinitionEntry':cfprQosclassDefinitionEntry,_E:cfprQosclassDefinitionInstanceId,'cfprQosclassDefinitionDn':cfprQosclassDefinitionDn,'cfprQosclassDefinitionRn':cfprQosclassDefinitionRn,'cfprQosclassDefinitionDescr':cfprQosclassDefinitionDescr,'cfprQosclassDefinitionFsmDescr':cfprQosclassDefinitionFsmDescr,'cfprQosclassDefinitionFsmPrev':cfprQosclassDefinitionFsmPrev,'cfprQosclassDefinitionFsmProgr':cfprQosclassDefinitionFsmProgr,'cfprQosclassDefinitionFsmRmtInvErrCode':cfprQosclassDefinitionFsmRmtInvErrCode,'cfprQosclassDefinitionFsmRmtInvErrDescr':cfprQosclassDefinitionFsmRmtInvErrDescr,'cfprQosclassDefinitionFsmRmtInvRslt':cfprQosclassDefinitionFsmRmtInvRslt,'cfprQosclassDefinitionFsmStageDescr':cfprQosclassDefinitionFsmStageDescr,'cfprQosclassDefinitionFsmStamp':cfprQosclassDefinitionFsmStamp,'cfprQosclassDefinitionFsmStatus':cfprQosclassDefinitionFsmStatus,'cfprQosclassDefinitionFsmTry':cfprQosclassDefinitionFsmTry,'cfprQosclassDefinitionIntId':cfprQosclassDefinitionIntId,'cfprQosclassDefinitionName':cfprQosclassDefinitionName,'cfprQosclassDefinitionPolicyLevel':cfprQosclassDefinitionPolicyLevel,'cfprQosclassDefinitionPolicyOwner':cfprQosclassDefinitionPolicyOwner,'cfprQosclassDefinitionFsmTable':cfprQosclassDefinitionFsmTable,'cfprQosclassDefinitionFsmEntry':cfprQosclassDefinitionFsmEntry,_F:cfprQosclassDefinitionFsmInstanceId,'cfprQosclassDefinitionFsmDn':cfprQosclassDefinitionFsmDn,'cfprQosclassDefinitionFsmRn':cfprQosclassDefinitionFsmRn,'cfprQosclassDefinitionFsmCompletionTime':cfprQosclassDefinitionFsmCompletionTime,'cfprQosclassDefinitionFsmCurrentFsm':cfprQosclassDefinitionFsmCurrentFsm,'cfprQosclassDefinitionFsmDescrData':cfprQosclassDefinitionFsmDescrData,'cfprQosclassDefinitionFsmFsmStatus':cfprQosclassDefinitionFsmFsmStatus,'cfprQosclassDefinitionFsmProgress':cfprQosclassDefinitionFsmProgress,'cfprQosclassDefinitionFsmRmtErrCode':cfprQosclassDefinitionFsmRmtErrCode,'cfprQosclassDefinitionFsmRmtErrDescr':cfprQosclassDefinitionFsmRmtErrDescr,'cfprQosclassDefinitionFsmRmtRslt':cfprQosclassDefinitionFsmRmtRslt,'cfprQosclassDefinitionFsmStageTable':cfprQosclassDefinitionFsmStageTable,'cfprQosclassDefinitionFsmStageEntry':cfprQosclassDefinitionFsmStageEntry,_G:cfprQosclassDefinitionFsmStageInstanceId,'cfprQosclassDefinitionFsmStageDn':cfprQosclassDefinitionFsmStageDn,'cfprQosclassDefinitionFsmStageRn':cfprQosclassDefinitionFsmStageRn,'cfprQosclassDefinitionFsmStageDescrData':cfprQosclassDefinitionFsmStageDescrData,'cfprQosclassDefinitionFsmStageLastUpdateTime':cfprQosclassDefinitionFsmStageLastUpdateTime,'cfprQosclassDefinitionFsmStageName':cfprQosclassDefinitionFsmStageName,'cfprQosclassDefinitionFsmStageOrder':cfprQosclassDefinitionFsmStageOrder,'cfprQosclassDefinitionFsmStageRetry':cfprQosclassDefinitionFsmStageRetry,'cfprQosclassDefinitionFsmStageStageStatus':cfprQosclassDefinitionFsmStageStageStatus,'cfprQosclassDefinitionFsmTaskTable':cfprQosclassDefinitionFsmTaskTable,'cfprQosclassDefinitionFsmTaskEntry':cfprQosclassDefinitionFsmTaskEntry,_H:cfprQosclassDefinitionFsmTaskInstanceId,'cfprQosclassDefinitionFsmTaskDn':cfprQosclassDefinitionFsmTaskDn,'cfprQosclassDefinitionFsmTaskRn':cfprQosclassDefinitionFsmTaskRn,'cfprQosclassDefinitionFsmTaskCompletion':cfprQosclassDefinitionFsmTaskCompletion,'cfprQosclassDefinitionFsmTaskFlags':cfprQosclassDefinitionFsmTaskFlags,'cfprQosclassDefinitionFsmTaskItem':cfprQosclassDefinitionFsmTaskItem,'cfprQosclassDefinitionFsmTaskSeqId':cfprQosclassDefinitionFsmTaskSeqId,'cfprQosclassEthBETable':cfprQosclassEthBETable,'cfprQosclassEthBEEntry':cfprQosclassEthBEEntry,_I:cfprQosclassEthBEInstanceId,'cfprQosclassEthBEDn':cfprQosclassEthBEDn,'cfprQosclassEthBERn':cfprQosclassEthBERn,'cfprQosclassEthBEAdminState':cfprQosclassEthBEAdminState,'cfprQosclassEthBEBwPercent':cfprQosclassEthBEBwPercent,'cfprQosclassEthBECos':cfprQosclassEthBECos,'cfprQosclassEthBEDrop':cfprQosclassEthBEDrop,'cfprQosclassEthBEMtu':cfprQosclassEthBEMtu,'cfprQosclassEthBEMulticastOptimize':cfprQosclassEthBEMulticastOptimize,'cfprQosclassEthBEName':cfprQosclassEthBEName,'cfprQosclassEthBEPriority':cfprQosclassEthBEPriority,'cfprQosclassEthBEWeight':cfprQosclassEthBEWeight,'cfprQosclassEthClassifiedTable':cfprQosclassEthClassifiedTable,'cfprQosclassEthClassifiedEntry':cfprQosclassEthClassifiedEntry,_J:cfprQosclassEthClassifiedInstanceId,'cfprQosclassEthClassifiedDn':cfprQosclassEthClassifiedDn,'cfprQosclassEthClassifiedRn':cfprQosclassEthClassifiedRn,'cfprQosclassEthClassifiedAdminState':cfprQosclassEthClassifiedAdminState,'cfprQosclassEthClassifiedBwPercent':cfprQosclassEthClassifiedBwPercent,'cfprQosclassEthClassifiedCos':cfprQosclassEthClassifiedCos,'cfprQosclassEthClassifiedDrop':cfprQosclassEthClassifiedDrop,'cfprQosclassEthClassifiedMtu':cfprQosclassEthClassifiedMtu,'cfprQosclassEthClassifiedMulticastOptimize':cfprQosclassEthClassifiedMulticastOptimize,'cfprQosclassEthClassifiedName':cfprQosclassEthClassifiedName,'cfprQosclassEthClassifiedPriority':cfprQosclassEthClassifiedPriority,'cfprQosclassEthClassifiedWeight':cfprQosclassEthClassifiedWeight,'cfprQosclassFcTable':cfprQosclassFcTable,'cfprQosclassFcEntry':cfprQosclassFcEntry,_K:cfprQosclassFcInstanceId,'cfprQosclassFcDn':cfprQosclassFcDn,'cfprQosclassFcRn':cfprQosclassFcRn,'cfprQosclassFcAdminState':cfprQosclassFcAdminState,'cfprQosclassFcBwPercent':cfprQosclassFcBwPercent,'cfprQosclassFcCos':cfprQosclassFcCos,'cfprQosclassFcDrop':cfprQosclassFcDrop,'cfprQosclassFcMtu':cfprQosclassFcMtu,'cfprQosclassFcName':cfprQosclassFcName,'cfprQosclassFcPriority':cfprQosclassFcPriority,'cfprQosclassFcWeight':cfprQosclassFcWeight})