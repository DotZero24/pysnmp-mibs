_AF='altigaPptpStatsGroup'
_AE='alPptpStatsSessionTunnelPeerIpAddr'
_AD='alPptpStatsSessionOutOfSequence'
_AC='alPptpStatsSessionOutOfWindow'
_AB='alPptpStatsSessionPeerFlowOff'
_AA='alPptpStatsSessionLocalFlowOff'
_A9='alPptpStatsSessionAckTimeouts'
_A8='alPptpStatsSessionSendZLB'
_A7='alPptpStatsSessionSendPackets'
_A6='alPptpStatsSessionSendOctets'
_A5='alPptpStatsSessionRecvZLB'
_A4='alPptpStatsSessionRecvDiscards'
_A3='alPptpStatsSessionRecvPackets'
_A2='alPptpStatsSessionRecvOctets'
_A1='alPptpStatsSessionPeerPpd'
_A0='alPptpStatsSessionLocalPpd'
_z='alPptpStatsSessionPeerWindowSize'
_y='alPptpStatsSessionLocalWindowSize'
_x='alPptpStatsSessionPhysicalChannel'
_w='alPptpStatsSessionFramingType'
_v='alPptpStatsSessionBearerType'
_u='alPptpStatsSessionConnectSpeed'
_t='alPptpStatsSessionMaximumSpeed'
_s='alPptpStatsSessionMinimumSpeed'
_r='alPptpStatsSessionSerial'
_q='alPptpStatsSessionUserName'
_p='alPptpStatsSessionPeerCallId'
_o='alPptpStatsSessionLocalCallId'
_n='alPptpStatsSessionRowStatus'
_m='alPptpStatsTunnelActiveSessions'
_l='alPptpStatsTunnelPeerMaxChan'
_k='alPptpStatsTunnelPeerBearerCap'
_j='alPptpStatsTunnelPeerFramingCap'
_i='alPptpStatsTunnelPeerProtVers'
_h='alPptpStatsTunnelPeerFirmwareRev'
_g='alPptpStatsTunnelPeerVendorName'
_f='alPptpStatsTunnelPeerHostName'
_e='alPptpStatsTunnelLocalIpAddr'
_d='alPptpStatsTunnelDatastreamId'
_c='alPptpStatsTunnelRowStatus'
_b='alPptpStatsPayloadSendPackets'
_a='alPptpStatsPayloadSendOctets'
_Z='alPptpStatsPayloadRecvDiscards'
_Y='alPptpStatsPayloadRecvPackets'
_X='alPptpStatsPayloadRecvOctets'
_W='alPptpStatsControlSendPackets'
_V='alPptpStatsControlSendOctets'
_U='alPptpStatsControlRecvDiscards'
_T='alPptpStatsControlRecvPackets'
_S='alPptpStatsControlRecvOctets'
_R='alPptpStatsMaxSessions'
_Q='alPptpStatsActiveSessions'
_P='alPptpStatsTotalSessions'
_O='alPptpStatsMaxTunnels'
_N='alPptpStatsActiveTunnels'
_M='alPptpStatsTotalTunnels'
_L='alPptpStatsLocalFirmwareRev'
_K='alPptpStatsLocalBearer'
_J='alPptpStatsLocalFraming'
_I='alPptpStatsLocalProtVers'
_H='read-write'
_G='alPptpStatsSessionDatastreamId'
_F='alPptpStatsTunnelPeerIpAddr'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='ALTIGA-PPTP-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alPptpMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alPptpMibModule')
alPptpGroup,alStatsPptp=mibBuilder.importSymbols('ALTIGA-MIB','alPptpGroup','alStatsPptp')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
altigaPptpStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,10,2))
if mibBuilder.loadTexts:altigaPptpStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaPptpStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaPptpStatsMibConformance=_AltigaPptpStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,10,2,1))
_AltigaPptpStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaPptpStatsMibCompliances=_AltigaPptpStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,10,2,1,1))
_AlStatsPptpGlobal_ObjectIdentity=ObjectIdentity
alStatsPptpGlobal=_AlStatsPptpGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,3,1))
class _AlPptpStatsLocalProtVers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AlPptpStatsLocalProtVers_Type.__name__=_E
_AlPptpStatsLocalProtVers_Object=MibScalar
alPptpStatsLocalProtVers=_AlPptpStatsLocalProtVers_Object((1,3,6,1,4,1,3076,2,1,2,3,1,1),_AlPptpStatsLocalProtVers_Type())
alPptpStatsLocalProtVers.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsLocalProtVers.setStatus(_A)
class _AlPptpStatsLocalFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AlPptpStatsLocalFraming_Type.__name__=_D
_AlPptpStatsLocalFraming_Object=MibScalar
alPptpStatsLocalFraming=_AlPptpStatsLocalFraming_Object((1,3,6,1,4,1,3076,2,1,2,3,1,2),_AlPptpStatsLocalFraming_Type())
alPptpStatsLocalFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsLocalFraming.setStatus(_A)
class _AlPptpStatsLocalBearer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AlPptpStatsLocalBearer_Type.__name__=_D
_AlPptpStatsLocalBearer_Object=MibScalar
alPptpStatsLocalBearer=_AlPptpStatsLocalBearer_Object((1,3,6,1,4,1,3076,2,1,2,3,1,3),_AlPptpStatsLocalBearer_Type())
alPptpStatsLocalBearer.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsLocalBearer.setStatus(_A)
class _AlPptpStatsLocalFirmwareRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AlPptpStatsLocalFirmwareRev_Type.__name__=_E
_AlPptpStatsLocalFirmwareRev_Object=MibScalar
alPptpStatsLocalFirmwareRev=_AlPptpStatsLocalFirmwareRev_Object((1,3,6,1,4,1,3076,2,1,2,3,1,4),_AlPptpStatsLocalFirmwareRev_Type())
alPptpStatsLocalFirmwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsLocalFirmwareRev.setStatus(_A)
_AlPptpStatsTotalTunnels_Type=Gauge32
_AlPptpStatsTotalTunnels_Object=MibScalar
alPptpStatsTotalTunnels=_AlPptpStatsTotalTunnels_Object((1,3,6,1,4,1,3076,2,1,2,3,1,5),_AlPptpStatsTotalTunnels_Type())
alPptpStatsTotalTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTotalTunnels.setStatus(_A)
_AlPptpStatsActiveTunnels_Type=Gauge32
_AlPptpStatsActiveTunnels_Object=MibScalar
alPptpStatsActiveTunnels=_AlPptpStatsActiveTunnels_Object((1,3,6,1,4,1,3076,2,1,2,3,1,6),_AlPptpStatsActiveTunnels_Type())
alPptpStatsActiveTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsActiveTunnels.setStatus(_A)
_AlPptpStatsMaxTunnels_Type=Gauge32
_AlPptpStatsMaxTunnels_Object=MibScalar
alPptpStatsMaxTunnels=_AlPptpStatsMaxTunnels_Object((1,3,6,1,4,1,3076,2,1,2,3,1,7),_AlPptpStatsMaxTunnels_Type())
alPptpStatsMaxTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsMaxTunnels.setStatus(_A)
_AlPptpStatsTotalSessions_Type=Gauge32
_AlPptpStatsTotalSessions_Object=MibScalar
alPptpStatsTotalSessions=_AlPptpStatsTotalSessions_Object((1,3,6,1,4,1,3076,2,1,2,3,1,8),_AlPptpStatsTotalSessions_Type())
alPptpStatsTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTotalSessions.setStatus(_A)
_AlPptpStatsActiveSessions_Type=Gauge32
_AlPptpStatsActiveSessions_Object=MibScalar
alPptpStatsActiveSessions=_AlPptpStatsActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,3,1,9),_AlPptpStatsActiveSessions_Type())
alPptpStatsActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsActiveSessions.setStatus(_A)
_AlPptpStatsMaxSessions_Type=Gauge32
_AlPptpStatsMaxSessions_Object=MibScalar
alPptpStatsMaxSessions=_AlPptpStatsMaxSessions_Object((1,3,6,1,4,1,3076,2,1,2,3,1,10),_AlPptpStatsMaxSessions_Type())
alPptpStatsMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsMaxSessions.setStatus(_A)
_AlPptpStatsControlRecvOctets_Type=Counter32
_AlPptpStatsControlRecvOctets_Object=MibScalar
alPptpStatsControlRecvOctets=_AlPptpStatsControlRecvOctets_Object((1,3,6,1,4,1,3076,2,1,2,3,1,11),_AlPptpStatsControlRecvOctets_Type())
alPptpStatsControlRecvOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsControlRecvOctets.setStatus(_A)
_AlPptpStatsControlRecvPackets_Type=Counter32
_AlPptpStatsControlRecvPackets_Object=MibScalar
alPptpStatsControlRecvPackets=_AlPptpStatsControlRecvPackets_Object((1,3,6,1,4,1,3076,2,1,2,3,1,12),_AlPptpStatsControlRecvPackets_Type())
alPptpStatsControlRecvPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsControlRecvPackets.setStatus(_A)
_AlPptpStatsControlRecvDiscards_Type=Counter32
_AlPptpStatsControlRecvDiscards_Object=MibScalar
alPptpStatsControlRecvDiscards=_AlPptpStatsControlRecvDiscards_Object((1,3,6,1,4,1,3076,2,1,2,3,1,13),_AlPptpStatsControlRecvDiscards_Type())
alPptpStatsControlRecvDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsControlRecvDiscards.setStatus(_A)
_AlPptpStatsControlSendOctets_Type=Counter32
_AlPptpStatsControlSendOctets_Object=MibScalar
alPptpStatsControlSendOctets=_AlPptpStatsControlSendOctets_Object((1,3,6,1,4,1,3076,2,1,2,3,1,14),_AlPptpStatsControlSendOctets_Type())
alPptpStatsControlSendOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsControlSendOctets.setStatus(_A)
_AlPptpStatsControlSendPackets_Type=Counter32
_AlPptpStatsControlSendPackets_Object=MibScalar
alPptpStatsControlSendPackets=_AlPptpStatsControlSendPackets_Object((1,3,6,1,4,1,3076,2,1,2,3,1,15),_AlPptpStatsControlSendPackets_Type())
alPptpStatsControlSendPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsControlSendPackets.setStatus(_A)
_AlPptpStatsPayloadRecvOctets_Type=Counter32
_AlPptpStatsPayloadRecvOctets_Object=MibScalar
alPptpStatsPayloadRecvOctets=_AlPptpStatsPayloadRecvOctets_Object((1,3,6,1,4,1,3076,2,1,2,3,1,16),_AlPptpStatsPayloadRecvOctets_Type())
alPptpStatsPayloadRecvOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsPayloadRecvOctets.setStatus(_A)
_AlPptpStatsPayloadRecvPackets_Type=Counter32
_AlPptpStatsPayloadRecvPackets_Object=MibScalar
alPptpStatsPayloadRecvPackets=_AlPptpStatsPayloadRecvPackets_Object((1,3,6,1,4,1,3076,2,1,2,3,1,17),_AlPptpStatsPayloadRecvPackets_Type())
alPptpStatsPayloadRecvPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsPayloadRecvPackets.setStatus(_A)
_AlPptpStatsPayloadRecvDiscards_Type=Counter32
_AlPptpStatsPayloadRecvDiscards_Object=MibScalar
alPptpStatsPayloadRecvDiscards=_AlPptpStatsPayloadRecvDiscards_Object((1,3,6,1,4,1,3076,2,1,2,3,1,18),_AlPptpStatsPayloadRecvDiscards_Type())
alPptpStatsPayloadRecvDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsPayloadRecvDiscards.setStatus(_A)
_AlPptpStatsPayloadSendOctets_Type=Counter32
_AlPptpStatsPayloadSendOctets_Object=MibScalar
alPptpStatsPayloadSendOctets=_AlPptpStatsPayloadSendOctets_Object((1,3,6,1,4,1,3076,2,1,2,3,1,19),_AlPptpStatsPayloadSendOctets_Type())
alPptpStatsPayloadSendOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsPayloadSendOctets.setStatus(_A)
_AlPptpStatsPayloadSendPackets_Type=Counter32
_AlPptpStatsPayloadSendPackets_Object=MibScalar
alPptpStatsPayloadSendPackets=_AlPptpStatsPayloadSendPackets_Object((1,3,6,1,4,1,3076,2,1,2,3,1,20),_AlPptpStatsPayloadSendPackets_Type())
alPptpStatsPayloadSendPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsPayloadSendPackets.setStatus(_A)
_AlPptpStatsTunnelTable_Object=MibTable
alPptpStatsTunnelTable=_AlPptpStatsTunnelTable_Object((1,3,6,1,4,1,3076,2,1,2,3,2))
if mibBuilder.loadTexts:alPptpStatsTunnelTable.setStatus(_A)
_AlPptpStatsTunnelEntry_Object=MibTableRow
alPptpStatsTunnelEntry=_AlPptpStatsTunnelEntry_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1))
alPptpStatsTunnelEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:alPptpStatsTunnelEntry.setStatus(_A)
_AlPptpStatsTunnelRowStatus_Type=RowStatus
_AlPptpStatsTunnelRowStatus_Object=MibTableColumn
alPptpStatsTunnelRowStatus=_AlPptpStatsTunnelRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,1),_AlPptpStatsTunnelRowStatus_Type())
alPptpStatsTunnelRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:alPptpStatsTunnelRowStatus.setStatus(_A)
_AlPptpStatsTunnelPeerIpAddr_Type=IpAddress
_AlPptpStatsTunnelPeerIpAddr_Object=MibTableColumn
alPptpStatsTunnelPeerIpAddr=_AlPptpStatsTunnelPeerIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,2),_AlPptpStatsTunnelPeerIpAddr_Type())
alPptpStatsTunnelPeerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelPeerIpAddr.setStatus(_A)
_AlPptpStatsTunnelDatastreamId_Type=Integer32
_AlPptpStatsTunnelDatastreamId_Object=MibTableColumn
alPptpStatsTunnelDatastreamId=_AlPptpStatsTunnelDatastreamId_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,3),_AlPptpStatsTunnelDatastreamId_Type())
alPptpStatsTunnelDatastreamId.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelDatastreamId.setStatus(_A)
_AlPptpStatsTunnelLocalIpAddr_Type=IpAddress
_AlPptpStatsTunnelLocalIpAddr_Object=MibTableColumn
alPptpStatsTunnelLocalIpAddr=_AlPptpStatsTunnelLocalIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,4),_AlPptpStatsTunnelLocalIpAddr_Type())
alPptpStatsTunnelLocalIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelLocalIpAddr.setStatus(_A)
_AlPptpStatsTunnelPeerHostName_Type=DisplayString
_AlPptpStatsTunnelPeerHostName_Object=MibTableColumn
alPptpStatsTunnelPeerHostName=_AlPptpStatsTunnelPeerHostName_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,5),_AlPptpStatsTunnelPeerHostName_Type())
alPptpStatsTunnelPeerHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelPeerHostName.setStatus(_A)
_AlPptpStatsTunnelPeerVendorName_Type=DisplayString
_AlPptpStatsTunnelPeerVendorName_Object=MibTableColumn
alPptpStatsTunnelPeerVendorName=_AlPptpStatsTunnelPeerVendorName_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,6),_AlPptpStatsTunnelPeerVendorName_Type())
alPptpStatsTunnelPeerVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelPeerVendorName.setStatus(_A)
class _AlPptpStatsTunnelPeerFirmwareRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AlPptpStatsTunnelPeerFirmwareRev_Type.__name__=_E
_AlPptpStatsTunnelPeerFirmwareRev_Object=MibTableColumn
alPptpStatsTunnelPeerFirmwareRev=_AlPptpStatsTunnelPeerFirmwareRev_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,7),_AlPptpStatsTunnelPeerFirmwareRev_Type())
alPptpStatsTunnelPeerFirmwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelPeerFirmwareRev.setStatus(_A)
class _AlPptpStatsTunnelPeerProtVers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AlPptpStatsTunnelPeerProtVers_Type.__name__=_E
_AlPptpStatsTunnelPeerProtVers_Object=MibTableColumn
alPptpStatsTunnelPeerProtVers=_AlPptpStatsTunnelPeerProtVers_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,8),_AlPptpStatsTunnelPeerProtVers_Type())
alPptpStatsTunnelPeerProtVers.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelPeerProtVers.setStatus(_A)
class _AlPptpStatsTunnelPeerFramingCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AlPptpStatsTunnelPeerFramingCap_Type.__name__=_D
_AlPptpStatsTunnelPeerFramingCap_Object=MibTableColumn
alPptpStatsTunnelPeerFramingCap=_AlPptpStatsTunnelPeerFramingCap_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,9),_AlPptpStatsTunnelPeerFramingCap_Type())
alPptpStatsTunnelPeerFramingCap.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelPeerFramingCap.setStatus(_A)
class _AlPptpStatsTunnelPeerBearerCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AlPptpStatsTunnelPeerBearerCap_Type.__name__=_D
_AlPptpStatsTunnelPeerBearerCap_Object=MibTableColumn
alPptpStatsTunnelPeerBearerCap=_AlPptpStatsTunnelPeerBearerCap_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,10),_AlPptpStatsTunnelPeerBearerCap_Type())
alPptpStatsTunnelPeerBearerCap.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelPeerBearerCap.setStatus(_A)
_AlPptpStatsTunnelPeerMaxChan_Type=Integer32
_AlPptpStatsTunnelPeerMaxChan_Object=MibTableColumn
alPptpStatsTunnelPeerMaxChan=_AlPptpStatsTunnelPeerMaxChan_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,11),_AlPptpStatsTunnelPeerMaxChan_Type())
alPptpStatsTunnelPeerMaxChan.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelPeerMaxChan.setStatus(_A)
_AlPptpStatsTunnelActiveSessions_Type=Counter32
_AlPptpStatsTunnelActiveSessions_Object=MibTableColumn
alPptpStatsTunnelActiveSessions=_AlPptpStatsTunnelActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,3,2,1,12),_AlPptpStatsTunnelActiveSessions_Type())
alPptpStatsTunnelActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsTunnelActiveSessions.setStatus(_A)
_AlPptpStatsSessionTable_Object=MibTable
alPptpStatsSessionTable=_AlPptpStatsSessionTable_Object((1,3,6,1,4,1,3076,2,1,2,3,3))
if mibBuilder.loadTexts:alPptpStatsSessionTable.setStatus(_A)
_AlPptpStatsSessionEntry_Object=MibTableRow
alPptpStatsSessionEntry=_AlPptpStatsSessionEntry_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1))
alPptpStatsSessionEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:alPptpStatsSessionEntry.setStatus(_A)
_AlPptpStatsSessionRowStatus_Type=RowStatus
_AlPptpStatsSessionRowStatus_Object=MibTableColumn
alPptpStatsSessionRowStatus=_AlPptpStatsSessionRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,1),_AlPptpStatsSessionRowStatus_Type())
alPptpStatsSessionRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:alPptpStatsSessionRowStatus.setStatus(_A)
_AlPptpStatsSessionDatastreamId_Type=Integer32
_AlPptpStatsSessionDatastreamId_Object=MibTableColumn
alPptpStatsSessionDatastreamId=_AlPptpStatsSessionDatastreamId_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,2),_AlPptpStatsSessionDatastreamId_Type())
alPptpStatsSessionDatastreamId.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionDatastreamId.setStatus(_A)
class _AlPptpStatsSessionLocalCallId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlPptpStatsSessionLocalCallId_Type.__name__=_D
_AlPptpStatsSessionLocalCallId_Object=MibTableColumn
alPptpStatsSessionLocalCallId=_AlPptpStatsSessionLocalCallId_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,3),_AlPptpStatsSessionLocalCallId_Type())
alPptpStatsSessionLocalCallId.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionLocalCallId.setStatus(_A)
class _AlPptpStatsSessionPeerCallId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlPptpStatsSessionPeerCallId_Type.__name__=_D
_AlPptpStatsSessionPeerCallId_Object=MibTableColumn
alPptpStatsSessionPeerCallId=_AlPptpStatsSessionPeerCallId_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,4),_AlPptpStatsSessionPeerCallId_Type())
alPptpStatsSessionPeerCallId.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionPeerCallId.setStatus(_A)
_AlPptpStatsSessionUserName_Type=DisplayString
_AlPptpStatsSessionUserName_Object=MibTableColumn
alPptpStatsSessionUserName=_AlPptpStatsSessionUserName_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,5),_AlPptpStatsSessionUserName_Type())
alPptpStatsSessionUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionUserName.setStatus(_A)
class _AlPptpStatsSessionSerial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlPptpStatsSessionSerial_Type.__name__=_D
_AlPptpStatsSessionSerial_Object=MibTableColumn
alPptpStatsSessionSerial=_AlPptpStatsSessionSerial_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,6),_AlPptpStatsSessionSerial_Type())
alPptpStatsSessionSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionSerial.setStatus(_A)
_AlPptpStatsSessionMinimumSpeed_Type=Integer32
_AlPptpStatsSessionMinimumSpeed_Object=MibTableColumn
alPptpStatsSessionMinimumSpeed=_AlPptpStatsSessionMinimumSpeed_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,7),_AlPptpStatsSessionMinimumSpeed_Type())
alPptpStatsSessionMinimumSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionMinimumSpeed.setStatus(_A)
_AlPptpStatsSessionMaximumSpeed_Type=Integer32
_AlPptpStatsSessionMaximumSpeed_Object=MibTableColumn
alPptpStatsSessionMaximumSpeed=_AlPptpStatsSessionMaximumSpeed_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,8),_AlPptpStatsSessionMaximumSpeed_Type())
alPptpStatsSessionMaximumSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionMaximumSpeed.setStatus(_A)
_AlPptpStatsSessionConnectSpeed_Type=Integer32
_AlPptpStatsSessionConnectSpeed_Object=MibTableColumn
alPptpStatsSessionConnectSpeed=_AlPptpStatsSessionConnectSpeed_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,9),_AlPptpStatsSessionConnectSpeed_Type())
alPptpStatsSessionConnectSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionConnectSpeed.setStatus(_A)
class _AlPptpStatsSessionBearerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('analog',1),('digital',2),('any',3)))
_AlPptpStatsSessionBearerType_Type.__name__=_D
_AlPptpStatsSessionBearerType_Object=MibTableColumn
alPptpStatsSessionBearerType=_AlPptpStatsSessionBearerType_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,10),_AlPptpStatsSessionBearerType_Type())
alPptpStatsSessionBearerType.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionBearerType.setStatus(_A)
class _AlPptpStatsSessionFramingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('asynchronous',1),('synchronous',2),('either',3)))
_AlPptpStatsSessionFramingType_Type.__name__=_D
_AlPptpStatsSessionFramingType_Object=MibTableColumn
alPptpStatsSessionFramingType=_AlPptpStatsSessionFramingType_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,11),_AlPptpStatsSessionFramingType_Type())
alPptpStatsSessionFramingType.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionFramingType.setStatus(_A)
_AlPptpStatsSessionPhysicalChannel_Type=Integer32
_AlPptpStatsSessionPhysicalChannel_Object=MibTableColumn
alPptpStatsSessionPhysicalChannel=_AlPptpStatsSessionPhysicalChannel_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,12),_AlPptpStatsSessionPhysicalChannel_Type())
alPptpStatsSessionPhysicalChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionPhysicalChannel.setStatus(_A)
_AlPptpStatsSessionLocalWindowSize_Type=Integer32
_AlPptpStatsSessionLocalWindowSize_Object=MibTableColumn
alPptpStatsSessionLocalWindowSize=_AlPptpStatsSessionLocalWindowSize_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,13),_AlPptpStatsSessionLocalWindowSize_Type())
alPptpStatsSessionLocalWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionLocalWindowSize.setStatus(_A)
_AlPptpStatsSessionPeerWindowSize_Type=Integer32
_AlPptpStatsSessionPeerWindowSize_Object=MibTableColumn
alPptpStatsSessionPeerWindowSize=_AlPptpStatsSessionPeerWindowSize_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,14),_AlPptpStatsSessionPeerWindowSize_Type())
alPptpStatsSessionPeerWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionPeerWindowSize.setStatus(_A)
_AlPptpStatsSessionLocalPpd_Type=Integer32
_AlPptpStatsSessionLocalPpd_Object=MibTableColumn
alPptpStatsSessionLocalPpd=_AlPptpStatsSessionLocalPpd_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,15),_AlPptpStatsSessionLocalPpd_Type())
alPptpStatsSessionLocalPpd.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionLocalPpd.setStatus(_A)
_AlPptpStatsSessionPeerPpd_Type=Integer32
_AlPptpStatsSessionPeerPpd_Object=MibTableColumn
alPptpStatsSessionPeerPpd=_AlPptpStatsSessionPeerPpd_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,16),_AlPptpStatsSessionPeerPpd_Type())
alPptpStatsSessionPeerPpd.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionPeerPpd.setStatus(_A)
_AlPptpStatsSessionRecvOctets_Type=Counter32
_AlPptpStatsSessionRecvOctets_Object=MibTableColumn
alPptpStatsSessionRecvOctets=_AlPptpStatsSessionRecvOctets_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,17),_AlPptpStatsSessionRecvOctets_Type())
alPptpStatsSessionRecvOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionRecvOctets.setStatus(_A)
_AlPptpStatsSessionRecvPackets_Type=Counter32
_AlPptpStatsSessionRecvPackets_Object=MibTableColumn
alPptpStatsSessionRecvPackets=_AlPptpStatsSessionRecvPackets_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,18),_AlPptpStatsSessionRecvPackets_Type())
alPptpStatsSessionRecvPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionRecvPackets.setStatus(_A)
_AlPptpStatsSessionRecvDiscards_Type=Counter32
_AlPptpStatsSessionRecvDiscards_Object=MibTableColumn
alPptpStatsSessionRecvDiscards=_AlPptpStatsSessionRecvDiscards_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,19),_AlPptpStatsSessionRecvDiscards_Type())
alPptpStatsSessionRecvDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionRecvDiscards.setStatus(_A)
_AlPptpStatsSessionRecvZLB_Type=Counter32
_AlPptpStatsSessionRecvZLB_Object=MibTableColumn
alPptpStatsSessionRecvZLB=_AlPptpStatsSessionRecvZLB_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,20),_AlPptpStatsSessionRecvZLB_Type())
alPptpStatsSessionRecvZLB.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionRecvZLB.setStatus(_A)
_AlPptpStatsSessionSendOctets_Type=Counter32
_AlPptpStatsSessionSendOctets_Object=MibTableColumn
alPptpStatsSessionSendOctets=_AlPptpStatsSessionSendOctets_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,21),_AlPptpStatsSessionSendOctets_Type())
alPptpStatsSessionSendOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionSendOctets.setStatus(_A)
_AlPptpStatsSessionSendPackets_Type=Counter32
_AlPptpStatsSessionSendPackets_Object=MibTableColumn
alPptpStatsSessionSendPackets=_AlPptpStatsSessionSendPackets_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,22),_AlPptpStatsSessionSendPackets_Type())
alPptpStatsSessionSendPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionSendPackets.setStatus(_A)
_AlPptpStatsSessionSendZLB_Type=Counter32
_AlPptpStatsSessionSendZLB_Object=MibTableColumn
alPptpStatsSessionSendZLB=_AlPptpStatsSessionSendZLB_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,23),_AlPptpStatsSessionSendZLB_Type())
alPptpStatsSessionSendZLB.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionSendZLB.setStatus(_A)
_AlPptpStatsSessionAckTimeouts_Type=Counter32
_AlPptpStatsSessionAckTimeouts_Object=MibTableColumn
alPptpStatsSessionAckTimeouts=_AlPptpStatsSessionAckTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,24),_AlPptpStatsSessionAckTimeouts_Type())
alPptpStatsSessionAckTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionAckTimeouts.setStatus(_A)
_AlPptpStatsSessionLocalFlowOff_Type=TruthValue
_AlPptpStatsSessionLocalFlowOff_Object=MibTableColumn
alPptpStatsSessionLocalFlowOff=_AlPptpStatsSessionLocalFlowOff_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,25),_AlPptpStatsSessionLocalFlowOff_Type())
alPptpStatsSessionLocalFlowOff.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionLocalFlowOff.setStatus(_A)
_AlPptpStatsSessionPeerFlowOff_Type=TruthValue
_AlPptpStatsSessionPeerFlowOff_Object=MibTableColumn
alPptpStatsSessionPeerFlowOff=_AlPptpStatsSessionPeerFlowOff_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,26),_AlPptpStatsSessionPeerFlowOff_Type())
alPptpStatsSessionPeerFlowOff.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionPeerFlowOff.setStatus(_A)
_AlPptpStatsSessionOutOfWindow_Type=Counter32
_AlPptpStatsSessionOutOfWindow_Object=MibTableColumn
alPptpStatsSessionOutOfWindow=_AlPptpStatsSessionOutOfWindow_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,27),_AlPptpStatsSessionOutOfWindow_Type())
alPptpStatsSessionOutOfWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionOutOfWindow.setStatus(_A)
_AlPptpStatsSessionOutOfSequence_Type=Counter32
_AlPptpStatsSessionOutOfSequence_Object=MibTableColumn
alPptpStatsSessionOutOfSequence=_AlPptpStatsSessionOutOfSequence_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,28),_AlPptpStatsSessionOutOfSequence_Type())
alPptpStatsSessionOutOfSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionOutOfSequence.setStatus(_A)
_AlPptpStatsSessionTunnelPeerIpAddr_Type=IpAddress
_AlPptpStatsSessionTunnelPeerIpAddr_Object=MibTableColumn
alPptpStatsSessionTunnelPeerIpAddr=_AlPptpStatsSessionTunnelPeerIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,3,3,1,29),_AlPptpStatsSessionTunnelPeerIpAddr_Type())
alPptpStatsSessionTunnelPeerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alPptpStatsSessionTunnelPeerIpAddr.setStatus(_A)
altigaPptpStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,3,2))
altigaPptpStatsGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_F),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_G),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:altigaPptpStatsGroup.setStatus(_A)
altigaPptpStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,10,2,1,1,1))
altigaPptpStatsMibCompliance.setObjects((_B,_AF))
if mibBuilder.loadTexts:altigaPptpStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaPptpStatsMibModule':altigaPptpStatsMibModule,'altigaPptpStatsMibConformance':altigaPptpStatsMibConformance,'altigaPptpStatsMibCompliances':altigaPptpStatsMibCompliances,'altigaPptpStatsMibCompliance':altigaPptpStatsMibCompliance,_AF:altigaPptpStatsGroup,'alStatsPptpGlobal':alStatsPptpGlobal,_I:alPptpStatsLocalProtVers,_J:alPptpStatsLocalFraming,_K:alPptpStatsLocalBearer,_L:alPptpStatsLocalFirmwareRev,_M:alPptpStatsTotalTunnels,_N:alPptpStatsActiveTunnels,_O:alPptpStatsMaxTunnels,_P:alPptpStatsTotalSessions,_Q:alPptpStatsActiveSessions,_R:alPptpStatsMaxSessions,_S:alPptpStatsControlRecvOctets,_T:alPptpStatsControlRecvPackets,_U:alPptpStatsControlRecvDiscards,_V:alPptpStatsControlSendOctets,_W:alPptpStatsControlSendPackets,_X:alPptpStatsPayloadRecvOctets,_Y:alPptpStatsPayloadRecvPackets,_Z:alPptpStatsPayloadRecvDiscards,_a:alPptpStatsPayloadSendOctets,_b:alPptpStatsPayloadSendPackets,'alPptpStatsTunnelTable':alPptpStatsTunnelTable,'alPptpStatsTunnelEntry':alPptpStatsTunnelEntry,_c:alPptpStatsTunnelRowStatus,_F:alPptpStatsTunnelPeerIpAddr,_d:alPptpStatsTunnelDatastreamId,_e:alPptpStatsTunnelLocalIpAddr,_f:alPptpStatsTunnelPeerHostName,_g:alPptpStatsTunnelPeerVendorName,_h:alPptpStatsTunnelPeerFirmwareRev,_i:alPptpStatsTunnelPeerProtVers,_j:alPptpStatsTunnelPeerFramingCap,_k:alPptpStatsTunnelPeerBearerCap,_l:alPptpStatsTunnelPeerMaxChan,_m:alPptpStatsTunnelActiveSessions,'alPptpStatsSessionTable':alPptpStatsSessionTable,'alPptpStatsSessionEntry':alPptpStatsSessionEntry,_n:alPptpStatsSessionRowStatus,_G:alPptpStatsSessionDatastreamId,_o:alPptpStatsSessionLocalCallId,_p:alPptpStatsSessionPeerCallId,_q:alPptpStatsSessionUserName,_r:alPptpStatsSessionSerial,_s:alPptpStatsSessionMinimumSpeed,_t:alPptpStatsSessionMaximumSpeed,_u:alPptpStatsSessionConnectSpeed,_v:alPptpStatsSessionBearerType,_w:alPptpStatsSessionFramingType,_x:alPptpStatsSessionPhysicalChannel,_y:alPptpStatsSessionLocalWindowSize,_z:alPptpStatsSessionPeerWindowSize,_A0:alPptpStatsSessionLocalPpd,_A1:alPptpStatsSessionPeerPpd,_A2:alPptpStatsSessionRecvOctets,_A3:alPptpStatsSessionRecvPackets,_A4:alPptpStatsSessionRecvDiscards,_A5:alPptpStatsSessionRecvZLB,_A6:alPptpStatsSessionSendOctets,_A7:alPptpStatsSessionSendPackets,_A8:alPptpStatsSessionSendZLB,_A9:alPptpStatsSessionAckTimeouts,_AA:alPptpStatsSessionLocalFlowOff,_AB:alPptpStatsSessionPeerFlowOff,_AC:alPptpStatsSessionOutOfWindow,_AD:alPptpStatsSessionOutOfSequence,_AE:alPptpStatsSessionTunnelPeerIpAddr})