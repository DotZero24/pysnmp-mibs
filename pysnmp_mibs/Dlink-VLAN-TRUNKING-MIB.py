_C='current'
_B='read-write'
_A='TruthValue'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_A)
rlVlanTrunking=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,136))
if mibBuilder.loadTexts:rlVlanTrunking.setRevisions(('2007-11-18 00:00',))
class _RlVlanTrunkingEnabled_Type(TruthValue):defaultValue=2
_RlVlanTrunkingEnabled_Type.__name__=_A
_RlVlanTrunkingEnabled_Object=MibScalar
rlVlanTrunkingEnabled=_RlVlanTrunkingEnabled_Object((1,3,6,1,4,1,171,10,94,89,89,136,1),_RlVlanTrunkingEnabled_Type())
rlVlanTrunkingEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:rlVlanTrunkingEnabled.setStatus(_C)
_RlVlanTrunkingUplinkPorts_Type=PortList
_RlVlanTrunkingUplinkPorts_Object=MibScalar
rlVlanTrunkingUplinkPorts=_RlVlanTrunkingUplinkPorts_Object((1,3,6,1,4,1,171,10,94,89,89,136,2),_RlVlanTrunkingUplinkPorts_Type())
rlVlanTrunkingUplinkPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlVlanTrunkingUplinkPorts.setStatus(_C)
mibBuilder.exportSymbols('Dlink-VLAN-TRUNKING-MIB',**{'rlVlanTrunking':rlVlanTrunking,'rlVlanTrunkingEnabled':rlVlanTrunkingEnabled,'rlVlanTrunkingUplinkPorts':rlVlanTrunkingUplinkPorts})