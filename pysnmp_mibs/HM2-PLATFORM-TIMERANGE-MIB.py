_R='saturday'
_Q='friday'
_P='thursday'
_O='wednesday'
_N='tuesday'
_M='monday'
_L='sunday'
_K='hm2AgentTimeRangePeriodicEntryIndex'
_J='hm2AgentTimeRangeAbsoluteEntryIndex'
_I='read-only'
_H='DisplayString'
_G='not-accessible'
_F='Bits'
_E='hm2AgentTimeRangeIndex'
_D='Integer32'
_C='HM2-PLATFORM-TIMERANGE-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2PlatformMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2PlatformMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
hm2PlatformTimeRange=ModuleIdentity((1,3,6,1,4,1,248,12,53))
if mibBuilder.loadTexts:hm2PlatformTimeRange.setRevisions(('2011-01-26 00:00',))
class Hm2AgentTimeRangeAbsoluteDateAndTime(TextualConvention,OctetString):status=_A;displayHint='2d-1d-1d,1d:1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class Hm2AgentTimeRangePeriodicTime(TextualConvention,OctetString):status=_A;displayHint='1d:1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Hm2AgentTimeRangeGroup_ObjectIdentity=ObjectIdentity
hm2AgentTimeRangeGroup=_Hm2AgentTimeRangeGroup_ObjectIdentity((1,3,6,1,4,1,248,12,53,1))
_Hm2AgentTimeRangeIndexNextFree_Type=Integer32
_Hm2AgentTimeRangeIndexNextFree_Object=MibScalar
hm2AgentTimeRangeIndexNextFree=_Hm2AgentTimeRangeIndexNextFree_Object((1,3,6,1,4,1,248,12,53,1,1),_Hm2AgentTimeRangeIndexNextFree_Type())
hm2AgentTimeRangeIndexNextFree.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2AgentTimeRangeIndexNextFree.setStatus(_A)
_Hm2AgentTimeRangeTable_Object=MibTable
hm2AgentTimeRangeTable=_Hm2AgentTimeRangeTable_Object((1,3,6,1,4,1,248,12,53,1,2))
if mibBuilder.loadTexts:hm2AgentTimeRangeTable.setStatus(_A)
_Hm2AgentTimeRangeEntry_Object=MibTableRow
hm2AgentTimeRangeEntry=_Hm2AgentTimeRangeEntry_Object((1,3,6,1,4,1,248,12,53,1,2,1))
hm2AgentTimeRangeEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hm2AgentTimeRangeEntry.setStatus(_A)
_Hm2AgentTimeRangeIndex_Type=Unsigned32
_Hm2AgentTimeRangeIndex_Object=MibTableColumn
hm2AgentTimeRangeIndex=_Hm2AgentTimeRangeIndex_Object((1,3,6,1,4,1,248,12,53,1,2,1,1),_Hm2AgentTimeRangeIndex_Type())
hm2AgentTimeRangeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentTimeRangeIndex.setStatus(_A)
class _Hm2AgentTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Hm2AgentTimeRangeName_Type.__name__=_H
_Hm2AgentTimeRangeName_Object=MibTableColumn
hm2AgentTimeRangeName=_Hm2AgentTimeRangeName_Object((1,3,6,1,4,1,248,12,53,1,2,1,2),_Hm2AgentTimeRangeName_Type())
hm2AgentTimeRangeName.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangeName.setStatus(_A)
class _Hm2AgentTimeRangeOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('active',0),('inactive',1)))
_Hm2AgentTimeRangeOperState_Type.__name__=_D
_Hm2AgentTimeRangeOperState_Object=MibTableColumn
hm2AgentTimeRangeOperState=_Hm2AgentTimeRangeOperState_Object((1,3,6,1,4,1,248,12,53,1,2,1,3),_Hm2AgentTimeRangeOperState_Type())
hm2AgentTimeRangeOperState.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2AgentTimeRangeOperState.setStatus(_A)
_Hm2AgentTimeRangeStatus_Type=RowStatus
_Hm2AgentTimeRangeStatus_Object=MibTableColumn
hm2AgentTimeRangeStatus=_Hm2AgentTimeRangeStatus_Object((1,3,6,1,4,1,248,12,53,1,2,1,4),_Hm2AgentTimeRangeStatus_Type())
hm2AgentTimeRangeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangeStatus.setStatus(_A)
_Hm2AgentTimeRangeAbsoluteTable_Object=MibTable
hm2AgentTimeRangeAbsoluteTable=_Hm2AgentTimeRangeAbsoluteTable_Object((1,3,6,1,4,1,248,12,53,1,3))
if mibBuilder.loadTexts:hm2AgentTimeRangeAbsoluteTable.setStatus(_A)
_Hm2AgentTimeRangeAbsoluteEntry_Object=MibTableRow
hm2AgentTimeRangeAbsoluteEntry=_Hm2AgentTimeRangeAbsoluteEntry_Object((1,3,6,1,4,1,248,12,53,1,3,1))
hm2AgentTimeRangeAbsoluteEntry.setIndexNames((0,_C,_E),(0,_C,_J))
if mibBuilder.loadTexts:hm2AgentTimeRangeAbsoluteEntry.setStatus(_A)
class _Hm2AgentTimeRangeAbsoluteEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Hm2AgentTimeRangeAbsoluteEntryIndex_Type.__name__=_D
_Hm2AgentTimeRangeAbsoluteEntryIndex_Object=MibTableColumn
hm2AgentTimeRangeAbsoluteEntryIndex=_Hm2AgentTimeRangeAbsoluteEntryIndex_Object((1,3,6,1,4,1,248,12,53,1,3,1,1),_Hm2AgentTimeRangeAbsoluteEntryIndex_Type())
hm2AgentTimeRangeAbsoluteEntryIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentTimeRangeAbsoluteEntryIndex.setStatus(_A)
_Hm2AgentTimeRangeAbsoluteStartDateAndTime_Type=Hm2AgentTimeRangeAbsoluteDateAndTime
_Hm2AgentTimeRangeAbsoluteStartDateAndTime_Object=MibTableColumn
hm2AgentTimeRangeAbsoluteStartDateAndTime=_Hm2AgentTimeRangeAbsoluteStartDateAndTime_Object((1,3,6,1,4,1,248,12,53,1,3,1,2),_Hm2AgentTimeRangeAbsoluteStartDateAndTime_Type())
hm2AgentTimeRangeAbsoluteStartDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangeAbsoluteStartDateAndTime.setStatus(_A)
_Hm2AgentTimeRangeAbsoluteEndDateAndTime_Type=Hm2AgentTimeRangeAbsoluteDateAndTime
_Hm2AgentTimeRangeAbsoluteEndDateAndTime_Object=MibTableColumn
hm2AgentTimeRangeAbsoluteEndDateAndTime=_Hm2AgentTimeRangeAbsoluteEndDateAndTime_Object((1,3,6,1,4,1,248,12,53,1,3,1,3),_Hm2AgentTimeRangeAbsoluteEndDateAndTime_Type())
hm2AgentTimeRangeAbsoluteEndDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangeAbsoluteEndDateAndTime.setStatus(_A)
_Hm2AgentTimeRangeAbsoluteStatus_Type=RowStatus
_Hm2AgentTimeRangeAbsoluteStatus_Object=MibTableColumn
hm2AgentTimeRangeAbsoluteStatus=_Hm2AgentTimeRangeAbsoluteStatus_Object((1,3,6,1,4,1,248,12,53,1,3,1,4),_Hm2AgentTimeRangeAbsoluteStatus_Type())
hm2AgentTimeRangeAbsoluteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangeAbsoluteStatus.setStatus(_A)
_Hm2AgentTimeRangePeriodicTable_Object=MibTable
hm2AgentTimeRangePeriodicTable=_Hm2AgentTimeRangePeriodicTable_Object((1,3,6,1,4,1,248,12,53,1,4))
if mibBuilder.loadTexts:hm2AgentTimeRangePeriodicTable.setStatus(_A)
_Hm2AgentTimeRangePeriodicEntry_Object=MibTableRow
hm2AgentTimeRangePeriodicEntry=_Hm2AgentTimeRangePeriodicEntry_Object((1,3,6,1,4,1,248,12,53,1,4,1))
hm2AgentTimeRangePeriodicEntry.setIndexNames((0,_C,_E),(0,_C,_K))
if mibBuilder.loadTexts:hm2AgentTimeRangePeriodicEntry.setStatus(_A)
class _Hm2AgentTimeRangePeriodicEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Hm2AgentTimeRangePeriodicEntryIndex_Type.__name__=_D
_Hm2AgentTimeRangePeriodicEntryIndex_Object=MibTableColumn
hm2AgentTimeRangePeriodicEntryIndex=_Hm2AgentTimeRangePeriodicEntryIndex_Object((1,3,6,1,4,1,248,12,53,1,4,1,1),_Hm2AgentTimeRangePeriodicEntryIndex_Type())
hm2AgentTimeRangePeriodicEntryIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentTimeRangePeriodicEntryIndex.setStatus(_A)
class _Hm2AgentTimeRangePeriodicStartDay_Type(Bits):namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7)))
_Hm2AgentTimeRangePeriodicStartDay_Type.__name__=_F
_Hm2AgentTimeRangePeriodicStartDay_Object=MibTableColumn
hm2AgentTimeRangePeriodicStartDay=_Hm2AgentTimeRangePeriodicStartDay_Object((1,3,6,1,4,1,248,12,53,1,4,1,2),_Hm2AgentTimeRangePeriodicStartDay_Type())
hm2AgentTimeRangePeriodicStartDay.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangePeriodicStartDay.setStatus(_A)
_Hm2AgentTimeRangePeriodicStartTime_Type=Hm2AgentTimeRangePeriodicTime
_Hm2AgentTimeRangePeriodicStartTime_Object=MibTableColumn
hm2AgentTimeRangePeriodicStartTime=_Hm2AgentTimeRangePeriodicStartTime_Object((1,3,6,1,4,1,248,12,53,1,4,1,3),_Hm2AgentTimeRangePeriodicStartTime_Type())
hm2AgentTimeRangePeriodicStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangePeriodicStartTime.setStatus(_A)
class _Hm2AgentTimeRangePeriodicEndDay_Type(Bits):namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7)))
_Hm2AgentTimeRangePeriodicEndDay_Type.__name__=_F
_Hm2AgentTimeRangePeriodicEndDay_Object=MibTableColumn
hm2AgentTimeRangePeriodicEndDay=_Hm2AgentTimeRangePeriodicEndDay_Object((1,3,6,1,4,1,248,12,53,1,4,1,4),_Hm2AgentTimeRangePeriodicEndDay_Type())
hm2AgentTimeRangePeriodicEndDay.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangePeriodicEndDay.setStatus(_A)
_Hm2AgentTimeRangePeriodicEndTime_Type=Hm2AgentTimeRangePeriodicTime
_Hm2AgentTimeRangePeriodicEndTime_Object=MibTableColumn
hm2AgentTimeRangePeriodicEndTime=_Hm2AgentTimeRangePeriodicEndTime_Object((1,3,6,1,4,1,248,12,53,1,4,1,5),_Hm2AgentTimeRangePeriodicEndTime_Type())
hm2AgentTimeRangePeriodicEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangePeriodicEndTime.setStatus(_A)
_Hm2AgentTimeRangePeriodicStatus_Type=RowStatus
_Hm2AgentTimeRangePeriodicStatus_Object=MibTableColumn
hm2AgentTimeRangePeriodicStatus=_Hm2AgentTimeRangePeriodicStatus_Object((1,3,6,1,4,1,248,12,53,1,4,1,6),_Hm2AgentTimeRangePeriodicStatus_Type())
hm2AgentTimeRangePeriodicStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTimeRangePeriodicStatus.setStatus(_A)
class _Hm2AgentTimeRangeAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_Hm2AgentTimeRangeAdminMode_Type.__name__=_D
_Hm2AgentTimeRangeAdminMode_Object=MibScalar
hm2AgentTimeRangeAdminMode=_Hm2AgentTimeRangeAdminMode_Object((1,3,6,1,4,1,248,12,53,1,248),_Hm2AgentTimeRangeAdminMode_Type())
hm2AgentTimeRangeAdminMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:hm2AgentTimeRangeAdminMode.setStatus(_A)
_Hm2AgentTimeRangeSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2AgentTimeRangeSNMPExtensionGroup=_Hm2AgentTimeRangeSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,12,53,260))
_Hm2AgentTimeRangeEndGreaterThanStartErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentTimeRangeEndGreaterThanStartErrorReturn=_Hm2AgentTimeRangeEndGreaterThanStartErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,53,260,1))
if mibBuilder.loadTexts:hm2AgentTimeRangeEndGreaterThanStartErrorReturn.setStatus(_A)
_Hm2AgentTimeRangeEntriesOverlapErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentTimeRangeEntriesOverlapErrorReturn=_Hm2AgentTimeRangeEntriesOverlapErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,53,260,2))
if mibBuilder.loadTexts:hm2AgentTimeRangeEntriesOverlapErrorReturn.setStatus(_A)
_Hm2AgentTimeRangeTooManyAbsoluteEntriesErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentTimeRangeTooManyAbsoluteEntriesErrorReturn=_Hm2AgentTimeRangeTooManyAbsoluteEntriesErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,53,260,3))
if mibBuilder.loadTexts:hm2AgentTimeRangeTooManyAbsoluteEntriesErrorReturn.setStatus(_A)
_Hm2AgentTimeRangeDifferentMultiDayListsErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentTimeRangeDifferentMultiDayListsErrorReturn=_Hm2AgentTimeRangeDifferentMultiDayListsErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,53,260,4))
if mibBuilder.loadTexts:hm2AgentTimeRangeDifferentMultiDayListsErrorReturn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Hm2AgentTimeRangeAbsoluteDateAndTime':Hm2AgentTimeRangeAbsoluteDateAndTime,'Hm2AgentTimeRangePeriodicTime':Hm2AgentTimeRangePeriodicTime,'hm2PlatformTimeRange':hm2PlatformTimeRange,'hm2AgentTimeRangeGroup':hm2AgentTimeRangeGroup,'hm2AgentTimeRangeIndexNextFree':hm2AgentTimeRangeIndexNextFree,'hm2AgentTimeRangeTable':hm2AgentTimeRangeTable,'hm2AgentTimeRangeEntry':hm2AgentTimeRangeEntry,_E:hm2AgentTimeRangeIndex,'hm2AgentTimeRangeName':hm2AgentTimeRangeName,'hm2AgentTimeRangeOperState':hm2AgentTimeRangeOperState,'hm2AgentTimeRangeStatus':hm2AgentTimeRangeStatus,'hm2AgentTimeRangeAbsoluteTable':hm2AgentTimeRangeAbsoluteTable,'hm2AgentTimeRangeAbsoluteEntry':hm2AgentTimeRangeAbsoluteEntry,_J:hm2AgentTimeRangeAbsoluteEntryIndex,'hm2AgentTimeRangeAbsoluteStartDateAndTime':hm2AgentTimeRangeAbsoluteStartDateAndTime,'hm2AgentTimeRangeAbsoluteEndDateAndTime':hm2AgentTimeRangeAbsoluteEndDateAndTime,'hm2AgentTimeRangeAbsoluteStatus':hm2AgentTimeRangeAbsoluteStatus,'hm2AgentTimeRangePeriodicTable':hm2AgentTimeRangePeriodicTable,'hm2AgentTimeRangePeriodicEntry':hm2AgentTimeRangePeriodicEntry,_K:hm2AgentTimeRangePeriodicEntryIndex,'hm2AgentTimeRangePeriodicStartDay':hm2AgentTimeRangePeriodicStartDay,'hm2AgentTimeRangePeriodicStartTime':hm2AgentTimeRangePeriodicStartTime,'hm2AgentTimeRangePeriodicEndDay':hm2AgentTimeRangePeriodicEndDay,'hm2AgentTimeRangePeriodicEndTime':hm2AgentTimeRangePeriodicEndTime,'hm2AgentTimeRangePeriodicStatus':hm2AgentTimeRangePeriodicStatus,'hm2AgentTimeRangeAdminMode':hm2AgentTimeRangeAdminMode,'hm2AgentTimeRangeSNMPExtensionGroup':hm2AgentTimeRangeSNMPExtensionGroup,'hm2AgentTimeRangeEndGreaterThanStartErrorReturn':hm2AgentTimeRangeEndGreaterThanStartErrorReturn,'hm2AgentTimeRangeEntriesOverlapErrorReturn':hm2AgentTimeRangeEntriesOverlapErrorReturn,'hm2AgentTimeRangeTooManyAbsoluteEntriesErrorReturn':hm2AgentTimeRangeTooManyAbsoluteEntriesErrorReturn,'hm2AgentTimeRangeDifferentMultiDayListsErrorReturn':hm2AgentTimeRangeDifferentMultiDayListsErrorReturn})