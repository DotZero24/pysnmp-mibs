_D='read-write'
_C='read-only'
_B='mandatory'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Avtech_ObjectIdentity=ObjectIdentity
avtech=_Avtech_ObjectIdentity((1,3,6,1,4,1,20916))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,20916,1))
_Roomalert12S_ObjectIdentity=ObjectIdentity
roomalert12S=_Roomalert12S_ObjectIdentity((1,3,6,1,4,1,20916,1,12))
_Sensors_ObjectIdentity=ObjectIdentity
sensors=_Sensors_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1))
_Internal_ObjectIdentity=ObjectIdentity
internal=_Internal_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1,1))
_Temperature_ObjectIdentity=ObjectIdentity
temperature=_Temperature_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1,1,1))
class _Internal_tempf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Internal_tempf_Type.__name__=_A
_Internal_tempf_Object=MibScalar
internal_tempf=_Internal_tempf_Object((1,3,6,1,4,1,20916,1,12,1,1,1,1),_Internal_tempf_Type())
internal_tempf.setMaxAccess(_C)
if mibBuilder.loadTexts:internal_tempf.setStatus(_B)
class _Internal_tempc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Internal_tempc_Type.__name__=_A
_Internal_tempc_Object=MibScalar
internal_tempc=_Internal_tempc_Object((1,3,6,1,4,1,20916,1,12,1,1,1,2),_Internal_tempc_Type())
internal_tempc.setMaxAccess(_C)
if mibBuilder.loadTexts:internal_tempc.setStatus(_B)
_Analog_ObjectIdentity=ObjectIdentity
analog=_Analog_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1,1,2))
class _Internal_analog1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Internal_analog1_Type.__name__=_A
_Internal_analog1_Object=MibScalar
internal_analog1=_Internal_analog1_Object((1,3,6,1,4,1,20916,1,12,1,1,2,1),_Internal_analog1_Type())
internal_analog1.setMaxAccess(_C)
if mibBuilder.loadTexts:internal_analog1.setStatus(_B)
_Relay_ObjectIdentity=ObjectIdentity
relay=_Relay_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1,1,3))
class _Internal_relay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Internal_relay1_Type.__name__=_A
_Internal_relay1_Object=MibScalar
internal_relay1=_Internal_relay1_Object((1,3,6,1,4,1,20916,1,12,1,1,3,1),_Internal_relay1_Type())
internal_relay1.setMaxAccess(_D)
if mibBuilder.loadTexts:internal_relay1.setStatus(_B)
_Digital_ObjectIdentity=ObjectIdentity
digital=_Digital_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1,2))
_Digital_sen1_ObjectIdentity=ObjectIdentity
digital_sen1=_Digital_sen1_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1,2,1))
class _Digital_sen1_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_1_Type.__name__=_A
_Digital_sen1_1_Object=MibScalar
digital_sen1_1=_Digital_sen1_1_Object((1,3,6,1,4,1,20916,1,12,1,2,1,1),_Digital_sen1_1_Type())
digital_sen1_1.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_1.setStatus(_B)
class _Digital_sen1_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_2_Type.__name__=_A
_Digital_sen1_2_Object=MibScalar
digital_sen1_2=_Digital_sen1_2_Object((1,3,6,1,4,1,20916,1,12,1,2,1,2),_Digital_sen1_2_Type())
digital_sen1_2.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_2.setStatus(_B)
class _Digital_sen1_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_3_Type.__name__=_A
_Digital_sen1_3_Object=MibScalar
digital_sen1_3=_Digital_sen1_3_Object((1,3,6,1,4,1,20916,1,12,1,2,1,3),_Digital_sen1_3_Type())
digital_sen1_3.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_3.setStatus(_B)
class _Digital_sen1_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_4_Type.__name__=_A
_Digital_sen1_4_Object=MibScalar
digital_sen1_4=_Digital_sen1_4_Object((1,3,6,1,4,1,20916,1,12,1,2,1,4),_Digital_sen1_4_Type())
digital_sen1_4.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_4.setStatus(_B)
class _Digital_sen1_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_5_Type.__name__=_A
_Digital_sen1_5_Object=MibScalar
digital_sen1_5=_Digital_sen1_5_Object((1,3,6,1,4,1,20916,1,12,1,2,1,5),_Digital_sen1_5_Type())
digital_sen1_5.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_5.setStatus(_B)
class _Digital_sen1_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_6_Type.__name__=_A
_Digital_sen1_6_Object=MibScalar
digital_sen1_6=_Digital_sen1_6_Object((1,3,6,1,4,1,20916,1,12,1,2,1,6),_Digital_sen1_6_Type())
digital_sen1_6.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_6.setStatus(_B)
class _Digital_sen1_7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen1_7_Type.__name__=_A
_Digital_sen1_7_Object=MibScalar
digital_sen1_7=_Digital_sen1_7_Object((1,3,6,1,4,1,20916,1,12,1,2,1,7),_Digital_sen1_7_Type())
digital_sen1_7.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen1_7.setStatus(_B)
_Digital_sen2_ObjectIdentity=ObjectIdentity
digital_sen2=_Digital_sen2_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1,2,2))
class _Digital_sen2_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_1_Type.__name__=_A
_Digital_sen2_1_Object=MibScalar
digital_sen2_1=_Digital_sen2_1_Object((1,3,6,1,4,1,20916,1,12,1,2,2,1),_Digital_sen2_1_Type())
digital_sen2_1.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_1.setStatus(_B)
class _Digital_sen2_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_2_Type.__name__=_A
_Digital_sen2_2_Object=MibScalar
digital_sen2_2=_Digital_sen2_2_Object((1,3,6,1,4,1,20916,1,12,1,2,2,2),_Digital_sen2_2_Type())
digital_sen2_2.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_2.setStatus(_B)
class _Digital_sen2_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_3_Type.__name__=_A
_Digital_sen2_3_Object=MibScalar
digital_sen2_3=_Digital_sen2_3_Object((1,3,6,1,4,1,20916,1,12,1,2,2,3),_Digital_sen2_3_Type())
digital_sen2_3.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_3.setStatus(_B)
class _Digital_sen2_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_4_Type.__name__=_A
_Digital_sen2_4_Object=MibScalar
digital_sen2_4=_Digital_sen2_4_Object((1,3,6,1,4,1,20916,1,12,1,2,2,4),_Digital_sen2_4_Type())
digital_sen2_4.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_4.setStatus(_B)
class _Digital_sen2_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_5_Type.__name__=_A
_Digital_sen2_5_Object=MibScalar
digital_sen2_5=_Digital_sen2_5_Object((1,3,6,1,4,1,20916,1,12,1,2,2,5),_Digital_sen2_5_Type())
digital_sen2_5.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_5.setStatus(_B)
class _Digital_sen2_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_6_Type.__name__=_A
_Digital_sen2_6_Object=MibScalar
digital_sen2_6=_Digital_sen2_6_Object((1,3,6,1,4,1,20916,1,12,1,2,2,6),_Digital_sen2_6_Type())
digital_sen2_6.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_6.setStatus(_B)
class _Digital_sen2_7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen2_7_Type.__name__=_A
_Digital_sen2_7_Object=MibScalar
digital_sen2_7=_Digital_sen2_7_Object((1,3,6,1,4,1,20916,1,12,1,2,2,7),_Digital_sen2_7_Type())
digital_sen2_7.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen2_7.setStatus(_B)
_Digital_sen3_ObjectIdentity=ObjectIdentity
digital_sen3=_Digital_sen3_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1,2,3))
class _Digital_sen3_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen3_1_Type.__name__=_A
_Digital_sen3_1_Object=MibScalar
digital_sen3_1=_Digital_sen3_1_Object((1,3,6,1,4,1,20916,1,12,1,2,3,1),_Digital_sen3_1_Type())
digital_sen3_1.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen3_1.setStatus(_B)
class _Digital_sen3_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen3_2_Type.__name__=_A
_Digital_sen3_2_Object=MibScalar
digital_sen3_2=_Digital_sen3_2_Object((1,3,6,1,4,1,20916,1,12,1,2,3,2),_Digital_sen3_2_Type())
digital_sen3_2.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen3_2.setStatus(_B)
class _Digital_sen3_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen3_3_Type.__name__=_A
_Digital_sen3_3_Object=MibScalar
digital_sen3_3=_Digital_sen3_3_Object((1,3,6,1,4,1,20916,1,12,1,2,3,3),_Digital_sen3_3_Type())
digital_sen3_3.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen3_3.setStatus(_B)
class _Digital_sen3_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen3_4_Type.__name__=_A
_Digital_sen3_4_Object=MibScalar
digital_sen3_4=_Digital_sen3_4_Object((1,3,6,1,4,1,20916,1,12,1,2,3,4),_Digital_sen3_4_Type())
digital_sen3_4.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen3_4.setStatus(_B)
class _Digital_sen3_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen3_5_Type.__name__=_A
_Digital_sen3_5_Object=MibScalar
digital_sen3_5=_Digital_sen3_5_Object((1,3,6,1,4,1,20916,1,12,1,2,3,5),_Digital_sen3_5_Type())
digital_sen3_5.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen3_5.setStatus(_B)
class _Digital_sen3_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen3_6_Type.__name__=_A
_Digital_sen3_6_Object=MibScalar
digital_sen3_6=_Digital_sen3_6_Object((1,3,6,1,4,1,20916,1,12,1,2,3,6),_Digital_sen3_6_Type())
digital_sen3_6.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen3_6.setStatus(_B)
class _Digital_sen3_7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Digital_sen3_7_Type.__name__=_A
_Digital_sen3_7_Object=MibScalar
digital_sen3_7=_Digital_sen3_7_Object((1,3,6,1,4,1,20916,1,12,1,2,3,7),_Digital_sen3_7_Type())
digital_sen3_7.setMaxAccess(_C)
if mibBuilder.loadTexts:digital_sen3_7.setStatus(_B)
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,20916,1,12,1,3))
class _Switch_sen1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Switch_sen1_Type.__name__=_A
_Switch_sen1_Object=MibScalar
switch_sen1=_Switch_sen1_Object((1,3,6,1,4,1,20916,1,12,1,3,1),_Switch_sen1_Type())
switch_sen1.setMaxAccess(_C)
if mibBuilder.loadTexts:switch_sen1.setStatus(_B)
class _Switch_sen2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Switch_sen2_Type.__name__=_A
_Switch_sen2_Object=MibScalar
switch_sen2=_Switch_sen2_Object((1,3,6,1,4,1,20916,1,12,1,3,2),_Switch_sen2_Type())
switch_sen2.setMaxAccess(_C)
if mibBuilder.loadTexts:switch_sen2.setStatus(_B)
class _Switch_sen3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Switch_sen3_Type.__name__=_A
_Switch_sen3_Object=MibScalar
switch_sen3=_Switch_sen3_Object((1,3,6,1,4,1,20916,1,12,1,3,3),_Switch_sen3_Type())
switch_sen3.setMaxAccess(_C)
if mibBuilder.loadTexts:switch_sen3.setStatus(_B)
class _Switch_sen4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Switch_sen4_Type.__name__=_A
_Switch_sen4_Object=MibScalar
switch_sen4=_Switch_sen4_Object((1,3,6,1,4,1,20916,1,12,1,3,4),_Switch_sen4_Type())
switch_sen4.setMaxAccess(_C)
if mibBuilder.loadTexts:switch_sen4.setStatus(_B)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,20916,1,12,2))
_Alarmmessage_Type=OctetString
_Alarmmessage_Object=MibScalar
alarmmessage=_Alarmmessage_Object((1,3,6,1,4,1,20916,1,12,2,1),_Alarmmessage_Type())
alarmmessage.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmmessage.setStatus(_B)
_Externalrelays_ObjectIdentity=ObjectIdentity
externalrelays=_Externalrelays_ObjectIdentity((1,3,6,1,4,1,20916,1,12,3))
_Externalrelay1_ObjectIdentity=ObjectIdentity
externalrelay1=_Externalrelay1_ObjectIdentity((1,3,6,1,4,1,20916,1,12,3,1))
class _Externalrelay1_element_one_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Externalrelay1_element_one_Type.__name__=_A
_Externalrelay1_element_one_Object=MibScalar
externalrelay1_element_one=_Externalrelay1_element_one_Object((1,3,6,1,4,1,20916,1,12,3,1,1),_Externalrelay1_element_one_Type())
externalrelay1_element_one.setMaxAccess(_D)
if mibBuilder.loadTexts:externalrelay1_element_one.setStatus(_B)
class _Externalrelay1_element_two_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Externalrelay1_element_two_Type.__name__=_A
_Externalrelay1_element_two_Object=MibScalar
externalrelay1_element_two=_Externalrelay1_element_two_Object((1,3,6,1,4,1,20916,1,12,3,1,2),_Externalrelay1_element_two_Type())
externalrelay1_element_two.setMaxAccess(_D)
if mibBuilder.loadTexts:externalrelay1_element_two.setStatus(_B)
class _Externalrelay1_element_three_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Externalrelay1_element_three_Type.__name__=_A
_Externalrelay1_element_three_Object=MibScalar
externalrelay1_element_three=_Externalrelay1_element_three_Object((1,3,6,1,4,1,20916,1,12,3,1,3),_Externalrelay1_element_three_Type())
externalrelay1_element_three.setMaxAccess(_D)
if mibBuilder.loadTexts:externalrelay1_element_three.setStatus(_B)
class _Externalrelay1_element_four_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Externalrelay1_element_four_Type.__name__=_A
_Externalrelay1_element_four_Object=MibScalar
externalrelay1_element_four=_Externalrelay1_element_four_Object((1,3,6,1,4,1,20916,1,12,3,1,4),_Externalrelay1_element_four_Type())
externalrelay1_element_four.setMaxAccess(_D)
if mibBuilder.loadTexts:externalrelay1_element_four.setStatus(_B)
class _Externalrelay1_element_five_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Externalrelay1_element_five_Type.__name__=_A
_Externalrelay1_element_five_Object=MibScalar
externalrelay1_element_five=_Externalrelay1_element_five_Object((1,3,6,1,4,1,20916,1,12,3,1,5),_Externalrelay1_element_five_Type())
externalrelay1_element_five.setMaxAccess(_D)
if mibBuilder.loadTexts:externalrelay1_element_five.setStatus(_B)
class _Externalrelay1_element_six_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Externalrelay1_element_six_Type.__name__=_A
_Externalrelay1_element_six_Object=MibScalar
externalrelay1_element_six=_Externalrelay1_element_six_Object((1,3,6,1,4,1,20916,1,12,3,1,6),_Externalrelay1_element_six_Type())
externalrelay1_element_six.setMaxAccess(_D)
if mibBuilder.loadTexts:externalrelay1_element_six.setStatus(_B)
class _Externalrelay1_element_seven_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Externalrelay1_element_seven_Type.__name__=_A
_Externalrelay1_element_seven_Object=MibScalar
externalrelay1_element_seven=_Externalrelay1_element_seven_Object((1,3,6,1,4,1,20916,1,12,3,1,7),_Externalrelay1_element_seven_Type())
externalrelay1_element_seven.setMaxAccess(_D)
if mibBuilder.loadTexts:externalrelay1_element_seven.setStatus(_B)
class _Externalrelay1_element_eight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Externalrelay1_element_eight_Type.__name__=_A
_Externalrelay1_element_eight_Object=MibScalar
externalrelay1_element_eight=_Externalrelay1_element_eight_Object((1,3,6,1,4,1,20916,1,12,3,1,8),_Externalrelay1_element_eight_Type())
externalrelay1_element_eight.setMaxAccess(_D)
if mibBuilder.loadTexts:externalrelay1_element_eight.setStatus(_B)
mibBuilder.exportSymbols('ROOMALERT12S-MIB',**{'avtech':avtech,'products':products,'roomalert12S':roomalert12S,'sensors':sensors,'internal':internal,'temperature':temperature,'internal-tempf':internal_tempf,'internal-tempc':internal_tempc,'analog':analog,'internal-analog1':internal_analog1,'relay':relay,'internal-relay1':internal_relay1,'digital':digital,'digital-sen1':digital_sen1,'digital-sen1-1':digital_sen1_1,'digital-sen1-2':digital_sen1_2,'digital-sen1-3':digital_sen1_3,'digital-sen1-4':digital_sen1_4,'digital-sen1-5':digital_sen1_5,'digital-sen1-6':digital_sen1_6,'digital-sen1-7':digital_sen1_7,'digital-sen2':digital_sen2,'digital-sen2-1':digital_sen2_1,'digital-sen2-2':digital_sen2_2,'digital-sen2-3':digital_sen2_3,'digital-sen2-4':digital_sen2_4,'digital-sen2-5':digital_sen2_5,'digital-sen2-6':digital_sen2_6,'digital-sen2-7':digital_sen2_7,'digital-sen3':digital_sen3,'digital-sen3-1':digital_sen3_1,'digital-sen3-2':digital_sen3_2,'digital-sen3-3':digital_sen3_3,'digital-sen3-4':digital_sen3_4,'digital-sen3-5':digital_sen3_5,'digital-sen3-6':digital_sen3_6,'digital-sen3-7':digital_sen3_7,'switch':switch,'switch-sen1':switch_sen1,'switch-sen2':switch_sen2,'switch-sen3':switch_sen3,'switch-sen4':switch_sen4,'traps':traps,'alarmmessage':alarmmessage,'externalrelays':externalrelays,'externalrelay1':externalrelay1,'externalrelay1-element-one':externalrelay1_element_one,'externalrelay1-element-two':externalrelay1_element_two,'externalrelay1-element-three':externalrelay1_element_three,'externalrelay1-element-four':externalrelay1_element_four,'externalrelay1-element-five':externalrelay1_element_five,'externalrelay1-element-six':externalrelay1_element_six,'externalrelay1-element-seven':externalrelay1_element_seven,'externalrelay1-element-eight':externalrelay1_element_eight})