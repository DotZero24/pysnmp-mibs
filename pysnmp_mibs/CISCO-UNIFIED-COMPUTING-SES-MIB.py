_F='cucsSesEnclosureInstanceId'
_E='not-accessible'
_D='cucsSesDiskSlotEpInstanceId'
_C='CISCO-UNIFIED-COMPUTING-SES-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsFsmLifecycle,CucsSesScsiDriveStatus=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsFsmLifecycle','CucsSesScsiDriveStatus')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsSesObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,80))
_CucsSesDiskSlotEpTable_Object=MibTable
cucsSesDiskSlotEpTable=_CucsSesDiskSlotEpTable_Object((1,3,6,1,4,1,9,9,719,1,80,1))
if mibBuilder.loadTexts:cucsSesDiskSlotEpTable.setStatus(_A)
_CucsSesDiskSlotEpEntry_Object=MibTableRow
cucsSesDiskSlotEpEntry=_CucsSesDiskSlotEpEntry_Object((1,3,6,1,4,1,9,9,719,1,80,1,1))
cucsSesDiskSlotEpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsSesDiskSlotEpEntry.setStatus(_A)
_CucsSesDiskSlotEpInstanceId_Type=CucsManagedObjectId
_CucsSesDiskSlotEpInstanceId_Object=MibTableColumn
cucsSesDiskSlotEpInstanceId=_CucsSesDiskSlotEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,1),_CucsSesDiskSlotEpInstanceId_Type())
cucsSesDiskSlotEpInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsSesDiskSlotEpInstanceId.setStatus(_A)
_CucsSesDiskSlotEpDn_Type=CucsManagedObjectDn
_CucsSesDiskSlotEpDn_Object=MibTableColumn
cucsSesDiskSlotEpDn=_CucsSesDiskSlotEpDn_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,2),_CucsSesDiskSlotEpDn_Type())
cucsSesDiskSlotEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpDn.setStatus(_A)
_CucsSesDiskSlotEpRn_Type=SnmpAdminString
_CucsSesDiskSlotEpRn_Object=MibTableColumn
cucsSesDiskSlotEpRn=_CucsSesDiskSlotEpRn_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,3),_CucsSesDiskSlotEpRn_Type())
cucsSesDiskSlotEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpRn.setStatus(_A)
_CucsSesDiskSlotEpEncId_Type=Gauge32
_CucsSesDiskSlotEpEncId_Object=MibTableColumn
cucsSesDiskSlotEpEncId=_CucsSesDiskSlotEpEncId_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,4),_CucsSesDiskSlotEpEncId_Type())
cucsSesDiskSlotEpEncId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpEncId.setStatus(_A)
_CucsSesDiskSlotEpId_Type=Gauge32
_CucsSesDiskSlotEpId_Object=MibTableColumn
cucsSesDiskSlotEpId=_CucsSesDiskSlotEpId_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,5),_CucsSesDiskSlotEpId_Type())
cucsSesDiskSlotEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpId.setStatus(_A)
_CucsSesDiskSlotEpSlotDn_Type=SnmpAdminString
_CucsSesDiskSlotEpSlotDn_Object=MibTableColumn
cucsSesDiskSlotEpSlotDn=_CucsSesDiskSlotEpSlotDn_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,6),_CucsSesDiskSlotEpSlotDn_Type())
cucsSesDiskSlotEpSlotDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpSlotDn.setStatus(_A)
_CucsSesDiskSlotEpDiskDn_Type=SnmpAdminString
_CucsSesDiskSlotEpDiskDn_Object=MibTableColumn
cucsSesDiskSlotEpDiskDn=_CucsSesDiskSlotEpDiskDn_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,7),_CucsSesDiskSlotEpDiskDn_Type())
cucsSesDiskSlotEpDiskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpDiskDn.setStatus(_A)
_CucsSesDiskSlotEpDiskPresent_Type=TruthValue
_CucsSesDiskSlotEpDiskPresent_Object=MibTableColumn
cucsSesDiskSlotEpDiskPresent=_CucsSesDiskSlotEpDiskPresent_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,8),_CucsSesDiskSlotEpDiskPresent_Type())
cucsSesDiskSlotEpDiskPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpDiskPresent.setStatus(_A)
_CucsSesDiskSlotEpLc_Type=CucsFsmLifecycle
_CucsSesDiskSlotEpLc_Object=MibTableColumn
cucsSesDiskSlotEpLc=_CucsSesDiskSlotEpLc_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,9),_CucsSesDiskSlotEpLc_Type())
cucsSesDiskSlotEpLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpLc.setStatus(_A)
_CucsSesDiskSlotEpModel_Type=SnmpAdminString
_CucsSesDiskSlotEpModel_Object=MibTableColumn
cucsSesDiskSlotEpModel=_CucsSesDiskSlotEpModel_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,10),_CucsSesDiskSlotEpModel_Type())
cucsSesDiskSlotEpModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpModel.setStatus(_A)
_CucsSesDiskSlotEpRevision_Type=SnmpAdminString
_CucsSesDiskSlotEpRevision_Object=MibTableColumn
cucsSesDiskSlotEpRevision=_CucsSesDiskSlotEpRevision_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,11),_CucsSesDiskSlotEpRevision_Type())
cucsSesDiskSlotEpRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpRevision.setStatus(_A)
_CucsSesDiskSlotEpScsiDiskState_Type=CucsSesScsiDriveStatus
_CucsSesDiskSlotEpScsiDiskState_Object=MibTableColumn
cucsSesDiskSlotEpScsiDiskState=_CucsSesDiskSlotEpScsiDiskState_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,12),_CucsSesDiskSlotEpScsiDiskState_Type())
cucsSesDiskSlotEpScsiDiskState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpScsiDiskState.setStatus(_A)
_CucsSesDiskSlotEpSerial_Type=SnmpAdminString
_CucsSesDiskSlotEpSerial_Object=MibTableColumn
cucsSesDiskSlotEpSerial=_CucsSesDiskSlotEpSerial_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,13),_CucsSesDiskSlotEpSerial_Type())
cucsSesDiskSlotEpSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpSerial.setStatus(_A)
_CucsSesDiskSlotEpVendor_Type=SnmpAdminString
_CucsSesDiskSlotEpVendor_Object=MibTableColumn
cucsSesDiskSlotEpVendor=_CucsSesDiskSlotEpVendor_Object((1,3,6,1,4,1,9,9,719,1,80,1,1,14),_CucsSesDiskSlotEpVendor_Type())
cucsSesDiskSlotEpVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesDiskSlotEpVendor.setStatus(_A)
_CucsSesEnclosureTable_Object=MibTable
cucsSesEnclosureTable=_CucsSesEnclosureTable_Object((1,3,6,1,4,1,9,9,719,1,80,2))
if mibBuilder.loadTexts:cucsSesEnclosureTable.setStatus(_A)
_CucsSesEnclosureEntry_Object=MibTableRow
cucsSesEnclosureEntry=_CucsSesEnclosureEntry_Object((1,3,6,1,4,1,9,9,719,1,80,2,1))
cucsSesEnclosureEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsSesEnclosureEntry.setStatus(_A)
_CucsSesEnclosureInstanceId_Type=CucsManagedObjectId
_CucsSesEnclosureInstanceId_Object=MibTableColumn
cucsSesEnclosureInstanceId=_CucsSesEnclosureInstanceId_Object((1,3,6,1,4,1,9,9,719,1,80,2,1,1),_CucsSesEnclosureInstanceId_Type())
cucsSesEnclosureInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsSesEnclosureInstanceId.setStatus(_A)
_CucsSesEnclosureDn_Type=CucsManagedObjectDn
_CucsSesEnclosureDn_Object=MibTableColumn
cucsSesEnclosureDn=_CucsSesEnclosureDn_Object((1,3,6,1,4,1,9,9,719,1,80,2,1,2),_CucsSesEnclosureDn_Type())
cucsSesEnclosureDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesEnclosureDn.setStatus(_A)
_CucsSesEnclosureRn_Type=SnmpAdminString
_CucsSesEnclosureRn_Object=MibTableColumn
cucsSesEnclosureRn=_CucsSesEnclosureRn_Object((1,3,6,1,4,1,9,9,719,1,80,2,1,3),_CucsSesEnclosureRn_Type())
cucsSesEnclosureRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesEnclosureRn.setStatus(_A)
_CucsSesEnclosureDescr_Type=SnmpAdminString
_CucsSesEnclosureDescr_Object=MibTableColumn
cucsSesEnclosureDescr=_CucsSesEnclosureDescr_Object((1,3,6,1,4,1,9,9,719,1,80,2,1,4),_CucsSesEnclosureDescr_Type())
cucsSesEnclosureDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesEnclosureDescr.setStatus(_A)
_CucsSesEnclosureElid_Type=SnmpAdminString
_CucsSesEnclosureElid_Object=MibTableColumn
cucsSesEnclosureElid=_CucsSesEnclosureElid_Object((1,3,6,1,4,1,9,9,719,1,80,2,1,5),_CucsSesEnclosureElid_Type())
cucsSesEnclosureElid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesEnclosureElid.setStatus(_A)
_CucsSesEnclosureId_Type=Gauge32
_CucsSesEnclosureId_Object=MibTableColumn
cucsSesEnclosureId=_CucsSesEnclosureId_Object((1,3,6,1,4,1,9,9,719,1,80,2,1,6),_CucsSesEnclosureId_Type())
cucsSesEnclosureId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesEnclosureId.setStatus(_A)
_CucsSesEnclosureLc_Type=CucsFsmLifecycle
_CucsSesEnclosureLc_Object=MibTableColumn
cucsSesEnclosureLc=_CucsSesEnclosureLc_Object((1,3,6,1,4,1,9,9,719,1,80,2,1,7),_CucsSesEnclosureLc_Type())
cucsSesEnclosureLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSesEnclosureLc.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsSesObjects':cucsSesObjects,'cucsSesDiskSlotEpTable':cucsSesDiskSlotEpTable,'cucsSesDiskSlotEpEntry':cucsSesDiskSlotEpEntry,_D:cucsSesDiskSlotEpInstanceId,'cucsSesDiskSlotEpDn':cucsSesDiskSlotEpDn,'cucsSesDiskSlotEpRn':cucsSesDiskSlotEpRn,'cucsSesDiskSlotEpEncId':cucsSesDiskSlotEpEncId,'cucsSesDiskSlotEpId':cucsSesDiskSlotEpId,'cucsSesDiskSlotEpSlotDn':cucsSesDiskSlotEpSlotDn,'cucsSesDiskSlotEpDiskDn':cucsSesDiskSlotEpDiskDn,'cucsSesDiskSlotEpDiskPresent':cucsSesDiskSlotEpDiskPresent,'cucsSesDiskSlotEpLc':cucsSesDiskSlotEpLc,'cucsSesDiskSlotEpModel':cucsSesDiskSlotEpModel,'cucsSesDiskSlotEpRevision':cucsSesDiskSlotEpRevision,'cucsSesDiskSlotEpScsiDiskState':cucsSesDiskSlotEpScsiDiskState,'cucsSesDiskSlotEpSerial':cucsSesDiskSlotEpSerial,'cucsSesDiskSlotEpVendor':cucsSesDiskSlotEpVendor,'cucsSesEnclosureTable':cucsSesEnclosureTable,'cucsSesEnclosureEntry':cucsSesEnclosureEntry,_F:cucsSesEnclosureInstanceId,'cucsSesEnclosureDn':cucsSesEnclosureDn,'cucsSesEnclosureRn':cucsSesEnclosureRn,'cucsSesEnclosureDescr':cucsSesEnclosureDescr,'cucsSesEnclosureElid':cucsSesEnclosureElid,'cucsSesEnclosureId':cucsSesEnclosureId,'cucsSesEnclosureLc':cucsSesEnclosureLc})