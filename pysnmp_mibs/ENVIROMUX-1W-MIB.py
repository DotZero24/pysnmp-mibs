_W='smAlertIndex'
_V='disconnected'
_U='dismissed'
_T='acknowledged'
_S='waitingAckDismiss'
_R='exitingCritical'
_Q='critical'
_P='enteringCritical'
_O='normal'
_N='alertIndex'
_M='ipDeviceIndex'
_L='digInputIndex'
_K='extSensorIndex'
_J='digInputValue'
_I='ipDeviceValue'
_H='not-accessible'
_G='Integer32'
_F='read-only'
_E='extSensorUnit'
_D='extSensorValue'
_C='alertStatus'
_B='current'
_A='ENVIROMUX-1W-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
enviromux1W=ModuleIdentity((1,3,6,1,4,1,3699,1,1,12))
if mibBuilder.loadTexts:enviromux1W.setRevisions(('2020-12-11 02:00','2020-08-18 14:00','2016-02-03 14:00'))
_Nti_ObjectIdentity=ObjectIdentity
nti=_Nti_ObjectIdentity((1,3,6,1,4,1,3699))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,3699,1))
_Hardware_ObjectIdentity=ObjectIdentity
hardware=_Hardware_ObjectIdentity((1,3,6,1,4,1,3699,1,1))
_MasterUnit_ObjectIdentity=ObjectIdentity
masterUnit=_MasterUnit_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1))
_ExtSensors_ObjectIdentity=ObjectIdentity
extSensors=_ExtSensors_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,2))
_ExtSensorTable_Object=MibTable
extSensorTable=_ExtSensorTable_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1))
if mibBuilder.loadTexts:extSensorTable.setStatus(_B)
_ExtSensorEntry_Object=MibTableRow
extSensorEntry=_ExtSensorEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1))
extSensorEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:extSensorEntry.setStatus(_B)
class _ExtSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_ExtSensorIndex_Type.__name__=_G
_ExtSensorIndex_Object=MibTableColumn
extSensorIndex=_ExtSensorIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,1),_ExtSensorIndex_Type())
extSensorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:extSensorIndex.setStatus(_B)
class _ExtSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,24)));namedValues=NamedValues(*(('undefined',0),('temperature',1),('humidity',2),('dewPoint',24)))
_ExtSensorType_Type.__name__=_G
_ExtSensorType_Object=MibTableColumn
extSensorType=_ExtSensorType_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,2),_ExtSensorType_Type())
extSensorType.setMaxAccess(_F)
if mibBuilder.loadTexts:extSensorType.setStatus(_B)
_ExtSensorDescription_Type=DisplayString
_ExtSensorDescription_Object=MibTableColumn
extSensorDescription=_ExtSensorDescription_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,3),_ExtSensorDescription_Type())
extSensorDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:extSensorDescription.setStatus(_B)
_ExtSensorValue_Type=Integer32
_ExtSensorValue_Object=MibTableColumn
extSensorValue=_ExtSensorValue_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,4),_ExtSensorValue_Type())
extSensorValue.setMaxAccess(_F)
if mibBuilder.loadTexts:extSensorValue.setStatus(_B)
class _ExtSensorUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ExtSensorUnit_Type.__name__=_G
_ExtSensorUnit_Object=MibTableColumn
extSensorUnit=_ExtSensorUnit_Object((1,3,6,1,4,1,3699,1,1,12,1,2,1,1,5),_ExtSensorUnit_Type())
extSensorUnit.setMaxAccess(_F)
if mibBuilder.loadTexts:extSensorUnit.setStatus(_B)
_DigInputs_ObjectIdentity=ObjectIdentity
digInputs=_DigInputs_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,3))
_DigInputTable_Object=MibTable
digInputTable=_DigInputTable_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1))
if mibBuilder.loadTexts:digInputTable.setStatus(_B)
_DigInputEntry_Object=MibTableRow
digInputEntry=_DigInputEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1,1))
digInputEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:digInputEntry.setStatus(_B)
class _DigInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DigInputIndex_Type.__name__=_G
_DigInputIndex_Object=MibTableColumn
digInputIndex=_DigInputIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1,1,1),_DigInputIndex_Type())
digInputIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:digInputIndex.setStatus(_B)
_DigInputDescription_Type=DisplayString
_DigInputDescription_Object=MibTableColumn
digInputDescription=_DigInputDescription_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1,1,2),_DigInputDescription_Type())
digInputDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:digInputDescription.setStatus(_B)
class _DigInputValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('closed',0),('open',1)))
_DigInputValue_Type.__name__=_G
_DigInputValue_Object=MibTableColumn
digInputValue=_DigInputValue_Object((1,3,6,1,4,1,3699,1,1,12,1,3,1,1,3),_DigInputValue_Type())
digInputValue.setMaxAccess(_F)
if mibBuilder.loadTexts:digInputValue.setStatus(_B)
_IpDevices_ObjectIdentity=ObjectIdentity
ipDevices=_IpDevices_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,4))
_IpDeviceTable_Object=MibTable
ipDeviceTable=_IpDeviceTable_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1))
if mibBuilder.loadTexts:ipDeviceTable.setStatus(_B)
_IpDeviceEntry_Object=MibTableRow
ipDeviceEntry=_IpDeviceEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1,1))
ipDeviceEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:ipDeviceEntry.setStatus(_B)
class _IpDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_IpDeviceIndex_Type.__name__=_G
_IpDeviceIndex_Object=MibTableColumn
ipDeviceIndex=_IpDeviceIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1,1,1),_IpDeviceIndex_Type())
ipDeviceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipDeviceIndex.setStatus(_B)
_IpDeviceDescription_Type=DisplayString
_IpDeviceDescription_Object=MibTableColumn
ipDeviceDescription=_IpDeviceDescription_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1,1,2),_IpDeviceDescription_Type())
ipDeviceDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:ipDeviceDescription.setStatus(_B)
class _IpDeviceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notResponding',0),('responding',1)))
_IpDeviceValue_Type.__name__=_G
_IpDeviceValue_Object=MibTableColumn
ipDeviceValue=_IpDeviceValue_Object((1,3,6,1,4,1,3699,1,1,12,1,4,1,1,3),_IpDeviceValue_Type())
ipDeviceValue.setMaxAccess(_F)
if mibBuilder.loadTexts:ipDeviceValue.setStatus(_B)
_EAlerts_ObjectIdentity=ObjectIdentity
eAlerts=_EAlerts_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,5))
_AlertTable_Object=MibTable
alertTable=_AlertTable_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1))
if mibBuilder.loadTexts:alertTable.setStatus(_B)
_AlertEntry_Object=MibTableRow
alertEntry=_AlertEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1))
alertEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:alertEntry.setStatus(_B)
class _AlertIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AlertIndex_Type.__name__=_G
_AlertIndex_Object=MibTableColumn
alertIndex=_AlertIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,1),_AlertIndex_Type())
alertIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alertIndex.setStatus(_B)
class _AlertEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_AlertEnabled_Type.__name__=_G
_AlertEnabled_Object=MibTableColumn
alertEnabled=_AlertEnabled_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,2),_AlertEnabled_Type())
alertEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:alertEnabled.setStatus(_B)
_AlertSensor_Type=DisplayString
_AlertSensor_Object=MibTableColumn
alertSensor=_AlertSensor_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,3),_AlertSensor_Type())
alertSensor.setMaxAccess(_F)
if mibBuilder.loadTexts:alertSensor.setStatus(_B)
_AlertSensorValue_Type=Integer32
_AlertSensorValue_Object=MibTableColumn
alertSensorValue=_AlertSensorValue_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,4),_AlertSensorValue_Type())
alertSensorValue.setMaxAccess(_F)
if mibBuilder.loadTexts:alertSensorValue.setStatus(_B)
_AlertThreshold_Type=Integer32
_AlertThreshold_Object=MibTableColumn
alertThreshold=_AlertThreshold_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,5),_AlertThreshold_Type())
alertThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:alertThreshold.setStatus(_B)
class _AlertThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('lessThan',0),('greaterThan',1)))
_AlertThresholdType_Type.__name__=_G
_AlertThresholdType_Object=MibTableColumn
alertThresholdType=_AlertThresholdType_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,6),_AlertThresholdType_Type())
alertThresholdType.setMaxAccess(_F)
if mibBuilder.loadTexts:alertThresholdType.setStatus(_B)
class _AlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7)))
_AlertStatus_Type.__name__=_G
_AlertStatus_Object=MibTableColumn
alertStatus=_AlertStatus_Object((1,3,6,1,4,1,3699,1,1,12,1,5,1,1,7),_AlertStatus_Type())
alertStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alertStatus.setStatus(_B)
_SmAlerts_ObjectIdentity=ObjectIdentity
smAlerts=_SmAlerts_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,1,6))
_SmAlertTable_Object=MibTable
smAlertTable=_SmAlertTable_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1))
if mibBuilder.loadTexts:smAlertTable.setStatus(_B)
_SmAlertEntry_Object=MibTableRow
smAlertEntry=_SmAlertEntry_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1,1))
smAlertEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:smAlertEntry.setStatus(_B)
class _SmAlertIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_SmAlertIndex_Type.__name__=_G
_SmAlertIndex_Object=MibTableColumn
smAlertIndex=_SmAlertIndex_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1,1,1),_SmAlertIndex_Type())
smAlertIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:smAlertIndex.setStatus(_B)
class _SmAlertEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_SmAlertEnabled_Type.__name__=_G
_SmAlertEnabled_Object=MibTableColumn
smAlertEnabled=_SmAlertEnabled_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1,1,2),_SmAlertEnabled_Type())
smAlertEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:smAlertEnabled.setStatus(_B)
class _SmAlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7)))
_SmAlertStatus_Type.__name__=_G
_SmAlertStatus_Object=MibTableColumn
smAlertStatus=_SmAlertStatus_Object((1,3,6,1,4,1,3699,1,1,12,1,6,1,1,3),_SmAlertStatus_Type())
smAlertStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:smAlertStatus.setStatus(_B)
_Enviromux1WTraps_ObjectIdentity=ObjectIdentity
enviromux1WTraps=_Enviromux1WTraps_ObjectIdentity((1,3,6,1,4,1,3699,1,1,12,100))
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
extSensor1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,1))
extSensor1Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor1Trap.setStatus(_B)
extSensor2Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,2))
extSensor2Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor2Trap.setStatus(_B)
extSensor3Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,3))
extSensor3Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor3Trap.setStatus(_B)
extSensor4Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,4))
extSensor4Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor4Trap.setStatus(_B)
extSensor5Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,5))
extSensor5Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor5Trap.setStatus(_B)
extSensor6Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,6))
extSensor6Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor6Trap.setStatus(_B)
extSensor7Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,7))
extSensor7Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor7Trap.setStatus(_B)
extSensor8Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,8))
extSensor8Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor8Trap.setStatus(_B)
extSensor9Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,9))
extSensor9Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor9Trap.setStatus(_B)
extSensor10Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,10))
extSensor10Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor10Trap.setStatus(_B)
extSensor11Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,11))
extSensor11Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor11Trap.setStatus(_B)
extSensor12Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,12))
extSensor12Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor12Trap.setStatus(_B)
extSensor13Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,13))
extSensor13Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor13Trap.setStatus(_B)
extSensor14Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,14))
extSensor14Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor14Trap.setStatus(_B)
extSensor15Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,15))
extSensor15Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor15Trap.setStatus(_B)
extSensor16Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,16))
extSensor16Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor16Trap.setStatus(_B)
extSensor17Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,17))
extSensor17Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor17Trap.setStatus(_B)
extSensor18Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,18))
extSensor18Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor18Trap.setStatus(_B)
extSensor19Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,19))
extSensor19Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor19Trap.setStatus(_B)
extSensor20Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,20))
extSensor20Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor20Trap.setStatus(_B)
extSensor21Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,21))
extSensor21Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor21Trap.setStatus(_B)
extSensor22Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,22))
extSensor22Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor22Trap.setStatus(_B)
extSensor23Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,23))
extSensor23Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor23Trap.setStatus(_B)
extSensor24Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,2,24))
extSensor24Trap.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:extSensor24Trap.setStatus(_B)
digInput1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,3,1))
digInput1Trap.setObjects(*((_A,_C),(_A,_J)))
if mibBuilder.loadTexts:digInput1Trap.setStatus(_B)
digInput2Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,3,2))
digInput2Trap.setObjects(*((_A,_C),(_A,_J)))
if mibBuilder.loadTexts:digInput2Trap.setStatus(_B)
ipDevice1Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,4,1))
ipDevice1Trap.setObjects(*((_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ipDevice1Trap.setStatus(_B)
ipDevice2Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,4,2))
ipDevice2Trap.setObjects(*((_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ipDevice2Trap.setStatus(_B)
ipDevice3Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,4,3))
ipDevice3Trap.setObjects(*((_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ipDevice3Trap.setStatus(_B)
ipDevice4Trap=NotificationType((1,3,6,1,4,1,3699,1,1,12,100,4,4))
ipDevice4Trap.setObjects(*((_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ipDevice4Trap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'nti':nti,'products':products,'hardware':hardware,'enviromux1W':enviromux1W,'masterUnit':masterUnit,'extSensors':extSensors,'extSensorTable':extSensorTable,'extSensorEntry':extSensorEntry,_K:extSensorIndex,'extSensorType':extSensorType,'extSensorDescription':extSensorDescription,_D:extSensorValue,_E:extSensorUnit,'digInputs':digInputs,'digInputTable':digInputTable,'digInputEntry':digInputEntry,_L:digInputIndex,'digInputDescription':digInputDescription,_J:digInputValue,'ipDevices':ipDevices,'ipDeviceTable':ipDeviceTable,'ipDeviceEntry':ipDeviceEntry,_M:ipDeviceIndex,'ipDeviceDescription':ipDeviceDescription,_I:ipDeviceValue,'eAlerts':eAlerts,'alertTable':alertTable,'alertEntry':alertEntry,_N:alertIndex,'alertEnabled':alertEnabled,'alertSensor':alertSensor,'alertSensorValue':alertSensorValue,'alertThreshold':alertThreshold,'alertThresholdType':alertThresholdType,_C:alertStatus,'smAlerts':smAlerts,'smAlertTable':smAlertTable,'smAlertEntry':smAlertEntry,_W:smAlertIndex,'smAlertEnabled':smAlertEnabled,'smAlertStatus':smAlertStatus,'enviromux1WTraps':enviromux1WTraps,'extSensorsTraps':extSensorsTraps,'extSensor1Trap':extSensor1Trap,'extSensor2Trap':extSensor2Trap,'extSensor3Trap':extSensor3Trap,'extSensor4Trap':extSensor4Trap,'extSensor5Trap':extSensor5Trap,'extSensor6Trap':extSensor6Trap,'extSensor7Trap':extSensor7Trap,'extSensor8Trap':extSensor8Trap,'extSensor9Trap':extSensor9Trap,'extSensor10Trap':extSensor10Trap,'extSensor11Trap':extSensor11Trap,'extSensor12Trap':extSensor12Trap,'extSensor13Trap':extSensor13Trap,'extSensor14Trap':extSensor14Trap,'extSensor15Trap':extSensor15Trap,'extSensor16Trap':extSensor16Trap,'extSensor17Trap':extSensor17Trap,'extSensor18Trap':extSensor18Trap,'extSensor19Trap':extSensor19Trap,'extSensor20Trap':extSensor20Trap,'extSensor21Trap':extSensor21Trap,'extSensor22Trap':extSensor22Trap,'extSensor23Trap':extSensor23Trap,'extSensor24Trap':extSensor24Trap,'digitalInputsTraps':digitalInputsTraps,'digInput1Trap':digInput1Trap,'digInput2Trap':digInput2Trap,'ipDevicesTraps':ipDevicesTraps,'ipDevice1Trap':ipDevice1Trap,'ipDevice2Trap':ipDevice2Trap,'ipDevice3Trap':ipDevice3Trap,'ipDevice4Trap':ipDevice4Trap,'otherProduct':otherProduct,'software':software})