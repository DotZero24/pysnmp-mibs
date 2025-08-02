_H='agentBGPPeerRemoteAddr'
_G='agentBGPDecProcIndex'
_F='not-accessible'
_E='agentBGPQueueIndex'
_D='Unsigned32'
_C='QUANTA-BGP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch,=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','switch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
quantaBGP=ModuleIdentity((1,3,6,1,4,1,7244,2,5))
_AgentBGPQueueGroup_ObjectIdentity=ObjectIdentity
agentBGPQueueGroup=_AgentBGPQueueGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,5,1))
_AgentBGPQueueTable_Object=MibTable
agentBGPQueueTable=_AgentBGPQueueTable_Object((1,3,6,1,4,1,7244,2,5,1,1))
if mibBuilder.loadTexts:agentBGPQueueTable.setStatus(_A)
_AgentBGPQueueEntry_Object=MibTableRow
agentBGPQueueEntry=_AgentBGPQueueEntry_Object((1,3,6,1,4,1,7244,2,5,1,1,1))
agentBGPQueueEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:agentBGPQueueEntry.setStatus(_A)
_AgentBGPQueueIndex_Type=Unsigned32
_AgentBGPQueueIndex_Object=MibTableColumn
agentBGPQueueIndex=_AgentBGPQueueIndex_Object((1,3,6,1,4,1,7244,2,5,1,1,1,1),_AgentBGPQueueIndex_Type())
agentBGPQueueIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:agentBGPQueueIndex.setStatus(_A)
_AgentBGPQueueName_Type=DisplayString
_AgentBGPQueueName_Object=MibTableColumn
agentBGPQueueName=_AgentBGPQueueName_Object((1,3,6,1,4,1,7244,2,5,1,1,1,2),_AgentBGPQueueName_Type())
agentBGPQueueName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPQueueName.setStatus(_A)
_AgentBGPQueueLength_Type=Gauge32
_AgentBGPQueueLength_Object=MibTableColumn
agentBGPQueueLength=_AgentBGPQueueLength_Object((1,3,6,1,4,1,7244,2,5,1,1,1,3),_AgentBGPQueueLength_Type())
agentBGPQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPQueueLength.setStatus(_A)
_AgentBGPQueueHigh_Type=Gauge32
_AgentBGPQueueHigh_Object=MibTableColumn
agentBGPQueueHigh=_AgentBGPQueueHigh_Object((1,3,6,1,4,1,7244,2,5,1,1,1,4),_AgentBGPQueueHigh_Type())
agentBGPQueueHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPQueueHigh.setStatus(_A)
_AgentBGPQueueDrops_Type=Counter32
_AgentBGPQueueDrops_Object=MibTableColumn
agentBGPQueueDrops=_AgentBGPQueueDrops_Object((1,3,6,1,4,1,7244,2,5,1,1,1,5),_AgentBGPQueueDrops_Type())
agentBGPQueueDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPQueueDrops.setStatus(_A)
_AgentBGPQueueLimit_Type=Unsigned32
_AgentBGPQueueLimit_Object=MibTableColumn
agentBGPQueueLimit=_AgentBGPQueueLimit_Object((1,3,6,1,4,1,7244,2,5,1,1,1,6),_AgentBGPQueueLimit_Type())
agentBGPQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPQueueLimit.setStatus(_A)
_AgentBGPMessageStatsGroup_ObjectIdentity=ObjectIdentity
agentBGPMessageStatsGroup=_AgentBGPMessageStatsGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,5,2))
_AgentBGPCountersCleared_Type=TimeTicks
_AgentBGPCountersCleared_Object=MibScalar
agentBGPCountersCleared=_AgentBGPCountersCleared_Object((1,3,6,1,4,1,7244,2,5,2,1),_AgentBGPCountersCleared_Type())
agentBGPCountersCleared.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPCountersCleared.setStatus(_A)
_AgentBGPInOpens_Type=Counter32
_AgentBGPInOpens_Object=MibScalar
agentBGPInOpens=_AgentBGPInOpens_Object((1,3,6,1,4,1,7244,2,5,2,2),_AgentBGPInOpens_Type())
agentBGPInOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPInOpens.setStatus(_A)
_AgentBGPOutOpens_Type=Counter32
_AgentBGPOutOpens_Object=MibScalar
agentBGPOutOpens=_AgentBGPOutOpens_Object((1,3,6,1,4,1,7244,2,5,2,3),_AgentBGPOutOpens_Type())
agentBGPOutOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPOutOpens.setStatus(_A)
_AgentBGPInUpdates_Type=Counter32
_AgentBGPInUpdates_Object=MibScalar
agentBGPInUpdates=_AgentBGPInUpdates_Object((1,3,6,1,4,1,7244,2,5,2,4),_AgentBGPInUpdates_Type())
agentBGPInUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPInUpdates.setStatus(_A)
_AgentBGPOutUpdates_Type=Counter32
_AgentBGPOutUpdates_Object=MibScalar
agentBGPOutUpdates=_AgentBGPOutUpdates_Object((1,3,6,1,4,1,7244,2,5,2,5),_AgentBGPOutUpdates_Type())
agentBGPOutUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPOutUpdates.setStatus(_A)
_AgentBGPInNotifications_Type=Counter32
_AgentBGPInNotifications_Object=MibScalar
agentBGPInNotifications=_AgentBGPInNotifications_Object((1,3,6,1,4,1,7244,2,5,2,6),_AgentBGPInNotifications_Type())
agentBGPInNotifications.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPInNotifications.setStatus(_A)
_AgentBGPOutNotifications_Type=Counter32
_AgentBGPOutNotifications_Object=MibScalar
agentBGPOutNotifications=_AgentBGPOutNotifications_Object((1,3,6,1,4,1,7244,2,5,2,7),_AgentBGPOutNotifications_Type())
agentBGPOutNotifications.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPOutNotifications.setStatus(_A)
_AgentBGPInKeepalives_Type=Counter32
_AgentBGPInKeepalives_Object=MibScalar
agentBGPInKeepalives=_AgentBGPInKeepalives_Object((1,3,6,1,4,1,7244,2,5,2,8),_AgentBGPInKeepalives_Type())
agentBGPInKeepalives.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPInKeepalives.setStatus(_A)
_AgentBGPOutKeepalives_Type=Counter32
_AgentBGPOutKeepalives_Object=MibScalar
agentBGPOutKeepalives=_AgentBGPOutKeepalives_Object((1,3,6,1,4,1,7244,2,5,2,9),_AgentBGPOutKeepalives_Type())
agentBGPOutKeepalives.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPOutKeepalives.setStatus(_A)
_AgentBGPInRouteRefreshes_Type=Counter32
_AgentBGPInRouteRefreshes_Object=MibScalar
agentBGPInRouteRefreshes=_AgentBGPInRouteRefreshes_Object((1,3,6,1,4,1,7244,2,5,2,10),_AgentBGPInRouteRefreshes_Type())
agentBGPInRouteRefreshes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPInRouteRefreshes.setStatus(_A)
_AgentBGPOutRouteRefreshes_Type=Counter32
_AgentBGPOutRouteRefreshes_Object=MibScalar
agentBGPOutRouteRefreshes=_AgentBGPOutRouteRefreshes_Object((1,3,6,1,4,1,7244,2,5,2,11),_AgentBGPOutRouteRefreshes_Type())
agentBGPOutRouteRefreshes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPOutRouteRefreshes.setStatus(_A)
_AgentBGPInUpdatesMax_Type=Gauge32
_AgentBGPInUpdatesMax_Object=MibScalar
agentBGPInUpdatesMax=_AgentBGPInUpdatesMax_Object((1,3,6,1,4,1,7244,2,5,2,12),_AgentBGPInUpdatesMax_Type())
agentBGPInUpdatesMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPInUpdatesMax.setStatus(_A)
_AgentBGPOutUpdatesMax_Type=Gauge32
_AgentBGPOutUpdatesMax_Object=MibScalar
agentBGPOutUpdatesMax=_AgentBGPOutUpdatesMax_Object((1,3,6,1,4,1,7244,2,5,2,13),_AgentBGPOutUpdatesMax_Type())
agentBGPOutUpdatesMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPOutUpdatesMax.setStatus(_A)
_AgentBGPDecProcTable_Object=MibTable
agentBGPDecProcTable=_AgentBGPDecProcTable_Object((1,3,6,1,4,1,7244,2,5,3))
if mibBuilder.loadTexts:agentBGPDecProcTable.setStatus(_A)
_AgentBGPDecProcEntry_Object=MibTableRow
agentBGPDecProcEntry=_AgentBGPDecProcEntry_Object((1,3,6,1,4,1,7244,2,5,3,1))
agentBGPDecProcEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:agentBGPDecProcEntry.setStatus(_A)
_AgentBGPDecProcIndex_Type=Counter32
_AgentBGPDecProcIndex_Object=MibTableColumn
agentBGPDecProcIndex=_AgentBGPDecProcIndex_Object((1,3,6,1,4,1,7244,2,5,3,1,1),_AgentBGPDecProcIndex_Type())
agentBGPDecProcIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:agentBGPDecProcIndex.setStatus(_A)
_AgentBGPDecProcDeltaT_Type=Unsigned32
_AgentBGPDecProcDeltaT_Object=MibTableColumn
agentBGPDecProcDeltaT=_AgentBGPDecProcDeltaT_Object((1,3,6,1,4,1,7244,2,5,3,1,2),_AgentBGPDecProcDeltaT_Type())
agentBGPDecProcDeltaT.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcDeltaT.setStatus(_A)
class _AgentBGPDecProcPhase_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AgentBGPDecProcPhase_Type.__name__=_D
_AgentBGPDecProcPhase_Object=MibTableColumn
agentBGPDecProcPhase=_AgentBGPDecProcPhase_Object((1,3,6,1,4,1,7244,2,5,3,1,3),_AgentBGPDecProcPhase_Type())
agentBGPDecProcPhase.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcPhase.setStatus(_A)
_AgentBGPDecProcUpdateGroup_Type=Unsigned32
_AgentBGPDecProcUpdateGroup_Object=MibTableColumn
agentBGPDecProcUpdateGroup=_AgentBGPDecProcUpdateGroup_Object((1,3,6,1,4,1,7244,2,5,3,1,4),_AgentBGPDecProcUpdateGroup_Type())
agentBGPDecProcUpdateGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcUpdateGroup.setStatus(_A)
_AgentBGPDecProcGenId_Type=Unsigned32
_AgentBGPDecProcGenId_Object=MibTableColumn
agentBGPDecProcGenId=_AgentBGPDecProcGenId_Object((1,3,6,1,4,1,7244,2,5,3,1,5),_AgentBGPDecProcGenId_Type())
agentBGPDecProcGenId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcGenId.setStatus(_A)
_AgentBGPDecProcReason_Type=DisplayString
_AgentBGPDecProcReason_Object=MibTableColumn
agentBGPDecProcReason=_AgentBGPDecProcReason_Object((1,3,6,1,4,1,7244,2,5,3,1,6),_AgentBGPDecProcReason_Type())
agentBGPDecProcReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcReason.setStatus(_A)
_AgentBGPDecProcPeer_Type=IpAddress
_AgentBGPDecProcPeer_Object=MibTableColumn
agentBGPDecProcPeer=_AgentBGPDecProcPeer_Object((1,3,6,1,4,1,7244,2,5,3,1,7),_AgentBGPDecProcPeer_Type())
agentBGPDecProcPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcPeer.setStatus(_A)
_AgentBGPDecProcDuration_Type=Gauge32
_AgentBGPDecProcDuration_Object=MibTableColumn
agentBGPDecProcDuration=_AgentBGPDecProcDuration_Object((1,3,6,1,4,1,7244,2,5,3,1,8),_AgentBGPDecProcDuration_Type())
agentBGPDecProcDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcDuration.setStatus(_A)
_AgentBGPDecProcAdds_Type=Gauge32
_AgentBGPDecProcAdds_Object=MibTableColumn
agentBGPDecProcAdds=_AgentBGPDecProcAdds_Object((1,3,6,1,4,1,7244,2,5,3,1,9),_AgentBGPDecProcAdds_Type())
agentBGPDecProcAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcAdds.setStatus(_A)
_AgentBGPDecProcMods_Type=Gauge32
_AgentBGPDecProcMods_Object=MibTableColumn
agentBGPDecProcMods=_AgentBGPDecProcMods_Object((1,3,6,1,4,1,7244,2,5,3,1,10),_AgentBGPDecProcMods_Type())
agentBGPDecProcMods.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcMods.setStatus(_A)
_AgentBGPDecProcDels_Type=Gauge32
_AgentBGPDecProcDels_Object=MibTableColumn
agentBGPDecProcDels=_AgentBGPDecProcDels_Object((1,3,6,1,4,1,7244,2,5,3,1,11),_AgentBGPDecProcDels_Type())
agentBGPDecProcDels.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPDecProcDels.setStatus(_A)
_AgentBGPPeerTable_Object=MibTable
agentBGPPeerTable=_AgentBGPPeerTable_Object((1,3,6,1,4,1,7244,2,5,4))
if mibBuilder.loadTexts:agentBGPPeerTable.setStatus(_A)
_AgentBGPPeerEntry_Object=MibTableRow
agentBGPPeerEntry=_AgentBGPPeerEntry_Object((1,3,6,1,4,1,7244,2,5,4,1))
agentBGPPeerEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:agentBGPPeerEntry.setStatus(_A)
_AgentBGPPeerRemoteAddr_Type=IpAddress
_AgentBGPPeerRemoteAddr_Object=MibTableColumn
agentBGPPeerRemoteAddr=_AgentBGPPeerRemoteAddr_Object((1,3,6,1,4,1,7244,2,5,4,1,1),_AgentBGPPeerRemoteAddr_Type())
agentBGPPeerRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerRemoteAddr.setStatus(_A)
_AgentBGPPeerInOpens_Type=Counter32
_AgentBGPPeerInOpens_Object=MibTableColumn
agentBGPPeerInOpens=_AgentBGPPeerInOpens_Object((1,3,6,1,4,1,7244,2,5,4,1,2),_AgentBGPPeerInOpens_Type())
agentBGPPeerInOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInOpens.setStatus(_A)
_AgentBGPPeerOutOpens_Type=Counter32
_AgentBGPPeerOutOpens_Object=MibTableColumn
agentBGPPeerOutOpens=_AgentBGPPeerOutOpens_Object((1,3,6,1,4,1,7244,2,5,4,1,3),_AgentBGPPeerOutOpens_Type())
agentBGPPeerOutOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutOpens.setStatus(_A)
_AgentBGPPeerInUpdates_Type=Counter32
_AgentBGPPeerInUpdates_Object=MibTableColumn
agentBGPPeerInUpdates=_AgentBGPPeerInUpdates_Object((1,3,6,1,4,1,7244,2,5,4,1,4),_AgentBGPPeerInUpdates_Type())
agentBGPPeerInUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInUpdates.setStatus(_A)
_AgentBGPPeerOutUpdates_Type=Counter32
_AgentBGPPeerOutUpdates_Object=MibTableColumn
agentBGPPeerOutUpdates=_AgentBGPPeerOutUpdates_Object((1,3,6,1,4,1,7244,2,5,4,1,5),_AgentBGPPeerOutUpdates_Type())
agentBGPPeerOutUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutUpdates.setStatus(_A)
_AgentBGPPeerInNotifications_Type=Counter32
_AgentBGPPeerInNotifications_Object=MibTableColumn
agentBGPPeerInNotifications=_AgentBGPPeerInNotifications_Object((1,3,6,1,4,1,7244,2,5,4,1,6),_AgentBGPPeerInNotifications_Type())
agentBGPPeerInNotifications.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInNotifications.setStatus(_A)
_AgentBGPPeerOutNotifications_Type=Counter32
_AgentBGPPeerOutNotifications_Object=MibTableColumn
agentBGPPeerOutNotifications=_AgentBGPPeerOutNotifications_Object((1,3,6,1,4,1,7244,2,5,4,1,7),_AgentBGPPeerOutNotifications_Type())
agentBGPPeerOutNotifications.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutNotifications.setStatus(_A)
_AgentBGPPeerInKeepalives_Type=Counter32
_AgentBGPPeerInKeepalives_Object=MibTableColumn
agentBGPPeerInKeepalives=_AgentBGPPeerInKeepalives_Object((1,3,6,1,4,1,7244,2,5,4,1,8),_AgentBGPPeerInKeepalives_Type())
agentBGPPeerInKeepalives.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInKeepalives.setStatus(_A)
_AgentBGPPeerOutKeepalives_Type=Counter32
_AgentBGPPeerOutKeepalives_Object=MibTableColumn
agentBGPPeerOutKeepalives=_AgentBGPPeerOutKeepalives_Object((1,3,6,1,4,1,7244,2,5,4,1,9),_AgentBGPPeerOutKeepalives_Type())
agentBGPPeerOutKeepalives.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutKeepalives.setStatus(_A)
_AgentBGPPeerInRouteRefreshes_Type=Counter32
_AgentBGPPeerInRouteRefreshes_Object=MibTableColumn
agentBGPPeerInRouteRefreshes=_AgentBGPPeerInRouteRefreshes_Object((1,3,6,1,4,1,7244,2,5,4,1,10),_AgentBGPPeerInRouteRefreshes_Type())
agentBGPPeerInRouteRefreshes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInRouteRefreshes.setStatus(_A)
_AgentBGPPeerOutRouteRefreshes_Type=Counter32
_AgentBGPPeerOutRouteRefreshes_Object=MibTableColumn
agentBGPPeerOutRouteRefreshes=_AgentBGPPeerOutRouteRefreshes_Object((1,3,6,1,4,1,7244,2,5,4,1,11),_AgentBGPPeerOutRouteRefreshes_Type())
agentBGPPeerOutRouteRefreshes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutRouteRefreshes.setStatus(_A)
_AgentBGPPeerInTotalMessages_Type=Counter32
_AgentBGPPeerInTotalMessages_Object=MibTableColumn
agentBGPPeerInTotalMessages=_AgentBGPPeerInTotalMessages_Object((1,3,6,1,4,1,7244,2,5,4,1,12),_AgentBGPPeerInTotalMessages_Type())
agentBGPPeerInTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInTotalMessages.setStatus(_A)
_AgentBGPPeerOutTotalMessages_Type=Counter32
_AgentBGPPeerOutTotalMessages_Object=MibTableColumn
agentBGPPeerOutTotalMessages=_AgentBGPPeerOutTotalMessages_Object((1,3,6,1,4,1,7244,2,5,4,1,13),_AgentBGPPeerOutTotalMessages_Type())
agentBGPPeerOutTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutTotalMessages.setStatus(_A)
_AgentBGPPeerUpdateQueueLen_Type=Gauge32
_AgentBGPPeerUpdateQueueLen_Object=MibTableColumn
agentBGPPeerUpdateQueueLen=_AgentBGPPeerUpdateQueueLen_Object((1,3,6,1,4,1,7244,2,5,4,1,14),_AgentBGPPeerUpdateQueueLen_Type())
agentBGPPeerUpdateQueueLen.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerUpdateQueueLen.setStatus(_A)
_AgentBGPPeerUpdateQueueHigh_Type=Gauge32
_AgentBGPPeerUpdateQueueHigh_Object=MibTableColumn
agentBGPPeerUpdateQueueHigh=_AgentBGPPeerUpdateQueueHigh_Object((1,3,6,1,4,1,7244,2,5,4,1,15),_AgentBGPPeerUpdateQueueHigh_Type())
agentBGPPeerUpdateQueueHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerUpdateQueueHigh.setStatus(_A)
_AgentBGPPeerUpdateQueueLimit_Type=Unsigned32
_AgentBGPPeerUpdateQueueLimit_Object=MibTableColumn
agentBGPPeerUpdateQueueLimit=_AgentBGPPeerUpdateQueueLimit_Object((1,3,6,1,4,1,7244,2,5,4,1,16),_AgentBGPPeerUpdateQueueLimit_Type())
agentBGPPeerUpdateQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerUpdateQueueLimit.setStatus(_A)
_AgentBGPPeerUpdateQueueDrops_Type=Counter32
_AgentBGPPeerUpdateQueueDrops_Object=MibTableColumn
agentBGPPeerUpdateQueueDrops=_AgentBGPPeerUpdateQueueDrops_Object((1,3,6,1,4,1,7244,2,5,4,1,17),_AgentBGPPeerUpdateQueueDrops_Type())
agentBGPPeerUpdateQueueDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerUpdateQueueDrops.setStatus(_A)
_AgentBGPPeerInPfxAdv_Type=Counter32
_AgentBGPPeerInPfxAdv_Object=MibTableColumn
agentBGPPeerInPfxAdv=_AgentBGPPeerInPfxAdv_Object((1,3,6,1,4,1,7244,2,5,4,1,18),_AgentBGPPeerInPfxAdv_Type())
agentBGPPeerInPfxAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInPfxAdv.setStatus(_A)
_AgentBGPPeerOutPfxAdv_Type=Counter32
_AgentBGPPeerOutPfxAdv_Object=MibTableColumn
agentBGPPeerOutPfxAdv=_AgentBGPPeerOutPfxAdv_Object((1,3,6,1,4,1,7244,2,5,4,1,19),_AgentBGPPeerOutPfxAdv_Type())
agentBGPPeerOutPfxAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutPfxAdv.setStatus(_A)
_AgentBGPPeerInPfxWithdrawn_Type=Counter32
_AgentBGPPeerInPfxWithdrawn_Object=MibTableColumn
agentBGPPeerInPfxWithdrawn=_AgentBGPPeerInPfxWithdrawn_Object((1,3,6,1,4,1,7244,2,5,4,1,20),_AgentBGPPeerInPfxWithdrawn_Type())
agentBGPPeerInPfxWithdrawn.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInPfxWithdrawn.setStatus(_A)
_AgentBGPPeerOutPfxWithdrawn_Type=Counter32
_AgentBGPPeerOutPfxWithdrawn_Object=MibTableColumn
agentBGPPeerOutPfxWithdrawn=_AgentBGPPeerOutPfxWithdrawn_Object((1,3,6,1,4,1,7244,2,5,4,1,21),_AgentBGPPeerOutPfxWithdrawn_Type())
agentBGPPeerOutPfxWithdrawn.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutPfxWithdrawn.setStatus(_A)
_AgentBGPPeerInPfxCurrent_Type=Gauge32
_AgentBGPPeerInPfxCurrent_Object=MibTableColumn
agentBGPPeerInPfxCurrent=_AgentBGPPeerInPfxCurrent_Object((1,3,6,1,4,1,7244,2,5,4,1,22),_AgentBGPPeerInPfxCurrent_Type())
agentBGPPeerInPfxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInPfxCurrent.setStatus(_A)
_AgentBGPPeerOutPfxCurrent_Type=Gauge32
_AgentBGPPeerOutPfxCurrent_Object=MibTableColumn
agentBGPPeerOutPfxCurrent=_AgentBGPPeerOutPfxCurrent_Object((1,3,6,1,4,1,7244,2,5,4,1,23),_AgentBGPPeerOutPfxCurrent_Type())
agentBGPPeerOutPfxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutPfxCurrent.setStatus(_A)
_AgentBGPPeerInPfxAccepted_Type=Gauge32
_AgentBGPPeerInPfxAccepted_Object=MibTableColumn
agentBGPPeerInPfxAccepted=_AgentBGPPeerInPfxAccepted_Object((1,3,6,1,4,1,7244,2,5,4,1,24),_AgentBGPPeerInPfxAccepted_Type())
agentBGPPeerInPfxAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInPfxAccepted.setStatus(_A)
_AgentBGPPeerInPfxRejected_Type=Gauge32
_AgentBGPPeerInPfxRejected_Object=MibTableColumn
agentBGPPeerInPfxRejected=_AgentBGPPeerInPfxRejected_Object((1,3,6,1,4,1,7244,2,5,4,1,25),_AgentBGPPeerInPfxRejected_Type())
agentBGPPeerInPfxRejected.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInPfxRejected.setStatus(_A)
_AgentBGPPeerInMaxNlriPerUpdate_Type=Gauge32
_AgentBGPPeerInMaxNlriPerUpdate_Object=MibTableColumn
agentBGPPeerInMaxNlriPerUpdate=_AgentBGPPeerInMaxNlriPerUpdate_Object((1,3,6,1,4,1,7244,2,5,4,1,26),_AgentBGPPeerInMaxNlriPerUpdate_Type())
agentBGPPeerInMaxNlriPerUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInMaxNlriPerUpdate.setStatus(_A)
_AgentBGPPeerOutMaxNlriPerUpdate_Type=Gauge32
_AgentBGPPeerOutMaxNlriPerUpdate_Object=MibTableColumn
agentBGPPeerOutMaxNlriPerUpdate=_AgentBGPPeerOutMaxNlriPerUpdate_Object((1,3,6,1,4,1,7244,2,5,4,1,27),_AgentBGPPeerOutMaxNlriPerUpdate_Type())
agentBGPPeerOutMaxNlriPerUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutMaxNlriPerUpdate.setStatus(_A)
_AgentBGPPeerInMinNlriPerUpdate_Type=Gauge32
_AgentBGPPeerInMinNlriPerUpdate_Object=MibTableColumn
agentBGPPeerInMinNlriPerUpdate=_AgentBGPPeerInMinNlriPerUpdate_Object((1,3,6,1,4,1,7244,2,5,4,1,28),_AgentBGPPeerInMinNlriPerUpdate_Type())
agentBGPPeerInMinNlriPerUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerInMinNlriPerUpdate.setStatus(_A)
_AgentBGPPeerOutMinNlriPerUpdate_Type=Gauge32
_AgentBGPPeerOutMinNlriPerUpdate_Object=MibTableColumn
agentBGPPeerOutMinNlriPerUpdate=_AgentBGPPeerOutMinNlriPerUpdate_Object((1,3,6,1,4,1,7244,2,5,4,1,29),_AgentBGPPeerOutMinNlriPerUpdate_Type())
agentBGPPeerOutMinNlriPerUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBGPPeerOutMinNlriPerUpdate.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'quantaBGP':quantaBGP,'agentBGPQueueGroup':agentBGPQueueGroup,'agentBGPQueueTable':agentBGPQueueTable,'agentBGPQueueEntry':agentBGPQueueEntry,_E:agentBGPQueueIndex,'agentBGPQueueName':agentBGPQueueName,'agentBGPQueueLength':agentBGPQueueLength,'agentBGPQueueHigh':agentBGPQueueHigh,'agentBGPQueueDrops':agentBGPQueueDrops,'agentBGPQueueLimit':agentBGPQueueLimit,'agentBGPMessageStatsGroup':agentBGPMessageStatsGroup,'agentBGPCountersCleared':agentBGPCountersCleared,'agentBGPInOpens':agentBGPInOpens,'agentBGPOutOpens':agentBGPOutOpens,'agentBGPInUpdates':agentBGPInUpdates,'agentBGPOutUpdates':agentBGPOutUpdates,'agentBGPInNotifications':agentBGPInNotifications,'agentBGPOutNotifications':agentBGPOutNotifications,'agentBGPInKeepalives':agentBGPInKeepalives,'agentBGPOutKeepalives':agentBGPOutKeepalives,'agentBGPInRouteRefreshes':agentBGPInRouteRefreshes,'agentBGPOutRouteRefreshes':agentBGPOutRouteRefreshes,'agentBGPInUpdatesMax':agentBGPInUpdatesMax,'agentBGPOutUpdatesMax':agentBGPOutUpdatesMax,'agentBGPDecProcTable':agentBGPDecProcTable,'agentBGPDecProcEntry':agentBGPDecProcEntry,_G:agentBGPDecProcIndex,'agentBGPDecProcDeltaT':agentBGPDecProcDeltaT,'agentBGPDecProcPhase':agentBGPDecProcPhase,'agentBGPDecProcUpdateGroup':agentBGPDecProcUpdateGroup,'agentBGPDecProcGenId':agentBGPDecProcGenId,'agentBGPDecProcReason':agentBGPDecProcReason,'agentBGPDecProcPeer':agentBGPDecProcPeer,'agentBGPDecProcDuration':agentBGPDecProcDuration,'agentBGPDecProcAdds':agentBGPDecProcAdds,'agentBGPDecProcMods':agentBGPDecProcMods,'agentBGPDecProcDels':agentBGPDecProcDels,'agentBGPPeerTable':agentBGPPeerTable,'agentBGPPeerEntry':agentBGPPeerEntry,_H:agentBGPPeerRemoteAddr,'agentBGPPeerInOpens':agentBGPPeerInOpens,'agentBGPPeerOutOpens':agentBGPPeerOutOpens,'agentBGPPeerInUpdates':agentBGPPeerInUpdates,'agentBGPPeerOutUpdates':agentBGPPeerOutUpdates,'agentBGPPeerInNotifications':agentBGPPeerInNotifications,'agentBGPPeerOutNotifications':agentBGPPeerOutNotifications,'agentBGPPeerInKeepalives':agentBGPPeerInKeepalives,'agentBGPPeerOutKeepalives':agentBGPPeerOutKeepalives,'agentBGPPeerInRouteRefreshes':agentBGPPeerInRouteRefreshes,'agentBGPPeerOutRouteRefreshes':agentBGPPeerOutRouteRefreshes,'agentBGPPeerInTotalMessages':agentBGPPeerInTotalMessages,'agentBGPPeerOutTotalMessages':agentBGPPeerOutTotalMessages,'agentBGPPeerUpdateQueueLen':agentBGPPeerUpdateQueueLen,'agentBGPPeerUpdateQueueHigh':agentBGPPeerUpdateQueueHigh,'agentBGPPeerUpdateQueueLimit':agentBGPPeerUpdateQueueLimit,'agentBGPPeerUpdateQueueDrops':agentBGPPeerUpdateQueueDrops,'agentBGPPeerInPfxAdv':agentBGPPeerInPfxAdv,'agentBGPPeerOutPfxAdv':agentBGPPeerOutPfxAdv,'agentBGPPeerInPfxWithdrawn':agentBGPPeerInPfxWithdrawn,'agentBGPPeerOutPfxWithdrawn':agentBGPPeerOutPfxWithdrawn,'agentBGPPeerInPfxCurrent':agentBGPPeerInPfxCurrent,'agentBGPPeerOutPfxCurrent':agentBGPPeerOutPfxCurrent,'agentBGPPeerInPfxAccepted':agentBGPPeerInPfxAccepted,'agentBGPPeerInPfxRejected':agentBGPPeerInPfxRejected,'agentBGPPeerInMaxNlriPerUpdate':agentBGPPeerInMaxNlriPerUpdate,'agentBGPPeerOutMaxNlriPerUpdate':agentBGPPeerOutMaxNlriPerUpdate,'agentBGPPeerInMinNlriPerUpdate':agentBGPPeerInMinNlriPerUpdate,'agentBGPPeerOutMinNlriPerUpdate':agentBGPPeerOutMinNlriPerUpdate})