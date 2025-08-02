_Z='mypvlanSVIGroup'
_Y='mypvlanPortModeGroup'
_X='mypvlanPromPortGroup'
_W='mypvlanPrivatePortGroup'
_V='mypvlanVlanGroup'
_U='mypvlanSVIMappingPrimarySVI'
_T='mypvlanPortMode'
_S='mypvlanPromPortSecondaryRemap4k'
_R='mypvlanPromPortSecondaryRemap3k'
_Q='mypvlanPromPortSecondaryRemap2k'
_P='mypvlanPromPortSecondaryRemap'
_O='mypvlanPrivatePortSecondaryVlan'
_N='mypvlanIfAssociatedPrimaryVlan'
_M='mypvlanVlanAssociatedPrimaryVlan'
_L='mypvlanVlanPrivateVlanType'
_K='mypvlanSVIMappingVlanIndex'
_J='Integer32'
_I='mypvlanPrivatePortPrimaryVlan'
_H='read-create'
_G='mypvlanVlanIndex'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-write'
_B='DES7200-PRIVATE-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
myPrivateVlanMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,44))
if mibBuilder.loadTexts:myPrivateVlanMIB.setRevisions(('2009-03-01 00:00',))
class PrivateVlanType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('primary',2),('isolated',3),('community',4)))
class VlanIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
class VlanIndexBitmap(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MypvlanMIBObjects_ObjectIdentity=ObjectIdentity
mypvlanMIBObjects=_MypvlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,44,1))
_MypvlanVlanObjects_ObjectIdentity=ObjectIdentity
mypvlanVlanObjects=_MypvlanVlanObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,44,1,1))
_MypvlanVlanTable_Object=MibTable
mypvlanVlanTable=_MypvlanVlanTable_Object((1,3,6,1,4,1,171,10,97,2,44,1,1,1))
if mibBuilder.loadTexts:mypvlanVlanTable.setStatus(_A)
_MypvlanVlanEntry_Object=MibTableRow
mypvlanVlanEntry=_MypvlanVlanEntry_Object((1,3,6,1,4,1,171,10,97,2,44,1,1,1,1))
mypvlanVlanEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:mypvlanVlanEntry.setStatus(_A)
_MypvlanVlanIndex_Type=VlanIndexOrZero
_MypvlanVlanIndex_Object=MibTableColumn
mypvlanVlanIndex=_MypvlanVlanIndex_Object((1,3,6,1,4,1,171,10,97,2,44,1,1,1,1,1),_MypvlanVlanIndex_Type())
mypvlanVlanIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:mypvlanVlanIndex.setStatus(_A)
_MypvlanVlanPrivateVlanType_Type=PrivateVlanType
_MypvlanVlanPrivateVlanType_Object=MibTableColumn
mypvlanVlanPrivateVlanType=_MypvlanVlanPrivateVlanType_Object((1,3,6,1,4,1,171,10,97,2,44,1,1,1,1,2),_MypvlanVlanPrivateVlanType_Type())
mypvlanVlanPrivateVlanType.setMaxAccess(_H)
if mibBuilder.loadTexts:mypvlanVlanPrivateVlanType.setStatus(_A)
_MypvlanVlanAssociatedPrimaryVlan_Type=VlanIndexOrZero
_MypvlanVlanAssociatedPrimaryVlan_Object=MibTableColumn
mypvlanVlanAssociatedPrimaryVlan=_MypvlanVlanAssociatedPrimaryVlan_Object((1,3,6,1,4,1,171,10,97,2,44,1,1,1,1,3),_MypvlanVlanAssociatedPrimaryVlan_Type())
mypvlanVlanAssociatedPrimaryVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:mypvlanVlanAssociatedPrimaryVlan.setStatus(_A)
_MypvlanIfAssociatedPrimaryVlan_Type=TruthValue
_MypvlanIfAssociatedPrimaryVlan_Object=MibTableColumn
mypvlanIfAssociatedPrimaryVlan=_MypvlanIfAssociatedPrimaryVlan_Object((1,3,6,1,4,1,171,10,97,2,44,1,1,1,1,4),_MypvlanIfAssociatedPrimaryVlan_Type())
mypvlanIfAssociatedPrimaryVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:mypvlanIfAssociatedPrimaryVlan.setStatus(_A)
_MypvlanPortObjects_ObjectIdentity=ObjectIdentity
mypvlanPortObjects=_MypvlanPortObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,44,1,2))
_MypvlanPrivatePortTable_Object=MibTable
mypvlanPrivatePortTable=_MypvlanPrivatePortTable_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,1))
if mibBuilder.loadTexts:mypvlanPrivatePortTable.setStatus(_A)
_MypvlanPrivatePortEntry_Object=MibTableRow
mypvlanPrivatePortEntry=_MypvlanPrivatePortEntry_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,1,1))
mypvlanPrivatePortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mypvlanPrivatePortEntry.setStatus(_A)
_MypvlanPrivatePortPrimaryVlan_Type=VlanIndexOrZero
_MypvlanPrivatePortPrimaryVlan_Object=MibTableColumn
mypvlanPrivatePortPrimaryVlan=_MypvlanPrivatePortPrimaryVlan_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,1,1,1),_MypvlanPrivatePortPrimaryVlan_Type())
mypvlanPrivatePortPrimaryVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:mypvlanPrivatePortPrimaryVlan.setStatus(_A)
_MypvlanPrivatePortSecondaryVlan_Type=VlanIndexOrZero
_MypvlanPrivatePortSecondaryVlan_Object=MibTableColumn
mypvlanPrivatePortSecondaryVlan=_MypvlanPrivatePortSecondaryVlan_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,1,1,2),_MypvlanPrivatePortSecondaryVlan_Type())
mypvlanPrivatePortSecondaryVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:mypvlanPrivatePortSecondaryVlan.setStatus(_A)
_MypvlanPromPortTable_Object=MibTable
mypvlanPromPortTable=_MypvlanPromPortTable_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,2))
if mibBuilder.loadTexts:mypvlanPromPortTable.setStatus(_A)
_MypvlanPromPortEntry_Object=MibTableRow
mypvlanPromPortEntry=_MypvlanPromPortEntry_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,2,1))
mypvlanPromPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mypvlanPromPortEntry.setStatus(_A)
_MypvlanPrivatePortPrimaryVlanId_Type=VlanIndexOrZero
_MypvlanPrivatePortPrimaryVlanId_Object=MibTableColumn
mypvlanPrivatePortPrimaryVlanId=_MypvlanPrivatePortPrimaryVlanId_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,2,1,1),_MypvlanPrivatePortPrimaryVlanId_Type())
mypvlanPrivatePortPrimaryVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:mypvlanPrivatePortPrimaryVlanId.setStatus(_A)
class _MypvlanPromPortSecondaryRemap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MypvlanPromPortSecondaryRemap_Type.__name__=_D
_MypvlanPromPortSecondaryRemap_Object=MibTableColumn
mypvlanPromPortSecondaryRemap=_MypvlanPromPortSecondaryRemap_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,2,1,2),_MypvlanPromPortSecondaryRemap_Type())
mypvlanPromPortSecondaryRemap.setMaxAccess(_C)
if mibBuilder.loadTexts:mypvlanPromPortSecondaryRemap.setStatus(_A)
class _MypvlanPromPortSecondaryRemap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MypvlanPromPortSecondaryRemap2k_Type.__name__=_D
_MypvlanPromPortSecondaryRemap2k_Object=MibTableColumn
mypvlanPromPortSecondaryRemap2k=_MypvlanPromPortSecondaryRemap2k_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,2,1,3),_MypvlanPromPortSecondaryRemap2k_Type())
mypvlanPromPortSecondaryRemap2k.setMaxAccess(_C)
if mibBuilder.loadTexts:mypvlanPromPortSecondaryRemap2k.setStatus(_A)
class _MypvlanPromPortSecondaryRemap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MypvlanPromPortSecondaryRemap3k_Type.__name__=_D
_MypvlanPromPortSecondaryRemap3k_Object=MibTableColumn
mypvlanPromPortSecondaryRemap3k=_MypvlanPromPortSecondaryRemap3k_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,2,1,4),_MypvlanPromPortSecondaryRemap3k_Type())
mypvlanPromPortSecondaryRemap3k.setMaxAccess(_C)
if mibBuilder.loadTexts:mypvlanPromPortSecondaryRemap3k.setStatus(_A)
class _MypvlanPromPortSecondaryRemap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MypvlanPromPortSecondaryRemap4k_Type.__name__=_D
_MypvlanPromPortSecondaryRemap4k_Object=MibTableColumn
mypvlanPromPortSecondaryRemap4k=_MypvlanPromPortSecondaryRemap4k_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,2,1,5),_MypvlanPromPortSecondaryRemap4k_Type())
mypvlanPromPortSecondaryRemap4k.setMaxAccess(_C)
if mibBuilder.loadTexts:mypvlanPromPortSecondaryRemap4k.setStatus(_A)
_MypvlanPortModeTable_Object=MibTable
mypvlanPortModeTable=_MypvlanPortModeTable_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,3))
if mibBuilder.loadTexts:mypvlanPortModeTable.setStatus(_A)
_MypvlanPortModeEntry_Object=MibTableRow
mypvlanPortModeEntry=_MypvlanPortModeEntry_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,3,1))
mypvlanPortModeEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mypvlanPortModeEntry.setStatus(_A)
class _MypvlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nonPrivateVlan',1),('host',2),('promiscuous',3)))
_MypvlanPortMode_Type.__name__=_J
_MypvlanPortMode_Object=MibTableColumn
mypvlanPortMode=_MypvlanPortMode_Object((1,3,6,1,4,1,171,10,97,2,44,1,2,3,1,1),_MypvlanPortMode_Type())
mypvlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mypvlanPortMode.setStatus(_A)
_MypvlanSVIObjects_ObjectIdentity=ObjectIdentity
mypvlanSVIObjects=_MypvlanSVIObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,44,1,3))
_MypvlanSVIMappingTable_Object=MibTable
mypvlanSVIMappingTable=_MypvlanSVIMappingTable_Object((1,3,6,1,4,1,171,10,97,2,44,1,3,1))
if mibBuilder.loadTexts:mypvlanSVIMappingTable.setStatus(_A)
_MypvlanSVIMappingEntry_Object=MibTableRow
mypvlanSVIMappingEntry=_MypvlanSVIMappingEntry_Object((1,3,6,1,4,1,171,10,97,2,44,1,3,1,1))
mypvlanSVIMappingEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:mypvlanSVIMappingEntry.setStatus(_A)
_MypvlanSVIMappingVlanIndex_Type=VlanIndexOrZero
_MypvlanSVIMappingVlanIndex_Object=MibTableColumn
mypvlanSVIMappingVlanIndex=_MypvlanSVIMappingVlanIndex_Object((1,3,6,1,4,1,171,10,97,2,44,1,3,1,1,1),_MypvlanSVIMappingVlanIndex_Type())
mypvlanSVIMappingVlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mypvlanSVIMappingVlanIndex.setStatus(_A)
_MypvlanSVIMappingPrimarySVI_Type=VlanIndexOrZero
_MypvlanSVIMappingPrimarySVI_Object=MibTableColumn
mypvlanSVIMappingPrimarySVI=_MypvlanSVIMappingPrimarySVI_Object((1,3,6,1,4,1,171,10,97,2,44,1,3,1,1,2),_MypvlanSVIMappingPrimarySVI_Type())
mypvlanSVIMappingPrimarySVI.setMaxAccess(_C)
if mibBuilder.loadTexts:mypvlanSVIMappingPrimarySVI.setStatus(_A)
_MypvlanMIBConformance_ObjectIdentity=ObjectIdentity
mypvlanMIBConformance=_MypvlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,44,2))
_MypvlanMIBCompliances_ObjectIdentity=ObjectIdentity
mypvlanMIBCompliances=_MypvlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,44,2,1))
_MypvlanMIBGroups_ObjectIdentity=ObjectIdentity
mypvlanMIBGroups=_MypvlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,44,2,2))
mypvlanVlanGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,44,2,2,1))
mypvlanVlanGroup.setObjects(*((_B,_G),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:mypvlanVlanGroup.setStatus(_A)
mypvlanPrivatePortGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,44,2,2,2))
mypvlanPrivatePortGroup.setObjects(*((_B,_I),(_B,_O)))
if mibBuilder.loadTexts:mypvlanPrivatePortGroup.setStatus(_A)
mypvlanPromPortGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,44,2,2,3))
mypvlanPromPortGroup.setObjects(*((_B,_I),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:mypvlanPromPortGroup.setStatus(_A)
mypvlanPortModeGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,44,2,2,4))
mypvlanPortModeGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:mypvlanPortModeGroup.setStatus(_A)
mypvlanSVIGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,44,2,2,5))
mypvlanSVIGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:mypvlanSVIGroup.setStatus(_A)
mypvlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,44,2,1,1))
mypvlanMIBCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:mypvlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PrivateVlanType':PrivateVlanType,'VlanIndexOrZero':VlanIndexOrZero,'VlanIndexBitmap':VlanIndexBitmap,'myPrivateVlanMIB':myPrivateVlanMIB,'mypvlanMIBObjects':mypvlanMIBObjects,'mypvlanVlanObjects':mypvlanVlanObjects,'mypvlanVlanTable':mypvlanVlanTable,'mypvlanVlanEntry':mypvlanVlanEntry,_G:mypvlanVlanIndex,_L:mypvlanVlanPrivateVlanType,_M:mypvlanVlanAssociatedPrimaryVlan,_N:mypvlanIfAssociatedPrimaryVlan,'mypvlanPortObjects':mypvlanPortObjects,'mypvlanPrivatePortTable':mypvlanPrivatePortTable,'mypvlanPrivatePortEntry':mypvlanPrivatePortEntry,_I:mypvlanPrivatePortPrimaryVlan,_O:mypvlanPrivatePortSecondaryVlan,'mypvlanPromPortTable':mypvlanPromPortTable,'mypvlanPromPortEntry':mypvlanPromPortEntry,'mypvlanPrivatePortPrimaryVlanId':mypvlanPrivatePortPrimaryVlanId,_P:mypvlanPromPortSecondaryRemap,_Q:mypvlanPromPortSecondaryRemap2k,_R:mypvlanPromPortSecondaryRemap3k,_S:mypvlanPromPortSecondaryRemap4k,'mypvlanPortModeTable':mypvlanPortModeTable,'mypvlanPortModeEntry':mypvlanPortModeEntry,_T:mypvlanPortMode,'mypvlanSVIObjects':mypvlanSVIObjects,'mypvlanSVIMappingTable':mypvlanSVIMappingTable,'mypvlanSVIMappingEntry':mypvlanSVIMappingEntry,_K:mypvlanSVIMappingVlanIndex,_U:mypvlanSVIMappingPrimarySVI,'mypvlanMIBConformance':mypvlanMIBConformance,'mypvlanMIBCompliances':mypvlanMIBCompliances,'mypvlanMIBCompliance':mypvlanMIBCompliance,'mypvlanMIBGroups':mypvlanMIBGroups,_V:mypvlanVlanGroup,_W:mypvlanPrivatePortGroup,_X:mypvlanPromPortGroup,_Y:mypvlanPortModeGroup,_Z:mypvlanSVIGroup})