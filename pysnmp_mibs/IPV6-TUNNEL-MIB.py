_J='agentTunnelIPV6PrefixPrefixLen'
_I='agentTunnelIPV6PrefixPrefix'
_H='InetAddressPrefixLength'
_G='read-write'
_F='not-accessible'
_E='agentTunnelID'
_D='read-create'
_C='Integer32'
_B='IPV6-TUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressIPv4,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4',_H)
Ipv6Address,Ipv6AddressPrefix,Ipv6IfIndex=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressPrefix','Ipv6IfIndex')
switch,=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','switch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ipv6Tunnel=ModuleIdentity((1,3,6,1,4,1,7244,2,27))
_AgentTunnelIPV6Group_ObjectIdentity=ObjectIdentity
agentTunnelIPV6Group=_AgentTunnelIPV6Group_ObjectIdentity((1,3,6,1,4,1,7244,2,27,1))
_AgentTunnelIPV6Table_Object=MibTable
agentTunnelIPV6Table=_AgentTunnelIPV6Table_Object((1,3,6,1,4,1,7244,2,27,1,1))
if mibBuilder.loadTexts:agentTunnelIPV6Table.setStatus(_A)
_AgentTunnelIPV6Entry_Object=MibTableRow
agentTunnelIPV6Entry=_AgentTunnelIPV6Entry_Object((1,3,6,1,4,1,7244,2,27,1,1,1))
agentTunnelIPV6Entry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:agentTunnelIPV6Entry.setStatus(_A)
class _AgentTunnelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentTunnelID_Type.__name__=_C
_AgentTunnelID_Object=MibTableColumn
agentTunnelID=_AgentTunnelID_Object((1,3,6,1,4,1,7244,2,27,1,1,1,1),_AgentTunnelID_Type())
agentTunnelID.setMaxAccess(_F)
if mibBuilder.loadTexts:agentTunnelID.setStatus(_A)
_AgentTunnelIfIndex_Type=Integer32
_AgentTunnelIfIndex_Object=MibTableColumn
agentTunnelIfIndex=_AgentTunnelIfIndex_Object((1,3,6,1,4,1,7244,2,27,1,1,1,2),_AgentTunnelIfIndex_Type())
agentTunnelIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:agentTunnelIfIndex.setStatus(_A)
class _AgentTunnelMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('undefined',1),('ip6over4',2),('ip6to4',3)))
_AgentTunnelMode_Type.__name__=_C
_AgentTunnelMode_Object=MibTableColumn
agentTunnelMode=_AgentTunnelMode_Object((1,3,6,1,4,1,7244,2,27,1,1,1,3),_AgentTunnelMode_Type())
agentTunnelMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentTunnelMode.setStatus(_A)
_AgentTunnelLocalIP4Addr_Type=InetAddressIPv4
_AgentTunnelLocalIP4Addr_Object=MibTableColumn
agentTunnelLocalIP4Addr=_AgentTunnelLocalIP4Addr_Object((1,3,6,1,4,1,7244,2,27,1,1,1,4),_AgentTunnelLocalIP4Addr_Type())
agentTunnelLocalIP4Addr.setMaxAccess(_G)
if mibBuilder.loadTexts:agentTunnelLocalIP4Addr.setStatus(_A)
_AgentTunnelRemoteIP4Addr_Type=InetAddressIPv4
_AgentTunnelRemoteIP4Addr_Object=MibTableColumn
agentTunnelRemoteIP4Addr=_AgentTunnelRemoteIP4Addr_Object((1,3,6,1,4,1,7244,2,27,1,1,1,5),_AgentTunnelRemoteIP4Addr_Type())
agentTunnelRemoteIP4Addr.setMaxAccess(_G)
if mibBuilder.loadTexts:agentTunnelRemoteIP4Addr.setStatus(_A)
_AgentTunnelLocalIfIndex_Type=Integer32
_AgentTunnelLocalIfIndex_Object=MibTableColumn
agentTunnelLocalIfIndex=_AgentTunnelLocalIfIndex_Object((1,3,6,1,4,1,7244,2,27,1,1,1,6),_AgentTunnelLocalIfIndex_Type())
agentTunnelLocalIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:agentTunnelLocalIfIndex.setStatus(_A)
_AgentTunnelStatus_Type=RowStatus
_AgentTunnelStatus_Object=MibTableColumn
agentTunnelStatus=_AgentTunnelStatus_Object((1,3,6,1,4,1,7244,2,27,1,1,1,7),_AgentTunnelStatus_Type())
agentTunnelStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentTunnelStatus.setStatus(_A)
class _AgentTunnelIcmpUnreachableMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentTunnelIcmpUnreachableMode_Type.__name__=_C
_AgentTunnelIcmpUnreachableMode_Object=MibTableColumn
agentTunnelIcmpUnreachableMode=_AgentTunnelIcmpUnreachableMode_Object((1,3,6,1,4,1,7244,2,27,1,1,1,8),_AgentTunnelIcmpUnreachableMode_Type())
agentTunnelIcmpUnreachableMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentTunnelIcmpUnreachableMode.setStatus(_A)
_AgentTunnelIPV6PrefixTable_Object=MibTable
agentTunnelIPV6PrefixTable=_AgentTunnelIPV6PrefixTable_Object((1,3,6,1,4,1,7244,2,27,1,2))
if mibBuilder.loadTexts:agentTunnelIPV6PrefixTable.setStatus(_A)
_AgentTunnelIPV6PrefixEntry_Object=MibTableRow
agentTunnelIPV6PrefixEntry=_AgentTunnelIPV6PrefixEntry_Object((1,3,6,1,4,1,7244,2,27,1,2,1))
agentTunnelIPV6PrefixEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:agentTunnelIPV6PrefixEntry.setStatus(_A)
_AgentTunnelIPV6PrefixPrefix_Type=Ipv6AddressPrefix
_AgentTunnelIPV6PrefixPrefix_Object=MibTableColumn
agentTunnelIPV6PrefixPrefix=_AgentTunnelIPV6PrefixPrefix_Object((1,3,6,1,4,1,7244,2,27,1,2,1,1),_AgentTunnelIPV6PrefixPrefix_Type())
agentTunnelIPV6PrefixPrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:agentTunnelIPV6PrefixPrefix.setStatus(_A)
class _AgentTunnelIPV6PrefixPrefixLen_Type(InetAddressPrefixLength):defaultValue=0
_AgentTunnelIPV6PrefixPrefixLen_Type.__name__=_H
_AgentTunnelIPV6PrefixPrefixLen_Object=MibTableColumn
agentTunnelIPV6PrefixPrefixLen=_AgentTunnelIPV6PrefixPrefixLen_Object((1,3,6,1,4,1,7244,2,27,1,2,1,2),_AgentTunnelIPV6PrefixPrefixLen_Type())
agentTunnelIPV6PrefixPrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:agentTunnelIPV6PrefixPrefixLen.setStatus(_A)
_AgentTunnelIPV6PrefixStatus_Type=RowStatus
_AgentTunnelIPV6PrefixStatus_Object=MibTableColumn
agentTunnelIPV6PrefixStatus=_AgentTunnelIPV6PrefixStatus_Object((1,3,6,1,4,1,7244,2,27,1,2,1,3),_AgentTunnelIPV6PrefixStatus_Type())
agentTunnelIPV6PrefixStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentTunnelIPV6PrefixStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipv6Tunnel':ipv6Tunnel,'agentTunnelIPV6Group':agentTunnelIPV6Group,'agentTunnelIPV6Table':agentTunnelIPV6Table,'agentTunnelIPV6Entry':agentTunnelIPV6Entry,_E:agentTunnelID,'agentTunnelIfIndex':agentTunnelIfIndex,'agentTunnelMode':agentTunnelMode,'agentTunnelLocalIP4Addr':agentTunnelLocalIP4Addr,'agentTunnelRemoteIP4Addr':agentTunnelRemoteIP4Addr,'agentTunnelLocalIfIndex':agentTunnelLocalIfIndex,'agentTunnelStatus':agentTunnelStatus,'agentTunnelIcmpUnreachableMode':agentTunnelIcmpUnreachableMode,'agentTunnelIPV6PrefixTable':agentTunnelIPV6PrefixTable,'agentTunnelIPV6PrefixEntry':agentTunnelIPV6PrefixEntry,_I:agentTunnelIPV6PrefixPrefix,_J:agentTunnelIPV6PrefixPrefixLen,'agentTunnelIPV6PrefixStatus':agentTunnelIPV6PrefixStatus})