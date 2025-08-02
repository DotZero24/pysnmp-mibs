_F='OctetString'
_E='read-only'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'PhysAddress','TextualConvention','TruthValue')
swTimeMIB=ModuleIdentity((1,3,6,1,4,1,171,12,10))
class _SwTimeCapacity_Type(Bits):namedValues=NamedValues(*(('systemTime',0),('sntp',1),('summerTime',2),('realTimeClock',3)))
_SwTimeCapacity_Type.__name__='Bits'
_SwTimeCapacity_Object=MibScalar
swTimeCapacity=_SwTimeCapacity_Object((1,3,6,1,4,1,171,12,10,1),_SwTimeCapacity_Type())
swTimeCapacity.setMaxAccess(_E)
if mibBuilder.loadTexts:swTimeCapacity.setStatus(_A)
_SwCurrentClock_Type=DateAndTime
_SwCurrentClock_Object=MibScalar
swCurrentClock=_SwCurrentClock_Object((1,3,6,1,4,1,171,12,10,2),_SwCurrentClock_Type())
swCurrentClock.setMaxAccess(_B)
if mibBuilder.loadTexts:swCurrentClock.setStatus(_A)
_SwClockLostOnReboot_Type=TruthValue
_SwClockLostOnReboot_Object=MibScalar
swClockLostOnReboot=_SwClockLostOnReboot_Object((1,3,6,1,4,1,171,12,10,3),_SwClockLostOnReboot_Type())
swClockLostOnReboot.setMaxAccess(_E)
if mibBuilder.loadTexts:swClockLostOnReboot.setStatus(_A)
_SwSystemTime_ObjectIdentity=ObjectIdentity
swSystemTime=_SwSystemTime_ObjectIdentity((1,3,6,1,4,1,171,12,10,10))
class _SwSystemCurrentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwSystemCurrentTime_Type.__name__=_D
_SwSystemCurrentTime_Object=MibScalar
swSystemCurrentTime=_SwSystemCurrentTime_Object((1,3,6,1,4,1,171,12,10,10,1),_SwSystemCurrentTime_Type())
swSystemCurrentTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swSystemCurrentTime.setStatus(_A)
class _SwSystemUpTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwSystemUpTime_Type.__name__=_D
_SwSystemUpTime_Object=MibScalar
swSystemUpTime=_SwSystemUpTime_Object((1,3,6,1,4,1,171,12,10,10,2),_SwSystemUpTime_Type())
swSystemUpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swSystemUpTime.setStatus(_A)
class _SwSystemBootTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwSystemBootTime_Type.__name__=_D
_SwSystemBootTime_Object=MibScalar
swSystemBootTime=_SwSystemBootTime_Object((1,3,6,1,4,1,171,12,10,10,3),_SwSystemBootTime_Type())
swSystemBootTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swSystemBootTime.setStatus(_A)
class _SwSystemTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-779,839))
_SwSystemTimeZone_Type.__name__=_C
_SwSystemTimeZone_Object=MibScalar
swSystemTimeZone=_SwSystemTimeZone_Object((1,3,6,1,4,1,171,12,10,10,4),_SwSystemTimeZone_Type())
swSystemTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:swSystemTimeZone.setStatus(_A)
_SwSNTP_ObjectIdentity=ObjectIdentity
swSNTP=_SwSNTP_ObjectIdentity((1,3,6,1,4,1,171,12,10,11))
class _SwSNTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('disabled',2),('enabled',3)))
_SwSNTPState_Type.__name__=_C
_SwSNTPState_Object=MibScalar
swSNTPState=_SwSNTPState_Object((1,3,6,1,4,1,171,12,10,11,1),_SwSNTPState_Type())
swSNTPState.setMaxAccess(_B)
if mibBuilder.loadTexts:swSNTPState.setStatus(_A)
class _SwSNTPTimeSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('system',0),('server1',1),('server2',2),('ipv6server1',3),('ipv6server2',4)))
_SwSNTPTimeSource_Type.__name__=_C
_SwSNTPTimeSource_Object=MibScalar
swSNTPTimeSource=_SwSNTPTimeSource_Object((1,3,6,1,4,1,171,12,10,11,2),_SwSNTPTimeSource_Type())
swSNTPTimeSource.setMaxAccess(_E)
if mibBuilder.loadTexts:swSNTPTimeSource.setStatus(_A)
_SwSNTPServer1IPAddr_Type=IpAddress
_SwSNTPServer1IPAddr_Object=MibScalar
swSNTPServer1IPAddr=_SwSNTPServer1IPAddr_Object((1,3,6,1,4,1,171,12,10,11,3),_SwSNTPServer1IPAddr_Type())
swSNTPServer1IPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swSNTPServer1IPAddr.setStatus(_A)
_SwSNTPServer2IPAddr_Type=IpAddress
_SwSNTPServer2IPAddr_Object=MibScalar
swSNTPServer2IPAddr=_SwSNTPServer2IPAddr_Object((1,3,6,1,4,1,171,12,10,11,4),_SwSNTPServer2IPAddr_Type())
swSNTPServer2IPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swSNTPServer2IPAddr.setStatus(_A)
class _SwSNTPPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,99999))
_SwSNTPPollInterval_Type.__name__=_C
_SwSNTPPollInterval_Object=MibScalar
swSNTPPollInterval=_SwSNTPPollInterval_Object((1,3,6,1,4,1,171,12,10,11,5),_SwSNTPPollInterval_Type())
swSNTPPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:swSNTPPollInterval.setStatus(_A)
_SwSNTPIPv6Server1IPAddr_Type=Ipv6Address
_SwSNTPIPv6Server1IPAddr_Object=MibScalar
swSNTPIPv6Server1IPAddr=_SwSNTPIPv6Server1IPAddr_Object((1,3,6,1,4,1,171,12,10,11,6),_SwSNTPIPv6Server1IPAddr_Type())
swSNTPIPv6Server1IPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swSNTPIPv6Server1IPAddr.setStatus(_A)
_SwSNTPIPv6Server2IPAddr_Type=Ipv6Address
_SwSNTPIPv6Server2IPAddr_Object=MibScalar
swSNTPIPv6Server2IPAddr=_SwSNTPIPv6Server2IPAddr_Object((1,3,6,1,4,1,171,12,10,11,7),_SwSNTPIPv6Server2IPAddr_Type())
swSNTPIPv6Server2IPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swSNTPIPv6Server2IPAddr.setStatus(_A)
class _SwSNTPIPv6Server1InterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwSNTPIPv6Server1InterfaceName_Type.__name__=_D
_SwSNTPIPv6Server1InterfaceName_Object=MibScalar
swSNTPIPv6Server1InterfaceName=_SwSNTPIPv6Server1InterfaceName_Object((1,3,6,1,4,1,171,12,10,11,8),_SwSNTPIPv6Server1InterfaceName_Type())
swSNTPIPv6Server1InterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swSNTPIPv6Server1InterfaceName.setStatus(_A)
class _SwSNTPIPv6Server2InterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwSNTPIPv6Server2InterfaceName_Type.__name__=_D
_SwSNTPIPv6Server2InterfaceName_Object=MibScalar
swSNTPIPv6Server2InterfaceName=_SwSNTPIPv6Server2InterfaceName_Object((1,3,6,1,4,1,171,12,10,11,9),_SwSNTPIPv6Server2InterfaceName_Type())
swSNTPIPv6Server2InterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swSNTPIPv6Server2InterfaceName.setStatus(_A)
_SwSummerTime_ObjectIdentity=ObjectIdentity
swSummerTime=_SwSummerTime_ObjectIdentity((1,3,6,1,4,1,171,12,10,12))
class _SwSummerTimeStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disable',0),('repeating',1),('annual',2)))
_SwSummerTimeStatus_Type.__name__=_C
_SwSummerTimeStatus_Object=MibScalar
swSummerTimeStatus=_SwSummerTimeStatus_Object((1,3,6,1,4,1,171,12,10,12,1),_SwSummerTimeStatus_Type())
swSummerTimeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swSummerTimeStatus.setStatus(_A)
class _SwSummerTimeOffset_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_SwSummerTimeOffset_Type.__name__=_C
_SwSummerTimeOffset_Object=MibScalar
swSummerTimeOffset=_SwSummerTimeOffset_Object((1,3,6,1,4,1,171,12,10,12,2),_SwSummerTimeOffset_Type())
swSummerTimeOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:swSummerTimeOffset.setStatus(_A)
if mibBuilder.loadTexts:swSummerTimeOffset.setUnits('Minutes')
class _SwRepeatSummerTimeStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SwRepeatSummerTimeStart_Type.__name__=_F
_SwRepeatSummerTimeStart_Object=MibScalar
swRepeatSummerTimeStart=_SwRepeatSummerTimeStart_Object((1,3,6,1,4,1,171,12,10,12,3),_SwRepeatSummerTimeStart_Type())
swRepeatSummerTimeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:swRepeatSummerTimeStart.setStatus(_A)
class _SwRepeatSummerTimeEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SwRepeatSummerTimeEnd_Type.__name__=_F
_SwRepeatSummerTimeEnd_Object=MibScalar
swRepeatSummerTimeEnd=_SwRepeatSummerTimeEnd_Object((1,3,6,1,4,1,171,12,10,12,4),_SwRepeatSummerTimeEnd_Type())
swRepeatSummerTimeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:swRepeatSummerTimeEnd.setStatus(_A)
class _SwAnnualSummerTimeStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwAnnualSummerTimeStart_Type.__name__=_F
_SwAnnualSummerTimeStart_Object=MibScalar
swAnnualSummerTimeStart=_SwAnnualSummerTimeStart_Object((1,3,6,1,4,1,171,12,10,12,5),_SwAnnualSummerTimeStart_Type())
swAnnualSummerTimeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:swAnnualSummerTimeStart.setStatus(_A)
class _SwAnnualSummerTimeEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwAnnualSummerTimeEnd_Type.__name__=_F
_SwAnnualSummerTimeEnd_Object=MibScalar
swAnnualSummerTimeEnd=_SwAnnualSummerTimeEnd_Object((1,3,6,1,4,1,171,12,10,12,6),_SwAnnualSummerTimeEnd_Type())
swAnnualSummerTimeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:swAnnualSummerTimeEnd.setStatus(_A)
_SwTimeNotifPrefix_ObjectIdentity=ObjectIdentity
swTimeNotifPrefix=_SwTimeNotifPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,10,13))
mibBuilder.exportSymbols('TIME-MIB',**{'swTimeMIB':swTimeMIB,'swTimeCapacity':swTimeCapacity,'swCurrentClock':swCurrentClock,'swClockLostOnReboot':swClockLostOnReboot,'swSystemTime':swSystemTime,'swSystemCurrentTime':swSystemCurrentTime,'swSystemUpTime':swSystemUpTime,'swSystemBootTime':swSystemBootTime,'swSystemTimeZone':swSystemTimeZone,'swSNTP':swSNTP,'swSNTPState':swSNTPState,'swSNTPTimeSource':swSNTPTimeSource,'swSNTPServer1IPAddr':swSNTPServer1IPAddr,'swSNTPServer2IPAddr':swSNTPServer2IPAddr,'swSNTPPollInterval':swSNTPPollInterval,'swSNTPIPv6Server1IPAddr':swSNTPIPv6Server1IPAddr,'swSNTPIPv6Server2IPAddr':swSNTPIPv6Server2IPAddr,'swSNTPIPv6Server1InterfaceName':swSNTPIPv6Server1InterfaceName,'swSNTPIPv6Server2InterfaceName':swSNTPIPv6Server2InterfaceName,'swSummerTime':swSummerTime,'swSummerTimeStatus':swSummerTimeStatus,'swSummerTimeOffset':swSummerTimeOffset,'swRepeatSummerTimeStart':swRepeatSummerTimeStart,'swRepeatSummerTimeEnd':swRepeatSummerTimeEnd,'swAnnualSummerTimeStart':swAnnualSummerTimeStart,'swAnnualSummerTimeEnd':swAnnualSummerTimeEnd,'swTimeNotifPrefix':swTimeNotifPrefix})