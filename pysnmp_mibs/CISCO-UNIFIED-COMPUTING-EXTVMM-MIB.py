_m='cucsExtvmmVMNetworkSetsInstanceId'
_l='cucsExtvmmVMNetworkDefinitionInstanceId'
_k='cucsExtvmmVMNetworkInstanceId'
_j='cucsExtvmmVMNDRefInstanceId'
_i='cucsExtvmmUpLinkPPInstanceId'
_h='cucsExtvmmNetworkSetsFsmTaskInstanceId'
_g='cucsExtvmmNetworkSetsFsmStageInstanceId'
_f='cucsExtvmmNetworkSetsFsmInstanceId'
_e='cucsExtvmmNetworkSetsInstanceId'
_d='cucsExtvmmFabricNetworkDefinitionInstanceId'
_c='cucsExtvmmFabricNetworkInstanceId'
_b='cucsExtvmmFNDReferenceInstanceId'
_a='cucsExtvmmSwitchDelTaskFsmStageInstanceId'
_Z='cucsExtvmmSwitchDelTaskFsmInstanceId'
_Y='cucsExtvmmProviderFsmStageInstanceId'
_X='cucsExtvmmProviderFsmInstanceId'
_W='cucsExtvmmMasterExtKeyFsmStageInstanceId'
_V='cucsExtvmmMasterExtKeyFsmInstanceId'
_U='cucsExtvmmKeyStoreFsmStageInstanceId'
_T='cucsExtvmmKeyStoreFsmInstanceId'
_S='cucsExtvmmEpFsmStageInstanceId'
_R='cucsExtvmmEpFsmInstanceId'
_Q='cucsExtvmmSwitchSetInstanceId'
_P='cucsExtvmmEpFsmTaskInstanceId'
_O='cucsExtvmmSwitchDelTaskFsmTaskInstanceId'
_N='cucsExtvmmSwitchDelTaskInstanceId'
_M='cucsExtvmmProviderFsmTaskInstanceId'
_L='cucsExtvmmProviderInstanceId'
_K='cucsExtvmmMasterExtKeyFsmTaskInstanceId'
_J='cucsExtvmmMasterExtKeyInstanceId'
_I='cucsExtvmmKeyStoreFsmTaskInstanceId'
_H='cucsExtvmmKeyStoreInstanceId'
_G='cucsExtvmmKeyRingInstanceId'
_F='cucsExtvmmKeyInstInstanceId'
_E='cucsExtvmmEpInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-EXTVMM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsCommFilePathProtocol,CucsConditionRemoteInvRslt,CucsExtvmmEpFsmCurrentFsm,CucsExtvmmEpFsmStageName,CucsExtvmmEpFsmTaskItem,CucsExtvmmFabricNetworkType,CucsExtvmmKeyStoreFsmCurrentFsm,CucsExtvmmKeyStoreFsmStageName,CucsExtvmmKeyStoreFsmTaskItem,CucsExtvmmMasterExtKeyFsmCurrentFsm,CucsExtvmmMasterExtKeyFsmStageName,CucsExtvmmMasterExtKeyFsmTaskItem,CucsExtvmmNetworkSetConfigQualifier,CucsExtvmmNetworkSetsFsmCurrentFsm,CucsExtvmmNetworkSetsFsmStageName,CucsExtvmmNetworkSetsFsmTaskItem,CucsExtvmmProviderFsmCurrentFsm,CucsExtvmmProviderFsmStageName,CucsExtvmmProviderFsmTaskItem,CucsExtvmmProviderVendorType,CucsExtvmmRefOperState,CucsExtvmmSwitchDelTaskFsmCurrentFsm,CucsExtvmmSwitchDelTaskFsmStageName,CucsExtvmmSwitchDelTaskFsmTaskItem,CucsExtvmmVcVersion,CucsExtvmmVnicType,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsCommFilePathProtocol','CucsConditionRemoteInvRslt','CucsExtvmmEpFsmCurrentFsm','CucsExtvmmEpFsmStageName','CucsExtvmmEpFsmTaskItem','CucsExtvmmFabricNetworkType','CucsExtvmmKeyStoreFsmCurrentFsm','CucsExtvmmKeyStoreFsmStageName','CucsExtvmmKeyStoreFsmTaskItem','CucsExtvmmMasterExtKeyFsmCurrentFsm','CucsExtvmmMasterExtKeyFsmStageName','CucsExtvmmMasterExtKeyFsmTaskItem','CucsExtvmmNetworkSetConfigQualifier','CucsExtvmmNetworkSetsFsmCurrentFsm','CucsExtvmmNetworkSetsFsmStageName','CucsExtvmmNetworkSetsFsmTaskItem','CucsExtvmmProviderFsmCurrentFsm','CucsExtvmmProviderFsmStageName','CucsExtvmmProviderFsmTaskItem','CucsExtvmmProviderVendorType','CucsExtvmmRefOperState','CucsExtvmmSwitchDelTaskFsmCurrentFsm','CucsExtvmmSwitchDelTaskFsmStageName','CucsExtvmmSwitchDelTaskFsmTaskItem','CucsExtvmmVcVersion','CucsExtvmmVnicType','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsExtvmmObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,18))
_CucsExtvmmEpTable_Object=MibTable
cucsExtvmmEpTable=_CucsExtvmmEpTable_Object((1,3,6,1,4,1,9,9,719,1,18,1))
if mibBuilder.loadTexts:cucsExtvmmEpTable.setStatus(_A)
_CucsExtvmmEpEntry_Object=MibTableRow
cucsExtvmmEpEntry=_CucsExtvmmEpEntry_Object((1,3,6,1,4,1,9,9,719,1,18,1,1))
cucsExtvmmEpEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsExtvmmEpEntry.setStatus(_A)
_CucsExtvmmEpInstanceId_Type=CucsManagedObjectId
_CucsExtvmmEpInstanceId_Object=MibTableColumn
cucsExtvmmEpInstanceId=_CucsExtvmmEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,1),_CucsExtvmmEpInstanceId_Type())
cucsExtvmmEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmEpInstanceId.setStatus(_A)
_CucsExtvmmEpDn_Type=CucsManagedObjectDn
_CucsExtvmmEpDn_Object=MibTableColumn
cucsExtvmmEpDn=_CucsExtvmmEpDn_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,2),_CucsExtvmmEpDn_Type())
cucsExtvmmEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpDn.setStatus(_A)
_CucsExtvmmEpRn_Type=SnmpAdminString
_CucsExtvmmEpRn_Object=MibTableColumn
cucsExtvmmEpRn=_CucsExtvmmEpRn_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,3),_CucsExtvmmEpRn_Type())
cucsExtvmmEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpRn.setStatus(_A)
_CucsExtvmmEpFsmDescr_Type=SnmpAdminString
_CucsExtvmmEpFsmDescr_Object=MibTableColumn
cucsExtvmmEpFsmDescr=_CucsExtvmmEpFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,4),_CucsExtvmmEpFsmDescr_Type())
cucsExtvmmEpFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmDescr.setStatus(_A)
_CucsExtvmmEpFsmPrev_Type=SnmpAdminString
_CucsExtvmmEpFsmPrev_Object=MibTableColumn
cucsExtvmmEpFsmPrev=_CucsExtvmmEpFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,5),_CucsExtvmmEpFsmPrev_Type())
cucsExtvmmEpFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmPrev.setStatus(_A)
_CucsExtvmmEpFsmProgr_Type=Gauge32
_CucsExtvmmEpFsmProgr_Object=MibTableColumn
cucsExtvmmEpFsmProgr=_CucsExtvmmEpFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,6),_CucsExtvmmEpFsmProgr_Type())
cucsExtvmmEpFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmProgr.setStatus(_A)
_CucsExtvmmEpFsmRmtInvErrCode_Type=Gauge32
_CucsExtvmmEpFsmRmtInvErrCode_Object=MibTableColumn
cucsExtvmmEpFsmRmtInvErrCode=_CucsExtvmmEpFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,7),_CucsExtvmmEpFsmRmtInvErrCode_Type())
cucsExtvmmEpFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmRmtInvErrCode.setStatus(_A)
_CucsExtvmmEpFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsExtvmmEpFsmRmtInvErrDescr_Object=MibTableColumn
cucsExtvmmEpFsmRmtInvErrDescr=_CucsExtvmmEpFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,8),_CucsExtvmmEpFsmRmtInvErrDescr_Type())
cucsExtvmmEpFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmRmtInvErrDescr.setStatus(_A)
_CucsExtvmmEpFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmEpFsmRmtInvRslt_Object=MibTableColumn
cucsExtvmmEpFsmRmtInvRslt=_CucsExtvmmEpFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,9),_CucsExtvmmEpFsmRmtInvRslt_Type())
cucsExtvmmEpFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmRmtInvRslt.setStatus(_A)
_CucsExtvmmEpFsmStageDescr_Type=SnmpAdminString
_CucsExtvmmEpFsmStageDescr_Object=MibTableColumn
cucsExtvmmEpFsmStageDescr=_CucsExtvmmEpFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,10),_CucsExtvmmEpFsmStageDescr_Type())
cucsExtvmmEpFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageDescr.setStatus(_A)
_CucsExtvmmEpFsmStamp_Type=DateAndTime
_CucsExtvmmEpFsmStamp_Object=MibTableColumn
cucsExtvmmEpFsmStamp=_CucsExtvmmEpFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,11),_CucsExtvmmEpFsmStamp_Type())
cucsExtvmmEpFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStamp.setStatus(_A)
_CucsExtvmmEpFsmStatus_Type=SnmpAdminString
_CucsExtvmmEpFsmStatus_Object=MibTableColumn
cucsExtvmmEpFsmStatus=_CucsExtvmmEpFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,12),_CucsExtvmmEpFsmStatus_Type())
cucsExtvmmEpFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStatus.setStatus(_A)
_CucsExtvmmEpFsmTry_Type=Gauge32
_CucsExtvmmEpFsmTry_Object=MibTableColumn
cucsExtvmmEpFsmTry=_CucsExtvmmEpFsmTry_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,13),_CucsExtvmmEpFsmTry_Type())
cucsExtvmmEpFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmTry.setStatus(_A)
_CucsExtvmmEpGenNum_Type=Gauge32
_CucsExtvmmEpGenNum_Object=MibTableColumn
cucsExtvmmEpGenNum=_CucsExtvmmEpGenNum_Object((1,3,6,1,4,1,9,9,719,1,18,1,1,14),_CucsExtvmmEpGenNum_Type())
cucsExtvmmEpGenNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpGenNum.setStatus(_A)
_CucsExtvmmKeyInstTable_Object=MibTable
cucsExtvmmKeyInstTable=_CucsExtvmmKeyInstTable_Object((1,3,6,1,4,1,9,9,719,1,18,2))
if mibBuilder.loadTexts:cucsExtvmmKeyInstTable.setStatus(_A)
_CucsExtvmmKeyInstEntry_Object=MibTableRow
cucsExtvmmKeyInstEntry=_CucsExtvmmKeyInstEntry_Object((1,3,6,1,4,1,9,9,719,1,18,2,1))
cucsExtvmmKeyInstEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsExtvmmKeyInstEntry.setStatus(_A)
_CucsExtvmmKeyInstInstanceId_Type=CucsManagedObjectId
_CucsExtvmmKeyInstInstanceId_Object=MibTableColumn
cucsExtvmmKeyInstInstanceId=_CucsExtvmmKeyInstInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,2,1,1),_CucsExtvmmKeyInstInstanceId_Type())
cucsExtvmmKeyInstInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmKeyInstInstanceId.setStatus(_A)
_CucsExtvmmKeyInstDn_Type=CucsManagedObjectDn
_CucsExtvmmKeyInstDn_Object=MibTableColumn
cucsExtvmmKeyInstDn=_CucsExtvmmKeyInstDn_Object((1,3,6,1,4,1,9,9,719,1,18,2,1,2),_CucsExtvmmKeyInstDn_Type())
cucsExtvmmKeyInstDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyInstDn.setStatus(_A)
_CucsExtvmmKeyInstRn_Type=SnmpAdminString
_CucsExtvmmKeyInstRn_Object=MibTableColumn
cucsExtvmmKeyInstRn=_CucsExtvmmKeyInstRn_Object((1,3,6,1,4,1,9,9,719,1,18,2,1,3),_CucsExtvmmKeyInstRn_Type())
cucsExtvmmKeyInstRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyInstRn.setStatus(_A)
_CucsExtvmmKeyInstInst_Type=Gauge32
_CucsExtvmmKeyInstInst_Object=MibTableColumn
cucsExtvmmKeyInstInst=_CucsExtvmmKeyInstInst_Object((1,3,6,1,4,1,9,9,719,1,18,2,1,4),_CucsExtvmmKeyInstInst_Type())
cucsExtvmmKeyInstInst.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyInstInst.setStatus(_A)
_CucsExtvmmKeyInstKey_Type=SnmpAdminString
_CucsExtvmmKeyInstKey_Object=MibTableColumn
cucsExtvmmKeyInstKey=_CucsExtvmmKeyInstKey_Object((1,3,6,1,4,1,9,9,719,1,18,2,1,5),_CucsExtvmmKeyInstKey_Type())
cucsExtvmmKeyInstKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyInstKey.setStatus(_A)
_CucsExtvmmKeyRingTable_Object=MibTable
cucsExtvmmKeyRingTable=_CucsExtvmmKeyRingTable_Object((1,3,6,1,4,1,9,9,719,1,18,3))
if mibBuilder.loadTexts:cucsExtvmmKeyRingTable.setStatus(_A)
_CucsExtvmmKeyRingEntry_Object=MibTableRow
cucsExtvmmKeyRingEntry=_CucsExtvmmKeyRingEntry_Object((1,3,6,1,4,1,9,9,719,1,18,3,1))
cucsExtvmmKeyRingEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsExtvmmKeyRingEntry.setStatus(_A)
_CucsExtvmmKeyRingInstanceId_Type=CucsManagedObjectId
_CucsExtvmmKeyRingInstanceId_Object=MibTableColumn
cucsExtvmmKeyRingInstanceId=_CucsExtvmmKeyRingInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,3,1,1),_CucsExtvmmKeyRingInstanceId_Type())
cucsExtvmmKeyRingInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmKeyRingInstanceId.setStatus(_A)
_CucsExtvmmKeyRingDn_Type=CucsManagedObjectDn
_CucsExtvmmKeyRingDn_Object=MibTableColumn
cucsExtvmmKeyRingDn=_CucsExtvmmKeyRingDn_Object((1,3,6,1,4,1,9,9,719,1,18,3,1,2),_CucsExtvmmKeyRingDn_Type())
cucsExtvmmKeyRingDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyRingDn.setStatus(_A)
_CucsExtvmmKeyRingRn_Type=SnmpAdminString
_CucsExtvmmKeyRingRn_Object=MibTableColumn
cucsExtvmmKeyRingRn=_CucsExtvmmKeyRingRn_Object((1,3,6,1,4,1,9,9,719,1,18,3,1,3),_CucsExtvmmKeyRingRn_Type())
cucsExtvmmKeyRingRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyRingRn.setStatus(_A)
_CucsExtvmmKeyRingCertFile_Type=SnmpAdminString
_CucsExtvmmKeyRingCertFile_Object=MibTableColumn
cucsExtvmmKeyRingCertFile=_CucsExtvmmKeyRingCertFile_Object((1,3,6,1,4,1,9,9,719,1,18,3,1,4),_CucsExtvmmKeyRingCertFile_Type())
cucsExtvmmKeyRingCertFile.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyRingCertFile.setStatus(_A)
_CucsExtvmmKeyRingLocation_Type=CucsCommFilePathProtocol
_CucsExtvmmKeyRingLocation_Object=MibTableColumn
cucsExtvmmKeyRingLocation=_CucsExtvmmKeyRingLocation_Object((1,3,6,1,4,1,9,9,719,1,18,3,1,5),_CucsExtvmmKeyRingLocation_Type())
cucsExtvmmKeyRingLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyRingLocation.setStatus(_A)
_CucsExtvmmKeyRingName_Type=SnmpAdminString
_CucsExtvmmKeyRingName_Object=MibTableColumn
cucsExtvmmKeyRingName=_CucsExtvmmKeyRingName_Object((1,3,6,1,4,1,9,9,719,1,18,3,1,6),_CucsExtvmmKeyRingName_Type())
cucsExtvmmKeyRingName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyRingName.setStatus(_A)
_CucsExtvmmKeyRingPath_Type=SnmpAdminString
_CucsExtvmmKeyRingPath_Object=MibTableColumn
cucsExtvmmKeyRingPath=_CucsExtvmmKeyRingPath_Object((1,3,6,1,4,1,9,9,719,1,18,3,1,7),_CucsExtvmmKeyRingPath_Type())
cucsExtvmmKeyRingPath.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyRingPath.setStatus(_A)
_CucsExtvmmKeyStoreTable_Object=MibTable
cucsExtvmmKeyStoreTable=_CucsExtvmmKeyStoreTable_Object((1,3,6,1,4,1,9,9,719,1,18,4))
if mibBuilder.loadTexts:cucsExtvmmKeyStoreTable.setStatus(_A)
_CucsExtvmmKeyStoreEntry_Object=MibTableRow
cucsExtvmmKeyStoreEntry=_CucsExtvmmKeyStoreEntry_Object((1,3,6,1,4,1,9,9,719,1,18,4,1))
cucsExtvmmKeyStoreEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsExtvmmKeyStoreEntry.setStatus(_A)
_CucsExtvmmKeyStoreInstanceId_Type=CucsManagedObjectId
_CucsExtvmmKeyStoreInstanceId_Object=MibTableColumn
cucsExtvmmKeyStoreInstanceId=_CucsExtvmmKeyStoreInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,1),_CucsExtvmmKeyStoreInstanceId_Type())
cucsExtvmmKeyStoreInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreInstanceId.setStatus(_A)
_CucsExtvmmKeyStoreDn_Type=CucsManagedObjectDn
_CucsExtvmmKeyStoreDn_Object=MibTableColumn
cucsExtvmmKeyStoreDn=_CucsExtvmmKeyStoreDn_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,2),_CucsExtvmmKeyStoreDn_Type())
cucsExtvmmKeyStoreDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreDn.setStatus(_A)
_CucsExtvmmKeyStoreRn_Type=SnmpAdminString
_CucsExtvmmKeyStoreRn_Object=MibTableColumn
cucsExtvmmKeyStoreRn=_CucsExtvmmKeyStoreRn_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,3),_CucsExtvmmKeyStoreRn_Type())
cucsExtvmmKeyStoreRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreRn.setStatus(_A)
_CucsExtvmmKeyStoreFsmDescr_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmDescr_Object=MibTableColumn
cucsExtvmmKeyStoreFsmDescr=_CucsExtvmmKeyStoreFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,4),_CucsExtvmmKeyStoreFsmDescr_Type())
cucsExtvmmKeyStoreFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmDescr.setStatus(_A)
_CucsExtvmmKeyStoreFsmPrev_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmPrev_Object=MibTableColumn
cucsExtvmmKeyStoreFsmPrev=_CucsExtvmmKeyStoreFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,5),_CucsExtvmmKeyStoreFsmPrev_Type())
cucsExtvmmKeyStoreFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmPrev.setStatus(_A)
_CucsExtvmmKeyStoreFsmProgr_Type=Gauge32
_CucsExtvmmKeyStoreFsmProgr_Object=MibTableColumn
cucsExtvmmKeyStoreFsmProgr=_CucsExtvmmKeyStoreFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,6),_CucsExtvmmKeyStoreFsmProgr_Type())
cucsExtvmmKeyStoreFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmProgr.setStatus(_A)
_CucsExtvmmKeyStoreFsmRmtInvErrCode_Type=Gauge32
_CucsExtvmmKeyStoreFsmRmtInvErrCode_Object=MibTableColumn
cucsExtvmmKeyStoreFsmRmtInvErrCode=_CucsExtvmmKeyStoreFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,7),_CucsExtvmmKeyStoreFsmRmtInvErrCode_Type())
cucsExtvmmKeyStoreFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmRmtInvErrCode.setStatus(_A)
_CucsExtvmmKeyStoreFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmRmtInvErrDescr_Object=MibTableColumn
cucsExtvmmKeyStoreFsmRmtInvErrDescr=_CucsExtvmmKeyStoreFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,8),_CucsExtvmmKeyStoreFsmRmtInvErrDescr_Type())
cucsExtvmmKeyStoreFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmRmtInvErrDescr.setStatus(_A)
_CucsExtvmmKeyStoreFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmKeyStoreFsmRmtInvRslt_Object=MibTableColumn
cucsExtvmmKeyStoreFsmRmtInvRslt=_CucsExtvmmKeyStoreFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,9),_CucsExtvmmKeyStoreFsmRmtInvRslt_Type())
cucsExtvmmKeyStoreFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmRmtInvRslt.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageDescr_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmStageDescr_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageDescr=_CucsExtvmmKeyStoreFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,10),_CucsExtvmmKeyStoreFsmStageDescr_Type())
cucsExtvmmKeyStoreFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageDescr.setStatus(_A)
_CucsExtvmmKeyStoreFsmStamp_Type=DateAndTime
_CucsExtvmmKeyStoreFsmStamp_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStamp=_CucsExtvmmKeyStoreFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,11),_CucsExtvmmKeyStoreFsmStamp_Type())
cucsExtvmmKeyStoreFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStamp.setStatus(_A)
_CucsExtvmmKeyStoreFsmStatus_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmStatus_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStatus=_CucsExtvmmKeyStoreFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,12),_CucsExtvmmKeyStoreFsmStatus_Type())
cucsExtvmmKeyStoreFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStatus.setStatus(_A)
_CucsExtvmmKeyStoreFsmTry_Type=Gauge32
_CucsExtvmmKeyStoreFsmTry_Object=MibTableColumn
cucsExtvmmKeyStoreFsmTry=_CucsExtvmmKeyStoreFsmTry_Object((1,3,6,1,4,1,9,9,719,1,18,4,1,13),_CucsExtvmmKeyStoreFsmTry_Type())
cucsExtvmmKeyStoreFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTry.setStatus(_A)
_CucsExtvmmKeyStoreFsmTaskTable_Object=MibTable
cucsExtvmmKeyStoreFsmTaskTable=_CucsExtvmmKeyStoreFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,18,5))
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTaskTable.setStatus(_A)
_CucsExtvmmKeyStoreFsmTaskEntry_Object=MibTableRow
cucsExtvmmKeyStoreFsmTaskEntry=_CucsExtvmmKeyStoreFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,18,5,1))
cucsExtvmmKeyStoreFsmTaskEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTaskEntry.setStatus(_A)
_CucsExtvmmKeyStoreFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsExtvmmKeyStoreFsmTaskInstanceId_Object=MibTableColumn
cucsExtvmmKeyStoreFsmTaskInstanceId=_CucsExtvmmKeyStoreFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,5,1,1),_CucsExtvmmKeyStoreFsmTaskInstanceId_Type())
cucsExtvmmKeyStoreFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTaskInstanceId.setStatus(_A)
_CucsExtvmmKeyStoreFsmTaskDn_Type=CucsManagedObjectDn
_CucsExtvmmKeyStoreFsmTaskDn_Object=MibTableColumn
cucsExtvmmKeyStoreFsmTaskDn=_CucsExtvmmKeyStoreFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,18,5,1,2),_CucsExtvmmKeyStoreFsmTaskDn_Type())
cucsExtvmmKeyStoreFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTaskDn.setStatus(_A)
_CucsExtvmmKeyStoreFsmTaskRn_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmTaskRn_Object=MibTableColumn
cucsExtvmmKeyStoreFsmTaskRn=_CucsExtvmmKeyStoreFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,18,5,1,3),_CucsExtvmmKeyStoreFsmTaskRn_Type())
cucsExtvmmKeyStoreFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTaskRn.setStatus(_A)
_CucsExtvmmKeyStoreFsmTaskCompletion_Type=CucsFsmCompletion
_CucsExtvmmKeyStoreFsmTaskCompletion_Object=MibTableColumn
cucsExtvmmKeyStoreFsmTaskCompletion=_CucsExtvmmKeyStoreFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,18,5,1,4),_CucsExtvmmKeyStoreFsmTaskCompletion_Type())
cucsExtvmmKeyStoreFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTaskCompletion.setStatus(_A)
_CucsExtvmmKeyStoreFsmTaskFlags_Type=CucsFsmFlags
_CucsExtvmmKeyStoreFsmTaskFlags_Object=MibTableColumn
cucsExtvmmKeyStoreFsmTaskFlags=_CucsExtvmmKeyStoreFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,18,5,1,5),_CucsExtvmmKeyStoreFsmTaskFlags_Type())
cucsExtvmmKeyStoreFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTaskFlags.setStatus(_A)
_CucsExtvmmKeyStoreFsmTaskItem_Type=CucsExtvmmKeyStoreFsmTaskItem
_CucsExtvmmKeyStoreFsmTaskItem_Object=MibTableColumn
cucsExtvmmKeyStoreFsmTaskItem=_CucsExtvmmKeyStoreFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,18,5,1,6),_CucsExtvmmKeyStoreFsmTaskItem_Type())
cucsExtvmmKeyStoreFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTaskItem.setStatus(_A)
_CucsExtvmmKeyStoreFsmTaskSeqId_Type=Gauge32
_CucsExtvmmKeyStoreFsmTaskSeqId_Object=MibTableColumn
cucsExtvmmKeyStoreFsmTaskSeqId=_CucsExtvmmKeyStoreFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,18,5,1,7),_CucsExtvmmKeyStoreFsmTaskSeqId_Type())
cucsExtvmmKeyStoreFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTaskSeqId.setStatus(_A)
_CucsExtvmmMasterExtKeyTable_Object=MibTable
cucsExtvmmMasterExtKeyTable=_CucsExtvmmMasterExtKeyTable_Object((1,3,6,1,4,1,9,9,719,1,18,6))
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyTable.setStatus(_A)
_CucsExtvmmMasterExtKeyEntry_Object=MibTableRow
cucsExtvmmMasterExtKeyEntry=_CucsExtvmmMasterExtKeyEntry_Object((1,3,6,1,4,1,9,9,719,1,18,6,1))
cucsExtvmmMasterExtKeyEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyEntry.setStatus(_A)
_CucsExtvmmMasterExtKeyInstanceId_Type=CucsManagedObjectId
_CucsExtvmmMasterExtKeyInstanceId_Object=MibTableColumn
cucsExtvmmMasterExtKeyInstanceId=_CucsExtvmmMasterExtKeyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,1),_CucsExtvmmMasterExtKeyInstanceId_Type())
cucsExtvmmMasterExtKeyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyInstanceId.setStatus(_A)
_CucsExtvmmMasterExtKeyDn_Type=CucsManagedObjectDn
_CucsExtvmmMasterExtKeyDn_Object=MibTableColumn
cucsExtvmmMasterExtKeyDn=_CucsExtvmmMasterExtKeyDn_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,2),_CucsExtvmmMasterExtKeyDn_Type())
cucsExtvmmMasterExtKeyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyDn.setStatus(_A)
_CucsExtvmmMasterExtKeyRn_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyRn_Object=MibTableColumn
cucsExtvmmMasterExtKeyRn=_CucsExtvmmMasterExtKeyRn_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,3),_CucsExtvmmMasterExtKeyRn_Type())
cucsExtvmmMasterExtKeyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyRn.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmDescr_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmDescr_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmDescr=_CucsExtvmmMasterExtKeyFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,4),_CucsExtvmmMasterExtKeyFsmDescr_Type())
cucsExtvmmMasterExtKeyFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmDescr.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmPrev_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmPrev_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmPrev=_CucsExtvmmMasterExtKeyFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,5),_CucsExtvmmMasterExtKeyFsmPrev_Type())
cucsExtvmmMasterExtKeyFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmPrev.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmProgr_Type=Gauge32
_CucsExtvmmMasterExtKeyFsmProgr_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmProgr=_CucsExtvmmMasterExtKeyFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,6),_CucsExtvmmMasterExtKeyFsmProgr_Type())
cucsExtvmmMasterExtKeyFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmProgr.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmRmtInvErrCode_Type=Gauge32
_CucsExtvmmMasterExtKeyFsmRmtInvErrCode_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtInvErrCode=_CucsExtvmmMasterExtKeyFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,7),_CucsExtvmmMasterExtKeyFsmRmtInvErrCode_Type())
cucsExtvmmMasterExtKeyFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmRmtInvErrCode.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmRmtInvErrDescr_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtInvErrDescr=_CucsExtvmmMasterExtKeyFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,8),_CucsExtvmmMasterExtKeyFsmRmtInvErrDescr_Type())
cucsExtvmmMasterExtKeyFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmRmtInvErrDescr.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmMasterExtKeyFsmRmtInvRslt_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtInvRslt=_CucsExtvmmMasterExtKeyFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,9),_CucsExtvmmMasterExtKeyFsmRmtInvRslt_Type())
cucsExtvmmMasterExtKeyFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmRmtInvRslt.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageDescr_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmStageDescr_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageDescr=_CucsExtvmmMasterExtKeyFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,10),_CucsExtvmmMasterExtKeyFsmStageDescr_Type())
cucsExtvmmMasterExtKeyFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageDescr.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStamp_Type=DateAndTime
_CucsExtvmmMasterExtKeyFsmStamp_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStamp=_CucsExtvmmMasterExtKeyFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,11),_CucsExtvmmMasterExtKeyFsmStamp_Type())
cucsExtvmmMasterExtKeyFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStamp.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStatus_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmStatus_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStatus=_CucsExtvmmMasterExtKeyFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,12),_CucsExtvmmMasterExtKeyFsmStatus_Type())
cucsExtvmmMasterExtKeyFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStatus.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTry_Type=Gauge32
_CucsExtvmmMasterExtKeyFsmTry_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmTry=_CucsExtvmmMasterExtKeyFsmTry_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,13),_CucsExtvmmMasterExtKeyFsmTry_Type())
cucsExtvmmMasterExtKeyFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTry.setStatus(_A)
_CucsExtvmmMasterExtKeyKey_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyKey_Object=MibTableColumn
cucsExtvmmMasterExtKeyKey=_CucsExtvmmMasterExtKeyKey_Object((1,3,6,1,4,1,9,9,719,1,18,6,1,14),_CucsExtvmmMasterExtKeyKey_Type())
cucsExtvmmMasterExtKeyKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyKey.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTaskTable_Object=MibTable
cucsExtvmmMasterExtKeyFsmTaskTable=_CucsExtvmmMasterExtKeyFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,18,7))
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTaskTable.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTaskEntry_Object=MibTableRow
cucsExtvmmMasterExtKeyFsmTaskEntry=_CucsExtvmmMasterExtKeyFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,18,7,1))
cucsExtvmmMasterExtKeyFsmTaskEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTaskEntry.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsExtvmmMasterExtKeyFsmTaskInstanceId_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskInstanceId=_CucsExtvmmMasterExtKeyFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,7,1,1),_CucsExtvmmMasterExtKeyFsmTaskInstanceId_Type())
cucsExtvmmMasterExtKeyFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTaskInstanceId.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTaskDn_Type=CucsManagedObjectDn
_CucsExtvmmMasterExtKeyFsmTaskDn_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskDn=_CucsExtvmmMasterExtKeyFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,18,7,1,2),_CucsExtvmmMasterExtKeyFsmTaskDn_Type())
cucsExtvmmMasterExtKeyFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTaskDn.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTaskRn_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmTaskRn_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskRn=_CucsExtvmmMasterExtKeyFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,18,7,1,3),_CucsExtvmmMasterExtKeyFsmTaskRn_Type())
cucsExtvmmMasterExtKeyFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTaskRn.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTaskCompletion_Type=CucsFsmCompletion
_CucsExtvmmMasterExtKeyFsmTaskCompletion_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskCompletion=_CucsExtvmmMasterExtKeyFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,18,7,1,4),_CucsExtvmmMasterExtKeyFsmTaskCompletion_Type())
cucsExtvmmMasterExtKeyFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTaskCompletion.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTaskFlags_Type=CucsFsmFlags
_CucsExtvmmMasterExtKeyFsmTaskFlags_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskFlags=_CucsExtvmmMasterExtKeyFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,18,7,1,5),_CucsExtvmmMasterExtKeyFsmTaskFlags_Type())
cucsExtvmmMasterExtKeyFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTaskFlags.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTaskItem_Type=CucsExtvmmMasterExtKeyFsmTaskItem
_CucsExtvmmMasterExtKeyFsmTaskItem_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskItem=_CucsExtvmmMasterExtKeyFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,18,7,1,6),_CucsExtvmmMasterExtKeyFsmTaskItem_Type())
cucsExtvmmMasterExtKeyFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTaskItem.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTaskSeqId_Type=Gauge32
_CucsExtvmmMasterExtKeyFsmTaskSeqId_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskSeqId=_CucsExtvmmMasterExtKeyFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,18,7,1,7),_CucsExtvmmMasterExtKeyFsmTaskSeqId_Type())
cucsExtvmmMasterExtKeyFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTaskSeqId.setStatus(_A)
_CucsExtvmmProviderTable_Object=MibTable
cucsExtvmmProviderTable=_CucsExtvmmProviderTable_Object((1,3,6,1,4,1,9,9,719,1,18,8))
if mibBuilder.loadTexts:cucsExtvmmProviderTable.setStatus(_A)
_CucsExtvmmProviderEntry_Object=MibTableRow
cucsExtvmmProviderEntry=_CucsExtvmmProviderEntry_Object((1,3,6,1,4,1,9,9,719,1,18,8,1))
cucsExtvmmProviderEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsExtvmmProviderEntry.setStatus(_A)
_CucsExtvmmProviderInstanceId_Type=CucsManagedObjectId
_CucsExtvmmProviderInstanceId_Object=MibTableColumn
cucsExtvmmProviderInstanceId=_CucsExtvmmProviderInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,1),_CucsExtvmmProviderInstanceId_Type())
cucsExtvmmProviderInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmProviderInstanceId.setStatus(_A)
_CucsExtvmmProviderDn_Type=CucsManagedObjectDn
_CucsExtvmmProviderDn_Object=MibTableColumn
cucsExtvmmProviderDn=_CucsExtvmmProviderDn_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,2),_CucsExtvmmProviderDn_Type())
cucsExtvmmProviderDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderDn.setStatus(_A)
_CucsExtvmmProviderRn_Type=SnmpAdminString
_CucsExtvmmProviderRn_Object=MibTableColumn
cucsExtvmmProviderRn=_CucsExtvmmProviderRn_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,3),_CucsExtvmmProviderRn_Type())
cucsExtvmmProviderRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderRn.setStatus(_A)
_CucsExtvmmProviderCert_Type=SnmpAdminString
_CucsExtvmmProviderCert_Object=MibTableColumn
cucsExtvmmProviderCert=_CucsExtvmmProviderCert_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,4),_CucsExtvmmProviderCert_Type())
cucsExtvmmProviderCert.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderCert.setStatus(_A)
_CucsExtvmmProviderDescr_Type=SnmpAdminString
_CucsExtvmmProviderDescr_Object=MibTableColumn
cucsExtvmmProviderDescr=_CucsExtvmmProviderDescr_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,5),_CucsExtvmmProviderDescr_Type())
cucsExtvmmProviderDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderDescr.setStatus(_A)
_CucsExtvmmProviderFsmDescr_Type=SnmpAdminString
_CucsExtvmmProviderFsmDescr_Object=MibTableColumn
cucsExtvmmProviderFsmDescr=_CucsExtvmmProviderFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,6),_CucsExtvmmProviderFsmDescr_Type())
cucsExtvmmProviderFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmDescr.setStatus(_A)
_CucsExtvmmProviderFsmPrev_Type=SnmpAdminString
_CucsExtvmmProviderFsmPrev_Object=MibTableColumn
cucsExtvmmProviderFsmPrev=_CucsExtvmmProviderFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,7),_CucsExtvmmProviderFsmPrev_Type())
cucsExtvmmProviderFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmPrev.setStatus(_A)
_CucsExtvmmProviderFsmProgr_Type=Gauge32
_CucsExtvmmProviderFsmProgr_Object=MibTableColumn
cucsExtvmmProviderFsmProgr=_CucsExtvmmProviderFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,8),_CucsExtvmmProviderFsmProgr_Type())
cucsExtvmmProviderFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmProgr.setStatus(_A)
_CucsExtvmmProviderFsmRmtInvErrCode_Type=Gauge32
_CucsExtvmmProviderFsmRmtInvErrCode_Object=MibTableColumn
cucsExtvmmProviderFsmRmtInvErrCode=_CucsExtvmmProviderFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,9),_CucsExtvmmProviderFsmRmtInvErrCode_Type())
cucsExtvmmProviderFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmRmtInvErrCode.setStatus(_A)
_CucsExtvmmProviderFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsExtvmmProviderFsmRmtInvErrDescr_Object=MibTableColumn
cucsExtvmmProviderFsmRmtInvErrDescr=_CucsExtvmmProviderFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,10),_CucsExtvmmProviderFsmRmtInvErrDescr_Type())
cucsExtvmmProviderFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmRmtInvErrDescr.setStatus(_A)
_CucsExtvmmProviderFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmProviderFsmRmtInvRslt_Object=MibTableColumn
cucsExtvmmProviderFsmRmtInvRslt=_CucsExtvmmProviderFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,11),_CucsExtvmmProviderFsmRmtInvRslt_Type())
cucsExtvmmProviderFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmRmtInvRslt.setStatus(_A)
_CucsExtvmmProviderFsmStageDescr_Type=SnmpAdminString
_CucsExtvmmProviderFsmStageDescr_Object=MibTableColumn
cucsExtvmmProviderFsmStageDescr=_CucsExtvmmProviderFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,12),_CucsExtvmmProviderFsmStageDescr_Type())
cucsExtvmmProviderFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageDescr.setStatus(_A)
_CucsExtvmmProviderFsmStamp_Type=DateAndTime
_CucsExtvmmProviderFsmStamp_Object=MibTableColumn
cucsExtvmmProviderFsmStamp=_CucsExtvmmProviderFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,13),_CucsExtvmmProviderFsmStamp_Type())
cucsExtvmmProviderFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStamp.setStatus(_A)
_CucsExtvmmProviderFsmStatus_Type=SnmpAdminString
_CucsExtvmmProviderFsmStatus_Object=MibTableColumn
cucsExtvmmProviderFsmStatus=_CucsExtvmmProviderFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,14),_CucsExtvmmProviderFsmStatus_Type())
cucsExtvmmProviderFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStatus.setStatus(_A)
_CucsExtvmmProviderFsmTry_Type=Gauge32
_CucsExtvmmProviderFsmTry_Object=MibTableColumn
cucsExtvmmProviderFsmTry=_CucsExtvmmProviderFsmTry_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,15),_CucsExtvmmProviderFsmTry_Type())
cucsExtvmmProviderFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTry.setStatus(_A)
_CucsExtvmmProviderHost_Type=SnmpAdminString
_CucsExtvmmProviderHost_Object=MibTableColumn
cucsExtvmmProviderHost=_CucsExtvmmProviderHost_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,16),_CucsExtvmmProviderHost_Type())
cucsExtvmmProviderHost.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderHost.setStatus(_A)
_CucsExtvmmProviderIntId_Type=SnmpAdminString
_CucsExtvmmProviderIntId_Object=MibTableColumn
cucsExtvmmProviderIntId=_CucsExtvmmProviderIntId_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,17),_CucsExtvmmProviderIntId_Type())
cucsExtvmmProviderIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderIntId.setStatus(_A)
_CucsExtvmmProviderKey_Type=SnmpAdminString
_CucsExtvmmProviderKey_Object=MibTableColumn
cucsExtvmmProviderKey=_CucsExtvmmProviderKey_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,18),_CucsExtvmmProviderKey_Type())
cucsExtvmmProviderKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderKey.setStatus(_A)
_CucsExtvmmProviderName_Type=SnmpAdminString
_CucsExtvmmProviderName_Object=MibTableColumn
cucsExtvmmProviderName=_CucsExtvmmProviderName_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,19),_CucsExtvmmProviderName_Type())
cucsExtvmmProviderName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderName.setStatus(_A)
_CucsExtvmmProviderUuid_Type=SnmpAdminString
_CucsExtvmmProviderUuid_Object=MibTableColumn
cucsExtvmmProviderUuid=_CucsExtvmmProviderUuid_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,20),_CucsExtvmmProviderUuid_Type())
cucsExtvmmProviderUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderUuid.setStatus(_A)
_CucsExtvmmProviderVer_Type=CucsExtvmmVcVersion
_CucsExtvmmProviderVer_Object=MibTableColumn
cucsExtvmmProviderVer=_CucsExtvmmProviderVer_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,21),_CucsExtvmmProviderVer_Type())
cucsExtvmmProviderVer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderVer.setStatus(_A)
_CucsExtvmmProviderVerRaw_Type=SnmpAdminString
_CucsExtvmmProviderVerRaw_Object=MibTableColumn
cucsExtvmmProviderVerRaw=_CucsExtvmmProviderVerRaw_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,22),_CucsExtvmmProviderVerRaw_Type())
cucsExtvmmProviderVerRaw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderVerRaw.setStatus(_A)
_CucsExtvmmProviderPolicyLevel_Type=Gauge32
_CucsExtvmmProviderPolicyLevel_Object=MibTableColumn
cucsExtvmmProviderPolicyLevel=_CucsExtvmmProviderPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,23),_CucsExtvmmProviderPolicyLevel_Type())
cucsExtvmmProviderPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderPolicyLevel.setStatus(_A)
_CucsExtvmmProviderPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtvmmProviderPolicyOwner_Object=MibTableColumn
cucsExtvmmProviderPolicyOwner=_CucsExtvmmProviderPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,24),_CucsExtvmmProviderPolicyOwner_Type())
cucsExtvmmProviderPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderPolicyOwner.setStatus(_A)
_CucsExtvmmProviderPortValue_Type=Gauge32
_CucsExtvmmProviderPortValue_Object=MibTableColumn
cucsExtvmmProviderPortValue=_CucsExtvmmProviderPortValue_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,25),_CucsExtvmmProviderPortValue_Type())
cucsExtvmmProviderPortValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderPortValue.setStatus(_A)
_CucsExtvmmProviderVendorType_Type=CucsExtvmmProviderVendorType
_CucsExtvmmProviderVendorType_Object=MibTableColumn
cucsExtvmmProviderVendorType=_CucsExtvmmProviderVendorType_Object((1,3,6,1,4,1,9,9,719,1,18,8,1,26),_CucsExtvmmProviderVendorType_Type())
cucsExtvmmProviderVendorType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderVendorType.setStatus(_A)
_CucsExtvmmProviderFsmTaskTable_Object=MibTable
cucsExtvmmProviderFsmTaskTable=_CucsExtvmmProviderFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,18,9))
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTaskTable.setStatus(_A)
_CucsExtvmmProviderFsmTaskEntry_Object=MibTableRow
cucsExtvmmProviderFsmTaskEntry=_CucsExtvmmProviderFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,18,9,1))
cucsExtvmmProviderFsmTaskEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTaskEntry.setStatus(_A)
_CucsExtvmmProviderFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsExtvmmProviderFsmTaskInstanceId_Object=MibTableColumn
cucsExtvmmProviderFsmTaskInstanceId=_CucsExtvmmProviderFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,9,1,1),_CucsExtvmmProviderFsmTaskInstanceId_Type())
cucsExtvmmProviderFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTaskInstanceId.setStatus(_A)
_CucsExtvmmProviderFsmTaskDn_Type=CucsManagedObjectDn
_CucsExtvmmProviderFsmTaskDn_Object=MibTableColumn
cucsExtvmmProviderFsmTaskDn=_CucsExtvmmProviderFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,18,9,1,2),_CucsExtvmmProviderFsmTaskDn_Type())
cucsExtvmmProviderFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTaskDn.setStatus(_A)
_CucsExtvmmProviderFsmTaskRn_Type=SnmpAdminString
_CucsExtvmmProviderFsmTaskRn_Object=MibTableColumn
cucsExtvmmProviderFsmTaskRn=_CucsExtvmmProviderFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,18,9,1,3),_CucsExtvmmProviderFsmTaskRn_Type())
cucsExtvmmProviderFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTaskRn.setStatus(_A)
_CucsExtvmmProviderFsmTaskCompletion_Type=CucsFsmCompletion
_CucsExtvmmProviderFsmTaskCompletion_Object=MibTableColumn
cucsExtvmmProviderFsmTaskCompletion=_CucsExtvmmProviderFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,18,9,1,4),_CucsExtvmmProviderFsmTaskCompletion_Type())
cucsExtvmmProviderFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTaskCompletion.setStatus(_A)
_CucsExtvmmProviderFsmTaskFlags_Type=CucsFsmFlags
_CucsExtvmmProviderFsmTaskFlags_Object=MibTableColumn
cucsExtvmmProviderFsmTaskFlags=_CucsExtvmmProviderFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,18,9,1,5),_CucsExtvmmProviderFsmTaskFlags_Type())
cucsExtvmmProviderFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTaskFlags.setStatus(_A)
_CucsExtvmmProviderFsmTaskItem_Type=CucsExtvmmProviderFsmTaskItem
_CucsExtvmmProviderFsmTaskItem_Object=MibTableColumn
cucsExtvmmProviderFsmTaskItem=_CucsExtvmmProviderFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,18,9,1,6),_CucsExtvmmProviderFsmTaskItem_Type())
cucsExtvmmProviderFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTaskItem.setStatus(_A)
_CucsExtvmmProviderFsmTaskSeqId_Type=Gauge32
_CucsExtvmmProviderFsmTaskSeqId_Object=MibTableColumn
cucsExtvmmProviderFsmTaskSeqId=_CucsExtvmmProviderFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,18,9,1,7),_CucsExtvmmProviderFsmTaskSeqId_Type())
cucsExtvmmProviderFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTaskSeqId.setStatus(_A)
_CucsExtvmmSwitchDelTaskTable_Object=MibTable
cucsExtvmmSwitchDelTaskTable=_CucsExtvmmSwitchDelTaskTable_Object((1,3,6,1,4,1,9,9,719,1,18,10))
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskTable.setStatus(_A)
_CucsExtvmmSwitchDelTaskEntry_Object=MibTableRow
cucsExtvmmSwitchDelTaskEntry=_CucsExtvmmSwitchDelTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,18,10,1))
cucsExtvmmSwitchDelTaskEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskEntry.setStatus(_A)
_CucsExtvmmSwitchDelTaskInstanceId_Type=CucsManagedObjectId
_CucsExtvmmSwitchDelTaskInstanceId_Object=MibTableColumn
cucsExtvmmSwitchDelTaskInstanceId=_CucsExtvmmSwitchDelTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,1),_CucsExtvmmSwitchDelTaskInstanceId_Type())
cucsExtvmmSwitchDelTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskInstanceId.setStatus(_A)
_CucsExtvmmSwitchDelTaskDn_Type=CucsManagedObjectDn
_CucsExtvmmSwitchDelTaskDn_Object=MibTableColumn
cucsExtvmmSwitchDelTaskDn=_CucsExtvmmSwitchDelTaskDn_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,2),_CucsExtvmmSwitchDelTaskDn_Type())
cucsExtvmmSwitchDelTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskDn.setStatus(_A)
_CucsExtvmmSwitchDelTaskRn_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskRn_Object=MibTableColumn
cucsExtvmmSwitchDelTaskRn=_CucsExtvmmSwitchDelTaskRn_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,3),_CucsExtvmmSwitchDelTaskRn_Type())
cucsExtvmmSwitchDelTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskRn.setStatus(_A)
_CucsExtvmmSwitchDelTaskCertFile_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskCertFile_Object=MibTableColumn
cucsExtvmmSwitchDelTaskCertFile=_CucsExtvmmSwitchDelTaskCertFile_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,4),_CucsExtvmmSwitchDelTaskCertFile_Type())
cucsExtvmmSwitchDelTaskCertFile.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskCertFile.setStatus(_A)
_CucsExtvmmSwitchDelTaskDcName_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskDcName_Object=MibTableColumn
cucsExtvmmSwitchDelTaskDcName=_CucsExtvmmSwitchDelTaskDcName_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,5),_CucsExtvmmSwitchDelTaskDcName_Type())
cucsExtvmmSwitchDelTaskDcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskDcName.setStatus(_A)
_CucsExtvmmSwitchDelTaskDcOrg_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskDcOrg_Object=MibTableColumn
cucsExtvmmSwitchDelTaskDcOrg=_CucsExtvmmSwitchDelTaskDcOrg_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,6),_CucsExtvmmSwitchDelTaskDcOrg_Type())
cucsExtvmmSwitchDelTaskDcOrg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskDcOrg.setStatus(_A)
_CucsExtvmmSwitchDelTaskDescr_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskDescr_Object=MibTableColumn
cucsExtvmmSwitchDelTaskDescr=_CucsExtvmmSwitchDelTaskDescr_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,7),_CucsExtvmmSwitchDelTaskDescr_Type())
cucsExtvmmSwitchDelTaskDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskDescr.setStatus(_A)
_CucsExtvmmSwitchDelTaskExtKey_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskExtKey_Object=MibTableColumn
cucsExtvmmSwitchDelTaskExtKey=_CucsExtvmmSwitchDelTaskExtKey_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,8),_CucsExtvmmSwitchDelTaskExtKey_Type())
cucsExtvmmSwitchDelTaskExtKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskExtKey.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmDescr_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmDescr_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmDescr=_CucsExtvmmSwitchDelTaskFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,9),_CucsExtvmmSwitchDelTaskFsmDescr_Type())
cucsExtvmmSwitchDelTaskFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmDescr.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmPrev_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmPrev_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmPrev=_CucsExtvmmSwitchDelTaskFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,10),_CucsExtvmmSwitchDelTaskFsmPrev_Type())
cucsExtvmmSwitchDelTaskFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmPrev.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmProgr_Type=Gauge32
_CucsExtvmmSwitchDelTaskFsmProgr_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmProgr=_CucsExtvmmSwitchDelTaskFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,11),_CucsExtvmmSwitchDelTaskFsmProgr_Type())
cucsExtvmmSwitchDelTaskFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmProgr.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmRmtInvErrCode_Type=Gauge32
_CucsExtvmmSwitchDelTaskFsmRmtInvErrCode_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtInvErrCode=_CucsExtvmmSwitchDelTaskFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,12),_CucsExtvmmSwitchDelTaskFsmRmtInvErrCode_Type())
cucsExtvmmSwitchDelTaskFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmRmtInvErrCode.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmRmtInvErrDescr_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr=_CucsExtvmmSwitchDelTaskFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,13),_CucsExtvmmSwitchDelTaskFsmRmtInvErrDescr_Type())
cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmSwitchDelTaskFsmRmtInvRslt_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtInvRslt=_CucsExtvmmSwitchDelTaskFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,14),_CucsExtvmmSwitchDelTaskFsmRmtInvRslt_Type())
cucsExtvmmSwitchDelTaskFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmRmtInvRslt.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageDescr_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmStageDescr_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageDescr=_CucsExtvmmSwitchDelTaskFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,15),_CucsExtvmmSwitchDelTaskFsmStageDescr_Type())
cucsExtvmmSwitchDelTaskFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageDescr.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStamp_Type=DateAndTime
_CucsExtvmmSwitchDelTaskFsmStamp_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStamp=_CucsExtvmmSwitchDelTaskFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,16),_CucsExtvmmSwitchDelTaskFsmStamp_Type())
cucsExtvmmSwitchDelTaskFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStamp.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStatus_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmStatus_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStatus=_CucsExtvmmSwitchDelTaskFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,17),_CucsExtvmmSwitchDelTaskFsmStatus_Type())
cucsExtvmmSwitchDelTaskFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStatus.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTry_Type=Gauge32
_CucsExtvmmSwitchDelTaskFsmTry_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmTry=_CucsExtvmmSwitchDelTaskFsmTry_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,18),_CucsExtvmmSwitchDelTaskFsmTry_Type())
cucsExtvmmSwitchDelTaskFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTry.setStatus(_A)
_CucsExtvmmSwitchDelTaskHost_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskHost_Object=MibTableColumn
cucsExtvmmSwitchDelTaskHost=_CucsExtvmmSwitchDelTaskHost_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,19),_CucsExtvmmSwitchDelTaskHost_Type())
cucsExtvmmSwitchDelTaskHost.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskHost.setStatus(_A)
_CucsExtvmmSwitchDelTaskIntId_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskIntId_Object=MibTableColumn
cucsExtvmmSwitchDelTaskIntId=_CucsExtvmmSwitchDelTaskIntId_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,20),_CucsExtvmmSwitchDelTaskIntId_Type())
cucsExtvmmSwitchDelTaskIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskIntId.setStatus(_A)
_CucsExtvmmSwitchDelTaskKeyInst_Type=Gauge32
_CucsExtvmmSwitchDelTaskKeyInst_Object=MibTableColumn
cucsExtvmmSwitchDelTaskKeyInst=_CucsExtvmmSwitchDelTaskKeyInst_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,21),_CucsExtvmmSwitchDelTaskKeyInst_Type())
cucsExtvmmSwitchDelTaskKeyInst.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskKeyInst.setStatus(_A)
_CucsExtvmmSwitchDelTaskName_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskName_Object=MibTableColumn
cucsExtvmmSwitchDelTaskName=_CucsExtvmmSwitchDelTaskName_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,22),_CucsExtvmmSwitchDelTaskName_Type())
cucsExtvmmSwitchDelTaskName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskName.setStatus(_A)
_CucsExtvmmSwitchDelTaskOrgPath_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskOrgPath_Object=MibTableColumn
cucsExtvmmSwitchDelTaskOrgPath=_CucsExtvmmSwitchDelTaskOrgPath_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,23),_CucsExtvmmSwitchDelTaskOrgPath_Type())
cucsExtvmmSwitchDelTaskOrgPath.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskOrgPath.setStatus(_A)
_CucsExtvmmSwitchDelTaskProvIntId_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskProvIntId_Object=MibTableColumn
cucsExtvmmSwitchDelTaskProvIntId=_CucsExtvmmSwitchDelTaskProvIntId_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,24),_CucsExtvmmSwitchDelTaskProvIntId_Type())
cucsExtvmmSwitchDelTaskProvIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskProvIntId.setStatus(_A)
_CucsExtvmmSwitchDelTaskProvider_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskProvider_Object=MibTableColumn
cucsExtvmmSwitchDelTaskProvider=_CucsExtvmmSwitchDelTaskProvider_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,25),_CucsExtvmmSwitchDelTaskProvider_Type())
cucsExtvmmSwitchDelTaskProvider.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskProvider.setStatus(_A)
_CucsExtvmmSwitchDelTaskSwIntId_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskSwIntId_Object=MibTableColumn
cucsExtvmmSwitchDelTaskSwIntId=_CucsExtvmmSwitchDelTaskSwIntId_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,26),_CucsExtvmmSwitchDelTaskSwIntId_Type())
cucsExtvmmSwitchDelTaskSwIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskSwIntId.setStatus(_A)
_CucsExtvmmSwitchDelTaskSwName_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskSwName_Object=MibTableColumn
cucsExtvmmSwitchDelTaskSwName=_CucsExtvmmSwitchDelTaskSwName_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,27),_CucsExtvmmSwitchDelTaskSwName_Type())
cucsExtvmmSwitchDelTaskSwName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskSwName.setStatus(_A)
_CucsExtvmmSwitchDelTaskPolicyLevel_Type=Gauge32
_CucsExtvmmSwitchDelTaskPolicyLevel_Object=MibTableColumn
cucsExtvmmSwitchDelTaskPolicyLevel=_CucsExtvmmSwitchDelTaskPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,28),_CucsExtvmmSwitchDelTaskPolicyLevel_Type())
cucsExtvmmSwitchDelTaskPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskPolicyLevel.setStatus(_A)
_CucsExtvmmSwitchDelTaskPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtvmmSwitchDelTaskPolicyOwner_Object=MibTableColumn
cucsExtvmmSwitchDelTaskPolicyOwner=_CucsExtvmmSwitchDelTaskPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,29),_CucsExtvmmSwitchDelTaskPolicyOwner_Type())
cucsExtvmmSwitchDelTaskPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskPolicyOwner.setStatus(_A)
_CucsExtvmmSwitchDelTaskPortValue_Type=Gauge32
_CucsExtvmmSwitchDelTaskPortValue_Object=MibTableColumn
cucsExtvmmSwitchDelTaskPortValue=_CucsExtvmmSwitchDelTaskPortValue_Object((1,3,6,1,4,1,9,9,719,1,18,10,1,30),_CucsExtvmmSwitchDelTaskPortValue_Type())
cucsExtvmmSwitchDelTaskPortValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskPortValue.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTaskTable_Object=MibTable
cucsExtvmmSwitchDelTaskFsmTaskTable=_CucsExtvmmSwitchDelTaskFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,18,11))
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTaskTable.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTaskEntry_Object=MibTableRow
cucsExtvmmSwitchDelTaskFsmTaskEntry=_CucsExtvmmSwitchDelTaskFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,18,11,1))
cucsExtvmmSwitchDelTaskFsmTaskEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTaskEntry.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsExtvmmSwitchDelTaskFsmTaskInstanceId_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskInstanceId=_CucsExtvmmSwitchDelTaskFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,11,1,1),_CucsExtvmmSwitchDelTaskFsmTaskInstanceId_Type())
cucsExtvmmSwitchDelTaskFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTaskInstanceId.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTaskDn_Type=CucsManagedObjectDn
_CucsExtvmmSwitchDelTaskFsmTaskDn_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskDn=_CucsExtvmmSwitchDelTaskFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,18,11,1,2),_CucsExtvmmSwitchDelTaskFsmTaskDn_Type())
cucsExtvmmSwitchDelTaskFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTaskDn.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTaskRn_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmTaskRn_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskRn=_CucsExtvmmSwitchDelTaskFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,18,11,1,3),_CucsExtvmmSwitchDelTaskFsmTaskRn_Type())
cucsExtvmmSwitchDelTaskFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTaskRn.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTaskCompletion_Type=CucsFsmCompletion
_CucsExtvmmSwitchDelTaskFsmTaskCompletion_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskCompletion=_CucsExtvmmSwitchDelTaskFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,18,11,1,4),_CucsExtvmmSwitchDelTaskFsmTaskCompletion_Type())
cucsExtvmmSwitchDelTaskFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTaskCompletion.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTaskFlags_Type=CucsFsmFlags
_CucsExtvmmSwitchDelTaskFsmTaskFlags_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskFlags=_CucsExtvmmSwitchDelTaskFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,18,11,1,5),_CucsExtvmmSwitchDelTaskFsmTaskFlags_Type())
cucsExtvmmSwitchDelTaskFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTaskFlags.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTaskItem_Type=CucsExtvmmSwitchDelTaskFsmTaskItem
_CucsExtvmmSwitchDelTaskFsmTaskItem_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskItem=_CucsExtvmmSwitchDelTaskFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,18,11,1,6),_CucsExtvmmSwitchDelTaskFsmTaskItem_Type())
cucsExtvmmSwitchDelTaskFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTaskItem.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTaskSeqId_Type=Gauge32
_CucsExtvmmSwitchDelTaskFsmTaskSeqId_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskSeqId=_CucsExtvmmSwitchDelTaskFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,18,11,1,7),_CucsExtvmmSwitchDelTaskFsmTaskSeqId_Type())
cucsExtvmmSwitchDelTaskFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTaskSeqId.setStatus(_A)
_CucsExtvmmEpFsmTaskTable_Object=MibTable
cucsExtvmmEpFsmTaskTable=_CucsExtvmmEpFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,18,12))
if mibBuilder.loadTexts:cucsExtvmmEpFsmTaskTable.setStatus(_A)
_CucsExtvmmEpFsmTaskEntry_Object=MibTableRow
cucsExtvmmEpFsmTaskEntry=_CucsExtvmmEpFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,18,12,1))
cucsExtvmmEpFsmTaskEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cucsExtvmmEpFsmTaskEntry.setStatus(_A)
_CucsExtvmmEpFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsExtvmmEpFsmTaskInstanceId_Object=MibTableColumn
cucsExtvmmEpFsmTaskInstanceId=_CucsExtvmmEpFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,12,1,1),_CucsExtvmmEpFsmTaskInstanceId_Type())
cucsExtvmmEpFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmEpFsmTaskInstanceId.setStatus(_A)
_CucsExtvmmEpFsmTaskDn_Type=CucsManagedObjectDn
_CucsExtvmmEpFsmTaskDn_Object=MibTableColumn
cucsExtvmmEpFsmTaskDn=_CucsExtvmmEpFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,18,12,1,2),_CucsExtvmmEpFsmTaskDn_Type())
cucsExtvmmEpFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmTaskDn.setStatus(_A)
_CucsExtvmmEpFsmTaskRn_Type=SnmpAdminString
_CucsExtvmmEpFsmTaskRn_Object=MibTableColumn
cucsExtvmmEpFsmTaskRn=_CucsExtvmmEpFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,18,12,1,3),_CucsExtvmmEpFsmTaskRn_Type())
cucsExtvmmEpFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmTaskRn.setStatus(_A)
_CucsExtvmmEpFsmTaskCompletion_Type=CucsFsmCompletion
_CucsExtvmmEpFsmTaskCompletion_Object=MibTableColumn
cucsExtvmmEpFsmTaskCompletion=_CucsExtvmmEpFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,18,12,1,4),_CucsExtvmmEpFsmTaskCompletion_Type())
cucsExtvmmEpFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmTaskCompletion.setStatus(_A)
_CucsExtvmmEpFsmTaskFlags_Type=CucsFsmFlags
_CucsExtvmmEpFsmTaskFlags_Object=MibTableColumn
cucsExtvmmEpFsmTaskFlags=_CucsExtvmmEpFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,18,12,1,5),_CucsExtvmmEpFsmTaskFlags_Type())
cucsExtvmmEpFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmTaskFlags.setStatus(_A)
_CucsExtvmmEpFsmTaskItem_Type=CucsExtvmmEpFsmTaskItem
_CucsExtvmmEpFsmTaskItem_Object=MibTableColumn
cucsExtvmmEpFsmTaskItem=_CucsExtvmmEpFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,18,12,1,6),_CucsExtvmmEpFsmTaskItem_Type())
cucsExtvmmEpFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmTaskItem.setStatus(_A)
_CucsExtvmmEpFsmTaskSeqId_Type=Gauge32
_CucsExtvmmEpFsmTaskSeqId_Object=MibTableColumn
cucsExtvmmEpFsmTaskSeqId=_CucsExtvmmEpFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,18,12,1,7),_CucsExtvmmEpFsmTaskSeqId_Type())
cucsExtvmmEpFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmTaskSeqId.setStatus(_A)
_CucsExtvmmSwitchSetTable_Object=MibTable
cucsExtvmmSwitchSetTable=_CucsExtvmmSwitchSetTable_Object((1,3,6,1,4,1,9,9,719,1,18,13))
if mibBuilder.loadTexts:cucsExtvmmSwitchSetTable.setStatus(_A)
_CucsExtvmmSwitchSetEntry_Object=MibTableRow
cucsExtvmmSwitchSetEntry=_CucsExtvmmSwitchSetEntry_Object((1,3,6,1,4,1,9,9,719,1,18,13,1))
cucsExtvmmSwitchSetEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cucsExtvmmSwitchSetEntry.setStatus(_A)
_CucsExtvmmSwitchSetInstanceId_Type=CucsManagedObjectId
_CucsExtvmmSwitchSetInstanceId_Object=MibTableColumn
cucsExtvmmSwitchSetInstanceId=_CucsExtvmmSwitchSetInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,13,1,1),_CucsExtvmmSwitchSetInstanceId_Type())
cucsExtvmmSwitchSetInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmSwitchSetInstanceId.setStatus(_A)
_CucsExtvmmSwitchSetDn_Type=CucsManagedObjectDn
_CucsExtvmmSwitchSetDn_Object=MibTableColumn
cucsExtvmmSwitchSetDn=_CucsExtvmmSwitchSetDn_Object((1,3,6,1,4,1,9,9,719,1,18,13,1,2),_CucsExtvmmSwitchSetDn_Type())
cucsExtvmmSwitchSetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchSetDn.setStatus(_A)
_CucsExtvmmSwitchSetRn_Type=SnmpAdminString
_CucsExtvmmSwitchSetRn_Object=MibTableColumn
cucsExtvmmSwitchSetRn=_CucsExtvmmSwitchSetRn_Object((1,3,6,1,4,1,9,9,719,1,18,13,1,3),_CucsExtvmmSwitchSetRn_Type())
cucsExtvmmSwitchSetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchSetRn.setStatus(_A)
_CucsExtvmmEpFsmTable_Object=MibTable
cucsExtvmmEpFsmTable=_CucsExtvmmEpFsmTable_Object((1,3,6,1,4,1,9,9,719,1,18,14))
if mibBuilder.loadTexts:cucsExtvmmEpFsmTable.setStatus(_A)
_CucsExtvmmEpFsmEntry_Object=MibTableRow
cucsExtvmmEpFsmEntry=_CucsExtvmmEpFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,18,14,1))
cucsExtvmmEpFsmEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cucsExtvmmEpFsmEntry.setStatus(_A)
_CucsExtvmmEpFsmInstanceId_Type=CucsManagedObjectId
_CucsExtvmmEpFsmInstanceId_Object=MibTableColumn
cucsExtvmmEpFsmInstanceId=_CucsExtvmmEpFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,1),_CucsExtvmmEpFsmInstanceId_Type())
cucsExtvmmEpFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmEpFsmInstanceId.setStatus(_A)
_CucsExtvmmEpFsmDn_Type=CucsManagedObjectDn
_CucsExtvmmEpFsmDn_Object=MibTableColumn
cucsExtvmmEpFsmDn=_CucsExtvmmEpFsmDn_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,2),_CucsExtvmmEpFsmDn_Type())
cucsExtvmmEpFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmDn.setStatus(_A)
_CucsExtvmmEpFsmRn_Type=SnmpAdminString
_CucsExtvmmEpFsmRn_Object=MibTableColumn
cucsExtvmmEpFsmRn=_CucsExtvmmEpFsmRn_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,3),_CucsExtvmmEpFsmRn_Type())
cucsExtvmmEpFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmRn.setStatus(_A)
_CucsExtvmmEpFsmCompletionTime_Type=DateAndTime
_CucsExtvmmEpFsmCompletionTime_Object=MibTableColumn
cucsExtvmmEpFsmCompletionTime=_CucsExtvmmEpFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,4),_CucsExtvmmEpFsmCompletionTime_Type())
cucsExtvmmEpFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmCompletionTime.setStatus(_A)
_CucsExtvmmEpFsmCurrentFsm_Type=CucsExtvmmEpFsmCurrentFsm
_CucsExtvmmEpFsmCurrentFsm_Object=MibTableColumn
cucsExtvmmEpFsmCurrentFsm=_CucsExtvmmEpFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,5),_CucsExtvmmEpFsmCurrentFsm_Type())
cucsExtvmmEpFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmCurrentFsm.setStatus(_A)
_CucsExtvmmEpFsmDescrData_Type=SnmpAdminString
_CucsExtvmmEpFsmDescrData_Object=MibTableColumn
cucsExtvmmEpFsmDescrData=_CucsExtvmmEpFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,6),_CucsExtvmmEpFsmDescrData_Type())
cucsExtvmmEpFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmDescrData.setStatus(_A)
_CucsExtvmmEpFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmEpFsmFsmStatus_Object=MibTableColumn
cucsExtvmmEpFsmFsmStatus=_CucsExtvmmEpFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,7),_CucsExtvmmEpFsmFsmStatus_Type())
cucsExtvmmEpFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmFsmStatus.setStatus(_A)
_CucsExtvmmEpFsmProgress_Type=Gauge32
_CucsExtvmmEpFsmProgress_Object=MibTableColumn
cucsExtvmmEpFsmProgress=_CucsExtvmmEpFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,8),_CucsExtvmmEpFsmProgress_Type())
cucsExtvmmEpFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmProgress.setStatus(_A)
_CucsExtvmmEpFsmRmtErrCode_Type=Gauge32
_CucsExtvmmEpFsmRmtErrCode_Object=MibTableColumn
cucsExtvmmEpFsmRmtErrCode=_CucsExtvmmEpFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,9),_CucsExtvmmEpFsmRmtErrCode_Type())
cucsExtvmmEpFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmRmtErrCode.setStatus(_A)
_CucsExtvmmEpFsmRmtErrDescr_Type=SnmpAdminString
_CucsExtvmmEpFsmRmtErrDescr_Object=MibTableColumn
cucsExtvmmEpFsmRmtErrDescr=_CucsExtvmmEpFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,10),_CucsExtvmmEpFsmRmtErrDescr_Type())
cucsExtvmmEpFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmRmtErrDescr.setStatus(_A)
_CucsExtvmmEpFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmEpFsmRmtRslt_Object=MibTableColumn
cucsExtvmmEpFsmRmtRslt=_CucsExtvmmEpFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,18,14,1,11),_CucsExtvmmEpFsmRmtRslt_Type())
cucsExtvmmEpFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmRmtRslt.setStatus(_A)
_CucsExtvmmEpFsmStageTable_Object=MibTable
cucsExtvmmEpFsmStageTable=_CucsExtvmmEpFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,18,15))
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageTable.setStatus(_A)
_CucsExtvmmEpFsmStageEntry_Object=MibTableRow
cucsExtvmmEpFsmStageEntry=_CucsExtvmmEpFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,18,15,1))
cucsExtvmmEpFsmStageEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageEntry.setStatus(_A)
_CucsExtvmmEpFsmStageInstanceId_Type=CucsManagedObjectId
_CucsExtvmmEpFsmStageInstanceId_Object=MibTableColumn
cucsExtvmmEpFsmStageInstanceId=_CucsExtvmmEpFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,15,1,1),_CucsExtvmmEpFsmStageInstanceId_Type())
cucsExtvmmEpFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageInstanceId.setStatus(_A)
_CucsExtvmmEpFsmStageDn_Type=CucsManagedObjectDn
_CucsExtvmmEpFsmStageDn_Object=MibTableColumn
cucsExtvmmEpFsmStageDn=_CucsExtvmmEpFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,18,15,1,2),_CucsExtvmmEpFsmStageDn_Type())
cucsExtvmmEpFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageDn.setStatus(_A)
_CucsExtvmmEpFsmStageRn_Type=SnmpAdminString
_CucsExtvmmEpFsmStageRn_Object=MibTableColumn
cucsExtvmmEpFsmStageRn=_CucsExtvmmEpFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,18,15,1,3),_CucsExtvmmEpFsmStageRn_Type())
cucsExtvmmEpFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageRn.setStatus(_A)
_CucsExtvmmEpFsmStageDescrData_Type=SnmpAdminString
_CucsExtvmmEpFsmStageDescrData_Object=MibTableColumn
cucsExtvmmEpFsmStageDescrData=_CucsExtvmmEpFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,15,1,4),_CucsExtvmmEpFsmStageDescrData_Type())
cucsExtvmmEpFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageDescrData.setStatus(_A)
_CucsExtvmmEpFsmStageLastUpdateTime_Type=DateAndTime
_CucsExtvmmEpFsmStageLastUpdateTime_Object=MibTableColumn
cucsExtvmmEpFsmStageLastUpdateTime=_CucsExtvmmEpFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,18,15,1,5),_CucsExtvmmEpFsmStageLastUpdateTime_Type())
cucsExtvmmEpFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageLastUpdateTime.setStatus(_A)
_CucsExtvmmEpFsmStageName_Type=CucsExtvmmEpFsmStageName
_CucsExtvmmEpFsmStageName_Object=MibTableColumn
cucsExtvmmEpFsmStageName=_CucsExtvmmEpFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,18,15,1,6),_CucsExtvmmEpFsmStageName_Type())
cucsExtvmmEpFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageName.setStatus(_A)
_CucsExtvmmEpFsmStageOrder_Type=Gauge32
_CucsExtvmmEpFsmStageOrder_Object=MibTableColumn
cucsExtvmmEpFsmStageOrder=_CucsExtvmmEpFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,18,15,1,7),_CucsExtvmmEpFsmStageOrder_Type())
cucsExtvmmEpFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageOrder.setStatus(_A)
_CucsExtvmmEpFsmStageRetry_Type=Gauge32
_CucsExtvmmEpFsmStageRetry_Object=MibTableColumn
cucsExtvmmEpFsmStageRetry=_CucsExtvmmEpFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,18,15,1,8),_CucsExtvmmEpFsmStageRetry_Type())
cucsExtvmmEpFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageRetry.setStatus(_A)
_CucsExtvmmEpFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmEpFsmStageStageStatus_Object=MibTableColumn
cucsExtvmmEpFsmStageStageStatus=_CucsExtvmmEpFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,18,15,1,9),_CucsExtvmmEpFsmStageStageStatus_Type())
cucsExtvmmEpFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmEpFsmStageStageStatus.setStatus(_A)
_CucsExtvmmKeyStoreFsmTable_Object=MibTable
cucsExtvmmKeyStoreFsmTable=_CucsExtvmmKeyStoreFsmTable_Object((1,3,6,1,4,1,9,9,719,1,18,16))
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmTable.setStatus(_A)
_CucsExtvmmKeyStoreFsmEntry_Object=MibTableRow
cucsExtvmmKeyStoreFsmEntry=_CucsExtvmmKeyStoreFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,18,16,1))
cucsExtvmmKeyStoreFsmEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmEntry.setStatus(_A)
_CucsExtvmmKeyStoreFsmInstanceId_Type=CucsManagedObjectId
_CucsExtvmmKeyStoreFsmInstanceId_Object=MibTableColumn
cucsExtvmmKeyStoreFsmInstanceId=_CucsExtvmmKeyStoreFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,1),_CucsExtvmmKeyStoreFsmInstanceId_Type())
cucsExtvmmKeyStoreFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmInstanceId.setStatus(_A)
_CucsExtvmmKeyStoreFsmDn_Type=CucsManagedObjectDn
_CucsExtvmmKeyStoreFsmDn_Object=MibTableColumn
cucsExtvmmKeyStoreFsmDn=_CucsExtvmmKeyStoreFsmDn_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,2),_CucsExtvmmKeyStoreFsmDn_Type())
cucsExtvmmKeyStoreFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmDn.setStatus(_A)
_CucsExtvmmKeyStoreFsmRn_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmRn_Object=MibTableColumn
cucsExtvmmKeyStoreFsmRn=_CucsExtvmmKeyStoreFsmRn_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,3),_CucsExtvmmKeyStoreFsmRn_Type())
cucsExtvmmKeyStoreFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmRn.setStatus(_A)
_CucsExtvmmKeyStoreFsmCompletionTime_Type=DateAndTime
_CucsExtvmmKeyStoreFsmCompletionTime_Object=MibTableColumn
cucsExtvmmKeyStoreFsmCompletionTime=_CucsExtvmmKeyStoreFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,4),_CucsExtvmmKeyStoreFsmCompletionTime_Type())
cucsExtvmmKeyStoreFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmCompletionTime.setStatus(_A)
_CucsExtvmmKeyStoreFsmCurrentFsm_Type=CucsExtvmmKeyStoreFsmCurrentFsm
_CucsExtvmmKeyStoreFsmCurrentFsm_Object=MibTableColumn
cucsExtvmmKeyStoreFsmCurrentFsm=_CucsExtvmmKeyStoreFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,5),_CucsExtvmmKeyStoreFsmCurrentFsm_Type())
cucsExtvmmKeyStoreFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmCurrentFsm.setStatus(_A)
_CucsExtvmmKeyStoreFsmDescrData_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmDescrData_Object=MibTableColumn
cucsExtvmmKeyStoreFsmDescrData=_CucsExtvmmKeyStoreFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,6),_CucsExtvmmKeyStoreFsmDescrData_Type())
cucsExtvmmKeyStoreFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmDescrData.setStatus(_A)
_CucsExtvmmKeyStoreFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmKeyStoreFsmFsmStatus_Object=MibTableColumn
cucsExtvmmKeyStoreFsmFsmStatus=_CucsExtvmmKeyStoreFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,7),_CucsExtvmmKeyStoreFsmFsmStatus_Type())
cucsExtvmmKeyStoreFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmFsmStatus.setStatus(_A)
_CucsExtvmmKeyStoreFsmProgress_Type=Gauge32
_CucsExtvmmKeyStoreFsmProgress_Object=MibTableColumn
cucsExtvmmKeyStoreFsmProgress=_CucsExtvmmKeyStoreFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,8),_CucsExtvmmKeyStoreFsmProgress_Type())
cucsExtvmmKeyStoreFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmProgress.setStatus(_A)
_CucsExtvmmKeyStoreFsmRmtErrCode_Type=Gauge32
_CucsExtvmmKeyStoreFsmRmtErrCode_Object=MibTableColumn
cucsExtvmmKeyStoreFsmRmtErrCode=_CucsExtvmmKeyStoreFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,9),_CucsExtvmmKeyStoreFsmRmtErrCode_Type())
cucsExtvmmKeyStoreFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmRmtErrCode.setStatus(_A)
_CucsExtvmmKeyStoreFsmRmtErrDescr_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmRmtErrDescr_Object=MibTableColumn
cucsExtvmmKeyStoreFsmRmtErrDescr=_CucsExtvmmKeyStoreFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,10),_CucsExtvmmKeyStoreFsmRmtErrDescr_Type())
cucsExtvmmKeyStoreFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmRmtErrDescr.setStatus(_A)
_CucsExtvmmKeyStoreFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmKeyStoreFsmRmtRslt_Object=MibTableColumn
cucsExtvmmKeyStoreFsmRmtRslt=_CucsExtvmmKeyStoreFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,18,16,1,11),_CucsExtvmmKeyStoreFsmRmtRslt_Type())
cucsExtvmmKeyStoreFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmRmtRslt.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageTable_Object=MibTable
cucsExtvmmKeyStoreFsmStageTable=_CucsExtvmmKeyStoreFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,18,17))
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageTable.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageEntry_Object=MibTableRow
cucsExtvmmKeyStoreFsmStageEntry=_CucsExtvmmKeyStoreFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,18,17,1))
cucsExtvmmKeyStoreFsmStageEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageEntry.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageInstanceId_Type=CucsManagedObjectId
_CucsExtvmmKeyStoreFsmStageInstanceId_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageInstanceId=_CucsExtvmmKeyStoreFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,17,1,1),_CucsExtvmmKeyStoreFsmStageInstanceId_Type())
cucsExtvmmKeyStoreFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageInstanceId.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageDn_Type=CucsManagedObjectDn
_CucsExtvmmKeyStoreFsmStageDn_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageDn=_CucsExtvmmKeyStoreFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,18,17,1,2),_CucsExtvmmKeyStoreFsmStageDn_Type())
cucsExtvmmKeyStoreFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageDn.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageRn_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmStageRn_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageRn=_CucsExtvmmKeyStoreFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,18,17,1,3),_CucsExtvmmKeyStoreFsmStageRn_Type())
cucsExtvmmKeyStoreFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageRn.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageDescrData_Type=SnmpAdminString
_CucsExtvmmKeyStoreFsmStageDescrData_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageDescrData=_CucsExtvmmKeyStoreFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,17,1,4),_CucsExtvmmKeyStoreFsmStageDescrData_Type())
cucsExtvmmKeyStoreFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageDescrData.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageLastUpdateTime_Type=DateAndTime
_CucsExtvmmKeyStoreFsmStageLastUpdateTime_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageLastUpdateTime=_CucsExtvmmKeyStoreFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,18,17,1,5),_CucsExtvmmKeyStoreFsmStageLastUpdateTime_Type())
cucsExtvmmKeyStoreFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageLastUpdateTime.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageName_Type=CucsExtvmmKeyStoreFsmStageName
_CucsExtvmmKeyStoreFsmStageName_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageName=_CucsExtvmmKeyStoreFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,18,17,1,6),_CucsExtvmmKeyStoreFsmStageName_Type())
cucsExtvmmKeyStoreFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageName.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageOrder_Type=Gauge32
_CucsExtvmmKeyStoreFsmStageOrder_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageOrder=_CucsExtvmmKeyStoreFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,18,17,1,7),_CucsExtvmmKeyStoreFsmStageOrder_Type())
cucsExtvmmKeyStoreFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageOrder.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageRetry_Type=Gauge32
_CucsExtvmmKeyStoreFsmStageRetry_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageRetry=_CucsExtvmmKeyStoreFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,18,17,1,8),_CucsExtvmmKeyStoreFsmStageRetry_Type())
cucsExtvmmKeyStoreFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageRetry.setStatus(_A)
_CucsExtvmmKeyStoreFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmKeyStoreFsmStageStageStatus_Object=MibTableColumn
cucsExtvmmKeyStoreFsmStageStageStatus=_CucsExtvmmKeyStoreFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,18,17,1,9),_CucsExtvmmKeyStoreFsmStageStageStatus_Type())
cucsExtvmmKeyStoreFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmKeyStoreFsmStageStageStatus.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmTable_Object=MibTable
cucsExtvmmMasterExtKeyFsmTable=_CucsExtvmmMasterExtKeyFsmTable_Object((1,3,6,1,4,1,9,9,719,1,18,18))
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmTable.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmEntry_Object=MibTableRow
cucsExtvmmMasterExtKeyFsmEntry=_CucsExtvmmMasterExtKeyFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,18,18,1))
cucsExtvmmMasterExtKeyFsmEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmEntry.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmInstanceId_Type=CucsManagedObjectId
_CucsExtvmmMasterExtKeyFsmInstanceId_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmInstanceId=_CucsExtvmmMasterExtKeyFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,1),_CucsExtvmmMasterExtKeyFsmInstanceId_Type())
cucsExtvmmMasterExtKeyFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmInstanceId.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmDn_Type=CucsManagedObjectDn
_CucsExtvmmMasterExtKeyFsmDn_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmDn=_CucsExtvmmMasterExtKeyFsmDn_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,2),_CucsExtvmmMasterExtKeyFsmDn_Type())
cucsExtvmmMasterExtKeyFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmDn.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmRn_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmRn_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmRn=_CucsExtvmmMasterExtKeyFsmRn_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,3),_CucsExtvmmMasterExtKeyFsmRn_Type())
cucsExtvmmMasterExtKeyFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmRn.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmCompletionTime_Type=DateAndTime
_CucsExtvmmMasterExtKeyFsmCompletionTime_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmCompletionTime=_CucsExtvmmMasterExtKeyFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,4),_CucsExtvmmMasterExtKeyFsmCompletionTime_Type())
cucsExtvmmMasterExtKeyFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmCompletionTime.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmCurrentFsm_Type=CucsExtvmmMasterExtKeyFsmCurrentFsm
_CucsExtvmmMasterExtKeyFsmCurrentFsm_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmCurrentFsm=_CucsExtvmmMasterExtKeyFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,5),_CucsExtvmmMasterExtKeyFsmCurrentFsm_Type())
cucsExtvmmMasterExtKeyFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmCurrentFsm.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmDescrData_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmDescrData_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmDescrData=_CucsExtvmmMasterExtKeyFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,6),_CucsExtvmmMasterExtKeyFsmDescrData_Type())
cucsExtvmmMasterExtKeyFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmDescrData.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmMasterExtKeyFsmFsmStatus_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmFsmStatus=_CucsExtvmmMasterExtKeyFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,7),_CucsExtvmmMasterExtKeyFsmFsmStatus_Type())
cucsExtvmmMasterExtKeyFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmFsmStatus.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmProgress_Type=Gauge32
_CucsExtvmmMasterExtKeyFsmProgress_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmProgress=_CucsExtvmmMasterExtKeyFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,8),_CucsExtvmmMasterExtKeyFsmProgress_Type())
cucsExtvmmMasterExtKeyFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmProgress.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmRmtErrCode_Type=Gauge32
_CucsExtvmmMasterExtKeyFsmRmtErrCode_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtErrCode=_CucsExtvmmMasterExtKeyFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,9),_CucsExtvmmMasterExtKeyFsmRmtErrCode_Type())
cucsExtvmmMasterExtKeyFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmRmtErrCode.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmRmtErrDescr_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmRmtErrDescr_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtErrDescr=_CucsExtvmmMasterExtKeyFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,10),_CucsExtvmmMasterExtKeyFsmRmtErrDescr_Type())
cucsExtvmmMasterExtKeyFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmRmtErrDescr.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmMasterExtKeyFsmRmtRslt_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtRslt=_CucsExtvmmMasterExtKeyFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,18,18,1,11),_CucsExtvmmMasterExtKeyFsmRmtRslt_Type())
cucsExtvmmMasterExtKeyFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmRmtRslt.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageTable_Object=MibTable
cucsExtvmmMasterExtKeyFsmStageTable=_CucsExtvmmMasterExtKeyFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,18,19))
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageTable.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageEntry_Object=MibTableRow
cucsExtvmmMasterExtKeyFsmStageEntry=_CucsExtvmmMasterExtKeyFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,18,19,1))
cucsExtvmmMasterExtKeyFsmStageEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageEntry.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageInstanceId_Type=CucsManagedObjectId
_CucsExtvmmMasterExtKeyFsmStageInstanceId_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageInstanceId=_CucsExtvmmMasterExtKeyFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,19,1,1),_CucsExtvmmMasterExtKeyFsmStageInstanceId_Type())
cucsExtvmmMasterExtKeyFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageInstanceId.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageDn_Type=CucsManagedObjectDn
_CucsExtvmmMasterExtKeyFsmStageDn_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageDn=_CucsExtvmmMasterExtKeyFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,18,19,1,2),_CucsExtvmmMasterExtKeyFsmStageDn_Type())
cucsExtvmmMasterExtKeyFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageDn.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageRn_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmStageRn_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageRn=_CucsExtvmmMasterExtKeyFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,18,19,1,3),_CucsExtvmmMasterExtKeyFsmStageRn_Type())
cucsExtvmmMasterExtKeyFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageRn.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageDescrData_Type=SnmpAdminString
_CucsExtvmmMasterExtKeyFsmStageDescrData_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageDescrData=_CucsExtvmmMasterExtKeyFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,19,1,4),_CucsExtvmmMasterExtKeyFsmStageDescrData_Type())
cucsExtvmmMasterExtKeyFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageDescrData.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageLastUpdateTime_Type=DateAndTime
_CucsExtvmmMasterExtKeyFsmStageLastUpdateTime_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageLastUpdateTime=_CucsExtvmmMasterExtKeyFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,18,19,1,5),_CucsExtvmmMasterExtKeyFsmStageLastUpdateTime_Type())
cucsExtvmmMasterExtKeyFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageLastUpdateTime.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageName_Type=CucsExtvmmMasterExtKeyFsmStageName
_CucsExtvmmMasterExtKeyFsmStageName_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageName=_CucsExtvmmMasterExtKeyFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,18,19,1,6),_CucsExtvmmMasterExtKeyFsmStageName_Type())
cucsExtvmmMasterExtKeyFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageName.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageOrder_Type=Gauge32
_CucsExtvmmMasterExtKeyFsmStageOrder_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageOrder=_CucsExtvmmMasterExtKeyFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,18,19,1,7),_CucsExtvmmMasterExtKeyFsmStageOrder_Type())
cucsExtvmmMasterExtKeyFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageOrder.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageRetry_Type=Gauge32
_CucsExtvmmMasterExtKeyFsmStageRetry_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageRetry=_CucsExtvmmMasterExtKeyFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,18,19,1,8),_CucsExtvmmMasterExtKeyFsmStageRetry_Type())
cucsExtvmmMasterExtKeyFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageRetry.setStatus(_A)
_CucsExtvmmMasterExtKeyFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmMasterExtKeyFsmStageStageStatus_Object=MibTableColumn
cucsExtvmmMasterExtKeyFsmStageStageStatus=_CucsExtvmmMasterExtKeyFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,18,19,1,9),_CucsExtvmmMasterExtKeyFsmStageStageStatus_Type())
cucsExtvmmMasterExtKeyFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmMasterExtKeyFsmStageStageStatus.setStatus(_A)
_CucsExtvmmProviderFsmTable_Object=MibTable
cucsExtvmmProviderFsmTable=_CucsExtvmmProviderFsmTable_Object((1,3,6,1,4,1,9,9,719,1,18,20))
if mibBuilder.loadTexts:cucsExtvmmProviderFsmTable.setStatus(_A)
_CucsExtvmmProviderFsmEntry_Object=MibTableRow
cucsExtvmmProviderFsmEntry=_CucsExtvmmProviderFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,18,20,1))
cucsExtvmmProviderFsmEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cucsExtvmmProviderFsmEntry.setStatus(_A)
_CucsExtvmmProviderFsmInstanceId_Type=CucsManagedObjectId
_CucsExtvmmProviderFsmInstanceId_Object=MibTableColumn
cucsExtvmmProviderFsmInstanceId=_CucsExtvmmProviderFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,1),_CucsExtvmmProviderFsmInstanceId_Type())
cucsExtvmmProviderFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmInstanceId.setStatus(_A)
_CucsExtvmmProviderFsmDn_Type=CucsManagedObjectDn
_CucsExtvmmProviderFsmDn_Object=MibTableColumn
cucsExtvmmProviderFsmDn=_CucsExtvmmProviderFsmDn_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,2),_CucsExtvmmProviderFsmDn_Type())
cucsExtvmmProviderFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmDn.setStatus(_A)
_CucsExtvmmProviderFsmRn_Type=SnmpAdminString
_CucsExtvmmProviderFsmRn_Object=MibTableColumn
cucsExtvmmProviderFsmRn=_CucsExtvmmProviderFsmRn_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,3),_CucsExtvmmProviderFsmRn_Type())
cucsExtvmmProviderFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmRn.setStatus(_A)
_CucsExtvmmProviderFsmCompletionTime_Type=DateAndTime
_CucsExtvmmProviderFsmCompletionTime_Object=MibTableColumn
cucsExtvmmProviderFsmCompletionTime=_CucsExtvmmProviderFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,4),_CucsExtvmmProviderFsmCompletionTime_Type())
cucsExtvmmProviderFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmCompletionTime.setStatus(_A)
_CucsExtvmmProviderFsmCurrentFsm_Type=CucsExtvmmProviderFsmCurrentFsm
_CucsExtvmmProviderFsmCurrentFsm_Object=MibTableColumn
cucsExtvmmProviderFsmCurrentFsm=_CucsExtvmmProviderFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,5),_CucsExtvmmProviderFsmCurrentFsm_Type())
cucsExtvmmProviderFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmCurrentFsm.setStatus(_A)
_CucsExtvmmProviderFsmDescrData_Type=SnmpAdminString
_CucsExtvmmProviderFsmDescrData_Object=MibTableColumn
cucsExtvmmProviderFsmDescrData=_CucsExtvmmProviderFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,6),_CucsExtvmmProviderFsmDescrData_Type())
cucsExtvmmProviderFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmDescrData.setStatus(_A)
_CucsExtvmmProviderFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmProviderFsmFsmStatus_Object=MibTableColumn
cucsExtvmmProviderFsmFsmStatus=_CucsExtvmmProviderFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,7),_CucsExtvmmProviderFsmFsmStatus_Type())
cucsExtvmmProviderFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmFsmStatus.setStatus(_A)
_CucsExtvmmProviderFsmProgress_Type=Gauge32
_CucsExtvmmProviderFsmProgress_Object=MibTableColumn
cucsExtvmmProviderFsmProgress=_CucsExtvmmProviderFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,8),_CucsExtvmmProviderFsmProgress_Type())
cucsExtvmmProviderFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmProgress.setStatus(_A)
_CucsExtvmmProviderFsmRmtErrCode_Type=Gauge32
_CucsExtvmmProviderFsmRmtErrCode_Object=MibTableColumn
cucsExtvmmProviderFsmRmtErrCode=_CucsExtvmmProviderFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,9),_CucsExtvmmProviderFsmRmtErrCode_Type())
cucsExtvmmProviderFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmRmtErrCode.setStatus(_A)
_CucsExtvmmProviderFsmRmtErrDescr_Type=SnmpAdminString
_CucsExtvmmProviderFsmRmtErrDescr_Object=MibTableColumn
cucsExtvmmProviderFsmRmtErrDescr=_CucsExtvmmProviderFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,10),_CucsExtvmmProviderFsmRmtErrDescr_Type())
cucsExtvmmProviderFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmRmtErrDescr.setStatus(_A)
_CucsExtvmmProviderFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmProviderFsmRmtRslt_Object=MibTableColumn
cucsExtvmmProviderFsmRmtRslt=_CucsExtvmmProviderFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,18,20,1,11),_CucsExtvmmProviderFsmRmtRslt_Type())
cucsExtvmmProviderFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmRmtRslt.setStatus(_A)
_CucsExtvmmProviderFsmStageTable_Object=MibTable
cucsExtvmmProviderFsmStageTable=_CucsExtvmmProviderFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,18,21))
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageTable.setStatus(_A)
_CucsExtvmmProviderFsmStageEntry_Object=MibTableRow
cucsExtvmmProviderFsmStageEntry=_CucsExtvmmProviderFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,18,21,1))
cucsExtvmmProviderFsmStageEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageEntry.setStatus(_A)
_CucsExtvmmProviderFsmStageInstanceId_Type=CucsManagedObjectId
_CucsExtvmmProviderFsmStageInstanceId_Object=MibTableColumn
cucsExtvmmProviderFsmStageInstanceId=_CucsExtvmmProviderFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,21,1,1),_CucsExtvmmProviderFsmStageInstanceId_Type())
cucsExtvmmProviderFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageInstanceId.setStatus(_A)
_CucsExtvmmProviderFsmStageDn_Type=CucsManagedObjectDn
_CucsExtvmmProviderFsmStageDn_Object=MibTableColumn
cucsExtvmmProviderFsmStageDn=_CucsExtvmmProviderFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,18,21,1,2),_CucsExtvmmProviderFsmStageDn_Type())
cucsExtvmmProviderFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageDn.setStatus(_A)
_CucsExtvmmProviderFsmStageRn_Type=SnmpAdminString
_CucsExtvmmProviderFsmStageRn_Object=MibTableColumn
cucsExtvmmProviderFsmStageRn=_CucsExtvmmProviderFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,18,21,1,3),_CucsExtvmmProviderFsmStageRn_Type())
cucsExtvmmProviderFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageRn.setStatus(_A)
_CucsExtvmmProviderFsmStageDescrData_Type=SnmpAdminString
_CucsExtvmmProviderFsmStageDescrData_Object=MibTableColumn
cucsExtvmmProviderFsmStageDescrData=_CucsExtvmmProviderFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,21,1,4),_CucsExtvmmProviderFsmStageDescrData_Type())
cucsExtvmmProviderFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageDescrData.setStatus(_A)
_CucsExtvmmProviderFsmStageLastUpdateTime_Type=DateAndTime
_CucsExtvmmProviderFsmStageLastUpdateTime_Object=MibTableColumn
cucsExtvmmProviderFsmStageLastUpdateTime=_CucsExtvmmProviderFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,18,21,1,5),_CucsExtvmmProviderFsmStageLastUpdateTime_Type())
cucsExtvmmProviderFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageLastUpdateTime.setStatus(_A)
_CucsExtvmmProviderFsmStageName_Type=CucsExtvmmProviderFsmStageName
_CucsExtvmmProviderFsmStageName_Object=MibTableColumn
cucsExtvmmProviderFsmStageName=_CucsExtvmmProviderFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,18,21,1,6),_CucsExtvmmProviderFsmStageName_Type())
cucsExtvmmProviderFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageName.setStatus(_A)
_CucsExtvmmProviderFsmStageOrder_Type=Gauge32
_CucsExtvmmProviderFsmStageOrder_Object=MibTableColumn
cucsExtvmmProviderFsmStageOrder=_CucsExtvmmProviderFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,18,21,1,7),_CucsExtvmmProviderFsmStageOrder_Type())
cucsExtvmmProviderFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageOrder.setStatus(_A)
_CucsExtvmmProviderFsmStageRetry_Type=Gauge32
_CucsExtvmmProviderFsmStageRetry_Object=MibTableColumn
cucsExtvmmProviderFsmStageRetry=_CucsExtvmmProviderFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,18,21,1,8),_CucsExtvmmProviderFsmStageRetry_Type())
cucsExtvmmProviderFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageRetry.setStatus(_A)
_CucsExtvmmProviderFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmProviderFsmStageStageStatus_Object=MibTableColumn
cucsExtvmmProviderFsmStageStageStatus=_CucsExtvmmProviderFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,18,21,1,9),_CucsExtvmmProviderFsmStageStageStatus_Type())
cucsExtvmmProviderFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmProviderFsmStageStageStatus.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmTable_Object=MibTable
cucsExtvmmSwitchDelTaskFsmTable=_CucsExtvmmSwitchDelTaskFsmTable_Object((1,3,6,1,4,1,9,9,719,1,18,22))
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmTable.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmEntry_Object=MibTableRow
cucsExtvmmSwitchDelTaskFsmEntry=_CucsExtvmmSwitchDelTaskFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,18,22,1))
cucsExtvmmSwitchDelTaskFsmEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmEntry.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmInstanceId_Type=CucsManagedObjectId
_CucsExtvmmSwitchDelTaskFsmInstanceId_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmInstanceId=_CucsExtvmmSwitchDelTaskFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,1),_CucsExtvmmSwitchDelTaskFsmInstanceId_Type())
cucsExtvmmSwitchDelTaskFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmInstanceId.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmDn_Type=CucsManagedObjectDn
_CucsExtvmmSwitchDelTaskFsmDn_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmDn=_CucsExtvmmSwitchDelTaskFsmDn_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,2),_CucsExtvmmSwitchDelTaskFsmDn_Type())
cucsExtvmmSwitchDelTaskFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmDn.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmRn_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmRn_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmRn=_CucsExtvmmSwitchDelTaskFsmRn_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,3),_CucsExtvmmSwitchDelTaskFsmRn_Type())
cucsExtvmmSwitchDelTaskFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmRn.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmCompletionTime_Type=DateAndTime
_CucsExtvmmSwitchDelTaskFsmCompletionTime_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmCompletionTime=_CucsExtvmmSwitchDelTaskFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,4),_CucsExtvmmSwitchDelTaskFsmCompletionTime_Type())
cucsExtvmmSwitchDelTaskFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmCompletionTime.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmCurrentFsm_Type=CucsExtvmmSwitchDelTaskFsmCurrentFsm
_CucsExtvmmSwitchDelTaskFsmCurrentFsm_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmCurrentFsm=_CucsExtvmmSwitchDelTaskFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,5),_CucsExtvmmSwitchDelTaskFsmCurrentFsm_Type())
cucsExtvmmSwitchDelTaskFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmCurrentFsm.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmDescrData_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmDescrData_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmDescrData=_CucsExtvmmSwitchDelTaskFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,6),_CucsExtvmmSwitchDelTaskFsmDescrData_Type())
cucsExtvmmSwitchDelTaskFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmDescrData.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmSwitchDelTaskFsmFsmStatus_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmFsmStatus=_CucsExtvmmSwitchDelTaskFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,7),_CucsExtvmmSwitchDelTaskFsmFsmStatus_Type())
cucsExtvmmSwitchDelTaskFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmFsmStatus.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmProgress_Type=Gauge32
_CucsExtvmmSwitchDelTaskFsmProgress_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmProgress=_CucsExtvmmSwitchDelTaskFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,8),_CucsExtvmmSwitchDelTaskFsmProgress_Type())
cucsExtvmmSwitchDelTaskFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmProgress.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmRmtErrCode_Type=Gauge32
_CucsExtvmmSwitchDelTaskFsmRmtErrCode_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtErrCode=_CucsExtvmmSwitchDelTaskFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,9),_CucsExtvmmSwitchDelTaskFsmRmtErrCode_Type())
cucsExtvmmSwitchDelTaskFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmRmtErrCode.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmRmtErrDescr_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmRmtErrDescr_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtErrDescr=_CucsExtvmmSwitchDelTaskFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,10),_CucsExtvmmSwitchDelTaskFsmRmtErrDescr_Type())
cucsExtvmmSwitchDelTaskFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmRmtErrDescr.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmSwitchDelTaskFsmRmtRslt_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtRslt=_CucsExtvmmSwitchDelTaskFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,18,22,1,11),_CucsExtvmmSwitchDelTaskFsmRmtRslt_Type())
cucsExtvmmSwitchDelTaskFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmRmtRslt.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageTable_Object=MibTable
cucsExtvmmSwitchDelTaskFsmStageTable=_CucsExtvmmSwitchDelTaskFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,18,23))
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageTable.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageEntry_Object=MibTableRow
cucsExtvmmSwitchDelTaskFsmStageEntry=_CucsExtvmmSwitchDelTaskFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,18,23,1))
cucsExtvmmSwitchDelTaskFsmStageEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageEntry.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageInstanceId_Type=CucsManagedObjectId
_CucsExtvmmSwitchDelTaskFsmStageInstanceId_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageInstanceId=_CucsExtvmmSwitchDelTaskFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,23,1,1),_CucsExtvmmSwitchDelTaskFsmStageInstanceId_Type())
cucsExtvmmSwitchDelTaskFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageInstanceId.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageDn_Type=CucsManagedObjectDn
_CucsExtvmmSwitchDelTaskFsmStageDn_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageDn=_CucsExtvmmSwitchDelTaskFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,18,23,1,2),_CucsExtvmmSwitchDelTaskFsmStageDn_Type())
cucsExtvmmSwitchDelTaskFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageDn.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageRn_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmStageRn_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageRn=_CucsExtvmmSwitchDelTaskFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,18,23,1,3),_CucsExtvmmSwitchDelTaskFsmStageRn_Type())
cucsExtvmmSwitchDelTaskFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageRn.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageDescrData_Type=SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmStageDescrData_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageDescrData=_CucsExtvmmSwitchDelTaskFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,23,1,4),_CucsExtvmmSwitchDelTaskFsmStageDescrData_Type())
cucsExtvmmSwitchDelTaskFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageDescrData.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageLastUpdateTime_Type=DateAndTime
_CucsExtvmmSwitchDelTaskFsmStageLastUpdateTime_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime=_CucsExtvmmSwitchDelTaskFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,18,23,1,5),_CucsExtvmmSwitchDelTaskFsmStageLastUpdateTime_Type())
cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageName_Type=CucsExtvmmSwitchDelTaskFsmStageName
_CucsExtvmmSwitchDelTaskFsmStageName_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageName=_CucsExtvmmSwitchDelTaskFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,18,23,1,6),_CucsExtvmmSwitchDelTaskFsmStageName_Type())
cucsExtvmmSwitchDelTaskFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageName.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageOrder_Type=Gauge32
_CucsExtvmmSwitchDelTaskFsmStageOrder_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageOrder=_CucsExtvmmSwitchDelTaskFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,18,23,1,7),_CucsExtvmmSwitchDelTaskFsmStageOrder_Type())
cucsExtvmmSwitchDelTaskFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageOrder.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageRetry_Type=Gauge32
_CucsExtvmmSwitchDelTaskFsmStageRetry_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageRetry=_CucsExtvmmSwitchDelTaskFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,18,23,1,8),_CucsExtvmmSwitchDelTaskFsmStageRetry_Type())
cucsExtvmmSwitchDelTaskFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageRetry.setStatus(_A)
_CucsExtvmmSwitchDelTaskFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmSwitchDelTaskFsmStageStageStatus_Object=MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageStageStatus=_CucsExtvmmSwitchDelTaskFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,18,23,1,9),_CucsExtvmmSwitchDelTaskFsmStageStageStatus_Type())
cucsExtvmmSwitchDelTaskFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmSwitchDelTaskFsmStageStageStatus.setStatus(_A)
_CucsExtvmmFNDReferenceTable_Object=MibTable
cucsExtvmmFNDReferenceTable=_CucsExtvmmFNDReferenceTable_Object((1,3,6,1,4,1,9,9,719,1,18,24))
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceTable.setStatus(_A)
_CucsExtvmmFNDReferenceEntry_Object=MibTableRow
cucsExtvmmFNDReferenceEntry=_CucsExtvmmFNDReferenceEntry_Object((1,3,6,1,4,1,9,9,719,1,18,24,1))
cucsExtvmmFNDReferenceEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceEntry.setStatus(_A)
_CucsExtvmmFNDReferenceInstanceId_Type=CucsManagedObjectId
_CucsExtvmmFNDReferenceInstanceId_Object=MibTableColumn
cucsExtvmmFNDReferenceInstanceId=_CucsExtvmmFNDReferenceInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,1),_CucsExtvmmFNDReferenceInstanceId_Type())
cucsExtvmmFNDReferenceInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceInstanceId.setStatus(_A)
_CucsExtvmmFNDReferenceDn_Type=CucsManagedObjectDn
_CucsExtvmmFNDReferenceDn_Object=MibTableColumn
cucsExtvmmFNDReferenceDn=_CucsExtvmmFNDReferenceDn_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,2),_CucsExtvmmFNDReferenceDn_Type())
cucsExtvmmFNDReferenceDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceDn.setStatus(_A)
_CucsExtvmmFNDReferenceRn_Type=SnmpAdminString
_CucsExtvmmFNDReferenceRn_Object=MibTableColumn
cucsExtvmmFNDReferenceRn=_CucsExtvmmFNDReferenceRn_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,3),_CucsExtvmmFNDReferenceRn_Type())
cucsExtvmmFNDReferenceRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceRn.setStatus(_A)
_CucsExtvmmFNDReferenceDescr_Type=SnmpAdminString
_CucsExtvmmFNDReferenceDescr_Object=MibTableColumn
cucsExtvmmFNDReferenceDescr=_CucsExtvmmFNDReferenceDescr_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,4),_CucsExtvmmFNDReferenceDescr_Type())
cucsExtvmmFNDReferenceDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceDescr.setStatus(_A)
_CucsExtvmmFNDReferenceFnDefName_Type=SnmpAdminString
_CucsExtvmmFNDReferenceFnDefName_Object=MibTableColumn
cucsExtvmmFNDReferenceFnDefName=_CucsExtvmmFNDReferenceFnDefName_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,5),_CucsExtvmmFNDReferenceFnDefName_Type())
cucsExtvmmFNDReferenceFnDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceFnDefName.setStatus(_A)
_CucsExtvmmFNDReferenceIntId_Type=SnmpAdminString
_CucsExtvmmFNDReferenceIntId_Object=MibTableColumn
cucsExtvmmFNDReferenceIntId=_CucsExtvmmFNDReferenceIntId_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,6),_CucsExtvmmFNDReferenceIntId_Type())
cucsExtvmmFNDReferenceIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceIntId.setStatus(_A)
_CucsExtvmmFNDReferenceName_Type=SnmpAdminString
_CucsExtvmmFNDReferenceName_Object=MibTableColumn
cucsExtvmmFNDReferenceName=_CucsExtvmmFNDReferenceName_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,7),_CucsExtvmmFNDReferenceName_Type())
cucsExtvmmFNDReferenceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceName.setStatus(_A)
_CucsExtvmmFNDReferenceOperFnDefName_Type=SnmpAdminString
_CucsExtvmmFNDReferenceOperFnDefName_Object=MibTableColumn
cucsExtvmmFNDReferenceOperFnDefName=_CucsExtvmmFNDReferenceOperFnDefName_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,8),_CucsExtvmmFNDReferenceOperFnDefName_Type())
cucsExtvmmFNDReferenceOperFnDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFNDReferenceOperFnDefName.setStatus(_A)
_CucsExtvmmFNDReferencePolicyLevel_Type=Gauge32
_CucsExtvmmFNDReferencePolicyLevel_Object=MibTableColumn
cucsExtvmmFNDReferencePolicyLevel=_CucsExtvmmFNDReferencePolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,9),_CucsExtvmmFNDReferencePolicyLevel_Type())
cucsExtvmmFNDReferencePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFNDReferencePolicyLevel.setStatus(_A)
_CucsExtvmmFNDReferencePolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtvmmFNDReferencePolicyOwner_Object=MibTableColumn
cucsExtvmmFNDReferencePolicyOwner=_CucsExtvmmFNDReferencePolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,18,24,1,10),_CucsExtvmmFNDReferencePolicyOwner_Type())
cucsExtvmmFNDReferencePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFNDReferencePolicyOwner.setStatus(_A)
_CucsExtvmmFabricNetworkTable_Object=MibTable
cucsExtvmmFabricNetworkTable=_CucsExtvmmFabricNetworkTable_Object((1,3,6,1,4,1,9,9,719,1,18,25))
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkTable.setStatus(_A)
_CucsExtvmmFabricNetworkEntry_Object=MibTableRow
cucsExtvmmFabricNetworkEntry=_CucsExtvmmFabricNetworkEntry_Object((1,3,6,1,4,1,9,9,719,1,18,25,1))
cucsExtvmmFabricNetworkEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkEntry.setStatus(_A)
_CucsExtvmmFabricNetworkInstanceId_Type=CucsManagedObjectId
_CucsExtvmmFabricNetworkInstanceId_Object=MibTableColumn
cucsExtvmmFabricNetworkInstanceId=_CucsExtvmmFabricNetworkInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,1),_CucsExtvmmFabricNetworkInstanceId_Type())
cucsExtvmmFabricNetworkInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkInstanceId.setStatus(_A)
_CucsExtvmmFabricNetworkDn_Type=CucsManagedObjectDn
_CucsExtvmmFabricNetworkDn_Object=MibTableColumn
cucsExtvmmFabricNetworkDn=_CucsExtvmmFabricNetworkDn_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,2),_CucsExtvmmFabricNetworkDn_Type())
cucsExtvmmFabricNetworkDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDn.setStatus(_A)
_CucsExtvmmFabricNetworkRn_Type=SnmpAdminString
_CucsExtvmmFabricNetworkRn_Object=MibTableColumn
cucsExtvmmFabricNetworkRn=_CucsExtvmmFabricNetworkRn_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,3),_CucsExtvmmFabricNetworkRn_Type())
cucsExtvmmFabricNetworkRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkRn.setStatus(_A)
_CucsExtvmmFabricNetworkDescr_Type=SnmpAdminString
_CucsExtvmmFabricNetworkDescr_Object=MibTableColumn
cucsExtvmmFabricNetworkDescr=_CucsExtvmmFabricNetworkDescr_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,4),_CucsExtvmmFabricNetworkDescr_Type())
cucsExtvmmFabricNetworkDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDescr.setStatus(_A)
_CucsExtvmmFabricNetworkGuid_Type=SnmpAdminString
_CucsExtvmmFabricNetworkGuid_Object=MibTableColumn
cucsExtvmmFabricNetworkGuid=_CucsExtvmmFabricNetworkGuid_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,5),_CucsExtvmmFabricNetworkGuid_Type())
cucsExtvmmFabricNetworkGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkGuid.setStatus(_A)
_CucsExtvmmFabricNetworkIntId_Type=SnmpAdminString
_CucsExtvmmFabricNetworkIntId_Object=MibTableColumn
cucsExtvmmFabricNetworkIntId=_CucsExtvmmFabricNetworkIntId_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,6),_CucsExtvmmFabricNetworkIntId_Type())
cucsExtvmmFabricNetworkIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkIntId.setStatus(_A)
_CucsExtvmmFabricNetworkName_Type=SnmpAdminString
_CucsExtvmmFabricNetworkName_Object=MibTableColumn
cucsExtvmmFabricNetworkName=_CucsExtvmmFabricNetworkName_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,7),_CucsExtvmmFabricNetworkName_Type())
cucsExtvmmFabricNetworkName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkName.setStatus(_A)
_CucsExtvmmFabricNetworkNetworkType_Type=CucsExtvmmFabricNetworkType
_CucsExtvmmFabricNetworkNetworkType_Object=MibTableColumn
cucsExtvmmFabricNetworkNetworkType=_CucsExtvmmFabricNetworkNetworkType_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,8),_CucsExtvmmFabricNetworkNetworkType_Type())
cucsExtvmmFabricNetworkNetworkType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkNetworkType.setStatus(_A)
_CucsExtvmmFabricNetworkPolicyLevel_Type=Gauge32
_CucsExtvmmFabricNetworkPolicyLevel_Object=MibTableColumn
cucsExtvmmFabricNetworkPolicyLevel=_CucsExtvmmFabricNetworkPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,9),_CucsExtvmmFabricNetworkPolicyLevel_Type())
cucsExtvmmFabricNetworkPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkPolicyLevel.setStatus(_A)
_CucsExtvmmFabricNetworkPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtvmmFabricNetworkPolicyOwner_Object=MibTableColumn
cucsExtvmmFabricNetworkPolicyOwner=_CucsExtvmmFabricNetworkPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,10),_CucsExtvmmFabricNetworkPolicyOwner_Type())
cucsExtvmmFabricNetworkPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkPolicyOwner.setStatus(_A)
_CucsExtvmmFabricNetworkRefOperState_Type=CucsExtvmmRefOperState
_CucsExtvmmFabricNetworkRefOperState_Object=MibTableColumn
cucsExtvmmFabricNetworkRefOperState=_CucsExtvmmFabricNetworkRefOperState_Object((1,3,6,1,4,1,9,9,719,1,18,25,1,11),_CucsExtvmmFabricNetworkRefOperState_Type())
cucsExtvmmFabricNetworkRefOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkRefOperState.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionTable_Object=MibTable
cucsExtvmmFabricNetworkDefinitionTable=_CucsExtvmmFabricNetworkDefinitionTable_Object((1,3,6,1,4,1,9,9,719,1,18,26))
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionTable.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionEntry_Object=MibTableRow
cucsExtvmmFabricNetworkDefinitionEntry=_CucsExtvmmFabricNetworkDefinitionEntry_Object((1,3,6,1,4,1,9,9,719,1,18,26,1))
cucsExtvmmFabricNetworkDefinitionEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionEntry.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionInstanceId_Type=CucsManagedObjectId
_CucsExtvmmFabricNetworkDefinitionInstanceId_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionInstanceId=_CucsExtvmmFabricNetworkDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,1),_CucsExtvmmFabricNetworkDefinitionInstanceId_Type())
cucsExtvmmFabricNetworkDefinitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionInstanceId.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionDn_Type=CucsManagedObjectDn
_CucsExtvmmFabricNetworkDefinitionDn_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionDn=_CucsExtvmmFabricNetworkDefinitionDn_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,2),_CucsExtvmmFabricNetworkDefinitionDn_Type())
cucsExtvmmFabricNetworkDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionDn.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionRn_Type=SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionRn_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionRn=_CucsExtvmmFabricNetworkDefinitionRn_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,3),_CucsExtvmmFabricNetworkDefinitionRn_Type())
cucsExtvmmFabricNetworkDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionRn.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionAllowedVnicType_Type=CucsExtvmmVnicType
_CucsExtvmmFabricNetworkDefinitionAllowedVnicType_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionAllowedVnicType=_CucsExtvmmFabricNetworkDefinitionAllowedVnicType_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,4),_CucsExtvmmFabricNetworkDefinitionAllowedVnicType_Type())
cucsExtvmmFabricNetworkDefinitionAllowedVnicType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionAllowedVnicType.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionDescr_Type=SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionDescr_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionDescr=_CucsExtvmmFabricNetworkDefinitionDescr_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,5),_CucsExtvmmFabricNetworkDefinitionDescr_Type())
cucsExtvmmFabricNetworkDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionDescr.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionGuid_Type=SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionGuid_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionGuid=_CucsExtvmmFabricNetworkDefinitionGuid_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,6),_CucsExtvmmFabricNetworkDefinitionGuid_Type())
cucsExtvmmFabricNetworkDefinitionGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionGuid.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionIntId_Type=SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionIntId_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionIntId=_CucsExtvmmFabricNetworkDefinitionIntId_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,7),_CucsExtvmmFabricNetworkDefinitionIntId_Type())
cucsExtvmmFabricNetworkDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionIntId.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionName_Type=SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionName_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionName=_CucsExtvmmFabricNetworkDefinitionName_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,8),_CucsExtvmmFabricNetworkDefinitionName_Type())
cucsExtvmmFabricNetworkDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionName.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionPolicyLevel_Type=Gauge32
_CucsExtvmmFabricNetworkDefinitionPolicyLevel_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionPolicyLevel=_CucsExtvmmFabricNetworkDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,9),_CucsExtvmmFabricNetworkDefinitionPolicyLevel_Type())
cucsExtvmmFabricNetworkDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionPolicyLevel.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtvmmFabricNetworkDefinitionPolicyOwner_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionPolicyOwner=_CucsExtvmmFabricNetworkDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,10),_CucsExtvmmFabricNetworkDefinitionPolicyOwner_Type())
cucsExtvmmFabricNetworkDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionPolicyOwner.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionPrimaryVlanId_Type=Gauge32
_CucsExtvmmFabricNetworkDefinitionPrimaryVlanId_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionPrimaryVlanId=_CucsExtvmmFabricNetworkDefinitionPrimaryVlanId_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,11),_CucsExtvmmFabricNetworkDefinitionPrimaryVlanId_Type())
cucsExtvmmFabricNetworkDefinitionPrimaryVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionPrimaryVlanId.setStatus(_A)
_CucsExtvmmFabricNetworkDefinitionRefOperState_Type=CucsExtvmmRefOperState
_CucsExtvmmFabricNetworkDefinitionRefOperState_Object=MibTableColumn
cucsExtvmmFabricNetworkDefinitionRefOperState=_CucsExtvmmFabricNetworkDefinitionRefOperState_Object((1,3,6,1,4,1,9,9,719,1,18,26,1,12),_CucsExtvmmFabricNetworkDefinitionRefOperState_Type())
cucsExtvmmFabricNetworkDefinitionRefOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmFabricNetworkDefinitionRefOperState.setStatus(_A)
_CucsExtvmmNetworkSetsTable_Object=MibTable
cucsExtvmmNetworkSetsTable=_CucsExtvmmNetworkSetsTable_Object((1,3,6,1,4,1,9,9,719,1,18,27))
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsTable.setStatus(_A)
_CucsExtvmmNetworkSetsEntry_Object=MibTableRow
cucsExtvmmNetworkSetsEntry=_CucsExtvmmNetworkSetsEntry_Object((1,3,6,1,4,1,9,9,719,1,18,27,1))
cucsExtvmmNetworkSetsEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsEntry.setStatus(_A)
_CucsExtvmmNetworkSetsInstanceId_Type=CucsManagedObjectId
_CucsExtvmmNetworkSetsInstanceId_Object=MibTableColumn
cucsExtvmmNetworkSetsInstanceId=_CucsExtvmmNetworkSetsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,1),_CucsExtvmmNetworkSetsInstanceId_Type())
cucsExtvmmNetworkSetsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsInstanceId.setStatus(_A)
_CucsExtvmmNetworkSetsDn_Type=CucsManagedObjectDn
_CucsExtvmmNetworkSetsDn_Object=MibTableColumn
cucsExtvmmNetworkSetsDn=_CucsExtvmmNetworkSetsDn_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,2),_CucsExtvmmNetworkSetsDn_Type())
cucsExtvmmNetworkSetsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsDn.setStatus(_A)
_CucsExtvmmNetworkSetsRn_Type=SnmpAdminString
_CucsExtvmmNetworkSetsRn_Object=MibTableColumn
cucsExtvmmNetworkSetsRn=_CucsExtvmmNetworkSetsRn_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,3),_CucsExtvmmNetworkSetsRn_Type())
cucsExtvmmNetworkSetsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsRn.setStatus(_A)
_CucsExtvmmNetworkSetsFltAggr_Type=Unsigned64
_CucsExtvmmNetworkSetsFltAggr_Object=MibTableColumn
cucsExtvmmNetworkSetsFltAggr=_CucsExtvmmNetworkSetsFltAggr_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,4),_CucsExtvmmNetworkSetsFltAggr_Type())
cucsExtvmmNetworkSetsFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFltAggr.setStatus(_A)
_CucsExtvmmNetworkSetsFsmDescr_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmDescr_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmDescr=_CucsExtvmmNetworkSetsFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,5),_CucsExtvmmNetworkSetsFsmDescr_Type())
cucsExtvmmNetworkSetsFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmDescr.setStatus(_A)
_CucsExtvmmNetworkSetsFsmPrev_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmPrev_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmPrev=_CucsExtvmmNetworkSetsFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,6),_CucsExtvmmNetworkSetsFsmPrev_Type())
cucsExtvmmNetworkSetsFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmPrev.setStatus(_A)
_CucsExtvmmNetworkSetsFsmProgr_Type=Gauge32
_CucsExtvmmNetworkSetsFsmProgr_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmProgr=_CucsExtvmmNetworkSetsFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,7),_CucsExtvmmNetworkSetsFsmProgr_Type())
cucsExtvmmNetworkSetsFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmProgr.setStatus(_A)
_CucsExtvmmNetworkSetsFsmRmtInvErrCode_Type=Gauge32
_CucsExtvmmNetworkSetsFsmRmtInvErrCode_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmRmtInvErrCode=_CucsExtvmmNetworkSetsFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,8),_CucsExtvmmNetworkSetsFsmRmtInvErrCode_Type())
cucsExtvmmNetworkSetsFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmRmtInvErrCode.setStatus(_A)
_CucsExtvmmNetworkSetsFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmRmtInvErrDescr_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmRmtInvErrDescr=_CucsExtvmmNetworkSetsFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,9),_CucsExtvmmNetworkSetsFsmRmtInvErrDescr_Type())
cucsExtvmmNetworkSetsFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmRmtInvErrDescr.setStatus(_A)
_CucsExtvmmNetworkSetsFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmNetworkSetsFsmRmtInvRslt_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmRmtInvRslt=_CucsExtvmmNetworkSetsFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,10),_CucsExtvmmNetworkSetsFsmRmtInvRslt_Type())
cucsExtvmmNetworkSetsFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmRmtInvRslt.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageDescr_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmStageDescr_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageDescr=_CucsExtvmmNetworkSetsFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,11),_CucsExtvmmNetworkSetsFsmStageDescr_Type())
cucsExtvmmNetworkSetsFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageDescr.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStamp_Type=DateAndTime
_CucsExtvmmNetworkSetsFsmStamp_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStamp=_CucsExtvmmNetworkSetsFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,12),_CucsExtvmmNetworkSetsFsmStamp_Type())
cucsExtvmmNetworkSetsFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStamp.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStatus_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmStatus_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStatus=_CucsExtvmmNetworkSetsFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,13),_CucsExtvmmNetworkSetsFsmStatus_Type())
cucsExtvmmNetworkSetsFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStatus.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTry_Type=Gauge32
_CucsExtvmmNetworkSetsFsmTry_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmTry=_CucsExtvmmNetworkSetsFsmTry_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,14),_CucsExtvmmNetworkSetsFsmTry_Type())
cucsExtvmmNetworkSetsFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTry.setStatus(_A)
_CucsExtvmmNetworkSetsGenNum_Type=Gauge32
_CucsExtvmmNetworkSetsGenNum_Object=MibTableColumn
cucsExtvmmNetworkSetsGenNum=_CucsExtvmmNetworkSetsGenNum_Object((1,3,6,1,4,1,9,9,719,1,18,27,1,15),_CucsExtvmmNetworkSetsGenNum_Type())
cucsExtvmmNetworkSetsGenNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsGenNum.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTable_Object=MibTable
cucsExtvmmNetworkSetsFsmTable=_CucsExtvmmNetworkSetsFsmTable_Object((1,3,6,1,4,1,9,9,719,1,18,28))
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTable.setStatus(_A)
_CucsExtvmmNetworkSetsFsmEntry_Object=MibTableRow
cucsExtvmmNetworkSetsFsmEntry=_CucsExtvmmNetworkSetsFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,18,28,1))
cucsExtvmmNetworkSetsFsmEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmEntry.setStatus(_A)
_CucsExtvmmNetworkSetsFsmInstanceId_Type=CucsManagedObjectId
_CucsExtvmmNetworkSetsFsmInstanceId_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmInstanceId=_CucsExtvmmNetworkSetsFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,1),_CucsExtvmmNetworkSetsFsmInstanceId_Type())
cucsExtvmmNetworkSetsFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmInstanceId.setStatus(_A)
_CucsExtvmmNetworkSetsFsmDn_Type=CucsManagedObjectDn
_CucsExtvmmNetworkSetsFsmDn_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmDn=_CucsExtvmmNetworkSetsFsmDn_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,2),_CucsExtvmmNetworkSetsFsmDn_Type())
cucsExtvmmNetworkSetsFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmDn.setStatus(_A)
_CucsExtvmmNetworkSetsFsmRn_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmRn_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmRn=_CucsExtvmmNetworkSetsFsmRn_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,3),_CucsExtvmmNetworkSetsFsmRn_Type())
cucsExtvmmNetworkSetsFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmRn.setStatus(_A)
_CucsExtvmmNetworkSetsFsmCompletionTime_Type=DateAndTime
_CucsExtvmmNetworkSetsFsmCompletionTime_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmCompletionTime=_CucsExtvmmNetworkSetsFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,4),_CucsExtvmmNetworkSetsFsmCompletionTime_Type())
cucsExtvmmNetworkSetsFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmCompletionTime.setStatus(_A)
_CucsExtvmmNetworkSetsFsmCurrentFsm_Type=CucsExtvmmNetworkSetsFsmCurrentFsm
_CucsExtvmmNetworkSetsFsmCurrentFsm_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmCurrentFsm=_CucsExtvmmNetworkSetsFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,5),_CucsExtvmmNetworkSetsFsmCurrentFsm_Type())
cucsExtvmmNetworkSetsFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmCurrentFsm.setStatus(_A)
_CucsExtvmmNetworkSetsFsmDescrData_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmDescrData_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmDescrData=_CucsExtvmmNetworkSetsFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,6),_CucsExtvmmNetworkSetsFsmDescrData_Type())
cucsExtvmmNetworkSetsFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmDescrData.setStatus(_A)
_CucsExtvmmNetworkSetsFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmNetworkSetsFsmFsmStatus_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmFsmStatus=_CucsExtvmmNetworkSetsFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,7),_CucsExtvmmNetworkSetsFsmFsmStatus_Type())
cucsExtvmmNetworkSetsFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmFsmStatus.setStatus(_A)
_CucsExtvmmNetworkSetsFsmProgress_Type=Gauge32
_CucsExtvmmNetworkSetsFsmProgress_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmProgress=_CucsExtvmmNetworkSetsFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,8),_CucsExtvmmNetworkSetsFsmProgress_Type())
cucsExtvmmNetworkSetsFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmProgress.setStatus(_A)
_CucsExtvmmNetworkSetsFsmRmtErrCode_Type=Gauge32
_CucsExtvmmNetworkSetsFsmRmtErrCode_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmRmtErrCode=_CucsExtvmmNetworkSetsFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,9),_CucsExtvmmNetworkSetsFsmRmtErrCode_Type())
cucsExtvmmNetworkSetsFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmRmtErrCode.setStatus(_A)
_CucsExtvmmNetworkSetsFsmRmtErrDescr_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmRmtErrDescr_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmRmtErrDescr=_CucsExtvmmNetworkSetsFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,10),_CucsExtvmmNetworkSetsFsmRmtErrDescr_Type())
cucsExtvmmNetworkSetsFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmRmtErrDescr.setStatus(_A)
_CucsExtvmmNetworkSetsFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsExtvmmNetworkSetsFsmRmtRslt_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmRmtRslt=_CucsExtvmmNetworkSetsFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,18,28,1,11),_CucsExtvmmNetworkSetsFsmRmtRslt_Type())
cucsExtvmmNetworkSetsFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmRmtRslt.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageTable_Object=MibTable
cucsExtvmmNetworkSetsFsmStageTable=_CucsExtvmmNetworkSetsFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,18,29))
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageTable.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageEntry_Object=MibTableRow
cucsExtvmmNetworkSetsFsmStageEntry=_CucsExtvmmNetworkSetsFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,18,29,1))
cucsExtvmmNetworkSetsFsmStageEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageEntry.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageInstanceId_Type=CucsManagedObjectId
_CucsExtvmmNetworkSetsFsmStageInstanceId_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageInstanceId=_CucsExtvmmNetworkSetsFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,29,1,1),_CucsExtvmmNetworkSetsFsmStageInstanceId_Type())
cucsExtvmmNetworkSetsFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageInstanceId.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageDn_Type=CucsManagedObjectDn
_CucsExtvmmNetworkSetsFsmStageDn_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageDn=_CucsExtvmmNetworkSetsFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,18,29,1,2),_CucsExtvmmNetworkSetsFsmStageDn_Type())
cucsExtvmmNetworkSetsFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageDn.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageRn_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmStageRn_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageRn=_CucsExtvmmNetworkSetsFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,18,29,1,3),_CucsExtvmmNetworkSetsFsmStageRn_Type())
cucsExtvmmNetworkSetsFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageRn.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageDescrData_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmStageDescrData_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageDescrData=_CucsExtvmmNetworkSetsFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,18,29,1,4),_CucsExtvmmNetworkSetsFsmStageDescrData_Type())
cucsExtvmmNetworkSetsFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageDescrData.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageLastUpdateTime_Type=DateAndTime
_CucsExtvmmNetworkSetsFsmStageLastUpdateTime_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageLastUpdateTime=_CucsExtvmmNetworkSetsFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,18,29,1,5),_CucsExtvmmNetworkSetsFsmStageLastUpdateTime_Type())
cucsExtvmmNetworkSetsFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageLastUpdateTime.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageName_Type=CucsExtvmmNetworkSetsFsmStageName
_CucsExtvmmNetworkSetsFsmStageName_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageName=_CucsExtvmmNetworkSetsFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,18,29,1,6),_CucsExtvmmNetworkSetsFsmStageName_Type())
cucsExtvmmNetworkSetsFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageName.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageOrder_Type=Gauge32
_CucsExtvmmNetworkSetsFsmStageOrder_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageOrder=_CucsExtvmmNetworkSetsFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,18,29,1,7),_CucsExtvmmNetworkSetsFsmStageOrder_Type())
cucsExtvmmNetworkSetsFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageOrder.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageRetry_Type=Gauge32
_CucsExtvmmNetworkSetsFsmStageRetry_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageRetry=_CucsExtvmmNetworkSetsFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,18,29,1,8),_CucsExtvmmNetworkSetsFsmStageRetry_Type())
cucsExtvmmNetworkSetsFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageRetry.setStatus(_A)
_CucsExtvmmNetworkSetsFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsExtvmmNetworkSetsFsmStageStageStatus_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmStageStageStatus=_CucsExtvmmNetworkSetsFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,18,29,1,9),_CucsExtvmmNetworkSetsFsmStageStageStatus_Type())
cucsExtvmmNetworkSetsFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmStageStageStatus.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTaskTable_Object=MibTable
cucsExtvmmNetworkSetsFsmTaskTable=_CucsExtvmmNetworkSetsFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,18,30))
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTaskTable.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTaskEntry_Object=MibTableRow
cucsExtvmmNetworkSetsFsmTaskEntry=_CucsExtvmmNetworkSetsFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,18,30,1))
cucsExtvmmNetworkSetsFsmTaskEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTaskEntry.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsExtvmmNetworkSetsFsmTaskInstanceId_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmTaskInstanceId=_CucsExtvmmNetworkSetsFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,30,1,1),_CucsExtvmmNetworkSetsFsmTaskInstanceId_Type())
cucsExtvmmNetworkSetsFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTaskInstanceId.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTaskDn_Type=CucsManagedObjectDn
_CucsExtvmmNetworkSetsFsmTaskDn_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmTaskDn=_CucsExtvmmNetworkSetsFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,18,30,1,2),_CucsExtvmmNetworkSetsFsmTaskDn_Type())
cucsExtvmmNetworkSetsFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTaskDn.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTaskRn_Type=SnmpAdminString
_CucsExtvmmNetworkSetsFsmTaskRn_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmTaskRn=_CucsExtvmmNetworkSetsFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,18,30,1,3),_CucsExtvmmNetworkSetsFsmTaskRn_Type())
cucsExtvmmNetworkSetsFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTaskRn.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTaskCompletion_Type=CucsFsmCompletion
_CucsExtvmmNetworkSetsFsmTaskCompletion_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmTaskCompletion=_CucsExtvmmNetworkSetsFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,18,30,1,4),_CucsExtvmmNetworkSetsFsmTaskCompletion_Type())
cucsExtvmmNetworkSetsFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTaskCompletion.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTaskFlags_Type=CucsFsmFlags
_CucsExtvmmNetworkSetsFsmTaskFlags_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmTaskFlags=_CucsExtvmmNetworkSetsFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,18,30,1,5),_CucsExtvmmNetworkSetsFsmTaskFlags_Type())
cucsExtvmmNetworkSetsFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTaskFlags.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTaskItem_Type=CucsExtvmmNetworkSetsFsmTaskItem
_CucsExtvmmNetworkSetsFsmTaskItem_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmTaskItem=_CucsExtvmmNetworkSetsFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,18,30,1,6),_CucsExtvmmNetworkSetsFsmTaskItem_Type())
cucsExtvmmNetworkSetsFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTaskItem.setStatus(_A)
_CucsExtvmmNetworkSetsFsmTaskSeqId_Type=Gauge32
_CucsExtvmmNetworkSetsFsmTaskSeqId_Object=MibTableColumn
cucsExtvmmNetworkSetsFsmTaskSeqId=_CucsExtvmmNetworkSetsFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,18,30,1,7),_CucsExtvmmNetworkSetsFsmTaskSeqId_Type())
cucsExtvmmNetworkSetsFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmNetworkSetsFsmTaskSeqId.setStatus(_A)
_CucsExtvmmUpLinkPPTable_Object=MibTable
cucsExtvmmUpLinkPPTable=_CucsExtvmmUpLinkPPTable_Object((1,3,6,1,4,1,9,9,719,1,18,31))
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPTable.setStatus(_A)
_CucsExtvmmUpLinkPPEntry_Object=MibTableRow
cucsExtvmmUpLinkPPEntry=_CucsExtvmmUpLinkPPEntry_Object((1,3,6,1,4,1,9,9,719,1,18,31,1))
cucsExtvmmUpLinkPPEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPEntry.setStatus(_A)
_CucsExtvmmUpLinkPPInstanceId_Type=CucsManagedObjectId
_CucsExtvmmUpLinkPPInstanceId_Object=MibTableColumn
cucsExtvmmUpLinkPPInstanceId=_CucsExtvmmUpLinkPPInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,1),_CucsExtvmmUpLinkPPInstanceId_Type())
cucsExtvmmUpLinkPPInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPInstanceId.setStatus(_A)
_CucsExtvmmUpLinkPPDn_Type=CucsManagedObjectDn
_CucsExtvmmUpLinkPPDn_Object=MibTableColumn
cucsExtvmmUpLinkPPDn=_CucsExtvmmUpLinkPPDn_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,2),_CucsExtvmmUpLinkPPDn_Type())
cucsExtvmmUpLinkPPDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPDn.setStatus(_A)
_CucsExtvmmUpLinkPPRn_Type=SnmpAdminString
_CucsExtvmmUpLinkPPRn_Object=MibTableColumn
cucsExtvmmUpLinkPPRn=_CucsExtvmmUpLinkPPRn_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,3),_CucsExtvmmUpLinkPPRn_Type())
cucsExtvmmUpLinkPPRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPRn.setStatus(_A)
_CucsExtvmmUpLinkPPDescr_Type=SnmpAdminString
_CucsExtvmmUpLinkPPDescr_Object=MibTableColumn
cucsExtvmmUpLinkPPDescr=_CucsExtvmmUpLinkPPDescr_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,4),_CucsExtvmmUpLinkPPDescr_Type())
cucsExtvmmUpLinkPPDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPDescr.setStatus(_A)
_CucsExtvmmUpLinkPPFltAggr_Type=Unsigned64
_CucsExtvmmUpLinkPPFltAggr_Object=MibTableColumn
cucsExtvmmUpLinkPPFltAggr=_CucsExtvmmUpLinkPPFltAggr_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,5),_CucsExtvmmUpLinkPPFltAggr_Type())
cucsExtvmmUpLinkPPFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPFltAggr.setStatus(_A)
_CucsExtvmmUpLinkPPGuid_Type=SnmpAdminString
_CucsExtvmmUpLinkPPGuid_Object=MibTableColumn
cucsExtvmmUpLinkPPGuid=_CucsExtvmmUpLinkPPGuid_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,6),_CucsExtvmmUpLinkPPGuid_Type())
cucsExtvmmUpLinkPPGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPGuid.setStatus(_A)
_CucsExtvmmUpLinkPPIntId_Type=SnmpAdminString
_CucsExtvmmUpLinkPPIntId_Object=MibTableColumn
cucsExtvmmUpLinkPPIntId=_CucsExtvmmUpLinkPPIntId_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,7),_CucsExtvmmUpLinkPPIntId_Type())
cucsExtvmmUpLinkPPIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPIntId.setStatus(_A)
_CucsExtvmmUpLinkPPName_Type=SnmpAdminString
_CucsExtvmmUpLinkPPName_Object=MibTableColumn
cucsExtvmmUpLinkPPName=_CucsExtvmmUpLinkPPName_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,8),_CucsExtvmmUpLinkPPName_Type())
cucsExtvmmUpLinkPPName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPName.setStatus(_A)
_CucsExtvmmUpLinkPPPolicyLevel_Type=Gauge32
_CucsExtvmmUpLinkPPPolicyLevel_Object=MibTableColumn
cucsExtvmmUpLinkPPPolicyLevel=_CucsExtvmmUpLinkPPPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,9),_CucsExtvmmUpLinkPPPolicyLevel_Type())
cucsExtvmmUpLinkPPPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPPolicyLevel.setStatus(_A)
_CucsExtvmmUpLinkPPPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtvmmUpLinkPPPolicyOwner_Object=MibTableColumn
cucsExtvmmUpLinkPPPolicyOwner=_CucsExtvmmUpLinkPPPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,10),_CucsExtvmmUpLinkPPPolicyOwner_Type())
cucsExtvmmUpLinkPPPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPPolicyOwner.setStatus(_A)
_CucsExtvmmUpLinkPPRefOperState_Type=CucsExtvmmRefOperState
_CucsExtvmmUpLinkPPRefOperState_Object=MibTableColumn
cucsExtvmmUpLinkPPRefOperState=_CucsExtvmmUpLinkPPRefOperState_Object((1,3,6,1,4,1,9,9,719,1,18,31,1,11),_CucsExtvmmUpLinkPPRefOperState_Type())
cucsExtvmmUpLinkPPRefOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmUpLinkPPRefOperState.setStatus(_A)
_CucsExtvmmVMNDRefTable_Object=MibTable
cucsExtvmmVMNDRefTable=_CucsExtvmmVMNDRefTable_Object((1,3,6,1,4,1,9,9,719,1,18,32))
if mibBuilder.loadTexts:cucsExtvmmVMNDRefTable.setStatus(_A)
_CucsExtvmmVMNDRefEntry_Object=MibTableRow
cucsExtvmmVMNDRefEntry=_CucsExtvmmVMNDRefEntry_Object((1,3,6,1,4,1,9,9,719,1,18,32,1))
cucsExtvmmVMNDRefEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:cucsExtvmmVMNDRefEntry.setStatus(_A)
_CucsExtvmmVMNDRefInstanceId_Type=CucsManagedObjectId
_CucsExtvmmVMNDRefInstanceId_Object=MibTableColumn
cucsExtvmmVMNDRefInstanceId=_CucsExtvmmVMNDRefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,1),_CucsExtvmmVMNDRefInstanceId_Type())
cucsExtvmmVMNDRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefInstanceId.setStatus(_A)
_CucsExtvmmVMNDRefDn_Type=CucsManagedObjectDn
_CucsExtvmmVMNDRefDn_Object=MibTableColumn
cucsExtvmmVMNDRefDn=_CucsExtvmmVMNDRefDn_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,2),_CucsExtvmmVMNDRefDn_Type())
cucsExtvmmVMNDRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefDn.setStatus(_A)
_CucsExtvmmVMNDRefRn_Type=SnmpAdminString
_CucsExtvmmVMNDRefRn_Object=MibTableColumn
cucsExtvmmVMNDRefRn=_CucsExtvmmVMNDRefRn_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,3),_CucsExtvmmVMNDRefRn_Type())
cucsExtvmmVMNDRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefRn.setStatus(_A)
_CucsExtvmmVMNDRefConfigQualifier_Type=CucsExtvmmNetworkSetConfigQualifier
_CucsExtvmmVMNDRefConfigQualifier_Object=MibTableColumn
cucsExtvmmVMNDRefConfigQualifier=_CucsExtvmmVMNDRefConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,4),_CucsExtvmmVMNDRefConfigQualifier_Type())
cucsExtvmmVMNDRefConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefConfigQualifier.setStatus(_A)
_CucsExtvmmVMNDRefDescr_Type=SnmpAdminString
_CucsExtvmmVMNDRefDescr_Object=MibTableColumn
cucsExtvmmVMNDRefDescr=_CucsExtvmmVMNDRefDescr_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,5),_CucsExtvmmVMNDRefDescr_Type())
cucsExtvmmVMNDRefDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefDescr.setStatus(_A)
_CucsExtvmmVMNDRefFnDefName_Type=SnmpAdminString
_CucsExtvmmVMNDRefFnDefName_Object=MibTableColumn
cucsExtvmmVMNDRefFnDefName=_CucsExtvmmVMNDRefFnDefName_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,6),_CucsExtvmmVMNDRefFnDefName_Type())
cucsExtvmmVMNDRefFnDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefFnDefName.setStatus(_A)
_CucsExtvmmVMNDRefFnName_Type=SnmpAdminString
_CucsExtvmmVMNDRefFnName_Object=MibTableColumn
cucsExtvmmVMNDRefFnName=_CucsExtvmmVMNDRefFnName_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,7),_CucsExtvmmVMNDRefFnName_Type())
cucsExtvmmVMNDRefFnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefFnName.setStatus(_A)
_CucsExtvmmVMNDRefIntId_Type=SnmpAdminString
_CucsExtvmmVMNDRefIntId_Object=MibTableColumn
cucsExtvmmVMNDRefIntId=_CucsExtvmmVMNDRefIntId_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,8),_CucsExtvmmVMNDRefIntId_Type())
cucsExtvmmVMNDRefIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefIntId.setStatus(_A)
_CucsExtvmmVMNDRefName_Type=SnmpAdminString
_CucsExtvmmVMNDRefName_Object=MibTableColumn
cucsExtvmmVMNDRefName=_CucsExtvmmVMNDRefName_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,9),_CucsExtvmmVMNDRefName_Type())
cucsExtvmmVMNDRefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefName.setStatus(_A)
_CucsExtvmmVMNDRefOperVmNetworkDefName_Type=SnmpAdminString
_CucsExtvmmVMNDRefOperVmNetworkDefName_Object=MibTableColumn
cucsExtvmmVMNDRefOperVmNetworkDefName=_CucsExtvmmVMNDRefOperVmNetworkDefName_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,10),_CucsExtvmmVMNDRefOperVmNetworkDefName_Type())
cucsExtvmmVMNDRefOperVmNetworkDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefOperVmNetworkDefName.setStatus(_A)
_CucsExtvmmVMNDRefPolicyLevel_Type=Gauge32
_CucsExtvmmVMNDRefPolicyLevel_Object=MibTableColumn
cucsExtvmmVMNDRefPolicyLevel=_CucsExtvmmVMNDRefPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,11),_CucsExtvmmVMNDRefPolicyLevel_Type())
cucsExtvmmVMNDRefPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefPolicyLevel.setStatus(_A)
_CucsExtvmmVMNDRefPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtvmmVMNDRefPolicyOwner_Object=MibTableColumn
cucsExtvmmVMNDRefPolicyOwner=_CucsExtvmmVMNDRefPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,12),_CucsExtvmmVMNDRefPolicyOwner_Type())
cucsExtvmmVMNDRefPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefPolicyOwner.setStatus(_A)
_CucsExtvmmVMNDRefVmNetworkDefName_Type=SnmpAdminString
_CucsExtvmmVMNDRefVmNetworkDefName_Object=MibTableColumn
cucsExtvmmVMNDRefVmNetworkDefName=_CucsExtvmmVMNDRefVmNetworkDefName_Object((1,3,6,1,4,1,9,9,719,1,18,32,1,13),_CucsExtvmmVMNDRefVmNetworkDefName_Type())
cucsExtvmmVMNDRefVmNetworkDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNDRefVmNetworkDefName.setStatus(_A)
_CucsExtvmmVMNetworkTable_Object=MibTable
cucsExtvmmVMNetworkTable=_CucsExtvmmVMNetworkTable_Object((1,3,6,1,4,1,9,9,719,1,18,33))
if mibBuilder.loadTexts:cucsExtvmmVMNetworkTable.setStatus(_A)
_CucsExtvmmVMNetworkEntry_Object=MibTableRow
cucsExtvmmVMNetworkEntry=_CucsExtvmmVMNetworkEntry_Object((1,3,6,1,4,1,9,9,719,1,18,33,1))
cucsExtvmmVMNetworkEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:cucsExtvmmVMNetworkEntry.setStatus(_A)
_CucsExtvmmVMNetworkInstanceId_Type=CucsManagedObjectId
_CucsExtvmmVMNetworkInstanceId_Object=MibTableColumn
cucsExtvmmVMNetworkInstanceId=_CucsExtvmmVMNetworkInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,1),_CucsExtvmmVMNetworkInstanceId_Type())
cucsExtvmmVMNetworkInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkInstanceId.setStatus(_A)
_CucsExtvmmVMNetworkDn_Type=CucsManagedObjectDn
_CucsExtvmmVMNetworkDn_Object=MibTableColumn
cucsExtvmmVMNetworkDn=_CucsExtvmmVMNetworkDn_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,2),_CucsExtvmmVMNetworkDn_Type())
cucsExtvmmVMNetworkDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDn.setStatus(_A)
_CucsExtvmmVMNetworkRn_Type=SnmpAdminString
_CucsExtvmmVMNetworkRn_Object=MibTableColumn
cucsExtvmmVMNetworkRn=_CucsExtvmmVMNetworkRn_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,3),_CucsExtvmmVMNetworkRn_Type())
cucsExtvmmVMNetworkRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkRn.setStatus(_A)
_CucsExtvmmVMNetworkDescr_Type=SnmpAdminString
_CucsExtvmmVMNetworkDescr_Object=MibTableColumn
cucsExtvmmVMNetworkDescr=_CucsExtvmmVMNetworkDescr_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,4),_CucsExtvmmVMNetworkDescr_Type())
cucsExtvmmVMNetworkDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDescr.setStatus(_A)
_CucsExtvmmVMNetworkFabricNetworkName_Type=SnmpAdminString
_CucsExtvmmVMNetworkFabricNetworkName_Object=MibTableColumn
cucsExtvmmVMNetworkFabricNetworkName=_CucsExtvmmVMNetworkFabricNetworkName_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,5),_CucsExtvmmVMNetworkFabricNetworkName_Type())
cucsExtvmmVMNetworkFabricNetworkName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkFabricNetworkName.setStatus(_A)
_CucsExtvmmVMNetworkFltAggr_Type=Unsigned64
_CucsExtvmmVMNetworkFltAggr_Object=MibTableColumn
cucsExtvmmVMNetworkFltAggr=_CucsExtvmmVMNetworkFltAggr_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,6),_CucsExtvmmVMNetworkFltAggr_Type())
cucsExtvmmVMNetworkFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkFltAggr.setStatus(_A)
_CucsExtvmmVMNetworkGuid_Type=SnmpAdminString
_CucsExtvmmVMNetworkGuid_Object=MibTableColumn
cucsExtvmmVMNetworkGuid=_CucsExtvmmVMNetworkGuid_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,7),_CucsExtvmmVMNetworkGuid_Type())
cucsExtvmmVMNetworkGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkGuid.setStatus(_A)
_CucsExtvmmVMNetworkIntId_Type=SnmpAdminString
_CucsExtvmmVMNetworkIntId_Object=MibTableColumn
cucsExtvmmVMNetworkIntId=_CucsExtvmmVMNetworkIntId_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,8),_CucsExtvmmVMNetworkIntId_Type())
cucsExtvmmVMNetworkIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkIntId.setStatus(_A)
_CucsExtvmmVMNetworkName_Type=SnmpAdminString
_CucsExtvmmVMNetworkName_Object=MibTableColumn
cucsExtvmmVMNetworkName=_CucsExtvmmVMNetworkName_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,9),_CucsExtvmmVMNetworkName_Type())
cucsExtvmmVMNetworkName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkName.setStatus(_A)
_CucsExtvmmVMNetworkOperFabricNetworkName_Type=SnmpAdminString
_CucsExtvmmVMNetworkOperFabricNetworkName_Object=MibTableColumn
cucsExtvmmVMNetworkOperFabricNetworkName=_CucsExtvmmVMNetworkOperFabricNetworkName_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,10),_CucsExtvmmVMNetworkOperFabricNetworkName_Type())
cucsExtvmmVMNetworkOperFabricNetworkName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkOperFabricNetworkName.setStatus(_A)
_CucsExtvmmVMNetworkPolicyLevel_Type=Gauge32
_CucsExtvmmVMNetworkPolicyLevel_Object=MibTableColumn
cucsExtvmmVMNetworkPolicyLevel=_CucsExtvmmVMNetworkPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,11),_CucsExtvmmVMNetworkPolicyLevel_Type())
cucsExtvmmVMNetworkPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkPolicyLevel.setStatus(_A)
_CucsExtvmmVMNetworkPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtvmmVMNetworkPolicyOwner_Object=MibTableColumn
cucsExtvmmVMNetworkPolicyOwner=_CucsExtvmmVMNetworkPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,18,33,1,12),_CucsExtvmmVMNetworkPolicyOwner_Type())
cucsExtvmmVMNetworkPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkPolicyOwner.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionTable_Object=MibTable
cucsExtvmmVMNetworkDefinitionTable=_CucsExtvmmVMNetworkDefinitionTable_Object((1,3,6,1,4,1,9,9,719,1,18,34))
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionTable.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionEntry_Object=MibTableRow
cucsExtvmmVMNetworkDefinitionEntry=_CucsExtvmmVMNetworkDefinitionEntry_Object((1,3,6,1,4,1,9,9,719,1,18,34,1))
cucsExtvmmVMNetworkDefinitionEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionEntry.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionInstanceId_Type=CucsManagedObjectId
_CucsExtvmmVMNetworkDefinitionInstanceId_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionInstanceId=_CucsExtvmmVMNetworkDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,1),_CucsExtvmmVMNetworkDefinitionInstanceId_Type())
cucsExtvmmVMNetworkDefinitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionInstanceId.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionDn_Type=CucsManagedObjectDn
_CucsExtvmmVMNetworkDefinitionDn_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionDn=_CucsExtvmmVMNetworkDefinitionDn_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,2),_CucsExtvmmVMNetworkDefinitionDn_Type())
cucsExtvmmVMNetworkDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionDn.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionRn_Type=SnmpAdminString
_CucsExtvmmVMNetworkDefinitionRn_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionRn=_CucsExtvmmVMNetworkDefinitionRn_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,3),_CucsExtvmmVMNetworkDefinitionRn_Type())
cucsExtvmmVMNetworkDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionRn.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionDescr_Type=SnmpAdminString
_CucsExtvmmVMNetworkDefinitionDescr_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionDescr=_CucsExtvmmVMNetworkDefinitionDescr_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,4),_CucsExtvmmVMNetworkDefinitionDescr_Type())
cucsExtvmmVMNetworkDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionDescr.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionExtIpPoolName_Type=SnmpAdminString
_CucsExtvmmVMNetworkDefinitionExtIpPoolName_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionExtIpPoolName=_CucsExtvmmVMNetworkDefinitionExtIpPoolName_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,5),_CucsExtvmmVMNetworkDefinitionExtIpPoolName_Type())
cucsExtvmmVMNetworkDefinitionExtIpPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionExtIpPoolName.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionGuid_Type=SnmpAdminString
_CucsExtvmmVMNetworkDefinitionGuid_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionGuid=_CucsExtvmmVMNetworkDefinitionGuid_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,6),_CucsExtvmmVMNetworkDefinitionGuid_Type())
cucsExtvmmVMNetworkDefinitionGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionGuid.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionIntId_Type=SnmpAdminString
_CucsExtvmmVMNetworkDefinitionIntId_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionIntId=_CucsExtvmmVMNetworkDefinitionIntId_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,7),_CucsExtvmmVMNetworkDefinitionIntId_Type())
cucsExtvmmVMNetworkDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionIntId.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionIpPoolGuid_Type=SnmpAdminString
_CucsExtvmmVMNetworkDefinitionIpPoolGuid_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionIpPoolGuid=_CucsExtvmmVMNetworkDefinitionIpPoolGuid_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,8),_CucsExtvmmVMNetworkDefinitionIpPoolGuid_Type())
cucsExtvmmVMNetworkDefinitionIpPoolGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionIpPoolGuid.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionMaxPorts_Type=Gauge32
_CucsExtvmmVMNetworkDefinitionMaxPorts_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionMaxPorts=_CucsExtvmmVMNetworkDefinitionMaxPorts_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,9),_CucsExtvmmVMNetworkDefinitionMaxPorts_Type())
cucsExtvmmVMNetworkDefinitionMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionMaxPorts.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionName_Type=SnmpAdminString
_CucsExtvmmVMNetworkDefinitionName_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionName=_CucsExtvmmVMNetworkDefinitionName_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,10),_CucsExtvmmVMNetworkDefinitionName_Type())
cucsExtvmmVMNetworkDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionName.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionOperExtIpPoolName_Type=SnmpAdminString
_CucsExtvmmVMNetworkDefinitionOperExtIpPoolName_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionOperExtIpPoolName=_CucsExtvmmVMNetworkDefinitionOperExtIpPoolName_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,11),_CucsExtvmmVMNetworkDefinitionOperExtIpPoolName_Type())
cucsExtvmmVMNetworkDefinitionOperExtIpPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionOperExtIpPoolName.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionPolicyLevel_Type=Gauge32
_CucsExtvmmVMNetworkDefinitionPolicyLevel_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionPolicyLevel=_CucsExtvmmVMNetworkDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,12),_CucsExtvmmVMNetworkDefinitionPolicyLevel_Type())
cucsExtvmmVMNetworkDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionPolicyLevel.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtvmmVMNetworkDefinitionPolicyOwner_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionPolicyOwner=_CucsExtvmmVMNetworkDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,13),_CucsExtvmmVMNetworkDefinitionPolicyOwner_Type())
cucsExtvmmVMNetworkDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionPolicyOwner.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionPrimaryVlanId_Type=Gauge32
_CucsExtvmmVMNetworkDefinitionPrimaryVlanId_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionPrimaryVlanId=_CucsExtvmmVMNetworkDefinitionPrimaryVlanId_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,14),_CucsExtvmmVMNetworkDefinitionPrimaryVlanId_Type())
cucsExtvmmVMNetworkDefinitionPrimaryVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionPrimaryVlanId.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionRefOperState_Type=CucsExtvmmRefOperState
_CucsExtvmmVMNetworkDefinitionRefOperState_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionRefOperState=_CucsExtvmmVMNetworkDefinitionRefOperState_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,15),_CucsExtvmmVMNetworkDefinitionRefOperState_Type())
cucsExtvmmVMNetworkDefinitionRefOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionRefOperState.setStatus(_A)
_CucsExtvmmVMNetworkDefinitionVlanName_Type=SnmpAdminString
_CucsExtvmmVMNetworkDefinitionVlanName_Object=MibTableColumn
cucsExtvmmVMNetworkDefinitionVlanName=_CucsExtvmmVMNetworkDefinitionVlanName_Object((1,3,6,1,4,1,9,9,719,1,18,34,1,16),_CucsExtvmmVMNetworkDefinitionVlanName_Type())
cucsExtvmmVMNetworkDefinitionVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkDefinitionVlanName.setStatus(_A)
_CucsExtvmmVMNetworkSetsTable_Object=MibTable
cucsExtvmmVMNetworkSetsTable=_CucsExtvmmVMNetworkSetsTable_Object((1,3,6,1,4,1,9,9,719,1,18,35))
if mibBuilder.loadTexts:cucsExtvmmVMNetworkSetsTable.setStatus(_A)
_CucsExtvmmVMNetworkSetsEntry_Object=MibTableRow
cucsExtvmmVMNetworkSetsEntry=_CucsExtvmmVMNetworkSetsEntry_Object((1,3,6,1,4,1,9,9,719,1,18,35,1))
cucsExtvmmVMNetworkSetsEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:cucsExtvmmVMNetworkSetsEntry.setStatus(_A)
_CucsExtvmmVMNetworkSetsInstanceId_Type=CucsManagedObjectId
_CucsExtvmmVMNetworkSetsInstanceId_Object=MibTableColumn
cucsExtvmmVMNetworkSetsInstanceId=_CucsExtvmmVMNetworkSetsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,18,35,1,1),_CucsExtvmmVMNetworkSetsInstanceId_Type())
cucsExtvmmVMNetworkSetsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkSetsInstanceId.setStatus(_A)
_CucsExtvmmVMNetworkSetsDn_Type=CucsManagedObjectDn
_CucsExtvmmVMNetworkSetsDn_Object=MibTableColumn
cucsExtvmmVMNetworkSetsDn=_CucsExtvmmVMNetworkSetsDn_Object((1,3,6,1,4,1,9,9,719,1,18,35,1,2),_CucsExtvmmVMNetworkSetsDn_Type())
cucsExtvmmVMNetworkSetsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkSetsDn.setStatus(_A)
_CucsExtvmmVMNetworkSetsRn_Type=SnmpAdminString
_CucsExtvmmVMNetworkSetsRn_Object=MibTableColumn
cucsExtvmmVMNetworkSetsRn=_CucsExtvmmVMNetworkSetsRn_Object((1,3,6,1,4,1,9,9,719,1,18,35,1,3),_CucsExtvmmVMNetworkSetsRn_Type())
cucsExtvmmVMNetworkSetsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkSetsRn.setStatus(_A)
_CucsExtvmmVMNetworkSetsFltAggr_Type=Unsigned64
_CucsExtvmmVMNetworkSetsFltAggr_Object=MibTableColumn
cucsExtvmmVMNetworkSetsFltAggr=_CucsExtvmmVMNetworkSetsFltAggr_Object((1,3,6,1,4,1,9,9,719,1,18,35,1,4),_CucsExtvmmVMNetworkSetsFltAggr_Type())
cucsExtvmmVMNetworkSetsFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkSetsFltAggr.setStatus(_A)
_CucsExtvmmVMNetworkSetsGenNum_Type=Gauge32
_CucsExtvmmVMNetworkSetsGenNum_Object=MibTableColumn
cucsExtvmmVMNetworkSetsGenNum=_CucsExtvmmVMNetworkSetsGenNum_Object((1,3,6,1,4,1,9,9,719,1,18,35,1,5),_CucsExtvmmVMNetworkSetsGenNum_Type())
cucsExtvmmVMNetworkSetsGenNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtvmmVMNetworkSetsGenNum.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsExtvmmObjects':cucsExtvmmObjects,'cucsExtvmmEpTable':cucsExtvmmEpTable,'cucsExtvmmEpEntry':cucsExtvmmEpEntry,_E:cucsExtvmmEpInstanceId,'cucsExtvmmEpDn':cucsExtvmmEpDn,'cucsExtvmmEpRn':cucsExtvmmEpRn,'cucsExtvmmEpFsmDescr':cucsExtvmmEpFsmDescr,'cucsExtvmmEpFsmPrev':cucsExtvmmEpFsmPrev,'cucsExtvmmEpFsmProgr':cucsExtvmmEpFsmProgr,'cucsExtvmmEpFsmRmtInvErrCode':cucsExtvmmEpFsmRmtInvErrCode,'cucsExtvmmEpFsmRmtInvErrDescr':cucsExtvmmEpFsmRmtInvErrDescr,'cucsExtvmmEpFsmRmtInvRslt':cucsExtvmmEpFsmRmtInvRslt,'cucsExtvmmEpFsmStageDescr':cucsExtvmmEpFsmStageDescr,'cucsExtvmmEpFsmStamp':cucsExtvmmEpFsmStamp,'cucsExtvmmEpFsmStatus':cucsExtvmmEpFsmStatus,'cucsExtvmmEpFsmTry':cucsExtvmmEpFsmTry,'cucsExtvmmEpGenNum':cucsExtvmmEpGenNum,'cucsExtvmmKeyInstTable':cucsExtvmmKeyInstTable,'cucsExtvmmKeyInstEntry':cucsExtvmmKeyInstEntry,_F:cucsExtvmmKeyInstInstanceId,'cucsExtvmmKeyInstDn':cucsExtvmmKeyInstDn,'cucsExtvmmKeyInstRn':cucsExtvmmKeyInstRn,'cucsExtvmmKeyInstInst':cucsExtvmmKeyInstInst,'cucsExtvmmKeyInstKey':cucsExtvmmKeyInstKey,'cucsExtvmmKeyRingTable':cucsExtvmmKeyRingTable,'cucsExtvmmKeyRingEntry':cucsExtvmmKeyRingEntry,_G:cucsExtvmmKeyRingInstanceId,'cucsExtvmmKeyRingDn':cucsExtvmmKeyRingDn,'cucsExtvmmKeyRingRn':cucsExtvmmKeyRingRn,'cucsExtvmmKeyRingCertFile':cucsExtvmmKeyRingCertFile,'cucsExtvmmKeyRingLocation':cucsExtvmmKeyRingLocation,'cucsExtvmmKeyRingName':cucsExtvmmKeyRingName,'cucsExtvmmKeyRingPath':cucsExtvmmKeyRingPath,'cucsExtvmmKeyStoreTable':cucsExtvmmKeyStoreTable,'cucsExtvmmKeyStoreEntry':cucsExtvmmKeyStoreEntry,_H:cucsExtvmmKeyStoreInstanceId,'cucsExtvmmKeyStoreDn':cucsExtvmmKeyStoreDn,'cucsExtvmmKeyStoreRn':cucsExtvmmKeyStoreRn,'cucsExtvmmKeyStoreFsmDescr':cucsExtvmmKeyStoreFsmDescr,'cucsExtvmmKeyStoreFsmPrev':cucsExtvmmKeyStoreFsmPrev,'cucsExtvmmKeyStoreFsmProgr':cucsExtvmmKeyStoreFsmProgr,'cucsExtvmmKeyStoreFsmRmtInvErrCode':cucsExtvmmKeyStoreFsmRmtInvErrCode,'cucsExtvmmKeyStoreFsmRmtInvErrDescr':cucsExtvmmKeyStoreFsmRmtInvErrDescr,'cucsExtvmmKeyStoreFsmRmtInvRslt':cucsExtvmmKeyStoreFsmRmtInvRslt,'cucsExtvmmKeyStoreFsmStageDescr':cucsExtvmmKeyStoreFsmStageDescr,'cucsExtvmmKeyStoreFsmStamp':cucsExtvmmKeyStoreFsmStamp,'cucsExtvmmKeyStoreFsmStatus':cucsExtvmmKeyStoreFsmStatus,'cucsExtvmmKeyStoreFsmTry':cucsExtvmmKeyStoreFsmTry,'cucsExtvmmKeyStoreFsmTaskTable':cucsExtvmmKeyStoreFsmTaskTable,'cucsExtvmmKeyStoreFsmTaskEntry':cucsExtvmmKeyStoreFsmTaskEntry,_I:cucsExtvmmKeyStoreFsmTaskInstanceId,'cucsExtvmmKeyStoreFsmTaskDn':cucsExtvmmKeyStoreFsmTaskDn,'cucsExtvmmKeyStoreFsmTaskRn':cucsExtvmmKeyStoreFsmTaskRn,'cucsExtvmmKeyStoreFsmTaskCompletion':cucsExtvmmKeyStoreFsmTaskCompletion,'cucsExtvmmKeyStoreFsmTaskFlags':cucsExtvmmKeyStoreFsmTaskFlags,'cucsExtvmmKeyStoreFsmTaskItem':cucsExtvmmKeyStoreFsmTaskItem,'cucsExtvmmKeyStoreFsmTaskSeqId':cucsExtvmmKeyStoreFsmTaskSeqId,'cucsExtvmmMasterExtKeyTable':cucsExtvmmMasterExtKeyTable,'cucsExtvmmMasterExtKeyEntry':cucsExtvmmMasterExtKeyEntry,_J:cucsExtvmmMasterExtKeyInstanceId,'cucsExtvmmMasterExtKeyDn':cucsExtvmmMasterExtKeyDn,'cucsExtvmmMasterExtKeyRn':cucsExtvmmMasterExtKeyRn,'cucsExtvmmMasterExtKeyFsmDescr':cucsExtvmmMasterExtKeyFsmDescr,'cucsExtvmmMasterExtKeyFsmPrev':cucsExtvmmMasterExtKeyFsmPrev,'cucsExtvmmMasterExtKeyFsmProgr':cucsExtvmmMasterExtKeyFsmProgr,'cucsExtvmmMasterExtKeyFsmRmtInvErrCode':cucsExtvmmMasterExtKeyFsmRmtInvErrCode,'cucsExtvmmMasterExtKeyFsmRmtInvErrDescr':cucsExtvmmMasterExtKeyFsmRmtInvErrDescr,'cucsExtvmmMasterExtKeyFsmRmtInvRslt':cucsExtvmmMasterExtKeyFsmRmtInvRslt,'cucsExtvmmMasterExtKeyFsmStageDescr':cucsExtvmmMasterExtKeyFsmStageDescr,'cucsExtvmmMasterExtKeyFsmStamp':cucsExtvmmMasterExtKeyFsmStamp,'cucsExtvmmMasterExtKeyFsmStatus':cucsExtvmmMasterExtKeyFsmStatus,'cucsExtvmmMasterExtKeyFsmTry':cucsExtvmmMasterExtKeyFsmTry,'cucsExtvmmMasterExtKeyKey':cucsExtvmmMasterExtKeyKey,'cucsExtvmmMasterExtKeyFsmTaskTable':cucsExtvmmMasterExtKeyFsmTaskTable,'cucsExtvmmMasterExtKeyFsmTaskEntry':cucsExtvmmMasterExtKeyFsmTaskEntry,_K:cucsExtvmmMasterExtKeyFsmTaskInstanceId,'cucsExtvmmMasterExtKeyFsmTaskDn':cucsExtvmmMasterExtKeyFsmTaskDn,'cucsExtvmmMasterExtKeyFsmTaskRn':cucsExtvmmMasterExtKeyFsmTaskRn,'cucsExtvmmMasterExtKeyFsmTaskCompletion':cucsExtvmmMasterExtKeyFsmTaskCompletion,'cucsExtvmmMasterExtKeyFsmTaskFlags':cucsExtvmmMasterExtKeyFsmTaskFlags,'cucsExtvmmMasterExtKeyFsmTaskItem':cucsExtvmmMasterExtKeyFsmTaskItem,'cucsExtvmmMasterExtKeyFsmTaskSeqId':cucsExtvmmMasterExtKeyFsmTaskSeqId,'cucsExtvmmProviderTable':cucsExtvmmProviderTable,'cucsExtvmmProviderEntry':cucsExtvmmProviderEntry,_L:cucsExtvmmProviderInstanceId,'cucsExtvmmProviderDn':cucsExtvmmProviderDn,'cucsExtvmmProviderRn':cucsExtvmmProviderRn,'cucsExtvmmProviderCert':cucsExtvmmProviderCert,'cucsExtvmmProviderDescr':cucsExtvmmProviderDescr,'cucsExtvmmProviderFsmDescr':cucsExtvmmProviderFsmDescr,'cucsExtvmmProviderFsmPrev':cucsExtvmmProviderFsmPrev,'cucsExtvmmProviderFsmProgr':cucsExtvmmProviderFsmProgr,'cucsExtvmmProviderFsmRmtInvErrCode':cucsExtvmmProviderFsmRmtInvErrCode,'cucsExtvmmProviderFsmRmtInvErrDescr':cucsExtvmmProviderFsmRmtInvErrDescr,'cucsExtvmmProviderFsmRmtInvRslt':cucsExtvmmProviderFsmRmtInvRslt,'cucsExtvmmProviderFsmStageDescr':cucsExtvmmProviderFsmStageDescr,'cucsExtvmmProviderFsmStamp':cucsExtvmmProviderFsmStamp,'cucsExtvmmProviderFsmStatus':cucsExtvmmProviderFsmStatus,'cucsExtvmmProviderFsmTry':cucsExtvmmProviderFsmTry,'cucsExtvmmProviderHost':cucsExtvmmProviderHost,'cucsExtvmmProviderIntId':cucsExtvmmProviderIntId,'cucsExtvmmProviderKey':cucsExtvmmProviderKey,'cucsExtvmmProviderName':cucsExtvmmProviderName,'cucsExtvmmProviderUuid':cucsExtvmmProviderUuid,'cucsExtvmmProviderVer':cucsExtvmmProviderVer,'cucsExtvmmProviderVerRaw':cucsExtvmmProviderVerRaw,'cucsExtvmmProviderPolicyLevel':cucsExtvmmProviderPolicyLevel,'cucsExtvmmProviderPolicyOwner':cucsExtvmmProviderPolicyOwner,'cucsExtvmmProviderPortValue':cucsExtvmmProviderPortValue,'cucsExtvmmProviderVendorType':cucsExtvmmProviderVendorType,'cucsExtvmmProviderFsmTaskTable':cucsExtvmmProviderFsmTaskTable,'cucsExtvmmProviderFsmTaskEntry':cucsExtvmmProviderFsmTaskEntry,_M:cucsExtvmmProviderFsmTaskInstanceId,'cucsExtvmmProviderFsmTaskDn':cucsExtvmmProviderFsmTaskDn,'cucsExtvmmProviderFsmTaskRn':cucsExtvmmProviderFsmTaskRn,'cucsExtvmmProviderFsmTaskCompletion':cucsExtvmmProviderFsmTaskCompletion,'cucsExtvmmProviderFsmTaskFlags':cucsExtvmmProviderFsmTaskFlags,'cucsExtvmmProviderFsmTaskItem':cucsExtvmmProviderFsmTaskItem,'cucsExtvmmProviderFsmTaskSeqId':cucsExtvmmProviderFsmTaskSeqId,'cucsExtvmmSwitchDelTaskTable':cucsExtvmmSwitchDelTaskTable,'cucsExtvmmSwitchDelTaskEntry':cucsExtvmmSwitchDelTaskEntry,_N:cucsExtvmmSwitchDelTaskInstanceId,'cucsExtvmmSwitchDelTaskDn':cucsExtvmmSwitchDelTaskDn,'cucsExtvmmSwitchDelTaskRn':cucsExtvmmSwitchDelTaskRn,'cucsExtvmmSwitchDelTaskCertFile':cucsExtvmmSwitchDelTaskCertFile,'cucsExtvmmSwitchDelTaskDcName':cucsExtvmmSwitchDelTaskDcName,'cucsExtvmmSwitchDelTaskDcOrg':cucsExtvmmSwitchDelTaskDcOrg,'cucsExtvmmSwitchDelTaskDescr':cucsExtvmmSwitchDelTaskDescr,'cucsExtvmmSwitchDelTaskExtKey':cucsExtvmmSwitchDelTaskExtKey,'cucsExtvmmSwitchDelTaskFsmDescr':cucsExtvmmSwitchDelTaskFsmDescr,'cucsExtvmmSwitchDelTaskFsmPrev':cucsExtvmmSwitchDelTaskFsmPrev,'cucsExtvmmSwitchDelTaskFsmProgr':cucsExtvmmSwitchDelTaskFsmProgr,'cucsExtvmmSwitchDelTaskFsmRmtInvErrCode':cucsExtvmmSwitchDelTaskFsmRmtInvErrCode,'cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr':cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr,'cucsExtvmmSwitchDelTaskFsmRmtInvRslt':cucsExtvmmSwitchDelTaskFsmRmtInvRslt,'cucsExtvmmSwitchDelTaskFsmStageDescr':cucsExtvmmSwitchDelTaskFsmStageDescr,'cucsExtvmmSwitchDelTaskFsmStamp':cucsExtvmmSwitchDelTaskFsmStamp,'cucsExtvmmSwitchDelTaskFsmStatus':cucsExtvmmSwitchDelTaskFsmStatus,'cucsExtvmmSwitchDelTaskFsmTry':cucsExtvmmSwitchDelTaskFsmTry,'cucsExtvmmSwitchDelTaskHost':cucsExtvmmSwitchDelTaskHost,'cucsExtvmmSwitchDelTaskIntId':cucsExtvmmSwitchDelTaskIntId,'cucsExtvmmSwitchDelTaskKeyInst':cucsExtvmmSwitchDelTaskKeyInst,'cucsExtvmmSwitchDelTaskName':cucsExtvmmSwitchDelTaskName,'cucsExtvmmSwitchDelTaskOrgPath':cucsExtvmmSwitchDelTaskOrgPath,'cucsExtvmmSwitchDelTaskProvIntId':cucsExtvmmSwitchDelTaskProvIntId,'cucsExtvmmSwitchDelTaskProvider':cucsExtvmmSwitchDelTaskProvider,'cucsExtvmmSwitchDelTaskSwIntId':cucsExtvmmSwitchDelTaskSwIntId,'cucsExtvmmSwitchDelTaskSwName':cucsExtvmmSwitchDelTaskSwName,'cucsExtvmmSwitchDelTaskPolicyLevel':cucsExtvmmSwitchDelTaskPolicyLevel,'cucsExtvmmSwitchDelTaskPolicyOwner':cucsExtvmmSwitchDelTaskPolicyOwner,'cucsExtvmmSwitchDelTaskPortValue':cucsExtvmmSwitchDelTaskPortValue,'cucsExtvmmSwitchDelTaskFsmTaskTable':cucsExtvmmSwitchDelTaskFsmTaskTable,'cucsExtvmmSwitchDelTaskFsmTaskEntry':cucsExtvmmSwitchDelTaskFsmTaskEntry,_O:cucsExtvmmSwitchDelTaskFsmTaskInstanceId,'cucsExtvmmSwitchDelTaskFsmTaskDn':cucsExtvmmSwitchDelTaskFsmTaskDn,'cucsExtvmmSwitchDelTaskFsmTaskRn':cucsExtvmmSwitchDelTaskFsmTaskRn,'cucsExtvmmSwitchDelTaskFsmTaskCompletion':cucsExtvmmSwitchDelTaskFsmTaskCompletion,'cucsExtvmmSwitchDelTaskFsmTaskFlags':cucsExtvmmSwitchDelTaskFsmTaskFlags,'cucsExtvmmSwitchDelTaskFsmTaskItem':cucsExtvmmSwitchDelTaskFsmTaskItem,'cucsExtvmmSwitchDelTaskFsmTaskSeqId':cucsExtvmmSwitchDelTaskFsmTaskSeqId,'cucsExtvmmEpFsmTaskTable':cucsExtvmmEpFsmTaskTable,'cucsExtvmmEpFsmTaskEntry':cucsExtvmmEpFsmTaskEntry,_P:cucsExtvmmEpFsmTaskInstanceId,'cucsExtvmmEpFsmTaskDn':cucsExtvmmEpFsmTaskDn,'cucsExtvmmEpFsmTaskRn':cucsExtvmmEpFsmTaskRn,'cucsExtvmmEpFsmTaskCompletion':cucsExtvmmEpFsmTaskCompletion,'cucsExtvmmEpFsmTaskFlags':cucsExtvmmEpFsmTaskFlags,'cucsExtvmmEpFsmTaskItem':cucsExtvmmEpFsmTaskItem,'cucsExtvmmEpFsmTaskSeqId':cucsExtvmmEpFsmTaskSeqId,'cucsExtvmmSwitchSetTable':cucsExtvmmSwitchSetTable,'cucsExtvmmSwitchSetEntry':cucsExtvmmSwitchSetEntry,_Q:cucsExtvmmSwitchSetInstanceId,'cucsExtvmmSwitchSetDn':cucsExtvmmSwitchSetDn,'cucsExtvmmSwitchSetRn':cucsExtvmmSwitchSetRn,'cucsExtvmmEpFsmTable':cucsExtvmmEpFsmTable,'cucsExtvmmEpFsmEntry':cucsExtvmmEpFsmEntry,_R:cucsExtvmmEpFsmInstanceId,'cucsExtvmmEpFsmDn':cucsExtvmmEpFsmDn,'cucsExtvmmEpFsmRn':cucsExtvmmEpFsmRn,'cucsExtvmmEpFsmCompletionTime':cucsExtvmmEpFsmCompletionTime,'cucsExtvmmEpFsmCurrentFsm':cucsExtvmmEpFsmCurrentFsm,'cucsExtvmmEpFsmDescrData':cucsExtvmmEpFsmDescrData,'cucsExtvmmEpFsmFsmStatus':cucsExtvmmEpFsmFsmStatus,'cucsExtvmmEpFsmProgress':cucsExtvmmEpFsmProgress,'cucsExtvmmEpFsmRmtErrCode':cucsExtvmmEpFsmRmtErrCode,'cucsExtvmmEpFsmRmtErrDescr':cucsExtvmmEpFsmRmtErrDescr,'cucsExtvmmEpFsmRmtRslt':cucsExtvmmEpFsmRmtRslt,'cucsExtvmmEpFsmStageTable':cucsExtvmmEpFsmStageTable,'cucsExtvmmEpFsmStageEntry':cucsExtvmmEpFsmStageEntry,_S:cucsExtvmmEpFsmStageInstanceId,'cucsExtvmmEpFsmStageDn':cucsExtvmmEpFsmStageDn,'cucsExtvmmEpFsmStageRn':cucsExtvmmEpFsmStageRn,'cucsExtvmmEpFsmStageDescrData':cucsExtvmmEpFsmStageDescrData,'cucsExtvmmEpFsmStageLastUpdateTime':cucsExtvmmEpFsmStageLastUpdateTime,'cucsExtvmmEpFsmStageName':cucsExtvmmEpFsmStageName,'cucsExtvmmEpFsmStageOrder':cucsExtvmmEpFsmStageOrder,'cucsExtvmmEpFsmStageRetry':cucsExtvmmEpFsmStageRetry,'cucsExtvmmEpFsmStageStageStatus':cucsExtvmmEpFsmStageStageStatus,'cucsExtvmmKeyStoreFsmTable':cucsExtvmmKeyStoreFsmTable,'cucsExtvmmKeyStoreFsmEntry':cucsExtvmmKeyStoreFsmEntry,_T:cucsExtvmmKeyStoreFsmInstanceId,'cucsExtvmmKeyStoreFsmDn':cucsExtvmmKeyStoreFsmDn,'cucsExtvmmKeyStoreFsmRn':cucsExtvmmKeyStoreFsmRn,'cucsExtvmmKeyStoreFsmCompletionTime':cucsExtvmmKeyStoreFsmCompletionTime,'cucsExtvmmKeyStoreFsmCurrentFsm':cucsExtvmmKeyStoreFsmCurrentFsm,'cucsExtvmmKeyStoreFsmDescrData':cucsExtvmmKeyStoreFsmDescrData,'cucsExtvmmKeyStoreFsmFsmStatus':cucsExtvmmKeyStoreFsmFsmStatus,'cucsExtvmmKeyStoreFsmProgress':cucsExtvmmKeyStoreFsmProgress,'cucsExtvmmKeyStoreFsmRmtErrCode':cucsExtvmmKeyStoreFsmRmtErrCode,'cucsExtvmmKeyStoreFsmRmtErrDescr':cucsExtvmmKeyStoreFsmRmtErrDescr,'cucsExtvmmKeyStoreFsmRmtRslt':cucsExtvmmKeyStoreFsmRmtRslt,'cucsExtvmmKeyStoreFsmStageTable':cucsExtvmmKeyStoreFsmStageTable,'cucsExtvmmKeyStoreFsmStageEntry':cucsExtvmmKeyStoreFsmStageEntry,_U:cucsExtvmmKeyStoreFsmStageInstanceId,'cucsExtvmmKeyStoreFsmStageDn':cucsExtvmmKeyStoreFsmStageDn,'cucsExtvmmKeyStoreFsmStageRn':cucsExtvmmKeyStoreFsmStageRn,'cucsExtvmmKeyStoreFsmStageDescrData':cucsExtvmmKeyStoreFsmStageDescrData,'cucsExtvmmKeyStoreFsmStageLastUpdateTime':cucsExtvmmKeyStoreFsmStageLastUpdateTime,'cucsExtvmmKeyStoreFsmStageName':cucsExtvmmKeyStoreFsmStageName,'cucsExtvmmKeyStoreFsmStageOrder':cucsExtvmmKeyStoreFsmStageOrder,'cucsExtvmmKeyStoreFsmStageRetry':cucsExtvmmKeyStoreFsmStageRetry,'cucsExtvmmKeyStoreFsmStageStageStatus':cucsExtvmmKeyStoreFsmStageStageStatus,'cucsExtvmmMasterExtKeyFsmTable':cucsExtvmmMasterExtKeyFsmTable,'cucsExtvmmMasterExtKeyFsmEntry':cucsExtvmmMasterExtKeyFsmEntry,_V:cucsExtvmmMasterExtKeyFsmInstanceId,'cucsExtvmmMasterExtKeyFsmDn':cucsExtvmmMasterExtKeyFsmDn,'cucsExtvmmMasterExtKeyFsmRn':cucsExtvmmMasterExtKeyFsmRn,'cucsExtvmmMasterExtKeyFsmCompletionTime':cucsExtvmmMasterExtKeyFsmCompletionTime,'cucsExtvmmMasterExtKeyFsmCurrentFsm':cucsExtvmmMasterExtKeyFsmCurrentFsm,'cucsExtvmmMasterExtKeyFsmDescrData':cucsExtvmmMasterExtKeyFsmDescrData,'cucsExtvmmMasterExtKeyFsmFsmStatus':cucsExtvmmMasterExtKeyFsmFsmStatus,'cucsExtvmmMasterExtKeyFsmProgress':cucsExtvmmMasterExtKeyFsmProgress,'cucsExtvmmMasterExtKeyFsmRmtErrCode':cucsExtvmmMasterExtKeyFsmRmtErrCode,'cucsExtvmmMasterExtKeyFsmRmtErrDescr':cucsExtvmmMasterExtKeyFsmRmtErrDescr,'cucsExtvmmMasterExtKeyFsmRmtRslt':cucsExtvmmMasterExtKeyFsmRmtRslt,'cucsExtvmmMasterExtKeyFsmStageTable':cucsExtvmmMasterExtKeyFsmStageTable,'cucsExtvmmMasterExtKeyFsmStageEntry':cucsExtvmmMasterExtKeyFsmStageEntry,_W:cucsExtvmmMasterExtKeyFsmStageInstanceId,'cucsExtvmmMasterExtKeyFsmStageDn':cucsExtvmmMasterExtKeyFsmStageDn,'cucsExtvmmMasterExtKeyFsmStageRn':cucsExtvmmMasterExtKeyFsmStageRn,'cucsExtvmmMasterExtKeyFsmStageDescrData':cucsExtvmmMasterExtKeyFsmStageDescrData,'cucsExtvmmMasterExtKeyFsmStageLastUpdateTime':cucsExtvmmMasterExtKeyFsmStageLastUpdateTime,'cucsExtvmmMasterExtKeyFsmStageName':cucsExtvmmMasterExtKeyFsmStageName,'cucsExtvmmMasterExtKeyFsmStageOrder':cucsExtvmmMasterExtKeyFsmStageOrder,'cucsExtvmmMasterExtKeyFsmStageRetry':cucsExtvmmMasterExtKeyFsmStageRetry,'cucsExtvmmMasterExtKeyFsmStageStageStatus':cucsExtvmmMasterExtKeyFsmStageStageStatus,'cucsExtvmmProviderFsmTable':cucsExtvmmProviderFsmTable,'cucsExtvmmProviderFsmEntry':cucsExtvmmProviderFsmEntry,_X:cucsExtvmmProviderFsmInstanceId,'cucsExtvmmProviderFsmDn':cucsExtvmmProviderFsmDn,'cucsExtvmmProviderFsmRn':cucsExtvmmProviderFsmRn,'cucsExtvmmProviderFsmCompletionTime':cucsExtvmmProviderFsmCompletionTime,'cucsExtvmmProviderFsmCurrentFsm':cucsExtvmmProviderFsmCurrentFsm,'cucsExtvmmProviderFsmDescrData':cucsExtvmmProviderFsmDescrData,'cucsExtvmmProviderFsmFsmStatus':cucsExtvmmProviderFsmFsmStatus,'cucsExtvmmProviderFsmProgress':cucsExtvmmProviderFsmProgress,'cucsExtvmmProviderFsmRmtErrCode':cucsExtvmmProviderFsmRmtErrCode,'cucsExtvmmProviderFsmRmtErrDescr':cucsExtvmmProviderFsmRmtErrDescr,'cucsExtvmmProviderFsmRmtRslt':cucsExtvmmProviderFsmRmtRslt,'cucsExtvmmProviderFsmStageTable':cucsExtvmmProviderFsmStageTable,'cucsExtvmmProviderFsmStageEntry':cucsExtvmmProviderFsmStageEntry,_Y:cucsExtvmmProviderFsmStageInstanceId,'cucsExtvmmProviderFsmStageDn':cucsExtvmmProviderFsmStageDn,'cucsExtvmmProviderFsmStageRn':cucsExtvmmProviderFsmStageRn,'cucsExtvmmProviderFsmStageDescrData':cucsExtvmmProviderFsmStageDescrData,'cucsExtvmmProviderFsmStageLastUpdateTime':cucsExtvmmProviderFsmStageLastUpdateTime,'cucsExtvmmProviderFsmStageName':cucsExtvmmProviderFsmStageName,'cucsExtvmmProviderFsmStageOrder':cucsExtvmmProviderFsmStageOrder,'cucsExtvmmProviderFsmStageRetry':cucsExtvmmProviderFsmStageRetry,'cucsExtvmmProviderFsmStageStageStatus':cucsExtvmmProviderFsmStageStageStatus,'cucsExtvmmSwitchDelTaskFsmTable':cucsExtvmmSwitchDelTaskFsmTable,'cucsExtvmmSwitchDelTaskFsmEntry':cucsExtvmmSwitchDelTaskFsmEntry,_Z:cucsExtvmmSwitchDelTaskFsmInstanceId,'cucsExtvmmSwitchDelTaskFsmDn':cucsExtvmmSwitchDelTaskFsmDn,'cucsExtvmmSwitchDelTaskFsmRn':cucsExtvmmSwitchDelTaskFsmRn,'cucsExtvmmSwitchDelTaskFsmCompletionTime':cucsExtvmmSwitchDelTaskFsmCompletionTime,'cucsExtvmmSwitchDelTaskFsmCurrentFsm':cucsExtvmmSwitchDelTaskFsmCurrentFsm,'cucsExtvmmSwitchDelTaskFsmDescrData':cucsExtvmmSwitchDelTaskFsmDescrData,'cucsExtvmmSwitchDelTaskFsmFsmStatus':cucsExtvmmSwitchDelTaskFsmFsmStatus,'cucsExtvmmSwitchDelTaskFsmProgress':cucsExtvmmSwitchDelTaskFsmProgress,'cucsExtvmmSwitchDelTaskFsmRmtErrCode':cucsExtvmmSwitchDelTaskFsmRmtErrCode,'cucsExtvmmSwitchDelTaskFsmRmtErrDescr':cucsExtvmmSwitchDelTaskFsmRmtErrDescr,'cucsExtvmmSwitchDelTaskFsmRmtRslt':cucsExtvmmSwitchDelTaskFsmRmtRslt,'cucsExtvmmSwitchDelTaskFsmStageTable':cucsExtvmmSwitchDelTaskFsmStageTable,'cucsExtvmmSwitchDelTaskFsmStageEntry':cucsExtvmmSwitchDelTaskFsmStageEntry,_a:cucsExtvmmSwitchDelTaskFsmStageInstanceId,'cucsExtvmmSwitchDelTaskFsmStageDn':cucsExtvmmSwitchDelTaskFsmStageDn,'cucsExtvmmSwitchDelTaskFsmStageRn':cucsExtvmmSwitchDelTaskFsmStageRn,'cucsExtvmmSwitchDelTaskFsmStageDescrData':cucsExtvmmSwitchDelTaskFsmStageDescrData,'cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime':cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime,'cucsExtvmmSwitchDelTaskFsmStageName':cucsExtvmmSwitchDelTaskFsmStageName,'cucsExtvmmSwitchDelTaskFsmStageOrder':cucsExtvmmSwitchDelTaskFsmStageOrder,'cucsExtvmmSwitchDelTaskFsmStageRetry':cucsExtvmmSwitchDelTaskFsmStageRetry,'cucsExtvmmSwitchDelTaskFsmStageStageStatus':cucsExtvmmSwitchDelTaskFsmStageStageStatus,'cucsExtvmmFNDReferenceTable':cucsExtvmmFNDReferenceTable,'cucsExtvmmFNDReferenceEntry':cucsExtvmmFNDReferenceEntry,_b:cucsExtvmmFNDReferenceInstanceId,'cucsExtvmmFNDReferenceDn':cucsExtvmmFNDReferenceDn,'cucsExtvmmFNDReferenceRn':cucsExtvmmFNDReferenceRn,'cucsExtvmmFNDReferenceDescr':cucsExtvmmFNDReferenceDescr,'cucsExtvmmFNDReferenceFnDefName':cucsExtvmmFNDReferenceFnDefName,'cucsExtvmmFNDReferenceIntId':cucsExtvmmFNDReferenceIntId,'cucsExtvmmFNDReferenceName':cucsExtvmmFNDReferenceName,'cucsExtvmmFNDReferenceOperFnDefName':cucsExtvmmFNDReferenceOperFnDefName,'cucsExtvmmFNDReferencePolicyLevel':cucsExtvmmFNDReferencePolicyLevel,'cucsExtvmmFNDReferencePolicyOwner':cucsExtvmmFNDReferencePolicyOwner,'cucsExtvmmFabricNetworkTable':cucsExtvmmFabricNetworkTable,'cucsExtvmmFabricNetworkEntry':cucsExtvmmFabricNetworkEntry,_c:cucsExtvmmFabricNetworkInstanceId,'cucsExtvmmFabricNetworkDn':cucsExtvmmFabricNetworkDn,'cucsExtvmmFabricNetworkRn':cucsExtvmmFabricNetworkRn,'cucsExtvmmFabricNetworkDescr':cucsExtvmmFabricNetworkDescr,'cucsExtvmmFabricNetworkGuid':cucsExtvmmFabricNetworkGuid,'cucsExtvmmFabricNetworkIntId':cucsExtvmmFabricNetworkIntId,'cucsExtvmmFabricNetworkName':cucsExtvmmFabricNetworkName,'cucsExtvmmFabricNetworkNetworkType':cucsExtvmmFabricNetworkNetworkType,'cucsExtvmmFabricNetworkPolicyLevel':cucsExtvmmFabricNetworkPolicyLevel,'cucsExtvmmFabricNetworkPolicyOwner':cucsExtvmmFabricNetworkPolicyOwner,'cucsExtvmmFabricNetworkRefOperState':cucsExtvmmFabricNetworkRefOperState,'cucsExtvmmFabricNetworkDefinitionTable':cucsExtvmmFabricNetworkDefinitionTable,'cucsExtvmmFabricNetworkDefinitionEntry':cucsExtvmmFabricNetworkDefinitionEntry,_d:cucsExtvmmFabricNetworkDefinitionInstanceId,'cucsExtvmmFabricNetworkDefinitionDn':cucsExtvmmFabricNetworkDefinitionDn,'cucsExtvmmFabricNetworkDefinitionRn':cucsExtvmmFabricNetworkDefinitionRn,'cucsExtvmmFabricNetworkDefinitionAllowedVnicType':cucsExtvmmFabricNetworkDefinitionAllowedVnicType,'cucsExtvmmFabricNetworkDefinitionDescr':cucsExtvmmFabricNetworkDefinitionDescr,'cucsExtvmmFabricNetworkDefinitionGuid':cucsExtvmmFabricNetworkDefinitionGuid,'cucsExtvmmFabricNetworkDefinitionIntId':cucsExtvmmFabricNetworkDefinitionIntId,'cucsExtvmmFabricNetworkDefinitionName':cucsExtvmmFabricNetworkDefinitionName,'cucsExtvmmFabricNetworkDefinitionPolicyLevel':cucsExtvmmFabricNetworkDefinitionPolicyLevel,'cucsExtvmmFabricNetworkDefinitionPolicyOwner':cucsExtvmmFabricNetworkDefinitionPolicyOwner,'cucsExtvmmFabricNetworkDefinitionPrimaryVlanId':cucsExtvmmFabricNetworkDefinitionPrimaryVlanId,'cucsExtvmmFabricNetworkDefinitionRefOperState':cucsExtvmmFabricNetworkDefinitionRefOperState,'cucsExtvmmNetworkSetsTable':cucsExtvmmNetworkSetsTable,'cucsExtvmmNetworkSetsEntry':cucsExtvmmNetworkSetsEntry,_e:cucsExtvmmNetworkSetsInstanceId,'cucsExtvmmNetworkSetsDn':cucsExtvmmNetworkSetsDn,'cucsExtvmmNetworkSetsRn':cucsExtvmmNetworkSetsRn,'cucsExtvmmNetworkSetsFltAggr':cucsExtvmmNetworkSetsFltAggr,'cucsExtvmmNetworkSetsFsmDescr':cucsExtvmmNetworkSetsFsmDescr,'cucsExtvmmNetworkSetsFsmPrev':cucsExtvmmNetworkSetsFsmPrev,'cucsExtvmmNetworkSetsFsmProgr':cucsExtvmmNetworkSetsFsmProgr,'cucsExtvmmNetworkSetsFsmRmtInvErrCode':cucsExtvmmNetworkSetsFsmRmtInvErrCode,'cucsExtvmmNetworkSetsFsmRmtInvErrDescr':cucsExtvmmNetworkSetsFsmRmtInvErrDescr,'cucsExtvmmNetworkSetsFsmRmtInvRslt':cucsExtvmmNetworkSetsFsmRmtInvRslt,'cucsExtvmmNetworkSetsFsmStageDescr':cucsExtvmmNetworkSetsFsmStageDescr,'cucsExtvmmNetworkSetsFsmStamp':cucsExtvmmNetworkSetsFsmStamp,'cucsExtvmmNetworkSetsFsmStatus':cucsExtvmmNetworkSetsFsmStatus,'cucsExtvmmNetworkSetsFsmTry':cucsExtvmmNetworkSetsFsmTry,'cucsExtvmmNetworkSetsGenNum':cucsExtvmmNetworkSetsGenNum,'cucsExtvmmNetworkSetsFsmTable':cucsExtvmmNetworkSetsFsmTable,'cucsExtvmmNetworkSetsFsmEntry':cucsExtvmmNetworkSetsFsmEntry,_f:cucsExtvmmNetworkSetsFsmInstanceId,'cucsExtvmmNetworkSetsFsmDn':cucsExtvmmNetworkSetsFsmDn,'cucsExtvmmNetworkSetsFsmRn':cucsExtvmmNetworkSetsFsmRn,'cucsExtvmmNetworkSetsFsmCompletionTime':cucsExtvmmNetworkSetsFsmCompletionTime,'cucsExtvmmNetworkSetsFsmCurrentFsm':cucsExtvmmNetworkSetsFsmCurrentFsm,'cucsExtvmmNetworkSetsFsmDescrData':cucsExtvmmNetworkSetsFsmDescrData,'cucsExtvmmNetworkSetsFsmFsmStatus':cucsExtvmmNetworkSetsFsmFsmStatus,'cucsExtvmmNetworkSetsFsmProgress':cucsExtvmmNetworkSetsFsmProgress,'cucsExtvmmNetworkSetsFsmRmtErrCode':cucsExtvmmNetworkSetsFsmRmtErrCode,'cucsExtvmmNetworkSetsFsmRmtErrDescr':cucsExtvmmNetworkSetsFsmRmtErrDescr,'cucsExtvmmNetworkSetsFsmRmtRslt':cucsExtvmmNetworkSetsFsmRmtRslt,'cucsExtvmmNetworkSetsFsmStageTable':cucsExtvmmNetworkSetsFsmStageTable,'cucsExtvmmNetworkSetsFsmStageEntry':cucsExtvmmNetworkSetsFsmStageEntry,_g:cucsExtvmmNetworkSetsFsmStageInstanceId,'cucsExtvmmNetworkSetsFsmStageDn':cucsExtvmmNetworkSetsFsmStageDn,'cucsExtvmmNetworkSetsFsmStageRn':cucsExtvmmNetworkSetsFsmStageRn,'cucsExtvmmNetworkSetsFsmStageDescrData':cucsExtvmmNetworkSetsFsmStageDescrData,'cucsExtvmmNetworkSetsFsmStageLastUpdateTime':cucsExtvmmNetworkSetsFsmStageLastUpdateTime,'cucsExtvmmNetworkSetsFsmStageName':cucsExtvmmNetworkSetsFsmStageName,'cucsExtvmmNetworkSetsFsmStageOrder':cucsExtvmmNetworkSetsFsmStageOrder,'cucsExtvmmNetworkSetsFsmStageRetry':cucsExtvmmNetworkSetsFsmStageRetry,'cucsExtvmmNetworkSetsFsmStageStageStatus':cucsExtvmmNetworkSetsFsmStageStageStatus,'cucsExtvmmNetworkSetsFsmTaskTable':cucsExtvmmNetworkSetsFsmTaskTable,'cucsExtvmmNetworkSetsFsmTaskEntry':cucsExtvmmNetworkSetsFsmTaskEntry,_h:cucsExtvmmNetworkSetsFsmTaskInstanceId,'cucsExtvmmNetworkSetsFsmTaskDn':cucsExtvmmNetworkSetsFsmTaskDn,'cucsExtvmmNetworkSetsFsmTaskRn':cucsExtvmmNetworkSetsFsmTaskRn,'cucsExtvmmNetworkSetsFsmTaskCompletion':cucsExtvmmNetworkSetsFsmTaskCompletion,'cucsExtvmmNetworkSetsFsmTaskFlags':cucsExtvmmNetworkSetsFsmTaskFlags,'cucsExtvmmNetworkSetsFsmTaskItem':cucsExtvmmNetworkSetsFsmTaskItem,'cucsExtvmmNetworkSetsFsmTaskSeqId':cucsExtvmmNetworkSetsFsmTaskSeqId,'cucsExtvmmUpLinkPPTable':cucsExtvmmUpLinkPPTable,'cucsExtvmmUpLinkPPEntry':cucsExtvmmUpLinkPPEntry,_i:cucsExtvmmUpLinkPPInstanceId,'cucsExtvmmUpLinkPPDn':cucsExtvmmUpLinkPPDn,'cucsExtvmmUpLinkPPRn':cucsExtvmmUpLinkPPRn,'cucsExtvmmUpLinkPPDescr':cucsExtvmmUpLinkPPDescr,'cucsExtvmmUpLinkPPFltAggr':cucsExtvmmUpLinkPPFltAggr,'cucsExtvmmUpLinkPPGuid':cucsExtvmmUpLinkPPGuid,'cucsExtvmmUpLinkPPIntId':cucsExtvmmUpLinkPPIntId,'cucsExtvmmUpLinkPPName':cucsExtvmmUpLinkPPName,'cucsExtvmmUpLinkPPPolicyLevel':cucsExtvmmUpLinkPPPolicyLevel,'cucsExtvmmUpLinkPPPolicyOwner':cucsExtvmmUpLinkPPPolicyOwner,'cucsExtvmmUpLinkPPRefOperState':cucsExtvmmUpLinkPPRefOperState,'cucsExtvmmVMNDRefTable':cucsExtvmmVMNDRefTable,'cucsExtvmmVMNDRefEntry':cucsExtvmmVMNDRefEntry,_j:cucsExtvmmVMNDRefInstanceId,'cucsExtvmmVMNDRefDn':cucsExtvmmVMNDRefDn,'cucsExtvmmVMNDRefRn':cucsExtvmmVMNDRefRn,'cucsExtvmmVMNDRefConfigQualifier':cucsExtvmmVMNDRefConfigQualifier,'cucsExtvmmVMNDRefDescr':cucsExtvmmVMNDRefDescr,'cucsExtvmmVMNDRefFnDefName':cucsExtvmmVMNDRefFnDefName,'cucsExtvmmVMNDRefFnName':cucsExtvmmVMNDRefFnName,'cucsExtvmmVMNDRefIntId':cucsExtvmmVMNDRefIntId,'cucsExtvmmVMNDRefName':cucsExtvmmVMNDRefName,'cucsExtvmmVMNDRefOperVmNetworkDefName':cucsExtvmmVMNDRefOperVmNetworkDefName,'cucsExtvmmVMNDRefPolicyLevel':cucsExtvmmVMNDRefPolicyLevel,'cucsExtvmmVMNDRefPolicyOwner':cucsExtvmmVMNDRefPolicyOwner,'cucsExtvmmVMNDRefVmNetworkDefName':cucsExtvmmVMNDRefVmNetworkDefName,'cucsExtvmmVMNetworkTable':cucsExtvmmVMNetworkTable,'cucsExtvmmVMNetworkEntry':cucsExtvmmVMNetworkEntry,_k:cucsExtvmmVMNetworkInstanceId,'cucsExtvmmVMNetworkDn':cucsExtvmmVMNetworkDn,'cucsExtvmmVMNetworkRn':cucsExtvmmVMNetworkRn,'cucsExtvmmVMNetworkDescr':cucsExtvmmVMNetworkDescr,'cucsExtvmmVMNetworkFabricNetworkName':cucsExtvmmVMNetworkFabricNetworkName,'cucsExtvmmVMNetworkFltAggr':cucsExtvmmVMNetworkFltAggr,'cucsExtvmmVMNetworkGuid':cucsExtvmmVMNetworkGuid,'cucsExtvmmVMNetworkIntId':cucsExtvmmVMNetworkIntId,'cucsExtvmmVMNetworkName':cucsExtvmmVMNetworkName,'cucsExtvmmVMNetworkOperFabricNetworkName':cucsExtvmmVMNetworkOperFabricNetworkName,'cucsExtvmmVMNetworkPolicyLevel':cucsExtvmmVMNetworkPolicyLevel,'cucsExtvmmVMNetworkPolicyOwner':cucsExtvmmVMNetworkPolicyOwner,'cucsExtvmmVMNetworkDefinitionTable':cucsExtvmmVMNetworkDefinitionTable,'cucsExtvmmVMNetworkDefinitionEntry':cucsExtvmmVMNetworkDefinitionEntry,_l:cucsExtvmmVMNetworkDefinitionInstanceId,'cucsExtvmmVMNetworkDefinitionDn':cucsExtvmmVMNetworkDefinitionDn,'cucsExtvmmVMNetworkDefinitionRn':cucsExtvmmVMNetworkDefinitionRn,'cucsExtvmmVMNetworkDefinitionDescr':cucsExtvmmVMNetworkDefinitionDescr,'cucsExtvmmVMNetworkDefinitionExtIpPoolName':cucsExtvmmVMNetworkDefinitionExtIpPoolName,'cucsExtvmmVMNetworkDefinitionGuid':cucsExtvmmVMNetworkDefinitionGuid,'cucsExtvmmVMNetworkDefinitionIntId':cucsExtvmmVMNetworkDefinitionIntId,'cucsExtvmmVMNetworkDefinitionIpPoolGuid':cucsExtvmmVMNetworkDefinitionIpPoolGuid,'cucsExtvmmVMNetworkDefinitionMaxPorts':cucsExtvmmVMNetworkDefinitionMaxPorts,'cucsExtvmmVMNetworkDefinitionName':cucsExtvmmVMNetworkDefinitionName,'cucsExtvmmVMNetworkDefinitionOperExtIpPoolName':cucsExtvmmVMNetworkDefinitionOperExtIpPoolName,'cucsExtvmmVMNetworkDefinitionPolicyLevel':cucsExtvmmVMNetworkDefinitionPolicyLevel,'cucsExtvmmVMNetworkDefinitionPolicyOwner':cucsExtvmmVMNetworkDefinitionPolicyOwner,'cucsExtvmmVMNetworkDefinitionPrimaryVlanId':cucsExtvmmVMNetworkDefinitionPrimaryVlanId,'cucsExtvmmVMNetworkDefinitionRefOperState':cucsExtvmmVMNetworkDefinitionRefOperState,'cucsExtvmmVMNetworkDefinitionVlanName':cucsExtvmmVMNetworkDefinitionVlanName,'cucsExtvmmVMNetworkSetsTable':cucsExtvmmVMNetworkSetsTable,'cucsExtvmmVMNetworkSetsEntry':cucsExtvmmVMNetworkSetsEntry,_m:cucsExtvmmVMNetworkSetsInstanceId,'cucsExtvmmVMNetworkSetsDn':cucsExtvmmVMNetworkSetsDn,'cucsExtvmmVMNetworkSetsRn':cucsExtvmmVMNetworkSetsRn,'cucsExtvmmVMNetworkSetsFltAggr':cucsExtvmmVMNetworkSetsFltAggr,'cucsExtvmmVMNetworkSetsGenNum':cucsExtvmmVMNetworkSetsGenNum})