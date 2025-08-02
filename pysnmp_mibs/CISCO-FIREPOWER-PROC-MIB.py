_K='cfprProcTxCountsInstanceId'
_J='cfprProcSvcInstanceId'
_I='cfprProcStimulusCountsInstanceId'
_H='cfprProcPrtCountsInstanceId'
_G='cfprProcPrtInstanceId'
_F='cfprProcManagerInstanceId'
_E='cfprProcDoerInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-PROC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprProcStatAdminState,=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprProcStatAdminState')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprProcObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,65))
_CfprProcDoerTable_Object=MibTable
cfprProcDoerTable=_CfprProcDoerTable_Object((1,3,6,1,4,1,9,9,826,1,65,1))
if mibBuilder.loadTexts:cfprProcDoerTable.setStatus(_A)
_CfprProcDoerEntry_Object=MibTableRow
cfprProcDoerEntry=_CfprProcDoerEntry_Object((1,3,6,1,4,1,9,9,826,1,65,1,1))
cfprProcDoerEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprProcDoerEntry.setStatus(_A)
_CfprProcDoerInstanceId_Type=CfprManagedObjectId
_CfprProcDoerInstanceId_Object=MibTableColumn
cfprProcDoerInstanceId=_CfprProcDoerInstanceId_Object((1,3,6,1,4,1,9,9,826,1,65,1,1,1),_CfprProcDoerInstanceId_Type())
cfprProcDoerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprProcDoerInstanceId.setStatus(_A)
_CfprProcDoerDn_Type=CfprManagedObjectDn
_CfprProcDoerDn_Object=MibTableColumn
cfprProcDoerDn=_CfprProcDoerDn_Object((1,3,6,1,4,1,9,9,826,1,65,1,1,2),_CfprProcDoerDn_Type())
cfprProcDoerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcDoerDn.setStatus(_A)
_CfprProcDoerRn_Type=SnmpAdminString
_CfprProcDoerRn_Object=MibTableColumn
cfprProcDoerRn=_CfprProcDoerRn_Object((1,3,6,1,4,1,9,9,826,1,65,1,1,3),_CfprProcDoerRn_Type())
cfprProcDoerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcDoerRn.setStatus(_A)
_CfprProcDoerId_Type=Gauge32
_CfprProcDoerId_Object=MibTableColumn
cfprProcDoerId=_CfprProcDoerId_Object((1,3,6,1,4,1,9,9,826,1,65,1,1,4),_CfprProcDoerId_Type())
cfprProcDoerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcDoerId.setStatus(_A)
_CfprProcDoerName_Type=SnmpAdminString
_CfprProcDoerName_Object=MibTableColumn
cfprProcDoerName=_CfprProcDoerName_Object((1,3,6,1,4,1,9,9,826,1,65,1,1,5),_CfprProcDoerName_Type())
cfprProcDoerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcDoerName.setStatus(_A)
_CfprProcManagerTable_Object=MibTable
cfprProcManagerTable=_CfprProcManagerTable_Object((1,3,6,1,4,1,9,9,826,1,65,2))
if mibBuilder.loadTexts:cfprProcManagerTable.setStatus(_A)
_CfprProcManagerEntry_Object=MibTableRow
cfprProcManagerEntry=_CfprProcManagerEntry_Object((1,3,6,1,4,1,9,9,826,1,65,2,1))
cfprProcManagerEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprProcManagerEntry.setStatus(_A)
_CfprProcManagerInstanceId_Type=CfprManagedObjectId
_CfprProcManagerInstanceId_Object=MibTableColumn
cfprProcManagerInstanceId=_CfprProcManagerInstanceId_Object((1,3,6,1,4,1,9,9,826,1,65,2,1,1),_CfprProcManagerInstanceId_Type())
cfprProcManagerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprProcManagerInstanceId.setStatus(_A)
_CfprProcManagerDn_Type=CfprManagedObjectDn
_CfprProcManagerDn_Object=MibTableColumn
cfprProcManagerDn=_CfprProcManagerDn_Object((1,3,6,1,4,1,9,9,826,1,65,2,1,2),_CfprProcManagerDn_Type())
cfprProcManagerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcManagerDn.setStatus(_A)
_CfprProcManagerRn_Type=SnmpAdminString
_CfprProcManagerRn_Object=MibTableColumn
cfprProcManagerRn=_CfprProcManagerRn_Object((1,3,6,1,4,1,9,9,826,1,65,2,1,3),_CfprProcManagerRn_Type())
cfprProcManagerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcManagerRn.setStatus(_A)
_CfprProcPrtTable_Object=MibTable
cfprProcPrtTable=_CfprProcPrtTable_Object((1,3,6,1,4,1,9,9,826,1,65,3))
if mibBuilder.loadTexts:cfprProcPrtTable.setStatus(_A)
_CfprProcPrtEntry_Object=MibTableRow
cfprProcPrtEntry=_CfprProcPrtEntry_Object((1,3,6,1,4,1,9,9,826,1,65,3,1))
cfprProcPrtEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprProcPrtEntry.setStatus(_A)
_CfprProcPrtInstanceId_Type=CfprManagedObjectId
_CfprProcPrtInstanceId_Object=MibTableColumn
cfprProcPrtInstanceId=_CfprProcPrtInstanceId_Object((1,3,6,1,4,1,9,9,826,1,65,3,1,1),_CfprProcPrtInstanceId_Type())
cfprProcPrtInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprProcPrtInstanceId.setStatus(_A)
_CfprProcPrtDn_Type=CfprManagedObjectDn
_CfprProcPrtDn_Object=MibTableColumn
cfprProcPrtDn=_CfprProcPrtDn_Object((1,3,6,1,4,1,9,9,826,1,65,3,1,2),_CfprProcPrtDn_Type())
cfprProcPrtDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtDn.setStatus(_A)
_CfprProcPrtRn_Type=SnmpAdminString
_CfprProcPrtRn_Object=MibTableColumn
cfprProcPrtRn=_CfprProcPrtRn_Object((1,3,6,1,4,1,9,9,826,1,65,3,1,3),_CfprProcPrtRn_Type())
cfprProcPrtRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtRn.setStatus(_A)
_CfprProcPrtId_Type=Gauge32
_CfprProcPrtId_Object=MibTableColumn
cfprProcPrtId=_CfprProcPrtId_Object((1,3,6,1,4,1,9,9,826,1,65,3,1,4),_CfprProcPrtId_Type())
cfprProcPrtId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtId.setStatus(_A)
_CfprProcPrtName_Type=SnmpAdminString
_CfprProcPrtName_Object=MibTableColumn
cfprProcPrtName=_CfprProcPrtName_Object((1,3,6,1,4,1,9,9,826,1,65,3,1,5),_CfprProcPrtName_Type())
cfprProcPrtName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtName.setStatus(_A)
_CfprProcPrtCountsTable_Object=MibTable
cfprProcPrtCountsTable=_CfprProcPrtCountsTable_Object((1,3,6,1,4,1,9,9,826,1,65,4))
if mibBuilder.loadTexts:cfprProcPrtCountsTable.setStatus(_A)
_CfprProcPrtCountsEntry_Object=MibTableRow
cfprProcPrtCountsEntry=_CfprProcPrtCountsEntry_Object((1,3,6,1,4,1,9,9,826,1,65,4,1))
cfprProcPrtCountsEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprProcPrtCountsEntry.setStatus(_A)
_CfprProcPrtCountsInstanceId_Type=CfprManagedObjectId
_CfprProcPrtCountsInstanceId_Object=MibTableColumn
cfprProcPrtCountsInstanceId=_CfprProcPrtCountsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,65,4,1,1),_CfprProcPrtCountsInstanceId_Type())
cfprProcPrtCountsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprProcPrtCountsInstanceId.setStatus(_A)
_CfprProcPrtCountsDn_Type=CfprManagedObjectDn
_CfprProcPrtCountsDn_Object=MibTableColumn
cfprProcPrtCountsDn=_CfprProcPrtCountsDn_Object((1,3,6,1,4,1,9,9,826,1,65,4,1,2),_CfprProcPrtCountsDn_Type())
cfprProcPrtCountsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtCountsDn.setStatus(_A)
_CfprProcPrtCountsRn_Type=SnmpAdminString
_CfprProcPrtCountsRn_Object=MibTableColumn
cfprProcPrtCountsRn=_CfprProcPrtCountsRn_Object((1,3,6,1,4,1,9,9,826,1,65,4,1,3),_CfprProcPrtCountsRn_Type())
cfprProcPrtCountsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtCountsRn.setStatus(_A)
_CfprProcPrtCountsCachenospc_Type=Gauge32
_CfprProcPrtCountsCachenospc_Object=MibTableColumn
cfprProcPrtCountsCachenospc=_CfprProcPrtCountsCachenospc_Object((1,3,6,1,4,1,9,9,826,1,65,4,1,4),_CfprProcPrtCountsCachenospc_Type())
cfprProcPrtCountsCachenospc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtCountsCachenospc.setStatus(_A)
_CfprProcPrtCountsDbtxs_Type=Gauge32
_CfprProcPrtCountsDbtxs_Object=MibTableColumn
cfprProcPrtCountsDbtxs=_CfprProcPrtCountsDbtxs_Object((1,3,6,1,4,1,9,9,826,1,65,4,1,5),_CfprProcPrtCountsDbtxs_Type())
cfprProcPrtCountsDbtxs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtCountsDbtxs.setStatus(_A)
_CfprProcPrtCountsLargetxs_Type=Gauge32
_CfprProcPrtCountsLargetxs_Object=MibTableColumn
cfprProcPrtCountsLargetxs=_CfprProcPrtCountsLargetxs_Object((1,3,6,1,4,1,9,9,826,1,65,4,1,6),_CfprProcPrtCountsLargetxs_Type())
cfprProcPrtCountsLargetxs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtCountsLargetxs.setStatus(_A)
_CfprProcPrtCountsPersistTime_Type=Unsigned64
_CfprProcPrtCountsPersistTime_Object=MibTableColumn
cfprProcPrtCountsPersistTime=_CfprProcPrtCountsPersistTime_Object((1,3,6,1,4,1,9,9,826,1,65,4,1,7),_CfprProcPrtCountsPersistTime_Type())
cfprProcPrtCountsPersistTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtCountsPersistTime.setStatus(_A)
_CfprProcPrtCountsTotal_Type=Gauge32
_CfprProcPrtCountsTotal_Object=MibTableColumn
cfprProcPrtCountsTotal=_CfprProcPrtCountsTotal_Object((1,3,6,1,4,1,9,9,826,1,65,4,1,8),_CfprProcPrtCountsTotal_Type())
cfprProcPrtCountsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcPrtCountsTotal.setStatus(_A)
_CfprProcStimulusCountsTable_Object=MibTable
cfprProcStimulusCountsTable=_CfprProcStimulusCountsTable_Object((1,3,6,1,4,1,9,9,826,1,65,5))
if mibBuilder.loadTexts:cfprProcStimulusCountsTable.setStatus(_A)
_CfprProcStimulusCountsEntry_Object=MibTableRow
cfprProcStimulusCountsEntry=_CfprProcStimulusCountsEntry_Object((1,3,6,1,4,1,9,9,826,1,65,5,1))
cfprProcStimulusCountsEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprProcStimulusCountsEntry.setStatus(_A)
_CfprProcStimulusCountsInstanceId_Type=CfprManagedObjectId
_CfprProcStimulusCountsInstanceId_Object=MibTableColumn
cfprProcStimulusCountsInstanceId=_CfprProcStimulusCountsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,1),_CfprProcStimulusCountsInstanceId_Type())
cfprProcStimulusCountsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprProcStimulusCountsInstanceId.setStatus(_A)
_CfprProcStimulusCountsDn_Type=CfprManagedObjectDn
_CfprProcStimulusCountsDn_Object=MibTableColumn
cfprProcStimulusCountsDn=_CfprProcStimulusCountsDn_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,2),_CfprProcStimulusCountsDn_Type())
cfprProcStimulusCountsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcStimulusCountsDn.setStatus(_A)
_CfprProcStimulusCountsRn_Type=SnmpAdminString
_CfprProcStimulusCountsRn_Object=MibTableColumn
cfprProcStimulusCountsRn=_CfprProcStimulusCountsRn_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,3),_CfprProcStimulusCountsRn_Type())
cfprProcStimulusCountsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcStimulusCountsRn.setStatus(_A)
_CfprProcStimulusCountsAdminState_Type=CfprProcStatAdminState
_CfprProcStimulusCountsAdminState_Object=MibTableColumn
cfprProcStimulusCountsAdminState=_CfprProcStimulusCountsAdminState_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,4),_CfprProcStimulusCountsAdminState_Type())
cfprProcStimulusCountsAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcStimulusCountsAdminState.setStatus(_A)
_CfprProcStimulusCountsBulked_Type=Gauge32
_CfprProcStimulusCountsBulked_Object=MibTableColumn
cfprProcStimulusCountsBulked=_CfprProcStimulusCountsBulked_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,5),_CfprProcStimulusCountsBulked_Type())
cfprProcStimulusCountsBulked.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcStimulusCountsBulked.setStatus(_A)
_CfprProcStimulusCountsFailed_Type=Gauge32
_CfprProcStimulusCountsFailed_Object=MibTableColumn
cfprProcStimulusCountsFailed=_CfprProcStimulusCountsFailed_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,6),_CfprProcStimulusCountsFailed_Type())
cfprProcStimulusCountsFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcStimulusCountsFailed.setStatus(_A)
_CfprProcStimulusCountsRetried_Type=Gauge32
_CfprProcStimulusCountsRetried_Object=MibTableColumn
cfprProcStimulusCountsRetried=_CfprProcStimulusCountsRetried_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,7),_CfprProcStimulusCountsRetried_Type())
cfprProcStimulusCountsRetried.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcStimulusCountsRetried.setStatus(_A)
_CfprProcStimulusCountsSingleton_Type=Gauge32
_CfprProcStimulusCountsSingleton_Object=MibTableColumn
cfprProcStimulusCountsSingleton=_CfprProcStimulusCountsSingleton_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,8),_CfprProcStimulusCountsSingleton_Type())
cfprProcStimulusCountsSingleton.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcStimulusCountsSingleton.setStatus(_A)
_CfprProcStimulusCountsSuccessfull_Type=Gauge32
_CfprProcStimulusCountsSuccessfull_Object=MibTableColumn
cfprProcStimulusCountsSuccessfull=_CfprProcStimulusCountsSuccessfull_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,9),_CfprProcStimulusCountsSuccessfull_Type())
cfprProcStimulusCountsSuccessfull.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcStimulusCountsSuccessfull.setStatus(_A)
_CfprProcStimulusCountsTotal_Type=Gauge32
_CfprProcStimulusCountsTotal_Object=MibTableColumn
cfprProcStimulusCountsTotal=_CfprProcStimulusCountsTotal_Object((1,3,6,1,4,1,9,9,826,1,65,5,1,10),_CfprProcStimulusCountsTotal_Type())
cfprProcStimulusCountsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcStimulusCountsTotal.setStatus(_A)
_CfprProcSvcTable_Object=MibTable
cfprProcSvcTable=_CfprProcSvcTable_Object((1,3,6,1,4,1,9,9,826,1,65,6))
if mibBuilder.loadTexts:cfprProcSvcTable.setStatus(_A)
_CfprProcSvcEntry_Object=MibTableRow
cfprProcSvcEntry=_CfprProcSvcEntry_Object((1,3,6,1,4,1,9,9,826,1,65,6,1))
cfprProcSvcEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprProcSvcEntry.setStatus(_A)
_CfprProcSvcInstanceId_Type=CfprManagedObjectId
_CfprProcSvcInstanceId_Object=MibTableColumn
cfprProcSvcInstanceId=_CfprProcSvcInstanceId_Object((1,3,6,1,4,1,9,9,826,1,65,6,1,1),_CfprProcSvcInstanceId_Type())
cfprProcSvcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprProcSvcInstanceId.setStatus(_A)
_CfprProcSvcDn_Type=CfprManagedObjectDn
_CfprProcSvcDn_Object=MibTableColumn
cfprProcSvcDn=_CfprProcSvcDn_Object((1,3,6,1,4,1,9,9,826,1,65,6,1,2),_CfprProcSvcDn_Type())
cfprProcSvcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcSvcDn.setStatus(_A)
_CfprProcSvcRn_Type=SnmpAdminString
_CfprProcSvcRn_Object=MibTableColumn
cfprProcSvcRn=_CfprProcSvcRn_Object((1,3,6,1,4,1,9,9,826,1,65,6,1,3),_CfprProcSvcRn_Type())
cfprProcSvcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcSvcRn.setStatus(_A)
_CfprProcSvcId_Type=Gauge32
_CfprProcSvcId_Object=MibTableColumn
cfprProcSvcId=_CfprProcSvcId_Object((1,3,6,1,4,1,9,9,826,1,65,6,1,4),_CfprProcSvcId_Type())
cfprProcSvcId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcSvcId.setStatus(_A)
_CfprProcSvcName_Type=SnmpAdminString
_CfprProcSvcName_Object=MibTableColumn
cfprProcSvcName=_CfprProcSvcName_Object((1,3,6,1,4,1,9,9,826,1,65,6,1,5),_CfprProcSvcName_Type())
cfprProcSvcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcSvcName.setStatus(_A)
_CfprProcTxCountsTable_Object=MibTable
cfprProcTxCountsTable=_CfprProcTxCountsTable_Object((1,3,6,1,4,1,9,9,826,1,65,7))
if mibBuilder.loadTexts:cfprProcTxCountsTable.setStatus(_A)
_CfprProcTxCountsEntry_Object=MibTableRow
cfprProcTxCountsEntry=_CfprProcTxCountsEntry_Object((1,3,6,1,4,1,9,9,826,1,65,7,1))
cfprProcTxCountsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprProcTxCountsEntry.setStatus(_A)
_CfprProcTxCountsInstanceId_Type=CfprManagedObjectId
_CfprProcTxCountsInstanceId_Object=MibTableColumn
cfprProcTxCountsInstanceId=_CfprProcTxCountsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,1),_CfprProcTxCountsInstanceId_Type())
cfprProcTxCountsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprProcTxCountsInstanceId.setStatus(_A)
_CfprProcTxCountsDn_Type=CfprManagedObjectDn
_CfprProcTxCountsDn_Object=MibTableColumn
cfprProcTxCountsDn=_CfprProcTxCountsDn_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,2),_CfprProcTxCountsDn_Type())
cfprProcTxCountsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcTxCountsDn.setStatus(_A)
_CfprProcTxCountsRn_Type=SnmpAdminString
_CfprProcTxCountsRn_Object=MibTableColumn
cfprProcTxCountsRn=_CfprProcTxCountsRn_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,3),_CfprProcTxCountsRn_Type())
cfprProcTxCountsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcTxCountsRn.setStatus(_A)
_CfprProcTxCountsAdminState_Type=CfprProcStatAdminState
_CfprProcTxCountsAdminState_Object=MibTableColumn
cfprProcTxCountsAdminState=_CfprProcTxCountsAdminState_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,4),_CfprProcTxCountsAdminState_Type())
cfprProcTxCountsAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcTxCountsAdminState.setStatus(_A)
_CfprProcTxCountsBulked_Type=Gauge32
_CfprProcTxCountsBulked_Object=MibTableColumn
cfprProcTxCountsBulked=_CfprProcTxCountsBulked_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,5),_CfprProcTxCountsBulked_Type())
cfprProcTxCountsBulked.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcTxCountsBulked.setStatus(_A)
_CfprProcTxCountsFailed_Type=Gauge32
_CfprProcTxCountsFailed_Object=MibTableColumn
cfprProcTxCountsFailed=_CfprProcTxCountsFailed_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,6),_CfprProcTxCountsFailed_Type())
cfprProcTxCountsFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcTxCountsFailed.setStatus(_A)
_CfprProcTxCountsRetried_Type=Gauge32
_CfprProcTxCountsRetried_Object=MibTableColumn
cfprProcTxCountsRetried=_CfprProcTxCountsRetried_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,7),_CfprProcTxCountsRetried_Type())
cfprProcTxCountsRetried.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcTxCountsRetried.setStatus(_A)
_CfprProcTxCountsSingleton_Type=Gauge32
_CfprProcTxCountsSingleton_Object=MibTableColumn
cfprProcTxCountsSingleton=_CfprProcTxCountsSingleton_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,8),_CfprProcTxCountsSingleton_Type())
cfprProcTxCountsSingleton.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcTxCountsSingleton.setStatus(_A)
_CfprProcTxCountsSuccessfull_Type=Gauge32
_CfprProcTxCountsSuccessfull_Object=MibTableColumn
cfprProcTxCountsSuccessfull=_CfprProcTxCountsSuccessfull_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,9),_CfprProcTxCountsSuccessfull_Type())
cfprProcTxCountsSuccessfull.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcTxCountsSuccessfull.setStatus(_A)
_CfprProcTxCountsTotal_Type=Gauge32
_CfprProcTxCountsTotal_Object=MibTableColumn
cfprProcTxCountsTotal=_CfprProcTxCountsTotal_Object((1,3,6,1,4,1,9,9,826,1,65,7,1,10),_CfprProcTxCountsTotal_Type())
cfprProcTxCountsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprProcTxCountsTotal.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprProcObjects':cfprProcObjects,'cfprProcDoerTable':cfprProcDoerTable,'cfprProcDoerEntry':cfprProcDoerEntry,_E:cfprProcDoerInstanceId,'cfprProcDoerDn':cfprProcDoerDn,'cfprProcDoerRn':cfprProcDoerRn,'cfprProcDoerId':cfprProcDoerId,'cfprProcDoerName':cfprProcDoerName,'cfprProcManagerTable':cfprProcManagerTable,'cfprProcManagerEntry':cfprProcManagerEntry,_F:cfprProcManagerInstanceId,'cfprProcManagerDn':cfprProcManagerDn,'cfprProcManagerRn':cfprProcManagerRn,'cfprProcPrtTable':cfprProcPrtTable,'cfprProcPrtEntry':cfprProcPrtEntry,_G:cfprProcPrtInstanceId,'cfprProcPrtDn':cfprProcPrtDn,'cfprProcPrtRn':cfprProcPrtRn,'cfprProcPrtId':cfprProcPrtId,'cfprProcPrtName':cfprProcPrtName,'cfprProcPrtCountsTable':cfprProcPrtCountsTable,'cfprProcPrtCountsEntry':cfprProcPrtCountsEntry,_H:cfprProcPrtCountsInstanceId,'cfprProcPrtCountsDn':cfprProcPrtCountsDn,'cfprProcPrtCountsRn':cfprProcPrtCountsRn,'cfprProcPrtCountsCachenospc':cfprProcPrtCountsCachenospc,'cfprProcPrtCountsDbtxs':cfprProcPrtCountsDbtxs,'cfprProcPrtCountsLargetxs':cfprProcPrtCountsLargetxs,'cfprProcPrtCountsPersistTime':cfprProcPrtCountsPersistTime,'cfprProcPrtCountsTotal':cfprProcPrtCountsTotal,'cfprProcStimulusCountsTable':cfprProcStimulusCountsTable,'cfprProcStimulusCountsEntry':cfprProcStimulusCountsEntry,_I:cfprProcStimulusCountsInstanceId,'cfprProcStimulusCountsDn':cfprProcStimulusCountsDn,'cfprProcStimulusCountsRn':cfprProcStimulusCountsRn,'cfprProcStimulusCountsAdminState':cfprProcStimulusCountsAdminState,'cfprProcStimulusCountsBulked':cfprProcStimulusCountsBulked,'cfprProcStimulusCountsFailed':cfprProcStimulusCountsFailed,'cfprProcStimulusCountsRetried':cfprProcStimulusCountsRetried,'cfprProcStimulusCountsSingleton':cfprProcStimulusCountsSingleton,'cfprProcStimulusCountsSuccessfull':cfprProcStimulusCountsSuccessfull,'cfprProcStimulusCountsTotal':cfprProcStimulusCountsTotal,'cfprProcSvcTable':cfprProcSvcTable,'cfprProcSvcEntry':cfprProcSvcEntry,_J:cfprProcSvcInstanceId,'cfprProcSvcDn':cfprProcSvcDn,'cfprProcSvcRn':cfprProcSvcRn,'cfprProcSvcId':cfprProcSvcId,'cfprProcSvcName':cfprProcSvcName,'cfprProcTxCountsTable':cfprProcTxCountsTable,'cfprProcTxCountsEntry':cfprProcTxCountsEntry,_K:cfprProcTxCountsInstanceId,'cfprProcTxCountsDn':cfprProcTxCountsDn,'cfprProcTxCountsRn':cfprProcTxCountsRn,'cfprProcTxCountsAdminState':cfprProcTxCountsAdminState,'cfprProcTxCountsBulked':cfprProcTxCountsBulked,'cfprProcTxCountsFailed':cfprProcTxCountsFailed,'cfprProcTxCountsRetried':cfprProcTxCountsRetried,'cfprProcTxCountsSingleton':cfprProcTxCountsSingleton,'cfprProcTxCountsSuccessfull':cfprProcTxCountsSuccessfull,'cfprProcTxCountsTotal':cfprProcTxCountsTotal})