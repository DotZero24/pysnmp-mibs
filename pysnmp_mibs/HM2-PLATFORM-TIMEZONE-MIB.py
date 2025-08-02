_H='fourth'
_G='second'
_F='read-only'
_E='DisplayString'
_D='none'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2PlatformMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2PlatformMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
hm2PlatformTimeZone=ModuleIdentity((1,3,6,1,4,1,248,12,42))
if mibBuilder.loadTexts:hm2PlatformTimeZone.setRevisions(('2011-10-12 00:00',))
_Hm2AgentSystemTimeGroup_ObjectIdentity=ObjectIdentity
hm2AgentSystemTimeGroup=_Hm2AgentSystemTimeGroup_ObjectIdentity((1,3,6,1,4,1,248,12,42,1))
_Hm2AgentSystemTime_Type=DisplayString
_Hm2AgentSystemTime_Object=MibScalar
hm2AgentSystemTime=_Hm2AgentSystemTime_Object((1,3,6,1,4,1,248,12,42,1,1),_Hm2AgentSystemTime_Type())
hm2AgentSystemTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentSystemTime.setStatus(_A)
_Hm2AgentSystemDate_Type=DisplayString
_Hm2AgentSystemDate_Object=MibScalar
hm2AgentSystemDate=_Hm2AgentSystemDate_Object((1,3,6,1,4,1,248,12,42,1,2),_Hm2AgentSystemDate_Type())
hm2AgentSystemDate.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentSystemDate.setStatus(_A)
_Hm2AgentSystemTimeZoneAcronym_Type=DisplayString
_Hm2AgentSystemTimeZoneAcronym_Object=MibScalar
hm2AgentSystemTimeZoneAcronym=_Hm2AgentSystemTimeZoneAcronym_Object((1,3,6,1,4,1,248,12,42,1,3),_Hm2AgentSystemTimeZoneAcronym_Type())
hm2AgentSystemTimeZoneAcronym.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentSystemTimeZoneAcronym.setStatus(_A)
class _Hm2AgentSystemSummerTimeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_Hm2AgentSystemSummerTimeState_Type.__name__=_C
_Hm2AgentSystemSummerTimeState_Object=MibScalar
hm2AgentSystemSummerTimeState=_Hm2AgentSystemSummerTimeState_Object((1,3,6,1,4,1,248,12,42,1,5),_Hm2AgentSystemSummerTimeState_Type())
hm2AgentSystemSummerTimeState.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentSystemSummerTimeState.setStatus(_A)
_Hm2AgentTimeZoneGroup_ObjectIdentity=ObjectIdentity
hm2AgentTimeZoneGroup=_Hm2AgentTimeZoneGroup_ObjectIdentity((1,3,6,1,4,1,248,12,42,2))
class _Hm2AgentTimeZoneHoursOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,14))
_Hm2AgentTimeZoneHoursOffset_Type.__name__=_C
_Hm2AgentTimeZoneHoursOffset_Object=MibScalar
hm2AgentTimeZoneHoursOffset=_Hm2AgentTimeZoneHoursOffset_Object((1,3,6,1,4,1,248,12,42,2,1),_Hm2AgentTimeZoneHoursOffset_Type())
hm2AgentTimeZoneHoursOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeZoneHoursOffset.setStatus(_A)
class _Hm2AgentTimeZoneMinutesOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Hm2AgentTimeZoneMinutesOffset_Type.__name__=_C
_Hm2AgentTimeZoneMinutesOffset_Object=MibScalar
hm2AgentTimeZoneMinutesOffset=_Hm2AgentTimeZoneMinutesOffset_Object((1,3,6,1,4,1,248,12,42,2,2),_Hm2AgentTimeZoneMinutesOffset_Type())
hm2AgentTimeZoneMinutesOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeZoneMinutesOffset.setStatus(_A)
class _Hm2AgentTimeZoneAcronym_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_Hm2AgentTimeZoneAcronym_Type.__name__=_E
_Hm2AgentTimeZoneAcronym_Object=MibScalar
hm2AgentTimeZoneAcronym=_Hm2AgentTimeZoneAcronym_Object((1,3,6,1,4,1,248,12,42,2,3),_Hm2AgentTimeZoneAcronym_Type())
hm2AgentTimeZoneAcronym.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeZoneAcronym.setStatus(_A)
_Hm2AgentSummerTimeGroup_ObjectIdentity=ObjectIdentity
hm2AgentSummerTimeGroup=_Hm2AgentSummerTimeGroup_ObjectIdentity((1,3,6,1,4,1,248,12,42,3))
class _Hm2AgentSummerTimeMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noSummertime',0),('recurring',1),('recurringEu',2),('recurringUsa',3)))
_Hm2AgentSummerTimeMode_Type.__name__=_C
_Hm2AgentSummerTimeMode_Object=MibScalar
hm2AgentSummerTimeMode=_Hm2AgentSummerTimeMode_Object((1,3,6,1,4,1,248,12,42,3,1),_Hm2AgentSummerTimeMode_Type())
hm2AgentSummerTimeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSummerTimeMode.setStatus(_A)
_Hm2AgentSummerTimeRecurringGroup_ObjectIdentity=ObjectIdentity
hm2AgentSummerTimeRecurringGroup=_Hm2AgentSummerTimeRecurringGroup_ObjectIdentity((1,3,6,1,4,1,248,12,42,3,2))
class _Hm2AgentStRecurringStartingWeek_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),('first',1),(_G,2),('third',3),(_H,4),('last',5)))
_Hm2AgentStRecurringStartingWeek_Type.__name__=_C
_Hm2AgentStRecurringStartingWeek_Object=MibScalar
hm2AgentStRecurringStartingWeek=_Hm2AgentStRecurringStartingWeek_Object((1,3,6,1,4,1,248,12,42,3,2,1),_Hm2AgentStRecurringStartingWeek_Type())
hm2AgentStRecurringStartingWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringStartingWeek.setStatus(_A)
class _Hm2AgentStRecurringStartingDay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,0),('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
_Hm2AgentStRecurringStartingDay_Type.__name__=_C
_Hm2AgentStRecurringStartingDay_Object=MibScalar
hm2AgentStRecurringStartingDay=_Hm2AgentStRecurringStartingDay_Object((1,3,6,1,4,1,248,12,42,3,2,2),_Hm2AgentStRecurringStartingDay_Type())
hm2AgentStRecurringStartingDay.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringStartingDay.setStatus(_A)
class _Hm2AgentStRecurringStartingMonth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_D,0),('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)))
_Hm2AgentStRecurringStartingMonth_Type.__name__=_C
_Hm2AgentStRecurringStartingMonth_Object=MibScalar
hm2AgentStRecurringStartingMonth=_Hm2AgentStRecurringStartingMonth_Object((1,3,6,1,4,1,248,12,42,3,2,3),_Hm2AgentStRecurringStartingMonth_Type())
hm2AgentStRecurringStartingMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringStartingMonth.setStatus(_A)
class _Hm2AgentStRecurringStartingTime_Type(DisplayString):defaultValue=OctetString('00:00');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_Hm2AgentStRecurringStartingTime_Type.__name__=_E
_Hm2AgentStRecurringStartingTime_Object=MibScalar
hm2AgentStRecurringStartingTime=_Hm2AgentStRecurringStartingTime_Object((1,3,6,1,4,1,248,12,42,3,2,4),_Hm2AgentStRecurringStartingTime_Type())
hm2AgentStRecurringStartingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringStartingTime.setStatus(_A)
class _Hm2AgentStRecurringEndingWeek_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),('first',1),(_G,2),('third',3),(_H,4),('last',5)))
_Hm2AgentStRecurringEndingWeek_Type.__name__=_C
_Hm2AgentStRecurringEndingWeek_Object=MibScalar
hm2AgentStRecurringEndingWeek=_Hm2AgentStRecurringEndingWeek_Object((1,3,6,1,4,1,248,12,42,3,2,5),_Hm2AgentStRecurringEndingWeek_Type())
hm2AgentStRecurringEndingWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringEndingWeek.setStatus(_A)
class _Hm2AgentStRecurringEndingDay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,0),('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
_Hm2AgentStRecurringEndingDay_Type.__name__=_C
_Hm2AgentStRecurringEndingDay_Object=MibScalar
hm2AgentStRecurringEndingDay=_Hm2AgentStRecurringEndingDay_Object((1,3,6,1,4,1,248,12,42,3,2,6),_Hm2AgentStRecurringEndingDay_Type())
hm2AgentStRecurringEndingDay.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringEndingDay.setStatus(_A)
class _Hm2AgentStRecurringEndingMonth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_D,0),('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)))
_Hm2AgentStRecurringEndingMonth_Type.__name__=_C
_Hm2AgentStRecurringEndingMonth_Object=MibScalar
hm2AgentStRecurringEndingMonth=_Hm2AgentStRecurringEndingMonth_Object((1,3,6,1,4,1,248,12,42,3,2,7),_Hm2AgentStRecurringEndingMonth_Type())
hm2AgentStRecurringEndingMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringEndingMonth.setStatus(_A)
class _Hm2AgentStRecurringEndingTime_Type(DisplayString):defaultValue=OctetString('00:00');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_Hm2AgentStRecurringEndingTime_Type.__name__=_E
_Hm2AgentStRecurringEndingTime_Object=MibScalar
hm2AgentStRecurringEndingTime=_Hm2AgentStRecurringEndingTime_Object((1,3,6,1,4,1,248,12,42,3,2,8),_Hm2AgentStRecurringEndingTime_Type())
hm2AgentStRecurringEndingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringEndingTime.setStatus(_A)
class _Hm2AgentStRecurringZoneAcronym_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_Hm2AgentStRecurringZoneAcronym_Type.__name__=_E
_Hm2AgentStRecurringZoneAcronym_Object=MibScalar
hm2AgentStRecurringZoneAcronym=_Hm2AgentStRecurringZoneAcronym_Object((1,3,6,1,4,1,248,12,42,3,2,9),_Hm2AgentStRecurringZoneAcronym_Type())
hm2AgentStRecurringZoneAcronym.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringZoneAcronym.setStatus(_A)
class _Hm2AgentStRecurringZoneOffset_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Hm2AgentStRecurringZoneOffset_Type.__name__=_C
_Hm2AgentStRecurringZoneOffset_Object=MibScalar
hm2AgentStRecurringZoneOffset=_Hm2AgentStRecurringZoneOffset_Object((1,3,6,1,4,1,248,12,42,3,2,10),_Hm2AgentStRecurringZoneOffset_Type())
hm2AgentStRecurringZoneOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStRecurringZoneOffset.setStatus(_A)
mibBuilder.exportSymbols('HM2-PLATFORM-TIMEZONE-MIB',**{'hm2PlatformTimeZone':hm2PlatformTimeZone,'hm2AgentSystemTimeGroup':hm2AgentSystemTimeGroup,'hm2AgentSystemTime':hm2AgentSystemTime,'hm2AgentSystemDate':hm2AgentSystemDate,'hm2AgentSystemTimeZoneAcronym':hm2AgentSystemTimeZoneAcronym,'hm2AgentSystemSummerTimeState':hm2AgentSystemSummerTimeState,'hm2AgentTimeZoneGroup':hm2AgentTimeZoneGroup,'hm2AgentTimeZoneHoursOffset':hm2AgentTimeZoneHoursOffset,'hm2AgentTimeZoneMinutesOffset':hm2AgentTimeZoneMinutesOffset,'hm2AgentTimeZoneAcronym':hm2AgentTimeZoneAcronym,'hm2AgentSummerTimeGroup':hm2AgentSummerTimeGroup,'hm2AgentSummerTimeMode':hm2AgentSummerTimeMode,'hm2AgentSummerTimeRecurringGroup':hm2AgentSummerTimeRecurringGroup,'hm2AgentStRecurringStartingWeek':hm2AgentStRecurringStartingWeek,'hm2AgentStRecurringStartingDay':hm2AgentStRecurringStartingDay,'hm2AgentStRecurringStartingMonth':hm2AgentStRecurringStartingMonth,'hm2AgentStRecurringStartingTime':hm2AgentStRecurringStartingTime,'hm2AgentStRecurringEndingWeek':hm2AgentStRecurringEndingWeek,'hm2AgentStRecurringEndingDay':hm2AgentStRecurringEndingDay,'hm2AgentStRecurringEndingMonth':hm2AgentStRecurringEndingMonth,'hm2AgentStRecurringEndingTime':hm2AgentStRecurringEndingTime,'hm2AgentStRecurringZoneAcronym':hm2AgentStRecurringZoneAcronym,'hm2AgentStRecurringZoneOffset':hm2AgentStRecurringZoneOffset})