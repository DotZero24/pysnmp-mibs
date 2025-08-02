_O='histTemp'
_N='NotificationType'
_M='compValAlarmInt'
_L='compVal'
_K='humAlarmInt'
_J='hum'
_I='tempAlarmInt'
_H='temp'
_G='DisplayString'
_F='Integer32'
_E='messageString'
_D='sensorName'
_C='read-only'
_B='mandatory'
_A='T3611-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Comet_ObjectIdentity=ObjectIdentity
comet=_Comet_ObjectIdentity((1,3,6,1,4,1,22626))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,22626,1))
_T3611_ObjectIdentity=ObjectIdentity
t3611=_T3611_ObjectIdentity((1,3,6,1,4,1,22626,1,2))
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
class _TempAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempAlarm_Type.__name__=_G
_TempAlarm_Object=MibScalar
tempAlarm=_TempAlarm_Object((1,3,6,1,4,1,22626,1,2,1,5),_TempAlarm_Type())
tempAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarm.setStatus(_B)
class _HumAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HumAlarm_Type.__name__=_G
_HumAlarm_Object=MibScalar
humAlarm=_HumAlarm_Object((1,3,6,1,4,1,22626,1,2,1,6),_HumAlarm_Type())
humAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:humAlarm.setStatus(_B)
class _CompValAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CompValAlarm_Type.__name__=_G
_CompValAlarm_Object=MibScalar
compValAlarm=_CompValAlarm_Object((1,3,6,1,4,1,22626,1,2,1,7),_CompValAlarm_Type())
compValAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:compValAlarm.setStatus(_B)
class _TempUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempUnit_Type.__name__=_G
_TempUnit_Object=MibScalar
tempUnit=_TempUnit_Object((1,3,6,1,4,1,22626,1,2,1,9),_TempUnit_Type())
tempUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:tempUnit.setStatus(_B)
class _HumUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HumUnit_Type.__name__=_G
_HumUnit_Object=MibScalar
humUnit=_HumUnit_Object((1,3,6,1,4,1,22626,1,2,1,10),_HumUnit_Type())
humUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:humUnit.setStatus(_B)
class _CompValUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CompValUnit_Type.__name__=_G
_CompValUnit_Object=MibScalar
compValUnit=_CompValUnit_Object((1,3,6,1,4,1,22626,1,2,1,11),_CompValUnit_Type())
compValUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:compValUnit.setStatus(_B)
class _TempMin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempMin_Type.__name__=_G
_TempMin_Object=MibScalar
tempMin=_TempMin_Object((1,3,6,1,4,1,22626,1,2,1,13),_TempMin_Type())
tempMin.setMaxAccess(_C)
if mibBuilder.loadTexts:tempMin.setStatus(_B)
class _HumMin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HumMin_Type.__name__=_G
_HumMin_Object=MibScalar
humMin=_HumMin_Object((1,3,6,1,4,1,22626,1,2,1,14),_HumMin_Type())
humMin.setMaxAccess(_C)
if mibBuilder.loadTexts:humMin.setStatus(_B)
class _CompValMin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CompValMin_Type.__name__=_G
_CompValMin_Object=MibScalar
compValMin=_CompValMin_Object((1,3,6,1,4,1,22626,1,2,1,15),_CompValMin_Type())
compValMin.setMaxAccess(_C)
if mibBuilder.loadTexts:compValMin.setStatus(_B)
class _TempMax_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempMax_Type.__name__=_G
_TempMax_Object=MibScalar
tempMax=_TempMax_Object((1,3,6,1,4,1,22626,1,2,1,17),_TempMax_Type())
tempMax.setMaxAccess(_C)
if mibBuilder.loadTexts:tempMax.setStatus(_B)
class _HumMax_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HumMax_Type.__name__=_G
_HumMax_Object=MibScalar
humMax=_HumMax_Object((1,3,6,1,4,1,22626,1,2,1,18),_HumMax_Type())
humMax.setMaxAccess(_C)
if mibBuilder.loadTexts:humMax.setStatus(_B)
class _CompValMax_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CompValMax_Type.__name__=_G
_CompValMax_Object=MibScalar
compValMax=_CompValMax_Object((1,3,6,1,4,1,22626,1,2,1,19),_CompValMax_Type())
compValMax.setMaxAccess(_C)
if mibBuilder.loadTexts:compValMax.setStatus(_B)
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
_DeviceType_Type.__name__=_F
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,22626,1,2,2,3),_DeviceType_Type())
deviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceType.setStatus(_B)
_ValuesInt_ObjectIdentity=ObjectIdentity
valuesInt=_ValuesInt_ObjectIdentity((1,3,6,1,4,1,22626,1,2,3))
class _TempInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempInt_Type.__name__=_F
_TempInt_Object=MibScalar
tempInt=_TempInt_Object((1,3,6,1,4,1,22626,1,2,3,1),_TempInt_Type())
tempInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempInt.setStatus(_B)
class _HumInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HumInt_Type.__name__=_F
_HumInt_Object=MibScalar
humInt=_HumInt_Object((1,3,6,1,4,1,22626,1,2,3,2),_HumInt_Type())
humInt.setMaxAccess(_C)
if mibBuilder.loadTexts:humInt.setStatus(_B)
class _CompValInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_CompValInt_Type.__name__=_F
_CompValInt_Object=MibScalar
compValInt=_CompValInt_Object((1,3,6,1,4,1,22626,1,2,3,3),_CompValInt_Type())
compValInt.setMaxAccess(_C)
if mibBuilder.loadTexts:compValInt.setStatus(_B)
class _TempAlarmInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_TempAlarmInt_Type.__name__=_F
_TempAlarmInt_Object=MibScalar
tempAlarmInt=_TempAlarmInt_Object((1,3,6,1,4,1,22626,1,2,3,5),_TempAlarmInt_Type())
tempAlarmInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarmInt.setStatus(_B)
class _HumAlarmInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HumAlarmInt_Type.__name__=_F
_HumAlarmInt_Object=MibScalar
humAlarmInt=_HumAlarmInt_Object((1,3,6,1,4,1,22626,1,2,3,6),_HumAlarmInt_Type())
humAlarmInt.setMaxAccess(_C)
if mibBuilder.loadTexts:humAlarmInt.setStatus(_B)
class _CompValAlarmInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CompValAlarmInt_Type.__name__=_F
_CompValAlarmInt_Object=MibScalar
compValAlarmInt=_CompValAlarmInt_Object((1,3,6,1,4,1,22626,1,2,3,7),_CompValAlarmInt_Type())
compValAlarmInt.setMaxAccess(_C)
if mibBuilder.loadTexts:compValAlarmInt.setStatus(_B)
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,22626,1,2,4))
class _TempLowInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempLowInt_Type.__name__=_F
_TempLowInt_Object=MibScalar
tempLowInt=_TempLowInt_Object((1,3,6,1,4,1,22626,1,2,4,1),_TempLowInt_Type())
tempLowInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempLowInt.setStatus(_B)
class _TempHighInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempHighInt_Type.__name__=_F
_TempHighInt_Object=MibScalar
tempHighInt=_TempHighInt_Object((1,3,6,1,4,1,22626,1,2,4,2),_TempHighInt_Type())
tempHighInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempHighInt.setStatus(_B)
class _HumLowInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HumLowInt_Type.__name__=_F
_HumLowInt_Object=MibScalar
humLowInt=_HumLowInt_Object((1,3,6,1,4,1,22626,1,2,4,3),_HumLowInt_Type())
humLowInt.setMaxAccess(_C)
if mibBuilder.loadTexts:humLowInt.setStatus(_B)
class _HumHighInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HumHighInt_Type.__name__=_F
_HumHighInt_Object=MibScalar
humHighInt=_HumHighInt_Object((1,3,6,1,4,1,22626,1,2,4,4),_HumHighInt_Type())
humHighInt.setMaxAccess(_C)
if mibBuilder.loadTexts:humHighInt.setStatus(_B)
class _CompValLowInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_CompValLowInt_Type.__name__=_F
_CompValLowInt_Object=MibScalar
compValLowInt=_CompValLowInt_Object((1,3,6,1,4,1,22626,1,2,4,5),_CompValLowInt_Type())
compValLowInt.setMaxAccess(_C)
if mibBuilder.loadTexts:compValLowInt.setStatus(_B)
class _CompValHighInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_CompValHighInt_Type.__name__=_F
_CompValHighInt_Object=MibScalar
compValHighInt=_CompValHighInt_Object((1,3,6,1,4,1,22626,1,2,4,6),_CompValHighInt_Type())
compValHighInt.setMaxAccess(_C)
if mibBuilder.loadTexts:compValHighInt.setStatus(_B)
class _TempDelayInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4500))
_TempDelayInt_Type.__name__=_F
_TempDelayInt_Object=MibScalar
tempDelayInt=_TempDelayInt_Object((1,3,6,1,4,1,22626,1,2,4,7),_TempDelayInt_Type())
tempDelayInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempDelayInt.setStatus(_B)
class _HumDelayInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4500))
_HumDelayInt_Type.__name__=_F
_HumDelayInt_Object=MibScalar
humDelayInt=_HumDelayInt_Object((1,3,6,1,4,1,22626,1,2,4,8),_HumDelayInt_Type())
humDelayInt.setMaxAccess(_C)
if mibBuilder.loadTexts:humDelayInt.setStatus(_B)
class _CompValDelayInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4500))
_CompValDelayInt_Type.__name__=_F
_CompValDelayInt_Object=MibScalar
compValDelayInt=_CompValDelayInt_Object((1,3,6,1,4,1,22626,1,2,4,9),_CompValDelayInt_Type())
compValDelayInt.setMaxAccess(_C)
if mibBuilder.loadTexts:compValDelayInt.setStatus(_B)
class _TempHystInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_TempHystInt_Type.__name__=_F
_TempHystInt_Object=MibScalar
tempHystInt=_TempHystInt_Object((1,3,6,1,4,1,22626,1,2,4,10),_TempHystInt_Type())
tempHystInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempHystInt.setStatus(_B)
class _HumHystInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_HumHystInt_Type.__name__=_F
_HumHystInt_Object=MibScalar
humHystInt=_HumHystInt_Object((1,3,6,1,4,1,22626,1,2,4,11),_HumHystInt_Type())
humHystInt.setMaxAccess(_C)
if mibBuilder.loadTexts:humHystInt.setStatus(_B)
class _CompValHystInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CompValHystInt_Type.__name__=_F
_CompValHystInt_Object=MibScalar
compValHystInt=_CompValHystInt_Object((1,3,6,1,4,1,22626,1,2,4,12),_CompValHystInt_Type())
compValHystInt.setMaxAccess(_C)
if mibBuilder.loadTexts:compValHystInt.setStatus(_B)
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
historyEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:historyEntry.setStatus('optional')
class _HistTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistTemp_Type.__name__=_F
_HistTemp_Object=MibTableColumn
histTemp=_HistTemp_Object((1,3,6,1,4,1,22626,1,2,6,1,1,1),_HistTemp_Type())
histTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:histTemp.setStatus(_B)
class _HistHum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistHum_Type.__name__=_F
_HistHum_Object=MibTableColumn
histHum=_HistHum_Object((1,3,6,1,4,1,22626,1,2,6,1,1,2),_HistHum_Type())
histHum.setMaxAccess(_C)
if mibBuilder.loadTexts:histHum.setStatus(_B)
class _HistCompVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistCompVal_Type.__name__=_F
_HistCompVal_Object=MibTableColumn
histCompVal=_HistCompVal_Object((1,3,6,1,4,1,22626,1,2,6,1,1,3),_HistCompVal_Type())
histCompVal.setMaxAccess(_C)
if mibBuilder.loadTexts:histCompVal.setStatus(_B)
trapTest=NotificationType((1,3,6,1,4,1,22626,0,0))
trapTest.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapTest.setStatus('')
trapNTPError=NotificationType((1,3,6,1,4,1,22626,0,1))
trapNTPError.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapNTPError.setStatus('')
trapEmailErrLogin=NotificationType((1,3,6,1,4,1,22626,0,2))
trapEmailErrLogin.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapEmailErrLogin.setStatus('')
trapEmailErrAuth=NotificationType((1,3,6,1,4,1,22626,0,3))
trapEmailErrAuth.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapEmailErrAuth.setStatus('')
trapEmailErrSome=NotificationType((1,3,6,1,4,1,22626,0,4))
trapEmailErrSome.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapEmailErrSome.setStatus('')
trapEmailErrSocket=NotificationType((1,3,6,1,4,1,22626,0,5))
trapEmailErrSocket.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapEmailErrSocket.setStatus('')
trapEmailErrDNS=NotificationType((1,3,6,1,4,1,22626,0,6))
trapEmailErrDNS.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapEmailErrDNS.setStatus('')
trapSOAPErrFile=NotificationType((1,3,6,1,4,1,22626,0,7))
trapSOAPErrFile.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapSOAPErrFile.setStatus('')
trapSOAPErrDNS=NotificationType((1,3,6,1,4,1,22626,0,8))
trapSOAPErrDNS.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapSOAPErrDNS.setStatus('')
trapSOAPErrSocket=NotificationType((1,3,6,1,4,1,22626,0,9))
trapSOAPErrSocket.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapSOAPErrSocket.setStatus('')
trapSOAPErrDelivery=NotificationType((1,3,6,1,4,1,22626,0,10))
trapSOAPErrDelivery.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapSOAPErrDelivery.setStatus('')
trapTempHighAlarm=NotificationType((1,3,6,1,4,1,22626,0,11))
trapTempHighAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapTempHighAlarm.setStatus('')
trapHumHighAlarm=NotificationType((1,3,6,1,4,1,22626,0,12))
trapHumHighAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:trapHumHighAlarm.setStatus('')
trapCompValHighAlarm=NotificationType((1,3,6,1,4,1,22626,0,13))
trapCompValHighAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:trapCompValHighAlarm.setStatus('')
trapTempLowAlarm=NotificationType((1,3,6,1,4,1,22626,0,21))
trapTempLowAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapTempLowAlarm.setStatus('')
trapHumLowAlarm=NotificationType((1,3,6,1,4,1,22626,0,22))
trapHumLowAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:trapHumLowAlarm.setStatus('')
trapCompValLowAlarm=NotificationType((1,3,6,1,4,1,22626,0,23))
trapCompValLowAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:trapCompValLowAlarm.setStatus('')
trapTempClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,31))
trapTempClrAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapTempClrAlarm.setStatus('')
trapHumClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,32))
trapHumClrAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:trapHumClrAlarm.setStatus('')
trapCompValClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,33))
trapCompValClrAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:trapCompValClrAlarm.setStatus('')
trapTempError=NotificationType((1,3,6,1,4,1,22626,0,41))
trapTempError.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapTempError.setStatus('')
trapHumError=NotificationType((1,3,6,1,4,1,22626,0,42))
trapHumError.setObjects(*((_A,_D),(_A,_E),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:trapHumError.setStatus('')
trapCompValError=NotificationType((1,3,6,1,4,1,22626,0,43))
trapCompValError.setObjects(*((_A,_D),(_A,_E),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:trapCompValError.setStatus('')
mibBuilder.exportSymbols(_A,**{_G:DisplayString,'comet':comet,'trapTest':trapTest,'trapNTPError':trapNTPError,'trapEmailErrLogin':trapEmailErrLogin,'trapEmailErrAuth':trapEmailErrAuth,'trapEmailErrSome':trapEmailErrSome,'trapEmailErrSocket':trapEmailErrSocket,'trapEmailErrDNS':trapEmailErrDNS,'trapSOAPErrFile':trapSOAPErrFile,'trapSOAPErrDNS':trapSOAPErrDNS,'trapSOAPErrSocket':trapSOAPErrSocket,'trapSOAPErrDelivery':trapSOAPErrDelivery,'trapTempHighAlarm':trapTempHighAlarm,'trapHumHighAlarm':trapHumHighAlarm,'trapCompValHighAlarm':trapCompValHighAlarm,'trapTempLowAlarm':trapTempLowAlarm,'trapHumLowAlarm':trapHumLowAlarm,'trapCompValLowAlarm':trapCompValLowAlarm,'trapTempClrAlarm':trapTempClrAlarm,'trapHumClrAlarm':trapHumClrAlarm,'trapCompValClrAlarm':trapCompValClrAlarm,'trapTempError':trapTempError,'trapHumError':trapHumError,'trapCompValError':trapCompValError,'products':products,'t3611':t3611,'values':values,_H:temp,_J:hum,_L:compVal,'tempAlarm':tempAlarm,'humAlarm':humAlarm,'compValAlarm':compValAlarm,'tempUnit':tempUnit,'humUnit':humUnit,'compValUnit':compValUnit,'tempMin':tempMin,'humMin':humMin,'compValMin':compValMin,'tempMax':tempMax,'humMax':humMax,'compValMax':compValMax,'global':_pysmi_global,_D:sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'valuesInt':valuesInt,'tempInt':tempInt,'humInt':humInt,'compValInt':compValInt,_I:tempAlarmInt,_K:humAlarmInt,_M:compValAlarmInt,'settings':settings,'tempLowInt':tempLowInt,'tempHighInt':tempHighInt,'humLowInt':humLowInt,'humHighInt':humHighInt,'compValLowInt':compValLowInt,'compValHighInt':compValHighInt,'tempDelayInt':tempDelayInt,'humDelayInt':humDelayInt,'compValDelayInt':compValDelayInt,'tempHystInt':tempHystInt,'humHystInt':humHystInt,'compValHystInt':compValHystInt,'traps':traps,_E:messageString,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_O:histTemp,'histHum':histHum,'histCompVal':histCompVal})