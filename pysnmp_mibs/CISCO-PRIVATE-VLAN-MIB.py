_m='cpvlanTrunkPortEncapOperType'
_l='cpvlanTrunkPortDynamicStatus'
_k='cpvlanTrunkPortNormalVlans4k'
_j='cpvlanTrunkPortNormalVlans3k'
_i='cpvlanTrunkPortNormalVlans2k'
_h='cpvlanTrunkPortNormalVlans'
_g='cpvlanTrunkPortSecondaryVlans4k'
_f='cpvlanTrunkPortSecondaryVlans3k'
_e='cpvlanTrunkPortSecondaryVlans2k'
_d='cpvlanTrunkPortSecondaryVlans'
_c='cpvlanTrunkPortNativeVlan'
_b='cpvlanTrunkPortEncapType'
_a='cpvlanTrunkPortDynamicState'
_Z='cpvlanSVIMappingPrimarySVI'
_Y='cpvlanPortMode'
_X='cpvlanPromPortSecondaryRemap4k'
_W='cpvlanPromPortSecondaryRemap3k'
_V='cpvlanPromPortSecondaryRemap2k'
_U='cpvlanPromPortTwoWayRemapCapable'
_T='cpvlanPromPortSecondaryRemap'
_S='cpvlanPromPortMultiPrimaryVlan'
_R='cpvlanPrivatePortSecondaryVlan'
_Q='cpvlanVlanEditAssocPrimaryVlan'
_P='cpvlanVlanEditPrivateVlanType'
_O='cpvlanVlanAssociatedPrimaryVlan'
_N='cpvlanVlanPrivateVlanType'
_M='cpvlanVlanEditEntry'
_L='cpvlanVlanEntry'
_K='cpvlanSVIMappingVlanIndex'
_J='PrivateVlanType'
_I='VlanIndexOrZero'
_H='ifIndex'
_G='IF-MIB'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='CISCO-PRIVATE-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
vtpVlanEditEntry,vtpVlanEntry=mibBuilder.importSymbols('CISCO-VTP-MIB','vtpVlanEditEntry','vtpVlanEntry')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoPrivateVlanMIB=ModuleIdentity((1,3,6,1,4,1,9,9,173))
if mibBuilder.loadTexts:ciscoPrivateVlanMIB.setRevisions(('2005-09-08 00:00','2002-07-24 00:00','2001-05-23 00:00','2001-04-17 00:00'))
class PrivateVlanType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normal',1),('primary',2),('isolated',3),('community',4),('twoWayCommunity',5)))
class VlanIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
class VlanIndexBitmap(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpvlanMIBObjects_ObjectIdentity=ObjectIdentity
cpvlanMIBObjects=_CpvlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,173,1))
_CpvlanVlanObjects_ObjectIdentity=ObjectIdentity
cpvlanVlanObjects=_CpvlanVlanObjects_ObjectIdentity((1,3,6,1,4,1,9,9,173,1,1))
_CpvlanVlanTable_Object=MibTable
cpvlanVlanTable=_CpvlanVlanTable_Object((1,3,6,1,4,1,9,9,173,1,1,1))
if mibBuilder.loadTexts:cpvlanVlanTable.setStatus(_A)
_CpvlanVlanEntry_Object=MibTableRow
cpvlanVlanEntry=_CpvlanVlanEntry_Object((1,3,6,1,4,1,9,9,173,1,1,1,1))
if mibBuilder.loadTexts:cpvlanVlanEntry.setStatus(_A)
_CpvlanVlanPrivateVlanType_Type=PrivateVlanType
_CpvlanVlanPrivateVlanType_Object=MibTableColumn
cpvlanVlanPrivateVlanType=_CpvlanVlanPrivateVlanType_Object((1,3,6,1,4,1,9,9,173,1,1,1,1,1),_CpvlanVlanPrivateVlanType_Type())
cpvlanVlanPrivateVlanType.setMaxAccess(_E)
if mibBuilder.loadTexts:cpvlanVlanPrivateVlanType.setStatus(_A)
_CpvlanVlanAssociatedPrimaryVlan_Type=VlanIndexOrZero
_CpvlanVlanAssociatedPrimaryVlan_Object=MibTableColumn
cpvlanVlanAssociatedPrimaryVlan=_CpvlanVlanAssociatedPrimaryVlan_Object((1,3,6,1,4,1,9,9,173,1,1,1,1,2),_CpvlanVlanAssociatedPrimaryVlan_Type())
cpvlanVlanAssociatedPrimaryVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:cpvlanVlanAssociatedPrimaryVlan.setStatus(_A)
_CpvlanVlanEditTable_Object=MibTable
cpvlanVlanEditTable=_CpvlanVlanEditTable_Object((1,3,6,1,4,1,9,9,173,1,1,2))
if mibBuilder.loadTexts:cpvlanVlanEditTable.setStatus(_A)
_CpvlanVlanEditEntry_Object=MibTableRow
cpvlanVlanEditEntry=_CpvlanVlanEditEntry_Object((1,3,6,1,4,1,9,9,173,1,1,2,1))
if mibBuilder.loadTexts:cpvlanVlanEditEntry.setStatus(_A)
class _CpvlanVlanEditPrivateVlanType_Type(PrivateVlanType):defaultValue=1
_CpvlanVlanEditPrivateVlanType_Type.__name__=_J
_CpvlanVlanEditPrivateVlanType_Object=MibTableColumn
cpvlanVlanEditPrivateVlanType=_CpvlanVlanEditPrivateVlanType_Object((1,3,6,1,4,1,9,9,173,1,1,2,1,1),_CpvlanVlanEditPrivateVlanType_Type())
cpvlanVlanEditPrivateVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanVlanEditPrivateVlanType.setStatus(_A)
class _CpvlanVlanEditAssocPrimaryVlan_Type(VlanIndexOrZero):defaultValue=0
_CpvlanVlanEditAssocPrimaryVlan_Type.__name__=_I
_CpvlanVlanEditAssocPrimaryVlan_Object=MibTableColumn
cpvlanVlanEditAssocPrimaryVlan=_CpvlanVlanEditAssocPrimaryVlan_Object((1,3,6,1,4,1,9,9,173,1,1,2,1,2),_CpvlanVlanEditAssocPrimaryVlan_Type())
cpvlanVlanEditAssocPrimaryVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanVlanEditAssocPrimaryVlan.setStatus(_A)
_CpvlanPortObjects_ObjectIdentity=ObjectIdentity
cpvlanPortObjects=_CpvlanPortObjects_ObjectIdentity((1,3,6,1,4,1,9,9,173,1,2))
_CpvlanPrivatePortTable_Object=MibTable
cpvlanPrivatePortTable=_CpvlanPrivatePortTable_Object((1,3,6,1,4,1,9,9,173,1,2,1))
if mibBuilder.loadTexts:cpvlanPrivatePortTable.setStatus(_A)
_CpvlanPrivatePortEntry_Object=MibTableRow
cpvlanPrivatePortEntry=_CpvlanPrivatePortEntry_Object((1,3,6,1,4,1,9,9,173,1,2,1,1))
cpvlanPrivatePortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cpvlanPrivatePortEntry.setStatus(_A)
class _CpvlanPrivatePortSecondaryVlan_Type(VlanIndexOrZero):defaultValue=0
_CpvlanPrivatePortSecondaryVlan_Type.__name__=_I
_CpvlanPrivatePortSecondaryVlan_Object=MibTableColumn
cpvlanPrivatePortSecondaryVlan=_CpvlanPrivatePortSecondaryVlan_Object((1,3,6,1,4,1,9,9,173,1,2,1,1,1),_CpvlanPrivatePortSecondaryVlan_Type())
cpvlanPrivatePortSecondaryVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanPrivatePortSecondaryVlan.setStatus(_A)
_CpvlanPromPortTable_Object=MibTable
cpvlanPromPortTable=_CpvlanPromPortTable_Object((1,3,6,1,4,1,9,9,173,1,2,2))
if mibBuilder.loadTexts:cpvlanPromPortTable.setStatus(_A)
_CpvlanPromPortEntry_Object=MibTableRow
cpvlanPromPortEntry=_CpvlanPromPortEntry_Object((1,3,6,1,4,1,9,9,173,1,2,2,1))
cpvlanPromPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cpvlanPromPortEntry.setStatus(_A)
_CpvlanPromPortMultiPrimaryVlan_Type=TruthValue
_CpvlanPromPortMultiPrimaryVlan_Object=MibTableColumn
cpvlanPromPortMultiPrimaryVlan=_CpvlanPromPortMultiPrimaryVlan_Object((1,3,6,1,4,1,9,9,173,1,2,2,1,1),_CpvlanPromPortMultiPrimaryVlan_Type())
cpvlanPromPortMultiPrimaryVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:cpvlanPromPortMultiPrimaryVlan.setStatus(_A)
class _CpvlanPromPortSecondaryRemap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpvlanPromPortSecondaryRemap_Type.__name__=_F
_CpvlanPromPortSecondaryRemap_Object=MibTableColumn
cpvlanPromPortSecondaryRemap=_CpvlanPromPortSecondaryRemap_Object((1,3,6,1,4,1,9,9,173,1,2,2,1,2),_CpvlanPromPortSecondaryRemap_Type())
cpvlanPromPortSecondaryRemap.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanPromPortSecondaryRemap.setStatus(_A)
class _CpvlanPromPortSecondaryRemap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpvlanPromPortSecondaryRemap2k_Type.__name__=_F
_CpvlanPromPortSecondaryRemap2k_Object=MibTableColumn
cpvlanPromPortSecondaryRemap2k=_CpvlanPromPortSecondaryRemap2k_Object((1,3,6,1,4,1,9,9,173,1,2,2,1,3),_CpvlanPromPortSecondaryRemap2k_Type())
cpvlanPromPortSecondaryRemap2k.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanPromPortSecondaryRemap2k.setStatus(_A)
class _CpvlanPromPortSecondaryRemap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpvlanPromPortSecondaryRemap3k_Type.__name__=_F
_CpvlanPromPortSecondaryRemap3k_Object=MibTableColumn
cpvlanPromPortSecondaryRemap3k=_CpvlanPromPortSecondaryRemap3k_Object((1,3,6,1,4,1,9,9,173,1,2,2,1,4),_CpvlanPromPortSecondaryRemap3k_Type())
cpvlanPromPortSecondaryRemap3k.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanPromPortSecondaryRemap3k.setStatus(_A)
class _CpvlanPromPortSecondaryRemap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpvlanPromPortSecondaryRemap4k_Type.__name__=_F
_CpvlanPromPortSecondaryRemap4k_Object=MibTableColumn
cpvlanPromPortSecondaryRemap4k=_CpvlanPromPortSecondaryRemap4k_Object((1,3,6,1,4,1,9,9,173,1,2,2,1,5),_CpvlanPromPortSecondaryRemap4k_Type())
cpvlanPromPortSecondaryRemap4k.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanPromPortSecondaryRemap4k.setStatus(_A)
_CpvlanPromPortTwoWayRemapCapable_Type=TruthValue
_CpvlanPromPortTwoWayRemapCapable_Object=MibTableColumn
cpvlanPromPortTwoWayRemapCapable=_CpvlanPromPortTwoWayRemapCapable_Object((1,3,6,1,4,1,9,9,173,1,2,2,1,6),_CpvlanPromPortTwoWayRemapCapable_Type())
cpvlanPromPortTwoWayRemapCapable.setMaxAccess(_E)
if mibBuilder.loadTexts:cpvlanPromPortTwoWayRemapCapable.setStatus(_A)
_CpvlanPortModeTable_Object=MibTable
cpvlanPortModeTable=_CpvlanPortModeTable_Object((1,3,6,1,4,1,9,9,173,1,2,3))
if mibBuilder.loadTexts:cpvlanPortModeTable.setStatus(_A)
_CpvlanPortModeEntry_Object=MibTableRow
cpvlanPortModeEntry=_CpvlanPortModeEntry_Object((1,3,6,1,4,1,9,9,173,1,2,3,1))
cpvlanPortModeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cpvlanPortModeEntry.setStatus(_A)
class _CpvlanPortMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonPrivateVlan',1),('host',2),('promiscuous',3),('secondaryTrunk',4),('promiscuousTrunk',5)))
_CpvlanPortMode_Type.__name__=_D
_CpvlanPortMode_Object=MibTableColumn
cpvlanPortMode=_CpvlanPortMode_Object((1,3,6,1,4,1,9,9,173,1,2,3,1,1),_CpvlanPortMode_Type())
cpvlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanPortMode.setStatus(_A)
_CpvlanTrunkPortTable_Object=MibTable
cpvlanTrunkPortTable=_CpvlanTrunkPortTable_Object((1,3,6,1,4,1,9,9,173,1,2,4))
if mibBuilder.loadTexts:cpvlanTrunkPortTable.setStatus(_A)
_CpvlanTrunkPortEntry_Object=MibTableRow
cpvlanTrunkPortEntry=_CpvlanTrunkPortEntry_Object((1,3,6,1,4,1,9,9,173,1,2,4,1))
cpvlanTrunkPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cpvlanTrunkPortEntry.setStatus(_A)
class _CpvlanTrunkPortDynamicState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('onNoNegotiate',2)))
_CpvlanTrunkPortDynamicState_Type.__name__=_D
_CpvlanTrunkPortDynamicState_Object=MibTableColumn
cpvlanTrunkPortDynamicState=_CpvlanTrunkPortDynamicState_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,1),_CpvlanTrunkPortDynamicState_Type())
cpvlanTrunkPortDynamicState.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortDynamicState.setStatus(_A)
class _CpvlanTrunkPortEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot1Q',1),('isl',2),('negotiate',3)))
_CpvlanTrunkPortEncapType_Type.__name__=_D
_CpvlanTrunkPortEncapType_Object=MibTableColumn
cpvlanTrunkPortEncapType=_CpvlanTrunkPortEncapType_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,2),_CpvlanTrunkPortEncapType_Type())
cpvlanTrunkPortEncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortEncapType.setStatus(_A)
_CpvlanTrunkPortNativeVlan_Type=VlanIndexOrZero
_CpvlanTrunkPortNativeVlan_Object=MibTableColumn
cpvlanTrunkPortNativeVlan=_CpvlanTrunkPortNativeVlan_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,3),_CpvlanTrunkPortNativeVlan_Type())
cpvlanTrunkPortNativeVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortNativeVlan.setStatus(_A)
_CpvlanTrunkPortSecondaryVlans_Type=VlanIndexBitmap
_CpvlanTrunkPortSecondaryVlans_Object=MibTableColumn
cpvlanTrunkPortSecondaryVlans=_CpvlanTrunkPortSecondaryVlans_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,4),_CpvlanTrunkPortSecondaryVlans_Type())
cpvlanTrunkPortSecondaryVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortSecondaryVlans.setStatus(_A)
_CpvlanTrunkPortSecondaryVlans2k_Type=VlanIndexBitmap
_CpvlanTrunkPortSecondaryVlans2k_Object=MibTableColumn
cpvlanTrunkPortSecondaryVlans2k=_CpvlanTrunkPortSecondaryVlans2k_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,5),_CpvlanTrunkPortSecondaryVlans2k_Type())
cpvlanTrunkPortSecondaryVlans2k.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortSecondaryVlans2k.setStatus(_A)
_CpvlanTrunkPortSecondaryVlans3k_Type=VlanIndexBitmap
_CpvlanTrunkPortSecondaryVlans3k_Object=MibTableColumn
cpvlanTrunkPortSecondaryVlans3k=_CpvlanTrunkPortSecondaryVlans3k_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,6),_CpvlanTrunkPortSecondaryVlans3k_Type())
cpvlanTrunkPortSecondaryVlans3k.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortSecondaryVlans3k.setStatus(_A)
_CpvlanTrunkPortSecondaryVlans4k_Type=VlanIndexBitmap
_CpvlanTrunkPortSecondaryVlans4k_Object=MibTableColumn
cpvlanTrunkPortSecondaryVlans4k=_CpvlanTrunkPortSecondaryVlans4k_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,7),_CpvlanTrunkPortSecondaryVlans4k_Type())
cpvlanTrunkPortSecondaryVlans4k.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortSecondaryVlans4k.setStatus(_A)
_CpvlanTrunkPortNormalVlans_Type=VlanIndexBitmap
_CpvlanTrunkPortNormalVlans_Object=MibTableColumn
cpvlanTrunkPortNormalVlans=_CpvlanTrunkPortNormalVlans_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,8),_CpvlanTrunkPortNormalVlans_Type())
cpvlanTrunkPortNormalVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortNormalVlans.setStatus(_A)
_CpvlanTrunkPortNormalVlans2k_Type=VlanIndexBitmap
_CpvlanTrunkPortNormalVlans2k_Object=MibTableColumn
cpvlanTrunkPortNormalVlans2k=_CpvlanTrunkPortNormalVlans2k_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,9),_CpvlanTrunkPortNormalVlans2k_Type())
cpvlanTrunkPortNormalVlans2k.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortNormalVlans2k.setStatus(_A)
_CpvlanTrunkPortNormalVlans3k_Type=VlanIndexBitmap
_CpvlanTrunkPortNormalVlans3k_Object=MibTableColumn
cpvlanTrunkPortNormalVlans3k=_CpvlanTrunkPortNormalVlans3k_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,10),_CpvlanTrunkPortNormalVlans3k_Type())
cpvlanTrunkPortNormalVlans3k.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortNormalVlans3k.setStatus(_A)
_CpvlanTrunkPortNormalVlans4k_Type=VlanIndexBitmap
_CpvlanTrunkPortNormalVlans4k_Object=MibTableColumn
cpvlanTrunkPortNormalVlans4k=_CpvlanTrunkPortNormalVlans4k_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,11),_CpvlanTrunkPortNormalVlans4k_Type())
cpvlanTrunkPortNormalVlans4k.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanTrunkPortNormalVlans4k.setStatus(_A)
class _CpvlanTrunkPortDynamicStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trunking',1),('notTrunking',2)))
_CpvlanTrunkPortDynamicStatus_Type.__name__=_D
_CpvlanTrunkPortDynamicStatus_Object=MibTableColumn
cpvlanTrunkPortDynamicStatus=_CpvlanTrunkPortDynamicStatus_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,12),_CpvlanTrunkPortDynamicStatus_Type())
cpvlanTrunkPortDynamicStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpvlanTrunkPortDynamicStatus.setStatus(_A)
class _CpvlanTrunkPortEncapOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot1Q',1),('isl',2),('notApplicable',3)))
_CpvlanTrunkPortEncapOperType_Type.__name__=_D
_CpvlanTrunkPortEncapOperType_Object=MibTableColumn
cpvlanTrunkPortEncapOperType=_CpvlanTrunkPortEncapOperType_Object((1,3,6,1,4,1,9,9,173,1,2,4,1,13),_CpvlanTrunkPortEncapOperType_Type())
cpvlanTrunkPortEncapOperType.setMaxAccess(_E)
if mibBuilder.loadTexts:cpvlanTrunkPortEncapOperType.setStatus(_A)
_CpvlanSVIObjects_ObjectIdentity=ObjectIdentity
cpvlanSVIObjects=_CpvlanSVIObjects_ObjectIdentity((1,3,6,1,4,1,9,9,173,1,3))
_CpvlanSVIMappingTable_Object=MibTable
cpvlanSVIMappingTable=_CpvlanSVIMappingTable_Object((1,3,6,1,4,1,9,9,173,1,3,1))
if mibBuilder.loadTexts:cpvlanSVIMappingTable.setStatus(_A)
_CpvlanSVIMappingEntry_Object=MibTableRow
cpvlanSVIMappingEntry=_CpvlanSVIMappingEntry_Object((1,3,6,1,4,1,9,9,173,1,3,1,1))
cpvlanSVIMappingEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cpvlanSVIMappingEntry.setStatus(_A)
_CpvlanSVIMappingVlanIndex_Type=VlanIndexOrZero
_CpvlanSVIMappingVlanIndex_Object=MibTableColumn
cpvlanSVIMappingVlanIndex=_CpvlanSVIMappingVlanIndex_Object((1,3,6,1,4,1,9,9,173,1,3,1,1,1),_CpvlanSVIMappingVlanIndex_Type())
cpvlanSVIMappingVlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cpvlanSVIMappingVlanIndex.setStatus(_A)
class _CpvlanSVIMappingPrimarySVI_Type(VlanIndexOrZero):defaultValue=0
_CpvlanSVIMappingPrimarySVI_Type.__name__=_I
_CpvlanSVIMappingPrimarySVI_Object=MibTableColumn
cpvlanSVIMappingPrimarySVI=_CpvlanSVIMappingPrimarySVI_Object((1,3,6,1,4,1,9,9,173,1,3,1,1,2),_CpvlanSVIMappingPrimarySVI_Type())
cpvlanSVIMappingPrimarySVI.setMaxAccess(_C)
if mibBuilder.loadTexts:cpvlanSVIMappingPrimarySVI.setStatus(_A)
_CpvlanMIBConformance_ObjectIdentity=ObjectIdentity
cpvlanMIBConformance=_CpvlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,173,2))
_CpvlanMIBCompliances_ObjectIdentity=ObjectIdentity
cpvlanMIBCompliances=_CpvlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,173,2,1))
_CpvlanMIBGroups_ObjectIdentity=ObjectIdentity
cpvlanMIBGroups=_CpvlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,173,2,2))
vtpVlanEntry.registerAugmentions((_B,_L))
cpvlanVlanEntry.setIndexNames(*vtpVlanEntry.getIndexNames())
vtpVlanEditEntry.registerAugmentions((_B,_M))
cpvlanVlanEditEntry.setIndexNames(*vtpVlanEditEntry.getIndexNames())
cpvlanVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,173,2,2,1))
cpvlanVlanGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cpvlanVlanGroup.setStatus(_A)
cpvlanPrivatePortGroup=ObjectGroup((1,3,6,1,4,1,9,9,173,2,2,2))
cpvlanPrivatePortGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:cpvlanPrivatePortGroup.setStatus(_A)
cpvlanPromPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,173,2,2,3))
cpvlanPromPortGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cpvlanPromPortGroup.setStatus(_A)
cpvlanPromPort4kGroup=ObjectGroup((1,3,6,1,4,1,9,9,173,2,2,4))
cpvlanPromPort4kGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cpvlanPromPort4kGroup.setStatus(_A)
cpvlanPortModeGroup=ObjectGroup((1,3,6,1,4,1,9,9,173,2,2,5))
cpvlanPortModeGroup.setObjects((_B,_Y))
if mibBuilder.loadTexts:cpvlanPortModeGroup.setStatus(_A)
cpvlanSVIMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,173,2,2,6))
cpvlanSVIMappingGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:cpvlanSVIMappingGroup.setStatus(_A)
cpvlanTrunkPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,173,2,2,7))
cpvlanTrunkPortGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:cpvlanTrunkPortGroup.setStatus(_A)
cpvlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,173,2,1,1))
if mibBuilder.loadTexts:cpvlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:PrivateVlanType,_I:VlanIndexOrZero,'VlanIndexBitmap':VlanIndexBitmap,'ciscoPrivateVlanMIB':ciscoPrivateVlanMIB,'cpvlanMIBObjects':cpvlanMIBObjects,'cpvlanVlanObjects':cpvlanVlanObjects,'cpvlanVlanTable':cpvlanVlanTable,_L:cpvlanVlanEntry,_N:cpvlanVlanPrivateVlanType,_O:cpvlanVlanAssociatedPrimaryVlan,'cpvlanVlanEditTable':cpvlanVlanEditTable,_M:cpvlanVlanEditEntry,_P:cpvlanVlanEditPrivateVlanType,_Q:cpvlanVlanEditAssocPrimaryVlan,'cpvlanPortObjects':cpvlanPortObjects,'cpvlanPrivatePortTable':cpvlanPrivatePortTable,'cpvlanPrivatePortEntry':cpvlanPrivatePortEntry,_R:cpvlanPrivatePortSecondaryVlan,'cpvlanPromPortTable':cpvlanPromPortTable,'cpvlanPromPortEntry':cpvlanPromPortEntry,_S:cpvlanPromPortMultiPrimaryVlan,_T:cpvlanPromPortSecondaryRemap,_V:cpvlanPromPortSecondaryRemap2k,_W:cpvlanPromPortSecondaryRemap3k,_X:cpvlanPromPortSecondaryRemap4k,_U:cpvlanPromPortTwoWayRemapCapable,'cpvlanPortModeTable':cpvlanPortModeTable,'cpvlanPortModeEntry':cpvlanPortModeEntry,_Y:cpvlanPortMode,'cpvlanTrunkPortTable':cpvlanTrunkPortTable,'cpvlanTrunkPortEntry':cpvlanTrunkPortEntry,_a:cpvlanTrunkPortDynamicState,_b:cpvlanTrunkPortEncapType,_c:cpvlanTrunkPortNativeVlan,_d:cpvlanTrunkPortSecondaryVlans,_e:cpvlanTrunkPortSecondaryVlans2k,_f:cpvlanTrunkPortSecondaryVlans3k,_g:cpvlanTrunkPortSecondaryVlans4k,_h:cpvlanTrunkPortNormalVlans,_i:cpvlanTrunkPortNormalVlans2k,_j:cpvlanTrunkPortNormalVlans3k,_k:cpvlanTrunkPortNormalVlans4k,_l:cpvlanTrunkPortDynamicStatus,_m:cpvlanTrunkPortEncapOperType,'cpvlanSVIObjects':cpvlanSVIObjects,'cpvlanSVIMappingTable':cpvlanSVIMappingTable,'cpvlanSVIMappingEntry':cpvlanSVIMappingEntry,_K:cpvlanSVIMappingVlanIndex,_Z:cpvlanSVIMappingPrimarySVI,'cpvlanMIBConformance':cpvlanMIBConformance,'cpvlanMIBCompliances':cpvlanMIBCompliances,'cpvlanMIBCompliance':cpvlanMIBCompliance,'cpvlanMIBGroups':cpvlanMIBGroups,'cpvlanVlanGroup':cpvlanVlanGroup,'cpvlanPrivatePortGroup':cpvlanPrivatePortGroup,'cpvlanPromPortGroup':cpvlanPromPortGroup,'cpvlanPromPort4kGroup':cpvlanPromPort4kGroup,'cpvlanPortModeGroup':cpvlanPortModeGroup,'cpvlanSVIMappingGroup':cpvlanSVIMappingGroup,'cpvlanTrunkPortGroup':cpvlanTrunkPortGroup})