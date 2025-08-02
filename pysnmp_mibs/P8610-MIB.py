_L='ch1value'
_K='NotificationType'
_J='ch1Alarm'
_I='ch1Val'
_H='ch1Name'
_G='Integer32'
_F='DisplayString'
_E='messageString'
_D='sensorName'
_C='read-only'
_B='mandatory'
_A='P8610-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Comet_ObjectIdentity=ObjectIdentity
comet=_Comet_ObjectIdentity((1,3,6,1,4,1,22626))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,22626,1))
_P8610_ObjectIdentity=ObjectIdentity
p8610=_P8610_ObjectIdentity((1,3,6,1,4,1,22626,1,5))
__pysmi_global_ObjectIdentity=ObjectIdentity
_pysmi_global=__pysmi_global_ObjectIdentity((1,3,6,1,4,1,22626,1,5,1))
class _SensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
_SensorName_Type.__name__=_F
_SensorName_Object=MibScalar
sensorName=_SensorName_Object((1,3,6,1,4,1,22626,1,5,1,1),_SensorName_Type())
sensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorName.setStatus(_B)
class _SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SerialNumber_Type.__name__=_F
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,22626,1,5,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:serialNumber.setStatus(_B)
class _DeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_DeviceType_Type.__name__=_G
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,22626,1,5,1,3),_DeviceType_Type())
deviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceType.setStatus(_B)
_Channels_ObjectIdentity=ObjectIdentity
channels=_Channels_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2))
_Channel1_ObjectIdentity=ObjectIdentity
channel1=_Channel1_ObjectIdentity((1,3,6,1,4,1,22626,1,5,2,1))
class _Ch1Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ch1Name_Type.__name__=_F
_Ch1Name_Object=MibScalar
ch1Name=_Ch1Name_Object((1,3,6,1,4,1,22626,1,5,2,1,1),_Ch1Name_Type())
ch1Name.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Name.setStatus(_B)
class _Ch1Val_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1Val_Type.__name__=_F
_Ch1Val_Object=MibScalar
ch1Val=_Ch1Val_Object((1,3,6,1,4,1,22626,1,5,2,1,2),_Ch1Val_Type())
ch1Val.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Val.setStatus(_B)
class _Ch1IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1IntVal_Type.__name__=_G
_Ch1IntVal_Object=MibScalar
ch1IntVal=_Ch1IntVal_Object((1,3,6,1,4,1,22626,1,5,2,1,3),_Ch1IntVal_Type())
ch1IntVal.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1IntVal.setStatus(_B)
class _Ch1Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Ch1Alarm_Type.__name__=_G
_Ch1Alarm_Object=MibScalar
ch1Alarm=_Ch1Alarm_Object((1,3,6,1,4,1,22626,1,5,2,1,4),_Ch1Alarm_Type())
ch1Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Alarm.setStatus(_B)
class _Ch1LimHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1LimHi_Type.__name__=_G
_Ch1LimHi_Object=MibScalar
ch1LimHi=_Ch1LimHi_Object((1,3,6,1,4,1,22626,1,5,2,1,5),_Ch1LimHi_Type())
ch1LimHi.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1LimHi.setStatus(_B)
class _Ch1LimLo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1LimLo_Type.__name__=_G
_Ch1LimLo_Object=MibScalar
ch1LimLo=_Ch1LimLo_Object((1,3,6,1,4,1,22626,1,5,2,1,6),_Ch1LimLo_Type())
ch1LimLo.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1LimLo.setStatus(_B)
class _Ch1LimHyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1LimHyst_Type.__name__=_G
_Ch1LimHyst_Object=MibScalar
ch1LimHyst=_Ch1LimHyst_Object((1,3,6,1,4,1,22626,1,5,2,1,7),_Ch1LimHyst_Type())
ch1LimHyst.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1LimHyst.setStatus(_B)
class _Ch1LimDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_Ch1LimDelay_Type.__name__=_G
_Ch1LimDelay_Object=MibScalar
ch1LimDelay=_Ch1LimDelay_Object((1,3,6,1,4,1,22626,1,5,2,1,8),_Ch1LimDelay_Type())
ch1LimDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1LimDelay.setStatus(_B)
class _Ch1Unit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1Unit_Type.__name__=_F
_Ch1Unit_Object=MibScalar
ch1Unit=_Ch1Unit_Object((1,3,6,1,4,1,22626,1,5,2,1,9),_Ch1Unit_Type())
ch1Unit.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Unit.setStatus(_B)
class _Ch1AlarmStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1AlarmStr_Type.__name__=_F
_Ch1AlarmStr_Object=MibScalar
ch1AlarmStr=_Ch1AlarmStr_Object((1,3,6,1,4,1,22626,1,5,2,1,10),_Ch1AlarmStr_Type())
ch1AlarmStr.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1AlarmStr.setStatus(_B)
class _Ch1Min_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1Min_Type.__name__=_F
_Ch1Min_Object=MibScalar
ch1Min=_Ch1Min_Object((1,3,6,1,4,1,22626,1,5,2,1,11),_Ch1Min_Type())
ch1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Min.setStatus(_B)
class _Ch1Max_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1Max_Type.__name__=_F
_Ch1Max_Object=MibScalar
ch1Max=_Ch1Max_Object((1,3,6,1,4,1,22626,1,5,2,1,12),_Ch1Max_Type())
ch1Max.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1Max.setStatus(_B)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,22626,1,5,3))
class _MessageString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MessageString_Type.__name__=_F
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
historyEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:historyEntry.setStatus('optional')
class _Ch1value_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_Ch1value_Type.__name__=_G
_Ch1value_Object=MibTableColumn
ch1value=_Ch1value_Object((1,3,6,1,4,1,22626,1,5,4,1,1,1),_Ch1value_Type())
ch1value.setMaxAccess(_C)
if mibBuilder.loadTexts:ch1value.setStatus(_B)
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
trapCh1HighAlarm=NotificationType((1,3,6,1,4,1,22626,0,11))
trapCh1HighAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapCh1HighAlarm.setStatus('')
trapCh1LowAlarm=NotificationType((1,3,6,1,4,1,22626,0,21))
trapCh1LowAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapCh1LowAlarm.setStatus('')
trapCh1ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,31))
trapCh1ClrAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapCh1ClrAlarm.setStatus('')
trapCh1Error=NotificationType((1,3,6,1,4,1,22626,0,41))
trapCh1Error.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapCh1Error.setStatus('')
mibBuilder.exportSymbols(_A,**{_F:DisplayString,'comet':comet,'trapTest':trapTest,'trapNTPError':trapNTPError,'trapEmailErrLogin':trapEmailErrLogin,'trapEmailErrAuth':trapEmailErrAuth,'trapEmailErrSome':trapEmailErrSome,'trapEmailErrSocket':trapEmailErrSocket,'trapEmailErrDNS':trapEmailErrDNS,'trapSOAPErrFile':trapSOAPErrFile,'trapSOAPErrDNS':trapSOAPErrDNS,'trapSOAPErrSocket':trapSOAPErrSocket,'trapSOAPErrDelivery':trapSOAPErrDelivery,'trapCh1HighAlarm':trapCh1HighAlarm,'trapCh1LowAlarm':trapCh1LowAlarm,'trapCh1ClrAlarm':trapCh1ClrAlarm,'trapCh1Error':trapCh1Error,'products':products,'p8610':p8610,'global':_pysmi_global,_D:sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'channels':channels,'channel1':channel1,_H:ch1Name,_I:ch1Val,'ch1IntVal':ch1IntVal,_J:ch1Alarm,'ch1LimHi':ch1LimHi,'ch1LimLo':ch1LimLo,'ch1LimHyst':ch1LimHyst,'ch1LimDelay':ch1LimDelay,'ch1Unit':ch1Unit,'ch1AlarmStr':ch1AlarmStr,'ch1Min':ch1Min,'ch1Max':ch1Max,'traps':traps,_E:messageString,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_L:ch1value})