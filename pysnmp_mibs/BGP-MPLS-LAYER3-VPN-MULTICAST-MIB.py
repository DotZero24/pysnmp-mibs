_A_='mvpnMvrfActionTaken'
_Az='mvpnMrouteNextHopCounterDiscontinuityTime'
_Ay='mvpnMrouteNextHopPkts'
_Ax='mvpnMrouteNextHopOctets'
_Aw='mvpnMrouteNextHopProtocol'
_Av='mvpnMrouteNextHopClosestMemberHops'
_Au='mvpnMrouteNextHopExpiryTime'
_At='mvpnMrouteNextHopState'
_As='mvpnMrouteCounterDiscontinuityTime'
_Ar='mvpnMrouteNumberOfRemoteReplication'
_Aq='mvpnMrouteNumberOfLocalReplication'
_Ap='mvpnMroutePmsiPointer'
_Ao='mvpnMrouteDroppedInPackets'
_An='mvpnMrouteDroppedInOctets'
_Am='mvpnMrouteTtlDroppedPackets'
_Al='mvpnMrouteTtlDroppedOctets'
_Ak='mvpnMroutePkts'
_Aj='mvpnMrouteOctets'
_Ai='mvpnMrouteRtType'
_Ah='mvpnMrouteRtPrefixLength'
_Ag='mvpnMrouteRtAddr'
_Af='mvpnMrouteRtAddrType'
_Ae='mvpnMrouteRtProtocol'
_Ad='mvpnMrouteProtocol'
_Ac='mvpnMrouteExpiryTime'
_Ab='mvpnMrouteInIfIndex'
_Aa='mvpnMrouteUpstreamNeighborAddr'
_AZ='mvpnMrouteUpstreamNeighborAddrType'
_AY='mvpnAdvtCounterDiscontinuityTime'
_AX='mvpnAdvtLastReceivedTime'
_AW='mvpnAdvtLastSentTime'
_AV='mvpnAdvtReceivedMalformedTunnelId'
_AU='mvpnAdvtReceivedMalformedTunnelType'
_AT='mvpnAdvtReceivedError'
_AS='mvpnAdvtReceived'
_AR='mvpnAdvtSent'
_AQ='mvpnSpmsiPmsiPointer'
_AP='mvpnPmsiEncapsulationType'
_AO='mvpnPmsiTunnelPimGroupAddr'
_AN='mvpnPmsiTunnelPimGroupAddrType'
_AM='mvpnPmsiTunnelAttribute'
_AL='mvpnPmsiTunnelType'
_AK='mvpnPmsiRD'
_AJ='mvpnBgpMaxSrcActiveAdRouteFreq'
_AI='mvpnBgpMaxSrcActiveAdRoutes'
_AH='mvpnBgpMaxSpmsiAdRouteFreq'
_AG='mvpnBgpMaxSpmsiAdRoutes'
_AF='mvpnBgpMsgRateLimit'
_AE='mvpnBgpSrcASExtendedCommunity'
_AD='mvpnBgpVrfRouteImportExtendedCommunity'
_AC='mvpnBgpMode'
_AB='mvpnGenInterAsPmsiInfo'
_AA='mvpnGenIpmsiInfo'
_A9='mvpnBgpSrcSharedTreeJoinTimer'
_A8='mvpnBgpCmcastRouteWithdrawalTimer'
_A7='mvpnBgpV6Mvrfs'
_A6='mvpnBgpV4Mvrfs'
_A5='mvpnMldpMvrfs'
_A4='mvpnSPTunnelLimit'
_A3='mvpnPimV6Mvrfs'
_A2='mvpnPimV4Mvrfs'
_A1='mvpnV6Mvrfs'
_A0='mvpnV4Mvrfs'
_z='mvpnMvrfs'
_y='mvpnMrouteNextHopAddr'
_x='mvpnMrouteNextHopAddrType'
_w='mvpnMrouteNextHopIfIndex'
_v='mvpnMrouteNextHopSourcePrefixLength'
_u='mvpnMrouteNextHopSourceAddrs'
_t='mvpnMrouteNextHopSourceAddrType'
_s='mvpnMrouteNextHopGroupPrefixLength'
_r='mvpnMrouteNextHopGroupAddr'
_q='mvpnMrouteNextHopGroupAddrType'
_p='mvpnMrouteCmcastSourcePrefixLength'
_o='mvpnMrouteCmcastSourceAddrs'
_n='mvpnMrouteCmcastSourceAddrType'
_m='mvpnMrouteCmcastGroupPrefixLength'
_l='mvpnMrouteCmcastGroupAddr'
_k='mvpnMrouteCmcastGroupAddrType'
_j='mvpnAdvtPeerAddr'
_i='mvpnAdvtPeerAddrType'
_h='mvpnAdvtType'
_g='mvpnSpmsiCmcastSourcePrefixLen'
_f='mvpnSpmsiCmcastSourceAddr'
_e='mvpnSpmsiCmcastSourceAddrType'
_d='mvpnSpmsiCmcastGroupPrefixLen'
_c='mvpnSpmsiCmcastGroupAddr'
_b='mvpnSpmsiCmcastGroupAddrType'
_a='mvpnPmsiTunnelIfIndex'
_Z='routes per second'
_Y='milliseconds'
_X='mvpnBgpGroup'
_W='mvpnBgpScalarGroup'
_V='mvpnNotificationGroup'
_U='mvpnMrouteNextHopGroup'
_T='mvpnMrouteGroup'
_S='mvpnPmsiGroup'
_R='mvpnGenericGroup'
_Q='mvpnScalarGroup'
_P='mvpnGenCustomerSiteType'
_O='mvpnGenUmhSelection'
_N='mvpnGenCmcastRouteProtocol'
_M='mvpnGenMvrfLastActionTime'
_L='mvpnGenMvrfLastAction'
_K='mvpnAdvtStatsGroup'
_J='mvpnGenMvrfCreationTime'
_I='mplsL3VpnVrfName'
_H='MPLS-L3VPN-STD-MIB'
_G='read-write'
_F='Unsigned32'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='current'
_A='BGP-MPLS-LAYER3-VPN-MULTICAST-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipMRouteProtocol,IANAipRouteProtocol=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol','IANAipRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
L2L3VpnMcastProviderTunnelType,=mibBuilder.importSymbols('L2L3-VPN-MULTICAST-TC-MIB','L2L3VpnMcastProviderTunnelType')
MplsL3VpnRouteDistinguisher,mplsL3VpnVrfName=mibBuilder.importSymbols(_H,'MplsL3VpnRouteDistinguisher',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','mib-2')
DateAndTime,DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp')
mvpnMIB=ModuleIdentity((1,3,6,1,2,1,243))
if mibBuilder.loadTexts:mvpnMIB.setRevisions(('2018-12-14 00:00',))
_MvpnNotifications_ObjectIdentity=ObjectIdentity
mvpnNotifications=_MvpnNotifications_ObjectIdentity((1,3,6,1,2,1,243,0))
_MvpnObjects_ObjectIdentity=ObjectIdentity
mvpnObjects=_MvpnObjects_ObjectIdentity((1,3,6,1,2,1,243,1))
_MvpnScalars_ObjectIdentity=ObjectIdentity
mvpnScalars=_MvpnScalars_ObjectIdentity((1,3,6,1,2,1,243,1,1))
_MvpnMvrfs_Type=Gauge32
_MvpnMvrfs_Object=MibScalar
mvpnMvrfs=_MvpnMvrfs_Object((1,3,6,1,2,1,243,1,1,1),_MvpnMvrfs_Type())
mvpnMvrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMvrfs.setStatus(_B)
_MvpnV4Mvrfs_Type=Gauge32
_MvpnV4Mvrfs_Object=MibScalar
mvpnV4Mvrfs=_MvpnV4Mvrfs_Object((1,3,6,1,2,1,243,1,1,2),_MvpnV4Mvrfs_Type())
mvpnV4Mvrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnV4Mvrfs.setStatus(_B)
_MvpnV6Mvrfs_Type=Gauge32
_MvpnV6Mvrfs_Object=MibScalar
mvpnV6Mvrfs=_MvpnV6Mvrfs_Object((1,3,6,1,2,1,243,1,1,3),_MvpnV6Mvrfs_Type())
mvpnV6Mvrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnV6Mvrfs.setStatus(_B)
_MvpnMldpMvrfs_Type=Gauge32
_MvpnMldpMvrfs_Object=MibScalar
mvpnMldpMvrfs=_MvpnMldpMvrfs_Object((1,3,6,1,2,1,243,1,1,4),_MvpnMldpMvrfs_Type())
mvpnMldpMvrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMldpMvrfs.setStatus(_B)
_MvpnPimV4Mvrfs_Type=Gauge32
_MvpnPimV4Mvrfs_Object=MibScalar
mvpnPimV4Mvrfs=_MvpnPimV4Mvrfs_Object((1,3,6,1,2,1,243,1,1,5),_MvpnPimV4Mvrfs_Type())
mvpnPimV4Mvrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnPimV4Mvrfs.setStatus(_B)
_MvpnPimV6Mvrfs_Type=Gauge32
_MvpnPimV6Mvrfs_Object=MibScalar
mvpnPimV6Mvrfs=_MvpnPimV6Mvrfs_Object((1,3,6,1,2,1,243,1,1,6),_MvpnPimV6Mvrfs_Type())
mvpnPimV6Mvrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnPimV6Mvrfs.setStatus(_B)
_MvpnBgpV4Mvrfs_Type=Gauge32
_MvpnBgpV4Mvrfs_Object=MibScalar
mvpnBgpV4Mvrfs=_MvpnBgpV4Mvrfs_Object((1,3,6,1,2,1,243,1,1,7),_MvpnBgpV4Mvrfs_Type())
mvpnBgpV4Mvrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnBgpV4Mvrfs.setStatus(_B)
_MvpnBgpV6Mvrfs_Type=Gauge32
_MvpnBgpV6Mvrfs_Object=MibScalar
mvpnBgpV6Mvrfs=_MvpnBgpV6Mvrfs_Object((1,3,6,1,2,1,243,1,1,8),_MvpnBgpV6Mvrfs_Type())
mvpnBgpV6Mvrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnBgpV6Mvrfs.setStatus(_B)
class _MvpnSPTunnelLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MvpnSPTunnelLimit_Type.__name__=_F
_MvpnSPTunnelLimit_Object=MibScalar
mvpnSPTunnelLimit=_MvpnSPTunnelLimit_Object((1,3,6,1,2,1,243,1,1,9),_MvpnSPTunnelLimit_Type())
mvpnSPTunnelLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:mvpnSPTunnelLimit.setStatus(_B)
_MvpnBgpCmcastRouteWithdrawalTimer_Type=Unsigned32
_MvpnBgpCmcastRouteWithdrawalTimer_Object=MibScalar
mvpnBgpCmcastRouteWithdrawalTimer=_MvpnBgpCmcastRouteWithdrawalTimer_Object((1,3,6,1,2,1,243,1,1,10),_MvpnBgpCmcastRouteWithdrawalTimer_Type())
mvpnBgpCmcastRouteWithdrawalTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:mvpnBgpCmcastRouteWithdrawalTimer.setStatus(_B)
if mibBuilder.loadTexts:mvpnBgpCmcastRouteWithdrawalTimer.setUnits(_Y)
_MvpnBgpSrcSharedTreeJoinTimer_Type=Unsigned32
_MvpnBgpSrcSharedTreeJoinTimer_Object=MibScalar
mvpnBgpSrcSharedTreeJoinTimer=_MvpnBgpSrcSharedTreeJoinTimer_Object((1,3,6,1,2,1,243,1,1,11),_MvpnBgpSrcSharedTreeJoinTimer_Type())
mvpnBgpSrcSharedTreeJoinTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:mvpnBgpSrcSharedTreeJoinTimer.setStatus(_B)
if mibBuilder.loadTexts:mvpnBgpSrcSharedTreeJoinTimer.setUnits(_Y)
_MvpnGenericTable_Object=MibTable
mvpnGenericTable=_MvpnGenericTable_Object((1,3,6,1,2,1,243,1,2))
if mibBuilder.loadTexts:mvpnGenericTable.setStatus(_B)
_MvpnGenericEntry_Object=MibTableRow
mvpnGenericEntry=_MvpnGenericEntry_Object((1,3,6,1,2,1,243,1,2,1))
mvpnGenericEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:mvpnGenericEntry.setStatus(_B)
class _MvpnGenMvrfLastAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('createdMvrf',1),('deletedMvrf',2),('modifiedMvrfIpmsiConfig',3),('modifiedMvrfSpmsiConfig',4)))
_MvpnGenMvrfLastAction_Type.__name__=_E
_MvpnGenMvrfLastAction_Object=MibTableColumn
mvpnGenMvrfLastAction=_MvpnGenMvrfLastAction_Object((1,3,6,1,2,1,243,1,2,1,2),_MvpnGenMvrfLastAction_Type())
mvpnGenMvrfLastAction.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnGenMvrfLastAction.setStatus(_B)
_MvpnGenMvrfLastActionTime_Type=DateAndTime
_MvpnGenMvrfLastActionTime_Object=MibTableColumn
mvpnGenMvrfLastActionTime=_MvpnGenMvrfLastActionTime_Object((1,3,6,1,2,1,243,1,2,1,3),_MvpnGenMvrfLastActionTime_Type())
mvpnGenMvrfLastActionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnGenMvrfLastActionTime.setStatus(_B)
_MvpnGenMvrfCreationTime_Type=DateAndTime
_MvpnGenMvrfCreationTime_Object=MibTableColumn
mvpnGenMvrfCreationTime=_MvpnGenMvrfCreationTime_Object((1,3,6,1,2,1,243,1,2,1,4),_MvpnGenMvrfCreationTime_Type())
mvpnGenMvrfCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnGenMvrfCreationTime.setStatus(_B)
class _MvpnGenCmcastRouteProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pim',1),('bgp',2)))
_MvpnGenCmcastRouteProtocol_Type.__name__=_E
_MvpnGenCmcastRouteProtocol_Object=MibTableColumn
mvpnGenCmcastRouteProtocol=_MvpnGenCmcastRouteProtocol_Object((1,3,6,1,2,1,243,1,2,1,5),_MvpnGenCmcastRouteProtocol_Type())
mvpnGenCmcastRouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnGenCmcastRouteProtocol.setStatus(_B)
_MvpnGenIpmsiInfo_Type=RowPointer
_MvpnGenIpmsiInfo_Object=MibTableColumn
mvpnGenIpmsiInfo=_MvpnGenIpmsiInfo_Object((1,3,6,1,2,1,243,1,2,1,6),_MvpnGenIpmsiInfo_Type())
mvpnGenIpmsiInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnGenIpmsiInfo.setStatus(_B)
_MvpnGenInterAsPmsiInfo_Type=RowPointer
_MvpnGenInterAsPmsiInfo_Object=MibTableColumn
mvpnGenInterAsPmsiInfo=_MvpnGenInterAsPmsiInfo_Object((1,3,6,1,2,1,243,1,2,1,7),_MvpnGenInterAsPmsiInfo_Type())
mvpnGenInterAsPmsiInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnGenInterAsPmsiInfo.setStatus(_B)
class _MvpnGenUmhSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('highestPeAddress',1),('cRootGroupHashing',2),('ucastUmhRoute',3)))
_MvpnGenUmhSelection_Type.__name__=_E
_MvpnGenUmhSelection_Object=MibTableColumn
mvpnGenUmhSelection=_MvpnGenUmhSelection_Object((1,3,6,1,2,1,243,1,2,1,8),_MvpnGenUmhSelection_Type())
mvpnGenUmhSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnGenUmhSelection.setStatus(_B)
class _MvpnGenCustomerSiteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('senderReceiver',1),('receiverOnly',2),('senderOnly',3)))
_MvpnGenCustomerSiteType_Type.__name__=_E
_MvpnGenCustomerSiteType_Object=MibTableColumn
mvpnGenCustomerSiteType=_MvpnGenCustomerSiteType_Object((1,3,6,1,2,1,243,1,2,1,9),_MvpnGenCustomerSiteType_Type())
mvpnGenCustomerSiteType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnGenCustomerSiteType.setStatus(_B)
_MvpnBgpTable_Object=MibTable
mvpnBgpTable=_MvpnBgpTable_Object((1,3,6,1,2,1,243,1,3))
if mibBuilder.loadTexts:mvpnBgpTable.setStatus(_B)
_MvpnBgpEntry_Object=MibTableRow
mvpnBgpEntry=_MvpnBgpEntry_Object((1,3,6,1,2,1,243,1,3,1))
mvpnBgpEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:mvpnBgpEntry.setStatus(_B)
class _MvpnBgpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),('rptSpt',1),('sptOnly',2)))
_MvpnBgpMode_Type.__name__=_E
_MvpnBgpMode_Object=MibTableColumn
mvpnBgpMode=_MvpnBgpMode_Object((1,3,6,1,2,1,243,1,3,1,1),_MvpnBgpMode_Type())
mvpnBgpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnBgpMode.setStatus(_B)
_MvpnBgpVrfRouteImportExtendedCommunity_Type=MplsL3VpnRouteDistinguisher
_MvpnBgpVrfRouteImportExtendedCommunity_Object=MibTableColumn
mvpnBgpVrfRouteImportExtendedCommunity=_MvpnBgpVrfRouteImportExtendedCommunity_Object((1,3,6,1,2,1,243,1,3,1,2),_MvpnBgpVrfRouteImportExtendedCommunity_Type())
mvpnBgpVrfRouteImportExtendedCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnBgpVrfRouteImportExtendedCommunity.setStatus(_B)
_MvpnBgpSrcASExtendedCommunity_Type=Unsigned32
_MvpnBgpSrcASExtendedCommunity_Object=MibTableColumn
mvpnBgpSrcASExtendedCommunity=_MvpnBgpSrcASExtendedCommunity_Object((1,3,6,1,2,1,243,1,3,1,3),_MvpnBgpSrcASExtendedCommunity_Type())
mvpnBgpSrcASExtendedCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnBgpSrcASExtendedCommunity.setStatus(_B)
class _MvpnBgpMsgRateLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MvpnBgpMsgRateLimit_Type.__name__=_F
_MvpnBgpMsgRateLimit_Object=MibTableColumn
mvpnBgpMsgRateLimit=_MvpnBgpMsgRateLimit_Object((1,3,6,1,2,1,243,1,3,1,4),_MvpnBgpMsgRateLimit_Type())
mvpnBgpMsgRateLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:mvpnBgpMsgRateLimit.setStatus(_B)
if mibBuilder.loadTexts:mvpnBgpMsgRateLimit.setUnits('messages per second')
class _MvpnBgpMaxSpmsiAdRoutes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MvpnBgpMaxSpmsiAdRoutes_Type.__name__=_F
_MvpnBgpMaxSpmsiAdRoutes_Object=MibTableColumn
mvpnBgpMaxSpmsiAdRoutes=_MvpnBgpMaxSpmsiAdRoutes_Object((1,3,6,1,2,1,243,1,3,1,5),_MvpnBgpMaxSpmsiAdRoutes_Type())
mvpnBgpMaxSpmsiAdRoutes.setMaxAccess(_G)
if mibBuilder.loadTexts:mvpnBgpMaxSpmsiAdRoutes.setStatus(_B)
class _MvpnBgpMaxSpmsiAdRouteFreq_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MvpnBgpMaxSpmsiAdRouteFreq_Type.__name__=_F
_MvpnBgpMaxSpmsiAdRouteFreq_Object=MibTableColumn
mvpnBgpMaxSpmsiAdRouteFreq=_MvpnBgpMaxSpmsiAdRouteFreq_Object((1,3,6,1,2,1,243,1,3,1,6),_MvpnBgpMaxSpmsiAdRouteFreq_Type())
mvpnBgpMaxSpmsiAdRouteFreq.setMaxAccess(_G)
if mibBuilder.loadTexts:mvpnBgpMaxSpmsiAdRouteFreq.setStatus(_B)
if mibBuilder.loadTexts:mvpnBgpMaxSpmsiAdRouteFreq.setUnits(_Z)
class _MvpnBgpMaxSrcActiveAdRoutes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MvpnBgpMaxSrcActiveAdRoutes_Type.__name__=_F
_MvpnBgpMaxSrcActiveAdRoutes_Object=MibTableColumn
mvpnBgpMaxSrcActiveAdRoutes=_MvpnBgpMaxSrcActiveAdRoutes_Object((1,3,6,1,2,1,243,1,3,1,7),_MvpnBgpMaxSrcActiveAdRoutes_Type())
mvpnBgpMaxSrcActiveAdRoutes.setMaxAccess(_G)
if mibBuilder.loadTexts:mvpnBgpMaxSrcActiveAdRoutes.setStatus(_B)
class _MvpnBgpMaxSrcActiveAdRouteFreq_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MvpnBgpMaxSrcActiveAdRouteFreq_Type.__name__=_F
_MvpnBgpMaxSrcActiveAdRouteFreq_Object=MibTableColumn
mvpnBgpMaxSrcActiveAdRouteFreq=_MvpnBgpMaxSrcActiveAdRouteFreq_Object((1,3,6,1,2,1,243,1,3,1,8),_MvpnBgpMaxSrcActiveAdRouteFreq_Type())
mvpnBgpMaxSrcActiveAdRouteFreq.setMaxAccess(_G)
if mibBuilder.loadTexts:mvpnBgpMaxSrcActiveAdRouteFreq.setStatus(_B)
if mibBuilder.loadTexts:mvpnBgpMaxSrcActiveAdRouteFreq.setUnits(_Z)
_MvpnPmsiTable_Object=MibTable
mvpnPmsiTable=_MvpnPmsiTable_Object((1,3,6,1,2,1,243,1,4))
if mibBuilder.loadTexts:mvpnPmsiTable.setStatus(_B)
_MvpnPmsiEntry_Object=MibTableRow
mvpnPmsiEntry=_MvpnPmsiEntry_Object((1,3,6,1,2,1,243,1,4,1))
mvpnPmsiEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:mvpnPmsiEntry.setStatus(_B)
_MvpnPmsiTunnelIfIndex_Type=InterfaceIndex
_MvpnPmsiTunnelIfIndex_Object=MibTableColumn
mvpnPmsiTunnelIfIndex=_MvpnPmsiTunnelIfIndex_Object((1,3,6,1,2,1,243,1,4,1,1),_MvpnPmsiTunnelIfIndex_Type())
mvpnPmsiTunnelIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnPmsiTunnelIfIndex.setStatus(_B)
_MvpnPmsiRD_Type=MplsL3VpnRouteDistinguisher
_MvpnPmsiRD_Object=MibTableColumn
mvpnPmsiRD=_MvpnPmsiRD_Object((1,3,6,1,2,1,243,1,4,1,3),_MvpnPmsiRD_Type())
mvpnPmsiRD.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnPmsiRD.setStatus(_B)
_MvpnPmsiTunnelType_Type=L2L3VpnMcastProviderTunnelType
_MvpnPmsiTunnelType_Object=MibTableColumn
mvpnPmsiTunnelType=_MvpnPmsiTunnelType_Object((1,3,6,1,2,1,243,1,4,1,4),_MvpnPmsiTunnelType_Type())
mvpnPmsiTunnelType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnPmsiTunnelType.setStatus(_B)
_MvpnPmsiTunnelAttribute_Type=RowPointer
_MvpnPmsiTunnelAttribute_Object=MibTableColumn
mvpnPmsiTunnelAttribute=_MvpnPmsiTunnelAttribute_Object((1,3,6,1,2,1,243,1,4,1,5),_MvpnPmsiTunnelAttribute_Type())
mvpnPmsiTunnelAttribute.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnPmsiTunnelAttribute.setStatus(_B)
_MvpnPmsiTunnelPimGroupAddrType_Type=InetAddressType
_MvpnPmsiTunnelPimGroupAddrType_Object=MibTableColumn
mvpnPmsiTunnelPimGroupAddrType=_MvpnPmsiTunnelPimGroupAddrType_Object((1,3,6,1,2,1,243,1,4,1,6),_MvpnPmsiTunnelPimGroupAddrType_Type())
mvpnPmsiTunnelPimGroupAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnPmsiTunnelPimGroupAddrType.setStatus(_B)
_MvpnPmsiTunnelPimGroupAddr_Type=InetAddress
_MvpnPmsiTunnelPimGroupAddr_Object=MibTableColumn
mvpnPmsiTunnelPimGroupAddr=_MvpnPmsiTunnelPimGroupAddr_Object((1,3,6,1,2,1,243,1,4,1,7),_MvpnPmsiTunnelPimGroupAddr_Type())
mvpnPmsiTunnelPimGroupAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnPmsiTunnelPimGroupAddr.setStatus(_B)
class _MvpnPmsiEncapsulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('greIp',1),('ipIp',2),('mpls',3)))
_MvpnPmsiEncapsulationType_Type.__name__=_E
_MvpnPmsiEncapsulationType_Object=MibTableColumn
mvpnPmsiEncapsulationType=_MvpnPmsiEncapsulationType_Object((1,3,6,1,2,1,243,1,4,1,8),_MvpnPmsiEncapsulationType_Type())
mvpnPmsiEncapsulationType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnPmsiEncapsulationType.setStatus(_B)
_MvpnSpmsiTable_Object=MibTable
mvpnSpmsiTable=_MvpnSpmsiTable_Object((1,3,6,1,2,1,243,1,5))
if mibBuilder.loadTexts:mvpnSpmsiTable.setStatus(_B)
_MvpnSpmsiEntry_Object=MibTableRow
mvpnSpmsiEntry=_MvpnSpmsiEntry_Object((1,3,6,1,2,1,243,1,5,1))
mvpnSpmsiEntry.setIndexNames((0,_H,_I),(0,_A,_b),(0,_A,_c),(0,_A,_d),(0,_A,_e),(0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:mvpnSpmsiEntry.setStatus(_B)
_MvpnSpmsiCmcastGroupAddrType_Type=InetAddressType
_MvpnSpmsiCmcastGroupAddrType_Object=MibTableColumn
mvpnSpmsiCmcastGroupAddrType=_MvpnSpmsiCmcastGroupAddrType_Object((1,3,6,1,2,1,243,1,5,1,1),_MvpnSpmsiCmcastGroupAddrType_Type())
mvpnSpmsiCmcastGroupAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnSpmsiCmcastGroupAddrType.setStatus(_B)
_MvpnSpmsiCmcastGroupAddr_Type=InetAddress
_MvpnSpmsiCmcastGroupAddr_Object=MibTableColumn
mvpnSpmsiCmcastGroupAddr=_MvpnSpmsiCmcastGroupAddr_Object((1,3,6,1,2,1,243,1,5,1,2),_MvpnSpmsiCmcastGroupAddr_Type())
mvpnSpmsiCmcastGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnSpmsiCmcastGroupAddr.setStatus(_B)
_MvpnSpmsiCmcastGroupPrefixLen_Type=InetAddressPrefixLength
_MvpnSpmsiCmcastGroupPrefixLen_Object=MibTableColumn
mvpnSpmsiCmcastGroupPrefixLen=_MvpnSpmsiCmcastGroupPrefixLen_Object((1,3,6,1,2,1,243,1,5,1,3),_MvpnSpmsiCmcastGroupPrefixLen_Type())
mvpnSpmsiCmcastGroupPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnSpmsiCmcastGroupPrefixLen.setStatus(_B)
_MvpnSpmsiCmcastSourceAddrType_Type=InetAddressType
_MvpnSpmsiCmcastSourceAddrType_Object=MibTableColumn
mvpnSpmsiCmcastSourceAddrType=_MvpnSpmsiCmcastSourceAddrType_Object((1,3,6,1,2,1,243,1,5,1,4),_MvpnSpmsiCmcastSourceAddrType_Type())
mvpnSpmsiCmcastSourceAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnSpmsiCmcastSourceAddrType.setStatus(_B)
_MvpnSpmsiCmcastSourceAddr_Type=InetAddress
_MvpnSpmsiCmcastSourceAddr_Object=MibTableColumn
mvpnSpmsiCmcastSourceAddr=_MvpnSpmsiCmcastSourceAddr_Object((1,3,6,1,2,1,243,1,5,1,5),_MvpnSpmsiCmcastSourceAddr_Type())
mvpnSpmsiCmcastSourceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnSpmsiCmcastSourceAddr.setStatus(_B)
_MvpnSpmsiCmcastSourcePrefixLen_Type=InetAddressPrefixLength
_MvpnSpmsiCmcastSourcePrefixLen_Object=MibTableColumn
mvpnSpmsiCmcastSourcePrefixLen=_MvpnSpmsiCmcastSourcePrefixLen_Object((1,3,6,1,2,1,243,1,5,1,6),_MvpnSpmsiCmcastSourcePrefixLen_Type())
mvpnSpmsiCmcastSourcePrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnSpmsiCmcastSourcePrefixLen.setStatus(_B)
_MvpnSpmsiPmsiPointer_Type=RowPointer
_MvpnSpmsiPmsiPointer_Object=MibTableColumn
mvpnSpmsiPmsiPointer=_MvpnSpmsiPmsiPointer_Object((1,3,6,1,2,1,243,1,5,1,7),_MvpnSpmsiPmsiPointer_Type())
mvpnSpmsiPmsiPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnSpmsiPmsiPointer.setStatus(_B)
_MvpnAdvtStatsTable_Object=MibTable
mvpnAdvtStatsTable=_MvpnAdvtStatsTable_Object((1,3,6,1,2,1,243,1,6))
if mibBuilder.loadTexts:mvpnAdvtStatsTable.setStatus(_B)
_MvpnAdvtStatsEntry_Object=MibTableRow
mvpnAdvtStatsEntry=_MvpnAdvtStatsEntry_Object((1,3,6,1,2,1,243,1,6,1))
mvpnAdvtStatsEntry.setIndexNames((0,_H,_I),(0,_A,_h),(0,_A,_i),(0,_A,_j))
if mibBuilder.loadTexts:mvpnAdvtStatsEntry.setStatus(_B)
class _MvpnAdvtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('intraAsIpmsi',0),('interAsIpmsi',1),('sPmsi',2)))
_MvpnAdvtType_Type.__name__=_E
_MvpnAdvtType_Object=MibTableColumn
mvpnAdvtType=_MvpnAdvtType_Object((1,3,6,1,2,1,243,1,6,1,1),_MvpnAdvtType_Type())
mvpnAdvtType.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnAdvtType.setStatus(_B)
_MvpnAdvtPeerAddrType_Type=InetAddressType
_MvpnAdvtPeerAddrType_Object=MibTableColumn
mvpnAdvtPeerAddrType=_MvpnAdvtPeerAddrType_Object((1,3,6,1,2,1,243,1,6,1,2),_MvpnAdvtPeerAddrType_Type())
mvpnAdvtPeerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnAdvtPeerAddrType.setStatus(_B)
_MvpnAdvtPeerAddr_Type=InetAddress
_MvpnAdvtPeerAddr_Object=MibTableColumn
mvpnAdvtPeerAddr=_MvpnAdvtPeerAddr_Object((1,3,6,1,2,1,243,1,6,1,3),_MvpnAdvtPeerAddr_Type())
mvpnAdvtPeerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnAdvtPeerAddr.setStatus(_B)
_MvpnAdvtSent_Type=Counter32
_MvpnAdvtSent_Object=MibTableColumn
mvpnAdvtSent=_MvpnAdvtSent_Object((1,3,6,1,2,1,243,1,6,1,4),_MvpnAdvtSent_Type())
mvpnAdvtSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnAdvtSent.setStatus(_B)
_MvpnAdvtReceived_Type=Counter32
_MvpnAdvtReceived_Object=MibTableColumn
mvpnAdvtReceived=_MvpnAdvtReceived_Object((1,3,6,1,2,1,243,1,6,1,5),_MvpnAdvtReceived_Type())
mvpnAdvtReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnAdvtReceived.setStatus(_B)
_MvpnAdvtReceivedError_Type=Counter32
_MvpnAdvtReceivedError_Object=MibTableColumn
mvpnAdvtReceivedError=_MvpnAdvtReceivedError_Object((1,3,6,1,2,1,243,1,6,1,6),_MvpnAdvtReceivedError_Type())
mvpnAdvtReceivedError.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnAdvtReceivedError.setStatus(_B)
_MvpnAdvtReceivedMalformedTunnelType_Type=Counter32
_MvpnAdvtReceivedMalformedTunnelType_Object=MibTableColumn
mvpnAdvtReceivedMalformedTunnelType=_MvpnAdvtReceivedMalformedTunnelType_Object((1,3,6,1,2,1,243,1,6,1,7),_MvpnAdvtReceivedMalformedTunnelType_Type())
mvpnAdvtReceivedMalformedTunnelType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnAdvtReceivedMalformedTunnelType.setStatus(_B)
_MvpnAdvtReceivedMalformedTunnelId_Type=Counter32
_MvpnAdvtReceivedMalformedTunnelId_Object=MibTableColumn
mvpnAdvtReceivedMalformedTunnelId=_MvpnAdvtReceivedMalformedTunnelId_Object((1,3,6,1,2,1,243,1,6,1,8),_MvpnAdvtReceivedMalformedTunnelId_Type())
mvpnAdvtReceivedMalformedTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnAdvtReceivedMalformedTunnelId.setStatus(_B)
_MvpnAdvtLastSentTime_Type=DateAndTime
_MvpnAdvtLastSentTime_Object=MibTableColumn
mvpnAdvtLastSentTime=_MvpnAdvtLastSentTime_Object((1,3,6,1,2,1,243,1,6,1,9),_MvpnAdvtLastSentTime_Type())
mvpnAdvtLastSentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnAdvtLastSentTime.setStatus(_B)
_MvpnAdvtLastReceivedTime_Type=DateAndTime
_MvpnAdvtLastReceivedTime_Object=MibTableColumn
mvpnAdvtLastReceivedTime=_MvpnAdvtLastReceivedTime_Object((1,3,6,1,2,1,243,1,6,1,10),_MvpnAdvtLastReceivedTime_Type())
mvpnAdvtLastReceivedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnAdvtLastReceivedTime.setStatus(_B)
_MvpnAdvtCounterDiscontinuityTime_Type=TimeStamp
_MvpnAdvtCounterDiscontinuityTime_Object=MibTableColumn
mvpnAdvtCounterDiscontinuityTime=_MvpnAdvtCounterDiscontinuityTime_Object((1,3,6,1,2,1,243,1,6,1,11),_MvpnAdvtCounterDiscontinuityTime_Type())
mvpnAdvtCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnAdvtCounterDiscontinuityTime.setStatus(_B)
_MvpnMrouteTable_Object=MibTable
mvpnMrouteTable=_MvpnMrouteTable_Object((1,3,6,1,2,1,243,1,7))
if mibBuilder.loadTexts:mvpnMrouteTable.setStatus(_B)
_MvpnMrouteEntry_Object=MibTableRow
mvpnMrouteEntry=_MvpnMrouteEntry_Object((1,3,6,1,2,1,243,1,7,1))
mvpnMrouteEntry.setIndexNames((0,_H,_I),(0,_A,_k),(0,_A,_l),(0,_A,_m),(0,_A,_n),(0,_A,_o),(0,_A,_p))
if mibBuilder.loadTexts:mvpnMrouteEntry.setStatus(_B)
_MvpnMrouteCmcastGroupAddrType_Type=InetAddressType
_MvpnMrouteCmcastGroupAddrType_Object=MibTableColumn
mvpnMrouteCmcastGroupAddrType=_MvpnMrouteCmcastGroupAddrType_Object((1,3,6,1,2,1,243,1,7,1,1),_MvpnMrouteCmcastGroupAddrType_Type())
mvpnMrouteCmcastGroupAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteCmcastGroupAddrType.setStatus(_B)
_MvpnMrouteCmcastGroupAddr_Type=InetAddress
_MvpnMrouteCmcastGroupAddr_Object=MibTableColumn
mvpnMrouteCmcastGroupAddr=_MvpnMrouteCmcastGroupAddr_Object((1,3,6,1,2,1,243,1,7,1,2),_MvpnMrouteCmcastGroupAddr_Type())
mvpnMrouteCmcastGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteCmcastGroupAddr.setStatus(_B)
_MvpnMrouteCmcastGroupPrefixLength_Type=InetAddressPrefixLength
_MvpnMrouteCmcastGroupPrefixLength_Object=MibTableColumn
mvpnMrouteCmcastGroupPrefixLength=_MvpnMrouteCmcastGroupPrefixLength_Object((1,3,6,1,2,1,243,1,7,1,3),_MvpnMrouteCmcastGroupPrefixLength_Type())
mvpnMrouteCmcastGroupPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteCmcastGroupPrefixLength.setStatus(_B)
_MvpnMrouteCmcastSourceAddrType_Type=InetAddressType
_MvpnMrouteCmcastSourceAddrType_Object=MibTableColumn
mvpnMrouteCmcastSourceAddrType=_MvpnMrouteCmcastSourceAddrType_Object((1,3,6,1,2,1,243,1,7,1,4),_MvpnMrouteCmcastSourceAddrType_Type())
mvpnMrouteCmcastSourceAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteCmcastSourceAddrType.setStatus(_B)
_MvpnMrouteCmcastSourceAddrs_Type=InetAddress
_MvpnMrouteCmcastSourceAddrs_Object=MibTableColumn
mvpnMrouteCmcastSourceAddrs=_MvpnMrouteCmcastSourceAddrs_Object((1,3,6,1,2,1,243,1,7,1,5),_MvpnMrouteCmcastSourceAddrs_Type())
mvpnMrouteCmcastSourceAddrs.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteCmcastSourceAddrs.setStatus(_B)
_MvpnMrouteCmcastSourcePrefixLength_Type=InetAddressPrefixLength
_MvpnMrouteCmcastSourcePrefixLength_Object=MibTableColumn
mvpnMrouteCmcastSourcePrefixLength=_MvpnMrouteCmcastSourcePrefixLength_Object((1,3,6,1,2,1,243,1,7,1,6),_MvpnMrouteCmcastSourcePrefixLength_Type())
mvpnMrouteCmcastSourcePrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteCmcastSourcePrefixLength.setStatus(_B)
_MvpnMrouteUpstreamNeighborAddrType_Type=InetAddressType
_MvpnMrouteUpstreamNeighborAddrType_Object=MibTableColumn
mvpnMrouteUpstreamNeighborAddrType=_MvpnMrouteUpstreamNeighborAddrType_Object((1,3,6,1,2,1,243,1,7,1,7),_MvpnMrouteUpstreamNeighborAddrType_Type())
mvpnMrouteUpstreamNeighborAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteUpstreamNeighborAddrType.setStatus(_B)
_MvpnMrouteUpstreamNeighborAddr_Type=InetAddress
_MvpnMrouteUpstreamNeighborAddr_Object=MibTableColumn
mvpnMrouteUpstreamNeighborAddr=_MvpnMrouteUpstreamNeighborAddr_Object((1,3,6,1,2,1,243,1,7,1,8),_MvpnMrouteUpstreamNeighborAddr_Type())
mvpnMrouteUpstreamNeighborAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteUpstreamNeighborAddr.setStatus(_B)
_MvpnMrouteInIfIndex_Type=InterfaceIndexOrZero
_MvpnMrouteInIfIndex_Object=MibTableColumn
mvpnMrouteInIfIndex=_MvpnMrouteInIfIndex_Object((1,3,6,1,2,1,243,1,7,1,9),_MvpnMrouteInIfIndex_Type())
mvpnMrouteInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteInIfIndex.setStatus(_B)
_MvpnMrouteExpiryTime_Type=TimeTicks
_MvpnMrouteExpiryTime_Object=MibTableColumn
mvpnMrouteExpiryTime=_MvpnMrouteExpiryTime_Object((1,3,6,1,2,1,243,1,7,1,10),_MvpnMrouteExpiryTime_Type())
mvpnMrouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteExpiryTime.setStatus(_B)
_MvpnMrouteProtocol_Type=IANAipMRouteProtocol
_MvpnMrouteProtocol_Object=MibTableColumn
mvpnMrouteProtocol=_MvpnMrouteProtocol_Object((1,3,6,1,2,1,243,1,7,1,11),_MvpnMrouteProtocol_Type())
mvpnMrouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteProtocol.setStatus(_B)
_MvpnMrouteRtProtocol_Type=IANAipRouteProtocol
_MvpnMrouteRtProtocol_Object=MibTableColumn
mvpnMrouteRtProtocol=_MvpnMrouteRtProtocol_Object((1,3,6,1,2,1,243,1,7,1,12),_MvpnMrouteRtProtocol_Type())
mvpnMrouteRtProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteRtProtocol.setStatus(_B)
_MvpnMrouteRtAddrType_Type=InetAddressType
_MvpnMrouteRtAddrType_Object=MibTableColumn
mvpnMrouteRtAddrType=_MvpnMrouteRtAddrType_Object((1,3,6,1,2,1,243,1,7,1,13),_MvpnMrouteRtAddrType_Type())
mvpnMrouteRtAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteRtAddrType.setStatus(_B)
_MvpnMrouteRtAddr_Type=InetAddress
_MvpnMrouteRtAddr_Object=MibTableColumn
mvpnMrouteRtAddr=_MvpnMrouteRtAddr_Object((1,3,6,1,2,1,243,1,7,1,14),_MvpnMrouteRtAddr_Type())
mvpnMrouteRtAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteRtAddr.setStatus(_B)
_MvpnMrouteRtPrefixLength_Type=InetAddressPrefixLength
_MvpnMrouteRtPrefixLength_Object=MibTableColumn
mvpnMrouteRtPrefixLength=_MvpnMrouteRtPrefixLength_Object((1,3,6,1,2,1,243,1,7,1,15),_MvpnMrouteRtPrefixLength_Type())
mvpnMrouteRtPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteRtPrefixLength.setStatus(_B)
class _MvpnMrouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_MvpnMrouteRtType_Type.__name__=_E
_MvpnMrouteRtType_Object=MibTableColumn
mvpnMrouteRtType=_MvpnMrouteRtType_Object((1,3,6,1,2,1,243,1,7,1,16),_MvpnMrouteRtType_Type())
mvpnMrouteRtType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteRtType.setStatus(_B)
_MvpnMrouteOctets_Type=Counter64
_MvpnMrouteOctets_Object=MibTableColumn
mvpnMrouteOctets=_MvpnMrouteOctets_Object((1,3,6,1,2,1,243,1,7,1,17),_MvpnMrouteOctets_Type())
mvpnMrouteOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteOctets.setStatus(_B)
_MvpnMroutePkts_Type=Counter64
_MvpnMroutePkts_Object=MibTableColumn
mvpnMroutePkts=_MvpnMroutePkts_Object((1,3,6,1,2,1,243,1,7,1,18),_MvpnMroutePkts_Type())
mvpnMroutePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMroutePkts.setStatus(_B)
_MvpnMrouteTtlDroppedOctets_Type=Counter64
_MvpnMrouteTtlDroppedOctets_Object=MibTableColumn
mvpnMrouteTtlDroppedOctets=_MvpnMrouteTtlDroppedOctets_Object((1,3,6,1,2,1,243,1,7,1,19),_MvpnMrouteTtlDroppedOctets_Type())
mvpnMrouteTtlDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteTtlDroppedOctets.setStatus(_B)
_MvpnMrouteTtlDroppedPackets_Type=Counter64
_MvpnMrouteTtlDroppedPackets_Object=MibTableColumn
mvpnMrouteTtlDroppedPackets=_MvpnMrouteTtlDroppedPackets_Object((1,3,6,1,2,1,243,1,7,1,20),_MvpnMrouteTtlDroppedPackets_Type())
mvpnMrouteTtlDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteTtlDroppedPackets.setStatus(_B)
_MvpnMrouteDroppedInOctets_Type=Counter64
_MvpnMrouteDroppedInOctets_Object=MibTableColumn
mvpnMrouteDroppedInOctets=_MvpnMrouteDroppedInOctets_Object((1,3,6,1,2,1,243,1,7,1,21),_MvpnMrouteDroppedInOctets_Type())
mvpnMrouteDroppedInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteDroppedInOctets.setStatus(_B)
_MvpnMrouteDroppedInPackets_Type=Counter64
_MvpnMrouteDroppedInPackets_Object=MibTableColumn
mvpnMrouteDroppedInPackets=_MvpnMrouteDroppedInPackets_Object((1,3,6,1,2,1,243,1,7,1,22),_MvpnMrouteDroppedInPackets_Type())
mvpnMrouteDroppedInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteDroppedInPackets.setStatus(_B)
_MvpnMroutePmsiPointer_Type=RowPointer
_MvpnMroutePmsiPointer_Object=MibTableColumn
mvpnMroutePmsiPointer=_MvpnMroutePmsiPointer_Object((1,3,6,1,2,1,243,1,7,1,23),_MvpnMroutePmsiPointer_Type())
mvpnMroutePmsiPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMroutePmsiPointer.setStatus(_B)
_MvpnMrouteNumberOfLocalReplication_Type=Unsigned32
_MvpnMrouteNumberOfLocalReplication_Object=MibTableColumn
mvpnMrouteNumberOfLocalReplication=_MvpnMrouteNumberOfLocalReplication_Object((1,3,6,1,2,1,243,1,7,1,24),_MvpnMrouteNumberOfLocalReplication_Type())
mvpnMrouteNumberOfLocalReplication.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteNumberOfLocalReplication.setStatus(_B)
_MvpnMrouteNumberOfRemoteReplication_Type=Unsigned32
_MvpnMrouteNumberOfRemoteReplication_Object=MibTableColumn
mvpnMrouteNumberOfRemoteReplication=_MvpnMrouteNumberOfRemoteReplication_Object((1,3,6,1,2,1,243,1,7,1,25),_MvpnMrouteNumberOfRemoteReplication_Type())
mvpnMrouteNumberOfRemoteReplication.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteNumberOfRemoteReplication.setStatus(_B)
_MvpnMrouteCounterDiscontinuityTime_Type=TimeStamp
_MvpnMrouteCounterDiscontinuityTime_Object=MibTableColumn
mvpnMrouteCounterDiscontinuityTime=_MvpnMrouteCounterDiscontinuityTime_Object((1,3,6,1,2,1,243,1,7,1,26),_MvpnMrouteCounterDiscontinuityTime_Type())
mvpnMrouteCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteCounterDiscontinuityTime.setStatus(_B)
_MvpnMrouteNextHopTable_Object=MibTable
mvpnMrouteNextHopTable=_MvpnMrouteNextHopTable_Object((1,3,6,1,2,1,243,1,8))
if mibBuilder.loadTexts:mvpnMrouteNextHopTable.setStatus(_B)
_MvpnMrouteNextHopEntry_Object=MibTableRow
mvpnMrouteNextHopEntry=_MvpnMrouteNextHopEntry_Object((1,3,6,1,2,1,243,1,8,1))
mvpnMrouteNextHopEntry.setIndexNames((0,_H,_I),(0,_A,_q),(0,_A,_r),(0,_A,_s),(0,_A,_t),(0,_A,_u),(0,_A,_v),(0,_A,_w),(0,_A,_x),(0,_A,_y))
if mibBuilder.loadTexts:mvpnMrouteNextHopEntry.setStatus(_B)
_MvpnMrouteNextHopGroupAddrType_Type=InetAddressType
_MvpnMrouteNextHopGroupAddrType_Object=MibTableColumn
mvpnMrouteNextHopGroupAddrType=_MvpnMrouteNextHopGroupAddrType_Object((1,3,6,1,2,1,243,1,8,1,1),_MvpnMrouteNextHopGroupAddrType_Type())
mvpnMrouteNextHopGroupAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteNextHopGroupAddrType.setStatus(_B)
_MvpnMrouteNextHopGroupAddr_Type=InetAddress
_MvpnMrouteNextHopGroupAddr_Object=MibTableColumn
mvpnMrouteNextHopGroupAddr=_MvpnMrouteNextHopGroupAddr_Object((1,3,6,1,2,1,243,1,8,1,2),_MvpnMrouteNextHopGroupAddr_Type())
mvpnMrouteNextHopGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteNextHopGroupAddr.setStatus(_B)
_MvpnMrouteNextHopGroupPrefixLength_Type=InetAddressPrefixLength
_MvpnMrouteNextHopGroupPrefixLength_Object=MibTableColumn
mvpnMrouteNextHopGroupPrefixLength=_MvpnMrouteNextHopGroupPrefixLength_Object((1,3,6,1,2,1,243,1,8,1,3),_MvpnMrouteNextHopGroupPrefixLength_Type())
mvpnMrouteNextHopGroupPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteNextHopGroupPrefixLength.setStatus(_B)
_MvpnMrouteNextHopSourceAddrType_Type=InetAddressType
_MvpnMrouteNextHopSourceAddrType_Object=MibTableColumn
mvpnMrouteNextHopSourceAddrType=_MvpnMrouteNextHopSourceAddrType_Object((1,3,6,1,2,1,243,1,8,1,4),_MvpnMrouteNextHopSourceAddrType_Type())
mvpnMrouteNextHopSourceAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteNextHopSourceAddrType.setStatus(_B)
_MvpnMrouteNextHopSourceAddrs_Type=InetAddress
_MvpnMrouteNextHopSourceAddrs_Object=MibTableColumn
mvpnMrouteNextHopSourceAddrs=_MvpnMrouteNextHopSourceAddrs_Object((1,3,6,1,2,1,243,1,8,1,5),_MvpnMrouteNextHopSourceAddrs_Type())
mvpnMrouteNextHopSourceAddrs.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteNextHopSourceAddrs.setStatus(_B)
_MvpnMrouteNextHopSourcePrefixLength_Type=InetAddressPrefixLength
_MvpnMrouteNextHopSourcePrefixLength_Object=MibTableColumn
mvpnMrouteNextHopSourcePrefixLength=_MvpnMrouteNextHopSourcePrefixLength_Object((1,3,6,1,2,1,243,1,8,1,6),_MvpnMrouteNextHopSourcePrefixLength_Type())
mvpnMrouteNextHopSourcePrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteNextHopSourcePrefixLength.setStatus(_B)
_MvpnMrouteNextHopIfIndex_Type=InterfaceIndex
_MvpnMrouteNextHopIfIndex_Object=MibTableColumn
mvpnMrouteNextHopIfIndex=_MvpnMrouteNextHopIfIndex_Object((1,3,6,1,2,1,243,1,8,1,7),_MvpnMrouteNextHopIfIndex_Type())
mvpnMrouteNextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteNextHopIfIndex.setStatus(_B)
_MvpnMrouteNextHopAddrType_Type=InetAddressType
_MvpnMrouteNextHopAddrType_Object=MibTableColumn
mvpnMrouteNextHopAddrType=_MvpnMrouteNextHopAddrType_Object((1,3,6,1,2,1,243,1,8,1,8),_MvpnMrouteNextHopAddrType_Type())
mvpnMrouteNextHopAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteNextHopAddrType.setStatus(_B)
_MvpnMrouteNextHopAddr_Type=InetAddress
_MvpnMrouteNextHopAddr_Object=MibTableColumn
mvpnMrouteNextHopAddr=_MvpnMrouteNextHopAddr_Object((1,3,6,1,2,1,243,1,8,1,9),_MvpnMrouteNextHopAddr_Type())
mvpnMrouteNextHopAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mvpnMrouteNextHopAddr.setStatus(_B)
class _MvpnMrouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),('forwarding',2)))
_MvpnMrouteNextHopState_Type.__name__=_E
_MvpnMrouteNextHopState_Object=MibTableColumn
mvpnMrouteNextHopState=_MvpnMrouteNextHopState_Object((1,3,6,1,2,1,243,1,8,1,10),_MvpnMrouteNextHopState_Type())
mvpnMrouteNextHopState.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteNextHopState.setStatus(_B)
_MvpnMrouteNextHopExpiryTime_Type=TimeTicks
_MvpnMrouteNextHopExpiryTime_Object=MibTableColumn
mvpnMrouteNextHopExpiryTime=_MvpnMrouteNextHopExpiryTime_Object((1,3,6,1,2,1,243,1,8,1,11),_MvpnMrouteNextHopExpiryTime_Type())
mvpnMrouteNextHopExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteNextHopExpiryTime.setStatus(_B)
class _MvpnMrouteNextHopClosestMemberHops_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_MvpnMrouteNextHopClosestMemberHops_Type.__name__=_F
_MvpnMrouteNextHopClosestMemberHops_Object=MibTableColumn
mvpnMrouteNextHopClosestMemberHops=_MvpnMrouteNextHopClosestMemberHops_Object((1,3,6,1,2,1,243,1,8,1,12),_MvpnMrouteNextHopClosestMemberHops_Type())
mvpnMrouteNextHopClosestMemberHops.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteNextHopClosestMemberHops.setStatus(_B)
_MvpnMrouteNextHopProtocol_Type=IANAipMRouteProtocol
_MvpnMrouteNextHopProtocol_Object=MibTableColumn
mvpnMrouteNextHopProtocol=_MvpnMrouteNextHopProtocol_Object((1,3,6,1,2,1,243,1,8,1,13),_MvpnMrouteNextHopProtocol_Type())
mvpnMrouteNextHopProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteNextHopProtocol.setStatus(_B)
_MvpnMrouteNextHopOctets_Type=Counter64
_MvpnMrouteNextHopOctets_Object=MibTableColumn
mvpnMrouteNextHopOctets=_MvpnMrouteNextHopOctets_Object((1,3,6,1,2,1,243,1,8,1,14),_MvpnMrouteNextHopOctets_Type())
mvpnMrouteNextHopOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteNextHopOctets.setStatus(_B)
_MvpnMrouteNextHopPkts_Type=Counter64
_MvpnMrouteNextHopPkts_Object=MibTableColumn
mvpnMrouteNextHopPkts=_MvpnMrouteNextHopPkts_Object((1,3,6,1,2,1,243,1,8,1,15),_MvpnMrouteNextHopPkts_Type())
mvpnMrouteNextHopPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteNextHopPkts.setStatus(_B)
_MvpnMrouteNextHopCounterDiscontinuityTime_Type=TimeStamp
_MvpnMrouteNextHopCounterDiscontinuityTime_Object=MibTableColumn
mvpnMrouteNextHopCounterDiscontinuityTime=_MvpnMrouteNextHopCounterDiscontinuityTime_Object((1,3,6,1,2,1,243,1,8,1,16),_MvpnMrouteNextHopCounterDiscontinuityTime_Type())
mvpnMrouteNextHopCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvpnMrouteNextHopCounterDiscontinuityTime.setStatus(_B)
_MvpnConformance_ObjectIdentity=ObjectIdentity
mvpnConformance=_MvpnConformance_ObjectIdentity((1,3,6,1,2,1,243,2))
_MvpnGroups_ObjectIdentity=ObjectIdentity
mvpnGroups=_MvpnGroups_ObjectIdentity((1,3,6,1,2,1,243,2,1))
_MvpnCompliances_ObjectIdentity=ObjectIdentity
mvpnCompliances=_MvpnCompliances_ObjectIdentity((1,3,6,1,2,1,243,2,2))
mvpnScalarGroup=ObjectGroup((1,3,6,1,2,1,243,2,1,1))
mvpnScalarGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:mvpnScalarGroup.setStatus(_B)
mvpnBgpScalarGroup=ObjectGroup((1,3,6,1,2,1,243,2,1,2))
mvpnBgpScalarGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:mvpnBgpScalarGroup.setStatus(_B)
mvpnGenericGroup=ObjectGroup((1,3,6,1,2,1,243,2,1,3))
mvpnGenericGroup.setObjects(*((_A,_L),(_A,_M),(_A,_J),(_A,_N),(_A,_AA),(_A,_AB),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:mvpnGenericGroup.setStatus(_B)
mvpnBgpGroup=ObjectGroup((1,3,6,1,2,1,243,2,1,4))
mvpnBgpGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:mvpnBgpGroup.setStatus(_B)
mvpnPmsiGroup=ObjectGroup((1,3,6,1,2,1,243,2,1,5))
mvpnPmsiGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:mvpnPmsiGroup.setStatus(_B)
mvpnAdvtStatsGroup=ObjectGroup((1,3,6,1,2,1,243,2,1,6))
mvpnAdvtStatsGroup.setObjects(*((_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:mvpnAdvtStatsGroup.setStatus(_B)
mvpnMrouteGroup=ObjectGroup((1,3,6,1,2,1,243,2,1,7))
mvpnMrouteGroup.setObjects(*((_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:mvpnMrouteGroup.setStatus(_B)
mvpnMrouteNextHopGroup=ObjectGroup((1,3,6,1,2,1,243,2,1,8))
mvpnMrouteNextHopGroup.setObjects(*((_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:mvpnMrouteNextHopGroup.setStatus(_B)
mvpnMvrfActionTaken=NotificationType((1,3,6,1,2,1,243,0,1))
mvpnMvrfActionTaken.setObjects(*((_A,_J),(_A,_L),(_A,_M),(_A,_J),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:mvpnMvrfActionTaken.setStatus(_B)
mvpnNotificationGroup=NotificationGroup((1,3,6,1,2,1,243,2,1,9))
mvpnNotificationGroup.setObjects((_A,_A_))
if mibBuilder.loadTexts:mvpnNotificationGroup.setStatus(_B)
mvpnModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,243,2,2,1))
mvpnModuleFullCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_K),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:mvpnModuleFullCompliance.setStatus(_B)
mvpnModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,243,2,2,2))
mvpnModuleReadOnlyCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_K),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:mvpnModuleReadOnlyCompliance.setStatus(_B)
mvpnModuleAdvtStatsCompliance=ModuleCompliance((1,3,6,1,2,1,243,2,2,3))
mvpnModuleAdvtStatsCompliance.setObjects((_A,_K))
if mibBuilder.loadTexts:mvpnModuleAdvtStatsCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'mvpnMIB':mvpnMIB,'mvpnNotifications':mvpnNotifications,_A_:mvpnMvrfActionTaken,'mvpnObjects':mvpnObjects,'mvpnScalars':mvpnScalars,_z:mvpnMvrfs,_A0:mvpnV4Mvrfs,_A1:mvpnV6Mvrfs,_A5:mvpnMldpMvrfs,_A2:mvpnPimV4Mvrfs,_A3:mvpnPimV6Mvrfs,_A6:mvpnBgpV4Mvrfs,_A7:mvpnBgpV6Mvrfs,_A4:mvpnSPTunnelLimit,_A8:mvpnBgpCmcastRouteWithdrawalTimer,_A9:mvpnBgpSrcSharedTreeJoinTimer,'mvpnGenericTable':mvpnGenericTable,'mvpnGenericEntry':mvpnGenericEntry,_L:mvpnGenMvrfLastAction,_M:mvpnGenMvrfLastActionTime,_J:mvpnGenMvrfCreationTime,_N:mvpnGenCmcastRouteProtocol,_AA:mvpnGenIpmsiInfo,_AB:mvpnGenInterAsPmsiInfo,_O:mvpnGenUmhSelection,_P:mvpnGenCustomerSiteType,'mvpnBgpTable':mvpnBgpTable,'mvpnBgpEntry':mvpnBgpEntry,_AC:mvpnBgpMode,_AD:mvpnBgpVrfRouteImportExtendedCommunity,_AE:mvpnBgpSrcASExtendedCommunity,_AF:mvpnBgpMsgRateLimit,_AG:mvpnBgpMaxSpmsiAdRoutes,_AH:mvpnBgpMaxSpmsiAdRouteFreq,_AI:mvpnBgpMaxSrcActiveAdRoutes,_AJ:mvpnBgpMaxSrcActiveAdRouteFreq,'mvpnPmsiTable':mvpnPmsiTable,'mvpnPmsiEntry':mvpnPmsiEntry,_a:mvpnPmsiTunnelIfIndex,_AK:mvpnPmsiRD,_AL:mvpnPmsiTunnelType,_AM:mvpnPmsiTunnelAttribute,_AN:mvpnPmsiTunnelPimGroupAddrType,_AO:mvpnPmsiTunnelPimGroupAddr,_AP:mvpnPmsiEncapsulationType,'mvpnSpmsiTable':mvpnSpmsiTable,'mvpnSpmsiEntry':mvpnSpmsiEntry,_b:mvpnSpmsiCmcastGroupAddrType,_c:mvpnSpmsiCmcastGroupAddr,_d:mvpnSpmsiCmcastGroupPrefixLen,_e:mvpnSpmsiCmcastSourceAddrType,_f:mvpnSpmsiCmcastSourceAddr,_g:mvpnSpmsiCmcastSourcePrefixLen,_AQ:mvpnSpmsiPmsiPointer,'mvpnAdvtStatsTable':mvpnAdvtStatsTable,'mvpnAdvtStatsEntry':mvpnAdvtStatsEntry,_h:mvpnAdvtType,_i:mvpnAdvtPeerAddrType,_j:mvpnAdvtPeerAddr,_AR:mvpnAdvtSent,_AS:mvpnAdvtReceived,_AT:mvpnAdvtReceivedError,_AU:mvpnAdvtReceivedMalformedTunnelType,_AV:mvpnAdvtReceivedMalformedTunnelId,_AW:mvpnAdvtLastSentTime,_AX:mvpnAdvtLastReceivedTime,_AY:mvpnAdvtCounterDiscontinuityTime,'mvpnMrouteTable':mvpnMrouteTable,'mvpnMrouteEntry':mvpnMrouteEntry,_k:mvpnMrouteCmcastGroupAddrType,_l:mvpnMrouteCmcastGroupAddr,_m:mvpnMrouteCmcastGroupPrefixLength,_n:mvpnMrouteCmcastSourceAddrType,_o:mvpnMrouteCmcastSourceAddrs,_p:mvpnMrouteCmcastSourcePrefixLength,_AZ:mvpnMrouteUpstreamNeighborAddrType,_Aa:mvpnMrouteUpstreamNeighborAddr,_Ab:mvpnMrouteInIfIndex,_Ac:mvpnMrouteExpiryTime,_Ad:mvpnMrouteProtocol,_Ae:mvpnMrouteRtProtocol,_Af:mvpnMrouteRtAddrType,_Ag:mvpnMrouteRtAddr,_Ah:mvpnMrouteRtPrefixLength,_Ai:mvpnMrouteRtType,_Aj:mvpnMrouteOctets,_Ak:mvpnMroutePkts,_Al:mvpnMrouteTtlDroppedOctets,_Am:mvpnMrouteTtlDroppedPackets,_An:mvpnMrouteDroppedInOctets,_Ao:mvpnMrouteDroppedInPackets,_Ap:mvpnMroutePmsiPointer,_Aq:mvpnMrouteNumberOfLocalReplication,_Ar:mvpnMrouteNumberOfRemoteReplication,_As:mvpnMrouteCounterDiscontinuityTime,'mvpnMrouteNextHopTable':mvpnMrouteNextHopTable,'mvpnMrouteNextHopEntry':mvpnMrouteNextHopEntry,_q:mvpnMrouteNextHopGroupAddrType,_r:mvpnMrouteNextHopGroupAddr,_s:mvpnMrouteNextHopGroupPrefixLength,_t:mvpnMrouteNextHopSourceAddrType,_u:mvpnMrouteNextHopSourceAddrs,_v:mvpnMrouteNextHopSourcePrefixLength,_w:mvpnMrouteNextHopIfIndex,_x:mvpnMrouteNextHopAddrType,_y:mvpnMrouteNextHopAddr,_At:mvpnMrouteNextHopState,_Au:mvpnMrouteNextHopExpiryTime,_Av:mvpnMrouteNextHopClosestMemberHops,_Aw:mvpnMrouteNextHopProtocol,_Ax:mvpnMrouteNextHopOctets,_Ay:mvpnMrouteNextHopPkts,_Az:mvpnMrouteNextHopCounterDiscontinuityTime,'mvpnConformance':mvpnConformance,'mvpnGroups':mvpnGroups,_Q:mvpnScalarGroup,_W:mvpnBgpScalarGroup,_R:mvpnGenericGroup,_X:mvpnBgpGroup,_S:mvpnPmsiGroup,_K:mvpnAdvtStatsGroup,_T:mvpnMrouteGroup,_U:mvpnMrouteNextHopGroup,_V:mvpnNotificationGroup,'mvpnCompliances':mvpnCompliances,'mvpnModuleFullCompliance':mvpnModuleFullCompliance,'mvpnModuleReadOnlyCompliance':mvpnModuleReadOnlyCompliance,'mvpnModuleAdvtStatsCompliance':mvpnModuleAdvtStatsCompliance})