_A7='agentOspfv3IfEntry'
_A6='agentOspfv3AsLsdbRouterId'
_A5='agentOspfv3AsLsdbLsid'
_A4='agentOspfv3AsLsdbType'
_A3='AutoCostRefBw'
_A2='unknownArea'
_A1='unknownLink'
_A0='intraPrefix'
_z='nssaExternal'
_y='multicastGroup'
_x='asExternal'
_w='interRouter'
_v='interNetwork'
_u='networkLink'
_t='routerLink'
_s='illegalLSA'
_r='agentOspfv3LsdbRouterId'
_q='agentOspfv3LsdbLsid'
_p='agentOspfv3LsdbType'
_o='agentOspfv3LsdbAreaId'
_n='agentOspfv3RouteRedistSource'
_m='externalType2'
_l='externalType1'
_k='agentRipngIfIndex'
_j='static'
_i='connected'
_h='agentRipngRouteRedistSource'
_g='agentDhcp6ClientInterfaceIndex'
_f='agentIpv6StaticNeighborIfIndex'
_e='agentIpv6NeighborAddress'
_d='agentIpv6NeighborIfIndex'
_c='unknown'
_b='reachable'
_a='agentIpv6ServicePortNbrAddr'
_Z='agentIpv6ServicePortDefaultRouterIndex'
_Y='agentIpv6ServicePortPrefixIndex'
_X='agentIpv6StaticRouteNextHop'
_W='agentIpv6StaticRouteIfIndex'
_V='agentIpv6StaticRoutePfxLength'
_U='agentIpv6StaticRouteDest'
_T='agentIpv6AddrAddress'
_S='agentIpv6AddrPrefixLength'
_R='agentIpv6AddrPrefix'
_Q='agentIpv6RouterAdvertisementIfIndex'
_P='DisplayString'
_O='seconds'
_N='bits'
_M='Unsigned32'
_L='OctetString'
_K='agentIpv6InterfaceIfIndex'
_J='read-create'
_I='TruthValue'
_H='not-accessible'
_G='disable'
_F='enable'
_E='ROUTING6-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,Ipv6AddressIfIdentifier,Ipv6AddressPrefix,Ipv6IfIndex,Ipv6IfIndexOrZero=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressIfIdentifier','Ipv6AddressPrefix','Ipv6IfIndex','Ipv6IfIndexOrZero')
AreaID,RouterID=mibBuilder.importSymbols('OSPF-MIB','AreaID','RouterID')
ospfv3AreaEntry,ospfv3IfEntry,ospfv3VirtIfEntry=mibBuilder.importSymbols('OSPFV3-MIB','ospfv3AreaEntry','ospfv3IfEntry','ospfv3VirtIfEntry')
switch,=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','switch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC',_P,'MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_I,'VariablePointer')
routingIpv6=ModuleIdentity((1,3,6,1,4,1,7244,2,30))
if mibBuilder.loadTexts:routingIpv6.setRevisions(('2011-08-31 00:00',))
class SpfTimerRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class AutoCostRefBw(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967))
_AgentIpv6Group_ObjectIdentity=ObjectIdentity
agentIpv6Group=_AgentIpv6Group_ObjectIdentity((1,3,6,1,4,1,7244,2,30,1))
class _AgentIpv6RoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentIpv6RoutingMode_Type.__name__=_C
_AgentIpv6RoutingMode_Object=MibScalar
agentIpv6RoutingMode=_AgentIpv6RoutingMode_Object((1,3,6,1,4,1,7244,2,30,1,1),_AgentIpv6RoutingMode_Type())
agentIpv6RoutingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RoutingMode.setStatus(_A)
_AgentIpv6InterfaceTable_Object=MibTable
agentIpv6InterfaceTable=_AgentIpv6InterfaceTable_Object((1,3,6,1,4,1,7244,2,30,1,2))
if mibBuilder.loadTexts:agentIpv6InterfaceTable.setStatus(_A)
_AgentIpv6InterfaceEntry_Object=MibTableRow
agentIpv6InterfaceEntry=_AgentIpv6InterfaceEntry_Object((1,3,6,1,4,1,7244,2,30,1,2,1))
agentIpv6InterfaceEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:agentIpv6InterfaceEntry.setStatus(_A)
class _AgentIpv6InterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIpv6InterfaceIfIndex_Type.__name__=_C
_AgentIpv6InterfaceIfIndex_Object=MibTableColumn
agentIpv6InterfaceIfIndex=_AgentIpv6InterfaceIfIndex_Object((1,3,6,1,4,1,7244,2,30,1,2,1,1),_AgentIpv6InterfaceIfIndex_Type())
agentIpv6InterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6InterfaceIfIndex.setStatus(_A)
class _AgentIpv6InterfaceMtuValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1280,1500))
_AgentIpv6InterfaceMtuValue_Type.__name__=_M
_AgentIpv6InterfaceMtuValue_Object=MibTableColumn
agentIpv6InterfaceMtuValue=_AgentIpv6InterfaceMtuValue_Object((1,3,6,1,4,1,7244,2,30,1,2,1,2),_AgentIpv6InterfaceMtuValue_Type())
agentIpv6InterfaceMtuValue.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6InterfaceMtuValue.setStatus(_A)
class _AgentIpv6InterfaceDadTransmits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_AgentIpv6InterfaceDadTransmits_Type.__name__=_C
_AgentIpv6InterfaceDadTransmits_Object=MibTableColumn
agentIpv6InterfaceDadTransmits=_AgentIpv6InterfaceDadTransmits_Object((1,3,6,1,4,1,7244,2,30,1,2,1,3),_AgentIpv6InterfaceDadTransmits_Type())
agentIpv6InterfaceDadTransmits.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6InterfaceDadTransmits.setStatus(_A)
class _AgentIpv6InterfaceLinkLocalOnly_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentIpv6InterfaceLinkLocalOnly_Type.__name__=_C
_AgentIpv6InterfaceLinkLocalOnly_Object=MibTableColumn
agentIpv6InterfaceLinkLocalOnly=_AgentIpv6InterfaceLinkLocalOnly_Object((1,3,6,1,4,1,7244,2,30,1,2,1,4),_AgentIpv6InterfaceLinkLocalOnly_Type())
agentIpv6InterfaceLinkLocalOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6InterfaceLinkLocalOnly.setStatus(_A)
class _AgentIpv6InterfaceIcmpUnreachables_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentIpv6InterfaceIcmpUnreachables_Type.__name__=_C
_AgentIpv6InterfaceIcmpUnreachables_Object=MibTableColumn
agentIpv6InterfaceIcmpUnreachables=_AgentIpv6InterfaceIcmpUnreachables_Object((1,3,6,1,4,1,7244,2,30,1,2,1,5),_AgentIpv6InterfaceIcmpUnreachables_Type())
agentIpv6InterfaceIcmpUnreachables.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6InterfaceIcmpUnreachables.setStatus(_A)
class _AgentIpv6InterfaceAutoconfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentIpv6InterfaceAutoconfig_Type.__name__=_C
_AgentIpv6InterfaceAutoconfig_Object=MibTableColumn
agentIpv6InterfaceAutoconfig=_AgentIpv6InterfaceAutoconfig_Object((1,3,6,1,4,1,7244,2,30,1,2,1,6),_AgentIpv6InterfaceAutoconfig_Type())
agentIpv6InterfaceAutoconfig.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6InterfaceAutoconfig.setStatus(_A)
class _AgentIpv6InterfaceDhcpClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentIpv6InterfaceDhcpClient_Type.__name__=_C
_AgentIpv6InterfaceDhcpClient_Object=MibTableColumn
agentIpv6InterfaceDhcpClient=_AgentIpv6InterfaceDhcpClient_Object((1,3,6,1,4,1,7244,2,30,1,2,1,7),_AgentIpv6InterfaceDhcpClient_Type())
agentIpv6InterfaceDhcpClient.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6InterfaceDhcpClient.setStatus(_A)
_AgentIpv6RouterAdvertisementTable_Object=MibTable
agentIpv6RouterAdvertisementTable=_AgentIpv6RouterAdvertisementTable_Object((1,3,6,1,4,1,7244,2,30,1,3))
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementTable.setStatus(_A)
_AgentIpv6RouterAdvertisementEntry_Object=MibTableRow
agentIpv6RouterAdvertisementEntry=_AgentIpv6RouterAdvertisementEntry_Object((1,3,6,1,4,1,7244,2,30,1,3,1))
agentIpv6RouterAdvertisementEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementEntry.setStatus(_A)
class _AgentIpv6RouterAdvertisementIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIpv6RouterAdvertisementIfIndex_Type.__name__=_C
_AgentIpv6RouterAdvertisementIfIndex_Object=MibTableColumn
agentIpv6RouterAdvertisementIfIndex=_AgentIpv6RouterAdvertisementIfIndex_Object((1,3,6,1,4,1,7244,2,30,1,3,1,1),_AgentIpv6RouterAdvertisementIfIndex_Type())
agentIpv6RouterAdvertisementIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementIfIndex.setStatus(_A)
class _AgentIpv6RouterAdvertisementSuppressMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentIpv6RouterAdvertisementSuppressMode_Type.__name__=_C
_AgentIpv6RouterAdvertisementSuppressMode_Object=MibTableColumn
agentIpv6RouterAdvertisementSuppressMode=_AgentIpv6RouterAdvertisementSuppressMode_Object((1,3,6,1,4,1,7244,2,30,1,3,1,2),_AgentIpv6RouterAdvertisementSuppressMode_Type())
agentIpv6RouterAdvertisementSuppressMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementSuppressMode.setStatus(_A)
class _AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type.__name__=_C
_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Object=MibTableColumn
agentIpv6RouterAdvertisementMaxAdvertisementInterval=_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Object((1,3,6,1,4,1,7244,2,30,1,3,1,3),_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type())
agentIpv6RouterAdvertisementMaxAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementMaxAdvertisementInterval.setStatus(_A)
class _AgentIpv6RouterAdvertisementMinAdvertisementInterval_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1350))
_AgentIpv6RouterAdvertisementMinAdvertisementInterval_Type.__name__=_C
_AgentIpv6RouterAdvertisementMinAdvertisementInterval_Object=MibTableColumn
agentIpv6RouterAdvertisementMinAdvertisementInterval=_AgentIpv6RouterAdvertisementMinAdvertisementInterval_Object((1,3,6,1,4,1,7244,2,30,1,3,1,4),_AgentIpv6RouterAdvertisementMinAdvertisementInterval_Type())
agentIpv6RouterAdvertisementMinAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementMinAdvertisementInterval.setStatus(_A)
class _AgentIpv6RouterAdvertisementAdvertisementLifetime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_AgentIpv6RouterAdvertisementAdvertisementLifetime_Type.__name__=_C
_AgentIpv6RouterAdvertisementAdvertisementLifetime_Object=MibTableColumn
agentIpv6RouterAdvertisementAdvertisementLifetime=_AgentIpv6RouterAdvertisementAdvertisementLifetime_Object((1,3,6,1,4,1,7244,2,30,1,3,1,5),_AgentIpv6RouterAdvertisementAdvertisementLifetime_Type())
agentIpv6RouterAdvertisementAdvertisementLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementAdvertisementLifetime.setStatus(_A)
class _AgentIpv6RouterAdvertisementNbrSolicitInterval_Type(Unsigned32):defaultValue=0
_AgentIpv6RouterAdvertisementNbrSolicitInterval_Type.__name__=_M
_AgentIpv6RouterAdvertisementNbrSolicitInterval_Object=MibTableColumn
agentIpv6RouterAdvertisementNbrSolicitInterval=_AgentIpv6RouterAdvertisementNbrSolicitInterval_Object((1,3,6,1,4,1,7244,2,30,1,3,1,6),_AgentIpv6RouterAdvertisementNbrSolicitInterval_Type())
agentIpv6RouterAdvertisementNbrSolicitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementNbrSolicitInterval.setStatus(_A)
class _AgentIpv6RouterAdvertisementReachableTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_AgentIpv6RouterAdvertisementReachableTime_Type.__name__=_C
_AgentIpv6RouterAdvertisementReachableTime_Object=MibTableColumn
agentIpv6RouterAdvertisementReachableTime=_AgentIpv6RouterAdvertisementReachableTime_Object((1,3,6,1,4,1,7244,2,30,1,3,1,7),_AgentIpv6RouterAdvertisementReachableTime_Type())
agentIpv6RouterAdvertisementReachableTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementReachableTime.setStatus(_A)
class _AgentIpv6RouterAdvertisementManagedFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentIpv6RouterAdvertisementManagedFlag_Type.__name__=_C
_AgentIpv6RouterAdvertisementManagedFlag_Object=MibTableColumn
agentIpv6RouterAdvertisementManagedFlag=_AgentIpv6RouterAdvertisementManagedFlag_Object((1,3,6,1,4,1,7244,2,30,1,3,1,8),_AgentIpv6RouterAdvertisementManagedFlag_Type())
agentIpv6RouterAdvertisementManagedFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementManagedFlag.setStatus(_A)
class _AgentIpv6RouterAdvertisementOtherFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentIpv6RouterAdvertisementOtherFlag_Type.__name__=_C
_AgentIpv6RouterAdvertisementOtherFlag_Object=MibTableColumn
agentIpv6RouterAdvertisementOtherFlag=_AgentIpv6RouterAdvertisementOtherFlag_Object((1,3,6,1,4,1,7244,2,30,1,3,1,9),_AgentIpv6RouterAdvertisementOtherFlag_Type())
agentIpv6RouterAdvertisementOtherFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementOtherFlag.setStatus(_A)
_AgentIpv6AddrPrefixTable_Object=MibTable
agentIpv6AddrPrefixTable=_AgentIpv6AddrPrefixTable_Object((1,3,6,1,4,1,7244,2,30,1,4))
if mibBuilder.loadTexts:agentIpv6AddrPrefixTable.setStatus(_A)
_AgentIpv6AddrPrefixEntry_Object=MibTableRow
agentIpv6AddrPrefixEntry=_AgentIpv6AddrPrefixEntry_Object((1,3,6,1,4,1,7244,2,30,1,4,1))
agentIpv6AddrPrefixEntry.setIndexNames((0,_E,_K),(0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:agentIpv6AddrPrefixEntry.setStatus(_A)
_AgentIpv6AddrPrefix_Type=Ipv6AddressPrefix
_AgentIpv6AddrPrefix_Object=MibTableColumn
agentIpv6AddrPrefix=_AgentIpv6AddrPrefix_Object((1,3,6,1,4,1,7244,2,30,1,4,1,1),_AgentIpv6AddrPrefix_Type())
agentIpv6AddrPrefix.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6AddrPrefix.setStatus(_A)
class _AgentIpv6AddrPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6AddrPrefixLength_Type.__name__=_C
_AgentIpv6AddrPrefixLength_Object=MibTableColumn
agentIpv6AddrPrefixLength=_AgentIpv6AddrPrefixLength_Object((1,3,6,1,4,1,7244,2,30,1,4,1,2),_AgentIpv6AddrPrefixLength_Type())
agentIpv6AddrPrefixLength.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6AddrPrefixLength.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPrefixLength.setUnits(_N)
_AgentIpv6AddrPrefixOnLinkFlag_Type=TruthValue
_AgentIpv6AddrPrefixOnLinkFlag_Object=MibTableColumn
agentIpv6AddrPrefixOnLinkFlag=_AgentIpv6AddrPrefixOnLinkFlag_Object((1,3,6,1,4,1,7244,2,30,1,4,1,3),_AgentIpv6AddrPrefixOnLinkFlag_Type())
agentIpv6AddrPrefixOnLinkFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6AddrPrefixOnLinkFlag.setStatus(_A)
_AgentIpv6AddrPrefixAutonomousFlag_Type=TruthValue
_AgentIpv6AddrPrefixAutonomousFlag_Object=MibTableColumn
agentIpv6AddrPrefixAutonomousFlag=_AgentIpv6AddrPrefixAutonomousFlag_Object((1,3,6,1,4,1,7244,2,30,1,4,1,4),_AgentIpv6AddrPrefixAutonomousFlag_Type())
agentIpv6AddrPrefixAutonomousFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAutonomousFlag.setStatus(_A)
_AgentIpv6AddrPrefixAdvPreferredLifetime_Type=Unsigned32
_AgentIpv6AddrPrefixAdvPreferredLifetime_Object=MibTableColumn
agentIpv6AddrPrefixAdvPreferredLifetime=_AgentIpv6AddrPrefixAdvPreferredLifetime_Object((1,3,6,1,4,1,7244,2,30,1,4,1,5),_AgentIpv6AddrPrefixAdvPreferredLifetime_Type())
agentIpv6AddrPrefixAdvPreferredLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvPreferredLifetime.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvPreferredLifetime.setUnits(_O)
_AgentIpv6AddrPrefixAdvValidLifetime_Type=Unsigned32
_AgentIpv6AddrPrefixAdvValidLifetime_Object=MibTableColumn
agentIpv6AddrPrefixAdvValidLifetime=_AgentIpv6AddrPrefixAdvValidLifetime_Object((1,3,6,1,4,1,7244,2,30,1,4,1,6),_AgentIpv6AddrPrefixAdvValidLifetime_Type())
agentIpv6AddrPrefixAdvValidLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvValidLifetime.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvValidLifetime.setUnits(_O)
_AgentIpv6AddrTable_Object=MibTable
agentIpv6AddrTable=_AgentIpv6AddrTable_Object((1,3,6,1,4,1,7244,2,30,1,5))
if mibBuilder.loadTexts:agentIpv6AddrTable.setStatus(_A)
_AgentIpv6AddrEntry_Object=MibTableRow
agentIpv6AddrEntry=_AgentIpv6AddrEntry_Object((1,3,6,1,4,1,7244,2,30,1,5,1))
agentIpv6AddrEntry.setIndexNames((0,_E,_K),(0,_E,_T))
if mibBuilder.loadTexts:agentIpv6AddrEntry.setStatus(_A)
_AgentIpv6AddrAddress_Type=Ipv6Address
_AgentIpv6AddrAddress_Object=MibTableColumn
agentIpv6AddrAddress=_AgentIpv6AddrAddress_Object((1,3,6,1,4,1,7244,2,30,1,5,1,1),_AgentIpv6AddrAddress_Type())
agentIpv6AddrAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6AddrAddress.setStatus(_A)
class _AgentIpv6AddrPfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6AddrPfxLength_Type.__name__=_C
_AgentIpv6AddrPfxLength_Object=MibTableColumn
agentIpv6AddrPfxLength=_AgentIpv6AddrPfxLength_Object((1,3,6,1,4,1,7244,2,30,1,5,1,2),_AgentIpv6AddrPfxLength_Type())
agentIpv6AddrPfxLength.setMaxAccess(_J)
if mibBuilder.loadTexts:agentIpv6AddrPfxLength.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPfxLength.setUnits(_N)
_AgentIpv6AddrEui64Flag_Type=TruthValue
_AgentIpv6AddrEui64Flag_Object=MibTableColumn
agentIpv6AddrEui64Flag=_AgentIpv6AddrEui64Flag_Object((1,3,6,1,4,1,7244,2,30,1,5,1,3),_AgentIpv6AddrEui64Flag_Type())
agentIpv6AddrEui64Flag.setMaxAccess(_J)
if mibBuilder.loadTexts:agentIpv6AddrEui64Flag.setStatus(_A)
_AgentIpv6AddrStatus_Type=RowStatus
_AgentIpv6AddrStatus_Object=MibTableColumn
agentIpv6AddrStatus=_AgentIpv6AddrStatus_Object((1,3,6,1,4,1,7244,2,30,1,5,1,4),_AgentIpv6AddrStatus_Type())
agentIpv6AddrStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:agentIpv6AddrStatus.setStatus(_A)
_AgentIpv6StaticRouteTable_Object=MibTable
agentIpv6StaticRouteTable=_AgentIpv6StaticRouteTable_Object((1,3,6,1,4,1,7244,2,30,1,6))
if mibBuilder.loadTexts:agentIpv6StaticRouteTable.setStatus(_A)
_AgentIpv6StaticRouteEntry_Object=MibTableRow
agentIpv6StaticRouteEntry=_AgentIpv6StaticRouteEntry_Object((1,3,6,1,4,1,7244,2,30,1,6,1))
agentIpv6StaticRouteEntry.setIndexNames((0,_E,_U),(0,_E,_V),(0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:agentIpv6StaticRouteEntry.setStatus(_A)
_AgentIpv6StaticRouteDest_Type=Ipv6AddressPrefix
_AgentIpv6StaticRouteDest_Object=MibTableColumn
agentIpv6StaticRouteDest=_AgentIpv6StaticRouteDest_Object((1,3,6,1,4,1,7244,2,30,1,6,1,1),_AgentIpv6StaticRouteDest_Type())
agentIpv6StaticRouteDest.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6StaticRouteDest.setStatus(_A)
class _AgentIpv6StaticRoutePfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6StaticRoutePfxLength_Type.__name__=_C
_AgentIpv6StaticRoutePfxLength_Object=MibTableColumn
agentIpv6StaticRoutePfxLength=_AgentIpv6StaticRoutePfxLength_Object((1,3,6,1,4,1,7244,2,30,1,6,1,2),_AgentIpv6StaticRoutePfxLength_Type())
agentIpv6StaticRoutePfxLength.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6StaticRoutePfxLength.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6StaticRoutePfxLength.setUnits(_N)
_AgentIpv6StaticRouteIfIndex_Type=Ipv6IfIndexOrZero
_AgentIpv6StaticRouteIfIndex_Object=MibTableColumn
agentIpv6StaticRouteIfIndex=_AgentIpv6StaticRouteIfIndex_Object((1,3,6,1,4,1,7244,2,30,1,6,1,3),_AgentIpv6StaticRouteIfIndex_Type())
agentIpv6StaticRouteIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6StaticRouteIfIndex.setStatus(_A)
_AgentIpv6StaticRouteNextHop_Type=Ipv6Address
_AgentIpv6StaticRouteNextHop_Object=MibTableColumn
agentIpv6StaticRouteNextHop=_AgentIpv6StaticRouteNextHop_Object((1,3,6,1,4,1,7244,2,30,1,6,1,4),_AgentIpv6StaticRouteNextHop_Type())
agentIpv6StaticRouteNextHop.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6StaticRouteNextHop.setStatus(_A)
class _AgentIpv6StaticRoutePreference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentIpv6StaticRoutePreference_Type.__name__=_C
_AgentIpv6StaticRoutePreference_Object=MibTableColumn
agentIpv6StaticRoutePreference=_AgentIpv6StaticRoutePreference_Object((1,3,6,1,4,1,7244,2,30,1,6,1,5),_AgentIpv6StaticRoutePreference_Type())
agentIpv6StaticRoutePreference.setMaxAccess(_J)
if mibBuilder.loadTexts:agentIpv6StaticRoutePreference.setStatus(_A)
_AgentIpv6StaticRouteStatus_Type=RowStatus
_AgentIpv6StaticRouteStatus_Object=MibTableColumn
agentIpv6StaticRouteStatus=_AgentIpv6StaticRouteStatus_Object((1,3,6,1,4,1,7244,2,30,1,6,1,6),_AgentIpv6StaticRouteStatus_Type())
agentIpv6StaticRouteStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:agentIpv6StaticRouteStatus.setStatus(_A)
_AgentIpv6ServicePortGroup_ObjectIdentity=ObjectIdentity
agentIpv6ServicePortGroup=_AgentIpv6ServicePortGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,30,1,7))
_AgentIpv6ServicePortPrefixTable_Object=MibTable
agentIpv6ServicePortPrefixTable=_AgentIpv6ServicePortPrefixTable_Object((1,3,6,1,4,1,7244,2,30,1,7,1))
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixTable.setStatus(_A)
_AgentIpv6ServicePortPrefixEntry_Object=MibTableRow
agentIpv6ServicePortPrefixEntry=_AgentIpv6ServicePortPrefixEntry_Object((1,3,6,1,4,1,7244,2,30,1,7,1,1))
agentIpv6ServicePortPrefixEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixEntry.setStatus(_A)
_AgentIpv6ServicePortPrefixIndex_Type=Unsigned32
_AgentIpv6ServicePortPrefixIndex_Object=MibTableColumn
agentIpv6ServicePortPrefixIndex=_AgentIpv6ServicePortPrefixIndex_Object((1,3,6,1,4,1,7244,2,30,1,7,1,1,1),_AgentIpv6ServicePortPrefixIndex_Type())
agentIpv6ServicePortPrefixIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixIndex.setStatus(_A)
_AgentIpv6ServicePortPrefix_Type=Ipv6Address
_AgentIpv6ServicePortPrefix_Object=MibTableColumn
agentIpv6ServicePortPrefix=_AgentIpv6ServicePortPrefix_Object((1,3,6,1,4,1,7244,2,30,1,7,1,1,2),_AgentIpv6ServicePortPrefix_Type())
agentIpv6ServicePortPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6ServicePortPrefix.setStatus(_A)
_AgentIpv6ServicePortPrefixLength_Type=Unsigned32
_AgentIpv6ServicePortPrefixLength_Object=MibTableColumn
agentIpv6ServicePortPrefixLength=_AgentIpv6ServicePortPrefixLength_Object((1,3,6,1,4,1,7244,2,30,1,7,1,1,3),_AgentIpv6ServicePortPrefixLength_Type())
agentIpv6ServicePortPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixLength.setStatus(_A)
_AgentIpv6ServicePortDefaultRouterTable_Object=MibTable
agentIpv6ServicePortDefaultRouterTable=_AgentIpv6ServicePortDefaultRouterTable_Object((1,3,6,1,4,1,7244,2,30,1,7,2))
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouterTable.setStatus(_A)
_AgentIpv6ServicePortDefaultRouterEntry_Object=MibTableRow
agentIpv6ServicePortDefaultRouterEntry=_AgentIpv6ServicePortDefaultRouterEntry_Object((1,3,6,1,4,1,7244,2,30,1,7,2,1))
agentIpv6ServicePortDefaultRouterEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouterEntry.setStatus(_A)
_AgentIpv6ServicePortDefaultRouterIndex_Type=Unsigned32
_AgentIpv6ServicePortDefaultRouterIndex_Object=MibTableColumn
agentIpv6ServicePortDefaultRouterIndex=_AgentIpv6ServicePortDefaultRouterIndex_Object((1,3,6,1,4,1,7244,2,30,1,7,2,1,1),_AgentIpv6ServicePortDefaultRouterIndex_Type())
agentIpv6ServicePortDefaultRouterIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouterIndex.setStatus(_A)
_AgentIpv6ServicePortDefaultRouter_Type=Ipv6Address
_AgentIpv6ServicePortDefaultRouter_Object=MibTableColumn
agentIpv6ServicePortDefaultRouter=_AgentIpv6ServicePortDefaultRouter_Object((1,3,6,1,4,1,7244,2,30,1,7,2,1,2),_AgentIpv6ServicePortDefaultRouter_Type())
agentIpv6ServicePortDefaultRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouter.setStatus(_A)
_AgentIpv6ServicePortNbrTable_Object=MibTable
agentIpv6ServicePortNbrTable=_AgentIpv6ServicePortNbrTable_Object((1,3,6,1,4,1,7244,2,30,1,7,3))
if mibBuilder.loadTexts:agentIpv6ServicePortNbrTable.setStatus(_A)
_AgentIpv6ServicePortNbrEntry_Object=MibTableRow
agentIpv6ServicePortNbrEntry=_AgentIpv6ServicePortNbrEntry_Object((1,3,6,1,4,1,7244,2,30,1,7,3,1))
agentIpv6ServicePortNbrEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:agentIpv6ServicePortNbrEntry.setStatus(_A)
_AgentIpv6ServicePortNbrAddr_Type=Ipv6Address
_AgentIpv6ServicePortNbrAddr_Object=MibTableColumn
agentIpv6ServicePortNbrAddr=_AgentIpv6ServicePortNbrAddr_Object((1,3,6,1,4,1,7244,2,30,1,7,3,1,1),_AgentIpv6ServicePortNbrAddr_Type())
agentIpv6ServicePortNbrAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrAddr.setStatus(_A)
_AgentIpv6ServicePortNbrPhysAddr_Type=MacAddress
_AgentIpv6ServicePortNbrPhysAddr_Object=MibTableColumn
agentIpv6ServicePortNbrPhysAddr=_AgentIpv6ServicePortNbrPhysAddr_Object((1,3,6,1,4,1,7244,2,30,1,7,3,1,2),_AgentIpv6ServicePortNbrPhysAddr_Type())
agentIpv6ServicePortNbrPhysAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrPhysAddr.setStatus(_A)
class _AgentIpv6ServicePortNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6)));namedValues=NamedValues(*((_b,1),('stale',2),('delay',3),('probe',4),(_c,6)))
_AgentIpv6ServicePortNbrState_Type.__name__=_C
_AgentIpv6ServicePortNbrState_Object=MibTableColumn
agentIpv6ServicePortNbrState=_AgentIpv6ServicePortNbrState_Object((1,3,6,1,4,1,7244,2,30,1,7,3,1,3),_AgentIpv6ServicePortNbrState_Type())
agentIpv6ServicePortNbrState.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrState.setStatus(_A)
_AgentIpv6ServicePortNbrUpdated_Type=TimeStamp
_AgentIpv6ServicePortNbrUpdated_Object=MibTableColumn
agentIpv6ServicePortNbrUpdated=_AgentIpv6ServicePortNbrUpdated_Object((1,3,6,1,4,1,7244,2,30,1,7,3,1,4),_AgentIpv6ServicePortNbrUpdated_Type())
agentIpv6ServicePortNbrUpdated.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrUpdated.setStatus(_A)
_AgentIpv6ServicePortNbrIsRouter_Type=TruthValue
_AgentIpv6ServicePortNbrIsRouter_Object=MibTableColumn
agentIpv6ServicePortNbrIsRouter=_AgentIpv6ServicePortNbrIsRouter_Object((1,3,6,1,4,1,7244,2,30,1,7,3,1,5),_AgentIpv6ServicePortNbrIsRouter_Type())
agentIpv6ServicePortNbrIsRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrIsRouter.setStatus(_A)
class _AgentIpv6ServicePortConfigProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('dhcp6',2)))
_AgentIpv6ServicePortConfigProtocol_Type.__name__=_C
_AgentIpv6ServicePortConfigProtocol_Object=MibScalar
agentIpv6ServicePortConfigProtocol=_AgentIpv6ServicePortConfigProtocol_Object((1,3,6,1,4,1,7244,2,30,1,7,4),_AgentIpv6ServicePortConfigProtocol_Type())
agentIpv6ServicePortConfigProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortConfigProtocol.setStatus(_A)
_AgentIpv6ServicePortDhcpRestart_Type=TruthValue
_AgentIpv6ServicePortDhcpRestart_Object=MibScalar
agentIpv6ServicePortDhcpRestart=_AgentIpv6ServicePortDhcpRestart_Object((1,3,6,1,4,1,7244,2,30,1,7,5),_AgentIpv6ServicePortDhcpRestart_Type())
agentIpv6ServicePortDhcpRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortDhcpRestart.setStatus(_A)
_AgentIpv6NeighborGroup_ObjectIdentity=ObjectIdentity
agentIpv6NeighborGroup=_AgentIpv6NeighborGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,30,1,9))
_AgentIpv6NeighborTable_Object=MibTable
agentIpv6NeighborTable=_AgentIpv6NeighborTable_Object((1,3,6,1,4,1,7244,2,30,1,9,1))
if mibBuilder.loadTexts:agentIpv6NeighborTable.setStatus(_A)
_AgentIpv6NeighborEntry_Object=MibTableRow
agentIpv6NeighborEntry=_AgentIpv6NeighborEntry_Object((1,3,6,1,4,1,7244,2,30,1,9,1,1))
agentIpv6NeighborEntry.setIndexNames((0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:agentIpv6NeighborEntry.setStatus(_A)
_AgentIpv6NeighborIfIndex_Type=Ipv6IfIndex
_AgentIpv6NeighborIfIndex_Object=MibTableColumn
agentIpv6NeighborIfIndex=_AgentIpv6NeighborIfIndex_Object((1,3,6,1,4,1,7244,2,30,1,9,1,1,1),_AgentIpv6NeighborIfIndex_Type())
agentIpv6NeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NeighborIfIndex.setStatus(_A)
_AgentIpv6NeighborAddress_Type=Ipv6Address
_AgentIpv6NeighborAddress_Object=MibTableColumn
agentIpv6NeighborAddress=_AgentIpv6NeighborAddress_Object((1,3,6,1,4,1,7244,2,30,1,9,1,1,2),_AgentIpv6NeighborAddress_Type())
agentIpv6NeighborAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NeighborAddress.setStatus(_A)
_AgentIpv6NeighborMacAddress_Type=PhysAddress
_AgentIpv6NeighborMacAddress_Object=MibTableColumn
agentIpv6NeighborMacAddress=_AgentIpv6NeighborMacAddress_Object((1,3,6,1,4,1,7244,2,30,1,9,1,1,3),_AgentIpv6NeighborMacAddress_Type())
agentIpv6NeighborMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NeighborMacAddress.setStatus(_A)
_AgentIpv6NeighborIsRouter_Type=TruthValue
_AgentIpv6NeighborIsRouter_Object=MibTableColumn
agentIpv6NeighborIsRouter=_AgentIpv6NeighborIsRouter_Object((1,3,6,1,4,1,7244,2,30,1,9,1,1,4),_AgentIpv6NeighborIsRouter_Type())
agentIpv6NeighborIsRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NeighborIsRouter.setStatus(_A)
class _AgentIpv6NeighborState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_b,1),('stale',2),('delay',3),('probe',4),('invalid',5),(_c,6)))
_AgentIpv6NeighborState_Type.__name__=_C
_AgentIpv6NeighborState_Object=MibTableColumn
agentIpv6NeighborState=_AgentIpv6NeighborState_Object((1,3,6,1,4,1,7244,2,30,1,9,1,1,5),_AgentIpv6NeighborState_Type())
agentIpv6NeighborState.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NeighborState.setStatus(_A)
_AgentIpv6NeighborLastUpdated_Type=TimeStamp
_AgentIpv6NeighborLastUpdated_Object=MibTableColumn
agentIpv6NeighborLastUpdated=_AgentIpv6NeighborLastUpdated_Object((1,3,6,1,4,1,7244,2,30,1,9,1,1,6),_AgentIpv6NeighborLastUpdated_Type())
agentIpv6NeighborLastUpdated.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NeighborLastUpdated.setStatus(_A)
_AgentIpv6StaticNeighbor_Object=MibTable
agentIpv6StaticNeighbor=_AgentIpv6StaticNeighbor_Object((1,3,6,1,4,1,7244,2,30,1,9,2))
if mibBuilder.loadTexts:agentIpv6StaticNeighbor.setStatus(_A)
_AgentIpv6StaticNeighborEntry_Object=MibTableRow
agentIpv6StaticNeighborEntry=_AgentIpv6StaticNeighborEntry_Object((1,3,6,1,4,1,7244,2,30,1,9,2,1))
agentIpv6StaticNeighborEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:agentIpv6StaticNeighborEntry.setStatus(_A)
_AgentIpv6StaticNeighborIfIndex_Type=Ipv6IfIndex
_AgentIpv6StaticNeighborIfIndex_Object=MibTableColumn
agentIpv6StaticNeighborIfIndex=_AgentIpv6StaticNeighborIfIndex_Object((1,3,6,1,4,1,7244,2,30,1,9,2,1,1),_AgentIpv6StaticNeighborIfIndex_Type())
agentIpv6StaticNeighborIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpv6StaticNeighborIfIndex.setStatus(_A)
_AgentIpv6StaticNeighborAddress_Type=Ipv6Address
_AgentIpv6StaticNeighborAddress_Object=MibTableColumn
agentIpv6StaticNeighborAddress=_AgentIpv6StaticNeighborAddress_Object((1,3,6,1,4,1,7244,2,30,1,9,2,1,2),_AgentIpv6StaticNeighborAddress_Type())
agentIpv6StaticNeighborAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6StaticNeighborAddress.setStatus(_A)
_AgentIpv6StaticNeighborMacAddress_Type=PhysAddress
_AgentIpv6StaticNeighborMacAddress_Object=MibTableColumn
agentIpv6StaticNeighborMacAddress=_AgentIpv6StaticNeighborMacAddress_Object((1,3,6,1,4,1,7244,2,30,1,9,2,1,3),_AgentIpv6StaticNeighborMacAddress_Type())
agentIpv6StaticNeighborMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6StaticNeighborMacAddress.setStatus(_A)
class _AgentIpv6StaticNeighborRowAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AgentIpv6StaticNeighborRowAddress_Type.__name__=_L
_AgentIpv6StaticNeighborRowAddress_Object=MibScalar
agentIpv6StaticNeighborRowAddress=_AgentIpv6StaticNeighborRowAddress_Object((1,3,6,1,4,1,7244,2,30,1,9,3),_AgentIpv6StaticNeighborRowAddress_Type())
agentIpv6StaticNeighborRowAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6StaticNeighborRowAddress.setStatus(_A)
_AgentIpv6StaticNeighborRowMacAddress_Type=PhysAddress
_AgentIpv6StaticNeighborRowMacAddress_Object=MibScalar
agentIpv6StaticNeighborRowMacAddress=_AgentIpv6StaticNeighborRowMacAddress_Object((1,3,6,1,4,1,7244,2,30,1,9,4),_AgentIpv6StaticNeighborRowMacAddress_Type())
agentIpv6StaticNeighborRowMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6StaticNeighborRowMacAddress.setStatus(_A)
_AgentIpv6StaticNeighborRowStatus_Type=RowStatus
_AgentIpv6StaticNeighborRowStatus_Object=MibScalar
agentIpv6StaticNeighborRowStatus=_AgentIpv6StaticNeighborRowStatus_Object((1,3,6,1,4,1,7244,2,30,1,9,5),_AgentIpv6StaticNeighborRowStatus_Type())
agentIpv6StaticNeighborRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6StaticNeighborRowStatus.setStatus(_A)
_AgentIpv6IcmpControlGroup_ObjectIdentity=ObjectIdentity
agentIpv6IcmpControlGroup=_AgentIpv6IcmpControlGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,30,1,10))
class _AgentIpv6IcmpRateLimitInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIpv6IcmpRateLimitInterval_Type.__name__=_C
_AgentIpv6IcmpRateLimitInterval_Object=MibScalar
agentIpv6IcmpRateLimitInterval=_AgentIpv6IcmpRateLimitInterval_Object((1,3,6,1,4,1,7244,2,30,1,10,1),_AgentIpv6IcmpRateLimitInterval_Type())
agentIpv6IcmpRateLimitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6IcmpRateLimitInterval.setStatus(_A)
class _AgentIpv6IcmpRateLimitBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_AgentIpv6IcmpRateLimitBurstSize_Type.__name__=_C
_AgentIpv6IcmpRateLimitBurstSize_Object=MibScalar
agentIpv6IcmpRateLimitBurstSize=_AgentIpv6IcmpRateLimitBurstSize_Object((1,3,6,1,4,1,7244,2,30,1,10,2),_AgentIpv6IcmpRateLimitBurstSize_Type())
agentIpv6IcmpRateLimitBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6IcmpRateLimitBurstSize.setStatus(_A)
_AgentDhcp6ClientParametersTable_Object=MibTable
agentDhcp6ClientParametersTable=_AgentDhcp6ClientParametersTable_Object((1,3,6,1,4,1,7244,2,30,1,11))
if mibBuilder.loadTexts:agentDhcp6ClientParametersTable.setStatus(_A)
_AgentDhcp6ClientParametersEntry_Object=MibTableRow
agentDhcp6ClientParametersEntry=_AgentDhcp6ClientParametersEntry_Object((1,3,6,1,4,1,7244,2,30,1,11,1))
agentDhcp6ClientParametersEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:agentDhcp6ClientParametersEntry.setStatus(_A)
_AgentDhcp6ClientInterfaceIndex_Type=Unsigned32
_AgentDhcp6ClientInterfaceIndex_Object=MibTableColumn
agentDhcp6ClientInterfaceIndex=_AgentDhcp6ClientInterfaceIndex_Object((1,3,6,1,4,1,7244,2,30,1,11,1,1),_AgentDhcp6ClientInterfaceIndex_Type())
agentDhcp6ClientInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientInterfaceIndex.setStatus(_A)
_AgentDhcp6ClientPrefix_Type=Ipv6AddressPrefix
_AgentDhcp6ClientPrefix_Object=MibTableColumn
agentDhcp6ClientPrefix=_AgentDhcp6ClientPrefix_Object((1,3,6,1,4,1,7244,2,30,1,11,1,2),_AgentDhcp6ClientPrefix_Type())
agentDhcp6ClientPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientPrefix.setStatus(_A)
_AgentDhcp6ClientPrefixlength_Type=Integer32
_AgentDhcp6ClientPrefixlength_Object=MibTableColumn
agentDhcp6ClientPrefixlength=_AgentDhcp6ClientPrefixlength_Object((1,3,6,1,4,1,7244,2,30,1,11,1,3),_AgentDhcp6ClientPrefixlength_Type())
agentDhcp6ClientPrefixlength.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientPrefixlength.setStatus(_A)
class _AgentDhcp6ClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('inactive',0),('solicit',1),('request',2),('active',3),('renew',4),('rebind',5),('release',6)))
_AgentDhcp6ClientState_Type.__name__=_C
_AgentDhcp6ClientState_Object=MibTableColumn
agentDhcp6ClientState=_AgentDhcp6ClientState_Object((1,3,6,1,4,1,7244,2,30,1,11,1,4),_AgentDhcp6ClientState_Type())
agentDhcp6ClientState.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientState.setStatus(_A)
class _AgentDhcp6ClientServerDUID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AgentDhcp6ClientServerDUID_Type.__name__=_P
_AgentDhcp6ClientServerDUID_Object=MibTableColumn
agentDhcp6ClientServerDUID=_AgentDhcp6ClientServerDUID_Object((1,3,6,1,4,1,7244,2,30,1,11,1,5),_AgentDhcp6ClientServerDUID_Type())
agentDhcp6ClientServerDUID.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientServerDUID.setStatus(_A)
_AgentDhcp6ClientT1Time_Type=Unsigned32
_AgentDhcp6ClientT1Time_Object=MibTableColumn
agentDhcp6ClientT1Time=_AgentDhcp6ClientT1Time_Object((1,3,6,1,4,1,7244,2,30,1,11,1,6),_AgentDhcp6ClientT1Time_Type())
agentDhcp6ClientT1Time.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientT1Time.setStatus(_A)
_AgentDhcp6ClientT2Time_Type=Unsigned32
_AgentDhcp6ClientT2Time_Object=MibTableColumn
agentDhcp6ClientT2Time=_AgentDhcp6ClientT2Time_Object((1,3,6,1,4,1,7244,2,30,1,11,1,7),_AgentDhcp6ClientT2Time_Type())
agentDhcp6ClientT2Time.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientT2Time.setStatus(_A)
_AgentDhcp6ClientIAID_Type=Unsigned32
_AgentDhcp6ClientIAID_Object=MibTableColumn
agentDhcp6ClientIAID=_AgentDhcp6ClientIAID_Object((1,3,6,1,4,1,7244,2,30,1,11,1,8),_AgentDhcp6ClientIAID_Type())
agentDhcp6ClientIAID.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientIAID.setStatus(_A)
_AgentDhcp6ClientPreferredLifeTime_Type=Unsigned32
_AgentDhcp6ClientPreferredLifeTime_Object=MibTableColumn
agentDhcp6ClientPreferredLifeTime=_AgentDhcp6ClientPreferredLifeTime_Object((1,3,6,1,4,1,7244,2,30,1,11,1,9),_AgentDhcp6ClientPreferredLifeTime_Type())
agentDhcp6ClientPreferredLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientPreferredLifeTime.setStatus(_A)
_AgentDhcp6ClientValidLifeTime_Type=Unsigned32
_AgentDhcp6ClientValidLifeTime_Object=MibTableColumn
agentDhcp6ClientValidLifeTime=_AgentDhcp6ClientValidLifeTime_Object((1,3,6,1,4,1,7244,2,30,1,11,1,10),_AgentDhcp6ClientValidLifeTime_Type())
agentDhcp6ClientValidLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientValidLifeTime.setStatus(_A)
_AgentDhcp6ClientRenewTime_Type=Unsigned32
_AgentDhcp6ClientRenewTime_Object=MibTableColumn
agentDhcp6ClientRenewTime=_AgentDhcp6ClientRenewTime_Object((1,3,6,1,4,1,7244,2,30,1,11,1,11),_AgentDhcp6ClientRenewTime_Type())
agentDhcp6ClientRenewTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientRenewTime.setStatus(_A)
_AgentDhcp6ClientExpireTime_Type=Unsigned32
_AgentDhcp6ClientExpireTime_Object=MibTableColumn
agentDhcp6ClientExpireTime=_AgentDhcp6ClientExpireTime_Object((1,3,6,1,4,1,7244,2,30,1,11,1,12),_AgentDhcp6ClientExpireTime_Type())
agentDhcp6ClientExpireTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDhcp6ClientExpireTime.setStatus(_A)
_AgentRouterRipngConfigGroup_ObjectIdentity=ObjectIdentity
agentRouterRipngConfigGroup=_AgentRouterRipngConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,30,2))
class _AgentRouterRipngAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRouterRipngAdminState_Type.__name__=_C
_AgentRouterRipngAdminState_Object=MibScalar
agentRouterRipngAdminState=_AgentRouterRipngAdminState_Object((1,3,6,1,4,1,7244,2,30,2,1),_AgentRouterRipngAdminState_Type())
agentRouterRipngAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipngAdminState.setStatus(_A)
class _AgentRouterRipngSplitHorizonMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('simple',2),('poisonReverse',3)))
_AgentRouterRipngSplitHorizonMode_Type.__name__=_C
_AgentRouterRipngSplitHorizonMode_Object=MibScalar
agentRouterRipngSplitHorizonMode=_AgentRouterRipngSplitHorizonMode_Object((1,3,6,1,4,1,7244,2,30,2,2),_AgentRouterRipngSplitHorizonMode_Type())
agentRouterRipngSplitHorizonMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipngSplitHorizonMode.setStatus(_A)
class _AgentRouterRipngDefaultMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_AgentRouterRipngDefaultMetric_Type.__name__=_C
_AgentRouterRipngDefaultMetric_Object=MibScalar
agentRouterRipngDefaultMetric=_AgentRouterRipngDefaultMetric_Object((1,3,6,1,4,1,7244,2,30,2,5),_AgentRouterRipngDefaultMetric_Type())
agentRouterRipngDefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipngDefaultMetric.setStatus(_A)
class _AgentRouterRipngDefaultMetricConfigured_Type(TruthValue):defaultValue=2
_AgentRouterRipngDefaultMetricConfigured_Type.__name__=_I
_AgentRouterRipngDefaultMetricConfigured_Object=MibScalar
agentRouterRipngDefaultMetricConfigured=_AgentRouterRipngDefaultMetricConfigured_Object((1,3,6,1,4,1,7244,2,30,2,6),_AgentRouterRipngDefaultMetricConfigured_Type())
agentRouterRipngDefaultMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipngDefaultMetricConfigured.setStatus(_A)
class _AgentRouterRipngDefaultInfoOriginate_Type(TruthValue):defaultValue=2
_AgentRouterRipngDefaultInfoOriginate_Type.__name__=_I
_AgentRouterRipngDefaultInfoOriginate_Object=MibScalar
agentRouterRipngDefaultInfoOriginate=_AgentRouterRipngDefaultInfoOriginate_Object((1,3,6,1,4,1,7244,2,30,2,7),_AgentRouterRipngDefaultInfoOriginate_Type())
agentRouterRipngDefaultInfoOriginate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipngDefaultInfoOriginate.setStatus(_A)
class _AgentRouterRipngDistance_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentRouterRipngDistance_Type.__name__=_C
_AgentRouterRipngDistance_Object=MibScalar
agentRouterRipngDistance=_AgentRouterRipngDistance_Object((1,3,6,1,4,1,7244,2,30,2,8),_AgentRouterRipngDistance_Type())
agentRouterRipngDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipngDistance.setStatus(_A)
_AgentRipngRouteRedistTable_Object=MibTable
agentRipngRouteRedistTable=_AgentRipngRouteRedistTable_Object((1,3,6,1,4,1,7244,2,30,2,9))
if mibBuilder.loadTexts:agentRipngRouteRedistTable.setStatus(_A)
_AgentRipngRouteRedistEntry_Object=MibTableRow
agentRipngRouteRedistEntry=_AgentRipngRouteRedistEntry_Object((1,3,6,1,4,1,7244,2,30,2,9,1))
agentRipngRouteRedistEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:agentRipngRouteRedistEntry.setStatus(_A)
class _AgentRipngRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),('ospf',3)))
_AgentRipngRouteRedistSource_Type.__name__=_C
_AgentRipngRouteRedistSource_Object=MibTableColumn
agentRipngRouteRedistSource=_AgentRipngRouteRedistSource_Object((1,3,6,1,4,1,7244,2,30,2,9,1,1),_AgentRipngRouteRedistSource_Type())
agentRipngRouteRedistSource.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRipngRouteRedistSource.setStatus(_A)
class _AgentRipngRouteRedistMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRipngRouteRedistMode_Type.__name__=_C
_AgentRipngRouteRedistMode_Object=MibTableColumn
agentRipngRouteRedistMode=_AgentRipngRouteRedistMode_Object((1,3,6,1,4,1,7244,2,30,2,9,1,2),_AgentRipngRouteRedistMode_Type())
agentRipngRouteRedistMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipngRouteRedistMode.setStatus(_A)
class _AgentRipngRouteRedistMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_AgentRipngRouteRedistMetric_Type.__name__=_C
_AgentRipngRouteRedistMetric_Object=MibTableColumn
agentRipngRouteRedistMetric=_AgentRipngRouteRedistMetric_Object((1,3,6,1,4,1,7244,2,30,2,9,1,3),_AgentRipngRouteRedistMetric_Type())
agentRipngRouteRedistMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipngRouteRedistMetric.setStatus(_A)
class _AgentRipngRouteRedistMetricConfigured_Type(TruthValue):defaultValue=2
_AgentRipngRouteRedistMetricConfigured_Type.__name__=_I
_AgentRipngRouteRedistMetricConfigured_Object=MibTableColumn
agentRipngRouteRedistMetricConfigured=_AgentRipngRouteRedistMetricConfigured_Object((1,3,6,1,4,1,7244,2,30,2,9,1,4),_AgentRipngRouteRedistMetricConfigured_Type())
agentRipngRouteRedistMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipngRouteRedistMetricConfigured.setStatus(_A)
class _AgentRouterRipngUpdateTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,2147483647))
_AgentRouterRipngUpdateTime_Type.__name__=_C
_AgentRouterRipngUpdateTime_Object=MibScalar
agentRouterRipngUpdateTime=_AgentRouterRipngUpdateTime_Object((1,3,6,1,4,1,7244,2,30,2,10),_AgentRouterRipngUpdateTime_Type())
agentRouterRipngUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipngUpdateTime.setStatus(_A)
class _AgentRouterRipngGarbageTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,2147483647))
_AgentRouterRipngGarbageTime_Type.__name__=_C
_AgentRouterRipngGarbageTime_Object=MibScalar
agentRouterRipngGarbageTime=_AgentRouterRipngGarbageTime_Object((1,3,6,1,4,1,7244,2,30,2,11),_AgentRouterRipngGarbageTime_Type())
agentRouterRipngGarbageTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipngGarbageTime.setStatus(_A)
class _AgentRouterRipngTimeoutTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,2147483647))
_AgentRouterRipngTimeoutTime_Type.__name__=_C
_AgentRouterRipngTimeoutTime_Object=MibScalar
agentRouterRipngTimeoutTime=_AgentRouterRipngTimeoutTime_Object((1,3,6,1,4,1,7244,2,30,2,12),_AgentRouterRipngTimeoutTime_Type())
agentRouterRipngTimeoutTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouterRipngTimeoutTime.setStatus(_A)
_AgentRipngIfTable_Object=MibTable
agentRipngIfTable=_AgentRipngIfTable_Object((1,3,6,1,4,1,7244,2,30,2,13))
if mibBuilder.loadTexts:agentRipngIfTable.setStatus(_A)
_AgentRipngIfEntry_Object=MibTableRow
agentRipngIfEntry=_AgentRipngIfEntry_Object((1,3,6,1,4,1,7244,2,30,2,13,1))
agentRipngIfEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:agentRipngIfEntry.setStatus(_A)
class _AgentRipngIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentRipngIfIndex_Type.__name__=_C
_AgentRipngIfIndex_Object=MibTableColumn
agentRipngIfIndex=_AgentRipngIfIndex_Object((1,3,6,1,4,1,7244,2,30,2,13,1,1),_AgentRipngIfIndex_Type())
agentRipngIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRipngIfIndex.setStatus(_A)
class _AgentRipngIfAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRipngIfAdminMode_Type.__name__=_C
_AgentRipngIfAdminMode_Object=MibTableColumn
agentRipngIfAdminMode=_AgentRipngIfAdminMode_Object((1,3,6,1,4,1,7244,2,30,2,13,1,2),_AgentRipngIfAdminMode_Type())
agentRipngIfAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipngIfAdminMode.setStatus(_A)
class _AgentRipngIfPassiveMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentRipngIfPassiveMode_Type.__name__=_C
_AgentRipngIfPassiveMode_Object=MibTableColumn
agentRipngIfPassiveMode=_AgentRipngIfPassiveMode_Object((1,3,6,1,4,1,7244,2,30,2,13,1,3),_AgentRipngIfPassiveMode_Type())
agentRipngIfPassiveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipngIfPassiveMode.setStatus(_A)
_AgentRouterOspfv3ConfigGroup_ObjectIdentity=ObjectIdentity
agentRouterOspfv3ConfigGroup=_AgentRouterOspfv3ConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,30,3))
class _AgentOspfv3DefaultMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_AgentOspfv3DefaultMetric_Type.__name__=_C
_AgentOspfv3DefaultMetric_Object=MibScalar
agentOspfv3DefaultMetric=_AgentOspfv3DefaultMetric_Object((1,3,6,1,4,1,7244,2,30,3,1),_AgentOspfv3DefaultMetric_Type())
agentOspfv3DefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3DefaultMetric.setStatus(_A)
_AgentOspfv3DefaultMetricConfigured_Type=TruthValue
_AgentOspfv3DefaultMetricConfigured_Object=MibScalar
agentOspfv3DefaultMetricConfigured=_AgentOspfv3DefaultMetricConfigured_Object((1,3,6,1,4,1,7244,2,30,3,2),_AgentOspfv3DefaultMetricConfigured_Type())
agentOspfv3DefaultMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3DefaultMetricConfigured.setStatus(_A)
class _AgentOspfv3DefaultInfoOriginate_Type(TruthValue):defaultValue=2
_AgentOspfv3DefaultInfoOriginate_Type.__name__=_I
_AgentOspfv3DefaultInfoOriginate_Object=MibScalar
agentOspfv3DefaultInfoOriginate=_AgentOspfv3DefaultInfoOriginate_Object((1,3,6,1,4,1,7244,2,30,3,3),_AgentOspfv3DefaultInfoOriginate_Type())
agentOspfv3DefaultInfoOriginate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3DefaultInfoOriginate.setStatus(_A)
class _AgentOspfv3DefaultInfoOriginateAlways_Type(TruthValue):defaultValue=2
_AgentOspfv3DefaultInfoOriginateAlways_Type.__name__=_I
_AgentOspfv3DefaultInfoOriginateAlways_Object=MibScalar
agentOspfv3DefaultInfoOriginateAlways=_AgentOspfv3DefaultInfoOriginateAlways_Object((1,3,6,1,4,1,7244,2,30,3,4),_AgentOspfv3DefaultInfoOriginateAlways_Type())
agentOspfv3DefaultInfoOriginateAlways.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3DefaultInfoOriginateAlways.setStatus(_A)
class _AgentOspfv3DefaultInfoOriginateMetric_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AgentOspfv3DefaultInfoOriginateMetric_Type.__name__=_C
_AgentOspfv3DefaultInfoOriginateMetric_Object=MibScalar
agentOspfv3DefaultInfoOriginateMetric=_AgentOspfv3DefaultInfoOriginateMetric_Object((1,3,6,1,4,1,7244,2,30,3,5),_AgentOspfv3DefaultInfoOriginateMetric_Type())
agentOspfv3DefaultInfoOriginateMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3DefaultInfoOriginateMetric.setStatus(_A)
_AgentOspfv3DefaultInfoOriginateMetricConfigured_Type=TruthValue
_AgentOspfv3DefaultInfoOriginateMetricConfigured_Object=MibScalar
agentOspfv3DefaultInfoOriginateMetricConfigured=_AgentOspfv3DefaultInfoOriginateMetricConfigured_Object((1,3,6,1,4,1,7244,2,30,3,6),_AgentOspfv3DefaultInfoOriginateMetricConfigured_Type())
agentOspfv3DefaultInfoOriginateMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3DefaultInfoOriginateMetricConfigured.setStatus(_A)
class _AgentOspfv3DefaultInfoOriginateMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_AgentOspfv3DefaultInfoOriginateMetricType_Type.__name__=_C
_AgentOspfv3DefaultInfoOriginateMetricType_Object=MibScalar
agentOspfv3DefaultInfoOriginateMetricType=_AgentOspfv3DefaultInfoOriginateMetricType_Object((1,3,6,1,4,1,7244,2,30,3,7),_AgentOspfv3DefaultInfoOriginateMetricType_Type())
agentOspfv3DefaultInfoOriginateMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3DefaultInfoOriginateMetricType.setStatus(_A)
_AgentOspfv3RouteRedistTable_Object=MibTable
agentOspfv3RouteRedistTable=_AgentOspfv3RouteRedistTable_Object((1,3,6,1,4,1,7244,2,30,3,8))
if mibBuilder.loadTexts:agentOspfv3RouteRedistTable.setStatus(_A)
_AgentOspfv3RouteRedistEntry_Object=MibTableRow
agentOspfv3RouteRedistEntry=_AgentOspfv3RouteRedistEntry_Object((1,3,6,1,4,1,7244,2,30,3,8,1))
agentOspfv3RouteRedistEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:agentOspfv3RouteRedistEntry.setStatus(_A)
class _AgentOspfv3RouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_AgentOspfv3RouteRedistSource_Type.__name__=_C
_AgentOspfv3RouteRedistSource_Object=MibTableColumn
agentOspfv3RouteRedistSource=_AgentOspfv3RouteRedistSource_Object((1,3,6,1,4,1,7244,2,30,3,8,1,1),_AgentOspfv3RouteRedistSource_Type())
agentOspfv3RouteRedistSource.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3RouteRedistSource.setStatus(_A)
class _AgentOspfv3RouteRedistMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentOspfv3RouteRedistMode_Type.__name__=_C
_AgentOspfv3RouteRedistMode_Object=MibTableColumn
agentOspfv3RouteRedistMode=_AgentOspfv3RouteRedistMode_Object((1,3,6,1,4,1,7244,2,30,3,8,1,2),_AgentOspfv3RouteRedistMode_Type())
agentOspfv3RouteRedistMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3RouteRedistMode.setStatus(_A)
class _AgentOspfv3RouteRedistMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_AgentOspfv3RouteRedistMetric_Type.__name__=_C
_AgentOspfv3RouteRedistMetric_Object=MibTableColumn
agentOspfv3RouteRedistMetric=_AgentOspfv3RouteRedistMetric_Object((1,3,6,1,4,1,7244,2,30,3,8,1,3),_AgentOspfv3RouteRedistMetric_Type())
agentOspfv3RouteRedistMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3RouteRedistMetric.setStatus(_A)
_AgentOspfv3RouteRedistMetricConfigured_Type=TruthValue
_AgentOspfv3RouteRedistMetricConfigured_Object=MibTableColumn
agentOspfv3RouteRedistMetricConfigured=_AgentOspfv3RouteRedistMetricConfigured_Object((1,3,6,1,4,1,7244,2,30,3,8,1,4),_AgentOspfv3RouteRedistMetricConfigured_Type())
agentOspfv3RouteRedistMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3RouteRedistMetricConfigured.setStatus(_A)
class _AgentOspfv3RouteRedistMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_AgentOspfv3RouteRedistMetricType_Type.__name__=_C
_AgentOspfv3RouteRedistMetricType_Object=MibTableColumn
agentOspfv3RouteRedistMetricType=_AgentOspfv3RouteRedistMetricType_Object((1,3,6,1,4,1,7244,2,30,3,8,1,5),_AgentOspfv3RouteRedistMetricType_Type())
agentOspfv3RouteRedistMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3RouteRedistMetricType.setStatus(_A)
_AgentOspfv3RouteRedistTag_Type=Unsigned32
_AgentOspfv3RouteRedistTag_Object=MibTableColumn
agentOspfv3RouteRedistTag=_AgentOspfv3RouteRedistTag_Object((1,3,6,1,4,1,7244,2,30,3,8,1,6),_AgentOspfv3RouteRedistTag_Type())
agentOspfv3RouteRedistTag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3RouteRedistTag.setStatus(_A)
_AgentOspfv3IfTable_Object=MibTable
agentOspfv3IfTable=_AgentOspfv3IfTable_Object((1,3,6,1,4,1,7244,2,30,3,9))
if mibBuilder.loadTexts:agentOspfv3IfTable.setStatus(_A)
_AgentOspfv3IfEntry_Object=MibTableRow
agentOspfv3IfEntry=_AgentOspfv3IfEntry_Object((1,3,6,1,4,1,7244,2,30,3,9,1))
if mibBuilder.loadTexts:agentOspfv3IfEntry.setStatus(_A)
class _AgentOspfv3IfIpMtuIgnoreFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentOspfv3IfIpMtuIgnoreFlag_Type.__name__=_C
_AgentOspfv3IfIpMtuIgnoreFlag_Object=MibTableColumn
agentOspfv3IfIpMtuIgnoreFlag=_AgentOspfv3IfIpMtuIgnoreFlag_Object((1,3,6,1,4,1,7244,2,30,3,9,1,2),_AgentOspfv3IfIpMtuIgnoreFlag_Type())
agentOspfv3IfIpMtuIgnoreFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3IfIpMtuIgnoreFlag.setStatus(_A)
class _AgentOspfv3IfPassiveMode_Type(TruthValue):defaultValue=2
_AgentOspfv3IfPassiveMode_Type.__name__=_I
_AgentOspfv3IfPassiveMode_Object=MibTableColumn
agentOspfv3IfPassiveMode=_AgentOspfv3IfPassiveMode_Object((1,3,6,1,4,1,7244,2,30,3,9,1,3),_AgentOspfv3IfPassiveMode_Type())
agentOspfv3IfPassiveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3IfPassiveMode.setStatus(_A)
_AgentOspfv3LsdbTable_Object=MibTable
agentOspfv3LsdbTable=_AgentOspfv3LsdbTable_Object((1,3,6,1,4,1,7244,2,30,3,10))
if mibBuilder.loadTexts:agentOspfv3LsdbTable.setStatus(_A)
_AgentOspfv3LsdbEntry_Object=MibTableRow
agentOspfv3LsdbEntry=_AgentOspfv3LsdbEntry_Object((1,3,6,1,4,1,7244,2,30,3,10,1))
agentOspfv3LsdbEntry.setIndexNames((0,_E,_o),(0,_E,_p),(0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:agentOspfv3LsdbEntry.setStatus(_A)
_AgentOspfv3LsdbAreaId_Type=AreaID
_AgentOspfv3LsdbAreaId_Object=MibTableColumn
agentOspfv3LsdbAreaId=_AgentOspfv3LsdbAreaId_Object((1,3,6,1,4,1,7244,2,30,3,10,1,1),_AgentOspfv3LsdbAreaId_Type())
agentOspfv3LsdbAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3LsdbAreaId.setStatus(_A)
class _AgentOspfv3LsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_s,0),(_t,1),(_u,2),(_v,3),(_w,4),(_x,5),(_y,6),(_z,7),('link',8),(_A0,9),(_A1,10),(_A2,11)))
_AgentOspfv3LsdbType_Type.__name__=_C
_AgentOspfv3LsdbType_Object=MibTableColumn
agentOspfv3LsdbType=_AgentOspfv3LsdbType_Object((1,3,6,1,4,1,7244,2,30,3,10,1,2),_AgentOspfv3LsdbType_Type())
agentOspfv3LsdbType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3LsdbType.setStatus(_A)
_AgentOspfv3LsdbLsid_Type=IpAddress
_AgentOspfv3LsdbLsid_Object=MibTableColumn
agentOspfv3LsdbLsid=_AgentOspfv3LsdbLsid_Object((1,3,6,1,4,1,7244,2,30,3,10,1,3),_AgentOspfv3LsdbLsid_Type())
agentOspfv3LsdbLsid.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3LsdbLsid.setStatus(_A)
_AgentOspfv3LsdbRouterId_Type=RouterID
_AgentOspfv3LsdbRouterId_Object=MibTableColumn
agentOspfv3LsdbRouterId=_AgentOspfv3LsdbRouterId_Object((1,3,6,1,4,1,7244,2,30,3,10,1,4),_AgentOspfv3LsdbRouterId_Type())
agentOspfv3LsdbRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3LsdbRouterId.setStatus(_A)
_AgentOspfv3LsdbSequence_Type=Unsigned32
_AgentOspfv3LsdbSequence_Object=MibTableColumn
agentOspfv3LsdbSequence=_AgentOspfv3LsdbSequence_Object((1,3,6,1,4,1,7244,2,30,3,10,1,5),_AgentOspfv3LsdbSequence_Type())
agentOspfv3LsdbSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3LsdbSequence.setStatus(_A)
class _AgentOspfv3LsdbAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentOspfv3LsdbAge_Type.__name__=_C
_AgentOspfv3LsdbAge_Object=MibTableColumn
agentOspfv3LsdbAge=_AgentOspfv3LsdbAge_Object((1,3,6,1,4,1,7244,2,30,3,10,1,6),_AgentOspfv3LsdbAge_Type())
agentOspfv3LsdbAge.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3LsdbAge.setStatus(_A)
_AgentOspfv3LsdbChecksum_Type=Unsigned32
_AgentOspfv3LsdbChecksum_Object=MibTableColumn
agentOspfv3LsdbChecksum=_AgentOspfv3LsdbChecksum_Object((1,3,6,1,4,1,7244,2,30,3,10,1,7),_AgentOspfv3LsdbChecksum_Type())
agentOspfv3LsdbChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3LsdbChecksum.setStatus(_A)
_AgentOspfv3LsdbAdvertisement_Type=DisplayString
_AgentOspfv3LsdbAdvertisement_Object=MibTableColumn
agentOspfv3LsdbAdvertisement=_AgentOspfv3LsdbAdvertisement_Object((1,3,6,1,4,1,7244,2,30,3,10,1,8),_AgentOspfv3LsdbAdvertisement_Type())
agentOspfv3LsdbAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3LsdbAdvertisement.setStatus(_A)
class _AgentOspfv3AutoCostRefBw_Type(AutoCostRefBw):defaultValue=100
_AgentOspfv3AutoCostRefBw_Type.__name__=_A3
_AgentOspfv3AutoCostRefBw_Object=MibScalar
agentOspfv3AutoCostRefBw=_AgentOspfv3AutoCostRefBw_Object((1,3,6,1,4,1,7244,2,30,3,14),_AgentOspfv3AutoCostRefBw_Type())
agentOspfv3AutoCostRefBw.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3AutoCostRefBw.setStatus(_A)
_AgentOspfv3AsLsdbTable_Object=MibTable
agentOspfv3AsLsdbTable=_AgentOspfv3AsLsdbTable_Object((1,3,6,1,4,1,7244,2,30,3,18))
if mibBuilder.loadTexts:agentOspfv3AsLsdbTable.setStatus(_A)
_AgentOspfv3AsLsdbEntry_Object=MibTableRow
agentOspfv3AsLsdbEntry=_AgentOspfv3AsLsdbEntry_Object((1,3,6,1,4,1,7244,2,30,3,18,1))
agentOspfv3AsLsdbEntry.setIndexNames((0,_E,_A4),(0,_E,_A5),(0,_E,_A6))
if mibBuilder.loadTexts:agentOspfv3AsLsdbEntry.setStatus(_A)
class _AgentOspfv3AsLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_s,0),(_t,1),(_u,2),(_v,3),(_w,4),(_x,5),(_y,6),(_z,7),('link',8),(_A0,9),(_A1,10),(_A2,11)))
_AgentOspfv3AsLsdbType_Type.__name__=_C
_AgentOspfv3AsLsdbType_Object=MibTableColumn
agentOspfv3AsLsdbType=_AgentOspfv3AsLsdbType_Object((1,3,6,1,4,1,7244,2,30,3,18,1,1),_AgentOspfv3AsLsdbType_Type())
agentOspfv3AsLsdbType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3AsLsdbType.setStatus(_A)
_AgentOspfv3AsLsdbLsid_Type=IpAddress
_AgentOspfv3AsLsdbLsid_Object=MibTableColumn
agentOspfv3AsLsdbLsid=_AgentOspfv3AsLsdbLsid_Object((1,3,6,1,4,1,7244,2,30,3,18,1,2),_AgentOspfv3AsLsdbLsid_Type())
agentOspfv3AsLsdbLsid.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3AsLsdbLsid.setStatus(_A)
_AgentOspfv3AsLsdbRouterId_Type=RouterID
_AgentOspfv3AsLsdbRouterId_Object=MibTableColumn
agentOspfv3AsLsdbRouterId=_AgentOspfv3AsLsdbRouterId_Object((1,3,6,1,4,1,7244,2,30,3,18,1,3),_AgentOspfv3AsLsdbRouterId_Type())
agentOspfv3AsLsdbRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3AsLsdbRouterId.setStatus(_A)
_AgentOspfv3AsLsdbSequence_Type=Unsigned32
_AgentOspfv3AsLsdbSequence_Object=MibTableColumn
agentOspfv3AsLsdbSequence=_AgentOspfv3AsLsdbSequence_Object((1,3,6,1,4,1,7244,2,30,3,18,1,4),_AgentOspfv3AsLsdbSequence_Type())
agentOspfv3AsLsdbSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3AsLsdbSequence.setStatus(_A)
class _AgentOspfv3AsLsdbAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentOspfv3AsLsdbAge_Type.__name__=_C
_AgentOspfv3AsLsdbAge_Object=MibTableColumn
agentOspfv3AsLsdbAge=_AgentOspfv3AsLsdbAge_Object((1,3,6,1,4,1,7244,2,30,3,18,1,5),_AgentOspfv3AsLsdbAge_Type())
agentOspfv3AsLsdbAge.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3AsLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:agentOspfv3AsLsdbAge.setUnits(_O)
class _AgentOspfv3AsLsdbChecksum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentOspfv3AsLsdbChecksum_Type.__name__=_C
_AgentOspfv3AsLsdbChecksum_Object=MibTableColumn
agentOspfv3AsLsdbChecksum=_AgentOspfv3AsLsdbChecksum_Object((1,3,6,1,4,1,7244,2,30,3,18,1,6),_AgentOspfv3AsLsdbChecksum_Type())
agentOspfv3AsLsdbChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3AsLsdbChecksum.setStatus(_A)
class _AgentOspfv3AsLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_AgentOspfv3AsLsdbAdvertisement_Type.__name__=_L
_AgentOspfv3AsLsdbAdvertisement_Object=MibTableColumn
agentOspfv3AsLsdbAdvertisement=_AgentOspfv3AsLsdbAdvertisement_Object((1,3,6,1,4,1,7244,2,30,3,18,1,7),_AgentOspfv3AsLsdbAdvertisement_Type())
agentOspfv3AsLsdbAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:agentOspfv3AsLsdbAdvertisement.setStatus(_A)
class _AgentOspfv3DefaultPassiveMode_Type(TruthValue):defaultValue=2
_AgentOspfv3DefaultPassiveMode_Type.__name__=_I
_AgentOspfv3DefaultPassiveMode_Object=MibScalar
agentOspfv3DefaultPassiveMode=_AgentOspfv3DefaultPassiveMode_Object((1,3,6,1,4,1,7244,2,30,3,19),_AgentOspfv3DefaultPassiveMode_Type())
agentOspfv3DefaultPassiveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfv3DefaultPassiveMode.setStatus(_A)
ospfv3IfEntry.registerAugmentions((_E,_A7))
agentOspfv3IfEntry.setIndexNames(*ospfv3IfEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'SpfTimerRange':SpfTimerRange,_A3:AutoCostRefBw,'routingIpv6':routingIpv6,'agentIpv6Group':agentIpv6Group,'agentIpv6RoutingMode':agentIpv6RoutingMode,'agentIpv6InterfaceTable':agentIpv6InterfaceTable,'agentIpv6InterfaceEntry':agentIpv6InterfaceEntry,_K:agentIpv6InterfaceIfIndex,'agentIpv6InterfaceMtuValue':agentIpv6InterfaceMtuValue,'agentIpv6InterfaceDadTransmits':agentIpv6InterfaceDadTransmits,'agentIpv6InterfaceLinkLocalOnly':agentIpv6InterfaceLinkLocalOnly,'agentIpv6InterfaceIcmpUnreachables':agentIpv6InterfaceIcmpUnreachables,'agentIpv6InterfaceAutoconfig':agentIpv6InterfaceAutoconfig,'agentIpv6InterfaceDhcpClient':agentIpv6InterfaceDhcpClient,'agentIpv6RouterAdvertisementTable':agentIpv6RouterAdvertisementTable,'agentIpv6RouterAdvertisementEntry':agentIpv6RouterAdvertisementEntry,_Q:agentIpv6RouterAdvertisementIfIndex,'agentIpv6RouterAdvertisementSuppressMode':agentIpv6RouterAdvertisementSuppressMode,'agentIpv6RouterAdvertisementMaxAdvertisementInterval':agentIpv6RouterAdvertisementMaxAdvertisementInterval,'agentIpv6RouterAdvertisementMinAdvertisementInterval':agentIpv6RouterAdvertisementMinAdvertisementInterval,'agentIpv6RouterAdvertisementAdvertisementLifetime':agentIpv6RouterAdvertisementAdvertisementLifetime,'agentIpv6RouterAdvertisementNbrSolicitInterval':agentIpv6RouterAdvertisementNbrSolicitInterval,'agentIpv6RouterAdvertisementReachableTime':agentIpv6RouterAdvertisementReachableTime,'agentIpv6RouterAdvertisementManagedFlag':agentIpv6RouterAdvertisementManagedFlag,'agentIpv6RouterAdvertisementOtherFlag':agentIpv6RouterAdvertisementOtherFlag,'agentIpv6AddrPrefixTable':agentIpv6AddrPrefixTable,'agentIpv6AddrPrefixEntry':agentIpv6AddrPrefixEntry,_R:agentIpv6AddrPrefix,_S:agentIpv6AddrPrefixLength,'agentIpv6AddrPrefixOnLinkFlag':agentIpv6AddrPrefixOnLinkFlag,'agentIpv6AddrPrefixAutonomousFlag':agentIpv6AddrPrefixAutonomousFlag,'agentIpv6AddrPrefixAdvPreferredLifetime':agentIpv6AddrPrefixAdvPreferredLifetime,'agentIpv6AddrPrefixAdvValidLifetime':agentIpv6AddrPrefixAdvValidLifetime,'agentIpv6AddrTable':agentIpv6AddrTable,'agentIpv6AddrEntry':agentIpv6AddrEntry,_T:agentIpv6AddrAddress,'agentIpv6AddrPfxLength':agentIpv6AddrPfxLength,'agentIpv6AddrEui64Flag':agentIpv6AddrEui64Flag,'agentIpv6AddrStatus':agentIpv6AddrStatus,'agentIpv6StaticRouteTable':agentIpv6StaticRouteTable,'agentIpv6StaticRouteEntry':agentIpv6StaticRouteEntry,_U:agentIpv6StaticRouteDest,_V:agentIpv6StaticRoutePfxLength,_W:agentIpv6StaticRouteIfIndex,_X:agentIpv6StaticRouteNextHop,'agentIpv6StaticRoutePreference':agentIpv6StaticRoutePreference,'agentIpv6StaticRouteStatus':agentIpv6StaticRouteStatus,'agentIpv6ServicePortGroup':agentIpv6ServicePortGroup,'agentIpv6ServicePortPrefixTable':agentIpv6ServicePortPrefixTable,'agentIpv6ServicePortPrefixEntry':agentIpv6ServicePortPrefixEntry,_Y:agentIpv6ServicePortPrefixIndex,'agentIpv6ServicePortPrefix':agentIpv6ServicePortPrefix,'agentIpv6ServicePortPrefixLength':agentIpv6ServicePortPrefixLength,'agentIpv6ServicePortDefaultRouterTable':agentIpv6ServicePortDefaultRouterTable,'agentIpv6ServicePortDefaultRouterEntry':agentIpv6ServicePortDefaultRouterEntry,_Z:agentIpv6ServicePortDefaultRouterIndex,'agentIpv6ServicePortDefaultRouter':agentIpv6ServicePortDefaultRouter,'agentIpv6ServicePortNbrTable':agentIpv6ServicePortNbrTable,'agentIpv6ServicePortNbrEntry':agentIpv6ServicePortNbrEntry,_a:agentIpv6ServicePortNbrAddr,'agentIpv6ServicePortNbrPhysAddr':agentIpv6ServicePortNbrPhysAddr,'agentIpv6ServicePortNbrState':agentIpv6ServicePortNbrState,'agentIpv6ServicePortNbrUpdated':agentIpv6ServicePortNbrUpdated,'agentIpv6ServicePortNbrIsRouter':agentIpv6ServicePortNbrIsRouter,'agentIpv6ServicePortConfigProtocol':agentIpv6ServicePortConfigProtocol,'agentIpv6ServicePortDhcpRestart':agentIpv6ServicePortDhcpRestart,'agentIpv6NeighborGroup':agentIpv6NeighborGroup,'agentIpv6NeighborTable':agentIpv6NeighborTable,'agentIpv6NeighborEntry':agentIpv6NeighborEntry,_d:agentIpv6NeighborIfIndex,_e:agentIpv6NeighborAddress,'agentIpv6NeighborMacAddress':agentIpv6NeighborMacAddress,'agentIpv6NeighborIsRouter':agentIpv6NeighborIsRouter,'agentIpv6NeighborState':agentIpv6NeighborState,'agentIpv6NeighborLastUpdated':agentIpv6NeighborLastUpdated,'agentIpv6StaticNeighbor':agentIpv6StaticNeighbor,'agentIpv6StaticNeighborEntry':agentIpv6StaticNeighborEntry,_f:agentIpv6StaticNeighborIfIndex,'agentIpv6StaticNeighborAddress':agentIpv6StaticNeighborAddress,'agentIpv6StaticNeighborMacAddress':agentIpv6StaticNeighborMacAddress,'agentIpv6StaticNeighborRowAddress':agentIpv6StaticNeighborRowAddress,'agentIpv6StaticNeighborRowMacAddress':agentIpv6StaticNeighborRowMacAddress,'agentIpv6StaticNeighborRowStatus':agentIpv6StaticNeighborRowStatus,'agentIpv6IcmpControlGroup':agentIpv6IcmpControlGroup,'agentIpv6IcmpRateLimitInterval':agentIpv6IcmpRateLimitInterval,'agentIpv6IcmpRateLimitBurstSize':agentIpv6IcmpRateLimitBurstSize,'agentDhcp6ClientParametersTable':agentDhcp6ClientParametersTable,'agentDhcp6ClientParametersEntry':agentDhcp6ClientParametersEntry,_g:agentDhcp6ClientInterfaceIndex,'agentDhcp6ClientPrefix':agentDhcp6ClientPrefix,'agentDhcp6ClientPrefixlength':agentDhcp6ClientPrefixlength,'agentDhcp6ClientState':agentDhcp6ClientState,'agentDhcp6ClientServerDUID':agentDhcp6ClientServerDUID,'agentDhcp6ClientT1Time':agentDhcp6ClientT1Time,'agentDhcp6ClientT2Time':agentDhcp6ClientT2Time,'agentDhcp6ClientIAID':agentDhcp6ClientIAID,'agentDhcp6ClientPreferredLifeTime':agentDhcp6ClientPreferredLifeTime,'agentDhcp6ClientValidLifeTime':agentDhcp6ClientValidLifeTime,'agentDhcp6ClientRenewTime':agentDhcp6ClientRenewTime,'agentDhcp6ClientExpireTime':agentDhcp6ClientExpireTime,'agentRouterRipngConfigGroup':agentRouterRipngConfigGroup,'agentRouterRipngAdminState':agentRouterRipngAdminState,'agentRouterRipngSplitHorizonMode':agentRouterRipngSplitHorizonMode,'agentRouterRipngDefaultMetric':agentRouterRipngDefaultMetric,'agentRouterRipngDefaultMetricConfigured':agentRouterRipngDefaultMetricConfigured,'agentRouterRipngDefaultInfoOriginate':agentRouterRipngDefaultInfoOriginate,'agentRouterRipngDistance':agentRouterRipngDistance,'agentRipngRouteRedistTable':agentRipngRouteRedistTable,'agentRipngRouteRedistEntry':agentRipngRouteRedistEntry,_h:agentRipngRouteRedistSource,'agentRipngRouteRedistMode':agentRipngRouteRedistMode,'agentRipngRouteRedistMetric':agentRipngRouteRedistMetric,'agentRipngRouteRedistMetricConfigured':agentRipngRouteRedistMetricConfigured,'agentRouterRipngUpdateTime':agentRouterRipngUpdateTime,'agentRouterRipngGarbageTime':agentRouterRipngGarbageTime,'agentRouterRipngTimeoutTime':agentRouterRipngTimeoutTime,'agentRipngIfTable':agentRipngIfTable,'agentRipngIfEntry':agentRipngIfEntry,_k:agentRipngIfIndex,'agentRipngIfAdminMode':agentRipngIfAdminMode,'agentRipngIfPassiveMode':agentRipngIfPassiveMode,'agentRouterOspfv3ConfigGroup':agentRouterOspfv3ConfigGroup,'agentOspfv3DefaultMetric':agentOspfv3DefaultMetric,'agentOspfv3DefaultMetricConfigured':agentOspfv3DefaultMetricConfigured,'agentOspfv3DefaultInfoOriginate':agentOspfv3DefaultInfoOriginate,'agentOspfv3DefaultInfoOriginateAlways':agentOspfv3DefaultInfoOriginateAlways,'agentOspfv3DefaultInfoOriginateMetric':agentOspfv3DefaultInfoOriginateMetric,'agentOspfv3DefaultInfoOriginateMetricConfigured':agentOspfv3DefaultInfoOriginateMetricConfigured,'agentOspfv3DefaultInfoOriginateMetricType':agentOspfv3DefaultInfoOriginateMetricType,'agentOspfv3RouteRedistTable':agentOspfv3RouteRedistTable,'agentOspfv3RouteRedistEntry':agentOspfv3RouteRedistEntry,_n:agentOspfv3RouteRedistSource,'agentOspfv3RouteRedistMode':agentOspfv3RouteRedistMode,'agentOspfv3RouteRedistMetric':agentOspfv3RouteRedistMetric,'agentOspfv3RouteRedistMetricConfigured':agentOspfv3RouteRedistMetricConfigured,'agentOspfv3RouteRedistMetricType':agentOspfv3RouteRedistMetricType,'agentOspfv3RouteRedistTag':agentOspfv3RouteRedistTag,'agentOspfv3IfTable':agentOspfv3IfTable,_A7:agentOspfv3IfEntry,'agentOspfv3IfIpMtuIgnoreFlag':agentOspfv3IfIpMtuIgnoreFlag,'agentOspfv3IfPassiveMode':agentOspfv3IfPassiveMode,'agentOspfv3LsdbTable':agentOspfv3LsdbTable,'agentOspfv3LsdbEntry':agentOspfv3LsdbEntry,_o:agentOspfv3LsdbAreaId,_p:agentOspfv3LsdbType,_q:agentOspfv3LsdbLsid,_r:agentOspfv3LsdbRouterId,'agentOspfv3LsdbSequence':agentOspfv3LsdbSequence,'agentOspfv3LsdbAge':agentOspfv3LsdbAge,'agentOspfv3LsdbChecksum':agentOspfv3LsdbChecksum,'agentOspfv3LsdbAdvertisement':agentOspfv3LsdbAdvertisement,'agentOspfv3AutoCostRefBw':agentOspfv3AutoCostRefBw,'agentOspfv3AsLsdbTable':agentOspfv3AsLsdbTable,'agentOspfv3AsLsdbEntry':agentOspfv3AsLsdbEntry,_A4:agentOspfv3AsLsdbType,_A5:agentOspfv3AsLsdbLsid,_A6:agentOspfv3AsLsdbRouterId,'agentOspfv3AsLsdbSequence':agentOspfv3AsLsdbSequence,'agentOspfv3AsLsdbAge':agentOspfv3AsLsdbAge,'agentOspfv3AsLsdbChecksum':agentOspfv3AsLsdbChecksum,'agentOspfv3AsLsdbAdvertisement':agentOspfv3AsLsdbAdvertisement,'agentOspfv3DefaultPassiveMode':agentOspfv3DefaultPassiveMode})