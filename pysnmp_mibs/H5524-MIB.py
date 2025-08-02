_N='histCO2'
_M='NotificationType'
_L='re2Int'
_K='re1Int'
_J='co2Alarm2Int'
_I='co2Alarm1Int'
_H='co2'
_G='DisplayString'
_F='Integer32'
_E='messageString'
_D='sensorName'
_C='read-only'
_B='mandatory'
_A='H5524-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_M,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_M,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Comet_ObjectIdentity=ObjectIdentity
comet=_Comet_ObjectIdentity((1,3,6,1,4,1,22626))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,22626,1))
_H5524_ObjectIdentity=ObjectIdentity
h5524=_H5524_ObjectIdentity((1,3,6,1,4,1,22626,1,2))
_Values_ObjectIdentity=ObjectIdentity
values=_Values_ObjectIdentity((1,3,6,1,4,1,22626,1,2,1))
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
class _Co2Alarm1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2Alarm1_Type.__name__=_G
_Co2Alarm1_Object=MibScalar
co2Alarm1=_Co2Alarm1_Object((1,3,6,1,4,1,22626,1,2,1,13),_Co2Alarm1_Type())
co2Alarm1.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Alarm1.setStatus(_B)
class _Co2Alarm2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Co2Alarm2_Type.__name__=_G
_Co2Alarm2_Object=MibScalar
co2Alarm2=_Co2Alarm2_Object((1,3,6,1,4,1,22626,1,2,1,17),_Co2Alarm2_Type())
co2Alarm2.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Alarm2.setStatus(_B)
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
_DeviceType_Type.__name__=_F
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,22626,1,2,2,3),_DeviceType_Type())
deviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceType.setStatus(_B)
_ValuesInt_ObjectIdentity=ObjectIdentity
valuesInt=_ValuesInt_ObjectIdentity((1,3,6,1,4,1,22626,1,2,3))
class _Co2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_Co2Int_Type.__name__=_F
_Co2Int_Object=MibScalar
co2Int=_Co2Int_Object((1,3,6,1,4,1,22626,1,2,3,4),_Co2Int_Type())
co2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Int.setStatus(_B)
class _Re1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Re1Int_Type.__name__=_F
_Re1Int_Object=MibScalar
re1Int=_Re1Int_Object((1,3,6,1,4,1,22626,1,2,3,8),_Re1Int_Type())
re1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:re1Int.setStatus(_B)
class _Re2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Re2Int_Type.__name__=_F
_Re2Int_Object=MibScalar
re2Int=_Re2Int_Object((1,3,6,1,4,1,22626,1,2,3,9),_Re2Int_Type())
re2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:re2Int.setStatus(_B)
class _Co2Alarm1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Co2Alarm1Int_Type.__name__=_F
_Co2Alarm1Int_Object=MibScalar
co2Alarm1Int=_Co2Alarm1Int_Object((1,3,6,1,4,1,22626,1,2,3,13),_Co2Alarm1Int_Type())
co2Alarm1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Alarm1Int.setStatus(_B)
class _Co2Alarm2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Co2Alarm2Int_Type.__name__=_F
_Co2Alarm2Int_Object=MibScalar
co2Alarm2Int=_Co2Alarm2Int_Object((1,3,6,1,4,1,22626,1,2,3,17),_Co2Alarm2Int_Type())
co2Alarm2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Alarm2Int.setStatus(_B)
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,22626,1,2,4))
class _Co2Lim1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_Co2Lim1Int_Type.__name__=_F
_Co2Lim1Int_Object=MibScalar
co2Lim1Int=_Co2Lim1Int_Object((1,3,6,1,4,1,22626,1,2,4,4),_Co2Lim1Int_Type())
co2Lim1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Lim1Int.setStatus(_B)
class _Co2Lim2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_Co2Lim2Int_Type.__name__=_F
_Co2Lim2Int_Object=MibScalar
co2Lim2Int=_Co2Lim2Int_Object((1,3,6,1,4,1,22626,1,2,4,8),_Co2Lim2Int_Type())
co2Lim2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Lim2Int.setStatus(_B)
class _Co2Hyst1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Co2Hyst1Int_Type.__name__=_F
_Co2Hyst1Int_Object=MibScalar
co2Hyst1Int=_Co2Hyst1Int_Object((1,3,6,1,4,1,22626,1,2,4,12),_Co2Hyst1Int_Type())
co2Hyst1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Hyst1Int.setStatus(_B)
class _Co2Hyst2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Co2Hyst2Int_Type.__name__=_F
_Co2Hyst2Int_Object=MibScalar
co2Hyst2Int=_Co2Hyst2Int_Object((1,3,6,1,4,1,22626,1,2,4,16),_Co2Hyst2Int_Type())
co2Hyst2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Hyst2Int.setStatus(_B)
class _Co2Delay1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Co2Delay1Int_Type.__name__=_F
_Co2Delay1Int_Object=MibScalar
co2Delay1Int=_Co2Delay1Int_Object((1,3,6,1,4,1,22626,1,2,4,20),_Co2Delay1Int_Type())
co2Delay1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Delay1Int.setStatus(_B)
class _Co2Delay2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Co2Delay2Int_Type.__name__=_F
_Co2Delay2Int_Object=MibScalar
co2Delay2Int=_Co2Delay2Int_Object((1,3,6,1,4,1,22626,1,2,4,24),_Co2Delay2Int_Type())
co2Delay2Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Delay2Int.setStatus(_B)
class _Co2Type1Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Co2Type1Int_Type.__name__=_F
_Co2Type1Int_Object=MibScalar
co2Type1Int=_Co2Type1Int_Object((1,3,6,1,4,1,22626,1,2,4,28),_Co2Type1Int_Type())
co2Type1Int.setMaxAccess(_C)
if mibBuilder.loadTexts:co2Type1Int.setStatus(_B)
class _Co2Type2Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Co2Type2Int_Type.__name__=_F
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
historyEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:historyEntry.setStatus('optional')
class _HistCO2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5000,20000))
_HistCO2_Type.__name__=_F
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
trapCO2Alarm1=NotificationType((1,3,6,1,4,1,22626,0,14))
trapCO2Alarm1.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapCO2Alarm1.setStatus('')
trapCO2Alarm2=NotificationType((1,3,6,1,4,1,22626,0,24))
trapCO2Alarm2.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:trapCO2Alarm2.setStatus('')
trapCO2ClrAlarm1=NotificationType((1,3,6,1,4,1,22626,0,34))
trapCO2ClrAlarm1.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:trapCO2ClrAlarm1.setStatus('')
trapCO2ClrAlarm2=NotificationType((1,3,6,1,4,1,22626,0,44))
trapCO2ClrAlarm2.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:trapCO2ClrAlarm2.setStatus('')
trapRelay1Closed=NotificationType((1,3,6,1,4,1,22626,0,70))
trapRelay1Closed.setObjects(*((_A,_D),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:trapRelay1Closed.setStatus('')
trapRelay2Closed=NotificationType((1,3,6,1,4,1,22626,0,71))
trapRelay2Closed.setObjects(*((_A,_D),(_A,_E),(_A,_L)))
if mibBuilder.loadTexts:trapRelay2Closed.setStatus('')
trapRelay1Open=NotificationType((1,3,6,1,4,1,22626,0,72))
trapRelay1Open.setObjects(*((_A,_D),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:trapRelay1Open.setStatus('')
trapRelay2Open=NotificationType((1,3,6,1,4,1,22626,0,73))
trapRelay2Open.setObjects(*((_A,_D),(_A,_E),(_A,_L)))
if mibBuilder.loadTexts:trapRelay2Open.setStatus('')
trapAcousticActivated=NotificationType((1,3,6,1,4,1,22626,0,74))
trapAcousticActivated.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapAcousticActivated.setStatus('')
trapAcousticDeactivated=NotificationType((1,3,6,1,4,1,22626,0,75))
trapAcousticDeactivated.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:trapAcousticDeactivated.setStatus('')
mibBuilder.exportSymbols(_A,**{_G:DisplayString,'comet':comet,'trapTest':trapTest,'trapNTPError':trapNTPError,'trapEmailErrLogin':trapEmailErrLogin,'trapEmailErrAuth':trapEmailErrAuth,'trapEmailErrSome':trapEmailErrSome,'trapEmailErrSocket':trapEmailErrSocket,'trapEmailErrDNS':trapEmailErrDNS,'trapSOAPErrFile':trapSOAPErrFile,'trapSOAPErrDNS':trapSOAPErrDNS,'trapSOAPErrSocket':trapSOAPErrSocket,'trapSOAPErrDelivery':trapSOAPErrDelivery,'trapCO2Alarm1':trapCO2Alarm1,'trapCO2Alarm2':trapCO2Alarm2,'trapCO2ClrAlarm1':trapCO2ClrAlarm1,'trapCO2ClrAlarm2':trapCO2ClrAlarm2,'trapRelay1Closed':trapRelay1Closed,'trapRelay2Closed':trapRelay2Closed,'trapRelay1Open':trapRelay1Open,'trapRelay2Open':trapRelay2Open,'trapAcousticActivated':trapAcousticActivated,'trapAcousticDeactivated':trapAcousticDeactivated,'products':products,'h5524':h5524,'values':values,_H:co2,'re1':re1,'re2':re2,'co2Alarm1':co2Alarm1,'co2Alarm2':co2Alarm2,'co2Unit':co2Unit,'global':_pysmi_global,_D:sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'valuesInt':valuesInt,'co2Int':co2Int,_K:re1Int,_L:re2Int,_I:co2Alarm1Int,_J:co2Alarm2Int,'settings':settings,'co2Lim1Int':co2Lim1Int,'co2Lim2Int':co2Lim2Int,'co2Hyst1Int':co2Hyst1Int,'co2Hyst2Int':co2Hyst2Int,'co2Delay1Int':co2Delay1Int,'co2Delay2Int':co2Delay2Int,'co2Type1Int':co2Type1Int,'co2Type2Int':co2Type2Int,'traps':traps,_E:messageString,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_N:histCO2})