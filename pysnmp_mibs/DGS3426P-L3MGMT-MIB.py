_n='swL3RouteRedistriDstProtocol'
_m='swL3RouteRedistriSrcProtocol'
_l='swL3RelayDnsCtrlIpAddr'
_k='swL3RelayDnsCtrlDomainName'
_j='swL3DHCPRelayOption61ClientID'
_i='swL3DHCPRelayOption61ClientType'
_h='swL3DHCPRelayOption60RelayIp'
_g='swL3DHCPRelayOption60String'
_f='swL3DHCPRelayOption60DefRelayIp'
_e='swL3RelayDhcpCtrlServer'
_d='swL3RelayDhcpCtrlInterfaceName'
_c='swL3IpStaticRouteNextHop'
_b='swL3IpStaticRouteMask'
_a='swL3IpStaticRouteDest'
_Z='static'
_Y='swL3IpFdbInfoIpAddr'
_X='swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen'
_W='swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr'
_V='swL3Ipv6DHCPv6CPDAddrCtrlPrefixName'
_U='swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName'
_T='swL3Ipv6AddressCtrlPrefixLen'
_S='swL3Ipv6Address'
_R='swL3Ipv6AddressCtrlInterfaceName'
_Q='swL3Ipv6CtrlInterfaceName'
_P='swL3IpCtrlInterfaceName'
_O='relay'
_N='valid'
_M='invalid'
_L='drop'
_K='Unsigned32'
_J='DisplayString'
_I='other'
_H='read-create'
_G='enabled'
_F='disabled'
_E='DGS3426P-L3MGMT-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
dgs3426p,=mibBuilder.importSymbols('SW34XXPRIMGMT-MIB','dgs3426p')
swL3MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,70,7,3))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwL3DevMgmt_ObjectIdentity=ObjectIdentity
swL3DevMgmt=_SwL3DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,1))
_SwL3DevCtrl_ObjectIdentity=ObjectIdentity
swL3DevCtrl=_SwL3DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,1,1))
class _SwL3DevCtrlRIPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_F,2),(_G,3)))
_SwL3DevCtrlRIPState_Type.__name__=_B
_SwL3DevCtrlRIPState_Object=MibScalar
swL3DevCtrlRIPState=_SwL3DevCtrlRIPState_Object((1,3,6,1,4,1,171,11,70,7,3,1,1,1),_SwL3DevCtrlRIPState_Type())
swL3DevCtrlRIPState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3DevCtrlRIPState.setStatus(_A)
_SwL3IpMgmt_ObjectIdentity=ObjectIdentity
swL3IpMgmt=_SwL3IpMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,2))
_SwL3IpCtrlMgmt_ObjectIdentity=ObjectIdentity
swL3IpCtrlMgmt=_SwL3IpCtrlMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,2,1))
_SwL3IpCtrlTable_Object=MibTable
swL3IpCtrlTable=_SwL3IpCtrlTable_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3))
if mibBuilder.loadTexts:swL3IpCtrlTable.setStatus(_A)
_SwL3IpCtrlEntry_Object=MibTableRow
swL3IpCtrlEntry=_SwL3IpCtrlEntry_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1))
swL3IpCtrlEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:swL3IpCtrlEntry.setStatus(_A)
class _SwL3IpCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3IpCtrlInterfaceName_Type.__name__=_J
_SwL3IpCtrlInterfaceName_Object=MibTableColumn
swL3IpCtrlInterfaceName=_SwL3IpCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,1),_SwL3IpCtrlInterfaceName_Type())
swL3IpCtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlInterfaceName.setStatus(_A)
class _SwL3IpCtrlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpCtrlIfIndex_Type.__name__=_B
_SwL3IpCtrlIfIndex_Object=MibTableColumn
swL3IpCtrlIfIndex=_SwL3IpCtrlIfIndex_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,2),_SwL3IpCtrlIfIndex_Type())
swL3IpCtrlIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIfIndex.setStatus(_A)
_SwL3IpCtrlIpAddr_Type=IpAddress
_SwL3IpCtrlIpAddr_Object=MibTableColumn
swL3IpCtrlIpAddr=_SwL3IpCtrlIpAddr_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,3),_SwL3IpCtrlIpAddr_Type())
swL3IpCtrlIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIpAddr.setStatus(_A)
_SwL3IpCtrlIpSubnetMask_Type=IpAddress
_SwL3IpCtrlIpSubnetMask_Object=MibTableColumn
swL3IpCtrlIpSubnetMask=_SwL3IpCtrlIpSubnetMask_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,4),_SwL3IpCtrlIpSubnetMask_Type())
swL3IpCtrlIpSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIpSubnetMask.setStatus(_A)
class _SwL3IpCtrlVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL3IpCtrlVlanName_Type.__name__=_J
_SwL3IpCtrlVlanName_Object=MibTableColumn
swL3IpCtrlVlanName=_SwL3IpCtrlVlanName_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,5),_SwL3IpCtrlVlanName_Type())
swL3IpCtrlVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlVlanName.setStatus(_A)
class _SwL3IpCtrlProxyArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3IpCtrlProxyArp_Type.__name__=_B
_SwL3IpCtrlProxyArp_Object=MibTableColumn
swL3IpCtrlProxyArp=_SwL3IpCtrlProxyArp_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,6),_SwL3IpCtrlProxyArp_Type())
swL3IpCtrlProxyArp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlProxyArp.setStatus(_A)
_SwL3IpCtrlSecondary_Type=TruthValue
_SwL3IpCtrlSecondary_Object=MibTableColumn
swL3IpCtrlSecondary=_SwL3IpCtrlSecondary_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,7),_SwL3IpCtrlSecondary_Type())
swL3IpCtrlSecondary.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlSecondary.setStatus(_A)
class _SwL3IpCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_I,1),('bootp',3),('dhcp',4)))
_SwL3IpCtrlMode_Type.__name__=_B
_SwL3IpCtrlMode_Object=MibTableColumn
swL3IpCtrlMode=_SwL3IpCtrlMode_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,8),_SwL3IpCtrlMode_Type())
swL3IpCtrlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlMode.setStatus(_A)
class _SwL3IpCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3IpCtrlAdminState_Type.__name__=_B
_SwL3IpCtrlAdminState_Object=MibTableColumn
swL3IpCtrlAdminState=_SwL3IpCtrlAdminState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,9),_SwL3IpCtrlAdminState_Type())
swL3IpCtrlAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlAdminState.setStatus(_A)
_SwL3IpCtrlIpv6LinkLocalAddress_Type=Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress=_SwL3IpCtrlIpv6LinkLocalAddress_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,14),_SwL3IpCtrlIpv6LinkLocalAddress_Type())
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalAddress.setStatus(_A)
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type=Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen=_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,15),_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type())
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus(_A)
_SwL3IpCtrlState_Type=RowStatus
_SwL3IpCtrlState_Object=MibTableColumn
swL3IpCtrlState=_SwL3IpCtrlState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,16),_SwL3IpCtrlState_Type())
swL3IpCtrlState.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3IpCtrlState.setStatus(_A)
class _SwL3IpCtrlIpv6LinkLocalAutoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_F,3)))
_SwL3IpCtrlIpv6LinkLocalAutoState_Type.__name__=_B
_SwL3IpCtrlIpv6LinkLocalAutoState_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalAutoState=_SwL3IpCtrlIpv6LinkLocalAutoState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,17),_SwL3IpCtrlIpv6LinkLocalAutoState_Type())
swL3IpCtrlIpv6LinkLocalAutoState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalAutoState.setStatus(_A)
class _SwL3IpCtrlLocalProxyArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3IpCtrlLocalProxyArp_Type.__name__=_B
_SwL3IpCtrlLocalProxyArp_Object=MibTableColumn
swL3IpCtrlLocalProxyArp=_SwL3IpCtrlLocalProxyArp_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,18),_SwL3IpCtrlLocalProxyArp_Type())
swL3IpCtrlLocalProxyArp.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3IpCtrlLocalProxyArp.setStatus(_A)
class _SwL3IpCtrlDhcpv6ClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3IpCtrlDhcpv6ClientState_Type.__name__=_B
_SwL3IpCtrlDhcpv6ClientState_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientState=_SwL3IpCtrlDhcpv6ClientState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,20),_SwL3IpCtrlDhcpv6ClientState_Type())
swL3IpCtrlDhcpv6ClientState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientState.setStatus(_A)
class _SwL3IpCtrlIpDirectedBroadcastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3IpCtrlIpDirectedBroadcastState_Type.__name__=_B
_SwL3IpCtrlIpDirectedBroadcastState_Object=MibTableColumn
swL3IpCtrlIpDirectedBroadcastState=_SwL3IpCtrlIpDirectedBroadcastState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,21),_SwL3IpCtrlIpDirectedBroadcastState_Type())
swL3IpCtrlIpDirectedBroadcastState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIpDirectedBroadcastState.setStatus(_A)
class _SwL3IpCtrlIpDhcpOption12State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3IpCtrlIpDhcpOption12State_Type.__name__=_B
_SwL3IpCtrlIpDhcpOption12State_Object=MibTableColumn
swL3IpCtrlIpDhcpOption12State=_SwL3IpCtrlIpDhcpOption12State_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,22),_SwL3IpCtrlIpDhcpOption12State_Type())
swL3IpCtrlIpDhcpOption12State.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIpDhcpOption12State.setStatus(_A)
class _SwL3IpCtrlIpDhcpOption12HostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_SwL3IpCtrlIpDhcpOption12HostName_Type.__name__=_J
_SwL3IpCtrlIpDhcpOption12HostName_Object=MibTableColumn
swL3IpCtrlIpDhcpOption12HostName=_SwL3IpCtrlIpDhcpOption12HostName_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,23),_SwL3IpCtrlIpDhcpOption12HostName_Type())
swL3IpCtrlIpDhcpOption12HostName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIpDhcpOption12HostName.setStatus(_A)
class _SwL3IpCtrlDhcpv6ClientPDState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3IpCtrlDhcpv6ClientPDState_Type.__name__=_B
_SwL3IpCtrlDhcpv6ClientPDState_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientPDState=_SwL3IpCtrlDhcpv6ClientPDState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,24),_SwL3IpCtrlDhcpv6ClientPDState_Type())
swL3IpCtrlDhcpv6ClientPDState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientPDState.setStatus(_A)
class _SwL3IpCtrlDhcpv6ClientPDPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwL3IpCtrlDhcpv6ClientPDPrefixName_Type.__name__=_J
_SwL3IpCtrlDhcpv6ClientPDPrefixName_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefixName=_SwL3IpCtrlDhcpv6ClientPDPrefixName_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,25),_SwL3IpCtrlDhcpv6ClientPDPrefixName_Type())
swL3IpCtrlDhcpv6ClientPDPrefixName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientPDPrefixName.setStatus(_A)
_SwL3IpCtrlDhcpv6ClientPDPrefix_Type=Ipv6Address
_SwL3IpCtrlDhcpv6ClientPDPrefix_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefix=_SwL3IpCtrlDhcpv6ClientPDPrefix_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,26),_SwL3IpCtrlDhcpv6ClientPDPrefix_Type())
swL3IpCtrlDhcpv6ClientPDPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientPDPrefix.setStatus(_A)
_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Type=Integer32
_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefixLen=_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,3,1,27),_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Type())
swL3IpCtrlDhcpv6ClientPDPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientPDPrefixLen.setStatus(_A)
_SwL3Ipv6CtrlTable_Object=MibTable
swL3Ipv6CtrlTable=_SwL3Ipv6CtrlTable_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4))
if mibBuilder.loadTexts:swL3Ipv6CtrlTable.setStatus(_A)
_SwL3Ipv6CtrlEntry_Object=MibTableRow
swL3Ipv6CtrlEntry=_SwL3Ipv6CtrlEntry_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1))
swL3Ipv6CtrlEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:swL3Ipv6CtrlEntry.setStatus(_A)
class _SwL3Ipv6CtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6CtrlInterfaceName_Type.__name__=_J
_SwL3Ipv6CtrlInterfaceName_Object=MibTableColumn
swL3Ipv6CtrlInterfaceName=_SwL3Ipv6CtrlInterfaceName_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,1),_SwL3Ipv6CtrlInterfaceName_Type())
swL3Ipv6CtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlInterfaceName.setStatus(_A)
_SwL3Ipv6CtrlMaxReassmblySize_Type=Integer32
_SwL3Ipv6CtrlMaxReassmblySize_Object=MibTableColumn
swL3Ipv6CtrlMaxReassmblySize=_SwL3Ipv6CtrlMaxReassmblySize_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,2),_SwL3Ipv6CtrlMaxReassmblySize_Type())
swL3Ipv6CtrlMaxReassmblySize.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlMaxReassmblySize.setStatus(_A)
class _SwL3Ipv6CtrlNsRetransTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwL3Ipv6CtrlNsRetransTimer_Type.__name__=_K
_SwL3Ipv6CtrlNsRetransTimer_Object=MibTableColumn
swL3Ipv6CtrlNsRetransTimer=_SwL3Ipv6CtrlNsRetransTimer_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,3),_SwL3Ipv6CtrlNsRetransTimer_Type())
swL3Ipv6CtrlNsRetransTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlNsRetransTimer.setStatus(_A)
class _SwL3Ipv6CtrlRaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3Ipv6CtrlRaState_Type.__name__=_B
_SwL3Ipv6CtrlRaState_Object=MibTableColumn
swL3Ipv6CtrlRaState=_SwL3Ipv6CtrlRaState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,5),_SwL3Ipv6CtrlRaState_Type())
swL3Ipv6CtrlRaState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaState.setStatus(_A)
class _SwL3Ipv6CtrlRaMinRtrAdvInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1350))
_SwL3Ipv6CtrlRaMinRtrAdvInterval_Type.__name__=_B
_SwL3Ipv6CtrlRaMinRtrAdvInterval_Object=MibTableColumn
swL3Ipv6CtrlRaMinRtrAdvInterval=_SwL3Ipv6CtrlRaMinRtrAdvInterval_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,6),_SwL3Ipv6CtrlRaMinRtrAdvInterval_Type())
swL3Ipv6CtrlRaMinRtrAdvInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaMinRtrAdvInterval.setStatus(_A)
class _SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type.__name__=_B
_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object=MibTableColumn
swL3Ipv6CtrlRaMaxRtrAdvInterval=_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,7),_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type())
swL3Ipv6CtrlRaMaxRtrAdvInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaMaxRtrAdvInterval.setStatus(_A)
class _SwL3Ipv6CtrlRaLifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_SwL3Ipv6CtrlRaLifeTime_Type.__name__=_B
_SwL3Ipv6CtrlRaLifeTime_Object=MibTableColumn
swL3Ipv6CtrlRaLifeTime=_SwL3Ipv6CtrlRaLifeTime_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,8),_SwL3Ipv6CtrlRaLifeTime_Type())
swL3Ipv6CtrlRaLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaLifeTime.setStatus(_A)
class _SwL3Ipv6CtrlRaReachableTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_SwL3Ipv6CtrlRaReachableTime_Type.__name__=_B
_SwL3Ipv6CtrlRaReachableTime_Object=MibTableColumn
swL3Ipv6CtrlRaReachableTime=_SwL3Ipv6CtrlRaReachableTime_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,9),_SwL3Ipv6CtrlRaReachableTime_Type())
swL3Ipv6CtrlRaReachableTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaReachableTime.setStatus(_A)
class _SwL3Ipv6CtrlRaRetransTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwL3Ipv6CtrlRaRetransTime_Type.__name__=_K
_SwL3Ipv6CtrlRaRetransTime_Object=MibTableColumn
swL3Ipv6CtrlRaRetransTime=_SwL3Ipv6CtrlRaRetransTime_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,10),_SwL3Ipv6CtrlRaRetransTime_Type())
swL3Ipv6CtrlRaRetransTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaRetransTime.setStatus(_A)
class _SwL3Ipv6CtrlRaHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3Ipv6CtrlRaHopLimit_Type.__name__=_B
_SwL3Ipv6CtrlRaHopLimit_Object=MibTableColumn
swL3Ipv6CtrlRaHopLimit=_SwL3Ipv6CtrlRaHopLimit_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,11),_SwL3Ipv6CtrlRaHopLimit_Type())
swL3Ipv6CtrlRaHopLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaHopLimit.setStatus(_A)
class _SwL3Ipv6CtrlRaManagedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3Ipv6CtrlRaManagedFlag_Type.__name__=_B
_SwL3Ipv6CtrlRaManagedFlag_Object=MibTableColumn
swL3Ipv6CtrlRaManagedFlag=_SwL3Ipv6CtrlRaManagedFlag_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,12),_SwL3Ipv6CtrlRaManagedFlag_Type())
swL3Ipv6CtrlRaManagedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaManagedFlag.setStatus(_A)
class _SwL3Ipv6CtrlRaOtherConfigFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3Ipv6CtrlRaOtherConfigFlag_Type.__name__=_B
_SwL3Ipv6CtrlRaOtherConfigFlag_Object=MibTableColumn
swL3Ipv6CtrlRaOtherConfigFlag=_SwL3Ipv6CtrlRaOtherConfigFlag_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,4,1,13),_SwL3Ipv6CtrlRaOtherConfigFlag_Type())
swL3Ipv6CtrlRaOtherConfigFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaOtherConfigFlag.setStatus(_A)
_SwL3Ipv6AddressCtrlTable_Object=MibTable
swL3Ipv6AddressCtrlTable=_SwL3Ipv6AddressCtrlTable_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5))
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlTable.setStatus(_A)
_SwL3Ipv6AddressCtrlEntry_Object=MibTableRow
swL3Ipv6AddressCtrlEntry=_SwL3Ipv6AddressCtrlEntry_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1))
swL3Ipv6AddressCtrlEntry.setIndexNames((0,_E,_R),(0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlEntry.setStatus(_A)
class _SwL3Ipv6AddressCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6AddressCtrlInterfaceName_Type.__name__=_J
_SwL3Ipv6AddressCtrlInterfaceName_Object=MibTableColumn
swL3Ipv6AddressCtrlInterfaceName=_SwL3Ipv6AddressCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1,1),_SwL3Ipv6AddressCtrlInterfaceName_Type())
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlInterfaceName.setStatus(_A)
_SwL3Ipv6Address_Type=Ipv6Address
_SwL3Ipv6Address_Object=MibTableColumn
swL3Ipv6Address=_SwL3Ipv6Address_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1,2),_SwL3Ipv6Address_Type())
swL3Ipv6Address.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6Address.setStatus(_A)
_SwL3Ipv6AddressCtrlPrefixLen_Type=Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object=MibTableColumn
swL3Ipv6AddressCtrlPrefixLen=_SwL3Ipv6AddressCtrlPrefixLen_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1,3),_SwL3Ipv6AddressCtrlPrefixLen_Type())
swL3Ipv6AddressCtrlPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlPrefixLen.setStatus(_A)
class _SwL3Ipv6AddressCtrlPreferredLifeTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwL3Ipv6AddressCtrlPreferredLifeTime_Type.__name__=_K
_SwL3Ipv6AddressCtrlPreferredLifeTime_Object=MibTableColumn
swL3Ipv6AddressCtrlPreferredLifeTime=_SwL3Ipv6AddressCtrlPreferredLifeTime_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1,4),_SwL3Ipv6AddressCtrlPreferredLifeTime_Type())
swL3Ipv6AddressCtrlPreferredLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlPreferredLifeTime.setStatus(_A)
class _SwL3Ipv6AddressCtrlValidLifeTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwL3Ipv6AddressCtrlValidLifeTime_Type.__name__=_K
_SwL3Ipv6AddressCtrlValidLifeTime_Object=MibTableColumn
swL3Ipv6AddressCtrlValidLifeTime=_SwL3Ipv6AddressCtrlValidLifeTime_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1,5),_SwL3Ipv6AddressCtrlValidLifeTime_Type())
swL3Ipv6AddressCtrlValidLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlValidLifeTime.setStatus(_A)
class _SwL3Ipv6AddressCtrlOnLinkFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3Ipv6AddressCtrlOnLinkFlag_Type.__name__=_B
_SwL3Ipv6AddressCtrlOnLinkFlag_Object=MibTableColumn
swL3Ipv6AddressCtrlOnLinkFlag=_SwL3Ipv6AddressCtrlOnLinkFlag_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1,6),_SwL3Ipv6AddressCtrlOnLinkFlag_Type())
swL3Ipv6AddressCtrlOnLinkFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlOnLinkFlag.setStatus(_A)
class _SwL3Ipv6AddressCtrlAutonomousFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3Ipv6AddressCtrlAutonomousFlag_Type.__name__=_B
_SwL3Ipv6AddressCtrlAutonomousFlag_Object=MibTableColumn
swL3Ipv6AddressCtrlAutonomousFlag=_SwL3Ipv6AddressCtrlAutonomousFlag_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1,7),_SwL3Ipv6AddressCtrlAutonomousFlag_Type())
swL3Ipv6AddressCtrlAutonomousFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlAutonomousFlag.setStatus(_A)
_SwL3Ipv6AddressCtrlState_Type=RowStatus
_SwL3Ipv6AddressCtrlState_Object=MibTableColumn
swL3Ipv6AddressCtrlState=_SwL3Ipv6AddressCtrlState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1,8),_SwL3Ipv6AddressCtrlState_Type())
swL3Ipv6AddressCtrlState.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlState.setStatus(_A)
class _SwL3Ipv6AddressCtrlAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('dhcpv6',2),('stateless',3)))
_SwL3Ipv6AddressCtrlAddressType_Type.__name__=_B
_SwL3Ipv6AddressCtrlAddressType_Object=MibTableColumn
swL3Ipv6AddressCtrlAddressType=_SwL3Ipv6AddressCtrlAddressType_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,5,1,9),_SwL3Ipv6AddressCtrlAddressType_Type())
swL3Ipv6AddressCtrlAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlAddressType.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlTable_Object=MibTable
swL3Ipv6DHCPv6CPDAddrCtrlTable=_SwL3Ipv6DHCPv6CPDAddrCtrlTable_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,6))
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlTable.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlEntry_Object=MibTableRow
swL3Ipv6DHCPv6CPDAddrCtrlEntry=_SwL3Ipv6DHCPv6CPDAddrCtrlEntry_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,6,1))
swL3Ipv6DHCPv6CPDAddrCtrlEntry.setIndexNames((0,_E,_U),(0,_E,_V),(0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlEntry.setStatus(_A)
class _SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type.__name__=_J
_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName=_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,6,1,1),_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type())
swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName.setStatus(_A)
class _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type.__name__=_J
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlPrefixName=_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,6,1,2),_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type())
swL3Ipv6DHCPv6CPDAddrCtrlPrefixName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlPrefixName.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Type=Ipv6Address
_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr=_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,6,1,3),_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Type())
swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Type=Integer32
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen=_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,6,1,4),_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Type())
swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlState_Type=RowStatus
_SwL3Ipv6DHCPv6CPDAddrCtrlState_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlState=_SwL3Ipv6DHCPv6CPDAddrCtrlState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,6,1,5),_SwL3Ipv6DHCPv6CPDAddrCtrlState_Type())
swL3Ipv6DHCPv6CPDAddrCtrlState.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlState.setStatus(_A)
class _SwL3IpCtrlAllIpIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_F,3)))
_SwL3IpCtrlAllIpIfState_Type.__name__=_B
_SwL3IpCtrlAllIpIfState_Object=MibScalar
swL3IpCtrlAllIpIfState=_SwL3IpCtrlAllIpIfState_Object((1,3,6,1,4,1,171,11,70,7,3,2,1,7),_SwL3IpCtrlAllIpIfState_Type())
swL3IpCtrlAllIpIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlAllIpIfState.setStatus(_A)
_SwL3IpFdbMgmt_ObjectIdentity=ObjectIdentity
swL3IpFdbMgmt=_SwL3IpFdbMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,2,2))
_SwL3IpFdbInfoTable_Object=MibTable
swL3IpFdbInfoTable=_SwL3IpFdbInfoTable_Object((1,3,6,1,4,1,171,11,70,7,3,2,2,1))
if mibBuilder.loadTexts:swL3IpFdbInfoTable.setStatus(_A)
_SwL3IpFdbInfoEntry_Object=MibTableRow
swL3IpFdbInfoEntry=_SwL3IpFdbInfoEntry_Object((1,3,6,1,4,1,171,11,70,7,3,2,2,1,1))
swL3IpFdbInfoEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:swL3IpFdbInfoEntry.setStatus(_A)
_SwL3IpFdbInfoIpAddr_Type=IpAddress
_SwL3IpFdbInfoIpAddr_Object=MibTableColumn
swL3IpFdbInfoIpAddr=_SwL3IpFdbInfoIpAddr_Object((1,3,6,1,4,1,171,11,70,7,3,2,2,1,1,1),_SwL3IpFdbInfoIpAddr_Type())
swL3IpFdbInfoIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpFdbInfoIpAddr.setStatus(_A)
_SwL3IpFdbInfoIpSubnetMask_Type=IpAddress
_SwL3IpFdbInfoIpSubnetMask_Object=MibTableColumn
swL3IpFdbInfoIpSubnetMask=_SwL3IpFdbInfoIpSubnetMask_Object((1,3,6,1,4,1,171,11,70,7,3,2,2,1,1,2),_SwL3IpFdbInfoIpSubnetMask_Type())
swL3IpFdbInfoIpSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpFdbInfoIpSubnetMask.setStatus(_A)
class _SwL3IpFdbInfoPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpFdbInfoPort_Type.__name__=_B
_SwL3IpFdbInfoPort_Object=MibTableColumn
swL3IpFdbInfoPort=_SwL3IpFdbInfoPort_Object((1,3,6,1,4,1,171,11,70,7,3,2,2,1,1,3),_SwL3IpFdbInfoPort_Type())
swL3IpFdbInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpFdbInfoPort.setStatus(_A)
class _SwL3IpFdbInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_Z,2),('dynamic',3)))
_SwL3IpFdbInfoType_Type.__name__=_B
_SwL3IpFdbInfoType_Object=MibTableColumn
swL3IpFdbInfoType=_SwL3IpFdbInfoType_Object((1,3,6,1,4,1,171,11,70,7,3,2,2,1,1,4),_SwL3IpFdbInfoType_Type())
swL3IpFdbInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpFdbInfoType.setStatus(_A)
class _SwL3IpArpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpArpAgingTime_Type.__name__=_B
_SwL3IpArpAgingTime_Object=MibScalar
swL3IpArpAgingTime=_SwL3IpArpAgingTime_Object((1,3,6,1,4,1,171,11,70,7,3,2,4),_SwL3IpArpAgingTime_Type())
swL3IpArpAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpArpAgingTime.setStatus(_A)
_SwL3IpStaticRouteTable_Object=MibTable
swL3IpStaticRouteTable=_SwL3IpStaticRouteTable_Object((1,3,6,1,4,1,171,11,70,7,3,2,5))
if mibBuilder.loadTexts:swL3IpStaticRouteTable.setStatus(_A)
_SwL3IpStaticRouteEntry_Object=MibTableRow
swL3IpStaticRouteEntry=_SwL3IpStaticRouteEntry_Object((1,3,6,1,4,1,171,11,70,7,3,2,5,1))
swL3IpStaticRouteEntry.setIndexNames((0,_E,_a),(0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:swL3IpStaticRouteEntry.setStatus(_A)
_SwL3IpStaticRouteDest_Type=IpAddress
_SwL3IpStaticRouteDest_Object=MibTableColumn
swL3IpStaticRouteDest=_SwL3IpStaticRouteDest_Object((1,3,6,1,4,1,171,11,70,7,3,2,5,1,1),_SwL3IpStaticRouteDest_Type())
swL3IpStaticRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpStaticRouteDest.setStatus(_A)
_SwL3IpStaticRouteMask_Type=IpAddress
_SwL3IpStaticRouteMask_Object=MibTableColumn
swL3IpStaticRouteMask=_SwL3IpStaticRouteMask_Object((1,3,6,1,4,1,171,11,70,7,3,2,5,1,2),_SwL3IpStaticRouteMask_Type())
swL3IpStaticRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpStaticRouteMask.setStatus(_A)
class _SwL3IpStaticRouteBkupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('backup',2)))
_SwL3IpStaticRouteBkupState_Type.__name__=_B
_SwL3IpStaticRouteBkupState_Object=MibTableColumn
swL3IpStaticRouteBkupState=_SwL3IpStaticRouteBkupState_Object((1,3,6,1,4,1,171,11,70,7,3,2,5,1,3),_SwL3IpStaticRouteBkupState_Type())
swL3IpStaticRouteBkupState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpStaticRouteBkupState.setStatus(_A)
_SwL3IpStaticRouteNextHop_Type=IpAddress
_SwL3IpStaticRouteNextHop_Object=MibTableColumn
swL3IpStaticRouteNextHop=_SwL3IpStaticRouteNextHop_Object((1,3,6,1,4,1,171,11,70,7,3,2,5,1,4),_SwL3IpStaticRouteNextHop_Type())
swL3IpStaticRouteNextHop.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3IpStaticRouteNextHop.setStatus(_A)
class _SwL3IpStaticRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3IpStaticRouteMetric_Type.__name__=_B
_SwL3IpStaticRouteMetric_Object=MibTableColumn
swL3IpStaticRouteMetric=_SwL3IpStaticRouteMetric_Object((1,3,6,1,4,1,171,11,70,7,3,2,5,1,5),_SwL3IpStaticRouteMetric_Type())
swL3IpStaticRouteMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3IpStaticRouteMetric.setStatus(_A)
class _SwL3IpStaticRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_M,2),(_N,3),('active',4),('inActive',5)))
_SwL3IpStaticRouteStatus_Type.__name__=_B
_SwL3IpStaticRouteStatus_Object=MibTableColumn
swL3IpStaticRouteStatus=_SwL3IpStaticRouteStatus_Object((1,3,6,1,4,1,171,11,70,7,3,2,5,1,6),_SwL3IpStaticRouteStatus_Type())
swL3IpStaticRouteStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3IpStaticRouteStatus.setStatus(_A)
_SwL3RelayMgmt_ObjectIdentity=ObjectIdentity
swL3RelayMgmt=_SwL3RelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,3))
_SwL3RelayDhcpMgmt_ObjectIdentity=ObjectIdentity
swL3RelayDhcpMgmt=_SwL3RelayDhcpMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,3,1))
class _SwL3RelayDhcpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_F,2),(_G,3)))
_SwL3RelayDhcpState_Type.__name__=_B
_SwL3RelayDhcpState_Object=MibScalar
swL3RelayDhcpState=_SwL3RelayDhcpState_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,1),_SwL3RelayDhcpState_Type())
swL3RelayDhcpState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDhcpState.setStatus(_A)
class _SwL3RelayDhcpHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SwL3RelayDhcpHopCount_Type.__name__=_B
_SwL3RelayDhcpHopCount_Object=MibScalar
swL3RelayDhcpHopCount=_SwL3RelayDhcpHopCount_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,2),_SwL3RelayDhcpHopCount_Type())
swL3RelayDhcpHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDhcpHopCount.setStatus(_A)
class _SwL3RelayDhcpTimeThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3RelayDhcpTimeThreshold_Type.__name__=_B
_SwL3RelayDhcpTimeThreshold_Object=MibScalar
swL3RelayDhcpTimeThreshold=_SwL3RelayDhcpTimeThreshold_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,3),_SwL3RelayDhcpTimeThreshold_Type())
swL3RelayDhcpTimeThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDhcpTimeThreshold.setStatus(_A)
_SwL3RelayDhcpCtrlTable_Object=MibTable
swL3RelayDhcpCtrlTable=_SwL3RelayDhcpCtrlTable_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,4))
if mibBuilder.loadTexts:swL3RelayDhcpCtrlTable.setStatus(_A)
_SwL3RelayDhcpCtrlEntry_Object=MibTableRow
swL3RelayDhcpCtrlEntry=_SwL3RelayDhcpCtrlEntry_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,4,1))
swL3RelayDhcpCtrlEntry.setIndexNames((0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:swL3RelayDhcpCtrlEntry.setStatus(_A)
class _SwL3RelayDhcpCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwL3RelayDhcpCtrlInterfaceName_Type.__name__=_J
_SwL3RelayDhcpCtrlInterfaceName_Object=MibTableColumn
swL3RelayDhcpCtrlInterfaceName=_SwL3RelayDhcpCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,4,1,1),_SwL3RelayDhcpCtrlInterfaceName_Type())
swL3RelayDhcpCtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDhcpCtrlInterfaceName.setStatus(_A)
_SwL3RelayDhcpCtrlServer_Type=IpAddress
_SwL3RelayDhcpCtrlServer_Object=MibTableColumn
swL3RelayDhcpCtrlServer=_SwL3RelayDhcpCtrlServer_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,4,1,2),_SwL3RelayDhcpCtrlServer_Type())
swL3RelayDhcpCtrlServer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDhcpCtrlServer.setStatus(_A)
class _SwL3RelayDhcpCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_M,2),(_N,3)))
_SwL3RelayDhcpCtrlState_Type.__name__=_B
_SwL3RelayDhcpCtrlState_Object=MibTableColumn
swL3RelayDhcpCtrlState=_SwL3RelayDhcpCtrlState_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,4,1,3),_SwL3RelayDhcpCtrlState_Type())
swL3RelayDhcpCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDhcpCtrlState.setStatus(_A)
class _SwL3RelayDhcpOption82State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SwL3RelayDhcpOption82State_Type.__name__=_B
_SwL3RelayDhcpOption82State_Object=MibScalar
swL3RelayDhcpOption82State=_SwL3RelayDhcpOption82State_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,5),_SwL3RelayDhcpOption82State_Type())
swL3RelayDhcpOption82State.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDhcpOption82State.setStatus(_A)
class _SwL3RelayDhcpOption82CheckState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SwL3RelayDhcpOption82CheckState_Type.__name__=_B
_SwL3RelayDhcpOption82CheckState_Object=MibScalar
swL3RelayDhcpOption82CheckState=_SwL3RelayDhcpOption82CheckState_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,6),_SwL3RelayDhcpOption82CheckState_Type())
swL3RelayDhcpOption82CheckState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDhcpOption82CheckState.setStatus(_A)
class _SwL3RelayDhcpOption82Policy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('replace',0),(_L,1),('keep',2)))
_SwL3RelayDhcpOption82Policy_Type.__name__=_B
_SwL3RelayDhcpOption82Policy_Object=MibScalar
swL3RelayDhcpOption82Policy=_SwL3RelayDhcpOption82Policy_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,7),_SwL3RelayDhcpOption82Policy_Type())
swL3RelayDhcpOption82Policy.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDhcpOption82Policy.setStatus(_A)
_SwL3DHCPRelayOption60_ObjectIdentity=ObjectIdentity
swL3DHCPRelayOption60=_SwL3DHCPRelayOption60_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,3,1,8))
class _SwL3DHCPRelayOption60State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3DHCPRelayOption60State_Type.__name__=_B
_SwL3DHCPRelayOption60State_Object=MibScalar
swL3DHCPRelayOption60State=_SwL3DHCPRelayOption60State_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,1),_SwL3DHCPRelayOption60State_Type())
swL3DHCPRelayOption60State.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3DHCPRelayOption60State.setStatus(_A)
class _SwL3DHCPRelayOption60DefMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_L,2)))
_SwL3DHCPRelayOption60DefMode_Type.__name__=_B
_SwL3DHCPRelayOption60DefMode_Object=MibScalar
swL3DHCPRelayOption60DefMode=_SwL3DHCPRelayOption60DefMode_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,2),_SwL3DHCPRelayOption60DefMode_Type())
swL3DHCPRelayOption60DefMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3DHCPRelayOption60DefMode.setStatus(_A)
_SwL3DHCPRelayOption60DefTable_Object=MibTable
swL3DHCPRelayOption60DefTable=_SwL3DHCPRelayOption60DefTable_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,3))
if mibBuilder.loadTexts:swL3DHCPRelayOption60DefTable.setStatus(_A)
_SwL3DHCPRelayOption60DefEntry_Object=MibTableRow
swL3DHCPRelayOption60DefEntry=_SwL3DHCPRelayOption60DefEntry_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,3,1))
swL3DHCPRelayOption60DefEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:swL3DHCPRelayOption60DefEntry.setStatus(_A)
_SwL3DHCPRelayOption60DefRelayIp_Type=IpAddress
_SwL3DHCPRelayOption60DefRelayIp_Object=MibTableColumn
swL3DHCPRelayOption60DefRelayIp=_SwL3DHCPRelayOption60DefRelayIp_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,3,1,1),_SwL3DHCPRelayOption60DefRelayIp_Type())
swL3DHCPRelayOption60DefRelayIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DHCPRelayOption60DefRelayIp.setStatus(_A)
_SwL3DHCPRelayOption60DefRowStatus_Type=RowStatus
_SwL3DHCPRelayOption60DefRowStatus_Object=MibTableColumn
swL3DHCPRelayOption60DefRowStatus=_SwL3DHCPRelayOption60DefRowStatus_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,3,1,2),_SwL3DHCPRelayOption60DefRowStatus_Type())
swL3DHCPRelayOption60DefRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3DHCPRelayOption60DefRowStatus.setStatus(_A)
_SwL3DHCPRelayOption60Table_Object=MibTable
swL3DHCPRelayOption60Table=_SwL3DHCPRelayOption60Table_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,4))
if mibBuilder.loadTexts:swL3DHCPRelayOption60Table.setStatus(_A)
_SwL3DHCPRelayOption60Entry_Object=MibTableRow
swL3DHCPRelayOption60Entry=_SwL3DHCPRelayOption60Entry_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,4,1))
swL3DHCPRelayOption60Entry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:swL3DHCPRelayOption60Entry.setStatus(_A)
_SwL3DHCPRelayOption60String_Type=DisplayString
_SwL3DHCPRelayOption60String_Object=MibTableColumn
swL3DHCPRelayOption60String=_SwL3DHCPRelayOption60String_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,4,1,1),_SwL3DHCPRelayOption60String_Type())
swL3DHCPRelayOption60String.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DHCPRelayOption60String.setStatus(_A)
_SwL3DHCPRelayOption60RelayIp_Type=IpAddress
_SwL3DHCPRelayOption60RelayIp_Object=MibTableColumn
swL3DHCPRelayOption60RelayIp=_SwL3DHCPRelayOption60RelayIp_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,4,1,2),_SwL3DHCPRelayOption60RelayIp_Type())
swL3DHCPRelayOption60RelayIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DHCPRelayOption60RelayIp.setStatus(_A)
class _SwL3DHCPRelayOption60MatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exact',1),('partial',2)))
_SwL3DHCPRelayOption60MatchType_Type.__name__=_B
_SwL3DHCPRelayOption60MatchType_Object=MibTableColumn
swL3DHCPRelayOption60MatchType=_SwL3DHCPRelayOption60MatchType_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,4,1,3),_SwL3DHCPRelayOption60MatchType_Type())
swL3DHCPRelayOption60MatchType.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3DHCPRelayOption60MatchType.setStatus(_A)
_SwL3DHCPRelayOption60RowStatus_Type=RowStatus
_SwL3DHCPRelayOption60RowStatus_Object=MibTableColumn
swL3DHCPRelayOption60RowStatus=_SwL3DHCPRelayOption60RowStatus_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,8,4,1,4),_SwL3DHCPRelayOption60RowStatus_Type())
swL3DHCPRelayOption60RowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3DHCPRelayOption60RowStatus.setStatus(_A)
_SwL3DHCPRelayOption61_ObjectIdentity=ObjectIdentity
swL3DHCPRelayOption61=_SwL3DHCPRelayOption61_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,3,1,9))
class _SwL3DHCPRelayOption61State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL3DHCPRelayOption61State_Type.__name__=_B
_SwL3DHCPRelayOption61State_Object=MibScalar
swL3DHCPRelayOption61State=_SwL3DHCPRelayOption61State_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,1),_SwL3DHCPRelayOption61State_Type())
swL3DHCPRelayOption61State.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3DHCPRelayOption61State.setStatus(_A)
class _SwL3DHCPRelayOption61DefMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_L,2)))
_SwL3DHCPRelayOption61DefMode_Type.__name__=_B
_SwL3DHCPRelayOption61DefMode_Object=MibScalar
swL3DHCPRelayOption61DefMode=_SwL3DHCPRelayOption61DefMode_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,2),_SwL3DHCPRelayOption61DefMode_Type())
swL3DHCPRelayOption61DefMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3DHCPRelayOption61DefMode.setStatus(_A)
_SwL3DHCPRelayOption61DefRelayIp_Type=IpAddress
_SwL3DHCPRelayOption61DefRelayIp_Object=MibScalar
swL3DHCPRelayOption61DefRelayIp=_SwL3DHCPRelayOption61DefRelayIp_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,3),_SwL3DHCPRelayOption61DefRelayIp_Type())
swL3DHCPRelayOption61DefRelayIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3DHCPRelayOption61DefRelayIp.setStatus(_A)
_SwL3DHCPRelayOption61Table_Object=MibTable
swL3DHCPRelayOption61Table=_SwL3DHCPRelayOption61Table_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,4))
if mibBuilder.loadTexts:swL3DHCPRelayOption61Table.setStatus(_A)
_SwL3DHCPRelayOption61Entry_Object=MibTableRow
swL3DHCPRelayOption61Entry=_SwL3DHCPRelayOption61Entry_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,4,1))
swL3DHCPRelayOption61Entry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:swL3DHCPRelayOption61Entry.setStatus(_A)
class _SwL3DHCPRelayOption61ClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mac',1),('string',2)))
_SwL3DHCPRelayOption61ClientType_Type.__name__=_B
_SwL3DHCPRelayOption61ClientType_Object=MibTableColumn
swL3DHCPRelayOption61ClientType=_SwL3DHCPRelayOption61ClientType_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,4,1,1),_SwL3DHCPRelayOption61ClientType_Type())
swL3DHCPRelayOption61ClientType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DHCPRelayOption61ClientType.setStatus(_A)
_SwL3DHCPRelayOption61ClientID_Type=DisplayString
_SwL3DHCPRelayOption61ClientID_Object=MibTableColumn
swL3DHCPRelayOption61ClientID=_SwL3DHCPRelayOption61ClientID_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,4,1,2),_SwL3DHCPRelayOption61ClientID_Type())
swL3DHCPRelayOption61ClientID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DHCPRelayOption61ClientID.setStatus(_A)
class _SwL3DHCPRelayOption61Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_L,2)))
_SwL3DHCPRelayOption61Mode_Type.__name__=_B
_SwL3DHCPRelayOption61Mode_Object=MibTableColumn
swL3DHCPRelayOption61Mode=_SwL3DHCPRelayOption61Mode_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,4,1,3),_SwL3DHCPRelayOption61Mode_Type())
swL3DHCPRelayOption61Mode.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3DHCPRelayOption61Mode.setStatus(_A)
_SwL3DHCPRelayOption61RelayIp_Type=IpAddress
_SwL3DHCPRelayOption61RelayIp_Object=MibTableColumn
swL3DHCPRelayOption61RelayIp=_SwL3DHCPRelayOption61RelayIp_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,4,1,4),_SwL3DHCPRelayOption61RelayIp_Type())
swL3DHCPRelayOption61RelayIp.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3DHCPRelayOption61RelayIp.setStatus(_A)
_SwL3DHCPRelayOption61RowStatus_Type=RowStatus
_SwL3DHCPRelayOption61RowStatus_Object=MibTableColumn
swL3DHCPRelayOption61RowStatus=_SwL3DHCPRelayOption61RowStatus_Object((1,3,6,1,4,1,171,11,70,7,3,3,1,9,4,1,5),_SwL3DHCPRelayOption61RowStatus_Type())
swL3DHCPRelayOption61RowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3DHCPRelayOption61RowStatus.setStatus(_A)
_SwL3RelayDnsMgmt_ObjectIdentity=ObjectIdentity
swL3RelayDnsMgmt=_SwL3RelayDnsMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,3,2))
class _SwL3RelayDnsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_F,2),(_G,3)))
_SwL3RelayDnsState_Type.__name__=_B
_SwL3RelayDnsState_Object=MibScalar
swL3RelayDnsState=_SwL3RelayDnsState_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,1),_SwL3RelayDnsState_Type())
swL3RelayDnsState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDnsState.setStatus(_A)
_SwL3RelayDnsPrimaryServer_Type=IpAddress
_SwL3RelayDnsPrimaryServer_Object=MibScalar
swL3RelayDnsPrimaryServer=_SwL3RelayDnsPrimaryServer_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,2),_SwL3RelayDnsPrimaryServer_Type())
swL3RelayDnsPrimaryServer.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDnsPrimaryServer.setStatus(_A)
_SwL3RelayDnsSecondaryServer_Type=IpAddress
_SwL3RelayDnsSecondaryServer_Object=MibScalar
swL3RelayDnsSecondaryServer=_SwL3RelayDnsSecondaryServer_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,3),_SwL3RelayDnsSecondaryServer_Type())
swL3RelayDnsSecondaryServer.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDnsSecondaryServer.setStatus(_A)
class _SwL3RelayDnsCacheState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_F,2),(_G,3)))
_SwL3RelayDnsCacheState_Type.__name__=_B
_SwL3RelayDnsCacheState_Object=MibScalar
swL3RelayDnsCacheState=_SwL3RelayDnsCacheState_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,4),_SwL3RelayDnsCacheState_Type())
swL3RelayDnsCacheState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDnsCacheState.setStatus(_A)
class _SwL3RelayDnsStaticTableState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_F,2),(_G,3)))
_SwL3RelayDnsStaticTableState_Type.__name__=_B
_SwL3RelayDnsStaticTableState_Object=MibScalar
swL3RelayDnsStaticTableState=_SwL3RelayDnsStaticTableState_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,5),_SwL3RelayDnsStaticTableState_Type())
swL3RelayDnsStaticTableState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDnsStaticTableState.setStatus(_A)
_SwL3RelayDnsCtrlTable_Object=MibTable
swL3RelayDnsCtrlTable=_SwL3RelayDnsCtrlTable_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,6))
if mibBuilder.loadTexts:swL3RelayDnsCtrlTable.setStatus(_A)
_SwL3RelayDnsCtrlEntry_Object=MibTableRow
swL3RelayDnsCtrlEntry=_SwL3RelayDnsCtrlEntry_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,6,1))
swL3RelayDnsCtrlEntry.setIndexNames((0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:swL3RelayDnsCtrlEntry.setStatus(_A)
class _SwL3RelayDnsCtrlDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwL3RelayDnsCtrlDomainName_Type.__name__=_J
_SwL3RelayDnsCtrlDomainName_Object=MibTableColumn
swL3RelayDnsCtrlDomainName=_SwL3RelayDnsCtrlDomainName_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,6,1,1),_SwL3RelayDnsCtrlDomainName_Type())
swL3RelayDnsCtrlDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsCtrlDomainName.setStatus(_A)
_SwL3RelayDnsCtrlIpAddr_Type=IpAddress
_SwL3RelayDnsCtrlIpAddr_Object=MibTableColumn
swL3RelayDnsCtrlIpAddr=_SwL3RelayDnsCtrlIpAddr_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,6,1,2),_SwL3RelayDnsCtrlIpAddr_Type())
swL3RelayDnsCtrlIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsCtrlIpAddr.setStatus(_A)
class _SwL3RelayDnsCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_M,2),(_N,3)))
_SwL3RelayDnsCtrlState_Type.__name__=_B
_SwL3RelayDnsCtrlState_Object=MibTableColumn
swL3RelayDnsCtrlState=_SwL3RelayDnsCtrlState_Object((1,3,6,1,4,1,171,11,70,7,3,3,2,6,1,3),_SwL3RelayDnsCtrlState_Type())
swL3RelayDnsCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDnsCtrlState.setStatus(_A)
_SwL3RouteRedistriTable_Object=MibTable
swL3RouteRedistriTable=_SwL3RouteRedistriTable_Object((1,3,6,1,4,1,171,11,70,7,3,5))
if mibBuilder.loadTexts:swL3RouteRedistriTable.setStatus(_A)
_SwL3RouteRedistriEntry_Object=MibTableRow
swL3RouteRedistriEntry=_SwL3RouteRedistriEntry_Object((1,3,6,1,4,1,171,11,70,7,3,5,1))
swL3RouteRedistriEntry.setIndexNames((0,_E,_m),(0,_E,_n))
if mibBuilder.loadTexts:swL3RouteRedistriEntry.setStatus(_A)
class _SwL3RouteRedistriSrcProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5)));namedValues=NamedValues(*((_I,1),(_Z,4),('local',5)))
_SwL3RouteRedistriSrcProtocol_Type.__name__=_B
_SwL3RouteRedistriSrcProtocol_Object=MibTableColumn
swL3RouteRedistriSrcProtocol=_SwL3RouteRedistriSrcProtocol_Object((1,3,6,1,4,1,171,11,70,7,3,5,1,1),_SwL3RouteRedistriSrcProtocol_Type())
swL3RouteRedistriSrcProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RouteRedistriSrcProtocol.setStatus(_A)
class _SwL3RouteRedistriDstProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('rip',2)))
_SwL3RouteRedistriDstProtocol_Type.__name__=_B
_SwL3RouteRedistriDstProtocol_Object=MibTableColumn
swL3RouteRedistriDstProtocol=_SwL3RouteRedistriDstProtocol_Object((1,3,6,1,4,1,171,11,70,7,3,5,1,2),_SwL3RouteRedistriDstProtocol_Type())
swL3RouteRedistriDstProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RouteRedistriDstProtocol.setStatus(_A)
class _SwL3RouteRedistriMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_SwL3RouteRedistriMetric_Type.__name__=_B
_SwL3RouteRedistriMetric_Object=MibTableColumn
swL3RouteRedistriMetric=_SwL3RouteRedistriMetric_Object((1,3,6,1,4,1,171,11,70,7,3,5,1,4),_SwL3RouteRedistriMetric_Type())
swL3RouteRedistriMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3RouteRedistriMetric.setStatus(_A)
_SwL3RouteRedistriRowStatus_Type=RowStatus
_SwL3RouteRedistriRowStatus_Object=MibTableColumn
swL3RouteRedistriRowStatus=_SwL3RouteRedistriRowStatus_Object((1,3,6,1,4,1,171,11,70,7,3,5,1,5),_SwL3RouteRedistriRowStatus_Type())
swL3RouteRedistriRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swL3RouteRedistriRowStatus.setStatus(_A)
_SwL3RoutePreference_ObjectIdentity=ObjectIdentity
swL3RoutePreference=_SwL3RoutePreference_ObjectIdentity((1,3,6,1,4,1,171,11,70,7,3,9))
class _SwL3RoutePreferenceRIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceRIP_Type.__name__=_B
_SwL3RoutePreferenceRIP_Object=MibScalar
swL3RoutePreferenceRIP=_SwL3RoutePreferenceRIP_Object((1,3,6,1,4,1,171,11,70,7,3,9,1),_SwL3RoutePreferenceRIP_Type())
swL3RoutePreferenceRIP.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RoutePreferenceRIP.setStatus(_A)
class _SwL3RoutePreferenceStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceStatic_Type.__name__=_B
_SwL3RoutePreferenceStatic_Object=MibScalar
swL3RoutePreferenceStatic=_SwL3RoutePreferenceStatic_Object((1,3,6,1,4,1,171,11,70,7,3,9,3),_SwL3RoutePreferenceStatic_Type())
swL3RoutePreferenceStatic.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RoutePreferenceStatic.setStatus(_A)
class _SwL3RoutePreferenceLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_SwL3RoutePreferenceLocal_Type.__name__=_B
_SwL3RoutePreferenceLocal_Object=MibScalar
swL3RoutePreferenceLocal=_SwL3RoutePreferenceLocal_Object((1,3,6,1,4,1,171,11,70,7,3,9,4),_SwL3RoutePreferenceLocal_Type())
swL3RoutePreferenceLocal.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceLocal.setStatus(_A)
class _SwL3RoutePreferenceDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceDefault_Type.__name__=_B
_SwL3RoutePreferenceDefault_Object=MibScalar
swL3RoutePreferenceDefault=_SwL3RoutePreferenceDefault_Object((1,3,6,1,4,1,171,11,70,7,3,9,8),_SwL3RoutePreferenceDefault_Type())
swL3RoutePreferenceDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RoutePreferenceDefault.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'Ipv6Address':Ipv6Address,'swL3MgmtMIB':swL3MgmtMIB,'swL3DevMgmt':swL3DevMgmt,'swL3DevCtrl':swL3DevCtrl,'swL3DevCtrlRIPState':swL3DevCtrlRIPState,'swL3IpMgmt':swL3IpMgmt,'swL3IpCtrlMgmt':swL3IpCtrlMgmt,'swL3IpCtrlTable':swL3IpCtrlTable,'swL3IpCtrlEntry':swL3IpCtrlEntry,_P:swL3IpCtrlInterfaceName,'swL3IpCtrlIfIndex':swL3IpCtrlIfIndex,'swL3IpCtrlIpAddr':swL3IpCtrlIpAddr,'swL3IpCtrlIpSubnetMask':swL3IpCtrlIpSubnetMask,'swL3IpCtrlVlanName':swL3IpCtrlVlanName,'swL3IpCtrlProxyArp':swL3IpCtrlProxyArp,'swL3IpCtrlSecondary':swL3IpCtrlSecondary,'swL3IpCtrlMode':swL3IpCtrlMode,'swL3IpCtrlAdminState':swL3IpCtrlAdminState,'swL3IpCtrlIpv6LinkLocalAddress':swL3IpCtrlIpv6LinkLocalAddress,'swL3IpCtrlIpv6LinkLocalPrefixLen':swL3IpCtrlIpv6LinkLocalPrefixLen,'swL3IpCtrlState':swL3IpCtrlState,'swL3IpCtrlIpv6LinkLocalAutoState':swL3IpCtrlIpv6LinkLocalAutoState,'swL3IpCtrlLocalProxyArp':swL3IpCtrlLocalProxyArp,'swL3IpCtrlDhcpv6ClientState':swL3IpCtrlDhcpv6ClientState,'swL3IpCtrlIpDirectedBroadcastState':swL3IpCtrlIpDirectedBroadcastState,'swL3IpCtrlIpDhcpOption12State':swL3IpCtrlIpDhcpOption12State,'swL3IpCtrlIpDhcpOption12HostName':swL3IpCtrlIpDhcpOption12HostName,'swL3IpCtrlDhcpv6ClientPDState':swL3IpCtrlDhcpv6ClientPDState,'swL3IpCtrlDhcpv6ClientPDPrefixName':swL3IpCtrlDhcpv6ClientPDPrefixName,'swL3IpCtrlDhcpv6ClientPDPrefix':swL3IpCtrlDhcpv6ClientPDPrefix,'swL3IpCtrlDhcpv6ClientPDPrefixLen':swL3IpCtrlDhcpv6ClientPDPrefixLen,'swL3Ipv6CtrlTable':swL3Ipv6CtrlTable,'swL3Ipv6CtrlEntry':swL3Ipv6CtrlEntry,_Q:swL3Ipv6CtrlInterfaceName,'swL3Ipv6CtrlMaxReassmblySize':swL3Ipv6CtrlMaxReassmblySize,'swL3Ipv6CtrlNsRetransTimer':swL3Ipv6CtrlNsRetransTimer,'swL3Ipv6CtrlRaState':swL3Ipv6CtrlRaState,'swL3Ipv6CtrlRaMinRtrAdvInterval':swL3Ipv6CtrlRaMinRtrAdvInterval,'swL3Ipv6CtrlRaMaxRtrAdvInterval':swL3Ipv6CtrlRaMaxRtrAdvInterval,'swL3Ipv6CtrlRaLifeTime':swL3Ipv6CtrlRaLifeTime,'swL3Ipv6CtrlRaReachableTime':swL3Ipv6CtrlRaReachableTime,'swL3Ipv6CtrlRaRetransTime':swL3Ipv6CtrlRaRetransTime,'swL3Ipv6CtrlRaHopLimit':swL3Ipv6CtrlRaHopLimit,'swL3Ipv6CtrlRaManagedFlag':swL3Ipv6CtrlRaManagedFlag,'swL3Ipv6CtrlRaOtherConfigFlag':swL3Ipv6CtrlRaOtherConfigFlag,'swL3Ipv6AddressCtrlTable':swL3Ipv6AddressCtrlTable,'swL3Ipv6AddressCtrlEntry':swL3Ipv6AddressCtrlEntry,_R:swL3Ipv6AddressCtrlInterfaceName,_S:swL3Ipv6Address,_T:swL3Ipv6AddressCtrlPrefixLen,'swL3Ipv6AddressCtrlPreferredLifeTime':swL3Ipv6AddressCtrlPreferredLifeTime,'swL3Ipv6AddressCtrlValidLifeTime':swL3Ipv6AddressCtrlValidLifeTime,'swL3Ipv6AddressCtrlOnLinkFlag':swL3Ipv6AddressCtrlOnLinkFlag,'swL3Ipv6AddressCtrlAutonomousFlag':swL3Ipv6AddressCtrlAutonomousFlag,'swL3Ipv6AddressCtrlState':swL3Ipv6AddressCtrlState,'swL3Ipv6AddressCtrlAddressType':swL3Ipv6AddressCtrlAddressType,'swL3Ipv6DHCPv6CPDAddrCtrlTable':swL3Ipv6DHCPv6CPDAddrCtrlTable,'swL3Ipv6DHCPv6CPDAddrCtrlEntry':swL3Ipv6DHCPv6CPDAddrCtrlEntry,_U:swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName,_V:swL3Ipv6DHCPv6CPDAddrCtrlPrefixName,_W:swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr,_X:swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen,'swL3Ipv6DHCPv6CPDAddrCtrlState':swL3Ipv6DHCPv6CPDAddrCtrlState,'swL3IpCtrlAllIpIfState':swL3IpCtrlAllIpIfState,'swL3IpFdbMgmt':swL3IpFdbMgmt,'swL3IpFdbInfoTable':swL3IpFdbInfoTable,'swL3IpFdbInfoEntry':swL3IpFdbInfoEntry,_Y:swL3IpFdbInfoIpAddr,'swL3IpFdbInfoIpSubnetMask':swL3IpFdbInfoIpSubnetMask,'swL3IpFdbInfoPort':swL3IpFdbInfoPort,'swL3IpFdbInfoType':swL3IpFdbInfoType,'swL3IpArpAgingTime':swL3IpArpAgingTime,'swL3IpStaticRouteTable':swL3IpStaticRouteTable,'swL3IpStaticRouteEntry':swL3IpStaticRouteEntry,_a:swL3IpStaticRouteDest,_b:swL3IpStaticRouteMask,'swL3IpStaticRouteBkupState':swL3IpStaticRouteBkupState,_c:swL3IpStaticRouteNextHop,'swL3IpStaticRouteMetric':swL3IpStaticRouteMetric,'swL3IpStaticRouteStatus':swL3IpStaticRouteStatus,'swL3RelayMgmt':swL3RelayMgmt,'swL3RelayDhcpMgmt':swL3RelayDhcpMgmt,'swL3RelayDhcpState':swL3RelayDhcpState,'swL3RelayDhcpHopCount':swL3RelayDhcpHopCount,'swL3RelayDhcpTimeThreshold':swL3RelayDhcpTimeThreshold,'swL3RelayDhcpCtrlTable':swL3RelayDhcpCtrlTable,'swL3RelayDhcpCtrlEntry':swL3RelayDhcpCtrlEntry,_d:swL3RelayDhcpCtrlInterfaceName,_e:swL3RelayDhcpCtrlServer,'swL3RelayDhcpCtrlState':swL3RelayDhcpCtrlState,'swL3RelayDhcpOption82State':swL3RelayDhcpOption82State,'swL3RelayDhcpOption82CheckState':swL3RelayDhcpOption82CheckState,'swL3RelayDhcpOption82Policy':swL3RelayDhcpOption82Policy,'swL3DHCPRelayOption60':swL3DHCPRelayOption60,'swL3DHCPRelayOption60State':swL3DHCPRelayOption60State,'swL3DHCPRelayOption60DefMode':swL3DHCPRelayOption60DefMode,'swL3DHCPRelayOption60DefTable':swL3DHCPRelayOption60DefTable,'swL3DHCPRelayOption60DefEntry':swL3DHCPRelayOption60DefEntry,_f:swL3DHCPRelayOption60DefRelayIp,'swL3DHCPRelayOption60DefRowStatus':swL3DHCPRelayOption60DefRowStatus,'swL3DHCPRelayOption60Table':swL3DHCPRelayOption60Table,'swL3DHCPRelayOption60Entry':swL3DHCPRelayOption60Entry,_g:swL3DHCPRelayOption60String,_h:swL3DHCPRelayOption60RelayIp,'swL3DHCPRelayOption60MatchType':swL3DHCPRelayOption60MatchType,'swL3DHCPRelayOption60RowStatus':swL3DHCPRelayOption60RowStatus,'swL3DHCPRelayOption61':swL3DHCPRelayOption61,'swL3DHCPRelayOption61State':swL3DHCPRelayOption61State,'swL3DHCPRelayOption61DefMode':swL3DHCPRelayOption61DefMode,'swL3DHCPRelayOption61DefRelayIp':swL3DHCPRelayOption61DefRelayIp,'swL3DHCPRelayOption61Table':swL3DHCPRelayOption61Table,'swL3DHCPRelayOption61Entry':swL3DHCPRelayOption61Entry,_i:swL3DHCPRelayOption61ClientType,_j:swL3DHCPRelayOption61ClientID,'swL3DHCPRelayOption61Mode':swL3DHCPRelayOption61Mode,'swL3DHCPRelayOption61RelayIp':swL3DHCPRelayOption61RelayIp,'swL3DHCPRelayOption61RowStatus':swL3DHCPRelayOption61RowStatus,'swL3RelayDnsMgmt':swL3RelayDnsMgmt,'swL3RelayDnsState':swL3RelayDnsState,'swL3RelayDnsPrimaryServer':swL3RelayDnsPrimaryServer,'swL3RelayDnsSecondaryServer':swL3RelayDnsSecondaryServer,'swL3RelayDnsCacheState':swL3RelayDnsCacheState,'swL3RelayDnsStaticTableState':swL3RelayDnsStaticTableState,'swL3RelayDnsCtrlTable':swL3RelayDnsCtrlTable,'swL3RelayDnsCtrlEntry':swL3RelayDnsCtrlEntry,_k:swL3RelayDnsCtrlDomainName,_l:swL3RelayDnsCtrlIpAddr,'swL3RelayDnsCtrlState':swL3RelayDnsCtrlState,'swL3RouteRedistriTable':swL3RouteRedistriTable,'swL3RouteRedistriEntry':swL3RouteRedistriEntry,_m:swL3RouteRedistriSrcProtocol,_n:swL3RouteRedistriDstProtocol,'swL3RouteRedistriMetric':swL3RouteRedistriMetric,'swL3RouteRedistriRowStatus':swL3RouteRedistriRowStatus,'swL3RoutePreference':swL3RoutePreference,'swL3RoutePreferenceRIP':swL3RoutePreferenceRIP,'swL3RoutePreferenceStatic':swL3RoutePreferenceStatic,'swL3RoutePreferenceLocal':swL3RoutePreferenceLocal,'swL3RoutePreferenceDefault':swL3RoutePreferenceDefault})