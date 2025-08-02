_U='rAlarmFallingThreshold'
_T='rAlarmRisingThreshold'
_S='rLogIndex'
_R='rLogEventIndex'
_Q='rEventIndex'
_P='rEtherHistorySampleIndex'
_O='rEtherHistoryIndex'
_N='rHistoryControlIndex'
_M='rEtherStatsIndex'
_L='NotificationType'
_K='OctetString'
_J='rAlarmValue'
_I='rAlarmSampleType'
_H='rAlarmVariable'
_G='DisplayString'
_F='rAlarmIndex'
_E='Integer32'
_D='SWITCH-RMON-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_L,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,'TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
rmonMib=ModuleIdentity((1,3,6,1,4,1,8886,6,1,22))
class OwnerString(DisplayString):0
class EntryStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
_RStatistics_ObjectIdentity=ObjectIdentity
rStatistics=_RStatistics_ObjectIdentity((1,3,6,1,4,1,8886,6,1,22,1))
_REtherStatsTable_Object=MibTable
rEtherStatsTable=_REtherStatsTable_Object((1,3,6,1,4,1,8886,6,1,22,1,1))
if mibBuilder.loadTexts:rEtherStatsTable.setStatus(_A)
_REtherStatsEntry_Object=MibTableRow
rEtherStatsEntry=_REtherStatsEntry_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1))
rEtherStatsEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:rEtherStatsEntry.setStatus(_A)
class _REtherStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_REtherStatsIndex_Type.__name__=_E
_REtherStatsIndex_Object=MibTableColumn
rEtherStatsIndex=_REtherStatsIndex_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,1),_REtherStatsIndex_Type())
rEtherStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsIndex.setStatus(_A)
_REtherStatsDataSource_Type=ObjectIdentifier
_REtherStatsDataSource_Object=MibTableColumn
rEtherStatsDataSource=_REtherStatsDataSource_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,2),_REtherStatsDataSource_Type())
rEtherStatsDataSource.setMaxAccess(_C)
if mibBuilder.loadTexts:rEtherStatsDataSource.setStatus(_A)
_REtherStatsDropEvents_Type=Counter32
_REtherStatsDropEvents_Object=MibTableColumn
rEtherStatsDropEvents=_REtherStatsDropEvents_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,3),_REtherStatsDropEvents_Type())
rEtherStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsDropEvents.setStatus(_A)
_REtherStatsOctets_Type=Counter32
_REtherStatsOctets_Object=MibTableColumn
rEtherStatsOctets=_REtherStatsOctets_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,4),_REtherStatsOctets_Type())
rEtherStatsOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsOctets.setStatus(_A)
_REtherStatsPkts_Type=Counter32
_REtherStatsPkts_Object=MibTableColumn
rEtherStatsPkts=_REtherStatsPkts_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,5),_REtherStatsPkts_Type())
rEtherStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsPkts.setStatus(_A)
_REtherStatsBroadcastPkts_Type=Counter32
_REtherStatsBroadcastPkts_Object=MibTableColumn
rEtherStatsBroadcastPkts=_REtherStatsBroadcastPkts_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,6),_REtherStatsBroadcastPkts_Type())
rEtherStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsBroadcastPkts.setStatus(_A)
_REtherStatsMulticastPkts_Type=Counter32
_REtherStatsMulticastPkts_Object=MibTableColumn
rEtherStatsMulticastPkts=_REtherStatsMulticastPkts_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,7),_REtherStatsMulticastPkts_Type())
rEtherStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsMulticastPkts.setStatus(_A)
_REtherStatsCRCAlignErrors_Type=Counter32
_REtherStatsCRCAlignErrors_Object=MibTableColumn
rEtherStatsCRCAlignErrors=_REtherStatsCRCAlignErrors_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,8),_REtherStatsCRCAlignErrors_Type())
rEtherStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsCRCAlignErrors.setStatus(_A)
_REtherStatsUndersizePkts_Type=Counter32
_REtherStatsUndersizePkts_Object=MibTableColumn
rEtherStatsUndersizePkts=_REtherStatsUndersizePkts_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,9),_REtherStatsUndersizePkts_Type())
rEtherStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsUndersizePkts.setStatus(_A)
_REtherStatsOversizePkts_Type=Counter32
_REtherStatsOversizePkts_Object=MibTableColumn
rEtherStatsOversizePkts=_REtherStatsOversizePkts_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,10),_REtherStatsOversizePkts_Type())
rEtherStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsOversizePkts.setStatus(_A)
_REtherStatsFragments_Type=Counter32
_REtherStatsFragments_Object=MibTableColumn
rEtherStatsFragments=_REtherStatsFragments_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,11),_REtherStatsFragments_Type())
rEtherStatsFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsFragments.setStatus(_A)
_REtherStatsJabbers_Type=Counter32
_REtherStatsJabbers_Object=MibTableColumn
rEtherStatsJabbers=_REtherStatsJabbers_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,12),_REtherStatsJabbers_Type())
rEtherStatsJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsJabbers.setStatus(_A)
_REtherStatsCollisions_Type=Counter32
_REtherStatsCollisions_Object=MibTableColumn
rEtherStatsCollisions=_REtherStatsCollisions_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,13),_REtherStatsCollisions_Type())
rEtherStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsCollisions.setStatus(_A)
_REtherStatsPkts64Octets_Type=Counter32
_REtherStatsPkts64Octets_Object=MibTableColumn
rEtherStatsPkts64Octets=_REtherStatsPkts64Octets_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,14),_REtherStatsPkts64Octets_Type())
rEtherStatsPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsPkts64Octets.setStatus(_A)
_REtherStatsPkts65to127Octets_Type=Counter32
_REtherStatsPkts65to127Octets_Object=MibTableColumn
rEtherStatsPkts65to127Octets=_REtherStatsPkts65to127Octets_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,15),_REtherStatsPkts65to127Octets_Type())
rEtherStatsPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsPkts65to127Octets.setStatus(_A)
_REtherStatsPkts128to255Octets_Type=Counter32
_REtherStatsPkts128to255Octets_Object=MibTableColumn
rEtherStatsPkts128to255Octets=_REtherStatsPkts128to255Octets_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,16),_REtherStatsPkts128to255Octets_Type())
rEtherStatsPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsPkts128to255Octets.setStatus(_A)
_REtherStatsPkts256to511Octets_Type=Counter32
_REtherStatsPkts256to511Octets_Object=MibTableColumn
rEtherStatsPkts256to511Octets=_REtherStatsPkts256to511Octets_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,17),_REtherStatsPkts256to511Octets_Type())
rEtherStatsPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsPkts256to511Octets.setStatus(_A)
_REtherStatsPkts512to1023Octets_Type=Counter32
_REtherStatsPkts512to1023Octets_Object=MibTableColumn
rEtherStatsPkts512to1023Octets=_REtherStatsPkts512to1023Octets_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,18),_REtherStatsPkts512to1023Octets_Type())
rEtherStatsPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsPkts512to1023Octets.setStatus(_A)
_REtherStatsPkts1024to1518Octets_Type=Counter32
_REtherStatsPkts1024to1518Octets_Object=MibTableColumn
rEtherStatsPkts1024to1518Octets=_REtherStatsPkts1024to1518Octets_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,19),_REtherStatsPkts1024to1518Octets_Type())
rEtherStatsPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherStatsPkts1024to1518Octets.setStatus(_A)
_REtherStatsOwner_Type=OwnerString
_REtherStatsOwner_Object=MibTableColumn
rEtherStatsOwner=_REtherStatsOwner_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,20),_REtherStatsOwner_Type())
rEtherStatsOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:rEtherStatsOwner.setStatus(_A)
_REtherStatsStatus_Type=EntryStatus
_REtherStatsStatus_Object=MibTableColumn
rEtherStatsStatus=_REtherStatsStatus_Object((1,3,6,1,4,1,8886,6,1,22,1,1,1,21),_REtherStatsStatus_Type())
rEtherStatsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rEtherStatsStatus.setStatus(_A)
_RHistory_ObjectIdentity=ObjectIdentity
rHistory=_RHistory_ObjectIdentity((1,3,6,1,4,1,8886,6,1,22,2))
_RHistoryControlTable_Object=MibTable
rHistoryControlTable=_RHistoryControlTable_Object((1,3,6,1,4,1,8886,6,1,22,2,1))
if mibBuilder.loadTexts:rHistoryControlTable.setStatus(_A)
_RHistoryControlEntry_Object=MibTableRow
rHistoryControlEntry=_RHistoryControlEntry_Object((1,3,6,1,4,1,8886,6,1,22,2,1,1))
rHistoryControlEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:rHistoryControlEntry.setStatus(_A)
class _RHistoryControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RHistoryControlIndex_Type.__name__=_E
_RHistoryControlIndex_Object=MibTableColumn
rHistoryControlIndex=_RHistoryControlIndex_Object((1,3,6,1,4,1,8886,6,1,22,2,1,1,1),_RHistoryControlIndex_Type())
rHistoryControlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rHistoryControlIndex.setStatus(_A)
_RHistoryControlDataSource_Type=ObjectIdentifier
_RHistoryControlDataSource_Object=MibTableColumn
rHistoryControlDataSource=_RHistoryControlDataSource_Object((1,3,6,1,4,1,8886,6,1,22,2,1,1,2),_RHistoryControlDataSource_Type())
rHistoryControlDataSource.setMaxAccess(_C)
if mibBuilder.loadTexts:rHistoryControlDataSource.setStatus(_A)
class _RHistoryControlBucketsRequested_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RHistoryControlBucketsRequested_Type.__name__=_E
_RHistoryControlBucketsRequested_Object=MibTableColumn
rHistoryControlBucketsRequested=_RHistoryControlBucketsRequested_Object((1,3,6,1,4,1,8886,6,1,22,2,1,1,3),_RHistoryControlBucketsRequested_Type())
rHistoryControlBucketsRequested.setMaxAccess(_C)
if mibBuilder.loadTexts:rHistoryControlBucketsRequested.setStatus(_A)
class _RHistoryControlBucketsGranted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RHistoryControlBucketsGranted_Type.__name__=_E
_RHistoryControlBucketsGranted_Object=MibTableColumn
rHistoryControlBucketsGranted=_RHistoryControlBucketsGranted_Object((1,3,6,1,4,1,8886,6,1,22,2,1,1,4),_RHistoryControlBucketsGranted_Type())
rHistoryControlBucketsGranted.setMaxAccess(_B)
if mibBuilder.loadTexts:rHistoryControlBucketsGranted.setStatus(_A)
class _RHistoryControlInterval_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_RHistoryControlInterval_Type.__name__=_E
_RHistoryControlInterval_Object=MibTableColumn
rHistoryControlInterval=_RHistoryControlInterval_Object((1,3,6,1,4,1,8886,6,1,22,2,1,1,5),_RHistoryControlInterval_Type())
rHistoryControlInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rHistoryControlInterval.setStatus(_A)
_RHistoryControlOwner_Type=OwnerString
_RHistoryControlOwner_Object=MibTableColumn
rHistoryControlOwner=_RHistoryControlOwner_Object((1,3,6,1,4,1,8886,6,1,22,2,1,1,6),_RHistoryControlOwner_Type())
rHistoryControlOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:rHistoryControlOwner.setStatus(_A)
_RHistoryControlStatus_Type=EntryStatus
_RHistoryControlStatus_Object=MibTableColumn
rHistoryControlStatus=_RHistoryControlStatus_Object((1,3,6,1,4,1,8886,6,1,22,2,1,1,7),_RHistoryControlStatus_Type())
rHistoryControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rHistoryControlStatus.setStatus(_A)
_REtherHistoryTable_Object=MibTable
rEtherHistoryTable=_REtherHistoryTable_Object((1,3,6,1,4,1,8886,6,1,22,2,2))
if mibBuilder.loadTexts:rEtherHistoryTable.setStatus(_A)
_REtherHistoryEntry_Object=MibTableRow
rEtherHistoryEntry=_REtherHistoryEntry_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1))
rEtherHistoryEntry.setIndexNames((0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:rEtherHistoryEntry.setStatus(_A)
class _REtherHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_REtherHistoryIndex_Type.__name__=_E
_REtherHistoryIndex_Object=MibTableColumn
rEtherHistoryIndex=_REtherHistoryIndex_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,1),_REtherHistoryIndex_Type())
rEtherHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryIndex.setStatus(_A)
class _REtherHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_REtherHistorySampleIndex_Type.__name__=_E
_REtherHistorySampleIndex_Object=MibTableColumn
rEtherHistorySampleIndex=_REtherHistorySampleIndex_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,2),_REtherHistorySampleIndex_Type())
rEtherHistorySampleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistorySampleIndex.setStatus(_A)
_REtherHistoryIntervalStart_Type=TimeTicks
_REtherHistoryIntervalStart_Object=MibTableColumn
rEtherHistoryIntervalStart=_REtherHistoryIntervalStart_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,3),_REtherHistoryIntervalStart_Type())
rEtherHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryIntervalStart.setStatus(_A)
_REtherHistoryDropEvents_Type=Counter32
_REtherHistoryDropEvents_Object=MibTableColumn
rEtherHistoryDropEvents=_REtherHistoryDropEvents_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,4),_REtherHistoryDropEvents_Type())
rEtherHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryDropEvents.setStatus(_A)
_REtherHistoryOctets_Type=Counter32
_REtherHistoryOctets_Object=MibTableColumn
rEtherHistoryOctets=_REtherHistoryOctets_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,5),_REtherHistoryOctets_Type())
rEtherHistoryOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryOctets.setStatus(_A)
_REtherHistoryPkts_Type=Counter32
_REtherHistoryPkts_Object=MibTableColumn
rEtherHistoryPkts=_REtherHistoryPkts_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,6),_REtherHistoryPkts_Type())
rEtherHistoryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryPkts.setStatus(_A)
_REtherHistoryBroadcastPkts_Type=Counter32
_REtherHistoryBroadcastPkts_Object=MibTableColumn
rEtherHistoryBroadcastPkts=_REtherHistoryBroadcastPkts_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,7),_REtherHistoryBroadcastPkts_Type())
rEtherHistoryBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryBroadcastPkts.setStatus(_A)
_REtherHistoryMulticastPkts_Type=Counter32
_REtherHistoryMulticastPkts_Object=MibTableColumn
rEtherHistoryMulticastPkts=_REtherHistoryMulticastPkts_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,8),_REtherHistoryMulticastPkts_Type())
rEtherHistoryMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryMulticastPkts.setStatus(_A)
_REtherHistoryCRCAlignErrors_Type=Counter32
_REtherHistoryCRCAlignErrors_Object=MibTableColumn
rEtherHistoryCRCAlignErrors=_REtherHistoryCRCAlignErrors_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,9),_REtherHistoryCRCAlignErrors_Type())
rEtherHistoryCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryCRCAlignErrors.setStatus(_A)
_REtherHistoryUndersizePkts_Type=Counter32
_REtherHistoryUndersizePkts_Object=MibTableColumn
rEtherHistoryUndersizePkts=_REtherHistoryUndersizePkts_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,10),_REtherHistoryUndersizePkts_Type())
rEtherHistoryUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryUndersizePkts.setStatus(_A)
_REtherHistoryOversizePkts_Type=Counter32
_REtherHistoryOversizePkts_Object=MibTableColumn
rEtherHistoryOversizePkts=_REtherHistoryOversizePkts_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,11),_REtherHistoryOversizePkts_Type())
rEtherHistoryOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryOversizePkts.setStatus(_A)
_REtherHistoryFragments_Type=Counter32
_REtherHistoryFragments_Object=MibTableColumn
rEtherHistoryFragments=_REtherHistoryFragments_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,12),_REtherHistoryFragments_Type())
rEtherHistoryFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryFragments.setStatus(_A)
_REtherHistoryJabbers_Type=Counter32
_REtherHistoryJabbers_Object=MibTableColumn
rEtherHistoryJabbers=_REtherHistoryJabbers_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,13),_REtherHistoryJabbers_Type())
rEtherHistoryJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryJabbers.setStatus(_A)
_REtherHistoryCollisions_Type=Counter32
_REtherHistoryCollisions_Object=MibTableColumn
rEtherHistoryCollisions=_REtherHistoryCollisions_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,14),_REtherHistoryCollisions_Type())
rEtherHistoryCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryCollisions.setStatus(_A)
class _REtherHistoryUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_REtherHistoryUtilization_Type.__name__=_E
_REtherHistoryUtilization_Object=MibTableColumn
rEtherHistoryUtilization=_REtherHistoryUtilization_Object((1,3,6,1,4,1,8886,6,1,22,2,2,1,15),_REtherHistoryUtilization_Type())
rEtherHistoryUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:rEtherHistoryUtilization.setStatus(_A)
_RAlarm_ObjectIdentity=ObjectIdentity
rAlarm=_RAlarm_ObjectIdentity((1,3,6,1,4,1,8886,6,1,22,3))
_RAlarmTable_Object=MibTable
rAlarmTable=_RAlarmTable_Object((1,3,6,1,4,1,8886,6,1,22,3,1))
if mibBuilder.loadTexts:rAlarmTable.setStatus(_A)
_RAlarmEntry_Object=MibTableRow
rAlarmEntry=_RAlarmEntry_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1))
rAlarmEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:rAlarmEntry.setStatus(_A)
class _RAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RAlarmIndex_Type.__name__=_E
_RAlarmIndex_Object=MibTableColumn
rAlarmIndex=_RAlarmIndex_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,1),_RAlarmIndex_Type())
rAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rAlarmIndex.setStatus(_A)
_RAlarmInterval_Type=Integer32
_RAlarmInterval_Object=MibTableColumn
rAlarmInterval=_RAlarmInterval_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,2),_RAlarmInterval_Type())
rAlarmInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmInterval.setStatus(_A)
_RAlarmVariable_Type=ObjectIdentifier
_RAlarmVariable_Object=MibTableColumn
rAlarmVariable=_RAlarmVariable_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,3),_RAlarmVariable_Type())
rAlarmVariable.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmVariable.setStatus(_A)
class _RAlarmSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2)))
_RAlarmSampleType_Type.__name__=_E
_RAlarmSampleType_Object=MibTableColumn
rAlarmSampleType=_RAlarmSampleType_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,4),_RAlarmSampleType_Type())
rAlarmSampleType.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmSampleType.setStatus(_A)
_RAlarmValue_Type=Integer32
_RAlarmValue_Object=MibTableColumn
rAlarmValue=_RAlarmValue_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,5),_RAlarmValue_Type())
rAlarmValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rAlarmValue.setStatus(_A)
class _RAlarmStartupAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
_RAlarmStartupAlarm_Type.__name__=_E
_RAlarmStartupAlarm_Object=MibTableColumn
rAlarmStartupAlarm=_RAlarmStartupAlarm_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,6),_RAlarmStartupAlarm_Type())
rAlarmStartupAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmStartupAlarm.setStatus(_A)
_RAlarmRisingThreshold_Type=Integer32
_RAlarmRisingThreshold_Object=MibTableColumn
rAlarmRisingThreshold=_RAlarmRisingThreshold_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,7),_RAlarmRisingThreshold_Type())
rAlarmRisingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmRisingThreshold.setStatus(_A)
_RAlarmFallingThreshold_Type=Integer32
_RAlarmFallingThreshold_Object=MibTableColumn
rAlarmFallingThreshold=_RAlarmFallingThreshold_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,8),_RAlarmFallingThreshold_Type())
rAlarmFallingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmFallingThreshold.setStatus(_A)
class _RAlarmRisingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RAlarmRisingEventIndex_Type.__name__=_E
_RAlarmRisingEventIndex_Object=MibTableColumn
rAlarmRisingEventIndex=_RAlarmRisingEventIndex_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,9),_RAlarmRisingEventIndex_Type())
rAlarmRisingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmRisingEventIndex.setStatus(_A)
class _RAlarmFallingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RAlarmFallingEventIndex_Type.__name__=_E
_RAlarmFallingEventIndex_Object=MibTableColumn
rAlarmFallingEventIndex=_RAlarmFallingEventIndex_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,10),_RAlarmFallingEventIndex_Type())
rAlarmFallingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmFallingEventIndex.setStatus(_A)
_RAlarmOwner_Type=OwnerString
_RAlarmOwner_Object=MibTableColumn
rAlarmOwner=_RAlarmOwner_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,11),_RAlarmOwner_Type())
rAlarmOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmOwner.setStatus(_A)
_RAlarmStatus_Type=EntryStatus
_RAlarmStatus_Object=MibTableColumn
rAlarmStatus=_RAlarmStatus_Object((1,3,6,1,4,1,8886,6,1,22,3,1,1,12),_RAlarmStatus_Type())
rAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rAlarmStatus.setStatus(_A)
_REvent_ObjectIdentity=ObjectIdentity
rEvent=_REvent_ObjectIdentity((1,3,6,1,4,1,8886,6,1,22,9))
_REventTable_Object=MibTable
rEventTable=_REventTable_Object((1,3,6,1,4,1,8886,6,1,22,9,1))
if mibBuilder.loadTexts:rEventTable.setStatus(_A)
_REventEntry_Object=MibTableRow
rEventEntry=_REventEntry_Object((1,3,6,1,4,1,8886,6,1,22,9,1,1))
rEventEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:rEventEntry.setStatus(_A)
class _REventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_REventIndex_Type.__name__=_E
_REventIndex_Object=MibTableColumn
rEventIndex=_REventIndex_Object((1,3,6,1,4,1,8886,6,1,22,9,1,1,1),_REventIndex_Type())
rEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rEventIndex.setStatus(_A)
class _REventDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_REventDescription_Type.__name__=_G
_REventDescription_Object=MibTableColumn
rEventDescription=_REventDescription_Object((1,3,6,1,4,1,8886,6,1,22,9,1,1,2),_REventDescription_Type())
rEventDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rEventDescription.setStatus(_A)
class _REventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('log',2),('snmp-trap',3),('log-and-trap',4)))
_REventType_Type.__name__=_E
_REventType_Object=MibTableColumn
rEventType=_REventType_Object((1,3,6,1,4,1,8886,6,1,22,9,1,1,3),_REventType_Type())
rEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:rEventType.setStatus(_A)
class _REventCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_REventCommunity_Type.__name__=_K
_REventCommunity_Object=MibTableColumn
rEventCommunity=_REventCommunity_Object((1,3,6,1,4,1,8886,6,1,22,9,1,1,4),_REventCommunity_Type())
rEventCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:rEventCommunity.setStatus(_A)
_REventLastTimeSent_Type=TimeTicks
_REventLastTimeSent_Object=MibTableColumn
rEventLastTimeSent=_REventLastTimeSent_Object((1,3,6,1,4,1,8886,6,1,22,9,1,1,5),_REventLastTimeSent_Type())
rEventLastTimeSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rEventLastTimeSent.setStatus(_A)
_REventOwner_Type=OwnerString
_REventOwner_Object=MibTableColumn
rEventOwner=_REventOwner_Object((1,3,6,1,4,1,8886,6,1,22,9,1,1,6),_REventOwner_Type())
rEventOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:rEventOwner.setStatus(_A)
_REventStatus_Type=EntryStatus
_REventStatus_Object=MibTableColumn
rEventStatus=_REventStatus_Object((1,3,6,1,4,1,8886,6,1,22,9,1,1,7),_REventStatus_Type())
rEventStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rEventStatus.setStatus(_A)
_RLogTable_Object=MibTable
rLogTable=_RLogTable_Object((1,3,6,1,4,1,8886,6,1,22,9,2))
if mibBuilder.loadTexts:rLogTable.setStatus(_A)
_RLogEntry_Object=MibTableRow
rLogEntry=_RLogEntry_Object((1,3,6,1,4,1,8886,6,1,22,9,2,1))
rLogEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:rLogEntry.setStatus(_A)
class _RLogEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RLogEventIndex_Type.__name__=_E
_RLogEventIndex_Object=MibTableColumn
rLogEventIndex=_RLogEventIndex_Object((1,3,6,1,4,1,8886,6,1,22,9,2,1,1),_RLogEventIndex_Type())
rLogEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rLogEventIndex.setStatus(_A)
class _RLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RLogIndex_Type.__name__=_E
_RLogIndex_Object=MibTableColumn
rLogIndex=_RLogIndex_Object((1,3,6,1,4,1,8886,6,1,22,9,2,1,2),_RLogIndex_Type())
rLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rLogIndex.setStatus(_A)
_RLogTime_Type=TimeTicks
_RLogTime_Object=MibTableColumn
rLogTime=_RLogTime_Object((1,3,6,1,4,1,8886,6,1,22,9,2,1,3),_RLogTime_Type())
rLogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rLogTime.setStatus(_A)
class _RLogDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RLogDescription_Type.__name__=_G
_RLogDescription_Object=MibTableColumn
rLogDescription=_RLogDescription_Object((1,3,6,1,4,1,8886,6,1,22,9,2,1,4),_RLogDescription_Type())
rLogDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rLogDescription.setStatus(_A)
rRisingAlarm=NotificationType((1,3,6,1,4,1,8886,6,1,22,0,1))
rRisingAlarm.setObjects(*((_D,_F),(_D,_H),(_D,_I),(_D,_J),(_D,_T)))
if mibBuilder.loadTexts:rRisingAlarm.setStatus('')
rFallingAlarm=NotificationType((1,3,6,1,4,1,8886,6,1,22,0,2))
rFallingAlarm.setObjects(*((_D,_F),(_D,_H),(_D,_I),(_D,_J),(_D,_U)))
if mibBuilder.loadTexts:rFallingAlarm.setStatus('')
mibBuilder.exportSymbols(_D,**{'OwnerString':OwnerString,'EntryStatus':EntryStatus,'rmonMib':rmonMib,'rRisingAlarm':rRisingAlarm,'rFallingAlarm':rFallingAlarm,'rStatistics':rStatistics,'rEtherStatsTable':rEtherStatsTable,'rEtherStatsEntry':rEtherStatsEntry,_M:rEtherStatsIndex,'rEtherStatsDataSource':rEtherStatsDataSource,'rEtherStatsDropEvents':rEtherStatsDropEvents,'rEtherStatsOctets':rEtherStatsOctets,'rEtherStatsPkts':rEtherStatsPkts,'rEtherStatsBroadcastPkts':rEtherStatsBroadcastPkts,'rEtherStatsMulticastPkts':rEtherStatsMulticastPkts,'rEtherStatsCRCAlignErrors':rEtherStatsCRCAlignErrors,'rEtherStatsUndersizePkts':rEtherStatsUndersizePkts,'rEtherStatsOversizePkts':rEtherStatsOversizePkts,'rEtherStatsFragments':rEtherStatsFragments,'rEtherStatsJabbers':rEtherStatsJabbers,'rEtherStatsCollisions':rEtherStatsCollisions,'rEtherStatsPkts64Octets':rEtherStatsPkts64Octets,'rEtherStatsPkts65to127Octets':rEtherStatsPkts65to127Octets,'rEtherStatsPkts128to255Octets':rEtherStatsPkts128to255Octets,'rEtherStatsPkts256to511Octets':rEtherStatsPkts256to511Octets,'rEtherStatsPkts512to1023Octets':rEtherStatsPkts512to1023Octets,'rEtherStatsPkts1024to1518Octets':rEtherStatsPkts1024to1518Octets,'rEtherStatsOwner':rEtherStatsOwner,'rEtherStatsStatus':rEtherStatsStatus,'rHistory':rHistory,'rHistoryControlTable':rHistoryControlTable,'rHistoryControlEntry':rHistoryControlEntry,_N:rHistoryControlIndex,'rHistoryControlDataSource':rHistoryControlDataSource,'rHistoryControlBucketsRequested':rHistoryControlBucketsRequested,'rHistoryControlBucketsGranted':rHistoryControlBucketsGranted,'rHistoryControlInterval':rHistoryControlInterval,'rHistoryControlOwner':rHistoryControlOwner,'rHistoryControlStatus':rHistoryControlStatus,'rEtherHistoryTable':rEtherHistoryTable,'rEtherHistoryEntry':rEtherHistoryEntry,_O:rEtherHistoryIndex,_P:rEtherHistorySampleIndex,'rEtherHistoryIntervalStart':rEtherHistoryIntervalStart,'rEtherHistoryDropEvents':rEtherHistoryDropEvents,'rEtherHistoryOctets':rEtherHistoryOctets,'rEtherHistoryPkts':rEtherHistoryPkts,'rEtherHistoryBroadcastPkts':rEtherHistoryBroadcastPkts,'rEtherHistoryMulticastPkts':rEtherHistoryMulticastPkts,'rEtherHistoryCRCAlignErrors':rEtherHistoryCRCAlignErrors,'rEtherHistoryUndersizePkts':rEtherHistoryUndersizePkts,'rEtherHistoryOversizePkts':rEtherHistoryOversizePkts,'rEtherHistoryFragments':rEtherHistoryFragments,'rEtherHistoryJabbers':rEtherHistoryJabbers,'rEtherHistoryCollisions':rEtherHistoryCollisions,'rEtherHistoryUtilization':rEtherHistoryUtilization,'rAlarm':rAlarm,'rAlarmTable':rAlarmTable,'rAlarmEntry':rAlarmEntry,_F:rAlarmIndex,'rAlarmInterval':rAlarmInterval,_H:rAlarmVariable,_I:rAlarmSampleType,_J:rAlarmValue,'rAlarmStartupAlarm':rAlarmStartupAlarm,_T:rAlarmRisingThreshold,_U:rAlarmFallingThreshold,'rAlarmRisingEventIndex':rAlarmRisingEventIndex,'rAlarmFallingEventIndex':rAlarmFallingEventIndex,'rAlarmOwner':rAlarmOwner,'rAlarmStatus':rAlarmStatus,'rEvent':rEvent,'rEventTable':rEventTable,'rEventEntry':rEventEntry,_Q:rEventIndex,'rEventDescription':rEventDescription,'rEventType':rEventType,'rEventCommunity':rEventCommunity,'rEventLastTimeSent':rEventLastTimeSent,'rEventOwner':rEventOwner,'rEventStatus':rEventStatus,'rLogTable':rLogTable,'rLogEntry':rLogEntry,_R:rLogEventIndex,_S:rLogIndex,'rLogTime':rLogTime,'rLogDescription':rLogDescription})