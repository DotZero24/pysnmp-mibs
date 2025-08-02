_AJ='agentOspfVirtIfEntry'
_AI='agentOspfIfEntry'
_AH='agentRip2IfConfEntry'
_AG='agentIsisConfigIfIndex'
_AF='agentIsisRouteRedistSource'
_AE='agentSwitchInternalVlanId'
_AD='agentSwitchIpHelperUdpPort'
_AC='agentSwitchIpHelperAddress'
_AB='agentRouterVrrpTrackRtPfxLen'
_AA='agentRouterVrrpTrackRtPfx'
_A9='agentRouterVrrpTrackIntf'
_A8='agentOspfNetworkAreaId'
_A7='agentOspfNetworkAreaWildcardMask'
_A6='agentOspfNetworkAreaIpAddress'
_A5='agentOspfAsLsdbRouterId'
_A4='agentOspfAsLsdbLsid'
_A3='agentOspfAsLsdbType'
_A2='agentOspfLocalLsdbRouterId'
_A1='agentOspfLocalLsdbLsid'
_A0='agentOspfLocalLsdbType'
_z='agentOspfLocalLsdbAddressLessIf'
_y='agentOspfLocalLsdbIpAddress'
_x='agentOspfAreaOpaqueLsdbRouterId'
_w='agentOspfAreaOpaqueLsdbLsid'
_v='agentOspfAreaOpaqueLsdbType'
_u='agentOspfAreaOpaqueLsdbAreaId'
_t='AutoCostRefBw'
_s='agentOspfRouteRedistSource'
_r='externalType2'
_q='externalType1'
_p='agentRipRouteRedistSource'
_o='agentSwitchIntfIpHelperIpAddress'
_n='agentSwitchIntfIpHelperUdpPort'
_m='agentSwitchHelperIpAddress'
_l='agentSwitchSecondaryIpAddress'
_k='agentSwitchIpVlanId'
_j='agentSwitchIpRouterDiscoveryIfIndex'
_i='agentSwitchIntfArpIfIndex'
_h='agentSwitchIntfArpIpAddress'
_g='dynamic'
_f='gateway'
_e='agentSwitchArpIpAddress'
_d='IpAddress'
_c='validate'
_b='sendOnly'
_a='agentRouterIsisConfigAreaIndex'
_Z='seconds'
_Y='SpfTimerRange'
_X='connected'
_W='agentSwitchIpInterfaceIfIndex'
_V='static'
_U='vrrpOperVrId'
_T='VRRP-MIB'
_S='none'
_R='ifIndex'
_Q='IF-MIB'
_P='not-accessible'
_O='not-applicable'
_N='false'
_M='true'
_L='TruthValue'
_K='OctetString'
_J='Unsigned32'
_I='read-create'
_H='disable'
_G='enable'
_F='obsolete'
_E='ROUTING-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_Q,'InterfaceIndex','InterfaceIndexOrZero',_R)
RouterID,ospfAreaEntry,ospfIfEntry,ospfVirtIfEntry=mibBuilder.importSymbols('OSPF-MIB','RouterID','ospfAreaEntry','ospfIfEntry','ospfVirtIfEntry')
quanta,switch=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','quanta','switch')
rip2IfConfEntry,=mibBuilder.importSymbols('RIPv2-MIB','rip2IfConfEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_d,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
vrrpOperVrId,=mibBuilder.importSymbols(_T,_U)
routing=ModuleIdentity((1,3,6,1,4,1,7244,2,2))
class SpfTimerRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class AutoCostRefBw(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967))
_AgentSwitchArpGroup_ObjectIdentity=ObjectIdentity
agentSwitchArpGroup=_AgentSwitchArpGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,1))
class _AgentSwitchArpAgeoutTime_Type(Integer32):defaultValue=1200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,21600))
_AgentSwitchArpAgeoutTime_Type.__name__=_C
_AgentSwitchArpAgeoutTime_Object=MibScalar
agentSwitchArpAgeoutTime=_AgentSwitchArpAgeoutTime_Object((1,3,6,1,4,1,7244,2,2,1,1),_AgentSwitchArpAgeoutTime_Type())
agentSwitchArpAgeoutTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpAgeoutTime.setStatus(_A)
class _AgentSwitchArpResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AgentSwitchArpResponseTime_Type.__name__=_C
_AgentSwitchArpResponseTime_Object=MibScalar
agentSwitchArpResponseTime=_AgentSwitchArpResponseTime_Object((1,3,6,1,4,1,7244,2,2,1,2),_AgentSwitchArpResponseTime_Type())
agentSwitchArpResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpResponseTime.setStatus(_A)
class _AgentSwitchArpMaxRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AgentSwitchArpMaxRetries_Type.__name__=_C
_AgentSwitchArpMaxRetries_Object=MibScalar
agentSwitchArpMaxRetries=_AgentSwitchArpMaxRetries_Object((1,3,6,1,4,1,7244,2,2,1,3),_AgentSwitchArpMaxRetries_Type())
agentSwitchArpMaxRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpMaxRetries.setStatus(_A)
_AgentSwitchArpCacheSize_Type=Integer32
_AgentSwitchArpCacheSize_Object=MibScalar
agentSwitchArpCacheSize=_AgentSwitchArpCacheSize_Object((1,3,6,1,4,1,7244,2,2,1,4),_AgentSwitchArpCacheSize_Type())
agentSwitchArpCacheSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpCacheSize.setStatus(_A)
class _AgentSwitchArpDynamicRenew_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchArpDynamicRenew_Type.__name__=_C
_AgentSwitchArpDynamicRenew_Object=MibScalar
agentSwitchArpDynamicRenew=_AgentSwitchArpDynamicRenew_Object((1,3,6,1,4,1,7244,2,2,1,5),_AgentSwitchArpDynamicRenew_Type())
agentSwitchArpDynamicRenew.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpDynamicRenew.setStatus(_A)
_AgentSwitchArpTotalEntryCountCurrent_Type=Gauge32
_AgentSwitchArpTotalEntryCountCurrent_Object=MibScalar
agentSwitchArpTotalEntryCountCurrent=_AgentSwitchArpTotalEntryCountCurrent_Object((1,3,6,1,4,1,7244,2,2,1,6),_AgentSwitchArpTotalEntryCountCurrent_Type())
agentSwitchArpTotalEntryCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchArpTotalEntryCountCurrent.setStatus(_A)
_AgentSwitchArpTotalEntryCountPeak_Type=Gauge32
_AgentSwitchArpTotalEntryCountPeak_Object=MibScalar
agentSwitchArpTotalEntryCountPeak=_AgentSwitchArpTotalEntryCountPeak_Object((1,3,6,1,4,1,7244,2,2,1,7),_AgentSwitchArpTotalEntryCountPeak_Type())
agentSwitchArpTotalEntryCountPeak.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchArpTotalEntryCountPeak.setStatus(_A)
_AgentSwitchArpStaticEntryCountCurrent_Type=Gauge32
_AgentSwitchArpStaticEntryCountCurrent_Object=MibScalar
agentSwitchArpStaticEntryCountCurrent=_AgentSwitchArpStaticEntryCountCurrent_Object((1,3,6,1,4,1,7244,2,2,1,8),_AgentSwitchArpStaticEntryCountCurrent_Type())
agentSwitchArpStaticEntryCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchArpStaticEntryCountCurrent.setStatus(_A)
_AgentSwitchArpStaticEntryCountMax_Type=Integer32
_AgentSwitchArpStaticEntryCountMax_Object=MibScalar
agentSwitchArpStaticEntryCountMax=_AgentSwitchArpStaticEntryCountMax_Object((1,3,6,1,4,1,7244,2,2,1,9),_AgentSwitchArpStaticEntryCountMax_Type())
agentSwitchArpStaticEntryCountMax.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchArpStaticEntryCountMax.setStatus(_A)
_AgentSwitchArpTable_Object=MibTable
agentSwitchArpTable=_AgentSwitchArpTable_Object((1,3,6,1,4,1,7244,2,2,1,10))
if mibBuilder.loadTexts:agentSwitchArpTable.setStatus(_F)
_AgentSwitchArpEntry_Object=MibTableRow
agentSwitchArpEntry=_AgentSwitchArpEntry_Object((1,3,6,1,4,1,7244,2,2,1,10,1))
agentSwitchArpEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:agentSwitchArpEntry.setStatus(_F)
_AgentSwitchArpAge_Type=TimeTicks
_AgentSwitchArpAge_Object=MibTableColumn
agentSwitchArpAge=_AgentSwitchArpAge_Object((1,3,6,1,4,1,7244,2,2,1,10,1,1),_AgentSwitchArpAge_Type())
agentSwitchArpAge.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchArpAge.setStatus(_F)
_AgentSwitchArpIpAddress_Type=IpAddress
_AgentSwitchArpIpAddress_Object=MibTableColumn
agentSwitchArpIpAddress=_AgentSwitchArpIpAddress_Object((1,3,6,1,4,1,7244,2,2,1,10,1,2),_AgentSwitchArpIpAddress_Type())
agentSwitchArpIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchArpIpAddress.setStatus(_F)
_AgentSwitchArpMacAddress_Type=PhysAddress
_AgentSwitchArpMacAddress_Object=MibTableColumn
agentSwitchArpMacAddress=_AgentSwitchArpMacAddress_Object((1,3,6,1,4,1,7244,2,2,1,10,1,3),_AgentSwitchArpMacAddress_Type())
agentSwitchArpMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchArpMacAddress.setStatus(_F)
_AgentSwitchArpInterface_Type=Integer32
_AgentSwitchArpInterface_Object=MibTableColumn
agentSwitchArpInterface=_AgentSwitchArpInterface_Object((1,3,6,1,4,1,7244,2,2,1,10,1,4),_AgentSwitchArpInterface_Type())
agentSwitchArpInterface.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchArpInterface.setStatus(_F)
class _AgentSwitchArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_f,2),(_V,3),(_g,4)))
_AgentSwitchArpType_Type.__name__=_C
_AgentSwitchArpType_Object=MibTableColumn
agentSwitchArpType=_AgentSwitchArpType_Object((1,3,6,1,4,1,7244,2,2,1,10,1,5),_AgentSwitchArpType_Type())
agentSwitchArpType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchArpType.setStatus(_F)
_AgentSwitchArpStatus_Type=RowStatus
_AgentSwitchArpStatus_Object=MibTableColumn
agentSwitchArpStatus=_AgentSwitchArpStatus_Object((1,3,6,1,4,1,7244,2,2,1,10,1,6),_AgentSwitchArpStatus_Type())
agentSwitchArpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpStatus.setStatus(_F)
_AgentSwitchLocalProxyArpTable_Object=MibTable
agentSwitchLocalProxyArpTable=_AgentSwitchLocalProxyArpTable_Object((1,3,6,1,4,1,7244,2,2,1,11))
if mibBuilder.loadTexts:agentSwitchLocalProxyArpTable.setStatus(_A)
_AgentSwitchLocalProxyArpEntry_Object=MibTableRow
agentSwitchLocalProxyArpEntry=_AgentSwitchLocalProxyArpEntry_Object((1,3,6,1,4,1,7244,2,2,1,11,1))
agentSwitchLocalProxyArpEntry.setIndexNames((0,_Q,_R))
if mibBuilder.loadTexts:agentSwitchLocalProxyArpEntry.setStatus(_A)
class _AgentSwitchLocalProxyArpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchLocalProxyArpMode_Type.__name__=_C
_AgentSwitchLocalProxyArpMode_Object=MibTableColumn
agentSwitchLocalProxyArpMode=_AgentSwitchLocalProxyArpMode_Object((1,3,6,1,4,1,7244,2,2,1,11,1,1),_AgentSwitchLocalProxyArpMode_Type())
agentSwitchLocalProxyArpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchLocalProxyArpMode.setStatus(_A)
_AgentSwitchIntfArpTable_Object=MibTable
agentSwitchIntfArpTable=_AgentSwitchIntfArpTable_Object((1,3,6,1,4,1,7244,2,2,1,12))
if mibBuilder.loadTexts:agentSwitchIntfArpTable.setStatus(_A)
_AgentSwitchIntfArpEntry_Object=MibTableRow
agentSwitchIntfArpEntry=_AgentSwitchIntfArpEntry_Object((1,3,6,1,4,1,7244,2,2,1,12,1))
agentSwitchIntfArpEntry.setIndexNames((0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:agentSwitchIntfArpEntry.setStatus(_A)
_AgentSwitchIntfArpIpAddress_Type=IpAddress
_AgentSwitchIntfArpIpAddress_Object=MibTableColumn
agentSwitchIntfArpIpAddress=_AgentSwitchIntfArpIpAddress_Object((1,3,6,1,4,1,7244,2,2,1,12,1,1),_AgentSwitchIntfArpIpAddress_Type())
agentSwitchIntfArpIpAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:agentSwitchIntfArpIpAddress.setStatus(_A)
_AgentSwitchIntfArpIfIndex_Type=InterfaceIndex
_AgentSwitchIntfArpIfIndex_Object=MibTableColumn
agentSwitchIntfArpIfIndex=_AgentSwitchIntfArpIfIndex_Object((1,3,6,1,4,1,7244,2,2,1,12,1,2),_AgentSwitchIntfArpIfIndex_Type())
agentSwitchIntfArpIfIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:agentSwitchIntfArpIfIndex.setStatus(_A)
_AgentSwitchIntfArpAge_Type=TimeTicks
_AgentSwitchIntfArpAge_Object=MibTableColumn
agentSwitchIntfArpAge=_AgentSwitchIntfArpAge_Object((1,3,6,1,4,1,7244,2,2,1,12,1,3),_AgentSwitchIntfArpAge_Type())
agentSwitchIntfArpAge.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchIntfArpAge.setStatus(_A)
_AgentSwitchIntfArpMacAddress_Type=PhysAddress
_AgentSwitchIntfArpMacAddress_Object=MibTableColumn
agentSwitchIntfArpMacAddress=_AgentSwitchIntfArpMacAddress_Object((1,3,6,1,4,1,7244,2,2,1,12,1,4),_AgentSwitchIntfArpMacAddress_Type())
agentSwitchIntfArpMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIntfArpMacAddress.setStatus(_A)
class _AgentSwitchIntfArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_f,2),(_V,3),(_g,4)))
_AgentSwitchIntfArpType_Type.__name__=_C
_AgentSwitchIntfArpType_Object=MibTableColumn
agentSwitchIntfArpType=_AgentSwitchIntfArpType_Object((1,3,6,1,4,1,7244,2,2,1,12,1,5),_AgentSwitchIntfArpType_Type())
agentSwitchIntfArpType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchIntfArpType.setStatus(_A)
_AgentSwitchIntfArpStatus_Type=RowStatus
_AgentSwitchIntfArpStatus_Object=MibTableColumn
agentSwitchIntfArpStatus=_AgentSwitchIntfArpStatus_Object((1,3,6,1,4,1,7244,2,2,1,12,1,6),_AgentSwitchIntfArpStatus_Type())
agentSwitchIntfArpStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIntfArpStatus.setStatus(_A)
_AgentSwitchIpGroup_ObjectIdentity=ObjectIdentity
agentSwitchIpGroup=_AgentSwitchIpGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,2))
class _AgentSwitchIpRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpRoutingMode_Type.__name__=_C
_AgentSwitchIpRoutingMode_Object=MibScalar
agentSwitchIpRoutingMode=_AgentSwitchIpRoutingMode_Object((1,3,6,1,4,1,7244,2,2,2,1),_AgentSwitchIpRoutingMode_Type())
agentSwitchIpRoutingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpRoutingMode.setStatus(_A)
_AgentSwitchIpDefaultGateway_Type=IpAddress
_AgentSwitchIpDefaultGateway_Object=MibScalar
agentSwitchIpDefaultGateway=_AgentSwitchIpDefaultGateway_Object((1,3,6,1,4,1,7244,2,2,2,2),_AgentSwitchIpDefaultGateway_Type())
agentSwitchIpDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpDefaultGateway.setStatus(_A)
_AgentSwitchIpInterfaceTable_Object=MibTable
agentSwitchIpInterfaceTable=_AgentSwitchIpInterfaceTable_Object((1,3,6,1,4,1,7244,2,2,2,3))
if mibBuilder.loadTexts:agentSwitchIpInterfaceTable.setStatus(_A)
_AgentSwitchIpInterfaceEntry_Object=MibTableRow
agentSwitchIpInterfaceEntry=_AgentSwitchIpInterfaceEntry_Object((1,3,6,1,4,1,7244,2,2,2,3,1))
agentSwitchIpInterfaceEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:agentSwitchIpInterfaceEntry.setStatus(_A)
class _AgentSwitchIpInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpInterfaceIfIndex_Type.__name__=_C
_AgentSwitchIpInterfaceIfIndex_Object=MibTableColumn
agentSwitchIpInterfaceIfIndex=_AgentSwitchIpInterfaceIfIndex_Object((1,3,6,1,4,1,7244,2,2,2,3,1,1),_AgentSwitchIpInterfaceIfIndex_Type())
agentSwitchIpInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIfIndex.setStatus(_A)
_AgentSwitchIpInterfaceIpAddress_Type=IpAddress
_AgentSwitchIpInterfaceIpAddress_Object=MibTableColumn
agentSwitchIpInterfaceIpAddress=_AgentSwitchIpInterfaceIpAddress_Object((1,3,6,1,4,1,7244,2,2,2,3,1,2),_AgentSwitchIpInterfaceIpAddress_Type())
agentSwitchIpInterfaceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIpAddress.setStatus(_A)
_AgentSwitchIpInterfaceNetMask_Type=IpAddress
_AgentSwitchIpInterfaceNetMask_Object=MibTableColumn
agentSwitchIpInterfaceNetMask=_AgentSwitchIpInterfaceNetMask_Object((1,3,6,1,4,1,7244,2,2,2,3,1,3),_AgentSwitchIpInterfaceNetMask_Type())
agentSwitchIpInterfaceNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceNetMask.setStatus(_A)
class _AgentSwitchIpInterfaceClearIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpInterfaceClearIp_Type.__name__=_C
_AgentSwitchIpInterfaceClearIp_Object=MibTableColumn
agentSwitchIpInterfaceClearIp=_AgentSwitchIpInterfaceClearIp_Object((1,3,6,1,4,1,7244,2,2,2,3,1,4),_AgentSwitchIpInterfaceClearIp_Type())
agentSwitchIpInterfaceClearIp.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceClearIp.setStatus(_A)
class _AgentSwitchIpInterfaceRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpInterfaceRoutingMode_Type.__name__=_C
_AgentSwitchIpInterfaceRoutingMode_Object=MibTableColumn
agentSwitchIpInterfaceRoutingMode=_AgentSwitchIpInterfaceRoutingMode_Object((1,3,6,1,4,1,7244,2,2,2,3,1,5),_AgentSwitchIpInterfaceRoutingMode_Type())
agentSwitchIpInterfaceRoutingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceRoutingMode.setStatus(_A)
class _AgentSwitchIpInterfaceProxyARPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpInterfaceProxyARPMode_Type.__name__=_C
_AgentSwitchIpInterfaceProxyARPMode_Object=MibTableColumn
agentSwitchIpInterfaceProxyARPMode=_AgentSwitchIpInterfaceProxyARPMode_Object((1,3,6,1,4,1,7244,2,2,2,3,1,6),_AgentSwitchIpInterfaceProxyARPMode_Type())
agentSwitchIpInterfaceProxyARPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceProxyARPMode.setStatus(_A)
class _AgentSwitchIpInterfaceMtuValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(68,12270))
_AgentSwitchIpInterfaceMtuValue_Type.__name__=_J
_AgentSwitchIpInterfaceMtuValue_Object=MibTableColumn
agentSwitchIpInterfaceMtuValue=_AgentSwitchIpInterfaceMtuValue_Object((1,3,6,1,4,1,7244,2,2,2,3,1,7),_AgentSwitchIpInterfaceMtuValue_Type())
agentSwitchIpInterfaceMtuValue.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceMtuValue.setStatus(_A)
class _AgentSwitchIpInterfaceBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,10000000))
_AgentSwitchIpInterfaceBandwidth_Type.__name__=_J
_AgentSwitchIpInterfaceBandwidth_Object=MibTableColumn
agentSwitchIpInterfaceBandwidth=_AgentSwitchIpInterfaceBandwidth_Object((1,3,6,1,4,1,7244,2,2,2,3,1,8),_AgentSwitchIpInterfaceBandwidth_Type())
agentSwitchIpInterfaceBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceBandwidth.setStatus(_A)
_AgentSwitchIpInterfaceUnnumberedIfIndex_Type=InterfaceIndexOrZero
_AgentSwitchIpInterfaceUnnumberedIfIndex_Object=MibTableColumn
agentSwitchIpInterfaceUnnumberedIfIndex=_AgentSwitchIpInterfaceUnnumberedIfIndex_Object((1,3,6,1,4,1,7244,2,2,2,3,1,9),_AgentSwitchIpInterfaceUnnumberedIfIndex_Type())
agentSwitchIpInterfaceUnnumberedIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchIpInterfaceUnnumberedIfIndex.setStatus(_A)
class _AgentSwitchIpInterfaceIcmpUnreachables_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpInterfaceIcmpUnreachables_Type.__name__=_C
_AgentSwitchIpInterfaceIcmpUnreachables_Object=MibTableColumn
agentSwitchIpInterfaceIcmpUnreachables=_AgentSwitchIpInterfaceIcmpUnreachables_Object((1,3,6,1,4,1,7244,2,2,2,3,1,10),_AgentSwitchIpInterfaceIcmpUnreachables_Type())
agentSwitchIpInterfaceIcmpUnreachables.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIcmpUnreachables.setStatus(_A)
class _AgentSwitchIpInterfaceIcmpRedirects_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpInterfaceIcmpRedirects_Type.__name__=_C
_AgentSwitchIpInterfaceIcmpRedirects_Object=MibTableColumn
agentSwitchIpInterfaceIcmpRedirects=_AgentSwitchIpInterfaceIcmpRedirects_Object((1,3,6,1,4,1,7244,2,2,2,3,1,11),_AgentSwitchIpInterfaceIcmpRedirects_Type())
agentSwitchIpInterfaceIcmpRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIcmpRedirects.setStatus(_A)
class _AgentSwitchDhcpOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('renew',1),('release',2),(_S,3)))
_AgentSwitchDhcpOperation_Type.__name__=_C
_AgentSwitchDhcpOperation_Object=MibTableColumn
agentSwitchDhcpOperation=_AgentSwitchDhcpOperation_Object((1,3,6,1,4,1,7244,2,2,2,3,1,12),_AgentSwitchDhcpOperation_Type())
agentSwitchDhcpOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDhcpOperation.setStatus(_F)
class _AgentSwitchIPAddressConfigMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('manual',1),('dhcp',2)))
_AgentSwitchIPAddressConfigMethod_Type.__name__=_C
_AgentSwitchIPAddressConfigMethod_Object=MibTableColumn
agentSwitchIPAddressConfigMethod=_AgentSwitchIPAddressConfigMethod_Object((1,3,6,1,4,1,7244,2,2,2,3,1,14),_AgentSwitchIPAddressConfigMethod_Type())
agentSwitchIPAddressConfigMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIPAddressConfigMethod.setStatus(_A)
class _AgentSwitchIpInterfaceDhcpClientRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restart',1))
_AgentSwitchIpInterfaceDhcpClientRestart_Type.__name__=_C
_AgentSwitchIpInterfaceDhcpClientRestart_Object=MibTableColumn
agentSwitchIpInterfaceDhcpClientRestart=_AgentSwitchIpInterfaceDhcpClientRestart_Object((1,3,6,1,4,1,7244,2,2,2,3,1,15),_AgentSwitchIpInterfaceDhcpClientRestart_Type())
agentSwitchIpInterfaceDhcpClientRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceDhcpClientRestart.setStatus(_A)
_AgentSwitchIpRouterDiscoveryTable_Object=MibTable
agentSwitchIpRouterDiscoveryTable=_AgentSwitchIpRouterDiscoveryTable_Object((1,3,6,1,4,1,7244,2,2,2,4))
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryTable.setStatus(_A)
_AgentSwitchIpRouterDiscoveryEntry_Object=MibTableRow
agentSwitchIpRouterDiscoveryEntry=_AgentSwitchIpRouterDiscoveryEntry_Object((1,3,6,1,4,1,7244,2,2,2,4,1))
agentSwitchIpRouterDiscoveryEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryEntry.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpRouterDiscoveryIfIndex_Type.__name__=_C
_AgentSwitchIpRouterDiscoveryIfIndex_Object=MibTableColumn
agentSwitchIpRouterDiscoveryIfIndex=_AgentSwitchIpRouterDiscoveryIfIndex_Object((1,3,6,1,4,1,7244,2,2,2,4,1,1),_AgentSwitchIpRouterDiscoveryIfIndex_Type())
agentSwitchIpRouterDiscoveryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryIfIndex.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryAdvertiseMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpRouterDiscoveryAdvertiseMode_Type.__name__=_C
_AgentSwitchIpRouterDiscoveryAdvertiseMode_Object=MibTableColumn
agentSwitchIpRouterDiscoveryAdvertiseMode=_AgentSwitchIpRouterDiscoveryAdvertiseMode_Object((1,3,6,1,4,1,7244,2,2,2,4,1,2),_AgentSwitchIpRouterDiscoveryAdvertiseMode_Type())
agentSwitchIpRouterDiscoveryAdvertiseMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryAdvertiseMode.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__=_C
_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object=MibTableColumn
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval=_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object((1,3,6,1,4,1,7244,2,2,2,4,1,3),_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type())
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):defaultValue=450;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type.__name__=_C
_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object=MibTableColumn
agentSwitchIpRouterDiscoveryMinAdvertisementInterval=_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object((1,3,6,1,4,1,7244,2,2,2,4,1,4),_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type())
agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,9000))
_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type.__name__=_C
_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object=MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementLifetime=_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object((1,3,6,1,4,1,7244,2,2,2,4,1,5),_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type())
agentSwitchIpRouterDiscoveryAdvertisementLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryAdvertisementLifetime.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryPreferenceLevel_Type(Integer32):defaultValue=0
_AgentSwitchIpRouterDiscoveryPreferenceLevel_Type.__name__=_C
_AgentSwitchIpRouterDiscoveryPreferenceLevel_Object=MibTableColumn
agentSwitchIpRouterDiscoveryPreferenceLevel=_AgentSwitchIpRouterDiscoveryPreferenceLevel_Object((1,3,6,1,4,1,7244,2,2,2,4,1,6),_AgentSwitchIpRouterDiscoveryPreferenceLevel_Type())
agentSwitchIpRouterDiscoveryPreferenceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryPreferenceLevel.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):defaultHexValue='E0000001'
_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type.__name__=_d
_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object=MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementAddress=_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object((1,3,6,1,4,1,7244,2,2,2,4,1,7),_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type())
agentSwitchIpRouterDiscoveryAdvertisementAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryAdvertisementAddress.setStatus(_A)
_AgentSwitchIpVlanTable_Object=MibTable
agentSwitchIpVlanTable=_AgentSwitchIpVlanTable_Object((1,3,6,1,4,1,7244,2,2,2,5))
if mibBuilder.loadTexts:agentSwitchIpVlanTable.setStatus(_A)
_AgentSwitchIpVlanEntry_Object=MibTableRow
agentSwitchIpVlanEntry=_AgentSwitchIpVlanEntry_Object((1,3,6,1,4,1,7244,2,2,2,5,1))
agentSwitchIpVlanEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:agentSwitchIpVlanEntry.setStatus(_A)
class _AgentSwitchIpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4093))
_AgentSwitchIpVlanId_Type.__name__=_C
_AgentSwitchIpVlanId_Object=MibTableColumn
agentSwitchIpVlanId=_AgentSwitchIpVlanId_Object((1,3,6,1,4,1,7244,2,2,2,5,1,1),_AgentSwitchIpVlanId_Type())
agentSwitchIpVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchIpVlanId.setStatus(_A)
_AgentSwitchIpVlanIfIndex_Type=Integer32
_AgentSwitchIpVlanIfIndex_Object=MibTableColumn
agentSwitchIpVlanIfIndex=_AgentSwitchIpVlanIfIndex_Object((1,3,6,1,4,1,7244,2,2,2,5,1,2),_AgentSwitchIpVlanIfIndex_Type())
agentSwitchIpVlanIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchIpVlanIfIndex.setStatus(_A)
_AgentSwitchIpVlanRoutingStatus_Type=RowStatus
_AgentSwitchIpVlanRoutingStatus_Object=MibTableColumn
agentSwitchIpVlanRoutingStatus=_AgentSwitchIpVlanRoutingStatus_Object((1,3,6,1,4,1,7244,2,2,2,5,1,3),_AgentSwitchIpVlanRoutingStatus_Type())
agentSwitchIpVlanRoutingStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIpVlanRoutingStatus.setStatus(_A)
_AgentSwitchSecondaryAddressTable_Object=MibTable
agentSwitchSecondaryAddressTable=_AgentSwitchSecondaryAddressTable_Object((1,3,6,1,4,1,7244,2,2,2,6))
if mibBuilder.loadTexts:agentSwitchSecondaryAddressTable.setStatus(_A)
_AgentSwitchSecondaryAddressEntry_Object=MibTableRow
agentSwitchSecondaryAddressEntry=_AgentSwitchSecondaryAddressEntry_Object((1,3,6,1,4,1,7244,2,2,2,6,1))
agentSwitchSecondaryAddressEntry.setIndexNames((0,_E,_W),(0,_E,_l))
if mibBuilder.loadTexts:agentSwitchSecondaryAddressEntry.setStatus(_A)
_AgentSwitchSecondaryIpAddress_Type=IpAddress
_AgentSwitchSecondaryIpAddress_Object=MibTableColumn
agentSwitchSecondaryIpAddress=_AgentSwitchSecondaryIpAddress_Object((1,3,6,1,4,1,7244,2,2,2,6,1,1),_AgentSwitchSecondaryIpAddress_Type())
agentSwitchSecondaryIpAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:agentSwitchSecondaryIpAddress.setStatus(_A)
_AgentSwitchSecondaryNetMask_Type=IpAddress
_AgentSwitchSecondaryNetMask_Object=MibTableColumn
agentSwitchSecondaryNetMask=_AgentSwitchSecondaryNetMask_Object((1,3,6,1,4,1,7244,2,2,2,6,1,2),_AgentSwitchSecondaryNetMask_Type())
agentSwitchSecondaryNetMask.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchSecondaryNetMask.setStatus(_A)
_AgentSwitchSecondaryStatus_Type=RowStatus
_AgentSwitchSecondaryStatus_Object=MibTableColumn
agentSwitchSecondaryStatus=_AgentSwitchSecondaryStatus_Object((1,3,6,1,4,1,7244,2,2,2,6,1,3),_AgentSwitchSecondaryStatus_Type())
agentSwitchSecondaryStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchSecondaryStatus.setStatus(_A)
_AgentSwitchHelperAddressTable_Object=MibTable
agentSwitchHelperAddressTable=_AgentSwitchHelperAddressTable_Object((1,3,6,1,4,1,7244,2,2,2,7))
if mibBuilder.loadTexts:agentSwitchHelperAddressTable.setStatus(_F)
_AgentSwitchHelperAddressEntry_Object=MibTableRow
agentSwitchHelperAddressEntry=_AgentSwitchHelperAddressEntry_Object((1,3,6,1,4,1,7244,2,2,2,7,1))
agentSwitchHelperAddressEntry.setIndexNames((0,_E,_W),(0,_E,_m))
if mibBuilder.loadTexts:agentSwitchHelperAddressEntry.setStatus(_F)
_AgentSwitchHelperIpAddress_Type=IpAddress
_AgentSwitchHelperIpAddress_Object=MibTableColumn
agentSwitchHelperIpAddress=_AgentSwitchHelperIpAddress_Object((1,3,6,1,4,1,7244,2,2,2,7,1,1),_AgentSwitchHelperIpAddress_Type())
agentSwitchHelperIpAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:agentSwitchHelperIpAddress.setStatus(_F)
_AgentSwitchHelperStatus_Type=RowStatus
_AgentSwitchHelperStatus_Object=MibTableColumn
agentSwitchHelperStatus=_AgentSwitchHelperStatus_Object((1,3,6,1,4,1,7244,2,2,2,7,1,2),_AgentSwitchHelperStatus_Type())
agentSwitchHelperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchHelperStatus.setStatus(_F)
_AgentSwitchIpIcmpControlGroup_ObjectIdentity=ObjectIdentity
agentSwitchIpIcmpControlGroup=_AgentSwitchIpIcmpControlGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,2,8))
class _AgentSwitchIpIcmpEchoReplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpIcmpEchoReplyMode_Type.__name__=_C
_AgentSwitchIpIcmpEchoReplyMode_Object=MibScalar
agentSwitchIpIcmpEchoReplyMode=_AgentSwitchIpIcmpEchoReplyMode_Object((1,3,6,1,4,1,7244,2,2,2,8,1),_AgentSwitchIpIcmpEchoReplyMode_Type())
agentSwitchIpIcmpEchoReplyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpIcmpEchoReplyMode.setStatus(_A)
class _AgentSwitchIpIcmpRedirectsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpIcmpRedirectsMode_Type.__name__=_C
_AgentSwitchIpIcmpRedirectsMode_Object=MibScalar
agentSwitchIpIcmpRedirectsMode=_AgentSwitchIpIcmpRedirectsMode_Object((1,3,6,1,4,1,7244,2,2,2,8,2),_AgentSwitchIpIcmpRedirectsMode_Type())
agentSwitchIpIcmpRedirectsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpIcmpRedirectsMode.setStatus(_A)
class _AgentSwitchIpIcmpRateLimitInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpIcmpRateLimitInterval_Type.__name__=_C
_AgentSwitchIpIcmpRateLimitInterval_Object=MibScalar
agentSwitchIpIcmpRateLimitInterval=_AgentSwitchIpIcmpRateLimitInterval_Object((1,3,6,1,4,1,7244,2,2,2,8,3),_AgentSwitchIpIcmpRateLimitInterval_Type())
agentSwitchIpIcmpRateLimitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpIcmpRateLimitInterval.setStatus(_A)
class _AgentSwitchIpIcmpRateLimitBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_AgentSwitchIpIcmpRateLimitBurstSize_Type.__name__=_C
_AgentSwitchIpIcmpRateLimitBurstSize_Object=MibScalar
agentSwitchIpIcmpRateLimitBurstSize=_AgentSwitchIpIcmpRateLimitBurstSize_Object((1,3,6,1,4,1,7244,2,2,2,8,4),_AgentSwitchIpIcmpRateLimitBurstSize_Type())
agentSwitchIpIcmpRateLimitBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpIcmpRateLimitBurstSize.setStatus(_A)
_AgentSwitchIntfIpHelperAddressTable_Object=MibTable
agentSwitchIntfIpHelperAddressTable=_AgentSwitchIntfIpHelperAddressTable_Object((1,3,6,1,4,1,7244,2,2,2,10))
if mibBuilder.loadTexts:agentSwitchIntfIpHelperAddressTable.setStatus(_A)
_AgentSwitchIntfIpHelperAddressEntry_Object=MibTableRow
agentSwitchIntfIpHelperAddressEntry=_AgentSwitchIntfIpHelperAddressEntry_Object((1,3,6,1,4,1,7244,2,2,2,10,1))
agentSwitchIntfIpHelperAddressEntry.setIndexNames((0,_E,_W),(0,_E,_n),(0,_E,_o))
if mibBuilder.loadTexts:agentSwitchIntfIpHelperAddressEntry.setStatus(_A)
_AgentSwitchIntfIpHelperIpAddress_Type=IpAddress
_AgentSwitchIntfIpHelperIpAddress_Object=MibTableColumn
agentSwitchIntfIpHelperIpAddress=_AgentSwitchIntfIpHelperIpAddress_Object((1,3,6,1,4,1,7244,2,2,2,10,1,1),_AgentSwitchIntfIpHelperIpAddress_Type())
agentSwitchIntfIpHelperIpAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperIpAddress.setStatus(_A)
class _AgentSwitchIntfIpHelperUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentSwitchIntfIpHelperUdpPort_Type.__name__=_J
_AgentSwitchIntfIpHelperUdpPort_Object=MibTableColumn
agentSwitchIntfIpHelperUdpPort=_AgentSwitchIntfIpHelperUdpPort_Object((1,3,6,1,4,1,7244,2,2,2,10,1,2),_AgentSwitchIntfIpHelperUdpPort_Type())
agentSwitchIntfIpHelperUdpPort.setMaxAccess(_P)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperUdpPort.setStatus(_A)
_AgentSwitchIntfIpHelperDiscard_Type=TruthValue
_AgentSwitchIntfIpHelperDiscard_Object=MibTableColumn
agentSwitchIntfIpHelperDiscard=_AgentSwitchIntfIpHelperDiscard_Object((1,3,6,1,4,1,7244,2,2,2,10,1,3),_AgentSwitchIntfIpHelperDiscard_Type())
agentSwitchIntfIpHelperDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperDiscard.setStatus(_F)
_AgentSwitchIntfIpHelperHitCount_Type=Unsigned32
_AgentSwitchIntfIpHelperHitCount_Object=MibTableColumn
agentSwitchIntfIpHelperHitCount=_AgentSwitchIntfIpHelperHitCount_Object((1,3,6,1,4,1,7244,2,2,2,10,1,4),_AgentSwitchIntfIpHelperHitCount_Type())
agentSwitchIntfIpHelperHitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperHitCount.setStatus(_A)
_AgentSwitchIntfIpHelperStatus_Type=RowStatus
_AgentSwitchIntfIpHelperStatus_Object=MibTableColumn
agentSwitchIntfIpHelperStatus=_AgentSwitchIntfIpHelperStatus_Object((1,3,6,1,4,1,7244,2,2,2,10,1,5),_AgentSwitchIntfIpHelperStatus_Type())
agentSwitchIntfIpHelperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperStatus.setStatus(_A)
class _AgentSwitchClearIpDefaultGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchClearIpDefaultGateway_Type.__name__=_C
_AgentSwitchClearIpDefaultGateway_Object=MibScalar
agentSwitchClearIpDefaultGateway=_AgentSwitchClearIpDefaultGateway_Object((1,3,6,1,4,1,7244,2,2,2,11),_AgentSwitchClearIpDefaultGateway_Type())
agentSwitchClearIpDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchClearIpDefaultGateway.setStatus(_A)
_AgentSwitchIpInterfaceRoutingModeEnable_Type=Integer32
_AgentSwitchIpInterfaceRoutingModeEnable_Object=MibScalar
agentSwitchIpInterfaceRoutingModeEnable=_AgentSwitchIpInterfaceRoutingModeEnable_Object((1,3,6,1,4,1,7244,2,2,2,12),_AgentSwitchIpInterfaceRoutingModeEnable_Type())
agentSwitchIpInterfaceRoutingModeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceRoutingModeEnable.setStatus(_A)
class _AgentSwitchIpDeadGatewayDetectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpDeadGatewayDetectMode_Type.__name__=_C
_AgentSwitchIpDeadGatewayDetectMode_Object=MibScalar
agentSwitchIpDeadGatewayDetectMode=_AgentSwitchIpDeadGatewayDetectMode_Object((1,3,6,1,4,1,7244,2,2,2,13),_AgentSwitchIpDeadGatewayDetectMode_Type())
agentSwitchIpDeadGatewayDetectMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpDeadGatewayDetectMode.setStatus(_A)
class _AgentSwitchIpDeadGatewayDetectionProbeInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentSwitchIpDeadGatewayDetectionProbeInterval_Type.__name__=_C
_AgentSwitchIpDeadGatewayDetectionProbeInterval_Object=MibScalar
agentSwitchIpDeadGatewayDetectionProbeInterval=_AgentSwitchIpDeadGatewayDetectionProbeInterval_Object((1,3,6,1,4,1,7244,2,2,2,14),_AgentSwitchIpDeadGatewayDetectionProbeInterval_Type())
agentSwitchIpDeadGatewayDetectionProbeInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpDeadGatewayDetectionProbeInterval.setStatus(_A)
_AgentRouterRipConfigGroup_ObjectIdentity=ObjectIdentity
agentRouterRipConfigGroup=_AgentRouterRipConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,3))
class _AgentRouterRipAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentRouterRipAdminState_Type.__name__=_C
_AgentRouterRipAdminState_Object=MibScalar
agentRouterRipAdminState=_AgentRouterRipAdminState_Object((1,3,6,1,4,1,7244,2,2,3,1),_AgentRouterRipAdminState_Type())
agentRouterRipAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipAdminState.setStatus(_A)
class _AgentRouterRipSplitHorizonMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('simple',2),('poisonReverse',3)))
_AgentRouterRipSplitHorizonMode_Type.__name__=_C
_AgentRouterRipSplitHorizonMode_Object=MibScalar
agentRouterRipSplitHorizonMode=_AgentRouterRipSplitHorizonMode_Object((1,3,6,1,4,1,7244,2,2,3,2),_AgentRouterRipSplitHorizonMode_Type())
agentRouterRipSplitHorizonMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipSplitHorizonMode.setStatus(_A)
class _AgentRouterRipAutoSummaryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentRouterRipAutoSummaryMode_Type.__name__=_C
_AgentRouterRipAutoSummaryMode_Object=MibScalar
agentRouterRipAutoSummaryMode=_AgentRouterRipAutoSummaryMode_Object((1,3,6,1,4,1,7244,2,2,3,3),_AgentRouterRipAutoSummaryMode_Type())
agentRouterRipAutoSummaryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipAutoSummaryMode.setStatus(_A)
class _AgentRouterRipHostRoutesAcceptMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentRouterRipHostRoutesAcceptMode_Type.__name__=_C
_AgentRouterRipHostRoutesAcceptMode_Object=MibScalar
agentRouterRipHostRoutesAcceptMode=_AgentRouterRipHostRoutesAcceptMode_Object((1,3,6,1,4,1,7244,2,2,3,4),_AgentRouterRipHostRoutesAcceptMode_Type())
agentRouterRipHostRoutesAcceptMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipHostRoutesAcceptMode.setStatus(_A)
class _AgentRouterRipDefaultMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_AgentRouterRipDefaultMetric_Type.__name__=_C
_AgentRouterRipDefaultMetric_Object=MibScalar
agentRouterRipDefaultMetric=_AgentRouterRipDefaultMetric_Object((1,3,6,1,4,1,7244,2,2,3,5),_AgentRouterRipDefaultMetric_Type())
agentRouterRipDefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipDefaultMetric.setStatus(_A)
class _AgentRouterRipDefaultMetricConfigured_Type(TruthValue):defaultValue=2
_AgentRouterRipDefaultMetricConfigured_Type.__name__=_L
_AgentRouterRipDefaultMetricConfigured_Object=MibScalar
agentRouterRipDefaultMetricConfigured=_AgentRouterRipDefaultMetricConfigured_Object((1,3,6,1,4,1,7244,2,2,3,6),_AgentRouterRipDefaultMetricConfigured_Type())
agentRouterRipDefaultMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipDefaultMetricConfigured.setStatus(_A)
class _AgentRouterRipDefaultInfoOriginate_Type(TruthValue):defaultValue=2
_AgentRouterRipDefaultInfoOriginate_Type.__name__=_L
_AgentRouterRipDefaultInfoOriginate_Object=MibScalar
agentRouterRipDefaultInfoOriginate=_AgentRouterRipDefaultInfoOriginate_Object((1,3,6,1,4,1,7244,2,2,3,7),_AgentRouterRipDefaultInfoOriginate_Type())
agentRouterRipDefaultInfoOriginate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipDefaultInfoOriginate.setStatus(_A)
class _AgentRouterRipDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentRouterRipDistance_Type.__name__=_C
_AgentRouterRipDistance_Object=MibScalar
agentRouterRipDistance=_AgentRouterRipDistance_Object((1,3,6,1,4,1,7244,2,2,3,8),_AgentRouterRipDistance_Type())
agentRouterRipDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipDistance.setStatus(_F)
_AgentRipRouteRedistTable_Object=MibTable
agentRipRouteRedistTable=_AgentRipRouteRedistTable_Object((1,3,6,1,4,1,7244,2,2,3,9))
if mibBuilder.loadTexts:agentRipRouteRedistTable.setStatus(_A)
_AgentRipRouteRedistEntry_Object=MibTableRow
agentRipRouteRedistEntry=_AgentRipRouteRedistEntry_Object((1,3,6,1,4,1,7244,2,2,3,9,1))
agentRipRouteRedistEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:agentRipRouteRedistEntry.setStatus(_A)
class _AgentRipRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_V,2),('ospf',3)))
_AgentRipRouteRedistSource_Type.__name__=_C
_AgentRipRouteRedistSource_Object=MibTableColumn
agentRipRouteRedistSource=_AgentRipRouteRedistSource_Object((1,3,6,1,4,1,7244,2,2,3,9,1,1),_AgentRipRouteRedistSource_Type())
agentRipRouteRedistSource.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRipRouteRedistSource.setStatus(_A)
class _AgentRipRouteRedistMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentRipRouteRedistMode_Type.__name__=_C
_AgentRipRouteRedistMode_Object=MibTableColumn
agentRipRouteRedistMode=_AgentRipRouteRedistMode_Object((1,3,6,1,4,1,7244,2,2,3,9,1,2),_AgentRipRouteRedistMode_Type())
agentRipRouteRedistMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistMode.setStatus(_A)
class _AgentRipRouteRedistMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_AgentRipRouteRedistMetric_Type.__name__=_C
_AgentRipRouteRedistMetric_Object=MibTableColumn
agentRipRouteRedistMetric=_AgentRipRouteRedistMetric_Object((1,3,6,1,4,1,7244,2,2,3,9,1,3),_AgentRipRouteRedistMetric_Type())
agentRipRouteRedistMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistMetric.setStatus(_A)
class _AgentRipRouteRedistMetricConfigured_Type(TruthValue):defaultValue=2
_AgentRipRouteRedistMetricConfigured_Type.__name__=_L
_AgentRipRouteRedistMetricConfigured_Object=MibTableColumn
agentRipRouteRedistMetricConfigured=_AgentRipRouteRedistMetricConfigured_Object((1,3,6,1,4,1,7244,2,2,3,9,1,4),_AgentRipRouteRedistMetricConfigured_Type())
agentRipRouteRedistMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistMetricConfigured.setStatus(_A)
class _AgentRipRouteRedistMatchInternal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentRipRouteRedistMatchInternal_Type.__name__=_C
_AgentRipRouteRedistMatchInternal_Object=MibTableColumn
agentRipRouteRedistMatchInternal=_AgentRipRouteRedistMatchInternal_Object((1,3,6,1,4,1,7244,2,2,3,9,1,5),_AgentRipRouteRedistMatchInternal_Type())
agentRipRouteRedistMatchInternal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistMatchInternal.setStatus(_A)
class _AgentRipRouteRedistMatchExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentRipRouteRedistMatchExternal1_Type.__name__=_C
_AgentRipRouteRedistMatchExternal1_Object=MibTableColumn
agentRipRouteRedistMatchExternal1=_AgentRipRouteRedistMatchExternal1_Object((1,3,6,1,4,1,7244,2,2,3,9,1,6),_AgentRipRouteRedistMatchExternal1_Type())
agentRipRouteRedistMatchExternal1.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistMatchExternal1.setStatus(_A)
class _AgentRipRouteRedistMatchExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentRipRouteRedistMatchExternal2_Type.__name__=_C
_AgentRipRouteRedistMatchExternal2_Object=MibTableColumn
agentRipRouteRedistMatchExternal2=_AgentRipRouteRedistMatchExternal2_Object((1,3,6,1,4,1,7244,2,2,3,9,1,7),_AgentRipRouteRedistMatchExternal2_Type())
agentRipRouteRedistMatchExternal2.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistMatchExternal2.setStatus(_A)
class _AgentRipRouteRedistMatchNSSAExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentRipRouteRedistMatchNSSAExternal1_Type.__name__=_C
_AgentRipRouteRedistMatchNSSAExternal1_Object=MibTableColumn
agentRipRouteRedistMatchNSSAExternal1=_AgentRipRouteRedistMatchNSSAExternal1_Object((1,3,6,1,4,1,7244,2,2,3,9,1,8),_AgentRipRouteRedistMatchNSSAExternal1_Type())
agentRipRouteRedistMatchNSSAExternal1.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistMatchNSSAExternal1.setStatus(_A)
class _AgentRipRouteRedistMatchNSSAExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentRipRouteRedistMatchNSSAExternal2_Type.__name__=_C
_AgentRipRouteRedistMatchNSSAExternal2_Object=MibTableColumn
agentRipRouteRedistMatchNSSAExternal2=_AgentRipRouteRedistMatchNSSAExternal2_Object((1,3,6,1,4,1,7244,2,2,3,9,1,9),_AgentRipRouteRedistMatchNSSAExternal2_Type())
agentRipRouteRedistMatchNSSAExternal2.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistMatchNSSAExternal2.setStatus(_A)
class _AgentRipRouteRedistDistList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_AgentRipRouteRedistDistList_Type.__name__=_J
_AgentRipRouteRedistDistList_Object=MibTableColumn
agentRipRouteRedistDistList=_AgentRipRouteRedistDistList_Object((1,3,6,1,4,1,7244,2,2,3,9,1,10),_AgentRipRouteRedistDistList_Type())
agentRipRouteRedistDistList.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistDistList.setStatus(_A)
_AgentRipRouteRedistDistListConfigured_Type=TruthValue
_AgentRipRouteRedistDistListConfigured_Object=MibTableColumn
agentRipRouteRedistDistListConfigured=_AgentRipRouteRedistDistListConfigured_Object((1,3,6,1,4,1,7244,2,2,3,9,1,11),_AgentRipRouteRedistDistListConfigured_Type())
agentRipRouteRedistDistListConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistDistListConfigured.setStatus(_A)
_AgentRip2IfConfTable_Object=MibTable
agentRip2IfConfTable=_AgentRip2IfConfTable_Object((1,3,6,1,4,1,7244,2,2,3,10))
if mibBuilder.loadTexts:agentRip2IfConfTable.setStatus(_A)
_AgentRip2IfConfEntry_Object=MibTableRow
agentRip2IfConfEntry=_AgentRip2IfConfEntry_Object((1,3,6,1,4,1,7244,2,2,3,10,1))
if mibBuilder.loadTexts:agentRip2IfConfEntry.setStatus(_A)
class _AgentRip2IfConfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentRip2IfConfAuthKeyId_Type.__name__=_C
_AgentRip2IfConfAuthKeyId_Object=MibTableColumn
agentRip2IfConfAuthKeyId=_AgentRip2IfConfAuthKeyId_Object((1,3,6,1,4,1,7244,2,2,3,10,1,1),_AgentRip2IfConfAuthKeyId_Type())
agentRip2IfConfAuthKeyId.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRip2IfConfAuthKeyId.setStatus(_A)
class _AgentRouterRipRoutePref_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentRouterRipRoutePref_Type.__name__=_C
_AgentRouterRipRoutePref_Object=MibScalar
agentRouterRipRoutePref=_AgentRouterRipRoutePref_Object((1,3,6,1,4,1,7244,2,2,3,11),_AgentRouterRipRoutePref_Type())
agentRouterRipRoutePref.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterRipRoutePref.setStatus(_A)
_AgentRouterOspfConfigGroup_ObjectIdentity=ObjectIdentity
agentRouterOspfConfigGroup=_AgentRouterOspfConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,4))
class _AgentOspfDefaultMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16777214))
_AgentOspfDefaultMetric_Type.__name__=_C
_AgentOspfDefaultMetric_Object=MibScalar
agentOspfDefaultMetric=_AgentOspfDefaultMetric_Object((1,3,6,1,4,1,7244,2,2,4,1),_AgentOspfDefaultMetric_Type())
agentOspfDefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDefaultMetric.setStatus(_A)
class _AgentOspfDefaultMetricConfigured_Type(TruthValue):defaultValue=2
_AgentOspfDefaultMetricConfigured_Type.__name__=_L
_AgentOspfDefaultMetricConfigured_Object=MibScalar
agentOspfDefaultMetricConfigured=_AgentOspfDefaultMetricConfigured_Object((1,3,6,1,4,1,7244,2,2,4,2),_AgentOspfDefaultMetricConfigured_Type())
agentOspfDefaultMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDefaultMetricConfigured.setStatus(_A)
class _AgentOspfDefaultInfoOriginate_Type(TruthValue):defaultValue=2
_AgentOspfDefaultInfoOriginate_Type.__name__=_L
_AgentOspfDefaultInfoOriginate_Object=MibScalar
agentOspfDefaultInfoOriginate=_AgentOspfDefaultInfoOriginate_Object((1,3,6,1,4,1,7244,2,2,4,3),_AgentOspfDefaultInfoOriginate_Type())
agentOspfDefaultInfoOriginate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginate.setStatus(_A)
class _AgentOspfDefaultInfoOriginateAlways_Type(TruthValue):defaultValue=2
_AgentOspfDefaultInfoOriginateAlways_Type.__name__=_L
_AgentOspfDefaultInfoOriginateAlways_Object=MibScalar
agentOspfDefaultInfoOriginateAlways=_AgentOspfDefaultInfoOriginateAlways_Object((1,3,6,1,4,1,7244,2,2,4,4),_AgentOspfDefaultInfoOriginateAlways_Type())
agentOspfDefaultInfoOriginateAlways.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginateAlways.setStatus(_A)
class _AgentOspfDefaultInfoOriginateMetric_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16777214))
_AgentOspfDefaultInfoOriginateMetric_Type.__name__=_C
_AgentOspfDefaultInfoOriginateMetric_Object=MibScalar
agentOspfDefaultInfoOriginateMetric=_AgentOspfDefaultInfoOriginateMetric_Object((1,3,6,1,4,1,7244,2,2,4,5),_AgentOspfDefaultInfoOriginateMetric_Type())
agentOspfDefaultInfoOriginateMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginateMetric.setStatus(_A)
_AgentOspfDefaultInfoOriginateMetricConfigured_Type=TruthValue
_AgentOspfDefaultInfoOriginateMetricConfigured_Object=MibScalar
agentOspfDefaultInfoOriginateMetricConfigured=_AgentOspfDefaultInfoOriginateMetricConfigured_Object((1,3,6,1,4,1,7244,2,2,4,6),_AgentOspfDefaultInfoOriginateMetricConfigured_Type())
agentOspfDefaultInfoOriginateMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginateMetricConfigured.setStatus(_A)
class _AgentOspfDefaultInfoOriginateMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_q,1),(_r,2)))
_AgentOspfDefaultInfoOriginateMetricType_Type.__name__=_C
_AgentOspfDefaultInfoOriginateMetricType_Object=MibScalar
agentOspfDefaultInfoOriginateMetricType=_AgentOspfDefaultInfoOriginateMetricType_Object((1,3,6,1,4,1,7244,2,2,4,7),_AgentOspfDefaultInfoOriginateMetricType_Type())
agentOspfDefaultInfoOriginateMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginateMetricType.setStatus(_A)
_AgentOspfRouteRedistTable_Object=MibTable
agentOspfRouteRedistTable=_AgentOspfRouteRedistTable_Object((1,3,6,1,4,1,7244,2,2,4,8))
if mibBuilder.loadTexts:agentOspfRouteRedistTable.setStatus(_A)
_AgentOspfRouteRedistEntry_Object=MibTableRow
agentOspfRouteRedistEntry=_AgentOspfRouteRedistEntry_Object((1,3,6,1,4,1,7244,2,2,4,8,1))
agentOspfRouteRedistEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:agentOspfRouteRedistEntry.setStatus(_A)
class _AgentOspfRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_V,2),('rip',3)))
_AgentOspfRouteRedistSource_Type.__name__=_C
_AgentOspfRouteRedistSource_Object=MibTableColumn
agentOspfRouteRedistSource=_AgentOspfRouteRedistSource_Object((1,3,6,1,4,1,7244,2,2,4,8,1,1),_AgentOspfRouteRedistSource_Type())
agentOspfRouteRedistSource.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfRouteRedistSource.setStatus(_A)
class _AgentOspfRouteRedistMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentOspfRouteRedistMode_Type.__name__=_C
_AgentOspfRouteRedistMode_Object=MibTableColumn
agentOspfRouteRedistMode=_AgentOspfRouteRedistMode_Object((1,3,6,1,4,1,7244,2,2,4,8,1,2),_AgentOspfRouteRedistMode_Type())
agentOspfRouteRedistMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRouteRedistMode.setStatus(_A)
class _AgentOspfRouteRedistMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_AgentOspfRouteRedistMetric_Type.__name__=_C
_AgentOspfRouteRedistMetric_Object=MibTableColumn
agentOspfRouteRedistMetric=_AgentOspfRouteRedistMetric_Object((1,3,6,1,4,1,7244,2,2,4,8,1,3),_AgentOspfRouteRedistMetric_Type())
agentOspfRouteRedistMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRouteRedistMetric.setStatus(_A)
_AgentOspfRouteRedistMetricConfigured_Type=TruthValue
_AgentOspfRouteRedistMetricConfigured_Object=MibTableColumn
agentOspfRouteRedistMetricConfigured=_AgentOspfRouteRedistMetricConfigured_Object((1,3,6,1,4,1,7244,2,2,4,8,1,4),_AgentOspfRouteRedistMetricConfigured_Type())
agentOspfRouteRedistMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRouteRedistMetricConfigured.setStatus(_A)
class _AgentOspfRouteRedistMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_q,1),(_r,2)))
_AgentOspfRouteRedistMetricType_Type.__name__=_C
_AgentOspfRouteRedistMetricType_Object=MibTableColumn
agentOspfRouteRedistMetricType=_AgentOspfRouteRedistMetricType_Object((1,3,6,1,4,1,7244,2,2,4,8,1,5),_AgentOspfRouteRedistMetricType_Type())
agentOspfRouteRedistMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRouteRedistMetricType.setStatus(_A)
_AgentOspfRouteRedistTag_Type=Unsigned32
_AgentOspfRouteRedistTag_Object=MibTableColumn
agentOspfRouteRedistTag=_AgentOspfRouteRedistTag_Object((1,3,6,1,4,1,7244,2,2,4,8,1,6),_AgentOspfRouteRedistTag_Type())
agentOspfRouteRedistTag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRouteRedistTag.setStatus(_A)
class _AgentOspfRouteRedistSubnets_Type(TruthValue):defaultValue=2
_AgentOspfRouteRedistSubnets_Type.__name__=_L
_AgentOspfRouteRedistSubnets_Object=MibTableColumn
agentOspfRouteRedistSubnets=_AgentOspfRouteRedistSubnets_Object((1,3,6,1,4,1,7244,2,2,4,8,1,7),_AgentOspfRouteRedistSubnets_Type())
agentOspfRouteRedistSubnets.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRouteRedistSubnets.setStatus(_A)
class _AgentOspfRouteRedistDistList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_AgentOspfRouteRedistDistList_Type.__name__=_J
_AgentOspfRouteRedistDistList_Object=MibTableColumn
agentOspfRouteRedistDistList=_AgentOspfRouteRedistDistList_Object((1,3,6,1,4,1,7244,2,2,4,8,1,8),_AgentOspfRouteRedistDistList_Type())
agentOspfRouteRedistDistList.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRouteRedistDistList.setStatus(_A)
_AgentOspfRouteRedistDistListConfigured_Type=TruthValue
_AgentOspfRouteRedistDistListConfigured_Object=MibTableColumn
agentOspfRouteRedistDistListConfigured=_AgentOspfRouteRedistDistListConfigured_Object((1,3,6,1,4,1,7244,2,2,4,8,1,9),_AgentOspfRouteRedistDistListConfigured_Type())
agentOspfRouteRedistDistListConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRouteRedistDistListConfigured.setStatus(_A)
_AgentOspfIfTable_Object=MibTable
agentOspfIfTable=_AgentOspfIfTable_Object((1,3,6,1,4,1,7244,2,2,4,9))
if mibBuilder.loadTexts:agentOspfIfTable.setStatus(_A)
_AgentOspfIfEntry_Object=MibTableRow
agentOspfIfEntry=_AgentOspfIfEntry_Object((1,3,6,1,4,1,7244,2,2,4,9,1))
if mibBuilder.loadTexts:agentOspfIfEntry.setStatus(_A)
class _AgentOspfIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOspfIfAuthKeyId_Type.__name__=_C
_AgentOspfIfAuthKeyId_Object=MibTableColumn
agentOspfIfAuthKeyId=_AgentOspfIfAuthKeyId_Object((1,3,6,1,4,1,7244,2,2,4,9,1,1),_AgentOspfIfAuthKeyId_Type())
agentOspfIfAuthKeyId.setMaxAccess(_I)
if mibBuilder.loadTexts:agentOspfIfAuthKeyId.setStatus(_A)
class _AgentOspfIfIpMtuIgnoreFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentOspfIfIpMtuIgnoreFlag_Type.__name__=_C
_AgentOspfIfIpMtuIgnoreFlag_Object=MibTableColumn
agentOspfIfIpMtuIgnoreFlag=_AgentOspfIfIpMtuIgnoreFlag_Object((1,3,6,1,4,1,7244,2,2,4,9,1,2),_AgentOspfIfIpMtuIgnoreFlag_Type())
agentOspfIfIpMtuIgnoreFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfIfIpMtuIgnoreFlag.setStatus(_A)
class _AgentOspfIfPassiveMode_Type(TruthValue):defaultValue=2
_AgentOspfIfPassiveMode_Type.__name__=_L
_AgentOspfIfPassiveMode_Object=MibTableColumn
agentOspfIfPassiveMode=_AgentOspfIfPassiveMode_Object((1,3,6,1,4,1,7244,2,2,4,9,1,3),_AgentOspfIfPassiveMode_Type())
agentOspfIfPassiveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfIfPassiveMode.setStatus(_A)
class _AgentOspfIfAdvertiseSecondaries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentOspfIfAdvertiseSecondaries_Type.__name__=_C
_AgentOspfIfAdvertiseSecondaries_Object=MibTableColumn
agentOspfIfAdvertiseSecondaries=_AgentOspfIfAdvertiseSecondaries_Object((1,3,6,1,4,1,7244,2,2,4,9,1,4),_AgentOspfIfAdvertiseSecondaries_Type())
agentOspfIfAdvertiseSecondaries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfIfAdvertiseSecondaries.setStatus(_A)
_AgentOspfVirtIfTable_Object=MibTable
agentOspfVirtIfTable=_AgentOspfVirtIfTable_Object((1,3,6,1,4,1,7244,2,2,4,10))
if mibBuilder.loadTexts:agentOspfVirtIfTable.setStatus(_A)
_AgentOspfVirtIfEntry_Object=MibTableRow
agentOspfVirtIfEntry=_AgentOspfVirtIfEntry_Object((1,3,6,1,4,1,7244,2,2,4,10,1))
if mibBuilder.loadTexts:agentOspfVirtIfEntry.setStatus(_A)
class _AgentOspfVirtIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOspfVirtIfAuthKeyId_Type.__name__=_C
_AgentOspfVirtIfAuthKeyId_Object=MibTableColumn
agentOspfVirtIfAuthKeyId=_AgentOspfVirtIfAuthKeyId_Object((1,3,6,1,4,1,7244,2,2,4,10,1,1),_AgentOspfVirtIfAuthKeyId_Type())
agentOspfVirtIfAuthKeyId.setMaxAccess(_I)
if mibBuilder.loadTexts:agentOspfVirtIfAuthKeyId.setStatus(_A)
class _AgentRouterOspfRFC1583CompatibilityMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentRouterOspfRFC1583CompatibilityMode_Type.__name__=_C
_AgentRouterOspfRFC1583CompatibilityMode_Object=MibScalar
agentRouterOspfRFC1583CompatibilityMode=_AgentRouterOspfRFC1583CompatibilityMode_Object((1,3,6,1,4,1,7244,2,2,4,11),_AgentRouterOspfRFC1583CompatibilityMode_Type())
agentRouterOspfRFC1583CompatibilityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterOspfRFC1583CompatibilityMode.setStatus(_A)
class _AgentOspfSpfDelayTime_Type(SpfTimerRange):defaultValue=5
_AgentOspfSpfDelayTime_Type.__name__=_Y
_AgentOspfSpfDelayTime_Object=MibScalar
agentOspfSpfDelayTime=_AgentOspfSpfDelayTime_Object((1,3,6,1,4,1,7244,2,2,4,12),_AgentOspfSpfDelayTime_Type())
agentOspfSpfDelayTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfSpfDelayTime.setStatus(_A)
class _AgentOspfSpfHoldTime_Type(SpfTimerRange):defaultValue=10
_AgentOspfSpfHoldTime_Type.__name__=_Y
_AgentOspfSpfHoldTime_Object=MibScalar
agentOspfSpfHoldTime=_AgentOspfSpfHoldTime_Object((1,3,6,1,4,1,7244,2,2,4,13),_AgentOspfSpfHoldTime_Type())
agentOspfSpfHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfSpfHoldTime.setStatus(_A)
class _AgentOspfAutoCostRefBw_Type(AutoCostRefBw):defaultValue=100
_AgentOspfAutoCostRefBw_Type.__name__=_t
_AgentOspfAutoCostRefBw_Object=MibScalar
agentOspfAutoCostRefBw=_AgentOspfAutoCostRefBw_Object((1,3,6,1,4,1,7244,2,2,4,14),_AgentOspfAutoCostRefBw_Type())
agentOspfAutoCostRefBw.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAutoCostRefBw.setStatus(_A)
_AgentOspfOpaqueLsaSupport_Type=TruthValue
_AgentOspfOpaqueLsaSupport_Object=MibScalar
agentOspfOpaqueLsaSupport=_AgentOspfOpaqueLsaSupport_Object((1,3,6,1,4,1,7244,2,2,4,15),_AgentOspfOpaqueLsaSupport_Type())
agentOspfOpaqueLsaSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfOpaqueLsaSupport.setStatus(_A)
_AgentOspfAreaOpaqueLsdbTable_Object=MibTable
agentOspfAreaOpaqueLsdbTable=_AgentOspfAreaOpaqueLsdbTable_Object((1,3,6,1,4,1,7244,2,2,4,16))
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbTable.setStatus(_A)
_AgentOspfAreaOpaqueLsdbEntry_Object=MibTableRow
agentOspfAreaOpaqueLsdbEntry=_AgentOspfAreaOpaqueLsdbEntry_Object((1,3,6,1,4,1,7244,2,2,4,16,1))
agentOspfAreaOpaqueLsdbEntry.setIndexNames((0,_E,_u),(0,_E,_v),(0,_E,_w),(0,_E,_x))
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbEntry.setStatus(_A)
_AgentOspfAreaOpaqueLsdbAreaId_Type=IpAddress
_AgentOspfAreaOpaqueLsdbAreaId_Object=MibTableColumn
agentOspfAreaOpaqueLsdbAreaId=_AgentOspfAreaOpaqueLsdbAreaId_Object((1,3,6,1,4,1,7244,2,2,4,16,1,1),_AgentOspfAreaOpaqueLsdbAreaId_Type())
agentOspfAreaOpaqueLsdbAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbAreaId.setStatus(_A)
class _AgentOspfAreaOpaqueLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(10));namedValues=NamedValues(('areaOpaqueLink',10))
_AgentOspfAreaOpaqueLsdbType_Type.__name__=_C
_AgentOspfAreaOpaqueLsdbType_Object=MibTableColumn
agentOspfAreaOpaqueLsdbType=_AgentOspfAreaOpaqueLsdbType_Object((1,3,6,1,4,1,7244,2,2,4,16,1,2),_AgentOspfAreaOpaqueLsdbType_Type())
agentOspfAreaOpaqueLsdbType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbType.setStatus(_A)
_AgentOspfAreaOpaqueLsdbLsid_Type=IpAddress
_AgentOspfAreaOpaqueLsdbLsid_Object=MibTableColumn
agentOspfAreaOpaqueLsdbLsid=_AgentOspfAreaOpaqueLsdbLsid_Object((1,3,6,1,4,1,7244,2,2,4,16,1,3),_AgentOspfAreaOpaqueLsdbLsid_Type())
agentOspfAreaOpaqueLsdbLsid.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbLsid.setStatus(_A)
_AgentOspfAreaOpaqueLsdbRouterId_Type=IpAddress
_AgentOspfAreaOpaqueLsdbRouterId_Object=MibTableColumn
agentOspfAreaOpaqueLsdbRouterId=_AgentOspfAreaOpaqueLsdbRouterId_Object((1,3,6,1,4,1,7244,2,2,4,16,1,4),_AgentOspfAreaOpaqueLsdbRouterId_Type())
agentOspfAreaOpaqueLsdbRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbRouterId.setStatus(_A)
_AgentOspfAreaOpaqueLsdbSequence_Type=Integer32
_AgentOspfAreaOpaqueLsdbSequence_Object=MibTableColumn
agentOspfAreaOpaqueLsdbSequence=_AgentOspfAreaOpaqueLsdbSequence_Object((1,3,6,1,4,1,7244,2,2,4,16,1,5),_AgentOspfAreaOpaqueLsdbSequence_Type())
agentOspfAreaOpaqueLsdbSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbSequence.setStatus(_A)
_AgentOspfAreaOpaqueLsdbAge_Type=Integer32
_AgentOspfAreaOpaqueLsdbAge_Object=MibTableColumn
agentOspfAreaOpaqueLsdbAge=_AgentOspfAreaOpaqueLsdbAge_Object((1,3,6,1,4,1,7244,2,2,4,16,1,6),_AgentOspfAreaOpaqueLsdbAge_Type())
agentOspfAreaOpaqueLsdbAge.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbAge.setUnits(_Z)
_AgentOspfAreaOpaqueLsdbChecksum_Type=Integer32
_AgentOspfAreaOpaqueLsdbChecksum_Object=MibTableColumn
agentOspfAreaOpaqueLsdbChecksum=_AgentOspfAreaOpaqueLsdbChecksum_Object((1,3,6,1,4,1,7244,2,2,4,16,1,7),_AgentOspfAreaOpaqueLsdbChecksum_Type())
agentOspfAreaOpaqueLsdbChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbChecksum.setStatus(_A)
class _AgentOspfAreaOpaqueLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_AgentOspfAreaOpaqueLsdbAdvertisement_Type.__name__=_K
_AgentOspfAreaOpaqueLsdbAdvertisement_Object=MibTableColumn
agentOspfAreaOpaqueLsdbAdvertisement=_AgentOspfAreaOpaqueLsdbAdvertisement_Object((1,3,6,1,4,1,7244,2,2,4,16,1,8),_AgentOspfAreaOpaqueLsdbAdvertisement_Type())
agentOspfAreaOpaqueLsdbAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbAdvertisement.setStatus(_A)
_AgentOspfLocalLsdbTable_Object=MibTable
agentOspfLocalLsdbTable=_AgentOspfLocalLsdbTable_Object((1,3,6,1,4,1,7244,2,2,4,17))
if mibBuilder.loadTexts:agentOspfLocalLsdbTable.setStatus(_A)
_AgentOspfLocalLsdbEntry_Object=MibTableRow
agentOspfLocalLsdbEntry=_AgentOspfLocalLsdbEntry_Object((1,3,6,1,4,1,7244,2,2,4,17,1))
agentOspfLocalLsdbEntry.setIndexNames((0,_E,_y),(0,_E,_z),(0,_E,_A0),(0,_E,_A1),(0,_E,_A2))
if mibBuilder.loadTexts:agentOspfLocalLsdbEntry.setStatus(_A)
_AgentOspfLocalLsdbIpAddress_Type=IpAddress
_AgentOspfLocalLsdbIpAddress_Object=MibTableColumn
agentOspfLocalLsdbIpAddress=_AgentOspfLocalLsdbIpAddress_Object((1,3,6,1,4,1,7244,2,2,4,17,1,1),_AgentOspfLocalLsdbIpAddress_Type())
agentOspfLocalLsdbIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfLocalLsdbIpAddress.setStatus(_A)
_AgentOspfLocalLsdbAddressLessIf_Type=InterfaceIndexOrZero
_AgentOspfLocalLsdbAddressLessIf_Object=MibTableColumn
agentOspfLocalLsdbAddressLessIf=_AgentOspfLocalLsdbAddressLessIf_Object((1,3,6,1,4,1,7244,2,2,4,17,1,2),_AgentOspfLocalLsdbAddressLessIf_Type())
agentOspfLocalLsdbAddressLessIf.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfLocalLsdbAddressLessIf.setStatus(_A)
class _AgentOspfLocalLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(9));namedValues=NamedValues(('localOpaqueLink',9))
_AgentOspfLocalLsdbType_Type.__name__=_C
_AgentOspfLocalLsdbType_Object=MibTableColumn
agentOspfLocalLsdbType=_AgentOspfLocalLsdbType_Object((1,3,6,1,4,1,7244,2,2,4,17,1,3),_AgentOspfLocalLsdbType_Type())
agentOspfLocalLsdbType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfLocalLsdbType.setStatus(_A)
_AgentOspfLocalLsdbLsid_Type=IpAddress
_AgentOspfLocalLsdbLsid_Object=MibTableColumn
agentOspfLocalLsdbLsid=_AgentOspfLocalLsdbLsid_Object((1,3,6,1,4,1,7244,2,2,4,17,1,4),_AgentOspfLocalLsdbLsid_Type())
agentOspfLocalLsdbLsid.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfLocalLsdbLsid.setStatus(_A)
_AgentOspfLocalLsdbRouterId_Type=RouterID
_AgentOspfLocalLsdbRouterId_Object=MibTableColumn
agentOspfLocalLsdbRouterId=_AgentOspfLocalLsdbRouterId_Object((1,3,6,1,4,1,7244,2,2,4,17,1,5),_AgentOspfLocalLsdbRouterId_Type())
agentOspfLocalLsdbRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfLocalLsdbRouterId.setStatus(_A)
_AgentOspfLocalLsdbSequence_Type=Integer32
_AgentOspfLocalLsdbSequence_Object=MibTableColumn
agentOspfLocalLsdbSequence=_AgentOspfLocalLsdbSequence_Object((1,3,6,1,4,1,7244,2,2,4,17,1,6),_AgentOspfLocalLsdbSequence_Type())
agentOspfLocalLsdbSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfLocalLsdbSequence.setStatus(_A)
_AgentOspfLocalLsdbAge_Type=Integer32
_AgentOspfLocalLsdbAge_Object=MibTableColumn
agentOspfLocalLsdbAge=_AgentOspfLocalLsdbAge_Object((1,3,6,1,4,1,7244,2,2,4,17,1,7),_AgentOspfLocalLsdbAge_Type())
agentOspfLocalLsdbAge.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfLocalLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:agentOspfLocalLsdbAge.setUnits(_Z)
_AgentOspfLocalLsdbChecksum_Type=Integer32
_AgentOspfLocalLsdbChecksum_Object=MibTableColumn
agentOspfLocalLsdbChecksum=_AgentOspfLocalLsdbChecksum_Object((1,3,6,1,4,1,7244,2,2,4,17,1,8),_AgentOspfLocalLsdbChecksum_Type())
agentOspfLocalLsdbChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfLocalLsdbChecksum.setStatus(_A)
class _AgentOspfLocalLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_AgentOspfLocalLsdbAdvertisement_Type.__name__=_K
_AgentOspfLocalLsdbAdvertisement_Object=MibTableColumn
agentOspfLocalLsdbAdvertisement=_AgentOspfLocalLsdbAdvertisement_Object((1,3,6,1,4,1,7244,2,2,4,17,1,9),_AgentOspfLocalLsdbAdvertisement_Type())
agentOspfLocalLsdbAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfLocalLsdbAdvertisement.setStatus(_A)
_AgentOspfAsLsdbTable_Object=MibTable
agentOspfAsLsdbTable=_AgentOspfAsLsdbTable_Object((1,3,6,1,4,1,7244,2,2,4,18))
if mibBuilder.loadTexts:agentOspfAsLsdbTable.setStatus(_A)
_AgentOspfAsLsdbEntry_Object=MibTableRow
agentOspfAsLsdbEntry=_AgentOspfAsLsdbEntry_Object((1,3,6,1,4,1,7244,2,2,4,18,1))
agentOspfAsLsdbEntry.setIndexNames((0,_E,_A3),(0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:agentOspfAsLsdbEntry.setStatus(_A)
class _AgentOspfAsLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(11));namedValues=NamedValues(('asOpaqueLink',11))
_AgentOspfAsLsdbType_Type.__name__=_C
_AgentOspfAsLsdbType_Object=MibTableColumn
agentOspfAsLsdbType=_AgentOspfAsLsdbType_Object((1,3,6,1,4,1,7244,2,2,4,18,1,1),_AgentOspfAsLsdbType_Type())
agentOspfAsLsdbType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAsLsdbType.setStatus(_A)
_AgentOspfAsLsdbLsid_Type=IpAddress
_AgentOspfAsLsdbLsid_Object=MibTableColumn
agentOspfAsLsdbLsid=_AgentOspfAsLsdbLsid_Object((1,3,6,1,4,1,7244,2,2,4,18,1,2),_AgentOspfAsLsdbLsid_Type())
agentOspfAsLsdbLsid.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAsLsdbLsid.setStatus(_A)
_AgentOspfAsLsdbRouterId_Type=RouterID
_AgentOspfAsLsdbRouterId_Object=MibTableColumn
agentOspfAsLsdbRouterId=_AgentOspfAsLsdbRouterId_Object((1,3,6,1,4,1,7244,2,2,4,18,1,3),_AgentOspfAsLsdbRouterId_Type())
agentOspfAsLsdbRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAsLsdbRouterId.setStatus(_A)
_AgentOspfAsLsdbSequence_Type=Integer32
_AgentOspfAsLsdbSequence_Object=MibTableColumn
agentOspfAsLsdbSequence=_AgentOspfAsLsdbSequence_Object((1,3,6,1,4,1,7244,2,2,4,18,1,4),_AgentOspfAsLsdbSequence_Type())
agentOspfAsLsdbSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAsLsdbSequence.setStatus(_A)
_AgentOspfAsLsdbAge_Type=Integer32
_AgentOspfAsLsdbAge_Object=MibTableColumn
agentOspfAsLsdbAge=_AgentOspfAsLsdbAge_Object((1,3,6,1,4,1,7244,2,2,4,18,1,5),_AgentOspfAsLsdbAge_Type())
agentOspfAsLsdbAge.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAsLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:agentOspfAsLsdbAge.setUnits(_Z)
_AgentOspfAsLsdbChecksum_Type=Integer32
_AgentOspfAsLsdbChecksum_Object=MibTableColumn
agentOspfAsLsdbChecksum=_AgentOspfAsLsdbChecksum_Object((1,3,6,1,4,1,7244,2,2,4,18,1,6),_AgentOspfAsLsdbChecksum_Type())
agentOspfAsLsdbChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAsLsdbChecksum.setStatus(_A)
class _AgentOspfAsLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_AgentOspfAsLsdbAdvertisement_Type.__name__=_K
_AgentOspfAsLsdbAdvertisement_Object=MibTableColumn
agentOspfAsLsdbAdvertisement=_AgentOspfAsLsdbAdvertisement_Object((1,3,6,1,4,1,7244,2,2,4,18,1,7),_AgentOspfAsLsdbAdvertisement_Type())
agentOspfAsLsdbAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfAsLsdbAdvertisement.setStatus(_A)
class _AgentOspfDefaultPassiveMode_Type(TruthValue):defaultValue=2
_AgentOspfDefaultPassiveMode_Type.__name__=_L
_AgentOspfDefaultPassiveMode_Object=MibScalar
agentOspfDefaultPassiveMode=_AgentOspfDefaultPassiveMode_Object((1,3,6,1,4,1,7244,2,2,4,19),_AgentOspfDefaultPassiveMode_Type())
agentOspfDefaultPassiveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDefaultPassiveMode.setStatus(_A)
class _AgentOspfRoutePrefIntraArea_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentOspfRoutePrefIntraArea_Type.__name__=_C
_AgentOspfRoutePrefIntraArea_Object=MibScalar
agentOspfRoutePrefIntraArea=_AgentOspfRoutePrefIntraArea_Object((1,3,6,1,4,1,7244,2,2,4,20),_AgentOspfRoutePrefIntraArea_Type())
agentOspfRoutePrefIntraArea.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRoutePrefIntraArea.setStatus(_A)
class _AgentOspfRoutePrefInterArea_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentOspfRoutePrefInterArea_Type.__name__=_C
_AgentOspfRoutePrefInterArea_Object=MibScalar
agentOspfRoutePrefInterArea=_AgentOspfRoutePrefInterArea_Object((1,3,6,1,4,1,7244,2,2,4,21),_AgentOspfRoutePrefInterArea_Type())
agentOspfRoutePrefInterArea.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRoutePrefInterArea.setStatus(_A)
class _AgentOspfRoutePrefExternal_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentOspfRoutePrefExternal_Type.__name__=_C
_AgentOspfRoutePrefExternal_Object=MibScalar
agentOspfRoutePrefExternal=_AgentOspfRoutePrefExternal_Object((1,3,6,1,4,1,7244,2,2,4,22),_AgentOspfRoutePrefExternal_Type())
agentOspfRoutePrefExternal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRoutePrefExternal.setStatus(_A)
_AgentOspfNetworkAreaTable_Object=MibTable
agentOspfNetworkAreaTable=_AgentOspfNetworkAreaTable_Object((1,3,6,1,4,1,7244,2,2,4,23))
if mibBuilder.loadTexts:agentOspfNetworkAreaTable.setStatus(_A)
_AgentOspfNetworkAreaEntry_Object=MibTableRow
agentOspfNetworkAreaEntry=_AgentOspfNetworkAreaEntry_Object((1,3,6,1,4,1,7244,2,2,4,23,1))
agentOspfNetworkAreaEntry.setIndexNames((0,_E,_A6),(0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:agentOspfNetworkAreaEntry.setStatus(_A)
_AgentOspfNetworkAreaIpAddress_Type=IpAddress
_AgentOspfNetworkAreaIpAddress_Object=MibTableColumn
agentOspfNetworkAreaIpAddress=_AgentOspfNetworkAreaIpAddress_Object((1,3,6,1,4,1,7244,2,2,4,23,1,1),_AgentOspfNetworkAreaIpAddress_Type())
agentOspfNetworkAreaIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfNetworkAreaIpAddress.setStatus(_A)
_AgentOspfNetworkAreaWildcardMask_Type=IpAddress
_AgentOspfNetworkAreaWildcardMask_Object=MibTableColumn
agentOspfNetworkAreaWildcardMask=_AgentOspfNetworkAreaWildcardMask_Object((1,3,6,1,4,1,7244,2,2,4,23,1,2),_AgentOspfNetworkAreaWildcardMask_Type())
agentOspfNetworkAreaWildcardMask.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfNetworkAreaWildcardMask.setStatus(_A)
_AgentOspfNetworkAreaId_Type=IpAddress
_AgentOspfNetworkAreaId_Object=MibTableColumn
agentOspfNetworkAreaId=_AgentOspfNetworkAreaId_Object((1,3,6,1,4,1,7244,2,2,4,23,1,3),_AgentOspfNetworkAreaId_Type())
agentOspfNetworkAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfNetworkAreaId.setStatus(_A)
_AgentOspfNetworkAreaRowStatus_Type=RowStatus
_AgentOspfNetworkAreaRowStatus_Object=MibTableColumn
agentOspfNetworkAreaRowStatus=_AgentOspfNetworkAreaRowStatus_Object((1,3,6,1,4,1,7244,2,2,4,23,1,4),_AgentOspfNetworkAreaRowStatus_Type())
agentOspfNetworkAreaRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentOspfNetworkAreaRowStatus.setStatus(_A)
_AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity=ObjectIdentity
agentSnmpTrapFlagsConfigGroupLayer3=_AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity((1,3,6,1,4,1,7244,2,2,5))
class _AgentSnmpVRRPNewMasterTrapFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSnmpVRRPNewMasterTrapFlag_Type.__name__=_C
_AgentSnmpVRRPNewMasterTrapFlag_Object=MibScalar
agentSnmpVRRPNewMasterTrapFlag=_AgentSnmpVRRPNewMasterTrapFlag_Object((1,3,6,1,4,1,7244,2,2,5,1),_AgentSnmpVRRPNewMasterTrapFlag_Type())
agentSnmpVRRPNewMasterTrapFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSnmpVRRPNewMasterTrapFlag.setStatus(_A)
class _AgentSnmpVRRPAuthFailureTrapFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSnmpVRRPAuthFailureTrapFlag_Type.__name__=_C
_AgentSnmpVRRPAuthFailureTrapFlag_Object=MibScalar
agentSnmpVRRPAuthFailureTrapFlag=_AgentSnmpVRRPAuthFailureTrapFlag_Object((1,3,6,1,4,1,7244,2,2,5,2),_AgentSnmpVRRPAuthFailureTrapFlag_Type())
agentSnmpVRRPAuthFailureTrapFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSnmpVRRPAuthFailureTrapFlag.setStatus(_A)
_AgentBootpDhcpRelayGroup_ObjectIdentity=ObjectIdentity
agentBootpDhcpRelayGroup=_AgentBootpDhcpRelayGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,6))
class _AgentBootpDhcpRelayMaxHopCount_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AgentBootpDhcpRelayMaxHopCount_Type.__name__=_C
_AgentBootpDhcpRelayMaxHopCount_Object=MibScalar
agentBootpDhcpRelayMaxHopCount=_AgentBootpDhcpRelayMaxHopCount_Object((1,3,6,1,4,1,7244,2,2,6,1),_AgentBootpDhcpRelayMaxHopCount_Type())
agentBootpDhcpRelayMaxHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayMaxHopCount.setStatus(_A)
class _AgentBootpDhcpRelayForwardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentBootpDhcpRelayForwardMode_Type.__name__=_C
_AgentBootpDhcpRelayForwardMode_Object=MibScalar
agentBootpDhcpRelayForwardMode=_AgentBootpDhcpRelayForwardMode_Object((1,3,6,1,4,1,7244,2,2,6,3),_AgentBootpDhcpRelayForwardMode_Type())
agentBootpDhcpRelayForwardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayForwardMode.setStatus(_F)
class _AgentBootpDhcpRelayMinWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AgentBootpDhcpRelayMinWaitTime_Type.__name__=_C
_AgentBootpDhcpRelayMinWaitTime_Object=MibScalar
agentBootpDhcpRelayMinWaitTime=_AgentBootpDhcpRelayMinWaitTime_Object((1,3,6,1,4,1,7244,2,2,6,4),_AgentBootpDhcpRelayMinWaitTime_Type())
agentBootpDhcpRelayMinWaitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayMinWaitTime.setStatus(_A)
class _AgentBootpDhcpRelayCircuitIdOptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentBootpDhcpRelayCircuitIdOptionMode_Type.__name__=_C
_AgentBootpDhcpRelayCircuitIdOptionMode_Object=MibScalar
agentBootpDhcpRelayCircuitIdOptionMode=_AgentBootpDhcpRelayCircuitIdOptionMode_Object((1,3,6,1,4,1,7244,2,2,6,5),_AgentBootpDhcpRelayCircuitIdOptionMode_Type())
agentBootpDhcpRelayCircuitIdOptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayCircuitIdOptionMode.setStatus(_A)
_AgentBootpDhcpRelayNumOfRequestsReceived_Type=Integer32
_AgentBootpDhcpRelayNumOfRequestsReceived_Object=MibScalar
agentBootpDhcpRelayNumOfRequestsReceived=_AgentBootpDhcpRelayNumOfRequestsReceived_Object((1,3,6,1,4,1,7244,2,2,6,6),_AgentBootpDhcpRelayNumOfRequestsReceived_Type())
agentBootpDhcpRelayNumOfRequestsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:agentBootpDhcpRelayNumOfRequestsReceived.setStatus(_F)
_AgentBootpDhcpRelayNumOfRequestsForwarded_Type=Integer32
_AgentBootpDhcpRelayNumOfRequestsForwarded_Object=MibScalar
agentBootpDhcpRelayNumOfRequestsForwarded=_AgentBootpDhcpRelayNumOfRequestsForwarded_Object((1,3,6,1,4,1,7244,2,2,6,7),_AgentBootpDhcpRelayNumOfRequestsForwarded_Type())
agentBootpDhcpRelayNumOfRequestsForwarded.setMaxAccess(_D)
if mibBuilder.loadTexts:agentBootpDhcpRelayNumOfRequestsForwarded.setStatus(_F)
_AgentBootpDhcpRelayNumOfDiscards_Type=Integer32
_AgentBootpDhcpRelayNumOfDiscards_Object=MibScalar
agentBootpDhcpRelayNumOfDiscards=_AgentBootpDhcpRelayNumOfDiscards_Object((1,3,6,1,4,1,7244,2,2,6,8),_AgentBootpDhcpRelayNumOfDiscards_Type())
agentBootpDhcpRelayNumOfDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:agentBootpDhcpRelayNumOfDiscards.setStatus(_F)
_AgentECMPGroup_ObjectIdentity=ObjectIdentity
agentECMPGroup=_AgentECMPGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,7))
class _AgentECMPOspfMaxPaths_Type(Integer32):defaultValue=4
_AgentECMPOspfMaxPaths_Type.__name__=_C
_AgentECMPOspfMaxPaths_Object=MibScalar
agentECMPOspfMaxPaths=_AgentECMPOspfMaxPaths_Object((1,3,6,1,4,1,7244,2,2,7,1),_AgentECMPOspfMaxPaths_Type())
agentECMPOspfMaxPaths.setMaxAccess(_B)
if mibBuilder.loadTexts:agentECMPOspfMaxPaths.setStatus(_A)
_AgentRouterVrrpConfigGroup_ObjectIdentity=ObjectIdentity
agentRouterVrrpConfigGroup=_AgentRouterVrrpConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,8))
class _AgentRouterVrrpAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentRouterVrrpAdminState_Type.__name__=_C
_AgentRouterVrrpAdminState_Object=MibScalar
agentRouterVrrpAdminState=_AgentRouterVrrpAdminState_Object((1,3,6,1,4,1,7244,2,2,8,1),_AgentRouterVrrpAdminState_Type())
agentRouterVrrpAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterVrrpAdminState.setStatus(_A)
_AgentRouterVrrpConfiguredTable_Object=MibTable
agentRouterVrrpConfiguredTable=_AgentRouterVrrpConfiguredTable_Object((1,3,6,1,4,1,7244,2,2,8,2))
if mibBuilder.loadTexts:agentRouterVrrpConfiguredTable.setStatus(_A)
_AgentRouterVrrpConfiguredEntry_Object=MibTableRow
agentRouterVrrpConfiguredEntry=_AgentRouterVrrpConfiguredEntry_Object((1,3,6,1,4,1,7244,2,2,8,2,1))
agentRouterVrrpConfiguredEntry.setIndexNames((0,_Q,_R),(0,_T,_U))
if mibBuilder.loadTexts:agentRouterVrrpConfiguredEntry.setStatus(_A)
class _AgentRouterVrrpConfiguredPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AgentRouterVrrpConfiguredPriority_Type.__name__=_C
_AgentRouterVrrpConfiguredPriority_Object=MibTableColumn
agentRouterVrrpConfiguredPriority=_AgentRouterVrrpConfiguredPriority_Object((1,3,6,1,4,1,7244,2,2,8,2,1,1),_AgentRouterVrrpConfiguredPriority_Type())
agentRouterVrrpConfiguredPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRouterVrrpConfiguredPriority.setStatus(_A)
_AgentVrrpOperations_ObjectIdentity=ObjectIdentity
agentVrrpOperations=_AgentVrrpOperations_ObjectIdentity((1,3,6,1,4,1,7244,2,2,9))
_AgentRouterVrrpOperTable_Object=MibTable
agentRouterVrrpOperTable=_AgentRouterVrrpOperTable_Object((1,3,6,1,4,1,7244,2,2,9,1))
if mibBuilder.loadTexts:agentRouterVrrpOperTable.setStatus(_F)
_AgentRouterVrrpOperEntry_Object=MibTableRow
agentRouterVrrpOperEntry=_AgentRouterVrrpOperEntry_Object((1,3,6,1,4,1,7244,2,2,9,1,1))
agentRouterVrrpOperEntry.setIndexNames((0,_Q,_R),(0,_T,_U))
if mibBuilder.loadTexts:agentRouterVrrpOperEntry.setStatus(_F)
class _AgentRouterVrrpOperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentRouterVrrpOperPriority_Type.__name__=_C
_AgentRouterVrrpOperPriority_Object=MibTableColumn
agentRouterVrrpOperPriority=_AgentRouterVrrpOperPriority_Object((1,3,6,1,4,1,7244,2,2,9,1,1,1),_AgentRouterVrrpOperPriority_Type())
agentRouterVrrpOperPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRouterVrrpOperPriority.setStatus(_F)
_AgentRouterVrrpTrackGroup_ObjectIdentity=ObjectIdentity
agentRouterVrrpTrackGroup=_AgentRouterVrrpTrackGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,10))
_AgentRouterVrrpTrackIntfTable_Object=MibTable
agentRouterVrrpTrackIntfTable=_AgentRouterVrrpTrackIntfTable_Object((1,3,6,1,4,1,7244,2,2,10,1))
if mibBuilder.loadTexts:agentRouterVrrpTrackIntfTable.setStatus(_A)
_AgentRouterVrrpTrackIntfEntry_Object=MibTableRow
agentRouterVrrpTrackIntfEntry=_AgentRouterVrrpTrackIntfEntry_Object((1,3,6,1,4,1,7244,2,2,10,1,1))
agentRouterVrrpTrackIntfEntry.setIndexNames((0,_Q,_R),(0,_T,_U),(0,_E,_A9))
if mibBuilder.loadTexts:agentRouterVrrpTrackIntfEntry.setStatus(_A)
_AgentRouterVrrpTrackIntf_Type=InterfaceIndex
_AgentRouterVrrpTrackIntf_Object=MibTableColumn
agentRouterVrrpTrackIntf=_AgentRouterVrrpTrackIntf_Object((1,3,6,1,4,1,7244,2,2,10,1,1,1),_AgentRouterVrrpTrackIntf_Type())
agentRouterVrrpTrackIntf.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackIntf.setStatus(_A)
class _AgentRouterVrrpTrackIfPrioDec_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AgentRouterVrrpTrackIfPrioDec_Type.__name__=_C
_AgentRouterVrrpTrackIfPrioDec_Object=MibTableColumn
agentRouterVrrpTrackIfPrioDec=_AgentRouterVrrpTrackIfPrioDec_Object((1,3,6,1,4,1,7244,2,2,10,1,1,2),_AgentRouterVrrpTrackIfPrioDec_Type())
agentRouterVrrpTrackIfPrioDec.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackIfPrioDec.setStatus(_A)
_AgentRouterVrrpTrackIfState_Type=TruthValue
_AgentRouterVrrpTrackIfState_Object=MibTableColumn
agentRouterVrrpTrackIfState=_AgentRouterVrrpTrackIfState_Object((1,3,6,1,4,1,7244,2,2,10,1,1,3),_AgentRouterVrrpTrackIfState_Type())
agentRouterVrrpTrackIfState.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRouterVrrpTrackIfState.setStatus(_A)
_AgentRouterVrrpTrackIfStatus_Type=RowStatus
_AgentRouterVrrpTrackIfStatus_Object=MibTableColumn
agentRouterVrrpTrackIfStatus=_AgentRouterVrrpTrackIfStatus_Object((1,3,6,1,4,1,7244,2,2,10,1,1,4),_AgentRouterVrrpTrackIfStatus_Type())
agentRouterVrrpTrackIfStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackIfStatus.setStatus(_A)
_AgentRouterVrrpTrackRouteTable_Object=MibTable
agentRouterVrrpTrackRouteTable=_AgentRouterVrrpTrackRouteTable_Object((1,3,6,1,4,1,7244,2,2,10,2))
if mibBuilder.loadTexts:agentRouterVrrpTrackRouteTable.setStatus(_A)
_AgentRouterVrrpTrackRouteEntry_Object=MibTableRow
agentRouterVrrpTrackRouteEntry=_AgentRouterVrrpTrackRouteEntry_Object((1,3,6,1,4,1,7244,2,2,10,2,1))
agentRouterVrrpTrackRouteEntry.setIndexNames((0,_Q,_R),(0,_T,_U),(0,_E,_AA),(0,_E,_AB))
if mibBuilder.loadTexts:agentRouterVrrpTrackRouteEntry.setStatus(_A)
_AgentRouterVrrpTrackRtPfx_Type=IpAddress
_AgentRouterVrrpTrackRtPfx_Object=MibTableColumn
agentRouterVrrpTrackRtPfx=_AgentRouterVrrpTrackRtPfx_Object((1,3,6,1,4,1,7244,2,2,10,2,1,1),_AgentRouterVrrpTrackRtPfx_Type())
agentRouterVrrpTrackRtPfx.setMaxAccess(_P)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtPfx.setStatus(_A)
class _AgentRouterVrrpTrackRtPfxLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AgentRouterVrrpTrackRtPfxLen_Type.__name__=_C
_AgentRouterVrrpTrackRtPfxLen_Object=MibTableColumn
agentRouterVrrpTrackRtPfxLen=_AgentRouterVrrpTrackRtPfxLen_Object((1,3,6,1,4,1,7244,2,2,10,2,1,2),_AgentRouterVrrpTrackRtPfxLen_Type())
agentRouterVrrpTrackRtPfxLen.setMaxAccess(_P)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtPfxLen.setStatus(_A)
class _AgentRouterVrrpTrackRtPrioDec_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AgentRouterVrrpTrackRtPrioDec_Type.__name__=_C
_AgentRouterVrrpTrackRtPrioDec_Object=MibTableColumn
agentRouterVrrpTrackRtPrioDec=_AgentRouterVrrpTrackRtPrioDec_Object((1,3,6,1,4,1,7244,2,2,10,2,1,3),_AgentRouterVrrpTrackRtPrioDec_Type())
agentRouterVrrpTrackRtPrioDec.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtPrioDec.setStatus(_A)
_AgentRouterVrrpTrackRtReachable_Type=TruthValue
_AgentRouterVrrpTrackRtReachable_Object=MibTableColumn
agentRouterVrrpTrackRtReachable=_AgentRouterVrrpTrackRtReachable_Object((1,3,6,1,4,1,7244,2,2,10,2,1,4),_AgentRouterVrrpTrackRtReachable_Type())
agentRouterVrrpTrackRtReachable.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtReachable.setStatus(_A)
_AgentRouterVrrpTrackRtStatus_Type=RowStatus
_AgentRouterVrrpTrackRtStatus_Object=MibTableColumn
agentRouterVrrpTrackRtStatus=_AgentRouterVrrpTrackRtStatus_Object((1,3,6,1,4,1,7244,2,2,10,2,1,5),_AgentRouterVrrpTrackRtStatus_Type())
agentRouterVrrpTrackRtStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtStatus.setStatus(_A)
_AgentIpHelperGroup_ObjectIdentity=ObjectIdentity
agentIpHelperGroup=_AgentIpHelperGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,11))
class _AgentIpHelperAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpHelperAdminMode_Type.__name__=_C
_AgentIpHelperAdminMode_Object=MibScalar
agentIpHelperAdminMode=_AgentIpHelperAdminMode_Object((1,3,6,1,4,1,7244,2,2,11,1),_AgentIpHelperAdminMode_Type())
agentIpHelperAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpHelperAdminMode.setStatus(_A)
_AgentDhcpClientMsgsReceived_Type=Counter32
_AgentDhcpClientMsgsReceived_Object=MibScalar
agentDhcpClientMsgsReceived=_AgentDhcpClientMsgsReceived_Object((1,3,6,1,4,1,7244,2,2,11,2),_AgentDhcpClientMsgsReceived_Type())
agentDhcpClientMsgsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcpClientMsgsReceived.setStatus(_A)
_AgentDhcpClientMsgsRelayed_Type=Counter32
_AgentDhcpClientMsgsRelayed_Object=MibScalar
agentDhcpClientMsgsRelayed=_AgentDhcpClientMsgsRelayed_Object((1,3,6,1,4,1,7244,2,2,11,3),_AgentDhcpClientMsgsRelayed_Type())
agentDhcpClientMsgsRelayed.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcpClientMsgsRelayed.setStatus(_A)
_AgentDhcpServerMsgsReceived_Type=Counter32
_AgentDhcpServerMsgsReceived_Object=MibScalar
agentDhcpServerMsgsReceived=_AgentDhcpServerMsgsReceived_Object((1,3,6,1,4,1,7244,2,2,11,4),_AgentDhcpServerMsgsReceived_Type())
agentDhcpServerMsgsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcpServerMsgsReceived.setStatus(_A)
_AgentDhcpServerMsgsRelayed_Type=Counter32
_AgentDhcpServerMsgsRelayed_Object=MibScalar
agentDhcpServerMsgsRelayed=_AgentDhcpServerMsgsRelayed_Object((1,3,6,1,4,1,7244,2,2,11,5),_AgentDhcpServerMsgsRelayed_Type())
agentDhcpServerMsgsRelayed.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcpServerMsgsRelayed.setStatus(_A)
_AgentUdpClientMsgsReceived_Type=Counter32
_AgentUdpClientMsgsReceived_Object=MibScalar
agentUdpClientMsgsReceived=_AgentUdpClientMsgsReceived_Object((1,3,6,1,4,1,7244,2,2,11,6),_AgentUdpClientMsgsReceived_Type())
agentUdpClientMsgsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:agentUdpClientMsgsReceived.setStatus(_A)
_AgentUdpClientMsgsRelayed_Type=Counter32
_AgentUdpClientMsgsRelayed_Object=MibScalar
agentUdpClientMsgsRelayed=_AgentUdpClientMsgsRelayed_Object((1,3,6,1,4,1,7244,2,2,11,7),_AgentUdpClientMsgsRelayed_Type())
agentUdpClientMsgsRelayed.setMaxAccess(_D)
if mibBuilder.loadTexts:agentUdpClientMsgsRelayed.setStatus(_A)
_AgentSwitchIpHelperAddressTable_Object=MibTable
agentSwitchIpHelperAddressTable=_AgentSwitchIpHelperAddressTable_Object((1,3,6,1,4,1,7244,2,2,11,8))
if mibBuilder.loadTexts:agentSwitchIpHelperAddressTable.setStatus(_A)
_AgentSwitchIpHelperAddressEntry_Object=MibTableRow
agentSwitchIpHelperAddressEntry=_AgentSwitchIpHelperAddressEntry_Object((1,3,6,1,4,1,7244,2,2,11,8,1))
agentSwitchIpHelperAddressEntry.setIndexNames((0,_E,_AC),(0,_E,_AD))
if mibBuilder.loadTexts:agentSwitchIpHelperAddressEntry.setStatus(_A)
_AgentSwitchIpHelperAddress_Type=IpAddress
_AgentSwitchIpHelperAddress_Object=MibTableColumn
agentSwitchIpHelperAddress=_AgentSwitchIpHelperAddress_Object((1,3,6,1,4,1,7244,2,2,11,8,1,1),_AgentSwitchIpHelperAddress_Type())
agentSwitchIpHelperAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpHelperAddress.setStatus(_A)
class _AgentSwitchIpHelperUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentSwitchIpHelperUdpPort_Type.__name__=_J
_AgentSwitchIpHelperUdpPort_Object=MibTableColumn
agentSwitchIpHelperUdpPort=_AgentSwitchIpHelperUdpPort_Object((1,3,6,1,4,1,7244,2,2,11,8,1,2),_AgentSwitchIpHelperUdpPort_Type())
agentSwitchIpHelperUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpHelperUdpPort.setStatus(_A)
_AgentSwitchIpHelperHitCount_Type=Unsigned32
_AgentSwitchIpHelperHitCount_Object=MibTableColumn
agentSwitchIpHelperHitCount=_AgentSwitchIpHelperHitCount_Object((1,3,6,1,4,1,7244,2,2,11,8,1,3),_AgentSwitchIpHelperHitCount_Type())
agentSwitchIpHelperHitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchIpHelperHitCount.setStatus(_A)
_AgentSwitchIpHelperStatus_Type=RowStatus
_AgentSwitchIpHelperStatus_Object=MibTableColumn
agentSwitchIpHelperStatus=_AgentSwitchIpHelperStatus_Object((1,3,6,1,4,1,7244,2,2,11,8,1,4),_AgentSwitchIpHelperStatus_Type())
agentSwitchIpHelperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIpHelperStatus.setStatus(_A)
_AgentUdpClientMsgsTtlExpired_Type=Counter32
_AgentUdpClientMsgsTtlExpired_Object=MibScalar
agentUdpClientMsgsTtlExpired=_AgentUdpClientMsgsTtlExpired_Object((1,3,6,1,4,1,7244,2,2,11,9),_AgentUdpClientMsgsTtlExpired_Type())
agentUdpClientMsgsTtlExpired.setMaxAccess(_D)
if mibBuilder.loadTexts:agentUdpClientMsgsTtlExpired.setStatus(_A)
_AgentUdpClientMsgsDiscarded_Type=Counter32
_AgentUdpClientMsgsDiscarded_Object=MibScalar
agentUdpClientMsgsDiscarded=_AgentUdpClientMsgsDiscarded_Object((1,3,6,1,4,1,7244,2,2,11,10),_AgentUdpClientMsgsDiscarded_Type())
agentUdpClientMsgsDiscarded.setMaxAccess(_D)
if mibBuilder.loadTexts:agentUdpClientMsgsDiscarded.setStatus(_A)
_AgentDhcpMsgHopCountExceededMax_Type=Counter32
_AgentDhcpMsgHopCountExceededMax_Object=MibScalar
agentDhcpMsgHopCountExceededMax=_AgentDhcpMsgHopCountExceededMax_Object((1,3,6,1,4,1,7244,2,2,11,11),_AgentDhcpMsgHopCountExceededMax_Type())
agentDhcpMsgHopCountExceededMax.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcpMsgHopCountExceededMax.setStatus(_A)
_AgentDhcpMsgWithSecsFieldBelowMin_Type=Counter32
_AgentDhcpMsgWithSecsFieldBelowMin_Object=MibScalar
agentDhcpMsgWithSecsFieldBelowMin=_AgentDhcpMsgWithSecsFieldBelowMin_Object((1,3,6,1,4,1,7244,2,2,11,12),_AgentDhcpMsgWithSecsFieldBelowMin_Type())
agentDhcpMsgWithSecsFieldBelowMin.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcpMsgWithSecsFieldBelowMin.setStatus(_A)
_AgentDhcpMsgWithGiaddrSetToLocalAddr_Type=Counter32
_AgentDhcpMsgWithGiaddrSetToLocalAddr_Object=MibScalar
agentDhcpMsgWithGiaddrSetToLocalAddr=_AgentDhcpMsgWithGiaddrSetToLocalAddr_Object((1,3,6,1,4,1,7244,2,2,11,13),_AgentDhcpMsgWithGiaddrSetToLocalAddr_Type())
agentDhcpMsgWithGiaddrSetToLocalAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcpMsgWithGiaddrSetToLocalAddr.setStatus(_A)
class _AgentIpHelperStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_AgentIpHelperStatisticsClear_Type.__name__=_C
_AgentIpHelperStatisticsClear_Object=MibScalar
agentIpHelperStatisticsClear=_AgentIpHelperStatisticsClear_Object((1,3,6,1,4,1,7244,2,2,11,20),_AgentIpHelperStatisticsClear_Type())
agentIpHelperStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpHelperStatisticsClear.setStatus(_A)
_AgentInternalVlanGroup_ObjectIdentity=ObjectIdentity
agentInternalVlanGroup=_AgentInternalVlanGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,12))
class _AgentInternalVlanBase_Type(Integer32):defaultValue=4093
_AgentInternalVlanBase_Type.__name__=_C
_AgentInternalVlanBase_Object=MibScalar
agentInternalVlanBase=_AgentInternalVlanBase_Object((1,3,6,1,4,1,7244,2,2,12,1),_AgentInternalVlanBase_Type())
agentInternalVlanBase.setMaxAccess(_B)
if mibBuilder.loadTexts:agentInternalVlanBase.setStatus(_A)
class _AgentInternalVlanPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ascending',0),('descending',1)))
_AgentInternalVlanPolicy_Type.__name__=_C
_AgentInternalVlanPolicy_Object=MibScalar
agentInternalVlanPolicy=_AgentInternalVlanPolicy_Object((1,3,6,1,4,1,7244,2,2,12,2),_AgentInternalVlanPolicy_Type())
agentInternalVlanPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:agentInternalVlanPolicy.setStatus(_A)
_AgentSwitchInternalVlanTable_Object=MibTable
agentSwitchInternalVlanTable=_AgentSwitchInternalVlanTable_Object((1,3,6,1,4,1,7244,2,2,12,3))
if mibBuilder.loadTexts:agentSwitchInternalVlanTable.setStatus(_A)
_AgentSwitchInternalVlanEntry_Object=MibTableRow
agentSwitchInternalVlanEntry=_AgentSwitchInternalVlanEntry_Object((1,3,6,1,4,1,7244,2,2,12,3,1))
agentSwitchInternalVlanEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:agentSwitchInternalVlanEntry.setStatus(_A)
class _AgentSwitchInternalVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchInternalVlanId_Type.__name__=_C
_AgentSwitchInternalVlanId_Object=MibTableColumn
agentSwitchInternalVlanId=_AgentSwitchInternalVlanId_Object((1,3,6,1,4,1,7244,2,2,12,3,1,1),_AgentSwitchInternalVlanId_Type())
agentSwitchInternalVlanId.setMaxAccess(_P)
if mibBuilder.loadTexts:agentSwitchInternalVlanId.setStatus(_A)
_AgentSwitchInternalVlanIfIndex_Type=Integer32
_AgentSwitchInternalVlanIfIndex_Object=MibTableColumn
agentSwitchInternalVlanIfIndex=_AgentSwitchInternalVlanIfIndex_Object((1,3,6,1,4,1,7244,2,2,12,3,1,2),_AgentSwitchInternalVlanIfIndex_Type())
agentSwitchInternalVlanIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchInternalVlanIfIndex.setStatus(_A)
_AgentRouterIsisConfigGroup_ObjectIdentity=ObjectIdentity
agentRouterIsisConfigGroup=_AgentRouterIsisConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,2,13))
_AgentRouterIsisConfigTable_Object=MibTable
agentRouterIsisConfigTable=_AgentRouterIsisConfigTable_Object((1,3,6,1,4,1,7244,2,2,13,1))
if mibBuilder.loadTexts:agentRouterIsisConfigTable.setStatus(_A)
_AgentRouterIsisConfigEntry_Object=MibTableRow
agentRouterIsisConfigEntry=_AgentRouterIsisConfigEntry_Object((1,3,6,1,4,1,7244,2,2,13,1,1))
agentRouterIsisConfigEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:agentRouterIsisConfigEntry.setStatus(_A)
_AgentRouterIsisConfigAreaIndex_Type=Unsigned32
_AgentRouterIsisConfigAreaIndex_Object=MibTableColumn
agentRouterIsisConfigAreaIndex=_AgentRouterIsisConfigAreaIndex_Object((1,3,6,1,4,1,7244,2,2,13,1,1,1),_AgentRouterIsisConfigAreaIndex_Type())
agentRouterIsisConfigAreaIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterIsisConfigAreaIndex.setStatus(_A)
class _AgentRouterIsisConfigAreaTag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AgentRouterIsisConfigAreaTag_Type.__name__=_K
_AgentRouterIsisConfigAreaTag_Object=MibTableColumn
agentRouterIsisConfigAreaTag=_AgentRouterIsisConfigAreaTag_Object((1,3,6,1,4,1,7244,2,2,13,1,1,2),_AgentRouterIsisConfigAreaTag_Type())
agentRouterIsisConfigAreaTag.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterIsisConfigAreaTag.setStatus(_A)
_AgentRouterIsisConfigSpfLevel1Interval_Type=Unsigned32
_AgentRouterIsisConfigSpfLevel1Interval_Object=MibTableColumn
agentRouterIsisConfigSpfLevel1Interval=_AgentRouterIsisConfigSpfLevel1Interval_Object((1,3,6,1,4,1,7244,2,2,13,1,1,3),_AgentRouterIsisConfigSpfLevel1Interval_Type())
agentRouterIsisConfigSpfLevel1Interval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigSpfLevel1Interval.setStatus(_A)
_AgentRouterIsisConfigSpfLevel2Interval_Type=Unsigned32
_AgentRouterIsisConfigSpfLevel2Interval_Object=MibTableColumn
agentRouterIsisConfigSpfLevel2Interval=_AgentRouterIsisConfigSpfLevel2Interval_Object((1,3,6,1,4,1,7244,2,2,13,1,1,4),_AgentRouterIsisConfigSpfLevel2Interval_Type())
agentRouterIsisConfigSpfLevel2Interval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigSpfLevel2Interval.setStatus(_A)
_AgentRouterIsisConfigLspLifeTimeInterval_Type=Unsigned32
_AgentRouterIsisConfigLspLifeTimeInterval_Object=MibTableColumn
agentRouterIsisConfigLspLifeTimeInterval=_AgentRouterIsisConfigLspLifeTimeInterval_Object((1,3,6,1,4,1,7244,2,2,13,1,1,5),_AgentRouterIsisConfigLspLifeTimeInterval_Type())
agentRouterIsisConfigLspLifeTimeInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigLspLifeTimeInterval.setStatus(_F)
_AgentRouterIsisConfigLspRefreshTimeInterval_Type=Unsigned32
_AgentRouterIsisConfigLspRefreshTimeInterval_Object=MibTableColumn
agentRouterIsisConfigLspRefreshTimeInterval=_AgentRouterIsisConfigLspRefreshTimeInterval_Object((1,3,6,1,4,1,7244,2,2,13,1,1,6),_AgentRouterIsisConfigLspRefreshTimeInterval_Type())
agentRouterIsisConfigLspRefreshTimeInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigLspRefreshTimeInterval.setStatus(_F)
_AgentRouterIsisConfigGenaralInterval1TimeInterval_Type=Unsigned32
_AgentRouterIsisConfigGenaralInterval1TimeInterval_Object=MibTableColumn
agentRouterIsisConfigGenaralInterval1TimeInterval=_AgentRouterIsisConfigGenaralInterval1TimeInterval_Object((1,3,6,1,4,1,7244,2,2,13,1,1,7),_AgentRouterIsisConfigGenaralInterval1TimeInterval_Type())
agentRouterIsisConfigGenaralInterval1TimeInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigGenaralInterval1TimeInterval.setStatus(_F)
_AgentRouterIsisConfigGenaralInterval2TimeInterval_Type=Unsigned32
_AgentRouterIsisConfigGenaralInterval2TimeInterval_Object=MibTableColumn
agentRouterIsisConfigGenaralInterval2TimeInterval=_AgentRouterIsisConfigGenaralInterval2TimeInterval_Object((1,3,6,1,4,1,7244,2,2,13,1,1,8),_AgentRouterIsisConfigGenaralInterval2TimeInterval_Type())
agentRouterIsisConfigGenaralInterval2TimeInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigGenaralInterval2TimeInterval.setStatus(_F)
class _AgentRouterIsisConfigIsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('level1',1),('level2',2),('level12',3)))
_AgentRouterIsisConfigIsType_Type.__name__=_C
_AgentRouterIsisConfigIsType_Object=MibTableColumn
agentRouterIsisConfigIsType=_AgentRouterIsisConfigIsType_Object((1,3,6,1,4,1,7244,2,2,13,1,1,9),_AgentRouterIsisConfigIsType_Type())
agentRouterIsisConfigIsType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigIsType.setStatus(_F)
class _AgentRouterIsisConfigMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('narrow',0),('wide',1),('transition',2)))
_AgentRouterIsisConfigMetricType_Type.__name__=_C
_AgentRouterIsisConfigMetricType_Object=MibTableColumn
agentRouterIsisConfigMetricType=_AgentRouterIsisConfigMetricType_Object((1,3,6,1,4,1,7244,2,2,13,1,1,10),_AgentRouterIsisConfigMetricType_Type())
agentRouterIsisConfigMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigMetricType.setStatus(_F)
class _AgentRouterIsisConfigHostname_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_AgentRouterIsisConfigHostname_Type.__name__=_C
_AgentRouterIsisConfigHostname_Object=MibTableColumn
agentRouterIsisConfigHostname=_AgentRouterIsisConfigHostname_Object((1,3,6,1,4,1,7244,2,2,13,1,1,11),_AgentRouterIsisConfigHostname_Type())
agentRouterIsisConfigHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigHostname.setStatus(_F)
_AgentRouterIsisConfigDistant_Type=Unsigned32
_AgentRouterIsisConfigDistant_Object=MibTableColumn
agentRouterIsisConfigDistant=_AgentRouterIsisConfigDistant_Object((1,3,6,1,4,1,7244,2,2,13,1,1,12),_AgentRouterIsisConfigDistant_Type())
agentRouterIsisConfigDistant.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigDistant.setStatus(_F)
_AgentRouterIsisConfigDefaultMetric_Type=Unsigned32
_AgentRouterIsisConfigDefaultMetric_Object=MibTableColumn
agentRouterIsisConfigDefaultMetric=_AgentRouterIsisConfigDefaultMetric_Object((1,3,6,1,4,1,7244,2,2,13,1,1,13),_AgentRouterIsisConfigDefaultMetric_Type())
agentRouterIsisConfigDefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigDefaultMetric.setStatus(_F)
class _AgentRouterIsisConfigDefaultInformation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_AgentRouterIsisConfigDefaultInformation_Type.__name__=_C
_AgentRouterIsisConfigDefaultInformation_Object=MibTableColumn
agentRouterIsisConfigDefaultInformation=_AgentRouterIsisConfigDefaultInformation_Object((1,3,6,1,4,1,7244,2,2,13,1,1,14),_AgentRouterIsisConfigDefaultInformation_Type())
agentRouterIsisConfigDefaultInformation.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigDefaultInformation.setStatus(_F)
class _AgentRouterIsisConfigDomainPasswoad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_AgentRouterIsisConfigDomainPasswoad_Type.__name__=_K
_AgentRouterIsisConfigDomainPasswoad_Object=MibTableColumn
agentRouterIsisConfigDomainPasswoad=_AgentRouterIsisConfigDomainPasswoad_Object((1,3,6,1,4,1,7244,2,2,13,1,1,15),_AgentRouterIsisConfigDomainPasswoad_Type())
agentRouterIsisConfigDomainPasswoad.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterIsisConfigDomainPasswoad.setStatus(_A)
class _AgentRouterIsisConfigDomainPasswoadAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_S,0),(_b,1),(_c,3)))
_AgentRouterIsisConfigDomainPasswoadAuthType_Type.__name__=_C
_AgentRouterIsisConfigDomainPasswoadAuthType_Object=MibTableColumn
agentRouterIsisConfigDomainPasswoadAuthType=_AgentRouterIsisConfigDomainPasswoadAuthType_Object((1,3,6,1,4,1,7244,2,2,13,1,1,16),_AgentRouterIsisConfigDomainPasswoadAuthType_Type())
agentRouterIsisConfigDomainPasswoadAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigDomainPasswoadAuthType.setStatus(_F)
class _AgentRouterIsisConfigAreaPasswoad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_AgentRouterIsisConfigAreaPasswoad_Type.__name__=_K
_AgentRouterIsisConfigAreaPasswoad_Object=MibTableColumn
agentRouterIsisConfigAreaPasswoad=_AgentRouterIsisConfigAreaPasswoad_Object((1,3,6,1,4,1,7244,2,2,13,1,1,17),_AgentRouterIsisConfigAreaPasswoad_Type())
agentRouterIsisConfigAreaPasswoad.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterIsisConfigAreaPasswoad.setStatus(_A)
class _AgentRouterIsisConfigAreaPasswoadAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_S,0),(_b,1),(_c,3)))
_AgentRouterIsisConfigAreaPasswoadAuthType_Type.__name__=_C
_AgentRouterIsisConfigAreaPasswoadAuthType_Object=MibTableColumn
agentRouterIsisConfigAreaPasswoadAuthType=_AgentRouterIsisConfigAreaPasswoadAuthType_Object((1,3,6,1,4,1,7244,2,2,13,1,1,18),_AgentRouterIsisConfigAreaPasswoadAuthType_Type())
agentRouterIsisConfigAreaPasswoadAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigAreaPasswoadAuthType.setStatus(_F)
class _AgentRouterIsisConfigAreaNET1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_AgentRouterIsisConfigAreaNET1_Type.__name__=_K
_AgentRouterIsisConfigAreaNET1_Object=MibTableColumn
agentRouterIsisConfigAreaNET1=_AgentRouterIsisConfigAreaNET1_Object((1,3,6,1,4,1,7244,2,2,13,1,1,19),_AgentRouterIsisConfigAreaNET1_Type())
agentRouterIsisConfigAreaNET1.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterIsisConfigAreaNET1.setStatus(_A)
class _AgentRouterIsisConfigAreaNET2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_AgentRouterIsisConfigAreaNET2_Type.__name__=_K
_AgentRouterIsisConfigAreaNET2_Object=MibTableColumn
agentRouterIsisConfigAreaNET2=_AgentRouterIsisConfigAreaNET2_Object((1,3,6,1,4,1,7244,2,2,13,1,1,20),_AgentRouterIsisConfigAreaNET2_Type())
agentRouterIsisConfigAreaNET2.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterIsisConfigAreaNET2.setStatus(_A)
class _AgentRouterIsisConfigAreaNET3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_AgentRouterIsisConfigAreaNET3_Type.__name__=_K
_AgentRouterIsisConfigAreaNET3_Object=MibTableColumn
agentRouterIsisConfigAreaNET3=_AgentRouterIsisConfigAreaNET3_Object((1,3,6,1,4,1,7244,2,2,13,1,1,21),_AgentRouterIsisConfigAreaNET3_Type())
agentRouterIsisConfigAreaNET3.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterIsisConfigAreaNET3.setStatus(_A)
_AgentRouterIsisConfigStatus_Type=RowStatus
_AgentRouterIsisConfigStatus_Object=MibTableColumn
agentRouterIsisConfigStatus=_AgentRouterIsisConfigStatus_Object((1,3,6,1,4,1,7244,2,2,13,1,1,22),_AgentRouterIsisConfigStatus_Type())
agentRouterIsisConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterIsisConfigStatus.setStatus(_F)
_AgentIsisRouteRedistTable_Object=MibTable
agentIsisRouteRedistTable=_AgentIsisRouteRedistTable_Object((1,3,6,1,4,1,7244,2,2,13,2))
if mibBuilder.loadTexts:agentIsisRouteRedistTable.setStatus(_A)
_AgentIsisRouteRedistEntry_Object=MibTableRow
agentIsisRouteRedistEntry=_AgentIsisRouteRedistEntry_Object((1,3,6,1,4,1,7244,2,2,13,2,1))
agentIsisRouteRedistEntry.setIndexNames((0,_E,_a),(0,_E,_AF))
if mibBuilder.loadTexts:agentIsisRouteRedistEntry.setStatus(_A)
class _AgentIsisRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_V,2),('ospf',3),('rip',4)))
_AgentIsisRouteRedistSource_Type.__name__=_C
_AgentIsisRouteRedistSource_Object=MibTableColumn
agentIsisRouteRedistSource=_AgentIsisRouteRedistSource_Object((1,3,6,1,4,1,7244,2,2,13,2,1,1),_AgentIsisRouteRedistSource_Type())
agentIsisRouteRedistSource.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIsisRouteRedistSource.setStatus(_A)
class _AgentIsisRouteRedistMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIsisRouteRedistMode_Type.__name__=_C
_AgentIsisRouteRedistMode_Object=MibTableColumn
agentIsisRouteRedistMode=_AgentIsisRouteRedistMode_Object((1,3,6,1,4,1,7244,2,2,13,2,1,2),_AgentIsisRouteRedistMode_Type())
agentIsisRouteRedistMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistMode.setStatus(_A)
class _AgentIsisRouteRedistMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16777214))
_AgentIsisRouteRedistMetric_Type.__name__=_C
_AgentIsisRouteRedistMetric_Object=MibTableColumn
agentIsisRouteRedistMetric=_AgentIsisRouteRedistMetric_Object((1,3,6,1,4,1,7244,2,2,13,2,1,3),_AgentIsisRouteRedistMetric_Type())
agentIsisRouteRedistMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistMetric.setStatus(_A)
class _AgentIsisRouteRedistMetricConfigured_Type(TruthValue):defaultValue=2
_AgentIsisRouteRedistMetricConfigured_Type.__name__=_L
_AgentIsisRouteRedistMetricConfigured_Object=MibTableColumn
agentIsisRouteRedistMetricConfigured=_AgentIsisRouteRedistMetricConfigured_Object((1,3,6,1,4,1,7244,2,2,13,2,1,4),_AgentIsisRouteRedistMetricConfigured_Type())
agentIsisRouteRedistMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistMetricConfigured.setStatus(_A)
class _AgentIsisRouteRedistMatchInternal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentIsisRouteRedistMatchInternal_Type.__name__=_C
_AgentIsisRouteRedistMatchInternal_Object=MibTableColumn
agentIsisRouteRedistMatchInternal=_AgentIsisRouteRedistMatchInternal_Object((1,3,6,1,4,1,7244,2,2,13,2,1,5),_AgentIsisRouteRedistMatchInternal_Type())
agentIsisRouteRedistMatchInternal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistMatchInternal.setStatus(_A)
class _AgentIsisRouteRedistMatchExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentIsisRouteRedistMatchExternal1_Type.__name__=_C
_AgentIsisRouteRedistMatchExternal1_Object=MibTableColumn
agentIsisRouteRedistMatchExternal1=_AgentIsisRouteRedistMatchExternal1_Object((1,3,6,1,4,1,7244,2,2,13,2,1,6),_AgentIsisRouteRedistMatchExternal1_Type())
agentIsisRouteRedistMatchExternal1.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistMatchExternal1.setStatus(_A)
class _AgentIsisRouteRedistMatchExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentIsisRouteRedistMatchExternal2_Type.__name__=_C
_AgentIsisRouteRedistMatchExternal2_Object=MibTableColumn
agentIsisRouteRedistMatchExternal2=_AgentIsisRouteRedistMatchExternal2_Object((1,3,6,1,4,1,7244,2,2,13,2,1,7),_AgentIsisRouteRedistMatchExternal2_Type())
agentIsisRouteRedistMatchExternal2.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistMatchExternal2.setStatus(_A)
class _AgentIsisRouteRedistMatchNSSAExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentIsisRouteRedistMatchNSSAExternal1_Type.__name__=_C
_AgentIsisRouteRedistMatchNSSAExternal1_Object=MibTableColumn
agentIsisRouteRedistMatchNSSAExternal1=_AgentIsisRouteRedistMatchNSSAExternal1_Object((1,3,6,1,4,1,7244,2,2,13,2,1,8),_AgentIsisRouteRedistMatchNSSAExternal1_Type())
agentIsisRouteRedistMatchNSSAExternal1.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistMatchNSSAExternal1.setStatus(_A)
class _AgentIsisRouteRedistMatchNSSAExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AgentIsisRouteRedistMatchNSSAExternal2_Type.__name__=_C
_AgentIsisRouteRedistMatchNSSAExternal2_Object=MibTableColumn
agentIsisRouteRedistMatchNSSAExternal2=_AgentIsisRouteRedistMatchNSSAExternal2_Object((1,3,6,1,4,1,7244,2,2,13,2,1,9),_AgentIsisRouteRedistMatchNSSAExternal2_Type())
agentIsisRouteRedistMatchNSSAExternal2.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistMatchNSSAExternal2.setStatus(_A)
class _AgentIsisRouteRedistDistList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_AgentIsisRouteRedistDistList_Type.__name__=_J
_AgentIsisRouteRedistDistList_Object=MibTableColumn
agentIsisRouteRedistDistList=_AgentIsisRouteRedistDistList_Object((1,3,6,1,4,1,7244,2,2,13,2,1,10),_AgentIsisRouteRedistDistList_Type())
agentIsisRouteRedistDistList.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistDistList.setStatus(_A)
_AgentIsisRouteRedistDistListConfigured_Type=TruthValue
_AgentIsisRouteRedistDistListConfigured_Object=MibTableColumn
agentIsisRouteRedistDistListConfigured=_AgentIsisRouteRedistDistListConfigured_Object((1,3,6,1,4,1,7244,2,2,13,2,1,11),_AgentIsisRouteRedistDistListConfigured_Type())
agentIsisRouteRedistDistListConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisRouteRedistDistListConfigured.setStatus(_A)
_AgentIsisConfigIfTable_Object=MibTable
agentIsisConfigIfTable=_AgentIsisConfigIfTable_Object((1,3,6,1,4,1,7244,2,2,13,3))
if mibBuilder.loadTexts:agentIsisConfigIfTable.setStatus(_A)
_AgentIsisConfigIfEntry_Object=MibTableRow
agentIsisConfigIfEntry=_AgentIsisConfigIfEntry_Object((1,3,6,1,4,1,7244,2,2,13,3,1))
agentIsisConfigIfEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:agentIsisConfigIfEntry.setStatus(_A)
class _AgentIsisConfigIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIsisConfigIfIndex_Type.__name__=_C
_AgentIsisConfigIfIndex_Object=MibTableColumn
agentIsisConfigIfIndex=_AgentIsisConfigIfIndex_Object((1,3,6,1,4,1,7244,2,2,13,3,1,1),_AgentIsisConfigIfIndex_Type())
agentIsisConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIsisConfigIfIndex.setStatus(_A)
_AgentIsisConfigIfArea_Type=OctetString
_AgentIsisConfigIfArea_Object=MibTableColumn
agentIsisConfigIfArea=_AgentIsisConfigIfArea_Object((1,3,6,1,4,1,7244,2,2,13,3,1,2),_AgentIsisConfigIfArea_Type())
agentIsisConfigIfArea.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIsisConfigIfArea.setStatus(_A)
class _AgentIsisConfigIfCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('level1',1),('level2',2),('level12',3)))
_AgentIsisConfigIfCircuitType_Type.__name__=_C
_AgentIsisConfigIfCircuitType_Object=MibTableColumn
agentIsisConfigIfCircuitType=_AgentIsisConfigIfCircuitType_Object((1,3,6,1,4,1,7244,2,2,13,3,1,3),_AgentIsisConfigIfCircuitType_Type())
agentIsisConfigIfCircuitType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfCircuitType.setStatus(_F)
class _AgentIsisConfigIfCSNPIntervalL1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentIsisConfigIfCSNPIntervalL1_Type.__name__=_J
_AgentIsisConfigIfCSNPIntervalL1_Object=MibTableColumn
agentIsisConfigIfCSNPIntervalL1=_AgentIsisConfigIfCSNPIntervalL1_Object((1,3,6,1,4,1,7244,2,2,13,3,1,4),_AgentIsisConfigIfCSNPIntervalL1_Type())
agentIsisConfigIfCSNPIntervalL1.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfCSNPIntervalL1.setStatus(_A)
class _AgentIsisConfigIfCSNPIntervalL2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentIsisConfigIfCSNPIntervalL2_Type.__name__=_J
_AgentIsisConfigIfCSNPIntervalL2_Object=MibTableColumn
agentIsisConfigIfCSNPIntervalL2=_AgentIsisConfigIfCSNPIntervalL2_Object((1,3,6,1,4,1,7244,2,2,13,3,1,5),_AgentIsisConfigIfCSNPIntervalL2_Type())
agentIsisConfigIfCSNPIntervalL2.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfCSNPIntervalL2.setStatus(_A)
class _AgentIsisConfigIfHelloIntervalL1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentIsisConfigIfHelloIntervalL1_Type.__name__=_J
_AgentIsisConfigIfHelloIntervalL1_Object=MibTableColumn
agentIsisConfigIfHelloIntervalL1=_AgentIsisConfigIfHelloIntervalL1_Object((1,3,6,1,4,1,7244,2,2,13,3,1,6),_AgentIsisConfigIfHelloIntervalL1_Type())
agentIsisConfigIfHelloIntervalL1.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfHelloIntervalL1.setStatus(_A)
class _AgentIsisConfigIfHelloIntervalL2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentIsisConfigIfHelloIntervalL2_Type.__name__=_J
_AgentIsisConfigIfHelloIntervalL2_Object=MibTableColumn
agentIsisConfigIfHelloIntervalL2=_AgentIsisConfigIfHelloIntervalL2_Object((1,3,6,1,4,1,7244,2,2,13,3,1,7),_AgentIsisConfigIfHelloIntervalL2_Type())
agentIsisConfigIfHelloIntervalL2.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfHelloIntervalL2.setStatus(_A)
class _AgentIsisConfigIfHelloMultiL1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1000))
_AgentIsisConfigIfHelloMultiL1_Type.__name__=_J
_AgentIsisConfigIfHelloMultiL1_Object=MibTableColumn
agentIsisConfigIfHelloMultiL1=_AgentIsisConfigIfHelloMultiL1_Object((1,3,6,1,4,1,7244,2,2,13,3,1,8),_AgentIsisConfigIfHelloMultiL1_Type())
agentIsisConfigIfHelloMultiL1.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfHelloMultiL1.setStatus(_A)
class _AgentIsisConfigIfHelloMultiL2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1000))
_AgentIsisConfigIfHelloMultiL2_Type.__name__=_J
_AgentIsisConfigIfHelloMultiL2_Object=MibTableColumn
agentIsisConfigIfHelloMultiL2=_AgentIsisConfigIfHelloMultiL2_Object((1,3,6,1,4,1,7244,2,2,13,3,1,9),_AgentIsisConfigIfHelloMultiL2_Type())
agentIsisConfigIfHelloMultiL2.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfHelloMultiL2.setStatus(_A)
class _AgentIsisConfigIfHelloPad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_AgentIsisConfigIfHelloPad_Type.__name__=_C
_AgentIsisConfigIfHelloPad_Object=MibTableColumn
agentIsisConfigIfHelloPad=_AgentIsisConfigIfHelloPad_Object((1,3,6,1,4,1,7244,2,2,13,3,1,10),_AgentIsisConfigIfHelloPad_Type())
agentIsisConfigIfHelloPad.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfHelloPad.setStatus(_F)
class _AgentIsisConfigIfMetricL1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_AgentIsisConfigIfMetricL1_Type.__name__=_J
_AgentIsisConfigIfMetricL1_Object=MibTableColumn
agentIsisConfigIfMetricL1=_AgentIsisConfigIfMetricL1_Object((1,3,6,1,4,1,7244,2,2,13,3,1,11),_AgentIsisConfigIfMetricL1_Type())
agentIsisConfigIfMetricL1.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfMetricL1.setStatus(_A)
class _AgentIsisConfigIfMetricL2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_AgentIsisConfigIfMetricL2_Type.__name__=_J
_AgentIsisConfigIfMetricL2_Object=MibTableColumn
agentIsisConfigIfMetricL2=_AgentIsisConfigIfMetricL2_Object((1,3,6,1,4,1,7244,2,2,13,3,1,12),_AgentIsisConfigIfMetricL2_Type())
agentIsisConfigIfMetricL2.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfMetricL2.setStatus(_A)
class _AgentIsisConfigIfPriorityL1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AgentIsisConfigIfPriorityL1_Type.__name__=_J
_AgentIsisConfigIfPriorityL1_Object=MibTableColumn
agentIsisConfigIfPriorityL1=_AgentIsisConfigIfPriorityL1_Object((1,3,6,1,4,1,7244,2,2,13,3,1,13),_AgentIsisConfigIfPriorityL1_Type())
agentIsisConfigIfPriorityL1.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfPriorityL1.setStatus(_A)
class _AgentIsisConfigIfPriorityL2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AgentIsisConfigIfPriorityL2_Type.__name__=_J
_AgentIsisConfigIfPriorityL2_Object=MibTableColumn
agentIsisConfigIfPriorityL2=_AgentIsisConfigIfPriorityL2_Object((1,3,6,1,4,1,7244,2,2,13,3,1,14),_AgentIsisConfigIfPriorityL2_Type())
agentIsisConfigIfPriorityL2.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfPriorityL2.setStatus(_A)
class _AgentIsisConfigIfPasswoad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_AgentIsisConfigIfPasswoad_Type.__name__=_K
_AgentIsisConfigIfPasswoad_Object=MibTableColumn
agentIsisConfigIfPasswoad=_AgentIsisConfigIfPasswoad_Object((1,3,6,1,4,1,7244,2,2,13,3,1,15),_AgentIsisConfigIfPasswoad_Type())
agentIsisConfigIfPasswoad.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIsisConfigIfPasswoad.setStatus(_A)
class _AgentIsisConfigIfPasswoadAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_S,0),(_b,1),(_c,3)))
_AgentIsisConfigIfPasswoadAuthType_Type.__name__=_C
_AgentIsisConfigIfPasswoadAuthType_Object=MibTableColumn
agentIsisConfigIfPasswoadAuthType=_AgentIsisConfigIfPasswoadAuthType_Object((1,3,6,1,4,1,7244,2,2,13,3,1,16),_AgentIsisConfigIfPasswoadAuthType_Type())
agentIsisConfigIfPasswoadAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigIfPasswoadAuthType.setStatus(_F)
_AgentIsisConfigifStatus_Type=RowStatus
_AgentIsisConfigifStatus_Object=MibTableColumn
agentIsisConfigifStatus=_AgentIsisConfigifStatus_Object((1,3,6,1,4,1,7244,2,2,13,3,1,17),_AgentIsisConfigifStatus_Type())
agentIsisConfigifStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIsisConfigifStatus.setStatus(_F)
rip2IfConfEntry.registerAugmentions((_E,_AH))
agentRip2IfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())
ospfIfEntry.registerAugmentions((_E,_AI))
agentOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions((_E,_AJ))
agentOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{_Y:SpfTimerRange,_t:AutoCostRefBw,'routing':routing,'agentSwitchArpGroup':agentSwitchArpGroup,'agentSwitchArpAgeoutTime':agentSwitchArpAgeoutTime,'agentSwitchArpResponseTime':agentSwitchArpResponseTime,'agentSwitchArpMaxRetries':agentSwitchArpMaxRetries,'agentSwitchArpCacheSize':agentSwitchArpCacheSize,'agentSwitchArpDynamicRenew':agentSwitchArpDynamicRenew,'agentSwitchArpTotalEntryCountCurrent':agentSwitchArpTotalEntryCountCurrent,'agentSwitchArpTotalEntryCountPeak':agentSwitchArpTotalEntryCountPeak,'agentSwitchArpStaticEntryCountCurrent':agentSwitchArpStaticEntryCountCurrent,'agentSwitchArpStaticEntryCountMax':agentSwitchArpStaticEntryCountMax,'agentSwitchArpTable':agentSwitchArpTable,'agentSwitchArpEntry':agentSwitchArpEntry,'agentSwitchArpAge':agentSwitchArpAge,_e:agentSwitchArpIpAddress,'agentSwitchArpMacAddress':agentSwitchArpMacAddress,'agentSwitchArpInterface':agentSwitchArpInterface,'agentSwitchArpType':agentSwitchArpType,'agentSwitchArpStatus':agentSwitchArpStatus,'agentSwitchLocalProxyArpTable':agentSwitchLocalProxyArpTable,'agentSwitchLocalProxyArpEntry':agentSwitchLocalProxyArpEntry,'agentSwitchLocalProxyArpMode':agentSwitchLocalProxyArpMode,'agentSwitchIntfArpTable':agentSwitchIntfArpTable,'agentSwitchIntfArpEntry':agentSwitchIntfArpEntry,_h:agentSwitchIntfArpIpAddress,_i:agentSwitchIntfArpIfIndex,'agentSwitchIntfArpAge':agentSwitchIntfArpAge,'agentSwitchIntfArpMacAddress':agentSwitchIntfArpMacAddress,'agentSwitchIntfArpType':agentSwitchIntfArpType,'agentSwitchIntfArpStatus':agentSwitchIntfArpStatus,'agentSwitchIpGroup':agentSwitchIpGroup,'agentSwitchIpRoutingMode':agentSwitchIpRoutingMode,'agentSwitchIpDefaultGateway':agentSwitchIpDefaultGateway,'agentSwitchIpInterfaceTable':agentSwitchIpInterfaceTable,'agentSwitchIpInterfaceEntry':agentSwitchIpInterfaceEntry,_W:agentSwitchIpInterfaceIfIndex,'agentSwitchIpInterfaceIpAddress':agentSwitchIpInterfaceIpAddress,'agentSwitchIpInterfaceNetMask':agentSwitchIpInterfaceNetMask,'agentSwitchIpInterfaceClearIp':agentSwitchIpInterfaceClearIp,'agentSwitchIpInterfaceRoutingMode':agentSwitchIpInterfaceRoutingMode,'agentSwitchIpInterfaceProxyARPMode':agentSwitchIpInterfaceProxyARPMode,'agentSwitchIpInterfaceMtuValue':agentSwitchIpInterfaceMtuValue,'agentSwitchIpInterfaceBandwidth':agentSwitchIpInterfaceBandwidth,'agentSwitchIpInterfaceUnnumberedIfIndex':agentSwitchIpInterfaceUnnumberedIfIndex,'agentSwitchIpInterfaceIcmpUnreachables':agentSwitchIpInterfaceIcmpUnreachables,'agentSwitchIpInterfaceIcmpRedirects':agentSwitchIpInterfaceIcmpRedirects,'agentSwitchDhcpOperation':agentSwitchDhcpOperation,'agentSwitchIPAddressConfigMethod':agentSwitchIPAddressConfigMethod,'agentSwitchIpInterfaceDhcpClientRestart':agentSwitchIpInterfaceDhcpClientRestart,'agentSwitchIpRouterDiscoveryTable':agentSwitchIpRouterDiscoveryTable,'agentSwitchIpRouterDiscoveryEntry':agentSwitchIpRouterDiscoveryEntry,_j:agentSwitchIpRouterDiscoveryIfIndex,'agentSwitchIpRouterDiscoveryAdvertiseMode':agentSwitchIpRouterDiscoveryAdvertiseMode,'agentSwitchIpRouterDiscoveryMaxAdvertisementInterval':agentSwitchIpRouterDiscoveryMaxAdvertisementInterval,'agentSwitchIpRouterDiscoveryMinAdvertisementInterval':agentSwitchIpRouterDiscoveryMinAdvertisementInterval,'agentSwitchIpRouterDiscoveryAdvertisementLifetime':agentSwitchIpRouterDiscoveryAdvertisementLifetime,'agentSwitchIpRouterDiscoveryPreferenceLevel':agentSwitchIpRouterDiscoveryPreferenceLevel,'agentSwitchIpRouterDiscoveryAdvertisementAddress':agentSwitchIpRouterDiscoveryAdvertisementAddress,'agentSwitchIpVlanTable':agentSwitchIpVlanTable,'agentSwitchIpVlanEntry':agentSwitchIpVlanEntry,_k:agentSwitchIpVlanId,'agentSwitchIpVlanIfIndex':agentSwitchIpVlanIfIndex,'agentSwitchIpVlanRoutingStatus':agentSwitchIpVlanRoutingStatus,'agentSwitchSecondaryAddressTable':agentSwitchSecondaryAddressTable,'agentSwitchSecondaryAddressEntry':agentSwitchSecondaryAddressEntry,_l:agentSwitchSecondaryIpAddress,'agentSwitchSecondaryNetMask':agentSwitchSecondaryNetMask,'agentSwitchSecondaryStatus':agentSwitchSecondaryStatus,'agentSwitchHelperAddressTable':agentSwitchHelperAddressTable,'agentSwitchHelperAddressEntry':agentSwitchHelperAddressEntry,_m:agentSwitchHelperIpAddress,'agentSwitchHelperStatus':agentSwitchHelperStatus,'agentSwitchIpIcmpControlGroup':agentSwitchIpIcmpControlGroup,'agentSwitchIpIcmpEchoReplyMode':agentSwitchIpIcmpEchoReplyMode,'agentSwitchIpIcmpRedirectsMode':agentSwitchIpIcmpRedirectsMode,'agentSwitchIpIcmpRateLimitInterval':agentSwitchIpIcmpRateLimitInterval,'agentSwitchIpIcmpRateLimitBurstSize':agentSwitchIpIcmpRateLimitBurstSize,'agentSwitchIntfIpHelperAddressTable':agentSwitchIntfIpHelperAddressTable,'agentSwitchIntfIpHelperAddressEntry':agentSwitchIntfIpHelperAddressEntry,_o:agentSwitchIntfIpHelperIpAddress,_n:agentSwitchIntfIpHelperUdpPort,'agentSwitchIntfIpHelperDiscard':agentSwitchIntfIpHelperDiscard,'agentSwitchIntfIpHelperHitCount':agentSwitchIntfIpHelperHitCount,'agentSwitchIntfIpHelperStatus':agentSwitchIntfIpHelperStatus,'agentSwitchClearIpDefaultGateway':agentSwitchClearIpDefaultGateway,'agentSwitchIpInterfaceRoutingModeEnable':agentSwitchIpInterfaceRoutingModeEnable,'agentSwitchIpDeadGatewayDetectMode':agentSwitchIpDeadGatewayDetectMode,'agentSwitchIpDeadGatewayDetectionProbeInterval':agentSwitchIpDeadGatewayDetectionProbeInterval,'agentRouterRipConfigGroup':agentRouterRipConfigGroup,'agentRouterRipAdminState':agentRouterRipAdminState,'agentRouterRipSplitHorizonMode':agentRouterRipSplitHorizonMode,'agentRouterRipAutoSummaryMode':agentRouterRipAutoSummaryMode,'agentRouterRipHostRoutesAcceptMode':agentRouterRipHostRoutesAcceptMode,'agentRouterRipDefaultMetric':agentRouterRipDefaultMetric,'agentRouterRipDefaultMetricConfigured':agentRouterRipDefaultMetricConfigured,'agentRouterRipDefaultInfoOriginate':agentRouterRipDefaultInfoOriginate,'agentRouterRipDistance':agentRouterRipDistance,'agentRipRouteRedistTable':agentRipRouteRedistTable,'agentRipRouteRedistEntry':agentRipRouteRedistEntry,_p:agentRipRouteRedistSource,'agentRipRouteRedistMode':agentRipRouteRedistMode,'agentRipRouteRedistMetric':agentRipRouteRedistMetric,'agentRipRouteRedistMetricConfigured':agentRipRouteRedistMetricConfigured,'agentRipRouteRedistMatchInternal':agentRipRouteRedistMatchInternal,'agentRipRouteRedistMatchExternal1':agentRipRouteRedistMatchExternal1,'agentRipRouteRedistMatchExternal2':agentRipRouteRedistMatchExternal2,'agentRipRouteRedistMatchNSSAExternal1':agentRipRouteRedistMatchNSSAExternal1,'agentRipRouteRedistMatchNSSAExternal2':agentRipRouteRedistMatchNSSAExternal2,'agentRipRouteRedistDistList':agentRipRouteRedistDistList,'agentRipRouteRedistDistListConfigured':agentRipRouteRedistDistListConfigured,'agentRip2IfConfTable':agentRip2IfConfTable,_AH:agentRip2IfConfEntry,'agentRip2IfConfAuthKeyId':agentRip2IfConfAuthKeyId,'agentRouterRipRoutePref':agentRouterRipRoutePref,'agentRouterOspfConfigGroup':agentRouterOspfConfigGroup,'agentOspfDefaultMetric':agentOspfDefaultMetric,'agentOspfDefaultMetricConfigured':agentOspfDefaultMetricConfigured,'agentOspfDefaultInfoOriginate':agentOspfDefaultInfoOriginate,'agentOspfDefaultInfoOriginateAlways':agentOspfDefaultInfoOriginateAlways,'agentOspfDefaultInfoOriginateMetric':agentOspfDefaultInfoOriginateMetric,'agentOspfDefaultInfoOriginateMetricConfigured':agentOspfDefaultInfoOriginateMetricConfigured,'agentOspfDefaultInfoOriginateMetricType':agentOspfDefaultInfoOriginateMetricType,'agentOspfRouteRedistTable':agentOspfRouteRedistTable,'agentOspfRouteRedistEntry':agentOspfRouteRedistEntry,_s:agentOspfRouteRedistSource,'agentOspfRouteRedistMode':agentOspfRouteRedistMode,'agentOspfRouteRedistMetric':agentOspfRouteRedistMetric,'agentOspfRouteRedistMetricConfigured':agentOspfRouteRedistMetricConfigured,'agentOspfRouteRedistMetricType':agentOspfRouteRedistMetricType,'agentOspfRouteRedistTag':agentOspfRouteRedistTag,'agentOspfRouteRedistSubnets':agentOspfRouteRedistSubnets,'agentOspfRouteRedistDistList':agentOspfRouteRedistDistList,'agentOspfRouteRedistDistListConfigured':agentOspfRouteRedistDistListConfigured,'agentOspfIfTable':agentOspfIfTable,_AI:agentOspfIfEntry,'agentOspfIfAuthKeyId':agentOspfIfAuthKeyId,'agentOspfIfIpMtuIgnoreFlag':agentOspfIfIpMtuIgnoreFlag,'agentOspfIfPassiveMode':agentOspfIfPassiveMode,'agentOspfIfAdvertiseSecondaries':agentOspfIfAdvertiseSecondaries,'agentOspfVirtIfTable':agentOspfVirtIfTable,_AJ:agentOspfVirtIfEntry,'agentOspfVirtIfAuthKeyId':agentOspfVirtIfAuthKeyId,'agentRouterOspfRFC1583CompatibilityMode':agentRouterOspfRFC1583CompatibilityMode,'agentOspfSpfDelayTime':agentOspfSpfDelayTime,'agentOspfSpfHoldTime':agentOspfSpfHoldTime,'agentOspfAutoCostRefBw':agentOspfAutoCostRefBw,'agentOspfOpaqueLsaSupport':agentOspfOpaqueLsaSupport,'agentOspfAreaOpaqueLsdbTable':agentOspfAreaOpaqueLsdbTable,'agentOspfAreaOpaqueLsdbEntry':agentOspfAreaOpaqueLsdbEntry,_u:agentOspfAreaOpaqueLsdbAreaId,_v:agentOspfAreaOpaqueLsdbType,_w:agentOspfAreaOpaqueLsdbLsid,_x:agentOspfAreaOpaqueLsdbRouterId,'agentOspfAreaOpaqueLsdbSequence':agentOspfAreaOpaqueLsdbSequence,'agentOspfAreaOpaqueLsdbAge':agentOspfAreaOpaqueLsdbAge,'agentOspfAreaOpaqueLsdbChecksum':agentOspfAreaOpaqueLsdbChecksum,'agentOspfAreaOpaqueLsdbAdvertisement':agentOspfAreaOpaqueLsdbAdvertisement,'agentOspfLocalLsdbTable':agentOspfLocalLsdbTable,'agentOspfLocalLsdbEntry':agentOspfLocalLsdbEntry,_y:agentOspfLocalLsdbIpAddress,_z:agentOspfLocalLsdbAddressLessIf,_A0:agentOspfLocalLsdbType,_A1:agentOspfLocalLsdbLsid,_A2:agentOspfLocalLsdbRouterId,'agentOspfLocalLsdbSequence':agentOspfLocalLsdbSequence,'agentOspfLocalLsdbAge':agentOspfLocalLsdbAge,'agentOspfLocalLsdbChecksum':agentOspfLocalLsdbChecksum,'agentOspfLocalLsdbAdvertisement':agentOspfLocalLsdbAdvertisement,'agentOspfAsLsdbTable':agentOspfAsLsdbTable,'agentOspfAsLsdbEntry':agentOspfAsLsdbEntry,_A3:agentOspfAsLsdbType,_A4:agentOspfAsLsdbLsid,_A5:agentOspfAsLsdbRouterId,'agentOspfAsLsdbSequence':agentOspfAsLsdbSequence,'agentOspfAsLsdbAge':agentOspfAsLsdbAge,'agentOspfAsLsdbChecksum':agentOspfAsLsdbChecksum,'agentOspfAsLsdbAdvertisement':agentOspfAsLsdbAdvertisement,'agentOspfDefaultPassiveMode':agentOspfDefaultPassiveMode,'agentOspfRoutePrefIntraArea':agentOspfRoutePrefIntraArea,'agentOspfRoutePrefInterArea':agentOspfRoutePrefInterArea,'agentOspfRoutePrefExternal':agentOspfRoutePrefExternal,'agentOspfNetworkAreaTable':agentOspfNetworkAreaTable,'agentOspfNetworkAreaEntry':agentOspfNetworkAreaEntry,_A6:agentOspfNetworkAreaIpAddress,_A7:agentOspfNetworkAreaWildcardMask,_A8:agentOspfNetworkAreaId,'agentOspfNetworkAreaRowStatus':agentOspfNetworkAreaRowStatus,'agentSnmpTrapFlagsConfigGroupLayer3':agentSnmpTrapFlagsConfigGroupLayer3,'agentSnmpVRRPNewMasterTrapFlag':agentSnmpVRRPNewMasterTrapFlag,'agentSnmpVRRPAuthFailureTrapFlag':agentSnmpVRRPAuthFailureTrapFlag,'agentBootpDhcpRelayGroup':agentBootpDhcpRelayGroup,'agentBootpDhcpRelayMaxHopCount':agentBootpDhcpRelayMaxHopCount,'agentBootpDhcpRelayForwardMode':agentBootpDhcpRelayForwardMode,'agentBootpDhcpRelayMinWaitTime':agentBootpDhcpRelayMinWaitTime,'agentBootpDhcpRelayCircuitIdOptionMode':agentBootpDhcpRelayCircuitIdOptionMode,'agentBootpDhcpRelayNumOfRequestsReceived':agentBootpDhcpRelayNumOfRequestsReceived,'agentBootpDhcpRelayNumOfRequestsForwarded':agentBootpDhcpRelayNumOfRequestsForwarded,'agentBootpDhcpRelayNumOfDiscards':agentBootpDhcpRelayNumOfDiscards,'agentECMPGroup':agentECMPGroup,'agentECMPOspfMaxPaths':agentECMPOspfMaxPaths,'agentRouterVrrpConfigGroup':agentRouterVrrpConfigGroup,'agentRouterVrrpAdminState':agentRouterVrrpAdminState,'agentRouterVrrpConfiguredTable':agentRouterVrrpConfiguredTable,'agentRouterVrrpConfiguredEntry':agentRouterVrrpConfiguredEntry,'agentRouterVrrpConfiguredPriority':agentRouterVrrpConfiguredPriority,'agentVrrpOperations':agentVrrpOperations,'agentRouterVrrpOperTable':agentRouterVrrpOperTable,'agentRouterVrrpOperEntry':agentRouterVrrpOperEntry,'agentRouterVrrpOperPriority':agentRouterVrrpOperPriority,'agentRouterVrrpTrackGroup':agentRouterVrrpTrackGroup,'agentRouterVrrpTrackIntfTable':agentRouterVrrpTrackIntfTable,'agentRouterVrrpTrackIntfEntry':agentRouterVrrpTrackIntfEntry,_A9:agentRouterVrrpTrackIntf,'agentRouterVrrpTrackIfPrioDec':agentRouterVrrpTrackIfPrioDec,'agentRouterVrrpTrackIfState':agentRouterVrrpTrackIfState,'agentRouterVrrpTrackIfStatus':agentRouterVrrpTrackIfStatus,'agentRouterVrrpTrackRouteTable':agentRouterVrrpTrackRouteTable,'agentRouterVrrpTrackRouteEntry':agentRouterVrrpTrackRouteEntry,_AA:agentRouterVrrpTrackRtPfx,_AB:agentRouterVrrpTrackRtPfxLen,'agentRouterVrrpTrackRtPrioDec':agentRouterVrrpTrackRtPrioDec,'agentRouterVrrpTrackRtReachable':agentRouterVrrpTrackRtReachable,'agentRouterVrrpTrackRtStatus':agentRouterVrrpTrackRtStatus,'agentIpHelperGroup':agentIpHelperGroup,'agentIpHelperAdminMode':agentIpHelperAdminMode,'agentDhcpClientMsgsReceived':agentDhcpClientMsgsReceived,'agentDhcpClientMsgsRelayed':agentDhcpClientMsgsRelayed,'agentDhcpServerMsgsReceived':agentDhcpServerMsgsReceived,'agentDhcpServerMsgsRelayed':agentDhcpServerMsgsRelayed,'agentUdpClientMsgsReceived':agentUdpClientMsgsReceived,'agentUdpClientMsgsRelayed':agentUdpClientMsgsRelayed,'agentSwitchIpHelperAddressTable':agentSwitchIpHelperAddressTable,'agentSwitchIpHelperAddressEntry':agentSwitchIpHelperAddressEntry,_AC:agentSwitchIpHelperAddress,_AD:agentSwitchIpHelperUdpPort,'agentSwitchIpHelperHitCount':agentSwitchIpHelperHitCount,'agentSwitchIpHelperStatus':agentSwitchIpHelperStatus,'agentUdpClientMsgsTtlExpired':agentUdpClientMsgsTtlExpired,'agentUdpClientMsgsDiscarded':agentUdpClientMsgsDiscarded,'agentDhcpMsgHopCountExceededMax':agentDhcpMsgHopCountExceededMax,'agentDhcpMsgWithSecsFieldBelowMin':agentDhcpMsgWithSecsFieldBelowMin,'agentDhcpMsgWithGiaddrSetToLocalAddr':agentDhcpMsgWithGiaddrSetToLocalAddr,'agentIpHelperStatisticsClear':agentIpHelperStatisticsClear,'agentInternalVlanGroup':agentInternalVlanGroup,'agentInternalVlanBase':agentInternalVlanBase,'agentInternalVlanPolicy':agentInternalVlanPolicy,'agentSwitchInternalVlanTable':agentSwitchInternalVlanTable,'agentSwitchInternalVlanEntry':agentSwitchInternalVlanEntry,_AE:agentSwitchInternalVlanId,'agentSwitchInternalVlanIfIndex':agentSwitchInternalVlanIfIndex,'agentRouterIsisConfigGroup':agentRouterIsisConfigGroup,'agentRouterIsisConfigTable':agentRouterIsisConfigTable,'agentRouterIsisConfigEntry':agentRouterIsisConfigEntry,_a:agentRouterIsisConfigAreaIndex,'agentRouterIsisConfigAreaTag':agentRouterIsisConfigAreaTag,'agentRouterIsisConfigSpfLevel1Interval':agentRouterIsisConfigSpfLevel1Interval,'agentRouterIsisConfigSpfLevel2Interval':agentRouterIsisConfigSpfLevel2Interval,'agentRouterIsisConfigLspLifeTimeInterval':agentRouterIsisConfigLspLifeTimeInterval,'agentRouterIsisConfigLspRefreshTimeInterval':agentRouterIsisConfigLspRefreshTimeInterval,'agentRouterIsisConfigGenaralInterval1TimeInterval':agentRouterIsisConfigGenaralInterval1TimeInterval,'agentRouterIsisConfigGenaralInterval2TimeInterval':agentRouterIsisConfigGenaralInterval2TimeInterval,'agentRouterIsisConfigIsType':agentRouterIsisConfigIsType,'agentRouterIsisConfigMetricType':agentRouterIsisConfigMetricType,'agentRouterIsisConfigHostname':agentRouterIsisConfigHostname,'agentRouterIsisConfigDistant':agentRouterIsisConfigDistant,'agentRouterIsisConfigDefaultMetric':agentRouterIsisConfigDefaultMetric,'agentRouterIsisConfigDefaultInformation':agentRouterIsisConfigDefaultInformation,'agentRouterIsisConfigDomainPasswoad':agentRouterIsisConfigDomainPasswoad,'agentRouterIsisConfigDomainPasswoadAuthType':agentRouterIsisConfigDomainPasswoadAuthType,'agentRouterIsisConfigAreaPasswoad':agentRouterIsisConfigAreaPasswoad,'agentRouterIsisConfigAreaPasswoadAuthType':agentRouterIsisConfigAreaPasswoadAuthType,'agentRouterIsisConfigAreaNET1':agentRouterIsisConfigAreaNET1,'agentRouterIsisConfigAreaNET2':agentRouterIsisConfigAreaNET2,'agentRouterIsisConfigAreaNET3':agentRouterIsisConfigAreaNET3,'agentRouterIsisConfigStatus':agentRouterIsisConfigStatus,'agentIsisRouteRedistTable':agentIsisRouteRedistTable,'agentIsisRouteRedistEntry':agentIsisRouteRedistEntry,_AF:agentIsisRouteRedistSource,'agentIsisRouteRedistMode':agentIsisRouteRedistMode,'agentIsisRouteRedistMetric':agentIsisRouteRedistMetric,'agentIsisRouteRedistMetricConfigured':agentIsisRouteRedistMetricConfigured,'agentIsisRouteRedistMatchInternal':agentIsisRouteRedistMatchInternal,'agentIsisRouteRedistMatchExternal1':agentIsisRouteRedistMatchExternal1,'agentIsisRouteRedistMatchExternal2':agentIsisRouteRedistMatchExternal2,'agentIsisRouteRedistMatchNSSAExternal1':agentIsisRouteRedistMatchNSSAExternal1,'agentIsisRouteRedistMatchNSSAExternal2':agentIsisRouteRedistMatchNSSAExternal2,'agentIsisRouteRedistDistList':agentIsisRouteRedistDistList,'agentIsisRouteRedistDistListConfigured':agentIsisRouteRedistDistListConfigured,'agentIsisConfigIfTable':agentIsisConfigIfTable,'agentIsisConfigIfEntry':agentIsisConfigIfEntry,_AG:agentIsisConfigIfIndex,'agentIsisConfigIfArea':agentIsisConfigIfArea,'agentIsisConfigIfCircuitType':agentIsisConfigIfCircuitType,'agentIsisConfigIfCSNPIntervalL1':agentIsisConfigIfCSNPIntervalL1,'agentIsisConfigIfCSNPIntervalL2':agentIsisConfigIfCSNPIntervalL2,'agentIsisConfigIfHelloIntervalL1':agentIsisConfigIfHelloIntervalL1,'agentIsisConfigIfHelloIntervalL2':agentIsisConfigIfHelloIntervalL2,'agentIsisConfigIfHelloMultiL1':agentIsisConfigIfHelloMultiL1,'agentIsisConfigIfHelloMultiL2':agentIsisConfigIfHelloMultiL2,'agentIsisConfigIfHelloPad':agentIsisConfigIfHelloPad,'agentIsisConfigIfMetricL1':agentIsisConfigIfMetricL1,'agentIsisConfigIfMetricL2':agentIsisConfigIfMetricL2,'agentIsisConfigIfPriorityL1':agentIsisConfigIfPriorityL1,'agentIsisConfigIfPriorityL2':agentIsisConfigIfPriorityL2,'agentIsisConfigIfPasswoad':agentIsisConfigIfPasswoad,'agentIsisConfigIfPasswoadAuthType':agentIsisConfigIfPasswoadAuthType,'agentIsisConfigifStatus':agentIsisConfigifStatus})