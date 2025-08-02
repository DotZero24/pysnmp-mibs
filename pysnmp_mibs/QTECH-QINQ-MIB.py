_g='qtechQinQMIBGroup'
_f='qtechselectiveQinQBasedOnAclVlanID'
_e='qtechselectiveQinQBasedOnVlanVlanList'
_d='qtechQinQPriorityRemarkValue'
_c='qtechQinQPriorityCopyPortStatus'
_b='qtechQinQIfServiceTPIDValue'
_a='qtechQinQServiceTPIDValue'
_Z='qtechQinQPortAllowedTagVlanList'
_Y='qtechQinQPortAllowedUntagVlanList'
_X='qtechQinQPortNativeVlan'
_W='qtechQinQPortConfigMode'
_V='qtechQinQVlanMappingType'
_U='qtechQinQVlanMappingIfIndex'
_T='qtechselectiveQinQBasedOnAclIfIndex'
_S='addOuterTag'
_R='qtechselectiveQinQBasedOnVlanIfIndex'
_Q='qtechQinQPriorityRemarkIfIndex'
_P='qtechQinQPriorityCopyIfIndex'
_O='qtechQinQIfServiceTPIDConfigIfIndex'
_N='qtechQinQPortConfigIndex'
_M='qtechQinQVlanMappingNewVlanID'
_L='qtechselectiveQinQBasedOnAclAclID'
_K='qtechselectiveQinQBasedOnAclType'
_J='qtechselectiveQinQBasedOnVlanOldOuterVlanID'
_I='qtechselectiveQinQBasedOnVlanOuterVlanID'
_H='qtechselectiveQinQBasedOnVlanType'
_G='qtechQinQPriorityValue'
_F='read-write'
_E='not-accessible'
_D='read-only'
_C='Integer32'
_B='QTECH-QINQ-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechQinQMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,53))
if mibBuilder.loadTexts:qtechQinQMIB.setRevisions(('2009-09-09 00:00',))
class VlanList(TextualConvention,OctetString):status=_A
_QtechQINQMIBObjects_ObjectIdentity=ObjectIdentity
qtechQINQMIBObjects=_QtechQINQMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,53,1))
_QtechQinQPortConfigTable_Object=MibTable
qtechQinQPortConfigTable=_QtechQinQPortConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,1))
if mibBuilder.loadTexts:qtechQinQPortConfigTable.setStatus(_A)
_QtechQinQPortConfigEntry_Object=MibTableRow
qtechQinQPortConfigEntry=_QtechQinQPortConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,1,1))
qtechQinQPortConfigEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:qtechQinQPortConfigEntry.setStatus(_A)
_QtechQinQPortConfigIndex_Type=IfIndex
_QtechQinQPortConfigIndex_Object=MibTableColumn
qtechQinQPortConfigIndex=_QtechQinQPortConfigIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,1,1,1),_QtechQinQPortConfigIndex_Type())
qtechQinQPortConfigIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQinQPortConfigIndex.setStatus(_A)
class _QtechQinQPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('dot1q-tunnel',2)))
_QtechQinQPortConfigMode_Type.__name__=_C
_QtechQinQPortConfigMode_Object=MibTableColumn
qtechQinQPortConfigMode=_QtechQinQPortConfigMode_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,1,1,2),_QtechQinQPortConfigMode_Type())
qtechQinQPortConfigMode.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechQinQPortConfigMode.setStatus(_A)
_QtechQinQPortNativeVlan_Type=VlanId
_QtechQinQPortNativeVlan_Object=MibTableColumn
qtechQinQPortNativeVlan=_QtechQinQPortNativeVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,1,1,3),_QtechQinQPortNativeVlan_Type())
qtechQinQPortNativeVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechQinQPortNativeVlan.setStatus(_A)
_QtechQinQPortAllowedUntagVlanList_Type=VlanList
_QtechQinQPortAllowedUntagVlanList_Object=MibTableColumn
qtechQinQPortAllowedUntagVlanList=_QtechQinQPortAllowedUntagVlanList_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,1,1,4),_QtechQinQPortAllowedUntagVlanList_Type())
qtechQinQPortAllowedUntagVlanList.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechQinQPortAllowedUntagVlanList.setStatus(_A)
_QtechQinQPortAllowedTagVlanList_Type=VlanList
_QtechQinQPortAllowedTagVlanList_Object=MibTableColumn
qtechQinQPortAllowedTagVlanList=_QtechQinQPortAllowedTagVlanList_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,1,1,5),_QtechQinQPortAllowedTagVlanList_Type())
qtechQinQPortAllowedTagVlanList.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechQinQPortAllowedTagVlanList.setStatus(_A)
class _QtechQinQServiceTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QtechQinQServiceTPIDValue_Type.__name__=_C
_QtechQinQServiceTPIDValue_Object=MibScalar
qtechQinQServiceTPIDValue=_QtechQinQServiceTPIDValue_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,2),_QtechQinQServiceTPIDValue_Type())
qtechQinQServiceTPIDValue.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechQinQServiceTPIDValue.setStatus(_A)
_QtechQinQIfServiceTPIDConfigTable_Object=MibTable
qtechQinQIfServiceTPIDConfigTable=_QtechQinQIfServiceTPIDConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,3))
if mibBuilder.loadTexts:qtechQinQIfServiceTPIDConfigTable.setStatus(_A)
_QtechQinQIfServiceTPIDConfigEntry_Object=MibTableRow
qtechQinQIfServiceTPIDConfigEntry=_QtechQinQIfServiceTPIDConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,3,1))
qtechQinQIfServiceTPIDConfigEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:qtechQinQIfServiceTPIDConfigEntry.setStatus(_A)
_QtechQinQIfServiceTPIDConfigIfIndex_Type=IfIndex
_QtechQinQIfServiceTPIDConfigIfIndex_Object=MibTableColumn
qtechQinQIfServiceTPIDConfigIfIndex=_QtechQinQIfServiceTPIDConfigIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,3,1,1),_QtechQinQIfServiceTPIDConfigIfIndex_Type())
qtechQinQIfServiceTPIDConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQinQIfServiceTPIDConfigIfIndex.setStatus(_A)
class _QtechQinQIfServiceTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QtechQinQIfServiceTPIDValue_Type.__name__=_C
_QtechQinQIfServiceTPIDValue_Object=MibTableColumn
qtechQinQIfServiceTPIDValue=_QtechQinQIfServiceTPIDValue_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,3,1,2),_QtechQinQIfServiceTPIDValue_Type())
qtechQinQIfServiceTPIDValue.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechQinQIfServiceTPIDValue.setStatus(_A)
_QtechQinQPriorityCopyTable_Object=MibTable
qtechQinQPriorityCopyTable=_QtechQinQPriorityCopyTable_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,4))
if mibBuilder.loadTexts:qtechQinQPriorityCopyTable.setStatus(_A)
_QtechQinQPriorityCopyEntry_Object=MibTableRow
qtechQinQPriorityCopyEntry=_QtechQinQPriorityCopyEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,4,1))
qtechQinQPriorityCopyEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:qtechQinQPriorityCopyEntry.setStatus(_A)
_QtechQinQPriorityCopyIfIndex_Type=IfIndex
_QtechQinQPriorityCopyIfIndex_Object=MibTableColumn
qtechQinQPriorityCopyIfIndex=_QtechQinQPriorityCopyIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,4,1,1),_QtechQinQPriorityCopyIfIndex_Type())
qtechQinQPriorityCopyIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQinQPriorityCopyIfIndex.setStatus(_A)
_QtechQinQPriorityCopyPortStatus_Type=EnabledStatus
_QtechQinQPriorityCopyPortStatus_Object=MibTableColumn
qtechQinQPriorityCopyPortStatus=_QtechQinQPriorityCopyPortStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,4,1,2),_QtechQinQPriorityCopyPortStatus_Type())
qtechQinQPriorityCopyPortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechQinQPriorityCopyPortStatus.setStatus(_A)
_QtechQinQPriorityRemarkTable_Object=MibTable
qtechQinQPriorityRemarkTable=_QtechQinQPriorityRemarkTable_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,5))
if mibBuilder.loadTexts:qtechQinQPriorityRemarkTable.setStatus(_A)
_QtechQinQPriorityRemarkEntry_Object=MibTableRow
qtechQinQPriorityRemarkEntry=_QtechQinQPriorityRemarkEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,5,1))
qtechQinQPriorityRemarkEntry.setIndexNames((0,_B,_Q),(0,_B,_G))
if mibBuilder.loadTexts:qtechQinQPriorityRemarkEntry.setStatus(_A)
_QtechQinQPriorityRemarkIfIndex_Type=IfIndex
_QtechQinQPriorityRemarkIfIndex_Object=MibTableColumn
qtechQinQPriorityRemarkIfIndex=_QtechQinQPriorityRemarkIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,5,1,1),_QtechQinQPriorityRemarkIfIndex_Type())
qtechQinQPriorityRemarkIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQinQPriorityRemarkIfIndex.setStatus(_A)
class _QtechQinQPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechQinQPriorityValue_Type.__name__=_C
_QtechQinQPriorityValue_Object=MibTableColumn
qtechQinQPriorityValue=_QtechQinQPriorityValue_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,5,1,2),_QtechQinQPriorityValue_Type())
qtechQinQPriorityValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechQinQPriorityValue.setStatus(_A)
class _QtechQinQPriorityRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechQinQPriorityRemarkValue_Type.__name__=_C
_QtechQinQPriorityRemarkValue_Object=MibTableColumn
qtechQinQPriorityRemarkValue=_QtechQinQPriorityRemarkValue_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,5,1,3),_QtechQinQPriorityRemarkValue_Type())
qtechQinQPriorityRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechQinQPriorityRemarkValue.setStatus(_A)
_QtechselectiveQinQBasedOnVlanTable_Object=MibTable
qtechselectiveQinQBasedOnVlanTable=_QtechselectiveQinQBasedOnVlanTable_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,6))
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnVlanTable.setStatus(_A)
_QtechselectiveQinQBasedOnVlanEntry_Object=MibTableRow
qtechselectiveQinQBasedOnVlanEntry=_QtechselectiveQinQBasedOnVlanEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,6,1))
qtechselectiveQinQBasedOnVlanEntry.setIndexNames((0,_B,_R),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnVlanEntry.setStatus(_A)
_QtechselectiveQinQBasedOnVlanIfIndex_Type=IfIndex
_QtechselectiveQinQBasedOnVlanIfIndex_Object=MibTableColumn
qtechselectiveQinQBasedOnVlanIfIndex=_QtechselectiveQinQBasedOnVlanIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,6,1,1),_QtechselectiveQinQBasedOnVlanIfIndex_Type())
qtechselectiveQinQBasedOnVlanIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnVlanIfIndex.setStatus(_A)
class _QtechselectiveQinQBasedOnVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('modifyOuterTagBaseInnerTag',2),('modifyOuterTagBaseOuterTag',3),('modifyOuterTagBaseInnerAndOuterTag',4)))
_QtechselectiveQinQBasedOnVlanType_Type.__name__=_C
_QtechselectiveQinQBasedOnVlanType_Object=MibTableColumn
qtechselectiveQinQBasedOnVlanType=_QtechselectiveQinQBasedOnVlanType_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,6,1,2),_QtechselectiveQinQBasedOnVlanType_Type())
qtechselectiveQinQBasedOnVlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnVlanType.setStatus(_A)
class _QtechselectiveQinQBasedOnVlanOuterVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QtechselectiveQinQBasedOnVlanOuterVlanID_Type.__name__=_C
_QtechselectiveQinQBasedOnVlanOuterVlanID_Object=MibTableColumn
qtechselectiveQinQBasedOnVlanOuterVlanID=_QtechselectiveQinQBasedOnVlanOuterVlanID_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,6,1,3),_QtechselectiveQinQBasedOnVlanOuterVlanID_Type())
qtechselectiveQinQBasedOnVlanOuterVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnVlanOuterVlanID.setStatus(_A)
class _QtechselectiveQinQBasedOnVlanOldOuterVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QtechselectiveQinQBasedOnVlanOldOuterVlanID_Type.__name__=_C
_QtechselectiveQinQBasedOnVlanOldOuterVlanID_Object=MibTableColumn
qtechselectiveQinQBasedOnVlanOldOuterVlanID=_QtechselectiveQinQBasedOnVlanOldOuterVlanID_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,6,1,4),_QtechselectiveQinQBasedOnVlanOldOuterVlanID_Type())
qtechselectiveQinQBasedOnVlanOldOuterVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnVlanOldOuterVlanID.setStatus(_A)
_QtechselectiveQinQBasedOnVlanVlanList_Type=VlanList
_QtechselectiveQinQBasedOnVlanVlanList_Object=MibTableColumn
qtechselectiveQinQBasedOnVlanVlanList=_QtechselectiveQinQBasedOnVlanVlanList_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,6,1,5),_QtechselectiveQinQBasedOnVlanVlanList_Type())
qtechselectiveQinQBasedOnVlanVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnVlanVlanList.setStatus(_A)
_QtechselectiveQinQBasedOnAclTable_Object=MibTable
qtechselectiveQinQBasedOnAclTable=_QtechselectiveQinQBasedOnAclTable_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,7))
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnAclTable.setStatus(_A)
_QtechselectiveQinQBasedOnAclEntry_Object=MibTableRow
qtechselectiveQinQBasedOnAclEntry=_QtechselectiveQinQBasedOnAclEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,7,1))
qtechselectiveQinQBasedOnAclEntry.setIndexNames((0,_B,_T),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnAclEntry.setStatus(_A)
_QtechselectiveQinQBasedOnAclIfIndex_Type=IfIndex
_QtechselectiveQinQBasedOnAclIfIndex_Object=MibTableColumn
qtechselectiveQinQBasedOnAclIfIndex=_QtechselectiveQinQBasedOnAclIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,7,1,1),_QtechselectiveQinQBasedOnAclIfIndex_Type())
qtechselectiveQinQBasedOnAclIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnAclIfIndex.setStatus(_A)
class _QtechselectiveQinQBasedOnAclType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('modifyOuterTag',2),('modifyInnerTag',3)))
_QtechselectiveQinQBasedOnAclType_Type.__name__=_C
_QtechselectiveQinQBasedOnAclType_Object=MibTableColumn
qtechselectiveQinQBasedOnAclType=_QtechselectiveQinQBasedOnAclType_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,7,1,2),_QtechselectiveQinQBasedOnAclType_Type())
qtechselectiveQinQBasedOnAclType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnAclType.setStatus(_A)
_QtechselectiveQinQBasedOnAclAclID_Type=Integer32
_QtechselectiveQinQBasedOnAclAclID_Object=MibTableColumn
qtechselectiveQinQBasedOnAclAclID=_QtechselectiveQinQBasedOnAclAclID_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,7,1,3),_QtechselectiveQinQBasedOnAclAclID_Type())
qtechselectiveQinQBasedOnAclAclID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnAclAclID.setStatus(_A)
class _QtechselectiveQinQBasedOnAclVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QtechselectiveQinQBasedOnAclVlanID_Type.__name__=_C
_QtechselectiveQinQBasedOnAclVlanID_Object=MibTableColumn
qtechselectiveQinQBasedOnAclVlanID=_QtechselectiveQinQBasedOnAclVlanID_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,7,1,4),_QtechselectiveQinQBasedOnAclVlanID_Type())
qtechselectiveQinQBasedOnAclVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechselectiveQinQBasedOnAclVlanID.setStatus(_A)
_QtechQinQVlanMappingTable_Object=MibTable
qtechQinQVlanMappingTable=_QtechQinQVlanMappingTable_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,8))
if mibBuilder.loadTexts:qtechQinQVlanMappingTable.setStatus(_A)
_QtechQinQVlanMappingEntry_Object=MibTableRow
qtechQinQVlanMappingEntry=_QtechQinQVlanMappingEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,8,1))
qtechQinQVlanMappingEntry.setIndexNames((0,_B,_U),(0,_B,_V),(0,_B,_M))
if mibBuilder.loadTexts:qtechQinQVlanMappingEntry.setStatus(_A)
_QtechQinQVlanMappingIfIndex_Type=IfIndex
_QtechQinQVlanMappingIfIndex_Object=MibTableColumn
qtechQinQVlanMappingIfIndex=_QtechQinQVlanMappingIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,8,1,1),_QtechQinQVlanMappingIfIndex_Type())
qtechQinQVlanMappingIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQinQVlanMappingIfIndex.setStatus(_A)
class _QtechQinQVlanMappingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlanMappingIn',1),('vlanMappingOut',2)))
_QtechQinQVlanMappingType_Type.__name__=_C
_QtechQinQVlanMappingType_Object=MibTableColumn
qtechQinQVlanMappingType=_QtechQinQVlanMappingType_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,8,1,2),_QtechQinQVlanMappingType_Type())
qtechQinQVlanMappingType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechQinQVlanMappingType.setStatus(_A)
class _QtechQinQVlanMappingNewVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QtechQinQVlanMappingNewVlanID_Type.__name__=_C
_QtechQinQVlanMappingNewVlanID_Object=MibTableColumn
qtechQinQVlanMappingNewVlanID=_QtechQinQVlanMappingNewVlanID_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,8,1,3),_QtechQinQVlanMappingNewVlanID_Type())
qtechQinQVlanMappingNewVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechQinQVlanMappingNewVlanID.setStatus(_A)
_QtechQinQVlanMappingOldVlanList_Type=VlanList
_QtechQinQVlanMappingOldVlanList_Object=MibTableColumn
qtechQinQVlanMappingOldVlanList=_QtechQinQVlanMappingOldVlanList_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,8,1,4),_QtechQinQVlanMappingOldVlanList_Type())
qtechQinQVlanMappingOldVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechQinQVlanMappingOldVlanList.setStatus(_A)
class _QtechQinQVlanMappingOldVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QtechQinQVlanMappingOldVlanID_Type.__name__=_C
_QtechQinQVlanMappingOldVlanID_Object=MibTableColumn
qtechQinQVlanMappingOldVlanID=_QtechQinQVlanMappingOldVlanID_Object((1,3,6,1,4,1,27514,1,1,10,2,53,1,8,1,5),_QtechQinQVlanMappingOldVlanID_Type())
qtechQinQVlanMappingOldVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechQinQVlanMappingOldVlanID.setStatus(_A)
_QtechQinQMIBConformance_ObjectIdentity=ObjectIdentity
qtechQinQMIBConformance=_QtechQinQMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,53,2))
_QtechQinQMIBCompliances_ObjectIdentity=ObjectIdentity
qtechQinQMIBCompliances=_QtechQinQMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,53,2,1))
_QtechQinQMIBGroups_ObjectIdentity=ObjectIdentity
qtechQinQMIBGroups=_QtechQinQMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,53,2,2))
qtechQinQMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,53,2,2,1))
qtechQinQMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_G),(_B,_d),(_B,_H),(_B,_I),(_B,_J),(_B,_e),(_B,_K),(_B,_L),(_B,_f),(_B,_M)))
if mibBuilder.loadTexts:qtechQinQMIBGroup.setStatus(_A)
qtechQinQMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,53,2,1,1))
qtechQinQMIBCompliance.setObjects((_B,_g))
if mibBuilder.loadTexts:qtechQinQMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VlanList':VlanList,'qtechQinQMIB':qtechQinQMIB,'qtechQINQMIBObjects':qtechQINQMIBObjects,'qtechQinQPortConfigTable':qtechQinQPortConfigTable,'qtechQinQPortConfigEntry':qtechQinQPortConfigEntry,_N:qtechQinQPortConfigIndex,_W:qtechQinQPortConfigMode,_X:qtechQinQPortNativeVlan,_Y:qtechQinQPortAllowedUntagVlanList,_Z:qtechQinQPortAllowedTagVlanList,_a:qtechQinQServiceTPIDValue,'qtechQinQIfServiceTPIDConfigTable':qtechQinQIfServiceTPIDConfigTable,'qtechQinQIfServiceTPIDConfigEntry':qtechQinQIfServiceTPIDConfigEntry,_O:qtechQinQIfServiceTPIDConfigIfIndex,_b:qtechQinQIfServiceTPIDValue,'qtechQinQPriorityCopyTable':qtechQinQPriorityCopyTable,'qtechQinQPriorityCopyEntry':qtechQinQPriorityCopyEntry,_P:qtechQinQPriorityCopyIfIndex,_c:qtechQinQPriorityCopyPortStatus,'qtechQinQPriorityRemarkTable':qtechQinQPriorityRemarkTable,'qtechQinQPriorityRemarkEntry':qtechQinQPriorityRemarkEntry,_Q:qtechQinQPriorityRemarkIfIndex,_G:qtechQinQPriorityValue,_d:qtechQinQPriorityRemarkValue,'qtechselectiveQinQBasedOnVlanTable':qtechselectiveQinQBasedOnVlanTable,'qtechselectiveQinQBasedOnVlanEntry':qtechselectiveQinQBasedOnVlanEntry,_R:qtechselectiveQinQBasedOnVlanIfIndex,_H:qtechselectiveQinQBasedOnVlanType,_I:qtechselectiveQinQBasedOnVlanOuterVlanID,_J:qtechselectiveQinQBasedOnVlanOldOuterVlanID,_e:qtechselectiveQinQBasedOnVlanVlanList,'qtechselectiveQinQBasedOnAclTable':qtechselectiveQinQBasedOnAclTable,'qtechselectiveQinQBasedOnAclEntry':qtechselectiveQinQBasedOnAclEntry,_T:qtechselectiveQinQBasedOnAclIfIndex,_K:qtechselectiveQinQBasedOnAclType,_L:qtechselectiveQinQBasedOnAclAclID,_f:qtechselectiveQinQBasedOnAclVlanID,'qtechQinQVlanMappingTable':qtechQinQVlanMappingTable,'qtechQinQVlanMappingEntry':qtechQinQVlanMappingEntry,_U:qtechQinQVlanMappingIfIndex,_V:qtechQinQVlanMappingType,_M:qtechQinQVlanMappingNewVlanID,'qtechQinQVlanMappingOldVlanList':qtechQinQVlanMappingOldVlanList,'qtechQinQVlanMappingOldVlanID':qtechQinQVlanMappingOldVlanID,'qtechQinQMIBConformance':qtechQinQMIBConformance,'qtechQinQMIBCompliances':qtechQinQMIBCompliances,'qtechQinQMIBCompliance':qtechQinQMIBCompliance,'qtechQinQMIBGroups':qtechQinQMIBGroups,_g:qtechQinQMIBGroup})