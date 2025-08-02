_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelPortBasedVlan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,63))
_ZyxelPortBasedVlanSetup_ObjectIdentity=ObjectIdentity
zyxelPortBasedVlanSetup=_ZyxelPortBasedVlanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,63,1))
_ZyxelPortBasedVlanTable_Object=MibTable
zyxelPortBasedVlanTable=_ZyxelPortBasedVlanTable_Object((1,3,6,1,4,1,890,1,15,3,63,1,1))
if mibBuilder.loadTexts:zyxelPortBasedVlanTable.setStatus(_A)
_ZyxelPortBasedVlanEntry_Object=MibTableRow
zyxelPortBasedVlanEntry=_ZyxelPortBasedVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,63,1,1,1))
zyxelPortBasedVlanEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelPortBasedVlanEntry.setStatus(_A)
_ZyPortBasedVlanPorts_Type=PortList
_ZyPortBasedVlanPorts_Object=MibTableColumn
zyPortBasedVlanPorts=_ZyPortBasedVlanPorts_Object((1,3,6,1,4,1,890,1,15,3,63,1,1,1,1),_ZyPortBasedVlanPorts_Type())
zyPortBasedVlanPorts.setMaxAccess('read-write')
if mibBuilder.loadTexts:zyPortBasedVlanPorts.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-PORT-BASED-VLAN-MIB',**{'zyxelPortBasedVlan':zyxelPortBasedVlan,'zyxelPortBasedVlanSetup':zyxelPortBasedVlanSetup,'zyxelPortBasedVlanTable':zyxelPortBasedVlanTable,'zyxelPortBasedVlanEntry':zyxelPortBasedVlanEntry,'zyPortBasedVlanPorts':zyPortBasedVlanPorts})