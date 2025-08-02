_d='smAlertIndex'
_c='disconnected'
_b='dismissed'
_a='acknowledged'
_Z='waitingAckDismiss'
_Y='exitingCritical'
_X='critical'
_W='enteringCritical'
_V='normal'
_U='alertIndex'
_T='ipDeviceIndex'
_S='digInputIndex'
_R='extSensorIndex'
_Q='dewPoint'
_P='humidity'
_O='temperature'
_N='undefined'
_M='intSensorIndex'
_L='digInputValue'
_K='intSensorUnit'
_J='intSensorValue'
_I='ipDeviceValue'
_H='not-accessible'
_G='extSensorUnit'
_F='extSensorValue'
_E='alertStatus'
_D='Integer32'
_C='read-only'
_B='ENVIROMUXMICRO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
enviromuxMicro=ModuleIdentity((1,3,6,1,4,1,3699,1,1,12))
if mibBuilder.loadTexts:enviromuxMicro.setRevisions(('2022-07-22 14:00','2021-03-07 14:00','2015-09-27 14:00','2015-02-23 14:00','2014-11-25 14:00','2014-11-14 14:00'))
_Nti_ObjectIdentity=ObjectIdentity
nti=_Nti_ObjectIdentity((1,3,6,1,4,1,3699))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,3699,1))
_Hardware_ObjectIdentity=ObjectIdentity
hardware=_Hardware_ObjectIdentity((1,3,6,1,4,1,3699,1,1))
_MasterUnit_ObjectIdentity=ObjectIdentity
masterUnit=_MasterUnit_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1))
_IntSensors_ObjectIdentity=ObjectIdentity
intSensors=_IntSensors_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,1))
_IntSensorTable_Object=MibTable
intSensorTable=_IntSensorTable_Object((1,3,6,1,4,1,3699,1,1,12,1,1,1))
if mibBuilder.loadTexts:intSensorTable.setStatus(_A)
_IntSensorEntry_Object=MibTableRow
intSensorEntry=_IntSensorEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,1,1,1))
intSensorEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:intSensorEntry.setStatus(_A)
class _IntSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_IntSensorIndex_Type.__name__=_D
_IntSensorIndex_Object=MibTableColumn
intSensorIndex=_IntSensorIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,1,1,1,1),_IntSensorIndex_Type())
intSensorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:intSensorIndex.setStatus(_A)
class _IntSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,24)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,24)))
_IntSensorType_Type.__name__=_D
_IntSensorType_Object=MibTableColumn
intSensorType=_IntSensorType_Object((1,3,6,1,4,1,3699,1,1,12,1,1,1,1,2),_IntSensorType_Type())
intSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:intSensorType.setStatus(_A)
_IntSensorDescription_Type=DisplayString
_IntSensorDescription_Object=MibTableColumn
intSensorDescription=_IntSensorDescription_Object((1,3,6,1,4,1,3699,1,1,12,1,1,1,1,3),_IntSensorDescription_Type())
intSensorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:intSensorDescription.setStatus(_A)
_IntSensorValue_Type=Integer32
_IntSensorValue_Object=MibTableColumn
intSensorValue=_IntSensorValue_Object((1,3,6,1,4,1,3699,1,1,12,1,1,1,1,4),_IntSensorValue_Type())
intSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:intSensorValue.setStatus(_A)
class _IntSensorUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_IntSensorUnit_Type.__name__=_D
_IntSensorUnit_Object=MibTableColumn
intSensorUnit=_IntSensorUnit_Object((1,3,6,1,4,1,3699,1,1,12,1,1,1,1,5),_IntSensorUnit_Type())
intSensorUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:intSensorUnit.setStatus(_A)
_ExtSensors_ObjectIdentity=ObjectIdentity
extSensors=_ExtSensors_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,2))
_ExtSensorTable_Object=MibTable
extSensorTable=_ExtSensorTable_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1))
if mibBuilder.loadTexts:extSensorTable.setStatus(_A)
_ExtSensorEntry_Object=MibTableRow
extSensorEntry=_ExtSensorEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1))
extSensorEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:extSensorEntry.setStatus(_A)
class _ExtSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_ExtSensorIndex_Type.__name__=_D
_ExtSensorIndex_Object=MibTableColumn
extSensorIndex=_ExtSensorIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,1),_ExtSensorIndex_Type())
extSensorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:extSensorIndex.setStatus(_A)
class _ExtSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,24)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,24)))
_ExtSensorType_Type.__name__=_D
_ExtSensorType_Object=MibTableColumn
extSensorType=_ExtSensorType_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,2),_ExtSensorType_Type())
extSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:extSensorType.setStatus(_A)
_ExtSensorDescription_Type=DisplayString
_ExtSensorDescription_Object=MibTableColumn
extSensorDescription=_ExtSensorDescription_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,3),_ExtSensorDescription_Type())
extSensorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:extSensorDescription.setStatus(_A)
_ExtSensorValue_Type=Integer32
_ExtSensorValue_Object=MibTableColumn
extSensorValue=_ExtSensorValue_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,4),_ExtSensorValue_Type())
extSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:extSensorValue.setStatus(_A)
class _ExtSensorUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ExtSensorUnit_Type.__name__=_D
_ExtSensorUnit_Object=MibTableColumn
extSensorUnit=_ExtSensorUnit_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,5),_ExtSensorUnit_Type())
extSensorUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:extSensorUnit.setStatus(_A)
_DigInputs_ObjectIdentity=ObjectIdentity
digInputs=_DigInputs_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,3))
_DigInputTable_Object=MibTable
digInputTable=_DigInputTable_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1))
if mibBuilder.loadTexts:digInputTable.setStatus(_A)
_DigInputEntry_Object=MibTableRow
digInputEntry=_DigInputEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1,1))
digInputEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:digInputEntry.setStatus(_A)
class _DigInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DigInputIndex_Type.__name__=_D
_DigInputIndex_Object=MibTableColumn
digInputIndex=_DigInputIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1,1,1),_DigInputIndex_Type())
digInputIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:digInputIndex.setStatus(_A)
_DigInputDescription_Type=DisplayString
_DigInputDescription_Object=MibTableColumn
digInputDescription=_DigInputDescription_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1,1,2),_DigInputDescription_Type())
digInputDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:digInputDescription.setStatus(_A)
class _DigInputValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('closed',0),('open',1)))
_DigInputValue_Type.__name__=_D
_DigInputValue_Object=MibTableColumn
digInputValue=_DigInputValue_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1,1,3),_DigInputValue_Type())
digInputValue.setMaxAccess(_C)
if mibBuilder.loadTexts:digInputValue.setStatus(_A)
_IpDevices_ObjectIdentity=ObjectIdentity
ipDevices=_IpDevices_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,4))
_IpDeviceTable_Object=MibTable
ipDeviceTable=_IpDeviceTable_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1))
if mibBuilder.loadTexts:ipDeviceTable.setStatus(_A)
_IpDeviceEntry_Object=MibTableRow
ipDeviceEntry=_IpDeviceEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1,1))
ipDeviceEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:ipDeviceEntry.setStatus(_A)
class _IpDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_IpDeviceIndex_Type.__name__=_D
_IpDeviceIndex_Object=MibTableColumn
ipDeviceIndex=_IpDeviceIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1,1,1),_IpDeviceIndex_Type())
ipDeviceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipDeviceIndex.setStatus(_A)
_IpDeviceDescription_Type=DisplayString
_IpDeviceDescription_Object=MibTableColumn
ipDeviceDescription=_IpDeviceDescription_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1,1,2),_IpDeviceDescription_Type())
ipDeviceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ipDeviceDescription.setStatus(_A)
class _IpDeviceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notResponding',0),('responding',1)))
_IpDeviceValue_Type.__name__=_D
_IpDeviceValue_Object=MibTableColumn
ipDeviceValue=_IpDeviceValue_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1,1,3),_IpDeviceValue_Type())
ipDeviceValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ipDeviceValue.setStatus(_A)
_EAlerts_ObjectIdentity=ObjectIdentity
eAlerts=_EAlerts_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,5))
_AlertTable_Object=MibTable
alertTable=_AlertTable_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1))
if mibBuilder.loadTexts:alertTable.setStatus(_A)
_AlertEntry_Object=MibTableRow
alertEntry=_AlertEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1))
alertEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:alertEntry.setStatus(_A)
class _AlertIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AlertIndex_Type.__name__=_D
_AlertIndex_Object=MibTableColumn
alertIndex=_AlertIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,1),_AlertIndex_Type())
alertIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alertIndex.setStatus(_A)
class _AlertEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_AlertEnabled_Type.__name__=_D
_AlertEnabled_Object=MibTableColumn
alertEnabled=_AlertEnabled_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,2),_AlertEnabled_Type())
alertEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:alertEnabled.setStatus(_A)
_AlertSensor_Type=DisplayString
_AlertSensor_Object=MibTableColumn
alertSensor=_AlertSensor_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,3),_AlertSensor_Type())
alertSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:alertSensor.setStatus(_A)
_AlertSensorValue_Type=Integer32
_AlertSensorValue_Object=MibTableColumn
alertSensorValue=_AlertSensorValue_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,4),_AlertSensorValue_Type())
alertSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:alertSensorValue.setStatus(_A)
_AlertThreshold_Type=Integer32
_AlertThreshold_Object=MibTableColumn
alertThreshold=_AlertThreshold_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,5),_AlertThreshold_Type())
alertThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:alertThreshold.setStatus(_A)
class _AlertThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('lessThan',0),('greaterThan',1)))
_AlertThresholdType_Type.__name__=_D
_AlertThresholdType_Object=MibTableColumn
alertThresholdType=_AlertThresholdType_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,6),_AlertThresholdType_Type())
alertThresholdType.setMaxAccess(_C)
if mibBuilder.loadTexts:alertThresholdType.setStatus(_A)
class _AlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7)))
_AlertStatus_Type.__name__=_D
_AlertStatus_Object=MibTableColumn
alertStatus=_AlertStatus_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,7),_AlertStatus_Type())
alertStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alertStatus.setStatus(_A)
_AlertName_Type=DisplayString
_AlertName_Object=MibTableColumn
alertName=_AlertName_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,8),_AlertName_Type())
alertName.setMaxAccess(_C)
if mibBuilder.loadTexts:alertName.setStatus(_A)
_SmAlerts_ObjectIdentity=ObjectIdentity
smAlerts=_SmAlerts_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,6))
_SmAlertTable_Object=MibTable
smAlertTable=_SmAlertTable_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1))
if mibBuilder.loadTexts:smAlertTable.setStatus(_A)
_SmAlertEntry_Object=MibTableRow
smAlertEntry=_SmAlertEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1,1))
smAlertEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:smAlertEntry.setStatus(_A)
class _SmAlertIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_SmAlertIndex_Type.__name__=_D
_SmAlertIndex_Object=MibTableColumn
smAlertIndex=_SmAlertIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1,1,1),_SmAlertIndex_Type())
smAlertIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:smAlertIndex.setStatus(_A)
class _SmAlertEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_SmAlertEnabled_Type.__name__=_D
_SmAlertEnabled_Object=MibTableColumn
smAlertEnabled=_SmAlertEnabled_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1,1,2),_SmAlertEnabled_Type())
smAlertEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:smAlertEnabled.setStatus(_A)
class _SmAlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7)))
_SmAlertStatus_Type.__name__=_D
_SmAlertStatus_Object=MibTableColumn
smAlertStatus=_SmAlertStatus_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1,1,3),_SmAlertStatus_Type())
smAlertStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:smAlertStatus.setStatus(_A)
_HostSystem_ObjectIdentity=ObjectIdentity
hostSystem=_HostSystem_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,100))
_UnitName_Type=DisplayString
_UnitName_Object=MibScalar
unitName=_UnitName_Object((1,3,6,1,4,1,3699,1,1,12,1,100,1),_UnitName_Type())
unitName.setMaxAccess(_C)
if mibBuilder.loadTexts:unitName.setStatus(_A)
_DeviceModel_Type=DisplayString
_DeviceModel_Object=MibScalar
deviceModel=_DeviceModel_Object((1,3,6,1,4,1,3699,1,1,12,1,100,2),_DeviceModel_Type())
deviceModel.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceModel.setStatus(_A)
_SerialNumber_Type=DisplayString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,3699,1,1,12,1,100,3),_SerialNumber_Type())
serialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_FirmwareRevision_Type=DisplayString
_FirmwareRevision_Object=MibScalar
firmwareRevision=_FirmwareRevision_Object((1,3,6,1,4,1,3699,1,1,12,1,100,4),_FirmwareRevision_Type())
firmwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareRevision.setStatus(_A)
_SenderEmailAddress_Type=DisplayString
_SenderEmailAddress_Object=MibScalar
senderEmailAddress=_SenderEmailAddress_Object((1,3,6,1,4,1,3699,1,1,12,1,100,5),_SenderEmailAddress_Type())
senderEmailAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:senderEmailAddress.setStatus(_A)
_EnviromuxMicroTraps_ObjectIdentity=ObjectIdentity
enviromuxMicroTraps=_EnviromuxMicroTraps_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,100))
_IntSensorsTraps_ObjectIdentity=ObjectIdentity
intSensorsTraps=_IntSensorsTraps_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,100,1))
_ExtSensorsTraps_ObjectIdentity=ObjectIdentity
extSensorsTraps=_ExtSensorsTraps_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,100,2))
_DigitalInputsTraps_ObjectIdentity=ObjectIdentity
digitalInputsTraps=_DigitalInputsTraps_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,100,3))
_IpDevicesTraps_ObjectIdentity=ObjectIdentity
ipDevicesTraps=_IpDevicesTraps_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,100,4))
_OtherProduct_ObjectIdentity=ObjectIdentity
otherProduct=_OtherProduct_ObjectIdentity((1,3,6,1,4,1,3699,1,1,200))
_Software_ObjectIdentity=ObjectIdentity
software=_Software_ObjectIdentity((1,3,6,1,4,1,3699,1,2))
intSensor1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,1,1))
intSensor1Trap.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:intSensor1Trap.setStatus(_A)
intSensor2Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,1,2))
intSensor2Trap.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:intSensor2Trap.setStatus(_A)
intSensor3Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,1,3))
intSensor3Trap.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:intSensor3Trap.setStatus(_A)
extSensor1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,1))
extSensor1Trap.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:extSensor1Trap.setStatus(_A)
extSensor2Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,2))
extSensor2Trap.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:extSensor2Trap.setStatus(_A)
extSensor3Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,3))
extSensor3Trap.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:extSensor3Trap.setStatus(_A)
extSensor4Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,4))
extSensor4Trap.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:extSensor4Trap.setStatus(_A)
extSensor5Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,5))
extSensor5Trap.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:extSensor5Trap.setStatus(_A)
extSensor6Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,6))
extSensor6Trap.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:extSensor6Trap.setStatus(_A)
digInput1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,3,1))
digInput1Trap.setObjects(*((_B,_E),(_B,_L)))
if mibBuilder.loadTexts:digInput1Trap.setStatus(_A)
digInpu21Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,3,2))
digInpu21Trap.setObjects(*((_B,_E),(_B,_L)))
if mibBuilder.loadTexts:digInpu21Trap.setStatus(_A)
ipDevice1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,4,1))
ipDevice1Trap.setObjects(*((_B,_E),(_B,_I)))
if mibBuilder.loadTexts:ipDevice1Trap.setStatus(_A)
ipDevice2Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,4,2))
ipDevice2Trap.setObjects(*((_B,_E),(_B,_I)))
if mibBuilder.loadTexts:ipDevice2Trap.setStatus(_A)
ipDevice3Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,4,3))
ipDevice3Trap.setObjects(*((_B,_E),(_B,_I)))
if mibBuilder.loadTexts:ipDevice3Trap.setStatus(_A)
ipDevice4Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,4,4))
ipDevice4Trap.setObjects(*((_B,_E),(_B,_I)))
if mibBuilder.loadTexts:ipDevice4Trap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nti':nti,'products':products,'hardware':hardware,'enviromuxMicro':enviromuxMicro,'masterUnit':masterUnit,'intSensors':intSensors,'intSensorTable':intSensorTable,'intSensorEntry':intSensorEntry,_M:intSensorIndex,'intSensorType':intSensorType,'intSensorDescription':intSensorDescription,_J:intSensorValue,_K:intSensorUnit,'extSensors':extSensors,'extSensorTable':extSensorTable,'extSensorEntry':extSensorEntry,_R:extSensorIndex,'extSensorType':extSensorType,'extSensorDescription':extSensorDescription,_F:extSensorValue,_G:extSensorUnit,'digInputs':digInputs,'digInputTable':digInputTable,'digInputEntry':digInputEntry,_S:digInputIndex,'digInputDescription':digInputDescription,_L:digInputValue,'ipDevices':ipDevices,'ipDeviceTable':ipDeviceTable,'ipDeviceEntry':ipDeviceEntry,_T:ipDeviceIndex,'ipDeviceDescription':ipDeviceDescription,_I:ipDeviceValue,'eAlerts':eAlerts,'alertTable':alertTable,'alertEntry':alertEntry,_U:alertIndex,'alertEnabled':alertEnabled,'alertSensor':alertSensor,'alertSensorValue':alertSensorValue,'alertThreshold':alertThreshold,'alertThresholdType':alertThresholdType,_E:alertStatus,'alertName':alertName,'smAlerts':smAlerts,'smAlertTable':smAlertTable,'smAlertEntry':smAlertEntry,_d:smAlertIndex,'smAlertEnabled':smAlertEnabled,'smAlertStatus':smAlertStatus,'hostSystem':hostSystem,'unitName':unitName,'deviceModel':deviceModel,'serialNumber':serialNumber,'firmwareRevision':firmwareRevision,'senderEmailAddress':senderEmailAddress,'enviromuxMicroTraps':enviromuxMicroTraps,'intSensorsTraps':intSensorsTraps,'intSensor1Trap':intSensor1Trap,'intSensor2Trap':intSensor2Trap,'intSensor3Trap':intSensor3Trap,'extSensorsTraps':extSensorsTraps,'extSensor1Trap':extSensor1Trap,'extSensor2Trap':extSensor2Trap,'extSensor3Trap':extSensor3Trap,'extSensor4Trap':extSensor4Trap,'extSensor5Trap':extSensor5Trap,'extSensor6Trap':extSensor6Trap,'digitalInputsTraps':digitalInputsTraps,'digInput1Trap':digInput1Trap,'digInpu21Trap':digInpu21Trap,'ipDevicesTraps':ipDevicesTraps,'ipDevice1Trap':ipDevice1Trap,'ipDevice2Trap':ipDevice2Trap,'ipDevice3Trap':ipDevice3Trap,'ipDevice4Trap':ipDevice4Trap,'otherProduct':otherProduct,'software':software})