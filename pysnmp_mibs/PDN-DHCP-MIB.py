_F='pdnDhcpVlanConfigOpt82Group'
_E='pdnDhcpVlanConfigOption82'
_D='pdnDhcpVlanConfigEntry'
_C='SwitchState'
_B='PDN-DHCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
SwitchState,=mibBuilder.importSymbols('PDN-TC',_C)
dot1qVlanStaticEntry,=mibBuilder.importSymbols('Q-BRIDGE-MIB','dot1qVlanStaticEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnDhcpMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,57))
if mibBuilder.loadTexts:pdnDhcpMIB.setRevisions(('2004-09-14 00:00',))
_PdnDhcpNotifications_ObjectIdentity=ObjectIdentity
pdnDhcpNotifications=_PdnDhcpNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,57,0))
_PdnDhcpObjects_ObjectIdentity=ObjectIdentity
pdnDhcpObjects=_PdnDhcpObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,57,1))
_PdnDhcpVlanConfigTable_Object=MibTable
pdnDhcpVlanConfigTable=_PdnDhcpVlanConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,57,1,1))
if mibBuilder.loadTexts:pdnDhcpVlanConfigTable.setStatus(_A)
_PdnDhcpVlanConfigEntry_Object=MibTableRow
pdnDhcpVlanConfigEntry=_PdnDhcpVlanConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,57,1,1,1))
if mibBuilder.loadTexts:pdnDhcpVlanConfigEntry.setStatus(_A)
class _PdnDhcpVlanConfigOption82_Type(SwitchState):defaultValue=2
_PdnDhcpVlanConfigOption82_Type.__name__=_C
_PdnDhcpVlanConfigOption82_Object=MibTableColumn
pdnDhcpVlanConfigOption82=_PdnDhcpVlanConfigOption82_Object((1,3,6,1,4,1,1795,2,24,2,57,1,1,1,1),_PdnDhcpVlanConfigOption82_Type())
pdnDhcpVlanConfigOption82.setMaxAccess('read-create')
if mibBuilder.loadTexts:pdnDhcpVlanConfigOption82.setStatus(_A)
_PdnDhcpAFNs_ObjectIdentity=ObjectIdentity
pdnDhcpAFNs=_PdnDhcpAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,57,2))
_PdnDhcpConformance_ObjectIdentity=ObjectIdentity
pdnDhcpConformance=_PdnDhcpConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,57,3))
_PdnDhcpCompliances_ObjectIdentity=ObjectIdentity
pdnDhcpCompliances=_PdnDhcpCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,57,3,1))
_PdnDhcpGroups_ObjectIdentity=ObjectIdentity
pdnDhcpGroups=_PdnDhcpGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,57,3,2))
_PdnDhcpObjGroups_ObjectIdentity=ObjectIdentity
pdnDhcpObjGroups=_PdnDhcpObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,57,3,2,1))
_PdnDhcpAfnGroups_ObjectIdentity=ObjectIdentity
pdnDhcpAfnGroups=_PdnDhcpAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,57,3,2,2))
_PdnDhcpNtfyGroups_ObjectIdentity=ObjectIdentity
pdnDhcpNtfyGroups=_PdnDhcpNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,57,3,2,3))
dot1qVlanStaticEntry.registerAugmentions((_B,_D))
pdnDhcpVlanConfigEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
pdnDhcpVlanConfigOpt82Group=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,57,3,2,1,2))
pdnDhcpVlanConfigOpt82Group.setObjects((_B,_E))
if mibBuilder.loadTexts:pdnDhcpVlanConfigOpt82Group.setStatus(_A)
pdnDhcpCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,57,3,1,1))
pdnDhcpCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:pdnDhcpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnDhcpMIB':pdnDhcpMIB,'pdnDhcpNotifications':pdnDhcpNotifications,'pdnDhcpObjects':pdnDhcpObjects,'pdnDhcpVlanConfigTable':pdnDhcpVlanConfigTable,_D:pdnDhcpVlanConfigEntry,_E:pdnDhcpVlanConfigOption82,'pdnDhcpAFNs':pdnDhcpAFNs,'pdnDhcpConformance':pdnDhcpConformance,'pdnDhcpCompliances':pdnDhcpCompliances,'pdnDhcpCompliance':pdnDhcpCompliance,'pdnDhcpGroups':pdnDhcpGroups,'pdnDhcpObjGroups':pdnDhcpObjGroups,_F:pdnDhcpVlanConfigOpt82Group,'pdnDhcpAfnGroups':pdnDhcpAfnGroups,'pdnDhcpNtfyGroups':pdnDhcpNtfyGroups})