_Z='fspvlanSVIGroup'
_Y='fspvlanPortModeGroup'
_X='fspvlanPromPortGroup'
_W='fspvlanPrivatePortGroup'
_V='fspvlanVlanGroup'
_U='fspvlanSVIMappingPrimarySVI'
_T='fspvlanPortMode'
_S='fspvlanPromPortSecondaryRemap4k'
_R='fspvlanPromPortSecondaryRemap3k'
_Q='fspvlanPromPortSecondaryRemap2k'
_P='fspvlanPromPortSecondaryRemap'
_O='fspvlanPrivatePortSecondaryVlan'
_N='fspvlanIfAssociatedPrimaryVlan'
_M='fspvlanVlanAssociatedPrimaryVlan'
_L='fspvlanVlanPrivateVlanType'
_K='fspvlanSVIMappingVlanIndex'
_J='Integer32'
_I='fspvlanPrivatePortPrimaryVlan'
_H='read-create'
_G='fspvlanVlanIndex'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-write'
_B='FS-PRIVATE-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fsPrivateVlanMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,44))
if mibBuilder.loadTexts:fsPrivateVlanMIB.setRevisions(('2009-03-01 00:00',))
class PrivateVlanType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('primary',2),('isolated',3),('community',4)))
class VlanIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_FspvlanMIBObjects_ObjectIdentity=ObjectIdentity
fspvlanMIBObjects=_FspvlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,44,1))
_FspvlanVlanObjects_ObjectIdentity=ObjectIdentity
fspvlanVlanObjects=_FspvlanVlanObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,44,1,1))
_FspvlanVlanTable_Object=MibTable
fspvlanVlanTable=_FspvlanVlanTable_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,1,1))
if mibBuilder.loadTexts:fspvlanVlanTable.setStatus(_A)
_FspvlanVlanEntry_Object=MibTableRow
fspvlanVlanEntry=_FspvlanVlanEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,1,1,1))
fspvlanVlanEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fspvlanVlanEntry.setStatus(_A)
_FspvlanVlanIndex_Type=VlanIndexOrZero
_FspvlanVlanIndex_Object=MibTableColumn
fspvlanVlanIndex=_FspvlanVlanIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,1,1,1,1),_FspvlanVlanIndex_Type())
fspvlanVlanIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:fspvlanVlanIndex.setStatus(_A)
_FspvlanVlanPrivateVlanType_Type=PrivateVlanType
_FspvlanVlanPrivateVlanType_Object=MibTableColumn
fspvlanVlanPrivateVlanType=_FspvlanVlanPrivateVlanType_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,1,1,1,2),_FspvlanVlanPrivateVlanType_Type())
fspvlanVlanPrivateVlanType.setMaxAccess(_H)
if mibBuilder.loadTexts:fspvlanVlanPrivateVlanType.setStatus(_A)
_FspvlanVlanAssociatedPrimaryVlan_Type=VlanIndexOrZero
_FspvlanVlanAssociatedPrimaryVlan_Object=MibTableColumn
fspvlanVlanAssociatedPrimaryVlan=_FspvlanVlanAssociatedPrimaryVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,1,1,1,3),_FspvlanVlanAssociatedPrimaryVlan_Type())
fspvlanVlanAssociatedPrimaryVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:fspvlanVlanAssociatedPrimaryVlan.setStatus(_A)
_FspvlanIfAssociatedPrimaryVlan_Type=TruthValue
_FspvlanIfAssociatedPrimaryVlan_Object=MibTableColumn
fspvlanIfAssociatedPrimaryVlan=_FspvlanIfAssociatedPrimaryVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,1,1,1,4),_FspvlanIfAssociatedPrimaryVlan_Type())
fspvlanIfAssociatedPrimaryVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:fspvlanIfAssociatedPrimaryVlan.setStatus(_A)
_FspvlanPortObjects_ObjectIdentity=ObjectIdentity
fspvlanPortObjects=_FspvlanPortObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,44,1,2))
_FspvlanPrivatePortTable_Object=MibTable
fspvlanPrivatePortTable=_FspvlanPrivatePortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,1))
if mibBuilder.loadTexts:fspvlanPrivatePortTable.setStatus(_A)
_FspvlanPrivatePortEntry_Object=MibTableRow
fspvlanPrivatePortEntry=_FspvlanPrivatePortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,1,1))
fspvlanPrivatePortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fspvlanPrivatePortEntry.setStatus(_A)
_FspvlanPrivatePortPrimaryVlan_Type=VlanIndexOrZero
_FspvlanPrivatePortPrimaryVlan_Object=MibTableColumn
fspvlanPrivatePortPrimaryVlan=_FspvlanPrivatePortPrimaryVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,1,1,1),_FspvlanPrivatePortPrimaryVlan_Type())
fspvlanPrivatePortPrimaryVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:fspvlanPrivatePortPrimaryVlan.setStatus(_A)
_FspvlanPrivatePortSecondaryVlan_Type=VlanIndexOrZero
_FspvlanPrivatePortSecondaryVlan_Object=MibTableColumn
fspvlanPrivatePortSecondaryVlan=_FspvlanPrivatePortSecondaryVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,1,1,2),_FspvlanPrivatePortSecondaryVlan_Type())
fspvlanPrivatePortSecondaryVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:fspvlanPrivatePortSecondaryVlan.setStatus(_A)
_FspvlanPromPortTable_Object=MibTable
fspvlanPromPortTable=_FspvlanPromPortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,2))
if mibBuilder.loadTexts:fspvlanPromPortTable.setStatus(_A)
_FspvlanPromPortEntry_Object=MibTableRow
fspvlanPromPortEntry=_FspvlanPromPortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,2,1))
fspvlanPromPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fspvlanPromPortEntry.setStatus(_A)
_FspvlanPrivatePortPrimaryVlanId_Type=VlanIndexOrZero
_FspvlanPrivatePortPrimaryVlanId_Object=MibTableColumn
fspvlanPrivatePortPrimaryVlanId=_FspvlanPrivatePortPrimaryVlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,2,1,1),_FspvlanPrivatePortPrimaryVlanId_Type())
fspvlanPrivatePortPrimaryVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:fspvlanPrivatePortPrimaryVlanId.setStatus(_A)
class _FspvlanPromPortSecondaryRemap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FspvlanPromPortSecondaryRemap_Type.__name__=_D
_FspvlanPromPortSecondaryRemap_Object=MibTableColumn
fspvlanPromPortSecondaryRemap=_FspvlanPromPortSecondaryRemap_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,2,1,2),_FspvlanPromPortSecondaryRemap_Type())
fspvlanPromPortSecondaryRemap.setMaxAccess(_C)
if mibBuilder.loadTexts:fspvlanPromPortSecondaryRemap.setStatus(_A)
class _FspvlanPromPortSecondaryRemap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FspvlanPromPortSecondaryRemap2k_Type.__name__=_D
_FspvlanPromPortSecondaryRemap2k_Object=MibTableColumn
fspvlanPromPortSecondaryRemap2k=_FspvlanPromPortSecondaryRemap2k_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,2,1,3),_FspvlanPromPortSecondaryRemap2k_Type())
fspvlanPromPortSecondaryRemap2k.setMaxAccess(_C)
if mibBuilder.loadTexts:fspvlanPromPortSecondaryRemap2k.setStatus(_A)
class _FspvlanPromPortSecondaryRemap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FspvlanPromPortSecondaryRemap3k_Type.__name__=_D
_FspvlanPromPortSecondaryRemap3k_Object=MibTableColumn
fspvlanPromPortSecondaryRemap3k=_FspvlanPromPortSecondaryRemap3k_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,2,1,4),_FspvlanPromPortSecondaryRemap3k_Type())
fspvlanPromPortSecondaryRemap3k.setMaxAccess(_C)
if mibBuilder.loadTexts:fspvlanPromPortSecondaryRemap3k.setStatus(_A)
class _FspvlanPromPortSecondaryRemap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FspvlanPromPortSecondaryRemap4k_Type.__name__=_D
_FspvlanPromPortSecondaryRemap4k_Object=MibTableColumn
fspvlanPromPortSecondaryRemap4k=_FspvlanPromPortSecondaryRemap4k_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,2,1,5),_FspvlanPromPortSecondaryRemap4k_Type())
fspvlanPromPortSecondaryRemap4k.setMaxAccess(_C)
if mibBuilder.loadTexts:fspvlanPromPortSecondaryRemap4k.setStatus(_A)
_FspvlanPortModeTable_Object=MibTable
fspvlanPortModeTable=_FspvlanPortModeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,3))
if mibBuilder.loadTexts:fspvlanPortModeTable.setStatus(_A)
_FspvlanPortModeEntry_Object=MibTableRow
fspvlanPortModeEntry=_FspvlanPortModeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,3,1))
fspvlanPortModeEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fspvlanPortModeEntry.setStatus(_A)
class _FspvlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nonPrivateVlan',1),('host',2),('promiscuous',3)))
_FspvlanPortMode_Type.__name__=_J
_FspvlanPortMode_Object=MibTableColumn
fspvlanPortMode=_FspvlanPortMode_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,2,3,1,1),_FspvlanPortMode_Type())
fspvlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fspvlanPortMode.setStatus(_A)
_FspvlanSVIObjects_ObjectIdentity=ObjectIdentity
fspvlanSVIObjects=_FspvlanSVIObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,44,1,3))
_FspvlanSVIMappingTable_Object=MibTable
fspvlanSVIMappingTable=_FspvlanSVIMappingTable_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,3,1))
if mibBuilder.loadTexts:fspvlanSVIMappingTable.setStatus(_A)
_FspvlanSVIMappingEntry_Object=MibTableRow
fspvlanSVIMappingEntry=_FspvlanSVIMappingEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,3,1,1))
fspvlanSVIMappingEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fspvlanSVIMappingEntry.setStatus(_A)
_FspvlanSVIMappingVlanIndex_Type=VlanIndexOrZero
_FspvlanSVIMappingVlanIndex_Object=MibTableColumn
fspvlanSVIMappingVlanIndex=_FspvlanSVIMappingVlanIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,3,1,1,1),_FspvlanSVIMappingVlanIndex_Type())
fspvlanSVIMappingVlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fspvlanSVIMappingVlanIndex.setStatus(_A)
_FspvlanSVIMappingPrimarySVI_Type=VlanIndexOrZero
_FspvlanSVIMappingPrimarySVI_Object=MibTableColumn
fspvlanSVIMappingPrimarySVI=_FspvlanSVIMappingPrimarySVI_Object((1,3,6,1,4,1,52642,1,1,10,2,44,1,3,1,1,2),_FspvlanSVIMappingPrimarySVI_Type())
fspvlanSVIMappingPrimarySVI.setMaxAccess(_C)
if mibBuilder.loadTexts:fspvlanSVIMappingPrimarySVI.setStatus(_A)
_FspvlanMIBConformance_ObjectIdentity=ObjectIdentity
fspvlanMIBConformance=_FspvlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,44,2))
_FspvlanMIBCompliances_ObjectIdentity=ObjectIdentity
fspvlanMIBCompliances=_FspvlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,44,2,1))
_FspvlanMIBGroups_ObjectIdentity=ObjectIdentity
fspvlanMIBGroups=_FspvlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,44,2,2))
fspvlanVlanGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,44,2,2,1))
fspvlanVlanGroup.setObjects(*((_B,_G),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:fspvlanVlanGroup.setStatus(_A)
fspvlanPrivatePortGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,44,2,2,2))
fspvlanPrivatePortGroup.setObjects(*((_B,_I),(_B,_O)))
if mibBuilder.loadTexts:fspvlanPrivatePortGroup.setStatus(_A)
fspvlanPromPortGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,44,2,2,3))
fspvlanPromPortGroup.setObjects(*((_B,_I),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:fspvlanPromPortGroup.setStatus(_A)
fspvlanPortModeGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,44,2,2,4))
fspvlanPortModeGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:fspvlanPortModeGroup.setStatus(_A)
fspvlanSVIGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,44,2,2,5))
fspvlanSVIGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:fspvlanSVIGroup.setStatus(_A)
fspvlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,44,2,1,1))
fspvlanMIBCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:fspvlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PrivateVlanType':PrivateVlanType,'VlanIndexOrZero':VlanIndexOrZero,'fsPrivateVlanMIB':fsPrivateVlanMIB,'fspvlanMIBObjects':fspvlanMIBObjects,'fspvlanVlanObjects':fspvlanVlanObjects,'fspvlanVlanTable':fspvlanVlanTable,'fspvlanVlanEntry':fspvlanVlanEntry,_G:fspvlanVlanIndex,_L:fspvlanVlanPrivateVlanType,_M:fspvlanVlanAssociatedPrimaryVlan,_N:fspvlanIfAssociatedPrimaryVlan,'fspvlanPortObjects':fspvlanPortObjects,'fspvlanPrivatePortTable':fspvlanPrivatePortTable,'fspvlanPrivatePortEntry':fspvlanPrivatePortEntry,_I:fspvlanPrivatePortPrimaryVlan,_O:fspvlanPrivatePortSecondaryVlan,'fspvlanPromPortTable':fspvlanPromPortTable,'fspvlanPromPortEntry':fspvlanPromPortEntry,'fspvlanPrivatePortPrimaryVlanId':fspvlanPrivatePortPrimaryVlanId,_P:fspvlanPromPortSecondaryRemap,_Q:fspvlanPromPortSecondaryRemap2k,_R:fspvlanPromPortSecondaryRemap3k,_S:fspvlanPromPortSecondaryRemap4k,'fspvlanPortModeTable':fspvlanPortModeTable,'fspvlanPortModeEntry':fspvlanPortModeEntry,_T:fspvlanPortMode,'fspvlanSVIObjects':fspvlanSVIObjects,'fspvlanSVIMappingTable':fspvlanSVIMappingTable,'fspvlanSVIMappingEntry':fspvlanSVIMappingEntry,_K:fspvlanSVIMappingVlanIndex,_U:fspvlanSVIMappingPrimarySVI,'fspvlanMIBConformance':fspvlanMIBConformance,'fspvlanMIBCompliances':fspvlanMIBCompliances,'fspvlanMIBCompliance':fspvlanMIBCompliance,'fspvlanMIBGroups':fspvlanMIBGroups,_V:fspvlanVlanGroup,_W:fspvlanPrivatePortGroup,_X:fspvlanPromPortGroup,_Y:fspvlanPortModeGroup,_Z:fspvlanSVIGroup})