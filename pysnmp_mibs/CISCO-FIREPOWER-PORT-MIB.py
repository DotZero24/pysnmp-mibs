_K='cfprPortTrustModeInstanceId'
_J='cfprPortSubGroupInstanceId'
_I='cfprPortPIoFsmTaskInstanceId'
_H='cfprPortPIoFsmStageInstanceId'
_G='cfprPortPIoFsmInstanceId'
_F='cfprPortGroupInstanceId'
_E='cfprPortDomainEpInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-PORT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprConditionRemoteInvRslt,CfprFsmCompletion,CfprFsmFlags,CfprFsmFsmStageStatus,CfprLicenseState,CfprNetworkConnectionType,CfprNetworkLocale,CfprNetworkPortRole,CfprNetworkPortType,CfprNetworkSwitchId,CfprNetworkTransport,CfprPortGroupType,CfprPortPIoFsmCurrentFsm,CfprPortPIoFsmStageName,CfprPortPIoFsmTaskItem,CfprPortSubGroupConfigState,CfprPortSubGroupSlotId,CfprPortTrust=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprConditionRemoteInvRslt','CfprFsmCompletion','CfprFsmFlags','CfprFsmFsmStageStatus','CfprLicenseState','CfprNetworkConnectionType','CfprNetworkLocale','CfprNetworkPortRole','CfprNetworkPortType','CfprNetworkSwitchId','CfprNetworkTransport','CfprPortGroupType','CfprPortPIoFsmCurrentFsm','CfprPortPIoFsmStageName','CfprPortPIoFsmTaskItem','CfprPortSubGroupConfigState','CfprPortSubGroupSlotId','CfprPortTrust')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprPortObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,63))
_CfprPortDomainEpTable_Object=MibTable
cfprPortDomainEpTable=_CfprPortDomainEpTable_Object((1,3,6,1,4,1,9,9,826,1,63,1))
if mibBuilder.loadTexts:cfprPortDomainEpTable.setStatus(_A)
_CfprPortDomainEpEntry_Object=MibTableRow
cfprPortDomainEpEntry=_CfprPortDomainEpEntry_Object((1,3,6,1,4,1,9,9,826,1,63,1,1))
cfprPortDomainEpEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprPortDomainEpEntry.setStatus(_A)
_CfprPortDomainEpInstanceId_Type=CfprManagedObjectId
_CfprPortDomainEpInstanceId_Object=MibTableColumn
cfprPortDomainEpInstanceId=_CfprPortDomainEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,1),_CfprPortDomainEpInstanceId_Type())
cfprPortDomainEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPortDomainEpInstanceId.setStatus(_A)
_CfprPortDomainEpDn_Type=CfprManagedObjectDn
_CfprPortDomainEpDn_Object=MibTableColumn
cfprPortDomainEpDn=_CfprPortDomainEpDn_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,2),_CfprPortDomainEpDn_Type())
cfprPortDomainEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpDn.setStatus(_A)
_CfprPortDomainEpRn_Type=SnmpAdminString
_CfprPortDomainEpRn_Object=MibTableColumn
cfprPortDomainEpRn=_CfprPortDomainEpRn_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,3),_CfprPortDomainEpRn_Type())
cfprPortDomainEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpRn.setStatus(_A)
_CfprPortDomainEpEpDn_Type=SnmpAdminString
_CfprPortDomainEpEpDn_Object=MibTableColumn
cfprPortDomainEpEpDn=_CfprPortDomainEpEpDn_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,4),_CfprPortDomainEpEpDn_Type())
cfprPortDomainEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpEpDn.setStatus(_A)
_CfprPortDomainEpIfRole_Type=CfprNetworkPortRole
_CfprPortDomainEpIfRole_Object=MibTableColumn
cfprPortDomainEpIfRole=_CfprPortDomainEpIfRole_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,5),_CfprPortDomainEpIfRole_Type())
cfprPortDomainEpIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpIfRole.setStatus(_A)
_CfprPortDomainEpIfType_Type=CfprNetworkPortType
_CfprPortDomainEpIfType_Object=MibTableColumn
cfprPortDomainEpIfType=_CfprPortDomainEpIfType_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,6),_CfprPortDomainEpIfType_Type())
cfprPortDomainEpIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpIfType.setStatus(_A)
_CfprPortDomainEpLocale_Type=CfprNetworkLocale
_CfprPortDomainEpLocale_Object=MibTableColumn
cfprPortDomainEpLocale=_CfprPortDomainEpLocale_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,7),_CfprPortDomainEpLocale_Type())
cfprPortDomainEpLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpLocale.setStatus(_A)
_CfprPortDomainEpName_Type=SnmpAdminString
_CfprPortDomainEpName_Object=MibTableColumn
cfprPortDomainEpName=_CfprPortDomainEpName_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,8),_CfprPortDomainEpName_Type())
cfprPortDomainEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpName.setStatus(_A)
_CfprPortDomainEpPeerDn_Type=SnmpAdminString
_CfprPortDomainEpPeerDn_Object=MibTableColumn
cfprPortDomainEpPeerDn=_CfprPortDomainEpPeerDn_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,9),_CfprPortDomainEpPeerDn_Type())
cfprPortDomainEpPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpPeerDn.setStatus(_A)
_CfprPortDomainEpTransport_Type=CfprNetworkTransport
_CfprPortDomainEpTransport_Object=MibTableColumn
cfprPortDomainEpTransport=_CfprPortDomainEpTransport_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,10),_CfprPortDomainEpTransport_Type())
cfprPortDomainEpTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpTransport.setStatus(_A)
_CfprPortDomainEpType_Type=CfprNetworkConnectionType
_CfprPortDomainEpType_Object=MibTableColumn
cfprPortDomainEpType=_CfprPortDomainEpType_Object((1,3,6,1,4,1,9,9,826,1,63,1,1,11),_CfprPortDomainEpType_Type())
cfprPortDomainEpType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortDomainEpType.setStatus(_A)
_CfprPortGroupTable_Object=MibTable
cfprPortGroupTable=_CfprPortGroupTable_Object((1,3,6,1,4,1,9,9,826,1,63,2))
if mibBuilder.loadTexts:cfprPortGroupTable.setStatus(_A)
_CfprPortGroupEntry_Object=MibTableRow
cfprPortGroupEntry=_CfprPortGroupEntry_Object((1,3,6,1,4,1,9,9,826,1,63,2,1))
cfprPortGroupEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprPortGroupEntry.setStatus(_A)
_CfprPortGroupInstanceId_Type=CfprManagedObjectId
_CfprPortGroupInstanceId_Object=MibTableColumn
cfprPortGroupInstanceId=_CfprPortGroupInstanceId_Object((1,3,6,1,4,1,9,9,826,1,63,2,1,1),_CfprPortGroupInstanceId_Type())
cfprPortGroupInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPortGroupInstanceId.setStatus(_A)
_CfprPortGroupDn_Type=CfprManagedObjectDn
_CfprPortGroupDn_Object=MibTableColumn
cfprPortGroupDn=_CfprPortGroupDn_Object((1,3,6,1,4,1,9,9,826,1,63,2,1,2),_CfprPortGroupDn_Type())
cfprPortGroupDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortGroupDn.setStatus(_A)
_CfprPortGroupRn_Type=SnmpAdminString
_CfprPortGroupRn_Object=MibTableColumn
cfprPortGroupRn=_CfprPortGroupRn_Object((1,3,6,1,4,1,9,9,826,1,63,2,1,3),_CfprPortGroupRn_Type())
cfprPortGroupRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortGroupRn.setStatus(_A)
_CfprPortGroupLocale_Type=CfprNetworkLocale
_CfprPortGroupLocale_Object=MibTableColumn
cfprPortGroupLocale=_CfprPortGroupLocale_Object((1,3,6,1,4,1,9,9,826,1,63,2,1,4),_CfprPortGroupLocale_Type())
cfprPortGroupLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortGroupLocale.setStatus(_A)
_CfprPortGroupName_Type=SnmpAdminString
_CfprPortGroupName_Object=MibTableColumn
cfprPortGroupName=_CfprPortGroupName_Object((1,3,6,1,4,1,9,9,826,1,63,2,1,5),_CfprPortGroupName_Type())
cfprPortGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortGroupName.setStatus(_A)
_CfprPortGroupTransport_Type=CfprNetworkTransport
_CfprPortGroupTransport_Object=MibTableColumn
cfprPortGroupTransport=_CfprPortGroupTransport_Object((1,3,6,1,4,1,9,9,826,1,63,2,1,6),_CfprPortGroupTransport_Type())
cfprPortGroupTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortGroupTransport.setStatus(_A)
_CfprPortGroupType_Type=CfprPortGroupType
_CfprPortGroupType_Object=MibTableColumn
cfprPortGroupType=_CfprPortGroupType_Object((1,3,6,1,4,1,9,9,826,1,63,2,1,7),_CfprPortGroupType_Type())
cfprPortGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortGroupType.setStatus(_A)
_CfprPortPIoFsmTable_Object=MibTable
cfprPortPIoFsmTable=_CfprPortPIoFsmTable_Object((1,3,6,1,4,1,9,9,826,1,63,3))
if mibBuilder.loadTexts:cfprPortPIoFsmTable.setStatus(_A)
_CfprPortPIoFsmEntry_Object=MibTableRow
cfprPortPIoFsmEntry=_CfprPortPIoFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,63,3,1))
cfprPortPIoFsmEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprPortPIoFsmEntry.setStatus(_A)
_CfprPortPIoFsmInstanceId_Type=CfprManagedObjectId
_CfprPortPIoFsmInstanceId_Object=MibTableColumn
cfprPortPIoFsmInstanceId=_CfprPortPIoFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,1),_CfprPortPIoFsmInstanceId_Type())
cfprPortPIoFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPortPIoFsmInstanceId.setStatus(_A)
_CfprPortPIoFsmDn_Type=CfprManagedObjectDn
_CfprPortPIoFsmDn_Object=MibTableColumn
cfprPortPIoFsmDn=_CfprPortPIoFsmDn_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,2),_CfprPortPIoFsmDn_Type())
cfprPortPIoFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmDn.setStatus(_A)
_CfprPortPIoFsmRn_Type=SnmpAdminString
_CfprPortPIoFsmRn_Object=MibTableColumn
cfprPortPIoFsmRn=_CfprPortPIoFsmRn_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,3),_CfprPortPIoFsmRn_Type())
cfprPortPIoFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmRn.setStatus(_A)
_CfprPortPIoFsmCompletionTime_Type=DateAndTime
_CfprPortPIoFsmCompletionTime_Object=MibTableColumn
cfprPortPIoFsmCompletionTime=_CfprPortPIoFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,4),_CfprPortPIoFsmCompletionTime_Type())
cfprPortPIoFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmCompletionTime.setStatus(_A)
_CfprPortPIoFsmCurrentFsm_Type=CfprPortPIoFsmCurrentFsm
_CfprPortPIoFsmCurrentFsm_Object=MibTableColumn
cfprPortPIoFsmCurrentFsm=_CfprPortPIoFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,5),_CfprPortPIoFsmCurrentFsm_Type())
cfprPortPIoFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmCurrentFsm.setStatus(_A)
_CfprPortPIoFsmDescr_Type=SnmpAdminString
_CfprPortPIoFsmDescr_Object=MibTableColumn
cfprPortPIoFsmDescr=_CfprPortPIoFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,6),_CfprPortPIoFsmDescr_Type())
cfprPortPIoFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmDescr.setStatus(_A)
_CfprPortPIoFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprPortPIoFsmFsmStatus_Object=MibTableColumn
cfprPortPIoFsmFsmStatus=_CfprPortPIoFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,7),_CfprPortPIoFsmFsmStatus_Type())
cfprPortPIoFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmFsmStatus.setStatus(_A)
_CfprPortPIoFsmProgress_Type=Gauge32
_CfprPortPIoFsmProgress_Object=MibTableColumn
cfprPortPIoFsmProgress=_CfprPortPIoFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,8),_CfprPortPIoFsmProgress_Type())
cfprPortPIoFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmProgress.setStatus(_A)
_CfprPortPIoFsmRmtErrCode_Type=Gauge32
_CfprPortPIoFsmRmtErrCode_Object=MibTableColumn
cfprPortPIoFsmRmtErrCode=_CfprPortPIoFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,9),_CfprPortPIoFsmRmtErrCode_Type())
cfprPortPIoFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmRmtErrCode.setStatus(_A)
_CfprPortPIoFsmRmtErrDescr_Type=SnmpAdminString
_CfprPortPIoFsmRmtErrDescr_Object=MibTableColumn
cfprPortPIoFsmRmtErrDescr=_CfprPortPIoFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,10),_CfprPortPIoFsmRmtErrDescr_Type())
cfprPortPIoFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmRmtErrDescr.setStatus(_A)
_CfprPortPIoFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprPortPIoFsmRmtRslt_Object=MibTableColumn
cfprPortPIoFsmRmtRslt=_CfprPortPIoFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,63,3,1,11),_CfprPortPIoFsmRmtRslt_Type())
cfprPortPIoFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmRmtRslt.setStatus(_A)
_CfprPortPIoFsmStageTable_Object=MibTable
cfprPortPIoFsmStageTable=_CfprPortPIoFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,63,4))
if mibBuilder.loadTexts:cfprPortPIoFsmStageTable.setStatus(_A)
_CfprPortPIoFsmStageEntry_Object=MibTableRow
cfprPortPIoFsmStageEntry=_CfprPortPIoFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,63,4,1))
cfprPortPIoFsmStageEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprPortPIoFsmStageEntry.setStatus(_A)
_CfprPortPIoFsmStageInstanceId_Type=CfprManagedObjectId
_CfprPortPIoFsmStageInstanceId_Object=MibTableColumn
cfprPortPIoFsmStageInstanceId=_CfprPortPIoFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,63,4,1,1),_CfprPortPIoFsmStageInstanceId_Type())
cfprPortPIoFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPortPIoFsmStageInstanceId.setStatus(_A)
_CfprPortPIoFsmStageDn_Type=CfprManagedObjectDn
_CfprPortPIoFsmStageDn_Object=MibTableColumn
cfprPortPIoFsmStageDn=_CfprPortPIoFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,63,4,1,2),_CfprPortPIoFsmStageDn_Type())
cfprPortPIoFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmStageDn.setStatus(_A)
_CfprPortPIoFsmStageRn_Type=SnmpAdminString
_CfprPortPIoFsmStageRn_Object=MibTableColumn
cfprPortPIoFsmStageRn=_CfprPortPIoFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,63,4,1,3),_CfprPortPIoFsmStageRn_Type())
cfprPortPIoFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmStageRn.setStatus(_A)
_CfprPortPIoFsmStageDescr_Type=SnmpAdminString
_CfprPortPIoFsmStageDescr_Object=MibTableColumn
cfprPortPIoFsmStageDescr=_CfprPortPIoFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,63,4,1,4),_CfprPortPIoFsmStageDescr_Type())
cfprPortPIoFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmStageDescr.setStatus(_A)
_CfprPortPIoFsmStageLastUpdateTime_Type=DateAndTime
_CfprPortPIoFsmStageLastUpdateTime_Object=MibTableColumn
cfprPortPIoFsmStageLastUpdateTime=_CfprPortPIoFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,63,4,1,5),_CfprPortPIoFsmStageLastUpdateTime_Type())
cfprPortPIoFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmStageLastUpdateTime.setStatus(_A)
_CfprPortPIoFsmStageName_Type=CfprPortPIoFsmStageName
_CfprPortPIoFsmStageName_Object=MibTableColumn
cfprPortPIoFsmStageName=_CfprPortPIoFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,63,4,1,6),_CfprPortPIoFsmStageName_Type())
cfprPortPIoFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmStageName.setStatus(_A)
_CfprPortPIoFsmStageOrder_Type=Gauge32
_CfprPortPIoFsmStageOrder_Object=MibTableColumn
cfprPortPIoFsmStageOrder=_CfprPortPIoFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,63,4,1,7),_CfprPortPIoFsmStageOrder_Type())
cfprPortPIoFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmStageOrder.setStatus(_A)
_CfprPortPIoFsmStageRetry_Type=Gauge32
_CfprPortPIoFsmStageRetry_Object=MibTableColumn
cfprPortPIoFsmStageRetry=_CfprPortPIoFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,63,4,1,8),_CfprPortPIoFsmStageRetry_Type())
cfprPortPIoFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmStageRetry.setStatus(_A)
_CfprPortPIoFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprPortPIoFsmStageStageStatus_Object=MibTableColumn
cfprPortPIoFsmStageStageStatus=_CfprPortPIoFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,63,4,1,9),_CfprPortPIoFsmStageStageStatus_Type())
cfprPortPIoFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmStageStageStatus.setStatus(_A)
_CfprPortPIoFsmTaskTable_Object=MibTable
cfprPortPIoFsmTaskTable=_CfprPortPIoFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,63,5))
if mibBuilder.loadTexts:cfprPortPIoFsmTaskTable.setStatus(_A)
_CfprPortPIoFsmTaskEntry_Object=MibTableRow
cfprPortPIoFsmTaskEntry=_CfprPortPIoFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,63,5,1))
cfprPortPIoFsmTaskEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprPortPIoFsmTaskEntry.setStatus(_A)
_CfprPortPIoFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprPortPIoFsmTaskInstanceId_Object=MibTableColumn
cfprPortPIoFsmTaskInstanceId=_CfprPortPIoFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,63,5,1,1),_CfprPortPIoFsmTaskInstanceId_Type())
cfprPortPIoFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPortPIoFsmTaskInstanceId.setStatus(_A)
_CfprPortPIoFsmTaskDn_Type=CfprManagedObjectDn
_CfprPortPIoFsmTaskDn_Object=MibTableColumn
cfprPortPIoFsmTaskDn=_CfprPortPIoFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,63,5,1,2),_CfprPortPIoFsmTaskDn_Type())
cfprPortPIoFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmTaskDn.setStatus(_A)
_CfprPortPIoFsmTaskRn_Type=SnmpAdminString
_CfprPortPIoFsmTaskRn_Object=MibTableColumn
cfprPortPIoFsmTaskRn=_CfprPortPIoFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,63,5,1,3),_CfprPortPIoFsmTaskRn_Type())
cfprPortPIoFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmTaskRn.setStatus(_A)
_CfprPortPIoFsmTaskCompletion_Type=CfprFsmCompletion
_CfprPortPIoFsmTaskCompletion_Object=MibTableColumn
cfprPortPIoFsmTaskCompletion=_CfprPortPIoFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,63,5,1,4),_CfprPortPIoFsmTaskCompletion_Type())
cfprPortPIoFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmTaskCompletion.setStatus(_A)
_CfprPortPIoFsmTaskFlags_Type=CfprFsmFlags
_CfprPortPIoFsmTaskFlags_Object=MibTableColumn
cfprPortPIoFsmTaskFlags=_CfprPortPIoFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,63,5,1,5),_CfprPortPIoFsmTaskFlags_Type())
cfprPortPIoFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmTaskFlags.setStatus(_A)
_CfprPortPIoFsmTaskItem_Type=CfprPortPIoFsmTaskItem
_CfprPortPIoFsmTaskItem_Object=MibTableColumn
cfprPortPIoFsmTaskItem=_CfprPortPIoFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,63,5,1,6),_CfprPortPIoFsmTaskItem_Type())
cfprPortPIoFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmTaskItem.setStatus(_A)
_CfprPortPIoFsmTaskSeqId_Type=Gauge32
_CfprPortPIoFsmTaskSeqId_Object=MibTableColumn
cfprPortPIoFsmTaskSeqId=_CfprPortPIoFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,63,5,1,7),_CfprPortPIoFsmTaskSeqId_Type())
cfprPortPIoFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortPIoFsmTaskSeqId.setStatus(_A)
_CfprPortSubGroupTable_Object=MibTable
cfprPortSubGroupTable=_CfprPortSubGroupTable_Object((1,3,6,1,4,1,9,9,826,1,63,6))
if mibBuilder.loadTexts:cfprPortSubGroupTable.setStatus(_A)
_CfprPortSubGroupEntry_Object=MibTableRow
cfprPortSubGroupEntry=_CfprPortSubGroupEntry_Object((1,3,6,1,4,1,9,9,826,1,63,6,1))
cfprPortSubGroupEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprPortSubGroupEntry.setStatus(_A)
_CfprPortSubGroupInstanceId_Type=CfprManagedObjectId
_CfprPortSubGroupInstanceId_Object=MibTableColumn
cfprPortSubGroupInstanceId=_CfprPortSubGroupInstanceId_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,1),_CfprPortSubGroupInstanceId_Type())
cfprPortSubGroupInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPortSubGroupInstanceId.setStatus(_A)
_CfprPortSubGroupDn_Type=CfprManagedObjectDn
_CfprPortSubGroupDn_Object=MibTableColumn
cfprPortSubGroupDn=_CfprPortSubGroupDn_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,2),_CfprPortSubGroupDn_Type())
cfprPortSubGroupDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupDn.setStatus(_A)
_CfprPortSubGroupRn_Type=SnmpAdminString
_CfprPortSubGroupRn_Object=MibTableColumn
cfprPortSubGroupRn=_CfprPortSubGroupRn_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,3),_CfprPortSubGroupRn_Type())
cfprPortSubGroupRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupRn.setStatus(_A)
_CfprPortSubGroupAggrPortId_Type=Gauge32
_CfprPortSubGroupAggrPortId_Object=MibTableColumn
cfprPortSubGroupAggrPortId=_CfprPortSubGroupAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,4),_CfprPortSubGroupAggrPortId_Type())
cfprPortSubGroupAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupAggrPortId.setStatus(_A)
_CfprPortSubGroupConfigState_Type=CfprPortSubGroupConfigState
_CfprPortSubGroupConfigState_Object=MibTableColumn
cfprPortSubGroupConfigState=_CfprPortSubGroupConfigState_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,5),_CfprPortSubGroupConfigState_Type())
cfprPortSubGroupConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupConfigState.setStatus(_A)
_CfprPortSubGroupLicGP_Type=Unsigned64
_CfprPortSubGroupLicGP_Object=MibTableColumn
cfprPortSubGroupLicGP=_CfprPortSubGroupLicGP_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,6),_CfprPortSubGroupLicGP_Type())
cfprPortSubGroupLicGP.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupLicGP.setStatus(_A)
_CfprPortSubGroupLicState_Type=CfprLicenseState
_CfprPortSubGroupLicState_Object=MibTableColumn
cfprPortSubGroupLicState=_CfprPortSubGroupLicState_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,7),_CfprPortSubGroupLicState_Type())
cfprPortSubGroupLicState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupLicState.setStatus(_A)
_CfprPortSubGroupLocale_Type=CfprNetworkLocale
_CfprPortSubGroupLocale_Object=MibTableColumn
cfprPortSubGroupLocale=_CfprPortSubGroupLocale_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,8),_CfprPortSubGroupLocale_Type())
cfprPortSubGroupLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupLocale.setStatus(_A)
_CfprPortSubGroupName_Type=SnmpAdminString
_CfprPortSubGroupName_Object=MibTableColumn
cfprPortSubGroupName=_CfprPortSubGroupName_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,9),_CfprPortSubGroupName_Type())
cfprPortSubGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupName.setStatus(_A)
_CfprPortSubGroupSlotId_Type=CfprPortSubGroupSlotId
_CfprPortSubGroupSlotId_Object=MibTableColumn
cfprPortSubGroupSlotId=_CfprPortSubGroupSlotId_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,10),_CfprPortSubGroupSlotId_Type())
cfprPortSubGroupSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupSlotId.setStatus(_A)
_CfprPortSubGroupSwitchId_Type=CfprNetworkSwitchId
_CfprPortSubGroupSwitchId_Object=MibTableColumn
cfprPortSubGroupSwitchId=_CfprPortSubGroupSwitchId_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,11),_CfprPortSubGroupSwitchId_Type())
cfprPortSubGroupSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupSwitchId.setStatus(_A)
_CfprPortSubGroupTransport_Type=CfprNetworkTransport
_CfprPortSubGroupTransport_Object=MibTableColumn
cfprPortSubGroupTransport=_CfprPortSubGroupTransport_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,12),_CfprPortSubGroupTransport_Type())
cfprPortSubGroupTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupTransport.setStatus(_A)
_CfprPortSubGroupType_Type=CfprNetworkConnectionType
_CfprPortSubGroupType_Object=MibTableColumn
cfprPortSubGroupType=_CfprPortSubGroupType_Object((1,3,6,1,4,1,9,9,826,1,63,6,1,13),_CfprPortSubGroupType_Type())
cfprPortSubGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortSubGroupType.setStatus(_A)
_CfprPortTrustModeTable_Object=MibTable
cfprPortTrustModeTable=_CfprPortTrustModeTable_Object((1,3,6,1,4,1,9,9,826,1,63,7))
if mibBuilder.loadTexts:cfprPortTrustModeTable.setStatus(_A)
_CfprPortTrustModeEntry_Object=MibTableRow
cfprPortTrustModeEntry=_CfprPortTrustModeEntry_Object((1,3,6,1,4,1,9,9,826,1,63,7,1))
cfprPortTrustModeEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprPortTrustModeEntry.setStatus(_A)
_CfprPortTrustModeInstanceId_Type=CfprManagedObjectId
_CfprPortTrustModeInstanceId_Object=MibTableColumn
cfprPortTrustModeInstanceId=_CfprPortTrustModeInstanceId_Object((1,3,6,1,4,1,9,9,826,1,63,7,1,1),_CfprPortTrustModeInstanceId_Type())
cfprPortTrustModeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPortTrustModeInstanceId.setStatus(_A)
_CfprPortTrustModeDn_Type=CfprManagedObjectDn
_CfprPortTrustModeDn_Object=MibTableColumn
cfprPortTrustModeDn=_CfprPortTrustModeDn_Object((1,3,6,1,4,1,9,9,826,1,63,7,1,2),_CfprPortTrustModeDn_Type())
cfprPortTrustModeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortTrustModeDn.setStatus(_A)
_CfprPortTrustModeRn_Type=SnmpAdminString
_CfprPortTrustModeRn_Object=MibTableColumn
cfprPortTrustModeRn=_CfprPortTrustModeRn_Object((1,3,6,1,4,1,9,9,826,1,63,7,1,3),_CfprPortTrustModeRn_Type())
cfprPortTrustModeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortTrustModeRn.setStatus(_A)
_CfprPortTrustModeState_Type=CfprPortTrust
_CfprPortTrustModeState_Object=MibTableColumn
cfprPortTrustModeState=_CfprPortTrustModeState_Object((1,3,6,1,4,1,9,9,826,1,63,7,1,4),_CfprPortTrustModeState_Type())
cfprPortTrustModeState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPortTrustModeState.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprPortObjects':cfprPortObjects,'cfprPortDomainEpTable':cfprPortDomainEpTable,'cfprPortDomainEpEntry':cfprPortDomainEpEntry,_E:cfprPortDomainEpInstanceId,'cfprPortDomainEpDn':cfprPortDomainEpDn,'cfprPortDomainEpRn':cfprPortDomainEpRn,'cfprPortDomainEpEpDn':cfprPortDomainEpEpDn,'cfprPortDomainEpIfRole':cfprPortDomainEpIfRole,'cfprPortDomainEpIfType':cfprPortDomainEpIfType,'cfprPortDomainEpLocale':cfprPortDomainEpLocale,'cfprPortDomainEpName':cfprPortDomainEpName,'cfprPortDomainEpPeerDn':cfprPortDomainEpPeerDn,'cfprPortDomainEpTransport':cfprPortDomainEpTransport,'cfprPortDomainEpType':cfprPortDomainEpType,'cfprPortGroupTable':cfprPortGroupTable,'cfprPortGroupEntry':cfprPortGroupEntry,_F:cfprPortGroupInstanceId,'cfprPortGroupDn':cfprPortGroupDn,'cfprPortGroupRn':cfprPortGroupRn,'cfprPortGroupLocale':cfprPortGroupLocale,'cfprPortGroupName':cfprPortGroupName,'cfprPortGroupTransport':cfprPortGroupTransport,'cfprPortGroupType':cfprPortGroupType,'cfprPortPIoFsmTable':cfprPortPIoFsmTable,'cfprPortPIoFsmEntry':cfprPortPIoFsmEntry,_G:cfprPortPIoFsmInstanceId,'cfprPortPIoFsmDn':cfprPortPIoFsmDn,'cfprPortPIoFsmRn':cfprPortPIoFsmRn,'cfprPortPIoFsmCompletionTime':cfprPortPIoFsmCompletionTime,'cfprPortPIoFsmCurrentFsm':cfprPortPIoFsmCurrentFsm,'cfprPortPIoFsmDescr':cfprPortPIoFsmDescr,'cfprPortPIoFsmFsmStatus':cfprPortPIoFsmFsmStatus,'cfprPortPIoFsmProgress':cfprPortPIoFsmProgress,'cfprPortPIoFsmRmtErrCode':cfprPortPIoFsmRmtErrCode,'cfprPortPIoFsmRmtErrDescr':cfprPortPIoFsmRmtErrDescr,'cfprPortPIoFsmRmtRslt':cfprPortPIoFsmRmtRslt,'cfprPortPIoFsmStageTable':cfprPortPIoFsmStageTable,'cfprPortPIoFsmStageEntry':cfprPortPIoFsmStageEntry,_H:cfprPortPIoFsmStageInstanceId,'cfprPortPIoFsmStageDn':cfprPortPIoFsmStageDn,'cfprPortPIoFsmStageRn':cfprPortPIoFsmStageRn,'cfprPortPIoFsmStageDescr':cfprPortPIoFsmStageDescr,'cfprPortPIoFsmStageLastUpdateTime':cfprPortPIoFsmStageLastUpdateTime,'cfprPortPIoFsmStageName':cfprPortPIoFsmStageName,'cfprPortPIoFsmStageOrder':cfprPortPIoFsmStageOrder,'cfprPortPIoFsmStageRetry':cfprPortPIoFsmStageRetry,'cfprPortPIoFsmStageStageStatus':cfprPortPIoFsmStageStageStatus,'cfprPortPIoFsmTaskTable':cfprPortPIoFsmTaskTable,'cfprPortPIoFsmTaskEntry':cfprPortPIoFsmTaskEntry,_I:cfprPortPIoFsmTaskInstanceId,'cfprPortPIoFsmTaskDn':cfprPortPIoFsmTaskDn,'cfprPortPIoFsmTaskRn':cfprPortPIoFsmTaskRn,'cfprPortPIoFsmTaskCompletion':cfprPortPIoFsmTaskCompletion,'cfprPortPIoFsmTaskFlags':cfprPortPIoFsmTaskFlags,'cfprPortPIoFsmTaskItem':cfprPortPIoFsmTaskItem,'cfprPortPIoFsmTaskSeqId':cfprPortPIoFsmTaskSeqId,'cfprPortSubGroupTable':cfprPortSubGroupTable,'cfprPortSubGroupEntry':cfprPortSubGroupEntry,_J:cfprPortSubGroupInstanceId,'cfprPortSubGroupDn':cfprPortSubGroupDn,'cfprPortSubGroupRn':cfprPortSubGroupRn,'cfprPortSubGroupAggrPortId':cfprPortSubGroupAggrPortId,'cfprPortSubGroupConfigState':cfprPortSubGroupConfigState,'cfprPortSubGroupLicGP':cfprPortSubGroupLicGP,'cfprPortSubGroupLicState':cfprPortSubGroupLicState,'cfprPortSubGroupLocale':cfprPortSubGroupLocale,'cfprPortSubGroupName':cfprPortSubGroupName,'cfprPortSubGroupSlotId':cfprPortSubGroupSlotId,'cfprPortSubGroupSwitchId':cfprPortSubGroupSwitchId,'cfprPortSubGroupTransport':cfprPortSubGroupTransport,'cfprPortSubGroupType':cfprPortSubGroupType,'cfprPortTrustModeTable':cfprPortTrustModeTable,'cfprPortTrustModeEntry':cfprPortTrustModeEntry,_K:cfprPortTrustModeInstanceId,'cfprPortTrustModeDn':cfprPortTrustModeDn,'cfprPortTrustModeRn':cfprPortTrustModeRn,'cfprPortTrustModeState':cfprPortTrustModeState})