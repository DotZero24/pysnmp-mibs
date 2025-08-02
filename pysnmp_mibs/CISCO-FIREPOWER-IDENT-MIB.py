_P='cfprIdentSysInfoInstanceId'
_O='cfprIdentRequestEpInstanceId'
_N='cfprIdentMetaVerseInstanceId'
_M='cfprIdentMetaSystemFsmTaskInstanceId'
_L='cfprIdentMetaSystemFsmStageInstanceId'
_K='cfprIdentMetaSystemFsmInstanceId'
_J='cfprIdentMetaSystemInstanceId'
_I='cfprIdentIdentRequestFsmTaskInstanceId'
_H='cfprIdentIdentRequestFsmStageInstanceId'
_G='cfprIdentIdentRequestFsmInstanceId'
_F='cfprIdentIdentRequestInstanceId'
_E='cfprIdentIdentCtxInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-IDENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprConditionRemoteInvRslt,CfprFsmCompletion,CfprFsmFlags,CfprFsmFsmStageStatus,CfprIdentConsType,CfprIdentIdDefinedInIdm,CfprIdentIdentReqIntent,CfprIdentIdentRequestFsmCurrentFsm,CfprIdentIdentRequestFsmStageName,CfprIdentIdentRequestFsmTaskItem,CfprIdentIdentType,CfprIdentMetaSystemFsmCurrentFsm,CfprIdentMetaSystemFsmStageName,CfprIdentMetaSystemFsmTaskItem,CfprIdentRetStatus=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprConditionRemoteInvRslt','CfprFsmCompletion','CfprFsmFlags','CfprFsmFsmStageStatus','CfprIdentConsType','CfprIdentIdDefinedInIdm','CfprIdentIdentReqIntent','CfprIdentIdentRequestFsmCurrentFsm','CfprIdentIdentRequestFsmStageName','CfprIdentIdentRequestFsmTaskItem','CfprIdentIdentType','CfprIdentMetaSystemFsmCurrentFsm','CfprIdentMetaSystemFsmStageName','CfprIdentMetaSystemFsmTaskItem','CfprIdentRetStatus')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprIdentObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,36))
_CfprIdentIdentCtxTable_Object=MibTable
cfprIdentIdentCtxTable=_CfprIdentIdentCtxTable_Object((1,3,6,1,4,1,9,9,826,1,36,1))
if mibBuilder.loadTexts:cfprIdentIdentCtxTable.setStatus(_A)
_CfprIdentIdentCtxEntry_Object=MibTableRow
cfprIdentIdentCtxEntry=_CfprIdentIdentCtxEntry_Object((1,3,6,1,4,1,9,9,826,1,36,1,1))
cfprIdentIdentCtxEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprIdentIdentCtxEntry.setStatus(_A)
_CfprIdentIdentCtxInstanceId_Type=CfprManagedObjectId
_CfprIdentIdentCtxInstanceId_Object=MibTableColumn
cfprIdentIdentCtxInstanceId=_CfprIdentIdentCtxInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,1),_CfprIdentIdentCtxInstanceId_Type())
cfprIdentIdentCtxInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentIdentCtxInstanceId.setStatus(_A)
_CfprIdentIdentCtxDn_Type=CfprManagedObjectDn
_CfprIdentIdentCtxDn_Object=MibTableColumn
cfprIdentIdentCtxDn=_CfprIdentIdentCtxDn_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,2),_CfprIdentIdentCtxDn_Type())
cfprIdentIdentCtxDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxDn.setStatus(_A)
_CfprIdentIdentCtxRn_Type=SnmpAdminString
_CfprIdentIdentCtxRn_Object=MibTableColumn
cfprIdentIdentCtxRn=_CfprIdentIdentCtxRn_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,3),_CfprIdentIdentCtxRn_Type())
cfprIdentIdentCtxRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxRn.setStatus(_A)
_CfprIdentIdentCtxAssigned_Type=SnmpAdminString
_CfprIdentIdentCtxAssigned_Object=MibTableColumn
cfprIdentIdentCtxAssigned=_CfprIdentIdentCtxAssigned_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,4),_CfprIdentIdentCtxAssigned_Type())
cfprIdentIdentCtxAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxAssigned.setStatus(_A)
_CfprIdentIdentCtxConsDn_Type=SnmpAdminString
_CfprIdentIdentCtxConsDn_Object=MibTableColumn
cfprIdentIdentCtxConsDn=_CfprIdentIdentCtxConsDn_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,5),_CfprIdentIdentCtxConsDn_Type())
cfprIdentIdentCtxConsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxConsDn.setStatus(_A)
_CfprIdentIdentCtxConsType_Type=CfprIdentConsType
_CfprIdentIdentCtxConsType_Object=MibTableColumn
cfprIdentIdentCtxConsType=_CfprIdentIdentCtxConsType_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,6),_CfprIdentIdentCtxConsType_Type())
cfprIdentIdentCtxConsType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxConsType.setStatus(_A)
_CfprIdentIdentCtxDefinedInIdm_Type=CfprIdentIdDefinedInIdm
_CfprIdentIdentCtxDefinedInIdm_Object=MibTableColumn
cfprIdentIdentCtxDefinedInIdm=_CfprIdentIdentCtxDefinedInIdm_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,7),_CfprIdentIdentCtxDefinedInIdm_Type())
cfprIdentIdentCtxDefinedInIdm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxDefinedInIdm.setStatus(_A)
_CfprIdentIdentCtxGlobalAssignedCnt_Type=Gauge32
_CfprIdentIdentCtxGlobalAssignedCnt_Object=MibTableColumn
cfprIdentIdentCtxGlobalAssignedCnt=_CfprIdentIdentCtxGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,8),_CfprIdentIdentCtxGlobalAssignedCnt_Type())
cfprIdentIdentCtxGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxGlobalAssignedCnt.setStatus(_A)
_CfprIdentIdentCtxGlobalDefinedCnt_Type=Gauge32
_CfprIdentIdentCtxGlobalDefinedCnt_Object=MibTableColumn
cfprIdentIdentCtxGlobalDefinedCnt=_CfprIdentIdentCtxGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,9),_CfprIdentIdentCtxGlobalDefinedCnt_Type())
cfprIdentIdentCtxGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxGlobalDefinedCnt.setStatus(_A)
_CfprIdentIdentCtxIdentPoolName_Type=SnmpAdminString
_CfprIdentIdentCtxIdentPoolName_Object=MibTableColumn
cfprIdentIdentCtxIdentPoolName=_CfprIdentIdentCtxIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,10),_CfprIdentIdentCtxIdentPoolName_Type())
cfprIdentIdentCtxIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxIdentPoolName.setStatus(_A)
_CfprIdentIdentCtxIdentType_Type=CfprIdentIdentType
_CfprIdentIdentCtxIdentType_Object=MibTableColumn
cfprIdentIdentCtxIdentType=_CfprIdentIdentCtxIdentType_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,11),_CfprIdentIdentCtxIdentType_Type())
cfprIdentIdentCtxIdentType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxIdentType.setStatus(_A)
_CfprIdentIdentCtxIntent_Type=CfprIdentIdentReqIntent
_CfprIdentIdentCtxIntent_Object=MibTableColumn
cfprIdentIdentCtxIntent=_CfprIdentIdentCtxIntent_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,12),_CfprIdentIdentCtxIntent_Type())
cfprIdentIdentCtxIntent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxIntent.setStatus(_A)
_CfprIdentIdentCtxIsAssignedLocally_Type=TruthValue
_CfprIdentIdentCtxIsAssignedLocally_Object=MibTableColumn
cfprIdentIdentCtxIsAssignedLocally=_CfprIdentIdentCtxIsAssignedLocally_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,13),_CfprIdentIdentCtxIsAssignedLocally_Type())
cfprIdentIdentCtxIsAssignedLocally.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxIsAssignedLocally.setStatus(_A)
_CfprIdentIdentCtxPoolDn_Type=SnmpAdminString
_CfprIdentIdentCtxPoolDn_Object=MibTableColumn
cfprIdentIdentCtxPoolDn=_CfprIdentIdentCtxPoolDn_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,14),_CfprIdentIdentCtxPoolDn_Type())
cfprIdentIdentCtxPoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxPoolDn.setStatus(_A)
_CfprIdentIdentCtxPoolOrgDn_Type=SnmpAdminString
_CfprIdentIdentCtxPoolOrgDn_Object=MibTableColumn
cfprIdentIdentCtxPoolOrgDn=_CfprIdentIdentCtxPoolOrgDn_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,15),_CfprIdentIdentCtxPoolOrgDn_Type())
cfprIdentIdentCtxPoolOrgDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxPoolOrgDn.setStatus(_A)
_CfprIdentIdentCtxPooledId_Type=Gauge32
_CfprIdentIdentCtxPooledId_Object=MibTableColumn
cfprIdentIdentCtxPooledId=_CfprIdentIdentCtxPooledId_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,16),_CfprIdentIdentCtxPooledId_Type())
cfprIdentIdentCtxPooledId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxPooledId.setStatus(_A)
_CfprIdentIdentCtxRetStatus_Type=CfprIdentRetStatus
_CfprIdentIdentCtxRetStatus_Object=MibTableColumn
cfprIdentIdentCtxRetStatus=_CfprIdentIdentCtxRetStatus_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,17),_CfprIdentIdentCtxRetStatus_Type())
cfprIdentIdentCtxRetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxRetStatus.setStatus(_A)
_CfprIdentIdentCtxSeqNum_Type=Gauge32
_CfprIdentIdentCtxSeqNum_Object=MibTableColumn
cfprIdentIdentCtxSeqNum=_CfprIdentIdentCtxSeqNum_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,18),_CfprIdentIdentCtxSeqNum_Type())
cfprIdentIdentCtxSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxSeqNum.setStatus(_A)
_CfprIdentIdentCtxSupplId1_Type=SnmpAdminString
_CfprIdentIdentCtxSupplId1_Object=MibTableColumn
cfprIdentIdentCtxSupplId1=_CfprIdentIdentCtxSupplId1_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,19),_CfprIdentIdentCtxSupplId1_Type())
cfprIdentIdentCtxSupplId1.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxSupplId1.setStatus(_A)
_CfprIdentIdentCtxSupplId2_Type=SnmpAdminString
_CfprIdentIdentCtxSupplId2_Object=MibTableColumn
cfprIdentIdentCtxSupplId2=_CfprIdentIdentCtxSupplId2_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,20),_CfprIdentIdentCtxSupplId2_Type())
cfprIdentIdentCtxSupplId2.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxSupplId2.setStatus(_A)
_CfprIdentIdentCtxSupplId3_Type=SnmpAdminString
_CfprIdentIdentCtxSupplId3_Object=MibTableColumn
cfprIdentIdentCtxSupplId3=_CfprIdentIdentCtxSupplId3_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,21),_CfprIdentIdentCtxSupplId3_Type())
cfprIdentIdentCtxSupplId3.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxSupplId3.setStatus(_A)
_CfprIdentIdentCtxSupplId4_Type=SnmpAdminString
_CfprIdentIdentCtxSupplId4_Object=MibTableColumn
cfprIdentIdentCtxSupplId4=_CfprIdentIdentCtxSupplId4_Object((1,3,6,1,4,1,9,9,826,1,36,1,1,22),_CfprIdentIdentCtxSupplId4_Type())
cfprIdentIdentCtxSupplId4.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentCtxSupplId4.setStatus(_A)
_CfprIdentIdentRequestTable_Object=MibTable
cfprIdentIdentRequestTable=_CfprIdentIdentRequestTable_Object((1,3,6,1,4,1,9,9,826,1,36,2))
if mibBuilder.loadTexts:cfprIdentIdentRequestTable.setStatus(_A)
_CfprIdentIdentRequestEntry_Object=MibTableRow
cfprIdentIdentRequestEntry=_CfprIdentIdentRequestEntry_Object((1,3,6,1,4,1,9,9,826,1,36,2,1))
cfprIdentIdentRequestEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprIdentIdentRequestEntry.setStatus(_A)
_CfprIdentIdentRequestInstanceId_Type=CfprManagedObjectId
_CfprIdentIdentRequestInstanceId_Object=MibTableColumn
cfprIdentIdentRequestInstanceId=_CfprIdentIdentRequestInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,1),_CfprIdentIdentRequestInstanceId_Type())
cfprIdentIdentRequestInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentIdentRequestInstanceId.setStatus(_A)
_CfprIdentIdentRequestDn_Type=CfprManagedObjectDn
_CfprIdentIdentRequestDn_Object=MibTableColumn
cfprIdentIdentRequestDn=_CfprIdentIdentRequestDn_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,2),_CfprIdentIdentRequestDn_Type())
cfprIdentIdentRequestDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestDn.setStatus(_A)
_CfprIdentIdentRequestRn_Type=SnmpAdminString
_CfprIdentIdentRequestRn_Object=MibTableColumn
cfprIdentIdentRequestRn=_CfprIdentIdentRequestRn_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,3),_CfprIdentIdentRequestRn_Type())
cfprIdentIdentRequestRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestRn.setStatus(_A)
_CfprIdentIdentRequestEpDn_Type=SnmpAdminString
_CfprIdentIdentRequestEpDn_Object=MibTableColumn
cfprIdentIdentRequestEpDn=_CfprIdentIdentRequestEpDn_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,4),_CfprIdentIdentRequestEpDn_Type())
cfprIdentIdentRequestEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestEpDn.setStatus(_A)
_CfprIdentIdentRequestFsmDescr_Type=SnmpAdminString
_CfprIdentIdentRequestFsmDescr_Object=MibTableColumn
cfprIdentIdentRequestFsmDescr=_CfprIdentIdentRequestFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,5),_CfprIdentIdentRequestFsmDescr_Type())
cfprIdentIdentRequestFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmDescr.setStatus(_A)
_CfprIdentIdentRequestFsmPrev_Type=SnmpAdminString
_CfprIdentIdentRequestFsmPrev_Object=MibTableColumn
cfprIdentIdentRequestFsmPrev=_CfprIdentIdentRequestFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,6),_CfprIdentIdentRequestFsmPrev_Type())
cfprIdentIdentRequestFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmPrev.setStatus(_A)
_CfprIdentIdentRequestFsmProgr_Type=Gauge32
_CfprIdentIdentRequestFsmProgr_Object=MibTableColumn
cfprIdentIdentRequestFsmProgr=_CfprIdentIdentRequestFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,7),_CfprIdentIdentRequestFsmProgr_Type())
cfprIdentIdentRequestFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmProgr.setStatus(_A)
_CfprIdentIdentRequestFsmRmtInvErrCode_Type=Gauge32
_CfprIdentIdentRequestFsmRmtInvErrCode_Object=MibTableColumn
cfprIdentIdentRequestFsmRmtInvErrCode=_CfprIdentIdentRequestFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,8),_CfprIdentIdentRequestFsmRmtInvErrCode_Type())
cfprIdentIdentRequestFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmRmtInvErrCode.setStatus(_A)
_CfprIdentIdentRequestFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprIdentIdentRequestFsmRmtInvErrDescr_Object=MibTableColumn
cfprIdentIdentRequestFsmRmtInvErrDescr=_CfprIdentIdentRequestFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,9),_CfprIdentIdentRequestFsmRmtInvErrDescr_Type())
cfprIdentIdentRequestFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmRmtInvErrDescr.setStatus(_A)
_CfprIdentIdentRequestFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprIdentIdentRequestFsmRmtInvRslt_Object=MibTableColumn
cfprIdentIdentRequestFsmRmtInvRslt=_CfprIdentIdentRequestFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,10),_CfprIdentIdentRequestFsmRmtInvRslt_Type())
cfprIdentIdentRequestFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmRmtInvRslt.setStatus(_A)
_CfprIdentIdentRequestFsmStageDescr_Type=SnmpAdminString
_CfprIdentIdentRequestFsmStageDescr_Object=MibTableColumn
cfprIdentIdentRequestFsmStageDescr=_CfprIdentIdentRequestFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,11),_CfprIdentIdentRequestFsmStageDescr_Type())
cfprIdentIdentRequestFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageDescr.setStatus(_A)
_CfprIdentIdentRequestFsmStamp_Type=DateAndTime
_CfprIdentIdentRequestFsmStamp_Object=MibTableColumn
cfprIdentIdentRequestFsmStamp=_CfprIdentIdentRequestFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,12),_CfprIdentIdentRequestFsmStamp_Type())
cfprIdentIdentRequestFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStamp.setStatus(_A)
_CfprIdentIdentRequestFsmStatus_Type=SnmpAdminString
_CfprIdentIdentRequestFsmStatus_Object=MibTableColumn
cfprIdentIdentRequestFsmStatus=_CfprIdentIdentRequestFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,13),_CfprIdentIdentRequestFsmStatus_Type())
cfprIdentIdentRequestFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStatus.setStatus(_A)
_CfprIdentIdentRequestFsmTry_Type=Gauge32
_CfprIdentIdentRequestFsmTry_Object=MibTableColumn
cfprIdentIdentRequestFsmTry=_CfprIdentIdentRequestFsmTry_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,14),_CfprIdentIdentRequestFsmTry_Type())
cfprIdentIdentRequestFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTry.setStatus(_A)
_CfprIdentIdentRequestId_Type=Gauge32
_CfprIdentIdentRequestId_Object=MibTableColumn
cfprIdentIdentRequestId=_CfprIdentIdentRequestId_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,15),_CfprIdentIdentRequestId_Type())
cfprIdentIdentRequestId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestId.setStatus(_A)
_CfprIdentIdentRequestRequestSize_Type=Gauge32
_CfprIdentIdentRequestRequestSize_Object=MibTableColumn
cfprIdentIdentRequestRequestSize=_CfprIdentIdentRequestRequestSize_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,16),_CfprIdentIdentRequestRequestSize_Type())
cfprIdentIdentRequestRequestSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestRequestSize.setStatus(_A)
_CfprIdentIdentRequestSeqNum_Type=Gauge32
_CfprIdentIdentRequestSeqNum_Object=MibTableColumn
cfprIdentIdentRequestSeqNum=_CfprIdentIdentRequestSeqNum_Object((1,3,6,1,4,1,9,9,826,1,36,2,1,17),_CfprIdentIdentRequestSeqNum_Type())
cfprIdentIdentRequestSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestSeqNum.setStatus(_A)
_CfprIdentIdentRequestFsmTable_Object=MibTable
cfprIdentIdentRequestFsmTable=_CfprIdentIdentRequestFsmTable_Object((1,3,6,1,4,1,9,9,826,1,36,3))
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTable.setStatus(_A)
_CfprIdentIdentRequestFsmEntry_Object=MibTableRow
cfprIdentIdentRequestFsmEntry=_CfprIdentIdentRequestFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,36,3,1))
cfprIdentIdentRequestFsmEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmEntry.setStatus(_A)
_CfprIdentIdentRequestFsmInstanceId_Type=CfprManagedObjectId
_CfprIdentIdentRequestFsmInstanceId_Object=MibTableColumn
cfprIdentIdentRequestFsmInstanceId=_CfprIdentIdentRequestFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,1),_CfprIdentIdentRequestFsmInstanceId_Type())
cfprIdentIdentRequestFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmInstanceId.setStatus(_A)
_CfprIdentIdentRequestFsmDn_Type=CfprManagedObjectDn
_CfprIdentIdentRequestFsmDn_Object=MibTableColumn
cfprIdentIdentRequestFsmDn=_CfprIdentIdentRequestFsmDn_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,2),_CfprIdentIdentRequestFsmDn_Type())
cfprIdentIdentRequestFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmDn.setStatus(_A)
_CfprIdentIdentRequestFsmRn_Type=SnmpAdminString
_CfprIdentIdentRequestFsmRn_Object=MibTableColumn
cfprIdentIdentRequestFsmRn=_CfprIdentIdentRequestFsmRn_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,3),_CfprIdentIdentRequestFsmRn_Type())
cfprIdentIdentRequestFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmRn.setStatus(_A)
_CfprIdentIdentRequestFsmCompletionTime_Type=DateAndTime
_CfprIdentIdentRequestFsmCompletionTime_Object=MibTableColumn
cfprIdentIdentRequestFsmCompletionTime=_CfprIdentIdentRequestFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,4),_CfprIdentIdentRequestFsmCompletionTime_Type())
cfprIdentIdentRequestFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmCompletionTime.setStatus(_A)
_CfprIdentIdentRequestFsmCurrentFsm_Type=CfprIdentIdentRequestFsmCurrentFsm
_CfprIdentIdentRequestFsmCurrentFsm_Object=MibTableColumn
cfprIdentIdentRequestFsmCurrentFsm=_CfprIdentIdentRequestFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,5),_CfprIdentIdentRequestFsmCurrentFsm_Type())
cfprIdentIdentRequestFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmCurrentFsm.setStatus(_A)
_CfprIdentIdentRequestFsmDescrData_Type=SnmpAdminString
_CfprIdentIdentRequestFsmDescrData_Object=MibTableColumn
cfprIdentIdentRequestFsmDescrData=_CfprIdentIdentRequestFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,6),_CfprIdentIdentRequestFsmDescrData_Type())
cfprIdentIdentRequestFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmDescrData.setStatus(_A)
_CfprIdentIdentRequestFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprIdentIdentRequestFsmFsmStatus_Object=MibTableColumn
cfprIdentIdentRequestFsmFsmStatus=_CfprIdentIdentRequestFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,7),_CfprIdentIdentRequestFsmFsmStatus_Type())
cfprIdentIdentRequestFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmFsmStatus.setStatus(_A)
_CfprIdentIdentRequestFsmProgress_Type=Gauge32
_CfprIdentIdentRequestFsmProgress_Object=MibTableColumn
cfprIdentIdentRequestFsmProgress=_CfprIdentIdentRequestFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,8),_CfprIdentIdentRequestFsmProgress_Type())
cfprIdentIdentRequestFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmProgress.setStatus(_A)
_CfprIdentIdentRequestFsmRmtErrCode_Type=Gauge32
_CfprIdentIdentRequestFsmRmtErrCode_Object=MibTableColumn
cfprIdentIdentRequestFsmRmtErrCode=_CfprIdentIdentRequestFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,9),_CfprIdentIdentRequestFsmRmtErrCode_Type())
cfprIdentIdentRequestFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmRmtErrCode.setStatus(_A)
_CfprIdentIdentRequestFsmRmtErrDescr_Type=SnmpAdminString
_CfprIdentIdentRequestFsmRmtErrDescr_Object=MibTableColumn
cfprIdentIdentRequestFsmRmtErrDescr=_CfprIdentIdentRequestFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,10),_CfprIdentIdentRequestFsmRmtErrDescr_Type())
cfprIdentIdentRequestFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmRmtErrDescr.setStatus(_A)
_CfprIdentIdentRequestFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprIdentIdentRequestFsmRmtRslt_Object=MibTableColumn
cfprIdentIdentRequestFsmRmtRslt=_CfprIdentIdentRequestFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,36,3,1,11),_CfprIdentIdentRequestFsmRmtRslt_Type())
cfprIdentIdentRequestFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmRmtRslt.setStatus(_A)
_CfprIdentIdentRequestFsmStageTable_Object=MibTable
cfprIdentIdentRequestFsmStageTable=_CfprIdentIdentRequestFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,36,4))
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageTable.setStatus(_A)
_CfprIdentIdentRequestFsmStageEntry_Object=MibTableRow
cfprIdentIdentRequestFsmStageEntry=_CfprIdentIdentRequestFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,36,4,1))
cfprIdentIdentRequestFsmStageEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageEntry.setStatus(_A)
_CfprIdentIdentRequestFsmStageInstanceId_Type=CfprManagedObjectId
_CfprIdentIdentRequestFsmStageInstanceId_Object=MibTableColumn
cfprIdentIdentRequestFsmStageInstanceId=_CfprIdentIdentRequestFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,4,1,1),_CfprIdentIdentRequestFsmStageInstanceId_Type())
cfprIdentIdentRequestFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageInstanceId.setStatus(_A)
_CfprIdentIdentRequestFsmStageDn_Type=CfprManagedObjectDn
_CfprIdentIdentRequestFsmStageDn_Object=MibTableColumn
cfprIdentIdentRequestFsmStageDn=_CfprIdentIdentRequestFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,36,4,1,2),_CfprIdentIdentRequestFsmStageDn_Type())
cfprIdentIdentRequestFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageDn.setStatus(_A)
_CfprIdentIdentRequestFsmStageRn_Type=SnmpAdminString
_CfprIdentIdentRequestFsmStageRn_Object=MibTableColumn
cfprIdentIdentRequestFsmStageRn=_CfprIdentIdentRequestFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,36,4,1,3),_CfprIdentIdentRequestFsmStageRn_Type())
cfprIdentIdentRequestFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageRn.setStatus(_A)
_CfprIdentIdentRequestFsmStageDescrData_Type=SnmpAdminString
_CfprIdentIdentRequestFsmStageDescrData_Object=MibTableColumn
cfprIdentIdentRequestFsmStageDescrData=_CfprIdentIdentRequestFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,36,4,1,4),_CfprIdentIdentRequestFsmStageDescrData_Type())
cfprIdentIdentRequestFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageDescrData.setStatus(_A)
_CfprIdentIdentRequestFsmStageLastUpdateTime_Type=DateAndTime
_CfprIdentIdentRequestFsmStageLastUpdateTime_Object=MibTableColumn
cfprIdentIdentRequestFsmStageLastUpdateTime=_CfprIdentIdentRequestFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,36,4,1,5),_CfprIdentIdentRequestFsmStageLastUpdateTime_Type())
cfprIdentIdentRequestFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageLastUpdateTime.setStatus(_A)
_CfprIdentIdentRequestFsmStageName_Type=CfprIdentIdentRequestFsmStageName
_CfprIdentIdentRequestFsmStageName_Object=MibTableColumn
cfprIdentIdentRequestFsmStageName=_CfprIdentIdentRequestFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,36,4,1,6),_CfprIdentIdentRequestFsmStageName_Type())
cfprIdentIdentRequestFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageName.setStatus(_A)
_CfprIdentIdentRequestFsmStageOrder_Type=Gauge32
_CfprIdentIdentRequestFsmStageOrder_Object=MibTableColumn
cfprIdentIdentRequestFsmStageOrder=_CfprIdentIdentRequestFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,36,4,1,7),_CfprIdentIdentRequestFsmStageOrder_Type())
cfprIdentIdentRequestFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageOrder.setStatus(_A)
_CfprIdentIdentRequestFsmStageRetry_Type=Gauge32
_CfprIdentIdentRequestFsmStageRetry_Object=MibTableColumn
cfprIdentIdentRequestFsmStageRetry=_CfprIdentIdentRequestFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,36,4,1,8),_CfprIdentIdentRequestFsmStageRetry_Type())
cfprIdentIdentRequestFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageRetry.setStatus(_A)
_CfprIdentIdentRequestFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprIdentIdentRequestFsmStageStageStatus_Object=MibTableColumn
cfprIdentIdentRequestFsmStageStageStatus=_CfprIdentIdentRequestFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,36,4,1,9),_CfprIdentIdentRequestFsmStageStageStatus_Type())
cfprIdentIdentRequestFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmStageStageStatus.setStatus(_A)
_CfprIdentIdentRequestFsmTaskTable_Object=MibTable
cfprIdentIdentRequestFsmTaskTable=_CfprIdentIdentRequestFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,36,5))
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTaskTable.setStatus(_A)
_CfprIdentIdentRequestFsmTaskEntry_Object=MibTableRow
cfprIdentIdentRequestFsmTaskEntry=_CfprIdentIdentRequestFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,36,5,1))
cfprIdentIdentRequestFsmTaskEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTaskEntry.setStatus(_A)
_CfprIdentIdentRequestFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprIdentIdentRequestFsmTaskInstanceId_Object=MibTableColumn
cfprIdentIdentRequestFsmTaskInstanceId=_CfprIdentIdentRequestFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,5,1,1),_CfprIdentIdentRequestFsmTaskInstanceId_Type())
cfprIdentIdentRequestFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTaskInstanceId.setStatus(_A)
_CfprIdentIdentRequestFsmTaskDn_Type=CfprManagedObjectDn
_CfprIdentIdentRequestFsmTaskDn_Object=MibTableColumn
cfprIdentIdentRequestFsmTaskDn=_CfprIdentIdentRequestFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,36,5,1,2),_CfprIdentIdentRequestFsmTaskDn_Type())
cfprIdentIdentRequestFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTaskDn.setStatus(_A)
_CfprIdentIdentRequestFsmTaskRn_Type=SnmpAdminString
_CfprIdentIdentRequestFsmTaskRn_Object=MibTableColumn
cfprIdentIdentRequestFsmTaskRn=_CfprIdentIdentRequestFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,36,5,1,3),_CfprIdentIdentRequestFsmTaskRn_Type())
cfprIdentIdentRequestFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTaskRn.setStatus(_A)
_CfprIdentIdentRequestFsmTaskCompletion_Type=CfprFsmCompletion
_CfprIdentIdentRequestFsmTaskCompletion_Object=MibTableColumn
cfprIdentIdentRequestFsmTaskCompletion=_CfprIdentIdentRequestFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,36,5,1,4),_CfprIdentIdentRequestFsmTaskCompletion_Type())
cfprIdentIdentRequestFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTaskCompletion.setStatus(_A)
_CfprIdentIdentRequestFsmTaskFlags_Type=CfprFsmFlags
_CfprIdentIdentRequestFsmTaskFlags_Object=MibTableColumn
cfprIdentIdentRequestFsmTaskFlags=_CfprIdentIdentRequestFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,36,5,1,5),_CfprIdentIdentRequestFsmTaskFlags_Type())
cfprIdentIdentRequestFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTaskFlags.setStatus(_A)
_CfprIdentIdentRequestFsmTaskItem_Type=CfprIdentIdentRequestFsmTaskItem
_CfprIdentIdentRequestFsmTaskItem_Object=MibTableColumn
cfprIdentIdentRequestFsmTaskItem=_CfprIdentIdentRequestFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,36,5,1,6),_CfprIdentIdentRequestFsmTaskItem_Type())
cfprIdentIdentRequestFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTaskItem.setStatus(_A)
_CfprIdentIdentRequestFsmTaskSeqId_Type=Gauge32
_CfprIdentIdentRequestFsmTaskSeqId_Object=MibTableColumn
cfprIdentIdentRequestFsmTaskSeqId=_CfprIdentIdentRequestFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,36,5,1,7),_CfprIdentIdentRequestFsmTaskSeqId_Type())
cfprIdentIdentRequestFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentIdentRequestFsmTaskSeqId.setStatus(_A)
_CfprIdentMetaSystemTable_Object=MibTable
cfprIdentMetaSystemTable=_CfprIdentMetaSystemTable_Object((1,3,6,1,4,1,9,9,826,1,36,6))
if mibBuilder.loadTexts:cfprIdentMetaSystemTable.setStatus(_A)
_CfprIdentMetaSystemEntry_Object=MibTableRow
cfprIdentMetaSystemEntry=_CfprIdentMetaSystemEntry_Object((1,3,6,1,4,1,9,9,826,1,36,6,1))
cfprIdentMetaSystemEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprIdentMetaSystemEntry.setStatus(_A)
_CfprIdentMetaSystemInstanceId_Type=CfprManagedObjectId
_CfprIdentMetaSystemInstanceId_Object=MibTableColumn
cfprIdentMetaSystemInstanceId=_CfprIdentMetaSystemInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,1),_CfprIdentMetaSystemInstanceId_Type())
cfprIdentMetaSystemInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentMetaSystemInstanceId.setStatus(_A)
_CfprIdentMetaSystemDn_Type=CfprManagedObjectDn
_CfprIdentMetaSystemDn_Object=MibTableColumn
cfprIdentMetaSystemDn=_CfprIdentMetaSystemDn_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,2),_CfprIdentMetaSystemDn_Type())
cfprIdentMetaSystemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemDn.setStatus(_A)
_CfprIdentMetaSystemRn_Type=SnmpAdminString
_CfprIdentMetaSystemRn_Object=MibTableColumn
cfprIdentMetaSystemRn=_CfprIdentMetaSystemRn_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,3),_CfprIdentMetaSystemRn_Type())
cfprIdentMetaSystemRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemRn.setStatus(_A)
_CfprIdentMetaSystemFsmDescr_Type=SnmpAdminString
_CfprIdentMetaSystemFsmDescr_Object=MibTableColumn
cfprIdentMetaSystemFsmDescr=_CfprIdentMetaSystemFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,4),_CfprIdentMetaSystemFsmDescr_Type())
cfprIdentMetaSystemFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmDescr.setStatus(_A)
_CfprIdentMetaSystemFsmPrev_Type=SnmpAdminString
_CfprIdentMetaSystemFsmPrev_Object=MibTableColumn
cfprIdentMetaSystemFsmPrev=_CfprIdentMetaSystemFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,5),_CfprIdentMetaSystemFsmPrev_Type())
cfprIdentMetaSystemFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmPrev.setStatus(_A)
_CfprIdentMetaSystemFsmProgr_Type=Gauge32
_CfprIdentMetaSystemFsmProgr_Object=MibTableColumn
cfprIdentMetaSystemFsmProgr=_CfprIdentMetaSystemFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,6),_CfprIdentMetaSystemFsmProgr_Type())
cfprIdentMetaSystemFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmProgr.setStatus(_A)
_CfprIdentMetaSystemFsmRmtInvErrCode_Type=Gauge32
_CfprIdentMetaSystemFsmRmtInvErrCode_Object=MibTableColumn
cfprIdentMetaSystemFsmRmtInvErrCode=_CfprIdentMetaSystemFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,7),_CfprIdentMetaSystemFsmRmtInvErrCode_Type())
cfprIdentMetaSystemFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmRmtInvErrCode.setStatus(_A)
_CfprIdentMetaSystemFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprIdentMetaSystemFsmRmtInvErrDescr_Object=MibTableColumn
cfprIdentMetaSystemFsmRmtInvErrDescr=_CfprIdentMetaSystemFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,8),_CfprIdentMetaSystemFsmRmtInvErrDescr_Type())
cfprIdentMetaSystemFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmRmtInvErrDescr.setStatus(_A)
_CfprIdentMetaSystemFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprIdentMetaSystemFsmRmtInvRslt_Object=MibTableColumn
cfprIdentMetaSystemFsmRmtInvRslt=_CfprIdentMetaSystemFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,9),_CfprIdentMetaSystemFsmRmtInvRslt_Type())
cfprIdentMetaSystemFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmRmtInvRslt.setStatus(_A)
_CfprIdentMetaSystemFsmStageDescr_Type=SnmpAdminString
_CfprIdentMetaSystemFsmStageDescr_Object=MibTableColumn
cfprIdentMetaSystemFsmStageDescr=_CfprIdentMetaSystemFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,10),_CfprIdentMetaSystemFsmStageDescr_Type())
cfprIdentMetaSystemFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageDescr.setStatus(_A)
_CfprIdentMetaSystemFsmStamp_Type=DateAndTime
_CfprIdentMetaSystemFsmStamp_Object=MibTableColumn
cfprIdentMetaSystemFsmStamp=_CfprIdentMetaSystemFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,11),_CfprIdentMetaSystemFsmStamp_Type())
cfprIdentMetaSystemFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStamp.setStatus(_A)
_CfprIdentMetaSystemFsmStatus_Type=SnmpAdminString
_CfprIdentMetaSystemFsmStatus_Object=MibTableColumn
cfprIdentMetaSystemFsmStatus=_CfprIdentMetaSystemFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,12),_CfprIdentMetaSystemFsmStatus_Type())
cfprIdentMetaSystemFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStatus.setStatus(_A)
_CfprIdentMetaSystemFsmTry_Type=Gauge32
_CfprIdentMetaSystemFsmTry_Object=MibTableColumn
cfprIdentMetaSystemFsmTry=_CfprIdentMetaSystemFsmTry_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,13),_CfprIdentMetaSystemFsmTry_Type())
cfprIdentMetaSystemFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTry.setStatus(_A)
_CfprIdentMetaSystemGeneration_Type=Gauge32
_CfprIdentMetaSystemGeneration_Object=MibTableColumn
cfprIdentMetaSystemGeneration=_CfprIdentMetaSystemGeneration_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,14),_CfprIdentMetaSystemGeneration_Type())
cfprIdentMetaSystemGeneration.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemGeneration.setStatus(_A)
_CfprIdentMetaSystemNextReqId_Type=Gauge32
_CfprIdentMetaSystemNextReqId_Object=MibTableColumn
cfprIdentMetaSystemNextReqId=_CfprIdentMetaSystemNextReqId_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,15),_CfprIdentMetaSystemNextReqId_Type())
cfprIdentMetaSystemNextReqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemNextReqId.setStatus(_A)
_CfprIdentMetaSystemSysid_Type=Gauge32
_CfprIdentMetaSystemSysid_Object=MibTableColumn
cfprIdentMetaSystemSysid=_CfprIdentMetaSystemSysid_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,16),_CfprIdentMetaSystemSysid_Type())
cfprIdentMetaSystemSysid.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemSysid.setStatus(_A)
_CfprIdentMetaSystemFprcGeneration_Type=Gauge32
_CfprIdentMetaSystemFprcGeneration_Object=MibTableColumn
cfprIdentMetaSystemFprcGeneration=_CfprIdentMetaSystemFprcGeneration_Object((1,3,6,1,4,1,9,9,826,1,36,6,1,17),_CfprIdentMetaSystemFprcGeneration_Type())
cfprIdentMetaSystemFprcGeneration.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFprcGeneration.setStatus(_A)
_CfprIdentMetaSystemFsmTable_Object=MibTable
cfprIdentMetaSystemFsmTable=_CfprIdentMetaSystemFsmTable_Object((1,3,6,1,4,1,9,9,826,1,36,7))
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTable.setStatus(_A)
_CfprIdentMetaSystemFsmEntry_Object=MibTableRow
cfprIdentMetaSystemFsmEntry=_CfprIdentMetaSystemFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,36,7,1))
cfprIdentMetaSystemFsmEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmEntry.setStatus(_A)
_CfprIdentMetaSystemFsmInstanceId_Type=CfprManagedObjectId
_CfprIdentMetaSystemFsmInstanceId_Object=MibTableColumn
cfprIdentMetaSystemFsmInstanceId=_CfprIdentMetaSystemFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,1),_CfprIdentMetaSystemFsmInstanceId_Type())
cfprIdentMetaSystemFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmInstanceId.setStatus(_A)
_CfprIdentMetaSystemFsmDn_Type=CfprManagedObjectDn
_CfprIdentMetaSystemFsmDn_Object=MibTableColumn
cfprIdentMetaSystemFsmDn=_CfprIdentMetaSystemFsmDn_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,2),_CfprIdentMetaSystemFsmDn_Type())
cfprIdentMetaSystemFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmDn.setStatus(_A)
_CfprIdentMetaSystemFsmRn_Type=SnmpAdminString
_CfprIdentMetaSystemFsmRn_Object=MibTableColumn
cfprIdentMetaSystemFsmRn=_CfprIdentMetaSystemFsmRn_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,3),_CfprIdentMetaSystemFsmRn_Type())
cfprIdentMetaSystemFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmRn.setStatus(_A)
_CfprIdentMetaSystemFsmCompletionTime_Type=DateAndTime
_CfprIdentMetaSystemFsmCompletionTime_Object=MibTableColumn
cfprIdentMetaSystemFsmCompletionTime=_CfprIdentMetaSystemFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,4),_CfprIdentMetaSystemFsmCompletionTime_Type())
cfprIdentMetaSystemFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmCompletionTime.setStatus(_A)
_CfprIdentMetaSystemFsmCurrentFsm_Type=CfprIdentMetaSystemFsmCurrentFsm
_CfprIdentMetaSystemFsmCurrentFsm_Object=MibTableColumn
cfprIdentMetaSystemFsmCurrentFsm=_CfprIdentMetaSystemFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,5),_CfprIdentMetaSystemFsmCurrentFsm_Type())
cfprIdentMetaSystemFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmCurrentFsm.setStatus(_A)
_CfprIdentMetaSystemFsmDescrData_Type=SnmpAdminString
_CfprIdentMetaSystemFsmDescrData_Object=MibTableColumn
cfprIdentMetaSystemFsmDescrData=_CfprIdentMetaSystemFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,6),_CfprIdentMetaSystemFsmDescrData_Type())
cfprIdentMetaSystemFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmDescrData.setStatus(_A)
_CfprIdentMetaSystemFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprIdentMetaSystemFsmFsmStatus_Object=MibTableColumn
cfprIdentMetaSystemFsmFsmStatus=_CfprIdentMetaSystemFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,7),_CfprIdentMetaSystemFsmFsmStatus_Type())
cfprIdentMetaSystemFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmFsmStatus.setStatus(_A)
_CfprIdentMetaSystemFsmProgress_Type=Gauge32
_CfprIdentMetaSystemFsmProgress_Object=MibTableColumn
cfprIdentMetaSystemFsmProgress=_CfprIdentMetaSystemFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,8),_CfprIdentMetaSystemFsmProgress_Type())
cfprIdentMetaSystemFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmProgress.setStatus(_A)
_CfprIdentMetaSystemFsmRmtErrCode_Type=Gauge32
_CfprIdentMetaSystemFsmRmtErrCode_Object=MibTableColumn
cfprIdentMetaSystemFsmRmtErrCode=_CfprIdentMetaSystemFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,9),_CfprIdentMetaSystemFsmRmtErrCode_Type())
cfprIdentMetaSystemFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmRmtErrCode.setStatus(_A)
_CfprIdentMetaSystemFsmRmtErrDescr_Type=SnmpAdminString
_CfprIdentMetaSystemFsmRmtErrDescr_Object=MibTableColumn
cfprIdentMetaSystemFsmRmtErrDescr=_CfprIdentMetaSystemFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,10),_CfprIdentMetaSystemFsmRmtErrDescr_Type())
cfprIdentMetaSystemFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmRmtErrDescr.setStatus(_A)
_CfprIdentMetaSystemFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprIdentMetaSystemFsmRmtRslt_Object=MibTableColumn
cfprIdentMetaSystemFsmRmtRslt=_CfprIdentMetaSystemFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,36,7,1,11),_CfprIdentMetaSystemFsmRmtRslt_Type())
cfprIdentMetaSystemFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmRmtRslt.setStatus(_A)
_CfprIdentMetaSystemFsmStageTable_Object=MibTable
cfprIdentMetaSystemFsmStageTable=_CfprIdentMetaSystemFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,36,8))
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageTable.setStatus(_A)
_CfprIdentMetaSystemFsmStageEntry_Object=MibTableRow
cfprIdentMetaSystemFsmStageEntry=_CfprIdentMetaSystemFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,36,8,1))
cfprIdentMetaSystemFsmStageEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageEntry.setStatus(_A)
_CfprIdentMetaSystemFsmStageInstanceId_Type=CfprManagedObjectId
_CfprIdentMetaSystemFsmStageInstanceId_Object=MibTableColumn
cfprIdentMetaSystemFsmStageInstanceId=_CfprIdentMetaSystemFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,8,1,1),_CfprIdentMetaSystemFsmStageInstanceId_Type())
cfprIdentMetaSystemFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageInstanceId.setStatus(_A)
_CfprIdentMetaSystemFsmStageDn_Type=CfprManagedObjectDn
_CfprIdentMetaSystemFsmStageDn_Object=MibTableColumn
cfprIdentMetaSystemFsmStageDn=_CfprIdentMetaSystemFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,36,8,1,2),_CfprIdentMetaSystemFsmStageDn_Type())
cfprIdentMetaSystemFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageDn.setStatus(_A)
_CfprIdentMetaSystemFsmStageRn_Type=SnmpAdminString
_CfprIdentMetaSystemFsmStageRn_Object=MibTableColumn
cfprIdentMetaSystemFsmStageRn=_CfprIdentMetaSystemFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,36,8,1,3),_CfprIdentMetaSystemFsmStageRn_Type())
cfprIdentMetaSystemFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageRn.setStatus(_A)
_CfprIdentMetaSystemFsmStageDescrData_Type=SnmpAdminString
_CfprIdentMetaSystemFsmStageDescrData_Object=MibTableColumn
cfprIdentMetaSystemFsmStageDescrData=_CfprIdentMetaSystemFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,36,8,1,4),_CfprIdentMetaSystemFsmStageDescrData_Type())
cfprIdentMetaSystemFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageDescrData.setStatus(_A)
_CfprIdentMetaSystemFsmStageLastUpdateTime_Type=DateAndTime
_CfprIdentMetaSystemFsmStageLastUpdateTime_Object=MibTableColumn
cfprIdentMetaSystemFsmStageLastUpdateTime=_CfprIdentMetaSystemFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,36,8,1,5),_CfprIdentMetaSystemFsmStageLastUpdateTime_Type())
cfprIdentMetaSystemFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageLastUpdateTime.setStatus(_A)
_CfprIdentMetaSystemFsmStageName_Type=CfprIdentMetaSystemFsmStageName
_CfprIdentMetaSystemFsmStageName_Object=MibTableColumn
cfprIdentMetaSystemFsmStageName=_CfprIdentMetaSystemFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,36,8,1,6),_CfprIdentMetaSystemFsmStageName_Type())
cfprIdentMetaSystemFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageName.setStatus(_A)
_CfprIdentMetaSystemFsmStageOrder_Type=Gauge32
_CfprIdentMetaSystemFsmStageOrder_Object=MibTableColumn
cfprIdentMetaSystemFsmStageOrder=_CfprIdentMetaSystemFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,36,8,1,7),_CfprIdentMetaSystemFsmStageOrder_Type())
cfprIdentMetaSystemFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageOrder.setStatus(_A)
_CfprIdentMetaSystemFsmStageRetry_Type=Gauge32
_CfprIdentMetaSystemFsmStageRetry_Object=MibTableColumn
cfprIdentMetaSystemFsmStageRetry=_CfprIdentMetaSystemFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,36,8,1,8),_CfprIdentMetaSystemFsmStageRetry_Type())
cfprIdentMetaSystemFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageRetry.setStatus(_A)
_CfprIdentMetaSystemFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprIdentMetaSystemFsmStageStageStatus_Object=MibTableColumn
cfprIdentMetaSystemFsmStageStageStatus=_CfprIdentMetaSystemFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,36,8,1,9),_CfprIdentMetaSystemFsmStageStageStatus_Type())
cfprIdentMetaSystemFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmStageStageStatus.setStatus(_A)
_CfprIdentMetaSystemFsmTaskTable_Object=MibTable
cfprIdentMetaSystemFsmTaskTable=_CfprIdentMetaSystemFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,36,9))
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTaskTable.setStatus(_A)
_CfprIdentMetaSystemFsmTaskEntry_Object=MibTableRow
cfprIdentMetaSystemFsmTaskEntry=_CfprIdentMetaSystemFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,36,9,1))
cfprIdentMetaSystemFsmTaskEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTaskEntry.setStatus(_A)
_CfprIdentMetaSystemFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprIdentMetaSystemFsmTaskInstanceId_Object=MibTableColumn
cfprIdentMetaSystemFsmTaskInstanceId=_CfprIdentMetaSystemFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,9,1,1),_CfprIdentMetaSystemFsmTaskInstanceId_Type())
cfprIdentMetaSystemFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTaskInstanceId.setStatus(_A)
_CfprIdentMetaSystemFsmTaskDn_Type=CfprManagedObjectDn
_CfprIdentMetaSystemFsmTaskDn_Object=MibTableColumn
cfprIdentMetaSystemFsmTaskDn=_CfprIdentMetaSystemFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,36,9,1,2),_CfprIdentMetaSystemFsmTaskDn_Type())
cfprIdentMetaSystemFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTaskDn.setStatus(_A)
_CfprIdentMetaSystemFsmTaskRn_Type=SnmpAdminString
_CfprIdentMetaSystemFsmTaskRn_Object=MibTableColumn
cfprIdentMetaSystemFsmTaskRn=_CfprIdentMetaSystemFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,36,9,1,3),_CfprIdentMetaSystemFsmTaskRn_Type())
cfprIdentMetaSystemFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTaskRn.setStatus(_A)
_CfprIdentMetaSystemFsmTaskCompletion_Type=CfprFsmCompletion
_CfprIdentMetaSystemFsmTaskCompletion_Object=MibTableColumn
cfprIdentMetaSystemFsmTaskCompletion=_CfprIdentMetaSystemFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,36,9,1,4),_CfprIdentMetaSystemFsmTaskCompletion_Type())
cfprIdentMetaSystemFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTaskCompletion.setStatus(_A)
_CfprIdentMetaSystemFsmTaskFlags_Type=CfprFsmFlags
_CfprIdentMetaSystemFsmTaskFlags_Object=MibTableColumn
cfprIdentMetaSystemFsmTaskFlags=_CfprIdentMetaSystemFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,36,9,1,5),_CfprIdentMetaSystemFsmTaskFlags_Type())
cfprIdentMetaSystemFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTaskFlags.setStatus(_A)
_CfprIdentMetaSystemFsmTaskItem_Type=CfprIdentMetaSystemFsmTaskItem
_CfprIdentMetaSystemFsmTaskItem_Object=MibTableColumn
cfprIdentMetaSystemFsmTaskItem=_CfprIdentMetaSystemFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,36,9,1,6),_CfprIdentMetaSystemFsmTaskItem_Type())
cfprIdentMetaSystemFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTaskItem.setStatus(_A)
_CfprIdentMetaSystemFsmTaskSeqId_Type=Gauge32
_CfprIdentMetaSystemFsmTaskSeqId_Object=MibTableColumn
cfprIdentMetaSystemFsmTaskSeqId=_CfprIdentMetaSystemFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,36,9,1,7),_CfprIdentMetaSystemFsmTaskSeqId_Type())
cfprIdentMetaSystemFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaSystemFsmTaskSeqId.setStatus(_A)
_CfprIdentMetaVerseTable_Object=MibTable
cfprIdentMetaVerseTable=_CfprIdentMetaVerseTable_Object((1,3,6,1,4,1,9,9,826,1,36,10))
if mibBuilder.loadTexts:cfprIdentMetaVerseTable.setStatus(_A)
_CfprIdentMetaVerseEntry_Object=MibTableRow
cfprIdentMetaVerseEntry=_CfprIdentMetaVerseEntry_Object((1,3,6,1,4,1,9,9,826,1,36,10,1))
cfprIdentMetaVerseEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cfprIdentMetaVerseEntry.setStatus(_A)
_CfprIdentMetaVerseInstanceId_Type=CfprManagedObjectId
_CfprIdentMetaVerseInstanceId_Object=MibTableColumn
cfprIdentMetaVerseInstanceId=_CfprIdentMetaVerseInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,10,1,1),_CfprIdentMetaVerseInstanceId_Type())
cfprIdentMetaVerseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentMetaVerseInstanceId.setStatus(_A)
_CfprIdentMetaVerseDn_Type=CfprManagedObjectDn
_CfprIdentMetaVerseDn_Object=MibTableColumn
cfprIdentMetaVerseDn=_CfprIdentMetaVerseDn_Object((1,3,6,1,4,1,9,9,826,1,36,10,1,2),_CfprIdentMetaVerseDn_Type())
cfprIdentMetaVerseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaVerseDn.setStatus(_A)
_CfprIdentMetaVerseRn_Type=SnmpAdminString
_CfprIdentMetaVerseRn_Object=MibTableColumn
cfprIdentMetaVerseRn=_CfprIdentMetaVerseRn_Object((1,3,6,1,4,1,9,9,826,1,36,10,1,3),_CfprIdentMetaVerseRn_Type())
cfprIdentMetaVerseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentMetaVerseRn.setStatus(_A)
_CfprIdentRequestEpTable_Object=MibTable
cfprIdentRequestEpTable=_CfprIdentRequestEpTable_Object((1,3,6,1,4,1,9,9,826,1,36,11))
if mibBuilder.loadTexts:cfprIdentRequestEpTable.setStatus(_A)
_CfprIdentRequestEpEntry_Object=MibTableRow
cfprIdentRequestEpEntry=_CfprIdentRequestEpEntry_Object((1,3,6,1,4,1,9,9,826,1,36,11,1))
cfprIdentRequestEpEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cfprIdentRequestEpEntry.setStatus(_A)
_CfprIdentRequestEpInstanceId_Type=CfprManagedObjectId
_CfprIdentRequestEpInstanceId_Object=MibTableColumn
cfprIdentRequestEpInstanceId=_CfprIdentRequestEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,11,1,1),_CfprIdentRequestEpInstanceId_Type())
cfprIdentRequestEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentRequestEpInstanceId.setStatus(_A)
_CfprIdentRequestEpDn_Type=CfprManagedObjectDn
_CfprIdentRequestEpDn_Object=MibTableColumn
cfprIdentRequestEpDn=_CfprIdentRequestEpDn_Object((1,3,6,1,4,1,9,9,826,1,36,11,1,2),_CfprIdentRequestEpDn_Type())
cfprIdentRequestEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentRequestEpDn.setStatus(_A)
_CfprIdentRequestEpRn_Type=SnmpAdminString
_CfprIdentRequestEpRn_Object=MibTableColumn
cfprIdentRequestEpRn=_CfprIdentRequestEpRn_Object((1,3,6,1,4,1,9,9,826,1,36,11,1,3),_CfprIdentRequestEpRn_Type())
cfprIdentRequestEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentRequestEpRn.setStatus(_A)
_CfprIdentRequestEpReqDn_Type=SnmpAdminString
_CfprIdentRequestEpReqDn_Object=MibTableColumn
cfprIdentRequestEpReqDn=_CfprIdentRequestEpReqDn_Object((1,3,6,1,4,1,9,9,826,1,36,11,1,4),_CfprIdentRequestEpReqDn_Type())
cfprIdentRequestEpReqDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentRequestEpReqDn.setStatus(_A)
_CfprIdentRequestEpReqId_Type=Gauge32
_CfprIdentRequestEpReqId_Object=MibTableColumn
cfprIdentRequestEpReqId=_CfprIdentRequestEpReqId_Object((1,3,6,1,4,1,9,9,826,1,36,11,1,5),_CfprIdentRequestEpReqId_Type())
cfprIdentRequestEpReqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentRequestEpReqId.setStatus(_A)
_CfprIdentSysInfoTable_Object=MibTable
cfprIdentSysInfoTable=_CfprIdentSysInfoTable_Object((1,3,6,1,4,1,9,9,826,1,36,12))
if mibBuilder.loadTexts:cfprIdentSysInfoTable.setStatus(_A)
_CfprIdentSysInfoEntry_Object=MibTableRow
cfprIdentSysInfoEntry=_CfprIdentSysInfoEntry_Object((1,3,6,1,4,1,9,9,826,1,36,12,1))
cfprIdentSysInfoEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cfprIdentSysInfoEntry.setStatus(_A)
_CfprIdentSysInfoInstanceId_Type=CfprManagedObjectId
_CfprIdentSysInfoInstanceId_Object=MibTableColumn
cfprIdentSysInfoInstanceId=_CfprIdentSysInfoInstanceId_Object((1,3,6,1,4,1,9,9,826,1,36,12,1,1),_CfprIdentSysInfoInstanceId_Type())
cfprIdentSysInfoInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIdentSysInfoInstanceId.setStatus(_A)
_CfprIdentSysInfoDn_Type=CfprManagedObjectDn
_CfprIdentSysInfoDn_Object=MibTableColumn
cfprIdentSysInfoDn=_CfprIdentSysInfoDn_Object((1,3,6,1,4,1,9,9,826,1,36,12,1,2),_CfprIdentSysInfoDn_Type())
cfprIdentSysInfoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentSysInfoDn.setStatus(_A)
_CfprIdentSysInfoRn_Type=SnmpAdminString
_CfprIdentSysInfoRn_Object=MibTableColumn
cfprIdentSysInfoRn=_CfprIdentSysInfoRn_Object((1,3,6,1,4,1,9,9,826,1,36,12,1,3),_CfprIdentSysInfoRn_Type())
cfprIdentSysInfoRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentSysInfoRn.setStatus(_A)
_CfprIdentSysInfoGeneration_Type=Gauge32
_CfprIdentSysInfoGeneration_Object=MibTableColumn
cfprIdentSysInfoGeneration=_CfprIdentSysInfoGeneration_Object((1,3,6,1,4,1,9,9,826,1,36,12,1,4),_CfprIdentSysInfoGeneration_Type())
cfprIdentSysInfoGeneration.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentSysInfoGeneration.setStatus(_A)
_CfprIdentSysInfoIsFirstSync_Type=TruthValue
_CfprIdentSysInfoIsFirstSync_Object=MibTableColumn
cfprIdentSysInfoIsFirstSync=_CfprIdentSysInfoIsFirstSync_Object((1,3,6,1,4,1,9,9,826,1,36,12,1,5),_CfprIdentSysInfoIsFirstSync_Type())
cfprIdentSysInfoIsFirstSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentSysInfoIsFirstSync.setStatus(_A)
_CfprIdentSysInfoIsSync_Type=TruthValue
_CfprIdentSysInfoIsSync_Object=MibTableColumn
cfprIdentSysInfoIsSync=_CfprIdentSysInfoIsSync_Object((1,3,6,1,4,1,9,9,826,1,36,12,1,6),_CfprIdentSysInfoIsSync_Type())
cfprIdentSysInfoIsSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentSysInfoIsSync.setStatus(_A)
_CfprIdentSysInfoIsSyncAllowed_Type=TruthValue
_CfprIdentSysInfoIsSyncAllowed_Object=MibTableColumn
cfprIdentSysInfoIsSyncAllowed=_CfprIdentSysInfoIsSyncAllowed_Object((1,3,6,1,4,1,9,9,826,1,36,12,1,7),_CfprIdentSysInfoIsSyncAllowed_Type())
cfprIdentSysInfoIsSyncAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentSysInfoIsSyncAllowed.setStatus(_A)
_CfprIdentSysInfoFprcGeneration_Type=Gauge32
_CfprIdentSysInfoFprcGeneration_Object=MibTableColumn
cfprIdentSysInfoFprcGeneration=_CfprIdentSysInfoFprcGeneration_Object((1,3,6,1,4,1,9,9,826,1,36,12,1,8),_CfprIdentSysInfoFprcGeneration_Type())
cfprIdentSysInfoFprcGeneration.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIdentSysInfoFprcGeneration.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprIdentObjects':cfprIdentObjects,'cfprIdentIdentCtxTable':cfprIdentIdentCtxTable,'cfprIdentIdentCtxEntry':cfprIdentIdentCtxEntry,_E:cfprIdentIdentCtxInstanceId,'cfprIdentIdentCtxDn':cfprIdentIdentCtxDn,'cfprIdentIdentCtxRn':cfprIdentIdentCtxRn,'cfprIdentIdentCtxAssigned':cfprIdentIdentCtxAssigned,'cfprIdentIdentCtxConsDn':cfprIdentIdentCtxConsDn,'cfprIdentIdentCtxConsType':cfprIdentIdentCtxConsType,'cfprIdentIdentCtxDefinedInIdm':cfprIdentIdentCtxDefinedInIdm,'cfprIdentIdentCtxGlobalAssignedCnt':cfprIdentIdentCtxGlobalAssignedCnt,'cfprIdentIdentCtxGlobalDefinedCnt':cfprIdentIdentCtxGlobalDefinedCnt,'cfprIdentIdentCtxIdentPoolName':cfprIdentIdentCtxIdentPoolName,'cfprIdentIdentCtxIdentType':cfprIdentIdentCtxIdentType,'cfprIdentIdentCtxIntent':cfprIdentIdentCtxIntent,'cfprIdentIdentCtxIsAssignedLocally':cfprIdentIdentCtxIsAssignedLocally,'cfprIdentIdentCtxPoolDn':cfprIdentIdentCtxPoolDn,'cfprIdentIdentCtxPoolOrgDn':cfprIdentIdentCtxPoolOrgDn,'cfprIdentIdentCtxPooledId':cfprIdentIdentCtxPooledId,'cfprIdentIdentCtxRetStatus':cfprIdentIdentCtxRetStatus,'cfprIdentIdentCtxSeqNum':cfprIdentIdentCtxSeqNum,'cfprIdentIdentCtxSupplId1':cfprIdentIdentCtxSupplId1,'cfprIdentIdentCtxSupplId2':cfprIdentIdentCtxSupplId2,'cfprIdentIdentCtxSupplId3':cfprIdentIdentCtxSupplId3,'cfprIdentIdentCtxSupplId4':cfprIdentIdentCtxSupplId4,'cfprIdentIdentRequestTable':cfprIdentIdentRequestTable,'cfprIdentIdentRequestEntry':cfprIdentIdentRequestEntry,_F:cfprIdentIdentRequestInstanceId,'cfprIdentIdentRequestDn':cfprIdentIdentRequestDn,'cfprIdentIdentRequestRn':cfprIdentIdentRequestRn,'cfprIdentIdentRequestEpDn':cfprIdentIdentRequestEpDn,'cfprIdentIdentRequestFsmDescr':cfprIdentIdentRequestFsmDescr,'cfprIdentIdentRequestFsmPrev':cfprIdentIdentRequestFsmPrev,'cfprIdentIdentRequestFsmProgr':cfprIdentIdentRequestFsmProgr,'cfprIdentIdentRequestFsmRmtInvErrCode':cfprIdentIdentRequestFsmRmtInvErrCode,'cfprIdentIdentRequestFsmRmtInvErrDescr':cfprIdentIdentRequestFsmRmtInvErrDescr,'cfprIdentIdentRequestFsmRmtInvRslt':cfprIdentIdentRequestFsmRmtInvRslt,'cfprIdentIdentRequestFsmStageDescr':cfprIdentIdentRequestFsmStageDescr,'cfprIdentIdentRequestFsmStamp':cfprIdentIdentRequestFsmStamp,'cfprIdentIdentRequestFsmStatus':cfprIdentIdentRequestFsmStatus,'cfprIdentIdentRequestFsmTry':cfprIdentIdentRequestFsmTry,'cfprIdentIdentRequestId':cfprIdentIdentRequestId,'cfprIdentIdentRequestRequestSize':cfprIdentIdentRequestRequestSize,'cfprIdentIdentRequestSeqNum':cfprIdentIdentRequestSeqNum,'cfprIdentIdentRequestFsmTable':cfprIdentIdentRequestFsmTable,'cfprIdentIdentRequestFsmEntry':cfprIdentIdentRequestFsmEntry,_G:cfprIdentIdentRequestFsmInstanceId,'cfprIdentIdentRequestFsmDn':cfprIdentIdentRequestFsmDn,'cfprIdentIdentRequestFsmRn':cfprIdentIdentRequestFsmRn,'cfprIdentIdentRequestFsmCompletionTime':cfprIdentIdentRequestFsmCompletionTime,'cfprIdentIdentRequestFsmCurrentFsm':cfprIdentIdentRequestFsmCurrentFsm,'cfprIdentIdentRequestFsmDescrData':cfprIdentIdentRequestFsmDescrData,'cfprIdentIdentRequestFsmFsmStatus':cfprIdentIdentRequestFsmFsmStatus,'cfprIdentIdentRequestFsmProgress':cfprIdentIdentRequestFsmProgress,'cfprIdentIdentRequestFsmRmtErrCode':cfprIdentIdentRequestFsmRmtErrCode,'cfprIdentIdentRequestFsmRmtErrDescr':cfprIdentIdentRequestFsmRmtErrDescr,'cfprIdentIdentRequestFsmRmtRslt':cfprIdentIdentRequestFsmRmtRslt,'cfprIdentIdentRequestFsmStageTable':cfprIdentIdentRequestFsmStageTable,'cfprIdentIdentRequestFsmStageEntry':cfprIdentIdentRequestFsmStageEntry,_H:cfprIdentIdentRequestFsmStageInstanceId,'cfprIdentIdentRequestFsmStageDn':cfprIdentIdentRequestFsmStageDn,'cfprIdentIdentRequestFsmStageRn':cfprIdentIdentRequestFsmStageRn,'cfprIdentIdentRequestFsmStageDescrData':cfprIdentIdentRequestFsmStageDescrData,'cfprIdentIdentRequestFsmStageLastUpdateTime':cfprIdentIdentRequestFsmStageLastUpdateTime,'cfprIdentIdentRequestFsmStageName':cfprIdentIdentRequestFsmStageName,'cfprIdentIdentRequestFsmStageOrder':cfprIdentIdentRequestFsmStageOrder,'cfprIdentIdentRequestFsmStageRetry':cfprIdentIdentRequestFsmStageRetry,'cfprIdentIdentRequestFsmStageStageStatus':cfprIdentIdentRequestFsmStageStageStatus,'cfprIdentIdentRequestFsmTaskTable':cfprIdentIdentRequestFsmTaskTable,'cfprIdentIdentRequestFsmTaskEntry':cfprIdentIdentRequestFsmTaskEntry,_I:cfprIdentIdentRequestFsmTaskInstanceId,'cfprIdentIdentRequestFsmTaskDn':cfprIdentIdentRequestFsmTaskDn,'cfprIdentIdentRequestFsmTaskRn':cfprIdentIdentRequestFsmTaskRn,'cfprIdentIdentRequestFsmTaskCompletion':cfprIdentIdentRequestFsmTaskCompletion,'cfprIdentIdentRequestFsmTaskFlags':cfprIdentIdentRequestFsmTaskFlags,'cfprIdentIdentRequestFsmTaskItem':cfprIdentIdentRequestFsmTaskItem,'cfprIdentIdentRequestFsmTaskSeqId':cfprIdentIdentRequestFsmTaskSeqId,'cfprIdentMetaSystemTable':cfprIdentMetaSystemTable,'cfprIdentMetaSystemEntry':cfprIdentMetaSystemEntry,_J:cfprIdentMetaSystemInstanceId,'cfprIdentMetaSystemDn':cfprIdentMetaSystemDn,'cfprIdentMetaSystemRn':cfprIdentMetaSystemRn,'cfprIdentMetaSystemFsmDescr':cfprIdentMetaSystemFsmDescr,'cfprIdentMetaSystemFsmPrev':cfprIdentMetaSystemFsmPrev,'cfprIdentMetaSystemFsmProgr':cfprIdentMetaSystemFsmProgr,'cfprIdentMetaSystemFsmRmtInvErrCode':cfprIdentMetaSystemFsmRmtInvErrCode,'cfprIdentMetaSystemFsmRmtInvErrDescr':cfprIdentMetaSystemFsmRmtInvErrDescr,'cfprIdentMetaSystemFsmRmtInvRslt':cfprIdentMetaSystemFsmRmtInvRslt,'cfprIdentMetaSystemFsmStageDescr':cfprIdentMetaSystemFsmStageDescr,'cfprIdentMetaSystemFsmStamp':cfprIdentMetaSystemFsmStamp,'cfprIdentMetaSystemFsmStatus':cfprIdentMetaSystemFsmStatus,'cfprIdentMetaSystemFsmTry':cfprIdentMetaSystemFsmTry,'cfprIdentMetaSystemGeneration':cfprIdentMetaSystemGeneration,'cfprIdentMetaSystemNextReqId':cfprIdentMetaSystemNextReqId,'cfprIdentMetaSystemSysid':cfprIdentMetaSystemSysid,'cfprIdentMetaSystemFprcGeneration':cfprIdentMetaSystemFprcGeneration,'cfprIdentMetaSystemFsmTable':cfprIdentMetaSystemFsmTable,'cfprIdentMetaSystemFsmEntry':cfprIdentMetaSystemFsmEntry,_K:cfprIdentMetaSystemFsmInstanceId,'cfprIdentMetaSystemFsmDn':cfprIdentMetaSystemFsmDn,'cfprIdentMetaSystemFsmRn':cfprIdentMetaSystemFsmRn,'cfprIdentMetaSystemFsmCompletionTime':cfprIdentMetaSystemFsmCompletionTime,'cfprIdentMetaSystemFsmCurrentFsm':cfprIdentMetaSystemFsmCurrentFsm,'cfprIdentMetaSystemFsmDescrData':cfprIdentMetaSystemFsmDescrData,'cfprIdentMetaSystemFsmFsmStatus':cfprIdentMetaSystemFsmFsmStatus,'cfprIdentMetaSystemFsmProgress':cfprIdentMetaSystemFsmProgress,'cfprIdentMetaSystemFsmRmtErrCode':cfprIdentMetaSystemFsmRmtErrCode,'cfprIdentMetaSystemFsmRmtErrDescr':cfprIdentMetaSystemFsmRmtErrDescr,'cfprIdentMetaSystemFsmRmtRslt':cfprIdentMetaSystemFsmRmtRslt,'cfprIdentMetaSystemFsmStageTable':cfprIdentMetaSystemFsmStageTable,'cfprIdentMetaSystemFsmStageEntry':cfprIdentMetaSystemFsmStageEntry,_L:cfprIdentMetaSystemFsmStageInstanceId,'cfprIdentMetaSystemFsmStageDn':cfprIdentMetaSystemFsmStageDn,'cfprIdentMetaSystemFsmStageRn':cfprIdentMetaSystemFsmStageRn,'cfprIdentMetaSystemFsmStageDescrData':cfprIdentMetaSystemFsmStageDescrData,'cfprIdentMetaSystemFsmStageLastUpdateTime':cfprIdentMetaSystemFsmStageLastUpdateTime,'cfprIdentMetaSystemFsmStageName':cfprIdentMetaSystemFsmStageName,'cfprIdentMetaSystemFsmStageOrder':cfprIdentMetaSystemFsmStageOrder,'cfprIdentMetaSystemFsmStageRetry':cfprIdentMetaSystemFsmStageRetry,'cfprIdentMetaSystemFsmStageStageStatus':cfprIdentMetaSystemFsmStageStageStatus,'cfprIdentMetaSystemFsmTaskTable':cfprIdentMetaSystemFsmTaskTable,'cfprIdentMetaSystemFsmTaskEntry':cfprIdentMetaSystemFsmTaskEntry,_M:cfprIdentMetaSystemFsmTaskInstanceId,'cfprIdentMetaSystemFsmTaskDn':cfprIdentMetaSystemFsmTaskDn,'cfprIdentMetaSystemFsmTaskRn':cfprIdentMetaSystemFsmTaskRn,'cfprIdentMetaSystemFsmTaskCompletion':cfprIdentMetaSystemFsmTaskCompletion,'cfprIdentMetaSystemFsmTaskFlags':cfprIdentMetaSystemFsmTaskFlags,'cfprIdentMetaSystemFsmTaskItem':cfprIdentMetaSystemFsmTaskItem,'cfprIdentMetaSystemFsmTaskSeqId':cfprIdentMetaSystemFsmTaskSeqId,'cfprIdentMetaVerseTable':cfprIdentMetaVerseTable,'cfprIdentMetaVerseEntry':cfprIdentMetaVerseEntry,_N:cfprIdentMetaVerseInstanceId,'cfprIdentMetaVerseDn':cfprIdentMetaVerseDn,'cfprIdentMetaVerseRn':cfprIdentMetaVerseRn,'cfprIdentRequestEpTable':cfprIdentRequestEpTable,'cfprIdentRequestEpEntry':cfprIdentRequestEpEntry,_O:cfprIdentRequestEpInstanceId,'cfprIdentRequestEpDn':cfprIdentRequestEpDn,'cfprIdentRequestEpRn':cfprIdentRequestEpRn,'cfprIdentRequestEpReqDn':cfprIdentRequestEpReqDn,'cfprIdentRequestEpReqId':cfprIdentRequestEpReqId,'cfprIdentSysInfoTable':cfprIdentSysInfoTable,'cfprIdentSysInfoEntry':cfprIdentSysInfoEntry,_P:cfprIdentSysInfoInstanceId,'cfprIdentSysInfoDn':cfprIdentSysInfoDn,'cfprIdentSysInfoRn':cfprIdentSysInfoRn,'cfprIdentSysInfoGeneration':cfprIdentSysInfoGeneration,'cfprIdentSysInfoIsFirstSync':cfprIdentSysInfoIsFirstSync,'cfprIdentSysInfoIsSync':cfprIdentSysInfoIsSync,'cfprIdentSysInfoIsSyncAllowed':cfprIdentSysInfoIsSyncAllowed,'cfprIdentSysInfoFprcGeneration':cfprIdentSysInfoFprcGeneration})