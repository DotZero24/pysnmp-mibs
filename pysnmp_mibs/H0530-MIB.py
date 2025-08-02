_T='histTemp'
_S='NotificationType'
_R='re2Int'
_Q='re1Int'
_P='bin3AlarmInt'
_O='bin3Int'
_N='bin2AlarmInt'
_M='bin2Int'
_L='bin1AlarmInt'
_K='bin1Int'
_J='tempAlarm2Int'
_I='tempAlarm1Int'
_H='temp'
_G='DisplayString'
_F='messageString'
_E='sensorName'
_D='Integer32'
_C='read-only'
_B='mandatory'
_A='H0530-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_S,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_S,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Comet_ObjectIdentity=ObjectIdentity
comet=_Comet_ObjectIdentity((1,3,6,1,4,1,22626))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,22626,1))
_H0530_ObjectIdentity=ObjectIdentity
h0530=_H0530_ObjectIdentity((1,3,6,1,4,1,22626,1,2))
_Values_ObjectIdentity=ObjectIdentity
values=_Values_ObjectIdentity((1,3,6,1,4,1,22626,1,2,1))
class _Temp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Temp_Type.__name__=_G
_Temp_Object=MibScalar
temp=_Temp_Object((1,3,6,1,4,1,22626,1,2,1,1),_Temp_Type())
temp.setMaxAccess(_C)
if mibBuilder.loadTexts:temp.setStatus(_B)
class _Bin1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin1_Type.__name__=_G
_Bin1_Object=MibScalar
bin1=_Bin1_Object((1,3,6,1,4,1,22626,1,2,1,5),_Bin1_Type())
bin1.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1.setStatus(_B)
class _Bin2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin2_Type.__name__=_G
_Bin2_Object=MibScalar
bin2=_Bin2_Object((1,3,6,1,4,1,22626,1,2,1,6),_Bin2_Type())
bin2.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2.setStatus(_B)
class _Bin3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin3_Type.__name__=_G
_Bin3_Object=MibScalar
bin3=_Bin3_Object((1,3,6,1,4,1,22626,1,2,1,7),_Bin3_Type())
bin3.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3.setStatus(_B)
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
class _TempAlarm2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempAlarm2_Type.__name__=_G
_TempAlarm2_Object=MibScalar
tempAlarm2=_TempAlarm2_Object((1,3,6,1,4,1,22626,1,2,1,14),_TempAlarm2_Type())
tempAlarm2.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarm2.setStatus(_B)
class _Bin1Alarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin1Alarm_Type.__name__=_G
_Bin1Alarm_Object=MibScalar
bin1Alarm=_Bin1Alarm_Object((1,3,6,1,4,1,22626,1,2,1,18),_Bin1Alarm_Type())
bin1Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1Alarm.setStatus(_B)
class _Bin2Alarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin2Alarm_Type.__name__=_G
_Bin2Alarm_Object=MibScalar
bin2Alarm=_Bin2Alarm_Object((1,3,6,1,4,1,22626,1,2,1,19),_Bin2Alarm_Type())
bin2Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2Alarm.setStatus(_B)
class _Bin3Alarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Bin3Alarm_Type.__name__=_G
_Bin3Alarm_Object=MibScalar
bin3Alarm=_Bin3Alarm_Object((1,3,6,1,4,1,22626,1,2,1,20),_Bin3Alarm_Type())
bin3Alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3Alarm.setStatus(_B)
class _TempUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TempUnit_Type.__name__=_G
_TempUnit_Object=MibScalar
tempUnit=_TempUnit_Object((1,3,6,1,4,1,22626,1,2,1,21),_TempUnit_Type())
tempUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:tempUnit.setStatus(_B)
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
class _Bin1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin1Int_Type.__name__=_D
_Bin1Int_Object=MibScalar
bin1Int=_Bin1Int_Object((1,3,6,1,4,1,22626,1,2,3,5),_Bin1Int_Type())
bin1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1Int.setStatus(_B)
class _Bin2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin2Int_Type.__name__=_D
_Bin2Int_Object=MibScalar
bin2Int=_Bin2Int_Object((1,3,6,1,4,1,22626,1,2,3,6),_Bin2Int_Type())
bin2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2Int.setStatus(_B)
class _Bin3Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin3Int_Type.__name__=_D
_Bin3Int_Object=MibScalar
bin3Int=_Bin3Int_Object((1,3,6,1,4,1,22626,1,2,3,7),_Bin3Int_Type())
bin3Int.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3Int.setStatus(_B)
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
class _TempAlarm2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_TempAlarm2Int_Type.__name__=_D
_TempAlarm2Int_Object=MibScalar
tempAlarm2Int=_TempAlarm2Int_Object((1,3,6,1,4,1,22626,1,2,3,14),_TempAlarm2Int_Type())
tempAlarm2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAlarm2Int.setStatus(_B)
class _Bin1AlarmInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin1AlarmInt_Type.__name__=_D
_Bin1AlarmInt_Object=MibScalar
bin1AlarmInt=_Bin1AlarmInt_Object((1,3,6,1,4,1,22626,1,2,3,18),_Bin1AlarmInt_Type())
bin1AlarmInt.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1AlarmInt.setStatus(_B)
class _Bin2AlarmInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin2AlarmInt_Type.__name__=_D
_Bin2AlarmInt_Object=MibScalar
bin2AlarmInt=_Bin2AlarmInt_Object((1,3,6,1,4,1,22626,1,2,3,19),_Bin2AlarmInt_Type())
bin2AlarmInt.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2AlarmInt.setStatus(_B)
class _Bin3AlarmInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin3AlarmInt_Type.__name__=_D
_Bin3AlarmInt_Object=MibScalar
bin3AlarmInt=_Bin3AlarmInt_Object((1,3,6,1,4,1,22626,1,2,3,20),_Bin3AlarmInt_Type())
bin3AlarmInt.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3AlarmInt.setStatus(_B)
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,22626,1,2,4))
class _TempLim1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempLim1Int_Type.__name__=_D
_TempLim1Int_Object=MibScalar
tempLim1Int=_TempLim1Int_Object((1,3,6,1,4,1,22626,1,2,4,1),_TempLim1Int_Type())
tempLim1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempLim1Int.setStatus(_B)
class _TempLim2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_TempLim2Int_Type.__name__=_D
_TempLim2Int_Object=MibScalar
tempLim2Int=_TempLim2Int_Object((1,3,6,1,4,1,22626,1,2,4,5),_TempLim2Int_Type())
tempLim2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempLim2Int.setStatus(_B)
class _TempHyst1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_TempHyst1Int_Type.__name__=_D
_TempHyst1Int_Object=MibScalar
tempHyst1Int=_TempHyst1Int_Object((1,3,6,1,4,1,22626,1,2,4,9),_TempHyst1Int_Type())
tempHyst1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempHyst1Int.setStatus(_B)
class _TempHyst2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_TempHyst2Int_Type.__name__=_D
_TempHyst2Int_Object=MibScalar
tempHyst2Int=_TempHyst2Int_Object((1,3,6,1,4,1,22626,1,2,4,13),_TempHyst2Int_Type())
tempHyst2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempHyst2Int.setStatus(_B)
class _TempDelay1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_TempDelay1Int_Type.__name__=_D
_TempDelay1Int_Object=MibScalar
tempDelay1Int=_TempDelay1Int_Object((1,3,6,1,4,1,22626,1,2,4,17),_TempDelay1Int_Type())
tempDelay1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempDelay1Int.setStatus(_B)
class _TempDelay2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_TempDelay2Int_Type.__name__=_D
_TempDelay2Int_Object=MibScalar
tempDelay2Int=_TempDelay2Int_Object((1,3,6,1,4,1,22626,1,2,4,21),_TempDelay2Int_Type())
tempDelay2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempDelay2Int.setStatus(_B)
class _TempType1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_TempType1Int_Type.__name__=_D
_TempType1Int_Object=MibScalar
tempType1Int=_TempType1Int_Object((1,3,6,1,4,1,22626,1,2,4,25),_TempType1Int_Type())
tempType1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempType1Int.setStatus(_B)
class _TempType2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_TempType2Int_Type.__name__=_D
_TempType2Int_Object=MibScalar
tempType2Int=_TempType2Int_Object((1,3,6,1,4,1,22626,1,2,4,29),_TempType2Int_Type())
tempType2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:tempType2Int.setStatus(_B)
class _Bin1DelayInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Bin1DelayInt_Type.__name__=_D
_Bin1DelayInt_Object=MibScalar
bin1DelayInt=_Bin1DelayInt_Object((1,3,6,1,4,1,22626,1,2,4,33),_Bin1DelayInt_Type())
bin1DelayInt.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1DelayInt.setStatus(_B)
class _Bin2DelayInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Bin2DelayInt_Type.__name__=_D
_Bin2DelayInt_Object=MibScalar
bin2DelayInt=_Bin2DelayInt_Object((1,3,6,1,4,1,22626,1,2,4,34),_Bin2DelayInt_Type())
bin2DelayInt.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2DelayInt.setStatus(_B)
class _Bin3DelayInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Bin3DelayInt_Type.__name__=_D
_Bin3DelayInt_Object=MibScalar
bin3DelayInt=_Bin3DelayInt_Object((1,3,6,1,4,1,22626,1,2,4,35),_Bin3DelayInt_Type())
bin3DelayInt.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3DelayInt.setStatus(_B)
class _Bin1TypeInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Bin1TypeInt_Type.__name__=_D
_Bin1TypeInt_Object=MibScalar
bin1TypeInt=_Bin1TypeInt_Object((1,3,6,1,4,1,22626,1,2,4,36),_Bin1TypeInt_Type())
bin1TypeInt.setMaxAccess(_C)
if mibBuilder.loadTexts:bin1TypeInt.setStatus(_B)
class _Bin2TypeInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Bin2TypeInt_Type.__name__=_D
_Bin2TypeInt_Object=MibScalar
bin2TypeInt=_Bin2TypeInt_Object((1,3,6,1,4,1,22626,1,2,4,37),_Bin2TypeInt_Type())
bin2TypeInt.setMaxAccess(_C)
if mibBuilder.loadTexts:bin2TypeInt.setStatus(_B)
class _Bin3TypeInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Bin3TypeInt_Type.__name__=_D
_Bin3TypeInt_Object=MibScalar
bin3TypeInt=_Bin3TypeInt_Object((1,3,6,1,4,1,22626,1,2,4,38),_Bin3TypeInt_Type())
bin3TypeInt.setMaxAccess(_C)
if mibBuilder.loadTexts:bin3TypeInt.setStatus(_B)
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
historyEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:historyEntry.setStatus('optional')
class _HistTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistTemp_Type.__name__=_D
_HistTemp_Object=MibTableColumn
histTemp=_HistTemp_Object((1,3,6,1,4,1,22626,1,2,6,1,1,1),_HistTemp_Type())
histTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:histTemp.setStatus(_B)
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
trapTempAlarm1.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapTempAlarm1.setStatus('')
trapTempAlarm2=NotificationType((1,3,6,1,4,1,22626,0,21))
trapTempAlarm2.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:trapTempAlarm2.setStatus('')
trapTempClrAlarm1=NotificationType((1,3,6,1,4,1,22626,0,31))
trapTempClrAlarm1.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapTempClrAlarm1.setStatus('')
trapTempClrAlarm2=NotificationType((1,3,6,1,4,1,22626,0,41))
trapTempClrAlarm2.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:trapTempClrAlarm2.setStatus('')
trapBin1Alarm=NotificationType((1,3,6,1,4,1,22626,0,51))
trapBin1Alarm.setObjects(*((_A,_E),(_A,_F),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:trapBin1Alarm.setStatus('')
trapBin2Alarm=NotificationType((1,3,6,1,4,1,22626,0,52))
trapBin2Alarm.setObjects(*((_A,_E),(_A,_F),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:trapBin2Alarm.setStatus('')
trapBin3Alarm=NotificationType((1,3,6,1,4,1,22626,0,53))
trapBin3Alarm.setObjects(*((_A,_E),(_A,_F),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:trapBin3Alarm.setStatus('')
trapBin1ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,61))
trapBin1ClrAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:trapBin1ClrAlarm.setStatus('')
trapBin2ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,62))
trapBin2ClrAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:trapBin2ClrAlarm.setStatus('')
trapBin3ClrAlarm=NotificationType((1,3,6,1,4,1,22626,0,63))
trapBin3ClrAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:trapBin3ClrAlarm.setStatus('')
trapRelay1Closed=NotificationType((1,3,6,1,4,1,22626,0,70))
trapRelay1Closed.setObjects(*((_A,_E),(_A,_F),(_A,_Q)))
if mibBuilder.loadTexts:trapRelay1Closed.setStatus('')
trapRelay2Closed=NotificationType((1,3,6,1,4,1,22626,0,71))
trapRelay2Closed.setObjects(*((_A,_E),(_A,_F),(_A,_R)))
if mibBuilder.loadTexts:trapRelay2Closed.setStatus('')
trapRelay1Open=NotificationType((1,3,6,1,4,1,22626,0,72))
trapRelay1Open.setObjects(*((_A,_E),(_A,_F),(_A,_Q)))
if mibBuilder.loadTexts:trapRelay1Open.setStatus('')
trapRelay2Open=NotificationType((1,3,6,1,4,1,22626,0,73))
trapRelay2Open.setObjects(*((_A,_E),(_A,_F),(_A,_R)))
if mibBuilder.loadTexts:trapRelay2Open.setStatus('')
trapAcousticActivated=NotificationType((1,3,6,1,4,1,22626,0,74))
trapAcousticActivated.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapAcousticActivated.setStatus('')
trapAcousticDeactivated=NotificationType((1,3,6,1,4,1,22626,0,75))
trapAcousticDeactivated.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapAcousticDeactivated.setStatus('')
mibBuilder.exportSymbols(_A,**{_G:DisplayString,'comet':comet,'trapTest':trapTest,'trapNTPError':trapNTPError,'trapEmailErrLogin':trapEmailErrLogin,'trapEmailErrAuth':trapEmailErrAuth,'trapEmailErrSome':trapEmailErrSome,'trapEmailErrSocket':trapEmailErrSocket,'trapEmailErrDNS':trapEmailErrDNS,'trapSOAPErrFile':trapSOAPErrFile,'trapSOAPErrDNS':trapSOAPErrDNS,'trapSOAPErrSocket':trapSOAPErrSocket,'trapSOAPErrDelivery':trapSOAPErrDelivery,'trapTempAlarm1':trapTempAlarm1,'trapTempAlarm2':trapTempAlarm2,'trapTempClrAlarm1':trapTempClrAlarm1,'trapTempClrAlarm2':trapTempClrAlarm2,'trapBin1Alarm':trapBin1Alarm,'trapBin2Alarm':trapBin2Alarm,'trapBin3Alarm':trapBin3Alarm,'trapBin1ClrAlarm':trapBin1ClrAlarm,'trapBin2ClrAlarm':trapBin2ClrAlarm,'trapBin3ClrAlarm':trapBin3ClrAlarm,'trapRelay1Closed':trapRelay1Closed,'trapRelay2Closed':trapRelay2Closed,'trapRelay1Open':trapRelay1Open,'trapRelay2Open':trapRelay2Open,'trapAcousticActivated':trapAcousticActivated,'trapAcousticDeactivated':trapAcousticDeactivated,'products':products,'h0530':h0530,'values':values,_H:temp,'bin1':bin1,'bin2':bin2,'bin3':bin3,'re1':re1,'re2':re2,'tempAlarm1':tempAlarm1,'tempAlarm2':tempAlarm2,'bin1Alarm':bin1Alarm,'bin2Alarm':bin2Alarm,'bin3Alarm':bin3Alarm,'tempUnit':tempUnit,'global':_pysmi_global,_E:sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'valuesInt':valuesInt,'tempInt':tempInt,_K:bin1Int,_M:bin2Int,_O:bin3Int,_Q:re1Int,_R:re2Int,_I:tempAlarm1Int,_J:tempAlarm2Int,_L:bin1AlarmInt,_N:bin2AlarmInt,_P:bin3AlarmInt,'settings':settings,'tempLim1Int':tempLim1Int,'tempLim2Int':tempLim2Int,'tempHyst1Int':tempHyst1Int,'tempHyst2Int':tempHyst2Int,'tempDelay1Int':tempDelay1Int,'tempDelay2Int':tempDelay2Int,'tempType1Int':tempType1Int,'tempType2Int':tempType2Int,'bin1DelayInt':bin1DelayInt,'bin2DelayInt':bin2DelayInt,'bin3DelayInt':bin3DelayInt,'bin1TypeInt':bin1TypeInt,'bin2TypeInt':bin2TypeInt,'bin3TypeInt':bin3TypeInt,'traps':traps,_F:messageString,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_T:histTemp})