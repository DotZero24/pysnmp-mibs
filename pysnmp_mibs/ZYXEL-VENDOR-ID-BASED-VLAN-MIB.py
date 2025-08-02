_G='not-accessible'
_F='zyVendorIdBasedVlanBindingMask'
_E='zyVendorIdBasedVlanBindingSourceMac'
_D='ZYXEL-VENDOR-ID-BASED-VLAN-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelVendorIdBasedVlan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,120))
_ZyxelVendorIdBasedVlanSetup_ObjectIdentity=ObjectIdentity
zyxelVendorIdBasedVlanSetup=_ZyxelVendorIdBasedVlanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,120,1))
_ZyVendorIdBasedVlanMaxNumberOfVlans_Type=Integer32
_ZyVendorIdBasedVlanMaxNumberOfVlans_Object=MibScalar
zyVendorIdBasedVlanMaxNumberOfVlans=_ZyVendorIdBasedVlanMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,120,1,1),_ZyVendorIdBasedVlanMaxNumberOfVlans_Type())
zyVendorIdBasedVlanMaxNumberOfVlans.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyVendorIdBasedVlanMaxNumberOfVlans.setStatus(_A)
_ZyxelVendorIdBasedVlanBindingTable_Object=MibTable
zyxelVendorIdBasedVlanBindingTable=_ZyxelVendorIdBasedVlanBindingTable_Object((1,3,6,1,4,1,890,1,15,3,120,1,2))
if mibBuilder.loadTexts:zyxelVendorIdBasedVlanBindingTable.setStatus(_A)
_ZyxelVendorIdBasedVlanBindingEntry_Object=MibTableRow
zyxelVendorIdBasedVlanBindingEntry=_ZyxelVendorIdBasedVlanBindingEntry_Object((1,3,6,1,4,1,890,1,15,3,120,1,2,1))
zyxelVendorIdBasedVlanBindingEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:zyxelVendorIdBasedVlanBindingEntry.setStatus(_A)
_ZyVendorIdBasedVlanBindingSourceMac_Type=MacAddress
_ZyVendorIdBasedVlanBindingSourceMac_Object=MibTableColumn
zyVendorIdBasedVlanBindingSourceMac=_ZyVendorIdBasedVlanBindingSourceMac_Object((1,3,6,1,4,1,890,1,15,3,120,1,2,1,1),_ZyVendorIdBasedVlanBindingSourceMac_Type())
zyVendorIdBasedVlanBindingSourceMac.setMaxAccess(_G)
if mibBuilder.loadTexts:zyVendorIdBasedVlanBindingSourceMac.setStatus(_A)
_ZyVendorIdBasedVlanBindingMask_Type=MacAddress
_ZyVendorIdBasedVlanBindingMask_Object=MibTableColumn
zyVendorIdBasedVlanBindingMask=_ZyVendorIdBasedVlanBindingMask_Object((1,3,6,1,4,1,890,1,15,3,120,1,2,1,2),_ZyVendorIdBasedVlanBindingMask_Type())
zyVendorIdBasedVlanBindingMask.setMaxAccess(_G)
if mibBuilder.loadTexts:zyVendorIdBasedVlanBindingMask.setStatus(_A)
_ZyVendorIdBasedVlanBindingName_Type=OctetString
_ZyVendorIdBasedVlanBindingName_Object=MibTableColumn
zyVendorIdBasedVlanBindingName=_ZyVendorIdBasedVlanBindingName_Object((1,3,6,1,4,1,890,1,15,3,120,1,2,1,3),_ZyVendorIdBasedVlanBindingName_Type())
zyVendorIdBasedVlanBindingName.setMaxAccess(_C)
if mibBuilder.loadTexts:zyVendorIdBasedVlanBindingName.setStatus(_A)
class _ZyVendorIdBasedVlanBindingVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyVendorIdBasedVlanBindingVlan_Type.__name__=_B
_ZyVendorIdBasedVlanBindingVlan_Object=MibTableColumn
zyVendorIdBasedVlanBindingVlan=_ZyVendorIdBasedVlanBindingVlan_Object((1,3,6,1,4,1,890,1,15,3,120,1,2,1,4),_ZyVendorIdBasedVlanBindingVlan_Type())
zyVendorIdBasedVlanBindingVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zyVendorIdBasedVlanBindingVlan.setStatus(_A)
class _ZyVendorIdBasedVlanBindingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZyVendorIdBasedVlanBindingPriority_Type.__name__=_B
_ZyVendorIdBasedVlanBindingPriority_Object=MibTableColumn
zyVendorIdBasedVlanBindingPriority=_ZyVendorIdBasedVlanBindingPriority_Object((1,3,6,1,4,1,890,1,15,3,120,1,2,1,5),_ZyVendorIdBasedVlanBindingPriority_Type())
zyVendorIdBasedVlanBindingPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zyVendorIdBasedVlanBindingPriority.setStatus(_A)
class _ZyVendorIdBasedVlanBindingWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZyVendorIdBasedVlanBindingWeight_Type.__name__=_B
_ZyVendorIdBasedVlanBindingWeight_Object=MibTableColumn
zyVendorIdBasedVlanBindingWeight=_ZyVendorIdBasedVlanBindingWeight_Object((1,3,6,1,4,1,890,1,15,3,120,1,2,1,6),_ZyVendorIdBasedVlanBindingWeight_Type())
zyVendorIdBasedVlanBindingWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zyVendorIdBasedVlanBindingWeight.setStatus(_A)
_ZyVendorIdBasedVlanBindingRowStatus_Type=RowStatus
_ZyVendorIdBasedVlanBindingRowStatus_Object=MibTableColumn
zyVendorIdBasedVlanBindingRowStatus=_ZyVendorIdBasedVlanBindingRowStatus_Object((1,3,6,1,4,1,890,1,15,3,120,1,2,1,7),_ZyVendorIdBasedVlanBindingRowStatus_Type())
zyVendorIdBasedVlanBindingRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyVendorIdBasedVlanBindingRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelVendorIdBasedVlan':zyxelVendorIdBasedVlan,'zyxelVendorIdBasedVlanSetup':zyxelVendorIdBasedVlanSetup,'zyVendorIdBasedVlanMaxNumberOfVlans':zyVendorIdBasedVlanMaxNumberOfVlans,'zyxelVendorIdBasedVlanBindingTable':zyxelVendorIdBasedVlanBindingTable,'zyxelVendorIdBasedVlanBindingEntry':zyxelVendorIdBasedVlanBindingEntry,_E:zyVendorIdBasedVlanBindingSourceMac,_F:zyVendorIdBasedVlanBindingMask,'zyVendorIdBasedVlanBindingName':zyVendorIdBasedVlanBindingName,'zyVendorIdBasedVlanBindingVlan':zyVendorIdBasedVlanBindingVlan,'zyVendorIdBasedVlanBindingPriority':zyVendorIdBasedVlanBindingPriority,'zyVendorIdBasedVlanBindingWeight':zyVendorIdBasedVlanBindingWeight,'zyVendorIdBasedVlanBindingRowStatus':zyVendorIdBasedVlanBindingRowStatus})