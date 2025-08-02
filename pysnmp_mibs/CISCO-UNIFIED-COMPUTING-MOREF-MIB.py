_K='cucsMorefRefInstanceId'
_J='cucsMorefPropInstanceId'
_I='cucsMorefImportRootFsmTaskInstanceId'
_H='cucsMorefImportRootFsmStageInstanceId'
_G='cucsMorefImportRootFsmInstanceId'
_F='cucsMorefImportRootInstanceId'
_E='cucsMorefFruRefInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-MOREF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsConditionRemoteInvRslt,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsMorefAdminState,CucsMorefImportRootFsmCurrentFsm,CucsMorefImportRootFsmStageName,CucsMorefImportRootFsmTaskItem=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsConditionRemoteInvRslt','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsMorefAdminState','CucsMorefImportRootFsmCurrentFsm','CucsMorefImportRootFsmStageName','CucsMorefImportRootFsmTaskItem')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsMorefObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,92))
_CucsMorefFruRefTable_Object=MibTable
cucsMorefFruRefTable=_CucsMorefFruRefTable_Object((1,3,6,1,4,1,9,9,719,1,92,1))
if mibBuilder.loadTexts:cucsMorefFruRefTable.setStatus(_A)
_CucsMorefFruRefEntry_Object=MibTableRow
cucsMorefFruRefEntry=_CucsMorefFruRefEntry_Object((1,3,6,1,4,1,9,9,719,1,92,1,1))
cucsMorefFruRefEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsMorefFruRefEntry.setStatus(_A)
_CucsMorefFruRefInstanceId_Type=CucsManagedObjectId
_CucsMorefFruRefInstanceId_Object=MibTableColumn
cucsMorefFruRefInstanceId=_CucsMorefFruRefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,92,1,1,1),_CucsMorefFruRefInstanceId_Type())
cucsMorefFruRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMorefFruRefInstanceId.setStatus(_A)
_CucsMorefFruRefDn_Type=CucsManagedObjectDn
_CucsMorefFruRefDn_Object=MibTableColumn
cucsMorefFruRefDn=_CucsMorefFruRefDn_Object((1,3,6,1,4,1,9,9,719,1,92,1,1,2),_CucsMorefFruRefDn_Type())
cucsMorefFruRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefFruRefDn.setStatus(_A)
_CucsMorefFruRefRn_Type=SnmpAdminString
_CucsMorefFruRefRn_Object=MibTableColumn
cucsMorefFruRefRn=_CucsMorefFruRefRn_Object((1,3,6,1,4,1,9,9,719,1,92,1,1,3),_CucsMorefFruRefRn_Type())
cucsMorefFruRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefFruRefRn.setStatus(_A)
_CucsMorefFruRefClassName_Type=SnmpAdminString
_CucsMorefFruRefClassName_Object=MibTableColumn
cucsMorefFruRefClassName=_CucsMorefFruRefClassName_Object((1,3,6,1,4,1,9,9,719,1,92,1,1,4),_CucsMorefFruRefClassName_Type())
cucsMorefFruRefClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefFruRefClassName.setStatus(_A)
_CucsMorefFruRefModel_Type=SnmpAdminString
_CucsMorefFruRefModel_Object=MibTableColumn
cucsMorefFruRefModel=_CucsMorefFruRefModel_Object((1,3,6,1,4,1,9,9,719,1,92,1,1,5),_CucsMorefFruRefModel_Type())
cucsMorefFruRefModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefFruRefModel.setStatus(_A)
_CucsMorefFruRefSerial_Type=SnmpAdminString
_CucsMorefFruRefSerial_Object=MibTableColumn
cucsMorefFruRefSerial=_CucsMorefFruRefSerial_Object((1,3,6,1,4,1,9,9,719,1,92,1,1,6),_CucsMorefFruRefSerial_Type())
cucsMorefFruRefSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefFruRefSerial.setStatus(_A)
_CucsMorefFruRefVendor_Type=SnmpAdminString
_CucsMorefFruRefVendor_Object=MibTableColumn
cucsMorefFruRefVendor=_CucsMorefFruRefVendor_Object((1,3,6,1,4,1,9,9,719,1,92,1,1,7),_CucsMorefFruRefVendor_Type())
cucsMorefFruRefVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefFruRefVendor.setStatus(_A)
_CucsMorefImportRootTable_Object=MibTable
cucsMorefImportRootTable=_CucsMorefImportRootTable_Object((1,3,6,1,4,1,9,9,719,1,92,2))
if mibBuilder.loadTexts:cucsMorefImportRootTable.setStatus(_A)
_CucsMorefImportRootEntry_Object=MibTableRow
cucsMorefImportRootEntry=_CucsMorefImportRootEntry_Object((1,3,6,1,4,1,9,9,719,1,92,2,1))
cucsMorefImportRootEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsMorefImportRootEntry.setStatus(_A)
_CucsMorefImportRootInstanceId_Type=CucsManagedObjectId
_CucsMorefImportRootInstanceId_Object=MibTableColumn
cucsMorefImportRootInstanceId=_CucsMorefImportRootInstanceId_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,1),_CucsMorefImportRootInstanceId_Type())
cucsMorefImportRootInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMorefImportRootInstanceId.setStatus(_A)
_CucsMorefImportRootDn_Type=CucsManagedObjectDn
_CucsMorefImportRootDn_Object=MibTableColumn
cucsMorefImportRootDn=_CucsMorefImportRootDn_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,2),_CucsMorefImportRootDn_Type())
cucsMorefImportRootDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootDn.setStatus(_A)
_CucsMorefImportRootRn_Type=SnmpAdminString
_CucsMorefImportRootRn_Object=MibTableColumn
cucsMorefImportRootRn=_CucsMorefImportRootRn_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,3),_CucsMorefImportRootRn_Type())
cucsMorefImportRootRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootRn.setStatus(_A)
_CucsMorefImportRootFsmDescr_Type=SnmpAdminString
_CucsMorefImportRootFsmDescr_Object=MibTableColumn
cucsMorefImportRootFsmDescr=_CucsMorefImportRootFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,4),_CucsMorefImportRootFsmDescr_Type())
cucsMorefImportRootFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmDescr.setStatus(_A)
_CucsMorefImportRootFsmPrev_Type=SnmpAdminString
_CucsMorefImportRootFsmPrev_Object=MibTableColumn
cucsMorefImportRootFsmPrev=_CucsMorefImportRootFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,5),_CucsMorefImportRootFsmPrev_Type())
cucsMorefImportRootFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmPrev.setStatus(_A)
_CucsMorefImportRootFsmProgr_Type=Gauge32
_CucsMorefImportRootFsmProgr_Object=MibTableColumn
cucsMorefImportRootFsmProgr=_CucsMorefImportRootFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,6),_CucsMorefImportRootFsmProgr_Type())
cucsMorefImportRootFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmProgr.setStatus(_A)
_CucsMorefImportRootFsmRmtInvErrCode_Type=Gauge32
_CucsMorefImportRootFsmRmtInvErrCode_Object=MibTableColumn
cucsMorefImportRootFsmRmtInvErrCode=_CucsMorefImportRootFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,7),_CucsMorefImportRootFsmRmtInvErrCode_Type())
cucsMorefImportRootFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmRmtInvErrCode.setStatus(_A)
_CucsMorefImportRootFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsMorefImportRootFsmRmtInvErrDescr_Object=MibTableColumn
cucsMorefImportRootFsmRmtInvErrDescr=_CucsMorefImportRootFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,8),_CucsMorefImportRootFsmRmtInvErrDescr_Type())
cucsMorefImportRootFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmRmtInvErrDescr.setStatus(_A)
_CucsMorefImportRootFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsMorefImportRootFsmRmtInvRslt_Object=MibTableColumn
cucsMorefImportRootFsmRmtInvRslt=_CucsMorefImportRootFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,9),_CucsMorefImportRootFsmRmtInvRslt_Type())
cucsMorefImportRootFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmRmtInvRslt.setStatus(_A)
_CucsMorefImportRootFsmStageDescr_Type=SnmpAdminString
_CucsMorefImportRootFsmStageDescr_Object=MibTableColumn
cucsMorefImportRootFsmStageDescr=_CucsMorefImportRootFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,10),_CucsMorefImportRootFsmStageDescr_Type())
cucsMorefImportRootFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageDescr.setStatus(_A)
_CucsMorefImportRootFsmStamp_Type=DateAndTime
_CucsMorefImportRootFsmStamp_Object=MibTableColumn
cucsMorefImportRootFsmStamp=_CucsMorefImportRootFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,11),_CucsMorefImportRootFsmStamp_Type())
cucsMorefImportRootFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStamp.setStatus(_A)
_CucsMorefImportRootFsmStatus_Type=SnmpAdminString
_CucsMorefImportRootFsmStatus_Object=MibTableColumn
cucsMorefImportRootFsmStatus=_CucsMorefImportRootFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,12),_CucsMorefImportRootFsmStatus_Type())
cucsMorefImportRootFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStatus.setStatus(_A)
_CucsMorefImportRootFsmTry_Type=Gauge32
_CucsMorefImportRootFsmTry_Object=MibTableColumn
cucsMorefImportRootFsmTry=_CucsMorefImportRootFsmTry_Object((1,3,6,1,4,1,9,9,719,1,92,2,1,13),_CucsMorefImportRootFsmTry_Type())
cucsMorefImportRootFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmTry.setStatus(_A)
_CucsMorefImportRootFsmTable_Object=MibTable
cucsMorefImportRootFsmTable=_CucsMorefImportRootFsmTable_Object((1,3,6,1,4,1,9,9,719,1,92,3))
if mibBuilder.loadTexts:cucsMorefImportRootFsmTable.setStatus(_A)
_CucsMorefImportRootFsmEntry_Object=MibTableRow
cucsMorefImportRootFsmEntry=_CucsMorefImportRootFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,92,3,1))
cucsMorefImportRootFsmEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsMorefImportRootFsmEntry.setStatus(_A)
_CucsMorefImportRootFsmInstanceId_Type=CucsManagedObjectId
_CucsMorefImportRootFsmInstanceId_Object=MibTableColumn
cucsMorefImportRootFsmInstanceId=_CucsMorefImportRootFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,1),_CucsMorefImportRootFsmInstanceId_Type())
cucsMorefImportRootFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMorefImportRootFsmInstanceId.setStatus(_A)
_CucsMorefImportRootFsmDn_Type=CucsManagedObjectDn
_CucsMorefImportRootFsmDn_Object=MibTableColumn
cucsMorefImportRootFsmDn=_CucsMorefImportRootFsmDn_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,2),_CucsMorefImportRootFsmDn_Type())
cucsMorefImportRootFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmDn.setStatus(_A)
_CucsMorefImportRootFsmRn_Type=SnmpAdminString
_CucsMorefImportRootFsmRn_Object=MibTableColumn
cucsMorefImportRootFsmRn=_CucsMorefImportRootFsmRn_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,3),_CucsMorefImportRootFsmRn_Type())
cucsMorefImportRootFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmRn.setStatus(_A)
_CucsMorefImportRootFsmCompletionTime_Type=DateAndTime
_CucsMorefImportRootFsmCompletionTime_Object=MibTableColumn
cucsMorefImportRootFsmCompletionTime=_CucsMorefImportRootFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,4),_CucsMorefImportRootFsmCompletionTime_Type())
cucsMorefImportRootFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmCompletionTime.setStatus(_A)
_CucsMorefImportRootFsmCurrentFsm_Type=CucsMorefImportRootFsmCurrentFsm
_CucsMorefImportRootFsmCurrentFsm_Object=MibTableColumn
cucsMorefImportRootFsmCurrentFsm=_CucsMorefImportRootFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,5),_CucsMorefImportRootFsmCurrentFsm_Type())
cucsMorefImportRootFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmCurrentFsm.setStatus(_A)
_CucsMorefImportRootFsmDescrData_Type=SnmpAdminString
_CucsMorefImportRootFsmDescrData_Object=MibTableColumn
cucsMorefImportRootFsmDescrData=_CucsMorefImportRootFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,6),_CucsMorefImportRootFsmDescrData_Type())
cucsMorefImportRootFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmDescrData.setStatus(_A)
_CucsMorefImportRootFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsMorefImportRootFsmFsmStatus_Object=MibTableColumn
cucsMorefImportRootFsmFsmStatus=_CucsMorefImportRootFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,7),_CucsMorefImportRootFsmFsmStatus_Type())
cucsMorefImportRootFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmFsmStatus.setStatus(_A)
_CucsMorefImportRootFsmProgress_Type=Gauge32
_CucsMorefImportRootFsmProgress_Object=MibTableColumn
cucsMorefImportRootFsmProgress=_CucsMorefImportRootFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,8),_CucsMorefImportRootFsmProgress_Type())
cucsMorefImportRootFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmProgress.setStatus(_A)
_CucsMorefImportRootFsmRmtErrCode_Type=Gauge32
_CucsMorefImportRootFsmRmtErrCode_Object=MibTableColumn
cucsMorefImportRootFsmRmtErrCode=_CucsMorefImportRootFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,9),_CucsMorefImportRootFsmRmtErrCode_Type())
cucsMorefImportRootFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmRmtErrCode.setStatus(_A)
_CucsMorefImportRootFsmRmtErrDescr_Type=SnmpAdminString
_CucsMorefImportRootFsmRmtErrDescr_Object=MibTableColumn
cucsMorefImportRootFsmRmtErrDescr=_CucsMorefImportRootFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,10),_CucsMorefImportRootFsmRmtErrDescr_Type())
cucsMorefImportRootFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmRmtErrDescr.setStatus(_A)
_CucsMorefImportRootFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsMorefImportRootFsmRmtRslt_Object=MibTableColumn
cucsMorefImportRootFsmRmtRslt=_CucsMorefImportRootFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,92,3,1,11),_CucsMorefImportRootFsmRmtRslt_Type())
cucsMorefImportRootFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmRmtRslt.setStatus(_A)
_CucsMorefImportRootFsmStageTable_Object=MibTable
cucsMorefImportRootFsmStageTable=_CucsMorefImportRootFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,92,4))
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageTable.setStatus(_A)
_CucsMorefImportRootFsmStageEntry_Object=MibTableRow
cucsMorefImportRootFsmStageEntry=_CucsMorefImportRootFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,92,4,1))
cucsMorefImportRootFsmStageEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageEntry.setStatus(_A)
_CucsMorefImportRootFsmStageInstanceId_Type=CucsManagedObjectId
_CucsMorefImportRootFsmStageInstanceId_Object=MibTableColumn
cucsMorefImportRootFsmStageInstanceId=_CucsMorefImportRootFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,92,4,1,1),_CucsMorefImportRootFsmStageInstanceId_Type())
cucsMorefImportRootFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageInstanceId.setStatus(_A)
_CucsMorefImportRootFsmStageDn_Type=CucsManagedObjectDn
_CucsMorefImportRootFsmStageDn_Object=MibTableColumn
cucsMorefImportRootFsmStageDn=_CucsMorefImportRootFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,92,4,1,2),_CucsMorefImportRootFsmStageDn_Type())
cucsMorefImportRootFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageDn.setStatus(_A)
_CucsMorefImportRootFsmStageRn_Type=SnmpAdminString
_CucsMorefImportRootFsmStageRn_Object=MibTableColumn
cucsMorefImportRootFsmStageRn=_CucsMorefImportRootFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,92,4,1,3),_CucsMorefImportRootFsmStageRn_Type())
cucsMorefImportRootFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageRn.setStatus(_A)
_CucsMorefImportRootFsmStageDescrData_Type=SnmpAdminString
_CucsMorefImportRootFsmStageDescrData_Object=MibTableColumn
cucsMorefImportRootFsmStageDescrData=_CucsMorefImportRootFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,92,4,1,4),_CucsMorefImportRootFsmStageDescrData_Type())
cucsMorefImportRootFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageDescrData.setStatus(_A)
_CucsMorefImportRootFsmStageLastUpdateTime_Type=DateAndTime
_CucsMorefImportRootFsmStageLastUpdateTime_Object=MibTableColumn
cucsMorefImportRootFsmStageLastUpdateTime=_CucsMorefImportRootFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,92,4,1,5),_CucsMorefImportRootFsmStageLastUpdateTime_Type())
cucsMorefImportRootFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageLastUpdateTime.setStatus(_A)
_CucsMorefImportRootFsmStageName_Type=CucsMorefImportRootFsmStageName
_CucsMorefImportRootFsmStageName_Object=MibTableColumn
cucsMorefImportRootFsmStageName=_CucsMorefImportRootFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,92,4,1,6),_CucsMorefImportRootFsmStageName_Type())
cucsMorefImportRootFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageName.setStatus(_A)
_CucsMorefImportRootFsmStageOrder_Type=Gauge32
_CucsMorefImportRootFsmStageOrder_Object=MibTableColumn
cucsMorefImportRootFsmStageOrder=_CucsMorefImportRootFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,92,4,1,7),_CucsMorefImportRootFsmStageOrder_Type())
cucsMorefImportRootFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageOrder.setStatus(_A)
_CucsMorefImportRootFsmStageRetry_Type=Gauge32
_CucsMorefImportRootFsmStageRetry_Object=MibTableColumn
cucsMorefImportRootFsmStageRetry=_CucsMorefImportRootFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,92,4,1,8),_CucsMorefImportRootFsmStageRetry_Type())
cucsMorefImportRootFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageRetry.setStatus(_A)
_CucsMorefImportRootFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsMorefImportRootFsmStageStageStatus_Object=MibTableColumn
cucsMorefImportRootFsmStageStageStatus=_CucsMorefImportRootFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,92,4,1,9),_CucsMorefImportRootFsmStageStageStatus_Type())
cucsMorefImportRootFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmStageStageStatus.setStatus(_A)
_CucsMorefImportRootFsmTaskTable_Object=MibTable
cucsMorefImportRootFsmTaskTable=_CucsMorefImportRootFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,92,5))
if mibBuilder.loadTexts:cucsMorefImportRootFsmTaskTable.setStatus(_A)
_CucsMorefImportRootFsmTaskEntry_Object=MibTableRow
cucsMorefImportRootFsmTaskEntry=_CucsMorefImportRootFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,92,5,1))
cucsMorefImportRootFsmTaskEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsMorefImportRootFsmTaskEntry.setStatus(_A)
_CucsMorefImportRootFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsMorefImportRootFsmTaskInstanceId_Object=MibTableColumn
cucsMorefImportRootFsmTaskInstanceId=_CucsMorefImportRootFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,92,5,1,1),_CucsMorefImportRootFsmTaskInstanceId_Type())
cucsMorefImportRootFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMorefImportRootFsmTaskInstanceId.setStatus(_A)
_CucsMorefImportRootFsmTaskDn_Type=CucsManagedObjectDn
_CucsMorefImportRootFsmTaskDn_Object=MibTableColumn
cucsMorefImportRootFsmTaskDn=_CucsMorefImportRootFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,92,5,1,2),_CucsMorefImportRootFsmTaskDn_Type())
cucsMorefImportRootFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmTaskDn.setStatus(_A)
_CucsMorefImportRootFsmTaskRn_Type=SnmpAdminString
_CucsMorefImportRootFsmTaskRn_Object=MibTableColumn
cucsMorefImportRootFsmTaskRn=_CucsMorefImportRootFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,92,5,1,3),_CucsMorefImportRootFsmTaskRn_Type())
cucsMorefImportRootFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmTaskRn.setStatus(_A)
_CucsMorefImportRootFsmTaskCompletion_Type=CucsFsmCompletion
_CucsMorefImportRootFsmTaskCompletion_Object=MibTableColumn
cucsMorefImportRootFsmTaskCompletion=_CucsMorefImportRootFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,92,5,1,4),_CucsMorefImportRootFsmTaskCompletion_Type())
cucsMorefImportRootFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmTaskCompletion.setStatus(_A)
_CucsMorefImportRootFsmTaskFlags_Type=CucsFsmFlags
_CucsMorefImportRootFsmTaskFlags_Object=MibTableColumn
cucsMorefImportRootFsmTaskFlags=_CucsMorefImportRootFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,92,5,1,5),_CucsMorefImportRootFsmTaskFlags_Type())
cucsMorefImportRootFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmTaskFlags.setStatus(_A)
_CucsMorefImportRootFsmTaskItem_Type=CucsMorefImportRootFsmTaskItem
_CucsMorefImportRootFsmTaskItem_Object=MibTableColumn
cucsMorefImportRootFsmTaskItem=_CucsMorefImportRootFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,92,5,1,6),_CucsMorefImportRootFsmTaskItem_Type())
cucsMorefImportRootFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmTaskItem.setStatus(_A)
_CucsMorefImportRootFsmTaskSeqId_Type=Gauge32
_CucsMorefImportRootFsmTaskSeqId_Object=MibTableColumn
cucsMorefImportRootFsmTaskSeqId=_CucsMorefImportRootFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,92,5,1,7),_CucsMorefImportRootFsmTaskSeqId_Type())
cucsMorefImportRootFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefImportRootFsmTaskSeqId.setStatus(_A)
_CucsMorefPropTable_Object=MibTable
cucsMorefPropTable=_CucsMorefPropTable_Object((1,3,6,1,4,1,9,9,719,1,92,6))
if mibBuilder.loadTexts:cucsMorefPropTable.setStatus(_A)
_CucsMorefPropEntry_Object=MibTableRow
cucsMorefPropEntry=_CucsMorefPropEntry_Object((1,3,6,1,4,1,9,9,719,1,92,6,1))
cucsMorefPropEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsMorefPropEntry.setStatus(_A)
_CucsMorefPropInstanceId_Type=CucsManagedObjectId
_CucsMorefPropInstanceId_Object=MibTableColumn
cucsMorefPropInstanceId=_CucsMorefPropInstanceId_Object((1,3,6,1,4,1,9,9,719,1,92,6,1,1),_CucsMorefPropInstanceId_Type())
cucsMorefPropInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMorefPropInstanceId.setStatus(_A)
_CucsMorefPropDn_Type=CucsManagedObjectDn
_CucsMorefPropDn_Object=MibTableColumn
cucsMorefPropDn=_CucsMorefPropDn_Object((1,3,6,1,4,1,9,9,719,1,92,6,1,2),_CucsMorefPropDn_Type())
cucsMorefPropDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefPropDn.setStatus(_A)
_CucsMorefPropRn_Type=SnmpAdminString
_CucsMorefPropRn_Object=MibTableColumn
cucsMorefPropRn=_CucsMorefPropRn_Object((1,3,6,1,4,1,9,9,719,1,92,6,1,3),_CucsMorefPropRn_Type())
cucsMorefPropRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefPropRn.setStatus(_A)
_CucsMorefPropAdminState_Type=CucsMorefAdminState
_CucsMorefPropAdminState_Object=MibTableColumn
cucsMorefPropAdminState=_CucsMorefPropAdminState_Object((1,3,6,1,4,1,9,9,719,1,92,6,1,4),_CucsMorefPropAdminState_Type())
cucsMorefPropAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefPropAdminState.setStatus(_A)
_CucsMorefPropName_Type=SnmpAdminString
_CucsMorefPropName_Object=MibTableColumn
cucsMorefPropName=_CucsMorefPropName_Object((1,3,6,1,4,1,9,9,719,1,92,6,1,5),_CucsMorefPropName_Type())
cucsMorefPropName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefPropName.setStatus(_A)
_CucsMorefPropValue_Type=SnmpAdminString
_CucsMorefPropValue_Object=MibTableColumn
cucsMorefPropValue=_CucsMorefPropValue_Object((1,3,6,1,4,1,9,9,719,1,92,6,1,6),_CucsMorefPropValue_Type())
cucsMorefPropValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefPropValue.setStatus(_A)
_CucsMorefRefTable_Object=MibTable
cucsMorefRefTable=_CucsMorefRefTable_Object((1,3,6,1,4,1,9,9,719,1,92,7))
if mibBuilder.loadTexts:cucsMorefRefTable.setStatus(_A)
_CucsMorefRefEntry_Object=MibTableRow
cucsMorefRefEntry=_CucsMorefRefEntry_Object((1,3,6,1,4,1,9,9,719,1,92,7,1))
cucsMorefRefEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsMorefRefEntry.setStatus(_A)
_CucsMorefRefInstanceId_Type=CucsManagedObjectId
_CucsMorefRefInstanceId_Object=MibTableColumn
cucsMorefRefInstanceId=_CucsMorefRefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,92,7,1,1),_CucsMorefRefInstanceId_Type())
cucsMorefRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMorefRefInstanceId.setStatus(_A)
_CucsMorefRefDn_Type=CucsManagedObjectDn
_CucsMorefRefDn_Object=MibTableColumn
cucsMorefRefDn=_CucsMorefRefDn_Object((1,3,6,1,4,1,9,9,719,1,92,7,1,2),_CucsMorefRefDn_Type())
cucsMorefRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefRefDn.setStatus(_A)
_CucsMorefRefRn_Type=SnmpAdminString
_CucsMorefRefRn_Object=MibTableColumn
cucsMorefRefRn=_CucsMorefRefRn_Object((1,3,6,1,4,1,9,9,719,1,92,7,1,3),_CucsMorefRefRn_Type())
cucsMorefRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefRefRn.setStatus(_A)
_CucsMorefRefMoRn_Type=SnmpAdminString
_CucsMorefRefMoRn_Object=MibTableColumn
cucsMorefRefMoRn=_CucsMorefRefMoRn_Object((1,3,6,1,4,1,9,9,719,1,92,7,1,6),_CucsMorefRefMoRn_Type())
cucsMorefRefMoRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMorefRefMoRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsMorefObjects':cucsMorefObjects,'cucsMorefFruRefTable':cucsMorefFruRefTable,'cucsMorefFruRefEntry':cucsMorefFruRefEntry,_E:cucsMorefFruRefInstanceId,'cucsMorefFruRefDn':cucsMorefFruRefDn,'cucsMorefFruRefRn':cucsMorefFruRefRn,'cucsMorefFruRefClassName':cucsMorefFruRefClassName,'cucsMorefFruRefModel':cucsMorefFruRefModel,'cucsMorefFruRefSerial':cucsMorefFruRefSerial,'cucsMorefFruRefVendor':cucsMorefFruRefVendor,'cucsMorefImportRootTable':cucsMorefImportRootTable,'cucsMorefImportRootEntry':cucsMorefImportRootEntry,_F:cucsMorefImportRootInstanceId,'cucsMorefImportRootDn':cucsMorefImportRootDn,'cucsMorefImportRootRn':cucsMorefImportRootRn,'cucsMorefImportRootFsmDescr':cucsMorefImportRootFsmDescr,'cucsMorefImportRootFsmPrev':cucsMorefImportRootFsmPrev,'cucsMorefImportRootFsmProgr':cucsMorefImportRootFsmProgr,'cucsMorefImportRootFsmRmtInvErrCode':cucsMorefImportRootFsmRmtInvErrCode,'cucsMorefImportRootFsmRmtInvErrDescr':cucsMorefImportRootFsmRmtInvErrDescr,'cucsMorefImportRootFsmRmtInvRslt':cucsMorefImportRootFsmRmtInvRslt,'cucsMorefImportRootFsmStageDescr':cucsMorefImportRootFsmStageDescr,'cucsMorefImportRootFsmStamp':cucsMorefImportRootFsmStamp,'cucsMorefImportRootFsmStatus':cucsMorefImportRootFsmStatus,'cucsMorefImportRootFsmTry':cucsMorefImportRootFsmTry,'cucsMorefImportRootFsmTable':cucsMorefImportRootFsmTable,'cucsMorefImportRootFsmEntry':cucsMorefImportRootFsmEntry,_G:cucsMorefImportRootFsmInstanceId,'cucsMorefImportRootFsmDn':cucsMorefImportRootFsmDn,'cucsMorefImportRootFsmRn':cucsMorefImportRootFsmRn,'cucsMorefImportRootFsmCompletionTime':cucsMorefImportRootFsmCompletionTime,'cucsMorefImportRootFsmCurrentFsm':cucsMorefImportRootFsmCurrentFsm,'cucsMorefImportRootFsmDescrData':cucsMorefImportRootFsmDescrData,'cucsMorefImportRootFsmFsmStatus':cucsMorefImportRootFsmFsmStatus,'cucsMorefImportRootFsmProgress':cucsMorefImportRootFsmProgress,'cucsMorefImportRootFsmRmtErrCode':cucsMorefImportRootFsmRmtErrCode,'cucsMorefImportRootFsmRmtErrDescr':cucsMorefImportRootFsmRmtErrDescr,'cucsMorefImportRootFsmRmtRslt':cucsMorefImportRootFsmRmtRslt,'cucsMorefImportRootFsmStageTable':cucsMorefImportRootFsmStageTable,'cucsMorefImportRootFsmStageEntry':cucsMorefImportRootFsmStageEntry,_H:cucsMorefImportRootFsmStageInstanceId,'cucsMorefImportRootFsmStageDn':cucsMorefImportRootFsmStageDn,'cucsMorefImportRootFsmStageRn':cucsMorefImportRootFsmStageRn,'cucsMorefImportRootFsmStageDescrData':cucsMorefImportRootFsmStageDescrData,'cucsMorefImportRootFsmStageLastUpdateTime':cucsMorefImportRootFsmStageLastUpdateTime,'cucsMorefImportRootFsmStageName':cucsMorefImportRootFsmStageName,'cucsMorefImportRootFsmStageOrder':cucsMorefImportRootFsmStageOrder,'cucsMorefImportRootFsmStageRetry':cucsMorefImportRootFsmStageRetry,'cucsMorefImportRootFsmStageStageStatus':cucsMorefImportRootFsmStageStageStatus,'cucsMorefImportRootFsmTaskTable':cucsMorefImportRootFsmTaskTable,'cucsMorefImportRootFsmTaskEntry':cucsMorefImportRootFsmTaskEntry,_I:cucsMorefImportRootFsmTaskInstanceId,'cucsMorefImportRootFsmTaskDn':cucsMorefImportRootFsmTaskDn,'cucsMorefImportRootFsmTaskRn':cucsMorefImportRootFsmTaskRn,'cucsMorefImportRootFsmTaskCompletion':cucsMorefImportRootFsmTaskCompletion,'cucsMorefImportRootFsmTaskFlags':cucsMorefImportRootFsmTaskFlags,'cucsMorefImportRootFsmTaskItem':cucsMorefImportRootFsmTaskItem,'cucsMorefImportRootFsmTaskSeqId':cucsMorefImportRootFsmTaskSeqId,'cucsMorefPropTable':cucsMorefPropTable,'cucsMorefPropEntry':cucsMorefPropEntry,_J:cucsMorefPropInstanceId,'cucsMorefPropDn':cucsMorefPropDn,'cucsMorefPropRn':cucsMorefPropRn,'cucsMorefPropAdminState':cucsMorefPropAdminState,'cucsMorefPropName':cucsMorefPropName,'cucsMorefPropValue':cucsMorefPropValue,'cucsMorefRefTable':cucsMorefRefTable,'cucsMorefRefEntry':cucsMorefRefEntry,_K:cucsMorefRefInstanceId,'cucsMorefRefDn':cucsMorefRefDn,'cucsMorefRefRn':cucsMorefRefRn,'cucsMorefRefMoRn':cucsMorefRefMoRn})