_I='cucsSysfileMutationFsmStageInstanceId'
_H='cucsSysfileMutationFsmInstanceId'
_G='cucsSysfileDigestInstanceId'
_F='cucsSysfileMutationFsmTaskInstanceId'
_E='cucsSysfileMutationInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-SYSFILE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsConditionRemoteInvRslt,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsNetworkSwitchId,CucsSysfileMutationAction,CucsSysfileMutationFsmCurrentFsm,CucsSysfileMutationFsmStageName,CucsSysfileMutationFsmTaskItem=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsConditionRemoteInvRslt','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsNetworkSwitchId','CucsSysfileMutationAction','CucsSysfileMutationFsmCurrentFsm','CucsSysfileMutationFsmStageName','CucsSysfileMutationFsmTaskItem')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsSysfileObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,48))
_CucsSysfileMutationTable_Object=MibTable
cucsSysfileMutationTable=_CucsSysfileMutationTable_Object((1,3,6,1,4,1,9,9,719,1,48,1))
if mibBuilder.loadTexts:cucsSysfileMutationTable.setStatus(_A)
_CucsSysfileMutationEntry_Object=MibTableRow
cucsSysfileMutationEntry=_CucsSysfileMutationEntry_Object((1,3,6,1,4,1,9,9,719,1,48,1,1))
cucsSysfileMutationEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsSysfileMutationEntry.setStatus(_A)
_CucsSysfileMutationInstanceId_Type=CucsManagedObjectId
_CucsSysfileMutationInstanceId_Object=MibTableColumn
cucsSysfileMutationInstanceId=_CucsSysfileMutationInstanceId_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,1),_CucsSysfileMutationInstanceId_Type())
cucsSysfileMutationInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsSysfileMutationInstanceId.setStatus(_A)
_CucsSysfileMutationDn_Type=CucsManagedObjectDn
_CucsSysfileMutationDn_Object=MibTableColumn
cucsSysfileMutationDn=_CucsSysfileMutationDn_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,2),_CucsSysfileMutationDn_Type())
cucsSysfileMutationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationDn.setStatus(_A)
_CucsSysfileMutationRn_Type=SnmpAdminString
_CucsSysfileMutationRn_Object=MibTableColumn
cucsSysfileMutationRn=_CucsSysfileMutationRn_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,3),_CucsSysfileMutationRn_Type())
cucsSysfileMutationRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationRn.setStatus(_A)
_CucsSysfileMutationAction_Type=CucsSysfileMutationAction
_CucsSysfileMutationAction_Object=MibTableColumn
cucsSysfileMutationAction=_CucsSysfileMutationAction_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,4),_CucsSysfileMutationAction_Type())
cucsSysfileMutationAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationAction.setStatus(_A)
_CucsSysfileMutationDescr_Type=SnmpAdminString
_CucsSysfileMutationDescr_Object=MibTableColumn
cucsSysfileMutationDescr=_CucsSysfileMutationDescr_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,5),_CucsSysfileMutationDescr_Type())
cucsSysfileMutationDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationDescr.setStatus(_A)
_CucsSysfileMutationFsmDescr_Type=SnmpAdminString
_CucsSysfileMutationFsmDescr_Object=MibTableColumn
cucsSysfileMutationFsmDescr=_CucsSysfileMutationFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,6),_CucsSysfileMutationFsmDescr_Type())
cucsSysfileMutationFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmDescr.setStatus(_A)
_CucsSysfileMutationFsmPrev_Type=SnmpAdminString
_CucsSysfileMutationFsmPrev_Object=MibTableColumn
cucsSysfileMutationFsmPrev=_CucsSysfileMutationFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,7),_CucsSysfileMutationFsmPrev_Type())
cucsSysfileMutationFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmPrev.setStatus(_A)
_CucsSysfileMutationFsmProgr_Type=Gauge32
_CucsSysfileMutationFsmProgr_Object=MibTableColumn
cucsSysfileMutationFsmProgr=_CucsSysfileMutationFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,8),_CucsSysfileMutationFsmProgr_Type())
cucsSysfileMutationFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmProgr.setStatus(_A)
_CucsSysfileMutationFsmRmtInvErrCode_Type=Gauge32
_CucsSysfileMutationFsmRmtInvErrCode_Object=MibTableColumn
cucsSysfileMutationFsmRmtInvErrCode=_CucsSysfileMutationFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,9),_CucsSysfileMutationFsmRmtInvErrCode_Type())
cucsSysfileMutationFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmRmtInvErrCode.setStatus(_A)
_CucsSysfileMutationFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsSysfileMutationFsmRmtInvErrDescr_Object=MibTableColumn
cucsSysfileMutationFsmRmtInvErrDescr=_CucsSysfileMutationFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,10),_CucsSysfileMutationFsmRmtInvErrDescr_Type())
cucsSysfileMutationFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmRmtInvErrDescr.setStatus(_A)
_CucsSysfileMutationFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsSysfileMutationFsmRmtInvRslt_Object=MibTableColumn
cucsSysfileMutationFsmRmtInvRslt=_CucsSysfileMutationFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,11),_CucsSysfileMutationFsmRmtInvRslt_Type())
cucsSysfileMutationFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmRmtInvRslt.setStatus(_A)
_CucsSysfileMutationFsmStageDescr_Type=SnmpAdminString
_CucsSysfileMutationFsmStageDescr_Object=MibTableColumn
cucsSysfileMutationFsmStageDescr=_CucsSysfileMutationFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,12),_CucsSysfileMutationFsmStageDescr_Type())
cucsSysfileMutationFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageDescr.setStatus(_A)
_CucsSysfileMutationFsmStamp_Type=DateAndTime
_CucsSysfileMutationFsmStamp_Object=MibTableColumn
cucsSysfileMutationFsmStamp=_CucsSysfileMutationFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,13),_CucsSysfileMutationFsmStamp_Type())
cucsSysfileMutationFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStamp.setStatus(_A)
_CucsSysfileMutationFsmStatus_Type=SnmpAdminString
_CucsSysfileMutationFsmStatus_Object=MibTableColumn
cucsSysfileMutationFsmStatus=_CucsSysfileMutationFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,14),_CucsSysfileMutationFsmStatus_Type())
cucsSysfileMutationFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStatus.setStatus(_A)
_CucsSysfileMutationFsmTry_Type=Gauge32
_CucsSysfileMutationFsmTry_Object=MibTableColumn
cucsSysfileMutationFsmTry=_CucsSysfileMutationFsmTry_Object((1,3,6,1,4,1,9,9,719,1,48,1,1,15),_CucsSysfileMutationFsmTry_Type())
cucsSysfileMutationFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmTry.setStatus(_A)
_CucsSysfileMutationFsmTaskTable_Object=MibTable
cucsSysfileMutationFsmTaskTable=_CucsSysfileMutationFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,48,2))
if mibBuilder.loadTexts:cucsSysfileMutationFsmTaskTable.setStatus(_A)
_CucsSysfileMutationFsmTaskEntry_Object=MibTableRow
cucsSysfileMutationFsmTaskEntry=_CucsSysfileMutationFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,48,2,1))
cucsSysfileMutationFsmTaskEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsSysfileMutationFsmTaskEntry.setStatus(_A)
_CucsSysfileMutationFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsSysfileMutationFsmTaskInstanceId_Object=MibTableColumn
cucsSysfileMutationFsmTaskInstanceId=_CucsSysfileMutationFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,48,2,1,1),_CucsSysfileMutationFsmTaskInstanceId_Type())
cucsSysfileMutationFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsSysfileMutationFsmTaskInstanceId.setStatus(_A)
_CucsSysfileMutationFsmTaskDn_Type=CucsManagedObjectDn
_CucsSysfileMutationFsmTaskDn_Object=MibTableColumn
cucsSysfileMutationFsmTaskDn=_CucsSysfileMutationFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,48,2,1,2),_CucsSysfileMutationFsmTaskDn_Type())
cucsSysfileMutationFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmTaskDn.setStatus(_A)
_CucsSysfileMutationFsmTaskRn_Type=SnmpAdminString
_CucsSysfileMutationFsmTaskRn_Object=MibTableColumn
cucsSysfileMutationFsmTaskRn=_CucsSysfileMutationFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,48,2,1,3),_CucsSysfileMutationFsmTaskRn_Type())
cucsSysfileMutationFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmTaskRn.setStatus(_A)
_CucsSysfileMutationFsmTaskCompletion_Type=CucsFsmCompletion
_CucsSysfileMutationFsmTaskCompletion_Object=MibTableColumn
cucsSysfileMutationFsmTaskCompletion=_CucsSysfileMutationFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,48,2,1,4),_CucsSysfileMutationFsmTaskCompletion_Type())
cucsSysfileMutationFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmTaskCompletion.setStatus(_A)
_CucsSysfileMutationFsmTaskFlags_Type=CucsFsmFlags
_CucsSysfileMutationFsmTaskFlags_Object=MibTableColumn
cucsSysfileMutationFsmTaskFlags=_CucsSysfileMutationFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,48,2,1,5),_CucsSysfileMutationFsmTaskFlags_Type())
cucsSysfileMutationFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmTaskFlags.setStatus(_A)
_CucsSysfileMutationFsmTaskItem_Type=CucsSysfileMutationFsmTaskItem
_CucsSysfileMutationFsmTaskItem_Object=MibTableColumn
cucsSysfileMutationFsmTaskItem=_CucsSysfileMutationFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,48,2,1,6),_CucsSysfileMutationFsmTaskItem_Type())
cucsSysfileMutationFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmTaskItem.setStatus(_A)
_CucsSysfileMutationFsmTaskSeqId_Type=Gauge32
_CucsSysfileMutationFsmTaskSeqId_Object=MibTableColumn
cucsSysfileMutationFsmTaskSeqId=_CucsSysfileMutationFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,48,2,1,7),_CucsSysfileMutationFsmTaskSeqId_Type())
cucsSysfileMutationFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmTaskSeqId.setStatus(_A)
_CucsSysfileDigestTable_Object=MibTable
cucsSysfileDigestTable=_CucsSysfileDigestTable_Object((1,3,6,1,4,1,9,9,719,1,48,3))
if mibBuilder.loadTexts:cucsSysfileDigestTable.setStatus(_A)
_CucsSysfileDigestEntry_Object=MibTableRow
cucsSysfileDigestEntry=_CucsSysfileDigestEntry_Object((1,3,6,1,4,1,9,9,719,1,48,3,1))
cucsSysfileDigestEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsSysfileDigestEntry.setStatus(_A)
_CucsSysfileDigestInstanceId_Type=CucsManagedObjectId
_CucsSysfileDigestInstanceId_Object=MibTableColumn
cucsSysfileDigestInstanceId=_CucsSysfileDigestInstanceId_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,1),_CucsSysfileDigestInstanceId_Type())
cucsSysfileDigestInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsSysfileDigestInstanceId.setStatus(_A)
_CucsSysfileDigestDn_Type=CucsManagedObjectDn
_CucsSysfileDigestDn_Object=MibTableColumn
cucsSysfileDigestDn=_CucsSysfileDigestDn_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,2),_CucsSysfileDigestDn_Type())
cucsSysfileDigestDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestDn.setStatus(_A)
_CucsSysfileDigestRn_Type=SnmpAdminString
_CucsSysfileDigestRn_Object=MibTableColumn
cucsSysfileDigestRn=_CucsSysfileDigestRn_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,3),_CucsSysfileDigestRn_Type())
cucsSysfileDigestRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestRn.setStatus(_A)
_CucsSysfileDigestCreationTS_Type=Unsigned64
_CucsSysfileDigestCreationTS_Object=MibTableColumn
cucsSysfileDigestCreationTS=_CucsSysfileDigestCreationTS_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,4),_CucsSysfileDigestCreationTS_Type())
cucsSysfileDigestCreationTS.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestCreationTS.setStatus(_A)
_CucsSysfileDigestDescr_Type=SnmpAdminString
_CucsSysfileDigestDescr_Object=MibTableColumn
cucsSysfileDigestDescr=_CucsSysfileDigestDescr_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,5),_CucsSysfileDigestDescr_Type())
cucsSysfileDigestDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestDescr.setStatus(_A)
_CucsSysfileDigestName_Type=SnmpAdminString
_CucsSysfileDigestName_Object=MibTableColumn
cucsSysfileDigestName=_CucsSysfileDigestName_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,6),_CucsSysfileDigestName_Type())
cucsSysfileDigestName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestName.setStatus(_A)
_CucsSysfileDigestSize_Type=Gauge32
_CucsSysfileDigestSize_Object=MibTableColumn
cucsSysfileDigestSize=_CucsSysfileDigestSize_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,7),_CucsSysfileDigestSize_Type())
cucsSysfileDigestSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestSize.setStatus(_A)
_CucsSysfileDigestSource_Type=SnmpAdminString
_CucsSysfileDigestSource_Object=MibTableColumn
cucsSysfileDigestSource=_CucsSysfileDigestSource_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,8),_CucsSysfileDigestSource_Type())
cucsSysfileDigestSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestSource.setStatus(_A)
_CucsSysfileDigestSwitchId_Type=CucsNetworkSwitchId
_CucsSysfileDigestSwitchId_Object=MibTableColumn
cucsSysfileDigestSwitchId=_CucsSysfileDigestSwitchId_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,9),_CucsSysfileDigestSwitchId_Type())
cucsSysfileDigestSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestSwitchId.setStatus(_A)
_CucsSysfileDigestTs_Type=DateAndTime
_CucsSysfileDigestTs_Object=MibTableColumn
cucsSysfileDigestTs=_CucsSysfileDigestTs_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,10),_CucsSysfileDigestTs_Type())
cucsSysfileDigestTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestTs.setStatus(_A)
_CucsSysfileDigestUri_Type=SnmpAdminString
_CucsSysfileDigestUri_Object=MibTableColumn
cucsSysfileDigestUri=_CucsSysfileDigestUri_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,11),_CucsSysfileDigestUri_Type())
cucsSysfileDigestUri.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestUri.setStatus(_A)
_CucsSysfileDigestChecksum_Type=SnmpAdminString
_CucsSysfileDigestChecksum_Object=MibTableColumn
cucsSysfileDigestChecksum=_CucsSysfileDigestChecksum_Object((1,3,6,1,4,1,9,9,719,1,48,3,1,12),_CucsSysfileDigestChecksum_Type())
cucsSysfileDigestChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileDigestChecksum.setStatus(_A)
_CucsSysfileMutationFsmTable_Object=MibTable
cucsSysfileMutationFsmTable=_CucsSysfileMutationFsmTable_Object((1,3,6,1,4,1,9,9,719,1,48,4))
if mibBuilder.loadTexts:cucsSysfileMutationFsmTable.setStatus(_A)
_CucsSysfileMutationFsmEntry_Object=MibTableRow
cucsSysfileMutationFsmEntry=_CucsSysfileMutationFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,48,4,1))
cucsSysfileMutationFsmEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsSysfileMutationFsmEntry.setStatus(_A)
_CucsSysfileMutationFsmInstanceId_Type=CucsManagedObjectId
_CucsSysfileMutationFsmInstanceId_Object=MibTableColumn
cucsSysfileMutationFsmInstanceId=_CucsSysfileMutationFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,1),_CucsSysfileMutationFsmInstanceId_Type())
cucsSysfileMutationFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsSysfileMutationFsmInstanceId.setStatus(_A)
_CucsSysfileMutationFsmDn_Type=CucsManagedObjectDn
_CucsSysfileMutationFsmDn_Object=MibTableColumn
cucsSysfileMutationFsmDn=_CucsSysfileMutationFsmDn_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,2),_CucsSysfileMutationFsmDn_Type())
cucsSysfileMutationFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmDn.setStatus(_A)
_CucsSysfileMutationFsmRn_Type=SnmpAdminString
_CucsSysfileMutationFsmRn_Object=MibTableColumn
cucsSysfileMutationFsmRn=_CucsSysfileMutationFsmRn_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,3),_CucsSysfileMutationFsmRn_Type())
cucsSysfileMutationFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmRn.setStatus(_A)
_CucsSysfileMutationFsmCompletionTime_Type=DateAndTime
_CucsSysfileMutationFsmCompletionTime_Object=MibTableColumn
cucsSysfileMutationFsmCompletionTime=_CucsSysfileMutationFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,4),_CucsSysfileMutationFsmCompletionTime_Type())
cucsSysfileMutationFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmCompletionTime.setStatus(_A)
_CucsSysfileMutationFsmCurrentFsm_Type=CucsSysfileMutationFsmCurrentFsm
_CucsSysfileMutationFsmCurrentFsm_Object=MibTableColumn
cucsSysfileMutationFsmCurrentFsm=_CucsSysfileMutationFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,5),_CucsSysfileMutationFsmCurrentFsm_Type())
cucsSysfileMutationFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmCurrentFsm.setStatus(_A)
_CucsSysfileMutationFsmDescrData_Type=SnmpAdminString
_CucsSysfileMutationFsmDescrData_Object=MibTableColumn
cucsSysfileMutationFsmDescrData=_CucsSysfileMutationFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,6),_CucsSysfileMutationFsmDescrData_Type())
cucsSysfileMutationFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmDescrData.setStatus(_A)
_CucsSysfileMutationFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsSysfileMutationFsmFsmStatus_Object=MibTableColumn
cucsSysfileMutationFsmFsmStatus=_CucsSysfileMutationFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,7),_CucsSysfileMutationFsmFsmStatus_Type())
cucsSysfileMutationFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmFsmStatus.setStatus(_A)
_CucsSysfileMutationFsmProgress_Type=Gauge32
_CucsSysfileMutationFsmProgress_Object=MibTableColumn
cucsSysfileMutationFsmProgress=_CucsSysfileMutationFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,8),_CucsSysfileMutationFsmProgress_Type())
cucsSysfileMutationFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmProgress.setStatus(_A)
_CucsSysfileMutationFsmRmtErrCode_Type=Gauge32
_CucsSysfileMutationFsmRmtErrCode_Object=MibTableColumn
cucsSysfileMutationFsmRmtErrCode=_CucsSysfileMutationFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,9),_CucsSysfileMutationFsmRmtErrCode_Type())
cucsSysfileMutationFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmRmtErrCode.setStatus(_A)
_CucsSysfileMutationFsmRmtErrDescr_Type=SnmpAdminString
_CucsSysfileMutationFsmRmtErrDescr_Object=MibTableColumn
cucsSysfileMutationFsmRmtErrDescr=_CucsSysfileMutationFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,10),_CucsSysfileMutationFsmRmtErrDescr_Type())
cucsSysfileMutationFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmRmtErrDescr.setStatus(_A)
_CucsSysfileMutationFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsSysfileMutationFsmRmtRslt_Object=MibTableColumn
cucsSysfileMutationFsmRmtRslt=_CucsSysfileMutationFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,48,4,1,11),_CucsSysfileMutationFsmRmtRslt_Type())
cucsSysfileMutationFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmRmtRslt.setStatus(_A)
_CucsSysfileMutationFsmStageTable_Object=MibTable
cucsSysfileMutationFsmStageTable=_CucsSysfileMutationFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,48,5))
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageTable.setStatus(_A)
_CucsSysfileMutationFsmStageEntry_Object=MibTableRow
cucsSysfileMutationFsmStageEntry=_CucsSysfileMutationFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,48,5,1))
cucsSysfileMutationFsmStageEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageEntry.setStatus(_A)
_CucsSysfileMutationFsmStageInstanceId_Type=CucsManagedObjectId
_CucsSysfileMutationFsmStageInstanceId_Object=MibTableColumn
cucsSysfileMutationFsmStageInstanceId=_CucsSysfileMutationFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,48,5,1,1),_CucsSysfileMutationFsmStageInstanceId_Type())
cucsSysfileMutationFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageInstanceId.setStatus(_A)
_CucsSysfileMutationFsmStageDn_Type=CucsManagedObjectDn
_CucsSysfileMutationFsmStageDn_Object=MibTableColumn
cucsSysfileMutationFsmStageDn=_CucsSysfileMutationFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,48,5,1,2),_CucsSysfileMutationFsmStageDn_Type())
cucsSysfileMutationFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageDn.setStatus(_A)
_CucsSysfileMutationFsmStageRn_Type=SnmpAdminString
_CucsSysfileMutationFsmStageRn_Object=MibTableColumn
cucsSysfileMutationFsmStageRn=_CucsSysfileMutationFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,48,5,1,3),_CucsSysfileMutationFsmStageRn_Type())
cucsSysfileMutationFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageRn.setStatus(_A)
_CucsSysfileMutationFsmStageDescrData_Type=SnmpAdminString
_CucsSysfileMutationFsmStageDescrData_Object=MibTableColumn
cucsSysfileMutationFsmStageDescrData=_CucsSysfileMutationFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,48,5,1,4),_CucsSysfileMutationFsmStageDescrData_Type())
cucsSysfileMutationFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageDescrData.setStatus(_A)
_CucsSysfileMutationFsmStageLastUpdateTime_Type=DateAndTime
_CucsSysfileMutationFsmStageLastUpdateTime_Object=MibTableColumn
cucsSysfileMutationFsmStageLastUpdateTime=_CucsSysfileMutationFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,48,5,1,5),_CucsSysfileMutationFsmStageLastUpdateTime_Type())
cucsSysfileMutationFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageLastUpdateTime.setStatus(_A)
_CucsSysfileMutationFsmStageName_Type=CucsSysfileMutationFsmStageName
_CucsSysfileMutationFsmStageName_Object=MibTableColumn
cucsSysfileMutationFsmStageName=_CucsSysfileMutationFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,48,5,1,6),_CucsSysfileMutationFsmStageName_Type())
cucsSysfileMutationFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageName.setStatus(_A)
_CucsSysfileMutationFsmStageOrder_Type=Gauge32
_CucsSysfileMutationFsmStageOrder_Object=MibTableColumn
cucsSysfileMutationFsmStageOrder=_CucsSysfileMutationFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,48,5,1,7),_CucsSysfileMutationFsmStageOrder_Type())
cucsSysfileMutationFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageOrder.setStatus(_A)
_CucsSysfileMutationFsmStageRetry_Type=Gauge32
_CucsSysfileMutationFsmStageRetry_Object=MibTableColumn
cucsSysfileMutationFsmStageRetry=_CucsSysfileMutationFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,48,5,1,8),_CucsSysfileMutationFsmStageRetry_Type())
cucsSysfileMutationFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageRetry.setStatus(_A)
_CucsSysfileMutationFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsSysfileMutationFsmStageStageStatus_Object=MibTableColumn
cucsSysfileMutationFsmStageStageStatus=_CucsSysfileMutationFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,48,5,1,9),_CucsSysfileMutationFsmStageStageStatus_Type())
cucsSysfileMutationFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSysfileMutationFsmStageStageStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsSysfileObjects':cucsSysfileObjects,'cucsSysfileMutationTable':cucsSysfileMutationTable,'cucsSysfileMutationEntry':cucsSysfileMutationEntry,_E:cucsSysfileMutationInstanceId,'cucsSysfileMutationDn':cucsSysfileMutationDn,'cucsSysfileMutationRn':cucsSysfileMutationRn,'cucsSysfileMutationAction':cucsSysfileMutationAction,'cucsSysfileMutationDescr':cucsSysfileMutationDescr,'cucsSysfileMutationFsmDescr':cucsSysfileMutationFsmDescr,'cucsSysfileMutationFsmPrev':cucsSysfileMutationFsmPrev,'cucsSysfileMutationFsmProgr':cucsSysfileMutationFsmProgr,'cucsSysfileMutationFsmRmtInvErrCode':cucsSysfileMutationFsmRmtInvErrCode,'cucsSysfileMutationFsmRmtInvErrDescr':cucsSysfileMutationFsmRmtInvErrDescr,'cucsSysfileMutationFsmRmtInvRslt':cucsSysfileMutationFsmRmtInvRslt,'cucsSysfileMutationFsmStageDescr':cucsSysfileMutationFsmStageDescr,'cucsSysfileMutationFsmStamp':cucsSysfileMutationFsmStamp,'cucsSysfileMutationFsmStatus':cucsSysfileMutationFsmStatus,'cucsSysfileMutationFsmTry':cucsSysfileMutationFsmTry,'cucsSysfileMutationFsmTaskTable':cucsSysfileMutationFsmTaskTable,'cucsSysfileMutationFsmTaskEntry':cucsSysfileMutationFsmTaskEntry,_F:cucsSysfileMutationFsmTaskInstanceId,'cucsSysfileMutationFsmTaskDn':cucsSysfileMutationFsmTaskDn,'cucsSysfileMutationFsmTaskRn':cucsSysfileMutationFsmTaskRn,'cucsSysfileMutationFsmTaskCompletion':cucsSysfileMutationFsmTaskCompletion,'cucsSysfileMutationFsmTaskFlags':cucsSysfileMutationFsmTaskFlags,'cucsSysfileMutationFsmTaskItem':cucsSysfileMutationFsmTaskItem,'cucsSysfileMutationFsmTaskSeqId':cucsSysfileMutationFsmTaskSeqId,'cucsSysfileDigestTable':cucsSysfileDigestTable,'cucsSysfileDigestEntry':cucsSysfileDigestEntry,_G:cucsSysfileDigestInstanceId,'cucsSysfileDigestDn':cucsSysfileDigestDn,'cucsSysfileDigestRn':cucsSysfileDigestRn,'cucsSysfileDigestCreationTS':cucsSysfileDigestCreationTS,'cucsSysfileDigestDescr':cucsSysfileDigestDescr,'cucsSysfileDigestName':cucsSysfileDigestName,'cucsSysfileDigestSize':cucsSysfileDigestSize,'cucsSysfileDigestSource':cucsSysfileDigestSource,'cucsSysfileDigestSwitchId':cucsSysfileDigestSwitchId,'cucsSysfileDigestTs':cucsSysfileDigestTs,'cucsSysfileDigestUri':cucsSysfileDigestUri,'cucsSysfileDigestChecksum':cucsSysfileDigestChecksum,'cucsSysfileMutationFsmTable':cucsSysfileMutationFsmTable,'cucsSysfileMutationFsmEntry':cucsSysfileMutationFsmEntry,_H:cucsSysfileMutationFsmInstanceId,'cucsSysfileMutationFsmDn':cucsSysfileMutationFsmDn,'cucsSysfileMutationFsmRn':cucsSysfileMutationFsmRn,'cucsSysfileMutationFsmCompletionTime':cucsSysfileMutationFsmCompletionTime,'cucsSysfileMutationFsmCurrentFsm':cucsSysfileMutationFsmCurrentFsm,'cucsSysfileMutationFsmDescrData':cucsSysfileMutationFsmDescrData,'cucsSysfileMutationFsmFsmStatus':cucsSysfileMutationFsmFsmStatus,'cucsSysfileMutationFsmProgress':cucsSysfileMutationFsmProgress,'cucsSysfileMutationFsmRmtErrCode':cucsSysfileMutationFsmRmtErrCode,'cucsSysfileMutationFsmRmtErrDescr':cucsSysfileMutationFsmRmtErrDescr,'cucsSysfileMutationFsmRmtRslt':cucsSysfileMutationFsmRmtRslt,'cucsSysfileMutationFsmStageTable':cucsSysfileMutationFsmStageTable,'cucsSysfileMutationFsmStageEntry':cucsSysfileMutationFsmStageEntry,_I:cucsSysfileMutationFsmStageInstanceId,'cucsSysfileMutationFsmStageDn':cucsSysfileMutationFsmStageDn,'cucsSysfileMutationFsmStageRn':cucsSysfileMutationFsmStageRn,'cucsSysfileMutationFsmStageDescrData':cucsSysfileMutationFsmStageDescrData,'cucsSysfileMutationFsmStageLastUpdateTime':cucsSysfileMutationFsmStageLastUpdateTime,'cucsSysfileMutationFsmStageName':cucsSysfileMutationFsmStageName,'cucsSysfileMutationFsmStageOrder':cucsSysfileMutationFsmStageOrder,'cucsSysfileMutationFsmStageRetry':cucsSysfileMutationFsmStageRetry,'cucsSysfileMutationFsmStageStageStatus':cucsSysfileMutationFsmStageStageStatus})