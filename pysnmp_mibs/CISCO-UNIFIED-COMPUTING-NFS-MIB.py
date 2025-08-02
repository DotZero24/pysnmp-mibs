_M='cucsNfsMountInstFsmTaskInstanceId'
_L='cucsNfsMountInstFsmStageInstanceId'
_K='cucsNfsMountInstFsmInstanceId'
_J='cucsNfsMountInstInstanceId'
_I='cucsNfsMountDefFsmTaskInstanceId'
_H='cucsNfsMountDefFsmStageInstanceId'
_G='cucsNfsMountDefFsmInstanceId'
_F='cucsNfsMountDefInstanceId'
_E='cucsNfsEpInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-NFS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsConditionRemoteInvRslt,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsNfsClientConfigState,CucsNfsDefAdminState,CucsNfsMntAdminState,CucsNfsMntOperState,CucsNfsMountDefFsmCurrentFsm,CucsNfsMountDefFsmStageName,CucsNfsMountDefFsmTaskItem,CucsNfsMountInstFsmCurrentFsm,CucsNfsMountInstFsmStageName,CucsNfsMountInstFsmTaskItem,CucsNfsPurpose,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsConditionRemoteInvRslt','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsNfsClientConfigState','CucsNfsDefAdminState','CucsNfsMntAdminState','CucsNfsMntOperState','CucsNfsMountDefFsmCurrentFsm','CucsNfsMountDefFsmStageName','CucsNfsMountDefFsmTaskItem','CucsNfsMountInstFsmCurrentFsm','CucsNfsMountInstFsmStageName','CucsNfsMountInstFsmTaskItem','CucsNfsPurpose','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsNfsObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,67))
_CucsNfsEpTable_Object=MibTable
cucsNfsEpTable=_CucsNfsEpTable_Object((1,3,6,1,4,1,9,9,719,1,67,1))
if mibBuilder.loadTexts:cucsNfsEpTable.setStatus(_A)
_CucsNfsEpEntry_Object=MibTableRow
cucsNfsEpEntry=_CucsNfsEpEntry_Object((1,3,6,1,4,1,9,9,719,1,67,1,1))
cucsNfsEpEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsNfsEpEntry.setStatus(_A)
_CucsNfsEpInstanceId_Type=CucsManagedObjectId
_CucsNfsEpInstanceId_Object=MibTableColumn
cucsNfsEpInstanceId=_CucsNfsEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,67,1,1,1),_CucsNfsEpInstanceId_Type())
cucsNfsEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsNfsEpInstanceId.setStatus(_A)
_CucsNfsEpDn_Type=CucsManagedObjectDn
_CucsNfsEpDn_Object=MibTableColumn
cucsNfsEpDn=_CucsNfsEpDn_Object((1,3,6,1,4,1,9,9,719,1,67,1,1,2),_CucsNfsEpDn_Type())
cucsNfsEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsEpDn.setStatus(_A)
_CucsNfsEpRn_Type=SnmpAdminString
_CucsNfsEpRn_Object=MibTableColumn
cucsNfsEpRn=_CucsNfsEpRn_Object((1,3,6,1,4,1,9,9,719,1,67,1,1,3),_CucsNfsEpRn_Type())
cucsNfsEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsEpRn.setStatus(_A)
_CucsNfsMountDefTable_Object=MibTable
cucsNfsMountDefTable=_CucsNfsMountDefTable_Object((1,3,6,1,4,1,9,9,719,1,67,2))
if mibBuilder.loadTexts:cucsNfsMountDefTable.setStatus(_A)
_CucsNfsMountDefEntry_Object=MibTableRow
cucsNfsMountDefEntry=_CucsNfsMountDefEntry_Object((1,3,6,1,4,1,9,9,719,1,67,2,1))
cucsNfsMountDefEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsNfsMountDefEntry.setStatus(_A)
_CucsNfsMountDefInstanceId_Type=CucsManagedObjectId
_CucsNfsMountDefInstanceId_Object=MibTableColumn
cucsNfsMountDefInstanceId=_CucsNfsMountDefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,1),_CucsNfsMountDefInstanceId_Type())
cucsNfsMountDefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsNfsMountDefInstanceId.setStatus(_A)
_CucsNfsMountDefDn_Type=CucsManagedObjectDn
_CucsNfsMountDefDn_Object=MibTableColumn
cucsNfsMountDefDn=_CucsNfsMountDefDn_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,2),_CucsNfsMountDefDn_Type())
cucsNfsMountDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefDn.setStatus(_A)
_CucsNfsMountDefRn_Type=SnmpAdminString
_CucsNfsMountDefRn_Object=MibTableColumn
cucsNfsMountDefRn=_CucsNfsMountDefRn_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,3),_CucsNfsMountDefRn_Type())
cucsNfsMountDefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefRn.setStatus(_A)
_CucsNfsMountDefAdminState_Type=CucsNfsDefAdminState
_CucsNfsMountDefAdminState_Object=MibTableColumn
cucsNfsMountDefAdminState=_CucsNfsMountDefAdminState_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,4),_CucsNfsMountDefAdminState_Type())
cucsNfsMountDefAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefAdminState.setStatus(_A)
_CucsNfsMountDefDescr_Type=SnmpAdminString
_CucsNfsMountDefDescr_Object=MibTableColumn
cucsNfsMountDefDescr=_CucsNfsMountDefDescr_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,5),_CucsNfsMountDefDescr_Type())
cucsNfsMountDefDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefDescr.setStatus(_A)
_CucsNfsMountDefFltAggr_Type=Unsigned64
_CucsNfsMountDefFltAggr_Object=MibTableColumn
cucsNfsMountDefFltAggr=_CucsNfsMountDefFltAggr_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,6),_CucsNfsMountDefFltAggr_Type())
cucsNfsMountDefFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFltAggr.setStatus(_A)
_CucsNfsMountDefFsmDescr_Type=SnmpAdminString
_CucsNfsMountDefFsmDescr_Object=MibTableColumn
cucsNfsMountDefFsmDescr=_CucsNfsMountDefFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,7),_CucsNfsMountDefFsmDescr_Type())
cucsNfsMountDefFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmDescr.setStatus(_A)
_CucsNfsMountDefFsmPrev_Type=SnmpAdminString
_CucsNfsMountDefFsmPrev_Object=MibTableColumn
cucsNfsMountDefFsmPrev=_CucsNfsMountDefFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,8),_CucsNfsMountDefFsmPrev_Type())
cucsNfsMountDefFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmPrev.setStatus(_A)
_CucsNfsMountDefFsmProgr_Type=Gauge32
_CucsNfsMountDefFsmProgr_Object=MibTableColumn
cucsNfsMountDefFsmProgr=_CucsNfsMountDefFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,9),_CucsNfsMountDefFsmProgr_Type())
cucsNfsMountDefFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmProgr.setStatus(_A)
_CucsNfsMountDefFsmRmtInvErrCode_Type=Gauge32
_CucsNfsMountDefFsmRmtInvErrCode_Object=MibTableColumn
cucsNfsMountDefFsmRmtInvErrCode=_CucsNfsMountDefFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,10),_CucsNfsMountDefFsmRmtInvErrCode_Type())
cucsNfsMountDefFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmRmtInvErrCode.setStatus(_A)
_CucsNfsMountDefFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsNfsMountDefFsmRmtInvErrDescr_Object=MibTableColumn
cucsNfsMountDefFsmRmtInvErrDescr=_CucsNfsMountDefFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,11),_CucsNfsMountDefFsmRmtInvErrDescr_Type())
cucsNfsMountDefFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmRmtInvErrDescr.setStatus(_A)
_CucsNfsMountDefFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsNfsMountDefFsmRmtInvRslt_Object=MibTableColumn
cucsNfsMountDefFsmRmtInvRslt=_CucsNfsMountDefFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,12),_CucsNfsMountDefFsmRmtInvRslt_Type())
cucsNfsMountDefFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmRmtInvRslt.setStatus(_A)
_CucsNfsMountDefFsmStageDescr_Type=SnmpAdminString
_CucsNfsMountDefFsmStageDescr_Object=MibTableColumn
cucsNfsMountDefFsmStageDescr=_CucsNfsMountDefFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,13),_CucsNfsMountDefFsmStageDescr_Type())
cucsNfsMountDefFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageDescr.setStatus(_A)
_CucsNfsMountDefFsmStamp_Type=DateAndTime
_CucsNfsMountDefFsmStamp_Object=MibTableColumn
cucsNfsMountDefFsmStamp=_CucsNfsMountDefFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,14),_CucsNfsMountDefFsmStamp_Type())
cucsNfsMountDefFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStamp.setStatus(_A)
_CucsNfsMountDefFsmStatus_Type=SnmpAdminString
_CucsNfsMountDefFsmStatus_Object=MibTableColumn
cucsNfsMountDefFsmStatus=_CucsNfsMountDefFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,15),_CucsNfsMountDefFsmStatus_Type())
cucsNfsMountDefFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStatus.setStatus(_A)
_CucsNfsMountDefFsmTry_Type=Gauge32
_CucsNfsMountDefFsmTry_Object=MibTableColumn
cucsNfsMountDefFsmTry=_CucsNfsMountDefFsmTry_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,16),_CucsNfsMountDefFsmTry_Type())
cucsNfsMountDefFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmTry.setStatus(_A)
_CucsNfsMountDefIntId_Type=SnmpAdminString
_CucsNfsMountDefIntId_Object=MibTableColumn
cucsNfsMountDefIntId=_CucsNfsMountDefIntId_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,17),_CucsNfsMountDefIntId_Type())
cucsNfsMountDefIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefIntId.setStatus(_A)
_CucsNfsMountDefLocalDir_Type=SnmpAdminString
_CucsNfsMountDefLocalDir_Object=MibTableColumn
cucsNfsMountDefLocalDir=_CucsNfsMountDefLocalDir_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,18),_CucsNfsMountDefLocalDir_Type())
cucsNfsMountDefLocalDir.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefLocalDir.setStatus(_A)
_CucsNfsMountDefName_Type=SnmpAdminString
_CucsNfsMountDefName_Object=MibTableColumn
cucsNfsMountDefName=_CucsNfsMountDefName_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,19),_CucsNfsMountDefName_Type())
cucsNfsMountDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefName.setStatus(_A)
_CucsNfsMountDefPolicyLevel_Type=Gauge32
_CucsNfsMountDefPolicyLevel_Object=MibTableColumn
cucsNfsMountDefPolicyLevel=_CucsNfsMountDefPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,20),_CucsNfsMountDefPolicyLevel_Type())
cucsNfsMountDefPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefPolicyLevel.setStatus(_A)
_CucsNfsMountDefPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsNfsMountDefPolicyOwner_Object=MibTableColumn
cucsNfsMountDefPolicyOwner=_CucsNfsMountDefPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,21),_CucsNfsMountDefPolicyOwner_Type())
cucsNfsMountDefPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefPolicyOwner.setStatus(_A)
_CucsNfsMountDefPurpose_Type=CucsNfsPurpose
_CucsNfsMountDefPurpose_Object=MibTableColumn
cucsNfsMountDefPurpose=_CucsNfsMountDefPurpose_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,22),_CucsNfsMountDefPurpose_Type())
cucsNfsMountDefPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefPurpose.setStatus(_A)
_CucsNfsMountDefRemoteDir_Type=SnmpAdminString
_CucsNfsMountDefRemoteDir_Object=MibTableColumn
cucsNfsMountDefRemoteDir=_CucsNfsMountDefRemoteDir_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,23),_CucsNfsMountDefRemoteDir_Type())
cucsNfsMountDefRemoteDir.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefRemoteDir.setStatus(_A)
_CucsNfsMountDefServer_Type=SnmpAdminString
_CucsNfsMountDefServer_Object=MibTableColumn
cucsNfsMountDefServer=_CucsNfsMountDefServer_Object((1,3,6,1,4,1,9,9,719,1,67,2,1,24),_CucsNfsMountDefServer_Type())
cucsNfsMountDefServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefServer.setStatus(_A)
_CucsNfsMountDefFsmTable_Object=MibTable
cucsNfsMountDefFsmTable=_CucsNfsMountDefFsmTable_Object((1,3,6,1,4,1,9,9,719,1,67,3))
if mibBuilder.loadTexts:cucsNfsMountDefFsmTable.setStatus(_A)
_CucsNfsMountDefFsmEntry_Object=MibTableRow
cucsNfsMountDefFsmEntry=_CucsNfsMountDefFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,67,3,1))
cucsNfsMountDefFsmEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsNfsMountDefFsmEntry.setStatus(_A)
_CucsNfsMountDefFsmInstanceId_Type=CucsManagedObjectId
_CucsNfsMountDefFsmInstanceId_Object=MibTableColumn
cucsNfsMountDefFsmInstanceId=_CucsNfsMountDefFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,1),_CucsNfsMountDefFsmInstanceId_Type())
cucsNfsMountDefFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsNfsMountDefFsmInstanceId.setStatus(_A)
_CucsNfsMountDefFsmDn_Type=CucsManagedObjectDn
_CucsNfsMountDefFsmDn_Object=MibTableColumn
cucsNfsMountDefFsmDn=_CucsNfsMountDefFsmDn_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,2),_CucsNfsMountDefFsmDn_Type())
cucsNfsMountDefFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmDn.setStatus(_A)
_CucsNfsMountDefFsmRn_Type=SnmpAdminString
_CucsNfsMountDefFsmRn_Object=MibTableColumn
cucsNfsMountDefFsmRn=_CucsNfsMountDefFsmRn_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,3),_CucsNfsMountDefFsmRn_Type())
cucsNfsMountDefFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmRn.setStatus(_A)
_CucsNfsMountDefFsmCompletionTime_Type=DateAndTime
_CucsNfsMountDefFsmCompletionTime_Object=MibTableColumn
cucsNfsMountDefFsmCompletionTime=_CucsNfsMountDefFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,4),_CucsNfsMountDefFsmCompletionTime_Type())
cucsNfsMountDefFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmCompletionTime.setStatus(_A)
_CucsNfsMountDefFsmCurrentFsm_Type=CucsNfsMountDefFsmCurrentFsm
_CucsNfsMountDefFsmCurrentFsm_Object=MibTableColumn
cucsNfsMountDefFsmCurrentFsm=_CucsNfsMountDefFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,5),_CucsNfsMountDefFsmCurrentFsm_Type())
cucsNfsMountDefFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmCurrentFsm.setStatus(_A)
_CucsNfsMountDefFsmDescrData_Type=SnmpAdminString
_CucsNfsMountDefFsmDescrData_Object=MibTableColumn
cucsNfsMountDefFsmDescrData=_CucsNfsMountDefFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,6),_CucsNfsMountDefFsmDescrData_Type())
cucsNfsMountDefFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmDescrData.setStatus(_A)
_CucsNfsMountDefFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsNfsMountDefFsmFsmStatus_Object=MibTableColumn
cucsNfsMountDefFsmFsmStatus=_CucsNfsMountDefFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,7),_CucsNfsMountDefFsmFsmStatus_Type())
cucsNfsMountDefFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmFsmStatus.setStatus(_A)
_CucsNfsMountDefFsmProgress_Type=Gauge32
_CucsNfsMountDefFsmProgress_Object=MibTableColumn
cucsNfsMountDefFsmProgress=_CucsNfsMountDefFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,8),_CucsNfsMountDefFsmProgress_Type())
cucsNfsMountDefFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmProgress.setStatus(_A)
_CucsNfsMountDefFsmRmtErrCode_Type=Gauge32
_CucsNfsMountDefFsmRmtErrCode_Object=MibTableColumn
cucsNfsMountDefFsmRmtErrCode=_CucsNfsMountDefFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,9),_CucsNfsMountDefFsmRmtErrCode_Type())
cucsNfsMountDefFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmRmtErrCode.setStatus(_A)
_CucsNfsMountDefFsmRmtErrDescr_Type=SnmpAdminString
_CucsNfsMountDefFsmRmtErrDescr_Object=MibTableColumn
cucsNfsMountDefFsmRmtErrDescr=_CucsNfsMountDefFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,10),_CucsNfsMountDefFsmRmtErrDescr_Type())
cucsNfsMountDefFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmRmtErrDescr.setStatus(_A)
_CucsNfsMountDefFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsNfsMountDefFsmRmtRslt_Object=MibTableColumn
cucsNfsMountDefFsmRmtRslt=_CucsNfsMountDefFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,67,3,1,11),_CucsNfsMountDefFsmRmtRslt_Type())
cucsNfsMountDefFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmRmtRslt.setStatus(_A)
_CucsNfsMountDefFsmStageTable_Object=MibTable
cucsNfsMountDefFsmStageTable=_CucsNfsMountDefFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,67,4))
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageTable.setStatus(_A)
_CucsNfsMountDefFsmStageEntry_Object=MibTableRow
cucsNfsMountDefFsmStageEntry=_CucsNfsMountDefFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,67,4,1))
cucsNfsMountDefFsmStageEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageEntry.setStatus(_A)
_CucsNfsMountDefFsmStageInstanceId_Type=CucsManagedObjectId
_CucsNfsMountDefFsmStageInstanceId_Object=MibTableColumn
cucsNfsMountDefFsmStageInstanceId=_CucsNfsMountDefFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,67,4,1,1),_CucsNfsMountDefFsmStageInstanceId_Type())
cucsNfsMountDefFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageInstanceId.setStatus(_A)
_CucsNfsMountDefFsmStageDn_Type=CucsManagedObjectDn
_CucsNfsMountDefFsmStageDn_Object=MibTableColumn
cucsNfsMountDefFsmStageDn=_CucsNfsMountDefFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,67,4,1,2),_CucsNfsMountDefFsmStageDn_Type())
cucsNfsMountDefFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageDn.setStatus(_A)
_CucsNfsMountDefFsmStageRn_Type=SnmpAdminString
_CucsNfsMountDefFsmStageRn_Object=MibTableColumn
cucsNfsMountDefFsmStageRn=_CucsNfsMountDefFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,67,4,1,3),_CucsNfsMountDefFsmStageRn_Type())
cucsNfsMountDefFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageRn.setStatus(_A)
_CucsNfsMountDefFsmStageDescrData_Type=SnmpAdminString
_CucsNfsMountDefFsmStageDescrData_Object=MibTableColumn
cucsNfsMountDefFsmStageDescrData=_CucsNfsMountDefFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,67,4,1,4),_CucsNfsMountDefFsmStageDescrData_Type())
cucsNfsMountDefFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageDescrData.setStatus(_A)
_CucsNfsMountDefFsmStageLastUpdateTime_Type=DateAndTime
_CucsNfsMountDefFsmStageLastUpdateTime_Object=MibTableColumn
cucsNfsMountDefFsmStageLastUpdateTime=_CucsNfsMountDefFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,67,4,1,5),_CucsNfsMountDefFsmStageLastUpdateTime_Type())
cucsNfsMountDefFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageLastUpdateTime.setStatus(_A)
_CucsNfsMountDefFsmStageName_Type=CucsNfsMountDefFsmStageName
_CucsNfsMountDefFsmStageName_Object=MibTableColumn
cucsNfsMountDefFsmStageName=_CucsNfsMountDefFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,67,4,1,6),_CucsNfsMountDefFsmStageName_Type())
cucsNfsMountDefFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageName.setStatus(_A)
_CucsNfsMountDefFsmStageOrder_Type=Gauge32
_CucsNfsMountDefFsmStageOrder_Object=MibTableColumn
cucsNfsMountDefFsmStageOrder=_CucsNfsMountDefFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,67,4,1,7),_CucsNfsMountDefFsmStageOrder_Type())
cucsNfsMountDefFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageOrder.setStatus(_A)
_CucsNfsMountDefFsmStageRetry_Type=Gauge32
_CucsNfsMountDefFsmStageRetry_Object=MibTableColumn
cucsNfsMountDefFsmStageRetry=_CucsNfsMountDefFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,67,4,1,8),_CucsNfsMountDefFsmStageRetry_Type())
cucsNfsMountDefFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageRetry.setStatus(_A)
_CucsNfsMountDefFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsNfsMountDefFsmStageStageStatus_Object=MibTableColumn
cucsNfsMountDefFsmStageStageStatus=_CucsNfsMountDefFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,67,4,1,9),_CucsNfsMountDefFsmStageStageStatus_Type())
cucsNfsMountDefFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmStageStageStatus.setStatus(_A)
_CucsNfsMountDefFsmTaskTable_Object=MibTable
cucsNfsMountDefFsmTaskTable=_CucsNfsMountDefFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,67,5))
if mibBuilder.loadTexts:cucsNfsMountDefFsmTaskTable.setStatus(_A)
_CucsNfsMountDefFsmTaskEntry_Object=MibTableRow
cucsNfsMountDefFsmTaskEntry=_CucsNfsMountDefFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,67,5,1))
cucsNfsMountDefFsmTaskEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsNfsMountDefFsmTaskEntry.setStatus(_A)
_CucsNfsMountDefFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsNfsMountDefFsmTaskInstanceId_Object=MibTableColumn
cucsNfsMountDefFsmTaskInstanceId=_CucsNfsMountDefFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,67,5,1,1),_CucsNfsMountDefFsmTaskInstanceId_Type())
cucsNfsMountDefFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsNfsMountDefFsmTaskInstanceId.setStatus(_A)
_CucsNfsMountDefFsmTaskDn_Type=CucsManagedObjectDn
_CucsNfsMountDefFsmTaskDn_Object=MibTableColumn
cucsNfsMountDefFsmTaskDn=_CucsNfsMountDefFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,67,5,1,2),_CucsNfsMountDefFsmTaskDn_Type())
cucsNfsMountDefFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmTaskDn.setStatus(_A)
_CucsNfsMountDefFsmTaskRn_Type=SnmpAdminString
_CucsNfsMountDefFsmTaskRn_Object=MibTableColumn
cucsNfsMountDefFsmTaskRn=_CucsNfsMountDefFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,67,5,1,3),_CucsNfsMountDefFsmTaskRn_Type())
cucsNfsMountDefFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmTaskRn.setStatus(_A)
_CucsNfsMountDefFsmTaskCompletion_Type=CucsFsmCompletion
_CucsNfsMountDefFsmTaskCompletion_Object=MibTableColumn
cucsNfsMountDefFsmTaskCompletion=_CucsNfsMountDefFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,67,5,1,4),_CucsNfsMountDefFsmTaskCompletion_Type())
cucsNfsMountDefFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmTaskCompletion.setStatus(_A)
_CucsNfsMountDefFsmTaskFlags_Type=CucsFsmFlags
_CucsNfsMountDefFsmTaskFlags_Object=MibTableColumn
cucsNfsMountDefFsmTaskFlags=_CucsNfsMountDefFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,67,5,1,5),_CucsNfsMountDefFsmTaskFlags_Type())
cucsNfsMountDefFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmTaskFlags.setStatus(_A)
_CucsNfsMountDefFsmTaskItem_Type=CucsNfsMountDefFsmTaskItem
_CucsNfsMountDefFsmTaskItem_Object=MibTableColumn
cucsNfsMountDefFsmTaskItem=_CucsNfsMountDefFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,67,5,1,6),_CucsNfsMountDefFsmTaskItem_Type())
cucsNfsMountDefFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmTaskItem.setStatus(_A)
_CucsNfsMountDefFsmTaskSeqId_Type=Gauge32
_CucsNfsMountDefFsmTaskSeqId_Object=MibTableColumn
cucsNfsMountDefFsmTaskSeqId=_CucsNfsMountDefFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,67,5,1,7),_CucsNfsMountDefFsmTaskSeqId_Type())
cucsNfsMountDefFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountDefFsmTaskSeqId.setStatus(_A)
_CucsNfsMountInstTable_Object=MibTable
cucsNfsMountInstTable=_CucsNfsMountInstTable_Object((1,3,6,1,4,1,9,9,719,1,67,6))
if mibBuilder.loadTexts:cucsNfsMountInstTable.setStatus(_A)
_CucsNfsMountInstEntry_Object=MibTableRow
cucsNfsMountInstEntry=_CucsNfsMountInstEntry_Object((1,3,6,1,4,1,9,9,719,1,67,6,1))
cucsNfsMountInstEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsNfsMountInstEntry.setStatus(_A)
_CucsNfsMountInstInstanceId_Type=CucsManagedObjectId
_CucsNfsMountInstInstanceId_Object=MibTableColumn
cucsNfsMountInstInstanceId=_CucsNfsMountInstInstanceId_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,1),_CucsNfsMountInstInstanceId_Type())
cucsNfsMountInstInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsNfsMountInstInstanceId.setStatus(_A)
_CucsNfsMountInstDn_Type=CucsManagedObjectDn
_CucsNfsMountInstDn_Object=MibTableColumn
cucsNfsMountInstDn=_CucsNfsMountInstDn_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,2),_CucsNfsMountInstDn_Type())
cucsNfsMountInstDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstDn.setStatus(_A)
_CucsNfsMountInstRn_Type=SnmpAdminString
_CucsNfsMountInstRn_Object=MibTableColumn
cucsNfsMountInstRn=_CucsNfsMountInstRn_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,3),_CucsNfsMountInstRn_Type())
cucsNfsMountInstRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstRn.setStatus(_A)
_CucsNfsMountInstAdminState_Type=CucsNfsMntAdminState
_CucsNfsMountInstAdminState_Object=MibTableColumn
cucsNfsMountInstAdminState=_CucsNfsMountInstAdminState_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,4),_CucsNfsMountInstAdminState_Type())
cucsNfsMountInstAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstAdminState.setStatus(_A)
_CucsNfsMountInstClientConfigState_Type=CucsNfsClientConfigState
_CucsNfsMountInstClientConfigState_Object=MibTableColumn
cucsNfsMountInstClientConfigState=_CucsNfsMountInstClientConfigState_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,5),_CucsNfsMountInstClientConfigState_Type())
cucsNfsMountInstClientConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstClientConfigState.setStatus(_A)
_CucsNfsMountInstDefDn_Type=SnmpAdminString
_CucsNfsMountInstDefDn_Object=MibTableColumn
cucsNfsMountInstDefDn=_CucsNfsMountInstDefDn_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,6),_CucsNfsMountInstDefDn_Type())
cucsNfsMountInstDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstDefDn.setStatus(_A)
_CucsNfsMountInstFsmDescr_Type=SnmpAdminString
_CucsNfsMountInstFsmDescr_Object=MibTableColumn
cucsNfsMountInstFsmDescr=_CucsNfsMountInstFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,7),_CucsNfsMountInstFsmDescr_Type())
cucsNfsMountInstFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmDescr.setStatus(_A)
_CucsNfsMountInstFsmPrev_Type=SnmpAdminString
_CucsNfsMountInstFsmPrev_Object=MibTableColumn
cucsNfsMountInstFsmPrev=_CucsNfsMountInstFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,8),_CucsNfsMountInstFsmPrev_Type())
cucsNfsMountInstFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmPrev.setStatus(_A)
_CucsNfsMountInstFsmProgr_Type=Gauge32
_CucsNfsMountInstFsmProgr_Object=MibTableColumn
cucsNfsMountInstFsmProgr=_CucsNfsMountInstFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,9),_CucsNfsMountInstFsmProgr_Type())
cucsNfsMountInstFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmProgr.setStatus(_A)
_CucsNfsMountInstFsmRmtInvErrCode_Type=Gauge32
_CucsNfsMountInstFsmRmtInvErrCode_Object=MibTableColumn
cucsNfsMountInstFsmRmtInvErrCode=_CucsNfsMountInstFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,10),_CucsNfsMountInstFsmRmtInvErrCode_Type())
cucsNfsMountInstFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmRmtInvErrCode.setStatus(_A)
_CucsNfsMountInstFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsNfsMountInstFsmRmtInvErrDescr_Object=MibTableColumn
cucsNfsMountInstFsmRmtInvErrDescr=_CucsNfsMountInstFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,11),_CucsNfsMountInstFsmRmtInvErrDescr_Type())
cucsNfsMountInstFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmRmtInvErrDescr.setStatus(_A)
_CucsNfsMountInstFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsNfsMountInstFsmRmtInvRslt_Object=MibTableColumn
cucsNfsMountInstFsmRmtInvRslt=_CucsNfsMountInstFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,12),_CucsNfsMountInstFsmRmtInvRslt_Type())
cucsNfsMountInstFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmRmtInvRslt.setStatus(_A)
_CucsNfsMountInstFsmStageDescr_Type=SnmpAdminString
_CucsNfsMountInstFsmStageDescr_Object=MibTableColumn
cucsNfsMountInstFsmStageDescr=_CucsNfsMountInstFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,13),_CucsNfsMountInstFsmStageDescr_Type())
cucsNfsMountInstFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageDescr.setStatus(_A)
_CucsNfsMountInstFsmStamp_Type=DateAndTime
_CucsNfsMountInstFsmStamp_Object=MibTableColumn
cucsNfsMountInstFsmStamp=_CucsNfsMountInstFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,14),_CucsNfsMountInstFsmStamp_Type())
cucsNfsMountInstFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStamp.setStatus(_A)
_CucsNfsMountInstFsmStatus_Type=SnmpAdminString
_CucsNfsMountInstFsmStatus_Object=MibTableColumn
cucsNfsMountInstFsmStatus=_CucsNfsMountInstFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,15),_CucsNfsMountInstFsmStatus_Type())
cucsNfsMountInstFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStatus.setStatus(_A)
_CucsNfsMountInstFsmTry_Type=Gauge32
_CucsNfsMountInstFsmTry_Object=MibTableColumn
cucsNfsMountInstFsmTry=_CucsNfsMountInstFsmTry_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,16),_CucsNfsMountInstFsmTry_Type())
cucsNfsMountInstFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmTry.setStatus(_A)
_CucsNfsMountInstLocalDir_Type=SnmpAdminString
_CucsNfsMountInstLocalDir_Object=MibTableColumn
cucsNfsMountInstLocalDir=_CucsNfsMountInstLocalDir_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,17),_CucsNfsMountInstLocalDir_Type())
cucsNfsMountInstLocalDir.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstLocalDir.setStatus(_A)
_CucsNfsMountInstName_Type=SnmpAdminString
_CucsNfsMountInstName_Object=MibTableColumn
cucsNfsMountInstName=_CucsNfsMountInstName_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,18),_CucsNfsMountInstName_Type())
cucsNfsMountInstName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstName.setStatus(_A)
_CucsNfsMountInstOperState_Type=CucsNfsMntOperState
_CucsNfsMountInstOperState_Object=MibTableColumn
cucsNfsMountInstOperState=_CucsNfsMountInstOperState_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,19),_CucsNfsMountInstOperState_Type())
cucsNfsMountInstOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstOperState.setStatus(_A)
_CucsNfsMountInstPurpose_Type=CucsNfsPurpose
_CucsNfsMountInstPurpose_Object=MibTableColumn
cucsNfsMountInstPurpose=_CucsNfsMountInstPurpose_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,20),_CucsNfsMountInstPurpose_Type())
cucsNfsMountInstPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstPurpose.setStatus(_A)
_CucsNfsMountInstRemoteDir_Type=SnmpAdminString
_CucsNfsMountInstRemoteDir_Object=MibTableColumn
cucsNfsMountInstRemoteDir=_CucsNfsMountInstRemoteDir_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,21),_CucsNfsMountInstRemoteDir_Type())
cucsNfsMountInstRemoteDir.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstRemoteDir.setStatus(_A)
_CucsNfsMountInstServer_Type=SnmpAdminString
_CucsNfsMountInstServer_Object=MibTableColumn
cucsNfsMountInstServer=_CucsNfsMountInstServer_Object((1,3,6,1,4,1,9,9,719,1,67,6,1,22),_CucsNfsMountInstServer_Type())
cucsNfsMountInstServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstServer.setStatus(_A)
_CucsNfsMountInstFsmTable_Object=MibTable
cucsNfsMountInstFsmTable=_CucsNfsMountInstFsmTable_Object((1,3,6,1,4,1,9,9,719,1,67,7))
if mibBuilder.loadTexts:cucsNfsMountInstFsmTable.setStatus(_A)
_CucsNfsMountInstFsmEntry_Object=MibTableRow
cucsNfsMountInstFsmEntry=_CucsNfsMountInstFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,67,7,1))
cucsNfsMountInstFsmEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsNfsMountInstFsmEntry.setStatus(_A)
_CucsNfsMountInstFsmInstanceId_Type=CucsManagedObjectId
_CucsNfsMountInstFsmInstanceId_Object=MibTableColumn
cucsNfsMountInstFsmInstanceId=_CucsNfsMountInstFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,1),_CucsNfsMountInstFsmInstanceId_Type())
cucsNfsMountInstFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsNfsMountInstFsmInstanceId.setStatus(_A)
_CucsNfsMountInstFsmDn_Type=CucsManagedObjectDn
_CucsNfsMountInstFsmDn_Object=MibTableColumn
cucsNfsMountInstFsmDn=_CucsNfsMountInstFsmDn_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,2),_CucsNfsMountInstFsmDn_Type())
cucsNfsMountInstFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmDn.setStatus(_A)
_CucsNfsMountInstFsmRn_Type=SnmpAdminString
_CucsNfsMountInstFsmRn_Object=MibTableColumn
cucsNfsMountInstFsmRn=_CucsNfsMountInstFsmRn_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,3),_CucsNfsMountInstFsmRn_Type())
cucsNfsMountInstFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmRn.setStatus(_A)
_CucsNfsMountInstFsmCompletionTime_Type=DateAndTime
_CucsNfsMountInstFsmCompletionTime_Object=MibTableColumn
cucsNfsMountInstFsmCompletionTime=_CucsNfsMountInstFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,4),_CucsNfsMountInstFsmCompletionTime_Type())
cucsNfsMountInstFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmCompletionTime.setStatus(_A)
_CucsNfsMountInstFsmCurrentFsm_Type=CucsNfsMountInstFsmCurrentFsm
_CucsNfsMountInstFsmCurrentFsm_Object=MibTableColumn
cucsNfsMountInstFsmCurrentFsm=_CucsNfsMountInstFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,5),_CucsNfsMountInstFsmCurrentFsm_Type())
cucsNfsMountInstFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmCurrentFsm.setStatus(_A)
_CucsNfsMountInstFsmDescrData_Type=SnmpAdminString
_CucsNfsMountInstFsmDescrData_Object=MibTableColumn
cucsNfsMountInstFsmDescrData=_CucsNfsMountInstFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,6),_CucsNfsMountInstFsmDescrData_Type())
cucsNfsMountInstFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmDescrData.setStatus(_A)
_CucsNfsMountInstFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsNfsMountInstFsmFsmStatus_Object=MibTableColumn
cucsNfsMountInstFsmFsmStatus=_CucsNfsMountInstFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,7),_CucsNfsMountInstFsmFsmStatus_Type())
cucsNfsMountInstFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmFsmStatus.setStatus(_A)
_CucsNfsMountInstFsmProgress_Type=Gauge32
_CucsNfsMountInstFsmProgress_Object=MibTableColumn
cucsNfsMountInstFsmProgress=_CucsNfsMountInstFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,8),_CucsNfsMountInstFsmProgress_Type())
cucsNfsMountInstFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmProgress.setStatus(_A)
_CucsNfsMountInstFsmRmtErrCode_Type=Gauge32
_CucsNfsMountInstFsmRmtErrCode_Object=MibTableColumn
cucsNfsMountInstFsmRmtErrCode=_CucsNfsMountInstFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,9),_CucsNfsMountInstFsmRmtErrCode_Type())
cucsNfsMountInstFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmRmtErrCode.setStatus(_A)
_CucsNfsMountInstFsmRmtErrDescr_Type=SnmpAdminString
_CucsNfsMountInstFsmRmtErrDescr_Object=MibTableColumn
cucsNfsMountInstFsmRmtErrDescr=_CucsNfsMountInstFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,10),_CucsNfsMountInstFsmRmtErrDescr_Type())
cucsNfsMountInstFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmRmtErrDescr.setStatus(_A)
_CucsNfsMountInstFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsNfsMountInstFsmRmtRslt_Object=MibTableColumn
cucsNfsMountInstFsmRmtRslt=_CucsNfsMountInstFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,67,7,1,11),_CucsNfsMountInstFsmRmtRslt_Type())
cucsNfsMountInstFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmRmtRslt.setStatus(_A)
_CucsNfsMountInstFsmStageTable_Object=MibTable
cucsNfsMountInstFsmStageTable=_CucsNfsMountInstFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,67,8))
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageTable.setStatus(_A)
_CucsNfsMountInstFsmStageEntry_Object=MibTableRow
cucsNfsMountInstFsmStageEntry=_CucsNfsMountInstFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,67,8,1))
cucsNfsMountInstFsmStageEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageEntry.setStatus(_A)
_CucsNfsMountInstFsmStageInstanceId_Type=CucsManagedObjectId
_CucsNfsMountInstFsmStageInstanceId_Object=MibTableColumn
cucsNfsMountInstFsmStageInstanceId=_CucsNfsMountInstFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,67,8,1,1),_CucsNfsMountInstFsmStageInstanceId_Type())
cucsNfsMountInstFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageInstanceId.setStatus(_A)
_CucsNfsMountInstFsmStageDn_Type=CucsManagedObjectDn
_CucsNfsMountInstFsmStageDn_Object=MibTableColumn
cucsNfsMountInstFsmStageDn=_CucsNfsMountInstFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,67,8,1,2),_CucsNfsMountInstFsmStageDn_Type())
cucsNfsMountInstFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageDn.setStatus(_A)
_CucsNfsMountInstFsmStageRn_Type=SnmpAdminString
_CucsNfsMountInstFsmStageRn_Object=MibTableColumn
cucsNfsMountInstFsmStageRn=_CucsNfsMountInstFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,67,8,1,3),_CucsNfsMountInstFsmStageRn_Type())
cucsNfsMountInstFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageRn.setStatus(_A)
_CucsNfsMountInstFsmStageDescrData_Type=SnmpAdminString
_CucsNfsMountInstFsmStageDescrData_Object=MibTableColumn
cucsNfsMountInstFsmStageDescrData=_CucsNfsMountInstFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,67,8,1,4),_CucsNfsMountInstFsmStageDescrData_Type())
cucsNfsMountInstFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageDescrData.setStatus(_A)
_CucsNfsMountInstFsmStageLastUpdateTime_Type=DateAndTime
_CucsNfsMountInstFsmStageLastUpdateTime_Object=MibTableColumn
cucsNfsMountInstFsmStageLastUpdateTime=_CucsNfsMountInstFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,67,8,1,5),_CucsNfsMountInstFsmStageLastUpdateTime_Type())
cucsNfsMountInstFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageLastUpdateTime.setStatus(_A)
_CucsNfsMountInstFsmStageName_Type=CucsNfsMountInstFsmStageName
_CucsNfsMountInstFsmStageName_Object=MibTableColumn
cucsNfsMountInstFsmStageName=_CucsNfsMountInstFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,67,8,1,6),_CucsNfsMountInstFsmStageName_Type())
cucsNfsMountInstFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageName.setStatus(_A)
_CucsNfsMountInstFsmStageOrder_Type=Gauge32
_CucsNfsMountInstFsmStageOrder_Object=MibTableColumn
cucsNfsMountInstFsmStageOrder=_CucsNfsMountInstFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,67,8,1,7),_CucsNfsMountInstFsmStageOrder_Type())
cucsNfsMountInstFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageOrder.setStatus(_A)
_CucsNfsMountInstFsmStageRetry_Type=Gauge32
_CucsNfsMountInstFsmStageRetry_Object=MibTableColumn
cucsNfsMountInstFsmStageRetry=_CucsNfsMountInstFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,67,8,1,8),_CucsNfsMountInstFsmStageRetry_Type())
cucsNfsMountInstFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageRetry.setStatus(_A)
_CucsNfsMountInstFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsNfsMountInstFsmStageStageStatus_Object=MibTableColumn
cucsNfsMountInstFsmStageStageStatus=_CucsNfsMountInstFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,67,8,1,9),_CucsNfsMountInstFsmStageStageStatus_Type())
cucsNfsMountInstFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmStageStageStatus.setStatus(_A)
_CucsNfsMountInstFsmTaskTable_Object=MibTable
cucsNfsMountInstFsmTaskTable=_CucsNfsMountInstFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,67,9))
if mibBuilder.loadTexts:cucsNfsMountInstFsmTaskTable.setStatus(_A)
_CucsNfsMountInstFsmTaskEntry_Object=MibTableRow
cucsNfsMountInstFsmTaskEntry=_CucsNfsMountInstFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,67,9,1))
cucsNfsMountInstFsmTaskEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsNfsMountInstFsmTaskEntry.setStatus(_A)
_CucsNfsMountInstFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsNfsMountInstFsmTaskInstanceId_Object=MibTableColumn
cucsNfsMountInstFsmTaskInstanceId=_CucsNfsMountInstFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,67,9,1,1),_CucsNfsMountInstFsmTaskInstanceId_Type())
cucsNfsMountInstFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsNfsMountInstFsmTaskInstanceId.setStatus(_A)
_CucsNfsMountInstFsmTaskDn_Type=CucsManagedObjectDn
_CucsNfsMountInstFsmTaskDn_Object=MibTableColumn
cucsNfsMountInstFsmTaskDn=_CucsNfsMountInstFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,67,9,1,2),_CucsNfsMountInstFsmTaskDn_Type())
cucsNfsMountInstFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmTaskDn.setStatus(_A)
_CucsNfsMountInstFsmTaskRn_Type=SnmpAdminString
_CucsNfsMountInstFsmTaskRn_Object=MibTableColumn
cucsNfsMountInstFsmTaskRn=_CucsNfsMountInstFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,67,9,1,3),_CucsNfsMountInstFsmTaskRn_Type())
cucsNfsMountInstFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmTaskRn.setStatus(_A)
_CucsNfsMountInstFsmTaskCompletion_Type=CucsFsmCompletion
_CucsNfsMountInstFsmTaskCompletion_Object=MibTableColumn
cucsNfsMountInstFsmTaskCompletion=_CucsNfsMountInstFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,67,9,1,4),_CucsNfsMountInstFsmTaskCompletion_Type())
cucsNfsMountInstFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmTaskCompletion.setStatus(_A)
_CucsNfsMountInstFsmTaskFlags_Type=CucsFsmFlags
_CucsNfsMountInstFsmTaskFlags_Object=MibTableColumn
cucsNfsMountInstFsmTaskFlags=_CucsNfsMountInstFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,67,9,1,5),_CucsNfsMountInstFsmTaskFlags_Type())
cucsNfsMountInstFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmTaskFlags.setStatus(_A)
_CucsNfsMountInstFsmTaskItem_Type=CucsNfsMountInstFsmTaskItem
_CucsNfsMountInstFsmTaskItem_Object=MibTableColumn
cucsNfsMountInstFsmTaskItem=_CucsNfsMountInstFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,67,9,1,6),_CucsNfsMountInstFsmTaskItem_Type())
cucsNfsMountInstFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmTaskItem.setStatus(_A)
_CucsNfsMountInstFsmTaskSeqId_Type=Gauge32
_CucsNfsMountInstFsmTaskSeqId_Object=MibTableColumn
cucsNfsMountInstFsmTaskSeqId=_CucsNfsMountInstFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,67,9,1,7),_CucsNfsMountInstFsmTaskSeqId_Type())
cucsNfsMountInstFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsNfsMountInstFsmTaskSeqId.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsNfsObjects':cucsNfsObjects,'cucsNfsEpTable':cucsNfsEpTable,'cucsNfsEpEntry':cucsNfsEpEntry,_E:cucsNfsEpInstanceId,'cucsNfsEpDn':cucsNfsEpDn,'cucsNfsEpRn':cucsNfsEpRn,'cucsNfsMountDefTable':cucsNfsMountDefTable,'cucsNfsMountDefEntry':cucsNfsMountDefEntry,_F:cucsNfsMountDefInstanceId,'cucsNfsMountDefDn':cucsNfsMountDefDn,'cucsNfsMountDefRn':cucsNfsMountDefRn,'cucsNfsMountDefAdminState':cucsNfsMountDefAdminState,'cucsNfsMountDefDescr':cucsNfsMountDefDescr,'cucsNfsMountDefFltAggr':cucsNfsMountDefFltAggr,'cucsNfsMountDefFsmDescr':cucsNfsMountDefFsmDescr,'cucsNfsMountDefFsmPrev':cucsNfsMountDefFsmPrev,'cucsNfsMountDefFsmProgr':cucsNfsMountDefFsmProgr,'cucsNfsMountDefFsmRmtInvErrCode':cucsNfsMountDefFsmRmtInvErrCode,'cucsNfsMountDefFsmRmtInvErrDescr':cucsNfsMountDefFsmRmtInvErrDescr,'cucsNfsMountDefFsmRmtInvRslt':cucsNfsMountDefFsmRmtInvRslt,'cucsNfsMountDefFsmStageDescr':cucsNfsMountDefFsmStageDescr,'cucsNfsMountDefFsmStamp':cucsNfsMountDefFsmStamp,'cucsNfsMountDefFsmStatus':cucsNfsMountDefFsmStatus,'cucsNfsMountDefFsmTry':cucsNfsMountDefFsmTry,'cucsNfsMountDefIntId':cucsNfsMountDefIntId,'cucsNfsMountDefLocalDir':cucsNfsMountDefLocalDir,'cucsNfsMountDefName':cucsNfsMountDefName,'cucsNfsMountDefPolicyLevel':cucsNfsMountDefPolicyLevel,'cucsNfsMountDefPolicyOwner':cucsNfsMountDefPolicyOwner,'cucsNfsMountDefPurpose':cucsNfsMountDefPurpose,'cucsNfsMountDefRemoteDir':cucsNfsMountDefRemoteDir,'cucsNfsMountDefServer':cucsNfsMountDefServer,'cucsNfsMountDefFsmTable':cucsNfsMountDefFsmTable,'cucsNfsMountDefFsmEntry':cucsNfsMountDefFsmEntry,_G:cucsNfsMountDefFsmInstanceId,'cucsNfsMountDefFsmDn':cucsNfsMountDefFsmDn,'cucsNfsMountDefFsmRn':cucsNfsMountDefFsmRn,'cucsNfsMountDefFsmCompletionTime':cucsNfsMountDefFsmCompletionTime,'cucsNfsMountDefFsmCurrentFsm':cucsNfsMountDefFsmCurrentFsm,'cucsNfsMountDefFsmDescrData':cucsNfsMountDefFsmDescrData,'cucsNfsMountDefFsmFsmStatus':cucsNfsMountDefFsmFsmStatus,'cucsNfsMountDefFsmProgress':cucsNfsMountDefFsmProgress,'cucsNfsMountDefFsmRmtErrCode':cucsNfsMountDefFsmRmtErrCode,'cucsNfsMountDefFsmRmtErrDescr':cucsNfsMountDefFsmRmtErrDescr,'cucsNfsMountDefFsmRmtRslt':cucsNfsMountDefFsmRmtRslt,'cucsNfsMountDefFsmStageTable':cucsNfsMountDefFsmStageTable,'cucsNfsMountDefFsmStageEntry':cucsNfsMountDefFsmStageEntry,_H:cucsNfsMountDefFsmStageInstanceId,'cucsNfsMountDefFsmStageDn':cucsNfsMountDefFsmStageDn,'cucsNfsMountDefFsmStageRn':cucsNfsMountDefFsmStageRn,'cucsNfsMountDefFsmStageDescrData':cucsNfsMountDefFsmStageDescrData,'cucsNfsMountDefFsmStageLastUpdateTime':cucsNfsMountDefFsmStageLastUpdateTime,'cucsNfsMountDefFsmStageName':cucsNfsMountDefFsmStageName,'cucsNfsMountDefFsmStageOrder':cucsNfsMountDefFsmStageOrder,'cucsNfsMountDefFsmStageRetry':cucsNfsMountDefFsmStageRetry,'cucsNfsMountDefFsmStageStageStatus':cucsNfsMountDefFsmStageStageStatus,'cucsNfsMountDefFsmTaskTable':cucsNfsMountDefFsmTaskTable,'cucsNfsMountDefFsmTaskEntry':cucsNfsMountDefFsmTaskEntry,_I:cucsNfsMountDefFsmTaskInstanceId,'cucsNfsMountDefFsmTaskDn':cucsNfsMountDefFsmTaskDn,'cucsNfsMountDefFsmTaskRn':cucsNfsMountDefFsmTaskRn,'cucsNfsMountDefFsmTaskCompletion':cucsNfsMountDefFsmTaskCompletion,'cucsNfsMountDefFsmTaskFlags':cucsNfsMountDefFsmTaskFlags,'cucsNfsMountDefFsmTaskItem':cucsNfsMountDefFsmTaskItem,'cucsNfsMountDefFsmTaskSeqId':cucsNfsMountDefFsmTaskSeqId,'cucsNfsMountInstTable':cucsNfsMountInstTable,'cucsNfsMountInstEntry':cucsNfsMountInstEntry,_J:cucsNfsMountInstInstanceId,'cucsNfsMountInstDn':cucsNfsMountInstDn,'cucsNfsMountInstRn':cucsNfsMountInstRn,'cucsNfsMountInstAdminState':cucsNfsMountInstAdminState,'cucsNfsMountInstClientConfigState':cucsNfsMountInstClientConfigState,'cucsNfsMountInstDefDn':cucsNfsMountInstDefDn,'cucsNfsMountInstFsmDescr':cucsNfsMountInstFsmDescr,'cucsNfsMountInstFsmPrev':cucsNfsMountInstFsmPrev,'cucsNfsMountInstFsmProgr':cucsNfsMountInstFsmProgr,'cucsNfsMountInstFsmRmtInvErrCode':cucsNfsMountInstFsmRmtInvErrCode,'cucsNfsMountInstFsmRmtInvErrDescr':cucsNfsMountInstFsmRmtInvErrDescr,'cucsNfsMountInstFsmRmtInvRslt':cucsNfsMountInstFsmRmtInvRslt,'cucsNfsMountInstFsmStageDescr':cucsNfsMountInstFsmStageDescr,'cucsNfsMountInstFsmStamp':cucsNfsMountInstFsmStamp,'cucsNfsMountInstFsmStatus':cucsNfsMountInstFsmStatus,'cucsNfsMountInstFsmTry':cucsNfsMountInstFsmTry,'cucsNfsMountInstLocalDir':cucsNfsMountInstLocalDir,'cucsNfsMountInstName':cucsNfsMountInstName,'cucsNfsMountInstOperState':cucsNfsMountInstOperState,'cucsNfsMountInstPurpose':cucsNfsMountInstPurpose,'cucsNfsMountInstRemoteDir':cucsNfsMountInstRemoteDir,'cucsNfsMountInstServer':cucsNfsMountInstServer,'cucsNfsMountInstFsmTable':cucsNfsMountInstFsmTable,'cucsNfsMountInstFsmEntry':cucsNfsMountInstFsmEntry,_K:cucsNfsMountInstFsmInstanceId,'cucsNfsMountInstFsmDn':cucsNfsMountInstFsmDn,'cucsNfsMountInstFsmRn':cucsNfsMountInstFsmRn,'cucsNfsMountInstFsmCompletionTime':cucsNfsMountInstFsmCompletionTime,'cucsNfsMountInstFsmCurrentFsm':cucsNfsMountInstFsmCurrentFsm,'cucsNfsMountInstFsmDescrData':cucsNfsMountInstFsmDescrData,'cucsNfsMountInstFsmFsmStatus':cucsNfsMountInstFsmFsmStatus,'cucsNfsMountInstFsmProgress':cucsNfsMountInstFsmProgress,'cucsNfsMountInstFsmRmtErrCode':cucsNfsMountInstFsmRmtErrCode,'cucsNfsMountInstFsmRmtErrDescr':cucsNfsMountInstFsmRmtErrDescr,'cucsNfsMountInstFsmRmtRslt':cucsNfsMountInstFsmRmtRslt,'cucsNfsMountInstFsmStageTable':cucsNfsMountInstFsmStageTable,'cucsNfsMountInstFsmStageEntry':cucsNfsMountInstFsmStageEntry,_L:cucsNfsMountInstFsmStageInstanceId,'cucsNfsMountInstFsmStageDn':cucsNfsMountInstFsmStageDn,'cucsNfsMountInstFsmStageRn':cucsNfsMountInstFsmStageRn,'cucsNfsMountInstFsmStageDescrData':cucsNfsMountInstFsmStageDescrData,'cucsNfsMountInstFsmStageLastUpdateTime':cucsNfsMountInstFsmStageLastUpdateTime,'cucsNfsMountInstFsmStageName':cucsNfsMountInstFsmStageName,'cucsNfsMountInstFsmStageOrder':cucsNfsMountInstFsmStageOrder,'cucsNfsMountInstFsmStageRetry':cucsNfsMountInstFsmStageRetry,'cucsNfsMountInstFsmStageStageStatus':cucsNfsMountInstFsmStageStageStatus,'cucsNfsMountInstFsmTaskTable':cucsNfsMountInstFsmTaskTable,'cucsNfsMountInstFsmTaskEntry':cucsNfsMountInstFsmTaskEntry,_M:cucsNfsMountInstFsmTaskInstanceId,'cucsNfsMountInstFsmTaskDn':cucsNfsMountInstFsmTaskDn,'cucsNfsMountInstFsmTaskRn':cucsNfsMountInstFsmTaskRn,'cucsNfsMountInstFsmTaskCompletion':cucsNfsMountInstFsmTaskCompletion,'cucsNfsMountInstFsmTaskFlags':cucsNfsMountInstFsmTaskFlags,'cucsNfsMountInstFsmTaskItem':cucsNfsMountInstFsmTaskItem,'cucsNfsMountInstFsmTaskSeqId':cucsNfsMountInstFsmTaskSeqId})