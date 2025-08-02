_G='enable'
_F='disable'
_E='read-only'
_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkSysTimeMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,2))
if mibBuilder.loadTexts:tplinkSysTimeMIB.setRevisions(('2012-12-13 09:30',))
_TplinkSysTimeMIBObjects_ObjectIdentity=ObjectIdentity
tplinkSysTimeMIBObjects=_TplinkSysTimeMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,2,1))
class _TpSysTimeCurrentTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpSysTimeCurrentTime_Type.__name__=_C
_TpSysTimeCurrentTime_Object=MibScalar
tpSysTimeCurrentTime=_TpSysTimeCurrentTime_Object((1,3,6,1,4,1,11863,6,2,1,1),_TpSysTimeCurrentTime_Type())
tpSysTimeCurrentTime.setMaxAccess(_E)
if mibBuilder.loadTexts:tpSysTimeCurrentTime.setStatus(_A)
class _TpSysTimeSource_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpSysTimeSource_Type.__name__=_C
_TpSysTimeSource_Object=MibScalar
tpSysTimeSource=_TpSysTimeSource_Object((1,3,6,1,4,1,11863,6,2,1,2),_TpSysTimeSource_Type())
tpSysTimeSource.setMaxAccess(_E)
if mibBuilder.loadTexts:tpSysTimeSource.setStatus(_A)
class _TpSysTimeMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpSysTimeMode_Type.__name__=_C
_TpSysTimeMode_Object=MibScalar
tpSysTimeMode=_TpSysTimeMode_Object((1,3,6,1,4,1,11863,6,2,1,3),_TpSysTimeMode_Type())
tpSysTimeMode.setMaxAccess(_E)
if mibBuilder.loadTexts:tpSysTimeMode.setStatus(_A)
_TpSysTimeManualTimeConfig_ObjectIdentity=ObjectIdentity
tpSysTimeManualTimeConfig=_TpSysTimeManualTimeConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,2,1,4))
class _TpSysTimeManualTimeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpSysTimeManualTimeStatus_Type.__name__=_D
_TpSysTimeManualTimeStatus_Object=MibScalar
tpSysTimeManualTimeStatus=_TpSysTimeManualTimeStatus_Object((1,3,6,1,4,1,11863,6,2,1,4,1),_TpSysTimeManualTimeStatus_Type())
tpSysTimeManualTimeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeManualTimeStatus.setStatus(_A)
class _TpSysTimeTimeToSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(19,19));fixedLength=19
_TpSysTimeTimeToSet_Type.__name__=_C
_TpSysTimeTimeToSet_Object=MibScalar
tpSysTimeTimeToSet=_TpSysTimeTimeToSet_Object((1,3,6,1,4,1,11863,6,2,1,4,2),_TpSysTimeTimeToSet_Type())
tpSysTimeTimeToSet.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeTimeToSet.setStatus(_A)
_TpSysTimeNTPClientConfig_ObjectIdentity=ObjectIdentity
tpSysTimeNTPClientConfig=_TpSysTimeNTPClientConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,2,1,5))
class _TpSysTimeNTPClientStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpSysTimeNTPClientStatus_Type.__name__=_D
_TpSysTimeNTPClientStatus_Object=MibScalar
tpSysTimeNTPClientStatus=_TpSysTimeNTPClientStatus_Object((1,3,6,1,4,1,11863,6,2,1,5,1),_TpSysTimeNTPClientStatus_Type())
tpSysTimeNTPClientStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeNTPClientStatus.setStatus(_A)
class _TpSysTimeNTPTimezone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1200,-1100,-1000,-900,-800,-700,-600,-500,-450,-400,-350,-300,-200,-100,0,100,200,300,350,400,450,500,550,575,600,650,700,800,900,950,1000,1100,1200,1300)));namedValues=NamedValues(*(('utc-1200',-1200),('utc-1100',-1100),('utc-1000',-1000),('utc-0900',-900),('utc-0800',-800),('utc-0700',-700),('utc-0600',-600),('utc-0500',-500),('utc-0430',-450),('utc-0400',-400),('utc-0330',-350),('utc-0300',-300),('utc-0200',-200),('utc-0100',-100),('utc',0),('utc0100',100),('utc0200',200),('utc0300',300),('utc0330',350),('utc0400',400),('utc0430',450),('utc0500',500),('utc0530',550),('utc0545',575),('utc0600',600),('utc0630',650),('utc0700',700),('utc0800',800),('utc0900',900),('utc0930',950),('utc1000',1000),('utc1100',1100),('utc1200',1200),('utc1300',1300)))
_TpSysTimeNTPTimezone_Type.__name__=_D
_TpSysTimeNTPTimezone_Object=MibScalar
tpSysTimeNTPTimezone=_TpSysTimeNTPTimezone_Object((1,3,6,1,4,1,11863,6,2,1,5,2),_TpSysTimeNTPTimezone_Type())
tpSysTimeNTPTimezone.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeNTPTimezone.setStatus(_A)
class _TpSysTimeNTPServerAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(93,93));fixedLength=93
_TpSysTimeNTPServerAddr_Type.__name__=_C
_TpSysTimeNTPServerAddr_Object=MibScalar
tpSysTimeNTPServerAddr=_TpSysTimeNTPServerAddr_Object((1,3,6,1,4,1,11863,6,2,1,5,3),_TpSysTimeNTPServerAddr_Type())
tpSysTimeNTPServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeNTPServerAddr.setStatus(_A)
class _TpSysTimeNTPUpdateRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_TpSysTimeNTPUpdateRate_Type.__name__=_D
_TpSysTimeNTPUpdateRate_Object=MibScalar
tpSysTimeNTPUpdateRate=_TpSysTimeNTPUpdateRate_Object((1,3,6,1,4,1,11863,6,2,1,5,4),_TpSysTimeNTPUpdateRate_Type())
tpSysTimeNTPUpdateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeNTPUpdateRate.setStatus(_A)
_TpSysTimeDstConfig_ObjectIdentity=ObjectIdentity
tpSysTimeDstConfig=_TpSysTimeDstConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,2,1,6))
class _TpSysTimeDstStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disabled',0),('predefined',1),('recurring',2),('date',3)))
_TpSysTimeDstStatus_Type.__name__=_D
_TpSysTimeDstStatus_Object=MibScalar
tpSysTimeDstStatus=_TpSysTimeDstStatus_Object((1,3,6,1,4,1,11863,6,2,1,6,1),_TpSysTimeDstStatus_Type())
tpSysTimeDstStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeDstStatus.setStatus(_A)
class _TpSysTimeDstOffset_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_TpSysTimeDstOffset_Type.__name__=_D
_TpSysTimeDstOffset_Object=MibScalar
tpSysTimeDstOffset=_TpSysTimeDstOffset_Object((1,3,6,1,4,1,11863,6,2,1,6,2),_TpSysTimeDstOffset_Type())
tpSysTimeDstOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeDstOffset.setStatus(_A)
if mibBuilder.loadTexts:tpSysTimeDstOffset.setUnits('Minutes')
_TpSysTimeDstDateMode_ObjectIdentity=ObjectIdentity
tpSysTimeDstDateMode=_TpSysTimeDstDateMode_ObjectIdentity((1,3,6,1,4,1,11863,6,2,1,6,3))
class _TpSysTimeDstDateTimeStartEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(33,33));fixedLength=33
_TpSysTimeDstDateTimeStartEnd_Type.__name__=_C
_TpSysTimeDstDateTimeStartEnd_Object=MibScalar
tpSysTimeDstDateTimeStartEnd=_TpSysTimeDstDateTimeStartEnd_Object((1,3,6,1,4,1,11863,6,2,1,6,3,1),_TpSysTimeDstDateTimeStartEnd_Type())
tpSysTimeDstDateTimeStartEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeDstDateTimeStartEnd.setStatus(_A)
_TpSysTimeDstPredefinedMode_ObjectIdentity=ObjectIdentity
tpSysTimeDstPredefinedMode=_TpSysTimeDstPredefinedMode_ObjectIdentity((1,3,6,1,4,1,11863,6,2,1,6,4))
class _TpSysTimeDstRegionSelected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('usa',1),('australia',2),('europe',3),('new-Zealand',4)))
_TpSysTimeDstRegionSelected_Type.__name__=_D
_TpSysTimeDstRegionSelected_Object=MibScalar
tpSysTimeDstRegionSelected=_TpSysTimeDstRegionSelected_Object((1,3,6,1,4,1,11863,6,2,1,6,4,1),_TpSysTimeDstRegionSelected_Type())
tpSysTimeDstRegionSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeDstRegionSelected.setStatus(_A)
_TpSysTimeDstRecurringMode_ObjectIdentity=ObjectIdentity
tpSysTimeDstRecurringMode=_TpSysTimeDstRecurringMode_ObjectIdentity((1,3,6,1,4,1,11863,6,2,1,6,5))
class _TpSysTimeDstRecurringToStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_TpSysTimeDstRecurringToStart_Type.__name__=_C
_TpSysTimeDstRecurringToStart_Object=MibScalar
tpSysTimeDstRecurringToStart=_TpSysTimeDstRecurringToStart_Object((1,3,6,1,4,1,11863,6,2,1,6,5,1),_TpSysTimeDstRecurringToStart_Type())
tpSysTimeDstRecurringToStart.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeDstRecurringToStart.setStatus(_A)
class _TpSysTimeDstRecurringToEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_TpSysTimeDstRecurringToEnd_Type.__name__=_C
_TpSysTimeDstRecurringToEnd_Object=MibScalar
tpSysTimeDstRecurringToEnd=_TpSysTimeDstRecurringToEnd_Object((1,3,6,1,4,1,11863,6,2,1,6,5,2),_TpSysTimeDstRecurringToEnd_Type())
tpSysTimeDstRecurringToEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSysTimeDstRecurringToEnd.setStatus(_A)
_TplinkSysTimeNotifications_ObjectIdentity=ObjectIdentity
tplinkSysTimeNotifications=_TplinkSysTimeNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,2,2))
mibBuilder.exportSymbols('TPLINK-SYSTIME-MIB',**{'tplinkSysTimeMIB':tplinkSysTimeMIB,'tplinkSysTimeMIBObjects':tplinkSysTimeMIBObjects,'tpSysTimeCurrentTime':tpSysTimeCurrentTime,'tpSysTimeSource':tpSysTimeSource,'tpSysTimeMode':tpSysTimeMode,'tpSysTimeManualTimeConfig':tpSysTimeManualTimeConfig,'tpSysTimeManualTimeStatus':tpSysTimeManualTimeStatus,'tpSysTimeTimeToSet':tpSysTimeTimeToSet,'tpSysTimeNTPClientConfig':tpSysTimeNTPClientConfig,'tpSysTimeNTPClientStatus':tpSysTimeNTPClientStatus,'tpSysTimeNTPTimezone':tpSysTimeNTPTimezone,'tpSysTimeNTPServerAddr':tpSysTimeNTPServerAddr,'tpSysTimeNTPUpdateRate':tpSysTimeNTPUpdateRate,'tpSysTimeDstConfig':tpSysTimeDstConfig,'tpSysTimeDstStatus':tpSysTimeDstStatus,'tpSysTimeDstOffset':tpSysTimeDstOffset,'tpSysTimeDstDateMode':tpSysTimeDstDateMode,'tpSysTimeDstDateTimeStartEnd':tpSysTimeDstDateTimeStartEnd,'tpSysTimeDstPredefinedMode':tpSysTimeDstPredefinedMode,'tpSysTimeDstRegionSelected':tpSysTimeDstRegionSelected,'tpSysTimeDstRecurringMode':tpSysTimeDstRecurringMode,'tpSysTimeDstRecurringToStart':tpSysTimeDstRecurringToStart,'tpSysTimeDstRecurringToEnd':tpSysTimeDstRecurringToEnd,'tplinkSysTimeNotifications':tplinkSysTimeNotifications})