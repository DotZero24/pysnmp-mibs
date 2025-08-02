_AZ='f3ErpUnitStatsGroup'
_AY='f3ErpUnitGroup'
_AX='f3ErpGroupGroup'
_AW='f3ErpUnitRapsRsvdEventSubcode'
_AV='f3ErpUnitRapsRsvdRequestPDUsRx'
_AU='f3ErpUnitRapsInvalidOamVersionPDUsRx'
_AT='f3ErpUnitRapsEventPDUsRx'
_AS='f3ErpUnitRapsForcedSwitchPDUsRx'
_AR='f3ErpUnitRapsManualSwitchPDUsRx'
_AQ='f3ErpUnitRapsSignalFailPDUsRx'
_AP='f3ErpUnitRapsNoReqRBPDUsRx'
_AO='f3ErpUnitRapsNoReqPDUsRx'
_AN='f3ErpUnitRapsEventPDUsTx'
_AM='f3ErpUnitRapsForcedSwitchPDUsTx'
_AL='f3ErpUnitRapsManualSwitchPDUsTx'
_AK='f3ErpUnitRapsSignalFailPDUsTx'
_AJ='f3ErpUnitRapsNoReqRBPDUsTx'
_AI='f3ErpUnitRapsNoReqPDUsTx'
_AH='f3ErpUnitRapsPDUsDiscarded'
_AG='f3ErpUnitRapsPDUsRx'
_AF='f3ErpUnitRapsPDUsTx'
_AE='f3ErpUnitNumBlockedStateTrans'
_AD='f3ErpUnitPortRapsFp'
_AC='f3ErpUnitPortRxRapsNodeId'
_AB='f3ErpUnitPortRxRapsBPR'
_AA='f3ErpUnitPortRxRapsDNF'
_A9='f3ErpUnitPortRxRapsRplBlocked'
_A8='f3ErpUnitPortRxRapsRequest'
_A7='f3ErpUnitPortStatus'
_A6='f3ErpUnitPortRole'
_A5='f3ErpUnitPortMEP'
_A4='f3ErpUnitPort'
_A3='f3ErpGroupRapsMultipleFailure'
_A2='f3ErpGroupRapsInterconnectionNode'
_A1='f3ErpGroupMaxFpNum'
_A0='f3ErpGroupRapsVirtualChannelMep'
_z='f3ErpGroupInterconnectPropagateTc'
_y='f3ErpGroupInterconnectionErp'
_x='f3ErpGroupRowStatus'
_w='f3ErpGroupStorageType'
_v='f3ErpGroupUserLabel'
_u='f3ErpGroupActionObject'
_t='f3ErpGroupAction'
_s='f3ErpGroupTxRapsBPR'
_r='f3ErpGroupTxRapsDNF'
_q='f3ErpGroupTxRapsRplBlocked'
_p='f3ErpGroupTxRapsRequest'
_o='f3ErpGroupWTRRemainingTime'
_n='f3ErpGroupNodeState'
_m='f3ErpGroupProtectMgmtTunnel'
_l='f3ErpGroupRingPort1Role'
_k='f3ErpGroupRingPort1MEP'
_j='f3ErpGroupRingPort1'
_i='f3ErpGroupRingPort0Role'
_h='f3ErpGroupRingPort0MEP'
_g='f3ErpGroupRingPort0'
_f='f3ErpGroupHoldOffTime'
_e='f3ErpGroupWaitToRestore'
_d='f3ErpGroupGuardTime'
_c='f3ErpGroupSubRingWithoutVirtChan'
_b='f3ErpGroupRevertive'
_a='f3ErpGroupCompatibleVersion'
_Z='f3ErpGroupRapsMdLevel'
_Y='f3ErpGroupRapsVlanEtherType'
_X='f3ErpGroupRapsVlanPrio'
_W='f3ErpGroupRapsVlanId'
_V='f3ErpGroupRapsNodeId'
_U='f3ErpGroupRapsRingId'
_T='f3ErpGroupSecondaryState'
_S='f3ErpGroupOperationalState'
_R='f3ErpGroupAdminState'
_Q='not-accessible'
_P='secondary'
_O='primary'
_N='forced'
_M='manual'
_L='DisplayString'
_K='f3ErpUnitIndex'
_J='f3ErpGroupProtectedFlow'
_I='f3ErpGroupIndex'
_H='neIndex'
_G='CM-ENTITY-MIB'
_F='read-write'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='F3-ERP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
AdminState,OperationalState,SecondaryState,VlanEthertype,VlanId,VlanPriority=mibBuilder.importSymbols('CM-COMMON-MIB','AdminState','OperationalState','SecondaryState','VlanEthertype','VlanId','VlanPriority')
neIndex,=mibBuilder.importSymbols(_G,_H)
CmProtUnitState,CmProtUnitType=mibBuilder.importSymbols('CM-PROTECTION-MIB','CmProtUnitState','CmProtUnitType')
Dot1agCfmMDLevel,=mibBuilder.importSymbols('IEEE8021-CFM-MIB','Dot1agCfmMDLevel')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue','VariablePointer')
f3ErpMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,25))
if mibBuilder.loadTexts:f3ErpMIB.setRevisions(('2012-09-13 00:00',))
class G8032Version(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v1',1),('v2',2)))
class RPLRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('neighbor',2),('owner',3)))
class RingPortStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('unblocked',1),('unblockedSF',2),('unblockedSD',3),('blockedRPL',4),('blockedSF',5),('blockedSD',6),('blockedMS',7),('blockedFS',8),('blockedPending',9),('subringInterConnect',10),('subringInterConnectSF',11)))
class RingNodeState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('protection',2),(_M,3),(_N,4),('pending',5)))
class RAPSRequest(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noRequest',1),(_M,2),(_N,3),('signailFail',4),('signailDegrade',5),('notApplicable',6)))
class ERPGroupAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noAction',1),('forcedSwitch',2),('manualSwitch',3),('clearSwitch',4),('resetStats',5)))
class RapsInterconnectionNode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_O,2),(_P,3)))
class RapsMultipleFailure(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),(_O,2),(_P,3)))
_F3ErpConfigObjects_ObjectIdentity=ObjectIdentity
f3ErpConfigObjects=_F3ErpConfigObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,25,1))
_F3ErpGroupTable_Object=MibTable
f3ErpGroupTable=_F3ErpGroupTable_Object((1,3,6,1,4,1,2544,1,12,25,1,1))
if mibBuilder.loadTexts:f3ErpGroupTable.setStatus(_A)
_F3ErpGroupEntry_Object=MibTableRow
f3ErpGroupEntry=_F3ErpGroupEntry_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1))
f3ErpGroupEntry.setIndexNames((0,_G,_H),(0,_B,_I))
if mibBuilder.loadTexts:f3ErpGroupEntry.setStatus(_A)
class _F3ErpGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_F3ErpGroupIndex_Type.__name__=_E
_F3ErpGroupIndex_Object=MibTableColumn
f3ErpGroupIndex=_F3ErpGroupIndex_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,1),_F3ErpGroupIndex_Type())
f3ErpGroupIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:f3ErpGroupIndex.setStatus(_A)
_F3ErpGroupAdminState_Type=AdminState
_F3ErpGroupAdminState_Object=MibTableColumn
f3ErpGroupAdminState=_F3ErpGroupAdminState_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,2),_F3ErpGroupAdminState_Type())
f3ErpGroupAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupAdminState.setStatus(_A)
_F3ErpGroupOperationalState_Type=OperationalState
_F3ErpGroupOperationalState_Object=MibTableColumn
f3ErpGroupOperationalState=_F3ErpGroupOperationalState_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,3),_F3ErpGroupOperationalState_Type())
f3ErpGroupOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpGroupOperationalState.setStatus(_A)
_F3ErpGroupSecondaryState_Type=SecondaryState
_F3ErpGroupSecondaryState_Object=MibTableColumn
f3ErpGroupSecondaryState=_F3ErpGroupSecondaryState_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,4),_F3ErpGroupSecondaryState_Type())
f3ErpGroupSecondaryState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpGroupSecondaryState.setStatus(_A)
class _F3ErpGroupRapsRingId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_F3ErpGroupRapsRingId_Type.__name__=_E
_F3ErpGroupRapsRingId_Object=MibTableColumn
f3ErpGroupRapsRingId=_F3ErpGroupRapsRingId_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,5),_F3ErpGroupRapsRingId_Type())
f3ErpGroupRapsRingId.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRapsRingId.setStatus(_A)
_F3ErpGroupRapsNodeId_Type=MacAddress
_F3ErpGroupRapsNodeId_Object=MibTableColumn
f3ErpGroupRapsNodeId=_F3ErpGroupRapsNodeId_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,6),_F3ErpGroupRapsNodeId_Type())
f3ErpGroupRapsNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRapsNodeId.setStatus(_A)
_F3ErpGroupRapsVlanId_Type=VlanId
_F3ErpGroupRapsVlanId_Object=MibTableColumn
f3ErpGroupRapsVlanId=_F3ErpGroupRapsVlanId_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,7),_F3ErpGroupRapsVlanId_Type())
f3ErpGroupRapsVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRapsVlanId.setStatus(_A)
_F3ErpGroupRapsVlanPrio_Type=VlanPriority
_F3ErpGroupRapsVlanPrio_Object=MibTableColumn
f3ErpGroupRapsVlanPrio=_F3ErpGroupRapsVlanPrio_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,8),_F3ErpGroupRapsVlanPrio_Type())
f3ErpGroupRapsVlanPrio.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRapsVlanPrio.setStatus(_A)
_F3ErpGroupRapsVlanEtherType_Type=Unsigned32
_F3ErpGroupRapsVlanEtherType_Object=MibTableColumn
f3ErpGroupRapsVlanEtherType=_F3ErpGroupRapsVlanEtherType_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,9),_F3ErpGroupRapsVlanEtherType_Type())
f3ErpGroupRapsVlanEtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRapsVlanEtherType.setStatus(_A)
_F3ErpGroupRapsMdLevel_Type=Dot1agCfmMDLevel
_F3ErpGroupRapsMdLevel_Object=MibTableColumn
f3ErpGroupRapsMdLevel=_F3ErpGroupRapsMdLevel_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,10),_F3ErpGroupRapsMdLevel_Type())
f3ErpGroupRapsMdLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRapsMdLevel.setStatus(_A)
_F3ErpGroupCompatibleVersion_Type=G8032Version
_F3ErpGroupCompatibleVersion_Object=MibTableColumn
f3ErpGroupCompatibleVersion=_F3ErpGroupCompatibleVersion_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,11),_F3ErpGroupCompatibleVersion_Type())
f3ErpGroupCompatibleVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ErpGroupCompatibleVersion.setStatus(_A)
_F3ErpGroupRevertive_Type=TruthValue
_F3ErpGroupRevertive_Object=MibTableColumn
f3ErpGroupRevertive=_F3ErpGroupRevertive_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,12),_F3ErpGroupRevertive_Type())
f3ErpGroupRevertive.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRevertive.setStatus(_A)
_F3ErpGroupSubRingWithoutVirtChan_Type=TruthValue
_F3ErpGroupSubRingWithoutVirtChan_Object=MibTableColumn
f3ErpGroupSubRingWithoutVirtChan=_F3ErpGroupSubRingWithoutVirtChan_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,13),_F3ErpGroupSubRingWithoutVirtChan_Type())
f3ErpGroupSubRingWithoutVirtChan.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupSubRingWithoutVirtChan.setStatus(_A)
class _F3ErpGroupGuardTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_F3ErpGroupGuardTime_Type.__name__=_E
_F3ErpGroupGuardTime_Object=MibTableColumn
f3ErpGroupGuardTime=_F3ErpGroupGuardTime_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,14),_F3ErpGroupGuardTime_Type())
f3ErpGroupGuardTime.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupGuardTime.setStatus(_A)
class _F3ErpGroupWaitToRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_F3ErpGroupWaitToRestore_Type.__name__=_E
_F3ErpGroupWaitToRestore_Object=MibTableColumn
f3ErpGroupWaitToRestore=_F3ErpGroupWaitToRestore_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,15),_F3ErpGroupWaitToRestore_Type())
f3ErpGroupWaitToRestore.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupWaitToRestore.setStatus(_A)
class _F3ErpGroupHoldOffTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_F3ErpGroupHoldOffTime_Type.__name__=_E
_F3ErpGroupHoldOffTime_Object=MibTableColumn
f3ErpGroupHoldOffTime=_F3ErpGroupHoldOffTime_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,16),_F3ErpGroupHoldOffTime_Type())
f3ErpGroupHoldOffTime.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupHoldOffTime.setStatus(_A)
_F3ErpGroupRingPort0_Type=VariablePointer
_F3ErpGroupRingPort0_Object=MibTableColumn
f3ErpGroupRingPort0=_F3ErpGroupRingPort0_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,17),_F3ErpGroupRingPort0_Type())
f3ErpGroupRingPort0.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRingPort0.setStatus(_A)
_F3ErpGroupRingPort0MEP_Type=VariablePointer
_F3ErpGroupRingPort0MEP_Object=MibTableColumn
f3ErpGroupRingPort0MEP=_F3ErpGroupRingPort0MEP_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,18),_F3ErpGroupRingPort0MEP_Type())
f3ErpGroupRingPort0MEP.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRingPort0MEP.setStatus(_A)
_F3ErpGroupRingPort0Role_Type=RPLRole
_F3ErpGroupRingPort0Role_Object=MibTableColumn
f3ErpGroupRingPort0Role=_F3ErpGroupRingPort0Role_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,19),_F3ErpGroupRingPort0Role_Type())
f3ErpGroupRingPort0Role.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRingPort0Role.setStatus(_A)
_F3ErpGroupRingPort1_Type=VariablePointer
_F3ErpGroupRingPort1_Object=MibTableColumn
f3ErpGroupRingPort1=_F3ErpGroupRingPort1_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,20),_F3ErpGroupRingPort1_Type())
f3ErpGroupRingPort1.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRingPort1.setStatus(_A)
_F3ErpGroupRingPort1MEP_Type=VariablePointer
_F3ErpGroupRingPort1MEP_Object=MibTableColumn
f3ErpGroupRingPort1MEP=_F3ErpGroupRingPort1MEP_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,21),_F3ErpGroupRingPort1MEP_Type())
f3ErpGroupRingPort1MEP.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRingPort1MEP.setStatus(_A)
_F3ErpGroupRingPort1Role_Type=RPLRole
_F3ErpGroupRingPort1Role_Object=MibTableColumn
f3ErpGroupRingPort1Role=_F3ErpGroupRingPort1Role_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,22),_F3ErpGroupRingPort1Role_Type())
f3ErpGroupRingPort1Role.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRingPort1Role.setStatus(_A)
_F3ErpGroupProtectMgmtTunnel_Type=TruthValue
_F3ErpGroupProtectMgmtTunnel_Object=MibTableColumn
f3ErpGroupProtectMgmtTunnel=_F3ErpGroupProtectMgmtTunnel_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,23),_F3ErpGroupProtectMgmtTunnel_Type())
f3ErpGroupProtectMgmtTunnel.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupProtectMgmtTunnel.setStatus(_A)
_F3ErpGroupNodeState_Type=RingNodeState
_F3ErpGroupNodeState_Object=MibTableColumn
f3ErpGroupNodeState=_F3ErpGroupNodeState_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,24),_F3ErpGroupNodeState_Type())
f3ErpGroupNodeState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpGroupNodeState.setStatus(_A)
_F3ErpGroupWTRRemainingTime_Type=Integer32
_F3ErpGroupWTRRemainingTime_Object=MibTableColumn
f3ErpGroupWTRRemainingTime=_F3ErpGroupWTRRemainingTime_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,25),_F3ErpGroupWTRRemainingTime_Type())
f3ErpGroupWTRRemainingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpGroupWTRRemainingTime.setStatus(_A)
_F3ErpGroupTxRapsRequest_Type=RAPSRequest
_F3ErpGroupTxRapsRequest_Object=MibTableColumn
f3ErpGroupTxRapsRequest=_F3ErpGroupTxRapsRequest_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,26),_F3ErpGroupTxRapsRequest_Type())
f3ErpGroupTxRapsRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpGroupTxRapsRequest.setStatus(_A)
_F3ErpGroupTxRapsRplBlocked_Type=TruthValue
_F3ErpGroupTxRapsRplBlocked_Object=MibTableColumn
f3ErpGroupTxRapsRplBlocked=_F3ErpGroupTxRapsRplBlocked_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,27),_F3ErpGroupTxRapsRplBlocked_Type())
f3ErpGroupTxRapsRplBlocked.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpGroupTxRapsRplBlocked.setStatus(_A)
_F3ErpGroupTxRapsDNF_Type=TruthValue
_F3ErpGroupTxRapsDNF_Object=MibTableColumn
f3ErpGroupTxRapsDNF=_F3ErpGroupTxRapsDNF_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,28),_F3ErpGroupTxRapsDNF_Type())
f3ErpGroupTxRapsDNF.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpGroupTxRapsDNF.setStatus(_A)
class _F3ErpGroupTxRapsBPR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_F3ErpGroupTxRapsBPR_Type.__name__=_E
_F3ErpGroupTxRapsBPR_Object=MibTableColumn
f3ErpGroupTxRapsBPR=_F3ErpGroupTxRapsBPR_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,29),_F3ErpGroupTxRapsBPR_Type())
f3ErpGroupTxRapsBPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpGroupTxRapsBPR.setStatus(_A)
_F3ErpGroupAction_Type=ERPGroupAction
_F3ErpGroupAction_Object=MibTableColumn
f3ErpGroupAction=_F3ErpGroupAction_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,30),_F3ErpGroupAction_Type())
f3ErpGroupAction.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ErpGroupAction.setStatus(_A)
_F3ErpGroupActionObject_Type=VariablePointer
_F3ErpGroupActionObject_Object=MibTableColumn
f3ErpGroupActionObject=_F3ErpGroupActionObject_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,31),_F3ErpGroupActionObject_Type())
f3ErpGroupActionObject.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ErpGroupActionObject.setStatus(_A)
class _F3ErpGroupUserLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_F3ErpGroupUserLabel_Type.__name__=_L
_F3ErpGroupUserLabel_Object=MibTableColumn
f3ErpGroupUserLabel=_F3ErpGroupUserLabel_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,32),_F3ErpGroupUserLabel_Type())
f3ErpGroupUserLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupUserLabel.setStatus(_A)
_F3ErpGroupStorageType_Type=StorageType
_F3ErpGroupStorageType_Object=MibTableColumn
f3ErpGroupStorageType=_F3ErpGroupStorageType_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,33),_F3ErpGroupStorageType_Type())
f3ErpGroupStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupStorageType.setStatus(_A)
_F3ErpGroupRowStatus_Type=RowStatus
_F3ErpGroupRowStatus_Object=MibTableColumn
f3ErpGroupRowStatus=_F3ErpGroupRowStatus_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,34),_F3ErpGroupRowStatus_Type())
f3ErpGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRowStatus.setStatus(_A)
_F3ErpGroupInterconnectionErp_Type=VariablePointer
_F3ErpGroupInterconnectionErp_Object=MibTableColumn
f3ErpGroupInterconnectionErp=_F3ErpGroupInterconnectionErp_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,35),_F3ErpGroupInterconnectionErp_Type())
f3ErpGroupInterconnectionErp.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ErpGroupInterconnectionErp.setStatus(_A)
_F3ErpGroupInterconnectPropagateTc_Type=TruthValue
_F3ErpGroupInterconnectPropagateTc_Object=MibTableColumn
f3ErpGroupInterconnectPropagateTc=_F3ErpGroupInterconnectPropagateTc_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,36),_F3ErpGroupInterconnectPropagateTc_Type())
f3ErpGroupInterconnectPropagateTc.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ErpGroupInterconnectPropagateTc.setStatus(_A)
_F3ErpGroupRapsVirtualChannelMep_Type=VariablePointer
_F3ErpGroupRapsVirtualChannelMep_Object=MibTableColumn
f3ErpGroupRapsVirtualChannelMep=_F3ErpGroupRapsVirtualChannelMep_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,37),_F3ErpGroupRapsVirtualChannelMep_Type())
f3ErpGroupRapsVirtualChannelMep.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ErpGroupRapsVirtualChannelMep.setStatus(_A)
_F3ErpGroupMaxFpNum_Type=Integer32
_F3ErpGroupMaxFpNum_Object=MibTableColumn
f3ErpGroupMaxFpNum=_F3ErpGroupMaxFpNum_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,38),_F3ErpGroupMaxFpNum_Type())
f3ErpGroupMaxFpNum.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ErpGroupMaxFpNum.setStatus(_A)
_F3ErpGroupRapsInterconnectionNode_Type=RapsInterconnectionNode
_F3ErpGroupRapsInterconnectionNode_Object=MibTableColumn
f3ErpGroupRapsInterconnectionNode=_F3ErpGroupRapsInterconnectionNode_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,39),_F3ErpGroupRapsInterconnectionNode_Type())
f3ErpGroupRapsInterconnectionNode.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRapsInterconnectionNode.setStatus(_A)
_F3ErpGroupRapsMultipleFailure_Type=RapsMultipleFailure
_F3ErpGroupRapsMultipleFailure_Object=MibTableColumn
f3ErpGroupRapsMultipleFailure=_F3ErpGroupRapsMultipleFailure_Object((1,3,6,1,4,1,2544,1,12,25,1,1,1,40),_F3ErpGroupRapsMultipleFailure_Type())
f3ErpGroupRapsMultipleFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:f3ErpGroupRapsMultipleFailure.setStatus(_A)
_F3ErpGroupProtectedFlowTable_Object=MibTable
f3ErpGroupProtectedFlowTable=_F3ErpGroupProtectedFlowTable_Object((1,3,6,1,4,1,2544,1,12,25,1,2))
if mibBuilder.loadTexts:f3ErpGroupProtectedFlowTable.setStatus(_A)
_F3ErpGroupProtectedFlowEntry_Object=MibTableRow
f3ErpGroupProtectedFlowEntry=_F3ErpGroupProtectedFlowEntry_Object((1,3,6,1,4,1,2544,1,12,25,1,2,1))
f3ErpGroupProtectedFlowEntry.setIndexNames((0,_G,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:f3ErpGroupProtectedFlowEntry.setStatus(_A)
_F3ErpGroupProtectedFlow_Type=VariablePointer
_F3ErpGroupProtectedFlow_Object=MibTableColumn
f3ErpGroupProtectedFlow=_F3ErpGroupProtectedFlow_Object((1,3,6,1,4,1,2544,1,12,25,1,2,1,1),_F3ErpGroupProtectedFlow_Type())
f3ErpGroupProtectedFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpGroupProtectedFlow.setStatus(_A)
_F3ErpUnitTable_Object=MibTable
f3ErpUnitTable=_F3ErpUnitTable_Object((1,3,6,1,4,1,2544,1,12,25,1,3))
if mibBuilder.loadTexts:f3ErpUnitTable.setStatus(_A)
_F3ErpUnitEntry_Object=MibTableRow
f3ErpUnitEntry=_F3ErpUnitEntry_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1))
f3ErpUnitEntry.setIndexNames((0,_G,_H),(0,_B,_I),(0,_B,_K))
if mibBuilder.loadTexts:f3ErpUnitEntry.setStatus(_A)
class _F3ErpUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_F3ErpUnitIndex_Type.__name__=_E
_F3ErpUnitIndex_Object=MibTableColumn
f3ErpUnitIndex=_F3ErpUnitIndex_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,1),_F3ErpUnitIndex_Type())
f3ErpUnitIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:f3ErpUnitIndex.setStatus(_A)
_F3ErpUnitPort_Type=VariablePointer
_F3ErpUnitPort_Object=MibTableColumn
f3ErpUnitPort=_F3ErpUnitPort_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,2),_F3ErpUnitPort_Type())
f3ErpUnitPort.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPort.setStatus(_A)
_F3ErpUnitPortMEP_Type=VariablePointer
_F3ErpUnitPortMEP_Object=MibTableColumn
f3ErpUnitPortMEP=_F3ErpUnitPortMEP_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,3),_F3ErpUnitPortMEP_Type())
f3ErpUnitPortMEP.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPortMEP.setStatus(_A)
_F3ErpUnitPortRole_Type=RPLRole
_F3ErpUnitPortRole_Object=MibTableColumn
f3ErpUnitPortRole=_F3ErpUnitPortRole_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,4),_F3ErpUnitPortRole_Type())
f3ErpUnitPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPortRole.setStatus(_A)
_F3ErpUnitPortStatus_Type=RingPortStatus
_F3ErpUnitPortStatus_Object=MibTableColumn
f3ErpUnitPortStatus=_F3ErpUnitPortStatus_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,5),_F3ErpUnitPortStatus_Type())
f3ErpUnitPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPortStatus.setStatus(_A)
_F3ErpUnitPortRxRapsRequest_Type=RAPSRequest
_F3ErpUnitPortRxRapsRequest_Object=MibTableColumn
f3ErpUnitPortRxRapsRequest=_F3ErpUnitPortRxRapsRequest_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,6),_F3ErpUnitPortRxRapsRequest_Type())
f3ErpUnitPortRxRapsRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPortRxRapsRequest.setStatus(_A)
_F3ErpUnitPortRxRapsRplBlocked_Type=TruthValue
_F3ErpUnitPortRxRapsRplBlocked_Object=MibTableColumn
f3ErpUnitPortRxRapsRplBlocked=_F3ErpUnitPortRxRapsRplBlocked_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,7),_F3ErpUnitPortRxRapsRplBlocked_Type())
f3ErpUnitPortRxRapsRplBlocked.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPortRxRapsRplBlocked.setStatus(_A)
_F3ErpUnitPortRxRapsDNF_Type=TruthValue
_F3ErpUnitPortRxRapsDNF_Object=MibTableColumn
f3ErpUnitPortRxRapsDNF=_F3ErpUnitPortRxRapsDNF_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,8),_F3ErpUnitPortRxRapsDNF_Type())
f3ErpUnitPortRxRapsDNF.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPortRxRapsDNF.setStatus(_A)
class _F3ErpUnitPortRxRapsBPR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_F3ErpUnitPortRxRapsBPR_Type.__name__=_E
_F3ErpUnitPortRxRapsBPR_Object=MibTableColumn
f3ErpUnitPortRxRapsBPR=_F3ErpUnitPortRxRapsBPR_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,9),_F3ErpUnitPortRxRapsBPR_Type())
f3ErpUnitPortRxRapsBPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPortRxRapsBPR.setStatus(_A)
_F3ErpUnitPortRxRapsNodeId_Type=MacAddress
_F3ErpUnitPortRxRapsNodeId_Object=MibTableColumn
f3ErpUnitPortRxRapsNodeId=_F3ErpUnitPortRxRapsNodeId_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,10),_F3ErpUnitPortRxRapsNodeId_Type())
f3ErpUnitPortRxRapsNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPortRxRapsNodeId.setStatus(_A)
_F3ErpUnitPortRapsFp_Type=VariablePointer
_F3ErpUnitPortRapsFp_Object=MibTableColumn
f3ErpUnitPortRapsFp=_F3ErpUnitPortRapsFp_Object((1,3,6,1,4,1,2544,1,12,25,1,3,1,11),_F3ErpUnitPortRapsFp_Type())
f3ErpUnitPortRapsFp.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitPortRapsFp.setStatus(_A)
_F3ErpStatsObjects_ObjectIdentity=ObjectIdentity
f3ErpStatsObjects=_F3ErpStatsObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,25,2))
_F3ErpUnitStatsTable_Object=MibTable
f3ErpUnitStatsTable=_F3ErpUnitStatsTable_Object((1,3,6,1,4,1,2544,1,12,25,2,1))
if mibBuilder.loadTexts:f3ErpUnitStatsTable.setStatus(_A)
_F3ErpUnitStatsEntry_Object=MibTableRow
f3ErpUnitStatsEntry=_F3ErpUnitStatsEntry_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1))
f3ErpUnitStatsEntry.setIndexNames((0,_G,_H),(0,_B,_I),(0,_B,_K))
if mibBuilder.loadTexts:f3ErpUnitStatsEntry.setStatus(_A)
_F3ErpUnitNumBlockedStateTrans_Type=Unsigned32
_F3ErpUnitNumBlockedStateTrans_Object=MibTableColumn
f3ErpUnitNumBlockedStateTrans=_F3ErpUnitNumBlockedStateTrans_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,1),_F3ErpUnitNumBlockedStateTrans_Type())
f3ErpUnitNumBlockedStateTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitNumBlockedStateTrans.setStatus(_A)
_F3ErpUnitRapsPDUsTx_Type=Unsigned32
_F3ErpUnitRapsPDUsTx_Object=MibTableColumn
f3ErpUnitRapsPDUsTx=_F3ErpUnitRapsPDUsTx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,2),_F3ErpUnitRapsPDUsTx_Type())
f3ErpUnitRapsPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsPDUsTx.setStatus(_A)
_F3ErpUnitRapsPDUsRx_Type=Unsigned32
_F3ErpUnitRapsPDUsRx_Object=MibTableColumn
f3ErpUnitRapsPDUsRx=_F3ErpUnitRapsPDUsRx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,3),_F3ErpUnitRapsPDUsRx_Type())
f3ErpUnitRapsPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsPDUsRx.setStatus(_A)
_F3ErpUnitRapsPDUsDiscarded_Type=Unsigned32
_F3ErpUnitRapsPDUsDiscarded_Object=MibTableColumn
f3ErpUnitRapsPDUsDiscarded=_F3ErpUnitRapsPDUsDiscarded_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,4),_F3ErpUnitRapsPDUsDiscarded_Type())
f3ErpUnitRapsPDUsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsPDUsDiscarded.setStatus(_A)
_F3ErpUnitRapsNoReqPDUsTx_Type=Unsigned32
_F3ErpUnitRapsNoReqPDUsTx_Object=MibTableColumn
f3ErpUnitRapsNoReqPDUsTx=_F3ErpUnitRapsNoReqPDUsTx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,5),_F3ErpUnitRapsNoReqPDUsTx_Type())
f3ErpUnitRapsNoReqPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsNoReqPDUsTx.setStatus(_A)
_F3ErpUnitRapsNoReqRBPDUsTx_Type=Unsigned32
_F3ErpUnitRapsNoReqRBPDUsTx_Object=MibTableColumn
f3ErpUnitRapsNoReqRBPDUsTx=_F3ErpUnitRapsNoReqRBPDUsTx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,6),_F3ErpUnitRapsNoReqRBPDUsTx_Type())
f3ErpUnitRapsNoReqRBPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsNoReqRBPDUsTx.setStatus(_A)
_F3ErpUnitRapsSignalFailPDUsTx_Type=Unsigned32
_F3ErpUnitRapsSignalFailPDUsTx_Object=MibTableColumn
f3ErpUnitRapsSignalFailPDUsTx=_F3ErpUnitRapsSignalFailPDUsTx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,7),_F3ErpUnitRapsSignalFailPDUsTx_Type())
f3ErpUnitRapsSignalFailPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsSignalFailPDUsTx.setStatus(_A)
_F3ErpUnitRapsManualSwitchPDUsTx_Type=Unsigned32
_F3ErpUnitRapsManualSwitchPDUsTx_Object=MibTableColumn
f3ErpUnitRapsManualSwitchPDUsTx=_F3ErpUnitRapsManualSwitchPDUsTx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,8),_F3ErpUnitRapsManualSwitchPDUsTx_Type())
f3ErpUnitRapsManualSwitchPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsManualSwitchPDUsTx.setStatus(_A)
_F3ErpUnitRapsForcedSwitchPDUsTx_Type=Unsigned32
_F3ErpUnitRapsForcedSwitchPDUsTx_Object=MibTableColumn
f3ErpUnitRapsForcedSwitchPDUsTx=_F3ErpUnitRapsForcedSwitchPDUsTx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,9),_F3ErpUnitRapsForcedSwitchPDUsTx_Type())
f3ErpUnitRapsForcedSwitchPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsForcedSwitchPDUsTx.setStatus(_A)
_F3ErpUnitRapsEventPDUsTx_Type=Unsigned32
_F3ErpUnitRapsEventPDUsTx_Object=MibTableColumn
f3ErpUnitRapsEventPDUsTx=_F3ErpUnitRapsEventPDUsTx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,10),_F3ErpUnitRapsEventPDUsTx_Type())
f3ErpUnitRapsEventPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsEventPDUsTx.setStatus(_A)
_F3ErpUnitRapsNoReqPDUsRx_Type=Unsigned32
_F3ErpUnitRapsNoReqPDUsRx_Object=MibTableColumn
f3ErpUnitRapsNoReqPDUsRx=_F3ErpUnitRapsNoReqPDUsRx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,11),_F3ErpUnitRapsNoReqPDUsRx_Type())
f3ErpUnitRapsNoReqPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsNoReqPDUsRx.setStatus(_A)
_F3ErpUnitRapsNoReqRBPDUsRx_Type=Unsigned32
_F3ErpUnitRapsNoReqRBPDUsRx_Object=MibTableColumn
f3ErpUnitRapsNoReqRBPDUsRx=_F3ErpUnitRapsNoReqRBPDUsRx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,12),_F3ErpUnitRapsNoReqRBPDUsRx_Type())
f3ErpUnitRapsNoReqRBPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsNoReqRBPDUsRx.setStatus(_A)
_F3ErpUnitRapsSignalFailPDUsRx_Type=Unsigned32
_F3ErpUnitRapsSignalFailPDUsRx_Object=MibTableColumn
f3ErpUnitRapsSignalFailPDUsRx=_F3ErpUnitRapsSignalFailPDUsRx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,13),_F3ErpUnitRapsSignalFailPDUsRx_Type())
f3ErpUnitRapsSignalFailPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsSignalFailPDUsRx.setStatus(_A)
_F3ErpUnitRapsManualSwitchPDUsRx_Type=Unsigned32
_F3ErpUnitRapsManualSwitchPDUsRx_Object=MibTableColumn
f3ErpUnitRapsManualSwitchPDUsRx=_F3ErpUnitRapsManualSwitchPDUsRx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,14),_F3ErpUnitRapsManualSwitchPDUsRx_Type())
f3ErpUnitRapsManualSwitchPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsManualSwitchPDUsRx.setStatus(_A)
_F3ErpUnitRapsForcedSwitchPDUsRx_Type=Unsigned32
_F3ErpUnitRapsForcedSwitchPDUsRx_Object=MibTableColumn
f3ErpUnitRapsForcedSwitchPDUsRx=_F3ErpUnitRapsForcedSwitchPDUsRx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,15),_F3ErpUnitRapsForcedSwitchPDUsRx_Type())
f3ErpUnitRapsForcedSwitchPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsForcedSwitchPDUsRx.setStatus(_A)
_F3ErpUnitRapsEventPDUsRx_Type=Unsigned32
_F3ErpUnitRapsEventPDUsRx_Object=MibTableColumn
f3ErpUnitRapsEventPDUsRx=_F3ErpUnitRapsEventPDUsRx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,16),_F3ErpUnitRapsEventPDUsRx_Type())
f3ErpUnitRapsEventPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsEventPDUsRx.setStatus(_A)
_F3ErpUnitRapsInvalidOamVersionPDUsRx_Type=Unsigned32
_F3ErpUnitRapsInvalidOamVersionPDUsRx_Object=MibTableColumn
f3ErpUnitRapsInvalidOamVersionPDUsRx=_F3ErpUnitRapsInvalidOamVersionPDUsRx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,17),_F3ErpUnitRapsInvalidOamVersionPDUsRx_Type())
f3ErpUnitRapsInvalidOamVersionPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsInvalidOamVersionPDUsRx.setStatus(_A)
_F3ErpUnitRapsRsvdRequestPDUsRx_Type=Unsigned32
_F3ErpUnitRapsRsvdRequestPDUsRx_Object=MibTableColumn
f3ErpUnitRapsRsvdRequestPDUsRx=_F3ErpUnitRapsRsvdRequestPDUsRx_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,18),_F3ErpUnitRapsRsvdRequestPDUsRx_Type())
f3ErpUnitRapsRsvdRequestPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsRsvdRequestPDUsRx.setStatus(_A)
_F3ErpUnitRapsRsvdEventSubcode_Type=Unsigned32
_F3ErpUnitRapsRsvdEventSubcode_Object=MibTableColumn
f3ErpUnitRapsRsvdEventSubcode=_F3ErpUnitRapsRsvdEventSubcode_Object((1,3,6,1,4,1,2544,1,12,25,2,1,1,19),_F3ErpUnitRapsRsvdEventSubcode_Type())
f3ErpUnitRapsRsvdEventSubcode.setMaxAccess(_C)
if mibBuilder.loadTexts:f3ErpUnitRapsRsvdEventSubcode.setStatus(_A)
_F3ErpConformance_ObjectIdentity=ObjectIdentity
f3ErpConformance=_F3ErpConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,25,3))
_F3ErpCompliances_ObjectIdentity=ObjectIdentity
f3ErpCompliances=_F3ErpCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,25,3,1))
_F3ErpGroups_ObjectIdentity=ObjectIdentity
f3ErpGroups=_F3ErpGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,25,3,2))
f3ErpGroupGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,25,3,2,1))
f3ErpGroupGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_J),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:f3ErpGroupGroup.setStatus(_A)
f3ErpUnitGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,25,3,2,2))
f3ErpUnitGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:f3ErpUnitGroup.setStatus(_A)
f3ErpUnitStatsGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,25,3,2,3))
f3ErpUnitStatsGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:f3ErpUnitStatsGroup.setStatus(_A)
f3ErpCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,25,3,1,1))
f3ErpCompliance.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:f3ErpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'G8032Version':G8032Version,'RPLRole':RPLRole,'RingPortStatus':RingPortStatus,'RingNodeState':RingNodeState,'RAPSRequest':RAPSRequest,'ERPGroupAction':ERPGroupAction,'RapsInterconnectionNode':RapsInterconnectionNode,'RapsMultipleFailure':RapsMultipleFailure,'f3ErpMIB':f3ErpMIB,'f3ErpConfigObjects':f3ErpConfigObjects,'f3ErpGroupTable':f3ErpGroupTable,'f3ErpGroupEntry':f3ErpGroupEntry,_I:f3ErpGroupIndex,_R:f3ErpGroupAdminState,_S:f3ErpGroupOperationalState,_T:f3ErpGroupSecondaryState,_U:f3ErpGroupRapsRingId,_V:f3ErpGroupRapsNodeId,_W:f3ErpGroupRapsVlanId,_X:f3ErpGroupRapsVlanPrio,_Y:f3ErpGroupRapsVlanEtherType,_Z:f3ErpGroupRapsMdLevel,_a:f3ErpGroupCompatibleVersion,_b:f3ErpGroupRevertive,_c:f3ErpGroupSubRingWithoutVirtChan,_d:f3ErpGroupGuardTime,_e:f3ErpGroupWaitToRestore,_f:f3ErpGroupHoldOffTime,_g:f3ErpGroupRingPort0,_h:f3ErpGroupRingPort0MEP,_i:f3ErpGroupRingPort0Role,_j:f3ErpGroupRingPort1,_k:f3ErpGroupRingPort1MEP,_l:f3ErpGroupRingPort1Role,_m:f3ErpGroupProtectMgmtTunnel,_n:f3ErpGroupNodeState,_o:f3ErpGroupWTRRemainingTime,_p:f3ErpGroupTxRapsRequest,_q:f3ErpGroupTxRapsRplBlocked,_r:f3ErpGroupTxRapsDNF,_s:f3ErpGroupTxRapsBPR,_t:f3ErpGroupAction,_u:f3ErpGroupActionObject,_v:f3ErpGroupUserLabel,_w:f3ErpGroupStorageType,_x:f3ErpGroupRowStatus,_y:f3ErpGroupInterconnectionErp,_z:f3ErpGroupInterconnectPropagateTc,_A0:f3ErpGroupRapsVirtualChannelMep,_A1:f3ErpGroupMaxFpNum,_A2:f3ErpGroupRapsInterconnectionNode,_A3:f3ErpGroupRapsMultipleFailure,'f3ErpGroupProtectedFlowTable':f3ErpGroupProtectedFlowTable,'f3ErpGroupProtectedFlowEntry':f3ErpGroupProtectedFlowEntry,_J:f3ErpGroupProtectedFlow,'f3ErpUnitTable':f3ErpUnitTable,'f3ErpUnitEntry':f3ErpUnitEntry,_K:f3ErpUnitIndex,_A4:f3ErpUnitPort,_A5:f3ErpUnitPortMEP,_A6:f3ErpUnitPortRole,_A7:f3ErpUnitPortStatus,_A8:f3ErpUnitPortRxRapsRequest,_A9:f3ErpUnitPortRxRapsRplBlocked,_AA:f3ErpUnitPortRxRapsDNF,_AB:f3ErpUnitPortRxRapsBPR,_AC:f3ErpUnitPortRxRapsNodeId,_AD:f3ErpUnitPortRapsFp,'f3ErpStatsObjects':f3ErpStatsObjects,'f3ErpUnitStatsTable':f3ErpUnitStatsTable,'f3ErpUnitStatsEntry':f3ErpUnitStatsEntry,_AE:f3ErpUnitNumBlockedStateTrans,_AF:f3ErpUnitRapsPDUsTx,_AG:f3ErpUnitRapsPDUsRx,_AH:f3ErpUnitRapsPDUsDiscarded,_AI:f3ErpUnitRapsNoReqPDUsTx,_AJ:f3ErpUnitRapsNoReqRBPDUsTx,_AK:f3ErpUnitRapsSignalFailPDUsTx,_AL:f3ErpUnitRapsManualSwitchPDUsTx,_AM:f3ErpUnitRapsForcedSwitchPDUsTx,_AN:f3ErpUnitRapsEventPDUsTx,_AO:f3ErpUnitRapsNoReqPDUsRx,_AP:f3ErpUnitRapsNoReqRBPDUsRx,_AQ:f3ErpUnitRapsSignalFailPDUsRx,_AR:f3ErpUnitRapsManualSwitchPDUsRx,_AS:f3ErpUnitRapsForcedSwitchPDUsRx,_AT:f3ErpUnitRapsEventPDUsRx,_AU:f3ErpUnitRapsInvalidOamVersionPDUsRx,_AV:f3ErpUnitRapsRsvdRequestPDUsRx,_AW:f3ErpUnitRapsRsvdEventSubcode,'f3ErpConformance':f3ErpConformance,'f3ErpCompliances':f3ErpCompliances,'f3ErpCompliance':f3ErpCompliance,'f3ErpGroups':f3ErpGroups,_AX:f3ErpGroupGroup,_AY:f3ErpUnitGroup,_AZ:f3ErpUnitStatsGroup})