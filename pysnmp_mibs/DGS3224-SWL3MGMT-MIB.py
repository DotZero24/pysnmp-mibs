_P='swL3Ipv6AddressCtrlPrefixLen'
_O='swL3Ipv6Address'
_N='swL3Ipv6AddressCtrlInterfaceName'
_M='swL3Ipv6CtrlInterfaceName'
_L='read-create'
_K='swL3IpCtrlInterfaceName'
_J='other'
_I='Unsigned32'
_H='DGS3224-SWL3MGMT-MIB'
_G='DisplayString'
_F='disabled'
_E='enabled'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
dgs3224,=mibBuilder.importSymbols('SW3200PRIMGMT-MIB','dgs3224')
swL3MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,101,3,3))
class NodeAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class NetAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
class VrId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL3IpMgmt_ObjectIdentity=ObjectIdentity
swL3IpMgmt=_SwL3IpMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,3,3,2))
_SwL3IpCtrlMgmt_ObjectIdentity=ObjectIdentity
swL3IpCtrlMgmt=_SwL3IpCtrlMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,3,3,2,1))
_SwL3IpCtrlTable_Object=MibTable
swL3IpCtrlTable=_SwL3IpCtrlTable_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3))
if mibBuilder.loadTexts:swL3IpCtrlTable.setStatus(_A)
_SwL3IpCtrlEntry_Object=MibTableRow
swL3IpCtrlEntry=_SwL3IpCtrlEntry_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1))
swL3IpCtrlEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:swL3IpCtrlEntry.setStatus(_A)
class _SwL3IpCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3IpCtrlInterfaceName_Type.__name__=_G
_SwL3IpCtrlInterfaceName_Object=MibTableColumn
swL3IpCtrlInterfaceName=_SwL3IpCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,1),_SwL3IpCtrlInterfaceName_Type())
swL3IpCtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlInterfaceName.setStatus(_A)
class _SwL3IpCtrlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpCtrlIfIndex_Type.__name__=_C
_SwL3IpCtrlIfIndex_Object=MibTableColumn
swL3IpCtrlIfIndex=_SwL3IpCtrlIfIndex_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,2),_SwL3IpCtrlIfIndex_Type())
swL3IpCtrlIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIfIndex.setStatus(_A)
_SwL3IpCtrlIpAddr_Type=IpAddress
_SwL3IpCtrlIpAddr_Object=MibTableColumn
swL3IpCtrlIpAddr=_SwL3IpCtrlIpAddr_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,3),_SwL3IpCtrlIpAddr_Type())
swL3IpCtrlIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlIpAddr.setStatus(_A)
_SwL3IpCtrlIpSubnetMask_Type=IpAddress
_SwL3IpCtrlIpSubnetMask_Object=MibTableColumn
swL3IpCtrlIpSubnetMask=_SwL3IpCtrlIpSubnetMask_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,4),_SwL3IpCtrlIpSubnetMask_Type())
swL3IpCtrlIpSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlIpSubnetMask.setStatus(_A)
class _SwL3IpCtrlVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL3IpCtrlVlanName_Type.__name__=_G
_SwL3IpCtrlVlanName_Object=MibTableColumn
swL3IpCtrlVlanName=_SwL3IpCtrlVlanName_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,5),_SwL3IpCtrlVlanName_Type())
swL3IpCtrlVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlVlanName.setStatus(_A)
class _SwL3IpCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_J,1),('bootp',3),('dhcp',4)))
_SwL3IpCtrlMode_Type.__name__=_C
_SwL3IpCtrlMode_Object=MibTableColumn
swL3IpCtrlMode=_SwL3IpCtrlMode_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,8),_SwL3IpCtrlMode_Type())
swL3IpCtrlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlMode.setStatus(_A)
class _SwL3IpCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwL3IpCtrlAdminState_Type.__name__=_C
_SwL3IpCtrlAdminState_Object=MibTableColumn
swL3IpCtrlAdminState=_SwL3IpCtrlAdminState_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,9),_SwL3IpCtrlAdminState_Type())
swL3IpCtrlAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlAdminState.setStatus(_A)
_SwL3IpCtrlIpv6LinkLocalAddress_Type=Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress=_SwL3IpCtrlIpv6LinkLocalAddress_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,14),_SwL3IpCtrlIpv6LinkLocalAddress_Type())
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalAddress.setStatus(_A)
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type=Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen=_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,15),_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type())
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus(_A)
_SwL3IpCtrlState_Type=RowStatus
_SwL3IpCtrlState_Object=MibTableColumn
swL3IpCtrlState=_SwL3IpCtrlState_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,16),_SwL3IpCtrlState_Type())
swL3IpCtrlState.setMaxAccess(_L)
if mibBuilder.loadTexts:swL3IpCtrlState.setStatus(_A)
class _SwL3IpCtrlIpv6LinkLocalAutoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_E,2),(_F,3)))
_SwL3IpCtrlIpv6LinkLocalAutoState_Type.__name__=_C
_SwL3IpCtrlIpv6LinkLocalAutoState_Object=MibTableColumn
swL3IpCtrlIpv6LinkLocalAutoState=_SwL3IpCtrlIpv6LinkLocalAutoState_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,17),_SwL3IpCtrlIpv6LinkLocalAutoState_Type())
swL3IpCtrlIpv6LinkLocalAutoState.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlIpv6LinkLocalAutoState.setStatus(_A)
class _SwL3IpCtrlDhcpv6ClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwL3IpCtrlDhcpv6ClientState_Type.__name__=_C
_SwL3IpCtrlDhcpv6ClientState_Object=MibTableColumn
swL3IpCtrlDhcpv6ClientState=_SwL3IpCtrlDhcpv6ClientState_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,20),_SwL3IpCtrlDhcpv6ClientState_Type())
swL3IpCtrlDhcpv6ClientState.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlDhcpv6ClientState.setStatus(_A)
class _SwL3IpCtrlIpDhcpOption12State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwL3IpCtrlIpDhcpOption12State_Type.__name__=_C
_SwL3IpCtrlIpDhcpOption12State_Object=MibTableColumn
swL3IpCtrlIpDhcpOption12State=_SwL3IpCtrlIpDhcpOption12State_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,22),_SwL3IpCtrlIpDhcpOption12State_Type())
swL3IpCtrlIpDhcpOption12State.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlIpDhcpOption12State.setStatus(_A)
class _SwL3IpCtrlIpDhcpOption12HostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_SwL3IpCtrlIpDhcpOption12HostName_Type.__name__=_G
_SwL3IpCtrlIpDhcpOption12HostName_Object=MibTableColumn
swL3IpCtrlIpDhcpOption12HostName=_SwL3IpCtrlIpDhcpOption12HostName_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,3,1,23),_SwL3IpCtrlIpDhcpOption12HostName_Type())
swL3IpCtrlIpDhcpOption12HostName.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlIpDhcpOption12HostName.setStatus(_A)
_SwL3Ipv6CtrlTable_Object=MibTable
swL3Ipv6CtrlTable=_SwL3Ipv6CtrlTable_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4))
if mibBuilder.loadTexts:swL3Ipv6CtrlTable.setStatus(_A)
_SwL3Ipv6CtrlEntry_Object=MibTableRow
swL3Ipv6CtrlEntry=_SwL3Ipv6CtrlEntry_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1))
swL3Ipv6CtrlEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:swL3Ipv6CtrlEntry.setStatus(_A)
class _SwL3Ipv6CtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6CtrlInterfaceName_Type.__name__=_G
_SwL3Ipv6CtrlInterfaceName_Object=MibTableColumn
swL3Ipv6CtrlInterfaceName=_SwL3Ipv6CtrlInterfaceName_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,1),_SwL3Ipv6CtrlInterfaceName_Type())
swL3Ipv6CtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlInterfaceName.setStatus(_A)
_SwL3Ipv6CtrlMaxReassmblySize_Type=Integer32
_SwL3Ipv6CtrlMaxReassmblySize_Object=MibTableColumn
swL3Ipv6CtrlMaxReassmblySize=_SwL3Ipv6CtrlMaxReassmblySize_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,2),_SwL3Ipv6CtrlMaxReassmblySize_Type())
swL3Ipv6CtrlMaxReassmblySize.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6CtrlMaxReassmblySize.setStatus(_A)
class _SwL3Ipv6CtrlNsRetransTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SwL3Ipv6CtrlNsRetransTimer_Type.__name__=_I
_SwL3Ipv6CtrlNsRetransTimer_Object=MibTableColumn
swL3Ipv6CtrlNsRetransTimer=_SwL3Ipv6CtrlNsRetransTimer_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,3),_SwL3Ipv6CtrlNsRetransTimer_Type())
swL3Ipv6CtrlNsRetransTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlNsRetransTimer.setStatus(_A)
class _SwL3Ipv6CtrlRaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwL3Ipv6CtrlRaState_Type.__name__=_C
_SwL3Ipv6CtrlRaState_Object=MibTableColumn
swL3Ipv6CtrlRaState=_SwL3Ipv6CtrlRaState_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,5),_SwL3Ipv6CtrlRaState_Type())
swL3Ipv6CtrlRaState.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaState.setStatus(_A)
class _SwL3Ipv6CtrlRaMinRtrAdvInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1350))
_SwL3Ipv6CtrlRaMinRtrAdvInterval_Type.__name__=_C
_SwL3Ipv6CtrlRaMinRtrAdvInterval_Object=MibTableColumn
swL3Ipv6CtrlRaMinRtrAdvInterval=_SwL3Ipv6CtrlRaMinRtrAdvInterval_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,6),_SwL3Ipv6CtrlRaMinRtrAdvInterval_Type())
swL3Ipv6CtrlRaMinRtrAdvInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaMinRtrAdvInterval.setStatus(_A)
class _SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type.__name__=_C
_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object=MibTableColumn
swL3Ipv6CtrlRaMaxRtrAdvInterval=_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,7),_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type())
swL3Ipv6CtrlRaMaxRtrAdvInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaMaxRtrAdvInterval.setStatus(_A)
class _SwL3Ipv6CtrlRaLifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_SwL3Ipv6CtrlRaLifeTime_Type.__name__=_C
_SwL3Ipv6CtrlRaLifeTime_Object=MibTableColumn
swL3Ipv6CtrlRaLifeTime=_SwL3Ipv6CtrlRaLifeTime_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,8),_SwL3Ipv6CtrlRaLifeTime_Type())
swL3Ipv6CtrlRaLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaLifeTime.setStatus(_A)
class _SwL3Ipv6CtrlRaReachableTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_SwL3Ipv6CtrlRaReachableTime_Type.__name__=_C
_SwL3Ipv6CtrlRaReachableTime_Object=MibTableColumn
swL3Ipv6CtrlRaReachableTime=_SwL3Ipv6CtrlRaReachableTime_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,9),_SwL3Ipv6CtrlRaReachableTime_Type())
swL3Ipv6CtrlRaReachableTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaReachableTime.setStatus(_A)
class _SwL3Ipv6CtrlRaRetransTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SwL3Ipv6CtrlRaRetransTime_Type.__name__=_I
_SwL3Ipv6CtrlRaRetransTime_Object=MibTableColumn
swL3Ipv6CtrlRaRetransTime=_SwL3Ipv6CtrlRaRetransTime_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,10),_SwL3Ipv6CtrlRaRetransTime_Type())
swL3Ipv6CtrlRaRetransTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaRetransTime.setStatus(_A)
class _SwL3Ipv6CtrlRaHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3Ipv6CtrlRaHopLimit_Type.__name__=_C
_SwL3Ipv6CtrlRaHopLimit_Object=MibTableColumn
swL3Ipv6CtrlRaHopLimit=_SwL3Ipv6CtrlRaHopLimit_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,11),_SwL3Ipv6CtrlRaHopLimit_Type())
swL3Ipv6CtrlRaHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaHopLimit.setStatus(_A)
class _SwL3Ipv6CtrlRaManagedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwL3Ipv6CtrlRaManagedFlag_Type.__name__=_C
_SwL3Ipv6CtrlRaManagedFlag_Object=MibTableColumn
swL3Ipv6CtrlRaManagedFlag=_SwL3Ipv6CtrlRaManagedFlag_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,12),_SwL3Ipv6CtrlRaManagedFlag_Type())
swL3Ipv6CtrlRaManagedFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaManagedFlag.setStatus(_A)
class _SwL3Ipv6CtrlRaOtherConfigFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwL3Ipv6CtrlRaOtherConfigFlag_Type.__name__=_C
_SwL3Ipv6CtrlRaOtherConfigFlag_Object=MibTableColumn
swL3Ipv6CtrlRaOtherConfigFlag=_SwL3Ipv6CtrlRaOtherConfigFlag_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,4,1,13),_SwL3Ipv6CtrlRaOtherConfigFlag_Type())
swL3Ipv6CtrlRaOtherConfigFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6CtrlRaOtherConfigFlag.setStatus(_A)
_SwL3Ipv6AddressCtrlTable_Object=MibTable
swL3Ipv6AddressCtrlTable=_SwL3Ipv6AddressCtrlTable_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5))
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlTable.setStatus(_A)
_SwL3Ipv6AddressCtrlEntry_Object=MibTableRow
swL3Ipv6AddressCtrlEntry=_SwL3Ipv6AddressCtrlEntry_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1))
swL3Ipv6AddressCtrlEntry.setIndexNames((0,_H,_N),(0,_H,_O),(0,_H,_P))
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlEntry.setStatus(_A)
class _SwL3Ipv6AddressCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3Ipv6AddressCtrlInterfaceName_Type.__name__=_G
_SwL3Ipv6AddressCtrlInterfaceName_Object=MibTableColumn
swL3Ipv6AddressCtrlInterfaceName=_SwL3Ipv6AddressCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1,1),_SwL3Ipv6AddressCtrlInterfaceName_Type())
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlInterfaceName.setStatus(_A)
_SwL3Ipv6Address_Type=Ipv6Address
_SwL3Ipv6Address_Object=MibTableColumn
swL3Ipv6Address=_SwL3Ipv6Address_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1,2),_SwL3Ipv6Address_Type())
swL3Ipv6Address.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6Address.setStatus(_A)
_SwL3Ipv6AddressCtrlPrefixLen_Type=Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object=MibTableColumn
swL3Ipv6AddressCtrlPrefixLen=_SwL3Ipv6AddressCtrlPrefixLen_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1,3),_SwL3Ipv6AddressCtrlPrefixLen_Type())
swL3Ipv6AddressCtrlPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlPrefixLen.setStatus(_A)
class _SwL3Ipv6AddressCtrlPreferredLifeTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwL3Ipv6AddressCtrlPreferredLifeTime_Type.__name__=_I
_SwL3Ipv6AddressCtrlPreferredLifeTime_Object=MibTableColumn
swL3Ipv6AddressCtrlPreferredLifeTime=_SwL3Ipv6AddressCtrlPreferredLifeTime_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1,4),_SwL3Ipv6AddressCtrlPreferredLifeTime_Type())
swL3Ipv6AddressCtrlPreferredLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlPreferredLifeTime.setStatus(_A)
class _SwL3Ipv6AddressCtrlValidLifeTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwL3Ipv6AddressCtrlValidLifeTime_Type.__name__=_I
_SwL3Ipv6AddressCtrlValidLifeTime_Object=MibTableColumn
swL3Ipv6AddressCtrlValidLifeTime=_SwL3Ipv6AddressCtrlValidLifeTime_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1,5),_SwL3Ipv6AddressCtrlValidLifeTime_Type())
swL3Ipv6AddressCtrlValidLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlValidLifeTime.setStatus(_A)
class _SwL3Ipv6AddressCtrlOnLinkFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwL3Ipv6AddressCtrlOnLinkFlag_Type.__name__=_C
_SwL3Ipv6AddressCtrlOnLinkFlag_Object=MibTableColumn
swL3Ipv6AddressCtrlOnLinkFlag=_SwL3Ipv6AddressCtrlOnLinkFlag_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1,6),_SwL3Ipv6AddressCtrlOnLinkFlag_Type())
swL3Ipv6AddressCtrlOnLinkFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlOnLinkFlag.setStatus(_A)
class _SwL3Ipv6AddressCtrlAutonomousFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwL3Ipv6AddressCtrlAutonomousFlag_Type.__name__=_C
_SwL3Ipv6AddressCtrlAutonomousFlag_Object=MibTableColumn
swL3Ipv6AddressCtrlAutonomousFlag=_SwL3Ipv6AddressCtrlAutonomousFlag_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1,7),_SwL3Ipv6AddressCtrlAutonomousFlag_Type())
swL3Ipv6AddressCtrlAutonomousFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlAutonomousFlag.setStatus(_A)
_SwL3Ipv6AddressCtrlState_Type=RowStatus
_SwL3Ipv6AddressCtrlState_Object=MibTableColumn
swL3Ipv6AddressCtrlState=_SwL3Ipv6AddressCtrlState_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1,8),_SwL3Ipv6AddressCtrlState_Type())
swL3Ipv6AddressCtrlState.setMaxAccess(_L)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlState.setStatus(_A)
class _SwL3Ipv6AddressCtrlAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('dhcpv6',2),('stateless',3)))
_SwL3Ipv6AddressCtrlAddressType_Type.__name__=_C
_SwL3Ipv6AddressCtrlAddressType_Object=MibTableColumn
swL3Ipv6AddressCtrlAddressType=_SwL3Ipv6AddressCtrlAddressType_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,5,1,9),_SwL3Ipv6AddressCtrlAddressType_Type())
swL3Ipv6AddressCtrlAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3Ipv6AddressCtrlAddressType.setStatus(_A)
class _SwL3IpCtrlAllIpIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_E,2),(_F,3)))
_SwL3IpCtrlAllIpIfState_Type.__name__=_C
_SwL3IpCtrlAllIpIfState_Object=MibScalar
swL3IpCtrlAllIpIfState=_SwL3IpCtrlAllIpIfState_Object((1,3,6,1,4,1,171,11,101,3,3,2,1,7),_SwL3IpCtrlAllIpIfState_Type())
swL3IpCtrlAllIpIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:swL3IpCtrlAllIpIfState.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'NodeAddress':NodeAddress,'NetAddress':NetAddress,'Ipv6Address':Ipv6Address,'VrId':VrId,'swL3MgmtMIB':swL3MgmtMIB,'swL3IpMgmt':swL3IpMgmt,'swL3IpCtrlMgmt':swL3IpCtrlMgmt,'swL3IpCtrlTable':swL3IpCtrlTable,'swL3IpCtrlEntry':swL3IpCtrlEntry,_K:swL3IpCtrlInterfaceName,'swL3IpCtrlIfIndex':swL3IpCtrlIfIndex,'swL3IpCtrlIpAddr':swL3IpCtrlIpAddr,'swL3IpCtrlIpSubnetMask':swL3IpCtrlIpSubnetMask,'swL3IpCtrlVlanName':swL3IpCtrlVlanName,'swL3IpCtrlMode':swL3IpCtrlMode,'swL3IpCtrlAdminState':swL3IpCtrlAdminState,'swL3IpCtrlIpv6LinkLocalAddress':swL3IpCtrlIpv6LinkLocalAddress,'swL3IpCtrlIpv6LinkLocalPrefixLen':swL3IpCtrlIpv6LinkLocalPrefixLen,'swL3IpCtrlState':swL3IpCtrlState,'swL3IpCtrlIpv6LinkLocalAutoState':swL3IpCtrlIpv6LinkLocalAutoState,'swL3IpCtrlDhcpv6ClientState':swL3IpCtrlDhcpv6ClientState,'swL3IpCtrlIpDhcpOption12State':swL3IpCtrlIpDhcpOption12State,'swL3IpCtrlIpDhcpOption12HostName':swL3IpCtrlIpDhcpOption12HostName,'swL3Ipv6CtrlTable':swL3Ipv6CtrlTable,'swL3Ipv6CtrlEntry':swL3Ipv6CtrlEntry,_M:swL3Ipv6CtrlInterfaceName,'swL3Ipv6CtrlMaxReassmblySize':swL3Ipv6CtrlMaxReassmblySize,'swL3Ipv6CtrlNsRetransTimer':swL3Ipv6CtrlNsRetransTimer,'swL3Ipv6CtrlRaState':swL3Ipv6CtrlRaState,'swL3Ipv6CtrlRaMinRtrAdvInterval':swL3Ipv6CtrlRaMinRtrAdvInterval,'swL3Ipv6CtrlRaMaxRtrAdvInterval':swL3Ipv6CtrlRaMaxRtrAdvInterval,'swL3Ipv6CtrlRaLifeTime':swL3Ipv6CtrlRaLifeTime,'swL3Ipv6CtrlRaReachableTime':swL3Ipv6CtrlRaReachableTime,'swL3Ipv6CtrlRaRetransTime':swL3Ipv6CtrlRaRetransTime,'swL3Ipv6CtrlRaHopLimit':swL3Ipv6CtrlRaHopLimit,'swL3Ipv6CtrlRaManagedFlag':swL3Ipv6CtrlRaManagedFlag,'swL3Ipv6CtrlRaOtherConfigFlag':swL3Ipv6CtrlRaOtherConfigFlag,'swL3Ipv6AddressCtrlTable':swL3Ipv6AddressCtrlTable,'swL3Ipv6AddressCtrlEntry':swL3Ipv6AddressCtrlEntry,_N:swL3Ipv6AddressCtrlInterfaceName,_O:swL3Ipv6Address,_P:swL3Ipv6AddressCtrlPrefixLen,'swL3Ipv6AddressCtrlPreferredLifeTime':swL3Ipv6AddressCtrlPreferredLifeTime,'swL3Ipv6AddressCtrlValidLifeTime':swL3Ipv6AddressCtrlValidLifeTime,'swL3Ipv6AddressCtrlOnLinkFlag':swL3Ipv6AddressCtrlOnLinkFlag,'swL3Ipv6AddressCtrlAutonomousFlag':swL3Ipv6AddressCtrlAutonomousFlag,'swL3Ipv6AddressCtrlState':swL3Ipv6AddressCtrlState,'swL3Ipv6AddressCtrlAddressType':swL3Ipv6AddressCtrlAddressType,'swL3IpCtrlAllIpIfState':swL3IpCtrlAllIpIfState})