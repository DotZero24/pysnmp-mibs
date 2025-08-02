_d='ch1value'
_c='NotificationType'
_b='bin3Alarm'
_a='bin3Val'
_Z='bin3Name'
_Y='bin2Alarm'
_X='bin2Val'
_W='bin2Name'
_V='bin1Alarm'
_U='bin1Val'
_T='bin1Name'
_S='ch4Alarm'
_R='ch4Val'
_Q='ch4Name'
_P='ch3Alarm'
_O='ch3Val'
_N='ch3Name'
_M='ch2Alarm'
_L='ch2Val'
_K='ch2Name'
_J='ch1Alarm'
_I='ch1Val'
_H='ch1Name'
_G='messageString'
_F='sensorName'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='mandatory'
_A='P8552-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_c,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_c,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Comet_ObjectIdentity=ObjectIdentity
comet=_Comet_ObjectIdentity((1,3,6,1,4,1,22626))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,22626,1))
_P8552_ObjectIdentity=ObjectIdentity
p8552=_P8552_ObjectIdentity((1,3,6,1,4,1,22626,1,5))
__pysmi_global_ObjectIdentity=ObjectIdentity
_pysmi_global=__pysmi_global_ObjectIdentity((1,3,6,1,4,1,22626,1,5,1))
class _SensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
_SensorName_Type.__name__=_D
_SensorName_Object=MibScalar
sensorName=_SensorName_Object((1,3,6,1,4,1,22626,1,5,1,1),_SensorName_Type())
sensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorName.setStatus(_B)
class _SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SerialNumber_Type.__name__=_D
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,22626,1,5,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:serialNumber.setStatus(_B)
class _DeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_DeviceType_Type.__name__=_E
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,22626,1,5,1,3),_DeviceType_Type())
deviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceType.setStatus(_B)
_Channels_ObjectIdentity=ObjectIdentity
channels=_Channels_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2))
_Channel1_ObjectIdentity=ObjectIdentity
channel1=_Channel1_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2,1))
class _Ch1Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ch1Name_Type.__name__=_D
_Ch1Name_Object=MibScalar
ch1Name=_Ch1Name_Object((1,3,6,1,4,1,22626,1,5,2,1,1),_Ch1Name_Type())
ch1Name.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Name.setStatus(_B)
class _Ch1Val_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1Val_Type.__name__=_D
_Ch1Val_Object=MibScalar
ch1Val=_Ch1Val_Object((1,3,6,1,4,1,22626,1,5,2,1,2),_Ch1Val_Type())
ch1Val.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Val.setStatus(_B)
class _Ch1IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1IntVal_Type.__name__=_E
_Ch1IntVal_Object=MibScalar
ch1IntVal=_Ch1IntVal_Object((1,3,6,1,4,1,22626,1,5,2,1,3),_Ch1IntVal_Type())
ch1IntVal.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1IntVal.setStatus(_B)
class _Ch1Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Ch1Alarm_Type.__name__=_E
_Ch1Alarm_Object=MibScalar
ch1Alarm=_Ch1Alarm_Object((1,3,6,1,4,1,22626,1,5,2,1,4),_Ch1Alarm_Type())
ch1Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Alarm.setStatus(_B)
class _Ch1LimHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1LimHi_Type.__name__=_E
_Ch1LimHi_Object=MibScalar
ch1LimHi=_Ch1LimHi_Object((1,3,6,1,4,1,22626,1,5,2,1,5),_Ch1LimHi_Type())
ch1LimHi.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1LimHi.setStatus(_B)
class _Ch1LimLo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1LimLo_Type.__name__=_E
_Ch1LimLo_Object=MibScalar
ch1LimLo=_Ch1LimLo_Object((1,3,6,1,4,1,22626,1,5,2,1,6),_Ch1LimLo_Type())
ch1LimLo.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1LimLo.setStatus(_B)
class _Ch1LimHyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1LimHyst_Type.__name__=_E
_Ch1LimHyst_Object=MibScalar
ch1LimHyst=_Ch1LimHyst_Object((1,3,6,1,4,1,22626,1,5,2,1,7),_Ch1LimHyst_Type())
ch1LimHyst.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1LimHyst.setStatus(_B)
class _Ch1LimDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_Ch1LimDelay_Type.__name__=_E
_Ch1LimDelay_Object=MibScalar
ch1LimDelay=_Ch1LimDelay_Object((1,3,6,1,4,1,22626,1,5,2,1,8),_Ch1LimDelay_Type())
ch1LimDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1LimDelay.setStatus(_B)
class _Ch1Unit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1Unit_Type.__name__=_D
_Ch1Unit_Object=MibScalar
ch1Unit=_Ch1Unit_Object((1,3,6,1,4,1,22626,1,5,2,1,9),_Ch1Unit_Type())
ch1Unit.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Unit.setStatus(_B)
class _Ch1AlarmStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1AlarmStr_Type.__name__=_D
_Ch1AlarmStr_Object=MibScalar
ch1AlarmStr=_Ch1AlarmStr_Object((1,3,6,1,4,1,22626,1,5,2,1,10),_Ch1AlarmStr_Type())
ch1AlarmStr.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1AlarmStr.setStatus(_B)
class _Ch1Min_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1Min_Type.__name__=_D
_Ch1Min_Object=MibScalar
ch1Min=_Ch1Min_Object((1,3,6,1,4,1,22626,1,5,2,1,11),_Ch1Min_Type())
ch1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Min.setStatus(_B)
class _Ch1Max_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1Max_Type.__name__=_D
_Ch1Max_Object=MibScalar
ch1Max=_Ch1Max_Object((1,3,6,1,4,1,22626,1,5,2,1,12),_Ch1Max_Type())
ch1Max.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Max.setStatus(_B)
_Channel2_ObjectIdentity=ObjectIdentity
channel2=_Channel2_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2,2))
class _Ch2Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ch2Name_Type.__name__=_D
_Ch2Name_Object=MibScalar
ch2Name=_Ch2Name_Object((1,3,6,1,4,1,22626,1,5,2,2,1),_Ch2Name_Type())
ch2Name.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2Name.setStatus(_B)
class _Ch2Val_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch2Val_Type.__name__=_D
_Ch2Val_Object=MibScalar
ch2Val=_Ch2Val_Object((1,3,6,1,4,1,22626,1,5,2,2,2),_Ch2Val_Type())
ch2Val.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2Val.setStatus(_B)
class _Ch2IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch2IntVal_Type.__name__=_E
_Ch2IntVal_Object=MibScalar
ch2IntVal=_Ch2IntVal_Object((1,3,6,1,4,1,22626,1,5,2,2,3),_Ch2IntVal_Type())
ch2IntVal.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2IntVal.setStatus(_B)
class _Ch2Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Ch2Alarm_Type.__name__=_E
_Ch2Alarm_Object=MibScalar
ch2Alarm=_Ch2Alarm_Object((1,3,6,1,4,1,22626,1,5,2,2,4),_Ch2Alarm_Type())
ch2Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2Alarm.setStatus(_B)
class _Ch2LimHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch2LimHi_Type.__name__=_E
_Ch2LimHi_Object=MibScalar
ch2LimHi=_Ch2LimHi_Object((1,3,6,1,4,1,22626,1,5,2,2,5),_Ch2LimHi_Type())
ch2LimHi.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2LimHi.setStatus(_B)
class _Ch2LimLo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch2LimLo_Type.__name__=_E
_Ch2LimLo_Object=MibScalar
ch2LimLo=_Ch2LimLo_Object((1,3,6,1,4,1,22626,1,5,2,2,6),_Ch2LimLo_Type())
ch2LimLo.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2LimLo.setStatus(_B)
class _Ch2LimHyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch2LimHyst_Type.__name__=_E
_Ch2LimHyst_Object=MibScalar
ch2LimHyst=_Ch2LimHyst_Object((1,3,6,1,4,1,22626,1,5,2,2,7),_Ch2LimHyst_Type())
ch2LimHyst.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2LimHyst.setStatus(_B)
class _Ch2LimDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_Ch2LimDelay_Type.__name__=_E
_Ch2LimDelay_Object=MibScalar
ch2LimDelay=_Ch2LimDelay_Object((1,3,6,1,4,1,22626,1,5,2,2,8),_Ch2LimDelay_Type())
ch2LimDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2LimDelay.setStatus(_B)
class _Ch2Unit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch2Unit_Type.__name__=_D
_Ch2Unit_Object=MibScalar
ch2Unit=_Ch2Unit_Object((1,3,6,1,4,1,22626,1,5,2,2,9),_Ch2Unit_Type())
ch2Unit.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2Unit.setStatus(_B)
class _Ch2AlarmStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch2AlarmStr_Type.__name__=_D
_Ch2AlarmStr_Object=MibScalar
ch2AlarmStr=_Ch2AlarmStr_Object((1,3,6,1,4,1,22626,1,5,2,2,10),_Ch2AlarmStr_Type())
ch2AlarmStr.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2AlarmStr.setStatus(_B)
class _Ch2Min_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch2Min_Type.__name__=_D
_Ch2Min_Object=MibScalar
ch2Min=_Ch2Min_Object((1,3,6,1,4,1,22626,1,5,2,2,11),_Ch2Min_Type())
ch2Min.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2Min.setStatus(_B)
class _Ch2Max_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch2Max_Type.__name__=_D
_Ch2Max_Object=MibScalar
ch2Max=_Ch2Max_Object((1,3,6,1,4,1,22626,1,5,2,2,12),_Ch2Max_Type())
ch2Max.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2Max.setStatus(_B)
_Channel3_ObjectIdentity=ObjectIdentity
channel3=_Channel3_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2,3))
class _Ch3Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ch3Name_Type.__name__=_D
_Ch3Name_Object=MibScalar
ch3Name=_Ch3Name_Object((1,3,6,1,4,1,22626,1,5,2,3,1),_Ch3Name_Type())
ch3Name.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3Name.setStatus(_B)
class _Ch3Val_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch3Val_Type.__name__=_D
_Ch3Val_Object=MibScalar
ch3Val=_Ch3Val_Object((1,3,6,1,4,1,22626,1,5,2,3,2),_Ch3Val_Type())
ch3Val.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3Val.setStatus(_B)
class _Ch3IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch3IntVal_Type.__name__=_E
_Ch3IntVal_Object=MibScalar
ch3IntVal=_Ch3IntVal_Object((1,3,6,1,4,1,22626,1,5,2,3,3),_Ch3IntVal_Type())
ch3IntVal.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3IntVal.setStatus(_B)
class _Ch3Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Ch3Alarm_Type.__name__=_E
_Ch3Alarm_Object=MibScalar
ch3Alarm=_Ch3Alarm_Object((1,3,6,1,4,1,22626,1,5,2,3,4),_Ch3Alarm_Type())
ch3Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3Alarm.setStatus(_B)
class _Ch3LimHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch3LimHi_Type.__name__=_E
_Ch3LimHi_Object=MibScalar
ch3LimHi=_Ch3LimHi_Object((1,3,6,1,4,1,22626,1,5,2,3,5),_Ch3LimHi_Type())
ch3LimHi.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3LimHi.setStatus(_B)
class _Ch3LimLo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch3LimLo_Type.__name__=_E
_Ch3LimLo_Object=MibScalar
ch3LimLo=_Ch3LimLo_Object((1,3,6,1,4,1,22626,1,5,2,3,6),_Ch3LimLo_Type())
ch3LimLo.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3LimLo.setStatus(_B)
class _Ch3LimHyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch3LimHyst_Type.__name__=_E
_Ch3LimHyst_Object=MibScalar
ch3LimHyst=_Ch3LimHyst_Object((1,3,6,1,4,1,22626,1,5,2,3,7),_Ch3LimHyst_Type())
ch3LimHyst.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3LimHyst.setStatus(_B)
class _Ch3LimDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_Ch3LimDelay_Type.__name__=_E
_Ch3LimDelay_Object=MibScalar
ch3LimDelay=_Ch3LimDelay_Object((1,3,6,1,4,1,22626,1,5,2,3,8),_Ch3LimDelay_Type())
ch3LimDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3LimDelay.setStatus(_B)
class _Ch3Unit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch3Unit_Type.__name__=_D
_Ch3Unit_Object=MibScalar
ch3Unit=_Ch3Unit_Object((1,3,6,1,4,1,22626,1,5,2,3,9),_Ch3Unit_Type())
ch3Unit.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3Unit.setStatus(_B)
class _Ch3AlarmStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch3AlarmStr_Type.__name__=_D
_Ch3AlarmStr_Object=MibScalar
ch3AlarmStr=_Ch3AlarmStr_Object((1,3,6,1,4,1,22626,1,5,2,3,10),_Ch3AlarmStr_Type())
ch3AlarmStr.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3AlarmStr.setStatus(_B)
class _Ch3Min_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch3Min_Type.__name__=_D
_Ch3Min_Object=MibScalar
ch3Min=_Ch3Min_Object((1,3,6,1,4,1,22626,1,5,2,3,11),_Ch3Min_Type())
ch3Min.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3Min.setStatus(_B)
class _Ch3Max_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch3Max_Type.__name__=_D
_Ch3Max_Object=MibScalar
ch3Max=_Ch3Max_Object((1,3,6,1,4,1,22626,1,5,2,3,12),_Ch3Max_Type())
ch3Max.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3Max.setStatus(_B)
_Channel4_ObjectIdentity=ObjectIdentity
channel4=_Channel4_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2,4))
class _Ch4Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ch4Name_Type.__name__=_D
_Ch4Name_Object=MibScalar
ch4Name=_Ch4Name_Object((1,3,6,1,4,1,22626,1,5,2,4,1),_Ch4Name_Type())
ch4Name.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4Name.setStatus(_B)
class _Ch4Val_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch4Val_Type.__name__=_D
_Ch4Val_Object=MibScalar
ch4Val=_Ch4Val_Object((1,3,6,1,4,1,22626,1,5,2,4,2),_Ch4Val_Type())
ch4Val.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4Val.setStatus(_B)
class _Ch4IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch4IntVal_Type.__name__=_E
_Ch4IntVal_Object=MibScalar
ch4IntVal=_Ch4IntVal_Object((1,3,6,1,4,1,22626,1,5,2,4,3),_Ch4IntVal_Type())
ch4IntVal.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4IntVal.setStatus(_B)
class _Ch4Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Ch4Alarm_Type.__name__=_E
_Ch4Alarm_Object=MibScalar
ch4Alarm=_Ch4Alarm_Object((1,3,6,1,4,1,22626,1,5,2,4,4),_Ch4Alarm_Type())
ch4Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4Alarm.setStatus(_B)
class _Ch4LimHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch4LimHi_Type.__name__=_E
_Ch4LimHi_Object=MibScalar
ch4LimHi=_Ch4LimHi_Object((1,3,6,1,4,1,22626,1,5,2,4,5),_Ch4LimHi_Type())
ch4LimHi.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4LimHi.setStatus(_B)
class _Ch4LimLo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch4LimLo_Type.__name__=_E
_Ch4LimLo_Object=MibScalar
ch4LimLo=_Ch4LimLo_Object((1,3,6,1,4,1,22626,1,5,2,4,6),_Ch4LimLo_Type())
ch4LimLo.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4LimLo.setStatus(_B)
class _Ch4LimHyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch4LimHyst_Type.__name__=_E
_Ch4LimHyst_Object=MibScalar
ch4LimHyst=_Ch4LimHyst_Object((1,3,6,1,4,1,22626,1,5,2,4,7),_Ch4LimHyst_Type())
ch4LimHyst.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4LimHyst.setStatus(_B)
class _Ch4LimDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_Ch4LimDelay_Type.__name__=_E
_Ch4LimDelay_Object=MibScalar
ch4LimDelay=_Ch4LimDelay_Object((1,3,6,1,4,1,22626,1,5,2,4,8),_Ch4LimDelay_Type())
ch4LimDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4LimDelay.setStatus(_B)
class _Ch4Unit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch4Unit_Type.__name__=_D
_Ch4Unit_Object=MibScalar
ch4Unit=_Ch4Unit_Object((1,3,6,1,4,1,22626,1,5,2,4,9),_Ch4Unit_Type())
ch4Unit.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4Unit.setStatus(_B)
class _Ch4AlarmStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch4AlarmStr_Type.__name__=_D
_Ch4AlarmStr_Object=MibScalar
ch4AlarmStr=_Ch4AlarmStr_Object((1,3,6,1,4,1,22626,1,5,2,4,10),_Ch4AlarmStr_Type())
ch4AlarmStr.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4AlarmStr.setStatus(_B)
class _Ch4Min_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch4Min_Type.__name__=_D
_Ch4Min_Object=MibScalar
ch4Min=_Ch4Min_Object((1,3,6,1,4,1,22626,1,5,2,4,11),_Ch4Min_Type())
ch4Min.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4Min.setStatus(_B)
class _Ch4Max_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch4Max_Type.__name__=_D
_Ch4Max_Object=MibScalar
ch4Max=_Ch4Max_Object((1,3,6,1,4,1,22626,1,5,2,4,12),_Ch4Max_Type())
ch4Max.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4Max.setStatus(_B)
_Bin1_ObjectIdentity=ObjectIdentity
bin1=_Bin1_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2,6))
class _Bin1Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Bin1Name_Type.__name__=_D
_Bin1Name_Object=MibScalar
bin1Name=_Bin1Name_Object((1,3,6,1,4,1,22626,1,5,2,6,1),_Bin1Name_Type())
bin1Name.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1Name.setStatus(_B)
class _Bin1Val_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin1Val_Type.__name__=_D
_Bin1Val_Object=MibScalar
bin1Val=_Bin1Val_Object((1,3,6,1,4,1,22626,1,5,2,6,2),_Bin1Val_Type())
bin1Val.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1Val.setStatus(_B)
class _Bin1IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Bin1IntVal_Type.__name__=_E
_Bin1IntVal_Object=MibScalar
bin1IntVal=_Bin1IntVal_Object((1,3,6,1,4,1,22626,1,5,2,6,3),_Bin1IntVal_Type())
bin1IntVal.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1IntVal.setStatus(_B)
class _Bin1AlarmStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin1AlarmStr_Type.__name__=_D
_Bin1AlarmStr_Object=MibScalar
bin1AlarmStr=_Bin1AlarmStr_Object((1,3,6,1,4,1,22626,1,5,2,6,4),_Bin1AlarmStr_Type())
bin1AlarmStr.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1AlarmStr.setStatus(_B)
class _Bin1Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin1Alarm_Type.__name__=_E
_Bin1Alarm_Object=MibScalar
bin1Alarm=_Bin1Alarm_Object((1,3,6,1,4,1,22626,1,5,2,6,5),_Bin1Alarm_Type())
bin1Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1Alarm.setStatus(_B)
_Bin2_ObjectIdentity=ObjectIdentity
bin2=_Bin2_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2,7))
class _Bin2Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Bin2Name_Type.__name__=_D
_Bin2Name_Object=MibScalar
bin2Name=_Bin2Name_Object((1,3,6,1,4,1,22626,1,5,2,7,1),_Bin2Name_Type())
bin2Name.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2Name.setStatus(_B)
class _Bin2Val_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin2Val_Type.__name__=_D
_Bin2Val_Object=MibScalar
bin2Val=_Bin2Val_Object((1,3,6,1,4,1,22626,1,5,2,7,2),_Bin2Val_Type())
bin2Val.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2Val.setStatus(_B)
class _Bin2IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Bin2IntVal_Type.__name__=_E
_Bin2IntVal_Object=MibScalar
bin2IntVal=_Bin2IntVal_Object((1,3,6,1,4,1,22626,1,5,2,7,3),_Bin2IntVal_Type())
bin2IntVal.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2IntVal.setStatus(_B)
class _Bin2AlarmStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin2AlarmStr_Type.__name__=_D
_Bin2AlarmStr_Object=MibScalar
bin2AlarmStr=_Bin2AlarmStr_Object((1,3,6,1,4,1,22626,1,5,2,7,4),_Bin2AlarmStr_Type())
bin2AlarmStr.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2AlarmStr.setStatus(_B)
class _Bin2Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin2Alarm_Type.__name__=_E
_Bin2Alarm_Object=MibScalar
bin2Alarm=_Bin2Alarm_Object((1,3,6,1,4,1,22626,1,5,2,7,5),_Bin2Alarm_Type())
bin2Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2Alarm.setStatus(_B)
_Bin3_ObjectIdentity=ObjectIdentity
bin3=_Bin3_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2,8))
class _Bin3Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Bin3Name_Type.__name__=_D
_Bin3Name_Object=MibScalar
bin3Name=_Bin3Name_Object((1,3,6,1,4,1,22626,1,5,2,8,1),_Bin3Name_Type())
bin3Name.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3Name.setStatus(_B)
class _Bin3Val_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin3Val_Type.__name__=_D
_Bin3Val_Object=MibScalar
bin3Val=_Bin3Val_Object((1,3,6,1,4,1,22626,1,5,2,8,2),_Bin3Val_Type())
bin3Val.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3Val.setStatus(_B)
class _Bin3IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Bin3IntVal_Type.__name__=_E
_Bin3IntVal_Object=MibScalar
bin3IntVal=_Bin3IntVal_Object((1,3,6,1,4,1,22626,1,5,2,8,3),_Bin3IntVal_Type())
bin3IntVal.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3IntVal.setStatus(_B)
class _Bin3AlarmStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin3AlarmStr_Type.__name__=_D
_Bin3AlarmStr_Object=MibScalar
bin3AlarmStr=_Bin3AlarmStr_Object((1,3,6,1,4,1,22626,1,5,2,8,4),_Bin3AlarmStr_Type())
bin3AlarmStr.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3AlarmStr.setStatus(_B)
class _Bin3Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin3Alarm_Type.__name__=_E
_Bin3Alarm_Object=MibScalar
bin3Alarm=_Bin3Alarm_Object((1,3,6,1,4,1,22626,1,5,2,8,5),_Bin3Alarm_Type())
bin3Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3Alarm.setStatus(_B)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,22626,1,5,3))
class _MessageString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MessageString_Type.__name__=_D
_MessageString_Object=MibScalar
messageString=_MessageString_Object((1,3,6,1,4,1,22626,1,5,3,1),_MessageString_Type())
messageString.setMaxAccess(_C)
if mibBuilder.loadTexts:messageString.setStatus(_B)
_Tables_ObjectIdentity=ObjectIdentity
tables=_Tables_ObjectIdentity((1,3,6,1,4,1,22626,1,5,4))
_HistoryTable_Object=MibTable
historyTable=_HistoryTable_Object((1,3,6,1,4,1,22626,1,5,4,1))
if mibBuilder.loadTexts:historyTable.setStatus(_B)
_HistoryEntry_Object=MibTableRow
historyEntry=_HistoryEntry_Object((1,3,6,1,4,1,22626,1,5,4,1,1))
historyEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:historyEntry.setStatus('optional')
class _Ch1value_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1value_Type.__name__=_E
_Ch1value_Object=MibTableColumn
ch1value=_Ch1value_Object((1,3,6,1,4,1,22626,1,5,4,1,1,1),_Ch1value_Type())
ch1value.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1value.setStatus(_B)
class _Ch2value_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch2value_Type.__name__=_E
_Ch2value_Object=MibTableColumn
ch2value=_Ch2value_Object((1,3,6,1,4,1,22626,1,5,4,1,1,2),_Ch2value_Type())
ch2value.setMaxAccess(_C)
if mibBuilder.loadTexts:ch2value.setStatus(_B)
class _Ch3value_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch3value_Type.__name__=_E
_Ch3value_Object=MibTableColumn
ch3value=_Ch3value_Object((1,3,6,1,4,1,22626,1,5,4,1,1,3),_Ch3value_Type())
ch3value.setMaxAccess(_C)
if mibBuilder.loadTexts:ch3value.setStatus(_B)
class _Ch4value_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch4value_Type.__name__=_E
_Ch4value_Object=MibTableColumn
ch4value=_Ch4value_Object((1,3,6,1,4,1,22626,1,5,4,1,1,4),_Ch4value_Type())
ch4value.setMaxAccess(_C)
if mibBuilder.loadTexts:ch4value.setStatus(_B)
trapTest=NotificationType((1,3,6,1,4,1,22626,0,0))
trapTest.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapTest.setStatus('')
trapNTPError=NotificationType((1,3,6,1,4,1,22626,0,1))
trapNTPError.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapNTPError.setStatus('')
trapEmailErrLogin=NotificationType((1,3,6,1,4,1,22626,0,2))
trapEmailErrLogin.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapEmailErrLogin.setStatus('')
trapEmailErrAuth=NotificationType((1,3,6,1,4,1,22626,0,3))
trapEmailErrAuth.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapEmailErrAuth.setStatus('')
trapEmailErrSome=NotificationType((1,3,6,1,4,1,22626,0,4))
trapEmailErrSome.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapEmailErrSome.setStatus('')
trapEmailErrSocket=NotificationType((1,3,6,1,4,1,22626,0,5))
trapEmailErrSocket.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapEmailErrSocket.setStatus('')
trapEmailErrDNS=NotificationType((1,3,6,1,4,1,22626,0,6))
trapEmailErrDNS.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapEmailErrDNS.setStatus('')
trapSOAPErrFile=NotificationType((1,3,6,1,4,1,22626,0,7))
trapSOAPErrFile.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapSOAPErrFile.setStatus('')
trapSOAPErrDNS=NotificationType((1,3,6,1,4,1,22626,0,8))
trapSOAPErrDNS.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapSOAPErrDNS.setStatus('')
trapSOAPErrSocket=NotificationType((1,3,6,1,4,1,22626,0,9))
trapSOAPErrSocket.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapSOAPErrSocket.setStatus('')
trapSOAPErrDelivery=NotificationType((1,3,6,1,4,1,22626,0,10))
trapSOAPErrDelivery.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapSOAPErrDelivery.setStatus('')
trapCh1HighAlarm=NotificationType((1,3,6,1,4,1,22626,0,11))
trapCh1HighAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh1HighAlarm.setStatus('')
trapCh2HighAlarm=NotificationType((1,3,6,1,4,1,22626,0,12))
trapCh2HighAlarm.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh2HighAlarm.setStatus('')
trapCh3HighAlarm=NotificationType((1,3,6,1,4,1,22626,0,13))
trapCh3HighAlarm.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh3HighAlarm.setStatus('')
trapCh4HighAlarm=NotificationType((1,3,6,1,4,1,22626,0,14))
trapCh4HighAlarm.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh4HighAlarm.setStatus('')
trapCh1LowAlarm=NotificationType((1,3,6,1,4,1,22626,0,21))
trapCh1LowAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh1LowAlarm.setStatus('')
trapCh2LowAlarm=NotificationType((1,3,6,1,4,1,22626,0,22))
trapCh2LowAlarm.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh2LowAlarm.setStatus('')
trapCh3LowAlarm=NotificationType((1,3,6,1,4,1,22626,0,23))
trapCh3LowAlarm.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh3LowAlarm.setStatus('')
trapCh4LowAlarm=NotificationType((1,3,6,1,4,1,22626,0,24))
trapCh4LowAlarm.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh4LowAlarm.setStatus('')
trapCh1ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,31))
trapCh1ClrAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh1ClrAlarm.setStatus('')
trapCh2ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,32))
trapCh2ClrAlarm.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh2ClrAlarm.setStatus('')
trapCh3ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,33))
trapCh3ClrAlarm.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh3ClrAlarm.setStatus('')
trapCh4ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,34))
trapCh4ClrAlarm.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh4ClrAlarm.setStatus('')
trapCh1Error=NotificationType((1,3,6,1,4,1,22626,0,41))
trapCh1Error.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh1Error.setStatus('')
trapCh2Error=NotificationType((1,3,6,1,4,1,22626,0,42))
trapCh2Error.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh2Error.setStatus('')
trapCh3Error=NotificationType((1,3,6,1,4,1,22626,0,43))
trapCh3Error.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh3Error.setStatus('')
trapCh4Error=NotificationType((1,3,6,1,4,1,22626,0,44))
trapCh4Error.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapCh4Error.setStatus('')
trapBin1Alarm=NotificationType((1,3,6,1,4,1,22626,0,51))
trapBin1Alarm.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapBin1Alarm.setStatus('')
trapBin2Alarm=NotificationType((1,3,6,1,4,1,22626,0,52))
trapBin2Alarm.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapBin2Alarm.setStatus('')
trapBin3Alarm=NotificationType((1,3,6,1,4,1,22626,0,53))
trapBin3Alarm.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapBin3Alarm.setStatus('')
trapBin1ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,61))
trapBin1ClrAlarm.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapBin1ClrAlarm.setStatus('')
trapBin2ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,62))
trapBin2ClrAlarm.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapBin2ClrAlarm.setStatus('')
trapBin3ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,63))
trapBin3ClrAlarm.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:trapBin3ClrAlarm.setStatus('')
mibBuilder.exportSymbols(_A,**{_D:DisplayString,'comet':comet,'trapTest':trapTest,'trapNTPError':trapNTPError,'trapEmailErrLogin':trapEmailErrLogin,'trapEmailErrAuth':trapEmailErrAuth,'trapEmailErrSome':trapEmailErrSome,'trapEmailErrSocket':trapEmailErrSocket,'trapEmailErrDNS':trapEmailErrDNS,'trapSOAPErrFile':trapSOAPErrFile,'trapSOAPErrDNS':trapSOAPErrDNS,'trapSOAPErrSocket':trapSOAPErrSocket,'trapSOAPErrDelivery':trapSOAPErrDelivery,'trapCh1HighAlarm':trapCh1HighAlarm,'trapCh2HighAlarm':trapCh2HighAlarm,'trapCh3HighAlarm':trapCh3HighAlarm,'trapCh4HighAlarm':trapCh4HighAlarm,'trapCh1LowAlarm':trapCh1LowAlarm,'trapCh2LowAlarm':trapCh2LowAlarm,'trapCh3LowAlarm':trapCh3LowAlarm,'trapCh4LowAlarm':trapCh4LowAlarm,'trapCh1ClrAlarm':trapCh1ClrAlarm,'trapCh2ClrAlarm':trapCh2ClrAlarm,'trapCh3ClrAlarm':trapCh3ClrAlarm,'trapCh4ClrAlarm':trapCh4ClrAlarm,'trapCh1Error':trapCh1Error,'trapCh2Error':trapCh2Error,'trapCh3Error':trapCh3Error,'trapCh4Error':trapCh4Error,'trapBin1Alarm':trapBin1Alarm,'trapBin2Alarm':trapBin2Alarm,'trapBin3Alarm':trapBin3Alarm,'trapBin1ClrAlarm':trapBin1ClrAlarm,'trapBin2ClrAlarm':trapBin2ClrAlarm,'trapBin3ClrAlarm':trapBin3ClrAlarm,'products':products,'p8552':p8552,'global':_pysmi_global,_F:sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'channels':channels,'channel1':channel1,_H:ch1Name,_I:ch1Val,'ch1IntVal':ch1IntVal,_J:ch1Alarm,'ch1LimHi':ch1LimHi,'ch1LimLo':ch1LimLo,'ch1LimHyst':ch1LimHyst,'ch1LimDelay':ch1LimDelay,'ch1Unit':ch1Unit,'ch1AlarmStr':ch1AlarmStr,'ch1Min':ch1Min,'ch1Max':ch1Max,'channel2':channel2,_K:ch2Name,_L:ch2Val,'ch2IntVal':ch2IntVal,_M:ch2Alarm,'ch2LimHi':ch2LimHi,'ch2LimLo':ch2LimLo,'ch2LimHyst':ch2LimHyst,'ch2LimDelay':ch2LimDelay,'ch2Unit':ch2Unit,'ch2AlarmStr':ch2AlarmStr,'ch2Min':ch2Min,'ch2Max':ch2Max,'channel3':channel3,_N:ch3Name,_O:ch3Val,'ch3IntVal':ch3IntVal,_P:ch3Alarm,'ch3LimHi':ch3LimHi,'ch3LimLo':ch3LimLo,'ch3LimHyst':ch3LimHyst,'ch3LimDelay':ch3LimDelay,'ch3Unit':ch3Unit,'ch3AlarmStr':ch3AlarmStr,'ch3Min':ch3Min,'ch3Max':ch3Max,'channel4':channel4,_Q:ch4Name,_R:ch4Val,'ch4IntVal':ch4IntVal,_S:ch4Alarm,'ch4LimHi':ch4LimHi,'ch4LimLo':ch4LimLo,'ch4LimHyst':ch4LimHyst,'ch4LimDelay':ch4LimDelay,'ch4Unit':ch4Unit,'ch4AlarmStr':ch4AlarmStr,'ch4Min':ch4Min,'ch4Max':ch4Max,'bin1':bin1,_T:bin1Name,_U:bin1Val,'bin1IntVal':bin1IntVal,'bin1AlarmStr':bin1AlarmStr,_V:bin1Alarm,'bin2':bin2,_W:bin2Name,_X:bin2Val,'bin2IntVal':bin2IntVal,'bin2AlarmStr':bin2AlarmStr,_Y:bin2Alarm,'bin3':bin3,_Z:bin3Name,_a:bin3Val,'bin3IntVal':bin3IntVal,'bin3AlarmStr':bin3AlarmStr,_b:bin3Alarm,'traps':traps,_G:messageString,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_d:ch1value,'ch2value':ch2value,'ch3value':ch3value,'ch4value':ch4value})