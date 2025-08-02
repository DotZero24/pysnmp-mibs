_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelVlanTrunk=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,90))
_ZyxelVlanTrunkSetup_ObjectIdentity=ObjectIdentity
zyxelVlanTrunkSetup=_ZyxelVlanTrunkSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,90,1))
_ZyxelVlanTrunkPortTable_Object=MibTable
zyxelVlanTrunkPortTable=_ZyxelVlanTrunkPortTable_Object((1,3,6,1,4,1,890,1,15,3,90,1,1))
if mibBuilder.loadTexts:zyxelVlanTrunkPortTable.setStatus(_A)
_ZyxelVlanTrunkPortEntry_Object=MibTableRow
zyxelVlanTrunkPortEntry=_ZyxelVlanTrunkPortEntry_Object((1,3,6,1,4,1,890,1,15,3,90,1,1,1))
zyxelVlanTrunkPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelVlanTrunkPortEntry.setStatus(_A)
_ZyVlanTrunkPortState_Type=EnabledStatus
_ZyVlanTrunkPortState_Object=MibTableColumn
zyVlanTrunkPortState=_ZyVlanTrunkPortState_Object((1,3,6,1,4,1,890,1,15,3,90,1,1,1,1),_ZyVlanTrunkPortState_Type())
zyVlanTrunkPortState.setMaxAccess('read-write')
if mibBuilder.loadTexts:zyVlanTrunkPortState.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-VLAN-TRUNK-MIB',**{'zyxelVlanTrunk':zyxelVlanTrunk,'zyxelVlanTrunkSetup':zyxelVlanTrunkSetup,'zyxelVlanTrunkPortTable':zyxelVlanTrunkPortTable,'zyxelVlanTrunkPortEntry':zyxelVlanTrunkPortEntry,'zyVlanTrunkPortState':zyVlanTrunkPortState})