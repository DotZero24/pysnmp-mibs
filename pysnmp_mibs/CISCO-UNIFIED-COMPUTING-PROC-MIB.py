_K='cucsProcSvcInstanceId'
_J='cucsProcTxCountsInstanceId'
_I='cucsProcStimulusCountsInstanceId'
_H='cucsProcPrtCountsInstanceId'
_G='cucsProcPrtInstanceId'
_F='cucsProcManagerInstanceId'
_E='cucsProcDoerInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-PROC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsProcStatAdminState,=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsProcStatAdminState')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsProcObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,40))
_CucsProcDoerTable_Object=MibTable
cucsProcDoerTable=_CucsProcDoerTable_Object((1,3,6,1,4,1,9,9,719,1,40,1))
if mibBuilder.loadTexts:cucsProcDoerTable.setStatus(_A)
_CucsProcDoerEntry_Object=MibTableRow
cucsProcDoerEntry=_CucsProcDoerEntry_Object((1,3,6,1,4,1,9,9,719,1,40,1,1))
cucsProcDoerEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsProcDoerEntry.setStatus(_A)
_CucsProcDoerInstanceId_Type=CucsManagedObjectId
_CucsProcDoerInstanceId_Object=MibTableColumn
cucsProcDoerInstanceId=_CucsProcDoerInstanceId_Object((1,3,6,1,4,1,9,9,719,1,40,1,1,1),_CucsProcDoerInstanceId_Type())
cucsProcDoerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsProcDoerInstanceId.setStatus(_A)
_CucsProcDoerDn_Type=CucsManagedObjectDn
_CucsProcDoerDn_Object=MibTableColumn
cucsProcDoerDn=_CucsProcDoerDn_Object((1,3,6,1,4,1,9,9,719,1,40,1,1,2),_CucsProcDoerDn_Type())
cucsProcDoerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcDoerDn.setStatus(_A)
_CucsProcDoerRn_Type=SnmpAdminString
_CucsProcDoerRn_Object=MibTableColumn
cucsProcDoerRn=_CucsProcDoerRn_Object((1,3,6,1,4,1,9,9,719,1,40,1,1,3),_CucsProcDoerRn_Type())
cucsProcDoerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcDoerRn.setStatus(_A)
_CucsProcDoerId_Type=Gauge32
_CucsProcDoerId_Object=MibTableColumn
cucsProcDoerId=_CucsProcDoerId_Object((1,3,6,1,4,1,9,9,719,1,40,1,1,4),_CucsProcDoerId_Type())
cucsProcDoerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcDoerId.setStatus(_A)
_CucsProcDoerName_Type=SnmpAdminString
_CucsProcDoerName_Object=MibTableColumn
cucsProcDoerName=_CucsProcDoerName_Object((1,3,6,1,4,1,9,9,719,1,40,1,1,5),_CucsProcDoerName_Type())
cucsProcDoerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcDoerName.setStatus(_A)
_CucsProcManagerTable_Object=MibTable
cucsProcManagerTable=_CucsProcManagerTable_Object((1,3,6,1,4,1,9,9,719,1,40,2))
if mibBuilder.loadTexts:cucsProcManagerTable.setStatus(_A)
_CucsProcManagerEntry_Object=MibTableRow
cucsProcManagerEntry=_CucsProcManagerEntry_Object((1,3,6,1,4,1,9,9,719,1,40,2,1))
cucsProcManagerEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsProcManagerEntry.setStatus(_A)
_CucsProcManagerInstanceId_Type=CucsManagedObjectId
_CucsProcManagerInstanceId_Object=MibTableColumn
cucsProcManagerInstanceId=_CucsProcManagerInstanceId_Object((1,3,6,1,4,1,9,9,719,1,40,2,1,1),_CucsProcManagerInstanceId_Type())
cucsProcManagerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsProcManagerInstanceId.setStatus(_A)
_CucsProcManagerDn_Type=CucsManagedObjectDn
_CucsProcManagerDn_Object=MibTableColumn
cucsProcManagerDn=_CucsProcManagerDn_Object((1,3,6,1,4,1,9,9,719,1,40,2,1,2),_CucsProcManagerDn_Type())
cucsProcManagerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcManagerDn.setStatus(_A)
_CucsProcManagerRn_Type=SnmpAdminString
_CucsProcManagerRn_Object=MibTableColumn
cucsProcManagerRn=_CucsProcManagerRn_Object((1,3,6,1,4,1,9,9,719,1,40,2,1,3),_CucsProcManagerRn_Type())
cucsProcManagerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcManagerRn.setStatus(_A)
_CucsProcPrtTable_Object=MibTable
cucsProcPrtTable=_CucsProcPrtTable_Object((1,3,6,1,4,1,9,9,719,1,40,3))
if mibBuilder.loadTexts:cucsProcPrtTable.setStatus(_A)
_CucsProcPrtEntry_Object=MibTableRow
cucsProcPrtEntry=_CucsProcPrtEntry_Object((1,3,6,1,4,1,9,9,719,1,40,3,1))
cucsProcPrtEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsProcPrtEntry.setStatus(_A)
_CucsProcPrtInstanceId_Type=CucsManagedObjectId
_CucsProcPrtInstanceId_Object=MibTableColumn
cucsProcPrtInstanceId=_CucsProcPrtInstanceId_Object((1,3,6,1,4,1,9,9,719,1,40,3,1,1),_CucsProcPrtInstanceId_Type())
cucsProcPrtInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsProcPrtInstanceId.setStatus(_A)
_CucsProcPrtDn_Type=CucsManagedObjectDn
_CucsProcPrtDn_Object=MibTableColumn
cucsProcPrtDn=_CucsProcPrtDn_Object((1,3,6,1,4,1,9,9,719,1,40,3,1,2),_CucsProcPrtDn_Type())
cucsProcPrtDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtDn.setStatus(_A)
_CucsProcPrtRn_Type=SnmpAdminString
_CucsProcPrtRn_Object=MibTableColumn
cucsProcPrtRn=_CucsProcPrtRn_Object((1,3,6,1,4,1,9,9,719,1,40,3,1,3),_CucsProcPrtRn_Type())
cucsProcPrtRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtRn.setStatus(_A)
_CucsProcPrtId_Type=Gauge32
_CucsProcPrtId_Object=MibTableColumn
cucsProcPrtId=_CucsProcPrtId_Object((1,3,6,1,4,1,9,9,719,1,40,3,1,4),_CucsProcPrtId_Type())
cucsProcPrtId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtId.setStatus(_A)
_CucsProcPrtName_Type=SnmpAdminString
_CucsProcPrtName_Object=MibTableColumn
cucsProcPrtName=_CucsProcPrtName_Object((1,3,6,1,4,1,9,9,719,1,40,3,1,5),_CucsProcPrtName_Type())
cucsProcPrtName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtName.setStatus(_A)
_CucsProcPrtCountsTable_Object=MibTable
cucsProcPrtCountsTable=_CucsProcPrtCountsTable_Object((1,3,6,1,4,1,9,9,719,1,40,4))
if mibBuilder.loadTexts:cucsProcPrtCountsTable.setStatus(_A)
_CucsProcPrtCountsEntry_Object=MibTableRow
cucsProcPrtCountsEntry=_CucsProcPrtCountsEntry_Object((1,3,6,1,4,1,9,9,719,1,40,4,1))
cucsProcPrtCountsEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsProcPrtCountsEntry.setStatus(_A)
_CucsProcPrtCountsInstanceId_Type=CucsManagedObjectId
_CucsProcPrtCountsInstanceId_Object=MibTableColumn
cucsProcPrtCountsInstanceId=_CucsProcPrtCountsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,40,4,1,1),_CucsProcPrtCountsInstanceId_Type())
cucsProcPrtCountsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsProcPrtCountsInstanceId.setStatus(_A)
_CucsProcPrtCountsDn_Type=CucsManagedObjectDn
_CucsProcPrtCountsDn_Object=MibTableColumn
cucsProcPrtCountsDn=_CucsProcPrtCountsDn_Object((1,3,6,1,4,1,9,9,719,1,40,4,1,2),_CucsProcPrtCountsDn_Type())
cucsProcPrtCountsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtCountsDn.setStatus(_A)
_CucsProcPrtCountsRn_Type=SnmpAdminString
_CucsProcPrtCountsRn_Object=MibTableColumn
cucsProcPrtCountsRn=_CucsProcPrtCountsRn_Object((1,3,6,1,4,1,9,9,719,1,40,4,1,3),_CucsProcPrtCountsRn_Type())
cucsProcPrtCountsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtCountsRn.setStatus(_A)
_CucsProcPrtCountsDbtxs_Type=Gauge32
_CucsProcPrtCountsDbtxs_Object=MibTableColumn
cucsProcPrtCountsDbtxs=_CucsProcPrtCountsDbtxs_Object((1,3,6,1,4,1,9,9,719,1,40,4,1,4),_CucsProcPrtCountsDbtxs_Type())
cucsProcPrtCountsDbtxs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtCountsDbtxs.setStatus(_A)
_CucsProcPrtCountsTotal_Type=Gauge32
_CucsProcPrtCountsTotal_Object=MibTableColumn
cucsProcPrtCountsTotal=_CucsProcPrtCountsTotal_Object((1,3,6,1,4,1,9,9,719,1,40,4,1,5),_CucsProcPrtCountsTotal_Type())
cucsProcPrtCountsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtCountsTotal.setStatus(_A)
_CucsProcPrtCountsCachenospc_Type=Gauge32
_CucsProcPrtCountsCachenospc_Object=MibTableColumn
cucsProcPrtCountsCachenospc=_CucsProcPrtCountsCachenospc_Object((1,3,6,1,4,1,9,9,719,1,40,4,1,6),_CucsProcPrtCountsCachenospc_Type())
cucsProcPrtCountsCachenospc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtCountsCachenospc.setStatus(_A)
_CucsProcPrtCountsLargetxs_Type=Gauge32
_CucsProcPrtCountsLargetxs_Object=MibTableColumn
cucsProcPrtCountsLargetxs=_CucsProcPrtCountsLargetxs_Object((1,3,6,1,4,1,9,9,719,1,40,4,1,7),_CucsProcPrtCountsLargetxs_Type())
cucsProcPrtCountsLargetxs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtCountsLargetxs.setStatus(_A)
_CucsProcPrtCountsPersistTime_Type=Unsigned64
_CucsProcPrtCountsPersistTime_Object=MibTableColumn
cucsProcPrtCountsPersistTime=_CucsProcPrtCountsPersistTime_Object((1,3,6,1,4,1,9,9,719,1,40,4,1,8),_CucsProcPrtCountsPersistTime_Type())
cucsProcPrtCountsPersistTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcPrtCountsPersistTime.setStatus(_A)
_CucsProcStimulusCountsTable_Object=MibTable
cucsProcStimulusCountsTable=_CucsProcStimulusCountsTable_Object((1,3,6,1,4,1,9,9,719,1,40,5))
if mibBuilder.loadTexts:cucsProcStimulusCountsTable.setStatus(_A)
_CucsProcStimulusCountsEntry_Object=MibTableRow
cucsProcStimulusCountsEntry=_CucsProcStimulusCountsEntry_Object((1,3,6,1,4,1,9,9,719,1,40,5,1))
cucsProcStimulusCountsEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsProcStimulusCountsEntry.setStatus(_A)
_CucsProcStimulusCountsInstanceId_Type=CucsManagedObjectId
_CucsProcStimulusCountsInstanceId_Object=MibTableColumn
cucsProcStimulusCountsInstanceId=_CucsProcStimulusCountsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,1),_CucsProcStimulusCountsInstanceId_Type())
cucsProcStimulusCountsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsProcStimulusCountsInstanceId.setStatus(_A)
_CucsProcStimulusCountsDn_Type=CucsManagedObjectDn
_CucsProcStimulusCountsDn_Object=MibTableColumn
cucsProcStimulusCountsDn=_CucsProcStimulusCountsDn_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,2),_CucsProcStimulusCountsDn_Type())
cucsProcStimulusCountsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcStimulusCountsDn.setStatus(_A)
_CucsProcStimulusCountsRn_Type=SnmpAdminString
_CucsProcStimulusCountsRn_Object=MibTableColumn
cucsProcStimulusCountsRn=_CucsProcStimulusCountsRn_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,3),_CucsProcStimulusCountsRn_Type())
cucsProcStimulusCountsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcStimulusCountsRn.setStatus(_A)
_CucsProcStimulusCountsBulked_Type=Gauge32
_CucsProcStimulusCountsBulked_Object=MibTableColumn
cucsProcStimulusCountsBulked=_CucsProcStimulusCountsBulked_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,4),_CucsProcStimulusCountsBulked_Type())
cucsProcStimulusCountsBulked.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcStimulusCountsBulked.setStatus(_A)
_CucsProcStimulusCountsFailed_Type=Gauge32
_CucsProcStimulusCountsFailed_Object=MibTableColumn
cucsProcStimulusCountsFailed=_CucsProcStimulusCountsFailed_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,5),_CucsProcStimulusCountsFailed_Type())
cucsProcStimulusCountsFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcStimulusCountsFailed.setStatus(_A)
_CucsProcStimulusCountsRetried_Type=Gauge32
_CucsProcStimulusCountsRetried_Object=MibTableColumn
cucsProcStimulusCountsRetried=_CucsProcStimulusCountsRetried_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,6),_CucsProcStimulusCountsRetried_Type())
cucsProcStimulusCountsRetried.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcStimulusCountsRetried.setStatus(_A)
_CucsProcStimulusCountsSingleton_Type=Gauge32
_CucsProcStimulusCountsSingleton_Object=MibTableColumn
cucsProcStimulusCountsSingleton=_CucsProcStimulusCountsSingleton_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,7),_CucsProcStimulusCountsSingleton_Type())
cucsProcStimulusCountsSingleton.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcStimulusCountsSingleton.setStatus(_A)
_CucsProcStimulusCountsSuccessfull_Type=Gauge32
_CucsProcStimulusCountsSuccessfull_Object=MibTableColumn
cucsProcStimulusCountsSuccessfull=_CucsProcStimulusCountsSuccessfull_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,8),_CucsProcStimulusCountsSuccessfull_Type())
cucsProcStimulusCountsSuccessfull.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcStimulusCountsSuccessfull.setStatus(_A)
_CucsProcStimulusCountsTotal_Type=Gauge32
_CucsProcStimulusCountsTotal_Object=MibTableColumn
cucsProcStimulusCountsTotal=_CucsProcStimulusCountsTotal_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,9),_CucsProcStimulusCountsTotal_Type())
cucsProcStimulusCountsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcStimulusCountsTotal.setStatus(_A)
_CucsProcStimulusCountsAdminState_Type=CucsProcStatAdminState
_CucsProcStimulusCountsAdminState_Object=MibTableColumn
cucsProcStimulusCountsAdminState=_CucsProcStimulusCountsAdminState_Object((1,3,6,1,4,1,9,9,719,1,40,5,1,10),_CucsProcStimulusCountsAdminState_Type())
cucsProcStimulusCountsAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcStimulusCountsAdminState.setStatus(_A)
_CucsProcTxCountsTable_Object=MibTable
cucsProcTxCountsTable=_CucsProcTxCountsTable_Object((1,3,6,1,4,1,9,9,719,1,40,6))
if mibBuilder.loadTexts:cucsProcTxCountsTable.setStatus(_A)
_CucsProcTxCountsEntry_Object=MibTableRow
cucsProcTxCountsEntry=_CucsProcTxCountsEntry_Object((1,3,6,1,4,1,9,9,719,1,40,6,1))
cucsProcTxCountsEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsProcTxCountsEntry.setStatus(_A)
_CucsProcTxCountsInstanceId_Type=CucsManagedObjectId
_CucsProcTxCountsInstanceId_Object=MibTableColumn
cucsProcTxCountsInstanceId=_CucsProcTxCountsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,1),_CucsProcTxCountsInstanceId_Type())
cucsProcTxCountsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsProcTxCountsInstanceId.setStatus(_A)
_CucsProcTxCountsDn_Type=CucsManagedObjectDn
_CucsProcTxCountsDn_Object=MibTableColumn
cucsProcTxCountsDn=_CucsProcTxCountsDn_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,2),_CucsProcTxCountsDn_Type())
cucsProcTxCountsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcTxCountsDn.setStatus(_A)
_CucsProcTxCountsRn_Type=SnmpAdminString
_CucsProcTxCountsRn_Object=MibTableColumn
cucsProcTxCountsRn=_CucsProcTxCountsRn_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,3),_CucsProcTxCountsRn_Type())
cucsProcTxCountsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcTxCountsRn.setStatus(_A)
_CucsProcTxCountsBulked_Type=Gauge32
_CucsProcTxCountsBulked_Object=MibTableColumn
cucsProcTxCountsBulked=_CucsProcTxCountsBulked_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,4),_CucsProcTxCountsBulked_Type())
cucsProcTxCountsBulked.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcTxCountsBulked.setStatus(_A)
_CucsProcTxCountsFailed_Type=Gauge32
_CucsProcTxCountsFailed_Object=MibTableColumn
cucsProcTxCountsFailed=_CucsProcTxCountsFailed_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,5),_CucsProcTxCountsFailed_Type())
cucsProcTxCountsFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcTxCountsFailed.setStatus(_A)
_CucsProcTxCountsRetried_Type=Gauge32
_CucsProcTxCountsRetried_Object=MibTableColumn
cucsProcTxCountsRetried=_CucsProcTxCountsRetried_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,6),_CucsProcTxCountsRetried_Type())
cucsProcTxCountsRetried.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcTxCountsRetried.setStatus(_A)
_CucsProcTxCountsSingleton_Type=Gauge32
_CucsProcTxCountsSingleton_Object=MibTableColumn
cucsProcTxCountsSingleton=_CucsProcTxCountsSingleton_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,7),_CucsProcTxCountsSingleton_Type())
cucsProcTxCountsSingleton.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcTxCountsSingleton.setStatus(_A)
_CucsProcTxCountsSuccessfull_Type=Gauge32
_CucsProcTxCountsSuccessfull_Object=MibTableColumn
cucsProcTxCountsSuccessfull=_CucsProcTxCountsSuccessfull_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,8),_CucsProcTxCountsSuccessfull_Type())
cucsProcTxCountsSuccessfull.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcTxCountsSuccessfull.setStatus(_A)
_CucsProcTxCountsTotal_Type=Gauge32
_CucsProcTxCountsTotal_Object=MibTableColumn
cucsProcTxCountsTotal=_CucsProcTxCountsTotal_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,9),_CucsProcTxCountsTotal_Type())
cucsProcTxCountsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcTxCountsTotal.setStatus(_A)
_CucsProcTxCountsAdminState_Type=CucsProcStatAdminState
_CucsProcTxCountsAdminState_Object=MibTableColumn
cucsProcTxCountsAdminState=_CucsProcTxCountsAdminState_Object((1,3,6,1,4,1,9,9,719,1,40,6,1,10),_CucsProcTxCountsAdminState_Type())
cucsProcTxCountsAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcTxCountsAdminState.setStatus(_A)
_CucsProcSvcTable_Object=MibTable
cucsProcSvcTable=_CucsProcSvcTable_Object((1,3,6,1,4,1,9,9,719,1,40,7))
if mibBuilder.loadTexts:cucsProcSvcTable.setStatus(_A)
_CucsProcSvcEntry_Object=MibTableRow
cucsProcSvcEntry=_CucsProcSvcEntry_Object((1,3,6,1,4,1,9,9,719,1,40,7,1))
cucsProcSvcEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsProcSvcEntry.setStatus(_A)
_CucsProcSvcInstanceId_Type=CucsManagedObjectId
_CucsProcSvcInstanceId_Object=MibTableColumn
cucsProcSvcInstanceId=_CucsProcSvcInstanceId_Object((1,3,6,1,4,1,9,9,719,1,40,7,1,1),_CucsProcSvcInstanceId_Type())
cucsProcSvcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsProcSvcInstanceId.setStatus(_A)
_CucsProcSvcDn_Type=CucsManagedObjectDn
_CucsProcSvcDn_Object=MibTableColumn
cucsProcSvcDn=_CucsProcSvcDn_Object((1,3,6,1,4,1,9,9,719,1,40,7,1,2),_CucsProcSvcDn_Type())
cucsProcSvcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcSvcDn.setStatus(_A)
_CucsProcSvcRn_Type=SnmpAdminString
_CucsProcSvcRn_Object=MibTableColumn
cucsProcSvcRn=_CucsProcSvcRn_Object((1,3,6,1,4,1,9,9,719,1,40,7,1,3),_CucsProcSvcRn_Type())
cucsProcSvcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcSvcRn.setStatus(_A)
_CucsProcSvcId_Type=Gauge32
_CucsProcSvcId_Object=MibTableColumn
cucsProcSvcId=_CucsProcSvcId_Object((1,3,6,1,4,1,9,9,719,1,40,7,1,4),_CucsProcSvcId_Type())
cucsProcSvcId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcSvcId.setStatus(_A)
_CucsProcSvcName_Type=SnmpAdminString
_CucsProcSvcName_Object=MibTableColumn
cucsProcSvcName=_CucsProcSvcName_Object((1,3,6,1,4,1,9,9,719,1,40,7,1,5),_CucsProcSvcName_Type())
cucsProcSvcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsProcSvcName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsProcObjects':cucsProcObjects,'cucsProcDoerTable':cucsProcDoerTable,'cucsProcDoerEntry':cucsProcDoerEntry,_E:cucsProcDoerInstanceId,'cucsProcDoerDn':cucsProcDoerDn,'cucsProcDoerRn':cucsProcDoerRn,'cucsProcDoerId':cucsProcDoerId,'cucsProcDoerName':cucsProcDoerName,'cucsProcManagerTable':cucsProcManagerTable,'cucsProcManagerEntry':cucsProcManagerEntry,_F:cucsProcManagerInstanceId,'cucsProcManagerDn':cucsProcManagerDn,'cucsProcManagerRn':cucsProcManagerRn,'cucsProcPrtTable':cucsProcPrtTable,'cucsProcPrtEntry':cucsProcPrtEntry,_G:cucsProcPrtInstanceId,'cucsProcPrtDn':cucsProcPrtDn,'cucsProcPrtRn':cucsProcPrtRn,'cucsProcPrtId':cucsProcPrtId,'cucsProcPrtName':cucsProcPrtName,'cucsProcPrtCountsTable':cucsProcPrtCountsTable,'cucsProcPrtCountsEntry':cucsProcPrtCountsEntry,_H:cucsProcPrtCountsInstanceId,'cucsProcPrtCountsDn':cucsProcPrtCountsDn,'cucsProcPrtCountsRn':cucsProcPrtCountsRn,'cucsProcPrtCountsDbtxs':cucsProcPrtCountsDbtxs,'cucsProcPrtCountsTotal':cucsProcPrtCountsTotal,'cucsProcPrtCountsCachenospc':cucsProcPrtCountsCachenospc,'cucsProcPrtCountsLargetxs':cucsProcPrtCountsLargetxs,'cucsProcPrtCountsPersistTime':cucsProcPrtCountsPersistTime,'cucsProcStimulusCountsTable':cucsProcStimulusCountsTable,'cucsProcStimulusCountsEntry':cucsProcStimulusCountsEntry,_I:cucsProcStimulusCountsInstanceId,'cucsProcStimulusCountsDn':cucsProcStimulusCountsDn,'cucsProcStimulusCountsRn':cucsProcStimulusCountsRn,'cucsProcStimulusCountsBulked':cucsProcStimulusCountsBulked,'cucsProcStimulusCountsFailed':cucsProcStimulusCountsFailed,'cucsProcStimulusCountsRetried':cucsProcStimulusCountsRetried,'cucsProcStimulusCountsSingleton':cucsProcStimulusCountsSingleton,'cucsProcStimulusCountsSuccessfull':cucsProcStimulusCountsSuccessfull,'cucsProcStimulusCountsTotal':cucsProcStimulusCountsTotal,'cucsProcStimulusCountsAdminState':cucsProcStimulusCountsAdminState,'cucsProcTxCountsTable':cucsProcTxCountsTable,'cucsProcTxCountsEntry':cucsProcTxCountsEntry,_J:cucsProcTxCountsInstanceId,'cucsProcTxCountsDn':cucsProcTxCountsDn,'cucsProcTxCountsRn':cucsProcTxCountsRn,'cucsProcTxCountsBulked':cucsProcTxCountsBulked,'cucsProcTxCountsFailed':cucsProcTxCountsFailed,'cucsProcTxCountsRetried':cucsProcTxCountsRetried,'cucsProcTxCountsSingleton':cucsProcTxCountsSingleton,'cucsProcTxCountsSuccessfull':cucsProcTxCountsSuccessfull,'cucsProcTxCountsTotal':cucsProcTxCountsTotal,'cucsProcTxCountsAdminState':cucsProcTxCountsAdminState,'cucsProcSvcTable':cucsProcSvcTable,'cucsProcSvcEntry':cucsProcSvcEntry,_K:cucsProcSvcInstanceId,'cucsProcSvcDn':cucsProcSvcDn,'cucsProcSvcRn':cucsProcSvcRn,'cucsProcSvcId':cucsProcSvcId,'cucsProcSvcName':cucsProcSvcName})