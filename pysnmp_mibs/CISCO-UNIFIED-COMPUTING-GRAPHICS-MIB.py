_F='cucsGraphicsControllerInstanceId'
_E='not-accessible'
_D='cucsGraphicsCardInstanceId'
_C='CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsEquipmentOperability,CucsEquipmentPowerState,CucsEquipmentPresence,CucsEquipmentSensorThresholdStatus,CucsFsmLifecycle,CucsGraphicsGpuMode=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsEquipmentOperability','CucsEquipmentPowerState','CucsEquipmentPresence','CucsEquipmentSensorThresholdStatus','CucsFsmLifecycle','CucsGraphicsGpuMode')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsGraphicsObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,73))
_CucsGraphicsCardTable_Object=MibTable
cucsGraphicsCardTable=_CucsGraphicsCardTable_Object((1,3,6,1,4,1,9,9,719,1,73,1))
if mibBuilder.loadTexts:cucsGraphicsCardTable.setStatus(_A)
_CucsGraphicsCardEntry_Object=MibTableRow
cucsGraphicsCardEntry=_CucsGraphicsCardEntry_Object((1,3,6,1,4,1,9,9,719,1,73,1,1))
cucsGraphicsCardEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsGraphicsCardEntry.setStatus(_A)
_CucsGraphicsCardInstanceId_Type=CucsManagedObjectId
_CucsGraphicsCardInstanceId_Object=MibTableColumn
cucsGraphicsCardInstanceId=_CucsGraphicsCardInstanceId_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,1),_CucsGraphicsCardInstanceId_Type())
cucsGraphicsCardInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsGraphicsCardInstanceId.setStatus(_A)
_CucsGraphicsCardDn_Type=CucsManagedObjectDn
_CucsGraphicsCardDn_Object=MibTableColumn
cucsGraphicsCardDn=_CucsGraphicsCardDn_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,2),_CucsGraphicsCardDn_Type())
cucsGraphicsCardDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardDn.setStatus(_A)
_CucsGraphicsCardRn_Type=SnmpAdminString
_CucsGraphicsCardRn_Object=MibTableColumn
cucsGraphicsCardRn=_CucsGraphicsCardRn_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,3),_CucsGraphicsCardRn_Type())
cucsGraphicsCardRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardRn.setStatus(_A)
_CucsGraphicsCardDeviceId_Type=Gauge32
_CucsGraphicsCardDeviceId_Object=MibTableColumn
cucsGraphicsCardDeviceId=_CucsGraphicsCardDeviceId_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,4),_CucsGraphicsCardDeviceId_Type())
cucsGraphicsCardDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardDeviceId.setStatus(_A)
_CucsGraphicsCardId_Type=Gauge32
_CucsGraphicsCardId_Object=MibTableColumn
cucsGraphicsCardId=_CucsGraphicsCardId_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,5),_CucsGraphicsCardId_Type())
cucsGraphicsCardId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardId.setStatus(_A)
_CucsGraphicsCardIsSupported_Type=TruthValue
_CucsGraphicsCardIsSupported_Object=MibTableColumn
cucsGraphicsCardIsSupported=_CucsGraphicsCardIsSupported_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,6),_CucsGraphicsCardIsSupported_Type())
cucsGraphicsCardIsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardIsSupported.setStatus(_A)
_CucsGraphicsCardLc_Type=CucsFsmLifecycle
_CucsGraphicsCardLc_Object=MibTableColumn
cucsGraphicsCardLc=_CucsGraphicsCardLc_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,7),_CucsGraphicsCardLc_Type())
cucsGraphicsCardLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardLc.setStatus(_A)
_CucsGraphicsCardModel_Type=SnmpAdminString
_CucsGraphicsCardModel_Object=MibTableColumn
cucsGraphicsCardModel=_CucsGraphicsCardModel_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,8),_CucsGraphicsCardModel_Type())
cucsGraphicsCardModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardModel.setStatus(_A)
_CucsGraphicsCardOperQualifierReason_Type=SnmpAdminString
_CucsGraphicsCardOperQualifierReason_Object=MibTableColumn
cucsGraphicsCardOperQualifierReason=_CucsGraphicsCardOperQualifierReason_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,9),_CucsGraphicsCardOperQualifierReason_Type())
cucsGraphicsCardOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardOperQualifierReason.setStatus(_A)
_CucsGraphicsCardOperState_Type=CucsEquipmentOperability
_CucsGraphicsCardOperState_Object=MibTableColumn
cucsGraphicsCardOperState=_CucsGraphicsCardOperState_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,10),_CucsGraphicsCardOperState_Type())
cucsGraphicsCardOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardOperState.setStatus(_A)
_CucsGraphicsCardOperability_Type=CucsEquipmentOperability
_CucsGraphicsCardOperability_Object=MibTableColumn
cucsGraphicsCardOperability=_CucsGraphicsCardOperability_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,11),_CucsGraphicsCardOperability_Type())
cucsGraphicsCardOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardOperability.setStatus(_A)
_CucsGraphicsCardPciAddr_Type=SnmpAdminString
_CucsGraphicsCardPciAddr_Object=MibTableColumn
cucsGraphicsCardPciAddr=_CucsGraphicsCardPciAddr_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,12),_CucsGraphicsCardPciAddr_Type())
cucsGraphicsCardPciAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardPciAddr.setStatus(_A)
_CucsGraphicsCardPciSlot_Type=SnmpAdminString
_CucsGraphicsCardPciSlot_Object=MibTableColumn
cucsGraphicsCardPciSlot=_CucsGraphicsCardPciSlot_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,13),_CucsGraphicsCardPciSlot_Type())
cucsGraphicsCardPciSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardPciSlot.setStatus(_A)
_CucsGraphicsCardPerf_Type=CucsEquipmentSensorThresholdStatus
_CucsGraphicsCardPerf_Object=MibTableColumn
cucsGraphicsCardPerf=_CucsGraphicsCardPerf_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,14),_CucsGraphicsCardPerf_Type())
cucsGraphicsCardPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardPerf.setStatus(_A)
_CucsGraphicsCardPower_Type=CucsEquipmentPowerState
_CucsGraphicsCardPower_Object=MibTableColumn
cucsGraphicsCardPower=_CucsGraphicsCardPower_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,15),_CucsGraphicsCardPower_Type())
cucsGraphicsCardPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardPower.setStatus(_A)
_CucsGraphicsCardPresence_Type=CucsEquipmentPresence
_CucsGraphicsCardPresence_Object=MibTableColumn
cucsGraphicsCardPresence=_CucsGraphicsCardPresence_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,16),_CucsGraphicsCardPresence_Type())
cucsGraphicsCardPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardPresence.setStatus(_A)
_CucsGraphicsCardRevision_Type=SnmpAdminString
_CucsGraphicsCardRevision_Object=MibTableColumn
cucsGraphicsCardRevision=_CucsGraphicsCardRevision_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,17),_CucsGraphicsCardRevision_Type())
cucsGraphicsCardRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardRevision.setStatus(_A)
_CucsGraphicsCardSerial_Type=SnmpAdminString
_CucsGraphicsCardSerial_Object=MibTableColumn
cucsGraphicsCardSerial=_CucsGraphicsCardSerial_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,18),_CucsGraphicsCardSerial_Type())
cucsGraphicsCardSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardSerial.setStatus(_A)
_CucsGraphicsCardSubDeviceId_Type=Gauge32
_CucsGraphicsCardSubDeviceId_Object=MibTableColumn
cucsGraphicsCardSubDeviceId=_CucsGraphicsCardSubDeviceId_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,19),_CucsGraphicsCardSubDeviceId_Type())
cucsGraphicsCardSubDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardSubDeviceId.setStatus(_A)
_CucsGraphicsCardSubVendorId_Type=Gauge32
_CucsGraphicsCardSubVendorId_Object=MibTableColumn
cucsGraphicsCardSubVendorId=_CucsGraphicsCardSubVendorId_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,20),_CucsGraphicsCardSubVendorId_Type())
cucsGraphicsCardSubVendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardSubVendorId.setStatus(_A)
_CucsGraphicsCardThermal_Type=CucsEquipmentSensorThresholdStatus
_CucsGraphicsCardThermal_Object=MibTableColumn
cucsGraphicsCardThermal=_CucsGraphicsCardThermal_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,21),_CucsGraphicsCardThermal_Type())
cucsGraphicsCardThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardThermal.setStatus(_A)
_CucsGraphicsCardVendor_Type=SnmpAdminString
_CucsGraphicsCardVendor_Object=MibTableColumn
cucsGraphicsCardVendor=_CucsGraphicsCardVendor_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,22),_CucsGraphicsCardVendor_Type())
cucsGraphicsCardVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardVendor.setStatus(_A)
_CucsGraphicsCardVendorId_Type=Gauge32
_CucsGraphicsCardVendorId_Object=MibTableColumn
cucsGraphicsCardVendorId=_CucsGraphicsCardVendorId_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,23),_CucsGraphicsCardVendorId_Type())
cucsGraphicsCardVendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardVendorId.setStatus(_A)
_CucsGraphicsCardVoltage_Type=CucsEquipmentSensorThresholdStatus
_CucsGraphicsCardVoltage_Object=MibTableColumn
cucsGraphicsCardVoltage=_CucsGraphicsCardVoltage_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,24),_CucsGraphicsCardVoltage_Type())
cucsGraphicsCardVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardVoltage.setStatus(_A)
_CucsGraphicsCardLocationDn_Type=SnmpAdminString
_CucsGraphicsCardLocationDn_Object=MibTableColumn
cucsGraphicsCardLocationDn=_CucsGraphicsCardLocationDn_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,25),_CucsGraphicsCardLocationDn_Type())
cucsGraphicsCardLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardLocationDn.setStatus(_A)
_CucsGraphicsCardStepping_Type=SnmpAdminString
_CucsGraphicsCardStepping_Object=MibTableColumn
cucsGraphicsCardStepping=_CucsGraphicsCardStepping_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,26),_CucsGraphicsCardStepping_Type())
cucsGraphicsCardStepping.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardStepping.setStatus(_A)
_CucsGraphicsCardExpanderSlot_Type=SnmpAdminString
_CucsGraphicsCardExpanderSlot_Object=MibTableColumn
cucsGraphicsCardExpanderSlot=_CucsGraphicsCardExpanderSlot_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,27),_CucsGraphicsCardExpanderSlot_Type())
cucsGraphicsCardExpanderSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardExpanderSlot.setStatus(_A)
_CucsGraphicsCardFirmwareVersion_Type=SnmpAdminString
_CucsGraphicsCardFirmwareVersion_Object=MibTableColumn
cucsGraphicsCardFirmwareVersion=_CucsGraphicsCardFirmwareVersion_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,28),_CucsGraphicsCardFirmwareVersion_Type())
cucsGraphicsCardFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardFirmwareVersion.setStatus(_A)
_CucsGraphicsCardPciAddrList_Type=SnmpAdminString
_CucsGraphicsCardPciAddrList_Object=MibTableColumn
cucsGraphicsCardPciAddrList=_CucsGraphicsCardPciAddrList_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,29),_CucsGraphicsCardPciAddrList_Type())
cucsGraphicsCardPciAddrList.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardPciAddrList.setStatus(_A)
_CucsGraphicsCardMode_Type=CucsGraphicsGpuMode
_CucsGraphicsCardMode_Object=MibTableColumn
cucsGraphicsCardMode=_CucsGraphicsCardMode_Object((1,3,6,1,4,1,9,9,719,1,73,1,1,30),_CucsGraphicsCardMode_Type())
cucsGraphicsCardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsCardMode.setStatus(_A)
_CucsGraphicsControllerTable_Object=MibTable
cucsGraphicsControllerTable=_CucsGraphicsControllerTable_Object((1,3,6,1,4,1,9,9,719,1,73,2))
if mibBuilder.loadTexts:cucsGraphicsControllerTable.setStatus(_A)
_CucsGraphicsControllerEntry_Object=MibTableRow
cucsGraphicsControllerEntry=_CucsGraphicsControllerEntry_Object((1,3,6,1,4,1,9,9,719,1,73,2,1))
cucsGraphicsControllerEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsGraphicsControllerEntry.setStatus(_A)
_CucsGraphicsControllerInstanceId_Type=CucsManagedObjectId
_CucsGraphicsControllerInstanceId_Object=MibTableColumn
cucsGraphicsControllerInstanceId=_CucsGraphicsControllerInstanceId_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,1),_CucsGraphicsControllerInstanceId_Type())
cucsGraphicsControllerInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsGraphicsControllerInstanceId.setStatus(_A)
_CucsGraphicsControllerDn_Type=CucsManagedObjectDn
_CucsGraphicsControllerDn_Object=MibTableColumn
cucsGraphicsControllerDn=_CucsGraphicsControllerDn_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,2),_CucsGraphicsControllerDn_Type())
cucsGraphicsControllerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerDn.setStatus(_A)
_CucsGraphicsControllerRn_Type=SnmpAdminString
_CucsGraphicsControllerRn_Object=MibTableColumn
cucsGraphicsControllerRn=_CucsGraphicsControllerRn_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,3),_CucsGraphicsControllerRn_Type())
cucsGraphicsControllerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerRn.setStatus(_A)
_CucsGraphicsControllerId_Type=Gauge32
_CucsGraphicsControllerId_Object=MibTableColumn
cucsGraphicsControllerId=_CucsGraphicsControllerId_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,4),_CucsGraphicsControllerId_Type())
cucsGraphicsControllerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerId.setStatus(_A)
_CucsGraphicsControllerModel_Type=SnmpAdminString
_CucsGraphicsControllerModel_Object=MibTableColumn
cucsGraphicsControllerModel=_CucsGraphicsControllerModel_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,5),_CucsGraphicsControllerModel_Type())
cucsGraphicsControllerModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerModel.setStatus(_A)
_CucsGraphicsControllerOperQualifierReason_Type=SnmpAdminString
_CucsGraphicsControllerOperQualifierReason_Object=MibTableColumn
cucsGraphicsControllerOperQualifierReason=_CucsGraphicsControllerOperQualifierReason_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,6),_CucsGraphicsControllerOperQualifierReason_Type())
cucsGraphicsControllerOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerOperQualifierReason.setStatus(_A)
_CucsGraphicsControllerOperState_Type=CucsEquipmentOperability
_CucsGraphicsControllerOperState_Object=MibTableColumn
cucsGraphicsControllerOperState=_CucsGraphicsControllerOperState_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,7),_CucsGraphicsControllerOperState_Type())
cucsGraphicsControllerOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerOperState.setStatus(_A)
_CucsGraphicsControllerOperability_Type=CucsEquipmentOperability
_CucsGraphicsControllerOperability_Object=MibTableColumn
cucsGraphicsControllerOperability=_CucsGraphicsControllerOperability_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,8),_CucsGraphicsControllerOperability_Type())
cucsGraphicsControllerOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerOperability.setStatus(_A)
_CucsGraphicsControllerPciAddr_Type=SnmpAdminString
_CucsGraphicsControllerPciAddr_Object=MibTableColumn
cucsGraphicsControllerPciAddr=_CucsGraphicsControllerPciAddr_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,9),_CucsGraphicsControllerPciAddr_Type())
cucsGraphicsControllerPciAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerPciAddr.setStatus(_A)
_CucsGraphicsControllerPciSlot_Type=SnmpAdminString
_CucsGraphicsControllerPciSlot_Object=MibTableColumn
cucsGraphicsControllerPciSlot=_CucsGraphicsControllerPciSlot_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,10),_CucsGraphicsControllerPciSlot_Type())
cucsGraphicsControllerPciSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerPciSlot.setStatus(_A)
_CucsGraphicsControllerPerf_Type=CucsEquipmentSensorThresholdStatus
_CucsGraphicsControllerPerf_Object=MibTableColumn
cucsGraphicsControllerPerf=_CucsGraphicsControllerPerf_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,11),_CucsGraphicsControllerPerf_Type())
cucsGraphicsControllerPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerPerf.setStatus(_A)
_CucsGraphicsControllerPower_Type=CucsEquipmentPowerState
_CucsGraphicsControllerPower_Object=MibTableColumn
cucsGraphicsControllerPower=_CucsGraphicsControllerPower_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,12),_CucsGraphicsControllerPower_Type())
cucsGraphicsControllerPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerPower.setStatus(_A)
_CucsGraphicsControllerPresence_Type=CucsEquipmentPresence
_CucsGraphicsControllerPresence_Object=MibTableColumn
cucsGraphicsControllerPresence=_CucsGraphicsControllerPresence_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,13),_CucsGraphicsControllerPresence_Type())
cucsGraphicsControllerPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerPresence.setStatus(_A)
_CucsGraphicsControllerRevision_Type=SnmpAdminString
_CucsGraphicsControllerRevision_Object=MibTableColumn
cucsGraphicsControllerRevision=_CucsGraphicsControllerRevision_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,14),_CucsGraphicsControllerRevision_Type())
cucsGraphicsControllerRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerRevision.setStatus(_A)
_CucsGraphicsControllerSerial_Type=SnmpAdminString
_CucsGraphicsControllerSerial_Object=MibTableColumn
cucsGraphicsControllerSerial=_CucsGraphicsControllerSerial_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,15),_CucsGraphicsControllerSerial_Type())
cucsGraphicsControllerSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerSerial.setStatus(_A)
_CucsGraphicsControllerThermal_Type=CucsEquipmentSensorThresholdStatus
_CucsGraphicsControllerThermal_Object=MibTableColumn
cucsGraphicsControllerThermal=_CucsGraphicsControllerThermal_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,16),_CucsGraphicsControllerThermal_Type())
cucsGraphicsControllerThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerThermal.setStatus(_A)
_CucsGraphicsControllerVendor_Type=SnmpAdminString
_CucsGraphicsControllerVendor_Object=MibTableColumn
cucsGraphicsControllerVendor=_CucsGraphicsControllerVendor_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,17),_CucsGraphicsControllerVendor_Type())
cucsGraphicsControllerVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerVendor.setStatus(_A)
_CucsGraphicsControllerVoltage_Type=CucsEquipmentSensorThresholdStatus
_CucsGraphicsControllerVoltage_Object=MibTableColumn
cucsGraphicsControllerVoltage=_CucsGraphicsControllerVoltage_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,18),_CucsGraphicsControllerVoltage_Type())
cucsGraphicsControllerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerVoltage.setStatus(_A)
_CucsGraphicsControllerLocationDn_Type=SnmpAdminString
_CucsGraphicsControllerLocationDn_Object=MibTableColumn
cucsGraphicsControllerLocationDn=_CucsGraphicsControllerLocationDn_Object((1,3,6,1,4,1,9,9,719,1,73,2,1,19),_CucsGraphicsControllerLocationDn_Type())
cucsGraphicsControllerLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsGraphicsControllerLocationDn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsGraphicsObjects':cucsGraphicsObjects,'cucsGraphicsCardTable':cucsGraphicsCardTable,'cucsGraphicsCardEntry':cucsGraphicsCardEntry,_D:cucsGraphicsCardInstanceId,'cucsGraphicsCardDn':cucsGraphicsCardDn,'cucsGraphicsCardRn':cucsGraphicsCardRn,'cucsGraphicsCardDeviceId':cucsGraphicsCardDeviceId,'cucsGraphicsCardId':cucsGraphicsCardId,'cucsGraphicsCardIsSupported':cucsGraphicsCardIsSupported,'cucsGraphicsCardLc':cucsGraphicsCardLc,'cucsGraphicsCardModel':cucsGraphicsCardModel,'cucsGraphicsCardOperQualifierReason':cucsGraphicsCardOperQualifierReason,'cucsGraphicsCardOperState':cucsGraphicsCardOperState,'cucsGraphicsCardOperability':cucsGraphicsCardOperability,'cucsGraphicsCardPciAddr':cucsGraphicsCardPciAddr,'cucsGraphicsCardPciSlot':cucsGraphicsCardPciSlot,'cucsGraphicsCardPerf':cucsGraphicsCardPerf,'cucsGraphicsCardPower':cucsGraphicsCardPower,'cucsGraphicsCardPresence':cucsGraphicsCardPresence,'cucsGraphicsCardRevision':cucsGraphicsCardRevision,'cucsGraphicsCardSerial':cucsGraphicsCardSerial,'cucsGraphicsCardSubDeviceId':cucsGraphicsCardSubDeviceId,'cucsGraphicsCardSubVendorId':cucsGraphicsCardSubVendorId,'cucsGraphicsCardThermal':cucsGraphicsCardThermal,'cucsGraphicsCardVendor':cucsGraphicsCardVendor,'cucsGraphicsCardVendorId':cucsGraphicsCardVendorId,'cucsGraphicsCardVoltage':cucsGraphicsCardVoltage,'cucsGraphicsCardLocationDn':cucsGraphicsCardLocationDn,'cucsGraphicsCardStepping':cucsGraphicsCardStepping,'cucsGraphicsCardExpanderSlot':cucsGraphicsCardExpanderSlot,'cucsGraphicsCardFirmwareVersion':cucsGraphicsCardFirmwareVersion,'cucsGraphicsCardPciAddrList':cucsGraphicsCardPciAddrList,'cucsGraphicsCardMode':cucsGraphicsCardMode,'cucsGraphicsControllerTable':cucsGraphicsControllerTable,'cucsGraphicsControllerEntry':cucsGraphicsControllerEntry,_F:cucsGraphicsControllerInstanceId,'cucsGraphicsControllerDn':cucsGraphicsControllerDn,'cucsGraphicsControllerRn':cucsGraphicsControllerRn,'cucsGraphicsControllerId':cucsGraphicsControllerId,'cucsGraphicsControllerModel':cucsGraphicsControllerModel,'cucsGraphicsControllerOperQualifierReason':cucsGraphicsControllerOperQualifierReason,'cucsGraphicsControllerOperState':cucsGraphicsControllerOperState,'cucsGraphicsControllerOperability':cucsGraphicsControllerOperability,'cucsGraphicsControllerPciAddr':cucsGraphicsControllerPciAddr,'cucsGraphicsControllerPciSlot':cucsGraphicsControllerPciSlot,'cucsGraphicsControllerPerf':cucsGraphicsControllerPerf,'cucsGraphicsControllerPower':cucsGraphicsControllerPower,'cucsGraphicsControllerPresence':cucsGraphicsControllerPresence,'cucsGraphicsControllerRevision':cucsGraphicsControllerRevision,'cucsGraphicsControllerSerial':cucsGraphicsControllerSerial,'cucsGraphicsControllerThermal':cucsGraphicsControllerThermal,'cucsGraphicsControllerVendor':cucsGraphicsControllerVendor,'cucsGraphicsControllerVoltage':cucsGraphicsControllerVoltage,'cucsGraphicsControllerLocationDn':cucsGraphicsControllerLocationDn})