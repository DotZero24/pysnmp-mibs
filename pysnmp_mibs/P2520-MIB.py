_D='DisplayString'
_C='Integer32'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Comet_ObjectIdentity=ObjectIdentity
comet=_Comet_ObjectIdentity((1,3,6,1,4,1,22626))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,22626,1))
_P2520_ObjectIdentity=ObjectIdentity
p2520=_P2520_ObjectIdentity((1,3,6,1,4,1,22626,1,6))
__pysmi_global_ObjectIdentity=ObjectIdentity
_pysmi_global=__pysmi_global_ObjectIdentity((1,3,6,1,4,1,22626,1,6,1))
class _SensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
_SensorName_Type.__name__=_D
_SensorName_Object=MibScalar
sensorName=_SensorName_Object((1,3,6,1,4,1,22626,1,6,1,1),_SensorName_Type())
sensorName.setMaxAccess(_A)
if mibBuilder.loadTexts:sensorName.setStatus(_B)
class _SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SerialNumber_Type.__name__=_D
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,22626,1,6,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:serialNumber.setStatus(_B)
class _DeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_DeviceType_Type.__name__=_C
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,22626,1,6,1,3),_DeviceType_Type())
deviceType.setMaxAccess(_A)
if mibBuilder.loadTexts:deviceType.setStatus(_B)
_Channels_ObjectIdentity=ObjectIdentity
channels=_Channels_ObjectIdentity((1,3,6,1,4,1,22626,1,6,2))
_Channel1_ObjectIdentity=ObjectIdentity
channel1=_Channel1_ObjectIdentity((1,3,6,1,4,1,22626,1,6,2,1))
class _Ch1Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Ch1Name_Type.__name__=_D
_Ch1Name_Object=MibScalar
ch1Name=_Ch1Name_Object((1,3,6,1,4,1,22626,1,6,2,1,1),_Ch1Name_Type())
ch1Name.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1Name.setStatus(_B)
class _Ch1Unit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1Unit_Type.__name__=_D
_Ch1Unit_Object=MibScalar
ch1Unit=_Ch1Unit_Object((1,3,6,1,4,1,22626,1,6,2,1,2),_Ch1Unit_Type())
ch1Unit.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1Unit.setStatus(_B)
class _Ch1StrVal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_Ch1StrVal_Type.__name__=_D
_Ch1StrVal_Object=MibScalar
ch1StrVal=_Ch1StrVal_Object((1,3,6,1,4,1,22626,1,6,2,1,3),_Ch1StrVal_Type())
ch1StrVal.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1StrVal.setStatus(_B)
class _Ch1IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32010,32767))
_Ch1IntVal_Type.__name__=_C
_Ch1IntVal_Object=MibScalar
ch1IntVal=_Ch1IntVal_Object((1,3,6,1,4,1,22626,1,6,2,1,4),_Ch1IntVal_Type())
ch1IntVal.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1IntVal.setStatus(_B)
class _Ch1Int10Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32010,32767))
_Ch1Int10Val_Type.__name__=_C
_Ch1Int10Val_Object=MibScalar
ch1Int10Val=_Ch1Int10Val_Object((1,3,6,1,4,1,22626,1,6,2,1,5),_Ch1Int10Val_Type())
ch1Int10Val.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1Int10Val.setStatus(_B)
class _Ch1Int100Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32010,32767))
_Ch1Int100Val_Type.__name__=_C
_Ch1Int100Val_Object=MibScalar
ch1Int100Val=_Ch1Int100Val_Object((1,3,6,1,4,1,22626,1,6,2,1,6),_Ch1Int100Val_Type())
ch1Int100Val.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1Int100Val.setStatus(_B)
class _Ch1DwVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-320000010,2147483647))
_Ch1DwVal_Type.__name__=_C
_Ch1DwVal_Object=MibScalar
ch1DwVal=_Ch1DwVal_Object((1,3,6,1,4,1,22626,1,6,2,1,7),_Ch1DwVal_Type())
ch1DwVal.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1DwVal.setStatus(_B)
class _Ch1Dw10Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-320000010,2147483647))
_Ch1Dw10Val_Type.__name__=_C
_Ch1Dw10Val_Object=MibScalar
ch1Dw10Val=_Ch1Dw10Val_Object((1,3,6,1,4,1,22626,1,6,2,1,8),_Ch1Dw10Val_Type())
ch1Dw10Val.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1Dw10Val.setStatus(_B)
class _Ch1Dw100Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-320000010,2147483647))
_Ch1Dw100Val_Type.__name__=_C
_Ch1Dw100Val_Object=MibScalar
ch1Dw100Val=_Ch1Dw100Val_Object((1,3,6,1,4,1,22626,1,6,2,1,9),_Ch1Dw100Val_Type())
ch1Dw100Val.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1Dw100Val.setStatus(_B)
class _Ch1StrCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_Ch1StrCurrent_Type.__name__=_D
_Ch1StrCurrent_Object=MibScalar
ch1StrCurrent=_Ch1StrCurrent_Object((1,3,6,1,4,1,22626,1,6,2,1,10),_Ch1StrCurrent_Type())
ch1StrCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1StrCurrent.setStatus(_B)
class _Ch1IntCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32010,32767))
_Ch1IntCurrent_Type.__name__=_C
_Ch1IntCurrent_Object=MibScalar
ch1IntCurrent=_Ch1IntCurrent_Object((1,3,6,1,4,1,22626,1,6,2,1,11),_Ch1IntCurrent_Type())
ch1IntCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1IntCurrent.setStatus(_B)
class _Ch1IntAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Ch1IntAlarm_Type.__name__=_C
_Ch1IntAlarm_Object=MibScalar
ch1IntAlarm=_Ch1IntAlarm_Object((1,3,6,1,4,1,22626,1,6,2,1,12),_Ch1IntAlarm_Type())
ch1IntAlarm.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1IntAlarm.setStatus(_B)
class _Ch1StrAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch1StrAlarm_Type.__name__=_D
_Ch1StrAlarm_Object=MibScalar
ch1StrAlarm=_Ch1StrAlarm_Object((1,3,6,1,4,1,22626,1,6,2,1,13),_Ch1StrAlarm_Type())
ch1StrAlarm.setMaxAccess(_A)
if mibBuilder.loadTexts:ch1StrAlarm.setStatus(_B)
_Channel2_ObjectIdentity=ObjectIdentity
channel2=_Channel2_ObjectIdentity((1,3,6,1,4,1,22626,1,6,2,2))
class _Ch2Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Ch2Name_Type.__name__=_D
_Ch2Name_Object=MibScalar
ch2Name=_Ch2Name_Object((1,3,6,1,4,1,22626,1,6,2,2,1),_Ch2Name_Type())
ch2Name.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2Name.setStatus(_B)
class _Ch2Unit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch2Unit_Type.__name__=_D
_Ch2Unit_Object=MibScalar
ch2Unit=_Ch2Unit_Object((1,3,6,1,4,1,22626,1,6,2,2,2),_Ch2Unit_Type())
ch2Unit.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2Unit.setStatus(_B)
class _Ch2StrVal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_Ch2StrVal_Type.__name__=_D
_Ch2StrVal_Object=MibScalar
ch2StrVal=_Ch2StrVal_Object((1,3,6,1,4,1,22626,1,6,2,2,3),_Ch2StrVal_Type())
ch2StrVal.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2StrVal.setStatus(_B)
class _Ch2IntVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32010,32767))
_Ch2IntVal_Type.__name__=_C
_Ch2IntVal_Object=MibScalar
ch2IntVal=_Ch2IntVal_Object((1,3,6,1,4,1,22626,1,6,2,2,4),_Ch2IntVal_Type())
ch2IntVal.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2IntVal.setStatus(_B)
class _Ch2Int10Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32010,32767))
_Ch2Int10Val_Type.__name__=_C
_Ch2Int10Val_Object=MibScalar
ch2Int10Val=_Ch2Int10Val_Object((1,3,6,1,4,1,22626,1,6,2,2,5),_Ch2Int10Val_Type())
ch2Int10Val.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2Int10Val.setStatus(_B)
class _Ch2Int100Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32010,32767))
_Ch2Int100Val_Type.__name__=_C
_Ch2Int100Val_Object=MibScalar
ch2Int100Val=_Ch2Int100Val_Object((1,3,6,1,4,1,22626,1,6,2,2,6),_Ch2Int100Val_Type())
ch2Int100Val.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2Int100Val.setStatus(_B)
class _Ch2DwVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-320000010,2147483647))
_Ch2DwVal_Type.__name__=_C
_Ch2DwVal_Object=MibScalar
ch2DwVal=_Ch2DwVal_Object((1,3,6,1,4,1,22626,1,6,2,2,7),_Ch2DwVal_Type())
ch2DwVal.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2DwVal.setStatus(_B)
class _Ch2Dw10Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-320000010,2147483647))
_Ch2Dw10Val_Type.__name__=_C
_Ch2Dw10Val_Object=MibScalar
ch2Dw10Val=_Ch2Dw10Val_Object((1,3,6,1,4,1,22626,1,6,2,2,8),_Ch2Dw10Val_Type())
ch2Dw10Val.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2Dw10Val.setStatus(_B)
class _Ch2Dw100Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-320000010,2147483647))
_Ch2Dw100Val_Type.__name__=_C
_Ch2Dw100Val_Object=MibScalar
ch2Dw100Val=_Ch2Dw100Val_Object((1,3,6,1,4,1,22626,1,6,2,2,9),_Ch2Dw100Val_Type())
ch2Dw100Val.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2Dw100Val.setStatus(_B)
class _Ch2StrCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_Ch2StrCurrent_Type.__name__=_D
_Ch2StrCurrent_Object=MibScalar
ch2StrCurrent=_Ch2StrCurrent_Object((1,3,6,1,4,1,22626,1,6,2,2,10),_Ch2StrCurrent_Type())
ch2StrCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2StrCurrent.setStatus(_B)
class _Ch2IntCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32010,32767))
_Ch2IntCurrent_Type.__name__=_C
_Ch2IntCurrent_Object=MibScalar
ch2IntCurrent=_Ch2IntCurrent_Object((1,3,6,1,4,1,22626,1,6,2,2,11),_Ch2IntCurrent_Type())
ch2IntCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2IntCurrent.setStatus(_B)
class _Ch2IntAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Ch2IntAlarm_Type.__name__=_C
_Ch2IntAlarm_Object=MibScalar
ch2IntAlarm=_Ch2IntAlarm_Object((1,3,6,1,4,1,22626,1,6,2,2,12),_Ch2IntAlarm_Type())
ch2IntAlarm.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2IntAlarm.setStatus(_B)
class _Ch2StrAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Ch2StrAlarm_Type.__name__=_D
_Ch2StrAlarm_Object=MibScalar
ch2StrAlarm=_Ch2StrAlarm_Object((1,3,6,1,4,1,22626,1,6,2,2,13),_Ch2StrAlarm_Type())
ch2StrAlarm.setMaxAccess(_A)
if mibBuilder.loadTexts:ch2StrAlarm.setStatus(_B)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,22626,1,6,3))
class _MessageString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MessageString_Type.__name__=_D
_MessageString_Object=MibScalar
messageString=_MessageString_Object((1,3,6,1,4,1,22626,1,6,3,1),_MessageString_Type())
messageString.setMaxAccess(_A)
if mibBuilder.loadTexts:messageString.setStatus(_B)
mibBuilder.exportSymbols('P2520-MIB',**{_D:DisplayString,'comet':comet,'products':products,'p2520':p2520,'global':_pysmi_global,'sensorName':sensorName,'serialNumber':serialNumber,'deviceType':deviceType,'channels':channels,'channel1':channel1,'ch1Name':ch1Name,'ch1Unit':ch1Unit,'ch1StrVal':ch1StrVal,'ch1IntVal':ch1IntVal,'ch1Int10Val':ch1Int10Val,'ch1Int100Val':ch1Int100Val,'ch1DwVal':ch1DwVal,'ch1Dw10Val':ch1Dw10Val,'ch1Dw100Val':ch1Dw100Val,'ch1StrCurrent':ch1StrCurrent,'ch1IntCurrent':ch1IntCurrent,'ch1IntAlarm':ch1IntAlarm,'ch1StrAlarm':ch1StrAlarm,'channel2':channel2,'ch2Name':ch2Name,'ch2Unit':ch2Unit,'ch2StrVal':ch2StrVal,'ch2IntVal':ch2IntVal,'ch2Int10Val':ch2Int10Val,'ch2Int100Val':ch2Int100Val,'ch2DwVal':ch2DwVal,'ch2Dw10Val':ch2Dw10Val,'ch2Dw100Val':ch2Dw100Val,'ch2StrCurrent':ch2StrCurrent,'ch2IntCurrent':ch2IntCurrent,'ch2IntAlarm':ch2IntAlarm,'ch2StrAlarm':ch2StrAlarm,'traps':traps,'messageString':messageString})