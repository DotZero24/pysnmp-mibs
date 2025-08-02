_K='histCO2'
_J='NotificationType'
_I='co2AlarmInt'
_H='co2'
_G='Integer32'
_F='DisplayString'
_E='messageString'
_D='sensorName'
_C='read-only'
_B='mandatory'
_A='T5541-MIB'
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
_T5541_ObjectIdentity=ObjectIdentity
t5541=_T5541_ObjectIdentity((1,3,6,1,4,1,22626,1,2))
_Values_ObjectIdentity=ObjectIdentity
values=_Values_ObjectIdentity((1,3,6,1,4,1,22626,1,2,1))
class _Co2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2_Type.__name__=_F
_Co2_Object=MibScalar
co2=_Co2_Object((1,3,6,1,4,1,22626,1,2,1,4),_Co2_Type())
co2.setMaxAccess(_C)
if mibBuilder.loadTexts:co2.setStatus(_B)
class _Co2Alarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2Alarm_Type.__name__=_F
_Co2Alarm_Object=MibScalar
co2Alarm=_Co2Alarm_Object((1,3,6,1,4,1,22626,1,2,1,8),_Co2Alarm_Type())
co2Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Alarm.setStatus(_B)
class _Co2Unit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2Unit_Type.__name__=_F
_Co2Unit_Object=MibScalar
co2Unit=_Co2Unit_Object((1,3,6,1,4,1,22626,1,2,1,12),_Co2Unit_Type())
co2Unit.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Unit.setStatus(_B)
class _Co2Min_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2Min_Type.__name__=_F
_Co2Min_Object=MibScalar
co2Min=_Co2Min_Object((1,3,6,1,4,1,22626,1,2,1,16),_Co2Min_Type())
co2Min.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Min.setStatus(_B)
class _Co2Max_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2Max_Type.__name__=_F
_Co2Max_Object=MibScalar
co2Max=_Co2Max_Object((1,3,6,1,4,1,22626,1,2,1,20),_Co2Max_Type())
co2Max.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Max.setStatus(_B)
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
class _Co2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_Co2Int_Type.__name__=_G
_Co2Int_Object=MibScalar
co2Int=_Co2Int_Object((1,3,6,1,4,1,22626,1,2,3,4),_Co2Int_Type())
co2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Int.setStatus(_B)
class _Co2AlarmInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Co2AlarmInt_Type.__name__=_G
_Co2AlarmInt_Object=MibScalar
co2AlarmInt=_Co2AlarmInt_Object((1,3,6,1,4,1,22626,1,2,3,8),_Co2AlarmInt_Type())
co2AlarmInt.setMaxAccess(_C)
if mibBuilder.loadTexts:co2AlarmInt.setStatus(_B)
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,22626,1,2,4))
class _Co2LowInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_Co2LowInt_Type.__name__=_G
_Co2LowInt_Object=MibScalar
co2LowInt=_Co2LowInt_Object((1,3,6,1,4,1,22626,1,2,4,13),_Co2LowInt_Type())
co2LowInt.setMaxAccess(_C)
if mibBuilder.loadTexts:co2LowInt.setStatus(_B)
class _Co2HighInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_Co2HighInt_Type.__name__=_G
_Co2HighInt_Object=MibScalar
co2HighInt=_Co2HighInt_Object((1,3,6,1,4,1,22626,1,2,4,14),_Co2HighInt_Type())
co2HighInt.setMaxAccess(_C)
if mibBuilder.loadTexts:co2HighInt.setStatus(_B)
class _Co2DelayInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4500))
_Co2DelayInt_Type.__name__=_G
_Co2DelayInt_Object=MibScalar
co2DelayInt=_Co2DelayInt_Object((1,3,6,1,4,1,22626,1,2,4,15),_Co2DelayInt_Type())
co2DelayInt.setMaxAccess(_C)
if mibBuilder.loadTexts:co2DelayInt.setStatus(_B)
class _Co2HystInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Co2HystInt_Type.__name__=_G
_Co2HystInt_Object=MibScalar
co2HystInt=_Co2HystInt_Object((1,3,6,1,4,1,22626,1,2,4,16),_Co2HystInt_Type())
co2HystInt.setMaxAccess(_C)
if mibBuilder.loadTexts:co2HystInt.setStatus(_B)
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
class _HistCO2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistCO2_Type.__name__=_G
_HistCO2_Object=MibTableColumn
histCO2=_HistCO2_Object((1,3,6,1,4,1,22626,1,2,6,1,1,4),_HistCO2_Type())
histCO2.setMaxAccess(_C)
if mibBuilder.loadTexts:histCO2.setStatus(_B)
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
trapCo2HighAlarm=NotificationType((1,3,6,1,4,1,22626,0,14))
trapCo2HighAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapCo2HighAlarm.setStatus('')
trapCo2LowAlarm=NotificationType((1,3,6,1,4,1,22626,0,24))
trapCo2LowAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapCo2LowAlarm.setStatus('')
trapCo2ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,34))
trapCo2ClrAlarm.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapCo2ClrAlarm.setStatus('')
trapCo2Error=NotificationType((1,3,6,1,4,1,22626,0,44))
trapCo2Error.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapCo2Error.setStatus('')
mibBuilder.exportSymbols(_A,**{_F:DisplayString,'comet':comet,'trapTest':trapTest,'trapNTPError':trapNTPError,'trapEmailErrLogin':trapEmailErrLogin,'trapEmailErrAuth':trapEmailErrAuth,'trapEmailErrSome':trapEmailErrSome,'trapEmailErrSocket':trapEmailErrSocket,'trapEmailErrDNS':trapEmailErrDNS,'trapSOAPErrFile':trapSOAPErrFile,'trapSOAPErrDNS':trapSOAPErrDNS,'trapSOAPErrSocket':trapSOAPErrSocket,'trapSOAPErrDelivery':trapSOAPErrDelivery,'trapCo2HighAlarm':trapCo2HighAlarm,'trapCo2LowAlarm':trapCo2LowAlarm,'trapCo2ClrAlarm':trapCo2ClrAlarm,'trapCo2Error':trapCo2Error,'products':products,'t5541':t5541,'values':values,_H:co2,'co2Alarm':co2Alarm,'co2Unit':co2Unit,'co2Min':co2Min,'co2Max':co2Max,'global':_pysmi_global,_D:sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'valuesInt':valuesInt,'co2Int':co2Int,_I:co2AlarmInt,'settings':settings,'co2LowInt':co2LowInt,'co2HighInt':co2HighInt,'co2DelayInt':co2DelayInt,'co2HystInt':co2HystInt,'traps':traps,_E:messageString,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_K:histCO2})