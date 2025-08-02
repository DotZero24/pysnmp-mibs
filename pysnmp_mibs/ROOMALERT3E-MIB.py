_G='alarmmessage'
_F='ROOMALERT3E-MIB'
_E='NotificationType'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Avtech_ObjectIdentity=ObjectIdentity
avtech=_Avtech_ObjectIdentity((1,3,6,1,4,1,20916))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,20916,1))
_Roomalert3E_ObjectIdentity=ObjectIdentity
roomalert3E=_Roomalert3E_ObjectIdentity((1,3,6,1,4,1,20916,1,9))
_Sensors_ObjectIdentity=ObjectIdentity
sensors=_Sensors_ObjectIdentity((1,3,6,1,4,1,20916,1,9,1))
_Digital_ObjectIdentity=ObjectIdentity
digital=_Digital_ObjectIdentity((1,3,6,1,4,1,20916,1,9,1,1))
_Digital_sen1_ObjectIdentity=ObjectIdentity
digital_sen1=_Digital_sen1_ObjectIdentity((1,3,6,1,4,1,20916,1,9,1,1,1))
class _Digital_sen1_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_1_Type.__name__=_B
_Digital_sen1_1_Object=MibScalar
digital_sen1_1=_Digital_sen1_1_Object((1,3,6,1,4,1,20916,1,9,1,1,1,1),_Digital_sen1_1_Type())
digital_sen1_1.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_1.setStatus(_A)
class _Digital_sen1_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_2_Type.__name__=_B
_Digital_sen1_2_Object=MibScalar
digital_sen1_2=_Digital_sen1_2_Object((1,3,6,1,4,1,20916,1,9,1,1,1,2),_Digital_sen1_2_Type())
digital_sen1_2.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_2.setStatus(_A)
_Digital_sen1_label_Type=OctetString
_Digital_sen1_label_Object=MibScalar
digital_sen1_label=_Digital_sen1_label_Object((1,3,6,1,4,1,20916,1,9,1,1,1,3),_Digital_sen1_label_Type())
digital_sen1_label.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_label.setStatus(_A)
_Digital_sen2_ObjectIdentity=ObjectIdentity
digital_sen2=_Digital_sen2_ObjectIdentity((1,3,6,1,4,1,20916,1,9,1,1,2))
class _Digital_sen2_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_1_Type.__name__=_B
_Digital_sen2_1_Object=MibScalar
digital_sen2_1=_Digital_sen2_1_Object((1,3,6,1,4,1,20916,1,9,1,1,2,1),_Digital_sen2_1_Type())
digital_sen2_1.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_1.setStatus(_A)
class _Digital_sen2_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_2_Type.__name__=_B
_Digital_sen2_2_Object=MibScalar
digital_sen2_2=_Digital_sen2_2_Object((1,3,6,1,4,1,20916,1,9,1,1,2,2),_Digital_sen2_2_Type())
digital_sen2_2.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_2.setStatus(_A)
class _Digital_sen2_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_3_Type.__name__=_B
_Digital_sen2_3_Object=MibScalar
digital_sen2_3=_Digital_sen2_3_Object((1,3,6,1,4,1,20916,1,9,1,1,2,3),_Digital_sen2_3_Type())
digital_sen2_3.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_3.setStatus(_A)
class _Digital_sen2_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_4_Type.__name__=_B
_Digital_sen2_4_Object=MibScalar
digital_sen2_4=_Digital_sen2_4_Object((1,3,6,1,4,1,20916,1,9,1,1,2,4),_Digital_sen2_4_Type())
digital_sen2_4.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_4.setStatus(_A)
class _Digital_sen2_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_5_Type.__name__=_B
_Digital_sen2_5_Object=MibScalar
digital_sen2_5=_Digital_sen2_5_Object((1,3,6,1,4,1,20916,1,9,1,1,2,5),_Digital_sen2_5_Type())
digital_sen2_5.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_5.setStatus(_A)
class _Digital_sen2_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_6_Type.__name__=_B
_Digital_sen2_6_Object=MibScalar
digital_sen2_6=_Digital_sen2_6_Object((1,3,6,1,4,1,20916,1,9,1,1,2,6),_Digital_sen2_6_Type())
digital_sen2_6.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_6.setStatus(_A)
class _Digital_sen2_7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_7_Type.__name__=_B
_Digital_sen2_7_Object=MibScalar
digital_sen2_7=_Digital_sen2_7_Object((1,3,6,1,4,1,20916,1,9,1,1,2,7),_Digital_sen2_7_Type())
digital_sen2_7.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_7.setStatus(_A)
_Digital_sen2_label_Type=OctetString
_Digital_sen2_label_Object=MibScalar
digital_sen2_label=_Digital_sen2_label_Object((1,3,6,1,4,1,20916,1,9,1,1,2,8),_Digital_sen2_label_Type())
digital_sen2_label.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_label.setStatus(_A)
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,20916,1,9,1,2))
class _Switch_sen1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Switch_sen1_Type.__name__=_B
_Switch_sen1_Object=MibScalar
switch_sen1=_Switch_sen1_Object((1,3,6,1,4,1,20916,1,9,1,2,1),_Switch_sen1_Type())
switch_sen1.setMaxAccess(_C)
if mibBuilder.loadTexts:switch_sen1.setStatus(_A)
_Switch_label_Type=OctetString
_Switch_label_Object=MibScalar
switch_label=_Switch_label_Object((1,3,6,1,4,1,20916,1,9,1,2,2),_Switch_label_Type())
switch_label.setMaxAccess(_C)
if mibBuilder.loadTexts:switch_label.setStatus(_A)
_Signaltower_ObjectIdentity=ObjectIdentity
signaltower=_Signaltower_ObjectIdentity((1,3,6,1,4,1,20916,1,9,2))
class _Red_led_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Red_led_Type.__name__=_B
_Red_led_Object=MibScalar
red_led=_Red_led_Object((1,3,6,1,4,1,20916,1,9,2,1),_Red_led_Type())
red_led.setMaxAccess(_D)
if mibBuilder.loadTexts:red_led.setStatus(_A)
class _Amber_led_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Amber_led_Type.__name__=_B
_Amber_led_Object=MibScalar
amber_led=_Amber_led_Object((1,3,6,1,4,1,20916,1,9,2,2),_Amber_led_Type())
amber_led.setMaxAccess(_D)
if mibBuilder.loadTexts:amber_led.setStatus(_A)
class _Green_led_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Green_led_Type.__name__=_B
_Green_led_Object=MibScalar
green_led=_Green_led_Object((1,3,6,1,4,1,20916,1,9,2,3),_Green_led_Type())
green_led.setMaxAccess(_D)
if mibBuilder.loadTexts:green_led.setStatus(_A)
class _Blue_led_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Blue_led_Type.__name__=_B
_Blue_led_Object=MibScalar
blue_led=_Blue_led_Object((1,3,6,1,4,1,20916,1,9,2,4),_Blue_led_Type())
blue_led.setMaxAccess(_D)
if mibBuilder.loadTexts:blue_led.setStatus(_A)
class _White_led_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_White_led_Type.__name__=_B
_White_led_Object=MibScalar
white_led=_White_led_Object((1,3,6,1,4,1,20916,1,9,2,5),_White_led_Type())
white_led.setMaxAccess(_D)
if mibBuilder.loadTexts:white_led.setStatus(_A)
class _Alarm1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alarm1_Type.__name__=_B
_Alarm1_Object=MibScalar
alarm1=_Alarm1_Object((1,3,6,1,4,1,20916,1,9,2,6),_Alarm1_Type())
alarm1.setMaxAccess(_D)
if mibBuilder.loadTexts:alarm1.setStatus(_A)
class _Alarm2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alarm2_Type.__name__=_B
_Alarm2_Object=MibScalar
alarm2=_Alarm2_Object((1,3,6,1,4,1,20916,1,9,2,7),_Alarm2_Type())
alarm2.setMaxAccess(_D)
if mibBuilder.loadTexts:alarm2.setStatus(_A)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,20916,1,9,3))
_Alarmmessage_Type=OctetString
_Alarmmessage_Object=MibScalar
alarmmessage=_Alarmmessage_Object((1,3,6,1,4,1,20916,1,9,3,1),_Alarmmessage_Type())
alarmmessage.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmmessage.setStatus(_A)
room_alert_3e_snmp_trap=NotificationType((1,3,6,1,4,1,20916,1,9,0,2))
room_alert_3e_snmp_trap.setObjects((_F,_G))
if mibBuilder.loadTexts:room_alert_3e_snmp_trap.setStatus('')
mibBuilder.exportSymbols(_F,**{'avtech':avtech,'products':products,'roomalert3E':roomalert3E,'room-alert-3e-snmp-trap':room_alert_3e_snmp_trap,'sensors':sensors,'digital':digital,'digital-sen1':digital_sen1,'digital-sen1-1':digital_sen1_1,'digital-sen1-2':digital_sen1_2,'digital-sen1-label':digital_sen1_label,'digital-sen2':digital_sen2,'digital-sen2-1':digital_sen2_1,'digital-sen2-2':digital_sen2_2,'digital-sen2-3':digital_sen2_3,'digital-sen2-4':digital_sen2_4,'digital-sen2-5':digital_sen2_5,'digital-sen2-6':digital_sen2_6,'digital-sen2-7':digital_sen2_7,'digital-sen2-label':digital_sen2_label,'switch':switch,'switch-sen1':switch_sen1,'switch-label':switch_label,'signaltower':signaltower,'red-led':red_led,'amber-led':amber_led,'green-led':green_led,'blue-led':blue_led,'white-led':white_led,'alarm1':alarm1,'alarm2':alarm2,'traps':traps,_G:alarmmessage})