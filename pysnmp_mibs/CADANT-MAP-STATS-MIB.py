_J='cadMapStatsBwRequestQueuesPriorityId'
_I='cadMapStatsBwRequestQueuesFlowState'
_H='cadMapStatsMSlotsPerIUCId'
_G='Unsigned32'
_F='not-accessible'
_E='CADANT-MAP-STATS-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadSpectrum,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadSpectrum')
FlowActivityState,=mibBuilder.importSymbols('CADANT-TC','FlowActivityState')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cadMapStatsMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,15,10))
if mibBuilder.loadTexts:cadMapStatsMib.setRevisions(('2008-10-23 00:00','2004-01-17 00:00','2004-01-16 00:00','2003-08-11 00:00','2003-08-06 00:00','2003-08-04 00:00','2003-04-04 00:00'))
class CadMapStatsIUCTypeId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
class CadMapStatsBwRequestQueuesPriorityId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('docsispri0',0),('docsispri1',1),('docsispri2',2),('docsispri3',3),('docsispri4',4),('docsispri5',5),('docsispri6',6),('docsispri7',7)))
_CadMapStatsBaseTable_Object=MibTable
cadMapStatsBaseTable=_CadMapStatsBaseTable_Object((1,3,6,1,4,1,4998,1,1,15,10,1))
if mibBuilder.loadTexts:cadMapStatsBaseTable.setStatus(_A)
_CadMapStatsBaseEntry_Object=MibTableRow
cadMapStatsBaseEntry=_CadMapStatsBaseEntry_Object((1,3,6,1,4,1,4998,1,1,15,10,1,1))
cadMapStatsBaseEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cadMapStatsBaseEntry.setStatus(_A)
_CadMapStatsTotalMapsSent_Type=Counter64
_CadMapStatsTotalMapsSent_Object=MibTableColumn
cadMapStatsTotalMapsSent=_CadMapStatsTotalMapsSent_Object((1,3,6,1,4,1,4998,1,1,15,10,1,1,1),_CadMapStatsTotalMapsSent_Type())
cadMapStatsTotalMapsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalMapsSent.setStatus(_A)
_CadMapStatsTotalFragmentedGrants_Type=Counter64
_CadMapStatsTotalFragmentedGrants_Object=MibTableColumn
cadMapStatsTotalFragmentedGrants=_CadMapStatsTotalFragmentedGrants_Object((1,3,6,1,4,1,4998,1,1,15,10,1,1,2),_CadMapStatsTotalFragmentedGrants_Type())
cadMapStatsTotalFragmentedGrants.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalFragmentedGrants.setStatus(_A)
_CadMapStatsTotalUgsQiTransitions_Type=Counter64
_CadMapStatsTotalUgsQiTransitions_Object=MibTableColumn
cadMapStatsTotalUgsQiTransitions=_CadMapStatsTotalUgsQiTransitions_Object((1,3,6,1,4,1,4998,1,1,15,10,1,1,3),_CadMapStatsTotalUgsQiTransitions_Type())
cadMapStatsTotalUgsQiTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalUgsQiTransitions.setStatus(_A)
_CadMapStatsTotalUgsadTransitions_Type=Counter64
_CadMapStatsTotalUgsadTransitions_Object=MibTableColumn
cadMapStatsTotalUgsadTransitions=_CadMapStatsTotalUgsadTransitions_Object((1,3,6,1,4,1,4998,1,1,15,10,1,1,4),_CadMapStatsTotalUgsadTransitions_Type())
cadMapStatsTotalUgsadTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalUgsadTransitions.setStatus(_A)
_CadMapStatsTotalUgsEHdrsSw_Type=Counter64
_CadMapStatsTotalUgsEHdrsSw_Object=MibTableColumn
cadMapStatsTotalUgsEHdrsSw=_CadMapStatsTotalUgsEHdrsSw_Object((1,3,6,1,4,1,4998,1,1,15,10,1,1,5),_CadMapStatsTotalUgsEHdrsSw_Type())
cadMapStatsTotalUgsEHdrsSw.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalUgsEHdrsSw.setStatus(_A)
_CadMapStatsTotalBadMaps_Type=Counter64
_CadMapStatsTotalBadMaps_Object=MibTableColumn
cadMapStatsTotalBadMaps=_CadMapStatsTotalBadMaps_Object((1,3,6,1,4,1,4998,1,1,15,10,1,1,6),_CadMapStatsTotalBadMaps_Type())
cadMapStatsTotalBadMaps.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalBadMaps.setStatus(_A)
_CadMapStatsMSlotsTable_Object=MibTable
cadMapStatsMSlotsTable=_CadMapStatsMSlotsTable_Object((1,3,6,1,4,1,4998,1,1,15,10,2))
if mibBuilder.loadTexts:cadMapStatsMSlotsTable.setStatus(_A)
_CadMapStatsMSlotsEntry_Object=MibTableRow
cadMapStatsMSlotsEntry=_CadMapStatsMSlotsEntry_Object((1,3,6,1,4,1,4998,1,1,15,10,2,1))
cadMapStatsMSlotsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cadMapStatsMSlotsEntry.setStatus(_A)
_CadMapStatsTotalMSlots_Type=Counter64
_CadMapStatsTotalMSlots_Object=MibTableColumn
cadMapStatsTotalMSlots=_CadMapStatsTotalMSlots_Object((1,3,6,1,4,1,4998,1,1,15,10,2,1,1),_CadMapStatsTotalMSlots_Type())
cadMapStatsTotalMSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalMSlots.setStatus(_A)
_CadMapStatsTotalUCastGrantedMSlots_Type=Counter64
_CadMapStatsTotalUCastGrantedMSlots_Object=MibTableColumn
cadMapStatsTotalUCastGrantedMSlots=_CadMapStatsTotalUCastGrantedMSlots_Object((1,3,6,1,4,1,4998,1,1,15,10,2,1,2),_CadMapStatsTotalUCastGrantedMSlots_Type())
cadMapStatsTotalUCastGrantedMSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalUCastGrantedMSlots.setStatus(_A)
_CadMapStatsTotalBwRequestMSlots_Type=Counter64
_CadMapStatsTotalBwRequestMSlots_Object=MibTableColumn
cadMapStatsTotalBwRequestMSlots=_CadMapStatsTotalBwRequestMSlots_Object((1,3,6,1,4,1,4998,1,1,15,10,2,1,3),_CadMapStatsTotalBwRequestMSlots_Type())
cadMapStatsTotalBwRequestMSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalBwRequestMSlots.setStatus(_A)
_CadMapStatsTotalSkippedMSlots_Type=Counter64
_CadMapStatsTotalSkippedMSlots_Object=MibTableColumn
cadMapStatsTotalSkippedMSlots=_CadMapStatsTotalSkippedMSlots_Object((1,3,6,1,4,1,4998,1,1,15,10,2,1,4),_CadMapStatsTotalSkippedMSlots_Type())
cadMapStatsTotalSkippedMSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalSkippedMSlots.setStatus(_A)
_CadMapStatsTotalLogicalNullPadMSlots_Type=Counter64
_CadMapStatsTotalLogicalNullPadMSlots_Object=MibTableColumn
cadMapStatsTotalLogicalNullPadMSlots=_CadMapStatsTotalLogicalNullPadMSlots_Object((1,3,6,1,4,1,4998,1,1,15,10,2,1,5),_CadMapStatsTotalLogicalNullPadMSlots_Type())
cadMapStatsTotalLogicalNullPadMSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalLogicalNullPadMSlots.setStatus(_A)
_CadMapStatsMSlotsPerIUCTable_Object=MibTable
cadMapStatsMSlotsPerIUCTable=_CadMapStatsMSlotsPerIUCTable_Object((1,3,6,1,4,1,4998,1,1,15,10,3))
if mibBuilder.loadTexts:cadMapStatsMSlotsPerIUCTable.setStatus(_A)
_CadMapStatsMSlotsPerIUCEntry_Object=MibTableRow
cadMapStatsMSlotsPerIUCEntry=_CadMapStatsMSlotsPerIUCEntry_Object((1,3,6,1,4,1,4998,1,1,15,10,3,1))
cadMapStatsMSlotsPerIUCEntry.setIndexNames((0,_C,_D),(0,_E,_H))
if mibBuilder.loadTexts:cadMapStatsMSlotsPerIUCEntry.setStatus(_A)
_CadMapStatsMSlotsPerIUCId_Type=CadMapStatsIUCTypeId
_CadMapStatsMSlotsPerIUCId_Object=MibTableColumn
cadMapStatsMSlotsPerIUCId=_CadMapStatsMSlotsPerIUCId_Object((1,3,6,1,4,1,4998,1,1,15,10,3,1,1),_CadMapStatsMSlotsPerIUCId_Type())
cadMapStatsMSlotsPerIUCId.setMaxAccess(_F)
if mibBuilder.loadTexts:cadMapStatsMSlotsPerIUCId.setStatus(_A)
_CadMapStatsGrantedBCastMSlots_Type=Counter64
_CadMapStatsGrantedBCastMSlots_Object=MibTableColumn
cadMapStatsGrantedBCastMSlots=_CadMapStatsGrantedBCastMSlots_Object((1,3,6,1,4,1,4998,1,1,15,10,3,1,2),_CadMapStatsGrantedBCastMSlots_Type())
cadMapStatsGrantedBCastMSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsGrantedBCastMSlots.setStatus(_A)
_CadMapStatsGrantedMCastMSlots_Type=Counter64
_CadMapStatsGrantedMCastMSlots_Object=MibTableColumn
cadMapStatsGrantedMCastMSlots=_CadMapStatsGrantedMCastMSlots_Object((1,3,6,1,4,1,4998,1,1,15,10,3,1,3),_CadMapStatsGrantedMCastMSlots_Type())
cadMapStatsGrantedMCastMSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsGrantedMCastMSlots.setStatus(_A)
_CadMapStatsGrantedUCastMSlots_Type=Counter64
_CadMapStatsGrantedUCastMSlots_Object=MibTableColumn
cadMapStatsGrantedUCastMSlots=_CadMapStatsGrantedUCastMSlots_Object((1,3,6,1,4,1,4998,1,1,15,10,3,1,4),_CadMapStatsGrantedUCastMSlots_Type())
cadMapStatsGrantedUCastMSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsGrantedUCastMSlots.setStatus(_A)
_CadMapStatsGrantedZeroSidMSlots_Type=Counter64
_CadMapStatsGrantedZeroSidMSlots_Object=MibTableColumn
cadMapStatsGrantedZeroSidMSlots=_CadMapStatsGrantedZeroSidMSlots_Object((1,3,6,1,4,1,4998,1,1,15,10,3,1,5),_CadMapStatsGrantedZeroSidMSlots_Type())
cadMapStatsGrantedZeroSidMSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsGrantedZeroSidMSlots.setStatus(_A)
_CadMapStatsBwRequestsTable_Object=MibTable
cadMapStatsBwRequestsTable=_CadMapStatsBwRequestsTable_Object((1,3,6,1,4,1,4998,1,1,15,10,4))
if mibBuilder.loadTexts:cadMapStatsBwRequestsTable.setStatus(_A)
_CadMapStatsBwRequestsEntry_Object=MibTableRow
cadMapStatsBwRequestsEntry=_CadMapStatsBwRequestsEntry_Object((1,3,6,1,4,1,4998,1,1,15,10,4,1))
cadMapStatsBwRequestsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cadMapStatsBwRequestsEntry.setStatus(_A)
_CadMapStatsTotalBwRequests_Type=Counter64
_CadMapStatsTotalBwRequests_Object=MibTableColumn
cadMapStatsTotalBwRequests=_CadMapStatsTotalBwRequests_Object((1,3,6,1,4,1,4998,1,1,15,10,4,1,1),_CadMapStatsTotalBwRequests_Type())
cadMapStatsTotalBwRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalBwRequests.setStatus(_A)
_CadMapStatsTotalBwRequestSchedulerDrops_Type=Counter64
_CadMapStatsTotalBwRequestSchedulerDrops_Object=MibTableColumn
cadMapStatsTotalBwRequestSchedulerDrops=_CadMapStatsTotalBwRequestSchedulerDrops_Object((1,3,6,1,4,1,4998,1,1,15,10,4,1,2),_CadMapStatsTotalBwRequestSchedulerDrops_Type())
cadMapStatsTotalBwRequestSchedulerDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalBwRequestSchedulerDrops.setStatus(_A)
_CadMapStatsTotalBwRequestSuperGreedyDrops_Type=Counter64
_CadMapStatsTotalBwRequestSuperGreedyDrops_Object=MibTableColumn
cadMapStatsTotalBwRequestSuperGreedyDrops=_CadMapStatsTotalBwRequestSuperGreedyDrops_Object((1,3,6,1,4,1,4998,1,1,15,10,4,1,3),_CadMapStatsTotalBwRequestSuperGreedyDrops_Type())
cadMapStatsTotalBwRequestSuperGreedyDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalBwRequestSuperGreedyDrops.setStatus(_A)
_CadMapStatsPeakBwRequestSize_Type=Unsigned32
_CadMapStatsPeakBwRequestSize_Object=MibTableColumn
cadMapStatsPeakBwRequestSize=_CadMapStatsPeakBwRequestSize_Object((1,3,6,1,4,1,4998,1,1,15,10,4,1,4),_CadMapStatsPeakBwRequestSize_Type())
cadMapStatsPeakBwRequestSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsPeakBwRequestSize.setStatus(_A)
_CadMapStatsPeakBwRequestsPerMap_Type=Unsigned32
_CadMapStatsPeakBwRequestsPerMap_Object=MibTableColumn
cadMapStatsPeakBwRequestsPerMap=_CadMapStatsPeakBwRequestsPerMap_Object((1,3,6,1,4,1,4998,1,1,15,10,4,1,5),_CadMapStatsPeakBwRequestsPerMap_Type())
cadMapStatsPeakBwRequestsPerMap.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsPeakBwRequestsPerMap.setStatus(_A)
_CadMapStatsGrantPendingsTable_Object=MibTable
cadMapStatsGrantPendingsTable=_CadMapStatsGrantPendingsTable_Object((1,3,6,1,4,1,4998,1,1,15,10,5))
if mibBuilder.loadTexts:cadMapStatsGrantPendingsTable.setStatus(_A)
_CadMapStatsGrantPendingsEntry_Object=MibTableRow
cadMapStatsGrantPendingsEntry=_CadMapStatsGrantPendingsEntry_Object((1,3,6,1,4,1,4998,1,1,15,10,5,1))
cadMapStatsGrantPendingsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cadMapStatsGrantPendingsEntry.setStatus(_A)
_CadMapStatsTotalGrantPendings_Type=Counter64
_CadMapStatsTotalGrantPendings_Object=MibTableColumn
cadMapStatsTotalGrantPendings=_CadMapStatsTotalGrantPendings_Object((1,3,6,1,4,1,4998,1,1,15,10,5,1,1),_CadMapStatsTotalGrantPendings_Type())
cadMapStatsTotalGrantPendings.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalGrantPendings.setStatus(_A)
_CadMapStatsTotalGrantPendingDrops_Type=Counter64
_CadMapStatsTotalGrantPendingDrops_Object=MibTableColumn
cadMapStatsTotalGrantPendingDrops=_CadMapStatsTotalGrantPendingDrops_Object((1,3,6,1,4,1,4998,1,1,15,10,5,1,2),_CadMapStatsTotalGrantPendingDrops_Type())
cadMapStatsTotalGrantPendingDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalGrantPendingDrops.setStatus(_A)
_CadMapStatsTotalGrantPendingPromos_Type=Counter64
_CadMapStatsTotalGrantPendingPromos_Object=MibTableColumn
cadMapStatsTotalGrantPendingPromos=_CadMapStatsTotalGrantPendingPromos_Object((1,3,6,1,4,1,4998,1,1,15,10,5,1,3),_CadMapStatsTotalGrantPendingPromos_Type())
cadMapStatsTotalGrantPendingPromos.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsTotalGrantPendingPromos.setStatus(_A)
_CadMapStatsPeakGrantPendingsPerMap_Type=Unsigned32
_CadMapStatsPeakGrantPendingsPerMap_Object=MibTableColumn
cadMapStatsPeakGrantPendingsPerMap=_CadMapStatsPeakGrantPendingsPerMap_Object((1,3,6,1,4,1,4998,1,1,15,10,5,1,4),_CadMapStatsPeakGrantPendingsPerMap_Type())
cadMapStatsPeakGrantPendingsPerMap.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsPeakGrantPendingsPerMap.setStatus(_A)
_CadMapStatsBwRequestQueuesTable_Object=MibTable
cadMapStatsBwRequestQueuesTable=_CadMapStatsBwRequestQueuesTable_Object((1,3,6,1,4,1,4998,1,1,15,10,6))
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesTable.setStatus(_A)
_CadMapStatsBwRequestQueuesEntry_Object=MibTableRow
cadMapStatsBwRequestQueuesEntry=_CadMapStatsBwRequestQueuesEntry_Object((1,3,6,1,4,1,4998,1,1,15,10,6,1))
cadMapStatsBwRequestQueuesEntry.setIndexNames((0,_C,_D),(0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesEntry.setStatus(_A)
_CadMapStatsBwRequestQueuesFlowState_Type=FlowActivityState
_CadMapStatsBwRequestQueuesFlowState_Object=MibTableColumn
cadMapStatsBwRequestQueuesFlowState=_CadMapStatsBwRequestQueuesFlowState_Object((1,3,6,1,4,1,4998,1,1,15,10,6,1,1),_CadMapStatsBwRequestQueuesFlowState_Type())
cadMapStatsBwRequestQueuesFlowState.setMaxAccess(_F)
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesFlowState.setStatus(_A)
_CadMapStatsBwRequestQueuesPriorityId_Type=CadMapStatsBwRequestQueuesPriorityId
_CadMapStatsBwRequestQueuesPriorityId_Object=MibTableColumn
cadMapStatsBwRequestQueuesPriorityId=_CadMapStatsBwRequestQueuesPriorityId_Object((1,3,6,1,4,1,4998,1,1,15,10,6,1,2),_CadMapStatsBwRequestQueuesPriorityId_Type())
cadMapStatsBwRequestQueuesPriorityId.setMaxAccess(_F)
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesPriorityId.setStatus(_A)
_CadMapStatsBwRequestQueuesNumAdds_Type=Counter64
_CadMapStatsBwRequestQueuesNumAdds_Object=MibTableColumn
cadMapStatsBwRequestQueuesNumAdds=_CadMapStatsBwRequestQueuesNumAdds_Object((1,3,6,1,4,1,4998,1,1,15,10,6,1,3),_CadMapStatsBwRequestQueuesNumAdds_Type())
cadMapStatsBwRequestQueuesNumAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesNumAdds.setStatus(_A)
_CadMapStatsBwRequestQueuesNumDrops_Type=Counter64
_CadMapStatsBwRequestQueuesNumDrops_Object=MibTableColumn
cadMapStatsBwRequestQueuesNumDrops=_CadMapStatsBwRequestQueuesNumDrops_Object((1,3,6,1,4,1,4998,1,1,15,10,6,1,4),_CadMapStatsBwRequestQueuesNumDrops_Type())
cadMapStatsBwRequestQueuesNumDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesNumDrops.setStatus(_A)
_CadMapStatsBwRequestQueuesNumPendings_Type=Counter64
_CadMapStatsBwRequestQueuesNumPendings_Object=MibTableColumn
cadMapStatsBwRequestQueuesNumPendings=_CadMapStatsBwRequestQueuesNumPendings_Object((1,3,6,1,4,1,4998,1,1,15,10,6,1,5),_CadMapStatsBwRequestQueuesNumPendings_Type())
cadMapStatsBwRequestQueuesNumPendings.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesNumPendings.setStatus(_A)
_CadMapStatsBwRequestQueuesNumPromos_Type=Counter64
_CadMapStatsBwRequestQueuesNumPromos_Object=MibTableColumn
cadMapStatsBwRequestQueuesNumPromos=_CadMapStatsBwRequestQueuesNumPromos_Object((1,3,6,1,4,1,4998,1,1,15,10,6,1,6),_CadMapStatsBwRequestQueuesNumPromos_Type())
cadMapStatsBwRequestQueuesNumPromos.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesNumPromos.setStatus(_A)
_CadMapStatsBwRequestQueuesNumElements_Type=Unsigned32
_CadMapStatsBwRequestQueuesNumElements_Object=MibTableColumn
cadMapStatsBwRequestQueuesNumElements=_CadMapStatsBwRequestQueuesNumElements_Object((1,3,6,1,4,1,4998,1,1,15,10,6,1,7),_CadMapStatsBwRequestQueuesNumElements_Type())
cadMapStatsBwRequestQueuesNumElements.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesNumElements.setStatus(_A)
_CadMapStatsBwRequestQueuesLatencySum_Type=Counter64
_CadMapStatsBwRequestQueuesLatencySum_Object=MibTableColumn
cadMapStatsBwRequestQueuesLatencySum=_CadMapStatsBwRequestQueuesLatencySum_Object((1,3,6,1,4,1,4998,1,1,15,10,6,1,8),_CadMapStatsBwRequestQueuesLatencySum_Type())
cadMapStatsBwRequestQueuesLatencySum.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsBwRequestQueuesLatencySum.setStatus(_A)
_CadMapStatsPeriodicFlowsTable_Object=MibTable
cadMapStatsPeriodicFlowsTable=_CadMapStatsPeriodicFlowsTable_Object((1,3,6,1,4,1,4998,1,1,15,10,7))
if mibBuilder.loadTexts:cadMapStatsPeriodicFlowsTable.setStatus(_A)
_CadMapStatsPeriodicFlowsEntry_Object=MibTableRow
cadMapStatsPeriodicFlowsEntry=_CadMapStatsPeriodicFlowsEntry_Object((1,3,6,1,4,1,4998,1,1,15,10,7,1))
cadMapStatsPeriodicFlowsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cadMapStatsPeriodicFlowsEntry.setStatus(_A)
_CadMapStatsNumNrtpsFlows_Type=Unsigned32
_CadMapStatsNumNrtpsFlows_Object=MibTableColumn
cadMapStatsNumNrtpsFlows=_CadMapStatsNumNrtpsFlows_Object((1,3,6,1,4,1,4998,1,1,15,10,7,1,1),_CadMapStatsNumNrtpsFlows_Type())
cadMapStatsNumNrtpsFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsNumNrtpsFlows.setStatus(_A)
_CadMapStatsNumRtpsFlows_Type=Unsigned32
_CadMapStatsNumRtpsFlows_Object=MibTableColumn
cadMapStatsNumRtpsFlows=_CadMapStatsNumRtpsFlows_Object((1,3,6,1,4,1,4998,1,1,15,10,7,1,2),_CadMapStatsNumRtpsFlows_Type())
cadMapStatsNumRtpsFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsNumRtpsFlows.setStatus(_A)
_CadMapStatsNumUgsadActiveFlows_Type=Unsigned32
_CadMapStatsNumUgsadActiveFlows_Object=MibTableColumn
cadMapStatsNumUgsadActiveFlows=_CadMapStatsNumUgsadActiveFlows_Object((1,3,6,1,4,1,4998,1,1,15,10,7,1,3),_CadMapStatsNumUgsadActiveFlows_Type())
cadMapStatsNumUgsadActiveFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsNumUgsadActiveFlows.setStatus(_A)
_CadMapStatsNumUgsadPollingFlows_Type=Unsigned32
_CadMapStatsNumUgsadPollingFlows_Object=MibTableColumn
cadMapStatsNumUgsadPollingFlows=_CadMapStatsNumUgsadPollingFlows_Object((1,3,6,1,4,1,4998,1,1,15,10,7,1,4),_CadMapStatsNumUgsadPollingFlows_Type())
cadMapStatsNumUgsadPollingFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsNumUgsadPollingFlows.setStatus(_A)
_CadMapStatsNumUgsFlows_Type=Unsigned32
_CadMapStatsNumUgsFlows_Object=MibTableColumn
cadMapStatsNumUgsFlows=_CadMapStatsNumUgsFlows_Object((1,3,6,1,4,1,4998,1,1,15,10,7,1,5),_CadMapStatsNumUgsFlows_Type())
cadMapStatsNumUgsFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsNumUgsFlows.setStatus(_A)
_CadMapStatsNumBEPollingFlows_Type=Unsigned32
_CadMapStatsNumBEPollingFlows_Object=MibTableColumn
cadMapStatsNumBEPollingFlows=_CadMapStatsNumBEPollingFlows_Object((1,3,6,1,4,1,4998,1,1,15,10,7,1,6),_CadMapStatsNumBEPollingFlows_Type())
cadMapStatsNumBEPollingFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsNumBEPollingFlows.setStatus(_A)
class _CadMapStatsNumBEFastPollingFlows_Type(Unsigned32):defaultValue=0
_CadMapStatsNumBEFastPollingFlows_Type.__name__=_G
_CadMapStatsNumBEFastPollingFlows_Object=MibTableColumn
cadMapStatsNumBEFastPollingFlows=_CadMapStatsNumBEFastPollingFlows_Object((1,3,6,1,4,1,4998,1,1,15,10,7,1,7),_CadMapStatsNumBEFastPollingFlows_Type())
cadMapStatsNumBEFastPollingFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMapStatsNumBEFastPollingFlows.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'CadMapStatsIUCTypeId':CadMapStatsIUCTypeId,'CadMapStatsBwRequestQueuesPriorityId':CadMapStatsBwRequestQueuesPriorityId,'cadMapStatsMib':cadMapStatsMib,'cadMapStatsBaseTable':cadMapStatsBaseTable,'cadMapStatsBaseEntry':cadMapStatsBaseEntry,'cadMapStatsTotalMapsSent':cadMapStatsTotalMapsSent,'cadMapStatsTotalFragmentedGrants':cadMapStatsTotalFragmentedGrants,'cadMapStatsTotalUgsQiTransitions':cadMapStatsTotalUgsQiTransitions,'cadMapStatsTotalUgsadTransitions':cadMapStatsTotalUgsadTransitions,'cadMapStatsTotalUgsEHdrsSw':cadMapStatsTotalUgsEHdrsSw,'cadMapStatsTotalBadMaps':cadMapStatsTotalBadMaps,'cadMapStatsMSlotsTable':cadMapStatsMSlotsTable,'cadMapStatsMSlotsEntry':cadMapStatsMSlotsEntry,'cadMapStatsTotalMSlots':cadMapStatsTotalMSlots,'cadMapStatsTotalUCastGrantedMSlots':cadMapStatsTotalUCastGrantedMSlots,'cadMapStatsTotalBwRequestMSlots':cadMapStatsTotalBwRequestMSlots,'cadMapStatsTotalSkippedMSlots':cadMapStatsTotalSkippedMSlots,'cadMapStatsTotalLogicalNullPadMSlots':cadMapStatsTotalLogicalNullPadMSlots,'cadMapStatsMSlotsPerIUCTable':cadMapStatsMSlotsPerIUCTable,'cadMapStatsMSlotsPerIUCEntry':cadMapStatsMSlotsPerIUCEntry,_H:cadMapStatsMSlotsPerIUCId,'cadMapStatsGrantedBCastMSlots':cadMapStatsGrantedBCastMSlots,'cadMapStatsGrantedMCastMSlots':cadMapStatsGrantedMCastMSlots,'cadMapStatsGrantedUCastMSlots':cadMapStatsGrantedUCastMSlots,'cadMapStatsGrantedZeroSidMSlots':cadMapStatsGrantedZeroSidMSlots,'cadMapStatsBwRequestsTable':cadMapStatsBwRequestsTable,'cadMapStatsBwRequestsEntry':cadMapStatsBwRequestsEntry,'cadMapStatsTotalBwRequests':cadMapStatsTotalBwRequests,'cadMapStatsTotalBwRequestSchedulerDrops':cadMapStatsTotalBwRequestSchedulerDrops,'cadMapStatsTotalBwRequestSuperGreedyDrops':cadMapStatsTotalBwRequestSuperGreedyDrops,'cadMapStatsPeakBwRequestSize':cadMapStatsPeakBwRequestSize,'cadMapStatsPeakBwRequestsPerMap':cadMapStatsPeakBwRequestsPerMap,'cadMapStatsGrantPendingsTable':cadMapStatsGrantPendingsTable,'cadMapStatsGrantPendingsEntry':cadMapStatsGrantPendingsEntry,'cadMapStatsTotalGrantPendings':cadMapStatsTotalGrantPendings,'cadMapStatsTotalGrantPendingDrops':cadMapStatsTotalGrantPendingDrops,'cadMapStatsTotalGrantPendingPromos':cadMapStatsTotalGrantPendingPromos,'cadMapStatsPeakGrantPendingsPerMap':cadMapStatsPeakGrantPendingsPerMap,'cadMapStatsBwRequestQueuesTable':cadMapStatsBwRequestQueuesTable,'cadMapStatsBwRequestQueuesEntry':cadMapStatsBwRequestQueuesEntry,_I:cadMapStatsBwRequestQueuesFlowState,_J:cadMapStatsBwRequestQueuesPriorityId,'cadMapStatsBwRequestQueuesNumAdds':cadMapStatsBwRequestQueuesNumAdds,'cadMapStatsBwRequestQueuesNumDrops':cadMapStatsBwRequestQueuesNumDrops,'cadMapStatsBwRequestQueuesNumPendings':cadMapStatsBwRequestQueuesNumPendings,'cadMapStatsBwRequestQueuesNumPromos':cadMapStatsBwRequestQueuesNumPromos,'cadMapStatsBwRequestQueuesNumElements':cadMapStatsBwRequestQueuesNumElements,'cadMapStatsBwRequestQueuesLatencySum':cadMapStatsBwRequestQueuesLatencySum,'cadMapStatsPeriodicFlowsTable':cadMapStatsPeriodicFlowsTable,'cadMapStatsPeriodicFlowsEntry':cadMapStatsPeriodicFlowsEntry,'cadMapStatsNumNrtpsFlows':cadMapStatsNumNrtpsFlows,'cadMapStatsNumRtpsFlows':cadMapStatsNumRtpsFlows,'cadMapStatsNumUgsadActiveFlows':cadMapStatsNumUgsadActiveFlows,'cadMapStatsNumUgsadPollingFlows':cadMapStatsNumUgsadPollingFlows,'cadMapStatsNumUgsFlows':cadMapStatsNumUgsFlows,'cadMapStatsNumBEPollingFlows':cadMapStatsNumBEPollingFlows,'cadMapStatsNumBEFastPollingFlows':cadMapStatsNumBEFastPollingFlows})