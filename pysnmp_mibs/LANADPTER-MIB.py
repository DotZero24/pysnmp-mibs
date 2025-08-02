_D='DisplayString'
_C='mandatory'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Comet_ObjectIdentity=ObjectIdentity
comet=_Comet_ObjectIdentity((1,3,6,1,4,1,22626))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,22626,1))
_Lanadapter_ObjectIdentity=ObjectIdentity
lanadapter=_Lanadapter_ObjectIdentity((1,3,6,1,4,1,22626,1,3))
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,22626,1,3,1))
class _MessageString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_MessageString_Type.__name__=_D
_MessageString_Object=MibScalar
messageString=_MessageString_Object((1,3,6,1,4,1,22626,1,3,1,1),_MessageString_Type())
messageString.setMaxAccess(_B)
if mibBuilder.loadTexts:messageString.setStatus(_C)
class _ChannelAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ChannelAlarm_Type.__name__=_A
_ChannelAlarm_Object=MibScalar
channelAlarm=_ChannelAlarm_Object((1,3,6,1,4,1,22626,1,3,1,2),_ChannelAlarm_Type())
channelAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:channelAlarm.setStatus(_C)
class _Memmory90Full_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Memmory90Full_Type.__name__=_A
_Memmory90Full_Object=MibScalar
memmory90Full=_Memmory90Full_Object((1,3,6,1,4,1,22626,1,3,1,3),_Memmory90Full_Type())
memmory90Full.setMaxAccess(_B)
if mibBuilder.loadTexts:memmory90Full.setStatus(_C)
class _Memmory100Full_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Memmory100Full_Type.__name__=_A
_Memmory100Full_Object=MibScalar
memmory100Full=_Memmory100Full_Object((1,3,6,1,4,1,22626,1,3,1,4),_Memmory100Full_Type())
memmory100Full.setMaxAccess(_B)
if mibBuilder.loadTexts:memmory100Full.setStatus(_C)
class _VccLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_VccLow_Type.__name__=_A
_VccLow_Object=MibScalar
vccLow=_VccLow_Object((1,3,6,1,4,1,22626,1,3,1,5),_VccLow_Type())
vccLow.setMaxAccess(_B)
if mibBuilder.loadTexts:vccLow.setStatus(_C)
class _BatteryEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BatteryEnd_Type.__name__=_A
_BatteryEnd_Object=MibScalar
batteryEnd=_BatteryEnd_Object((1,3,6,1,4,1,22626,1,3,1,6),_BatteryEnd_Type())
batteryEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryEnd.setStatus(_C)
class _BatteryLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BatteryLow_Type.__name__=_A
_BatteryLow_Object=MibScalar
batteryLow=_BatteryLow_Object((1,3,6,1,4,1,22626,1,3,1,7),_BatteryLow_Type())
batteryLow.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryLow.setStatus(_C)
class _CommunicationError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CommunicationError_Type.__name__=_A
_CommunicationError_Object=MibScalar
communicationError=_CommunicationError_Object((1,3,6,1,4,1,22626,1,3,1,8),_CommunicationError_Type())
communicationError.setMaxAccess(_B)
if mibBuilder.loadTexts:communicationError.setStatus(_C)
class _LoggerOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LoggerOff_Type.__name__=_A
_LoggerOff_Object=MibScalar
loggerOff=_LoggerOff_Object((1,3,6,1,4,1,22626,1,3,1,9),_LoggerOff_Type())
loggerOff.setMaxAccess(_B)
if mibBuilder.loadTexts:loggerOff.setStatus(_C)
_Channels_ObjectIdentity=ObjectIdentity
channels=_Channels_ObjectIdentity((1,3,6,1,4,1,22626,1,3,2))
_Channel1_ObjectIdentity=ObjectIdentity
channel1=_Channel1_ObjectIdentity((1,3,6,1,4,1,22626,1,3,2,1))
class _Ch1Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ch1Alarm_Type.__name__=_A
_Ch1Alarm_Object=MibScalar
ch1Alarm=_Ch1Alarm_Object((1,3,6,1,4,1,22626,1,3,2,1,1),_Ch1Alarm_Type())
ch1Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ch1Alarm.setStatus(_C)
_Channel2_ObjectIdentity=ObjectIdentity
channel2=_Channel2_ObjectIdentity((1,3,6,1,4,1,22626,1,3,2,2))
class _Ch2Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ch2Alarm_Type.__name__=_A
_Ch2Alarm_Object=MibScalar
ch2Alarm=_Ch2Alarm_Object((1,3,6,1,4,1,22626,1,3,2,2,1),_Ch2Alarm_Type())
ch2Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ch2Alarm.setStatus(_C)
_Channel3_ObjectIdentity=ObjectIdentity
channel3=_Channel3_ObjectIdentity((1,3,6,1,4,1,22626,1,3,2,3))
class _Ch3Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ch3Alarm_Type.__name__=_A
_Ch3Alarm_Object=MibScalar
ch3Alarm=_Ch3Alarm_Object((1,3,6,1,4,1,22626,1,3,2,3,1),_Ch3Alarm_Type())
ch3Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ch3Alarm.setStatus(_C)
_Channel4_ObjectIdentity=ObjectIdentity
channel4=_Channel4_ObjectIdentity((1,3,6,1,4,1,22626,1,3,2,4))
class _Ch4Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ch4Alarm_Type.__name__=_A
_Ch4Alarm_Object=MibScalar
ch4Alarm=_Ch4Alarm_Object((1,3,6,1,4,1,22626,1,3,2,4,1),_Ch4Alarm_Type())
ch4Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ch4Alarm.setStatus(_C)
_Channel5_ObjectIdentity=ObjectIdentity
channel5=_Channel5_ObjectIdentity((1,3,6,1,4,1,22626,1,3,2,5))
class _Ch5Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ch5Alarm_Type.__name__=_A
_Ch5Alarm_Object=MibScalar
ch5Alarm=_Ch5Alarm_Object((1,3,6,1,4,1,22626,1,3,2,5,1),_Ch5Alarm_Type())
ch5Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ch5Alarm.setStatus(_C)
_Channel6_ObjectIdentity=ObjectIdentity
channel6=_Channel6_ObjectIdentity((1,3,6,1,4,1,22626,1,3,2,6))
class _Ch6Alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ch6Alarm_Type.__name__=_A
_Ch6Alarm_Object=MibScalar
ch6Alarm=_Ch6Alarm_Object((1,3,6,1,4,1,22626,1,3,2,6,1),_Ch6Alarm_Type())
ch6Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ch6Alarm.setStatus(_C)
mibBuilder.exportSymbols('LANADPTER-MIB',**{_D:DisplayString,'comet':comet,'products':products,'lanadapter':lanadapter,'traps':traps,'messageString':messageString,'channelAlarm':channelAlarm,'memmory90Full':memmory90Full,'memmory100Full':memmory100Full,'vccLow':vccLow,'batteryEnd':batteryEnd,'batteryLow':batteryLow,'communicationError':communicationError,'loggerOff':loggerOff,'channels':channels,'channel1':channel1,'ch1Alarm':ch1Alarm,'channel2':channel2,'ch2Alarm':ch2Alarm,'channel3':channel3,'ch3Alarm':ch3Alarm,'channel4':channel4,'ch4Alarm':ch4Alarm,'channel5':channel5,'ch5Alarm':ch5Alarm,'channel6':channel6,'ch6Alarm':ch6Alarm})