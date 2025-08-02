_X='dpTimeSummerTimeCfgGroup'
_W='dpTimeSntpGroup'
_V='dpTimeClockGroup'
_U='dpTimeSysInfoGroup'
_T='dpTimeSummerTimeOffset'
_S='dpTimeSummerTimeEnd'
_R='dpTimeSummerTimeStart'
_Q='dpTimeSummerTimeTimeZone'
_P='dpTimeSummerTimeAutoSwitchMode'
_O='dpTimeSntpServerLastReceive'
_N='dpTimeSntpServerVersion'
_M='dpTimeSntpServerStratum'
_L='dpTimeSntpServerAddr'
_K='dpTimeSntpPollInterval'
_J='dpTimeSntpEnabled'
_I='dpTimeManagedClock'
_H='dpTimeCurrentTime'
_G='dpTimeCurrentTimeSource'
_F='Unsigned32'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='DLINKPRIME-TIME-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkPrimeTimeMIB=ModuleIdentity((1,3,6,1,4,1,171,15,23))
if mibBuilder.loadTexts:dlinkPrimeTimeMIB.setRevisions(('2014-04-26 00:00',))
class DlinkTimeSummerTimeValue(TextualConvention,OctetString):status=_A;displayHint='2d-1d-1d,1d:1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_DpTimeMIBNotifications_ObjectIdentity=ObjectIdentity
dpTimeMIBNotifications=_DpTimeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,23,0))
_DpTimeMIBObjects_ObjectIdentity=ObjectIdentity
dpTimeMIBObjects=_DpTimeMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,23,1))
_DpTimeGeneral_ObjectIdentity=ObjectIdentity
dpTimeGeneral=_DpTimeGeneral_ObjectIdentity((1,3,6,1,4,1,171,15,23,1,1))
_DpTimeSntpEnabled_Type=TruthValue
_DpTimeSntpEnabled_Object=MibScalar
dpTimeSntpEnabled=_DpTimeSntpEnabled_Object((1,3,6,1,4,1,171,15,23,1,1,1),_DpTimeSntpEnabled_Type())
dpTimeSntpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeSntpEnabled.setStatus(_A)
class _DpTimeSntpPollInterval_Type(Unsigned32):defaultValue=720;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,99999))
_DpTimeSntpPollInterval_Type.__name__=_F
_DpTimeSntpPollInterval_Object=MibScalar
dpTimeSntpPollInterval=_DpTimeSntpPollInterval_Object((1,3,6,1,4,1,171,15,23,1,1,2),_DpTimeSntpPollInterval_Type())
dpTimeSntpPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeSntpPollInterval.setStatus(_A)
_DpTimeClock_ObjectIdentity=ObjectIdentity
dpTimeClock=_DpTimeClock_ObjectIdentity((1,3,6,1,4,1,171,15,23,1,2))
_DpTimeManagedClock_Type=DateAndTime
_DpTimeManagedClock_Object=MibScalar
dpTimeManagedClock=_DpTimeManagedClock_Object((1,3,6,1,4,1,171,15,23,1,2,1),_DpTimeManagedClock_Type())
dpTimeManagedClock.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeManagedClock.setStatus(_A)
class _DpTimeCurrentTimeSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sntp',1),('noTimeSource',2)))
_DpTimeCurrentTimeSource_Type.__name__=_D
_DpTimeCurrentTimeSource_Object=MibScalar
dpTimeCurrentTimeSource=_DpTimeCurrentTimeSource_Object((1,3,6,1,4,1,171,15,23,1,2,2),_DpTimeCurrentTimeSource_Type())
dpTimeCurrentTimeSource.setMaxAccess(_E)
if mibBuilder.loadTexts:dpTimeCurrentTimeSource.setStatus(_A)
_DpTimeCurrentTime_Type=DateAndTime
_DpTimeCurrentTime_Object=MibScalar
dpTimeCurrentTime=_DpTimeCurrentTime_Object((1,3,6,1,4,1,171,15,23,1,2,3),_DpTimeCurrentTime_Type())
dpTimeCurrentTime.setMaxAccess(_E)
if mibBuilder.loadTexts:dpTimeCurrentTime.setStatus(_A)
_DpTimeSummerTime_ObjectIdentity=ObjectIdentity
dpTimeSummerTime=_DpTimeSummerTime_ObjectIdentity((1,3,6,1,4,1,171,15,23,1,2,4))
class _DpTimeSummerTimeAutoSwitchMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('date',2)))
_DpTimeSummerTimeAutoSwitchMode_Type.__name__=_D
_DpTimeSummerTimeAutoSwitchMode_Object=MibScalar
dpTimeSummerTimeAutoSwitchMode=_DpTimeSummerTimeAutoSwitchMode_Object((1,3,6,1,4,1,171,15,23,1,2,4,1),_DpTimeSummerTimeAutoSwitchMode_Type())
dpTimeSummerTimeAutoSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeSummerTimeAutoSwitchMode.setStatus(_A)
class _DpTimeSummerTimeTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-779,839))
_DpTimeSummerTimeTimeZone_Type.__name__=_D
_DpTimeSummerTimeTimeZone_Object=MibScalar
dpTimeSummerTimeTimeZone=_DpTimeSummerTimeTimeZone_Object((1,3,6,1,4,1,171,15,23,1,2,4,2),_DpTimeSummerTimeTimeZone_Type())
dpTimeSummerTimeTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeSummerTimeTimeZone.setStatus(_A)
_DpTimeSummerTimeStart_Type=DlinkTimeSummerTimeValue
_DpTimeSummerTimeStart_Object=MibScalar
dpTimeSummerTimeStart=_DpTimeSummerTimeStart_Object((1,3,6,1,4,1,171,15,23,1,2,4,3),_DpTimeSummerTimeStart_Type())
dpTimeSummerTimeStart.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeSummerTimeStart.setStatus(_A)
_DpTimeSummerTimeEnd_Type=DlinkTimeSummerTimeValue
_DpTimeSummerTimeEnd_Object=MibScalar
dpTimeSummerTimeEnd=_DpTimeSummerTimeEnd_Object((1,3,6,1,4,1,171,15,23,1,2,4,4),_DpTimeSummerTimeEnd_Type())
dpTimeSummerTimeEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeSummerTimeEnd.setStatus(_A)
class _DpTimeSummerTimeOffset_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,30),ValueRangeConstraint(60,60),ValueRangeConstraint(90,90),ValueRangeConstraint(120,120))
_DpTimeSummerTimeOffset_Type.__name__=_D
_DpTimeSummerTimeOffset_Object=MibScalar
dpTimeSummerTimeOffset=_DpTimeSummerTimeOffset_Object((1,3,6,1,4,1,171,15,23,1,2,4,5),_DpTimeSummerTimeOffset_Type())
dpTimeSummerTimeOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeSummerTimeOffset.setStatus(_A)
if mibBuilder.loadTexts:dpTimeSummerTimeOffset.setUnits('Minutes')
_DpTimeServer_ObjectIdentity=ObjectIdentity
dpTimeServer=_DpTimeServer_ObjectIdentity((1,3,6,1,4,1,171,15,23,1,3))
_DpTimeSntpServerAddr_Type=IpAddress
_DpTimeSntpServerAddr_Object=MibScalar
dpTimeSntpServerAddr=_DpTimeSntpServerAddr_Object((1,3,6,1,4,1,171,15,23,1,3,1),_DpTimeSntpServerAddr_Type())
dpTimeSntpServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeSntpServerAddr.setStatus(_A)
_DpTimeSntpServerStratum_Type=Unsigned32
_DpTimeSntpServerStratum_Object=MibScalar
dpTimeSntpServerStratum=_DpTimeSntpServerStratum_Object((1,3,6,1,4,1,171,15,23,1,3,2),_DpTimeSntpServerStratum_Type())
dpTimeSntpServerStratum.setMaxAccess(_E)
if mibBuilder.loadTexts:dpTimeSntpServerStratum.setStatus(_A)
_DpTimeSntpServerVersion_Type=Unsigned32
_DpTimeSntpServerVersion_Object=MibScalar
dpTimeSntpServerVersion=_DpTimeSntpServerVersion_Object((1,3,6,1,4,1,171,15,23,1,3,3),_DpTimeSntpServerVersion_Type())
dpTimeSntpServerVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:dpTimeSntpServerVersion.setStatus(_A)
_DpTimeSntpServerLastReceive_Type=Unsigned32
_DpTimeSntpServerLastReceive_Object=MibScalar
dpTimeSntpServerLastReceive=_DpTimeSntpServerLastReceive_Object((1,3,6,1,4,1,171,15,23,1,3,4),_DpTimeSntpServerLastReceive_Type())
dpTimeSntpServerLastReceive.setMaxAccess(_E)
if mibBuilder.loadTexts:dpTimeSntpServerLastReceive.setStatus(_A)
if mibBuilder.loadTexts:dpTimeSntpServerLastReceive.setUnits('seconds')
_DpTimeMIBConformance_ObjectIdentity=ObjectIdentity
dpTimeMIBConformance=_DpTimeMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,23,2))
_DpTimeCompliances_ObjectIdentity=ObjectIdentity
dpTimeCompliances=_DpTimeCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,23,2,1))
_DpTimeGroups_ObjectIdentity=ObjectIdentity
dpTimeGroups=_DpTimeGroups_ObjectIdentity((1,3,6,1,4,1,171,15,23,2,2))
dpTimeSysInfoGroup=ObjectGroup((1,3,6,1,4,1,171,15,23,2,2,1))
dpTimeSysInfoGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:dpTimeSysInfoGroup.setStatus(_A)
dpTimeClockGroup=ObjectGroup((1,3,6,1,4,1,171,15,23,2,2,2))
dpTimeClockGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:dpTimeClockGroup.setStatus(_A)
dpTimeSntpGroup=ObjectGroup((1,3,6,1,4,1,171,15,23,2,2,3))
dpTimeSntpGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:dpTimeSntpGroup.setStatus(_A)
dpTimeSummerTimeCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,23,2,2,4))
dpTimeSummerTimeCfgGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:dpTimeSummerTimeCfgGroup.setStatus(_A)
dpTimeCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,23,2,1,1))
dpTimeCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:dpTimeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DlinkTimeSummerTimeValue':DlinkTimeSummerTimeValue,'dlinkPrimeTimeMIB':dlinkPrimeTimeMIB,'dpTimeMIBNotifications':dpTimeMIBNotifications,'dpTimeMIBObjects':dpTimeMIBObjects,'dpTimeGeneral':dpTimeGeneral,_J:dpTimeSntpEnabled,_K:dpTimeSntpPollInterval,'dpTimeClock':dpTimeClock,_I:dpTimeManagedClock,_G:dpTimeCurrentTimeSource,_H:dpTimeCurrentTime,'dpTimeSummerTime':dpTimeSummerTime,_P:dpTimeSummerTimeAutoSwitchMode,_Q:dpTimeSummerTimeTimeZone,_R:dpTimeSummerTimeStart,_S:dpTimeSummerTimeEnd,_T:dpTimeSummerTimeOffset,'dpTimeServer':dpTimeServer,_L:dpTimeSntpServerAddr,_M:dpTimeSntpServerStratum,_N:dpTimeSntpServerVersion,_O:dpTimeSntpServerLastReceive,'dpTimeMIBConformance':dpTimeMIBConformance,'dpTimeCompliances':dpTimeCompliances,'dpTimeCompliance':dpTimeCompliance,'dpTimeGroups':dpTimeGroups,_U:dpTimeSysInfoGroup,_V:dpTimeClockGroup,_W:dpTimeSntpGroup,_X:dpTimeSummerTimeCfgGroup})