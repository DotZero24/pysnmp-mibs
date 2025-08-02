_At='altigaL2tpStatsGroup'
_As='alL2tpStatsSessionRecvSeqResets'
_Ar='alL2tpStatsSessionSendSeqResets'
_Aq='alL2tpStatsSessionCurrentRemoteRWS'
_Ap='alL2tpStatsSessionAckTimeouts'
_Ao='alL2tpStatsSessionOutOfWindow'
_An='alL2tpStatsSessionSendZLB'
_Am='alL2tpStatsSessionRecvZLB'
_Al='alL2tpStatsSessionRemoteInitialRWS'
_Ak='alL2tpStatsSessionLocalRWS'
_Aj='alL2tpStatsSessionTunnelPeerIpAddr'
_Ai='alL2tpStatsSessionRecvSeqAck'
_Ah='alL2tpStatsSessionRecvSeq'
_Ag='alL2tpStatsSessionSendSeqAck'
_Af='alL2tpStatsSessionSendSeq'
_Ae='alL2tpStatsSessionReassemblyTimeouts'
_Ad='alL2tpStatsSessionSendPackets'
_Ac='alL2tpStatsSessionSendOctets'
_Ab='alL2tpStatsSessionOutSequence'
_Aa='alL2tpStatsSessionRecvDiscards'
_AZ='alL2tpStatsSessionRecvPackets'
_AY='alL2tpStatsSessionRecvOctets'
_AX='alL2tpStatsSessionSequencingState'
_AW='alL2tpStatsSessionRemotePPD'
_AV='alL2tpStatsSessionAuthMethod'
_AU='alL2tpStatsSessionProxyLcp'
_AT='alL2tpStatsSessionPrivateGroupID'
_AS='alL2tpStatsSessionSubAddress'
_AR='alL2tpStatsSessionCLID'
_AQ='alL2tpStatsSessionDNIS'
_AP='alL2tpStatsSessionPhysChanId'
_AO='alL2tpStatsSessionFramingType'
_AN='alL2tpStatsSessionCallBearerType'
_AM='alL2tpStatsSessionRxConnectSpeed'
_AL='alL2tpStatsSessionTxConnectSpeed'
_AK='alL2tpStatsSessionCallSerialNumber'
_AJ='alL2tpStatsSessionCallType'
_AI='alL2tpStatsSessionState'
_AH='alL2tpStatsSessionUserName'
_AG='alL2tpStatsSessionRemoteCID'
_AF='alL2tpStatsSessionLocalCID'
_AE='alL2tpStatsSessionTID'
_AD='alL2tpStatsSessionRowStatus'
_AC='alL2tpStatsTunnelLastErrorMessage'
_AB='alL2tpStatsTunnelLastErrorCode'
_AA='alL2tpStatsTunnelLastResultCode'
_A9='alL2tpStatsTunnelActiveSessions'
_A8='alL2tpStatsTunnelFailedSessions'
_A7='alL2tpStatsTunnelTotalSessions'
_A6='alL2tpStatsTunnelRecvSeqAck'
_A5='alL2tpStatsTunnelRecvSeq'
_A4='alL2tpStatsTunnelSendSeqAck'
_A3='alL2tpStatsTunnelSendSeq'
_A2='alL2tpStatsTunnelCurrentRemoteRWS'
_A1='alL2tpStatsTunnelControlAckTimeouts'
_A0='alL2tpStatsTunnelControlSendZLB'
_z='alL2tpStatsTunnelControlSendPackets'
_y='alL2tpStatsTunnelControlOutOfWindow'
_x='alL2tpStatsTunnelControlOutOfSequence'
_w='alL2tpStatsTunnelControlRecvZLB'
_v='alL2tpStatsTunnelControlRecvDiscards'
_u='alL2tpStatsTunnelControlRecvPackets'
_t='alL2tpStatsTunnelFramingCapabilities'
_s='alL2tpStatsTunnelBearerCapabilities'
_r='alL2tpStatsTunnelInitialRemoteRWS'
_q='alL2tpStatsTunnelRemoteProtocolVersion'
_p='alL2tpStatsTunnelRemoteFirmwareRevision'
_o='alL2tpStatsTunnelRemoteVendorName'
_n='alL2tpStatsTunnelRemoteHostName'
_m='alL2tpStatsTunnelInitiated'
_l='alL2tpStatsTunnelState'
_k='alL2tpStatsTunnelRemoteTID'
_j='alL2tpStatsTunnelLocalTID'
_i='alL2tpStatsTunnelRowStatus'
_h='alL2tpStatsPayloadSendPackets'
_g='alL2tpStatsPayloadSendOctets'
_f='alL2tpStatsPayloadRecvDiscards'
_e='alL2tpStatsPayloadRecvPackets'
_d='alL2tpStatsPayloadRecvOctets'
_c='alL2tpStatsControlSendPackets'
_b='alL2tpStatsControlSendOctets'
_a='alL2tpStatsControlRecvDiscards'
_Z='alL2tpStatsControlRecvPackets'
_Y='alL2tpStatsControlRecvOctets'
_X='alL2tpStatsMaxSessions'
_W='alL2tpStatsActiveSessions'
_V='alL2tpStatsFailedSessions'
_U='alL2tpStatsTotalSessions'
_T='alL2tpStatsMaxTunnels'
_S='alL2tpStatsActiveTunnels'
_R='alL2tpStatsFailedAuthentications'
_Q='alL2tpStatsFailedTunnels'
_P='alL2tpStatsTotalTunnels'
_O='alL2tpStatsFirmwareRev'
_N='alL2tpStatsVendorName'
_M='alL2tpStatsLocalProtVers'
_L='analog'
_K='digital'
_J='read-write'
_I='alL2tpStatsSessionIfIndex'
_H='alL2tpStatsTunnelPeerIpAddr'
_G='Gauge32'
_F='OctetString'
_E='deprecated'
_D='Integer32'
_C='current'
_B='read-only'
_A='ALTIGA-L2TP-STATS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alL2tpMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alL2tpMibModule')
alL2tpGroup,alStatsL2tp=mibBuilder.importSymbols('ALTIGA-MIB','alL2tpGroup','alStatsL2tp')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_G,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
altigaL2tpStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,21,2))
if mibBuilder.loadTexts:altigaL2tpStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaL2tpStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaL2tpStatsMibConformance=_AltigaL2tpStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,21,2,1))
_AltigaL2tpStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaL2tpStatsMibCompliances=_AltigaL2tpStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,21,2,1,1))
_AlStatsL2tpGlobal_ObjectIdentity=ObjectIdentity
alStatsL2tpGlobal=_AlStatsL2tpGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,16,1))
class _AlL2tpStatsLocalProtVers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AlL2tpStatsLocalProtVers_Type.__name__=_F
_AlL2tpStatsLocalProtVers_Object=MibScalar
alL2tpStatsLocalProtVers=_AlL2tpStatsLocalProtVers_Object((1,3,6,1,4,1,3076,2,1,2,16,1,1),_AlL2tpStatsLocalProtVers_Type())
alL2tpStatsLocalProtVers.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsLocalProtVers.setStatus(_C)
_AlL2tpStatsVendorName_Type=DisplayString
_AlL2tpStatsVendorName_Object=MibScalar
alL2tpStatsVendorName=_AlL2tpStatsVendorName_Object((1,3,6,1,4,1,3076,2,1,2,16,1,2),_AlL2tpStatsVendorName_Type())
alL2tpStatsVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsVendorName.setStatus(_C)
class _AlL2tpStatsFirmwareRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AlL2tpStatsFirmwareRev_Type.__name__=_F
_AlL2tpStatsFirmwareRev_Object=MibScalar
alL2tpStatsFirmwareRev=_AlL2tpStatsFirmwareRev_Object((1,3,6,1,4,1,3076,2,1,2,16,1,3),_AlL2tpStatsFirmwareRev_Type())
alL2tpStatsFirmwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsFirmwareRev.setStatus(_C)
_AlL2tpStatsTotalTunnels_Type=Counter32
_AlL2tpStatsTotalTunnels_Object=MibScalar
alL2tpStatsTotalTunnels=_AlL2tpStatsTotalTunnels_Object((1,3,6,1,4,1,3076,2,1,2,16,1,4),_AlL2tpStatsTotalTunnels_Type())
alL2tpStatsTotalTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTotalTunnels.setStatus(_C)
_AlL2tpStatsFailedTunnels_Type=Counter32
_AlL2tpStatsFailedTunnels_Object=MibScalar
alL2tpStatsFailedTunnels=_AlL2tpStatsFailedTunnels_Object((1,3,6,1,4,1,3076,2,1,2,16,1,5),_AlL2tpStatsFailedTunnels_Type())
alL2tpStatsFailedTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsFailedTunnels.setStatus(_C)
_AlL2tpStatsFailedAuthentications_Type=Counter32
_AlL2tpStatsFailedAuthentications_Object=MibScalar
alL2tpStatsFailedAuthentications=_AlL2tpStatsFailedAuthentications_Object((1,3,6,1,4,1,3076,2,1,2,16,1,6),_AlL2tpStatsFailedAuthentications_Type())
alL2tpStatsFailedAuthentications.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsFailedAuthentications.setStatus(_C)
_AlL2tpStatsActiveTunnels_Type=Gauge32
_AlL2tpStatsActiveTunnels_Object=MibScalar
alL2tpStatsActiveTunnels=_AlL2tpStatsActiveTunnels_Object((1,3,6,1,4,1,3076,2,1,2,16,1,7),_AlL2tpStatsActiveTunnels_Type())
alL2tpStatsActiveTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsActiveTunnels.setStatus(_C)
_AlL2tpStatsMaxTunnels_Type=Gauge32
_AlL2tpStatsMaxTunnels_Object=MibScalar
alL2tpStatsMaxTunnels=_AlL2tpStatsMaxTunnels_Object((1,3,6,1,4,1,3076,2,1,2,16,1,8),_AlL2tpStatsMaxTunnels_Type())
alL2tpStatsMaxTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsMaxTunnels.setStatus(_C)
_AlL2tpStatsTotalSessions_Type=Counter32
_AlL2tpStatsTotalSessions_Object=MibScalar
alL2tpStatsTotalSessions=_AlL2tpStatsTotalSessions_Object((1,3,6,1,4,1,3076,2,1,2,16,1,9),_AlL2tpStatsTotalSessions_Type())
alL2tpStatsTotalSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTotalSessions.setStatus(_C)
_AlL2tpStatsFailedSessions_Type=Counter32
_AlL2tpStatsFailedSessions_Object=MibScalar
alL2tpStatsFailedSessions=_AlL2tpStatsFailedSessions_Object((1,3,6,1,4,1,3076,2,1,2,16,1,10),_AlL2tpStatsFailedSessions_Type())
alL2tpStatsFailedSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsFailedSessions.setStatus(_C)
_AlL2tpStatsActiveSessions_Type=Gauge32
_AlL2tpStatsActiveSessions_Object=MibScalar
alL2tpStatsActiveSessions=_AlL2tpStatsActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,16,1,11),_AlL2tpStatsActiveSessions_Type())
alL2tpStatsActiveSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsActiveSessions.setStatus(_C)
_AlL2tpStatsMaxSessions_Type=Gauge32
_AlL2tpStatsMaxSessions_Object=MibScalar
alL2tpStatsMaxSessions=_AlL2tpStatsMaxSessions_Object((1,3,6,1,4,1,3076,2,1,2,16,1,12),_AlL2tpStatsMaxSessions_Type())
alL2tpStatsMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsMaxSessions.setStatus(_C)
_AlL2tpStatsControlRecvOctets_Type=Counter32
_AlL2tpStatsControlRecvOctets_Object=MibScalar
alL2tpStatsControlRecvOctets=_AlL2tpStatsControlRecvOctets_Object((1,3,6,1,4,1,3076,2,1,2,16,1,13),_AlL2tpStatsControlRecvOctets_Type())
alL2tpStatsControlRecvOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsControlRecvOctets.setStatus(_C)
_AlL2tpStatsControlRecvPackets_Type=Counter32
_AlL2tpStatsControlRecvPackets_Object=MibScalar
alL2tpStatsControlRecvPackets=_AlL2tpStatsControlRecvPackets_Object((1,3,6,1,4,1,3076,2,1,2,16,1,14),_AlL2tpStatsControlRecvPackets_Type())
alL2tpStatsControlRecvPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsControlRecvPackets.setStatus(_C)
_AlL2tpStatsControlRecvDiscards_Type=Counter32
_AlL2tpStatsControlRecvDiscards_Object=MibScalar
alL2tpStatsControlRecvDiscards=_AlL2tpStatsControlRecvDiscards_Object((1,3,6,1,4,1,3076,2,1,2,16,1,15),_AlL2tpStatsControlRecvDiscards_Type())
alL2tpStatsControlRecvDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsControlRecvDiscards.setStatus(_C)
_AlL2tpStatsControlSendOctets_Type=Counter32
_AlL2tpStatsControlSendOctets_Object=MibScalar
alL2tpStatsControlSendOctets=_AlL2tpStatsControlSendOctets_Object((1,3,6,1,4,1,3076,2,1,2,16,1,16),_AlL2tpStatsControlSendOctets_Type())
alL2tpStatsControlSendOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsControlSendOctets.setStatus(_C)
_AlL2tpStatsControlSendPackets_Type=Counter32
_AlL2tpStatsControlSendPackets_Object=MibScalar
alL2tpStatsControlSendPackets=_AlL2tpStatsControlSendPackets_Object((1,3,6,1,4,1,3076,2,1,2,16,1,17),_AlL2tpStatsControlSendPackets_Type())
alL2tpStatsControlSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsControlSendPackets.setStatus(_C)
_AlL2tpStatsPayloadRecvOctets_Type=Counter32
_AlL2tpStatsPayloadRecvOctets_Object=MibScalar
alL2tpStatsPayloadRecvOctets=_AlL2tpStatsPayloadRecvOctets_Object((1,3,6,1,4,1,3076,2,1,2,16,1,18),_AlL2tpStatsPayloadRecvOctets_Type())
alL2tpStatsPayloadRecvOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsPayloadRecvOctets.setStatus(_C)
_AlL2tpStatsPayloadRecvPackets_Type=Counter32
_AlL2tpStatsPayloadRecvPackets_Object=MibScalar
alL2tpStatsPayloadRecvPackets=_AlL2tpStatsPayloadRecvPackets_Object((1,3,6,1,4,1,3076,2,1,2,16,1,19),_AlL2tpStatsPayloadRecvPackets_Type())
alL2tpStatsPayloadRecvPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsPayloadRecvPackets.setStatus(_C)
_AlL2tpStatsPayloadRecvDiscards_Type=Counter32
_AlL2tpStatsPayloadRecvDiscards_Object=MibScalar
alL2tpStatsPayloadRecvDiscards=_AlL2tpStatsPayloadRecvDiscards_Object((1,3,6,1,4,1,3076,2,1,2,16,1,20),_AlL2tpStatsPayloadRecvDiscards_Type())
alL2tpStatsPayloadRecvDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsPayloadRecvDiscards.setStatus(_C)
_AlL2tpStatsPayloadSendOctets_Type=Counter32
_AlL2tpStatsPayloadSendOctets_Object=MibScalar
alL2tpStatsPayloadSendOctets=_AlL2tpStatsPayloadSendOctets_Object((1,3,6,1,4,1,3076,2,1,2,16,1,21),_AlL2tpStatsPayloadSendOctets_Type())
alL2tpStatsPayloadSendOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsPayloadSendOctets.setStatus(_C)
_AlL2tpStatsPayloadSendPackets_Type=Counter32
_AlL2tpStatsPayloadSendPackets_Object=MibScalar
alL2tpStatsPayloadSendPackets=_AlL2tpStatsPayloadSendPackets_Object((1,3,6,1,4,1,3076,2,1,2,16,1,22),_AlL2tpStatsPayloadSendPackets_Type())
alL2tpStatsPayloadSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsPayloadSendPackets.setStatus(_C)
_AlL2tpStatsTunnelTable_Object=MibTable
alL2tpStatsTunnelTable=_AlL2tpStatsTunnelTable_Object((1,3,6,1,4,1,3076,2,1,2,16,2))
if mibBuilder.loadTexts:alL2tpStatsTunnelTable.setStatus(_C)
_AlL2tpStatsTunnelEntry_Object=MibTableRow
alL2tpStatsTunnelEntry=_AlL2tpStatsTunnelEntry_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1))
alL2tpStatsTunnelEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:alL2tpStatsTunnelEntry.setStatus(_C)
_AlL2tpStatsTunnelRowStatus_Type=RowStatus
_AlL2tpStatsTunnelRowStatus_Object=MibTableColumn
alL2tpStatsTunnelRowStatus=_AlL2tpStatsTunnelRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,1),_AlL2tpStatsTunnelRowStatus_Type())
alL2tpStatsTunnelRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:alL2tpStatsTunnelRowStatus.setStatus(_C)
_AlL2tpStatsTunnelPeerIpAddr_Type=IpAddress
_AlL2tpStatsTunnelPeerIpAddr_Object=MibTableColumn
alL2tpStatsTunnelPeerIpAddr=_AlL2tpStatsTunnelPeerIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,2),_AlL2tpStatsTunnelPeerIpAddr_Type())
alL2tpStatsTunnelPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelPeerIpAddr.setStatus(_C)
class _AlL2tpStatsTunnelLocalTID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsTunnelLocalTID_Type.__name__=_D
_AlL2tpStatsTunnelLocalTID_Object=MibTableColumn
alL2tpStatsTunnelLocalTID=_AlL2tpStatsTunnelLocalTID_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,3),_AlL2tpStatsTunnelLocalTID_Type())
alL2tpStatsTunnelLocalTID.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelLocalTID.setStatus(_C)
class _AlL2tpStatsTunnelRemoteTID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsTunnelRemoteTID_Type.__name__=_D
_AlL2tpStatsTunnelRemoteTID_Object=MibTableColumn
alL2tpStatsTunnelRemoteTID=_AlL2tpStatsTunnelRemoteTID_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,4),_AlL2tpStatsTunnelRemoteTID_Type())
alL2tpStatsTunnelRemoteTID.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelRemoteTID.setStatus(_C)
class _AlL2tpStatsTunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tunnelIdle',1),('tunnelConnecting',2),('tunnelEstablished',3),('tunnelDisconnecting',4)))
_AlL2tpStatsTunnelState_Type.__name__=_D
_AlL2tpStatsTunnelState_Object=MibTableColumn
alL2tpStatsTunnelState=_AlL2tpStatsTunnelState_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,5),_AlL2tpStatsTunnelState_Type())
alL2tpStatsTunnelState.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelState.setStatus(_C)
class _AlL2tpStatsTunnelInitiated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('locally',1),('remotely',2)))
_AlL2tpStatsTunnelInitiated_Type.__name__=_D
_AlL2tpStatsTunnelInitiated_Object=MibTableColumn
alL2tpStatsTunnelInitiated=_AlL2tpStatsTunnelInitiated_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,6),_AlL2tpStatsTunnelInitiated_Type())
alL2tpStatsTunnelInitiated.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelInitiated.setStatus(_C)
_AlL2tpStatsTunnelRemoteHostName_Type=DisplayString
_AlL2tpStatsTunnelRemoteHostName_Object=MibTableColumn
alL2tpStatsTunnelRemoteHostName=_AlL2tpStatsTunnelRemoteHostName_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,7),_AlL2tpStatsTunnelRemoteHostName_Type())
alL2tpStatsTunnelRemoteHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelRemoteHostName.setStatus(_C)
_AlL2tpStatsTunnelRemoteVendorName_Type=DisplayString
_AlL2tpStatsTunnelRemoteVendorName_Object=MibTableColumn
alL2tpStatsTunnelRemoteVendorName=_AlL2tpStatsTunnelRemoteVendorName_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,8),_AlL2tpStatsTunnelRemoteVendorName_Type())
alL2tpStatsTunnelRemoteVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelRemoteVendorName.setStatus(_C)
class _AlL2tpStatsTunnelRemoteFirmwareRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AlL2tpStatsTunnelRemoteFirmwareRevision_Type.__name__=_F
_AlL2tpStatsTunnelRemoteFirmwareRevision_Object=MibTableColumn
alL2tpStatsTunnelRemoteFirmwareRevision=_AlL2tpStatsTunnelRemoteFirmwareRevision_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,9),_AlL2tpStatsTunnelRemoteFirmwareRevision_Type())
alL2tpStatsTunnelRemoteFirmwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelRemoteFirmwareRevision.setStatus(_C)
class _AlL2tpStatsTunnelRemoteProtocolVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AlL2tpStatsTunnelRemoteProtocolVersion_Type.__name__=_F
_AlL2tpStatsTunnelRemoteProtocolVersion_Object=MibTableColumn
alL2tpStatsTunnelRemoteProtocolVersion=_AlL2tpStatsTunnelRemoteProtocolVersion_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,10),_AlL2tpStatsTunnelRemoteProtocolVersion_Type())
alL2tpStatsTunnelRemoteProtocolVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelRemoteProtocolVersion.setStatus(_C)
class _AlL2tpStatsTunnelInitialRemoteRWS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsTunnelInitialRemoteRWS_Type.__name__=_D
_AlL2tpStatsTunnelInitialRemoteRWS_Object=MibTableColumn
alL2tpStatsTunnelInitialRemoteRWS=_AlL2tpStatsTunnelInitialRemoteRWS_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,11),_AlL2tpStatsTunnelInitialRemoteRWS_Type())
alL2tpStatsTunnelInitialRemoteRWS.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelInitialRemoteRWS.setStatus(_C)
class _AlL2tpStatsTunnelBearerCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sync',1),('async',2),('syncAsync',3)))
_AlL2tpStatsTunnelBearerCapabilities_Type.__name__=_D
_AlL2tpStatsTunnelBearerCapabilities_Object=MibTableColumn
alL2tpStatsTunnelBearerCapabilities=_AlL2tpStatsTunnelBearerCapabilities_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,12),_AlL2tpStatsTunnelBearerCapabilities_Type())
alL2tpStatsTunnelBearerCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelBearerCapabilities.setStatus(_C)
class _AlL2tpStatsTunnelFramingCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),('digitalAnalog',3)))
_AlL2tpStatsTunnelFramingCapabilities_Type.__name__=_D
_AlL2tpStatsTunnelFramingCapabilities_Object=MibTableColumn
alL2tpStatsTunnelFramingCapabilities=_AlL2tpStatsTunnelFramingCapabilities_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,13),_AlL2tpStatsTunnelFramingCapabilities_Type())
alL2tpStatsTunnelFramingCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelFramingCapabilities.setStatus(_C)
_AlL2tpStatsTunnelControlRecvPackets_Type=Counter32
_AlL2tpStatsTunnelControlRecvPackets_Object=MibTableColumn
alL2tpStatsTunnelControlRecvPackets=_AlL2tpStatsTunnelControlRecvPackets_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,14),_AlL2tpStatsTunnelControlRecvPackets_Type())
alL2tpStatsTunnelControlRecvPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelControlRecvPackets.setStatus(_C)
_AlL2tpStatsTunnelControlRecvDiscards_Type=Counter32
_AlL2tpStatsTunnelControlRecvDiscards_Object=MibTableColumn
alL2tpStatsTunnelControlRecvDiscards=_AlL2tpStatsTunnelControlRecvDiscards_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,15),_AlL2tpStatsTunnelControlRecvDiscards_Type())
alL2tpStatsTunnelControlRecvDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelControlRecvDiscards.setStatus(_C)
_AlL2tpStatsTunnelControlRecvZLB_Type=Counter32
_AlL2tpStatsTunnelControlRecvZLB_Object=MibTableColumn
alL2tpStatsTunnelControlRecvZLB=_AlL2tpStatsTunnelControlRecvZLB_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,16),_AlL2tpStatsTunnelControlRecvZLB_Type())
alL2tpStatsTunnelControlRecvZLB.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelControlRecvZLB.setStatus(_C)
_AlL2tpStatsTunnelControlOutOfSequence_Type=Counter32
_AlL2tpStatsTunnelControlOutOfSequence_Object=MibTableColumn
alL2tpStatsTunnelControlOutOfSequence=_AlL2tpStatsTunnelControlOutOfSequence_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,17),_AlL2tpStatsTunnelControlOutOfSequence_Type())
alL2tpStatsTunnelControlOutOfSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelControlOutOfSequence.setStatus(_C)
_AlL2tpStatsTunnelControlOutOfWindow_Type=Counter32
_AlL2tpStatsTunnelControlOutOfWindow_Object=MibTableColumn
alL2tpStatsTunnelControlOutOfWindow=_AlL2tpStatsTunnelControlOutOfWindow_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,18),_AlL2tpStatsTunnelControlOutOfWindow_Type())
alL2tpStatsTunnelControlOutOfWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelControlOutOfWindow.setStatus(_C)
_AlL2tpStatsTunnelControlSendPackets_Type=Counter32
_AlL2tpStatsTunnelControlSendPackets_Object=MibTableColumn
alL2tpStatsTunnelControlSendPackets=_AlL2tpStatsTunnelControlSendPackets_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,19),_AlL2tpStatsTunnelControlSendPackets_Type())
alL2tpStatsTunnelControlSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelControlSendPackets.setStatus(_C)
_AlL2tpStatsTunnelControlSendZLB_Type=Counter32
_AlL2tpStatsTunnelControlSendZLB_Object=MibTableColumn
alL2tpStatsTunnelControlSendZLB=_AlL2tpStatsTunnelControlSendZLB_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,20),_AlL2tpStatsTunnelControlSendZLB_Type())
alL2tpStatsTunnelControlSendZLB.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelControlSendZLB.setStatus(_C)
_AlL2tpStatsTunnelControlAckTimeouts_Type=Counter32
_AlL2tpStatsTunnelControlAckTimeouts_Object=MibTableColumn
alL2tpStatsTunnelControlAckTimeouts=_AlL2tpStatsTunnelControlAckTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,21),_AlL2tpStatsTunnelControlAckTimeouts_Type())
alL2tpStatsTunnelControlAckTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelControlAckTimeouts.setStatus(_C)
class _AlL2tpStatsTunnelCurrentRemoteRWS_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_AlL2tpStatsTunnelCurrentRemoteRWS_Type.__name__=_G
_AlL2tpStatsTunnelCurrentRemoteRWS_Object=MibTableColumn
alL2tpStatsTunnelCurrentRemoteRWS=_AlL2tpStatsTunnelCurrentRemoteRWS_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,22),_AlL2tpStatsTunnelCurrentRemoteRWS_Type())
alL2tpStatsTunnelCurrentRemoteRWS.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelCurrentRemoteRWS.setStatus(_C)
class _AlL2tpStatsTunnelSendSeq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsTunnelSendSeq_Type.__name__=_D
_AlL2tpStatsTunnelSendSeq_Object=MibTableColumn
alL2tpStatsTunnelSendSeq=_AlL2tpStatsTunnelSendSeq_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,23),_AlL2tpStatsTunnelSendSeq_Type())
alL2tpStatsTunnelSendSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelSendSeq.setStatus(_C)
class _AlL2tpStatsTunnelSendSeqAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsTunnelSendSeqAck_Type.__name__=_D
_AlL2tpStatsTunnelSendSeqAck_Object=MibTableColumn
alL2tpStatsTunnelSendSeqAck=_AlL2tpStatsTunnelSendSeqAck_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,24),_AlL2tpStatsTunnelSendSeqAck_Type())
alL2tpStatsTunnelSendSeqAck.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelSendSeqAck.setStatus(_C)
class _AlL2tpStatsTunnelRecvSeq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsTunnelRecvSeq_Type.__name__=_D
_AlL2tpStatsTunnelRecvSeq_Object=MibTableColumn
alL2tpStatsTunnelRecvSeq=_AlL2tpStatsTunnelRecvSeq_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,25),_AlL2tpStatsTunnelRecvSeq_Type())
alL2tpStatsTunnelRecvSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelRecvSeq.setStatus(_C)
class _AlL2tpStatsTunnelRecvSeqAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsTunnelRecvSeqAck_Type.__name__=_D
_AlL2tpStatsTunnelRecvSeqAck_Object=MibTableColumn
alL2tpStatsTunnelRecvSeqAck=_AlL2tpStatsTunnelRecvSeqAck_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,26),_AlL2tpStatsTunnelRecvSeqAck_Type())
alL2tpStatsTunnelRecvSeqAck.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelRecvSeqAck.setStatus(_C)
_AlL2tpStatsTunnelTotalSessions_Type=Counter32
_AlL2tpStatsTunnelTotalSessions_Object=MibTableColumn
alL2tpStatsTunnelTotalSessions=_AlL2tpStatsTunnelTotalSessions_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,27),_AlL2tpStatsTunnelTotalSessions_Type())
alL2tpStatsTunnelTotalSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelTotalSessions.setStatus(_C)
_AlL2tpStatsTunnelFailedSessions_Type=Counter32
_AlL2tpStatsTunnelFailedSessions_Object=MibTableColumn
alL2tpStatsTunnelFailedSessions=_AlL2tpStatsTunnelFailedSessions_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,28),_AlL2tpStatsTunnelFailedSessions_Type())
alL2tpStatsTunnelFailedSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelFailedSessions.setStatus(_C)
_AlL2tpStatsTunnelActiveSessions_Type=Gauge32
_AlL2tpStatsTunnelActiveSessions_Object=MibTableColumn
alL2tpStatsTunnelActiveSessions=_AlL2tpStatsTunnelActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,29),_AlL2tpStatsTunnelActiveSessions_Type())
alL2tpStatsTunnelActiveSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelActiveSessions.setStatus(_C)
class _AlL2tpStatsTunnelLastResultCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsTunnelLastResultCode_Type.__name__=_D
_AlL2tpStatsTunnelLastResultCode_Object=MibTableColumn
alL2tpStatsTunnelLastResultCode=_AlL2tpStatsTunnelLastResultCode_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,30),_AlL2tpStatsTunnelLastResultCode_Type())
alL2tpStatsTunnelLastResultCode.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelLastResultCode.setStatus(_C)
class _AlL2tpStatsTunnelLastErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsTunnelLastErrorCode_Type.__name__=_D
_AlL2tpStatsTunnelLastErrorCode_Object=MibTableColumn
alL2tpStatsTunnelLastErrorCode=_AlL2tpStatsTunnelLastErrorCode_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,31),_AlL2tpStatsTunnelLastErrorCode_Type())
alL2tpStatsTunnelLastErrorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelLastErrorCode.setStatus(_C)
_AlL2tpStatsTunnelLastErrorMessage_Type=DisplayString
_AlL2tpStatsTunnelLastErrorMessage_Object=MibTableColumn
alL2tpStatsTunnelLastErrorMessage=_AlL2tpStatsTunnelLastErrorMessage_Object((1,3,6,1,4,1,3076,2,1,2,16,2,1,32),_AlL2tpStatsTunnelLastErrorMessage_Type())
alL2tpStatsTunnelLastErrorMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsTunnelLastErrorMessage.setStatus(_C)
_AlL2tpStatsSessionTable_Object=MibTable
alL2tpStatsSessionTable=_AlL2tpStatsSessionTable_Object((1,3,6,1,4,1,3076,2,1,2,16,3))
if mibBuilder.loadTexts:alL2tpStatsSessionTable.setStatus(_C)
_AlL2tpStatsSessionEntry_Object=MibTableRow
alL2tpStatsSessionEntry=_AlL2tpStatsSessionEntry_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1))
alL2tpStatsSessionEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:alL2tpStatsSessionEntry.setStatus(_C)
_AlL2tpStatsSessionRowStatus_Type=RowStatus
_AlL2tpStatsSessionRowStatus_Object=MibTableColumn
alL2tpStatsSessionRowStatus=_AlL2tpStatsSessionRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,1),_AlL2tpStatsSessionRowStatus_Type())
alL2tpStatsSessionRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:alL2tpStatsSessionRowStatus.setStatus(_C)
_AlL2tpStatsSessionIfIndex_Type=InterfaceIndex
_AlL2tpStatsSessionIfIndex_Object=MibTableColumn
alL2tpStatsSessionIfIndex=_AlL2tpStatsSessionIfIndex_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,2),_AlL2tpStatsSessionIfIndex_Type())
alL2tpStatsSessionIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionIfIndex.setStatus(_C)
class _AlL2tpStatsSessionTID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionTID_Type.__name__=_D
_AlL2tpStatsSessionTID_Object=MibTableColumn
alL2tpStatsSessionTID=_AlL2tpStatsSessionTID_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,3),_AlL2tpStatsSessionTID_Type())
alL2tpStatsSessionTID.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionTID.setStatus(_C)
class _AlL2tpStatsSessionLocalCID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionLocalCID_Type.__name__=_D
_AlL2tpStatsSessionLocalCID_Object=MibTableColumn
alL2tpStatsSessionLocalCID=_AlL2tpStatsSessionLocalCID_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,4),_AlL2tpStatsSessionLocalCID_Type())
alL2tpStatsSessionLocalCID.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionLocalCID.setStatus(_C)
class _AlL2tpStatsSessionRemoteCID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionRemoteCID_Type.__name__=_D
_AlL2tpStatsSessionRemoteCID_Object=MibTableColumn
alL2tpStatsSessionRemoteCID=_AlL2tpStatsSessionRemoteCID_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,5),_AlL2tpStatsSessionRemoteCID_Type())
alL2tpStatsSessionRemoteCID.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRemoteCID.setStatus(_C)
_AlL2tpStatsSessionUserName_Type=DisplayString
_AlL2tpStatsSessionUserName_Object=MibTableColumn
alL2tpStatsSessionUserName=_AlL2tpStatsSessionUserName_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,6),_AlL2tpStatsSessionUserName_Type())
alL2tpStatsSessionUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionUserName.setStatus(_C)
class _AlL2tpStatsSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sessionIdle',1),('sessionConnecting',2),('sessionEstablished',3),('sessionDisconnecting',4)))
_AlL2tpStatsSessionState_Type.__name__=_D
_AlL2tpStatsSessionState_Object=MibTableColumn
alL2tpStatsSessionState=_AlL2tpStatsSessionState_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,7),_AlL2tpStatsSessionState_Type())
alL2tpStatsSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionState.setStatus(_C)
class _AlL2tpStatsSessionCallType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lacIncoming',1),('lnsIncoming',2),('lacOutgoing',3),('lnsOutgoing',4)))
_AlL2tpStatsSessionCallType_Type.__name__=_D
_AlL2tpStatsSessionCallType_Object=MibTableColumn
alL2tpStatsSessionCallType=_AlL2tpStatsSessionCallType_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,8),_AlL2tpStatsSessionCallType_Type())
alL2tpStatsSessionCallType.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionCallType.setStatus(_C)
_AlL2tpStatsSessionCallSerialNumber_Type=Unsigned32
_AlL2tpStatsSessionCallSerialNumber_Object=MibTableColumn
alL2tpStatsSessionCallSerialNumber=_AlL2tpStatsSessionCallSerialNumber_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,9),_AlL2tpStatsSessionCallSerialNumber_Type())
alL2tpStatsSessionCallSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionCallSerialNumber.setStatus(_C)
_AlL2tpStatsSessionTxConnectSpeed_Type=Integer32
_AlL2tpStatsSessionTxConnectSpeed_Object=MibTableColumn
alL2tpStatsSessionTxConnectSpeed=_AlL2tpStatsSessionTxConnectSpeed_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,10),_AlL2tpStatsSessionTxConnectSpeed_Type())
alL2tpStatsSessionTxConnectSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionTxConnectSpeed.setStatus(_C)
_AlL2tpStatsSessionRxConnectSpeed_Type=Integer32
_AlL2tpStatsSessionRxConnectSpeed_Object=MibTableColumn
alL2tpStatsSessionRxConnectSpeed=_AlL2tpStatsSessionRxConnectSpeed_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,11),_AlL2tpStatsSessionRxConnectSpeed_Type())
alL2tpStatsSessionRxConnectSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRxConnectSpeed.setStatus(_C)
class _AlL2tpStatsSessionCallBearerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AlL2tpStatsSessionCallBearerType_Type.__name__=_D
_AlL2tpStatsSessionCallBearerType_Object=MibTableColumn
alL2tpStatsSessionCallBearerType=_AlL2tpStatsSessionCallBearerType_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,12),_AlL2tpStatsSessionCallBearerType_Type())
alL2tpStatsSessionCallBearerType.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionCallBearerType.setStatus(_C)
class _AlL2tpStatsSessionFramingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('asynchronous',1),('synchronous',2)))
_AlL2tpStatsSessionFramingType_Type.__name__=_D
_AlL2tpStatsSessionFramingType_Object=MibTableColumn
alL2tpStatsSessionFramingType=_AlL2tpStatsSessionFramingType_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,13),_AlL2tpStatsSessionFramingType_Type())
alL2tpStatsSessionFramingType.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionFramingType.setStatus(_C)
_AlL2tpStatsSessionPhysChanId_Type=Integer32
_AlL2tpStatsSessionPhysChanId_Object=MibTableColumn
alL2tpStatsSessionPhysChanId=_AlL2tpStatsSessionPhysChanId_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,14),_AlL2tpStatsSessionPhysChanId_Type())
alL2tpStatsSessionPhysChanId.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionPhysChanId.setStatus(_C)
_AlL2tpStatsSessionDNIS_Type=DisplayString
_AlL2tpStatsSessionDNIS_Object=MibTableColumn
alL2tpStatsSessionDNIS=_AlL2tpStatsSessionDNIS_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,15),_AlL2tpStatsSessionDNIS_Type())
alL2tpStatsSessionDNIS.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionDNIS.setStatus(_C)
_AlL2tpStatsSessionCLID_Type=DisplayString
_AlL2tpStatsSessionCLID_Object=MibTableColumn
alL2tpStatsSessionCLID=_AlL2tpStatsSessionCLID_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,16),_AlL2tpStatsSessionCLID_Type())
alL2tpStatsSessionCLID.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionCLID.setStatus(_C)
_AlL2tpStatsSessionSubAddress_Type=DisplayString
_AlL2tpStatsSessionSubAddress_Object=MibTableColumn
alL2tpStatsSessionSubAddress=_AlL2tpStatsSessionSubAddress_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,17),_AlL2tpStatsSessionSubAddress_Type())
alL2tpStatsSessionSubAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionSubAddress.setStatus(_C)
_AlL2tpStatsSessionPrivateGroupID_Type=DisplayString
_AlL2tpStatsSessionPrivateGroupID_Object=MibTableColumn
alL2tpStatsSessionPrivateGroupID=_AlL2tpStatsSessionPrivateGroupID_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,18),_AlL2tpStatsSessionPrivateGroupID_Type())
alL2tpStatsSessionPrivateGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionPrivateGroupID.setStatus(_C)
_AlL2tpStatsSessionProxyLcp_Type=TruthValue
_AlL2tpStatsSessionProxyLcp_Object=MibTableColumn
alL2tpStatsSessionProxyLcp=_AlL2tpStatsSessionProxyLcp_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,19),_AlL2tpStatsSessionProxyLcp_Type())
alL2tpStatsSessionProxyLcp.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionProxyLcp.setStatus(_C)
class _AlL2tpStatsSessionAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('text',2),('pppChap',3),('pppPap',4)))
_AlL2tpStatsSessionAuthMethod_Type.__name__=_D
_AlL2tpStatsSessionAuthMethod_Object=MibTableColumn
alL2tpStatsSessionAuthMethod=_AlL2tpStatsSessionAuthMethod_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,20),_AlL2tpStatsSessionAuthMethod_Type())
alL2tpStatsSessionAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionAuthMethod.setStatus(_C)
class _AlL2tpStatsSessionLocalRWS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionLocalRWS_Type.__name__=_D
_AlL2tpStatsSessionLocalRWS_Object=MibTableColumn
alL2tpStatsSessionLocalRWS=_AlL2tpStatsSessionLocalRWS_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,21),_AlL2tpStatsSessionLocalRWS_Type())
alL2tpStatsSessionLocalRWS.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionLocalRWS.setStatus(_E)
class _AlL2tpStatsSessionRemoteInitialRWS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionRemoteInitialRWS_Type.__name__=_D
_AlL2tpStatsSessionRemoteInitialRWS_Object=MibTableColumn
alL2tpStatsSessionRemoteInitialRWS=_AlL2tpStatsSessionRemoteInitialRWS_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,22),_AlL2tpStatsSessionRemoteInitialRWS_Type())
alL2tpStatsSessionRemoteInitialRWS.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRemoteInitialRWS.setStatus(_E)
_AlL2tpStatsSessionRemotePPD_Type=Integer32
_AlL2tpStatsSessionRemotePPD_Object=MibTableColumn
alL2tpStatsSessionRemotePPD=_AlL2tpStatsSessionRemotePPD_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,23),_AlL2tpStatsSessionRemotePPD_Type())
alL2tpStatsSessionRemotePPD.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRemotePPD.setStatus(_C)
class _AlL2tpStatsSessionSequencingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('remote',2),('local',3),('both',4)))
_AlL2tpStatsSessionSequencingState_Type.__name__=_D
_AlL2tpStatsSessionSequencingState_Object=MibTableColumn
alL2tpStatsSessionSequencingState=_AlL2tpStatsSessionSequencingState_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,24),_AlL2tpStatsSessionSequencingState_Type())
alL2tpStatsSessionSequencingState.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionSequencingState.setStatus(_C)
_AlL2tpStatsSessionRecvOctets_Type=Counter32
_AlL2tpStatsSessionRecvOctets_Object=MibTableColumn
alL2tpStatsSessionRecvOctets=_AlL2tpStatsSessionRecvOctets_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,25),_AlL2tpStatsSessionRecvOctets_Type())
alL2tpStatsSessionRecvOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRecvOctets.setStatus(_C)
_AlL2tpStatsSessionRecvPackets_Type=Counter32
_AlL2tpStatsSessionRecvPackets_Object=MibTableColumn
alL2tpStatsSessionRecvPackets=_AlL2tpStatsSessionRecvPackets_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,26),_AlL2tpStatsSessionRecvPackets_Type())
alL2tpStatsSessionRecvPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRecvPackets.setStatus(_C)
_AlL2tpStatsSessionRecvDiscards_Type=Counter32
_AlL2tpStatsSessionRecvDiscards_Object=MibTableColumn
alL2tpStatsSessionRecvDiscards=_AlL2tpStatsSessionRecvDiscards_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,27),_AlL2tpStatsSessionRecvDiscards_Type())
alL2tpStatsSessionRecvDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRecvDiscards.setStatus(_C)
_AlL2tpStatsSessionRecvZLB_Type=Counter32
_AlL2tpStatsSessionRecvZLB_Object=MibTableColumn
alL2tpStatsSessionRecvZLB=_AlL2tpStatsSessionRecvZLB_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,28),_AlL2tpStatsSessionRecvZLB_Type())
alL2tpStatsSessionRecvZLB.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRecvZLB.setStatus(_E)
_AlL2tpStatsSessionOutSequence_Type=Counter32
_AlL2tpStatsSessionOutSequence_Object=MibTableColumn
alL2tpStatsSessionOutSequence=_AlL2tpStatsSessionOutSequence_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,29),_AlL2tpStatsSessionOutSequence_Type())
alL2tpStatsSessionOutSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionOutSequence.setStatus(_C)
_AlL2tpStatsSessionOutOfWindow_Type=Counter32
_AlL2tpStatsSessionOutOfWindow_Object=MibTableColumn
alL2tpStatsSessionOutOfWindow=_AlL2tpStatsSessionOutOfWindow_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,30),_AlL2tpStatsSessionOutOfWindow_Type())
alL2tpStatsSessionOutOfWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionOutOfWindow.setStatus(_E)
_AlL2tpStatsSessionSendOctets_Type=Counter32
_AlL2tpStatsSessionSendOctets_Object=MibTableColumn
alL2tpStatsSessionSendOctets=_AlL2tpStatsSessionSendOctets_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,31),_AlL2tpStatsSessionSendOctets_Type())
alL2tpStatsSessionSendOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionSendOctets.setStatus(_C)
_AlL2tpStatsSessionSendPackets_Type=Counter32
_AlL2tpStatsSessionSendPackets_Object=MibTableColumn
alL2tpStatsSessionSendPackets=_AlL2tpStatsSessionSendPackets_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,32),_AlL2tpStatsSessionSendPackets_Type())
alL2tpStatsSessionSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionSendPackets.setStatus(_C)
_AlL2tpStatsSessionSendZLB_Type=Counter32
_AlL2tpStatsSessionSendZLB_Object=MibTableColumn
alL2tpStatsSessionSendZLB=_AlL2tpStatsSessionSendZLB_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,33),_AlL2tpStatsSessionSendZLB_Type())
alL2tpStatsSessionSendZLB.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionSendZLB.setStatus(_E)
_AlL2tpStatsSessionAckTimeouts_Type=Counter32
_AlL2tpStatsSessionAckTimeouts_Object=MibTableColumn
alL2tpStatsSessionAckTimeouts=_AlL2tpStatsSessionAckTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,34),_AlL2tpStatsSessionAckTimeouts_Type())
alL2tpStatsSessionAckTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionAckTimeouts.setStatus(_E)
_AlL2tpStatsSessionReassemblyTimeouts_Type=Counter32
_AlL2tpStatsSessionReassemblyTimeouts_Object=MibTableColumn
alL2tpStatsSessionReassemblyTimeouts=_AlL2tpStatsSessionReassemblyTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,35),_AlL2tpStatsSessionReassemblyTimeouts_Type())
alL2tpStatsSessionReassemblyTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionReassemblyTimeouts.setStatus(_C)
class _AlL2tpStatsSessionCurrentRemoteRWS_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionCurrentRemoteRWS_Type.__name__=_G
_AlL2tpStatsSessionCurrentRemoteRWS_Object=MibTableColumn
alL2tpStatsSessionCurrentRemoteRWS=_AlL2tpStatsSessionCurrentRemoteRWS_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,36),_AlL2tpStatsSessionCurrentRemoteRWS_Type())
alL2tpStatsSessionCurrentRemoteRWS.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionCurrentRemoteRWS.setStatus(_E)
class _AlL2tpStatsSessionSendSeq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionSendSeq_Type.__name__=_D
_AlL2tpStatsSessionSendSeq_Object=MibTableColumn
alL2tpStatsSessionSendSeq=_AlL2tpStatsSessionSendSeq_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,37),_AlL2tpStatsSessionSendSeq_Type())
alL2tpStatsSessionSendSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionSendSeq.setStatus(_C)
class _AlL2tpStatsSessionSendSeqAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionSendSeqAck_Type.__name__=_D
_AlL2tpStatsSessionSendSeqAck_Object=MibTableColumn
alL2tpStatsSessionSendSeqAck=_AlL2tpStatsSessionSendSeqAck_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,38),_AlL2tpStatsSessionSendSeqAck_Type())
alL2tpStatsSessionSendSeqAck.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionSendSeqAck.setStatus(_C)
_AlL2tpStatsSessionSendSeqResets_Type=Counter32
_AlL2tpStatsSessionSendSeqResets_Object=MibTableColumn
alL2tpStatsSessionSendSeqResets=_AlL2tpStatsSessionSendSeqResets_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,39),_AlL2tpStatsSessionSendSeqResets_Type())
alL2tpStatsSessionSendSeqResets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionSendSeqResets.setStatus(_E)
class _AlL2tpStatsSessionRecvSeq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionRecvSeq_Type.__name__=_D
_AlL2tpStatsSessionRecvSeq_Object=MibTableColumn
alL2tpStatsSessionRecvSeq=_AlL2tpStatsSessionRecvSeq_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,40),_AlL2tpStatsSessionRecvSeq_Type())
alL2tpStatsSessionRecvSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRecvSeq.setStatus(_C)
class _AlL2tpStatsSessionRecvSeqAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlL2tpStatsSessionRecvSeqAck_Type.__name__=_D
_AlL2tpStatsSessionRecvSeqAck_Object=MibTableColumn
alL2tpStatsSessionRecvSeqAck=_AlL2tpStatsSessionRecvSeqAck_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,41),_AlL2tpStatsSessionRecvSeqAck_Type())
alL2tpStatsSessionRecvSeqAck.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRecvSeqAck.setStatus(_C)
_AlL2tpStatsSessionRecvSeqResets_Type=Counter32
_AlL2tpStatsSessionRecvSeqResets_Object=MibTableColumn
alL2tpStatsSessionRecvSeqResets=_AlL2tpStatsSessionRecvSeqResets_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,42),_AlL2tpStatsSessionRecvSeqResets_Type())
alL2tpStatsSessionRecvSeqResets.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionRecvSeqResets.setStatus(_E)
_AlL2tpStatsSessionTunnelPeerIpAddr_Type=IpAddress
_AlL2tpStatsSessionTunnelPeerIpAddr_Object=MibTableColumn
alL2tpStatsSessionTunnelPeerIpAddr=_AlL2tpStatsSessionTunnelPeerIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,16,3,1,43),_AlL2tpStatsSessionTunnelPeerIpAddr_Type())
alL2tpStatsSessionTunnelPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:alL2tpStatsSessionTunnelPeerIpAddr.setStatus(_C)
altigaL2tpStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,16,2))
altigaL2tpStatsGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_H),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_I),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:altigaL2tpStatsGroup.setStatus(_C)
altigaL2tpStatsDepGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,16,3))
altigaL2tpStatsDepGroup.setObjects(*((_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:altigaL2tpStatsDepGroup.setStatus(_E)
altigaL2tpStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,21,2,1,1,1))
altigaL2tpStatsMibCompliance.setObjects((_A,_At))
if mibBuilder.loadTexts:altigaL2tpStatsMibCompliance.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'altigaL2tpStatsMibModule':altigaL2tpStatsMibModule,'altigaL2tpStatsMibConformance':altigaL2tpStatsMibConformance,'altigaL2tpStatsMibCompliances':altigaL2tpStatsMibCompliances,'altigaL2tpStatsMibCompliance':altigaL2tpStatsMibCompliance,_At:altigaL2tpStatsGroup,'altigaL2tpStatsDepGroup':altigaL2tpStatsDepGroup,'alStatsL2tpGlobal':alStatsL2tpGlobal,_M:alL2tpStatsLocalProtVers,_N:alL2tpStatsVendorName,_O:alL2tpStatsFirmwareRev,_P:alL2tpStatsTotalTunnels,_Q:alL2tpStatsFailedTunnels,_R:alL2tpStatsFailedAuthentications,_S:alL2tpStatsActiveTunnels,_T:alL2tpStatsMaxTunnels,_U:alL2tpStatsTotalSessions,_V:alL2tpStatsFailedSessions,_W:alL2tpStatsActiveSessions,_X:alL2tpStatsMaxSessions,_Y:alL2tpStatsControlRecvOctets,_Z:alL2tpStatsControlRecvPackets,_a:alL2tpStatsControlRecvDiscards,_b:alL2tpStatsControlSendOctets,_c:alL2tpStatsControlSendPackets,_d:alL2tpStatsPayloadRecvOctets,_e:alL2tpStatsPayloadRecvPackets,_f:alL2tpStatsPayloadRecvDiscards,_g:alL2tpStatsPayloadSendOctets,_h:alL2tpStatsPayloadSendPackets,'alL2tpStatsTunnelTable':alL2tpStatsTunnelTable,'alL2tpStatsTunnelEntry':alL2tpStatsTunnelEntry,_i:alL2tpStatsTunnelRowStatus,_H:alL2tpStatsTunnelPeerIpAddr,_j:alL2tpStatsTunnelLocalTID,_k:alL2tpStatsTunnelRemoteTID,_l:alL2tpStatsTunnelState,_m:alL2tpStatsTunnelInitiated,_n:alL2tpStatsTunnelRemoteHostName,_o:alL2tpStatsTunnelRemoteVendorName,_p:alL2tpStatsTunnelRemoteFirmwareRevision,_q:alL2tpStatsTunnelRemoteProtocolVersion,_r:alL2tpStatsTunnelInitialRemoteRWS,_s:alL2tpStatsTunnelBearerCapabilities,_t:alL2tpStatsTunnelFramingCapabilities,_u:alL2tpStatsTunnelControlRecvPackets,_v:alL2tpStatsTunnelControlRecvDiscards,_w:alL2tpStatsTunnelControlRecvZLB,_x:alL2tpStatsTunnelControlOutOfSequence,_y:alL2tpStatsTunnelControlOutOfWindow,_z:alL2tpStatsTunnelControlSendPackets,_A0:alL2tpStatsTunnelControlSendZLB,_A1:alL2tpStatsTunnelControlAckTimeouts,_A2:alL2tpStatsTunnelCurrentRemoteRWS,_A3:alL2tpStatsTunnelSendSeq,_A4:alL2tpStatsTunnelSendSeqAck,_A5:alL2tpStatsTunnelRecvSeq,_A6:alL2tpStatsTunnelRecvSeqAck,_A7:alL2tpStatsTunnelTotalSessions,_A8:alL2tpStatsTunnelFailedSessions,_A9:alL2tpStatsTunnelActiveSessions,_AA:alL2tpStatsTunnelLastResultCode,_AB:alL2tpStatsTunnelLastErrorCode,_AC:alL2tpStatsTunnelLastErrorMessage,'alL2tpStatsSessionTable':alL2tpStatsSessionTable,'alL2tpStatsSessionEntry':alL2tpStatsSessionEntry,_AD:alL2tpStatsSessionRowStatus,_I:alL2tpStatsSessionIfIndex,_AE:alL2tpStatsSessionTID,_AF:alL2tpStatsSessionLocalCID,_AG:alL2tpStatsSessionRemoteCID,_AH:alL2tpStatsSessionUserName,_AI:alL2tpStatsSessionState,_AJ:alL2tpStatsSessionCallType,_AK:alL2tpStatsSessionCallSerialNumber,_AL:alL2tpStatsSessionTxConnectSpeed,_AM:alL2tpStatsSessionRxConnectSpeed,_AN:alL2tpStatsSessionCallBearerType,_AO:alL2tpStatsSessionFramingType,_AP:alL2tpStatsSessionPhysChanId,_AQ:alL2tpStatsSessionDNIS,_AR:alL2tpStatsSessionCLID,_AS:alL2tpStatsSessionSubAddress,_AT:alL2tpStatsSessionPrivateGroupID,_AU:alL2tpStatsSessionProxyLcp,_AV:alL2tpStatsSessionAuthMethod,_Ak:alL2tpStatsSessionLocalRWS,_Al:alL2tpStatsSessionRemoteInitialRWS,_AW:alL2tpStatsSessionRemotePPD,_AX:alL2tpStatsSessionSequencingState,_AY:alL2tpStatsSessionRecvOctets,_AZ:alL2tpStatsSessionRecvPackets,_Aa:alL2tpStatsSessionRecvDiscards,_Am:alL2tpStatsSessionRecvZLB,_Ab:alL2tpStatsSessionOutSequence,_Ao:alL2tpStatsSessionOutOfWindow,_Ac:alL2tpStatsSessionSendOctets,_Ad:alL2tpStatsSessionSendPackets,_An:alL2tpStatsSessionSendZLB,_Ap:alL2tpStatsSessionAckTimeouts,_Ae:alL2tpStatsSessionReassemblyTimeouts,_Aq:alL2tpStatsSessionCurrentRemoteRWS,_Af:alL2tpStatsSessionSendSeq,_Ag:alL2tpStatsSessionSendSeqAck,_Ar:alL2tpStatsSessionSendSeqResets,_Ah:alL2tpStatsSessionRecvSeq,_Ai:alL2tpStatsSessionRecvSeqAck,_As:alL2tpStatsSessionRecvSeqResets,_Aj:alL2tpStatsSessionTunnelPeerIpAddr})