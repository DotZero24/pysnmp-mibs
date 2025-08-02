_AK='agentOspfVirtIfEntry'
_AJ='agentOspfIfEntry'
_AI='agentRip2IfConfEntry'
_AH='agentStaticRoutesPreference'
_AG='agentStaticRoutesType'
_AF='agentStaticRoutesNextHop'
_AE='agentStaticRoutesNetMask'
_AD='agentStaticRoutesNetworkAddress'
_AC='agentEcmpNextHopCount'
_AB='agentOspfSpfIndex'
_AA='agentOspfQueueIndex'
_A9='agentSwitchInternalVlanId'
_A8='agentSwitchIpHelperUdpPort'
_A7='agentSwitchIpHelperAddress'
_A6='agentRouterVrrpTrackRtPfxLen'
_A5='agentRouterVrrpTrackRtPfx'
_A4='agentRouterVrrpTrackIntf'
_A3='agentOspfAsLsdbRouterId'
_A2='agentOspfAsLsdbLsid'
_A1='agentOspfAsLsdbType'
_A0='agentOspfLocalLsdbRouterId'
_z='agentOspfLocalLsdbLsid'
_y='agentOspfLocalLsdbType'
_x='agentOspfLocalLsdbAddressLessIf'
_w='agentOspfLocalLsdbIpAddress'
_v='agentOspfAreaOpaqueLsdbRouterId'
_u='agentOspfAreaOpaqueLsdbLsid'
_t='agentOspfAreaOpaqueLsdbType'
_s='agentOspfAreaOpaqueLsdbAreaId'
_r='AutoCostRefBw'
_q='agentOspfRouteRedistSource'
_p='externalType2'
_o='externalType1'
_n='connected'
_m='agentRipRouteRedistSource'
_l='agentSwitchIntfIpHelperIpAddress'
_k='agentSwitchIntfIpHelperUdpPort'
_j='agentSwitchHelperIpAddress'
_i='agentSwitchSecondaryIpAddress'
_h='agentSwitchIpVlanId'
_g='agentSwitchIpRouterDiscoveryIfIndex'
_f='agentSwitchIntfArpIfIndex'
_e='agentSwitchIntfArpIpAddress'
_d='dynamic'
_c='gateway'
_b='agentSwitchArpIpAddress'
_a='DisplayString'
_Z='IpAddress'
_Y='seconds'
_X='SpfTimerRange'
_W='none'
_V='OctetString'
_U='not-applicable'
_T='false'
_S='true'
_R='agentSwitchIpInterfaceIfIndex'
_Q='static'
_P='vrrpOperVrId'
_O='VRRP-MIB'
_N='ifIndex'
_M='IF-MIB'
_L='TruthValue'
_K='Unsigned32'
_J='not-accessible'
_I='read-create'
_H='obsolete'
_G='disable'
_F='enable'
_E='LANCOM-ROUTING-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_M,'InterfaceIndex','InterfaceIndexOrZero',_N)
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
RouterID,ospfAreaEntry,ospfIfEntry,ospfVirtIfEntry=mibBuilder.importSymbols('OSPF-MIB','RouterID','ospfAreaEntry','ospfIfEntry','ospfVirtIfEntry')
rip2IfConfEntry,=mibBuilder.importSymbols('RIPv2-MIB','rip2IfConfEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_Z,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_a,'PhysAddress','RowStatus','TextualConvention',_L)
vrrpOperVrId,=mibBuilder.importSymbols(_O,_P)
fastPathRouting=ModuleIdentity((1,3,6,1,4,1,2356,16,1,2))
if mibBuilder.loadTexts:fastPathRouting.setRevisions(('2017-12-15 00:00','2011-01-26 00:00','2007-05-23 00:00','2003-11-21 00:00','2003-04-02 17:00'))
class SpfTimerRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class AutoCostRefBw(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967))
_AgentSwitchArpGroup_ObjectIdentity=ObjectIdentity
agentSwitchArpGroup=_AgentSwitchArpGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,1))
class _AgentSwitchArpAgeoutTime_Type(Integer32):defaultValue=1200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,21600))
_AgentSwitchArpAgeoutTime_Type.__name__=_D
_AgentSwitchArpAgeoutTime_Object=MibScalar
agentSwitchArpAgeoutTime=_AgentSwitchArpAgeoutTime_Object((1,3,6,1,4,1,2356,16,1,2,1,1),_AgentSwitchArpAgeoutTime_Type())
agentSwitchArpAgeoutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpAgeoutTime.setStatus(_A)
class _AgentSwitchArpResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AgentSwitchArpResponseTime_Type.__name__=_D
_AgentSwitchArpResponseTime_Object=MibScalar
agentSwitchArpResponseTime=_AgentSwitchArpResponseTime_Object((1,3,6,1,4,1,2356,16,1,2,1,2),_AgentSwitchArpResponseTime_Type())
agentSwitchArpResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpResponseTime.setStatus(_A)
class _AgentSwitchArpMaxRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AgentSwitchArpMaxRetries_Type.__name__=_D
_AgentSwitchArpMaxRetries_Object=MibScalar
agentSwitchArpMaxRetries=_AgentSwitchArpMaxRetries_Object((1,3,6,1,4,1,2356,16,1,2,1,3),_AgentSwitchArpMaxRetries_Type())
agentSwitchArpMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpMaxRetries.setStatus(_A)
_AgentSwitchArpCacheSize_Type=Integer32
_AgentSwitchArpCacheSize_Object=MibScalar
agentSwitchArpCacheSize=_AgentSwitchArpCacheSize_Object((1,3,6,1,4,1,2356,16,1,2,1,4),_AgentSwitchArpCacheSize_Type())
agentSwitchArpCacheSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpCacheSize.setStatus(_A)
class _AgentSwitchArpDynamicRenew_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchArpDynamicRenew_Type.__name__=_D
_AgentSwitchArpDynamicRenew_Object=MibScalar
agentSwitchArpDynamicRenew=_AgentSwitchArpDynamicRenew_Object((1,3,6,1,4,1,2356,16,1,2,1,5),_AgentSwitchArpDynamicRenew_Type())
agentSwitchArpDynamicRenew.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpDynamicRenew.setStatus(_A)
_AgentSwitchArpTotalEntryCountCurrent_Type=Gauge32
_AgentSwitchArpTotalEntryCountCurrent_Object=MibScalar
agentSwitchArpTotalEntryCountCurrent=_AgentSwitchArpTotalEntryCountCurrent_Object((1,3,6,1,4,1,2356,16,1,2,1,6),_AgentSwitchArpTotalEntryCountCurrent_Type())
agentSwitchArpTotalEntryCountCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpTotalEntryCountCurrent.setStatus(_A)
_AgentSwitchArpTotalEntryCountPeak_Type=Gauge32
_AgentSwitchArpTotalEntryCountPeak_Object=MibScalar
agentSwitchArpTotalEntryCountPeak=_AgentSwitchArpTotalEntryCountPeak_Object((1,3,6,1,4,1,2356,16,1,2,1,7),_AgentSwitchArpTotalEntryCountPeak_Type())
agentSwitchArpTotalEntryCountPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpTotalEntryCountPeak.setStatus(_A)
_AgentSwitchArpStaticEntryCountCurrent_Type=Gauge32
_AgentSwitchArpStaticEntryCountCurrent_Object=MibScalar
agentSwitchArpStaticEntryCountCurrent=_AgentSwitchArpStaticEntryCountCurrent_Object((1,3,6,1,4,1,2356,16,1,2,1,8),_AgentSwitchArpStaticEntryCountCurrent_Type())
agentSwitchArpStaticEntryCountCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpStaticEntryCountCurrent.setStatus(_A)
_AgentSwitchArpStaticEntryCountMax_Type=Integer32
_AgentSwitchArpStaticEntryCountMax_Object=MibScalar
agentSwitchArpStaticEntryCountMax=_AgentSwitchArpStaticEntryCountMax_Object((1,3,6,1,4,1,2356,16,1,2,1,9),_AgentSwitchArpStaticEntryCountMax_Type())
agentSwitchArpStaticEntryCountMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpStaticEntryCountMax.setStatus(_A)
_AgentSwitchArpTable_Object=MibTable
agentSwitchArpTable=_AgentSwitchArpTable_Object((1,3,6,1,4,1,2356,16,1,2,1,10))
if mibBuilder.loadTexts:agentSwitchArpTable.setStatus(_H)
_AgentSwitchArpEntry_Object=MibTableRow
agentSwitchArpEntry=_AgentSwitchArpEntry_Object((1,3,6,1,4,1,2356,16,1,2,1,10,1))
agentSwitchArpEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:agentSwitchArpEntry.setStatus(_H)
_AgentSwitchArpAge_Type=TimeTicks
_AgentSwitchArpAge_Object=MibTableColumn
agentSwitchArpAge=_AgentSwitchArpAge_Object((1,3,6,1,4,1,2356,16,1,2,1,10,1,1),_AgentSwitchArpAge_Type())
agentSwitchArpAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpAge.setStatus(_H)
_AgentSwitchArpIpAddress_Type=IpAddress
_AgentSwitchArpIpAddress_Object=MibTableColumn
agentSwitchArpIpAddress=_AgentSwitchArpIpAddress_Object((1,3,6,1,4,1,2356,16,1,2,1,10,1,2),_AgentSwitchArpIpAddress_Type())
agentSwitchArpIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpIpAddress.setStatus(_H)
_AgentSwitchArpMacAddress_Type=PhysAddress
_AgentSwitchArpMacAddress_Object=MibTableColumn
agentSwitchArpMacAddress=_AgentSwitchArpMacAddress_Object((1,3,6,1,4,1,2356,16,1,2,1,10,1,3),_AgentSwitchArpMacAddress_Type())
agentSwitchArpMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchArpMacAddress.setStatus(_H)
_AgentSwitchArpInterface_Type=Integer32
_AgentSwitchArpInterface_Object=MibTableColumn
agentSwitchArpInterface=_AgentSwitchArpInterface_Object((1,3,6,1,4,1,2356,16,1,2,1,10,1,4),_AgentSwitchArpInterface_Type())
agentSwitchArpInterface.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchArpInterface.setStatus(_H)
class _AgentSwitchArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_c,2),(_Q,3),(_d,4)))
_AgentSwitchArpType_Type.__name__=_D
_AgentSwitchArpType_Object=MibTableColumn
agentSwitchArpType=_AgentSwitchArpType_Object((1,3,6,1,4,1,2356,16,1,2,1,10,1,5),_AgentSwitchArpType_Type())
agentSwitchArpType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpType.setStatus(_H)
_AgentSwitchArpStatus_Type=RowStatus
_AgentSwitchArpStatus_Object=MibTableColumn
agentSwitchArpStatus=_AgentSwitchArpStatus_Object((1,3,6,1,4,1,2356,16,1,2,1,10,1,6),_AgentSwitchArpStatus_Type())
agentSwitchArpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpStatus.setStatus(_H)
_AgentSwitchLocalProxyArpTable_Object=MibTable
agentSwitchLocalProxyArpTable=_AgentSwitchLocalProxyArpTable_Object((1,3,6,1,4,1,2356,16,1,2,1,11))
if mibBuilder.loadTexts:agentSwitchLocalProxyArpTable.setStatus(_A)
_AgentSwitchLocalProxyArpEntry_Object=MibTableRow
agentSwitchLocalProxyArpEntry=_AgentSwitchLocalProxyArpEntry_Object((1,3,6,1,4,1,2356,16,1,2,1,11,1))
agentSwitchLocalProxyArpEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:agentSwitchLocalProxyArpEntry.setStatus(_A)
class _AgentSwitchLocalProxyArpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchLocalProxyArpMode_Type.__name__=_D
_AgentSwitchLocalProxyArpMode_Object=MibTableColumn
agentSwitchLocalProxyArpMode=_AgentSwitchLocalProxyArpMode_Object((1,3,6,1,4,1,2356,16,1,2,1,11,1,1),_AgentSwitchLocalProxyArpMode_Type())
agentSwitchLocalProxyArpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchLocalProxyArpMode.setStatus(_A)
_AgentSwitchIntfArpTable_Object=MibTable
agentSwitchIntfArpTable=_AgentSwitchIntfArpTable_Object((1,3,6,1,4,1,2356,16,1,2,1,12))
if mibBuilder.loadTexts:agentSwitchIntfArpTable.setStatus(_A)
_AgentSwitchIntfArpEntry_Object=MibTableRow
agentSwitchIntfArpEntry=_AgentSwitchIntfArpEntry_Object((1,3,6,1,4,1,2356,16,1,2,1,12,1))
agentSwitchIntfArpEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:agentSwitchIntfArpEntry.setStatus(_A)
_AgentSwitchIntfArpIpAddress_Type=IpAddress
_AgentSwitchIntfArpIpAddress_Object=MibTableColumn
agentSwitchIntfArpIpAddress=_AgentSwitchIntfArpIpAddress_Object((1,3,6,1,4,1,2356,16,1,2,1,12,1,1),_AgentSwitchIntfArpIpAddress_Type())
agentSwitchIntfArpIpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:agentSwitchIntfArpIpAddress.setStatus(_A)
_AgentSwitchIntfArpIfIndex_Type=InterfaceIndex
_AgentSwitchIntfArpIfIndex_Object=MibTableColumn
agentSwitchIntfArpIfIndex=_AgentSwitchIntfArpIfIndex_Object((1,3,6,1,4,1,2356,16,1,2,1,12,1,2),_AgentSwitchIntfArpIfIndex_Type())
agentSwitchIntfArpIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentSwitchIntfArpIfIndex.setStatus(_A)
_AgentSwitchIntfArpAge_Type=TimeTicks
_AgentSwitchIntfArpAge_Object=MibTableColumn
agentSwitchIntfArpAge=_AgentSwitchIntfArpAge_Object((1,3,6,1,4,1,2356,16,1,2,1,12,1,3),_AgentSwitchIntfArpAge_Type())
agentSwitchIntfArpAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIntfArpAge.setStatus(_A)
_AgentSwitchIntfArpMacAddress_Type=PhysAddress
_AgentSwitchIntfArpMacAddress_Object=MibTableColumn
agentSwitchIntfArpMacAddress=_AgentSwitchIntfArpMacAddress_Object((1,3,6,1,4,1,2356,16,1,2,1,12,1,4),_AgentSwitchIntfArpMacAddress_Type())
agentSwitchIntfArpMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIntfArpMacAddress.setStatus(_A)
class _AgentSwitchIntfArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_c,2),(_Q,3),(_d,4)))
_AgentSwitchIntfArpType_Type.__name__=_D
_AgentSwitchIntfArpType_Object=MibTableColumn
agentSwitchIntfArpType=_AgentSwitchIntfArpType_Object((1,3,6,1,4,1,2356,16,1,2,1,12,1,5),_AgentSwitchIntfArpType_Type())
agentSwitchIntfArpType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIntfArpType.setStatus(_A)
_AgentSwitchIntfArpStatus_Type=RowStatus
_AgentSwitchIntfArpStatus_Object=MibTableColumn
agentSwitchIntfArpStatus=_AgentSwitchIntfArpStatus_Object((1,3,6,1,4,1,2356,16,1,2,1,12,1,6),_AgentSwitchIntfArpStatus_Type())
agentSwitchIntfArpStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIntfArpStatus.setStatus(_A)
_AgentSwitchIpGroup_ObjectIdentity=ObjectIdentity
agentSwitchIpGroup=_AgentSwitchIpGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,2))
class _AgentSwitchIpRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpRoutingMode_Type.__name__=_D
_AgentSwitchIpRoutingMode_Object=MibScalar
agentSwitchIpRoutingMode=_AgentSwitchIpRoutingMode_Object((1,3,6,1,4,1,2356,16,1,2,2,1),_AgentSwitchIpRoutingMode_Type())
agentSwitchIpRoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRoutingMode.setStatus(_A)
_AgentSwitchIpDefaultGateway_Type=IpAddress
_AgentSwitchIpDefaultGateway_Object=MibScalar
agentSwitchIpDefaultGateway=_AgentSwitchIpDefaultGateway_Object((1,3,6,1,4,1,2356,16,1,2,2,2),_AgentSwitchIpDefaultGateway_Type())
agentSwitchIpDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpDefaultGateway.setStatus(_A)
_AgentSwitchIpInterfaceTable_Object=MibTable
agentSwitchIpInterfaceTable=_AgentSwitchIpInterfaceTable_Object((1,3,6,1,4,1,2356,16,1,2,2,3))
if mibBuilder.loadTexts:agentSwitchIpInterfaceTable.setStatus(_A)
_AgentSwitchIpInterfaceEntry_Object=MibTableRow
agentSwitchIpInterfaceEntry=_AgentSwitchIpInterfaceEntry_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1))
agentSwitchIpInterfaceEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:agentSwitchIpInterfaceEntry.setStatus(_A)
class _AgentSwitchIpInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpInterfaceIfIndex_Type.__name__=_D
_AgentSwitchIpInterfaceIfIndex_Object=MibTableColumn
agentSwitchIpInterfaceIfIndex=_AgentSwitchIpInterfaceIfIndex_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,1),_AgentSwitchIpInterfaceIfIndex_Type())
agentSwitchIpInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIfIndex.setStatus(_A)
class _AgentSwitchIPAddressConfigMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_W,0),('manual',1),('dhcp',2)))
_AgentSwitchIPAddressConfigMethod_Type.__name__=_D
_AgentSwitchIPAddressConfigMethod_Object=MibTableColumn
agentSwitchIPAddressConfigMethod=_AgentSwitchIPAddressConfigMethod_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,2),_AgentSwitchIPAddressConfigMethod_Type())
agentSwitchIPAddressConfigMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIPAddressConfigMethod.setStatus(_A)
_AgentSwitchIpInterfaceIpAddress_Type=IpAddress
_AgentSwitchIpInterfaceIpAddress_Object=MibTableColumn
agentSwitchIpInterfaceIpAddress=_AgentSwitchIpInterfaceIpAddress_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,3),_AgentSwitchIpInterfaceIpAddress_Type())
agentSwitchIpInterfaceIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIpAddress.setStatus(_A)
_AgentSwitchIpInterfaceNetMask_Type=IpAddress
_AgentSwitchIpInterfaceNetMask_Object=MibTableColumn
agentSwitchIpInterfaceNetMask=_AgentSwitchIpInterfaceNetMask_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,4),_AgentSwitchIpInterfaceNetMask_Type())
agentSwitchIpInterfaceNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceNetMask.setStatus(_A)
class _AgentSwitchIpInterfaceClearIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpInterfaceClearIp_Type.__name__=_D
_AgentSwitchIpInterfaceClearIp_Object=MibTableColumn
agentSwitchIpInterfaceClearIp=_AgentSwitchIpInterfaceClearIp_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,5),_AgentSwitchIpInterfaceClearIp_Type())
agentSwitchIpInterfaceClearIp.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceClearIp.setStatus(_A)
class _AgentSwitchIpInterfaceRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpInterfaceRoutingMode_Type.__name__=_D
_AgentSwitchIpInterfaceRoutingMode_Object=MibTableColumn
agentSwitchIpInterfaceRoutingMode=_AgentSwitchIpInterfaceRoutingMode_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,6),_AgentSwitchIpInterfaceRoutingMode_Type())
agentSwitchIpInterfaceRoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceRoutingMode.setStatus(_A)
class _AgentSwitchIpInterfaceProxyARPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpInterfaceProxyARPMode_Type.__name__=_D
_AgentSwitchIpInterfaceProxyARPMode_Object=MibTableColumn
agentSwitchIpInterfaceProxyARPMode=_AgentSwitchIpInterfaceProxyARPMode_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,7),_AgentSwitchIpInterfaceProxyARPMode_Type())
agentSwitchIpInterfaceProxyARPMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceProxyARPMode.setStatus(_A)
class _AgentSwitchIpInterfaceMtuValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(68,9198))
_AgentSwitchIpInterfaceMtuValue_Type.__name__=_K
_AgentSwitchIpInterfaceMtuValue_Object=MibTableColumn
agentSwitchIpInterfaceMtuValue=_AgentSwitchIpInterfaceMtuValue_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,8),_AgentSwitchIpInterfaceMtuValue_Type())
agentSwitchIpInterfaceMtuValue.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceMtuValue.setStatus(_A)
class _AgentSwitchIpInterfaceBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,10000000))
_AgentSwitchIpInterfaceBandwidth_Type.__name__=_K
_AgentSwitchIpInterfaceBandwidth_Object=MibTableColumn
agentSwitchIpInterfaceBandwidth=_AgentSwitchIpInterfaceBandwidth_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,9),_AgentSwitchIpInterfaceBandwidth_Type())
agentSwitchIpInterfaceBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceBandwidth.setStatus(_A)
_AgentSwitchIpInterfaceUnnumberedIfIndex_Type=InterfaceIndexOrZero
_AgentSwitchIpInterfaceUnnumberedIfIndex_Object=MibTableColumn
agentSwitchIpInterfaceUnnumberedIfIndex=_AgentSwitchIpInterfaceUnnumberedIfIndex_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,10),_AgentSwitchIpInterfaceUnnumberedIfIndex_Type())
agentSwitchIpInterfaceUnnumberedIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceUnnumberedIfIndex.setStatus(_A)
class _AgentSwitchIpInterfaceIcmpUnreachables_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpInterfaceIcmpUnreachables_Type.__name__=_D
_AgentSwitchIpInterfaceIcmpUnreachables_Object=MibTableColumn
agentSwitchIpInterfaceIcmpUnreachables=_AgentSwitchIpInterfaceIcmpUnreachables_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,11),_AgentSwitchIpInterfaceIcmpUnreachables_Type())
agentSwitchIpInterfaceIcmpUnreachables.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIcmpUnreachables.setStatus(_A)
class _AgentSwitchIpInterfaceIcmpRedirects_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpInterfaceIcmpRedirects_Type.__name__=_D
_AgentSwitchIpInterfaceIcmpRedirects_Object=MibTableColumn
agentSwitchIpInterfaceIcmpRedirects=_AgentSwitchIpInterfaceIcmpRedirects_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,12),_AgentSwitchIpInterfaceIcmpRedirects_Type())
agentSwitchIpInterfaceIcmpRedirects.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIcmpRedirects.setStatus(_A)
class _AgentSwitchDhcpOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('renew',1),('release',2),(_W,3)))
_AgentSwitchDhcpOperation_Type.__name__=_D
_AgentSwitchDhcpOperation_Object=MibTableColumn
agentSwitchDhcpOperation=_AgentSwitchDhcpOperation_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,13),_AgentSwitchDhcpOperation_Type())
agentSwitchDhcpOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchDhcpOperation.setStatus(_A)
class _AgentSwitchIpInterfaceSuppressed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unsuppressed',0),('suppressed',1)))
_AgentSwitchIpInterfaceSuppressed_Type.__name__=_D
_AgentSwitchIpInterfaceSuppressed_Object=MibTableColumn
agentSwitchIpInterfaceSuppressed=_AgentSwitchIpInterfaceSuppressed_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,14),_AgentSwitchIpInterfaceSuppressed_Type())
agentSwitchIpInterfaceSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceSuppressed.setStatus(_A)
class _AgentSwitchIpInterfaceNumberOfFlaps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AgentSwitchIpInterfaceNumberOfFlaps_Type.__name__=_K
_AgentSwitchIpInterfaceNumberOfFlaps_Object=MibTableColumn
agentSwitchIpInterfaceNumberOfFlaps=_AgentSwitchIpInterfaceNumberOfFlaps_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,15),_AgentSwitchIpInterfaceNumberOfFlaps_Type())
agentSwitchIpInterfaceNumberOfFlaps.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceNumberOfFlaps.setStatus(_A)
class _AgentSwitchIpInterfaceCurrentPenalty_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_AgentSwitchIpInterfaceCurrentPenalty_Type.__name__=_K
_AgentSwitchIpInterfaceCurrentPenalty_Object=MibTableColumn
agentSwitchIpInterfaceCurrentPenalty=_AgentSwitchIpInterfaceCurrentPenalty_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,16),_AgentSwitchIpInterfaceCurrentPenalty_Type())
agentSwitchIpInterfaceCurrentPenalty.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceCurrentPenalty.setStatus(_A)
class _AgentSwitchIpInterfaceReUseTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentSwitchIpInterfaceReUseTime_Type.__name__=_K
_AgentSwitchIpInterfaceReUseTime_Object=MibTableColumn
agentSwitchIpInterfaceReUseTime=_AgentSwitchIpInterfaceReUseTime_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,17),_AgentSwitchIpInterfaceReUseTime_Type())
agentSwitchIpInterfaceReUseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceReUseTime.setStatus(_A)
class _AgentSwitchIpInterfaceAutoStateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpInterfaceAutoStateMode_Type.__name__=_D
_AgentSwitchIpInterfaceAutoStateMode_Object=MibTableColumn
agentSwitchIpInterfaceAutoStateMode=_AgentSwitchIpInterfaceAutoStateMode_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,18),_AgentSwitchIpInterfaceAutoStateMode_Type())
agentSwitchIpInterfaceAutoStateMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceAutoStateMode.setStatus(_A)
class _AgentSwitchIpInterfaceFptiName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AgentSwitchIpInterfaceFptiName_Type.__name__=_a
_AgentSwitchIpInterfaceFptiName_Object=MibTableColumn
agentSwitchIpInterfaceFptiName=_AgentSwitchIpInterfaceFptiName_Object((1,3,6,1,4,1,2356,16,1,2,2,3,1,19),_AgentSwitchIpInterfaceFptiName_Type())
agentSwitchIpInterfaceFptiName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceFptiName.setStatus(_A)
_AgentSwitchIpRouterDiscoveryTable_Object=MibTable
agentSwitchIpRouterDiscoveryTable=_AgentSwitchIpRouterDiscoveryTable_Object((1,3,6,1,4,1,2356,16,1,2,2,4))
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryTable.setStatus(_A)
_AgentSwitchIpRouterDiscoveryEntry_Object=MibTableRow
agentSwitchIpRouterDiscoveryEntry=_AgentSwitchIpRouterDiscoveryEntry_Object((1,3,6,1,4,1,2356,16,1,2,2,4,1))
agentSwitchIpRouterDiscoveryEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryEntry.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpRouterDiscoveryIfIndex_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryIfIndex_Object=MibTableColumn
agentSwitchIpRouterDiscoveryIfIndex=_AgentSwitchIpRouterDiscoveryIfIndex_Object((1,3,6,1,4,1,2356,16,1,2,2,4,1,1),_AgentSwitchIpRouterDiscoveryIfIndex_Type())
agentSwitchIpRouterDiscoveryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryIfIndex.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryAdvertiseMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpRouterDiscoveryAdvertiseMode_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryAdvertiseMode_Object=MibTableColumn
agentSwitchIpRouterDiscoveryAdvertiseMode=_AgentSwitchIpRouterDiscoveryAdvertiseMode_Object((1,3,6,1,4,1,2356,16,1,2,2,4,1,2),_AgentSwitchIpRouterDiscoveryAdvertiseMode_Type())
agentSwitchIpRouterDiscoveryAdvertiseMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryAdvertiseMode.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object=MibTableColumn
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval=_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object((1,3,6,1,4,1,2356,16,1,2,2,4,1,3),_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type())
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):defaultValue=450;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object=MibTableColumn
agentSwitchIpRouterDiscoveryMinAdvertisementInterval=_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object((1,3,6,1,4,1,2356,16,1,2,2,4,1,4),_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type())
agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,9000))
_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object=MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementLifetime=_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object((1,3,6,1,4,1,2356,16,1,2,2,4,1,5),_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type())
agentSwitchIpRouterDiscoveryAdvertisementLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryAdvertisementLifetime.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryPreferenceLevel_Type(Integer32):defaultValue=0
_AgentSwitchIpRouterDiscoveryPreferenceLevel_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryPreferenceLevel_Object=MibTableColumn
agentSwitchIpRouterDiscoveryPreferenceLevel=_AgentSwitchIpRouterDiscoveryPreferenceLevel_Object((1,3,6,1,4,1,2356,16,1,2,2,4,1,6),_AgentSwitchIpRouterDiscoveryPreferenceLevel_Type())
agentSwitchIpRouterDiscoveryPreferenceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryPreferenceLevel.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):defaultHexValue='E0000001'
_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type.__name__=_Z
_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object=MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementAddress=_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object((1,3,6,1,4,1,2356,16,1,2,2,4,1,7),_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type())
agentSwitchIpRouterDiscoveryAdvertisementAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryAdvertisementAddress.setStatus(_A)
_AgentSwitchIpVlanTable_Object=MibTable
agentSwitchIpVlanTable=_AgentSwitchIpVlanTable_Object((1,3,6,1,4,1,2356,16,1,2,2,5))
if mibBuilder.loadTexts:agentSwitchIpVlanTable.setStatus(_A)
_AgentSwitchIpVlanEntry_Object=MibTableRow
agentSwitchIpVlanEntry=_AgentSwitchIpVlanEntry_Object((1,3,6,1,4,1,2356,16,1,2,2,5,1))
agentSwitchIpVlanEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:agentSwitchIpVlanEntry.setStatus(_A)
class _AgentSwitchIpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpVlanId_Type.__name__=_D
_AgentSwitchIpVlanId_Object=MibTableColumn
agentSwitchIpVlanId=_AgentSwitchIpVlanId_Object((1,3,6,1,4,1,2356,16,1,2,2,5,1,1),_AgentSwitchIpVlanId_Type())
agentSwitchIpVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpVlanId.setStatus(_A)
_AgentSwitchIpVlanIfIndex_Type=Integer32
_AgentSwitchIpVlanIfIndex_Object=MibTableColumn
agentSwitchIpVlanIfIndex=_AgentSwitchIpVlanIfIndex_Object((1,3,6,1,4,1,2356,16,1,2,2,5,1,2),_AgentSwitchIpVlanIfIndex_Type())
agentSwitchIpVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpVlanIfIndex.setStatus(_A)
_AgentSwitchIpVlanRoutingStatus_Type=RowStatus
_AgentSwitchIpVlanRoutingStatus_Object=MibTableColumn
agentSwitchIpVlanRoutingStatus=_AgentSwitchIpVlanRoutingStatus_Object((1,3,6,1,4,1,2356,16,1,2,2,5,1,3),_AgentSwitchIpVlanRoutingStatus_Type())
agentSwitchIpVlanRoutingStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIpVlanRoutingStatus.setStatus(_A)
_AgentSwitchSecondaryAddressTable_Object=MibTable
agentSwitchSecondaryAddressTable=_AgentSwitchSecondaryAddressTable_Object((1,3,6,1,4,1,2356,16,1,2,2,6))
if mibBuilder.loadTexts:agentSwitchSecondaryAddressTable.setStatus(_A)
_AgentSwitchSecondaryAddressEntry_Object=MibTableRow
agentSwitchSecondaryAddressEntry=_AgentSwitchSecondaryAddressEntry_Object((1,3,6,1,4,1,2356,16,1,2,2,6,1))
agentSwitchSecondaryAddressEntry.setIndexNames((0,_E,_R),(0,_E,_i))
if mibBuilder.loadTexts:agentSwitchSecondaryAddressEntry.setStatus(_A)
_AgentSwitchSecondaryIpAddress_Type=IpAddress
_AgentSwitchSecondaryIpAddress_Object=MibTableColumn
agentSwitchSecondaryIpAddress=_AgentSwitchSecondaryIpAddress_Object((1,3,6,1,4,1,2356,16,1,2,2,6,1,1),_AgentSwitchSecondaryIpAddress_Type())
agentSwitchSecondaryIpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:agentSwitchSecondaryIpAddress.setStatus(_A)
_AgentSwitchSecondaryNetMask_Type=IpAddress
_AgentSwitchSecondaryNetMask_Object=MibTableColumn
agentSwitchSecondaryNetMask=_AgentSwitchSecondaryNetMask_Object((1,3,6,1,4,1,2356,16,1,2,2,6,1,2),_AgentSwitchSecondaryNetMask_Type())
agentSwitchSecondaryNetMask.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchSecondaryNetMask.setStatus(_A)
_AgentSwitchSecondaryStatus_Type=RowStatus
_AgentSwitchSecondaryStatus_Object=MibTableColumn
agentSwitchSecondaryStatus=_AgentSwitchSecondaryStatus_Object((1,3,6,1,4,1,2356,16,1,2,2,6,1,3),_AgentSwitchSecondaryStatus_Type())
agentSwitchSecondaryStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchSecondaryStatus.setStatus(_A)
_AgentSwitchHelperAddressTable_Object=MibTable
agentSwitchHelperAddressTable=_AgentSwitchHelperAddressTable_Object((1,3,6,1,4,1,2356,16,1,2,2,7))
if mibBuilder.loadTexts:agentSwitchHelperAddressTable.setStatus(_H)
_AgentSwitchHelperAddressEntry_Object=MibTableRow
agentSwitchHelperAddressEntry=_AgentSwitchHelperAddressEntry_Object((1,3,6,1,4,1,2356,16,1,2,2,7,1))
agentSwitchHelperAddressEntry.setIndexNames((0,_E,_R),(0,_E,_j))
if mibBuilder.loadTexts:agentSwitchHelperAddressEntry.setStatus(_H)
_AgentSwitchHelperIpAddress_Type=IpAddress
_AgentSwitchHelperIpAddress_Object=MibTableColumn
agentSwitchHelperIpAddress=_AgentSwitchHelperIpAddress_Object((1,3,6,1,4,1,2356,16,1,2,2,7,1,1),_AgentSwitchHelperIpAddress_Type())
agentSwitchHelperIpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:agentSwitchHelperIpAddress.setStatus(_H)
_AgentSwitchHelperStatus_Type=RowStatus
_AgentSwitchHelperStatus_Object=MibTableColumn
agentSwitchHelperStatus=_AgentSwitchHelperStatus_Object((1,3,6,1,4,1,2356,16,1,2,2,7,1,2),_AgentSwitchHelperStatus_Type())
agentSwitchHelperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchHelperStatus.setStatus(_H)
_AgentSwitchIpIcmpControlGroup_ObjectIdentity=ObjectIdentity
agentSwitchIpIcmpControlGroup=_AgentSwitchIpIcmpControlGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,2,8))
class _AgentSwitchIpIcmpEchoReplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpIcmpEchoReplyMode_Type.__name__=_D
_AgentSwitchIpIcmpEchoReplyMode_Object=MibScalar
agentSwitchIpIcmpEchoReplyMode=_AgentSwitchIpIcmpEchoReplyMode_Object((1,3,6,1,4,1,2356,16,1,2,2,8,1),_AgentSwitchIpIcmpEchoReplyMode_Type())
agentSwitchIpIcmpEchoReplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpIcmpEchoReplyMode.setStatus(_A)
class _AgentSwitchIpIcmpRedirectsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchIpIcmpRedirectsMode_Type.__name__=_D
_AgentSwitchIpIcmpRedirectsMode_Object=MibScalar
agentSwitchIpIcmpRedirectsMode=_AgentSwitchIpIcmpRedirectsMode_Object((1,3,6,1,4,1,2356,16,1,2,2,8,2),_AgentSwitchIpIcmpRedirectsMode_Type())
agentSwitchIpIcmpRedirectsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpIcmpRedirectsMode.setStatus(_A)
class _AgentSwitchIpIcmpRateLimitInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpIcmpRateLimitInterval_Type.__name__=_D
_AgentSwitchIpIcmpRateLimitInterval_Object=MibScalar
agentSwitchIpIcmpRateLimitInterval=_AgentSwitchIpIcmpRateLimitInterval_Object((1,3,6,1,4,1,2356,16,1,2,2,8,3),_AgentSwitchIpIcmpRateLimitInterval_Type())
agentSwitchIpIcmpRateLimitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpIcmpRateLimitInterval.setStatus(_A)
class _AgentSwitchIpIcmpRateLimitBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_AgentSwitchIpIcmpRateLimitBurstSize_Type.__name__=_D
_AgentSwitchIpIcmpRateLimitBurstSize_Object=MibScalar
agentSwitchIpIcmpRateLimitBurstSize=_AgentSwitchIpIcmpRateLimitBurstSize_Object((1,3,6,1,4,1,2356,16,1,2,2,8,4),_AgentSwitchIpIcmpRateLimitBurstSize_Type())
agentSwitchIpIcmpRateLimitBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpIcmpRateLimitBurstSize.setStatus(_A)
_AgentSwitchIntfIpHelperAddressTable_Object=MibTable
agentSwitchIntfIpHelperAddressTable=_AgentSwitchIntfIpHelperAddressTable_Object((1,3,6,1,4,1,2356,16,1,2,2,10))
if mibBuilder.loadTexts:agentSwitchIntfIpHelperAddressTable.setStatus(_A)
_AgentSwitchIntfIpHelperAddressEntry_Object=MibTableRow
agentSwitchIntfIpHelperAddressEntry=_AgentSwitchIntfIpHelperAddressEntry_Object((1,3,6,1,4,1,2356,16,1,2,2,10,1))
agentSwitchIntfIpHelperAddressEntry.setIndexNames((0,_E,_R),(0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:agentSwitchIntfIpHelperAddressEntry.setStatus(_A)
_AgentSwitchIntfIpHelperIpAddress_Type=IpAddress
_AgentSwitchIntfIpHelperIpAddress_Object=MibTableColumn
agentSwitchIntfIpHelperIpAddress=_AgentSwitchIntfIpHelperIpAddress_Object((1,3,6,1,4,1,2356,16,1,2,2,10,1,1),_AgentSwitchIntfIpHelperIpAddress_Type())
agentSwitchIntfIpHelperIpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperIpAddress.setStatus(_A)
class _AgentSwitchIntfIpHelperUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentSwitchIntfIpHelperUdpPort_Type.__name__=_K
_AgentSwitchIntfIpHelperUdpPort_Object=MibTableColumn
agentSwitchIntfIpHelperUdpPort=_AgentSwitchIntfIpHelperUdpPort_Object((1,3,6,1,4,1,2356,16,1,2,2,10,1,2),_AgentSwitchIntfIpHelperUdpPort_Type())
agentSwitchIntfIpHelperUdpPort.setMaxAccess(_J)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperUdpPort.setStatus(_A)
_AgentSwitchIntfIpHelperDiscard_Type=TruthValue
_AgentSwitchIntfIpHelperDiscard_Object=MibTableColumn
agentSwitchIntfIpHelperDiscard=_AgentSwitchIntfIpHelperDiscard_Object((1,3,6,1,4,1,2356,16,1,2,2,10,1,3),_AgentSwitchIntfIpHelperDiscard_Type())
agentSwitchIntfIpHelperDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperDiscard.setStatus(_H)
_AgentSwitchIntfIpHelperHitCount_Type=Unsigned32
_AgentSwitchIntfIpHelperHitCount_Object=MibTableColumn
agentSwitchIntfIpHelperHitCount=_AgentSwitchIntfIpHelperHitCount_Object((1,3,6,1,4,1,2356,16,1,2,2,10,1,4),_AgentSwitchIntfIpHelperHitCount_Type())
agentSwitchIntfIpHelperHitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperHitCount.setStatus(_A)
_AgentSwitchIntfIpHelperStatus_Type=RowStatus
_AgentSwitchIntfIpHelperStatus_Object=MibTableColumn
agentSwitchIntfIpHelperStatus=_AgentSwitchIntfIpHelperStatus_Object((1,3,6,1,4,1,2356,16,1,2,2,10,1,5),_AgentSwitchIntfIpHelperStatus_Type())
agentSwitchIntfIpHelperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperStatus.setStatus(_A)
class _AgentSwitchClearIpDefaultGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSwitchClearIpDefaultGateway_Type.__name__=_D
_AgentSwitchClearIpDefaultGateway_Object=MibScalar
agentSwitchClearIpDefaultGateway=_AgentSwitchClearIpDefaultGateway_Object((1,3,6,1,4,1,2356,16,1,2,2,11),_AgentSwitchClearIpDefaultGateway_Type())
agentSwitchClearIpDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchClearIpDefaultGateway.setStatus(_A)
_AgentRouterRipConfigGroup_ObjectIdentity=ObjectIdentity
agentRouterRipConfigGroup=_AgentRouterRipConfigGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,3))
class _AgentRouterRipAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRouterRipAdminState_Type.__name__=_D
_AgentRouterRipAdminState_Object=MibScalar
agentRouterRipAdminState=_AgentRouterRipAdminState_Object((1,3,6,1,4,1,2356,16,1,2,3,1),_AgentRouterRipAdminState_Type())
agentRouterRipAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRouterRipAdminState.setStatus(_A)
class _AgentRouterRipSplitHorizonMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),('simple',2),('poisonReverse',3)))
_AgentRouterRipSplitHorizonMode_Type.__name__=_D
_AgentRouterRipSplitHorizonMode_Object=MibScalar
agentRouterRipSplitHorizonMode=_AgentRouterRipSplitHorizonMode_Object((1,3,6,1,4,1,2356,16,1,2,3,2),_AgentRouterRipSplitHorizonMode_Type())
agentRouterRipSplitHorizonMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRouterRipSplitHorizonMode.setStatus(_A)
class _AgentRouterRipAutoSummaryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRouterRipAutoSummaryMode_Type.__name__=_D
_AgentRouterRipAutoSummaryMode_Object=MibScalar
agentRouterRipAutoSummaryMode=_AgentRouterRipAutoSummaryMode_Object((1,3,6,1,4,1,2356,16,1,2,3,3),_AgentRouterRipAutoSummaryMode_Type())
agentRouterRipAutoSummaryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRouterRipAutoSummaryMode.setStatus(_A)
class _AgentRouterRipHostRoutesAcceptMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRouterRipHostRoutesAcceptMode_Type.__name__=_D
_AgentRouterRipHostRoutesAcceptMode_Object=MibScalar
agentRouterRipHostRoutesAcceptMode=_AgentRouterRipHostRoutesAcceptMode_Object((1,3,6,1,4,1,2356,16,1,2,3,4),_AgentRouterRipHostRoutesAcceptMode_Type())
agentRouterRipHostRoutesAcceptMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRouterRipHostRoutesAcceptMode.setStatus(_A)
class _AgentRouterRipDefaultMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_AgentRouterRipDefaultMetric_Type.__name__=_D
_AgentRouterRipDefaultMetric_Object=MibScalar
agentRouterRipDefaultMetric=_AgentRouterRipDefaultMetric_Object((1,3,6,1,4,1,2356,16,1,2,3,5),_AgentRouterRipDefaultMetric_Type())
agentRouterRipDefaultMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRouterRipDefaultMetric.setStatus(_A)
class _AgentRouterRipDefaultMetricConfigured_Type(TruthValue):defaultValue=2
_AgentRouterRipDefaultMetricConfigured_Type.__name__=_L
_AgentRouterRipDefaultMetricConfigured_Object=MibScalar
agentRouterRipDefaultMetricConfigured=_AgentRouterRipDefaultMetricConfigured_Object((1,3,6,1,4,1,2356,16,1,2,3,6),_AgentRouterRipDefaultMetricConfigured_Type())
agentRouterRipDefaultMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRouterRipDefaultMetricConfigured.setStatus(_A)
class _AgentRouterRipDefaultInfoOriginate_Type(TruthValue):defaultValue=2
_AgentRouterRipDefaultInfoOriginate_Type.__name__=_L
_AgentRouterRipDefaultInfoOriginate_Object=MibScalar
agentRouterRipDefaultInfoOriginate=_AgentRouterRipDefaultInfoOriginate_Object((1,3,6,1,4,1,2356,16,1,2,3,7),_AgentRouterRipDefaultInfoOriginate_Type())
agentRouterRipDefaultInfoOriginate.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRouterRipDefaultInfoOriginate.setStatus(_A)
_AgentRipRouteRedistTable_Object=MibTable
agentRipRouteRedistTable=_AgentRipRouteRedistTable_Object((1,3,6,1,4,1,2356,16,1,2,3,8))
if mibBuilder.loadTexts:agentRipRouteRedistTable.setStatus(_A)
_AgentRipRouteRedistEntry_Object=MibTableRow
agentRipRouteRedistEntry=_AgentRipRouteRedistEntry_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1))
agentRipRouteRedistEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:agentRipRouteRedistEntry.setStatus(_A)
class _AgentRipRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_n,1),(_Q,2),('ospf',3),('bgp',4)))
_AgentRipRouteRedistSource_Type.__name__=_D
_AgentRipRouteRedistSource_Object=MibTableColumn
agentRipRouteRedistSource=_AgentRipRouteRedistSource_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,1),_AgentRipRouteRedistSource_Type())
agentRipRouteRedistSource.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRouteRedistSource.setStatus(_A)
class _AgentRipRouteRedistMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRipRouteRedistMode_Type.__name__=_D
_AgentRipRouteRedistMode_Object=MibTableColumn
agentRipRouteRedistMode=_AgentRipRouteRedistMode_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,2),_AgentRipRouteRedistMode_Type())
agentRipRouteRedistMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistMode.setStatus(_A)
class _AgentRipRouteRedistMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_AgentRipRouteRedistMetric_Type.__name__=_D
_AgentRipRouteRedistMetric_Object=MibTableColumn
agentRipRouteRedistMetric=_AgentRipRouteRedistMetric_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,3),_AgentRipRouteRedistMetric_Type())
agentRipRouteRedistMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistMetric.setStatus(_A)
class _AgentRipRouteRedistMetricConfigured_Type(TruthValue):defaultValue=2
_AgentRipRouteRedistMetricConfigured_Type.__name__=_L
_AgentRipRouteRedistMetricConfigured_Object=MibTableColumn
agentRipRouteRedistMetricConfigured=_AgentRipRouteRedistMetricConfigured_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,4),_AgentRipRouteRedistMetricConfigured_Type())
agentRipRouteRedistMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistMetricConfigured.setStatus(_A)
class _AgentRipRouteRedistMatchInternal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3)))
_AgentRipRouteRedistMatchInternal_Type.__name__=_D
_AgentRipRouteRedistMatchInternal_Object=MibTableColumn
agentRipRouteRedistMatchInternal=_AgentRipRouteRedistMatchInternal_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,5),_AgentRipRouteRedistMatchInternal_Type())
agentRipRouteRedistMatchInternal.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistMatchInternal.setStatus(_A)
class _AgentRipRouteRedistMatchExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3)))
_AgentRipRouteRedistMatchExternal1_Type.__name__=_D
_AgentRipRouteRedistMatchExternal1_Object=MibTableColumn
agentRipRouteRedistMatchExternal1=_AgentRipRouteRedistMatchExternal1_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,6),_AgentRipRouteRedistMatchExternal1_Type())
agentRipRouteRedistMatchExternal1.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistMatchExternal1.setStatus(_A)
class _AgentRipRouteRedistMatchExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3)))
_AgentRipRouteRedistMatchExternal2_Type.__name__=_D
_AgentRipRouteRedistMatchExternal2_Object=MibTableColumn
agentRipRouteRedistMatchExternal2=_AgentRipRouteRedistMatchExternal2_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,7),_AgentRipRouteRedistMatchExternal2_Type())
agentRipRouteRedistMatchExternal2.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistMatchExternal2.setStatus(_A)
class _AgentRipRouteRedistMatchNSSAExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3)))
_AgentRipRouteRedistMatchNSSAExternal1_Type.__name__=_D
_AgentRipRouteRedistMatchNSSAExternal1_Object=MibTableColumn
agentRipRouteRedistMatchNSSAExternal1=_AgentRipRouteRedistMatchNSSAExternal1_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,8),_AgentRipRouteRedistMatchNSSAExternal1_Type())
agentRipRouteRedistMatchNSSAExternal1.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistMatchNSSAExternal1.setStatus(_A)
class _AgentRipRouteRedistMatchNSSAExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3)))
_AgentRipRouteRedistMatchNSSAExternal2_Type.__name__=_D
_AgentRipRouteRedistMatchNSSAExternal2_Object=MibTableColumn
agentRipRouteRedistMatchNSSAExternal2=_AgentRipRouteRedistMatchNSSAExternal2_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,9),_AgentRipRouteRedistMatchNSSAExternal2_Type())
agentRipRouteRedistMatchNSSAExternal2.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistMatchNSSAExternal2.setStatus(_A)
class _AgentRipRouteRedistDistList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_AgentRipRouteRedistDistList_Type.__name__=_K
_AgentRipRouteRedistDistList_Object=MibTableColumn
agentRipRouteRedistDistList=_AgentRipRouteRedistDistList_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,10),_AgentRipRouteRedistDistList_Type())
agentRipRouteRedistDistList.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistDistList.setStatus(_A)
_AgentRipRouteRedistDistListConfigured_Type=TruthValue
_AgentRipRouteRedistDistListConfigured_Object=MibTableColumn
agentRipRouteRedistDistListConfigured=_AgentRipRouteRedistDistListConfigured_Object((1,3,6,1,4,1,2356,16,1,2,3,8,1,11),_AgentRipRouteRedistDistListConfigured_Type())
agentRipRouteRedistDistListConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRipRouteRedistDistListConfigured.setStatus(_A)
_AgentRip2IfConfTable_Object=MibTable
agentRip2IfConfTable=_AgentRip2IfConfTable_Object((1,3,6,1,4,1,2356,16,1,2,3,9))
if mibBuilder.loadTexts:agentRip2IfConfTable.setStatus(_A)
_AgentRip2IfConfEntry_Object=MibTableRow
agentRip2IfConfEntry=_AgentRip2IfConfEntry_Object((1,3,6,1,4,1,2356,16,1,2,3,9,1))
if mibBuilder.loadTexts:agentRip2IfConfEntry.setStatus(_A)
class _AgentRip2IfConfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentRip2IfConfAuthKeyId_Type.__name__=_D
_AgentRip2IfConfAuthKeyId_Object=MibTableColumn
agentRip2IfConfAuthKeyId=_AgentRip2IfConfAuthKeyId_Object((1,3,6,1,4,1,2356,16,1,2,3,9,1,1),_AgentRip2IfConfAuthKeyId_Type())
agentRip2IfConfAuthKeyId.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRip2IfConfAuthKeyId.setStatus(_A)
class _AgentRouterRipRoutePref_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentRouterRipRoutePref_Type.__name__=_D
_AgentRouterRipRoutePref_Object=MibScalar
agentRouterRipRoutePref=_AgentRouterRipRoutePref_Object((1,3,6,1,4,1,2356,16,1,2,3,10),_AgentRouterRipRoutePref_Type())
agentRouterRipRoutePref.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterRipRoutePref.setStatus(_A)
_AgentRouterOspfConfigGroup_ObjectIdentity=ObjectIdentity
agentRouterOspfConfigGroup=_AgentRouterOspfConfigGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,4))
class _AgentOspfDefaultMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16777214))
_AgentOspfDefaultMetric_Type.__name__=_D
_AgentOspfDefaultMetric_Object=MibScalar
agentOspfDefaultMetric=_AgentOspfDefaultMetric_Object((1,3,6,1,4,1,2356,16,1,2,4,1),_AgentOspfDefaultMetric_Type())
agentOspfDefaultMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfDefaultMetric.setStatus(_A)
class _AgentOspfDefaultMetricConfigured_Type(TruthValue):defaultValue=2
_AgentOspfDefaultMetricConfigured_Type.__name__=_L
_AgentOspfDefaultMetricConfigured_Object=MibScalar
agentOspfDefaultMetricConfigured=_AgentOspfDefaultMetricConfigured_Object((1,3,6,1,4,1,2356,16,1,2,4,2),_AgentOspfDefaultMetricConfigured_Type())
agentOspfDefaultMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfDefaultMetricConfigured.setStatus(_A)
class _AgentOspfDefaultInfoOriginate_Type(TruthValue):defaultValue=2
_AgentOspfDefaultInfoOriginate_Type.__name__=_L
_AgentOspfDefaultInfoOriginate_Object=MibScalar
agentOspfDefaultInfoOriginate=_AgentOspfDefaultInfoOriginate_Object((1,3,6,1,4,1,2356,16,1,2,4,3),_AgentOspfDefaultInfoOriginate_Type())
agentOspfDefaultInfoOriginate.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginate.setStatus(_A)
class _AgentOspfDefaultInfoOriginateAlways_Type(TruthValue):defaultValue=2
_AgentOspfDefaultInfoOriginateAlways_Type.__name__=_L
_AgentOspfDefaultInfoOriginateAlways_Object=MibScalar
agentOspfDefaultInfoOriginateAlways=_AgentOspfDefaultInfoOriginateAlways_Object((1,3,6,1,4,1,2356,16,1,2,4,4),_AgentOspfDefaultInfoOriginateAlways_Type())
agentOspfDefaultInfoOriginateAlways.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginateAlways.setStatus(_A)
class _AgentOspfDefaultInfoOriginateMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16777214))
_AgentOspfDefaultInfoOriginateMetric_Type.__name__=_D
_AgentOspfDefaultInfoOriginateMetric_Object=MibScalar
agentOspfDefaultInfoOriginateMetric=_AgentOspfDefaultInfoOriginateMetric_Object((1,3,6,1,4,1,2356,16,1,2,4,5),_AgentOspfDefaultInfoOriginateMetric_Type())
agentOspfDefaultInfoOriginateMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginateMetric.setStatus(_A)
_AgentOspfDefaultInfoOriginateMetricConfigured_Type=TruthValue
_AgentOspfDefaultInfoOriginateMetricConfigured_Object=MibScalar
agentOspfDefaultInfoOriginateMetricConfigured=_AgentOspfDefaultInfoOriginateMetricConfigured_Object((1,3,6,1,4,1,2356,16,1,2,4,6),_AgentOspfDefaultInfoOriginateMetricConfigured_Type())
agentOspfDefaultInfoOriginateMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginateMetricConfigured.setStatus(_A)
class _AgentOspfDefaultInfoOriginateMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_p,2)))
_AgentOspfDefaultInfoOriginateMetricType_Type.__name__=_D
_AgentOspfDefaultInfoOriginateMetricType_Object=MibScalar
agentOspfDefaultInfoOriginateMetricType=_AgentOspfDefaultInfoOriginateMetricType_Object((1,3,6,1,4,1,2356,16,1,2,4,7),_AgentOspfDefaultInfoOriginateMetricType_Type())
agentOspfDefaultInfoOriginateMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfDefaultInfoOriginateMetricType.setStatus(_A)
_AgentOspfRouteRedistTable_Object=MibTable
agentOspfRouteRedistTable=_AgentOspfRouteRedistTable_Object((1,3,6,1,4,1,2356,16,1,2,4,8))
if mibBuilder.loadTexts:agentOspfRouteRedistTable.setStatus(_A)
_AgentOspfRouteRedistEntry_Object=MibTableRow
agentOspfRouteRedistEntry=_AgentOspfRouteRedistEntry_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1))
agentOspfRouteRedistEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:agentOspfRouteRedistEntry.setStatus(_A)
class _AgentOspfRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_n,1),(_Q,2),('rip',3),('bgp',4)))
_AgentOspfRouteRedistSource_Type.__name__=_D
_AgentOspfRouteRedistSource_Object=MibTableColumn
agentOspfRouteRedistSource=_AgentOspfRouteRedistSource_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1,1),_AgentOspfRouteRedistSource_Type())
agentOspfRouteRedistSource.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRouteRedistSource.setStatus(_A)
class _AgentOspfRouteRedistMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentOspfRouteRedistMode_Type.__name__=_D
_AgentOspfRouteRedistMode_Object=MibTableColumn
agentOspfRouteRedistMode=_AgentOspfRouteRedistMode_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1,2),_AgentOspfRouteRedistMode_Type())
agentOspfRouteRedistMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRouteRedistMode.setStatus(_A)
class _AgentOspfRouteRedistMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_AgentOspfRouteRedistMetric_Type.__name__=_D
_AgentOspfRouteRedistMetric_Object=MibTableColumn
agentOspfRouteRedistMetric=_AgentOspfRouteRedistMetric_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1,3),_AgentOspfRouteRedistMetric_Type())
agentOspfRouteRedistMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRouteRedistMetric.setStatus(_A)
_AgentOspfRouteRedistMetricConfigured_Type=TruthValue
_AgentOspfRouteRedistMetricConfigured_Object=MibTableColumn
agentOspfRouteRedistMetricConfigured=_AgentOspfRouteRedistMetricConfigured_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1,4),_AgentOspfRouteRedistMetricConfigured_Type())
agentOspfRouteRedistMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRouteRedistMetricConfigured.setStatus(_A)
class _AgentOspfRouteRedistMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_p,2)))
_AgentOspfRouteRedistMetricType_Type.__name__=_D
_AgentOspfRouteRedistMetricType_Object=MibTableColumn
agentOspfRouteRedistMetricType=_AgentOspfRouteRedistMetricType_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1,5),_AgentOspfRouteRedistMetricType_Type())
agentOspfRouteRedistMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRouteRedistMetricType.setStatus(_A)
_AgentOspfRouteRedistTag_Type=Unsigned32
_AgentOspfRouteRedistTag_Object=MibTableColumn
agentOspfRouteRedistTag=_AgentOspfRouteRedistTag_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1,6),_AgentOspfRouteRedistTag_Type())
agentOspfRouteRedistTag.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRouteRedistTag.setStatus(_A)
class _AgentOspfRouteRedistSubnets_Type(TruthValue):defaultValue=2
_AgentOspfRouteRedistSubnets_Type.__name__=_L
_AgentOspfRouteRedistSubnets_Object=MibTableColumn
agentOspfRouteRedistSubnets=_AgentOspfRouteRedistSubnets_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1,7),_AgentOspfRouteRedistSubnets_Type())
agentOspfRouteRedistSubnets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRouteRedistSubnets.setStatus(_A)
class _AgentOspfRouteRedistDistList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_AgentOspfRouteRedistDistList_Type.__name__=_K
_AgentOspfRouteRedistDistList_Object=MibTableColumn
agentOspfRouteRedistDistList=_AgentOspfRouteRedistDistList_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1,8),_AgentOspfRouteRedistDistList_Type())
agentOspfRouteRedistDistList.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRouteRedistDistList.setStatus(_A)
_AgentOspfRouteRedistDistListConfigured_Type=TruthValue
_AgentOspfRouteRedistDistListConfigured_Object=MibTableColumn
agentOspfRouteRedistDistListConfigured=_AgentOspfRouteRedistDistListConfigured_Object((1,3,6,1,4,1,2356,16,1,2,4,8,1,9),_AgentOspfRouteRedistDistListConfigured_Type())
agentOspfRouteRedistDistListConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRouteRedistDistListConfigured.setStatus(_A)
_AgentOspfIfTable_Object=MibTable
agentOspfIfTable=_AgentOspfIfTable_Object((1,3,6,1,4,1,2356,16,1,2,4,9))
if mibBuilder.loadTexts:agentOspfIfTable.setStatus(_A)
_AgentOspfIfEntry_Object=MibTableRow
agentOspfIfEntry=_AgentOspfIfEntry_Object((1,3,6,1,4,1,2356,16,1,2,4,9,1))
if mibBuilder.loadTexts:agentOspfIfEntry.setStatus(_A)
class _AgentOspfIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOspfIfAuthKeyId_Type.__name__=_D
_AgentOspfIfAuthKeyId_Object=MibTableColumn
agentOspfIfAuthKeyId=_AgentOspfIfAuthKeyId_Object((1,3,6,1,4,1,2356,16,1,2,4,9,1,1),_AgentOspfIfAuthKeyId_Type())
agentOspfIfAuthKeyId.setMaxAccess(_I)
if mibBuilder.loadTexts:agentOspfIfAuthKeyId.setStatus(_A)
class _AgentOspfIfIpMtuIgnoreFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentOspfIfIpMtuIgnoreFlag_Type.__name__=_D
_AgentOspfIfIpMtuIgnoreFlag_Object=MibTableColumn
agentOspfIfIpMtuIgnoreFlag=_AgentOspfIfIpMtuIgnoreFlag_Object((1,3,6,1,4,1,2356,16,1,2,4,9,1,2),_AgentOspfIfIpMtuIgnoreFlag_Type())
agentOspfIfIpMtuIgnoreFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfIfIpMtuIgnoreFlag.setStatus(_A)
class _AgentOspfIfPassiveMode_Type(TruthValue):defaultValue=2
_AgentOspfIfPassiveMode_Type.__name__=_L
_AgentOspfIfPassiveMode_Object=MibTableColumn
agentOspfIfPassiveMode=_AgentOspfIfPassiveMode_Object((1,3,6,1,4,1,2356,16,1,2,4,9,1,3),_AgentOspfIfPassiveMode_Type())
agentOspfIfPassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfIfPassiveMode.setStatus(_A)
class _AgentOspfIfAdvertiseSecondaries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentOspfIfAdvertiseSecondaries_Type.__name__=_D
_AgentOspfIfAdvertiseSecondaries_Object=MibTableColumn
agentOspfIfAdvertiseSecondaries=_AgentOspfIfAdvertiseSecondaries_Object((1,3,6,1,4,1,2356,16,1,2,4,9,1,4),_AgentOspfIfAdvertiseSecondaries_Type())
agentOspfIfAdvertiseSecondaries.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfIfAdvertiseSecondaries.setStatus(_A)
_AgentOspfVirtIfTable_Object=MibTable
agentOspfVirtIfTable=_AgentOspfVirtIfTable_Object((1,3,6,1,4,1,2356,16,1,2,4,10))
if mibBuilder.loadTexts:agentOspfVirtIfTable.setStatus(_A)
_AgentOspfVirtIfEntry_Object=MibTableRow
agentOspfVirtIfEntry=_AgentOspfVirtIfEntry_Object((1,3,6,1,4,1,2356,16,1,2,4,10,1))
if mibBuilder.loadTexts:agentOspfVirtIfEntry.setStatus(_A)
class _AgentOspfVirtIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOspfVirtIfAuthKeyId_Type.__name__=_D
_AgentOspfVirtIfAuthKeyId_Object=MibTableColumn
agentOspfVirtIfAuthKeyId=_AgentOspfVirtIfAuthKeyId_Object((1,3,6,1,4,1,2356,16,1,2,4,10,1,1),_AgentOspfVirtIfAuthKeyId_Type())
agentOspfVirtIfAuthKeyId.setMaxAccess(_I)
if mibBuilder.loadTexts:agentOspfVirtIfAuthKeyId.setStatus(_A)
class _AgentRouterOspfRFC1583CompatibilityMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRouterOspfRFC1583CompatibilityMode_Type.__name__=_D
_AgentRouterOspfRFC1583CompatibilityMode_Object=MibScalar
agentRouterOspfRFC1583CompatibilityMode=_AgentRouterOspfRFC1583CompatibilityMode_Object((1,3,6,1,4,1,2356,16,1,2,4,11),_AgentRouterOspfRFC1583CompatibilityMode_Type())
agentRouterOspfRFC1583CompatibilityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRouterOspfRFC1583CompatibilityMode.setStatus(_A)
class _AgentOspfSpfDelayTime_Type(SpfTimerRange):defaultValue=5
_AgentOspfSpfDelayTime_Type.__name__=_X
_AgentOspfSpfDelayTime_Object=MibScalar
agentOspfSpfDelayTime=_AgentOspfSpfDelayTime_Object((1,3,6,1,4,1,2356,16,1,2,4,12),_AgentOspfSpfDelayTime_Type())
agentOspfSpfDelayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfSpfDelayTime.setStatus(_A)
class _AgentOspfSpfHoldTime_Type(SpfTimerRange):defaultValue=10
_AgentOspfSpfHoldTime_Type.__name__=_X
_AgentOspfSpfHoldTime_Object=MibScalar
agentOspfSpfHoldTime=_AgentOspfSpfHoldTime_Object((1,3,6,1,4,1,2356,16,1,2,4,13),_AgentOspfSpfHoldTime_Type())
agentOspfSpfHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfSpfHoldTime.setStatus(_A)
class _AgentOspfAutoCostRefBw_Type(AutoCostRefBw):defaultValue=100
_AgentOspfAutoCostRefBw_Type.__name__=_r
_AgentOspfAutoCostRefBw_Object=MibScalar
agentOspfAutoCostRefBw=_AgentOspfAutoCostRefBw_Object((1,3,6,1,4,1,2356,16,1,2,4,14),_AgentOspfAutoCostRefBw_Type())
agentOspfAutoCostRefBw.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfAutoCostRefBw.setStatus(_A)
_AgentOspfOpaqueLsaSupport_Type=TruthValue
_AgentOspfOpaqueLsaSupport_Object=MibScalar
agentOspfOpaqueLsaSupport=_AgentOspfOpaqueLsaSupport_Object((1,3,6,1,4,1,2356,16,1,2,4,15),_AgentOspfOpaqueLsaSupport_Type())
agentOspfOpaqueLsaSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfOpaqueLsaSupport.setStatus(_A)
_AgentOspfAreaOpaqueLsdbTable_Object=MibTable
agentOspfAreaOpaqueLsdbTable=_AgentOspfAreaOpaqueLsdbTable_Object((1,3,6,1,4,1,2356,16,1,2,4,16))
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbTable.setStatus(_A)
_AgentOspfAreaOpaqueLsdbEntry_Object=MibTableRow
agentOspfAreaOpaqueLsdbEntry=_AgentOspfAreaOpaqueLsdbEntry_Object((1,3,6,1,4,1,2356,16,1,2,4,16,1))
agentOspfAreaOpaqueLsdbEntry.setIndexNames((0,_E,_s),(0,_E,_t),(0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbEntry.setStatus(_A)
_AgentOspfAreaOpaqueLsdbAreaId_Type=IpAddress
_AgentOspfAreaOpaqueLsdbAreaId_Object=MibTableColumn
agentOspfAreaOpaqueLsdbAreaId=_AgentOspfAreaOpaqueLsdbAreaId_Object((1,3,6,1,4,1,2356,16,1,2,4,16,1,1),_AgentOspfAreaOpaqueLsdbAreaId_Type())
agentOspfAreaOpaqueLsdbAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbAreaId.setStatus(_A)
class _AgentOspfAreaOpaqueLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(10));namedValues=NamedValues(('areaOpaqueLink',10))
_AgentOspfAreaOpaqueLsdbType_Type.__name__=_D
_AgentOspfAreaOpaqueLsdbType_Object=MibTableColumn
agentOspfAreaOpaqueLsdbType=_AgentOspfAreaOpaqueLsdbType_Object((1,3,6,1,4,1,2356,16,1,2,4,16,1,2),_AgentOspfAreaOpaqueLsdbType_Type())
agentOspfAreaOpaqueLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbType.setStatus(_A)
_AgentOspfAreaOpaqueLsdbLsid_Type=IpAddress
_AgentOspfAreaOpaqueLsdbLsid_Object=MibTableColumn
agentOspfAreaOpaqueLsdbLsid=_AgentOspfAreaOpaqueLsdbLsid_Object((1,3,6,1,4,1,2356,16,1,2,4,16,1,3),_AgentOspfAreaOpaqueLsdbLsid_Type())
agentOspfAreaOpaqueLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbLsid.setStatus(_A)
_AgentOspfAreaOpaqueLsdbRouterId_Type=IpAddress
_AgentOspfAreaOpaqueLsdbRouterId_Object=MibTableColumn
agentOspfAreaOpaqueLsdbRouterId=_AgentOspfAreaOpaqueLsdbRouterId_Object((1,3,6,1,4,1,2356,16,1,2,4,16,1,4),_AgentOspfAreaOpaqueLsdbRouterId_Type())
agentOspfAreaOpaqueLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbRouterId.setStatus(_A)
_AgentOspfAreaOpaqueLsdbSequence_Type=Integer32
_AgentOspfAreaOpaqueLsdbSequence_Object=MibTableColumn
agentOspfAreaOpaqueLsdbSequence=_AgentOspfAreaOpaqueLsdbSequence_Object((1,3,6,1,4,1,2356,16,1,2,4,16,1,5),_AgentOspfAreaOpaqueLsdbSequence_Type())
agentOspfAreaOpaqueLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbSequence.setStatus(_A)
_AgentOspfAreaOpaqueLsdbAge_Type=Integer32
_AgentOspfAreaOpaqueLsdbAge_Object=MibTableColumn
agentOspfAreaOpaqueLsdbAge=_AgentOspfAreaOpaqueLsdbAge_Object((1,3,6,1,4,1,2356,16,1,2,4,16,1,6),_AgentOspfAreaOpaqueLsdbAge_Type())
agentOspfAreaOpaqueLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbAge.setUnits(_Y)
_AgentOspfAreaOpaqueLsdbChecksum_Type=Integer32
_AgentOspfAreaOpaqueLsdbChecksum_Object=MibTableColumn
agentOspfAreaOpaqueLsdbChecksum=_AgentOspfAreaOpaqueLsdbChecksum_Object((1,3,6,1,4,1,2356,16,1,2,4,16,1,7),_AgentOspfAreaOpaqueLsdbChecksum_Type())
agentOspfAreaOpaqueLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbChecksum.setStatus(_A)
class _AgentOspfAreaOpaqueLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_AgentOspfAreaOpaqueLsdbAdvertisement_Type.__name__=_V
_AgentOspfAreaOpaqueLsdbAdvertisement_Object=MibTableColumn
agentOspfAreaOpaqueLsdbAdvertisement=_AgentOspfAreaOpaqueLsdbAdvertisement_Object((1,3,6,1,4,1,2356,16,1,2,4,16,1,8),_AgentOspfAreaOpaqueLsdbAdvertisement_Type())
agentOspfAreaOpaqueLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAreaOpaqueLsdbAdvertisement.setStatus(_A)
_AgentOspfLocalLsdbTable_Object=MibTable
agentOspfLocalLsdbTable=_AgentOspfLocalLsdbTable_Object((1,3,6,1,4,1,2356,16,1,2,4,17))
if mibBuilder.loadTexts:agentOspfLocalLsdbTable.setStatus(_A)
_AgentOspfLocalLsdbEntry_Object=MibTableRow
agentOspfLocalLsdbEntry=_AgentOspfLocalLsdbEntry_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1))
agentOspfLocalLsdbEntry.setIndexNames((0,_E,_w),(0,_E,_x),(0,_E,_y),(0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:agentOspfLocalLsdbEntry.setStatus(_A)
_AgentOspfLocalLsdbIpAddress_Type=IpAddress
_AgentOspfLocalLsdbIpAddress_Object=MibTableColumn
agentOspfLocalLsdbIpAddress=_AgentOspfLocalLsdbIpAddress_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1,1),_AgentOspfLocalLsdbIpAddress_Type())
agentOspfLocalLsdbIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLocalLsdbIpAddress.setStatus(_A)
_AgentOspfLocalLsdbAddressLessIf_Type=InterfaceIndexOrZero
_AgentOspfLocalLsdbAddressLessIf_Object=MibTableColumn
agentOspfLocalLsdbAddressLessIf=_AgentOspfLocalLsdbAddressLessIf_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1,2),_AgentOspfLocalLsdbAddressLessIf_Type())
agentOspfLocalLsdbAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLocalLsdbAddressLessIf.setStatus(_A)
class _AgentOspfLocalLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(9));namedValues=NamedValues(('localOpaqueLink',9))
_AgentOspfLocalLsdbType_Type.__name__=_D
_AgentOspfLocalLsdbType_Object=MibTableColumn
agentOspfLocalLsdbType=_AgentOspfLocalLsdbType_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1,3),_AgentOspfLocalLsdbType_Type())
agentOspfLocalLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLocalLsdbType.setStatus(_A)
_AgentOspfLocalLsdbLsid_Type=IpAddress
_AgentOspfLocalLsdbLsid_Object=MibTableColumn
agentOspfLocalLsdbLsid=_AgentOspfLocalLsdbLsid_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1,4),_AgentOspfLocalLsdbLsid_Type())
agentOspfLocalLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLocalLsdbLsid.setStatus(_A)
_AgentOspfLocalLsdbRouterId_Type=RouterID
_AgentOspfLocalLsdbRouterId_Object=MibTableColumn
agentOspfLocalLsdbRouterId=_AgentOspfLocalLsdbRouterId_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1,5),_AgentOspfLocalLsdbRouterId_Type())
agentOspfLocalLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLocalLsdbRouterId.setStatus(_A)
_AgentOspfLocalLsdbSequence_Type=Integer32
_AgentOspfLocalLsdbSequence_Object=MibTableColumn
agentOspfLocalLsdbSequence=_AgentOspfLocalLsdbSequence_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1,6),_AgentOspfLocalLsdbSequence_Type())
agentOspfLocalLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLocalLsdbSequence.setStatus(_A)
_AgentOspfLocalLsdbAge_Type=Integer32
_AgentOspfLocalLsdbAge_Object=MibTableColumn
agentOspfLocalLsdbAge=_AgentOspfLocalLsdbAge_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1,7),_AgentOspfLocalLsdbAge_Type())
agentOspfLocalLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLocalLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:agentOspfLocalLsdbAge.setUnits(_Y)
_AgentOspfLocalLsdbChecksum_Type=Integer32
_AgentOspfLocalLsdbChecksum_Object=MibTableColumn
agentOspfLocalLsdbChecksum=_AgentOspfLocalLsdbChecksum_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1,8),_AgentOspfLocalLsdbChecksum_Type())
agentOspfLocalLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLocalLsdbChecksum.setStatus(_A)
class _AgentOspfLocalLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_AgentOspfLocalLsdbAdvertisement_Type.__name__=_V
_AgentOspfLocalLsdbAdvertisement_Object=MibTableColumn
agentOspfLocalLsdbAdvertisement=_AgentOspfLocalLsdbAdvertisement_Object((1,3,6,1,4,1,2356,16,1,2,4,17,1,9),_AgentOspfLocalLsdbAdvertisement_Type())
agentOspfLocalLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLocalLsdbAdvertisement.setStatus(_A)
_AgentOspfAsLsdbTable_Object=MibTable
agentOspfAsLsdbTable=_AgentOspfAsLsdbTable_Object((1,3,6,1,4,1,2356,16,1,2,4,18))
if mibBuilder.loadTexts:agentOspfAsLsdbTable.setStatus(_A)
_AgentOspfAsLsdbEntry_Object=MibTableRow
agentOspfAsLsdbEntry=_AgentOspfAsLsdbEntry_Object((1,3,6,1,4,1,2356,16,1,2,4,18,1))
agentOspfAsLsdbEntry.setIndexNames((0,_E,_A1),(0,_E,_A2),(0,_E,_A3))
if mibBuilder.loadTexts:agentOspfAsLsdbEntry.setStatus(_A)
class _AgentOspfAsLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(11));namedValues=NamedValues(('asOpaqueLink',11))
_AgentOspfAsLsdbType_Type.__name__=_D
_AgentOspfAsLsdbType_Object=MibTableColumn
agentOspfAsLsdbType=_AgentOspfAsLsdbType_Object((1,3,6,1,4,1,2356,16,1,2,4,18,1,1),_AgentOspfAsLsdbType_Type())
agentOspfAsLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAsLsdbType.setStatus(_A)
_AgentOspfAsLsdbLsid_Type=IpAddress
_AgentOspfAsLsdbLsid_Object=MibTableColumn
agentOspfAsLsdbLsid=_AgentOspfAsLsdbLsid_Object((1,3,6,1,4,1,2356,16,1,2,4,18,1,2),_AgentOspfAsLsdbLsid_Type())
agentOspfAsLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAsLsdbLsid.setStatus(_A)
_AgentOspfAsLsdbRouterId_Type=RouterID
_AgentOspfAsLsdbRouterId_Object=MibTableColumn
agentOspfAsLsdbRouterId=_AgentOspfAsLsdbRouterId_Object((1,3,6,1,4,1,2356,16,1,2,4,18,1,3),_AgentOspfAsLsdbRouterId_Type())
agentOspfAsLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAsLsdbRouterId.setStatus(_A)
_AgentOspfAsLsdbSequence_Type=Integer32
_AgentOspfAsLsdbSequence_Object=MibTableColumn
agentOspfAsLsdbSequence=_AgentOspfAsLsdbSequence_Object((1,3,6,1,4,1,2356,16,1,2,4,18,1,4),_AgentOspfAsLsdbSequence_Type())
agentOspfAsLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAsLsdbSequence.setStatus(_A)
_AgentOspfAsLsdbAge_Type=Integer32
_AgentOspfAsLsdbAge_Object=MibTableColumn
agentOspfAsLsdbAge=_AgentOspfAsLsdbAge_Object((1,3,6,1,4,1,2356,16,1,2,4,18,1,5),_AgentOspfAsLsdbAge_Type())
agentOspfAsLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAsLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:agentOspfAsLsdbAge.setUnits(_Y)
_AgentOspfAsLsdbChecksum_Type=Integer32
_AgentOspfAsLsdbChecksum_Object=MibTableColumn
agentOspfAsLsdbChecksum=_AgentOspfAsLsdbChecksum_Object((1,3,6,1,4,1,2356,16,1,2,4,18,1,6),_AgentOspfAsLsdbChecksum_Type())
agentOspfAsLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAsLsdbChecksum.setStatus(_A)
class _AgentOspfAsLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_AgentOspfAsLsdbAdvertisement_Type.__name__=_V
_AgentOspfAsLsdbAdvertisement_Object=MibTableColumn
agentOspfAsLsdbAdvertisement=_AgentOspfAsLsdbAdvertisement_Object((1,3,6,1,4,1,2356,16,1,2,4,18,1,7),_AgentOspfAsLsdbAdvertisement_Type())
agentOspfAsLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfAsLsdbAdvertisement.setStatus(_A)
class _AgentOspfDefaultPassiveMode_Type(TruthValue):defaultValue=2
_AgentOspfDefaultPassiveMode_Type.__name__=_L
_AgentOspfDefaultPassiveMode_Object=MibScalar
agentOspfDefaultPassiveMode=_AgentOspfDefaultPassiveMode_Object((1,3,6,1,4,1,2356,16,1,2,4,19),_AgentOspfDefaultPassiveMode_Type())
agentOspfDefaultPassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfDefaultPassiveMode.setStatus(_A)
class _AgentOspfRoutePrefIntraArea_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentOspfRoutePrefIntraArea_Type.__name__=_D
_AgentOspfRoutePrefIntraArea_Object=MibScalar
agentOspfRoutePrefIntraArea=_AgentOspfRoutePrefIntraArea_Object((1,3,6,1,4,1,2356,16,1,2,4,20),_AgentOspfRoutePrefIntraArea_Type())
agentOspfRoutePrefIntraArea.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRoutePrefIntraArea.setStatus(_A)
class _AgentOspfRoutePrefInterArea_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentOspfRoutePrefInterArea_Type.__name__=_D
_AgentOspfRoutePrefInterArea_Object=MibScalar
agentOspfRoutePrefInterArea=_AgentOspfRoutePrefInterArea_Object((1,3,6,1,4,1,2356,16,1,2,4,21),_AgentOspfRoutePrefInterArea_Type())
agentOspfRoutePrefInterArea.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRoutePrefInterArea.setStatus(_A)
class _AgentOspfRoutePrefExternal_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentOspfRoutePrefExternal_Type.__name__=_D
_AgentOspfRoutePrefExternal_Object=MibScalar
agentOspfRoutePrefExternal=_AgentOspfRoutePrefExternal_Object((1,3,6,1,4,1,2356,16,1,2,4,22),_AgentOspfRoutePrefExternal_Type())
agentOspfRoutePrefExternal.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOspfRoutePrefExternal.setStatus(_A)
_AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity=ObjectIdentity
agentSnmpTrapFlagsConfigGroupLayer3=_AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,5))
class _AgentSnmpVRRPNewMasterTrapFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSnmpVRRPNewMasterTrapFlag_Type.__name__=_D
_AgentSnmpVRRPNewMasterTrapFlag_Object=MibScalar
agentSnmpVRRPNewMasterTrapFlag=_AgentSnmpVRRPNewMasterTrapFlag_Object((1,3,6,1,4,1,2356,16,1,2,5,1),_AgentSnmpVRRPNewMasterTrapFlag_Type())
agentSnmpVRRPNewMasterTrapFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSnmpVRRPNewMasterTrapFlag.setStatus(_A)
class _AgentSnmpVRRPAuthFailureTrapFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSnmpVRRPAuthFailureTrapFlag_Type.__name__=_D
_AgentSnmpVRRPAuthFailureTrapFlag_Object=MibScalar
agentSnmpVRRPAuthFailureTrapFlag=_AgentSnmpVRRPAuthFailureTrapFlag_Object((1,3,6,1,4,1,2356,16,1,2,5,2),_AgentSnmpVRRPAuthFailureTrapFlag_Type())
agentSnmpVRRPAuthFailureTrapFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSnmpVRRPAuthFailureTrapFlag.setStatus(_A)
_AgentBootpDhcpRelayGroup_ObjectIdentity=ObjectIdentity
agentBootpDhcpRelayGroup=_AgentBootpDhcpRelayGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,6))
class _AgentBootpDhcpRelayMaxHopCount_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AgentBootpDhcpRelayMaxHopCount_Type.__name__=_D
_AgentBootpDhcpRelayMaxHopCount_Object=MibScalar
agentBootpDhcpRelayMaxHopCount=_AgentBootpDhcpRelayMaxHopCount_Object((1,3,6,1,4,1,2356,16,1,2,6,1),_AgentBootpDhcpRelayMaxHopCount_Type())
agentBootpDhcpRelayMaxHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayMaxHopCount.setStatus(_A)
_AgentBootpDhcpRelayForwardingIp_Type=IpAddress
_AgentBootpDhcpRelayForwardingIp_Object=MibScalar
agentBootpDhcpRelayForwardingIp=_AgentBootpDhcpRelayForwardingIp_Object((1,3,6,1,4,1,2356,16,1,2,6,2),_AgentBootpDhcpRelayForwardingIp_Type())
agentBootpDhcpRelayForwardingIp.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayForwardingIp.setStatus(_H)
class _AgentBootpDhcpRelayForwardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentBootpDhcpRelayForwardMode_Type.__name__=_D
_AgentBootpDhcpRelayForwardMode_Object=MibScalar
agentBootpDhcpRelayForwardMode=_AgentBootpDhcpRelayForwardMode_Object((1,3,6,1,4,1,2356,16,1,2,6,3),_AgentBootpDhcpRelayForwardMode_Type())
agentBootpDhcpRelayForwardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayForwardMode.setStatus(_H)
class _AgentBootpDhcpRelayMinWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AgentBootpDhcpRelayMinWaitTime_Type.__name__=_D
_AgentBootpDhcpRelayMinWaitTime_Object=MibScalar
agentBootpDhcpRelayMinWaitTime=_AgentBootpDhcpRelayMinWaitTime_Object((1,3,6,1,4,1,2356,16,1,2,6,4),_AgentBootpDhcpRelayMinWaitTime_Type())
agentBootpDhcpRelayMinWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayMinWaitTime.setStatus(_A)
class _AgentBootpDhcpRelayCircuitIdOptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_W,3)))
_AgentBootpDhcpRelayCircuitIdOptionMode_Type.__name__=_D
_AgentBootpDhcpRelayCircuitIdOptionMode_Object=MibScalar
agentBootpDhcpRelayCircuitIdOptionMode=_AgentBootpDhcpRelayCircuitIdOptionMode_Object((1,3,6,1,4,1,2356,16,1,2,6,5),_AgentBootpDhcpRelayCircuitIdOptionMode_Type())
agentBootpDhcpRelayCircuitIdOptionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayCircuitIdOptionMode.setStatus(_A)
_AgentBootpDhcpRelayNumOfRequestsReceived_Type=Integer32
_AgentBootpDhcpRelayNumOfRequestsReceived_Object=MibScalar
agentBootpDhcpRelayNumOfRequestsReceived=_AgentBootpDhcpRelayNumOfRequestsReceived_Object((1,3,6,1,4,1,2356,16,1,2,6,6),_AgentBootpDhcpRelayNumOfRequestsReceived_Type())
agentBootpDhcpRelayNumOfRequestsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayNumOfRequestsReceived.setStatus(_H)
_AgentBootpDhcpRelayNumOfRequestsForwarded_Type=Integer32
_AgentBootpDhcpRelayNumOfRequestsForwarded_Object=MibScalar
agentBootpDhcpRelayNumOfRequestsForwarded=_AgentBootpDhcpRelayNumOfRequestsForwarded_Object((1,3,6,1,4,1,2356,16,1,2,6,7),_AgentBootpDhcpRelayNumOfRequestsForwarded_Type())
agentBootpDhcpRelayNumOfRequestsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayNumOfRequestsForwarded.setStatus(_H)
_AgentBootpDhcpRelayNumOfDiscards_Type=Integer32
_AgentBootpDhcpRelayNumOfDiscards_Object=MibScalar
agentBootpDhcpRelayNumOfDiscards=_AgentBootpDhcpRelayNumOfDiscards_Object((1,3,6,1,4,1,2356,16,1,2,6,8),_AgentBootpDhcpRelayNumOfDiscards_Type())
agentBootpDhcpRelayNumOfDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayNumOfDiscards.setStatus(_H)
_AgentECMPGroup_ObjectIdentity=ObjectIdentity
agentECMPGroup=_AgentECMPGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,7))
class _AgentECMPOspfMaxPaths_Type(Integer32):defaultValue=4
_AgentECMPOspfMaxPaths_Type.__name__=_D
_AgentECMPOspfMaxPaths_Object=MibScalar
agentECMPOspfMaxPaths=_AgentECMPOspfMaxPaths_Object((1,3,6,1,4,1,2356,16,1,2,7,1),_AgentECMPOspfMaxPaths_Type())
agentECMPOspfMaxPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:agentECMPOspfMaxPaths.setStatus(_A)
_AgentRouterVrrpConfigGroup_ObjectIdentity=ObjectIdentity
agentRouterVrrpConfigGroup=_AgentRouterVrrpConfigGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,8))
class _AgentRouterVrrpAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRouterVrrpAdminState_Type.__name__=_D
_AgentRouterVrrpAdminState_Object=MibScalar
agentRouterVrrpAdminState=_AgentRouterVrrpAdminState_Object((1,3,6,1,4,1,2356,16,1,2,8,1),_AgentRouterVrrpAdminState_Type())
agentRouterVrrpAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRouterVrrpAdminState.setStatus(_A)
_AgentRouterVrrpConfiguredTable_Object=MibTable
agentRouterVrrpConfiguredTable=_AgentRouterVrrpConfiguredTable_Object((1,3,6,1,4,1,2356,16,1,2,8,2))
if mibBuilder.loadTexts:agentRouterVrrpConfiguredTable.setStatus(_A)
_AgentRouterVrrpConfiguredEntry_Object=MibTableRow
agentRouterVrrpConfiguredEntry=_AgentRouterVrrpConfiguredEntry_Object((1,3,6,1,4,1,2356,16,1,2,8,2,1))
agentRouterVrrpConfiguredEntry.setIndexNames((0,_M,_N),(0,_O,_P))
if mibBuilder.loadTexts:agentRouterVrrpConfiguredEntry.setStatus(_A)
class _AgentRouterVrrpConfiguredPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AgentRouterVrrpConfiguredPriority_Type.__name__=_D
_AgentRouterVrrpConfiguredPriority_Object=MibTableColumn
agentRouterVrrpConfiguredPriority=_AgentRouterVrrpConfiguredPriority_Object((1,3,6,1,4,1,2356,16,1,2,8,2,1,1),_AgentRouterVrrpConfiguredPriority_Type())
agentRouterVrrpConfiguredPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterVrrpConfiguredPriority.setStatus(_A)
_AgentVrrpOperations_ObjectIdentity=ObjectIdentity
agentVrrpOperations=_AgentVrrpOperations_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,9))
_AgentRouterVrrpOperTable_Object=MibTable
agentRouterVrrpOperTable=_AgentRouterVrrpOperTable_Object((1,3,6,1,4,1,2356,16,1,2,9,1))
if mibBuilder.loadTexts:agentRouterVrrpOperTable.setStatus(_H)
_AgentRouterVrrpOperEntry_Object=MibTableRow
agentRouterVrrpOperEntry=_AgentRouterVrrpOperEntry_Object((1,3,6,1,4,1,2356,16,1,2,9,1,1))
agentRouterVrrpOperEntry.setIndexNames((0,_M,_N),(0,_O,_P))
if mibBuilder.loadTexts:agentRouterVrrpOperEntry.setStatus(_H)
class _AgentRouterVrrpOperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentRouterVrrpOperPriority_Type.__name__=_D
_AgentRouterVrrpOperPriority_Object=MibTableColumn
agentRouterVrrpOperPriority=_AgentRouterVrrpOperPriority_Object((1,3,6,1,4,1,2356,16,1,2,9,1,1,1),_AgentRouterVrrpOperPriority_Type())
agentRouterVrrpOperPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterVrrpOperPriority.setStatus(_H)
_AgentRouterVrrpTrackGroup_ObjectIdentity=ObjectIdentity
agentRouterVrrpTrackGroup=_AgentRouterVrrpTrackGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,10))
_AgentRouterVrrpTrackIntfTable_Object=MibTable
agentRouterVrrpTrackIntfTable=_AgentRouterVrrpTrackIntfTable_Object((1,3,6,1,4,1,2356,16,1,2,10,1))
if mibBuilder.loadTexts:agentRouterVrrpTrackIntfTable.setStatus(_A)
_AgentRouterVrrpTrackIntfEntry_Object=MibTableRow
agentRouterVrrpTrackIntfEntry=_AgentRouterVrrpTrackIntfEntry_Object((1,3,6,1,4,1,2356,16,1,2,10,1,1))
agentRouterVrrpTrackIntfEntry.setIndexNames((0,_M,_N),(0,_O,_P),(0,_E,_A4))
if mibBuilder.loadTexts:agentRouterVrrpTrackIntfEntry.setStatus(_A)
_AgentRouterVrrpTrackIntf_Type=InterfaceIndex
_AgentRouterVrrpTrackIntf_Object=MibTableColumn
agentRouterVrrpTrackIntf=_AgentRouterVrrpTrackIntf_Object((1,3,6,1,4,1,2356,16,1,2,10,1,1,1),_AgentRouterVrrpTrackIntf_Type())
agentRouterVrrpTrackIntf.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackIntf.setStatus(_A)
class _AgentRouterVrrpTrackIfPrioDec_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AgentRouterVrrpTrackIfPrioDec_Type.__name__=_D
_AgentRouterVrrpTrackIfPrioDec_Object=MibTableColumn
agentRouterVrrpTrackIfPrioDec=_AgentRouterVrrpTrackIfPrioDec_Object((1,3,6,1,4,1,2356,16,1,2,10,1,1,2),_AgentRouterVrrpTrackIfPrioDec_Type())
agentRouterVrrpTrackIfPrioDec.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackIfPrioDec.setStatus(_A)
_AgentRouterVrrpTrackIfState_Type=TruthValue
_AgentRouterVrrpTrackIfState_Object=MibTableColumn
agentRouterVrrpTrackIfState=_AgentRouterVrrpTrackIfState_Object((1,3,6,1,4,1,2356,16,1,2,10,1,1,3),_AgentRouterVrrpTrackIfState_Type())
agentRouterVrrpTrackIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterVrrpTrackIfState.setStatus(_A)
_AgentRouterVrrpTrackIfStatus_Type=RowStatus
_AgentRouterVrrpTrackIfStatus_Object=MibTableColumn
agentRouterVrrpTrackIfStatus=_AgentRouterVrrpTrackIfStatus_Object((1,3,6,1,4,1,2356,16,1,2,10,1,1,4),_AgentRouterVrrpTrackIfStatus_Type())
agentRouterVrrpTrackIfStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackIfStatus.setStatus(_A)
_AgentRouterVrrpTrackRouteTable_Object=MibTable
agentRouterVrrpTrackRouteTable=_AgentRouterVrrpTrackRouteTable_Object((1,3,6,1,4,1,2356,16,1,2,10,2))
if mibBuilder.loadTexts:agentRouterVrrpTrackRouteTable.setStatus(_A)
_AgentRouterVrrpTrackRouteEntry_Object=MibTableRow
agentRouterVrrpTrackRouteEntry=_AgentRouterVrrpTrackRouteEntry_Object((1,3,6,1,4,1,2356,16,1,2,10,2,1))
agentRouterVrrpTrackRouteEntry.setIndexNames((0,_M,_N),(0,_O,_P),(0,_E,_A5),(0,_E,_A6))
if mibBuilder.loadTexts:agentRouterVrrpTrackRouteEntry.setStatus(_A)
_AgentRouterVrrpTrackRtPfx_Type=IpAddress
_AgentRouterVrrpTrackRtPfx_Object=MibTableColumn
agentRouterVrrpTrackRtPfx=_AgentRouterVrrpTrackRtPfx_Object((1,3,6,1,4,1,2356,16,1,2,10,2,1,1),_AgentRouterVrrpTrackRtPfx_Type())
agentRouterVrrpTrackRtPfx.setMaxAccess(_J)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtPfx.setStatus(_A)
class _AgentRouterVrrpTrackRtPfxLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AgentRouterVrrpTrackRtPfxLen_Type.__name__=_D
_AgentRouterVrrpTrackRtPfxLen_Object=MibTableColumn
agentRouterVrrpTrackRtPfxLen=_AgentRouterVrrpTrackRtPfxLen_Object((1,3,6,1,4,1,2356,16,1,2,10,2,1,2),_AgentRouterVrrpTrackRtPfxLen_Type())
agentRouterVrrpTrackRtPfxLen.setMaxAccess(_J)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtPfxLen.setStatus(_A)
class _AgentRouterVrrpTrackRtPrioDec_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AgentRouterVrrpTrackRtPrioDec_Type.__name__=_D
_AgentRouterVrrpTrackRtPrioDec_Object=MibTableColumn
agentRouterVrrpTrackRtPrioDec=_AgentRouterVrrpTrackRtPrioDec_Object((1,3,6,1,4,1,2356,16,1,2,10,2,1,3),_AgentRouterVrrpTrackRtPrioDec_Type())
agentRouterVrrpTrackRtPrioDec.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtPrioDec.setStatus(_A)
_AgentRouterVrrpTrackRtReachable_Type=TruthValue
_AgentRouterVrrpTrackRtReachable_Object=MibTableColumn
agentRouterVrrpTrackRtReachable=_AgentRouterVrrpTrackRtReachable_Object((1,3,6,1,4,1,2356,16,1,2,10,2,1,4),_AgentRouterVrrpTrackRtReachable_Type())
agentRouterVrrpTrackRtReachable.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtReachable.setStatus(_A)
_AgentRouterVrrpTrackRtStatus_Type=RowStatus
_AgentRouterVrrpTrackRtStatus_Object=MibTableColumn
agentRouterVrrpTrackRtStatus=_AgentRouterVrrpTrackRtStatus_Object((1,3,6,1,4,1,2356,16,1,2,10,2,1,5),_AgentRouterVrrpTrackRtStatus_Type())
agentRouterVrrpTrackRtStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRouterVrrpTrackRtStatus.setStatus(_A)
_AgentIpHelperGroup_ObjectIdentity=ObjectIdentity
agentIpHelperGroup=_AgentIpHelperGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,11))
class _AgentIpHelperAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentIpHelperAdminMode_Type.__name__=_D
_AgentIpHelperAdminMode_Object=MibScalar
agentIpHelperAdminMode=_AgentIpHelperAdminMode_Object((1,3,6,1,4,1,2356,16,1,2,11,1),_AgentIpHelperAdminMode_Type())
agentIpHelperAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpHelperAdminMode.setStatus(_A)
_AgentDhcpClientMsgsReceived_Type=Counter32
_AgentDhcpClientMsgsReceived_Object=MibScalar
agentDhcpClientMsgsReceived=_AgentDhcpClientMsgsReceived_Object((1,3,6,1,4,1,2356,16,1,2,11,2),_AgentDhcpClientMsgsReceived_Type())
agentDhcpClientMsgsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpClientMsgsReceived.setStatus(_A)
_AgentDhcpClientMsgsRelayed_Type=Counter32
_AgentDhcpClientMsgsRelayed_Object=MibScalar
agentDhcpClientMsgsRelayed=_AgentDhcpClientMsgsRelayed_Object((1,3,6,1,4,1,2356,16,1,2,11,3),_AgentDhcpClientMsgsRelayed_Type())
agentDhcpClientMsgsRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpClientMsgsRelayed.setStatus(_A)
_AgentDhcpServerMsgsReceived_Type=Counter32
_AgentDhcpServerMsgsReceived_Object=MibScalar
agentDhcpServerMsgsReceived=_AgentDhcpServerMsgsReceived_Object((1,3,6,1,4,1,2356,16,1,2,11,4),_AgentDhcpServerMsgsReceived_Type())
agentDhcpServerMsgsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerMsgsReceived.setStatus(_A)
_AgentDhcpServerMsgsRelayed_Type=Counter32
_AgentDhcpServerMsgsRelayed_Object=MibScalar
agentDhcpServerMsgsRelayed=_AgentDhcpServerMsgsRelayed_Object((1,3,6,1,4,1,2356,16,1,2,11,5),_AgentDhcpServerMsgsRelayed_Type())
agentDhcpServerMsgsRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerMsgsRelayed.setStatus(_A)
_AgentUdpClientMsgsReceived_Type=Counter32
_AgentUdpClientMsgsReceived_Object=MibScalar
agentUdpClientMsgsReceived=_AgentUdpClientMsgsReceived_Object((1,3,6,1,4,1,2356,16,1,2,11,6),_AgentUdpClientMsgsReceived_Type())
agentUdpClientMsgsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUdpClientMsgsReceived.setStatus(_A)
_AgentUdpClientMsgsRelayed_Type=Counter32
_AgentUdpClientMsgsRelayed_Object=MibScalar
agentUdpClientMsgsRelayed=_AgentUdpClientMsgsRelayed_Object((1,3,6,1,4,1,2356,16,1,2,11,7),_AgentUdpClientMsgsRelayed_Type())
agentUdpClientMsgsRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUdpClientMsgsRelayed.setStatus(_A)
_AgentSwitchIpHelperAddressTable_Object=MibTable
agentSwitchIpHelperAddressTable=_AgentSwitchIpHelperAddressTable_Object((1,3,6,1,4,1,2356,16,1,2,11,8))
if mibBuilder.loadTexts:agentSwitchIpHelperAddressTable.setStatus(_A)
_AgentSwitchIpHelperAddressEntry_Object=MibTableRow
agentSwitchIpHelperAddressEntry=_AgentSwitchIpHelperAddressEntry_Object((1,3,6,1,4,1,2356,16,1,2,11,8,1))
agentSwitchIpHelperAddressEntry.setIndexNames((0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:agentSwitchIpHelperAddressEntry.setStatus(_A)
_AgentSwitchIpHelperAddress_Type=IpAddress
_AgentSwitchIpHelperAddress_Object=MibTableColumn
agentSwitchIpHelperAddress=_AgentSwitchIpHelperAddress_Object((1,3,6,1,4,1,2356,16,1,2,11,8,1,1),_AgentSwitchIpHelperAddress_Type())
agentSwitchIpHelperAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpHelperAddress.setStatus(_A)
class _AgentSwitchIpHelperUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentSwitchIpHelperUdpPort_Type.__name__=_K
_AgentSwitchIpHelperUdpPort_Object=MibTableColumn
agentSwitchIpHelperUdpPort=_AgentSwitchIpHelperUdpPort_Object((1,3,6,1,4,1,2356,16,1,2,11,8,1,2),_AgentSwitchIpHelperUdpPort_Type())
agentSwitchIpHelperUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpHelperUdpPort.setStatus(_A)
_AgentSwitchIpHelperHitCount_Type=Unsigned32
_AgentSwitchIpHelperHitCount_Object=MibTableColumn
agentSwitchIpHelperHitCount=_AgentSwitchIpHelperHitCount_Object((1,3,6,1,4,1,2356,16,1,2,11,8,1,3),_AgentSwitchIpHelperHitCount_Type())
agentSwitchIpHelperHitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpHelperHitCount.setStatus(_A)
_AgentSwitchIpHelperStatus_Type=RowStatus
_AgentSwitchIpHelperStatus_Object=MibTableColumn
agentSwitchIpHelperStatus=_AgentSwitchIpHelperStatus_Object((1,3,6,1,4,1,2356,16,1,2,11,8,1,4),_AgentSwitchIpHelperStatus_Type())
agentSwitchIpHelperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIpHelperStatus.setStatus(_A)
_AgentUdpClientMsgsTtlExpired_Type=Counter32
_AgentUdpClientMsgsTtlExpired_Object=MibScalar
agentUdpClientMsgsTtlExpired=_AgentUdpClientMsgsTtlExpired_Object((1,3,6,1,4,1,2356,16,1,2,11,9),_AgentUdpClientMsgsTtlExpired_Type())
agentUdpClientMsgsTtlExpired.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUdpClientMsgsTtlExpired.setStatus(_A)
_AgentUdpClientMsgsDiscarded_Type=Counter32
_AgentUdpClientMsgsDiscarded_Object=MibScalar
agentUdpClientMsgsDiscarded=_AgentUdpClientMsgsDiscarded_Object((1,3,6,1,4,1,2356,16,1,2,11,10),_AgentUdpClientMsgsDiscarded_Type())
agentUdpClientMsgsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUdpClientMsgsDiscarded.setStatus(_A)
_AgentInternalVlanGroup_ObjectIdentity=ObjectIdentity
agentInternalVlanGroup=_AgentInternalVlanGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,12))
class _AgentInternalVlanBase_Type(Integer32):defaultValue=4093
_AgentInternalVlanBase_Type.__name__=_D
_AgentInternalVlanBase_Object=MibScalar
agentInternalVlanBase=_AgentInternalVlanBase_Object((1,3,6,1,4,1,2356,16,1,2,12,1),_AgentInternalVlanBase_Type())
agentInternalVlanBase.setMaxAccess(_C)
if mibBuilder.loadTexts:agentInternalVlanBase.setStatus(_A)
class _AgentInternalVlanPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ascending',0),('descending',1)))
_AgentInternalVlanPolicy_Type.__name__=_D
_AgentInternalVlanPolicy_Object=MibScalar
agentInternalVlanPolicy=_AgentInternalVlanPolicy_Object((1,3,6,1,4,1,2356,16,1,2,12,2),_AgentInternalVlanPolicy_Type())
agentInternalVlanPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:agentInternalVlanPolicy.setStatus(_A)
_AgentSwitchInternalVlanTable_Object=MibTable
agentSwitchInternalVlanTable=_AgentSwitchInternalVlanTable_Object((1,3,6,1,4,1,2356,16,1,2,12,3))
if mibBuilder.loadTexts:agentSwitchInternalVlanTable.setStatus(_A)
_AgentSwitchInternalVlanEntry_Object=MibTableRow
agentSwitchInternalVlanEntry=_AgentSwitchInternalVlanEntry_Object((1,3,6,1,4,1,2356,16,1,2,12,3,1))
agentSwitchInternalVlanEntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:agentSwitchInternalVlanEntry.setStatus(_A)
class _AgentSwitchInternalVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchInternalVlanId_Type.__name__=_D
_AgentSwitchInternalVlanId_Object=MibTableColumn
agentSwitchInternalVlanId=_AgentSwitchInternalVlanId_Object((1,3,6,1,4,1,2356,16,1,2,12,3,1,1),_AgentSwitchInternalVlanId_Type())
agentSwitchInternalVlanId.setMaxAccess(_J)
if mibBuilder.loadTexts:agentSwitchInternalVlanId.setStatus(_A)
_AgentSwitchInternalVlanIfIndex_Type=Integer32
_AgentSwitchInternalVlanIfIndex_Object=MibTableColumn
agentSwitchInternalVlanIfIndex=_AgentSwitchInternalVlanIfIndex_Object((1,3,6,1,4,1,2356,16,1,2,12,3,1,2),_AgentSwitchInternalVlanIfIndex_Type())
agentSwitchInternalVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchInternalVlanIfIndex.setStatus(_A)
_AgentOspfQueueGroup_ObjectIdentity=ObjectIdentity
agentOspfQueueGroup=_AgentOspfQueueGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,13))
_AgentOspfQueueTable_Object=MibTable
agentOspfQueueTable=_AgentOspfQueueTable_Object((1,3,6,1,4,1,2356,16,1,2,13,1))
if mibBuilder.loadTexts:agentOspfQueueTable.setStatus(_A)
_AgentOspfQueueEntry_Object=MibTableRow
agentOspfQueueEntry=_AgentOspfQueueEntry_Object((1,3,6,1,4,1,2356,16,1,2,13,1,1))
agentOspfQueueEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:agentOspfQueueEntry.setStatus(_A)
_AgentOspfQueueIndex_Type=Unsigned32
_AgentOspfQueueIndex_Object=MibTableColumn
agentOspfQueueIndex=_AgentOspfQueueIndex_Object((1,3,6,1,4,1,2356,16,1,2,13,1,1,1),_AgentOspfQueueIndex_Type())
agentOspfQueueIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentOspfQueueIndex.setStatus(_A)
_AgentOspfQueueName_Type=DisplayString
_AgentOspfQueueName_Object=MibTableColumn
agentOspfQueueName=_AgentOspfQueueName_Object((1,3,6,1,4,1,2356,16,1,2,13,1,1,2),_AgentOspfQueueName_Type())
agentOspfQueueName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfQueueName.setStatus(_A)
_AgentOspfQueueLength_Type=Gauge32
_AgentOspfQueueLength_Object=MibTableColumn
agentOspfQueueLength=_AgentOspfQueueLength_Object((1,3,6,1,4,1,2356,16,1,2,13,1,1,3),_AgentOspfQueueLength_Type())
agentOspfQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfQueueLength.setStatus(_A)
_AgentOspfQueueHigh_Type=Gauge32
_AgentOspfQueueHigh_Object=MibTableColumn
agentOspfQueueHigh=_AgentOspfQueueHigh_Object((1,3,6,1,4,1,2356,16,1,2,13,1,1,4),_AgentOspfQueueHigh_Type())
agentOspfQueueHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfQueueHigh.setStatus(_A)
_AgentOspfQueueDrops_Type=Counter32
_AgentOspfQueueDrops_Object=MibTableColumn
agentOspfQueueDrops=_AgentOspfQueueDrops_Object((1,3,6,1,4,1,2356,16,1,2,13,1,1,5),_AgentOspfQueueDrops_Type())
agentOspfQueueDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfQueueDrops.setStatus(_A)
_AgentOspfQueueLimit_Type=Unsigned32
_AgentOspfQueueLimit_Object=MibTableColumn
agentOspfQueueLimit=_AgentOspfQueueLimit_Object((1,3,6,1,4,1,2356,16,1,2,13,1,1,6),_AgentOspfQueueLimit_Type())
agentOspfQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfQueueLimit.setStatus(_A)
_AgentOspfPacketStatsGroup_ObjectIdentity=ObjectIdentity
agentOspfPacketStatsGroup=_AgentOspfPacketStatsGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,14))
_AgentOspfCountersCleared_Type=Unsigned32
_AgentOspfCountersCleared_Object=MibScalar
agentOspfCountersCleared=_AgentOspfCountersCleared_Object((1,3,6,1,4,1,2356,16,1,2,14,1),_AgentOspfCountersCleared_Type())
agentOspfCountersCleared.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfCountersCleared.setStatus(_A)
_AgentOspfLsaRetxCount_Type=Counter32
_AgentOspfLsaRetxCount_Object=MibScalar
agentOspfLsaRetxCount=_AgentOspfLsaRetxCount_Object((1,3,6,1,4,1,2356,16,1,2,14,2),_AgentOspfLsaRetxCount_Type())
agentOspfLsaRetxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLsaRetxCount.setStatus(_A)
_AgentOspfHellosRx_Type=Counter32
_AgentOspfHellosRx_Object=MibScalar
agentOspfHellosRx=_AgentOspfHellosRx_Object((1,3,6,1,4,1,2356,16,1,2,14,3),_AgentOspfHellosRx_Type())
agentOspfHellosRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfHellosRx.setStatus(_A)
_AgentOspfHellosTx_Type=Counter32
_AgentOspfHellosTx_Object=MibScalar
agentOspfHellosTx=_AgentOspfHellosTx_Object((1,3,6,1,4,1,2356,16,1,2,14,4),_AgentOspfHellosTx_Type())
agentOspfHellosTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfHellosTx.setStatus(_A)
_AgentOspfDdRx_Type=Counter32
_AgentOspfDdRx_Object=MibScalar
agentOspfDdRx=_AgentOspfDdRx_Object((1,3,6,1,4,1,2356,16,1,2,14,5),_AgentOspfDdRx_Type())
agentOspfDdRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDdRx.setStatus(_A)
_AgentOspfDdTx_Type=Counter32
_AgentOspfDdTx_Object=MibScalar
agentOspfDdTx=_AgentOspfDdTx_Object((1,3,6,1,4,1,2356,16,1,2,14,6),_AgentOspfDdTx_Type())
agentOspfDdTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfDdTx.setStatus(_A)
_AgentOspfLsReqRx_Type=Counter32
_AgentOspfLsReqRx_Object=MibScalar
agentOspfLsReqRx=_AgentOspfLsReqRx_Object((1,3,6,1,4,1,2356,16,1,2,14,7),_AgentOspfLsReqRx_Type())
agentOspfLsReqRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLsReqRx.setStatus(_A)
_AgentOspfLsReqTx_Type=Counter32
_AgentOspfLsReqTx_Object=MibScalar
agentOspfLsReqTx=_AgentOspfLsReqTx_Object((1,3,6,1,4,1,2356,16,1,2,14,8),_AgentOspfLsReqTx_Type())
agentOspfLsReqTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLsReqTx.setStatus(_A)
_AgentOspfLsUpdatesRx_Type=Counter32
_AgentOspfLsUpdatesRx_Object=MibScalar
agentOspfLsUpdatesRx=_AgentOspfLsUpdatesRx_Object((1,3,6,1,4,1,2356,16,1,2,14,9),_AgentOspfLsUpdatesRx_Type())
agentOspfLsUpdatesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLsUpdatesRx.setStatus(_A)
_AgentOspfLsUpdatesTx_Type=Counter32
_AgentOspfLsUpdatesTx_Object=MibScalar
agentOspfLsUpdatesTx=_AgentOspfLsUpdatesTx_Object((1,3,6,1,4,1,2356,16,1,2,14,10),_AgentOspfLsUpdatesTx_Type())
agentOspfLsUpdatesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLsUpdatesTx.setStatus(_A)
_AgentOspfLsAckRx_Type=Counter32
_AgentOspfLsAckRx_Object=MibScalar
agentOspfLsAckRx=_AgentOspfLsAckRx_Object((1,3,6,1,4,1,2356,16,1,2,14,11),_AgentOspfLsAckRx_Type())
agentOspfLsAckRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLsAckRx.setStatus(_A)
_AgentOspfLsAckTx_Type=Counter32
_AgentOspfLsAckTx_Object=MibScalar
agentOspfLsAckTx=_AgentOspfLsAckTx_Object((1,3,6,1,4,1,2356,16,1,2,14,12),_AgentOspfLsAckTx_Type())
agentOspfLsAckTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLsAckTx.setStatus(_A)
_AgentOspfLsUpdatesRxMax_Type=Gauge32
_AgentOspfLsUpdatesRxMax_Object=MibScalar
agentOspfLsUpdatesRxMax=_AgentOspfLsUpdatesRxMax_Object((1,3,6,1,4,1,2356,16,1,2,14,13),_AgentOspfLsUpdatesRxMax_Type())
agentOspfLsUpdatesRxMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLsUpdatesRxMax.setStatus(_A)
_AgentOspfLsUpdatesTxMax_Type=Gauge32
_AgentOspfLsUpdatesTxMax_Object=MibScalar
agentOspfLsUpdatesTxMax=_AgentOspfLsUpdatesTxMax_Object((1,3,6,1,4,1,2356,16,1,2,14,14),_AgentOspfLsUpdatesTxMax_Type())
agentOspfLsUpdatesTxMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfLsUpdatesTxMax.setStatus(_A)
_AgentOspfType1LsasRx_Type=Counter32
_AgentOspfType1LsasRx_Object=MibScalar
agentOspfType1LsasRx=_AgentOspfType1LsasRx_Object((1,3,6,1,4,1,2356,16,1,2,14,15),_AgentOspfType1LsasRx_Type())
agentOspfType1LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfType1LsasRx.setStatus(_A)
_AgentOspfType2LsasRx_Type=Counter32
_AgentOspfType2LsasRx_Object=MibScalar
agentOspfType2LsasRx=_AgentOspfType2LsasRx_Object((1,3,6,1,4,1,2356,16,1,2,14,16),_AgentOspfType2LsasRx_Type())
agentOspfType2LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfType2LsasRx.setStatus(_A)
_AgentOspfType3LsasRx_Type=Counter32
_AgentOspfType3LsasRx_Object=MibScalar
agentOspfType3LsasRx=_AgentOspfType3LsasRx_Object((1,3,6,1,4,1,2356,16,1,2,14,17),_AgentOspfType3LsasRx_Type())
agentOspfType3LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfType3LsasRx.setStatus(_A)
_AgentOspfType4LsasRx_Type=Counter32
_AgentOspfType4LsasRx_Object=MibScalar
agentOspfType4LsasRx=_AgentOspfType4LsasRx_Object((1,3,6,1,4,1,2356,16,1,2,14,18),_AgentOspfType4LsasRx_Type())
agentOspfType4LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfType4LsasRx.setStatus(_A)
_AgentOspfType5LsasRx_Type=Counter32
_AgentOspfType5LsasRx_Object=MibScalar
agentOspfType5LsasRx=_AgentOspfType5LsasRx_Object((1,3,6,1,4,1,2356,16,1,2,14,19),_AgentOspfType5LsasRx_Type())
agentOspfType5LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfType5LsasRx.setStatus(_A)
_AgentOspfType7LsasRx_Type=Counter32
_AgentOspfType7LsasRx_Object=MibScalar
agentOspfType7LsasRx=_AgentOspfType7LsasRx_Object((1,3,6,1,4,1,2356,16,1,2,14,20),_AgentOspfType7LsasRx_Type())
agentOspfType7LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfType7LsasRx.setStatus(_A)
_AgentOspfType9LsasRx_Type=Counter32
_AgentOspfType9LsasRx_Object=MibScalar
agentOspfType9LsasRx=_AgentOspfType9LsasRx_Object((1,3,6,1,4,1,2356,16,1,2,14,21),_AgentOspfType9LsasRx_Type())
agentOspfType9LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfType9LsasRx.setStatus(_A)
_AgentOspfType10LsasRx_Type=Counter32
_AgentOspfType10LsasRx_Object=MibScalar
agentOspfType10LsasRx=_AgentOspfType10LsasRx_Object((1,3,6,1,4,1,2356,16,1,2,14,22),_AgentOspfType10LsasRx_Type())
agentOspfType10LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfType10LsasRx.setStatus(_A)
_AgentOspfType11LsasRx_Type=Counter32
_AgentOspfType11LsasRx_Object=MibScalar
agentOspfType11LsasRx=_AgentOspfType11LsasRx_Object((1,3,6,1,4,1,2356,16,1,2,14,23),_AgentOspfType11LsasRx_Type())
agentOspfType11LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfType11LsasRx.setStatus(_A)
_AgentOspfSpfStatsTable_Object=MibTable
agentOspfSpfStatsTable=_AgentOspfSpfStatsTable_Object((1,3,6,1,4,1,2356,16,1,2,15))
if mibBuilder.loadTexts:agentOspfSpfStatsTable.setStatus(_A)
_AgentOspfSpfStatsEntry_Object=MibTableRow
agentOspfSpfStatsEntry=_AgentOspfSpfStatsEntry_Object((1,3,6,1,4,1,2356,16,1,2,15,1))
agentOspfSpfStatsEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:agentOspfSpfStatsEntry.setStatus(_A)
_AgentOspfSpfIndex_Type=Counter32
_AgentOspfSpfIndex_Object=MibTableColumn
agentOspfSpfIndex=_AgentOspfSpfIndex_Object((1,3,6,1,4,1,2356,16,1,2,15,1,1),_AgentOspfSpfIndex_Type())
agentOspfSpfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentOspfSpfIndex.setStatus(_A)
_AgentOspfSpfStatsDeltaT_Type=Unsigned32
_AgentOspfSpfStatsDeltaT_Object=MibTableColumn
agentOspfSpfStatsDeltaT=_AgentOspfSpfStatsDeltaT_Object((1,3,6,1,4,1,2356,16,1,2,15,1,2),_AgentOspfSpfStatsDeltaT_Type())
agentOspfSpfStatsDeltaT.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfSpfStatsDeltaT.setStatus(_A)
_AgentOspfSpfStatsIntra_Type=Gauge32
_AgentOspfSpfStatsIntra_Object=MibTableColumn
agentOspfSpfStatsIntra=_AgentOspfSpfStatsIntra_Object((1,3,6,1,4,1,2356,16,1,2,15,1,3),_AgentOspfSpfStatsIntra_Type())
agentOspfSpfStatsIntra.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfSpfStatsIntra.setStatus(_A)
_AgentOspfSpfStatsSumm_Type=Gauge32
_AgentOspfSpfStatsSumm_Object=MibTableColumn
agentOspfSpfStatsSumm=_AgentOspfSpfStatsSumm_Object((1,3,6,1,4,1,2356,16,1,2,15,1,4),_AgentOspfSpfStatsSumm_Type())
agentOspfSpfStatsSumm.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfSpfStatsSumm.setStatus(_A)
_AgentOspfSpfStatsExt_Type=Gauge32
_AgentOspfSpfStatsExt_Object=MibTableColumn
agentOspfSpfStatsExt=_AgentOspfSpfStatsExt_Object((1,3,6,1,4,1,2356,16,1,2,15,1,5),_AgentOspfSpfStatsExt_Type())
agentOspfSpfStatsExt.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfSpfStatsExt.setStatus(_A)
_AgentOspfSpfStatsSpfTotal_Type=Gauge32
_AgentOspfSpfStatsSpfTotal_Object=MibTableColumn
agentOspfSpfStatsSpfTotal=_AgentOspfSpfStatsSpfTotal_Object((1,3,6,1,4,1,2356,16,1,2,15,1,6),_AgentOspfSpfStatsSpfTotal_Type())
agentOspfSpfStatsSpfTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfSpfStatsSpfTotal.setStatus(_A)
_AgentOspfSpfStatsRibUpdate_Type=Gauge32
_AgentOspfSpfStatsRibUpdate_Object=MibTableColumn
agentOspfSpfStatsRibUpdate=_AgentOspfSpfStatsRibUpdate_Object((1,3,6,1,4,1,2356,16,1,2,15,1,7),_AgentOspfSpfStatsRibUpdate_Type())
agentOspfSpfStatsRibUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfSpfStatsRibUpdate.setStatus(_A)
_AgentOspfSpfStatsReason_Type=DisplayString
_AgentOspfSpfStatsReason_Object=MibTableColumn
agentOspfSpfStatsReason=_AgentOspfSpfStatsReason_Object((1,3,6,1,4,1,2356,16,1,2,15,1,8),_AgentOspfSpfStatsReason_Type())
agentOspfSpfStatsReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfSpfStatsReason.setStatus(_A)
_AgentRoutingHeapGroup_ObjectIdentity=ObjectIdentity
agentRoutingHeapGroup=_AgentRoutingHeapGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,16))
_AgentRoutingHeapSize_Type=Unsigned32
_AgentRoutingHeapSize_Object=MibScalar
agentRoutingHeapSize=_AgentRoutingHeapSize_Object((1,3,6,1,4,1,2356,16,1,2,16,1),_AgentRoutingHeapSize_Type())
agentRoutingHeapSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRoutingHeapSize.setStatus(_A)
_AgentRoutingHeapInUse_Type=Gauge32
_AgentRoutingHeapInUse_Object=MibScalar
agentRoutingHeapInUse=_AgentRoutingHeapInUse_Object((1,3,6,1,4,1,2356,16,1,2,16,2),_AgentRoutingHeapInUse_Type())
agentRoutingHeapInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRoutingHeapInUse.setStatus(_A)
_AgentRoutingHeapHigh_Type=Gauge32
_AgentRoutingHeapHigh_Object=MibScalar
agentRoutingHeapHigh=_AgentRoutingHeapHigh_Object((1,3,6,1,4,1,2356,16,1,2,16,3),_AgentRoutingHeapHigh_Type())
agentRoutingHeapHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRoutingHeapHigh.setStatus(_A)
_AgentRoutingTableSummaryGroup_ObjectIdentity=ObjectIdentity
agentRoutingTableSummaryGroup=_AgentRoutingTableSummaryGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,17))
_AgentConnectedRoutes_Type=Gauge32
_AgentConnectedRoutes_Object=MibScalar
agentConnectedRoutes=_AgentConnectedRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,1),_AgentConnectedRoutes_Type())
agentConnectedRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentConnectedRoutes.setStatus(_A)
_AgentStaticRoutes_Type=Gauge32
_AgentStaticRoutes_Object=MibScalar
agentStaticRoutes=_AgentStaticRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,2),_AgentStaticRoutes_Type())
agentStaticRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStaticRoutes.setStatus(_A)
_AgentRipRoutes_Type=Gauge32
_AgentRipRoutes_Object=MibScalar
agentRipRoutes=_AgentRipRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,3),_AgentRipRoutes_Type())
agentRipRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRoutes.setStatus(_A)
_AgentOspfRoutes_Type=Gauge32
_AgentOspfRoutes_Object=MibScalar
agentOspfRoutes=_AgentOspfRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,4),_AgentOspfRoutes_Type())
agentOspfRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRoutes.setStatus(_A)
_AgentOspfIntraRoutes_Type=Gauge32
_AgentOspfIntraRoutes_Object=MibScalar
agentOspfIntraRoutes=_AgentOspfIntraRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,5),_AgentOspfIntraRoutes_Type())
agentOspfIntraRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfIntraRoutes.setStatus(_A)
_AgentOspfInterRoutes_Type=Gauge32
_AgentOspfInterRoutes_Object=MibScalar
agentOspfInterRoutes=_AgentOspfInterRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,6),_AgentOspfInterRoutes_Type())
agentOspfInterRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfInterRoutes.setStatus(_A)
_AgentOspfExt1Routes_Type=Gauge32
_AgentOspfExt1Routes_Object=MibScalar
agentOspfExt1Routes=_AgentOspfExt1Routes_Object((1,3,6,1,4,1,2356,16,1,2,17,7),_AgentOspfExt1Routes_Type())
agentOspfExt1Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfExt1Routes.setStatus(_A)
_AgentOspfExt2Routes_Type=Gauge32
_AgentOspfExt2Routes_Object=MibScalar
agentOspfExt2Routes=_AgentOspfExt2Routes_Object((1,3,6,1,4,1,2356,16,1,2,17,8),_AgentOspfExt2Routes_Type())
agentOspfExt2Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfExt2Routes.setStatus(_A)
_AgentBgpRoutes_Type=Gauge32
_AgentBgpRoutes_Object=MibScalar
agentBgpRoutes=_AgentBgpRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,9),_AgentBgpRoutes_Type())
agentBgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBgpRoutes.setStatus(_A)
_AgentEbgpRoutes_Type=Gauge32
_AgentEbgpRoutes_Object=MibScalar
agentEbgpRoutes=_AgentEbgpRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,10),_AgentEbgpRoutes_Type())
agentEbgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEbgpRoutes.setStatus(_A)
_AgentIbgpRoutes_Type=Gauge32
_AgentIbgpRoutes_Object=MibScalar
agentIbgpRoutes=_AgentIbgpRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,11),_AgentIbgpRoutes_Type())
agentIbgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIbgpRoutes.setStatus(_A)
_AgentLocalBgpRoutes_Type=Gauge32
_AgentLocalBgpRoutes_Object=MibScalar
agentLocalBgpRoutes=_AgentLocalBgpRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,12),_AgentLocalBgpRoutes_Type())
agentLocalBgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLocalBgpRoutes.setStatus(_A)
_AgentRejectRoutes_Type=Gauge32
_AgentRejectRoutes_Object=MibScalar
agentRejectRoutes=_AgentRejectRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,13),_AgentRejectRoutes_Type())
agentRejectRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRejectRoutes.setStatus(_A)
_AgentTotalRoutes_Type=Gauge32
_AgentTotalRoutes_Object=MibScalar
agentTotalRoutes=_AgentTotalRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,14),_AgentTotalRoutes_Type())
agentTotalRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTotalRoutes.setStatus(_A)
_AgentBestRoutes_Type=Gauge32
_AgentBestRoutes_Object=MibScalar
agentBestRoutes=_AgentBestRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,15),_AgentBestRoutes_Type())
agentBestRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBestRoutes.setStatus(_A)
_AgentBestRoutesHigh_Type=Gauge32
_AgentBestRoutesHigh_Object=MibScalar
agentBestRoutesHigh=_AgentBestRoutesHigh_Object((1,3,6,1,4,1,2356,16,1,2,17,16),_AgentBestRoutesHigh_Type())
agentBestRoutesHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBestRoutesHigh.setStatus(_A)
_AgentAlternateRoutes_Type=Gauge32
_AgentAlternateRoutes_Object=MibScalar
agentAlternateRoutes=_AgentAlternateRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,17),_AgentAlternateRoutes_Type())
agentAlternateRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAlternateRoutes.setStatus(_A)
_AgentRouteAdds_Type=Counter32
_AgentRouteAdds_Object=MibScalar
agentRouteAdds=_AgentRouteAdds_Object((1,3,6,1,4,1,2356,16,1,2,17,18),_AgentRouteAdds_Type())
agentRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouteAdds.setStatus(_A)
_AgentRouteModifies_Type=Counter32
_AgentRouteModifies_Object=MibScalar
agentRouteModifies=_AgentRouteModifies_Object((1,3,6,1,4,1,2356,16,1,2,17,19),_AgentRouteModifies_Type())
agentRouteModifies.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouteModifies.setStatus(_A)
_AgentRouteDeletes_Type=Counter32
_AgentRouteDeletes_Object=MibScalar
agentRouteDeletes=_AgentRouteDeletes_Object((1,3,6,1,4,1,2356,16,1,2,17,20),_AgentRouteDeletes_Type())
agentRouteDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouteDeletes.setStatus(_A)
_AgentUnresolvedRouteAdds_Type=Counter32
_AgentUnresolvedRouteAdds_Object=MibScalar
agentUnresolvedRouteAdds=_AgentUnresolvedRouteAdds_Object((1,3,6,1,4,1,2356,16,1,2,17,21),_AgentUnresolvedRouteAdds_Type())
agentUnresolvedRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUnresolvedRouteAdds.setStatus(_A)
_AgentInvalidRouteAdds_Type=Counter32
_AgentInvalidRouteAdds_Object=MibScalar
agentInvalidRouteAdds=_AgentInvalidRouteAdds_Object((1,3,6,1,4,1,2356,16,1,2,17,22),_AgentInvalidRouteAdds_Type())
agentInvalidRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentInvalidRouteAdds.setStatus(_A)
_AgentFailedRouteAdds_Type=Counter32
_AgentFailedRouteAdds_Object=MibScalar
agentFailedRouteAdds=_AgentFailedRouteAdds_Object((1,3,6,1,4,1,2356,16,1,2,17,23),_AgentFailedRouteAdds_Type())
agentFailedRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentFailedRouteAdds.setStatus(_A)
_AgentReservedLocals_Type=Gauge32
_AgentReservedLocals_Object=MibScalar
agentReservedLocals=_AgentReservedLocals_Object((1,3,6,1,4,1,2356,16,1,2,17,24),_AgentReservedLocals_Type())
agentReservedLocals.setMaxAccess(_B)
if mibBuilder.loadTexts:agentReservedLocals.setStatus(_A)
_AgentUniqueNextHops_Type=Gauge32
_AgentUniqueNextHops_Object=MibScalar
agentUniqueNextHops=_AgentUniqueNextHops_Object((1,3,6,1,4,1,2356,16,1,2,17,25),_AgentUniqueNextHops_Type())
agentUniqueNextHops.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUniqueNextHops.setStatus(_A)
_AgentUniqueNextHopsHigh_Type=Gauge32
_AgentUniqueNextHopsHigh_Object=MibScalar
agentUniqueNextHopsHigh=_AgentUniqueNextHopsHigh_Object((1,3,6,1,4,1,2356,16,1,2,17,26),_AgentUniqueNextHopsHigh_Type())
agentUniqueNextHopsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUniqueNextHopsHigh.setStatus(_A)
_AgentNextHopGroups_Type=Gauge32
_AgentNextHopGroups_Object=MibScalar
agentNextHopGroups=_AgentNextHopGroups_Object((1,3,6,1,4,1,2356,16,1,2,17,27),_AgentNextHopGroups_Type())
agentNextHopGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNextHopGroups.setStatus(_A)
_AgentNextHopGroupsHigh_Type=Gauge32
_AgentNextHopGroupsHigh_Object=MibScalar
agentNextHopGroupsHigh=_AgentNextHopGroupsHigh_Object((1,3,6,1,4,1,2356,16,1,2,17,28),_AgentNextHopGroupsHigh_Type())
agentNextHopGroupsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNextHopGroupsHigh.setStatus(_A)
_AgentEcmpGroups_Type=Gauge32
_AgentEcmpGroups_Object=MibScalar
agentEcmpGroups=_AgentEcmpGroups_Object((1,3,6,1,4,1,2356,16,1,2,17,29),_AgentEcmpGroups_Type())
agentEcmpGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpGroups.setStatus(_A)
_AgentEcmpGroupsHigh_Type=Gauge32
_AgentEcmpGroupsHigh_Object=MibScalar
agentEcmpGroupsHigh=_AgentEcmpGroupsHigh_Object((1,3,6,1,4,1,2356,16,1,2,17,30),_AgentEcmpGroupsHigh_Type())
agentEcmpGroupsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpGroupsHigh.setStatus(_A)
_AgentEcmpRoutes_Type=Gauge32
_AgentEcmpRoutes_Object=MibScalar
agentEcmpRoutes=_AgentEcmpRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,31),_AgentEcmpRoutes_Type())
agentEcmpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpRoutes.setStatus(_A)
_AgentTruncEcmpRoutes_Type=Gauge32
_AgentTruncEcmpRoutes_Object=MibScalar
agentTruncEcmpRoutes=_AgentTruncEcmpRoutes_Object((1,3,6,1,4,1,2356,16,1,2,17,32),_AgentTruncEcmpRoutes_Type())
agentTruncEcmpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTruncEcmpRoutes.setStatus(_A)
_AgentEcmpRetries_Type=Counter32
_AgentEcmpRetries_Object=MibScalar
agentEcmpRetries=_AgentEcmpRetries_Object((1,3,6,1,4,1,2356,16,1,2,17,33),_AgentEcmpRetries_Type())
agentEcmpRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpRetries.setStatus(_A)
_AgentEcmpCountTable_Object=MibTable
agentEcmpCountTable=_AgentEcmpCountTable_Object((1,3,6,1,4,1,2356,16,1,2,18))
if mibBuilder.loadTexts:agentEcmpCountTable.setStatus(_A)
_AgentEcmpCountEntry_Object=MibTableRow
agentEcmpCountEntry=_AgentEcmpCountEntry_Object((1,3,6,1,4,1,2356,16,1,2,18,1))
agentEcmpCountEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:agentEcmpCountEntry.setStatus(_A)
class _AgentEcmpNextHopCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentEcmpNextHopCount_Type.__name__=_K
_AgentEcmpNextHopCount_Object=MibTableColumn
agentEcmpNextHopCount=_AgentEcmpNextHopCount_Object((1,3,6,1,4,1,2356,16,1,2,18,1,1),_AgentEcmpNextHopCount_Type())
agentEcmpNextHopCount.setMaxAccess(_J)
if mibBuilder.loadTexts:agentEcmpNextHopCount.setStatus(_A)
_AgentEcmpRouteCount_Type=Gauge32
_AgentEcmpRouteCount_Object=MibTableColumn
agentEcmpRouteCount=_AgentEcmpRouteCount_Object((1,3,6,1,4,1,2356,16,1,2,18,1,2),_AgentEcmpRouteCount_Type())
agentEcmpRouteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpRouteCount.setStatus(_A)
_AgentOspfStubRouterGroup_ObjectIdentity=ObjectIdentity
agentOspfStubRouterGroup=_AgentOspfStubRouterGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,19))
class _OspfStubRouterAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doNotAdvertise',1),('advertise',2)))
_OspfStubRouterAdvertisement_Type.__name__=_D
_OspfStubRouterAdvertisement_Object=MibScalar
ospfStubRouterAdvertisement=_OspfStubRouterAdvertisement_Object((1,3,6,1,4,1,2356,16,1,2,19,1),_OspfStubRouterAdvertisement_Type())
ospfStubRouterAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfStubRouterAdvertisement.setStatus(_A)
class _AgentOspfStubRouterReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('configured',0),('startup',1),('resource-limitation',2)))
_AgentOspfStubRouterReason_Type.__name__=_D
_AgentOspfStubRouterReason_Object=MibScalar
agentOspfStubRouterReason=_AgentOspfStubRouterReason_Object((1,3,6,1,4,1,2356,16,1,2,19,2),_AgentOspfStubRouterReason_Type())
agentOspfStubRouterReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfStubRouterReason.setStatus(_A)
_AgentOspfStubRouterStartupTimeRemaining_Type=Unsigned32
_AgentOspfStubRouterStartupTimeRemaining_Object=MibScalar
agentOspfStubRouterStartupTimeRemaining=_AgentOspfStubRouterStartupTimeRemaining_Object((1,3,6,1,4,1,2356,16,1,2,19,3),_AgentOspfStubRouterStartupTimeRemaining_Type())
agentOspfStubRouterStartupTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfStubRouterStartupTimeRemaining.setStatus(_A)
_AgentOspfStubRouterDuration_Type=Unsigned32
_AgentOspfStubRouterDuration_Object=MibScalar
agentOspfStubRouterDuration=_AgentOspfStubRouterDuration_Object((1,3,6,1,4,1,2356,16,1,2,19,4),_AgentOspfStubRouterDuration_Type())
agentOspfStubRouterDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfStubRouterDuration.setStatus(_A)
_AgentRoutesConfigGroup_ObjectIdentity=ObjectIdentity
agentRoutesConfigGroup=_AgentRoutesConfigGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,2,150))
_AgentStaticRoutesTable_Object=MibTable
agentStaticRoutesTable=_AgentStaticRoutesTable_Object((1,3,6,1,4,1,2356,16,1,2,150,1))
if mibBuilder.loadTexts:agentStaticRoutesTable.setStatus(_A)
_AgentStaticRoutesTableEntry_Object=MibTableRow
agentStaticRoutesTableEntry=_AgentStaticRoutesTableEntry_Object((1,3,6,1,4,1,2356,16,1,2,150,1,1))
agentStaticRoutesTableEntry.setIndexNames((0,_E,_AD),(0,_E,_AE),(0,_E,_AF),(0,_E,_AG),(0,_E,_AH))
if mibBuilder.loadTexts:agentStaticRoutesTableEntry.setStatus(_A)
_AgentStaticRoutesNetworkAddress_Type=IpAddress
_AgentStaticRoutesNetworkAddress_Object=MibTableColumn
agentStaticRoutesNetworkAddress=_AgentStaticRoutesNetworkAddress_Object((1,3,6,1,4,1,2356,16,1,2,150,1,1,1),_AgentStaticRoutesNetworkAddress_Type())
agentStaticRoutesNetworkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStaticRoutesNetworkAddress.setStatus(_A)
_AgentStaticRoutesNetMask_Type=IpAddress
_AgentStaticRoutesNetMask_Object=MibTableColumn
agentStaticRoutesNetMask=_AgentStaticRoutesNetMask_Object((1,3,6,1,4,1,2356,16,1,2,150,1,1,2),_AgentStaticRoutesNetMask_Type())
agentStaticRoutesNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:agentStaticRoutesNetMask.setStatus(_A)
_AgentStaticRoutesNextHop_Type=IpAddress
_AgentStaticRoutesNextHop_Object=MibTableColumn
agentStaticRoutesNextHop=_AgentStaticRoutesNextHop_Object((1,3,6,1,4,1,2356,16,1,2,150,1,1,3),_AgentStaticRoutesNextHop_Type())
agentStaticRoutesNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:agentStaticRoutesNextHop.setStatus(_A)
class _AgentStaticRoutesType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),(_Q,2),('reject',3)))
_AgentStaticRoutesType_Type.__name__=_D
_AgentStaticRoutesType_Object=MibTableColumn
agentStaticRoutesType=_AgentStaticRoutesType_Object((1,3,6,1,4,1,2356,16,1,2,150,1,1,4),_AgentStaticRoutesType_Type())
agentStaticRoutesType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStaticRoutesType.setStatus(_A)
_AgentStaticRoutesPreference_Type=Integer32
_AgentStaticRoutesPreference_Object=MibTableColumn
agentStaticRoutesPreference=_AgentStaticRoutesPreference_Object((1,3,6,1,4,1,2356,16,1,2,150,1,1,5),_AgentStaticRoutesPreference_Type())
agentStaticRoutesPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:agentStaticRoutesPreference.setStatus(_A)
_AgentStaticRoutesStatus_Type=RowStatus
_AgentStaticRoutesStatus_Object=MibTableColumn
agentStaticRoutesStatus=_AgentStaticRoutesStatus_Object((1,3,6,1,4,1,2356,16,1,2,150,1,1,6),_AgentStaticRoutesStatus_Type())
agentStaticRoutesStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentStaticRoutesStatus.setStatus(_A)
rip2IfConfEntry.registerAugmentions((_E,_AI))
agentRip2IfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())
ospfIfEntry.registerAugmentions((_E,_AJ))
agentOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions((_E,_AK))
agentOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{_X:SpfTimerRange,_r:AutoCostRefBw,'fastPathRouting':fastPathRouting,'agentSwitchArpGroup':agentSwitchArpGroup,'agentSwitchArpAgeoutTime':agentSwitchArpAgeoutTime,'agentSwitchArpResponseTime':agentSwitchArpResponseTime,'agentSwitchArpMaxRetries':agentSwitchArpMaxRetries,'agentSwitchArpCacheSize':agentSwitchArpCacheSize,'agentSwitchArpDynamicRenew':agentSwitchArpDynamicRenew,'agentSwitchArpTotalEntryCountCurrent':agentSwitchArpTotalEntryCountCurrent,'agentSwitchArpTotalEntryCountPeak':agentSwitchArpTotalEntryCountPeak,'agentSwitchArpStaticEntryCountCurrent':agentSwitchArpStaticEntryCountCurrent,'agentSwitchArpStaticEntryCountMax':agentSwitchArpStaticEntryCountMax,'agentSwitchArpTable':agentSwitchArpTable,'agentSwitchArpEntry':agentSwitchArpEntry,'agentSwitchArpAge':agentSwitchArpAge,_b:agentSwitchArpIpAddress,'agentSwitchArpMacAddress':agentSwitchArpMacAddress,'agentSwitchArpInterface':agentSwitchArpInterface,'agentSwitchArpType':agentSwitchArpType,'agentSwitchArpStatus':agentSwitchArpStatus,'agentSwitchLocalProxyArpTable':agentSwitchLocalProxyArpTable,'agentSwitchLocalProxyArpEntry':agentSwitchLocalProxyArpEntry,'agentSwitchLocalProxyArpMode':agentSwitchLocalProxyArpMode,'agentSwitchIntfArpTable':agentSwitchIntfArpTable,'agentSwitchIntfArpEntry':agentSwitchIntfArpEntry,_e:agentSwitchIntfArpIpAddress,_f:agentSwitchIntfArpIfIndex,'agentSwitchIntfArpAge':agentSwitchIntfArpAge,'agentSwitchIntfArpMacAddress':agentSwitchIntfArpMacAddress,'agentSwitchIntfArpType':agentSwitchIntfArpType,'agentSwitchIntfArpStatus':agentSwitchIntfArpStatus,'agentSwitchIpGroup':agentSwitchIpGroup,'agentSwitchIpRoutingMode':agentSwitchIpRoutingMode,'agentSwitchIpDefaultGateway':agentSwitchIpDefaultGateway,'agentSwitchIpInterfaceTable':agentSwitchIpInterfaceTable,'agentSwitchIpInterfaceEntry':agentSwitchIpInterfaceEntry,_R:agentSwitchIpInterfaceIfIndex,'agentSwitchIPAddressConfigMethod':agentSwitchIPAddressConfigMethod,'agentSwitchIpInterfaceIpAddress':agentSwitchIpInterfaceIpAddress,'agentSwitchIpInterfaceNetMask':agentSwitchIpInterfaceNetMask,'agentSwitchIpInterfaceClearIp':agentSwitchIpInterfaceClearIp,'agentSwitchIpInterfaceRoutingMode':agentSwitchIpInterfaceRoutingMode,'agentSwitchIpInterfaceProxyARPMode':agentSwitchIpInterfaceProxyARPMode,'agentSwitchIpInterfaceMtuValue':agentSwitchIpInterfaceMtuValue,'agentSwitchIpInterfaceBandwidth':agentSwitchIpInterfaceBandwidth,'agentSwitchIpInterfaceUnnumberedIfIndex':agentSwitchIpInterfaceUnnumberedIfIndex,'agentSwitchIpInterfaceIcmpUnreachables':agentSwitchIpInterfaceIcmpUnreachables,'agentSwitchIpInterfaceIcmpRedirects':agentSwitchIpInterfaceIcmpRedirects,'agentSwitchDhcpOperation':agentSwitchDhcpOperation,'agentSwitchIpInterfaceSuppressed':agentSwitchIpInterfaceSuppressed,'agentSwitchIpInterfaceNumberOfFlaps':agentSwitchIpInterfaceNumberOfFlaps,'agentSwitchIpInterfaceCurrentPenalty':agentSwitchIpInterfaceCurrentPenalty,'agentSwitchIpInterfaceReUseTime':agentSwitchIpInterfaceReUseTime,'agentSwitchIpInterfaceAutoStateMode':agentSwitchIpInterfaceAutoStateMode,'agentSwitchIpInterfaceFptiName':agentSwitchIpInterfaceFptiName,'agentSwitchIpRouterDiscoveryTable':agentSwitchIpRouterDiscoveryTable,'agentSwitchIpRouterDiscoveryEntry':agentSwitchIpRouterDiscoveryEntry,_g:agentSwitchIpRouterDiscoveryIfIndex,'agentSwitchIpRouterDiscoveryAdvertiseMode':agentSwitchIpRouterDiscoveryAdvertiseMode,'agentSwitchIpRouterDiscoveryMaxAdvertisementInterval':agentSwitchIpRouterDiscoveryMaxAdvertisementInterval,'agentSwitchIpRouterDiscoveryMinAdvertisementInterval':agentSwitchIpRouterDiscoveryMinAdvertisementInterval,'agentSwitchIpRouterDiscoveryAdvertisementLifetime':agentSwitchIpRouterDiscoveryAdvertisementLifetime,'agentSwitchIpRouterDiscoveryPreferenceLevel':agentSwitchIpRouterDiscoveryPreferenceLevel,'agentSwitchIpRouterDiscoveryAdvertisementAddress':agentSwitchIpRouterDiscoveryAdvertisementAddress,'agentSwitchIpVlanTable':agentSwitchIpVlanTable,'agentSwitchIpVlanEntry':agentSwitchIpVlanEntry,_h:agentSwitchIpVlanId,'agentSwitchIpVlanIfIndex':agentSwitchIpVlanIfIndex,'agentSwitchIpVlanRoutingStatus':agentSwitchIpVlanRoutingStatus,'agentSwitchSecondaryAddressTable':agentSwitchSecondaryAddressTable,'agentSwitchSecondaryAddressEntry':agentSwitchSecondaryAddressEntry,_i:agentSwitchSecondaryIpAddress,'agentSwitchSecondaryNetMask':agentSwitchSecondaryNetMask,'agentSwitchSecondaryStatus':agentSwitchSecondaryStatus,'agentSwitchHelperAddressTable':agentSwitchHelperAddressTable,'agentSwitchHelperAddressEntry':agentSwitchHelperAddressEntry,_j:agentSwitchHelperIpAddress,'agentSwitchHelperStatus':agentSwitchHelperStatus,'agentSwitchIpIcmpControlGroup':agentSwitchIpIcmpControlGroup,'agentSwitchIpIcmpEchoReplyMode':agentSwitchIpIcmpEchoReplyMode,'agentSwitchIpIcmpRedirectsMode':agentSwitchIpIcmpRedirectsMode,'agentSwitchIpIcmpRateLimitInterval':agentSwitchIpIcmpRateLimitInterval,'agentSwitchIpIcmpRateLimitBurstSize':agentSwitchIpIcmpRateLimitBurstSize,'agentSwitchIntfIpHelperAddressTable':agentSwitchIntfIpHelperAddressTable,'agentSwitchIntfIpHelperAddressEntry':agentSwitchIntfIpHelperAddressEntry,_l:agentSwitchIntfIpHelperIpAddress,_k:agentSwitchIntfIpHelperUdpPort,'agentSwitchIntfIpHelperDiscard':agentSwitchIntfIpHelperDiscard,'agentSwitchIntfIpHelperHitCount':agentSwitchIntfIpHelperHitCount,'agentSwitchIntfIpHelperStatus':agentSwitchIntfIpHelperStatus,'agentSwitchClearIpDefaultGateway':agentSwitchClearIpDefaultGateway,'agentRouterRipConfigGroup':agentRouterRipConfigGroup,'agentRouterRipAdminState':agentRouterRipAdminState,'agentRouterRipSplitHorizonMode':agentRouterRipSplitHorizonMode,'agentRouterRipAutoSummaryMode':agentRouterRipAutoSummaryMode,'agentRouterRipHostRoutesAcceptMode':agentRouterRipHostRoutesAcceptMode,'agentRouterRipDefaultMetric':agentRouterRipDefaultMetric,'agentRouterRipDefaultMetricConfigured':agentRouterRipDefaultMetricConfigured,'agentRouterRipDefaultInfoOriginate':agentRouterRipDefaultInfoOriginate,'agentRipRouteRedistTable':agentRipRouteRedistTable,'agentRipRouteRedistEntry':agentRipRouteRedistEntry,_m:agentRipRouteRedistSource,'agentRipRouteRedistMode':agentRipRouteRedistMode,'agentRipRouteRedistMetric':agentRipRouteRedistMetric,'agentRipRouteRedistMetricConfigured':agentRipRouteRedistMetricConfigured,'agentRipRouteRedistMatchInternal':agentRipRouteRedistMatchInternal,'agentRipRouteRedistMatchExternal1':agentRipRouteRedistMatchExternal1,'agentRipRouteRedistMatchExternal2':agentRipRouteRedistMatchExternal2,'agentRipRouteRedistMatchNSSAExternal1':agentRipRouteRedistMatchNSSAExternal1,'agentRipRouteRedistMatchNSSAExternal2':agentRipRouteRedistMatchNSSAExternal2,'agentRipRouteRedistDistList':agentRipRouteRedistDistList,'agentRipRouteRedistDistListConfigured':agentRipRouteRedistDistListConfigured,'agentRip2IfConfTable':agentRip2IfConfTable,_AI:agentRip2IfConfEntry,'agentRip2IfConfAuthKeyId':agentRip2IfConfAuthKeyId,'agentRouterRipRoutePref':agentRouterRipRoutePref,'agentRouterOspfConfigGroup':agentRouterOspfConfigGroup,'agentOspfDefaultMetric':agentOspfDefaultMetric,'agentOspfDefaultMetricConfigured':agentOspfDefaultMetricConfigured,'agentOspfDefaultInfoOriginate':agentOspfDefaultInfoOriginate,'agentOspfDefaultInfoOriginateAlways':agentOspfDefaultInfoOriginateAlways,'agentOspfDefaultInfoOriginateMetric':agentOspfDefaultInfoOriginateMetric,'agentOspfDefaultInfoOriginateMetricConfigured':agentOspfDefaultInfoOriginateMetricConfigured,'agentOspfDefaultInfoOriginateMetricType':agentOspfDefaultInfoOriginateMetricType,'agentOspfRouteRedistTable':agentOspfRouteRedistTable,'agentOspfRouteRedistEntry':agentOspfRouteRedistEntry,_q:agentOspfRouteRedistSource,'agentOspfRouteRedistMode':agentOspfRouteRedistMode,'agentOspfRouteRedistMetric':agentOspfRouteRedistMetric,'agentOspfRouteRedistMetricConfigured':agentOspfRouteRedistMetricConfigured,'agentOspfRouteRedistMetricType':agentOspfRouteRedistMetricType,'agentOspfRouteRedistTag':agentOspfRouteRedistTag,'agentOspfRouteRedistSubnets':agentOspfRouteRedistSubnets,'agentOspfRouteRedistDistList':agentOspfRouteRedistDistList,'agentOspfRouteRedistDistListConfigured':agentOspfRouteRedistDistListConfigured,'agentOspfIfTable':agentOspfIfTable,_AJ:agentOspfIfEntry,'agentOspfIfAuthKeyId':agentOspfIfAuthKeyId,'agentOspfIfIpMtuIgnoreFlag':agentOspfIfIpMtuIgnoreFlag,'agentOspfIfPassiveMode':agentOspfIfPassiveMode,'agentOspfIfAdvertiseSecondaries':agentOspfIfAdvertiseSecondaries,'agentOspfVirtIfTable':agentOspfVirtIfTable,_AK:agentOspfVirtIfEntry,'agentOspfVirtIfAuthKeyId':agentOspfVirtIfAuthKeyId,'agentRouterOspfRFC1583CompatibilityMode':agentRouterOspfRFC1583CompatibilityMode,'agentOspfSpfDelayTime':agentOspfSpfDelayTime,'agentOspfSpfHoldTime':agentOspfSpfHoldTime,'agentOspfAutoCostRefBw':agentOspfAutoCostRefBw,'agentOspfOpaqueLsaSupport':agentOspfOpaqueLsaSupport,'agentOspfAreaOpaqueLsdbTable':agentOspfAreaOpaqueLsdbTable,'agentOspfAreaOpaqueLsdbEntry':agentOspfAreaOpaqueLsdbEntry,_s:agentOspfAreaOpaqueLsdbAreaId,_t:agentOspfAreaOpaqueLsdbType,_u:agentOspfAreaOpaqueLsdbLsid,_v:agentOspfAreaOpaqueLsdbRouterId,'agentOspfAreaOpaqueLsdbSequence':agentOspfAreaOpaqueLsdbSequence,'agentOspfAreaOpaqueLsdbAge':agentOspfAreaOpaqueLsdbAge,'agentOspfAreaOpaqueLsdbChecksum':agentOspfAreaOpaqueLsdbChecksum,'agentOspfAreaOpaqueLsdbAdvertisement':agentOspfAreaOpaqueLsdbAdvertisement,'agentOspfLocalLsdbTable':agentOspfLocalLsdbTable,'agentOspfLocalLsdbEntry':agentOspfLocalLsdbEntry,_w:agentOspfLocalLsdbIpAddress,_x:agentOspfLocalLsdbAddressLessIf,_y:agentOspfLocalLsdbType,_z:agentOspfLocalLsdbLsid,_A0:agentOspfLocalLsdbRouterId,'agentOspfLocalLsdbSequence':agentOspfLocalLsdbSequence,'agentOspfLocalLsdbAge':agentOspfLocalLsdbAge,'agentOspfLocalLsdbChecksum':agentOspfLocalLsdbChecksum,'agentOspfLocalLsdbAdvertisement':agentOspfLocalLsdbAdvertisement,'agentOspfAsLsdbTable':agentOspfAsLsdbTable,'agentOspfAsLsdbEntry':agentOspfAsLsdbEntry,_A1:agentOspfAsLsdbType,_A2:agentOspfAsLsdbLsid,_A3:agentOspfAsLsdbRouterId,'agentOspfAsLsdbSequence':agentOspfAsLsdbSequence,'agentOspfAsLsdbAge':agentOspfAsLsdbAge,'agentOspfAsLsdbChecksum':agentOspfAsLsdbChecksum,'agentOspfAsLsdbAdvertisement':agentOspfAsLsdbAdvertisement,'agentOspfDefaultPassiveMode':agentOspfDefaultPassiveMode,'agentOspfRoutePrefIntraArea':agentOspfRoutePrefIntraArea,'agentOspfRoutePrefInterArea':agentOspfRoutePrefInterArea,'agentOspfRoutePrefExternal':agentOspfRoutePrefExternal,'agentSnmpTrapFlagsConfigGroupLayer3':agentSnmpTrapFlagsConfigGroupLayer3,'agentSnmpVRRPNewMasterTrapFlag':agentSnmpVRRPNewMasterTrapFlag,'agentSnmpVRRPAuthFailureTrapFlag':agentSnmpVRRPAuthFailureTrapFlag,'agentBootpDhcpRelayGroup':agentBootpDhcpRelayGroup,'agentBootpDhcpRelayMaxHopCount':agentBootpDhcpRelayMaxHopCount,'agentBootpDhcpRelayForwardingIp':agentBootpDhcpRelayForwardingIp,'agentBootpDhcpRelayForwardMode':agentBootpDhcpRelayForwardMode,'agentBootpDhcpRelayMinWaitTime':agentBootpDhcpRelayMinWaitTime,'agentBootpDhcpRelayCircuitIdOptionMode':agentBootpDhcpRelayCircuitIdOptionMode,'agentBootpDhcpRelayNumOfRequestsReceived':agentBootpDhcpRelayNumOfRequestsReceived,'agentBootpDhcpRelayNumOfRequestsForwarded':agentBootpDhcpRelayNumOfRequestsForwarded,'agentBootpDhcpRelayNumOfDiscards':agentBootpDhcpRelayNumOfDiscards,'agentECMPGroup':agentECMPGroup,'agentECMPOspfMaxPaths':agentECMPOspfMaxPaths,'agentRouterVrrpConfigGroup':agentRouterVrrpConfigGroup,'agentRouterVrrpAdminState':agentRouterVrrpAdminState,'agentRouterVrrpConfiguredTable':agentRouterVrrpConfiguredTable,'agentRouterVrrpConfiguredEntry':agentRouterVrrpConfiguredEntry,'agentRouterVrrpConfiguredPriority':agentRouterVrrpConfiguredPriority,'agentVrrpOperations':agentVrrpOperations,'agentRouterVrrpOperTable':agentRouterVrrpOperTable,'agentRouterVrrpOperEntry':agentRouterVrrpOperEntry,'agentRouterVrrpOperPriority':agentRouterVrrpOperPriority,'agentRouterVrrpTrackGroup':agentRouterVrrpTrackGroup,'agentRouterVrrpTrackIntfTable':agentRouterVrrpTrackIntfTable,'agentRouterVrrpTrackIntfEntry':agentRouterVrrpTrackIntfEntry,_A4:agentRouterVrrpTrackIntf,'agentRouterVrrpTrackIfPrioDec':agentRouterVrrpTrackIfPrioDec,'agentRouterVrrpTrackIfState':agentRouterVrrpTrackIfState,'agentRouterVrrpTrackIfStatus':agentRouterVrrpTrackIfStatus,'agentRouterVrrpTrackRouteTable':agentRouterVrrpTrackRouteTable,'agentRouterVrrpTrackRouteEntry':agentRouterVrrpTrackRouteEntry,_A5:agentRouterVrrpTrackRtPfx,_A6:agentRouterVrrpTrackRtPfxLen,'agentRouterVrrpTrackRtPrioDec':agentRouterVrrpTrackRtPrioDec,'agentRouterVrrpTrackRtReachable':agentRouterVrrpTrackRtReachable,'agentRouterVrrpTrackRtStatus':agentRouterVrrpTrackRtStatus,'agentIpHelperGroup':agentIpHelperGroup,'agentIpHelperAdminMode':agentIpHelperAdminMode,'agentDhcpClientMsgsReceived':agentDhcpClientMsgsReceived,'agentDhcpClientMsgsRelayed':agentDhcpClientMsgsRelayed,'agentDhcpServerMsgsReceived':agentDhcpServerMsgsReceived,'agentDhcpServerMsgsRelayed':agentDhcpServerMsgsRelayed,'agentUdpClientMsgsReceived':agentUdpClientMsgsReceived,'agentUdpClientMsgsRelayed':agentUdpClientMsgsRelayed,'agentSwitchIpHelperAddressTable':agentSwitchIpHelperAddressTable,'agentSwitchIpHelperAddressEntry':agentSwitchIpHelperAddressEntry,_A7:agentSwitchIpHelperAddress,_A8:agentSwitchIpHelperUdpPort,'agentSwitchIpHelperHitCount':agentSwitchIpHelperHitCount,'agentSwitchIpHelperStatus':agentSwitchIpHelperStatus,'agentUdpClientMsgsTtlExpired':agentUdpClientMsgsTtlExpired,'agentUdpClientMsgsDiscarded':agentUdpClientMsgsDiscarded,'agentInternalVlanGroup':agentInternalVlanGroup,'agentInternalVlanBase':agentInternalVlanBase,'agentInternalVlanPolicy':agentInternalVlanPolicy,'agentSwitchInternalVlanTable':agentSwitchInternalVlanTable,'agentSwitchInternalVlanEntry':agentSwitchInternalVlanEntry,_A9:agentSwitchInternalVlanId,'agentSwitchInternalVlanIfIndex':agentSwitchInternalVlanIfIndex,'agentOspfQueueGroup':agentOspfQueueGroup,'agentOspfQueueTable':agentOspfQueueTable,'agentOspfQueueEntry':agentOspfQueueEntry,_AA:agentOspfQueueIndex,'agentOspfQueueName':agentOspfQueueName,'agentOspfQueueLength':agentOspfQueueLength,'agentOspfQueueHigh':agentOspfQueueHigh,'agentOspfQueueDrops':agentOspfQueueDrops,'agentOspfQueueLimit':agentOspfQueueLimit,'agentOspfPacketStatsGroup':agentOspfPacketStatsGroup,'agentOspfCountersCleared':agentOspfCountersCleared,'agentOspfLsaRetxCount':agentOspfLsaRetxCount,'agentOspfHellosRx':agentOspfHellosRx,'agentOspfHellosTx':agentOspfHellosTx,'agentOspfDdRx':agentOspfDdRx,'agentOspfDdTx':agentOspfDdTx,'agentOspfLsReqRx':agentOspfLsReqRx,'agentOspfLsReqTx':agentOspfLsReqTx,'agentOspfLsUpdatesRx':agentOspfLsUpdatesRx,'agentOspfLsUpdatesTx':agentOspfLsUpdatesTx,'agentOspfLsAckRx':agentOspfLsAckRx,'agentOspfLsAckTx':agentOspfLsAckTx,'agentOspfLsUpdatesRxMax':agentOspfLsUpdatesRxMax,'agentOspfLsUpdatesTxMax':agentOspfLsUpdatesTxMax,'agentOspfType1LsasRx':agentOspfType1LsasRx,'agentOspfType2LsasRx':agentOspfType2LsasRx,'agentOspfType3LsasRx':agentOspfType3LsasRx,'agentOspfType4LsasRx':agentOspfType4LsasRx,'agentOspfType5LsasRx':agentOspfType5LsasRx,'agentOspfType7LsasRx':agentOspfType7LsasRx,'agentOspfType9LsasRx':agentOspfType9LsasRx,'agentOspfType10LsasRx':agentOspfType10LsasRx,'agentOspfType11LsasRx':agentOspfType11LsasRx,'agentOspfSpfStatsTable':agentOspfSpfStatsTable,'agentOspfSpfStatsEntry':agentOspfSpfStatsEntry,_AB:agentOspfSpfIndex,'agentOspfSpfStatsDeltaT':agentOspfSpfStatsDeltaT,'agentOspfSpfStatsIntra':agentOspfSpfStatsIntra,'agentOspfSpfStatsSumm':agentOspfSpfStatsSumm,'agentOspfSpfStatsExt':agentOspfSpfStatsExt,'agentOspfSpfStatsSpfTotal':agentOspfSpfStatsSpfTotal,'agentOspfSpfStatsRibUpdate':agentOspfSpfStatsRibUpdate,'agentOspfSpfStatsReason':agentOspfSpfStatsReason,'agentRoutingHeapGroup':agentRoutingHeapGroup,'agentRoutingHeapSize':agentRoutingHeapSize,'agentRoutingHeapInUse':agentRoutingHeapInUse,'agentRoutingHeapHigh':agentRoutingHeapHigh,'agentRoutingTableSummaryGroup':agentRoutingTableSummaryGroup,'agentConnectedRoutes':agentConnectedRoutes,'agentStaticRoutes':agentStaticRoutes,'agentRipRoutes':agentRipRoutes,'agentOspfRoutes':agentOspfRoutes,'agentOspfIntraRoutes':agentOspfIntraRoutes,'agentOspfInterRoutes':agentOspfInterRoutes,'agentOspfExt1Routes':agentOspfExt1Routes,'agentOspfExt2Routes':agentOspfExt2Routes,'agentBgpRoutes':agentBgpRoutes,'agentEbgpRoutes':agentEbgpRoutes,'agentIbgpRoutes':agentIbgpRoutes,'agentLocalBgpRoutes':agentLocalBgpRoutes,'agentRejectRoutes':agentRejectRoutes,'agentTotalRoutes':agentTotalRoutes,'agentBestRoutes':agentBestRoutes,'agentBestRoutesHigh':agentBestRoutesHigh,'agentAlternateRoutes':agentAlternateRoutes,'agentRouteAdds':agentRouteAdds,'agentRouteModifies':agentRouteModifies,'agentRouteDeletes':agentRouteDeletes,'agentUnresolvedRouteAdds':agentUnresolvedRouteAdds,'agentInvalidRouteAdds':agentInvalidRouteAdds,'agentFailedRouteAdds':agentFailedRouteAdds,'agentReservedLocals':agentReservedLocals,'agentUniqueNextHops':agentUniqueNextHops,'agentUniqueNextHopsHigh':agentUniqueNextHopsHigh,'agentNextHopGroups':agentNextHopGroups,'agentNextHopGroupsHigh':agentNextHopGroupsHigh,'agentEcmpGroups':agentEcmpGroups,'agentEcmpGroupsHigh':agentEcmpGroupsHigh,'agentEcmpRoutes':agentEcmpRoutes,'agentTruncEcmpRoutes':agentTruncEcmpRoutes,'agentEcmpRetries':agentEcmpRetries,'agentEcmpCountTable':agentEcmpCountTable,'agentEcmpCountEntry':agentEcmpCountEntry,_AC:agentEcmpNextHopCount,'agentEcmpRouteCount':agentEcmpRouteCount,'agentOspfStubRouterGroup':agentOspfStubRouterGroup,'ospfStubRouterAdvertisement':ospfStubRouterAdvertisement,'agentOspfStubRouterReason':agentOspfStubRouterReason,'agentOspfStubRouterStartupTimeRemaining':agentOspfStubRouterStartupTimeRemaining,'agentOspfStubRouterDuration':agentOspfStubRouterDuration,'agentRoutesConfigGroup':agentRoutesConfigGroup,'agentStaticRoutesTable':agentStaticRoutesTable,'agentStaticRoutesTableEntry':agentStaticRoutesTableEntry,_AD:agentStaticRoutesNetworkAddress,_AE:agentStaticRoutesNetMask,_AF:agentStaticRoutesNextHop,_AG:agentStaticRoutesType,_AH:agentStaticRoutesPreference,'agentStaticRoutesStatus':agentStaticRoutesStatus})