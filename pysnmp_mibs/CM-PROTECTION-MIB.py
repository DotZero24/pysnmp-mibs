_v='cmMSProtObjectGroup'
_u='cmProtObjectGroup'
_t='cmMSPUnitPort'
_s='cmMSPUnitState'
_r='cmMSPUnitType'
_q='cmMSPGroupMacAddress'
_p='cmMSPGroupRowStatus'
_o='cmMSPGroupStorageType'
_n='cmMSPGroupAction'
_m='cmMSPGroupStatus'
_l='cmMSPGroupProtPort'
_k='cmMSPGroupWorkPort'
_j='cmMSPGroupDirection'
_i='cmMSPGroupB2DEGTrigger'
_h='cmMSPGroupWaitToRestore'
_g='cmMSPGroupRevertive'
_f='cmMSPGroupSwitchMode'
_e='cmMSPGroupUserLabel'
_d='cmFacProtUnitPort'
_c='cmFacProtUnitState'
_b='cmFacProtUnitType'
_a='cmFacProtGroupMacAddress'
_Z='cmFacProtGroupRowStatus'
_Y='cmFacProtGroupStorageType'
_X='cmFacProtGroupAction'
_W='cmFacProtGroupStatus'
_V='cmFacProtGroupProtPort'
_U='cmFacProtGroupWorkPort'
_T='cmFacProtGroupDirection'
_S='cmFacProtGroupWaitToRestore'
_R='cmFacProtGroupRevertive'
_Q='cmFacProtGroupSwitchMode'
_P='cmFacProtGroupUserLabel'
_O='read-write'
_N='cmMSPUnitIndex'
_M='cmFacProtUnitIndex'
_L='DisplayString'
_K='Integer32'
_J='slotIndex'
_I='shelfIndex'
_H='cmMSPGroupIndex'
_G='cmFacProtGroupIndex'
_F='neIndex'
_E='CM-ENTITY-MIB'
_D='read-only'
_C='read-create'
_B='CM-PROTECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
neIndex,shelfIndex,slotIndex=mibBuilder.importSymbols(_E,_F,_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue','VariablePointer')
cmProtectionMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,7))
if mibBuilder.loadTexts:cmProtectionMIB.setRevisions(('2010-06-23 00:00',))
class CmProtSwitchMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('oneplusone',1),('dualactiverx',2),('universalring',3)))
class CmProtSwitchDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
class CmProtSwitchAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('releaseprotswitch',2),('manualfromworking',3),('forcedfromworking',4),('manualfromprotect',5),('forcedfromprotect',6),('lockoutfromprotect',7)))
class CmProtUnitType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('working',1),('protect',2)))
class CmProtUnitState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('standby',2)))
class CmProtGroupStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('nooutstandingreq',1),('sf-protect',2),('sf-working',3),('sd-protect',4),('sd-working',5),('manual-protect',6),('manual-working',7),('forced-protect',8),('forced-working',9),('lockout-protect',10),('waitToRestore',11)))
_CmProtObjects_ObjectIdentity=ObjectIdentity
cmProtObjects=_CmProtObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,7,1))
_CmFacProtGroupTable_Object=MibTable
cmFacProtGroupTable=_CmFacProtGroupTable_Object((1,3,6,1,4,1,2544,1,12,7,1,1))
if mibBuilder.loadTexts:cmFacProtGroupTable.setStatus(_A)
_CmFacProtGroupEntry_Object=MibTableRow
cmFacProtGroupEntry=_CmFacProtGroupEntry_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1))
cmFacProtGroupEntry.setIndexNames((0,_E,_F),(0,_E,_I),(0,_E,_J),(0,_B,_G))
if mibBuilder.loadTexts:cmFacProtGroupEntry.setStatus(_A)
_CmFacProtGroupIndex_Type=Integer32
_CmFacProtGroupIndex_Object=MibTableColumn
cmFacProtGroupIndex=_CmFacProtGroupIndex_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,1),_CmFacProtGroupIndex_Type())
cmFacProtGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cmFacProtGroupIndex.setStatus(_A)
class _CmFacProtGroupUserLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmFacProtGroupUserLabel_Type.__name__=_L
_CmFacProtGroupUserLabel_Object=MibTableColumn
cmFacProtGroupUserLabel=_CmFacProtGroupUserLabel_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,2),_CmFacProtGroupUserLabel_Type())
cmFacProtGroupUserLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFacProtGroupUserLabel.setStatus(_A)
_CmFacProtGroupSwitchMode_Type=CmProtSwitchMode
_CmFacProtGroupSwitchMode_Object=MibTableColumn
cmFacProtGroupSwitchMode=_CmFacProtGroupSwitchMode_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,3),_CmFacProtGroupSwitchMode_Type())
cmFacProtGroupSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFacProtGroupSwitchMode.setStatus(_A)
_CmFacProtGroupRevertive_Type=TruthValue
_CmFacProtGroupRevertive_Object=MibTableColumn
cmFacProtGroupRevertive=_CmFacProtGroupRevertive_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,4),_CmFacProtGroupRevertive_Type())
cmFacProtGroupRevertive.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFacProtGroupRevertive.setStatus(_A)
class _CmFacProtGroupWaitToRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60),ValueRangeConstraint(0,0))
_CmFacProtGroupWaitToRestore_Type.__name__=_K
_CmFacProtGroupWaitToRestore_Object=MibTableColumn
cmFacProtGroupWaitToRestore=_CmFacProtGroupWaitToRestore_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,5),_CmFacProtGroupWaitToRestore_Type())
cmFacProtGroupWaitToRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFacProtGroupWaitToRestore.setStatus(_A)
_CmFacProtGroupDirection_Type=CmProtSwitchDirection
_CmFacProtGroupDirection_Object=MibTableColumn
cmFacProtGroupDirection=_CmFacProtGroupDirection_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,6),_CmFacProtGroupDirection_Type())
cmFacProtGroupDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFacProtGroupDirection.setStatus(_A)
_CmFacProtGroupWorkPort_Type=VariablePointer
_CmFacProtGroupWorkPort_Object=MibTableColumn
cmFacProtGroupWorkPort=_CmFacProtGroupWorkPort_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,7),_CmFacProtGroupWorkPort_Type())
cmFacProtGroupWorkPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFacProtGroupWorkPort.setStatus(_A)
_CmFacProtGroupProtPort_Type=VariablePointer
_CmFacProtGroupProtPort_Object=MibTableColumn
cmFacProtGroupProtPort=_CmFacProtGroupProtPort_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,8),_CmFacProtGroupProtPort_Type())
cmFacProtGroupProtPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFacProtGroupProtPort.setStatus(_A)
_CmFacProtGroupStatus_Type=CmProtGroupStatus
_CmFacProtGroupStatus_Object=MibTableColumn
cmFacProtGroupStatus=_CmFacProtGroupStatus_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,9),_CmFacProtGroupStatus_Type())
cmFacProtGroupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cmFacProtGroupStatus.setStatus(_A)
_CmFacProtGroupAction_Type=CmProtSwitchAction
_CmFacProtGroupAction_Object=MibTableColumn
cmFacProtGroupAction=_CmFacProtGroupAction_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,10),_CmFacProtGroupAction_Type())
cmFacProtGroupAction.setMaxAccess(_O)
if mibBuilder.loadTexts:cmFacProtGroupAction.setStatus(_A)
_CmFacProtGroupStorageType_Type=StorageType
_CmFacProtGroupStorageType_Object=MibTableColumn
cmFacProtGroupStorageType=_CmFacProtGroupStorageType_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,11),_CmFacProtGroupStorageType_Type())
cmFacProtGroupStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFacProtGroupStorageType.setStatus(_A)
_CmFacProtGroupRowStatus_Type=RowStatus
_CmFacProtGroupRowStatus_Object=MibTableColumn
cmFacProtGroupRowStatus=_CmFacProtGroupRowStatus_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,12),_CmFacProtGroupRowStatus_Type())
cmFacProtGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFacProtGroupRowStatus.setStatus(_A)
_CmFacProtGroupMacAddress_Type=MacAddress
_CmFacProtGroupMacAddress_Object=MibTableColumn
cmFacProtGroupMacAddress=_CmFacProtGroupMacAddress_Object((1,3,6,1,4,1,2544,1,12,7,1,1,1,13),_CmFacProtGroupMacAddress_Type())
cmFacProtGroupMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cmFacProtGroupMacAddress.setStatus(_A)
_CmFacProtUnitTable_Object=MibTable
cmFacProtUnitTable=_CmFacProtUnitTable_Object((1,3,6,1,4,1,2544,1,12,7,1,2))
if mibBuilder.loadTexts:cmFacProtUnitTable.setStatus(_A)
_CmFacProtUnitEntry_Object=MibTableRow
cmFacProtUnitEntry=_CmFacProtUnitEntry_Object((1,3,6,1,4,1,2544,1,12,7,1,2,1))
cmFacProtUnitEntry.setIndexNames((0,_E,_F),(0,_E,_I),(0,_E,_J),(0,_B,_G),(0,_B,_M))
if mibBuilder.loadTexts:cmFacProtUnitEntry.setStatus(_A)
_CmFacProtUnitIndex_Type=Integer32
_CmFacProtUnitIndex_Object=MibTableColumn
cmFacProtUnitIndex=_CmFacProtUnitIndex_Object((1,3,6,1,4,1,2544,1,12,7,1,2,1,1),_CmFacProtUnitIndex_Type())
cmFacProtUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cmFacProtUnitIndex.setStatus(_A)
_CmFacProtUnitType_Type=CmProtUnitType
_CmFacProtUnitType_Object=MibTableColumn
cmFacProtUnitType=_CmFacProtUnitType_Object((1,3,6,1,4,1,2544,1,12,7,1,2,1,2),_CmFacProtUnitType_Type())
cmFacProtUnitType.setMaxAccess(_D)
if mibBuilder.loadTexts:cmFacProtUnitType.setStatus(_A)
_CmFacProtUnitState_Type=CmProtUnitState
_CmFacProtUnitState_Object=MibTableColumn
cmFacProtUnitState=_CmFacProtUnitState_Object((1,3,6,1,4,1,2544,1,12,7,1,2,1,3),_CmFacProtUnitState_Type())
cmFacProtUnitState.setMaxAccess(_D)
if mibBuilder.loadTexts:cmFacProtUnitState.setStatus(_A)
_CmFacProtUnitPort_Type=VariablePointer
_CmFacProtUnitPort_Object=MibTableColumn
cmFacProtUnitPort=_CmFacProtUnitPort_Object((1,3,6,1,4,1,2544,1,12,7,1,2,1,4),_CmFacProtUnitPort_Type())
cmFacProtUnitPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cmFacProtUnitPort.setStatus(_A)
_CmMSPGroupTable_Object=MibTable
cmMSPGroupTable=_CmMSPGroupTable_Object((1,3,6,1,4,1,2544,1,12,7,1,3))
if mibBuilder.loadTexts:cmMSPGroupTable.setStatus(_A)
_CmMSPGroupEntry_Object=MibTableRow
cmMSPGroupEntry=_CmMSPGroupEntry_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1))
cmMSPGroupEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:cmMSPGroupEntry.setStatus(_A)
_CmMSPGroupIndex_Type=Integer32
_CmMSPGroupIndex_Object=MibTableColumn
cmMSPGroupIndex=_CmMSPGroupIndex_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,1),_CmMSPGroupIndex_Type())
cmMSPGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cmMSPGroupIndex.setStatus(_A)
class _CmMSPGroupUserLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmMSPGroupUserLabel_Type.__name__=_L
_CmMSPGroupUserLabel_Object=MibTableColumn
cmMSPGroupUserLabel=_CmMSPGroupUserLabel_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,2),_CmMSPGroupUserLabel_Type())
cmMSPGroupUserLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupUserLabel.setStatus(_A)
_CmMSPGroupSwitchMode_Type=CmProtSwitchMode
_CmMSPGroupSwitchMode_Object=MibTableColumn
cmMSPGroupSwitchMode=_CmMSPGroupSwitchMode_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,3),_CmMSPGroupSwitchMode_Type())
cmMSPGroupSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupSwitchMode.setStatus(_A)
_CmMSPGroupRevertive_Type=TruthValue
_CmMSPGroupRevertive_Object=MibTableColumn
cmMSPGroupRevertive=_CmMSPGroupRevertive_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,4),_CmMSPGroupRevertive_Type())
cmMSPGroupRevertive.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupRevertive.setStatus(_A)
class _CmMSPGroupWaitToRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60),ValueRangeConstraint(0,0))
_CmMSPGroupWaitToRestore_Type.__name__=_K
_CmMSPGroupWaitToRestore_Object=MibTableColumn
cmMSPGroupWaitToRestore=_CmMSPGroupWaitToRestore_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,5),_CmMSPGroupWaitToRestore_Type())
cmMSPGroupWaitToRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupWaitToRestore.setStatus(_A)
_CmMSPGroupB2DEGTrigger_Type=TruthValue
_CmMSPGroupB2DEGTrigger_Object=MibTableColumn
cmMSPGroupB2DEGTrigger=_CmMSPGroupB2DEGTrigger_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,6),_CmMSPGroupB2DEGTrigger_Type())
cmMSPGroupB2DEGTrigger.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupB2DEGTrigger.setStatus(_A)
_CmMSPGroupDirection_Type=CmProtSwitchDirection
_CmMSPGroupDirection_Object=MibTableColumn
cmMSPGroupDirection=_CmMSPGroupDirection_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,7),_CmMSPGroupDirection_Type())
cmMSPGroupDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupDirection.setStatus(_A)
_CmMSPGroupWorkPort_Type=VariablePointer
_CmMSPGroupWorkPort_Object=MibTableColumn
cmMSPGroupWorkPort=_CmMSPGroupWorkPort_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,8),_CmMSPGroupWorkPort_Type())
cmMSPGroupWorkPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupWorkPort.setStatus(_A)
_CmMSPGroupProtPort_Type=VariablePointer
_CmMSPGroupProtPort_Object=MibTableColumn
cmMSPGroupProtPort=_CmMSPGroupProtPort_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,9),_CmMSPGroupProtPort_Type())
cmMSPGroupProtPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupProtPort.setStatus(_A)
_CmMSPGroupStatus_Type=CmProtGroupStatus
_CmMSPGroupStatus_Object=MibTableColumn
cmMSPGroupStatus=_CmMSPGroupStatus_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,10),_CmMSPGroupStatus_Type())
cmMSPGroupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cmMSPGroupStatus.setStatus(_A)
_CmMSPGroupAction_Type=CmProtSwitchAction
_CmMSPGroupAction_Object=MibTableColumn
cmMSPGroupAction=_CmMSPGroupAction_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,11),_CmMSPGroupAction_Type())
cmMSPGroupAction.setMaxAccess(_O)
if mibBuilder.loadTexts:cmMSPGroupAction.setStatus(_A)
_CmMSPGroupStorageType_Type=StorageType
_CmMSPGroupStorageType_Object=MibTableColumn
cmMSPGroupStorageType=_CmMSPGroupStorageType_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,12),_CmMSPGroupStorageType_Type())
cmMSPGroupStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupStorageType.setStatus(_A)
_CmMSPGroupRowStatus_Type=RowStatus
_CmMSPGroupRowStatus_Object=MibTableColumn
cmMSPGroupRowStatus=_CmMSPGroupRowStatus_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,13),_CmMSPGroupRowStatus_Type())
cmMSPGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMSPGroupRowStatus.setStatus(_A)
_CmMSPGroupMacAddress_Type=MacAddress
_CmMSPGroupMacAddress_Object=MibTableColumn
cmMSPGroupMacAddress=_CmMSPGroupMacAddress_Object((1,3,6,1,4,1,2544,1,12,7,1,3,1,14),_CmMSPGroupMacAddress_Type())
cmMSPGroupMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cmMSPGroupMacAddress.setStatus(_A)
_CmMSPUnitTable_Object=MibTable
cmMSPUnitTable=_CmMSPUnitTable_Object((1,3,6,1,4,1,2544,1,12,7,1,4))
if mibBuilder.loadTexts:cmMSPUnitTable.setStatus(_A)
_CmMSPUnitEntry_Object=MibTableRow
cmMSPUnitEntry=_CmMSPUnitEntry_Object((1,3,6,1,4,1,2544,1,12,7,1,4,1))
cmMSPUnitEntry.setIndexNames((0,_E,_F),(0,_B,_H),(0,_B,_N))
if mibBuilder.loadTexts:cmMSPUnitEntry.setStatus(_A)
_CmMSPUnitIndex_Type=Integer32
_CmMSPUnitIndex_Object=MibTableColumn
cmMSPUnitIndex=_CmMSPUnitIndex_Object((1,3,6,1,4,1,2544,1,12,7,1,4,1,1),_CmMSPUnitIndex_Type())
cmMSPUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cmMSPUnitIndex.setStatus(_A)
_CmMSPUnitType_Type=CmProtUnitType
_CmMSPUnitType_Object=MibTableColumn
cmMSPUnitType=_CmMSPUnitType_Object((1,3,6,1,4,1,2544,1,12,7,1,4,1,2),_CmMSPUnitType_Type())
cmMSPUnitType.setMaxAccess(_D)
if mibBuilder.loadTexts:cmMSPUnitType.setStatus(_A)
_CmMSPUnitState_Type=CmProtUnitState
_CmMSPUnitState_Object=MibTableColumn
cmMSPUnitState=_CmMSPUnitState_Object((1,3,6,1,4,1,2544,1,12,7,1,4,1,3),_CmMSPUnitState_Type())
cmMSPUnitState.setMaxAccess(_D)
if mibBuilder.loadTexts:cmMSPUnitState.setStatus(_A)
_CmMSPUnitPort_Type=VariablePointer
_CmMSPUnitPort_Object=MibTableColumn
cmMSPUnitPort=_CmMSPUnitPort_Object((1,3,6,1,4,1,2544,1,12,7,1,4,1,4),_CmMSPUnitPort_Type())
cmMSPUnitPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cmMSPUnitPort.setStatus(_A)
_CmProtNotifications_ObjectIdentity=ObjectIdentity
cmProtNotifications=_CmProtNotifications_ObjectIdentity((1,3,6,1,4,1,2544,1,12,7,2))
_CmProtConformance_ObjectIdentity=ObjectIdentity
cmProtConformance=_CmProtConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,7,3))
_CmProtCompliances_ObjectIdentity=ObjectIdentity
cmProtCompliances=_CmProtCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,7,3,1))
_CmProtGroups_ObjectIdentity=ObjectIdentity
cmProtGroups=_CmProtGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,7,3,2))
cmProtObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,7,3,2,1))
cmProtObjectGroup.setObjects(*((_B,_G),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_M),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:cmProtObjectGroup.setStatus(_A)
cmMSProtObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,7,3,2,2))
cmMSProtObjectGroup.setObjects(*((_B,_H),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_N),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:cmMSProtObjectGroup.setStatus(_A)
cmProtCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,7,3,1,1))
cmProtCompliance.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:cmProtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CmProtSwitchMode':CmProtSwitchMode,'CmProtSwitchDirection':CmProtSwitchDirection,'CmProtSwitchAction':CmProtSwitchAction,'CmProtUnitType':CmProtUnitType,'CmProtUnitState':CmProtUnitState,'CmProtGroupStatus':CmProtGroupStatus,'cmProtectionMIB':cmProtectionMIB,'cmProtObjects':cmProtObjects,'cmFacProtGroupTable':cmFacProtGroupTable,'cmFacProtGroupEntry':cmFacProtGroupEntry,_G:cmFacProtGroupIndex,_P:cmFacProtGroupUserLabel,_Q:cmFacProtGroupSwitchMode,_R:cmFacProtGroupRevertive,_S:cmFacProtGroupWaitToRestore,_T:cmFacProtGroupDirection,_U:cmFacProtGroupWorkPort,_V:cmFacProtGroupProtPort,_W:cmFacProtGroupStatus,_X:cmFacProtGroupAction,_Y:cmFacProtGroupStorageType,_Z:cmFacProtGroupRowStatus,_a:cmFacProtGroupMacAddress,'cmFacProtUnitTable':cmFacProtUnitTable,'cmFacProtUnitEntry':cmFacProtUnitEntry,_M:cmFacProtUnitIndex,_b:cmFacProtUnitType,_c:cmFacProtUnitState,_d:cmFacProtUnitPort,'cmMSPGroupTable':cmMSPGroupTable,'cmMSPGroupEntry':cmMSPGroupEntry,_H:cmMSPGroupIndex,_e:cmMSPGroupUserLabel,_f:cmMSPGroupSwitchMode,_g:cmMSPGroupRevertive,_h:cmMSPGroupWaitToRestore,_i:cmMSPGroupB2DEGTrigger,_j:cmMSPGroupDirection,_k:cmMSPGroupWorkPort,_l:cmMSPGroupProtPort,_m:cmMSPGroupStatus,_n:cmMSPGroupAction,_o:cmMSPGroupStorageType,_p:cmMSPGroupRowStatus,_q:cmMSPGroupMacAddress,'cmMSPUnitTable':cmMSPUnitTable,'cmMSPUnitEntry':cmMSPUnitEntry,_N:cmMSPUnitIndex,_r:cmMSPUnitType,_s:cmMSPUnitState,_t:cmMSPUnitPort,'cmProtNotifications':cmProtNotifications,'cmProtConformance':cmProtConformance,'cmProtCompliances':cmProtCompliances,'cmProtCompliance':cmProtCompliance,'cmProtGroups':cmProtGroups,_u:cmProtObjectGroup,_v:cmMSProtObjectGroup})