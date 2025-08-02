_j='agentIpv6NbrCfgAddr'
_i='agentIpv6IfIndex'
_h='agentIpv6NetworkPortNbrCfgAddr'
_g='agentIpv6NetworkPortNbrAddr'
_f='agentIpv6EcmpNextHopCount'
_e='agentDhcp6ClientInterfaceIndex'
_d='agentIpv6ServicePortNbrCfgAddr'
_c='static'
_b='dynamic'
_a='unknown'
_Z='reachable'
_Y='agentIpv6ServicePortNbrAddr'
_X='agentIpv6ServicePortDefaultRouterIndex'
_W='agentIpv6ServicePortPrefixIndex'
_V='agentIpv6StaticRouteNextHop'
_U='agentIpv6StaticRouteIfIndex'
_T='agentIpv6StaticRoutePfxLength'
_S='agentIpv6StaticRouteDest'
_R='agentIpv6AddrAddress'
_Q='seconds'
_P='agentIpv6AddrPrefixLength'
_O='agentIpv6AddrPrefix'
_N='agentIpv6RouterAdvertisementIfIndex'
_M='DisplayString'
_L='bits'
_K='Unsigned32'
_J='agentIpv6InterfaceIfIndex'
_I='read-create'
_H='disable'
_G='enable'
_F='not-accessible'
_E='LANCOM-ROUTING6-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,Ipv6AddressIfIdentifier,Ipv6AddressPrefix,Ipv6IfIndex,Ipv6IfIndexOrZero=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressIfIdentifier','Ipv6AddressPrefix','Ipv6IfIndex','Ipv6IfIndexOrZero')
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC',_M,'MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp','TruthValue','VariablePointer')
fastPathRoutingIpv6=ModuleIdentity((1,3,6,1,4,1,2356,16,1,30))
if mibBuilder.loadTexts:fastPathRoutingIpv6.setRevisions(('2011-01-26 00:00','2007-05-23 00:00','2005-09-21 17:00'))
_AgentIpv6Group_ObjectIdentity=ObjectIdentity
agentIpv6Group=_AgentIpv6Group_ObjectIdentity((1,3,6,1,4,1,2356,16,1,30,1))
class _AgentIpv6RoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6RoutingMode_Type.__name__=_C
_AgentIpv6RoutingMode_Object=MibScalar
agentIpv6RoutingMode=_AgentIpv6RoutingMode_Object((1,3,6,1,4,1,2356,16,1,30,1,1),_AgentIpv6RoutingMode_Type())
agentIpv6RoutingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RoutingMode.setStatus(_A)
_AgentIpv6InterfaceTable_Object=MibTable
agentIpv6InterfaceTable=_AgentIpv6InterfaceTable_Object((1,3,6,1,4,1,2356,16,1,30,1,2))
if mibBuilder.loadTexts:agentIpv6InterfaceTable.setStatus(_A)
_AgentIpv6InterfaceEntry_Object=MibTableRow
agentIpv6InterfaceEntry=_AgentIpv6InterfaceEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,2,1))
agentIpv6InterfaceEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:agentIpv6InterfaceEntry.setStatus(_A)
class _AgentIpv6InterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIpv6InterfaceIfIndex_Type.__name__=_C
_AgentIpv6InterfaceIfIndex_Object=MibTableColumn
agentIpv6InterfaceIfIndex=_AgentIpv6InterfaceIfIndex_Object((1,3,6,1,4,1,2356,16,1,30,1,2,1,1),_AgentIpv6InterfaceIfIndex_Type())
agentIpv6InterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6InterfaceIfIndex.setStatus(_A)
class _AgentIpv6InterfaceMtuValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1280,9198))
_AgentIpv6InterfaceMtuValue_Type.__name__=_K
_AgentIpv6InterfaceMtuValue_Object=MibTableColumn
agentIpv6InterfaceMtuValue=_AgentIpv6InterfaceMtuValue_Object((1,3,6,1,4,1,2356,16,1,30,1,2,1,2),_AgentIpv6InterfaceMtuValue_Type())
agentIpv6InterfaceMtuValue.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6InterfaceMtuValue.setStatus(_A)
class _AgentIpv6InterfaceDadTransmits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AgentIpv6InterfaceDadTransmits_Type.__name__=_C
_AgentIpv6InterfaceDadTransmits_Object=MibTableColumn
agentIpv6InterfaceDadTransmits=_AgentIpv6InterfaceDadTransmits_Object((1,3,6,1,4,1,2356,16,1,30,1,2,1,3),_AgentIpv6InterfaceDadTransmits_Type())
agentIpv6InterfaceDadTransmits.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6InterfaceDadTransmits.setStatus(_A)
class _AgentIpv6InterfaceLinkLocalOnly_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6InterfaceLinkLocalOnly_Type.__name__=_C
_AgentIpv6InterfaceLinkLocalOnly_Object=MibTableColumn
agentIpv6InterfaceLinkLocalOnly=_AgentIpv6InterfaceLinkLocalOnly_Object((1,3,6,1,4,1,2356,16,1,30,1,2,1,4),_AgentIpv6InterfaceLinkLocalOnly_Type())
agentIpv6InterfaceLinkLocalOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6InterfaceLinkLocalOnly.setStatus(_A)
class _AgentIpv6InterfaceIcmpUnreachables_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6InterfaceIcmpUnreachables_Type.__name__=_C
_AgentIpv6InterfaceIcmpUnreachables_Object=MibTableColumn
agentIpv6InterfaceIcmpUnreachables=_AgentIpv6InterfaceIcmpUnreachables_Object((1,3,6,1,4,1,2356,16,1,30,1,2,1,5),_AgentIpv6InterfaceIcmpUnreachables_Type())
agentIpv6InterfaceIcmpUnreachables.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6InterfaceIcmpUnreachables.setStatus(_A)
class _AgentIpv6InterfaceAutoconfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6InterfaceAutoconfig_Type.__name__=_C
_AgentIpv6InterfaceAutoconfig_Object=MibTableColumn
agentIpv6InterfaceAutoconfig=_AgentIpv6InterfaceAutoconfig_Object((1,3,6,1,4,1,2356,16,1,30,1,2,1,6),_AgentIpv6InterfaceAutoconfig_Type())
agentIpv6InterfaceAutoconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6InterfaceAutoconfig.setStatus(_A)
class _AgentIpv6InterfaceDhcpClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6InterfaceDhcpClient_Type.__name__=_C
_AgentIpv6InterfaceDhcpClient_Object=MibTableColumn
agentIpv6InterfaceDhcpClient=_AgentIpv6InterfaceDhcpClient_Object((1,3,6,1,4,1,2356,16,1,30,1,2,1,7),_AgentIpv6InterfaceDhcpClient_Type())
agentIpv6InterfaceDhcpClient.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6InterfaceDhcpClient.setStatus(_A)
class _AgentIpv6InterfaceIcmpRedirects_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6InterfaceIcmpRedirects_Type.__name__=_C
_AgentIpv6InterfaceIcmpRedirects_Object=MibTableColumn
agentIpv6InterfaceIcmpRedirects=_AgentIpv6InterfaceIcmpRedirects_Object((1,3,6,1,4,1,2356,16,1,30,1,2,1,8),_AgentIpv6InterfaceIcmpRedirects_Type())
agentIpv6InterfaceIcmpRedirects.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6InterfaceIcmpRedirects.setStatus(_A)
_AgentIpv6RouterAdvertisementTable_Object=MibTable
agentIpv6RouterAdvertisementTable=_AgentIpv6RouterAdvertisementTable_Object((1,3,6,1,4,1,2356,16,1,30,1,3))
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementTable.setStatus(_A)
_AgentIpv6RouterAdvertisementEntry_Object=MibTableRow
agentIpv6RouterAdvertisementEntry=_AgentIpv6RouterAdvertisementEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1))
agentIpv6RouterAdvertisementEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementEntry.setStatus(_A)
class _AgentIpv6RouterAdvertisementIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIpv6RouterAdvertisementIfIndex_Type.__name__=_C
_AgentIpv6RouterAdvertisementIfIndex_Object=MibTableColumn
agentIpv6RouterAdvertisementIfIndex=_AgentIpv6RouterAdvertisementIfIndex_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1,1),_AgentIpv6RouterAdvertisementIfIndex_Type())
agentIpv6RouterAdvertisementIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementIfIndex.setStatus(_A)
class _AgentIpv6RouterAdvertisementSuppressMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6RouterAdvertisementSuppressMode_Type.__name__=_C
_AgentIpv6RouterAdvertisementSuppressMode_Object=MibTableColumn
agentIpv6RouterAdvertisementSuppressMode=_AgentIpv6RouterAdvertisementSuppressMode_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1,2),_AgentIpv6RouterAdvertisementSuppressMode_Type())
agentIpv6RouterAdvertisementSuppressMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementSuppressMode.setStatus(_A)
class _AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type.__name__=_C
_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Object=MibTableColumn
agentIpv6RouterAdvertisementMaxAdvertisementInterval=_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1,3),_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type())
agentIpv6RouterAdvertisementMaxAdvertisementInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementMaxAdvertisementInterval.setStatus(_A)
class _AgentIpv6RouterAdvertisementAdvertisementLifetime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,65520))
_AgentIpv6RouterAdvertisementAdvertisementLifetime_Type.__name__=_C
_AgentIpv6RouterAdvertisementAdvertisementLifetime_Object=MibTableColumn
agentIpv6RouterAdvertisementAdvertisementLifetime=_AgentIpv6RouterAdvertisementAdvertisementLifetime_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1,4),_AgentIpv6RouterAdvertisementAdvertisementLifetime_Type())
agentIpv6RouterAdvertisementAdvertisementLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementAdvertisementLifetime.setStatus(_A)
class _AgentIpv6RouterAdvertisementNbrSolicitInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_AgentIpv6RouterAdvertisementNbrSolicitInterval_Type.__name__=_C
_AgentIpv6RouterAdvertisementNbrSolicitInterval_Object=MibTableColumn
agentIpv6RouterAdvertisementNbrSolicitInterval=_AgentIpv6RouterAdvertisementNbrSolicitInterval_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1,5),_AgentIpv6RouterAdvertisementNbrSolicitInterval_Type())
agentIpv6RouterAdvertisementNbrSolicitInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementNbrSolicitInterval.setStatus(_A)
class _AgentIpv6RouterAdvertisementReachableTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_AgentIpv6RouterAdvertisementReachableTime_Type.__name__=_C
_AgentIpv6RouterAdvertisementReachableTime_Object=MibTableColumn
agentIpv6RouterAdvertisementReachableTime=_AgentIpv6RouterAdvertisementReachableTime_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1,6),_AgentIpv6RouterAdvertisementReachableTime_Type())
agentIpv6RouterAdvertisementReachableTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementReachableTime.setStatus(_A)
class _AgentIpv6RouterAdvertisementManagedFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6RouterAdvertisementManagedFlag_Type.__name__=_C
_AgentIpv6RouterAdvertisementManagedFlag_Object=MibTableColumn
agentIpv6RouterAdvertisementManagedFlag=_AgentIpv6RouterAdvertisementManagedFlag_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1,7),_AgentIpv6RouterAdvertisementManagedFlag_Type())
agentIpv6RouterAdvertisementManagedFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementManagedFlag.setStatus(_A)
class _AgentIpv6RouterAdvertisementOtherFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6RouterAdvertisementOtherFlag_Type.__name__=_C
_AgentIpv6RouterAdvertisementOtherFlag_Object=MibTableColumn
agentIpv6RouterAdvertisementOtherFlag=_AgentIpv6RouterAdvertisementOtherFlag_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1,8),_AgentIpv6RouterAdvertisementOtherFlag_Type())
agentIpv6RouterAdvertisementOtherFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementOtherFlag.setStatus(_A)
class _AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Type.__name__=_C
_AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Object=MibTableColumn
agentIpv6RouterAdvertisementHopLimitUnspecifiedMode=_AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Object((1,3,6,1,4,1,2356,16,1,30,1,3,1,9),_AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Type())
agentIpv6RouterAdvertisementHopLimitUnspecifiedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementHopLimitUnspecifiedMode.setStatus(_A)
_AgentIpv6AddrPrefixTable_Object=MibTable
agentIpv6AddrPrefixTable=_AgentIpv6AddrPrefixTable_Object((1,3,6,1,4,1,2356,16,1,30,1,4))
if mibBuilder.loadTexts:agentIpv6AddrPrefixTable.setStatus(_A)
_AgentIpv6AddrPrefixEntry_Object=MibTableRow
agentIpv6AddrPrefixEntry=_AgentIpv6AddrPrefixEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,4,1))
agentIpv6AddrPrefixEntry.setIndexNames((0,_E,_J),(0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:agentIpv6AddrPrefixEntry.setStatus(_A)
_AgentIpv6AddrPrefix_Type=Ipv6AddressPrefix
_AgentIpv6AddrPrefix_Object=MibTableColumn
agentIpv6AddrPrefix=_AgentIpv6AddrPrefix_Object((1,3,6,1,4,1,2356,16,1,30,1,4,1,1),_AgentIpv6AddrPrefix_Type())
agentIpv6AddrPrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6AddrPrefix.setStatus(_A)
class _AgentIpv6AddrPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6AddrPrefixLength_Type.__name__=_C
_AgentIpv6AddrPrefixLength_Object=MibTableColumn
agentIpv6AddrPrefixLength=_AgentIpv6AddrPrefixLength_Object((1,3,6,1,4,1,2356,16,1,30,1,4,1,2),_AgentIpv6AddrPrefixLength_Type())
agentIpv6AddrPrefixLength.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6AddrPrefixLength.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPrefixLength.setUnits(_L)
_AgentIpv6AddrPrefixOnLinkFlag_Type=TruthValue
_AgentIpv6AddrPrefixOnLinkFlag_Object=MibTableColumn
agentIpv6AddrPrefixOnLinkFlag=_AgentIpv6AddrPrefixOnLinkFlag_Object((1,3,6,1,4,1,2356,16,1,30,1,4,1,3),_AgentIpv6AddrPrefixOnLinkFlag_Type())
agentIpv6AddrPrefixOnLinkFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6AddrPrefixOnLinkFlag.setStatus(_A)
_AgentIpv6AddrPrefixAutonomousFlag_Type=TruthValue
_AgentIpv6AddrPrefixAutonomousFlag_Object=MibTableColumn
agentIpv6AddrPrefixAutonomousFlag=_AgentIpv6AddrPrefixAutonomousFlag_Object((1,3,6,1,4,1,2356,16,1,30,1,4,1,4),_AgentIpv6AddrPrefixAutonomousFlag_Type())
agentIpv6AddrPrefixAutonomousFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAutonomousFlag.setStatus(_A)
_AgentIpv6AddrPrefixAdvPreferredLifetime_Type=Unsigned32
_AgentIpv6AddrPrefixAdvPreferredLifetime_Object=MibTableColumn
agentIpv6AddrPrefixAdvPreferredLifetime=_AgentIpv6AddrPrefixAdvPreferredLifetime_Object((1,3,6,1,4,1,2356,16,1,30,1,4,1,5),_AgentIpv6AddrPrefixAdvPreferredLifetime_Type())
agentIpv6AddrPrefixAdvPreferredLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvPreferredLifetime.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvPreferredLifetime.setUnits(_Q)
_AgentIpv6AddrPrefixAdvValidLifetime_Type=Unsigned32
_AgentIpv6AddrPrefixAdvValidLifetime_Object=MibTableColumn
agentIpv6AddrPrefixAdvValidLifetime=_AgentIpv6AddrPrefixAdvValidLifetime_Object((1,3,6,1,4,1,2356,16,1,30,1,4,1,6),_AgentIpv6AddrPrefixAdvValidLifetime_Type())
agentIpv6AddrPrefixAdvValidLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvValidLifetime.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvValidLifetime.setUnits(_Q)
_AgentIpv6AddrTable_Object=MibTable
agentIpv6AddrTable=_AgentIpv6AddrTable_Object((1,3,6,1,4,1,2356,16,1,30,1,5))
if mibBuilder.loadTexts:agentIpv6AddrTable.setStatus(_A)
_AgentIpv6AddrEntry_Object=MibTableRow
agentIpv6AddrEntry=_AgentIpv6AddrEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,5,1))
agentIpv6AddrEntry.setIndexNames((0,_E,_J),(0,_E,_R))
if mibBuilder.loadTexts:agentIpv6AddrEntry.setStatus(_A)
_AgentIpv6AddrAddress_Type=Ipv6Address
_AgentIpv6AddrAddress_Object=MibTableColumn
agentIpv6AddrAddress=_AgentIpv6AddrAddress_Object((1,3,6,1,4,1,2356,16,1,30,1,5,1,1),_AgentIpv6AddrAddress_Type())
agentIpv6AddrAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6AddrAddress.setStatus(_A)
class _AgentIpv6AddrPfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6AddrPfxLength_Type.__name__=_C
_AgentIpv6AddrPfxLength_Object=MibTableColumn
agentIpv6AddrPfxLength=_AgentIpv6AddrPfxLength_Object((1,3,6,1,4,1,2356,16,1,30,1,5,1,2),_AgentIpv6AddrPfxLength_Type())
agentIpv6AddrPfxLength.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6AddrPfxLength.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPfxLength.setUnits(_L)
_AgentIpv6AddrEui64Flag_Type=TruthValue
_AgentIpv6AddrEui64Flag_Object=MibTableColumn
agentIpv6AddrEui64Flag=_AgentIpv6AddrEui64Flag_Object((1,3,6,1,4,1,2356,16,1,30,1,5,1,3),_AgentIpv6AddrEui64Flag_Type())
agentIpv6AddrEui64Flag.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6AddrEui64Flag.setStatus(_A)
_AgentIpv6AddrStatus_Type=RowStatus
_AgentIpv6AddrStatus_Object=MibTableColumn
agentIpv6AddrStatus=_AgentIpv6AddrStatus_Object((1,3,6,1,4,1,2356,16,1,30,1,5,1,4),_AgentIpv6AddrStatus_Type())
agentIpv6AddrStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6AddrStatus.setStatus(_A)
_AgentIpv6StaticRouteTable_Object=MibTable
agentIpv6StaticRouteTable=_AgentIpv6StaticRouteTable_Object((1,3,6,1,4,1,2356,16,1,30,1,6))
if mibBuilder.loadTexts:agentIpv6StaticRouteTable.setStatus(_A)
_AgentIpv6StaticRouteEntry_Object=MibTableRow
agentIpv6StaticRouteEntry=_AgentIpv6StaticRouteEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,6,1))
agentIpv6StaticRouteEntry.setIndexNames((0,_E,_S),(0,_E,_T),(0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:agentIpv6StaticRouteEntry.setStatus(_A)
_AgentIpv6StaticRouteDest_Type=Ipv6AddressPrefix
_AgentIpv6StaticRouteDest_Object=MibTableColumn
agentIpv6StaticRouteDest=_AgentIpv6StaticRouteDest_Object((1,3,6,1,4,1,2356,16,1,30,1,6,1,1),_AgentIpv6StaticRouteDest_Type())
agentIpv6StaticRouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6StaticRouteDest.setStatus(_A)
class _AgentIpv6StaticRoutePfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6StaticRoutePfxLength_Type.__name__=_C
_AgentIpv6StaticRoutePfxLength_Object=MibTableColumn
agentIpv6StaticRoutePfxLength=_AgentIpv6StaticRoutePfxLength_Object((1,3,6,1,4,1,2356,16,1,30,1,6,1,2),_AgentIpv6StaticRoutePfxLength_Type())
agentIpv6StaticRoutePfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6StaticRoutePfxLength.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6StaticRoutePfxLength.setUnits(_L)
_AgentIpv6StaticRouteIfIndex_Type=Ipv6IfIndexOrZero
_AgentIpv6StaticRouteIfIndex_Object=MibTableColumn
agentIpv6StaticRouteIfIndex=_AgentIpv6StaticRouteIfIndex_Object((1,3,6,1,4,1,2356,16,1,30,1,6,1,3),_AgentIpv6StaticRouteIfIndex_Type())
agentIpv6StaticRouteIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6StaticRouteIfIndex.setStatus(_A)
_AgentIpv6StaticRouteNextHop_Type=Ipv6Address
_AgentIpv6StaticRouteNextHop_Object=MibTableColumn
agentIpv6StaticRouteNextHop=_AgentIpv6StaticRouteNextHop_Object((1,3,6,1,4,1,2356,16,1,30,1,6,1,4),_AgentIpv6StaticRouteNextHop_Type())
agentIpv6StaticRouteNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6StaticRouteNextHop.setStatus(_A)
class _AgentIpv6StaticRoutePreference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentIpv6StaticRoutePreference_Type.__name__=_C
_AgentIpv6StaticRoutePreference_Object=MibTableColumn
agentIpv6StaticRoutePreference=_AgentIpv6StaticRoutePreference_Object((1,3,6,1,4,1,2356,16,1,30,1,6,1,5),_AgentIpv6StaticRoutePreference_Type())
agentIpv6StaticRoutePreference.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6StaticRoutePreference.setStatus(_A)
_AgentIpv6StaticRouteStatus_Type=RowStatus
_AgentIpv6StaticRouteStatus_Object=MibTableColumn
agentIpv6StaticRouteStatus=_AgentIpv6StaticRouteStatus_Object((1,3,6,1,4,1,2356,16,1,30,1,6,1,6),_AgentIpv6StaticRouteStatus_Type())
agentIpv6StaticRouteStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6StaticRouteStatus.setStatus(_A)
_AgentIpv6ServicePortGroup_ObjectIdentity=ObjectIdentity
agentIpv6ServicePortGroup=_AgentIpv6ServicePortGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,30,1,7))
_AgentIpv6ServicePortPrefixTable_Object=MibTable
agentIpv6ServicePortPrefixTable=_AgentIpv6ServicePortPrefixTable_Object((1,3,6,1,4,1,2356,16,1,30,1,7,1))
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixTable.setStatus(_A)
_AgentIpv6ServicePortPrefixEntry_Object=MibTableRow
agentIpv6ServicePortPrefixEntry=_AgentIpv6ServicePortPrefixEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,7,1,1))
agentIpv6ServicePortPrefixEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixEntry.setStatus(_A)
_AgentIpv6ServicePortPrefixIndex_Type=Unsigned32
_AgentIpv6ServicePortPrefixIndex_Object=MibTableColumn
agentIpv6ServicePortPrefixIndex=_AgentIpv6ServicePortPrefixIndex_Object((1,3,6,1,4,1,2356,16,1,30,1,7,1,1,1),_AgentIpv6ServicePortPrefixIndex_Type())
agentIpv6ServicePortPrefixIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixIndex.setStatus(_A)
_AgentIpv6ServicePortPrefix_Type=Ipv6Address
_AgentIpv6ServicePortPrefix_Object=MibTableColumn
agentIpv6ServicePortPrefix=_AgentIpv6ServicePortPrefix_Object((1,3,6,1,4,1,2356,16,1,30,1,7,1,1,2),_AgentIpv6ServicePortPrefix_Type())
agentIpv6ServicePortPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortPrefix.setStatus(_A)
_AgentIpv6ServicePortPrefixLength_Type=Unsigned32
_AgentIpv6ServicePortPrefixLength_Object=MibTableColumn
agentIpv6ServicePortPrefixLength=_AgentIpv6ServicePortPrefixLength_Object((1,3,6,1,4,1,2356,16,1,30,1,7,1,1,3),_AgentIpv6ServicePortPrefixLength_Type())
agentIpv6ServicePortPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixLength.setStatus(_A)
_AgentIpv6ServicePortDefaultRouterTable_Object=MibTable
agentIpv6ServicePortDefaultRouterTable=_AgentIpv6ServicePortDefaultRouterTable_Object((1,3,6,1,4,1,2356,16,1,30,1,7,2))
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouterTable.setStatus(_A)
_AgentIpv6ServicePortDefaultRouterEntry_Object=MibTableRow
agentIpv6ServicePortDefaultRouterEntry=_AgentIpv6ServicePortDefaultRouterEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,7,2,1))
agentIpv6ServicePortDefaultRouterEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouterEntry.setStatus(_A)
_AgentIpv6ServicePortDefaultRouterIndex_Type=Unsigned32
_AgentIpv6ServicePortDefaultRouterIndex_Object=MibTableColumn
agentIpv6ServicePortDefaultRouterIndex=_AgentIpv6ServicePortDefaultRouterIndex_Object((1,3,6,1,4,1,2356,16,1,30,1,7,2,1,1),_AgentIpv6ServicePortDefaultRouterIndex_Type())
agentIpv6ServicePortDefaultRouterIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouterIndex.setStatus(_A)
_AgentIpv6ServicePortDefaultRouter_Type=Ipv6Address
_AgentIpv6ServicePortDefaultRouter_Object=MibTableColumn
agentIpv6ServicePortDefaultRouter=_AgentIpv6ServicePortDefaultRouter_Object((1,3,6,1,4,1,2356,16,1,30,1,7,2,1,2),_AgentIpv6ServicePortDefaultRouter_Type())
agentIpv6ServicePortDefaultRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouter.setStatus(_A)
_AgentIpv6ServicePortNbrTable_Object=MibTable
agentIpv6ServicePortNbrTable=_AgentIpv6ServicePortNbrTable_Object((1,3,6,1,4,1,2356,16,1,30,1,7,3))
if mibBuilder.loadTexts:agentIpv6ServicePortNbrTable.setStatus(_A)
_AgentIpv6ServicePortNbrEntry_Object=MibTableRow
agentIpv6ServicePortNbrEntry=_AgentIpv6ServicePortNbrEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,7,3,1))
agentIpv6ServicePortNbrEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:agentIpv6ServicePortNbrEntry.setStatus(_A)
_AgentIpv6ServicePortNbrAddr_Type=Ipv6Address
_AgentIpv6ServicePortNbrAddr_Object=MibTableColumn
agentIpv6ServicePortNbrAddr=_AgentIpv6ServicePortNbrAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,7,3,1,1),_AgentIpv6ServicePortNbrAddr_Type())
agentIpv6ServicePortNbrAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrAddr.setStatus(_A)
_AgentIpv6ServicePortNbrPhysAddr_Type=MacAddress
_AgentIpv6ServicePortNbrPhysAddr_Object=MibTableColumn
agentIpv6ServicePortNbrPhysAddr=_AgentIpv6ServicePortNbrPhysAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,7,3,1,2),_AgentIpv6ServicePortNbrPhysAddr_Type())
agentIpv6ServicePortNbrPhysAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrPhysAddr.setStatus(_A)
class _AgentIpv6ServicePortNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6)));namedValues=NamedValues(*((_Z,1),('stale',2),('delay',3),('probe',4),(_a,6)))
_AgentIpv6ServicePortNbrState_Type.__name__=_C
_AgentIpv6ServicePortNbrState_Object=MibTableColumn
agentIpv6ServicePortNbrState=_AgentIpv6ServicePortNbrState_Object((1,3,6,1,4,1,2356,16,1,30,1,7,3,1,3),_AgentIpv6ServicePortNbrState_Type())
agentIpv6ServicePortNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrState.setStatus(_A)
_AgentIpv6ServicePortNbrUpdated_Type=TimeStamp
_AgentIpv6ServicePortNbrUpdated_Object=MibTableColumn
agentIpv6ServicePortNbrUpdated=_AgentIpv6ServicePortNbrUpdated_Object((1,3,6,1,4,1,2356,16,1,30,1,7,3,1,4),_AgentIpv6ServicePortNbrUpdated_Type())
agentIpv6ServicePortNbrUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrUpdated.setStatus(_A)
_AgentIpv6ServicePortNbrIsRouter_Type=TruthValue
_AgentIpv6ServicePortNbrIsRouter_Object=MibTableColumn
agentIpv6ServicePortNbrIsRouter=_AgentIpv6ServicePortNbrIsRouter_Object((1,3,6,1,4,1,2356,16,1,30,1,7,3,1,5),_AgentIpv6ServicePortNbrIsRouter_Type())
agentIpv6ServicePortNbrIsRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrIsRouter.setStatus(_A)
class _AgentIpv6ServicePortNbrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_b,2),(_c,3),('local',4)))
_AgentIpv6ServicePortNbrType_Type.__name__=_C
_AgentIpv6ServicePortNbrType_Object=MibTableColumn
agentIpv6ServicePortNbrType=_AgentIpv6ServicePortNbrType_Object((1,3,6,1,4,1,2356,16,1,30,1,7,3,1,6),_AgentIpv6ServicePortNbrType_Type())
agentIpv6ServicePortNbrType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrType.setStatus(_A)
_AgentIpv6ServicePortNbrCfgTable_Object=MibTable
agentIpv6ServicePortNbrCfgTable=_AgentIpv6ServicePortNbrCfgTable_Object((1,3,6,1,4,1,2356,16,1,30,1,7,4))
if mibBuilder.loadTexts:agentIpv6ServicePortNbrCfgTable.setStatus(_A)
_AgentIpv6ServicePortNbrCfgEntry_Object=MibTableRow
agentIpv6ServicePortNbrCfgEntry=_AgentIpv6ServicePortNbrCfgEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,7,4,1))
agentIpv6ServicePortNbrCfgEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:agentIpv6ServicePortNbrCfgEntry.setStatus(_A)
_AgentIpv6ServicePortNbrCfgAddr_Type=Ipv6Address
_AgentIpv6ServicePortNbrCfgAddr_Object=MibTableColumn
agentIpv6ServicePortNbrCfgAddr=_AgentIpv6ServicePortNbrCfgAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,7,4,1,1),_AgentIpv6ServicePortNbrCfgAddr_Type())
agentIpv6ServicePortNbrCfgAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrCfgAddr.setStatus(_A)
_AgentIpv6ServicePortNbrCfgPhysAddr_Type=MacAddress
_AgentIpv6ServicePortNbrCfgPhysAddr_Object=MibTableColumn
agentIpv6ServicePortNbrCfgPhysAddr=_AgentIpv6ServicePortNbrCfgPhysAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,7,4,1,2),_AgentIpv6ServicePortNbrCfgPhysAddr_Type())
agentIpv6ServicePortNbrCfgPhysAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrCfgPhysAddr.setStatus(_A)
_AgentIpv6ServicePortNbrCfgEntryStatus_Type=RowStatus
_AgentIpv6ServicePortNbrCfgEntryStatus_Object=MibTableColumn
agentIpv6ServicePortNbrCfgEntryStatus=_AgentIpv6ServicePortNbrCfgEntryStatus_Object((1,3,6,1,4,1,2356,16,1,30,1,7,4,1,3),_AgentIpv6ServicePortNbrCfgEntryStatus_Type())
agentIpv6ServicePortNbrCfgEntryStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrCfgEntryStatus.setStatus(_A)
_AgentIpv6IcmpControlGroup_ObjectIdentity=ObjectIdentity
agentIpv6IcmpControlGroup=_AgentIpv6IcmpControlGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,30,1,8))
class _AgentIpv6IcmpRateLimitInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIpv6IcmpRateLimitInterval_Type.__name__=_C
_AgentIpv6IcmpRateLimitInterval_Object=MibScalar
agentIpv6IcmpRateLimitInterval=_AgentIpv6IcmpRateLimitInterval_Object((1,3,6,1,4,1,2356,16,1,30,1,8,1),_AgentIpv6IcmpRateLimitInterval_Type())
agentIpv6IcmpRateLimitInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6IcmpRateLimitInterval.setStatus(_A)
class _AgentIpv6IcmpRateLimitBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_AgentIpv6IcmpRateLimitBurstSize_Type.__name__=_C
_AgentIpv6IcmpRateLimitBurstSize_Object=MibScalar
agentIpv6IcmpRateLimitBurstSize=_AgentIpv6IcmpRateLimitBurstSize_Object((1,3,6,1,4,1,2356,16,1,30,1,8,2),_AgentIpv6IcmpRateLimitBurstSize_Type())
agentIpv6IcmpRateLimitBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6IcmpRateLimitBurstSize.setStatus(_A)
_AgentDhcp6ClientParametersTable_Object=MibTable
agentDhcp6ClientParametersTable=_AgentDhcp6ClientParametersTable_Object((1,3,6,1,4,1,2356,16,1,30,1,9))
if mibBuilder.loadTexts:agentDhcp6ClientParametersTable.setStatus(_A)
_AgentDhcp6ClientParametersEntry_Object=MibTableRow
agentDhcp6ClientParametersEntry=_AgentDhcp6ClientParametersEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1))
agentDhcp6ClientParametersEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:agentDhcp6ClientParametersEntry.setStatus(_A)
_AgentDhcp6ClientInterfaceIndex_Type=Unsigned32
_AgentDhcp6ClientInterfaceIndex_Object=MibTableColumn
agentDhcp6ClientInterfaceIndex=_AgentDhcp6ClientInterfaceIndex_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,1),_AgentDhcp6ClientInterfaceIndex_Type())
agentDhcp6ClientInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientInterfaceIndex.setStatus(_A)
_AgentDhcp6ClientPrefix_Type=Ipv6AddressPrefix
_AgentDhcp6ClientPrefix_Object=MibTableColumn
agentDhcp6ClientPrefix=_AgentDhcp6ClientPrefix_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,2),_AgentDhcp6ClientPrefix_Type())
agentDhcp6ClientPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientPrefix.setStatus(_A)
_AgentDhcp6ClientPrefixlength_Type=Integer32
_AgentDhcp6ClientPrefixlength_Object=MibTableColumn
agentDhcp6ClientPrefixlength=_AgentDhcp6ClientPrefixlength_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,3),_AgentDhcp6ClientPrefixlength_Type())
agentDhcp6ClientPrefixlength.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientPrefixlength.setStatus(_A)
class _AgentDhcp6ClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('inactive',0),('solicit',1),('request',2),('active',3),('renew',4),('rebind',5),('release',6)))
_AgentDhcp6ClientState_Type.__name__=_C
_AgentDhcp6ClientState_Object=MibTableColumn
agentDhcp6ClientState=_AgentDhcp6ClientState_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,4),_AgentDhcp6ClientState_Type())
agentDhcp6ClientState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientState.setStatus(_A)
class _AgentDhcp6ClientServerDUID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AgentDhcp6ClientServerDUID_Type.__name__=_M
_AgentDhcp6ClientServerDUID_Object=MibTableColumn
agentDhcp6ClientServerDUID=_AgentDhcp6ClientServerDUID_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,5),_AgentDhcp6ClientServerDUID_Type())
agentDhcp6ClientServerDUID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientServerDUID.setStatus(_A)
_AgentDhcp6ClientT1Time_Type=Unsigned32
_AgentDhcp6ClientT1Time_Object=MibTableColumn
agentDhcp6ClientT1Time=_AgentDhcp6ClientT1Time_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,6),_AgentDhcp6ClientT1Time_Type())
agentDhcp6ClientT1Time.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientT1Time.setStatus(_A)
_AgentDhcp6ClientT2Time_Type=Unsigned32
_AgentDhcp6ClientT2Time_Object=MibTableColumn
agentDhcp6ClientT2Time=_AgentDhcp6ClientT2Time_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,7),_AgentDhcp6ClientT2Time_Type())
agentDhcp6ClientT2Time.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientT2Time.setStatus(_A)
_AgentDhcp6ClientIAID_Type=Unsigned32
_AgentDhcp6ClientIAID_Object=MibTableColumn
agentDhcp6ClientIAID=_AgentDhcp6ClientIAID_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,8),_AgentDhcp6ClientIAID_Type())
agentDhcp6ClientIAID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientIAID.setStatus(_A)
_AgentDhcp6ClientPreferredLifeTime_Type=Unsigned32
_AgentDhcp6ClientPreferredLifeTime_Object=MibTableColumn
agentDhcp6ClientPreferredLifeTime=_AgentDhcp6ClientPreferredLifeTime_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,9),_AgentDhcp6ClientPreferredLifeTime_Type())
agentDhcp6ClientPreferredLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientPreferredLifeTime.setStatus(_A)
_AgentDhcp6ClientValidLifeTime_Type=Unsigned32
_AgentDhcp6ClientValidLifeTime_Object=MibTableColumn
agentDhcp6ClientValidLifeTime=_AgentDhcp6ClientValidLifeTime_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,10),_AgentDhcp6ClientValidLifeTime_Type())
agentDhcp6ClientValidLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientValidLifeTime.setStatus(_A)
_AgentDhcp6ClientRenewTime_Type=Unsigned32
_AgentDhcp6ClientRenewTime_Object=MibTableColumn
agentDhcp6ClientRenewTime=_AgentDhcp6ClientRenewTime_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,11),_AgentDhcp6ClientRenewTime_Type())
agentDhcp6ClientRenewTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientRenewTime.setStatus(_A)
_AgentDhcp6ClientExpireTime_Type=Unsigned32
_AgentDhcp6ClientExpireTime_Object=MibTableColumn
agentDhcp6ClientExpireTime=_AgentDhcp6ClientExpireTime_Object((1,3,6,1,4,1,2356,16,1,30,1,9,1,12),_AgentDhcp6ClientExpireTime_Type())
agentDhcp6ClientExpireTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ClientExpireTime.setStatus(_A)
_AgentIpv6RoutingTableSummaryGroup_ObjectIdentity=ObjectIdentity
agentIpv6RoutingTableSummaryGroup=_AgentIpv6RoutingTableSummaryGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,30,1,10))
_AgentIpv6ConnectedRoutes_Type=Gauge32
_AgentIpv6ConnectedRoutes_Object=MibScalar
agentIpv6ConnectedRoutes=_AgentIpv6ConnectedRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,1),_AgentIpv6ConnectedRoutes_Type())
agentIpv6ConnectedRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ConnectedRoutes.setStatus(_A)
_AgentIpv6StaticRoutes_Type=Gauge32
_AgentIpv6StaticRoutes_Object=MibScalar
agentIpv6StaticRoutes=_AgentIpv6StaticRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,2),_AgentIpv6StaticRoutes_Type())
agentIpv6StaticRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6StaticRoutes.setStatus(_A)
_AgentIpv66to4Routes_Type=Gauge32
_AgentIpv66to4Routes_Object=MibScalar
agentIpv66to4Routes=_AgentIpv66to4Routes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,3),_AgentIpv66to4Routes_Type())
agentIpv66to4Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv66to4Routes.setStatus(_A)
_AgentIpv6OspfRoutes_Type=Gauge32
_AgentIpv6OspfRoutes_Object=MibScalar
agentIpv6OspfRoutes=_AgentIpv6OspfRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,4),_AgentIpv6OspfRoutes_Type())
agentIpv6OspfRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6OspfRoutes.setStatus(_A)
_AgentIpv6OspfIntraRoutes_Type=Gauge32
_AgentIpv6OspfIntraRoutes_Object=MibScalar
agentIpv6OspfIntraRoutes=_AgentIpv6OspfIntraRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,5),_AgentIpv6OspfIntraRoutes_Type())
agentIpv6OspfIntraRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6OspfIntraRoutes.setStatus(_A)
_AgentIpv6OspfInterRoutes_Type=Gauge32
_AgentIpv6OspfInterRoutes_Object=MibScalar
agentIpv6OspfInterRoutes=_AgentIpv6OspfInterRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,6),_AgentIpv6OspfInterRoutes_Type())
agentIpv6OspfInterRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6OspfInterRoutes.setStatus(_A)
_AgentIpv6OspfExt1Routes_Type=Gauge32
_AgentIpv6OspfExt1Routes_Object=MibScalar
agentIpv6OspfExt1Routes=_AgentIpv6OspfExt1Routes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,7),_AgentIpv6OspfExt1Routes_Type())
agentIpv6OspfExt1Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6OspfExt1Routes.setStatus(_A)
_AgentIpv6OspfExt2Routes_Type=Gauge32
_AgentIpv6OspfExt2Routes_Object=MibScalar
agentIpv6OspfExt2Routes=_AgentIpv6OspfExt2Routes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,8),_AgentIpv6OspfExt2Routes_Type())
agentIpv6OspfExt2Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6OspfExt2Routes.setStatus(_A)
_AgentIpv6BgpRoutes_Type=Gauge32
_AgentIpv6BgpRoutes_Object=MibScalar
agentIpv6BgpRoutes=_AgentIpv6BgpRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,9),_AgentIpv6BgpRoutes_Type())
agentIpv6BgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6BgpRoutes.setStatus(_A)
_AgentIpv6EbgpRoutes_Type=Gauge32
_AgentIpv6EbgpRoutes_Object=MibScalar
agentIpv6EbgpRoutes=_AgentIpv6EbgpRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,10),_AgentIpv6EbgpRoutes_Type())
agentIpv6EbgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6EbgpRoutes.setStatus(_A)
_AgentIpv6IbgpRoutes_Type=Gauge32
_AgentIpv6IbgpRoutes_Object=MibScalar
agentIpv6IbgpRoutes=_AgentIpv6IbgpRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,11),_AgentIpv6IbgpRoutes_Type())
agentIpv6IbgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6IbgpRoutes.setStatus(_A)
_AgentIpv6LocalBgpRoutes_Type=Gauge32
_AgentIpv6LocalBgpRoutes_Object=MibScalar
agentIpv6LocalBgpRoutes=_AgentIpv6LocalBgpRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,12),_AgentIpv6LocalBgpRoutes_Type())
agentIpv6LocalBgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6LocalBgpRoutes.setStatus(_A)
_AgentIpv6RejectRoutes_Type=Gauge32
_AgentIpv6RejectRoutes_Object=MibScalar
agentIpv6RejectRoutes=_AgentIpv6RejectRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,13),_AgentIpv6RejectRoutes_Type())
agentIpv6RejectRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RejectRoutes.setStatus(_A)
_AgentIpv6TotalRoutes_Type=Gauge32
_AgentIpv6TotalRoutes_Object=MibScalar
agentIpv6TotalRoutes=_AgentIpv6TotalRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,14),_AgentIpv6TotalRoutes_Type())
agentIpv6TotalRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6TotalRoutes.setStatus(_A)
_AgentIpv6BestRoutes_Type=Gauge32
_AgentIpv6BestRoutes_Object=MibScalar
agentIpv6BestRoutes=_AgentIpv6BestRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,15),_AgentIpv6BestRoutes_Type())
agentIpv6BestRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6BestRoutes.setStatus(_A)
_AgentIpv6BestRoutesHigh_Type=Gauge32
_AgentIpv6BestRoutesHigh_Object=MibScalar
agentIpv6BestRoutesHigh=_AgentIpv6BestRoutesHigh_Object((1,3,6,1,4,1,2356,16,1,30,1,10,16),_AgentIpv6BestRoutesHigh_Type())
agentIpv6BestRoutesHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6BestRoutesHigh.setStatus(_A)
_AgentIpv6AlternateRoutes_Type=Gauge32
_AgentIpv6AlternateRoutes_Object=MibScalar
agentIpv6AlternateRoutes=_AgentIpv6AlternateRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,17),_AgentIpv6AlternateRoutes_Type())
agentIpv6AlternateRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6AlternateRoutes.setStatus(_A)
_AgentIpv6RouteAdds_Type=Counter32
_AgentIpv6RouteAdds_Object=MibScalar
agentIpv6RouteAdds=_AgentIpv6RouteAdds_Object((1,3,6,1,4,1,2356,16,1,30,1,10,18),_AgentIpv6RouteAdds_Type())
agentIpv6RouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouteAdds.setStatus(_A)
_AgentIpv6RouteModifies_Type=Counter32
_AgentIpv6RouteModifies_Object=MibScalar
agentIpv6RouteModifies=_AgentIpv6RouteModifies_Object((1,3,6,1,4,1,2356,16,1,30,1,10,19),_AgentIpv6RouteModifies_Type())
agentIpv6RouteModifies.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouteModifies.setStatus(_A)
_AgentIpv6RouteDeletes_Type=Counter32
_AgentIpv6RouteDeletes_Object=MibScalar
agentIpv6RouteDeletes=_AgentIpv6RouteDeletes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,20),_AgentIpv6RouteDeletes_Type())
agentIpv6RouteDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6RouteDeletes.setStatus(_A)
_AgentIpv6UnresolvedRouteAdds_Type=Counter32
_AgentIpv6UnresolvedRouteAdds_Object=MibScalar
agentIpv6UnresolvedRouteAdds=_AgentIpv6UnresolvedRouteAdds_Object((1,3,6,1,4,1,2356,16,1,30,1,10,21),_AgentIpv6UnresolvedRouteAdds_Type())
agentIpv6UnresolvedRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6UnresolvedRouteAdds.setStatus(_A)
_AgentIpv6InvalidRouteAdds_Type=Counter32
_AgentIpv6InvalidRouteAdds_Object=MibScalar
agentIpv6InvalidRouteAdds=_AgentIpv6InvalidRouteAdds_Object((1,3,6,1,4,1,2356,16,1,30,1,10,22),_AgentIpv6InvalidRouteAdds_Type())
agentIpv6InvalidRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6InvalidRouteAdds.setStatus(_A)
_AgentIpv6FailedRouteAdds_Type=Counter32
_AgentIpv6FailedRouteAdds_Object=MibScalar
agentIpv6FailedRouteAdds=_AgentIpv6FailedRouteAdds_Object((1,3,6,1,4,1,2356,16,1,30,1,10,23),_AgentIpv6FailedRouteAdds_Type())
agentIpv6FailedRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6FailedRouteAdds.setStatus(_A)
_AgentIpv6ReservedLocals_Type=Gauge32
_AgentIpv6ReservedLocals_Object=MibScalar
agentIpv6ReservedLocals=_AgentIpv6ReservedLocals_Object((1,3,6,1,4,1,2356,16,1,30,1,10,24),_AgentIpv6ReservedLocals_Type())
agentIpv6ReservedLocals.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6ReservedLocals.setStatus(_A)
_AgentIpv6UniqueNextHops_Type=Gauge32
_AgentIpv6UniqueNextHops_Object=MibScalar
agentIpv6UniqueNextHops=_AgentIpv6UniqueNextHops_Object((1,3,6,1,4,1,2356,16,1,30,1,10,25),_AgentIpv6UniqueNextHops_Type())
agentIpv6UniqueNextHops.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6UniqueNextHops.setStatus(_A)
_AgentIpv6UniqueNextHopsHigh_Type=Gauge32
_AgentIpv6UniqueNextHopsHigh_Object=MibScalar
agentIpv6UniqueNextHopsHigh=_AgentIpv6UniqueNextHopsHigh_Object((1,3,6,1,4,1,2356,16,1,30,1,10,26),_AgentIpv6UniqueNextHopsHigh_Type())
agentIpv6UniqueNextHopsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6UniqueNextHopsHigh.setStatus(_A)
_AgentIpv6NextHopGroups_Type=Gauge32
_AgentIpv6NextHopGroups_Object=MibScalar
agentIpv6NextHopGroups=_AgentIpv6NextHopGroups_Object((1,3,6,1,4,1,2356,16,1,30,1,10,27),_AgentIpv6NextHopGroups_Type())
agentIpv6NextHopGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6NextHopGroups.setStatus(_A)
_AgentIpv6NextHopGroupsHigh_Type=Gauge32
_AgentIpv6NextHopGroupsHigh_Object=MibScalar
agentIpv6NextHopGroupsHigh=_AgentIpv6NextHopGroupsHigh_Object((1,3,6,1,4,1,2356,16,1,30,1,10,28),_AgentIpv6NextHopGroupsHigh_Type())
agentIpv6NextHopGroupsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6NextHopGroupsHigh.setStatus(_A)
_AgentIpv6EcmpGroups_Type=Gauge32
_AgentIpv6EcmpGroups_Object=MibScalar
agentIpv6EcmpGroups=_AgentIpv6EcmpGroups_Object((1,3,6,1,4,1,2356,16,1,30,1,10,29),_AgentIpv6EcmpGroups_Type())
agentIpv6EcmpGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6EcmpGroups.setStatus(_A)
_AgentIpv6EcmpGroupsHigh_Type=Gauge32
_AgentIpv6EcmpGroupsHigh_Object=MibScalar
agentIpv6EcmpGroupsHigh=_AgentIpv6EcmpGroupsHigh_Object((1,3,6,1,4,1,2356,16,1,30,1,10,30),_AgentIpv6EcmpGroupsHigh_Type())
agentIpv6EcmpGroupsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6EcmpGroupsHigh.setStatus(_A)
_AgentIpv6EcmpRoutes_Type=Gauge32
_AgentIpv6EcmpRoutes_Object=MibScalar
agentIpv6EcmpRoutes=_AgentIpv6EcmpRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,31),_AgentIpv6EcmpRoutes_Type())
agentIpv6EcmpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6EcmpRoutes.setStatus(_A)
_AgentIpv6TruncEcmpRoutes_Type=Gauge32
_AgentIpv6TruncEcmpRoutes_Object=MibScalar
agentIpv6TruncEcmpRoutes=_AgentIpv6TruncEcmpRoutes_Object((1,3,6,1,4,1,2356,16,1,30,1,10,32),_AgentIpv6TruncEcmpRoutes_Type())
agentIpv6TruncEcmpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6TruncEcmpRoutes.setStatus(_A)
_AgentIpv6EcmpRetries_Type=Counter32
_AgentIpv6EcmpRetries_Object=MibScalar
agentIpv6EcmpRetries=_AgentIpv6EcmpRetries_Object((1,3,6,1,4,1,2356,16,1,30,1,10,33),_AgentIpv6EcmpRetries_Type())
agentIpv6EcmpRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6EcmpRetries.setStatus(_A)
_AgentIpv6EcmpCountTable_Object=MibTable
agentIpv6EcmpCountTable=_AgentIpv6EcmpCountTable_Object((1,3,6,1,4,1,2356,16,1,30,1,11))
if mibBuilder.loadTexts:agentIpv6EcmpCountTable.setStatus(_A)
_AgentIpv6EcmpCountEntry_Object=MibTableRow
agentIpv6EcmpCountEntry=_AgentIpv6EcmpCountEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,11,1))
agentIpv6EcmpCountEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:agentIpv6EcmpCountEntry.setStatus(_A)
class _AgentIpv6EcmpNextHopCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6EcmpNextHopCount_Type.__name__=_K
_AgentIpv6EcmpNextHopCount_Object=MibTableColumn
agentIpv6EcmpNextHopCount=_AgentIpv6EcmpNextHopCount_Object((1,3,6,1,4,1,2356,16,1,30,1,11,1,1),_AgentIpv6EcmpNextHopCount_Type())
agentIpv6EcmpNextHopCount.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6EcmpNextHopCount.setStatus(_A)
_AgentIpv6EcmpRouteCount_Type=Gauge32
_AgentIpv6EcmpRouteCount_Object=MibTableColumn
agentIpv6EcmpRouteCount=_AgentIpv6EcmpRouteCount_Object((1,3,6,1,4,1,2356,16,1,30,1,11,1,2),_AgentIpv6EcmpRouteCount_Type())
agentIpv6EcmpRouteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6EcmpRouteCount.setStatus(_A)
_AgentIpv6NetworkPortGroup_ObjectIdentity=ObjectIdentity
agentIpv6NetworkPortGroup=_AgentIpv6NetworkPortGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,30,1,12))
_AgentIpv6NetworkPortNbrTable_Object=MibTable
agentIpv6NetworkPortNbrTable=_AgentIpv6NetworkPortNbrTable_Object((1,3,6,1,4,1,2356,16,1,30,1,12,1))
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrTable.setStatus(_A)
_AgentIpv6NetworkPortNbrEntry_Object=MibTableRow
agentIpv6NetworkPortNbrEntry=_AgentIpv6NetworkPortNbrEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,12,1,1))
agentIpv6NetworkPortNbrEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrEntry.setStatus(_A)
_AgentIpv6NetworkPortNbrAddr_Type=Ipv6Address
_AgentIpv6NetworkPortNbrAddr_Object=MibTableColumn
agentIpv6NetworkPortNbrAddr=_AgentIpv6NetworkPortNbrAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,12,1,1,1),_AgentIpv6NetworkPortNbrAddr_Type())
agentIpv6NetworkPortNbrAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrAddr.setStatus(_A)
_AgentIpv6NetworkPortNbrPhysAddr_Type=MacAddress
_AgentIpv6NetworkPortNbrPhysAddr_Object=MibTableColumn
agentIpv6NetworkPortNbrPhysAddr=_AgentIpv6NetworkPortNbrPhysAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,12,1,1,2),_AgentIpv6NetworkPortNbrPhysAddr_Type())
agentIpv6NetworkPortNbrPhysAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrPhysAddr.setStatus(_A)
class _AgentIpv6NetworkPortNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6)));namedValues=NamedValues(*((_Z,1),('stale',2),('delay',3),('probe',4),(_a,6)))
_AgentIpv6NetworkPortNbrState_Type.__name__=_C
_AgentIpv6NetworkPortNbrState_Object=MibTableColumn
agentIpv6NetworkPortNbrState=_AgentIpv6NetworkPortNbrState_Object((1,3,6,1,4,1,2356,16,1,30,1,12,1,1,3),_AgentIpv6NetworkPortNbrState_Type())
agentIpv6NetworkPortNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrState.setStatus(_A)
_AgentIpv6NetworkPortNbrUpdated_Type=TimeStamp
_AgentIpv6NetworkPortNbrUpdated_Object=MibTableColumn
agentIpv6NetworkPortNbrUpdated=_AgentIpv6NetworkPortNbrUpdated_Object((1,3,6,1,4,1,2356,16,1,30,1,12,1,1,4),_AgentIpv6NetworkPortNbrUpdated_Type())
agentIpv6NetworkPortNbrUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrUpdated.setStatus(_A)
_AgentIpv6NetworkPortNbrIsRouter_Type=TruthValue
_AgentIpv6NetworkPortNbrIsRouter_Object=MibTableColumn
agentIpv6NetworkPortNbrIsRouter=_AgentIpv6NetworkPortNbrIsRouter_Object((1,3,6,1,4,1,2356,16,1,30,1,12,1,1,5),_AgentIpv6NetworkPortNbrIsRouter_Type())
agentIpv6NetworkPortNbrIsRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrIsRouter.setStatus(_A)
class _AgentIpv6NetworkPortNbrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_b,2),(_c,3),('local',4)))
_AgentIpv6NetworkPortNbrType_Type.__name__=_C
_AgentIpv6NetworkPortNbrType_Object=MibTableColumn
agentIpv6NetworkPortNbrType=_AgentIpv6NetworkPortNbrType_Object((1,3,6,1,4,1,2356,16,1,30,1,12,1,1,6),_AgentIpv6NetworkPortNbrType_Type())
agentIpv6NetworkPortNbrType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrType.setStatus(_A)
_AgentIpv6NetworkPortNbrCfgTable_Object=MibTable
agentIpv6NetworkPortNbrCfgTable=_AgentIpv6NetworkPortNbrCfgTable_Object((1,3,6,1,4,1,2356,16,1,30,1,12,2))
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrCfgTable.setStatus(_A)
_AgentIpv6NetworkPortNbrCfgEntry_Object=MibTableRow
agentIpv6NetworkPortNbrCfgEntry=_AgentIpv6NetworkPortNbrCfgEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,12,2,1))
agentIpv6NetworkPortNbrCfgEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrCfgEntry.setStatus(_A)
_AgentIpv6NetworkPortNbrCfgAddr_Type=Ipv6Address
_AgentIpv6NetworkPortNbrCfgAddr_Object=MibTableColumn
agentIpv6NetworkPortNbrCfgAddr=_AgentIpv6NetworkPortNbrCfgAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,12,2,1,1),_AgentIpv6NetworkPortNbrCfgAddr_Type())
agentIpv6NetworkPortNbrCfgAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrCfgAddr.setStatus(_A)
_AgentIpv6NetworkPortNbrCfgPhysAddr_Type=MacAddress
_AgentIpv6NetworkPortNbrCfgPhysAddr_Object=MibTableColumn
agentIpv6NetworkPortNbrCfgPhysAddr=_AgentIpv6NetworkPortNbrCfgPhysAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,12,2,1,2),_AgentIpv6NetworkPortNbrCfgPhysAddr_Type())
agentIpv6NetworkPortNbrCfgPhysAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrCfgPhysAddr.setStatus(_A)
_AgentIpv6NetworkPortNbrCfgEntryStatus_Type=RowStatus
_AgentIpv6NetworkPortNbrCfgEntryStatus_Object=MibTableColumn
agentIpv6NetworkPortNbrCfgEntryStatus=_AgentIpv6NetworkPortNbrCfgEntryStatus_Object((1,3,6,1,4,1,2356,16,1,30,1,12,2,1,3),_AgentIpv6NetworkPortNbrCfgEntryStatus_Type())
agentIpv6NetworkPortNbrCfgEntryStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6NetworkPortNbrCfgEntryStatus.setStatus(_A)
_AgentIpv6NbrCfgTable_Object=MibTable
agentIpv6NbrCfgTable=_AgentIpv6NbrCfgTable_Object((1,3,6,1,4,1,2356,16,1,30,1,13))
if mibBuilder.loadTexts:agentIpv6NbrCfgTable.setStatus(_A)
_AgentIpv6NbrCfgEntry_Object=MibTableRow
agentIpv6NbrCfgEntry=_AgentIpv6NbrCfgEntry_Object((1,3,6,1,4,1,2356,16,1,30,1,13,1))
agentIpv6NbrCfgEntry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:agentIpv6NbrCfgEntry.setStatus(_A)
_AgentIpv6IfIndex_Type=Ipv6IfIndex
_AgentIpv6IfIndex_Object=MibTableColumn
agentIpv6IfIndex=_AgentIpv6IfIndex_Object((1,3,6,1,4,1,2356,16,1,30,1,13,1,1),_AgentIpv6IfIndex_Type())
agentIpv6IfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6IfIndex.setStatus(_A)
_AgentIpv6NbrCfgAddr_Type=Ipv6Address
_AgentIpv6NbrCfgAddr_Object=MibTableColumn
agentIpv6NbrCfgAddr=_AgentIpv6NbrCfgAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,13,1,2),_AgentIpv6NbrCfgAddr_Type())
agentIpv6NbrCfgAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6NbrCfgAddr.setStatus(_A)
_AgentIpv6NbrCfgPhysAddr_Type=MacAddress
_AgentIpv6NbrCfgPhysAddr_Object=MibTableColumn
agentIpv6NbrCfgPhysAddr=_AgentIpv6NbrCfgPhysAddr_Object((1,3,6,1,4,1,2356,16,1,30,1,13,1,3),_AgentIpv6NbrCfgPhysAddr_Type())
agentIpv6NbrCfgPhysAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6NbrCfgPhysAddr.setStatus(_A)
_AgentIpv6NbrCfgEntryStatus_Type=RowStatus
_AgentIpv6NbrCfgEntryStatus_Object=MibTableColumn
agentIpv6NbrCfgEntryStatus=_AgentIpv6NbrCfgEntryStatus_Object((1,3,6,1,4,1,2356,16,1,30,1,13,1,4),_AgentIpv6NbrCfgEntryStatus_Type())
agentIpv6NbrCfgEntryStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6NbrCfgEntryStatus.setStatus(_A)
class _AgentIpv6NeighborsDynamicRenew_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6NeighborsDynamicRenew_Type.__name__=_C
_AgentIpv6NeighborsDynamicRenew_Object=MibScalar
agentIpv6NeighborsDynamicRenew=_AgentIpv6NeighborsDynamicRenew_Object((1,3,6,1,4,1,2356,16,1,30,1,14),_AgentIpv6NeighborsDynamicRenew_Type())
agentIpv6NeighborsDynamicRenew.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NeighborsDynamicRenew.setStatus(_A)
class _AgentIpv6UnresolvedDataRateLimit_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,1024))
_AgentIpv6UnresolvedDataRateLimit_Type.__name__=_C
_AgentIpv6UnresolvedDataRateLimit_Object=MibScalar
agentIpv6UnresolvedDataRateLimit=_AgentIpv6UnresolvedDataRateLimit_Object((1,3,6,1,4,1,2356,16,1,30,1,15),_AgentIpv6UnresolvedDataRateLimit_Type())
agentIpv6UnresolvedDataRateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6UnresolvedDataRateLimit.setStatus(_A)
class _AgentIpv6NUDMaxUnicastSolicits_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_AgentIpv6NUDMaxUnicastSolicits_Type.__name__=_C
_AgentIpv6NUDMaxUnicastSolicits_Object=MibScalar
agentIpv6NUDMaxUnicastSolicits=_AgentIpv6NUDMaxUnicastSolicits_Object((1,3,6,1,4,1,2356,16,1,30,1,16),_AgentIpv6NUDMaxUnicastSolicits_Type())
agentIpv6NUDMaxUnicastSolicits.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NUDMaxUnicastSolicits.setStatus(_A)
class _AgentIpv6NUDMaxMulticastSolicits_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,255))
_AgentIpv6NUDMaxMulticastSolicits_Type.__name__=_C
_AgentIpv6NUDMaxMulticastSolicits_Object=MibScalar
agentIpv6NUDMaxMulticastSolicits=_AgentIpv6NUDMaxMulticastSolicits_Object((1,3,6,1,4,1,2356,16,1,30,1,17),_AgentIpv6NUDMaxMulticastSolicits_Type())
agentIpv6NUDMaxMulticastSolicits.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NUDMaxMulticastSolicits.setStatus(_A)
class _AgentIpv6NUDBackoffMultiple_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_AgentIpv6NUDBackoffMultiple_Type.__name__=_C
_AgentIpv6NUDBackoffMultiple_Object=MibScalar
agentIpv6NUDBackoffMultiple=_AgentIpv6NUDBackoffMultiple_Object((1,3,6,1,4,1,2356,16,1,30,1,18),_AgentIpv6NUDBackoffMultiple_Type())
agentIpv6NUDBackoffMultiple.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpv6NUDBackoffMultiple.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fastPathRoutingIpv6':fastPathRoutingIpv6,'agentIpv6Group':agentIpv6Group,'agentIpv6RoutingMode':agentIpv6RoutingMode,'agentIpv6InterfaceTable':agentIpv6InterfaceTable,'agentIpv6InterfaceEntry':agentIpv6InterfaceEntry,_J:agentIpv6InterfaceIfIndex,'agentIpv6InterfaceMtuValue':agentIpv6InterfaceMtuValue,'agentIpv6InterfaceDadTransmits':agentIpv6InterfaceDadTransmits,'agentIpv6InterfaceLinkLocalOnly':agentIpv6InterfaceLinkLocalOnly,'agentIpv6InterfaceIcmpUnreachables':agentIpv6InterfaceIcmpUnreachables,'agentIpv6InterfaceAutoconfig':agentIpv6InterfaceAutoconfig,'agentIpv6InterfaceDhcpClient':agentIpv6InterfaceDhcpClient,'agentIpv6InterfaceIcmpRedirects':agentIpv6InterfaceIcmpRedirects,'agentIpv6RouterAdvertisementTable':agentIpv6RouterAdvertisementTable,'agentIpv6RouterAdvertisementEntry':agentIpv6RouterAdvertisementEntry,_N:agentIpv6RouterAdvertisementIfIndex,'agentIpv6RouterAdvertisementSuppressMode':agentIpv6RouterAdvertisementSuppressMode,'agentIpv6RouterAdvertisementMaxAdvertisementInterval':agentIpv6RouterAdvertisementMaxAdvertisementInterval,'agentIpv6RouterAdvertisementAdvertisementLifetime':agentIpv6RouterAdvertisementAdvertisementLifetime,'agentIpv6RouterAdvertisementNbrSolicitInterval':agentIpv6RouterAdvertisementNbrSolicitInterval,'agentIpv6RouterAdvertisementReachableTime':agentIpv6RouterAdvertisementReachableTime,'agentIpv6RouterAdvertisementManagedFlag':agentIpv6RouterAdvertisementManagedFlag,'agentIpv6RouterAdvertisementOtherFlag':agentIpv6RouterAdvertisementOtherFlag,'agentIpv6RouterAdvertisementHopLimitUnspecifiedMode':agentIpv6RouterAdvertisementHopLimitUnspecifiedMode,'agentIpv6AddrPrefixTable':agentIpv6AddrPrefixTable,'agentIpv6AddrPrefixEntry':agentIpv6AddrPrefixEntry,_O:agentIpv6AddrPrefix,_P:agentIpv6AddrPrefixLength,'agentIpv6AddrPrefixOnLinkFlag':agentIpv6AddrPrefixOnLinkFlag,'agentIpv6AddrPrefixAutonomousFlag':agentIpv6AddrPrefixAutonomousFlag,'agentIpv6AddrPrefixAdvPreferredLifetime':agentIpv6AddrPrefixAdvPreferredLifetime,'agentIpv6AddrPrefixAdvValidLifetime':agentIpv6AddrPrefixAdvValidLifetime,'agentIpv6AddrTable':agentIpv6AddrTable,'agentIpv6AddrEntry':agentIpv6AddrEntry,_R:agentIpv6AddrAddress,'agentIpv6AddrPfxLength':agentIpv6AddrPfxLength,'agentIpv6AddrEui64Flag':agentIpv6AddrEui64Flag,'agentIpv6AddrStatus':agentIpv6AddrStatus,'agentIpv6StaticRouteTable':agentIpv6StaticRouteTable,'agentIpv6StaticRouteEntry':agentIpv6StaticRouteEntry,_S:agentIpv6StaticRouteDest,_T:agentIpv6StaticRoutePfxLength,_U:agentIpv6StaticRouteIfIndex,_V:agentIpv6StaticRouteNextHop,'agentIpv6StaticRoutePreference':agentIpv6StaticRoutePreference,'agentIpv6StaticRouteStatus':agentIpv6StaticRouteStatus,'agentIpv6ServicePortGroup':agentIpv6ServicePortGroup,'agentIpv6ServicePortPrefixTable':agentIpv6ServicePortPrefixTable,'agentIpv6ServicePortPrefixEntry':agentIpv6ServicePortPrefixEntry,_W:agentIpv6ServicePortPrefixIndex,'agentIpv6ServicePortPrefix':agentIpv6ServicePortPrefix,'agentIpv6ServicePortPrefixLength':agentIpv6ServicePortPrefixLength,'agentIpv6ServicePortDefaultRouterTable':agentIpv6ServicePortDefaultRouterTable,'agentIpv6ServicePortDefaultRouterEntry':agentIpv6ServicePortDefaultRouterEntry,_X:agentIpv6ServicePortDefaultRouterIndex,'agentIpv6ServicePortDefaultRouter':agentIpv6ServicePortDefaultRouter,'agentIpv6ServicePortNbrTable':agentIpv6ServicePortNbrTable,'agentIpv6ServicePortNbrEntry':agentIpv6ServicePortNbrEntry,_Y:agentIpv6ServicePortNbrAddr,'agentIpv6ServicePortNbrPhysAddr':agentIpv6ServicePortNbrPhysAddr,'agentIpv6ServicePortNbrState':agentIpv6ServicePortNbrState,'agentIpv6ServicePortNbrUpdated':agentIpv6ServicePortNbrUpdated,'agentIpv6ServicePortNbrIsRouter':agentIpv6ServicePortNbrIsRouter,'agentIpv6ServicePortNbrType':agentIpv6ServicePortNbrType,'agentIpv6ServicePortNbrCfgTable':agentIpv6ServicePortNbrCfgTable,'agentIpv6ServicePortNbrCfgEntry':agentIpv6ServicePortNbrCfgEntry,_d:agentIpv6ServicePortNbrCfgAddr,'agentIpv6ServicePortNbrCfgPhysAddr':agentIpv6ServicePortNbrCfgPhysAddr,'agentIpv6ServicePortNbrCfgEntryStatus':agentIpv6ServicePortNbrCfgEntryStatus,'agentIpv6IcmpControlGroup':agentIpv6IcmpControlGroup,'agentIpv6IcmpRateLimitInterval':agentIpv6IcmpRateLimitInterval,'agentIpv6IcmpRateLimitBurstSize':agentIpv6IcmpRateLimitBurstSize,'agentDhcp6ClientParametersTable':agentDhcp6ClientParametersTable,'agentDhcp6ClientParametersEntry':agentDhcp6ClientParametersEntry,_e:agentDhcp6ClientInterfaceIndex,'agentDhcp6ClientPrefix':agentDhcp6ClientPrefix,'agentDhcp6ClientPrefixlength':agentDhcp6ClientPrefixlength,'agentDhcp6ClientState':agentDhcp6ClientState,'agentDhcp6ClientServerDUID':agentDhcp6ClientServerDUID,'agentDhcp6ClientT1Time':agentDhcp6ClientT1Time,'agentDhcp6ClientT2Time':agentDhcp6ClientT2Time,'agentDhcp6ClientIAID':agentDhcp6ClientIAID,'agentDhcp6ClientPreferredLifeTime':agentDhcp6ClientPreferredLifeTime,'agentDhcp6ClientValidLifeTime':agentDhcp6ClientValidLifeTime,'agentDhcp6ClientRenewTime':agentDhcp6ClientRenewTime,'agentDhcp6ClientExpireTime':agentDhcp6ClientExpireTime,'agentIpv6RoutingTableSummaryGroup':agentIpv6RoutingTableSummaryGroup,'agentIpv6ConnectedRoutes':agentIpv6ConnectedRoutes,'agentIpv6StaticRoutes':agentIpv6StaticRoutes,'agentIpv66to4Routes':agentIpv66to4Routes,'agentIpv6OspfRoutes':agentIpv6OspfRoutes,'agentIpv6OspfIntraRoutes':agentIpv6OspfIntraRoutes,'agentIpv6OspfInterRoutes':agentIpv6OspfInterRoutes,'agentIpv6OspfExt1Routes':agentIpv6OspfExt1Routes,'agentIpv6OspfExt2Routes':agentIpv6OspfExt2Routes,'agentIpv6BgpRoutes':agentIpv6BgpRoutes,'agentIpv6EbgpRoutes':agentIpv6EbgpRoutes,'agentIpv6IbgpRoutes':agentIpv6IbgpRoutes,'agentIpv6LocalBgpRoutes':agentIpv6LocalBgpRoutes,'agentIpv6RejectRoutes':agentIpv6RejectRoutes,'agentIpv6TotalRoutes':agentIpv6TotalRoutes,'agentIpv6BestRoutes':agentIpv6BestRoutes,'agentIpv6BestRoutesHigh':agentIpv6BestRoutesHigh,'agentIpv6AlternateRoutes':agentIpv6AlternateRoutes,'agentIpv6RouteAdds':agentIpv6RouteAdds,'agentIpv6RouteModifies':agentIpv6RouteModifies,'agentIpv6RouteDeletes':agentIpv6RouteDeletes,'agentIpv6UnresolvedRouteAdds':agentIpv6UnresolvedRouteAdds,'agentIpv6InvalidRouteAdds':agentIpv6InvalidRouteAdds,'agentIpv6FailedRouteAdds':agentIpv6FailedRouteAdds,'agentIpv6ReservedLocals':agentIpv6ReservedLocals,'agentIpv6UniqueNextHops':agentIpv6UniqueNextHops,'agentIpv6UniqueNextHopsHigh':agentIpv6UniqueNextHopsHigh,'agentIpv6NextHopGroups':agentIpv6NextHopGroups,'agentIpv6NextHopGroupsHigh':agentIpv6NextHopGroupsHigh,'agentIpv6EcmpGroups':agentIpv6EcmpGroups,'agentIpv6EcmpGroupsHigh':agentIpv6EcmpGroupsHigh,'agentIpv6EcmpRoutes':agentIpv6EcmpRoutes,'agentIpv6TruncEcmpRoutes':agentIpv6TruncEcmpRoutes,'agentIpv6EcmpRetries':agentIpv6EcmpRetries,'agentIpv6EcmpCountTable':agentIpv6EcmpCountTable,'agentIpv6EcmpCountEntry':agentIpv6EcmpCountEntry,_f:agentIpv6EcmpNextHopCount,'agentIpv6EcmpRouteCount':agentIpv6EcmpRouteCount,'agentIpv6NetworkPortGroup':agentIpv6NetworkPortGroup,'agentIpv6NetworkPortNbrTable':agentIpv6NetworkPortNbrTable,'agentIpv6NetworkPortNbrEntry':agentIpv6NetworkPortNbrEntry,_g:agentIpv6NetworkPortNbrAddr,'agentIpv6NetworkPortNbrPhysAddr':agentIpv6NetworkPortNbrPhysAddr,'agentIpv6NetworkPortNbrState':agentIpv6NetworkPortNbrState,'agentIpv6NetworkPortNbrUpdated':agentIpv6NetworkPortNbrUpdated,'agentIpv6NetworkPortNbrIsRouter':agentIpv6NetworkPortNbrIsRouter,'agentIpv6NetworkPortNbrType':agentIpv6NetworkPortNbrType,'agentIpv6NetworkPortNbrCfgTable':agentIpv6NetworkPortNbrCfgTable,'agentIpv6NetworkPortNbrCfgEntry':agentIpv6NetworkPortNbrCfgEntry,_h:agentIpv6NetworkPortNbrCfgAddr,'agentIpv6NetworkPortNbrCfgPhysAddr':agentIpv6NetworkPortNbrCfgPhysAddr,'agentIpv6NetworkPortNbrCfgEntryStatus':agentIpv6NetworkPortNbrCfgEntryStatus,'agentIpv6NbrCfgTable':agentIpv6NbrCfgTable,'agentIpv6NbrCfgEntry':agentIpv6NbrCfgEntry,_i:agentIpv6IfIndex,_j:agentIpv6NbrCfgAddr,'agentIpv6NbrCfgPhysAddr':agentIpv6NbrCfgPhysAddr,'agentIpv6NbrCfgEntryStatus':agentIpv6NbrCfgEntryStatus,'agentIpv6NeighborsDynamicRenew':agentIpv6NeighborsDynamicRenew,'agentIpv6UnresolvedDataRateLimit':agentIpv6UnresolvedDataRateLimit,'agentIpv6NUDMaxUnicastSolicits':agentIpv6NUDMaxUnicastSolicits,'agentIpv6NUDMaxMulticastSolicits':agentIpv6NUDMaxMulticastSolicits,'agentIpv6NUDBackoffMultiple':agentIpv6NUDBackoffMultiple})