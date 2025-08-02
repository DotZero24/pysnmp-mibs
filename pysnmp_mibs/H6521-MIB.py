_W='histTemp'
_V='NotificationType'
_U='re2Int'
_T='re1Int'
_S='co2Alarm2Int'
_R='compValAlarm2Int'
_Q='humAlarm2Int'
_P='tempAlarm2Int'
_O='co2Alarm1Int'
_N='compValAlarm1Int'
_M='humAlarm1Int'
_L='tempAlarm1Int'
_K='co2'
_J='compVal'
_I='hum'
_H='temp'
_G='DisplayString'
_F='messageString'
_E='sensorName'
_D='Integer32'
_C='read-only'
_B='mandatory'
_A='H6521-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_V,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_V,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Comet_ObjectIdentity=ObjectIdentity
comet=_Comet_ObjectIdentity((1,3,6,1,4,1,22626))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,22626,1))
_H6521_ObjectIdentity=ObjectIdentity
h6521=_H6521_ObjectIdentity((1,3,6,1,4,1,22626,1,2))
_Values_ObjectIdentity=ObjectIdentity
values=_Values_ObjectIdentity((1,3,6,1,4,1,22626,1,2,1))
class _Temp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Temp_Type.__name__=_G
_Temp_Object=MibScalar
temp=_Temp_Object((1,3,6,1,4,1,22626,1,2,1,1),_Temp_Type())
temp.setMaxAccess(_C)
if mibBuilder.loadTexts:temp.setStatus(_B)
class _Hum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Hum_Type.__name__=_G
_Hum_Object=MibScalar
hum=_Hum_Object((1,3,6,1,4,1,22626,1,2,1,2),_Hum_Type())
hum.setMaxAccess(_C)
if mibBuilder.loadTexts:hum.setStatus(_B)
class _CompVal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CompVal_Type.__name__=_G
_CompVal_Object=MibScalar
compVal=_CompVal_Object((1,3,6,1,4,1,22626,1,2,1,3),_CompVal_Type())
compVal.setMaxAccess(_C)
if mibBuilder.loadTexts:compVal.setStatus(_B)
class _Co2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2_Type.__name__=_G
_Co2_Object=MibScalar
co2=_Co2_Object((1,3,6,1,4,1,22626,1,2,1,4),_Co2_Type())
co2.setMaxAccess(_C)
if mibBuilder.loadTexts:co2.setStatus(_B)
class _Re1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Re1_Type.__name__=_G
_Re1_Object=MibScalar
re1=_Re1_Object((1,3,6,1,4,1,22626,1,2,1,8),_Re1_Type())
re1.setMaxAccess(_C)
if mibBuilder.loadTexts:re1.setStatus(_B)
class _Re2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Re2_Type.__name__=_G
_Re2_Object=MibScalar
re2=_Re2_Object((1,3,6,1,4,1,22626,1,2,1,9),_Re2_Type())
re2.setMaxAccess(_C)
if mibBuilder.loadTexts:re2.setStatus(_B)
class _TempAlarm1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempAlarm1_Type.__name__=_G
_TempAlarm1_Object=MibScalar
tempAlarm1=_TempAlarm1_Object((1,3,6,1,4,1,22626,1,2,1,10),_TempAlarm1_Type())
tempAlarm1.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarm1.setStatus(_B)
class _HumAlarm1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HumAlarm1_Type.__name__=_G
_HumAlarm1_Object=MibScalar
humAlarm1=_HumAlarm1_Object((1,3,6,1,4,1,22626,1,2,1,11),_HumAlarm1_Type())
humAlarm1.setMaxAccess(_C)
if mibBuilder.loadTexts:humAlarm1.setStatus(_B)
class _CompValAlarm1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CompValAlarm1_Type.__name__=_G
_CompValAlarm1_Object=MibScalar
compValAlarm1=_CompValAlarm1_Object((1,3,6,1,4,1,22626,1,2,1,12),_CompValAlarm1_Type())
compValAlarm1.setMaxAccess(_C)
if mibBuilder.loadTexts:compValAlarm1.setStatus(_B)
class _Co2Alarm1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2Alarm1_Type.__name__=_G
_Co2Alarm1_Object=MibScalar
co2Alarm1=_Co2Alarm1_Object((1,3,6,1,4,1,22626,1,2,1,13),_Co2Alarm1_Type())
co2Alarm1.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Alarm1.setStatus(_B)
class _TempAlarm2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempAlarm2_Type.__name__=_G
_TempAlarm2_Object=MibScalar
tempAlarm2=_TempAlarm2_Object((1,3,6,1,4,1,22626,1,2,1,14),_TempAlarm2_Type())
tempAlarm2.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarm2.setStatus(_B)
class _HumAlarm2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HumAlarm2_Type.__name__=_G
_HumAlarm2_Object=MibScalar
humAlarm2=_HumAlarm2_Object((1,3,6,1,4,1,22626,1,2,1,15),_HumAlarm2_Type())
humAlarm2.setMaxAccess(_C)
if mibBuilder.loadTexts:humAlarm2.setStatus(_B)
class _CompValAlarm2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CompValAlarm2_Type.__name__=_G
_CompValAlarm2_Object=MibScalar
compValAlarm2=_CompValAlarm2_Object((1,3,6,1,4,1,22626,1,2,1,16),_CompValAlarm2_Type())
compValAlarm2.setMaxAccess(_C)
if mibBuilder.loadTexts:compValAlarm2.setStatus(_B)
class _Co2Alarm2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2Alarm2_Type.__name__=_G
_Co2Alarm2_Object=MibScalar
co2Alarm2=_Co2Alarm2_Object((1,3,6,1,4,1,22626,1,2,1,17),_Co2Alarm2_Type())
co2Alarm2.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Alarm2.setStatus(_B)
class _TempUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempUnit_Type.__name__=_G
_TempUnit_Object=MibScalar
tempUnit=_TempUnit_Object((1,3,6,1,4,1,22626,1,2,1,21),_TempUnit_Type())
tempUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:tempUnit.setStatus(_B)
class _HumUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HumUnit_Type.__name__=_G
_HumUnit_Object=MibScalar
humUnit=_HumUnit_Object((1,3,6,1,4,1,22626,1,2,1,22),_HumUnit_Type())
humUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:humUnit.setStatus(_B)
class _CompValUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CompValUnit_Type.__name__=_G
_CompValUnit_Object=MibScalar
compValUnit=_CompValUnit_Object((1,3,6,1,4,1,22626,1,2,1,23),_CompValUnit_Type())
compValUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:compValUnit.setStatus(_B)
class _Co2Unit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2Unit_Type.__name__=_G
_Co2Unit_Object=MibScalar
co2Unit=_Co2Unit_Object((1,3,6,1,4,1,22626,1,2,1,24),_Co2Unit_Type())
co2Unit.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Unit.setStatus(_B)
__pysmi_global_ObjectIdentity=ObjectIdentity
_pysmi_global=__pysmi_global_ObjectIdentity((1,3,6,1,4,1,22626,1,2,2))
class _SensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
_SensorName_Type.__name__=_G
_SensorName_Object=MibScalar
sensorName=_SensorName_Object((1,3,6,1,4,1,22626,1,2,2,1),_SensorName_Type())
sensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorName.setStatus(_B)
class _SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SerialNumber_Type.__name__=_G
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,22626,1,2,2,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:serialNumber.setStatus(_B)
class _DeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_DeviceType_Type.__name__=_D
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,22626,1,2,2,3),_DeviceType_Type())
deviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceType.setStatus(_B)
_ValuesInt_ObjectIdentity=ObjectIdentity
valuesInt=_ValuesInt_ObjectIdentity((1,3,6,1,4,1,22626,1,2,3))
class _TempInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempInt_Type.__name__=_D
_TempInt_Object=MibScalar
tempInt=_TempInt_Object((1,3,6,1,4,1,22626,1,2,3,1),_TempInt_Type())
tempInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempInt.setStatus(_B)
class _HumInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HumInt_Type.__name__=_D
_HumInt_Object=MibScalar
humInt=_HumInt_Object((1,3,6,1,4,1,22626,1,2,3,2),_HumInt_Type())
humInt.setMaxAccess(_C)
if mibBuilder.loadTexts:humInt.setStatus(_B)
class _CompValInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_CompValInt_Type.__name__=_D
_CompValInt_Object=MibScalar
compValInt=_CompValInt_Object((1,3,6,1,4,1,22626,1,2,3,3),_CompValInt_Type())
compValInt.setMaxAccess(_C)
if mibBuilder.loadTexts:compValInt.setStatus(_B)
class _Co2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_Co2Int_Type.__name__=_D
_Co2Int_Object=MibScalar
co2Int=_Co2Int_Object((1,3,6,1,4,1,22626,1,2,3,4),_Co2Int_Type())
co2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Int.setStatus(_B)
class _Re1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Re1Int_Type.__name__=_D
_Re1Int_Object=MibScalar
re1Int=_Re1Int_Object((1,3,6,1,4,1,22626,1,2,3,8),_Re1Int_Type())
re1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:re1Int.setStatus(_B)
class _Re2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Re2Int_Type.__name__=_D
_Re2Int_Object=MibScalar
re2Int=_Re2Int_Object((1,3,6,1,4,1,22626,1,2,3,9),_Re2Int_Type())
re2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:re2Int.setStatus(_B)
class _TempAlarm1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_TempAlarm1Int_Type.__name__=_D
_TempAlarm1Int_Object=MibScalar
tempAlarm1Int=_TempAlarm1Int_Object((1,3,6,1,4,1,22626,1,2,3,10),_TempAlarm1Int_Type())
tempAlarm1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarm1Int.setStatus(_B)
class _HumAlarm1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HumAlarm1Int_Type.__name__=_D
_HumAlarm1Int_Object=MibScalar
humAlarm1Int=_HumAlarm1Int_Object((1,3,6,1,4,1,22626,1,2,3,11),_HumAlarm1Int_Type())
humAlarm1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humAlarm1Int.setStatus(_B)
class _CompValAlarm1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CompValAlarm1Int_Type.__name__=_D
_CompValAlarm1Int_Object=MibScalar
compValAlarm1Int=_CompValAlarm1Int_Object((1,3,6,1,4,1,22626,1,2,3,12),_CompValAlarm1Int_Type())
compValAlarm1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValAlarm1Int.setStatus(_B)
class _Co2Alarm1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Co2Alarm1Int_Type.__name__=_D
_Co2Alarm1Int_Object=MibScalar
co2Alarm1Int=_Co2Alarm1Int_Object((1,3,6,1,4,1,22626,1,2,3,13),_Co2Alarm1Int_Type())
co2Alarm1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Alarm1Int.setStatus(_B)
class _TempAlarm2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_TempAlarm2Int_Type.__name__=_D
_TempAlarm2Int_Object=MibScalar
tempAlarm2Int=_TempAlarm2Int_Object((1,3,6,1,4,1,22626,1,2,3,14),_TempAlarm2Int_Type())
tempAlarm2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarm2Int.setStatus(_B)
class _HumAlarm2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HumAlarm2Int_Type.__name__=_D
_HumAlarm2Int_Object=MibScalar
humAlarm2Int=_HumAlarm2Int_Object((1,3,6,1,4,1,22626,1,2,3,15),_HumAlarm2Int_Type())
humAlarm2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humAlarm2Int.setStatus(_B)
class _CompValAlarm2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CompValAlarm2Int_Type.__name__=_D
_CompValAlarm2Int_Object=MibScalar
compValAlarm2Int=_CompValAlarm2Int_Object((1,3,6,1,4,1,22626,1,2,3,16),_CompValAlarm2Int_Type())
compValAlarm2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValAlarm2Int.setStatus(_B)
class _Co2Alarm2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Co2Alarm2Int_Type.__name__=_D
_Co2Alarm2Int_Object=MibScalar
co2Alarm2Int=_Co2Alarm2Int_Object((1,3,6,1,4,1,22626,1,2,3,17),_Co2Alarm2Int_Type())
co2Alarm2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Alarm2Int.setStatus(_B)
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,22626,1,2,4))
class _TempLim1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempLim1Int_Type.__name__=_D
_TempLim1Int_Object=MibScalar
tempLim1Int=_TempLim1Int_Object((1,3,6,1,4,1,22626,1,2,4,1),_TempLim1Int_Type())
tempLim1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempLim1Int.setStatus(_B)
class _HumLim1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HumLim1Int_Type.__name__=_D
_HumLim1Int_Object=MibScalar
humLim1Int=_HumLim1Int_Object((1,3,6,1,4,1,22626,1,2,4,2),_HumLim1Int_Type())
humLim1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humLim1Int.setStatus(_B)
class _CompValLim1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_CompValLim1Int_Type.__name__=_D
_CompValLim1Int_Object=MibScalar
compValLim1Int=_CompValLim1Int_Object((1,3,6,1,4,1,22626,1,2,4,3),_CompValLim1Int_Type())
compValLim1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValLim1Int.setStatus(_B)
class _Co2Lim1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_Co2Lim1Int_Type.__name__=_D
_Co2Lim1Int_Object=MibScalar
co2Lim1Int=_Co2Lim1Int_Object((1,3,6,1,4,1,22626,1,2,4,4),_Co2Lim1Int_Type())
co2Lim1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Lim1Int.setStatus(_B)
class _TempLim2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempLim2Int_Type.__name__=_D
_TempLim2Int_Object=MibScalar
tempLim2Int=_TempLim2Int_Object((1,3,6,1,4,1,22626,1,2,4,5),_TempLim2Int_Type())
tempLim2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempLim2Int.setStatus(_B)
class _HumLim2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HumLim2Int_Type.__name__=_D
_HumLim2Int_Object=MibScalar
humLim2Int=_HumLim2Int_Object((1,3,6,1,4,1,22626,1,2,4,6),_HumLim2Int_Type())
humLim2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humLim2Int.setStatus(_B)
class _CompValLim2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_CompValLim2Int_Type.__name__=_D
_CompValLim2Int_Object=MibScalar
compValLim2Int=_CompValLim2Int_Object((1,3,6,1,4,1,22626,1,2,4,7),_CompValLim2Int_Type())
compValLim2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValLim2Int.setStatus(_B)
class _Co2Lim2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_Co2Lim2Int_Type.__name__=_D
_Co2Lim2Int_Object=MibScalar
co2Lim2Int=_Co2Lim2Int_Object((1,3,6,1,4,1,22626,1,2,4,8),_Co2Lim2Int_Type())
co2Lim2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Lim2Int.setStatus(_B)
class _TempHyst1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_TempHyst1Int_Type.__name__=_D
_TempHyst1Int_Object=MibScalar
tempHyst1Int=_TempHyst1Int_Object((1,3,6,1,4,1,22626,1,2,4,9),_TempHyst1Int_Type())
tempHyst1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempHyst1Int.setStatus(_B)
class _HumHyst1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_HumHyst1Int_Type.__name__=_D
_HumHyst1Int_Object=MibScalar
humHyst1Int=_HumHyst1Int_Object((1,3,6,1,4,1,22626,1,2,4,10),_HumHyst1Int_Type())
humHyst1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humHyst1Int.setStatus(_B)
class _CompValHyst1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CompValHyst1Int_Type.__name__=_D
_CompValHyst1Int_Object=MibScalar
compValHyst1Int=_CompValHyst1Int_Object((1,3,6,1,4,1,22626,1,2,4,11),_CompValHyst1Int_Type())
compValHyst1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValHyst1Int.setStatus(_B)
class _Co2Hyst1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Co2Hyst1Int_Type.__name__=_D
_Co2Hyst1Int_Object=MibScalar
co2Hyst1Int=_Co2Hyst1Int_Object((1,3,6,1,4,1,22626,1,2,4,12),_Co2Hyst1Int_Type())
co2Hyst1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Hyst1Int.setStatus(_B)
class _TempHyst2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_TempHyst2Int_Type.__name__=_D
_TempHyst2Int_Object=MibScalar
tempHyst2Int=_TempHyst2Int_Object((1,3,6,1,4,1,22626,1,2,4,13),_TempHyst2Int_Type())
tempHyst2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempHyst2Int.setStatus(_B)
class _HumHyst2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_HumHyst2Int_Type.__name__=_D
_HumHyst2Int_Object=MibScalar
humHyst2Int=_HumHyst2Int_Object((1,3,6,1,4,1,22626,1,2,4,14),_HumHyst2Int_Type())
humHyst2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humHyst2Int.setStatus(_B)
class _CompValHyst2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CompValHyst2Int_Type.__name__=_D
_CompValHyst2Int_Object=MibScalar
compValHyst2Int=_CompValHyst2Int_Object((1,3,6,1,4,1,22626,1,2,4,15),_CompValHyst2Int_Type())
compValHyst2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValHyst2Int.setStatus(_B)
class _Co2Hyst2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Co2Hyst2Int_Type.__name__=_D
_Co2Hyst2Int_Object=MibScalar
co2Hyst2Int=_Co2Hyst2Int_Object((1,3,6,1,4,1,22626,1,2,4,16),_Co2Hyst2Int_Type())
co2Hyst2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Hyst2Int.setStatus(_B)
class _TempDelay1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_TempDelay1Int_Type.__name__=_D
_TempDelay1Int_Object=MibScalar
tempDelay1Int=_TempDelay1Int_Object((1,3,6,1,4,1,22626,1,2,4,17),_TempDelay1Int_Type())
tempDelay1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempDelay1Int.setStatus(_B)
class _HumDelay1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_HumDelay1Int_Type.__name__=_D
_HumDelay1Int_Object=MibScalar
humDelay1Int=_HumDelay1Int_Object((1,3,6,1,4,1,22626,1,2,4,18),_HumDelay1Int_Type())
humDelay1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humDelay1Int.setStatus(_B)
class _CompValDelay1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_CompValDelay1Int_Type.__name__=_D
_CompValDelay1Int_Object=MibScalar
compValDelay1Int=_CompValDelay1Int_Object((1,3,6,1,4,1,22626,1,2,4,19),_CompValDelay1Int_Type())
compValDelay1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValDelay1Int.setStatus(_B)
class _Co2Delay1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Co2Delay1Int_Type.__name__=_D
_Co2Delay1Int_Object=MibScalar
co2Delay1Int=_Co2Delay1Int_Object((1,3,6,1,4,1,22626,1,2,4,20),_Co2Delay1Int_Type())
co2Delay1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Delay1Int.setStatus(_B)
class _TempDelay2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_TempDelay2Int_Type.__name__=_D
_TempDelay2Int_Object=MibScalar
tempDelay2Int=_TempDelay2Int_Object((1,3,6,1,4,1,22626,1,2,4,21),_TempDelay2Int_Type())
tempDelay2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempDelay2Int.setStatus(_B)
class _HumDelay2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_HumDelay2Int_Type.__name__=_D
_HumDelay2Int_Object=MibScalar
humDelay2Int=_HumDelay2Int_Object((1,3,6,1,4,1,22626,1,2,4,22),_HumDelay2Int_Type())
humDelay2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humDelay2Int.setStatus(_B)
class _CompValDelay2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_CompValDelay2Int_Type.__name__=_D
_CompValDelay2Int_Object=MibScalar
compValDelay2Int=_CompValDelay2Int_Object((1,3,6,1,4,1,22626,1,2,4,23),_CompValDelay2Int_Type())
compValDelay2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValDelay2Int.setStatus(_B)
class _Co2Delay2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Co2Delay2Int_Type.__name__=_D
_Co2Delay2Int_Object=MibScalar
co2Delay2Int=_Co2Delay2Int_Object((1,3,6,1,4,1,22626,1,2,4,24),_Co2Delay2Int_Type())
co2Delay2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Delay2Int.setStatus(_B)
class _TempType1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_TempType1Int_Type.__name__=_D
_TempType1Int_Object=MibScalar
tempType1Int=_TempType1Int_Object((1,3,6,1,4,1,22626,1,2,4,25),_TempType1Int_Type())
tempType1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempType1Int.setStatus(_B)
class _HumType1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HumType1Int_Type.__name__=_D
_HumType1Int_Object=MibScalar
humType1Int=_HumType1Int_Object((1,3,6,1,4,1,22626,1,2,4,26),_HumType1Int_Type())
humType1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humType1Int.setStatus(_B)
class _CompValType1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CompValType1Int_Type.__name__=_D
_CompValType1Int_Object=MibScalar
compValType1Int=_CompValType1Int_Object((1,3,6,1,4,1,22626,1,2,4,27),_CompValType1Int_Type())
compValType1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValType1Int.setStatus(_B)
class _Co2Type1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Co2Type1Int_Type.__name__=_D
_Co2Type1Int_Object=MibScalar
co2Type1Int=_Co2Type1Int_Object((1,3,6,1,4,1,22626,1,2,4,28),_Co2Type1Int_Type())
co2Type1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Type1Int.setStatus(_B)
class _TempType2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_TempType2Int_Type.__name__=_D
_TempType2Int_Object=MibScalar
tempType2Int=_TempType2Int_Object((1,3,6,1,4,1,22626,1,2,4,29),_TempType2Int_Type())
tempType2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempType2Int.setStatus(_B)
class _HumType2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HumType2Int_Type.__name__=_D
_HumType2Int_Object=MibScalar
humType2Int=_HumType2Int_Object((1,3,6,1,4,1,22626,1,2,4,30),_HumType2Int_Type())
humType2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:humType2Int.setStatus(_B)
class _CompValType2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CompValType2Int_Type.__name__=_D
_CompValType2Int_Object=MibScalar
compValType2Int=_CompValType2Int_Object((1,3,6,1,4,1,22626,1,2,4,31),_CompValType2Int_Type())
compValType2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:compValType2Int.setStatus(_B)
class _Co2Type2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Co2Type2Int_Type.__name__=_D
_Co2Type2Int_Object=MibScalar
co2Type2Int=_Co2Type2Int_Object((1,3,6,1,4,1,22626,1,2,4,32),_Co2Type2Int_Type())
co2Type2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Type2Int.setStatus(_B)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,22626,1,2,5))
class _MessageString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MessageString_Type.__name__=_G
_MessageString_Object=MibScalar
messageString=_MessageString_Object((1,3,6,1,4,1,22626,1,2,5,1),_MessageString_Type())
messageString.setMaxAccess(_C)
if mibBuilder.loadTexts:messageString.setStatus(_B)
_Tables_ObjectIdentity=ObjectIdentity
tables=_Tables_ObjectIdentity((1,3,6,1,4,1,22626,1,2,6))
_HistoryTable_Object=MibTable
historyTable=_HistoryTable_Object((1,3,6,1,4,1,22626,1,2,6,1))
if mibBuilder.loadTexts:historyTable.setStatus(_B)
_HistoryEntry_Object=MibTableRow
historyEntry=_HistoryEntry_Object((1,3,6,1,4,1,22626,1,2,6,1,1))
historyEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:historyEntry.setStatus('optional')
class _HistTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistTemp_Type.__name__=_D
_HistTemp_Object=MibTableColumn
histTemp=_HistTemp_Object((1,3,6,1,4,1,22626,1,2,6,1,1,1),_HistTemp_Type())
histTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:histTemp.setStatus(_B)
class _HistHum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistHum_Type.__name__=_D
_HistHum_Object=MibTableColumn
histHum=_HistHum_Object((1,3,6,1,4,1,22626,1,2,6,1,1,2),_HistHum_Type())
histHum.setMaxAccess(_C)
if mibBuilder.loadTexts:histHum.setStatus(_B)
class _HistCompVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistCompVal_Type.__name__=_D
_HistCompVal_Object=MibTableColumn
histCompVal=_HistCompVal_Object((1,3,6,1,4,1,22626,1,2,6,1,1,3),_HistCompVal_Type())
histCompVal.setMaxAccess(_C)
if mibBuilder.loadTexts:histCompVal.setStatus(_B)
class _HistCO2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistCO2_Type.__name__=_D
_HistCO2_Object=MibTableColumn
histCO2=_HistCO2_Object((1,3,6,1,4,1,22626,1,2,6,1,1,4),_HistCO2_Type())
histCO2.setMaxAccess(_C)
if mibBuilder.loadTexts:histCO2.setStatus(_B)
trapTest=NotificationType((1,3,6,1,4,1,22626,0,0))
trapTest.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapTest.setStatus('')
trapNTPError=NotificationType((1,3,6,1,4,1,22626,0,1))
trapNTPError.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapNTPError.setStatus('')
trapEmailErrLogin=NotificationType((1,3,6,1,4,1,22626,0,2))
trapEmailErrLogin.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapEmailErrLogin.setStatus('')
trapEmailErrAuth=NotificationType((1,3,6,1,4,1,22626,0,3))
trapEmailErrAuth.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapEmailErrAuth.setStatus('')
trapEmailErrSome=NotificationType((1,3,6,1,4,1,22626,0,4))
trapEmailErrSome.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapEmailErrSome.setStatus('')
trapEmailErrSocket=NotificationType((1,3,6,1,4,1,22626,0,5))
trapEmailErrSocket.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapEmailErrSocket.setStatus('')
trapEmailErrDNS=NotificationType((1,3,6,1,4,1,22626,0,6))
trapEmailErrDNS.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapEmailErrDNS.setStatus('')
trapSOAPErrFile=NotificationType((1,3,6,1,4,1,22626,0,7))
trapSOAPErrFile.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapSOAPErrFile.setStatus('')
trapSOAPErrDNS=NotificationType((1,3,6,1,4,1,22626,0,8))
trapSOAPErrDNS.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapSOAPErrDNS.setStatus('')
trapSOAPErrSocket=NotificationType((1,3,6,1,4,1,22626,0,9))
trapSOAPErrSocket.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapSOAPErrSocket.setStatus('')
trapSOAPErrDelivery=NotificationType((1,3,6,1,4,1,22626,0,10))
trapSOAPErrDelivery.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapSOAPErrDelivery.setStatus('')
trapTempAlarm1=NotificationType((1,3,6,1,4,1,22626,0,11))
trapTempAlarm1.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:trapTempAlarm1.setStatus('')
trapHumAlarm1=NotificationType((1,3,6,1,4,1,22626,0,12))
trapHumAlarm1.setObjects(*((_A,_E),(_A,_F),(_A,_I),(_A,_M)))
if mibBuilder.loadTexts:trapHumAlarm1.setStatus('')
trapCompValAlarm1=NotificationType((1,3,6,1,4,1,22626,0,13))
trapCompValAlarm1.setObjects(*((_A,_E),(_A,_F),(_A,_J),(_A,_N)))
if mibBuilder.loadTexts:trapCompValAlarm1.setStatus('')
trapCO2Alarm1=NotificationType((1,3,6,1,4,1,22626,0,14))
trapCO2Alarm1.setObjects(*((_A,_E),(_A,_F),(_A,_K),(_A,_O)))
if mibBuilder.loadTexts:trapCO2Alarm1.setStatus('')
trapTempAlarm2=NotificationType((1,3,6,1,4,1,22626,0,21))
trapTempAlarm2.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_P)))
if mibBuilder.loadTexts:trapTempAlarm2.setStatus('')
trapHumAlarm2=NotificationType((1,3,6,1,4,1,22626,0,22))
trapHumAlarm2.setObjects(*((_A,_E),(_A,_F),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:trapHumAlarm2.setStatus('')
trapCompValAlarm2=NotificationType((1,3,6,1,4,1,22626,0,23))
trapCompValAlarm2.setObjects(*((_A,_E),(_A,_F),(_A,_J),(_A,_R)))
if mibBuilder.loadTexts:trapCompValAlarm2.setStatus('')
trapCO2Alarm2=NotificationType((1,3,6,1,4,1,22626,0,24))
trapCO2Alarm2.setObjects(*((_A,_E),(_A,_F),(_A,_K),(_A,_S)))
if mibBuilder.loadTexts:trapCO2Alarm2.setStatus('')
trapTempClrAlarm1=NotificationType((1,3,6,1,4,1,22626,0,31))
trapTempClrAlarm1.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:trapTempClrAlarm1.setStatus('')
trapHumClrAlarm1=NotificationType((1,3,6,1,4,1,22626,0,32))
trapHumClrAlarm1.setObjects(*((_A,_E),(_A,_F),(_A,_I),(_A,_M)))
if mibBuilder.loadTexts:trapHumClrAlarm1.setStatus('')
trapCompValClrAlarm1=NotificationType((1,3,6,1,4,1,22626,0,33))
trapCompValClrAlarm1.setObjects(*((_A,_E),(_A,_F),(_A,_J),(_A,_N)))
if mibBuilder.loadTexts:trapCompValClrAlarm1.setStatus('')
trapCO2ClrAlarm1=NotificationType((1,3,6,1,4,1,22626,0,34))
trapCO2ClrAlarm1.setObjects(*((_A,_E),(_A,_F),(_A,_K),(_A,_O)))
if mibBuilder.loadTexts:trapCO2ClrAlarm1.setStatus('')
trapTempClrAlarm2=NotificationType((1,3,6,1,4,1,22626,0,41))
trapTempClrAlarm2.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_P)))
if mibBuilder.loadTexts:trapTempClrAlarm2.setStatus('')
trapHumClrAlarm2=NotificationType((1,3,6,1,4,1,22626,0,42))
trapHumClrAlarm2.setObjects(*((_A,_E),(_A,_F),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:trapHumClrAlarm2.setStatus('')
trapCompValClrAlarm2=NotificationType((1,3,6,1,4,1,22626,0,43))
trapCompValClrAlarm2.setObjects(*((_A,_E),(_A,_F),(_A,_J),(_A,_R)))
if mibBuilder.loadTexts:trapCompValClrAlarm2.setStatus('')
trapCO2ClrAlarm2=NotificationType((1,3,6,1,4,1,22626,0,44))
trapCO2ClrAlarm2.setObjects(*((_A,_E),(_A,_F),(_A,_K),(_A,_S)))
if mibBuilder.loadTexts:trapCO2ClrAlarm2.setStatus('')
trapRelay1Closed=NotificationType((1,3,6,1,4,1,22626,0,70))
trapRelay1Closed.setObjects(*((_A,_E),(_A,_F),(_A,_T)))
if mibBuilder.loadTexts:trapRelay1Closed.setStatus('')
trapRelay2Closed=NotificationType((1,3,6,1,4,1,22626,0,71))
trapRelay2Closed.setObjects(*((_A,_E),(_A,_F),(_A,_U)))
if mibBuilder.loadTexts:trapRelay2Closed.setStatus('')
trapRelay1Open=NotificationType((1,3,6,1,4,1,22626,0,72))
trapRelay1Open.setObjects(*((_A,_E),(_A,_F),(_A,_T)))
if mibBuilder.loadTexts:trapRelay1Open.setStatus('')
trapRelay2Open=NotificationType((1,3,6,1,4,1,22626,0,73))
trapRelay2Open.setObjects(*((_A,_E),(_A,_F),(_A,_U)))
if mibBuilder.loadTexts:trapRelay2Open.setStatus('')
trapAcousticActivated=NotificationType((1,3,6,1,4,1,22626,0,74))
trapAcousticActivated.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapAcousticActivated.setStatus('')
trapAcousticDeactivated=NotificationType((1,3,6,1,4,1,22626,0,75))
trapAcousticDeactivated.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapAcousticDeactivated.setStatus('')
mibBuilder.exportSymbols(_A,**{_G:DisplayString,'comet':comet,'trapTest':trapTest,'trapNTPError':trapNTPError,'trapEmailErrLogin':trapEmailErrLogin,'trapEmailErrAuth':trapEmailErrAuth,'trapEmailErrSome':trapEmailErrSome,'trapEmailErrSocket':trapEmailErrSocket,'trapEmailErrDNS':trapEmailErrDNS,'trapSOAPErrFile':trapSOAPErrFile,'trapSOAPErrDNS':trapSOAPErrDNS,'trapSOAPErrSocket':trapSOAPErrSocket,'trapSOAPErrDelivery':trapSOAPErrDelivery,'trapTempAlarm1':trapTempAlarm1,'trapHumAlarm1':trapHumAlarm1,'trapCompValAlarm1':trapCompValAlarm1,'trapCO2Alarm1':trapCO2Alarm1,'trapTempAlarm2':trapTempAlarm2,'trapHumAlarm2':trapHumAlarm2,'trapCompValAlarm2':trapCompValAlarm2,'trapCO2Alarm2':trapCO2Alarm2,'trapTempClrAlarm1':trapTempClrAlarm1,'trapHumClrAlarm1':trapHumClrAlarm1,'trapCompValClrAlarm1':trapCompValClrAlarm1,'trapCO2ClrAlarm1':trapCO2ClrAlarm1,'trapTempClrAlarm2':trapTempClrAlarm2,'trapHumClrAlarm2':trapHumClrAlarm2,'trapCompValClrAlarm2':trapCompValClrAlarm2,'trapCO2ClrAlarm2':trapCO2ClrAlarm2,'trapRelay1Closed':trapRelay1Closed,'trapRelay2Closed':trapRelay2Closed,'trapRelay1Open':trapRelay1Open,'trapRelay2Open':trapRelay2Open,'trapAcousticActivated':trapAcousticActivated,'trapAcousticDeactivated':trapAcousticDeactivated,'products':products,'h6521':h6521,'values':values,_H:temp,_I:hum,_J:compVal,_K:co2,'re1':re1,'re2':re2,'tempAlarm1':tempAlarm1,'humAlarm1':humAlarm1,'compValAlarm1':compValAlarm1,'co2Alarm1':co2Alarm1,'tempAlarm2':tempAlarm2,'humAlarm2':humAlarm2,'compValAlarm2':compValAlarm2,'co2Alarm2':co2Alarm2,'tempUnit':tempUnit,'humUnit':humUnit,'compValUnit':compValUnit,'co2Unit':co2Unit,'global':_pysmi_global,_E:sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'valuesInt':valuesInt,'tempInt':tempInt,'humInt':humInt,'compValInt':compValInt,'co2Int':co2Int,_T:re1Int,_U:re2Int,_L:tempAlarm1Int,_M:humAlarm1Int,_N:compValAlarm1Int,_O:co2Alarm1Int,_P:tempAlarm2Int,_Q:humAlarm2Int,_R:compValAlarm2Int,_S:co2Alarm2Int,'settings':settings,'tempLim1Int':tempLim1Int,'humLim1Int':humLim1Int,'compValLim1Int':compValLim1Int,'co2Lim1Int':co2Lim1Int,'tempLim2Int':tempLim2Int,'humLim2Int':humLim2Int,'compValLim2Int':compValLim2Int,'co2Lim2Int':co2Lim2Int,'tempHyst1Int':tempHyst1Int,'humHyst1Int':humHyst1Int,'compValHyst1Int':compValHyst1Int,'co2Hyst1Int':co2Hyst1Int,'tempHyst2Int':tempHyst2Int,'humHyst2Int':humHyst2Int,'compValHyst2Int':compValHyst2Int,'co2Hyst2Int':co2Hyst2Int,'tempDelay1Int':tempDelay1Int,'humDelay1Int':humDelay1Int,'compValDelay1Int':compValDelay1Int,'co2Delay1Int':co2Delay1Int,'tempDelay2Int':tempDelay2Int,'humDelay2Int':humDelay2Int,'compValDelay2Int':compValDelay2Int,'co2Delay2Int':co2Delay2Int,'tempType1Int':tempType1Int,'humType1Int':humType1Int,'compValType1Int':compValType1Int,'co2Type1Int':co2Type1Int,'tempType2Int':tempType2Int,'humType2Int':humType2Int,'compValType2Int':compValType2Int,'co2Type2Int':co2Type2Int,'traps':traps,_F:messageString,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_W:histTemp,'histHum':histHum,'histCompVal':histCompVal,'histCO2':histCO2})