_At='vceArpGroup'
_As='vcePathGroup'
_Ar='vceLinkGroup'
_Aq='vceHealthGroup'
_Ap='vceHaGroup'
_Ao='vceArpState'
_An='vceArpCtag'
_Am='vceArpStag'
_Al='vceArpMac'
_Ak='vceArpNum'
_Aj='vcePathTxJitterGauge'
_Ai='vcePathRxJitterGauge'
_Ah='vcePathTxLostPktGauge'
_Ag='vcePathRxLostPktGauge'
_Af='vcePathTxJitter'
_Ae='vcePathRxJitter'
_Ad='vcePathTxPkt'
_Ac='vcePathRxPkt'
_Ab='vcePathTxLostPkt'
_Aa='vcePathRxLostPkt'
_AZ='vcePathTxBytes'
_AY='vcePathRxBytes'
_AX='vcePathRxAveLatency'
_AW='vcePathTxAveLatency'
_AV='vcePathTunlMode'
_AU='vcePathTxState'
_AT='vcePathRxState'
_AS='vcePathUpTime'
_AR='vcePathState'
_AQ='vcePathPeerName'
_AP='vcePathIp'
_AO='vcePathIpType'
_AN='vcePathNum'
_AM='vceLinkRxLostPktGauge'
_AL='vceLinkTxLostPktGauge'
_AK='vceLinkRxLatencyGauge'
_AJ='vceLinkTxLatencyGauge'
_AI='vceLinkRxJitterGauge'
_AH='vceLinkTxJitterGauge'
_AG='vceLinkNextHop'
_AF='vceLinkNextHopType'
_AE='vceLinkIf'
_AD='vceLinkTotRxBytes'
_AC='vceLinkTotTxbytes'
_AB='vceLinkTotRxPkts'
_AA='vceLinkTotTxPkts'
_A9='vceLinkVeloSvcReachable'
_A8='vceLinkState'
_A7='vceLinkItf'
_A6='vceLinkMtu'
_A5='vceLinkVlanId'
_A4='vceLinkLocalIp'
_A3='vceLinkLocalIpType'
_A2='vceLinkPublicIp'
_A1='vceLinkPublicIpType'
_A0='vceLinkRxLostPkt'
_z='vceLinkTxLostPkt'
_y='vceLinkRxLatency'
_x='vceLinkTxLatency'
_w='vceLinkRxJitter'
_v='vceLinkTxJitter'
_u='vceLinkRxCtlBytes'
_t='vceLinkTxCtlBytes'
_s='vceLinkRxCtlPkt'
_r='vceLinkTxCtlPkt'
_q='vceLinkRxP3Bytes'
_p='vceLinkTxP3Bytes'
_o='vceLinkRxP3Pkt'
_n='vceLinkTxP3Pkt'
_m='vceLinkRxP2Bytes'
_l='vceLinkTxP2Bytes'
_k='vceLinkRxP2Pkt'
_j='vceLinkTxP2Pkt'
_i='vceLinkRxP1Bytes'
_h='vceLinkTxP1Bytes'
_g='vceLinkRxP1Pkt'
_f='vceLinkTxP1Pkt'
_e='vceLinkName'
_d='vceLinkNum'
_c='vceMemUsedPct'
_b='vceCpuUtilPct30sec'
_a='vceCpuUtilPct5min'
_Z='vceHaStanbyLanItfNum'
_Y='vceHaStanbyWanItfNum'
_X='vceHaActiveLanItfNum'
_W='vceHaActiveWanItfNum'
_V='vceHaPeerState'
_U='vceHaAdminState'
_T='vceArpIpAddr'
_S='vceArpIpAddrType'
_R='vceArpItf'
_Q='vcePathGwAddr'
_P='vcePathGwAddrType'
_O='vcePathIfIntId'
_N='vceLinkIntId'
_M='stable'
_L='unstable'
_K='unusable'
_J='initial'
_I='standby'
_H='active'
_G='PhysAddress'
_F='unknown'
_E='not-accessible'
_D='deprecated'
_C='read-only'
_B='VELOCLOUD-EDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_G,'TextualConvention','TruthValue')
UUID,=mibBuilder.importSymbols('UUID-TC-MIB','UUID')
modules,=mibBuilder.importSymbols('VELOCLOUD-MIB','modules')
edge=ModuleIdentity((1,3,6,1,4,1,45346,1,1))
if mibBuilder.loadTexts:edge.setRevisions(('2021-08-31 00:00','2021-07-14 00:00','2021-05-10 00:00','2019-08-02 00:00','2017-01-18 00:00','2017-01-13 00:00'))
class VceHaAdminStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('theVelocloudActiveStandbyPair',2),('theVeloCloudCluster',3),('nonVeloCloudVrrpPair',4),(_F,5)))
class VceHaPeerStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initializing',1),(_H,2),(_I,3),(_F,4)))
class VceLinkStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),('dead',2),(_K,3),('quiet',4),(_I,5),(_L,6),(_M,7),(_F,8)))
class VcePathStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_J,1),('dead',2),(_K,3),('quiet',4),(_L,5),('bwUnmeasurable',6),('waitingForLinkbw',7),('measuringTxBw',8),('measuringRxBw',9),(_M,10),(_H,11),('upHsby',12),('idleHsby',13),('backup',14),(_F,15)))
class VcePathTunlModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('default',1),('trusted',2),('untrustedTransport',3),('untrustedTunnel',4),(_F,5)))
class VceArpStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,7)));namedValues=NamedValues(*(('reachable',1),('stale',2),('invalid',5),(_F,6),('incomplete',7)))
_VceEdgeObject_ObjectIdentity=ObjectIdentity
vceEdgeObject=_VceEdgeObject_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2))
_VceHA_ObjectIdentity=ObjectIdentity
vceHA=_VceHA_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,1))
_VceHAObject_ObjectIdentity=ObjectIdentity
vceHAObject=_VceHAObject_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,1,2))
_VceHaAdminState_Type=VceHaAdminStateType
_VceHaAdminState_Object=MibScalar
vceHaAdminState=_VceHaAdminState_Object((1,3,6,1,4,1,45346,1,1,2,1,2,1),_VceHaAdminState_Type())
vceHaAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vceHaAdminState.setStatus(_A)
_VceHaPeerState_Type=VceHaPeerStateType
_VceHaPeerState_Object=MibScalar
vceHaPeerState=_VceHaPeerState_Object((1,3,6,1,4,1,45346,1,1,2,1,2,2),_VceHaPeerState_Type())
vceHaPeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:vceHaPeerState.setStatus(_A)
_VceHaActiveWanItfNum_Type=Integer32
_VceHaActiveWanItfNum_Object=MibScalar
vceHaActiveWanItfNum=_VceHaActiveWanItfNum_Object((1,3,6,1,4,1,45346,1,1,2,1,2,3),_VceHaActiveWanItfNum_Type())
vceHaActiveWanItfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vceHaActiveWanItfNum.setStatus(_A)
_VceHaActiveLanItfNum_Type=Integer32
_VceHaActiveLanItfNum_Object=MibScalar
vceHaActiveLanItfNum=_VceHaActiveLanItfNum_Object((1,3,6,1,4,1,45346,1,1,2,1,2,4),_VceHaActiveLanItfNum_Type())
vceHaActiveLanItfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vceHaActiveLanItfNum.setStatus(_A)
_VceHaStanbyWanItfNum_Type=Integer32
_VceHaStanbyWanItfNum_Object=MibScalar
vceHaStanbyWanItfNum=_VceHaStanbyWanItfNum_Object((1,3,6,1,4,1,45346,1,1,2,1,2,5),_VceHaStanbyWanItfNum_Type())
vceHaStanbyWanItfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vceHaStanbyWanItfNum.setStatus(_A)
_VceHaStanbyLanItfNum_Type=Integer32
_VceHaStanbyLanItfNum_Object=MibScalar
vceHaStanbyLanItfNum=_VceHaStanbyLanItfNum_Object((1,3,6,1,4,1,45346,1,1,2,1,2,6),_VceHaStanbyLanItfNum_Type())
vceHaStanbyLanItfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vceHaStanbyLanItfNum.setStatus(_A)
_VceHealth_ObjectIdentity=ObjectIdentity
vceHealth=_VceHealth_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,2))
_VceHealthObject_ObjectIdentity=ObjectIdentity
vceHealthObject=_VceHealthObject_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,2,2))
_VceCpuUtilPct5min_Type=Integer32
_VceCpuUtilPct5min_Object=MibScalar
vceCpuUtilPct5min=_VceCpuUtilPct5min_Object((1,3,6,1,4,1,45346,1,1,2,2,2,1),_VceCpuUtilPct5min_Type())
vceCpuUtilPct5min.setMaxAccess(_C)
if mibBuilder.loadTexts:vceCpuUtilPct5min.setStatus(_A)
_VceCpuUtilPct30sec_Type=Integer32
_VceCpuUtilPct30sec_Object=MibScalar
vceCpuUtilPct30sec=_VceCpuUtilPct30sec_Object((1,3,6,1,4,1,45346,1,1,2,2,2,2),_VceCpuUtilPct30sec_Type())
vceCpuUtilPct30sec.setMaxAccess(_C)
if mibBuilder.loadTexts:vceCpuUtilPct30sec.setStatus(_A)
_VceMemUsedPct_Type=Integer32
_VceMemUsedPct_Object=MibScalar
vceMemUsedPct=_VceMemUsedPct_Object((1,3,6,1,4,1,45346,1,1,2,2,2,3),_VceMemUsedPct_Type())
vceMemUsedPct.setMaxAccess(_C)
if mibBuilder.loadTexts:vceMemUsedPct.setStatus(_A)
_VceLink_ObjectIdentity=ObjectIdentity
vceLink=_VceLink_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,3))
_VceLinkObject_ObjectIdentity=ObjectIdentity
vceLinkObject=_VceLinkObject_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,3,2))
_VceLinkNum_Type=Integer32
_VceLinkNum_Object=MibScalar
vceLinkNum=_VceLinkNum_Object((1,3,6,1,4,1,45346,1,1,2,3,2,1),_VceLinkNum_Type())
vceLinkNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkNum.setStatus(_A)
_VceLinkTable_Object=MibTable
vceLinkTable=_VceLinkTable_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2))
if mibBuilder.loadTexts:vceLinkTable.setStatus(_A)
_VceLinkEntry_Object=MibTableRow
vceLinkEntry=_VceLinkEntry_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1))
vceLinkEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:vceLinkEntry.setStatus(_A)
_VceLinkIntId_Type=UUID
_VceLinkIntId_Object=MibTableColumn
vceLinkIntId=_VceLinkIntId_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,2),_VceLinkIntId_Type())
vceLinkIntId.setMaxAccess(_E)
if mibBuilder.loadTexts:vceLinkIntId.setStatus(_A)
_VceLinkName_Type=DisplayString
_VceLinkName_Object=MibTableColumn
vceLinkName=_VceLinkName_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,3),_VceLinkName_Type())
vceLinkName.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkName.setStatus(_A)
_VceLinkTxP1Pkt_Type=Counter64
_VceLinkTxP1Pkt_Object=MibTableColumn
vceLinkTxP1Pkt=_VceLinkTxP1Pkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,4),_VceLinkTxP1Pkt_Type())
vceLinkTxP1Pkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxP1Pkt.setStatus(_A)
_VceLinkRxP1Pkt_Type=Counter64
_VceLinkRxP1Pkt_Object=MibTableColumn
vceLinkRxP1Pkt=_VceLinkRxP1Pkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,5),_VceLinkRxP1Pkt_Type())
vceLinkRxP1Pkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxP1Pkt.setStatus(_A)
_VceLinkTxP1Bytes_Type=Counter64
_VceLinkTxP1Bytes_Object=MibTableColumn
vceLinkTxP1Bytes=_VceLinkTxP1Bytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,6),_VceLinkTxP1Bytes_Type())
vceLinkTxP1Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxP1Bytes.setStatus(_A)
_VceLinkRxP1Bytes_Type=Counter64
_VceLinkRxP1Bytes_Object=MibTableColumn
vceLinkRxP1Bytes=_VceLinkRxP1Bytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,7),_VceLinkRxP1Bytes_Type())
vceLinkRxP1Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxP1Bytes.setStatus(_A)
_VceLinkTxP2Pkt_Type=Counter64
_VceLinkTxP2Pkt_Object=MibTableColumn
vceLinkTxP2Pkt=_VceLinkTxP2Pkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,8),_VceLinkTxP2Pkt_Type())
vceLinkTxP2Pkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxP2Pkt.setStatus(_A)
_VceLinkRxP2Pkt_Type=Counter64
_VceLinkRxP2Pkt_Object=MibTableColumn
vceLinkRxP2Pkt=_VceLinkRxP2Pkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,9),_VceLinkRxP2Pkt_Type())
vceLinkRxP2Pkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxP2Pkt.setStatus(_A)
_VceLinkTxP2Bytes_Type=Counter64
_VceLinkTxP2Bytes_Object=MibTableColumn
vceLinkTxP2Bytes=_VceLinkTxP2Bytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,10),_VceLinkTxP2Bytes_Type())
vceLinkTxP2Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxP2Bytes.setStatus(_A)
_VceLinkRxP2Bytes_Type=Counter64
_VceLinkRxP2Bytes_Object=MibTableColumn
vceLinkRxP2Bytes=_VceLinkRxP2Bytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,11),_VceLinkRxP2Bytes_Type())
vceLinkRxP2Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxP2Bytes.setStatus(_A)
_VceLinkTxP3Pkt_Type=Counter64
_VceLinkTxP3Pkt_Object=MibTableColumn
vceLinkTxP3Pkt=_VceLinkTxP3Pkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,12),_VceLinkTxP3Pkt_Type())
vceLinkTxP3Pkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxP3Pkt.setStatus(_A)
_VceLinkRxP3Pkt_Type=Counter64
_VceLinkRxP3Pkt_Object=MibTableColumn
vceLinkRxP3Pkt=_VceLinkRxP3Pkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,13),_VceLinkRxP3Pkt_Type())
vceLinkRxP3Pkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxP3Pkt.setStatus(_A)
_VceLinkTxP3Bytes_Type=Counter64
_VceLinkTxP3Bytes_Object=MibTableColumn
vceLinkTxP3Bytes=_VceLinkTxP3Bytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,14),_VceLinkTxP3Bytes_Type())
vceLinkTxP3Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxP3Bytes.setStatus(_A)
_VceLinkRxP3Bytes_Type=Counter64
_VceLinkRxP3Bytes_Object=MibTableColumn
vceLinkRxP3Bytes=_VceLinkRxP3Bytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,15),_VceLinkRxP3Bytes_Type())
vceLinkRxP3Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxP3Bytes.setStatus(_A)
_VceLinkTxCtlPkt_Type=Counter64
_VceLinkTxCtlPkt_Object=MibTableColumn
vceLinkTxCtlPkt=_VceLinkTxCtlPkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,16),_VceLinkTxCtlPkt_Type())
vceLinkTxCtlPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxCtlPkt.setStatus(_A)
_VceLinkRxCtlPkt_Type=Counter64
_VceLinkRxCtlPkt_Object=MibTableColumn
vceLinkRxCtlPkt=_VceLinkRxCtlPkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,17),_VceLinkRxCtlPkt_Type())
vceLinkRxCtlPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxCtlPkt.setStatus(_A)
_VceLinkTxCtlBytes_Type=Counter64
_VceLinkTxCtlBytes_Object=MibTableColumn
vceLinkTxCtlBytes=_VceLinkTxCtlBytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,18),_VceLinkTxCtlBytes_Type())
vceLinkTxCtlBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxCtlBytes.setStatus(_A)
_VceLinkRxCtlBytes_Type=Counter64
_VceLinkRxCtlBytes_Object=MibTableColumn
vceLinkRxCtlBytes=_VceLinkRxCtlBytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,19),_VceLinkRxCtlBytes_Type())
vceLinkRxCtlBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxCtlBytes.setStatus(_A)
_VceLinkTxJitter_Type=Counter64
_VceLinkTxJitter_Object=MibTableColumn
vceLinkTxJitter=_VceLinkTxJitter_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,20),_VceLinkTxJitter_Type())
vceLinkTxJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxJitter.setStatus(_D)
_VceLinkRxJitter_Type=Counter64
_VceLinkRxJitter_Object=MibTableColumn
vceLinkRxJitter=_VceLinkRxJitter_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,21),_VceLinkRxJitter_Type())
vceLinkRxJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxJitter.setStatus(_D)
_VceLinkTxLatency_Type=Counter64
_VceLinkTxLatency_Object=MibTableColumn
vceLinkTxLatency=_VceLinkTxLatency_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,22),_VceLinkTxLatency_Type())
vceLinkTxLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxLatency.setStatus(_D)
_VceLinkRxLatency_Type=Counter64
_VceLinkRxLatency_Object=MibTableColumn
vceLinkRxLatency=_VceLinkRxLatency_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,23),_VceLinkRxLatency_Type())
vceLinkRxLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxLatency.setStatus(_D)
_VceLinkTxLostPkt_Type=Counter64
_VceLinkTxLostPkt_Object=MibTableColumn
vceLinkTxLostPkt=_VceLinkTxLostPkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,24),_VceLinkTxLostPkt_Type())
vceLinkTxLostPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxLostPkt.setStatus(_D)
_VceLinkRxLostPkt_Type=Counter64
_VceLinkRxLostPkt_Object=MibTableColumn
vceLinkRxLostPkt=_VceLinkRxLostPkt_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,25),_VceLinkRxLostPkt_Type())
vceLinkRxLostPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxLostPkt.setStatus(_D)
_VceLinkPublicIpType_Type=InetAddressType
_VceLinkPublicIpType_Object=MibTableColumn
vceLinkPublicIpType=_VceLinkPublicIpType_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,27),_VceLinkPublicIpType_Type())
vceLinkPublicIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkPublicIpType.setStatus(_A)
_VceLinkPublicIp_Type=InetAddress
_VceLinkPublicIp_Object=MibTableColumn
vceLinkPublicIp=_VceLinkPublicIp_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,28),_VceLinkPublicIp_Type())
vceLinkPublicIp.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkPublicIp.setStatus(_A)
_VceLinkLocalIpType_Type=InetAddressType
_VceLinkLocalIpType_Object=MibTableColumn
vceLinkLocalIpType=_VceLinkLocalIpType_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,29),_VceLinkLocalIpType_Type())
vceLinkLocalIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkLocalIpType.setStatus(_A)
_VceLinkLocalIp_Type=InetAddress
_VceLinkLocalIp_Object=MibTableColumn
vceLinkLocalIp=_VceLinkLocalIp_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,30),_VceLinkLocalIp_Type())
vceLinkLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkLocalIp.setStatus(_A)
_VceLinkVlanId_Type=Integer32
_VceLinkVlanId_Object=MibTableColumn
vceLinkVlanId=_VceLinkVlanId_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,31),_VceLinkVlanId_Type())
vceLinkVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkVlanId.setStatus(_A)
_VceLinkMtu_Type=Integer32
_VceLinkMtu_Object=MibTableColumn
vceLinkMtu=_VceLinkMtu_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,32),_VceLinkMtu_Type())
vceLinkMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkMtu.setStatus(_A)
_VceLinkItf_Type=DisplayString
_VceLinkItf_Object=MibTableColumn
vceLinkItf=_VceLinkItf_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,33),_VceLinkItf_Type())
vceLinkItf.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkItf.setStatus(_A)
_VceLinkState_Type=VceLinkStateType
_VceLinkState_Object=MibTableColumn
vceLinkState=_VceLinkState_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,34),_VceLinkState_Type())
vceLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkState.setStatus(_A)
_VceLinkVeloSvcReachable_Type=TruthValue
_VceLinkVeloSvcReachable_Object=MibTableColumn
vceLinkVeloSvcReachable=_VceLinkVeloSvcReachable_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,35),_VceLinkVeloSvcReachable_Type())
vceLinkVeloSvcReachable.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkVeloSvcReachable.setStatus(_A)
_VceLinkTotTxPkts_Type=Counter64
_VceLinkTotTxPkts_Object=MibTableColumn
vceLinkTotTxPkts=_VceLinkTotTxPkts_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,36),_VceLinkTotTxPkts_Type())
vceLinkTotTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTotTxPkts.setStatus(_A)
_VceLinkTotRxPkts_Type=Counter64
_VceLinkTotRxPkts_Object=MibTableColumn
vceLinkTotRxPkts=_VceLinkTotRxPkts_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,37),_VceLinkTotRxPkts_Type())
vceLinkTotRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTotRxPkts.setStatus(_A)
_VceLinkTotTxbytes_Type=Counter64
_VceLinkTotTxbytes_Object=MibTableColumn
vceLinkTotTxbytes=_VceLinkTotTxbytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,38),_VceLinkTotTxbytes_Type())
vceLinkTotTxbytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTotTxbytes.setStatus(_A)
_VceLinkTotRxBytes_Type=Counter64
_VceLinkTotRxBytes_Object=MibTableColumn
vceLinkTotRxBytes=_VceLinkTotRxBytes_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,39),_VceLinkTotRxBytes_Type())
vceLinkTotRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTotRxBytes.setStatus(_A)
_VceLinkIf_Type=InterfaceIndex
_VceLinkIf_Object=MibTableColumn
vceLinkIf=_VceLinkIf_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,40),_VceLinkIf_Type())
vceLinkIf.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkIf.setStatus(_A)
_VceLinkNextHopType_Type=InetAddressType
_VceLinkNextHopType_Object=MibTableColumn
vceLinkNextHopType=_VceLinkNextHopType_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,41),_VceLinkNextHopType_Type())
vceLinkNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkNextHopType.setStatus(_A)
_VceLinkNextHop_Type=InetAddress
_VceLinkNextHop_Object=MibTableColumn
vceLinkNextHop=_VceLinkNextHop_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,42),_VceLinkNextHop_Type())
vceLinkNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkNextHop.setStatus(_A)
_VceLinkTxJitterGauge_Type=Gauge32
_VceLinkTxJitterGauge_Object=MibTableColumn
vceLinkTxJitterGauge=_VceLinkTxJitterGauge_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,43),_VceLinkTxJitterGauge_Type())
vceLinkTxJitterGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxJitterGauge.setStatus(_A)
_VceLinkRxJitterGauge_Type=Gauge32
_VceLinkRxJitterGauge_Object=MibTableColumn
vceLinkRxJitterGauge=_VceLinkRxJitterGauge_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,44),_VceLinkRxJitterGauge_Type())
vceLinkRxJitterGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxJitterGauge.setStatus(_A)
_VceLinkTxLatencyGauge_Type=Gauge32
_VceLinkTxLatencyGauge_Object=MibTableColumn
vceLinkTxLatencyGauge=_VceLinkTxLatencyGauge_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,45),_VceLinkTxLatencyGauge_Type())
vceLinkTxLatencyGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxLatencyGauge.setStatus(_A)
_VceLinkRxLatencyGauge_Type=Gauge32
_VceLinkRxLatencyGauge_Object=MibTableColumn
vceLinkRxLatencyGauge=_VceLinkRxLatencyGauge_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,46),_VceLinkRxLatencyGauge_Type())
vceLinkRxLatencyGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxLatencyGauge.setStatus(_A)
_VceLinkTxLostPktGauge_Type=Gauge32
_VceLinkTxLostPktGauge_Object=MibTableColumn
vceLinkTxLostPktGauge=_VceLinkTxLostPktGauge_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,47),_VceLinkTxLostPktGauge_Type())
vceLinkTxLostPktGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkTxLostPktGauge.setStatus(_A)
_VceLinkRxLostPktGauge_Type=Gauge32
_VceLinkRxLostPktGauge_Object=MibTableColumn
vceLinkRxLostPktGauge=_VceLinkRxLostPktGauge_Object((1,3,6,1,4,1,45346,1,1,2,3,2,2,1,48),_VceLinkRxLostPktGauge_Type())
vceLinkRxLostPktGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vceLinkRxLostPktGauge.setStatus(_A)
_VcePath_ObjectIdentity=ObjectIdentity
vcePath=_VcePath_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,4))
_VcePathObject_ObjectIdentity=ObjectIdentity
vcePathObject=_VcePathObject_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,4,2))
_VcePathNum_Type=Integer32
_VcePathNum_Object=MibScalar
vcePathNum=_VcePathNum_Object((1,3,6,1,4,1,45346,1,1,2,4,2,1),_VcePathNum_Type())
vcePathNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathNum.setStatus(_A)
_VcePathTable_Object=MibTable
vcePathTable=_VcePathTable_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2))
if mibBuilder.loadTexts:vcePathTable.setStatus(_A)
_VcePathEntry_Object=MibTableRow
vcePathEntry=_VcePathEntry_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1))
vcePathEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:vcePathEntry.setStatus(_A)
_VcePathIfIntId_Type=UUID
_VcePathIfIntId_Object=MibTableColumn
vcePathIfIntId=_VcePathIfIntId_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,1),_VcePathIfIntId_Type())
vcePathIfIntId.setMaxAccess(_E)
if mibBuilder.loadTexts:vcePathIfIntId.setStatus(_A)
_VcePathIpType_Type=InetAddressType
_VcePathIpType_Object=MibTableColumn
vcePathIpType=_VcePathIpType_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,2),_VcePathIpType_Type())
vcePathIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathIpType.setStatus(_A)
_VcePathIp_Type=InetAddress
_VcePathIp_Object=MibTableColumn
vcePathIp=_VcePathIp_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,3),_VcePathIp_Type())
vcePathIp.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathIp.setStatus(_A)
_VcePathGwAddrType_Type=InetAddressType
_VcePathGwAddrType_Object=MibTableColumn
vcePathGwAddrType=_VcePathGwAddrType_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,4),_VcePathGwAddrType_Type())
vcePathGwAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:vcePathGwAddrType.setStatus(_A)
_VcePathGwAddr_Type=InetAddress
_VcePathGwAddr_Object=MibTableColumn
vcePathGwAddr=_VcePathGwAddr_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,5),_VcePathGwAddr_Type())
vcePathGwAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:vcePathGwAddr.setStatus(_A)
_VcePathPeerName_Type=DisplayString
_VcePathPeerName_Object=MibTableColumn
vcePathPeerName=_VcePathPeerName_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,6),_VcePathPeerName_Type())
vcePathPeerName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathPeerName.setStatus(_A)
_VcePathState_Type=VcePathStateType
_VcePathState_Object=MibTableColumn
vcePathState=_VcePathState_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,7),_VcePathState_Type())
vcePathState.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathState.setStatus(_A)
_VcePathUpTime_Type=TimeTicks
_VcePathUpTime_Object=MibTableColumn
vcePathUpTime=_VcePathUpTime_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,8),_VcePathUpTime_Type())
vcePathUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathUpTime.setStatus(_A)
_VcePathRxState_Type=VcePathStateType
_VcePathRxState_Object=MibTableColumn
vcePathRxState=_VcePathRxState_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,10),_VcePathRxState_Type())
vcePathRxState.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathRxState.setStatus(_A)
_VcePathTxState_Type=VcePathStateType
_VcePathTxState_Object=MibTableColumn
vcePathTxState=_VcePathTxState_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,11),_VcePathTxState_Type())
vcePathTxState.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathTxState.setStatus(_A)
_VcePathTunlMode_Type=VcePathTunlModeType
_VcePathTunlMode_Object=MibTableColumn
vcePathTunlMode=_VcePathTunlMode_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,12),_VcePathTunlMode_Type())
vcePathTunlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathTunlMode.setStatus(_A)
_VcePathTxAveLatency_Type=Integer32
_VcePathTxAveLatency_Object=MibTableColumn
vcePathTxAveLatency=_VcePathTxAveLatency_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,13),_VcePathTxAveLatency_Type())
vcePathTxAveLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathTxAveLatency.setStatus(_A)
_VcePathRxAveLatency_Type=Integer32
_VcePathRxAveLatency_Object=MibTableColumn
vcePathRxAveLatency=_VcePathRxAveLatency_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,14),_VcePathRxAveLatency_Type())
vcePathRxAveLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathRxAveLatency.setStatus(_A)
_VcePathRxBytes_Type=Counter64
_VcePathRxBytes_Object=MibTableColumn
vcePathRxBytes=_VcePathRxBytes_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,15),_VcePathRxBytes_Type())
vcePathRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathRxBytes.setStatus(_A)
_VcePathTxBytes_Type=Counter64
_VcePathTxBytes_Object=MibTableColumn
vcePathTxBytes=_VcePathTxBytes_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,16),_VcePathTxBytes_Type())
vcePathTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathTxBytes.setStatus(_A)
_VcePathRxLostPkt_Type=Counter64
_VcePathRxLostPkt_Object=MibTableColumn
vcePathRxLostPkt=_VcePathRxLostPkt_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,17),_VcePathRxLostPkt_Type())
vcePathRxLostPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathRxLostPkt.setStatus(_D)
_VcePathTxLostPkt_Type=Counter64
_VcePathTxLostPkt_Object=MibTableColumn
vcePathTxLostPkt=_VcePathTxLostPkt_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,18),_VcePathTxLostPkt_Type())
vcePathTxLostPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathTxLostPkt.setStatus(_D)
_VcePathRxPkt_Type=Counter64
_VcePathRxPkt_Object=MibTableColumn
vcePathRxPkt=_VcePathRxPkt_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,19),_VcePathRxPkt_Type())
vcePathRxPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathRxPkt.setStatus(_A)
_VcePathTxPkt_Type=Counter64
_VcePathTxPkt_Object=MibTableColumn
vcePathTxPkt=_VcePathTxPkt_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,20),_VcePathTxPkt_Type())
vcePathTxPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathTxPkt.setStatus(_A)
_VcePathRxJitter_Type=Counter64
_VcePathRxJitter_Object=MibTableColumn
vcePathRxJitter=_VcePathRxJitter_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,21),_VcePathRxJitter_Type())
vcePathRxJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathRxJitter.setStatus(_D)
_VcePathTxJitter_Type=Counter64
_VcePathTxJitter_Object=MibTableColumn
vcePathTxJitter=_VcePathTxJitter_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,22),_VcePathTxJitter_Type())
vcePathTxJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathTxJitter.setStatus(_D)
_VcePathRxLostPktGauge_Type=Gauge32
_VcePathRxLostPktGauge_Object=MibTableColumn
vcePathRxLostPktGauge=_VcePathRxLostPktGauge_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,23),_VcePathRxLostPktGauge_Type())
vcePathRxLostPktGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathRxLostPktGauge.setStatus(_A)
_VcePathTxLostPktGauge_Type=Gauge32
_VcePathTxLostPktGauge_Object=MibTableColumn
vcePathTxLostPktGauge=_VcePathTxLostPktGauge_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,24),_VcePathTxLostPktGauge_Type())
vcePathTxLostPktGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathTxLostPktGauge.setStatus(_A)
_VcePathRxJitterGauge_Type=Gauge32
_VcePathRxJitterGauge_Object=MibTableColumn
vcePathRxJitterGauge=_VcePathRxJitterGauge_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,25),_VcePathRxJitterGauge_Type())
vcePathRxJitterGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathRxJitterGauge.setStatus(_A)
_VcePathTxJitterGauge_Type=Gauge32
_VcePathTxJitterGauge_Object=MibTableColumn
vcePathTxJitterGauge=_VcePathTxJitterGauge_Object((1,3,6,1,4,1,45346,1,1,2,4,2,2,1,26),_VcePathTxJitterGauge_Type())
vcePathTxJitterGauge.setMaxAccess(_C)
if mibBuilder.loadTexts:vcePathTxJitterGauge.setStatus(_A)
_VceARP_ObjectIdentity=ObjectIdentity
vceARP=_VceARP_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,5))
_VceArpObject_ObjectIdentity=ObjectIdentity
vceArpObject=_VceArpObject_ObjectIdentity((1,3,6,1,4,1,45346,1,1,2,5,2))
_VceArpNum_Type=Integer32
_VceArpNum_Object=MibScalar
vceArpNum=_VceArpNum_Object((1,3,6,1,4,1,45346,1,1,2,5,2,1),_VceArpNum_Type())
vceArpNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vceArpNum.setStatus(_A)
_VceArpTable_Object=MibTable
vceArpTable=_VceArpTable_Object((1,3,6,1,4,1,45346,1,1,2,5,2,2))
if mibBuilder.loadTexts:vceArpTable.setStatus(_A)
_VceArpEntry_Object=MibTableRow
vceArpEntry=_VceArpEntry_Object((1,3,6,1,4,1,45346,1,1,2,5,2,2,1))
vceArpEntry.setIndexNames((0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:vceArpEntry.setStatus(_A)
_VceArpItf_Type=InterfaceIndex
_VceArpItf_Object=MibTableColumn
vceArpItf=_VceArpItf_Object((1,3,6,1,4,1,45346,1,1,2,5,2,2,1,1),_VceArpItf_Type())
vceArpItf.setMaxAccess(_E)
if mibBuilder.loadTexts:vceArpItf.setStatus(_A)
_VceArpIpAddrType_Type=InetAddressType
_VceArpIpAddrType_Object=MibTableColumn
vceArpIpAddrType=_VceArpIpAddrType_Object((1,3,6,1,4,1,45346,1,1,2,5,2,2,1,2),_VceArpIpAddrType_Type())
vceArpIpAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:vceArpIpAddrType.setStatus(_A)
_VceArpIpAddr_Type=InetAddress
_VceArpIpAddr_Object=MibTableColumn
vceArpIpAddr=_VceArpIpAddr_Object((1,3,6,1,4,1,45346,1,1,2,5,2,2,1,3),_VceArpIpAddr_Type())
vceArpIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:vceArpIpAddr.setStatus(_A)
class _VceArpMac_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_VceArpMac_Type.__name__=_G
_VceArpMac_Object=MibTableColumn
vceArpMac=_VceArpMac_Object((1,3,6,1,4,1,45346,1,1,2,5,2,2,1,4),_VceArpMac_Type())
vceArpMac.setMaxAccess(_C)
if mibBuilder.loadTexts:vceArpMac.setStatus(_A)
_VceArpStag_Type=Integer32
_VceArpStag_Object=MibTableColumn
vceArpStag=_VceArpStag_Object((1,3,6,1,4,1,45346,1,1,2,5,2,2,1,5),_VceArpStag_Type())
vceArpStag.setMaxAccess(_C)
if mibBuilder.loadTexts:vceArpStag.setStatus(_A)
_VceArpCtag_Type=Integer32
_VceArpCtag_Object=MibTableColumn
vceArpCtag=_VceArpCtag_Object((1,3,6,1,4,1,45346,1,1,2,5,2,2,1,6),_VceArpCtag_Type())
vceArpCtag.setMaxAccess(_C)
if mibBuilder.loadTexts:vceArpCtag.setStatus(_A)
_VceArpState_Type=VceArpStateType
_VceArpState_Object=MibTableColumn
vceArpState=_VceArpState_Object((1,3,6,1,4,1,45346,1,1,2,5,2,2,1,7),_VceArpState_Type())
vceArpState.setMaxAccess(_C)
if mibBuilder.loadTexts:vceArpState.setStatus(_A)
vceHaGroup=ObjectGroup((1,3,6,1,4,1,45346,1,1,2,1,1))
vceHaGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:vceHaGroup.setStatus(_A)
vceHealthGroup=ObjectGroup((1,3,6,1,4,1,45346,1,1,2,2,1))
vceHealthGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:vceHealthGroup.setStatus(_A)
vceLinkGroup=ObjectGroup((1,3,6,1,4,1,45346,1,1,2,3,1))
vceLinkGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:vceLinkGroup.setStatus(_A)
vcePathGroup=ObjectGroup((1,3,6,1,4,1,45346,1,1,2,4,1))
vcePathGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj)))
if mibBuilder.loadTexts:vcePathGroup.setStatus(_A)
vceArpGroup=ObjectGroup((1,3,6,1,4,1,45346,1,1,2,5,1))
vceArpGroup.setObjects(*((_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao)))
if mibBuilder.loadTexts:vceArpGroup.setStatus(_A)
vceCompliance=ModuleCompliance((1,3,6,1,4,1,45346,1,1,1))
vceCompliance.setObjects(*((_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At)))
if mibBuilder.loadTexts:vceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VceHaAdminStateType':VceHaAdminStateType,'VceHaPeerStateType':VceHaPeerStateType,'VceLinkStateType':VceLinkStateType,'VcePathStateType':VcePathStateType,'VcePathTunlModeType':VcePathTunlModeType,'VceArpStateType':VceArpStateType,'edge':edge,'vceCompliance':vceCompliance,'vceEdgeObject':vceEdgeObject,'vceHA':vceHA,_Ap:vceHaGroup,'vceHAObject':vceHAObject,_U:vceHaAdminState,_V:vceHaPeerState,_W:vceHaActiveWanItfNum,_X:vceHaActiveLanItfNum,_Y:vceHaStanbyWanItfNum,_Z:vceHaStanbyLanItfNum,'vceHealth':vceHealth,_Aq:vceHealthGroup,'vceHealthObject':vceHealthObject,_a:vceCpuUtilPct5min,_b:vceCpuUtilPct30sec,_c:vceMemUsedPct,'vceLink':vceLink,_Ar:vceLinkGroup,'vceLinkObject':vceLinkObject,_d:vceLinkNum,'vceLinkTable':vceLinkTable,'vceLinkEntry':vceLinkEntry,_N:vceLinkIntId,_e:vceLinkName,_f:vceLinkTxP1Pkt,_g:vceLinkRxP1Pkt,_h:vceLinkTxP1Bytes,_i:vceLinkRxP1Bytes,_j:vceLinkTxP2Pkt,_k:vceLinkRxP2Pkt,_l:vceLinkTxP2Bytes,_m:vceLinkRxP2Bytes,_n:vceLinkTxP3Pkt,_o:vceLinkRxP3Pkt,_p:vceLinkTxP3Bytes,_q:vceLinkRxP3Bytes,_r:vceLinkTxCtlPkt,_s:vceLinkRxCtlPkt,_t:vceLinkTxCtlBytes,_u:vceLinkRxCtlBytes,_v:vceLinkTxJitter,_w:vceLinkRxJitter,_x:vceLinkTxLatency,_y:vceLinkRxLatency,_z:vceLinkTxLostPkt,_A0:vceLinkRxLostPkt,_A1:vceLinkPublicIpType,_A2:vceLinkPublicIp,_A3:vceLinkLocalIpType,_A4:vceLinkLocalIp,_A5:vceLinkVlanId,_A6:vceLinkMtu,_A7:vceLinkItf,_A8:vceLinkState,_A9:vceLinkVeloSvcReachable,_AA:vceLinkTotTxPkts,_AB:vceLinkTotRxPkts,_AC:vceLinkTotTxbytes,_AD:vceLinkTotRxBytes,_AE:vceLinkIf,_AF:vceLinkNextHopType,_AG:vceLinkNextHop,_AH:vceLinkTxJitterGauge,_AI:vceLinkRxJitterGauge,_AJ:vceLinkTxLatencyGauge,_AK:vceLinkRxLatencyGauge,_AL:vceLinkTxLostPktGauge,_AM:vceLinkRxLostPktGauge,'vcePath':vcePath,_As:vcePathGroup,'vcePathObject':vcePathObject,_AN:vcePathNum,'vcePathTable':vcePathTable,'vcePathEntry':vcePathEntry,_O:vcePathIfIntId,_AO:vcePathIpType,_AP:vcePathIp,_P:vcePathGwAddrType,_Q:vcePathGwAddr,_AQ:vcePathPeerName,_AR:vcePathState,_AS:vcePathUpTime,_AT:vcePathRxState,_AU:vcePathTxState,_AV:vcePathTunlMode,_AW:vcePathTxAveLatency,_AX:vcePathRxAveLatency,_AY:vcePathRxBytes,_AZ:vcePathTxBytes,_Aa:vcePathRxLostPkt,_Ab:vcePathTxLostPkt,_Ac:vcePathRxPkt,_Ad:vcePathTxPkt,_Ae:vcePathRxJitter,_Af:vcePathTxJitter,_Ag:vcePathRxLostPktGauge,_Ah:vcePathTxLostPktGauge,_Ai:vcePathRxJitterGauge,_Aj:vcePathTxJitterGauge,'vceARP':vceARP,_At:vceArpGroup,'vceArpObject':vceArpObject,_Ak:vceArpNum,'vceArpTable':vceArpTable,'vceArpEntry':vceArpEntry,_R:vceArpItf,_S:vceArpIpAddrType,_T:vceArpIpAddr,_Al:vceArpMac,_Am:vceArpStag,_An:vceArpCtag,_Ao:vceArpState})