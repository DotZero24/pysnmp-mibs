_K='extEtherHistoryEntry'
_J='pmQueueEtherHistorySampleIndex'
_I='pmQueueEtherHistoryIndex'
_H='pmQueueHistoryControlIndex'
_G='pmQueueStatsIndex'
_F='Unsigned32'
_E='SM-STATS-MIB'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etherHistoryEntry,=mibBuilder.importSymbols('RMON-MIB','etherHistoryEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
smStatMibs=ModuleIdentity((1,3,6,1,4,1,29601,100,1,1))
if mibBuilder.loadTexts:smStatMibs.setRevisions(('2012-09-05 00:00',))
class OwnerString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class EntryStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
_SmStats_ObjectIdentity=ObjectIdentity
smStats=_SmStats_ObjectIdentity((1,3,6,1,4,1,29601,100,1,1,1))
_PmQueueStatsTable_Object=MibTable
pmQueueStatsTable=_PmQueueStatsTable_Object((1,3,6,1,4,1,29601,100,1,1,1,1))
if mibBuilder.loadTexts:pmQueueStatsTable.setStatus(_A)
_PmQueueStatsEntry_Object=MibTableRow
pmQueueStatsEntry=_PmQueueStatsEntry_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1))
pmQueueStatsEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:pmQueueStatsEntry.setStatus(_A)
class _PmQueueStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PmQueueStatsIndex_Type.__name__=_C
_PmQueueStatsIndex_Object=MibTableColumn
pmQueueStatsIndex=_PmQueueStatsIndex_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1,1),_PmQueueStatsIndex_Type())
pmQueueStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueStatsIndex.setStatus(_A)
_PmQueueStatsDataSource_Type=ObjectIdentifier
_PmQueueStatsDataSource_Object=MibTableColumn
pmQueueStatsDataSource=_PmQueueStatsDataSource_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1,2),_PmQueueStatsDataSource_Type())
pmQueueStatsDataSource.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueStatsDataSource.setStatus(_A)
class _PmQueueStatsQueue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PmQueueStatsQueue_Type.__name__=_F
_PmQueueStatsQueue_Object=MibTableColumn
pmQueueStatsQueue=_PmQueueStatsQueue_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1,3),_PmQueueStatsQueue_Type())
pmQueueStatsQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueStatsQueue.setStatus(_A)
_PmQueueStatsTxPkts_Type=Counter64
_PmQueueStatsTxPkts_Object=MibTableColumn
pmQueueStatsTxPkts=_PmQueueStatsTxPkts_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1,4),_PmQueueStatsTxPkts_Type())
pmQueueStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueStatsTxPkts.setStatus(_A)
_PmQueueStatsTxBytes_Type=Counter64
_PmQueueStatsTxBytes_Object=MibTableColumn
pmQueueStatsTxBytes=_PmQueueStatsTxBytes_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1,5),_PmQueueStatsTxBytes_Type())
pmQueueStatsTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueStatsTxBytes.setStatus(_A)
_PmQueueStatsTxDiscardPkts_Type=Counter64
_PmQueueStatsTxDiscardPkts_Object=MibTableColumn
pmQueueStatsTxDiscardPkts=_PmQueueStatsTxDiscardPkts_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1,6),_PmQueueStatsTxDiscardPkts_Type())
pmQueueStatsTxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueStatsTxDiscardPkts.setStatus(_A)
_PmQueueStatsTxDiscardBytes_Type=Counter64
_PmQueueStatsTxDiscardBytes_Object=MibTableColumn
pmQueueStatsTxDiscardBytes=_PmQueueStatsTxDiscardBytes_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1,7),_PmQueueStatsTxDiscardBytes_Type())
pmQueueStatsTxDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueStatsTxDiscardBytes.setStatus(_A)
_PmQueueStatsOwner_Type=OwnerString
_PmQueueStatsOwner_Object=MibTableColumn
pmQueueStatsOwner=_PmQueueStatsOwner_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1,8),_PmQueueStatsOwner_Type())
pmQueueStatsOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueStatsOwner.setStatus(_A)
_PmQueueStatsStatus_Type=EntryStatus
_PmQueueStatsStatus_Object=MibTableColumn
pmQueueStatsStatus=_PmQueueStatsStatus_Object((1,3,6,1,4,1,29601,100,1,1,1,1,1,9),_PmQueueStatsStatus_Type())
pmQueueStatsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueStatsStatus.setStatus(_A)
_PmQueueHistoryControlTable_Object=MibTable
pmQueueHistoryControlTable=_PmQueueHistoryControlTable_Object((1,3,6,1,4,1,29601,100,1,1,1,2))
if mibBuilder.loadTexts:pmQueueHistoryControlTable.setStatus(_A)
_PmQueueHistoryControlEntry_Object=MibTableRow
pmQueueHistoryControlEntry=_PmQueueHistoryControlEntry_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1))
pmQueueHistoryControlEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:pmQueueHistoryControlEntry.setStatus(_A)
class _PmQueueHistoryControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PmQueueHistoryControlIndex_Type.__name__=_C
_PmQueueHistoryControlIndex_Object=MibTableColumn
pmQueueHistoryControlIndex=_PmQueueHistoryControlIndex_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1,1),_PmQueueHistoryControlIndex_Type())
pmQueueHistoryControlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueHistoryControlIndex.setStatus(_A)
_PmQueueHistoryControlQueue_Type=Unsigned32
_PmQueueHistoryControlQueue_Object=MibTableColumn
pmQueueHistoryControlQueue=_PmQueueHistoryControlQueue_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1,2),_PmQueueHistoryControlQueue_Type())
pmQueueHistoryControlQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueHistoryControlQueue.setStatus(_A)
_PmQueueHistoryControlDataSource_Type=ObjectIdentifier
_PmQueueHistoryControlDataSource_Object=MibTableColumn
pmQueueHistoryControlDataSource=_PmQueueHistoryControlDataSource_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1,3),_PmQueueHistoryControlDataSource_Type())
pmQueueHistoryControlDataSource.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueHistoryControlDataSource.setStatus(_A)
class _PmQueueHistoryControlBucketsRequested_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PmQueueHistoryControlBucketsRequested_Type.__name__=_C
_PmQueueHistoryControlBucketsRequested_Object=MibTableColumn
pmQueueHistoryControlBucketsRequested=_PmQueueHistoryControlBucketsRequested_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1,4),_PmQueueHistoryControlBucketsRequested_Type())
pmQueueHistoryControlBucketsRequested.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueHistoryControlBucketsRequested.setStatus(_A)
class _PmQueueHistoryControlBucketsGranted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PmQueueHistoryControlBucketsGranted_Type.__name__=_C
_PmQueueHistoryControlBucketsGranted_Object=MibTableColumn
pmQueueHistoryControlBucketsGranted=_PmQueueHistoryControlBucketsGranted_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1,5),_PmQueueHistoryControlBucketsGranted_Type())
pmQueueHistoryControlBucketsGranted.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueHistoryControlBucketsGranted.setStatus(_A)
class _PmQueueHistoryControlInterval_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_PmQueueHistoryControlInterval_Type.__name__=_C
_PmQueueHistoryControlInterval_Object=MibTableColumn
pmQueueHistoryControlInterval=_PmQueueHistoryControlInterval_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1,6),_PmQueueHistoryControlInterval_Type())
pmQueueHistoryControlInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueHistoryControlInterval.setStatus(_A)
if mibBuilder.loadTexts:pmQueueHistoryControlInterval.setUnits('Seconds')
_PmQueueHistoryControlOwner_Type=OwnerString
_PmQueueHistoryControlOwner_Object=MibTableColumn
pmQueueHistoryControlOwner=_PmQueueHistoryControlOwner_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1,7),_PmQueueHistoryControlOwner_Type())
pmQueueHistoryControlOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueHistoryControlOwner.setStatus(_A)
class _PmQueueHistoryControlPersistence_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('disable',0),('enable',2)))
_PmQueueHistoryControlPersistence_Type.__name__=_C
_PmQueueHistoryControlPersistence_Object=MibTableColumn
pmQueueHistoryControlPersistence=_PmQueueHistoryControlPersistence_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1,8),_PmQueueHistoryControlPersistence_Type())
pmQueueHistoryControlPersistence.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueHistoryControlPersistence.setStatus(_A)
_PmQueueHistoryControlStatus_Type=EntryStatus
_PmQueueHistoryControlStatus_Object=MibTableColumn
pmQueueHistoryControlStatus=_PmQueueHistoryControlStatus_Object((1,3,6,1,4,1,29601,100,1,1,1,2,1,9),_PmQueueHistoryControlStatus_Type())
pmQueueHistoryControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pmQueueHistoryControlStatus.setStatus(_A)
_PmQueueEtherHistoryTable_Object=MibTable
pmQueueEtherHistoryTable=_PmQueueEtherHistoryTable_Object((1,3,6,1,4,1,29601,100,1,1,1,3))
if mibBuilder.loadTexts:pmQueueEtherHistoryTable.setStatus(_A)
_PmQueueEtherHistoryEntry_Object=MibTableRow
pmQueueEtherHistoryEntry=_PmQueueEtherHistoryEntry_Object((1,3,6,1,4,1,29601,100,1,1,1,3,1))
pmQueueEtherHistoryEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:pmQueueEtherHistoryEntry.setStatus(_A)
class _PmQueueEtherHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PmQueueEtherHistoryIndex_Type.__name__=_C
_PmQueueEtherHistoryIndex_Object=MibTableColumn
pmQueueEtherHistoryIndex=_PmQueueEtherHistoryIndex_Object((1,3,6,1,4,1,29601,100,1,1,1,3,1,1),_PmQueueEtherHistoryIndex_Type())
pmQueueEtherHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueEtherHistoryIndex.setStatus(_A)
class _PmQueueEtherHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PmQueueEtherHistorySampleIndex_Type.__name__=_C
_PmQueueEtherHistorySampleIndex_Object=MibTableColumn
pmQueueEtherHistorySampleIndex=_PmQueueEtherHistorySampleIndex_Object((1,3,6,1,4,1,29601,100,1,1,1,3,1,2),_PmQueueEtherHistorySampleIndex_Type())
pmQueueEtherHistorySampleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueEtherHistorySampleIndex.setStatus(_A)
_PmQueueEtherHistoryIntervalStart_Type=TimeTicks
_PmQueueEtherHistoryIntervalStart_Object=MibTableColumn
pmQueueEtherHistoryIntervalStart=_PmQueueEtherHistoryIntervalStart_Object((1,3,6,1,4,1,29601,100,1,1,1,3,1,3),_PmQueueEtherHistoryIntervalStart_Type())
pmQueueEtherHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueEtherHistoryIntervalStart.setStatus(_A)
_PmQueueHistoryTxPkts_Type=Counter64
_PmQueueHistoryTxPkts_Object=MibTableColumn
pmQueueHistoryTxPkts=_PmQueueHistoryTxPkts_Object((1,3,6,1,4,1,29601,100,1,1,1,3,1,4),_PmQueueHistoryTxPkts_Type())
pmQueueHistoryTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueHistoryTxPkts.setStatus(_A)
_PmQueueHistoryTxBytes_Type=Counter64
_PmQueueHistoryTxBytes_Object=MibTableColumn
pmQueueHistoryTxBytes=_PmQueueHistoryTxBytes_Object((1,3,6,1,4,1,29601,100,1,1,1,3,1,5),_PmQueueHistoryTxBytes_Type())
pmQueueHistoryTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueHistoryTxBytes.setStatus(_A)
_PmQueueHistoryTxDiscardPkts_Type=Counter64
_PmQueueHistoryTxDiscardPkts_Object=MibTableColumn
pmQueueHistoryTxDiscardPkts=_PmQueueHistoryTxDiscardPkts_Object((1,3,6,1,4,1,29601,100,1,1,1,3,1,6),_PmQueueHistoryTxDiscardPkts_Type())
pmQueueHistoryTxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueHistoryTxDiscardPkts.setStatus(_A)
_PmQueueHistoryTxDiscardBytes_Type=Counter64
_PmQueueHistoryTxDiscardBytes_Object=MibTableColumn
pmQueueHistoryTxDiscardBytes=_PmQueueHistoryTxDiscardBytes_Object((1,3,6,1,4,1,29601,100,1,1,1,3,1,7),_PmQueueHistoryTxDiscardBytes_Type())
pmQueueHistoryTxDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:pmQueueHistoryTxDiscardBytes.setStatus(_A)
_SmExtHistory_ObjectIdentity=ObjectIdentity
smExtHistory=_SmExtHistory_ObjectIdentity((1,3,6,1,4,1,29601,100,1,1,2))
_ExtEtherHistoryTable_Object=MibTable
extEtherHistoryTable=_ExtEtherHistoryTable_Object((1,3,6,1,4,1,29601,100,1,1,2,1))
if mibBuilder.loadTexts:extEtherHistoryTable.setStatus(_A)
_ExtEtherHistoryEntry_Object=MibTableRow
extEtherHistoryEntry=_ExtEtherHistoryEntry_Object((1,3,6,1,4,1,29601,100,1,1,2,1,1))
if mibBuilder.loadTexts:extEtherHistoryEntry.setStatus(_A)
class _EtherHistoryMinUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EtherHistoryMinUtilization_Type.__name__=_C
_EtherHistoryMinUtilization_Object=MibTableColumn
etherHistoryMinUtilization=_EtherHistoryMinUtilization_Object((1,3,6,1,4,1,29601,100,1,1,2,1,1,1),_EtherHistoryMinUtilization_Type())
etherHistoryMinUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:etherHistoryMinUtilization.setStatus(_A)
class _EtherHistoryMaxUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EtherHistoryMaxUtilization_Type.__name__=_C
_EtherHistoryMaxUtilization_Object=MibTableColumn
etherHistoryMaxUtilization=_EtherHistoryMaxUtilization_Object((1,3,6,1,4,1,29601,100,1,1,2,1,1,2),_EtherHistoryMaxUtilization_Type())
etherHistoryMaxUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:etherHistoryMaxUtilization.setStatus(_A)
class _EtherHistoryTxMinUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EtherHistoryTxMinUtilization_Type.__name__=_C
_EtherHistoryTxMinUtilization_Object=MibTableColumn
etherHistoryTxMinUtilization=_EtherHistoryTxMinUtilization_Object((1,3,6,1,4,1,29601,100,1,1,2,1,1,3),_EtherHistoryTxMinUtilization_Type())
etherHistoryTxMinUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:etherHistoryTxMinUtilization.setStatus(_A)
class _EtherHistoryTxMaxUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EtherHistoryTxMaxUtilization_Type.__name__=_C
_EtherHistoryTxMaxUtilization_Object=MibTableColumn
etherHistoryTxMaxUtilization=_EtherHistoryTxMaxUtilization_Object((1,3,6,1,4,1,29601,100,1,1,2,1,1,4),_EtherHistoryTxMaxUtilization_Type())
etherHistoryTxMaxUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:etherHistoryTxMaxUtilization.setStatus(_A)
etherHistoryEntry.registerAugmentions((_E,_K))
extEtherHistoryEntry.setIndexNames(*etherHistoryEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'OwnerString':OwnerString,'EntryStatus':EntryStatus,'smStatMibs':smStatMibs,'smStats':smStats,'pmQueueStatsTable':pmQueueStatsTable,'pmQueueStatsEntry':pmQueueStatsEntry,_G:pmQueueStatsIndex,'pmQueueStatsDataSource':pmQueueStatsDataSource,'pmQueueStatsQueue':pmQueueStatsQueue,'pmQueueStatsTxPkts':pmQueueStatsTxPkts,'pmQueueStatsTxBytes':pmQueueStatsTxBytes,'pmQueueStatsTxDiscardPkts':pmQueueStatsTxDiscardPkts,'pmQueueStatsTxDiscardBytes':pmQueueStatsTxDiscardBytes,'pmQueueStatsOwner':pmQueueStatsOwner,'pmQueueStatsStatus':pmQueueStatsStatus,'pmQueueHistoryControlTable':pmQueueHistoryControlTable,'pmQueueHistoryControlEntry':pmQueueHistoryControlEntry,_H:pmQueueHistoryControlIndex,'pmQueueHistoryControlQueue':pmQueueHistoryControlQueue,'pmQueueHistoryControlDataSource':pmQueueHistoryControlDataSource,'pmQueueHistoryControlBucketsRequested':pmQueueHistoryControlBucketsRequested,'pmQueueHistoryControlBucketsGranted':pmQueueHistoryControlBucketsGranted,'pmQueueHistoryControlInterval':pmQueueHistoryControlInterval,'pmQueueHistoryControlOwner':pmQueueHistoryControlOwner,'pmQueueHistoryControlPersistence':pmQueueHistoryControlPersistence,'pmQueueHistoryControlStatus':pmQueueHistoryControlStatus,'pmQueueEtherHistoryTable':pmQueueEtherHistoryTable,'pmQueueEtherHistoryEntry':pmQueueEtherHistoryEntry,_I:pmQueueEtherHistoryIndex,_J:pmQueueEtherHistorySampleIndex,'pmQueueEtherHistoryIntervalStart':pmQueueEtherHistoryIntervalStart,'pmQueueHistoryTxPkts':pmQueueHistoryTxPkts,'pmQueueHistoryTxBytes':pmQueueHistoryTxBytes,'pmQueueHistoryTxDiscardPkts':pmQueueHistoryTxDiscardPkts,'pmQueueHistoryTxDiscardBytes':pmQueueHistoryTxDiscardBytes,'smExtHistory':smExtHistory,'extEtherHistoryTable':extEtherHistoryTable,_K:extEtherHistoryEntry,'etherHistoryMinUtilization':etherHistoryMinUtilization,'etherHistoryMaxUtilization':etherHistoryMaxUtilization,'etherHistoryTxMinUtilization':etherHistoryTxMinUtilization,'etherHistoryTxMaxUtilization':etherHistoryTxMaxUtilization})