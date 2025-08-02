_X='agentIpv6ServicePortNbrAddr'
_W='agentIpv6ServicePortDefaultRouterIndex'
_V='agentIpv6ServicePortPrefixIndex'
_U='agentIpv6StaticRouteNextHop'
_T='agentIpv6StaticRouteIfIndex'
_S='agentIpv6StaticRoutePfxLength'
_R='agentIpv6StaticRouteDest'
_Q='agentIpv6AddrAddress'
_P='seconds'
_O='agentIpv6AddrPrefixLength'
_N='agentIpv6AddrPrefix'
_M='agentIpv6RouterAdvertisementIfIndex'
_L='Unsigned32'
_K='bits'
_J='agentIpv6InterfaceIfIndex'
_I='read-create'
_H='disable'
_G='enable'
_F='read-only'
_E='not-accessible'
_D='FASTPATH-ROUTING6-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('BROADCOM-REF-MIB','fastPath')
Ipv6Address,Ipv6AddressIfIdentifier,Ipv6AddressPrefix,Ipv6IfIndex,Ipv6IfIndexOrZero=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressIfIdentifier','Ipv6AddressPrefix','Ipv6IfIndex','Ipv6IfIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp','TruthValue','VariablePointer')
fastPathRoutingIpv6=ModuleIdentity((1,3,6,1,4,1,4413,1,1,30))
if mibBuilder.loadTexts:fastPathRoutingIpv6.setRevisions(('2007-05-23 00:00','2005-09-21 17:00'))
_AgentIpv6Group_ObjectIdentity=ObjectIdentity
agentIpv6Group=_AgentIpv6Group_ObjectIdentity((1,3,6,1,4,1,4413,1,1,30,1))
class _AgentIpv6RoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6RoutingMode_Type.__name__=_B
_AgentIpv6RoutingMode_Object=MibScalar
agentIpv6RoutingMode=_AgentIpv6RoutingMode_Object((1,3,6,1,4,1,4413,1,1,30,1,1),_AgentIpv6RoutingMode_Type())
agentIpv6RoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6RoutingMode.setStatus(_A)
_AgentIpv6InterfaceTable_Object=MibTable
agentIpv6InterfaceTable=_AgentIpv6InterfaceTable_Object((1,3,6,1,4,1,4413,1,1,30,1,2))
if mibBuilder.loadTexts:agentIpv6InterfaceTable.setStatus(_A)
_AgentIpv6InterfaceEntry_Object=MibTableRow
agentIpv6InterfaceEntry=_AgentIpv6InterfaceEntry_Object((1,3,6,1,4,1,4413,1,1,30,1,2,1))
agentIpv6InterfaceEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:agentIpv6InterfaceEntry.setStatus(_A)
class _AgentIpv6InterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIpv6InterfaceIfIndex_Type.__name__=_B
_AgentIpv6InterfaceIfIndex_Object=MibTableColumn
agentIpv6InterfaceIfIndex=_AgentIpv6InterfaceIfIndex_Object((1,3,6,1,4,1,4413,1,1,30,1,2,1,1),_AgentIpv6InterfaceIfIndex_Type())
agentIpv6InterfaceIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6InterfaceIfIndex.setStatus(_A)
class _AgentIpv6InterfaceMtuValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1280,1500))
_AgentIpv6InterfaceMtuValue_Type.__name__=_L
_AgentIpv6InterfaceMtuValue_Object=MibTableColumn
agentIpv6InterfaceMtuValue=_AgentIpv6InterfaceMtuValue_Object((1,3,6,1,4,1,4413,1,1,30,1,2,1,2),_AgentIpv6InterfaceMtuValue_Type())
agentIpv6InterfaceMtuValue.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6InterfaceMtuValue.setStatus(_A)
class _AgentIpv6InterfaceDadTransmits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AgentIpv6InterfaceDadTransmits_Type.__name__=_B
_AgentIpv6InterfaceDadTransmits_Object=MibTableColumn
agentIpv6InterfaceDadTransmits=_AgentIpv6InterfaceDadTransmits_Object((1,3,6,1,4,1,4413,1,1,30,1,2,1,3),_AgentIpv6InterfaceDadTransmits_Type())
agentIpv6InterfaceDadTransmits.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6InterfaceDadTransmits.setStatus(_A)
class _AgentIpv6InterfaceLinkLocalOnly_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6InterfaceLinkLocalOnly_Type.__name__=_B
_AgentIpv6InterfaceLinkLocalOnly_Object=MibTableColumn
agentIpv6InterfaceLinkLocalOnly=_AgentIpv6InterfaceLinkLocalOnly_Object((1,3,6,1,4,1,4413,1,1,30,1,2,1,4),_AgentIpv6InterfaceLinkLocalOnly_Type())
agentIpv6InterfaceLinkLocalOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6InterfaceLinkLocalOnly.setStatus(_A)
class _AgentIpv6InterfaceIcmpUnreachables_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6InterfaceIcmpUnreachables_Type.__name__=_B
_AgentIpv6InterfaceIcmpUnreachables_Object=MibTableColumn
agentIpv6InterfaceIcmpUnreachables=_AgentIpv6InterfaceIcmpUnreachables_Object((1,3,6,1,4,1,4413,1,1,30,1,2,1,5),_AgentIpv6InterfaceIcmpUnreachables_Type())
agentIpv6InterfaceIcmpUnreachables.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6InterfaceIcmpUnreachables.setStatus(_A)
_AgentIpv6RouterAdvertisementTable_Object=MibTable
agentIpv6RouterAdvertisementTable=_AgentIpv6RouterAdvertisementTable_Object((1,3,6,1,4,1,4413,1,1,30,1,3))
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementTable.setStatus(_A)
_AgentIpv6RouterAdvertisementEntry_Object=MibTableRow
agentIpv6RouterAdvertisementEntry=_AgentIpv6RouterAdvertisementEntry_Object((1,3,6,1,4,1,4413,1,1,30,1,3,1))
agentIpv6RouterAdvertisementEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementEntry.setStatus(_A)
class _AgentIpv6RouterAdvertisementIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIpv6RouterAdvertisementIfIndex_Type.__name__=_B
_AgentIpv6RouterAdvertisementIfIndex_Object=MibTableColumn
agentIpv6RouterAdvertisementIfIndex=_AgentIpv6RouterAdvertisementIfIndex_Object((1,3,6,1,4,1,4413,1,1,30,1,3,1,1),_AgentIpv6RouterAdvertisementIfIndex_Type())
agentIpv6RouterAdvertisementIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementIfIndex.setStatus(_A)
class _AgentIpv6RouterAdvertisementSuppressMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6RouterAdvertisementSuppressMode_Type.__name__=_B
_AgentIpv6RouterAdvertisementSuppressMode_Object=MibTableColumn
agentIpv6RouterAdvertisementSuppressMode=_AgentIpv6RouterAdvertisementSuppressMode_Object((1,3,6,1,4,1,4413,1,1,30,1,3,1,2),_AgentIpv6RouterAdvertisementSuppressMode_Type())
agentIpv6RouterAdvertisementSuppressMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementSuppressMode.setStatus(_A)
class _AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type.__name__=_B
_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Object=MibTableColumn
agentIpv6RouterAdvertisementMaxAdvertisementInterval=_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Object((1,3,6,1,4,1,4413,1,1,30,1,3,1,3),_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type())
agentIpv6RouterAdvertisementMaxAdvertisementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementMaxAdvertisementInterval.setStatus(_A)
class _AgentIpv6RouterAdvertisementAdvertisementLifetime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,65520))
_AgentIpv6RouterAdvertisementAdvertisementLifetime_Type.__name__=_B
_AgentIpv6RouterAdvertisementAdvertisementLifetime_Object=MibTableColumn
agentIpv6RouterAdvertisementAdvertisementLifetime=_AgentIpv6RouterAdvertisementAdvertisementLifetime_Object((1,3,6,1,4,1,4413,1,1,30,1,3,1,4),_AgentIpv6RouterAdvertisementAdvertisementLifetime_Type())
agentIpv6RouterAdvertisementAdvertisementLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementAdvertisementLifetime.setStatus(_A)
class _AgentIpv6RouterAdvertisementNbrSolicitInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_AgentIpv6RouterAdvertisementNbrSolicitInterval_Type.__name__=_B
_AgentIpv6RouterAdvertisementNbrSolicitInterval_Object=MibTableColumn
agentIpv6RouterAdvertisementNbrSolicitInterval=_AgentIpv6RouterAdvertisementNbrSolicitInterval_Object((1,3,6,1,4,1,4413,1,1,30,1,3,1,5),_AgentIpv6RouterAdvertisementNbrSolicitInterval_Type())
agentIpv6RouterAdvertisementNbrSolicitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementNbrSolicitInterval.setStatus(_A)
class _AgentIpv6RouterAdvertisementReachableTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_AgentIpv6RouterAdvertisementReachableTime_Type.__name__=_B
_AgentIpv6RouterAdvertisementReachableTime_Object=MibTableColumn
agentIpv6RouterAdvertisementReachableTime=_AgentIpv6RouterAdvertisementReachableTime_Object((1,3,6,1,4,1,4413,1,1,30,1,3,1,6),_AgentIpv6RouterAdvertisementReachableTime_Type())
agentIpv6RouterAdvertisementReachableTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementReachableTime.setStatus(_A)
class _AgentIpv6RouterAdvertisementManagedFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6RouterAdvertisementManagedFlag_Type.__name__=_B
_AgentIpv6RouterAdvertisementManagedFlag_Object=MibTableColumn
agentIpv6RouterAdvertisementManagedFlag=_AgentIpv6RouterAdvertisementManagedFlag_Object((1,3,6,1,4,1,4413,1,1,30,1,3,1,7),_AgentIpv6RouterAdvertisementManagedFlag_Type())
agentIpv6RouterAdvertisementManagedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementManagedFlag.setStatus(_A)
class _AgentIpv6RouterAdvertisementOtherFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpv6RouterAdvertisementOtherFlag_Type.__name__=_B
_AgentIpv6RouterAdvertisementOtherFlag_Object=MibTableColumn
agentIpv6RouterAdvertisementOtherFlag=_AgentIpv6RouterAdvertisementOtherFlag_Object((1,3,6,1,4,1,4413,1,1,30,1,3,1,8),_AgentIpv6RouterAdvertisementOtherFlag_Type())
agentIpv6RouterAdvertisementOtherFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6RouterAdvertisementOtherFlag.setStatus(_A)
_AgentIpv6AddrPrefixTable_Object=MibTable
agentIpv6AddrPrefixTable=_AgentIpv6AddrPrefixTable_Object((1,3,6,1,4,1,4413,1,1,30,1,4))
if mibBuilder.loadTexts:agentIpv6AddrPrefixTable.setStatus(_A)
_AgentIpv6AddrPrefixEntry_Object=MibTableRow
agentIpv6AddrPrefixEntry=_AgentIpv6AddrPrefixEntry_Object((1,3,6,1,4,1,4413,1,1,30,1,4,1))
agentIpv6AddrPrefixEntry.setIndexNames((0,_D,_J),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:agentIpv6AddrPrefixEntry.setStatus(_A)
_AgentIpv6AddrPrefix_Type=Ipv6AddressPrefix
_AgentIpv6AddrPrefix_Object=MibTableColumn
agentIpv6AddrPrefix=_AgentIpv6AddrPrefix_Object((1,3,6,1,4,1,4413,1,1,30,1,4,1,1),_AgentIpv6AddrPrefix_Type())
agentIpv6AddrPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6AddrPrefix.setStatus(_A)
class _AgentIpv6AddrPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6AddrPrefixLength_Type.__name__=_B
_AgentIpv6AddrPrefixLength_Object=MibTableColumn
agentIpv6AddrPrefixLength=_AgentIpv6AddrPrefixLength_Object((1,3,6,1,4,1,4413,1,1,30,1,4,1,2),_AgentIpv6AddrPrefixLength_Type())
agentIpv6AddrPrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6AddrPrefixLength.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPrefixLength.setUnits(_K)
_AgentIpv6AddrPrefixOnLinkFlag_Type=TruthValue
_AgentIpv6AddrPrefixOnLinkFlag_Object=MibTableColumn
agentIpv6AddrPrefixOnLinkFlag=_AgentIpv6AddrPrefixOnLinkFlag_Object((1,3,6,1,4,1,4413,1,1,30,1,4,1,3),_AgentIpv6AddrPrefixOnLinkFlag_Type())
agentIpv6AddrPrefixOnLinkFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6AddrPrefixOnLinkFlag.setStatus(_A)
_AgentIpv6AddrPrefixAutonomousFlag_Type=TruthValue
_AgentIpv6AddrPrefixAutonomousFlag_Object=MibTableColumn
agentIpv6AddrPrefixAutonomousFlag=_AgentIpv6AddrPrefixAutonomousFlag_Object((1,3,6,1,4,1,4413,1,1,30,1,4,1,4),_AgentIpv6AddrPrefixAutonomousFlag_Type())
agentIpv6AddrPrefixAutonomousFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAutonomousFlag.setStatus(_A)
_AgentIpv6AddrPrefixAdvPreferredLifetime_Type=Unsigned32
_AgentIpv6AddrPrefixAdvPreferredLifetime_Object=MibTableColumn
agentIpv6AddrPrefixAdvPreferredLifetime=_AgentIpv6AddrPrefixAdvPreferredLifetime_Object((1,3,6,1,4,1,4413,1,1,30,1,4,1,5),_AgentIpv6AddrPrefixAdvPreferredLifetime_Type())
agentIpv6AddrPrefixAdvPreferredLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvPreferredLifetime.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvPreferredLifetime.setUnits(_P)
_AgentIpv6AddrPrefixAdvValidLifetime_Type=Unsigned32
_AgentIpv6AddrPrefixAdvValidLifetime_Object=MibTableColumn
agentIpv6AddrPrefixAdvValidLifetime=_AgentIpv6AddrPrefixAdvValidLifetime_Object((1,3,6,1,4,1,4413,1,1,30,1,4,1,6),_AgentIpv6AddrPrefixAdvValidLifetime_Type())
agentIpv6AddrPrefixAdvValidLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvValidLifetime.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPrefixAdvValidLifetime.setUnits(_P)
_AgentIpv6AddrTable_Object=MibTable
agentIpv6AddrTable=_AgentIpv6AddrTable_Object((1,3,6,1,4,1,4413,1,1,30,1,5))
if mibBuilder.loadTexts:agentIpv6AddrTable.setStatus(_A)
_AgentIpv6AddrEntry_Object=MibTableRow
agentIpv6AddrEntry=_AgentIpv6AddrEntry_Object((1,3,6,1,4,1,4413,1,1,30,1,5,1))
agentIpv6AddrEntry.setIndexNames((0,_D,_J),(0,_D,_Q))
if mibBuilder.loadTexts:agentIpv6AddrEntry.setStatus(_A)
_AgentIpv6AddrAddress_Type=Ipv6Address
_AgentIpv6AddrAddress_Object=MibTableColumn
agentIpv6AddrAddress=_AgentIpv6AddrAddress_Object((1,3,6,1,4,1,4413,1,1,30,1,5,1,1),_AgentIpv6AddrAddress_Type())
agentIpv6AddrAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6AddrAddress.setStatus(_A)
class _AgentIpv6AddrPfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6AddrPfxLength_Type.__name__=_B
_AgentIpv6AddrPfxLength_Object=MibTableColumn
agentIpv6AddrPfxLength=_AgentIpv6AddrPfxLength_Object((1,3,6,1,4,1,4413,1,1,30,1,5,1,2),_AgentIpv6AddrPfxLength_Type())
agentIpv6AddrPfxLength.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6AddrPfxLength.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6AddrPfxLength.setUnits(_K)
_AgentIpv6AddrEui64Flag_Type=TruthValue
_AgentIpv6AddrEui64Flag_Object=MibTableColumn
agentIpv6AddrEui64Flag=_AgentIpv6AddrEui64Flag_Object((1,3,6,1,4,1,4413,1,1,30,1,5,1,3),_AgentIpv6AddrEui64Flag_Type())
agentIpv6AddrEui64Flag.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6AddrEui64Flag.setStatus(_A)
_AgentIpv6AddrStatus_Type=RowStatus
_AgentIpv6AddrStatus_Object=MibTableColumn
agentIpv6AddrStatus=_AgentIpv6AddrStatus_Object((1,3,6,1,4,1,4413,1,1,30,1,5,1,4),_AgentIpv6AddrStatus_Type())
agentIpv6AddrStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6AddrStatus.setStatus(_A)
_AgentIpv6StaticRouteTable_Object=MibTable
agentIpv6StaticRouteTable=_AgentIpv6StaticRouteTable_Object((1,3,6,1,4,1,4413,1,1,30,1,6))
if mibBuilder.loadTexts:agentIpv6StaticRouteTable.setStatus(_A)
_AgentIpv6StaticRouteEntry_Object=MibTableRow
agentIpv6StaticRouteEntry=_AgentIpv6StaticRouteEntry_Object((1,3,6,1,4,1,4413,1,1,30,1,6,1))
agentIpv6StaticRouteEntry.setIndexNames((0,_D,_R),(0,_D,_S),(0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:agentIpv6StaticRouteEntry.setStatus(_A)
_AgentIpv6StaticRouteDest_Type=Ipv6AddressPrefix
_AgentIpv6StaticRouteDest_Object=MibTableColumn
agentIpv6StaticRouteDest=_AgentIpv6StaticRouteDest_Object((1,3,6,1,4,1,4413,1,1,30,1,6,1,1),_AgentIpv6StaticRouteDest_Type())
agentIpv6StaticRouteDest.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6StaticRouteDest.setStatus(_A)
class _AgentIpv6StaticRoutePfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentIpv6StaticRoutePfxLength_Type.__name__=_B
_AgentIpv6StaticRoutePfxLength_Object=MibTableColumn
agentIpv6StaticRoutePfxLength=_AgentIpv6StaticRoutePfxLength_Object((1,3,6,1,4,1,4413,1,1,30,1,6,1,2),_AgentIpv6StaticRoutePfxLength_Type())
agentIpv6StaticRoutePfxLength.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6StaticRoutePfxLength.setStatus(_A)
if mibBuilder.loadTexts:agentIpv6StaticRoutePfxLength.setUnits(_K)
_AgentIpv6StaticRouteIfIndex_Type=Ipv6IfIndexOrZero
_AgentIpv6StaticRouteIfIndex_Object=MibTableColumn
agentIpv6StaticRouteIfIndex=_AgentIpv6StaticRouteIfIndex_Object((1,3,6,1,4,1,4413,1,1,30,1,6,1,3),_AgentIpv6StaticRouteIfIndex_Type())
agentIpv6StaticRouteIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6StaticRouteIfIndex.setStatus(_A)
_AgentIpv6StaticRouteNextHop_Type=Ipv6Address
_AgentIpv6StaticRouteNextHop_Object=MibTableColumn
agentIpv6StaticRouteNextHop=_AgentIpv6StaticRouteNextHop_Object((1,3,6,1,4,1,4413,1,1,30,1,6,1,4),_AgentIpv6StaticRouteNextHop_Type())
agentIpv6StaticRouteNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6StaticRouteNextHop.setStatus(_A)
class _AgentIpv6StaticRoutePreference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentIpv6StaticRoutePreference_Type.__name__=_B
_AgentIpv6StaticRoutePreference_Object=MibTableColumn
agentIpv6StaticRoutePreference=_AgentIpv6StaticRoutePreference_Object((1,3,6,1,4,1,4413,1,1,30,1,6,1,5),_AgentIpv6StaticRoutePreference_Type())
agentIpv6StaticRoutePreference.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6StaticRoutePreference.setStatus(_A)
_AgentIpv6StaticRouteStatus_Type=RowStatus
_AgentIpv6StaticRouteStatus_Object=MibTableColumn
agentIpv6StaticRouteStatus=_AgentIpv6StaticRouteStatus_Object((1,3,6,1,4,1,4413,1,1,30,1,6,1,6),_AgentIpv6StaticRouteStatus_Type())
agentIpv6StaticRouteStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpv6StaticRouteStatus.setStatus(_A)
_AgentIpv6ServicePortGroup_ObjectIdentity=ObjectIdentity
agentIpv6ServicePortGroup=_AgentIpv6ServicePortGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,30,1,7))
_AgentIpv6ServicePortPrefixTable_Object=MibTable
agentIpv6ServicePortPrefixTable=_AgentIpv6ServicePortPrefixTable_Object((1,3,6,1,4,1,4413,1,1,30,1,7,1))
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixTable.setStatus(_A)
_AgentIpv6ServicePortPrefixEntry_Object=MibTableRow
agentIpv6ServicePortPrefixEntry=_AgentIpv6ServicePortPrefixEntry_Object((1,3,6,1,4,1,4413,1,1,30,1,7,1,1))
agentIpv6ServicePortPrefixEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixEntry.setStatus(_A)
_AgentIpv6ServicePortPrefixIndex_Type=Unsigned32
_AgentIpv6ServicePortPrefixIndex_Object=MibTableColumn
agentIpv6ServicePortPrefixIndex=_AgentIpv6ServicePortPrefixIndex_Object((1,3,6,1,4,1,4413,1,1,30,1,7,1,1,1),_AgentIpv6ServicePortPrefixIndex_Type())
agentIpv6ServicePortPrefixIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixIndex.setStatus(_A)
_AgentIpv6ServicePortPrefix_Type=Ipv6Address
_AgentIpv6ServicePortPrefix_Object=MibTableColumn
agentIpv6ServicePortPrefix=_AgentIpv6ServicePortPrefix_Object((1,3,6,1,4,1,4413,1,1,30,1,7,1,1,2),_AgentIpv6ServicePortPrefix_Type())
agentIpv6ServicePortPrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortPrefix.setStatus(_A)
_AgentIpv6ServicePortPrefixLength_Type=Unsigned32
_AgentIpv6ServicePortPrefixLength_Object=MibTableColumn
agentIpv6ServicePortPrefixLength=_AgentIpv6ServicePortPrefixLength_Object((1,3,6,1,4,1,4413,1,1,30,1,7,1,1,3),_AgentIpv6ServicePortPrefixLength_Type())
agentIpv6ServicePortPrefixLength.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortPrefixLength.setStatus(_A)
_AgentIpv6ServicePortDefaultRouterTable_Object=MibTable
agentIpv6ServicePortDefaultRouterTable=_AgentIpv6ServicePortDefaultRouterTable_Object((1,3,6,1,4,1,4413,1,1,30,1,7,2))
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouterTable.setStatus(_A)
_AgentIpv6ServicePortDefaultRouterEntry_Object=MibTableRow
agentIpv6ServicePortDefaultRouterEntry=_AgentIpv6ServicePortDefaultRouterEntry_Object((1,3,6,1,4,1,4413,1,1,30,1,7,2,1))
agentIpv6ServicePortDefaultRouterEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouterEntry.setStatus(_A)
_AgentIpv6ServicePortDefaultRouterIndex_Type=Unsigned32
_AgentIpv6ServicePortDefaultRouterIndex_Object=MibTableColumn
agentIpv6ServicePortDefaultRouterIndex=_AgentIpv6ServicePortDefaultRouterIndex_Object((1,3,6,1,4,1,4413,1,1,30,1,7,2,1,1),_AgentIpv6ServicePortDefaultRouterIndex_Type())
agentIpv6ServicePortDefaultRouterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouterIndex.setStatus(_A)
_AgentIpv6ServicePortDefaultRouter_Type=Ipv6Address
_AgentIpv6ServicePortDefaultRouter_Object=MibTableColumn
agentIpv6ServicePortDefaultRouter=_AgentIpv6ServicePortDefaultRouter_Object((1,3,6,1,4,1,4413,1,1,30,1,7,2,1,2),_AgentIpv6ServicePortDefaultRouter_Type())
agentIpv6ServicePortDefaultRouter.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortDefaultRouter.setStatus(_A)
_AgentIpv6ServicePortNbrTable_Object=MibTable
agentIpv6ServicePortNbrTable=_AgentIpv6ServicePortNbrTable_Object((1,3,6,1,4,1,4413,1,1,30,1,7,3))
if mibBuilder.loadTexts:agentIpv6ServicePortNbrTable.setStatus(_A)
_AgentIpv6ServicePortNbrEntry_Object=MibTableRow
agentIpv6ServicePortNbrEntry=_AgentIpv6ServicePortNbrEntry_Object((1,3,6,1,4,1,4413,1,1,30,1,7,3,1))
agentIpv6ServicePortNbrEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:agentIpv6ServicePortNbrEntry.setStatus(_A)
_AgentIpv6ServicePortNbrAddr_Type=Ipv6Address
_AgentIpv6ServicePortNbrAddr_Object=MibTableColumn
agentIpv6ServicePortNbrAddr=_AgentIpv6ServicePortNbrAddr_Object((1,3,6,1,4,1,4413,1,1,30,1,7,3,1,1),_AgentIpv6ServicePortNbrAddr_Type())
agentIpv6ServicePortNbrAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrAddr.setStatus(_A)
_AgentIpv6ServicePortNbrPhysAddr_Type=MacAddress
_AgentIpv6ServicePortNbrPhysAddr_Object=MibTableColumn
agentIpv6ServicePortNbrPhysAddr=_AgentIpv6ServicePortNbrPhysAddr_Object((1,3,6,1,4,1,4413,1,1,30,1,7,3,1,2),_AgentIpv6ServicePortNbrPhysAddr_Type())
agentIpv6ServicePortNbrPhysAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrPhysAddr.setStatus(_A)
class _AgentIpv6ServicePortNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6)));namedValues=NamedValues(*(('reachable',1),('stale',2),('delay',3),('probe',4),('unknown',6)))
_AgentIpv6ServicePortNbrState_Type.__name__=_B
_AgentIpv6ServicePortNbrState_Object=MibTableColumn
agentIpv6ServicePortNbrState=_AgentIpv6ServicePortNbrState_Object((1,3,6,1,4,1,4413,1,1,30,1,7,3,1,3),_AgentIpv6ServicePortNbrState_Type())
agentIpv6ServicePortNbrState.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrState.setStatus(_A)
_AgentIpv6ServicePortNbrUpdated_Type=TimeStamp
_AgentIpv6ServicePortNbrUpdated_Object=MibTableColumn
agentIpv6ServicePortNbrUpdated=_AgentIpv6ServicePortNbrUpdated_Object((1,3,6,1,4,1,4413,1,1,30,1,7,3,1,4),_AgentIpv6ServicePortNbrUpdated_Type())
agentIpv6ServicePortNbrUpdated.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrUpdated.setStatus(_A)
_AgentIpv6ServicePortNbrIsRouter_Type=TruthValue
_AgentIpv6ServicePortNbrIsRouter_Object=MibTableColumn
agentIpv6ServicePortNbrIsRouter=_AgentIpv6ServicePortNbrIsRouter_Object((1,3,6,1,4,1,4413,1,1,30,1,7,3,1,5),_AgentIpv6ServicePortNbrIsRouter_Type())
agentIpv6ServicePortNbrIsRouter.setMaxAccess(_F)
if mibBuilder.loadTexts:agentIpv6ServicePortNbrIsRouter.setStatus(_A)
_AgentIpv6IcmpControlGroup_ObjectIdentity=ObjectIdentity
agentIpv6IcmpControlGroup=_AgentIpv6IcmpControlGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,30,1,8))
class _AgentIpv6IcmpRateLimitInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentIpv6IcmpRateLimitInterval_Type.__name__=_B
_AgentIpv6IcmpRateLimitInterval_Object=MibScalar
agentIpv6IcmpRateLimitInterval=_AgentIpv6IcmpRateLimitInterval_Object((1,3,6,1,4,1,4413,1,1,30,1,8,1),_AgentIpv6IcmpRateLimitInterval_Type())
agentIpv6IcmpRateLimitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6IcmpRateLimitInterval.setStatus(_A)
class _AgentIpv6IcmpRateLimitBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_AgentIpv6IcmpRateLimitBurstSize_Type.__name__=_B
_AgentIpv6IcmpRateLimitBurstSize_Object=MibScalar
agentIpv6IcmpRateLimitBurstSize=_AgentIpv6IcmpRateLimitBurstSize_Object((1,3,6,1,4,1,4413,1,1,30,1,8,2),_AgentIpv6IcmpRateLimitBurstSize_Type())
agentIpv6IcmpRateLimitBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpv6IcmpRateLimitBurstSize.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathRoutingIpv6':fastPathRoutingIpv6,'agentIpv6Group':agentIpv6Group,'agentIpv6RoutingMode':agentIpv6RoutingMode,'agentIpv6InterfaceTable':agentIpv6InterfaceTable,'agentIpv6InterfaceEntry':agentIpv6InterfaceEntry,_J:agentIpv6InterfaceIfIndex,'agentIpv6InterfaceMtuValue':agentIpv6InterfaceMtuValue,'agentIpv6InterfaceDadTransmits':agentIpv6InterfaceDadTransmits,'agentIpv6InterfaceLinkLocalOnly':agentIpv6InterfaceLinkLocalOnly,'agentIpv6InterfaceIcmpUnreachables':agentIpv6InterfaceIcmpUnreachables,'agentIpv6RouterAdvertisementTable':agentIpv6RouterAdvertisementTable,'agentIpv6RouterAdvertisementEntry':agentIpv6RouterAdvertisementEntry,_M:agentIpv6RouterAdvertisementIfIndex,'agentIpv6RouterAdvertisementSuppressMode':agentIpv6RouterAdvertisementSuppressMode,'agentIpv6RouterAdvertisementMaxAdvertisementInterval':agentIpv6RouterAdvertisementMaxAdvertisementInterval,'agentIpv6RouterAdvertisementAdvertisementLifetime':agentIpv6RouterAdvertisementAdvertisementLifetime,'agentIpv6RouterAdvertisementNbrSolicitInterval':agentIpv6RouterAdvertisementNbrSolicitInterval,'agentIpv6RouterAdvertisementReachableTime':agentIpv6RouterAdvertisementReachableTime,'agentIpv6RouterAdvertisementManagedFlag':agentIpv6RouterAdvertisementManagedFlag,'agentIpv6RouterAdvertisementOtherFlag':agentIpv6RouterAdvertisementOtherFlag,'agentIpv6AddrPrefixTable':agentIpv6AddrPrefixTable,'agentIpv6AddrPrefixEntry':agentIpv6AddrPrefixEntry,_N:agentIpv6AddrPrefix,_O:agentIpv6AddrPrefixLength,'agentIpv6AddrPrefixOnLinkFlag':agentIpv6AddrPrefixOnLinkFlag,'agentIpv6AddrPrefixAutonomousFlag':agentIpv6AddrPrefixAutonomousFlag,'agentIpv6AddrPrefixAdvPreferredLifetime':agentIpv6AddrPrefixAdvPreferredLifetime,'agentIpv6AddrPrefixAdvValidLifetime':agentIpv6AddrPrefixAdvValidLifetime,'agentIpv6AddrTable':agentIpv6AddrTable,'agentIpv6AddrEntry':agentIpv6AddrEntry,_Q:agentIpv6AddrAddress,'agentIpv6AddrPfxLength':agentIpv6AddrPfxLength,'agentIpv6AddrEui64Flag':agentIpv6AddrEui64Flag,'agentIpv6AddrStatus':agentIpv6AddrStatus,'agentIpv6StaticRouteTable':agentIpv6StaticRouteTable,'agentIpv6StaticRouteEntry':agentIpv6StaticRouteEntry,_R:agentIpv6StaticRouteDest,_S:agentIpv6StaticRoutePfxLength,_T:agentIpv6StaticRouteIfIndex,_U:agentIpv6StaticRouteNextHop,'agentIpv6StaticRoutePreference':agentIpv6StaticRoutePreference,'agentIpv6StaticRouteStatus':agentIpv6StaticRouteStatus,'agentIpv6ServicePortGroup':agentIpv6ServicePortGroup,'agentIpv6ServicePortPrefixTable':agentIpv6ServicePortPrefixTable,'agentIpv6ServicePortPrefixEntry':agentIpv6ServicePortPrefixEntry,_V:agentIpv6ServicePortPrefixIndex,'agentIpv6ServicePortPrefix':agentIpv6ServicePortPrefix,'agentIpv6ServicePortPrefixLength':agentIpv6ServicePortPrefixLength,'agentIpv6ServicePortDefaultRouterTable':agentIpv6ServicePortDefaultRouterTable,'agentIpv6ServicePortDefaultRouterEntry':agentIpv6ServicePortDefaultRouterEntry,_W:agentIpv6ServicePortDefaultRouterIndex,'agentIpv6ServicePortDefaultRouter':agentIpv6ServicePortDefaultRouter,'agentIpv6ServicePortNbrTable':agentIpv6ServicePortNbrTable,'agentIpv6ServicePortNbrEntry':agentIpv6ServicePortNbrEntry,_X:agentIpv6ServicePortNbrAddr,'agentIpv6ServicePortNbrPhysAddr':agentIpv6ServicePortNbrPhysAddr,'agentIpv6ServicePortNbrState':agentIpv6ServicePortNbrState,'agentIpv6ServicePortNbrUpdated':agentIpv6ServicePortNbrUpdated,'agentIpv6ServicePortNbrIsRouter':agentIpv6ServicePortNbrIsRouter,'agentIpv6IcmpControlGroup':agentIpv6IcmpControlGroup,'agentIpv6IcmpRateLimitInterval':agentIpv6IcmpRateLimitInterval,'agentIpv6IcmpRateLimitBurstSize':agentIpv6IcmpRateLimitBurstSize})