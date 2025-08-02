_F='cucsPciEquipSlotInstanceId'
_E='not-accessible'
_D='cucsPciUnitInstanceId'
_C='CISCO-UNIFIED-COMPUTING-PCI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsEquipmentDiscoveryState,CucsEquipmentOperability,CucsEquipmentPowerState,CucsEquipmentPresence,CucsEquipmentSensorThresholdStatus,CucsPciEquipSlotId=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsEquipmentDiscoveryState','CucsEquipmentOperability','CucsEquipmentPowerState','CucsEquipmentPresence','CucsEquipmentSensorThresholdStatus','CucsPciEquipSlotId')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsPciObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,36))
_CucsPciUnitTable_Object=MibTable
cucsPciUnitTable=_CucsPciUnitTable_Object((1,3,6,1,4,1,9,9,719,1,36,1))
if mibBuilder.loadTexts:cucsPciUnitTable.setStatus(_A)
_CucsPciUnitEntry_Object=MibTableRow
cucsPciUnitEntry=_CucsPciUnitEntry_Object((1,3,6,1,4,1,9,9,719,1,36,1,1))
cucsPciUnitEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsPciUnitEntry.setStatus(_A)
_CucsPciUnitInstanceId_Type=CucsManagedObjectId
_CucsPciUnitInstanceId_Object=MibTableColumn
cucsPciUnitInstanceId=_CucsPciUnitInstanceId_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,1),_CucsPciUnitInstanceId_Type())
cucsPciUnitInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsPciUnitInstanceId.setStatus(_A)
_CucsPciUnitDn_Type=CucsManagedObjectDn
_CucsPciUnitDn_Object=MibTableColumn
cucsPciUnitDn=_CucsPciUnitDn_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,2),_CucsPciUnitDn_Type())
cucsPciUnitDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitDn.setStatus(_A)
_CucsPciUnitRn_Type=SnmpAdminString
_CucsPciUnitRn_Object=MibTableColumn
cucsPciUnitRn=_CucsPciUnitRn_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,3),_CucsPciUnitRn_Type())
cucsPciUnitRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitRn.setStatus(_A)
_CucsPciUnitId_Type=Gauge32
_CucsPciUnitId_Object=MibTableColumn
cucsPciUnitId=_CucsPciUnitId_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,4),_CucsPciUnitId_Type())
cucsPciUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitId.setStatus(_A)
_CucsPciUnitModel_Type=SnmpAdminString
_CucsPciUnitModel_Object=MibTableColumn
cucsPciUnitModel=_CucsPciUnitModel_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,5),_CucsPciUnitModel_Type())
cucsPciUnitModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitModel.setStatus(_A)
_CucsPciUnitOperState_Type=CucsEquipmentOperability
_CucsPciUnitOperState_Object=MibTableColumn
cucsPciUnitOperState=_CucsPciUnitOperState_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,6),_CucsPciUnitOperState_Type())
cucsPciUnitOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitOperState.setStatus(_A)
_CucsPciUnitOperability_Type=CucsEquipmentOperability
_CucsPciUnitOperability_Object=MibTableColumn
cucsPciUnitOperability=_CucsPciUnitOperability_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,7),_CucsPciUnitOperability_Type())
cucsPciUnitOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitOperability.setStatus(_A)
_CucsPciUnitPciAddr_Type=SnmpAdminString
_CucsPciUnitPciAddr_Object=MibTableColumn
cucsPciUnitPciAddr=_CucsPciUnitPciAddr_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,8),_CucsPciUnitPciAddr_Type())
cucsPciUnitPciAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitPciAddr.setStatus(_A)
_CucsPciUnitPciSlot_Type=SnmpAdminString
_CucsPciUnitPciSlot_Object=MibTableColumn
cucsPciUnitPciSlot=_CucsPciUnitPciSlot_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,9),_CucsPciUnitPciSlot_Type())
cucsPciUnitPciSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitPciSlot.setStatus(_A)
_CucsPciUnitPerf_Type=CucsEquipmentSensorThresholdStatus
_CucsPciUnitPerf_Object=MibTableColumn
cucsPciUnitPerf=_CucsPciUnitPerf_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,10),_CucsPciUnitPerf_Type())
cucsPciUnitPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitPerf.setStatus(_A)
_CucsPciUnitPower_Type=CucsEquipmentPowerState
_CucsPciUnitPower_Object=MibTableColumn
cucsPciUnitPower=_CucsPciUnitPower_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,11),_CucsPciUnitPower_Type())
cucsPciUnitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitPower.setStatus(_A)
_CucsPciUnitPresence_Type=CucsEquipmentPresence
_CucsPciUnitPresence_Object=MibTableColumn
cucsPciUnitPresence=_CucsPciUnitPresence_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,12),_CucsPciUnitPresence_Type())
cucsPciUnitPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitPresence.setStatus(_A)
_CucsPciUnitRevision_Type=SnmpAdminString
_CucsPciUnitRevision_Object=MibTableColumn
cucsPciUnitRevision=_CucsPciUnitRevision_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,13),_CucsPciUnitRevision_Type())
cucsPciUnitRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitRevision.setStatus(_A)
_CucsPciUnitSerial_Type=SnmpAdminString
_CucsPciUnitSerial_Object=MibTableColumn
cucsPciUnitSerial=_CucsPciUnitSerial_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,14),_CucsPciUnitSerial_Type())
cucsPciUnitSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitSerial.setStatus(_A)
_CucsPciUnitThermal_Type=CucsEquipmentSensorThresholdStatus
_CucsPciUnitThermal_Object=MibTableColumn
cucsPciUnitThermal=_CucsPciUnitThermal_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,15),_CucsPciUnitThermal_Type())
cucsPciUnitThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitThermal.setStatus(_A)
_CucsPciUnitVendor_Type=SnmpAdminString
_CucsPciUnitVendor_Object=MibTableColumn
cucsPciUnitVendor=_CucsPciUnitVendor_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,16),_CucsPciUnitVendor_Type())
cucsPciUnitVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitVendor.setStatus(_A)
_CucsPciUnitVoltage_Type=CucsEquipmentSensorThresholdStatus
_CucsPciUnitVoltage_Object=MibTableColumn
cucsPciUnitVoltage=_CucsPciUnitVoltage_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,17),_CucsPciUnitVoltage_Type())
cucsPciUnitVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitVoltage.setStatus(_A)
_CucsPciUnitOperQualifierReason_Type=SnmpAdminString
_CucsPciUnitOperQualifierReason_Object=MibTableColumn
cucsPciUnitOperQualifierReason=_CucsPciUnitOperQualifierReason_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,18),_CucsPciUnitOperQualifierReason_Type())
cucsPciUnitOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitOperQualifierReason.setStatus(_A)
_CucsPciUnitLocationDn_Type=SnmpAdminString
_CucsPciUnitLocationDn_Object=MibTableColumn
cucsPciUnitLocationDn=_CucsPciUnitLocationDn_Object((1,3,6,1,4,1,9,9,719,1,36,1,1,19),_CucsPciUnitLocationDn_Type())
cucsPciUnitLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciUnitLocationDn.setStatus(_A)
_CucsPciEquipSlotTable_Object=MibTable
cucsPciEquipSlotTable=_CucsPciEquipSlotTable_Object((1,3,6,1,4,1,9,9,719,1,36,2))
if mibBuilder.loadTexts:cucsPciEquipSlotTable.setStatus(_A)
_CucsPciEquipSlotEntry_Object=MibTableRow
cucsPciEquipSlotEntry=_CucsPciEquipSlotEntry_Object((1,3,6,1,4,1,9,9,719,1,36,2,1))
cucsPciEquipSlotEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsPciEquipSlotEntry.setStatus(_A)
_CucsPciEquipSlotInstanceId_Type=CucsManagedObjectId
_CucsPciEquipSlotInstanceId_Object=MibTableColumn
cucsPciEquipSlotInstanceId=_CucsPciEquipSlotInstanceId_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,1),_CucsPciEquipSlotInstanceId_Type())
cucsPciEquipSlotInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsPciEquipSlotInstanceId.setStatus(_A)
_CucsPciEquipSlotDn_Type=CucsManagedObjectDn
_CucsPciEquipSlotDn_Object=MibTableColumn
cucsPciEquipSlotDn=_CucsPciEquipSlotDn_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,2),_CucsPciEquipSlotDn_Type())
cucsPciEquipSlotDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotDn.setStatus(_A)
_CucsPciEquipSlotRn_Type=SnmpAdminString
_CucsPciEquipSlotRn_Object=MibTableColumn
cucsPciEquipSlotRn=_CucsPciEquipSlotRn_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,3),_CucsPciEquipSlotRn_Type())
cucsPciEquipSlotRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotRn.setStatus(_A)
_CucsPciEquipSlotControllerReported_Type=SnmpAdminString
_CucsPciEquipSlotControllerReported_Object=MibTableColumn
cucsPciEquipSlotControllerReported=_CucsPciEquipSlotControllerReported_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,4),_CucsPciEquipSlotControllerReported_Type())
cucsPciEquipSlotControllerReported.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotControllerReported.setStatus(_A)
_CucsPciEquipSlotDiscoveryState_Type=CucsEquipmentDiscoveryState
_CucsPciEquipSlotDiscoveryState_Object=MibTableColumn
cucsPciEquipSlotDiscoveryState=_CucsPciEquipSlotDiscoveryState_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,5),_CucsPciEquipSlotDiscoveryState_Type())
cucsPciEquipSlotDiscoveryState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotDiscoveryState.setStatus(_A)
_CucsPciEquipSlotFltAggr_Type=Unsigned64
_CucsPciEquipSlotFltAggr_Object=MibTableColumn
cucsPciEquipSlotFltAggr=_CucsPciEquipSlotFltAggr_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,6),_CucsPciEquipSlotFltAggr_Type())
cucsPciEquipSlotFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotFltAggr.setStatus(_A)
_CucsPciEquipSlotHostReported_Type=SnmpAdminString
_CucsPciEquipSlotHostReported_Object=MibTableColumn
cucsPciEquipSlotHostReported=_CucsPciEquipSlotHostReported_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,7),_CucsPciEquipSlotHostReported_Type())
cucsPciEquipSlotHostReported.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotHostReported.setStatus(_A)
_CucsPciEquipSlotId_Type=CucsPciEquipSlotId
_CucsPciEquipSlotId_Object=MibTableColumn
cucsPciEquipSlotId=_CucsPciEquipSlotId_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,8),_CucsPciEquipSlotId_Type())
cucsPciEquipSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotId.setStatus(_A)
_CucsPciEquipSlotMacLeft_Type=MacAddress
_CucsPciEquipSlotMacLeft_Object=MibTableColumn
cucsPciEquipSlotMacLeft=_CucsPciEquipSlotMacLeft_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,9),_CucsPciEquipSlotMacLeft_Type())
cucsPciEquipSlotMacLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotMacLeft.setStatus(_A)
_CucsPciEquipSlotMacRight_Type=MacAddress
_CucsPciEquipSlotMacRight_Object=MibTableColumn
cucsPciEquipSlotMacRight=_CucsPciEquipSlotMacRight_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,10),_CucsPciEquipSlotMacRight_Type())
cucsPciEquipSlotMacRight.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotMacRight.setStatus(_A)
_CucsPciEquipSlotModel_Type=SnmpAdminString
_CucsPciEquipSlotModel_Object=MibTableColumn
cucsPciEquipSlotModel=_CucsPciEquipSlotModel_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,11),_CucsPciEquipSlotModel_Type())
cucsPciEquipSlotModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotModel.setStatus(_A)
_CucsPciEquipSlotRevision_Type=SnmpAdminString
_CucsPciEquipSlotRevision_Object=MibTableColumn
cucsPciEquipSlotRevision=_CucsPciEquipSlotRevision_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,12),_CucsPciEquipSlotRevision_Type())
cucsPciEquipSlotRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotRevision.setStatus(_A)
_CucsPciEquipSlotSerial_Type=SnmpAdminString
_CucsPciEquipSlotSerial_Object=MibTableColumn
cucsPciEquipSlotSerial=_CucsPciEquipSlotSerial_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,13),_CucsPciEquipSlotSerial_Type())
cucsPciEquipSlotSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotSerial.setStatus(_A)
_CucsPciEquipSlotSmbiosId_Type=Gauge32
_CucsPciEquipSlotSmbiosId_Object=MibTableColumn
cucsPciEquipSlotSmbiosId=_CucsPciEquipSlotSmbiosId_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,14),_CucsPciEquipSlotSmbiosId_Type())
cucsPciEquipSlotSmbiosId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotSmbiosId.setStatus(_A)
_CucsPciEquipSlotVendor_Type=SnmpAdminString
_CucsPciEquipSlotVendor_Object=MibTableColumn
cucsPciEquipSlotVendor=_CucsPciEquipSlotVendor_Object((1,3,6,1,4,1,9,9,719,1,36,2,1,15),_CucsPciEquipSlotVendor_Type())
cucsPciEquipSlotVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPciEquipSlotVendor.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsPciObjects':cucsPciObjects,'cucsPciUnitTable':cucsPciUnitTable,'cucsPciUnitEntry':cucsPciUnitEntry,_D:cucsPciUnitInstanceId,'cucsPciUnitDn':cucsPciUnitDn,'cucsPciUnitRn':cucsPciUnitRn,'cucsPciUnitId':cucsPciUnitId,'cucsPciUnitModel':cucsPciUnitModel,'cucsPciUnitOperState':cucsPciUnitOperState,'cucsPciUnitOperability':cucsPciUnitOperability,'cucsPciUnitPciAddr':cucsPciUnitPciAddr,'cucsPciUnitPciSlot':cucsPciUnitPciSlot,'cucsPciUnitPerf':cucsPciUnitPerf,'cucsPciUnitPower':cucsPciUnitPower,'cucsPciUnitPresence':cucsPciUnitPresence,'cucsPciUnitRevision':cucsPciUnitRevision,'cucsPciUnitSerial':cucsPciUnitSerial,'cucsPciUnitThermal':cucsPciUnitThermal,'cucsPciUnitVendor':cucsPciUnitVendor,'cucsPciUnitVoltage':cucsPciUnitVoltage,'cucsPciUnitOperQualifierReason':cucsPciUnitOperQualifierReason,'cucsPciUnitLocationDn':cucsPciUnitLocationDn,'cucsPciEquipSlotTable':cucsPciEquipSlotTable,'cucsPciEquipSlotEntry':cucsPciEquipSlotEntry,_F:cucsPciEquipSlotInstanceId,'cucsPciEquipSlotDn':cucsPciEquipSlotDn,'cucsPciEquipSlotRn':cucsPciEquipSlotRn,'cucsPciEquipSlotControllerReported':cucsPciEquipSlotControllerReported,'cucsPciEquipSlotDiscoveryState':cucsPciEquipSlotDiscoveryState,'cucsPciEquipSlotFltAggr':cucsPciEquipSlotFltAggr,'cucsPciEquipSlotHostReported':cucsPciEquipSlotHostReported,'cucsPciEquipSlotId':cucsPciEquipSlotId,'cucsPciEquipSlotMacLeft':cucsPciEquipSlotMacLeft,'cucsPciEquipSlotMacRight':cucsPciEquipSlotMacRight,'cucsPciEquipSlotModel':cucsPciEquipSlotModel,'cucsPciEquipSlotRevision':cucsPciEquipSlotRevision,'cucsPciEquipSlotSerial':cucsPciEquipSlotSerial,'cucsPciEquipSlotSmbiosId':cucsPciEquipSlotSmbiosId,'cucsPciEquipSlotVendor':cucsPciEquipSlotVendor})