_R='saturday'
_Q='friday'
_P='thursday'
_O='wednesday'
_N='tuesday'
_M='monday'
_L='sunday'
_K='timeRangePeriodicEntryIndex'
_J='timeRangeAbsoluteEntryIndex'
_I='DisplayString'
_H='not-accessible'
_G='read-only'
_F='Bits'
_E='timeRangeIndex'
_D='NETGEAR-TIMERANGE-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
fastPathTimeRange=ModuleIdentity((1,3,6,1,4,1,4526,10,53))
if mibBuilder.loadTexts:fastPathTimeRange.setRevisions(('2011-01-26 00:00','2009-09-24 00:00'))
class TimeRangeAbsoluteDateAndTime(TextualConvention,OctetString):status=_A;displayHint='2d-1d-1d,1d:1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class TimeRangePeriodicTime(TextualConvention,OctetString):status=_A;displayHint='1d:1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class TimeRangePeriodicDate(TextualConvention,OctetString):status=_A;displayHint='2d-1d-1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_FastPathTimeRangeGroup_ObjectIdentity=ObjectIdentity
fastPathTimeRangeGroup=_FastPathTimeRangeGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,53,1))
class _TimeRangeAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_TimeRangeAdminMode_Type.__name__=_C
_TimeRangeAdminMode_Object=MibScalar
timeRangeAdminMode=_TimeRangeAdminMode_Object((1,3,6,1,4,1,4526,10,53,1,1),_TimeRangeAdminMode_Type())
timeRangeAdminMode.setMaxAccess(_G)
if mibBuilder.loadTexts:timeRangeAdminMode.setStatus(_A)
_TimeRangeIndexNextFree_Type=Integer32
_TimeRangeIndexNextFree_Object=MibScalar
timeRangeIndexNextFree=_TimeRangeIndexNextFree_Object((1,3,6,1,4,1,4526,10,53,1,2),_TimeRangeIndexNextFree_Type())
timeRangeIndexNextFree.setMaxAccess(_G)
if mibBuilder.loadTexts:timeRangeIndexNextFree.setStatus(_A)
_TimeRangeTable_Object=MibTable
timeRangeTable=_TimeRangeTable_Object((1,3,6,1,4,1,4526,10,53,1,3))
if mibBuilder.loadTexts:timeRangeTable.setStatus(_A)
_TimeRangeEntry_Object=MibTableRow
timeRangeEntry=_TimeRangeEntry_Object((1,3,6,1,4,1,4526,10,53,1,3,1))
timeRangeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:timeRangeEntry.setStatus(_A)
_TimeRangeIndex_Type=Unsigned32
_TimeRangeIndex_Object=MibTableColumn
timeRangeIndex=_TimeRangeIndex_Object((1,3,6,1,4,1,4526,10,53,1,3,1,1),_TimeRangeIndex_Type())
timeRangeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:timeRangeIndex.setStatus(_A)
class _TimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_TimeRangeName_Type.__name__=_I
_TimeRangeName_Object=MibTableColumn
timeRangeName=_TimeRangeName_Object((1,3,6,1,4,1,4526,10,53,1,3,1,2),_TimeRangeName_Type())
timeRangeName.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangeName.setStatus(_A)
class _TimeRangeOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('active',0),('inactive',1)))
_TimeRangeOperState_Type.__name__=_C
_TimeRangeOperState_Object=MibTableColumn
timeRangeOperState=_TimeRangeOperState_Object((1,3,6,1,4,1,4526,10,53,1,3,1,3),_TimeRangeOperState_Type())
timeRangeOperState.setMaxAccess(_G)
if mibBuilder.loadTexts:timeRangeOperState.setStatus(_A)
_TimeRangeStatus_Type=RowStatus
_TimeRangeStatus_Object=MibTableColumn
timeRangeStatus=_TimeRangeStatus_Object((1,3,6,1,4,1,4526,10,53,1,3,1,4),_TimeRangeStatus_Type())
timeRangeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangeStatus.setStatus(_A)
_TimeRangeAbsoluteEntryTable_Object=MibTable
timeRangeAbsoluteEntryTable=_TimeRangeAbsoluteEntryTable_Object((1,3,6,1,4,1,4526,10,53,1,4))
if mibBuilder.loadTexts:timeRangeAbsoluteEntryTable.setStatus(_A)
_TimeRangeAbsoluteEntry_Object=MibTableRow
timeRangeAbsoluteEntry=_TimeRangeAbsoluteEntry_Object((1,3,6,1,4,1,4526,10,53,1,4,1))
timeRangeAbsoluteEntry.setIndexNames((0,_D,_E),(0,_D,_J))
if mibBuilder.loadTexts:timeRangeAbsoluteEntry.setStatus(_A)
class _TimeRangeAbsoluteEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_TimeRangeAbsoluteEntryIndex_Type.__name__=_C
_TimeRangeAbsoluteEntryIndex_Object=MibTableColumn
timeRangeAbsoluteEntryIndex=_TimeRangeAbsoluteEntryIndex_Object((1,3,6,1,4,1,4526,10,53,1,4,1,1),_TimeRangeAbsoluteEntryIndex_Type())
timeRangeAbsoluteEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:timeRangeAbsoluteEntryIndex.setStatus(_A)
_TimeRangeAbsoluteStartDateAndTime_Type=TimeRangeAbsoluteDateAndTime
_TimeRangeAbsoluteStartDateAndTime_Object=MibTableColumn
timeRangeAbsoluteStartDateAndTime=_TimeRangeAbsoluteStartDateAndTime_Object((1,3,6,1,4,1,4526,10,53,1,4,1,2),_TimeRangeAbsoluteStartDateAndTime_Type())
timeRangeAbsoluteStartDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangeAbsoluteStartDateAndTime.setStatus(_A)
_TimeRangeAbsoluteEndDateAndTime_Type=TimeRangeAbsoluteDateAndTime
_TimeRangeAbsoluteEndDateAndTime_Object=MibTableColumn
timeRangeAbsoluteEndDateAndTime=_TimeRangeAbsoluteEndDateAndTime_Object((1,3,6,1,4,1,4526,10,53,1,4,1,3),_TimeRangeAbsoluteEndDateAndTime_Type())
timeRangeAbsoluteEndDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangeAbsoluteEndDateAndTime.setStatus(_A)
_TimeRangeAbsoluteStatus_Type=RowStatus
_TimeRangeAbsoluteStatus_Object=MibTableColumn
timeRangeAbsoluteStatus=_TimeRangeAbsoluteStatus_Object((1,3,6,1,4,1,4526,10,53,1,4,1,4),_TimeRangeAbsoluteStatus_Type())
timeRangeAbsoluteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangeAbsoluteStatus.setStatus(_A)
_TimeRangePeriodicEntryTable_Object=MibTable
timeRangePeriodicEntryTable=_TimeRangePeriodicEntryTable_Object((1,3,6,1,4,1,4526,10,53,1,5))
if mibBuilder.loadTexts:timeRangePeriodicEntryTable.setStatus(_A)
_TimeRangePeriodicEntry_Object=MibTableRow
timeRangePeriodicEntry=_TimeRangePeriodicEntry_Object((1,3,6,1,4,1,4526,10,53,1,5,1))
timeRangePeriodicEntry.setIndexNames((0,_D,_E),(0,_D,_K))
if mibBuilder.loadTexts:timeRangePeriodicEntry.setStatus(_A)
class _TimeRangePeriodicEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_TimeRangePeriodicEntryIndex_Type.__name__=_C
_TimeRangePeriodicEntryIndex_Object=MibTableColumn
timeRangePeriodicEntryIndex=_TimeRangePeriodicEntryIndex_Object((1,3,6,1,4,1,4526,10,53,1,5,1,1),_TimeRangePeriodicEntryIndex_Type())
timeRangePeriodicEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:timeRangePeriodicEntryIndex.setStatus(_A)
class _TimeRangePeriodicFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TimeRangePeriodicFrequency_Type.__name__=_C
_TimeRangePeriodicFrequency_Object=MibTableColumn
timeRangePeriodicFrequency=_TimeRangePeriodicFrequency_Object((1,3,6,1,4,1,4526,10,53,1,5,1,2),_TimeRangePeriodicFrequency_Type())
timeRangePeriodicFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicFrequency.setStatus(_A)
class _TimeRangePeriodicPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_TimeRangePeriodicPattern_Type.__name__=_C
_TimeRangePeriodicPattern_Object=MibTableColumn
timeRangePeriodicPattern=_TimeRangePeriodicPattern_Object((1,3,6,1,4,1,4526,10,53,1,5,1,3),_TimeRangePeriodicPattern_Type())
timeRangePeriodicPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicPattern.setStatus(_A)
_TimeRangePeriodicDayMask_Type=Integer32
_TimeRangePeriodicDayMask_Object=MibTableColumn
timeRangePeriodicDayMask=_TimeRangePeriodicDayMask_Object((1,3,6,1,4,1,4526,10,53,1,5,1,4),_TimeRangePeriodicDayMask_Type())
timeRangePeriodicDayMask.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicDayMask.setStatus(_A)
_TimeRangePeriodicStartDate_Type=TimeRangePeriodicDate
_TimeRangePeriodicStartDate_Object=MibTableColumn
timeRangePeriodicStartDate=_TimeRangePeriodicStartDate_Object((1,3,6,1,4,1,4526,10,53,1,5,1,5),_TimeRangePeriodicStartDate_Type())
timeRangePeriodicStartDate.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicStartDate.setStatus(_A)
class _TimeRangePeriodicStartDay_Type(Bits):namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7)))
_TimeRangePeriodicStartDay_Type.__name__=_F
_TimeRangePeriodicStartDay_Object=MibTableColumn
timeRangePeriodicStartDay=_TimeRangePeriodicStartDay_Object((1,3,6,1,4,1,4526,10,53,1,5,1,6),_TimeRangePeriodicStartDay_Type())
timeRangePeriodicStartDay.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicStartDay.setStatus(_A)
_TimeRangePeriodicStartTime_Type=TimeRangePeriodicTime
_TimeRangePeriodicStartTime_Object=MibTableColumn
timeRangePeriodicStartTime=_TimeRangePeriodicStartTime_Object((1,3,6,1,4,1,4526,10,53,1,5,1,7),_TimeRangePeriodicStartTime_Type())
timeRangePeriodicStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicStartTime.setStatus(_A)
_TimeRangePeriodicEndDate_Type=TimeRangePeriodicDate
_TimeRangePeriodicEndDate_Object=MibTableColumn
timeRangePeriodicEndDate=_TimeRangePeriodicEndDate_Object((1,3,6,1,4,1,4526,10,53,1,5,1,8),_TimeRangePeriodicEndDate_Type())
timeRangePeriodicEndDate.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicEndDate.setStatus(_A)
class _TimeRangePeriodicEndDay_Type(Bits):namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7)))
_TimeRangePeriodicEndDay_Type.__name__=_F
_TimeRangePeriodicEndDay_Object=MibTableColumn
timeRangePeriodicEndDay=_TimeRangePeriodicEndDay_Object((1,3,6,1,4,1,4526,10,53,1,5,1,9),_TimeRangePeriodicEndDay_Type())
timeRangePeriodicEndDay.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicEndDay.setStatus(_A)
_TimeRangePeriodicEndTime_Type=TimeRangePeriodicTime
_TimeRangePeriodicEndTime_Object=MibTableColumn
timeRangePeriodicEndTime=_TimeRangePeriodicEndTime_Object((1,3,6,1,4,1,4526,10,53,1,5,1,10),_TimeRangePeriodicEndTime_Type())
timeRangePeriodicEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicEndTime.setStatus(_A)
_TimeRangePeriodicStatus_Type=RowStatus
_TimeRangePeriodicStatus_Object=MibTableColumn
timeRangePeriodicStatus=_TimeRangePeriodicStatus_Object((1,3,6,1,4,1,4526,10,53,1,5,1,11),_TimeRangePeriodicStatus_Type())
timeRangePeriodicStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRangePeriodicStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'TimeRangeAbsoluteDateAndTime':TimeRangeAbsoluteDateAndTime,'TimeRangePeriodicTime':TimeRangePeriodicTime,'TimeRangePeriodicDate':TimeRangePeriodicDate,'fastPathTimeRange':fastPathTimeRange,'fastPathTimeRangeGroup':fastPathTimeRangeGroup,'timeRangeAdminMode':timeRangeAdminMode,'timeRangeIndexNextFree':timeRangeIndexNextFree,'timeRangeTable':timeRangeTable,'timeRangeEntry':timeRangeEntry,_E:timeRangeIndex,'timeRangeName':timeRangeName,'timeRangeOperState':timeRangeOperState,'timeRangeStatus':timeRangeStatus,'timeRangeAbsoluteEntryTable':timeRangeAbsoluteEntryTable,'timeRangeAbsoluteEntry':timeRangeAbsoluteEntry,_J:timeRangeAbsoluteEntryIndex,'timeRangeAbsoluteStartDateAndTime':timeRangeAbsoluteStartDateAndTime,'timeRangeAbsoluteEndDateAndTime':timeRangeAbsoluteEndDateAndTime,'timeRangeAbsoluteStatus':timeRangeAbsoluteStatus,'timeRangePeriodicEntryTable':timeRangePeriodicEntryTable,'timeRangePeriodicEntry':timeRangePeriodicEntry,_K:timeRangePeriodicEntryIndex,'timeRangePeriodicFrequency':timeRangePeriodicFrequency,'timeRangePeriodicPattern':timeRangePeriodicPattern,'timeRangePeriodicDayMask':timeRangePeriodicDayMask,'timeRangePeriodicStartDate':timeRangePeriodicStartDate,'timeRangePeriodicStartDay':timeRangePeriodicStartDay,'timeRangePeriodicStartTime':timeRangePeriodicStartTime,'timeRangePeriodicEndDate':timeRangePeriodicEndDate,'timeRangePeriodicEndDay':timeRangePeriodicEndDay,'timeRangePeriodicEndTime':timeRangePeriodicEndTime,'timeRangePeriodicStatus':timeRangePeriodicStatus})