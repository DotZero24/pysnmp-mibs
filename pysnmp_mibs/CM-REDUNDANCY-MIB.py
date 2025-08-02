_U='cmRedundancyObjectGroup'
_T='cmRedundancyGroupAction'
_S='cmRedundancyGroupSyncStatus'
_R='cmRedundancyGroupState'
_Q='cmRedundancyGroupLastSwitchOverReason'
_P='cmRedundancyGroupLastSwitchOverTime'
_O='cmRedundancyGroupStandbyCardState'
_N='cmRedundancyGroupStandbyCard'
_M='cmRedundancyGroupActiveCardState'
_L='cmRedundancyGroupActiveCard'
_K='cmRedundancyGroupSyncEnabled'
_J='cmRedundancyGroupType'
_I='cmRedundancyGroupUserLabel'
_H='read-write'
_G='DisplayString'
_F='neIndex'
_E='CM-ENTITY-MIB'
_D='cmRedundancyGroupIndex'
_C='read-only'
_B='CM-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
CardType,neIndex=mibBuilder.importSymbols(_E,'CardType',_F)
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue','VariablePointer')
cmRedundancyMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,15))
if mibBuilder.loadTexts:cmRedundancyMIB.setRevisions(('2009-02-24 00:00',))
class CmRedundancyArch(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loadbalance',1),('activestandby',2)))
class CmRedundancyStandbyMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cold',1),('warm',2),('hot',3)))
class CmRedundancyState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
class CmRedundancySyncStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('out-of-synchronize',2),('bulk-synchronize',3),('incremental-synchronize',4)))
class CmRedundancySwitchOverReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),('latestUpdatedData',2),('userTrigger',3),('cardReset',4),('cardRemoval',5),('softwareFailure',6),('hardwareFailure',7)))
class CmRedundancySyncMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatically',1),('manually',2)))
class CmRedundancyAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notApplicable',0),('force',1),('manual',2),('releaseforce',3)))
class CmRedundancyUnitState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',1),('normal',2),('maintenance',3),('faultisolation',4),('lock',5),('extracted',6),('init',7),('stanbdby',8)))
_CmRedundancyObjects_ObjectIdentity=ObjectIdentity
cmRedundancyObjects=_CmRedundancyObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,15,1))
_CmRedundancyGroupTable_Object=MibTable
cmRedundancyGroupTable=_CmRedundancyGroupTable_Object((1,3,6,1,4,1,2544,1,12,15,1,1))
if mibBuilder.loadTexts:cmRedundancyGroupTable.setStatus(_A)
_CmRedundancyGroupEntry_Object=MibTableRow
cmRedundancyGroupEntry=_CmRedundancyGroupEntry_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1))
cmRedundancyGroupEntry.setIndexNames((0,_E,_F),(0,_B,_D))
if mibBuilder.loadTexts:cmRedundancyGroupEntry.setStatus(_A)
_CmRedundancyGroupIndex_Type=Integer32
_CmRedundancyGroupIndex_Object=MibTableColumn
cmRedundancyGroupIndex=_CmRedundancyGroupIndex_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,1),_CmRedundancyGroupIndex_Type())
cmRedundancyGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupIndex.setStatus(_A)
class _CmRedundancyGroupUserLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmRedundancyGroupUserLabel_Type.__name__=_G
_CmRedundancyGroupUserLabel_Object=MibTableColumn
cmRedundancyGroupUserLabel=_CmRedundancyGroupUserLabel_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,2),_CmRedundancyGroupUserLabel_Type())
cmRedundancyGroupUserLabel.setMaxAccess('read-create')
if mibBuilder.loadTexts:cmRedundancyGroupUserLabel.setStatus(_A)
_CmRedundancyGroupType_Type=CardType
_CmRedundancyGroupType_Object=MibTableColumn
cmRedundancyGroupType=_CmRedundancyGroupType_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,3),_CmRedundancyGroupType_Type())
cmRedundancyGroupType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupType.setStatus(_A)
_CmRedundancyGroupSyncEnabled_Type=TruthValue
_CmRedundancyGroupSyncEnabled_Object=MibTableColumn
cmRedundancyGroupSyncEnabled=_CmRedundancyGroupSyncEnabled_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,4),_CmRedundancyGroupSyncEnabled_Type())
cmRedundancyGroupSyncEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:cmRedundancyGroupSyncEnabled.setStatus(_A)
_CmRedundancyGroupActiveCard_Type=VariablePointer
_CmRedundancyGroupActiveCard_Object=MibTableColumn
cmRedundancyGroupActiveCard=_CmRedundancyGroupActiveCard_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,5),_CmRedundancyGroupActiveCard_Type())
cmRedundancyGroupActiveCard.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupActiveCard.setStatus(_A)
_CmRedundancyGroupActiveCardState_Type=CmRedundancyUnitState
_CmRedundancyGroupActiveCardState_Object=MibTableColumn
cmRedundancyGroupActiveCardState=_CmRedundancyGroupActiveCardState_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,6),_CmRedundancyGroupActiveCardState_Type())
cmRedundancyGroupActiveCardState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupActiveCardState.setStatus(_A)
_CmRedundancyGroupStandbyCard_Type=VariablePointer
_CmRedundancyGroupStandbyCard_Object=MibTableColumn
cmRedundancyGroupStandbyCard=_CmRedundancyGroupStandbyCard_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,7),_CmRedundancyGroupStandbyCard_Type())
cmRedundancyGroupStandbyCard.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupStandbyCard.setStatus(_A)
_CmRedundancyGroupStandbyCardState_Type=CmRedundancyUnitState
_CmRedundancyGroupStandbyCardState_Object=MibTableColumn
cmRedundancyGroupStandbyCardState=_CmRedundancyGroupStandbyCardState_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,8),_CmRedundancyGroupStandbyCardState_Type())
cmRedundancyGroupStandbyCardState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupStandbyCardState.setStatus(_A)
_CmRedundancyGroupLastSwitchOverTime_Type=TimeTicks
_CmRedundancyGroupLastSwitchOverTime_Object=MibTableColumn
cmRedundancyGroupLastSwitchOverTime=_CmRedundancyGroupLastSwitchOverTime_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,9),_CmRedundancyGroupLastSwitchOverTime_Type())
cmRedundancyGroupLastSwitchOverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupLastSwitchOverTime.setStatus(_A)
_CmRedundancyGroupLastSwitchOverReason_Type=CmRedundancySwitchOverReason
_CmRedundancyGroupLastSwitchOverReason_Object=MibTableColumn
cmRedundancyGroupLastSwitchOverReason=_CmRedundancyGroupLastSwitchOverReason_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,10),_CmRedundancyGroupLastSwitchOverReason_Type())
cmRedundancyGroupLastSwitchOverReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupLastSwitchOverReason.setStatus(_A)
_CmRedundancyGroupState_Type=CmRedundancyState
_CmRedundancyGroupState_Object=MibTableColumn
cmRedundancyGroupState=_CmRedundancyGroupState_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,11),_CmRedundancyGroupState_Type())
cmRedundancyGroupState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupState.setStatus(_A)
_CmRedundancyGroupSyncStatus_Type=CmRedundancySyncStatus
_CmRedundancyGroupSyncStatus_Object=MibTableColumn
cmRedundancyGroupSyncStatus=_CmRedundancyGroupSyncStatus_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,12),_CmRedundancyGroupSyncStatus_Type())
cmRedundancyGroupSyncStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRedundancyGroupSyncStatus.setStatus(_A)
_CmRedundancyGroupAction_Type=CmRedundancyAction
_CmRedundancyGroupAction_Object=MibTableColumn
cmRedundancyGroupAction=_CmRedundancyGroupAction_Object((1,3,6,1,4,1,2544,1,12,15,1,1,1,13),_CmRedundancyGroupAction_Type())
cmRedundancyGroupAction.setMaxAccess(_H)
if mibBuilder.loadTexts:cmRedundancyGroupAction.setStatus(_A)
_CmRedundancyNotifications_ObjectIdentity=ObjectIdentity
cmRedundancyNotifications=_CmRedundancyNotifications_ObjectIdentity((1,3,6,1,4,1,2544,1,12,15,2))
_CmRedundancyConformance_ObjectIdentity=ObjectIdentity
cmRedundancyConformance=_CmRedundancyConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,15,3))
_CmRedundancyCompliances_ObjectIdentity=ObjectIdentity
cmRedundancyCompliances=_CmRedundancyCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,15,3,1))
_CmRedundancyGroups_ObjectIdentity=ObjectIdentity
cmRedundancyGroups=_CmRedundancyGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,15,3,2))
cmRedundancyObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,15,3,2,1))
cmRedundancyObjectGroup.setObjects(*((_B,_D),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cmRedundancyObjectGroup.setStatus(_A)
cmRedundancyCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,15,3,1,1))
cmRedundancyCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:cmRedundancyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CmRedundancyArch':CmRedundancyArch,'CmRedundancyStandbyMode':CmRedundancyStandbyMode,'CmRedundancyState':CmRedundancyState,'CmRedundancySyncStatus':CmRedundancySyncStatus,'CmRedundancySwitchOverReason':CmRedundancySwitchOverReason,'CmRedundancySyncMode':CmRedundancySyncMode,'CmRedundancyAction':CmRedundancyAction,'CmRedundancyUnitState':CmRedundancyUnitState,'cmRedundancyMIB':cmRedundancyMIB,'cmRedundancyObjects':cmRedundancyObjects,'cmRedundancyGroupTable':cmRedundancyGroupTable,'cmRedundancyGroupEntry':cmRedundancyGroupEntry,_D:cmRedundancyGroupIndex,_I:cmRedundancyGroupUserLabel,_J:cmRedundancyGroupType,_K:cmRedundancyGroupSyncEnabled,_L:cmRedundancyGroupActiveCard,_M:cmRedundancyGroupActiveCardState,_N:cmRedundancyGroupStandbyCard,_O:cmRedundancyGroupStandbyCardState,_P:cmRedundancyGroupLastSwitchOverTime,_Q:cmRedundancyGroupLastSwitchOverReason,_R:cmRedundancyGroupState,_S:cmRedundancyGroupSyncStatus,_T:cmRedundancyGroupAction,'cmRedundancyNotifications':cmRedundancyNotifications,'cmRedundancyConformance':cmRedundancyConformance,'cmRedundancyCompliances':cmRedundancyCompliances,'cmRedundancyCompliance':cmRedundancyCompliance,'cmRedundancyGroups':cmRedundancyGroups,_U:cmRedundancyObjectGroup})