_E='hpicfDot1qIsolatedPortGroup'
_D='hpicfDot1qVlanStaticIsolatedPorts'
_C='hpicfDot1qIsolatedPortsEntry'
_B='HP-ICF-ISOLATED-PORTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
PortList,dot1qVlanStaticEntry=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','dot1qVlanStaticEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfDot1qIsolatedPorts=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,109))
if mibBuilder.loadTexts:hpicfDot1qIsolatedPorts.setRevisions(('2014-04-14 00:00',))
_HpicfDot1qIsolatedPortConfigurationObjects_ObjectIdentity=ObjectIdentity
hpicfDot1qIsolatedPortConfigurationObjects=_HpicfDot1qIsolatedPortConfigurationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,109,1))
_HpicfDot1qIsolatedPortsTable_Object=MibTable
hpicfDot1qIsolatedPortsTable=_HpicfDot1qIsolatedPortsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,109,1,1))
if mibBuilder.loadTexts:hpicfDot1qIsolatedPortsTable.setStatus(_A)
_HpicfDot1qIsolatedPortsEntry_Object=MibTableRow
hpicfDot1qIsolatedPortsEntry=_HpicfDot1qIsolatedPortsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,109,1,1,1))
if mibBuilder.loadTexts:hpicfDot1qIsolatedPortsEntry.setStatus(_A)
_HpicfDot1qVlanStaticIsolatedPorts_Type=PortList
_HpicfDot1qVlanStaticIsolatedPorts_Object=MibTableColumn
hpicfDot1qVlanStaticIsolatedPorts=_HpicfDot1qVlanStaticIsolatedPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,109,1,1,1,1),_HpicfDot1qVlanStaticIsolatedPorts_Type())
hpicfDot1qVlanStaticIsolatedPorts.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpicfDot1qVlanStaticIsolatedPorts.setStatus(_A)
_HpicfDot1qIsolatedPortConformance_ObjectIdentity=ObjectIdentity
hpicfDot1qIsolatedPortConformance=_HpicfDot1qIsolatedPortConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,109,2))
_HpicfDot1qIsolatedPortCompliances_ObjectIdentity=ObjectIdentity
hpicfDot1qIsolatedPortCompliances=_HpicfDot1qIsolatedPortCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,109,2,1))
_HpicfDot1qIsolatedPortGroups_ObjectIdentity=ObjectIdentity
hpicfDot1qIsolatedPortGroups=_HpicfDot1qIsolatedPortGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,109,2,2))
dot1qVlanStaticEntry.registerAugmentions((_B,_C))
hpicfDot1qIsolatedPortsEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
hpicfDot1qIsolatedPortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,109,2,2,1))
hpicfDot1qIsolatedPortGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:hpicfDot1qIsolatedPortGroup.setStatus(_A)
hpicfDot1qIsolatedPortCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,109,2,1,1))
hpicfDot1qIsolatedPortCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:hpicfDot1qIsolatedPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfDot1qIsolatedPorts':hpicfDot1qIsolatedPorts,'hpicfDot1qIsolatedPortConfigurationObjects':hpicfDot1qIsolatedPortConfigurationObjects,'hpicfDot1qIsolatedPortsTable':hpicfDot1qIsolatedPortsTable,_C:hpicfDot1qIsolatedPortsEntry,_D:hpicfDot1qVlanStaticIsolatedPorts,'hpicfDot1qIsolatedPortConformance':hpicfDot1qIsolatedPortConformance,'hpicfDot1qIsolatedPortCompliances':hpicfDot1qIsolatedPortCompliances,'hpicfDot1qIsolatedPortCompliance':hpicfDot1qIsolatedPortCompliance,'hpicfDot1qIsolatedPortGroups':hpicfDot1qIsolatedPortGroups,_E:hpicfDot1qIsolatedPortGroup})