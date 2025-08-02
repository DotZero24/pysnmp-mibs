_AN='swL3Route6RedistriDstProtocol'
_AM='swL3Route6RedistriSrcProtocol'
_AL='swL3RIPInboundRouteFilterIfIpAddress'
_AK='swL3VrrpOperVrId'
_AJ='swL3VrrpOperIfIndex'
_AI='swL3OspfExternalLsdbRouterId'
_AH='swL3OspfExternalLsdbLsid'
_AG='swL3OspfExternalLsdbType'
_AF='nssaExternalLink'
_AE='asExternalLink'
_AD='swL3OspfInternalLsdbRouterId'
_AC='swL3OspfInternalLsdbLsid'
_AB='swL3OspfInternalLsdbType'
_AA='swL3OspfInternalLsdbAreaId'
_A9='swL3dvmrpInterfaceIfIndex'
_A8='swL3ospfAreaId'
_A7='access_list'
_A6='swL3ospfAddressLessIf'
_A5='swL3ospfIfIpAddress'
_A4='0000000000000000'
_A3='swL3ospfVirtIfNeighbor'
_A2='swL3ospfVirtIfAreaId'
_A1='swL3OspfHostTOS'
_A0='swL3OspfHostIpAddress'
_z='swL3RouteRedistriDstProtocol'
_y='swL3RouteRedistriSrcProtocol'
_x='swL3Md5KeyId'
_w='swL3RelayDnsCtrlIpAddr'
_v='swL3RelayDnsCtrlDomainName'
_u='swL3IpStaticRouteTunnelInterfaceName'
_t='swL3IpMcastStaticRouteIpmrouteMask'
_s='swL3IpMcastStaticRouteIpmrouteAddr'
_r='invalid'
_q='backup'
_p='swL3IpStaticRouteNextHop'
_o='swL3IpFdbInfoIpAddr'
_n='swL3LoopBackIpCtrlInterfaceName'
_m='swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen'
_l='swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr'
_k='swL3Ipv6DHCPv6CPDAddrCtrlPrefixName'
_j='swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName'
_i='swL3Ipv6AddressCtrlPrefixLen'
_h='swL3Ipv6Address'
_g='swL3Ipv6AddressCtrlInterfaceName'
_f='swL3Ipv6CtrlInterfaceName'
_e='swL3IpCtrlInterfaceName'
_d='Status'
_c='DesignatedRouterPriority'
_b='AreaID'
_a='pointToPoint'
_Z='down'
_Y='not-accessible'
_X='swL3IpStaticRouteMask'
_W='swL3IpStaticRouteDest'
_V='static'
_U='TruthValue'
_T='PositiveInteger'
_S='HelloRange'
_R='00000000'
_Q='type-2'
_P='type-1'
_O='IpAddress'
_N='Unsigned32'
_M='UpToMaxAge'
_L='none'
_K='OctetString'
_J='DisplayString'
_I='other'
_H='enabled'
_G='disabled'
_F='DGS-3620-52P-L3MGMT-MIB'
_E='read-create'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
AreaID,DesignatedRouterPriority,HelloRange,Metric,PositiveInteger,RouterID,Status,TOSType,UpToMaxAge=mibBuilder.importSymbols('OSPF-MIB',_b,_c,_S,'Metric',_T,'RouterID',_d,'TOSType',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_O,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_U)
dlink_Dgs3620Proj_Dgs3620_52P,=mibBuilder.importSymbols('SWDGS3620PRIMGMT-MIB','dlink-Dgs3620Proj-Dgs3620-52P')
swL3MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,118,5,3))
class NodeAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class NetAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class VrId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL3DevMgmt_ObjectIdentity=ObjectIdentity
swL3DevMgmt=_SwL3DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,1))
_SwL3DevCtrl_ObjectIdentity=ObjectIdentity
swL3DevCtrl=_SwL3DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,1,1))
class _SwL3DevCtrlRIPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_SwL3DevCtrlRIPState_Type.__name__=_B
_SwL3DevCtrlRIPState_Object=MibScalar
swL3DevCtrlRIPState=_SwL3DevCtrlRIPState_Object((1,3,6,1,4,1,171,11,118,5,3,1,1,1),_SwL3DevCtrlRIPState_Type())
swL3DevCtrlRIPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlRIPState.setStatus(_A)
class _SwL3DevCtrlOSPFState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_SwL3DevCtrlOSPFState_Type.__name__=_B
_SwL3DevCtrlOSPFState_Object=MibScalar
swL3DevCtrlOSPFState=_SwL3DevCtrlOSPFState_Object((1,3,6,1,4,1,171,11,118,5,3,1,1,2),_SwL3DevCtrlOSPFState_Type())
swL3DevCtrlOSPFState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlOSPFState.setStatus(_A)
class _SwL3DevCtrlDVMRPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_SwL3DevCtrlDVMRPState_Type.__name__=_B
_SwL3DevCtrlDVMRPState_Object=MibScalar
swL3DevCtrlDVMRPState=_SwL3DevCtrlDVMRPState_Object((1,3,6,1,4,1,171,11,118,5,3,1,1,3),_SwL3DevCtrlDVMRPState_Type())
swL3DevCtrlDVMRPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlDVMRPState.setStatus(_A)
class _SwL3DevCtrlVRRPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_SwL3DevCtrlVRRPState_Type.__name__=_B
_SwL3DevCtrlVRRPState_Object=MibScalar
swL3DevCtrlVRRPState=_SwL3DevCtrlVRRPState_Object((1,3,6,1,4,1,171,11,118,5,3,1,1,5),_SwL3DevCtrlVRRPState_Type())
swL3DevCtrlVRRPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlVRRPState.setStatus(_A)
class _SwL3DevCtrlVrrpPingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_SwL3DevCtrlVrrpPingState_Type.__name__=_B
_SwL3DevCtrlVrrpPingState_Object=MibScalar
swL3DevCtrlVrrpPingState=_SwL3DevCtrlVrrpPingState_Object((1,3,6,1,4,1,171,11,118,5,3,1,1,6),_SwL3DevCtrlVrrpPingState_Type())
swL3DevCtrlVrrpPingState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlVrrpPingState.setStatus(_A)
_SwL3IpMgmt_ObjectIdentity=ObjectIdentity
swL3IpMgmt=_SwL3IpMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,2))
_SwL3IpCtrlMgmt_ObjectIdentity=ObjectIdentity
swL3IpCtrlMgmt=_SwL3IpCtrlMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,2,1))
_SwL3IpCtrlTable_Object=MibTable
swL3IpCtrlTable=_SwL3IpCtrlTable_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3))
if mibBuilder.loadTexts:swL3IpCtrlTable.setStatus(_A)
_SwL3IpCtrlEntry_Object=MibTableRow
swL3IpCtrlEntry=_SwL3IpCtrlEntry_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1))
swL3IpCtrlEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:swL3IpCtrlEntry.setStatus(_A)
class _SwL3IpCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3IpCtrlInterfaceName_Type.__name__=_J
_SwL3IpCtrlInterfaceName_Object=MibTableColumn
swL3IpCtrlInterfaceName=_SwL3IpCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,1),_SwL3IpCtrlInterfaceName_Type())
swL3IpCtrlInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlInterfaceName.setStatus(_A)
class _SwL3IpCtrlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpCtrlIfIndex_Type.__name__=_B
_SwL3IpCtrlIfIndex_Object=MibTableColumn
swL3IpCtrlIfIndex=_SwL3IpCtrlIfIndex_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,2),_SwL3IpCtrlIfIndex_Type())
swL3IpCtrlIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIfIndex.setStatus(_A)
_SwL3IpCtrlIpAddr_Type=IpAddress
_SwL3IpCtrlIpAddr_Object=MibTableColumn
swL3IpCtrlIpAddr=_SwL3IpCtrlIpAddr_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,3),_SwL3IpCtrlIpAddr_Type())
swL3IpCtrlIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpAddr.setStatus(_A)
_SwL3IpCtrlIpSubnetMask_Type=IpAddress
_SwL3IpCtrlIpSubnetMask_Object=MibTableColumn
swL3IpCtrlIpSubnetMask=_SwL3IpCtrlIpSubnetMask_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,4),_SwL3IpCtrlIpSubnetMask_Type())
swL3IpCtrlIpSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpSubnetMask.setStatus(_A)
class _SwL3IpCtrlVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL3IpCtrlVlanName_Type.__name__=_J
_SwL3IpCtrlVlanName_Object=MibTableColumn
swL3IpCtrlVlanName=_SwL3IpCtrlVlanName_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,5),_SwL3IpCtrlVlanName_Type())
swL3IpCtrlVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlVlanName.setStatus(_A)
class _SwL3IpCtrlProxyArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3IpCtrlProxyArp_Type.__name__=_B
_SwL3IpCtrlProxyArp_Object=MibTableColumn
swL3IpCtrlProxyArp=_SwL3IpCtrlProxyArp_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,6),_SwL3IpCtrlProxyArp_Type())
swL3IpCtrlProxyArp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlProxyArp.setStatus(_A)
_SwL3IpCtrlSecondary_Type=TruthValue
_SwL3IpCtrlSecondary_Object=MibTableColumn
swL3IpCtrlSecondary=_SwL3IpCtrlSecondary_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,7),_SwL3IpCtrlSecondary_Type())
swL3IpCtrlSecondary.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlSecondary.setStatus(_A)
class _SwL3IpCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_I,1),('bootp',3),('dhcp',4)))
_SwL3IpCtrlMode_Type.__name__=_B
_SwL3IpCtrlMode_Object=MibTableColumn
swL3IpCtrlMode=_SwL3IpCtrlMode_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,8),_SwL3IpCtrlMode_Type())
swL3IpCtrlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlMode.setStatus(_A)
class _SwL3IpCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3IpCtrlAdminState_Type.__name__=_B
_SwL3IpCtrlAdminState_Object=MibTableColumn
swL3IpCtrlAdminState=_SwL3IpCtrlAdminState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,9),_SwL3IpCtrlAdminState_Type())
swL3IpCtrlAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlAdminState.setStatus(_A)
class _SwL3IpCtrlIpv4AdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3IpCtrlIpv4AdminState_Type.__name__=_B
_SwL3IpCtrlIpv4AdminState_Object=MibTableColumn
swL3IpCtrlIpv4AdminState=_SwL3IpCtrlIpv4AdminState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,10),_SwL3IpCtrlIpv4AdminState_Type())
swL3IpCtrlIpv4AdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpv4AdminState.setStatus(_A)
class _SwL3IpCtrlIpv6AdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3IpCtrlIpv6AdminState_Type.__name__=_B
_SwL3IpCtrlIpv6AdminState_Object=MibTableColumn
swL3IpCtrlIpv6AdminState=_SwL3IpCtrlIpv6AdminState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,12),_SwL3IpCtrlIpv6AdminState_Type())
swL3IpCtrlIpv6AdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpv6AdminState.setStatus(_A)
_SwL3IpCtrlIpv6LinkLocalAddress_Type=Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress=_SwL3IpCtrlIpv6LinkLocalAddress_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,14),_SwL3IpCtrlIpv6LinkLocalAddress_Type())
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalAddress.setStatus(_A)
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type=Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen=_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,15),_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type())
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus(_A)
_SwL3IpCtrlState_Type=RowStatus
_SwL3IpCtrlState_Object=MibTableColumn
swL3IpCtrlState=_SwL3IpCtrlState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,16),_SwL3IpCtrlState_Type())
swL3IpCtrlState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpCtrlState.setStatus(_A)
class _SwL3IpCtrlIpv6LinkLocalAutoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_H,2),(_G,3)))
_SwL3IpCtrlIpv6LinkLocalAutoState_Type.__name__=_B
_SwL3IpCtrlIpv6LinkLocalAutoState_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalAutoState=_SwL3IpCtrlIpv6LinkLocalAutoState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,17),_SwL3IpCtrlIpv6LinkLocalAutoState_Type())
swL3IpCtrlIpv6LinkLocalAutoState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalAutoState.setStatus(_A)
class _SwL3IpCtrlLocalProxyArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3IpCtrlLocalProxyArp_Type.__name__=_B
_SwL3IpCtrlLocalProxyArp_Object=MibTableColumn
swL3IpCtrlLocalProxyArp=_SwL3IpCtrlLocalProxyArp_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,18),_SwL3IpCtrlLocalProxyArp_Type())
swL3IpCtrlLocalProxyArp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlLocalProxyArp.setStatus(_A)
class _SwL3IpCtrlIpMtu_Type(Integer32):defaultValue=1500
_SwL3IpCtrlIpMtu_Type.__name__=_B
_SwL3IpCtrlIpMtu_Object=MibTableColumn
swL3IpCtrlIpMtu=_SwL3IpCtrlIpMtu_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,19),_SwL3IpCtrlIpMtu_Type())
swL3IpCtrlIpMtu.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpCtrlIpMtu.setStatus(_A)
if mibBuilder.loadTexts:swL3IpCtrlIpMtu.setUnits('bytes')
class _SwL3IpCtrlDhcpv6ClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3IpCtrlDhcpv6ClientState_Type.__name__=_B
_SwL3IpCtrlDhcpv6ClientState_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientState=_SwL3IpCtrlDhcpv6ClientState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,20),_SwL3IpCtrlDhcpv6ClientState_Type())
swL3IpCtrlDhcpv6ClientState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientState.setStatus(_A)
class _SwL3IpCtrlIpDirectedBroadcastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3IpCtrlIpDirectedBroadcastState_Type.__name__=_B
_SwL3IpCtrlIpDirectedBroadcastState_Object=MibTableColumn
swL3IpCtrlIpDirectedBroadcastState=_SwL3IpCtrlIpDirectedBroadcastState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,21),_SwL3IpCtrlIpDirectedBroadcastState_Type())
swL3IpCtrlIpDirectedBroadcastState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpDirectedBroadcastState.setStatus(_A)
class _SwL3IpCtrlDhcpv6ClientPDState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3IpCtrlDhcpv6ClientPDState_Type.__name__=_B
_SwL3IpCtrlDhcpv6ClientPDState_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientPDState=_SwL3IpCtrlDhcpv6ClientPDState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,24),_SwL3IpCtrlDhcpv6ClientPDState_Type())
swL3IpCtrlDhcpv6ClientPDState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientPDState.setStatus(_A)
class _SwL3IpCtrlDhcpv6ClientPDPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwL3IpCtrlDhcpv6ClientPDPrefixName_Type.__name__=_J
_SwL3IpCtrlDhcpv6ClientPDPrefixName_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefixName=_SwL3IpCtrlDhcpv6ClientPDPrefixName_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,25),_SwL3IpCtrlDhcpv6ClientPDPrefixName_Type())
swL3IpCtrlDhcpv6ClientPDPrefixName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientPDPrefixName.setStatus(_A)
_SwL3IpCtrlDhcpv6ClientPDPrefix_Type=Ipv6Address
_SwL3IpCtrlDhcpv6ClientPDPrefix_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefix=_SwL3IpCtrlDhcpv6ClientPDPrefix_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,26),_SwL3IpCtrlDhcpv6ClientPDPrefix_Type())
swL3IpCtrlDhcpv6ClientPDPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientPDPrefix.setStatus(_A)
_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Type=Integer32
_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefixLen=_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,3,1,27),_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Type())
swL3IpCtrlDhcpv6ClientPDPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientPDPrefixLen.setStatus(_A)
_SwL3Ipv6CtrlTable_Object=MibTable
swL3Ipv6CtrlTable=_SwL3Ipv6CtrlTable_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4))
if mibBuilder.loadTexts:swL3Ipv6CtrlTable.setStatus(_A)
_SwL3Ipv6CtrlEntry_Object=MibTableRow
swL3Ipv6CtrlEntry=_SwL3Ipv6CtrlEntry_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1))
swL3Ipv6CtrlEntry.setIndexNames((0,_F,_f))
if mibBuilder.loadTexts:swL3Ipv6CtrlEntry.setStatus(_A)
class _SwL3Ipv6CtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6CtrlInterfaceName_Type.__name__=_J
_SwL3Ipv6CtrlInterfaceName_Object=MibTableColumn
swL3Ipv6CtrlInterfaceName=_SwL3Ipv6CtrlInterfaceName_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,1),_SwL3Ipv6CtrlInterfaceName_Type())
swL3Ipv6CtrlInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlInterfaceName.setStatus(_A)
_SwL3Ipv6CtrlMaxReassmblySize_Type=Integer32
_SwL3Ipv6CtrlMaxReassmblySize_Object=MibTableColumn
swL3Ipv6CtrlMaxReassmblySize=_SwL3Ipv6CtrlMaxReassmblySize_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,2),_SwL3Ipv6CtrlMaxReassmblySize_Type())
swL3Ipv6CtrlMaxReassmblySize.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6CtrlMaxReassmblySize.setStatus(_A)
class _SwL3Ipv6CtrlNsRetransTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SwL3Ipv6CtrlNsRetransTimer_Type.__name__=_N
_SwL3Ipv6CtrlNsRetransTimer_Object=MibTableColumn
swL3Ipv6CtrlNsRetransTimer=_SwL3Ipv6CtrlNsRetransTimer_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,3),_SwL3Ipv6CtrlNsRetransTimer_Type())
swL3Ipv6CtrlNsRetransTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlNsRetransTimer.setStatus(_A)
class _SwL3Ipv6CtrlRaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3Ipv6CtrlRaState_Type.__name__=_B
_SwL3Ipv6CtrlRaState_Object=MibTableColumn
swL3Ipv6CtrlRaState=_SwL3Ipv6CtrlRaState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,5),_SwL3Ipv6CtrlRaState_Type())
swL3Ipv6CtrlRaState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaState.setStatus(_A)
class _SwL3Ipv6CtrlRaMinRtrAdvInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1350))
_SwL3Ipv6CtrlRaMinRtrAdvInterval_Type.__name__=_B
_SwL3Ipv6CtrlRaMinRtrAdvInterval_Object=MibTableColumn
swL3Ipv6CtrlRaMinRtrAdvInterval=_SwL3Ipv6CtrlRaMinRtrAdvInterval_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,6),_SwL3Ipv6CtrlRaMinRtrAdvInterval_Type())
swL3Ipv6CtrlRaMinRtrAdvInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaMinRtrAdvInterval.setStatus(_A)
class _SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type.__name__=_B
_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object=MibTableColumn
swL3Ipv6CtrlRaMaxRtrAdvInterval=_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,7),_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type())
swL3Ipv6CtrlRaMaxRtrAdvInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaMaxRtrAdvInterval.setStatus(_A)
class _SwL3Ipv6CtrlRaLifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_SwL3Ipv6CtrlRaLifeTime_Type.__name__=_B
_SwL3Ipv6CtrlRaLifeTime_Object=MibTableColumn
swL3Ipv6CtrlRaLifeTime=_SwL3Ipv6CtrlRaLifeTime_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,8),_SwL3Ipv6CtrlRaLifeTime_Type())
swL3Ipv6CtrlRaLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaLifeTime.setStatus(_A)
class _SwL3Ipv6CtrlRaReachableTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_SwL3Ipv6CtrlRaReachableTime_Type.__name__=_B
_SwL3Ipv6CtrlRaReachableTime_Object=MibTableColumn
swL3Ipv6CtrlRaReachableTime=_SwL3Ipv6CtrlRaReachableTime_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,9),_SwL3Ipv6CtrlRaReachableTime_Type())
swL3Ipv6CtrlRaReachableTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaReachableTime.setStatus(_A)
class _SwL3Ipv6CtrlRaRetransTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SwL3Ipv6CtrlRaRetransTime_Type.__name__=_N
_SwL3Ipv6CtrlRaRetransTime_Object=MibTableColumn
swL3Ipv6CtrlRaRetransTime=_SwL3Ipv6CtrlRaRetransTime_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,10),_SwL3Ipv6CtrlRaRetransTime_Type())
swL3Ipv6CtrlRaRetransTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaRetransTime.setStatus(_A)
class _SwL3Ipv6CtrlRaHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3Ipv6CtrlRaHopLimit_Type.__name__=_B
_SwL3Ipv6CtrlRaHopLimit_Object=MibTableColumn
swL3Ipv6CtrlRaHopLimit=_SwL3Ipv6CtrlRaHopLimit_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,11),_SwL3Ipv6CtrlRaHopLimit_Type())
swL3Ipv6CtrlRaHopLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaHopLimit.setStatus(_A)
class _SwL3Ipv6CtrlRaManagedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3Ipv6CtrlRaManagedFlag_Type.__name__=_B
_SwL3Ipv6CtrlRaManagedFlag_Object=MibTableColumn
swL3Ipv6CtrlRaManagedFlag=_SwL3Ipv6CtrlRaManagedFlag_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,12),_SwL3Ipv6CtrlRaManagedFlag_Type())
swL3Ipv6CtrlRaManagedFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaManagedFlag.setStatus(_A)
class _SwL3Ipv6CtrlRaOtherConfigFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3Ipv6CtrlRaOtherConfigFlag_Type.__name__=_B
_SwL3Ipv6CtrlRaOtherConfigFlag_Object=MibTableColumn
swL3Ipv6CtrlRaOtherConfigFlag=_SwL3Ipv6CtrlRaOtherConfigFlag_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,4,1,13),_SwL3Ipv6CtrlRaOtherConfigFlag_Type())
swL3Ipv6CtrlRaOtherConfigFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaOtherConfigFlag.setStatus(_A)
_SwL3Ipv6AddressCtrlTable_Object=MibTable
swL3Ipv6AddressCtrlTable=_SwL3Ipv6AddressCtrlTable_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5))
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlTable.setStatus(_A)
_SwL3Ipv6AddressCtrlEntry_Object=MibTableRow
swL3Ipv6AddressCtrlEntry=_SwL3Ipv6AddressCtrlEntry_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5,1))
swL3Ipv6AddressCtrlEntry.setIndexNames((0,_F,_g),(0,_F,_h),(0,_F,_i))
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlEntry.setStatus(_A)
class _SwL3Ipv6AddressCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6AddressCtrlInterfaceName_Type.__name__=_J
_SwL3Ipv6AddressCtrlInterfaceName_Object=MibTableColumn
swL3Ipv6AddressCtrlInterfaceName=_SwL3Ipv6AddressCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5,1,1),_SwL3Ipv6AddressCtrlInterfaceName_Type())
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlInterfaceName.setStatus(_A)
_SwL3Ipv6Address_Type=Ipv6Address
_SwL3Ipv6Address_Object=MibTableColumn
swL3Ipv6Address=_SwL3Ipv6Address_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5,1,2),_SwL3Ipv6Address_Type())
swL3Ipv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6Address.setStatus(_A)
_SwL3Ipv6AddressCtrlPrefixLen_Type=Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object=MibTableColumn
swL3Ipv6AddressCtrlPrefixLen=_SwL3Ipv6AddressCtrlPrefixLen_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5,1,3),_SwL3Ipv6AddressCtrlPrefixLen_Type())
swL3Ipv6AddressCtrlPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlPrefixLen.setStatus(_A)
class _SwL3Ipv6AddressCtrlPreferredLifeTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwL3Ipv6AddressCtrlPreferredLifeTime_Type.__name__=_N
_SwL3Ipv6AddressCtrlPreferredLifeTime_Object=MibTableColumn
swL3Ipv6AddressCtrlPreferredLifeTime=_SwL3Ipv6AddressCtrlPreferredLifeTime_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5,1,4),_SwL3Ipv6AddressCtrlPreferredLifeTime_Type())
swL3Ipv6AddressCtrlPreferredLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlPreferredLifeTime.setStatus(_A)
class _SwL3Ipv6AddressCtrlValidLifeTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwL3Ipv6AddressCtrlValidLifeTime_Type.__name__=_N
_SwL3Ipv6AddressCtrlValidLifeTime_Object=MibTableColumn
swL3Ipv6AddressCtrlValidLifeTime=_SwL3Ipv6AddressCtrlValidLifeTime_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5,1,5),_SwL3Ipv6AddressCtrlValidLifeTime_Type())
swL3Ipv6AddressCtrlValidLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlValidLifeTime.setStatus(_A)
class _SwL3Ipv6AddressCtrlOnLinkFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3Ipv6AddressCtrlOnLinkFlag_Type.__name__=_B
_SwL3Ipv6AddressCtrlOnLinkFlag_Object=MibTableColumn
swL3Ipv6AddressCtrlOnLinkFlag=_SwL3Ipv6AddressCtrlOnLinkFlag_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5,1,6),_SwL3Ipv6AddressCtrlOnLinkFlag_Type())
swL3Ipv6AddressCtrlOnLinkFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlOnLinkFlag.setStatus(_A)
class _SwL3Ipv6AddressCtrlAutonomousFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3Ipv6AddressCtrlAutonomousFlag_Type.__name__=_B
_SwL3Ipv6AddressCtrlAutonomousFlag_Object=MibTableColumn
swL3Ipv6AddressCtrlAutonomousFlag=_SwL3Ipv6AddressCtrlAutonomousFlag_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5,1,7),_SwL3Ipv6AddressCtrlAutonomousFlag_Type())
swL3Ipv6AddressCtrlAutonomousFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlAutonomousFlag.setStatus(_A)
_SwL3Ipv6AddressCtrlState_Type=RowStatus
_SwL3Ipv6AddressCtrlState_Object=MibTableColumn
swL3Ipv6AddressCtrlState=_SwL3Ipv6AddressCtrlState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,5,1,8),_SwL3Ipv6AddressCtrlState_Type())
swL3Ipv6AddressCtrlState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlState.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlTable_Object=MibTable
swL3Ipv6DHCPv6CPDAddrCtrlTable=_SwL3Ipv6DHCPv6CPDAddrCtrlTable_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,6))
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlTable.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlEntry_Object=MibTableRow
swL3Ipv6DHCPv6CPDAddrCtrlEntry=_SwL3Ipv6DHCPv6CPDAddrCtrlEntry_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,6,1))
swL3Ipv6DHCPv6CPDAddrCtrlEntry.setIndexNames((0,_F,_j),(0,_F,_k),(0,_F,_l),(0,_F,_m))
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlEntry.setStatus(_A)
class _SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type.__name__=_J
_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName=_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,6,1,1),_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type())
swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName.setStatus(_A)
class _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type.__name__=_J
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlPrefixName=_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,6,1,2),_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type())
swL3Ipv6DHCPv6CPDAddrCtrlPrefixName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlPrefixName.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Type=Ipv6Address
_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr=_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,6,1,3),_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Type())
swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Type=Integer32
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen=_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,6,1,4),_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Type())
swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen.setStatus(_A)
_SwL3Ipv6DHCPv6CPDAddrCtrlState_Type=RowStatus
_SwL3Ipv6DHCPv6CPDAddrCtrlState_Object=MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlState=_SwL3Ipv6DHCPv6CPDAddrCtrlState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,6,1,5),_SwL3Ipv6DHCPv6CPDAddrCtrlState_Type())
swL3Ipv6DHCPv6CPDAddrCtrlState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3Ipv6DHCPv6CPDAddrCtrlState.setStatus(_A)
class _SwL3IpCtrlAllIpIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_H,2),(_G,3)))
_SwL3IpCtrlAllIpIfState_Type.__name__=_B
_SwL3IpCtrlAllIpIfState_Object=MibScalar
swL3IpCtrlAllIpIfState=_SwL3IpCtrlAllIpIfState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,7),_SwL3IpCtrlAllIpIfState_Type())
swL3IpCtrlAllIpIfState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlAllIpIfState.setStatus(_A)
_SwL3LoopBackIpCtrlTable_Object=MibTable
swL3LoopBackIpCtrlTable=_SwL3LoopBackIpCtrlTable_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,8))
if mibBuilder.loadTexts:swL3LoopBackIpCtrlTable.setStatus(_A)
_SwL3LoopBackIpCtrlEntry_Object=MibTableRow
swL3LoopBackIpCtrlEntry=_SwL3LoopBackIpCtrlEntry_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,8,1))
swL3LoopBackIpCtrlEntry.setIndexNames((0,_F,_n))
if mibBuilder.loadTexts:swL3LoopBackIpCtrlEntry.setStatus(_A)
class _SwL3LoopBackIpCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3LoopBackIpCtrlInterfaceName_Type.__name__=_J
_SwL3LoopBackIpCtrlInterfaceName_Object=MibTableColumn
swL3LoopBackIpCtrlInterfaceName=_SwL3LoopBackIpCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,8,1,1),_SwL3LoopBackIpCtrlInterfaceName_Type())
swL3LoopBackIpCtrlInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3LoopBackIpCtrlInterfaceName.setStatus(_A)
class _SwL3LoopBackIpCtrlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3LoopBackIpCtrlIfIndex_Type.__name__=_B
_SwL3LoopBackIpCtrlIfIndex_Object=MibTableColumn
swL3LoopBackIpCtrlIfIndex=_SwL3LoopBackIpCtrlIfIndex_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,8,1,2),_SwL3LoopBackIpCtrlIfIndex_Type())
swL3LoopBackIpCtrlIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3LoopBackIpCtrlIfIndex.setStatus(_A)
_SwL3LoopBackIpCtrlIpAddr_Type=IpAddress
_SwL3LoopBackIpCtrlIpAddr_Object=MibTableColumn
swL3LoopBackIpCtrlIpAddr=_SwL3LoopBackIpCtrlIpAddr_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,8,1,3),_SwL3LoopBackIpCtrlIpAddr_Type())
swL3LoopBackIpCtrlIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3LoopBackIpCtrlIpAddr.setStatus(_A)
_SwL3LoopBackIpCtrlIpSubnetMask_Type=IpAddress
_SwL3LoopBackIpCtrlIpSubnetMask_Object=MibTableColumn
swL3LoopBackIpCtrlIpSubnetMask=_SwL3LoopBackIpCtrlIpSubnetMask_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,8,1,4),_SwL3LoopBackIpCtrlIpSubnetMask_Type())
swL3LoopBackIpCtrlIpSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3LoopBackIpCtrlIpSubnetMask.setStatus(_A)
class _SwL3LoopBackIpCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3LoopBackIpCtrlAdminState_Type.__name__=_B
_SwL3LoopBackIpCtrlAdminState_Object=MibTableColumn
swL3LoopBackIpCtrlAdminState=_SwL3LoopBackIpCtrlAdminState_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,8,1,5),_SwL3LoopBackIpCtrlAdminState_Type())
swL3LoopBackIpCtrlAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3LoopBackIpCtrlAdminState.setStatus(_A)
_SwL3LoopBackIpCtrlRowStatus_Type=RowStatus
_SwL3LoopBackIpCtrlRowStatus_Object=MibTableColumn
swL3LoopBackIpCtrlRowStatus=_SwL3LoopBackIpCtrlRowStatus_Object((1,3,6,1,4,1,171,11,118,5,3,2,1,8,1,6),_SwL3LoopBackIpCtrlRowStatus_Type())
swL3LoopBackIpCtrlRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3LoopBackIpCtrlRowStatus.setStatus(_A)
_SwL3IpFdbMgmt_ObjectIdentity=ObjectIdentity
swL3IpFdbMgmt=_SwL3IpFdbMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,2,2))
_SwL3IpFdbInfoTable_Object=MibTable
swL3IpFdbInfoTable=_SwL3IpFdbInfoTable_Object((1,3,6,1,4,1,171,11,118,5,3,2,2,1))
if mibBuilder.loadTexts:swL3IpFdbInfoTable.setStatus(_A)
_SwL3IpFdbInfoEntry_Object=MibTableRow
swL3IpFdbInfoEntry=_SwL3IpFdbInfoEntry_Object((1,3,6,1,4,1,171,11,118,5,3,2,2,1,1))
swL3IpFdbInfoEntry.setIndexNames((0,_F,_o))
if mibBuilder.loadTexts:swL3IpFdbInfoEntry.setStatus(_A)
_SwL3IpFdbInfoIpAddr_Type=IpAddress
_SwL3IpFdbInfoIpAddr_Object=MibTableColumn
swL3IpFdbInfoIpAddr=_SwL3IpFdbInfoIpAddr_Object((1,3,6,1,4,1,171,11,118,5,3,2,2,1,1,1),_SwL3IpFdbInfoIpAddr_Type())
swL3IpFdbInfoIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpFdbInfoIpAddr.setStatus(_A)
_SwL3IpFdbInfoIpSubnetMask_Type=IpAddress
_SwL3IpFdbInfoIpSubnetMask_Object=MibTableColumn
swL3IpFdbInfoIpSubnetMask=_SwL3IpFdbInfoIpSubnetMask_Object((1,3,6,1,4,1,171,11,118,5,3,2,2,1,1,2),_SwL3IpFdbInfoIpSubnetMask_Type())
swL3IpFdbInfoIpSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpFdbInfoIpSubnetMask.setStatus(_A)
class _SwL3IpFdbInfoPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpFdbInfoPort_Type.__name__=_B
_SwL3IpFdbInfoPort_Object=MibTableColumn
swL3IpFdbInfoPort=_SwL3IpFdbInfoPort_Object((1,3,6,1,4,1,171,11,118,5,3,2,2,1,1,3),_SwL3IpFdbInfoPort_Type())
swL3IpFdbInfoPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpFdbInfoPort.setStatus(_A)
class _SwL3IpFdbInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_V,2),('dynamic',3)))
_SwL3IpFdbInfoType_Type.__name__=_B
_SwL3IpFdbInfoType_Object=MibTableColumn
swL3IpFdbInfoType=_SwL3IpFdbInfoType_Object((1,3,6,1,4,1,171,11,118,5,3,2,2,1,1,4),_SwL3IpFdbInfoType_Type())
swL3IpFdbInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpFdbInfoType.setStatus(_A)
class _SwL3IpArpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpArpAgingTime_Type.__name__=_B
_SwL3IpArpAgingTime_Object=MibScalar
swL3IpArpAgingTime=_SwL3IpArpAgingTime_Object((1,3,6,1,4,1,171,11,118,5,3,2,4),_SwL3IpArpAgingTime_Type())
swL3IpArpAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpArpAgingTime.setStatus(_A)
_SwL3IpStaticRouteTable_Object=MibTable
swL3IpStaticRouteTable=_SwL3IpStaticRouteTable_Object((1,3,6,1,4,1,171,11,118,5,3,2,5))
if mibBuilder.loadTexts:swL3IpStaticRouteTable.setStatus(_A)
_SwL3IpStaticRouteEntry_Object=MibTableRow
swL3IpStaticRouteEntry=_SwL3IpStaticRouteEntry_Object((1,3,6,1,4,1,171,11,118,5,3,2,5,1))
swL3IpStaticRouteEntry.setIndexNames((0,_F,_W),(0,_F,_X),(0,_F,_p))
if mibBuilder.loadTexts:swL3IpStaticRouteEntry.setStatus(_A)
_SwL3IpStaticRouteDest_Type=IpAddress
_SwL3IpStaticRouteDest_Object=MibTableColumn
swL3IpStaticRouteDest=_SwL3IpStaticRouteDest_Object((1,3,6,1,4,1,171,11,118,5,3,2,5,1,1),_SwL3IpStaticRouteDest_Type())
swL3IpStaticRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpStaticRouteDest.setStatus(_A)
_SwL3IpStaticRouteMask_Type=IpAddress
_SwL3IpStaticRouteMask_Object=MibTableColumn
swL3IpStaticRouteMask=_SwL3IpStaticRouteMask_Object((1,3,6,1,4,1,171,11,118,5,3,2,5,1,2),_SwL3IpStaticRouteMask_Type())
swL3IpStaticRouteMask.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpStaticRouteMask.setStatus(_A)
class _SwL3IpStaticRouteBkupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),(_q,2),(_L,3)))
_SwL3IpStaticRouteBkupState_Type.__name__=_B
_SwL3IpStaticRouteBkupState_Object=MibTableColumn
swL3IpStaticRouteBkupState=_SwL3IpStaticRouteBkupState_Object((1,3,6,1,4,1,171,11,118,5,3,2,5,1,3),_SwL3IpStaticRouteBkupState_Type())
swL3IpStaticRouteBkupState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpStaticRouteBkupState.setStatus(_A)
_SwL3IpStaticRouteNextHop_Type=IpAddress
_SwL3IpStaticRouteNextHop_Object=MibTableColumn
swL3IpStaticRouteNextHop=_SwL3IpStaticRouteNextHop_Object((1,3,6,1,4,1,171,11,118,5,3,2,5,1,4),_SwL3IpStaticRouteNextHop_Type())
swL3IpStaticRouteNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpStaticRouteNextHop.setStatus(_A)
class _SwL3IpStaticRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3IpStaticRouteMetric_Type.__name__=_B
_SwL3IpStaticRouteMetric_Object=MibTableColumn
swL3IpStaticRouteMetric=_SwL3IpStaticRouteMetric_Object((1,3,6,1,4,1,171,11,118,5,3,2,5,1,5),_SwL3IpStaticRouteMetric_Type())
swL3IpStaticRouteMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpStaticRouteMetric.setStatus(_A)
class _SwL3IpStaticRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_r,2),('valid',3),('active',4),('inActive',5)))
_SwL3IpStaticRouteStatus_Type.__name__=_B
_SwL3IpStaticRouteStatus_Object=MibTableColumn
swL3IpStaticRouteStatus=_SwL3IpStaticRouteStatus_Object((1,3,6,1,4,1,171,11,118,5,3,2,5,1,6),_SwL3IpStaticRouteStatus_Type())
swL3IpStaticRouteStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpStaticRouteStatus.setStatus(_A)
class _SwL3IpStaticRouteWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_SwL3IpStaticRouteWeight_Type.__name__=_B
_SwL3IpStaticRouteWeight_Object=MibTableColumn
swL3IpStaticRouteWeight=_SwL3IpStaticRouteWeight_Object((1,3,6,1,4,1,171,11,118,5,3,2,5,1,7),_SwL3IpStaticRouteWeight_Type())
swL3IpStaticRouteWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpStaticRouteWeight.setStatus(_A)
_SwL3IpStaticRouteInterfaceName_Type=DisplayString
_SwL3IpStaticRouteInterfaceName_Object=MibTableColumn
swL3IpStaticRouteInterfaceName=_SwL3IpStaticRouteInterfaceName_Object((1,3,6,1,4,1,171,11,118,5,3,2,5,1,8),_SwL3IpStaticRouteInterfaceName_Type())
swL3IpStaticRouteInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpStaticRouteInterfaceName.setStatus(_A)
_SwL3IpMcastMgmt_ObjectIdentity=ObjectIdentity
swL3IpMcastMgmt=_SwL3IpMcastMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,2,6))
_SwL3IpMcastStaticRouteTable_Object=MibTable
swL3IpMcastStaticRouteTable=_SwL3IpMcastStaticRouteTable_Object((1,3,6,1,4,1,171,11,118,5,3,2,6,1))
if mibBuilder.loadTexts:swL3IpMcastStaticRouteTable.setStatus(_A)
_SwL3IpMcastStaticRouteEntry_Object=MibTableRow
swL3IpMcastStaticRouteEntry=_SwL3IpMcastStaticRouteEntry_Object((1,3,6,1,4,1,171,11,118,5,3,2,6,1,1))
swL3IpMcastStaticRouteEntry.setIndexNames((0,_F,_s),(0,_F,_t))
if mibBuilder.loadTexts:swL3IpMcastStaticRouteEntry.setStatus(_A)
_SwL3IpMcastStaticRouteIpmrouteAddr_Type=IpAddress
_SwL3IpMcastStaticRouteIpmrouteAddr_Object=MibTableColumn
swL3IpMcastStaticRouteIpmrouteAddr=_SwL3IpMcastStaticRouteIpmrouteAddr_Object((1,3,6,1,4,1,171,11,118,5,3,2,6,1,1,1),_SwL3IpMcastStaticRouteIpmrouteAddr_Type())
swL3IpMcastStaticRouteIpmrouteAddr.setMaxAccess(_Y)
if mibBuilder.loadTexts:swL3IpMcastStaticRouteIpmrouteAddr.setStatus(_A)
_SwL3IpMcastStaticRouteIpmrouteMask_Type=IpAddress
_SwL3IpMcastStaticRouteIpmrouteMask_Object=MibTableColumn
swL3IpMcastStaticRouteIpmrouteMask=_SwL3IpMcastStaticRouteIpmrouteMask_Object((1,3,6,1,4,1,171,11,118,5,3,2,6,1,1,2),_SwL3IpMcastStaticRouteIpmrouteMask_Type())
swL3IpMcastStaticRouteIpmrouteMask.setMaxAccess(_Y)
if mibBuilder.loadTexts:swL3IpMcastStaticRouteIpmrouteMask.setStatus(_A)
_SwL3IpMcastStaticRouteRpfAddr_Type=IpAddress
_SwL3IpMcastStaticRouteRpfAddr_Object=MibTableColumn
swL3IpMcastStaticRouteRpfAddr=_SwL3IpMcastStaticRouteRpfAddr_Object((1,3,6,1,4,1,171,11,118,5,3,2,6,1,1,3),_SwL3IpMcastStaticRouteRpfAddr_Type())
swL3IpMcastStaticRouteRpfAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpMcastStaticRouteRpfAddr.setStatus(_A)
_SwL3IpMcastStaticRouteRowStatus_Type=RowStatus
_SwL3IpMcastStaticRouteRowStatus_Object=MibTableColumn
swL3IpMcastStaticRouteRowStatus=_SwL3IpMcastStaticRouteRowStatus_Object((1,3,6,1,4,1,171,11,118,5,3,2,6,1,1,4),_SwL3IpMcastStaticRouteRowStatus_Type())
swL3IpMcastStaticRouteRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpMcastStaticRouteRowStatus.setStatus(_A)
_SwL3IpStaticRouteTunnelTable_Object=MibTable
swL3IpStaticRouteTunnelTable=_SwL3IpStaticRouteTunnelTable_Object((1,3,6,1,4,1,171,11,118,5,3,2,7))
if mibBuilder.loadTexts:swL3IpStaticRouteTunnelTable.setStatus(_A)
_SwL3IpStaticRouteTunnelEntry_Object=MibTableRow
swL3IpStaticRouteTunnelEntry=_SwL3IpStaticRouteTunnelEntry_Object((1,3,6,1,4,1,171,11,118,5,3,2,7,1))
swL3IpStaticRouteTunnelEntry.setIndexNames((0,_F,_W),(0,_F,_X),(0,_F,_u))
if mibBuilder.loadTexts:swL3IpStaticRouteTunnelEntry.setStatus(_A)
class _SwL3IpStaticRouteTunnelInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwL3IpStaticRouteTunnelInterfaceName_Type.__name__=_J
_SwL3IpStaticRouteTunnelInterfaceName_Object=MibTableColumn
swL3IpStaticRouteTunnelInterfaceName=_SwL3IpStaticRouteTunnelInterfaceName_Object((1,3,6,1,4,1,171,11,118,5,3,2,7,1,1),_SwL3IpStaticRouteTunnelInterfaceName_Type())
swL3IpStaticRouteTunnelInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpStaticRouteTunnelInterfaceName.setStatus(_A)
_SwL3IpStaticRouteTunnelRowStatus_Type=RowStatus
_SwL3IpStaticRouteTunnelRowStatus_Object=MibTableColumn
swL3IpStaticRouteTunnelRowStatus=_SwL3IpStaticRouteTunnelRowStatus_Object((1,3,6,1,4,1,171,11,118,5,3,2,7,1,2),_SwL3IpStaticRouteTunnelRowStatus_Type())
swL3IpStaticRouteTunnelRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpStaticRouteTunnelRowStatus.setStatus(_A)
_SwL3RelayMgmt_ObjectIdentity=ObjectIdentity
swL3RelayMgmt=_SwL3RelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,3))
_SwL3RelayDnsMgmt_ObjectIdentity=ObjectIdentity
swL3RelayDnsMgmt=_SwL3RelayDnsMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,3,3))
class _SwL3RelayDnsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_SwL3RelayDnsState_Type.__name__=_B
_SwL3RelayDnsState_Object=MibScalar
swL3RelayDnsState=_SwL3RelayDnsState_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,1),_SwL3RelayDnsState_Type())
swL3RelayDnsState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsState.setStatus(_A)
_SwL3RelayDnsPrimaryServer_Type=IpAddress
_SwL3RelayDnsPrimaryServer_Object=MibScalar
swL3RelayDnsPrimaryServer=_SwL3RelayDnsPrimaryServer_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,2),_SwL3RelayDnsPrimaryServer_Type())
swL3RelayDnsPrimaryServer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsPrimaryServer.setStatus(_A)
_SwL3RelayDnsSecondaryServer_Type=IpAddress
_SwL3RelayDnsSecondaryServer_Object=MibScalar
swL3RelayDnsSecondaryServer=_SwL3RelayDnsSecondaryServer_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,3),_SwL3RelayDnsSecondaryServer_Type())
swL3RelayDnsSecondaryServer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsSecondaryServer.setStatus(_A)
class _SwL3RelayDnsCacheState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_SwL3RelayDnsCacheState_Type.__name__=_B
_SwL3RelayDnsCacheState_Object=MibScalar
swL3RelayDnsCacheState=_SwL3RelayDnsCacheState_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,4),_SwL3RelayDnsCacheState_Type())
swL3RelayDnsCacheState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsCacheState.setStatus(_A)
class _SwL3RelayDnsStaticTableState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_SwL3RelayDnsStaticTableState_Type.__name__=_B
_SwL3RelayDnsStaticTableState_Object=MibScalar
swL3RelayDnsStaticTableState=_SwL3RelayDnsStaticTableState_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,5),_SwL3RelayDnsStaticTableState_Type())
swL3RelayDnsStaticTableState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsStaticTableState.setStatus(_A)
_SwL3RelayDnsCtrlTable_Object=MibTable
swL3RelayDnsCtrlTable=_SwL3RelayDnsCtrlTable_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,6))
if mibBuilder.loadTexts:swL3RelayDnsCtrlTable.setStatus(_A)
_SwL3RelayDnsCtrlEntry_Object=MibTableRow
swL3RelayDnsCtrlEntry=_SwL3RelayDnsCtrlEntry_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,6,1))
swL3RelayDnsCtrlEntry.setIndexNames((0,_F,_v),(0,_F,_w))
if mibBuilder.loadTexts:swL3RelayDnsCtrlEntry.setStatus(_A)
class _SwL3RelayDnsCtrlDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwL3RelayDnsCtrlDomainName_Type.__name__=_J
_SwL3RelayDnsCtrlDomainName_Object=MibTableColumn
swL3RelayDnsCtrlDomainName=_SwL3RelayDnsCtrlDomainName_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,6,1,1),_SwL3RelayDnsCtrlDomainName_Type())
swL3RelayDnsCtrlDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDnsCtrlDomainName.setStatus(_A)
_SwL3RelayDnsCtrlIpAddr_Type=IpAddress
_SwL3RelayDnsCtrlIpAddr_Object=MibTableColumn
swL3RelayDnsCtrlIpAddr=_SwL3RelayDnsCtrlIpAddr_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,6,1,2),_SwL3RelayDnsCtrlIpAddr_Type())
swL3RelayDnsCtrlIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RelayDnsCtrlIpAddr.setStatus(_A)
class _SwL3RelayDnsCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_r,2),('valid',3)))
_SwL3RelayDnsCtrlState_Type.__name__=_B
_SwL3RelayDnsCtrlState_Object=MibTableColumn
swL3RelayDnsCtrlState=_SwL3RelayDnsCtrlState_Object((1,3,6,1,4,1,171,11,118,5,3,3,3,6,1,3),_SwL3RelayDnsCtrlState_Type())
swL3RelayDnsCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsCtrlState.setStatus(_A)
_SwL3Md5Table_Object=MibTable
swL3Md5Table=_SwL3Md5Table_Object((1,3,6,1,4,1,171,11,118,5,3,4))
if mibBuilder.loadTexts:swL3Md5Table.setStatus(_A)
_SwL3Md5Entry_Object=MibTableRow
swL3Md5Entry=_SwL3Md5Entry_Object((1,3,6,1,4,1,171,11,118,5,3,4,1))
swL3Md5Entry.setIndexNames((0,_F,_x))
if mibBuilder.loadTexts:swL3Md5Entry.setStatus(_A)
class _SwL3Md5KeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL3Md5KeyId_Type.__name__=_B
_SwL3Md5KeyId_Object=MibTableColumn
swL3Md5KeyId=_SwL3Md5KeyId_Object((1,3,6,1,4,1,171,11,118,5,3,4,1,1),_SwL3Md5KeyId_Type())
swL3Md5KeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Md5KeyId.setStatus(_A)
class _SwL3Md5Key_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SwL3Md5Key_Type.__name__=_J
_SwL3Md5Key_Object=MibTableColumn
swL3Md5Key=_SwL3Md5Key_Object((1,3,6,1,4,1,171,11,118,5,3,4,1,2),_SwL3Md5Key_Type())
swL3Md5Key.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3Md5Key.setStatus(_A)
_SwL3Md5RowStatus_Type=RowStatus
_SwL3Md5RowStatus_Object=MibTableColumn
swL3Md5RowStatus=_SwL3Md5RowStatus_Object((1,3,6,1,4,1,171,11,118,5,3,4,1,3),_SwL3Md5RowStatus_Type())
swL3Md5RowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3Md5RowStatus.setStatus(_A)
_SwL3RouteRedistriTable_Object=MibTable
swL3RouteRedistriTable=_SwL3RouteRedistriTable_Object((1,3,6,1,4,1,171,11,118,5,3,5))
if mibBuilder.loadTexts:swL3RouteRedistriTable.setStatus(_A)
_SwL3RouteRedistriEntry_Object=MibTableRow
swL3RouteRedistriEntry=_SwL3RouteRedistriEntry_Object((1,3,6,1,4,1,171,11,118,5,3,5,1))
swL3RouteRedistriEntry.setIndexNames((0,_F,_y),(0,_F,_z))
if mibBuilder.loadTexts:swL3RouteRedistriEntry.setStatus(_A)
class _SwL3RouteRedistriSrcProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('rip',2),('ospf',3),(_V,4),('local',5),('bgp',6)))
_SwL3RouteRedistriSrcProtocol_Type.__name__=_B
_SwL3RouteRedistriSrcProtocol_Object=MibTableColumn
swL3RouteRedistriSrcProtocol=_SwL3RouteRedistriSrcProtocol_Object((1,3,6,1,4,1,171,11,118,5,3,5,1,1),_SwL3RouteRedistriSrcProtocol_Type())
swL3RouteRedistriSrcProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RouteRedistriSrcProtocol.setStatus(_A)
class _SwL3RouteRedistriDstProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,6)));namedValues=NamedValues(*((_I,1),('rip',2),('ospf',3),('bgp',6)))
_SwL3RouteRedistriDstProtocol_Type.__name__=_B
_SwL3RouteRedistriDstProtocol_Object=MibTableColumn
swL3RouteRedistriDstProtocol=_SwL3RouteRedistriDstProtocol_Object((1,3,6,1,4,1,171,11,118,5,3,5,1,2),_SwL3RouteRedistriDstProtocol_Type())
swL3RouteRedistriDstProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RouteRedistriDstProtocol.setStatus(_A)
class _SwL3RouteRedistriType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_I,1),('all',2),(_P,3),(_Q,4),('internal',5),('external',6),('inter-E1',7),('inter-E2',8),('extType1',9),('extType2',10)))
_SwL3RouteRedistriType_Type.__name__=_B
_SwL3RouteRedistriType_Object=MibTableColumn
swL3RouteRedistriType=_SwL3RouteRedistriType_Object((1,3,6,1,4,1,171,11,118,5,3,5,1,3),_SwL3RouteRedistriType_Type())
swL3RouteRedistriType.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RouteRedistriType.setStatus(_A)
_SwL3RouteRedistriMetric_Type=Unsigned32
_SwL3RouteRedistriMetric_Object=MibTableColumn
swL3RouteRedistriMetric=_SwL3RouteRedistriMetric_Object((1,3,6,1,4,1,171,11,118,5,3,5,1,4),_SwL3RouteRedistriMetric_Type())
swL3RouteRedistriMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RouteRedistriMetric.setStatus(_A)
_SwL3RouteRedistriRowStatus_Type=RowStatus
_SwL3RouteRedistriRowStatus_Object=MibTableColumn
swL3RouteRedistriRowStatus=_SwL3RouteRedistriRowStatus_Object((1,3,6,1,4,1,171,11,118,5,3,5,1,5),_SwL3RouteRedistriRowStatus_Type())
swL3RouteRedistriRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RouteRedistriRowStatus.setStatus(_A)
class _SwL3RouteRedistriRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SwL3RouteRedistriRouteMapName_Type.__name__=_J
_SwL3RouteRedistriRouteMapName_Object=MibTableColumn
swL3RouteRedistriRouteMapName=_SwL3RouteRedistriRouteMapName_Object((1,3,6,1,4,1,171,11,118,5,3,5,1,6),_SwL3RouteRedistriRouteMapName_Type())
swL3RouteRedistriRouteMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RouteRedistriRouteMapName.setStatus(_A)
_SwL3OspfHostTable_Object=MibTable
swL3OspfHostTable=_SwL3OspfHostTable_Object((1,3,6,1,4,1,171,11,118,5,3,6))
if mibBuilder.loadTexts:swL3OspfHostTable.setStatus(_A)
_SwL3OspfHostEntry_Object=MibTableRow
swL3OspfHostEntry=_SwL3OspfHostEntry_Object((1,3,6,1,4,1,171,11,118,5,3,6,1))
swL3OspfHostEntry.setIndexNames((0,_F,_A0),(0,_F,_A1))
if mibBuilder.loadTexts:swL3OspfHostEntry.setStatus(_A)
_SwL3OspfHostIpAddress_Type=IpAddress
_SwL3OspfHostIpAddress_Object=MibTableColumn
swL3OspfHostIpAddress=_SwL3OspfHostIpAddress_Object((1,3,6,1,4,1,171,11,118,5,3,6,1,1),_SwL3OspfHostIpAddress_Type())
swL3OspfHostIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfHostIpAddress.setStatus(_A)
_SwL3OspfHostTOS_Type=TOSType
_SwL3OspfHostTOS_Object=MibTableColumn
swL3OspfHostTOS=_SwL3OspfHostTOS_Object((1,3,6,1,4,1,171,11,118,5,3,6,1,2),_SwL3OspfHostTOS_Type())
swL3OspfHostTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfHostTOS.setStatus(_A)
_SwL3OspfHostMetric_Type=Metric
_SwL3OspfHostMetric_Object=MibTableColumn
swL3OspfHostMetric=_SwL3OspfHostMetric_Object((1,3,6,1,4,1,171,11,118,5,3,6,1,3),_SwL3OspfHostMetric_Type())
swL3OspfHostMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3OspfHostMetric.setStatus(_A)
_SwL3OspfHostAreaID_Type=AreaID
_SwL3OspfHostAreaID_Object=MibTableColumn
swL3OspfHostAreaID=_SwL3OspfHostAreaID_Object((1,3,6,1,4,1,171,11,118,5,3,6,1,4),_SwL3OspfHostAreaID_Type())
swL3OspfHostAreaID.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3OspfHostAreaID.setStatus(_A)
_SwL3OspfHostStatus_Type=RowStatus
_SwL3OspfHostStatus_Object=MibTableColumn
swL3OspfHostStatus=_SwL3OspfHostStatus_Object((1,3,6,1,4,1,171,11,118,5,3,6,1,5),_SwL3OspfHostStatus_Type())
swL3OspfHostStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3OspfHostStatus.setStatus(_A)
_SwL3ospfVirtIfTable_Object=MibTable
swL3ospfVirtIfTable=_SwL3ospfVirtIfTable_Object((1,3,6,1,4,1,171,11,118,5,3,7))
if mibBuilder.loadTexts:swL3ospfVirtIfTable.setStatus(_A)
_SwL3ospfVirtIfEntry_Object=MibTableRow
swL3ospfVirtIfEntry=_SwL3ospfVirtIfEntry_Object((1,3,6,1,4,1,171,11,118,5,3,7,1))
swL3ospfVirtIfEntry.setIndexNames((0,_F,_A2),(0,_F,_A3))
if mibBuilder.loadTexts:swL3ospfVirtIfEntry.setStatus(_A)
_SwL3ospfVirtIfAreaId_Type=AreaID
_SwL3ospfVirtIfAreaId_Object=MibTableColumn
swL3ospfVirtIfAreaId=_SwL3ospfVirtIfAreaId_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,1),_SwL3ospfVirtIfAreaId_Type())
swL3ospfVirtIfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfAreaId.setStatus(_A)
_SwL3ospfVirtIfNeighbor_Type=RouterID
_SwL3ospfVirtIfNeighbor_Object=MibTableColumn
swL3ospfVirtIfNeighbor=_SwL3ospfVirtIfNeighbor_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,2),_SwL3ospfVirtIfNeighbor_Type())
swL3ospfVirtIfNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfNeighbor.setStatus(_A)
class _SwL3ospfVirtIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_SwL3ospfVirtIfTransitDelay_Type.__name__=_M
_SwL3ospfVirtIfTransitDelay_Object=MibTableColumn
swL3ospfVirtIfTransitDelay=_SwL3ospfVirtIfTransitDelay_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,3),_SwL3ospfVirtIfTransitDelay_Type())
swL3ospfVirtIfTransitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfTransitDelay.setStatus(_A)
class _SwL3ospfVirtIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_SwL3ospfVirtIfRetransInterval_Type.__name__=_M
_SwL3ospfVirtIfRetransInterval_Object=MibTableColumn
swL3ospfVirtIfRetransInterval=_SwL3ospfVirtIfRetransInterval_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,4),_SwL3ospfVirtIfRetransInterval_Type())
swL3ospfVirtIfRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfRetransInterval.setStatus(_A)
class _SwL3ospfVirtIfHelloInterval_Type(HelloRange):defaultValue=10
_SwL3ospfVirtIfHelloInterval_Type.__name__=_S
_SwL3ospfVirtIfHelloInterval_Object=MibTableColumn
swL3ospfVirtIfHelloInterval=_SwL3ospfVirtIfHelloInterval_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,5),_SwL3ospfVirtIfHelloInterval_Type())
swL3ospfVirtIfHelloInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfHelloInterval.setStatus(_A)
class _SwL3ospfVirtIfRtrDeadInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3ospfVirtIfRtrDeadInterval_Type.__name__=_B
_SwL3ospfVirtIfRtrDeadInterval_Object=MibTableColumn
swL3ospfVirtIfRtrDeadInterval=_SwL3ospfVirtIfRtrDeadInterval_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,6),_SwL3ospfVirtIfRtrDeadInterval_Type())
swL3ospfVirtIfRtrDeadInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfRtrDeadInterval.setStatus(_A)
class _SwL3ospfVirtIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_Z,1),(_a,4)))
_SwL3ospfVirtIfState_Type.__name__=_B
_SwL3ospfVirtIfState_Object=MibTableColumn
swL3ospfVirtIfState=_SwL3ospfVirtIfState_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,7),_SwL3ospfVirtIfState_Type())
swL3ospfVirtIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfState.setStatus(_A)
_SwL3ospfVirtIfEvents_Type=Counter32
_SwL3ospfVirtIfEvents_Object=MibTableColumn
swL3ospfVirtIfEvents=_SwL3ospfVirtIfEvents_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,8),_SwL3ospfVirtIfEvents_Type())
swL3ospfVirtIfEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfEvents.setStatus(_A)
class _SwL3ospfVirtIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3ospfVirtIfAuthType_Type.__name__=_B
_SwL3ospfVirtIfAuthType_Object=MibTableColumn
swL3ospfVirtIfAuthType=_SwL3ospfVirtIfAuthType_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,9),_SwL3ospfVirtIfAuthType_Type())
swL3ospfVirtIfAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfAuthType.setStatus(_A)
class _SwL3ospfVirtIfAuthKey_Type(OctetString):defaultHexValue=_A4;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SwL3ospfVirtIfAuthKey_Type.__name__=_K
_SwL3ospfVirtIfAuthKey_Object=MibTableColumn
swL3ospfVirtIfAuthKey=_SwL3ospfVirtIfAuthKey_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,10),_SwL3ospfVirtIfAuthKey_Type())
swL3ospfVirtIfAuthKey.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfAuthKey.setStatus(_A)
class _SwL3ospfVirtIfAuthKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3ospfVirtIfAuthKeyID_Type.__name__=_B
_SwL3ospfVirtIfAuthKeyID_Object=MibTableColumn
swL3ospfVirtIfAuthKeyID=_SwL3ospfVirtIfAuthKeyID_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,11),_SwL3ospfVirtIfAuthKeyID_Type())
swL3ospfVirtIfAuthKeyID.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfAuthKeyID.setStatus(_A)
_SwL3ospfVirtIfStatus_Type=RowStatus
_SwL3ospfVirtIfStatus_Object=MibTableColumn
swL3ospfVirtIfStatus=_SwL3ospfVirtIfStatus_Object((1,3,6,1,4,1,171,11,118,5,3,7,1,12),_SwL3ospfVirtIfStatus_Type())
swL3ospfVirtIfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfStatus.setStatus(_A)
_SwL3ospfIfTable_Object=MibTable
swL3ospfIfTable=_SwL3ospfIfTable_Object((1,3,6,1,4,1,171,11,118,5,3,8))
if mibBuilder.loadTexts:swL3ospfIfTable.setStatus(_A)
_SwL3ospfIfEntry_Object=MibTableRow
swL3ospfIfEntry=_SwL3ospfIfEntry_Object((1,3,6,1,4,1,171,11,118,5,3,8,1))
swL3ospfIfEntry.setIndexNames((0,_F,_A5),(0,_F,_A6))
if mibBuilder.loadTexts:swL3ospfIfEntry.setStatus(_A)
_SwL3ospfIfIpAddress_Type=IpAddress
_SwL3ospfIfIpAddress_Object=MibTableColumn
swL3ospfIfIpAddress=_SwL3ospfIfIpAddress_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,1),_SwL3ospfIfIpAddress_Type())
swL3ospfIfIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfIpAddress.setStatus(_A)
_SwL3ospfAddressLessIf_Type=Integer32
_SwL3ospfAddressLessIf_Object=MibTableColumn
swL3ospfAddressLessIf=_SwL3ospfAddressLessIf_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,2),_SwL3ospfAddressLessIf_Type())
swL3ospfAddressLessIf.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfAddressLessIf.setStatus(_A)
class _SwL3ospfIfAreaId_Type(AreaID):defaultHexValue=_R
_SwL3ospfIfAreaId_Type.__name__=_b
_SwL3ospfIfAreaId_Object=MibTableColumn
swL3ospfIfAreaId=_SwL3ospfIfAreaId_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,3),_SwL3ospfIfAreaId_Type())
swL3ospfIfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfAreaId.setStatus(_A)
class _SwL3ospfIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_a,3),('pointToMultipoint',5)))
_SwL3ospfIfType_Type.__name__=_B
_SwL3ospfIfType_Object=MibTableColumn
swL3ospfIfType=_SwL3ospfIfType_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,4),_SwL3ospfIfType_Type())
swL3ospfIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfType.setStatus(_A)
class _SwL3ospfIfAdminStat_Type(Status):defaultValue=1
_SwL3ospfIfAdminStat_Type.__name__=_d
_SwL3ospfIfAdminStat_Object=MibTableColumn
swL3ospfIfAdminStat=_SwL3ospfIfAdminStat_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,5),_SwL3ospfIfAdminStat_Type())
swL3ospfIfAdminStat.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfAdminStat.setStatus(_A)
class _SwL3ospfIfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_SwL3ospfIfRtrPriority_Type.__name__=_c
_SwL3ospfIfRtrPriority_Object=MibTableColumn
swL3ospfIfRtrPriority=_SwL3ospfIfRtrPriority_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,6),_SwL3ospfIfRtrPriority_Type())
swL3ospfIfRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfRtrPriority.setStatus(_A)
class _SwL3ospfIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_SwL3ospfIfTransitDelay_Type.__name__=_M
_SwL3ospfIfTransitDelay_Object=MibTableColumn
swL3ospfIfTransitDelay=_SwL3ospfIfTransitDelay_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,7),_SwL3ospfIfTransitDelay_Type())
swL3ospfIfTransitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfTransitDelay.setStatus(_A)
class _SwL3ospfIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_SwL3ospfIfRetransInterval_Type.__name__=_M
_SwL3ospfIfRetransInterval_Object=MibTableColumn
swL3ospfIfRetransInterval=_SwL3ospfIfRetransInterval_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,8),_SwL3ospfIfRetransInterval_Type())
swL3ospfIfRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfRetransInterval.setStatus(_A)
class _SwL3ospfIfHelloInterval_Type(HelloRange):defaultValue=10
_SwL3ospfIfHelloInterval_Type.__name__=_S
_SwL3ospfIfHelloInterval_Object=MibTableColumn
swL3ospfIfHelloInterval=_SwL3ospfIfHelloInterval_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,9),_SwL3ospfIfHelloInterval_Type())
swL3ospfIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfHelloInterval.setStatus(_A)
class _SwL3ospfIfRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_SwL3ospfIfRtrDeadInterval_Type.__name__=_T
_SwL3ospfIfRtrDeadInterval_Object=MibTableColumn
swL3ospfIfRtrDeadInterval=_SwL3ospfIfRtrDeadInterval_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,10),_SwL3ospfIfRtrDeadInterval_Type())
swL3ospfIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfRtrDeadInterval.setStatus(_A)
class _SwL3ospfIfPollInterval_Type(PositiveInteger):defaultValue=120
_SwL3ospfIfPollInterval_Type.__name__=_T
_SwL3ospfIfPollInterval_Object=MibTableColumn
swL3ospfIfPollInterval=_SwL3ospfIfPollInterval_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,11),_SwL3ospfIfPollInterval_Type())
swL3ospfIfPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfPollInterval.setStatus(_A)
class _SwL3ospfIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Z,1),('loopback',2),('waiting',3),(_a,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7)))
_SwL3ospfIfState_Type.__name__=_B
_SwL3ospfIfState_Object=MibTableColumn
swL3ospfIfState=_SwL3ospfIfState_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,12),_SwL3ospfIfState_Type())
swL3ospfIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfState.setStatus(_A)
class _SwL3ospfIfDesignatedRouter_Type(IpAddress):defaultHexValue=_R
_SwL3ospfIfDesignatedRouter_Type.__name__=_O
_SwL3ospfIfDesignatedRouter_Object=MibTableColumn
swL3ospfIfDesignatedRouter=_SwL3ospfIfDesignatedRouter_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,13),_SwL3ospfIfDesignatedRouter_Type())
swL3ospfIfDesignatedRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfDesignatedRouter.setStatus(_A)
class _SwL3ospfIfBackupDesignatedRouter_Type(IpAddress):defaultHexValue=_R
_SwL3ospfIfBackupDesignatedRouter_Type.__name__=_O
_SwL3ospfIfBackupDesignatedRouter_Object=MibTableColumn
swL3ospfIfBackupDesignatedRouter=_SwL3ospfIfBackupDesignatedRouter_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,14),_SwL3ospfIfBackupDesignatedRouter_Type())
swL3ospfIfBackupDesignatedRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfBackupDesignatedRouter.setStatus(_A)
_SwL3ospfIfEvents_Type=Counter32
_SwL3ospfIfEvents_Object=MibTableColumn
swL3ospfIfEvents=_SwL3ospfIfEvents_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,15),_SwL3ospfIfEvents_Type())
swL3ospfIfEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfEvents.setStatus(_A)
class _SwL3ospfIfMulticastForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blocked',1),('multicast',2),('unicast',3)))
_SwL3ospfIfMulticastForwarding_Type.__name__=_B
_SwL3ospfIfMulticastForwarding_Object=MibTableColumn
swL3ospfIfMulticastForwarding=_SwL3ospfIfMulticastForwarding_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,16),_SwL3ospfIfMulticastForwarding_Type())
swL3ospfIfMulticastForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfMulticastForwarding.setStatus(_A)
class _SwL3ospfIfDemand_Type(TruthValue):defaultValue=2
_SwL3ospfIfDemand_Type.__name__=_U
_SwL3ospfIfDemand_Object=MibTableColumn
swL3ospfIfDemand=_SwL3ospfIfDemand_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,17),_SwL3ospfIfDemand_Type())
swL3ospfIfDemand.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfDemand.setStatus(_A)
class _SwL3ospfIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3ospfIfAuthType_Type.__name__=_B
_SwL3ospfIfAuthType_Object=MibTableColumn
swL3ospfIfAuthType=_SwL3ospfIfAuthType_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,18),_SwL3ospfIfAuthType_Type())
swL3ospfIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfAuthType.setStatus(_A)
class _SwL3ospfIfAuthKey_Type(OctetString):defaultHexValue=_A4;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SwL3ospfIfAuthKey_Type.__name__=_K
_SwL3ospfIfAuthKey_Object=MibTableColumn
swL3ospfIfAuthKey=_SwL3ospfIfAuthKey_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,19),_SwL3ospfIfAuthKey_Type())
swL3ospfIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfAuthKey.setStatus(_A)
class _SwL3ospfIfAuthKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3ospfIfAuthKeyID_Type.__name__=_B
_SwL3ospfIfAuthKeyID_Object=MibTableColumn
swL3ospfIfAuthKeyID=_SwL3ospfIfAuthKeyID_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,20),_SwL3ospfIfAuthKeyID_Type())
swL3ospfIfAuthKeyID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfAuthKeyID.setStatus(_A)
class _SwL3ospfIfPassiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_SwL3ospfIfPassiveMode_Type.__name__=_B
_SwL3ospfIfPassiveMode_Object=MibTableColumn
swL3ospfIfPassiveMode=_SwL3ospfIfPassiveMode_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,21),_SwL3ospfIfPassiveMode_Type())
swL3ospfIfPassiveMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfPassiveMode.setStatus(_A)
_SwL3ospfIfMetric_Type=Metric
_SwL3ospfIfMetric_Object=MibTableColumn
swL3ospfIfMetric=_SwL3ospfIfMetric_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,23),_SwL3ospfIfMetric_Type())
swL3ospfIfMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfMetric.setStatus(_A)
class _SwL3ospfIfDistributeListInType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_A7,2)))
_SwL3ospfIfDistributeListInType_Type.__name__=_B
_SwL3ospfIfDistributeListInType_Object=MibTableColumn
swL3ospfIfDistributeListInType=_SwL3ospfIfDistributeListInType_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,24),_SwL3ospfIfDistributeListInType_Type())
swL3ospfIfDistributeListInType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfDistributeListInType.setStatus(_A)
class _SwL3ospfIfDistributeListInName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SwL3ospfIfDistributeListInName_Type.__name__=_J
_SwL3ospfIfDistributeListInName_Object=MibTableColumn
swL3ospfIfDistributeListInName=_SwL3ospfIfDistributeListInName_Object((1,3,6,1,4,1,171,11,118,5,3,8,1,25),_SwL3ospfIfDistributeListInName_Type())
swL3ospfIfDistributeListInName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfIfDistributeListInName.setStatus(_A)
_SwL3RoutePreference_ObjectIdentity=ObjectIdentity
swL3RoutePreference=_SwL3RoutePreference_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,9))
class _SwL3RoutePreferenceRIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceRIP_Type.__name__=_B
_SwL3RoutePreferenceRIP_Object=MibScalar
swL3RoutePreferenceRIP=_SwL3RoutePreferenceRIP_Object((1,3,6,1,4,1,171,11,118,5,3,9,1),_SwL3RoutePreferenceRIP_Type())
swL3RoutePreferenceRIP.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceRIP.setStatus(_A)
class _SwL3RoutePreferenceOSPFIntra_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceOSPFIntra_Type.__name__=_B
_SwL3RoutePreferenceOSPFIntra_Object=MibScalar
swL3RoutePreferenceOSPFIntra=_SwL3RoutePreferenceOSPFIntra_Object((1,3,6,1,4,1,171,11,118,5,3,9,2),_SwL3RoutePreferenceOSPFIntra_Type())
swL3RoutePreferenceOSPFIntra.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceOSPFIntra.setStatus(_A)
class _SwL3RoutePreferenceStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceStatic_Type.__name__=_B
_SwL3RoutePreferenceStatic_Object=MibScalar
swL3RoutePreferenceStatic=_SwL3RoutePreferenceStatic_Object((1,3,6,1,4,1,171,11,118,5,3,9,3),_SwL3RoutePreferenceStatic_Type())
swL3RoutePreferenceStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceStatic.setStatus(_A)
class _SwL3RoutePreferenceLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_SwL3RoutePreferenceLocal_Type.__name__=_B
_SwL3RoutePreferenceLocal_Object=MibScalar
swL3RoutePreferenceLocal=_SwL3RoutePreferenceLocal_Object((1,3,6,1,4,1,171,11,118,5,3,9,4),_SwL3RoutePreferenceLocal_Type())
swL3RoutePreferenceLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RoutePreferenceLocal.setStatus(_A)
class _SwL3RoutePreferenceOSPFInter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceOSPFInter_Type.__name__=_B
_SwL3RoutePreferenceOSPFInter_Object=MibScalar
swL3RoutePreferenceOSPFInter=_SwL3RoutePreferenceOSPFInter_Object((1,3,6,1,4,1,171,11,118,5,3,9,5),_SwL3RoutePreferenceOSPFInter_Type())
swL3RoutePreferenceOSPFInter.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceOSPFInter.setStatus(_A)
class _SwL3RoutePreferenceOSPFExtT1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceOSPFExtT1_Type.__name__=_B
_SwL3RoutePreferenceOSPFExtT1_Object=MibScalar
swL3RoutePreferenceOSPFExtT1=_SwL3RoutePreferenceOSPFExtT1_Object((1,3,6,1,4,1,171,11,118,5,3,9,6),_SwL3RoutePreferenceOSPFExtT1_Type())
swL3RoutePreferenceOSPFExtT1.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceOSPFExtT1.setStatus(_A)
class _SwL3RoutePreferenceOSPFExtT2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceOSPFExtT2_Type.__name__=_B
_SwL3RoutePreferenceOSPFExtT2_Object=MibScalar
swL3RoutePreferenceOSPFExtT2=_SwL3RoutePreferenceOSPFExtT2_Object((1,3,6,1,4,1,171,11,118,5,3,9,7),_SwL3RoutePreferenceOSPFExtT2_Type())
swL3RoutePreferenceOSPFExtT2.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceOSPFExtT2.setStatus(_A)
class _SwL3RoutePreferenceDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceDefault_Type.__name__=_B
_SwL3RoutePreferenceDefault_Object=MibScalar
swL3RoutePreferenceDefault=_SwL3RoutePreferenceDefault_Object((1,3,6,1,4,1,171,11,118,5,3,9,8),_SwL3RoutePreferenceDefault_Type())
swL3RoutePreferenceDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceDefault.setStatus(_A)
class _SwL3RoutePreferenceEBGP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceEBGP_Type.__name__=_B
_SwL3RoutePreferenceEBGP_Object=MibScalar
swL3RoutePreferenceEBGP=_SwL3RoutePreferenceEBGP_Object((1,3,6,1,4,1,171,11,118,5,3,9,9),_SwL3RoutePreferenceEBGP_Type())
swL3RoutePreferenceEBGP.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceEBGP.setStatus(_A)
class _SwL3RoutePreferenceIBGP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceIBGP_Type.__name__=_B
_SwL3RoutePreferenceIBGP_Object=MibScalar
swL3RoutePreferenceIBGP=_SwL3RoutePreferenceIBGP_Object((1,3,6,1,4,1,171,11,118,5,3,9,10),_SwL3RoutePreferenceIBGP_Type())
swL3RoutePreferenceIBGP.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceIBGP.setStatus(_A)
_SwL3ospfAreaTable_Object=MibTable
swL3ospfAreaTable=_SwL3ospfAreaTable_Object((1,3,6,1,4,1,171,11,118,5,3,10))
if mibBuilder.loadTexts:swL3ospfAreaTable.setStatus(_A)
_SwL3ospfAreaEntry_Object=MibTableRow
swL3ospfAreaEntry=_SwL3ospfAreaEntry_Object((1,3,6,1,4,1,171,11,118,5,3,10,1))
swL3ospfAreaEntry.setIndexNames((0,_F,_A8))
if mibBuilder.loadTexts:swL3ospfAreaEntry.setStatus(_A)
_SwL3ospfAreaId_Type=AreaID
_SwL3ospfAreaId_Object=MibTableColumn
swL3ospfAreaId=_SwL3ospfAreaId_Object((1,3,6,1,4,1,171,11,118,5,3,10,1,1),_SwL3ospfAreaId_Type())
swL3ospfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfAreaId.setStatus(_A)
class _SwL3ospfAreaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('stub',2),('nssa',3)))
_SwL3ospfAreaType_Type.__name__=_B
_SwL3ospfAreaType_Object=MibTableColumn
swL3ospfAreaType=_SwL3ospfAreaType_Object((1,3,6,1,4,1,171,11,118,5,3,10,1,2),_SwL3ospfAreaType_Type())
swL3ospfAreaType.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfAreaType.setStatus('obsolete')
class _SwL3ospfAreaSummaryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_G,2),(_H,3)))
_SwL3ospfAreaSummaryState_Type.__name__=_B
_SwL3ospfAreaSummaryState_Object=MibTableColumn
swL3ospfAreaSummaryState=_SwL3ospfAreaSummaryState_Object((1,3,6,1,4,1,171,11,118,5,3,10,1,3),_SwL3ospfAreaSummaryState_Type())
swL3ospfAreaSummaryState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfAreaSummaryState.setStatus(_A)
class _SwL3ospfAreaMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3ospfAreaMetric_Type.__name__=_B
_SwL3ospfAreaMetric_Object=MibTableColumn
swL3ospfAreaMetric=_SwL3ospfAreaMetric_Object((1,3,6,1,4,1,171,11,118,5,3,10,1,4),_SwL3ospfAreaMetric_Type())
swL3ospfAreaMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3ospfAreaMetric.setStatus(_A)
class _SwL3ospfAreaTranslateState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_G,2),(_H,3)))
_SwL3ospfAreaTranslateState_Type.__name__=_B
_SwL3ospfAreaTranslateState_Object=MibTableColumn
swL3ospfAreaTranslateState=_SwL3ospfAreaTranslateState_Object((1,3,6,1,4,1,171,11,118,5,3,10,1,5),_SwL3ospfAreaTranslateState_Type())
swL3ospfAreaTranslateState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfAreaTranslateState.setStatus(_A)
_SwL3ospfAreaStatus_Type=RowStatus
_SwL3ospfAreaStatus_Object=MibTableColumn
swL3ospfAreaStatus=_SwL3ospfAreaStatus_Object((1,3,6,1,4,1,171,11,118,5,3,10,1,6),_SwL3ospfAreaStatus_Type())
swL3ospfAreaStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfAreaStatus.setStatus(_A)
_SwL3dvmrpInterfaceTable_Object=MibTable
swL3dvmrpInterfaceTable=_SwL3dvmrpInterfaceTable_Object((1,3,6,1,4,1,171,11,118,5,3,12))
if mibBuilder.loadTexts:swL3dvmrpInterfaceTable.setStatus(_A)
_SwL3dvmrpInterfaceEntry_Object=MibTableRow
swL3dvmrpInterfaceEntry=_SwL3dvmrpInterfaceEntry_Object((1,3,6,1,4,1,171,11,118,5,3,12,1))
swL3dvmrpInterfaceEntry.setIndexNames((0,_F,_A9))
if mibBuilder.loadTexts:swL3dvmrpInterfaceEntry.setStatus(_A)
_SwL3dvmrpInterfaceIfIndex_Type=Integer32
_SwL3dvmrpInterfaceIfIndex_Object=MibTableColumn
swL3dvmrpInterfaceIfIndex=_SwL3dvmrpInterfaceIfIndex_Object((1,3,6,1,4,1,171,11,118,5,3,12,1,1),_SwL3dvmrpInterfaceIfIndex_Type())
swL3dvmrpInterfaceIfIndex.setMaxAccess(_Y)
if mibBuilder.loadTexts:swL3dvmrpInterfaceIfIndex.setStatus(_A)
_SwL3dvmrpInterfaceLocalAddress_Type=IpAddress
_SwL3dvmrpInterfaceLocalAddress_Object=MibTableColumn
swL3dvmrpInterfaceLocalAddress=_SwL3dvmrpInterfaceLocalAddress_Object((1,3,6,1,4,1,171,11,118,5,3,12,1,2),_SwL3dvmrpInterfaceLocalAddress_Type())
swL3dvmrpInterfaceLocalAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3dvmrpInterfaceLocalAddress.setStatus(_A)
class _SwL3dvmrpInterfaceMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_SwL3dvmrpInterfaceMetric_Type.__name__=_B
_SwL3dvmrpInterfaceMetric_Object=MibTableColumn
swL3dvmrpInterfaceMetric=_SwL3dvmrpInterfaceMetric_Object((1,3,6,1,4,1,171,11,118,5,3,12,1,3),_SwL3dvmrpInterfaceMetric_Type())
swL3dvmrpInterfaceMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3dvmrpInterfaceMetric.setStatus(_A)
class _SwL3dvmrpInterfaceProbe_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3dvmrpInterfaceProbe_Type.__name__=_B
_SwL3dvmrpInterfaceProbe_Object=MibTableColumn
swL3dvmrpInterfaceProbe=_SwL3dvmrpInterfaceProbe_Object((1,3,6,1,4,1,171,11,118,5,3,12,1,4),_SwL3dvmrpInterfaceProbe_Type())
swL3dvmrpInterfaceProbe.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3dvmrpInterfaceProbe.setStatus(_A)
class _SwL3dvmrpInterfaceNbrTimeout_Type(Integer32):defaultValue=35;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3dvmrpInterfaceNbrTimeout_Type.__name__=_B
_SwL3dvmrpInterfaceNbrTimeout_Object=MibTableColumn
swL3dvmrpInterfaceNbrTimeout=_SwL3dvmrpInterfaceNbrTimeout_Object((1,3,6,1,4,1,171,11,118,5,3,12,1,5),_SwL3dvmrpInterfaceNbrTimeout_Type())
swL3dvmrpInterfaceNbrTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3dvmrpInterfaceNbrTimeout.setStatus(_A)
_SwL3dvmrpInterfaceStatus_Type=RowStatus
_SwL3dvmrpInterfaceStatus_Object=MibTableColumn
swL3dvmrpInterfaceStatus=_SwL3dvmrpInterfaceStatus_Object((1,3,6,1,4,1,171,11,118,5,3,12,1,6),_SwL3dvmrpInterfaceStatus_Type())
swL3dvmrpInterfaceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3dvmrpInterfaceStatus.setStatus(_A)
_SwL3dvmrpInterfaceRcvBadPkts_Type=Counter32
_SwL3dvmrpInterfaceRcvBadPkts_Object=MibTableColumn
swL3dvmrpInterfaceRcvBadPkts=_SwL3dvmrpInterfaceRcvBadPkts_Object((1,3,6,1,4,1,171,11,118,5,3,12,1,7),_SwL3dvmrpInterfaceRcvBadPkts_Type())
swL3dvmrpInterfaceRcvBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3dvmrpInterfaceRcvBadPkts.setStatus(_A)
_SwL3dvmrpInterfaceRcvBadRoutes_Type=Counter32
_SwL3dvmrpInterfaceRcvBadRoutes_Object=MibTableColumn
swL3dvmrpInterfaceRcvBadRoutes=_SwL3dvmrpInterfaceRcvBadRoutes_Object((1,3,6,1,4,1,171,11,118,5,3,12,1,8),_SwL3dvmrpInterfaceRcvBadRoutes_Type())
swL3dvmrpInterfaceRcvBadRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3dvmrpInterfaceRcvBadRoutes.setStatus(_A)
_SwL3OspfLsdbMgmt_ObjectIdentity=ObjectIdentity
swL3OspfLsdbMgmt=_SwL3OspfLsdbMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,13))
_SwL3OspfInternalLsdbTable_Object=MibTable
swL3OspfInternalLsdbTable=_SwL3OspfInternalLsdbTable_Object((1,3,6,1,4,1,171,11,118,5,3,13,1))
if mibBuilder.loadTexts:swL3OspfInternalLsdbTable.setStatus(_A)
_SwL3OspfInternalLsdbEntry_Object=MibTableRow
swL3OspfInternalLsdbEntry=_SwL3OspfInternalLsdbEntry_Object((1,3,6,1,4,1,171,11,118,5,3,13,1,1))
swL3OspfInternalLsdbEntry.setIndexNames((0,_F,_AA),(0,_F,_AB),(0,_F,_AC),(0,_F,_AD))
if mibBuilder.loadTexts:swL3OspfInternalLsdbEntry.setStatus(_A)
_SwL3OspfInternalLsdbAreaId_Type=AreaID
_SwL3OspfInternalLsdbAreaId_Object=MibTableColumn
swL3OspfInternalLsdbAreaId=_SwL3OspfInternalLsdbAreaId_Object((1,3,6,1,4,1,171,11,118,5,3,13,1,1,1),_SwL3OspfInternalLsdbAreaId_Type())
swL3OspfInternalLsdbAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfInternalLsdbAreaId.setStatus(_A)
class _SwL3OspfInternalLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('routerLink',1),('networkLink',2),('summaryLink',3),('asSummaryLink',4),(_AE,5),('multicastLink',6),(_AF,7)))
_SwL3OspfInternalLsdbType_Type.__name__=_B
_SwL3OspfInternalLsdbType_Object=MibTableColumn
swL3OspfInternalLsdbType=_SwL3OspfInternalLsdbType_Object((1,3,6,1,4,1,171,11,118,5,3,13,1,1,2),_SwL3OspfInternalLsdbType_Type())
swL3OspfInternalLsdbType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfInternalLsdbType.setStatus(_A)
_SwL3OspfInternalLsdbLsid_Type=IpAddress
_SwL3OspfInternalLsdbLsid_Object=MibTableColumn
swL3OspfInternalLsdbLsid=_SwL3OspfInternalLsdbLsid_Object((1,3,6,1,4,1,171,11,118,5,3,13,1,1,3),_SwL3OspfInternalLsdbLsid_Type())
swL3OspfInternalLsdbLsid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfInternalLsdbLsid.setStatus(_A)
_SwL3OspfInternalLsdbRouterId_Type=RouterID
_SwL3OspfInternalLsdbRouterId_Object=MibTableColumn
swL3OspfInternalLsdbRouterId=_SwL3OspfInternalLsdbRouterId_Object((1,3,6,1,4,1,171,11,118,5,3,13,1,1,4),_SwL3OspfInternalLsdbRouterId_Type())
swL3OspfInternalLsdbRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfInternalLsdbRouterId.setStatus(_A)
class _SwL3OspfInternalLsdbMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3OspfInternalLsdbMetric_Type.__name__=_B
_SwL3OspfInternalLsdbMetric_Object=MibTableColumn
swL3OspfInternalLsdbMetric=_SwL3OspfInternalLsdbMetric_Object((1,3,6,1,4,1,171,11,118,5,3,13,1,1,5),_SwL3OspfInternalLsdbMetric_Type())
swL3OspfInternalLsdbMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfInternalLsdbMetric.setStatus(_A)
class _SwL3OspfInternalLsdbSequenceNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwL3OspfInternalLsdbSequenceNo_Type.__name__=_K
_SwL3OspfInternalLsdbSequenceNo_Object=MibTableColumn
swL3OspfInternalLsdbSequenceNo=_SwL3OspfInternalLsdbSequenceNo_Object((1,3,6,1,4,1,171,11,118,5,3,13,1,1,6),_SwL3OspfInternalLsdbSequenceNo_Type())
swL3OspfInternalLsdbSequenceNo.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfInternalLsdbSequenceNo.setStatus(_A)
_SwL3OspfInternalLsdbAge_Type=Unsigned32
_SwL3OspfInternalLsdbAge_Object=MibTableColumn
swL3OspfInternalLsdbAge=_SwL3OspfInternalLsdbAge_Object((1,3,6,1,4,1,171,11,118,5,3,13,1,1,7),_SwL3OspfInternalLsdbAge_Type())
swL3OspfInternalLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfInternalLsdbAge.setStatus(_A)
_SwL3OspfInternalLsdbChecksum_Type=Integer32
_SwL3OspfInternalLsdbChecksum_Object=MibTableColumn
swL3OspfInternalLsdbChecksum=_SwL3OspfInternalLsdbChecksum_Object((1,3,6,1,4,1,171,11,118,5,3,13,1,1,8),_SwL3OspfInternalLsdbChecksum_Type())
swL3OspfInternalLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfInternalLsdbChecksum.setStatus(_A)
_SwL3OspfExternalLsdbTable_Object=MibTable
swL3OspfExternalLsdbTable=_SwL3OspfExternalLsdbTable_Object((1,3,6,1,4,1,171,11,118,5,3,13,2))
if mibBuilder.loadTexts:swL3OspfExternalLsdbTable.setStatus(_A)
_SwL3OspfExternalLsdbEntry_Object=MibTableRow
swL3OspfExternalLsdbEntry=_SwL3OspfExternalLsdbEntry_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1))
swL3OspfExternalLsdbEntry.setIndexNames((0,_F,_AG),(0,_F,_AH),(0,_F,_AI))
if mibBuilder.loadTexts:swL3OspfExternalLsdbEntry.setStatus(_A)
class _SwL3OspfExternalLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,7)));namedValues=NamedValues(*((_AE,5),(_AF,7)))
_SwL3OspfExternalLsdbType_Type.__name__=_B
_SwL3OspfExternalLsdbType_Object=MibTableColumn
swL3OspfExternalLsdbType=_SwL3OspfExternalLsdbType_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,1),_SwL3OspfExternalLsdbType_Type())
swL3OspfExternalLsdbType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbType.setStatus(_A)
_SwL3OspfExternalLsdbLsid_Type=IpAddress
_SwL3OspfExternalLsdbLsid_Object=MibTableColumn
swL3OspfExternalLsdbLsid=_SwL3OspfExternalLsdbLsid_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,2),_SwL3OspfExternalLsdbLsid_Type())
swL3OspfExternalLsdbLsid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbLsid.setStatus(_A)
_SwL3OspfExternalLsdbRouterId_Type=RouterID
_SwL3OspfExternalLsdbRouterId_Object=MibTableColumn
swL3OspfExternalLsdbRouterId=_SwL3OspfExternalLsdbRouterId_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,3),_SwL3OspfExternalLsdbRouterId_Type())
swL3OspfExternalLsdbRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbRouterId.setStatus(_A)
class _SwL3OspfExternalLsdbMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3OspfExternalLsdbMetric_Type.__name__=_B
_SwL3OspfExternalLsdbMetric_Object=MibTableColumn
swL3OspfExternalLsdbMetric=_SwL3OspfExternalLsdbMetric_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,4),_SwL3OspfExternalLsdbMetric_Type())
swL3OspfExternalLsdbMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbMetric.setStatus(_A)
class _SwL3OspfExternalLsdbMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unrecognized',0),(_P,1),(_Q,2)))
_SwL3OspfExternalLsdbMetricType_Type.__name__=_B
_SwL3OspfExternalLsdbMetricType_Object=MibTableColumn
swL3OspfExternalLsdbMetricType=_SwL3OspfExternalLsdbMetricType_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,5),_SwL3OspfExternalLsdbMetricType_Type())
swL3OspfExternalLsdbMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbMetricType.setStatus(_A)
class _SwL3OspfExternalLsdbSequenceNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwL3OspfExternalLsdbSequenceNo_Type.__name__=_K
_SwL3OspfExternalLsdbSequenceNo_Object=MibTableColumn
swL3OspfExternalLsdbSequenceNo=_SwL3OspfExternalLsdbSequenceNo_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,6),_SwL3OspfExternalLsdbSequenceNo_Type())
swL3OspfExternalLsdbSequenceNo.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbSequenceNo.setStatus(_A)
_SwL3OspfExternalLsdbAge_Type=Unsigned32
_SwL3OspfExternalLsdbAge_Object=MibTableColumn
swL3OspfExternalLsdbAge=_SwL3OspfExternalLsdbAge_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,7),_SwL3OspfExternalLsdbAge_Type())
swL3OspfExternalLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbAge.setStatus(_A)
_SwL3OspfExternalLsdbChecksum_Type=Integer32
_SwL3OspfExternalLsdbChecksum_Object=MibTableColumn
swL3OspfExternalLsdbChecksum=_SwL3OspfExternalLsdbChecksum_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,8),_SwL3OspfExternalLsdbChecksum_Type())
swL3OspfExternalLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbChecksum.setStatus(_A)
_SwL3OspfExternalLsdbForwardingAddress_Type=IpAddress
_SwL3OspfExternalLsdbForwardingAddress_Object=MibTableColumn
swL3OspfExternalLsdbForwardingAddress=_SwL3OspfExternalLsdbForwardingAddress_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,9),_SwL3OspfExternalLsdbForwardingAddress_Type())
swL3OspfExternalLsdbForwardingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbForwardingAddress.setStatus(_A)
_SwL3OspfExternalLsdbRouteTag_Type=OctetString
_SwL3OspfExternalLsdbRouteTag_Object=MibTableColumn
swL3OspfExternalLsdbRouteTag=_SwL3OspfExternalLsdbRouteTag_Object((1,3,6,1,4,1,171,11,118,5,3,13,2,1,10),_SwL3OspfExternalLsdbRouteTag_Type())
swL3OspfExternalLsdbRouteTag.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfExternalLsdbRouteTag.setStatus(_A)
_SwL3VrrpOperMgmt_ObjectIdentity=ObjectIdentity
swL3VrrpOperMgmt=_SwL3VrrpOperMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,14))
_SwL3VrrpOperTable_Object=MibTable
swL3VrrpOperTable=_SwL3VrrpOperTable_Object((1,3,6,1,4,1,171,11,118,5,3,14,1))
if mibBuilder.loadTexts:swL3VrrpOperTable.setStatus(_A)
_SwL3VrrpOperEntry_Object=MibTableRow
swL3VrrpOperEntry=_SwL3VrrpOperEntry_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1))
swL3VrrpOperEntry.setIndexNames((0,_F,_AJ),(0,_F,_AK))
if mibBuilder.loadTexts:swL3VrrpOperEntry.setStatus(_A)
_SwL3VrrpOperIfIndex_Type=Integer32
_SwL3VrrpOperIfIndex_Object=MibTableColumn
swL3VrrpOperIfIndex=_SwL3VrrpOperIfIndex_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,1),_SwL3VrrpOperIfIndex_Type())
swL3VrrpOperIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3VrrpOperIfIndex.setStatus(_A)
_SwL3VrrpOperVrId_Type=VrId
_SwL3VrrpOperVrId_Object=MibTableColumn
swL3VrrpOperVrId=_SwL3VrrpOperVrId_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,2),_SwL3VrrpOperVrId_Type())
swL3VrrpOperVrId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3VrrpOperVrId.setStatus(_A)
_SwL3VrrpOperVirtualMacAddr_Type=MacAddress
_SwL3VrrpOperVirtualMacAddr_Object=MibTableColumn
swL3VrrpOperVirtualMacAddr=_SwL3VrrpOperVirtualMacAddr_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,3),_SwL3VrrpOperVirtualMacAddr_Type())
swL3VrrpOperVirtualMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3VrrpOperVirtualMacAddr.setStatus(_A)
class _SwL3VrrpOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initialize',1),(_q,2),('master',3)))
_SwL3VrrpOperState_Type.__name__=_B
_SwL3VrrpOperState_Object=MibTableColumn
swL3VrrpOperState=_SwL3VrrpOperState_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,4),_SwL3VrrpOperState_Type())
swL3VrrpOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3VrrpOperState.setStatus(_A)
class _SwL3VrrpOperAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_Z,2)))
_SwL3VrrpOperAdminState_Type.__name__=_B
_SwL3VrrpOperAdminState_Object=MibTableColumn
swL3VrrpOperAdminState=_SwL3VrrpOperAdminState_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,5),_SwL3VrrpOperAdminState_Type())
swL3VrrpOperAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperAdminState.setStatus(_A)
class _SwL3VrrpOperPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3VrrpOperPriority_Type.__name__=_B
_SwL3VrrpOperPriority_Object=MibTableColumn
swL3VrrpOperPriority=_SwL3VrrpOperPriority_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,6),_SwL3VrrpOperPriority_Type())
swL3VrrpOperPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperPriority.setStatus(_A)
_SwL3VrrpOperMasterIpAddr_Type=IpAddress
_SwL3VrrpOperMasterIpAddr_Object=MibTableColumn
swL3VrrpOperMasterIpAddr=_SwL3VrrpOperMasterIpAddr_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,7),_SwL3VrrpOperMasterIpAddr_Type())
swL3VrrpOperMasterIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3VrrpOperMasterIpAddr.setStatus(_A)
class _SwL3VrrpOperCriticalIpAddr_Type(IpAddress):defaultHexValue=_R
_SwL3VrrpOperCriticalIpAddr_Type.__name__=_O
_SwL3VrrpOperCriticalIpAddr_Object=MibTableColumn
swL3VrrpOperCriticalIpAddr=_SwL3VrrpOperCriticalIpAddr_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,8),_SwL3VrrpOperCriticalIpAddr_Type())
swL3VrrpOperCriticalIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperCriticalIpAddr.setStatus(_A)
class _SwL3VrrpOperCheckCriticalIpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_G,1),(_H,2)))
_SwL3VrrpOperCheckCriticalIpState_Type.__name__=_B
_SwL3VrrpOperCheckCriticalIpState_Object=MibTableColumn
swL3VrrpOperCheckCriticalIpState=_SwL3VrrpOperCheckCriticalIpState_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,9),_SwL3VrrpOperCheckCriticalIpState_Type())
swL3VrrpOperCheckCriticalIpState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperCheckCriticalIpState.setStatus(_A)
class _SwL3VrrpOperAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthentication',1),('simpleTextPassword',2),('ipAuthenticationHeader',3)))
_SwL3VrrpOperAuthType_Type.__name__=_B
_SwL3VrrpOperAuthType_Object=MibTableColumn
swL3VrrpOperAuthType=_SwL3VrrpOperAuthType_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,10),_SwL3VrrpOperAuthType_Type())
swL3VrrpOperAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperAuthType.setStatus(_A)
class _SwL3VrrpOperAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SwL3VrrpOperAuthKey_Type.__name__=_K
_SwL3VrrpOperAuthKey_Object=MibTableColumn
swL3VrrpOperAuthKey=_SwL3VrrpOperAuthKey_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,11),_SwL3VrrpOperAuthKey_Type())
swL3VrrpOperAuthKey.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperAuthKey.setStatus(_A)
class _SwL3VrrpOperAdvertisementInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL3VrrpOperAdvertisementInterval_Type.__name__=_B
_SwL3VrrpOperAdvertisementInterval_Object=MibTableColumn
swL3VrrpOperAdvertisementInterval=_SwL3VrrpOperAdvertisementInterval_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,12),_SwL3VrrpOperAdvertisementInterval_Type())
swL3VrrpOperAdvertisementInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperAdvertisementInterval.setStatus(_A)
if mibBuilder.loadTexts:swL3VrrpOperAdvertisementInterval.setUnits('seconds')
class _SwL3VrrpOperPreemptMode_Type(TruthValue):defaultValue=1
_SwL3VrrpOperPreemptMode_Type.__name__=_U
_SwL3VrrpOperPreemptMode_Object=MibTableColumn
swL3VrrpOperPreemptMode=_SwL3VrrpOperPreemptMode_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,13),_SwL3VrrpOperPreemptMode_Type())
swL3VrrpOperPreemptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperPreemptMode.setStatus(_A)
_SwL3VrrpOperVirtualRouterUpTime_Type=TimeStamp
_SwL3VrrpOperVirtualRouterUpTime_Object=MibTableColumn
swL3VrrpOperVirtualRouterUpTime=_SwL3VrrpOperVirtualRouterUpTime_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,14),_SwL3VrrpOperVirtualRouterUpTime_Type())
swL3VrrpOperVirtualRouterUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3VrrpOperVirtualRouterUpTime.setStatus(_A)
_SwL3VrrpOperVirtualIpAddr_Type=IpAddress
_SwL3VrrpOperVirtualIpAddr_Object=MibTableColumn
swL3VrrpOperVirtualIpAddr=_SwL3VrrpOperVirtualIpAddr_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,15),_SwL3VrrpOperVirtualIpAddr_Type())
swL3VrrpOperVirtualIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperVirtualIpAddr.setStatus(_A)
_SwL3VrrpOperRowStatus_Type=RowStatus
_SwL3VrrpOperRowStatus_Object=MibTableColumn
swL3VrrpOperRowStatus=_SwL3VrrpOperRowStatus_Object((1,3,6,1,4,1,171,11,118,5,3,14,1,1,16),_SwL3VrrpOperRowStatus_Type())
swL3VrrpOperRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VrrpOperRowStatus.setStatus(_A)
_SwL3OspfECMPMgmt_ObjectIdentity=ObjectIdentity
swL3OspfECMPMgmt=_SwL3OspfECMPMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,15))
class _SwL3OspfECMPIpDestination_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3OspfECMPIpDestination_Type.__name__=_B
_SwL3OspfECMPIpDestination_Object=MibScalar
swL3OspfECMPIpDestination=_SwL3OspfECMPIpDestination_Object((1,3,6,1,4,1,171,11,118,5,3,15,1),_SwL3OspfECMPIpDestination_Type())
swL3OspfECMPIpDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfECMPIpDestination.setStatus(_A)
class _SwL3OspfECMPIpSource_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3OspfECMPIpSource_Type.__name__=_B
_SwL3OspfECMPIpSource_Object=MibScalar
swL3OspfECMPIpSource=_SwL3OspfECMPIpSource_Object((1,3,6,1,4,1,171,11,118,5,3,15,2),_SwL3OspfECMPIpSource_Type())
swL3OspfECMPIpSource.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfECMPIpSource.setStatus(_A)
class _SwL3OspfECMPCrcLow_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3OspfECMPCrcLow_Type.__name__=_B
_SwL3OspfECMPCrcLow_Object=MibScalar
swL3OspfECMPCrcLow=_SwL3OspfECMPCrcLow_Object((1,3,6,1,4,1,171,11,118,5,3,15,3),_SwL3OspfECMPCrcLow_Type())
swL3OspfECMPCrcLow.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfECMPCrcLow.setStatus(_A)
class _SwL3OspfECMPCrcHigh_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3OspfECMPCrcHigh_Type.__name__=_B
_SwL3OspfECMPCrcHigh_Object=MibScalar
swL3OspfECMPCrcHigh=_SwL3OspfECMPCrcHigh_Object((1,3,6,1,4,1,171,11,118,5,3,15,4),_SwL3OspfECMPCrcHigh_Type())
swL3OspfECMPCrcHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfECMPCrcHigh.setStatus(_A)
class _SwL3OspfECMPTCPorUDPport_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3OspfECMPTCPorUDPport_Type.__name__=_B
_SwL3OspfECMPTCPorUDPport_Object=MibScalar
swL3OspfECMPTCPorUDPport=_SwL3OspfECMPTCPorUDPport_Object((1,3,6,1,4,1,171,11,118,5,3,15,5),_SwL3OspfECMPTCPorUDPport_Type())
swL3OspfECMPTCPorUDPport.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfECMPTCPorUDPport.setStatus(_A)
class _SwL3OspfECMPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL3OspfECMPState_Type.__name__=_B
_SwL3OspfECMPState_Object=MibScalar
swL3OspfECMPState=_SwL3OspfECMPState_Object((1,3,6,1,4,1,171,11,118,5,3,15,6),_SwL3OspfECMPState_Type())
swL3OspfECMPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfECMPState.setStatus(_A)
_SwL3RIPTimerMgmt_ObjectIdentity=ObjectIdentity
swL3RIPTimerMgmt=_SwL3RIPTimerMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,17))
class _SwL3RIPUpdateTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3RIPUpdateTime_Type.__name__=_B
_SwL3RIPUpdateTime_Object=MibScalar
swL3RIPUpdateTime=_SwL3RIPUpdateTime_Object((1,3,6,1,4,1,171,11,118,5,3,17,1),_SwL3RIPUpdateTime_Type())
swL3RIPUpdateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RIPUpdateTime.setStatus(_A)
class _SwL3RIPTimeOutTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3RIPTimeOutTime_Type.__name__=_B
_SwL3RIPTimeOutTime_Object=MibScalar
swL3RIPTimeOutTime=_SwL3RIPTimeOutTime_Object((1,3,6,1,4,1,171,11,118,5,3,17,2),_SwL3RIPTimeOutTime_Type())
swL3RIPTimeOutTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RIPTimeOutTime.setStatus(_A)
class _SwL3RIPGarbageCollectionTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3RIPGarbageCollectionTime_Type.__name__=_B
_SwL3RIPGarbageCollectionTime_Object=MibScalar
swL3RIPGarbageCollectionTime=_SwL3RIPGarbageCollectionTime_Object((1,3,6,1,4,1,171,11,118,5,3,17,3),_SwL3RIPGarbageCollectionTime_Type())
swL3RIPGarbageCollectionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RIPGarbageCollectionTime.setStatus(_A)
_SwL3OspfDefInfoOrigMgmt_ObjectIdentity=ObjectIdentity
swL3OspfDefInfoOrigMgmt=_SwL3OspfDefInfoOrigMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,118,5,3,18))
class _SwL3OspfDefInfoOriginate_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('always',1),('default',2),(_L,3)))
_SwL3OspfDefInfoOriginate_Type.__name__=_B
_SwL3OspfDefInfoOriginate_Object=MibScalar
swL3OspfDefInfoOriginate=_SwL3OspfDefInfoOriginate_Object((1,3,6,1,4,1,171,11,118,5,3,18,1),_SwL3OspfDefInfoOriginate_Type())
swL3OspfDefInfoOriginate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfDefInfoOriginate.setStatus(_A)
class _SwL3OspfDefInfoOrigMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SwL3OspfDefInfoOrigMetricType_Type.__name__=_B
_SwL3OspfDefInfoOrigMetricType_Object=MibScalar
swL3OspfDefInfoOrigMetricType=_SwL3OspfDefInfoOrigMetricType_Object((1,3,6,1,4,1,171,11,118,5,3,18,2),_SwL3OspfDefInfoOrigMetricType_Type())
swL3OspfDefInfoOrigMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfDefInfoOrigMetricType.setStatus(_A)
class _SwL3OspfDefInfoOrigMetric_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3OspfDefInfoOrigMetric_Type.__name__=_B
_SwL3OspfDefInfoOrigMetric_Object=MibScalar
swL3OspfDefInfoOrigMetric=_SwL3OspfDefInfoOrigMetric_Object((1,3,6,1,4,1,171,11,118,5,3,18,3),_SwL3OspfDefInfoOrigMetric_Type())
swL3OspfDefInfoOrigMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfDefInfoOrigMetric.setStatus(_A)
_SwL3RIPInboundRouteFilterTable_Object=MibTable
swL3RIPInboundRouteFilterTable=_SwL3RIPInboundRouteFilterTable_Object((1,3,6,1,4,1,171,11,118,5,3,19))
if mibBuilder.loadTexts:swL3RIPInboundRouteFilterTable.setStatus(_A)
_SwL3RIPInboundRouteFilterEntry_Object=MibTableRow
swL3RIPInboundRouteFilterEntry=_SwL3RIPInboundRouteFilterEntry_Object((1,3,6,1,4,1,171,11,118,5,3,19,1))
swL3RIPInboundRouteFilterEntry.setIndexNames((0,_F,_AL))
if mibBuilder.loadTexts:swL3RIPInboundRouteFilterEntry.setStatus(_A)
_SwL3RIPInboundRouteFilterIfIpAddress_Type=IpAddress
_SwL3RIPInboundRouteFilterIfIpAddress_Object=MibTableColumn
swL3RIPInboundRouteFilterIfIpAddress=_SwL3RIPInboundRouteFilterIfIpAddress_Object((1,3,6,1,4,1,171,11,118,5,3,19,1,1),_SwL3RIPInboundRouteFilterIfIpAddress_Type())
swL3RIPInboundRouteFilterIfIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RIPInboundRouteFilterIfIpAddress.setStatus(_A)
class _SwL3RIPInboundRouteFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_A7,2)))
_SwL3RIPInboundRouteFilterType_Type.__name__=_B
_SwL3RIPInboundRouteFilterType_Object=MibTableColumn
swL3RIPInboundRouteFilterType=_SwL3RIPInboundRouteFilterType_Object((1,3,6,1,4,1,171,11,118,5,3,19,1,2),_SwL3RIPInboundRouteFilterType_Type())
swL3RIPInboundRouteFilterType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RIPInboundRouteFilterType.setStatus(_A)
class _SwL3RIPInboundRouteFilterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SwL3RIPInboundRouteFilterName_Type.__name__=_J
_SwL3RIPInboundRouteFilterName_Object=MibTableColumn
swL3RIPInboundRouteFilterName=_SwL3RIPInboundRouteFilterName_Object((1,3,6,1,4,1,171,11,118,5,3,19,1,3),_SwL3RIPInboundRouteFilterName_Type())
swL3RIPInboundRouteFilterName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RIPInboundRouteFilterName.setStatus(_A)
_SwL3Route6RedistriTable_Object=MibTable
swL3Route6RedistriTable=_SwL3Route6RedistriTable_Object((1,3,6,1,4,1,171,11,118,5,3,20))
if mibBuilder.loadTexts:swL3Route6RedistriTable.setStatus(_A)
_SwL3Route6RedistriEntry_Object=MibTableRow
swL3Route6RedistriEntry=_SwL3Route6RedistriEntry_Object((1,3,6,1,4,1,171,11,118,5,3,20,1))
swL3Route6RedistriEntry.setIndexNames((0,_F,_AM),(0,_F,_AN))
if mibBuilder.loadTexts:swL3Route6RedistriEntry.setStatus(_A)
class _SwL3Route6RedistriSrcProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_V,2),('ripng',3),('ospfv3',4)))
_SwL3Route6RedistriSrcProtocol_Type.__name__=_B
_SwL3Route6RedistriSrcProtocol_Object=MibTableColumn
swL3Route6RedistriSrcProtocol=_SwL3Route6RedistriSrcProtocol_Object((1,3,6,1,4,1,171,11,118,5,3,20,1,1),_SwL3Route6RedistriSrcProtocol_Type())
swL3Route6RedistriSrcProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Route6RedistriSrcProtocol.setStatus(_A)
class _SwL3Route6RedistriDstProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ripng',1),('ospfv3',2)))
_SwL3Route6RedistriDstProtocol_Type.__name__=_B
_SwL3Route6RedistriDstProtocol_Object=MibTableColumn
swL3Route6RedistriDstProtocol=_SwL3Route6RedistriDstProtocol_Object((1,3,6,1,4,1,171,11,118,5,3,20,1,2),_SwL3Route6RedistriDstProtocol_Type())
swL3Route6RedistriDstProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Route6RedistriDstProtocol.setStatus(_A)
class _SwL3Route6RedistriType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),('all',3)))
_SwL3Route6RedistriType_Type.__name__=_B
_SwL3Route6RedistriType_Object=MibTableColumn
swL3Route6RedistriType=_SwL3Route6RedistriType_Object((1,3,6,1,4,1,171,11,118,5,3,20,1,3),_SwL3Route6RedistriType_Type())
swL3Route6RedistriType.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3Route6RedistriType.setStatus(_A)
_SwL3Route6RedistriMetric_Type=Unsigned32
_SwL3Route6RedistriMetric_Object=MibTableColumn
swL3Route6RedistriMetric=_SwL3Route6RedistriMetric_Object((1,3,6,1,4,1,171,11,118,5,3,20,1,4),_SwL3Route6RedistriMetric_Type())
swL3Route6RedistriMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3Route6RedistriMetric.setStatus(_A)
_SwL3Route6RedistriRowStatus_Type=RowStatus
_SwL3Route6RedistriRowStatus_Object=MibTableColumn
swL3Route6RedistriRowStatus=_SwL3Route6RedistriRowStatus_Object((1,3,6,1,4,1,171,11,118,5,3,20,1,5),_SwL3Route6RedistriRowStatus_Type())
swL3Route6RedistriRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3Route6RedistriRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'NodeAddress':NodeAddress,'NetAddress':NetAddress,'VrId':VrId,'swL3MgmtMIB':swL3MgmtMIB,'swL3DevMgmt':swL3DevMgmt,'swL3DevCtrl':swL3DevCtrl,'swL3DevCtrlRIPState':swL3DevCtrlRIPState,'swL3DevCtrlOSPFState':swL3DevCtrlOSPFState,'swL3DevCtrlDVMRPState':swL3DevCtrlDVMRPState,'swL3DevCtrlVRRPState':swL3DevCtrlVRRPState,'swL3DevCtrlVrrpPingState':swL3DevCtrlVrrpPingState,'swL3IpMgmt':swL3IpMgmt,'swL3IpCtrlMgmt':swL3IpCtrlMgmt,'swL3IpCtrlTable':swL3IpCtrlTable,'swL3IpCtrlEntry':swL3IpCtrlEntry,_e:swL3IpCtrlInterfaceName,'swL3IpCtrlIfIndex':swL3IpCtrlIfIndex,'swL3IpCtrlIpAddr':swL3IpCtrlIpAddr,'swL3IpCtrlIpSubnetMask':swL3IpCtrlIpSubnetMask,'swL3IpCtrlVlanName':swL3IpCtrlVlanName,'swL3IpCtrlProxyArp':swL3IpCtrlProxyArp,'swL3IpCtrlSecondary':swL3IpCtrlSecondary,'swL3IpCtrlMode':swL3IpCtrlMode,'swL3IpCtrlAdminState':swL3IpCtrlAdminState,'swL3IpCtrlIpv4AdminState':swL3IpCtrlIpv4AdminState,'swL3IpCtrlIpv6AdminState':swL3IpCtrlIpv6AdminState,'swL3IpCtrlIpv6LinkLocalAddress':swL3IpCtrlIpv6LinkLocalAddress,'swL3IpCtrlIpv6LinkLocalPrefixLen':swL3IpCtrlIpv6LinkLocalPrefixLen,'swL3IpCtrlState':swL3IpCtrlState,'swL3IpCtrlIpv6LinkLocalAutoState':swL3IpCtrlIpv6LinkLocalAutoState,'swL3IpCtrlLocalProxyArp':swL3IpCtrlLocalProxyArp,'swL3IpCtrlIpMtu':swL3IpCtrlIpMtu,'swL3IpCtrlDhcpv6ClientState':swL3IpCtrlDhcpv6ClientState,'swL3IpCtrlIpDirectedBroadcastState':swL3IpCtrlIpDirectedBroadcastState,'swL3IpCtrlDhcpv6ClientPDState':swL3IpCtrlDhcpv6ClientPDState,'swL3IpCtrlDhcpv6ClientPDPrefixName':swL3IpCtrlDhcpv6ClientPDPrefixName,'swL3IpCtrlDhcpv6ClientPDPrefix':swL3IpCtrlDhcpv6ClientPDPrefix,'swL3IpCtrlDhcpv6ClientPDPrefixLen':swL3IpCtrlDhcpv6ClientPDPrefixLen,'swL3Ipv6CtrlTable':swL3Ipv6CtrlTable,'swL3Ipv6CtrlEntry':swL3Ipv6CtrlEntry,_f:swL3Ipv6CtrlInterfaceName,'swL3Ipv6CtrlMaxReassmblySize':swL3Ipv6CtrlMaxReassmblySize,'swL3Ipv6CtrlNsRetransTimer':swL3Ipv6CtrlNsRetransTimer,'swL3Ipv6CtrlRaState':swL3Ipv6CtrlRaState,'swL3Ipv6CtrlRaMinRtrAdvInterval':swL3Ipv6CtrlRaMinRtrAdvInterval,'swL3Ipv6CtrlRaMaxRtrAdvInterval':swL3Ipv6CtrlRaMaxRtrAdvInterval,'swL3Ipv6CtrlRaLifeTime':swL3Ipv6CtrlRaLifeTime,'swL3Ipv6CtrlRaReachableTime':swL3Ipv6CtrlRaReachableTime,'swL3Ipv6CtrlRaRetransTime':swL3Ipv6CtrlRaRetransTime,'swL3Ipv6CtrlRaHopLimit':swL3Ipv6CtrlRaHopLimit,'swL3Ipv6CtrlRaManagedFlag':swL3Ipv6CtrlRaManagedFlag,'swL3Ipv6CtrlRaOtherConfigFlag':swL3Ipv6CtrlRaOtherConfigFlag,'swL3Ipv6AddressCtrlTable':swL3Ipv6AddressCtrlTable,'swL3Ipv6AddressCtrlEntry':swL3Ipv6AddressCtrlEntry,_g:swL3Ipv6AddressCtrlInterfaceName,_h:swL3Ipv6Address,_i:swL3Ipv6AddressCtrlPrefixLen,'swL3Ipv6AddressCtrlPreferredLifeTime':swL3Ipv6AddressCtrlPreferredLifeTime,'swL3Ipv6AddressCtrlValidLifeTime':swL3Ipv6AddressCtrlValidLifeTime,'swL3Ipv6AddressCtrlOnLinkFlag':swL3Ipv6AddressCtrlOnLinkFlag,'swL3Ipv6AddressCtrlAutonomousFlag':swL3Ipv6AddressCtrlAutonomousFlag,'swL3Ipv6AddressCtrlState':swL3Ipv6AddressCtrlState,'swL3Ipv6DHCPv6CPDAddrCtrlTable':swL3Ipv6DHCPv6CPDAddrCtrlTable,'swL3Ipv6DHCPv6CPDAddrCtrlEntry':swL3Ipv6DHCPv6CPDAddrCtrlEntry,_j:swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName,_k:swL3Ipv6DHCPv6CPDAddrCtrlPrefixName,_l:swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr,_m:swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen,'swL3Ipv6DHCPv6CPDAddrCtrlState':swL3Ipv6DHCPv6CPDAddrCtrlState,'swL3IpCtrlAllIpIfState':swL3IpCtrlAllIpIfState,'swL3LoopBackIpCtrlTable':swL3LoopBackIpCtrlTable,'swL3LoopBackIpCtrlEntry':swL3LoopBackIpCtrlEntry,_n:swL3LoopBackIpCtrlInterfaceName,'swL3LoopBackIpCtrlIfIndex':swL3LoopBackIpCtrlIfIndex,'swL3LoopBackIpCtrlIpAddr':swL3LoopBackIpCtrlIpAddr,'swL3LoopBackIpCtrlIpSubnetMask':swL3LoopBackIpCtrlIpSubnetMask,'swL3LoopBackIpCtrlAdminState':swL3LoopBackIpCtrlAdminState,'swL3LoopBackIpCtrlRowStatus':swL3LoopBackIpCtrlRowStatus,'swL3IpFdbMgmt':swL3IpFdbMgmt,'swL3IpFdbInfoTable':swL3IpFdbInfoTable,'swL3IpFdbInfoEntry':swL3IpFdbInfoEntry,_o:swL3IpFdbInfoIpAddr,'swL3IpFdbInfoIpSubnetMask':swL3IpFdbInfoIpSubnetMask,'swL3IpFdbInfoPort':swL3IpFdbInfoPort,'swL3IpFdbInfoType':swL3IpFdbInfoType,'swL3IpArpAgingTime':swL3IpArpAgingTime,'swL3IpStaticRouteTable':swL3IpStaticRouteTable,'swL3IpStaticRouteEntry':swL3IpStaticRouteEntry,_W:swL3IpStaticRouteDest,_X:swL3IpStaticRouteMask,'swL3IpStaticRouteBkupState':swL3IpStaticRouteBkupState,_p:swL3IpStaticRouteNextHop,'swL3IpStaticRouteMetric':swL3IpStaticRouteMetric,'swL3IpStaticRouteStatus':swL3IpStaticRouteStatus,'swL3IpStaticRouteWeight':swL3IpStaticRouteWeight,'swL3IpStaticRouteInterfaceName':swL3IpStaticRouteInterfaceName,'swL3IpMcastMgmt':swL3IpMcastMgmt,'swL3IpMcastStaticRouteTable':swL3IpMcastStaticRouteTable,'swL3IpMcastStaticRouteEntry':swL3IpMcastStaticRouteEntry,_s:swL3IpMcastStaticRouteIpmrouteAddr,_t:swL3IpMcastStaticRouteIpmrouteMask,'swL3IpMcastStaticRouteRpfAddr':swL3IpMcastStaticRouteRpfAddr,'swL3IpMcastStaticRouteRowStatus':swL3IpMcastStaticRouteRowStatus,'swL3IpStaticRouteTunnelTable':swL3IpStaticRouteTunnelTable,'swL3IpStaticRouteTunnelEntry':swL3IpStaticRouteTunnelEntry,_u:swL3IpStaticRouteTunnelInterfaceName,'swL3IpStaticRouteTunnelRowStatus':swL3IpStaticRouteTunnelRowStatus,'swL3RelayMgmt':swL3RelayMgmt,'swL3RelayDnsMgmt':swL3RelayDnsMgmt,'swL3RelayDnsState':swL3RelayDnsState,'swL3RelayDnsPrimaryServer':swL3RelayDnsPrimaryServer,'swL3RelayDnsSecondaryServer':swL3RelayDnsSecondaryServer,'swL3RelayDnsCacheState':swL3RelayDnsCacheState,'swL3RelayDnsStaticTableState':swL3RelayDnsStaticTableState,'swL3RelayDnsCtrlTable':swL3RelayDnsCtrlTable,'swL3RelayDnsCtrlEntry':swL3RelayDnsCtrlEntry,_v:swL3RelayDnsCtrlDomainName,_w:swL3RelayDnsCtrlIpAddr,'swL3RelayDnsCtrlState':swL3RelayDnsCtrlState,'swL3Md5Table':swL3Md5Table,'swL3Md5Entry':swL3Md5Entry,_x:swL3Md5KeyId,'swL3Md5Key':swL3Md5Key,'swL3Md5RowStatus':swL3Md5RowStatus,'swL3RouteRedistriTable':swL3RouteRedistriTable,'swL3RouteRedistriEntry':swL3RouteRedistriEntry,_y:swL3RouteRedistriSrcProtocol,_z:swL3RouteRedistriDstProtocol,'swL3RouteRedistriType':swL3RouteRedistriType,'swL3RouteRedistriMetric':swL3RouteRedistriMetric,'swL3RouteRedistriRowStatus':swL3RouteRedistriRowStatus,'swL3RouteRedistriRouteMapName':swL3RouteRedistriRouteMapName,'swL3OspfHostTable':swL3OspfHostTable,'swL3OspfHostEntry':swL3OspfHostEntry,_A0:swL3OspfHostIpAddress,_A1:swL3OspfHostTOS,'swL3OspfHostMetric':swL3OspfHostMetric,'swL3OspfHostAreaID':swL3OspfHostAreaID,'swL3OspfHostStatus':swL3OspfHostStatus,'swL3ospfVirtIfTable':swL3ospfVirtIfTable,'swL3ospfVirtIfEntry':swL3ospfVirtIfEntry,_A2:swL3ospfVirtIfAreaId,_A3:swL3ospfVirtIfNeighbor,'swL3ospfVirtIfTransitDelay':swL3ospfVirtIfTransitDelay,'swL3ospfVirtIfRetransInterval':swL3ospfVirtIfRetransInterval,'swL3ospfVirtIfHelloInterval':swL3ospfVirtIfHelloInterval,'swL3ospfVirtIfRtrDeadInterval':swL3ospfVirtIfRtrDeadInterval,'swL3ospfVirtIfState':swL3ospfVirtIfState,'swL3ospfVirtIfEvents':swL3ospfVirtIfEvents,'swL3ospfVirtIfAuthType':swL3ospfVirtIfAuthType,'swL3ospfVirtIfAuthKey':swL3ospfVirtIfAuthKey,'swL3ospfVirtIfAuthKeyID':swL3ospfVirtIfAuthKeyID,'swL3ospfVirtIfStatus':swL3ospfVirtIfStatus,'swL3ospfIfTable':swL3ospfIfTable,'swL3ospfIfEntry':swL3ospfIfEntry,_A5:swL3ospfIfIpAddress,_A6:swL3ospfAddressLessIf,'swL3ospfIfAreaId':swL3ospfIfAreaId,'swL3ospfIfType':swL3ospfIfType,'swL3ospfIfAdminStat':swL3ospfIfAdminStat,'swL3ospfIfRtrPriority':swL3ospfIfRtrPriority,'swL3ospfIfTransitDelay':swL3ospfIfTransitDelay,'swL3ospfIfRetransInterval':swL3ospfIfRetransInterval,'swL3ospfIfHelloInterval':swL3ospfIfHelloInterval,'swL3ospfIfRtrDeadInterval':swL3ospfIfRtrDeadInterval,'swL3ospfIfPollInterval':swL3ospfIfPollInterval,'swL3ospfIfState':swL3ospfIfState,'swL3ospfIfDesignatedRouter':swL3ospfIfDesignatedRouter,'swL3ospfIfBackupDesignatedRouter':swL3ospfIfBackupDesignatedRouter,'swL3ospfIfEvents':swL3ospfIfEvents,'swL3ospfIfMulticastForwarding':swL3ospfIfMulticastForwarding,'swL3ospfIfDemand':swL3ospfIfDemand,'swL3ospfIfAuthType':swL3ospfIfAuthType,'swL3ospfIfAuthKey':swL3ospfIfAuthKey,'swL3ospfIfAuthKeyID':swL3ospfIfAuthKeyID,'swL3ospfIfPassiveMode':swL3ospfIfPassiveMode,'swL3ospfIfMetric':swL3ospfIfMetric,'swL3ospfIfDistributeListInType':swL3ospfIfDistributeListInType,'swL3ospfIfDistributeListInName':swL3ospfIfDistributeListInName,'swL3RoutePreference':swL3RoutePreference,'swL3RoutePreferenceRIP':swL3RoutePreferenceRIP,'swL3RoutePreferenceOSPFIntra':swL3RoutePreferenceOSPFIntra,'swL3RoutePreferenceStatic':swL3RoutePreferenceStatic,'swL3RoutePreferenceLocal':swL3RoutePreferenceLocal,'swL3RoutePreferenceOSPFInter':swL3RoutePreferenceOSPFInter,'swL3RoutePreferenceOSPFExtT1':swL3RoutePreferenceOSPFExtT1,'swL3RoutePreferenceOSPFExtT2':swL3RoutePreferenceOSPFExtT2,'swL3RoutePreferenceDefault':swL3RoutePreferenceDefault,'swL3RoutePreferenceEBGP':swL3RoutePreferenceEBGP,'swL3RoutePreferenceIBGP':swL3RoutePreferenceIBGP,'swL3ospfAreaTable':swL3ospfAreaTable,'swL3ospfAreaEntry':swL3ospfAreaEntry,_A8:swL3ospfAreaId,'swL3ospfAreaType':swL3ospfAreaType,'swL3ospfAreaSummaryState':swL3ospfAreaSummaryState,'swL3ospfAreaMetric':swL3ospfAreaMetric,'swL3ospfAreaTranslateState':swL3ospfAreaTranslateState,'swL3ospfAreaStatus':swL3ospfAreaStatus,'swL3dvmrpInterfaceTable':swL3dvmrpInterfaceTable,'swL3dvmrpInterfaceEntry':swL3dvmrpInterfaceEntry,_A9:swL3dvmrpInterfaceIfIndex,'swL3dvmrpInterfaceLocalAddress':swL3dvmrpInterfaceLocalAddress,'swL3dvmrpInterfaceMetric':swL3dvmrpInterfaceMetric,'swL3dvmrpInterfaceProbe':swL3dvmrpInterfaceProbe,'swL3dvmrpInterfaceNbrTimeout':swL3dvmrpInterfaceNbrTimeout,'swL3dvmrpInterfaceStatus':swL3dvmrpInterfaceStatus,'swL3dvmrpInterfaceRcvBadPkts':swL3dvmrpInterfaceRcvBadPkts,'swL3dvmrpInterfaceRcvBadRoutes':swL3dvmrpInterfaceRcvBadRoutes,'swL3OspfLsdbMgmt':swL3OspfLsdbMgmt,'swL3OspfInternalLsdbTable':swL3OspfInternalLsdbTable,'swL3OspfInternalLsdbEntry':swL3OspfInternalLsdbEntry,_AA:swL3OspfInternalLsdbAreaId,_AB:swL3OspfInternalLsdbType,_AC:swL3OspfInternalLsdbLsid,_AD:swL3OspfInternalLsdbRouterId,'swL3OspfInternalLsdbMetric':swL3OspfInternalLsdbMetric,'swL3OspfInternalLsdbSequenceNo':swL3OspfInternalLsdbSequenceNo,'swL3OspfInternalLsdbAge':swL3OspfInternalLsdbAge,'swL3OspfInternalLsdbChecksum':swL3OspfInternalLsdbChecksum,'swL3OspfExternalLsdbTable':swL3OspfExternalLsdbTable,'swL3OspfExternalLsdbEntry':swL3OspfExternalLsdbEntry,_AG:swL3OspfExternalLsdbType,_AH:swL3OspfExternalLsdbLsid,_AI:swL3OspfExternalLsdbRouterId,'swL3OspfExternalLsdbMetric':swL3OspfExternalLsdbMetric,'swL3OspfExternalLsdbMetricType':swL3OspfExternalLsdbMetricType,'swL3OspfExternalLsdbSequenceNo':swL3OspfExternalLsdbSequenceNo,'swL3OspfExternalLsdbAge':swL3OspfExternalLsdbAge,'swL3OspfExternalLsdbChecksum':swL3OspfExternalLsdbChecksum,'swL3OspfExternalLsdbForwardingAddress':swL3OspfExternalLsdbForwardingAddress,'swL3OspfExternalLsdbRouteTag':swL3OspfExternalLsdbRouteTag,'swL3VrrpOperMgmt':swL3VrrpOperMgmt,'swL3VrrpOperTable':swL3VrrpOperTable,'swL3VrrpOperEntry':swL3VrrpOperEntry,_AJ:swL3VrrpOperIfIndex,_AK:swL3VrrpOperVrId,'swL3VrrpOperVirtualMacAddr':swL3VrrpOperVirtualMacAddr,'swL3VrrpOperState':swL3VrrpOperState,'swL3VrrpOperAdminState':swL3VrrpOperAdminState,'swL3VrrpOperPriority':swL3VrrpOperPriority,'swL3VrrpOperMasterIpAddr':swL3VrrpOperMasterIpAddr,'swL3VrrpOperCriticalIpAddr':swL3VrrpOperCriticalIpAddr,'swL3VrrpOperCheckCriticalIpState':swL3VrrpOperCheckCriticalIpState,'swL3VrrpOperAuthType':swL3VrrpOperAuthType,'swL3VrrpOperAuthKey':swL3VrrpOperAuthKey,'swL3VrrpOperAdvertisementInterval':swL3VrrpOperAdvertisementInterval,'swL3VrrpOperPreemptMode':swL3VrrpOperPreemptMode,'swL3VrrpOperVirtualRouterUpTime':swL3VrrpOperVirtualRouterUpTime,'swL3VrrpOperVirtualIpAddr':swL3VrrpOperVirtualIpAddr,'swL3VrrpOperRowStatus':swL3VrrpOperRowStatus,'swL3OspfECMPMgmt':swL3OspfECMPMgmt,'swL3OspfECMPIpDestination':swL3OspfECMPIpDestination,'swL3OspfECMPIpSource':swL3OspfECMPIpSource,'swL3OspfECMPCrcLow':swL3OspfECMPCrcLow,'swL3OspfECMPCrcHigh':swL3OspfECMPCrcHigh,'swL3OspfECMPTCPorUDPport':swL3OspfECMPTCPorUDPport,'swL3OspfECMPState':swL3OspfECMPState,'swL3RIPTimerMgmt':swL3RIPTimerMgmt,'swL3RIPUpdateTime':swL3RIPUpdateTime,'swL3RIPTimeOutTime':swL3RIPTimeOutTime,'swL3RIPGarbageCollectionTime':swL3RIPGarbageCollectionTime,'swL3OspfDefInfoOrigMgmt':swL3OspfDefInfoOrigMgmt,'swL3OspfDefInfoOriginate':swL3OspfDefInfoOriginate,'swL3OspfDefInfoOrigMetricType':swL3OspfDefInfoOrigMetricType,'swL3OspfDefInfoOrigMetric':swL3OspfDefInfoOrigMetric,'swL3RIPInboundRouteFilterTable':swL3RIPInboundRouteFilterTable,'swL3RIPInboundRouteFilterEntry':swL3RIPInboundRouteFilterEntry,_AL:swL3RIPInboundRouteFilterIfIpAddress,'swL3RIPInboundRouteFilterType':swL3RIPInboundRouteFilterType,'swL3RIPInboundRouteFilterName':swL3RIPInboundRouteFilterName,'swL3Route6RedistriTable':swL3Route6RedistriTable,'swL3Route6RedistriEntry':swL3Route6RedistriEntry,_AM:swL3Route6RedistriSrcProtocol,_AN:swL3Route6RedistriDstProtocol,'swL3Route6RedistriType':swL3Route6RedistriType,'swL3Route6RedistriMetric':swL3Route6RedistriMetric,'swL3Route6RedistriRowStatus':swL3Route6RedistriRowStatus})