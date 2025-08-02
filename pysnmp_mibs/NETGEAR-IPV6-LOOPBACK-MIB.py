_H='not-accessible'
_G='agentLoopbackIpv6PrefixPrefixLen'
_F='agentLoopbackIpv6PrefixPrefix'
_E='agentLoopbackID'
_D='NETGEAR-LOOPBACK-MIB'
_C='InetAddressPrefixLength'
_B='NETGEAR-IPV6-LOOPBACK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressPrefixLength,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_C)
Ipv6AddressPrefix,=mibBuilder.importSymbols('IPV6-TC','Ipv6AddressPrefix')
agentLoopbackID,=mibBuilder.importSymbols(_D,_E)
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fastPathIpv6Loopback=ModuleIdentity((1,3,6,1,4,1,4526,10,23))
if mibBuilder.loadTexts:fastPathIpv6Loopback.setRevisions(('2011-01-26 00:00','2007-05-23 00:00'))
_AgentLoopbackIpv6Group_ObjectIdentity=ObjectIdentity
agentLoopbackIpv6Group=_AgentLoopbackIpv6Group_ObjectIdentity((1,3,6,1,4,1,4526,10,23,1))
_AgentLoopbackIpv6PrefixTable_Object=MibTable
agentLoopbackIpv6PrefixTable=_AgentLoopbackIpv6PrefixTable_Object((1,3,6,1,4,1,4526,10,23,1,1))
if mibBuilder.loadTexts:agentLoopbackIpv6PrefixTable.setStatus(_A)
_AgentLoopbackIpv6PrefixEntry_Object=MibTableRow
agentLoopbackIpv6PrefixEntry=_AgentLoopbackIpv6PrefixEntry_Object((1,3,6,1,4,1,4526,10,23,1,1,1))
agentLoopbackIpv6PrefixEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:agentLoopbackIpv6PrefixEntry.setStatus(_A)
_AgentLoopbackIpv6PrefixPrefix_Type=Ipv6AddressPrefix
_AgentLoopbackIpv6PrefixPrefix_Object=MibTableColumn
agentLoopbackIpv6PrefixPrefix=_AgentLoopbackIpv6PrefixPrefix_Object((1,3,6,1,4,1,4526,10,23,1,1,1,1),_AgentLoopbackIpv6PrefixPrefix_Type())
agentLoopbackIpv6PrefixPrefix.setMaxAccess(_H)
if mibBuilder.loadTexts:agentLoopbackIpv6PrefixPrefix.setStatus(_A)
class _AgentLoopbackIpv6PrefixPrefixLen_Type(InetAddressPrefixLength):defaultValue=0
_AgentLoopbackIpv6PrefixPrefixLen_Type.__name__=_C
_AgentLoopbackIpv6PrefixPrefixLen_Object=MibTableColumn
agentLoopbackIpv6PrefixPrefixLen=_AgentLoopbackIpv6PrefixPrefixLen_Object((1,3,6,1,4,1,4526,10,23,1,1,1,2),_AgentLoopbackIpv6PrefixPrefixLen_Type())
agentLoopbackIpv6PrefixPrefixLen.setMaxAccess(_H)
if mibBuilder.loadTexts:agentLoopbackIpv6PrefixPrefixLen.setStatus(_A)
_AgentLoopbackIpv6PrefixStatus_Type=RowStatus
_AgentLoopbackIpv6PrefixStatus_Object=MibTableColumn
agentLoopbackIpv6PrefixStatus=_AgentLoopbackIpv6PrefixStatus_Object((1,3,6,1,4,1,4526,10,23,1,1,1,3),_AgentLoopbackIpv6PrefixStatus_Type())
agentLoopbackIpv6PrefixStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:agentLoopbackIpv6PrefixStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fastPathIpv6Loopback':fastPathIpv6Loopback,'agentLoopbackIpv6Group':agentLoopbackIpv6Group,'agentLoopbackIpv6PrefixTable':agentLoopbackIpv6PrefixTable,'agentLoopbackIpv6PrefixEntry':agentLoopbackIpv6PrefixEntry,_F:agentLoopbackIpv6PrefixPrefix,_G:agentLoopbackIpv6PrefixPrefixLen,'agentLoopbackIpv6PrefixStatus':agentLoopbackIpv6PrefixStatus})