_AM='adGenAOSMediaGatewayRtpChannelTotalsGroup'
_AL='adGenAOSMediaGatewayInfoGroup'
_AK='adGenAOSMediaGatewayRtpSessionTotalsGroup'
_AJ='adGenAOSMediaGatewayRtpSessionGroup'
_AI='adGenAOSRtpChannelTimeSinceLastClearCounters'
_AH='adGenAOSRtpChannelClearCounters'
_AG='adGenAOSRtpChannelTotalRxFrameOutOfOrders'
_AF='adGenAOSRtpChannelTotalRxFrameOverflows'
_AE='adGenAOSRtpChannelTotalRxFrameLateDiscards'
_AD='adGenAOSRtpChannelTotalRxMaxDepth'
_AC='adGenAOSRtpChannelTotalTxOctets'
_AB='adGenAOSRtpChannelTotalTxPackets'
_AA='adGenAOSRtpChannelTotalRxPacketsUnknown'
_A9='adGenAOSRtpChannelTotalRxPacketsLost'
_A8='adGenAOSRtpChannelTotalRxOctets'
_A7='adGenAOSRtpChannelTotalRxPackets'
_A6='adGenAOSRtpChannelTotalSessionDuration'
_A5='adGenAOSRtpChannelTotalSessions'
_A4='adGenAOSRtpChannelTotalIdName'
_A3='adGenAOSMediaGatewayInfoUptime'
_A2='adGenAOSMediaGatewayInfoFreePacketBuffers'
_A1='adGenAOSMediaGatewayInfoUtilizationMaximum'
_A0='adGenAOSMediaGatewayInfoUtilization'
_z='adGenAOSMediaGatewayInfoSoftwareVersion'
_y='adGenAOSRtpSessionTotalsTimeSinceLastClearCounters'
_x='adGenAOSRtpSessionTotalsClearCounters'
_w='adGenAOSRtpSessionTotalsRxFrameOutOfOrders'
_v='adGenAOSRtpSessionTotalsRxFrameOverflows'
_u='adGenAOSRtpSessionTotalsRxFrameLateDiscards'
_t='adGenAOSRtpSessionTotalsTxOctets'
_s='adGenAOSRtpSessionTotalsTxPackets'
_r='adGenAOSRtpSessionTotalsRxPacketsUnknown'
_q='adGenAOSRtpSessionTotalsRxPacketsLost'
_p='adGenAOSRtpSessionTotalsRxOctets'
_o='adGenAOSRtpSessionTotalsRxPackets'
_n='adGenAOSRtpSessionTotalsSessionDuration'
_m='adGenAOSRtpSessionTxSyncSource'
_l='adGenAOSRtpSessionTxOctets'
_k='adGenAOSRtpSessionTxPackets'
_j='adGenAOSRtpSessionRxSyncSource'
_i='adGenAOSRtpSessionRxFrameOutOfOrders'
_h='adGenAOSRtpSessionRxFrameOverflows'
_g='adGenAOSRtpSessionRxFrameLateDiscards'
_f='adGenAOSRtpSessionRxMaxJitterBufferDepth'
_e='adGenAOSRtpSessionRxJitterBufferDepth'
_d='adGenAOSRtpSessionRxPacketsUnknown'
_c='adGenAOSRtpSessionRxPacketsLost'
_b='adGenAOSRtpSessionRxOctets'
_a='adGenAOSRtpSessionRxPackets'
_Z='adGenAOSRtpSessionEchoCancellerEnabled'
_Y='adGenAOSRtpSessionTxFramesPerPacket'
_X='adGenAOSRtpSessionRemoteUdpPort'
_W='adGenAOSRtpSessionRemoteIPAddress'
_V='adGenAOSRtpSessionSIPPortDescription'
_U='adGenAOSRtpSessionLocalUdpPort'
_T='adGenAOSRtpSessionLocalIPAddress'
_S='adGenAOSRtpSessionTdmPortDescription'
_R='adGenAOSRtpSessionVAD'
_Q='adGenAOSRtpSessionVocoder'
_P='adGenAOSRtpSessionDuration'
_O='adGenAOSRtpSessionStartTime'
_N='adGenAOSRtpSessionStatus'
_M='adGenAOSRtpSessionChannelIdName'
_L='read-write'
_K='enabled'
_J='disabled'
_I='adGenAOSRtpChannelTotalId'
_H='adGenAOSMediaGatewayInfoIdentifier'
_G='adGenAOSRtpSessionTotalsSessions'
_F='adGenAOSRtpSessionChannelId'
_E='Integer32'
_D='obsolete'
_C='read-only'
_B='current'
_A='ADTRAN-AOS-MEDIAGATEWAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSVoice,=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSVoice')
adIdentity,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adShared')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAOSMediaGatewayMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,5,2))
if mibBuilder.loadTexts:adGenAOSMediaGatewayMIB.setRevisions(('2012-08-22 00:00',))
_AdGenAOSMediaGateway_ObjectIdentity=ObjectIdentity
adGenAOSMediaGateway=_AdGenAOSMediaGateway_ObjectIdentity((1,3,6,1,4,1,664,5,53,5,2))
_AdGenAOSMediaGatewayObjects_ObjectIdentity=ObjectIdentity
adGenAOSMediaGatewayObjects=_AdGenAOSMediaGatewayObjects_ObjectIdentity((1,3,6,1,4,1,664,5,53,5,2,1))
_AdGenAOSRtpSessionTable_Object=MibTable
adGenAOSRtpSessionTable=_AdGenAOSRtpSessionTable_Object((1,3,6,1,4,1,664,5,53,5,2,1,1))
if mibBuilder.loadTexts:adGenAOSRtpSessionTable.setStatus(_B)
_AdGenAOSRtpSessionEntry_Object=MibTableRow
adGenAOSRtpSessionEntry=_AdGenAOSRtpSessionEntry_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1))
adGenAOSRtpSessionEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:adGenAOSRtpSessionEntry.setStatus(_B)
_AdGenAOSRtpSessionChannelId_Type=Integer32
_AdGenAOSRtpSessionChannelId_Object=MibTableColumn
adGenAOSRtpSessionChannelId=_AdGenAOSRtpSessionChannelId_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,1),_AdGenAOSRtpSessionChannelId_Type())
adGenAOSRtpSessionChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionChannelId.setStatus(_B)
_AdGenAOSRtpSessionChannelIdName_Type=DisplayString
_AdGenAOSRtpSessionChannelIdName_Object=MibTableColumn
adGenAOSRtpSessionChannelIdName=_AdGenAOSRtpSessionChannelIdName_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,2),_AdGenAOSRtpSessionChannelIdName_Type())
adGenAOSRtpSessionChannelIdName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionChannelIdName.setStatus(_B)
class _AdGenAOSRtpSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unavailable',0),('available',1),('reserved',2),('allocated',3),('active',4),('interrupted',5)))
_AdGenAOSRtpSessionStatus_Type.__name__=_E
_AdGenAOSRtpSessionStatus_Object=MibTableColumn
adGenAOSRtpSessionStatus=_AdGenAOSRtpSessionStatus_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,3),_AdGenAOSRtpSessionStatus_Type())
adGenAOSRtpSessionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionStatus.setStatus(_B)
_AdGenAOSRtpSessionStartTime_Type=DisplayString
_AdGenAOSRtpSessionStartTime_Object=MibTableColumn
adGenAOSRtpSessionStartTime=_AdGenAOSRtpSessionStartTime_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,4),_AdGenAOSRtpSessionStartTime_Type())
adGenAOSRtpSessionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionStartTime.setStatus(_B)
_AdGenAOSRtpSessionDuration_Type=DisplayString
_AdGenAOSRtpSessionDuration_Object=MibTableColumn
adGenAOSRtpSessionDuration=_AdGenAOSRtpSessionDuration_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,5),_AdGenAOSRtpSessionDuration_Type())
adGenAOSRtpSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionDuration.setStatus(_B)
class _AdGenAOSRtpSessionVocoder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39)));namedValues=NamedValues(*(('none',0),('g711ulaw',1),('gsm',2),('g723',3),('g711alaw',4),('g722',5),('g728',6),('g729a',7),('dynamic96',8),('dynamic97',9),('dynamic98',10),('dynamic99',11),('dynamic100',12),('dynamic101',13),('dynamic102',14),('dynamic103',15),('dynamic104',16),('dynamic105',17),('dynamic106',18),('dynamic107',19),('dynamic108',20),('dynamic109',21),('dynamic110',22),('dynamic111',23),('dynamic112',24),('dynamic113',25),('dynamic114',26),('dynamic115',27),('dynamic116',28),('dynamic117',29),('dynamic118',30),('dynamic119',31),('dynamic120',32),('dynamic121',33),('dynamic122',34),('dynamic123',35),('dynamic124',36),('dynamic125',37),('dynamic126',38),('dynamic127',39)))
_AdGenAOSRtpSessionVocoder_Type.__name__=_E
_AdGenAOSRtpSessionVocoder_Object=MibTableColumn
adGenAOSRtpSessionVocoder=_AdGenAOSRtpSessionVocoder_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,6),_AdGenAOSRtpSessionVocoder_Type())
adGenAOSRtpSessionVocoder.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionVocoder.setStatus(_B)
class _AdGenAOSRtpSessionVAD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_AdGenAOSRtpSessionVAD_Type.__name__=_E
_AdGenAOSRtpSessionVAD_Object=MibTableColumn
adGenAOSRtpSessionVAD=_AdGenAOSRtpSessionVAD_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,7),_AdGenAOSRtpSessionVAD_Type())
adGenAOSRtpSessionVAD.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionVAD.setStatus(_B)
_AdGenAOSRtpSessionTdmPortDescription_Type=DisplayString
_AdGenAOSRtpSessionTdmPortDescription_Object=MibTableColumn
adGenAOSRtpSessionTdmPortDescription=_AdGenAOSRtpSessionTdmPortDescription_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,8),_AdGenAOSRtpSessionTdmPortDescription_Type())
adGenAOSRtpSessionTdmPortDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTdmPortDescription.setStatus(_B)
_AdGenAOSRtpSessionLocalIPAddress_Type=IpAddress
_AdGenAOSRtpSessionLocalIPAddress_Object=MibTableColumn
adGenAOSRtpSessionLocalIPAddress=_AdGenAOSRtpSessionLocalIPAddress_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,9),_AdGenAOSRtpSessionLocalIPAddress_Type())
adGenAOSRtpSessionLocalIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionLocalIPAddress.setStatus(_B)
_AdGenAOSRtpSessionLocalUdpPort_Type=Integer32
_AdGenAOSRtpSessionLocalUdpPort_Object=MibTableColumn
adGenAOSRtpSessionLocalUdpPort=_AdGenAOSRtpSessionLocalUdpPort_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,10),_AdGenAOSRtpSessionLocalUdpPort_Type())
adGenAOSRtpSessionLocalUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionLocalUdpPort.setStatus(_B)
_AdGenAOSRtpSessionSIPPortDescription_Type=DisplayString
_AdGenAOSRtpSessionSIPPortDescription_Object=MibTableColumn
adGenAOSRtpSessionSIPPortDescription=_AdGenAOSRtpSessionSIPPortDescription_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,11),_AdGenAOSRtpSessionSIPPortDescription_Type())
adGenAOSRtpSessionSIPPortDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionSIPPortDescription.setStatus(_B)
_AdGenAOSRtpSessionRemoteIPAddress_Type=IpAddress
_AdGenAOSRtpSessionRemoteIPAddress_Object=MibTableColumn
adGenAOSRtpSessionRemoteIPAddress=_AdGenAOSRtpSessionRemoteIPAddress_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,12),_AdGenAOSRtpSessionRemoteIPAddress_Type())
adGenAOSRtpSessionRemoteIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRemoteIPAddress.setStatus(_B)
_AdGenAOSRtpSessionRemoteUdpPort_Type=Integer32
_AdGenAOSRtpSessionRemoteUdpPort_Object=MibTableColumn
adGenAOSRtpSessionRemoteUdpPort=_AdGenAOSRtpSessionRemoteUdpPort_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,13),_AdGenAOSRtpSessionRemoteUdpPort_Type())
adGenAOSRtpSessionRemoteUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRemoteUdpPort.setStatus(_B)
_AdGenAOSRtpSessionTxFramesPerPacket_Type=Integer32
_AdGenAOSRtpSessionTxFramesPerPacket_Object=MibTableColumn
adGenAOSRtpSessionTxFramesPerPacket=_AdGenAOSRtpSessionTxFramesPerPacket_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,14),_AdGenAOSRtpSessionTxFramesPerPacket_Type())
adGenAOSRtpSessionTxFramesPerPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTxFramesPerPacket.setStatus(_B)
class _AdGenAOSRtpSessionEchoCancellerEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_AdGenAOSRtpSessionEchoCancellerEnabled_Type.__name__=_E
_AdGenAOSRtpSessionEchoCancellerEnabled_Object=MibTableColumn
adGenAOSRtpSessionEchoCancellerEnabled=_AdGenAOSRtpSessionEchoCancellerEnabled_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,15),_AdGenAOSRtpSessionEchoCancellerEnabled_Type())
adGenAOSRtpSessionEchoCancellerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionEchoCancellerEnabled.setStatus(_B)
_AdGenAOSRtpSessionRxPackets_Type=Integer32
_AdGenAOSRtpSessionRxPackets_Object=MibTableColumn
adGenAOSRtpSessionRxPackets=_AdGenAOSRtpSessionRxPackets_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,22),_AdGenAOSRtpSessionRxPackets_Type())
adGenAOSRtpSessionRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxPackets.setStatus(_B)
_AdGenAOSRtpSessionRxOctets_Type=Integer32
_AdGenAOSRtpSessionRxOctets_Object=MibTableColumn
adGenAOSRtpSessionRxOctets=_AdGenAOSRtpSessionRxOctets_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,23),_AdGenAOSRtpSessionRxOctets_Type())
adGenAOSRtpSessionRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxOctets.setStatus(_B)
_AdGenAOSRtpSessionRxPacketsLost_Type=Integer32
_AdGenAOSRtpSessionRxPacketsLost_Object=MibTableColumn
adGenAOSRtpSessionRxPacketsLost=_AdGenAOSRtpSessionRxPacketsLost_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,24),_AdGenAOSRtpSessionRxPacketsLost_Type())
adGenAOSRtpSessionRxPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxPacketsLost.setStatus(_D)
_AdGenAOSRtpSessionRxPacketsUnknown_Type=Integer32
_AdGenAOSRtpSessionRxPacketsUnknown_Object=MibTableColumn
adGenAOSRtpSessionRxPacketsUnknown=_AdGenAOSRtpSessionRxPacketsUnknown_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,25),_AdGenAOSRtpSessionRxPacketsUnknown_Type())
adGenAOSRtpSessionRxPacketsUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxPacketsUnknown.setStatus(_B)
_AdGenAOSRtpSessionRxJitterBufferDepth_Type=Integer32
_AdGenAOSRtpSessionRxJitterBufferDepth_Object=MibTableColumn
adGenAOSRtpSessionRxJitterBufferDepth=_AdGenAOSRtpSessionRxJitterBufferDepth_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,26),_AdGenAOSRtpSessionRxJitterBufferDepth_Type())
adGenAOSRtpSessionRxJitterBufferDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxJitterBufferDepth.setStatus(_B)
_AdGenAOSRtpSessionRxMaxJitterBufferDepth_Type=Integer32
_AdGenAOSRtpSessionRxMaxJitterBufferDepth_Object=MibTableColumn
adGenAOSRtpSessionRxMaxJitterBufferDepth=_AdGenAOSRtpSessionRxMaxJitterBufferDepth_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,27),_AdGenAOSRtpSessionRxMaxJitterBufferDepth_Type())
adGenAOSRtpSessionRxMaxJitterBufferDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxMaxJitterBufferDepth.setStatus(_B)
_AdGenAOSRtpSessionRxFrameLateDiscards_Type=Integer32
_AdGenAOSRtpSessionRxFrameLateDiscards_Object=MibTableColumn
adGenAOSRtpSessionRxFrameLateDiscards=_AdGenAOSRtpSessionRxFrameLateDiscards_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,30),_AdGenAOSRtpSessionRxFrameLateDiscards_Type())
adGenAOSRtpSessionRxFrameLateDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxFrameLateDiscards.setStatus(_D)
_AdGenAOSRtpSessionRxFrameOverflows_Type=Integer32
_AdGenAOSRtpSessionRxFrameOverflows_Object=MibTableColumn
adGenAOSRtpSessionRxFrameOverflows=_AdGenAOSRtpSessionRxFrameOverflows_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,31),_AdGenAOSRtpSessionRxFrameOverflows_Type())
adGenAOSRtpSessionRxFrameOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxFrameOverflows.setStatus(_D)
_AdGenAOSRtpSessionRxFrameOutOfOrders_Type=Integer32
_AdGenAOSRtpSessionRxFrameOutOfOrders_Object=MibTableColumn
adGenAOSRtpSessionRxFrameOutOfOrders=_AdGenAOSRtpSessionRxFrameOutOfOrders_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,33),_AdGenAOSRtpSessionRxFrameOutOfOrders_Type())
adGenAOSRtpSessionRxFrameOutOfOrders.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxFrameOutOfOrders.setStatus(_B)
_AdGenAOSRtpSessionRxSyncSource_Type=Integer32
_AdGenAOSRtpSessionRxSyncSource_Object=MibTableColumn
adGenAOSRtpSessionRxSyncSource=_AdGenAOSRtpSessionRxSyncSource_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,34),_AdGenAOSRtpSessionRxSyncSource_Type())
adGenAOSRtpSessionRxSyncSource.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionRxSyncSource.setStatus(_B)
_AdGenAOSRtpSessionTxPackets_Type=Integer32
_AdGenAOSRtpSessionTxPackets_Object=MibTableColumn
adGenAOSRtpSessionTxPackets=_AdGenAOSRtpSessionTxPackets_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,35),_AdGenAOSRtpSessionTxPackets_Type())
adGenAOSRtpSessionTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTxPackets.setStatus(_B)
_AdGenAOSRtpSessionTxOctets_Type=Integer32
_AdGenAOSRtpSessionTxOctets_Object=MibTableColumn
adGenAOSRtpSessionTxOctets=_AdGenAOSRtpSessionTxOctets_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,36),_AdGenAOSRtpSessionTxOctets_Type())
adGenAOSRtpSessionTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTxOctets.setStatus(_B)
_AdGenAOSRtpSessionTxSyncSource_Type=Integer32
_AdGenAOSRtpSessionTxSyncSource_Object=MibTableColumn
adGenAOSRtpSessionTxSyncSource=_AdGenAOSRtpSessionTxSyncSource_Object((1,3,6,1,4,1,664,5,53,5,2,1,1,1,37),_AdGenAOSRtpSessionTxSyncSource_Type())
adGenAOSRtpSessionTxSyncSource.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTxSyncSource.setStatus(_B)
_AdGenAOSRtpSessionTotalsTable_Object=MibTable
adGenAOSRtpSessionTotalsTable=_AdGenAOSRtpSessionTotalsTable_Object((1,3,6,1,4,1,664,5,53,5,2,1,2))
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsTable.setStatus(_B)
_AdGenAOSRtpSessionTotalsEntry_Object=MibTableRow
adGenAOSRtpSessionTotalsEntry=_AdGenAOSRtpSessionTotalsEntry_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1))
adGenAOSRtpSessionTotalsEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsEntry.setStatus(_B)
_AdGenAOSRtpSessionTotalsSessions_Type=Integer32
_AdGenAOSRtpSessionTotalsSessions_Object=MibTableColumn
adGenAOSRtpSessionTotalsSessions=_AdGenAOSRtpSessionTotalsSessions_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,1),_AdGenAOSRtpSessionTotalsSessions_Type())
adGenAOSRtpSessionTotalsSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsSessions.setStatus(_B)
_AdGenAOSRtpSessionTotalsSessionDuration_Type=DisplayString
_AdGenAOSRtpSessionTotalsSessionDuration_Object=MibTableColumn
adGenAOSRtpSessionTotalsSessionDuration=_AdGenAOSRtpSessionTotalsSessionDuration_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,2),_AdGenAOSRtpSessionTotalsSessionDuration_Type())
adGenAOSRtpSessionTotalsSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsSessionDuration.setStatus(_B)
_AdGenAOSRtpSessionTotalsRxPackets_Type=Integer32
_AdGenAOSRtpSessionTotalsRxPackets_Object=MibTableColumn
adGenAOSRtpSessionTotalsRxPackets=_AdGenAOSRtpSessionTotalsRxPackets_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,3),_AdGenAOSRtpSessionTotalsRxPackets_Type())
adGenAOSRtpSessionTotalsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsRxPackets.setStatus(_B)
_AdGenAOSRtpSessionTotalsRxOctets_Type=Integer32
_AdGenAOSRtpSessionTotalsRxOctets_Object=MibTableColumn
adGenAOSRtpSessionTotalsRxOctets=_AdGenAOSRtpSessionTotalsRxOctets_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,4),_AdGenAOSRtpSessionTotalsRxOctets_Type())
adGenAOSRtpSessionTotalsRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsRxOctets.setStatus(_B)
_AdGenAOSRtpSessionTotalsRxPacketsLost_Type=Integer32
_AdGenAOSRtpSessionTotalsRxPacketsLost_Object=MibTableColumn
adGenAOSRtpSessionTotalsRxPacketsLost=_AdGenAOSRtpSessionTotalsRxPacketsLost_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,5),_AdGenAOSRtpSessionTotalsRxPacketsLost_Type())
adGenAOSRtpSessionTotalsRxPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsRxPacketsLost.setStatus(_D)
_AdGenAOSRtpSessionTotalsRxPacketsUnknown_Type=Integer32
_AdGenAOSRtpSessionTotalsRxPacketsUnknown_Object=MibTableColumn
adGenAOSRtpSessionTotalsRxPacketsUnknown=_AdGenAOSRtpSessionTotalsRxPacketsUnknown_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,6),_AdGenAOSRtpSessionTotalsRxPacketsUnknown_Type())
adGenAOSRtpSessionTotalsRxPacketsUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsRxPacketsUnknown.setStatus(_B)
_AdGenAOSRtpSessionTotalsTxPackets_Type=Integer32
_AdGenAOSRtpSessionTotalsTxPackets_Object=MibTableColumn
adGenAOSRtpSessionTotalsTxPackets=_AdGenAOSRtpSessionTotalsTxPackets_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,7),_AdGenAOSRtpSessionTotalsTxPackets_Type())
adGenAOSRtpSessionTotalsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsTxPackets.setStatus(_B)
_AdGenAOSRtpSessionTotalsTxOctets_Type=Integer32
_AdGenAOSRtpSessionTotalsTxOctets_Object=MibTableColumn
adGenAOSRtpSessionTotalsTxOctets=_AdGenAOSRtpSessionTotalsTxOctets_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,8),_AdGenAOSRtpSessionTotalsTxOctets_Type())
adGenAOSRtpSessionTotalsTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsTxOctets.setStatus(_B)
_AdGenAOSRtpSessionTotalsRxFrameLateDiscards_Type=Integer32
_AdGenAOSRtpSessionTotalsRxFrameLateDiscards_Object=MibTableColumn
adGenAOSRtpSessionTotalsRxFrameLateDiscards=_AdGenAOSRtpSessionTotalsRxFrameLateDiscards_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,9),_AdGenAOSRtpSessionTotalsRxFrameLateDiscards_Type())
adGenAOSRtpSessionTotalsRxFrameLateDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsRxFrameLateDiscards.setStatus(_D)
_AdGenAOSRtpSessionTotalsRxFrameOverflows_Type=Integer32
_AdGenAOSRtpSessionTotalsRxFrameOverflows_Object=MibTableColumn
adGenAOSRtpSessionTotalsRxFrameOverflows=_AdGenAOSRtpSessionTotalsRxFrameOverflows_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,11),_AdGenAOSRtpSessionTotalsRxFrameOverflows_Type())
adGenAOSRtpSessionTotalsRxFrameOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsRxFrameOverflows.setStatus(_D)
_AdGenAOSRtpSessionTotalsRxFrameOutOfOrders_Type=Integer32
_AdGenAOSRtpSessionTotalsRxFrameOutOfOrders_Object=MibTableColumn
adGenAOSRtpSessionTotalsRxFrameOutOfOrders=_AdGenAOSRtpSessionTotalsRxFrameOutOfOrders_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,12),_AdGenAOSRtpSessionTotalsRxFrameOutOfOrders_Type())
adGenAOSRtpSessionTotalsRxFrameOutOfOrders.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsRxFrameOutOfOrders.setStatus(_B)
_AdGenAOSRtpSessionTotalsClearCounters_Type=Integer32
_AdGenAOSRtpSessionTotalsClearCounters_Object=MibTableColumn
adGenAOSRtpSessionTotalsClearCounters=_AdGenAOSRtpSessionTotalsClearCounters_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,13),_AdGenAOSRtpSessionTotalsClearCounters_Type())
adGenAOSRtpSessionTotalsClearCounters.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsClearCounters.setStatus(_B)
_AdGenAOSRtpSessionTotalsTimeSinceLastClearCounters_Type=DisplayString
_AdGenAOSRtpSessionTotalsTimeSinceLastClearCounters_Object=MibTableColumn
adGenAOSRtpSessionTotalsTimeSinceLastClearCounters=_AdGenAOSRtpSessionTotalsTimeSinceLastClearCounters_Object((1,3,6,1,4,1,664,5,53,5,2,1,2,1,14),_AdGenAOSRtpSessionTotalsTimeSinceLastClearCounters_Type())
adGenAOSRtpSessionTotalsTimeSinceLastClearCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpSessionTotalsTimeSinceLastClearCounters.setStatus(_B)
_AdGenAOSMediaGatewayInfoTable_Object=MibTable
adGenAOSMediaGatewayInfoTable=_AdGenAOSMediaGatewayInfoTable_Object((1,3,6,1,4,1,664,5,53,5,2,1,3))
if mibBuilder.loadTexts:adGenAOSMediaGatewayInfoTable.setStatus(_B)
_AdGenAOSMediaGatewayInfoEntry_Object=MibTableRow
adGenAOSMediaGatewayInfoEntry=_AdGenAOSMediaGatewayInfoEntry_Object((1,3,6,1,4,1,664,5,53,5,2,1,3,1))
adGenAOSMediaGatewayInfoEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:adGenAOSMediaGatewayInfoEntry.setStatus(_B)
_AdGenAOSMediaGatewayInfoIdentifier_Type=Integer32
_AdGenAOSMediaGatewayInfoIdentifier_Object=MibTableColumn
adGenAOSMediaGatewayInfoIdentifier=_AdGenAOSMediaGatewayInfoIdentifier_Object((1,3,6,1,4,1,664,5,53,5,2,1,3,1,1),_AdGenAOSMediaGatewayInfoIdentifier_Type())
adGenAOSMediaGatewayInfoIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSMediaGatewayInfoIdentifier.setStatus(_B)
_AdGenAOSMediaGatewayInfoSoftwareVersion_Type=DisplayString
_AdGenAOSMediaGatewayInfoSoftwareVersion_Object=MibTableColumn
adGenAOSMediaGatewayInfoSoftwareVersion=_AdGenAOSMediaGatewayInfoSoftwareVersion_Object((1,3,6,1,4,1,664,5,53,5,2,1,3,1,2),_AdGenAOSMediaGatewayInfoSoftwareVersion_Type())
adGenAOSMediaGatewayInfoSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSMediaGatewayInfoSoftwareVersion.setStatus(_B)
_AdGenAOSMediaGatewayInfoUtilization_Type=Integer32
_AdGenAOSMediaGatewayInfoUtilization_Object=MibTableColumn
adGenAOSMediaGatewayInfoUtilization=_AdGenAOSMediaGatewayInfoUtilization_Object((1,3,6,1,4,1,664,5,53,5,2,1,3,1,3),_AdGenAOSMediaGatewayInfoUtilization_Type())
adGenAOSMediaGatewayInfoUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSMediaGatewayInfoUtilization.setStatus(_B)
_AdGenAOSMediaGatewayInfoUtilizationMaximum_Type=Integer32
_AdGenAOSMediaGatewayInfoUtilizationMaximum_Object=MibTableColumn
adGenAOSMediaGatewayInfoUtilizationMaximum=_AdGenAOSMediaGatewayInfoUtilizationMaximum_Object((1,3,6,1,4,1,664,5,53,5,2,1,3,1,4),_AdGenAOSMediaGatewayInfoUtilizationMaximum_Type())
adGenAOSMediaGatewayInfoUtilizationMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSMediaGatewayInfoUtilizationMaximum.setStatus(_B)
_AdGenAOSMediaGatewayInfoFreePacketBuffers_Type=Integer32
_AdGenAOSMediaGatewayInfoFreePacketBuffers_Object=MibTableColumn
adGenAOSMediaGatewayInfoFreePacketBuffers=_AdGenAOSMediaGatewayInfoFreePacketBuffers_Object((1,3,6,1,4,1,664,5,53,5,2,1,3,1,5),_AdGenAOSMediaGatewayInfoFreePacketBuffers_Type())
adGenAOSMediaGatewayInfoFreePacketBuffers.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSMediaGatewayInfoFreePacketBuffers.setStatus(_B)
_AdGenAOSMediaGatewayInfoUptime_Type=DisplayString
_AdGenAOSMediaGatewayInfoUptime_Object=MibTableColumn
adGenAOSMediaGatewayInfoUptime=_AdGenAOSMediaGatewayInfoUptime_Object((1,3,6,1,4,1,664,5,53,5,2,1,3,1,6),_AdGenAOSMediaGatewayInfoUptime_Type())
adGenAOSMediaGatewayInfoUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSMediaGatewayInfoUptime.setStatus(_B)
_AdGenAOSRtpChannelTotalTable_Object=MibTable
adGenAOSRtpChannelTotalTable=_AdGenAOSRtpChannelTotalTable_Object((1,3,6,1,4,1,664,5,53,5,2,1,4))
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalTable.setStatus(_B)
_AdGenAOSRtpChannelTotalEntry_Object=MibTableRow
adGenAOSRtpChannelTotalEntry=_AdGenAOSRtpChannelTotalEntry_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1))
adGenAOSRtpChannelTotalEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalEntry.setStatus(_B)
_AdGenAOSRtpChannelTotalId_Type=Integer32
_AdGenAOSRtpChannelTotalId_Object=MibTableColumn
adGenAOSRtpChannelTotalId=_AdGenAOSRtpChannelTotalId_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,1),_AdGenAOSRtpChannelTotalId_Type())
adGenAOSRtpChannelTotalId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalId.setStatus(_B)
_AdGenAOSRtpChannelTotalIdName_Type=DisplayString
_AdGenAOSRtpChannelTotalIdName_Object=MibTableColumn
adGenAOSRtpChannelTotalIdName=_AdGenAOSRtpChannelTotalIdName_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,2),_AdGenAOSRtpChannelTotalIdName_Type())
adGenAOSRtpChannelTotalIdName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalIdName.setStatus(_B)
_AdGenAOSRtpChannelTotalSessions_Type=Integer32
_AdGenAOSRtpChannelTotalSessions_Object=MibTableColumn
adGenAOSRtpChannelTotalSessions=_AdGenAOSRtpChannelTotalSessions_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,3),_AdGenAOSRtpChannelTotalSessions_Type())
adGenAOSRtpChannelTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalSessions.setStatus(_B)
_AdGenAOSRtpChannelTotalSessionDuration_Type=DisplayString
_AdGenAOSRtpChannelTotalSessionDuration_Object=MibTableColumn
adGenAOSRtpChannelTotalSessionDuration=_AdGenAOSRtpChannelTotalSessionDuration_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,4),_AdGenAOSRtpChannelTotalSessionDuration_Type())
adGenAOSRtpChannelTotalSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalSessionDuration.setStatus(_B)
_AdGenAOSRtpChannelTotalRxPackets_Type=Integer32
_AdGenAOSRtpChannelTotalRxPackets_Object=MibTableColumn
adGenAOSRtpChannelTotalRxPackets=_AdGenAOSRtpChannelTotalRxPackets_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,5),_AdGenAOSRtpChannelTotalRxPackets_Type())
adGenAOSRtpChannelTotalRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalRxPackets.setStatus(_B)
_AdGenAOSRtpChannelTotalRxOctets_Type=Integer32
_AdGenAOSRtpChannelTotalRxOctets_Object=MibTableColumn
adGenAOSRtpChannelTotalRxOctets=_AdGenAOSRtpChannelTotalRxOctets_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,6),_AdGenAOSRtpChannelTotalRxOctets_Type())
adGenAOSRtpChannelTotalRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalRxOctets.setStatus(_B)
_AdGenAOSRtpChannelTotalRxPacketsLost_Type=Integer32
_AdGenAOSRtpChannelTotalRxPacketsLost_Object=MibTableColumn
adGenAOSRtpChannelTotalRxPacketsLost=_AdGenAOSRtpChannelTotalRxPacketsLost_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,7),_AdGenAOSRtpChannelTotalRxPacketsLost_Type())
adGenAOSRtpChannelTotalRxPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalRxPacketsLost.setStatus(_D)
_AdGenAOSRtpChannelTotalRxPacketsUnknown_Type=Integer32
_AdGenAOSRtpChannelTotalRxPacketsUnknown_Object=MibTableColumn
adGenAOSRtpChannelTotalRxPacketsUnknown=_AdGenAOSRtpChannelTotalRxPacketsUnknown_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,8),_AdGenAOSRtpChannelTotalRxPacketsUnknown_Type())
adGenAOSRtpChannelTotalRxPacketsUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalRxPacketsUnknown.setStatus(_B)
_AdGenAOSRtpChannelTotalTxPackets_Type=Integer32
_AdGenAOSRtpChannelTotalTxPackets_Object=MibTableColumn
adGenAOSRtpChannelTotalTxPackets=_AdGenAOSRtpChannelTotalTxPackets_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,9),_AdGenAOSRtpChannelTotalTxPackets_Type())
adGenAOSRtpChannelTotalTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalTxPackets.setStatus(_B)
_AdGenAOSRtpChannelTotalTxOctets_Type=Integer32
_AdGenAOSRtpChannelTotalTxOctets_Object=MibTableColumn
adGenAOSRtpChannelTotalTxOctets=_AdGenAOSRtpChannelTotalTxOctets_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,10),_AdGenAOSRtpChannelTotalTxOctets_Type())
adGenAOSRtpChannelTotalTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalTxOctets.setStatus(_B)
_AdGenAOSRtpChannelTotalRxMaxDepth_Type=Integer32
_AdGenAOSRtpChannelTotalRxMaxDepth_Object=MibTableColumn
adGenAOSRtpChannelTotalRxMaxDepth=_AdGenAOSRtpChannelTotalRxMaxDepth_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,11),_AdGenAOSRtpChannelTotalRxMaxDepth_Type())
adGenAOSRtpChannelTotalRxMaxDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalRxMaxDepth.setStatus(_D)
_AdGenAOSRtpChannelTotalRxFrameLateDiscards_Type=Integer32
_AdGenAOSRtpChannelTotalRxFrameLateDiscards_Object=MibTableColumn
adGenAOSRtpChannelTotalRxFrameLateDiscards=_AdGenAOSRtpChannelTotalRxFrameLateDiscards_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,12),_AdGenAOSRtpChannelTotalRxFrameLateDiscards_Type())
adGenAOSRtpChannelTotalRxFrameLateDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalRxFrameLateDiscards.setStatus(_D)
_AdGenAOSRtpChannelTotalRxFrameOverflows_Type=Integer32
_AdGenAOSRtpChannelTotalRxFrameOverflows_Object=MibTableColumn
adGenAOSRtpChannelTotalRxFrameOverflows=_AdGenAOSRtpChannelTotalRxFrameOverflows_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,14),_AdGenAOSRtpChannelTotalRxFrameOverflows_Type())
adGenAOSRtpChannelTotalRxFrameOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalRxFrameOverflows.setStatus(_D)
_AdGenAOSRtpChannelTotalRxFrameOutOfOrders_Type=Integer32
_AdGenAOSRtpChannelTotalRxFrameOutOfOrders_Object=MibTableColumn
adGenAOSRtpChannelTotalRxFrameOutOfOrders=_AdGenAOSRtpChannelTotalRxFrameOutOfOrders_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,15),_AdGenAOSRtpChannelTotalRxFrameOutOfOrders_Type())
adGenAOSRtpChannelTotalRxFrameOutOfOrders.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTotalRxFrameOutOfOrders.setStatus(_B)
_AdGenAOSRtpChannelClearCounters_Type=Integer32
_AdGenAOSRtpChannelClearCounters_Object=MibTableColumn
adGenAOSRtpChannelClearCounters=_AdGenAOSRtpChannelClearCounters_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,16),_AdGenAOSRtpChannelClearCounters_Type())
adGenAOSRtpChannelClearCounters.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenAOSRtpChannelClearCounters.setStatus(_B)
_AdGenAOSRtpChannelTimeSinceLastClearCounters_Type=DisplayString
_AdGenAOSRtpChannelTimeSinceLastClearCounters_Object=MibTableColumn
adGenAOSRtpChannelTimeSinceLastClearCounters=_AdGenAOSRtpChannelTimeSinceLastClearCounters_Object((1,3,6,1,4,1,664,5,53,5,2,1,4,1,17),_AdGenAOSRtpChannelTimeSinceLastClearCounters_Type())
adGenAOSRtpChannelTimeSinceLastClearCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAOSRtpChannelTimeSinceLastClearCounters.setStatus(_B)
_AdGenAOSMediaGatewayConformance_ObjectIdentity=ObjectIdentity
adGenAOSMediaGatewayConformance=_AdGenAOSMediaGatewayConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,5,2,99))
_AdGenAOSMediaGatewayCompliances_ObjectIdentity=ObjectIdentity
adGenAOSMediaGatewayCompliances=_AdGenAOSMediaGatewayCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,5,2,99,1))
_AdGenAOSMediaGatewayMIBGroups_ObjectIdentity=ObjectIdentity
adGenAOSMediaGatewayMIBGroups=_AdGenAOSMediaGatewayMIBGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,5,2,99,2))
adGenAOSMediaGatewayRtpSessionGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,5,2,99,2,1))
adGenAOSMediaGatewayRtpSessionGroup.setObjects(*((_A,_F),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:adGenAOSMediaGatewayRtpSessionGroup.setStatus(_B)
adGenAOSMediaGatewayRtpSessionTotalsGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,5,2,99,2,2))
adGenAOSMediaGatewayRtpSessionTotalsGroup.setObjects(*((_A,_G),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:adGenAOSMediaGatewayRtpSessionTotalsGroup.setStatus(_B)
adGenAOSMediaGatewayInfoGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,5,2,99,2,3))
adGenAOSMediaGatewayInfoGroup.setObjects(*((_A,_H),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:adGenAOSMediaGatewayInfoGroup.setStatus(_B)
adGenAOSMediaGatewayRtpChannelTotalsGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,5,2,99,2,4))
adGenAOSMediaGatewayRtpChannelTotalsGroup.setObjects(*((_A,_I),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:adGenAOSMediaGatewayRtpChannelTotalsGroup.setStatus(_B)
adGenAOSMediaGatewayCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,5,2,99,1,1))
adGenAOSMediaGatewayCompliance.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:adGenAOSMediaGatewayCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'adGenAOSMediaGateway':adGenAOSMediaGateway,'adGenAOSMediaGatewayObjects':adGenAOSMediaGatewayObjects,'adGenAOSRtpSessionTable':adGenAOSRtpSessionTable,'adGenAOSRtpSessionEntry':adGenAOSRtpSessionEntry,_F:adGenAOSRtpSessionChannelId,_M:adGenAOSRtpSessionChannelIdName,_N:adGenAOSRtpSessionStatus,_O:adGenAOSRtpSessionStartTime,_P:adGenAOSRtpSessionDuration,_Q:adGenAOSRtpSessionVocoder,_R:adGenAOSRtpSessionVAD,_S:adGenAOSRtpSessionTdmPortDescription,_T:adGenAOSRtpSessionLocalIPAddress,_U:adGenAOSRtpSessionLocalUdpPort,_V:adGenAOSRtpSessionSIPPortDescription,_W:adGenAOSRtpSessionRemoteIPAddress,_X:adGenAOSRtpSessionRemoteUdpPort,_Y:adGenAOSRtpSessionTxFramesPerPacket,_Z:adGenAOSRtpSessionEchoCancellerEnabled,_a:adGenAOSRtpSessionRxPackets,_b:adGenAOSRtpSessionRxOctets,_c:adGenAOSRtpSessionRxPacketsLost,_d:adGenAOSRtpSessionRxPacketsUnknown,_e:adGenAOSRtpSessionRxJitterBufferDepth,_f:adGenAOSRtpSessionRxMaxJitterBufferDepth,_g:adGenAOSRtpSessionRxFrameLateDiscards,_h:adGenAOSRtpSessionRxFrameOverflows,_i:adGenAOSRtpSessionRxFrameOutOfOrders,_j:adGenAOSRtpSessionRxSyncSource,_k:adGenAOSRtpSessionTxPackets,_l:adGenAOSRtpSessionTxOctets,_m:adGenAOSRtpSessionTxSyncSource,'adGenAOSRtpSessionTotalsTable':adGenAOSRtpSessionTotalsTable,'adGenAOSRtpSessionTotalsEntry':adGenAOSRtpSessionTotalsEntry,_G:adGenAOSRtpSessionTotalsSessions,_n:adGenAOSRtpSessionTotalsSessionDuration,_o:adGenAOSRtpSessionTotalsRxPackets,_p:adGenAOSRtpSessionTotalsRxOctets,_q:adGenAOSRtpSessionTotalsRxPacketsLost,_r:adGenAOSRtpSessionTotalsRxPacketsUnknown,_s:adGenAOSRtpSessionTotalsTxPackets,_t:adGenAOSRtpSessionTotalsTxOctets,_u:adGenAOSRtpSessionTotalsRxFrameLateDiscards,_v:adGenAOSRtpSessionTotalsRxFrameOverflows,_w:adGenAOSRtpSessionTotalsRxFrameOutOfOrders,_x:adGenAOSRtpSessionTotalsClearCounters,_y:adGenAOSRtpSessionTotalsTimeSinceLastClearCounters,'adGenAOSMediaGatewayInfoTable':adGenAOSMediaGatewayInfoTable,'adGenAOSMediaGatewayInfoEntry':adGenAOSMediaGatewayInfoEntry,_H:adGenAOSMediaGatewayInfoIdentifier,_z:adGenAOSMediaGatewayInfoSoftwareVersion,_A0:adGenAOSMediaGatewayInfoUtilization,_A1:adGenAOSMediaGatewayInfoUtilizationMaximum,_A2:adGenAOSMediaGatewayInfoFreePacketBuffers,_A3:adGenAOSMediaGatewayInfoUptime,'adGenAOSRtpChannelTotalTable':adGenAOSRtpChannelTotalTable,'adGenAOSRtpChannelTotalEntry':adGenAOSRtpChannelTotalEntry,_I:adGenAOSRtpChannelTotalId,_A4:adGenAOSRtpChannelTotalIdName,_A5:adGenAOSRtpChannelTotalSessions,_A6:adGenAOSRtpChannelTotalSessionDuration,_A7:adGenAOSRtpChannelTotalRxPackets,_A8:adGenAOSRtpChannelTotalRxOctets,_A9:adGenAOSRtpChannelTotalRxPacketsLost,_AA:adGenAOSRtpChannelTotalRxPacketsUnknown,_AB:adGenAOSRtpChannelTotalTxPackets,_AC:adGenAOSRtpChannelTotalTxOctets,_AD:adGenAOSRtpChannelTotalRxMaxDepth,_AE:adGenAOSRtpChannelTotalRxFrameLateDiscards,_AF:adGenAOSRtpChannelTotalRxFrameOverflows,_AG:adGenAOSRtpChannelTotalRxFrameOutOfOrders,_AH:adGenAOSRtpChannelClearCounters,_AI:adGenAOSRtpChannelTimeSinceLastClearCounters,'adGenAOSMediaGatewayConformance':adGenAOSMediaGatewayConformance,'adGenAOSMediaGatewayCompliances':adGenAOSMediaGatewayCompliances,'adGenAOSMediaGatewayCompliance':adGenAOSMediaGatewayCompliance,'adGenAOSMediaGatewayMIBGroups':adGenAOSMediaGatewayMIBGroups,_AJ:adGenAOSMediaGatewayRtpSessionGroup,_AK:adGenAOSMediaGatewayRtpSessionTotalsGroup,_AL:adGenAOSMediaGatewayInfoGroup,_AM:adGenAOSMediaGatewayRtpChannelTotalsGroup,'adGenAOSMediaGatewayMIB':adGenAOSMediaGatewayMIB})