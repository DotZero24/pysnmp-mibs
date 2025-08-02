_K='cucsPortSubGroupInstanceId'
_J='cucsPortPIoFsmStageInstanceId'
_I='cucsPortPIoFsmInstanceId'
_H='cucsPortPIoFsmTaskInstanceId'
_G='cucsPortTrustModeInstanceId'
_F='cucsPortGroupInstanceId'
_E='cucsPortDomainEpInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-PORT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsConditionRemoteInvRslt,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsLicenseState,CucsNetworkConnectionType,CucsNetworkLocale,CucsNetworkPortRole,CucsNetworkPortType,CucsNetworkSwitchId,CucsNetworkTransport,CucsPortGroupType,CucsPortPIoFsmCurrentFsm,CucsPortPIoFsmStageName,CucsPortPIoFsmTaskItem,CucsPortSubGroupConfigState,CucsPortSubGroupSlotId,CucsPortTrust=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsConditionRemoteInvRslt','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsLicenseState','CucsNetworkConnectionType','CucsNetworkLocale','CucsNetworkPortRole','CucsNetworkPortType','CucsNetworkSwitchId','CucsNetworkTransport','CucsPortGroupType','CucsPortPIoFsmCurrentFsm','CucsPortPIoFsmStageName','CucsPortPIoFsmTaskItem','CucsPortSubGroupConfigState','CucsPortSubGroupSlotId','CucsPortTrust')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsPortObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,38))
_CucsPortDomainEpTable_Object=MibTable
cucsPortDomainEpTable=_CucsPortDomainEpTable_Object((1,3,6,1,4,1,9,9,719,1,38,1))
if mibBuilder.loadTexts:cucsPortDomainEpTable.setStatus(_A)
_CucsPortDomainEpEntry_Object=MibTableRow
cucsPortDomainEpEntry=_CucsPortDomainEpEntry_Object((1,3,6,1,4,1,9,9,719,1,38,1,1))
cucsPortDomainEpEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsPortDomainEpEntry.setStatus(_A)
_CucsPortDomainEpInstanceId_Type=CucsManagedObjectId
_CucsPortDomainEpInstanceId_Object=MibTableColumn
cucsPortDomainEpInstanceId=_CucsPortDomainEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,1),_CucsPortDomainEpInstanceId_Type())
cucsPortDomainEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPortDomainEpInstanceId.setStatus(_A)
_CucsPortDomainEpDn_Type=CucsManagedObjectDn
_CucsPortDomainEpDn_Object=MibTableColumn
cucsPortDomainEpDn=_CucsPortDomainEpDn_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,2),_CucsPortDomainEpDn_Type())
cucsPortDomainEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpDn.setStatus(_A)
_CucsPortDomainEpRn_Type=SnmpAdminString
_CucsPortDomainEpRn_Object=MibTableColumn
cucsPortDomainEpRn=_CucsPortDomainEpRn_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,3),_CucsPortDomainEpRn_Type())
cucsPortDomainEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpRn.setStatus(_A)
_CucsPortDomainEpEpDn_Type=SnmpAdminString
_CucsPortDomainEpEpDn_Object=MibTableColumn
cucsPortDomainEpEpDn=_CucsPortDomainEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,4),_CucsPortDomainEpEpDn_Type())
cucsPortDomainEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpEpDn.setStatus(_A)
_CucsPortDomainEpIfRole_Type=CucsNetworkPortRole
_CucsPortDomainEpIfRole_Object=MibTableColumn
cucsPortDomainEpIfRole=_CucsPortDomainEpIfRole_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,5),_CucsPortDomainEpIfRole_Type())
cucsPortDomainEpIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpIfRole.setStatus(_A)
_CucsPortDomainEpIfType_Type=CucsNetworkPortType
_CucsPortDomainEpIfType_Object=MibTableColumn
cucsPortDomainEpIfType=_CucsPortDomainEpIfType_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,6),_CucsPortDomainEpIfType_Type())
cucsPortDomainEpIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpIfType.setStatus(_A)
_CucsPortDomainEpLocale_Type=CucsNetworkLocale
_CucsPortDomainEpLocale_Object=MibTableColumn
cucsPortDomainEpLocale=_CucsPortDomainEpLocale_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,7),_CucsPortDomainEpLocale_Type())
cucsPortDomainEpLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpLocale.setStatus(_A)
_CucsPortDomainEpName_Type=SnmpAdminString
_CucsPortDomainEpName_Object=MibTableColumn
cucsPortDomainEpName=_CucsPortDomainEpName_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,8),_CucsPortDomainEpName_Type())
cucsPortDomainEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpName.setStatus(_A)
_CucsPortDomainEpPeerDn_Type=SnmpAdminString
_CucsPortDomainEpPeerDn_Object=MibTableColumn
cucsPortDomainEpPeerDn=_CucsPortDomainEpPeerDn_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,9),_CucsPortDomainEpPeerDn_Type())
cucsPortDomainEpPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpPeerDn.setStatus(_A)
_CucsPortDomainEpTransport_Type=CucsNetworkTransport
_CucsPortDomainEpTransport_Object=MibTableColumn
cucsPortDomainEpTransport=_CucsPortDomainEpTransport_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,10),_CucsPortDomainEpTransport_Type())
cucsPortDomainEpTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpTransport.setStatus(_A)
_CucsPortDomainEpType_Type=CucsNetworkConnectionType
_CucsPortDomainEpType_Object=MibTableColumn
cucsPortDomainEpType=_CucsPortDomainEpType_Object((1,3,6,1,4,1,9,9,719,1,38,1,1,11),_CucsPortDomainEpType_Type())
cucsPortDomainEpType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortDomainEpType.setStatus(_A)
_CucsPortGroupTable_Object=MibTable
cucsPortGroupTable=_CucsPortGroupTable_Object((1,3,6,1,4,1,9,9,719,1,38,2))
if mibBuilder.loadTexts:cucsPortGroupTable.setStatus(_A)
_CucsPortGroupEntry_Object=MibTableRow
cucsPortGroupEntry=_CucsPortGroupEntry_Object((1,3,6,1,4,1,9,9,719,1,38,2,1))
cucsPortGroupEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsPortGroupEntry.setStatus(_A)
_CucsPortGroupInstanceId_Type=CucsManagedObjectId
_CucsPortGroupInstanceId_Object=MibTableColumn
cucsPortGroupInstanceId=_CucsPortGroupInstanceId_Object((1,3,6,1,4,1,9,9,719,1,38,2,1,1),_CucsPortGroupInstanceId_Type())
cucsPortGroupInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPortGroupInstanceId.setStatus(_A)
_CucsPortGroupDn_Type=CucsManagedObjectDn
_CucsPortGroupDn_Object=MibTableColumn
cucsPortGroupDn=_CucsPortGroupDn_Object((1,3,6,1,4,1,9,9,719,1,38,2,1,2),_CucsPortGroupDn_Type())
cucsPortGroupDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortGroupDn.setStatus(_A)
_CucsPortGroupRn_Type=SnmpAdminString
_CucsPortGroupRn_Object=MibTableColumn
cucsPortGroupRn=_CucsPortGroupRn_Object((1,3,6,1,4,1,9,9,719,1,38,2,1,3),_CucsPortGroupRn_Type())
cucsPortGroupRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortGroupRn.setStatus(_A)
_CucsPortGroupLocale_Type=CucsNetworkLocale
_CucsPortGroupLocale_Object=MibTableColumn
cucsPortGroupLocale=_CucsPortGroupLocale_Object((1,3,6,1,4,1,9,9,719,1,38,2,1,4),_CucsPortGroupLocale_Type())
cucsPortGroupLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortGroupLocale.setStatus(_A)
_CucsPortGroupName_Type=SnmpAdminString
_CucsPortGroupName_Object=MibTableColumn
cucsPortGroupName=_CucsPortGroupName_Object((1,3,6,1,4,1,9,9,719,1,38,2,1,5),_CucsPortGroupName_Type())
cucsPortGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortGroupName.setStatus(_A)
_CucsPortGroupTransport_Type=CucsNetworkTransport
_CucsPortGroupTransport_Object=MibTableColumn
cucsPortGroupTransport=_CucsPortGroupTransport_Object((1,3,6,1,4,1,9,9,719,1,38,2,1,6),_CucsPortGroupTransport_Type())
cucsPortGroupTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortGroupTransport.setStatus(_A)
_CucsPortGroupType_Type=CucsPortGroupType
_CucsPortGroupType_Object=MibTableColumn
cucsPortGroupType=_CucsPortGroupType_Object((1,3,6,1,4,1,9,9,719,1,38,2,1,7),_CucsPortGroupType_Type())
cucsPortGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortGroupType.setStatus(_A)
_CucsPortTrustModeTable_Object=MibTable
cucsPortTrustModeTable=_CucsPortTrustModeTable_Object((1,3,6,1,4,1,9,9,719,1,38,3))
if mibBuilder.loadTexts:cucsPortTrustModeTable.setStatus(_A)
_CucsPortTrustModeEntry_Object=MibTableRow
cucsPortTrustModeEntry=_CucsPortTrustModeEntry_Object((1,3,6,1,4,1,9,9,719,1,38,3,1))
cucsPortTrustModeEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsPortTrustModeEntry.setStatus(_A)
_CucsPortTrustModeInstanceId_Type=CucsManagedObjectId
_CucsPortTrustModeInstanceId_Object=MibTableColumn
cucsPortTrustModeInstanceId=_CucsPortTrustModeInstanceId_Object((1,3,6,1,4,1,9,9,719,1,38,3,1,1),_CucsPortTrustModeInstanceId_Type())
cucsPortTrustModeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPortTrustModeInstanceId.setStatus(_A)
_CucsPortTrustModeDn_Type=CucsManagedObjectDn
_CucsPortTrustModeDn_Object=MibTableColumn
cucsPortTrustModeDn=_CucsPortTrustModeDn_Object((1,3,6,1,4,1,9,9,719,1,38,3,1,2),_CucsPortTrustModeDn_Type())
cucsPortTrustModeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortTrustModeDn.setStatus(_A)
_CucsPortTrustModeRn_Type=SnmpAdminString
_CucsPortTrustModeRn_Object=MibTableColumn
cucsPortTrustModeRn=_CucsPortTrustModeRn_Object((1,3,6,1,4,1,9,9,719,1,38,3,1,3),_CucsPortTrustModeRn_Type())
cucsPortTrustModeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortTrustModeRn.setStatus(_A)
_CucsPortTrustModeState_Type=CucsPortTrust
_CucsPortTrustModeState_Object=MibTableColumn
cucsPortTrustModeState=_CucsPortTrustModeState_Object((1,3,6,1,4,1,9,9,719,1,38,3,1,4),_CucsPortTrustModeState_Type())
cucsPortTrustModeState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortTrustModeState.setStatus(_A)
_CucsPortPIoFsmTaskTable_Object=MibTable
cucsPortPIoFsmTaskTable=_CucsPortPIoFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,38,4))
if mibBuilder.loadTexts:cucsPortPIoFsmTaskTable.setStatus(_A)
_CucsPortPIoFsmTaskEntry_Object=MibTableRow
cucsPortPIoFsmTaskEntry=_CucsPortPIoFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,38,4,1))
cucsPortPIoFsmTaskEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsPortPIoFsmTaskEntry.setStatus(_A)
_CucsPortPIoFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsPortPIoFsmTaskInstanceId_Object=MibTableColumn
cucsPortPIoFsmTaskInstanceId=_CucsPortPIoFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,38,4,1,1),_CucsPortPIoFsmTaskInstanceId_Type())
cucsPortPIoFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPortPIoFsmTaskInstanceId.setStatus(_A)
_CucsPortPIoFsmTaskDn_Type=CucsManagedObjectDn
_CucsPortPIoFsmTaskDn_Object=MibTableColumn
cucsPortPIoFsmTaskDn=_CucsPortPIoFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,38,4,1,2),_CucsPortPIoFsmTaskDn_Type())
cucsPortPIoFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmTaskDn.setStatus(_A)
_CucsPortPIoFsmTaskRn_Type=SnmpAdminString
_CucsPortPIoFsmTaskRn_Object=MibTableColumn
cucsPortPIoFsmTaskRn=_CucsPortPIoFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,38,4,1,3),_CucsPortPIoFsmTaskRn_Type())
cucsPortPIoFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmTaskRn.setStatus(_A)
_CucsPortPIoFsmTaskCompletion_Type=CucsFsmCompletion
_CucsPortPIoFsmTaskCompletion_Object=MibTableColumn
cucsPortPIoFsmTaskCompletion=_CucsPortPIoFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,38,4,1,4),_CucsPortPIoFsmTaskCompletion_Type())
cucsPortPIoFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmTaskCompletion.setStatus(_A)
_CucsPortPIoFsmTaskFlags_Type=CucsFsmFlags
_CucsPortPIoFsmTaskFlags_Object=MibTableColumn
cucsPortPIoFsmTaskFlags=_CucsPortPIoFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,38,4,1,5),_CucsPortPIoFsmTaskFlags_Type())
cucsPortPIoFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmTaskFlags.setStatus(_A)
_CucsPortPIoFsmTaskItem_Type=CucsPortPIoFsmTaskItem
_CucsPortPIoFsmTaskItem_Object=MibTableColumn
cucsPortPIoFsmTaskItem=_CucsPortPIoFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,38,4,1,6),_CucsPortPIoFsmTaskItem_Type())
cucsPortPIoFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmTaskItem.setStatus(_A)
_CucsPortPIoFsmTaskSeqId_Type=Gauge32
_CucsPortPIoFsmTaskSeqId_Object=MibTableColumn
cucsPortPIoFsmTaskSeqId=_CucsPortPIoFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,38,4,1,7),_CucsPortPIoFsmTaskSeqId_Type())
cucsPortPIoFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmTaskSeqId.setStatus(_A)
_CucsPortPIoFsmTable_Object=MibTable
cucsPortPIoFsmTable=_CucsPortPIoFsmTable_Object((1,3,6,1,4,1,9,9,719,1,38,5))
if mibBuilder.loadTexts:cucsPortPIoFsmTable.setStatus(_A)
_CucsPortPIoFsmEntry_Object=MibTableRow
cucsPortPIoFsmEntry=_CucsPortPIoFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,38,5,1))
cucsPortPIoFsmEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsPortPIoFsmEntry.setStatus(_A)
_CucsPortPIoFsmInstanceId_Type=CucsManagedObjectId
_CucsPortPIoFsmInstanceId_Object=MibTableColumn
cucsPortPIoFsmInstanceId=_CucsPortPIoFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,1),_CucsPortPIoFsmInstanceId_Type())
cucsPortPIoFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPortPIoFsmInstanceId.setStatus(_A)
_CucsPortPIoFsmDn_Type=CucsManagedObjectDn
_CucsPortPIoFsmDn_Object=MibTableColumn
cucsPortPIoFsmDn=_CucsPortPIoFsmDn_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,2),_CucsPortPIoFsmDn_Type())
cucsPortPIoFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmDn.setStatus(_A)
_CucsPortPIoFsmRn_Type=SnmpAdminString
_CucsPortPIoFsmRn_Object=MibTableColumn
cucsPortPIoFsmRn=_CucsPortPIoFsmRn_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,3),_CucsPortPIoFsmRn_Type())
cucsPortPIoFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmRn.setStatus(_A)
_CucsPortPIoFsmCompletionTime_Type=DateAndTime
_CucsPortPIoFsmCompletionTime_Object=MibTableColumn
cucsPortPIoFsmCompletionTime=_CucsPortPIoFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,4),_CucsPortPIoFsmCompletionTime_Type())
cucsPortPIoFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmCompletionTime.setStatus(_A)
_CucsPortPIoFsmCurrentFsm_Type=CucsPortPIoFsmCurrentFsm
_CucsPortPIoFsmCurrentFsm_Object=MibTableColumn
cucsPortPIoFsmCurrentFsm=_CucsPortPIoFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,5),_CucsPortPIoFsmCurrentFsm_Type())
cucsPortPIoFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmCurrentFsm.setStatus(_A)
_CucsPortPIoFsmDescr_Type=SnmpAdminString
_CucsPortPIoFsmDescr_Object=MibTableColumn
cucsPortPIoFsmDescr=_CucsPortPIoFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,6),_CucsPortPIoFsmDescr_Type())
cucsPortPIoFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmDescr.setStatus(_A)
_CucsPortPIoFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsPortPIoFsmFsmStatus_Object=MibTableColumn
cucsPortPIoFsmFsmStatus=_CucsPortPIoFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,7),_CucsPortPIoFsmFsmStatus_Type())
cucsPortPIoFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmFsmStatus.setStatus(_A)
_CucsPortPIoFsmProgress_Type=Gauge32
_CucsPortPIoFsmProgress_Object=MibTableColumn
cucsPortPIoFsmProgress=_CucsPortPIoFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,8),_CucsPortPIoFsmProgress_Type())
cucsPortPIoFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmProgress.setStatus(_A)
_CucsPortPIoFsmRmtErrCode_Type=Gauge32
_CucsPortPIoFsmRmtErrCode_Object=MibTableColumn
cucsPortPIoFsmRmtErrCode=_CucsPortPIoFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,9),_CucsPortPIoFsmRmtErrCode_Type())
cucsPortPIoFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmRmtErrCode.setStatus(_A)
_CucsPortPIoFsmRmtErrDescr_Type=SnmpAdminString
_CucsPortPIoFsmRmtErrDescr_Object=MibTableColumn
cucsPortPIoFsmRmtErrDescr=_CucsPortPIoFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,10),_CucsPortPIoFsmRmtErrDescr_Type())
cucsPortPIoFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmRmtErrDescr.setStatus(_A)
_CucsPortPIoFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsPortPIoFsmRmtRslt_Object=MibTableColumn
cucsPortPIoFsmRmtRslt=_CucsPortPIoFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,38,5,1,11),_CucsPortPIoFsmRmtRslt_Type())
cucsPortPIoFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmRmtRslt.setStatus(_A)
_CucsPortPIoFsmStageTable_Object=MibTable
cucsPortPIoFsmStageTable=_CucsPortPIoFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,38,6))
if mibBuilder.loadTexts:cucsPortPIoFsmStageTable.setStatus(_A)
_CucsPortPIoFsmStageEntry_Object=MibTableRow
cucsPortPIoFsmStageEntry=_CucsPortPIoFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,38,6,1))
cucsPortPIoFsmStageEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsPortPIoFsmStageEntry.setStatus(_A)
_CucsPortPIoFsmStageInstanceId_Type=CucsManagedObjectId
_CucsPortPIoFsmStageInstanceId_Object=MibTableColumn
cucsPortPIoFsmStageInstanceId=_CucsPortPIoFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,38,6,1,1),_CucsPortPIoFsmStageInstanceId_Type())
cucsPortPIoFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPortPIoFsmStageInstanceId.setStatus(_A)
_CucsPortPIoFsmStageDn_Type=CucsManagedObjectDn
_CucsPortPIoFsmStageDn_Object=MibTableColumn
cucsPortPIoFsmStageDn=_CucsPortPIoFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,38,6,1,2),_CucsPortPIoFsmStageDn_Type())
cucsPortPIoFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmStageDn.setStatus(_A)
_CucsPortPIoFsmStageRn_Type=SnmpAdminString
_CucsPortPIoFsmStageRn_Object=MibTableColumn
cucsPortPIoFsmStageRn=_CucsPortPIoFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,38,6,1,3),_CucsPortPIoFsmStageRn_Type())
cucsPortPIoFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmStageRn.setStatus(_A)
_CucsPortPIoFsmStageDescr_Type=SnmpAdminString
_CucsPortPIoFsmStageDescr_Object=MibTableColumn
cucsPortPIoFsmStageDescr=_CucsPortPIoFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,38,6,1,4),_CucsPortPIoFsmStageDescr_Type())
cucsPortPIoFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmStageDescr.setStatus(_A)
_CucsPortPIoFsmStageLastUpdateTime_Type=DateAndTime
_CucsPortPIoFsmStageLastUpdateTime_Object=MibTableColumn
cucsPortPIoFsmStageLastUpdateTime=_CucsPortPIoFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,38,6,1,5),_CucsPortPIoFsmStageLastUpdateTime_Type())
cucsPortPIoFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmStageLastUpdateTime.setStatus(_A)
_CucsPortPIoFsmStageName_Type=CucsPortPIoFsmStageName
_CucsPortPIoFsmStageName_Object=MibTableColumn
cucsPortPIoFsmStageName=_CucsPortPIoFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,38,6,1,6),_CucsPortPIoFsmStageName_Type())
cucsPortPIoFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmStageName.setStatus(_A)
_CucsPortPIoFsmStageOrder_Type=Gauge32
_CucsPortPIoFsmStageOrder_Object=MibTableColumn
cucsPortPIoFsmStageOrder=_CucsPortPIoFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,38,6,1,7),_CucsPortPIoFsmStageOrder_Type())
cucsPortPIoFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmStageOrder.setStatus(_A)
_CucsPortPIoFsmStageRetry_Type=Gauge32
_CucsPortPIoFsmStageRetry_Object=MibTableColumn
cucsPortPIoFsmStageRetry=_CucsPortPIoFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,38,6,1,8),_CucsPortPIoFsmStageRetry_Type())
cucsPortPIoFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmStageRetry.setStatus(_A)
_CucsPortPIoFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsPortPIoFsmStageStageStatus_Object=MibTableColumn
cucsPortPIoFsmStageStageStatus=_CucsPortPIoFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,38,6,1,9),_CucsPortPIoFsmStageStageStatus_Type())
cucsPortPIoFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortPIoFsmStageStageStatus.setStatus(_A)
_CucsPortSubGroupTable_Object=MibTable
cucsPortSubGroupTable=_CucsPortSubGroupTable_Object((1,3,6,1,4,1,9,9,719,1,38,7))
if mibBuilder.loadTexts:cucsPortSubGroupTable.setStatus(_A)
_CucsPortSubGroupEntry_Object=MibTableRow
cucsPortSubGroupEntry=_CucsPortSubGroupEntry_Object((1,3,6,1,4,1,9,9,719,1,38,7,1))
cucsPortSubGroupEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsPortSubGroupEntry.setStatus(_A)
_CucsPortSubGroupInstanceId_Type=CucsManagedObjectId
_CucsPortSubGroupInstanceId_Object=MibTableColumn
cucsPortSubGroupInstanceId=_CucsPortSubGroupInstanceId_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,1),_CucsPortSubGroupInstanceId_Type())
cucsPortSubGroupInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPortSubGroupInstanceId.setStatus(_A)
_CucsPortSubGroupDn_Type=CucsManagedObjectDn
_CucsPortSubGroupDn_Object=MibTableColumn
cucsPortSubGroupDn=_CucsPortSubGroupDn_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,2),_CucsPortSubGroupDn_Type())
cucsPortSubGroupDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupDn.setStatus(_A)
_CucsPortSubGroupRn_Type=SnmpAdminString
_CucsPortSubGroupRn_Object=MibTableColumn
cucsPortSubGroupRn=_CucsPortSubGroupRn_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,3),_CucsPortSubGroupRn_Type())
cucsPortSubGroupRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupRn.setStatus(_A)
_CucsPortSubGroupAggrPortId_Type=Gauge32
_CucsPortSubGroupAggrPortId_Object=MibTableColumn
cucsPortSubGroupAggrPortId=_CucsPortSubGroupAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,4),_CucsPortSubGroupAggrPortId_Type())
cucsPortSubGroupAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupAggrPortId.setStatus(_A)
_CucsPortSubGroupConfigState_Type=CucsPortSubGroupConfigState
_CucsPortSubGroupConfigState_Object=MibTableColumn
cucsPortSubGroupConfigState=_CucsPortSubGroupConfigState_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,5),_CucsPortSubGroupConfigState_Type())
cucsPortSubGroupConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupConfigState.setStatus(_A)
_CucsPortSubGroupLicGP_Type=Unsigned64
_CucsPortSubGroupLicGP_Object=MibTableColumn
cucsPortSubGroupLicGP=_CucsPortSubGroupLicGP_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,6),_CucsPortSubGroupLicGP_Type())
cucsPortSubGroupLicGP.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupLicGP.setStatus(_A)
_CucsPortSubGroupLicState_Type=CucsLicenseState
_CucsPortSubGroupLicState_Object=MibTableColumn
cucsPortSubGroupLicState=_CucsPortSubGroupLicState_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,7),_CucsPortSubGroupLicState_Type())
cucsPortSubGroupLicState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupLicState.setStatus(_A)
_CucsPortSubGroupLocale_Type=CucsNetworkLocale
_CucsPortSubGroupLocale_Object=MibTableColumn
cucsPortSubGroupLocale=_CucsPortSubGroupLocale_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,8),_CucsPortSubGroupLocale_Type())
cucsPortSubGroupLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupLocale.setStatus(_A)
_CucsPortSubGroupName_Type=SnmpAdminString
_CucsPortSubGroupName_Object=MibTableColumn
cucsPortSubGroupName=_CucsPortSubGroupName_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,9),_CucsPortSubGroupName_Type())
cucsPortSubGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupName.setStatus(_A)
_CucsPortSubGroupSlotId_Type=CucsPortSubGroupSlotId
_CucsPortSubGroupSlotId_Object=MibTableColumn
cucsPortSubGroupSlotId=_CucsPortSubGroupSlotId_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,10),_CucsPortSubGroupSlotId_Type())
cucsPortSubGroupSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupSlotId.setStatus(_A)
_CucsPortSubGroupSwitchId_Type=CucsNetworkSwitchId
_CucsPortSubGroupSwitchId_Object=MibTableColumn
cucsPortSubGroupSwitchId=_CucsPortSubGroupSwitchId_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,11),_CucsPortSubGroupSwitchId_Type())
cucsPortSubGroupSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupSwitchId.setStatus(_A)
_CucsPortSubGroupTransport_Type=CucsNetworkTransport
_CucsPortSubGroupTransport_Object=MibTableColumn
cucsPortSubGroupTransport=_CucsPortSubGroupTransport_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,12),_CucsPortSubGroupTransport_Type())
cucsPortSubGroupTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupTransport.setStatus(_A)
_CucsPortSubGroupType_Type=CucsNetworkConnectionType
_CucsPortSubGroupType_Object=MibTableColumn
cucsPortSubGroupType=_CucsPortSubGroupType_Object((1,3,6,1,4,1,9,9,719,1,38,7,1,13),_CucsPortSubGroupType_Type())
cucsPortSubGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPortSubGroupType.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsPortObjects':cucsPortObjects,'cucsPortDomainEpTable':cucsPortDomainEpTable,'cucsPortDomainEpEntry':cucsPortDomainEpEntry,_E:cucsPortDomainEpInstanceId,'cucsPortDomainEpDn':cucsPortDomainEpDn,'cucsPortDomainEpRn':cucsPortDomainEpRn,'cucsPortDomainEpEpDn':cucsPortDomainEpEpDn,'cucsPortDomainEpIfRole':cucsPortDomainEpIfRole,'cucsPortDomainEpIfType':cucsPortDomainEpIfType,'cucsPortDomainEpLocale':cucsPortDomainEpLocale,'cucsPortDomainEpName':cucsPortDomainEpName,'cucsPortDomainEpPeerDn':cucsPortDomainEpPeerDn,'cucsPortDomainEpTransport':cucsPortDomainEpTransport,'cucsPortDomainEpType':cucsPortDomainEpType,'cucsPortGroupTable':cucsPortGroupTable,'cucsPortGroupEntry':cucsPortGroupEntry,_F:cucsPortGroupInstanceId,'cucsPortGroupDn':cucsPortGroupDn,'cucsPortGroupRn':cucsPortGroupRn,'cucsPortGroupLocale':cucsPortGroupLocale,'cucsPortGroupName':cucsPortGroupName,'cucsPortGroupTransport':cucsPortGroupTransport,'cucsPortGroupType':cucsPortGroupType,'cucsPortTrustModeTable':cucsPortTrustModeTable,'cucsPortTrustModeEntry':cucsPortTrustModeEntry,_G:cucsPortTrustModeInstanceId,'cucsPortTrustModeDn':cucsPortTrustModeDn,'cucsPortTrustModeRn':cucsPortTrustModeRn,'cucsPortTrustModeState':cucsPortTrustModeState,'cucsPortPIoFsmTaskTable':cucsPortPIoFsmTaskTable,'cucsPortPIoFsmTaskEntry':cucsPortPIoFsmTaskEntry,_H:cucsPortPIoFsmTaskInstanceId,'cucsPortPIoFsmTaskDn':cucsPortPIoFsmTaskDn,'cucsPortPIoFsmTaskRn':cucsPortPIoFsmTaskRn,'cucsPortPIoFsmTaskCompletion':cucsPortPIoFsmTaskCompletion,'cucsPortPIoFsmTaskFlags':cucsPortPIoFsmTaskFlags,'cucsPortPIoFsmTaskItem':cucsPortPIoFsmTaskItem,'cucsPortPIoFsmTaskSeqId':cucsPortPIoFsmTaskSeqId,'cucsPortPIoFsmTable':cucsPortPIoFsmTable,'cucsPortPIoFsmEntry':cucsPortPIoFsmEntry,_I:cucsPortPIoFsmInstanceId,'cucsPortPIoFsmDn':cucsPortPIoFsmDn,'cucsPortPIoFsmRn':cucsPortPIoFsmRn,'cucsPortPIoFsmCompletionTime':cucsPortPIoFsmCompletionTime,'cucsPortPIoFsmCurrentFsm':cucsPortPIoFsmCurrentFsm,'cucsPortPIoFsmDescr':cucsPortPIoFsmDescr,'cucsPortPIoFsmFsmStatus':cucsPortPIoFsmFsmStatus,'cucsPortPIoFsmProgress':cucsPortPIoFsmProgress,'cucsPortPIoFsmRmtErrCode':cucsPortPIoFsmRmtErrCode,'cucsPortPIoFsmRmtErrDescr':cucsPortPIoFsmRmtErrDescr,'cucsPortPIoFsmRmtRslt':cucsPortPIoFsmRmtRslt,'cucsPortPIoFsmStageTable':cucsPortPIoFsmStageTable,'cucsPortPIoFsmStageEntry':cucsPortPIoFsmStageEntry,_J:cucsPortPIoFsmStageInstanceId,'cucsPortPIoFsmStageDn':cucsPortPIoFsmStageDn,'cucsPortPIoFsmStageRn':cucsPortPIoFsmStageRn,'cucsPortPIoFsmStageDescr':cucsPortPIoFsmStageDescr,'cucsPortPIoFsmStageLastUpdateTime':cucsPortPIoFsmStageLastUpdateTime,'cucsPortPIoFsmStageName':cucsPortPIoFsmStageName,'cucsPortPIoFsmStageOrder':cucsPortPIoFsmStageOrder,'cucsPortPIoFsmStageRetry':cucsPortPIoFsmStageRetry,'cucsPortPIoFsmStageStageStatus':cucsPortPIoFsmStageStageStatus,'cucsPortSubGroupTable':cucsPortSubGroupTable,'cucsPortSubGroupEntry':cucsPortSubGroupEntry,_K:cucsPortSubGroupInstanceId,'cucsPortSubGroupDn':cucsPortSubGroupDn,'cucsPortSubGroupRn':cucsPortSubGroupRn,'cucsPortSubGroupAggrPortId':cucsPortSubGroupAggrPortId,'cucsPortSubGroupConfigState':cucsPortSubGroupConfigState,'cucsPortSubGroupLicGP':cucsPortSubGroupLicGP,'cucsPortSubGroupLicState':cucsPortSubGroupLicState,'cucsPortSubGroupLocale':cucsPortSubGroupLocale,'cucsPortSubGroupName':cucsPortSubGroupName,'cucsPortSubGroupSlotId':cucsPortSubGroupSlotId,'cucsPortSubGroupSwitchId':cucsPortSubGroupSwitchId,'cucsPortSubGroupTransport':cucsPortSubGroupTransport,'cucsPortSubGroupType':cucsPortSubGroupType})