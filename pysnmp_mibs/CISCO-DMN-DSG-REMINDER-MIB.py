_F='reminderTimerID'
_E='CISCO-DMN-DSG-REMINDER-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
ciscoDSGReminder=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,30))
if mibBuilder.loadTexts:ciscoDSGReminder.setRevisions(('2010-08-30 11:00','2010-06-17 06:00','2010-04-12 06:00'))
_ReminderTable_ObjectIdentity=ObjectIdentity
reminderTable=_ReminderTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,30,2))
_ReminderTimerTable_Object=MibTable
reminderTimerTable=_ReminderTimerTable_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1))
if mibBuilder.loadTexts:reminderTimerTable.setStatus(_A)
_ReminderTimerEntry_Object=MibTableRow
reminderTimerEntry=_ReminderTimerEntry_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1))
reminderTimerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:reminderTimerEntry.setStatus(_A)
class _ReminderTimerID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_ReminderTimerID_Type.__name__=_C
_ReminderTimerID_Object=MibTableColumn
reminderTimerID=_ReminderTimerID_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,1),_ReminderTimerID_Type())
reminderTimerID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:reminderTimerID.setStatus(_A)
class _ReminderTimerChType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tv',1),('radio',2),('other',3)))
_ReminderTimerChType_Type.__name__=_C
_ReminderTimerChType_Object=MibTableColumn
reminderTimerChType=_ReminderTimerChType_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,2),_ReminderTimerChType_Type())
reminderTimerChType.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerChType.setStatus(_A)
class _ReminderTimerChNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ReminderTimerChNum_Type.__name__=_C
_ReminderTimerChNum_Object=MibTableColumn
reminderTimerChNum=_ReminderTimerChNum_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,3),_ReminderTimerChNum_Type())
reminderTimerChNum.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerChNum.setStatus(_A)
class _ReminderTimerChName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ReminderTimerChName_Type.__name__=_D
_ReminderTimerChName_Object=MibTableColumn
reminderTimerChName=_ReminderTimerChName_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,4),_ReminderTimerChName_Type())
reminderTimerChName.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerChName.setStatus(_A)
class _ReminderTimerEvtName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ReminderTimerEvtName_Type.__name__=_D
_ReminderTimerEvtName_Object=MibTableColumn
reminderTimerEvtName=_ReminderTimerEvtName_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,5),_ReminderTimerEvtName_Type())
reminderTimerEvtName.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerEvtName.setStatus(_A)
class _ReminderTimerDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6),('sunday',7)))
_ReminderTimerDay_Type.__name__=_C
_ReminderTimerDay_Object=MibTableColumn
reminderTimerDay=_ReminderTimerDay_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,6),_ReminderTimerDay_Type())
reminderTimerDay.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerDay.setStatus(_A)
class _ReminderTimerStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ReminderTimerStartTime_Type.__name__=_D
_ReminderTimerStartTime_Object=MibTableColumn
reminderTimerStartTime=_ReminderTimerStartTime_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,7),_ReminderTimerStartTime_Type())
reminderTimerStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerStartTime.setStatus(_A)
class _ReminderTimerEndTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ReminderTimerEndTime_Type.__name__=_D
_ReminderTimerEndTime_Object=MibTableColumn
reminderTimerEndTime=_ReminderTimerEndTime_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,8),_ReminderTimerEndTime_Type())
reminderTimerEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerEndTime.setStatus(_A)
class _ReminderTimerEvtParentalRating_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ReminderTimerEvtParentalRating_Type.__name__=_C
_ReminderTimerEvtParentalRating_Object=MibTableColumn
reminderTimerEvtParentalRating=_ReminderTimerEvtParentalRating_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,9),_ReminderTimerEvtParentalRating_Type())
reminderTimerEvtParentalRating.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerEvtParentalRating.setStatus(_A)
class _ReminderTimerFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('once',1),('daily',2),('weekly',3),('weekDays',4)))
_ReminderTimerFrequency_Type.__name__=_C
_ReminderTimerFrequency_Object=MibTableColumn
reminderTimerFrequency=_ReminderTimerFrequency_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,10),_ReminderTimerFrequency_Type())
reminderTimerFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerFrequency.setStatus(_A)
_ReminderTimerRowStatus_Type=RowStatus
_ReminderTimerRowStatus_Object=MibTableColumn
reminderTimerRowStatus=_ReminderTimerRowStatus_Object((1,3,6,1,4,1,1429,2,2,5,30,2,1,1,11),_ReminderTimerRowStatus_Type())
reminderTimerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:reminderTimerRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGReminder':ciscoDSGReminder,'reminderTable':reminderTable,'reminderTimerTable':reminderTimerTable,'reminderTimerEntry':reminderTimerEntry,_F:reminderTimerID,'reminderTimerChType':reminderTimerChType,'reminderTimerChNum':reminderTimerChNum,'reminderTimerChName':reminderTimerChName,'reminderTimerEvtName':reminderTimerEvtName,'reminderTimerDay':reminderTimerDay,'reminderTimerStartTime':reminderTimerStartTime,'reminderTimerEndTime':reminderTimerEndTime,'reminderTimerEvtParentalRating':reminderTimerEvtParentalRating,'reminderTimerFrequency':reminderTimerFrequency,'reminderTimerRowStatus':reminderTimerRowStatus})