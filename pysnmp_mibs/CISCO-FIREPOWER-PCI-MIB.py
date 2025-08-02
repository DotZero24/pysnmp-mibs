_F='cfprPciUnitInstanceId'
_E='not-accessible'
_D='cfprPciEquipSlotInstanceId'
_C='CISCO-FIREPOWER-PCI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprEquipmentDiscoveryState,CfprEquipmentOperability,CfprEquipmentPowerState,CfprEquipmentPresence,CfprEquipmentSensorThresholdStatus,CfprPciEquipSlotId=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprEquipmentDiscoveryState','CfprEquipmentOperability','CfprEquipmentPowerState','CfprEquipmentPresence','CfprEquipmentSensorThresholdStatus','CfprPciEquipSlotId')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprPciObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,60))
_CfprPciEquipSlotTable_Object=MibTable
cfprPciEquipSlotTable=_CfprPciEquipSlotTable_Object((1,3,6,1,4,1,9,9,826,1,60,1))
if mibBuilder.loadTexts:cfprPciEquipSlotTable.setStatus(_A)
_CfprPciEquipSlotEntry_Object=MibTableRow
cfprPciEquipSlotEntry=_CfprPciEquipSlotEntry_Object((1,3,6,1,4,1,9,9,826,1,60,1,1))
cfprPciEquipSlotEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprPciEquipSlotEntry.setStatus(_A)
_CfprPciEquipSlotInstanceId_Type=CfprManagedObjectId
_CfprPciEquipSlotInstanceId_Object=MibTableColumn
cfprPciEquipSlotInstanceId=_CfprPciEquipSlotInstanceId_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,1),_CfprPciEquipSlotInstanceId_Type())
cfprPciEquipSlotInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprPciEquipSlotInstanceId.setStatus(_A)
_CfprPciEquipSlotDn_Type=CfprManagedObjectDn
_CfprPciEquipSlotDn_Object=MibTableColumn
cfprPciEquipSlotDn=_CfprPciEquipSlotDn_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,2),_CfprPciEquipSlotDn_Type())
cfprPciEquipSlotDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotDn.setStatus(_A)
_CfprPciEquipSlotRn_Type=SnmpAdminString
_CfprPciEquipSlotRn_Object=MibTableColumn
cfprPciEquipSlotRn=_CfprPciEquipSlotRn_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,3),_CfprPciEquipSlotRn_Type())
cfprPciEquipSlotRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotRn.setStatus(_A)
_CfprPciEquipSlotControllerReported_Type=SnmpAdminString
_CfprPciEquipSlotControllerReported_Object=MibTableColumn
cfprPciEquipSlotControllerReported=_CfprPciEquipSlotControllerReported_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,4),_CfprPciEquipSlotControllerReported_Type())
cfprPciEquipSlotControllerReported.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotControllerReported.setStatus(_A)
_CfprPciEquipSlotDiscoveryState_Type=CfprEquipmentDiscoveryState
_CfprPciEquipSlotDiscoveryState_Object=MibTableColumn
cfprPciEquipSlotDiscoveryState=_CfprPciEquipSlotDiscoveryState_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,5),_CfprPciEquipSlotDiscoveryState_Type())
cfprPciEquipSlotDiscoveryState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotDiscoveryState.setStatus(_A)
_CfprPciEquipSlotFltAggr_Type=Unsigned64
_CfprPciEquipSlotFltAggr_Object=MibTableColumn
cfprPciEquipSlotFltAggr=_CfprPciEquipSlotFltAggr_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,6),_CfprPciEquipSlotFltAggr_Type())
cfprPciEquipSlotFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotFltAggr.setStatus(_A)
_CfprPciEquipSlotHostReported_Type=SnmpAdminString
_CfprPciEquipSlotHostReported_Object=MibTableColumn
cfprPciEquipSlotHostReported=_CfprPciEquipSlotHostReported_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,7),_CfprPciEquipSlotHostReported_Type())
cfprPciEquipSlotHostReported.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotHostReported.setStatus(_A)
_CfprPciEquipSlotId_Type=CfprPciEquipSlotId
_CfprPciEquipSlotId_Object=MibTableColumn
cfprPciEquipSlotId=_CfprPciEquipSlotId_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,8),_CfprPciEquipSlotId_Type())
cfprPciEquipSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotId.setStatus(_A)
_CfprPciEquipSlotMacLeft_Type=MacAddress
_CfprPciEquipSlotMacLeft_Object=MibTableColumn
cfprPciEquipSlotMacLeft=_CfprPciEquipSlotMacLeft_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,9),_CfprPciEquipSlotMacLeft_Type())
cfprPciEquipSlotMacLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotMacLeft.setStatus(_A)
_CfprPciEquipSlotMacRight_Type=MacAddress
_CfprPciEquipSlotMacRight_Object=MibTableColumn
cfprPciEquipSlotMacRight=_CfprPciEquipSlotMacRight_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,10),_CfprPciEquipSlotMacRight_Type())
cfprPciEquipSlotMacRight.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotMacRight.setStatus(_A)
_CfprPciEquipSlotModel_Type=SnmpAdminString
_CfprPciEquipSlotModel_Object=MibTableColumn
cfprPciEquipSlotModel=_CfprPciEquipSlotModel_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,11),_CfprPciEquipSlotModel_Type())
cfprPciEquipSlotModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotModel.setStatus(_A)
_CfprPciEquipSlotRevision_Type=SnmpAdminString
_CfprPciEquipSlotRevision_Object=MibTableColumn
cfprPciEquipSlotRevision=_CfprPciEquipSlotRevision_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,12),_CfprPciEquipSlotRevision_Type())
cfprPciEquipSlotRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotRevision.setStatus(_A)
_CfprPciEquipSlotSerial_Type=SnmpAdminString
_CfprPciEquipSlotSerial_Object=MibTableColumn
cfprPciEquipSlotSerial=_CfprPciEquipSlotSerial_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,13),_CfprPciEquipSlotSerial_Type())
cfprPciEquipSlotSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotSerial.setStatus(_A)
_CfprPciEquipSlotSmbiosId_Type=Gauge32
_CfprPciEquipSlotSmbiosId_Object=MibTableColumn
cfprPciEquipSlotSmbiosId=_CfprPciEquipSlotSmbiosId_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,14),_CfprPciEquipSlotSmbiosId_Type())
cfprPciEquipSlotSmbiosId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotSmbiosId.setStatus(_A)
_CfprPciEquipSlotVendor_Type=SnmpAdminString
_CfprPciEquipSlotVendor_Object=MibTableColumn
cfprPciEquipSlotVendor=_CfprPciEquipSlotVendor_Object((1,3,6,1,4,1,9,9,826,1,60,1,1,15),_CfprPciEquipSlotVendor_Type())
cfprPciEquipSlotVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciEquipSlotVendor.setStatus(_A)
_CfprPciUnitTable_Object=MibTable
cfprPciUnitTable=_CfprPciUnitTable_Object((1,3,6,1,4,1,9,9,826,1,60,2))
if mibBuilder.loadTexts:cfprPciUnitTable.setStatus(_A)
_CfprPciUnitEntry_Object=MibTableRow
cfprPciUnitEntry=_CfprPciUnitEntry_Object((1,3,6,1,4,1,9,9,826,1,60,2,1))
cfprPciUnitEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprPciUnitEntry.setStatus(_A)
_CfprPciUnitInstanceId_Type=CfprManagedObjectId
_CfprPciUnitInstanceId_Object=MibTableColumn
cfprPciUnitInstanceId=_CfprPciUnitInstanceId_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,1),_CfprPciUnitInstanceId_Type())
cfprPciUnitInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprPciUnitInstanceId.setStatus(_A)
_CfprPciUnitDn_Type=CfprManagedObjectDn
_CfprPciUnitDn_Object=MibTableColumn
cfprPciUnitDn=_CfprPciUnitDn_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,2),_CfprPciUnitDn_Type())
cfprPciUnitDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitDn.setStatus(_A)
_CfprPciUnitRn_Type=SnmpAdminString
_CfprPciUnitRn_Object=MibTableColumn
cfprPciUnitRn=_CfprPciUnitRn_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,3),_CfprPciUnitRn_Type())
cfprPciUnitRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitRn.setStatus(_A)
_CfprPciUnitId_Type=Gauge32
_CfprPciUnitId_Object=MibTableColumn
cfprPciUnitId=_CfprPciUnitId_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,4),_CfprPciUnitId_Type())
cfprPciUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitId.setStatus(_A)
_CfprPciUnitLocationDn_Type=SnmpAdminString
_CfprPciUnitLocationDn_Object=MibTableColumn
cfprPciUnitLocationDn=_CfprPciUnitLocationDn_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,5),_CfprPciUnitLocationDn_Type())
cfprPciUnitLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitLocationDn.setStatus(_A)
_CfprPciUnitModel_Type=SnmpAdminString
_CfprPciUnitModel_Object=MibTableColumn
cfprPciUnitModel=_CfprPciUnitModel_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,6),_CfprPciUnitModel_Type())
cfprPciUnitModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitModel.setStatus(_A)
_CfprPciUnitOperQualifierReason_Type=SnmpAdminString
_CfprPciUnitOperQualifierReason_Object=MibTableColumn
cfprPciUnitOperQualifierReason=_CfprPciUnitOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,7),_CfprPciUnitOperQualifierReason_Type())
cfprPciUnitOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitOperQualifierReason.setStatus(_A)
_CfprPciUnitOperState_Type=CfprEquipmentOperability
_CfprPciUnitOperState_Object=MibTableColumn
cfprPciUnitOperState=_CfprPciUnitOperState_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,8),_CfprPciUnitOperState_Type())
cfprPciUnitOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitOperState.setStatus(_A)
_CfprPciUnitOperability_Type=CfprEquipmentOperability
_CfprPciUnitOperability_Object=MibTableColumn
cfprPciUnitOperability=_CfprPciUnitOperability_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,9),_CfprPciUnitOperability_Type())
cfprPciUnitOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitOperability.setStatus(_A)
_CfprPciUnitPciAddr_Type=SnmpAdminString
_CfprPciUnitPciAddr_Object=MibTableColumn
cfprPciUnitPciAddr=_CfprPciUnitPciAddr_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,10),_CfprPciUnitPciAddr_Type())
cfprPciUnitPciAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitPciAddr.setStatus(_A)
_CfprPciUnitPciSlot_Type=SnmpAdminString
_CfprPciUnitPciSlot_Object=MibTableColumn
cfprPciUnitPciSlot=_CfprPciUnitPciSlot_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,11),_CfprPciUnitPciSlot_Type())
cfprPciUnitPciSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitPciSlot.setStatus(_A)
_CfprPciUnitPerf_Type=CfprEquipmentSensorThresholdStatus
_CfprPciUnitPerf_Object=MibTableColumn
cfprPciUnitPerf=_CfprPciUnitPerf_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,12),_CfprPciUnitPerf_Type())
cfprPciUnitPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitPerf.setStatus(_A)
_CfprPciUnitPower_Type=CfprEquipmentPowerState
_CfprPciUnitPower_Object=MibTableColumn
cfprPciUnitPower=_CfprPciUnitPower_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,13),_CfprPciUnitPower_Type())
cfprPciUnitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitPower.setStatus(_A)
_CfprPciUnitPresence_Type=CfprEquipmentPresence
_CfprPciUnitPresence_Object=MibTableColumn
cfprPciUnitPresence=_CfprPciUnitPresence_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,14),_CfprPciUnitPresence_Type())
cfprPciUnitPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitPresence.setStatus(_A)
_CfprPciUnitRevision_Type=SnmpAdminString
_CfprPciUnitRevision_Object=MibTableColumn
cfprPciUnitRevision=_CfprPciUnitRevision_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,15),_CfprPciUnitRevision_Type())
cfprPciUnitRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitRevision.setStatus(_A)
_CfprPciUnitSerial_Type=SnmpAdminString
_CfprPciUnitSerial_Object=MibTableColumn
cfprPciUnitSerial=_CfprPciUnitSerial_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,16),_CfprPciUnitSerial_Type())
cfprPciUnitSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitSerial.setStatus(_A)
_CfprPciUnitThermal_Type=CfprEquipmentSensorThresholdStatus
_CfprPciUnitThermal_Object=MibTableColumn
cfprPciUnitThermal=_CfprPciUnitThermal_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,17),_CfprPciUnitThermal_Type())
cfprPciUnitThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitThermal.setStatus(_A)
_CfprPciUnitVendor_Type=SnmpAdminString
_CfprPciUnitVendor_Object=MibTableColumn
cfprPciUnitVendor=_CfprPciUnitVendor_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,18),_CfprPciUnitVendor_Type())
cfprPciUnitVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitVendor.setStatus(_A)
_CfprPciUnitVoltage_Type=CfprEquipmentSensorThresholdStatus
_CfprPciUnitVoltage_Object=MibTableColumn
cfprPciUnitVoltage=_CfprPciUnitVoltage_Object((1,3,6,1,4,1,9,9,826,1,60,2,1,19),_CfprPciUnitVoltage_Type())
cfprPciUnitVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPciUnitVoltage.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprPciObjects':cfprPciObjects,'cfprPciEquipSlotTable':cfprPciEquipSlotTable,'cfprPciEquipSlotEntry':cfprPciEquipSlotEntry,_D:cfprPciEquipSlotInstanceId,'cfprPciEquipSlotDn':cfprPciEquipSlotDn,'cfprPciEquipSlotRn':cfprPciEquipSlotRn,'cfprPciEquipSlotControllerReported':cfprPciEquipSlotControllerReported,'cfprPciEquipSlotDiscoveryState':cfprPciEquipSlotDiscoveryState,'cfprPciEquipSlotFltAggr':cfprPciEquipSlotFltAggr,'cfprPciEquipSlotHostReported':cfprPciEquipSlotHostReported,'cfprPciEquipSlotId':cfprPciEquipSlotId,'cfprPciEquipSlotMacLeft':cfprPciEquipSlotMacLeft,'cfprPciEquipSlotMacRight':cfprPciEquipSlotMacRight,'cfprPciEquipSlotModel':cfprPciEquipSlotModel,'cfprPciEquipSlotRevision':cfprPciEquipSlotRevision,'cfprPciEquipSlotSerial':cfprPciEquipSlotSerial,'cfprPciEquipSlotSmbiosId':cfprPciEquipSlotSmbiosId,'cfprPciEquipSlotVendor':cfprPciEquipSlotVendor,'cfprPciUnitTable':cfprPciUnitTable,'cfprPciUnitEntry':cfprPciUnitEntry,_F:cfprPciUnitInstanceId,'cfprPciUnitDn':cfprPciUnitDn,'cfprPciUnitRn':cfprPciUnitRn,'cfprPciUnitId':cfprPciUnitId,'cfprPciUnitLocationDn':cfprPciUnitLocationDn,'cfprPciUnitModel':cfprPciUnitModel,'cfprPciUnitOperQualifierReason':cfprPciUnitOperQualifierReason,'cfprPciUnitOperState':cfprPciUnitOperState,'cfprPciUnitOperability':cfprPciUnitOperability,'cfprPciUnitPciAddr':cfprPciUnitPciAddr,'cfprPciUnitPciSlot':cfprPciUnitPciSlot,'cfprPciUnitPerf':cfprPciUnitPerf,'cfprPciUnitPower':cfprPciUnitPower,'cfprPciUnitPresence':cfprPciUnitPresence,'cfprPciUnitRevision':cfprPciUnitRevision,'cfprPciUnitSerial':cfprPciUnitSerial,'cfprPciUnitThermal':cfprPciUnitThermal,'cfprPciUnitVendor':cfprPciUnitVendor,'cfprPciUnitVoltage':cfprPciUnitVoltage})