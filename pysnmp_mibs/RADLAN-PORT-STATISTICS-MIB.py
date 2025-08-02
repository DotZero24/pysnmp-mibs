_O='rlPortStatLastEventCounterName'
_N='rlPortStatLastEventIfIndex'
_M='rlPortStatLastSampleCounterName'
_L='rlPortStatLastSampleStatSubType'
_K='rlPortStatLastSampleIfIndex'
_J='rlPortStatSampleStatID'
_I='rlPortStatSampleCounterName'
_H='rlPortStatSampleStatSubType'
_G='rlPortStatSampleIfIndex'
_F='read-write'
_E='DisplayString'
_D='not-accessible'
_C='RADLAN-PORT-STATISTICS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlPortStat=ModuleIdentity((1,3,6,1,4,1,89,223))
if mibBuilder.loadTexts:rlPortStat.setRevisions(('2015-04-06 00:00',))
class PortStatisticsSubType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('second',1),('minute',2),('hour',3),('day',4),('week',5)))
class PortStatisticsSampleClockSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internal',1),('sntp',2),('userDefined',3)))
class PortStatisticsCounterName(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*(('anyCounter',0),('unicastFrameSent',1),('broadcastFrameSent',2),('multicastFrameSent',3),('goodOctetsSent',4),('txUtilization',5),('goodUnicastFrameReceived',6),('broadcastFrameReceived',7),('multicastFrameReceived',8),('rxErrorFrameReceived',9),('totalOctetsReceived',10),('rxUtilization',11),('txRxUtilization',12),('frames64B',13),('frames65To127B',14),('frames128To255B',15),('frames256To511B',16),('frames512To1023B',17),('frames1024To1518B',18),('dot3StatsFCSErrors',19),('dot3StatsSingleCollisionFrames',20),('dot3StatsLateCollisions',21),('dot3StatsExcessiveCollisions',22),('dot3StatsFrameTooLongs',23),('dot3StatsInternalMacReceiveErrors',24),('dot3InPauseFrames',25),('dot3OutPauseFrames',26),('etherStatsDropEvents',27),('etherStatsCRCAlignErrors',28),('etherStatsUndersizePkts',29),('etherStatsOversizePkts',30),('etherStatsFragments',31),('etherStatsJabbers',32),('etherStatsCollisions',33),('goodOctetsReceived',34),('badOctetsReceived',35),('goodFrameSent',36),('goodFrameReceived',37),('lastCounterSpecifier',38)))
_RlPortStatEnabledPorts_Type=PortList
_RlPortStatEnabledPorts_Object=MibScalar
rlPortStatEnabledPorts=_RlPortStatEnabledPorts_Object((1,3,6,1,4,1,89,223,1),_RlPortStatEnabledPorts_Type())
rlPortStatEnabledPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPortStatEnabledPorts.setStatus(_A)
_RlPortStatClearPorts_Type=PortList
_RlPortStatClearPorts_Object=MibScalar
rlPortStatClearPorts=_RlPortStatClearPorts_Object((1,3,6,1,4,1,89,223,2),_RlPortStatClearPorts_Type())
rlPortStatClearPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPortStatClearPorts.setStatus(_A)
_RlPortStatSampleTable_Object=MibTable
rlPortStatSampleTable=_RlPortStatSampleTable_Object((1,3,6,1,4,1,89,223,3))
if mibBuilder.loadTexts:rlPortStatSampleTable.setStatus(_A)
_RlPortStatSampleEntry_Object=MibTableRow
rlPortStatSampleEntry=_RlPortStatSampleEntry_Object((1,3,6,1,4,1,89,223,3,1))
rlPortStatSampleEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:rlPortStatSampleEntry.setStatus(_A)
_RlPortStatSampleIfIndex_Type=InterfaceIndex
_RlPortStatSampleIfIndex_Object=MibTableColumn
rlPortStatSampleIfIndex=_RlPortStatSampleIfIndex_Object((1,3,6,1,4,1,89,223,3,1,1),_RlPortStatSampleIfIndex_Type())
rlPortStatSampleIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPortStatSampleIfIndex.setStatus(_A)
_RlPortStatSampleStatSubType_Type=PortStatisticsSubType
_RlPortStatSampleStatSubType_Object=MibTableColumn
rlPortStatSampleStatSubType=_RlPortStatSampleStatSubType_Object((1,3,6,1,4,1,89,223,3,1,2),_RlPortStatSampleStatSubType_Type())
rlPortStatSampleStatSubType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPortStatSampleStatSubType.setStatus(_A)
_RlPortStatSampleCounterName_Type=PortStatisticsCounterName
_RlPortStatSampleCounterName_Object=MibTableColumn
rlPortStatSampleCounterName=_RlPortStatSampleCounterName_Object((1,3,6,1,4,1,89,223,3,1,3),_RlPortStatSampleCounterName_Type())
rlPortStatSampleCounterName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPortStatSampleCounterName.setStatus(_A)
_RlPortStatSampleStatID_Type=Unsigned32
_RlPortStatSampleStatID_Object=MibTableColumn
rlPortStatSampleStatID=_RlPortStatSampleStatID_Object((1,3,6,1,4,1,89,223,3,1,4),_RlPortStatSampleStatID_Type())
rlPortStatSampleStatID.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPortStatSampleStatID.setStatus(_A)
_RlPortStatSampleCollectionInterval_Type=Unsigned32
_RlPortStatSampleCollectionInterval_Object=MibTableColumn
rlPortStatSampleCollectionInterval=_RlPortStatSampleCollectionInterval_Object((1,3,6,1,4,1,89,223,3,1,5),_RlPortStatSampleCollectionInterval_Type())
rlPortStatSampleCollectionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatSampleCollectionInterval.setStatus(_A)
_RlPortStatSampleSystemCollectionTime_Type=Unsigned32
_RlPortStatSampleSystemCollectionTime_Object=MibTableColumn
rlPortStatSampleSystemCollectionTime=_RlPortStatSampleSystemCollectionTime_Object((1,3,6,1,4,1,89,223,3,1,6),_RlPortStatSampleSystemCollectionTime_Type())
rlPortStatSampleSystemCollectionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatSampleSystemCollectionTime.setStatus(_A)
_RlPortStatSampleCollectionTime_Type=Unsigned32
_RlPortStatSampleCollectionTime_Object=MibTableColumn
rlPortStatSampleCollectionTime=_RlPortStatSampleCollectionTime_Object((1,3,6,1,4,1,89,223,3,1,7),_RlPortStatSampleCollectionTime_Type())
rlPortStatSampleCollectionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatSampleCollectionTime.setStatus(_A)
class _RlPortStatSampleCollectionTimeStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RlPortStatSampleCollectionTimeStr_Type.__name__=_E
_RlPortStatSampleCollectionTimeStr_Object=MibTableColumn
rlPortStatSampleCollectionTimeStr=_RlPortStatSampleCollectionTimeStr_Object((1,3,6,1,4,1,89,223,3,1,8),_RlPortStatSampleCollectionTimeStr_Type())
rlPortStatSampleCollectionTimeStr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatSampleCollectionTimeStr.setStatus(_A)
_RlPortStatSampleCounterValue_Type=Counter64
_RlPortStatSampleCounterValue_Object=MibTableColumn
rlPortStatSampleCounterValue=_RlPortStatSampleCounterValue_Object((1,3,6,1,4,1,89,223,3,1,9),_RlPortStatSampleCounterValue_Type())
rlPortStatSampleCounterValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatSampleCounterValue.setStatus(_A)
_RlPortStatSamplePartialFlag_Type=TruthValue
_RlPortStatSamplePartialFlag_Object=MibTableColumn
rlPortStatSamplePartialFlag=_RlPortStatSamplePartialFlag_Object((1,3,6,1,4,1,89,223,3,1,10),_RlPortStatSamplePartialFlag_Type())
rlPortStatSamplePartialFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatSamplePartialFlag.setStatus(_A)
_RlPortStatSampleClockSource_Type=PortStatisticsSampleClockSource
_RlPortStatSampleClockSource_Object=MibTableColumn
rlPortStatSampleClockSource=_RlPortStatSampleClockSource_Object((1,3,6,1,4,1,89,223,3,1,11),_RlPortStatSampleClockSource_Type())
rlPortStatSampleClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatSampleClockSource.setStatus(_A)
_RlPortStatLastSampleTable_Object=MibTable
rlPortStatLastSampleTable=_RlPortStatLastSampleTable_Object((1,3,6,1,4,1,89,223,4))
if mibBuilder.loadTexts:rlPortStatLastSampleTable.setStatus(_A)
_RlPortStatLastSampleEntry_Object=MibTableRow
rlPortStatLastSampleEntry=_RlPortStatLastSampleEntry_Object((1,3,6,1,4,1,89,223,4,1))
rlPortStatLastSampleEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:rlPortStatLastSampleEntry.setStatus(_A)
_RlPortStatLastSampleIfIndex_Type=InterfaceIndex
_RlPortStatLastSampleIfIndex_Object=MibTableColumn
rlPortStatLastSampleIfIndex=_RlPortStatLastSampleIfIndex_Object((1,3,6,1,4,1,89,223,4,1,1),_RlPortStatLastSampleIfIndex_Type())
rlPortStatLastSampleIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPortStatLastSampleIfIndex.setStatus(_A)
_RlPortStatLastSampleStatSubType_Type=PortStatisticsSubType
_RlPortStatLastSampleStatSubType_Object=MibTableColumn
rlPortStatLastSampleStatSubType=_RlPortStatLastSampleStatSubType_Object((1,3,6,1,4,1,89,223,4,1,2),_RlPortStatLastSampleStatSubType_Type())
rlPortStatLastSampleStatSubType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPortStatLastSampleStatSubType.setStatus(_A)
_RlPortStatLastSampleCounterName_Type=PortStatisticsCounterName
_RlPortStatLastSampleCounterName_Object=MibTableColumn
rlPortStatLastSampleCounterName=_RlPortStatLastSampleCounterName_Object((1,3,6,1,4,1,89,223,4,1,3),_RlPortStatLastSampleCounterName_Type())
rlPortStatLastSampleCounterName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPortStatLastSampleCounterName.setStatus(_A)
_RlPortStatLastSampleStatID_Type=Unsigned32
_RlPortStatLastSampleStatID_Object=MibTableColumn
rlPortStatLastSampleStatID=_RlPortStatLastSampleStatID_Object((1,3,6,1,4,1,89,223,4,1,4),_RlPortStatLastSampleStatID_Type())
rlPortStatLastSampleStatID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastSampleStatID.setStatus(_A)
_RlPortStatLastSampleCollectionInterval_Type=Unsigned32
_RlPortStatLastSampleCollectionInterval_Object=MibTableColumn
rlPortStatLastSampleCollectionInterval=_RlPortStatLastSampleCollectionInterval_Object((1,3,6,1,4,1,89,223,4,1,5),_RlPortStatLastSampleCollectionInterval_Type())
rlPortStatLastSampleCollectionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastSampleCollectionInterval.setStatus(_A)
_RlPortStatLastSampleSystemCollectionTime_Type=Unsigned32
_RlPortStatLastSampleSystemCollectionTime_Object=MibTableColumn
rlPortStatLastSampleSystemCollectionTime=_RlPortStatLastSampleSystemCollectionTime_Object((1,3,6,1,4,1,89,223,4,1,6),_RlPortStatLastSampleSystemCollectionTime_Type())
rlPortStatLastSampleSystemCollectionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastSampleSystemCollectionTime.setStatus(_A)
_RlPortStatLastSampleCollectionTime_Type=Unsigned32
_RlPortStatLastSampleCollectionTime_Object=MibTableColumn
rlPortStatLastSampleCollectionTime=_RlPortStatLastSampleCollectionTime_Object((1,3,6,1,4,1,89,223,4,1,7),_RlPortStatLastSampleCollectionTime_Type())
rlPortStatLastSampleCollectionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastSampleCollectionTime.setStatus(_A)
class _RlPortStatLastSampleCollectionTimeStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RlPortStatLastSampleCollectionTimeStr_Type.__name__=_E
_RlPortStatLastSampleCollectionTimeStr_Object=MibTableColumn
rlPortStatLastSampleCollectionTimeStr=_RlPortStatLastSampleCollectionTimeStr_Object((1,3,6,1,4,1,89,223,4,1,8),_RlPortStatLastSampleCollectionTimeStr_Type())
rlPortStatLastSampleCollectionTimeStr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastSampleCollectionTimeStr.setStatus(_A)
_RlPortStatLastSampleCounterValue_Type=Counter64
_RlPortStatLastSampleCounterValue_Object=MibTableColumn
rlPortStatLastSampleCounterValue=_RlPortStatLastSampleCounterValue_Object((1,3,6,1,4,1,89,223,4,1,9),_RlPortStatLastSampleCounterValue_Type())
rlPortStatLastSampleCounterValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastSampleCounterValue.setStatus(_A)
_RlPortStatLastSamplePartialFlag_Type=TruthValue
_RlPortStatLastSamplePartialFlag_Object=MibTableColumn
rlPortStatLastSamplePartialFlag=_RlPortStatLastSamplePartialFlag_Object((1,3,6,1,4,1,89,223,4,1,10),_RlPortStatLastSamplePartialFlag_Type())
rlPortStatLastSamplePartialFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastSamplePartialFlag.setStatus(_A)
_RlPortStatLastSampleClockSource_Type=PortStatisticsSampleClockSource
_RlPortStatLastSampleClockSource_Object=MibTableColumn
rlPortStatLastSampleClockSource=_RlPortStatLastSampleClockSource_Object((1,3,6,1,4,1,89,223,4,1,11),_RlPortStatLastSampleClockSource_Type())
rlPortStatLastSampleClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastSampleClockSource.setStatus(_A)
_RlPortStatLastEventTable_Object=MibTable
rlPortStatLastEventTable=_RlPortStatLastEventTable_Object((1,3,6,1,4,1,89,223,5))
if mibBuilder.loadTexts:rlPortStatLastEventTable.setStatus(_A)
_RlPortStatLastEventEntry_Object=MibTableRow
rlPortStatLastEventEntry=_RlPortStatLastEventEntry_Object((1,3,6,1,4,1,89,223,5,1))
rlPortStatLastEventEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:rlPortStatLastEventEntry.setStatus(_A)
_RlPortStatLastEventIfIndex_Type=InterfaceIndex
_RlPortStatLastEventIfIndex_Object=MibTableColumn
rlPortStatLastEventIfIndex=_RlPortStatLastEventIfIndex_Object((1,3,6,1,4,1,89,223,5,1,1),_RlPortStatLastEventIfIndex_Type())
rlPortStatLastEventIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPortStatLastEventIfIndex.setStatus(_A)
_RlPortStatLastEventCounterName_Type=PortStatisticsCounterName
_RlPortStatLastEventCounterName_Object=MibTableColumn
rlPortStatLastEventCounterName=_RlPortStatLastEventCounterName_Object((1,3,6,1,4,1,89,223,5,1,2),_RlPortStatLastEventCounterName_Type())
rlPortStatLastEventCounterName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlPortStatLastEventCounterName.setStatus(_A)
_RlPortStatLastEventSystemTime_Type=Unsigned32
_RlPortStatLastEventSystemTime_Object=MibTableColumn
rlPortStatLastEventSystemTime=_RlPortStatLastEventSystemTime_Object((1,3,6,1,4,1,89,223,5,1,3),_RlPortStatLastEventSystemTime_Type())
rlPortStatLastEventSystemTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastEventSystemTime.setStatus(_A)
_RlPortStatLastEventPosixTime_Type=Unsigned32
_RlPortStatLastEventPosixTime_Object=MibTableColumn
rlPortStatLastEventPosixTime=_RlPortStatLastEventPosixTime_Object((1,3,6,1,4,1,89,223,5,1,4),_RlPortStatLastEventPosixTime_Type())
rlPortStatLastEventPosixTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastEventPosixTime.setStatus(_A)
class _RlPortStatLastEventTimeStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RlPortStatLastEventTimeStr_Type.__name__=_E
_RlPortStatLastEventTimeStr_Object=MibTableColumn
rlPortStatLastEventTimeStr=_RlPortStatLastEventTimeStr_Object((1,3,6,1,4,1,89,223,5,1,5),_RlPortStatLastEventTimeStr_Type())
rlPortStatLastEventTimeStr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastEventTimeStr.setStatus(_A)
_RlPortStatLastEventCounter_Type=PortStatisticsCounterName
_RlPortStatLastEventCounter_Object=MibTableColumn
rlPortStatLastEventCounter=_RlPortStatLastEventCounter_Object((1,3,6,1,4,1,89,223,5,1,6),_RlPortStatLastEventCounter_Type())
rlPortStatLastEventCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastEventCounter.setStatus(_A)
_RlPortStatLastEventCounterValue_Type=Counter64
_RlPortStatLastEventCounterValue_Object=MibTableColumn
rlPortStatLastEventCounterValue=_RlPortStatLastEventCounterValue_Object((1,3,6,1,4,1,89,223,5,1,7),_RlPortStatLastEventCounterValue_Type())
rlPortStatLastEventCounterValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortStatLastEventCounterValue.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PortStatisticsSubType':PortStatisticsSubType,'PortStatisticsSampleClockSource':PortStatisticsSampleClockSource,'PortStatisticsCounterName':PortStatisticsCounterName,'rlPortStat':rlPortStat,'rlPortStatEnabledPorts':rlPortStatEnabledPorts,'rlPortStatClearPorts':rlPortStatClearPorts,'rlPortStatSampleTable':rlPortStatSampleTable,'rlPortStatSampleEntry':rlPortStatSampleEntry,_G:rlPortStatSampleIfIndex,_H:rlPortStatSampleStatSubType,_I:rlPortStatSampleCounterName,_J:rlPortStatSampleStatID,'rlPortStatSampleCollectionInterval':rlPortStatSampleCollectionInterval,'rlPortStatSampleSystemCollectionTime':rlPortStatSampleSystemCollectionTime,'rlPortStatSampleCollectionTime':rlPortStatSampleCollectionTime,'rlPortStatSampleCollectionTimeStr':rlPortStatSampleCollectionTimeStr,'rlPortStatSampleCounterValue':rlPortStatSampleCounterValue,'rlPortStatSamplePartialFlag':rlPortStatSamplePartialFlag,'rlPortStatSampleClockSource':rlPortStatSampleClockSource,'rlPortStatLastSampleTable':rlPortStatLastSampleTable,'rlPortStatLastSampleEntry':rlPortStatLastSampleEntry,_K:rlPortStatLastSampleIfIndex,_L:rlPortStatLastSampleStatSubType,_M:rlPortStatLastSampleCounterName,'rlPortStatLastSampleStatID':rlPortStatLastSampleStatID,'rlPortStatLastSampleCollectionInterval':rlPortStatLastSampleCollectionInterval,'rlPortStatLastSampleSystemCollectionTime':rlPortStatLastSampleSystemCollectionTime,'rlPortStatLastSampleCollectionTime':rlPortStatLastSampleCollectionTime,'rlPortStatLastSampleCollectionTimeStr':rlPortStatLastSampleCollectionTimeStr,'rlPortStatLastSampleCounterValue':rlPortStatLastSampleCounterValue,'rlPortStatLastSamplePartialFlag':rlPortStatLastSamplePartialFlag,'rlPortStatLastSampleClockSource':rlPortStatLastSampleClockSource,'rlPortStatLastEventTable':rlPortStatLastEventTable,'rlPortStatLastEventEntry':rlPortStatLastEventEntry,_N:rlPortStatLastEventIfIndex,_O:rlPortStatLastEventCounterName,'rlPortStatLastEventSystemTime':rlPortStatLastEventSystemTime,'rlPortStatLastEventPosixTime':rlPortStatLastEventPosixTime,'rlPortStatLastEventTimeStr':rlPortStatLastEventTimeStr,'rlPortStatLastEventCounter':rlPortStatLastEventCounter,'rlPortStatLastEventCounterValue':rlPortStatLastEventCounterValue})