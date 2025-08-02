_T='fourth'
_S='second'
_R='read-only'
_Q='dec'
_P='nov'
_O='oct'
_N='sep'
_M='aug'
_L='jul'
_K='jun'
_J='may'
_I='apr'
_H='mar'
_G='feb'
_F='jan'
_E='DisplayString'
_D='none'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
fastPathTimeZonePrivate=ModuleIdentity((1,3,6,1,4,1,2356,16,1,42))
if mibBuilder.loadTexts:fastPathTimeZonePrivate.setRevisions(('2011-01-26 00:00','2007-02-28 05:00'))
_AgentSystemTimeGroup_ObjectIdentity=ObjectIdentity
agentSystemTimeGroup=_AgentSystemTimeGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,42,1))
_AgentSystemTime_Type=DisplayString
_AgentSystemTime_Object=MibScalar
agentSystemTime=_AgentSystemTime_Object((1,3,6,1,4,1,2356,16,1,42,1,1),_AgentSystemTime_Type())
agentSystemTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSystemTime.setStatus(_A)
_AgentSystemDate_Type=DisplayString
_AgentSystemDate_Object=MibScalar
agentSystemDate=_AgentSystemDate_Object((1,3,6,1,4,1,2356,16,1,42,1,2),_AgentSystemDate_Type())
agentSystemDate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSystemDate.setStatus(_A)
_AgentSystemTimeZoneAcronym_Type=DisplayString
_AgentSystemTimeZoneAcronym_Object=MibScalar
agentSystemTimeZoneAcronym=_AgentSystemTimeZoneAcronym_Object((1,3,6,1,4,1,2356,16,1,42,1,3),_AgentSystemTimeZoneAcronym_Type())
agentSystemTimeZoneAcronym.setMaxAccess(_R)
if mibBuilder.loadTexts:agentSystemTimeZoneAcronym.setStatus(_A)
class _AgentSystemTimeSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('sntp',1)))
_AgentSystemTimeSource_Type.__name__=_C
_AgentSystemTimeSource_Object=MibScalar
agentSystemTimeSource=_AgentSystemTimeSource_Object((1,3,6,1,4,1,2356,16,1,42,1,4),_AgentSystemTimeSource_Type())
agentSystemTimeSource.setMaxAccess(_R)
if mibBuilder.loadTexts:agentSystemTimeSource.setStatus(_A)
class _AgentSystemSummerTimeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_AgentSystemSummerTimeState_Type.__name__=_C
_AgentSystemSummerTimeState_Object=MibScalar
agentSystemSummerTimeState=_AgentSystemSummerTimeState_Object((1,3,6,1,4,1,2356,16,1,42,1,5),_AgentSystemSummerTimeState_Type())
agentSystemSummerTimeState.setMaxAccess(_R)
if mibBuilder.loadTexts:agentSystemSummerTimeState.setStatus(_A)
_AgentTimeZoneGroup_ObjectIdentity=ObjectIdentity
agentTimeZoneGroup=_AgentTimeZoneGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,42,2))
class _AgentTimeZoneHoursOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,13))
_AgentTimeZoneHoursOffset_Type.__name__=_C
_AgentTimeZoneHoursOffset_Object=MibScalar
agentTimeZoneHoursOffset=_AgentTimeZoneHoursOffset_Object((1,3,6,1,4,1,2356,16,1,42,2,1),_AgentTimeZoneHoursOffset_Type())
agentTimeZoneHoursOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTimeZoneHoursOffset.setStatus(_A)
class _AgentTimeZoneMinutesOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_AgentTimeZoneMinutesOffset_Type.__name__=_C
_AgentTimeZoneMinutesOffset_Object=MibScalar
agentTimeZoneMinutesOffset=_AgentTimeZoneMinutesOffset_Object((1,3,6,1,4,1,2356,16,1,42,2,2),_AgentTimeZoneMinutesOffset_Type())
agentTimeZoneMinutesOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTimeZoneMinutesOffset.setStatus(_A)
_AgentTimeZoneAcronym_Type=DisplayString
_AgentTimeZoneAcronym_Object=MibScalar
agentTimeZoneAcronym=_AgentTimeZoneAcronym_Object((1,3,6,1,4,1,2356,16,1,42,2,3),_AgentTimeZoneAcronym_Type())
agentTimeZoneAcronym.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTimeZoneAcronym.setStatus(_A)
_AgentSummerTimeGroup_ObjectIdentity=ObjectIdentity
agentSummerTimeGroup=_AgentSummerTimeGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,42,3))
class _AgentSummerTimeMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noSummertime',0),('recurring',1),('recurringEu',2),('recurringUsa',3),('nonrecurring',4)))
_AgentSummerTimeMode_Type.__name__=_C
_AgentSummerTimeMode_Object=MibScalar
agentSummerTimeMode=_AgentSummerTimeMode_Object((1,3,6,1,4,1,2356,16,1,42,3,1),_AgentSummerTimeMode_Type())
agentSummerTimeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSummerTimeMode.setStatus(_A)
_AgentSummerTimeRecurringGroup_ObjectIdentity=ObjectIdentity
agentSummerTimeRecurringGroup=_AgentSummerTimeRecurringGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,42,3,2))
class _AgentStRecurringStartingWeek_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),('first',1),(_S,2),('third',3),(_T,4),('last',5)))
_AgentStRecurringStartingWeek_Type.__name__=_C
_AgentStRecurringStartingWeek_Object=MibScalar
agentStRecurringStartingWeek=_AgentStRecurringStartingWeek_Object((1,3,6,1,4,1,2356,16,1,42,3,2,1),_AgentStRecurringStartingWeek_Type())
agentStRecurringStartingWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringStartingWeek.setStatus(_A)
class _AgentStRecurringStartingDay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,0),('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
_AgentStRecurringStartingDay_Type.__name__=_C
_AgentStRecurringStartingDay_Object=MibScalar
agentStRecurringStartingDay=_AgentStRecurringStartingDay_Object((1,3,6,1,4,1,2356,16,1,42,3,2,2),_AgentStRecurringStartingDay_Type())
agentStRecurringStartingDay.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringStartingDay.setStatus(_A)
class _AgentStRecurringStartingMonth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_D,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),(_O,10),(_P,11),(_Q,12)))
_AgentStRecurringStartingMonth_Type.__name__=_C
_AgentStRecurringStartingMonth_Object=MibScalar
agentStRecurringStartingMonth=_AgentStRecurringStartingMonth_Object((1,3,6,1,4,1,2356,16,1,42,3,2,3),_AgentStRecurringStartingMonth_Type())
agentStRecurringStartingMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringStartingMonth.setStatus(_A)
class _AgentStRecurringStartingTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_AgentStRecurringStartingTime_Type.__name__=_E
_AgentStRecurringStartingTime_Object=MibScalar
agentStRecurringStartingTime=_AgentStRecurringStartingTime_Object((1,3,6,1,4,1,2356,16,1,42,3,2,4),_AgentStRecurringStartingTime_Type())
agentStRecurringStartingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringStartingTime.setStatus(_A)
class _AgentStRecurringEndingWeek_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),('first',1),(_S,2),('third',3),(_T,4),('last',5)))
_AgentStRecurringEndingWeek_Type.__name__=_C
_AgentStRecurringEndingWeek_Object=MibScalar
agentStRecurringEndingWeek=_AgentStRecurringEndingWeek_Object((1,3,6,1,4,1,2356,16,1,42,3,2,5),_AgentStRecurringEndingWeek_Type())
agentStRecurringEndingWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringEndingWeek.setStatus(_A)
class _AgentStRecurringEndingDay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,0),('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
_AgentStRecurringEndingDay_Type.__name__=_C
_AgentStRecurringEndingDay_Object=MibScalar
agentStRecurringEndingDay=_AgentStRecurringEndingDay_Object((1,3,6,1,4,1,2356,16,1,42,3,2,6),_AgentStRecurringEndingDay_Type())
agentStRecurringEndingDay.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringEndingDay.setStatus(_A)
class _AgentStRecurringEndingMonth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_D,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),(_O,10),(_P,11),(_Q,12)))
_AgentStRecurringEndingMonth_Type.__name__=_C
_AgentStRecurringEndingMonth_Object=MibScalar
agentStRecurringEndingMonth=_AgentStRecurringEndingMonth_Object((1,3,6,1,4,1,2356,16,1,42,3,2,7),_AgentStRecurringEndingMonth_Type())
agentStRecurringEndingMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringEndingMonth.setStatus(_A)
class _AgentStRecurringEndingTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_AgentStRecurringEndingTime_Type.__name__=_E
_AgentStRecurringEndingTime_Object=MibScalar
agentStRecurringEndingTime=_AgentStRecurringEndingTime_Object((1,3,6,1,4,1,2356,16,1,42,3,2,8),_AgentStRecurringEndingTime_Type())
agentStRecurringEndingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringEndingTime.setStatus(_A)
class _AgentStRecurringZoneAcronym_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AgentStRecurringZoneAcronym_Type.__name__=_E
_AgentStRecurringZoneAcronym_Object=MibScalar
agentStRecurringZoneAcronym=_AgentStRecurringZoneAcronym_Object((1,3,6,1,4,1,2356,16,1,42,3,2,9),_AgentStRecurringZoneAcronym_Type())
agentStRecurringZoneAcronym.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringZoneAcronym.setStatus(_A)
class _AgentStRecurringZoneOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1440))
_AgentStRecurringZoneOffset_Type.__name__=_C
_AgentStRecurringZoneOffset_Object=MibScalar
agentStRecurringZoneOffset=_AgentStRecurringZoneOffset_Object((1,3,6,1,4,1,2356,16,1,42,3,2,10),_AgentStRecurringZoneOffset_Type())
agentStRecurringZoneOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStRecurringZoneOffset.setStatus(_A)
_AgentSummerTimeNonRecurringGroup_ObjectIdentity=ObjectIdentity
agentSummerTimeNonRecurringGroup=_AgentSummerTimeNonRecurringGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,42,3,3))
class _AgentStNonRecurringStartingDay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,31))
_AgentStNonRecurringStartingDay_Type.__name__=_C
_AgentStNonRecurringStartingDay_Object=MibScalar
agentStNonRecurringStartingDay=_AgentStNonRecurringStartingDay_Object((1,3,6,1,4,1,2356,16,1,42,3,3,1),_AgentStNonRecurringStartingDay_Type())
agentStNonRecurringStartingDay.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringStartingDay.setStatus(_A)
class _AgentStNonRecurringStartingMonth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_D,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),(_O,10),(_P,11),(_Q,12)))
_AgentStNonRecurringStartingMonth_Type.__name__=_C
_AgentStNonRecurringStartingMonth_Object=MibScalar
agentStNonRecurringStartingMonth=_AgentStNonRecurringStartingMonth_Object((1,3,6,1,4,1,2356,16,1,42,3,3,2),_AgentStNonRecurringStartingMonth_Type())
agentStNonRecurringStartingMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringStartingMonth.setStatus(_A)
class _AgentStNonRecurringStartingYear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,2097))
_AgentStNonRecurringStartingYear_Type.__name__=_C
_AgentStNonRecurringStartingYear_Object=MibScalar
agentStNonRecurringStartingYear=_AgentStNonRecurringStartingYear_Object((1,3,6,1,4,1,2356,16,1,42,3,3,3),_AgentStNonRecurringStartingYear_Type())
agentStNonRecurringStartingYear.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringStartingYear.setStatus(_A)
class _AgentStNonRecurringStartingTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_AgentStNonRecurringStartingTime_Type.__name__=_E
_AgentStNonRecurringStartingTime_Object=MibScalar
agentStNonRecurringStartingTime=_AgentStNonRecurringStartingTime_Object((1,3,6,1,4,1,2356,16,1,42,3,3,4),_AgentStNonRecurringStartingTime_Type())
agentStNonRecurringStartingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringStartingTime.setStatus(_A)
class _AgentStNonRecurringEndingDay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,31))
_AgentStNonRecurringEndingDay_Type.__name__=_C
_AgentStNonRecurringEndingDay_Object=MibScalar
agentStNonRecurringEndingDay=_AgentStNonRecurringEndingDay_Object((1,3,6,1,4,1,2356,16,1,42,3,3,5),_AgentStNonRecurringEndingDay_Type())
agentStNonRecurringEndingDay.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringEndingDay.setStatus(_A)
class _AgentStNonRecurringEndingMonth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_D,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),(_O,10),(_P,11),(_Q,12)))
_AgentStNonRecurringEndingMonth_Type.__name__=_C
_AgentStNonRecurringEndingMonth_Object=MibScalar
agentStNonRecurringEndingMonth=_AgentStNonRecurringEndingMonth_Object((1,3,6,1,4,1,2356,16,1,42,3,3,6),_AgentStNonRecurringEndingMonth_Type())
agentStNonRecurringEndingMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringEndingMonth.setStatus(_A)
class _AgentStNonRecurringEndingYear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,2097))
_AgentStNonRecurringEndingYear_Type.__name__=_C
_AgentStNonRecurringEndingYear_Object=MibScalar
agentStNonRecurringEndingYear=_AgentStNonRecurringEndingYear_Object((1,3,6,1,4,1,2356,16,1,42,3,3,7),_AgentStNonRecurringEndingYear_Type())
agentStNonRecurringEndingYear.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringEndingYear.setStatus(_A)
class _AgentStNonRecurringEndingTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_AgentStNonRecurringEndingTime_Type.__name__=_E
_AgentStNonRecurringEndingTime_Object=MibScalar
agentStNonRecurringEndingTime=_AgentStNonRecurringEndingTime_Object((1,3,6,1,4,1,2356,16,1,42,3,3,8),_AgentStNonRecurringEndingTime_Type())
agentStNonRecurringEndingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringEndingTime.setStatus(_A)
class _AgentStNonRecurringZoneOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1440))
_AgentStNonRecurringZoneOffset_Type.__name__=_C
_AgentStNonRecurringZoneOffset_Object=MibScalar
agentStNonRecurringZoneOffset=_AgentStNonRecurringZoneOffset_Object((1,3,6,1,4,1,2356,16,1,42,3,3,9),_AgentStNonRecurringZoneOffset_Type())
agentStNonRecurringZoneOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringZoneOffset.setStatus(_A)
class _AgentStNonRecurringZoneAcronym_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AgentStNonRecurringZoneAcronym_Type.__name__=_E
_AgentStNonRecurringZoneAcronym_Object=MibScalar
agentStNonRecurringZoneAcronym=_AgentStNonRecurringZoneAcronym_Object((1,3,6,1,4,1,2356,16,1,42,3,3,10),_AgentStNonRecurringZoneAcronym_Type())
agentStNonRecurringZoneAcronym.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStNonRecurringZoneAcronym.setStatus(_A)
mibBuilder.exportSymbols('LANCOM-TIMEZONE-PRIVATE-MIB',**{'fastPathTimeZonePrivate':fastPathTimeZonePrivate,'agentSystemTimeGroup':agentSystemTimeGroup,'agentSystemTime':agentSystemTime,'agentSystemDate':agentSystemDate,'agentSystemTimeZoneAcronym':agentSystemTimeZoneAcronym,'agentSystemTimeSource':agentSystemTimeSource,'agentSystemSummerTimeState':agentSystemSummerTimeState,'agentTimeZoneGroup':agentTimeZoneGroup,'agentTimeZoneHoursOffset':agentTimeZoneHoursOffset,'agentTimeZoneMinutesOffset':agentTimeZoneMinutesOffset,'agentTimeZoneAcronym':agentTimeZoneAcronym,'agentSummerTimeGroup':agentSummerTimeGroup,'agentSummerTimeMode':agentSummerTimeMode,'agentSummerTimeRecurringGroup':agentSummerTimeRecurringGroup,'agentStRecurringStartingWeek':agentStRecurringStartingWeek,'agentStRecurringStartingDay':agentStRecurringStartingDay,'agentStRecurringStartingMonth':agentStRecurringStartingMonth,'agentStRecurringStartingTime':agentStRecurringStartingTime,'agentStRecurringEndingWeek':agentStRecurringEndingWeek,'agentStRecurringEndingDay':agentStRecurringEndingDay,'agentStRecurringEndingMonth':agentStRecurringEndingMonth,'agentStRecurringEndingTime':agentStRecurringEndingTime,'agentStRecurringZoneAcronym':agentStRecurringZoneAcronym,'agentStRecurringZoneOffset':agentStRecurringZoneOffset,'agentSummerTimeNonRecurringGroup':agentSummerTimeNonRecurringGroup,'agentStNonRecurringStartingDay':agentStNonRecurringStartingDay,'agentStNonRecurringStartingMonth':agentStNonRecurringStartingMonth,'agentStNonRecurringStartingYear':agentStNonRecurringStartingYear,'agentStNonRecurringStartingTime':agentStNonRecurringStartingTime,'agentStNonRecurringEndingDay':agentStNonRecurringEndingDay,'agentStNonRecurringEndingMonth':agentStNonRecurringEndingMonth,'agentStNonRecurringEndingYear':agentStNonRecurringEndingYear,'agentStNonRecurringEndingTime':agentStNonRecurringEndingTime,'agentStNonRecurringZoneOffset':agentStNonRecurringZoneOffset,'agentStNonRecurringZoneAcronym':agentStNonRecurringZoneAcronym})