_AK='juniDosProtectionScfdsNonSuspiciousControlFlowMac'
_AJ='juniDosProtectionScfdsSuspiciousControlFlowMac'
_AI='juniDosProtectionScfdsNonSuspiciousControlFlow'
_AH='juniDosProtectionScfdsSuspiciousControlFlow'
_AG='juniDosProtectionScfdsFlowRate'
_AF='juniDosProtectionDpgSlotRateMaxBurst'
_AE='juniDosProtectionDpgSlotRateMinBurst'
_AD='juniDosProtectionDpgSlotRateMaxRate'
_AC='juniDosProtectionDpgSlotRateMinRate'
_AB='juniDosProtectionScfdsSlotFlowMacGroup'
_AA='juniDosProtectionScfdsSlotFlowMacIngressSlot'
_A9='juniDosProtectionScfdsSlotFlowMacClearEntry'
_A8='juniDosProtectionScfdsSlotFlowMacTimeFlagged'
_A7='juniDosProtectionScfdsSlotFlowMacPeakRate'
_A6='juniDosProtectionScfdsSlotFlowMacRate'
_A5='juniDosProtectionScfdsSlotFlowGroup'
_A4='juniDosProtectionScfdsSlotFlowIngressSlot'
_A3='juniDosProtectionScfdsSlotFlowClearEntry'
_A2='juniDosProtectionScfdsSlotFlowTimeFlagged'
_A1='juniDosProtectionScfdsSlotFlowPeakRate'
_A0='juniDosProtectionScfdsSlotFlowRate'
_z='juniDosProtectionDpgSlotRateProtocol'
_y='juniDosProtectionDpgSlotRateDpgName'
_x='juniDosProtectionDpgSlotRateSlot'
_w='juniDosProtectionScfdsSlotFlowMacSrcMac'
_v='juniDosProtectionScfdsSlotFlowMacProtocol'
_u='juniDosProtectionScfdsSlotFlowMacGroupId'
_t='juniDosProtectionScfdsSlotFlowMacIfIndex'
_s='juniDosProtectionScfdsSlotFlowMacSlot'
_r='juniDosProtectionScfdsSlotFlowProtocol'
_q='juniDosProtectionScfdsSlotFlowGroupId'
_p='juniDosProtectionScfdsSlotFlowIfIndex'
_o='juniDosProtectionScfdsSlotProtocolIndex'
_n='juniDosProtectionScfdsSlotProtocolSlot'
_m='MacAddress'
_l='DisplayString'
_k='juniDosProtectionScfdsNonSuspiciousPriority'
_j='juniDosProtectionScfdsSuspiciousPriority'
_i='juniDosProtectionScfdsNonSuspiciousProtocol'
_h='juniDosProtectionScfdsSuspiciousProtocol'
_g='juniDosProtectionScfdsGroupingInUse'
_f='juniDosProtectionScfdsTableNotFull'
_e='juniDosProtectionScfdsTableFull'
_d='juniDosProtectionScfdsNonSuspiciousControlFlowGroup'
_c='juniDosProtectionScfdsSuspiciousControlFlowGroup'
_b='juniDosProtectionSrcPhysAddr'
_a='juniDosProtectionPriority'
_Z='juniDosProtectionGroupId'
_Y='juniDosProtectionScfdsSlotOverflows'
_X='juniDosProtectionScfdsSlotNumberFalseNegativeFlows'
_W='juniDosProtectionScfdsSlotCurrentFalseNegativeFlows'
_V='juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups'
_U='juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups'
_T='juniDosProtectionScfdsSlotNumberSuspiciousFlows'
_S='juniDosProtectionScfdsSlotCurrentSuspiciousFlows'
_R='juniDosProtectionScfdsSlotTableOverflowState'
_Q='juniDosProtectionScfdsSlotDiscontinuityTime'
_P='juniDosProtectionScfdsSlotProtocolTransitions'
_O='juniDosProtectionScfdsSlotProtocolState'
_N='read-write'
_M='clear'
_L='juniDosProtectionScfdsSlotFlowSlot'
_K='Unsigned32'
_J='Integer32'
_I='juniDosProtectionIfIndex'
_H='accessible-for-notify'
_G='juniDosProtectionProtocol'
_F='juniDosProtectionScfdsSlot'
_E='not-accessible'
_D='obsolete'
_C='read-only'
_B='current'
_A='Juniper-DOS-PROTECTION-PLATFORM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
JuniDosProtectionPriorityType,JuniDosProtectionProtocolState,JuniDosProtectionProtocolType,JuniDosProtectionScfdsTableOverflowState=mibBuilder.importSymbols('Juniper-DOS-PROTECTION-MIB','JuniDosProtectionPriorityType','JuniDosProtectionProtocolState','JuniDosProtectionProtocolType','JuniDosProtectionScfdsTableOverflowState')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,=mibBuilder.importSymbols('Juniper-TC','JuniEnable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_l,_m,'PhysAddress','TextualConvention','TruthValue')
juniDosProtectionPlatformMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,81))
if mibBuilder.loadTexts:juniDosProtectionPlatformMIB.setRevisions(('2006-07-01 00:00','2006-01-01 00:00'))
_JuniDosProtectionPlatformTraps_ObjectIdentity=ObjectIdentity
juniDosProtectionPlatformTraps=_JuniDosProtectionPlatformTraps_ObjectIdentity((1,3,6,1,4,1,4874,2,2,81,0))
_JuniDosProtectionPlatformScfdsTraps_ObjectIdentity=ObjectIdentity
juniDosProtectionPlatformScfdsTraps=_JuniDosProtectionPlatformScfdsTraps_ObjectIdentity((1,3,6,1,4,1,4874,2,2,81,0,0))
_JuniDosProtectionPlatformObjects_ObjectIdentity=ObjectIdentity
juniDosProtectionPlatformObjects=_JuniDosProtectionPlatformObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,81,1))
_JuniDosProtectionPlatformScfdsGroup_ObjectIdentity=ObjectIdentity
juniDosProtectionPlatformScfdsGroup=_JuniDosProtectionPlatformScfdsGroup_ObjectIdentity((1,3,6,1,4,1,4874,2,2,81,1,1))
_JuniDosProtectionScfdsSlotProtocolTable_Object=MibTable
juniDosProtectionScfdsSlotProtocolTable=_JuniDosProtectionScfdsSlotProtocolTable_Object((1,3,6,1,4,1,4874,2,2,81,1,1,1))
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotProtocolTable.setStatus(_B)
_JuniDosProtectionScfdsSlotProtocolEntry_Object=MibTableRow
juniDosProtectionScfdsSlotProtocolEntry=_JuniDosProtectionScfdsSlotProtocolEntry_Object((1,3,6,1,4,1,4874,2,2,81,1,1,1,1))
juniDosProtectionScfdsSlotProtocolEntry.setIndexNames((0,_A,_n),(0,_A,_o))
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotProtocolEntry.setStatus(_B)
_JuniDosProtectionScfdsSlotProtocolSlot_Type=Unsigned32
_JuniDosProtectionScfdsSlotProtocolSlot_Object=MibTableColumn
juniDosProtectionScfdsSlotProtocolSlot=_JuniDosProtectionScfdsSlotProtocolSlot_Object((1,3,6,1,4,1,4874,2,2,81,1,1,1,1,1),_JuniDosProtectionScfdsSlotProtocolSlot_Type())
juniDosProtectionScfdsSlotProtocolSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotProtocolSlot.setStatus(_B)
_JuniDosProtectionScfdsSlotProtocolIndex_Type=JuniDosProtectionProtocolType
_JuniDosProtectionScfdsSlotProtocolIndex_Object=MibTableColumn
juniDosProtectionScfdsSlotProtocolIndex=_JuniDosProtectionScfdsSlotProtocolIndex_Object((1,3,6,1,4,1,4874,2,2,81,1,1,1,1,2),_JuniDosProtectionScfdsSlotProtocolIndex_Type())
juniDosProtectionScfdsSlotProtocolIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotProtocolIndex.setStatus(_B)
_JuniDosProtectionScfdsSlotProtocolState_Type=JuniDosProtectionProtocolState
_JuniDosProtectionScfdsSlotProtocolState_Object=MibTableColumn
juniDosProtectionScfdsSlotProtocolState=_JuniDosProtectionScfdsSlotProtocolState_Object((1,3,6,1,4,1,4874,2,2,81,1,1,1,1,3),_JuniDosProtectionScfdsSlotProtocolState_Type())
juniDosProtectionScfdsSlotProtocolState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotProtocolState.setStatus(_B)
_JuniDosProtectionScfdsSlotProtocolTransitions_Type=Counter32
_JuniDosProtectionScfdsSlotProtocolTransitions_Object=MibTableColumn
juniDosProtectionScfdsSlotProtocolTransitions=_JuniDosProtectionScfdsSlotProtocolTransitions_Object((1,3,6,1,4,1,4874,2,2,81,1,1,1,1,4),_JuniDosProtectionScfdsSlotProtocolTransitions_Type())
juniDosProtectionScfdsSlotProtocolTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotProtocolTransitions.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowTable_Object=MibTable
juniDosProtectionScfdsSlotFlowTable=_JuniDosProtectionScfdsSlotFlowTable_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2))
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowTable.setStatus(_D)
_JuniDosProtectionScfdsSlotFlowEntry_Object=MibTableRow
juniDosProtectionScfdsSlotFlowEntry=_JuniDosProtectionScfdsSlotFlowEntry_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1))
juniDosProtectionScfdsSlotFlowEntry.setIndexNames((0,_A,_L),(0,_A,_p),(0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowEntry.setStatus(_D)
_JuniDosProtectionScfdsSlotFlowSlot_Type=Unsigned32
_JuniDosProtectionScfdsSlotFlowSlot_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowSlot=_JuniDosProtectionScfdsSlotFlowSlot_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,1),_JuniDosProtectionScfdsSlotFlowSlot_Type())
juniDosProtectionScfdsSlotFlowSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowSlot.setStatus(_D)
_JuniDosProtectionScfdsSlotFlowIfIndex_Type=InterfaceIndex
_JuniDosProtectionScfdsSlotFlowIfIndex_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowIfIndex=_JuniDosProtectionScfdsSlotFlowIfIndex_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,2),_JuniDosProtectionScfdsSlotFlowIfIndex_Type())
juniDosProtectionScfdsSlotFlowIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowIfIndex.setStatus(_D)
class _JuniDosProtectionScfdsSlotFlowGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_JuniDosProtectionScfdsSlotFlowGroupId_Type.__name__=_K
_JuniDosProtectionScfdsSlotFlowGroupId_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowGroupId=_JuniDosProtectionScfdsSlotFlowGroupId_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,3),_JuniDosProtectionScfdsSlotFlowGroupId_Type())
juniDosProtectionScfdsSlotFlowGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowGroupId.setStatus(_D)
_JuniDosProtectionScfdsSlotFlowProtocol_Type=JuniDosProtectionProtocolType
_JuniDosProtectionScfdsSlotFlowProtocol_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowProtocol=_JuniDosProtectionScfdsSlotFlowProtocol_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,4),_JuniDosProtectionScfdsSlotFlowProtocol_Type())
juniDosProtectionScfdsSlotFlowProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowProtocol.setStatus(_D)
_JuniDosProtectionScfdsSlotFlowRate_Type=Unsigned32
_JuniDosProtectionScfdsSlotFlowRate_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowRate=_JuniDosProtectionScfdsSlotFlowRate_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,5),_JuniDosProtectionScfdsSlotFlowRate_Type())
juniDosProtectionScfdsSlotFlowRate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowRate.setStatus(_D)
_JuniDosProtectionScfdsSlotFlowPeakRate_Type=Unsigned32
_JuniDosProtectionScfdsSlotFlowPeakRate_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowPeakRate=_JuniDosProtectionScfdsSlotFlowPeakRate_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,6),_JuniDosProtectionScfdsSlotFlowPeakRate_Type())
juniDosProtectionScfdsSlotFlowPeakRate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowPeakRate.setStatus(_D)
_JuniDosProtectionScfdsSlotFlowTimeFlagged_Type=Unsigned32
_JuniDosProtectionScfdsSlotFlowTimeFlagged_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowTimeFlagged=_JuniDosProtectionScfdsSlotFlowTimeFlagged_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,7),_JuniDosProtectionScfdsSlotFlowTimeFlagged_Type())
juniDosProtectionScfdsSlotFlowTimeFlagged.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowTimeFlagged.setStatus(_D)
_JuniDosProtectionScfdsSlotFlowIngressSlot_Type=Integer32
_JuniDosProtectionScfdsSlotFlowIngressSlot_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowIngressSlot=_JuniDosProtectionScfdsSlotFlowIngressSlot_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,8),_JuniDosProtectionScfdsSlotFlowIngressSlot_Type())
juniDosProtectionScfdsSlotFlowIngressSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowIngressSlot.setStatus(_D)
_JuniDosProtectionScfdsSlotFlowGroup_Type=TruthValue
_JuniDosProtectionScfdsSlotFlowGroup_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowGroup=_JuniDosProtectionScfdsSlotFlowGroup_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,9),_JuniDosProtectionScfdsSlotFlowGroup_Type())
juniDosProtectionScfdsSlotFlowGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowGroup.setStatus(_D)
class _JuniDosProtectionScfdsSlotFlowClearEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ok',0),(_M,1)))
_JuniDosProtectionScfdsSlotFlowClearEntry_Type.__name__=_J
_JuniDosProtectionScfdsSlotFlowClearEntry_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowClearEntry=_JuniDosProtectionScfdsSlotFlowClearEntry_Object((1,3,6,1,4,1,4874,2,2,81,1,1,2,1,10),_JuniDosProtectionScfdsSlotFlowClearEntry_Type())
juniDosProtectionScfdsSlotFlowClearEntry.setMaxAccess(_N)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowClearEntry.setStatus(_D)
_JuniDosProtectionScfdsSlotTable_Object=MibTable
juniDosProtectionScfdsSlotTable=_JuniDosProtectionScfdsSlotTable_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3))
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotTable.setStatus(_B)
_JuniDosProtectionScfdsSlotEntry_Object=MibTableRow
juniDosProtectionScfdsSlotEntry=_JuniDosProtectionScfdsSlotEntry_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1))
juniDosProtectionScfdsSlotEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotEntry.setStatus(_B)
_JuniDosProtectionScfdsSlotSlot_Type=Unsigned32
_JuniDosProtectionScfdsSlotSlot_Object=MibTableColumn
juniDosProtectionScfdsSlotSlot=_JuniDosProtectionScfdsSlotSlot_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,1),_JuniDosProtectionScfdsSlotSlot_Type())
juniDosProtectionScfdsSlotSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotSlot.setStatus(_B)
class _JuniDosProtectionScfdsSlotClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ok',0),(_M,1)))
_JuniDosProtectionScfdsSlotClearAll_Type.__name__=_J
_JuniDosProtectionScfdsSlotClearAll_Object=MibTableColumn
juniDosProtectionScfdsSlotClearAll=_JuniDosProtectionScfdsSlotClearAll_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,2),_JuniDosProtectionScfdsSlotClearAll_Type())
juniDosProtectionScfdsSlotClearAll.setMaxAccess(_N)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotClearAll.setStatus(_B)
_JuniDosProtectionScfdsSlotDiscontinuityTime_Type=Unsigned32
_JuniDosProtectionScfdsSlotDiscontinuityTime_Object=MibTableColumn
juniDosProtectionScfdsSlotDiscontinuityTime=_JuniDosProtectionScfdsSlotDiscontinuityTime_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,3),_JuniDosProtectionScfdsSlotDiscontinuityTime_Type())
juniDosProtectionScfdsSlotDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotDiscontinuityTime.setStatus(_B)
_JuniDosProtectionScfdsSlotTableOverflowState_Type=JuniDosProtectionScfdsTableOverflowState
_JuniDosProtectionScfdsSlotTableOverflowState_Object=MibTableColumn
juniDosProtectionScfdsSlotTableOverflowState=_JuniDosProtectionScfdsSlotTableOverflowState_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,4),_JuniDosProtectionScfdsSlotTableOverflowState_Type())
juniDosProtectionScfdsSlotTableOverflowState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotTableOverflowState.setStatus(_B)
_JuniDosProtectionScfdsSlotCurrentSuspiciousFlows_Type=Counter32
_JuniDosProtectionScfdsSlotCurrentSuspiciousFlows_Object=MibTableColumn
juniDosProtectionScfdsSlotCurrentSuspiciousFlows=_JuniDosProtectionScfdsSlotCurrentSuspiciousFlows_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,5),_JuniDosProtectionScfdsSlotCurrentSuspiciousFlows_Type())
juniDosProtectionScfdsSlotCurrentSuspiciousFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotCurrentSuspiciousFlows.setStatus(_B)
_JuniDosProtectionScfdsSlotNumberSuspiciousFlows_Type=Counter32
_JuniDosProtectionScfdsSlotNumberSuspiciousFlows_Object=MibTableColumn
juniDosProtectionScfdsSlotNumberSuspiciousFlows=_JuniDosProtectionScfdsSlotNumberSuspiciousFlows_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,6),_JuniDosProtectionScfdsSlotNumberSuspiciousFlows_Type())
juniDosProtectionScfdsSlotNumberSuspiciousFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotNumberSuspiciousFlows.setStatus(_B)
_JuniDosProtectionScfdsSlotNumberSuspiciousFlowGroups_Type=Counter32
_JuniDosProtectionScfdsSlotNumberSuspiciousFlowGroups_Object=MibTableColumn
juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups=_JuniDosProtectionScfdsSlotNumberSuspiciousFlowGroups_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,7),_JuniDosProtectionScfdsSlotNumberSuspiciousFlowGroups_Type())
juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups.setStatus(_B)
_JuniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups_Type=Counter32
_JuniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups_Object=MibTableColumn
juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups=_JuniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,8),_JuniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups_Type())
juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups.setStatus(_B)
_JuniDosProtectionScfdsSlotCurrentFalseNegativeFlows_Type=Counter32
_JuniDosProtectionScfdsSlotCurrentFalseNegativeFlows_Object=MibTableColumn
juniDosProtectionScfdsSlotCurrentFalseNegativeFlows=_JuniDosProtectionScfdsSlotCurrentFalseNegativeFlows_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,9),_JuniDosProtectionScfdsSlotCurrentFalseNegativeFlows_Type())
juniDosProtectionScfdsSlotCurrentFalseNegativeFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotCurrentFalseNegativeFlows.setStatus(_B)
_JuniDosProtectionScfdsSlotNumberFalseNegativeFlows_Type=Counter32
_JuniDosProtectionScfdsSlotNumberFalseNegativeFlows_Object=MibTableColumn
juniDosProtectionScfdsSlotNumberFalseNegativeFlows=_JuniDosProtectionScfdsSlotNumberFalseNegativeFlows_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,10),_JuniDosProtectionScfdsSlotNumberFalseNegativeFlows_Type())
juniDosProtectionScfdsSlotNumberFalseNegativeFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotNumberFalseNegativeFlows.setStatus(_B)
_JuniDosProtectionScfdsSlotOverflows_Type=Counter32
_JuniDosProtectionScfdsSlotOverflows_Object=MibTableColumn
juniDosProtectionScfdsSlotOverflows=_JuniDosProtectionScfdsSlotOverflows_Object((1,3,6,1,4,1,4874,2,2,81,1,1,3,1,11),_JuniDosProtectionScfdsSlotOverflows_Type())
juniDosProtectionScfdsSlotOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotOverflows.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacTable_Object=MibTable
juniDosProtectionScfdsSlotFlowMacTable=_JuniDosProtectionScfdsSlotFlowMacTable_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4))
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacTable.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacEntry_Object=MibTableRow
juniDosProtectionScfdsSlotFlowMacEntry=_JuniDosProtectionScfdsSlotFlowMacEntry_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1))
juniDosProtectionScfdsSlotFlowMacEntry.setIndexNames((0,_A,_s),(0,_A,_t),(0,_A,_u),(0,_A,_v),(0,_A,_w))
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacEntry.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacSlot_Type=Unsigned32
_JuniDosProtectionScfdsSlotFlowMacSlot_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacSlot=_JuniDosProtectionScfdsSlotFlowMacSlot_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,1),_JuniDosProtectionScfdsSlotFlowMacSlot_Type())
juniDosProtectionScfdsSlotFlowMacSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacSlot.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacIfIndex_Type=InterfaceIndex
_JuniDosProtectionScfdsSlotFlowMacIfIndex_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacIfIndex=_JuniDosProtectionScfdsSlotFlowMacIfIndex_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,2),_JuniDosProtectionScfdsSlotFlowMacIfIndex_Type())
juniDosProtectionScfdsSlotFlowMacIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacIfIndex.setStatus(_B)
class _JuniDosProtectionScfdsSlotFlowMacGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_JuniDosProtectionScfdsSlotFlowMacGroupId_Type.__name__=_K
_JuniDosProtectionScfdsSlotFlowMacGroupId_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacGroupId=_JuniDosProtectionScfdsSlotFlowMacGroupId_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,3),_JuniDosProtectionScfdsSlotFlowMacGroupId_Type())
juniDosProtectionScfdsSlotFlowMacGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacGroupId.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacProtocol_Type=JuniDosProtectionProtocolType
_JuniDosProtectionScfdsSlotFlowMacProtocol_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacProtocol=_JuniDosProtectionScfdsSlotFlowMacProtocol_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,4),_JuniDosProtectionScfdsSlotFlowMacProtocol_Type())
juniDosProtectionScfdsSlotFlowMacProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacProtocol.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacSrcMac_Type=MacAddress
_JuniDosProtectionScfdsSlotFlowMacSrcMac_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacSrcMac=_JuniDosProtectionScfdsSlotFlowMacSrcMac_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,5),_JuniDosProtectionScfdsSlotFlowMacSrcMac_Type())
juniDosProtectionScfdsSlotFlowMacSrcMac.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacSrcMac.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacRate_Type=Unsigned32
_JuniDosProtectionScfdsSlotFlowMacRate_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacRate=_JuniDosProtectionScfdsSlotFlowMacRate_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,6),_JuniDosProtectionScfdsSlotFlowMacRate_Type())
juniDosProtectionScfdsSlotFlowMacRate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacRate.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacPeakRate_Type=Unsigned32
_JuniDosProtectionScfdsSlotFlowMacPeakRate_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacPeakRate=_JuniDosProtectionScfdsSlotFlowMacPeakRate_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,7),_JuniDosProtectionScfdsSlotFlowMacPeakRate_Type())
juniDosProtectionScfdsSlotFlowMacPeakRate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacPeakRate.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacTimeFlagged_Type=Unsigned32
_JuniDosProtectionScfdsSlotFlowMacTimeFlagged_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacTimeFlagged=_JuniDosProtectionScfdsSlotFlowMacTimeFlagged_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,8),_JuniDosProtectionScfdsSlotFlowMacTimeFlagged_Type())
juniDosProtectionScfdsSlotFlowMacTimeFlagged.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacTimeFlagged.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacIngressSlot_Type=Integer32
_JuniDosProtectionScfdsSlotFlowMacIngressSlot_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacIngressSlot=_JuniDosProtectionScfdsSlotFlowMacIngressSlot_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,9),_JuniDosProtectionScfdsSlotFlowMacIngressSlot_Type())
juniDosProtectionScfdsSlotFlowMacIngressSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacIngressSlot.setStatus(_B)
_JuniDosProtectionScfdsSlotFlowMacGroup_Type=TruthValue
_JuniDosProtectionScfdsSlotFlowMacGroup_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacGroup=_JuniDosProtectionScfdsSlotFlowMacGroup_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,10),_JuniDosProtectionScfdsSlotFlowMacGroup_Type())
juniDosProtectionScfdsSlotFlowMacGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacGroup.setStatus(_B)
class _JuniDosProtectionScfdsSlotFlowMacClearEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ok',0),(_M,1)))
_JuniDosProtectionScfdsSlotFlowMacClearEntry_Type.__name__=_J
_JuniDosProtectionScfdsSlotFlowMacClearEntry_Object=MibTableColumn
juniDosProtectionScfdsSlotFlowMacClearEntry=_JuniDosProtectionScfdsSlotFlowMacClearEntry_Object((1,3,6,1,4,1,4874,2,2,81,1,1,4,1,11),_JuniDosProtectionScfdsSlotFlowMacClearEntry_Type())
juniDosProtectionScfdsSlotFlowMacClearEntry.setMaxAccess(_N)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlotFlowMacClearEntry.setStatus(_B)
_JuniDosProtectionPlatformDpgGroup_ObjectIdentity=ObjectIdentity
juniDosProtectionPlatformDpgGroup=_JuniDosProtectionPlatformDpgGroup_ObjectIdentity((1,3,6,1,4,1,4874,2,2,81,1,2))
_JuniDosProtectionDpgSlotRateTable_Object=MibTable
juniDosProtectionDpgSlotRateTable=_JuniDosProtectionDpgSlotRateTable_Object((1,3,6,1,4,1,4874,2,2,81,1,2,1))
if mibBuilder.loadTexts:juniDosProtectionDpgSlotRateTable.setStatus(_B)
_JuniDosProtectionDpgSlotRateEntry_Object=MibTableRow
juniDosProtectionDpgSlotRateEntry=_JuniDosProtectionDpgSlotRateEntry_Object((1,3,6,1,4,1,4874,2,2,81,1,2,1,1))
juniDosProtectionDpgSlotRateEntry.setIndexNames((0,_A,_x),(0,_A,_y),(0,_A,_z))
if mibBuilder.loadTexts:juniDosProtectionDpgSlotRateEntry.setStatus(_B)
_JuniDosProtectionDpgSlotRateSlot_Type=Unsigned32
_JuniDosProtectionDpgSlotRateSlot_Object=MibTableColumn
juniDosProtectionDpgSlotRateSlot=_JuniDosProtectionDpgSlotRateSlot_Object((1,3,6,1,4,1,4874,2,2,81,1,2,1,1,1),_JuniDosProtectionDpgSlotRateSlot_Type())
juniDosProtectionDpgSlotRateSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionDpgSlotRateSlot.setStatus(_B)
class _JuniDosProtectionDpgSlotRateDpgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_JuniDosProtectionDpgSlotRateDpgName_Type.__name__=_l
_JuniDosProtectionDpgSlotRateDpgName_Object=MibTableColumn
juniDosProtectionDpgSlotRateDpgName=_JuniDosProtectionDpgSlotRateDpgName_Object((1,3,6,1,4,1,4874,2,2,81,1,2,1,1,2),_JuniDosProtectionDpgSlotRateDpgName_Type())
juniDosProtectionDpgSlotRateDpgName.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionDpgSlotRateDpgName.setStatus(_B)
_JuniDosProtectionDpgSlotRateProtocol_Type=JuniDosProtectionProtocolType
_JuniDosProtectionDpgSlotRateProtocol_Object=MibTableColumn
juniDosProtectionDpgSlotRateProtocol=_JuniDosProtectionDpgSlotRateProtocol_Object((1,3,6,1,4,1,4874,2,2,81,1,2,1,1,3),_JuniDosProtectionDpgSlotRateProtocol_Type())
juniDosProtectionDpgSlotRateProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDosProtectionDpgSlotRateProtocol.setStatus(_B)
_JuniDosProtectionDpgSlotRateMinRate_Type=Unsigned32
_JuniDosProtectionDpgSlotRateMinRate_Object=MibTableColumn
juniDosProtectionDpgSlotRateMinRate=_JuniDosProtectionDpgSlotRateMinRate_Object((1,3,6,1,4,1,4874,2,2,81,1,2,1,1,4),_JuniDosProtectionDpgSlotRateMinRate_Type())
juniDosProtectionDpgSlotRateMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionDpgSlotRateMinRate.setStatus(_B)
_JuniDosProtectionDpgSlotRateMaxRate_Type=Unsigned32
_JuniDosProtectionDpgSlotRateMaxRate_Object=MibTableColumn
juniDosProtectionDpgSlotRateMaxRate=_JuniDosProtectionDpgSlotRateMaxRate_Object((1,3,6,1,4,1,4874,2,2,81,1,2,1,1,5),_JuniDosProtectionDpgSlotRateMaxRate_Type())
juniDosProtectionDpgSlotRateMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionDpgSlotRateMaxRate.setStatus(_B)
_JuniDosProtectionDpgSlotRateMinBurst_Type=Unsigned32
_JuniDosProtectionDpgSlotRateMinBurst_Object=MibTableColumn
juniDosProtectionDpgSlotRateMinBurst=_JuniDosProtectionDpgSlotRateMinBurst_Object((1,3,6,1,4,1,4874,2,2,81,1,2,1,1,6),_JuniDosProtectionDpgSlotRateMinBurst_Type())
juniDosProtectionDpgSlotRateMinBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionDpgSlotRateMinBurst.setStatus(_B)
_JuniDosProtectionDpgSlotRateMaxBurst_Type=Unsigned32
_JuniDosProtectionDpgSlotRateMaxBurst_Object=MibTableColumn
juniDosProtectionDpgSlotRateMaxBurst=_JuniDosProtectionDpgSlotRateMaxBurst_Object((1,3,6,1,4,1,4874,2,2,81,1,2,1,1,7),_JuniDosProtectionDpgSlotRateMaxBurst_Type())
juniDosProtectionDpgSlotRateMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionDpgSlotRateMaxBurst.setStatus(_B)
_JuniDosProtectionPlatformTrapControl_ObjectIdentity=ObjectIdentity
juniDosProtectionPlatformTrapControl=_JuniDosProtectionPlatformTrapControl_ObjectIdentity((1,3,6,1,4,1,4874,2,2,81,2))
_JuniDosProtectionScfdsSlot_Type=Unsigned32
_JuniDosProtectionScfdsSlot_Object=MibScalar
juniDosProtectionScfdsSlot=_JuniDosProtectionScfdsSlot_Object((1,3,6,1,4,1,4874,2,2,81,2,1),_JuniDosProtectionScfdsSlot_Type())
juniDosProtectionScfdsSlot.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDosProtectionScfdsSlot.setStatus(_B)
_JuniDosProtectionPriority_Type=JuniDosProtectionPriorityType
_JuniDosProtectionPriority_Object=MibScalar
juniDosProtectionPriority=_JuniDosProtectionPriority_Object((1,3,6,1,4,1,4874,2,2,81,2,2),_JuniDosProtectionPriority_Type())
juniDosProtectionPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDosProtectionPriority.setStatus(_B)
_JuniDosProtectionProtocol_Type=JuniDosProtectionProtocolType
_JuniDosProtectionProtocol_Object=MibScalar
juniDosProtectionProtocol=_JuniDosProtectionProtocol_Object((1,3,6,1,4,1,4874,2,2,81,2,3),_JuniDosProtectionProtocol_Type())
juniDosProtectionProtocol.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDosProtectionProtocol.setStatus(_B)
_JuniDosProtectionIfIndex_Type=InterfaceIndex
_JuniDosProtectionIfIndex_Object=MibScalar
juniDosProtectionIfIndex=_JuniDosProtectionIfIndex_Object((1,3,6,1,4,1,4874,2,2,81,2,4),_JuniDosProtectionIfIndex_Type())
juniDosProtectionIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDosProtectionIfIndex.setStatus(_B)
_JuniDosProtectionGroupId_Type=Unsigned32
_JuniDosProtectionGroupId_Object=MibScalar
juniDosProtectionGroupId=_JuniDosProtectionGroupId_Object((1,3,6,1,4,1,4874,2,2,81,2,5),_JuniDosProtectionGroupId_Type())
juniDosProtectionGroupId.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDosProtectionGroupId.setStatus(_B)
class _JuniDosProtectionSrcPhysAddr_Type(MacAddress):subtypeSpec=MacAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_JuniDosProtectionSrcPhysAddr_Type.__name__=_m
_JuniDosProtectionSrcPhysAddr_Object=MibScalar
juniDosProtectionSrcPhysAddr=_JuniDosProtectionSrcPhysAddr_Object((1,3,6,1,4,1,4874,2,2,81,2,6),_JuniDosProtectionSrcPhysAddr_Type())
juniDosProtectionSrcPhysAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDosProtectionSrcPhysAddr.setStatus(_B)
_JuniDosProtectionScfdsFlowRate_Type=Unsigned32
_JuniDosProtectionScfdsFlowRate_Object=MibScalar
juniDosProtectionScfdsFlowRate=_JuniDosProtectionScfdsFlowRate_Object((1,3,6,1,4,1,4874,2,2,81,2,7),_JuniDosProtectionScfdsFlowRate_Type())
juniDosProtectionScfdsFlowRate.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDosProtectionScfdsFlowRate.setStatus(_B)
_JuniDosProtectionPlatformMIBConformance_ObjectIdentity=ObjectIdentity
juniDosProtectionPlatformMIBConformance=_JuniDosProtectionPlatformMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,81,4))
_JuniDosProtectionPlatformMIBCompliances_ObjectIdentity=ObjectIdentity
juniDosProtectionPlatformMIBCompliances=_JuniDosProtectionPlatformMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,81,4,1))
_JuniDosProtectionPlatformMIBGroups_ObjectIdentity=ObjectIdentity
juniDosProtectionPlatformMIBGroups=_JuniDosProtectionPlatformMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,81,4,2))
juniDosProtectionGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,81,4,2,1))
juniDosProtectionGroup.setObjects(*((_A,_O),(_A,_P),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:juniDosProtectionGroup.setStatus(_B)
juniDosProtectionGroup1=ObjectGroup((1,3,6,1,4,1,4874,2,2,81,4,2,3))
juniDosProtectionGroup1.setObjects(*((_A,_O),(_A,_P),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:juniDosProtectionGroup1.setStatus(_B)
juniDosProtectionScfdsSuspiciousControlFlow=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,1))
juniDosProtectionScfdsSuspiciousControlFlow.setObjects(*((_A,_I),(_A,_G)))
if mibBuilder.loadTexts:juniDosProtectionScfdsSuspiciousControlFlow.setStatus(_D)
juniDosProtectionScfdsNonSuspiciousControlFlow=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,2))
juniDosProtectionScfdsNonSuspiciousControlFlow.setObjects(*((_A,_I),(_A,_G)))
if mibBuilder.loadTexts:juniDosProtectionScfdsNonSuspiciousControlFlow.setStatus(_D)
juniDosProtectionScfdsSuspiciousControlFlowGroup=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,3))
juniDosProtectionScfdsSuspiciousControlFlowGroup.setObjects(*((_A,_F),(_A,_Z),(_A,_G)))
if mibBuilder.loadTexts:juniDosProtectionScfdsSuspiciousControlFlowGroup.setStatus(_B)
juniDosProtectionScfdsNonSuspiciousControlFlowGroup=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,4))
juniDosProtectionScfdsNonSuspiciousControlFlowGroup.setObjects(*((_A,_F),(_A,_Z),(_A,_G)))
if mibBuilder.loadTexts:juniDosProtectionScfdsNonSuspiciousControlFlowGroup.setStatus(_B)
juniDosProtectionScfdsTableFull=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,5))
juniDosProtectionScfdsTableFull.setObjects((_A,_F))
if mibBuilder.loadTexts:juniDosProtectionScfdsTableFull.setStatus(_B)
juniDosProtectionScfdsTableNotFull=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,6))
juniDosProtectionScfdsTableNotFull.setObjects((_A,_F))
if mibBuilder.loadTexts:juniDosProtectionScfdsTableNotFull.setStatus(_B)
juniDosProtectionScfdsGroupingInUse=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,7))
juniDosProtectionScfdsGroupingInUse.setObjects((_A,_F))
if mibBuilder.loadTexts:juniDosProtectionScfdsGroupingInUse.setStatus(_B)
juniDosProtectionScfdsSuspiciousProtocol=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,8))
juniDosProtectionScfdsSuspiciousProtocol.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:juniDosProtectionScfdsSuspiciousProtocol.setStatus(_B)
juniDosProtectionScfdsNonSuspiciousProtocol=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,9))
juniDosProtectionScfdsNonSuspiciousProtocol.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:juniDosProtectionScfdsNonSuspiciousProtocol.setStatus(_B)
juniDosProtectionScfdsSuspiciousPriority=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,10))
juniDosProtectionScfdsSuspiciousPriority.setObjects(*((_A,_F),(_A,_a)))
if mibBuilder.loadTexts:juniDosProtectionScfdsSuspiciousPriority.setStatus(_B)
juniDosProtectionScfdsNonSuspiciousPriority=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,11))
juniDosProtectionScfdsNonSuspiciousPriority.setObjects(*((_A,_F),(_A,_a)))
if mibBuilder.loadTexts:juniDosProtectionScfdsNonSuspiciousPriority.setStatus(_B)
juniDosProtectionScfdsSuspiciousControlFlowMac=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,12))
juniDosProtectionScfdsSuspiciousControlFlowMac.setObjects(*((_A,_I),(_A,_G),(_A,_b),(_A,_AG)))
if mibBuilder.loadTexts:juniDosProtectionScfdsSuspiciousControlFlowMac.setStatus(_B)
juniDosProtectionScfdsNonSuspiciousControlFlowMac=NotificationType((1,3,6,1,4,1,4874,2,2,81,0,0,13))
juniDosProtectionScfdsNonSuspiciousControlFlowMac.setObjects(*((_A,_I),(_A,_G),(_A,_b)))
if mibBuilder.loadTexts:juniDosProtectionScfdsNonSuspiciousControlFlowMac.setStatus(_D)
juniDosProtectionNotificationGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,81,4,2,2))
juniDosProtectionNotificationGroup.setObjects(*((_A,_AH),(_A,_AI),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:juniDosProtectionNotificationGroup.setStatus(_B)
juniDosProtectionNotificationGroup1=NotificationGroup((1,3,6,1,4,1,4874,2,2,81,4,2,4))
juniDosProtectionNotificationGroup1.setObjects(*((_A,_AJ),(_A,_AK),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:juniDosProtectionNotificationGroup1.setStatus(_B)
juniDosProtectionCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,81,4,1,1))
juniDosProtectionCompliance.setObjects(*((_A,'juniDosProtectionPlatformGroup'),(_A,'juniDosProtectionPlatformNotificationGroup')))
if mibBuilder.loadTexts:juniDosProtectionCompliance.setStatus(_D)
juniDosProtectionCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,81,4,1,2))
juniDosProtectionCompliance2.setObjects(*((_A,'juniDosProtectionPlatformGroup1'),(_A,'juniDosProtectionPlatformNotificationGroup1')))
if mibBuilder.loadTexts:juniDosProtectionCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniDosProtectionPlatformMIB':juniDosProtectionPlatformMIB,'juniDosProtectionPlatformTraps':juniDosProtectionPlatformTraps,'juniDosProtectionPlatformScfdsTraps':juniDosProtectionPlatformScfdsTraps,_AH:juniDosProtectionScfdsSuspiciousControlFlow,_AI:juniDosProtectionScfdsNonSuspiciousControlFlow,_c:juniDosProtectionScfdsSuspiciousControlFlowGroup,_d:juniDosProtectionScfdsNonSuspiciousControlFlowGroup,_e:juniDosProtectionScfdsTableFull,_f:juniDosProtectionScfdsTableNotFull,_g:juniDosProtectionScfdsGroupingInUse,_h:juniDosProtectionScfdsSuspiciousProtocol,_i:juniDosProtectionScfdsNonSuspiciousProtocol,_j:juniDosProtectionScfdsSuspiciousPriority,_k:juniDosProtectionScfdsNonSuspiciousPriority,_AJ:juniDosProtectionScfdsSuspiciousControlFlowMac,_AK:juniDosProtectionScfdsNonSuspiciousControlFlowMac,'juniDosProtectionPlatformObjects':juniDosProtectionPlatformObjects,'juniDosProtectionPlatformScfdsGroup':juniDosProtectionPlatformScfdsGroup,'juniDosProtectionScfdsSlotProtocolTable':juniDosProtectionScfdsSlotProtocolTable,'juniDosProtectionScfdsSlotProtocolEntry':juniDosProtectionScfdsSlotProtocolEntry,_n:juniDosProtectionScfdsSlotProtocolSlot,_o:juniDosProtectionScfdsSlotProtocolIndex,_O:juniDosProtectionScfdsSlotProtocolState,_P:juniDosProtectionScfdsSlotProtocolTransitions,'juniDosProtectionScfdsSlotFlowTable':juniDosProtectionScfdsSlotFlowTable,'juniDosProtectionScfdsSlotFlowEntry':juniDosProtectionScfdsSlotFlowEntry,_L:juniDosProtectionScfdsSlotFlowSlot,_p:juniDosProtectionScfdsSlotFlowIfIndex,_q:juniDosProtectionScfdsSlotFlowGroupId,_r:juniDosProtectionScfdsSlotFlowProtocol,_A0:juniDosProtectionScfdsSlotFlowRate,_A1:juniDosProtectionScfdsSlotFlowPeakRate,_A2:juniDosProtectionScfdsSlotFlowTimeFlagged,_A4:juniDosProtectionScfdsSlotFlowIngressSlot,_A5:juniDosProtectionScfdsSlotFlowGroup,_A3:juniDosProtectionScfdsSlotFlowClearEntry,'juniDosProtectionScfdsSlotTable':juniDosProtectionScfdsSlotTable,'juniDosProtectionScfdsSlotEntry':juniDosProtectionScfdsSlotEntry,'juniDosProtectionScfdsSlotSlot':juniDosProtectionScfdsSlotSlot,'juniDosProtectionScfdsSlotClearAll':juniDosProtectionScfdsSlotClearAll,_Q:juniDosProtectionScfdsSlotDiscontinuityTime,_R:juniDosProtectionScfdsSlotTableOverflowState,_S:juniDosProtectionScfdsSlotCurrentSuspiciousFlows,_T:juniDosProtectionScfdsSlotNumberSuspiciousFlows,_U:juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups,_V:juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups,_W:juniDosProtectionScfdsSlotCurrentFalseNegativeFlows,_X:juniDosProtectionScfdsSlotNumberFalseNegativeFlows,_Y:juniDosProtectionScfdsSlotOverflows,'juniDosProtectionScfdsSlotFlowMacTable':juniDosProtectionScfdsSlotFlowMacTable,'juniDosProtectionScfdsSlotFlowMacEntry':juniDosProtectionScfdsSlotFlowMacEntry,_s:juniDosProtectionScfdsSlotFlowMacSlot,_t:juniDosProtectionScfdsSlotFlowMacIfIndex,_u:juniDosProtectionScfdsSlotFlowMacGroupId,_v:juniDosProtectionScfdsSlotFlowMacProtocol,_w:juniDosProtectionScfdsSlotFlowMacSrcMac,_A6:juniDosProtectionScfdsSlotFlowMacRate,_A7:juniDosProtectionScfdsSlotFlowMacPeakRate,_A8:juniDosProtectionScfdsSlotFlowMacTimeFlagged,_AA:juniDosProtectionScfdsSlotFlowMacIngressSlot,_AB:juniDosProtectionScfdsSlotFlowMacGroup,_A9:juniDosProtectionScfdsSlotFlowMacClearEntry,'juniDosProtectionPlatformDpgGroup':juniDosProtectionPlatformDpgGroup,'juniDosProtectionDpgSlotRateTable':juniDosProtectionDpgSlotRateTable,'juniDosProtectionDpgSlotRateEntry':juniDosProtectionDpgSlotRateEntry,_x:juniDosProtectionDpgSlotRateSlot,_y:juniDosProtectionDpgSlotRateDpgName,_z:juniDosProtectionDpgSlotRateProtocol,_AC:juniDosProtectionDpgSlotRateMinRate,_AD:juniDosProtectionDpgSlotRateMaxRate,_AE:juniDosProtectionDpgSlotRateMinBurst,_AF:juniDosProtectionDpgSlotRateMaxBurst,'juniDosProtectionPlatformTrapControl':juniDosProtectionPlatformTrapControl,_F:juniDosProtectionScfdsSlot,_a:juniDosProtectionPriority,_G:juniDosProtectionProtocol,_I:juniDosProtectionIfIndex,_Z:juniDosProtectionGroupId,_b:juniDosProtectionSrcPhysAddr,_AG:juniDosProtectionScfdsFlowRate,'juniDosProtectionPlatformMIBConformance':juniDosProtectionPlatformMIBConformance,'juniDosProtectionPlatformMIBCompliances':juniDosProtectionPlatformMIBCompliances,'juniDosProtectionCompliance':juniDosProtectionCompliance,'juniDosProtectionCompliance2':juniDosProtectionCompliance2,'juniDosProtectionPlatformMIBGroups':juniDosProtectionPlatformMIBGroups,'juniDosProtectionGroup':juniDosProtectionGroup,'juniDosProtectionNotificationGroup':juniDosProtectionNotificationGroup,'juniDosProtectionGroup1':juniDosProtectionGroup1,'juniDosProtectionNotificationGroup1':juniDosProtectionNotificationGroup1})