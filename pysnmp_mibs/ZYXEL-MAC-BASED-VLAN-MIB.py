_E='zyMacBasedVlanBindingSourceMac'
_D='ZYXEL-MAC-BASED-VLAN-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelMacBasedVlan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,99))
_ZyxelMacBasedVlanSetup_ObjectIdentity=ObjectIdentity
zyxelMacBasedVlanSetup=_ZyxelMacBasedVlanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,99,1))
_ZyMacBasedVlanMaxNumberOfVlans_Type=Integer32
_ZyMacBasedVlanMaxNumberOfVlans_Object=MibScalar
zyMacBasedVlanMaxNumberOfVlans=_ZyMacBasedVlanMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,99,1,1),_ZyMacBasedVlanMaxNumberOfVlans_Type())
zyMacBasedVlanMaxNumberOfVlans.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyMacBasedVlanMaxNumberOfVlans.setStatus(_A)
_ZyxelMacBasedVlanBindingTable_Object=MibTable
zyxelMacBasedVlanBindingTable=_ZyxelMacBasedVlanBindingTable_Object((1,3,6,1,4,1,890,1,15,3,99,1,2))
if mibBuilder.loadTexts:zyxelMacBasedVlanBindingTable.setStatus(_A)
_ZyxelMacBasedVlanBindingEntry_Object=MibTableRow
zyxelMacBasedVlanBindingEntry=_ZyxelMacBasedVlanBindingEntry_Object((1,3,6,1,4,1,890,1,15,3,99,1,2,1))
zyxelMacBasedVlanBindingEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelMacBasedVlanBindingEntry.setStatus(_A)
_ZyMacBasedVlanBindingSourceMac_Type=MacAddress
_ZyMacBasedVlanBindingSourceMac_Object=MibTableColumn
zyMacBasedVlanBindingSourceMac=_ZyMacBasedVlanBindingSourceMac_Object((1,3,6,1,4,1,890,1,15,3,99,1,2,1,1),_ZyMacBasedVlanBindingSourceMac_Type())
zyMacBasedVlanBindingSourceMac.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyMacBasedVlanBindingSourceMac.setStatus(_A)
_ZyMacBasedVlanBindingName_Type=OctetString
_ZyMacBasedVlanBindingName_Object=MibTableColumn
zyMacBasedVlanBindingName=_ZyMacBasedVlanBindingName_Object((1,3,6,1,4,1,890,1,15,3,99,1,2,1,2),_ZyMacBasedVlanBindingName_Type())
zyMacBasedVlanBindingName.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMacBasedVlanBindingName.setStatus(_A)
class _ZyMacBasedVlanBindingVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyMacBasedVlanBindingVlan_Type.__name__=_B
_ZyMacBasedVlanBindingVlan_Object=MibTableColumn
zyMacBasedVlanBindingVlan=_ZyMacBasedVlanBindingVlan_Object((1,3,6,1,4,1,890,1,15,3,99,1,2,1,3),_ZyMacBasedVlanBindingVlan_Type())
zyMacBasedVlanBindingVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMacBasedVlanBindingVlan.setStatus(_A)
class _ZyMacBasedVlanBindingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZyMacBasedVlanBindingPriority_Type.__name__=_B
_ZyMacBasedVlanBindingPriority_Object=MibTableColumn
zyMacBasedVlanBindingPriority=_ZyMacBasedVlanBindingPriority_Object((1,3,6,1,4,1,890,1,15,3,99,1,2,1,4),_ZyMacBasedVlanBindingPriority_Type())
zyMacBasedVlanBindingPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMacBasedVlanBindingPriority.setStatus(_A)
_ZyMacBasedVlanBindingRowStatus_Type=RowStatus
_ZyMacBasedVlanBindingRowStatus_Object=MibTableColumn
zyMacBasedVlanBindingRowStatus=_ZyMacBasedVlanBindingRowStatus_Object((1,3,6,1,4,1,890,1,15,3,99,1,2,1,5),_ZyMacBasedVlanBindingRowStatus_Type())
zyMacBasedVlanBindingRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyMacBasedVlanBindingRowStatus.setStatus(_A)
_ZyxelMacBasedVlanStatus_ObjectIdentity=ObjectIdentity
zyxelMacBasedVlanStatus=_ZyxelMacBasedVlanStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,99,2))
mibBuilder.exportSymbols(_D,**{'zyxelMacBasedVlan':zyxelMacBasedVlan,'zyxelMacBasedVlanSetup':zyxelMacBasedVlanSetup,'zyMacBasedVlanMaxNumberOfVlans':zyMacBasedVlanMaxNumberOfVlans,'zyxelMacBasedVlanBindingTable':zyxelMacBasedVlanBindingTable,'zyxelMacBasedVlanBindingEntry':zyxelMacBasedVlanBindingEntry,_E:zyMacBasedVlanBindingSourceMac,'zyMacBasedVlanBindingName':zyMacBasedVlanBindingName,'zyMacBasedVlanBindingVlan':zyMacBasedVlanBindingVlan,'zyMacBasedVlanBindingPriority':zyMacBasedVlanBindingPriority,'zyMacBasedVlanBindingRowStatus':zyMacBasedVlanBindingRowStatus,'zyxelMacBasedVlanStatus':zyxelMacBasedVlanStatus})