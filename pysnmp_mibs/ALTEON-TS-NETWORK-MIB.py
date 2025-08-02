_A4='vrrpNewCfgVirtRtrGrpIndx'
_A3='vrrpCurCfgVirtRtrGrpIndx'
_A2='vrrpNewCfgIfIndx'
_A1='simple-text-password'
_A0='vrrpCurCfgIfIndx'
_z='vrrpNewCfgVirtRtrIndx'
_y='vrrpCurCfgVirtRtrIndx'
_x='vrrpOperVirtRtrIndex'
_w='routerLSAId'
_v='routerLSALinkIndex'
_u='routerLSAAreaIndex'
_t='ospfIfInfoIndex'
_s='ospfAreaInfoIndex'
_r='vrrpInfoVirtRtrIndex'
_q='arpInfoDestIp'
_p='indirect'
_o='multicast'
_n='martian'
_m='broadcast'
_l='ipRouteInfoIndx'
_k='ospfIntfIndex'
_j='ospfIntfNbrIndex'
_i='ospfIntfRxTxIndex'
_h='ospfAreaIntfIndex'
_g='ospfAreaNbrIndex'
_f='ospfAreaRxTxIndex'
_e='ospfNewCfgAreaId'
_d='ospfNewCfgAreaIndex'
_c='password'
_b='ospfCurCfgAreaId'
_a='ospfCurCfgAreaIndex'
_Z='roundrobin'
_Y='strict'
_X='ipFwdNewCfgLocalIndex'
_W='ipFwdCurCfgLocalIndex'
_V='ipFwdNewCfgPortIndex'
_U='ipFwdCurCfgPortIndex'
_T='ipNewCfgStaticRouteIndx'
_S='ipCurCfgStaticRouteIndx'
_R='ipNewCfgGwIndex'
_Q='ipCurCfgGwIndex'
_P='ipNewCfgIntfIndex'
_O='ipCurCfgIntfIndex'
_N='backup'
_M='DisplayString'
_L='off'
_K='on'
_J='none'
_I='delete'
_H='other'
_G='ALTEON-TS-NETWORK-MIB'
_F='disabled'
_E='enabled'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch,=mibBuilder.importSymbols('ALTEON-ROOT-MIB','switch')
information,operCmds,stats=mibBuilder.importSymbols('ALTEON-TIGON-SWITCH-MIB','information','operCmds','stats')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention')
_Iprouting_ObjectIdentity=ObjectIdentity
iprouting=_Iprouting_ObjectIdentity((1,3,6,1,4,1,1872,2,1,3))
_IpInterfaceTableMax_Type=Integer32
_IpInterfaceTableMax_Object=MibScalar
ipInterfaceTableMax=_IpInterfaceTableMax_Object((1,3,6,1,4,1,1872,2,1,3,1),_IpInterfaceTableMax_Type())
ipInterfaceTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipInterfaceTableMax.setStatus(_A)
_IpCurCfgIntfTable_Object=MibTable
ipCurCfgIntfTable=_IpCurCfgIntfTable_Object((1,3,6,1,4,1,1872,2,1,3,2))
if mibBuilder.loadTexts:ipCurCfgIntfTable.setStatus(_A)
_IpCurCfgIntfEntry_Object=MibTableRow
ipCurCfgIntfEntry=_IpCurCfgIntfEntry_Object((1,3,6,1,4,1,1872,2,1,3,2,1))
ipCurCfgIntfEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:ipCurCfgIntfEntry.setStatus(_A)
_IpCurCfgIntfIndex_Type=Integer32
_IpCurCfgIntfIndex_Object=MibTableColumn
ipCurCfgIntfIndex=_IpCurCfgIntfIndex_Object((1,3,6,1,4,1,1872,2,1,3,2,1,1),_IpCurCfgIntfIndex_Type())
ipCurCfgIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfIndex.setStatus(_A)
_IpCurCfgIntfAddr_Type=IpAddress
_IpCurCfgIntfAddr_Object=MibTableColumn
ipCurCfgIntfAddr=_IpCurCfgIntfAddr_Object((1,3,6,1,4,1,1872,2,1,3,2,1,2),_IpCurCfgIntfAddr_Type())
ipCurCfgIntfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfAddr.setStatus(_A)
_IpCurCfgIntfMask_Type=IpAddress
_IpCurCfgIntfMask_Object=MibTableColumn
ipCurCfgIntfMask=_IpCurCfgIntfMask_Object((1,3,6,1,4,1,1872,2,1,3,2,1,3),_IpCurCfgIntfMask_Type())
ipCurCfgIntfMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfMask.setStatus(_A)
_IpCurCfgIntfBroadcast_Type=IpAddress
_IpCurCfgIntfBroadcast_Object=MibTableColumn
ipCurCfgIntfBroadcast=_IpCurCfgIntfBroadcast_Object((1,3,6,1,4,1,1872,2,1,3,2,1,4),_IpCurCfgIntfBroadcast_Type())
ipCurCfgIntfBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfBroadcast.setStatus(_A)
class _IpCurCfgIntfVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_IpCurCfgIntfVlan_Type.__name__=_C
_IpCurCfgIntfVlan_Object=MibTableColumn
ipCurCfgIntfVlan=_IpCurCfgIntfVlan_Object((1,3,6,1,4,1,1872,2,1,3,2,1,5),_IpCurCfgIntfVlan_Type())
ipCurCfgIntfVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfVlan.setStatus(_A)
class _IpCurCfgIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpCurCfgIntfState_Type.__name__=_C
_IpCurCfgIntfState_Object=MibTableColumn
ipCurCfgIntfState=_IpCurCfgIntfState_Object((1,3,6,1,4,1,1872,2,1,3,2,1,6),_IpCurCfgIntfState_Type())
ipCurCfgIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfState.setStatus(_A)
class _IpCurCfgIntfBootpRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_IpCurCfgIntfBootpRelay_Type.__name__=_C
_IpCurCfgIntfBootpRelay_Object=MibTableColumn
ipCurCfgIntfBootpRelay=_IpCurCfgIntfBootpRelay_Object((1,3,6,1,4,1,1872,2,1,3,2,1,7),_IpCurCfgIntfBootpRelay_Type())
ipCurCfgIntfBootpRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgIntfBootpRelay.setStatus(_A)
_IpNewCfgIntfTable_Object=MibTable
ipNewCfgIntfTable=_IpNewCfgIntfTable_Object((1,3,6,1,4,1,1872,2,1,3,3))
if mibBuilder.loadTexts:ipNewCfgIntfTable.setStatus(_A)
_IpNewCfgIntfEntry_Object=MibTableRow
ipNewCfgIntfEntry=_IpNewCfgIntfEntry_Object((1,3,6,1,4,1,1872,2,1,3,3,1))
ipNewCfgIntfEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:ipNewCfgIntfEntry.setStatus(_A)
_IpNewCfgIntfIndex_Type=Integer32
_IpNewCfgIntfIndex_Object=MibTableColumn
ipNewCfgIntfIndex=_IpNewCfgIntfIndex_Object((1,3,6,1,4,1,1872,2,1,3,3,1,1),_IpNewCfgIntfIndex_Type())
ipNewCfgIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgIntfIndex.setStatus(_A)
_IpNewCfgIntfAddr_Type=IpAddress
_IpNewCfgIntfAddr_Object=MibTableColumn
ipNewCfgIntfAddr=_IpNewCfgIntfAddr_Object((1,3,6,1,4,1,1872,2,1,3,3,1,2),_IpNewCfgIntfAddr_Type())
ipNewCfgIntfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfAddr.setStatus(_A)
_IpNewCfgIntfMask_Type=IpAddress
_IpNewCfgIntfMask_Object=MibTableColumn
ipNewCfgIntfMask=_IpNewCfgIntfMask_Object((1,3,6,1,4,1,1872,2,1,3,3,1,3),_IpNewCfgIntfMask_Type())
ipNewCfgIntfMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfMask.setStatus(_A)
_IpNewCfgIntfBroadcast_Type=IpAddress
_IpNewCfgIntfBroadcast_Object=MibTableColumn
ipNewCfgIntfBroadcast=_IpNewCfgIntfBroadcast_Object((1,3,6,1,4,1,1872,2,1,3,3,1,4),_IpNewCfgIntfBroadcast_Type())
ipNewCfgIntfBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfBroadcast.setStatus(_A)
class _IpNewCfgIntfVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_IpNewCfgIntfVlan_Type.__name__=_C
_IpNewCfgIntfVlan_Object=MibTableColumn
ipNewCfgIntfVlan=_IpNewCfgIntfVlan_Object((1,3,6,1,4,1,1872,2,1,3,3,1,5),_IpNewCfgIntfVlan_Type())
ipNewCfgIntfVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfVlan.setStatus(_A)
class _IpNewCfgIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpNewCfgIntfState_Type.__name__=_C
_IpNewCfgIntfState_Object=MibTableColumn
ipNewCfgIntfState=_IpNewCfgIntfState_Object((1,3,6,1,4,1,1872,2,1,3,3,1,6),_IpNewCfgIntfState_Type())
ipNewCfgIntfState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfState.setStatus(_A)
class _IpNewCfgIntfDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpNewCfgIntfDelete_Type.__name__=_C
_IpNewCfgIntfDelete_Object=MibTableColumn
ipNewCfgIntfDelete=_IpNewCfgIntfDelete_Object((1,3,6,1,4,1,1872,2,1,3,3,1,7),_IpNewCfgIntfDelete_Type())
ipNewCfgIntfDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfDelete.setStatus(_A)
class _IpNewCfgIntfBootpRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_IpNewCfgIntfBootpRelay_Type.__name__=_C
_IpNewCfgIntfBootpRelay_Object=MibTableColumn
ipNewCfgIntfBootpRelay=_IpNewCfgIntfBootpRelay_Object((1,3,6,1,4,1,1872,2,1,3,3,1,8),_IpNewCfgIntfBootpRelay_Type())
ipNewCfgIntfBootpRelay.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgIntfBootpRelay.setStatus(_A)
_IpGatewayTableMax_Type=Integer32
_IpGatewayTableMax_Object=MibScalar
ipGatewayTableMax=_IpGatewayTableMax_Object((1,3,6,1,4,1,1872,2,1,3,4),_IpGatewayTableMax_Type())
ipGatewayTableMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipGatewayTableMax.setStatus(_A)
_IpCurCfgGwTable_Object=MibTable
ipCurCfgGwTable=_IpCurCfgGwTable_Object((1,3,6,1,4,1,1872,2,1,3,5))
if mibBuilder.loadTexts:ipCurCfgGwTable.setStatus(_A)
_IpCurCfgGwEntry_Object=MibTableRow
ipCurCfgGwEntry=_IpCurCfgGwEntry_Object((1,3,6,1,4,1,1872,2,1,3,5,1))
ipCurCfgGwEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:ipCurCfgGwEntry.setStatus(_A)
_IpCurCfgGwIndex_Type=Integer32
_IpCurCfgGwIndex_Object=MibTableColumn
ipCurCfgGwIndex=_IpCurCfgGwIndex_Object((1,3,6,1,4,1,1872,2,1,3,5,1,1),_IpCurCfgGwIndex_Type())
ipCurCfgGwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwIndex.setStatus(_A)
_IpCurCfgGwAddr_Type=IpAddress
_IpCurCfgGwAddr_Object=MibTableColumn
ipCurCfgGwAddr=_IpCurCfgGwAddr_Object((1,3,6,1,4,1,1872,2,1,3,5,1,2),_IpCurCfgGwAddr_Type())
ipCurCfgGwAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwAddr.setStatus(_A)
class _IpCurCfgGwInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_IpCurCfgGwInterval_Type.__name__=_C
_IpCurCfgGwInterval_Object=MibTableColumn
ipCurCfgGwInterval=_IpCurCfgGwInterval_Object((1,3,6,1,4,1,1872,2,1,3,5,1,3),_IpCurCfgGwInterval_Type())
ipCurCfgGwInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwInterval.setStatus(_A)
class _IpCurCfgGwRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_IpCurCfgGwRetry_Type.__name__=_C
_IpCurCfgGwRetry_Object=MibTableColumn
ipCurCfgGwRetry=_IpCurCfgGwRetry_Object((1,3,6,1,4,1,1872,2,1,3,5,1,4),_IpCurCfgGwRetry_Type())
ipCurCfgGwRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwRetry.setStatus(_A)
class _IpCurCfgGwState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpCurCfgGwState_Type.__name__=_C
_IpCurCfgGwState_Object=MibTableColumn
ipCurCfgGwState=_IpCurCfgGwState_Object((1,3,6,1,4,1,1872,2,1,3,5,1,5),_IpCurCfgGwState_Type())
ipCurCfgGwState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwState.setStatus(_A)
class _IpCurCfgGwArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpCurCfgGwArp_Type.__name__=_C
_IpCurCfgGwArp_Object=MibTableColumn
ipCurCfgGwArp=_IpCurCfgGwArp_Object((1,3,6,1,4,1,1872,2,1,3,5,1,6),_IpCurCfgGwArp_Type())
ipCurCfgGwArp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwArp.setStatus(_A)
class _IpCurCfgGwVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_IpCurCfgGwVlan_Type.__name__=_C
_IpCurCfgGwVlan_Object=MibTableColumn
ipCurCfgGwVlan=_IpCurCfgGwVlan_Object((1,3,6,1,4,1,1872,2,1,3,5,1,7),_IpCurCfgGwVlan_Type())
ipCurCfgGwVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwVlan.setStatus(_A)
_IpNewCfgGwTable_Object=MibTable
ipNewCfgGwTable=_IpNewCfgGwTable_Object((1,3,6,1,4,1,1872,2,1,3,6))
if mibBuilder.loadTexts:ipNewCfgGwTable.setStatus(_A)
_IpNewCfgGwEntry_Object=MibTableRow
ipNewCfgGwEntry=_IpNewCfgGwEntry_Object((1,3,6,1,4,1,1872,2,1,3,6,1))
ipNewCfgGwEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:ipNewCfgGwEntry.setStatus(_A)
_IpNewCfgGwIndex_Type=Integer32
_IpNewCfgGwIndex_Object=MibTableColumn
ipNewCfgGwIndex=_IpNewCfgGwIndex_Object((1,3,6,1,4,1,1872,2,1,3,6,1,1),_IpNewCfgGwIndex_Type())
ipNewCfgGwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgGwIndex.setStatus(_A)
_IpNewCfgGwAddr_Type=IpAddress
_IpNewCfgGwAddr_Object=MibTableColumn
ipNewCfgGwAddr=_IpNewCfgGwAddr_Object((1,3,6,1,4,1,1872,2,1,3,6,1,2),_IpNewCfgGwAddr_Type())
ipNewCfgGwAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwAddr.setStatus(_A)
class _IpNewCfgGwInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_IpNewCfgGwInterval_Type.__name__=_C
_IpNewCfgGwInterval_Object=MibTableColumn
ipNewCfgGwInterval=_IpNewCfgGwInterval_Object((1,3,6,1,4,1,1872,2,1,3,6,1,3),_IpNewCfgGwInterval_Type())
ipNewCfgGwInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwInterval.setStatus(_A)
class _IpNewCfgGwRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_IpNewCfgGwRetry_Type.__name__=_C
_IpNewCfgGwRetry_Object=MibTableColumn
ipNewCfgGwRetry=_IpNewCfgGwRetry_Object((1,3,6,1,4,1,1872,2,1,3,6,1,4),_IpNewCfgGwRetry_Type())
ipNewCfgGwRetry.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwRetry.setStatus(_A)
class _IpNewCfgGwState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpNewCfgGwState_Type.__name__=_C
_IpNewCfgGwState_Object=MibTableColumn
ipNewCfgGwState=_IpNewCfgGwState_Object((1,3,6,1,4,1,1872,2,1,3,6,1,5),_IpNewCfgGwState_Type())
ipNewCfgGwState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwState.setStatus(_A)
class _IpNewCfgGwDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpNewCfgGwDelete_Type.__name__=_C
_IpNewCfgGwDelete_Object=MibTableColumn
ipNewCfgGwDelete=_IpNewCfgGwDelete_Object((1,3,6,1,4,1,1872,2,1,3,6,1,6),_IpNewCfgGwDelete_Type())
ipNewCfgGwDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwDelete.setStatus(_A)
class _IpNewCfgGwArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpNewCfgGwArp_Type.__name__=_C
_IpNewCfgGwArp_Object=MibTableColumn
ipNewCfgGwArp=_IpNewCfgGwArp_Object((1,3,6,1,4,1,1872,2,1,3,6,1,7),_IpNewCfgGwArp_Type())
ipNewCfgGwArp.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwArp.setStatus(_A)
class _IpNewCfgGwVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_IpNewCfgGwVlan_Type.__name__=_C
_IpNewCfgGwVlan_Object=MibTableColumn
ipNewCfgGwVlan=_IpNewCfgGwVlan_Object((1,3,6,1,4,1,1872,2,1,3,6,1,8),_IpNewCfgGwVlan_Type())
ipNewCfgGwVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwVlan.setStatus(_A)
_IpCurCfgStaticRouteTable_Object=MibTable
ipCurCfgStaticRouteTable=_IpCurCfgStaticRouteTable_Object((1,3,6,1,4,1,1872,2,1,3,7))
if mibBuilder.loadTexts:ipCurCfgStaticRouteTable.setStatus(_A)
_IpCurCfgStaticRouteEntry_Object=MibTableRow
ipCurCfgStaticRouteEntry=_IpCurCfgStaticRouteEntry_Object((1,3,6,1,4,1,1872,2,1,3,7,1))
ipCurCfgStaticRouteEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:ipCurCfgStaticRouteEntry.setStatus(_A)
_IpCurCfgStaticRouteIndx_Type=Integer32
_IpCurCfgStaticRouteIndx_Object=MibTableColumn
ipCurCfgStaticRouteIndx=_IpCurCfgStaticRouteIndx_Object((1,3,6,1,4,1,1872,2,1,3,7,1,1),_IpCurCfgStaticRouteIndx_Type())
ipCurCfgStaticRouteIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteIndx.setStatus(_A)
_IpCurCfgStaticRouteDestIp_Type=IpAddress
_IpCurCfgStaticRouteDestIp_Object=MibTableColumn
ipCurCfgStaticRouteDestIp=_IpCurCfgStaticRouteDestIp_Object((1,3,6,1,4,1,1872,2,1,3,7,1,2),_IpCurCfgStaticRouteDestIp_Type())
ipCurCfgStaticRouteDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteDestIp.setStatus(_A)
_IpCurCfgStaticRouteMask_Type=IpAddress
_IpCurCfgStaticRouteMask_Object=MibTableColumn
ipCurCfgStaticRouteMask=_IpCurCfgStaticRouteMask_Object((1,3,6,1,4,1,1872,2,1,3,7,1,3),_IpCurCfgStaticRouteMask_Type())
ipCurCfgStaticRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteMask.setStatus(_A)
_IpCurCfgStaticRouteGateway_Type=IpAddress
_IpCurCfgStaticRouteGateway_Object=MibTableColumn
ipCurCfgStaticRouteGateway=_IpCurCfgStaticRouteGateway_Object((1,3,6,1,4,1,1872,2,1,3,7,1,4),_IpCurCfgStaticRouteGateway_Type())
ipCurCfgStaticRouteGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteGateway.setStatus(_A)
_IpCurCfgStaticRouteInterface_Type=Integer32
_IpCurCfgStaticRouteInterface_Object=MibTableColumn
ipCurCfgStaticRouteInterface=_IpCurCfgStaticRouteInterface_Object((1,3,6,1,4,1,1872,2,1,3,7,1,5),_IpCurCfgStaticRouteInterface_Type())
ipCurCfgStaticRouteInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgStaticRouteInterface.setStatus(_A)
_IpNewCfgStaticRouteTable_Object=MibTable
ipNewCfgStaticRouteTable=_IpNewCfgStaticRouteTable_Object((1,3,6,1,4,1,1872,2,1,3,8))
if mibBuilder.loadTexts:ipNewCfgStaticRouteTable.setStatus(_A)
_IpNewCfgStaticRouteEntry_Object=MibTableRow
ipNewCfgStaticRouteEntry=_IpNewCfgStaticRouteEntry_Object((1,3,6,1,4,1,1872,2,1,3,8,1))
ipNewCfgStaticRouteEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:ipNewCfgStaticRouteEntry.setStatus(_A)
_IpNewCfgStaticRouteIndx_Type=Integer32
_IpNewCfgStaticRouteIndx_Object=MibTableColumn
ipNewCfgStaticRouteIndx=_IpNewCfgStaticRouteIndx_Object((1,3,6,1,4,1,1872,2,1,3,8,1,1),_IpNewCfgStaticRouteIndx_Type())
ipNewCfgStaticRouteIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNewCfgStaticRouteIndx.setStatus(_A)
_IpNewCfgStaticRouteDestIp_Type=IpAddress
_IpNewCfgStaticRouteDestIp_Object=MibTableColumn
ipNewCfgStaticRouteDestIp=_IpNewCfgStaticRouteDestIp_Object((1,3,6,1,4,1,1872,2,1,3,8,1,2),_IpNewCfgStaticRouteDestIp_Type())
ipNewCfgStaticRouteDestIp.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteDestIp.setStatus(_A)
_IpNewCfgStaticRouteMask_Type=IpAddress
_IpNewCfgStaticRouteMask_Object=MibTableColumn
ipNewCfgStaticRouteMask=_IpNewCfgStaticRouteMask_Object((1,3,6,1,4,1,1872,2,1,3,8,1,3),_IpNewCfgStaticRouteMask_Type())
ipNewCfgStaticRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteMask.setStatus(_A)
_IpNewCfgStaticRouteGateway_Type=IpAddress
_IpNewCfgStaticRouteGateway_Object=MibTableColumn
ipNewCfgStaticRouteGateway=_IpNewCfgStaticRouteGateway_Object((1,3,6,1,4,1,1872,2,1,3,8,1,4),_IpNewCfgStaticRouteGateway_Type())
ipNewCfgStaticRouteGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteGateway.setStatus(_A)
class _IpNewCfgStaticRouteAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpNewCfgStaticRouteAction_Type.__name__=_C
_IpNewCfgStaticRouteAction_Object=MibTableColumn
ipNewCfgStaticRouteAction=_IpNewCfgStaticRouteAction_Object((1,3,6,1,4,1,1872,2,1,3,8,1,5),_IpNewCfgStaticRouteAction_Type())
ipNewCfgStaticRouteAction.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteAction.setStatus(_A)
_IpNewCfgStaticRouteInterface_Type=Integer32
_IpNewCfgStaticRouteInterface_Object=MibTableColumn
ipNewCfgStaticRouteInterface=_IpNewCfgStaticRouteInterface_Object((1,3,6,1,4,1,1872,2,1,3,8,1,6),_IpNewCfgStaticRouteInterface_Type())
ipNewCfgStaticRouteInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgStaticRouteInterface.setStatus(_A)
_IpForward_ObjectIdentity=ObjectIdentity
ipForward=_IpForward_ObjectIdentity((1,3,6,1,4,1,1872,2,1,3,9))
_RipConfig_ObjectIdentity=ObjectIdentity
ripConfig=_RipConfig_ObjectIdentity((1,3,6,1,4,1,1872,2,1,3,9,1))
class _RipCurCfgSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipCurCfgSupply_Type.__name__=_C
_RipCurCfgSupply_Object=MibScalar
ripCurCfgSupply=_RipCurCfgSupply_Object((1,3,6,1,4,1,1872,2,1,3,9,1,1),_RipCurCfgSupply_Type())
ripCurCfgSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgSupply.setStatus(_A)
class _RipNewCfgSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipNewCfgSupply_Type.__name__=_C
_RipNewCfgSupply_Object=MibScalar
ripNewCfgSupply=_RipNewCfgSupply_Object((1,3,6,1,4,1,1872,2,1,3,9,1,2),_RipNewCfgSupply_Type())
ripNewCfgSupply.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgSupply.setStatus(_A)
class _RipCurCfgListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipCurCfgListen_Type.__name__=_C
_RipCurCfgListen_Object=MibScalar
ripCurCfgListen=_RipCurCfgListen_Object((1,3,6,1,4,1,1872,2,1,3,9,1,3),_RipCurCfgListen_Type())
ripCurCfgListen.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgListen.setStatus(_A)
class _RipNewCfgListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipNewCfgListen_Type.__name__=_C
_RipNewCfgListen_Object=MibScalar
ripNewCfgListen=_RipNewCfgListen_Object((1,3,6,1,4,1,1872,2,1,3,9,1,4),_RipNewCfgListen_Type())
ripNewCfgListen.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgListen.setStatus(_A)
class _RipCurCfgDefListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipCurCfgDefListen_Type.__name__=_C
_RipCurCfgDefListen_Object=MibScalar
ripCurCfgDefListen=_RipCurCfgDefListen_Object((1,3,6,1,4,1,1872,2,1,3,9,1,5),_RipCurCfgDefListen_Type())
ripCurCfgDefListen.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgDefListen.setStatus(_A)
class _RipNewCfgDefListen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipNewCfgDefListen_Type.__name__=_C
_RipNewCfgDefListen_Object=MibScalar
ripNewCfgDefListen=_RipNewCfgDefListen_Object((1,3,6,1,4,1,1872,2,1,3,9,1,6),_RipNewCfgDefListen_Type())
ripNewCfgDefListen.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgDefListen.setStatus(_A)
class _RipCurCfgStaticSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipCurCfgStaticSupply_Type.__name__=_C
_RipCurCfgStaticSupply_Object=MibScalar
ripCurCfgStaticSupply=_RipCurCfgStaticSupply_Object((1,3,6,1,4,1,1872,2,1,3,9,1,7),_RipCurCfgStaticSupply_Type())
ripCurCfgStaticSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgStaticSupply.setStatus(_A)
class _RipNewCfgStaticSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipNewCfgStaticSupply_Type.__name__=_C
_RipNewCfgStaticSupply_Object=MibScalar
ripNewCfgStaticSupply=_RipNewCfgStaticSupply_Object((1,3,6,1,4,1,1872,2,1,3,9,1,8),_RipNewCfgStaticSupply_Type())
ripNewCfgStaticSupply.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgStaticSupply.setStatus(_A)
class _RipCurCfgUpdatePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_RipCurCfgUpdatePeriod_Type.__name__=_C
_RipCurCfgUpdatePeriod_Object=MibScalar
ripCurCfgUpdatePeriod=_RipCurCfgUpdatePeriod_Object((1,3,6,1,4,1,1872,2,1,3,9,1,9),_RipCurCfgUpdatePeriod_Type())
ripCurCfgUpdatePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgUpdatePeriod.setStatus(_A)
class _RipNewCfgUpdatePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_RipNewCfgUpdatePeriod_Type.__name__=_C
_RipNewCfgUpdatePeriod_Object=MibScalar
ripNewCfgUpdatePeriod=_RipNewCfgUpdatePeriod_Object((1,3,6,1,4,1,1872,2,1,3,9,1,10),_RipNewCfgUpdatePeriod_Type())
ripNewCfgUpdatePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgUpdatePeriod.setStatus(_A)
class _RipCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_K,2),(_L,3)))
_RipCurCfgState_Type.__name__=_C
_RipCurCfgState_Object=MibScalar
ripCurCfgState=_RipCurCfgState_Object((1,3,6,1,4,1,1872,2,1,3,9,1,11),_RipCurCfgState_Type())
ripCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgState.setStatus(_A)
class _RipNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_K,2),(_L,3)))
_RipNewCfgState_Type.__name__=_C
_RipNewCfgState_Object=MibScalar
ripNewCfgState=_RipNewCfgState_Object((1,3,6,1,4,1,1872,2,1,3,9,1,12),_RipNewCfgState_Type())
ripNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgState.setStatus(_A)
class _RipCurCfgPoisonReverse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipCurCfgPoisonReverse_Type.__name__=_C
_RipCurCfgPoisonReverse_Object=MibScalar
ripCurCfgPoisonReverse=_RipCurCfgPoisonReverse_Object((1,3,6,1,4,1,1872,2,1,3,9,1,13),_RipCurCfgPoisonReverse_Type())
ripCurCfgPoisonReverse.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgPoisonReverse.setStatus(_A)
class _RipNewCfgPoisonReverse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipNewCfgPoisonReverse_Type.__name__=_C
_RipNewCfgPoisonReverse_Object=MibScalar
ripNewCfgPoisonReverse=_RipNewCfgPoisonReverse_Object((1,3,6,1,4,1,1872,2,1,3,9,1,14),_RipNewCfgPoisonReverse_Type())
ripNewCfgPoisonReverse.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgPoisonReverse.setStatus(_A)
class _RipCurCfgVip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipCurCfgVip_Type.__name__=_C
_RipCurCfgVip_Object=MibScalar
ripCurCfgVip=_RipCurCfgVip_Object((1,3,6,1,4,1,1872,2,1,3,9,1,15),_RipCurCfgVip_Type())
ripCurCfgVip.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCurCfgVip.setStatus(_A)
class _RipNewCfgVip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RipNewCfgVip_Type.__name__=_C
_RipNewCfgVip_Object=MibScalar
ripNewCfgVip=_RipNewCfgVip_Object((1,3,6,1,4,1,1872,2,1,3,9,1,16),_RipNewCfgVip_Type())
ripNewCfgVip.setMaxAccess(_D)
if mibBuilder.loadTexts:ripNewCfgVip.setStatus(_A)
_IpFwdCurCfgPortTable_Object=MibTable
ipFwdCurCfgPortTable=_IpFwdCurCfgPortTable_Object((1,3,6,1,4,1,1872,2,1,3,9,2))
if mibBuilder.loadTexts:ipFwdCurCfgPortTable.setStatus(_A)
_IpFwdCurCfgPortEntry_Object=MibTableRow
ipFwdCurCfgPortEntry=_IpFwdCurCfgPortEntry_Object((1,3,6,1,4,1,1872,2,1,3,9,2,1))
ipFwdCurCfgPortEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:ipFwdCurCfgPortEntry.setStatus(_A)
_IpFwdCurCfgPortIndex_Type=Integer32
_IpFwdCurCfgPortIndex_Object=MibTableColumn
ipFwdCurCfgPortIndex=_IpFwdCurCfgPortIndex_Object((1,3,6,1,4,1,1872,2,1,3,9,2,1,1),_IpFwdCurCfgPortIndex_Type())
ipFwdCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgPortIndex.setStatus(_A)
class _IpFwdCurCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpFwdCurCfgPortState_Type.__name__=_C
_IpFwdCurCfgPortState_Object=MibTableColumn
ipFwdCurCfgPortState=_IpFwdCurCfgPortState_Object((1,3,6,1,4,1,1872,2,1,3,9,2,1,2),_IpFwdCurCfgPortState_Type())
ipFwdCurCfgPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgPortState.setStatus(_A)
_IpFwdNewCfgPortTable_Object=MibTable
ipFwdNewCfgPortTable=_IpFwdNewCfgPortTable_Object((1,3,6,1,4,1,1872,2,1,3,9,3))
if mibBuilder.loadTexts:ipFwdNewCfgPortTable.setStatus(_A)
_IpFwdNewCfgPortEntry_Object=MibTableRow
ipFwdNewCfgPortEntry=_IpFwdNewCfgPortEntry_Object((1,3,6,1,4,1,1872,2,1,3,9,3,1))
ipFwdNewCfgPortEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:ipFwdNewCfgPortEntry.setStatus(_A)
_IpFwdNewCfgPortIndex_Type=Integer32
_IpFwdNewCfgPortIndex_Object=MibTableColumn
ipFwdNewCfgPortIndex=_IpFwdNewCfgPortIndex_Object((1,3,6,1,4,1,1872,2,1,3,9,3,1,1),_IpFwdNewCfgPortIndex_Type())
ipFwdNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdNewCfgPortIndex.setStatus(_A)
class _IpFwdNewCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpFwdNewCfgPortState_Type.__name__=_C
_IpFwdNewCfgPortState_Object=MibTableColumn
ipFwdNewCfgPortState=_IpFwdNewCfgPortState_Object((1,3,6,1,4,1,1872,2,1,3,9,3,1,2),_IpFwdNewCfgPortState_Type())
ipFwdNewCfgPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipFwdNewCfgPortState.setStatus(_A)
class _IpFwdCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_K,2),(_L,3)))
_IpFwdCurCfgState_Type.__name__=_C
_IpFwdCurCfgState_Object=MibScalar
ipFwdCurCfgState=_IpFwdCurCfgState_Object((1,3,6,1,4,1,1872,2,1,3,9,8),_IpFwdCurCfgState_Type())
ipFwdCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgState.setStatus(_A)
class _IpFwdNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_K,2),(_L,3)))
_IpFwdNewCfgState_Type.__name__=_C
_IpFwdNewCfgState_Object=MibScalar
ipFwdNewCfgState=_IpFwdNewCfgState_Object((1,3,6,1,4,1,1872,2,1,3,9,9),_IpFwdNewCfgState_Type())
ipFwdNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipFwdNewCfgState.setStatus(_A)
class _IpFwdCurCfgDirectedBcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpFwdCurCfgDirectedBcast_Type.__name__=_C
_IpFwdCurCfgDirectedBcast_Object=MibScalar
ipFwdCurCfgDirectedBcast=_IpFwdCurCfgDirectedBcast_Object((1,3,6,1,4,1,1872,2,1,3,9,10),_IpFwdCurCfgDirectedBcast_Type())
ipFwdCurCfgDirectedBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgDirectedBcast.setStatus(_A)
class _IpFwdNewCfgDirectedBcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpFwdNewCfgDirectedBcast_Type.__name__=_C
_IpFwdNewCfgDirectedBcast_Object=MibScalar
ipFwdNewCfgDirectedBcast=_IpFwdNewCfgDirectedBcast_Object((1,3,6,1,4,1,1872,2,1,3,9,11),_IpFwdNewCfgDirectedBcast_Type())
ipFwdNewCfgDirectedBcast.setMaxAccess(_D)
if mibBuilder.loadTexts:ipFwdNewCfgDirectedBcast.setStatus(_A)
_IpFwdPortTableMaxSize_Type=Integer32
_IpFwdPortTableMaxSize_Object=MibScalar
ipFwdPortTableMaxSize=_IpFwdPortTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,3,9,12),_IpFwdPortTableMaxSize_Type())
ipFwdPortTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdPortTableMaxSize.setStatus(_A)
_IpFwdLocalTableMaxSize_Type=Integer32
_IpFwdLocalTableMaxSize_Object=MibScalar
ipFwdLocalTableMaxSize=_IpFwdLocalTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,3,9,13),_IpFwdLocalTableMaxSize_Type())
ipFwdLocalTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdLocalTableMaxSize.setStatus(_A)
_IpFwdCurCfgLocalTable_Object=MibTable
ipFwdCurCfgLocalTable=_IpFwdCurCfgLocalTable_Object((1,3,6,1,4,1,1872,2,1,3,9,14))
if mibBuilder.loadTexts:ipFwdCurCfgLocalTable.setStatus(_A)
_IpFwdCurCfgLocalEntry_Object=MibTableRow
ipFwdCurCfgLocalEntry=_IpFwdCurCfgLocalEntry_Object((1,3,6,1,4,1,1872,2,1,3,9,14,1))
ipFwdCurCfgLocalEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:ipFwdCurCfgLocalEntry.setStatus(_A)
_IpFwdCurCfgLocalIndex_Type=Integer32
_IpFwdCurCfgLocalIndex_Object=MibTableColumn
ipFwdCurCfgLocalIndex=_IpFwdCurCfgLocalIndex_Object((1,3,6,1,4,1,1872,2,1,3,9,14,1,1),_IpFwdCurCfgLocalIndex_Type())
ipFwdCurCfgLocalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgLocalIndex.setStatus(_A)
_IpFwdCurCfgLocalSubnet_Type=IpAddress
_IpFwdCurCfgLocalSubnet_Object=MibTableColumn
ipFwdCurCfgLocalSubnet=_IpFwdCurCfgLocalSubnet_Object((1,3,6,1,4,1,1872,2,1,3,9,14,1,2),_IpFwdCurCfgLocalSubnet_Type())
ipFwdCurCfgLocalSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgLocalSubnet.setStatus(_A)
_IpFwdCurCfgLocalMask_Type=IpAddress
_IpFwdCurCfgLocalMask_Object=MibTableColumn
ipFwdCurCfgLocalMask=_IpFwdCurCfgLocalMask_Object((1,3,6,1,4,1,1872,2,1,3,9,14,1,3),_IpFwdCurCfgLocalMask_Type())
ipFwdCurCfgLocalMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdCurCfgLocalMask.setStatus(_A)
_IpFwdNewCfgLocalTable_Object=MibTable
ipFwdNewCfgLocalTable=_IpFwdNewCfgLocalTable_Object((1,3,6,1,4,1,1872,2,1,3,9,15))
if mibBuilder.loadTexts:ipFwdNewCfgLocalTable.setStatus(_A)
_IpFwdNewCfgLocalEntry_Object=MibTableRow
ipFwdNewCfgLocalEntry=_IpFwdNewCfgLocalEntry_Object((1,3,6,1,4,1,1872,2,1,3,9,15,1))
ipFwdNewCfgLocalEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:ipFwdNewCfgLocalEntry.setStatus(_A)
_IpFwdNewCfgLocalIndex_Type=Integer32
_IpFwdNewCfgLocalIndex_Object=MibTableColumn
ipFwdNewCfgLocalIndex=_IpFwdNewCfgLocalIndex_Object((1,3,6,1,4,1,1872,2,1,3,9,15,1,1),_IpFwdNewCfgLocalIndex_Type())
ipFwdNewCfgLocalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFwdNewCfgLocalIndex.setStatus(_A)
_IpFwdNewCfgLocalSubnet_Type=IpAddress
_IpFwdNewCfgLocalSubnet_Object=MibTableColumn
ipFwdNewCfgLocalSubnet=_IpFwdNewCfgLocalSubnet_Object((1,3,6,1,4,1,1872,2,1,3,9,15,1,2),_IpFwdNewCfgLocalSubnet_Type())
ipFwdNewCfgLocalSubnet.setMaxAccess(_D)
if mibBuilder.loadTexts:ipFwdNewCfgLocalSubnet.setStatus(_A)
_IpFwdNewCfgLocalMask_Type=IpAddress
_IpFwdNewCfgLocalMask_Object=MibTableColumn
ipFwdNewCfgLocalMask=_IpFwdNewCfgLocalMask_Object((1,3,6,1,4,1,1872,2,1,3,9,15,1,3),_IpFwdNewCfgLocalMask_Type())
ipFwdNewCfgLocalMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipFwdNewCfgLocalMask.setStatus(_A)
class _IpFwdNewCfgLocalDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpFwdNewCfgLocalDelete_Type.__name__=_C
_IpFwdNewCfgLocalDelete_Object=MibTableColumn
ipFwdNewCfgLocalDelete=_IpFwdNewCfgLocalDelete_Object((1,3,6,1,4,1,1872,2,1,3,9,15,1,4),_IpFwdNewCfgLocalDelete_Type())
ipFwdNewCfgLocalDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:ipFwdNewCfgLocalDelete.setStatus(_A)
class _ArpCurCfgReARPPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,120))
_ArpCurCfgReARPPeriod_Type.__name__=_C
_ArpCurCfgReARPPeriod_Object=MibScalar
arpCurCfgReARPPeriod=_ArpCurCfgReARPPeriod_Object((1,3,6,1,4,1,1872,2,1,3,10),_ArpCurCfgReARPPeriod_Type())
arpCurCfgReARPPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:arpCurCfgReARPPeriod.setStatus(_A)
class _ArpNewCfgReARPPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,120))
_ArpNewCfgReARPPeriod_Type.__name__=_C
_ArpNewCfgReARPPeriod_Object=MibScalar
arpNewCfgReARPPeriod=_ArpNewCfgReARPPeriod_Object((1,3,6,1,4,1,1872,2,1,3,11),_ArpNewCfgReARPPeriod_Type())
arpNewCfgReARPPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:arpNewCfgReARPPeriod.setStatus(_A)
class _IpCurCfgGwMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_IpCurCfgGwMetric_Type.__name__=_C
_IpCurCfgGwMetric_Object=MibScalar
ipCurCfgGwMetric=_IpCurCfgGwMetric_Object((1,3,6,1,4,1,1872,2,1,3,12),_IpCurCfgGwMetric_Type())
ipCurCfgGwMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgGwMetric.setStatus(_A)
class _IpNewCfgGwMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_IpNewCfgGwMetric_Type.__name__=_C
_IpNewCfgGwMetric_Object=MibScalar
ipNewCfgGwMetric=_IpNewCfgGwMetric_Object((1,3,6,1,4,1,1872,2,1,3,13),_IpNewCfgGwMetric_Type())
ipNewCfgGwMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgGwMetric.setStatus(_A)
_IpCurCfgBootpAddr_Type=IpAddress
_IpCurCfgBootpAddr_Object=MibScalar
ipCurCfgBootpAddr=_IpCurCfgBootpAddr_Object((1,3,6,1,4,1,1872,2,1,3,14),_IpCurCfgBootpAddr_Type())
ipCurCfgBootpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgBootpAddr.setStatus(_A)
_IpNewCfgBootpAddr_Type=IpAddress
_IpNewCfgBootpAddr_Object=MibScalar
ipNewCfgBootpAddr=_IpNewCfgBootpAddr_Object((1,3,6,1,4,1,1872,2,1,3,15),_IpNewCfgBootpAddr_Type())
ipNewCfgBootpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgBootpAddr.setStatus(_A)
_IpCurCfgBootpAddr2_Type=IpAddress
_IpCurCfgBootpAddr2_Object=MibScalar
ipCurCfgBootpAddr2=_IpCurCfgBootpAddr2_Object((1,3,6,1,4,1,1872,2,1,3,16),_IpCurCfgBootpAddr2_Type())
ipCurCfgBootpAddr2.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgBootpAddr2.setStatus(_A)
_IpNewCfgBootpAddr2_Type=IpAddress
_IpNewCfgBootpAddr2_Object=MibScalar
ipNewCfgBootpAddr2=_IpNewCfgBootpAddr2_Object((1,3,6,1,4,1,1872,2,1,3,17),_IpNewCfgBootpAddr2_Type())
ipNewCfgBootpAddr2.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgBootpAddr2.setStatus(_A)
class _IpCurCfgBootpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpCurCfgBootpState_Type.__name__=_C
_IpCurCfgBootpState_Object=MibScalar
ipCurCfgBootpState=_IpCurCfgBootpState_Object((1,3,6,1,4,1,1872,2,1,3,18),_IpCurCfgBootpState_Type())
ipCurCfgBootpState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipCurCfgBootpState.setStatus(_A)
class _IpNewCfgBootpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_IpNewCfgBootpState_Type.__name__=_C
_IpNewCfgBootpState_Object=MibScalar
ipNewCfgBootpState=_IpNewCfgBootpState_Object((1,3,6,1,4,1,1872,2,1,3,19),_IpNewCfgBootpState_Type())
ipNewCfgBootpState.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNewCfgBootpState.setStatus(_A)
_IpStaticRouteTableMaxSize_Type=Integer32
_IpStaticRouteTableMaxSize_Object=MibScalar
ipStaticRouteTableMaxSize=_IpStaticRouteTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,3,20),_IpStaticRouteTableMaxSize_Type())
ipStaticRouteTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ipStaticRouteTableMaxSize.setStatus(_A)
_OspfCfg_ObjectIdentity=ObjectIdentity
ospfCfg=_OspfCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,1,3,21))
_OspfGeneral_ObjectIdentity=ObjectIdentity
ospfGeneral=_OspfGeneral_ObjectIdentity((1,3,6,1,4,1,1872,2,1,3,21,1))
class _OspfCurCfgDefaultRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfCurCfgDefaultRouteMetric_Type.__name__=_C
_OspfCurCfgDefaultRouteMetric_Object=MibScalar
ospfCurCfgDefaultRouteMetric=_OspfCurCfgDefaultRouteMetric_Object((1,3,6,1,4,1,1872,2,1,3,21,1,1),_OspfCurCfgDefaultRouteMetric_Type())
ospfCurCfgDefaultRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgDefaultRouteMetric.setStatus(_A)
class _OspfNewCfgDefaultRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_OspfNewCfgDefaultRouteMetric_Type.__name__=_C
_OspfNewCfgDefaultRouteMetric_Object=MibScalar
ospfNewCfgDefaultRouteMetric=_OspfNewCfgDefaultRouteMetric_Object((1,3,6,1,4,1,1872,2,1,3,21,1,2),_OspfNewCfgDefaultRouteMetric_Type())
ospfNewCfgDefaultRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgDefaultRouteMetric.setStatus(_A)
class _OspfCurCfgDefaultRouteMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('type1',2),('type2',3)))
_OspfCurCfgDefaultRouteMetricType_Type.__name__=_C
_OspfCurCfgDefaultRouteMetricType_Object=MibScalar
ospfCurCfgDefaultRouteMetricType=_OspfCurCfgDefaultRouteMetricType_Object((1,3,6,1,4,1,1872,2,1,3,21,1,3),_OspfCurCfgDefaultRouteMetricType_Type())
ospfCurCfgDefaultRouteMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgDefaultRouteMetricType.setStatus(_A)
class _OspfNewCfgDefaultRouteMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('type1',2),('type2',3)))
_OspfNewCfgDefaultRouteMetricType_Type.__name__=_C
_OspfNewCfgDefaultRouteMetricType_Object=MibScalar
ospfNewCfgDefaultRouteMetricType=_OspfNewCfgDefaultRouteMetricType_Object((1,3,6,1,4,1,1872,2,1,3,21,1,4),_OspfNewCfgDefaultRouteMetricType_Type())
ospfNewCfgDefaultRouteMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgDefaultRouteMetricType.setStatus(_A)
_OspfIntfTableMaxSize_Type=Integer32
_OspfIntfTableMaxSize_Object=MibScalar
ospfIntfTableMaxSize=_OspfIntfTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,3,21,1,5),_OspfIntfTableMaxSize_Type())
ospfIntfTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTableMaxSize.setStatus(_A)
_OspfAreaTableMaxSize_Type=Integer32
_OspfAreaTableMaxSize_Object=MibScalar
ospfAreaTableMaxSize=_OspfAreaTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,3,21,1,6),_OspfAreaTableMaxSize_Type())
ospfAreaTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTableMaxSize.setStatus(_A)
_OspfRangeTableMaxSize_Type=Integer32
_OspfRangeTableMaxSize_Object=MibScalar
ospfRangeTableMaxSize=_OspfRangeTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,3,21,1,7),_OspfRangeTableMaxSize_Type())
ospfRangeTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRangeTableMaxSize.setStatus(_A)
_OspfVirtIntfTableMaxSize_Type=Integer32
_OspfVirtIntfTableMaxSize_Object=MibScalar
ospfVirtIntfTableMaxSize=_OspfVirtIntfTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,3,21,1,8),_OspfVirtIntfTableMaxSize_Type())
ospfVirtIntfTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIntfTableMaxSize.setStatus(_A)
_OspfHostTableMaxSize_Type=Integer32
_OspfHostTableMaxSize_Object=MibScalar
ospfHostTableMaxSize=_OspfHostTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,3,21,1,9),_OspfHostTableMaxSize_Type())
ospfHostTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfHostTableMaxSize.setStatus(_A)
_OspfCurCfgAreaTable_Object=MibTable
ospfCurCfgAreaTable=_OspfCurCfgAreaTable_Object((1,3,6,1,4,1,1872,2,1,3,21,2))
if mibBuilder.loadTexts:ospfCurCfgAreaTable.setStatus(_A)
_OspfCurCfgAreaEntry_Object=MibTableRow
ospfCurCfgAreaEntry=_OspfCurCfgAreaEntry_Object((1,3,6,1,4,1,1872,2,1,3,21,2,1))
ospfCurCfgAreaEntry.setIndexNames((0,_G,_a),(0,_G,_b))
if mibBuilder.loadTexts:ospfCurCfgAreaEntry.setStatus(_A)
class _OspfCurCfgAreaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_OspfCurCfgAreaIndex_Type.__name__=_C
_OspfCurCfgAreaIndex_Object=MibTableColumn
ospfCurCfgAreaIndex=_OspfCurCfgAreaIndex_Object((1,3,6,1,4,1,1872,2,1,3,21,2,1,1),_OspfCurCfgAreaIndex_Type())
ospfCurCfgAreaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaIndex.setStatus(_A)
_OspfCurCfgAreaId_Type=IpAddress
_OspfCurCfgAreaId_Object=MibTableColumn
ospfCurCfgAreaId=_OspfCurCfgAreaId_Object((1,3,6,1,4,1,1872,2,1,3,21,2,1,2),_OspfCurCfgAreaId_Type())
ospfCurCfgAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaId.setStatus(_A)
class _OspfCurCfgAreaSpfInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfCurCfgAreaSpfInterval_Type.__name__=_C
_OspfCurCfgAreaSpfInterval_Object=MibTableColumn
ospfCurCfgAreaSpfInterval=_OspfCurCfgAreaSpfInterval_Object((1,3,6,1,4,1,1872,2,1,3,21,2,1,3),_OspfCurCfgAreaSpfInterval_Type())
ospfCurCfgAreaSpfInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaSpfInterval.setStatus(_A)
class _OspfCurCfgAreaAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_c,2)))
_OspfCurCfgAreaAuthType_Type.__name__=_C
_OspfCurCfgAreaAuthType_Object=MibTableColumn
ospfCurCfgAreaAuthType=_OspfCurCfgAreaAuthType_Object((1,3,6,1,4,1,1872,2,1,3,21,2,1,4),_OspfCurCfgAreaAuthType_Type())
ospfCurCfgAreaAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCurCfgAreaAuthType.setStatus(_A)
_OspfNewCfgAreaTable_Object=MibTable
ospfNewCfgAreaTable=_OspfNewCfgAreaTable_Object((1,3,6,1,4,1,1872,2,1,3,21,3))
if mibBuilder.loadTexts:ospfNewCfgAreaTable.setStatus(_A)
_OspfNewCfgAreaEntry_Object=MibTableRow
ospfNewCfgAreaEntry=_OspfNewCfgAreaEntry_Object((1,3,6,1,4,1,1872,2,1,3,21,3,1))
ospfNewCfgAreaEntry.setIndexNames((0,_G,_d),(0,_G,_e))
if mibBuilder.loadTexts:ospfNewCfgAreaEntry.setStatus(_A)
class _OspfNewCfgAreaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_OspfNewCfgAreaIndex_Type.__name__=_C
_OspfNewCfgAreaIndex_Object=MibTableColumn
ospfNewCfgAreaIndex=_OspfNewCfgAreaIndex_Object((1,3,6,1,4,1,1872,2,1,3,21,3,1,1),_OspfNewCfgAreaIndex_Type())
ospfNewCfgAreaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgAreaIndex.setStatus(_A)
_OspfNewCfgAreaId_Type=IpAddress
_OspfNewCfgAreaId_Object=MibTableColumn
ospfNewCfgAreaId=_OspfNewCfgAreaId_Object((1,3,6,1,4,1,1872,2,1,3,21,3,1,2),_OspfNewCfgAreaId_Type())
ospfNewCfgAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNewCfgAreaId.setStatus(_A)
class _OspfNewCfgAreaSpfInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfNewCfgAreaSpfInterval_Type.__name__=_C
_OspfNewCfgAreaSpfInterval_Object=MibTableColumn
ospfNewCfgAreaSpfInterval=_OspfNewCfgAreaSpfInterval_Object((1,3,6,1,4,1,1872,2,1,3,21,3,1,3),_OspfNewCfgAreaSpfInterval_Type())
ospfNewCfgAreaSpfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgAreaSpfInterval.setStatus(_A)
class _OspfNewCfgAreaAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_c,2)))
_OspfNewCfgAreaAuthType_Type.__name__=_C
_OspfNewCfgAreaAuthType_Object=MibTableColumn
ospfNewCfgAreaAuthType=_OspfNewCfgAreaAuthType_Object((1,3,6,1,4,1,1872,2,1,3,21,3,1,4),_OspfNewCfgAreaAuthType_Type())
ospfNewCfgAreaAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfNewCfgAreaAuthType.setStatus(_A)
_RipStats_ObjectIdentity=ObjectIdentity
ripStats=_RipStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,1))
_RipStatInPkts_Type=Counter32
_RipStatInPkts_Object=MibScalar
ripStatInPkts=_RipStatInPkts_Object((1,3,6,1,4,1,1872,2,1,8,1,1),_RipStatInPkts_Type())
ripStatInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInPkts.setStatus(_A)
_RipStatOutPkts_Type=Counter32
_RipStatOutPkts_Object=MibScalar
ripStatOutPkts=_RipStatOutPkts_Object((1,3,6,1,4,1,1872,2,1,8,1,2),_RipStatOutPkts_Type())
ripStatOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatOutPkts.setStatus(_A)
_RipStatInErrorPkts_Type=Counter32
_RipStatInErrorPkts_Object=MibScalar
ripStatInErrorPkts=_RipStatInErrorPkts_Object((1,3,6,1,4,1,1872,2,1,8,1,3),_RipStatInErrorPkts_Type())
ripStatInErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatInErrorPkts.setStatus(_A)
_RipStatRoutesAgedOut_Type=Counter32
_RipStatRoutesAgedOut_Object=MibScalar
ripStatRoutesAgedOut=_RipStatRoutesAgedOut_Object((1,3,6,1,4,1,1872,2,1,8,1,4),_RipStatRoutesAgedOut_Type())
ripStatRoutesAgedOut.setMaxAccess(_B)
if mibBuilder.loadTexts:ripStatRoutesAgedOut.setStatus(_A)
_ArpStats_ObjectIdentity=ObjectIdentity
arpStats=_ArpStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,3))
_ArpStatEntries_Type=Gauge32
_ArpStatEntries_Object=MibScalar
arpStatEntries=_ArpStatEntries_Object((1,3,6,1,4,1,1872,2,1,8,3,1),_ArpStatEntries_Type())
arpStatEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:arpStatEntries.setStatus(_A)
_ArpStatHighWater_Type=Gauge32
_ArpStatHighWater_Object=MibScalar
arpStatHighWater=_ArpStatHighWater_Object((1,3,6,1,4,1,1872,2,1,8,3,2),_ArpStatHighWater_Type())
arpStatHighWater.setMaxAccess(_B)
if mibBuilder.loadTexts:arpStatHighWater.setStatus(_A)
_ArpStatMaxEntries_Type=Gauge32
_ArpStatMaxEntries_Object=MibScalar
arpStatMaxEntries=_ArpStatMaxEntries_Object((1,3,6,1,4,1,1872,2,1,8,3,3),_ArpStatMaxEntries_Type())
arpStatMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:arpStatMaxEntries.setStatus(_A)
_RouteStats_ObjectIdentity=ObjectIdentity
routeStats=_RouteStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,4))
_RouteStatEntries_Type=Gauge32
_RouteStatEntries_Object=MibScalar
routeStatEntries=_RouteStatEntries_Object((1,3,6,1,4,1,1872,2,1,8,4,1),_RouteStatEntries_Type())
routeStatEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:routeStatEntries.setStatus(_A)
_RouteStatHighWater_Type=Gauge32
_RouteStatHighWater_Object=MibScalar
routeStatHighWater=_RouteStatHighWater_Object((1,3,6,1,4,1,1872,2,1,8,4,2),_RouteStatHighWater_Type())
routeStatHighWater.setMaxAccess(_B)
if mibBuilder.loadTexts:routeStatHighWater.setStatus(_A)
_RouteStatMaxEntries_Type=Gauge32
_RouteStatMaxEntries_Object=MibScalar
routeStatMaxEntries=_RouteStatMaxEntries_Object((1,3,6,1,4,1,1872,2,1,8,4,3),_RouteStatMaxEntries_Type())
routeStatMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:routeStatMaxEntries.setStatus(_A)
_DnsStats_ObjectIdentity=ObjectIdentity
dnsStats=_DnsStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,5))
_DnsStatInGoodDnsRequests_Type=Counter32
_DnsStatInGoodDnsRequests_Object=MibScalar
dnsStatInGoodDnsRequests=_DnsStatInGoodDnsRequests_Object((1,3,6,1,4,1,1872,2,1,8,5,1),_DnsStatInGoodDnsRequests_Type())
dnsStatInGoodDnsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsStatInGoodDnsRequests.setStatus(_A)
_DnsStatInBadDnsRequests_Type=Counter32
_DnsStatInBadDnsRequests_Object=MibScalar
dnsStatInBadDnsRequests=_DnsStatInBadDnsRequests_Object((1,3,6,1,4,1,1872,2,1,8,5,2),_DnsStatInBadDnsRequests_Type())
dnsStatInBadDnsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsStatInBadDnsRequests.setStatus(_A)
_VrrpStats_ObjectIdentity=ObjectIdentity
vrrpStats=_VrrpStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,9))
_VrrpStatInAdvers_Type=Counter32
_VrrpStatInAdvers_Object=MibScalar
vrrpStatInAdvers=_VrrpStatInAdvers_Object((1,3,6,1,4,1,1872,2,1,8,9,1),_VrrpStatInAdvers_Type())
vrrpStatInAdvers.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpStatInAdvers.setStatus(_A)
_VrrpStatOutAdvers_Type=Counter32
_VrrpStatOutAdvers_Object=MibScalar
vrrpStatOutAdvers=_VrrpStatOutAdvers_Object((1,3,6,1,4,1,1872,2,1,8,9,2),_VrrpStatOutAdvers_Type())
vrrpStatOutAdvers.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpStatOutAdvers.setStatus(_A)
_VrrpStatOutBadAdvers_Type=Counter32
_VrrpStatOutBadAdvers_Object=MibScalar
vrrpStatOutBadAdvers=_VrrpStatOutBadAdvers_Object((1,3,6,1,4,1,1872,2,1,8,9,3),_VrrpStatOutBadAdvers_Type())
vrrpStatOutBadAdvers.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpStatOutBadAdvers.setStatus(_A)
_OspfStats_ObjectIdentity=ObjectIdentity
ospfStats=_OspfStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,22))
_OspfGeneralStats_ObjectIdentity=ObjectIdentity
ospfGeneralStats=_OspfGeneralStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,22,1))
_OspfCumRxTxStats_ObjectIdentity=ObjectIdentity
ospfCumRxTxStats=_OspfCumRxTxStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,22,1,1))
_OspfCumRxPkts_Type=Counter32
_OspfCumRxPkts_Object=MibScalar
ospfCumRxPkts=_OspfCumRxPkts_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,1),_OspfCumRxPkts_Type())
ospfCumRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxPkts.setStatus(_A)
_OspfCumTxPkts_Type=Counter32
_OspfCumTxPkts_Object=MibScalar
ospfCumTxPkts=_OspfCumTxPkts_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,2),_OspfCumTxPkts_Type())
ospfCumTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxPkts.setStatus(_A)
_OspfCumRxHello_Type=Counter32
_OspfCumRxHello_Object=MibScalar
ospfCumRxHello=_OspfCumRxHello_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,3),_OspfCumRxHello_Type())
ospfCumRxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxHello.setStatus(_A)
_OspfCumTxHello_Type=Counter32
_OspfCumTxHello_Object=MibScalar
ospfCumTxHello=_OspfCumTxHello_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,4),_OspfCumTxHello_Type())
ospfCumTxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxHello.setStatus(_A)
_OspfCumRxDatabase_Type=Counter32
_OspfCumRxDatabase_Object=MibScalar
ospfCumRxDatabase=_OspfCumRxDatabase_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,5),_OspfCumRxDatabase_Type())
ospfCumRxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxDatabase.setStatus(_A)
_OspfCumTxDatabase_Type=Counter32
_OspfCumTxDatabase_Object=MibScalar
ospfCumTxDatabase=_OspfCumTxDatabase_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,6),_OspfCumTxDatabase_Type())
ospfCumTxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxDatabase.setStatus(_A)
_OspfCumRxlsReqs_Type=Counter32
_OspfCumRxlsReqs_Object=MibScalar
ospfCumRxlsReqs=_OspfCumRxlsReqs_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,7),_OspfCumRxlsReqs_Type())
ospfCumRxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxlsReqs.setStatus(_A)
_OspfCumTxlsReqs_Type=Counter32
_OspfCumTxlsReqs_Object=MibScalar
ospfCumTxlsReqs=_OspfCumTxlsReqs_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,8),_OspfCumTxlsReqs_Type())
ospfCumTxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxlsReqs.setStatus(_A)
_OspfCumRxlsAcks_Type=Counter32
_OspfCumRxlsAcks_Object=MibScalar
ospfCumRxlsAcks=_OspfCumRxlsAcks_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,9),_OspfCumRxlsAcks_Type())
ospfCumRxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxlsAcks.setStatus(_A)
_OspfCumTxlsAcks_Type=Counter32
_OspfCumTxlsAcks_Object=MibScalar
ospfCumTxlsAcks=_OspfCumTxlsAcks_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,10),_OspfCumTxlsAcks_Type())
ospfCumTxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxlsAcks.setStatus(_A)
_OspfCumRxlsUpdates_Type=Counter32
_OspfCumRxlsUpdates_Object=MibScalar
ospfCumRxlsUpdates=_OspfCumRxlsUpdates_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,11),_OspfCumRxlsUpdates_Type())
ospfCumRxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumRxlsUpdates.setStatus(_A)
_OspfCumTxlsUpdates_Type=Counter32
_OspfCumTxlsUpdates_Object=MibScalar
ospfCumTxlsUpdates=_OspfCumTxlsUpdates_Object((1,3,6,1,4,1,1872,2,1,8,22,1,1,12),_OspfCumTxlsUpdates_Type())
ospfCumTxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumTxlsUpdates.setStatus(_A)
_OspfCumNbrChangeStats_ObjectIdentity=ObjectIdentity
ospfCumNbrChangeStats=_OspfCumNbrChangeStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,22,1,2))
_OspfCumNbrhello_Type=Counter32
_OspfCumNbrhello_Object=MibScalar
ospfCumNbrhello=_OspfCumNbrhello_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,1),_OspfCumNbrhello_Type())
ospfCumNbrhello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrhello.setStatus(_A)
_OspfCumNbrStart_Type=Counter32
_OspfCumNbrStart_Object=MibScalar
ospfCumNbrStart=_OspfCumNbrStart_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,2),_OspfCumNbrStart_Type())
ospfCumNbrStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrStart.setStatus(_A)
_OspfCumNbrAdjointOk_Type=Counter32
_OspfCumNbrAdjointOk_Object=MibScalar
ospfCumNbrAdjointOk=_OspfCumNbrAdjointOk_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,3),_OspfCumNbrAdjointOk_Type())
ospfCumNbrAdjointOk.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrAdjointOk.setStatus(_A)
_OspfCumNbrNegotiationDone_Type=Counter32
_OspfCumNbrNegotiationDone_Object=MibScalar
ospfCumNbrNegotiationDone=_OspfCumNbrNegotiationDone_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,4),_OspfCumNbrNegotiationDone_Type())
ospfCumNbrNegotiationDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrNegotiationDone.setStatus(_A)
_OspfCumNbrExchangeDone_Type=Counter32
_OspfCumNbrExchangeDone_Object=MibScalar
ospfCumNbrExchangeDone=_OspfCumNbrExchangeDone_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,5),_OspfCumNbrExchangeDone_Type())
ospfCumNbrExchangeDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrExchangeDone.setStatus(_A)
_OspfCumNbrBadRequests_Type=Counter32
_OspfCumNbrBadRequests_Object=MibScalar
ospfCumNbrBadRequests=_OspfCumNbrBadRequests_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,6),_OspfCumNbrBadRequests_Type())
ospfCumNbrBadRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrBadRequests.setStatus(_A)
_OspfCumNbrBadSequence_Type=Counter32
_OspfCumNbrBadSequence_Object=MibScalar
ospfCumNbrBadSequence=_OspfCumNbrBadSequence_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,7),_OspfCumNbrBadSequence_Type())
ospfCumNbrBadSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrBadSequence.setStatus(_A)
_OspfCumNbrLoadingDone_Type=Counter32
_OspfCumNbrLoadingDone_Object=MibScalar
ospfCumNbrLoadingDone=_OspfCumNbrLoadingDone_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,8),_OspfCumNbrLoadingDone_Type())
ospfCumNbrLoadingDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrLoadingDone.setStatus(_A)
_OspfCumNbrN1way_Type=Counter32
_OspfCumNbrN1way_Object=MibScalar
ospfCumNbrN1way=_OspfCumNbrN1way_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,9),_OspfCumNbrN1way_Type())
ospfCumNbrN1way.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrN1way.setStatus(_A)
_OspfCumNbrRstAd_Type=Counter32
_OspfCumNbrRstAd_Object=MibScalar
ospfCumNbrRstAd=_OspfCumNbrRstAd_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,10),_OspfCumNbrRstAd_Type())
ospfCumNbrRstAd.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrRstAd.setStatus(_A)
_OspfCumNbrDown_Type=Counter32
_OspfCumNbrDown_Object=MibScalar
ospfCumNbrDown=_OspfCumNbrDown_Object((1,3,6,1,4,1,1872,2,1,8,22,1,2,11),_OspfCumNbrDown_Type())
ospfCumNbrDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumNbrDown.setStatus(_A)
_OspfCumIntfChangeStats_ObjectIdentity=ObjectIdentity
ospfCumIntfChangeStats=_OspfCumIntfChangeStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,22,1,3))
_OspfCumIntfHello_Type=Counter32
_OspfCumIntfHello_Object=MibScalar
ospfCumIntfHello=_OspfCumIntfHello_Object((1,3,6,1,4,1,1872,2,1,8,22,1,3,1),_OspfCumIntfHello_Type())
ospfCumIntfHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfHello.setStatus(_A)
_OspfCumIntfDown_Type=Counter32
_OspfCumIntfDown_Object=MibScalar
ospfCumIntfDown=_OspfCumIntfDown_Object((1,3,6,1,4,1,1872,2,1,8,22,1,3,2),_OspfCumIntfDown_Type())
ospfCumIntfDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfDown.setStatus(_A)
_OspfCumIntfLoop_Type=Counter32
_OspfCumIntfLoop_Object=MibScalar
ospfCumIntfLoop=_OspfCumIntfLoop_Object((1,3,6,1,4,1,1872,2,1,8,22,1,3,3),_OspfCumIntfLoop_Type())
ospfCumIntfLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfLoop.setStatus(_A)
_OspfCumIntfUnloop_Type=Counter32
_OspfCumIntfUnloop_Object=MibScalar
ospfCumIntfUnloop=_OspfCumIntfUnloop_Object((1,3,6,1,4,1,1872,2,1,8,22,1,3,4),_OspfCumIntfUnloop_Type())
ospfCumIntfUnloop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfUnloop.setStatus(_A)
_OspfCumIntfWaitTimer_Type=Counter32
_OspfCumIntfWaitTimer_Object=MibScalar
ospfCumIntfWaitTimer=_OspfCumIntfWaitTimer_Object((1,3,6,1,4,1,1872,2,1,8,22,1,3,5),_OspfCumIntfWaitTimer_Type())
ospfCumIntfWaitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfWaitTimer.setStatus(_A)
_OspfCumIntfBackup_Type=Counter32
_OspfCumIntfBackup_Object=MibScalar
ospfCumIntfBackup=_OspfCumIntfBackup_Object((1,3,6,1,4,1,1872,2,1,8,22,1,3,6),_OspfCumIntfBackup_Type())
ospfCumIntfBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfBackup.setStatus(_A)
_OspfCumIntfNbrChange_Type=Counter32
_OspfCumIntfNbrChange_Object=MibScalar
ospfCumIntfNbrChange=_OspfCumIntfNbrChange_Object((1,3,6,1,4,1,1872,2,1,8,22,1,3,7),_OspfCumIntfNbrChange_Type())
ospfCumIntfNbrChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfCumIntfNbrChange.setStatus(_A)
_OspfTimersKickOffStats_ObjectIdentity=ObjectIdentity
ospfTimersKickOffStats=_OspfTimersKickOffStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,22,1,4))
_OspfTmrsKckOffHello_Type=Counter32
_OspfTmrsKckOffHello_Object=MibScalar
ospfTmrsKckOffHello=_OspfTmrsKckOffHello_Object((1,3,6,1,4,1,1872,2,1,8,22,1,4,1),_OspfTmrsKckOffHello_Type())
ospfTmrsKckOffHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffHello.setStatus(_A)
_OspfTmrsKckOffRetransmit_Type=Counter32
_OspfTmrsKckOffRetransmit_Object=MibScalar
ospfTmrsKckOffRetransmit=_OspfTmrsKckOffRetransmit_Object((1,3,6,1,4,1,1872,2,1,8,22,1,4,2),_OspfTmrsKckOffRetransmit_Type())
ospfTmrsKckOffRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffRetransmit.setStatus(_A)
_OspfTmrsKckOffLsaLock_Type=Counter32
_OspfTmrsKckOffLsaLock_Object=MibScalar
ospfTmrsKckOffLsaLock=_OspfTmrsKckOffLsaLock_Object((1,3,6,1,4,1,1872,2,1,8,22,1,4,3),_OspfTmrsKckOffLsaLock_Type())
ospfTmrsKckOffLsaLock.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffLsaLock.setStatus(_A)
_OspfTmrsKckOffLsaAck_Type=Counter32
_OspfTmrsKckOffLsaAck_Object=MibScalar
ospfTmrsKckOffLsaAck=_OspfTmrsKckOffLsaAck_Object((1,3,6,1,4,1,1872,2,1,8,22,1,4,4),_OspfTmrsKckOffLsaAck_Type())
ospfTmrsKckOffLsaAck.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffLsaAck.setStatus(_A)
_OspfTmrsKckOffDbage_Type=Counter32
_OspfTmrsKckOffDbage_Object=MibScalar
ospfTmrsKckOffDbage=_OspfTmrsKckOffDbage_Object((1,3,6,1,4,1,1872,2,1,8,22,1,4,5),_OspfTmrsKckOffDbage_Type())
ospfTmrsKckOffDbage.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffDbage.setStatus(_A)
_OspfTmrsKckOffSummary_Type=Counter32
_OspfTmrsKckOffSummary_Object=MibScalar
ospfTmrsKckOffSummary=_OspfTmrsKckOffSummary_Object((1,3,6,1,4,1,1872,2,1,8,22,1,4,6),_OspfTmrsKckOffSummary_Type())
ospfTmrsKckOffSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffSummary.setStatus(_A)
_OspfTmrsKckOffAseExport_Type=Counter32
_OspfTmrsKckOffAseExport_Object=MibScalar
ospfTmrsKckOffAseExport=_OspfTmrsKckOffAseExport_Object((1,3,6,1,4,1,1872,2,1,8,22,1,4,7),_OspfTmrsKckOffAseExport_Type())
ospfTmrsKckOffAseExport.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTmrsKckOffAseExport.setStatus(_A)
_OspfArea_ObjectIdentity=ObjectIdentity
ospfArea=_OspfArea_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,22,2))
_OspfAreaRxTxStats_Object=MibTable
ospfAreaRxTxStats=_OspfAreaRxTxStats_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1))
if mibBuilder.loadTexts:ospfAreaRxTxStats.setStatus(_A)
_OspfAreaRxTxStatsEntry_Object=MibTableRow
ospfAreaRxTxStatsEntry=_OspfAreaRxTxStatsEntry_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1))
ospfAreaRxTxStatsEntry.setIndexNames((0,_G,_f))
if mibBuilder.loadTexts:ospfAreaRxTxStatsEntry.setStatus(_A)
_OspfAreaRxTxIndex_Type=Integer32
_OspfAreaRxTxIndex_Object=MibTableColumn
ospfAreaRxTxIndex=_OspfAreaRxTxIndex_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,1),_OspfAreaRxTxIndex_Type())
ospfAreaRxTxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxTxIndex.setStatus(_A)
_OspfAreaRxPkts_Type=Counter32
_OspfAreaRxPkts_Object=MibTableColumn
ospfAreaRxPkts=_OspfAreaRxPkts_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,2),_OspfAreaRxPkts_Type())
ospfAreaRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxPkts.setStatus(_A)
_OspfAreaTxPkts_Type=Counter32
_OspfAreaTxPkts_Object=MibTableColumn
ospfAreaTxPkts=_OspfAreaTxPkts_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,3),_OspfAreaTxPkts_Type())
ospfAreaTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxPkts.setStatus(_A)
_OspfAreaRxHello_Type=Counter32
_OspfAreaRxHello_Object=MibTableColumn
ospfAreaRxHello=_OspfAreaRxHello_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,4),_OspfAreaRxHello_Type())
ospfAreaRxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxHello.setStatus(_A)
_OspfAreaTxHello_Type=Counter32
_OspfAreaTxHello_Object=MibTableColumn
ospfAreaTxHello=_OspfAreaTxHello_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,5),_OspfAreaTxHello_Type())
ospfAreaTxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxHello.setStatus(_A)
_OspfAreaRxDatabase_Type=Counter32
_OspfAreaRxDatabase_Object=MibTableColumn
ospfAreaRxDatabase=_OspfAreaRxDatabase_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,6),_OspfAreaRxDatabase_Type())
ospfAreaRxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxDatabase.setStatus(_A)
_OspfAreaTxDatabase_Type=Counter32
_OspfAreaTxDatabase_Object=MibTableColumn
ospfAreaTxDatabase=_OspfAreaTxDatabase_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,7),_OspfAreaTxDatabase_Type())
ospfAreaTxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxDatabase.setStatus(_A)
_OspfAreaRxlsReqs_Type=Counter32
_OspfAreaRxlsReqs_Object=MibTableColumn
ospfAreaRxlsReqs=_OspfAreaRxlsReqs_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,8),_OspfAreaRxlsReqs_Type())
ospfAreaRxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxlsReqs.setStatus(_A)
_OspfAreaTxlsReqs_Type=Counter32
_OspfAreaTxlsReqs_Object=MibTableColumn
ospfAreaTxlsReqs=_OspfAreaTxlsReqs_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,9),_OspfAreaTxlsReqs_Type())
ospfAreaTxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxlsReqs.setStatus(_A)
_OspfAreaRxlsAcks_Type=Counter32
_OspfAreaRxlsAcks_Object=MibTableColumn
ospfAreaRxlsAcks=_OspfAreaRxlsAcks_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,10),_OspfAreaRxlsAcks_Type())
ospfAreaRxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxlsAcks.setStatus(_A)
_OspfAreaTxlsAcks_Type=Counter32
_OspfAreaTxlsAcks_Object=MibTableColumn
ospfAreaTxlsAcks=_OspfAreaTxlsAcks_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,11),_OspfAreaTxlsAcks_Type())
ospfAreaTxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxlsAcks.setStatus(_A)
_OspfAreaRxlsUpdates_Type=Counter32
_OspfAreaRxlsUpdates_Object=MibTableColumn
ospfAreaRxlsUpdates=_OspfAreaRxlsUpdates_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,12),_OspfAreaRxlsUpdates_Type())
ospfAreaRxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRxlsUpdates.setStatus(_A)
_OspfAreaTxlsUpdates_Type=Counter32
_OspfAreaTxlsUpdates_Object=MibTableColumn
ospfAreaTxlsUpdates=_OspfAreaTxlsUpdates_Object((1,3,6,1,4,1,1872,2,1,8,22,2,1,1,13),_OspfAreaTxlsUpdates_Type())
ospfAreaTxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaTxlsUpdates.setStatus(_A)
_OspfAreaNbrChangeStats_Object=MibTable
ospfAreaNbrChangeStats=_OspfAreaNbrChangeStats_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2))
if mibBuilder.loadTexts:ospfAreaNbrChangeStats.setStatus(_A)
_OspfAreaNbrChangeStatsEntry_Object=MibTableRow
ospfAreaNbrChangeStatsEntry=_OspfAreaNbrChangeStatsEntry_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1))
ospfAreaNbrChangeStatsEntry.setIndexNames((0,_G,_g))
if mibBuilder.loadTexts:ospfAreaNbrChangeStatsEntry.setStatus(_A)
_OspfAreaNbrIndex_Type=Integer32
_OspfAreaNbrIndex_Object=MibTableColumn
ospfAreaNbrIndex=_OspfAreaNbrIndex_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,1),_OspfAreaNbrIndex_Type())
ospfAreaNbrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrIndex.setStatus(_A)
_OspfAreaNbrhello_Type=Counter32
_OspfAreaNbrhello_Object=MibTableColumn
ospfAreaNbrhello=_OspfAreaNbrhello_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,2),_OspfAreaNbrhello_Type())
ospfAreaNbrhello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrhello.setStatus(_A)
_OspfAreaNbrStart_Type=Counter32
_OspfAreaNbrStart_Object=MibTableColumn
ospfAreaNbrStart=_OspfAreaNbrStart_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,3),_OspfAreaNbrStart_Type())
ospfAreaNbrStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrStart.setStatus(_A)
_OspfAreaNbrAdjointOk_Type=Counter32
_OspfAreaNbrAdjointOk_Object=MibTableColumn
ospfAreaNbrAdjointOk=_OspfAreaNbrAdjointOk_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,4),_OspfAreaNbrAdjointOk_Type())
ospfAreaNbrAdjointOk.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrAdjointOk.setStatus(_A)
_OspfAreaNbrNegotiationDone_Type=Counter32
_OspfAreaNbrNegotiationDone_Object=MibTableColumn
ospfAreaNbrNegotiationDone=_OspfAreaNbrNegotiationDone_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,5),_OspfAreaNbrNegotiationDone_Type())
ospfAreaNbrNegotiationDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrNegotiationDone.setStatus(_A)
_OspfAreaNbrExchangeDone_Type=Counter32
_OspfAreaNbrExchangeDone_Object=MibTableColumn
ospfAreaNbrExchangeDone=_OspfAreaNbrExchangeDone_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,6),_OspfAreaNbrExchangeDone_Type())
ospfAreaNbrExchangeDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrExchangeDone.setStatus(_A)
_OspfAreaNbrBadRequests_Type=Counter32
_OspfAreaNbrBadRequests_Object=MibTableColumn
ospfAreaNbrBadRequests=_OspfAreaNbrBadRequests_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,7),_OspfAreaNbrBadRequests_Type())
ospfAreaNbrBadRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrBadRequests.setStatus(_A)
_OspfAreaNbrBadSequence_Type=Counter32
_OspfAreaNbrBadSequence_Object=MibTableColumn
ospfAreaNbrBadSequence=_OspfAreaNbrBadSequence_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,8),_OspfAreaNbrBadSequence_Type())
ospfAreaNbrBadSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrBadSequence.setStatus(_A)
_OspfAreaNbrLoadingDone_Type=Counter32
_OspfAreaNbrLoadingDone_Object=MibTableColumn
ospfAreaNbrLoadingDone=_OspfAreaNbrLoadingDone_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,9),_OspfAreaNbrLoadingDone_Type())
ospfAreaNbrLoadingDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrLoadingDone.setStatus(_A)
_OspfAreaNbrN1way_Type=Counter32
_OspfAreaNbrN1way_Object=MibTableColumn
ospfAreaNbrN1way=_OspfAreaNbrN1way_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,10),_OspfAreaNbrN1way_Type())
ospfAreaNbrN1way.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrN1way.setStatus(_A)
_OspfAreaNbrRstAd_Type=Counter32
_OspfAreaNbrRstAd_Object=MibTableColumn
ospfAreaNbrRstAd=_OspfAreaNbrRstAd_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,11),_OspfAreaNbrRstAd_Type())
ospfAreaNbrRstAd.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrRstAd.setStatus(_A)
_OspfAreaNbrDown_Type=Counter32
_OspfAreaNbrDown_Object=MibTableColumn
ospfAreaNbrDown=_OspfAreaNbrDown_Object((1,3,6,1,4,1,1872,2,1,8,22,2,2,1,12),_OspfAreaNbrDown_Type())
ospfAreaNbrDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaNbrDown.setStatus(_A)
_OspfAreaChangeStats_Object=MibTable
ospfAreaChangeStats=_OspfAreaChangeStats_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3))
if mibBuilder.loadTexts:ospfAreaChangeStats.setStatus(_A)
_OspfAreaChangeStatsEntry_Object=MibTableRow
ospfAreaChangeStatsEntry=_OspfAreaChangeStatsEntry_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3,1))
ospfAreaChangeStatsEntry.setIndexNames((0,_G,_h))
if mibBuilder.loadTexts:ospfAreaChangeStatsEntry.setStatus(_A)
_OspfAreaIntfIndex_Type=Integer32
_OspfAreaIntfIndex_Object=MibTableColumn
ospfAreaIntfIndex=_OspfAreaIntfIndex_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3,1,1),_OspfAreaIntfIndex_Type())
ospfAreaIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfIndex.setStatus(_A)
_OspfAreaIntfHello_Type=Counter32
_OspfAreaIntfHello_Object=MibTableColumn
ospfAreaIntfHello=_OspfAreaIntfHello_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3,1,2),_OspfAreaIntfHello_Type())
ospfAreaIntfHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfHello.setStatus(_A)
_OspfAreaIntfDown_Type=Counter32
_OspfAreaIntfDown_Object=MibTableColumn
ospfAreaIntfDown=_OspfAreaIntfDown_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3,1,3),_OspfAreaIntfDown_Type())
ospfAreaIntfDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfDown.setStatus(_A)
_OspfAreaIntfLoop_Type=Counter32
_OspfAreaIntfLoop_Object=MibTableColumn
ospfAreaIntfLoop=_OspfAreaIntfLoop_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3,1,4),_OspfAreaIntfLoop_Type())
ospfAreaIntfLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfLoop.setStatus(_A)
_OspfAreaIntfUnloop_Type=Counter32
_OspfAreaIntfUnloop_Object=MibTableColumn
ospfAreaIntfUnloop=_OspfAreaIntfUnloop_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3,1,5),_OspfAreaIntfUnloop_Type())
ospfAreaIntfUnloop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfUnloop.setStatus(_A)
_OspfAreaIntfWaitTimer_Type=Counter32
_OspfAreaIntfWaitTimer_Object=MibTableColumn
ospfAreaIntfWaitTimer=_OspfAreaIntfWaitTimer_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3,1,6),_OspfAreaIntfWaitTimer_Type())
ospfAreaIntfWaitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfWaitTimer.setStatus(_A)
_OspfAreaIntfBackup_Type=Counter32
_OspfAreaIntfBackup_Object=MibTableColumn
ospfAreaIntfBackup=_OspfAreaIntfBackup_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3,1,7),_OspfAreaIntfBackup_Type())
ospfAreaIntfBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfBackup.setStatus(_A)
_OspfAreaIntfNbrChange_Type=Counter32
_OspfAreaIntfNbrChange_Object=MibTableColumn
ospfAreaIntfNbrChange=_OspfAreaIntfNbrChange_Object((1,3,6,1,4,1,1872,2,1,8,22,2,3,1,8),_OspfAreaIntfNbrChange_Type())
ospfAreaIntfNbrChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaIntfNbrChange.setStatus(_A)
_OspfInterface_ObjectIdentity=ObjectIdentity
ospfInterface=_OspfInterface_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,22,3))
_OspfIntfRxTxStats_Object=MibTable
ospfIntfRxTxStats=_OspfIntfRxTxStats_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1))
if mibBuilder.loadTexts:ospfIntfRxTxStats.setStatus(_A)
_OspfIntfRxTxStatsEntry_Object=MibTableRow
ospfIntfRxTxStatsEntry=_OspfIntfRxTxStatsEntry_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1))
ospfIntfRxTxStatsEntry.setIndexNames((0,_G,_i))
if mibBuilder.loadTexts:ospfIntfRxTxStatsEntry.setStatus(_A)
_OspfIntfRxTxIndex_Type=Integer32
_OspfIntfRxTxIndex_Object=MibTableColumn
ospfIntfRxTxIndex=_OspfIntfRxTxIndex_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,1),_OspfIntfRxTxIndex_Type())
ospfIntfRxTxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxTxIndex.setStatus(_A)
_OspfIntfRxPkts_Type=Counter32
_OspfIntfRxPkts_Object=MibTableColumn
ospfIntfRxPkts=_OspfIntfRxPkts_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,2),_OspfIntfRxPkts_Type())
ospfIntfRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxPkts.setStatus(_A)
_OspfIntfTxPkts_Type=Counter32
_OspfIntfTxPkts_Object=MibTableColumn
ospfIntfTxPkts=_OspfIntfTxPkts_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,3),_OspfIntfTxPkts_Type())
ospfIntfTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxPkts.setStatus(_A)
_OspfIntfRxHello_Type=Counter32
_OspfIntfRxHello_Object=MibTableColumn
ospfIntfRxHello=_OspfIntfRxHello_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,4),_OspfIntfRxHello_Type())
ospfIntfRxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxHello.setStatus(_A)
_OspfIntfTxHello_Type=Counter32
_OspfIntfTxHello_Object=MibTableColumn
ospfIntfTxHello=_OspfIntfTxHello_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,5),_OspfIntfTxHello_Type())
ospfIntfTxHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxHello.setStatus(_A)
_OspfIntfRxDatabase_Type=Counter32
_OspfIntfRxDatabase_Object=MibTableColumn
ospfIntfRxDatabase=_OspfIntfRxDatabase_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,6),_OspfIntfRxDatabase_Type())
ospfIntfRxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxDatabase.setStatus(_A)
_OspfIntfTxDatabase_Type=Counter32
_OspfIntfTxDatabase_Object=MibTableColumn
ospfIntfTxDatabase=_OspfIntfTxDatabase_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,7),_OspfIntfTxDatabase_Type())
ospfIntfTxDatabase.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxDatabase.setStatus(_A)
_OspfIntfRxlsReqs_Type=Counter32
_OspfIntfRxlsReqs_Object=MibTableColumn
ospfIntfRxlsReqs=_OspfIntfRxlsReqs_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,8),_OspfIntfRxlsReqs_Type())
ospfIntfRxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxlsReqs.setStatus(_A)
_OspfIntfTxlsReqs_Type=Counter32
_OspfIntfTxlsReqs_Object=MibTableColumn
ospfIntfTxlsReqs=_OspfIntfTxlsReqs_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,9),_OspfIntfTxlsReqs_Type())
ospfIntfTxlsReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxlsReqs.setStatus(_A)
_OspfIntfRxlsAcks_Type=Counter32
_OspfIntfRxlsAcks_Object=MibTableColumn
ospfIntfRxlsAcks=_OspfIntfRxlsAcks_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,10),_OspfIntfRxlsAcks_Type())
ospfIntfRxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxlsAcks.setStatus(_A)
_OspfIntfTxlsAcks_Type=Counter32
_OspfIntfTxlsAcks_Object=MibTableColumn
ospfIntfTxlsAcks=_OspfIntfTxlsAcks_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,11),_OspfIntfTxlsAcks_Type())
ospfIntfTxlsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxlsAcks.setStatus(_A)
_OspfIntfRxlsUpdates_Type=Counter32
_OspfIntfRxlsUpdates_Object=MibTableColumn
ospfIntfRxlsUpdates=_OspfIntfRxlsUpdates_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,12),_OspfIntfRxlsUpdates_Type())
ospfIntfRxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfRxlsUpdates.setStatus(_A)
_OspfIntfTxlsUpdates_Type=Counter32
_OspfIntfTxlsUpdates_Object=MibTableColumn
ospfIntfTxlsUpdates=_OspfIntfTxlsUpdates_Object((1,3,6,1,4,1,1872,2,1,8,22,3,1,1,13),_OspfIntfTxlsUpdates_Type())
ospfIntfTxlsUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfTxlsUpdates.setStatus(_A)
_OspfIntfNbrChangeStats_Object=MibTable
ospfIntfNbrChangeStats=_OspfIntfNbrChangeStats_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2))
if mibBuilder.loadTexts:ospfIntfNbrChangeStats.setStatus(_A)
_OspfIntfNbrChangeStatsEntry_Object=MibTableRow
ospfIntfNbrChangeStatsEntry=_OspfIntfNbrChangeStatsEntry_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1))
ospfIntfNbrChangeStatsEntry.setIndexNames((0,_G,_j))
if mibBuilder.loadTexts:ospfIntfNbrChangeStatsEntry.setStatus(_A)
_OspfIntfNbrIndex_Type=Integer32
_OspfIntfNbrIndex_Object=MibTableColumn
ospfIntfNbrIndex=_OspfIntfNbrIndex_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,1),_OspfIntfNbrIndex_Type())
ospfIntfNbrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrIndex.setStatus(_A)
_OspfIntfNbrhello_Type=Counter32
_OspfIntfNbrhello_Object=MibTableColumn
ospfIntfNbrhello=_OspfIntfNbrhello_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,2),_OspfIntfNbrhello_Type())
ospfIntfNbrhello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrhello.setStatus(_A)
_OspfIntfNbrStart_Type=Counter32
_OspfIntfNbrStart_Object=MibTableColumn
ospfIntfNbrStart=_OspfIntfNbrStart_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,3),_OspfIntfNbrStart_Type())
ospfIntfNbrStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrStart.setStatus(_A)
_OspfIntfNbrAdjointOk_Type=Counter32
_OspfIntfNbrAdjointOk_Object=MibTableColumn
ospfIntfNbrAdjointOk=_OspfIntfNbrAdjointOk_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,4),_OspfIntfNbrAdjointOk_Type())
ospfIntfNbrAdjointOk.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrAdjointOk.setStatus(_A)
_OspfIntfNbrNegotiationDone_Type=Counter32
_OspfIntfNbrNegotiationDone_Object=MibTableColumn
ospfIntfNbrNegotiationDone=_OspfIntfNbrNegotiationDone_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,5),_OspfIntfNbrNegotiationDone_Type())
ospfIntfNbrNegotiationDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrNegotiationDone.setStatus(_A)
_OspfIntfNbrExchangeDone_Type=Counter32
_OspfIntfNbrExchangeDone_Object=MibTableColumn
ospfIntfNbrExchangeDone=_OspfIntfNbrExchangeDone_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,6),_OspfIntfNbrExchangeDone_Type())
ospfIntfNbrExchangeDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrExchangeDone.setStatus(_A)
_OspfIntfNbrBadRequests_Type=Counter32
_OspfIntfNbrBadRequests_Object=MibTableColumn
ospfIntfNbrBadRequests=_OspfIntfNbrBadRequests_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,7),_OspfIntfNbrBadRequests_Type())
ospfIntfNbrBadRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrBadRequests.setStatus(_A)
_OspfIntfNbrBadSequence_Type=Counter32
_OspfIntfNbrBadSequence_Object=MibTableColumn
ospfIntfNbrBadSequence=_OspfIntfNbrBadSequence_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,8),_OspfIntfNbrBadSequence_Type())
ospfIntfNbrBadSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrBadSequence.setStatus(_A)
_OspfIntfNbrLoadingDone_Type=Counter32
_OspfIntfNbrLoadingDone_Object=MibTableColumn
ospfIntfNbrLoadingDone=_OspfIntfNbrLoadingDone_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,9),_OspfIntfNbrLoadingDone_Type())
ospfIntfNbrLoadingDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrLoadingDone.setStatus(_A)
_OspfIntfNbrN1way_Type=Counter32
_OspfIntfNbrN1way_Object=MibTableColumn
ospfIntfNbrN1way=_OspfIntfNbrN1way_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,10),_OspfIntfNbrN1way_Type())
ospfIntfNbrN1way.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrN1way.setStatus(_A)
_OspfIntfNbrRstAd_Type=Counter32
_OspfIntfNbrRstAd_Object=MibTableColumn
ospfIntfNbrRstAd=_OspfIntfNbrRstAd_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,11),_OspfIntfNbrRstAd_Type())
ospfIntfNbrRstAd.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrRstAd.setStatus(_A)
_OspfIntfNbrDown_Type=Counter32
_OspfIntfNbrDown_Object=MibTableColumn
ospfIntfNbrDown=_OspfIntfNbrDown_Object((1,3,6,1,4,1,1872,2,1,8,22,3,2,1,12),_OspfIntfNbrDown_Type())
ospfIntfNbrDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrDown.setStatus(_A)
_OspfIntfChangeStats_Object=MibTable
ospfIntfChangeStats=_OspfIntfChangeStats_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3))
if mibBuilder.loadTexts:ospfIntfChangeStats.setStatus(_A)
_OspfIntfChangeStatsEntry_Object=MibTableRow
ospfIntfChangeStatsEntry=_OspfIntfChangeStatsEntry_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3,1))
ospfIntfChangeStatsEntry.setIndexNames((0,_G,_k))
if mibBuilder.loadTexts:ospfIntfChangeStatsEntry.setStatus(_A)
_OspfIntfIndex_Type=Integer32
_OspfIntfIndex_Object=MibTableColumn
ospfIntfIndex=_OspfIntfIndex_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3,1,1),_OspfIntfIndex_Type())
ospfIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfIndex.setStatus(_A)
_OspfIntfHello_Type=Counter32
_OspfIntfHello_Object=MibTableColumn
ospfIntfHello=_OspfIntfHello_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3,1,2),_OspfIntfHello_Type())
ospfIntfHello.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfHello.setStatus(_A)
_OspfIntfDown_Type=Counter32
_OspfIntfDown_Object=MibTableColumn
ospfIntfDown=_OspfIntfDown_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3,1,3),_OspfIntfDown_Type())
ospfIntfDown.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfDown.setStatus(_A)
_OspfIntfLoop_Type=Counter32
_OspfIntfLoop_Object=MibTableColumn
ospfIntfLoop=_OspfIntfLoop_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3,1,4),_OspfIntfLoop_Type())
ospfIntfLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfLoop.setStatus(_A)
_OspfIntfUnloop_Type=Counter32
_OspfIntfUnloop_Object=MibTableColumn
ospfIntfUnloop=_OspfIntfUnloop_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3,1,5),_OspfIntfUnloop_Type())
ospfIntfUnloop.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfUnloop.setStatus(_A)
_OspfIntfWaitTimer_Type=Counter32
_OspfIntfWaitTimer_Object=MibTableColumn
ospfIntfWaitTimer=_OspfIntfWaitTimer_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3,1,6),_OspfIntfWaitTimer_Type())
ospfIntfWaitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfWaitTimer.setStatus(_A)
_OspfIntfBackup_Type=Counter32
_OspfIntfBackup_Object=MibTableColumn
ospfIntfBackup=_OspfIntfBackup_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3,1,7),_OspfIntfBackup_Type())
ospfIntfBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfBackup.setStatus(_A)
_OspfIntfNbrChange_Type=Counter32
_OspfIntfNbrChange_Object=MibTableColumn
ospfIntfNbrChange=_OspfIntfNbrChange_Object((1,3,6,1,4,1,1872,2,1,8,22,3,3,1,8),_OspfIntfNbrChange_Type())
ospfIntfNbrChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfNbrChange.setStatus(_A)
_Ip_info_ObjectIdentity=ObjectIdentity
ip_info=_Ip_info_ObjectIdentity((1,3,6,1,4,1,1872,2,1,9,3))
_IpRouteInfoTable_Object=MibTable
ipRouteInfoTable=_IpRouteInfoTable_Object((1,3,6,1,4,1,1872,2,1,9,3,1))
if mibBuilder.loadTexts:ipRouteInfoTable.setStatus(_A)
_IpRouteInfoEntry_Object=MibTableRow
ipRouteInfoEntry=_IpRouteInfoEntry_Object((1,3,6,1,4,1,1872,2,1,9,3,1,1))
ipRouteInfoEntry.setIndexNames((0,_G,_l))
if mibBuilder.loadTexts:ipRouteInfoEntry.setStatus(_A)
_IpRouteInfoIndx_Type=Integer32
_IpRouteInfoIndx_Object=MibTableColumn
ipRouteInfoIndx=_IpRouteInfoIndx_Object((1,3,6,1,4,1,1872,2,1,9,3,1,1,1),_IpRouteInfoIndx_Type())
ipRouteInfoIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoIndx.setStatus(_A)
_IpRouteInfoDestIp_Type=IpAddress
_IpRouteInfoDestIp_Object=MibTableColumn
ipRouteInfoDestIp=_IpRouteInfoDestIp_Object((1,3,6,1,4,1,1872,2,1,9,3,1,1,2),_IpRouteInfoDestIp_Type())
ipRouteInfoDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoDestIp.setStatus(_A)
_IpRouteInfoMask_Type=IpAddress
_IpRouteInfoMask_Object=MibTableColumn
ipRouteInfoMask=_IpRouteInfoMask_Object((1,3,6,1,4,1,1872,2,1,9,3,1,1,3),_IpRouteInfoMask_Type())
ipRouteInfoMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoMask.setStatus(_A)
_IpRouteInfoGateway_Type=IpAddress
_IpRouteInfoGateway_Object=MibTableColumn
ipRouteInfoGateway=_IpRouteInfoGateway_Object((1,3,6,1,4,1,1872,2,1,9,3,1,1,4),_IpRouteInfoGateway_Type())
ipRouteInfoGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoGateway.setStatus(_A)
class _IpRouteInfoTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('fixed',1),('icmp',2),('static',3),('snmp',4),('addr',5),('rip',6),(_m,7),(_n,8),(_o,9),('vip',10),('bgp',11),(_J,12),('ospf',13)))
_IpRouteInfoTag_Type.__name__=_C
_IpRouteInfoTag_Object=MibTableColumn
ipRouteInfoTag=_IpRouteInfoTag_Object((1,3,6,1,4,1,1872,2,1,9,3,1,1,5),_IpRouteInfoTag_Type())
ipRouteInfoTag.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoTag.setStatus(_A)
class _IpRouteInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_p,1),('direct',2),('local',3),(_m,4),(_n,5),(_o,6),(_H,7)))
_IpRouteInfoType_Type.__name__=_C
_IpRouteInfoType_Object=MibTableColumn
ipRouteInfoType=_IpRouteInfoType_Object((1,3,6,1,4,1,1872,2,1,9,3,1,1,6),_IpRouteInfoType_Type())
ipRouteInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoType.setStatus(_A)
_IpRouteInfoInterface_Type=Integer32
_IpRouteInfoInterface_Object=MibTableColumn
ipRouteInfoInterface=_IpRouteInfoInterface_Object((1,3,6,1,4,1,1872,2,1,9,3,1,1,7),_IpRouteInfoInterface_Type())
ipRouteInfoInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfoInterface.setStatus(_A)
_ArpInfoTable_Object=MibTable
arpInfoTable=_ArpInfoTable_Object((1,3,6,1,4,1,1872,2,1,9,3,2))
if mibBuilder.loadTexts:arpInfoTable.setStatus(_A)
_ArpInfoEntry_Object=MibTableRow
arpInfoEntry=_ArpInfoEntry_Object((1,3,6,1,4,1,1872,2,1,9,3,2,1))
arpInfoEntry.setIndexNames((0,_G,_q))
if mibBuilder.loadTexts:arpInfoEntry.setStatus(_A)
_ArpInfoDestIp_Type=IpAddress
_ArpInfoDestIp_Object=MibTableColumn
arpInfoDestIp=_ArpInfoDestIp_Object((1,3,6,1,4,1,1872,2,1,9,3,2,1,1),_ArpInfoDestIp_Type())
arpInfoDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoDestIp.setStatus(_A)
_ArpInfoMacAddr_Type=PhysAddress
_ArpInfoMacAddr_Object=MibTableColumn
arpInfoMacAddr=_ArpInfoMacAddr_Object((1,3,6,1,4,1,1872,2,1,9,3,2,1,2),_ArpInfoMacAddr_Type())
arpInfoMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoMacAddr.setStatus(_A)
_ArpInfoVLAN_Type=Integer32
_ArpInfoVLAN_Object=MibTableColumn
arpInfoVLAN=_ArpInfoVLAN_Object((1,3,6,1,4,1,1872,2,1,9,3,2,1,3),_ArpInfoVLAN_Type())
arpInfoVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoVLAN.setStatus(_A)
_ArpInfoSrcPort_Type=Integer32
_ArpInfoSrcPort_Object=MibTableColumn
arpInfoSrcPort=_ArpInfoSrcPort_Object((1,3,6,1,4,1,1872,2,1,9,3,2,1,4),_ArpInfoSrcPort_Type())
arpInfoSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoSrcPort.setStatus(_A)
_ArpInfoRefPorts_Type=Integer32
_ArpInfoRefPorts_Object=MibTableColumn
arpInfoRefPorts=_ArpInfoRefPorts_Object((1,3,6,1,4,1,1872,2,1,9,3,2,1,5),_ArpInfoRefPorts_Type())
arpInfoRefPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoRefPorts.setStatus(_A)
class _ArpInfoFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('clear',1),('unresolved',2),('permanent',3),(_p,4)))
_ArpInfoFlag_Type.__name__=_C
_ArpInfoFlag_Object=MibTableColumn
arpInfoFlag=_ArpInfoFlag_Object((1,3,6,1,4,1,1872,2,1,9,3,2,1,6),_ArpInfoFlag_Type())
arpInfoFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:arpInfoFlag.setStatus(_A)
_Vrrp_info_ObjectIdentity=ObjectIdentity
vrrp_info=_Vrrp_info_ObjectIdentity((1,3,6,1,4,1,1872,2,1,9,4))
_VrrpInfoVirtRtrTable_Object=MibTable
vrrpInfoVirtRtrTable=_VrrpInfoVirtRtrTable_Object((1,3,6,1,4,1,1872,2,1,9,4,1))
if mibBuilder.loadTexts:vrrpInfoVirtRtrTable.setStatus(_A)
_VrrpInfoVirtRtrTableEntry_Object=MibTableRow
vrrpInfoVirtRtrTableEntry=_VrrpInfoVirtRtrTableEntry_Object((1,3,6,1,4,1,1872,2,1,9,4,1,1))
vrrpInfoVirtRtrTableEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:vrrpInfoVirtRtrTableEntry.setStatus(_A)
_VrrpInfoVirtRtrIndex_Type=Integer32
_VrrpInfoVirtRtrIndex_Object=MibTableColumn
vrrpInfoVirtRtrIndex=_VrrpInfoVirtRtrIndex_Object((1,3,6,1,4,1,1872,2,1,9,4,1,1,1),_VrrpInfoVirtRtrIndex_Type())
vrrpInfoVirtRtrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrIndex.setStatus(_A)
class _VrrpInfoVirtRtrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('init',1),('master',2),(_N,3)))
_VrrpInfoVirtRtrState_Type.__name__=_C
_VrrpInfoVirtRtrState_Object=MibTableColumn
vrrpInfoVirtRtrState=_VrrpInfoVirtRtrState_Object((1,3,6,1,4,1,1872,2,1,9,4,1,1,2),_VrrpInfoVirtRtrState_Type())
vrrpInfoVirtRtrState.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrState.setStatus(_A)
class _VrrpInfoVirtRtrOwnership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('owner',1),('renter',2)))
_VrrpInfoVirtRtrOwnership_Type.__name__=_C
_VrrpInfoVirtRtrOwnership_Object=MibTableColumn
vrrpInfoVirtRtrOwnership=_VrrpInfoVirtRtrOwnership_Object((1,3,6,1,4,1,1872,2,1,9,4,1,1,3),_VrrpInfoVirtRtrOwnership_Type())
vrrpInfoVirtRtrOwnership.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrOwnership.setStatus(_A)
class _VrrpInfoVirtRtrServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_VrrpInfoVirtRtrServer_Type.__name__=_C
_VrrpInfoVirtRtrServer_Object=MibTableColumn
vrrpInfoVirtRtrServer=_VrrpInfoVirtRtrServer_Object((1,3,6,1,4,1,1872,2,1,9,4,1,1,4),_VrrpInfoVirtRtrServer_Type())
vrrpInfoVirtRtrServer.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrServer.setStatus(_A)
class _VrrpInfoVirtRtrProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_VrrpInfoVirtRtrProxy_Type.__name__=_C
_VrrpInfoVirtRtrProxy_Object=MibTableColumn
vrrpInfoVirtRtrProxy=_VrrpInfoVirtRtrProxy_Object((1,3,6,1,4,1,1872,2,1,9,4,1,1,5),_VrrpInfoVirtRtrProxy_Type())
vrrpInfoVirtRtrProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpInfoVirtRtrProxy.setStatus(_A)
_Ospfinfo_ObjectIdentity=ObjectIdentity
ospfinfo=_Ospfinfo_ObjectIdentity((1,3,6,1,4,1,1872,2,1,9,5))
_OspfGeneralInfo_ObjectIdentity=ObjectIdentity
ospfGeneralInfo=_OspfGeneralInfo_ObjectIdentity((1,3,6,1,4,1,1872,2,1,9,5,1))
_OspfStartTime_Type=Integer32
_OspfStartTime_Object=MibScalar
ospfStartTime=_OspfStartTime_Object((1,3,6,1,4,1,1872,2,1,9,5,1,1),_OspfStartTime_Type())
ospfStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfStartTime.setStatus(_A)
_OspfProcessUptime_Type=Counter32
_OspfProcessUptime_Object=MibScalar
ospfProcessUptime=_OspfProcessUptime_Object((1,3,6,1,4,1,1872,2,1,9,5,1,2),_OspfProcessUptime_Type())
ospfProcessUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfProcessUptime.setStatus(_A)
_OspfLsTypesSupported_Type=Integer32
_OspfLsTypesSupported_Object=MibScalar
ospfLsTypesSupported=_OspfLsTypesSupported_Object((1,3,6,1,4,1,1872,2,1,9,5,1,3),_OspfLsTypesSupported_Type())
ospfLsTypesSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfLsTypesSupported.setStatus(_A)
_OspfIntfCountForRouter_Type=Integer32
_OspfIntfCountForRouter_Object=MibScalar
ospfIntfCountForRouter=_OspfIntfCountForRouter_Object((1,3,6,1,4,1,1872,2,1,9,5,1,4),_OspfIntfCountForRouter_Type())
ospfIntfCountForRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIntfCountForRouter.setStatus(_A)
_OspfVlinkCountForRouter_Type=Integer32
_OspfVlinkCountForRouter_Object=MibScalar
ospfVlinkCountForRouter=_OspfVlinkCountForRouter_Object((1,3,6,1,4,1,1872,2,1,9,5,1,5),_OspfVlinkCountForRouter_Type())
ospfVlinkCountForRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVlinkCountForRouter.setStatus(_A)
_OspfTotalNeighbours_Type=Integer32
_OspfTotalNeighbours_Object=MibScalar
ospfTotalNeighbours=_OspfTotalNeighbours_Object((1,3,6,1,4,1,1872,2,1,9,5,1,6),_OspfTotalNeighbours_Type())
ospfTotalNeighbours.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalNeighbours.setStatus(_A)
_OspfNbrInInitState_Type=Integer32
_OspfNbrInInitState_Object=MibScalar
ospfNbrInInitState=_OspfNbrInInitState_Object((1,3,6,1,4,1,1872,2,1,9,5,1,7),_OspfNbrInInitState_Type())
ospfNbrInInitState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNbrInInitState.setStatus(_A)
_OspfNbrInExchState_Type=Integer32
_OspfNbrInExchState_Object=MibScalar
ospfNbrInExchState=_OspfNbrInExchState_Object((1,3,6,1,4,1,1872,2,1,9,5,1,8),_OspfNbrInExchState_Type())
ospfNbrInExchState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNbrInExchState.setStatus(_A)
_OspfNbrInFullState_Type=Integer32
_OspfNbrInFullState_Object=MibScalar
ospfNbrInFullState=_OspfNbrInFullState_Object((1,3,6,1,4,1,1872,2,1,9,5,1,9),_OspfNbrInFullState_Type())
ospfNbrInFullState.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNbrInFullState.setStatus(_A)
_OspfTotalAreas_Type=Integer32
_OspfTotalAreas_Object=MibScalar
ospfTotalAreas=_OspfTotalAreas_Object((1,3,6,1,4,1,1872,2,1,9,5,1,10),_OspfTotalAreas_Type())
ospfTotalAreas.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalAreas.setStatus(_A)
_OspfTotalTransitAreas_Type=Integer32
_OspfTotalTransitAreas_Object=MibScalar
ospfTotalTransitAreas=_OspfTotalTransitAreas_Object((1,3,6,1,4,1,1872,2,1,9,5,1,11),_OspfTotalTransitAreas_Type())
ospfTotalTransitAreas.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalTransitAreas.setStatus(_A)
_OspfTotalNssaAreas_Type=Integer32
_OspfTotalNssaAreas_Object=MibScalar
ospfTotalNssaAreas=_OspfTotalNssaAreas_Object((1,3,6,1,4,1,1872,2,1,9,5,1,12),_OspfTotalNssaAreas_Type())
ospfTotalNssaAreas.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalNssaAreas.setStatus(_A)
_OspfAreaInfoTable_Object=MibTable
ospfAreaInfoTable=_OspfAreaInfoTable_Object((1,3,6,1,4,1,1872,2,1,9,5,2))
if mibBuilder.loadTexts:ospfAreaInfoTable.setStatus(_A)
_OspfAreaInfoEntry_Object=MibTableRow
ospfAreaInfoEntry=_OspfAreaInfoEntry_Object((1,3,6,1,4,1,1872,2,1,9,5,2,1))
ospfAreaInfoEntry.setIndexNames((0,_G,_s))
if mibBuilder.loadTexts:ospfAreaInfoEntry.setStatus(_A)
_OspfAreaInfoIndex_Type=Integer32
_OspfAreaInfoIndex_Object=MibTableColumn
ospfAreaInfoIndex=_OspfAreaInfoIndex_Object((1,3,6,1,4,1,1872,2,1,9,5,2,1,1),_OspfAreaInfoIndex_Type())
ospfAreaInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaInfoIndex.setStatus(_A)
_OspfTotalNumberOfInterfaces_Type=Integer32
_OspfTotalNumberOfInterfaces_Object=MibTableColumn
ospfTotalNumberOfInterfaces=_OspfTotalNumberOfInterfaces_Object((1,3,6,1,4,1,1872,2,1,9,5,2,1,2),_OspfTotalNumberOfInterfaces_Type())
ospfTotalNumberOfInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTotalNumberOfInterfaces.setStatus(_A)
_OspfNumberOfInterfacesUp_Type=Integer32
_OspfNumberOfInterfacesUp_Object=MibTableColumn
ospfNumberOfInterfacesUp=_OspfNumberOfInterfacesUp_Object((1,3,6,1,4,1,1872,2,1,9,5,2,1,3),_OspfNumberOfInterfacesUp_Type())
ospfNumberOfInterfacesUp.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNumberOfInterfacesUp.setStatus(_A)
_OspfNumberOfLsdbEntries_Type=Integer32
_OspfNumberOfLsdbEntries_Object=MibTableColumn
ospfNumberOfLsdbEntries=_OspfNumberOfLsdbEntries_Object((1,3,6,1,4,1,1872,2,1,9,5,2,1,4),_OspfNumberOfLsdbEntries_Type())
ospfNumberOfLsdbEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNumberOfLsdbEntries.setStatus(_A)
_OspfAreaInfoId_Type=IpAddress
_OspfAreaInfoId_Object=MibTableColumn
ospfAreaInfoId=_OspfAreaInfoId_Object((1,3,6,1,4,1,1872,2,1,9,5,2,1,5),_OspfAreaInfoId_Type())
ospfAreaInfoId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaInfoId.setStatus(_A)
_OspfIntfInfoTable_Object=MibTable
ospfIntfInfoTable=_OspfIntfInfoTable_Object((1,3,6,1,4,1,1872,2,1,9,5,3))
if mibBuilder.loadTexts:ospfIntfInfoTable.setStatus(_A)
_OspfIntfInfoEntry_Object=MibTableRow
ospfIntfInfoEntry=_OspfIntfInfoEntry_Object((1,3,6,1,4,1,1872,2,1,9,5,3,1))
ospfIntfInfoEntry.setIndexNames((0,_G,_t))
if mibBuilder.loadTexts:ospfIntfInfoEntry.setStatus(_A)
_OspfIfInfoIndex_Type=Integer32
_OspfIfInfoIndex_Object=MibTableColumn
ospfIfInfoIndex=_OspfIfInfoIndex_Object((1,3,6,1,4,1,1872,2,1,9,5,3,1,1),_OspfIfInfoIndex_Type())
ospfIfInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfInfoIndex.setStatus(_A)
_OspfIfDesignatedRouterIP_Type=IpAddress
_OspfIfDesignatedRouterIP_Object=MibTableColumn
ospfIfDesignatedRouterIP=_OspfIfDesignatedRouterIP_Object((1,3,6,1,4,1,1872,2,1,9,5,3,1,2),_OspfIfDesignatedRouterIP_Type())
ospfIfDesignatedRouterIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfDesignatedRouterIP.setStatus(_A)
_OspfIfBackupDesignatedRouterIP_Type=IpAddress
_OspfIfBackupDesignatedRouterIP_Object=MibTableColumn
ospfIfBackupDesignatedRouterIP=_OspfIfBackupDesignatedRouterIP_Object((1,3,6,1,4,1,1872,2,1,9,5,3,1,3),_OspfIfBackupDesignatedRouterIP_Type())
ospfIfBackupDesignatedRouterIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfBackupDesignatedRouterIP.setStatus(_A)
_OspfIfWaitInterval_Type=Integer32
_OspfIfWaitInterval_Object=MibTableColumn
ospfIfWaitInterval=_OspfIfWaitInterval_Object((1,3,6,1,4,1,1872,2,1,9,5,3,1,4),_OspfIfWaitInterval_Type())
ospfIfWaitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfWaitInterval.setStatus(_A)
_OspfIfTotalNeighbours_Type=Integer32
_OspfIfTotalNeighbours_Object=MibTableColumn
ospfIfTotalNeighbours=_OspfIfTotalNeighbours_Object((1,3,6,1,4,1,1872,2,1,9,5,3,1,5),_OspfIfTotalNeighbours_Type())
ospfIfTotalNeighbours.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfTotalNeighbours.setStatus(_A)
_OspfIfInfoIpAddress_Type=IpAddress
_OspfIfInfoIpAddress_Object=MibTableColumn
ospfIfInfoIpAddress=_OspfIfInfoIpAddress_Object((1,3,6,1,4,1,1872,2,1,9,5,3,1,6),_OspfIfInfoIpAddress_Type())
ospfIfInfoIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfInfoIpAddress.setStatus(_A)
_OspfRouterLSAInfoTable_Object=MibTable
ospfRouterLSAInfoTable=_OspfRouterLSAInfoTable_Object((1,3,6,1,4,1,1872,2,1,9,5,4))
if mibBuilder.loadTexts:ospfRouterLSAInfoTable.setStatus(_A)
_OspfRouterLSAInfoEntry_Object=MibTableRow
ospfRouterLSAInfoEntry=_OspfRouterLSAInfoEntry_Object((1,3,6,1,4,1,1872,2,1,9,5,4,1))
ospfRouterLSAInfoEntry.setIndexNames((0,_G,_u),(0,_G,_v),(0,_G,_w))
if mibBuilder.loadTexts:ospfRouterLSAInfoEntry.setStatus(_A)
_RouterLSAAreaIndex_Type=Integer32
_RouterLSAAreaIndex_Object=MibTableColumn
routerLSAAreaIndex=_RouterLSAAreaIndex_Object((1,3,6,1,4,1,1872,2,1,9,5,4,1,1),_RouterLSAAreaIndex_Type())
routerLSAAreaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:routerLSAAreaIndex.setStatus(_A)
_RouterLSALinkIndex_Type=Integer32
_RouterLSALinkIndex_Object=MibTableColumn
routerLSALinkIndex=_RouterLSALinkIndex_Object((1,3,6,1,4,1,1872,2,1,9,5,4,1,2),_RouterLSALinkIndex_Type())
routerLSALinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:routerLSALinkIndex.setStatus(_A)
_RouterLSAId_Type=IpAddress
_RouterLSAId_Object=MibTableColumn
routerLSAId=_RouterLSAId_Object((1,3,6,1,4,1,1872,2,1,9,5,4,1,3),_RouterLSAId_Type())
routerLSAId.setMaxAccess(_B)
if mibBuilder.loadTexts:routerLSAId.setStatus(_A)
_RouterLSALinkID_Type=IpAddress
_RouterLSALinkID_Object=MibTableColumn
routerLSALinkID=_RouterLSALinkID_Object((1,3,6,1,4,1,1872,2,1,9,5,4,1,4),_RouterLSALinkID_Type())
routerLSALinkID.setMaxAccess(_B)
if mibBuilder.loadTexts:routerLSALinkID.setStatus(_A)
_RouterLSALinkData_Type=IpAddress
_RouterLSALinkData_Object=MibTableColumn
routerLSALinkData=_RouterLSALinkData_Object((1,3,6,1,4,1,1872,2,1,9,5,4,1,5),_RouterLSALinkData_Type())
routerLSALinkData.setMaxAccess(_B)
if mibBuilder.loadTexts:routerLSALinkData.setStatus(_A)
_RouterLSALinkIfIndex_Type=Integer32
_RouterLSALinkIfIndex_Object=MibTableColumn
routerLSALinkIfIndex=_RouterLSALinkIfIndex_Object((1,3,6,1,4,1,1872,2,1,9,5,4,1,6),_RouterLSALinkIfIndex_Type())
routerLSALinkIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:routerLSALinkIfIndex.setStatus(_A)
_RouterLSANoOfTOSMetrics_Type=Integer32
_RouterLSANoOfTOSMetrics_Object=MibTableColumn
routerLSANoOfTOSMetrics=_RouterLSANoOfTOSMetrics_Object((1,3,6,1,4,1,1872,2,1,9,5,4,1,7),_RouterLSANoOfTOSMetrics_Type())
routerLSANoOfTOSMetrics.setMaxAccess(_B)
if mibBuilder.loadTexts:routerLSANoOfTOSMetrics.setStatus(_A)
_RouterLSANoOfTOSZeroMetrics_Type=Integer32
_RouterLSANoOfTOSZeroMetrics_Object=MibTableColumn
routerLSANoOfTOSZeroMetrics=_RouterLSANoOfTOSZeroMetrics_Object((1,3,6,1,4,1,1872,2,1,9,5,4,1,8),_RouterLSANoOfTOSZeroMetrics_Type())
routerLSANoOfTOSZeroMetrics.setMaxAccess(_B)
if mibBuilder.loadTexts:routerLSANoOfTOSZeroMetrics.setStatus(_A)
_VrrpOper_ObjectIdentity=ObjectIdentity
vrrpOper=_VrrpOper_ObjectIdentity((1,3,6,1,4,1,1872,2,1,14,5))
_VrrpOperVirtRtrTable_Object=MibTable
vrrpOperVirtRtrTable=_VrrpOperVirtRtrTable_Object((1,3,6,1,4,1,1872,2,1,14,5,1))
if mibBuilder.loadTexts:vrrpOperVirtRtrTable.setStatus(_A)
_VrrpOperVirtRtrEntry_Object=MibTableRow
vrrpOperVirtRtrEntry=_VrrpOperVirtRtrEntry_Object((1,3,6,1,4,1,1872,2,1,14,5,1,1))
vrrpOperVirtRtrEntry.setIndexNames((0,_G,_x))
if mibBuilder.loadTexts:vrrpOperVirtRtrEntry.setStatus(_A)
_VrrpOperVirtRtrIndex_Type=Integer32
_VrrpOperVirtRtrIndex_Object=MibTableColumn
vrrpOperVirtRtrIndex=_VrrpOperVirtRtrIndex_Object((1,3,6,1,4,1,1872,2,1,14,5,1,1,1),_VrrpOperVirtRtrIndex_Type())
vrrpOperVirtRtrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpOperVirtRtrIndex.setStatus(_A)
class _VrrpOperVirtRtrBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_N,2)))
_VrrpOperVirtRtrBackup_Type.__name__=_C
_VrrpOperVirtRtrBackup_Object=MibTableColumn
vrrpOperVirtRtrBackup=_VrrpOperVirtRtrBackup_Object((1,3,6,1,4,1,1872,2,1,14,5,1,1,2),_VrrpOperVirtRtrBackup_Type())
vrrpOperVirtRtrBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperVirtRtrBackup.setStatus(_A)
class _VrrpOperVirtRtrGroupBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_N,2)))
_VrrpOperVirtRtrGroupBackup_Type.__name__=_C
_VrrpOperVirtRtrGroupBackup_Object=MibScalar
vrrpOperVirtRtrGroupBackup=_VrrpOperVirtRtrGroupBackup_Object((1,3,6,1,4,1,1872,2,1,14,5,2),_VrrpOperVirtRtrGroupBackup_Type())
vrrpOperVirtRtrGroupBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperVirtRtrGroupBackup.setStatus(_A)
_Vrrp_ObjectIdentity=ObjectIdentity
vrrp=_Vrrp_ObjectIdentity((1,3,6,1,4,1,1872,2,1,15))
_VrrpGeneral_ObjectIdentity=ObjectIdentity
vrrpGeneral=_VrrpGeneral_ObjectIdentity((1,3,6,1,4,1,1872,2,1,15,1))
class _VrrpCurCfgGenState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgGenState_Type.__name__=_C
_VrrpCurCfgGenState_Object=MibScalar
vrrpCurCfgGenState=_VrrpCurCfgGenState_Object((1,3,6,1,4,1,1872,2,1,15,1,1),_VrrpCurCfgGenState_Type())
vrrpCurCfgGenState.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenState.setStatus(_A)
class _VrrpNewCfgGenState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgGenState_Type.__name__=_C
_VrrpNewCfgGenState_Object=MibScalar
vrrpNewCfgGenState=_VrrpNewCfgGenState_Object((1,3,6,1,4,1,1872,2,1,15,1,2),_VrrpNewCfgGenState_Type())
vrrpNewCfgGenState.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgGenState.setStatus(_A)
class _VrrpCurCfgGenTckVirtRtrInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckVirtRtrInc_Type.__name__=_C
_VrrpCurCfgGenTckVirtRtrInc_Object=MibScalar
vrrpCurCfgGenTckVirtRtrInc=_VrrpCurCfgGenTckVirtRtrInc_Object((1,3,6,1,4,1,1872,2,1,15,1,3),_VrrpCurCfgGenTckVirtRtrInc_Type())
vrrpCurCfgGenTckVirtRtrInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckVirtRtrInc.setStatus(_A)
class _VrrpNewCfgGenTckVirtRtrInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckVirtRtrInc_Type.__name__=_C
_VrrpNewCfgGenTckVirtRtrInc_Object=MibScalar
vrrpNewCfgGenTckVirtRtrInc=_VrrpNewCfgGenTckVirtRtrInc_Object((1,3,6,1,4,1,1872,2,1,15,1,4),_VrrpNewCfgGenTckVirtRtrInc_Type())
vrrpNewCfgGenTckVirtRtrInc.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgGenTckVirtRtrInc.setStatus(_A)
class _VrrpCurCfgGenTckIpIntfInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckIpIntfInc_Type.__name__=_C
_VrrpCurCfgGenTckIpIntfInc_Object=MibScalar
vrrpCurCfgGenTckIpIntfInc=_VrrpCurCfgGenTckIpIntfInc_Object((1,3,6,1,4,1,1872,2,1,15,1,5),_VrrpCurCfgGenTckIpIntfInc_Type())
vrrpCurCfgGenTckIpIntfInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckIpIntfInc.setStatus(_A)
class _VrrpNewCfgGenTckIpIntfInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckIpIntfInc_Type.__name__=_C
_VrrpNewCfgGenTckIpIntfInc_Object=MibScalar
vrrpNewCfgGenTckIpIntfInc=_VrrpNewCfgGenTckIpIntfInc_Object((1,3,6,1,4,1,1872,2,1,15,1,6),_VrrpNewCfgGenTckIpIntfInc_Type())
vrrpNewCfgGenTckIpIntfInc.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgGenTckIpIntfInc.setStatus(_A)
class _VrrpCurCfgGenTckVlanPortInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckVlanPortInc_Type.__name__=_C
_VrrpCurCfgGenTckVlanPortInc_Object=MibScalar
vrrpCurCfgGenTckVlanPortInc=_VrrpCurCfgGenTckVlanPortInc_Object((1,3,6,1,4,1,1872,2,1,15,1,7),_VrrpCurCfgGenTckVlanPortInc_Type())
vrrpCurCfgGenTckVlanPortInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckVlanPortInc.setStatus(_A)
class _VrrpNewCfgGenTckVlanPortInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckVlanPortInc_Type.__name__=_C
_VrrpNewCfgGenTckVlanPortInc_Object=MibScalar
vrrpNewCfgGenTckVlanPortInc=_VrrpNewCfgGenTckVlanPortInc_Object((1,3,6,1,4,1,1872,2,1,15,1,8),_VrrpNewCfgGenTckVlanPortInc_Type())
vrrpNewCfgGenTckVlanPortInc.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgGenTckVlanPortInc.setStatus(_A)
class _VrrpCurCfgGenTckL4PortInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckL4PortInc_Type.__name__=_C
_VrrpCurCfgGenTckL4PortInc_Object=MibScalar
vrrpCurCfgGenTckL4PortInc=_VrrpCurCfgGenTckL4PortInc_Object((1,3,6,1,4,1,1872,2,1,15,1,9),_VrrpCurCfgGenTckL4PortInc_Type())
vrrpCurCfgGenTckL4PortInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckL4PortInc.setStatus(_A)
class _VrrpNewCfgGenTckL4PortInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckL4PortInc_Type.__name__=_C
_VrrpNewCfgGenTckL4PortInc_Object=MibScalar
vrrpNewCfgGenTckL4PortInc=_VrrpNewCfgGenTckL4PortInc_Object((1,3,6,1,4,1,1872,2,1,15,1,10),_VrrpNewCfgGenTckL4PortInc_Type())
vrrpNewCfgGenTckL4PortInc.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgGenTckL4PortInc.setStatus(_A)
class _VrrpCurCfgGenTckRServerInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckRServerInc_Type.__name__=_C
_VrrpCurCfgGenTckRServerInc_Object=MibScalar
vrrpCurCfgGenTckRServerInc=_VrrpCurCfgGenTckRServerInc_Object((1,3,6,1,4,1,1872,2,1,15,1,11),_VrrpCurCfgGenTckRServerInc_Type())
vrrpCurCfgGenTckRServerInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckRServerInc.setStatus(_A)
class _VrrpNewCfgGenTckRServerInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckRServerInc_Type.__name__=_C
_VrrpNewCfgGenTckRServerInc_Object=MibScalar
vrrpNewCfgGenTckRServerInc=_VrrpNewCfgGenTckRServerInc_Object((1,3,6,1,4,1,1872,2,1,15,1,12),_VrrpNewCfgGenTckRServerInc_Type())
vrrpNewCfgGenTckRServerInc.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgGenTckRServerInc.setStatus(_A)
class _VrrpCurCfgGenTckHsrpInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckHsrpInc_Type.__name__=_C
_VrrpCurCfgGenTckHsrpInc_Object=MibScalar
vrrpCurCfgGenTckHsrpInc=_VrrpCurCfgGenTckHsrpInc_Object((1,3,6,1,4,1,1872,2,1,15,1,13),_VrrpCurCfgGenTckHsrpInc_Type())
vrrpCurCfgGenTckHsrpInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckHsrpInc.setStatus(_A)
class _VrrpNewCfgGenTckHsrpInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckHsrpInc_Type.__name__=_C
_VrrpNewCfgGenTckHsrpInc_Object=MibScalar
vrrpNewCfgGenTckHsrpInc=_VrrpNewCfgGenTckHsrpInc_Object((1,3,6,1,4,1,1872,2,1,15,1,14),_VrrpNewCfgGenTckHsrpInc_Type())
vrrpNewCfgGenTckHsrpInc.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgGenTckHsrpInc.setStatus(_A)
class _VrrpCurCfgGenHotstandby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgGenHotstandby_Type.__name__=_C
_VrrpCurCfgGenHotstandby_Object=MibScalar
vrrpCurCfgGenHotstandby=_VrrpCurCfgGenHotstandby_Object((1,3,6,1,4,1,1872,2,1,15,1,15),_VrrpCurCfgGenHotstandby_Type())
vrrpCurCfgGenHotstandby.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenHotstandby.setStatus(_A)
class _VrrpNewCfgGenHotstandby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgGenHotstandby_Type.__name__=_C
_VrrpNewCfgGenHotstandby_Object=MibScalar
vrrpNewCfgGenHotstandby=_VrrpNewCfgGenHotstandby_Object((1,3,6,1,4,1,1872,2,1,15,1,16),_VrrpNewCfgGenHotstandby_Type())
vrrpNewCfgGenHotstandby.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgGenHotstandby.setStatus(_A)
class _VrrpCurCfgGenTckHsrvInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpCurCfgGenTckHsrvInc_Type.__name__=_C
_VrrpCurCfgGenTckHsrvInc_Object=MibScalar
vrrpCurCfgGenTckHsrvInc=_VrrpCurCfgGenTckHsrvInc_Object((1,3,6,1,4,1,1872,2,1,15,1,17),_VrrpCurCfgGenTckHsrvInc_Type())
vrrpCurCfgGenTckHsrvInc.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgGenTckHsrvInc.setStatus(_A)
class _VrrpNewCfgGenTckHsrvInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_VrrpNewCfgGenTckHsrvInc_Type.__name__=_C
_VrrpNewCfgGenTckHsrvInc_Object=MibScalar
vrrpNewCfgGenTckHsrvInc=_VrrpNewCfgGenTckHsrvInc_Object((1,3,6,1,4,1,1872,2,1,15,1,18),_VrrpNewCfgGenTckHsrvInc_Type())
vrrpNewCfgGenTckHsrvInc.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgGenTckHsrvInc.setStatus(_A)
_VrrpCurCfgVirtRtrTable_Object=MibTable
vrrpCurCfgVirtRtrTable=_VrrpCurCfgVirtRtrTable_Object((1,3,6,1,4,1,1872,2,1,15,2))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTable.setStatus(_A)
_VrrpCurCfgVirtRtrTableEntry_Object=MibTableRow
vrrpCurCfgVirtRtrTableEntry=_VrrpCurCfgVirtRtrTableEntry_Object((1,3,6,1,4,1,1872,2,1,15,2,1))
vrrpCurCfgVirtRtrTableEntry.setIndexNames((0,_G,_y))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTableEntry.setStatus(_A)
_VrrpCurCfgVirtRtrIndx_Type=Integer32
_VrrpCurCfgVirtRtrIndx_Object=MibTableColumn
vrrpCurCfgVirtRtrIndx=_VrrpCurCfgVirtRtrIndx_Object((1,3,6,1,4,1,1872,2,1,15,2,1,1),_VrrpCurCfgVirtRtrIndx_Type())
vrrpCurCfgVirtRtrIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrIndx.setStatus(_A)
class _VrrpCurCfgVirtRtrID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpCurCfgVirtRtrID_Type.__name__=_C
_VrrpCurCfgVirtRtrID_Object=MibTableColumn
vrrpCurCfgVirtRtrID=_VrrpCurCfgVirtRtrID_Object((1,3,6,1,4,1,1872,2,1,15,2,1,2),_VrrpCurCfgVirtRtrID_Type())
vrrpCurCfgVirtRtrID.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrID.setStatus(_A)
_VrrpCurCfgVirtRtrAddr_Type=IpAddress
_VrrpCurCfgVirtRtrAddr_Object=MibTableColumn
vrrpCurCfgVirtRtrAddr=_VrrpCurCfgVirtRtrAddr_Object((1,3,6,1,4,1,1872,2,1,15,2,1,3),_VrrpCurCfgVirtRtrAddr_Type())
vrrpCurCfgVirtRtrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrAddr.setStatus(_A)
_VrrpCurCfgVirtRtrIfIndex_Type=Integer32
_VrrpCurCfgVirtRtrIfIndex_Object=MibTableColumn
vrrpCurCfgVirtRtrIfIndex=_VrrpCurCfgVirtRtrIfIndex_Object((1,3,6,1,4,1,1872,2,1,15,2,1,4),_VrrpCurCfgVirtRtrIfIndex_Type())
vrrpCurCfgVirtRtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrIfIndex.setStatus(_A)
class _VrrpCurCfgVirtRtrInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpCurCfgVirtRtrInterval_Type.__name__=_C
_VrrpCurCfgVirtRtrInterval_Object=MibTableColumn
vrrpCurCfgVirtRtrInterval=_VrrpCurCfgVirtRtrInterval_Object((1,3,6,1,4,1,1872,2,1,15,2,1,5),_VrrpCurCfgVirtRtrInterval_Type())
vrrpCurCfgVirtRtrInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrInterval.setStatus(_A)
class _VrrpCurCfgVirtRtrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpCurCfgVirtRtrPriority_Type.__name__=_C
_VrrpCurCfgVirtRtrPriority_Object=MibTableColumn
vrrpCurCfgVirtRtrPriority=_VrrpCurCfgVirtRtrPriority_Object((1,3,6,1,4,1,1872,2,1,15,2,1,6),_VrrpCurCfgVirtRtrPriority_Type())
vrrpCurCfgVirtRtrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrPriority.setStatus(_A)
class _VrrpCurCfgVirtRtrPreempt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrPreempt_Type.__name__=_C
_VrrpCurCfgVirtRtrPreempt_Object=MibTableColumn
vrrpCurCfgVirtRtrPreempt=_VrrpCurCfgVirtRtrPreempt_Object((1,3,6,1,4,1,1872,2,1,15,2,1,7),_VrrpCurCfgVirtRtrPreempt_Type())
vrrpCurCfgVirtRtrPreempt.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrPreempt.setStatus(_A)
class _VrrpCurCfgVirtRtrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrState_Type.__name__=_C
_VrrpCurCfgVirtRtrState_Object=MibTableColumn
vrrpCurCfgVirtRtrState=_VrrpCurCfgVirtRtrState_Object((1,3,6,1,4,1,1872,2,1,15,2,1,8),_VrrpCurCfgVirtRtrState_Type())
vrrpCurCfgVirtRtrState.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrState.setStatus(_A)
class _VrrpCurCfgVirtRtrSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrSharing_Type.__name__=_C
_VrrpCurCfgVirtRtrSharing_Object=MibTableColumn
vrrpCurCfgVirtRtrSharing=_VrrpCurCfgVirtRtrSharing_Object((1,3,6,1,4,1,1872,2,1,15,2,1,9),_VrrpCurCfgVirtRtrSharing_Type())
vrrpCurCfgVirtRtrSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrSharing.setStatus(_A)
class _VrrpCurCfgVirtRtrTckVirtRtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrTckVirtRtr_Type.__name__=_C
_VrrpCurCfgVirtRtrTckVirtRtr_Object=MibTableColumn
vrrpCurCfgVirtRtrTckVirtRtr=_VrrpCurCfgVirtRtrTckVirtRtr_Object((1,3,6,1,4,1,1872,2,1,15,2,1,10),_VrrpCurCfgVirtRtrTckVirtRtr_Type())
vrrpCurCfgVirtRtrTckVirtRtr.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckVirtRtr.setStatus(_A)
class _VrrpCurCfgVirtRtrTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrTckIpIntf_Type.__name__=_C
_VrrpCurCfgVirtRtrTckIpIntf_Object=MibTableColumn
vrrpCurCfgVirtRtrTckIpIntf=_VrrpCurCfgVirtRtrTckIpIntf_Object((1,3,6,1,4,1,1872,2,1,15,2,1,11),_VrrpCurCfgVirtRtrTckIpIntf_Type())
vrrpCurCfgVirtRtrTckIpIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckIpIntf.setStatus(_A)
class _VrrpCurCfgVirtRtrTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrTckVlanPort_Type.__name__=_C
_VrrpCurCfgVirtRtrTckVlanPort_Object=MibTableColumn
vrrpCurCfgVirtRtrTckVlanPort=_VrrpCurCfgVirtRtrTckVlanPort_Object((1,3,6,1,4,1,1872,2,1,15,2,1,12),_VrrpCurCfgVirtRtrTckVlanPort_Type())
vrrpCurCfgVirtRtrTckVlanPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckVlanPort.setStatus(_A)
class _VrrpCurCfgVirtRtrTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrTckL4Port_Type.__name__=_C
_VrrpCurCfgVirtRtrTckL4Port_Object=MibTableColumn
vrrpCurCfgVirtRtrTckL4Port=_VrrpCurCfgVirtRtrTckL4Port_Object((1,3,6,1,4,1,1872,2,1,15,2,1,13),_VrrpCurCfgVirtRtrTckL4Port_Type())
vrrpCurCfgVirtRtrTckL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckL4Port.setStatus(_A)
class _VrrpCurCfgVirtRtrTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrTckRServer_Type.__name__=_C
_VrrpCurCfgVirtRtrTckRServer_Object=MibTableColumn
vrrpCurCfgVirtRtrTckRServer=_VrrpCurCfgVirtRtrTckRServer_Object((1,3,6,1,4,1,1872,2,1,15,2,1,14),_VrrpCurCfgVirtRtrTckRServer_Type())
vrrpCurCfgVirtRtrTckRServer.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckRServer.setStatus(_A)
class _VrrpCurCfgVirtRtrTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrTckHsrp_Type.__name__=_C
_VrrpCurCfgVirtRtrTckHsrp_Object=MibTableColumn
vrrpCurCfgVirtRtrTckHsrp=_VrrpCurCfgVirtRtrTckHsrp_Object((1,3,6,1,4,1,1872,2,1,15,2,1,15),_VrrpCurCfgVirtRtrTckHsrp_Type())
vrrpCurCfgVirtRtrTckHsrp.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckHsrp.setStatus(_A)
class _VrrpCurCfgVirtRtrTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrTckHsrv_Type.__name__=_C
_VrrpCurCfgVirtRtrTckHsrv_Object=MibTableColumn
vrrpCurCfgVirtRtrTckHsrv=_VrrpCurCfgVirtRtrTckHsrv_Object((1,3,6,1,4,1,1872,2,1,15,2,1,16),_VrrpCurCfgVirtRtrTckHsrv_Type())
vrrpCurCfgVirtRtrTckHsrv.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrTckHsrv.setStatus(_A)
_VrrpNewCfgVirtRtrTable_Object=MibTable
vrrpNewCfgVirtRtrTable=_VrrpNewCfgVirtRtrTable_Object((1,3,6,1,4,1,1872,2,1,15,3))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTable.setStatus(_A)
_VrrpNewCfgVirtRtrTableEntry_Object=MibTableRow
vrrpNewCfgVirtRtrTableEntry=_VrrpNewCfgVirtRtrTableEntry_Object((1,3,6,1,4,1,1872,2,1,15,3,1))
vrrpNewCfgVirtRtrTableEntry.setIndexNames((0,_G,_z))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTableEntry.setStatus(_A)
_VrrpNewCfgVirtRtrIndx_Type=Integer32
_VrrpNewCfgVirtRtrIndx_Object=MibTableColumn
vrrpNewCfgVirtRtrIndx=_VrrpNewCfgVirtRtrIndx_Object((1,3,6,1,4,1,1872,2,1,15,3,1,1),_VrrpNewCfgVirtRtrIndx_Type())
vrrpNewCfgVirtRtrIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrIndx.setStatus(_A)
class _VrrpNewCfgVirtRtrID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpNewCfgVirtRtrID_Type.__name__=_C
_VrrpNewCfgVirtRtrID_Object=MibTableColumn
vrrpNewCfgVirtRtrID=_VrrpNewCfgVirtRtrID_Object((1,3,6,1,4,1,1872,2,1,15,3,1,2),_VrrpNewCfgVirtRtrID_Type())
vrrpNewCfgVirtRtrID.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrID.setStatus(_A)
_VrrpNewCfgVirtRtrAddr_Type=IpAddress
_VrrpNewCfgVirtRtrAddr_Object=MibTableColumn
vrrpNewCfgVirtRtrAddr=_VrrpNewCfgVirtRtrAddr_Object((1,3,6,1,4,1,1872,2,1,15,3,1,3),_VrrpNewCfgVirtRtrAddr_Type())
vrrpNewCfgVirtRtrAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrAddr.setStatus(_A)
_VrrpNewCfgVirtRtrIfIndex_Type=Integer32
_VrrpNewCfgVirtRtrIfIndex_Object=MibTableColumn
vrrpNewCfgVirtRtrIfIndex=_VrrpNewCfgVirtRtrIfIndex_Object((1,3,6,1,4,1,1872,2,1,15,3,1,4),_VrrpNewCfgVirtRtrIfIndex_Type())
vrrpNewCfgVirtRtrIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrIfIndex.setStatus(_A)
class _VrrpNewCfgVirtRtrInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpNewCfgVirtRtrInterval_Type.__name__=_C
_VrrpNewCfgVirtRtrInterval_Object=MibTableColumn
vrrpNewCfgVirtRtrInterval=_VrrpNewCfgVirtRtrInterval_Object((1,3,6,1,4,1,1872,2,1,15,3,1,5),_VrrpNewCfgVirtRtrInterval_Type())
vrrpNewCfgVirtRtrInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrInterval.setStatus(_A)
class _VrrpNewCfgVirtRtrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpNewCfgVirtRtrPriority_Type.__name__=_C
_VrrpNewCfgVirtRtrPriority_Object=MibTableColumn
vrrpNewCfgVirtRtrPriority=_VrrpNewCfgVirtRtrPriority_Object((1,3,6,1,4,1,1872,2,1,15,3,1,6),_VrrpNewCfgVirtRtrPriority_Type())
vrrpNewCfgVirtRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrPriority.setStatus(_A)
class _VrrpNewCfgVirtRtrPreempt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrPreempt_Type.__name__=_C
_VrrpNewCfgVirtRtrPreempt_Object=MibTableColumn
vrrpNewCfgVirtRtrPreempt=_VrrpNewCfgVirtRtrPreempt_Object((1,3,6,1,4,1,1872,2,1,15,3,1,7),_VrrpNewCfgVirtRtrPreempt_Type())
vrrpNewCfgVirtRtrPreempt.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrPreempt.setStatus(_A)
class _VrrpNewCfgVirtRtrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrState_Type.__name__=_C
_VrrpNewCfgVirtRtrState_Object=MibTableColumn
vrrpNewCfgVirtRtrState=_VrrpNewCfgVirtRtrState_Object((1,3,6,1,4,1,1872,2,1,15,3,1,8),_VrrpNewCfgVirtRtrState_Type())
vrrpNewCfgVirtRtrState.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrState.setStatus(_A)
class _VrrpNewCfgVirtRtrDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_VrrpNewCfgVirtRtrDelete_Type.__name__=_C
_VrrpNewCfgVirtRtrDelete_Object=MibTableColumn
vrrpNewCfgVirtRtrDelete=_VrrpNewCfgVirtRtrDelete_Object((1,3,6,1,4,1,1872,2,1,15,3,1,9),_VrrpNewCfgVirtRtrDelete_Type())
vrrpNewCfgVirtRtrDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrDelete.setStatus(_A)
class _VrrpNewCfgVirtRtrSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrSharing_Type.__name__=_C
_VrrpNewCfgVirtRtrSharing_Object=MibTableColumn
vrrpNewCfgVirtRtrSharing=_VrrpNewCfgVirtRtrSharing_Object((1,3,6,1,4,1,1872,2,1,15,3,1,10),_VrrpNewCfgVirtRtrSharing_Type())
vrrpNewCfgVirtRtrSharing.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrSharing.setStatus(_A)
class _VrrpNewCfgVirtRtrTckVirtRtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrTckVirtRtr_Type.__name__=_C
_VrrpNewCfgVirtRtrTckVirtRtr_Object=MibTableColumn
vrrpNewCfgVirtRtrTckVirtRtr=_VrrpNewCfgVirtRtrTckVirtRtr_Object((1,3,6,1,4,1,1872,2,1,15,3,1,11),_VrrpNewCfgVirtRtrTckVirtRtr_Type())
vrrpNewCfgVirtRtrTckVirtRtr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckVirtRtr.setStatus(_A)
class _VrrpNewCfgVirtRtrTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrTckIpIntf_Type.__name__=_C
_VrrpNewCfgVirtRtrTckIpIntf_Object=MibTableColumn
vrrpNewCfgVirtRtrTckIpIntf=_VrrpNewCfgVirtRtrTckIpIntf_Object((1,3,6,1,4,1,1872,2,1,15,3,1,12),_VrrpNewCfgVirtRtrTckIpIntf_Type())
vrrpNewCfgVirtRtrTckIpIntf.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckIpIntf.setStatus(_A)
class _VrrpNewCfgVirtRtrTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrTckVlanPort_Type.__name__=_C
_VrrpNewCfgVirtRtrTckVlanPort_Object=MibTableColumn
vrrpNewCfgVirtRtrTckVlanPort=_VrrpNewCfgVirtRtrTckVlanPort_Object((1,3,6,1,4,1,1872,2,1,15,3,1,13),_VrrpNewCfgVirtRtrTckVlanPort_Type())
vrrpNewCfgVirtRtrTckVlanPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckVlanPort.setStatus(_A)
class _VrrpNewCfgVirtRtrTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrTckL4Port_Type.__name__=_C
_VrrpNewCfgVirtRtrTckL4Port_Object=MibTableColumn
vrrpNewCfgVirtRtrTckL4Port=_VrrpNewCfgVirtRtrTckL4Port_Object((1,3,6,1,4,1,1872,2,1,15,3,1,14),_VrrpNewCfgVirtRtrTckL4Port_Type())
vrrpNewCfgVirtRtrTckL4Port.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckL4Port.setStatus(_A)
class _VrrpNewCfgVirtRtrTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrTckRServer_Type.__name__=_C
_VrrpNewCfgVirtRtrTckRServer_Object=MibTableColumn
vrrpNewCfgVirtRtrTckRServer=_VrrpNewCfgVirtRtrTckRServer_Object((1,3,6,1,4,1,1872,2,1,15,3,1,15),_VrrpNewCfgVirtRtrTckRServer_Type())
vrrpNewCfgVirtRtrTckRServer.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckRServer.setStatus(_A)
class _VrrpNewCfgVirtRtrTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrTckHsrp_Type.__name__=_C
_VrrpNewCfgVirtRtrTckHsrp_Object=MibTableColumn
vrrpNewCfgVirtRtrTckHsrp=_VrrpNewCfgVirtRtrTckHsrp_Object((1,3,6,1,4,1,1872,2,1,15,3,1,16),_VrrpNewCfgVirtRtrTckHsrp_Type())
vrrpNewCfgVirtRtrTckHsrp.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckHsrp.setStatus(_A)
class _VrrpNewCfgVirtRtrTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrTckHsrv_Type.__name__=_C
_VrrpNewCfgVirtRtrTckHsrv_Object=MibTableColumn
vrrpNewCfgVirtRtrTckHsrv=_VrrpNewCfgVirtRtrTckHsrv_Object((1,3,6,1,4,1,1872,2,1,15,3,1,17),_VrrpNewCfgVirtRtrTckHsrv_Type())
vrrpNewCfgVirtRtrTckHsrv.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrTckHsrv.setStatus(_A)
_VrrpCurCfgIfTable_Object=MibTable
vrrpCurCfgIfTable=_VrrpCurCfgIfTable_Object((1,3,6,1,4,1,1872,2,1,15,4))
if mibBuilder.loadTexts:vrrpCurCfgIfTable.setStatus(_A)
_VrrpCurCfgIfTableEntry_Object=MibTableRow
vrrpCurCfgIfTableEntry=_VrrpCurCfgIfTableEntry_Object((1,3,6,1,4,1,1872,2,1,15,4,1))
vrrpCurCfgIfTableEntry.setIndexNames((0,_G,_A0))
if mibBuilder.loadTexts:vrrpCurCfgIfTableEntry.setStatus(_A)
_VrrpCurCfgIfIndx_Type=Integer32
_VrrpCurCfgIfIndx_Object=MibTableColumn
vrrpCurCfgIfIndx=_VrrpCurCfgIfIndx_Object((1,3,6,1,4,1,1872,2,1,15,4,1,1),_VrrpCurCfgIfIndx_Type())
vrrpCurCfgIfIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgIfIndx.setStatus(_A)
class _VrrpCurCfgIfAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_A1,2)))
_VrrpCurCfgIfAuthType_Type.__name__=_C
_VrrpCurCfgIfAuthType_Object=MibTableColumn
vrrpCurCfgIfAuthType=_VrrpCurCfgIfAuthType_Object((1,3,6,1,4,1,1872,2,1,15,4,1,2),_VrrpCurCfgIfAuthType_Type())
vrrpCurCfgIfAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgIfAuthType.setStatus(_A)
class _VrrpCurCfgIfPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_VrrpCurCfgIfPasswd_Type.__name__=_M
_VrrpCurCfgIfPasswd_Object=MibTableColumn
vrrpCurCfgIfPasswd=_VrrpCurCfgIfPasswd_Object((1,3,6,1,4,1,1872,2,1,15,4,1,3),_VrrpCurCfgIfPasswd_Type())
vrrpCurCfgIfPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgIfPasswd.setStatus(_A)
_VrrpNewCfgIfTable_Object=MibTable
vrrpNewCfgIfTable=_VrrpNewCfgIfTable_Object((1,3,6,1,4,1,1872,2,1,15,5))
if mibBuilder.loadTexts:vrrpNewCfgIfTable.setStatus(_A)
_VrrpNewCfgIfTableEntry_Object=MibTableRow
vrrpNewCfgIfTableEntry=_VrrpNewCfgIfTableEntry_Object((1,3,6,1,4,1,1872,2,1,15,5,1))
vrrpNewCfgIfTableEntry.setIndexNames((0,_G,_A2))
if mibBuilder.loadTexts:vrrpNewCfgIfTableEntry.setStatus(_A)
_VrrpNewCfgIfIndx_Type=Integer32
_VrrpNewCfgIfIndx_Object=MibTableColumn
vrrpNewCfgIfIndx=_VrrpNewCfgIfIndx_Object((1,3,6,1,4,1,1872,2,1,15,5,1,1),_VrrpNewCfgIfIndx_Type())
vrrpNewCfgIfIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpNewCfgIfIndx.setStatus(_A)
class _VrrpNewCfgIfAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_A1,2)))
_VrrpNewCfgIfAuthType_Type.__name__=_C
_VrrpNewCfgIfAuthType_Object=MibTableColumn
vrrpNewCfgIfAuthType=_VrrpNewCfgIfAuthType_Object((1,3,6,1,4,1,1872,2,1,15,5,1,2),_VrrpNewCfgIfAuthType_Type())
vrrpNewCfgIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgIfAuthType.setStatus(_A)
class _VrrpNewCfgIfPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_VrrpNewCfgIfPasswd_Type.__name__=_M
_VrrpNewCfgIfPasswd_Object=MibTableColumn
vrrpNewCfgIfPasswd=_VrrpNewCfgIfPasswd_Object((1,3,6,1,4,1,1872,2,1,15,5,1,3),_VrrpNewCfgIfPasswd_Type())
vrrpNewCfgIfPasswd.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgIfPasswd.setStatus(_A)
class _VrrpNewCfgIfDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_VrrpNewCfgIfDelete_Type.__name__=_C
_VrrpNewCfgIfDelete_Object=MibTableColumn
vrrpNewCfgIfDelete=_VrrpNewCfgIfDelete_Object((1,3,6,1,4,1,1872,2,1,15,5,1,4),_VrrpNewCfgIfDelete_Type())
vrrpNewCfgIfDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgIfDelete.setStatus(_A)
_VrrpCurCfgVirtRtrGrpTable_Object=MibTable
vrrpCurCfgVirtRtrGrpTable=_VrrpCurCfgVirtRtrGrpTable_Object((1,3,6,1,4,1,1872,2,1,15,6))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTable.setStatus(_A)
_VrrpCurCfgVirtRtrGrpTableEntry_Object=MibTableRow
vrrpCurCfgVirtRtrGrpTableEntry=_VrrpCurCfgVirtRtrGrpTableEntry_Object((1,3,6,1,4,1,1872,2,1,15,6,1))
vrrpCurCfgVirtRtrGrpTableEntry.setIndexNames((0,_G,_A3))
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTableEntry.setStatus(_A)
_VrrpCurCfgVirtRtrGrpIndx_Type=Integer32
_VrrpCurCfgVirtRtrGrpIndx_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpIndx=_VrrpCurCfgVirtRtrGrpIndx_Object((1,3,6,1,4,1,1872,2,1,15,6,1,1),_VrrpCurCfgVirtRtrGrpIndx_Type())
vrrpCurCfgVirtRtrGrpIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpIndx.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpCurCfgVirtRtrGrpID_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpID_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpID=_VrrpCurCfgVirtRtrGrpID_Object((1,3,6,1,4,1,1872,2,1,15,6,1,2),_VrrpCurCfgVirtRtrGrpID_Type())
vrrpCurCfgVirtRtrGrpID.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpID.setStatus(_A)
_VrrpCurCfgVirtRtrGrpIfIndex_Type=Integer32
_VrrpCurCfgVirtRtrGrpIfIndex_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpIfIndex=_VrrpCurCfgVirtRtrGrpIfIndex_Object((1,3,6,1,4,1,1872,2,1,15,6,1,3),_VrrpCurCfgVirtRtrGrpIfIndex_Type())
vrrpCurCfgVirtRtrGrpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpIfIndex.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpCurCfgVirtRtrGrpInterval_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpInterval_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpInterval=_VrrpCurCfgVirtRtrGrpInterval_Object((1,3,6,1,4,1,1872,2,1,15,6,1,4),_VrrpCurCfgVirtRtrGrpInterval_Type())
vrrpCurCfgVirtRtrGrpInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpInterval.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpCurCfgVirtRtrGrpPriority_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpPriority_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpPriority=_VrrpCurCfgVirtRtrGrpPriority_Object((1,3,6,1,4,1,1872,2,1,15,6,1,5),_VrrpCurCfgVirtRtrGrpPriority_Type())
vrrpCurCfgVirtRtrGrpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpPriority.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpPreempt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpPreempt_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpPreempt_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpPreempt=_VrrpCurCfgVirtRtrGrpPreempt_Object((1,3,6,1,4,1,1872,2,1,15,6,1,6),_VrrpCurCfgVirtRtrGrpPreempt_Type())
vrrpCurCfgVirtRtrGrpPreempt.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpPreempt.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpState_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpState_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpState=_VrrpCurCfgVirtRtrGrpState_Object((1,3,6,1,4,1,1872,2,1,15,6,1,7),_VrrpCurCfgVirtRtrGrpState_Type())
vrrpCurCfgVirtRtrGrpState.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpState.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpSharing_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpSharing_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpSharing=_VrrpCurCfgVirtRtrGrpSharing_Object((1,3,6,1,4,1,1872,2,1,15,6,1,8),_VrrpCurCfgVirtRtrGrpSharing_Type())
vrrpCurCfgVirtRtrGrpSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpSharing.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckVirtRtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpTckVirtRtr_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckVirtRtr_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckVirtRtr=_VrrpCurCfgVirtRtrGrpTckVirtRtr_Object((1,3,6,1,4,1,1872,2,1,15,6,1,9),_VrrpCurCfgVirtRtrGrpTckVirtRtr_Type())
vrrpCurCfgVirtRtrGrpTckVirtRtr.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckVirtRtr.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpTckIpIntf_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckIpIntf_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckIpIntf=_VrrpCurCfgVirtRtrGrpTckIpIntf_Object((1,3,6,1,4,1,1872,2,1,15,6,1,10),_VrrpCurCfgVirtRtrGrpTckIpIntf_Type())
vrrpCurCfgVirtRtrGrpTckIpIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckIpIntf.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpTckVlanPort_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckVlanPort_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckVlanPort=_VrrpCurCfgVirtRtrGrpTckVlanPort_Object((1,3,6,1,4,1,1872,2,1,15,6,1,11),_VrrpCurCfgVirtRtrGrpTckVlanPort_Type())
vrrpCurCfgVirtRtrGrpTckVlanPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckVlanPort.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpTckL4Port_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckL4Port_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckL4Port=_VrrpCurCfgVirtRtrGrpTckL4Port_Object((1,3,6,1,4,1,1872,2,1,15,6,1,12),_VrrpCurCfgVirtRtrGrpTckL4Port_Type())
vrrpCurCfgVirtRtrGrpTckL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckL4Port.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpTckRServer_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckRServer_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckRServer=_VrrpCurCfgVirtRtrGrpTckRServer_Object((1,3,6,1,4,1,1872,2,1,15,6,1,13),_VrrpCurCfgVirtRtrGrpTckRServer_Type())
vrrpCurCfgVirtRtrGrpTckRServer.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckRServer.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpTckHsrp_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckHsrp_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckHsrp=_VrrpCurCfgVirtRtrGrpTckHsrp_Object((1,3,6,1,4,1,1872,2,1,15,6,1,14),_VrrpCurCfgVirtRtrGrpTckHsrp_Type())
vrrpCurCfgVirtRtrGrpTckHsrp.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckHsrp.setStatus(_A)
class _VrrpCurCfgVirtRtrGrpTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpCurCfgVirtRtrGrpTckHsrv_Type.__name__=_C
_VrrpCurCfgVirtRtrGrpTckHsrv_Object=MibTableColumn
vrrpCurCfgVirtRtrGrpTckHsrv=_VrrpCurCfgVirtRtrGrpTckHsrv_Object((1,3,6,1,4,1,1872,2,1,15,6,1,15),_VrrpCurCfgVirtRtrGrpTckHsrv_Type())
vrrpCurCfgVirtRtrGrpTckHsrv.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpCurCfgVirtRtrGrpTckHsrv.setStatus(_A)
_VrrpNewCfgVirtRtrGrpTable_Object=MibTable
vrrpNewCfgVirtRtrGrpTable=_VrrpNewCfgVirtRtrGrpTable_Object((1,3,6,1,4,1,1872,2,1,15,7))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTable.setStatus(_A)
_VrrpNewCfgVirtRtrGrpTableEntry_Object=MibTableRow
vrrpNewCfgVirtRtrGrpTableEntry=_VrrpNewCfgVirtRtrGrpTableEntry_Object((1,3,6,1,4,1,1872,2,1,15,7,1))
vrrpNewCfgVirtRtrGrpTableEntry.setIndexNames((0,_G,_A4))
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTableEntry.setStatus(_A)
_VrrpNewCfgVirtRtrGrpIndx_Type=Integer32
_VrrpNewCfgVirtRtrGrpIndx_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpIndx=_VrrpNewCfgVirtRtrGrpIndx_Object((1,3,6,1,4,1,1872,2,1,15,7,1,1),_VrrpNewCfgVirtRtrGrpIndx_Type())
vrrpNewCfgVirtRtrGrpIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpIndx.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpNewCfgVirtRtrGrpID_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpID_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpID=_VrrpNewCfgVirtRtrGrpID_Object((1,3,6,1,4,1,1872,2,1,15,7,1,2),_VrrpNewCfgVirtRtrGrpID_Type())
vrrpNewCfgVirtRtrGrpID.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpID.setStatus(_A)
_VrrpNewCfgVirtRtrGrpIfIndex_Type=Integer32
_VrrpNewCfgVirtRtrGrpIfIndex_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpIfIndex=_VrrpNewCfgVirtRtrGrpIfIndex_Object((1,3,6,1,4,1,1872,2,1,15,7,1,3),_VrrpNewCfgVirtRtrGrpIfIndex_Type())
vrrpNewCfgVirtRtrGrpIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpIfIndex.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpNewCfgVirtRtrGrpInterval_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpInterval_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpInterval=_VrrpNewCfgVirtRtrGrpInterval_Object((1,3,6,1,4,1,1872,2,1,15,7,1,4),_VrrpNewCfgVirtRtrGrpInterval_Type())
vrrpNewCfgVirtRtrGrpInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpInterval.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_VrrpNewCfgVirtRtrGrpPriority_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpPriority_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpPriority=_VrrpNewCfgVirtRtrGrpPriority_Object((1,3,6,1,4,1,1872,2,1,15,7,1,5),_VrrpNewCfgVirtRtrGrpPriority_Type())
vrrpNewCfgVirtRtrGrpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpPriority.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpPreempt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpPreempt_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpPreempt_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpPreempt=_VrrpNewCfgVirtRtrGrpPreempt_Object((1,3,6,1,4,1,1872,2,1,15,7,1,6),_VrrpNewCfgVirtRtrGrpPreempt_Type())
vrrpNewCfgVirtRtrGrpPreempt.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpPreempt.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpState_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpState_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpState=_VrrpNewCfgVirtRtrGrpState_Object((1,3,6,1,4,1,1872,2,1,15,7,1,7),_VrrpNewCfgVirtRtrGrpState_Type())
vrrpNewCfgVirtRtrGrpState.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpState.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_VrrpNewCfgVirtRtrGrpDelete_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpDelete_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpDelete=_VrrpNewCfgVirtRtrGrpDelete_Object((1,3,6,1,4,1,1872,2,1,15,7,1,8),_VrrpNewCfgVirtRtrGrpDelete_Type())
vrrpNewCfgVirtRtrGrpDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpDelete.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpSharing_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpSharing_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpSharing=_VrrpNewCfgVirtRtrGrpSharing_Object((1,3,6,1,4,1,1872,2,1,15,7,1,9),_VrrpNewCfgVirtRtrGrpSharing_Type())
vrrpNewCfgVirtRtrGrpSharing.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpSharing.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckVirtRtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpTckVirtRtr_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckVirtRtr_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckVirtRtr=_VrrpNewCfgVirtRtrGrpTckVirtRtr_Object((1,3,6,1,4,1,1872,2,1,15,7,1,10),_VrrpNewCfgVirtRtrGrpTckVirtRtr_Type())
vrrpNewCfgVirtRtrGrpTckVirtRtr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckVirtRtr.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckIpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpTckIpIntf_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckIpIntf_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckIpIntf=_VrrpNewCfgVirtRtrGrpTckIpIntf_Object((1,3,6,1,4,1,1872,2,1,15,7,1,11),_VrrpNewCfgVirtRtrGrpTckIpIntf_Type())
vrrpNewCfgVirtRtrGrpTckIpIntf.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckIpIntf.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpTckVlanPort_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckVlanPort_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckVlanPort=_VrrpNewCfgVirtRtrGrpTckVlanPort_Object((1,3,6,1,4,1,1872,2,1,15,7,1,12),_VrrpNewCfgVirtRtrGrpTckVlanPort_Type())
vrrpNewCfgVirtRtrGrpTckVlanPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckVlanPort.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckL4Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpTckL4Port_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckL4Port_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckL4Port=_VrrpNewCfgVirtRtrGrpTckL4Port_Object((1,3,6,1,4,1,1872,2,1,15,7,1,13),_VrrpNewCfgVirtRtrGrpTckL4Port_Type())
vrrpNewCfgVirtRtrGrpTckL4Port.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckL4Port.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckRServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpTckRServer_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckRServer_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckRServer=_VrrpNewCfgVirtRtrGrpTckRServer_Object((1,3,6,1,4,1,1872,2,1,15,7,1,14),_VrrpNewCfgVirtRtrGrpTckRServer_Type())
vrrpNewCfgVirtRtrGrpTckRServer.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckRServer.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckHsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpTckHsrp_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckHsrp_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckHsrp=_VrrpNewCfgVirtRtrGrpTckHsrp_Object((1,3,6,1,4,1,1872,2,1,15,7,1,15),_VrrpNewCfgVirtRtrGrpTckHsrp_Type())
vrrpNewCfgVirtRtrGrpTckHsrp.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckHsrp.setStatus(_A)
class _VrrpNewCfgVirtRtrGrpTckHsrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_VrrpNewCfgVirtRtrGrpTckHsrv_Type.__name__=_C
_VrrpNewCfgVirtRtrGrpTckHsrv_Object=MibTableColumn
vrrpNewCfgVirtRtrGrpTckHsrv=_VrrpNewCfgVirtRtrGrpTckHsrv_Object((1,3,6,1,4,1,1872,2,1,15,7,1,16),_VrrpNewCfgVirtRtrGrpTckHsrv_Type())
vrrpNewCfgVirtRtrGrpTckHsrv.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewCfgVirtRtrGrpTckHsrv.setStatus(_A)
_VrrpVirtRtrTableMaxSize_Type=Integer32
_VrrpVirtRtrTableMaxSize_Object=MibScalar
vrrpVirtRtrTableMaxSize=_VrrpVirtRtrTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,15,8),_VrrpVirtRtrTableMaxSize_Type())
vrrpVirtRtrTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpVirtRtrTableMaxSize.setStatus(_A)
_VrrpIfTableMaxSize_Type=Integer32
_VrrpIfTableMaxSize_Object=MibScalar
vrrpIfTableMaxSize=_VrrpIfTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,15,9),_VrrpIfTableMaxSize_Type())
vrrpIfTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpIfTableMaxSize.setStatus(_A)
_VrrpVirtRtrGrpTableMaxSize_Type=Integer32
_VrrpVirtRtrGrpTableMaxSize_Object=MibScalar
vrrpVirtRtrGrpTableMaxSize=_VrrpVirtRtrGrpTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,15,10),_VrrpVirtRtrGrpTableMaxSize_Type())
vrrpVirtRtrGrpTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vrrpVirtRtrGrpTableMaxSize.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'iprouting':iprouting,'ipInterfaceTableMax':ipInterfaceTableMax,'ipCurCfgIntfTable':ipCurCfgIntfTable,'ipCurCfgIntfEntry':ipCurCfgIntfEntry,_O:ipCurCfgIntfIndex,'ipCurCfgIntfAddr':ipCurCfgIntfAddr,'ipCurCfgIntfMask':ipCurCfgIntfMask,'ipCurCfgIntfBroadcast':ipCurCfgIntfBroadcast,'ipCurCfgIntfVlan':ipCurCfgIntfVlan,'ipCurCfgIntfState':ipCurCfgIntfState,'ipCurCfgIntfBootpRelay':ipCurCfgIntfBootpRelay,'ipNewCfgIntfTable':ipNewCfgIntfTable,'ipNewCfgIntfEntry':ipNewCfgIntfEntry,_P:ipNewCfgIntfIndex,'ipNewCfgIntfAddr':ipNewCfgIntfAddr,'ipNewCfgIntfMask':ipNewCfgIntfMask,'ipNewCfgIntfBroadcast':ipNewCfgIntfBroadcast,'ipNewCfgIntfVlan':ipNewCfgIntfVlan,'ipNewCfgIntfState':ipNewCfgIntfState,'ipNewCfgIntfDelete':ipNewCfgIntfDelete,'ipNewCfgIntfBootpRelay':ipNewCfgIntfBootpRelay,'ipGatewayTableMax':ipGatewayTableMax,'ipCurCfgGwTable':ipCurCfgGwTable,'ipCurCfgGwEntry':ipCurCfgGwEntry,_Q:ipCurCfgGwIndex,'ipCurCfgGwAddr':ipCurCfgGwAddr,'ipCurCfgGwInterval':ipCurCfgGwInterval,'ipCurCfgGwRetry':ipCurCfgGwRetry,'ipCurCfgGwState':ipCurCfgGwState,'ipCurCfgGwArp':ipCurCfgGwArp,'ipCurCfgGwVlan':ipCurCfgGwVlan,'ipNewCfgGwTable':ipNewCfgGwTable,'ipNewCfgGwEntry':ipNewCfgGwEntry,_R:ipNewCfgGwIndex,'ipNewCfgGwAddr':ipNewCfgGwAddr,'ipNewCfgGwInterval':ipNewCfgGwInterval,'ipNewCfgGwRetry':ipNewCfgGwRetry,'ipNewCfgGwState':ipNewCfgGwState,'ipNewCfgGwDelete':ipNewCfgGwDelete,'ipNewCfgGwArp':ipNewCfgGwArp,'ipNewCfgGwVlan':ipNewCfgGwVlan,'ipCurCfgStaticRouteTable':ipCurCfgStaticRouteTable,'ipCurCfgStaticRouteEntry':ipCurCfgStaticRouteEntry,_S:ipCurCfgStaticRouteIndx,'ipCurCfgStaticRouteDestIp':ipCurCfgStaticRouteDestIp,'ipCurCfgStaticRouteMask':ipCurCfgStaticRouteMask,'ipCurCfgStaticRouteGateway':ipCurCfgStaticRouteGateway,'ipCurCfgStaticRouteInterface':ipCurCfgStaticRouteInterface,'ipNewCfgStaticRouteTable':ipNewCfgStaticRouteTable,'ipNewCfgStaticRouteEntry':ipNewCfgStaticRouteEntry,_T:ipNewCfgStaticRouteIndx,'ipNewCfgStaticRouteDestIp':ipNewCfgStaticRouteDestIp,'ipNewCfgStaticRouteMask':ipNewCfgStaticRouteMask,'ipNewCfgStaticRouteGateway':ipNewCfgStaticRouteGateway,'ipNewCfgStaticRouteAction':ipNewCfgStaticRouteAction,'ipNewCfgStaticRouteInterface':ipNewCfgStaticRouteInterface,'ipForward':ipForward,'ripConfig':ripConfig,'ripCurCfgSupply':ripCurCfgSupply,'ripNewCfgSupply':ripNewCfgSupply,'ripCurCfgListen':ripCurCfgListen,'ripNewCfgListen':ripNewCfgListen,'ripCurCfgDefListen':ripCurCfgDefListen,'ripNewCfgDefListen':ripNewCfgDefListen,'ripCurCfgStaticSupply':ripCurCfgStaticSupply,'ripNewCfgStaticSupply':ripNewCfgStaticSupply,'ripCurCfgUpdatePeriod':ripCurCfgUpdatePeriod,'ripNewCfgUpdatePeriod':ripNewCfgUpdatePeriod,'ripCurCfgState':ripCurCfgState,'ripNewCfgState':ripNewCfgState,'ripCurCfgPoisonReverse':ripCurCfgPoisonReverse,'ripNewCfgPoisonReverse':ripNewCfgPoisonReverse,'ripCurCfgVip':ripCurCfgVip,'ripNewCfgVip':ripNewCfgVip,'ipFwdCurCfgPortTable':ipFwdCurCfgPortTable,'ipFwdCurCfgPortEntry':ipFwdCurCfgPortEntry,_U:ipFwdCurCfgPortIndex,'ipFwdCurCfgPortState':ipFwdCurCfgPortState,'ipFwdNewCfgPortTable':ipFwdNewCfgPortTable,'ipFwdNewCfgPortEntry':ipFwdNewCfgPortEntry,_V:ipFwdNewCfgPortIndex,'ipFwdNewCfgPortState':ipFwdNewCfgPortState,'ipFwdCurCfgState':ipFwdCurCfgState,'ipFwdNewCfgState':ipFwdNewCfgState,'ipFwdCurCfgDirectedBcast':ipFwdCurCfgDirectedBcast,'ipFwdNewCfgDirectedBcast':ipFwdNewCfgDirectedBcast,'ipFwdPortTableMaxSize':ipFwdPortTableMaxSize,'ipFwdLocalTableMaxSize':ipFwdLocalTableMaxSize,'ipFwdCurCfgLocalTable':ipFwdCurCfgLocalTable,'ipFwdCurCfgLocalEntry':ipFwdCurCfgLocalEntry,_W:ipFwdCurCfgLocalIndex,'ipFwdCurCfgLocalSubnet':ipFwdCurCfgLocalSubnet,'ipFwdCurCfgLocalMask':ipFwdCurCfgLocalMask,'ipFwdNewCfgLocalTable':ipFwdNewCfgLocalTable,'ipFwdNewCfgLocalEntry':ipFwdNewCfgLocalEntry,_X:ipFwdNewCfgLocalIndex,'ipFwdNewCfgLocalSubnet':ipFwdNewCfgLocalSubnet,'ipFwdNewCfgLocalMask':ipFwdNewCfgLocalMask,'ipFwdNewCfgLocalDelete':ipFwdNewCfgLocalDelete,'arpCurCfgReARPPeriod':arpCurCfgReARPPeriod,'arpNewCfgReARPPeriod':arpNewCfgReARPPeriod,'ipCurCfgGwMetric':ipCurCfgGwMetric,'ipNewCfgGwMetric':ipNewCfgGwMetric,'ipCurCfgBootpAddr':ipCurCfgBootpAddr,'ipNewCfgBootpAddr':ipNewCfgBootpAddr,'ipCurCfgBootpAddr2':ipCurCfgBootpAddr2,'ipNewCfgBootpAddr2':ipNewCfgBootpAddr2,'ipCurCfgBootpState':ipCurCfgBootpState,'ipNewCfgBootpState':ipNewCfgBootpState,'ipStaticRouteTableMaxSize':ipStaticRouteTableMaxSize,'ospfCfg':ospfCfg,'ospfGeneral':ospfGeneral,'ospfCurCfgDefaultRouteMetric':ospfCurCfgDefaultRouteMetric,'ospfNewCfgDefaultRouteMetric':ospfNewCfgDefaultRouteMetric,'ospfCurCfgDefaultRouteMetricType':ospfCurCfgDefaultRouteMetricType,'ospfNewCfgDefaultRouteMetricType':ospfNewCfgDefaultRouteMetricType,'ospfIntfTableMaxSize':ospfIntfTableMaxSize,'ospfAreaTableMaxSize':ospfAreaTableMaxSize,'ospfRangeTableMaxSize':ospfRangeTableMaxSize,'ospfVirtIntfTableMaxSize':ospfVirtIntfTableMaxSize,'ospfHostTableMaxSize':ospfHostTableMaxSize,'ospfCurCfgAreaTable':ospfCurCfgAreaTable,'ospfCurCfgAreaEntry':ospfCurCfgAreaEntry,_a:ospfCurCfgAreaIndex,_b:ospfCurCfgAreaId,'ospfCurCfgAreaSpfInterval':ospfCurCfgAreaSpfInterval,'ospfCurCfgAreaAuthType':ospfCurCfgAreaAuthType,'ospfNewCfgAreaTable':ospfNewCfgAreaTable,'ospfNewCfgAreaEntry':ospfNewCfgAreaEntry,_d:ospfNewCfgAreaIndex,_e:ospfNewCfgAreaId,'ospfNewCfgAreaSpfInterval':ospfNewCfgAreaSpfInterval,'ospfNewCfgAreaAuthType':ospfNewCfgAreaAuthType,'ripStats':ripStats,'ripStatInPkts':ripStatInPkts,'ripStatOutPkts':ripStatOutPkts,'ripStatInErrorPkts':ripStatInErrorPkts,'ripStatRoutesAgedOut':ripStatRoutesAgedOut,'arpStats':arpStats,'arpStatEntries':arpStatEntries,'arpStatHighWater':arpStatHighWater,'arpStatMaxEntries':arpStatMaxEntries,'routeStats':routeStats,'routeStatEntries':routeStatEntries,'routeStatHighWater':routeStatHighWater,'routeStatMaxEntries':routeStatMaxEntries,'dnsStats':dnsStats,'dnsStatInGoodDnsRequests':dnsStatInGoodDnsRequests,'dnsStatInBadDnsRequests':dnsStatInBadDnsRequests,'vrrpStats':vrrpStats,'vrrpStatInAdvers':vrrpStatInAdvers,'vrrpStatOutAdvers':vrrpStatOutAdvers,'vrrpStatOutBadAdvers':vrrpStatOutBadAdvers,'ospfStats':ospfStats,'ospfGeneralStats':ospfGeneralStats,'ospfCumRxTxStats':ospfCumRxTxStats,'ospfCumRxPkts':ospfCumRxPkts,'ospfCumTxPkts':ospfCumTxPkts,'ospfCumRxHello':ospfCumRxHello,'ospfCumTxHello':ospfCumTxHello,'ospfCumRxDatabase':ospfCumRxDatabase,'ospfCumTxDatabase':ospfCumTxDatabase,'ospfCumRxlsReqs':ospfCumRxlsReqs,'ospfCumTxlsReqs':ospfCumTxlsReqs,'ospfCumRxlsAcks':ospfCumRxlsAcks,'ospfCumTxlsAcks':ospfCumTxlsAcks,'ospfCumRxlsUpdates':ospfCumRxlsUpdates,'ospfCumTxlsUpdates':ospfCumTxlsUpdates,'ospfCumNbrChangeStats':ospfCumNbrChangeStats,'ospfCumNbrhello':ospfCumNbrhello,'ospfCumNbrStart':ospfCumNbrStart,'ospfCumNbrAdjointOk':ospfCumNbrAdjointOk,'ospfCumNbrNegotiationDone':ospfCumNbrNegotiationDone,'ospfCumNbrExchangeDone':ospfCumNbrExchangeDone,'ospfCumNbrBadRequests':ospfCumNbrBadRequests,'ospfCumNbrBadSequence':ospfCumNbrBadSequence,'ospfCumNbrLoadingDone':ospfCumNbrLoadingDone,'ospfCumNbrN1way':ospfCumNbrN1way,'ospfCumNbrRstAd':ospfCumNbrRstAd,'ospfCumNbrDown':ospfCumNbrDown,'ospfCumIntfChangeStats':ospfCumIntfChangeStats,'ospfCumIntfHello':ospfCumIntfHello,'ospfCumIntfDown':ospfCumIntfDown,'ospfCumIntfLoop':ospfCumIntfLoop,'ospfCumIntfUnloop':ospfCumIntfUnloop,'ospfCumIntfWaitTimer':ospfCumIntfWaitTimer,'ospfCumIntfBackup':ospfCumIntfBackup,'ospfCumIntfNbrChange':ospfCumIntfNbrChange,'ospfTimersKickOffStats':ospfTimersKickOffStats,'ospfTmrsKckOffHello':ospfTmrsKckOffHello,'ospfTmrsKckOffRetransmit':ospfTmrsKckOffRetransmit,'ospfTmrsKckOffLsaLock':ospfTmrsKckOffLsaLock,'ospfTmrsKckOffLsaAck':ospfTmrsKckOffLsaAck,'ospfTmrsKckOffDbage':ospfTmrsKckOffDbage,'ospfTmrsKckOffSummary':ospfTmrsKckOffSummary,'ospfTmrsKckOffAseExport':ospfTmrsKckOffAseExport,'ospfArea':ospfArea,'ospfAreaRxTxStats':ospfAreaRxTxStats,'ospfAreaRxTxStatsEntry':ospfAreaRxTxStatsEntry,_f:ospfAreaRxTxIndex,'ospfAreaRxPkts':ospfAreaRxPkts,'ospfAreaTxPkts':ospfAreaTxPkts,'ospfAreaRxHello':ospfAreaRxHello,'ospfAreaTxHello':ospfAreaTxHello,'ospfAreaRxDatabase':ospfAreaRxDatabase,'ospfAreaTxDatabase':ospfAreaTxDatabase,'ospfAreaRxlsReqs':ospfAreaRxlsReqs,'ospfAreaTxlsReqs':ospfAreaTxlsReqs,'ospfAreaRxlsAcks':ospfAreaRxlsAcks,'ospfAreaTxlsAcks':ospfAreaTxlsAcks,'ospfAreaRxlsUpdates':ospfAreaRxlsUpdates,'ospfAreaTxlsUpdates':ospfAreaTxlsUpdates,'ospfAreaNbrChangeStats':ospfAreaNbrChangeStats,'ospfAreaNbrChangeStatsEntry':ospfAreaNbrChangeStatsEntry,_g:ospfAreaNbrIndex,'ospfAreaNbrhello':ospfAreaNbrhello,'ospfAreaNbrStart':ospfAreaNbrStart,'ospfAreaNbrAdjointOk':ospfAreaNbrAdjointOk,'ospfAreaNbrNegotiationDone':ospfAreaNbrNegotiationDone,'ospfAreaNbrExchangeDone':ospfAreaNbrExchangeDone,'ospfAreaNbrBadRequests':ospfAreaNbrBadRequests,'ospfAreaNbrBadSequence':ospfAreaNbrBadSequence,'ospfAreaNbrLoadingDone':ospfAreaNbrLoadingDone,'ospfAreaNbrN1way':ospfAreaNbrN1way,'ospfAreaNbrRstAd':ospfAreaNbrRstAd,'ospfAreaNbrDown':ospfAreaNbrDown,'ospfAreaChangeStats':ospfAreaChangeStats,'ospfAreaChangeStatsEntry':ospfAreaChangeStatsEntry,_h:ospfAreaIntfIndex,'ospfAreaIntfHello':ospfAreaIntfHello,'ospfAreaIntfDown':ospfAreaIntfDown,'ospfAreaIntfLoop':ospfAreaIntfLoop,'ospfAreaIntfUnloop':ospfAreaIntfUnloop,'ospfAreaIntfWaitTimer':ospfAreaIntfWaitTimer,'ospfAreaIntfBackup':ospfAreaIntfBackup,'ospfAreaIntfNbrChange':ospfAreaIntfNbrChange,'ospfInterface':ospfInterface,'ospfIntfRxTxStats':ospfIntfRxTxStats,'ospfIntfRxTxStatsEntry':ospfIntfRxTxStatsEntry,_i:ospfIntfRxTxIndex,'ospfIntfRxPkts':ospfIntfRxPkts,'ospfIntfTxPkts':ospfIntfTxPkts,'ospfIntfRxHello':ospfIntfRxHello,'ospfIntfTxHello':ospfIntfTxHello,'ospfIntfRxDatabase':ospfIntfRxDatabase,'ospfIntfTxDatabase':ospfIntfTxDatabase,'ospfIntfRxlsReqs':ospfIntfRxlsReqs,'ospfIntfTxlsReqs':ospfIntfTxlsReqs,'ospfIntfRxlsAcks':ospfIntfRxlsAcks,'ospfIntfTxlsAcks':ospfIntfTxlsAcks,'ospfIntfRxlsUpdates':ospfIntfRxlsUpdates,'ospfIntfTxlsUpdates':ospfIntfTxlsUpdates,'ospfIntfNbrChangeStats':ospfIntfNbrChangeStats,'ospfIntfNbrChangeStatsEntry':ospfIntfNbrChangeStatsEntry,_j:ospfIntfNbrIndex,'ospfIntfNbrhello':ospfIntfNbrhello,'ospfIntfNbrStart':ospfIntfNbrStart,'ospfIntfNbrAdjointOk':ospfIntfNbrAdjointOk,'ospfIntfNbrNegotiationDone':ospfIntfNbrNegotiationDone,'ospfIntfNbrExchangeDone':ospfIntfNbrExchangeDone,'ospfIntfNbrBadRequests':ospfIntfNbrBadRequests,'ospfIntfNbrBadSequence':ospfIntfNbrBadSequence,'ospfIntfNbrLoadingDone':ospfIntfNbrLoadingDone,'ospfIntfNbrN1way':ospfIntfNbrN1way,'ospfIntfNbrRstAd':ospfIntfNbrRstAd,'ospfIntfNbrDown':ospfIntfNbrDown,'ospfIntfChangeStats':ospfIntfChangeStats,'ospfIntfChangeStatsEntry':ospfIntfChangeStatsEntry,_k:ospfIntfIndex,'ospfIntfHello':ospfIntfHello,'ospfIntfDown':ospfIntfDown,'ospfIntfLoop':ospfIntfLoop,'ospfIntfUnloop':ospfIntfUnloop,'ospfIntfWaitTimer':ospfIntfWaitTimer,'ospfIntfBackup':ospfIntfBackup,'ospfIntfNbrChange':ospfIntfNbrChange,'ip-info':ip_info,'ipRouteInfoTable':ipRouteInfoTable,'ipRouteInfoEntry':ipRouteInfoEntry,_l:ipRouteInfoIndx,'ipRouteInfoDestIp':ipRouteInfoDestIp,'ipRouteInfoMask':ipRouteInfoMask,'ipRouteInfoGateway':ipRouteInfoGateway,'ipRouteInfoTag':ipRouteInfoTag,'ipRouteInfoType':ipRouteInfoType,'ipRouteInfoInterface':ipRouteInfoInterface,'arpInfoTable':arpInfoTable,'arpInfoEntry':arpInfoEntry,_q:arpInfoDestIp,'arpInfoMacAddr':arpInfoMacAddr,'arpInfoVLAN':arpInfoVLAN,'arpInfoSrcPort':arpInfoSrcPort,'arpInfoRefPorts':arpInfoRefPorts,'arpInfoFlag':arpInfoFlag,'vrrp-info':vrrp_info,'vrrpInfoVirtRtrTable':vrrpInfoVirtRtrTable,'vrrpInfoVirtRtrTableEntry':vrrpInfoVirtRtrTableEntry,_r:vrrpInfoVirtRtrIndex,'vrrpInfoVirtRtrState':vrrpInfoVirtRtrState,'vrrpInfoVirtRtrOwnership':vrrpInfoVirtRtrOwnership,'vrrpInfoVirtRtrServer':vrrpInfoVirtRtrServer,'vrrpInfoVirtRtrProxy':vrrpInfoVirtRtrProxy,'ospfinfo':ospfinfo,'ospfGeneralInfo':ospfGeneralInfo,'ospfStartTime':ospfStartTime,'ospfProcessUptime':ospfProcessUptime,'ospfLsTypesSupported':ospfLsTypesSupported,'ospfIntfCountForRouter':ospfIntfCountForRouter,'ospfVlinkCountForRouter':ospfVlinkCountForRouter,'ospfTotalNeighbours':ospfTotalNeighbours,'ospfNbrInInitState':ospfNbrInInitState,'ospfNbrInExchState':ospfNbrInExchState,'ospfNbrInFullState':ospfNbrInFullState,'ospfTotalAreas':ospfTotalAreas,'ospfTotalTransitAreas':ospfTotalTransitAreas,'ospfTotalNssaAreas':ospfTotalNssaAreas,'ospfAreaInfoTable':ospfAreaInfoTable,'ospfAreaInfoEntry':ospfAreaInfoEntry,_s:ospfAreaInfoIndex,'ospfTotalNumberOfInterfaces':ospfTotalNumberOfInterfaces,'ospfNumberOfInterfacesUp':ospfNumberOfInterfacesUp,'ospfNumberOfLsdbEntries':ospfNumberOfLsdbEntries,'ospfAreaInfoId':ospfAreaInfoId,'ospfIntfInfoTable':ospfIntfInfoTable,'ospfIntfInfoEntry':ospfIntfInfoEntry,_t:ospfIfInfoIndex,'ospfIfDesignatedRouterIP':ospfIfDesignatedRouterIP,'ospfIfBackupDesignatedRouterIP':ospfIfBackupDesignatedRouterIP,'ospfIfWaitInterval':ospfIfWaitInterval,'ospfIfTotalNeighbours':ospfIfTotalNeighbours,'ospfIfInfoIpAddress':ospfIfInfoIpAddress,'ospfRouterLSAInfoTable':ospfRouterLSAInfoTable,'ospfRouterLSAInfoEntry':ospfRouterLSAInfoEntry,_u:routerLSAAreaIndex,_v:routerLSALinkIndex,_w:routerLSAId,'routerLSALinkID':routerLSALinkID,'routerLSALinkData':routerLSALinkData,'routerLSALinkIfIndex':routerLSALinkIfIndex,'routerLSANoOfTOSMetrics':routerLSANoOfTOSMetrics,'routerLSANoOfTOSZeroMetrics':routerLSANoOfTOSZeroMetrics,'vrrpOper':vrrpOper,'vrrpOperVirtRtrTable':vrrpOperVirtRtrTable,'vrrpOperVirtRtrEntry':vrrpOperVirtRtrEntry,_x:vrrpOperVirtRtrIndex,'vrrpOperVirtRtrBackup':vrrpOperVirtRtrBackup,'vrrpOperVirtRtrGroupBackup':vrrpOperVirtRtrGroupBackup,'vrrp':vrrp,'vrrpGeneral':vrrpGeneral,'vrrpCurCfgGenState':vrrpCurCfgGenState,'vrrpNewCfgGenState':vrrpNewCfgGenState,'vrrpCurCfgGenTckVirtRtrInc':vrrpCurCfgGenTckVirtRtrInc,'vrrpNewCfgGenTckVirtRtrInc':vrrpNewCfgGenTckVirtRtrInc,'vrrpCurCfgGenTckIpIntfInc':vrrpCurCfgGenTckIpIntfInc,'vrrpNewCfgGenTckIpIntfInc':vrrpNewCfgGenTckIpIntfInc,'vrrpCurCfgGenTckVlanPortInc':vrrpCurCfgGenTckVlanPortInc,'vrrpNewCfgGenTckVlanPortInc':vrrpNewCfgGenTckVlanPortInc,'vrrpCurCfgGenTckL4PortInc':vrrpCurCfgGenTckL4PortInc,'vrrpNewCfgGenTckL4PortInc':vrrpNewCfgGenTckL4PortInc,'vrrpCurCfgGenTckRServerInc':vrrpCurCfgGenTckRServerInc,'vrrpNewCfgGenTckRServerInc':vrrpNewCfgGenTckRServerInc,'vrrpCurCfgGenTckHsrpInc':vrrpCurCfgGenTckHsrpInc,'vrrpNewCfgGenTckHsrpInc':vrrpNewCfgGenTckHsrpInc,'vrrpCurCfgGenHotstandby':vrrpCurCfgGenHotstandby,'vrrpNewCfgGenHotstandby':vrrpNewCfgGenHotstandby,'vrrpCurCfgGenTckHsrvInc':vrrpCurCfgGenTckHsrvInc,'vrrpNewCfgGenTckHsrvInc':vrrpNewCfgGenTckHsrvInc,'vrrpCurCfgVirtRtrTable':vrrpCurCfgVirtRtrTable,'vrrpCurCfgVirtRtrTableEntry':vrrpCurCfgVirtRtrTableEntry,_y:vrrpCurCfgVirtRtrIndx,'vrrpCurCfgVirtRtrID':vrrpCurCfgVirtRtrID,'vrrpCurCfgVirtRtrAddr':vrrpCurCfgVirtRtrAddr,'vrrpCurCfgVirtRtrIfIndex':vrrpCurCfgVirtRtrIfIndex,'vrrpCurCfgVirtRtrInterval':vrrpCurCfgVirtRtrInterval,'vrrpCurCfgVirtRtrPriority':vrrpCurCfgVirtRtrPriority,'vrrpCurCfgVirtRtrPreempt':vrrpCurCfgVirtRtrPreempt,'vrrpCurCfgVirtRtrState':vrrpCurCfgVirtRtrState,'vrrpCurCfgVirtRtrSharing':vrrpCurCfgVirtRtrSharing,'vrrpCurCfgVirtRtrTckVirtRtr':vrrpCurCfgVirtRtrTckVirtRtr,'vrrpCurCfgVirtRtrTckIpIntf':vrrpCurCfgVirtRtrTckIpIntf,'vrrpCurCfgVirtRtrTckVlanPort':vrrpCurCfgVirtRtrTckVlanPort,'vrrpCurCfgVirtRtrTckL4Port':vrrpCurCfgVirtRtrTckL4Port,'vrrpCurCfgVirtRtrTckRServer':vrrpCurCfgVirtRtrTckRServer,'vrrpCurCfgVirtRtrTckHsrp':vrrpCurCfgVirtRtrTckHsrp,'vrrpCurCfgVirtRtrTckHsrv':vrrpCurCfgVirtRtrTckHsrv,'vrrpNewCfgVirtRtrTable':vrrpNewCfgVirtRtrTable,'vrrpNewCfgVirtRtrTableEntry':vrrpNewCfgVirtRtrTableEntry,_z:vrrpNewCfgVirtRtrIndx,'vrrpNewCfgVirtRtrID':vrrpNewCfgVirtRtrID,'vrrpNewCfgVirtRtrAddr':vrrpNewCfgVirtRtrAddr,'vrrpNewCfgVirtRtrIfIndex':vrrpNewCfgVirtRtrIfIndex,'vrrpNewCfgVirtRtrInterval':vrrpNewCfgVirtRtrInterval,'vrrpNewCfgVirtRtrPriority':vrrpNewCfgVirtRtrPriority,'vrrpNewCfgVirtRtrPreempt':vrrpNewCfgVirtRtrPreempt,'vrrpNewCfgVirtRtrState':vrrpNewCfgVirtRtrState,'vrrpNewCfgVirtRtrDelete':vrrpNewCfgVirtRtrDelete,'vrrpNewCfgVirtRtrSharing':vrrpNewCfgVirtRtrSharing,'vrrpNewCfgVirtRtrTckVirtRtr':vrrpNewCfgVirtRtrTckVirtRtr,'vrrpNewCfgVirtRtrTckIpIntf':vrrpNewCfgVirtRtrTckIpIntf,'vrrpNewCfgVirtRtrTckVlanPort':vrrpNewCfgVirtRtrTckVlanPort,'vrrpNewCfgVirtRtrTckL4Port':vrrpNewCfgVirtRtrTckL4Port,'vrrpNewCfgVirtRtrTckRServer':vrrpNewCfgVirtRtrTckRServer,'vrrpNewCfgVirtRtrTckHsrp':vrrpNewCfgVirtRtrTckHsrp,'vrrpNewCfgVirtRtrTckHsrv':vrrpNewCfgVirtRtrTckHsrv,'vrrpCurCfgIfTable':vrrpCurCfgIfTable,'vrrpCurCfgIfTableEntry':vrrpCurCfgIfTableEntry,_A0:vrrpCurCfgIfIndx,'vrrpCurCfgIfAuthType':vrrpCurCfgIfAuthType,'vrrpCurCfgIfPasswd':vrrpCurCfgIfPasswd,'vrrpNewCfgIfTable':vrrpNewCfgIfTable,'vrrpNewCfgIfTableEntry':vrrpNewCfgIfTableEntry,_A2:vrrpNewCfgIfIndx,'vrrpNewCfgIfAuthType':vrrpNewCfgIfAuthType,'vrrpNewCfgIfPasswd':vrrpNewCfgIfPasswd,'vrrpNewCfgIfDelete':vrrpNewCfgIfDelete,'vrrpCurCfgVirtRtrGrpTable':vrrpCurCfgVirtRtrGrpTable,'vrrpCurCfgVirtRtrGrpTableEntry':vrrpCurCfgVirtRtrGrpTableEntry,_A3:vrrpCurCfgVirtRtrGrpIndx,'vrrpCurCfgVirtRtrGrpID':vrrpCurCfgVirtRtrGrpID,'vrrpCurCfgVirtRtrGrpIfIndex':vrrpCurCfgVirtRtrGrpIfIndex,'vrrpCurCfgVirtRtrGrpInterval':vrrpCurCfgVirtRtrGrpInterval,'vrrpCurCfgVirtRtrGrpPriority':vrrpCurCfgVirtRtrGrpPriority,'vrrpCurCfgVirtRtrGrpPreempt':vrrpCurCfgVirtRtrGrpPreempt,'vrrpCurCfgVirtRtrGrpState':vrrpCurCfgVirtRtrGrpState,'vrrpCurCfgVirtRtrGrpSharing':vrrpCurCfgVirtRtrGrpSharing,'vrrpCurCfgVirtRtrGrpTckVirtRtr':vrrpCurCfgVirtRtrGrpTckVirtRtr,'vrrpCurCfgVirtRtrGrpTckIpIntf':vrrpCurCfgVirtRtrGrpTckIpIntf,'vrrpCurCfgVirtRtrGrpTckVlanPort':vrrpCurCfgVirtRtrGrpTckVlanPort,'vrrpCurCfgVirtRtrGrpTckL4Port':vrrpCurCfgVirtRtrGrpTckL4Port,'vrrpCurCfgVirtRtrGrpTckRServer':vrrpCurCfgVirtRtrGrpTckRServer,'vrrpCurCfgVirtRtrGrpTckHsrp':vrrpCurCfgVirtRtrGrpTckHsrp,'vrrpCurCfgVirtRtrGrpTckHsrv':vrrpCurCfgVirtRtrGrpTckHsrv,'vrrpNewCfgVirtRtrGrpTable':vrrpNewCfgVirtRtrGrpTable,'vrrpNewCfgVirtRtrGrpTableEntry':vrrpNewCfgVirtRtrGrpTableEntry,_A4:vrrpNewCfgVirtRtrGrpIndx,'vrrpNewCfgVirtRtrGrpID':vrrpNewCfgVirtRtrGrpID,'vrrpNewCfgVirtRtrGrpIfIndex':vrrpNewCfgVirtRtrGrpIfIndex,'vrrpNewCfgVirtRtrGrpInterval':vrrpNewCfgVirtRtrGrpInterval,'vrrpNewCfgVirtRtrGrpPriority':vrrpNewCfgVirtRtrGrpPriority,'vrrpNewCfgVirtRtrGrpPreempt':vrrpNewCfgVirtRtrGrpPreempt,'vrrpNewCfgVirtRtrGrpState':vrrpNewCfgVirtRtrGrpState,'vrrpNewCfgVirtRtrGrpDelete':vrrpNewCfgVirtRtrGrpDelete,'vrrpNewCfgVirtRtrGrpSharing':vrrpNewCfgVirtRtrGrpSharing,'vrrpNewCfgVirtRtrGrpTckVirtRtr':vrrpNewCfgVirtRtrGrpTckVirtRtr,'vrrpNewCfgVirtRtrGrpTckIpIntf':vrrpNewCfgVirtRtrGrpTckIpIntf,'vrrpNewCfgVirtRtrGrpTckVlanPort':vrrpNewCfgVirtRtrGrpTckVlanPort,'vrrpNewCfgVirtRtrGrpTckL4Port':vrrpNewCfgVirtRtrGrpTckL4Port,'vrrpNewCfgVirtRtrGrpTckRServer':vrrpNewCfgVirtRtrGrpTckRServer,'vrrpNewCfgVirtRtrGrpTckHsrp':vrrpNewCfgVirtRtrGrpTckHsrp,'vrrpNewCfgVirtRtrGrpTckHsrv':vrrpNewCfgVirtRtrGrpTckHsrv,'vrrpVirtRtrTableMaxSize':vrrpVirtRtrTableMaxSize,'vrrpIfTableMaxSize':vrrpIfTableMaxSize,'vrrpVirtRtrGrpTableMaxSize':vrrpVirtRtrGrpTableMaxSize})