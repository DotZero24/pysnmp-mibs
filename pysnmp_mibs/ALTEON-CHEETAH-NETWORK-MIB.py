_BB='vrrpOperVirtRtrIndex'
_BA='allowedNwInfoIndex'
_B9='rip2RoutesInfoNxtHopIndex'
_B8='rip2RoutesInfoDestIndex'
_B7='ripInfoIntfIndex'
_B6='intfInfoIndex'
_B5='ipRoute6InfoIndx'
_B4='nbrcacheInfoIndex'
_B3='gatewayInfoIndex'
_B2='ospfIfNbrIpAddr'
_B1='ospfIfNbrIntfIndex'
_B0='ospfIfInfoIndex'
_A_='ospfAreaInfoIndex'
_Az='vrrpInfoVirtRtrIndex'
_Ay='arpInfoDestIp'
_Ax='multicast'
_Aw='broadcast'
_Av='ipRouteInfoIndx'
_Au='ip6GwStatsIndex'
_At='icmp6StatsIndx'
_As='ifStatsIndex'
_Ar='ospfIntfErrIndex'
_Aq='ospfIntfIndex'
_Ap='ospfIntfNbrIndex'
_Ao='ospfIntfRxTxIndex'
_An='ospfAreaErrIndex'
_Am='ospfAreaIntfIndex'
_Al='ospfAreaNbrIndex'
_Ak='ospfAreaRxTxIndex'
_Aj='ripNewCfgIntfIndex'
_Ai='ripCurCfgIntfIndex'
_Ah='ipNewCfgStaticArpIndx'
_Ag='ipCurCfgStaticArpIndx'
_Af='ospfNewCfgVisionAreaIndex'
_Ae='ospfNewCfgRangeIndex'
_Ad='ospfCurCfgRangeIndex'
_Ac='ospfNewCfgHostIndex'
_Ab='ospfCurCfgHostIndex'
_Aa='ospfNewCfgVirtIntfIndex'
_AZ='ospfCurCfgVirtIntfIndex'
_AY='ospfNewCfgIntfIndex'
_AX='ospfCurCfgIntfIndex'
_AW='ospfNewCfgMdkeyIndex'
_AV='ospfCurCfgMdkeyIndex'
_AU='ospfNewCfgAreaId'
_AT='ospfNewCfgAreaIndex'
_AS='ospfCurCfgAreaId'
_AR='ospfCurCfgAreaIndex'
_AQ='bgpNewCfgAggrIndex'
_AP='bgpCurCfgAggrIndex'
_AO='bgpNewCfgPeerIndex'
_AN='redistribute'
_AM='originate'
_AL='bgpCurCfgPeerIndex'
_AK='ipNewCfgAspathIndex'
_AJ='ipNewCfgAspathRmapIndex'
_AI='ipCurCfgAspathRmapIndex'
_AH='ipNewCfgAlistIndex'
_AG='ipNewCfgAlistRmapIndex'
_AF='ipCurCfgAlistRmapIndex'
_AE='ipNewCfgRmapIndex'
_AD='ipCurCfgRmapIndex'
_AC='ipNewCfgNwfIndex'
_AB='ipCurCfgNwfIndex'
_AA='vrrpNewCfgVirtRtrVrGrpIndx'
_A9='vrrpCurCfgVirtRtrVrGrpIndx'
_A8='vrrpNewCfgVirtRtrGrpIndx'
_A7='vrrpCurCfgVirtRtrGrpIndx'
_A6='vrrpNewCfgIfIndx'
_A5='simple-text-password'
_A4='vrrpCurCfgIfIndx'
_A3='vrrpNewCfgVirtRtrIndx'
_A2='vrrpCurCfgVirtRtrIndx'
_A1='ipFwdNewCfgLocalIndex'
_A0='ipFwdCurCfgLocalIndex'
_z='ipFwdNewCfgPortIndex'
_y='ipFwdCurCfgPortIndex'
_x='ipv6NewCfgStaticRouteIndx'
_w='ipv6CurCfgStaticRouteIndx'
_v='ipNewCfgStaticRouteIndx'
_u='ipCurCfgStaticRouteIndx'
_t='ipNewCfgGwIndex'
_s='ipCurCfgGwIndex'
_r='roundrobin'
_q='strict'
_p='ipNewCfgIntfIndex'
_o='ipCurCfgIntfIndex'
_n='backup'
_m='local'
_l='static'
_k='supply'
_j='listen'
_i='ripVersion2'
_h='ripVersion1'
_g='nssa'
_f='stub'
_e='transit'
_d='md5'
_c='ipCurCfgAlistIndex'
_b='deny'
_a='permit'
_Z='v6'
_Y='v4'
_X='obsolete'
_W='both'
_V='clear'
_U='password'
_T='ipv6'
_S='ipv4'
_R='ok'
_Q='off'
_P='on'
_O='type2'
_N='type1'
_M='Unsigned32'
_L='delete'
_K='other'
_J='none'
_I='DisplayString'
_H='read-write'
_G='ALTEON-CHEETAH-NETWORK-MIB'
_F='enabled'
_E='disabled'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aws_switch,=mibBuilder.importSymbols('ALTEON-ROOT-MIB','aws-switch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
layer3=ModuleIdentity((1,3,6,1,4,1,1872,2,5,3))
if mibBuilder.loadTexts:layer3.setRevisions(('2009-08-05 00:00',))
_Layer3Configs_ObjectIdentity=ObjectIdentity
layer3Configs=_Layer3Configs_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1))
_IpInterfaceCfg_ObjectIdentity=ObjectIdentity
ipInterfaceCfg=_IpInterfaceCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,1))
_IpInterfaceTableMax_Type=Integer32
_IpInterfaceTableMax_Object=MibScalar
ipInterfaceTableMax=_IpInterfaceTableMax_Object((1,3,6,1,4,1,1872,2,5,3,1,1,1),_IpInterfaceTableMax_Type())
ipInterfaceTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipInterfaceTableMax.setStatus(_A)
_IpCurCfgIntfTable_Object=MibTable
ipCurCfgIntfTable=_IpCurCfgIntfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2))
if mibBuilder.loadTexts:ipCurCfgIntfTable.setStatus(_A)
_IpCurCfgIntfEntry_Object=MibTableRow
ipCurCfgIntfEntry=_IpCurCfgIntfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1))
ipCurCfgIntfEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:ipCurCfgIntfEntry.setStatus(_A)
_IpCurCfgIntfIndex_Type=Integer32
_IpCurCfgIntfIndex_Object=MibTableColumn
ipCurCfgIntfIndex=_IpCurCfgIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,1),_IpCurCfgIntfIndex_Type())
ipCurCfgIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfIndex.setStatus(_A)
_IpCurCfgIntfAddr_Type=IpAddress
_IpCurCfgIntfAddr_Object=MibTableColumn
ipCurCfgIntfAddr=_IpCurCfgIntfAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,2),_IpCurCfgIntfAddr_Type())
ipCurCfgIntfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfAddr.setStatus(_A)
_IpCurCfgIntfMask_Type=IpAddress
_IpCurCfgIntfMask_Object=MibTableColumn
ipCurCfgIntfMask=_IpCurCfgIntfMask_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,3),_IpCurCfgIntfMask_Type())
ipCurCfgIntfMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfMask.setStatus(_A)
_IpCurCfgIntfBroadcast_Type=IpAddress
_IpCurCfgIntfBroadcast_Object=MibTableColumn
ipCurCfgIntfBroadcast=_IpCurCfgIntfBroadcast_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,4),_IpCurCfgIntfBroadcast_Type())
ipCurCfgIntfBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfBroadcast.setStatus(_X)
_IpCurCfgIntfVlan_Type=Integer32
_IpCurCfgIntfVlan_Object=MibTableColumn
ipCurCfgIntfVlan=_IpCurCfgIntfVlan_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,5),_IpCurCfgIntfVlan_Type())
ipCurCfgIntfVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfVlan.setStatus(_A)
class _IpCurCfgIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpCurCfgIntfState_Type.__name__=_C
_IpCurCfgIntfState_Object=MibTableColumn
ipCurCfgIntfState=_IpCurCfgIntfState_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,6),_IpCurCfgIntfState_Type())
ipCurCfgIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfState.setStatus(_A)
class _IpCurCfgIntfBootpRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpCurCfgIntfBootpRelay_Type.__name__=_C
_IpCurCfgIntfBootpRelay_Object=MibTableColumn
ipCurCfgIntfBootpRelay=_IpCurCfgIntfBootpRelay_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,7),_IpCurCfgIntfBootpRelay_Type())
ipCurCfgIntfBootpRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfBootpRelay.setStatus(_A)
class _IpCurCfgIntfIpVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_IpCurCfgIntfIpVer_Type.__name__=_C
_IpCurCfgIntfIpVer_Object=MibTableColumn
ipCurCfgIntfIpVer=_IpCurCfgIntfIpVer_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,9),_IpCurCfgIntfIpVer_Type())
ipCurCfgIntfIpVer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfIpVer.setStatus(_A)
class _IpCurCfgIntfIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_IpCurCfgIntfIpv6Addr_Type.__name__=_I
_IpCurCfgIntfIpv6Addr_Object=MibTableColumn
ipCurCfgIntfIpv6Addr=_IpCurCfgIntfIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,10),_IpCurCfgIntfIpv6Addr_Type())
ipCurCfgIntfIpv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfIpv6Addr.setStatus(_A)
class _IpCurCfgIntfPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_IpCurCfgIntfPrefixLen_Type.__name__=_C
_IpCurCfgIntfPrefixLen_Object=MibTableColumn
ipCurCfgIntfPrefixLen=_IpCurCfgIntfPrefixLen_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,11),_IpCurCfgIntfPrefixLen_Type())
ipCurCfgIntfPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfPrefixLen.setStatus(_A)
class _IpCurCfgIntfRouteAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpCurCfgIntfRouteAdv_Type.__name__=_C
_IpCurCfgIntfRouteAdv_Object=MibTableColumn
ipCurCfgIntfRouteAdv=_IpCurCfgIntfRouteAdv_Object((1,3,6,1,4,1,1872,2,5,3,1,1,2,1,12),_IpCurCfgIntfRouteAdv_Type())
ipCurCfgIntfRouteAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfRouteAdv.setStatus(_A)
_IpNewCfgIntfTable_Object=MibTable
ipNewCfgIntfTable=_IpNewCfgIntfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3))
if mibBuilder.loadTexts:ipNewCfgIntfTable.setStatus(_A)
_IpNewCfgIntfEntry_Object=MibTableRow
ipNewCfgIntfEntry=_IpNewCfgIntfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1))
ipNewCfgIntfEntry.setIndexNames((0,_G,_p))
if mibBuilder.loadTexts:ipNewCfgIntfEntry.setStatus(_A)
_IpNewCfgIntfIndex_Type=Integer32
_IpNewCfgIntfIndex_Object=MibTableColumn
ipNewCfgIntfIndex=_IpNewCfgIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,1),_IpNewCfgIntfIndex_Type())
ipNewCfgIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgIntfIndex.setStatus(_A)
_IpNewCfgIntfAddr_Type=IpAddress
_IpNewCfgIntfAddr_Object=MibTableColumn
ipNewCfgIntfAddr=_IpNewCfgIntfAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,2),_IpNewCfgIntfAddr_Type())
ipNewCfgIntfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfAddr.setStatus(_A)
_IpNewCfgIntfMask_Type=IpAddress
_IpNewCfgIntfMask_Object=MibTableColumn
ipNewCfgIntfMask=_IpNewCfgIntfMask_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,3),_IpNewCfgIntfMask_Type())
ipNewCfgIntfMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfMask.setStatus(_A)
_IpNewCfgIntfBroadcast_Type=IpAddress
_IpNewCfgIntfBroadcast_Object=MibTableColumn
ipNewCfgIntfBroadcast=_IpNewCfgIntfBroadcast_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,4),_IpNewCfgIntfBroadcast_Type())
ipNewCfgIntfBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfBroadcast.setStatus(_X)
_IpNewCfgIntfVlan_Type=Integer32
_IpNewCfgIntfVlan_Object=MibTableColumn
ipNewCfgIntfVlan=_IpNewCfgIntfVlan_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,5),_IpNewCfgIntfVlan_Type())
ipNewCfgIntfVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfVlan.setStatus(_A)
class _IpNewCfgIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpNewCfgIntfState_Type.__name__=_C
_IpNewCfgIntfState_Object=MibTableColumn
ipNewCfgIntfState=_IpNewCfgIntfState_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,6),_IpNewCfgIntfState_Type())
ipNewCfgIntfState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfState.setStatus(_A)
class _IpNewCfgIntfDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_IpNewCfgIntfDelete_Type.__name__=_C
_IpNewCfgIntfDelete_Object=MibTableColumn
ipNewCfgIntfDelete=_IpNewCfgIntfDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,7),_IpNewCfgIntfDelete_Type())
ipNewCfgIntfDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfDelete.setStatus(_A)
class _IpNewCfgIntfBootpRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpNewCfgIntfBootpRelay_Type.__name__=_C
_IpNewCfgIntfBootpRelay_Object=MibTableColumn
ipNewCfgIntfBootpRelay=_IpNewCfgIntfBootpRelay_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,8),_IpNewCfgIntfBootpRelay_Type())
ipNewCfgIntfBootpRelay.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfBootpRelay.setStatus(_A)
class _IpNewCfgIntfIpVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_IpNewCfgIntfIpVer_Type.__name__=_C
_IpNewCfgIntfIpVer_Object=MibTableColumn
ipNewCfgIntfIpVer=_IpNewCfgIntfIpVer_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,10),_IpNewCfgIntfIpVer_Type())
ipNewCfgIntfIpVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfIpVer.setStatus(_A)
class _IpNewCfgIntfIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_IpNewCfgIntfIpv6Addr_Type.__name__=_I
_IpNewCfgIntfIpv6Addr_Object=MibTableColumn
ipNewCfgIntfIpv6Addr=_IpNewCfgIntfIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,11),_IpNewCfgIntfIpv6Addr_Type())
ipNewCfgIntfIpv6Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfIpv6Addr.setStatus(_A)
class _IpNewCfgIntfPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_IpNewCfgIntfPrefixLen_Type.__name__=_C
_IpNewCfgIntfPrefixLen_Object=MibTableColumn
ipNewCfgIntfPrefixLen=_IpNewCfgIntfPrefixLen_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,12),_IpNewCfgIntfPrefixLen_Type())
ipNewCfgIntfPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfPrefixLen.setStatus(_A)
class _IpNewCfgIntfRouteAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpNewCfgIntfRouteAdv_Type.__name__=_C
_IpNewCfgIntfRouteAdv_Object=MibTableColumn
ipNewCfgIntfRouteAdv=_IpNewCfgIntfRouteAdv_Object((1,3,6,1,4,1,1872,2,5,3,1,1,3,1,13),_IpNewCfgIntfRouteAdv_Type())
ipNewCfgIntfRouteAdv.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfRouteAdv.setStatus(_A)
_IpGatewayCfg_ObjectIdentity=ObjectIdentity
ipGatewayCfg=_IpGatewayCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,2))
class _IpCurCfgGwMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_q,1),(_r,2)))
_IpCurCfgGwMetric_Type.__name__=_C
_IpCurCfgGwMetric_Object=MibScalar
ipCurCfgGwMetric=_IpCurCfgGwMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,2,1),_IpCurCfgGwMetric_Type())
ipCurCfgGwMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwMetric.setStatus(_A)
class _IpNewCfgGwMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_q,1),(_r,2)))
_IpNewCfgGwMetric_Type.__name__=_C
_IpNewCfgGwMetric_Object=MibScalar
ipNewCfgGwMetric=_IpNewCfgGwMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,2,2),_IpNewCfgGwMetric_Type())
ipNewCfgGwMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:ipNewCfgGwMetric.setStatus(_A)
_IpGatewayTableMax_Type=Integer32
_IpGatewayTableMax_Object=MibScalar
ipGatewayTableMax=_IpGatewayTableMax_Object((1,3,6,1,4,1,1872,2,5,3,1,2,3),_IpGatewayTableMax_Type())
ipGatewayTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipGatewayTableMax.setStatus(_A)
_IpCurCfgGwTable_Object=MibTable
ipCurCfgGwTable=_IpCurCfgGwTable_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4))
if mibBuilder.loadTexts:ipCurCfgGwTable.setStatus(_A)
_IpCurCfgGwEntry_Object=MibTableRow
ipCurCfgGwEntry=_IpCurCfgGwEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1))
ipCurCfgGwEntry.setIndexNames((0,_G,_s))
if mibBuilder.loadTexts:ipCurCfgGwEntry.setStatus(_A)
_IpCurCfgGwIndex_Type=Integer32
_IpCurCfgGwIndex_Object=MibTableColumn
ipCurCfgGwIndex=_IpCurCfgGwIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,1),_IpCurCfgGwIndex_Type())
ipCurCfgGwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwIndex.setStatus(_A)
_IpCurCfgGwAddr_Type=IpAddress
_IpCurCfgGwAddr_Object=MibTableColumn
ipCurCfgGwAddr=_IpCurCfgGwAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,2),_IpCurCfgGwAddr_Type())
ipCurCfgGwAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwAddr.setStatus(_A)
class _IpCurCfgGwInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_IpCurCfgGwInterval_Type.__name__=_C
_IpCurCfgGwInterval_Object=MibTableColumn
ipCurCfgGwInterval=_IpCurCfgGwInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,3),_IpCurCfgGwInterval_Type())
ipCurCfgGwInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwInterval.setStatus(_A)
class _IpCurCfgGwRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_IpCurCfgGwRetry_Type.__name__=_C
_IpCurCfgGwRetry_Object=MibTableColumn
ipCurCfgGwRetry=_IpCurCfgGwRetry_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,4),_IpCurCfgGwRetry_Type())
ipCurCfgGwRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwRetry.setStatus(_A)
class _IpCurCfgGwState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpCurCfgGwState_Type.__name__=_C
_IpCurCfgGwState_Object=MibTableColumn
ipCurCfgGwState=_IpCurCfgGwState_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,5),_IpCurCfgGwState_Type())
ipCurCfgGwState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwState.setStatus(_A)
class _IpCurCfgGwArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpCurCfgGwArp_Type.__name__=_C
_IpCurCfgGwArp_Object=MibTableColumn
ipCurCfgGwArp=_IpCurCfgGwArp_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,6),_IpCurCfgGwArp_Type())
ipCurCfgGwArp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwArp.setStatus(_A)
_IpCurCfgGwVlan_Type=Integer32
_IpCurCfgGwVlan_Object=MibTableColumn
ipCurCfgGwVlan=_IpCurCfgGwVlan_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,7),_IpCurCfgGwVlan_Type())
ipCurCfgGwVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwVlan.setStatus(_A)
class _IpCurCfgGwPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_IpCurCfgGwPriority_Type.__name__=_C
_IpCurCfgGwPriority_Object=MibTableColumn
ipCurCfgGwPriority=_IpCurCfgGwPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,8),_IpCurCfgGwPriority_Type())
ipCurCfgGwPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwPriority.setStatus(_A)
class _IpCurCfgGwIpVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_IpCurCfgGwIpVer_Type.__name__=_C
_IpCurCfgGwIpVer_Object=MibTableColumn
ipCurCfgGwIpVer=_IpCurCfgGwIpVer_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,9),_IpCurCfgGwIpVer_Type())
ipCurCfgGwIpVer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwIpVer.setStatus(_A)
class _IpCurCfgGwIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_IpCurCfgGwIpv6Addr_Type.__name__=_I
_IpCurCfgGwIpv6Addr_Object=MibTableColumn
ipCurCfgGwIpv6Addr=_IpCurCfgGwIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,2,4,1,10),_IpCurCfgGwIpv6Addr_Type())
ipCurCfgGwIpv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwIpv6Addr.setStatus(_A)
_IpNewCfgGwTable_Object=MibTable
ipNewCfgGwTable=_IpNewCfgGwTable_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5))
if mibBuilder.loadTexts:ipNewCfgGwTable.setStatus(_A)
_IpNewCfgGwEntry_Object=MibTableRow
ipNewCfgGwEntry=_IpNewCfgGwEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1))
ipNewCfgGwEntry.setIndexNames((0,_G,_t))
if mibBuilder.loadTexts:ipNewCfgGwEntry.setStatus(_A)
_IpNewCfgGwIndex_Type=Integer32
_IpNewCfgGwIndex_Object=MibTableColumn
ipNewCfgGwIndex=_IpNewCfgGwIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,1),_IpNewCfgGwIndex_Type())
ipNewCfgGwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgGwIndex.setStatus(_A)
_IpNewCfgGwAddr_Type=IpAddress
_IpNewCfgGwAddr_Object=MibTableColumn
ipNewCfgGwAddr=_IpNewCfgGwAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,2),_IpNewCfgGwAddr_Type())
ipNewCfgGwAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwAddr.setStatus(_A)
class _IpNewCfgGwInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_IpNewCfgGwInterval_Type.__name__=_C
_IpNewCfgGwInterval_Object=MibTableColumn
ipNewCfgGwInterval=_IpNewCfgGwInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,3),_IpNewCfgGwInterval_Type())
ipNewCfgGwInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwInterval.setStatus(_A)
class _IpNewCfgGwRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_IpNewCfgGwRetry_Type.__name__=_C
_IpNewCfgGwRetry_Object=MibTableColumn
ipNewCfgGwRetry=_IpNewCfgGwRetry_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,4),_IpNewCfgGwRetry_Type())
ipNewCfgGwRetry.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwRetry.setStatus(_A)
class _IpNewCfgGwState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpNewCfgGwState_Type.__name__=_C
_IpNewCfgGwState_Object=MibTableColumn
ipNewCfgGwState=_IpNewCfgGwState_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,5),_IpNewCfgGwState_Type())
ipNewCfgGwState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwState.setStatus(_A)
class _IpNewCfgGwDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_IpNewCfgGwDelete_Type.__name__=_C
_IpNewCfgGwDelete_Object=MibTableColumn
ipNewCfgGwDelete=_IpNewCfgGwDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,6),_IpNewCfgGwDelete_Type())
ipNewCfgGwDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwDelete.setStatus(_A)
class _IpNewCfgGwArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpNewCfgGwArp_Type.__name__=_C
_IpNewCfgGwArp_Object=MibTableColumn
ipNewCfgGwArp=_IpNewCfgGwArp_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,7),_IpNewCfgGwArp_Type())
ipNewCfgGwArp.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwArp.setStatus(_A)
_IpNewCfgGwVlan_Type=Integer32
_IpNewCfgGwVlan_Object=MibTableColumn
ipNewCfgGwVlan=_IpNewCfgGwVlan_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,8),_IpNewCfgGwVlan_Type())
ipNewCfgGwVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwVlan.setStatus(_A)
class _IpNewCfgGwPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_IpNewCfgGwPriority_Type.__name__=_C
_IpNewCfgGwPriority_Object=MibTableColumn
ipNewCfgGwPriority=_IpNewCfgGwPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,9),_IpNewCfgGwPriority_Type())
ipNewCfgGwPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwPriority.setStatus(_A)
class _IpNewCfgGwIpVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_IpNewCfgGwIpVer_Type.__name__=_C
_IpNewCfgGwIpVer_Object=MibTableColumn
ipNewCfgGwIpVer=_IpNewCfgGwIpVer_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,10),_IpNewCfgGwIpVer_Type())
ipNewCfgGwIpVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwIpVer.setStatus(_A)
class _IpNewCfgGwIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_IpNewCfgGwIpv6Addr_Type.__name__=_I
_IpNewCfgGwIpv6Addr_Object=MibTableColumn
ipNewCfgGwIpv6Addr=_IpNewCfgGwIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,2,5,1,11),_IpNewCfgGwIpv6Addr_Type())
ipNewCfgGwIpv6Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwIpv6Addr.setStatus(_A)
_IpStaticRouteCfg_ObjectIdentity=ObjectIdentity
ipStaticRouteCfg=_IpStaticRouteCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,3))
_IpStaticRouteTableMaxSize_Type=Integer32
_IpStaticRouteTableMaxSize_Object=MibScalar
ipStaticRouteTableMaxSize=_IpStaticRouteTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,3,1),_IpStaticRouteTableMaxSize_Type())
ipStaticRouteTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ipStaticRouteTableMaxSize.setStatus(_A)
_IpCurCfgStaticRouteTable_Object=MibTable
ipCurCfgStaticRouteTable=_IpCurCfgStaticRouteTable_Object((1,3,6,1,4,1,1872,2,5,3,1,3,2))
if mibBuilder.loadTexts:ipCurCfgStaticRouteTable.setStatus(_A)
_IpCurCfgStaticRouteEntry_Object=MibTableRow
ipCurCfgStaticRouteEntry=_IpCurCfgStaticRouteEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,3,2,1))
ipCurCfgStaticRouteEntry.setIndexNames((0,_G,_u))
if mibBuilder.loadTexts:ipCurCfgStaticRouteEntry.setStatus(_A)
_IpCurCfgStaticRouteIndx_Type=Integer32
_IpCurCfgStaticRouteIndx_Object=MibTableColumn
ipCurCfgStaticRouteIndx=_IpCurCfgStaticRouteIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,3,2,1,1),_IpCurCfgStaticRouteIndx_Type())
ipCurCfgStaticRouteIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteIndx.setStatus(_A)
_IpCurCfgStaticRouteDestIp_Type=IpAddress
_IpCurCfgStaticRouteDestIp_Object=MibTableColumn
ipCurCfgStaticRouteDestIp=_IpCurCfgStaticRouteDestIp_Object((1,3,6,1,4,1,1872,2,5,3,1,3,2,1,2),_IpCurCfgStaticRouteDestIp_Type())
ipCurCfgStaticRouteDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteDestIp.setStatus(_A)
_IpCurCfgStaticRouteMask_Type=IpAddress
_IpCurCfgStaticRouteMask_Object=MibTableColumn
ipCurCfgStaticRouteMask=_IpCurCfgStaticRouteMask_Object((1,3,6,1,4,1,1872,2,5,3,1,3,2,1,3),_IpCurCfgStaticRouteMask_Type())
ipCurCfgStaticRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteMask.setStatus(_A)
_IpCurCfgStaticRouteGateway_Type=IpAddress
_IpCurCfgStaticRouteGateway_Object=MibTableColumn
ipCurCfgStaticRouteGateway=_IpCurCfgStaticRouteGateway_Object((1,3,6,1,4,1,1872,2,5,3,1,3,2,1,4),_IpCurCfgStaticRouteGateway_Type())
ipCurCfgStaticRouteGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteGateway.setStatus(_A)
_IpCurCfgStaticRouteInterface_Type=Integer32
_IpCurCfgStaticRouteInterface_Object=MibTableColumn
ipCurCfgStaticRouteInterface=_IpCurCfgStaticRouteInterface_Object((1,3,6,1,4,1,1872,2,5,3,1,3,2,1,5),_IpCurCfgStaticRouteInterface_Type())
ipCurCfgStaticRouteInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteInterface.setStatus(_A)
_IpNewCfgStaticRouteTable_Object=MibTable
ipNewCfgStaticRouteTable=_IpNewCfgStaticRouteTable_Object((1,3,6,1,4,1,1872,2,5,3,1,3,3))
if mibBuilder.loadTexts:ipNewCfgStaticRouteTable.setStatus(_A)
_IpNewCfgStaticRouteEntry_Object=MibTableRow
ipNewCfgStaticRouteEntry=_IpNewCfgStaticRouteEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,3,3,1))
ipNewCfgStaticRouteEntry.setIndexNames((0,_G,_v))
if mibBuilder.loadTexts:ipNewCfgStaticRouteEntry.setStatus(_A)
_IpNewCfgStaticRouteIndx_Type=Integer32
_IpNewCfgStaticRouteIndx_Object=MibTableColumn
ipNewCfgStaticRouteIndx=_IpNewCfgStaticRouteIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,3,3,1,1),_IpNewCfgStaticRouteIndx_Type())
ipNewCfgStaticRouteIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgStaticRouteIndx.setStatus(_A)
_IpNewCfgStaticRouteDestIp_Type=IpAddress
_IpNewCfgStaticRouteDestIp_Object=MibTableColumn
ipNewCfgStaticRouteDestIp=_IpNewCfgStaticRouteDestIp_Object((1,3,6,1,4,1,1872,2,5,3,1,3,3,1,2),_IpNewCfgStaticRouteDestIp_Type())
ipNewCfgStaticRouteDestIp.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteDestIp.setStatus(_A)
_IpNewCfgStaticRouteMask_Type=IpAddress
_IpNewCfgStaticRouteMask_Object=MibTableColumn
ipNewCfgStaticRouteMask=_IpNewCfgStaticRouteMask_Object((1,3,6,1,4,1,1872,2,5,3,1,3,3,1,3),_IpNewCfgStaticRouteMask_Type())
ipNewCfgStaticRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteMask.setStatus(_A)
_IpNewCfgStaticRouteGateway_Type=IpAddress
_IpNewCfgStaticRouteGateway_Object=MibTableColumn
ipNewCfgStaticRouteGateway=_IpNewCfgStaticRouteGateway_Object((1,3,6,1,4,1,1872,2,5,3,1,3,3,1,4),_IpNewCfgStaticRouteGateway_Type())
ipNewCfgStaticRouteGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteGateway.setStatus(_A)
class _IpNewCfgStaticRouteAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_IpNewCfgStaticRouteAction_Type.__name__=_C
_IpNewCfgStaticRouteAction_Object=MibTableColumn
ipNewCfgStaticRouteAction=_IpNewCfgStaticRouteAction_Object((1,3,6,1,4,1,1872,2,5,3,1,3,3,1,5),_IpNewCfgStaticRouteAction_Type())
ipNewCfgStaticRouteAction.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteAction.setStatus(_A)
_IpNewCfgStaticRouteInterface_Type=Integer32
_IpNewCfgStaticRouteInterface_Object=MibTableColumn
ipNewCfgStaticRouteInterface=_IpNewCfgStaticRouteInterface_Object((1,3,6,1,4,1,1872,2,5,3,1,3,3,1,6),_IpNewCfgStaticRouteInterface_Type())
ipNewCfgStaticRouteInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteInterface.setStatus(_A)
_Ipv6CurCfgStaticRouteTable_Object=MibTable
ipv6CurCfgStaticRouteTable=_Ipv6CurCfgStaticRouteTable_Object((1,3,6,1,4,1,1872,2,5,3,1,3,4))
if mibBuilder.loadTexts:ipv6CurCfgStaticRouteTable.setStatus(_A)
_Ipv6CurCfgStaticRouteEntry_Object=MibTableRow
ipv6CurCfgStaticRouteEntry=_Ipv6CurCfgStaticRouteEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,3,4,1))
ipv6CurCfgStaticRouteEntry.setIndexNames((0,_G,_w))
if mibBuilder.loadTexts:ipv6CurCfgStaticRouteEntry.setStatus(_A)
_Ipv6CurCfgStaticRouteIndx_Type=Integer32
_Ipv6CurCfgStaticRouteIndx_Object=MibTableColumn
ipv6CurCfgStaticRouteIndx=_Ipv6CurCfgStaticRouteIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,3,4,1,1),_Ipv6CurCfgStaticRouteIndx_Type())
ipv6CurCfgStaticRouteIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6CurCfgStaticRouteIndx.setStatus(_A)
class _Ipv6CurCfgStaticRouteDestIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Ipv6CurCfgStaticRouteDestIp_Type.__name__=_I
_Ipv6CurCfgStaticRouteDestIp_Object=MibTableColumn
ipv6CurCfgStaticRouteDestIp=_Ipv6CurCfgStaticRouteDestIp_Object((1,3,6,1,4,1,1872,2,5,3,1,3,4,1,2),_Ipv6CurCfgStaticRouteDestIp_Type())
ipv6CurCfgStaticRouteDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6CurCfgStaticRouteDestIp.setStatus(_A)
class _Ipv6CurCfgStaticRouteMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Ipv6CurCfgStaticRouteMask_Type.__name__=_C
_Ipv6CurCfgStaticRouteMask_Object=MibTableColumn
ipv6CurCfgStaticRouteMask=_Ipv6CurCfgStaticRouteMask_Object((1,3,6,1,4,1,1872,2,5,3,1,3,4,1,3),_Ipv6CurCfgStaticRouteMask_Type())
ipv6CurCfgStaticRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6CurCfgStaticRouteMask.setStatus(_A)
class _Ipv6CurCfgStaticRouteGateway_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Ipv6CurCfgStaticRouteGateway_Type.__name__=_I
_Ipv6CurCfgStaticRouteGateway_Object=MibTableColumn
ipv6CurCfgStaticRouteGateway=_Ipv6CurCfgStaticRouteGateway_Object((1,3,6,1,4,1,1872,2,5,3,1,3,4,1,4),_Ipv6CurCfgStaticRouteGateway_Type())
ipv6CurCfgStaticRouteGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6CurCfgStaticRouteGateway.setStatus(_A)
class _Ipv6CurCfgStaticRouteInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Ipv6CurCfgStaticRouteInterface_Type.__name__=_C
_Ipv6CurCfgStaticRouteInterface_Object=MibTableColumn
ipv6CurCfgStaticRouteInterface=_Ipv6CurCfgStaticRouteInterface_Object((1,3,6,1,4,1,1872,2,5,3,1,3,4,1,5),_Ipv6CurCfgStaticRouteInterface_Type())
ipv6CurCfgStaticRouteInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6CurCfgStaticRouteInterface.setStatus(_A)
_Ipv6NewCfgStaticRouteTable_Object=MibTable
ipv6NewCfgStaticRouteTable=_Ipv6NewCfgStaticRouteTable_Object((1,3,6,1,4,1,1872,2,5,3,1,3,5))
if mibBuilder.loadTexts:ipv6NewCfgStaticRouteTable.setStatus(_A)
_Ipv6NewCfgStaticRouteEntry_Object=MibTableRow
ipv6NewCfgStaticRouteEntry=_Ipv6NewCfgStaticRouteEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,3,5,1))
ipv6NewCfgStaticRouteEntry.setIndexNames((0,_G,_x))
if mibBuilder.loadTexts:ipv6NewCfgStaticRouteEntry.setStatus(_A)
_Ipv6NewCfgStaticRouteIndx_Type=Integer32
_Ipv6NewCfgStaticRouteIndx_Object=MibTableColumn
ipv6NewCfgStaticRouteIndx=_Ipv6NewCfgStaticRouteIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,3,5,1,1),_Ipv6NewCfgStaticRouteIndx_Type())
ipv6NewCfgStaticRouteIndx.setMaxAccess(_D)
if mibBuilder.loadTexts:ipv6NewCfgStaticRouteIndx.setStatus(_A)
class _Ipv6NewCfgStaticRouteDestIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Ipv6NewCfgStaticRouteDestIp_Type.__name__=_I
_Ipv6NewCfgStaticRouteDestIp_Object=MibTableColumn
ipv6NewCfgStaticRouteDestIp=_Ipv6NewCfgStaticRouteDestIp_Object((1,3,6,1,4,1,1872,2,5,3,1,3,5,1,2),_Ipv6NewCfgStaticRouteDestIp_Type())
ipv6NewCfgStaticRouteDestIp.setMaxAccess(_D)
if mibBuilder.loadTexts:ipv6NewCfgStaticRouteDestIp.setStatus(_A)
class _Ipv6NewCfgStaticRouteMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Ipv6NewCfgStaticRouteMask_Type.__name__=_C
_Ipv6NewCfgStaticRouteMask_Object=MibTableColumn
ipv6NewCfgStaticRouteMask=_Ipv6NewCfgStaticRouteMask_Object((1,3,6,1,4,1,1872,2,5,3,1,3,5,1,3),_Ipv6NewCfgStaticRouteMask_Type())
ipv6NewCfgStaticRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipv6NewCfgStaticRouteMask.setStatus(_A)
class _Ipv6NewCfgStaticRouteGateway_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Ipv6NewCfgStaticRouteGateway_Type.__name__=_I
_Ipv6NewCfgStaticRouteGateway_Object=MibTableColumn
ipv6NewCfgStaticRouteGateway=_Ipv6NewCfgStaticRouteGateway_Object((1,3,6,1,4,1,1872,2,5,3,1,3,5,1,4),_Ipv6NewCfgStaticRouteGateway_Type())
ipv6NewCfgStaticRouteGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:ipv6NewCfgStaticRouteGateway.setStatus(_A)
class _Ipv6NewCfgStaticRouteAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Ipv6NewCfgStaticRouteAction_Type.__name__=_C
_Ipv6NewCfgStaticRouteAction_Object=MibTableColumn
ipv6NewCfgStaticRouteAction=_Ipv6NewCfgStaticRouteAction_Object((1,3,6,1,4,1,1872,2,5,3,1,3,5,1,5),_Ipv6NewCfgStaticRouteAction_Type())
ipv6NewCfgStaticRouteAction.setMaxAccess(_D)
if mibBuilder.loadTexts:ipv6NewCfgStaticRouteAction.setStatus(_A)
class _Ipv6NewCfgStaticRouteInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Ipv6NewCfgStaticRouteInterface_Type.__name__=_C
_Ipv6NewCfgStaticRouteInterface_Object=MibTableColumn
ipv6NewCfgStaticRouteInterface=_Ipv6NewCfgStaticRouteInterface_Object((1,3,6,1,4,1,1872,2,5,3,1,3,5,1,6),_Ipv6NewCfgStaticRouteInterface_Type())
ipv6NewCfgStaticRouteInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:ipv6NewCfgStaticRouteInterface.setStatus(_A)
_IpForwardCfg_ObjectIdentity=ObjectIdentity
ipForwardCfg=_IpForwardCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,4))
_IpFwdGeneralCfg_ObjectIdentity=ObjectIdentity
ipFwdGeneralCfg=_IpFwdGeneralCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,4,1))
class _IpFwdCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_P,2),(_Q,3)))
_IpFwdCurCfgState_Type.__name__=_C
_IpFwdCurCfgState_Object=MibScalar
ipFwdCurCfgState=_IpFwdCurCfgState_Object((1,3,6,1,4,1,1872,2,5,3,1,4,1,1),_IpFwdCurCfgState_Type())
ipFwdCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgState.setStatus(_A)
class _IpFwdNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_P,2),(_Q,3)))
_IpFwdNewCfgState_Type.__name__=_C
_IpFwdNewCfgState_Object=MibScalar
ipFwdNewCfgState=_IpFwdNewCfgState_Object((1,3,6,1,4,1,1872,2,5,3,1,4,1,2),_IpFwdNewCfgState_Type())
ipFwdNewCfgState.setMaxAccess(_H)
if mibBuilder.loadTexts:ipFwdNewCfgState.setStatus(_A)
class _IpFwdCurCfgDirectedBcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpFwdCurCfgDirectedBcast_Type.__name__=_C
_IpFwdCurCfgDirectedBcast_Object=MibScalar
ipFwdCurCfgDirectedBcast=_IpFwdCurCfgDirectedBcast_Object((1,3,6,1,4,1,1872,2,5,3,1,4,1,3),_IpFwdCurCfgDirectedBcast_Type())
ipFwdCurCfgDirectedBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgDirectedBcast.setStatus(_A)
class _IpFwdNewCfgDirectedBcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpFwdNewCfgDirectedBcast_Type.__name__=_C
_IpFwdNewCfgDirectedBcast_Object=MibScalar
ipFwdNewCfgDirectedBcast=_IpFwdNewCfgDirectedBcast_Object((1,3,6,1,4,1,1872,2,5,3,1,4,1,4),_IpFwdNewCfgDirectedBcast_Type())
ipFwdNewCfgDirectedBcast.setMaxAccess(_H)
if mibBuilder.loadTexts:ipFwdNewCfgDirectedBcast.setStatus(_A)
class _IpFwdCurCfgNoICMPRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpFwdCurCfgNoICMPRedirect_Type.__name__=_C
_IpFwdCurCfgNoICMPRedirect_Object=MibScalar
ipFwdCurCfgNoICMPRedirect=_IpFwdCurCfgNoICMPRedirect_Object((1,3,6,1,4,1,1872,2,5,3,1,4,1,5),_IpFwdCurCfgNoICMPRedirect_Type())
ipFwdCurCfgNoICMPRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgNoICMPRedirect.setStatus(_A)
class _IpFwdNewCfgNoICMPRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpFwdNewCfgNoICMPRedirect_Type.__name__=_C
_IpFwdNewCfgNoICMPRedirect_Object=MibScalar
ipFwdNewCfgNoICMPRedirect=_IpFwdNewCfgNoICMPRedirect_Object((1,3,6,1,4,1,1872,2,5,3,1,4,1,6),_IpFwdNewCfgNoICMPRedirect_Type())
ipFwdNewCfgNoICMPRedirect.setMaxAccess(_H)
if mibBuilder.loadTexts:ipFwdNewCfgNoICMPRedirect.setStatus(_A)
class _IpFwdCurCfgRtCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpFwdCurCfgRtCache_Type.__name__=_C
_IpFwdCurCfgRtCache_Object=MibScalar
ipFwdCurCfgRtCache=_IpFwdCurCfgRtCache_Object((1,3,6,1,4,1,1872,2,5,3,1,4,1,7),_IpFwdCurCfgRtCache_Type())
ipFwdCurCfgRtCache.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgRtCache.setStatus(_A)
class _IpFwdNewCfgRtCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpFwdNewCfgRtCache_Type.__name__=_C
_IpFwdNewCfgRtCache_Object=MibScalar
ipFwdNewCfgRtCache=_IpFwdNewCfgRtCache_Object((1,3,6,1,4,1,1872,2,5,3,1,4,1,8),_IpFwdNewCfgRtCache_Type())
ipFwdNewCfgRtCache.setMaxAccess(_H)
if mibBuilder.loadTexts:ipFwdNewCfgRtCache.setStatus(_A)
_IpFwdPortTableMaxSize_Type=Integer32
_IpFwdPortTableMaxSize_Object=MibScalar
ipFwdPortTableMaxSize=_IpFwdPortTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,4,2),_IpFwdPortTableMaxSize_Type())
ipFwdPortTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdPortTableMaxSize.setStatus(_A)
_IpFwdCurCfgPortTable_Object=MibTable
ipFwdCurCfgPortTable=_IpFwdCurCfgPortTable_Object((1,3,6,1,4,1,1872,2,5,3,1,4,3))
if mibBuilder.loadTexts:ipFwdCurCfgPortTable.setStatus(_A)
_IpFwdCurCfgPortEntry_Object=MibTableRow
ipFwdCurCfgPortEntry=_IpFwdCurCfgPortEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,4,3,1))
ipFwdCurCfgPortEntry.setIndexNames((0,_G,_y))
if mibBuilder.loadTexts:ipFwdCurCfgPortEntry.setStatus(_A)
_IpFwdCurCfgPortIndex_Type=Integer32
_IpFwdCurCfgPortIndex_Object=MibTableColumn
ipFwdCurCfgPortIndex=_IpFwdCurCfgPortIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,4,3,1,1),_IpFwdCurCfgPortIndex_Type())
ipFwdCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgPortIndex.setStatus(_A)
class _IpFwdCurCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpFwdCurCfgPortState_Type.__name__=_C
_IpFwdCurCfgPortState_Object=MibTableColumn
ipFwdCurCfgPortState=_IpFwdCurCfgPortState_Object((1,3,6,1,4,1,1872,2,5,3,1,4,3,1,2),_IpFwdCurCfgPortState_Type())
ipFwdCurCfgPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgPortState.setStatus(_A)
_IpFwdNewCfgPortTable_Object=MibTable
ipFwdNewCfgPortTable=_IpFwdNewCfgPortTable_Object((1,3,6,1,4,1,1872,2,5,3,1,4,4))
if mibBuilder.loadTexts:ipFwdNewCfgPortTable.setStatus(_A)
_IpFwdNewCfgPortEntry_Object=MibTableRow
ipFwdNewCfgPortEntry=_IpFwdNewCfgPortEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,4,4,1))
ipFwdNewCfgPortEntry.setIndexNames((0,_G,_z))
if mibBuilder.loadTexts:ipFwdNewCfgPortEntry.setStatus(_A)
_IpFwdNewCfgPortIndex_Type=Integer32
_IpFwdNewCfgPortIndex_Object=MibTableColumn
ipFwdNewCfgPortIndex=_IpFwdNewCfgPortIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,4,4,1,1),_IpFwdNewCfgPortIndex_Type())
ipFwdNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdNewCfgPortIndex.setStatus(_A)
class _IpFwdNewCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpFwdNewCfgPortState_Type.__name__=_C
_IpFwdNewCfgPortState_Object=MibTableColumn
ipFwdNewCfgPortState=_IpFwdNewCfgPortState_Object((1,3,6,1,4,1,1872,2,5,3,1,4,4,1,2),_IpFwdNewCfgPortState_Type())
ipFwdNewCfgPortState.setMaxAccess(_H)
if mibBuilder.loadTexts:ipFwdNewCfgPortState.setStatus(_A)
_IpFwdLocalTableMaxSize_Type=Integer32
_IpFwdLocalTableMaxSize_Object=MibScalar
ipFwdLocalTableMaxSize=_IpFwdLocalTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,4,5),_IpFwdLocalTableMaxSize_Type())
ipFwdLocalTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdLocalTableMaxSize.setStatus(_A)
_IpFwdCurCfgLocalTable_Object=MibTable
ipFwdCurCfgLocalTable=_IpFwdCurCfgLocalTable_Object((1,3,6,1,4,1,1872,2,5,3,1,4,6))
if mibBuilder.loadTexts:ipFwdCurCfgLocalTable.setStatus(_A)
_IpFwdCurCfgLocalEntry_Object=MibTableRow
ipFwdCurCfgLocalEntry=_IpFwdCurCfgLocalEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,4,6,1))
ipFwdCurCfgLocalEntry.setIndexNames((0,_G,_A0))
if mibBuilder.loadTexts:ipFwdCurCfgLocalEntry.setStatus(_A)
_IpFwdCurCfgLocalIndex_Type=Integer32
_IpFwdCurCfgLocalIndex_Object=MibTableColumn
ipFwdCurCfgLocalIndex=_IpFwdCurCfgLocalIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,4,6,1,1),_IpFwdCurCfgLocalIndex_Type())
ipFwdCurCfgLocalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgLocalIndex.setStatus(_A)
_IpFwdCurCfgLocalSubnet_Type=IpAddress
_IpFwdCurCfgLocalSubnet_Object=MibTableColumn
ipFwdCurCfgLocalSubnet=_IpFwdCurCfgLocalSubnet_Object((1,3,6,1,4,1,1872,2,5,3,1,4,6,1,2),_IpFwdCurCfgLocalSubnet_Type())
ipFwdCurCfgLocalSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgLocalSubnet.setStatus(_A)
_IpFwdCurCfgLocalMask_Type=IpAddress
_IpFwdCurCfgLocalMask_Object=MibTableColumn
ipFwdCurCfgLocalMask=_IpFwdCurCfgLocalMask_Object((1,3,6,1,4,1,1872,2,5,3,1,4,6,1,3),_IpFwdCurCfgLocalMask_Type())
ipFwdCurCfgLocalMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgLocalMask.setStatus(_A)
_IpFwdNewCfgLocalTable_Object=MibTable
ipFwdNewCfgLocalTable=_IpFwdNewCfgLocalTable_Object((1,3,6,1,4,1,1872,2,5,3,1,4,7))
if mibBuilder.loadTexts:ipFwdNewCfgLocalTable.setStatus(_A)
_IpFwdNewCfgLocalEntry_Object=MibTableRow
ipFwdNewCfgLocalEntry=_IpFwdNewCfgLocalEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,4,7,1))
ipFwdNewCfgLocalEntry.setIndexNames((0,_G,_A1))
if mibBuilder.loadTexts:ipFwdNewCfgLocalEntry.setStatus(_A)
_IpFwdNewCfgLocalIndex_Type=Integer32
_IpFwdNewCfgLocalIndex_Object=MibTableColumn
ipFwdNewCfgLocalIndex=_IpFwdNewCfgLocalIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,4,7,1,1),_IpFwdNewCfgLocalIndex_Type())
ipFwdNewCfgLocalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdNewCfgLocalIndex.setStatus(_A)
_IpFwdNewCfgLocalSubnet_Type=IpAddress
_IpFwdNewCfgLocalSubnet_Object=MibTableColumn
ipFwdNewCfgLocalSubnet=_IpFwdNewCfgLocalSubnet_Object((1,3,6,1,4,1,1872,2,5,3,1,4,7,1,2),_IpFwdNewCfgLocalSubnet_Type())
ipFwdNewCfgLocalSubnet.setMaxAccess(_D)
if mibBuilder.loadTexts:ipFwdNewCfgLocalSubnet.setStatus(_A)
_IpFwdNewCfgLocalMask_Type=IpAddress
_IpFwdNewCfgLocalMask_Object=MibTableColumn
ipFwdNewCfgLocalMask=_IpFwdNewCfgLocalMask_Object((1,3,6,1,4,1,1872,2,5,3,1,4,7,1,3),_IpFwdNewCfgLocalMask_Type())
ipFwdNewCfgLocalMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipFwdNewCfgLocalMask.setStatus(_A)
class _IpFwdNewCfgLocalDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_IpFwdNewCfgLocalDelete_Type.__name__=_C
_IpFwdNewCfgLocalDelete_Object=MibTableColumn
ipFwdNewCfgLocalDelete=_IpFwdNewCfgLocalDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,4,7,1,4),_IpFwdNewCfgLocalDelete_Type())
ipFwdNewCfgLocalDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipFwdNewCfgLocalDelete.setStatus(_A)
_VrrpCfg_ObjectIdentity=ObjectIdentity
vrrpCfg=_VrrpCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,6))
_VrrpGeneral_ObjectIdentity=ObjectIdentity
vrrpGeneral=_VrrpGeneral_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,6,1))
class _VrrpCurCfgGenState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgGenState_Type.__name__=_C
_VrrpCurCfgGenState_Object=MibScalar
vrrpCurCfgGenState=_VrrpCurCfgGenState_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,1),_VrrpCurCfgGenState_Type())
vrrpCurCfgGenState.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenState.setStatus(_A)
class _VrrpNewCfgGenState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgGenState_Type.__name__=_C
_VrrpNewCfgGenState_Object=MibScalar
vrrpNewCfgGenState=_VrrpNewCfgGenState_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,2),_VrrpNewCfgGenState_Type())
vrrpNewCfgGenState.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenState.setStatus(_A)
class _VrrpCurCfgGenTckVirtRtrInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckVirtRtrInc_Type.__name__=_C
_VrrpCurCfgGenTckVirtRtrInc_Object=MibScalar
vrrpCurCfgGenTckVirtRtrInc=_VrrpCurCfgGenTckVirtRtrInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,3),_VrrpCurCfgGenTckVirtRtrInc_Type())
vrrpCurCfgGenTckVirtRtrInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckVirtRtrInc.setStatus(_A)
class _VrrpNewCfgGenTckVirtRtrInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckVirtRtrInc_Type.__name__=_C
_VrrpNewCfgGenTckVirtRtrInc_Object=MibScalar
vrrpNewCfgGenTckVirtRtrInc=_VrrpNewCfgGenTckVirtRtrInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,4),_VrrpNewCfgGenTckVirtRtrInc_Type())
vrrpNewCfgGenTckVirtRtrInc.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenTckVirtRtrInc.setStatus(_A)
class _VrrpCurCfgGenTckIpIntfInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckIpIntfInc_Type.__name__=_C
_VrrpCurCfgGenTckIpIntfInc_Object=MibScalar
vrrpCurCfgGenTckIpIntfInc=_VrrpCurCfgGenTckIpIntfInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,5),_VrrpCurCfgGenTckIpIntfInc_Type())
vrrpCurCfgGenTckIpIntfInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckIpIntfInc.setStatus(_A)
class _VrrpNewCfgGenTckIpIntfInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckIpIntfInc_Type.__name__=_C
_VrrpNewCfgGenTckIpIntfInc_Object=MibScalar
vrrpNewCfgGenTckIpIntfInc=_VrrpNewCfgGenTckIpIntfInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,6),_VrrpNewCfgGenTckIpIntfInc_Type())
vrrpNewCfgGenTckIpIntfInc.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenTckIpIntfInc.setStatus(_A)
class _VrrpCurCfgGenTckVlanPortInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckVlanPortInc_Type.__name__=_C
_VrrpCurCfgGenTckVlanPortInc_Object=MibScalar
vrrpCurCfgGenTckVlanPortInc=_VrrpCurCfgGenTckVlanPortInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,7),_VrrpCurCfgGenTckVlanPortInc_Type())
vrrpCurCfgGenTckVlanPortInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckVlanPortInc.setStatus(_A)
class _VrrpNewCfgGenTckVlanPortInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckVlanPortInc_Type.__name__=_C
_VrrpNewCfgGenTckVlanPortInc_Object=MibScalar
vrrpNewCfgGenTckVlanPortInc=_VrrpNewCfgGenTckVlanPortInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,8),_VrrpNewCfgGenTckVlanPortInc_Type())
vrrpNewCfgGenTckVlanPortInc.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenTckVlanPortInc.setStatus(_A)
class _VrrpCurCfgGenTckL4PortInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckL4PortInc_Type.__name__=_C
_VrrpCurCfgGenTckL4PortInc_Object=MibScalar
vrrpCurCfgGenTckL4PortInc=_VrrpCurCfgGenTckL4PortInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,9),_VrrpCurCfgGenTckL4PortInc_Type())
vrrpCurCfgGenTckL4PortInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckL4PortInc.setStatus(_A)
class _VrrpNewCfgGenTckL4PortInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckL4PortInc_Type.__name__=_C
_VrrpNewCfgGenTckL4PortInc_Object=MibScalar
vrrpNewCfgGenTckL4PortInc=_VrrpNewCfgGenTckL4PortInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,10),_VrrpNewCfgGenTckL4PortInc_Type())
vrrpNewCfgGenTckL4PortInc.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenTckL4PortInc.setStatus(_A)
class _VrrpCurCfgGenTckRServerInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckRServerInc_Type.__name__=_C
_VrrpCurCfgGenTckRServerInc_Object=MibScalar
vrrpCurCfgGenTckRServerInc=_VrrpCurCfgGenTckRServerInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,11),_VrrpCurCfgGenTckRServerInc_Type())
vrrpCurCfgGenTckRServerInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckRServerInc.setStatus(_A)
class _VrrpNewCfgGenTckRServerInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckRServerInc_Type.__name__=_C
_VrrpNewCfgGenTckRServerInc_Object=MibScalar
vrrpNewCfgGenTckRServerInc=_VrrpNewCfgGenTckRServerInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,12),_VrrpNewCfgGenTckRServerInc_Type())
vrrpNewCfgGenTckRServerInc.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenTckRServerInc.setStatus(_A)
class _VrrpCurCfgGenTckHsrpInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckHsrpInc_Type.__name__=_C
_VrrpCurCfgGenTckHsrpInc_Object=MibScalar
vrrpCurCfgGenTckHsrpInc=_VrrpCurCfgGenTckHsrpInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,13),_VrrpCurCfgGenTckHsrpInc_Type())
vrrpCurCfgGenTckHsrpInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckHsrpInc.setStatus(_A)
class _VrrpNewCfgGenTckHsrpInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckHsrpInc_Type.__name__=_C
_VrrpNewCfgGenTckHsrpInc_Object=MibScalar
vrrpNewCfgGenTckHsrpInc=_VrrpNewCfgGenTckHsrpInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,14),_VrrpNewCfgGenTckHsrpInc_Type())
vrrpNewCfgGenTckHsrpInc.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenTckHsrpInc.setStatus(_A)
class _VrrpCurCfgGenHotstandby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgGenHotstandby_Type.__name__=_C
_VrrpCurCfgGenHotstandby_Object=MibScalar
vrrpCurCfgGenHotstandby=_VrrpCurCfgGenHotstandby_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,15),_VrrpCurCfgGenHotstandby_Type())
vrrpCurCfgGenHotstandby.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenHotstandby.setStatus(_A)
class _VrrpNewCfgGenHotstandby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgGenHotstandby_Type.__name__=_C
_VrrpNewCfgGenHotstandby_Object=MibScalar
vrrpNewCfgGenHotstandby=_VrrpNewCfgGenHotstandby_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,16),_VrrpNewCfgGenHotstandby_Type())
vrrpNewCfgGenHotstandby.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenHotstandby.setStatus(_A)
class _VrrpCurCfgGenTckHsrvInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckHsrvInc_Type.__name__=_C
_VrrpCurCfgGenTckHsrvInc_Object=MibScalar
vrrpCurCfgGenTckHsrvInc=_VrrpCurCfgGenTckHsrvInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,17),_VrrpCurCfgGenTckHsrvInc_Type())
vrrpCurCfgGenTckHsrvInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckHsrvInc.setStatus(_A)
class _VrrpNewCfgGenTckHsrvInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckHsrvInc_Type.__name__=_C
_VrrpNewCfgGenTckHsrvInc_Object=MibScalar
vrrpNewCfgGenTckHsrvInc=_VrrpNewCfgGenTckHsrvInc_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,18),_VrrpNewCfgGenTckHsrvInc_Type())
vrrpNewCfgGenTckHsrvInc.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenTckHsrvInc.setStatus(_A)
class _VrrpCurCfgGenHoldoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VrrpCurCfgGenHoldoff_Type.__name__=_C
_VrrpCurCfgGenHoldoff_Object=MibScalar
vrrpCurCfgGenHoldoff=_VrrpCurCfgGenHoldoff_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,19),_VrrpCurCfgGenHoldoff_Type())
vrrpCurCfgGenHoldoff.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenHoldoff.setStatus(_A)
class _VrrpNewCfgGenHoldoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VrrpNewCfgGenHoldoff_Type.__name__=_C
_VrrpNewCfgGenHoldoff_Object=MibScalar
vrrpNewCfgGenHoldoff=_VrrpNewCfgGenHoldoff_Object((1,3,6,1,4,1,1872,2,5,3,1,6,1,20),_VrrpNewCfgGenHoldoff_Type())
vrrpNewCfgGenHoldoff.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpNewCfgGenHoldoff.setStatus(_A)
_VrrpVirtRtrTableMaxSize_Type=Integer32
_VrrpVirtRtrTableMaxSize_Object=MibScalar
vrrpVirtRtrTableMaxSize=_VrrpVirtRtrTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,6,2),_VrrpVirtRtrTableMaxSize_Type())
vrrpVirtRtrTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpVirtRtrTableMaxSize.setStatus(_A)
_VrrpCurCfgVirtRtrTable_Object=MibTable
vrrpCurCfgVirtRtrTable=_VrrpCurCfgVirtRtrTable_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTable.setStatus(_A)
_VrrpCurCfgVirtRtrTableEntry_Object=MibTableRow
vrrpCurCfgVirtRtrTableEntry=_VrrpCurCfgVirtRtrTableEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1))
vrrpCurCfgVirtRtrTableEntry.setIndexNames((0,_G,_A2))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTableEntry.setStatus(_A)
_VrrpCurCfgVirtRtrIndx_Type=Integer32
_VrrpCurCfgVirtRtrIndx_Object=MibTableColumn
vrrpCurCfgVirtRtrIndx=_VrrpCurCfgVirtRtrIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,1),_VrrpCurCfgVirtRtrIndx_Type())
vrrpCurCfgVirtRtrIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrIndx.setStatus(_A)
class _VrrpCurCfgVirtRtrID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_VrrpCurCfgVirtRtrID_Type.__name__=_C
_VrrpCurCfgVirtRtrID_Object=MibTableColumn
vrrpCurCfgVirtRtrID=_VrrpCurCfgVirtRtrID_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,2),_VrrpCurCfgVirtRtrID_Type())
vrrpCurCfgVirtRtrID.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrID.setStatus(_A)
_VrrpCurCfgVirtRtrAddr_Type=IpAddress
_VrrpCurCfgVirtRtrAddr_Object=MibTableColumn
vrrpCurCfgVirtRtrAddr=_VrrpCurCfgVirtRtrAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,3),_VrrpCurCfgVirtRtrAddr_Type())
vrrpCurCfgVirtRtrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrAddr.setStatus(_A)
_VrrpCurCfgVirtRtrIfIndex_Type=Integer32
_VrrpCurCfgVirtRtrIfIndex_Object=MibTableColumn
vrrpCurCfgVirtRtrIfIndex=_VrrpCurCfgVirtRtrIfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,4),_VrrpCurCfgVirtRtrIfIndex_Type())
vrrpCurCfgVirtRtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrIfIndex.setStatus(_A)
class _VrrpCurCfgVirtRtrInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpCurCfgVirtRtrInterval_Type.__name__=_C
_VrrpCurCfgVirtRtrInterval_Object=MibTableColumn
vrrpCurCfgVirtRtrInterval=_VrrpCurCfgVirtRtrInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,5),_VrrpCurCfgVirtRtrInterval_Type())
vrrpCurCfgVirtRtrInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrInterval.setStatus(_A)
class _VrrpCurCfgVirtRtrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpCurCfgVirtRtrPriority_Type.__name__=_C
_VrrpCurCfgVirtRtrPriority_Object=MibTableColumn
vrrpCurCfgVirtRtrPriority=_VrrpCurCfgVirtRtrPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,6),_VrrpCurCfgVirtRtrPriority_Type())
vrrpCurCfgVirtRtrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrPriority.setStatus(_A)
class _VrrpCurCfgVirtRtrPreempt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrPreempt_Type.__name__=_C
_VrrpCurCfgVirtRtrPreempt_Object=MibTableColumn
vrrpCurCfgVirtRtrPreempt=_VrrpCurCfgVirtRtrPreempt_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,7),_VrrpCurCfgVirtRtrPreempt_Type())
vrrpCurCfgVirtRtrPreempt.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrPreempt.setStatus(_A)
class _VrrpCurCfgVirtRtrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrState_Type.__name__=_C
_VrrpCurCfgVirtRtrState_Object=MibTableColumn
vrrpCurCfgVirtRtrState=_VrrpCurCfgVirtRtrState_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,8),_VrrpCurCfgVirtRtrState_Type())
vrrpCurCfgVirtRtrState.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrState.setStatus(_A)
class _VrrpCurCfgVirtRtrSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrSharing_Type.__name__=_C
_VrrpCurCfgVirtRtrSharing_Object=MibTableColumn
vrrpCurCfgVirtRtrSharing=_VrrpCurCfgVirtRtrSharing_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,9),_VrrpCurCfgVirtRtrSharing_Type())
vrrpCurCfgVirtRtrSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrSharing.setStatus(_A)
class _VrrpCurCfgVirtRtrTckVirtRtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrTckVirtRtr_Type.__name__=_C
_VrrpCurCfgVirtRtrTckVirtRtr_Object=MibTableColumn
vrrpCurCfgVirtRtrTckVirtRtr=_VrrpCurCfgVirtRtrTckVirtRtr_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,10),_VrrpCurCfgVirtRtrTckVirtRtr_Type())
vrrpCurCfgVirtRtrTckVirtRtr.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckVirtRtr.setStatus(_A)
class _VrrpCurCfgVirtRtrTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrTckIpIntf_Type.__name__=_C
_VrrpCurCfgVirtRtrTckIpIntf_Object=MibTableColumn
vrrpCurCfgVirtRtrTckIpIntf=_VrrpCurCfgVirtRtrTckIpIntf_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,11),_VrrpCurCfgVirtRtrTckIpIntf_Type())
vrrpCurCfgVirtRtrTckIpIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckIpIntf.setStatus(_A)
class _VrrpCurCfgVirtRtrTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrTckVlanPort_Type.__name__=_C
_VrrpCurCfgVirtRtrTckVlanPort_Object=MibTableColumn
vrrpCurCfgVirtRtrTckVlanPort=_VrrpCurCfgVirtRtrTckVlanPort_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,12),_VrrpCurCfgVirtRtrTckVlanPort_Type())
vrrpCurCfgVirtRtrTckVlanPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckVlanPort.setStatus(_A)
class _VrrpCurCfgVirtRtrTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrTckL4Port_Type.__name__=_C
_VrrpCurCfgVirtRtrTckL4Port_Object=MibTableColumn
vrrpCurCfgVirtRtrTckL4Port=_VrrpCurCfgVirtRtrTckL4Port_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,13),_VrrpCurCfgVirtRtrTckL4Port_Type())
vrrpCurCfgVirtRtrTckL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckL4Port.setStatus(_A)
class _VrrpCurCfgVirtRtrTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrTckRServer_Type.__name__=_C
_VrrpCurCfgVirtRtrTckRServer_Object=MibTableColumn
vrrpCurCfgVirtRtrTckRServer=_VrrpCurCfgVirtRtrTckRServer_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,14),_VrrpCurCfgVirtRtrTckRServer_Type())
vrrpCurCfgVirtRtrTckRServer.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckRServer.setStatus(_A)
class _VrrpCurCfgVirtRtrTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrTckHsrp_Type.__name__=_C
_VrrpCurCfgVirtRtrTckHsrp_Object=MibTableColumn
vrrpCurCfgVirtRtrTckHsrp=_VrrpCurCfgVirtRtrTckHsrp_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,15),_VrrpCurCfgVirtRtrTckHsrp_Type())
vrrpCurCfgVirtRtrTckHsrp.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckHsrp.setStatus(_A)
class _VrrpCurCfgVirtRtrTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrTckHsrv_Type.__name__=_C
_VrrpCurCfgVirtRtrTckHsrv_Object=MibTableColumn
vrrpCurCfgVirtRtrTckHsrv=_VrrpCurCfgVirtRtrTckHsrv_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,16),_VrrpCurCfgVirtRtrTckHsrv_Type())
vrrpCurCfgVirtRtrTckHsrv.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckHsrv.setStatus(_A)
class _VrrpCurCfgVirtRtrVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_VrrpCurCfgVirtRtrVersion_Type.__name__=_C
_VrrpCurCfgVirtRtrVersion_Object=MibTableColumn
vrrpCurCfgVirtRtrVersion=_VrrpCurCfgVirtRtrVersion_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,17),_VrrpCurCfgVirtRtrVersion_Type())
vrrpCurCfgVirtRtrVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVersion.setStatus(_A)
class _VrrpCurCfgVirtRtrIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_VrrpCurCfgVirtRtrIpv6Addr_Type.__name__=_I
_VrrpCurCfgVirtRtrIpv6Addr_Object=MibTableColumn
vrrpCurCfgVirtRtrIpv6Addr=_VrrpCurCfgVirtRtrIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,18),_VrrpCurCfgVirtRtrIpv6Addr_Type())
vrrpCurCfgVirtRtrIpv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrIpv6Addr.setStatus(_A)
class _VrrpCurCfgVirtRtrIpv6Interval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1045))
_VrrpCurCfgVirtRtrIpv6Interval_Type.__name__=_C
_VrrpCurCfgVirtRtrIpv6Interval_Object=MibTableColumn
vrrpCurCfgVirtRtrIpv6Interval=_VrrpCurCfgVirtRtrIpv6Interval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,3,1,19),_VrrpCurCfgVirtRtrIpv6Interval_Type())
vrrpCurCfgVirtRtrIpv6Interval.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrIpv6Interval.setStatus(_A)
_VrrpNewCfgVirtRtrTable_Object=MibTable
vrrpNewCfgVirtRtrTable=_VrrpNewCfgVirtRtrTable_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTable.setStatus(_A)
_VrrpNewCfgVirtRtrTableEntry_Object=MibTableRow
vrrpNewCfgVirtRtrTableEntry=_VrrpNewCfgVirtRtrTableEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1))
vrrpNewCfgVirtRtrTableEntry.setIndexNames((0,_G,_A3))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTableEntry.setStatus(_A)
_VrrpNewCfgVirtRtrIndx_Type=Integer32
_VrrpNewCfgVirtRtrIndx_Object=MibTableColumn
vrrpNewCfgVirtRtrIndx=_VrrpNewCfgVirtRtrIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,1),_VrrpNewCfgVirtRtrIndx_Type())
vrrpNewCfgVirtRtrIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrIndx.setStatus(_A)
class _VrrpNewCfgVirtRtrID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_VrrpNewCfgVirtRtrID_Type.__name__=_C
_VrrpNewCfgVirtRtrID_Object=MibTableColumn
vrrpNewCfgVirtRtrID=_VrrpNewCfgVirtRtrID_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,2),_VrrpNewCfgVirtRtrID_Type())
vrrpNewCfgVirtRtrID.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrID.setStatus(_A)
_VrrpNewCfgVirtRtrAddr_Type=IpAddress
_VrrpNewCfgVirtRtrAddr_Object=MibTableColumn
vrrpNewCfgVirtRtrAddr=_VrrpNewCfgVirtRtrAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,3),_VrrpNewCfgVirtRtrAddr_Type())
vrrpNewCfgVirtRtrAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrAddr.setStatus(_A)
_VrrpNewCfgVirtRtrIfIndex_Type=Integer32
_VrrpNewCfgVirtRtrIfIndex_Object=MibTableColumn
vrrpNewCfgVirtRtrIfIndex=_VrrpNewCfgVirtRtrIfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,4),_VrrpNewCfgVirtRtrIfIndex_Type())
vrrpNewCfgVirtRtrIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrIfIndex.setStatus(_A)
class _VrrpNewCfgVirtRtrInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpNewCfgVirtRtrInterval_Type.__name__=_C
_VrrpNewCfgVirtRtrInterval_Object=MibTableColumn
vrrpNewCfgVirtRtrInterval=_VrrpNewCfgVirtRtrInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,5),_VrrpNewCfgVirtRtrInterval_Type())
vrrpNewCfgVirtRtrInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrInterval.setStatus(_A)
class _VrrpNewCfgVirtRtrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpNewCfgVirtRtrPriority_Type.__name__=_C
_VrrpNewCfgVirtRtrPriority_Object=MibTableColumn
vrrpNewCfgVirtRtrPriority=_VrrpNewCfgVirtRtrPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,6),_VrrpNewCfgVirtRtrPriority_Type())
vrrpNewCfgVirtRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrPriority.setStatus(_A)
class _VrrpNewCfgVirtRtrPreempt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrPreempt_Type.__name__=_C
_VrrpNewCfgVirtRtrPreempt_Object=MibTableColumn
vrrpNewCfgVirtRtrPreempt=_VrrpNewCfgVirtRtrPreempt_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,7),_VrrpNewCfgVirtRtrPreempt_Type())
vrrpNewCfgVirtRtrPreempt.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrPreempt.setStatus(_A)
class _VrrpNewCfgVirtRtrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrState_Type.__name__=_C
_VrrpNewCfgVirtRtrState_Object=MibTableColumn
vrrpNewCfgVirtRtrState=_VrrpNewCfgVirtRtrState_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,8),_VrrpNewCfgVirtRtrState_Type())
vrrpNewCfgVirtRtrState.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrState.setStatus(_A)
class _VrrpNewCfgVirtRtrDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_VrrpNewCfgVirtRtrDelete_Type.__name__=_C
_VrrpNewCfgVirtRtrDelete_Object=MibTableColumn
vrrpNewCfgVirtRtrDelete=_VrrpNewCfgVirtRtrDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,9),_VrrpNewCfgVirtRtrDelete_Type())
vrrpNewCfgVirtRtrDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrDelete.setStatus(_A)
class _VrrpNewCfgVirtRtrSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrSharing_Type.__name__=_C
_VrrpNewCfgVirtRtrSharing_Object=MibTableColumn
vrrpNewCfgVirtRtrSharing=_VrrpNewCfgVirtRtrSharing_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,10),_VrrpNewCfgVirtRtrSharing_Type())
vrrpNewCfgVirtRtrSharing.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrSharing.setStatus(_A)
class _VrrpNewCfgVirtRtrTckVirtRtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrTckVirtRtr_Type.__name__=_C
_VrrpNewCfgVirtRtrTckVirtRtr_Object=MibTableColumn
vrrpNewCfgVirtRtrTckVirtRtr=_VrrpNewCfgVirtRtrTckVirtRtr_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,11),_VrrpNewCfgVirtRtrTckVirtRtr_Type())
vrrpNewCfgVirtRtrTckVirtRtr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckVirtRtr.setStatus(_A)
class _VrrpNewCfgVirtRtrTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrTckIpIntf_Type.__name__=_C
_VrrpNewCfgVirtRtrTckIpIntf_Object=MibTableColumn
vrrpNewCfgVirtRtrTckIpIntf=_VrrpNewCfgVirtRtrTckIpIntf_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,12),_VrrpNewCfgVirtRtrTckIpIntf_Type())
vrrpNewCfgVirtRtrTckIpIntf.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckIpIntf.setStatus(_A)
class _VrrpNewCfgVirtRtrTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrTckVlanPort_Type.__name__=_C
_VrrpNewCfgVirtRtrTckVlanPort_Object=MibTableColumn
vrrpNewCfgVirtRtrTckVlanPort=_VrrpNewCfgVirtRtrTckVlanPort_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,13),_VrrpNewCfgVirtRtrTckVlanPort_Type())
vrrpNewCfgVirtRtrTckVlanPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckVlanPort.setStatus(_A)
class _VrrpNewCfgVirtRtrTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrTckL4Port_Type.__name__=_C
_VrrpNewCfgVirtRtrTckL4Port_Object=MibTableColumn
vrrpNewCfgVirtRtrTckL4Port=_VrrpNewCfgVirtRtrTckL4Port_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,14),_VrrpNewCfgVirtRtrTckL4Port_Type())
vrrpNewCfgVirtRtrTckL4Port.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckL4Port.setStatus(_A)
class _VrrpNewCfgVirtRtrTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrTckRServer_Type.__name__=_C
_VrrpNewCfgVirtRtrTckRServer_Object=MibTableColumn
vrrpNewCfgVirtRtrTckRServer=_VrrpNewCfgVirtRtrTckRServer_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,15),_VrrpNewCfgVirtRtrTckRServer_Type())
vrrpNewCfgVirtRtrTckRServer.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckRServer.setStatus(_A)
class _VrrpNewCfgVirtRtrTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrTckHsrp_Type.__name__=_C
_VrrpNewCfgVirtRtrTckHsrp_Object=MibTableColumn
vrrpNewCfgVirtRtrTckHsrp=_VrrpNewCfgVirtRtrTckHsrp_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,16),_VrrpNewCfgVirtRtrTckHsrp_Type())
vrrpNewCfgVirtRtrTckHsrp.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckHsrp.setStatus(_A)
class _VrrpNewCfgVirtRtrTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrTckHsrv_Type.__name__=_C
_VrrpNewCfgVirtRtrTckHsrv_Object=MibTableColumn
vrrpNewCfgVirtRtrTckHsrv=_VrrpNewCfgVirtRtrTckHsrv_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,17),_VrrpNewCfgVirtRtrTckHsrv_Type())
vrrpNewCfgVirtRtrTckHsrv.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckHsrv.setStatus(_A)
class _VrrpNewCfgVirtRtrVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_VrrpNewCfgVirtRtrVersion_Type.__name__=_C
_VrrpNewCfgVirtRtrVersion_Object=MibTableColumn
vrrpNewCfgVirtRtrVersion=_VrrpNewCfgVirtRtrVersion_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,18),_VrrpNewCfgVirtRtrVersion_Type())
vrrpNewCfgVirtRtrVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVersion.setStatus(_A)
class _VrrpNewCfgVirtRtrIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_VrrpNewCfgVirtRtrIpv6Addr_Type.__name__=_I
_VrrpNewCfgVirtRtrIpv6Addr_Object=MibTableColumn
vrrpNewCfgVirtRtrIpv6Addr=_VrrpNewCfgVirtRtrIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,19),_VrrpNewCfgVirtRtrIpv6Addr_Type())
vrrpNewCfgVirtRtrIpv6Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrIpv6Addr.setStatus(_A)
class _VrrpNewCfgVirtRtrIpv6Interval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_VrrpNewCfgVirtRtrIpv6Interval_Type.__name__=_C
_VrrpNewCfgVirtRtrIpv6Interval_Object=MibTableColumn
vrrpNewCfgVirtRtrIpv6Interval=_VrrpNewCfgVirtRtrIpv6Interval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,4,1,20),_VrrpNewCfgVirtRtrIpv6Interval_Type())
vrrpNewCfgVirtRtrIpv6Interval.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrIpv6Interval.setStatus(_A)
_VrrpIfTableMaxSize_Type=Integer32
_VrrpIfTableMaxSize_Object=MibScalar
vrrpIfTableMaxSize=_VrrpIfTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,6,5),_VrrpIfTableMaxSize_Type())
vrrpIfTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpIfTableMaxSize.setStatus(_A)
_VrrpCurCfgIfTable_Object=MibTable
vrrpCurCfgIfTable=_VrrpCurCfgIfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,6,6))
if mibBuilder.loadTexts:vrrpCurCfgIfTable.setStatus(_A)
_VrrpCurCfgIfTableEntry_Object=MibTableRow
vrrpCurCfgIfTableEntry=_VrrpCurCfgIfTableEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,6,6,1))
vrrpCurCfgIfTableEntry.setIndexNames((0,_G,_A4))
if mibBuilder.loadTexts:vrrpCurCfgIfTableEntry.setStatus(_A)
_VrrpCurCfgIfIndx_Type=Integer32
_VrrpCurCfgIfIndx_Object=MibTableColumn
vrrpCurCfgIfIndx=_VrrpCurCfgIfIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,6,6,1,1),_VrrpCurCfgIfIndx_Type())
vrrpCurCfgIfIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgIfIndx.setStatus(_A)
class _VrrpCurCfgIfAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_A5,2)))
_VrrpCurCfgIfAuthType_Type.__name__=_C
_VrrpCurCfgIfAuthType_Object=MibTableColumn
vrrpCurCfgIfAuthType=_VrrpCurCfgIfAuthType_Object((1,3,6,1,4,1,1872,2,5,3,1,6,6,1,2),_VrrpCurCfgIfAuthType_Type())
vrrpCurCfgIfAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgIfAuthType.setStatus(_A)
class _VrrpCurCfgIfPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_VrrpCurCfgIfPasswd_Type.__name__=_I
_VrrpCurCfgIfPasswd_Object=MibTableColumn
vrrpCurCfgIfPasswd=_VrrpCurCfgIfPasswd_Object((1,3,6,1,4,1,1872,2,5,3,1,6,6,1,3),_VrrpCurCfgIfPasswd_Type())
vrrpCurCfgIfPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgIfPasswd.setStatus(_A)
_VrrpCurCfgIfIpAddr_Type=IpAddress
_VrrpCurCfgIfIpAddr_Object=MibTableColumn
vrrpCurCfgIfIpAddr=_VrrpCurCfgIfIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,6,6,1,4),_VrrpCurCfgIfIpAddr_Type())
vrrpCurCfgIfIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgIfIpAddr.setStatus(_A)
_VrrpNewCfgIfTable_Object=MibTable
vrrpNewCfgIfTable=_VrrpNewCfgIfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,6,7))
if mibBuilder.loadTexts:vrrpNewCfgIfTable.setStatus(_A)
_VrrpNewCfgIfTableEntry_Object=MibTableRow
vrrpNewCfgIfTableEntry=_VrrpNewCfgIfTableEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,6,7,1))
vrrpNewCfgIfTableEntry.setIndexNames((0,_G,_A6))
if mibBuilder.loadTexts:vrrpNewCfgIfTableEntry.setStatus(_A)
_VrrpNewCfgIfIndx_Type=Integer32
_VrrpNewCfgIfIndx_Object=MibTableColumn
vrrpNewCfgIfIndx=_VrrpNewCfgIfIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,6,7,1,1),_VrrpNewCfgIfIndx_Type())
vrrpNewCfgIfIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpNewCfgIfIndx.setStatus(_A)
class _VrrpNewCfgIfAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_A5,2)))
_VrrpNewCfgIfAuthType_Type.__name__=_C
_VrrpNewCfgIfAuthType_Object=MibTableColumn
vrrpNewCfgIfAuthType=_VrrpNewCfgIfAuthType_Object((1,3,6,1,4,1,1872,2,5,3,1,6,7,1,2),_VrrpNewCfgIfAuthType_Type())
vrrpNewCfgIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgIfAuthType.setStatus(_A)
class _VrrpNewCfgIfPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_VrrpNewCfgIfPasswd_Type.__name__=_I
_VrrpNewCfgIfPasswd_Object=MibTableColumn
vrrpNewCfgIfPasswd=_VrrpNewCfgIfPasswd_Object((1,3,6,1,4,1,1872,2,5,3,1,6,7,1,3),_VrrpNewCfgIfPasswd_Type())
vrrpNewCfgIfPasswd.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgIfPasswd.setStatus(_A)
class _VrrpNewCfgIfDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_VrrpNewCfgIfDelete_Type.__name__=_C
_VrrpNewCfgIfDelete_Object=MibTableColumn
vrrpNewCfgIfDelete=_VrrpNewCfgIfDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,6,7,1,4),_VrrpNewCfgIfDelete_Type())
vrrpNewCfgIfDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgIfDelete.setStatus(_A)
_VrrpVirtRtrGrpTableMaxSize_Type=Integer32
_VrrpVirtRtrGrpTableMaxSize_Object=MibScalar
vrrpVirtRtrGrpTableMaxSize=_VrrpVirtRtrGrpTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,6,8),_VrrpVirtRtrGrpTableMaxSize_Type())
vrrpVirtRtrGrpTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpVirtRtrGrpTableMaxSize.setStatus(_A)
_VrrpCurCfgVirtRtrGrpTable_Object=MibTable
vrrpCurCfgVirtRtrGrpTable=_VrrpCurCfgVirtRtrGrpTable_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTable.setStatus(_A)
_VrrpCurCfgVirtRtrGrpTableEntry_Object=MibTableRow
vrrpCurCfgVirtRtrGrpTableEntry=_VrrpCurCfgVirtRtrGrpTableEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1))
vrrpCurCfgVirtRtrGrpTableEntry.setIndexNames((0,_G,_A7))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTableEntry.setStatus(_A)
_VrrpCurCfgVirtRtrGrpIndx_Type=Integer32
_VrrpCurCfgVirtRtrGrpIndx_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpIndx=_VrrpCurCfgVirtRtrGrpIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,1),_VrrpCurCfgVirtRtrGrpIndx_Type())
vrrpCurCfgVirtRtrGrpIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpIndx.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_VrrpCurCfgVirtRtrGrpID_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpID_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpID=_VrrpCurCfgVirtRtrGrpID_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,2),_VrrpCurCfgVirtRtrGrpID_Type())
vrrpCurCfgVirtRtrGrpID.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpID.setStatus(_A)
_VrrpCurCfgVirtRtrGrpIfIndex_Type=Integer32
_VrrpCurCfgVirtRtrGrpIfIndex_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpIfIndex=_VrrpCurCfgVirtRtrGrpIfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,3),_VrrpCurCfgVirtRtrGrpIfIndex_Type())
vrrpCurCfgVirtRtrGrpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpIfIndex.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpCurCfgVirtRtrGrpInterval_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpInterval_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpInterval=_VrrpCurCfgVirtRtrGrpInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,4),_VrrpCurCfgVirtRtrGrpInterval_Type())
vrrpCurCfgVirtRtrGrpInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpInterval.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpCurCfgVirtRtrGrpPriority_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpPriority_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpPriority=_VrrpCurCfgVirtRtrGrpPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,5),_VrrpCurCfgVirtRtrGrpPriority_Type())
vrrpCurCfgVirtRtrGrpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpPriority.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpPreempt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpPreempt_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpPreempt_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpPreempt=_VrrpCurCfgVirtRtrGrpPreempt_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,6),_VrrpCurCfgVirtRtrGrpPreempt_Type())
vrrpCurCfgVirtRtrGrpPreempt.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpPreempt.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpState_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpState_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpState=_VrrpCurCfgVirtRtrGrpState_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,7),_VrrpCurCfgVirtRtrGrpState_Type())
vrrpCurCfgVirtRtrGrpState.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpState.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpSharing_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpSharing_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpSharing=_VrrpCurCfgVirtRtrGrpSharing_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,8),_VrrpCurCfgVirtRtrGrpSharing_Type())
vrrpCurCfgVirtRtrGrpSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpSharing.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckVirtRtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpTckVirtRtr_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckVirtRtr_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckVirtRtr=_VrrpCurCfgVirtRtrGrpTckVirtRtr_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,9),_VrrpCurCfgVirtRtrGrpTckVirtRtr_Type())
vrrpCurCfgVirtRtrGrpTckVirtRtr.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckVirtRtr.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpTckIpIntf_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckIpIntf_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckIpIntf=_VrrpCurCfgVirtRtrGrpTckIpIntf_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,10),_VrrpCurCfgVirtRtrGrpTckIpIntf_Type())
vrrpCurCfgVirtRtrGrpTckIpIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckIpIntf.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpTckVlanPort_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckVlanPort_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckVlanPort=_VrrpCurCfgVirtRtrGrpTckVlanPort_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,11),_VrrpCurCfgVirtRtrGrpTckVlanPort_Type())
vrrpCurCfgVirtRtrGrpTckVlanPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckVlanPort.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpTckL4Port_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckL4Port_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckL4Port=_VrrpCurCfgVirtRtrGrpTckL4Port_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,12),_VrrpCurCfgVirtRtrGrpTckL4Port_Type())
vrrpCurCfgVirtRtrGrpTckL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckL4Port.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpTckRServer_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckRServer_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckRServer=_VrrpCurCfgVirtRtrGrpTckRServer_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,13),_VrrpCurCfgVirtRtrGrpTckRServer_Type())
vrrpCurCfgVirtRtrGrpTckRServer.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckRServer.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpTckHsrp_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckHsrp_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckHsrp=_VrrpCurCfgVirtRtrGrpTckHsrp_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,14),_VrrpCurCfgVirtRtrGrpTckHsrp_Type())
vrrpCurCfgVirtRtrGrpTckHsrp.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckHsrp.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrGrpTckHsrv_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckHsrv_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckHsrv=_VrrpCurCfgVirtRtrGrpTckHsrv_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,15),_VrrpCurCfgVirtRtrGrpTckHsrv_Type())
vrrpCurCfgVirtRtrGrpTckHsrv.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckHsrv.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_VrrpCurCfgVirtRtrGrpVersion_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpVersion_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpVersion=_VrrpCurCfgVirtRtrGrpVersion_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,16),_VrrpCurCfgVirtRtrGrpVersion_Type())
vrrpCurCfgVirtRtrGrpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpVersion.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpIpv6Interval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_VrrpCurCfgVirtRtrGrpIpv6Interval_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpIpv6Interval_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpIpv6Interval=_VrrpCurCfgVirtRtrGrpIpv6Interval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,9,1,17),_VrrpCurCfgVirtRtrGrpIpv6Interval_Type())
vrrpCurCfgVirtRtrGrpIpv6Interval.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpIpv6Interval.setStatus(_A)
_VrrpNewCfgVirtRtrGrpTable_Object=MibTable
vrrpNewCfgVirtRtrGrpTable=_VrrpNewCfgVirtRtrGrpTable_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTable.setStatus(_A)
_VrrpNewCfgVirtRtrGrpTableEntry_Object=MibTableRow
vrrpNewCfgVirtRtrGrpTableEntry=_VrrpNewCfgVirtRtrGrpTableEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1))
vrrpNewCfgVirtRtrGrpTableEntry.setIndexNames((0,_G,_A8))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTableEntry.setStatus(_A)
_VrrpNewCfgVirtRtrGrpIndx_Type=Integer32
_VrrpNewCfgVirtRtrGrpIndx_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpIndx=_VrrpNewCfgVirtRtrGrpIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,1),_VrrpNewCfgVirtRtrGrpIndx_Type())
vrrpNewCfgVirtRtrGrpIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpIndx.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_VrrpNewCfgVirtRtrGrpID_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpID_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpID=_VrrpNewCfgVirtRtrGrpID_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,2),_VrrpNewCfgVirtRtrGrpID_Type())
vrrpNewCfgVirtRtrGrpID.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpID.setStatus(_A)
_VrrpNewCfgVirtRtrGrpIfIndex_Type=Integer32
_VrrpNewCfgVirtRtrGrpIfIndex_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpIfIndex=_VrrpNewCfgVirtRtrGrpIfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,3),_VrrpNewCfgVirtRtrGrpIfIndex_Type())
vrrpNewCfgVirtRtrGrpIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpIfIndex.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpNewCfgVirtRtrGrpInterval_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpInterval_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpInterval=_VrrpNewCfgVirtRtrGrpInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,4),_VrrpNewCfgVirtRtrGrpInterval_Type())
vrrpNewCfgVirtRtrGrpInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpInterval.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpNewCfgVirtRtrGrpPriority_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpPriority_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpPriority=_VrrpNewCfgVirtRtrGrpPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,5),_VrrpNewCfgVirtRtrGrpPriority_Type())
vrrpNewCfgVirtRtrGrpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpPriority.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpPreempt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpPreempt_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpPreempt_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpPreempt=_VrrpNewCfgVirtRtrGrpPreempt_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,6),_VrrpNewCfgVirtRtrGrpPreempt_Type())
vrrpNewCfgVirtRtrGrpPreempt.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpPreempt.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpState_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpState_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpState=_VrrpNewCfgVirtRtrGrpState_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,7),_VrrpNewCfgVirtRtrGrpState_Type())
vrrpNewCfgVirtRtrGrpState.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpState.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_VrrpNewCfgVirtRtrGrpDelete_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpDelete_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpDelete=_VrrpNewCfgVirtRtrGrpDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,8),_VrrpNewCfgVirtRtrGrpDelete_Type())
vrrpNewCfgVirtRtrGrpDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpDelete.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpSharing_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpSharing_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpSharing=_VrrpNewCfgVirtRtrGrpSharing_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,9),_VrrpNewCfgVirtRtrGrpSharing_Type())
vrrpNewCfgVirtRtrGrpSharing.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpSharing.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckVirtRtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpTckVirtRtr_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckVirtRtr_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckVirtRtr=_VrrpNewCfgVirtRtrGrpTckVirtRtr_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,10),_VrrpNewCfgVirtRtrGrpTckVirtRtr_Type())
vrrpNewCfgVirtRtrGrpTckVirtRtr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckVirtRtr.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpTckIpIntf_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckIpIntf_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckIpIntf=_VrrpNewCfgVirtRtrGrpTckIpIntf_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,11),_VrrpNewCfgVirtRtrGrpTckIpIntf_Type())
vrrpNewCfgVirtRtrGrpTckIpIntf.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckIpIntf.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpTckVlanPort_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckVlanPort_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckVlanPort=_VrrpNewCfgVirtRtrGrpTckVlanPort_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,12),_VrrpNewCfgVirtRtrGrpTckVlanPort_Type())
vrrpNewCfgVirtRtrGrpTckVlanPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckVlanPort.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpTckL4Port_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckL4Port_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckL4Port=_VrrpNewCfgVirtRtrGrpTckL4Port_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,13),_VrrpNewCfgVirtRtrGrpTckL4Port_Type())
vrrpNewCfgVirtRtrGrpTckL4Port.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckL4Port.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpTckRServer_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckRServer_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckRServer=_VrrpNewCfgVirtRtrGrpTckRServer_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,14),_VrrpNewCfgVirtRtrGrpTckRServer_Type())
vrrpNewCfgVirtRtrGrpTckRServer.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckRServer.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpTckHsrp_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckHsrp_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckHsrp=_VrrpNewCfgVirtRtrGrpTckHsrp_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,15),_VrrpNewCfgVirtRtrGrpTckHsrp_Type())
vrrpNewCfgVirtRtrGrpTckHsrp.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckHsrp.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrGrpTckHsrv_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckHsrv_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckHsrv=_VrrpNewCfgVirtRtrGrpTckHsrv_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,16),_VrrpNewCfgVirtRtrGrpTckHsrv_Type())
vrrpNewCfgVirtRtrGrpTckHsrv.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckHsrv.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_VrrpNewCfgVirtRtrGrpVersion_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpVersion_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpVersion=_VrrpNewCfgVirtRtrGrpVersion_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,17),_VrrpNewCfgVirtRtrGrpVersion_Type())
vrrpNewCfgVirtRtrGrpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpVersion.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpIpv6Interval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_VrrpNewCfgVirtRtrGrpIpv6Interval_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpIpv6Interval_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpIpv6Interval=_VrrpNewCfgVirtRtrGrpIpv6Interval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,10,1,18),_VrrpNewCfgVirtRtrGrpIpv6Interval_Type())
vrrpNewCfgVirtRtrGrpIpv6Interval.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpIpv6Interval.setStatus(_A)
_VrrpVirtRtrVrGrpTableMaxSize_Type=Integer32
_VrrpVirtRtrVrGrpTableMaxSize_Object=MibScalar
vrrpVirtRtrVrGrpTableMaxSize=_VrrpVirtRtrVrGrpTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,6,11),_VrrpVirtRtrVrGrpTableMaxSize_Type())
vrrpVirtRtrVrGrpTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpVirtRtrVrGrpTableMaxSize.setStatus(_A)
_VrrpCurCfgVirtRtrVrGrpTable_Object=MibTable
vrrpCurCfgVirtRtrVrGrpTable=_VrrpCurCfgVirtRtrVrGrpTable_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpTable.setStatus(_A)
_VrrpCurCfgVirtRtrVrGrpTableEntry_Object=MibTableRow
vrrpCurCfgVirtRtrVrGrpTableEntry=_VrrpCurCfgVirtRtrVrGrpTableEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1))
vrrpCurCfgVirtRtrVrGrpTableEntry.setIndexNames((0,_G,_A9))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpTableEntry.setStatus(_A)
_VrrpCurCfgVirtRtrVrGrpIndx_Type=Integer32
_VrrpCurCfgVirtRtrVrGrpIndx_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpIndx=_VrrpCurCfgVirtRtrVrGrpIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,1),_VrrpCurCfgVirtRtrVrGrpIndx_Type())
vrrpCurCfgVirtRtrVrGrpIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpIndx.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_VrrpCurCfgVirtRtrVrGrpName_Type.__name__=_I
_VrrpCurCfgVirtRtrVrGrpName_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpName=_VrrpCurCfgVirtRtrVrGrpName_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,2),_VrrpCurCfgVirtRtrVrGrpName_Type())
vrrpCurCfgVirtRtrVrGrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpName.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrVrGrpState_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpState_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpState=_VrrpCurCfgVirtRtrVrGrpState_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,3),_VrrpCurCfgVirtRtrVrGrpState_Type())
vrrpCurCfgVirtRtrVrGrpState.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpState.setStatus(_A)
_VrrpCurCfgVirtRtrVrGrpBmap_Type=OctetString
_VrrpCurCfgVirtRtrVrGrpBmap_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpBmap=_VrrpCurCfgVirtRtrVrGrpBmap_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,4),_VrrpCurCfgVirtRtrVrGrpBmap_Type())
vrrpCurCfgVirtRtrVrGrpBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpBmap.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpCurCfgVirtRtrVrGrpPriority_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpPriority_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpPriority=_VrrpCurCfgVirtRtrVrGrpPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,5),_VrrpCurCfgVirtRtrVrGrpPriority_Type())
vrrpCurCfgVirtRtrVrGrpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpPriority.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrVrGrpTckIpIntf_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpTckIpIntf_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckIpIntf=_VrrpCurCfgVirtRtrVrGrpTckIpIntf_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,6),_VrrpCurCfgVirtRtrVrGrpTckIpIntf_Type())
vrrpCurCfgVirtRtrVrGrpTckIpIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpTckIpIntf.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrVrGrpTckVlanPort_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpTckVlanPort_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckVlanPort=_VrrpCurCfgVirtRtrVrGrpTckVlanPort_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,7),_VrrpCurCfgVirtRtrVrGrpTckVlanPort_Type())
vrrpCurCfgVirtRtrVrGrpTckVlanPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpTckVlanPort.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrVrGrpTckL4Port_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpTckL4Port_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckL4Port=_VrrpCurCfgVirtRtrVrGrpTckL4Port_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,8),_VrrpCurCfgVirtRtrVrGrpTckL4Port_Type())
vrrpCurCfgVirtRtrVrGrpTckL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpTckL4Port.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrVrGrpTckRServer_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpTckRServer_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckRServer=_VrrpCurCfgVirtRtrVrGrpTckRServer_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,9),_VrrpCurCfgVirtRtrVrGrpTckRServer_Type())
vrrpCurCfgVirtRtrVrGrpTckRServer.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpTckRServer.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrVrGrpTckHsrp_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpTckHsrp_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckHsrp=_VrrpCurCfgVirtRtrVrGrpTckHsrp_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,10),_VrrpCurCfgVirtRtrVrGrpTckHsrp_Type())
vrrpCurCfgVirtRtrVrGrpTckHsrp.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpTckHsrp.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrVrGrpTckHsrv_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpTckHsrv_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckHsrv=_VrrpCurCfgVirtRtrVrGrpTckHsrv_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,11),_VrrpCurCfgVirtRtrVrGrpTckHsrv_Type())
vrrpCurCfgVirtRtrVrGrpTckHsrv.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpTckHsrv.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo=_VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,12),_VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Type())
vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_VrrpCurCfgVirtRtrVrGrpAdd_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpAdd_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpAdd=_VrrpCurCfgVirtRtrVrGrpAdd_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,13),_VrrpCurCfgVirtRtrVrGrpAdd_Type())
vrrpCurCfgVirtRtrVrGrpAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpAdd.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpAdverInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpCurCfgVirtRtrVrGrpAdverInterval_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpAdverInterval_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpAdverInterval=_VrrpCurCfgVirtRtrVrGrpAdverInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,14),_VrrpCurCfgVirtRtrVrGrpAdverInterval_Type())
vrrpCurCfgVirtRtrVrGrpAdverInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpAdverInterval.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpPreemption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrVrGrpPreemption_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpPreemption_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpPreemption=_VrrpCurCfgVirtRtrVrGrpPreemption_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,15),_VrrpCurCfgVirtRtrVrGrpPreemption_Type())
vrrpCurCfgVirtRtrVrGrpPreemption.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpPreemption.setStatus(_A)
class _VrrpCurCfgVirtRtrVrGrpSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpCurCfgVirtRtrVrGrpSharing_Type.__name__=_C
_VrrpCurCfgVirtRtrVrGrpSharing_Object=MibTableColumn
vrrpCurCfgVirtRtrVrGrpSharing=_VrrpCurCfgVirtRtrVrGrpSharing_Object((1,3,6,1,4,1,1872,2,5,3,1,6,12,1,16),_VrrpCurCfgVirtRtrVrGrpSharing_Type())
vrrpCurCfgVirtRtrVrGrpSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrVrGrpSharing.setStatus(_A)
_VrrpNewCfgVirtRtrVrGrpTable_Object=MibTable
vrrpNewCfgVirtRtrVrGrpTable=_VrrpNewCfgVirtRtrVrGrpTable_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpTable.setStatus(_A)
_VrrpNewCfgVirtRtrVrGrpTableEntry_Object=MibTableRow
vrrpNewCfgVirtRtrVrGrpTableEntry=_VrrpNewCfgVirtRtrVrGrpTableEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1))
vrrpNewCfgVirtRtrVrGrpTableEntry.setIndexNames((0,_G,_AA))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpTableEntry.setStatus(_A)
_VrrpNewCfgVirtRtrVrGrpIndx_Type=Integer32
_VrrpNewCfgVirtRtrVrGrpIndx_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpIndx=_VrrpNewCfgVirtRtrVrGrpIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,1),_VrrpNewCfgVirtRtrVrGrpIndx_Type())
vrrpNewCfgVirtRtrVrGrpIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpIndx.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_VrrpNewCfgVirtRtrVrGrpName_Type.__name__=_I
_VrrpNewCfgVirtRtrVrGrpName_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpName=_VrrpNewCfgVirtRtrVrGrpName_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,2),_VrrpNewCfgVirtRtrVrGrpName_Type())
vrrpNewCfgVirtRtrVrGrpName.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpName.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_VrrpNewCfgVirtRtrVrGrpAdd_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpAdd_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpAdd=_VrrpNewCfgVirtRtrVrGrpAdd_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,3),_VrrpNewCfgVirtRtrVrGrpAdd_Type())
vrrpNewCfgVirtRtrVrGrpAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpAdd.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpRem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_VrrpNewCfgVirtRtrVrGrpRem_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpRem_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpRem=_VrrpNewCfgVirtRtrVrGrpRem_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,4),_VrrpNewCfgVirtRtrVrGrpRem_Type())
vrrpNewCfgVirtRtrVrGrpRem.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpRem.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrVrGrpState_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpState_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpState=_VrrpNewCfgVirtRtrVrGrpState_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,5),_VrrpNewCfgVirtRtrVrGrpState_Type())
vrrpNewCfgVirtRtrVrGrpState.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpState.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_VrrpNewCfgVirtRtrVrGrpDelete_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpDelete_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpDelete=_VrrpNewCfgVirtRtrVrGrpDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,6),_VrrpNewCfgVirtRtrVrGrpDelete_Type())
vrrpNewCfgVirtRtrVrGrpDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpDelete.setStatus(_A)
_VrrpNewCfgVirtRtrVrGrpBmap_Type=OctetString
_VrrpNewCfgVirtRtrVrGrpBmap_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpBmap=_VrrpNewCfgVirtRtrVrGrpBmap_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,7),_VrrpNewCfgVirtRtrVrGrpBmap_Type())
vrrpNewCfgVirtRtrVrGrpBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpBmap.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpNewCfgVirtRtrVrGrpPriority_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpPriority_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpPriority=_VrrpNewCfgVirtRtrVrGrpPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,8),_VrrpNewCfgVirtRtrVrGrpPriority_Type())
vrrpNewCfgVirtRtrVrGrpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpPriority.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrVrGrpTckIpIntf_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpTckIpIntf_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckIpIntf=_VrrpNewCfgVirtRtrVrGrpTckIpIntf_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,9),_VrrpNewCfgVirtRtrVrGrpTckIpIntf_Type())
vrrpNewCfgVirtRtrVrGrpTckIpIntf.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpTckIpIntf.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrVrGrpTckVlanPort_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpTckVlanPort_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckVlanPort=_VrrpNewCfgVirtRtrVrGrpTckVlanPort_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,10),_VrrpNewCfgVirtRtrVrGrpTckVlanPort_Type())
vrrpNewCfgVirtRtrVrGrpTckVlanPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpTckVlanPort.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrVrGrpTckL4Port_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpTckL4Port_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckL4Port=_VrrpNewCfgVirtRtrVrGrpTckL4Port_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,11),_VrrpNewCfgVirtRtrVrGrpTckL4Port_Type())
vrrpNewCfgVirtRtrVrGrpTckL4Port.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpTckL4Port.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrVrGrpTckRServer_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpTckRServer_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckRServer=_VrrpNewCfgVirtRtrVrGrpTckRServer_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,12),_VrrpNewCfgVirtRtrVrGrpTckRServer_Type())
vrrpNewCfgVirtRtrVrGrpTckRServer.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpTckRServer.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrVrGrpTckHsrp_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpTckHsrp_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckHsrp=_VrrpNewCfgVirtRtrVrGrpTckHsrp_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,13),_VrrpNewCfgVirtRtrVrGrpTckHsrp_Type())
vrrpNewCfgVirtRtrVrGrpTckHsrp.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpTckHsrp.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrVrGrpTckHsrv_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpTckHsrv_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckHsrv=_VrrpNewCfgVirtRtrVrGrpTckHsrv_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,14),_VrrpNewCfgVirtRtrVrGrpTckHsrv_Type())
vrrpNewCfgVirtRtrVrGrpTckHsrv.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpTckHsrv.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo=_VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,15),_VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Type())
vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpAdverInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpNewCfgVirtRtrVrGrpAdverInterval_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpAdverInterval_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpAdverInterval=_VrrpNewCfgVirtRtrVrGrpAdverInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,16),_VrrpNewCfgVirtRtrVrGrpAdverInterval_Type())
vrrpNewCfgVirtRtrVrGrpAdverInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpAdverInterval.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpPreemption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrVrGrpPreemption_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpPreemption_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpPreemption=_VrrpNewCfgVirtRtrVrGrpPreemption_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,17),_VrrpNewCfgVirtRtrVrGrpPreemption_Type())
vrrpNewCfgVirtRtrVrGrpPreemption.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpPreemption.setStatus(_A)
class _VrrpNewCfgVirtRtrVrGrpSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_VrrpNewCfgVirtRtrVrGrpSharing_Type.__name__=_C
_VrrpNewCfgVirtRtrVrGrpSharing_Object=MibTableColumn
vrrpNewCfgVirtRtrVrGrpSharing=_VrrpNewCfgVirtRtrVrGrpSharing_Object((1,3,6,1,4,1,1872,2,5,3,1,6,13,1,18),_VrrpNewCfgVirtRtrVrGrpSharing_Type())
vrrpNewCfgVirtRtrVrGrpSharing.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrVrGrpSharing.setStatus(_A)
_ArpCfg_ObjectIdentity=ObjectIdentity
arpCfg=_ArpCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,7))
class _ArpCurCfgReARPPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,120))
_ArpCurCfgReARPPeriod_Type.__name__=_C
_ArpCurCfgReARPPeriod_Object=MibScalar
arpCurCfgReARPPeriod=_ArpCurCfgReARPPeriod_Object((1,3,6,1,4,1,1872,2,5,3,1,7,1),_ArpCurCfgReARPPeriod_Type())
arpCurCfgReARPPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:arpCurCfgReARPPeriod.setStatus(_A)
class _ArpNewCfgReARPPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,120))
_ArpNewCfgReARPPeriod_Type.__name__=_C
_ArpNewCfgReARPPeriod_Object=MibScalar
arpNewCfgReARPPeriod=_ArpNewCfgReARPPeriod_Object((1,3,6,1,4,1,1872,2,5,3,1,7,2),_ArpNewCfgReARPPeriod_Type())
arpNewCfgReARPPeriod.setMaxAccess(_H)
if mibBuilder.loadTexts:arpNewCfgReARPPeriod.setStatus(_A)
_IpBootpCfg_ObjectIdentity=ObjectIdentity
ipBootpCfg=_IpBootpCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,8))
_IpCurCfgBootpAddr_Type=IpAddress
_IpCurCfgBootpAddr_Object=MibScalar
ipCurCfgBootpAddr=_IpCurCfgBootpAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,8,1),_IpCurCfgBootpAddr_Type())
ipCurCfgBootpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgBootpAddr.setStatus(_A)
_IpNewCfgBootpAddr_Type=IpAddress
_IpNewCfgBootpAddr_Object=MibScalar
ipNewCfgBootpAddr=_IpNewCfgBootpAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,8,2),_IpNewCfgBootpAddr_Type())
ipNewCfgBootpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:ipNewCfgBootpAddr.setStatus(_A)
_IpCurCfgBootpAddr2_Type=IpAddress
_IpCurCfgBootpAddr2_Object=MibScalar
ipCurCfgBootpAddr2=_IpCurCfgBootpAddr2_Object((1,3,6,1,4,1,1872,2,5,3,1,8,3),_IpCurCfgBootpAddr2_Type())
ipCurCfgBootpAddr2.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgBootpAddr2.setStatus(_A)
_IpNewCfgBootpAddr2_Type=IpAddress
_IpNewCfgBootpAddr2_Object=MibScalar
ipNewCfgBootpAddr2=_IpNewCfgBootpAddr2_Object((1,3,6,1,4,1,1872,2,5,3,1,8,4),_IpNewCfgBootpAddr2_Type())
ipNewCfgBootpAddr2.setMaxAccess(_H)
if mibBuilder.loadTexts:ipNewCfgBootpAddr2.setStatus(_A)
class _IpCurCfgBootpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpCurCfgBootpState_Type.__name__=_C
_IpCurCfgBootpState_Object=MibScalar
ipCurCfgBootpState=_IpCurCfgBootpState_Object((1,3,6,1,4,1,1872,2,5,3,1,8,5),_IpCurCfgBootpState_Type())
ipCurCfgBootpState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgBootpState.setStatus(_A)
class _IpNewCfgBootpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_IpNewCfgBootpState_Type.__name__=_C
_IpNewCfgBootpState_Object=MibScalar
ipNewCfgBootpState=_IpNewCfgBootpState_Object((1,3,6,1,4,1,1872,2,5,3,1,8,6),_IpNewCfgBootpState_Type())
ipNewCfgBootpState.setMaxAccess(_H)
if mibBuilder.loadTexts:ipNewCfgBootpState.setStatus(_A)
_DnsCfg_ObjectIdentity=ObjectIdentity
dnsCfg=_DnsCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,9))
_DnsCurCfgPrimaryIpAddr_Type=IpAddress
_DnsCurCfgPrimaryIpAddr_Object=MibScalar
dnsCurCfgPrimaryIpAddr=_DnsCurCfgPrimaryIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,9,1),_DnsCurCfgPrimaryIpAddr_Type())
dnsCurCfgPrimaryIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsCurCfgPrimaryIpAddr.setStatus(_A)
_DnsNewCfgPrimaryIpAddr_Type=IpAddress
_DnsNewCfgPrimaryIpAddr_Object=MibScalar
dnsNewCfgPrimaryIpAddr=_DnsNewCfgPrimaryIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,9,2),_DnsNewCfgPrimaryIpAddr_Type())
dnsNewCfgPrimaryIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:dnsNewCfgPrimaryIpAddr.setStatus(_A)
_DnsCurCfgSecondaryIpAddr_Type=IpAddress
_DnsCurCfgSecondaryIpAddr_Object=MibScalar
dnsCurCfgSecondaryIpAddr=_DnsCurCfgSecondaryIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,9,3),_DnsCurCfgSecondaryIpAddr_Type())
dnsCurCfgSecondaryIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsCurCfgSecondaryIpAddr.setStatus(_A)
_DnsNewCfgSecondaryIpAddr_Type=IpAddress
_DnsNewCfgSecondaryIpAddr_Object=MibScalar
dnsNewCfgSecondaryIpAddr=_DnsNewCfgSecondaryIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,9,4),_DnsNewCfgSecondaryIpAddr_Type())
dnsNewCfgSecondaryIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:dnsNewCfgSecondaryIpAddr.setStatus(_A)
class _DnsCurCfgDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,191))
_DnsCurCfgDomainName_Type.__name__=_I
_DnsCurCfgDomainName_Object=MibScalar
dnsCurCfgDomainName=_DnsCurCfgDomainName_Object((1,3,6,1,4,1,1872,2,5,3,1,9,5),_DnsCurCfgDomainName_Type())
dnsCurCfgDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsCurCfgDomainName.setStatus(_A)
class _DnsNewCfgDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,191))
_DnsNewCfgDomainName_Type.__name__=_I
_DnsNewCfgDomainName_Object=MibScalar
dnsNewCfgDomainName=_DnsNewCfgDomainName_Object((1,3,6,1,4,1,1872,2,5,3,1,9,6),_DnsNewCfgDomainName_Type())
dnsNewCfgDomainName.setMaxAccess(_H)
if mibBuilder.loadTexts:dnsNewCfgDomainName.setStatus(_A)
class _DnsCurCfgPrimaryIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DnsCurCfgPrimaryIpv6Addr_Type.__name__=_I
_DnsCurCfgPrimaryIpv6Addr_Object=MibScalar
dnsCurCfgPrimaryIpv6Addr=_DnsCurCfgPrimaryIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,9,7),_DnsCurCfgPrimaryIpv6Addr_Type())
dnsCurCfgPrimaryIpv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsCurCfgPrimaryIpv6Addr.setStatus(_A)
class _DnsNewCfgPrimaryIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DnsNewCfgPrimaryIpv6Addr_Type.__name__=_I
_DnsNewCfgPrimaryIpv6Addr_Object=MibScalar
dnsNewCfgPrimaryIpv6Addr=_DnsNewCfgPrimaryIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,9,8),_DnsNewCfgPrimaryIpv6Addr_Type())
dnsNewCfgPrimaryIpv6Addr.setMaxAccess(_H)
if mibBuilder.loadTexts:dnsNewCfgPrimaryIpv6Addr.setStatus(_A)
class _DnsCurCfgSecondaryIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DnsCurCfgSecondaryIpv6Addr_Type.__name__=_I
_DnsCurCfgSecondaryIpv6Addr_Object=MibScalar
dnsCurCfgSecondaryIpv6Addr=_DnsCurCfgSecondaryIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,9,9),_DnsCurCfgSecondaryIpv6Addr_Type())
dnsCurCfgSecondaryIpv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsCurCfgSecondaryIpv6Addr.setStatus(_A)
class _DnsNewCfgSecondaryIpv6Addr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DnsNewCfgSecondaryIpv6Addr_Type.__name__=_I
_DnsNewCfgSecondaryIpv6Addr_Object=MibScalar
dnsNewCfgSecondaryIpv6Addr=_DnsNewCfgSecondaryIpv6Addr_Object((1,3,6,1,4,1,1872,2,5,3,1,9,10),_DnsNewCfgSecondaryIpv6Addr_Type())
dnsNewCfgSecondaryIpv6Addr.setMaxAccess(_H)
if mibBuilder.loadTexts:dnsNewCfgSecondaryIpv6Addr.setStatus(_A)
_IpNwfCfg_ObjectIdentity=ObjectIdentity
ipNwfCfg=_IpNwfCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,10))
_IpNwfTableMax_Type=Integer32
_IpNwfTableMax_Object=MibScalar
ipNwfTableMax=_IpNwfTableMax_Object((1,3,6,1,4,1,1872,2,5,3,1,10,1),_IpNwfTableMax_Type())
ipNwfTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNwfTableMax.setStatus(_A)
_IpCurCfgNwfTable_Object=MibTable
ipCurCfgNwfTable=_IpCurCfgNwfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,10,2))
if mibBuilder.loadTexts:ipCurCfgNwfTable.setStatus(_A)
_IpCurCfgNwfEntry_Object=MibTableRow
ipCurCfgNwfEntry=_IpCurCfgNwfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,10,2,1))
ipCurCfgNwfEntry.setIndexNames((0,_G,_AB))
if mibBuilder.loadTexts:ipCurCfgNwfEntry.setStatus(_A)
_IpCurCfgNwfIndex_Type=Integer32
_IpCurCfgNwfIndex_Object=MibTableColumn
ipCurCfgNwfIndex=_IpCurCfgNwfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,10,2,1,1),_IpCurCfgNwfIndex_Type())
ipCurCfgNwfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgNwfIndex.setStatus(_A)
_IpCurCfgNwfAddr_Type=IpAddress
_IpCurCfgNwfAddr_Object=MibTableColumn
ipCurCfgNwfAddr=_IpCurCfgNwfAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,10,2,1,2),_IpCurCfgNwfAddr_Type())
ipCurCfgNwfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgNwfAddr.setStatus(_A)
_IpCurCfgNwfMask_Type=IpAddress
_IpCurCfgNwfMask_Object=MibTableColumn
ipCurCfgNwfMask=_IpCurCfgNwfMask_Object((1,3,6,1,4,1,1872,2,5,3,1,10,2,1,3),_IpCurCfgNwfMask_Type())
ipCurCfgNwfMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgNwfMask.setStatus(_A)
class _IpCurCfgNwfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpCurCfgNwfState_Type.__name__=_C
_IpCurCfgNwfState_Object=MibTableColumn
ipCurCfgNwfState=_IpCurCfgNwfState_Object((1,3,6,1,4,1,1872,2,5,3,1,10,2,1,4),_IpCurCfgNwfState_Type())
ipCurCfgNwfState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgNwfState.setStatus(_A)
_IpNewCfgNwfTable_Object=MibTable
ipNewCfgNwfTable=_IpNewCfgNwfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,10,3))
if mibBuilder.loadTexts:ipNewCfgNwfTable.setStatus(_A)
_IpNewCfgNwfEntry_Object=MibTableRow
ipNewCfgNwfEntry=_IpNewCfgNwfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,10,3,1))
ipNewCfgNwfEntry.setIndexNames((0,_G,_AC))
if mibBuilder.loadTexts:ipNewCfgNwfEntry.setStatus(_A)
_IpNewCfgNwfIndex_Type=Integer32
_IpNewCfgNwfIndex_Object=MibTableColumn
ipNewCfgNwfIndex=_IpNewCfgNwfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,10,3,1,1),_IpNewCfgNwfIndex_Type())
ipNewCfgNwfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgNwfIndex.setStatus(_A)
_IpNewCfgNwfAddr_Type=IpAddress
_IpNewCfgNwfAddr_Object=MibTableColumn
ipNewCfgNwfAddr=_IpNewCfgNwfAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,10,3,1,2),_IpNewCfgNwfAddr_Type())
ipNewCfgNwfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgNwfAddr.setStatus(_A)
_IpNewCfgNwfMask_Type=IpAddress
_IpNewCfgNwfMask_Object=MibTableColumn
ipNewCfgNwfMask=_IpNewCfgNwfMask_Object((1,3,6,1,4,1,1872,2,5,3,1,10,3,1,3),_IpNewCfgNwfMask_Type())
ipNewCfgNwfMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgNwfMask.setStatus(_A)
class _IpNewCfgNwfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpNewCfgNwfState_Type.__name__=_C
_IpNewCfgNwfState_Object=MibTableColumn
ipNewCfgNwfState=_IpNewCfgNwfState_Object((1,3,6,1,4,1,1872,2,5,3,1,10,3,1,4),_IpNewCfgNwfState_Type())
ipNewCfgNwfState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgNwfState.setStatus(_A)
class _IpNewCfgNwfDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_IpNewCfgNwfDelete_Type.__name__=_C
_IpNewCfgNwfDelete_Object=MibTableColumn
ipNewCfgNwfDelete=_IpNewCfgNwfDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,10,3,1,5),_IpNewCfgNwfDelete_Type())
ipNewCfgNwfDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgNwfDelete.setStatus(_A)
_IpRmapCfg_ObjectIdentity=ObjectIdentity
ipRmapCfg=_IpRmapCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,11))
_IpRmapTableMax_Type=Integer32
_IpRmapTableMax_Object=MibScalar
ipRmapTableMax=_IpRmapTableMax_Object((1,3,6,1,4,1,1872,2,5,3,1,11,1),_IpRmapTableMax_Type())
ipRmapTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRmapTableMax.setStatus(_A)
_IpCurCfgRmapTable_Object=MibTable
ipCurCfgRmapTable=_IpCurCfgRmapTable_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2))
if mibBuilder.loadTexts:ipCurCfgRmapTable.setStatus(_A)
_IpCurCfgRmapEntry_Object=MibTableRow
ipCurCfgRmapEntry=_IpCurCfgRmapEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2,1))
ipCurCfgRmapEntry.setIndexNames((0,_G,_AD))
if mibBuilder.loadTexts:ipCurCfgRmapEntry.setStatus(_A)
_IpCurCfgRmapIndex_Type=Integer32
_IpCurCfgRmapIndex_Object=MibTableColumn
ipCurCfgRmapIndex=_IpCurCfgRmapIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2,1,1),_IpCurCfgRmapIndex_Type())
ipCurCfgRmapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgRmapIndex.setStatus(_A)
class _IpCurCfgRmapLp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IpCurCfgRmapLp_Type.__name__=_M
_IpCurCfgRmapLp_Object=MibTableColumn
ipCurCfgRmapLp=_IpCurCfgRmapLp_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2,1,2),_IpCurCfgRmapLp_Type())
ipCurCfgRmapLp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgRmapLp.setStatus(_A)
class _IpCurCfgRmapMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IpCurCfgRmapMetric_Type.__name__=_M
_IpCurCfgRmapMetric_Object=MibTableColumn
ipCurCfgRmapMetric=_IpCurCfgRmapMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2,1,3),_IpCurCfgRmapMetric_Type())
ipCurCfgRmapMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgRmapMetric.setStatus(_A)
class _IpCurCfgRmapPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpCurCfgRmapPrec_Type.__name__=_C
_IpCurCfgRmapPrec_Object=MibTableColumn
ipCurCfgRmapPrec=_IpCurCfgRmapPrec_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2,1,4),_IpCurCfgRmapPrec_Type())
ipCurCfgRmapPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgRmapPrec.setStatus(_A)
class _IpCurCfgRmapWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpCurCfgRmapWeight_Type.__name__=_C
_IpCurCfgRmapWeight_Object=MibTableColumn
ipCurCfgRmapWeight=_IpCurCfgRmapWeight_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2,1,5),_IpCurCfgRmapWeight_Type())
ipCurCfgRmapWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgRmapWeight.setStatus(_A)
class _IpCurCfgRmapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpCurCfgRmapState_Type.__name__=_C
_IpCurCfgRmapState_Object=MibTableColumn
ipCurCfgRmapState=_IpCurCfgRmapState_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2,1,6),_IpCurCfgRmapState_Type())
ipCurCfgRmapState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgRmapState.setStatus(_A)
class _IpCurCfgRmapAp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_IpCurCfgRmapAp_Type.__name__=_I
_IpCurCfgRmapAp_Object=MibTableColumn
ipCurCfgRmapAp=_IpCurCfgRmapAp_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2,1,7),_IpCurCfgRmapAp_Type())
ipCurCfgRmapAp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgRmapAp.setStatus(_A)
class _IpCurCfgRmapMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_IpCurCfgRmapMetricType_Type.__name__=_C
_IpCurCfgRmapMetricType_Object=MibTableColumn
ipCurCfgRmapMetricType=_IpCurCfgRmapMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,11,2,1,8),_IpCurCfgRmapMetricType_Type())
ipCurCfgRmapMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgRmapMetricType.setStatus(_A)
_IpNewCfgRmapTable_Object=MibTable
ipNewCfgRmapTable=_IpNewCfgRmapTable_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3))
if mibBuilder.loadTexts:ipNewCfgRmapTable.setStatus(_A)
_IpNewCfgRmapEntry_Object=MibTableRow
ipNewCfgRmapEntry=_IpNewCfgRmapEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1))
ipNewCfgRmapEntry.setIndexNames((0,_G,_AE))
if mibBuilder.loadTexts:ipNewCfgRmapEntry.setStatus(_A)
_IpNewCfgRmapIndex_Type=Integer32
_IpNewCfgRmapIndex_Object=MibTableColumn
ipNewCfgRmapIndex=_IpNewCfgRmapIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1,1),_IpNewCfgRmapIndex_Type())
ipNewCfgRmapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgRmapIndex.setStatus(_A)
class _IpNewCfgRmapLp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IpNewCfgRmapLp_Type.__name__=_M
_IpNewCfgRmapLp_Object=MibTableColumn
ipNewCfgRmapLp=_IpNewCfgRmapLp_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1,2),_IpNewCfgRmapLp_Type())
ipNewCfgRmapLp.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgRmapLp.setStatus(_A)
class _IpNewCfgRmapMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IpNewCfgRmapMetric_Type.__name__=_M
_IpNewCfgRmapMetric_Object=MibTableColumn
ipNewCfgRmapMetric=_IpNewCfgRmapMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1,3),_IpNewCfgRmapMetric_Type())
ipNewCfgRmapMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgRmapMetric.setStatus(_A)
class _IpNewCfgRmapPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpNewCfgRmapPrec_Type.__name__=_C
_IpNewCfgRmapPrec_Object=MibTableColumn
ipNewCfgRmapPrec=_IpNewCfgRmapPrec_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1,4),_IpNewCfgRmapPrec_Type())
ipNewCfgRmapPrec.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgRmapPrec.setStatus(_A)
class _IpNewCfgRmapWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpNewCfgRmapWeight_Type.__name__=_C
_IpNewCfgRmapWeight_Object=MibTableColumn
ipNewCfgRmapWeight=_IpNewCfgRmapWeight_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1,5),_IpNewCfgRmapWeight_Type())
ipNewCfgRmapWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgRmapWeight.setStatus(_A)
class _IpNewCfgRmapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpNewCfgRmapState_Type.__name__=_C
_IpNewCfgRmapState_Object=MibTableColumn
ipNewCfgRmapState=_IpNewCfgRmapState_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1,6),_IpNewCfgRmapState_Type())
ipNewCfgRmapState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgRmapState.setStatus(_A)
class _IpNewCfgRmapAp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_IpNewCfgRmapAp_Type.__name__=_I
_IpNewCfgRmapAp_Object=MibTableColumn
ipNewCfgRmapAp=_IpNewCfgRmapAp_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1,7),_IpNewCfgRmapAp_Type())
ipNewCfgRmapAp.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgRmapAp.setStatus(_A)
class _IpNewCfgRmapMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_IpNewCfgRmapMetricType_Type.__name__=_C
_IpNewCfgRmapMetricType_Object=MibTableColumn
ipNewCfgRmapMetricType=_IpNewCfgRmapMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1,8),_IpNewCfgRmapMetricType_Type())
ipNewCfgRmapMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgRmapMetricType.setStatus(_A)
class _IpNewCfgRmapDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_IpNewCfgRmapDelete_Type.__name__=_C
_IpNewCfgRmapDelete_Object=MibTableColumn
ipNewCfgRmapDelete=_IpNewCfgRmapDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,11,3,1,9),_IpNewCfgRmapDelete_Type())
ipNewCfgRmapDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgRmapDelete.setStatus(_A)
_IpAlistTableMax_Type=Integer32
_IpAlistTableMax_Object=MibScalar
ipAlistTableMax=_IpAlistTableMax_Object((1,3,6,1,4,1,1872,2,5,3,1,11,4),_IpAlistTableMax_Type())
ipAlistTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipAlistTableMax.setStatus(_A)
_IpCurCfgAlistTable_Object=MibTable
ipCurCfgAlistTable=_IpCurCfgAlistTable_Object((1,3,6,1,4,1,1872,2,5,3,1,11,5))
if mibBuilder.loadTexts:ipCurCfgAlistTable.setStatus(_A)
_IpCurCfgAlistEntry_Object=MibTableRow
ipCurCfgAlistEntry=_IpCurCfgAlistEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,11,5,1))
ipCurCfgAlistEntry.setIndexNames((0,_G,_AF),(0,_G,_c))
if mibBuilder.loadTexts:ipCurCfgAlistEntry.setStatus(_A)
_IpCurCfgAlistRmapIndex_Type=Integer32
_IpCurCfgAlistRmapIndex_Object=MibTableColumn
ipCurCfgAlistRmapIndex=_IpCurCfgAlistRmapIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,5,1,1),_IpCurCfgAlistRmapIndex_Type())
ipCurCfgAlistRmapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAlistRmapIndex.setStatus(_A)
_IpCurCfgAlistIndex_Type=Integer32
_IpCurCfgAlistIndex_Object=MibTableColumn
ipCurCfgAlistIndex=_IpCurCfgAlistIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,5,1,2),_IpCurCfgAlistIndex_Type())
ipCurCfgAlistIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAlistIndex.setStatus(_A)
class _IpCurCfgAlistNwf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_IpCurCfgAlistNwf_Type.__name__=_C
_IpCurCfgAlistNwf_Object=MibTableColumn
ipCurCfgAlistNwf=_IpCurCfgAlistNwf_Object((1,3,6,1,4,1,1872,2,5,3,1,11,5,1,3),_IpCurCfgAlistNwf_Type())
ipCurCfgAlistNwf.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAlistNwf.setStatus(_A)
class _IpCurCfgAlistMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IpCurCfgAlistMetric_Type.__name__=_M
_IpCurCfgAlistMetric_Object=MibTableColumn
ipCurCfgAlistMetric=_IpCurCfgAlistMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,11,5,1,4),_IpCurCfgAlistMetric_Type())
ipCurCfgAlistMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAlistMetric.setStatus(_A)
class _IpCurCfgAlistAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_IpCurCfgAlistAction_Type.__name__=_C
_IpCurCfgAlistAction_Object=MibTableColumn
ipCurCfgAlistAction=_IpCurCfgAlistAction_Object((1,3,6,1,4,1,1872,2,5,3,1,11,5,1,5),_IpCurCfgAlistAction_Type())
ipCurCfgAlistAction.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAlistAction.setStatus(_A)
class _IpCurCfgAlistState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpCurCfgAlistState_Type.__name__=_C
_IpCurCfgAlistState_Object=MibTableColumn
ipCurCfgAlistState=_IpCurCfgAlistState_Object((1,3,6,1,4,1,1872,2,5,3,1,11,5,1,6),_IpCurCfgAlistState_Type())
ipCurCfgAlistState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAlistState.setStatus(_A)
_IpNewCfgAlistTable_Object=MibTable
ipNewCfgAlistTable=_IpNewCfgAlistTable_Object((1,3,6,1,4,1,1872,2,5,3,1,11,6))
if mibBuilder.loadTexts:ipNewCfgAlistTable.setStatus(_A)
_IpNewCfgAlistEntry_Object=MibTableRow
ipNewCfgAlistEntry=_IpNewCfgAlistEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,11,6,1))
ipNewCfgAlistEntry.setIndexNames((0,_G,_AG),(0,_G,_AH))
if mibBuilder.loadTexts:ipNewCfgAlistEntry.setStatus(_A)
_IpNewCfgAlistRmapIndex_Type=Integer32
_IpNewCfgAlistRmapIndex_Object=MibTableColumn
ipNewCfgAlistRmapIndex=_IpNewCfgAlistRmapIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,6,1,1),_IpNewCfgAlistRmapIndex_Type())
ipNewCfgAlistRmapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgAlistRmapIndex.setStatus(_A)
_IpNewCfgAlistIndex_Type=Integer32
_IpNewCfgAlistIndex_Object=MibTableColumn
ipNewCfgAlistIndex=_IpNewCfgAlistIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,6,1,2),_IpNewCfgAlistIndex_Type())
ipNewCfgAlistIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgAlistIndex.setStatus(_A)
class _IpNewCfgAlistNwf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_IpNewCfgAlistNwf_Type.__name__=_C
_IpNewCfgAlistNwf_Object=MibTableColumn
ipNewCfgAlistNwf=_IpNewCfgAlistNwf_Object((1,3,6,1,4,1,1872,2,5,3,1,11,6,1,3),_IpNewCfgAlistNwf_Type())
ipNewCfgAlistNwf.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgAlistNwf.setStatus(_A)
class _IpNewCfgAlistMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IpNewCfgAlistMetric_Type.__name__=_M
_IpNewCfgAlistMetric_Object=MibTableColumn
ipNewCfgAlistMetric=_IpNewCfgAlistMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,11,6,1,4),_IpNewCfgAlistMetric_Type())
ipNewCfgAlistMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgAlistMetric.setStatus(_A)
class _IpNewCfgAlistAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_IpNewCfgAlistAction_Type.__name__=_C
_IpNewCfgAlistAction_Object=MibTableColumn
ipNewCfgAlistAction=_IpNewCfgAlistAction_Object((1,3,6,1,4,1,1872,2,5,3,1,11,6,1,5),_IpNewCfgAlistAction_Type())
ipNewCfgAlistAction.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgAlistAction.setStatus(_A)
class _IpNewCfgAlistState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpNewCfgAlistState_Type.__name__=_C
_IpNewCfgAlistState_Object=MibTableColumn
ipNewCfgAlistState=_IpNewCfgAlistState_Object((1,3,6,1,4,1,1872,2,5,3,1,11,6,1,6),_IpNewCfgAlistState_Type())
ipNewCfgAlistState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgAlistState.setStatus(_A)
class _IpNewCfgAlistDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_IpNewCfgAlistDelete_Type.__name__=_C
_IpNewCfgAlistDelete_Object=MibTableColumn
ipNewCfgAlistDelete=_IpNewCfgAlistDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,11,6,1,7),_IpNewCfgAlistDelete_Type())
ipNewCfgAlistDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgAlistDelete.setStatus(_A)
_IpAspathTableMax_Type=Integer32
_IpAspathTableMax_Object=MibScalar
ipAspathTableMax=_IpAspathTableMax_Object((1,3,6,1,4,1,1872,2,5,3,1,11,7),_IpAspathTableMax_Type())
ipAspathTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipAspathTableMax.setStatus(_A)
_IpCurCfgAspathTable_Object=MibTable
ipCurCfgAspathTable=_IpCurCfgAspathTable_Object((1,3,6,1,4,1,1872,2,5,3,1,11,8))
if mibBuilder.loadTexts:ipCurCfgAspathTable.setStatus(_A)
_IpCurCfgAspathEntry_Object=MibTableRow
ipCurCfgAspathEntry=_IpCurCfgAspathEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,11,8,1))
ipCurCfgAspathEntry.setIndexNames((0,_G,_AI),(0,_G,_c))
if mibBuilder.loadTexts:ipCurCfgAspathEntry.setStatus(_A)
_IpCurCfgAspathRmapIndex_Type=Integer32
_IpCurCfgAspathRmapIndex_Object=MibTableColumn
ipCurCfgAspathRmapIndex=_IpCurCfgAspathRmapIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,8,1,1),_IpCurCfgAspathRmapIndex_Type())
ipCurCfgAspathRmapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAspathRmapIndex.setStatus(_A)
_IpCurCfgAspathIndex_Type=Integer32
_IpCurCfgAspathIndex_Object=MibTableColumn
ipCurCfgAspathIndex=_IpCurCfgAspathIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,8,1,2),_IpCurCfgAspathIndex_Type())
ipCurCfgAspathIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAspathIndex.setStatus(_A)
class _IpCurCfgAspathAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpCurCfgAspathAS_Type.__name__=_C
_IpCurCfgAspathAS_Object=MibTableColumn
ipCurCfgAspathAS=_IpCurCfgAspathAS_Object((1,3,6,1,4,1,1872,2,5,3,1,11,8,1,3),_IpCurCfgAspathAS_Type())
ipCurCfgAspathAS.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAspathAS.setStatus(_A)
class _IpCurCfgAspathAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_IpCurCfgAspathAction_Type.__name__=_C
_IpCurCfgAspathAction_Object=MibTableColumn
ipCurCfgAspathAction=_IpCurCfgAspathAction_Object((1,3,6,1,4,1,1872,2,5,3,1,11,8,1,4),_IpCurCfgAspathAction_Type())
ipCurCfgAspathAction.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAspathAction.setStatus(_A)
class _IpCurCfgAspathState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpCurCfgAspathState_Type.__name__=_C
_IpCurCfgAspathState_Object=MibTableColumn
ipCurCfgAspathState=_IpCurCfgAspathState_Object((1,3,6,1,4,1,1872,2,5,3,1,11,8,1,5),_IpCurCfgAspathState_Type())
ipCurCfgAspathState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgAspathState.setStatus(_A)
_IpNewCfgAspathTable_Object=MibTable
ipNewCfgAspathTable=_IpNewCfgAspathTable_Object((1,3,6,1,4,1,1872,2,5,3,1,11,9))
if mibBuilder.loadTexts:ipNewCfgAspathTable.setStatus(_A)
_IpNewCfgAspathEntry_Object=MibTableRow
ipNewCfgAspathEntry=_IpNewCfgAspathEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,11,9,1))
ipNewCfgAspathEntry.setIndexNames((0,_G,_AJ),(0,_G,_AK))
if mibBuilder.loadTexts:ipNewCfgAspathEntry.setStatus(_A)
_IpNewCfgAspathRmapIndex_Type=Integer32
_IpNewCfgAspathRmapIndex_Object=MibTableColumn
ipNewCfgAspathRmapIndex=_IpNewCfgAspathRmapIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,9,1,1),_IpNewCfgAspathRmapIndex_Type())
ipNewCfgAspathRmapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgAspathRmapIndex.setStatus(_A)
_IpNewCfgAspathIndex_Type=Integer32
_IpNewCfgAspathIndex_Object=MibTableColumn
ipNewCfgAspathIndex=_IpNewCfgAspathIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,11,9,1,2),_IpNewCfgAspathIndex_Type())
ipNewCfgAspathIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgAspathIndex.setStatus(_A)
class _IpNewCfgAspathAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpNewCfgAspathAS_Type.__name__=_C
_IpNewCfgAspathAS_Object=MibTableColumn
ipNewCfgAspathAS=_IpNewCfgAspathAS_Object((1,3,6,1,4,1,1872,2,5,3,1,11,9,1,3),_IpNewCfgAspathAS_Type())
ipNewCfgAspathAS.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgAspathAS.setStatus(_A)
class _IpNewCfgAspathAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_IpNewCfgAspathAction_Type.__name__=_C
_IpNewCfgAspathAction_Object=MibTableColumn
ipNewCfgAspathAction=_IpNewCfgAspathAction_Object((1,3,6,1,4,1,1872,2,5,3,1,11,9,1,4),_IpNewCfgAspathAction_Type())
ipNewCfgAspathAction.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgAspathAction.setStatus(_A)
class _IpNewCfgAspathState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_IpNewCfgAspathState_Type.__name__=_C
_IpNewCfgAspathState_Object=MibTableColumn
ipNewCfgAspathState=_IpNewCfgAspathState_Object((1,3,6,1,4,1,1872,2,5,3,1,11,9,1,5),_IpNewCfgAspathState_Type())
ipNewCfgAspathState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgAspathState.setStatus(_A)
class _IpNewCfgAspathDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_IpNewCfgAspathDelete_Type.__name__=_C
_IpNewCfgAspathDelete_Object=MibTableColumn
ipNewCfgAspathDelete=_IpNewCfgAspathDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,11,9,1,6),_IpNewCfgAspathDelete_Type())
ipNewCfgAspathDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgAspathDelete.setStatus(_A)
_BgpCfg_ObjectIdentity=ObjectIdentity
bgpCfg=_BgpCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,12))
_BgpGeneral_ObjectIdentity=ObjectIdentity
bgpGeneral=_BgpGeneral_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,12,1))
class _BgpCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_BgpCurCfgState_Type.__name__=_C
_BgpCurCfgState_Object=MibScalar
bgpCurCfgState=_BgpCurCfgState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,1,1),_BgpCurCfgState_Type())
bgpCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgState.setStatus(_A)
class _BgpNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_BgpNewCfgState_Type.__name__=_C
_BgpNewCfgState_Object=MibScalar
bgpNewCfgState=_BgpNewCfgState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,1,2),_BgpNewCfgState_Type())
bgpNewCfgState.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpNewCfgState.setStatus(_A)
class _BgpCurCfgLocalPref_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_BgpCurCfgLocalPref_Type.__name__=_M
_BgpCurCfgLocalPref_Object=MibScalar
bgpCurCfgLocalPref=_BgpCurCfgLocalPref_Object((1,3,6,1,4,1,1872,2,5,3,1,12,1,3),_BgpCurCfgLocalPref_Type())
bgpCurCfgLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgLocalPref.setStatus(_A)
class _BgpNewCfgLocalPref_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_BgpNewCfgLocalPref_Type.__name__=_M
_BgpNewCfgLocalPref_Object=MibScalar
bgpNewCfgLocalPref=_BgpNewCfgLocalPref_Object((1,3,6,1,4,1,1872,2,5,3,1,12,1,4),_BgpNewCfgLocalPref_Type())
bgpNewCfgLocalPref.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpNewCfgLocalPref.setStatus(_A)
class _BgpCurCfgMaxASPath_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_BgpCurCfgMaxASPath_Type.__name__=_M
_BgpCurCfgMaxASPath_Object=MibScalar
bgpCurCfgMaxASPath=_BgpCurCfgMaxASPath_Object((1,3,6,1,4,1,1872,2,5,3,1,12,1,5),_BgpCurCfgMaxASPath_Type())
bgpCurCfgMaxASPath.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgMaxASPath.setStatus(_A)
class _BgpNewCfgMaxASPath_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_BgpNewCfgMaxASPath_Type.__name__=_M
_BgpNewCfgMaxASPath_Object=MibScalar
bgpNewCfgMaxASPath=_BgpNewCfgMaxASPath_Object((1,3,6,1,4,1,1872,2,5,3,1,12,1,6),_BgpNewCfgMaxASPath_Type())
bgpNewCfgMaxASPath.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpNewCfgMaxASPath.setStatus(_A)
class _BgpCurCfgASNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpCurCfgASNumber_Type.__name__=_M
_BgpCurCfgASNumber_Object=MibScalar
bgpCurCfgASNumber=_BgpCurCfgASNumber_Object((1,3,6,1,4,1,1872,2,5,3,1,12,1,7),_BgpCurCfgASNumber_Type())
bgpCurCfgASNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgASNumber.setStatus(_A)
class _BgpNewCfgASNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpNewCfgASNumber_Type.__name__=_M
_BgpNewCfgASNumber_Object=MibScalar
bgpNewCfgASNumber=_BgpNewCfgASNumber_Object((1,3,6,1,4,1,1872,2,5,3,1,12,1,8),_BgpNewCfgASNumber_Type())
bgpNewCfgASNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpNewCfgASNumber.setStatus(_A)
_BgpPeerTableMax_Type=Integer32
_BgpPeerTableMax_Object=MibScalar
bgpPeerTableMax=_BgpPeerTableMax_Object((1,3,6,1,4,1,1872,2,5,3,1,12,2),_BgpPeerTableMax_Type())
bgpPeerTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerTableMax.setStatus(_A)
_BgpCurCfgPeerTable_Object=MibTable
bgpCurCfgPeerTable=_BgpCurCfgPeerTable_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3))
if mibBuilder.loadTexts:bgpCurCfgPeerTable.setStatus(_A)
_BgpCurCfgPeerEntry_Object=MibTableRow
bgpCurCfgPeerEntry=_BgpCurCfgPeerEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1))
bgpCurCfgPeerEntry.setIndexNames((0,_G,_AL))
if mibBuilder.loadTexts:bgpCurCfgPeerEntry.setStatus(_A)
_BgpCurCfgPeerIndex_Type=Integer32
_BgpCurCfgPeerIndex_Object=MibTableColumn
bgpCurCfgPeerIndex=_BgpCurCfgPeerIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,1),_BgpCurCfgPeerIndex_Type())
bgpCurCfgPeerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerIndex.setStatus(_A)
_BgpCurCfgPeerRemoteAddr_Type=IpAddress
_BgpCurCfgPeerRemoteAddr_Object=MibTableColumn
bgpCurCfgPeerRemoteAddr=_BgpCurCfgPeerRemoteAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,2),_BgpCurCfgPeerRemoteAddr_Type())
bgpCurCfgPeerRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerRemoteAddr.setStatus(_A)
class _BgpCurCfgPeerRemoteAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpCurCfgPeerRemoteAs_Type.__name__=_C
_BgpCurCfgPeerRemoteAs_Object=MibTableColumn
bgpCurCfgPeerRemoteAs=_BgpCurCfgPeerRemoteAs_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,3),_BgpCurCfgPeerRemoteAs_Type())
bgpCurCfgPeerRemoteAs.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerRemoteAs.setStatus(_A)
class _BgpCurCfgPeerTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BgpCurCfgPeerTtl_Type.__name__=_C
_BgpCurCfgPeerTtl_Object=MibTableColumn
bgpCurCfgPeerTtl=_BgpCurCfgPeerTtl_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,4),_BgpCurCfgPeerTtl_Type())
bgpCurCfgPeerTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerTtl.setStatus(_A)
class _BgpCurCfgPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpCurCfgPeerState_Type.__name__=_C
_BgpCurCfgPeerState_Object=MibTableColumn
bgpCurCfgPeerState=_BgpCurCfgPeerState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,5),_BgpCurCfgPeerState_Type())
bgpCurCfgPeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerState.setStatus(_A)
class _BgpCurCfgPeerMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_BgpCurCfgPeerMetric_Type.__name__=_M
_BgpCurCfgPeerMetric_Object=MibTableColumn
bgpCurCfgPeerMetric=_BgpCurCfgPeerMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,10),_BgpCurCfgPeerMetric_Type())
bgpCurCfgPeerMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerMetric.setStatus(_A)
class _BgpCurCfgPeerDefaultAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('import',2),(_AM,3),(_AN,4)))
_BgpCurCfgPeerDefaultAction_Type.__name__=_C
_BgpCurCfgPeerDefaultAction_Object=MibTableColumn
bgpCurCfgPeerDefaultAction=_BgpCurCfgPeerDefaultAction_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,11),_BgpCurCfgPeerDefaultAction_Type())
bgpCurCfgPeerDefaultAction.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerDefaultAction.setStatus(_A)
class _BgpCurCfgPeerOspfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpCurCfgPeerOspfState_Type.__name__=_C
_BgpCurCfgPeerOspfState_Object=MibTableColumn
bgpCurCfgPeerOspfState=_BgpCurCfgPeerOspfState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,12),_BgpCurCfgPeerOspfState_Type())
bgpCurCfgPeerOspfState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerOspfState.setStatus(_A)
class _BgpCurCfgPeerFixedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpCurCfgPeerFixedState_Type.__name__=_C
_BgpCurCfgPeerFixedState_Object=MibTableColumn
bgpCurCfgPeerFixedState=_BgpCurCfgPeerFixedState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,13),_BgpCurCfgPeerFixedState_Type())
bgpCurCfgPeerFixedState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerFixedState.setStatus(_A)
class _BgpCurCfgPeerStaticState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpCurCfgPeerStaticState_Type.__name__=_C
_BgpCurCfgPeerStaticState_Object=MibTableColumn
bgpCurCfgPeerStaticState=_BgpCurCfgPeerStaticState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,14),_BgpCurCfgPeerStaticState_Type())
bgpCurCfgPeerStaticState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerStaticState.setStatus(_A)
class _BgpCurCfgPeerVipState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpCurCfgPeerVipState_Type.__name__=_C
_BgpCurCfgPeerVipState_Object=MibTableColumn
bgpCurCfgPeerVipState=_BgpCurCfgPeerVipState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,15),_BgpCurCfgPeerVipState_Type())
bgpCurCfgPeerVipState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerVipState.setStatus(_A)
_BgpCurCfgPeerInRmapList_Type=OctetString
_BgpCurCfgPeerInRmapList_Object=MibTableColumn
bgpCurCfgPeerInRmapList=_BgpCurCfgPeerInRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,16),_BgpCurCfgPeerInRmapList_Type())
bgpCurCfgPeerInRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerInRmapList.setStatus(_A)
_BgpCurCfgPeerOutRmapList_Type=OctetString
_BgpCurCfgPeerOutRmapList_Object=MibTableColumn
bgpCurCfgPeerOutRmapList=_BgpCurCfgPeerOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,17),_BgpCurCfgPeerOutRmapList_Type())
bgpCurCfgPeerOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerOutRmapList.setStatus(_A)
class _BgpCurCfgPeerHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BgpCurCfgPeerHoldTime_Type.__name__=_C
_BgpCurCfgPeerHoldTime_Object=MibTableColumn
bgpCurCfgPeerHoldTime=_BgpCurCfgPeerHoldTime_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,18),_BgpCurCfgPeerHoldTime_Type())
bgpCurCfgPeerHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerHoldTime.setStatus(_A)
class _BgpCurCfgPeerKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,21845))
_BgpCurCfgPeerKeepAlive_Type.__name__=_C
_BgpCurCfgPeerKeepAlive_Object=MibTableColumn
bgpCurCfgPeerKeepAlive=_BgpCurCfgPeerKeepAlive_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,19),_BgpCurCfgPeerKeepAlive_Type())
bgpCurCfgPeerKeepAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerKeepAlive.setStatus(_A)
class _BgpCurCfgPeerMinTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BgpCurCfgPeerMinTime_Type.__name__=_C
_BgpCurCfgPeerMinTime_Object=MibTableColumn
bgpCurCfgPeerMinTime=_BgpCurCfgPeerMinTime_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,20),_BgpCurCfgPeerMinTime_Type())
bgpCurCfgPeerMinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerMinTime.setStatus(_A)
class _BgpCurCfgPeerConRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BgpCurCfgPeerConRetry_Type.__name__=_C
_BgpCurCfgPeerConRetry_Object=MibTableColumn
bgpCurCfgPeerConRetry=_BgpCurCfgPeerConRetry_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,21),_BgpCurCfgPeerConRetry_Type())
bgpCurCfgPeerConRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerConRetry.setStatus(_A)
class _BgpCurCfgPeerMinAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,65535))
_BgpCurCfgPeerMinAS_Type.__name__=_C
_BgpCurCfgPeerMinAS_Object=MibTableColumn
bgpCurCfgPeerMinAS=_BgpCurCfgPeerMinAS_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,22),_BgpCurCfgPeerMinAS_Type())
bgpCurCfgPeerMinAS.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerMinAS.setStatus(_A)
class _BgpCurCfgPeerRipState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpCurCfgPeerRipState_Type.__name__=_C
_BgpCurCfgPeerRipState_Object=MibTableColumn
bgpCurCfgPeerRipState=_BgpCurCfgPeerRipState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,3,1,23),_BgpCurCfgPeerRipState_Type())
bgpCurCfgPeerRipState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgPeerRipState.setStatus(_A)
_BgpNewCfgPeerTable_Object=MibTable
bgpNewCfgPeerTable=_BgpNewCfgPeerTable_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4))
if mibBuilder.loadTexts:bgpNewCfgPeerTable.setStatus(_A)
_BgpNewCfgPeerEntry_Object=MibTableRow
bgpNewCfgPeerEntry=_BgpNewCfgPeerEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1))
bgpNewCfgPeerEntry.setIndexNames((0,_G,_AO))
if mibBuilder.loadTexts:bgpNewCfgPeerEntry.setStatus(_A)
_BgpNewCfgPeerIndex_Type=Integer32
_BgpNewCfgPeerIndex_Object=MibTableColumn
bgpNewCfgPeerIndex=_BgpNewCfgPeerIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,1),_BgpNewCfgPeerIndex_Type())
bgpNewCfgPeerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpNewCfgPeerIndex.setStatus(_A)
_BgpNewCfgPeerRemoteAddr_Type=IpAddress
_BgpNewCfgPeerRemoteAddr_Object=MibTableColumn
bgpNewCfgPeerRemoteAddr=_BgpNewCfgPeerRemoteAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,2),_BgpNewCfgPeerRemoteAddr_Type())
bgpNewCfgPeerRemoteAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerRemoteAddr.setStatus(_A)
class _BgpNewCfgPeerRemoteAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpNewCfgPeerRemoteAs_Type.__name__=_C
_BgpNewCfgPeerRemoteAs_Object=MibTableColumn
bgpNewCfgPeerRemoteAs=_BgpNewCfgPeerRemoteAs_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,3),_BgpNewCfgPeerRemoteAs_Type())
bgpNewCfgPeerRemoteAs.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerRemoteAs.setStatus(_A)
class _BgpNewCfgPeerTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BgpNewCfgPeerTtl_Type.__name__=_C
_BgpNewCfgPeerTtl_Object=MibTableColumn
bgpNewCfgPeerTtl=_BgpNewCfgPeerTtl_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,4),_BgpNewCfgPeerTtl_Type())
bgpNewCfgPeerTtl.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerTtl.setStatus(_A)
class _BgpNewCfgPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpNewCfgPeerState_Type.__name__=_C
_BgpNewCfgPeerState_Object=MibTableColumn
bgpNewCfgPeerState=_BgpNewCfgPeerState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,5),_BgpNewCfgPeerState_Type())
bgpNewCfgPeerState.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerState.setStatus(_A)
class _BgpNewCfgPeerDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_BgpNewCfgPeerDelete_Type.__name__=_C
_BgpNewCfgPeerDelete_Object=MibTableColumn
bgpNewCfgPeerDelete=_BgpNewCfgPeerDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,6),_BgpNewCfgPeerDelete_Type())
bgpNewCfgPeerDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerDelete.setStatus(_A)
class _BgpNewCfgPeerMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_BgpNewCfgPeerMetric_Type.__name__=_M
_BgpNewCfgPeerMetric_Object=MibTableColumn
bgpNewCfgPeerMetric=_BgpNewCfgPeerMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,10),_BgpNewCfgPeerMetric_Type())
bgpNewCfgPeerMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerMetric.setStatus(_A)
class _BgpNewCfgPeerDefaultAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('import',2),(_AM,3),(_AN,4)))
_BgpNewCfgPeerDefaultAction_Type.__name__=_C
_BgpNewCfgPeerDefaultAction_Object=MibTableColumn
bgpNewCfgPeerDefaultAction=_BgpNewCfgPeerDefaultAction_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,11),_BgpNewCfgPeerDefaultAction_Type())
bgpNewCfgPeerDefaultAction.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerDefaultAction.setStatus(_A)
class _BgpNewCfgPeerOspfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpNewCfgPeerOspfState_Type.__name__=_C
_BgpNewCfgPeerOspfState_Object=MibTableColumn
bgpNewCfgPeerOspfState=_BgpNewCfgPeerOspfState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,12),_BgpNewCfgPeerOspfState_Type())
bgpNewCfgPeerOspfState.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerOspfState.setStatus(_A)
class _BgpNewCfgPeerFixedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpNewCfgPeerFixedState_Type.__name__=_C
_BgpNewCfgPeerFixedState_Object=MibTableColumn
bgpNewCfgPeerFixedState=_BgpNewCfgPeerFixedState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,13),_BgpNewCfgPeerFixedState_Type())
bgpNewCfgPeerFixedState.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerFixedState.setStatus(_A)
class _BgpNewCfgPeerStaticState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpNewCfgPeerStaticState_Type.__name__=_C
_BgpNewCfgPeerStaticState_Object=MibTableColumn
bgpNewCfgPeerStaticState=_BgpNewCfgPeerStaticState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,14),_BgpNewCfgPeerStaticState_Type())
bgpNewCfgPeerStaticState.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerStaticState.setStatus(_A)
class _BgpNewCfgPeerVipState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpNewCfgPeerVipState_Type.__name__=_C
_BgpNewCfgPeerVipState_Object=MibTableColumn
bgpNewCfgPeerVipState=_BgpNewCfgPeerVipState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,15),_BgpNewCfgPeerVipState_Type())
bgpNewCfgPeerVipState.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerVipState.setStatus(_A)
_BgpNewCfgPeerInRmapList_Type=OctetString
_BgpNewCfgPeerInRmapList_Object=MibTableColumn
bgpNewCfgPeerInRmapList=_BgpNewCfgPeerInRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,16),_BgpNewCfgPeerInRmapList_Type())
bgpNewCfgPeerInRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpNewCfgPeerInRmapList.setStatus(_A)
_BgpNewCfgPeerOutRmapList_Type=OctetString
_BgpNewCfgPeerOutRmapList_Object=MibTableColumn
bgpNewCfgPeerOutRmapList=_BgpNewCfgPeerOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,17),_BgpNewCfgPeerOutRmapList_Type())
bgpNewCfgPeerOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpNewCfgPeerOutRmapList.setStatus(_A)
_BgpNewCfgPeerAddInRmap_Type=Integer32
_BgpNewCfgPeerAddInRmap_Object=MibTableColumn
bgpNewCfgPeerAddInRmap=_BgpNewCfgPeerAddInRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,18),_BgpNewCfgPeerAddInRmap_Type())
bgpNewCfgPeerAddInRmap.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerAddInRmap.setStatus(_A)
_BgpNewCfgPeerAddOutRmap_Type=Integer32
_BgpNewCfgPeerAddOutRmap_Object=MibTableColumn
bgpNewCfgPeerAddOutRmap=_BgpNewCfgPeerAddOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,19),_BgpNewCfgPeerAddOutRmap_Type())
bgpNewCfgPeerAddOutRmap.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerAddOutRmap.setStatus(_A)
_BgpNewCfgPeerRemoveInRmap_Type=Integer32
_BgpNewCfgPeerRemoveInRmap_Object=MibTableColumn
bgpNewCfgPeerRemoveInRmap=_BgpNewCfgPeerRemoveInRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,20),_BgpNewCfgPeerRemoveInRmap_Type())
bgpNewCfgPeerRemoveInRmap.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerRemoveInRmap.setStatus(_A)
_BgpNewCfgPeerRemoveOutRmap_Type=Integer32
_BgpNewCfgPeerRemoveOutRmap_Object=MibTableColumn
bgpNewCfgPeerRemoveOutRmap=_BgpNewCfgPeerRemoveOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,21),_BgpNewCfgPeerRemoveOutRmap_Type())
bgpNewCfgPeerRemoveOutRmap.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerRemoveOutRmap.setStatus(_A)
class _BgpNewCfgPeerHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpNewCfgPeerHoldTime_Type.__name__=_C
_BgpNewCfgPeerHoldTime_Object=MibTableColumn
bgpNewCfgPeerHoldTime=_BgpNewCfgPeerHoldTime_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,22),_BgpNewCfgPeerHoldTime_Type())
bgpNewCfgPeerHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerHoldTime.setStatus(_A)
class _BgpNewCfgPeerKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,21845))
_BgpNewCfgPeerKeepAlive_Type.__name__=_C
_BgpNewCfgPeerKeepAlive_Object=MibTableColumn
bgpNewCfgPeerKeepAlive=_BgpNewCfgPeerKeepAlive_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,23),_BgpNewCfgPeerKeepAlive_Type())
bgpNewCfgPeerKeepAlive.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerKeepAlive.setStatus(_A)
class _BgpNewCfgPeerMinTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BgpNewCfgPeerMinTime_Type.__name__=_C
_BgpNewCfgPeerMinTime_Object=MibTableColumn
bgpNewCfgPeerMinTime=_BgpNewCfgPeerMinTime_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,24),_BgpNewCfgPeerMinTime_Type())
bgpNewCfgPeerMinTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerMinTime.setStatus(_A)
class _BgpNewCfgPeerConRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BgpNewCfgPeerConRetry_Type.__name__=_C
_BgpNewCfgPeerConRetry_Object=MibTableColumn
bgpNewCfgPeerConRetry=_BgpNewCfgPeerConRetry_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,25),_BgpNewCfgPeerConRetry_Type())
bgpNewCfgPeerConRetry.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerConRetry.setStatus(_A)
class _BgpNewCfgPeerMinAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,65535))
_BgpNewCfgPeerMinAS_Type.__name__=_C
_BgpNewCfgPeerMinAS_Object=MibTableColumn
bgpNewCfgPeerMinAS=_BgpNewCfgPeerMinAS_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,26),_BgpNewCfgPeerMinAS_Type())
bgpNewCfgPeerMinAS.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerMinAS.setStatus(_A)
class _BgpNewCfgPeerRipState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpNewCfgPeerRipState_Type.__name__=_C
_BgpNewCfgPeerRipState_Object=MibTableColumn
bgpNewCfgPeerRipState=_BgpNewCfgPeerRipState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,4,1,27),_BgpNewCfgPeerRipState_Type())
bgpNewCfgPeerRipState.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgPeerRipState.setStatus(_A)
_BgpAggrTableMax_Type=Integer32
_BgpAggrTableMax_Object=MibScalar
bgpAggrTableMax=_BgpAggrTableMax_Object((1,3,6,1,4,1,1872,2,5,3,1,12,5),_BgpAggrTableMax_Type())
bgpAggrTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpAggrTableMax.setStatus(_A)
_BgpCurCfgAggrTable_Object=MibTable
bgpCurCfgAggrTable=_BgpCurCfgAggrTable_Object((1,3,6,1,4,1,1872,2,5,3,1,12,6))
if mibBuilder.loadTexts:bgpCurCfgAggrTable.setStatus(_A)
_BgpCurCfgAggrEntry_Object=MibTableRow
bgpCurCfgAggrEntry=_BgpCurCfgAggrEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,12,6,1))
bgpCurCfgAggrEntry.setIndexNames((0,_G,_AP))
if mibBuilder.loadTexts:bgpCurCfgAggrEntry.setStatus(_A)
_BgpCurCfgAggrIndex_Type=Integer32
_BgpCurCfgAggrIndex_Object=MibTableColumn
bgpCurCfgAggrIndex=_BgpCurCfgAggrIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,12,6,1,1),_BgpCurCfgAggrIndex_Type())
bgpCurCfgAggrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgAggrIndex.setStatus(_A)
_BgpCurCfgAggrAddr_Type=IpAddress
_BgpCurCfgAggrAddr_Object=MibTableColumn
bgpCurCfgAggrAddr=_BgpCurCfgAggrAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,12,6,1,2),_BgpCurCfgAggrAddr_Type())
bgpCurCfgAggrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgAggrAddr.setStatus(_A)
_BgpCurCfgAggrMask_Type=IpAddress
_BgpCurCfgAggrMask_Object=MibTableColumn
bgpCurCfgAggrMask=_BgpCurCfgAggrMask_Object((1,3,6,1,4,1,1872,2,5,3,1,12,6,1,3),_BgpCurCfgAggrMask_Type())
bgpCurCfgAggrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgAggrMask.setStatus(_A)
class _BgpCurCfgAggrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpCurCfgAggrState_Type.__name__=_C
_BgpCurCfgAggrState_Object=MibTableColumn
bgpCurCfgAggrState=_BgpCurCfgAggrState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,6,1,4),_BgpCurCfgAggrState_Type())
bgpCurCfgAggrState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpCurCfgAggrState.setStatus(_A)
_BgpNewCfgAggrTable_Object=MibTable
bgpNewCfgAggrTable=_BgpNewCfgAggrTable_Object((1,3,6,1,4,1,1872,2,5,3,1,12,7))
if mibBuilder.loadTexts:bgpNewCfgAggrTable.setStatus(_A)
_BgpNewCfgAggrEntry_Object=MibTableRow
bgpNewCfgAggrEntry=_BgpNewCfgAggrEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,12,7,1))
bgpNewCfgAggrEntry.setIndexNames((0,_G,_AQ))
if mibBuilder.loadTexts:bgpNewCfgAggrEntry.setStatus(_A)
_BgpNewCfgAggrIndex_Type=Integer32
_BgpNewCfgAggrIndex_Object=MibTableColumn
bgpNewCfgAggrIndex=_BgpNewCfgAggrIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,12,7,1,1),_BgpNewCfgAggrIndex_Type())
bgpNewCfgAggrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpNewCfgAggrIndex.setStatus(_A)
_BgpNewCfgAggrAddr_Type=IpAddress
_BgpNewCfgAggrAddr_Object=MibTableColumn
bgpNewCfgAggrAddr=_BgpNewCfgAggrAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,12,7,1,2),_BgpNewCfgAggrAddr_Type())
bgpNewCfgAggrAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgAggrAddr.setStatus(_A)
_BgpNewCfgAggrMask_Type=IpAddress
_BgpNewCfgAggrMask_Object=MibTableColumn
bgpNewCfgAggrMask=_BgpNewCfgAggrMask_Object((1,3,6,1,4,1,1872,2,5,3,1,12,7,1,3),_BgpNewCfgAggrMask_Type())
bgpNewCfgAggrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgAggrMask.setStatus(_A)
class _BgpNewCfgAggrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_BgpNewCfgAggrState_Type.__name__=_C
_BgpNewCfgAggrState_Object=MibTableColumn
bgpNewCfgAggrState=_BgpNewCfgAggrState_Object((1,3,6,1,4,1,1872,2,5,3,1,12,7,1,4),_BgpNewCfgAggrState_Type())
bgpNewCfgAggrState.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgAggrState.setStatus(_A)
class _BgpNewCfgAggrDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_BgpNewCfgAggrDelete_Type.__name__=_C
_BgpNewCfgAggrDelete_Object=MibTableColumn
bgpNewCfgAggrDelete=_BgpNewCfgAggrDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,12,7,1,5),_BgpNewCfgAggrDelete_Type())
bgpNewCfgAggrDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNewCfgAggrDelete.setStatus(_A)
_OspfCfg_ObjectIdentity=ObjectIdentity
ospfCfg=_OspfCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,13))
_OspfGeneral_ObjectIdentity=ObjectIdentity
ospfGeneral=_OspfGeneral_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,13,1))
class _OspfCurCfgDefaultRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfCurCfgDefaultRouteMetric_Type.__name__=_C
_OspfCurCfgDefaultRouteMetric_Object=MibScalar
ospfCurCfgDefaultRouteMetric=_OspfCurCfgDefaultRouteMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,1),_OspfCurCfgDefaultRouteMetric_Type())
ospfCurCfgDefaultRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgDefaultRouteMetric.setStatus(_A)
class _OspfNewCfgDefaultRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfNewCfgDefaultRouteMetric_Type.__name__=_C
_OspfNewCfgDefaultRouteMetric_Object=MibScalar
ospfNewCfgDefaultRouteMetric=_OspfNewCfgDefaultRouteMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,2),_OspfNewCfgDefaultRouteMetric_Type())
ospfNewCfgDefaultRouteMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgDefaultRouteMetric.setStatus(_A)
class _OspfCurCfgDefaultRouteMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfCurCfgDefaultRouteMetricType_Type.__name__=_C
_OspfCurCfgDefaultRouteMetricType_Object=MibScalar
ospfCurCfgDefaultRouteMetricType=_OspfCurCfgDefaultRouteMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,3),_OspfCurCfgDefaultRouteMetricType_Type())
ospfCurCfgDefaultRouteMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgDefaultRouteMetricType.setStatus(_A)
class _OspfNewCfgDefaultRouteMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfNewCfgDefaultRouteMetricType_Type.__name__=_C
_OspfNewCfgDefaultRouteMetricType_Object=MibScalar
ospfNewCfgDefaultRouteMetricType=_OspfNewCfgDefaultRouteMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,4),_OspfNewCfgDefaultRouteMetricType_Type())
ospfNewCfgDefaultRouteMetricType.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgDefaultRouteMetricType.setStatus(_A)
_OspfIntfTableMaxSize_Type=Integer32
_OspfIntfTableMaxSize_Object=MibScalar
ospfIntfTableMaxSize=_OspfIntfTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,5),_OspfIntfTableMaxSize_Type())
ospfIntfTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTableMaxSize.setStatus(_A)
_OspfAreaTableMaxSize_Type=Integer32
_OspfAreaTableMaxSize_Object=MibScalar
ospfAreaTableMaxSize=_OspfAreaTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,6),_OspfAreaTableMaxSize_Type())
ospfAreaTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTableMaxSize.setStatus(_A)
_OspfRangeTableMaxSize_Type=Integer32
_OspfRangeTableMaxSize_Object=MibScalar
ospfRangeTableMaxSize=_OspfRangeTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,7),_OspfRangeTableMaxSize_Type())
ospfRangeTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRangeTableMaxSize.setStatus(_A)
_OspfVirtIntfTableMaxSize_Type=Integer32
_OspfVirtIntfTableMaxSize_Object=MibScalar
ospfVirtIntfTableMaxSize=_OspfVirtIntfTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,8),_OspfVirtIntfTableMaxSize_Type())
ospfVirtIntfTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIntfTableMaxSize.setStatus(_A)
_OspfHostTableMaxSize_Type=Integer32
_OspfHostTableMaxSize_Object=MibScalar
ospfHostTableMaxSize=_OspfHostTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,9),_OspfHostTableMaxSize_Type())
ospfHostTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfHostTableMaxSize.setStatus(_A)
class _OspfCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_OspfCurCfgState_Type.__name__=_C
_OspfCurCfgState_Object=MibScalar
ospfCurCfgState=_OspfCurCfgState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,10),_OspfCurCfgState_Type())
ospfCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgState.setStatus(_A)
class _OspfNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_OspfNewCfgState_Type.__name__=_C
_OspfNewCfgState_Object=MibScalar
ospfNewCfgState=_OspfNewCfgState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,11),_OspfNewCfgState_Type())
ospfNewCfgState.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgState.setStatus(_A)
class _OspfCurCfgLsdb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_OspfCurCfgLsdb_Type.__name__=_C
_OspfCurCfgLsdb_Object=MibScalar
ospfCurCfgLsdb=_OspfCurCfgLsdb_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,12),_OspfCurCfgLsdb_Type())
ospfCurCfgLsdb.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgLsdb.setStatus(_A)
class _OspfNewCfgLsdb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_OspfNewCfgLsdb_Type.__name__=_C
_OspfNewCfgLsdb_Object=MibScalar
ospfNewCfgLsdb=_OspfNewCfgLsdb_Object((1,3,6,1,4,1,1872,2,5,3,1,13,1,13),_OspfNewCfgLsdb_Type())
ospfNewCfgLsdb.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgLsdb.setStatus(_A)
_OspfCurCfgAreaTable_Object=MibTable
ospfCurCfgAreaTable=_OspfCurCfgAreaTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,2))
if mibBuilder.loadTexts:ospfCurCfgAreaTable.setStatus(_A)
_OspfCurCfgAreaEntry_Object=MibTableRow
ospfCurCfgAreaEntry=_OspfCurCfgAreaEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,2,1))
ospfCurCfgAreaEntry.setIndexNames((0,_G,_AR),(0,_G,_AS))
if mibBuilder.loadTexts:ospfCurCfgAreaEntry.setStatus(_A)
_OspfCurCfgAreaIndex_Type=Integer32
_OspfCurCfgAreaIndex_Object=MibTableColumn
ospfCurCfgAreaIndex=_OspfCurCfgAreaIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,2,1,1),_OspfCurCfgAreaIndex_Type())
ospfCurCfgAreaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaIndex.setStatus(_A)
_OspfCurCfgAreaId_Type=IpAddress
_OspfCurCfgAreaId_Object=MibTableColumn
ospfCurCfgAreaId=_OspfCurCfgAreaId_Object((1,3,6,1,4,1,1872,2,5,3,1,13,2,1,2),_OspfCurCfgAreaId_Type())
ospfCurCfgAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaId.setStatus(_A)
class _OspfCurCfgAreaSpfInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfCurCfgAreaSpfInterval_Type.__name__=_C
_OspfCurCfgAreaSpfInterval_Object=MibTableColumn
ospfCurCfgAreaSpfInterval=_OspfCurCfgAreaSpfInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,13,2,1,3),_OspfCurCfgAreaSpfInterval_Type())
ospfCurCfgAreaSpfInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaSpfInterval.setStatus(_A)
class _OspfCurCfgAreaAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_U,2),(_d,3)))
_OspfCurCfgAreaAuthType_Type.__name__=_C
_OspfCurCfgAreaAuthType_Object=MibTableColumn
ospfCurCfgAreaAuthType=_OspfCurCfgAreaAuthType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,2,1,4),_OspfCurCfgAreaAuthType_Type())
ospfCurCfgAreaAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaAuthType.setStatus(_A)
class _OspfCurCfgAreaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3)))
_OspfCurCfgAreaType_Type.__name__=_C
_OspfCurCfgAreaType_Object=MibTableColumn
ospfCurCfgAreaType=_OspfCurCfgAreaType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,2,1,5),_OspfCurCfgAreaType_Type())
ospfCurCfgAreaType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaType.setStatus(_A)
class _OspfCurCfgAreaMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfCurCfgAreaMetric_Type.__name__=_C
_OspfCurCfgAreaMetric_Object=MibTableColumn
ospfCurCfgAreaMetric=_OspfCurCfgAreaMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,2,1,6),_OspfCurCfgAreaMetric_Type())
ospfCurCfgAreaMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaMetric.setStatus(_A)
class _OspfCurCfgAreaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_OspfCurCfgAreaState_Type.__name__=_C
_OspfCurCfgAreaState_Object=MibTableColumn
ospfCurCfgAreaState=_OspfCurCfgAreaState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,2,1,7),_OspfCurCfgAreaState_Type())
ospfCurCfgAreaState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaState.setStatus(_A)
_OspfNewCfgAreaTable_Object=MibTable
ospfNewCfgAreaTable=_OspfNewCfgAreaTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3))
if mibBuilder.loadTexts:ospfNewCfgAreaTable.setStatus(_A)
_OspfNewCfgAreaEntry_Object=MibTableRow
ospfNewCfgAreaEntry=_OspfNewCfgAreaEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3,1))
ospfNewCfgAreaEntry.setIndexNames((0,_G,_AT),(0,_G,_AU))
if mibBuilder.loadTexts:ospfNewCfgAreaEntry.setStatus(_A)
_OspfNewCfgAreaIndex_Type=Integer32
_OspfNewCfgAreaIndex_Object=MibTableColumn
ospfNewCfgAreaIndex=_OspfNewCfgAreaIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3,1,1),_OspfNewCfgAreaIndex_Type())
ospfNewCfgAreaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgAreaIndex.setStatus(_A)
_OspfNewCfgAreaId_Type=IpAddress
_OspfNewCfgAreaId_Object=MibTableColumn
ospfNewCfgAreaId=_OspfNewCfgAreaId_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3,1,2),_OspfNewCfgAreaId_Type())
ospfNewCfgAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgAreaId.setStatus(_A)
class _OspfNewCfgAreaSpfInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfNewCfgAreaSpfInterval_Type.__name__=_C
_OspfNewCfgAreaSpfInterval_Object=MibTableColumn
ospfNewCfgAreaSpfInterval=_OspfNewCfgAreaSpfInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3,1,3),_OspfNewCfgAreaSpfInterval_Type())
ospfNewCfgAreaSpfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgAreaSpfInterval.setStatus(_A)
class _OspfNewCfgAreaAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_U,2),(_d,3)))
_OspfNewCfgAreaAuthType_Type.__name__=_C
_OspfNewCfgAreaAuthType_Object=MibTableColumn
ospfNewCfgAreaAuthType=_OspfNewCfgAreaAuthType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3,1,4),_OspfNewCfgAreaAuthType_Type())
ospfNewCfgAreaAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgAreaAuthType.setStatus(_A)
class _OspfNewCfgAreaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3)))
_OspfNewCfgAreaType_Type.__name__=_C
_OspfNewCfgAreaType_Object=MibTableColumn
ospfNewCfgAreaType=_OspfNewCfgAreaType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3,1,5),_OspfNewCfgAreaType_Type())
ospfNewCfgAreaType.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgAreaType.setStatus(_A)
class _OspfNewCfgAreaMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfNewCfgAreaMetric_Type.__name__=_C
_OspfNewCfgAreaMetric_Object=MibTableColumn
ospfNewCfgAreaMetric=_OspfNewCfgAreaMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3,1,6),_OspfNewCfgAreaMetric_Type())
ospfNewCfgAreaMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgAreaMetric.setStatus(_A)
class _OspfNewCfgAreaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfNewCfgAreaState_Type.__name__=_C
_OspfNewCfgAreaState_Object=MibTableColumn
ospfNewCfgAreaState=_OspfNewCfgAreaState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3,1,7),_OspfNewCfgAreaState_Type())
ospfNewCfgAreaState.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgAreaState.setStatus(_A)
class _OspfNewCfgAreaDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_OspfNewCfgAreaDelete_Type.__name__=_C
_OspfNewCfgAreaDelete_Object=MibTableColumn
ospfNewCfgAreaDelete=_OspfNewCfgAreaDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,13,3,1,8),_OspfNewCfgAreaDelete_Type())
ospfNewCfgAreaDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgAreaDelete.setStatus(_A)
_OspfRouteRedistribution_ObjectIdentity=ObjectIdentity
ospfRouteRedistribution=_OspfRouteRedistribution_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,13,4))
_OspfRedistributeStatic_ObjectIdentity=ObjectIdentity
ospfRedistributeStatic=_OspfRedistributeStatic_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,13,4,1))
class _OspfCurCfgStaticMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfCurCfgStaticMetric_Type.__name__=_C
_OspfCurCfgStaticMetric_Object=MibScalar
ospfCurCfgStaticMetric=_OspfCurCfgStaticMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,1,1),_OspfCurCfgStaticMetric_Type())
ospfCurCfgStaticMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgStaticMetric.setStatus(_A)
class _OspfNewCfgStaticMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfNewCfgStaticMetric_Type.__name__=_C
_OspfNewCfgStaticMetric_Object=MibScalar
ospfNewCfgStaticMetric=_OspfNewCfgStaticMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,1,2),_OspfNewCfgStaticMetric_Type())
ospfNewCfgStaticMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgStaticMetric.setStatus(_A)
class _OspfCurCfgStaticMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfCurCfgStaticMetricType_Type.__name__=_C
_OspfCurCfgStaticMetricType_Object=MibScalar
ospfCurCfgStaticMetricType=_OspfCurCfgStaticMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,1,3),_OspfCurCfgStaticMetricType_Type())
ospfCurCfgStaticMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgStaticMetricType.setStatus(_A)
class _OspfNewCfgStaticMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfNewCfgStaticMetricType_Type.__name__=_C
_OspfNewCfgStaticMetricType_Object=MibScalar
ospfNewCfgStaticMetricType=_OspfNewCfgStaticMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,1,4),_OspfNewCfgStaticMetricType_Type())
ospfNewCfgStaticMetricType.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgStaticMetricType.setStatus(_A)
_OspfCurCfgStaticOutRmapList_Type=OctetString
_OspfCurCfgStaticOutRmapList_Object=MibScalar
ospfCurCfgStaticOutRmapList=_OspfCurCfgStaticOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,1,5),_OspfCurCfgStaticOutRmapList_Type())
ospfCurCfgStaticOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgStaticOutRmapList.setStatus(_A)
_OspfNewCfgStaticOutRmapList_Type=OctetString
_OspfNewCfgStaticOutRmapList_Object=MibScalar
ospfNewCfgStaticOutRmapList=_OspfNewCfgStaticOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,1,6),_OspfNewCfgStaticOutRmapList_Type())
ospfNewCfgStaticOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgStaticOutRmapList.setStatus(_A)
_OspfNewCfgStaticAddOutRmap_Type=Integer32
_OspfNewCfgStaticAddOutRmap_Object=MibScalar
ospfNewCfgStaticAddOutRmap=_OspfNewCfgStaticAddOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,1,7),_OspfNewCfgStaticAddOutRmap_Type())
ospfNewCfgStaticAddOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgStaticAddOutRmap.setStatus(_A)
_OspfNewCfgStaticRemoveOutRmap_Type=Integer32
_OspfNewCfgStaticRemoveOutRmap_Object=MibScalar
ospfNewCfgStaticRemoveOutRmap=_OspfNewCfgStaticRemoveOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,1,8),_OspfNewCfgStaticRemoveOutRmap_Type())
ospfNewCfgStaticRemoveOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgStaticRemoveOutRmap.setStatus(_A)
_OspfRedistributeEbgp_ObjectIdentity=ObjectIdentity
ospfRedistributeEbgp=_OspfRedistributeEbgp_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,13,4,2))
class _OspfCurCfgEbgpMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfCurCfgEbgpMetric_Type.__name__=_C
_OspfCurCfgEbgpMetric_Object=MibScalar
ospfCurCfgEbgpMetric=_OspfCurCfgEbgpMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,2,1),_OspfCurCfgEbgpMetric_Type())
ospfCurCfgEbgpMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgEbgpMetric.setStatus(_A)
class _OspfNewCfgEbgpMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfNewCfgEbgpMetric_Type.__name__=_C
_OspfNewCfgEbgpMetric_Object=MibScalar
ospfNewCfgEbgpMetric=_OspfNewCfgEbgpMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,2,2),_OspfNewCfgEbgpMetric_Type())
ospfNewCfgEbgpMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgEbgpMetric.setStatus(_A)
class _OspfCurCfgEbgpMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfCurCfgEbgpMetricType_Type.__name__=_C
_OspfCurCfgEbgpMetricType_Object=MibScalar
ospfCurCfgEbgpMetricType=_OspfCurCfgEbgpMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,2,3),_OspfCurCfgEbgpMetricType_Type())
ospfCurCfgEbgpMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgEbgpMetricType.setStatus(_A)
class _OspfNewCfgEbgpMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfNewCfgEbgpMetricType_Type.__name__=_C
_OspfNewCfgEbgpMetricType_Object=MibScalar
ospfNewCfgEbgpMetricType=_OspfNewCfgEbgpMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,2,4),_OspfNewCfgEbgpMetricType_Type())
ospfNewCfgEbgpMetricType.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgEbgpMetricType.setStatus(_A)
_OspfCurCfgEbgpOutRmapList_Type=OctetString
_OspfCurCfgEbgpOutRmapList_Object=MibScalar
ospfCurCfgEbgpOutRmapList=_OspfCurCfgEbgpOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,2,5),_OspfCurCfgEbgpOutRmapList_Type())
ospfCurCfgEbgpOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgEbgpOutRmapList.setStatus(_A)
_OspfNewCfgEbgpOutRmapList_Type=OctetString
_OspfNewCfgEbgpOutRmapList_Object=MibScalar
ospfNewCfgEbgpOutRmapList=_OspfNewCfgEbgpOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,2,6),_OspfNewCfgEbgpOutRmapList_Type())
ospfNewCfgEbgpOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgEbgpOutRmapList.setStatus(_A)
_OspfNewCfgEbgpAddOutRmap_Type=Integer32
_OspfNewCfgEbgpAddOutRmap_Object=MibScalar
ospfNewCfgEbgpAddOutRmap=_OspfNewCfgEbgpAddOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,2,7),_OspfNewCfgEbgpAddOutRmap_Type())
ospfNewCfgEbgpAddOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgEbgpAddOutRmap.setStatus(_A)
_OspfNewCfgEbgpRemoveOutRmap_Type=Integer32
_OspfNewCfgEbgpRemoveOutRmap_Object=MibScalar
ospfNewCfgEbgpRemoveOutRmap=_OspfNewCfgEbgpRemoveOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,2,8),_OspfNewCfgEbgpRemoveOutRmap_Type())
ospfNewCfgEbgpRemoveOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgEbgpRemoveOutRmap.setStatus(_A)
_OspfRedistributeIbgp_ObjectIdentity=ObjectIdentity
ospfRedistributeIbgp=_OspfRedistributeIbgp_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,13,4,3))
class _OspfCurCfgIbgpMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfCurCfgIbgpMetric_Type.__name__=_C
_OspfCurCfgIbgpMetric_Object=MibScalar
ospfCurCfgIbgpMetric=_OspfCurCfgIbgpMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,3,1),_OspfCurCfgIbgpMetric_Type())
ospfCurCfgIbgpMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIbgpMetric.setStatus(_A)
class _OspfNewCfgIbgpMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfNewCfgIbgpMetric_Type.__name__=_C
_OspfNewCfgIbgpMetric_Object=MibScalar
ospfNewCfgIbgpMetric=_OspfNewCfgIbgpMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,3,2),_OspfNewCfgIbgpMetric_Type())
ospfNewCfgIbgpMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgIbgpMetric.setStatus(_A)
class _OspfCurCfgIbgpMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfCurCfgIbgpMetricType_Type.__name__=_C
_OspfCurCfgIbgpMetricType_Object=MibScalar
ospfCurCfgIbgpMetricType=_OspfCurCfgIbgpMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,3,3),_OspfCurCfgIbgpMetricType_Type())
ospfCurCfgIbgpMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIbgpMetricType.setStatus(_A)
class _OspfNewCfgIbgpMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfNewCfgIbgpMetricType_Type.__name__=_C
_OspfNewCfgIbgpMetricType_Object=MibScalar
ospfNewCfgIbgpMetricType=_OspfNewCfgIbgpMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,3,4),_OspfNewCfgIbgpMetricType_Type())
ospfNewCfgIbgpMetricType.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgIbgpMetricType.setStatus(_A)
_OspfCurCfgIbgpOutRmapList_Type=OctetString
_OspfCurCfgIbgpOutRmapList_Object=MibScalar
ospfCurCfgIbgpOutRmapList=_OspfCurCfgIbgpOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,3,5),_OspfCurCfgIbgpOutRmapList_Type())
ospfCurCfgIbgpOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIbgpOutRmapList.setStatus(_A)
_OspfNewCfgIbgpOutRmapList_Type=OctetString
_OspfNewCfgIbgpOutRmapList_Object=MibScalar
ospfNewCfgIbgpOutRmapList=_OspfNewCfgIbgpOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,3,6),_OspfNewCfgIbgpOutRmapList_Type())
ospfNewCfgIbgpOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgIbgpOutRmapList.setStatus(_A)
_OspfNewCfgIbgpAddOutRmap_Type=Integer32
_OspfNewCfgIbgpAddOutRmap_Object=MibScalar
ospfNewCfgIbgpAddOutRmap=_OspfNewCfgIbgpAddOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,3,7),_OspfNewCfgIbgpAddOutRmap_Type())
ospfNewCfgIbgpAddOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgIbgpAddOutRmap.setStatus(_A)
_OspfNewCfgIbgpRemoveOutRmap_Type=Integer32
_OspfNewCfgIbgpRemoveOutRmap_Object=MibScalar
ospfNewCfgIbgpRemoveOutRmap=_OspfNewCfgIbgpRemoveOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,3,8),_OspfNewCfgIbgpRemoveOutRmap_Type())
ospfNewCfgIbgpRemoveOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgIbgpRemoveOutRmap.setStatus(_A)
_OspfRedistributeFixed_ObjectIdentity=ObjectIdentity
ospfRedistributeFixed=_OspfRedistributeFixed_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,13,4,4))
class _OspfCurCfgFixedMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfCurCfgFixedMetric_Type.__name__=_C
_OspfCurCfgFixedMetric_Object=MibScalar
ospfCurCfgFixedMetric=_OspfCurCfgFixedMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,4,1),_OspfCurCfgFixedMetric_Type())
ospfCurCfgFixedMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgFixedMetric.setStatus(_A)
class _OspfNewCfgFixedMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfNewCfgFixedMetric_Type.__name__=_C
_OspfNewCfgFixedMetric_Object=MibScalar
ospfNewCfgFixedMetric=_OspfNewCfgFixedMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,4,2),_OspfNewCfgFixedMetric_Type())
ospfNewCfgFixedMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgFixedMetric.setStatus(_A)
class _OspfCurCfgFixedMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfCurCfgFixedMetricType_Type.__name__=_C
_OspfCurCfgFixedMetricType_Object=MibScalar
ospfCurCfgFixedMetricType=_OspfCurCfgFixedMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,4,3),_OspfCurCfgFixedMetricType_Type())
ospfCurCfgFixedMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgFixedMetricType.setStatus(_A)
class _OspfNewCfgFixedMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfNewCfgFixedMetricType_Type.__name__=_C
_OspfNewCfgFixedMetricType_Object=MibScalar
ospfNewCfgFixedMetricType=_OspfNewCfgFixedMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,4,4),_OspfNewCfgFixedMetricType_Type())
ospfNewCfgFixedMetricType.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgFixedMetricType.setStatus(_A)
_OspfCurCfgFixedOutRmapList_Type=OctetString
_OspfCurCfgFixedOutRmapList_Object=MibScalar
ospfCurCfgFixedOutRmapList=_OspfCurCfgFixedOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,4,5),_OspfCurCfgFixedOutRmapList_Type())
ospfCurCfgFixedOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgFixedOutRmapList.setStatus(_A)
_OspfNewCfgFixedOutRmapList_Type=OctetString
_OspfNewCfgFixedOutRmapList_Object=MibScalar
ospfNewCfgFixedOutRmapList=_OspfNewCfgFixedOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,4,6),_OspfNewCfgFixedOutRmapList_Type())
ospfNewCfgFixedOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgFixedOutRmapList.setStatus(_A)
_OspfNewCfgFixedAddOutRmap_Type=Integer32
_OspfNewCfgFixedAddOutRmap_Object=MibScalar
ospfNewCfgFixedAddOutRmap=_OspfNewCfgFixedAddOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,4,7),_OspfNewCfgFixedAddOutRmap_Type())
ospfNewCfgFixedAddOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgFixedAddOutRmap.setStatus(_A)
_OspfNewCfgFixedRemoveOutRmap_Type=Integer32
_OspfNewCfgFixedRemoveOutRmap_Object=MibScalar
ospfNewCfgFixedRemoveOutRmap=_OspfNewCfgFixedRemoveOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,4,8),_OspfNewCfgFixedRemoveOutRmap_Type())
ospfNewCfgFixedRemoveOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgFixedRemoveOutRmap.setStatus(_A)
_OspfRedistributeRip_ObjectIdentity=ObjectIdentity
ospfRedistributeRip=_OspfRedistributeRip_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,13,4,5))
class _OspfCurCfgRipMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfCurCfgRipMetric_Type.__name__=_C
_OspfCurCfgRipMetric_Object=MibScalar
ospfCurCfgRipMetric=_OspfCurCfgRipMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,5,1),_OspfCurCfgRipMetric_Type())
ospfCurCfgRipMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgRipMetric.setStatus(_A)
class _OspfNewCfgRipMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfNewCfgRipMetric_Type.__name__=_C
_OspfNewCfgRipMetric_Object=MibScalar
ospfNewCfgRipMetric=_OspfNewCfgRipMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,5,2),_OspfNewCfgRipMetric_Type())
ospfNewCfgRipMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgRipMetric.setStatus(_A)
class _OspfCurCfgRipMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfCurCfgRipMetricType_Type.__name__=_C
_OspfCurCfgRipMetricType_Object=MibScalar
ospfCurCfgRipMetricType=_OspfCurCfgRipMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,5,3),_OspfCurCfgRipMetricType_Type())
ospfCurCfgRipMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgRipMetricType.setStatus(_A)
class _OspfNewCfgRipMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),(_O,3)))
_OspfNewCfgRipMetricType_Type.__name__=_C
_OspfNewCfgRipMetricType_Object=MibScalar
ospfNewCfgRipMetricType=_OspfNewCfgRipMetricType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,5,4),_OspfNewCfgRipMetricType_Type())
ospfNewCfgRipMetricType.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgRipMetricType.setStatus(_A)
_OspfCurCfgRipOutRmapList_Type=OctetString
_OspfCurCfgRipOutRmapList_Object=MibScalar
ospfCurCfgRipOutRmapList=_OspfCurCfgRipOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,5,5),_OspfCurCfgRipOutRmapList_Type())
ospfCurCfgRipOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgRipOutRmapList.setStatus(_A)
_OspfNewCfgRipOutRmapList_Type=OctetString
_OspfNewCfgRipOutRmapList_Object=MibScalar
ospfNewCfgRipOutRmapList=_OspfNewCfgRipOutRmapList_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,5,6),_OspfNewCfgRipOutRmapList_Type())
ospfNewCfgRipOutRmapList.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgRipOutRmapList.setStatus(_A)
_OspfNewCfgRipAddOutRmap_Type=Integer32
_OspfNewCfgRipAddOutRmap_Object=MibScalar
ospfNewCfgRipAddOutRmap=_OspfNewCfgRipAddOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,5,7),_OspfNewCfgRipAddOutRmap_Type())
ospfNewCfgRipAddOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgRipAddOutRmap.setStatus(_A)
_OspfNewCfgRipRemoveOutRmap_Type=Integer32
_OspfNewCfgRipRemoveOutRmap_Object=MibScalar
ospfNewCfgRipRemoveOutRmap=_OspfNewCfgRipRemoveOutRmap_Object((1,3,6,1,4,1,1872,2,5,3,1,13,4,5,8),_OspfNewCfgRipRemoveOutRmap_Type())
ospfNewCfgRipRemoveOutRmap.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgRipRemoveOutRmap.setStatus(_A)
_OspfCurCfgMdkeyTable_Object=MibTable
ospfCurCfgMdkeyTable=_OspfCurCfgMdkeyTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,5))
if mibBuilder.loadTexts:ospfCurCfgMdkeyTable.setStatus(_A)
_OspfCurCfgMdkeyEntry_Object=MibTableRow
ospfCurCfgMdkeyEntry=_OspfCurCfgMdkeyEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,5,1))
ospfCurCfgMdkeyEntry.setIndexNames((0,_G,_AV))
if mibBuilder.loadTexts:ospfCurCfgMdkeyEntry.setStatus(_A)
_OspfCurCfgMdkeyIndex_Type=Integer32
_OspfCurCfgMdkeyIndex_Object=MibTableColumn
ospfCurCfgMdkeyIndex=_OspfCurCfgMdkeyIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,5,1,1),_OspfCurCfgMdkeyIndex_Type())
ospfCurCfgMdkeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgMdkeyIndex.setStatus(_A)
class _OspfCurCfgMdkeyKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_OspfCurCfgMdkeyKey_Type.__name__=_I
_OspfCurCfgMdkeyKey_Object=MibTableColumn
ospfCurCfgMdkeyKey=_OspfCurCfgMdkeyKey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,5,1,2),_OspfCurCfgMdkeyKey_Type())
ospfCurCfgMdkeyKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgMdkeyKey.setStatus(_A)
_OspfNewCfgMdkeyTable_Object=MibTable
ospfNewCfgMdkeyTable=_OspfNewCfgMdkeyTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,6))
if mibBuilder.loadTexts:ospfNewCfgMdkeyTable.setStatus(_A)
_OspfNewCfgMdkeyEntry_Object=MibTableRow
ospfNewCfgMdkeyEntry=_OspfNewCfgMdkeyEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,6,1))
ospfNewCfgMdkeyEntry.setIndexNames((0,_G,_AW))
if mibBuilder.loadTexts:ospfNewCfgMdkeyEntry.setStatus(_A)
_OspfNewCfgMdkeyIndex_Type=Integer32
_OspfNewCfgMdkeyIndex_Object=MibTableColumn
ospfNewCfgMdkeyIndex=_OspfNewCfgMdkeyIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,6,1,1),_OspfNewCfgMdkeyIndex_Type())
ospfNewCfgMdkeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgMdkeyIndex.setStatus(_A)
class _OspfNewCfgMdkeyKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_OspfNewCfgMdkeyKey_Type.__name__=_I
_OspfNewCfgMdkeyKey_Object=MibTableColumn
ospfNewCfgMdkeyKey=_OspfNewCfgMdkeyKey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,6,1,2),_OspfNewCfgMdkeyKey_Type())
ospfNewCfgMdkeyKey.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgMdkeyKey.setStatus(_A)
class _OspfNewCfgMdkeyDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_OspfNewCfgMdkeyDelete_Type.__name__=_C
_OspfNewCfgMdkeyDelete_Object=MibTableColumn
ospfNewCfgMdkeyDelete=_OspfNewCfgMdkeyDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,13,6,1,3),_OspfNewCfgMdkeyDelete_Type())
ospfNewCfgMdkeyDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgMdkeyDelete.setStatus(_A)
_OspfCurCfgIntfTable_Object=MibTable
ospfCurCfgIntfTable=_OspfCurCfgIntfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7))
if mibBuilder.loadTexts:ospfCurCfgIntfTable.setStatus(_A)
_OspfCurCfgIntfEntry_Object=MibTableRow
ospfCurCfgIntfEntry=_OspfCurCfgIntfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1))
ospfCurCfgIntfEntry.setIndexNames((0,_G,_AX))
if mibBuilder.loadTexts:ospfCurCfgIntfEntry.setStatus(_A)
_OspfCurCfgIntfIndex_Type=Integer32
_OspfCurCfgIntfIndex_Object=MibTableColumn
ospfCurCfgIntfIndex=_OspfCurCfgIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,1),_OspfCurCfgIntfIndex_Type())
ospfCurCfgIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfIndex.setStatus(_A)
_OspfCurCfgIntfId_Type=IpAddress
_OspfCurCfgIntfId_Object=MibTableColumn
ospfCurCfgIntfId=_OspfCurCfgIntfId_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,2),_OspfCurCfgIntfId_Type())
ospfCurCfgIntfId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfId.setStatus(_A)
class _OspfCurCfgIntfMdkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfCurCfgIntfMdkey_Type.__name__=_C
_OspfCurCfgIntfMdkey_Object=MibTableColumn
ospfCurCfgIntfMdkey=_OspfCurCfgIntfMdkey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,3),_OspfCurCfgIntfMdkey_Type())
ospfCurCfgIntfMdkey.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfMdkey.setStatus(_A)
class _OspfCurCfgIntfAreaId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_OspfCurCfgIntfAreaId_Type.__name__=_C
_OspfCurCfgIntfAreaId_Object=MibTableColumn
ospfCurCfgIntfAreaId=_OspfCurCfgIntfAreaId_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,4),_OspfCurCfgIntfAreaId_Type())
ospfCurCfgIntfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfAreaId.setStatus(_A)
class _OspfCurCfgIntfPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfCurCfgIntfPriority_Type.__name__=_C
_OspfCurCfgIntfPriority_Object=MibTableColumn
ospfCurCfgIntfPriority=_OspfCurCfgIntfPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,5),_OspfCurCfgIntfPriority_Type())
ospfCurCfgIntfPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfPriority.setStatus(_A)
class _OspfCurCfgIntfCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfCurCfgIntfCost_Type.__name__=_C
_OspfCurCfgIntfCost_Object=MibTableColumn
ospfCurCfgIntfCost=_OspfCurCfgIntfCost_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,6),_OspfCurCfgIntfCost_Type())
ospfCurCfgIntfCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfCost.setStatus(_A)
class _OspfCurCfgIntfHello_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfCurCfgIntfHello_Type.__name__=_C
_OspfCurCfgIntfHello_Object=MibTableColumn
ospfCurCfgIntfHello=_OspfCurCfgIntfHello_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,7),_OspfCurCfgIntfHello_Type())
ospfCurCfgIntfHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfHello.setStatus(_A)
class _OspfCurCfgIntfDead_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfCurCfgIntfDead_Type.__name__=_C
_OspfCurCfgIntfDead_Object=MibTableColumn
ospfCurCfgIntfDead=_OspfCurCfgIntfDead_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,8),_OspfCurCfgIntfDead_Type())
ospfCurCfgIntfDead.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfDead.setStatus(_A)
class _OspfCurCfgIntfTransit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_OspfCurCfgIntfTransit_Type.__name__=_C
_OspfCurCfgIntfTransit_Object=MibTableColumn
ospfCurCfgIntfTransit=_OspfCurCfgIntfTransit_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,9),_OspfCurCfgIntfTransit_Type())
ospfCurCfgIntfTransit.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfTransit.setStatus(_A)
class _OspfCurCfgIntfRetrans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_OspfCurCfgIntfRetrans_Type.__name__=_C
_OspfCurCfgIntfRetrans_Object=MibTableColumn
ospfCurCfgIntfRetrans=_OspfCurCfgIntfRetrans_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,10),_OspfCurCfgIntfRetrans_Type())
ospfCurCfgIntfRetrans.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfRetrans.setStatus(_A)
class _OspfCurCfgIntfKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_OspfCurCfgIntfKey_Type.__name__=_I
_OspfCurCfgIntfKey_Object=MibTableColumn
ospfCurCfgIntfKey=_OspfCurCfgIntfKey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,11),_OspfCurCfgIntfKey_Type())
ospfCurCfgIntfKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfKey.setStatus(_A)
class _OspfCurCfgIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfCurCfgIntfState_Type.__name__=_C
_OspfCurCfgIntfState_Object=MibTableColumn
ospfCurCfgIntfState=_OspfCurCfgIntfState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,7,1,12),_OspfCurCfgIntfState_Type())
ospfCurCfgIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgIntfState.setStatus(_A)
_OspfNewCfgIntfTable_Object=MibTable
ospfNewCfgIntfTable=_OspfNewCfgIntfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8))
if mibBuilder.loadTexts:ospfNewCfgIntfTable.setStatus(_A)
_OspfNewCfgIntfEntry_Object=MibTableRow
ospfNewCfgIntfEntry=_OspfNewCfgIntfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1))
ospfNewCfgIntfEntry.setIndexNames((0,_G,_AY))
if mibBuilder.loadTexts:ospfNewCfgIntfEntry.setStatus(_A)
_OspfNewCfgIntfIndex_Type=Integer32
_OspfNewCfgIntfIndex_Object=MibTableColumn
ospfNewCfgIntfIndex=_OspfNewCfgIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,1),_OspfNewCfgIntfIndex_Type())
ospfNewCfgIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgIntfIndex.setStatus(_A)
_OspfNewCfgIntfId_Type=IpAddress
_OspfNewCfgIntfId_Object=MibTableColumn
ospfNewCfgIntfId=_OspfNewCfgIntfId_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,2),_OspfNewCfgIntfId_Type())
ospfNewCfgIntfId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgIntfId.setStatus(_A)
class _OspfNewCfgIntfMdkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfNewCfgIntfMdkey_Type.__name__=_C
_OspfNewCfgIntfMdkey_Object=MibTableColumn
ospfNewCfgIntfMdkey=_OspfNewCfgIntfMdkey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,3),_OspfNewCfgIntfMdkey_Type())
ospfNewCfgIntfMdkey.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfMdkey.setStatus(_A)
class _OspfNewCfgIntfAreaId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_OspfNewCfgIntfAreaId_Type.__name__=_C
_OspfNewCfgIntfAreaId_Object=MibTableColumn
ospfNewCfgIntfAreaId=_OspfNewCfgIntfAreaId_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,4),_OspfNewCfgIntfAreaId_Type())
ospfNewCfgIntfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfAreaId.setStatus(_A)
class _OspfNewCfgIntfPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfNewCfgIntfPriority_Type.__name__=_C
_OspfNewCfgIntfPriority_Object=MibTableColumn
ospfNewCfgIntfPriority=_OspfNewCfgIntfPriority_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,5),_OspfNewCfgIntfPriority_Type())
ospfNewCfgIntfPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfPriority.setStatus(_A)
class _OspfNewCfgIntfCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfNewCfgIntfCost_Type.__name__=_C
_OspfNewCfgIntfCost_Object=MibTableColumn
ospfNewCfgIntfCost=_OspfNewCfgIntfCost_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,6),_OspfNewCfgIntfCost_Type())
ospfNewCfgIntfCost.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfCost.setStatus(_A)
class _OspfNewCfgIntfHello_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfNewCfgIntfHello_Type.__name__=_C
_OspfNewCfgIntfHello_Object=MibTableColumn
ospfNewCfgIntfHello=_OspfNewCfgIntfHello_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,7),_OspfNewCfgIntfHello_Type())
ospfNewCfgIntfHello.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfHello.setStatus(_A)
class _OspfNewCfgIntfDead_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfNewCfgIntfDead_Type.__name__=_C
_OspfNewCfgIntfDead_Object=MibTableColumn
ospfNewCfgIntfDead=_OspfNewCfgIntfDead_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,8),_OspfNewCfgIntfDead_Type())
ospfNewCfgIntfDead.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfDead.setStatus(_A)
class _OspfNewCfgIntfTransit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_OspfNewCfgIntfTransit_Type.__name__=_C
_OspfNewCfgIntfTransit_Object=MibTableColumn
ospfNewCfgIntfTransit=_OspfNewCfgIntfTransit_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,9),_OspfNewCfgIntfTransit_Type())
ospfNewCfgIntfTransit.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfTransit.setStatus(_A)
class _OspfNewCfgIntfRetrans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_OspfNewCfgIntfRetrans_Type.__name__=_C
_OspfNewCfgIntfRetrans_Object=MibTableColumn
ospfNewCfgIntfRetrans=_OspfNewCfgIntfRetrans_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,10),_OspfNewCfgIntfRetrans_Type())
ospfNewCfgIntfRetrans.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfRetrans.setStatus(_A)
class _OspfNewCfgIntfKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_OspfNewCfgIntfKey_Type.__name__=_I
_OspfNewCfgIntfKey_Object=MibTableColumn
ospfNewCfgIntfKey=_OspfNewCfgIntfKey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,11),_OspfNewCfgIntfKey_Type())
ospfNewCfgIntfKey.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfKey.setStatus(_A)
class _OspfNewCfgIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfNewCfgIntfState_Type.__name__=_C
_OspfNewCfgIntfState_Object=MibTableColumn
ospfNewCfgIntfState=_OspfNewCfgIntfState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,12),_OspfNewCfgIntfState_Type())
ospfNewCfgIntfState.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfState.setStatus(_A)
class _OspfNewCfgIntfDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_OspfNewCfgIntfDelete_Type.__name__=_C
_OspfNewCfgIntfDelete_Object=MibTableColumn
ospfNewCfgIntfDelete=_OspfNewCfgIntfDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,13,8,1,13),_OspfNewCfgIntfDelete_Type())
ospfNewCfgIntfDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgIntfDelete.setStatus(_A)
_OspfCurCfgVirtIntfTable_Object=MibTable
ospfCurCfgVirtIntfTable=_OspfCurCfgVirtIntfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9))
if mibBuilder.loadTexts:ospfCurCfgVirtIntfTable.setStatus(_A)
_OspfCurCfgVirtIntfEntry_Object=MibTableRow
ospfCurCfgVirtIntfEntry=_OspfCurCfgVirtIntfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1))
ospfCurCfgVirtIntfEntry.setIndexNames((0,_G,_AZ))
if mibBuilder.loadTexts:ospfCurCfgVirtIntfEntry.setStatus(_A)
_OspfCurCfgVirtIntfIndex_Type=Integer32
_OspfCurCfgVirtIntfIndex_Object=MibTableColumn
ospfCurCfgVirtIntfIndex=_OspfCurCfgVirtIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,1),_OspfCurCfgVirtIntfIndex_Type())
ospfCurCfgVirtIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfIndex.setStatus(_A)
class _OspfCurCfgVirtIntfAreaId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_OspfCurCfgVirtIntfAreaId_Type.__name__=_C
_OspfCurCfgVirtIntfAreaId_Object=MibTableColumn
ospfCurCfgVirtIntfAreaId=_OspfCurCfgVirtIntfAreaId_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,2),_OspfCurCfgVirtIntfAreaId_Type())
ospfCurCfgVirtIntfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfAreaId.setStatus(_A)
_OspfCurCfgVirtIntfNbr_Type=IpAddress
_OspfCurCfgVirtIntfNbr_Object=MibTableColumn
ospfCurCfgVirtIntfNbr=_OspfCurCfgVirtIntfNbr_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,3),_OspfCurCfgVirtIntfNbr_Type())
ospfCurCfgVirtIntfNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfNbr.setStatus(_A)
class _OspfCurCfgVirtIntfMdkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfCurCfgVirtIntfMdkey_Type.__name__=_C
_OspfCurCfgVirtIntfMdkey_Object=MibTableColumn
ospfCurCfgVirtIntfMdkey=_OspfCurCfgVirtIntfMdkey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,4),_OspfCurCfgVirtIntfMdkey_Type())
ospfCurCfgVirtIntfMdkey.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfMdkey.setStatus(_A)
class _OspfCurCfgVirtIntfHello_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfCurCfgVirtIntfHello_Type.__name__=_C
_OspfCurCfgVirtIntfHello_Object=MibTableColumn
ospfCurCfgVirtIntfHello=_OspfCurCfgVirtIntfHello_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,5),_OspfCurCfgVirtIntfHello_Type())
ospfCurCfgVirtIntfHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfHello.setStatus(_A)
class _OspfCurCfgVirtIntfDead_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfCurCfgVirtIntfDead_Type.__name__=_C
_OspfCurCfgVirtIntfDead_Object=MibTableColumn
ospfCurCfgVirtIntfDead=_OspfCurCfgVirtIntfDead_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,6),_OspfCurCfgVirtIntfDead_Type())
ospfCurCfgVirtIntfDead.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfDead.setStatus(_A)
class _OspfCurCfgVirtIntfTransit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_OspfCurCfgVirtIntfTransit_Type.__name__=_C
_OspfCurCfgVirtIntfTransit_Object=MibTableColumn
ospfCurCfgVirtIntfTransit=_OspfCurCfgVirtIntfTransit_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,7),_OspfCurCfgVirtIntfTransit_Type())
ospfCurCfgVirtIntfTransit.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfTransit.setStatus(_A)
class _OspfCurCfgVirtIntfRetrans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_OspfCurCfgVirtIntfRetrans_Type.__name__=_C
_OspfCurCfgVirtIntfRetrans_Object=MibTableColumn
ospfCurCfgVirtIntfRetrans=_OspfCurCfgVirtIntfRetrans_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,8),_OspfCurCfgVirtIntfRetrans_Type())
ospfCurCfgVirtIntfRetrans.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfRetrans.setStatus(_A)
class _OspfCurCfgVirtIntfKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_OspfCurCfgVirtIntfKey_Type.__name__=_I
_OspfCurCfgVirtIntfKey_Object=MibTableColumn
ospfCurCfgVirtIntfKey=_OspfCurCfgVirtIntfKey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,9),_OspfCurCfgVirtIntfKey_Type())
ospfCurCfgVirtIntfKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfKey.setStatus(_A)
class _OspfCurCfgVirtIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfCurCfgVirtIntfState_Type.__name__=_C
_OspfCurCfgVirtIntfState_Object=MibTableColumn
ospfCurCfgVirtIntfState=_OspfCurCfgVirtIntfState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,9,1,10),_OspfCurCfgVirtIntfState_Type())
ospfCurCfgVirtIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgVirtIntfState.setStatus(_A)
_OspfNewCfgVirtIntfTable_Object=MibTable
ospfNewCfgVirtIntfTable=_OspfNewCfgVirtIntfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10))
if mibBuilder.loadTexts:ospfNewCfgVirtIntfTable.setStatus(_A)
_OspfNewCfgVirtIntfEntry_Object=MibTableRow
ospfNewCfgVirtIntfEntry=_OspfNewCfgVirtIntfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1))
ospfNewCfgVirtIntfEntry.setIndexNames((0,_G,_Aa))
if mibBuilder.loadTexts:ospfNewCfgVirtIntfEntry.setStatus(_A)
_OspfNewCfgVirtIntfIndex_Type=Integer32
_OspfNewCfgVirtIntfIndex_Object=MibTableColumn
ospfNewCfgVirtIntfIndex=_OspfNewCfgVirtIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,1),_OspfNewCfgVirtIntfIndex_Type())
ospfNewCfgVirtIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfIndex.setStatus(_A)
class _OspfNewCfgVirtIntfAreaId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_OspfNewCfgVirtIntfAreaId_Type.__name__=_C
_OspfNewCfgVirtIntfAreaId_Object=MibTableColumn
ospfNewCfgVirtIntfAreaId=_OspfNewCfgVirtIntfAreaId_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,2),_OspfNewCfgVirtIntfAreaId_Type())
ospfNewCfgVirtIntfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfAreaId.setStatus(_A)
_OspfNewCfgVirtIntfNbr_Type=IpAddress
_OspfNewCfgVirtIntfNbr_Object=MibTableColumn
ospfNewCfgVirtIntfNbr=_OspfNewCfgVirtIntfNbr_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,3),_OspfNewCfgVirtIntfNbr_Type())
ospfNewCfgVirtIntfNbr.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfNbr.setStatus(_A)
class _OspfNewCfgVirtIntfMdkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfNewCfgVirtIntfMdkey_Type.__name__=_C
_OspfNewCfgVirtIntfMdkey_Object=MibTableColumn
ospfNewCfgVirtIntfMdkey=_OspfNewCfgVirtIntfMdkey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,4),_OspfNewCfgVirtIntfMdkey_Type())
ospfNewCfgVirtIntfMdkey.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfMdkey.setStatus(_A)
class _OspfNewCfgVirtIntfHello_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfNewCfgVirtIntfHello_Type.__name__=_C
_OspfNewCfgVirtIntfHello_Object=MibTableColumn
ospfNewCfgVirtIntfHello=_OspfNewCfgVirtIntfHello_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,5),_OspfNewCfgVirtIntfHello_Type())
ospfNewCfgVirtIntfHello.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfHello.setStatus(_A)
class _OspfNewCfgVirtIntfDead_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfNewCfgVirtIntfDead_Type.__name__=_C
_OspfNewCfgVirtIntfDead_Object=MibTableColumn
ospfNewCfgVirtIntfDead=_OspfNewCfgVirtIntfDead_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,6),_OspfNewCfgVirtIntfDead_Type())
ospfNewCfgVirtIntfDead.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfDead.setStatus(_A)
class _OspfNewCfgVirtIntfTransit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_OspfNewCfgVirtIntfTransit_Type.__name__=_C
_OspfNewCfgVirtIntfTransit_Object=MibTableColumn
ospfNewCfgVirtIntfTransit=_OspfNewCfgVirtIntfTransit_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,7),_OspfNewCfgVirtIntfTransit_Type())
ospfNewCfgVirtIntfTransit.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfTransit.setStatus(_A)
class _OspfNewCfgVirtIntfRetrans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_OspfNewCfgVirtIntfRetrans_Type.__name__=_C
_OspfNewCfgVirtIntfRetrans_Object=MibTableColumn
ospfNewCfgVirtIntfRetrans=_OspfNewCfgVirtIntfRetrans_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,8),_OspfNewCfgVirtIntfRetrans_Type())
ospfNewCfgVirtIntfRetrans.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfRetrans.setStatus(_A)
class _OspfNewCfgVirtIntfKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_OspfNewCfgVirtIntfKey_Type.__name__=_I
_OspfNewCfgVirtIntfKey_Object=MibTableColumn
ospfNewCfgVirtIntfKey=_OspfNewCfgVirtIntfKey_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,9),_OspfNewCfgVirtIntfKey_Type())
ospfNewCfgVirtIntfKey.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfKey.setStatus(_A)
class _OspfNewCfgVirtIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfNewCfgVirtIntfState_Type.__name__=_C
_OspfNewCfgVirtIntfState_Object=MibTableColumn
ospfNewCfgVirtIntfState=_OspfNewCfgVirtIntfState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,10),_OspfNewCfgVirtIntfState_Type())
ospfNewCfgVirtIntfState.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfState.setStatus(_A)
class _OspfNewCfgVirtIntfDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_OspfNewCfgVirtIntfDelete_Type.__name__=_C
_OspfNewCfgVirtIntfDelete_Object=MibTableColumn
ospfNewCfgVirtIntfDelete=_OspfNewCfgVirtIntfDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,13,10,1,11),_OspfNewCfgVirtIntfDelete_Type())
ospfNewCfgVirtIntfDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVirtIntfDelete.setStatus(_A)
_OspfMdkeyTableMaxSize_Type=Integer32
_OspfMdkeyTableMaxSize_Object=MibScalar
ospfMdkeyTableMaxSize=_OspfMdkeyTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,13,11),_OspfMdkeyTableMaxSize_Type())
ospfMdkeyTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfMdkeyTableMaxSize.setStatus(_A)
_OspfCurCfgHostTable_Object=MibTable
ospfCurCfgHostTable=_OspfCurCfgHostTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,12))
if mibBuilder.loadTexts:ospfCurCfgHostTable.setStatus(_A)
_OspfCurCfgHostEntry_Object=MibTableRow
ospfCurCfgHostEntry=_OspfCurCfgHostEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,12,1))
ospfCurCfgHostEntry.setIndexNames((0,_G,_Ab))
if mibBuilder.loadTexts:ospfCurCfgHostEntry.setStatus(_A)
_OspfCurCfgHostIndex_Type=Integer32
_OspfCurCfgHostIndex_Object=MibTableColumn
ospfCurCfgHostIndex=_OspfCurCfgHostIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,12,1,1),_OspfCurCfgHostIndex_Type())
ospfCurCfgHostIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgHostIndex.setStatus(_A)
_OspfCurCfgHostIpAddr_Type=IpAddress
_OspfCurCfgHostIpAddr_Object=MibTableColumn
ospfCurCfgHostIpAddr=_OspfCurCfgHostIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,13,12,1,2),_OspfCurCfgHostIpAddr_Type())
ospfCurCfgHostIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgHostIpAddr.setStatus(_A)
_OspfCurCfgHostAreaIndex_Type=Integer32
_OspfCurCfgHostAreaIndex_Object=MibTableColumn
ospfCurCfgHostAreaIndex=_OspfCurCfgHostAreaIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,12,1,3),_OspfCurCfgHostAreaIndex_Type())
ospfCurCfgHostAreaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgHostAreaIndex.setStatus(_A)
class _OspfCurCfgHostCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfCurCfgHostCost_Type.__name__=_C
_OspfCurCfgHostCost_Object=MibTableColumn
ospfCurCfgHostCost=_OspfCurCfgHostCost_Object((1,3,6,1,4,1,1872,2,5,3,1,13,12,1,4),_OspfCurCfgHostCost_Type())
ospfCurCfgHostCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgHostCost.setStatus(_A)
class _OspfCurCfgHostState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfCurCfgHostState_Type.__name__=_C
_OspfCurCfgHostState_Object=MibTableColumn
ospfCurCfgHostState=_OspfCurCfgHostState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,12,1,5),_OspfCurCfgHostState_Type())
ospfCurCfgHostState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgHostState.setStatus(_A)
_OspfNewCfgHostTable_Object=MibTable
ospfNewCfgHostTable=_OspfNewCfgHostTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,13))
if mibBuilder.loadTexts:ospfNewCfgHostTable.setStatus(_A)
_OspfNewCfgHostEntry_Object=MibTableRow
ospfNewCfgHostEntry=_OspfNewCfgHostEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,13,1))
ospfNewCfgHostEntry.setIndexNames((0,_G,_Ac))
if mibBuilder.loadTexts:ospfNewCfgHostEntry.setStatus(_A)
_OspfNewCfgHostIndex_Type=Integer32
_OspfNewCfgHostIndex_Object=MibTableColumn
ospfNewCfgHostIndex=_OspfNewCfgHostIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,13,1,1),_OspfNewCfgHostIndex_Type())
ospfNewCfgHostIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgHostIndex.setStatus(_A)
_OspfNewCfgHostIpAddr_Type=IpAddress
_OspfNewCfgHostIpAddr_Object=MibTableColumn
ospfNewCfgHostIpAddr=_OspfNewCfgHostIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,13,13,1,2),_OspfNewCfgHostIpAddr_Type())
ospfNewCfgHostIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgHostIpAddr.setStatus(_A)
_OspfNewCfgHostAreaIndex_Type=Integer32
_OspfNewCfgHostAreaIndex_Object=MibTableColumn
ospfNewCfgHostAreaIndex=_OspfNewCfgHostAreaIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,13,1,3),_OspfNewCfgHostAreaIndex_Type())
ospfNewCfgHostAreaIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgHostAreaIndex.setStatus(_A)
class _OspfNewCfgHostCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfNewCfgHostCost_Type.__name__=_C
_OspfNewCfgHostCost_Object=MibTableColumn
ospfNewCfgHostCost=_OspfNewCfgHostCost_Object((1,3,6,1,4,1,1872,2,5,3,1,13,13,1,4),_OspfNewCfgHostCost_Type())
ospfNewCfgHostCost.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgHostCost.setStatus(_A)
class _OspfNewCfgHostState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfNewCfgHostState_Type.__name__=_C
_OspfNewCfgHostState_Object=MibTableColumn
ospfNewCfgHostState=_OspfNewCfgHostState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,13,1,5),_OspfNewCfgHostState_Type())
ospfNewCfgHostState.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgHostState.setStatus(_A)
class _OspfNewCfgHostDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_OspfNewCfgHostDelete_Type.__name__=_C
_OspfNewCfgHostDelete_Object=MibTableColumn
ospfNewCfgHostDelete=_OspfNewCfgHostDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,13,13,1,6),_OspfNewCfgHostDelete_Type())
ospfNewCfgHostDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgHostDelete.setStatus(_A)
_OspfCurCfgRangeTable_Object=MibTable
ospfCurCfgRangeTable=_OspfCurCfgRangeTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,14))
if mibBuilder.loadTexts:ospfCurCfgRangeTable.setStatus(_A)
_OspfCurCfgRangeEntry_Object=MibTableRow
ospfCurCfgRangeEntry=_OspfCurCfgRangeEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,14,1))
ospfCurCfgRangeEntry.setIndexNames((0,_G,_Ad))
if mibBuilder.loadTexts:ospfCurCfgRangeEntry.setStatus(_A)
_OspfCurCfgRangeIndex_Type=Integer32
_OspfCurCfgRangeIndex_Object=MibTableColumn
ospfCurCfgRangeIndex=_OspfCurCfgRangeIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,14,1,1),_OspfCurCfgRangeIndex_Type())
ospfCurCfgRangeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgRangeIndex.setStatus(_A)
_OspfCurCfgRangeAddr_Type=IpAddress
_OspfCurCfgRangeAddr_Object=MibTableColumn
ospfCurCfgRangeAddr=_OspfCurCfgRangeAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,13,14,1,2),_OspfCurCfgRangeAddr_Type())
ospfCurCfgRangeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgRangeAddr.setStatus(_A)
_OspfCurCfgRangeMask_Type=IpAddress
_OspfCurCfgRangeMask_Object=MibTableColumn
ospfCurCfgRangeMask=_OspfCurCfgRangeMask_Object((1,3,6,1,4,1,1872,2,5,3,1,13,14,1,3),_OspfCurCfgRangeMask_Type())
ospfCurCfgRangeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgRangeMask.setStatus(_A)
_OspfCurCfgRangeAreaIndex_Type=Integer32
_OspfCurCfgRangeAreaIndex_Object=MibTableColumn
ospfCurCfgRangeAreaIndex=_OspfCurCfgRangeAreaIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,14,1,4),_OspfCurCfgRangeAreaIndex_Type())
ospfCurCfgRangeAreaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgRangeAreaIndex.setStatus(_A)
class _OspfCurCfgRangeHideState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfCurCfgRangeHideState_Type.__name__=_C
_OspfCurCfgRangeHideState_Object=MibTableColumn
ospfCurCfgRangeHideState=_OspfCurCfgRangeHideState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,14,1,5),_OspfCurCfgRangeHideState_Type())
ospfCurCfgRangeHideState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgRangeHideState.setStatus(_A)
class _OspfCurCfgRangeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfCurCfgRangeState_Type.__name__=_C
_OspfCurCfgRangeState_Object=MibTableColumn
ospfCurCfgRangeState=_OspfCurCfgRangeState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,14,1,6),_OspfCurCfgRangeState_Type())
ospfCurCfgRangeState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgRangeState.setStatus(_A)
_OspfNewCfgRangeTable_Object=MibTable
ospfNewCfgRangeTable=_OspfNewCfgRangeTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,15))
if mibBuilder.loadTexts:ospfNewCfgRangeTable.setStatus(_A)
_OspfNewCfgRangeEntry_Object=MibTableRow
ospfNewCfgRangeEntry=_OspfNewCfgRangeEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,15,1))
ospfNewCfgRangeEntry.setIndexNames((0,_G,_Ae))
if mibBuilder.loadTexts:ospfNewCfgRangeEntry.setStatus(_A)
_OspfNewCfgRangeIndex_Type=Integer32
_OspfNewCfgRangeIndex_Object=MibTableColumn
ospfNewCfgRangeIndex=_OspfNewCfgRangeIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,15,1,1),_OspfNewCfgRangeIndex_Type())
ospfNewCfgRangeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgRangeIndex.setStatus(_A)
_OspfNewCfgRangeAddr_Type=IpAddress
_OspfNewCfgRangeAddr_Object=MibTableColumn
ospfNewCfgRangeAddr=_OspfNewCfgRangeAddr_Object((1,3,6,1,4,1,1872,2,5,3,1,13,15,1,2),_OspfNewCfgRangeAddr_Type())
ospfNewCfgRangeAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgRangeAddr.setStatus(_A)
_OspfNewCfgRangeMask_Type=IpAddress
_OspfNewCfgRangeMask_Object=MibTableColumn
ospfNewCfgRangeMask=_OspfNewCfgRangeMask_Object((1,3,6,1,4,1,1872,2,5,3,1,13,15,1,3),_OspfNewCfgRangeMask_Type())
ospfNewCfgRangeMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgRangeMask.setStatus(_A)
_OspfNewCfgRangeAreaIndex_Type=Integer32
_OspfNewCfgRangeAreaIndex_Object=MibTableColumn
ospfNewCfgRangeAreaIndex=_OspfNewCfgRangeAreaIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,15,1,4),_OspfNewCfgRangeAreaIndex_Type())
ospfNewCfgRangeAreaIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgRangeAreaIndex.setStatus(_A)
class _OspfNewCfgRangeHideState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfNewCfgRangeHideState_Type.__name__=_C
_OspfNewCfgRangeHideState_Object=MibTableColumn
ospfNewCfgRangeHideState=_OspfNewCfgRangeHideState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,15,1,5),_OspfNewCfgRangeHideState_Type())
ospfNewCfgRangeHideState.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgRangeHideState.setStatus(_A)
class _OspfNewCfgRangeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfNewCfgRangeState_Type.__name__=_C
_OspfNewCfgRangeState_Object=MibTableColumn
ospfNewCfgRangeState=_OspfNewCfgRangeState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,15,1,6),_OspfNewCfgRangeState_Type())
ospfNewCfgRangeState.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgRangeState.setStatus(_A)
class _OspfNewCfgRangeDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_OspfNewCfgRangeDelete_Type.__name__=_C
_OspfNewCfgRangeDelete_Object=MibTableColumn
ospfNewCfgRangeDelete=_OspfNewCfgRangeDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,13,15,1,7),_OspfNewCfgRangeDelete_Type())
ospfNewCfgRangeDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgRangeDelete.setStatus(_A)
_OspfNewCfgVisionAreaTable_Object=MibTable
ospfNewCfgVisionAreaTable=_OspfNewCfgVisionAreaTable_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16))
if mibBuilder.loadTexts:ospfNewCfgVisionAreaTable.setStatus(_A)
_OspfNewCfgVisionAreaEntry_Object=MibTableRow
ospfNewCfgVisionAreaEntry=_OspfNewCfgVisionAreaEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16,1))
ospfNewCfgVisionAreaEntry.setIndexNames((0,_G,_Af))
if mibBuilder.loadTexts:ospfNewCfgVisionAreaEntry.setStatus(_A)
_OspfNewCfgVisionAreaIndex_Type=Integer32
_OspfNewCfgVisionAreaIndex_Object=MibTableColumn
ospfNewCfgVisionAreaIndex=_OspfNewCfgVisionAreaIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16,1,1),_OspfNewCfgVisionAreaIndex_Type())
ospfNewCfgVisionAreaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgVisionAreaIndex.setStatus(_A)
_OspfNewCfgVisionAreaId_Type=IpAddress
_OspfNewCfgVisionAreaId_Object=MibTableColumn
ospfNewCfgVisionAreaId=_OspfNewCfgVisionAreaId_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16,1,2),_OspfNewCfgVisionAreaId_Type())
ospfNewCfgVisionAreaId.setMaxAccess(_H)
if mibBuilder.loadTexts:ospfNewCfgVisionAreaId.setStatus(_A)
class _OspfNewCfgVisionAreaSpfInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfNewCfgVisionAreaSpfInterval_Type.__name__=_C
_OspfNewCfgVisionAreaSpfInterval_Object=MibTableColumn
ospfNewCfgVisionAreaSpfInterval=_OspfNewCfgVisionAreaSpfInterval_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16,1,3),_OspfNewCfgVisionAreaSpfInterval_Type())
ospfNewCfgVisionAreaSpfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVisionAreaSpfInterval.setStatus(_A)
class _OspfNewCfgVisionAreaAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_U,2),(_d,3)))
_OspfNewCfgVisionAreaAuthType_Type.__name__=_C
_OspfNewCfgVisionAreaAuthType_Object=MibTableColumn
ospfNewCfgVisionAreaAuthType=_OspfNewCfgVisionAreaAuthType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16,1,4),_OspfNewCfgVisionAreaAuthType_Type())
ospfNewCfgVisionAreaAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVisionAreaAuthType.setStatus(_A)
class _OspfNewCfgVisionAreaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3)))
_OspfNewCfgVisionAreaType_Type.__name__=_C
_OspfNewCfgVisionAreaType_Object=MibTableColumn
ospfNewCfgVisionAreaType=_OspfNewCfgVisionAreaType_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16,1,5),_OspfNewCfgVisionAreaType_Type())
ospfNewCfgVisionAreaType.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVisionAreaType.setStatus(_A)
class _OspfNewCfgVisionAreaMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfNewCfgVisionAreaMetric_Type.__name__=_C
_OspfNewCfgVisionAreaMetric_Object=MibTableColumn
ospfNewCfgVisionAreaMetric=_OspfNewCfgVisionAreaMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16,1,6),_OspfNewCfgVisionAreaMetric_Type())
ospfNewCfgVisionAreaMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVisionAreaMetric.setStatus(_A)
class _OspfNewCfgVisionAreaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_OspfNewCfgVisionAreaState_Type.__name__=_C
_OspfNewCfgVisionAreaState_Object=MibTableColumn
ospfNewCfgVisionAreaState=_OspfNewCfgVisionAreaState_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16,1,7),_OspfNewCfgVisionAreaState_Type())
ospfNewCfgVisionAreaState.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVisionAreaState.setStatus(_A)
class _OspfNewCfgVisionAreaDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_OspfNewCfgVisionAreaDelete_Type.__name__=_C
_OspfNewCfgVisionAreaDelete_Object=MibTableColumn
ospfNewCfgVisionAreaDelete=_OspfNewCfgVisionAreaDelete_Object((1,3,6,1,4,1,1872,2,5,3,1,13,16,1,8),_OspfNewCfgVisionAreaDelete_Type())
ospfNewCfgVisionAreaDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgVisionAreaDelete.setStatus(_A)
_IpGeneralCfg_ObjectIdentity=ObjectIdentity
ipGeneralCfg=_IpGeneralCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,14))
_IpCurCfgRouterID_Type=IpAddress
_IpCurCfgRouterID_Object=MibScalar
ipCurCfgRouterID=_IpCurCfgRouterID_Object((1,3,6,1,4,1,1872,2,5,3,1,14,1),_IpCurCfgRouterID_Type())
ipCurCfgRouterID.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgRouterID.setStatus(_A)
_IpNewCfgRouterID_Type=IpAddress
_IpNewCfgRouterID_Object=MibScalar
ipNewCfgRouterID=_IpNewCfgRouterID_Object((1,3,6,1,4,1,1872,2,5,3,1,14,2),_IpNewCfgRouterID_Type())
ipNewCfgRouterID.setMaxAccess(_H)
if mibBuilder.loadTexts:ipNewCfgRouterID.setStatus(_A)
class _IpCurCfgASNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpCurCfgASNumber_Type.__name__=_C
_IpCurCfgASNumber_Object=MibScalar
ipCurCfgASNumber=_IpCurCfgASNumber_Object((1,3,6,1,4,1,1872,2,5,3,1,14,3),_IpCurCfgASNumber_Type())
ipCurCfgASNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgASNumber.setStatus(_A)
class _IpNewCfgASNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpNewCfgASNumber_Type.__name__=_C
_IpNewCfgASNumber_Object=MibScalar
ipNewCfgASNumber=_IpNewCfgASNumber_Object((1,3,6,1,4,1,1872,2,5,3,1,14,4),_IpNewCfgASNumber_Type())
ipNewCfgASNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:ipNewCfgASNumber.setStatus(_A)
_IpStaticArpCfg_ObjectIdentity=ObjectIdentity
ipStaticArpCfg=_IpStaticArpCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,15))
_IpStaticArpTableMaxSize_Type=Integer32
_IpStaticArpTableMaxSize_Object=MibScalar
ipStaticArpTableMaxSize=_IpStaticArpTableMaxSize_Object((1,3,6,1,4,1,1872,2,5,3,1,15,1),_IpStaticArpTableMaxSize_Type())
ipStaticArpTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ipStaticArpTableMaxSize.setStatus(_A)
_IpCurCfgStaticArpTable_Object=MibTable
ipCurCfgStaticArpTable=_IpCurCfgStaticArpTable_Object((1,3,6,1,4,1,1872,2,5,3,1,15,2))
if mibBuilder.loadTexts:ipCurCfgStaticArpTable.setStatus(_A)
_IpCurCfgStaticArpEntry_Object=MibTableRow
ipCurCfgStaticArpEntry=_IpCurCfgStaticArpEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,15,2,1))
ipCurCfgStaticArpEntry.setIndexNames((0,_G,_Ag))
if mibBuilder.loadTexts:ipCurCfgStaticArpEntry.setStatus(_A)
_IpCurCfgStaticArpIndx_Type=Integer32
_IpCurCfgStaticArpIndx_Object=MibTableColumn
ipCurCfgStaticArpIndx=_IpCurCfgStaticArpIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,15,2,1,1),_IpCurCfgStaticArpIndx_Type())
ipCurCfgStaticArpIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticArpIndx.setStatus(_A)
_IpCurCfgStaticArpIp_Type=IpAddress
_IpCurCfgStaticArpIp_Object=MibTableColumn
ipCurCfgStaticArpIp=_IpCurCfgStaticArpIp_Object((1,3,6,1,4,1,1872,2,5,3,1,15,2,1,2),_IpCurCfgStaticArpIp_Type())
ipCurCfgStaticArpIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticArpIp.setStatus(_A)
_IpCurCfgStaticArpMAC_Type=PhysAddress
_IpCurCfgStaticArpMAC_Object=MibTableColumn
ipCurCfgStaticArpMAC=_IpCurCfgStaticArpMAC_Object((1,3,6,1,4,1,1872,2,5,3,1,15,2,1,3),_IpCurCfgStaticArpMAC_Type())
ipCurCfgStaticArpMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticArpMAC.setStatus(_A)
_IpCurCfgStaticArpVlan_Type=Integer32
_IpCurCfgStaticArpVlan_Object=MibTableColumn
ipCurCfgStaticArpVlan=_IpCurCfgStaticArpVlan_Object((1,3,6,1,4,1,1872,2,5,3,1,15,2,1,4),_IpCurCfgStaticArpVlan_Type())
ipCurCfgStaticArpVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticArpVlan.setStatus(_A)
_IpCurCfgStaticArpPort_Type=Integer32
_IpCurCfgStaticArpPort_Object=MibTableColumn
ipCurCfgStaticArpPort=_IpCurCfgStaticArpPort_Object((1,3,6,1,4,1,1872,2,5,3,1,15,2,1,5),_IpCurCfgStaticArpPort_Type())
ipCurCfgStaticArpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticArpPort.setStatus(_A)
_IpNewCfgStaticArpTable_Object=MibTable
ipNewCfgStaticArpTable=_IpNewCfgStaticArpTable_Object((1,3,6,1,4,1,1872,2,5,3,1,15,3))
if mibBuilder.loadTexts:ipNewCfgStaticArpTable.setStatus(_A)
_IpNewCfgStaticArpEntry_Object=MibTableRow
ipNewCfgStaticArpEntry=_IpNewCfgStaticArpEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,15,3,1))
ipNewCfgStaticArpEntry.setIndexNames((0,_G,_Ah))
if mibBuilder.loadTexts:ipNewCfgStaticArpEntry.setStatus(_A)
_IpNewCfgStaticArpIndx_Type=Integer32
_IpNewCfgStaticArpIndx_Object=MibTableColumn
ipNewCfgStaticArpIndx=_IpNewCfgStaticArpIndx_Object((1,3,6,1,4,1,1872,2,5,3,1,15,3,1,1),_IpNewCfgStaticArpIndx_Type())
ipNewCfgStaticArpIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgStaticArpIndx.setStatus(_A)
_IpNewCfgStaticArpIp_Type=IpAddress
_IpNewCfgStaticArpIp_Object=MibTableColumn
ipNewCfgStaticArpIp=_IpNewCfgStaticArpIp_Object((1,3,6,1,4,1,1872,2,5,3,1,15,3,1,2),_IpNewCfgStaticArpIp_Type())
ipNewCfgStaticArpIp.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticArpIp.setStatus(_A)
_IpNewCfgStaticArpMAC_Type=PhysAddress
_IpNewCfgStaticArpMAC_Object=MibTableColumn
ipNewCfgStaticArpMAC=_IpNewCfgStaticArpMAC_Object((1,3,6,1,4,1,1872,2,5,3,1,15,3,1,3),_IpNewCfgStaticArpMAC_Type())
ipNewCfgStaticArpMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticArpMAC.setStatus(_A)
_IpNewCfgStaticArpVlan_Type=Integer32
_IpNewCfgStaticArpVlan_Object=MibTableColumn
ipNewCfgStaticArpVlan=_IpNewCfgStaticArpVlan_Object((1,3,6,1,4,1,1872,2,5,3,1,15,3,1,4),_IpNewCfgStaticArpVlan_Type())
ipNewCfgStaticArpVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticArpVlan.setStatus(_A)
_IpNewCfgStaticArpPort_Type=Integer32
_IpNewCfgStaticArpPort_Object=MibTableColumn
ipNewCfgStaticArpPort=_IpNewCfgStaticArpPort_Object((1,3,6,1,4,1,1872,2,5,3,1,15,3,1,5),_IpNewCfgStaticArpPort_Type())
ipNewCfgStaticArpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticArpPort.setStatus(_A)
class _IpNewCfgStaticArpAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_IpNewCfgStaticArpAction_Type.__name__=_C
_IpNewCfgStaticArpAction_Object=MibTableColumn
ipNewCfgStaticArpAction=_IpNewCfgStaticArpAction_Object((1,3,6,1,4,1,1872,2,5,3,1,15,3,1,6),_IpNewCfgStaticArpAction_Type())
ipNewCfgStaticArpAction.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticArpAction.setStatus(_A)
_IpStaticArpTableNextAvailableIndex_Type=Integer32
_IpStaticArpTableNextAvailableIndex_Object=MibScalar
ipStaticArpTableNextAvailableIndex=_IpStaticArpTableNextAvailableIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,15,4),_IpStaticArpTableNextAvailableIndex_Type())
ipStaticArpTableNextAvailableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipStaticArpTableNextAvailableIndex.setStatus(_A)
_Rip2Cfg_ObjectIdentity=ObjectIdentity
rip2Cfg=_Rip2Cfg_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,18))
_RipCurCfgIntfTable_Object=MibTable
ripCurCfgIntfTable=_RipCurCfgIntfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1))
if mibBuilder.loadTexts:ripCurCfgIntfTable.setStatus(_A)
_RipCurCfgIntfEntry_Object=MibTableRow
ripCurCfgIntfEntry=_RipCurCfgIntfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1))
ripCurCfgIntfEntry.setIndexNames((0,_G,_Ai))
if mibBuilder.loadTexts:ripCurCfgIntfEntry.setStatus(_A)
_RipCurCfgIntfIndex_Type=Integer32
_RipCurCfgIntfIndex_Object=MibTableColumn
ripCurCfgIntfIndex=_RipCurCfgIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,1),_RipCurCfgIntfIndex_Type())
ripCurCfgIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfIndex.setStatus(_A)
class _RipCurCfgIntfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),(_i,2),(_W,3)))
_RipCurCfgIntfVersion_Type.__name__=_C
_RipCurCfgIntfVersion_Object=MibTableColumn
ripCurCfgIntfVersion=_RipCurCfgIntfVersion_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,2),_RipCurCfgIntfVersion_Type())
ripCurCfgIntfVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfVersion.setStatus(_A)
class _RipCurCfgIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipCurCfgIntfState_Type.__name__=_C
_RipCurCfgIntfState_Object=MibTableColumn
ripCurCfgIntfState=_RipCurCfgIntfState_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,3),_RipCurCfgIntfState_Type())
ripCurCfgIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfState.setStatus(_A)
class _RipCurCfgIntfListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipCurCfgIntfListen_Type.__name__=_C
_RipCurCfgIntfListen_Object=MibTableColumn
ripCurCfgIntfListen=_RipCurCfgIntfListen_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,4),_RipCurCfgIntfListen_Type())
ripCurCfgIntfListen.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfListen.setStatus(_A)
class _RipCurCfgIntfDefListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipCurCfgIntfDefListen_Type.__name__=_C
_RipCurCfgIntfDefListen_Object=MibTableColumn
ripCurCfgIntfDefListen=_RipCurCfgIntfDefListen_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,5),_RipCurCfgIntfDefListen_Type())
ripCurCfgIntfDefListen.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfDefListen.setStatus(_X)
class _RipCurCfgIntfTrigUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipCurCfgIntfTrigUpdate_Type.__name__=_C
_RipCurCfgIntfTrigUpdate_Object=MibTableColumn
ripCurCfgIntfTrigUpdate=_RipCurCfgIntfTrigUpdate_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,6),_RipCurCfgIntfTrigUpdate_Type())
ripCurCfgIntfTrigUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfTrigUpdate.setStatus(_A)
class _RipCurCfgIntfMcastUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipCurCfgIntfMcastUpdate_Type.__name__=_C
_RipCurCfgIntfMcastUpdate_Object=MibTableColumn
ripCurCfgIntfMcastUpdate=_RipCurCfgIntfMcastUpdate_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,7),_RipCurCfgIntfMcastUpdate_Type())
ripCurCfgIntfMcastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfMcastUpdate.setStatus(_A)
class _RipCurCfgIntfPoisonReverse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipCurCfgIntfPoisonReverse_Type.__name__=_C
_RipCurCfgIntfPoisonReverse_Object=MibTableColumn
ripCurCfgIntfPoisonReverse=_RipCurCfgIntfPoisonReverse_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,8),_RipCurCfgIntfPoisonReverse_Type())
ripCurCfgIntfPoisonReverse.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfPoisonReverse.setStatus(_A)
class _RipCurCfgIntfSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipCurCfgIntfSupply_Type.__name__=_C
_RipCurCfgIntfSupply_Object=MibTableColumn
ripCurCfgIntfSupply=_RipCurCfgIntfSupply_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,9),_RipCurCfgIntfSupply_Type())
ripCurCfgIntfSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfSupply.setStatus(_A)
class _RipCurCfgIntfMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_RipCurCfgIntfMetric_Type.__name__=_C
_RipCurCfgIntfMetric_Object=MibTableColumn
ripCurCfgIntfMetric=_RipCurCfgIntfMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,10),_RipCurCfgIntfMetric_Type())
ripCurCfgIntfMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfMetric.setStatus(_A)
class _RipCurCfgIntfAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_U,2)))
_RipCurCfgIntfAuth_Type.__name__=_C
_RipCurCfgIntfAuth_Object=MibTableColumn
ripCurCfgIntfAuth=_RipCurCfgIntfAuth_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,11),_RipCurCfgIntfAuth_Type())
ripCurCfgIntfAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfAuth.setStatus(_A)
class _RipCurCfgIntfKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RipCurCfgIntfKey_Type.__name__=_I
_RipCurCfgIntfKey_Object=MibTableColumn
ripCurCfgIntfKey=_RipCurCfgIntfKey_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,12),_RipCurCfgIntfKey_Type())
ripCurCfgIntfKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfKey.setStatus(_A)
class _RipCurCfgIntfDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_j,2),(_k,3),(_J,4)))
_RipCurCfgIntfDefault_Type.__name__=_C
_RipCurCfgIntfDefault_Object=MibTableColumn
ripCurCfgIntfDefault=_RipCurCfgIntfDefault_Object((1,3,6,1,4,1,1872,2,5,3,1,18,1,1,13),_RipCurCfgIntfDefault_Type())
ripCurCfgIntfDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgIntfDefault.setStatus(_A)
_RipNewCfgIntfTable_Object=MibTable
ripNewCfgIntfTable=_RipNewCfgIntfTable_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2))
if mibBuilder.loadTexts:ripNewCfgIntfTable.setStatus(_A)
_RipNewCfgIntfEntry_Object=MibTableRow
ripNewCfgIntfEntry=_RipNewCfgIntfEntry_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1))
ripNewCfgIntfEntry.setIndexNames((0,_G,_Aj))
if mibBuilder.loadTexts:ripNewCfgIntfEntry.setStatus(_A)
_RipNewCfgIntfIndex_Type=Integer32
_RipNewCfgIntfIndex_Object=MibTableColumn
ripNewCfgIntfIndex=_RipNewCfgIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,1),_RipNewCfgIntfIndex_Type())
ripNewCfgIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ripNewCfgIntfIndex.setStatus(_A)
class _RipNewCfgIntfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),(_i,2),(_W,3)))
_RipNewCfgIntfVersion_Type.__name__=_C
_RipNewCfgIntfVersion_Object=MibTableColumn
ripNewCfgIntfVersion=_RipNewCfgIntfVersion_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,2),_RipNewCfgIntfVersion_Type())
ripNewCfgIntfVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfVersion.setStatus(_A)
class _RipNewCfgIntfSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipNewCfgIntfSupply_Type.__name__=_C
_RipNewCfgIntfSupply_Object=MibTableColumn
ripNewCfgIntfSupply=_RipNewCfgIntfSupply_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,3),_RipNewCfgIntfSupply_Type())
ripNewCfgIntfSupply.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfSupply.setStatus(_A)
class _RipNewCfgIntfListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipNewCfgIntfListen_Type.__name__=_C
_RipNewCfgIntfListen_Object=MibTableColumn
ripNewCfgIntfListen=_RipNewCfgIntfListen_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,4),_RipNewCfgIntfListen_Type())
ripNewCfgIntfListen.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfListen.setStatus(_A)
class _RipNewCfgIntfDefListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipNewCfgIntfDefListen_Type.__name__=_C
_RipNewCfgIntfDefListen_Object=MibTableColumn
ripNewCfgIntfDefListen=_RipNewCfgIntfDefListen_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,5),_RipNewCfgIntfDefListen_Type())
ripNewCfgIntfDefListen.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfDefListen.setStatus(_X)
class _RipNewCfgIntfTrigUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipNewCfgIntfTrigUpdate_Type.__name__=_C
_RipNewCfgIntfTrigUpdate_Object=MibTableColumn
ripNewCfgIntfTrigUpdate=_RipNewCfgIntfTrigUpdate_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,6),_RipNewCfgIntfTrigUpdate_Type())
ripNewCfgIntfTrigUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfTrigUpdate.setStatus(_A)
class _RipNewCfgIntfMcastUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipNewCfgIntfMcastUpdate_Type.__name__=_C
_RipNewCfgIntfMcastUpdate_Object=MibTableColumn
ripNewCfgIntfMcastUpdate=_RipNewCfgIntfMcastUpdate_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,7),_RipNewCfgIntfMcastUpdate_Type())
ripNewCfgIntfMcastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfMcastUpdate.setStatus(_A)
class _RipNewCfgIntfPoisonReverse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipNewCfgIntfPoisonReverse_Type.__name__=_C
_RipNewCfgIntfPoisonReverse_Object=MibTableColumn
ripNewCfgIntfPoisonReverse=_RipNewCfgIntfPoisonReverse_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,8),_RipNewCfgIntfPoisonReverse_Type())
ripNewCfgIntfPoisonReverse.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfPoisonReverse.setStatus(_A)
class _RipNewCfgIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipNewCfgIntfState_Type.__name__=_C
_RipNewCfgIntfState_Object=MibTableColumn
ripNewCfgIntfState=_RipNewCfgIntfState_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,9),_RipNewCfgIntfState_Type())
ripNewCfgIntfState.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfState.setStatus(_A)
class _RipNewCfgIntfMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_RipNewCfgIntfMetric_Type.__name__=_C
_RipNewCfgIntfMetric_Object=MibTableColumn
ripNewCfgIntfMetric=_RipNewCfgIntfMetric_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,10),_RipNewCfgIntfMetric_Type())
ripNewCfgIntfMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:ripNewCfgIntfMetric.setStatus(_A)
class _RipNewCfgIntfAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_U,2)))
_RipNewCfgIntfAuth_Type.__name__=_C
_RipNewCfgIntfAuth_Object=MibTableColumn
ripNewCfgIntfAuth=_RipNewCfgIntfAuth_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,11),_RipNewCfgIntfAuth_Type())
ripNewCfgIntfAuth.setMaxAccess(_H)
if mibBuilder.loadTexts:ripNewCfgIntfAuth.setStatus(_A)
class _RipNewCfgIntfKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RipNewCfgIntfKey_Type.__name__=_I
_RipNewCfgIntfKey_Object=MibTableColumn
ripNewCfgIntfKey=_RipNewCfgIntfKey_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,12),_RipNewCfgIntfKey_Type())
ripNewCfgIntfKey.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfKey.setStatus(_A)
class _RipNewCfgIntfDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_j,2),(_k,3),(_J,4)))
_RipNewCfgIntfDefault_Type.__name__=_C
_RipNewCfgIntfDefault_Object=MibTableColumn
ripNewCfgIntfDefault=_RipNewCfgIntfDefault_Object((1,3,6,1,4,1,1872,2,5,3,1,18,2,1,13),_RipNewCfgIntfDefault_Type())
ripNewCfgIntfDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgIntfDefault.setStatus(_A)
_RipGeneral_ObjectIdentity=ObjectIdentity
ripGeneral=_RipGeneral_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,1,18,3))
class _Rip2CurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_Rip2CurCfgState_Type.__name__=_C
_Rip2CurCfgState_Object=MibScalar
rip2CurCfgState=_Rip2CurCfgState_Object((1,3,6,1,4,1,1872,2,5,3,1,18,3,1),_Rip2CurCfgState_Type())
rip2CurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2CurCfgState.setStatus(_A)
class _Rip2NewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_Rip2NewCfgState_Type.__name__=_C
_Rip2NewCfgState_Object=MibScalar
rip2NewCfgState=_Rip2NewCfgState_Object((1,3,6,1,4,1,1872,2,5,3,1,18,3,2),_Rip2NewCfgState_Type())
rip2NewCfgState.setMaxAccess(_H)
if mibBuilder.loadTexts:rip2NewCfgState.setStatus(_A)
class _Rip2CurCfgUpdatePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_Rip2CurCfgUpdatePeriod_Type.__name__=_C
_Rip2CurCfgUpdatePeriod_Object=MibScalar
rip2CurCfgUpdatePeriod=_Rip2CurCfgUpdatePeriod_Object((1,3,6,1,4,1,1872,2,5,3,1,18,3,3),_Rip2CurCfgUpdatePeriod_Type())
rip2CurCfgUpdatePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2CurCfgUpdatePeriod.setStatus(_A)
class _Rip2NewCfgUpdatePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_Rip2NewCfgUpdatePeriod_Type.__name__=_C
_Rip2NewCfgUpdatePeriod_Object=MibScalar
rip2NewCfgUpdatePeriod=_Rip2NewCfgUpdatePeriod_Object((1,3,6,1,4,1,1872,2,5,3,1,18,3,4),_Rip2NewCfgUpdatePeriod_Type())
rip2NewCfgUpdatePeriod.setMaxAccess(_H)
if mibBuilder.loadTexts:rip2NewCfgUpdatePeriod.setStatus(_A)
class _Rip2CurCfgVip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_Rip2CurCfgVip_Type.__name__=_C
_Rip2CurCfgVip_Object=MibScalar
rip2CurCfgVip=_Rip2CurCfgVip_Object((1,3,6,1,4,1,1872,2,5,3,1,18,3,5),_Rip2CurCfgVip_Type())
rip2CurCfgVip.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2CurCfgVip.setStatus(_A)
class _Rip2NewCfgVip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_Rip2NewCfgVip_Type.__name__=_C
_Rip2NewCfgVip_Object=MibScalar
rip2NewCfgVip=_Rip2NewCfgVip_Object((1,3,6,1,4,1,1872,2,5,3,1,18,3,6),_Rip2NewCfgVip_Type())
rip2NewCfgVip.setMaxAccess(_H)
if mibBuilder.loadTexts:rip2NewCfgVip.setStatus(_A)
class _Rip2CurCfgStaticSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_Rip2CurCfgStaticSupply_Type.__name__=_C
_Rip2CurCfgStaticSupply_Object=MibScalar
rip2CurCfgStaticSupply=_Rip2CurCfgStaticSupply_Object((1,3,6,1,4,1,1872,2,5,3,1,18,3,7),_Rip2CurCfgStaticSupply_Type())
rip2CurCfgStaticSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2CurCfgStaticSupply.setStatus(_A)
class _Rip2NewCfgStaticSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_Rip2NewCfgStaticSupply_Type.__name__=_C
_Rip2NewCfgStaticSupply_Object=MibScalar
rip2NewCfgStaticSupply=_Rip2NewCfgStaticSupply_Object((1,3,6,1,4,1,1872,2,5,3,1,18,3,8),_Rip2NewCfgStaticSupply_Type())
rip2NewCfgStaticSupply.setMaxAccess(_H)
if mibBuilder.loadTexts:rip2NewCfgStaticSupply.setStatus(_A)
_Layer3Stats_ObjectIdentity=ObjectIdentity
layer3Stats=_Layer3Stats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2))
_ArpStats_ObjectIdentity=ObjectIdentity
arpStats=_ArpStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,2))
_ArpStatEntries_Type=Gauge32
_ArpStatEntries_Object=MibScalar
arpStatEntries=_ArpStatEntries_Object((1,3,6,1,4,1,1872,2,5,3,2,2,1),_ArpStatEntries_Type())
arpStatEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:arpStatEntries.setStatus(_A)
_ArpStatHighWater_Type=Gauge32
_ArpStatHighWater_Object=MibScalar
arpStatHighWater=_ArpStatHighWater_Object((1,3,6,1,4,1,1872,2,5,3,2,2,2),_ArpStatHighWater_Type())
arpStatHighWater.setMaxAccess(_B)
if mibBuilder.loadTexts:arpStatHighWater.setStatus(_A)
_ArpStatMaxEntries_Type=Gauge32
_ArpStatMaxEntries_Object=MibScalar
arpStatMaxEntries=_ArpStatMaxEntries_Object((1,3,6,1,4,1,1872,2,5,3,2,2,3),_ArpStatMaxEntries_Type())
arpStatMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:arpStatMaxEntries.setStatus(_A)
_RouteStats_ObjectIdentity=ObjectIdentity
routeStats=_RouteStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,3))
_RouteStatEntries_Type=Gauge32
_RouteStatEntries_Object=MibScalar
routeStatEntries=_RouteStatEntries_Object((1,3,6,1,4,1,1872,2,5,3,2,3,1),_RouteStatEntries_Type())
routeStatEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:routeStatEntries.setStatus(_A)
_RouteStatHighWater_Type=Gauge32
_RouteStatHighWater_Object=MibScalar
routeStatHighWater=_RouteStatHighWater_Object((1,3,6,1,4,1,1872,2,5,3,2,3,2),_RouteStatHighWater_Type())
routeStatHighWater.setMaxAccess(_B)
if mibBuilder.loadTexts:routeStatHighWater.setStatus(_A)
_RouteStatMaxEntries_Type=Gauge32
_RouteStatMaxEntries_Object=MibScalar
routeStatMaxEntries=_RouteStatMaxEntries_Object((1,3,6,1,4,1,1872,2,5,3,2,3,3),_RouteStatMaxEntries_Type())
routeStatMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:routeStatMaxEntries.setStatus(_A)
_DnsStats_ObjectIdentity=ObjectIdentity
dnsStats=_DnsStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,4))
_DnsStatInGoodDnsRequests_Type=Counter32
_DnsStatInGoodDnsRequests_Object=MibScalar
dnsStatInGoodDnsRequests=_DnsStatInGoodDnsRequests_Object((1,3,6,1,4,1,1872,2,5,3,2,4,1),_DnsStatInGoodDnsRequests_Type())
dnsStatInGoodDnsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsStatInGoodDnsRequests.setStatus(_A)
_DnsStatInBadDnsRequests_Type=Counter32
_DnsStatInBadDnsRequests_Object=MibScalar
dnsStatInBadDnsRequests=_DnsStatInBadDnsRequests_Object((1,3,6,1,4,1,1872,2,5,3,2,4,2),_DnsStatInBadDnsRequests_Type())
dnsStatInBadDnsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsStatInBadDnsRequests.setStatus(_A)
_DnsStatOutDnsRequests_Type=Counter32
_DnsStatOutDnsRequests_Object=MibScalar
dnsStatOutDnsRequests=_DnsStatOutDnsRequests_Object((1,3,6,1,4,1,1872,2,5,3,2,4,3),_DnsStatOutDnsRequests_Type())
dnsStatOutDnsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsStatOutDnsRequests.setStatus(_A)
_VrrpStats_ObjectIdentity=ObjectIdentity
vrrpStats=_VrrpStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,5))
_VrrpStatInAdvers_Type=Counter32
_VrrpStatInAdvers_Object=MibScalar
vrrpStatInAdvers=_VrrpStatInAdvers_Object((1,3,6,1,4,1,1872,2,5,3,2,5,1),_VrrpStatInAdvers_Type())
vrrpStatInAdvers.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpStatInAdvers.setStatus(_A)
_VrrpStatOutAdvers_Type=Counter32
_VrrpStatOutAdvers_Object=MibScalar
vrrpStatOutAdvers=_VrrpStatOutAdvers_Object((1,3,6,1,4,1,1872,2,5,3,2,5,2),_VrrpStatOutAdvers_Type())
vrrpStatOutAdvers.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpStatOutAdvers.setStatus(_A)
_VrrpStatOutBadAdvers_Type=Counter32
_VrrpStatOutBadAdvers_Object=MibScalar
vrrpStatOutBadAdvers=_VrrpStatOutBadAdvers_Object((1,3,6,1,4,1,1872,2,5,3,2,5,3),_VrrpStatOutBadAdvers_Type())
vrrpStatOutBadAdvers.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpStatOutBadAdvers.setStatus(_A)
_OspfStats_ObjectIdentity=ObjectIdentity
ospfStats=_OspfStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,6))
_OspfGeneralStats_ObjectIdentity=ObjectIdentity
ospfGeneralStats=_OspfGeneralStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,6,1))
_OspfCumRxTxStats_ObjectIdentity=ObjectIdentity
ospfCumRxTxStats=_OspfCumRxTxStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,6,1,1))
_OspfCumRxPkts_Type=Counter32
_OspfCumRxPkts_Object=MibScalar
ospfCumRxPkts=_OspfCumRxPkts_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,1),_OspfCumRxPkts_Type())
ospfCumRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxPkts.setStatus(_A)
_OspfCumTxPkts_Type=Counter32
_OspfCumTxPkts_Object=MibScalar
ospfCumTxPkts=_OspfCumTxPkts_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,2),_OspfCumTxPkts_Type())
ospfCumTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxPkts.setStatus(_A)
_OspfCumRxHello_Type=Counter32
_OspfCumRxHello_Object=MibScalar
ospfCumRxHello=_OspfCumRxHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,3),_OspfCumRxHello_Type())
ospfCumRxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxHello.setStatus(_A)
_OspfCumTxHello_Type=Counter32
_OspfCumTxHello_Object=MibScalar
ospfCumTxHello=_OspfCumTxHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,4),_OspfCumTxHello_Type())
ospfCumTxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxHello.setStatus(_A)
_OspfCumRxDatabase_Type=Counter32
_OspfCumRxDatabase_Object=MibScalar
ospfCumRxDatabase=_OspfCumRxDatabase_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,5),_OspfCumRxDatabase_Type())
ospfCumRxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxDatabase.setStatus(_A)
_OspfCumTxDatabase_Type=Counter32
_OspfCumTxDatabase_Object=MibScalar
ospfCumTxDatabase=_OspfCumTxDatabase_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,6),_OspfCumTxDatabase_Type())
ospfCumTxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxDatabase.setStatus(_A)
_OspfCumRxlsReqs_Type=Counter32
_OspfCumRxlsReqs_Object=MibScalar
ospfCumRxlsReqs=_OspfCumRxlsReqs_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,7),_OspfCumRxlsReqs_Type())
ospfCumRxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxlsReqs.setStatus(_A)
_OspfCumTxlsReqs_Type=Counter32
_OspfCumTxlsReqs_Object=MibScalar
ospfCumTxlsReqs=_OspfCumTxlsReqs_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,8),_OspfCumTxlsReqs_Type())
ospfCumTxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxlsReqs.setStatus(_A)
_OspfCumRxlsAcks_Type=Counter32
_OspfCumRxlsAcks_Object=MibScalar
ospfCumRxlsAcks=_OspfCumRxlsAcks_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,9),_OspfCumRxlsAcks_Type())
ospfCumRxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxlsAcks.setStatus(_A)
_OspfCumTxlsAcks_Type=Counter32
_OspfCumTxlsAcks_Object=MibScalar
ospfCumTxlsAcks=_OspfCumTxlsAcks_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,10),_OspfCumTxlsAcks_Type())
ospfCumTxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxlsAcks.setStatus(_A)
_OspfCumRxlsUpdates_Type=Counter32
_OspfCumRxlsUpdates_Object=MibScalar
ospfCumRxlsUpdates=_OspfCumRxlsUpdates_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,11),_OspfCumRxlsUpdates_Type())
ospfCumRxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxlsUpdates.setStatus(_A)
_OspfCumTxlsUpdates_Type=Counter32
_OspfCumTxlsUpdates_Object=MibScalar
ospfCumTxlsUpdates=_OspfCumTxlsUpdates_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,1,12),_OspfCumTxlsUpdates_Type())
ospfCumTxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxlsUpdates.setStatus(_A)
_OspfCumNbrChangeStats_ObjectIdentity=ObjectIdentity
ospfCumNbrChangeStats=_OspfCumNbrChangeStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,6,1,2))
_OspfCumNbrhello_Type=Counter32
_OspfCumNbrhello_Object=MibScalar
ospfCumNbrhello=_OspfCumNbrhello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,1),_OspfCumNbrhello_Type())
ospfCumNbrhello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrhello.setStatus(_A)
_OspfCumNbrStart_Type=Counter32
_OspfCumNbrStart_Object=MibScalar
ospfCumNbrStart=_OspfCumNbrStart_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,2),_OspfCumNbrStart_Type())
ospfCumNbrStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrStart.setStatus(_A)
_OspfCumNbrAdjointOk_Type=Counter32
_OspfCumNbrAdjointOk_Object=MibScalar
ospfCumNbrAdjointOk=_OspfCumNbrAdjointOk_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,3),_OspfCumNbrAdjointOk_Type())
ospfCumNbrAdjointOk.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrAdjointOk.setStatus(_A)
_OspfCumNbrNegotiationDone_Type=Counter32
_OspfCumNbrNegotiationDone_Object=MibScalar
ospfCumNbrNegotiationDone=_OspfCumNbrNegotiationDone_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,4),_OspfCumNbrNegotiationDone_Type())
ospfCumNbrNegotiationDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrNegotiationDone.setStatus(_A)
_OspfCumNbrExchangeDone_Type=Counter32
_OspfCumNbrExchangeDone_Object=MibScalar
ospfCumNbrExchangeDone=_OspfCumNbrExchangeDone_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,5),_OspfCumNbrExchangeDone_Type())
ospfCumNbrExchangeDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrExchangeDone.setStatus(_A)
_OspfCumNbrBadRequests_Type=Counter32
_OspfCumNbrBadRequests_Object=MibScalar
ospfCumNbrBadRequests=_OspfCumNbrBadRequests_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,6),_OspfCumNbrBadRequests_Type())
ospfCumNbrBadRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrBadRequests.setStatus(_A)
_OspfCumNbrBadSequence_Type=Counter32
_OspfCumNbrBadSequence_Object=MibScalar
ospfCumNbrBadSequence=_OspfCumNbrBadSequence_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,7),_OspfCumNbrBadSequence_Type())
ospfCumNbrBadSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrBadSequence.setStatus(_A)
_OspfCumNbrLoadingDone_Type=Counter32
_OspfCumNbrLoadingDone_Object=MibScalar
ospfCumNbrLoadingDone=_OspfCumNbrLoadingDone_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,8),_OspfCumNbrLoadingDone_Type())
ospfCumNbrLoadingDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrLoadingDone.setStatus(_A)
_OspfCumNbrN1way_Type=Counter32
_OspfCumNbrN1way_Object=MibScalar
ospfCumNbrN1way=_OspfCumNbrN1way_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,9),_OspfCumNbrN1way_Type())
ospfCumNbrN1way.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrN1way.setStatus(_A)
_OspfCumNbrRstAd_Type=Counter32
_OspfCumNbrRstAd_Object=MibScalar
ospfCumNbrRstAd=_OspfCumNbrRstAd_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,10),_OspfCumNbrRstAd_Type())
ospfCumNbrRstAd.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrRstAd.setStatus(_A)
_OspfCumNbrDown_Type=Counter32
_OspfCumNbrDown_Object=MibScalar
ospfCumNbrDown=_OspfCumNbrDown_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,11),_OspfCumNbrDown_Type())
ospfCumNbrDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrDown.setStatus(_A)
_OspfCumNbrN2way_Type=Counter32
_OspfCumNbrN2way_Object=MibScalar
ospfCumNbrN2way=_OspfCumNbrN2way_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,2,12),_OspfCumNbrN2way_Type())
ospfCumNbrN2way.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrN2way.setStatus(_A)
_OspfCumIntfChangeStats_ObjectIdentity=ObjectIdentity
ospfCumIntfChangeStats=_OspfCumIntfChangeStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,6,1,3))
_OspfCumIntfHello_Type=Counter32
_OspfCumIntfHello_Object=MibScalar
ospfCumIntfHello=_OspfCumIntfHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,3,1),_OspfCumIntfHello_Type())
ospfCumIntfHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfHello.setStatus(_A)
_OspfCumIntfDown_Type=Counter32
_OspfCumIntfDown_Object=MibScalar
ospfCumIntfDown=_OspfCumIntfDown_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,3,2),_OspfCumIntfDown_Type())
ospfCumIntfDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfDown.setStatus(_A)
_OspfCumIntfLoop_Type=Counter32
_OspfCumIntfLoop_Object=MibScalar
ospfCumIntfLoop=_OspfCumIntfLoop_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,3,3),_OspfCumIntfLoop_Type())
ospfCumIntfLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfLoop.setStatus(_A)
_OspfCumIntfUnloop_Type=Counter32
_OspfCumIntfUnloop_Object=MibScalar
ospfCumIntfUnloop=_OspfCumIntfUnloop_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,3,4),_OspfCumIntfUnloop_Type())
ospfCumIntfUnloop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfUnloop.setStatus(_A)
_OspfCumIntfWaitTimer_Type=Counter32
_OspfCumIntfWaitTimer_Object=MibScalar
ospfCumIntfWaitTimer=_OspfCumIntfWaitTimer_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,3,5),_OspfCumIntfWaitTimer_Type())
ospfCumIntfWaitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfWaitTimer.setStatus(_A)
_OspfCumIntfBackup_Type=Counter32
_OspfCumIntfBackup_Object=MibScalar
ospfCumIntfBackup=_OspfCumIntfBackup_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,3,6),_OspfCumIntfBackup_Type())
ospfCumIntfBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfBackup.setStatus(_A)
_OspfCumIntfNbrChange_Type=Counter32
_OspfCumIntfNbrChange_Object=MibScalar
ospfCumIntfNbrChange=_OspfCumIntfNbrChange_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,3,7),_OspfCumIntfNbrChange_Type())
ospfCumIntfNbrChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfNbrChange.setStatus(_A)
_OspfTimersKickOffStats_ObjectIdentity=ObjectIdentity
ospfTimersKickOffStats=_OspfTimersKickOffStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,6,1,4))
_OspfTmrsKckOffHello_Type=Counter32
_OspfTmrsKckOffHello_Object=MibScalar
ospfTmrsKckOffHello=_OspfTmrsKckOffHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,4,1),_OspfTmrsKckOffHello_Type())
ospfTmrsKckOffHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffHello.setStatus(_A)
_OspfTmrsKckOffRetransmit_Type=Counter32
_OspfTmrsKckOffRetransmit_Object=MibScalar
ospfTmrsKckOffRetransmit=_OspfTmrsKckOffRetransmit_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,4,2),_OspfTmrsKckOffRetransmit_Type())
ospfTmrsKckOffRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffRetransmit.setStatus(_A)
_OspfTmrsKckOffLsaLock_Type=Counter32
_OspfTmrsKckOffLsaLock_Object=MibScalar
ospfTmrsKckOffLsaLock=_OspfTmrsKckOffLsaLock_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,4,3),_OspfTmrsKckOffLsaLock_Type())
ospfTmrsKckOffLsaLock.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffLsaLock.setStatus(_A)
_OspfTmrsKckOffLsaAck_Type=Counter32
_OspfTmrsKckOffLsaAck_Object=MibScalar
ospfTmrsKckOffLsaAck=_OspfTmrsKckOffLsaAck_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,4,4),_OspfTmrsKckOffLsaAck_Type())
ospfTmrsKckOffLsaAck.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffLsaAck.setStatus(_A)
_OspfTmrsKckOffDbage_Type=Counter32
_OspfTmrsKckOffDbage_Object=MibScalar
ospfTmrsKckOffDbage=_OspfTmrsKckOffDbage_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,4,5),_OspfTmrsKckOffDbage_Type())
ospfTmrsKckOffDbage.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffDbage.setStatus(_A)
_OspfTmrsKckOffSummary_Type=Counter32
_OspfTmrsKckOffSummary_Object=MibScalar
ospfTmrsKckOffSummary=_OspfTmrsKckOffSummary_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,4,6),_OspfTmrsKckOffSummary_Type())
ospfTmrsKckOffSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffSummary.setStatus(_A)
_OspfTmrsKckOffAseExport_Type=Counter32
_OspfTmrsKckOffAseExport_Object=MibScalar
ospfTmrsKckOffAseExport=_OspfTmrsKckOffAseExport_Object((1,3,6,1,4,1,1872,2,5,3,2,6,1,4,7),_OspfTmrsKckOffAseExport_Type())
ospfTmrsKckOffAseExport.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffAseExport.setStatus(_A)
_OspfArea_ObjectIdentity=ObjectIdentity
ospfArea=_OspfArea_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,6,2))
_OspfAreaRxTxStats_Object=MibTable
ospfAreaRxTxStats=_OspfAreaRxTxStats_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1))
if mibBuilder.loadTexts:ospfAreaRxTxStats.setStatus(_A)
_OspfAreaRxTxStatsEntry_Object=MibTableRow
ospfAreaRxTxStatsEntry=_OspfAreaRxTxStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1))
ospfAreaRxTxStatsEntry.setIndexNames((0,_G,_Ak))
if mibBuilder.loadTexts:ospfAreaRxTxStatsEntry.setStatus(_A)
_OspfAreaRxTxIndex_Type=Integer32
_OspfAreaRxTxIndex_Object=MibTableColumn
ospfAreaRxTxIndex=_OspfAreaRxTxIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,1),_OspfAreaRxTxIndex_Type())
ospfAreaRxTxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxTxIndex.setStatus(_A)
_OspfAreaRxPkts_Type=Counter32
_OspfAreaRxPkts_Object=MibTableColumn
ospfAreaRxPkts=_OspfAreaRxPkts_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,2),_OspfAreaRxPkts_Type())
ospfAreaRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxPkts.setStatus(_A)
_OspfAreaTxPkts_Type=Counter32
_OspfAreaTxPkts_Object=MibTableColumn
ospfAreaTxPkts=_OspfAreaTxPkts_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,3),_OspfAreaTxPkts_Type())
ospfAreaTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxPkts.setStatus(_A)
_OspfAreaRxHello_Type=Counter32
_OspfAreaRxHello_Object=MibTableColumn
ospfAreaRxHello=_OspfAreaRxHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,4),_OspfAreaRxHello_Type())
ospfAreaRxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxHello.setStatus(_A)
_OspfAreaTxHello_Type=Counter32
_OspfAreaTxHello_Object=MibTableColumn
ospfAreaTxHello=_OspfAreaTxHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,5),_OspfAreaTxHello_Type())
ospfAreaTxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxHello.setStatus(_A)
_OspfAreaRxDatabase_Type=Counter32
_OspfAreaRxDatabase_Object=MibTableColumn
ospfAreaRxDatabase=_OspfAreaRxDatabase_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,6),_OspfAreaRxDatabase_Type())
ospfAreaRxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxDatabase.setStatus(_A)
_OspfAreaTxDatabase_Type=Counter32
_OspfAreaTxDatabase_Object=MibTableColumn
ospfAreaTxDatabase=_OspfAreaTxDatabase_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,7),_OspfAreaTxDatabase_Type())
ospfAreaTxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxDatabase.setStatus(_A)
_OspfAreaRxlsReqs_Type=Counter32
_OspfAreaRxlsReqs_Object=MibTableColumn
ospfAreaRxlsReqs=_OspfAreaRxlsReqs_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,8),_OspfAreaRxlsReqs_Type())
ospfAreaRxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxlsReqs.setStatus(_A)
_OspfAreaTxlsReqs_Type=Counter32
_OspfAreaTxlsReqs_Object=MibTableColumn
ospfAreaTxlsReqs=_OspfAreaTxlsReqs_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,9),_OspfAreaTxlsReqs_Type())
ospfAreaTxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxlsReqs.setStatus(_A)
_OspfAreaRxlsAcks_Type=Counter32
_OspfAreaRxlsAcks_Object=MibTableColumn
ospfAreaRxlsAcks=_OspfAreaRxlsAcks_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,10),_OspfAreaRxlsAcks_Type())
ospfAreaRxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxlsAcks.setStatus(_A)
_OspfAreaTxlsAcks_Type=Counter32
_OspfAreaTxlsAcks_Object=MibTableColumn
ospfAreaTxlsAcks=_OspfAreaTxlsAcks_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,11),_OspfAreaTxlsAcks_Type())
ospfAreaTxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxlsAcks.setStatus(_A)
_OspfAreaRxlsUpdates_Type=Counter32
_OspfAreaRxlsUpdates_Object=MibTableColumn
ospfAreaRxlsUpdates=_OspfAreaRxlsUpdates_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,12),_OspfAreaRxlsUpdates_Type())
ospfAreaRxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxlsUpdates.setStatus(_A)
_OspfAreaTxlsUpdates_Type=Counter32
_OspfAreaTxlsUpdates_Object=MibTableColumn
ospfAreaTxlsUpdates=_OspfAreaTxlsUpdates_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,1,1,13),_OspfAreaTxlsUpdates_Type())
ospfAreaTxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxlsUpdates.setStatus(_A)
_OspfAreaNbrChangeStats_Object=MibTable
ospfAreaNbrChangeStats=_OspfAreaNbrChangeStats_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2))
if mibBuilder.loadTexts:ospfAreaNbrChangeStats.setStatus(_A)
_OspfAreaNbrChangeStatsEntry_Object=MibTableRow
ospfAreaNbrChangeStatsEntry=_OspfAreaNbrChangeStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1))
ospfAreaNbrChangeStatsEntry.setIndexNames((0,_G,_Al))
if mibBuilder.loadTexts:ospfAreaNbrChangeStatsEntry.setStatus(_A)
_OspfAreaNbrIndex_Type=Integer32
_OspfAreaNbrIndex_Object=MibTableColumn
ospfAreaNbrIndex=_OspfAreaNbrIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,1),_OspfAreaNbrIndex_Type())
ospfAreaNbrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrIndex.setStatus(_A)
_OspfAreaNbrhello_Type=Counter32
_OspfAreaNbrhello_Object=MibTableColumn
ospfAreaNbrhello=_OspfAreaNbrhello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,2),_OspfAreaNbrhello_Type())
ospfAreaNbrhello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrhello.setStatus(_A)
_OspfAreaNbrStart_Type=Counter32
_OspfAreaNbrStart_Object=MibTableColumn
ospfAreaNbrStart=_OspfAreaNbrStart_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,3),_OspfAreaNbrStart_Type())
ospfAreaNbrStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrStart.setStatus(_A)
_OspfAreaNbrAdjointOk_Type=Counter32
_OspfAreaNbrAdjointOk_Object=MibTableColumn
ospfAreaNbrAdjointOk=_OspfAreaNbrAdjointOk_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,4),_OspfAreaNbrAdjointOk_Type())
ospfAreaNbrAdjointOk.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrAdjointOk.setStatus(_A)
_OspfAreaNbrNegotiationDone_Type=Counter32
_OspfAreaNbrNegotiationDone_Object=MibTableColumn
ospfAreaNbrNegotiationDone=_OspfAreaNbrNegotiationDone_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,5),_OspfAreaNbrNegotiationDone_Type())
ospfAreaNbrNegotiationDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrNegotiationDone.setStatus(_A)
_OspfAreaNbrExchangeDone_Type=Counter32
_OspfAreaNbrExchangeDone_Object=MibTableColumn
ospfAreaNbrExchangeDone=_OspfAreaNbrExchangeDone_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,6),_OspfAreaNbrExchangeDone_Type())
ospfAreaNbrExchangeDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrExchangeDone.setStatus(_A)
_OspfAreaNbrBadRequests_Type=Counter32
_OspfAreaNbrBadRequests_Object=MibTableColumn
ospfAreaNbrBadRequests=_OspfAreaNbrBadRequests_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,7),_OspfAreaNbrBadRequests_Type())
ospfAreaNbrBadRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrBadRequests.setStatus(_A)
_OspfAreaNbrBadSequence_Type=Counter32
_OspfAreaNbrBadSequence_Object=MibTableColumn
ospfAreaNbrBadSequence=_OspfAreaNbrBadSequence_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,8),_OspfAreaNbrBadSequence_Type())
ospfAreaNbrBadSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrBadSequence.setStatus(_A)
_OspfAreaNbrLoadingDone_Type=Counter32
_OspfAreaNbrLoadingDone_Object=MibTableColumn
ospfAreaNbrLoadingDone=_OspfAreaNbrLoadingDone_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,9),_OspfAreaNbrLoadingDone_Type())
ospfAreaNbrLoadingDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrLoadingDone.setStatus(_A)
_OspfAreaNbrN1way_Type=Counter32
_OspfAreaNbrN1way_Object=MibTableColumn
ospfAreaNbrN1way=_OspfAreaNbrN1way_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,10),_OspfAreaNbrN1way_Type())
ospfAreaNbrN1way.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrN1way.setStatus(_A)
_OspfAreaNbrRstAd_Type=Counter32
_OspfAreaNbrRstAd_Object=MibTableColumn
ospfAreaNbrRstAd=_OspfAreaNbrRstAd_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,11),_OspfAreaNbrRstAd_Type())
ospfAreaNbrRstAd.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrRstAd.setStatus(_A)
_OspfAreaNbrDown_Type=Counter32
_OspfAreaNbrDown_Object=MibTableColumn
ospfAreaNbrDown=_OspfAreaNbrDown_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,12),_OspfAreaNbrDown_Type())
ospfAreaNbrDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrDown.setStatus(_A)
_OspfAreaNbrN2way_Type=Counter32
_OspfAreaNbrN2way_Object=MibTableColumn
ospfAreaNbrN2way=_OspfAreaNbrN2way_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,2,1,13),_OspfAreaNbrN2way_Type())
ospfAreaNbrN2way.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrN2way.setStatus(_A)
_OspfAreaChangeStats_Object=MibTable
ospfAreaChangeStats=_OspfAreaChangeStats_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3))
if mibBuilder.loadTexts:ospfAreaChangeStats.setStatus(_A)
_OspfAreaChangeStatsEntry_Object=MibTableRow
ospfAreaChangeStatsEntry=_OspfAreaChangeStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3,1))
ospfAreaChangeStatsEntry.setIndexNames((0,_G,_Am))
if mibBuilder.loadTexts:ospfAreaChangeStatsEntry.setStatus(_A)
_OspfAreaIntfIndex_Type=Integer32
_OspfAreaIntfIndex_Object=MibTableColumn
ospfAreaIntfIndex=_OspfAreaIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3,1,1),_OspfAreaIntfIndex_Type())
ospfAreaIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfIndex.setStatus(_A)
_OspfAreaIntfHello_Type=Counter32
_OspfAreaIntfHello_Object=MibTableColumn
ospfAreaIntfHello=_OspfAreaIntfHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3,1,2),_OspfAreaIntfHello_Type())
ospfAreaIntfHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfHello.setStatus(_A)
_OspfAreaIntfDown_Type=Counter32
_OspfAreaIntfDown_Object=MibTableColumn
ospfAreaIntfDown=_OspfAreaIntfDown_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3,1,3),_OspfAreaIntfDown_Type())
ospfAreaIntfDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfDown.setStatus(_A)
_OspfAreaIntfLoop_Type=Counter32
_OspfAreaIntfLoop_Object=MibTableColumn
ospfAreaIntfLoop=_OspfAreaIntfLoop_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3,1,4),_OspfAreaIntfLoop_Type())
ospfAreaIntfLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfLoop.setStatus(_A)
_OspfAreaIntfUnloop_Type=Counter32
_OspfAreaIntfUnloop_Object=MibTableColumn
ospfAreaIntfUnloop=_OspfAreaIntfUnloop_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3,1,5),_OspfAreaIntfUnloop_Type())
ospfAreaIntfUnloop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfUnloop.setStatus(_A)
_OspfAreaIntfWaitTimer_Type=Counter32
_OspfAreaIntfWaitTimer_Object=MibTableColumn
ospfAreaIntfWaitTimer=_OspfAreaIntfWaitTimer_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3,1,6),_OspfAreaIntfWaitTimer_Type())
ospfAreaIntfWaitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfWaitTimer.setStatus(_A)
_OspfAreaIntfBackup_Type=Counter32
_OspfAreaIntfBackup_Object=MibTableColumn
ospfAreaIntfBackup=_OspfAreaIntfBackup_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3,1,7),_OspfAreaIntfBackup_Type())
ospfAreaIntfBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfBackup.setStatus(_A)
_OspfAreaIntfNbrChange_Type=Counter32
_OspfAreaIntfNbrChange_Object=MibTableColumn
ospfAreaIntfNbrChange=_OspfAreaIntfNbrChange_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,3,1,8),_OspfAreaIntfNbrChange_Type())
ospfAreaIntfNbrChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfNbrChange.setStatus(_A)
_OspfAreaErrorStats_Object=MibTable
ospfAreaErrorStats=_OspfAreaErrorStats_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,4))
if mibBuilder.loadTexts:ospfAreaErrorStats.setStatus(_A)
_OspfAreaErrorStatsEntry_Object=MibTableRow
ospfAreaErrorStatsEntry=_OspfAreaErrorStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,4,1))
ospfAreaErrorStatsEntry.setIndexNames((0,_G,_An))
if mibBuilder.loadTexts:ospfAreaErrorStatsEntry.setStatus(_A)
_OspfAreaErrIndex_Type=Integer32
_OspfAreaErrIndex_Object=MibTableColumn
ospfAreaErrIndex=_OspfAreaErrIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,4,1,1),_OspfAreaErrIndex_Type())
ospfAreaErrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaErrIndex.setStatus(_A)
_OspfAreaErrAuthFailure_Type=Counter32
_OspfAreaErrAuthFailure_Object=MibTableColumn
ospfAreaErrAuthFailure=_OspfAreaErrAuthFailure_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,4,1,2),_OspfAreaErrAuthFailure_Type())
ospfAreaErrAuthFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaErrAuthFailure.setStatus(_A)
_OspfAreaErrNetmaskMismatch_Type=Counter32
_OspfAreaErrNetmaskMismatch_Object=MibTableColumn
ospfAreaErrNetmaskMismatch=_OspfAreaErrNetmaskMismatch_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,4,1,3),_OspfAreaErrNetmaskMismatch_Type())
ospfAreaErrNetmaskMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaErrNetmaskMismatch.setStatus(_A)
_OspfAreaErrHelloMismatch_Type=Counter32
_OspfAreaErrHelloMismatch_Object=MibTableColumn
ospfAreaErrHelloMismatch=_OspfAreaErrHelloMismatch_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,4,1,4),_OspfAreaErrHelloMismatch_Type())
ospfAreaErrHelloMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaErrHelloMismatch.setStatus(_A)
_OspfAreaErrDeadMismatch_Type=Counter32
_OspfAreaErrDeadMismatch_Object=MibTableColumn
ospfAreaErrDeadMismatch=_OspfAreaErrDeadMismatch_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,4,1,5),_OspfAreaErrDeadMismatch_Type())
ospfAreaErrDeadMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaErrDeadMismatch.setStatus(_A)
_OspfAreaErrOptionsMismatch_Type=Counter32
_OspfAreaErrOptionsMismatch_Object=MibTableColumn
ospfAreaErrOptionsMismatch=_OspfAreaErrOptionsMismatch_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,4,1,6),_OspfAreaErrOptionsMismatch_Type())
ospfAreaErrOptionsMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaErrOptionsMismatch.setStatus(_A)
_OspfAreaErrUnknownNbr_Type=Counter32
_OspfAreaErrUnknownNbr_Object=MibTableColumn
ospfAreaErrUnknownNbr=_OspfAreaErrUnknownNbr_Object((1,3,6,1,4,1,1872,2,5,3,2,6,2,4,1,7),_OspfAreaErrUnknownNbr_Type())
ospfAreaErrUnknownNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaErrUnknownNbr.setStatus(_A)
_OspfInterface_ObjectIdentity=ObjectIdentity
ospfInterface=_OspfInterface_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,6,3))
_OspfIntfRxTxStats_Object=MibTable
ospfIntfRxTxStats=_OspfIntfRxTxStats_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1))
if mibBuilder.loadTexts:ospfIntfRxTxStats.setStatus(_A)
_OspfIntfRxTxStatsEntry_Object=MibTableRow
ospfIntfRxTxStatsEntry=_OspfIntfRxTxStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1))
ospfIntfRxTxStatsEntry.setIndexNames((0,_G,_Ao))
if mibBuilder.loadTexts:ospfIntfRxTxStatsEntry.setStatus(_A)
_OspfIntfRxTxIndex_Type=Integer32
_OspfIntfRxTxIndex_Object=MibTableColumn
ospfIntfRxTxIndex=_OspfIntfRxTxIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,1),_OspfIntfRxTxIndex_Type())
ospfIntfRxTxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxTxIndex.setStatus(_A)
_OspfIntfRxPkts_Type=Counter32
_OspfIntfRxPkts_Object=MibTableColumn
ospfIntfRxPkts=_OspfIntfRxPkts_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,2),_OspfIntfRxPkts_Type())
ospfIntfRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxPkts.setStatus(_A)
_OspfIntfTxPkts_Type=Counter32
_OspfIntfTxPkts_Object=MibTableColumn
ospfIntfTxPkts=_OspfIntfTxPkts_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,3),_OspfIntfTxPkts_Type())
ospfIntfTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxPkts.setStatus(_A)
_OspfIntfRxHello_Type=Counter32
_OspfIntfRxHello_Object=MibTableColumn
ospfIntfRxHello=_OspfIntfRxHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,4),_OspfIntfRxHello_Type())
ospfIntfRxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxHello.setStatus(_A)
_OspfIntfTxHello_Type=Counter32
_OspfIntfTxHello_Object=MibTableColumn
ospfIntfTxHello=_OspfIntfTxHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,5),_OspfIntfTxHello_Type())
ospfIntfTxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxHello.setStatus(_A)
_OspfIntfRxDatabase_Type=Counter32
_OspfIntfRxDatabase_Object=MibTableColumn
ospfIntfRxDatabase=_OspfIntfRxDatabase_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,6),_OspfIntfRxDatabase_Type())
ospfIntfRxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxDatabase.setStatus(_A)
_OspfIntfTxDatabase_Type=Counter32
_OspfIntfTxDatabase_Object=MibTableColumn
ospfIntfTxDatabase=_OspfIntfTxDatabase_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,7),_OspfIntfTxDatabase_Type())
ospfIntfTxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxDatabase.setStatus(_A)
_OspfIntfRxlsReqs_Type=Counter32
_OspfIntfRxlsReqs_Object=MibTableColumn
ospfIntfRxlsReqs=_OspfIntfRxlsReqs_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,8),_OspfIntfRxlsReqs_Type())
ospfIntfRxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxlsReqs.setStatus(_A)
_OspfIntfTxlsReqs_Type=Counter32
_OspfIntfTxlsReqs_Object=MibTableColumn
ospfIntfTxlsReqs=_OspfIntfTxlsReqs_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,9),_OspfIntfTxlsReqs_Type())
ospfIntfTxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxlsReqs.setStatus(_A)
_OspfIntfRxlsAcks_Type=Counter32
_OspfIntfRxlsAcks_Object=MibTableColumn
ospfIntfRxlsAcks=_OspfIntfRxlsAcks_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,10),_OspfIntfRxlsAcks_Type())
ospfIntfRxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxlsAcks.setStatus(_A)
_OspfIntfTxlsAcks_Type=Counter32
_OspfIntfTxlsAcks_Object=MibTableColumn
ospfIntfTxlsAcks=_OspfIntfTxlsAcks_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,11),_OspfIntfTxlsAcks_Type())
ospfIntfTxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxlsAcks.setStatus(_A)
_OspfIntfRxlsUpdates_Type=Counter32
_OspfIntfRxlsUpdates_Object=MibTableColumn
ospfIntfRxlsUpdates=_OspfIntfRxlsUpdates_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,12),_OspfIntfRxlsUpdates_Type())
ospfIntfRxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxlsUpdates.setStatus(_A)
_OspfIntfTxlsUpdates_Type=Counter32
_OspfIntfTxlsUpdates_Object=MibTableColumn
ospfIntfTxlsUpdates=_OspfIntfTxlsUpdates_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,1,1,13),_OspfIntfTxlsUpdates_Type())
ospfIntfTxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxlsUpdates.setStatus(_A)
_OspfIntfNbrChangeStats_Object=MibTable
ospfIntfNbrChangeStats=_OspfIntfNbrChangeStats_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2))
if mibBuilder.loadTexts:ospfIntfNbrChangeStats.setStatus(_A)
_OspfIntfNbrChangeStatsEntry_Object=MibTableRow
ospfIntfNbrChangeStatsEntry=_OspfIntfNbrChangeStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1))
ospfIntfNbrChangeStatsEntry.setIndexNames((0,_G,_Ap))
if mibBuilder.loadTexts:ospfIntfNbrChangeStatsEntry.setStatus(_A)
_OspfIntfNbrIndex_Type=Integer32
_OspfIntfNbrIndex_Object=MibTableColumn
ospfIntfNbrIndex=_OspfIntfNbrIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,1),_OspfIntfNbrIndex_Type())
ospfIntfNbrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrIndex.setStatus(_A)
_OspfIntfNbrhello_Type=Counter32
_OspfIntfNbrhello_Object=MibTableColumn
ospfIntfNbrhello=_OspfIntfNbrhello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,2),_OspfIntfNbrhello_Type())
ospfIntfNbrhello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrhello.setStatus(_A)
_OspfIntfNbrStart_Type=Counter32
_OspfIntfNbrStart_Object=MibTableColumn
ospfIntfNbrStart=_OspfIntfNbrStart_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,3),_OspfIntfNbrStart_Type())
ospfIntfNbrStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrStart.setStatus(_A)
_OspfIntfNbrAdjointOk_Type=Counter32
_OspfIntfNbrAdjointOk_Object=MibTableColumn
ospfIntfNbrAdjointOk=_OspfIntfNbrAdjointOk_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,4),_OspfIntfNbrAdjointOk_Type())
ospfIntfNbrAdjointOk.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrAdjointOk.setStatus(_A)
_OspfIntfNbrNegotiationDone_Type=Counter32
_OspfIntfNbrNegotiationDone_Object=MibTableColumn
ospfIntfNbrNegotiationDone=_OspfIntfNbrNegotiationDone_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,5),_OspfIntfNbrNegotiationDone_Type())
ospfIntfNbrNegotiationDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrNegotiationDone.setStatus(_A)
_OspfIntfNbrExchangeDone_Type=Counter32
_OspfIntfNbrExchangeDone_Object=MibTableColumn
ospfIntfNbrExchangeDone=_OspfIntfNbrExchangeDone_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,6),_OspfIntfNbrExchangeDone_Type())
ospfIntfNbrExchangeDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrExchangeDone.setStatus(_A)
_OspfIntfNbrBadRequests_Type=Counter32
_OspfIntfNbrBadRequests_Object=MibTableColumn
ospfIntfNbrBadRequests=_OspfIntfNbrBadRequests_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,7),_OspfIntfNbrBadRequests_Type())
ospfIntfNbrBadRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrBadRequests.setStatus(_A)
_OspfIntfNbrBadSequence_Type=Counter32
_OspfIntfNbrBadSequence_Object=MibTableColumn
ospfIntfNbrBadSequence=_OspfIntfNbrBadSequence_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,8),_OspfIntfNbrBadSequence_Type())
ospfIntfNbrBadSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrBadSequence.setStatus(_A)
_OspfIntfNbrLoadingDone_Type=Counter32
_OspfIntfNbrLoadingDone_Object=MibTableColumn
ospfIntfNbrLoadingDone=_OspfIntfNbrLoadingDone_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,9),_OspfIntfNbrLoadingDone_Type())
ospfIntfNbrLoadingDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrLoadingDone.setStatus(_A)
_OspfIntfNbrN1way_Type=Counter32
_OspfIntfNbrN1way_Object=MibTableColumn
ospfIntfNbrN1way=_OspfIntfNbrN1way_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,10),_OspfIntfNbrN1way_Type())
ospfIntfNbrN1way.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrN1way.setStatus(_A)
_OspfIntfNbrRstAd_Type=Counter32
_OspfIntfNbrRstAd_Object=MibTableColumn
ospfIntfNbrRstAd=_OspfIntfNbrRstAd_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,11),_OspfIntfNbrRstAd_Type())
ospfIntfNbrRstAd.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrRstAd.setStatus(_A)
_OspfIntfNbrDown_Type=Counter32
_OspfIntfNbrDown_Object=MibTableColumn
ospfIntfNbrDown=_OspfIntfNbrDown_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,12),_OspfIntfNbrDown_Type())
ospfIntfNbrDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrDown.setStatus(_A)
_OspfIntfNbrN2way_Type=Counter32
_OspfIntfNbrN2way_Object=MibTableColumn
ospfIntfNbrN2way=_OspfIntfNbrN2way_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,2,1,13),_OspfIntfNbrN2way_Type())
ospfIntfNbrN2way.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrN2way.setStatus(_A)
_OspfIntfChangeStats_Object=MibTable
ospfIntfChangeStats=_OspfIntfChangeStats_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3))
if mibBuilder.loadTexts:ospfIntfChangeStats.setStatus(_A)
_OspfIntfChangeStatsEntry_Object=MibTableRow
ospfIntfChangeStatsEntry=_OspfIntfChangeStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3,1))
ospfIntfChangeStatsEntry.setIndexNames((0,_G,_Aq))
if mibBuilder.loadTexts:ospfIntfChangeStatsEntry.setStatus(_A)
_OspfIntfIndex_Type=Integer32
_OspfIntfIndex_Object=MibTableColumn
ospfIntfIndex=_OspfIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3,1,1),_OspfIntfIndex_Type())
ospfIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfIndex.setStatus(_A)
_OspfIntfHello_Type=Counter32
_OspfIntfHello_Object=MibTableColumn
ospfIntfHello=_OspfIntfHello_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3,1,2),_OspfIntfHello_Type())
ospfIntfHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfHello.setStatus(_A)
_OspfIntfDown_Type=Counter32
_OspfIntfDown_Object=MibTableColumn
ospfIntfDown=_OspfIntfDown_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3,1,3),_OspfIntfDown_Type())
ospfIntfDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfDown.setStatus(_A)
_OspfIntfLoop_Type=Counter32
_OspfIntfLoop_Object=MibTableColumn
ospfIntfLoop=_OspfIntfLoop_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3,1,4),_OspfIntfLoop_Type())
ospfIntfLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfLoop.setStatus(_A)
_OspfIntfUnloop_Type=Counter32
_OspfIntfUnloop_Object=MibTableColumn
ospfIntfUnloop=_OspfIntfUnloop_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3,1,5),_OspfIntfUnloop_Type())
ospfIntfUnloop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfUnloop.setStatus(_A)
_OspfIntfWaitTimer_Type=Counter32
_OspfIntfWaitTimer_Object=MibTableColumn
ospfIntfWaitTimer=_OspfIntfWaitTimer_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3,1,6),_OspfIntfWaitTimer_Type())
ospfIntfWaitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfWaitTimer.setStatus(_A)
_OspfIntfBackup_Type=Counter32
_OspfIntfBackup_Object=MibTableColumn
ospfIntfBackup=_OspfIntfBackup_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3,1,7),_OspfIntfBackup_Type())
ospfIntfBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfBackup.setStatus(_A)
_OspfIntfNbrChange_Type=Counter32
_OspfIntfNbrChange_Object=MibTableColumn
ospfIntfNbrChange=_OspfIntfNbrChange_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,3,1,8),_OspfIntfNbrChange_Type())
ospfIntfNbrChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrChange.setStatus(_A)
_OspfIntfErrorStats_Object=MibTable
ospfIntfErrorStats=_OspfIntfErrorStats_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,4))
if mibBuilder.loadTexts:ospfIntfErrorStats.setStatus(_A)
_OspfIntfErrorStatsEntry_Object=MibTableRow
ospfIntfErrorStatsEntry=_OspfIntfErrorStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,4,1))
ospfIntfErrorStatsEntry.setIndexNames((0,_G,_Ar))
if mibBuilder.loadTexts:ospfIntfErrorStatsEntry.setStatus(_A)
_OspfIntfErrIndex_Type=Integer32
_OspfIntfErrIndex_Object=MibTableColumn
ospfIntfErrIndex=_OspfIntfErrIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,4,1,1),_OspfIntfErrIndex_Type())
ospfIntfErrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfErrIndex.setStatus(_A)
_OspfIntfErrAuthFailure_Type=Counter32
_OspfIntfErrAuthFailure_Object=MibTableColumn
ospfIntfErrAuthFailure=_OspfIntfErrAuthFailure_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,4,1,2),_OspfIntfErrAuthFailure_Type())
ospfIntfErrAuthFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfErrAuthFailure.setStatus(_A)
_OspfIntfErrNetmaskMismatch_Type=Counter32
_OspfIntfErrNetmaskMismatch_Object=MibTableColumn
ospfIntfErrNetmaskMismatch=_OspfIntfErrNetmaskMismatch_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,4,1,3),_OspfIntfErrNetmaskMismatch_Type())
ospfIntfErrNetmaskMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfErrNetmaskMismatch.setStatus(_A)
_OspfIntfErrHelloMismatch_Type=Counter32
_OspfIntfErrHelloMismatch_Object=MibTableColumn
ospfIntfErrHelloMismatch=_OspfIntfErrHelloMismatch_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,4,1,4),_OspfIntfErrHelloMismatch_Type())
ospfIntfErrHelloMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfErrHelloMismatch.setStatus(_A)
_OspfIntfErrDeadMismatch_Type=Counter32
_OspfIntfErrDeadMismatch_Object=MibTableColumn
ospfIntfErrDeadMismatch=_OspfIntfErrDeadMismatch_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,4,1,5),_OspfIntfErrDeadMismatch_Type())
ospfIntfErrDeadMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfErrDeadMismatch.setStatus(_A)
_OspfIntfErrOptionsMismatch_Type=Counter32
_OspfIntfErrOptionsMismatch_Object=MibTableColumn
ospfIntfErrOptionsMismatch=_OspfIntfErrOptionsMismatch_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,4,1,6),_OspfIntfErrOptionsMismatch_Type())
ospfIntfErrOptionsMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfErrOptionsMismatch.setStatus(_A)
_OspfIntfErrUnknownNbr_Type=Counter32
_OspfIntfErrUnknownNbr_Object=MibTableColumn
ospfIntfErrUnknownNbr=_OspfIntfErrUnknownNbr_Object((1,3,6,1,4,1,1872,2,5,3,2,6,3,4,1,7),_OspfIntfErrUnknownNbr_Type())
ospfIntfErrUnknownNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfErrUnknownNbr.setStatus(_A)
_ClearStats_ObjectIdentity=ObjectIdentity
clearStats=_ClearStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,7))
class _IpClearStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_V,2)))
_IpClearStats_Type.__name__=_C
_IpClearStats_Object=MibScalar
ipClearStats=_IpClearStats_Object((1,3,6,1,4,1,1872,2,5,3,2,7,1),_IpClearStats_Type())
ipClearStats.setMaxAccess(_H)
if mibBuilder.loadTexts:ipClearStats.setStatus(_A)
_IfStatsTable_Object=MibTable
ifStatsTable=_IfStatsTable_Object((1,3,6,1,4,1,1872,2,5,3,2,7,2))
if mibBuilder.loadTexts:ifStatsTable.setStatus(_A)
_IfStatsEntry_Object=MibTableRow
ifStatsEntry=_IfStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,7,2,1))
ifStatsEntry.setIndexNames((0,_G,_As))
if mibBuilder.loadTexts:ifStatsEntry.setStatus(_A)
_IfStatsIndex_Type=Integer32
_IfStatsIndex_Object=MibTableColumn
ifStatsIndex=_IfStatsIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,7,2,1,1),_IfStatsIndex_Type())
ifStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStatsIndex.setStatus(_A)
class _IfClearStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_V,2)))
_IfClearStats_Type.__name__=_C
_IfClearStats_Object=MibTableColumn
ifClearStats=_IfClearStats_Object((1,3,6,1,4,1,1872,2,5,3,2,7,2,1,2),_IfClearStats_Type())
ifClearStats.setMaxAccess(_H)
if mibBuilder.loadTexts:ifClearStats.setStatus(_A)
_Ip6Stats_ObjectIdentity=ObjectIdentity
ip6Stats=_Ip6Stats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,10))
_Ip6InReceives_Type=Counter32
_Ip6InReceives_Object=MibScalar
ip6InReceives=_Ip6InReceives_Object((1,3,6,1,4,1,1872,2,5,3,2,10,1),_Ip6InReceives_Type())
ip6InReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6InReceives.setStatus(_A)
_Ip6ForwDatagrams_Type=Counter32
_Ip6ForwDatagrams_Object=MibScalar
ip6ForwDatagrams=_Ip6ForwDatagrams_Object((1,3,6,1,4,1,1872,2,5,3,2,10,2),_Ip6ForwDatagrams_Type())
ip6ForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6ForwDatagrams.setStatus(_A)
_Ip6InDelivers_Type=Counter32
_Ip6InDelivers_Object=MibScalar
ip6InDelivers=_Ip6InDelivers_Object((1,3,6,1,4,1,1872,2,5,3,2,10,3),_Ip6InDelivers_Type())
ip6InDelivers.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6InDelivers.setStatus(_A)
_Ip6InDiscards_Type=Counter32
_Ip6InDiscards_Object=MibScalar
ip6InDiscards=_Ip6InDiscards_Object((1,3,6,1,4,1,1872,2,5,3,2,10,4),_Ip6InDiscards_Type())
ip6InDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6InDiscards.setStatus(_A)
_Ip6InUnknownProtos_Type=Counter32
_Ip6InUnknownProtos_Object=MibScalar
ip6InUnknownProtos=_Ip6InUnknownProtos_Object((1,3,6,1,4,1,1872,2,5,3,2,10,5),_Ip6InUnknownProtos_Type())
ip6InUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6InUnknownProtos.setStatus(_A)
_Ip6InAddrErrors_Type=Counter32
_Ip6InAddrErrors_Object=MibScalar
ip6InAddrErrors=_Ip6InAddrErrors_Object((1,3,6,1,4,1,1872,2,5,3,2,10,6),_Ip6InAddrErrors_Type())
ip6InAddrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6InAddrErrors.setStatus(_A)
_Ip6OutRequests_Type=Counter32
_Ip6OutRequests_Object=MibScalar
ip6OutRequests=_Ip6OutRequests_Object((1,3,6,1,4,1,1872,2,5,3,2,10,7),_Ip6OutRequests_Type())
ip6OutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6OutRequests.setStatus(_A)
_Ip6OutNoRoutes_Type=Counter32
_Ip6OutNoRoutes_Object=MibScalar
ip6OutNoRoutes=_Ip6OutNoRoutes_Object((1,3,6,1,4,1,1872,2,5,3,2,10,8),_Ip6OutNoRoutes_Type())
ip6OutNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6OutNoRoutes.setStatus(_A)
_Ip6ReasmOKs_Type=Counter32
_Ip6ReasmOKs_Object=MibScalar
ip6ReasmOKs=_Ip6ReasmOKs_Object((1,3,6,1,4,1,1872,2,5,3,2,10,9),_Ip6ReasmOKs_Type())
ip6ReasmOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6ReasmOKs.setStatus(_A)
_Ip6ReasmFails_Type=Counter32
_Ip6ReasmFails_Object=MibScalar
ip6ReasmFails=_Ip6ReasmFails_Object((1,3,6,1,4,1,1872,2,5,3,2,10,10),_Ip6ReasmFails_Type())
ip6ReasmFails.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6ReasmFails.setStatus(_A)
_Ip6icmpInMsgs_Type=Counter32
_Ip6icmpInMsgs_Object=MibScalar
ip6icmpInMsgs=_Ip6icmpInMsgs_Object((1,3,6,1,4,1,1872,2,5,3,2,10,11),_Ip6icmpInMsgs_Type())
ip6icmpInMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6icmpInMsgs.setStatus(_A)
_Ip6icmpOutMsgs_Type=Counter32
_Ip6icmpOutMsgs_Object=MibScalar
ip6icmpOutMsgs=_Ip6icmpOutMsgs_Object((1,3,6,1,4,1,1872,2,5,3,2,10,12),_Ip6icmpOutMsgs_Type())
ip6icmpOutMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6icmpOutMsgs.setStatus(_A)
_Ip6icmpInErrors_Type=Counter32
_Ip6icmpInErrors_Object=MibScalar
ip6icmpInErrors=_Ip6icmpInErrors_Object((1,3,6,1,4,1,1872,2,5,3,2,10,13),_Ip6icmpInErrors_Type())
ip6icmpInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6icmpInErrors.setStatus(_A)
_Ip6icmpOutErrors_Type=Counter32
_Ip6icmpOutErrors_Object=MibScalar
ip6icmpOutErrors=_Ip6icmpOutErrors_Object((1,3,6,1,4,1,1872,2,5,3,2,10,14),_Ip6icmpOutErrors_Type())
ip6icmpOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6icmpOutErrors.setStatus(_A)
_Icmp6Stats_ObjectIdentity=ObjectIdentity
icmp6Stats=_Icmp6Stats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,11))
_Icmp6StatsTable_Object=MibTable
icmp6StatsTable=_Icmp6StatsTable_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1))
if mibBuilder.loadTexts:icmp6StatsTable.setStatus(_A)
_Icmp6StatsEntry_Object=MibTableRow
icmp6StatsEntry=_Icmp6StatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1))
icmp6StatsEntry.setIndexNames((0,_G,_At))
if mibBuilder.loadTexts:icmp6StatsEntry.setStatus(_A)
_Icmp6StatsIndx_Type=Integer32
_Icmp6StatsIndx_Object=MibTableColumn
icmp6StatsIndx=_Icmp6StatsIndx_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,1),_Icmp6StatsIndx_Type())
icmp6StatsIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6StatsIndx.setStatus(_A)
_Icmp6IntfIndex_Type=Integer32
_Icmp6IntfIndex_Object=MibTableColumn
icmp6IntfIndex=_Icmp6IntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,2),_Icmp6IntfIndex_Type())
icmp6IntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6IntfIndex.setStatus(_A)
_Icmp6InMsgs_Type=Counter32
_Icmp6InMsgs_Object=MibTableColumn
icmp6InMsgs=_Icmp6InMsgs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,3),_Icmp6InMsgs_Type())
icmp6InMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InMsgs.setStatus(_A)
_Icmp6InErrors_Type=Counter32
_Icmp6InErrors_Object=MibTableColumn
icmp6InErrors=_Icmp6InErrors_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,4),_Icmp6InErrors_Type())
icmp6InErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InErrors.setStatus(_A)
_Icmp6InEchos_Type=Counter32
_Icmp6InEchos_Object=MibTableColumn
icmp6InEchos=_Icmp6InEchos_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,5),_Icmp6InEchos_Type())
icmp6InEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InEchos.setStatus(_A)
_Icmp6InEchoReps_Type=Counter32
_Icmp6InEchoReps_Object=MibTableColumn
icmp6InEchoReps=_Icmp6InEchoReps_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,6),_Icmp6InEchoReps_Type())
icmp6InEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InEchoReps.setStatus(_A)
_Icmp6InNSs_Type=Counter32
_Icmp6InNSs_Object=MibTableColumn
icmp6InNSs=_Icmp6InNSs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,7),_Icmp6InNSs_Type())
icmp6InNSs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InNSs.setStatus(_A)
_Icmp6InNAs_Type=Counter32
_Icmp6InNAs_Object=MibTableColumn
icmp6InNAs=_Icmp6InNAs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,8),_Icmp6InNAs_Type())
icmp6InNAs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InNAs.setStatus(_A)
_Icmp6InRSs_Type=Counter32
_Icmp6InRSs_Object=MibTableColumn
icmp6InRSs=_Icmp6InRSs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,9),_Icmp6InRSs_Type())
icmp6InRSs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InRSs.setStatus(_A)
_Icmp6InRAs_Type=Counter32
_Icmp6InRAs_Object=MibTableColumn
icmp6InRAs=_Icmp6InRAs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,10),_Icmp6InRAs_Type())
icmp6InRAs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InRAs.setStatus(_A)
_Icmp6InDestUnreachs_Type=Counter32
_Icmp6InDestUnreachs_Object=MibTableColumn
icmp6InDestUnreachs=_Icmp6InDestUnreachs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,11),_Icmp6InDestUnreachs_Type())
icmp6InDestUnreachs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InDestUnreachs.setStatus(_A)
_Icmp6InTimeExcds_Type=Counter32
_Icmp6InTimeExcds_Object=MibTableColumn
icmp6InTimeExcds=_Icmp6InTimeExcds_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,12),_Icmp6InTimeExcds_Type())
icmp6InTimeExcds.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InTimeExcds.setStatus(_A)
_Icmp6InTooBigs_Type=Counter32
_Icmp6InTooBigs_Object=MibTableColumn
icmp6InTooBigs=_Icmp6InTooBigs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,13),_Icmp6InTooBigs_Type())
icmp6InTooBigs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InTooBigs.setStatus(_A)
_Icmp6InParmProbs_Type=Counter32
_Icmp6InParmProbs_Object=MibTableColumn
icmp6InParmProbs=_Icmp6InParmProbs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,14),_Icmp6InParmProbs_Type())
icmp6InParmProbs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InParmProbs.setStatus(_A)
_Icmp6InRedirects_Type=Counter32
_Icmp6InRedirects_Object=MibTableColumn
icmp6InRedirects=_Icmp6InRedirects_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,15),_Icmp6InRedirects_Type())
icmp6InRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6InRedirects.setStatus(_A)
_Icmp6OutMsgs_Type=Counter32
_Icmp6OutMsgs_Object=MibTableColumn
icmp6OutMsgs=_Icmp6OutMsgs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,16),_Icmp6OutMsgs_Type())
icmp6OutMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6OutMsgs.setStatus(_A)
_Icmp6OutErrors_Type=Counter32
_Icmp6OutErrors_Object=MibTableColumn
icmp6OutErrors=_Icmp6OutErrors_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,17),_Icmp6OutErrors_Type())
icmp6OutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6OutErrors.setStatus(_A)
_Icmp6OutEchos_Type=Counter32
_Icmp6OutEchos_Object=MibTableColumn
icmp6OutEchos=_Icmp6OutEchos_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,18),_Icmp6OutEchos_Type())
icmp6OutEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6OutEchos.setStatus(_A)
_Icmp6OutEchoReps_Type=Counter32
_Icmp6OutEchoReps_Object=MibTableColumn
icmp6OutEchoReps=_Icmp6OutEchoReps_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,19),_Icmp6OutEchoReps_Type())
icmp6OutEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6OutEchoReps.setStatus(_A)
_Icmp6OutNSs_Type=Counter32
_Icmp6OutNSs_Object=MibTableColumn
icmp6OutNSs=_Icmp6OutNSs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,20),_Icmp6OutNSs_Type())
icmp6OutNSs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6OutNSs.setStatus(_A)
_Icmp6OutNAs_Type=Counter32
_Icmp6OutNAs_Object=MibTableColumn
icmp6OutNAs=_Icmp6OutNAs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,21),_Icmp6OutNAs_Type())
icmp6OutNAs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6OutNAs.setStatus(_A)
_Icmp6OutRSs_Type=Counter32
_Icmp6OutRSs_Object=MibTableColumn
icmp6OutRSs=_Icmp6OutRSs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,22),_Icmp6OutRSs_Type())
icmp6OutRSs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6OutRSs.setStatus(_A)
_Icmp6OutRAs_Type=Counter32
_Icmp6OutRAs_Object=MibTableColumn
icmp6OutRAs=_Icmp6OutRAs_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,23),_Icmp6OutRAs_Type())
icmp6OutRAs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6OutRAs.setStatus(_A)
_Icmp6OutRedirects_Type=Counter32
_Icmp6OutRedirects_Object=MibTableColumn
icmp6OutRedirects=_Icmp6OutRedirects_Object((1,3,6,1,4,1,1872,2,5,3,2,11,1,1,24),_Icmp6OutRedirects_Type())
icmp6OutRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:icmp6OutRedirects.setStatus(_A)
_Ip6gwStats_ObjectIdentity=ObjectIdentity
ip6gwStats=_Ip6gwStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,12))
_Ip6GwStatsTable_Object=MibTable
ip6GwStatsTable=_Ip6GwStatsTable_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1))
if mibBuilder.loadTexts:ip6GwStatsTable.setStatus(_A)
_Ip6GwStatsEntry_Object=MibTableRow
ip6GwStatsEntry=_Ip6GwStatsEntry_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1,1))
ip6GwStatsEntry.setIndexNames((0,_G,_Au))
if mibBuilder.loadTexts:ip6GwStatsEntry.setStatus(_A)
_Ip6GwStatsIndex_Type=Integer32
_Ip6GwStatsIndex_Object=MibTableColumn
ip6GwStatsIndex=_Ip6GwStatsIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1,1,1),_Ip6GwStatsIndex_Type())
ip6GwStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6GwStatsIndex.setStatus(_A)
_Ip6GwIndex_Type=Integer32
_Ip6GwIndex_Object=MibTableColumn
ip6GwIndex=_Ip6GwIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1,1,2),_Ip6GwIndex_Type())
ip6GwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6GwIndex.setStatus(_A)
_Ip6GwEchoreq_Type=Counter32
_Ip6GwEchoreq_Object=MibTableColumn
ip6GwEchoreq=_Ip6GwEchoreq_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1,1,3),_Ip6GwEchoreq_Type())
ip6GwEchoreq.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6GwEchoreq.setStatus(_A)
_Ip6GwEchoresp_Type=Counter32
_Ip6GwEchoresp_Object=MibTableColumn
ip6GwEchoresp=_Ip6GwEchoresp_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1,1,4),_Ip6GwEchoresp_Type())
ip6GwEchoresp.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6GwEchoresp.setStatus(_A)
_Ip6GwFails_Type=Counter32
_Ip6GwFails_Object=MibTableColumn
ip6GwFails=_Ip6GwFails_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1,1,5),_Ip6GwFails_Type())
ip6GwFails.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6GwFails.setStatus(_A)
_Ip6GwMaster_Type=Integer32
_Ip6GwMaster_Object=MibTableColumn
ip6GwMaster=_Ip6GwMaster_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1,1,6),_Ip6GwMaster_Type())
ip6GwMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6GwMaster.setStatus(_A)
_Ip6IfIndex_Type=Integer32
_Ip6IfIndex_Object=MibTableColumn
ip6IfIndex=_Ip6IfIndex_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1,1,7),_Ip6IfIndex_Type())
ip6IfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6IfIndex.setStatus(_A)
_Ip6GwRetry_Type=Counter32
_Ip6GwRetry_Object=MibTableColumn
ip6GwRetry=_Ip6GwRetry_Object((1,3,6,1,4,1,1872,2,5,3,2,12,1,1,8),_Ip6GwRetry_Type())
ip6GwRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:ip6GwRetry.setStatus(_A)
_Rip2Stats_ObjectIdentity=ObjectIdentity
rip2Stats=_Rip2Stats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,13))
_RipStatInPackets_Type=Counter32
_RipStatInPackets_Object=MibScalar
ripStatInPackets=_RipStatInPackets_Object((1,3,6,1,4,1,1872,2,5,3,2,13,1),_RipStatInPackets_Type())
ripStatInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInPackets.setStatus(_A)
_RipStatOutPackets_Type=Counter32
_RipStatOutPackets_Object=MibScalar
ripStatOutPackets=_RipStatOutPackets_Object((1,3,6,1,4,1,1872,2,5,3,2,13,2),_RipStatOutPackets_Type())
ripStatOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatOutPackets.setStatus(_A)
_RipStatInRequestPkts_Type=Counter32
_RipStatInRequestPkts_Object=MibScalar
ripStatInRequestPkts=_RipStatInRequestPkts_Object((1,3,6,1,4,1,1872,2,5,3,2,13,3),_RipStatInRequestPkts_Type())
ripStatInRequestPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInRequestPkts.setStatus(_A)
_RipStatInResponsePkts_Type=Counter32
_RipStatInResponsePkts_Object=MibScalar
ripStatInResponsePkts=_RipStatInResponsePkts_Object((1,3,6,1,4,1,1872,2,5,3,2,13,4),_RipStatInResponsePkts_Type())
ripStatInResponsePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInResponsePkts.setStatus(_A)
_RipStatOutRequestPkts_Type=Counter32
_RipStatOutRequestPkts_Object=MibScalar
ripStatOutRequestPkts=_RipStatOutRequestPkts_Object((1,3,6,1,4,1,1872,2,5,3,2,13,5),_RipStatOutRequestPkts_Type())
ripStatOutRequestPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatOutRequestPkts.setStatus(_A)
_RipStatOutResponsePkts_Type=Counter32
_RipStatOutResponsePkts_Object=MibScalar
ripStatOutResponsePkts=_RipStatOutResponsePkts_Object((1,3,6,1,4,1,1872,2,5,3,2,13,6),_RipStatOutResponsePkts_Type())
ripStatOutResponsePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatOutResponsePkts.setStatus(_A)
_RipStatRouteTimeout_Type=Counter32
_RipStatRouteTimeout_Object=MibScalar
ripStatRouteTimeout=_RipStatRouteTimeout_Object((1,3,6,1,4,1,1872,2,5,3,2,13,7),_RipStatRouteTimeout_Type())
ripStatRouteTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatRouteTimeout.setStatus(_A)
_RipStatInBadSizePkts_Type=Counter32
_RipStatInBadSizePkts_Object=MibScalar
ripStatInBadSizePkts=_RipStatInBadSizePkts_Object((1,3,6,1,4,1,1872,2,5,3,2,13,8),_RipStatInBadSizePkts_Type())
ripStatInBadSizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInBadSizePkts.setStatus(_A)
_RipStatInBadVersion_Type=Counter32
_RipStatInBadVersion_Object=MibScalar
ripStatInBadVersion=_RipStatInBadVersion_Object((1,3,6,1,4,1,1872,2,5,3,2,13,9),_RipStatInBadVersion_Type())
ripStatInBadVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInBadVersion.setStatus(_A)
_RipStatInBadZeros_Type=Counter32
_RipStatInBadZeros_Object=MibScalar
ripStatInBadZeros=_RipStatInBadZeros_Object((1,3,6,1,4,1,1872,2,5,3,2,13,10),_RipStatInBadZeros_Type())
ripStatInBadZeros.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInBadZeros.setStatus(_A)
_RipStatInBadSourcePort_Type=Counter32
_RipStatInBadSourcePort_Object=MibScalar
ripStatInBadSourcePort=_RipStatInBadSourcePort_Object((1,3,6,1,4,1,1872,2,5,3,2,13,11),_RipStatInBadSourcePort_Type())
ripStatInBadSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInBadSourcePort.setStatus(_A)
_RipStatInBadSourceIP_Type=Counter32
_RipStatInBadSourceIP_Object=MibScalar
ripStatInBadSourceIP=_RipStatInBadSourceIP_Object((1,3,6,1,4,1,1872,2,5,3,2,13,12),_RipStatInBadSourceIP_Type())
ripStatInBadSourceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInBadSourceIP.setStatus(_A)
_RipStatInSelfRcvPkts_Type=Counter32
_RipStatInSelfRcvPkts_Object=MibScalar
ripStatInSelfRcvPkts=_RipStatInSelfRcvPkts_Object((1,3,6,1,4,1,1872,2,5,3,2,13,13),_RipStatInSelfRcvPkts_Type())
ripStatInSelfRcvPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInSelfRcvPkts.setStatus(_A)
_TcpStats_ObjectIdentity=ObjectIdentity
tcpStats=_TcpStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,2,14))
_TcpStatCurConn_Type=Counter32
_TcpStatCurConn_Object=MibScalar
tcpStatCurConn=_TcpStatCurConn_Object((1,3,6,1,4,1,1872,2,5,3,2,14,1),_TcpStatCurConn_Type())
tcpStatCurConn.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpStatCurConn.setStatus(_A)
_TcpStatCurInConn_Type=Counter32
_TcpStatCurInConn_Object=MibScalar
tcpStatCurInConn=_TcpStatCurInConn_Object((1,3,6,1,4,1,1872,2,5,3,2,14,2),_TcpStatCurInConn_Type())
tcpStatCurInConn.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpStatCurInConn.setStatus(_A)
_TcpStatCurOutConn_Type=Counter32
_TcpStatCurOutConn_Object=MibScalar
tcpStatCurOutConn=_TcpStatCurOutConn_Object((1,3,6,1,4,1,1872,2,5,3,2,14,3),_TcpStatCurOutConn_Type())
tcpStatCurOutConn.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpStatCurOutConn.setStatus(_A)
_Layer3Info_ObjectIdentity=ObjectIdentity
layer3Info=_Layer3Info_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3))
_IpRoutingInfo_ObjectIdentity=ObjectIdentity
ipRoutingInfo=_IpRoutingInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,1))
_IpRouteInfoTable_Object=MibTable
ipRouteInfoTable=_IpRouteInfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1))
if mibBuilder.loadTexts:ipRouteInfoTable.setStatus(_A)
_IpRouteInfoEntry_Object=MibTableRow
ipRouteInfoEntry=_IpRouteInfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1))
ipRouteInfoEntry.setIndexNames((0,_G,_Av))
if mibBuilder.loadTexts:ipRouteInfoEntry.setStatus(_A)
_IpRouteInfoIndx_Type=Integer32
_IpRouteInfoIndx_Object=MibTableColumn
ipRouteInfoIndx=_IpRouteInfoIndx_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,1),_IpRouteInfoIndx_Type())
ipRouteInfoIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoIndx.setStatus(_A)
_IpRouteInfoDestIp_Type=IpAddress
_IpRouteInfoDestIp_Object=MibTableColumn
ipRouteInfoDestIp=_IpRouteInfoDestIp_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,2),_IpRouteInfoDestIp_Type())
ipRouteInfoDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoDestIp.setStatus(_A)
_IpRouteInfoMask_Type=IpAddress
_IpRouteInfoMask_Object=MibTableColumn
ipRouteInfoMask=_IpRouteInfoMask_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,3),_IpRouteInfoMask_Type())
ipRouteInfoMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoMask.setStatus(_A)
_IpRouteInfoGateway_Type=IpAddress
_IpRouteInfoGateway_Object=MibTableColumn
ipRouteInfoGateway=_IpRouteInfoGateway_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,4),_IpRouteInfoGateway_Type())
ipRouteInfoGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoGateway.setStatus(_A)
class _IpRouteInfoTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('fixed',1),(_l,2),('addr',3),('rip',4),(_Aw,5),('martian',6),(_Ax,7),('vip',8),('bgp',9),('ospf',10),(_J,11)))
_IpRouteInfoTag_Type.__name__=_C
_IpRouteInfoTag_Object=MibTableColumn
ipRouteInfoTag=_IpRouteInfoTag_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,5),_IpRouteInfoTag_Type())
ipRouteInfoTag.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoTag.setStatus(_A)
class _IpRouteInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('indirect',1),('direct',2),(_m,3),(_Aw,4),('martian',5),(_Ax,6),(_K,7)))
_IpRouteInfoType_Type.__name__=_C
_IpRouteInfoType_Object=MibTableColumn
ipRouteInfoType=_IpRouteInfoType_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,6),_IpRouteInfoType_Type())
ipRouteInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoType.setStatus(_A)
_IpRouteInfoInterface_Type=Integer32
_IpRouteInfoInterface_Object=MibTableColumn
ipRouteInfoInterface=_IpRouteInfoInterface_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,7),_IpRouteInfoInterface_Type())
ipRouteInfoInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoInterface.setStatus(_A)
_IpRouteInfoGateway1_Type=IpAddress
_IpRouteInfoGateway1_Object=MibTableColumn
ipRouteInfoGateway1=_IpRouteInfoGateway1_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,8),_IpRouteInfoGateway1_Type())
ipRouteInfoGateway1.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoGateway1.setStatus(_A)
_IpRouteInfoGateway2_Type=IpAddress
_IpRouteInfoGateway2_Object=MibTableColumn
ipRouteInfoGateway2=_IpRouteInfoGateway2_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,9),_IpRouteInfoGateway2_Type())
ipRouteInfoGateway2.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoGateway2.setStatus(_A)
_IpRouteInfoMetric_Type=Integer32
_IpRouteInfoMetric_Object=MibTableColumn
ipRouteInfoMetric=_IpRouteInfoMetric_Object((1,3,6,1,4,1,1872,2,5,3,3,1,1,1,10),_IpRouteInfoMetric_Type())
ipRouteInfoMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoMetric.setStatus(_A)
class _RouteTableClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_V,2)))
_RouteTableClear_Type.__name__=_C
_RouteTableClear_Object=MibScalar
routeTableClear=_RouteTableClear_Object((1,3,6,1,4,1,1872,2,5,3,3,1,2),_RouteTableClear_Type())
routeTableClear.setMaxAccess(_H)
if mibBuilder.loadTexts:routeTableClear.setStatus(_A)
_ArpInfo_ObjectIdentity=ObjectIdentity
arpInfo=_ArpInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,2))
_ArpInfoTable_Object=MibTable
arpInfoTable=_ArpInfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,2,1))
if mibBuilder.loadTexts:arpInfoTable.setStatus(_A)
_ArpInfoEntry_Object=MibTableRow
arpInfoEntry=_ArpInfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,2,1,1))
arpInfoEntry.setIndexNames((0,_G,_Ay))
if mibBuilder.loadTexts:arpInfoEntry.setStatus(_A)
_ArpInfoDestIp_Type=IpAddress
_ArpInfoDestIp_Object=MibTableColumn
arpInfoDestIp=_ArpInfoDestIp_Object((1,3,6,1,4,1,1872,2,5,3,3,2,1,1,1),_ArpInfoDestIp_Type())
arpInfoDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoDestIp.setStatus(_A)
_ArpInfoMacAddr_Type=PhysAddress
_ArpInfoMacAddr_Object=MibTableColumn
arpInfoMacAddr=_ArpInfoMacAddr_Object((1,3,6,1,4,1,1872,2,5,3,3,2,1,1,2),_ArpInfoMacAddr_Type())
arpInfoMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoMacAddr.setStatus(_A)
_ArpInfoVLAN_Type=Integer32
_ArpInfoVLAN_Object=MibTableColumn
arpInfoVLAN=_ArpInfoVLAN_Object((1,3,6,1,4,1,1872,2,5,3,3,2,1,1,3),_ArpInfoVLAN_Type())
arpInfoVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoVLAN.setStatus(_A)
_ArpInfoSrcPort_Type=Integer32
_ArpInfoSrcPort_Object=MibTableColumn
arpInfoSrcPort=_ArpInfoSrcPort_Object((1,3,6,1,4,1,1872,2,5,3,3,2,1,1,4),_ArpInfoSrcPort_Type())
arpInfoSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoSrcPort.setStatus(_A)
_ArpInfoRefPorts_Type=Integer32
_ArpInfoRefPorts_Object=MibTableColumn
arpInfoRefPorts=_ArpInfoRefPorts_Object((1,3,6,1,4,1,1872,2,5,3,3,2,1,1,5),_ArpInfoRefPorts_Type())
arpInfoRefPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoRefPorts.setStatus(_A)
class _ArpInfoFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_V,1),('unresolved',2),('permanent',3),('indirect',4),('layer4',5)))
_ArpInfoFlag_Type.__name__=_C
_ArpInfoFlag_Object=MibTableColumn
arpInfoFlag=_ArpInfoFlag_Object((1,3,6,1,4,1,1872,2,5,3,3,2,1,1,6),_ArpInfoFlag_Type())
arpInfoFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoFlag.setStatus(_A)
class _ArpCacheClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_V,2)))
_ArpCacheClear_Type.__name__=_C
_ArpCacheClear_Object=MibScalar
arpCacheClear=_ArpCacheClear_Object((1,3,6,1,4,1,1872,2,5,3,3,2,2),_ArpCacheClear_Type())
arpCacheClear.setMaxAccess(_H)
if mibBuilder.loadTexts:arpCacheClear.setStatus(_A)
_VrrpInfo_ObjectIdentity=ObjectIdentity
vrrpInfo=_VrrpInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,3))
_VrrpInfoVirtRtrTable_Object=MibTable
vrrpInfoVirtRtrTable=_VrrpInfoVirtRtrTable_Object((1,3,6,1,4,1,1872,2,5,3,3,3,1))
if mibBuilder.loadTexts:vrrpInfoVirtRtrTable.setStatus(_A)
_VrrpInfoVirtRtrTableEntry_Object=MibTableRow
vrrpInfoVirtRtrTableEntry=_VrrpInfoVirtRtrTableEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,3,1,1))
vrrpInfoVirtRtrTableEntry.setIndexNames((0,_G,_Az))
if mibBuilder.loadTexts:vrrpInfoVirtRtrTableEntry.setStatus(_A)
_VrrpInfoVirtRtrIndex_Type=Integer32
_VrrpInfoVirtRtrIndex_Object=MibTableColumn
vrrpInfoVirtRtrIndex=_VrrpInfoVirtRtrIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,3,1,1,1),_VrrpInfoVirtRtrIndex_Type())
vrrpInfoVirtRtrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrIndex.setStatus(_A)
class _VrrpInfoVirtRtrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('master',2),(_n,3),('holdoff',4)))
_VrrpInfoVirtRtrState_Type.__name__=_C
_VrrpInfoVirtRtrState_Object=MibTableColumn
vrrpInfoVirtRtrState=_VrrpInfoVirtRtrState_Object((1,3,6,1,4,1,1872,2,5,3,3,3,1,1,2),_VrrpInfoVirtRtrState_Type())
vrrpInfoVirtRtrState.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrState.setStatus(_A)
class _VrrpInfoVirtRtrOwnership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('owner',1),('renter',2)))
_VrrpInfoVirtRtrOwnership_Type.__name__=_C
_VrrpInfoVirtRtrOwnership_Object=MibTableColumn
vrrpInfoVirtRtrOwnership=_VrrpInfoVirtRtrOwnership_Object((1,3,6,1,4,1,1872,2,5,3,3,3,1,1,3),_VrrpInfoVirtRtrOwnership_Type())
vrrpInfoVirtRtrOwnership.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrOwnership.setStatus(_A)
class _VrrpInfoVirtRtrServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_VrrpInfoVirtRtrServer_Type.__name__=_C
_VrrpInfoVirtRtrServer_Object=MibTableColumn
vrrpInfoVirtRtrServer=_VrrpInfoVirtRtrServer_Object((1,3,6,1,4,1,1872,2,5,3,3,3,1,1,4),_VrrpInfoVirtRtrServer_Type())
vrrpInfoVirtRtrServer.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrServer.setStatus(_A)
class _VrrpInfoVirtRtrProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_VrrpInfoVirtRtrProxy_Type.__name__=_C
_VrrpInfoVirtRtrProxy_Object=MibTableColumn
vrrpInfoVirtRtrProxy=_VrrpInfoVirtRtrProxy_Object((1,3,6,1,4,1,1872,2,5,3,3,3,1,1,5),_VrrpInfoVirtRtrProxy_Type())
vrrpInfoVirtRtrProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrProxy.setStatus(_A)
_VrrpInfoVirtRtrPriority_Type=Integer32
_VrrpInfoVirtRtrPriority_Object=MibTableColumn
vrrpInfoVirtRtrPriority=_VrrpInfoVirtRtrPriority_Object((1,3,6,1,4,1,1872,2,5,3,3,3,1,1,6),_VrrpInfoVirtRtrPriority_Type())
vrrpInfoVirtRtrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrPriority.setStatus(_A)
_Ospfinfo_ObjectIdentity=ObjectIdentity
ospfinfo=_Ospfinfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,4))
_OspfGeneralInfo_ObjectIdentity=ObjectIdentity
ospfGeneralInfo=_OspfGeneralInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,4,1))
_OspfStartTime_Type=Integer32
_OspfStartTime_Object=MibScalar
ospfStartTime=_OspfStartTime_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,1),_OspfStartTime_Type())
ospfStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfStartTime.setStatus(_A)
_OspfProcessUptime_Type=Counter32
_OspfProcessUptime_Object=MibScalar
ospfProcessUptime=_OspfProcessUptime_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,2),_OspfProcessUptime_Type())
ospfProcessUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfProcessUptime.setStatus(_A)
_OspfLsTypesSupported_Type=Integer32
_OspfLsTypesSupported_Object=MibScalar
ospfLsTypesSupported=_OspfLsTypesSupported_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,3),_OspfLsTypesSupported_Type())
ospfLsTypesSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfLsTypesSupported.setStatus(_A)
_OspfIntfCountForRouter_Type=Integer32
_OspfIntfCountForRouter_Object=MibScalar
ospfIntfCountForRouter=_OspfIntfCountForRouter_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,4),_OspfIntfCountForRouter_Type())
ospfIntfCountForRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfCountForRouter.setStatus(_A)
_OspfVlinkCountForRouter_Type=Integer32
_OspfVlinkCountForRouter_Object=MibScalar
ospfVlinkCountForRouter=_OspfVlinkCountForRouter_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,5),_OspfVlinkCountForRouter_Type())
ospfVlinkCountForRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVlinkCountForRouter.setStatus(_A)
_OspfTotalNeighbours_Type=Integer32
_OspfTotalNeighbours_Object=MibScalar
ospfTotalNeighbours=_OspfTotalNeighbours_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,6),_OspfTotalNeighbours_Type())
ospfTotalNeighbours.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalNeighbours.setStatus(_A)
_OspfNbrInInitState_Type=Integer32
_OspfNbrInInitState_Object=MibScalar
ospfNbrInInitState=_OspfNbrInInitState_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,7),_OspfNbrInInitState_Type())
ospfNbrInInitState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNbrInInitState.setStatus(_A)
_OspfNbrInExchState_Type=Integer32
_OspfNbrInExchState_Object=MibScalar
ospfNbrInExchState=_OspfNbrInExchState_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,8),_OspfNbrInExchState_Type())
ospfNbrInExchState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNbrInExchState.setStatus(_A)
_OspfNbrInFullState_Type=Integer32
_OspfNbrInFullState_Object=MibScalar
ospfNbrInFullState=_OspfNbrInFullState_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,9),_OspfNbrInFullState_Type())
ospfNbrInFullState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNbrInFullState.setStatus(_A)
_OspfTotalAreas_Type=Integer32
_OspfTotalAreas_Object=MibScalar
ospfTotalAreas=_OspfTotalAreas_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,10),_OspfTotalAreas_Type())
ospfTotalAreas.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalAreas.setStatus(_A)
_OspfTotalTransitAreas_Type=Integer32
_OspfTotalTransitAreas_Object=MibScalar
ospfTotalTransitAreas=_OspfTotalTransitAreas_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,11),_OspfTotalTransitAreas_Type())
ospfTotalTransitAreas.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalTransitAreas.setStatus(_A)
_OspfTotalNssaAreas_Type=Integer32
_OspfTotalNssaAreas_Object=MibScalar
ospfTotalNssaAreas=_OspfTotalNssaAreas_Object((1,3,6,1,4,1,1872,2,5,3,3,4,1,12),_OspfTotalNssaAreas_Type())
ospfTotalNssaAreas.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalNssaAreas.setStatus(_A)
_OspfAreaInfoTable_Object=MibTable
ospfAreaInfoTable=_OspfAreaInfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,4,2))
if mibBuilder.loadTexts:ospfAreaInfoTable.setStatus(_A)
_OspfAreaInfoEntry_Object=MibTableRow
ospfAreaInfoEntry=_OspfAreaInfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,4,2,1))
ospfAreaInfoEntry.setIndexNames((0,_G,_A_))
if mibBuilder.loadTexts:ospfAreaInfoEntry.setStatus(_A)
_OspfAreaInfoIndex_Type=Integer32
_OspfAreaInfoIndex_Object=MibTableColumn
ospfAreaInfoIndex=_OspfAreaInfoIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,4,2,1,1),_OspfAreaInfoIndex_Type())
ospfAreaInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaInfoIndex.setStatus(_A)
_OspfTotalNumberOfInterfaces_Type=Integer32
_OspfTotalNumberOfInterfaces_Object=MibTableColumn
ospfTotalNumberOfInterfaces=_OspfTotalNumberOfInterfaces_Object((1,3,6,1,4,1,1872,2,5,3,3,4,2,1,2),_OspfTotalNumberOfInterfaces_Type())
ospfTotalNumberOfInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalNumberOfInterfaces.setStatus(_A)
_OspfNumberOfInterfacesUp_Type=Integer32
_OspfNumberOfInterfacesUp_Object=MibTableColumn
ospfNumberOfInterfacesUp=_OspfNumberOfInterfacesUp_Object((1,3,6,1,4,1,1872,2,5,3,3,4,2,1,3),_OspfNumberOfInterfacesUp_Type())
ospfNumberOfInterfacesUp.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNumberOfInterfacesUp.setStatus(_A)
_OspfNumberOfLsdbEntries_Type=Integer32
_OspfNumberOfLsdbEntries_Object=MibTableColumn
ospfNumberOfLsdbEntries=_OspfNumberOfLsdbEntries_Object((1,3,6,1,4,1,1872,2,5,3,3,4,2,1,4),_OspfNumberOfLsdbEntries_Type())
ospfNumberOfLsdbEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNumberOfLsdbEntries.setStatus(_A)
_OspfAreaInfoId_Type=IpAddress
_OspfAreaInfoId_Object=MibTableColumn
ospfAreaInfoId=_OspfAreaInfoId_Object((1,3,6,1,4,1,1872,2,5,3,3,4,2,1,5),_OspfAreaInfoId_Type())
ospfAreaInfoId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaInfoId.setStatus(_A)
_OspfIntfInfoTable_Object=MibTable
ospfIntfInfoTable=_OspfIntfInfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,4,3))
if mibBuilder.loadTexts:ospfIntfInfoTable.setStatus(_A)
_OspfIntfInfoEntry_Object=MibTableRow
ospfIntfInfoEntry=_OspfIntfInfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,4,3,1))
ospfIntfInfoEntry.setIndexNames((0,_G,_B0))
if mibBuilder.loadTexts:ospfIntfInfoEntry.setStatus(_A)
_OspfIfInfoIndex_Type=Integer32
_OspfIfInfoIndex_Object=MibTableColumn
ospfIfInfoIndex=_OspfIfInfoIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,4,3,1,1),_OspfIfInfoIndex_Type())
ospfIfInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfInfoIndex.setStatus(_A)
_OspfIfDesignatedRouterIP_Type=IpAddress
_OspfIfDesignatedRouterIP_Object=MibTableColumn
ospfIfDesignatedRouterIP=_OspfIfDesignatedRouterIP_Object((1,3,6,1,4,1,1872,2,5,3,3,4,3,1,2),_OspfIfDesignatedRouterIP_Type())
ospfIfDesignatedRouterIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfDesignatedRouterIP.setStatus(_A)
_OspfIfBackupDesignatedRouterIP_Type=IpAddress
_OspfIfBackupDesignatedRouterIP_Object=MibTableColumn
ospfIfBackupDesignatedRouterIP=_OspfIfBackupDesignatedRouterIP_Object((1,3,6,1,4,1,1872,2,5,3,3,4,3,1,3),_OspfIfBackupDesignatedRouterIP_Type())
ospfIfBackupDesignatedRouterIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfBackupDesignatedRouterIP.setStatus(_A)
_OspfIfWaitInterval_Type=Integer32
_OspfIfWaitInterval_Object=MibTableColumn
ospfIfWaitInterval=_OspfIfWaitInterval_Object((1,3,6,1,4,1,1872,2,5,3,3,4,3,1,4),_OspfIfWaitInterval_Type())
ospfIfWaitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfWaitInterval.setStatus(_A)
_OspfIfTotalNeighbours_Type=Integer32
_OspfIfTotalNeighbours_Object=MibTableColumn
ospfIfTotalNeighbours=_OspfIfTotalNeighbours_Object((1,3,6,1,4,1,1872,2,5,3,3,4,3,1,5),_OspfIfTotalNeighbours_Type())
ospfIfTotalNeighbours.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfTotalNeighbours.setStatus(_A)
_OspfIfInfoIpAddress_Type=IpAddress
_OspfIfInfoIpAddress_Object=MibTableColumn
ospfIfInfoIpAddress=_OspfIfInfoIpAddress_Object((1,3,6,1,4,1,1872,2,5,3,3,4,3,1,6),_OspfIfInfoIpAddress_Type())
ospfIfInfoIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfInfoIpAddress.setStatus(_A)
_OspfIfNbrTable_Object=MibTable
ospfIfNbrTable=_OspfIfNbrTable_Object((1,3,6,1,4,1,1872,2,5,3,3,4,5))
if mibBuilder.loadTexts:ospfIfNbrTable.setStatus(_A)
_OspfIfNbrEntry_Object=MibTableRow
ospfIfNbrEntry=_OspfIfNbrEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,4,5,1))
ospfIfNbrEntry.setIndexNames((0,_G,_B1),(0,_G,_B2))
if mibBuilder.loadTexts:ospfIfNbrEntry.setStatus(_A)
_OspfIfNbrIntfIndex_Type=Integer32
_OspfIfNbrIntfIndex_Object=MibTableColumn
ospfIfNbrIntfIndex=_OspfIfNbrIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,4,5,1,1),_OspfIfNbrIntfIndex_Type())
ospfIfNbrIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfNbrIntfIndex.setStatus(_A)
_OspfIfNbrIpAddr_Type=IpAddress
_OspfIfNbrIpAddr_Object=MibTableColumn
ospfIfNbrIpAddr=_OspfIfNbrIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,3,4,5,1,2),_OspfIfNbrIpAddr_Type())
ospfIfNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfNbrIpAddr.setStatus(_A)
_OspfIfNbrPriority_Type=Integer32
_OspfIfNbrPriority_Object=MibTableColumn
ospfIfNbrPriority=_OspfIfNbrPriority_Object((1,3,6,1,4,1,1872,2,5,3,3,4,5,1,3),_OspfIfNbrPriority_Type())
ospfIfNbrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfNbrPriority.setStatus(_A)
class _OspfIfNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('down',1),('attempt',2),('init',3),('twoway',4),('exStart',5),('exchange',6),('loading',7),('full',8)))
_OspfIfNbrState_Type.__name__=_C
_OspfIfNbrState_Object=MibTableColumn
ospfIfNbrState=_OspfIfNbrState_Object((1,3,6,1,4,1,1872,2,5,3,3,4,5,1,4),_OspfIfNbrState_Type())
ospfIfNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfNbrState.setStatus(_A)
_OspfIfNbrDesignatedRtr_Type=IpAddress
_OspfIfNbrDesignatedRtr_Object=MibTableColumn
ospfIfNbrDesignatedRtr=_OspfIfNbrDesignatedRtr_Object((1,3,6,1,4,1,1872,2,5,3,3,4,5,1,5),_OspfIfNbrDesignatedRtr_Type())
ospfIfNbrDesignatedRtr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfNbrDesignatedRtr.setStatus(_A)
_OspfIfNbrBackupDesignatedRtr_Type=IpAddress
_OspfIfNbrBackupDesignatedRtr_Object=MibTableColumn
ospfIfNbrBackupDesignatedRtr=_OspfIfNbrBackupDesignatedRtr_Object((1,3,6,1,4,1,1872,2,5,3,3,4,5,1,6),_OspfIfNbrBackupDesignatedRtr_Type())
ospfIfNbrBackupDesignatedRtr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfNbrBackupDesignatedRtr.setStatus(_A)
_OspfIfNbrIpAddress_Type=IpAddress
_OspfIfNbrIpAddress_Object=MibTableColumn
ospfIfNbrIpAddress=_OspfIfNbrIpAddress_Object((1,3,6,1,4,1,1872,2,5,3,3,4,5,1,7),_OspfIfNbrIpAddress_Type())
ospfIfNbrIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfNbrIpAddress.setStatus(_A)
_GatewayInfo_ObjectIdentity=ObjectIdentity
gatewayInfo=_GatewayInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,5))
_GatewayInfoTable_Object=MibTable
gatewayInfoTable=_GatewayInfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,5,1))
if mibBuilder.loadTexts:gatewayInfoTable.setStatus(_A)
_GatewayInfoEntry_Object=MibTableRow
gatewayInfoEntry=_GatewayInfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,5,1,1))
gatewayInfoEntry.setIndexNames((0,_G,_B3))
if mibBuilder.loadTexts:gatewayInfoEntry.setStatus(_A)
_GatewayInfoIndex_Type=Integer32
_GatewayInfoIndex_Object=MibTableColumn
gatewayInfoIndex=_GatewayInfoIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,5,1,1,1),_GatewayInfoIndex_Type())
gatewayInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayInfoIndex.setStatus(_A)
_GatewayInfoAddr_Type=IpAddress
_GatewayInfoAddr_Object=MibTableColumn
gatewayInfoAddr=_GatewayInfoAddr_Object((1,3,6,1,4,1,1872,2,5,3,3,5,1,1,2),_GatewayInfoAddr_Type())
gatewayInfoAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayInfoAddr.setStatus(_A)
_GatewayInfoVlan_Type=Integer32
_GatewayInfoVlan_Object=MibTableColumn
gatewayInfoVlan=_GatewayInfoVlan_Object((1,3,6,1,4,1,1872,2,5,3,3,5,1,1,3),_GatewayInfoVlan_Type())
gatewayInfoVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayInfoVlan.setStatus(_A)
class _GatewayInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('failed',2)))
_GatewayInfoStatus_Type.__name__=_C
_GatewayInfoStatus_Object=MibTableColumn
gatewayInfoStatus=_GatewayInfoStatus_Object((1,3,6,1,4,1,1872,2,5,3,3,5,1,1,4),_GatewayInfoStatus_Type())
gatewayInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayInfoStatus.setStatus(_A)
_GatewayInfoAddr6_Type=DisplayString
_GatewayInfoAddr6_Object=MibTableColumn
gatewayInfoAddr6=_GatewayInfoAddr6_Object((1,3,6,1,4,1,1872,2,5,3,3,5,1,1,5),_GatewayInfoAddr6_Type())
gatewayInfoAddr6.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayInfoAddr6.setStatus(_A)
_NbrcacheInfo_ObjectIdentity=ObjectIdentity
nbrcacheInfo=_NbrcacheInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,7))
_NbrcacheInfoTable_Object=MibTable
nbrcacheInfoTable=_NbrcacheInfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,7,1))
if mibBuilder.loadTexts:nbrcacheInfoTable.setStatus(_A)
_NbrcacheInfoEntry_Object=MibTableRow
nbrcacheInfoEntry=_NbrcacheInfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,7,1,1))
nbrcacheInfoEntry.setIndexNames((0,_G,_B4))
if mibBuilder.loadTexts:nbrcacheInfoEntry.setStatus(_A)
_NbrcacheInfoIndex_Type=Integer32
_NbrcacheInfoIndex_Object=MibTableColumn
nbrcacheInfoIndex=_NbrcacheInfoIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,7,1,1,1),_NbrcacheInfoIndex_Type())
nbrcacheInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoIndex.setStatus(_A)
_NbrcacheInfoDestIp_Type=DisplayString
_NbrcacheInfoDestIp_Object=MibTableColumn
nbrcacheInfoDestIp=_NbrcacheInfoDestIp_Object((1,3,6,1,4,1,1872,2,5,3,3,7,1,1,2),_NbrcacheInfoDestIp_Type())
nbrcacheInfoDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoDestIp.setStatus(_A)
class _NbrcacheInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('undef',1),('reach',2),('stale',3),('delay',4),('probe',5),('inval',6),('unknown',7),('incmp',8)))
_NbrcacheInfoState_Type.__name__=_C
_NbrcacheInfoState_Object=MibTableColumn
nbrcacheInfoState=_NbrcacheInfoState_Object((1,3,6,1,4,1,1872,2,5,3,3,7,1,1,3),_NbrcacheInfoState_Type())
nbrcacheInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoState.setStatus(_A)
class _NbrcacheInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('undef',1),(_K,2),('invalid',3),('dynamic',4),(_l,5),(_m,6)))
_NbrcacheInfoType_Type.__name__=_C
_NbrcacheInfoType_Object=MibTableColumn
nbrcacheInfoType=_NbrcacheInfoType_Object((1,3,6,1,4,1,1872,2,5,3,3,7,1,1,4),_NbrcacheInfoType_Type())
nbrcacheInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoType.setStatus(_A)
_NbrcacheInfoMacAddr_Type=PhysAddress
_NbrcacheInfoMacAddr_Object=MibTableColumn
nbrcacheInfoMacAddr=_NbrcacheInfoMacAddr_Object((1,3,6,1,4,1,1872,2,5,3,3,7,1,1,5),_NbrcacheInfoMacAddr_Type())
nbrcacheInfoMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoMacAddr.setStatus(_A)
_NbrcacheInfoVlanId_Type=Integer32
_NbrcacheInfoVlanId_Object=MibTableColumn
nbrcacheInfoVlanId=_NbrcacheInfoVlanId_Object((1,3,6,1,4,1,1872,2,5,3,3,7,1,1,6),_NbrcacheInfoVlanId_Type())
nbrcacheInfoVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoVlanId.setStatus(_A)
_NbrcacheInfoPortNum_Type=Integer32
_NbrcacheInfoPortNum_Object=MibTableColumn
nbrcacheInfoPortNum=_NbrcacheInfoPortNum_Object((1,3,6,1,4,1,1872,2,5,3,3,7,1,1,7),_NbrcacheInfoPortNum_Type())
nbrcacheInfoPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoPortNum.setStatus(_A)
class _NbrcacheClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_V,2)))
_NbrcacheClear_Type.__name__=_C
_NbrcacheClear_Object=MibScalar
nbrcacheClear=_NbrcacheClear_Object((1,3,6,1,4,1,1872,2,5,3,3,7,2),_NbrcacheClear_Type())
nbrcacheClear.setMaxAccess(_H)
if mibBuilder.loadTexts:nbrcacheClear.setStatus(_A)
_NbrcacheInfoTotDynamicEntries_Type=Integer32
_NbrcacheInfoTotDynamicEntries_Object=MibScalar
nbrcacheInfoTotDynamicEntries=_NbrcacheInfoTotDynamicEntries_Object((1,3,6,1,4,1,1872,2,5,3,3,7,3),_NbrcacheInfoTotDynamicEntries_Type())
nbrcacheInfoTotDynamicEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoTotDynamicEntries.setStatus(_A)
_NbrcacheInfoTotLocalEntries_Type=Integer32
_NbrcacheInfoTotLocalEntries_Object=MibScalar
nbrcacheInfoTotLocalEntries=_NbrcacheInfoTotLocalEntries_Object((1,3,6,1,4,1,1872,2,5,3,3,7,4),_NbrcacheInfoTotLocalEntries_Type())
nbrcacheInfoTotLocalEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoTotLocalEntries.setStatus(_A)
_NbrcacheInfoTotOtherEntries_Type=Integer32
_NbrcacheInfoTotOtherEntries_Object=MibScalar
nbrcacheInfoTotOtherEntries=_NbrcacheInfoTotOtherEntries_Object((1,3,6,1,4,1,1872,2,5,3,3,7,5),_NbrcacheInfoTotOtherEntries_Type())
nbrcacheInfoTotOtherEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nbrcacheInfoTotOtherEntries.setStatus(_A)
_IpRoute6Info_ObjectIdentity=ObjectIdentity
ipRoute6Info=_IpRoute6Info_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,8))
_IpRoute6InfoTable_Object=MibTable
ipRoute6InfoTable=_IpRoute6InfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,8,1))
if mibBuilder.loadTexts:ipRoute6InfoTable.setStatus(_A)
_IpRoute6InfoEntry_Object=MibTableRow
ipRoute6InfoEntry=_IpRoute6InfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,8,1,1))
ipRoute6InfoEntry.setIndexNames((0,_G,_B5))
if mibBuilder.loadTexts:ipRoute6InfoEntry.setStatus(_A)
_IpRoute6InfoIndx_Type=Integer32
_IpRoute6InfoIndx_Object=MibTableColumn
ipRoute6InfoIndx=_IpRoute6InfoIndx_Object((1,3,6,1,4,1,1872,2,5,3,3,8,1,1,1),_IpRoute6InfoIndx_Type())
ipRoute6InfoIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoute6InfoIndx.setStatus(_A)
_IpRoute6InfoDestIp6_Type=DisplayString
_IpRoute6InfoDestIp6_Object=MibTableColumn
ipRoute6InfoDestIp6=_IpRoute6InfoDestIp6_Object((1,3,6,1,4,1,1872,2,5,3,3,8,1,1,2),_IpRoute6InfoDestIp6_Type())
ipRoute6InfoDestIp6.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoute6InfoDestIp6.setStatus(_A)
_IpRoute6InfoInterface_Type=Integer32
_IpRoute6InfoInterface_Object=MibTableColumn
ipRoute6InfoInterface=_IpRoute6InfoInterface_Object((1,3,6,1,4,1,1872,2,5,3,3,8,1,1,3),_IpRoute6InfoInterface_Type())
ipRoute6InfoInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoute6InfoInterface.setStatus(_A)
_IpRoute6InfoNextHop_Type=DisplayString
_IpRoute6InfoNextHop_Object=MibTableColumn
ipRoute6InfoNextHop=_IpRoute6InfoNextHop_Object((1,3,6,1,4,1,1872,2,5,3,3,8,1,1,4),_IpRoute6InfoNextHop_Type())
ipRoute6InfoNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoute6InfoNextHop.setStatus(_A)
class _IpRoute6InfoProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('isis',1),('rip',2),('ospf',3),(_l,4),(_m,5),('bgp',6),('stlow',7),('ospfi',8),('ospfe',9),('ospfe2',10),('ospfa',11),('ripa',12),('bgpa',13),('igmp',14),('unknown',15),('natpt',16)))
_IpRoute6InfoProto_Type.__name__=_C
_IpRoute6InfoProto_Object=MibTableColumn
ipRoute6InfoProto=_IpRoute6InfoProto_Object((1,3,6,1,4,1,1872,2,5,3,3,8,1,1,5),_IpRoute6InfoProto_Type())
ipRoute6InfoProto.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoute6InfoProto.setStatus(_A)
_IpIntfInfo_ObjectIdentity=ObjectIdentity
ipIntfInfo=_IpIntfInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,9))
_IpIntfInfoTable_Object=MibTable
ipIntfInfoTable=_IpIntfInfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1))
if mibBuilder.loadTexts:ipIntfInfoTable.setStatus(_A)
_IntfInfoEntry_Object=MibTableRow
intfInfoEntry=_IntfInfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1,1))
intfInfoEntry.setIndexNames((0,_G,_B6))
if mibBuilder.loadTexts:intfInfoEntry.setStatus(_A)
_IntfInfoIndex_Type=Integer32
_IntfInfoIndex_Object=MibTableColumn
intfInfoIndex=_IntfInfoIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1,1,1),_IntfInfoIndex_Type())
intfInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:intfInfoIndex.setStatus(_A)
class _IntfInfoIpver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_IntfInfoIpver_Type.__name__=_C
_IntfInfoIpver_Object=MibTableColumn
intfInfoIpver=_IntfInfoIpver_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1,1,2),_IntfInfoIpver_Type())
intfInfoIpver.setMaxAccess(_B)
if mibBuilder.loadTexts:intfInfoIpver.setStatus(_A)
_IntfInfoAddr_Type=DisplayString
_IntfInfoAddr_Object=MibTableColumn
intfInfoAddr=_IntfInfoAddr_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1,1,3),_IntfInfoAddr_Type())
intfInfoAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:intfInfoAddr.setStatus(_A)
_IntfInfoNetMask_Type=DisplayString
_IntfInfoNetMask_Object=MibTableColumn
intfInfoNetMask=_IntfInfoNetMask_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1,1,4),_IntfInfoNetMask_Type())
intfInfoNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:intfInfoNetMask.setStatus(_A)
_IntfInfoBcastAddr_Type=DisplayString
_IntfInfoBcastAddr_Object=MibTableColumn
intfInfoBcastAddr=_IntfInfoBcastAddr_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1,1,5),_IntfInfoBcastAddr_Type())
intfInfoBcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:intfInfoBcastAddr.setStatus(_A)
_IntfInfoVlan_Type=Integer32
_IntfInfoVlan_Object=MibTableColumn
intfInfoVlan=_IntfInfoVlan_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1,1,6),_IntfInfoVlan_Type())
intfInfoVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:intfInfoVlan.setStatus(_A)
class _IntfInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_E,3)))
_IntfInfoStatus_Type.__name__=_C
_IntfInfoStatus_Object=MibTableColumn
intfInfoStatus=_IntfInfoStatus_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1,1,7),_IntfInfoStatus_Type())
intfInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:intfInfoStatus.setStatus(_A)
_IntfInfoLinkLocalAddr_Type=DisplayString
_IntfInfoLinkLocalAddr_Object=MibTableColumn
intfInfoLinkLocalAddr=_IntfInfoLinkLocalAddr_Object((1,3,6,1,4,1,1872,2,5,3,3,9,1,1,8),_IntfInfoLinkLocalAddr_Type())
intfInfoLinkLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:intfInfoLinkLocalAddr.setStatus(_A)
_Rip2Info_ObjectIdentity=ObjectIdentity
rip2Info=_Rip2Info_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,10))
_Rip2GeneralInfo_ObjectIdentity=ObjectIdentity
rip2GeneralInfo=_Rip2GeneralInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,10,1))
class _RipInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_RipInfoState_Type.__name__=_C
_RipInfoState_Object=MibScalar
ripInfoState=_RipInfoState_Object((1,3,6,1,4,1,1872,2,5,3,3,10,1,1),_RipInfoState_Type())
ripInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoState.setStatus(_A)
class _RipInfoUpdatePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_RipInfoUpdatePeriod_Type.__name__=_C
_RipInfoUpdatePeriod_Object=MibScalar
ripInfoUpdatePeriod=_RipInfoUpdatePeriod_Object((1,3,6,1,4,1,1872,2,5,3,3,10,1,2),_RipInfoUpdatePeriod_Type())
ripInfoUpdatePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoUpdatePeriod.setStatus(_A)
class _RipInfoVip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_RipInfoVip_Type.__name__=_C
_RipInfoVip_Object=MibScalar
ripInfoVip=_RipInfoVip_Object((1,3,6,1,4,1,1872,2,5,3,3,10,1,3),_RipInfoVip_Type())
ripInfoVip.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoVip.setStatus(_A)
class _RipInfoStaticSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_E,3)))
_RipInfoStaticSupply_Type.__name__=_C
_RipInfoStaticSupply_Object=MibScalar
ripInfoStaticSupply=_RipInfoStaticSupply_Object((1,3,6,1,4,1,1872,2,5,3,3,10,1,4),_RipInfoStaticSupply_Type())
ripInfoStaticSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoStaticSupply.setStatus(_A)
_Rip2InfoIntfTable_Object=MibTable
rip2InfoIntfTable=_Rip2InfoIntfTable_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2))
if mibBuilder.loadTexts:rip2InfoIntfTable.setStatus(_A)
_RipInfoIntfEntry_Object=MibTableRow
ripInfoIntfEntry=_RipInfoIntfEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1))
ripInfoIntfEntry.setIndexNames((0,_G,_B7))
if mibBuilder.loadTexts:ripInfoIntfEntry.setStatus(_A)
_RipInfoIntfIndex_Type=Integer32
_RipInfoIntfIndex_Object=MibTableColumn
ripInfoIntfIndex=_RipInfoIntfIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,1),_RipInfoIntfIndex_Type())
ripInfoIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfIndex.setStatus(_A)
class _RipInfoIntfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_RipInfoIntfVersion_Type.__name__=_C
_RipInfoIntfVersion_Object=MibTableColumn
ripInfoIntfVersion=_RipInfoIntfVersion_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,2),_RipInfoIntfVersion_Type())
ripInfoIntfVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfVersion.setStatus(_A)
_RipInfoIntfAddress_Type=IpAddress
_RipInfoIntfAddress_Object=MibTableColumn
ripInfoIntfAddress=_RipInfoIntfAddress_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,3),_RipInfoIntfAddress_Type())
ripInfoIntfAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfAddress.setStatus(_A)
class _RipInfoIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipInfoIntfState_Type.__name__=_C
_RipInfoIntfState_Object=MibTableColumn
ripInfoIntfState=_RipInfoIntfState_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,4),_RipInfoIntfState_Type())
ripInfoIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfState.setStatus(_A)
class _RipInfoIntfListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipInfoIntfListen_Type.__name__=_C
_RipInfoIntfListen_Object=MibTableColumn
ripInfoIntfListen=_RipInfoIntfListen_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,5),_RipInfoIntfListen_Type())
ripInfoIntfListen.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfListen.setStatus(_A)
class _RipInfoIntfTrigUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipInfoIntfTrigUpdate_Type.__name__=_C
_RipInfoIntfTrigUpdate_Object=MibTableColumn
ripInfoIntfTrigUpdate=_RipInfoIntfTrigUpdate_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,6),_RipInfoIntfTrigUpdate_Type())
ripInfoIntfTrigUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfTrigUpdate.setStatus(_A)
class _RipInfoIntfMcastUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipInfoIntfMcastUpdate_Type.__name__=_C
_RipInfoIntfMcastUpdate_Object=MibTableColumn
ripInfoIntfMcastUpdate=_RipInfoIntfMcastUpdate_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,7),_RipInfoIntfMcastUpdate_Type())
ripInfoIntfMcastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfMcastUpdate.setStatus(_A)
class _RipInfoIntfPoisonReverse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipInfoIntfPoisonReverse_Type.__name__=_C
_RipInfoIntfPoisonReverse_Object=MibTableColumn
ripInfoIntfPoisonReverse=_RipInfoIntfPoisonReverse_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,8),_RipInfoIntfPoisonReverse_Type())
ripInfoIntfPoisonReverse.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfPoisonReverse.setStatus(_A)
class _RipInfoIntfSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_RipInfoIntfSupply_Type.__name__=_C
_RipInfoIntfSupply_Object=MibTableColumn
ripInfoIntfSupply=_RipInfoIntfSupply_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,9),_RipInfoIntfSupply_Type())
ripInfoIntfSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfSupply.setStatus(_A)
class _RipInfoIntfMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_RipInfoIntfMetric_Type.__name__=_C
_RipInfoIntfMetric_Object=MibTableColumn
ripInfoIntfMetric=_RipInfoIntfMetric_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,10),_RipInfoIntfMetric_Type())
ripInfoIntfMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfMetric.setStatus(_A)
class _RipInfoIntfAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_U,2)))
_RipInfoIntfAuth_Type.__name__=_C
_RipInfoIntfAuth_Object=MibTableColumn
ripInfoIntfAuth=_RipInfoIntfAuth_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,11),_RipInfoIntfAuth_Type())
ripInfoIntfAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfAuth.setStatus(_A)
class _RipInfoIntfKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RipInfoIntfKey_Type.__name__=_I
_RipInfoIntfKey_Object=MibTableColumn
ripInfoIntfKey=_RipInfoIntfKey_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,12),_RipInfoIntfKey_Type())
ripInfoIntfKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfKey.setStatus(_A)
class _RipInfoIntfDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_j,2),(_k,3),(_J,4)))
_RipInfoIntfDefault_Type.__name__=_C
_RipInfoIntfDefault_Object=MibTableColumn
ripInfoIntfDefault=_RipInfoIntfDefault_Object((1,3,6,1,4,1,1872,2,5,3,3,10,2,1,13),_RipInfoIntfDefault_Type())
ripInfoIntfDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:ripInfoIntfDefault.setStatus(_A)
_Rip2RoutesInfo_ObjectIdentity=ObjectIdentity
rip2RoutesInfo=_Rip2RoutesInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,11))
_Rip2RoutesInfoTable_Object=MibTable
rip2RoutesInfoTable=_Rip2RoutesInfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,11,1))
if mibBuilder.loadTexts:rip2RoutesInfoTable.setStatus(_A)
_Rip2RoutesInfoEntry_Object=MibTableRow
rip2RoutesInfoEntry=_Rip2RoutesInfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,11,1,1))
rip2RoutesInfoEntry.setIndexNames((0,_G,_B8),(0,_G,_B9))
if mibBuilder.loadTexts:rip2RoutesInfoEntry.setStatus(_A)
_Rip2RoutesInfoDestIndex_Type=Integer32
_Rip2RoutesInfoDestIndex_Object=MibTableColumn
rip2RoutesInfoDestIndex=_Rip2RoutesInfoDestIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,11,1,1,1),_Rip2RoutesInfoDestIndex_Type())
rip2RoutesInfoDestIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2RoutesInfoDestIndex.setStatus(_A)
_Rip2RoutesInfoNxtHopIndex_Type=Integer32
_Rip2RoutesInfoNxtHopIndex_Object=MibTableColumn
rip2RoutesInfoNxtHopIndex=_Rip2RoutesInfoNxtHopIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,11,1,1,2),_Rip2RoutesInfoNxtHopIndex_Type())
rip2RoutesInfoNxtHopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2RoutesInfoNxtHopIndex.setStatus(_A)
_Rip2RoutesInfoDestination_Type=DisplayString
_Rip2RoutesInfoDestination_Object=MibTableColumn
rip2RoutesInfoDestination=_Rip2RoutesInfoDestination_Object((1,3,6,1,4,1,1872,2,5,3,3,11,1,1,3),_Rip2RoutesInfoDestination_Type())
rip2RoutesInfoDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2RoutesInfoDestination.setStatus(_A)
_Rip2RoutesInfoIpAddress_Type=IpAddress
_Rip2RoutesInfoIpAddress_Object=MibTableColumn
rip2RoutesInfoIpAddress=_Rip2RoutesInfoIpAddress_Object((1,3,6,1,4,1,1872,2,5,3,3,11,1,1,4),_Rip2RoutesInfoIpAddress_Type())
rip2RoutesInfoIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2RoutesInfoIpAddress.setStatus(_A)
class _Rip2RoutesInfoMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Rip2RoutesInfoMetric_Type.__name__=_C
_Rip2RoutesInfoMetric_Object=MibTableColumn
rip2RoutesInfoMetric=_Rip2RoutesInfoMetric_Object((1,3,6,1,4,1,1872,2,5,3,3,11,1,1,5),_Rip2RoutesInfoMetric_Type())
rip2RoutesInfoMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2RoutesInfoMetric.setStatus(_A)
_AllowedNwInfo_ObjectIdentity=ObjectIdentity
allowedNwInfo=_AllowedNwInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,3,12))
_AllowedNwInfoTable_Object=MibTable
allowedNwInfoTable=_AllowedNwInfoTable_Object((1,3,6,1,4,1,1872,2,5,3,3,12,1))
if mibBuilder.loadTexts:allowedNwInfoTable.setStatus(_A)
_AllowedNwInfoEntry_Object=MibTableRow
allowedNwInfoEntry=_AllowedNwInfoEntry_Object((1,3,6,1,4,1,1872,2,5,3,3,12,1,1))
allowedNwInfoEntry.setIndexNames((0,_G,_BA))
if mibBuilder.loadTexts:allowedNwInfoEntry.setStatus(_A)
_AllowedNwInfoIndex_Type=Integer32
_AllowedNwInfoIndex_Object=MibTableColumn
allowedNwInfoIndex=_AllowedNwInfoIndex_Object((1,3,6,1,4,1,1872,2,5,3,3,12,1,1,1),_AllowedNwInfoIndex_Type())
allowedNwInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:allowedNwInfoIndex.setStatus(_A)
class _AllowedNwInfoIpver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_AllowedNwInfoIpver_Type.__name__=_C
_AllowedNwInfoIpver_Object=MibTableColumn
allowedNwInfoIpver=_AllowedNwInfoIpver_Object((1,3,6,1,4,1,1872,2,5,3,3,12,1,1,2),_AllowedNwInfoIpver_Type())
allowedNwInfoIpver.setMaxAccess(_B)
if mibBuilder.loadTexts:allowedNwInfoIpver.setStatus(_A)
_AllowedNwInfoVlan_Type=Integer32
_AllowedNwInfoVlan_Object=MibTableColumn
allowedNwInfoVlan=_AllowedNwInfoVlan_Object((1,3,6,1,4,1,1872,2,5,3,3,12,1,1,3),_AllowedNwInfoVlan_Type())
allowedNwInfoVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:allowedNwInfoVlan.setStatus(_A)
_AllowedNwInfoBeginIpAddr_Type=DisplayString
_AllowedNwInfoBeginIpAddr_Object=MibTableColumn
allowedNwInfoBeginIpAddr=_AllowedNwInfoBeginIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,3,12,1,1,4),_AllowedNwInfoBeginIpAddr_Type())
allowedNwInfoBeginIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:allowedNwInfoBeginIpAddr.setStatus(_A)
_AllowedNwInfoEndIpAddr_Type=DisplayString
_AllowedNwInfoEndIpAddr_Object=MibTableColumn
allowedNwInfoEndIpAddr=_AllowedNwInfoEndIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,3,12,1,1,5),_AllowedNwInfoEndIpAddr_Type())
allowedNwInfoEndIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:allowedNwInfoEndIpAddr.setStatus(_A)
_AllowedNwInfoNetMask_Type=DisplayString
_AllowedNwInfoNetMask_Object=MibTableColumn
allowedNwInfoNetMask=_AllowedNwInfoNetMask_Object((1,3,6,1,4,1,1872,2,5,3,3,12,1,1,6),_AllowedNwInfoNetMask_Type())
allowedNwInfoNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:allowedNwInfoNetMask.setStatus(_A)
_AllowedNwInfoIp6Prefix_Type=Integer32
_AllowedNwInfoIp6Prefix_Object=MibTableColumn
allowedNwInfoIp6Prefix=_AllowedNwInfoIp6Prefix_Object((1,3,6,1,4,1,1872,2,5,3,3,12,1,1,7),_AllowedNwInfoIp6Prefix_Type())
allowedNwInfoIp6Prefix.setMaxAccess(_B)
if mibBuilder.loadTexts:allowedNwInfoIp6Prefix.setStatus(_A)
_Layer3Oper_ObjectIdentity=ObjectIdentity
layer3Oper=_Layer3Oper_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,4))
_VrrpOper_ObjectIdentity=ObjectIdentity
vrrpOper=_VrrpOper_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,4,1))
_VrrpOperVirtRtrTable_Object=MibTable
vrrpOperVirtRtrTable=_VrrpOperVirtRtrTable_Object((1,3,6,1,4,1,1872,2,5,3,4,1,1))
if mibBuilder.loadTexts:vrrpOperVirtRtrTable.setStatus(_A)
_VrrpOperVirtRtrEntry_Object=MibTableRow
vrrpOperVirtRtrEntry=_VrrpOperVirtRtrEntry_Object((1,3,6,1,4,1,1872,2,5,3,4,1,1,1))
vrrpOperVirtRtrEntry.setIndexNames((0,_G,_BB))
if mibBuilder.loadTexts:vrrpOperVirtRtrEntry.setStatus(_A)
_VrrpOperVirtRtrIndex_Type=Integer32
_VrrpOperVirtRtrIndex_Object=MibTableColumn
vrrpOperVirtRtrIndex=_VrrpOperVirtRtrIndex_Object((1,3,6,1,4,1,1872,2,5,3,4,1,1,1,1),_VrrpOperVirtRtrIndex_Type())
vrrpOperVirtRtrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpOperVirtRtrIndex.setStatus(_A)
class _VrrpOperVirtRtrBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_n,2)))
_VrrpOperVirtRtrBackup_Type.__name__=_C
_VrrpOperVirtRtrBackup_Object=MibTableColumn
vrrpOperVirtRtrBackup=_VrrpOperVirtRtrBackup_Object((1,3,6,1,4,1,1872,2,5,3,4,1,1,1,2),_VrrpOperVirtRtrBackup_Type())
vrrpOperVirtRtrBackup.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpOperVirtRtrBackup.setStatus(_A)
class _VrrpOperVirtRtrGroupBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_n,2)))
_VrrpOperVirtRtrGroupBackup_Type.__name__=_C
_VrrpOperVirtRtrGroupBackup_Object=MibScalar
vrrpOperVirtRtrGroupBackup=_VrrpOperVirtRtrGroupBackup_Object((1,3,6,1,4,1,1872,2,5,3,4,1,2),_VrrpOperVirtRtrGroupBackup_Type())
vrrpOperVirtRtrGroupBackup.setMaxAccess(_H)
if mibBuilder.loadTexts:vrrpOperVirtRtrGroupBackup.setStatus(_A)
_IpOper_ObjectIdentity=ObjectIdentity
ipOper=_IpOper_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,4,2))
_BgpOper_ObjectIdentity=ObjectIdentity
bgpOper=_BgpOper_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,4,2,1))
_BgpOperStart_ObjectIdentity=ObjectIdentity
bgpOperStart=_BgpOperStart_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,4,2,1,1))
class _BgpOperStartPeerNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BgpOperStartPeerNum_Type.__name__=_C
_BgpOperStartPeerNum_Object=MibScalar
bgpOperStartPeerNum=_BgpOperStartPeerNum_Object((1,3,6,1,4,1,1872,2,5,3,4,2,1,1,1),_BgpOperStartPeerNum_Type())
bgpOperStartPeerNum.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpOperStartPeerNum.setStatus(_A)
class _BgpOperStartSess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),('start',2)))
_BgpOperStartSess_Type.__name__=_C
_BgpOperStartSess_Object=MibScalar
bgpOperStartSess=_BgpOperStartSess_Object((1,3,6,1,4,1,1872,2,5,3,4,2,1,1,2),_BgpOperStartSess_Type())
bgpOperStartSess.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpOperStartSess.setStatus(_A)
_BgpOperStop_ObjectIdentity=ObjectIdentity
bgpOperStop=_BgpOperStop_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,4,2,1,2))
class _BgpOperStopPeerNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BgpOperStopPeerNum_Type.__name__=_C
_BgpOperStopPeerNum_Object=MibScalar
bgpOperStopPeerNum=_BgpOperStopPeerNum_Object((1,3,6,1,4,1,1872,2,5,3,4,2,1,2,1),_BgpOperStopPeerNum_Type())
bgpOperStopPeerNum.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpOperStopPeerNum.setStatus(_A)
class _BgpOperStopSess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),('stop',2)))
_BgpOperStopSess_Type.__name__=_C
_BgpOperStopSess_Object=MibScalar
bgpOperStopSess=_BgpOperStopSess_Object((1,3,6,1,4,1,1872,2,5,3,4,2,1,2,2),_BgpOperStopSess_Type())
bgpOperStopSess.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpOperStopSess.setStatus(_A)
_GarpOper_ObjectIdentity=ObjectIdentity
garpOper=_GarpOper_ObjectIdentity((1,3,6,1,4,1,1872,2,5,3,4,2,2))
_GarpOperIpAddr_Type=IpAddress
_GarpOperIpAddr_Object=MibScalar
garpOperIpAddr=_GarpOperIpAddr_Object((1,3,6,1,4,1,1872,2,5,3,4,2,2,1),_GarpOperIpAddr_Type())
garpOperIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:garpOperIpAddr.setStatus(_A)
class _GarpOperVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4090))
_GarpOperVlanNumber_Type.__name__=_C
_GarpOperVlanNumber_Object=MibScalar
garpOperVlanNumber=_GarpOperVlanNumber_Object((1,3,6,1,4,1,1872,2,5,3,4,2,2,2),_GarpOperVlanNumber_Type())
garpOperVlanNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:garpOperVlanNumber.setStatus(_A)
class _GarpOperSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('send',2),('error',3)))
_GarpOperSend_Type.__name__=_C
_GarpOperSend_Object=MibScalar
garpOperSend=_GarpOperSend_Object((1,3,6,1,4,1,1872,2,5,3,4,2,2,3),_GarpOperSend_Type())
garpOperSend.setMaxAccess(_H)
if mibBuilder.loadTexts:garpOperSend.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'layer3':layer3,'layer3Configs':layer3Configs,'ipInterfaceCfg':ipInterfaceCfg,'ipInterfaceTableMax':ipInterfaceTableMax,'ipCurCfgIntfTable':ipCurCfgIntfTable,'ipCurCfgIntfEntry':ipCurCfgIntfEntry,_o:ipCurCfgIntfIndex,'ipCurCfgIntfAddr':ipCurCfgIntfAddr,'ipCurCfgIntfMask':ipCurCfgIntfMask,'ipCurCfgIntfBroadcast':ipCurCfgIntfBroadcast,'ipCurCfgIntfVlan':ipCurCfgIntfVlan,'ipCurCfgIntfState':ipCurCfgIntfState,'ipCurCfgIntfBootpRelay':ipCurCfgIntfBootpRelay,'ipCurCfgIntfIpVer':ipCurCfgIntfIpVer,'ipCurCfgIntfIpv6Addr':ipCurCfgIntfIpv6Addr,'ipCurCfgIntfPrefixLen':ipCurCfgIntfPrefixLen,'ipCurCfgIntfRouteAdv':ipCurCfgIntfRouteAdv,'ipNewCfgIntfTable':ipNewCfgIntfTable,'ipNewCfgIntfEntry':ipNewCfgIntfEntry,_p:ipNewCfgIntfIndex,'ipNewCfgIntfAddr':ipNewCfgIntfAddr,'ipNewCfgIntfMask':ipNewCfgIntfMask,'ipNewCfgIntfBroadcast':ipNewCfgIntfBroadcast,'ipNewCfgIntfVlan':ipNewCfgIntfVlan,'ipNewCfgIntfState':ipNewCfgIntfState,'ipNewCfgIntfDelete':ipNewCfgIntfDelete,'ipNewCfgIntfBootpRelay':ipNewCfgIntfBootpRelay,'ipNewCfgIntfIpVer':ipNewCfgIntfIpVer,'ipNewCfgIntfIpv6Addr':ipNewCfgIntfIpv6Addr,'ipNewCfgIntfPrefixLen':ipNewCfgIntfPrefixLen,'ipNewCfgIntfRouteAdv':ipNewCfgIntfRouteAdv,'ipGatewayCfg':ipGatewayCfg,'ipCurCfgGwMetric':ipCurCfgGwMetric,'ipNewCfgGwMetric':ipNewCfgGwMetric,'ipGatewayTableMax':ipGatewayTableMax,'ipCurCfgGwTable':ipCurCfgGwTable,'ipCurCfgGwEntry':ipCurCfgGwEntry,_s:ipCurCfgGwIndex,'ipCurCfgGwAddr':ipCurCfgGwAddr,'ipCurCfgGwInterval':ipCurCfgGwInterval,'ipCurCfgGwRetry':ipCurCfgGwRetry,'ipCurCfgGwState':ipCurCfgGwState,'ipCurCfgGwArp':ipCurCfgGwArp,'ipCurCfgGwVlan':ipCurCfgGwVlan,'ipCurCfgGwPriority':ipCurCfgGwPriority,'ipCurCfgGwIpVer':ipCurCfgGwIpVer,'ipCurCfgGwIpv6Addr':ipCurCfgGwIpv6Addr,'ipNewCfgGwTable':ipNewCfgGwTable,'ipNewCfgGwEntry':ipNewCfgGwEntry,_t:ipNewCfgGwIndex,'ipNewCfgGwAddr':ipNewCfgGwAddr,'ipNewCfgGwInterval':ipNewCfgGwInterval,'ipNewCfgGwRetry':ipNewCfgGwRetry,'ipNewCfgGwState':ipNewCfgGwState,'ipNewCfgGwDelete':ipNewCfgGwDelete,'ipNewCfgGwArp':ipNewCfgGwArp,'ipNewCfgGwVlan':ipNewCfgGwVlan,'ipNewCfgGwPriority':ipNewCfgGwPriority,'ipNewCfgGwIpVer':ipNewCfgGwIpVer,'ipNewCfgGwIpv6Addr':ipNewCfgGwIpv6Addr,'ipStaticRouteCfg':ipStaticRouteCfg,'ipStaticRouteTableMaxSize':ipStaticRouteTableMaxSize,'ipCurCfgStaticRouteTable':ipCurCfgStaticRouteTable,'ipCurCfgStaticRouteEntry':ipCurCfgStaticRouteEntry,_u:ipCurCfgStaticRouteIndx,'ipCurCfgStaticRouteDestIp':ipCurCfgStaticRouteDestIp,'ipCurCfgStaticRouteMask':ipCurCfgStaticRouteMask,'ipCurCfgStaticRouteGateway':ipCurCfgStaticRouteGateway,'ipCurCfgStaticRouteInterface':ipCurCfgStaticRouteInterface,'ipNewCfgStaticRouteTable':ipNewCfgStaticRouteTable,'ipNewCfgStaticRouteEntry':ipNewCfgStaticRouteEntry,_v:ipNewCfgStaticRouteIndx,'ipNewCfgStaticRouteDestIp':ipNewCfgStaticRouteDestIp,'ipNewCfgStaticRouteMask':ipNewCfgStaticRouteMask,'ipNewCfgStaticRouteGateway':ipNewCfgStaticRouteGateway,'ipNewCfgStaticRouteAction':ipNewCfgStaticRouteAction,'ipNewCfgStaticRouteInterface':ipNewCfgStaticRouteInterface,'ipv6CurCfgStaticRouteTable':ipv6CurCfgStaticRouteTable,'ipv6CurCfgStaticRouteEntry':ipv6CurCfgStaticRouteEntry,_w:ipv6CurCfgStaticRouteIndx,'ipv6CurCfgStaticRouteDestIp':ipv6CurCfgStaticRouteDestIp,'ipv6CurCfgStaticRouteMask':ipv6CurCfgStaticRouteMask,'ipv6CurCfgStaticRouteGateway':ipv6CurCfgStaticRouteGateway,'ipv6CurCfgStaticRouteInterface':ipv6CurCfgStaticRouteInterface,'ipv6NewCfgStaticRouteTable':ipv6NewCfgStaticRouteTable,'ipv6NewCfgStaticRouteEntry':ipv6NewCfgStaticRouteEntry,_x:ipv6NewCfgStaticRouteIndx,'ipv6NewCfgStaticRouteDestIp':ipv6NewCfgStaticRouteDestIp,'ipv6NewCfgStaticRouteMask':ipv6NewCfgStaticRouteMask,'ipv6NewCfgStaticRouteGateway':ipv6NewCfgStaticRouteGateway,'ipv6NewCfgStaticRouteAction':ipv6NewCfgStaticRouteAction,'ipv6NewCfgStaticRouteInterface':ipv6NewCfgStaticRouteInterface,'ipForwardCfg':ipForwardCfg,'ipFwdGeneralCfg':ipFwdGeneralCfg,'ipFwdCurCfgState':ipFwdCurCfgState,'ipFwdNewCfgState':ipFwdNewCfgState,'ipFwdCurCfgDirectedBcast':ipFwdCurCfgDirectedBcast,'ipFwdNewCfgDirectedBcast':ipFwdNewCfgDirectedBcast,'ipFwdCurCfgNoICMPRedirect':ipFwdCurCfgNoICMPRedirect,'ipFwdNewCfgNoICMPRedirect':ipFwdNewCfgNoICMPRedirect,'ipFwdCurCfgRtCache':ipFwdCurCfgRtCache,'ipFwdNewCfgRtCache':ipFwdNewCfgRtCache,'ipFwdPortTableMaxSize':ipFwdPortTableMaxSize,'ipFwdCurCfgPortTable':ipFwdCurCfgPortTable,'ipFwdCurCfgPortEntry':ipFwdCurCfgPortEntry,_y:ipFwdCurCfgPortIndex,'ipFwdCurCfgPortState':ipFwdCurCfgPortState,'ipFwdNewCfgPortTable':ipFwdNewCfgPortTable,'ipFwdNewCfgPortEntry':ipFwdNewCfgPortEntry,_z:ipFwdNewCfgPortIndex,'ipFwdNewCfgPortState':ipFwdNewCfgPortState,'ipFwdLocalTableMaxSize':ipFwdLocalTableMaxSize,'ipFwdCurCfgLocalTable':ipFwdCurCfgLocalTable,'ipFwdCurCfgLocalEntry':ipFwdCurCfgLocalEntry,_A0:ipFwdCurCfgLocalIndex,'ipFwdCurCfgLocalSubnet':ipFwdCurCfgLocalSubnet,'ipFwdCurCfgLocalMask':ipFwdCurCfgLocalMask,'ipFwdNewCfgLocalTable':ipFwdNewCfgLocalTable,'ipFwdNewCfgLocalEntry':ipFwdNewCfgLocalEntry,_A1:ipFwdNewCfgLocalIndex,'ipFwdNewCfgLocalSubnet':ipFwdNewCfgLocalSubnet,'ipFwdNewCfgLocalMask':ipFwdNewCfgLocalMask,'ipFwdNewCfgLocalDelete':ipFwdNewCfgLocalDelete,'vrrpCfg':vrrpCfg,'vrrpGeneral':vrrpGeneral,'vrrpCurCfgGenState':vrrpCurCfgGenState,'vrrpNewCfgGenState':vrrpNewCfgGenState,'vrrpCurCfgGenTckVirtRtrInc':vrrpCurCfgGenTckVirtRtrInc,'vrrpNewCfgGenTckVirtRtrInc':vrrpNewCfgGenTckVirtRtrInc,'vrrpCurCfgGenTckIpIntfInc':vrrpCurCfgGenTckIpIntfInc,'vrrpNewCfgGenTckIpIntfInc':vrrpNewCfgGenTckIpIntfInc,'vrrpCurCfgGenTckVlanPortInc':vrrpCurCfgGenTckVlanPortInc,'vrrpNewCfgGenTckVlanPortInc':vrrpNewCfgGenTckVlanPortInc,'vrrpCurCfgGenTckL4PortInc':vrrpCurCfgGenTckL4PortInc,'vrrpNewCfgGenTckL4PortInc':vrrpNewCfgGenTckL4PortInc,'vrrpCurCfgGenTckRServerInc':vrrpCurCfgGenTckRServerInc,'vrrpNewCfgGenTckRServerInc':vrrpNewCfgGenTckRServerInc,'vrrpCurCfgGenTckHsrpInc':vrrpCurCfgGenTckHsrpInc,'vrrpNewCfgGenTckHsrpInc':vrrpNewCfgGenTckHsrpInc,'vrrpCurCfgGenHotstandby':vrrpCurCfgGenHotstandby,'vrrpNewCfgGenHotstandby':vrrpNewCfgGenHotstandby,'vrrpCurCfgGenTckHsrvInc':vrrpCurCfgGenTckHsrvInc,'vrrpNewCfgGenTckHsrvInc':vrrpNewCfgGenTckHsrvInc,'vrrpCurCfgGenHoldoff':vrrpCurCfgGenHoldoff,'vrrpNewCfgGenHoldoff':vrrpNewCfgGenHoldoff,'vrrpVirtRtrTableMaxSize':vrrpVirtRtrTableMaxSize,'vrrpCurCfgVirtRtrTable':vrrpCurCfgVirtRtrTable,'vrrpCurCfgVirtRtrTableEntry':vrrpCurCfgVirtRtrTableEntry,_A2:vrrpCurCfgVirtRtrIndx,'vrrpCurCfgVirtRtrID':vrrpCurCfgVirtRtrID,'vrrpCurCfgVirtRtrAddr':vrrpCurCfgVirtRtrAddr,'vrrpCurCfgVirtRtrIfIndex':vrrpCurCfgVirtRtrIfIndex,'vrrpCurCfgVirtRtrInterval':vrrpCurCfgVirtRtrInterval,'vrrpCurCfgVirtRtrPriority':vrrpCurCfgVirtRtrPriority,'vrrpCurCfgVirtRtrPreempt':vrrpCurCfgVirtRtrPreempt,'vrrpCurCfgVirtRtrState':vrrpCurCfgVirtRtrState,'vrrpCurCfgVirtRtrSharing':vrrpCurCfgVirtRtrSharing,'vrrpCurCfgVirtRtrTckVirtRtr':vrrpCurCfgVirtRtrTckVirtRtr,'vrrpCurCfgVirtRtrTckIpIntf':vrrpCurCfgVirtRtrTckIpIntf,'vrrpCurCfgVirtRtrTckVlanPort':vrrpCurCfgVirtRtrTckVlanPort,'vrrpCurCfgVirtRtrTckL4Port':vrrpCurCfgVirtRtrTckL4Port,'vrrpCurCfgVirtRtrTckRServer':vrrpCurCfgVirtRtrTckRServer,'vrrpCurCfgVirtRtrTckHsrp':vrrpCurCfgVirtRtrTckHsrp,'vrrpCurCfgVirtRtrTckHsrv':vrrpCurCfgVirtRtrTckHsrv,'vrrpCurCfgVirtRtrVersion':vrrpCurCfgVirtRtrVersion,'vrrpCurCfgVirtRtrIpv6Addr':vrrpCurCfgVirtRtrIpv6Addr,'vrrpCurCfgVirtRtrIpv6Interval':vrrpCurCfgVirtRtrIpv6Interval,'vrrpNewCfgVirtRtrTable':vrrpNewCfgVirtRtrTable,'vrrpNewCfgVirtRtrTableEntry':vrrpNewCfgVirtRtrTableEntry,_A3:vrrpNewCfgVirtRtrIndx,'vrrpNewCfgVirtRtrID':vrrpNewCfgVirtRtrID,'vrrpNewCfgVirtRtrAddr':vrrpNewCfgVirtRtrAddr,'vrrpNewCfgVirtRtrIfIndex':vrrpNewCfgVirtRtrIfIndex,'vrrpNewCfgVirtRtrInterval':vrrpNewCfgVirtRtrInterval,'vrrpNewCfgVirtRtrPriority':vrrpNewCfgVirtRtrPriority,'vrrpNewCfgVirtRtrPreempt':vrrpNewCfgVirtRtrPreempt,'vrrpNewCfgVirtRtrState':vrrpNewCfgVirtRtrState,'vrrpNewCfgVirtRtrDelete':vrrpNewCfgVirtRtrDelete,'vrrpNewCfgVirtRtrSharing':vrrpNewCfgVirtRtrSharing,'vrrpNewCfgVirtRtrTckVirtRtr':vrrpNewCfgVirtRtrTckVirtRtr,'vrrpNewCfgVirtRtrTckIpIntf':vrrpNewCfgVirtRtrTckIpIntf,'vrrpNewCfgVirtRtrTckVlanPort':vrrpNewCfgVirtRtrTckVlanPort,'vrrpNewCfgVirtRtrTckL4Port':vrrpNewCfgVirtRtrTckL4Port,'vrrpNewCfgVirtRtrTckRServer':vrrpNewCfgVirtRtrTckRServer,'vrrpNewCfgVirtRtrTckHsrp':vrrpNewCfgVirtRtrTckHsrp,'vrrpNewCfgVirtRtrTckHsrv':vrrpNewCfgVirtRtrTckHsrv,'vrrpNewCfgVirtRtrVersion':vrrpNewCfgVirtRtrVersion,'vrrpNewCfgVirtRtrIpv6Addr':vrrpNewCfgVirtRtrIpv6Addr,'vrrpNewCfgVirtRtrIpv6Interval':vrrpNewCfgVirtRtrIpv6Interval,'vrrpIfTableMaxSize':vrrpIfTableMaxSize,'vrrpCurCfgIfTable':vrrpCurCfgIfTable,'vrrpCurCfgIfTableEntry':vrrpCurCfgIfTableEntry,_A4:vrrpCurCfgIfIndx,'vrrpCurCfgIfAuthType':vrrpCurCfgIfAuthType,'vrrpCurCfgIfPasswd':vrrpCurCfgIfPasswd,'vrrpCurCfgIfIpAddr':vrrpCurCfgIfIpAddr,'vrrpNewCfgIfTable':vrrpNewCfgIfTable,'vrrpNewCfgIfTableEntry':vrrpNewCfgIfTableEntry,_A6:vrrpNewCfgIfIndx,'vrrpNewCfgIfAuthType':vrrpNewCfgIfAuthType,'vrrpNewCfgIfPasswd':vrrpNewCfgIfPasswd,'vrrpNewCfgIfDelete':vrrpNewCfgIfDelete,'vrrpVirtRtrGrpTableMaxSize':vrrpVirtRtrGrpTableMaxSize,'vrrpCurCfgVirtRtrGrpTable':vrrpCurCfgVirtRtrGrpTable,'vrrpCurCfgVirtRtrGrpTableEntry':vrrpCurCfgVirtRtrGrpTableEntry,_A7:vrrpCurCfgVirtRtrGrpIndx,'vrrpCurCfgVirtRtrGrpID':vrrpCurCfgVirtRtrGrpID,'vrrpCurCfgVirtRtrGrpIfIndex':vrrpCurCfgVirtRtrGrpIfIndex,'vrrpCurCfgVirtRtrGrpInterval':vrrpCurCfgVirtRtrGrpInterval,'vrrpCurCfgVirtRtrGrpPriority':vrrpCurCfgVirtRtrGrpPriority,'vrrpCurCfgVirtRtrGrpPreempt':vrrpCurCfgVirtRtrGrpPreempt,'vrrpCurCfgVirtRtrGrpState':vrrpCurCfgVirtRtrGrpState,'vrrpCurCfgVirtRtrGrpSharing':vrrpCurCfgVirtRtrGrpSharing,'vrrpCurCfgVirtRtrGrpTckVirtRtr':vrrpCurCfgVirtRtrGrpTckVirtRtr,'vrrpCurCfgVirtRtrGrpTckIpIntf':vrrpCurCfgVirtRtrGrpTckIpIntf,'vrrpCurCfgVirtRtrGrpTckVlanPort':vrrpCurCfgVirtRtrGrpTckVlanPort,'vrrpCurCfgVirtRtrGrpTckL4Port':vrrpCurCfgVirtRtrGrpTckL4Port,'vrrpCurCfgVirtRtrGrpTckRServer':vrrpCurCfgVirtRtrGrpTckRServer,'vrrpCurCfgVirtRtrGrpTckHsrp':vrrpCurCfgVirtRtrGrpTckHsrp,'vrrpCurCfgVirtRtrGrpTckHsrv':vrrpCurCfgVirtRtrGrpTckHsrv,'vrrpCurCfgVirtRtrGrpVersion':vrrpCurCfgVirtRtrGrpVersion,'vrrpCurCfgVirtRtrGrpIpv6Interval':vrrpCurCfgVirtRtrGrpIpv6Interval,'vrrpNewCfgVirtRtrGrpTable':vrrpNewCfgVirtRtrGrpTable,'vrrpNewCfgVirtRtrGrpTableEntry':vrrpNewCfgVirtRtrGrpTableEntry,_A8:vrrpNewCfgVirtRtrGrpIndx,'vrrpNewCfgVirtRtrGrpID':vrrpNewCfgVirtRtrGrpID,'vrrpNewCfgVirtRtrGrpIfIndex':vrrpNewCfgVirtRtrGrpIfIndex,'vrrpNewCfgVirtRtrGrpInterval':vrrpNewCfgVirtRtrGrpInterval,'vrrpNewCfgVirtRtrGrpPriority':vrrpNewCfgVirtRtrGrpPriority,'vrrpNewCfgVirtRtrGrpPreempt':vrrpNewCfgVirtRtrGrpPreempt,'vrrpNewCfgVirtRtrGrpState':vrrpNewCfgVirtRtrGrpState,'vrrpNewCfgVirtRtrGrpDelete':vrrpNewCfgVirtRtrGrpDelete,'vrrpNewCfgVirtRtrGrpSharing':vrrpNewCfgVirtRtrGrpSharing,'vrrpNewCfgVirtRtrGrpTckVirtRtr':vrrpNewCfgVirtRtrGrpTckVirtRtr,'vrrpNewCfgVirtRtrGrpTckIpIntf':vrrpNewCfgVirtRtrGrpTckIpIntf,'vrrpNewCfgVirtRtrGrpTckVlanPort':vrrpNewCfgVirtRtrGrpTckVlanPort,'vrrpNewCfgVirtRtrGrpTckL4Port':vrrpNewCfgVirtRtrGrpTckL4Port,'vrrpNewCfgVirtRtrGrpTckRServer':vrrpNewCfgVirtRtrGrpTckRServer,'vrrpNewCfgVirtRtrGrpTckHsrp':vrrpNewCfgVirtRtrGrpTckHsrp,'vrrpNewCfgVirtRtrGrpTckHsrv':vrrpNewCfgVirtRtrGrpTckHsrv,'vrrpNewCfgVirtRtrGrpVersion':vrrpNewCfgVirtRtrGrpVersion,'vrrpNewCfgVirtRtrGrpIpv6Interval':vrrpNewCfgVirtRtrGrpIpv6Interval,'vrrpVirtRtrVrGrpTableMaxSize':vrrpVirtRtrVrGrpTableMaxSize,'vrrpCurCfgVirtRtrVrGrpTable':vrrpCurCfgVirtRtrVrGrpTable,'vrrpCurCfgVirtRtrVrGrpTableEntry':vrrpCurCfgVirtRtrVrGrpTableEntry,_A9:vrrpCurCfgVirtRtrVrGrpIndx,'vrrpCurCfgVirtRtrVrGrpName':vrrpCurCfgVirtRtrVrGrpName,'vrrpCurCfgVirtRtrVrGrpState':vrrpCurCfgVirtRtrVrGrpState,'vrrpCurCfgVirtRtrVrGrpBmap':vrrpCurCfgVirtRtrVrGrpBmap,'vrrpCurCfgVirtRtrVrGrpPriority':vrrpCurCfgVirtRtrVrGrpPriority,'vrrpCurCfgVirtRtrVrGrpTckIpIntf':vrrpCurCfgVirtRtrVrGrpTckIpIntf,'vrrpCurCfgVirtRtrVrGrpTckVlanPort':vrrpCurCfgVirtRtrVrGrpTckVlanPort,'vrrpCurCfgVirtRtrVrGrpTckL4Port':vrrpCurCfgVirtRtrVrGrpTckL4Port,'vrrpCurCfgVirtRtrVrGrpTckRServer':vrrpCurCfgVirtRtrVrGrpTckRServer,'vrrpCurCfgVirtRtrVrGrpTckHsrp':vrrpCurCfgVirtRtrVrGrpTckHsrp,'vrrpCurCfgVirtRtrVrGrpTckHsrv':vrrpCurCfgVirtRtrVrGrpTckHsrv,'vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo':vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo,'vrrpCurCfgVirtRtrVrGrpAdd':vrrpCurCfgVirtRtrVrGrpAdd,'vrrpCurCfgVirtRtrVrGrpAdverInterval':vrrpCurCfgVirtRtrVrGrpAdverInterval,'vrrpCurCfgVirtRtrVrGrpPreemption':vrrpCurCfgVirtRtrVrGrpPreemption,'vrrpCurCfgVirtRtrVrGrpSharing':vrrpCurCfgVirtRtrVrGrpSharing,'vrrpNewCfgVirtRtrVrGrpTable':vrrpNewCfgVirtRtrVrGrpTable,'vrrpNewCfgVirtRtrVrGrpTableEntry':vrrpNewCfgVirtRtrVrGrpTableEntry,_AA:vrrpNewCfgVirtRtrVrGrpIndx,'vrrpNewCfgVirtRtrVrGrpName':vrrpNewCfgVirtRtrVrGrpName,'vrrpNewCfgVirtRtrVrGrpAdd':vrrpNewCfgVirtRtrVrGrpAdd,'vrrpNewCfgVirtRtrVrGrpRem':vrrpNewCfgVirtRtrVrGrpRem,'vrrpNewCfgVirtRtrVrGrpState':vrrpNewCfgVirtRtrVrGrpState,'vrrpNewCfgVirtRtrVrGrpDelete':vrrpNewCfgVirtRtrVrGrpDelete,'vrrpNewCfgVirtRtrVrGrpBmap':vrrpNewCfgVirtRtrVrGrpBmap,'vrrpNewCfgVirtRtrVrGrpPriority':vrrpNewCfgVirtRtrVrGrpPriority,'vrrpNewCfgVirtRtrVrGrpTckIpIntf':vrrpNewCfgVirtRtrVrGrpTckIpIntf,'vrrpNewCfgVirtRtrVrGrpTckVlanPort':vrrpNewCfgVirtRtrVrGrpTckVlanPort,'vrrpNewCfgVirtRtrVrGrpTckL4Port':vrrpNewCfgVirtRtrVrGrpTckL4Port,'vrrpNewCfgVirtRtrVrGrpTckRServer':vrrpNewCfgVirtRtrVrGrpTckRServer,'vrrpNewCfgVirtRtrVrGrpTckHsrp':vrrpNewCfgVirtRtrVrGrpTckHsrp,'vrrpNewCfgVirtRtrVrGrpTckHsrv':vrrpNewCfgVirtRtrVrGrpTckHsrv,'vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo':vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo,'vrrpNewCfgVirtRtrVrGrpAdverInterval':vrrpNewCfgVirtRtrVrGrpAdverInterval,'vrrpNewCfgVirtRtrVrGrpPreemption':vrrpNewCfgVirtRtrVrGrpPreemption,'vrrpNewCfgVirtRtrVrGrpSharing':vrrpNewCfgVirtRtrVrGrpSharing,'arpCfg':arpCfg,'arpCurCfgReARPPeriod':arpCurCfgReARPPeriod,'arpNewCfgReARPPeriod':arpNewCfgReARPPeriod,'ipBootpCfg':ipBootpCfg,'ipCurCfgBootpAddr':ipCurCfgBootpAddr,'ipNewCfgBootpAddr':ipNewCfgBootpAddr,'ipCurCfgBootpAddr2':ipCurCfgBootpAddr2,'ipNewCfgBootpAddr2':ipNewCfgBootpAddr2,'ipCurCfgBootpState':ipCurCfgBootpState,'ipNewCfgBootpState':ipNewCfgBootpState,'dnsCfg':dnsCfg,'dnsCurCfgPrimaryIpAddr':dnsCurCfgPrimaryIpAddr,'dnsNewCfgPrimaryIpAddr':dnsNewCfgPrimaryIpAddr,'dnsCurCfgSecondaryIpAddr':dnsCurCfgSecondaryIpAddr,'dnsNewCfgSecondaryIpAddr':dnsNewCfgSecondaryIpAddr,'dnsCurCfgDomainName':dnsCurCfgDomainName,'dnsNewCfgDomainName':dnsNewCfgDomainName,'dnsCurCfgPrimaryIpv6Addr':dnsCurCfgPrimaryIpv6Addr,'dnsNewCfgPrimaryIpv6Addr':dnsNewCfgPrimaryIpv6Addr,'dnsCurCfgSecondaryIpv6Addr':dnsCurCfgSecondaryIpv6Addr,'dnsNewCfgSecondaryIpv6Addr':dnsNewCfgSecondaryIpv6Addr,'ipNwfCfg':ipNwfCfg,'ipNwfTableMax':ipNwfTableMax,'ipCurCfgNwfTable':ipCurCfgNwfTable,'ipCurCfgNwfEntry':ipCurCfgNwfEntry,_AB:ipCurCfgNwfIndex,'ipCurCfgNwfAddr':ipCurCfgNwfAddr,'ipCurCfgNwfMask':ipCurCfgNwfMask,'ipCurCfgNwfState':ipCurCfgNwfState,'ipNewCfgNwfTable':ipNewCfgNwfTable,'ipNewCfgNwfEntry':ipNewCfgNwfEntry,_AC:ipNewCfgNwfIndex,'ipNewCfgNwfAddr':ipNewCfgNwfAddr,'ipNewCfgNwfMask':ipNewCfgNwfMask,'ipNewCfgNwfState':ipNewCfgNwfState,'ipNewCfgNwfDelete':ipNewCfgNwfDelete,'ipRmapCfg':ipRmapCfg,'ipRmapTableMax':ipRmapTableMax,'ipCurCfgRmapTable':ipCurCfgRmapTable,'ipCurCfgRmapEntry':ipCurCfgRmapEntry,_AD:ipCurCfgRmapIndex,'ipCurCfgRmapLp':ipCurCfgRmapLp,'ipCurCfgRmapMetric':ipCurCfgRmapMetric,'ipCurCfgRmapPrec':ipCurCfgRmapPrec,'ipCurCfgRmapWeight':ipCurCfgRmapWeight,'ipCurCfgRmapState':ipCurCfgRmapState,'ipCurCfgRmapAp':ipCurCfgRmapAp,'ipCurCfgRmapMetricType':ipCurCfgRmapMetricType,'ipNewCfgRmapTable':ipNewCfgRmapTable,'ipNewCfgRmapEntry':ipNewCfgRmapEntry,_AE:ipNewCfgRmapIndex,'ipNewCfgRmapLp':ipNewCfgRmapLp,'ipNewCfgRmapMetric':ipNewCfgRmapMetric,'ipNewCfgRmapPrec':ipNewCfgRmapPrec,'ipNewCfgRmapWeight':ipNewCfgRmapWeight,'ipNewCfgRmapState':ipNewCfgRmapState,'ipNewCfgRmapAp':ipNewCfgRmapAp,'ipNewCfgRmapMetricType':ipNewCfgRmapMetricType,'ipNewCfgRmapDelete':ipNewCfgRmapDelete,'ipAlistTableMax':ipAlistTableMax,'ipCurCfgAlistTable':ipCurCfgAlistTable,'ipCurCfgAlistEntry':ipCurCfgAlistEntry,_AF:ipCurCfgAlistRmapIndex,_c:ipCurCfgAlistIndex,'ipCurCfgAlistNwf':ipCurCfgAlistNwf,'ipCurCfgAlistMetric':ipCurCfgAlistMetric,'ipCurCfgAlistAction':ipCurCfgAlistAction,'ipCurCfgAlistState':ipCurCfgAlistState,'ipNewCfgAlistTable':ipNewCfgAlistTable,'ipNewCfgAlistEntry':ipNewCfgAlistEntry,_AG:ipNewCfgAlistRmapIndex,_AH:ipNewCfgAlistIndex,'ipNewCfgAlistNwf':ipNewCfgAlistNwf,'ipNewCfgAlistMetric':ipNewCfgAlistMetric,'ipNewCfgAlistAction':ipNewCfgAlistAction,'ipNewCfgAlistState':ipNewCfgAlistState,'ipNewCfgAlistDelete':ipNewCfgAlistDelete,'ipAspathTableMax':ipAspathTableMax,'ipCurCfgAspathTable':ipCurCfgAspathTable,'ipCurCfgAspathEntry':ipCurCfgAspathEntry,_AI:ipCurCfgAspathRmapIndex,'ipCurCfgAspathIndex':ipCurCfgAspathIndex,'ipCurCfgAspathAS':ipCurCfgAspathAS,'ipCurCfgAspathAction':ipCurCfgAspathAction,'ipCurCfgAspathState':ipCurCfgAspathState,'ipNewCfgAspathTable':ipNewCfgAspathTable,'ipNewCfgAspathEntry':ipNewCfgAspathEntry,_AJ:ipNewCfgAspathRmapIndex,_AK:ipNewCfgAspathIndex,'ipNewCfgAspathAS':ipNewCfgAspathAS,'ipNewCfgAspathAction':ipNewCfgAspathAction,'ipNewCfgAspathState':ipNewCfgAspathState,'ipNewCfgAspathDelete':ipNewCfgAspathDelete,'bgpCfg':bgpCfg,'bgpGeneral':bgpGeneral,'bgpCurCfgState':bgpCurCfgState,'bgpNewCfgState':bgpNewCfgState,'bgpCurCfgLocalPref':bgpCurCfgLocalPref,'bgpNewCfgLocalPref':bgpNewCfgLocalPref,'bgpCurCfgMaxASPath':bgpCurCfgMaxASPath,'bgpNewCfgMaxASPath':bgpNewCfgMaxASPath,'bgpCurCfgASNumber':bgpCurCfgASNumber,'bgpNewCfgASNumber':bgpNewCfgASNumber,'bgpPeerTableMax':bgpPeerTableMax,'bgpCurCfgPeerTable':bgpCurCfgPeerTable,'bgpCurCfgPeerEntry':bgpCurCfgPeerEntry,_AL:bgpCurCfgPeerIndex,'bgpCurCfgPeerRemoteAddr':bgpCurCfgPeerRemoteAddr,'bgpCurCfgPeerRemoteAs':bgpCurCfgPeerRemoteAs,'bgpCurCfgPeerTtl':bgpCurCfgPeerTtl,'bgpCurCfgPeerState':bgpCurCfgPeerState,'bgpCurCfgPeerMetric':bgpCurCfgPeerMetric,'bgpCurCfgPeerDefaultAction':bgpCurCfgPeerDefaultAction,'bgpCurCfgPeerOspfState':bgpCurCfgPeerOspfState,'bgpCurCfgPeerFixedState':bgpCurCfgPeerFixedState,'bgpCurCfgPeerStaticState':bgpCurCfgPeerStaticState,'bgpCurCfgPeerVipState':bgpCurCfgPeerVipState,'bgpCurCfgPeerInRmapList':bgpCurCfgPeerInRmapList,'bgpCurCfgPeerOutRmapList':bgpCurCfgPeerOutRmapList,'bgpCurCfgPeerHoldTime':bgpCurCfgPeerHoldTime,'bgpCurCfgPeerKeepAlive':bgpCurCfgPeerKeepAlive,'bgpCurCfgPeerMinTime':bgpCurCfgPeerMinTime,'bgpCurCfgPeerConRetry':bgpCurCfgPeerConRetry,'bgpCurCfgPeerMinAS':bgpCurCfgPeerMinAS,'bgpCurCfgPeerRipState':bgpCurCfgPeerRipState,'bgpNewCfgPeerTable':bgpNewCfgPeerTable,'bgpNewCfgPeerEntry':bgpNewCfgPeerEntry,_AO:bgpNewCfgPeerIndex,'bgpNewCfgPeerRemoteAddr':bgpNewCfgPeerRemoteAddr,'bgpNewCfgPeerRemoteAs':bgpNewCfgPeerRemoteAs,'bgpNewCfgPeerTtl':bgpNewCfgPeerTtl,'bgpNewCfgPeerState':bgpNewCfgPeerState,'bgpNewCfgPeerDelete':bgpNewCfgPeerDelete,'bgpNewCfgPeerMetric':bgpNewCfgPeerMetric,'bgpNewCfgPeerDefaultAction':bgpNewCfgPeerDefaultAction,'bgpNewCfgPeerOspfState':bgpNewCfgPeerOspfState,'bgpNewCfgPeerFixedState':bgpNewCfgPeerFixedState,'bgpNewCfgPeerStaticState':bgpNewCfgPeerStaticState,'bgpNewCfgPeerVipState':bgpNewCfgPeerVipState,'bgpNewCfgPeerInRmapList':bgpNewCfgPeerInRmapList,'bgpNewCfgPeerOutRmapList':bgpNewCfgPeerOutRmapList,'bgpNewCfgPeerAddInRmap':bgpNewCfgPeerAddInRmap,'bgpNewCfgPeerAddOutRmap':bgpNewCfgPeerAddOutRmap,'bgpNewCfgPeerRemoveInRmap':bgpNewCfgPeerRemoveInRmap,'bgpNewCfgPeerRemoveOutRmap':bgpNewCfgPeerRemoveOutRmap,'bgpNewCfgPeerHoldTime':bgpNewCfgPeerHoldTime,'bgpNewCfgPeerKeepAlive':bgpNewCfgPeerKeepAlive,'bgpNewCfgPeerMinTime':bgpNewCfgPeerMinTime,'bgpNewCfgPeerConRetry':bgpNewCfgPeerConRetry,'bgpNewCfgPeerMinAS':bgpNewCfgPeerMinAS,'bgpNewCfgPeerRipState':bgpNewCfgPeerRipState,'bgpAggrTableMax':bgpAggrTableMax,'bgpCurCfgAggrTable':bgpCurCfgAggrTable,'bgpCurCfgAggrEntry':bgpCurCfgAggrEntry,_AP:bgpCurCfgAggrIndex,'bgpCurCfgAggrAddr':bgpCurCfgAggrAddr,'bgpCurCfgAggrMask':bgpCurCfgAggrMask,'bgpCurCfgAggrState':bgpCurCfgAggrState,'bgpNewCfgAggrTable':bgpNewCfgAggrTable,'bgpNewCfgAggrEntry':bgpNewCfgAggrEntry,_AQ:bgpNewCfgAggrIndex,'bgpNewCfgAggrAddr':bgpNewCfgAggrAddr,'bgpNewCfgAggrMask':bgpNewCfgAggrMask,'bgpNewCfgAggrState':bgpNewCfgAggrState,'bgpNewCfgAggrDelete':bgpNewCfgAggrDelete,'ospfCfg':ospfCfg,'ospfGeneral':ospfGeneral,'ospfCurCfgDefaultRouteMetric':ospfCurCfgDefaultRouteMetric,'ospfNewCfgDefaultRouteMetric':ospfNewCfgDefaultRouteMetric,'ospfCurCfgDefaultRouteMetricType':ospfCurCfgDefaultRouteMetricType,'ospfNewCfgDefaultRouteMetricType':ospfNewCfgDefaultRouteMetricType,'ospfIntfTableMaxSize':ospfIntfTableMaxSize,'ospfAreaTableMaxSize':ospfAreaTableMaxSize,'ospfRangeTableMaxSize':ospfRangeTableMaxSize,'ospfVirtIntfTableMaxSize':ospfVirtIntfTableMaxSize,'ospfHostTableMaxSize':ospfHostTableMaxSize,'ospfCurCfgState':ospfCurCfgState,'ospfNewCfgState':ospfNewCfgState,'ospfCurCfgLsdb':ospfCurCfgLsdb,'ospfNewCfgLsdb':ospfNewCfgLsdb,'ospfCurCfgAreaTable':ospfCurCfgAreaTable,'ospfCurCfgAreaEntry':ospfCurCfgAreaEntry,_AR:ospfCurCfgAreaIndex,_AS:ospfCurCfgAreaId,'ospfCurCfgAreaSpfInterval':ospfCurCfgAreaSpfInterval,'ospfCurCfgAreaAuthType':ospfCurCfgAreaAuthType,'ospfCurCfgAreaType':ospfCurCfgAreaType,'ospfCurCfgAreaMetric':ospfCurCfgAreaMetric,'ospfCurCfgAreaState':ospfCurCfgAreaState,'ospfNewCfgAreaTable':ospfNewCfgAreaTable,'ospfNewCfgAreaEntry':ospfNewCfgAreaEntry,_AT:ospfNewCfgAreaIndex,_AU:ospfNewCfgAreaId,'ospfNewCfgAreaSpfInterval':ospfNewCfgAreaSpfInterval,'ospfNewCfgAreaAuthType':ospfNewCfgAreaAuthType,'ospfNewCfgAreaType':ospfNewCfgAreaType,'ospfNewCfgAreaMetric':ospfNewCfgAreaMetric,'ospfNewCfgAreaState':ospfNewCfgAreaState,'ospfNewCfgAreaDelete':ospfNewCfgAreaDelete,'ospfRouteRedistribution':ospfRouteRedistribution,'ospfRedistributeStatic':ospfRedistributeStatic,'ospfCurCfgStaticMetric':ospfCurCfgStaticMetric,'ospfNewCfgStaticMetric':ospfNewCfgStaticMetric,'ospfCurCfgStaticMetricType':ospfCurCfgStaticMetricType,'ospfNewCfgStaticMetricType':ospfNewCfgStaticMetricType,'ospfCurCfgStaticOutRmapList':ospfCurCfgStaticOutRmapList,'ospfNewCfgStaticOutRmapList':ospfNewCfgStaticOutRmapList,'ospfNewCfgStaticAddOutRmap':ospfNewCfgStaticAddOutRmap,'ospfNewCfgStaticRemoveOutRmap':ospfNewCfgStaticRemoveOutRmap,'ospfRedistributeEbgp':ospfRedistributeEbgp,'ospfCurCfgEbgpMetric':ospfCurCfgEbgpMetric,'ospfNewCfgEbgpMetric':ospfNewCfgEbgpMetric,'ospfCurCfgEbgpMetricType':ospfCurCfgEbgpMetricType,'ospfNewCfgEbgpMetricType':ospfNewCfgEbgpMetricType,'ospfCurCfgEbgpOutRmapList':ospfCurCfgEbgpOutRmapList,'ospfNewCfgEbgpOutRmapList':ospfNewCfgEbgpOutRmapList,'ospfNewCfgEbgpAddOutRmap':ospfNewCfgEbgpAddOutRmap,'ospfNewCfgEbgpRemoveOutRmap':ospfNewCfgEbgpRemoveOutRmap,'ospfRedistributeIbgp':ospfRedistributeIbgp,'ospfCurCfgIbgpMetric':ospfCurCfgIbgpMetric,'ospfNewCfgIbgpMetric':ospfNewCfgIbgpMetric,'ospfCurCfgIbgpMetricType':ospfCurCfgIbgpMetricType,'ospfNewCfgIbgpMetricType':ospfNewCfgIbgpMetricType,'ospfCurCfgIbgpOutRmapList':ospfCurCfgIbgpOutRmapList,'ospfNewCfgIbgpOutRmapList':ospfNewCfgIbgpOutRmapList,'ospfNewCfgIbgpAddOutRmap':ospfNewCfgIbgpAddOutRmap,'ospfNewCfgIbgpRemoveOutRmap':ospfNewCfgIbgpRemoveOutRmap,'ospfRedistributeFixed':ospfRedistributeFixed,'ospfCurCfgFixedMetric':ospfCurCfgFixedMetric,'ospfNewCfgFixedMetric':ospfNewCfgFixedMetric,'ospfCurCfgFixedMetricType':ospfCurCfgFixedMetricType,'ospfNewCfgFixedMetricType':ospfNewCfgFixedMetricType,'ospfCurCfgFixedOutRmapList':ospfCurCfgFixedOutRmapList,'ospfNewCfgFixedOutRmapList':ospfNewCfgFixedOutRmapList,'ospfNewCfgFixedAddOutRmap':ospfNewCfgFixedAddOutRmap,'ospfNewCfgFixedRemoveOutRmap':ospfNewCfgFixedRemoveOutRmap,'ospfRedistributeRip':ospfRedistributeRip,'ospfCurCfgRipMetric':ospfCurCfgRipMetric,'ospfNewCfgRipMetric':ospfNewCfgRipMetric,'ospfCurCfgRipMetricType':ospfCurCfgRipMetricType,'ospfNewCfgRipMetricType':ospfNewCfgRipMetricType,'ospfCurCfgRipOutRmapList':ospfCurCfgRipOutRmapList,'ospfNewCfgRipOutRmapList':ospfNewCfgRipOutRmapList,'ospfNewCfgRipAddOutRmap':ospfNewCfgRipAddOutRmap,'ospfNewCfgRipRemoveOutRmap':ospfNewCfgRipRemoveOutRmap,'ospfCurCfgMdkeyTable':ospfCurCfgMdkeyTable,'ospfCurCfgMdkeyEntry':ospfCurCfgMdkeyEntry,_AV:ospfCurCfgMdkeyIndex,'ospfCurCfgMdkeyKey':ospfCurCfgMdkeyKey,'ospfNewCfgMdkeyTable':ospfNewCfgMdkeyTable,'ospfNewCfgMdkeyEntry':ospfNewCfgMdkeyEntry,_AW:ospfNewCfgMdkeyIndex,'ospfNewCfgMdkeyKey':ospfNewCfgMdkeyKey,'ospfNewCfgMdkeyDelete':ospfNewCfgMdkeyDelete,'ospfCurCfgIntfTable':ospfCurCfgIntfTable,'ospfCurCfgIntfEntry':ospfCurCfgIntfEntry,_AX:ospfCurCfgIntfIndex,'ospfCurCfgIntfId':ospfCurCfgIntfId,'ospfCurCfgIntfMdkey':ospfCurCfgIntfMdkey,'ospfCurCfgIntfAreaId':ospfCurCfgIntfAreaId,'ospfCurCfgIntfPriority':ospfCurCfgIntfPriority,'ospfCurCfgIntfCost':ospfCurCfgIntfCost,'ospfCurCfgIntfHello':ospfCurCfgIntfHello,'ospfCurCfgIntfDead':ospfCurCfgIntfDead,'ospfCurCfgIntfTransit':ospfCurCfgIntfTransit,'ospfCurCfgIntfRetrans':ospfCurCfgIntfRetrans,'ospfCurCfgIntfKey':ospfCurCfgIntfKey,'ospfCurCfgIntfState':ospfCurCfgIntfState,'ospfNewCfgIntfTable':ospfNewCfgIntfTable,'ospfNewCfgIntfEntry':ospfNewCfgIntfEntry,_AY:ospfNewCfgIntfIndex,'ospfNewCfgIntfId':ospfNewCfgIntfId,'ospfNewCfgIntfMdkey':ospfNewCfgIntfMdkey,'ospfNewCfgIntfAreaId':ospfNewCfgIntfAreaId,'ospfNewCfgIntfPriority':ospfNewCfgIntfPriority,'ospfNewCfgIntfCost':ospfNewCfgIntfCost,'ospfNewCfgIntfHello':ospfNewCfgIntfHello,'ospfNewCfgIntfDead':ospfNewCfgIntfDead,'ospfNewCfgIntfTransit':ospfNewCfgIntfTransit,'ospfNewCfgIntfRetrans':ospfNewCfgIntfRetrans,'ospfNewCfgIntfKey':ospfNewCfgIntfKey,'ospfNewCfgIntfState':ospfNewCfgIntfState,'ospfNewCfgIntfDelete':ospfNewCfgIntfDelete,'ospfCurCfgVirtIntfTable':ospfCurCfgVirtIntfTable,'ospfCurCfgVirtIntfEntry':ospfCurCfgVirtIntfEntry,_AZ:ospfCurCfgVirtIntfIndex,'ospfCurCfgVirtIntfAreaId':ospfCurCfgVirtIntfAreaId,'ospfCurCfgVirtIntfNbr':ospfCurCfgVirtIntfNbr,'ospfCurCfgVirtIntfMdkey':ospfCurCfgVirtIntfMdkey,'ospfCurCfgVirtIntfHello':ospfCurCfgVirtIntfHello,'ospfCurCfgVirtIntfDead':ospfCurCfgVirtIntfDead,'ospfCurCfgVirtIntfTransit':ospfCurCfgVirtIntfTransit,'ospfCurCfgVirtIntfRetrans':ospfCurCfgVirtIntfRetrans,'ospfCurCfgVirtIntfKey':ospfCurCfgVirtIntfKey,'ospfCurCfgVirtIntfState':ospfCurCfgVirtIntfState,'ospfNewCfgVirtIntfTable':ospfNewCfgVirtIntfTable,'ospfNewCfgVirtIntfEntry':ospfNewCfgVirtIntfEntry,_Aa:ospfNewCfgVirtIntfIndex,'ospfNewCfgVirtIntfAreaId':ospfNewCfgVirtIntfAreaId,'ospfNewCfgVirtIntfNbr':ospfNewCfgVirtIntfNbr,'ospfNewCfgVirtIntfMdkey':ospfNewCfgVirtIntfMdkey,'ospfNewCfgVirtIntfHello':ospfNewCfgVirtIntfHello,'ospfNewCfgVirtIntfDead':ospfNewCfgVirtIntfDead,'ospfNewCfgVirtIntfTransit':ospfNewCfgVirtIntfTransit,'ospfNewCfgVirtIntfRetrans':ospfNewCfgVirtIntfRetrans,'ospfNewCfgVirtIntfKey':ospfNewCfgVirtIntfKey,'ospfNewCfgVirtIntfState':ospfNewCfgVirtIntfState,'ospfNewCfgVirtIntfDelete':ospfNewCfgVirtIntfDelete,'ospfMdkeyTableMaxSize':ospfMdkeyTableMaxSize,'ospfCurCfgHostTable':ospfCurCfgHostTable,'ospfCurCfgHostEntry':ospfCurCfgHostEntry,_Ab:ospfCurCfgHostIndex,'ospfCurCfgHostIpAddr':ospfCurCfgHostIpAddr,'ospfCurCfgHostAreaIndex':ospfCurCfgHostAreaIndex,'ospfCurCfgHostCost':ospfCurCfgHostCost,'ospfCurCfgHostState':ospfCurCfgHostState,'ospfNewCfgHostTable':ospfNewCfgHostTable,'ospfNewCfgHostEntry':ospfNewCfgHostEntry,_Ac:ospfNewCfgHostIndex,'ospfNewCfgHostIpAddr':ospfNewCfgHostIpAddr,'ospfNewCfgHostAreaIndex':ospfNewCfgHostAreaIndex,'ospfNewCfgHostCost':ospfNewCfgHostCost,'ospfNewCfgHostState':ospfNewCfgHostState,'ospfNewCfgHostDelete':ospfNewCfgHostDelete,'ospfCurCfgRangeTable':ospfCurCfgRangeTable,'ospfCurCfgRangeEntry':ospfCurCfgRangeEntry,_Ad:ospfCurCfgRangeIndex,'ospfCurCfgRangeAddr':ospfCurCfgRangeAddr,'ospfCurCfgRangeMask':ospfCurCfgRangeMask,'ospfCurCfgRangeAreaIndex':ospfCurCfgRangeAreaIndex,'ospfCurCfgRangeHideState':ospfCurCfgRangeHideState,'ospfCurCfgRangeState':ospfCurCfgRangeState,'ospfNewCfgRangeTable':ospfNewCfgRangeTable,'ospfNewCfgRangeEntry':ospfNewCfgRangeEntry,_Ae:ospfNewCfgRangeIndex,'ospfNewCfgRangeAddr':ospfNewCfgRangeAddr,'ospfNewCfgRangeMask':ospfNewCfgRangeMask,'ospfNewCfgRangeAreaIndex':ospfNewCfgRangeAreaIndex,'ospfNewCfgRangeHideState':ospfNewCfgRangeHideState,'ospfNewCfgRangeState':ospfNewCfgRangeState,'ospfNewCfgRangeDelete':ospfNewCfgRangeDelete,'ospfNewCfgVisionAreaTable':ospfNewCfgVisionAreaTable,'ospfNewCfgVisionAreaEntry':ospfNewCfgVisionAreaEntry,_Af:ospfNewCfgVisionAreaIndex,'ospfNewCfgVisionAreaId':ospfNewCfgVisionAreaId,'ospfNewCfgVisionAreaSpfInterval':ospfNewCfgVisionAreaSpfInterval,'ospfNewCfgVisionAreaAuthType':ospfNewCfgVisionAreaAuthType,'ospfNewCfgVisionAreaType':ospfNewCfgVisionAreaType,'ospfNewCfgVisionAreaMetric':ospfNewCfgVisionAreaMetric,'ospfNewCfgVisionAreaState':ospfNewCfgVisionAreaState,'ospfNewCfgVisionAreaDelete':ospfNewCfgVisionAreaDelete,'ipGeneralCfg':ipGeneralCfg,'ipCurCfgRouterID':ipCurCfgRouterID,'ipNewCfgRouterID':ipNewCfgRouterID,'ipCurCfgASNumber':ipCurCfgASNumber,'ipNewCfgASNumber':ipNewCfgASNumber,'ipStaticArpCfg':ipStaticArpCfg,'ipStaticArpTableMaxSize':ipStaticArpTableMaxSize,'ipCurCfgStaticArpTable':ipCurCfgStaticArpTable,'ipCurCfgStaticArpEntry':ipCurCfgStaticArpEntry,_Ag:ipCurCfgStaticArpIndx,'ipCurCfgStaticArpIp':ipCurCfgStaticArpIp,'ipCurCfgStaticArpMAC':ipCurCfgStaticArpMAC,'ipCurCfgStaticArpVlan':ipCurCfgStaticArpVlan,'ipCurCfgStaticArpPort':ipCurCfgStaticArpPort,'ipNewCfgStaticArpTable':ipNewCfgStaticArpTable,'ipNewCfgStaticArpEntry':ipNewCfgStaticArpEntry,_Ah:ipNewCfgStaticArpIndx,'ipNewCfgStaticArpIp':ipNewCfgStaticArpIp,'ipNewCfgStaticArpMAC':ipNewCfgStaticArpMAC,'ipNewCfgStaticArpVlan':ipNewCfgStaticArpVlan,'ipNewCfgStaticArpPort':ipNewCfgStaticArpPort,'ipNewCfgStaticArpAction':ipNewCfgStaticArpAction,'ipStaticArpTableNextAvailableIndex':ipStaticArpTableNextAvailableIndex,'rip2Cfg':rip2Cfg,'ripCurCfgIntfTable':ripCurCfgIntfTable,'ripCurCfgIntfEntry':ripCurCfgIntfEntry,_Ai:ripCurCfgIntfIndex,'ripCurCfgIntfVersion':ripCurCfgIntfVersion,'ripCurCfgIntfState':ripCurCfgIntfState,'ripCurCfgIntfListen':ripCurCfgIntfListen,'ripCurCfgIntfDefListen':ripCurCfgIntfDefListen,'ripCurCfgIntfTrigUpdate':ripCurCfgIntfTrigUpdate,'ripCurCfgIntfMcastUpdate':ripCurCfgIntfMcastUpdate,'ripCurCfgIntfPoisonReverse':ripCurCfgIntfPoisonReverse,'ripCurCfgIntfSupply':ripCurCfgIntfSupply,'ripCurCfgIntfMetric':ripCurCfgIntfMetric,'ripCurCfgIntfAuth':ripCurCfgIntfAuth,'ripCurCfgIntfKey':ripCurCfgIntfKey,'ripCurCfgIntfDefault':ripCurCfgIntfDefault,'ripNewCfgIntfTable':ripNewCfgIntfTable,'ripNewCfgIntfEntry':ripNewCfgIntfEntry,_Aj:ripNewCfgIntfIndex,'ripNewCfgIntfVersion':ripNewCfgIntfVersion,'ripNewCfgIntfSupply':ripNewCfgIntfSupply,'ripNewCfgIntfListen':ripNewCfgIntfListen,'ripNewCfgIntfDefListen':ripNewCfgIntfDefListen,'ripNewCfgIntfTrigUpdate':ripNewCfgIntfTrigUpdate,'ripNewCfgIntfMcastUpdate':ripNewCfgIntfMcastUpdate,'ripNewCfgIntfPoisonReverse':ripNewCfgIntfPoisonReverse,'ripNewCfgIntfState':ripNewCfgIntfState,'ripNewCfgIntfMetric':ripNewCfgIntfMetric,'ripNewCfgIntfAuth':ripNewCfgIntfAuth,'ripNewCfgIntfKey':ripNewCfgIntfKey,'ripNewCfgIntfDefault':ripNewCfgIntfDefault,'ripGeneral':ripGeneral,'rip2CurCfgState':rip2CurCfgState,'rip2NewCfgState':rip2NewCfgState,'rip2CurCfgUpdatePeriod':rip2CurCfgUpdatePeriod,'rip2NewCfgUpdatePeriod':rip2NewCfgUpdatePeriod,'rip2CurCfgVip':rip2CurCfgVip,'rip2NewCfgVip':rip2NewCfgVip,'rip2CurCfgStaticSupply':rip2CurCfgStaticSupply,'rip2NewCfgStaticSupply':rip2NewCfgStaticSupply,'layer3Stats':layer3Stats,'arpStats':arpStats,'arpStatEntries':arpStatEntries,'arpStatHighWater':arpStatHighWater,'arpStatMaxEntries':arpStatMaxEntries,'routeStats':routeStats,'routeStatEntries':routeStatEntries,'routeStatHighWater':routeStatHighWater,'routeStatMaxEntries':routeStatMaxEntries,'dnsStats':dnsStats,'dnsStatInGoodDnsRequests':dnsStatInGoodDnsRequests,'dnsStatInBadDnsRequests':dnsStatInBadDnsRequests,'dnsStatOutDnsRequests':dnsStatOutDnsRequests,'vrrpStats':vrrpStats,'vrrpStatInAdvers':vrrpStatInAdvers,'vrrpStatOutAdvers':vrrpStatOutAdvers,'vrrpStatOutBadAdvers':vrrpStatOutBadAdvers,'ospfStats':ospfStats,'ospfGeneralStats':ospfGeneralStats,'ospfCumRxTxStats':ospfCumRxTxStats,'ospfCumRxPkts':ospfCumRxPkts,'ospfCumTxPkts':ospfCumTxPkts,'ospfCumRxHello':ospfCumRxHello,'ospfCumTxHello':ospfCumTxHello,'ospfCumRxDatabase':ospfCumRxDatabase,'ospfCumTxDatabase':ospfCumTxDatabase,'ospfCumRxlsReqs':ospfCumRxlsReqs,'ospfCumTxlsReqs':ospfCumTxlsReqs,'ospfCumRxlsAcks':ospfCumRxlsAcks,'ospfCumTxlsAcks':ospfCumTxlsAcks,'ospfCumRxlsUpdates':ospfCumRxlsUpdates,'ospfCumTxlsUpdates':ospfCumTxlsUpdates,'ospfCumNbrChangeStats':ospfCumNbrChangeStats,'ospfCumNbrhello':ospfCumNbrhello,'ospfCumNbrStart':ospfCumNbrStart,'ospfCumNbrAdjointOk':ospfCumNbrAdjointOk,'ospfCumNbrNegotiationDone':ospfCumNbrNegotiationDone,'ospfCumNbrExchangeDone':ospfCumNbrExchangeDone,'ospfCumNbrBadRequests':ospfCumNbrBadRequests,'ospfCumNbrBadSequence':ospfCumNbrBadSequence,'ospfCumNbrLoadingDone':ospfCumNbrLoadingDone,'ospfCumNbrN1way':ospfCumNbrN1way,'ospfCumNbrRstAd':ospfCumNbrRstAd,'ospfCumNbrDown':ospfCumNbrDown,'ospfCumNbrN2way':ospfCumNbrN2way,'ospfCumIntfChangeStats':ospfCumIntfChangeStats,'ospfCumIntfHello':ospfCumIntfHello,'ospfCumIntfDown':ospfCumIntfDown,'ospfCumIntfLoop':ospfCumIntfLoop,'ospfCumIntfUnloop':ospfCumIntfUnloop,'ospfCumIntfWaitTimer':ospfCumIntfWaitTimer,'ospfCumIntfBackup':ospfCumIntfBackup,'ospfCumIntfNbrChange':ospfCumIntfNbrChange,'ospfTimersKickOffStats':ospfTimersKickOffStats,'ospfTmrsKckOffHello':ospfTmrsKckOffHello,'ospfTmrsKckOffRetransmit':ospfTmrsKckOffRetransmit,'ospfTmrsKckOffLsaLock':ospfTmrsKckOffLsaLock,'ospfTmrsKckOffLsaAck':ospfTmrsKckOffLsaAck,'ospfTmrsKckOffDbage':ospfTmrsKckOffDbage,'ospfTmrsKckOffSummary':ospfTmrsKckOffSummary,'ospfTmrsKckOffAseExport':ospfTmrsKckOffAseExport,'ospfArea':ospfArea,'ospfAreaRxTxStats':ospfAreaRxTxStats,'ospfAreaRxTxStatsEntry':ospfAreaRxTxStatsEntry,_Ak:ospfAreaRxTxIndex,'ospfAreaRxPkts':ospfAreaRxPkts,'ospfAreaTxPkts':ospfAreaTxPkts,'ospfAreaRxHello':ospfAreaRxHello,'ospfAreaTxHello':ospfAreaTxHello,'ospfAreaRxDatabase':ospfAreaRxDatabase,'ospfAreaTxDatabase':ospfAreaTxDatabase,'ospfAreaRxlsReqs':ospfAreaRxlsReqs,'ospfAreaTxlsReqs':ospfAreaTxlsReqs,'ospfAreaRxlsAcks':ospfAreaRxlsAcks,'ospfAreaTxlsAcks':ospfAreaTxlsAcks,'ospfAreaRxlsUpdates':ospfAreaRxlsUpdates,'ospfAreaTxlsUpdates':ospfAreaTxlsUpdates,'ospfAreaNbrChangeStats':ospfAreaNbrChangeStats,'ospfAreaNbrChangeStatsEntry':ospfAreaNbrChangeStatsEntry,_Al:ospfAreaNbrIndex,'ospfAreaNbrhello':ospfAreaNbrhello,'ospfAreaNbrStart':ospfAreaNbrStart,'ospfAreaNbrAdjointOk':ospfAreaNbrAdjointOk,'ospfAreaNbrNegotiationDone':ospfAreaNbrNegotiationDone,'ospfAreaNbrExchangeDone':ospfAreaNbrExchangeDone,'ospfAreaNbrBadRequests':ospfAreaNbrBadRequests,'ospfAreaNbrBadSequence':ospfAreaNbrBadSequence,'ospfAreaNbrLoadingDone':ospfAreaNbrLoadingDone,'ospfAreaNbrN1way':ospfAreaNbrN1way,'ospfAreaNbrRstAd':ospfAreaNbrRstAd,'ospfAreaNbrDown':ospfAreaNbrDown,'ospfAreaNbrN2way':ospfAreaNbrN2way,'ospfAreaChangeStats':ospfAreaChangeStats,'ospfAreaChangeStatsEntry':ospfAreaChangeStatsEntry,_Am:ospfAreaIntfIndex,'ospfAreaIntfHello':ospfAreaIntfHello,'ospfAreaIntfDown':ospfAreaIntfDown,'ospfAreaIntfLoop':ospfAreaIntfLoop,'ospfAreaIntfUnloop':ospfAreaIntfUnloop,'ospfAreaIntfWaitTimer':ospfAreaIntfWaitTimer,'ospfAreaIntfBackup':ospfAreaIntfBackup,'ospfAreaIntfNbrChange':ospfAreaIntfNbrChange,'ospfAreaErrorStats':ospfAreaErrorStats,'ospfAreaErrorStatsEntry':ospfAreaErrorStatsEntry,_An:ospfAreaErrIndex,'ospfAreaErrAuthFailure':ospfAreaErrAuthFailure,'ospfAreaErrNetmaskMismatch':ospfAreaErrNetmaskMismatch,'ospfAreaErrHelloMismatch':ospfAreaErrHelloMismatch,'ospfAreaErrDeadMismatch':ospfAreaErrDeadMismatch,'ospfAreaErrOptionsMismatch':ospfAreaErrOptionsMismatch,'ospfAreaErrUnknownNbr':ospfAreaErrUnknownNbr,'ospfInterface':ospfInterface,'ospfIntfRxTxStats':ospfIntfRxTxStats,'ospfIntfRxTxStatsEntry':ospfIntfRxTxStatsEntry,_Ao:ospfIntfRxTxIndex,'ospfIntfRxPkts':ospfIntfRxPkts,'ospfIntfTxPkts':ospfIntfTxPkts,'ospfIntfRxHello':ospfIntfRxHello,'ospfIntfTxHello':ospfIntfTxHello,'ospfIntfRxDatabase':ospfIntfRxDatabase,'ospfIntfTxDatabase':ospfIntfTxDatabase,'ospfIntfRxlsReqs':ospfIntfRxlsReqs,'ospfIntfTxlsReqs':ospfIntfTxlsReqs,'ospfIntfRxlsAcks':ospfIntfRxlsAcks,'ospfIntfTxlsAcks':ospfIntfTxlsAcks,'ospfIntfRxlsUpdates':ospfIntfRxlsUpdates,'ospfIntfTxlsUpdates':ospfIntfTxlsUpdates,'ospfIntfNbrChangeStats':ospfIntfNbrChangeStats,'ospfIntfNbrChangeStatsEntry':ospfIntfNbrChangeStatsEntry,_Ap:ospfIntfNbrIndex,'ospfIntfNbrhello':ospfIntfNbrhello,'ospfIntfNbrStart':ospfIntfNbrStart,'ospfIntfNbrAdjointOk':ospfIntfNbrAdjointOk,'ospfIntfNbrNegotiationDone':ospfIntfNbrNegotiationDone,'ospfIntfNbrExchangeDone':ospfIntfNbrExchangeDone,'ospfIntfNbrBadRequests':ospfIntfNbrBadRequests,'ospfIntfNbrBadSequence':ospfIntfNbrBadSequence,'ospfIntfNbrLoadingDone':ospfIntfNbrLoadingDone,'ospfIntfNbrN1way':ospfIntfNbrN1way,'ospfIntfNbrRstAd':ospfIntfNbrRstAd,'ospfIntfNbrDown':ospfIntfNbrDown,'ospfIntfNbrN2way':ospfIntfNbrN2way,'ospfIntfChangeStats':ospfIntfChangeStats,'ospfIntfChangeStatsEntry':ospfIntfChangeStatsEntry,_Aq:ospfIntfIndex,'ospfIntfHello':ospfIntfHello,'ospfIntfDown':ospfIntfDown,'ospfIntfLoop':ospfIntfLoop,'ospfIntfUnloop':ospfIntfUnloop,'ospfIntfWaitTimer':ospfIntfWaitTimer,'ospfIntfBackup':ospfIntfBackup,'ospfIntfNbrChange':ospfIntfNbrChange,'ospfIntfErrorStats':ospfIntfErrorStats,'ospfIntfErrorStatsEntry':ospfIntfErrorStatsEntry,_Ar:ospfIntfErrIndex,'ospfIntfErrAuthFailure':ospfIntfErrAuthFailure,'ospfIntfErrNetmaskMismatch':ospfIntfErrNetmaskMismatch,'ospfIntfErrHelloMismatch':ospfIntfErrHelloMismatch,'ospfIntfErrDeadMismatch':ospfIntfErrDeadMismatch,'ospfIntfErrOptionsMismatch':ospfIntfErrOptionsMismatch,'ospfIntfErrUnknownNbr':ospfIntfErrUnknownNbr,'clearStats':clearStats,'ipClearStats':ipClearStats,'ifStatsTable':ifStatsTable,'ifStatsEntry':ifStatsEntry,_As:ifStatsIndex,'ifClearStats':ifClearStats,'ip6Stats':ip6Stats,'ip6InReceives':ip6InReceives,'ip6ForwDatagrams':ip6ForwDatagrams,'ip6InDelivers':ip6InDelivers,'ip6InDiscards':ip6InDiscards,'ip6InUnknownProtos':ip6InUnknownProtos,'ip6InAddrErrors':ip6InAddrErrors,'ip6OutRequests':ip6OutRequests,'ip6OutNoRoutes':ip6OutNoRoutes,'ip6ReasmOKs':ip6ReasmOKs,'ip6ReasmFails':ip6ReasmFails,'ip6icmpInMsgs':ip6icmpInMsgs,'ip6icmpOutMsgs':ip6icmpOutMsgs,'ip6icmpInErrors':ip6icmpInErrors,'ip6icmpOutErrors':ip6icmpOutErrors,'icmp6Stats':icmp6Stats,'icmp6StatsTable':icmp6StatsTable,'icmp6StatsEntry':icmp6StatsEntry,_At:icmp6StatsIndx,'icmp6IntfIndex':icmp6IntfIndex,'icmp6InMsgs':icmp6InMsgs,'icmp6InErrors':icmp6InErrors,'icmp6InEchos':icmp6InEchos,'icmp6InEchoReps':icmp6InEchoReps,'icmp6InNSs':icmp6InNSs,'icmp6InNAs':icmp6InNAs,'icmp6InRSs':icmp6InRSs,'icmp6InRAs':icmp6InRAs,'icmp6InDestUnreachs':icmp6InDestUnreachs,'icmp6InTimeExcds':icmp6InTimeExcds,'icmp6InTooBigs':icmp6InTooBigs,'icmp6InParmProbs':icmp6InParmProbs,'icmp6InRedirects':icmp6InRedirects,'icmp6OutMsgs':icmp6OutMsgs,'icmp6OutErrors':icmp6OutErrors,'icmp6OutEchos':icmp6OutEchos,'icmp6OutEchoReps':icmp6OutEchoReps,'icmp6OutNSs':icmp6OutNSs,'icmp6OutNAs':icmp6OutNAs,'icmp6OutRSs':icmp6OutRSs,'icmp6OutRAs':icmp6OutRAs,'icmp6OutRedirects':icmp6OutRedirects,'ip6gwStats':ip6gwStats,'ip6GwStatsTable':ip6GwStatsTable,'ip6GwStatsEntry':ip6GwStatsEntry,_Au:ip6GwStatsIndex,'ip6GwIndex':ip6GwIndex,'ip6GwEchoreq':ip6GwEchoreq,'ip6GwEchoresp':ip6GwEchoresp,'ip6GwFails':ip6GwFails,'ip6GwMaster':ip6GwMaster,'ip6IfIndex':ip6IfIndex,'ip6GwRetry':ip6GwRetry,'rip2Stats':rip2Stats,'ripStatInPackets':ripStatInPackets,'ripStatOutPackets':ripStatOutPackets,'ripStatInRequestPkts':ripStatInRequestPkts,'ripStatInResponsePkts':ripStatInResponsePkts,'ripStatOutRequestPkts':ripStatOutRequestPkts,'ripStatOutResponsePkts':ripStatOutResponsePkts,'ripStatRouteTimeout':ripStatRouteTimeout,'ripStatInBadSizePkts':ripStatInBadSizePkts,'ripStatInBadVersion':ripStatInBadVersion,'ripStatInBadZeros':ripStatInBadZeros,'ripStatInBadSourcePort':ripStatInBadSourcePort,'ripStatInBadSourceIP':ripStatInBadSourceIP,'ripStatInSelfRcvPkts':ripStatInSelfRcvPkts,'tcpStats':tcpStats,'tcpStatCurConn':tcpStatCurConn,'tcpStatCurInConn':tcpStatCurInConn,'tcpStatCurOutConn':tcpStatCurOutConn,'layer3Info':layer3Info,'ipRoutingInfo':ipRoutingInfo,'ipRouteInfoTable':ipRouteInfoTable,'ipRouteInfoEntry':ipRouteInfoEntry,_Av:ipRouteInfoIndx,'ipRouteInfoDestIp':ipRouteInfoDestIp,'ipRouteInfoMask':ipRouteInfoMask,'ipRouteInfoGateway':ipRouteInfoGateway,'ipRouteInfoTag':ipRouteInfoTag,'ipRouteInfoType':ipRouteInfoType,'ipRouteInfoInterface':ipRouteInfoInterface,'ipRouteInfoGateway1':ipRouteInfoGateway1,'ipRouteInfoGateway2':ipRouteInfoGateway2,'ipRouteInfoMetric':ipRouteInfoMetric,'routeTableClear':routeTableClear,'arpInfo':arpInfo,'arpInfoTable':arpInfoTable,'arpInfoEntry':arpInfoEntry,_Ay:arpInfoDestIp,'arpInfoMacAddr':arpInfoMacAddr,'arpInfoVLAN':arpInfoVLAN,'arpInfoSrcPort':arpInfoSrcPort,'arpInfoRefPorts':arpInfoRefPorts,'arpInfoFlag':arpInfoFlag,'arpCacheClear':arpCacheClear,'vrrpInfo':vrrpInfo,'vrrpInfoVirtRtrTable':vrrpInfoVirtRtrTable,'vrrpInfoVirtRtrTableEntry':vrrpInfoVirtRtrTableEntry,_Az:vrrpInfoVirtRtrIndex,'vrrpInfoVirtRtrState':vrrpInfoVirtRtrState,'vrrpInfoVirtRtrOwnership':vrrpInfoVirtRtrOwnership,'vrrpInfoVirtRtrServer':vrrpInfoVirtRtrServer,'vrrpInfoVirtRtrProxy':vrrpInfoVirtRtrProxy,'vrrpInfoVirtRtrPriority':vrrpInfoVirtRtrPriority,'ospfinfo':ospfinfo,'ospfGeneralInfo':ospfGeneralInfo,'ospfStartTime':ospfStartTime,'ospfProcessUptime':ospfProcessUptime,'ospfLsTypesSupported':ospfLsTypesSupported,'ospfIntfCountForRouter':ospfIntfCountForRouter,'ospfVlinkCountForRouter':ospfVlinkCountForRouter,'ospfTotalNeighbours':ospfTotalNeighbours,'ospfNbrInInitState':ospfNbrInInitState,'ospfNbrInExchState':ospfNbrInExchState,'ospfNbrInFullState':ospfNbrInFullState,'ospfTotalAreas':ospfTotalAreas,'ospfTotalTransitAreas':ospfTotalTransitAreas,'ospfTotalNssaAreas':ospfTotalNssaAreas,'ospfAreaInfoTable':ospfAreaInfoTable,'ospfAreaInfoEntry':ospfAreaInfoEntry,_A_:ospfAreaInfoIndex,'ospfTotalNumberOfInterfaces':ospfTotalNumberOfInterfaces,'ospfNumberOfInterfacesUp':ospfNumberOfInterfacesUp,'ospfNumberOfLsdbEntries':ospfNumberOfLsdbEntries,'ospfAreaInfoId':ospfAreaInfoId,'ospfIntfInfoTable':ospfIntfInfoTable,'ospfIntfInfoEntry':ospfIntfInfoEntry,_B0:ospfIfInfoIndex,'ospfIfDesignatedRouterIP':ospfIfDesignatedRouterIP,'ospfIfBackupDesignatedRouterIP':ospfIfBackupDesignatedRouterIP,'ospfIfWaitInterval':ospfIfWaitInterval,'ospfIfTotalNeighbours':ospfIfTotalNeighbours,'ospfIfInfoIpAddress':ospfIfInfoIpAddress,'ospfIfNbrTable':ospfIfNbrTable,'ospfIfNbrEntry':ospfIfNbrEntry,_B1:ospfIfNbrIntfIndex,_B2:ospfIfNbrIpAddr,'ospfIfNbrPriority':ospfIfNbrPriority,'ospfIfNbrState':ospfIfNbrState,'ospfIfNbrDesignatedRtr':ospfIfNbrDesignatedRtr,'ospfIfNbrBackupDesignatedRtr':ospfIfNbrBackupDesignatedRtr,'ospfIfNbrIpAddress':ospfIfNbrIpAddress,'gatewayInfo':gatewayInfo,'gatewayInfoTable':gatewayInfoTable,'gatewayInfoEntry':gatewayInfoEntry,_B3:gatewayInfoIndex,'gatewayInfoAddr':gatewayInfoAddr,'gatewayInfoVlan':gatewayInfoVlan,'gatewayInfoStatus':gatewayInfoStatus,'gatewayInfoAddr6':gatewayInfoAddr6,'nbrcacheInfo':nbrcacheInfo,'nbrcacheInfoTable':nbrcacheInfoTable,'nbrcacheInfoEntry':nbrcacheInfoEntry,_B4:nbrcacheInfoIndex,'nbrcacheInfoDestIp':nbrcacheInfoDestIp,'nbrcacheInfoState':nbrcacheInfoState,'nbrcacheInfoType':nbrcacheInfoType,'nbrcacheInfoMacAddr':nbrcacheInfoMacAddr,'nbrcacheInfoVlanId':nbrcacheInfoVlanId,'nbrcacheInfoPortNum':nbrcacheInfoPortNum,'nbrcacheClear':nbrcacheClear,'nbrcacheInfoTotDynamicEntries':nbrcacheInfoTotDynamicEntries,'nbrcacheInfoTotLocalEntries':nbrcacheInfoTotLocalEntries,'nbrcacheInfoTotOtherEntries':nbrcacheInfoTotOtherEntries,'ipRoute6Info':ipRoute6Info,'ipRoute6InfoTable':ipRoute6InfoTable,'ipRoute6InfoEntry':ipRoute6InfoEntry,_B5:ipRoute6InfoIndx,'ipRoute6InfoDestIp6':ipRoute6InfoDestIp6,'ipRoute6InfoInterface':ipRoute6InfoInterface,'ipRoute6InfoNextHop':ipRoute6InfoNextHop,'ipRoute6InfoProto':ipRoute6InfoProto,'ipIntfInfo':ipIntfInfo,'ipIntfInfoTable':ipIntfInfoTable,'intfInfoEntry':intfInfoEntry,_B6:intfInfoIndex,'intfInfoIpver':intfInfoIpver,'intfInfoAddr':intfInfoAddr,'intfInfoNetMask':intfInfoNetMask,'intfInfoBcastAddr':intfInfoBcastAddr,'intfInfoVlan':intfInfoVlan,'intfInfoStatus':intfInfoStatus,'intfInfoLinkLocalAddr':intfInfoLinkLocalAddr,'rip2Info':rip2Info,'rip2GeneralInfo':rip2GeneralInfo,'ripInfoState':ripInfoState,'ripInfoUpdatePeriod':ripInfoUpdatePeriod,'ripInfoVip':ripInfoVip,'ripInfoStaticSupply':ripInfoStaticSupply,'rip2InfoIntfTable':rip2InfoIntfTable,'ripInfoIntfEntry':ripInfoIntfEntry,_B7:ripInfoIntfIndex,'ripInfoIntfVersion':ripInfoIntfVersion,'ripInfoIntfAddress':ripInfoIntfAddress,'ripInfoIntfState':ripInfoIntfState,'ripInfoIntfListen':ripInfoIntfListen,'ripInfoIntfTrigUpdate':ripInfoIntfTrigUpdate,'ripInfoIntfMcastUpdate':ripInfoIntfMcastUpdate,'ripInfoIntfPoisonReverse':ripInfoIntfPoisonReverse,'ripInfoIntfSupply':ripInfoIntfSupply,'ripInfoIntfMetric':ripInfoIntfMetric,'ripInfoIntfAuth':ripInfoIntfAuth,'ripInfoIntfKey':ripInfoIntfKey,'ripInfoIntfDefault':ripInfoIntfDefault,'rip2RoutesInfo':rip2RoutesInfo,'rip2RoutesInfoTable':rip2RoutesInfoTable,'rip2RoutesInfoEntry':rip2RoutesInfoEntry,_B8:rip2RoutesInfoDestIndex,_B9:rip2RoutesInfoNxtHopIndex,'rip2RoutesInfoDestination':rip2RoutesInfoDestination,'rip2RoutesInfoIpAddress':rip2RoutesInfoIpAddress,'rip2RoutesInfoMetric':rip2RoutesInfoMetric,'allowedNwInfo':allowedNwInfo,'allowedNwInfoTable':allowedNwInfoTable,'allowedNwInfoEntry':allowedNwInfoEntry,_BA:allowedNwInfoIndex,'allowedNwInfoIpver':allowedNwInfoIpver,'allowedNwInfoVlan':allowedNwInfoVlan,'allowedNwInfoBeginIpAddr':allowedNwInfoBeginIpAddr,'allowedNwInfoEndIpAddr':allowedNwInfoEndIpAddr,'allowedNwInfoNetMask':allowedNwInfoNetMask,'allowedNwInfoIp6Prefix':allowedNwInfoIp6Prefix,'layer3Oper':layer3Oper,'vrrpOper':vrrpOper,'vrrpOperVirtRtrTable':vrrpOperVirtRtrTable,'vrrpOperVirtRtrEntry':vrrpOperVirtRtrEntry,_BB:vrrpOperVirtRtrIndex,'vrrpOperVirtRtrBackup':vrrpOperVirtRtrBackup,'vrrpOperVirtRtrGroupBackup':vrrpOperVirtRtrGroupBackup,'ipOper':ipOper,'bgpOper':bgpOper,'bgpOperStart':bgpOperStart,'bgpOperStartPeerNum':bgpOperStartPeerNum,'bgpOperStartSess':bgpOperStartSess,'bgpOperStop':bgpOperStop,'bgpOperStopPeerNum':bgpOperStopPeerNum,'bgpOperStopSess':bgpOperStopSess,'garpOper':garpOper,'garpOperIpAddr':garpOperIpAddr,'garpOperVlanNumber':garpOperVlanNumber,'garpOperSend':garpOperSend})