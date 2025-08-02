_K='cucsQosclassDefinitionFsmStageInstanceId'
_J='cucsQosclassDefinitionFsmInstanceId'
_I='cucsQosclassFcInstanceId'
_H='cucsQosclassEthClassifiedInstanceId'
_G='cucsQosclassEthBEInstanceId'
_F='cucsQosclassDefinitionFsmTaskInstanceId'
_E='cucsQosclassDefinitionInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsConditionRemoteInvRslt,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsPolicyPolicyOwner,CucsQosclassDefinitionFsmCurrentFsm,CucsQosclassDefinitionFsmStageName,CucsQosclassDefinitionFsmTaskItem,CucsQosclassEthBEAdminState,CucsQosclassEthBEDrop,CucsQosclassEthBEPriority,CucsQosclassEthClassifiedAdminState,CucsQosclassEthClassifiedDrop,CucsQosclassEthClassifiedPriority,CucsQosclassFcAdminState,CucsQosclassFcDrop,CucsQosclassFcPriority=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsConditionRemoteInvRslt','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsPolicyPolicyOwner','CucsQosclassDefinitionFsmCurrentFsm','CucsQosclassDefinitionFsmStageName','CucsQosclassDefinitionFsmTaskItem','CucsQosclassEthBEAdminState','CucsQosclassEthBEDrop','CucsQosclassEthBEPriority','CucsQosclassEthClassifiedAdminState','CucsQosclassEthClassifiedDrop','CucsQosclassEthClassifiedPriority','CucsQosclassFcAdminState','CucsQosclassFcDrop','CucsQosclassFcPriority')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsQosclassObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,42))
_CucsQosclassDefinitionTable_Object=MibTable
cucsQosclassDefinitionTable=_CucsQosclassDefinitionTable_Object((1,3,6,1,4,1,9,9,719,1,42,1))
if mibBuilder.loadTexts:cucsQosclassDefinitionTable.setStatus(_A)
_CucsQosclassDefinitionEntry_Object=MibTableRow
cucsQosclassDefinitionEntry=_CucsQosclassDefinitionEntry_Object((1,3,6,1,4,1,9,9,719,1,42,1,1))
cucsQosclassDefinitionEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsQosclassDefinitionEntry.setStatus(_A)
_CucsQosclassDefinitionInstanceId_Type=CucsManagedObjectId
_CucsQosclassDefinitionInstanceId_Object=MibTableColumn
cucsQosclassDefinitionInstanceId=_CucsQosclassDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,1),_CucsQosclassDefinitionInstanceId_Type())
cucsQosclassDefinitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsQosclassDefinitionInstanceId.setStatus(_A)
_CucsQosclassDefinitionDn_Type=CucsManagedObjectDn
_CucsQosclassDefinitionDn_Object=MibTableColumn
cucsQosclassDefinitionDn=_CucsQosclassDefinitionDn_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,2),_CucsQosclassDefinitionDn_Type())
cucsQosclassDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionDn.setStatus(_A)
_CucsQosclassDefinitionRn_Type=SnmpAdminString
_CucsQosclassDefinitionRn_Object=MibTableColumn
cucsQosclassDefinitionRn=_CucsQosclassDefinitionRn_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,3),_CucsQosclassDefinitionRn_Type())
cucsQosclassDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionRn.setStatus(_A)
_CucsQosclassDefinitionDescr_Type=SnmpAdminString
_CucsQosclassDefinitionDescr_Object=MibTableColumn
cucsQosclassDefinitionDescr=_CucsQosclassDefinitionDescr_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,4),_CucsQosclassDefinitionDescr_Type())
cucsQosclassDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionDescr.setStatus(_A)
_CucsQosclassDefinitionFsmDescr_Type=SnmpAdminString
_CucsQosclassDefinitionFsmDescr_Object=MibTableColumn
cucsQosclassDefinitionFsmDescr=_CucsQosclassDefinitionFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,5),_CucsQosclassDefinitionFsmDescr_Type())
cucsQosclassDefinitionFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmDescr.setStatus(_A)
_CucsQosclassDefinitionFsmPrev_Type=SnmpAdminString
_CucsQosclassDefinitionFsmPrev_Object=MibTableColumn
cucsQosclassDefinitionFsmPrev=_CucsQosclassDefinitionFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,6),_CucsQosclassDefinitionFsmPrev_Type())
cucsQosclassDefinitionFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmPrev.setStatus(_A)
_CucsQosclassDefinitionFsmProgr_Type=Gauge32
_CucsQosclassDefinitionFsmProgr_Object=MibTableColumn
cucsQosclassDefinitionFsmProgr=_CucsQosclassDefinitionFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,7),_CucsQosclassDefinitionFsmProgr_Type())
cucsQosclassDefinitionFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmProgr.setStatus(_A)
_CucsQosclassDefinitionFsmRmtInvErrCode_Type=Gauge32
_CucsQosclassDefinitionFsmRmtInvErrCode_Object=MibTableColumn
cucsQosclassDefinitionFsmRmtInvErrCode=_CucsQosclassDefinitionFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,8),_CucsQosclassDefinitionFsmRmtInvErrCode_Type())
cucsQosclassDefinitionFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmRmtInvErrCode.setStatus(_A)
_CucsQosclassDefinitionFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsQosclassDefinitionFsmRmtInvErrDescr_Object=MibTableColumn
cucsQosclassDefinitionFsmRmtInvErrDescr=_CucsQosclassDefinitionFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,9),_CucsQosclassDefinitionFsmRmtInvErrDescr_Type())
cucsQosclassDefinitionFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmRmtInvErrDescr.setStatus(_A)
_CucsQosclassDefinitionFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsQosclassDefinitionFsmRmtInvRslt_Object=MibTableColumn
cucsQosclassDefinitionFsmRmtInvRslt=_CucsQosclassDefinitionFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,10),_CucsQosclassDefinitionFsmRmtInvRslt_Type())
cucsQosclassDefinitionFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmRmtInvRslt.setStatus(_A)
_CucsQosclassDefinitionFsmStageDescr_Type=SnmpAdminString
_CucsQosclassDefinitionFsmStageDescr_Object=MibTableColumn
cucsQosclassDefinitionFsmStageDescr=_CucsQosclassDefinitionFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,11),_CucsQosclassDefinitionFsmStageDescr_Type())
cucsQosclassDefinitionFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageDescr.setStatus(_A)
_CucsQosclassDefinitionFsmStamp_Type=DateAndTime
_CucsQosclassDefinitionFsmStamp_Object=MibTableColumn
cucsQosclassDefinitionFsmStamp=_CucsQosclassDefinitionFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,12),_CucsQosclassDefinitionFsmStamp_Type())
cucsQosclassDefinitionFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStamp.setStatus(_A)
_CucsQosclassDefinitionFsmStatus_Type=SnmpAdminString
_CucsQosclassDefinitionFsmStatus_Object=MibTableColumn
cucsQosclassDefinitionFsmStatus=_CucsQosclassDefinitionFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,13),_CucsQosclassDefinitionFsmStatus_Type())
cucsQosclassDefinitionFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStatus.setStatus(_A)
_CucsQosclassDefinitionFsmTry_Type=Gauge32
_CucsQosclassDefinitionFsmTry_Object=MibTableColumn
cucsQosclassDefinitionFsmTry=_CucsQosclassDefinitionFsmTry_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,14),_CucsQosclassDefinitionFsmTry_Type())
cucsQosclassDefinitionFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTry.setStatus(_A)
_CucsQosclassDefinitionIntId_Type=SnmpAdminString
_CucsQosclassDefinitionIntId_Object=MibTableColumn
cucsQosclassDefinitionIntId=_CucsQosclassDefinitionIntId_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,15),_CucsQosclassDefinitionIntId_Type())
cucsQosclassDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionIntId.setStatus(_A)
_CucsQosclassDefinitionName_Type=SnmpAdminString
_CucsQosclassDefinitionName_Object=MibTableColumn
cucsQosclassDefinitionName=_CucsQosclassDefinitionName_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,16),_CucsQosclassDefinitionName_Type())
cucsQosclassDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionName.setStatus(_A)
_CucsQosclassDefinitionPolicyLevel_Type=Gauge32
_CucsQosclassDefinitionPolicyLevel_Object=MibTableColumn
cucsQosclassDefinitionPolicyLevel=_CucsQosclassDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,17),_CucsQosclassDefinitionPolicyLevel_Type())
cucsQosclassDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionPolicyLevel.setStatus(_A)
_CucsQosclassDefinitionPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsQosclassDefinitionPolicyOwner_Object=MibTableColumn
cucsQosclassDefinitionPolicyOwner=_CucsQosclassDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,18),_CucsQosclassDefinitionPolicyOwner_Type())
cucsQosclassDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionPolicyOwner.setStatus(_A)
_CucsQosclassDefinitionMmuPercent_Type=Gauge32
_CucsQosclassDefinitionMmuPercent_Object=MibTableColumn
cucsQosclassDefinitionMmuPercent=_CucsQosclassDefinitionMmuPercent_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,19),_CucsQosclassDefinitionMmuPercent_Type())
cucsQosclassDefinitionMmuPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionMmuPercent.setStatus(_A)
_CucsQosclassDefinitionNumBreakoutPort_Type=Gauge32
_CucsQosclassDefinitionNumBreakoutPort_Object=MibTableColumn
cucsQosclassDefinitionNumBreakoutPort=_CucsQosclassDefinitionNumBreakoutPort_Object((1,3,6,1,4,1,9,9,719,1,42,1,1,20),_CucsQosclassDefinitionNumBreakoutPort_Type())
cucsQosclassDefinitionNumBreakoutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionNumBreakoutPort.setStatus(_A)
_CucsQosclassDefinitionFsmTaskTable_Object=MibTable
cucsQosclassDefinitionFsmTaskTable=_CucsQosclassDefinitionFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,42,2))
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTaskTable.setStatus(_A)
_CucsQosclassDefinitionFsmTaskEntry_Object=MibTableRow
cucsQosclassDefinitionFsmTaskEntry=_CucsQosclassDefinitionFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,42,2,1))
cucsQosclassDefinitionFsmTaskEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTaskEntry.setStatus(_A)
_CucsQosclassDefinitionFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsQosclassDefinitionFsmTaskInstanceId_Object=MibTableColumn
cucsQosclassDefinitionFsmTaskInstanceId=_CucsQosclassDefinitionFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,42,2,1,1),_CucsQosclassDefinitionFsmTaskInstanceId_Type())
cucsQosclassDefinitionFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTaskInstanceId.setStatus(_A)
_CucsQosclassDefinitionFsmTaskDn_Type=CucsManagedObjectDn
_CucsQosclassDefinitionFsmTaskDn_Object=MibTableColumn
cucsQosclassDefinitionFsmTaskDn=_CucsQosclassDefinitionFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,42,2,1,2),_CucsQosclassDefinitionFsmTaskDn_Type())
cucsQosclassDefinitionFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTaskDn.setStatus(_A)
_CucsQosclassDefinitionFsmTaskRn_Type=SnmpAdminString
_CucsQosclassDefinitionFsmTaskRn_Object=MibTableColumn
cucsQosclassDefinitionFsmTaskRn=_CucsQosclassDefinitionFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,42,2,1,3),_CucsQosclassDefinitionFsmTaskRn_Type())
cucsQosclassDefinitionFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTaskRn.setStatus(_A)
_CucsQosclassDefinitionFsmTaskCompletion_Type=CucsFsmCompletion
_CucsQosclassDefinitionFsmTaskCompletion_Object=MibTableColumn
cucsQosclassDefinitionFsmTaskCompletion=_CucsQosclassDefinitionFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,42,2,1,4),_CucsQosclassDefinitionFsmTaskCompletion_Type())
cucsQosclassDefinitionFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTaskCompletion.setStatus(_A)
_CucsQosclassDefinitionFsmTaskFlags_Type=CucsFsmFlags
_CucsQosclassDefinitionFsmTaskFlags_Object=MibTableColumn
cucsQosclassDefinitionFsmTaskFlags=_CucsQosclassDefinitionFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,42,2,1,5),_CucsQosclassDefinitionFsmTaskFlags_Type())
cucsQosclassDefinitionFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTaskFlags.setStatus(_A)
_CucsQosclassDefinitionFsmTaskItem_Type=CucsQosclassDefinitionFsmTaskItem
_CucsQosclassDefinitionFsmTaskItem_Object=MibTableColumn
cucsQosclassDefinitionFsmTaskItem=_CucsQosclassDefinitionFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,42,2,1,6),_CucsQosclassDefinitionFsmTaskItem_Type())
cucsQosclassDefinitionFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTaskItem.setStatus(_A)
_CucsQosclassDefinitionFsmTaskSeqId_Type=Gauge32
_CucsQosclassDefinitionFsmTaskSeqId_Object=MibTableColumn
cucsQosclassDefinitionFsmTaskSeqId=_CucsQosclassDefinitionFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,42,2,1,7),_CucsQosclassDefinitionFsmTaskSeqId_Type())
cucsQosclassDefinitionFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTaskSeqId.setStatus(_A)
_CucsQosclassEthBETable_Object=MibTable
cucsQosclassEthBETable=_CucsQosclassEthBETable_Object((1,3,6,1,4,1,9,9,719,1,42,3))
if mibBuilder.loadTexts:cucsQosclassEthBETable.setStatus(_A)
_CucsQosclassEthBEEntry_Object=MibTableRow
cucsQosclassEthBEEntry=_CucsQosclassEthBEEntry_Object((1,3,6,1,4,1,9,9,719,1,42,3,1))
cucsQosclassEthBEEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsQosclassEthBEEntry.setStatus(_A)
_CucsQosclassEthBEInstanceId_Type=CucsManagedObjectId
_CucsQosclassEthBEInstanceId_Object=MibTableColumn
cucsQosclassEthBEInstanceId=_CucsQosclassEthBEInstanceId_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,1),_CucsQosclassEthBEInstanceId_Type())
cucsQosclassEthBEInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsQosclassEthBEInstanceId.setStatus(_A)
_CucsQosclassEthBEDn_Type=CucsManagedObjectDn
_CucsQosclassEthBEDn_Object=MibTableColumn
cucsQosclassEthBEDn=_CucsQosclassEthBEDn_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,2),_CucsQosclassEthBEDn_Type())
cucsQosclassEthBEDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBEDn.setStatus(_A)
_CucsQosclassEthBERn_Type=SnmpAdminString
_CucsQosclassEthBERn_Object=MibTableColumn
cucsQosclassEthBERn=_CucsQosclassEthBERn_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,3),_CucsQosclassEthBERn_Type())
cucsQosclassEthBERn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBERn.setStatus(_A)
_CucsQosclassEthBEAdminState_Type=CucsQosclassEthBEAdminState
_CucsQosclassEthBEAdminState_Object=MibTableColumn
cucsQosclassEthBEAdminState=_CucsQosclassEthBEAdminState_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,4),_CucsQosclassEthBEAdminState_Type())
cucsQosclassEthBEAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBEAdminState.setStatus(_A)
_CucsQosclassEthBEBwPercent_Type=Gauge32
_CucsQosclassEthBEBwPercent_Object=MibTableColumn
cucsQosclassEthBEBwPercent=_CucsQosclassEthBEBwPercent_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,5),_CucsQosclassEthBEBwPercent_Type())
cucsQosclassEthBEBwPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBEBwPercent.setStatus(_A)
_CucsQosclassEthBECos_Type=Gauge32
_CucsQosclassEthBECos_Object=MibTableColumn
cucsQosclassEthBECos=_CucsQosclassEthBECos_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,6),_CucsQosclassEthBECos_Type())
cucsQosclassEthBECos.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBECos.setStatus(_A)
_CucsQosclassEthBEDrop_Type=CucsQosclassEthBEDrop
_CucsQosclassEthBEDrop_Object=MibTableColumn
cucsQosclassEthBEDrop=_CucsQosclassEthBEDrop_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,7),_CucsQosclassEthBEDrop_Type())
cucsQosclassEthBEDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBEDrop.setStatus(_A)
_CucsQosclassEthBEMtu_Type=SnmpAdminString
_CucsQosclassEthBEMtu_Object=MibTableColumn
cucsQosclassEthBEMtu=_CucsQosclassEthBEMtu_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,8),_CucsQosclassEthBEMtu_Type())
cucsQosclassEthBEMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBEMtu.setStatus(_A)
_CucsQosclassEthBEMulticastOptimize_Type=TruthValue
_CucsQosclassEthBEMulticastOptimize_Object=MibTableColumn
cucsQosclassEthBEMulticastOptimize=_CucsQosclassEthBEMulticastOptimize_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,9),_CucsQosclassEthBEMulticastOptimize_Type())
cucsQosclassEthBEMulticastOptimize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBEMulticastOptimize.setStatus(_A)
_CucsQosclassEthBEName_Type=SnmpAdminString
_CucsQosclassEthBEName_Object=MibTableColumn
cucsQosclassEthBEName=_CucsQosclassEthBEName_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,10),_CucsQosclassEthBEName_Type())
cucsQosclassEthBEName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBEName.setStatus(_A)
_CucsQosclassEthBEPriority_Type=CucsQosclassEthBEPriority
_CucsQosclassEthBEPriority_Object=MibTableColumn
cucsQosclassEthBEPriority=_CucsQosclassEthBEPriority_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,11),_CucsQosclassEthBEPriority_Type())
cucsQosclassEthBEPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBEPriority.setStatus(_A)
_CucsQosclassEthBEWeight_Type=Gauge32
_CucsQosclassEthBEWeight_Object=MibTableColumn
cucsQosclassEthBEWeight=_CucsQosclassEthBEWeight_Object((1,3,6,1,4,1,9,9,719,1,42,3,1,12),_CucsQosclassEthBEWeight_Type())
cucsQosclassEthBEWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthBEWeight.setStatus(_A)
_CucsQosclassEthClassifiedTable_Object=MibTable
cucsQosclassEthClassifiedTable=_CucsQosclassEthClassifiedTable_Object((1,3,6,1,4,1,9,9,719,1,42,4))
if mibBuilder.loadTexts:cucsQosclassEthClassifiedTable.setStatus(_A)
_CucsQosclassEthClassifiedEntry_Object=MibTableRow
cucsQosclassEthClassifiedEntry=_CucsQosclassEthClassifiedEntry_Object((1,3,6,1,4,1,9,9,719,1,42,4,1))
cucsQosclassEthClassifiedEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsQosclassEthClassifiedEntry.setStatus(_A)
_CucsQosclassEthClassifiedInstanceId_Type=CucsManagedObjectId
_CucsQosclassEthClassifiedInstanceId_Object=MibTableColumn
cucsQosclassEthClassifiedInstanceId=_CucsQosclassEthClassifiedInstanceId_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,1),_CucsQosclassEthClassifiedInstanceId_Type())
cucsQosclassEthClassifiedInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedInstanceId.setStatus(_A)
_CucsQosclassEthClassifiedDn_Type=CucsManagedObjectDn
_CucsQosclassEthClassifiedDn_Object=MibTableColumn
cucsQosclassEthClassifiedDn=_CucsQosclassEthClassifiedDn_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,2),_CucsQosclassEthClassifiedDn_Type())
cucsQosclassEthClassifiedDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedDn.setStatus(_A)
_CucsQosclassEthClassifiedRn_Type=SnmpAdminString
_CucsQosclassEthClassifiedRn_Object=MibTableColumn
cucsQosclassEthClassifiedRn=_CucsQosclassEthClassifiedRn_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,3),_CucsQosclassEthClassifiedRn_Type())
cucsQosclassEthClassifiedRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedRn.setStatus(_A)
_CucsQosclassEthClassifiedAdminState_Type=CucsQosclassEthClassifiedAdminState
_CucsQosclassEthClassifiedAdminState_Object=MibTableColumn
cucsQosclassEthClassifiedAdminState=_CucsQosclassEthClassifiedAdminState_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,4),_CucsQosclassEthClassifiedAdminState_Type())
cucsQosclassEthClassifiedAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedAdminState.setStatus(_A)
_CucsQosclassEthClassifiedBwPercent_Type=Gauge32
_CucsQosclassEthClassifiedBwPercent_Object=MibTableColumn
cucsQosclassEthClassifiedBwPercent=_CucsQosclassEthClassifiedBwPercent_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,5),_CucsQosclassEthClassifiedBwPercent_Type())
cucsQosclassEthClassifiedBwPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedBwPercent.setStatus(_A)
_CucsQosclassEthClassifiedCos_Type=Gauge32
_CucsQosclassEthClassifiedCos_Object=MibTableColumn
cucsQosclassEthClassifiedCos=_CucsQosclassEthClassifiedCos_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,6),_CucsQosclassEthClassifiedCos_Type())
cucsQosclassEthClassifiedCos.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedCos.setStatus(_A)
_CucsQosclassEthClassifiedDrop_Type=CucsQosclassEthClassifiedDrop
_CucsQosclassEthClassifiedDrop_Object=MibTableColumn
cucsQosclassEthClassifiedDrop=_CucsQosclassEthClassifiedDrop_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,7),_CucsQosclassEthClassifiedDrop_Type())
cucsQosclassEthClassifiedDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedDrop.setStatus(_A)
_CucsQosclassEthClassifiedMtu_Type=SnmpAdminString
_CucsQosclassEthClassifiedMtu_Object=MibTableColumn
cucsQosclassEthClassifiedMtu=_CucsQosclassEthClassifiedMtu_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,8),_CucsQosclassEthClassifiedMtu_Type())
cucsQosclassEthClassifiedMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedMtu.setStatus(_A)
_CucsQosclassEthClassifiedMulticastOptimize_Type=TruthValue
_CucsQosclassEthClassifiedMulticastOptimize_Object=MibTableColumn
cucsQosclassEthClassifiedMulticastOptimize=_CucsQosclassEthClassifiedMulticastOptimize_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,9),_CucsQosclassEthClassifiedMulticastOptimize_Type())
cucsQosclassEthClassifiedMulticastOptimize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedMulticastOptimize.setStatus(_A)
_CucsQosclassEthClassifiedName_Type=SnmpAdminString
_CucsQosclassEthClassifiedName_Object=MibTableColumn
cucsQosclassEthClassifiedName=_CucsQosclassEthClassifiedName_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,10),_CucsQosclassEthClassifiedName_Type())
cucsQosclassEthClassifiedName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedName.setStatus(_A)
_CucsQosclassEthClassifiedPriority_Type=CucsQosclassEthClassifiedPriority
_CucsQosclassEthClassifiedPriority_Object=MibTableColumn
cucsQosclassEthClassifiedPriority=_CucsQosclassEthClassifiedPriority_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,11),_CucsQosclassEthClassifiedPriority_Type())
cucsQosclassEthClassifiedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedPriority.setStatus(_A)
_CucsQosclassEthClassifiedWeight_Type=Gauge32
_CucsQosclassEthClassifiedWeight_Object=MibTableColumn
cucsQosclassEthClassifiedWeight=_CucsQosclassEthClassifiedWeight_Object((1,3,6,1,4,1,9,9,719,1,42,4,1,12),_CucsQosclassEthClassifiedWeight_Type())
cucsQosclassEthClassifiedWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassEthClassifiedWeight.setStatus(_A)
_CucsQosclassFcTable_Object=MibTable
cucsQosclassFcTable=_CucsQosclassFcTable_Object((1,3,6,1,4,1,9,9,719,1,42,5))
if mibBuilder.loadTexts:cucsQosclassFcTable.setStatus(_A)
_CucsQosclassFcEntry_Object=MibTableRow
cucsQosclassFcEntry=_CucsQosclassFcEntry_Object((1,3,6,1,4,1,9,9,719,1,42,5,1))
cucsQosclassFcEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsQosclassFcEntry.setStatus(_A)
_CucsQosclassFcInstanceId_Type=CucsManagedObjectId
_CucsQosclassFcInstanceId_Object=MibTableColumn
cucsQosclassFcInstanceId=_CucsQosclassFcInstanceId_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,1),_CucsQosclassFcInstanceId_Type())
cucsQosclassFcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsQosclassFcInstanceId.setStatus(_A)
_CucsQosclassFcDn_Type=CucsManagedObjectDn
_CucsQosclassFcDn_Object=MibTableColumn
cucsQosclassFcDn=_CucsQosclassFcDn_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,2),_CucsQosclassFcDn_Type())
cucsQosclassFcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcDn.setStatus(_A)
_CucsQosclassFcRn_Type=SnmpAdminString
_CucsQosclassFcRn_Object=MibTableColumn
cucsQosclassFcRn=_CucsQosclassFcRn_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,3),_CucsQosclassFcRn_Type())
cucsQosclassFcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcRn.setStatus(_A)
_CucsQosclassFcAdminState_Type=CucsQosclassFcAdminState
_CucsQosclassFcAdminState_Object=MibTableColumn
cucsQosclassFcAdminState=_CucsQosclassFcAdminState_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,4),_CucsQosclassFcAdminState_Type())
cucsQosclassFcAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcAdminState.setStatus(_A)
_CucsQosclassFcBwPercent_Type=Gauge32
_CucsQosclassFcBwPercent_Object=MibTableColumn
cucsQosclassFcBwPercent=_CucsQosclassFcBwPercent_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,5),_CucsQosclassFcBwPercent_Type())
cucsQosclassFcBwPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcBwPercent.setStatus(_A)
_CucsQosclassFcCos_Type=Gauge32
_CucsQosclassFcCos_Object=MibTableColumn
cucsQosclassFcCos=_CucsQosclassFcCos_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,6),_CucsQosclassFcCos_Type())
cucsQosclassFcCos.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcCos.setStatus(_A)
_CucsQosclassFcDrop_Type=CucsQosclassFcDrop
_CucsQosclassFcDrop_Object=MibTableColumn
cucsQosclassFcDrop=_CucsQosclassFcDrop_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,7),_CucsQosclassFcDrop_Type())
cucsQosclassFcDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcDrop.setStatus(_A)
_CucsQosclassFcMtu_Type=SnmpAdminString
_CucsQosclassFcMtu_Object=MibTableColumn
cucsQosclassFcMtu=_CucsQosclassFcMtu_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,8),_CucsQosclassFcMtu_Type())
cucsQosclassFcMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcMtu.setStatus(_A)
_CucsQosclassFcName_Type=SnmpAdminString
_CucsQosclassFcName_Object=MibTableColumn
cucsQosclassFcName=_CucsQosclassFcName_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,9),_CucsQosclassFcName_Type())
cucsQosclassFcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcName.setStatus(_A)
_CucsQosclassFcPriority_Type=CucsQosclassFcPriority
_CucsQosclassFcPriority_Object=MibTableColumn
cucsQosclassFcPriority=_CucsQosclassFcPriority_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,10),_CucsQosclassFcPriority_Type())
cucsQosclassFcPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcPriority.setStatus(_A)
_CucsQosclassFcWeight_Type=Gauge32
_CucsQosclassFcWeight_Object=MibTableColumn
cucsQosclassFcWeight=_CucsQosclassFcWeight_Object((1,3,6,1,4,1,9,9,719,1,42,5,1,11),_CucsQosclassFcWeight_Type())
cucsQosclassFcWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassFcWeight.setStatus(_A)
_CucsQosclassDefinitionFsmTable_Object=MibTable
cucsQosclassDefinitionFsmTable=_CucsQosclassDefinitionFsmTable_Object((1,3,6,1,4,1,9,9,719,1,42,6))
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmTable.setStatus(_A)
_CucsQosclassDefinitionFsmEntry_Object=MibTableRow
cucsQosclassDefinitionFsmEntry=_CucsQosclassDefinitionFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,42,6,1))
cucsQosclassDefinitionFsmEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmEntry.setStatus(_A)
_CucsQosclassDefinitionFsmInstanceId_Type=CucsManagedObjectId
_CucsQosclassDefinitionFsmInstanceId_Object=MibTableColumn
cucsQosclassDefinitionFsmInstanceId=_CucsQosclassDefinitionFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,1),_CucsQosclassDefinitionFsmInstanceId_Type())
cucsQosclassDefinitionFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmInstanceId.setStatus(_A)
_CucsQosclassDefinitionFsmDn_Type=CucsManagedObjectDn
_CucsQosclassDefinitionFsmDn_Object=MibTableColumn
cucsQosclassDefinitionFsmDn=_CucsQosclassDefinitionFsmDn_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,2),_CucsQosclassDefinitionFsmDn_Type())
cucsQosclassDefinitionFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmDn.setStatus(_A)
_CucsQosclassDefinitionFsmRn_Type=SnmpAdminString
_CucsQosclassDefinitionFsmRn_Object=MibTableColumn
cucsQosclassDefinitionFsmRn=_CucsQosclassDefinitionFsmRn_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,3),_CucsQosclassDefinitionFsmRn_Type())
cucsQosclassDefinitionFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmRn.setStatus(_A)
_CucsQosclassDefinitionFsmCompletionTime_Type=DateAndTime
_CucsQosclassDefinitionFsmCompletionTime_Object=MibTableColumn
cucsQosclassDefinitionFsmCompletionTime=_CucsQosclassDefinitionFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,4),_CucsQosclassDefinitionFsmCompletionTime_Type())
cucsQosclassDefinitionFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmCompletionTime.setStatus(_A)
_CucsQosclassDefinitionFsmCurrentFsm_Type=CucsQosclassDefinitionFsmCurrentFsm
_CucsQosclassDefinitionFsmCurrentFsm_Object=MibTableColumn
cucsQosclassDefinitionFsmCurrentFsm=_CucsQosclassDefinitionFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,5),_CucsQosclassDefinitionFsmCurrentFsm_Type())
cucsQosclassDefinitionFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmCurrentFsm.setStatus(_A)
_CucsQosclassDefinitionFsmDescrData_Type=SnmpAdminString
_CucsQosclassDefinitionFsmDescrData_Object=MibTableColumn
cucsQosclassDefinitionFsmDescrData=_CucsQosclassDefinitionFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,6),_CucsQosclassDefinitionFsmDescrData_Type())
cucsQosclassDefinitionFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmDescrData.setStatus(_A)
_CucsQosclassDefinitionFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsQosclassDefinitionFsmFsmStatus_Object=MibTableColumn
cucsQosclassDefinitionFsmFsmStatus=_CucsQosclassDefinitionFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,7),_CucsQosclassDefinitionFsmFsmStatus_Type())
cucsQosclassDefinitionFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmFsmStatus.setStatus(_A)
_CucsQosclassDefinitionFsmProgress_Type=Gauge32
_CucsQosclassDefinitionFsmProgress_Object=MibTableColumn
cucsQosclassDefinitionFsmProgress=_CucsQosclassDefinitionFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,8),_CucsQosclassDefinitionFsmProgress_Type())
cucsQosclassDefinitionFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmProgress.setStatus(_A)
_CucsQosclassDefinitionFsmRmtErrCode_Type=Gauge32
_CucsQosclassDefinitionFsmRmtErrCode_Object=MibTableColumn
cucsQosclassDefinitionFsmRmtErrCode=_CucsQosclassDefinitionFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,9),_CucsQosclassDefinitionFsmRmtErrCode_Type())
cucsQosclassDefinitionFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmRmtErrCode.setStatus(_A)
_CucsQosclassDefinitionFsmRmtErrDescr_Type=SnmpAdminString
_CucsQosclassDefinitionFsmRmtErrDescr_Object=MibTableColumn
cucsQosclassDefinitionFsmRmtErrDescr=_CucsQosclassDefinitionFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,10),_CucsQosclassDefinitionFsmRmtErrDescr_Type())
cucsQosclassDefinitionFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmRmtErrDescr.setStatus(_A)
_CucsQosclassDefinitionFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsQosclassDefinitionFsmRmtRslt_Object=MibTableColumn
cucsQosclassDefinitionFsmRmtRslt=_CucsQosclassDefinitionFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,42,6,1,11),_CucsQosclassDefinitionFsmRmtRslt_Type())
cucsQosclassDefinitionFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmRmtRslt.setStatus(_A)
_CucsQosclassDefinitionFsmStageTable_Object=MibTable
cucsQosclassDefinitionFsmStageTable=_CucsQosclassDefinitionFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,42,7))
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageTable.setStatus(_A)
_CucsQosclassDefinitionFsmStageEntry_Object=MibTableRow
cucsQosclassDefinitionFsmStageEntry=_CucsQosclassDefinitionFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,42,7,1))
cucsQosclassDefinitionFsmStageEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageEntry.setStatus(_A)
_CucsQosclassDefinitionFsmStageInstanceId_Type=CucsManagedObjectId
_CucsQosclassDefinitionFsmStageInstanceId_Object=MibTableColumn
cucsQosclassDefinitionFsmStageInstanceId=_CucsQosclassDefinitionFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,42,7,1,1),_CucsQosclassDefinitionFsmStageInstanceId_Type())
cucsQosclassDefinitionFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageInstanceId.setStatus(_A)
_CucsQosclassDefinitionFsmStageDn_Type=CucsManagedObjectDn
_CucsQosclassDefinitionFsmStageDn_Object=MibTableColumn
cucsQosclassDefinitionFsmStageDn=_CucsQosclassDefinitionFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,42,7,1,2),_CucsQosclassDefinitionFsmStageDn_Type())
cucsQosclassDefinitionFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageDn.setStatus(_A)
_CucsQosclassDefinitionFsmStageRn_Type=SnmpAdminString
_CucsQosclassDefinitionFsmStageRn_Object=MibTableColumn
cucsQosclassDefinitionFsmStageRn=_CucsQosclassDefinitionFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,42,7,1,3),_CucsQosclassDefinitionFsmStageRn_Type())
cucsQosclassDefinitionFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageRn.setStatus(_A)
_CucsQosclassDefinitionFsmStageDescrData_Type=SnmpAdminString
_CucsQosclassDefinitionFsmStageDescrData_Object=MibTableColumn
cucsQosclassDefinitionFsmStageDescrData=_CucsQosclassDefinitionFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,42,7,1,4),_CucsQosclassDefinitionFsmStageDescrData_Type())
cucsQosclassDefinitionFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageDescrData.setStatus(_A)
_CucsQosclassDefinitionFsmStageLastUpdateTime_Type=DateAndTime
_CucsQosclassDefinitionFsmStageLastUpdateTime_Object=MibTableColumn
cucsQosclassDefinitionFsmStageLastUpdateTime=_CucsQosclassDefinitionFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,42,7,1,5),_CucsQosclassDefinitionFsmStageLastUpdateTime_Type())
cucsQosclassDefinitionFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageLastUpdateTime.setStatus(_A)
_CucsQosclassDefinitionFsmStageName_Type=CucsQosclassDefinitionFsmStageName
_CucsQosclassDefinitionFsmStageName_Object=MibTableColumn
cucsQosclassDefinitionFsmStageName=_CucsQosclassDefinitionFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,42,7,1,6),_CucsQosclassDefinitionFsmStageName_Type())
cucsQosclassDefinitionFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageName.setStatus(_A)
_CucsQosclassDefinitionFsmStageOrder_Type=Gauge32
_CucsQosclassDefinitionFsmStageOrder_Object=MibTableColumn
cucsQosclassDefinitionFsmStageOrder=_CucsQosclassDefinitionFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,42,7,1,7),_CucsQosclassDefinitionFsmStageOrder_Type())
cucsQosclassDefinitionFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageOrder.setStatus(_A)
_CucsQosclassDefinitionFsmStageRetry_Type=Gauge32
_CucsQosclassDefinitionFsmStageRetry_Object=MibTableColumn
cucsQosclassDefinitionFsmStageRetry=_CucsQosclassDefinitionFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,42,7,1,8),_CucsQosclassDefinitionFsmStageRetry_Type())
cucsQosclassDefinitionFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageRetry.setStatus(_A)
_CucsQosclassDefinitionFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsQosclassDefinitionFsmStageStageStatus_Object=MibTableColumn
cucsQosclassDefinitionFsmStageStageStatus=_CucsQosclassDefinitionFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,42,7,1,9),_CucsQosclassDefinitionFsmStageStageStatus_Type())
cucsQosclassDefinitionFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQosclassDefinitionFsmStageStageStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsQosclassObjects':cucsQosclassObjects,'cucsQosclassDefinitionTable':cucsQosclassDefinitionTable,'cucsQosclassDefinitionEntry':cucsQosclassDefinitionEntry,_E:cucsQosclassDefinitionInstanceId,'cucsQosclassDefinitionDn':cucsQosclassDefinitionDn,'cucsQosclassDefinitionRn':cucsQosclassDefinitionRn,'cucsQosclassDefinitionDescr':cucsQosclassDefinitionDescr,'cucsQosclassDefinitionFsmDescr':cucsQosclassDefinitionFsmDescr,'cucsQosclassDefinitionFsmPrev':cucsQosclassDefinitionFsmPrev,'cucsQosclassDefinitionFsmProgr':cucsQosclassDefinitionFsmProgr,'cucsQosclassDefinitionFsmRmtInvErrCode':cucsQosclassDefinitionFsmRmtInvErrCode,'cucsQosclassDefinitionFsmRmtInvErrDescr':cucsQosclassDefinitionFsmRmtInvErrDescr,'cucsQosclassDefinitionFsmRmtInvRslt':cucsQosclassDefinitionFsmRmtInvRslt,'cucsQosclassDefinitionFsmStageDescr':cucsQosclassDefinitionFsmStageDescr,'cucsQosclassDefinitionFsmStamp':cucsQosclassDefinitionFsmStamp,'cucsQosclassDefinitionFsmStatus':cucsQosclassDefinitionFsmStatus,'cucsQosclassDefinitionFsmTry':cucsQosclassDefinitionFsmTry,'cucsQosclassDefinitionIntId':cucsQosclassDefinitionIntId,'cucsQosclassDefinitionName':cucsQosclassDefinitionName,'cucsQosclassDefinitionPolicyLevel':cucsQosclassDefinitionPolicyLevel,'cucsQosclassDefinitionPolicyOwner':cucsQosclassDefinitionPolicyOwner,'cucsQosclassDefinitionMmuPercent':cucsQosclassDefinitionMmuPercent,'cucsQosclassDefinitionNumBreakoutPort':cucsQosclassDefinitionNumBreakoutPort,'cucsQosclassDefinitionFsmTaskTable':cucsQosclassDefinitionFsmTaskTable,'cucsQosclassDefinitionFsmTaskEntry':cucsQosclassDefinitionFsmTaskEntry,_F:cucsQosclassDefinitionFsmTaskInstanceId,'cucsQosclassDefinitionFsmTaskDn':cucsQosclassDefinitionFsmTaskDn,'cucsQosclassDefinitionFsmTaskRn':cucsQosclassDefinitionFsmTaskRn,'cucsQosclassDefinitionFsmTaskCompletion':cucsQosclassDefinitionFsmTaskCompletion,'cucsQosclassDefinitionFsmTaskFlags':cucsQosclassDefinitionFsmTaskFlags,'cucsQosclassDefinitionFsmTaskItem':cucsQosclassDefinitionFsmTaskItem,'cucsQosclassDefinitionFsmTaskSeqId':cucsQosclassDefinitionFsmTaskSeqId,'cucsQosclassEthBETable':cucsQosclassEthBETable,'cucsQosclassEthBEEntry':cucsQosclassEthBEEntry,_G:cucsQosclassEthBEInstanceId,'cucsQosclassEthBEDn':cucsQosclassEthBEDn,'cucsQosclassEthBERn':cucsQosclassEthBERn,'cucsQosclassEthBEAdminState':cucsQosclassEthBEAdminState,'cucsQosclassEthBEBwPercent':cucsQosclassEthBEBwPercent,'cucsQosclassEthBECos':cucsQosclassEthBECos,'cucsQosclassEthBEDrop':cucsQosclassEthBEDrop,'cucsQosclassEthBEMtu':cucsQosclassEthBEMtu,'cucsQosclassEthBEMulticastOptimize':cucsQosclassEthBEMulticastOptimize,'cucsQosclassEthBEName':cucsQosclassEthBEName,'cucsQosclassEthBEPriority':cucsQosclassEthBEPriority,'cucsQosclassEthBEWeight':cucsQosclassEthBEWeight,'cucsQosclassEthClassifiedTable':cucsQosclassEthClassifiedTable,'cucsQosclassEthClassifiedEntry':cucsQosclassEthClassifiedEntry,_H:cucsQosclassEthClassifiedInstanceId,'cucsQosclassEthClassifiedDn':cucsQosclassEthClassifiedDn,'cucsQosclassEthClassifiedRn':cucsQosclassEthClassifiedRn,'cucsQosclassEthClassifiedAdminState':cucsQosclassEthClassifiedAdminState,'cucsQosclassEthClassifiedBwPercent':cucsQosclassEthClassifiedBwPercent,'cucsQosclassEthClassifiedCos':cucsQosclassEthClassifiedCos,'cucsQosclassEthClassifiedDrop':cucsQosclassEthClassifiedDrop,'cucsQosclassEthClassifiedMtu':cucsQosclassEthClassifiedMtu,'cucsQosclassEthClassifiedMulticastOptimize':cucsQosclassEthClassifiedMulticastOptimize,'cucsQosclassEthClassifiedName':cucsQosclassEthClassifiedName,'cucsQosclassEthClassifiedPriority':cucsQosclassEthClassifiedPriority,'cucsQosclassEthClassifiedWeight':cucsQosclassEthClassifiedWeight,'cucsQosclassFcTable':cucsQosclassFcTable,'cucsQosclassFcEntry':cucsQosclassFcEntry,_I:cucsQosclassFcInstanceId,'cucsQosclassFcDn':cucsQosclassFcDn,'cucsQosclassFcRn':cucsQosclassFcRn,'cucsQosclassFcAdminState':cucsQosclassFcAdminState,'cucsQosclassFcBwPercent':cucsQosclassFcBwPercent,'cucsQosclassFcCos':cucsQosclassFcCos,'cucsQosclassFcDrop':cucsQosclassFcDrop,'cucsQosclassFcMtu':cucsQosclassFcMtu,'cucsQosclassFcName':cucsQosclassFcName,'cucsQosclassFcPriority':cucsQosclassFcPriority,'cucsQosclassFcWeight':cucsQosclassFcWeight,'cucsQosclassDefinitionFsmTable':cucsQosclassDefinitionFsmTable,'cucsQosclassDefinitionFsmEntry':cucsQosclassDefinitionFsmEntry,_J:cucsQosclassDefinitionFsmInstanceId,'cucsQosclassDefinitionFsmDn':cucsQosclassDefinitionFsmDn,'cucsQosclassDefinitionFsmRn':cucsQosclassDefinitionFsmRn,'cucsQosclassDefinitionFsmCompletionTime':cucsQosclassDefinitionFsmCompletionTime,'cucsQosclassDefinitionFsmCurrentFsm':cucsQosclassDefinitionFsmCurrentFsm,'cucsQosclassDefinitionFsmDescrData':cucsQosclassDefinitionFsmDescrData,'cucsQosclassDefinitionFsmFsmStatus':cucsQosclassDefinitionFsmFsmStatus,'cucsQosclassDefinitionFsmProgress':cucsQosclassDefinitionFsmProgress,'cucsQosclassDefinitionFsmRmtErrCode':cucsQosclassDefinitionFsmRmtErrCode,'cucsQosclassDefinitionFsmRmtErrDescr':cucsQosclassDefinitionFsmRmtErrDescr,'cucsQosclassDefinitionFsmRmtRslt':cucsQosclassDefinitionFsmRmtRslt,'cucsQosclassDefinitionFsmStageTable':cucsQosclassDefinitionFsmStageTable,'cucsQosclassDefinitionFsmStageEntry':cucsQosclassDefinitionFsmStageEntry,_K:cucsQosclassDefinitionFsmStageInstanceId,'cucsQosclassDefinitionFsmStageDn':cucsQosclassDefinitionFsmStageDn,'cucsQosclassDefinitionFsmStageRn':cucsQosclassDefinitionFsmStageRn,'cucsQosclassDefinitionFsmStageDescrData':cucsQosclassDefinitionFsmStageDescrData,'cucsQosclassDefinitionFsmStageLastUpdateTime':cucsQosclassDefinitionFsmStageLastUpdateTime,'cucsQosclassDefinitionFsmStageName':cucsQosclassDefinitionFsmStageName,'cucsQosclassDefinitionFsmStageOrder':cucsQosclassDefinitionFsmStageOrder,'cucsQosclassDefinitionFsmStageRetry':cucsQosclassDefinitionFsmStageRetry,'cucsQosclassDefinitionFsmStageStageStatus':cucsQosclassDefinitionFsmStageStageStatus})