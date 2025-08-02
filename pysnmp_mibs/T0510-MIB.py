_K='histTemp'
_J='NotificationType'
_I='tempAlarmInt'
_H='temp'
_G='Integer32'
_F='DisplayString'
_E='messageString'
_D='sensorName'
_C='read-only'
_B='mandatory'
_A='T0510-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Comet_ObjectIdentity=ObjectIdentity
comet=_Comet_ObjectIdentity((1,3,6,1,4,1,22626))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,22626,1))
_T0510_ObjectIdentity=ObjectIdentity
t0510=_T0510_ObjectIdentity((1,3,6,1,4,1,22626,1,2))
_Values_ObjectIdentity=ObjectIdentity
values=_Values_ObjectIdentity((1,3,6,1,4,1,22626,1,2,1))
class _Temp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Temp_Type.__name__=_F
_Temp_Object=MibScalar
temp=_Temp_Object((1,3,6,1,4,1,22626,1,2,1,1),_Temp_Type())
temp.setMaxAccess(_C)
if mibBuilder.loadTexts:temp.setStatus(_B)
class _TempAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempAlarm_Type.__name__=_F
_TempAlarm_Object=MibScalar
tempAlarm=_TempAlarm_Object((1,3,6,1,4,1,22626,1,2,1,5),_TempAlarm_Type())
tempAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarm.setStatus(_B)
class _TempUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempUnit_Type.__name__=_F
_TempUnit_Object=MibScalar
tempUnit=_TempUnit_Object((1,3,6,1,4,1,22626,1,2,1,9),_TempUnit_Type())
tempUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:tempUnit.setStatus(_B)
class _TempMin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempMin_Type.__name__=_F
_TempMin_Object=MibScalar
tempMin=_TempMin_Object((1,3,6,1,4,1,22626,1,2,1,13),_TempMin_Type())
tempMin.setMaxAccess(_C)
if mibBuilder.loadTexts:tempMin.setStatus(_B)
class _TempMax_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempMax_Type.__name__=_F
_TempMax_Object=MibScalar
tempMax=_TempMax_Object((1,3,6,1,4,1,22626,1,2,1,17),_TempMax_Type())
tempMax.setMaxAccess(_C)
if mibBuilder.loadTexts:tempMax.setStatus(_B)
__pysmi_global_ObjectIdentity=ObjectIdentity
_pysmi_global=__pysmi_global_ObjectIdentity((1,3,6,1,4,1,22626,1,2,2))
class _SensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
_SensorName_Type.__name__=_F
_SensorName_Object=MibScalar
sensorName=_SensorName_Object((1,3,6,1,4,1,22626,1,2,2,1),_SensorName_Type())
sensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorName.setStatus(_B)
class _SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SerialNumber_Type.__name__=_F
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,22626,1,2,2,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:serialNumber.setStatus(_B)
class _DeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_DeviceType_Type.__name__=_G
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,22626,1,2,2,3),_DeviceType_Type())
deviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceType.setStatus(_B)
_ValuesInt_ObjectIdentity=ObjectIdentity
valuesInt=_ValuesInt_ObjectIdentity((1,3,6,1,4,1,22626,1,2,3))
class _TempInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempInt_Type.__name__=_G
_TempInt_Object=MibScalar
tempInt=_TempInt_Object((1,3,6,1,4,1,22626,1,2,3,1),_TempInt_Type())
tempInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempInt.setStatus(_B)
class _TempAlarmInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_TempAlarmInt_Type.__name__=_G
_TempAlarmInt_Object=MibScalar
tempAlarmInt=_TempAlarmInt_Object((1,3,6,1,4,1,22626,1,2,3,5),_TempAlarmInt_Type())
tempAlarmInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarmInt.setStatus(_B)
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,22626,1,2,4))
class _TempLowInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempLowInt_Type.__name__=_G
_TempLowInt_Object=MibScalar
tempLowInt=_TempLowInt_Object((1,3,6,1,4,1,22626,1,2,4,1),_TempLowInt_Type())
tempLowInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempLowInt.setStatus(_B)
class _TempHighInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempHighInt_Type.__name__=_G
_TempHighInt_Object=MibScalar
tempHighInt=_TempHighInt_Object((1,3,6,1,4,1,22626,1,2,4,2),_TempHighInt_Type())
tempHighInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempHighInt.setStatus(_B)
class _TempDelayInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4500))
_TempDelayInt_Type.__name__=_G
_TempDelayInt_Object=MibScalar
tempDelayInt=_TempDelayInt_Object((1,3,6,1,4,1,22626,1,2,4,7),_TempDelayInt_Type())
tempDelayInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempDelayInt.setStatus(_B)
class _TempHystInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_TempHystInt_Type.__name__=_G
_TempHystInt_Object=MibScalar
tempHystInt=_TempHystInt_Object((1,3,6,1,4,1,22626,1,2,4,10),_TempHystInt_Type())
tempHystInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tempHystInt.setStatus(_B)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,22626,1,2,5))
class _MessageString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MessageString_Type.__name__=_F
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
historyEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:historyEntry.setStatus('optional')
class _HistTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistTemp_Type.__name__=_G
_HistTemp_Object=MibTableColumn
histTemp=_HistTemp_Object((1,3,6,1,4,1,22626,1,2,6,1,1,1),_HistTemp_Type())
histTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:histTemp.setStatus(_B)
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
trapTempLowAlarm=NotificationType((1,3,6,1,4,1,22626,0,21))
trapTempLowAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapTempLowAlarm.setStatus('')
trapTempClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,31))
trapTempClrAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapTempClrAlarm.setStatus('')
trapTempError=NotificationType((1,3,6,1,4,1,22626,0,41))
trapTempError.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapTempError.setStatus('')
mibBuilder.exportSymbols(_A,**{_F:DisplayString,'comet':comet,'trapTest':trapTest,'trapNTPError':trapNTPError,'trapEmailErrLogin':trapEmailErrLogin,'trapEmailErrAuth':trapEmailErrAuth,'trapEmailErrSome':trapEmailErrSome,'trapEmailErrSocket':trapEmailErrSocket,'trapEmailErrDNS':trapEmailErrDNS,'trapSOAPErrFile':trapSOAPErrFile,'trapSOAPErrDNS':trapSOAPErrDNS,'trapSOAPErrSocket':trapSOAPErrSocket,'trapSOAPErrDelivery':trapSOAPErrDelivery,'trapTempHighAlarm':trapTempHighAlarm,'trapTempLowAlarm':trapTempLowAlarm,'trapTempClrAlarm':trapTempClrAlarm,'trapTempError':trapTempError,'products':products,'t0510':t0510,'values':values,_H:temp,'tempAlarm':tempAlarm,'tempUnit':tempUnit,'tempMin':tempMin,'tempMax':tempMax,'global':_pysmi_global,_D:sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'valuesInt':valuesInt,'tempInt':tempInt,_I:tempAlarmInt,'settings':settings,'tempLowInt':tempLowInt,'tempHighInt':tempHighInt,'tempDelayInt':tempDelayInt,'tempHystInt':tempHystInt,'traps':traps,_E:messageString,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_K:histTemp})