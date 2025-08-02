_Z='NotificationType'
_Y='sensor4-3'
_X='sensor3-3'
_W='sensor2-3'
_V='sensor2-2'
_U='sensor4-2'
_T='sensor3-2'
_S='sensor2-1'
_R='alarmMessage2'
_Q='alarmMessage4'
_P='alarmMessage3'
_O='sensor1-8'
_N='sensor1-7'
_M='sensor1-6'
_L='sensor1-5'
_K='sensor1-4'
_J='sensor1-3'
_I='sensor1-2'
_H='sensor1-1'
_G='sensor4-1'
_F='sensor3-1'
_E='alarmMessage1'
_D='Integer32'
_C='mandatory'
_B='read-only'
_A='ROOMALERT11E-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_Z,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Z,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Avtech_ObjectIdentity=ObjectIdentity
avtech=_Avtech_ObjectIdentity((1,3,6,1,4,1,20916))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,20916,1))
_Roomalert11E_ObjectIdentity=ObjectIdentity
roomalert11E=_Roomalert11E_ObjectIdentity((1,3,6,1,4,1,20916,1,3))
_Sensors_ObjectIdentity=ObjectIdentity
sensors=_Sensors_ObjectIdentity((1,3,6,1,4,1,20916,1,3,1))
_Channel1_ObjectIdentity=ObjectIdentity
channel1=_Channel1_ObjectIdentity((1,3,6,1,4,1,20916,1,3,1,1))
class _Sensor1_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sensor1_1_Type.__name__=_D
_Sensor1_1_Object=MibScalar
sensor1_1=_Sensor1_1_Object((1,3,6,1,4,1,20916,1,3,1,1,1),_Sensor1_1_Type())
sensor1_1.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor1_1.setStatus(_C)
class _Sensor1_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sensor1_2_Type.__name__=_D
_Sensor1_2_Object=MibScalar
sensor1_2=_Sensor1_2_Object((1,3,6,1,4,1,20916,1,3,1,1,2),_Sensor1_2_Type())
sensor1_2.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor1_2.setStatus(_C)
class _Sensor1_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sensor1_3_Type.__name__=_D
_Sensor1_3_Object=MibScalar
sensor1_3=_Sensor1_3_Object((1,3,6,1,4,1,20916,1,3,1,1,3),_Sensor1_3_Type())
sensor1_3.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor1_3.setStatus(_C)
class _Sensor1_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sensor1_4_Type.__name__=_D
_Sensor1_4_Object=MibScalar
sensor1_4=_Sensor1_4_Object((1,3,6,1,4,1,20916,1,3,1,1,4),_Sensor1_4_Type())
sensor1_4.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor1_4.setStatus(_C)
class _Sensor1_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sensor1_5_Type.__name__=_D
_Sensor1_5_Object=MibScalar
sensor1_5=_Sensor1_5_Object((1,3,6,1,4,1,20916,1,3,1,1,5),_Sensor1_5_Type())
sensor1_5.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor1_5.setStatus(_C)
class _Sensor1_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sensor1_6_Type.__name__=_D
_Sensor1_6_Object=MibScalar
sensor1_6=_Sensor1_6_Object((1,3,6,1,4,1,20916,1,3,1,1,6),_Sensor1_6_Type())
sensor1_6.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor1_6.setStatus(_C)
class _Sensor1_7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sensor1_7_Type.__name__=_D
_Sensor1_7_Object=MibScalar
sensor1_7=_Sensor1_7_Object((1,3,6,1,4,1,20916,1,3,1,1,7),_Sensor1_7_Type())
sensor1_7.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor1_7.setStatus(_C)
class _Sensor1_8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sensor1_8_Type.__name__=_D
_Sensor1_8_Object=MibScalar
sensor1_8=_Sensor1_8_Object((1,3,6,1,4,1,20916,1,3,1,1,8),_Sensor1_8_Type())
sensor1_8.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor1_8.setStatus(_C)
_Switch_label_1_Type=OctetString
_Switch_label_1_Object=MibScalar
switch_label_1=_Switch_label_1_Object((1,3,6,1,4,1,20916,1,3,1,1,9),_Switch_label_1_Type())
switch_label_1.setMaxAccess(_B)
if mibBuilder.loadTexts:switch_label_1.setStatus(_C)
_Switch_label_2_Type=OctetString
_Switch_label_2_Object=MibScalar
switch_label_2=_Switch_label_2_Object((1,3,6,1,4,1,20916,1,3,1,1,10),_Switch_label_2_Type())
switch_label_2.setMaxAccess(_B)
if mibBuilder.loadTexts:switch_label_2.setStatus(_C)
_Switch_label_3_Type=OctetString
_Switch_label_3_Object=MibScalar
switch_label_3=_Switch_label_3_Object((1,3,6,1,4,1,20916,1,3,1,1,11),_Switch_label_3_Type())
switch_label_3.setMaxAccess(_B)
if mibBuilder.loadTexts:switch_label_3.setStatus(_C)
_Switch_label_4_Type=OctetString
_Switch_label_4_Object=MibScalar
switch_label_4=_Switch_label_4_Object((1,3,6,1,4,1,20916,1,3,1,1,12),_Switch_label_4_Type())
switch_label_4.setMaxAccess(_B)
if mibBuilder.loadTexts:switch_label_4.setStatus(_C)
_Switch_label_5_Type=OctetString
_Switch_label_5_Object=MibScalar
switch_label_5=_Switch_label_5_Object((1,3,6,1,4,1,20916,1,3,1,1,13),_Switch_label_5_Type())
switch_label_5.setMaxAccess(_B)
if mibBuilder.loadTexts:switch_label_5.setStatus(_C)
_Switch_label_6_Type=OctetString
_Switch_label_6_Object=MibScalar
switch_label_6=_Switch_label_6_Object((1,3,6,1,4,1,20916,1,3,1,1,14),_Switch_label_6_Type())
switch_label_6.setMaxAccess(_B)
if mibBuilder.loadTexts:switch_label_6.setStatus(_C)
_Switch_label_7_Type=OctetString
_Switch_label_7_Object=MibScalar
switch_label_7=_Switch_label_7_Object((1,3,6,1,4,1,20916,1,3,1,1,15),_Switch_label_7_Type())
switch_label_7.setMaxAccess(_B)
if mibBuilder.loadTexts:switch_label_7.setStatus(_C)
_Switch_label_8_Type=OctetString
_Switch_label_8_Object=MibScalar
switch_label_8=_Switch_label_8_Object((1,3,6,1,4,1,20916,1,3,1,1,16),_Switch_label_8_Type())
switch_label_8.setMaxAccess(_B)
if mibBuilder.loadTexts:switch_label_8.setStatus(_C)
_Channel2_ObjectIdentity=ObjectIdentity
channel2=_Channel2_ObjectIdentity((1,3,6,1,4,1,20916,1,3,1,2))
class _Sensor2_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor2_1_Type.__name__=_D
_Sensor2_1_Object=MibScalar
sensor2_1=_Sensor2_1_Object((1,3,6,1,4,1,20916,1,3,1,2,1),_Sensor2_1_Type())
sensor2_1.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor2_1.setStatus(_C)
class _Sensor2_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor2_2_Type.__name__=_D
_Sensor2_2_Object=MibScalar
sensor2_2=_Sensor2_2_Object((1,3,6,1,4,1,20916,1,3,1,2,2),_Sensor2_2_Type())
sensor2_2.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor2_2.setStatus(_C)
class _Sensor2_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor2_3_Type.__name__=_D
_Sensor2_3_Object=MibScalar
sensor2_3=_Sensor2_3_Object((1,3,6,1,4,1,20916,1,3,1,2,3),_Sensor2_3_Type())
sensor2_3.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor2_3.setStatus(_C)
class _Sensor2_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor2_4_Type.__name__=_D
_Sensor2_4_Object=MibScalar
sensor2_4=_Sensor2_4_Object((1,3,6,1,4,1,20916,1,3,1,2,4),_Sensor2_4_Type())
sensor2_4.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor2_4.setStatus(_C)
class _Sensor2_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor2_5_Type.__name__=_D
_Sensor2_5_Object=MibScalar
sensor2_5=_Sensor2_5_Object((1,3,6,1,4,1,20916,1,3,1,2,5),_Sensor2_5_Type())
sensor2_5.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor2_5.setStatus(_C)
_Sensor2_6_label_Type=OctetString
_Sensor2_6_label_Object=MibScalar
sensor2_6_label=_Sensor2_6_label_Object((1,3,6,1,4,1,20916,1,3,1,2,6),_Sensor2_6_label_Type())
sensor2_6_label.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor2_6_label.setStatus(_C)
_Channel3_ObjectIdentity=ObjectIdentity
channel3=_Channel3_ObjectIdentity((1,3,6,1,4,1,20916,1,3,1,3))
class _Sensor3_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor3_1_Type.__name__=_D
_Sensor3_1_Object=MibScalar
sensor3_1=_Sensor3_1_Object((1,3,6,1,4,1,20916,1,3,1,3,1),_Sensor3_1_Type())
sensor3_1.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor3_1.setStatus(_C)
class _Sensor3_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor3_2_Type.__name__=_D
_Sensor3_2_Object=MibScalar
sensor3_2=_Sensor3_2_Object((1,3,6,1,4,1,20916,1,3,1,3,2),_Sensor3_2_Type())
sensor3_2.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor3_2.setStatus(_C)
class _Sensor3_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor3_3_Type.__name__=_D
_Sensor3_3_Object=MibScalar
sensor3_3=_Sensor3_3_Object((1,3,6,1,4,1,20916,1,3,1,3,3),_Sensor3_3_Type())
sensor3_3.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor3_3.setStatus(_C)
class _Sensor3_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor3_4_Type.__name__=_D
_Sensor3_4_Object=MibScalar
sensor3_4=_Sensor3_4_Object((1,3,6,1,4,1,20916,1,3,1,3,4),_Sensor3_4_Type())
sensor3_4.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor3_4.setStatus(_C)
class _Sensor3_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor3_5_Type.__name__=_D
_Sensor3_5_Object=MibScalar
sensor3_5=_Sensor3_5_Object((1,3,6,1,4,1,20916,1,3,1,3,5),_Sensor3_5_Type())
sensor3_5.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor3_5.setStatus(_C)
_Sensor3_6_label_Type=OctetString
_Sensor3_6_label_Object=MibScalar
sensor3_6_label=_Sensor3_6_label_Object((1,3,6,1,4,1,20916,1,3,1,3,6),_Sensor3_6_label_Type())
sensor3_6_label.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor3_6_label.setStatus(_C)
_Channel4_ObjectIdentity=ObjectIdentity
channel4=_Channel4_ObjectIdentity((1,3,6,1,4,1,20916,1,3,1,4))
class _Sensor4_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor4_1_Type.__name__=_D
_Sensor4_1_Object=MibScalar
sensor4_1=_Sensor4_1_Object((1,3,6,1,4,1,20916,1,3,1,4,1),_Sensor4_1_Type())
sensor4_1.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor4_1.setStatus(_C)
class _Sensor4_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor4_2_Type.__name__=_D
_Sensor4_2_Object=MibScalar
sensor4_2=_Sensor4_2_Object((1,3,6,1,4,1,20916,1,3,1,4,2),_Sensor4_2_Type())
sensor4_2.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor4_2.setStatus(_C)
class _Sensor4_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor4_3_Type.__name__=_D
_Sensor4_3_Object=MibScalar
sensor4_3=_Sensor4_3_Object((1,3,6,1,4,1,20916,1,3,1,4,3),_Sensor4_3_Type())
sensor4_3.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor4_3.setStatus(_C)
class _Sensor4_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor4_4_Type.__name__=_D
_Sensor4_4_Object=MibScalar
sensor4_4=_Sensor4_4_Object((1,3,6,1,4,1,20916,1,3,1,4,4),_Sensor4_4_Type())
sensor4_4.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor4_4.setStatus(_C)
class _Sensor4_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sensor4_5_Type.__name__=_D
_Sensor4_5_Object=MibScalar
sensor4_5=_Sensor4_5_Object((1,3,6,1,4,1,20916,1,3,1,4,5),_Sensor4_5_Type())
sensor4_5.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor4_5.setStatus(_C)
_Sensor4_6_label_Type=OctetString
_Sensor4_6_label_Object=MibScalar
sensor4_6_label=_Sensor4_6_label_Object((1,3,6,1,4,1,20916,1,3,1,4,6),_Sensor4_6_label_Type())
sensor4_6_label.setMaxAccess(_B)
if mibBuilder.loadTexts:sensor4_6_label.setStatus(_C)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,20916,1,3,2))
class _Alarm1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Alarm1_Type.__name__=_D
_Alarm1_Object=MibScalar
alarm1=_Alarm1_Object((1,3,6,1,4,1,20916,1,3,2,1),_Alarm1_Type())
alarm1.setMaxAccess(_B)
if mibBuilder.loadTexts:alarm1.setStatus(_C)
class _Alarm2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Alarm2_Type.__name__=_D
_Alarm2_Object=MibScalar
alarm2=_Alarm2_Object((1,3,6,1,4,1,20916,1,3,2,2),_Alarm2_Type())
alarm2.setMaxAccess(_B)
if mibBuilder.loadTexts:alarm2.setStatus(_C)
class _Alarm3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Alarm3_Type.__name__=_D
_Alarm3_Object=MibScalar
alarm3=_Alarm3_Object((1,3,6,1,4,1,20916,1,3,2,3),_Alarm3_Type())
alarm3.setMaxAccess(_B)
if mibBuilder.loadTexts:alarm3.setStatus(_C)
class _Alarm4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Alarm4_Type.__name__=_D
_Alarm4_Object=MibScalar
alarm4=_Alarm4_Object((1,3,6,1,4,1,20916,1,3,2,4),_Alarm4_Type())
alarm4.setMaxAccess(_B)
if mibBuilder.loadTexts:alarm4.setStatus(_C)
_AlarmMessage1_Type=OctetString
_AlarmMessage1_Object=MibScalar
alarmMessage1=_AlarmMessage1_Object((1,3,6,1,4,1,20916,1,3,2,5),_AlarmMessage1_Type())
alarmMessage1.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmMessage1.setStatus(_C)
_AlarmMessage2_Type=OctetString
_AlarmMessage2_Object=MibScalar
alarmMessage2=_AlarmMessage2_Object((1,3,6,1,4,1,20916,1,3,2,6),_AlarmMessage2_Type())
alarmMessage2.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmMessage2.setStatus(_C)
_AlarmMessage3_Type=OctetString
_AlarmMessage3_Object=MibScalar
alarmMessage3=_AlarmMessage3_Object((1,3,6,1,4,1,20916,1,3,2,7),_AlarmMessage3_Type())
alarmMessage3.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmMessage3.setStatus(_C)
_AlarmMessage4_Type=OctetString
_AlarmMessage4_Object=MibScalar
alarmMessage4=_AlarmMessage4_Object((1,3,6,1,4,1,20916,1,3,2,8),_AlarmMessage4_Type())
alarmMessage4.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmMessage4.setStatus(_C)
_Thresholds_ObjectIdentity=ObjectIdentity
thresholds=_Thresholds_ObjectIdentity((1,3,6,1,4,1,20916,1,3,3))
_Channels_ObjectIdentity=ObjectIdentity
channels=_Channels_ObjectIdentity((1,3,6,1,4,1,20916,1,3,3,1))
_Channels1_ObjectIdentity=ObjectIdentity
channels1=_Channels1_ObjectIdentity((1,3,6,1,4,1,20916,1,3,3,1,1))
class _Threshold1_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold1_1_Type.__name__=_D
_Threshold1_1_Object=MibScalar
threshold1_1=_Threshold1_1_Object((1,3,6,1,4,1,20916,1,3,3,1,1,1),_Threshold1_1_Type())
threshold1_1.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold1_1.setStatus(_C)
class _Threshold1_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold1_2_Type.__name__=_D
_Threshold1_2_Object=MibScalar
threshold1_2=_Threshold1_2_Object((1,3,6,1,4,1,20916,1,3,3,1,1,2),_Threshold1_2_Type())
threshold1_2.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold1_2.setStatus(_C)
class _Threshold1_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold1_3_Type.__name__=_D
_Threshold1_3_Object=MibScalar
threshold1_3=_Threshold1_3_Object((1,3,6,1,4,1,20916,1,3,3,1,1,3),_Threshold1_3_Type())
threshold1_3.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold1_3.setStatus(_C)
class _Threshold1_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold1_4_Type.__name__=_D
_Threshold1_4_Object=MibScalar
threshold1_4=_Threshold1_4_Object((1,3,6,1,4,1,20916,1,3,3,1,1,4),_Threshold1_4_Type())
threshold1_4.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold1_4.setStatus(_C)
class _Threshold1_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold1_5_Type.__name__=_D
_Threshold1_5_Object=MibScalar
threshold1_5=_Threshold1_5_Object((1,3,6,1,4,1,20916,1,3,3,1,1,5),_Threshold1_5_Type())
threshold1_5.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold1_5.setStatus(_C)
class _Threshold1_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold1_6_Type.__name__=_D
_Threshold1_6_Object=MibScalar
threshold1_6=_Threshold1_6_Object((1,3,6,1,4,1,20916,1,3,3,1,1,6),_Threshold1_6_Type())
threshold1_6.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold1_6.setStatus(_C)
class _Threshold1_7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold1_7_Type.__name__=_D
_Threshold1_7_Object=MibScalar
threshold1_7=_Threshold1_7_Object((1,3,6,1,4,1,20916,1,3,3,1,1,7),_Threshold1_7_Type())
threshold1_7.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold1_7.setStatus(_C)
class _Threshold1_8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold1_8_Type.__name__=_D
_Threshold1_8_Object=MibScalar
threshold1_8=_Threshold1_8_Object((1,3,6,1,4,1,20916,1,3,3,1,1,8),_Threshold1_8_Type())
threshold1_8.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold1_8.setStatus(_C)
_Channels2_ObjectIdentity=ObjectIdentity
channels2=_Channels2_ObjectIdentity((1,3,6,1,4,1,20916,1,3,3,1,2))
class _Threshold2_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold2_1_Type.__name__=_D
_Threshold2_1_Object=MibScalar
threshold2_1=_Threshold2_1_Object((1,3,6,1,4,1,20916,1,3,3,1,2,1),_Threshold2_1_Type())
threshold2_1.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold2_1.setStatus(_C)
class _Threshold2_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold2_2_Type.__name__=_D
_Threshold2_2_Object=MibScalar
threshold2_2=_Threshold2_2_Object((1,3,6,1,4,1,20916,1,3,3,1,2,2),_Threshold2_2_Type())
threshold2_2.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold2_2.setStatus(_C)
class _Threshold2_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold2_3_Type.__name__=_D
_Threshold2_3_Object=MibScalar
threshold2_3=_Threshold2_3_Object((1,3,6,1,4,1,20916,1,3,3,1,2,3),_Threshold2_3_Type())
threshold2_3.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold2_3.setStatus(_C)
class _Threshold2_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold2_4_Type.__name__=_D
_Threshold2_4_Object=MibScalar
threshold2_4=_Threshold2_4_Object((1,3,6,1,4,1,20916,1,3,3,1,2,4),_Threshold2_4_Type())
threshold2_4.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold2_4.setStatus(_C)
_Channels3_ObjectIdentity=ObjectIdentity
channels3=_Channels3_ObjectIdentity((1,3,6,1,4,1,20916,1,3,3,1,3))
class _Threshold3_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold3_1_Type.__name__=_D
_Threshold3_1_Object=MibScalar
threshold3_1=_Threshold3_1_Object((1,3,6,1,4,1,20916,1,3,3,1,3,1),_Threshold3_1_Type())
threshold3_1.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold3_1.setStatus(_C)
class _Threshold3_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold3_2_Type.__name__=_D
_Threshold3_2_Object=MibScalar
threshold3_2=_Threshold3_2_Object((1,3,6,1,4,1,20916,1,3,3,1,3,2),_Threshold3_2_Type())
threshold3_2.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold3_2.setStatus(_C)
class _Threshold3_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold3_3_Type.__name__=_D
_Threshold3_3_Object=MibScalar
threshold3_3=_Threshold3_3_Object((1,3,6,1,4,1,20916,1,3,3,1,3,3),_Threshold3_3_Type())
threshold3_3.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold3_3.setStatus(_C)
class _Threshold3_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold3_4_Type.__name__=_D
_Threshold3_4_Object=MibScalar
threshold3_4=_Threshold3_4_Object((1,3,6,1,4,1,20916,1,3,3,1,3,4),_Threshold3_4_Type())
threshold3_4.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold3_4.setStatus(_C)
_Channels4_ObjectIdentity=ObjectIdentity
channels4=_Channels4_ObjectIdentity((1,3,6,1,4,1,20916,1,3,3,1,4))
class _Threshold4_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold4_1_Type.__name__=_D
_Threshold4_1_Object=MibScalar
threshold4_1=_Threshold4_1_Object((1,3,6,1,4,1,20916,1,3,3,1,4,1),_Threshold4_1_Type())
threshold4_1.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold4_1.setStatus(_C)
class _Threshold4_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold4_2_Type.__name__=_D
_Threshold4_2_Object=MibScalar
threshold4_2=_Threshold4_2_Object((1,3,6,1,4,1,20916,1,3,3,1,4,2),_Threshold4_2_Type())
threshold4_2.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold4_2.setStatus(_C)
class _Threshold4_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold4_3_Type.__name__=_D
_Threshold4_3_Object=MibScalar
threshold4_3=_Threshold4_3_Object((1,3,6,1,4,1,20916,1,3,3,1,4,3),_Threshold4_3_Type())
threshold4_3.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold4_3.setStatus(_C)
class _Threshold4_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Threshold4_4_Type.__name__=_D
_Threshold4_4_Object=MibScalar
threshold4_4=_Threshold4_4_Object((1,3,6,1,4,1,20916,1,3,3,1,4,4),_Threshold4_4_Type())
threshold4_4.setMaxAccess(_B)
if mibBuilder.loadTexts:threshold4_4.setStatus(_C)
tempAlarm1_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,1))
tempAlarm1_11e.setObjects(*((_A,_R),(_A,_S),(_A,_V),(_A,_S)))
if mibBuilder.loadTexts:tempAlarm1_11e.setStatus('')
room_alert_11E_SNMP_trap=NotificationType((1,3,6,1,4,1,20916,1,3,0,2))
room_alert_11E_SNMP_trap.setObjects(*((_A,_E),(_A,_R),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:room_alert_11E_SNMP_trap.setStatus('')
tempAlarm2_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,3))
tempAlarm2_11e.setObjects(*((_A,_P),(_A,_F),(_A,_T),(_A,_F)))
if mibBuilder.loadTexts:tempAlarm2_11e.setStatus('')
tempClear2_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,4))
tempClear2_11e.setObjects(*((_A,_P),(_A,_F),(_A,_T),(_A,_F)))
if mibBuilder.loadTexts:tempClear2_11e.setStatus('')
tempAlarm3_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,5))
tempAlarm3_11e.setObjects(*((_A,_Q),(_A,_G),(_A,_U),(_A,_G)))
if mibBuilder.loadTexts:tempAlarm3_11e.setStatus('')
tempClear3_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,6))
tempClear3_11e.setObjects(*((_A,_Q),(_A,_G),(_A,_U),(_A,_G)))
if mibBuilder.loadTexts:tempClear3_11e.setStatus('')
humidityAlarm1_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,7))
humidityAlarm1_11e.setObjects(*((_A,_R),(_A,_S),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:humidityAlarm1_11e.setStatus('')
humidityClear1_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,8))
humidityClear1_11e.setObjects(*((_A,_R),(_A,_S),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:humidityClear1_11e.setStatus('')
humidityAlarm2_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,9))
humidityAlarm2_11e.setObjects(*((_A,_P),(_A,_F),(_A,_T),(_A,_X)))
if mibBuilder.loadTexts:humidityAlarm2_11e.setStatus('')
humidityClear2_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,10))
humidityClear2_11e.setObjects(*((_A,_P),(_A,_F),(_A,_T),(_A,_X)))
if mibBuilder.loadTexts:humidityClear2_11e.setStatus('')
humidityAlarm3_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,11))
humidityAlarm3_11e.setObjects(*((_A,_Q),(_A,_G),(_A,_U),(_A,_Y)))
if mibBuilder.loadTexts:humidityAlarm3_11e.setStatus('')
humidityClear3_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,12))
humidityClear3_11e.setObjects(*((_A,_Q),(_A,_G),(_A,_U),(_A,_Y)))
if mibBuilder.loadTexts:humidityClear3_11e.setStatus('')
switchAlarm1_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,13))
switchAlarm1_11e.setObjects(*((_A,_E),(_A,_H),(_A,_H),(_A,_H)))
if mibBuilder.loadTexts:switchAlarm1_11e.setStatus('')
switchClear1_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,14))
switchClear1_11e.setObjects(*((_A,_E),(_A,_H),(_A,_H),(_A,_H)))
if mibBuilder.loadTexts:switchClear1_11e.setStatus('')
switchAlarm2_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,15))
switchAlarm2_11e.setObjects(*((_A,_E),(_A,_I),(_A,_I),(_A,_I)))
if mibBuilder.loadTexts:switchAlarm2_11e.setStatus('')
switchClear2_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,16))
switchClear2_11e.setObjects(*((_A,_E),(_A,_I),(_A,_I),(_A,_I)))
if mibBuilder.loadTexts:switchClear2_11e.setStatus('')
switchAlarm3_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,17))
switchAlarm3_11e.setObjects(*((_A,_E),(_A,_J),(_A,_J),(_A,_J)))
if mibBuilder.loadTexts:switchAlarm3_11e.setStatus('')
switchClear3_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,18))
switchClear3_11e.setObjects(*((_A,_E),(_A,_J),(_A,_J),(_A,_J)))
if mibBuilder.loadTexts:switchClear3_11e.setStatus('')
switchAlarm4_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,19))
switchAlarm4_11e.setObjects(*((_A,_E),(_A,_K),(_A,_K),(_A,_K)))
if mibBuilder.loadTexts:switchAlarm4_11e.setStatus('')
switchClear4_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,20))
switchClear4_11e.setObjects(*((_A,_E),(_A,_K),(_A,_K),(_A,_K)))
if mibBuilder.loadTexts:switchClear4_11e.setStatus('')
switchAlarm5_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,21))
switchAlarm5_11e.setObjects(*((_A,_E),(_A,_L),(_A,_L),(_A,_L)))
if mibBuilder.loadTexts:switchAlarm5_11e.setStatus('')
switchClear5_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,22))
switchClear5_11e.setObjects(*((_A,_E),(_A,_L),(_A,_L),(_A,_L)))
if mibBuilder.loadTexts:switchClear5_11e.setStatus('')
switchAlarm6_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,23))
switchAlarm6_11e.setObjects(*((_A,_E),(_A,_M),(_A,_M),(_A,_M)))
if mibBuilder.loadTexts:switchAlarm6_11e.setStatus('')
switchClear6_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,24))
switchClear6_11e.setObjects(*((_A,_E),(_A,_M),(_A,_M),(_A,_M)))
if mibBuilder.loadTexts:switchClear6_11e.setStatus('')
switchAlarm7_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,25))
switchAlarm7_11e.setObjects(*((_A,_E),(_A,_N),(_A,_N),(_A,_N)))
if mibBuilder.loadTexts:switchAlarm7_11e.setStatus('')
switchClear7_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,26))
switchClear7_11e.setObjects(*((_A,_E),(_A,_N),(_A,_N),(_A,_N)))
if mibBuilder.loadTexts:switchClear7_11e.setStatus('')
switchAlarm8_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,27))
switchAlarm8_11e.setObjects(*((_A,_E),(_A,_O),(_A,_O),(_A,_O)))
if mibBuilder.loadTexts:switchAlarm8_11e.setStatus('')
switchClear8_11e=NotificationType((1,3,6,1,4,1,20916,1,3,0,28))
switchClear8_11e.setObjects(*((_A,_E),(_A,_O),(_A,_O),(_A,_O)))
if mibBuilder.loadTexts:switchClear8_11e.setStatus('')
mibBuilder.exportSymbols(_A,**{'avtech':avtech,'products':products,'roomalert11E':roomalert11E,'tempAlarm1-11e':tempAlarm1_11e,'room-alert-11E-SNMP-trap':room_alert_11E_SNMP_trap,'tempAlarm2-11e':tempAlarm2_11e,'tempClear2-11e':tempClear2_11e,'tempAlarm3-11e':tempAlarm3_11e,'tempClear3-11e':tempClear3_11e,'humidityAlarm1-11e':humidityAlarm1_11e,'humidityClear1-11e':humidityClear1_11e,'humidityAlarm2-11e':humidityAlarm2_11e,'humidityClear2-11e':humidityClear2_11e,'humidityAlarm3-11e':humidityAlarm3_11e,'humidityClear3-11e':humidityClear3_11e,'switchAlarm1-11e':switchAlarm1_11e,'switchClear1-11e':switchClear1_11e,'switchAlarm2-11e':switchAlarm2_11e,'switchClear2-11e':switchClear2_11e,'switchAlarm3-11e':switchAlarm3_11e,'switchClear3-11e':switchClear3_11e,'switchAlarm4-11e':switchAlarm4_11e,'switchClear4-11e':switchClear4_11e,'switchAlarm5-11e':switchAlarm5_11e,'switchClear5-11e':switchClear5_11e,'switchAlarm6-11e':switchAlarm6_11e,'switchClear6-11e':switchClear6_11e,'switchAlarm7-11e':switchAlarm7_11e,'switchClear7-11e':switchClear7_11e,'switchAlarm8-11e':switchAlarm8_11e,'switchClear8-11e':switchClear8_11e,'sensors':sensors,'channel1':channel1,_H:sensor1_1,_I:sensor1_2,_J:sensor1_3,_K:sensor1_4,_L:sensor1_5,_M:sensor1_6,_N:sensor1_7,_O:sensor1_8,'switch-label-1':switch_label_1,'switch-label-2':switch_label_2,'switch-label-3':switch_label_3,'switch-label-4':switch_label_4,'switch-label-5':switch_label_5,'switch-label-6':switch_label_6,'switch-label-7':switch_label_7,'switch-label-8':switch_label_8,'channel2':channel2,_S:sensor2_1,_V:sensor2_2,_W:sensor2_3,'sensor2-4':sensor2_4,'sensor2-5':sensor2_5,'sensor2-6-label':sensor2_6_label,'channel3':channel3,_F:sensor3_1,_T:sensor3_2,_X:sensor3_3,'sensor3-4':sensor3_4,'sensor3-5':sensor3_5,'sensor3-6-label':sensor3_6_label,'channel4':channel4,_G:sensor4_1,_U:sensor4_2,_Y:sensor4_3,'sensor4-4':sensor4_4,'sensor4-5':sensor4_5,'sensor4-6-label':sensor4_6_label,'traps':traps,'alarm1':alarm1,'alarm2':alarm2,'alarm3':alarm3,'alarm4':alarm4,_E:alarmMessage1,_R:alarmMessage2,_P:alarmMessage3,_Q:alarmMessage4,'thresholds':thresholds,'channels':channels,'channels1':channels1,'threshold1-1':threshold1_1,'threshold1-2':threshold1_2,'threshold1-3':threshold1_3,'threshold1-4':threshold1_4,'threshold1-5':threshold1_5,'threshold1-6':threshold1_6,'threshold1-7':threshold1_7,'threshold1-8':threshold1_8,'channels2':channels2,'threshold2-1':threshold2_1,'threshold2-2':threshold2_2,'threshold2-3':threshold2_3,'threshold2-4':threshold2_4,'channels3':channels3,'threshold3-1':threshold3_1,'threshold3-2':threshold3_2,'threshold3-3':threshold3_3,'threshold3-4':threshold3_4,'channels4':channels4,'threshold4-1':threshold4_1,'threshold4-2':threshold4_2,'threshold4-3':threshold4_3,'threshold4-4':threshold4_4})