_D='read-write'
_C='dot1qVlanIndex'
_B='Q-BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,dot1qVlanIndex=mibBuilder.importSymbols(_B,'PortList',_C)
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlDhcpSpoofing=ModuleIdentity((1,3,6,1,4,1,89,113))
if mibBuilder.loadTexts:rlDhcpSpoofing.setRevisions(('2006-05-15 00:00',))
_RlDhcpSpoofingServerPorts_Type=PortList
_RlDhcpSpoofingServerPorts_Object=MibScalar
rlDhcpSpoofingServerPorts=_RlDhcpSpoofingServerPorts_Object((1,3,6,1,4,1,89,113,1),_RlDhcpSpoofingServerPorts_Type())
rlDhcpSpoofingServerPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:rlDhcpSpoofingServerPorts.setStatus(_A)
_RlDhcpSpoofingVlanTable_Object=MibTable
rlDhcpSpoofingVlanTable=_RlDhcpSpoofingVlanTable_Object((1,3,6,1,4,1,89,113,2))
if mibBuilder.loadTexts:rlDhcpSpoofingVlanTable.setStatus(_A)
_RlDhcpSpoofingVlanEntry_Object=MibTableRow
rlDhcpSpoofingVlanEntry=_RlDhcpSpoofingVlanEntry_Object((1,3,6,1,4,1,89,113,2,1))
rlDhcpSpoofingVlanEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:rlDhcpSpoofingVlanEntry.setStatus(_A)
_RlDhcpSpoofingEnabled_Type=TruthValue
_RlDhcpSpoofingEnabled_Object=MibTableColumn
rlDhcpSpoofingEnabled=_RlDhcpSpoofingEnabled_Object((1,3,6,1,4,1,89,113,2,1,1),_RlDhcpSpoofingEnabled_Type())
rlDhcpSpoofingEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlDhcpSpoofingEnabled.setStatus(_A)
mibBuilder.exportSymbols('RADLAN-DhcpSpoofing-MIB',**{'rlDhcpSpoofing':rlDhcpSpoofing,'rlDhcpSpoofingServerPorts':rlDhcpSpoofingServerPorts,'rlDhcpSpoofingVlanTable':rlDhcpSpoofingVlanTable,'rlDhcpSpoofingVlanEntry':rlDhcpSpoofingVlanEntry,'rlDhcpSpoofingEnabled':rlDhcpSpoofingEnabled})