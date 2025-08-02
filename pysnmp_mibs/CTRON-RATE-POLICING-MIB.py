_T='ctRatePolicingConfigGroup'
_S='ctRatePolicingDirection'
_R='ctRatePolicingDirectionsAllowed'
_Q='ctRatePolicingActionsTaken'
_P='ctRatePolicingRuleStatus'
_O='ctRatePolicingPriorityList'
_N='ctRatePolicingThreshHold'
_M='ctRatePolicingAction'
_L='ctRatePolicingActionsAllowed'
_K='ctRatePolicingConfigLastChange'
_J='ctRatePolicingAdminStatus'
_I='kilobytes'
_H='ctRatePolicingResourceIndex'
_G='dot1dBasePort'
_F='BRIDGE-MIB'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CTRON-RATE-POLICING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_F,_G)
ctPriorityExt,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctPriorityExt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ctRatePolicing=ModuleIdentity((1,3,6,1,4,1,52,4,1,2,14,7))
if mibBuilder.loadTexts:ctRatePolicing.setRevisions(('2003-04-10 15:18','2003-03-11 15:53','2000-11-28 15:51','1999-06-21 00:00'))
class CtPriList(TextualConvention,Integer32):status=_A;displayHint='x';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class CtRatePolActionList(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('dropPacket',1),('flowCtrlPacketAndDrop',2),('dropPacketOrFlowCtrlAndDrop',3)))
class CtRatePolDirectionList(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('inbound',1),('outbound',2),('inboundAndOutbound',3)))
_CtRatePolicingObjects_ObjectIdentity=ObjectIdentity
ctRatePolicingObjects=_CtRatePolicingObjects_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,7,1))
class _CtRatePolicingAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CtRatePolicingAdminStatus_Type.__name__=_C
_CtRatePolicingAdminStatus_Object=MibScalar
ctRatePolicingAdminStatus=_CtRatePolicingAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,1),_CtRatePolicingAdminStatus_Type())
ctRatePolicingAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctRatePolicingAdminStatus.setStatus(_A)
_CtRatePolicingConfigLastChange_Type=TimeTicks
_CtRatePolicingConfigLastChange_Object=MibScalar
ctRatePolicingConfigLastChange=_CtRatePolicingConfigLastChange_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,2),_CtRatePolicingConfigLastChange_Type())
ctRatePolicingConfigLastChange.setMaxAccess(_E)
if mibBuilder.loadTexts:ctRatePolicingConfigLastChange.setStatus(_A)
_CtRatePolicingConfigTable_Object=MibTable
ctRatePolicingConfigTable=_CtRatePolicingConfigTable_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3))
if mibBuilder.loadTexts:ctRatePolicingConfigTable.setStatus(_A)
_CtRatePolicingConfigEntry_Object=MibTableRow
ctRatePolicingConfigEntry=_CtRatePolicingConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1))
ctRatePolicingConfigEntry.setIndexNames((0,_F,_G),(0,_B,_H))
if mibBuilder.loadTexts:ctRatePolicingConfigEntry.setStatus(_A)
class _CtRatePolicingResourceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CtRatePolicingResourceIndex_Type.__name__=_C
_CtRatePolicingResourceIndex_Object=MibTableColumn
ctRatePolicingResourceIndex=_CtRatePolicingResourceIndex_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,1),_CtRatePolicingResourceIndex_Type())
ctRatePolicingResourceIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ctRatePolicingResourceIndex.setStatus(_A)
_CtRatePolicingActionsAllowed_Type=CtRatePolActionList
_CtRatePolicingActionsAllowed_Object=MibTableColumn
ctRatePolicingActionsAllowed=_CtRatePolicingActionsAllowed_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,2),_CtRatePolicingActionsAllowed_Type())
ctRatePolicingActionsAllowed.setMaxAccess(_E)
if mibBuilder.loadTexts:ctRatePolicingActionsAllowed.setStatus(_A)
_CtRatePolicingAction_Type=CtRatePolActionList
_CtRatePolicingAction_Object=MibTableColumn
ctRatePolicingAction=_CtRatePolicingAction_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,3),_CtRatePolicingAction_Type())
ctRatePolicingAction.setMaxAccess(_D)
if mibBuilder.loadTexts:ctRatePolicingAction.setStatus(_A)
class _CtRatePolicingThreshHoldMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtRatePolicingThreshHoldMin_Type.__name__=_C
_CtRatePolicingThreshHoldMin_Object=MibTableColumn
ctRatePolicingThreshHoldMin=_CtRatePolicingThreshHoldMin_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,4),_CtRatePolicingThreshHoldMin_Type())
ctRatePolicingThreshHoldMin.setMaxAccess(_E)
if mibBuilder.loadTexts:ctRatePolicingThreshHoldMin.setStatus(_A)
if mibBuilder.loadTexts:ctRatePolicingThreshHoldMin.setUnits(_I)
class _CtRatePolicingThreshHold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtRatePolicingThreshHold_Type.__name__=_C
_CtRatePolicingThreshHold_Object=MibTableColumn
ctRatePolicingThreshHold=_CtRatePolicingThreshHold_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,5),_CtRatePolicingThreshHold_Type())
ctRatePolicingThreshHold.setMaxAccess(_D)
if mibBuilder.loadTexts:ctRatePolicingThreshHold.setStatus(_A)
if mibBuilder.loadTexts:ctRatePolicingThreshHold.setUnits(_I)
_CtRatePolicingPriorityList_Type=CtPriList
_CtRatePolicingPriorityList_Object=MibTableColumn
ctRatePolicingPriorityList=_CtRatePolicingPriorityList_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,6),_CtRatePolicingPriorityList_Type())
ctRatePolicingPriorityList.setMaxAccess(_D)
if mibBuilder.loadTexts:ctRatePolicingPriorityList.setStatus(_A)
class _CtRatePolicingRuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('disabled',2)))
_CtRatePolicingRuleStatus_Type.__name__=_C
_CtRatePolicingRuleStatus_Object=MibTableColumn
ctRatePolicingRuleStatus=_CtRatePolicingRuleStatus_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,7),_CtRatePolicingRuleStatus_Type())
ctRatePolicingRuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctRatePolicingRuleStatus.setStatus(_A)
_CtRatePolicingActionsTaken_Type=Integer32
_CtRatePolicingActionsTaken_Object=MibTableColumn
ctRatePolicingActionsTaken=_CtRatePolicingActionsTaken_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,8),_CtRatePolicingActionsTaken_Type())
ctRatePolicingActionsTaken.setMaxAccess(_E)
if mibBuilder.loadTexts:ctRatePolicingActionsTaken.setStatus(_A)
_CtRatePolicingDirectionsAllowed_Type=CtRatePolDirectionList
_CtRatePolicingDirectionsAllowed_Object=MibTableColumn
ctRatePolicingDirectionsAllowed=_CtRatePolicingDirectionsAllowed_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,9),_CtRatePolicingDirectionsAllowed_Type())
ctRatePolicingDirectionsAllowed.setMaxAccess(_E)
if mibBuilder.loadTexts:ctRatePolicingDirectionsAllowed.setStatus(_A)
_CtRatePolicingDirection_Type=CtRatePolDirectionList
_CtRatePolicingDirection_Object=MibTableColumn
ctRatePolicingDirection=_CtRatePolicingDirection_Object((1,3,6,1,4,1,52,4,1,2,14,7,1,3,1,10),_CtRatePolicingDirection_Type())
ctRatePolicingDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:ctRatePolicingDirection.setStatus(_A)
_CtRatePolicingConformance_ObjectIdentity=ObjectIdentity
ctRatePolicingConformance=_CtRatePolicingConformance_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,7,2))
_CtRatePolicingGroups_ObjectIdentity=ObjectIdentity
ctRatePolicingGroups=_CtRatePolicingGroups_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,7,2,1))
_CtRatePolicingCompliances_ObjectIdentity=ObjectIdentity
ctRatePolicingCompliances=_CtRatePolicingCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,7,2,2))
ctRatePolicingConfigGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,14,7,2,1,1))
ctRatePolicingConfigGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ctRatePolicingConfigGroup.setStatus(_A)
ctRatePolicingCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,14,7,2,2,1))
ctRatePolicingCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:ctRatePolicingCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CtPriList':CtPriList,'CtRatePolActionList':CtRatePolActionList,'CtRatePolDirectionList':CtRatePolDirectionList,'ctRatePolicing':ctRatePolicing,'ctRatePolicingObjects':ctRatePolicingObjects,_J:ctRatePolicingAdminStatus,_K:ctRatePolicingConfigLastChange,'ctRatePolicingConfigTable':ctRatePolicingConfigTable,'ctRatePolicingConfigEntry':ctRatePolicingConfigEntry,_H:ctRatePolicingResourceIndex,_L:ctRatePolicingActionsAllowed,_M:ctRatePolicingAction,'ctRatePolicingThreshHoldMin':ctRatePolicingThreshHoldMin,_N:ctRatePolicingThreshHold,_O:ctRatePolicingPriorityList,_P:ctRatePolicingRuleStatus,_Q:ctRatePolicingActionsTaken,_R:ctRatePolicingDirectionsAllowed,_S:ctRatePolicingDirection,'ctRatePolicingConformance':ctRatePolicingConformance,'ctRatePolicingGroups':ctRatePolicingGroups,_T:ctRatePolicingConfigGroup,'ctRatePolicingCompliances':ctRatePolicingCompliances,'ctRatePolicingCompliance':ctRatePolicingCompliance})