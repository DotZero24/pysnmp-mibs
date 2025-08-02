_g='fsQinQMIBGroup'
_f='fsselectiveQinQBasedOnAclVlanID'
_e='fsselectiveQinQBasedOnVlanVlanList'
_d='fsQinQPriorityRemarkValue'
_c='fsQinQPriorityCopyPortStatus'
_b='fsQinQIfServiceTPIDValue'
_a='fsQinQServiceTPIDValue'
_Z='fsQinQPortAllowedTagVlanList'
_Y='fsQinQPortAllowedUntagVlanList'
_X='fsQinQPortNativeVlan'
_W='fsQinQPortConfigMode'
_V='fsQinQVlanMappingType'
_U='fsQinQVlanMappingIfIndex'
_T='fsselectiveQinQBasedOnAclIfIndex'
_S='addOuterTag'
_R='fsselectiveQinQBasedOnVlanIfIndex'
_Q='fsQinQPriorityRemarkIfIndex'
_P='fsQinQPriorityCopyIfIndex'
_O='fsQinQIfServiceTPIDConfigIfIndex'
_N='fsQinQPortConfigIndex'
_M='fsQinQVlanMappingNewVlanID'
_L='fsselectiveQinQBasedOnAclAclID'
_K='fsselectiveQinQBasedOnAclType'
_J='fsselectiveQinQBasedOnVlanOldOuterVlanID'
_I='fsselectiveQinQBasedOnVlanOuterVlanID'
_H='fsselectiveQinQBasedOnVlanType'
_G='fsQinQPriorityValue'
_F='read-write'
_E='not-accessible'
_D='read-only'
_C='Integer32'
_B='FS-QINQ-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsQinQMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,53))
if mibBuilder.loadTexts:fsQinQMIB.setRevisions(('2009-09-09 00:00',))
class VlanList(TextualConvention,OctetString):status=_A
_FsQINQMIBObjects_ObjectIdentity=ObjectIdentity
fsQINQMIBObjects=_FsQINQMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,53,1))
_FsQinQPortConfigTable_Object=MibTable
fsQinQPortConfigTable=_FsQinQPortConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,1))
if mibBuilder.loadTexts:fsQinQPortConfigTable.setStatus(_A)
_FsQinQPortConfigEntry_Object=MibTableRow
fsQinQPortConfigEntry=_FsQinQPortConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,1,1))
fsQinQPortConfigEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:fsQinQPortConfigEntry.setStatus(_A)
_FsQinQPortConfigIndex_Type=IfIndex
_FsQinQPortConfigIndex_Object=MibTableColumn
fsQinQPortConfigIndex=_FsQinQPortConfigIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,1,1,1),_FsQinQPortConfigIndex_Type())
fsQinQPortConfigIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQinQPortConfigIndex.setStatus(_A)
class _FsQinQPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('dot1q-tunnel',2)))
_FsQinQPortConfigMode_Type.__name__=_C
_FsQinQPortConfigMode_Object=MibTableColumn
fsQinQPortConfigMode=_FsQinQPortConfigMode_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,1,1,2),_FsQinQPortConfigMode_Type())
fsQinQPortConfigMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQinQPortConfigMode.setStatus(_A)
_FsQinQPortNativeVlan_Type=VlanId
_FsQinQPortNativeVlan_Object=MibTableColumn
fsQinQPortNativeVlan=_FsQinQPortNativeVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,1,1,3),_FsQinQPortNativeVlan_Type())
fsQinQPortNativeVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQinQPortNativeVlan.setStatus(_A)
_FsQinQPortAllowedUntagVlanList_Type=VlanList
_FsQinQPortAllowedUntagVlanList_Object=MibTableColumn
fsQinQPortAllowedUntagVlanList=_FsQinQPortAllowedUntagVlanList_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,1,1,4),_FsQinQPortAllowedUntagVlanList_Type())
fsQinQPortAllowedUntagVlanList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQinQPortAllowedUntagVlanList.setStatus(_A)
_FsQinQPortAllowedTagVlanList_Type=VlanList
_FsQinQPortAllowedTagVlanList_Object=MibTableColumn
fsQinQPortAllowedTagVlanList=_FsQinQPortAllowedTagVlanList_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,1,1,5),_FsQinQPortAllowedTagVlanList_Type())
fsQinQPortAllowedTagVlanList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQinQPortAllowedTagVlanList.setStatus(_A)
class _FsQinQServiceTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQinQServiceTPIDValue_Type.__name__=_C
_FsQinQServiceTPIDValue_Object=MibScalar
fsQinQServiceTPIDValue=_FsQinQServiceTPIDValue_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,2),_FsQinQServiceTPIDValue_Type())
fsQinQServiceTPIDValue.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQinQServiceTPIDValue.setStatus(_A)
_FsQinQIfServiceTPIDConfigTable_Object=MibTable
fsQinQIfServiceTPIDConfigTable=_FsQinQIfServiceTPIDConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,3))
if mibBuilder.loadTexts:fsQinQIfServiceTPIDConfigTable.setStatus(_A)
_FsQinQIfServiceTPIDConfigEntry_Object=MibTableRow
fsQinQIfServiceTPIDConfigEntry=_FsQinQIfServiceTPIDConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,3,1))
fsQinQIfServiceTPIDConfigEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:fsQinQIfServiceTPIDConfigEntry.setStatus(_A)
_FsQinQIfServiceTPIDConfigIfIndex_Type=IfIndex
_FsQinQIfServiceTPIDConfigIfIndex_Object=MibTableColumn
fsQinQIfServiceTPIDConfigIfIndex=_FsQinQIfServiceTPIDConfigIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,3,1,1),_FsQinQIfServiceTPIDConfigIfIndex_Type())
fsQinQIfServiceTPIDConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQinQIfServiceTPIDConfigIfIndex.setStatus(_A)
class _FsQinQIfServiceTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsQinQIfServiceTPIDValue_Type.__name__=_C
_FsQinQIfServiceTPIDValue_Object=MibTableColumn
fsQinQIfServiceTPIDValue=_FsQinQIfServiceTPIDValue_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,3,1,2),_FsQinQIfServiceTPIDValue_Type())
fsQinQIfServiceTPIDValue.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQinQIfServiceTPIDValue.setStatus(_A)
_FsQinQPriorityCopyTable_Object=MibTable
fsQinQPriorityCopyTable=_FsQinQPriorityCopyTable_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,4))
if mibBuilder.loadTexts:fsQinQPriorityCopyTable.setStatus(_A)
_FsQinQPriorityCopyEntry_Object=MibTableRow
fsQinQPriorityCopyEntry=_FsQinQPriorityCopyEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,4,1))
fsQinQPriorityCopyEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:fsQinQPriorityCopyEntry.setStatus(_A)
_FsQinQPriorityCopyIfIndex_Type=IfIndex
_FsQinQPriorityCopyIfIndex_Object=MibTableColumn
fsQinQPriorityCopyIfIndex=_FsQinQPriorityCopyIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,4,1,1),_FsQinQPriorityCopyIfIndex_Type())
fsQinQPriorityCopyIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQinQPriorityCopyIfIndex.setStatus(_A)
_FsQinQPriorityCopyPortStatus_Type=EnabledStatus
_FsQinQPriorityCopyPortStatus_Object=MibTableColumn
fsQinQPriorityCopyPortStatus=_FsQinQPriorityCopyPortStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,4,1,2),_FsQinQPriorityCopyPortStatus_Type())
fsQinQPriorityCopyPortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsQinQPriorityCopyPortStatus.setStatus(_A)
_FsQinQPriorityRemarkTable_Object=MibTable
fsQinQPriorityRemarkTable=_FsQinQPriorityRemarkTable_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,5))
if mibBuilder.loadTexts:fsQinQPriorityRemarkTable.setStatus(_A)
_FsQinQPriorityRemarkEntry_Object=MibTableRow
fsQinQPriorityRemarkEntry=_FsQinQPriorityRemarkEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,5,1))
fsQinQPriorityRemarkEntry.setIndexNames((0,_B,_Q),(0,_B,_G))
if mibBuilder.loadTexts:fsQinQPriorityRemarkEntry.setStatus(_A)
_FsQinQPriorityRemarkIfIndex_Type=IfIndex
_FsQinQPriorityRemarkIfIndex_Object=MibTableColumn
fsQinQPriorityRemarkIfIndex=_FsQinQPriorityRemarkIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,5,1,1),_FsQinQPriorityRemarkIfIndex_Type())
fsQinQPriorityRemarkIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQinQPriorityRemarkIfIndex.setStatus(_A)
class _FsQinQPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQinQPriorityValue_Type.__name__=_C
_FsQinQPriorityValue_Object=MibTableColumn
fsQinQPriorityValue=_FsQinQPriorityValue_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,5,1,2),_FsQinQPriorityValue_Type())
fsQinQPriorityValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsQinQPriorityValue.setStatus(_A)
class _FsQinQPriorityRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsQinQPriorityRemarkValue_Type.__name__=_C
_FsQinQPriorityRemarkValue_Object=MibTableColumn
fsQinQPriorityRemarkValue=_FsQinQPriorityRemarkValue_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,5,1,3),_FsQinQPriorityRemarkValue_Type())
fsQinQPriorityRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsQinQPriorityRemarkValue.setStatus(_A)
_FsselectiveQinQBasedOnVlanTable_Object=MibTable
fsselectiveQinQBasedOnVlanTable=_FsselectiveQinQBasedOnVlanTable_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,6))
if mibBuilder.loadTexts:fsselectiveQinQBasedOnVlanTable.setStatus(_A)
_FsselectiveQinQBasedOnVlanEntry_Object=MibTableRow
fsselectiveQinQBasedOnVlanEntry=_FsselectiveQinQBasedOnVlanEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,6,1))
fsselectiveQinQBasedOnVlanEntry.setIndexNames((0,_B,_R),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:fsselectiveQinQBasedOnVlanEntry.setStatus(_A)
_FsselectiveQinQBasedOnVlanIfIndex_Type=IfIndex
_FsselectiveQinQBasedOnVlanIfIndex_Object=MibTableColumn
fsselectiveQinQBasedOnVlanIfIndex=_FsselectiveQinQBasedOnVlanIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,6,1,1),_FsselectiveQinQBasedOnVlanIfIndex_Type())
fsselectiveQinQBasedOnVlanIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsselectiveQinQBasedOnVlanIfIndex.setStatus(_A)
class _FsselectiveQinQBasedOnVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('modifyOuterTagBaseInnerTag',2),('modifyOuterTagBaseOuterTag',3),('modifyOuterTagBaseInnerAndOuterTag',4)))
_FsselectiveQinQBasedOnVlanType_Type.__name__=_C
_FsselectiveQinQBasedOnVlanType_Object=MibTableColumn
fsselectiveQinQBasedOnVlanType=_FsselectiveQinQBasedOnVlanType_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,6,1,2),_FsselectiveQinQBasedOnVlanType_Type())
fsselectiveQinQBasedOnVlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsselectiveQinQBasedOnVlanType.setStatus(_A)
class _FsselectiveQinQBasedOnVlanOuterVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsselectiveQinQBasedOnVlanOuterVlanID_Type.__name__=_C
_FsselectiveQinQBasedOnVlanOuterVlanID_Object=MibTableColumn
fsselectiveQinQBasedOnVlanOuterVlanID=_FsselectiveQinQBasedOnVlanOuterVlanID_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,6,1,3),_FsselectiveQinQBasedOnVlanOuterVlanID_Type())
fsselectiveQinQBasedOnVlanOuterVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsselectiveQinQBasedOnVlanOuterVlanID.setStatus(_A)
class _FsselectiveQinQBasedOnVlanOldOuterVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsselectiveQinQBasedOnVlanOldOuterVlanID_Type.__name__=_C
_FsselectiveQinQBasedOnVlanOldOuterVlanID_Object=MibTableColumn
fsselectiveQinQBasedOnVlanOldOuterVlanID=_FsselectiveQinQBasedOnVlanOldOuterVlanID_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,6,1,4),_FsselectiveQinQBasedOnVlanOldOuterVlanID_Type())
fsselectiveQinQBasedOnVlanOldOuterVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsselectiveQinQBasedOnVlanOldOuterVlanID.setStatus(_A)
_FsselectiveQinQBasedOnVlanVlanList_Type=VlanList
_FsselectiveQinQBasedOnVlanVlanList_Object=MibTableColumn
fsselectiveQinQBasedOnVlanVlanList=_FsselectiveQinQBasedOnVlanVlanList_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,6,1,5),_FsselectiveQinQBasedOnVlanVlanList_Type())
fsselectiveQinQBasedOnVlanVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsselectiveQinQBasedOnVlanVlanList.setStatus(_A)
_FsselectiveQinQBasedOnAclTable_Object=MibTable
fsselectiveQinQBasedOnAclTable=_FsselectiveQinQBasedOnAclTable_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,7))
if mibBuilder.loadTexts:fsselectiveQinQBasedOnAclTable.setStatus(_A)
_FsselectiveQinQBasedOnAclEntry_Object=MibTableRow
fsselectiveQinQBasedOnAclEntry=_FsselectiveQinQBasedOnAclEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,7,1))
fsselectiveQinQBasedOnAclEntry.setIndexNames((0,_B,_T),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:fsselectiveQinQBasedOnAclEntry.setStatus(_A)
_FsselectiveQinQBasedOnAclIfIndex_Type=IfIndex
_FsselectiveQinQBasedOnAclIfIndex_Object=MibTableColumn
fsselectiveQinQBasedOnAclIfIndex=_FsselectiveQinQBasedOnAclIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,7,1,1),_FsselectiveQinQBasedOnAclIfIndex_Type())
fsselectiveQinQBasedOnAclIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsselectiveQinQBasedOnAclIfIndex.setStatus(_A)
class _FsselectiveQinQBasedOnAclType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('modifyOuterTag',2),('modifyInnerTag',3)))
_FsselectiveQinQBasedOnAclType_Type.__name__=_C
_FsselectiveQinQBasedOnAclType_Object=MibTableColumn
fsselectiveQinQBasedOnAclType=_FsselectiveQinQBasedOnAclType_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,7,1,2),_FsselectiveQinQBasedOnAclType_Type())
fsselectiveQinQBasedOnAclType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsselectiveQinQBasedOnAclType.setStatus(_A)
_FsselectiveQinQBasedOnAclAclID_Type=Integer32
_FsselectiveQinQBasedOnAclAclID_Object=MibTableColumn
fsselectiveQinQBasedOnAclAclID=_FsselectiveQinQBasedOnAclAclID_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,7,1,3),_FsselectiveQinQBasedOnAclAclID_Type())
fsselectiveQinQBasedOnAclAclID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsselectiveQinQBasedOnAclAclID.setStatus(_A)
class _FsselectiveQinQBasedOnAclVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsselectiveQinQBasedOnAclVlanID_Type.__name__=_C
_FsselectiveQinQBasedOnAclVlanID_Object=MibTableColumn
fsselectiveQinQBasedOnAclVlanID=_FsselectiveQinQBasedOnAclVlanID_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,7,1,4),_FsselectiveQinQBasedOnAclVlanID_Type())
fsselectiveQinQBasedOnAclVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsselectiveQinQBasedOnAclVlanID.setStatus(_A)
_FsQinQVlanMappingTable_Object=MibTable
fsQinQVlanMappingTable=_FsQinQVlanMappingTable_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,8))
if mibBuilder.loadTexts:fsQinQVlanMappingTable.setStatus(_A)
_FsQinQVlanMappingEntry_Object=MibTableRow
fsQinQVlanMappingEntry=_FsQinQVlanMappingEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,8,1))
fsQinQVlanMappingEntry.setIndexNames((0,_B,_U),(0,_B,_V),(0,_B,_M))
if mibBuilder.loadTexts:fsQinQVlanMappingEntry.setStatus(_A)
_FsQinQVlanMappingIfIndex_Type=IfIndex
_FsQinQVlanMappingIfIndex_Object=MibTableColumn
fsQinQVlanMappingIfIndex=_FsQinQVlanMappingIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,8,1,1),_FsQinQVlanMappingIfIndex_Type())
fsQinQVlanMappingIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQinQVlanMappingIfIndex.setStatus(_A)
class _FsQinQVlanMappingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlanMappingIn',1),('vlanMappingOut',2)))
_FsQinQVlanMappingType_Type.__name__=_C
_FsQinQVlanMappingType_Object=MibTableColumn
fsQinQVlanMappingType=_FsQinQVlanMappingType_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,8,1,2),_FsQinQVlanMappingType_Type())
fsQinQVlanMappingType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsQinQVlanMappingType.setStatus(_A)
class _FsQinQVlanMappingNewVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsQinQVlanMappingNewVlanID_Type.__name__=_C
_FsQinQVlanMappingNewVlanID_Object=MibTableColumn
fsQinQVlanMappingNewVlanID=_FsQinQVlanMappingNewVlanID_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,8,1,3),_FsQinQVlanMappingNewVlanID_Type())
fsQinQVlanMappingNewVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsQinQVlanMappingNewVlanID.setStatus(_A)
_FsQinQVlanMappingOldVlanList_Type=VlanList
_FsQinQVlanMappingOldVlanList_Object=MibTableColumn
fsQinQVlanMappingOldVlanList=_FsQinQVlanMappingOldVlanList_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,8,1,4),_FsQinQVlanMappingOldVlanList_Type())
fsQinQVlanMappingOldVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsQinQVlanMappingOldVlanList.setStatus(_A)
class _FsQinQVlanMappingOldVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsQinQVlanMappingOldVlanID_Type.__name__=_C
_FsQinQVlanMappingOldVlanID_Object=MibTableColumn
fsQinQVlanMappingOldVlanID=_FsQinQVlanMappingOldVlanID_Object((1,3,6,1,4,1,52642,1,1,10,2,53,1,8,1,5),_FsQinQVlanMappingOldVlanID_Type())
fsQinQVlanMappingOldVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsQinQVlanMappingOldVlanID.setStatus(_A)
_FsQinQMIBConformance_ObjectIdentity=ObjectIdentity
fsQinQMIBConformance=_FsQinQMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,53,2))
_FsQinQMIBCompliances_ObjectIdentity=ObjectIdentity
fsQinQMIBCompliances=_FsQinQMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,53,2,1))
_FsQinQMIBGroups_ObjectIdentity=ObjectIdentity
fsQinQMIBGroups=_FsQinQMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,53,2,2))
fsQinQMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,53,2,2,1))
fsQinQMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_G),(_B,_d),(_B,_H),(_B,_I),(_B,_J),(_B,_e),(_B,_K),(_B,_L),(_B,_f),(_B,_M)))
if mibBuilder.loadTexts:fsQinQMIBGroup.setStatus(_A)
fsQinQMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,53,2,1,1))
fsQinQMIBCompliance.setObjects((_B,_g))
if mibBuilder.loadTexts:fsQinQMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VlanList':VlanList,'fsQinQMIB':fsQinQMIB,'fsQINQMIBObjects':fsQINQMIBObjects,'fsQinQPortConfigTable':fsQinQPortConfigTable,'fsQinQPortConfigEntry':fsQinQPortConfigEntry,_N:fsQinQPortConfigIndex,_W:fsQinQPortConfigMode,_X:fsQinQPortNativeVlan,_Y:fsQinQPortAllowedUntagVlanList,_Z:fsQinQPortAllowedTagVlanList,_a:fsQinQServiceTPIDValue,'fsQinQIfServiceTPIDConfigTable':fsQinQIfServiceTPIDConfigTable,'fsQinQIfServiceTPIDConfigEntry':fsQinQIfServiceTPIDConfigEntry,_O:fsQinQIfServiceTPIDConfigIfIndex,_b:fsQinQIfServiceTPIDValue,'fsQinQPriorityCopyTable':fsQinQPriorityCopyTable,'fsQinQPriorityCopyEntry':fsQinQPriorityCopyEntry,_P:fsQinQPriorityCopyIfIndex,_c:fsQinQPriorityCopyPortStatus,'fsQinQPriorityRemarkTable':fsQinQPriorityRemarkTable,'fsQinQPriorityRemarkEntry':fsQinQPriorityRemarkEntry,_Q:fsQinQPriorityRemarkIfIndex,_G:fsQinQPriorityValue,_d:fsQinQPriorityRemarkValue,'fsselectiveQinQBasedOnVlanTable':fsselectiveQinQBasedOnVlanTable,'fsselectiveQinQBasedOnVlanEntry':fsselectiveQinQBasedOnVlanEntry,_R:fsselectiveQinQBasedOnVlanIfIndex,_H:fsselectiveQinQBasedOnVlanType,_I:fsselectiveQinQBasedOnVlanOuterVlanID,_J:fsselectiveQinQBasedOnVlanOldOuterVlanID,_e:fsselectiveQinQBasedOnVlanVlanList,'fsselectiveQinQBasedOnAclTable':fsselectiveQinQBasedOnAclTable,'fsselectiveQinQBasedOnAclEntry':fsselectiveQinQBasedOnAclEntry,_T:fsselectiveQinQBasedOnAclIfIndex,_K:fsselectiveQinQBasedOnAclType,_L:fsselectiveQinQBasedOnAclAclID,_f:fsselectiveQinQBasedOnAclVlanID,'fsQinQVlanMappingTable':fsQinQVlanMappingTable,'fsQinQVlanMappingEntry':fsQinQVlanMappingEntry,_U:fsQinQVlanMappingIfIndex,_V:fsQinQVlanMappingType,_M:fsQinQVlanMappingNewVlanID,'fsQinQVlanMappingOldVlanList':fsQinQVlanMappingOldVlanList,'fsQinQVlanMappingOldVlanID':fsQinQVlanMappingOldVlanID,'fsQinQMIBConformance':fsQinQMIBConformance,'fsQinQMIBCompliances':fsQinQMIBCompliances,'fsQinQMIBCompliance':fsQinQMIBCompliance,'fsQinQMIBGroups':fsQinQMIBGroups,_g:fsQinQMIBGroup})