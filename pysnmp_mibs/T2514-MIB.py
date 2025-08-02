_K='histPress'
_J='NotificationType'
_I='pressAlarmInt'
_H='press'
_G='Integer32'
_F='DisplayString'
_E='messageString'
_D='sensorName'
_C='read-only'
_B='mandatory'
_A='T2514-MIB'
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
_T2514_ObjectIdentity=ObjectIdentity
t2514=_T2514_ObjectIdentity((1,3,6,1,4,1,22626,1,2))
_Values_ObjectIdentity=ObjectIdentity
values=_Values_ObjectIdentity((1,3,6,1,4,1,22626,1,2,1))
class _Press_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Press_Type.__name__=_F
_Press_Object=MibScalar
press=_Press_Object((1,3,6,1,4,1,22626,1,2,1,4),_Press_Type())
press.setMaxAccess(_C)
if mibBuilder.loadTexts:press.setStatus(_B)
class _PressAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_PressAlarm_Type.__name__=_F
_PressAlarm_Object=MibScalar
pressAlarm=_PressAlarm_Object((1,3,6,1,4,1,22626,1,2,1,8),_PressAlarm_Type())
pressAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:pressAlarm.setStatus(_B)
class _PressUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_PressUnit_Type.__name__=_F
_PressUnit_Object=MibScalar
pressUnit=_PressUnit_Object((1,3,6,1,4,1,22626,1,2,1,12),_PressUnit_Type())
pressUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:pressUnit.setStatus(_B)
class _PressMin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_PressMin_Type.__name__=_F
_PressMin_Object=MibScalar
pressMin=_PressMin_Object((1,3,6,1,4,1,22626,1,2,1,16),_PressMin_Type())
pressMin.setMaxAccess(_C)
if mibBuilder.loadTexts:pressMin.setStatus(_B)
class _PressMax_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_PressMax_Type.__name__=_F
_PressMax_Object=MibScalar
pressMax=_PressMax_Object((1,3,6,1,4,1,22626,1,2,1,20),_PressMax_Type())
pressMax.setMaxAccess(_C)
if mibBuilder.loadTexts:pressMax.setStatus(_B)
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
class _PressInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_PressInt_Type.__name__=_G
_PressInt_Object=MibScalar
pressInt=_PressInt_Object((1,3,6,1,4,1,22626,1,2,3,4),_PressInt_Type())
pressInt.setMaxAccess(_C)
if mibBuilder.loadTexts:pressInt.setStatus(_B)
class _PressAlarmInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_PressAlarmInt_Type.__name__=_G
_PressAlarmInt_Object=MibScalar
pressAlarmInt=_PressAlarmInt_Object((1,3,6,1,4,1,22626,1,2,3,8),_PressAlarmInt_Type())
pressAlarmInt.setMaxAccess(_C)
if mibBuilder.loadTexts:pressAlarmInt.setStatus(_B)
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,22626,1,2,4))
class _PressLowInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_PressLowInt_Type.__name__=_G
_PressLowInt_Object=MibScalar
pressLowInt=_PressLowInt_Object((1,3,6,1,4,1,22626,1,2,4,13),_PressLowInt_Type())
pressLowInt.setMaxAccess(_C)
if mibBuilder.loadTexts:pressLowInt.setStatus(_B)
class _PressHighInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_PressHighInt_Type.__name__=_G
_PressHighInt_Object=MibScalar
pressHighInt=_PressHighInt_Object((1,3,6,1,4,1,22626,1,2,4,14),_PressHighInt_Type())
pressHighInt.setMaxAccess(_C)
if mibBuilder.loadTexts:pressHighInt.setStatus(_B)
class _PressDelayInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4500))
_PressDelayInt_Type.__name__=_G
_PressDelayInt_Object=MibScalar
pressDelayInt=_PressDelayInt_Object((1,3,6,1,4,1,22626,1,2,4,15),_PressDelayInt_Type())
pressDelayInt.setMaxAccess(_C)
if mibBuilder.loadTexts:pressDelayInt.setStatus(_B)
class _PressHystInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_PressHystInt_Type.__name__=_G
_PressHystInt_Object=MibScalar
pressHystInt=_PressHystInt_Object((1,3,6,1,4,1,22626,1,2,4,16),_PressHystInt_Type())
pressHystInt.setMaxAccess(_C)
if mibBuilder.loadTexts:pressHystInt.setStatus(_B)
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
class _HistPress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistPress_Type.__name__=_G
_HistPress_Object=MibTableColumn
histPress=_HistPress_Object((1,3,6,1,4,1,22626,1,2,6,1,1,4),_HistPress_Type())
histPress.setMaxAccess(_C)
if mibBuilder.loadTexts:histPress.setStatus(_B)
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
trapPressHighAlarm=NotificationType((1,3,6,1,4,1,22626,0,14))
trapPressHighAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapPressHighAlarm.setStatus('')
trapPressLowAlarm=NotificationType((1,3,6,1,4,1,22626,0,24))
trapPressLowAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapPressLowAlarm.setStatus('')
trapPressClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,34))
trapPressClrAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapPressClrAlarm.setStatus('')
trapPressError=NotificationType((1,3,6,1,4,1,22626,0,44))
trapPressError.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapPressError.setStatus('')
mibBuilder.exportSymbols(_A,**{_F:DisplayString,'comet':comet,'trapTest':trapTest,'trapNTPError':trapNTPError,'trapEmailErrLogin':trapEmailErrLogin,'trapEmailErrAuth':trapEmailErrAuth,'trapEmailErrSome':trapEmailErrSome,'trapEmailErrSocket':trapEmailErrSocket,'trapEmailErrDNS':trapEmailErrDNS,'trapSOAPErrFile':trapSOAPErrFile,'trapSOAPErrDNS':trapSOAPErrDNS,'trapSOAPErrSocket':trapSOAPErrSocket,'trapSOAPErrDelivery':trapSOAPErrDelivery,'trapPressHighAlarm':trapPressHighAlarm,'trapPressLowAlarm':trapPressLowAlarm,'trapPressClrAlarm':trapPressClrAlarm,'trapPressError':trapPressError,'products':products,'t2514':t2514,'values':values,_H:press,'pressAlarm':pressAlarm,'pressUnit':pressUnit,'pressMin':pressMin,'pressMax':pressMax,'global':_pysmi_global,_D:sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'valuesInt':valuesInt,'pressInt':pressInt,_I:pressAlarmInt,'settings':settings,'pressLowInt':pressLowInt,'pressHighInt':pressHighInt,'pressDelayInt':pressDelayInt,'pressHystInt':pressHystInt,'traps':traps,_E:messageString,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_K:histPress})