_M='timeRangeRuleIndex'
_L='timeRangeRuleName'
_K='read-only'
_J='inactive'
_I='active'
_H='timeRangeName'
_G='disabled'
_F='DisplayString'
_E='MPTIMERANGE-MIB'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mpTimeRangeMib=ModuleIdentity((1,3,6,1,4,1,5651,3,400))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_G,2)))
_TimeRangeEnable_Type=EnabledStatus
_TimeRangeEnable_Object=MibScalar
timeRangeEnable=_TimeRangeEnable_Object((1,3,6,1,4,1,5651,3,400,1),_TimeRangeEnable_Type())
timeRangeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeEnable.setStatus(_A)
class _TimeRangeFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_TimeRangeFrequency_Type.__name__=_B
_TimeRangeFrequency_Object=MibScalar
timeRangeFrequency=_TimeRangeFrequency_Object((1,3,6,1,4,1,5651,3,400,2),_TimeRangeFrequency_Type())
timeRangeFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeFrequency.setStatus(_A)
class _TimeRangeMaxOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_TimeRangeMaxOffset_Type.__name__=_B
_TimeRangeMaxOffset_Object=MibScalar
timeRangeMaxOffset=_TimeRangeMaxOffset_Object((1,3,6,1,4,1,5651,3,400,3),_TimeRangeMaxOffset_Type())
timeRangeMaxOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeMaxOffset.setStatus(_A)
_TimeRangeTable_Object=MibTable
timeRangeTable=_TimeRangeTable_Object((1,3,6,1,4,1,5651,3,400,6))
if mibBuilder.loadTexts:timeRangeTable.setStatus(_A)
_TimeRangeEntry_Object=MibTableRow
timeRangeEntry=_TimeRangeEntry_Object((1,3,6,1,4,1,5651,3,400,6,1))
timeRangeEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:timeRangeEntry.setStatus(_A)
class _TimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_TimeRangeName_Type.__name__=_F
_TimeRangeName_Object=MibTableColumn
timeRangeName=_TimeRangeName_Object((1,3,6,1,4,1,5651,3,400,6,1,1),_TimeRangeName_Type())
timeRangeName.setMaxAccess(_D)
if mibBuilder.loadTexts:timeRangeName.setStatus(_A)
class _TimeRangeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_G,3)))
_TimeRangeState_Type.__name__=_B
_TimeRangeState_Object=MibTableColumn
timeRangeState=_TimeRangeState_Object((1,3,6,1,4,1,5651,3,400,6,1,2),_TimeRangeState_Type())
timeRangeState.setMaxAccess(_K)
if mibBuilder.loadTexts:timeRangeState.setStatus(_A)
_TimeRangeRowStatus_Type=RowStatus
_TimeRangeRowStatus_Object=MibTableColumn
timeRangeRowStatus=_TimeRangeRowStatus_Object((1,3,6,1,4,1,5651,3,400,6,1,3),_TimeRangeRowStatus_Type())
timeRangeRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:timeRangeRowStatus.setStatus(_A)
_TimeRangeRuleTable_Object=MibTable
timeRangeRuleTable=_TimeRangeRuleTable_Object((1,3,6,1,4,1,5651,3,400,8))
if mibBuilder.loadTexts:timeRangeRuleTable.setStatus(_A)
_TimeRangeRuleEntry_Object=MibTableRow
timeRangeRuleEntry=_TimeRangeRuleEntry_Object((1,3,6,1,4,1,5651,3,400,8,1))
timeRangeRuleEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:timeRangeRuleEntry.setStatus(_A)
class _TimeRangeRuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_TimeRangeRuleName_Type.__name__=_F
_TimeRangeRuleName_Object=MibTableColumn
timeRangeRuleName=_TimeRangeRuleName_Object((1,3,6,1,4,1,5651,3,400,8,1,1),_TimeRangeRuleName_Type())
timeRangeRuleName.setMaxAccess(_D)
if mibBuilder.loadTexts:timeRangeRuleName.setStatus(_A)
class _TimeRangeRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TimeRangeRuleIndex_Type.__name__=_B
_TimeRangeRuleIndex_Object=MibTableColumn
timeRangeRuleIndex=_TimeRangeRuleIndex_Object((1,3,6,1,4,1,5651,3,400,8,1,2),_TimeRangeRuleIndex_Type())
timeRangeRuleIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:timeRangeRuleIndex.setStatus(_A)
class _TimeRangeRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('periodic',1),('absolute',2)))
_TimeRangeRuleType_Type.__name__=_B
_TimeRangeRuleType_Object=MibTableColumn
timeRangeRuleType=_TimeRangeRuleType_Object((1,3,6,1,4,1,5651,3,400,8,1,3),_TimeRangeRuleType_Type())
timeRangeRuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleType.setStatus(_A)
class _TimeRangeRuleStartWeekDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TimeRangeRuleStartWeekDay_Type.__name__=_B
_TimeRangeRuleStartWeekDay_Object=MibTableColumn
timeRangeRuleStartWeekDay=_TimeRangeRuleStartWeekDay_Object((1,3,6,1,4,1,5651,3,400,8,1,4),_TimeRangeRuleStartWeekDay_Type())
timeRangeRuleStartWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleStartWeekDay.setStatus(_A)
class _TimeRangeRuleEndWeekDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TimeRangeRuleEndWeekDay_Type.__name__=_B
_TimeRangeRuleEndWeekDay_Object=MibTableColumn
timeRangeRuleEndWeekDay=_TimeRangeRuleEndWeekDay_Object((1,3,6,1,4,1,5651,3,400,8,1,5),_TimeRangeRuleEndWeekDay_Type())
timeRangeRuleEndWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleEndWeekDay.setStatus(_A)
class _TimeRangeRuleStartTimeHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_TimeRangeRuleStartTimeHour_Type.__name__=_B
_TimeRangeRuleStartTimeHour_Object=MibTableColumn
timeRangeRuleStartTimeHour=_TimeRangeRuleStartTimeHour_Object((1,3,6,1,4,1,5651,3,400,8,1,6),_TimeRangeRuleStartTimeHour_Type())
timeRangeRuleStartTimeHour.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleStartTimeHour.setStatus(_A)
class _TimeRangeRuleStartTimeMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_TimeRangeRuleStartTimeMinute_Type.__name__=_B
_TimeRangeRuleStartTimeMinute_Object=MibTableColumn
timeRangeRuleStartTimeMinute=_TimeRangeRuleStartTimeMinute_Object((1,3,6,1,4,1,5651,3,400,8,1,7),_TimeRangeRuleStartTimeMinute_Type())
timeRangeRuleStartTimeMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleStartTimeMinute.setStatus(_A)
class _TimeRangeRuleEndTimeHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_TimeRangeRuleEndTimeHour_Type.__name__=_B
_TimeRangeRuleEndTimeHour_Object=MibTableColumn
timeRangeRuleEndTimeHour=_TimeRangeRuleEndTimeHour_Object((1,3,6,1,4,1,5651,3,400,8,1,8),_TimeRangeRuleEndTimeHour_Type())
timeRangeRuleEndTimeHour.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleEndTimeHour.setStatus(_A)
class _TimeRangeRuleEndTimeMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_TimeRangeRuleEndTimeMinute_Type.__name__=_B
_TimeRangeRuleEndTimeMinute_Object=MibTableColumn
timeRangeRuleEndTimeMinute=_TimeRangeRuleEndTimeMinute_Object((1,3,6,1,4,1,5651,3,400,8,1,9),_TimeRangeRuleEndTimeMinute_Type())
timeRangeRuleEndTimeMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleEndTimeMinute.setStatus(_A)
class _TimeRangeRuleStartDateDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_TimeRangeRuleStartDateDay_Type.__name__=_B
_TimeRangeRuleStartDateDay_Object=MibTableColumn
timeRangeRuleStartDateDay=_TimeRangeRuleStartDateDay_Object((1,3,6,1,4,1,5651,3,400,8,1,10),_TimeRangeRuleStartDateDay_Type())
timeRangeRuleStartDateDay.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleStartDateDay.setStatus(_A)
class _TimeRangeRuleStartDateMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_TimeRangeRuleStartDateMonth_Type.__name__=_B
_TimeRangeRuleStartDateMonth_Object=MibTableColumn
timeRangeRuleStartDateMonth=_TimeRangeRuleStartDateMonth_Object((1,3,6,1,4,1,5651,3,400,8,1,11),_TimeRangeRuleStartDateMonth_Type())
timeRangeRuleStartDateMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleStartDateMonth.setStatus(_A)
class _TimeRangeRuleStartDateYear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2100))
_TimeRangeRuleStartDateYear_Type.__name__=_B
_TimeRangeRuleStartDateYear_Object=MibTableColumn
timeRangeRuleStartDateYear=_TimeRangeRuleStartDateYear_Object((1,3,6,1,4,1,5651,3,400,8,1,12),_TimeRangeRuleStartDateYear_Type())
timeRangeRuleStartDateYear.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleStartDateYear.setStatus(_A)
class _TimeRangeRuleEndDateDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_TimeRangeRuleEndDateDay_Type.__name__=_B
_TimeRangeRuleEndDateDay_Object=MibTableColumn
timeRangeRuleEndDateDay=_TimeRangeRuleEndDateDay_Object((1,3,6,1,4,1,5651,3,400,8,1,13),_TimeRangeRuleEndDateDay_Type())
timeRangeRuleEndDateDay.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleEndDateDay.setStatus(_A)
class _TimeRangeRuleEndDateMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_TimeRangeRuleEndDateMonth_Type.__name__=_B
_TimeRangeRuleEndDateMonth_Object=MibTableColumn
timeRangeRuleEndDateMonth=_TimeRangeRuleEndDateMonth_Object((1,3,6,1,4,1,5651,3,400,8,1,14),_TimeRangeRuleEndDateMonth_Type())
timeRangeRuleEndDateMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleEndDateMonth.setStatus(_A)
class _TimeRangeRuleEndDateYear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2100))
_TimeRangeRuleEndDateYear_Type.__name__=_B
_TimeRangeRuleEndDateYear_Object=MibTableColumn
timeRangeRuleEndDateYear=_TimeRangeRuleEndDateYear_Object((1,3,6,1,4,1,5651,3,400,8,1,15),_TimeRangeRuleEndDateYear_Type())
timeRangeRuleEndDateYear.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRangeRuleEndDateYear.setStatus(_A)
class _TimeRangeRuleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_G,3)))
_TimeRangeRuleState_Type.__name__=_B
_TimeRangeRuleState_Object=MibTableColumn
timeRangeRuleState=_TimeRangeRuleState_Object((1,3,6,1,4,1,5651,3,400,8,1,16),_TimeRangeRuleState_Type())
timeRangeRuleState.setMaxAccess(_K)
if mibBuilder.loadTexts:timeRangeRuleState.setStatus(_A)
_TimeRangeRuleRowStatus_Type=RowStatus
_TimeRangeRuleRowStatus_Object=MibTableColumn
timeRangeRuleRowStatus=_TimeRangeRuleRowStatus_Object((1,3,6,1,4,1,5651,3,400,8,1,17),_TimeRangeRuleRowStatus_Type())
timeRangeRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:timeRangeRuleRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'EnabledStatus':EnabledStatus,'mpTimeRangeMib':mpTimeRangeMib,'timeRangeEnable':timeRangeEnable,'timeRangeFrequency':timeRangeFrequency,'timeRangeMaxOffset':timeRangeMaxOffset,'timeRangeTable':timeRangeTable,'timeRangeEntry':timeRangeEntry,_H:timeRangeName,'timeRangeState':timeRangeState,'timeRangeRowStatus':timeRangeRowStatus,'timeRangeRuleTable':timeRangeRuleTable,'timeRangeRuleEntry':timeRangeRuleEntry,_L:timeRangeRuleName,_M:timeRangeRuleIndex,'timeRangeRuleType':timeRangeRuleType,'timeRangeRuleStartWeekDay':timeRangeRuleStartWeekDay,'timeRangeRuleEndWeekDay':timeRangeRuleEndWeekDay,'timeRangeRuleStartTimeHour':timeRangeRuleStartTimeHour,'timeRangeRuleStartTimeMinute':timeRangeRuleStartTimeMinute,'timeRangeRuleEndTimeHour':timeRangeRuleEndTimeHour,'timeRangeRuleEndTimeMinute':timeRangeRuleEndTimeMinute,'timeRangeRuleStartDateDay':timeRangeRuleStartDateDay,'timeRangeRuleStartDateMonth':timeRangeRuleStartDateMonth,'timeRangeRuleStartDateYear':timeRangeRuleStartDateYear,'timeRangeRuleEndDateDay':timeRangeRuleEndDateDay,'timeRangeRuleEndDateMonth':timeRangeRuleEndDateMonth,'timeRangeRuleEndDateYear':timeRangeRuleEndDateYear,'timeRangeRuleState':timeRangeRuleState,'timeRangeRuleRowStatus':timeRangeRuleRowStatus})