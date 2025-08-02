_D='cucsSecurityUnitInstanceId'
_C='CISCO-UNIFIED-COMPUTING-SECURITY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsEquipmentOperability,CucsEquipmentPowerState,CucsEquipmentPresence,CucsEquipmentSensorThresholdStatus,CucsSecurityUnitId=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsEquipmentOperability','CucsEquipmentPowerState','CucsEquipmentPresence','CucsEquipmentSensorThresholdStatus','CucsSecurityUnitId')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsSecurityObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,88))
_CucsSecurityUnitTable_Object=MibTable
cucsSecurityUnitTable=_CucsSecurityUnitTable_Object((1,3,6,1,4,1,9,9,719,1,88,1))
if mibBuilder.loadTexts:cucsSecurityUnitTable.setStatus(_A)
_CucsSecurityUnitEntry_Object=MibTableRow
cucsSecurityUnitEntry=_CucsSecurityUnitEntry_Object((1,3,6,1,4,1,9,9,719,1,88,1,1))
cucsSecurityUnitEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsSecurityUnitEntry.setStatus(_A)
_CucsSecurityUnitInstanceId_Type=CucsManagedObjectId
_CucsSecurityUnitInstanceId_Object=MibTableColumn
cucsSecurityUnitInstanceId=_CucsSecurityUnitInstanceId_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,1),_CucsSecurityUnitInstanceId_Type())
cucsSecurityUnitInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cucsSecurityUnitInstanceId.setStatus(_A)
_CucsSecurityUnitDn_Type=CucsManagedObjectDn
_CucsSecurityUnitDn_Object=MibTableColumn
cucsSecurityUnitDn=_CucsSecurityUnitDn_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,2),_CucsSecurityUnitDn_Type())
cucsSecurityUnitDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitDn.setStatus(_A)
_CucsSecurityUnitRn_Type=SnmpAdminString
_CucsSecurityUnitRn_Object=MibTableColumn
cucsSecurityUnitRn=_CucsSecurityUnitRn_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,3),_CucsSecurityUnitRn_Type())
cucsSecurityUnitRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitRn.setStatus(_A)
_CucsSecurityUnitId_Type=CucsSecurityUnitId
_CucsSecurityUnitId_Object=MibTableColumn
cucsSecurityUnitId=_CucsSecurityUnitId_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,4),_CucsSecurityUnitId_Type())
cucsSecurityUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitId.setStatus(_A)
_CucsSecurityUnitLocationDn_Type=SnmpAdminString
_CucsSecurityUnitLocationDn_Object=MibTableColumn
cucsSecurityUnitLocationDn=_CucsSecurityUnitLocationDn_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,5),_CucsSecurityUnitLocationDn_Type())
cucsSecurityUnitLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitLocationDn.setStatus(_A)
_CucsSecurityUnitModel_Type=SnmpAdminString
_CucsSecurityUnitModel_Object=MibTableColumn
cucsSecurityUnitModel=_CucsSecurityUnitModel_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,6),_CucsSecurityUnitModel_Type())
cucsSecurityUnitModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitModel.setStatus(_A)
_CucsSecurityUnitOperQualifierReason_Type=SnmpAdminString
_CucsSecurityUnitOperQualifierReason_Object=MibTableColumn
cucsSecurityUnitOperQualifierReason=_CucsSecurityUnitOperQualifierReason_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,7),_CucsSecurityUnitOperQualifierReason_Type())
cucsSecurityUnitOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitOperQualifierReason.setStatus(_A)
_CucsSecurityUnitOperState_Type=CucsEquipmentOperability
_CucsSecurityUnitOperState_Object=MibTableColumn
cucsSecurityUnitOperState=_CucsSecurityUnitOperState_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,8),_CucsSecurityUnitOperState_Type())
cucsSecurityUnitOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitOperState.setStatus(_A)
_CucsSecurityUnitOperability_Type=CucsEquipmentOperability
_CucsSecurityUnitOperability_Object=MibTableColumn
cucsSecurityUnitOperability=_CucsSecurityUnitOperability_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,9),_CucsSecurityUnitOperability_Type())
cucsSecurityUnitOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitOperability.setStatus(_A)
_CucsSecurityUnitPartNumber_Type=SnmpAdminString
_CucsSecurityUnitPartNumber_Object=MibTableColumn
cucsSecurityUnitPartNumber=_CucsSecurityUnitPartNumber_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,10),_CucsSecurityUnitPartNumber_Type())
cucsSecurityUnitPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitPartNumber.setStatus(_A)
_CucsSecurityUnitPciAddr_Type=SnmpAdminString
_CucsSecurityUnitPciAddr_Object=MibTableColumn
cucsSecurityUnitPciAddr=_CucsSecurityUnitPciAddr_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,11),_CucsSecurityUnitPciAddr_Type())
cucsSecurityUnitPciAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitPciAddr.setStatus(_A)
_CucsSecurityUnitPciSlot_Type=SnmpAdminString
_CucsSecurityUnitPciSlot_Object=MibTableColumn
cucsSecurityUnitPciSlot=_CucsSecurityUnitPciSlot_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,12),_CucsSecurityUnitPciSlot_Type())
cucsSecurityUnitPciSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitPciSlot.setStatus(_A)
_CucsSecurityUnitPerf_Type=CucsEquipmentSensorThresholdStatus
_CucsSecurityUnitPerf_Object=MibTableColumn
cucsSecurityUnitPerf=_CucsSecurityUnitPerf_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,13),_CucsSecurityUnitPerf_Type())
cucsSecurityUnitPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitPerf.setStatus(_A)
_CucsSecurityUnitPower_Type=CucsEquipmentPowerState
_CucsSecurityUnitPower_Object=MibTableColumn
cucsSecurityUnitPower=_CucsSecurityUnitPower_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,14),_CucsSecurityUnitPower_Type())
cucsSecurityUnitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitPower.setStatus(_A)
_CucsSecurityUnitPresence_Type=CucsEquipmentPresence
_CucsSecurityUnitPresence_Object=MibTableColumn
cucsSecurityUnitPresence=_CucsSecurityUnitPresence_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,15),_CucsSecurityUnitPresence_Type())
cucsSecurityUnitPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitPresence.setStatus(_A)
_CucsSecurityUnitRevision_Type=SnmpAdminString
_CucsSecurityUnitRevision_Object=MibTableColumn
cucsSecurityUnitRevision=_CucsSecurityUnitRevision_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,16),_CucsSecurityUnitRevision_Type())
cucsSecurityUnitRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitRevision.setStatus(_A)
_CucsSecurityUnitSerial_Type=SnmpAdminString
_CucsSecurityUnitSerial_Object=MibTableColumn
cucsSecurityUnitSerial=_CucsSecurityUnitSerial_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,17),_CucsSecurityUnitSerial_Type())
cucsSecurityUnitSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitSerial.setStatus(_A)
_CucsSecurityUnitThermal_Type=CucsEquipmentSensorThresholdStatus
_CucsSecurityUnitThermal_Object=MibTableColumn
cucsSecurityUnitThermal=_CucsSecurityUnitThermal_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,18),_CucsSecurityUnitThermal_Type())
cucsSecurityUnitThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitThermal.setStatus(_A)
_CucsSecurityUnitVendor_Type=SnmpAdminString
_CucsSecurityUnitVendor_Object=MibTableColumn
cucsSecurityUnitVendor=_CucsSecurityUnitVendor_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,19),_CucsSecurityUnitVendor_Type())
cucsSecurityUnitVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitVendor.setStatus(_A)
_CucsSecurityUnitVid_Type=SnmpAdminString
_CucsSecurityUnitVid_Object=MibTableColumn
cucsSecurityUnitVid=_CucsSecurityUnitVid_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,20),_CucsSecurityUnitVid_Type())
cucsSecurityUnitVid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitVid.setStatus(_A)
_CucsSecurityUnitVoltage_Type=CucsEquipmentSensorThresholdStatus
_CucsSecurityUnitVoltage_Object=MibTableColumn
cucsSecurityUnitVoltage=_CucsSecurityUnitVoltage_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,21),_CucsSecurityUnitVoltage_Type())
cucsSecurityUnitVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitVoltage.setStatus(_A)
_CucsSecurityUnitAssetTag_Type=SnmpAdminString
_CucsSecurityUnitAssetTag_Object=MibTableColumn
cucsSecurityUnitAssetTag=_CucsSecurityUnitAssetTag_Object((1,3,6,1,4,1,9,9,719,1,88,1,1,22),_CucsSecurityUnitAssetTag_Type())
cucsSecurityUnitAssetTag.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsSecurityUnitAssetTag.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsSecurityObjects':cucsSecurityObjects,'cucsSecurityUnitTable':cucsSecurityUnitTable,'cucsSecurityUnitEntry':cucsSecurityUnitEntry,_D:cucsSecurityUnitInstanceId,'cucsSecurityUnitDn':cucsSecurityUnitDn,'cucsSecurityUnitRn':cucsSecurityUnitRn,'cucsSecurityUnitId':cucsSecurityUnitId,'cucsSecurityUnitLocationDn':cucsSecurityUnitLocationDn,'cucsSecurityUnitModel':cucsSecurityUnitModel,'cucsSecurityUnitOperQualifierReason':cucsSecurityUnitOperQualifierReason,'cucsSecurityUnitOperState':cucsSecurityUnitOperState,'cucsSecurityUnitOperability':cucsSecurityUnitOperability,'cucsSecurityUnitPartNumber':cucsSecurityUnitPartNumber,'cucsSecurityUnitPciAddr':cucsSecurityUnitPciAddr,'cucsSecurityUnitPciSlot':cucsSecurityUnitPciSlot,'cucsSecurityUnitPerf':cucsSecurityUnitPerf,'cucsSecurityUnitPower':cucsSecurityUnitPower,'cucsSecurityUnitPresence':cucsSecurityUnitPresence,'cucsSecurityUnitRevision':cucsSecurityUnitRevision,'cucsSecurityUnitSerial':cucsSecurityUnitSerial,'cucsSecurityUnitThermal':cucsSecurityUnitThermal,'cucsSecurityUnitVendor':cucsSecurityUnitVendor,'cucsSecurityUnitVid':cucsSecurityUnitVid,'cucsSecurityUnitVoltage':cucsSecurityUnitVoltage,'cucsSecurityUnitAssetTag':cucsSecurityUnitAssetTag})