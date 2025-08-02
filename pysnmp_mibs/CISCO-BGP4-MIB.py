_BI='ciscoBgp4Peer2NotificationsGroup'
_BH='ciscoBgp4Peer2Group'
_BG='ciscoBgp4GlobalGroup'
_BF='ciscoBgp4NotificationsGroup'
_BE='ciscoBgp4PeerGroup'
_BD='cbgpPeer2PrefixThresholdClear'
_BC='cbgpPeer2PrefixThresholdExceeded'
_BB='cbgpPeer2BackwardTransition'
_BA='cbgpPeer2FsmStateChange'
_B9='cbgpPeer2BackwardTransNotification'
_B8='cbgpPeer2EstablishedNotification'
_B7='cbgpPrefixThresholdClear'
_B6='cbgpPrefixThresholdExceeded'
_B5='cbgpBackwardTransition'
_B4='cbgpLocalAs'
_B3='cbgpNotifsEnable'
_B2='cbgpPeer2WithdrawnPrefixes'
_B1='cbgpPeer2SuppressedPrefixes'
_B0='cbgpPeer2AdvertisedPrefixes'
_A_='cbgpPeer2DeniedPrefixes'
_Az='cbgpPeer2AcceptedPrefixes'
_Ay='cbgpPeer2AddrFamilyName'
_Ax='cbgpPeer2CapValue'
_Aw='cbgpPeer2InUpdateElapsedTime'
_Av='cbgpPeer2MinRouteAdvertisementInterval'
_Au='cbgpPeer2MinASOriginationInterval'
_At='cbgpPeer2KeepAliveConfigured'
_As='cbgpPeer2HoldTimeConfigured'
_Ar='cbgpPeer2KeepAlive'
_Aq='cbgpPeer2HoldTime'
_Ap='cbgpPeer2ConnectRetryInterval'
_Ao='cbgpPeer2FsmEstablishedTime'
_An='cbgpPeer2FsmEstablishedTransitions'
_Am='cbgpPeer2OutTotalMessages'
_Al='cbgpPeer2InTotalMessages'
_Ak='cbgpPeer2OutUpdates'
_Aj='cbgpPeer2InUpdates'
_Ai='cbgpPeer2RemoteIdentifier'
_Ah='cbgpPeer2RemoteAs'
_Ag='cbgpPeer2RemotePort'
_Af='cbgpPeer2LocalIdentifier'
_Ae='cbgpPeer2LocalAs'
_Ad='cbgpPeer2LocalPort'
_Ac='cbgpPeer2LocalAddr'
_Ab='cbgpPeer2NegotiatedVersion'
_Aa='cbgpPeer2AdminStatus'
_AZ='cbgpPeerWithdrawnPrefixes'
_AY='cbgpPeerSuppressedPrefixes'
_AX='cbgpPeerAdvertisedPrefixes'
_AW='cbgpPeerDeniedPrefixes'
_AV='cbgpPeerAcceptedPrefixes'
_AU='cbgpPeerAddrFamilyName'
_AT='cbgpPeerCapValue'
_AS='cbgpPeerPrefixWithdrawn'
_AR='cbgpPeerPrefixSuppressed'
_AQ='cbgpPeerPrefixAdvertised'
_AP='cbgpPeerPrefixLimit'
_AO='cbgpPeerPrefixDenied'
_AN='cbgpPeerPrefixAccepted'
_AM='cbgpRouteUnknownAttr'
_AL='cbgpRouteBest'
_AK='cbgpRouteAggregatorAddr'
_AJ='cbgpRouteAggregatorAddrType'
_AI='cbgpRouteAggregatorAS'
_AH='cbgpRouteAtomicAggregate'
_AG='cbgpRouteLocalPref'
_AF='cbgpRouteLocalPrefPresent'
_AE='cbgpRouteMultiExitDisc'
_AD='cbgpRouteMedPresent'
_AC='cbgpRouteNextHop'
_AB='cbgpRouteASPathSegment'
_AA='cbgpRouteOrigin'
_A9='cbgpPeerEntry'
_A8='cbgpPeer3RemoteAddr'
_A7='cbgpPeer3Type'
_A6='cbgpPeer3VrfId'
_A5='cbgpPeer2CapIndex'
_A4='cbgpPeer2CapCode'
_A3='routeRefreshOld'
_A2='gracefulRestart'
_A1='routeRefresh'
_A0='multiProtocol'
_z='cbgpPeerCapIndex'
_y='cbgpPeerCapCode'
_x='cbgpRouteAddrPrefixLen'
_w='cbgpRouteAddrPrefix'
_v='cbgpRoutePeer'
_u='cbgpRoutePeerType'
_t='cbgpRouteSafi'
_s='cbgpRouteAfi'
_r='SnmpAdminString'
_q='ciscoBgp4NotificationsGroup1'
_p='ciscoBgp4PeerGroup1'
_o='cbgpFsmStateChange'
_n='cbgpPeer2PrefixClearThreshold'
_m='cbgpPeer2PrefixThreshold'
_l='cbgpPeerPrefixClearThreshold'
_k='cbgpPeerPrefixThreshold'
_j='cbgpPeer2AddrFamilySafi'
_i='cbgpPeer2AddrFamilyAfi'
_h='cbgpPeerAddrFamilySafi'
_g='cbgpPeerAddrFamilyAfi'
_f='none'
_e='bgpPeerState'
_d='bgpPeerLastError'
_c='cbgpPeer2PrefixAdminLimit'
_b='cbgpPeer2PrevState'
_a='cbgpPeer2LastErrorTxt'
_Z='cbgpPeerPrefixAdminLimit'
_Y='cbgpPeerLastErrorTxt'
_X='cbgpPeerPrevState'
_W='bgpPeerRemoteAddr'
_V='ciscoBgp4RouteGroup'
_U='cbgpPeer2RemoteAddr'
_T='cbgpPeer2Type'
_S='established'
_R='openconfirm'
_Q='opensent'
_P='active'
_O='connect'
_N='idle'
_M='cbgpPeer2LastError'
_L='cbgpPeer2State'
_K='OctetString'
_J='BGP4-MIB'
_I='deprecated'
_H='Unsigned32'
_G='not-accessible'
_F='seconds'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-BGP4-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bgpPeerEntry,bgpPeerLastError,bgpPeerRemoteAddr,bgpPeerState=mibBuilder.importSymbols(_J,'bgpPeerEntry',_d,_W,_e)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetAutonomousSystemNumber,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetAutonomousSystemNumber','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_r)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoBgp4MIB=ModuleIdentity((1,3,6,1,4,1,9,9,187))
if mibBuilder.loadTexts:ciscoBgp4MIB.setRevisions(('2020-05-06 00:00','2020-04-14 00:00','2010-09-30 00:00','2003-02-24 00:00','2002-12-19 00:00','2001-08-13 00:00'))
class CbgpSafi(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,70,128)));namedValues=NamedValues(*(('unicast',1),('multicast',2),('unicastAndMulticast',3),('evpn',70),('vpn',128)))
class CbgpNetworkAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CiscoBgp4NotifyPrefix_ObjectIdentity=ObjectIdentity
ciscoBgp4NotifyPrefix=_CiscoBgp4NotifyPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,187,0))
_CiscoBgp4MIBObjects_ObjectIdentity=ObjectIdentity
ciscoBgp4MIBObjects=_CiscoBgp4MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,187,1))
_CbgpRoute_ObjectIdentity=ObjectIdentity
cbgpRoute=_CbgpRoute_ObjectIdentity((1,3,6,1,4,1,9,9,187,1,1))
_CbgpRouteTable_Object=MibTable
cbgpRouteTable=_CbgpRouteTable_Object((1,3,6,1,4,1,9,9,187,1,1,1))
if mibBuilder.loadTexts:cbgpRouteTable.setStatus(_A)
_CbgpRouteEntry_Object=MibTableRow
cbgpRouteEntry=_CbgpRouteEntry_Object((1,3,6,1,4,1,9,9,187,1,1,1,1))
cbgpRouteEntry.setIndexNames((0,_B,_s),(0,_B,_t),(0,_B,_u),(0,_B,_v),(0,_B,_w),(0,_B,_x))
if mibBuilder.loadTexts:cbgpRouteEntry.setStatus(_A)
_CbgpRouteAfi_Type=InetAddressType
_CbgpRouteAfi_Object=MibTableColumn
cbgpRouteAfi=_CbgpRouteAfi_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,1),_CbgpRouteAfi_Type())
cbgpRouteAfi.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpRouteAfi.setStatus(_A)
_CbgpRouteSafi_Type=CbgpSafi
_CbgpRouteSafi_Object=MibTableColumn
cbgpRouteSafi=_CbgpRouteSafi_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,2),_CbgpRouteSafi_Type())
cbgpRouteSafi.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpRouteSafi.setStatus(_A)
_CbgpRoutePeerType_Type=InetAddressType
_CbgpRoutePeerType_Object=MibTableColumn
cbgpRoutePeerType=_CbgpRoutePeerType_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,3),_CbgpRoutePeerType_Type())
cbgpRoutePeerType.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpRoutePeerType.setStatus(_A)
_CbgpRoutePeer_Type=InetAddress
_CbgpRoutePeer_Object=MibTableColumn
cbgpRoutePeer=_CbgpRoutePeer_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,4),_CbgpRoutePeer_Type())
cbgpRoutePeer.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpRoutePeer.setStatus(_A)
_CbgpRouteAddrPrefix_Type=CbgpNetworkAddress
_CbgpRouteAddrPrefix_Object=MibTableColumn
cbgpRouteAddrPrefix=_CbgpRouteAddrPrefix_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,5),_CbgpRouteAddrPrefix_Type())
cbgpRouteAddrPrefix.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpRouteAddrPrefix.setStatus(_A)
class _CbgpRouteAddrPrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2040))
_CbgpRouteAddrPrefixLen_Type.__name__=_H
_CbgpRouteAddrPrefixLen_Object=MibTableColumn
cbgpRouteAddrPrefixLen=_CbgpRouteAddrPrefixLen_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,6),_CbgpRouteAddrPrefixLen_Type())
cbgpRouteAddrPrefixLen.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpRouteAddrPrefixLen.setStatus(_A)
class _CbgpRouteOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_CbgpRouteOrigin_Type.__name__=_D
_CbgpRouteOrigin_Object=MibTableColumn
cbgpRouteOrigin=_CbgpRouteOrigin_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,7),_CbgpRouteOrigin_Type())
cbgpRouteOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteOrigin.setStatus(_A)
class _CbgpRouteASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CbgpRouteASPathSegment_Type.__name__=_K
_CbgpRouteASPathSegment_Object=MibTableColumn
cbgpRouteASPathSegment=_CbgpRouteASPathSegment_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,8),_CbgpRouteASPathSegment_Type())
cbgpRouteASPathSegment.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteASPathSegment.setStatus(_A)
_CbgpRouteNextHop_Type=CbgpNetworkAddress
_CbgpRouteNextHop_Object=MibTableColumn
cbgpRouteNextHop=_CbgpRouteNextHop_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,9),_CbgpRouteNextHop_Type())
cbgpRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteNextHop.setStatus(_A)
_CbgpRouteMedPresent_Type=TruthValue
_CbgpRouteMedPresent_Object=MibTableColumn
cbgpRouteMedPresent=_CbgpRouteMedPresent_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,10),_CbgpRouteMedPresent_Type())
cbgpRouteMedPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteMedPresent.setStatus(_A)
class _CbgpRouteMultiExitDisc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CbgpRouteMultiExitDisc_Type.__name__=_H
_CbgpRouteMultiExitDisc_Object=MibTableColumn
cbgpRouteMultiExitDisc=_CbgpRouteMultiExitDisc_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,11),_CbgpRouteMultiExitDisc_Type())
cbgpRouteMultiExitDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteMultiExitDisc.setStatus(_A)
_CbgpRouteLocalPrefPresent_Type=TruthValue
_CbgpRouteLocalPrefPresent_Object=MibTableColumn
cbgpRouteLocalPrefPresent=_CbgpRouteLocalPrefPresent_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,12),_CbgpRouteLocalPrefPresent_Type())
cbgpRouteLocalPrefPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteLocalPrefPresent.setStatus(_A)
class _CbgpRouteLocalPref_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CbgpRouteLocalPref_Type.__name__=_H
_CbgpRouteLocalPref_Object=MibTableColumn
cbgpRouteLocalPref=_CbgpRouteLocalPref_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,13),_CbgpRouteLocalPref_Type())
cbgpRouteLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteLocalPref.setStatus(_A)
class _CbgpRouteAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRouteNotSelected',1),('lessSpecificRouteSelected',2)))
_CbgpRouteAtomicAggregate_Type.__name__=_D
_CbgpRouteAtomicAggregate_Object=MibTableColumn
cbgpRouteAtomicAggregate=_CbgpRouteAtomicAggregate_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,14),_CbgpRouteAtomicAggregate_Type())
cbgpRouteAtomicAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteAtomicAggregate.setStatus(_A)
class _CbgpRouteAggregatorAS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CbgpRouteAggregatorAS_Type.__name__=_H
_CbgpRouteAggregatorAS_Object=MibTableColumn
cbgpRouteAggregatorAS=_CbgpRouteAggregatorAS_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,15),_CbgpRouteAggregatorAS_Type())
cbgpRouteAggregatorAS.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteAggregatorAS.setStatus(_A)
_CbgpRouteAggregatorAddrType_Type=InetAddressType
_CbgpRouteAggregatorAddrType_Object=MibTableColumn
cbgpRouteAggregatorAddrType=_CbgpRouteAggregatorAddrType_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,16),_CbgpRouteAggregatorAddrType_Type())
cbgpRouteAggregatorAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteAggregatorAddrType.setStatus(_A)
_CbgpRouteAggregatorAddr_Type=InetAddress
_CbgpRouteAggregatorAddr_Object=MibTableColumn
cbgpRouteAggregatorAddr=_CbgpRouteAggregatorAddr_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,17),_CbgpRouteAggregatorAddr_Type())
cbgpRouteAggregatorAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteAggregatorAddr.setStatus(_A)
_CbgpRouteBest_Type=TruthValue
_CbgpRouteBest_Object=MibTableColumn
cbgpRouteBest=_CbgpRouteBest_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,18),_CbgpRouteBest_Type())
cbgpRouteBest.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteBest.setStatus(_A)
class _CbgpRouteUnknownAttr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CbgpRouteUnknownAttr_Type.__name__=_K
_CbgpRouteUnknownAttr_Object=MibTableColumn
cbgpRouteUnknownAttr=_CbgpRouteUnknownAttr_Object((1,3,6,1,4,1,9,9,187,1,1,1,1,19),_CbgpRouteUnknownAttr_Type())
cbgpRouteUnknownAttr.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpRouteUnknownAttr.setStatus(_A)
_CbgpPeer_ObjectIdentity=ObjectIdentity
cbgpPeer=_CbgpPeer_ObjectIdentity((1,3,6,1,4,1,9,9,187,1,2))
_CbgpPeerTable_Object=MibTable
cbgpPeerTable=_CbgpPeerTable_Object((1,3,6,1,4,1,9,9,187,1,2,1))
if mibBuilder.loadTexts:cbgpPeerTable.setStatus(_A)
_CbgpPeerEntry_Object=MibTableRow
cbgpPeerEntry=_CbgpPeerEntry_Object((1,3,6,1,4,1,9,9,187,1,2,1,1))
if mibBuilder.loadTexts:cbgpPeerEntry.setStatus(_A)
_CbgpPeerPrefixAccepted_Type=Counter32
_CbgpPeerPrefixAccepted_Object=MibTableColumn
cbgpPeerPrefixAccepted=_CbgpPeerPrefixAccepted_Object((1,3,6,1,4,1,9,9,187,1,2,1,1,1),_CbgpPeerPrefixAccepted_Type())
cbgpPeerPrefixAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerPrefixAccepted.setStatus(_I)
_CbgpPeerPrefixDenied_Type=Counter32
_CbgpPeerPrefixDenied_Object=MibTableColumn
cbgpPeerPrefixDenied=_CbgpPeerPrefixDenied_Object((1,3,6,1,4,1,9,9,187,1,2,1,1,2),_CbgpPeerPrefixDenied_Type())
cbgpPeerPrefixDenied.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerPrefixDenied.setStatus(_I)
class _CbgpPeerPrefixLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CbgpPeerPrefixLimit_Type.__name__=_H
_CbgpPeerPrefixLimit_Object=MibTableColumn
cbgpPeerPrefixLimit=_CbgpPeerPrefixLimit_Object((1,3,6,1,4,1,9,9,187,1,2,1,1,3),_CbgpPeerPrefixLimit_Type())
cbgpPeerPrefixLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeerPrefixLimit.setStatus(_I)
_CbgpPeerPrefixAdvertised_Type=Counter32
_CbgpPeerPrefixAdvertised_Object=MibTableColumn
cbgpPeerPrefixAdvertised=_CbgpPeerPrefixAdvertised_Object((1,3,6,1,4,1,9,9,187,1,2,1,1,4),_CbgpPeerPrefixAdvertised_Type())
cbgpPeerPrefixAdvertised.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerPrefixAdvertised.setStatus(_I)
_CbgpPeerPrefixSuppressed_Type=Counter32
_CbgpPeerPrefixSuppressed_Object=MibTableColumn
cbgpPeerPrefixSuppressed=_CbgpPeerPrefixSuppressed_Object((1,3,6,1,4,1,9,9,187,1,2,1,1,5),_CbgpPeerPrefixSuppressed_Type())
cbgpPeerPrefixSuppressed.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerPrefixSuppressed.setStatus(_I)
_CbgpPeerPrefixWithdrawn_Type=Counter32
_CbgpPeerPrefixWithdrawn_Object=MibTableColumn
cbgpPeerPrefixWithdrawn=_CbgpPeerPrefixWithdrawn_Object((1,3,6,1,4,1,9,9,187,1,2,1,1,6),_CbgpPeerPrefixWithdrawn_Type())
cbgpPeerPrefixWithdrawn.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerPrefixWithdrawn.setStatus(_I)
_CbgpPeerLastErrorTxt_Type=SnmpAdminString
_CbgpPeerLastErrorTxt_Object=MibTableColumn
cbgpPeerLastErrorTxt=_CbgpPeerLastErrorTxt_Object((1,3,6,1,4,1,9,9,187,1,2,1,1,7),_CbgpPeerLastErrorTxt_Type())
cbgpPeerLastErrorTxt.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerLastErrorTxt.setStatus(_A)
class _CbgpPeerPrevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_f,0),(_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_CbgpPeerPrevState_Type.__name__=_D
_CbgpPeerPrevState_Object=MibTableColumn
cbgpPeerPrevState=_CbgpPeerPrevState_Object((1,3,6,1,4,1,9,9,187,1,2,1,1,8),_CbgpPeerPrevState_Type())
cbgpPeerPrevState.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerPrevState.setStatus(_A)
_CbgpPeerCapsTable_Object=MibTable
cbgpPeerCapsTable=_CbgpPeerCapsTable_Object((1,3,6,1,4,1,9,9,187,1,2,2))
if mibBuilder.loadTexts:cbgpPeerCapsTable.setStatus(_A)
_CbgpPeerCapsEntry_Object=MibTableRow
cbgpPeerCapsEntry=_CbgpPeerCapsEntry_Object((1,3,6,1,4,1,9,9,187,1,2,2,1))
cbgpPeerCapsEntry.setIndexNames((0,_J,_W),(0,_B,_y),(0,_B,_z))
if mibBuilder.loadTexts:cbgpPeerCapsEntry.setStatus(_A)
class _CbgpPeerCapCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,64,128)));namedValues=NamedValues(*((_A0,1),(_A1,2),(_A2,64),(_A3,128)))
_CbgpPeerCapCode_Type.__name__=_D
_CbgpPeerCapCode_Object=MibTableColumn
cbgpPeerCapCode=_CbgpPeerCapCode_Object((1,3,6,1,4,1,9,9,187,1,2,2,1,1),_CbgpPeerCapCode_Type())
cbgpPeerCapCode.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeerCapCode.setStatus(_A)
class _CbgpPeerCapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CbgpPeerCapIndex_Type.__name__=_H
_CbgpPeerCapIndex_Object=MibTableColumn
cbgpPeerCapIndex=_CbgpPeerCapIndex_Object((1,3,6,1,4,1,9,9,187,1,2,2,1,2),_CbgpPeerCapIndex_Type())
cbgpPeerCapIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeerCapIndex.setStatus(_A)
class _CbgpPeerCapValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CbgpPeerCapValue_Type.__name__=_K
_CbgpPeerCapValue_Object=MibTableColumn
cbgpPeerCapValue=_CbgpPeerCapValue_Object((1,3,6,1,4,1,9,9,187,1,2,2,1,3),_CbgpPeerCapValue_Type())
cbgpPeerCapValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerCapValue.setStatus(_A)
_CbgpPeerAddrFamilyTable_Object=MibTable
cbgpPeerAddrFamilyTable=_CbgpPeerAddrFamilyTable_Object((1,3,6,1,4,1,9,9,187,1,2,3))
if mibBuilder.loadTexts:cbgpPeerAddrFamilyTable.setStatus(_A)
_CbgpPeerAddrFamilyEntry_Object=MibTableRow
cbgpPeerAddrFamilyEntry=_CbgpPeerAddrFamilyEntry_Object((1,3,6,1,4,1,9,9,187,1,2,3,1))
cbgpPeerAddrFamilyEntry.setIndexNames((0,_J,_W),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:cbgpPeerAddrFamilyEntry.setStatus(_A)
_CbgpPeerAddrFamilyAfi_Type=InetAddressType
_CbgpPeerAddrFamilyAfi_Object=MibTableColumn
cbgpPeerAddrFamilyAfi=_CbgpPeerAddrFamilyAfi_Object((1,3,6,1,4,1,9,9,187,1,2,3,1,1),_CbgpPeerAddrFamilyAfi_Type())
cbgpPeerAddrFamilyAfi.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeerAddrFamilyAfi.setStatus(_A)
_CbgpPeerAddrFamilySafi_Type=CbgpSafi
_CbgpPeerAddrFamilySafi_Object=MibTableColumn
cbgpPeerAddrFamilySafi=_CbgpPeerAddrFamilySafi_Object((1,3,6,1,4,1,9,9,187,1,2,3,1,2),_CbgpPeerAddrFamilySafi_Type())
cbgpPeerAddrFamilySafi.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeerAddrFamilySafi.setStatus(_A)
_CbgpPeerAddrFamilyName_Type=SnmpAdminString
_CbgpPeerAddrFamilyName_Object=MibTableColumn
cbgpPeerAddrFamilyName=_CbgpPeerAddrFamilyName_Object((1,3,6,1,4,1,9,9,187,1,2,3,1,3),_CbgpPeerAddrFamilyName_Type())
cbgpPeerAddrFamilyName.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerAddrFamilyName.setStatus(_A)
_CbgpPeerAddrFamilyPrefixTable_Object=MibTable
cbgpPeerAddrFamilyPrefixTable=_CbgpPeerAddrFamilyPrefixTable_Object((1,3,6,1,4,1,9,9,187,1,2,4))
if mibBuilder.loadTexts:cbgpPeerAddrFamilyPrefixTable.setStatus(_A)
_CbgpPeerAddrFamilyPrefixEntry_Object=MibTableRow
cbgpPeerAddrFamilyPrefixEntry=_CbgpPeerAddrFamilyPrefixEntry_Object((1,3,6,1,4,1,9,9,187,1,2,4,1))
cbgpPeerAddrFamilyPrefixEntry.setIndexNames((0,_J,_W),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:cbgpPeerAddrFamilyPrefixEntry.setStatus(_A)
_CbgpPeerAcceptedPrefixes_Type=Counter32
_CbgpPeerAcceptedPrefixes_Object=MibTableColumn
cbgpPeerAcceptedPrefixes=_CbgpPeerAcceptedPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,4,1,1),_CbgpPeerAcceptedPrefixes_Type())
cbgpPeerAcceptedPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerAcceptedPrefixes.setStatus(_A)
_CbgpPeerDeniedPrefixes_Type=Gauge32
_CbgpPeerDeniedPrefixes_Object=MibTableColumn
cbgpPeerDeniedPrefixes=_CbgpPeerDeniedPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,4,1,2),_CbgpPeerDeniedPrefixes_Type())
cbgpPeerDeniedPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerDeniedPrefixes.setStatus(_A)
class _CbgpPeerPrefixAdminLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CbgpPeerPrefixAdminLimit_Type.__name__=_H
_CbgpPeerPrefixAdminLimit_Object=MibTableColumn
cbgpPeerPrefixAdminLimit=_CbgpPeerPrefixAdminLimit_Object((1,3,6,1,4,1,9,9,187,1,2,4,1,3),_CbgpPeerPrefixAdminLimit_Type())
cbgpPeerPrefixAdminLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeerPrefixAdminLimit.setStatus(_A)
class _CbgpPeerPrefixThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CbgpPeerPrefixThreshold_Type.__name__=_H
_CbgpPeerPrefixThreshold_Object=MibTableColumn
cbgpPeerPrefixThreshold=_CbgpPeerPrefixThreshold_Object((1,3,6,1,4,1,9,9,187,1,2,4,1,4),_CbgpPeerPrefixThreshold_Type())
cbgpPeerPrefixThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeerPrefixThreshold.setStatus(_A)
class _CbgpPeerPrefixClearThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CbgpPeerPrefixClearThreshold_Type.__name__=_H
_CbgpPeerPrefixClearThreshold_Object=MibTableColumn
cbgpPeerPrefixClearThreshold=_CbgpPeerPrefixClearThreshold_Object((1,3,6,1,4,1,9,9,187,1,2,4,1,5),_CbgpPeerPrefixClearThreshold_Type())
cbgpPeerPrefixClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerPrefixClearThreshold.setStatus(_A)
_CbgpPeerAdvertisedPrefixes_Type=Gauge32
_CbgpPeerAdvertisedPrefixes_Object=MibTableColumn
cbgpPeerAdvertisedPrefixes=_CbgpPeerAdvertisedPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,4,1,6),_CbgpPeerAdvertisedPrefixes_Type())
cbgpPeerAdvertisedPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerAdvertisedPrefixes.setStatus(_A)
_CbgpPeerSuppressedPrefixes_Type=Gauge32
_CbgpPeerSuppressedPrefixes_Object=MibTableColumn
cbgpPeerSuppressedPrefixes=_CbgpPeerSuppressedPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,4,1,7),_CbgpPeerSuppressedPrefixes_Type())
cbgpPeerSuppressedPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerSuppressedPrefixes.setStatus(_A)
_CbgpPeerWithdrawnPrefixes_Type=Gauge32
_CbgpPeerWithdrawnPrefixes_Object=MibTableColumn
cbgpPeerWithdrawnPrefixes=_CbgpPeerWithdrawnPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,4,1,8),_CbgpPeerWithdrawnPrefixes_Type())
cbgpPeerWithdrawnPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeerWithdrawnPrefixes.setStatus(_A)
_CbgpPeer2Table_Object=MibTable
cbgpPeer2Table=_CbgpPeer2Table_Object((1,3,6,1,4,1,9,9,187,1,2,5))
if mibBuilder.loadTexts:cbgpPeer2Table.setStatus(_A)
_CbgpPeer2Entry_Object=MibTableRow
cbgpPeer2Entry=_CbgpPeer2Entry_Object((1,3,6,1,4,1,9,9,187,1,2,5,1))
cbgpPeer2Entry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:cbgpPeer2Entry.setStatus(_A)
_CbgpPeer2Type_Type=InetAddressType
_CbgpPeer2Type_Object=MibTableColumn
cbgpPeer2Type=_CbgpPeer2Type_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,1),_CbgpPeer2Type_Type())
cbgpPeer2Type.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeer2Type.setStatus(_A)
_CbgpPeer2RemoteAddr_Type=InetAddress
_CbgpPeer2RemoteAddr_Object=MibTableColumn
cbgpPeer2RemoteAddr=_CbgpPeer2RemoteAddr_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,2),_CbgpPeer2RemoteAddr_Type())
cbgpPeer2RemoteAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeer2RemoteAddr.setStatus(_A)
class _CbgpPeer2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_CbgpPeer2State_Type.__name__=_D
_CbgpPeer2State_Object=MibTableColumn
cbgpPeer2State=_CbgpPeer2State_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,3),_CbgpPeer2State_Type())
cbgpPeer2State.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2State.setStatus(_A)
class _CbgpPeer2AdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_CbgpPeer2AdminStatus_Type.__name__=_D
_CbgpPeer2AdminStatus_Object=MibTableColumn
cbgpPeer2AdminStatus=_CbgpPeer2AdminStatus_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,4),_CbgpPeer2AdminStatus_Type())
cbgpPeer2AdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer2AdminStatus.setStatus(_A)
_CbgpPeer2NegotiatedVersion_Type=Integer32
_CbgpPeer2NegotiatedVersion_Object=MibTableColumn
cbgpPeer2NegotiatedVersion=_CbgpPeer2NegotiatedVersion_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,5),_CbgpPeer2NegotiatedVersion_Type())
cbgpPeer2NegotiatedVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2NegotiatedVersion.setStatus(_A)
_CbgpPeer2LocalAddr_Type=InetAddress
_CbgpPeer2LocalAddr_Object=MibTableColumn
cbgpPeer2LocalAddr=_CbgpPeer2LocalAddr_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,6),_CbgpPeer2LocalAddr_Type())
cbgpPeer2LocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2LocalAddr.setStatus(_A)
_CbgpPeer2LocalPort_Type=InetPortNumber
_CbgpPeer2LocalPort_Object=MibTableColumn
cbgpPeer2LocalPort=_CbgpPeer2LocalPort_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,7),_CbgpPeer2LocalPort_Type())
cbgpPeer2LocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2LocalPort.setStatus(_A)
_CbgpPeer2LocalAs_Type=InetAutonomousSystemNumber
_CbgpPeer2LocalAs_Object=MibTableColumn
cbgpPeer2LocalAs=_CbgpPeer2LocalAs_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,8),_CbgpPeer2LocalAs_Type())
cbgpPeer2LocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2LocalAs.setStatus(_A)
_CbgpPeer2LocalIdentifier_Type=IpAddress
_CbgpPeer2LocalIdentifier_Object=MibTableColumn
cbgpPeer2LocalIdentifier=_CbgpPeer2LocalIdentifier_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,9),_CbgpPeer2LocalIdentifier_Type())
cbgpPeer2LocalIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2LocalIdentifier.setStatus(_A)
_CbgpPeer2RemotePort_Type=InetPortNumber
_CbgpPeer2RemotePort_Object=MibTableColumn
cbgpPeer2RemotePort=_CbgpPeer2RemotePort_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,10),_CbgpPeer2RemotePort_Type())
cbgpPeer2RemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2RemotePort.setStatus(_A)
_CbgpPeer2RemoteAs_Type=InetAutonomousSystemNumber
_CbgpPeer2RemoteAs_Object=MibTableColumn
cbgpPeer2RemoteAs=_CbgpPeer2RemoteAs_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,11),_CbgpPeer2RemoteAs_Type())
cbgpPeer2RemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2RemoteAs.setStatus(_A)
_CbgpPeer2RemoteIdentifier_Type=IpAddress
_CbgpPeer2RemoteIdentifier_Object=MibTableColumn
cbgpPeer2RemoteIdentifier=_CbgpPeer2RemoteIdentifier_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,12),_CbgpPeer2RemoteIdentifier_Type())
cbgpPeer2RemoteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2RemoteIdentifier.setStatus(_A)
_CbgpPeer2InUpdates_Type=Counter32
_CbgpPeer2InUpdates_Object=MibTableColumn
cbgpPeer2InUpdates=_CbgpPeer2InUpdates_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,13),_CbgpPeer2InUpdates_Type())
cbgpPeer2InUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2InUpdates.setStatus(_A)
_CbgpPeer2OutUpdates_Type=Counter32
_CbgpPeer2OutUpdates_Object=MibTableColumn
cbgpPeer2OutUpdates=_CbgpPeer2OutUpdates_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,14),_CbgpPeer2OutUpdates_Type())
cbgpPeer2OutUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2OutUpdates.setStatus(_A)
_CbgpPeer2InTotalMessages_Type=Counter32
_CbgpPeer2InTotalMessages_Object=MibTableColumn
cbgpPeer2InTotalMessages=_CbgpPeer2InTotalMessages_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,15),_CbgpPeer2InTotalMessages_Type())
cbgpPeer2InTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2InTotalMessages.setStatus(_A)
_CbgpPeer2OutTotalMessages_Type=Counter32
_CbgpPeer2OutTotalMessages_Object=MibTableColumn
cbgpPeer2OutTotalMessages=_CbgpPeer2OutTotalMessages_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,16),_CbgpPeer2OutTotalMessages_Type())
cbgpPeer2OutTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2OutTotalMessages.setStatus(_A)
class _CbgpPeer2LastError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CbgpPeer2LastError_Type.__name__=_K
_CbgpPeer2LastError_Object=MibTableColumn
cbgpPeer2LastError=_CbgpPeer2LastError_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,17),_CbgpPeer2LastError_Type())
cbgpPeer2LastError.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2LastError.setStatus(_A)
_CbgpPeer2FsmEstablishedTransitions_Type=Counter32
_CbgpPeer2FsmEstablishedTransitions_Object=MibTableColumn
cbgpPeer2FsmEstablishedTransitions=_CbgpPeer2FsmEstablishedTransitions_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,18),_CbgpPeer2FsmEstablishedTransitions_Type())
cbgpPeer2FsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2FsmEstablishedTransitions.setStatus(_A)
_CbgpPeer2FsmEstablishedTime_Type=Gauge32
_CbgpPeer2FsmEstablishedTime_Object=MibTableColumn
cbgpPeer2FsmEstablishedTime=_CbgpPeer2FsmEstablishedTime_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,19),_CbgpPeer2FsmEstablishedTime_Type())
cbgpPeer2FsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2FsmEstablishedTime.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2FsmEstablishedTime.setUnits(_F)
class _CbgpPeer2ConnectRetryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CbgpPeer2ConnectRetryInterval_Type.__name__=_D
_CbgpPeer2ConnectRetryInterval_Object=MibTableColumn
cbgpPeer2ConnectRetryInterval=_CbgpPeer2ConnectRetryInterval_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,20),_CbgpPeer2ConnectRetryInterval_Type())
cbgpPeer2ConnectRetryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer2ConnectRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2ConnectRetryInterval.setUnits(_F)
class _CbgpPeer2HoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_CbgpPeer2HoldTime_Type.__name__=_D
_CbgpPeer2HoldTime_Object=MibTableColumn
cbgpPeer2HoldTime=_CbgpPeer2HoldTime_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,21),_CbgpPeer2HoldTime_Type())
cbgpPeer2HoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2HoldTime.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2HoldTime.setUnits(_F)
class _CbgpPeer2KeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_CbgpPeer2KeepAlive_Type.__name__=_D
_CbgpPeer2KeepAlive_Object=MibTableColumn
cbgpPeer2KeepAlive=_CbgpPeer2KeepAlive_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,22),_CbgpPeer2KeepAlive_Type())
cbgpPeer2KeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2KeepAlive.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2KeepAlive.setUnits(_F)
class _CbgpPeer2HoldTimeConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_CbgpPeer2HoldTimeConfigured_Type.__name__=_D
_CbgpPeer2HoldTimeConfigured_Object=MibTableColumn
cbgpPeer2HoldTimeConfigured=_CbgpPeer2HoldTimeConfigured_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,23),_CbgpPeer2HoldTimeConfigured_Type())
cbgpPeer2HoldTimeConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer2HoldTimeConfigured.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2HoldTimeConfigured.setUnits(_F)
class _CbgpPeer2KeepAliveConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_CbgpPeer2KeepAliveConfigured_Type.__name__=_D
_CbgpPeer2KeepAliveConfigured_Object=MibTableColumn
cbgpPeer2KeepAliveConfigured=_CbgpPeer2KeepAliveConfigured_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,24),_CbgpPeer2KeepAliveConfigured_Type())
cbgpPeer2KeepAliveConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer2KeepAliveConfigured.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2KeepAliveConfigured.setUnits(_F)
class _CbgpPeer2MinASOriginationInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CbgpPeer2MinASOriginationInterval_Type.__name__=_D
_CbgpPeer2MinASOriginationInterval_Object=MibTableColumn
cbgpPeer2MinASOriginationInterval=_CbgpPeer2MinASOriginationInterval_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,25),_CbgpPeer2MinASOriginationInterval_Type())
cbgpPeer2MinASOriginationInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer2MinASOriginationInterval.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2MinASOriginationInterval.setUnits(_F)
class _CbgpPeer2MinRouteAdvertisementInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CbgpPeer2MinRouteAdvertisementInterval_Type.__name__=_D
_CbgpPeer2MinRouteAdvertisementInterval_Object=MibTableColumn
cbgpPeer2MinRouteAdvertisementInterval=_CbgpPeer2MinRouteAdvertisementInterval_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,26),_CbgpPeer2MinRouteAdvertisementInterval_Type())
cbgpPeer2MinRouteAdvertisementInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer2MinRouteAdvertisementInterval.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2MinRouteAdvertisementInterval.setUnits(_F)
_CbgpPeer2InUpdateElapsedTime_Type=Gauge32
_CbgpPeer2InUpdateElapsedTime_Object=MibTableColumn
cbgpPeer2InUpdateElapsedTime=_CbgpPeer2InUpdateElapsedTime_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,27),_CbgpPeer2InUpdateElapsedTime_Type())
cbgpPeer2InUpdateElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2InUpdateElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2InUpdateElapsedTime.setUnits(_F)
_CbgpPeer2LastErrorTxt_Type=SnmpAdminString
_CbgpPeer2LastErrorTxt_Object=MibTableColumn
cbgpPeer2LastErrorTxt=_CbgpPeer2LastErrorTxt_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,28),_CbgpPeer2LastErrorTxt_Type())
cbgpPeer2LastErrorTxt.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2LastErrorTxt.setStatus(_A)
class _CbgpPeer2PrevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_f,0),(_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_CbgpPeer2PrevState_Type.__name__=_D
_CbgpPeer2PrevState_Object=MibTableColumn
cbgpPeer2PrevState=_CbgpPeer2PrevState_Object((1,3,6,1,4,1,9,9,187,1,2,5,1,29),_CbgpPeer2PrevState_Type())
cbgpPeer2PrevState.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2PrevState.setStatus(_A)
_CbgpPeer2CapsTable_Object=MibTable
cbgpPeer2CapsTable=_CbgpPeer2CapsTable_Object((1,3,6,1,4,1,9,9,187,1,2,6))
if mibBuilder.loadTexts:cbgpPeer2CapsTable.setStatus(_A)
_CbgpPeer2CapsEntry_Object=MibTableRow
cbgpPeer2CapsEntry=_CbgpPeer2CapsEntry_Object((1,3,6,1,4,1,9,9,187,1,2,6,1))
cbgpPeer2CapsEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_A4),(0,_B,_A5))
if mibBuilder.loadTexts:cbgpPeer2CapsEntry.setStatus(_A)
class _CbgpPeer2CapCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,64,65,69,128)));namedValues=NamedValues(*((_A0,1),(_A1,2),(_A2,64),('fourByteAs',65),('addPath',69),(_A3,128)))
_CbgpPeer2CapCode_Type.__name__=_D
_CbgpPeer2CapCode_Object=MibTableColumn
cbgpPeer2CapCode=_CbgpPeer2CapCode_Object((1,3,6,1,4,1,9,9,187,1,2,6,1,1),_CbgpPeer2CapCode_Type())
cbgpPeer2CapCode.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeer2CapCode.setStatus(_A)
class _CbgpPeer2CapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CbgpPeer2CapIndex_Type.__name__=_H
_CbgpPeer2CapIndex_Object=MibTableColumn
cbgpPeer2CapIndex=_CbgpPeer2CapIndex_Object((1,3,6,1,4,1,9,9,187,1,2,6,1,2),_CbgpPeer2CapIndex_Type())
cbgpPeer2CapIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeer2CapIndex.setStatus(_A)
class _CbgpPeer2CapValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CbgpPeer2CapValue_Type.__name__=_K
_CbgpPeer2CapValue_Object=MibTableColumn
cbgpPeer2CapValue=_CbgpPeer2CapValue_Object((1,3,6,1,4,1,9,9,187,1,2,6,1,3),_CbgpPeer2CapValue_Type())
cbgpPeer2CapValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2CapValue.setStatus(_A)
_CbgpPeer2AddrFamilyTable_Object=MibTable
cbgpPeer2AddrFamilyTable=_CbgpPeer2AddrFamilyTable_Object((1,3,6,1,4,1,9,9,187,1,2,7))
if mibBuilder.loadTexts:cbgpPeer2AddrFamilyTable.setStatus(_A)
_CbgpPeer2AddrFamilyEntry_Object=MibTableRow
cbgpPeer2AddrFamilyEntry=_CbgpPeer2AddrFamilyEntry_Object((1,3,6,1,4,1,9,9,187,1,2,7,1))
cbgpPeer2AddrFamilyEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:cbgpPeer2AddrFamilyEntry.setStatus(_A)
_CbgpPeer2AddrFamilyAfi_Type=InetAddressType
_CbgpPeer2AddrFamilyAfi_Object=MibTableColumn
cbgpPeer2AddrFamilyAfi=_CbgpPeer2AddrFamilyAfi_Object((1,3,6,1,4,1,9,9,187,1,2,7,1,1),_CbgpPeer2AddrFamilyAfi_Type())
cbgpPeer2AddrFamilyAfi.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeer2AddrFamilyAfi.setStatus(_A)
_CbgpPeer2AddrFamilySafi_Type=CbgpSafi
_CbgpPeer2AddrFamilySafi_Object=MibTableColumn
cbgpPeer2AddrFamilySafi=_CbgpPeer2AddrFamilySafi_Object((1,3,6,1,4,1,9,9,187,1,2,7,1,2),_CbgpPeer2AddrFamilySafi_Type())
cbgpPeer2AddrFamilySafi.setMaxAccess(_G)
if mibBuilder.loadTexts:cbgpPeer2AddrFamilySafi.setStatus(_A)
_CbgpPeer2AddrFamilyName_Type=SnmpAdminString
_CbgpPeer2AddrFamilyName_Object=MibTableColumn
cbgpPeer2AddrFamilyName=_CbgpPeer2AddrFamilyName_Object((1,3,6,1,4,1,9,9,187,1,2,7,1,3),_CbgpPeer2AddrFamilyName_Type())
cbgpPeer2AddrFamilyName.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2AddrFamilyName.setStatus(_A)
_CbgpPeer2AddrFamilyPrefixTable_Object=MibTable
cbgpPeer2AddrFamilyPrefixTable=_CbgpPeer2AddrFamilyPrefixTable_Object((1,3,6,1,4,1,9,9,187,1,2,8))
if mibBuilder.loadTexts:cbgpPeer2AddrFamilyPrefixTable.setStatus(_A)
_CbgpPeer2AddrFamilyPrefixEntry_Object=MibTableRow
cbgpPeer2AddrFamilyPrefixEntry=_CbgpPeer2AddrFamilyPrefixEntry_Object((1,3,6,1,4,1,9,9,187,1,2,8,1))
cbgpPeer2AddrFamilyPrefixEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:cbgpPeer2AddrFamilyPrefixEntry.setStatus(_A)
_CbgpPeer2AcceptedPrefixes_Type=Counter32
_CbgpPeer2AcceptedPrefixes_Object=MibTableColumn
cbgpPeer2AcceptedPrefixes=_CbgpPeer2AcceptedPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,8,1,1),_CbgpPeer2AcceptedPrefixes_Type())
cbgpPeer2AcceptedPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2AcceptedPrefixes.setStatus(_A)
_CbgpPeer2DeniedPrefixes_Type=Gauge32
_CbgpPeer2DeniedPrefixes_Object=MibTableColumn
cbgpPeer2DeniedPrefixes=_CbgpPeer2DeniedPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,8,1,2),_CbgpPeer2DeniedPrefixes_Type())
cbgpPeer2DeniedPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2DeniedPrefixes.setStatus(_A)
class _CbgpPeer2PrefixAdminLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CbgpPeer2PrefixAdminLimit_Type.__name__=_H
_CbgpPeer2PrefixAdminLimit_Object=MibTableColumn
cbgpPeer2PrefixAdminLimit=_CbgpPeer2PrefixAdminLimit_Object((1,3,6,1,4,1,9,9,187,1,2,8,1,3),_CbgpPeer2PrefixAdminLimit_Type())
cbgpPeer2PrefixAdminLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer2PrefixAdminLimit.setStatus(_A)
class _CbgpPeer2PrefixThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CbgpPeer2PrefixThreshold_Type.__name__=_H
_CbgpPeer2PrefixThreshold_Object=MibTableColumn
cbgpPeer2PrefixThreshold=_CbgpPeer2PrefixThreshold_Object((1,3,6,1,4,1,9,9,187,1,2,8,1,4),_CbgpPeer2PrefixThreshold_Type())
cbgpPeer2PrefixThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer2PrefixThreshold.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2PrefixThreshold.setUnits('percent')
class _CbgpPeer2PrefixClearThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CbgpPeer2PrefixClearThreshold_Type.__name__=_H
_CbgpPeer2PrefixClearThreshold_Object=MibTableColumn
cbgpPeer2PrefixClearThreshold=_CbgpPeer2PrefixClearThreshold_Object((1,3,6,1,4,1,9,9,187,1,2,8,1,5),_CbgpPeer2PrefixClearThreshold_Type())
cbgpPeer2PrefixClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2PrefixClearThreshold.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer2PrefixClearThreshold.setUnits('percent')
_CbgpPeer2AdvertisedPrefixes_Type=Gauge32
_CbgpPeer2AdvertisedPrefixes_Object=MibTableColumn
cbgpPeer2AdvertisedPrefixes=_CbgpPeer2AdvertisedPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,8,1,6),_CbgpPeer2AdvertisedPrefixes_Type())
cbgpPeer2AdvertisedPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2AdvertisedPrefixes.setStatus(_A)
_CbgpPeer2SuppressedPrefixes_Type=Gauge32
_CbgpPeer2SuppressedPrefixes_Object=MibTableColumn
cbgpPeer2SuppressedPrefixes=_CbgpPeer2SuppressedPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,8,1,7),_CbgpPeer2SuppressedPrefixes_Type())
cbgpPeer2SuppressedPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2SuppressedPrefixes.setStatus(_A)
_CbgpPeer2WithdrawnPrefixes_Type=Gauge32
_CbgpPeer2WithdrawnPrefixes_Object=MibTableColumn
cbgpPeer2WithdrawnPrefixes=_CbgpPeer2WithdrawnPrefixes_Object((1,3,6,1,4,1,9,9,187,1,2,8,1,8),_CbgpPeer2WithdrawnPrefixes_Type())
cbgpPeer2WithdrawnPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer2WithdrawnPrefixes.setStatus(_A)
_CbgpPeer3Table_Object=MibTable
cbgpPeer3Table=_CbgpPeer3Table_Object((1,3,6,1,4,1,9,9,187,1,2,9))
if mibBuilder.loadTexts:cbgpPeer3Table.setStatus(_A)
_CbgpPeer3Entry_Object=MibTableRow
cbgpPeer3Entry=_CbgpPeer3Entry_Object((1,3,6,1,4,1,9,9,187,1,2,9,1))
cbgpPeer3Entry.setIndexNames((0,_B,_A6),(0,_B,_A7),(0,_B,_A8))
if mibBuilder.loadTexts:cbgpPeer3Entry.setStatus(_A)
class _CbgpPeer3VrfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CbgpPeer3VrfId_Type.__name__=_H
_CbgpPeer3VrfId_Object=MibTableColumn
cbgpPeer3VrfId=_CbgpPeer3VrfId_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,1),_CbgpPeer3VrfId_Type())
cbgpPeer3VrfId.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3VrfId.setStatus(_A)
_CbgpPeer3Type_Type=InetAddressType
_CbgpPeer3Type_Object=MibTableColumn
cbgpPeer3Type=_CbgpPeer3Type_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,2),_CbgpPeer3Type_Type())
cbgpPeer3Type.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3Type.setStatus(_A)
_CbgpPeer3RemoteAddr_Type=InetAddress
_CbgpPeer3RemoteAddr_Object=MibTableColumn
cbgpPeer3RemoteAddr=_CbgpPeer3RemoteAddr_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,3),_CbgpPeer3RemoteAddr_Type())
cbgpPeer3RemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3RemoteAddr.setStatus(_A)
class _CbgpPeer3VrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CbgpPeer3VrfName_Type.__name__=_r
_CbgpPeer3VrfName_Object=MibTableColumn
cbgpPeer3VrfName=_CbgpPeer3VrfName_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,4),_CbgpPeer3VrfName_Type())
cbgpPeer3VrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3VrfName.setStatus(_A)
class _CbgpPeer3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_CbgpPeer3State_Type.__name__=_D
_CbgpPeer3State_Object=MibTableColumn
cbgpPeer3State=_CbgpPeer3State_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,5),_CbgpPeer3State_Type())
cbgpPeer3State.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3State.setStatus(_A)
class _CbgpPeer3AdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_CbgpPeer3AdminStatus_Type.__name__=_D
_CbgpPeer3AdminStatus_Object=MibTableColumn
cbgpPeer3AdminStatus=_CbgpPeer3AdminStatus_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,6),_CbgpPeer3AdminStatus_Type())
cbgpPeer3AdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer3AdminStatus.setStatus(_A)
_CbgpPeer3NegotiatedVersion_Type=Integer32
_CbgpPeer3NegotiatedVersion_Object=MibTableColumn
cbgpPeer3NegotiatedVersion=_CbgpPeer3NegotiatedVersion_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,7),_CbgpPeer3NegotiatedVersion_Type())
cbgpPeer3NegotiatedVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3NegotiatedVersion.setStatus(_A)
_CbgpPeer3LocalAddr_Type=InetAddress
_CbgpPeer3LocalAddr_Object=MibTableColumn
cbgpPeer3LocalAddr=_CbgpPeer3LocalAddr_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,8),_CbgpPeer3LocalAddr_Type())
cbgpPeer3LocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3LocalAddr.setStatus(_A)
_CbgpPeer3LocalPort_Type=InetPortNumber
_CbgpPeer3LocalPort_Object=MibTableColumn
cbgpPeer3LocalPort=_CbgpPeer3LocalPort_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,9),_CbgpPeer3LocalPort_Type())
cbgpPeer3LocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3LocalPort.setStatus(_A)
_CbgpPeer3LocalAs_Type=InetAutonomousSystemNumber
_CbgpPeer3LocalAs_Object=MibTableColumn
cbgpPeer3LocalAs=_CbgpPeer3LocalAs_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,10),_CbgpPeer3LocalAs_Type())
cbgpPeer3LocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3LocalAs.setStatus(_A)
_CbgpPeer3LocalIdentifier_Type=IpAddress
_CbgpPeer3LocalIdentifier_Object=MibTableColumn
cbgpPeer3LocalIdentifier=_CbgpPeer3LocalIdentifier_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,11),_CbgpPeer3LocalIdentifier_Type())
cbgpPeer3LocalIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3LocalIdentifier.setStatus(_A)
_CbgpPeer3RemotePort_Type=InetPortNumber
_CbgpPeer3RemotePort_Object=MibTableColumn
cbgpPeer3RemotePort=_CbgpPeer3RemotePort_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,12),_CbgpPeer3RemotePort_Type())
cbgpPeer3RemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3RemotePort.setStatus(_A)
_CbgpPeer3RemoteAs_Type=InetAutonomousSystemNumber
_CbgpPeer3RemoteAs_Object=MibTableColumn
cbgpPeer3RemoteAs=_CbgpPeer3RemoteAs_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,13),_CbgpPeer3RemoteAs_Type())
cbgpPeer3RemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3RemoteAs.setStatus(_A)
_CbgpPeer3RemoteIdentifier_Type=IpAddress
_CbgpPeer3RemoteIdentifier_Object=MibTableColumn
cbgpPeer3RemoteIdentifier=_CbgpPeer3RemoteIdentifier_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,14),_CbgpPeer3RemoteIdentifier_Type())
cbgpPeer3RemoteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3RemoteIdentifier.setStatus(_A)
_CbgpPeer3InUpdates_Type=Counter32
_CbgpPeer3InUpdates_Object=MibTableColumn
cbgpPeer3InUpdates=_CbgpPeer3InUpdates_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,15),_CbgpPeer3InUpdates_Type())
cbgpPeer3InUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3InUpdates.setStatus(_A)
_CbgpPeer3OutUpdates_Type=Counter32
_CbgpPeer3OutUpdates_Object=MibTableColumn
cbgpPeer3OutUpdates=_CbgpPeer3OutUpdates_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,16),_CbgpPeer3OutUpdates_Type())
cbgpPeer3OutUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3OutUpdates.setStatus(_A)
_CbgpPeer3InTotalMessages_Type=Counter32
_CbgpPeer3InTotalMessages_Object=MibTableColumn
cbgpPeer3InTotalMessages=_CbgpPeer3InTotalMessages_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,17),_CbgpPeer3InTotalMessages_Type())
cbgpPeer3InTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3InTotalMessages.setStatus(_A)
_CbgpPeer3OutTotalMessages_Type=Counter32
_CbgpPeer3OutTotalMessages_Object=MibTableColumn
cbgpPeer3OutTotalMessages=_CbgpPeer3OutTotalMessages_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,18),_CbgpPeer3OutTotalMessages_Type())
cbgpPeer3OutTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3OutTotalMessages.setStatus(_A)
class _CbgpPeer3LastError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CbgpPeer3LastError_Type.__name__=_K
_CbgpPeer3LastError_Object=MibTableColumn
cbgpPeer3LastError=_CbgpPeer3LastError_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,19),_CbgpPeer3LastError_Type())
cbgpPeer3LastError.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3LastError.setStatus(_A)
_CbgpPeer3FsmEstablishedTransitions_Type=Counter32
_CbgpPeer3FsmEstablishedTransitions_Object=MibTableColumn
cbgpPeer3FsmEstablishedTransitions=_CbgpPeer3FsmEstablishedTransitions_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,20),_CbgpPeer3FsmEstablishedTransitions_Type())
cbgpPeer3FsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3FsmEstablishedTransitions.setStatus(_A)
_CbgpPeer3FsmEstablishedTime_Type=Gauge32
_CbgpPeer3FsmEstablishedTime_Object=MibTableColumn
cbgpPeer3FsmEstablishedTime=_CbgpPeer3FsmEstablishedTime_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,21),_CbgpPeer3FsmEstablishedTime_Type())
cbgpPeer3FsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3FsmEstablishedTime.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer3FsmEstablishedTime.setUnits(_F)
class _CbgpPeer3ConnectRetryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CbgpPeer3ConnectRetryInterval_Type.__name__=_D
_CbgpPeer3ConnectRetryInterval_Object=MibTableColumn
cbgpPeer3ConnectRetryInterval=_CbgpPeer3ConnectRetryInterval_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,22),_CbgpPeer3ConnectRetryInterval_Type())
cbgpPeer3ConnectRetryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer3ConnectRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer3ConnectRetryInterval.setUnits(_F)
class _CbgpPeer3HoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_CbgpPeer3HoldTime_Type.__name__=_D
_CbgpPeer3HoldTime_Object=MibTableColumn
cbgpPeer3HoldTime=_CbgpPeer3HoldTime_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,23),_CbgpPeer3HoldTime_Type())
cbgpPeer3HoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3HoldTime.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer3HoldTime.setUnits(_F)
class _CbgpPeer3KeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_CbgpPeer3KeepAlive_Type.__name__=_D
_CbgpPeer3KeepAlive_Object=MibTableColumn
cbgpPeer3KeepAlive=_CbgpPeer3KeepAlive_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,24),_CbgpPeer3KeepAlive_Type())
cbgpPeer3KeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3KeepAlive.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer3KeepAlive.setUnits(_F)
class _CbgpPeer3HoldTimeConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_CbgpPeer3HoldTimeConfigured_Type.__name__=_D
_CbgpPeer3HoldTimeConfigured_Object=MibTableColumn
cbgpPeer3HoldTimeConfigured=_CbgpPeer3HoldTimeConfigured_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,25),_CbgpPeer3HoldTimeConfigured_Type())
cbgpPeer3HoldTimeConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer3HoldTimeConfigured.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer3HoldTimeConfigured.setUnits(_F)
class _CbgpPeer3KeepAliveConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_CbgpPeer3KeepAliveConfigured_Type.__name__=_D
_CbgpPeer3KeepAliveConfigured_Object=MibTableColumn
cbgpPeer3KeepAliveConfigured=_CbgpPeer3KeepAliveConfigured_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,26),_CbgpPeer3KeepAliveConfigured_Type())
cbgpPeer3KeepAliveConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer3KeepAliveConfigured.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer3KeepAliveConfigured.setUnits(_F)
class _CbgpPeer3MinASOriginationInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CbgpPeer3MinASOriginationInterval_Type.__name__=_D
_CbgpPeer3MinASOriginationInterval_Object=MibTableColumn
cbgpPeer3MinASOriginationInterval=_CbgpPeer3MinASOriginationInterval_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,27),_CbgpPeer3MinASOriginationInterval_Type())
cbgpPeer3MinASOriginationInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer3MinASOriginationInterval.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer3MinASOriginationInterval.setUnits(_F)
class _CbgpPeer3MinRouteAdvertisementInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CbgpPeer3MinRouteAdvertisementInterval_Type.__name__=_D
_CbgpPeer3MinRouteAdvertisementInterval_Object=MibTableColumn
cbgpPeer3MinRouteAdvertisementInterval=_CbgpPeer3MinRouteAdvertisementInterval_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,28),_CbgpPeer3MinRouteAdvertisementInterval_Type())
cbgpPeer3MinRouteAdvertisementInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpPeer3MinRouteAdvertisementInterval.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer3MinRouteAdvertisementInterval.setUnits(_F)
_CbgpPeer3InUpdateElapsedTime_Type=Gauge32
_CbgpPeer3InUpdateElapsedTime_Object=MibTableColumn
cbgpPeer3InUpdateElapsedTime=_CbgpPeer3InUpdateElapsedTime_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,29),_CbgpPeer3InUpdateElapsedTime_Type())
cbgpPeer3InUpdateElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3InUpdateElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:cbgpPeer3InUpdateElapsedTime.setUnits(_F)
_CbgpPeer3LastErrorTxt_Type=SnmpAdminString
_CbgpPeer3LastErrorTxt_Object=MibTableColumn
cbgpPeer3LastErrorTxt=_CbgpPeer3LastErrorTxt_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,30),_CbgpPeer3LastErrorTxt_Type())
cbgpPeer3LastErrorTxt.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3LastErrorTxt.setStatus(_A)
class _CbgpPeer3PrevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_f,0),(_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_CbgpPeer3PrevState_Type.__name__=_D
_CbgpPeer3PrevState_Object=MibTableColumn
cbgpPeer3PrevState=_CbgpPeer3PrevState_Object((1,3,6,1,4,1,9,9,187,1,2,9,1,31),_CbgpPeer3PrevState_Type())
cbgpPeer3PrevState.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpPeer3PrevState.setStatus(_A)
_CbgpGlobal_ObjectIdentity=ObjectIdentity
cbgpGlobal=_CbgpGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,187,1,3))
class _CbgpNotifsEnable_Type(Bits):namedValues=NamedValues(*(('notifsEnable',0),('notifsPeer2Enable',1)))
_CbgpNotifsEnable_Type.__name__='Bits'
_CbgpNotifsEnable_Object=MibScalar
cbgpNotifsEnable=_CbgpNotifsEnable_Object((1,3,6,1,4,1,9,9,187,1,3,1),_CbgpNotifsEnable_Type())
cbgpNotifsEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cbgpNotifsEnable.setStatus(_A)
_CbgpLocalAs_Type=InetAutonomousSystemNumber
_CbgpLocalAs_Object=MibScalar
cbgpLocalAs=_CbgpLocalAs_Object((1,3,6,1,4,1,9,9,187,1,3,2),_CbgpLocalAs_Type())
cbgpLocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:cbgpLocalAs.setStatus(_A)
_CiscoBgp4NotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoBgp4NotificationPrefix=_CiscoBgp4NotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,187,2))
_CiscoBgp4MIBConformance_ObjectIdentity=ObjectIdentity
ciscoBgp4MIBConformance=_CiscoBgp4MIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,187,3))
_CiscoBgp4MIBCompliances_ObjectIdentity=ObjectIdentity
ciscoBgp4MIBCompliances=_CiscoBgp4MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,187,3,1))
_CiscoBgp4MIBGroups_ObjectIdentity=ObjectIdentity
ciscoBgp4MIBGroups=_CiscoBgp4MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,187,3,2))
bgpPeerEntry.registerAugmentions((_B,_A9))
cbgpPeerEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
ciscoBgp4RouteGroup=ObjectGroup((1,3,6,1,4,1,9,9,187,3,2,1))
ciscoBgp4RouteGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:ciscoBgp4RouteGroup.setStatus(_A)
ciscoBgp4PeerGroup=ObjectGroup((1,3,6,1,4,1,9,9,187,3,2,2))
ciscoBgp4PeerGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:ciscoBgp4PeerGroup.setStatus(_I)
ciscoBgp4PeerGroup1=ObjectGroup((1,3,6,1,4,1,9,9,187,3,2,4))
ciscoBgp4PeerGroup1.setObjects(*((_B,_X),(_B,_Y),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_Z),(_B,_k),(_B,_l),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:ciscoBgp4PeerGroup1.setStatus(_A)
ciscoBgp4Peer2Group=ObjectGroup((1,3,6,1,4,1,9,9,187,3,2,6))
ciscoBgp4Peer2Group.setObjects(*((_B,_L),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_M),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_a),(_B,_b),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_c),(_B,_m),(_B,_n),(_B,_B0),(_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:ciscoBgp4Peer2Group.setStatus(_A)
ciscoBgp4GlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,187,3,2,8))
ciscoBgp4GlobalGroup.setObjects(*((_B,_B3),(_B,_B4)))
if mibBuilder.loadTexts:ciscoBgp4GlobalGroup.setStatus(_A)
cbgpFsmStateChange=NotificationType((1,3,6,1,4,1,9,9,187,0,1))
cbgpFsmStateChange.setObjects(*((_J,_d),(_J,_e),(_B,_Y),(_B,_X)))
if mibBuilder.loadTexts:cbgpFsmStateChange.setStatus(_A)
cbgpBackwardTransition=NotificationType((1,3,6,1,4,1,9,9,187,0,2))
cbgpBackwardTransition.setObjects(*((_J,_d),(_J,_e),(_B,_Y),(_B,_X)))
if mibBuilder.loadTexts:cbgpBackwardTransition.setStatus(_A)
cbgpPrefixThresholdExceeded=NotificationType((1,3,6,1,4,1,9,9,187,0,3))
cbgpPrefixThresholdExceeded.setObjects(*((_B,_Z),(_B,_k)))
if mibBuilder.loadTexts:cbgpPrefixThresholdExceeded.setStatus(_A)
cbgpPrefixThresholdClear=NotificationType((1,3,6,1,4,1,9,9,187,0,4))
cbgpPrefixThresholdClear.setObjects(*((_B,_Z),(_B,_l)))
if mibBuilder.loadTexts:cbgpPrefixThresholdClear.setStatus(_A)
cbgpPeer2EstablishedNotification=NotificationType((1,3,6,1,4,1,9,9,187,0,5))
cbgpPeer2EstablishedNotification.setObjects(*((_B,_M),(_B,_L)))
if mibBuilder.loadTexts:cbgpPeer2EstablishedNotification.setStatus(_A)
cbgpPeer2BackwardTransNotification=NotificationType((1,3,6,1,4,1,9,9,187,0,6))
cbgpPeer2BackwardTransNotification.setObjects(*((_B,_M),(_B,_L)))
if mibBuilder.loadTexts:cbgpPeer2BackwardTransNotification.setStatus(_A)
cbgpPeer2FsmStateChange=NotificationType((1,3,6,1,4,1,9,9,187,0,7))
cbgpPeer2FsmStateChange.setObjects(*((_B,_M),(_B,_L),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:cbgpPeer2FsmStateChange.setStatus(_A)
cbgpPeer2BackwardTransition=NotificationType((1,3,6,1,4,1,9,9,187,0,8))
cbgpPeer2BackwardTransition.setObjects(*((_B,_M),(_B,_L),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:cbgpPeer2BackwardTransition.setStatus(_A)
cbgpPeer2PrefixThresholdExceeded=NotificationType((1,3,6,1,4,1,9,9,187,0,9))
cbgpPeer2PrefixThresholdExceeded.setObjects(*((_B,_c),(_B,_m)))
if mibBuilder.loadTexts:cbgpPeer2PrefixThresholdExceeded.setStatus(_A)
cbgpPeer2PrefixThresholdClear=NotificationType((1,3,6,1,4,1,9,9,187,0,10))
cbgpPeer2PrefixThresholdClear.setObjects(*((_B,_c),(_B,_n)))
if mibBuilder.loadTexts:cbgpPeer2PrefixThresholdClear.setStatus(_A)
ciscoBgp4NotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,187,3,2,3))
ciscoBgp4NotificationsGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:ciscoBgp4NotificationsGroup.setStatus(_I)
ciscoBgp4NotificationsGroup1=NotificationGroup((1,3,6,1,4,1,9,9,187,3,2,5))
ciscoBgp4NotificationsGroup1.setObjects(*((_B,_o),(_B,_B5),(_B,_B6),(_B,_B7)))
if mibBuilder.loadTexts:ciscoBgp4NotificationsGroup1.setStatus(_A)
ciscoBgp4Peer2NotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,187,3,2,7))
ciscoBgp4Peer2NotificationsGroup.setObjects(*((_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD)))
if mibBuilder.loadTexts:ciscoBgp4Peer2NotificationsGroup.setStatus(_A)
ciscoBgp4MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,187,3,1,1))
ciscoBgp4MIBCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:ciscoBgp4MIBCompliance.setStatus(_I)
ciscoBgp4MIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,187,3,1,2))
ciscoBgp4MIBComplianceRev1.setObjects(*((_B,_V),(_B,_BE),(_B,_BF)))
if mibBuilder.loadTexts:ciscoBgp4MIBComplianceRev1.setStatus(_I)
ciscoBgp4MIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,187,3,1,3))
ciscoBgp4MIBComplianceRev2.setObjects(*((_B,_V),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoBgp4MIBComplianceRev2.setStatus(_I)
ciscoBgp4MIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,187,3,1,4))
ciscoBgp4MIBComplianceRev3.setObjects(*((_B,_V),(_B,_p),(_B,_BG),(_B,_q),(_B,_BH),(_B,_BI)))
if mibBuilder.loadTexts:ciscoBgp4MIBComplianceRev3.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CbgpSafi':CbgpSafi,'CbgpNetworkAddress':CbgpNetworkAddress,'ciscoBgp4MIB':ciscoBgp4MIB,'ciscoBgp4NotifyPrefix':ciscoBgp4NotifyPrefix,_o:cbgpFsmStateChange,_B5:cbgpBackwardTransition,_B6:cbgpPrefixThresholdExceeded,_B7:cbgpPrefixThresholdClear,_B8:cbgpPeer2EstablishedNotification,_B9:cbgpPeer2BackwardTransNotification,_BA:cbgpPeer2FsmStateChange,_BB:cbgpPeer2BackwardTransition,_BC:cbgpPeer2PrefixThresholdExceeded,_BD:cbgpPeer2PrefixThresholdClear,'ciscoBgp4MIBObjects':ciscoBgp4MIBObjects,'cbgpRoute':cbgpRoute,'cbgpRouteTable':cbgpRouteTable,'cbgpRouteEntry':cbgpRouteEntry,_s:cbgpRouteAfi,_t:cbgpRouteSafi,_u:cbgpRoutePeerType,_v:cbgpRoutePeer,_w:cbgpRouteAddrPrefix,_x:cbgpRouteAddrPrefixLen,_AA:cbgpRouteOrigin,_AB:cbgpRouteASPathSegment,_AC:cbgpRouteNextHop,_AD:cbgpRouteMedPresent,_AE:cbgpRouteMultiExitDisc,_AF:cbgpRouteLocalPrefPresent,_AG:cbgpRouteLocalPref,_AH:cbgpRouteAtomicAggregate,_AI:cbgpRouteAggregatorAS,_AJ:cbgpRouteAggregatorAddrType,_AK:cbgpRouteAggregatorAddr,_AL:cbgpRouteBest,_AM:cbgpRouteUnknownAttr,'cbgpPeer':cbgpPeer,'cbgpPeerTable':cbgpPeerTable,_A9:cbgpPeerEntry,_AN:cbgpPeerPrefixAccepted,_AO:cbgpPeerPrefixDenied,_AP:cbgpPeerPrefixLimit,_AQ:cbgpPeerPrefixAdvertised,_AR:cbgpPeerPrefixSuppressed,_AS:cbgpPeerPrefixWithdrawn,_Y:cbgpPeerLastErrorTxt,_X:cbgpPeerPrevState,'cbgpPeerCapsTable':cbgpPeerCapsTable,'cbgpPeerCapsEntry':cbgpPeerCapsEntry,_y:cbgpPeerCapCode,_z:cbgpPeerCapIndex,_AT:cbgpPeerCapValue,'cbgpPeerAddrFamilyTable':cbgpPeerAddrFamilyTable,'cbgpPeerAddrFamilyEntry':cbgpPeerAddrFamilyEntry,_g:cbgpPeerAddrFamilyAfi,_h:cbgpPeerAddrFamilySafi,_AU:cbgpPeerAddrFamilyName,'cbgpPeerAddrFamilyPrefixTable':cbgpPeerAddrFamilyPrefixTable,'cbgpPeerAddrFamilyPrefixEntry':cbgpPeerAddrFamilyPrefixEntry,_AV:cbgpPeerAcceptedPrefixes,_AW:cbgpPeerDeniedPrefixes,_Z:cbgpPeerPrefixAdminLimit,_k:cbgpPeerPrefixThreshold,_l:cbgpPeerPrefixClearThreshold,_AX:cbgpPeerAdvertisedPrefixes,_AY:cbgpPeerSuppressedPrefixes,_AZ:cbgpPeerWithdrawnPrefixes,'cbgpPeer2Table':cbgpPeer2Table,'cbgpPeer2Entry':cbgpPeer2Entry,_T:cbgpPeer2Type,_U:cbgpPeer2RemoteAddr,_L:cbgpPeer2State,_Aa:cbgpPeer2AdminStatus,_Ab:cbgpPeer2NegotiatedVersion,_Ac:cbgpPeer2LocalAddr,_Ad:cbgpPeer2LocalPort,_Ae:cbgpPeer2LocalAs,_Af:cbgpPeer2LocalIdentifier,_Ag:cbgpPeer2RemotePort,_Ah:cbgpPeer2RemoteAs,_Ai:cbgpPeer2RemoteIdentifier,_Aj:cbgpPeer2InUpdates,_Ak:cbgpPeer2OutUpdates,_Al:cbgpPeer2InTotalMessages,_Am:cbgpPeer2OutTotalMessages,_M:cbgpPeer2LastError,_An:cbgpPeer2FsmEstablishedTransitions,_Ao:cbgpPeer2FsmEstablishedTime,_Ap:cbgpPeer2ConnectRetryInterval,_Aq:cbgpPeer2HoldTime,_Ar:cbgpPeer2KeepAlive,_As:cbgpPeer2HoldTimeConfigured,_At:cbgpPeer2KeepAliveConfigured,_Au:cbgpPeer2MinASOriginationInterval,_Av:cbgpPeer2MinRouteAdvertisementInterval,_Aw:cbgpPeer2InUpdateElapsedTime,_a:cbgpPeer2LastErrorTxt,_b:cbgpPeer2PrevState,'cbgpPeer2CapsTable':cbgpPeer2CapsTable,'cbgpPeer2CapsEntry':cbgpPeer2CapsEntry,_A4:cbgpPeer2CapCode,_A5:cbgpPeer2CapIndex,_Ax:cbgpPeer2CapValue,'cbgpPeer2AddrFamilyTable':cbgpPeer2AddrFamilyTable,'cbgpPeer2AddrFamilyEntry':cbgpPeer2AddrFamilyEntry,_i:cbgpPeer2AddrFamilyAfi,_j:cbgpPeer2AddrFamilySafi,_Ay:cbgpPeer2AddrFamilyName,'cbgpPeer2AddrFamilyPrefixTable':cbgpPeer2AddrFamilyPrefixTable,'cbgpPeer2AddrFamilyPrefixEntry':cbgpPeer2AddrFamilyPrefixEntry,_Az:cbgpPeer2AcceptedPrefixes,_A_:cbgpPeer2DeniedPrefixes,_c:cbgpPeer2PrefixAdminLimit,_m:cbgpPeer2PrefixThreshold,_n:cbgpPeer2PrefixClearThreshold,_B0:cbgpPeer2AdvertisedPrefixes,_B1:cbgpPeer2SuppressedPrefixes,_B2:cbgpPeer2WithdrawnPrefixes,'cbgpPeer3Table':cbgpPeer3Table,'cbgpPeer3Entry':cbgpPeer3Entry,_A6:cbgpPeer3VrfId,_A7:cbgpPeer3Type,_A8:cbgpPeer3RemoteAddr,'cbgpPeer3VrfName':cbgpPeer3VrfName,'cbgpPeer3State':cbgpPeer3State,'cbgpPeer3AdminStatus':cbgpPeer3AdminStatus,'cbgpPeer3NegotiatedVersion':cbgpPeer3NegotiatedVersion,'cbgpPeer3LocalAddr':cbgpPeer3LocalAddr,'cbgpPeer3LocalPort':cbgpPeer3LocalPort,'cbgpPeer3LocalAs':cbgpPeer3LocalAs,'cbgpPeer3LocalIdentifier':cbgpPeer3LocalIdentifier,'cbgpPeer3RemotePort':cbgpPeer3RemotePort,'cbgpPeer3RemoteAs':cbgpPeer3RemoteAs,'cbgpPeer3RemoteIdentifier':cbgpPeer3RemoteIdentifier,'cbgpPeer3InUpdates':cbgpPeer3InUpdates,'cbgpPeer3OutUpdates':cbgpPeer3OutUpdates,'cbgpPeer3InTotalMessages':cbgpPeer3InTotalMessages,'cbgpPeer3OutTotalMessages':cbgpPeer3OutTotalMessages,'cbgpPeer3LastError':cbgpPeer3LastError,'cbgpPeer3FsmEstablishedTransitions':cbgpPeer3FsmEstablishedTransitions,'cbgpPeer3FsmEstablishedTime':cbgpPeer3FsmEstablishedTime,'cbgpPeer3ConnectRetryInterval':cbgpPeer3ConnectRetryInterval,'cbgpPeer3HoldTime':cbgpPeer3HoldTime,'cbgpPeer3KeepAlive':cbgpPeer3KeepAlive,'cbgpPeer3HoldTimeConfigured':cbgpPeer3HoldTimeConfigured,'cbgpPeer3KeepAliveConfigured':cbgpPeer3KeepAliveConfigured,'cbgpPeer3MinASOriginationInterval':cbgpPeer3MinASOriginationInterval,'cbgpPeer3MinRouteAdvertisementInterval':cbgpPeer3MinRouteAdvertisementInterval,'cbgpPeer3InUpdateElapsedTime':cbgpPeer3InUpdateElapsedTime,'cbgpPeer3LastErrorTxt':cbgpPeer3LastErrorTxt,'cbgpPeer3PrevState':cbgpPeer3PrevState,'cbgpGlobal':cbgpGlobal,_B3:cbgpNotifsEnable,_B4:cbgpLocalAs,'ciscoBgp4NotificationPrefix':ciscoBgp4NotificationPrefix,'ciscoBgp4MIBConformance':ciscoBgp4MIBConformance,'ciscoBgp4MIBCompliances':ciscoBgp4MIBCompliances,'ciscoBgp4MIBCompliance':ciscoBgp4MIBCompliance,'ciscoBgp4MIBComplianceRev1':ciscoBgp4MIBComplianceRev1,'ciscoBgp4MIBComplianceRev2':ciscoBgp4MIBComplianceRev2,'ciscoBgp4MIBComplianceRev3':ciscoBgp4MIBComplianceRev3,'ciscoBgp4MIBGroups':ciscoBgp4MIBGroups,_V:ciscoBgp4RouteGroup,_BE:ciscoBgp4PeerGroup,_BF:ciscoBgp4NotificationsGroup,_p:ciscoBgp4PeerGroup1,_q:ciscoBgp4NotificationsGroup1,_BH:ciscoBgp4Peer2Group,_BI:ciscoBgp4Peer2NotificationsGroup,_BG:ciscoBgp4GlobalGroup})