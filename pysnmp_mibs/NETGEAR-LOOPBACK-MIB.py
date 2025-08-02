_E='read-write'
_D='agentLoopbackID'
_C='NETGEAR-LOOPBACK-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressIPv4,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fastPathLoopback=ModuleIdentity((1,3,6,1,4,1,4526,10,22))
if mibBuilder.loadTexts:fastPathLoopback.setRevisions(('2011-01-26 00:00','2007-05-23 00:00'))
_AgentLoopbackGroup_ObjectIdentity=ObjectIdentity
agentLoopbackGroup=_AgentLoopbackGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,22,1))
_AgentLoopbackTable_Object=MibTable
agentLoopbackTable=_AgentLoopbackTable_Object((1,3,6,1,4,1,4526,10,22,1,1))
if mibBuilder.loadTexts:agentLoopbackTable.setStatus(_A)
_AgentLoopbackEntry_Object=MibTableRow
agentLoopbackEntry=_AgentLoopbackEntry_Object((1,3,6,1,4,1,4526,10,22,1,1,1))
agentLoopbackEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:agentLoopbackEntry.setStatus(_A)
class _AgentLoopbackID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentLoopbackID_Type.__name__=_B
_AgentLoopbackID_Object=MibTableColumn
agentLoopbackID=_AgentLoopbackID_Object((1,3,6,1,4,1,4526,10,22,1,1,1,1),_AgentLoopbackID_Type())
agentLoopbackID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentLoopbackID.setStatus(_A)
_AgentLoopbackIfIndex_Type=Integer32
_AgentLoopbackIfIndex_Object=MibTableColumn
agentLoopbackIfIndex=_AgentLoopbackIfIndex_Object((1,3,6,1,4,1,4526,10,22,1,1,1,2),_AgentLoopbackIfIndex_Type())
agentLoopbackIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:agentLoopbackIfIndex.setStatus(_A)
_AgentLoopbackIPAddress_Type=InetAddressIPv4
_AgentLoopbackIPAddress_Object=MibTableColumn
agentLoopbackIPAddress=_AgentLoopbackIPAddress_Object((1,3,6,1,4,1,4526,10,22,1,1,1,3),_AgentLoopbackIPAddress_Type())
agentLoopbackIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentLoopbackIPAddress.setStatus(_A)
_AgentLoopbackIPSubnet_Type=InetAddressIPv4
_AgentLoopbackIPSubnet_Object=MibTableColumn
agentLoopbackIPSubnet=_AgentLoopbackIPSubnet_Object((1,3,6,1,4,1,4526,10,22,1,1,1,4),_AgentLoopbackIPSubnet_Type())
agentLoopbackIPSubnet.setMaxAccess(_E)
if mibBuilder.loadTexts:agentLoopbackIPSubnet.setStatus(_A)
_AgentLoopbackStatus_Type=RowStatus
_AgentLoopbackStatus_Object=MibTableColumn
agentLoopbackStatus=_AgentLoopbackStatus_Object((1,3,6,1,4,1,4526,10,22,1,1,1,5),_AgentLoopbackStatus_Type())
agentLoopbackStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:agentLoopbackStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fastPathLoopback':fastPathLoopback,'agentLoopbackGroup':agentLoopbackGroup,'agentLoopbackTable':agentLoopbackTable,'agentLoopbackEntry':agentLoopbackEntry,_D:agentLoopbackID,'agentLoopbackIfIndex':agentLoopbackIfIndex,'agentLoopbackIPAddress':agentLoopbackIPAddress,'agentLoopbackIPSubnet':agentLoopbackIPSubnet,'agentLoopbackStatus':agentLoopbackStatus})