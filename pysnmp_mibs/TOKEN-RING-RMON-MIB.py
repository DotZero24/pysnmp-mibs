_W='sourceRoutingStatsIfIndex'
_V='ringStationConfigMacAddress'
_U='ringStationConfigIfIndex'
_T='stable'
_S='ringStationConfigControlMacAddress'
_R='ringStationConfigControlIfIndex'
_Q='ringStationOrderOrderIndex'
_P='ringStationOrderIfIndex'
_O='ringStationMacAddress'
_N='ringStationIfIndex'
_M='ringStationControlIfIndex'
_L='tokenRingPHistorySampleIndex'
_K='tokenRingPHistoryIndex'
_J='tokenRingMLHistorySampleIndex'
_I='tokenRingMLHistoryIndex'
_H='tokenRingPStatsIndex'
_G='tokenRingMLStatsIndex'
_F='OctetString'
_E='Integer32'
_D='read-write'
_C='TOKEN-RING-RMON-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EntryStatus,OwnerString,history,rmon,statistics=mibBuilder.importSymbols('RFC1271-MIB','EntryStatus','OwnerString','history','rmon','statistics')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class TimeInterval(Integer32):0
_TokenRingMLStatsTable_Object=MibTable
tokenRingMLStatsTable=_TokenRingMLStatsTable_Object((1,3,6,1,2,1,16,1,2))
if mibBuilder.loadTexts:tokenRingMLStatsTable.setStatus(_A)
_TokenRingMLStatsEntry_Object=MibTableRow
tokenRingMLStatsEntry=_TokenRingMLStatsEntry_Object((1,3,6,1,2,1,16,1,2,1))
tokenRingMLStatsEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:tokenRingMLStatsEntry.setStatus(_A)
class _TokenRingMLStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TokenRingMLStatsIndex_Type.__name__=_E
_TokenRingMLStatsIndex_Object=MibTableColumn
tokenRingMLStatsIndex=_TokenRingMLStatsIndex_Object((1,3,6,1,2,1,16,1,2,1,1),_TokenRingMLStatsIndex_Type())
tokenRingMLStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsIndex.setStatus(_A)
_TokenRingMLStatsDataSource_Type=ObjectIdentifier
_TokenRingMLStatsDataSource_Object=MibTableColumn
tokenRingMLStatsDataSource=_TokenRingMLStatsDataSource_Object((1,3,6,1,2,1,16,1,2,1,2),_TokenRingMLStatsDataSource_Type())
tokenRingMLStatsDataSource.setMaxAccess(_D)
if mibBuilder.loadTexts:tokenRingMLStatsDataSource.setStatus(_A)
_TokenRingMLStatsDropEvents_Type=Counter32
_TokenRingMLStatsDropEvents_Object=MibTableColumn
tokenRingMLStatsDropEvents=_TokenRingMLStatsDropEvents_Object((1,3,6,1,2,1,16,1,2,1,3),_TokenRingMLStatsDropEvents_Type())
tokenRingMLStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsDropEvents.setStatus(_A)
_TokenRingMLStatsMacOctets_Type=Counter32
_TokenRingMLStatsMacOctets_Object=MibTableColumn
tokenRingMLStatsMacOctets=_TokenRingMLStatsMacOctets_Object((1,3,6,1,2,1,16,1,2,1,4),_TokenRingMLStatsMacOctets_Type())
tokenRingMLStatsMacOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsMacOctets.setStatus(_A)
_TokenRingMLStatsMacPkts_Type=Counter32
_TokenRingMLStatsMacPkts_Object=MibTableColumn
tokenRingMLStatsMacPkts=_TokenRingMLStatsMacPkts_Object((1,3,6,1,2,1,16,1,2,1,5),_TokenRingMLStatsMacPkts_Type())
tokenRingMLStatsMacPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsMacPkts.setStatus(_A)
_TokenRingMLStatsRingPurgeEvents_Type=Counter32
_TokenRingMLStatsRingPurgeEvents_Object=MibTableColumn
tokenRingMLStatsRingPurgeEvents=_TokenRingMLStatsRingPurgeEvents_Object((1,3,6,1,2,1,16,1,2,1,6),_TokenRingMLStatsRingPurgeEvents_Type())
tokenRingMLStatsRingPurgeEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsRingPurgeEvents.setStatus(_A)
_TokenRingMLStatsRingPurgePkts_Type=Counter32
_TokenRingMLStatsRingPurgePkts_Object=MibTableColumn
tokenRingMLStatsRingPurgePkts=_TokenRingMLStatsRingPurgePkts_Object((1,3,6,1,2,1,16,1,2,1,7),_TokenRingMLStatsRingPurgePkts_Type())
tokenRingMLStatsRingPurgePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsRingPurgePkts.setStatus(_A)
_TokenRingMLStatsBeaconEvents_Type=Counter32
_TokenRingMLStatsBeaconEvents_Object=MibTableColumn
tokenRingMLStatsBeaconEvents=_TokenRingMLStatsBeaconEvents_Object((1,3,6,1,2,1,16,1,2,1,8),_TokenRingMLStatsBeaconEvents_Type())
tokenRingMLStatsBeaconEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsBeaconEvents.setStatus(_A)
_TokenRingMLStatsBeaconTime_Type=TimeInterval
_TokenRingMLStatsBeaconTime_Object=MibTableColumn
tokenRingMLStatsBeaconTime=_TokenRingMLStatsBeaconTime_Object((1,3,6,1,2,1,16,1,2,1,9),_TokenRingMLStatsBeaconTime_Type())
tokenRingMLStatsBeaconTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsBeaconTime.setStatus(_A)
_TokenRingMLStatsBeaconPkts_Type=Counter32
_TokenRingMLStatsBeaconPkts_Object=MibTableColumn
tokenRingMLStatsBeaconPkts=_TokenRingMLStatsBeaconPkts_Object((1,3,6,1,2,1,16,1,2,1,10),_TokenRingMLStatsBeaconPkts_Type())
tokenRingMLStatsBeaconPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsBeaconPkts.setStatus(_A)
_TokenRingMLStatsClaimTokenEvents_Type=Counter32
_TokenRingMLStatsClaimTokenEvents_Object=MibTableColumn
tokenRingMLStatsClaimTokenEvents=_TokenRingMLStatsClaimTokenEvents_Object((1,3,6,1,2,1,16,1,2,1,11),_TokenRingMLStatsClaimTokenEvents_Type())
tokenRingMLStatsClaimTokenEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsClaimTokenEvents.setStatus(_A)
_TokenRingMLStatsClaimTokenPkts_Type=Counter32
_TokenRingMLStatsClaimTokenPkts_Object=MibTableColumn
tokenRingMLStatsClaimTokenPkts=_TokenRingMLStatsClaimTokenPkts_Object((1,3,6,1,2,1,16,1,2,1,12),_TokenRingMLStatsClaimTokenPkts_Type())
tokenRingMLStatsClaimTokenPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsClaimTokenPkts.setStatus(_A)
_TokenRingMLStatsNAUNChanges_Type=Counter32
_TokenRingMLStatsNAUNChanges_Object=MibTableColumn
tokenRingMLStatsNAUNChanges=_TokenRingMLStatsNAUNChanges_Object((1,3,6,1,2,1,16,1,2,1,13),_TokenRingMLStatsNAUNChanges_Type())
tokenRingMLStatsNAUNChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsNAUNChanges.setStatus(_A)
_TokenRingMLStatsLineErrors_Type=Counter32
_TokenRingMLStatsLineErrors_Object=MibTableColumn
tokenRingMLStatsLineErrors=_TokenRingMLStatsLineErrors_Object((1,3,6,1,2,1,16,1,2,1,14),_TokenRingMLStatsLineErrors_Type())
tokenRingMLStatsLineErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsLineErrors.setStatus(_A)
_TokenRingMLStatsInternalErrors_Type=Counter32
_TokenRingMLStatsInternalErrors_Object=MibTableColumn
tokenRingMLStatsInternalErrors=_TokenRingMLStatsInternalErrors_Object((1,3,6,1,2,1,16,1,2,1,15),_TokenRingMLStatsInternalErrors_Type())
tokenRingMLStatsInternalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsInternalErrors.setStatus(_A)
_TokenRingMLStatsBurstErrors_Type=Counter32
_TokenRingMLStatsBurstErrors_Object=MibTableColumn
tokenRingMLStatsBurstErrors=_TokenRingMLStatsBurstErrors_Object((1,3,6,1,2,1,16,1,2,1,16),_TokenRingMLStatsBurstErrors_Type())
tokenRingMLStatsBurstErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsBurstErrors.setStatus(_A)
_TokenRingMLStatsACErrors_Type=Counter32
_TokenRingMLStatsACErrors_Object=MibTableColumn
tokenRingMLStatsACErrors=_TokenRingMLStatsACErrors_Object((1,3,6,1,2,1,16,1,2,1,17),_TokenRingMLStatsACErrors_Type())
tokenRingMLStatsACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsACErrors.setStatus(_A)
_TokenRingMLStatsAbortErrors_Type=Counter32
_TokenRingMLStatsAbortErrors_Object=MibTableColumn
tokenRingMLStatsAbortErrors=_TokenRingMLStatsAbortErrors_Object((1,3,6,1,2,1,16,1,2,1,18),_TokenRingMLStatsAbortErrors_Type())
tokenRingMLStatsAbortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsAbortErrors.setStatus(_A)
_TokenRingMLStatsLostFrameErrors_Type=Counter32
_TokenRingMLStatsLostFrameErrors_Object=MibTableColumn
tokenRingMLStatsLostFrameErrors=_TokenRingMLStatsLostFrameErrors_Object((1,3,6,1,2,1,16,1,2,1,19),_TokenRingMLStatsLostFrameErrors_Type())
tokenRingMLStatsLostFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsLostFrameErrors.setStatus(_A)
_TokenRingMLStatsCongestionErrors_Type=Counter32
_TokenRingMLStatsCongestionErrors_Object=MibTableColumn
tokenRingMLStatsCongestionErrors=_TokenRingMLStatsCongestionErrors_Object((1,3,6,1,2,1,16,1,2,1,20),_TokenRingMLStatsCongestionErrors_Type())
tokenRingMLStatsCongestionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsCongestionErrors.setStatus(_A)
_TokenRingMLStatsFrameCopiedErrors_Type=Counter32
_TokenRingMLStatsFrameCopiedErrors_Object=MibTableColumn
tokenRingMLStatsFrameCopiedErrors=_TokenRingMLStatsFrameCopiedErrors_Object((1,3,6,1,2,1,16,1,2,1,21),_TokenRingMLStatsFrameCopiedErrors_Type())
tokenRingMLStatsFrameCopiedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsFrameCopiedErrors.setStatus(_A)
_TokenRingMLStatsFrequencyErrors_Type=Counter32
_TokenRingMLStatsFrequencyErrors_Object=MibTableColumn
tokenRingMLStatsFrequencyErrors=_TokenRingMLStatsFrequencyErrors_Object((1,3,6,1,2,1,16,1,2,1,22),_TokenRingMLStatsFrequencyErrors_Type())
tokenRingMLStatsFrequencyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsFrequencyErrors.setStatus(_A)
_TokenRingMLStatsTokenErrors_Type=Counter32
_TokenRingMLStatsTokenErrors_Object=MibTableColumn
tokenRingMLStatsTokenErrors=_TokenRingMLStatsTokenErrors_Object((1,3,6,1,2,1,16,1,2,1,23),_TokenRingMLStatsTokenErrors_Type())
tokenRingMLStatsTokenErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsTokenErrors.setStatus(_A)
_TokenRingMLStatsSoftErrorReports_Type=Counter32
_TokenRingMLStatsSoftErrorReports_Object=MibTableColumn
tokenRingMLStatsSoftErrorReports=_TokenRingMLStatsSoftErrorReports_Object((1,3,6,1,2,1,16,1,2,1,24),_TokenRingMLStatsSoftErrorReports_Type())
tokenRingMLStatsSoftErrorReports.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsSoftErrorReports.setStatus(_A)
_TokenRingMLStatsRingPollEvents_Type=Counter32
_TokenRingMLStatsRingPollEvents_Object=MibTableColumn
tokenRingMLStatsRingPollEvents=_TokenRingMLStatsRingPollEvents_Object((1,3,6,1,2,1,16,1,2,1,25),_TokenRingMLStatsRingPollEvents_Type())
tokenRingMLStatsRingPollEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLStatsRingPollEvents.setStatus(_A)
_TokenRingMLStatsOwner_Type=OwnerString
_TokenRingMLStatsOwner_Object=MibTableColumn
tokenRingMLStatsOwner=_TokenRingMLStatsOwner_Object((1,3,6,1,2,1,16,1,2,1,26),_TokenRingMLStatsOwner_Type())
tokenRingMLStatsOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:tokenRingMLStatsOwner.setStatus(_A)
_TokenRingMLStatsStatus_Type=EntryStatus
_TokenRingMLStatsStatus_Object=MibTableColumn
tokenRingMLStatsStatus=_TokenRingMLStatsStatus_Object((1,3,6,1,2,1,16,1,2,1,27),_TokenRingMLStatsStatus_Type())
tokenRingMLStatsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tokenRingMLStatsStatus.setStatus(_A)
_TokenRingPStatsTable_Object=MibTable
tokenRingPStatsTable=_TokenRingPStatsTable_Object((1,3,6,1,2,1,16,1,3))
if mibBuilder.loadTexts:tokenRingPStatsTable.setStatus(_A)
_TokenRingPStatsEntry_Object=MibTableRow
tokenRingPStatsEntry=_TokenRingPStatsEntry_Object((1,3,6,1,2,1,16,1,3,1))
tokenRingPStatsEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:tokenRingPStatsEntry.setStatus(_A)
class _TokenRingPStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TokenRingPStatsIndex_Type.__name__=_E
_TokenRingPStatsIndex_Object=MibTableColumn
tokenRingPStatsIndex=_TokenRingPStatsIndex_Object((1,3,6,1,2,1,16,1,3,1,1),_TokenRingPStatsIndex_Type())
tokenRingPStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsIndex.setStatus(_A)
_TokenRingPStatsDataSource_Type=ObjectIdentifier
_TokenRingPStatsDataSource_Object=MibTableColumn
tokenRingPStatsDataSource=_TokenRingPStatsDataSource_Object((1,3,6,1,2,1,16,1,3,1,2),_TokenRingPStatsDataSource_Type())
tokenRingPStatsDataSource.setMaxAccess(_D)
if mibBuilder.loadTexts:tokenRingPStatsDataSource.setStatus(_A)
_TokenRingPStatsDropEvents_Type=Counter32
_TokenRingPStatsDropEvents_Object=MibTableColumn
tokenRingPStatsDropEvents=_TokenRingPStatsDropEvents_Object((1,3,6,1,2,1,16,1,3,1,3),_TokenRingPStatsDropEvents_Type())
tokenRingPStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDropEvents.setStatus(_A)
_TokenRingPStatsDataOctets_Type=Counter32
_TokenRingPStatsDataOctets_Object=MibTableColumn
tokenRingPStatsDataOctets=_TokenRingPStatsDataOctets_Object((1,3,6,1,2,1,16,1,3,1,4),_TokenRingPStatsDataOctets_Type())
tokenRingPStatsDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataOctets.setStatus(_A)
_TokenRingPStatsDataPkts_Type=Counter32
_TokenRingPStatsDataPkts_Object=MibTableColumn
tokenRingPStatsDataPkts=_TokenRingPStatsDataPkts_Object((1,3,6,1,2,1,16,1,3,1,5),_TokenRingPStatsDataPkts_Type())
tokenRingPStatsDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts.setStatus(_A)
_TokenRingPStatsDataBroadcastPkts_Type=Counter32
_TokenRingPStatsDataBroadcastPkts_Object=MibTableColumn
tokenRingPStatsDataBroadcastPkts=_TokenRingPStatsDataBroadcastPkts_Object((1,3,6,1,2,1,16,1,3,1,6),_TokenRingPStatsDataBroadcastPkts_Type())
tokenRingPStatsDataBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataBroadcastPkts.setStatus(_A)
_TokenRingPStatsDataMulticastPkts_Type=Counter32
_TokenRingPStatsDataMulticastPkts_Object=MibTableColumn
tokenRingPStatsDataMulticastPkts=_TokenRingPStatsDataMulticastPkts_Object((1,3,6,1,2,1,16,1,3,1,7),_TokenRingPStatsDataMulticastPkts_Type())
tokenRingPStatsDataMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataMulticastPkts.setStatus(_A)
_TokenRingPStatsDataPkts18to63Octets_Type=Counter32
_TokenRingPStatsDataPkts18to63Octets_Object=MibTableColumn
tokenRingPStatsDataPkts18to63Octets=_TokenRingPStatsDataPkts18to63Octets_Object((1,3,6,1,2,1,16,1,3,1,8),_TokenRingPStatsDataPkts18to63Octets_Type())
tokenRingPStatsDataPkts18to63Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts18to63Octets.setStatus(_A)
_TokenRingPStatsDataPkts64to127Octets_Type=Counter32
_TokenRingPStatsDataPkts64to127Octets_Object=MibTableColumn
tokenRingPStatsDataPkts64to127Octets=_TokenRingPStatsDataPkts64to127Octets_Object((1,3,6,1,2,1,16,1,3,1,9),_TokenRingPStatsDataPkts64to127Octets_Type())
tokenRingPStatsDataPkts64to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts64to127Octets.setStatus(_A)
_TokenRingPStatsDataPkts128to255Octets_Type=Counter32
_TokenRingPStatsDataPkts128to255Octets_Object=MibTableColumn
tokenRingPStatsDataPkts128to255Octets=_TokenRingPStatsDataPkts128to255Octets_Object((1,3,6,1,2,1,16,1,3,1,10),_TokenRingPStatsDataPkts128to255Octets_Type())
tokenRingPStatsDataPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts128to255Octets.setStatus(_A)
_TokenRingPStatsDataPkts256to511Octets_Type=Counter32
_TokenRingPStatsDataPkts256to511Octets_Object=MibTableColumn
tokenRingPStatsDataPkts256to511Octets=_TokenRingPStatsDataPkts256to511Octets_Object((1,3,6,1,2,1,16,1,3,1,11),_TokenRingPStatsDataPkts256to511Octets_Type())
tokenRingPStatsDataPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts256to511Octets.setStatus(_A)
_TokenRingPStatsDataPkts512to1023Octets_Type=Counter32
_TokenRingPStatsDataPkts512to1023Octets_Object=MibTableColumn
tokenRingPStatsDataPkts512to1023Octets=_TokenRingPStatsDataPkts512to1023Octets_Object((1,3,6,1,2,1,16,1,3,1,12),_TokenRingPStatsDataPkts512to1023Octets_Type())
tokenRingPStatsDataPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts512to1023Octets.setStatus(_A)
_TokenRingPStatsDataPkts1024to2047Octets_Type=Counter32
_TokenRingPStatsDataPkts1024to2047Octets_Object=MibTableColumn
tokenRingPStatsDataPkts1024to2047Octets=_TokenRingPStatsDataPkts1024to2047Octets_Object((1,3,6,1,2,1,16,1,3,1,13),_TokenRingPStatsDataPkts1024to2047Octets_Type())
tokenRingPStatsDataPkts1024to2047Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts1024to2047Octets.setStatus(_A)
_TokenRingPStatsDataPkts2048to4095Octets_Type=Counter32
_TokenRingPStatsDataPkts2048to4095Octets_Object=MibTableColumn
tokenRingPStatsDataPkts2048to4095Octets=_TokenRingPStatsDataPkts2048to4095Octets_Object((1,3,6,1,2,1,16,1,3,1,14),_TokenRingPStatsDataPkts2048to4095Octets_Type())
tokenRingPStatsDataPkts2048to4095Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts2048to4095Octets.setStatus(_A)
_TokenRingPStatsDataPkts4096to8191Octets_Type=Counter32
_TokenRingPStatsDataPkts4096to8191Octets_Object=MibTableColumn
tokenRingPStatsDataPkts4096to8191Octets=_TokenRingPStatsDataPkts4096to8191Octets_Object((1,3,6,1,2,1,16,1,3,1,15),_TokenRingPStatsDataPkts4096to8191Octets_Type())
tokenRingPStatsDataPkts4096to8191Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts4096to8191Octets.setStatus(_A)
_TokenRingPStatsDataPkts8192to18000Octets_Type=Counter32
_TokenRingPStatsDataPkts8192to18000Octets_Object=MibTableColumn
tokenRingPStatsDataPkts8192to18000Octets=_TokenRingPStatsDataPkts8192to18000Octets_Object((1,3,6,1,2,1,16,1,3,1,16),_TokenRingPStatsDataPkts8192to18000Octets_Type())
tokenRingPStatsDataPkts8192to18000Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPkts8192to18000Octets.setStatus(_A)
_TokenRingPStatsDataPktsGreaterThan18000Octets_Type=Counter32
_TokenRingPStatsDataPktsGreaterThan18000Octets_Object=MibTableColumn
tokenRingPStatsDataPktsGreaterThan18000Octets=_TokenRingPStatsDataPktsGreaterThan18000Octets_Object((1,3,6,1,2,1,16,1,3,1,17),_TokenRingPStatsDataPktsGreaterThan18000Octets_Type())
tokenRingPStatsDataPktsGreaterThan18000Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPStatsDataPktsGreaterThan18000Octets.setStatus(_A)
_TokenRingPStatsOwner_Type=OwnerString
_TokenRingPStatsOwner_Object=MibTableColumn
tokenRingPStatsOwner=_TokenRingPStatsOwner_Object((1,3,6,1,2,1,16,1,3,1,18),_TokenRingPStatsOwner_Type())
tokenRingPStatsOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:tokenRingPStatsOwner.setStatus(_A)
_TokenRingPStatsStatus_Type=EntryStatus
_TokenRingPStatsStatus_Object=MibTableColumn
tokenRingPStatsStatus=_TokenRingPStatsStatus_Object((1,3,6,1,2,1,16,1,3,1,19),_TokenRingPStatsStatus_Type())
tokenRingPStatsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tokenRingPStatsStatus.setStatus(_A)
_TokenRingMLHistoryTable_Object=MibTable
tokenRingMLHistoryTable=_TokenRingMLHistoryTable_Object((1,3,6,1,2,1,16,2,3))
if mibBuilder.loadTexts:tokenRingMLHistoryTable.setStatus(_A)
_TokenRingMLHistoryEntry_Object=MibTableRow
tokenRingMLHistoryEntry=_TokenRingMLHistoryEntry_Object((1,3,6,1,2,1,16,2,3,1))
tokenRingMLHistoryEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:tokenRingMLHistoryEntry.setStatus(_A)
class _TokenRingMLHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TokenRingMLHistoryIndex_Type.__name__=_E
_TokenRingMLHistoryIndex_Object=MibTableColumn
tokenRingMLHistoryIndex=_TokenRingMLHistoryIndex_Object((1,3,6,1,2,1,16,2,3,1,1),_TokenRingMLHistoryIndex_Type())
tokenRingMLHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryIndex.setStatus(_A)
_TokenRingMLHistorySampleIndex_Type=Integer32
_TokenRingMLHistorySampleIndex_Object=MibTableColumn
tokenRingMLHistorySampleIndex=_TokenRingMLHistorySampleIndex_Object((1,3,6,1,2,1,16,2,3,1,2),_TokenRingMLHistorySampleIndex_Type())
tokenRingMLHistorySampleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistorySampleIndex.setStatus(_A)
_TokenRingMLHistoryIntervalStart_Type=TimeTicks
_TokenRingMLHistoryIntervalStart_Object=MibTableColumn
tokenRingMLHistoryIntervalStart=_TokenRingMLHistoryIntervalStart_Object((1,3,6,1,2,1,16,2,3,1,3),_TokenRingMLHistoryIntervalStart_Type())
tokenRingMLHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryIntervalStart.setStatus(_A)
_TokenRingMLHistoryDropEvents_Type=Counter32
_TokenRingMLHistoryDropEvents_Object=MibTableColumn
tokenRingMLHistoryDropEvents=_TokenRingMLHistoryDropEvents_Object((1,3,6,1,2,1,16,2,3,1,4),_TokenRingMLHistoryDropEvents_Type())
tokenRingMLHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryDropEvents.setStatus(_A)
_TokenRingMLHistoryMacOctets_Type=Counter32
_TokenRingMLHistoryMacOctets_Object=MibTableColumn
tokenRingMLHistoryMacOctets=_TokenRingMLHistoryMacOctets_Object((1,3,6,1,2,1,16,2,3,1,5),_TokenRingMLHistoryMacOctets_Type())
tokenRingMLHistoryMacOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryMacOctets.setStatus(_A)
_TokenRingMLHistoryMacPkts_Type=Counter32
_TokenRingMLHistoryMacPkts_Object=MibTableColumn
tokenRingMLHistoryMacPkts=_TokenRingMLHistoryMacPkts_Object((1,3,6,1,2,1,16,2,3,1,6),_TokenRingMLHistoryMacPkts_Type())
tokenRingMLHistoryMacPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryMacPkts.setStatus(_A)
_TokenRingMLHistoryRingPurgeEvents_Type=Counter32
_TokenRingMLHistoryRingPurgeEvents_Object=MibTableColumn
tokenRingMLHistoryRingPurgeEvents=_TokenRingMLHistoryRingPurgeEvents_Object((1,3,6,1,2,1,16,2,3,1,7),_TokenRingMLHistoryRingPurgeEvents_Type())
tokenRingMLHistoryRingPurgeEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryRingPurgeEvents.setStatus(_A)
_TokenRingMLHistoryRingPurgePkts_Type=Counter32
_TokenRingMLHistoryRingPurgePkts_Object=MibTableColumn
tokenRingMLHistoryRingPurgePkts=_TokenRingMLHistoryRingPurgePkts_Object((1,3,6,1,2,1,16,2,3,1,8),_TokenRingMLHistoryRingPurgePkts_Type())
tokenRingMLHistoryRingPurgePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryRingPurgePkts.setStatus(_A)
_TokenRingMLHistoryBeaconEvents_Type=Counter32
_TokenRingMLHistoryBeaconEvents_Object=MibTableColumn
tokenRingMLHistoryBeaconEvents=_TokenRingMLHistoryBeaconEvents_Object((1,3,6,1,2,1,16,2,3,1,9),_TokenRingMLHistoryBeaconEvents_Type())
tokenRingMLHistoryBeaconEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryBeaconEvents.setStatus(_A)
_TokenRingMLHistoryBeaconTime_Type=TimeInterval
_TokenRingMLHistoryBeaconTime_Object=MibTableColumn
tokenRingMLHistoryBeaconTime=_TokenRingMLHistoryBeaconTime_Object((1,3,6,1,2,1,16,2,3,1,10),_TokenRingMLHistoryBeaconTime_Type())
tokenRingMLHistoryBeaconTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryBeaconTime.setStatus(_A)
_TokenRingMLHistoryBeaconPkts_Type=Counter32
_TokenRingMLHistoryBeaconPkts_Object=MibTableColumn
tokenRingMLHistoryBeaconPkts=_TokenRingMLHistoryBeaconPkts_Object((1,3,6,1,2,1,16,2,3,1,11),_TokenRingMLHistoryBeaconPkts_Type())
tokenRingMLHistoryBeaconPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryBeaconPkts.setStatus(_A)
_TokenRingMLHistoryClaimTokenEvents_Type=Counter32
_TokenRingMLHistoryClaimTokenEvents_Object=MibTableColumn
tokenRingMLHistoryClaimTokenEvents=_TokenRingMLHistoryClaimTokenEvents_Object((1,3,6,1,2,1,16,2,3,1,12),_TokenRingMLHistoryClaimTokenEvents_Type())
tokenRingMLHistoryClaimTokenEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryClaimTokenEvents.setStatus(_A)
_TokenRingMLHistoryClaimTokenPkts_Type=Counter32
_TokenRingMLHistoryClaimTokenPkts_Object=MibTableColumn
tokenRingMLHistoryClaimTokenPkts=_TokenRingMLHistoryClaimTokenPkts_Object((1,3,6,1,2,1,16,2,3,1,13),_TokenRingMLHistoryClaimTokenPkts_Type())
tokenRingMLHistoryClaimTokenPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryClaimTokenPkts.setStatus(_A)
_TokenRingMLHistoryNAUNChanges_Type=Counter32
_TokenRingMLHistoryNAUNChanges_Object=MibTableColumn
tokenRingMLHistoryNAUNChanges=_TokenRingMLHistoryNAUNChanges_Object((1,3,6,1,2,1,16,2,3,1,14),_TokenRingMLHistoryNAUNChanges_Type())
tokenRingMLHistoryNAUNChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryNAUNChanges.setStatus(_A)
_TokenRingMLHistoryLineErrors_Type=Counter32
_TokenRingMLHistoryLineErrors_Object=MibTableColumn
tokenRingMLHistoryLineErrors=_TokenRingMLHistoryLineErrors_Object((1,3,6,1,2,1,16,2,3,1,15),_TokenRingMLHistoryLineErrors_Type())
tokenRingMLHistoryLineErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryLineErrors.setStatus(_A)
_TokenRingMLHistoryInternalErrors_Type=Counter32
_TokenRingMLHistoryInternalErrors_Object=MibTableColumn
tokenRingMLHistoryInternalErrors=_TokenRingMLHistoryInternalErrors_Object((1,3,6,1,2,1,16,2,3,1,16),_TokenRingMLHistoryInternalErrors_Type())
tokenRingMLHistoryInternalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryInternalErrors.setStatus(_A)
_TokenRingMLHistoryBurstErrors_Type=Counter32
_TokenRingMLHistoryBurstErrors_Object=MibTableColumn
tokenRingMLHistoryBurstErrors=_TokenRingMLHistoryBurstErrors_Object((1,3,6,1,2,1,16,2,3,1,17),_TokenRingMLHistoryBurstErrors_Type())
tokenRingMLHistoryBurstErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryBurstErrors.setStatus(_A)
_TokenRingMLHistoryACErrors_Type=Counter32
_TokenRingMLHistoryACErrors_Object=MibTableColumn
tokenRingMLHistoryACErrors=_TokenRingMLHistoryACErrors_Object((1,3,6,1,2,1,16,2,3,1,18),_TokenRingMLHistoryACErrors_Type())
tokenRingMLHistoryACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryACErrors.setStatus(_A)
_TokenRingMLHistoryAbortErrors_Type=Counter32
_TokenRingMLHistoryAbortErrors_Object=MibTableColumn
tokenRingMLHistoryAbortErrors=_TokenRingMLHistoryAbortErrors_Object((1,3,6,1,2,1,16,2,3,1,19),_TokenRingMLHistoryAbortErrors_Type())
tokenRingMLHistoryAbortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryAbortErrors.setStatus(_A)
_TokenRingMLHistoryLostFrameErrors_Type=Counter32
_TokenRingMLHistoryLostFrameErrors_Object=MibTableColumn
tokenRingMLHistoryLostFrameErrors=_TokenRingMLHistoryLostFrameErrors_Object((1,3,6,1,2,1,16,2,3,1,20),_TokenRingMLHistoryLostFrameErrors_Type())
tokenRingMLHistoryLostFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryLostFrameErrors.setStatus(_A)
_TokenRingMLHistoryCongestionErrors_Type=Counter32
_TokenRingMLHistoryCongestionErrors_Object=MibTableColumn
tokenRingMLHistoryCongestionErrors=_TokenRingMLHistoryCongestionErrors_Object((1,3,6,1,2,1,16,2,3,1,21),_TokenRingMLHistoryCongestionErrors_Type())
tokenRingMLHistoryCongestionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryCongestionErrors.setStatus(_A)
_TokenRingMLHistoryFrameCopiedErrors_Type=Counter32
_TokenRingMLHistoryFrameCopiedErrors_Object=MibTableColumn
tokenRingMLHistoryFrameCopiedErrors=_TokenRingMLHistoryFrameCopiedErrors_Object((1,3,6,1,2,1,16,2,3,1,22),_TokenRingMLHistoryFrameCopiedErrors_Type())
tokenRingMLHistoryFrameCopiedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryFrameCopiedErrors.setStatus(_A)
_TokenRingMLHistoryFrequencyErrors_Type=Counter32
_TokenRingMLHistoryFrequencyErrors_Object=MibTableColumn
tokenRingMLHistoryFrequencyErrors=_TokenRingMLHistoryFrequencyErrors_Object((1,3,6,1,2,1,16,2,3,1,23),_TokenRingMLHistoryFrequencyErrors_Type())
tokenRingMLHistoryFrequencyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryFrequencyErrors.setStatus(_A)
_TokenRingMLHistoryTokenErrors_Type=Counter32
_TokenRingMLHistoryTokenErrors_Object=MibTableColumn
tokenRingMLHistoryTokenErrors=_TokenRingMLHistoryTokenErrors_Object((1,3,6,1,2,1,16,2,3,1,24),_TokenRingMLHistoryTokenErrors_Type())
tokenRingMLHistoryTokenErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryTokenErrors.setStatus(_A)
_TokenRingMLHistorySoftErrorReports_Type=Counter32
_TokenRingMLHistorySoftErrorReports_Object=MibTableColumn
tokenRingMLHistorySoftErrorReports=_TokenRingMLHistorySoftErrorReports_Object((1,3,6,1,2,1,16,2,3,1,25),_TokenRingMLHistorySoftErrorReports_Type())
tokenRingMLHistorySoftErrorReports.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistorySoftErrorReports.setStatus(_A)
_TokenRingMLHistoryRingPollEvents_Type=Counter32
_TokenRingMLHistoryRingPollEvents_Object=MibTableColumn
tokenRingMLHistoryRingPollEvents=_TokenRingMLHistoryRingPollEvents_Object((1,3,6,1,2,1,16,2,3,1,26),_TokenRingMLHistoryRingPollEvents_Type())
tokenRingMLHistoryRingPollEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryRingPollEvents.setStatus(_A)
_TokenRingMLHistoryActiveStations_Type=Integer32
_TokenRingMLHistoryActiveStations_Object=MibTableColumn
tokenRingMLHistoryActiveStations=_TokenRingMLHistoryActiveStations_Object((1,3,6,1,2,1,16,2,3,1,27),_TokenRingMLHistoryActiveStations_Type())
tokenRingMLHistoryActiveStations.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingMLHistoryActiveStations.setStatus(_A)
_TokenRingPHistoryTable_Object=MibTable
tokenRingPHistoryTable=_TokenRingPHistoryTable_Object((1,3,6,1,2,1,16,2,4))
if mibBuilder.loadTexts:tokenRingPHistoryTable.setStatus(_A)
_TokenRingPHistoryEntry_Object=MibTableRow
tokenRingPHistoryEntry=_TokenRingPHistoryEntry_Object((1,3,6,1,2,1,16,2,4,1))
tokenRingPHistoryEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:tokenRingPHistoryEntry.setStatus(_A)
class _TokenRingPHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TokenRingPHistoryIndex_Type.__name__=_E
_TokenRingPHistoryIndex_Object=MibTableColumn
tokenRingPHistoryIndex=_TokenRingPHistoryIndex_Object((1,3,6,1,2,1,16,2,4,1,1),_TokenRingPHistoryIndex_Type())
tokenRingPHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryIndex.setStatus(_A)
_TokenRingPHistorySampleIndex_Type=Integer32
_TokenRingPHistorySampleIndex_Object=MibTableColumn
tokenRingPHistorySampleIndex=_TokenRingPHistorySampleIndex_Object((1,3,6,1,2,1,16,2,4,1,2),_TokenRingPHistorySampleIndex_Type())
tokenRingPHistorySampleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistorySampleIndex.setStatus(_A)
_TokenRingPHistoryIntervalStart_Type=TimeTicks
_TokenRingPHistoryIntervalStart_Object=MibTableColumn
tokenRingPHistoryIntervalStart=_TokenRingPHistoryIntervalStart_Object((1,3,6,1,2,1,16,2,4,1,3),_TokenRingPHistoryIntervalStart_Type())
tokenRingPHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryIntervalStart.setStatus(_A)
_TokenRingPHistoryDropEvents_Type=Counter32
_TokenRingPHistoryDropEvents_Object=MibTableColumn
tokenRingPHistoryDropEvents=_TokenRingPHistoryDropEvents_Object((1,3,6,1,2,1,16,2,4,1,4),_TokenRingPHistoryDropEvents_Type())
tokenRingPHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDropEvents.setStatus(_A)
_TokenRingPHistoryDataOctets_Type=Counter32
_TokenRingPHistoryDataOctets_Object=MibTableColumn
tokenRingPHistoryDataOctets=_TokenRingPHistoryDataOctets_Object((1,3,6,1,2,1,16,2,4,1,5),_TokenRingPHistoryDataOctets_Type())
tokenRingPHistoryDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataOctets.setStatus(_A)
_TokenRingPHistoryDataPkts_Type=Counter32
_TokenRingPHistoryDataPkts_Object=MibTableColumn
tokenRingPHistoryDataPkts=_TokenRingPHistoryDataPkts_Object((1,3,6,1,2,1,16,2,4,1,6),_TokenRingPHistoryDataPkts_Type())
tokenRingPHistoryDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts.setStatus(_A)
_TokenRingPHistoryDataBroadcastPkts_Type=Counter32
_TokenRingPHistoryDataBroadcastPkts_Object=MibTableColumn
tokenRingPHistoryDataBroadcastPkts=_TokenRingPHistoryDataBroadcastPkts_Object((1,3,6,1,2,1,16,2,4,1,7),_TokenRingPHistoryDataBroadcastPkts_Type())
tokenRingPHistoryDataBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataBroadcastPkts.setStatus(_A)
_TokenRingPHistoryDataMulticastPkts_Type=Counter32
_TokenRingPHistoryDataMulticastPkts_Object=MibTableColumn
tokenRingPHistoryDataMulticastPkts=_TokenRingPHistoryDataMulticastPkts_Object((1,3,6,1,2,1,16,2,4,1,8),_TokenRingPHistoryDataMulticastPkts_Type())
tokenRingPHistoryDataMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataMulticastPkts.setStatus(_A)
_TokenRingPHistoryDataPkts18to63Octets_Type=Counter32
_TokenRingPHistoryDataPkts18to63Octets_Object=MibTableColumn
tokenRingPHistoryDataPkts18to63Octets=_TokenRingPHistoryDataPkts18to63Octets_Object((1,3,6,1,2,1,16,2,4,1,9),_TokenRingPHistoryDataPkts18to63Octets_Type())
tokenRingPHistoryDataPkts18to63Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts18to63Octets.setStatus(_A)
_TokenRingPHistoryDataPkts64to127Octets_Type=Counter32
_TokenRingPHistoryDataPkts64to127Octets_Object=MibTableColumn
tokenRingPHistoryDataPkts64to127Octets=_TokenRingPHistoryDataPkts64to127Octets_Object((1,3,6,1,2,1,16,2,4,1,10),_TokenRingPHistoryDataPkts64to127Octets_Type())
tokenRingPHistoryDataPkts64to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts64to127Octets.setStatus(_A)
_TokenRingPHistoryDataPkts128to255Octets_Type=Counter32
_TokenRingPHistoryDataPkts128to255Octets_Object=MibTableColumn
tokenRingPHistoryDataPkts128to255Octets=_TokenRingPHistoryDataPkts128to255Octets_Object((1,3,6,1,2,1,16,2,4,1,11),_TokenRingPHistoryDataPkts128to255Octets_Type())
tokenRingPHistoryDataPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts128to255Octets.setStatus(_A)
_TokenRingPHistoryDataPkts256to511Octets_Type=Counter32
_TokenRingPHistoryDataPkts256to511Octets_Object=MibTableColumn
tokenRingPHistoryDataPkts256to511Octets=_TokenRingPHistoryDataPkts256to511Octets_Object((1,3,6,1,2,1,16,2,4,1,12),_TokenRingPHistoryDataPkts256to511Octets_Type())
tokenRingPHistoryDataPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts256to511Octets.setStatus(_A)
_TokenRingPHistoryDataPkts512to1023Octets_Type=Counter32
_TokenRingPHistoryDataPkts512to1023Octets_Object=MibTableColumn
tokenRingPHistoryDataPkts512to1023Octets=_TokenRingPHistoryDataPkts512to1023Octets_Object((1,3,6,1,2,1,16,2,4,1,13),_TokenRingPHistoryDataPkts512to1023Octets_Type())
tokenRingPHistoryDataPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts512to1023Octets.setStatus(_A)
_TokenRingPHistoryDataPkts1024to2047Octets_Type=Counter32
_TokenRingPHistoryDataPkts1024to2047Octets_Object=MibTableColumn
tokenRingPHistoryDataPkts1024to2047Octets=_TokenRingPHistoryDataPkts1024to2047Octets_Object((1,3,6,1,2,1,16,2,4,1,14),_TokenRingPHistoryDataPkts1024to2047Octets_Type())
tokenRingPHistoryDataPkts1024to2047Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts1024to2047Octets.setStatus(_A)
_TokenRingPHistoryDataPkts2048to4095Octets_Type=Counter32
_TokenRingPHistoryDataPkts2048to4095Octets_Object=MibTableColumn
tokenRingPHistoryDataPkts2048to4095Octets=_TokenRingPHistoryDataPkts2048to4095Octets_Object((1,3,6,1,2,1,16,2,4,1,15),_TokenRingPHistoryDataPkts2048to4095Octets_Type())
tokenRingPHistoryDataPkts2048to4095Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts2048to4095Octets.setStatus(_A)
_TokenRingPHistoryDataPkts4096to8191Octets_Type=Counter32
_TokenRingPHistoryDataPkts4096to8191Octets_Object=MibTableColumn
tokenRingPHistoryDataPkts4096to8191Octets=_TokenRingPHistoryDataPkts4096to8191Octets_Object((1,3,6,1,2,1,16,2,4,1,16),_TokenRingPHistoryDataPkts4096to8191Octets_Type())
tokenRingPHistoryDataPkts4096to8191Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts4096to8191Octets.setStatus(_A)
_TokenRingPHistoryDataPkts8192to18000Octets_Type=Counter32
_TokenRingPHistoryDataPkts8192to18000Octets_Object=MibTableColumn
tokenRingPHistoryDataPkts8192to18000Octets=_TokenRingPHistoryDataPkts8192to18000Octets_Object((1,3,6,1,2,1,16,2,4,1,17),_TokenRingPHistoryDataPkts8192to18000Octets_Type())
tokenRingPHistoryDataPkts8192to18000Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPkts8192to18000Octets.setStatus(_A)
_TokenRingPHistoryDataPktsGreaterThan18000Octets_Type=Counter32
_TokenRingPHistoryDataPktsGreaterThan18000Octets_Object=MibTableColumn
tokenRingPHistoryDataPktsGreaterThan18000Octets=_TokenRingPHistoryDataPktsGreaterThan18000Octets_Object((1,3,6,1,2,1,16,2,4,1,18),_TokenRingPHistoryDataPktsGreaterThan18000Octets_Type())
tokenRingPHistoryDataPktsGreaterThan18000Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tokenRingPHistoryDataPktsGreaterThan18000Octets.setStatus(_A)
_TokenRing_ObjectIdentity=ObjectIdentity
tokenRing=_TokenRing_ObjectIdentity((1,3,6,1,2,1,16,10))
_RingStationControlTable_Object=MibTable
ringStationControlTable=_RingStationControlTable_Object((1,3,6,1,2,1,16,10,1))
if mibBuilder.loadTexts:ringStationControlTable.setStatus(_A)
_RingStationControlEntry_Object=MibTableRow
ringStationControlEntry=_RingStationControlEntry_Object((1,3,6,1,2,1,16,10,1,1))
ringStationControlEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:ringStationControlEntry.setStatus(_A)
class _RingStationControlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RingStationControlIfIndex_Type.__name__=_E
_RingStationControlIfIndex_Object=MibTableColumn
ringStationControlIfIndex=_RingStationControlIfIndex_Object((1,3,6,1,2,1,16,10,1,1,1),_RingStationControlIfIndex_Type())
ringStationControlIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationControlIfIndex.setStatus(_A)
_RingStationControlTableSize_Type=Integer32
_RingStationControlTableSize_Object=MibTableColumn
ringStationControlTableSize=_RingStationControlTableSize_Object((1,3,6,1,2,1,16,10,1,1,2),_RingStationControlTableSize_Type())
ringStationControlTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationControlTableSize.setStatus(_A)
_RingStationControlActiveStations_Type=Integer32
_RingStationControlActiveStations_Object=MibTableColumn
ringStationControlActiveStations=_RingStationControlActiveStations_Object((1,3,6,1,2,1,16,10,1,1,3),_RingStationControlActiveStations_Type())
ringStationControlActiveStations.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationControlActiveStations.setStatus(_A)
class _RingStationControlRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('normalOperation',1),('ringPurgeState',2),('claimTokenState',3),('beaconFrameStreamingState',4),('beaconBitStreamingState',5),('beaconRingSignalLossState',6),('beaconSetRecoveryModeState',7)))
_RingStationControlRingState_Type.__name__=_E
_RingStationControlRingState_Object=MibTableColumn
ringStationControlRingState=_RingStationControlRingState_Object((1,3,6,1,2,1,16,10,1,1,4),_RingStationControlRingState_Type())
ringStationControlRingState.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationControlRingState.setStatus(_A)
_RingStationControlBeaconSender_Type=MacAddress
_RingStationControlBeaconSender_Object=MibTableColumn
ringStationControlBeaconSender=_RingStationControlBeaconSender_Object((1,3,6,1,2,1,16,10,1,1,5),_RingStationControlBeaconSender_Type())
ringStationControlBeaconSender.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationControlBeaconSender.setStatus(_A)
_RingStationControlBeaconNAUN_Type=MacAddress
_RingStationControlBeaconNAUN_Object=MibTableColumn
ringStationControlBeaconNAUN=_RingStationControlBeaconNAUN_Object((1,3,6,1,2,1,16,10,1,1,6),_RingStationControlBeaconNAUN_Type())
ringStationControlBeaconNAUN.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationControlBeaconNAUN.setStatus(_A)
_RingStationControlActiveMonitor_Type=MacAddress
_RingStationControlActiveMonitor_Object=MibTableColumn
ringStationControlActiveMonitor=_RingStationControlActiveMonitor_Object((1,3,6,1,2,1,16,10,1,1,7),_RingStationControlActiveMonitor_Type())
ringStationControlActiveMonitor.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationControlActiveMonitor.setStatus(_A)
_RingStationControlOrderChanges_Type=Counter32
_RingStationControlOrderChanges_Object=MibTableColumn
ringStationControlOrderChanges=_RingStationControlOrderChanges_Object((1,3,6,1,2,1,16,10,1,1,8),_RingStationControlOrderChanges_Type())
ringStationControlOrderChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationControlOrderChanges.setStatus(_A)
_RingStationControlOwner_Type=OwnerString
_RingStationControlOwner_Object=MibTableColumn
ringStationControlOwner=_RingStationControlOwner_Object((1,3,6,1,2,1,16,10,1,1,9),_RingStationControlOwner_Type())
ringStationControlOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:ringStationControlOwner.setStatus(_A)
_RingStationControlStatus_Type=EntryStatus
_RingStationControlStatus_Object=MibTableColumn
ringStationControlStatus=_RingStationControlStatus_Object((1,3,6,1,2,1,16,10,1,1,10),_RingStationControlStatus_Type())
ringStationControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ringStationControlStatus.setStatus(_A)
_RingStationTable_Object=MibTable
ringStationTable=_RingStationTable_Object((1,3,6,1,2,1,16,10,2))
if mibBuilder.loadTexts:ringStationTable.setStatus(_A)
_RingStationEntry_Object=MibTableRow
ringStationEntry=_RingStationEntry_Object((1,3,6,1,2,1,16,10,2,1))
ringStationEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:ringStationEntry.setStatus(_A)
_RingStationIfIndex_Type=Integer32
_RingStationIfIndex_Object=MibTableColumn
ringStationIfIndex=_RingStationIfIndex_Object((1,3,6,1,2,1,16,10,2,1,1),_RingStationIfIndex_Type())
ringStationIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationIfIndex.setStatus(_A)
_RingStationMacAddress_Type=MacAddress
_RingStationMacAddress_Object=MibTableColumn
ringStationMacAddress=_RingStationMacAddress_Object((1,3,6,1,2,1,16,10,2,1,2),_RingStationMacAddress_Type())
ringStationMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationMacAddress.setStatus(_A)
_RingStationLastNAUN_Type=MacAddress
_RingStationLastNAUN_Object=MibTableColumn
ringStationLastNAUN=_RingStationLastNAUN_Object((1,3,6,1,2,1,16,10,2,1,3),_RingStationLastNAUN_Type())
ringStationLastNAUN.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationLastNAUN.setStatus(_A)
class _RingStationStationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('forcedRemoval',3)))
_RingStationStationStatus_Type.__name__=_E
_RingStationStationStatus_Object=MibTableColumn
ringStationStationStatus=_RingStationStationStatus_Object((1,3,6,1,2,1,16,10,2,1,4),_RingStationStationStatus_Type())
ringStationStationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationStationStatus.setStatus(_A)
_RingStationLastEnterTime_Type=TimeTicks
_RingStationLastEnterTime_Object=MibTableColumn
ringStationLastEnterTime=_RingStationLastEnterTime_Object((1,3,6,1,2,1,16,10,2,1,5),_RingStationLastEnterTime_Type())
ringStationLastEnterTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationLastEnterTime.setStatus(_A)
_RingStationLastExitTime_Type=TimeTicks
_RingStationLastExitTime_Object=MibTableColumn
ringStationLastExitTime=_RingStationLastExitTime_Object((1,3,6,1,2,1,16,10,2,1,6),_RingStationLastExitTime_Type())
ringStationLastExitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationLastExitTime.setStatus(_A)
_RingStationDuplicateAddresses_Type=Counter32
_RingStationDuplicateAddresses_Object=MibTableColumn
ringStationDuplicateAddresses=_RingStationDuplicateAddresses_Object((1,3,6,1,2,1,16,10,2,1,7),_RingStationDuplicateAddresses_Type())
ringStationDuplicateAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationDuplicateAddresses.setStatus(_A)
_RingStationInLineErrors_Type=Counter32
_RingStationInLineErrors_Object=MibTableColumn
ringStationInLineErrors=_RingStationInLineErrors_Object((1,3,6,1,2,1,16,10,2,1,8),_RingStationInLineErrors_Type())
ringStationInLineErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationInLineErrors.setStatus(_A)
_RingStationOutLineErrors_Type=Counter32
_RingStationOutLineErrors_Object=MibTableColumn
ringStationOutLineErrors=_RingStationOutLineErrors_Object((1,3,6,1,2,1,16,10,2,1,9),_RingStationOutLineErrors_Type())
ringStationOutLineErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationOutLineErrors.setStatus(_A)
_RingStationInternalErrors_Type=Counter32
_RingStationInternalErrors_Object=MibTableColumn
ringStationInternalErrors=_RingStationInternalErrors_Object((1,3,6,1,2,1,16,10,2,1,10),_RingStationInternalErrors_Type())
ringStationInternalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationInternalErrors.setStatus(_A)
_RingStationInBurstErrors_Type=Counter32
_RingStationInBurstErrors_Object=MibTableColumn
ringStationInBurstErrors=_RingStationInBurstErrors_Object((1,3,6,1,2,1,16,10,2,1,11),_RingStationInBurstErrors_Type())
ringStationInBurstErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationInBurstErrors.setStatus(_A)
_RingStationOutBurstErrors_Type=Counter32
_RingStationOutBurstErrors_Object=MibTableColumn
ringStationOutBurstErrors=_RingStationOutBurstErrors_Object((1,3,6,1,2,1,16,10,2,1,12),_RingStationOutBurstErrors_Type())
ringStationOutBurstErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationOutBurstErrors.setStatus(_A)
_RingStationACErrors_Type=Counter32
_RingStationACErrors_Object=MibTableColumn
ringStationACErrors=_RingStationACErrors_Object((1,3,6,1,2,1,16,10,2,1,13),_RingStationACErrors_Type())
ringStationACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationACErrors.setStatus(_A)
_RingStationAbortErrors_Type=Counter32
_RingStationAbortErrors_Object=MibTableColumn
ringStationAbortErrors=_RingStationAbortErrors_Object((1,3,6,1,2,1,16,10,2,1,14),_RingStationAbortErrors_Type())
ringStationAbortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationAbortErrors.setStatus(_A)
_RingStationLostFrameErrors_Type=Counter32
_RingStationLostFrameErrors_Object=MibTableColumn
ringStationLostFrameErrors=_RingStationLostFrameErrors_Object((1,3,6,1,2,1,16,10,2,1,15),_RingStationLostFrameErrors_Type())
ringStationLostFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationLostFrameErrors.setStatus(_A)
_RingStationCongestionErrors_Type=Counter32
_RingStationCongestionErrors_Object=MibTableColumn
ringStationCongestionErrors=_RingStationCongestionErrors_Object((1,3,6,1,2,1,16,10,2,1,16),_RingStationCongestionErrors_Type())
ringStationCongestionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationCongestionErrors.setStatus(_A)
_RingStationFrameCopiedErrors_Type=Counter32
_RingStationFrameCopiedErrors_Object=MibTableColumn
ringStationFrameCopiedErrors=_RingStationFrameCopiedErrors_Object((1,3,6,1,2,1,16,10,2,1,17),_RingStationFrameCopiedErrors_Type())
ringStationFrameCopiedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationFrameCopiedErrors.setStatus(_A)
_RingStationFrequencyErrors_Type=Counter32
_RingStationFrequencyErrors_Object=MibTableColumn
ringStationFrequencyErrors=_RingStationFrequencyErrors_Object((1,3,6,1,2,1,16,10,2,1,18),_RingStationFrequencyErrors_Type())
ringStationFrequencyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationFrequencyErrors.setStatus(_A)
_RingStationTokenErrors_Type=Counter32
_RingStationTokenErrors_Object=MibTableColumn
ringStationTokenErrors=_RingStationTokenErrors_Object((1,3,6,1,2,1,16,10,2,1,19),_RingStationTokenErrors_Type())
ringStationTokenErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationTokenErrors.setStatus(_A)
_RingStationInBeaconErrors_Type=Counter32
_RingStationInBeaconErrors_Object=MibTableColumn
ringStationInBeaconErrors=_RingStationInBeaconErrors_Object((1,3,6,1,2,1,16,10,2,1,20),_RingStationInBeaconErrors_Type())
ringStationInBeaconErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationInBeaconErrors.setStatus(_A)
_RingStationOutBeaconErrors_Type=Counter32
_RingStationOutBeaconErrors_Object=MibTableColumn
ringStationOutBeaconErrors=_RingStationOutBeaconErrors_Object((1,3,6,1,2,1,16,10,2,1,21),_RingStationOutBeaconErrors_Type())
ringStationOutBeaconErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationOutBeaconErrors.setStatus(_A)
_RingStationInsertions_Type=Counter32
_RingStationInsertions_Object=MibTableColumn
ringStationInsertions=_RingStationInsertions_Object((1,3,6,1,2,1,16,10,2,1,22),_RingStationInsertions_Type())
ringStationInsertions.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationInsertions.setStatus(_A)
_RingStationOrderTable_Object=MibTable
ringStationOrderTable=_RingStationOrderTable_Object((1,3,6,1,2,1,16,10,3))
if mibBuilder.loadTexts:ringStationOrderTable.setStatus(_A)
_RingStationOrderEntry_Object=MibTableRow
ringStationOrderEntry=_RingStationOrderEntry_Object((1,3,6,1,2,1,16,10,3,1))
ringStationOrderEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:ringStationOrderEntry.setStatus(_A)
_RingStationOrderIfIndex_Type=Integer32
_RingStationOrderIfIndex_Object=MibTableColumn
ringStationOrderIfIndex=_RingStationOrderIfIndex_Object((1,3,6,1,2,1,16,10,3,1,1),_RingStationOrderIfIndex_Type())
ringStationOrderIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationOrderIfIndex.setStatus(_A)
_RingStationOrderOrderIndex_Type=Integer32
_RingStationOrderOrderIndex_Object=MibTableColumn
ringStationOrderOrderIndex=_RingStationOrderOrderIndex_Object((1,3,6,1,2,1,16,10,3,1,2),_RingStationOrderOrderIndex_Type())
ringStationOrderOrderIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationOrderOrderIndex.setStatus(_A)
_RingStationOrderMacAddress_Type=MacAddress
_RingStationOrderMacAddress_Object=MibTableColumn
ringStationOrderMacAddress=_RingStationOrderMacAddress_Object((1,3,6,1,2,1,16,10,3,1,3),_RingStationOrderMacAddress_Type())
ringStationOrderMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationOrderMacAddress.setStatus(_A)
_RingStationConfigControlTable_Object=MibTable
ringStationConfigControlTable=_RingStationConfigControlTable_Object((1,3,6,1,2,1,16,10,4))
if mibBuilder.loadTexts:ringStationConfigControlTable.setStatus(_A)
_RingStationConfigControlEntry_Object=MibTableRow
ringStationConfigControlEntry=_RingStationConfigControlEntry_Object((1,3,6,1,2,1,16,10,4,1))
ringStationConfigControlEntry.setIndexNames((0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:ringStationConfigControlEntry.setStatus(_A)
_RingStationConfigControlIfIndex_Type=Integer32
_RingStationConfigControlIfIndex_Object=MibTableColumn
ringStationConfigControlIfIndex=_RingStationConfigControlIfIndex_Object((1,3,6,1,2,1,16,10,4,1,1),_RingStationConfigControlIfIndex_Type())
ringStationConfigControlIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationConfigControlIfIndex.setStatus(_A)
_RingStationConfigControlMacAddress_Type=MacAddress
_RingStationConfigControlMacAddress_Object=MibTableColumn
ringStationConfigControlMacAddress=_RingStationConfigControlMacAddress_Object((1,3,6,1,2,1,16,10,4,1,2),_RingStationConfigControlMacAddress_Type())
ringStationConfigControlMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationConfigControlMacAddress.setStatus(_A)
class _RingStationConfigControlRemove_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('removing',2)))
_RingStationConfigControlRemove_Type.__name__=_E
_RingStationConfigControlRemove_Object=MibTableColumn
ringStationConfigControlRemove=_RingStationConfigControlRemove_Object((1,3,6,1,2,1,16,10,4,1,3),_RingStationConfigControlRemove_Type())
ringStationConfigControlRemove.setMaxAccess(_D)
if mibBuilder.loadTexts:ringStationConfigControlRemove.setStatus(_A)
class _RingStationConfigControlUpdateStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('updating',2)))
_RingStationConfigControlUpdateStats_Type.__name__=_E
_RingStationConfigControlUpdateStats_Object=MibTableColumn
ringStationConfigControlUpdateStats=_RingStationConfigControlUpdateStats_Object((1,3,6,1,2,1,16,10,4,1,4),_RingStationConfigControlUpdateStats_Type())
ringStationConfigControlUpdateStats.setMaxAccess(_D)
if mibBuilder.loadTexts:ringStationConfigControlUpdateStats.setStatus(_A)
_RingStationConfigTable_Object=MibTable
ringStationConfigTable=_RingStationConfigTable_Object((1,3,6,1,2,1,16,10,5))
if mibBuilder.loadTexts:ringStationConfigTable.setStatus(_A)
_RingStationConfigEntry_Object=MibTableRow
ringStationConfigEntry=_RingStationConfigEntry_Object((1,3,6,1,2,1,16,10,5,1))
ringStationConfigEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:ringStationConfigEntry.setStatus(_A)
_RingStationConfigIfIndex_Type=Integer32
_RingStationConfigIfIndex_Object=MibTableColumn
ringStationConfigIfIndex=_RingStationConfigIfIndex_Object((1,3,6,1,2,1,16,10,5,1,1),_RingStationConfigIfIndex_Type())
ringStationConfigIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationConfigIfIndex.setStatus(_A)
_RingStationConfigMacAddress_Type=MacAddress
_RingStationConfigMacAddress_Object=MibTableColumn
ringStationConfigMacAddress=_RingStationConfigMacAddress_Object((1,3,6,1,2,1,16,10,5,1,2),_RingStationConfigMacAddress_Type())
ringStationConfigMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationConfigMacAddress.setStatus(_A)
_RingStationConfigUpdateTime_Type=TimeTicks
_RingStationConfigUpdateTime_Object=MibTableColumn
ringStationConfigUpdateTime=_RingStationConfigUpdateTime_Object((1,3,6,1,2,1,16,10,5,1,3),_RingStationConfigUpdateTime_Type())
ringStationConfigUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationConfigUpdateTime.setStatus(_A)
class _RingStationConfigLocation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_RingStationConfigLocation_Type.__name__=_F
_RingStationConfigLocation_Object=MibTableColumn
ringStationConfigLocation=_RingStationConfigLocation_Object((1,3,6,1,2,1,16,10,5,1,4),_RingStationConfigLocation_Type())
ringStationConfigLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationConfigLocation.setStatus(_A)
class _RingStationConfigMicrocode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_RingStationConfigMicrocode_Type.__name__=_F
_RingStationConfigMicrocode_Object=MibTableColumn
ringStationConfigMicrocode=_RingStationConfigMicrocode_Object((1,3,6,1,2,1,16,10,5,1,5),_RingStationConfigMicrocode_Type())
ringStationConfigMicrocode.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationConfigMicrocode.setStatus(_A)
class _RingStationConfigGroupAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_RingStationConfigGroupAddress_Type.__name__=_F
_RingStationConfigGroupAddress_Object=MibTableColumn
ringStationConfigGroupAddress=_RingStationConfigGroupAddress_Object((1,3,6,1,2,1,16,10,5,1,6),_RingStationConfigGroupAddress_Type())
ringStationConfigGroupAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationConfigGroupAddress.setStatus(_A)
class _RingStationConfigFunctionalAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_RingStationConfigFunctionalAddress_Type.__name__=_F
_RingStationConfigFunctionalAddress_Object=MibTableColumn
ringStationConfigFunctionalAddress=_RingStationConfigFunctionalAddress_Object((1,3,6,1,2,1,16,10,5,1,7),_RingStationConfigFunctionalAddress_Type())
ringStationConfigFunctionalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ringStationConfigFunctionalAddress.setStatus(_A)
_SourceRoutingStatsTable_Object=MibTable
sourceRoutingStatsTable=_SourceRoutingStatsTable_Object((1,3,6,1,2,1,16,10,6))
if mibBuilder.loadTexts:sourceRoutingStatsTable.setStatus(_A)
_SourceRoutingStatsEntry_Object=MibTableRow
sourceRoutingStatsEntry=_SourceRoutingStatsEntry_Object((1,3,6,1,2,1,16,10,6,1))
sourceRoutingStatsEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:sourceRoutingStatsEntry.setStatus(_A)
_SourceRoutingStatsIfIndex_Type=Integer32
_SourceRoutingStatsIfIndex_Object=MibTableColumn
sourceRoutingStatsIfIndex=_SourceRoutingStatsIfIndex_Object((1,3,6,1,2,1,16,10,6,1,1),_SourceRoutingStatsIfIndex_Type())
sourceRoutingStatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsIfIndex.setStatus(_A)
_SourceRoutingStatsRingNumber_Type=Integer32
_SourceRoutingStatsRingNumber_Object=MibTableColumn
sourceRoutingStatsRingNumber=_SourceRoutingStatsRingNumber_Object((1,3,6,1,2,1,16,10,6,1,2),_SourceRoutingStatsRingNumber_Type())
sourceRoutingStatsRingNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsRingNumber.setStatus(_A)
_SourceRoutingStatsInFrames_Type=Counter32
_SourceRoutingStatsInFrames_Object=MibTableColumn
sourceRoutingStatsInFrames=_SourceRoutingStatsInFrames_Object((1,3,6,1,2,1,16,10,6,1,3),_SourceRoutingStatsInFrames_Type())
sourceRoutingStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsInFrames.setStatus(_A)
_SourceRoutingStatsOutFrames_Type=Counter32
_SourceRoutingStatsOutFrames_Object=MibTableColumn
sourceRoutingStatsOutFrames=_SourceRoutingStatsOutFrames_Object((1,3,6,1,2,1,16,10,6,1,4),_SourceRoutingStatsOutFrames_Type())
sourceRoutingStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsOutFrames.setStatus(_A)
_SourceRoutingStatsThroughFrames_Type=Counter32
_SourceRoutingStatsThroughFrames_Object=MibTableColumn
sourceRoutingStatsThroughFrames=_SourceRoutingStatsThroughFrames_Object((1,3,6,1,2,1,16,10,6,1,5),_SourceRoutingStatsThroughFrames_Type())
sourceRoutingStatsThroughFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsThroughFrames.setStatus(_A)
_SourceRoutingStatsAllRoutesBroadcastFrames_Type=Counter32
_SourceRoutingStatsAllRoutesBroadcastFrames_Object=MibTableColumn
sourceRoutingStatsAllRoutesBroadcastFrames=_SourceRoutingStatsAllRoutesBroadcastFrames_Object((1,3,6,1,2,1,16,10,6,1,6),_SourceRoutingStatsAllRoutesBroadcastFrames_Type())
sourceRoutingStatsAllRoutesBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsAllRoutesBroadcastFrames.setStatus(_A)
_SourceRoutingStatsSingleRouteBroadcastFrames_Type=Counter32
_SourceRoutingStatsSingleRouteBroadcastFrames_Object=MibTableColumn
sourceRoutingStatsSingleRouteBroadcastFrames=_SourceRoutingStatsSingleRouteBroadcastFrames_Object((1,3,6,1,2,1,16,10,6,1,7),_SourceRoutingStatsSingleRouteBroadcastFrames_Type())
sourceRoutingStatsSingleRouteBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsSingleRouteBroadcastFrames.setStatus(_A)
_SourceRoutingStatsInOctets_Type=Counter32
_SourceRoutingStatsInOctets_Object=MibTableColumn
sourceRoutingStatsInOctets=_SourceRoutingStatsInOctets_Object((1,3,6,1,2,1,16,10,6,1,8),_SourceRoutingStatsInOctets_Type())
sourceRoutingStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsInOctets.setStatus(_A)
_SourceRoutingStatsOutOctets_Type=Counter32
_SourceRoutingStatsOutOctets_Object=MibTableColumn
sourceRoutingStatsOutOctets=_SourceRoutingStatsOutOctets_Object((1,3,6,1,2,1,16,10,6,1,9),_SourceRoutingStatsOutOctets_Type())
sourceRoutingStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsOutOctets.setStatus(_A)
_SourceRoutingStatsThroughOctets_Type=Counter32
_SourceRoutingStatsThroughOctets_Object=MibTableColumn
sourceRoutingStatsThroughOctets=_SourceRoutingStatsThroughOctets_Object((1,3,6,1,2,1,16,10,6,1,10),_SourceRoutingStatsThroughOctets_Type())
sourceRoutingStatsThroughOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsThroughOctets.setStatus(_A)
_SourceRoutingStatsAllRoutesBroadcastOctets_Type=Counter32
_SourceRoutingStatsAllRoutesBroadcastOctets_Object=MibTableColumn
sourceRoutingStatsAllRoutesBroadcastOctets=_SourceRoutingStatsAllRoutesBroadcastOctets_Object((1,3,6,1,2,1,16,10,6,1,11),_SourceRoutingStatsAllRoutesBroadcastOctets_Type())
sourceRoutingStatsAllRoutesBroadcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsAllRoutesBroadcastOctets.setStatus(_A)
_SourceRoutingStatsSingleRoutesBroadcastOctets_Type=Counter32
_SourceRoutingStatsSingleRoutesBroadcastOctets_Object=MibTableColumn
sourceRoutingStatsSingleRoutesBroadcastOctets=_SourceRoutingStatsSingleRoutesBroadcastOctets_Object((1,3,6,1,2,1,16,10,6,1,12),_SourceRoutingStatsSingleRoutesBroadcastOctets_Type())
sourceRoutingStatsSingleRoutesBroadcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsSingleRoutesBroadcastOctets.setStatus(_A)
_SourceRoutingStatsLocalLLCFrames_Type=Counter32
_SourceRoutingStatsLocalLLCFrames_Object=MibTableColumn
sourceRoutingStatsLocalLLCFrames=_SourceRoutingStatsLocalLLCFrames_Object((1,3,6,1,2,1,16,10,6,1,13),_SourceRoutingStatsLocalLLCFrames_Type())
sourceRoutingStatsLocalLLCFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsLocalLLCFrames.setStatus(_A)
_SourceRoutingStats1HopFrames_Type=Counter32
_SourceRoutingStats1HopFrames_Object=MibTableColumn
sourceRoutingStats1HopFrames=_SourceRoutingStats1HopFrames_Object((1,3,6,1,2,1,16,10,6,1,14),_SourceRoutingStats1HopFrames_Type())
sourceRoutingStats1HopFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStats1HopFrames.setStatus(_A)
_SourceRoutingStats2HopsFrames_Type=Counter32
_SourceRoutingStats2HopsFrames_Object=MibTableColumn
sourceRoutingStats2HopsFrames=_SourceRoutingStats2HopsFrames_Object((1,3,6,1,2,1,16,10,6,1,15),_SourceRoutingStats2HopsFrames_Type())
sourceRoutingStats2HopsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStats2HopsFrames.setStatus(_A)
_SourceRoutingStats3HopsFrames_Type=Counter32
_SourceRoutingStats3HopsFrames_Object=MibTableColumn
sourceRoutingStats3HopsFrames=_SourceRoutingStats3HopsFrames_Object((1,3,6,1,2,1,16,10,6,1,16),_SourceRoutingStats3HopsFrames_Type())
sourceRoutingStats3HopsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStats3HopsFrames.setStatus(_A)
_SourceRoutingStats4HopsFrames_Type=Counter32
_SourceRoutingStats4HopsFrames_Object=MibTableColumn
sourceRoutingStats4HopsFrames=_SourceRoutingStats4HopsFrames_Object((1,3,6,1,2,1,16,10,6,1,17),_SourceRoutingStats4HopsFrames_Type())
sourceRoutingStats4HopsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStats4HopsFrames.setStatus(_A)
_SourceRoutingStats5HopsFrames_Type=Counter32
_SourceRoutingStats5HopsFrames_Object=MibTableColumn
sourceRoutingStats5HopsFrames=_SourceRoutingStats5HopsFrames_Object((1,3,6,1,2,1,16,10,6,1,18),_SourceRoutingStats5HopsFrames_Type())
sourceRoutingStats5HopsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStats5HopsFrames.setStatus(_A)
_SourceRoutingStats6HopsFrames_Type=Counter32
_SourceRoutingStats6HopsFrames_Object=MibTableColumn
sourceRoutingStats6HopsFrames=_SourceRoutingStats6HopsFrames_Object((1,3,6,1,2,1,16,10,6,1,19),_SourceRoutingStats6HopsFrames_Type())
sourceRoutingStats6HopsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStats6HopsFrames.setStatus(_A)
_SourceRoutingStats7HopsFrames_Type=Counter32
_SourceRoutingStats7HopsFrames_Object=MibTableColumn
sourceRoutingStats7HopsFrames=_SourceRoutingStats7HopsFrames_Object((1,3,6,1,2,1,16,10,6,1,20),_SourceRoutingStats7HopsFrames_Type())
sourceRoutingStats7HopsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStats7HopsFrames.setStatus(_A)
_SourceRoutingStats8HopsFrames_Type=Counter32
_SourceRoutingStats8HopsFrames_Object=MibTableColumn
sourceRoutingStats8HopsFrames=_SourceRoutingStats8HopsFrames_Object((1,3,6,1,2,1,16,10,6,1,21),_SourceRoutingStats8HopsFrames_Type())
sourceRoutingStats8HopsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStats8HopsFrames.setStatus(_A)
_SourceRoutingStatsMoreThan8HopsFrames_Type=Counter32
_SourceRoutingStatsMoreThan8HopsFrames_Object=MibTableColumn
sourceRoutingStatsMoreThan8HopsFrames=_SourceRoutingStatsMoreThan8HopsFrames_Object((1,3,6,1,2,1,16,10,6,1,22),_SourceRoutingStatsMoreThan8HopsFrames_Type())
sourceRoutingStatsMoreThan8HopsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceRoutingStatsMoreThan8HopsFrames.setStatus(_A)
_SourceRoutingStatsOwner_Type=OwnerString
_SourceRoutingStatsOwner_Object=MibTableColumn
sourceRoutingStatsOwner=_SourceRoutingStatsOwner_Object((1,3,6,1,2,1,16,10,6,1,23),_SourceRoutingStatsOwner_Type())
sourceRoutingStatsOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:sourceRoutingStatsOwner.setStatus(_A)
_SourceRoutingStatsStatus_Type=EntryStatus
_SourceRoutingStatsStatus_Object=MibTableColumn
sourceRoutingStatsStatus=_SourceRoutingStatsStatus_Object((1,3,6,1,2,1,16,10,6,1,24),_SourceRoutingStatsStatus_Type())
sourceRoutingStatsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sourceRoutingStatsStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'MacAddress':MacAddress,'TimeInterval':TimeInterval,'tokenRingMLStatsTable':tokenRingMLStatsTable,'tokenRingMLStatsEntry':tokenRingMLStatsEntry,_G:tokenRingMLStatsIndex,'tokenRingMLStatsDataSource':tokenRingMLStatsDataSource,'tokenRingMLStatsDropEvents':tokenRingMLStatsDropEvents,'tokenRingMLStatsMacOctets':tokenRingMLStatsMacOctets,'tokenRingMLStatsMacPkts':tokenRingMLStatsMacPkts,'tokenRingMLStatsRingPurgeEvents':tokenRingMLStatsRingPurgeEvents,'tokenRingMLStatsRingPurgePkts':tokenRingMLStatsRingPurgePkts,'tokenRingMLStatsBeaconEvents':tokenRingMLStatsBeaconEvents,'tokenRingMLStatsBeaconTime':tokenRingMLStatsBeaconTime,'tokenRingMLStatsBeaconPkts':tokenRingMLStatsBeaconPkts,'tokenRingMLStatsClaimTokenEvents':tokenRingMLStatsClaimTokenEvents,'tokenRingMLStatsClaimTokenPkts':tokenRingMLStatsClaimTokenPkts,'tokenRingMLStatsNAUNChanges':tokenRingMLStatsNAUNChanges,'tokenRingMLStatsLineErrors':tokenRingMLStatsLineErrors,'tokenRingMLStatsInternalErrors':tokenRingMLStatsInternalErrors,'tokenRingMLStatsBurstErrors':tokenRingMLStatsBurstErrors,'tokenRingMLStatsACErrors':tokenRingMLStatsACErrors,'tokenRingMLStatsAbortErrors':tokenRingMLStatsAbortErrors,'tokenRingMLStatsLostFrameErrors':tokenRingMLStatsLostFrameErrors,'tokenRingMLStatsCongestionErrors':tokenRingMLStatsCongestionErrors,'tokenRingMLStatsFrameCopiedErrors':tokenRingMLStatsFrameCopiedErrors,'tokenRingMLStatsFrequencyErrors':tokenRingMLStatsFrequencyErrors,'tokenRingMLStatsTokenErrors':tokenRingMLStatsTokenErrors,'tokenRingMLStatsSoftErrorReports':tokenRingMLStatsSoftErrorReports,'tokenRingMLStatsRingPollEvents':tokenRingMLStatsRingPollEvents,'tokenRingMLStatsOwner':tokenRingMLStatsOwner,'tokenRingMLStatsStatus':tokenRingMLStatsStatus,'tokenRingPStatsTable':tokenRingPStatsTable,'tokenRingPStatsEntry':tokenRingPStatsEntry,_H:tokenRingPStatsIndex,'tokenRingPStatsDataSource':tokenRingPStatsDataSource,'tokenRingPStatsDropEvents':tokenRingPStatsDropEvents,'tokenRingPStatsDataOctets':tokenRingPStatsDataOctets,'tokenRingPStatsDataPkts':tokenRingPStatsDataPkts,'tokenRingPStatsDataBroadcastPkts':tokenRingPStatsDataBroadcastPkts,'tokenRingPStatsDataMulticastPkts':tokenRingPStatsDataMulticastPkts,'tokenRingPStatsDataPkts18to63Octets':tokenRingPStatsDataPkts18to63Octets,'tokenRingPStatsDataPkts64to127Octets':tokenRingPStatsDataPkts64to127Octets,'tokenRingPStatsDataPkts128to255Octets':tokenRingPStatsDataPkts128to255Octets,'tokenRingPStatsDataPkts256to511Octets':tokenRingPStatsDataPkts256to511Octets,'tokenRingPStatsDataPkts512to1023Octets':tokenRingPStatsDataPkts512to1023Octets,'tokenRingPStatsDataPkts1024to2047Octets':tokenRingPStatsDataPkts1024to2047Octets,'tokenRingPStatsDataPkts2048to4095Octets':tokenRingPStatsDataPkts2048to4095Octets,'tokenRingPStatsDataPkts4096to8191Octets':tokenRingPStatsDataPkts4096to8191Octets,'tokenRingPStatsDataPkts8192to18000Octets':tokenRingPStatsDataPkts8192to18000Octets,'tokenRingPStatsDataPktsGreaterThan18000Octets':tokenRingPStatsDataPktsGreaterThan18000Octets,'tokenRingPStatsOwner':tokenRingPStatsOwner,'tokenRingPStatsStatus':tokenRingPStatsStatus,'tokenRingMLHistoryTable':tokenRingMLHistoryTable,'tokenRingMLHistoryEntry':tokenRingMLHistoryEntry,_I:tokenRingMLHistoryIndex,_J:tokenRingMLHistorySampleIndex,'tokenRingMLHistoryIntervalStart':tokenRingMLHistoryIntervalStart,'tokenRingMLHistoryDropEvents':tokenRingMLHistoryDropEvents,'tokenRingMLHistoryMacOctets':tokenRingMLHistoryMacOctets,'tokenRingMLHistoryMacPkts':tokenRingMLHistoryMacPkts,'tokenRingMLHistoryRingPurgeEvents':tokenRingMLHistoryRingPurgeEvents,'tokenRingMLHistoryRingPurgePkts':tokenRingMLHistoryRingPurgePkts,'tokenRingMLHistoryBeaconEvents':tokenRingMLHistoryBeaconEvents,'tokenRingMLHistoryBeaconTime':tokenRingMLHistoryBeaconTime,'tokenRingMLHistoryBeaconPkts':tokenRingMLHistoryBeaconPkts,'tokenRingMLHistoryClaimTokenEvents':tokenRingMLHistoryClaimTokenEvents,'tokenRingMLHistoryClaimTokenPkts':tokenRingMLHistoryClaimTokenPkts,'tokenRingMLHistoryNAUNChanges':tokenRingMLHistoryNAUNChanges,'tokenRingMLHistoryLineErrors':tokenRingMLHistoryLineErrors,'tokenRingMLHistoryInternalErrors':tokenRingMLHistoryInternalErrors,'tokenRingMLHistoryBurstErrors':tokenRingMLHistoryBurstErrors,'tokenRingMLHistoryACErrors':tokenRingMLHistoryACErrors,'tokenRingMLHistoryAbortErrors':tokenRingMLHistoryAbortErrors,'tokenRingMLHistoryLostFrameErrors':tokenRingMLHistoryLostFrameErrors,'tokenRingMLHistoryCongestionErrors':tokenRingMLHistoryCongestionErrors,'tokenRingMLHistoryFrameCopiedErrors':tokenRingMLHistoryFrameCopiedErrors,'tokenRingMLHistoryFrequencyErrors':tokenRingMLHistoryFrequencyErrors,'tokenRingMLHistoryTokenErrors':tokenRingMLHistoryTokenErrors,'tokenRingMLHistorySoftErrorReports':tokenRingMLHistorySoftErrorReports,'tokenRingMLHistoryRingPollEvents':tokenRingMLHistoryRingPollEvents,'tokenRingMLHistoryActiveStations':tokenRingMLHistoryActiveStations,'tokenRingPHistoryTable':tokenRingPHistoryTable,'tokenRingPHistoryEntry':tokenRingPHistoryEntry,_K:tokenRingPHistoryIndex,_L:tokenRingPHistorySampleIndex,'tokenRingPHistoryIntervalStart':tokenRingPHistoryIntervalStart,'tokenRingPHistoryDropEvents':tokenRingPHistoryDropEvents,'tokenRingPHistoryDataOctets':tokenRingPHistoryDataOctets,'tokenRingPHistoryDataPkts':tokenRingPHistoryDataPkts,'tokenRingPHistoryDataBroadcastPkts':tokenRingPHistoryDataBroadcastPkts,'tokenRingPHistoryDataMulticastPkts':tokenRingPHistoryDataMulticastPkts,'tokenRingPHistoryDataPkts18to63Octets':tokenRingPHistoryDataPkts18to63Octets,'tokenRingPHistoryDataPkts64to127Octets':tokenRingPHistoryDataPkts64to127Octets,'tokenRingPHistoryDataPkts128to255Octets':tokenRingPHistoryDataPkts128to255Octets,'tokenRingPHistoryDataPkts256to511Octets':tokenRingPHistoryDataPkts256to511Octets,'tokenRingPHistoryDataPkts512to1023Octets':tokenRingPHistoryDataPkts512to1023Octets,'tokenRingPHistoryDataPkts1024to2047Octets':tokenRingPHistoryDataPkts1024to2047Octets,'tokenRingPHistoryDataPkts2048to4095Octets':tokenRingPHistoryDataPkts2048to4095Octets,'tokenRingPHistoryDataPkts4096to8191Octets':tokenRingPHistoryDataPkts4096to8191Octets,'tokenRingPHistoryDataPkts8192to18000Octets':tokenRingPHistoryDataPkts8192to18000Octets,'tokenRingPHistoryDataPktsGreaterThan18000Octets':tokenRingPHistoryDataPktsGreaterThan18000Octets,'tokenRing':tokenRing,'ringStationControlTable':ringStationControlTable,'ringStationControlEntry':ringStationControlEntry,_M:ringStationControlIfIndex,'ringStationControlTableSize':ringStationControlTableSize,'ringStationControlActiveStations':ringStationControlActiveStations,'ringStationControlRingState':ringStationControlRingState,'ringStationControlBeaconSender':ringStationControlBeaconSender,'ringStationControlBeaconNAUN':ringStationControlBeaconNAUN,'ringStationControlActiveMonitor':ringStationControlActiveMonitor,'ringStationControlOrderChanges':ringStationControlOrderChanges,'ringStationControlOwner':ringStationControlOwner,'ringStationControlStatus':ringStationControlStatus,'ringStationTable':ringStationTable,'ringStationEntry':ringStationEntry,_N:ringStationIfIndex,_O:ringStationMacAddress,'ringStationLastNAUN':ringStationLastNAUN,'ringStationStationStatus':ringStationStationStatus,'ringStationLastEnterTime':ringStationLastEnterTime,'ringStationLastExitTime':ringStationLastExitTime,'ringStationDuplicateAddresses':ringStationDuplicateAddresses,'ringStationInLineErrors':ringStationInLineErrors,'ringStationOutLineErrors':ringStationOutLineErrors,'ringStationInternalErrors':ringStationInternalErrors,'ringStationInBurstErrors':ringStationInBurstErrors,'ringStationOutBurstErrors':ringStationOutBurstErrors,'ringStationACErrors':ringStationACErrors,'ringStationAbortErrors':ringStationAbortErrors,'ringStationLostFrameErrors':ringStationLostFrameErrors,'ringStationCongestionErrors':ringStationCongestionErrors,'ringStationFrameCopiedErrors':ringStationFrameCopiedErrors,'ringStationFrequencyErrors':ringStationFrequencyErrors,'ringStationTokenErrors':ringStationTokenErrors,'ringStationInBeaconErrors':ringStationInBeaconErrors,'ringStationOutBeaconErrors':ringStationOutBeaconErrors,'ringStationInsertions':ringStationInsertions,'ringStationOrderTable':ringStationOrderTable,'ringStationOrderEntry':ringStationOrderEntry,_P:ringStationOrderIfIndex,_Q:ringStationOrderOrderIndex,'ringStationOrderMacAddress':ringStationOrderMacAddress,'ringStationConfigControlTable':ringStationConfigControlTable,'ringStationConfigControlEntry':ringStationConfigControlEntry,_R:ringStationConfigControlIfIndex,_S:ringStationConfigControlMacAddress,'ringStationConfigControlRemove':ringStationConfigControlRemove,'ringStationConfigControlUpdateStats':ringStationConfigControlUpdateStats,'ringStationConfigTable':ringStationConfigTable,'ringStationConfigEntry':ringStationConfigEntry,_U:ringStationConfigIfIndex,_V:ringStationConfigMacAddress,'ringStationConfigUpdateTime':ringStationConfigUpdateTime,'ringStationConfigLocation':ringStationConfigLocation,'ringStationConfigMicrocode':ringStationConfigMicrocode,'ringStationConfigGroupAddress':ringStationConfigGroupAddress,'ringStationConfigFunctionalAddress':ringStationConfigFunctionalAddress,'sourceRoutingStatsTable':sourceRoutingStatsTable,'sourceRoutingStatsEntry':sourceRoutingStatsEntry,_W:sourceRoutingStatsIfIndex,'sourceRoutingStatsRingNumber':sourceRoutingStatsRingNumber,'sourceRoutingStatsInFrames':sourceRoutingStatsInFrames,'sourceRoutingStatsOutFrames':sourceRoutingStatsOutFrames,'sourceRoutingStatsThroughFrames':sourceRoutingStatsThroughFrames,'sourceRoutingStatsAllRoutesBroadcastFrames':sourceRoutingStatsAllRoutesBroadcastFrames,'sourceRoutingStatsSingleRouteBroadcastFrames':sourceRoutingStatsSingleRouteBroadcastFrames,'sourceRoutingStatsInOctets':sourceRoutingStatsInOctets,'sourceRoutingStatsOutOctets':sourceRoutingStatsOutOctets,'sourceRoutingStatsThroughOctets':sourceRoutingStatsThroughOctets,'sourceRoutingStatsAllRoutesBroadcastOctets':sourceRoutingStatsAllRoutesBroadcastOctets,'sourceRoutingStatsSingleRoutesBroadcastOctets':sourceRoutingStatsSingleRoutesBroadcastOctets,'sourceRoutingStatsLocalLLCFrames':sourceRoutingStatsLocalLLCFrames,'sourceRoutingStats1HopFrames':sourceRoutingStats1HopFrames,'sourceRoutingStats2HopsFrames':sourceRoutingStats2HopsFrames,'sourceRoutingStats3HopsFrames':sourceRoutingStats3HopsFrames,'sourceRoutingStats4HopsFrames':sourceRoutingStats4HopsFrames,'sourceRoutingStats5HopsFrames':sourceRoutingStats5HopsFrames,'sourceRoutingStats6HopsFrames':sourceRoutingStats6HopsFrames,'sourceRoutingStats7HopsFrames':sourceRoutingStats7HopsFrames,'sourceRoutingStats8HopsFrames':sourceRoutingStats8HopsFrames,'sourceRoutingStatsMoreThan8HopsFrames':sourceRoutingStatsMoreThan8HopsFrames,'sourceRoutingStatsOwner':sourceRoutingStatsOwner,'sourceRoutingStatsStatus':sourceRoutingStatsStatus})