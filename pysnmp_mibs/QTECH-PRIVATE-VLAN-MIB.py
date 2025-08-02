_Z='qtechpvlanSVIGroup'
_Y='qtechpvlanPortModeGroup'
_X='qtechpvlanPromPortGroup'
_W='qtechpvlanPrivatePortGroup'
_V='qtechpvlanVlanGroup'
_U='qtechpvlanSVIMappingPrimarySVI'
_T='qtechpvlanPortMode'
_S='qtechpvlanPromPortSecondaryRemap4k'
_R='qtechpvlanPromPortSecondaryRemap3k'
_Q='qtechpvlanPromPortSecondaryRemap2k'
_P='qtechpvlanPromPortSecondaryRemap'
_O='qtechpvlanPrivatePortSecondaryVlan'
_N='qtechpvlanIfAssociatedPrimaryVlan'
_M='qtechpvlanVlanAssociatedPrimaryVlan'
_L='qtechpvlanVlanPrivateVlanType'
_K='qtechpvlanSVIMappingVlanIndex'
_J='Integer32'
_I='qtechpvlanPrivatePortPrimaryVlan'
_H='read-create'
_G='qtechpvlanVlanIndex'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-write'
_B='QTECH-PRIVATE-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
qtechPrivateVlanMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,44))
if mibBuilder.loadTexts:qtechPrivateVlanMIB.setRevisions(('2009-03-01 00:00',))
class PrivateVlanType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('primary',2),('isolated',3),('community',4)))
class VlanIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_QtechpvlanMIBObjects_ObjectIdentity=ObjectIdentity
qtechpvlanMIBObjects=_QtechpvlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,44,1))
_QtechpvlanVlanObjects_ObjectIdentity=ObjectIdentity
qtechpvlanVlanObjects=_QtechpvlanVlanObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,44,1,1))
_QtechpvlanVlanTable_Object=MibTable
qtechpvlanVlanTable=_QtechpvlanVlanTable_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,1,1))
if mibBuilder.loadTexts:qtechpvlanVlanTable.setStatus(_A)
_QtechpvlanVlanEntry_Object=MibTableRow
qtechpvlanVlanEntry=_QtechpvlanVlanEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,1,1,1))
qtechpvlanVlanEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:qtechpvlanVlanEntry.setStatus(_A)
_QtechpvlanVlanIndex_Type=VlanIndexOrZero
_QtechpvlanVlanIndex_Object=MibTableColumn
qtechpvlanVlanIndex=_QtechpvlanVlanIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,1,1,1,1),_QtechpvlanVlanIndex_Type())
qtechpvlanVlanIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:qtechpvlanVlanIndex.setStatus(_A)
_QtechpvlanVlanPrivateVlanType_Type=PrivateVlanType
_QtechpvlanVlanPrivateVlanType_Object=MibTableColumn
qtechpvlanVlanPrivateVlanType=_QtechpvlanVlanPrivateVlanType_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,1,1,1,2),_QtechpvlanVlanPrivateVlanType_Type())
qtechpvlanVlanPrivateVlanType.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechpvlanVlanPrivateVlanType.setStatus(_A)
_QtechpvlanVlanAssociatedPrimaryVlan_Type=VlanIndexOrZero
_QtechpvlanVlanAssociatedPrimaryVlan_Object=MibTableColumn
qtechpvlanVlanAssociatedPrimaryVlan=_QtechpvlanVlanAssociatedPrimaryVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,1,1,1,3),_QtechpvlanVlanAssociatedPrimaryVlan_Type())
qtechpvlanVlanAssociatedPrimaryVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechpvlanVlanAssociatedPrimaryVlan.setStatus(_A)
_QtechpvlanIfAssociatedPrimaryVlan_Type=TruthValue
_QtechpvlanIfAssociatedPrimaryVlan_Object=MibTableColumn
qtechpvlanIfAssociatedPrimaryVlan=_QtechpvlanIfAssociatedPrimaryVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,1,1,1,4),_QtechpvlanIfAssociatedPrimaryVlan_Type())
qtechpvlanIfAssociatedPrimaryVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechpvlanIfAssociatedPrimaryVlan.setStatus(_A)
_QtechpvlanPortObjects_ObjectIdentity=ObjectIdentity
qtechpvlanPortObjects=_QtechpvlanPortObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,44,1,2))
_QtechpvlanPrivatePortTable_Object=MibTable
qtechpvlanPrivatePortTable=_QtechpvlanPrivatePortTable_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,1))
if mibBuilder.loadTexts:qtechpvlanPrivatePortTable.setStatus(_A)
_QtechpvlanPrivatePortEntry_Object=MibTableRow
qtechpvlanPrivatePortEntry=_QtechpvlanPrivatePortEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,1,1))
qtechpvlanPrivatePortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qtechpvlanPrivatePortEntry.setStatus(_A)
_QtechpvlanPrivatePortPrimaryVlan_Type=VlanIndexOrZero
_QtechpvlanPrivatePortPrimaryVlan_Object=MibTableColumn
qtechpvlanPrivatePortPrimaryVlan=_QtechpvlanPrivatePortPrimaryVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,1,1,1),_QtechpvlanPrivatePortPrimaryVlan_Type())
qtechpvlanPrivatePortPrimaryVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechpvlanPrivatePortPrimaryVlan.setStatus(_A)
_QtechpvlanPrivatePortSecondaryVlan_Type=VlanIndexOrZero
_QtechpvlanPrivatePortSecondaryVlan_Object=MibTableColumn
qtechpvlanPrivatePortSecondaryVlan=_QtechpvlanPrivatePortSecondaryVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,1,1,2),_QtechpvlanPrivatePortSecondaryVlan_Type())
qtechpvlanPrivatePortSecondaryVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechpvlanPrivatePortSecondaryVlan.setStatus(_A)
_QtechpvlanPromPortTable_Object=MibTable
qtechpvlanPromPortTable=_QtechpvlanPromPortTable_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,2))
if mibBuilder.loadTexts:qtechpvlanPromPortTable.setStatus(_A)
_QtechpvlanPromPortEntry_Object=MibTableRow
qtechpvlanPromPortEntry=_QtechpvlanPromPortEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,2,1))
qtechpvlanPromPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qtechpvlanPromPortEntry.setStatus(_A)
_QtechpvlanPrivatePortPrimaryVlanId_Type=VlanIndexOrZero
_QtechpvlanPrivatePortPrimaryVlanId_Object=MibTableColumn
qtechpvlanPrivatePortPrimaryVlanId=_QtechpvlanPrivatePortPrimaryVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,2,1,1),_QtechpvlanPrivatePortPrimaryVlanId_Type())
qtechpvlanPrivatePortPrimaryVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechpvlanPrivatePortPrimaryVlanId.setStatus(_A)
class _QtechpvlanPromPortSecondaryRemap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_QtechpvlanPromPortSecondaryRemap_Type.__name__=_D
_QtechpvlanPromPortSecondaryRemap_Object=MibTableColumn
qtechpvlanPromPortSecondaryRemap=_QtechpvlanPromPortSecondaryRemap_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,2,1,2),_QtechpvlanPromPortSecondaryRemap_Type())
qtechpvlanPromPortSecondaryRemap.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechpvlanPromPortSecondaryRemap.setStatus(_A)
class _QtechpvlanPromPortSecondaryRemap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_QtechpvlanPromPortSecondaryRemap2k_Type.__name__=_D
_QtechpvlanPromPortSecondaryRemap2k_Object=MibTableColumn
qtechpvlanPromPortSecondaryRemap2k=_QtechpvlanPromPortSecondaryRemap2k_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,2,1,3),_QtechpvlanPromPortSecondaryRemap2k_Type())
qtechpvlanPromPortSecondaryRemap2k.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechpvlanPromPortSecondaryRemap2k.setStatus(_A)
class _QtechpvlanPromPortSecondaryRemap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_QtechpvlanPromPortSecondaryRemap3k_Type.__name__=_D
_QtechpvlanPromPortSecondaryRemap3k_Object=MibTableColumn
qtechpvlanPromPortSecondaryRemap3k=_QtechpvlanPromPortSecondaryRemap3k_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,2,1,4),_QtechpvlanPromPortSecondaryRemap3k_Type())
qtechpvlanPromPortSecondaryRemap3k.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechpvlanPromPortSecondaryRemap3k.setStatus(_A)
class _QtechpvlanPromPortSecondaryRemap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_QtechpvlanPromPortSecondaryRemap4k_Type.__name__=_D
_QtechpvlanPromPortSecondaryRemap4k_Object=MibTableColumn
qtechpvlanPromPortSecondaryRemap4k=_QtechpvlanPromPortSecondaryRemap4k_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,2,1,5),_QtechpvlanPromPortSecondaryRemap4k_Type())
qtechpvlanPromPortSecondaryRemap4k.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechpvlanPromPortSecondaryRemap4k.setStatus(_A)
_QtechpvlanPortModeTable_Object=MibTable
qtechpvlanPortModeTable=_QtechpvlanPortModeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,3))
if mibBuilder.loadTexts:qtechpvlanPortModeTable.setStatus(_A)
_QtechpvlanPortModeEntry_Object=MibTableRow
qtechpvlanPortModeEntry=_QtechpvlanPortModeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,3,1))
qtechpvlanPortModeEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qtechpvlanPortModeEntry.setStatus(_A)
class _QtechpvlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nonPrivateVlan',1),('host',2),('promiscuous',3)))
_QtechpvlanPortMode_Type.__name__=_J
_QtechpvlanPortMode_Object=MibTableColumn
qtechpvlanPortMode=_QtechpvlanPortMode_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,2,3,1,1),_QtechpvlanPortMode_Type())
qtechpvlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechpvlanPortMode.setStatus(_A)
_QtechpvlanSVIObjects_ObjectIdentity=ObjectIdentity
qtechpvlanSVIObjects=_QtechpvlanSVIObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,44,1,3))
_QtechpvlanSVIMappingTable_Object=MibTable
qtechpvlanSVIMappingTable=_QtechpvlanSVIMappingTable_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,3,1))
if mibBuilder.loadTexts:qtechpvlanSVIMappingTable.setStatus(_A)
_QtechpvlanSVIMappingEntry_Object=MibTableRow
qtechpvlanSVIMappingEntry=_QtechpvlanSVIMappingEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,3,1,1))
qtechpvlanSVIMappingEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechpvlanSVIMappingEntry.setStatus(_A)
_QtechpvlanSVIMappingVlanIndex_Type=VlanIndexOrZero
_QtechpvlanSVIMappingVlanIndex_Object=MibTableColumn
qtechpvlanSVIMappingVlanIndex=_QtechpvlanSVIMappingVlanIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,3,1,1,1),_QtechpvlanSVIMappingVlanIndex_Type())
qtechpvlanSVIMappingVlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechpvlanSVIMappingVlanIndex.setStatus(_A)
_QtechpvlanSVIMappingPrimarySVI_Type=VlanIndexOrZero
_QtechpvlanSVIMappingPrimarySVI_Object=MibTableColumn
qtechpvlanSVIMappingPrimarySVI=_QtechpvlanSVIMappingPrimarySVI_Object((1,3,6,1,4,1,27514,1,1,10,2,44,1,3,1,1,2),_QtechpvlanSVIMappingPrimarySVI_Type())
qtechpvlanSVIMappingPrimarySVI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechpvlanSVIMappingPrimarySVI.setStatus(_A)
_QtechpvlanMIBConformance_ObjectIdentity=ObjectIdentity
qtechpvlanMIBConformance=_QtechpvlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,44,2))
_QtechpvlanMIBCompliances_ObjectIdentity=ObjectIdentity
qtechpvlanMIBCompliances=_QtechpvlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,44,2,1))
_QtechpvlanMIBGroups_ObjectIdentity=ObjectIdentity
qtechpvlanMIBGroups=_QtechpvlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,44,2,2))
qtechpvlanVlanGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,44,2,2,1))
qtechpvlanVlanGroup.setObjects(*((_B,_G),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:qtechpvlanVlanGroup.setStatus(_A)
qtechpvlanPrivatePortGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,44,2,2,2))
qtechpvlanPrivatePortGroup.setObjects(*((_B,_I),(_B,_O)))
if mibBuilder.loadTexts:qtechpvlanPrivatePortGroup.setStatus(_A)
qtechpvlanPromPortGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,44,2,2,3))
qtechpvlanPromPortGroup.setObjects(*((_B,_I),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:qtechpvlanPromPortGroup.setStatus(_A)
qtechpvlanPortModeGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,44,2,2,4))
qtechpvlanPortModeGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:qtechpvlanPortModeGroup.setStatus(_A)
qtechpvlanSVIGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,44,2,2,5))
qtechpvlanSVIGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:qtechpvlanSVIGroup.setStatus(_A)
qtechpvlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,44,2,1,1))
qtechpvlanMIBCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:qtechpvlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PrivateVlanType':PrivateVlanType,'VlanIndexOrZero':VlanIndexOrZero,'qtechPrivateVlanMIB':qtechPrivateVlanMIB,'qtechpvlanMIBObjects':qtechpvlanMIBObjects,'qtechpvlanVlanObjects':qtechpvlanVlanObjects,'qtechpvlanVlanTable':qtechpvlanVlanTable,'qtechpvlanVlanEntry':qtechpvlanVlanEntry,_G:qtechpvlanVlanIndex,_L:qtechpvlanVlanPrivateVlanType,_M:qtechpvlanVlanAssociatedPrimaryVlan,_N:qtechpvlanIfAssociatedPrimaryVlan,'qtechpvlanPortObjects':qtechpvlanPortObjects,'qtechpvlanPrivatePortTable':qtechpvlanPrivatePortTable,'qtechpvlanPrivatePortEntry':qtechpvlanPrivatePortEntry,_I:qtechpvlanPrivatePortPrimaryVlan,_O:qtechpvlanPrivatePortSecondaryVlan,'qtechpvlanPromPortTable':qtechpvlanPromPortTable,'qtechpvlanPromPortEntry':qtechpvlanPromPortEntry,'qtechpvlanPrivatePortPrimaryVlanId':qtechpvlanPrivatePortPrimaryVlanId,_P:qtechpvlanPromPortSecondaryRemap,_Q:qtechpvlanPromPortSecondaryRemap2k,_R:qtechpvlanPromPortSecondaryRemap3k,_S:qtechpvlanPromPortSecondaryRemap4k,'qtechpvlanPortModeTable':qtechpvlanPortModeTable,'qtechpvlanPortModeEntry':qtechpvlanPortModeEntry,_T:qtechpvlanPortMode,'qtechpvlanSVIObjects':qtechpvlanSVIObjects,'qtechpvlanSVIMappingTable':qtechpvlanSVIMappingTable,'qtechpvlanSVIMappingEntry':qtechpvlanSVIMappingEntry,_K:qtechpvlanSVIMappingVlanIndex,_U:qtechpvlanSVIMappingPrimarySVI,'qtechpvlanMIBConformance':qtechpvlanMIBConformance,'qtechpvlanMIBCompliances':qtechpvlanMIBCompliances,'qtechpvlanMIBCompliance':qtechpvlanMIBCompliance,'qtechpvlanMIBGroups':qtechpvlanMIBGroups,_V:qtechpvlanVlanGroup,_W:qtechpvlanPrivatePortGroup,_X:qtechpvlanPromPortGroup,_Y:qtechpvlanPortModeGroup,_Z:qtechpvlanSVIGroup})