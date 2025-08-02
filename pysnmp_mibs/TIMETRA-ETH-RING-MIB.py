_AF='tmnxEthRingCommandV9v0Group'
_AE='tmnxEthRingSubRingV9v0Group'
_AD='tmnxEthRingBaseConfigV9v0Group'
_AC='tmnxEthRingApsPrvsnClearAlarm'
_AB='tmnxEthRingApsPrvsnRaiseAlarm'
_AA='tmnxEthRingPathFwdStateChange'
_A9='tmnxEthRingCommandSwitch'
_A8='tmnxEthRingSubRingPropTopChange'
_A7='tmnxEthRingSubRingInterconnectId'
_A6='tmnxEthRingSubRingType'
_A5='tmnxEthRingCompatibleVersion'
_A4='tmnxEthRingSAPPathControlFlag'
_A3='tmnxEthRingSAPPathIndex'
_A2='tmnxEthRingPathFwdStateChgTime'
_A1='tmnxEthRingPathType'
_A0='tmnxEthRingPathOperStatus'
_z='tmnxEthRingPathAdminStatus'
_y='tmnxEthRingPathDescription'
_x='tmnxEthRingPathIfRapsCcTag'
_w='tmnxEthRingPathIfIndex'
_v='tmnxEthRingPathRowStatus'
_u='tmnxEthRingNodeId'
_t='tmnxEthRingRplNode'
_s='tmnxEthRingRevertTimeCountDn'
_r='tmnxEthRingRevertTime'
_q='tmnxEthRingCcmHoldUpTime'
_p='tmnxEthRingCcmHoldDownTime'
_o='tmnxEthRingGuardTime'
_n='tmnxEthRingOperState'
_m='tmnxEthRingAdminState'
_l='tmnxEthRingDescription'
_k='tmnxEthRingRowStatus'
_j='tmnxEthRingSAPPathTblChanged'
_i='tmnxEthRingPathTimeStamp'
_h='tmnxEthRingPathTblLastChanged'
_g='tmnxEthRingTimeStamp'
_f='tmnxEthRingCfgTblLastChanged'
_e='tmnxEthRingCommandEntry'
_d='tmnxEthRingPathIndex'
_c='TmnxEthRingRplNodeType'
_b='seconds'
_a='deciseconds'
_Z='not-accessible'
_Y='TmnxEthRingIndex'
_X='TItemDescription'
_W='TIMETRA-SERV-MIB'
_V='sapPortId'
_U='sapEncapValue'
_T='TruthValue'
_S='tmnxEthRingApsNotifyGroup'
_R='tmnxEthRingOperNotifyGroup'
_Q='tmnxEthRingSAPPathGroup'
_P='tmnxEthRingBasePathGroup'
_O='tmnxEthRingBaseConfigGroup'
_N='tmnxEthRingTimeStampGroup'
_M='tmnxEthRingPathFwdState'
_L='tmnxEthRingIndex'
_K='TmnxAdminState'
_J='TIMETRA-SAP-MIB'
_I='tmnxEthRingPathRxApsPdu'
_H='tmnxEthRingDefectStatus'
_G='tmnxEthRingTxApsPdu'
_F='Integer32'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='current'
_A='TIMETRA-ETH-RING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_T)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
sapEncapValue,sapPortId=mibBuilder.importSymbols(_J,_U,_V)
svcId,=mibBuilder.importSymbols(_W,'svcId')
TItemDescription,TmnxAdminState,TmnxEncapVal,TmnxOperState=mibBuilder.importSymbols('TIMETRA-TC-MIB',_X,_K,'TmnxEncapVal','TmnxOperState')
timetraEthRingMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,72))
if mibBuilder.loadTexts:timetraEthRingMIBModule.setRevisions(('2011-02-01 00:00','2010-01-01 00:00'))
class TmnxEthRingIndex(TextualConvention,Unsigned32):status=_B
class TmnxEthRingPathIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('pathA',0),('pathB',1)))
class TmnxEthRingRplNodeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('rplNone',0),('rplOwner',1),('rplNeighbor',2)))
class TmnxEthRingApsInfoType(TextualConvention,OctetString):status=_B;displayHint='1x-1x [1x:1x:1x:1x:1x:1x] 24x-';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,32))
_TmnxEthRingConformance_ObjectIdentity=ObjectIdentity
tmnxEthRingConformance=_TmnxEthRingConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72))
_TmnxEthRingCompliances_ObjectIdentity=ObjectIdentity
tmnxEthRingCompliances=_TmnxEthRingCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,1))
_TmnxEthRingGroups_ObjectIdentity=ObjectIdentity
tmnxEthRingGroups=_TmnxEthRingGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,2))
_TmnxEthRingTSGroups_ObjectIdentity=ObjectIdentity
tmnxEthRingTSGroups=_TmnxEthRingTSGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,2,0))
_TmnxEthRingConfigGroups_ObjectIdentity=ObjectIdentity
tmnxEthRingConfigGroups=_TmnxEthRingConfigGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,2,1))
_TmnxEthRingOperGroups_ObjectIdentity=ObjectIdentity
tmnxEthRingOperGroups=_TmnxEthRingOperGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,2,2))
_TmnxEthRingMemberGroups_ObjectIdentity=ObjectIdentity
tmnxEthRingMemberGroups=_TmnxEthRingMemberGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,2,3))
_TmnxEthRingAPSGroups_ObjectIdentity=ObjectIdentity
tmnxEthRingAPSGroups=_TmnxEthRingAPSGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,2,4))
_TmnxEthRingNotifyGroups_ObjectIdentity=ObjectIdentity
tmnxEthRingNotifyGroups=_TmnxEthRingNotifyGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,2,5))
_TmnxEthRingSAPGroups_ObjectIdentity=ObjectIdentity
tmnxEthRingSAPGroups=_TmnxEthRingSAPGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,2,6))
_TmnxEthRingV9v0Groups_ObjectIdentity=ObjectIdentity
tmnxEthRingV9v0Groups=_TmnxEthRingV9v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,72,2,7))
_TmnxEthRingObjs_ObjectIdentity=ObjectIdentity
tmnxEthRingObjs=_TmnxEthRingObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,72))
_TmnxEthRingConfigTimeStamps_ObjectIdentity=ObjectIdentity
tmnxEthRingConfigTimeStamps=_TmnxEthRingConfigTimeStamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,72,0))
_TmnxEthRingCfgTblLastChanged_Type=TimeStamp
_TmnxEthRingCfgTblLastChanged_Object=MibScalar
tmnxEthRingCfgTblLastChanged=_TmnxEthRingCfgTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,72,0,1),_TmnxEthRingCfgTblLastChanged_Type())
tmnxEthRingCfgTblLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingCfgTblLastChanged.setStatus(_B)
_TmnxEthRingPathTblLastChanged_Type=TimeStamp
_TmnxEthRingPathTblLastChanged_Object=MibScalar
tmnxEthRingPathTblLastChanged=_TmnxEthRingPathTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,72,0,2),_TmnxEthRingPathTblLastChanged_Type())
tmnxEthRingPathTblLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingPathTblLastChanged.setStatus(_B)
_TmnxEthRingSAPPathTblChanged_Type=TimeStamp
_TmnxEthRingSAPPathTblChanged_Object=MibScalar
tmnxEthRingSAPPathTblChanged=_TmnxEthRingSAPPathTblChanged_Object((1,3,6,1,4,1,6527,3,1,2,72,0,4),_TmnxEthRingSAPPathTblChanged_Type())
tmnxEthRingSAPPathTblChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingSAPPathTblChanged.setStatus(_B)
_TmnxEthRingConfigurations_ObjectIdentity=ObjectIdentity
tmnxEthRingConfigurations=_TmnxEthRingConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,72,1))
_TmnxEthRingConfigTable_Object=MibTable
tmnxEthRingConfigTable=_TmnxEthRingConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1))
if mibBuilder.loadTexts:tmnxEthRingConfigTable.setStatus(_B)
_TmnxEthRingConfigEntry_Object=MibTableRow
tmnxEthRingConfigEntry=_TmnxEthRingConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1))
tmnxEthRingConfigEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:tmnxEthRingConfigEntry.setStatus(_B)
class _TmnxEthRingIndex_Type(TmnxEthRingIndex):subtypeSpec=TmnxEthRingIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967294))
_TmnxEthRingIndex_Type.__name__=_Y
_TmnxEthRingIndex_Object=MibTableColumn
tmnxEthRingIndex=_TmnxEthRingIndex_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,1),_TmnxEthRingIndex_Type())
tmnxEthRingIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:tmnxEthRingIndex.setStatus(_B)
_TmnxEthRingRowStatus_Type=RowStatus
_TmnxEthRingRowStatus_Object=MibTableColumn
tmnxEthRingRowStatus=_TmnxEthRingRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,2),_TmnxEthRingRowStatus_Type())
tmnxEthRingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingRowStatus.setStatus(_B)
_TmnxEthRingTimeStamp_Type=TimeStamp
_TmnxEthRingTimeStamp_Object=MibTableColumn
tmnxEthRingTimeStamp=_TmnxEthRingTimeStamp_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,3),_TmnxEthRingTimeStamp_Type())
tmnxEthRingTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingTimeStamp.setStatus(_B)
class _TmnxEthRingDescription_Type(TItemDescription):defaultValue=OctetString('')
_TmnxEthRingDescription_Type.__name__=_X
_TmnxEthRingDescription_Object=MibTableColumn
tmnxEthRingDescription=_TmnxEthRingDescription_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,4),_TmnxEthRingDescription_Type())
tmnxEthRingDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingDescription.setStatus(_B)
class _TmnxEthRingAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxEthRingAdminState_Type.__name__=_K
_TmnxEthRingAdminState_Object=MibTableColumn
tmnxEthRingAdminState=_TmnxEthRingAdminState_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,5),_TmnxEthRingAdminState_Type())
tmnxEthRingAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingAdminState.setStatus(_B)
_TmnxEthRingOperState_Type=TmnxOperState
_TmnxEthRingOperState_Object=MibTableColumn
tmnxEthRingOperState=_TmnxEthRingOperState_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,6),_TmnxEthRingOperState_Type())
tmnxEthRingOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingOperState.setStatus(_B)
class _TmnxEthRingGuardTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_TmnxEthRingGuardTime_Type.__name__=_E
_TmnxEthRingGuardTime_Object=MibTableColumn
tmnxEthRingGuardTime=_TmnxEthRingGuardTime_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,7),_TmnxEthRingGuardTime_Type())
tmnxEthRingGuardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingGuardTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthRingGuardTime.setUnits(_a)
class _TmnxEthRingRevertTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,720))
_TmnxEthRingRevertTime_Type.__name__=_E
_TmnxEthRingRevertTime_Object=MibTableColumn
tmnxEthRingRevertTime=_TmnxEthRingRevertTime_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,8),_TmnxEthRingRevertTime_Type())
tmnxEthRingRevertTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingRevertTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthRingRevertTime.setUnits(_b)
class _TmnxEthRingRevertTimeCountDn_Type(Unsigned32):defaultValue=0
_TmnxEthRingRevertTimeCountDn_Type.__name__=_E
_TmnxEthRingRevertTimeCountDn_Object=MibTableColumn
tmnxEthRingRevertTimeCountDn=_TmnxEthRingRevertTimeCountDn_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,9),_TmnxEthRingRevertTimeCountDn_Type())
tmnxEthRingRevertTimeCountDn.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingRevertTimeCountDn.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthRingRevertTimeCountDn.setUnits(_b)
class _TmnxEthRingCcmHoldDownTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_TmnxEthRingCcmHoldDownTime_Type.__name__=_E
_TmnxEthRingCcmHoldDownTime_Object=MibTableColumn
tmnxEthRingCcmHoldDownTime=_TmnxEthRingCcmHoldDownTime_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,10),_TmnxEthRingCcmHoldDownTime_Type())
tmnxEthRingCcmHoldDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingCcmHoldDownTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthRingCcmHoldDownTime.setUnits('centiseconds')
class _TmnxEthRingCcmHoldUpTime_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_TmnxEthRingCcmHoldUpTime_Type.__name__=_E
_TmnxEthRingCcmHoldUpTime_Object=MibTableColumn
tmnxEthRingCcmHoldUpTime=_TmnxEthRingCcmHoldUpTime_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,11),_TmnxEthRingCcmHoldUpTime_Type())
tmnxEthRingCcmHoldUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingCcmHoldUpTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthRingCcmHoldUpTime.setUnits(_a)
class _TmnxEthRingRplNode_Type(TmnxEthRingRplNodeType):defaultValue=0
_TmnxEthRingRplNode_Type.__name__=_c
_TmnxEthRingRplNode_Object=MibTableColumn
tmnxEthRingRplNode=_TmnxEthRingRplNode_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,12),_TmnxEthRingRplNode_Type())
tmnxEthRingRplNode.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingRplNode.setStatus(_B)
_TmnxEthRingNodeId_Type=MacAddress
_TmnxEthRingNodeId_Object=MibTableColumn
tmnxEthRingNodeId=_TmnxEthRingNodeId_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,13),_TmnxEthRingNodeId_Type())
tmnxEthRingNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingNodeId.setStatus(_B)
_TmnxEthRingTxApsPdu_Type=TmnxEthRingApsInfoType
_TmnxEthRingTxApsPdu_Object=MibTableColumn
tmnxEthRingTxApsPdu=_TmnxEthRingTxApsPdu_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,14),_TmnxEthRingTxApsPdu_Type())
tmnxEthRingTxApsPdu.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingTxApsPdu.setStatus(_B)
class _TmnxEthRingDefectStatus_Type(Bits):namedValues=NamedValues(('dFopPM',0))
_TmnxEthRingDefectStatus_Type.__name__='Bits'
_TmnxEthRingDefectStatus_Object=MibTableColumn
tmnxEthRingDefectStatus=_TmnxEthRingDefectStatus_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,15),_TmnxEthRingDefectStatus_Type())
tmnxEthRingDefectStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingDefectStatus.setStatus(_B)
class _TmnxEthRingSubRingType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('virtualLink',1),('nonVirtualLink',2)))
_TmnxEthRingSubRingType_Type.__name__=_F
_TmnxEthRingSubRingType_Object=MibTableColumn
tmnxEthRingSubRingType=_TmnxEthRingSubRingType_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,16),_TmnxEthRingSubRingType_Type())
tmnxEthRingSubRingType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingSubRingType.setStatus(_B)
class _TmnxEthRingSubRingInterconnectId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967294),ValueRangeConstraint(4294967295,4294967295))
_TmnxEthRingSubRingInterconnectId_Type.__name__=_E
_TmnxEthRingSubRingInterconnectId_Object=MibTableColumn
tmnxEthRingSubRingInterconnectId=_TmnxEthRingSubRingInterconnectId_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,17),_TmnxEthRingSubRingInterconnectId_Type())
tmnxEthRingSubRingInterconnectId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingSubRingInterconnectId.setStatus(_B)
class _TmnxEthRingSubRingPropTopChange_Type(TruthValue):defaultValue=2
_TmnxEthRingSubRingPropTopChange_Type.__name__=_T
_TmnxEthRingSubRingPropTopChange_Object=MibTableColumn
tmnxEthRingSubRingPropTopChange=_TmnxEthRingSubRingPropTopChange_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,18),_TmnxEthRingSubRingPropTopChange_Type())
tmnxEthRingSubRingPropTopChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingSubRingPropTopChange.setStatus(_B)
class _TmnxEthRingCompatibleVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version1',1),('version2',2)))
_TmnxEthRingCompatibleVersion_Type.__name__=_F
_TmnxEthRingCompatibleVersion_Object=MibTableColumn
tmnxEthRingCompatibleVersion=_TmnxEthRingCompatibleVersion_Object((1,3,6,1,4,1,6527,3,1,2,72,1,1,1,19),_TmnxEthRingCompatibleVersion_Type())
tmnxEthRingCompatibleVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingCompatibleVersion.setStatus(_B)
_TmnxEthRingPathTable_Object=MibTable
tmnxEthRingPathTable=_TmnxEthRingPathTable_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3))
if mibBuilder.loadTexts:tmnxEthRingPathTable.setStatus(_B)
_TmnxEthRingPathEntry_Object=MibTableRow
tmnxEthRingPathEntry=_TmnxEthRingPathEntry_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1))
tmnxEthRingPathEntry.setIndexNames((0,_A,_L),(0,_A,_d))
if mibBuilder.loadTexts:tmnxEthRingPathEntry.setStatus(_B)
_TmnxEthRingPathIndex_Type=TmnxEthRingPathIndex
_TmnxEthRingPathIndex_Object=MibTableColumn
tmnxEthRingPathIndex=_TmnxEthRingPathIndex_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,1),_TmnxEthRingPathIndex_Type())
tmnxEthRingPathIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:tmnxEthRingPathIndex.setStatus(_B)
_TmnxEthRingPathRowStatus_Type=RowStatus
_TmnxEthRingPathRowStatus_Object=MibTableColumn
tmnxEthRingPathRowStatus=_TmnxEthRingPathRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,2),_TmnxEthRingPathRowStatus_Type())
tmnxEthRingPathRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingPathRowStatus.setStatus(_B)
_TmnxEthRingPathTimeStamp_Type=TimeStamp
_TmnxEthRingPathTimeStamp_Object=MibTableColumn
tmnxEthRingPathTimeStamp=_TmnxEthRingPathTimeStamp_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,3),_TmnxEthRingPathTimeStamp_Type())
tmnxEthRingPathTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingPathTimeStamp.setStatus(_B)
_TmnxEthRingPathIfIndex_Type=InterfaceIndexOrZero
_TmnxEthRingPathIfIndex_Object=MibTableColumn
tmnxEthRingPathIfIndex=_TmnxEthRingPathIfIndex_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,4),_TmnxEthRingPathIfIndex_Type())
tmnxEthRingPathIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingPathIfIndex.setStatus(_B)
_TmnxEthRingPathIfRapsCcTag_Type=TmnxEncapVal
_TmnxEthRingPathIfRapsCcTag_Object=MibTableColumn
tmnxEthRingPathIfRapsCcTag=_TmnxEthRingPathIfRapsCcTag_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,5),_TmnxEthRingPathIfRapsCcTag_Type())
tmnxEthRingPathIfRapsCcTag.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingPathIfRapsCcTag.setStatus(_B)
_TmnxEthRingPathDescription_Type=TItemDescription
_TmnxEthRingPathDescription_Object=MibTableColumn
tmnxEthRingPathDescription=_TmnxEthRingPathDescription_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,6),_TmnxEthRingPathDescription_Type())
tmnxEthRingPathDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingPathDescription.setStatus(_B)
class _TmnxEthRingPathAdminStatus_Type(TmnxAdminState):defaultValue=3
_TmnxEthRingPathAdminStatus_Type.__name__=_K
_TmnxEthRingPathAdminStatus_Object=MibTableColumn
tmnxEthRingPathAdminStatus=_TmnxEthRingPathAdminStatus_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,7),_TmnxEthRingPathAdminStatus_Type())
tmnxEthRingPathAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingPathAdminStatus.setStatus(_B)
_TmnxEthRingPathOperStatus_Type=TmnxOperState
_TmnxEthRingPathOperStatus_Object=MibTableColumn
tmnxEthRingPathOperStatus=_TmnxEthRingPathOperStatus_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,8),_TmnxEthRingPathOperStatus_Type())
tmnxEthRingPathOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingPathOperStatus.setStatus(_B)
class _TmnxEthRingPathType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('rplEnd',1)))
_TmnxEthRingPathType_Type.__name__=_F
_TmnxEthRingPathType_Object=MibTableColumn
tmnxEthRingPathType=_TmnxEthRingPathType_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,9),_TmnxEthRingPathType_Type())
tmnxEthRingPathType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingPathType.setStatus(_B)
class _TmnxEthRingPathFwdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unblocked',0),('blocked',1)))
_TmnxEthRingPathFwdState_Type.__name__=_F
_TmnxEthRingPathFwdState_Object=MibTableColumn
tmnxEthRingPathFwdState=_TmnxEthRingPathFwdState_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,10),_TmnxEthRingPathFwdState_Type())
tmnxEthRingPathFwdState.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingPathFwdState.setStatus(_B)
_TmnxEthRingPathFwdStateChgTime_Type=TimeStamp
_TmnxEthRingPathFwdStateChgTime_Object=MibTableColumn
tmnxEthRingPathFwdStateChgTime=_TmnxEthRingPathFwdStateChgTime_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,11),_TmnxEthRingPathFwdStateChgTime_Type())
tmnxEthRingPathFwdStateChgTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingPathFwdStateChgTime.setStatus(_B)
_TmnxEthRingPathRxApsPdu_Type=TmnxEthRingApsInfoType
_TmnxEthRingPathRxApsPdu_Object=MibTableColumn
tmnxEthRingPathRxApsPdu=_TmnxEthRingPathRxApsPdu_Object((1,3,6,1,4,1,6527,3,1,2,72,1,3,1,12),_TmnxEthRingPathRxApsPdu_Type())
tmnxEthRingPathRxApsPdu.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingPathRxApsPdu.setStatus(_B)
_TmnxEthRingSAPConfigs_ObjectIdentity=ObjectIdentity
tmnxEthRingSAPConfigs=_TmnxEthRingSAPConfigs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,72,1,4))
_TmnxEthRingSAPPathTable_Object=MibTable
tmnxEthRingSAPPathTable=_TmnxEthRingSAPPathTable_Object((1,3,6,1,4,1,6527,3,1,2,72,1,4,1))
if mibBuilder.loadTexts:tmnxEthRingSAPPathTable.setStatus(_B)
_TmnxEthRingSAPPathEntry_Object=MibTableRow
tmnxEthRingSAPPathEntry=_TmnxEthRingSAPPathEntry_Object((1,3,6,1,4,1,6527,3,1,2,72,1,4,1,1))
tmnxEthRingSAPPathEntry.setIndexNames((0,_W,'svcId'),(0,_J,_V),(0,_J,_U))
if mibBuilder.loadTexts:tmnxEthRingSAPPathEntry.setStatus(_B)
_TmnxEthRingSAPPathIndex_Type=Unsigned32
_TmnxEthRingSAPPathIndex_Object=MibTableColumn
tmnxEthRingSAPPathIndex=_TmnxEthRingSAPPathIndex_Object((1,3,6,1,4,1,6527,3,1,2,72,1,4,1,1,1),_TmnxEthRingSAPPathIndex_Type())
tmnxEthRingSAPPathIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingSAPPathIndex.setStatus(_B)
_TmnxEthRingSAPPathControlFlag_Type=TruthValue
_TmnxEthRingSAPPathControlFlag_Object=MibTableColumn
tmnxEthRingSAPPathControlFlag=_TmnxEthRingSAPPathControlFlag_Object((1,3,6,1,4,1,6527,3,1,2,72,1,4,1,1,2),_TmnxEthRingSAPPathControlFlag_Type())
tmnxEthRingSAPPathControlFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthRingSAPPathControlFlag.setStatus(_B)
_TmnxEthRingCommandTable_Object=MibTable
tmnxEthRingCommandTable=_TmnxEthRingCommandTable_Object((1,3,6,1,4,1,6527,3,1,2,72,1,5))
if mibBuilder.loadTexts:tmnxEthRingCommandTable.setStatus(_B)
_TmnxEthRingCommandEntry_Object=MibTableRow
tmnxEthRingCommandEntry=_TmnxEthRingCommandEntry_Object((1,3,6,1,4,1,6527,3,1,2,72,1,5,1))
if mibBuilder.loadTexts:tmnxEthRingCommandEntry.setStatus(_B)
class _TmnxEthRingCommandSwitch_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noCmd',0),('clear',1),('forceSwitch',2),('manualSwitch',3)))
_TmnxEthRingCommandSwitch_Type.__name__=_F
_TmnxEthRingCommandSwitch_Object=MibTableColumn
tmnxEthRingCommandSwitch=_TmnxEthRingCommandSwitch_Object((1,3,6,1,4,1,6527,3,1,2,72,1,5,1,1),_TmnxEthRingCommandSwitch_Type())
tmnxEthRingCommandSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthRingCommandSwitch.setStatus(_B)
_TmnxEthRingStatistics_ObjectIdentity=ObjectIdentity
tmnxEthRingStatistics=_TmnxEthRingStatistics_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,72,2))
_TmnxEthRingNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxEthRingNotifyPrefix=_TmnxEthRingNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,72))
_TmnxEthRingNotifications_ObjectIdentity=ObjectIdentity
tmnxEthRingNotifications=_TmnxEthRingNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,72,0))
_TmnxEthRingOprNotifications_ObjectIdentity=ObjectIdentity
tmnxEthRingOprNotifications=_TmnxEthRingOprNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,72,0,1))
_TmnxEthRingApsNotifications_ObjectIdentity=ObjectIdentity
tmnxEthRingApsNotifications=_TmnxEthRingApsNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,72,0,2))
tmnxEthRingPathEntry.registerAugmentions((_A,_e))
tmnxEthRingCommandEntry.setIndexNames(*tmnxEthRingPathEntry.getIndexNames())
tmnxEthRingTimeStampGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,72,2,0,1))
tmnxEthRingTimeStampGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:tmnxEthRingTimeStampGroup.setStatus(_B)
tmnxEthRingBaseConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,72,2,1,1))
tmnxEthRingBaseConfigGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:tmnxEthRingBaseConfigGroup.setStatus(_B)
tmnxEthRingBasePathGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,72,2,3,1))
tmnxEthRingBasePathGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_M),(_A,_A2),(_A,_I)))
if mibBuilder.loadTexts:tmnxEthRingBasePathGroup.setStatus(_B)
tmnxEthRingSAPPathGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,72,2,6,1))
tmnxEthRingSAPPathGroup.setObjects(*((_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:tmnxEthRingSAPPathGroup.setStatus(_B)
tmnxEthRingBaseConfigV9v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,72,2,7,1))
tmnxEthRingBaseConfigV9v0Group.setObjects((_A,_A5))
if mibBuilder.loadTexts:tmnxEthRingBaseConfigV9v0Group.setStatus(_B)
tmnxEthRingSubRingV9v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,72,2,7,2))
tmnxEthRingSubRingV9v0Group.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:tmnxEthRingSubRingV9v0Group.setStatus(_B)
tmnxEthRingCommandV9v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,72,2,7,3))
tmnxEthRingCommandV9v0Group.setObjects((_A,_A9))
if mibBuilder.loadTexts:tmnxEthRingCommandV9v0Group.setStatus(_B)
tmnxEthRingPathFwdStateChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,72,0,1,1))
tmnxEthRingPathFwdStateChange.setObjects((_A,_M))
if mibBuilder.loadTexts:tmnxEthRingPathFwdStateChange.setStatus(_B)
tmnxEthRingApsPrvsnRaiseAlarm=NotificationType((1,3,6,1,4,1,6527,3,1,3,72,0,2,1))
tmnxEthRingApsPrvsnRaiseAlarm.setObjects(*((_A,_G),(_A,_I),(_A,_H)))
if mibBuilder.loadTexts:tmnxEthRingApsPrvsnRaiseAlarm.setStatus(_B)
tmnxEthRingApsPrvsnClearAlarm=NotificationType((1,3,6,1,4,1,6527,3,1,3,72,0,2,2))
tmnxEthRingApsPrvsnClearAlarm.setObjects(*((_A,_G),(_A,_I),(_A,_H)))
if mibBuilder.loadTexts:tmnxEthRingApsPrvsnClearAlarm.setStatus(_B)
tmnxEthRingOperNotifyGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,72,2,5,1))
tmnxEthRingOperNotifyGroup.setObjects((_A,_AA))
if mibBuilder.loadTexts:tmnxEthRingOperNotifyGroup.setStatus(_B)
tmnxEthRingApsNotifyGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,72,2,5,2))
tmnxEthRingApsNotifyGroup.setObjects(*((_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:tmnxEthRingApsNotifyGroup.setStatus(_B)
tmnxEthRingCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,72,1,1))
tmnxEthRingCompliance.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:tmnxEthRingCompliance.setStatus('obsolete')
tmnxEthRingV9v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,72,1,2))
tmnxEthRingV9v0Compliance.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:tmnxEthRingV9v0Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_Y:TmnxEthRingIndex,'TmnxEthRingPathIndex':TmnxEthRingPathIndex,_c:TmnxEthRingRplNodeType,'TmnxEthRingApsInfoType':TmnxEthRingApsInfoType,'timetraEthRingMIBModule':timetraEthRingMIBModule,'tmnxEthRingConformance':tmnxEthRingConformance,'tmnxEthRingCompliances':tmnxEthRingCompliances,'tmnxEthRingCompliance':tmnxEthRingCompliance,'tmnxEthRingV9v0Compliance':tmnxEthRingV9v0Compliance,'tmnxEthRingGroups':tmnxEthRingGroups,'tmnxEthRingTSGroups':tmnxEthRingTSGroups,_N:tmnxEthRingTimeStampGroup,'tmnxEthRingConfigGroups':tmnxEthRingConfigGroups,_O:tmnxEthRingBaseConfigGroup,'tmnxEthRingOperGroups':tmnxEthRingOperGroups,'tmnxEthRingMemberGroups':tmnxEthRingMemberGroups,_P:tmnxEthRingBasePathGroup,'tmnxEthRingAPSGroups':tmnxEthRingAPSGroups,'tmnxEthRingNotifyGroups':tmnxEthRingNotifyGroups,_R:tmnxEthRingOperNotifyGroup,_S:tmnxEthRingApsNotifyGroup,'tmnxEthRingSAPGroups':tmnxEthRingSAPGroups,_Q:tmnxEthRingSAPPathGroup,'tmnxEthRingV9v0Groups':tmnxEthRingV9v0Groups,_AD:tmnxEthRingBaseConfigV9v0Group,_AE:tmnxEthRingSubRingV9v0Group,_AF:tmnxEthRingCommandV9v0Group,'tmnxEthRingObjs':tmnxEthRingObjs,'tmnxEthRingConfigTimeStamps':tmnxEthRingConfigTimeStamps,_f:tmnxEthRingCfgTblLastChanged,_h:tmnxEthRingPathTblLastChanged,_j:tmnxEthRingSAPPathTblChanged,'tmnxEthRingConfigurations':tmnxEthRingConfigurations,'tmnxEthRingConfigTable':tmnxEthRingConfigTable,'tmnxEthRingConfigEntry':tmnxEthRingConfigEntry,_L:tmnxEthRingIndex,_k:tmnxEthRingRowStatus,_g:tmnxEthRingTimeStamp,_l:tmnxEthRingDescription,_m:tmnxEthRingAdminState,_n:tmnxEthRingOperState,_o:tmnxEthRingGuardTime,_r:tmnxEthRingRevertTime,_s:tmnxEthRingRevertTimeCountDn,_p:tmnxEthRingCcmHoldDownTime,_q:tmnxEthRingCcmHoldUpTime,_t:tmnxEthRingRplNode,_u:tmnxEthRingNodeId,_G:tmnxEthRingTxApsPdu,_H:tmnxEthRingDefectStatus,_A6:tmnxEthRingSubRingType,_A7:tmnxEthRingSubRingInterconnectId,_A8:tmnxEthRingSubRingPropTopChange,_A5:tmnxEthRingCompatibleVersion,'tmnxEthRingPathTable':tmnxEthRingPathTable,'tmnxEthRingPathEntry':tmnxEthRingPathEntry,_d:tmnxEthRingPathIndex,_v:tmnxEthRingPathRowStatus,_i:tmnxEthRingPathTimeStamp,_w:tmnxEthRingPathIfIndex,_x:tmnxEthRingPathIfRapsCcTag,_y:tmnxEthRingPathDescription,_z:tmnxEthRingPathAdminStatus,_A0:tmnxEthRingPathOperStatus,_A1:tmnxEthRingPathType,_M:tmnxEthRingPathFwdState,_A2:tmnxEthRingPathFwdStateChgTime,_I:tmnxEthRingPathRxApsPdu,'tmnxEthRingSAPConfigs':tmnxEthRingSAPConfigs,'tmnxEthRingSAPPathTable':tmnxEthRingSAPPathTable,'tmnxEthRingSAPPathEntry':tmnxEthRingSAPPathEntry,_A3:tmnxEthRingSAPPathIndex,_A4:tmnxEthRingSAPPathControlFlag,'tmnxEthRingCommandTable':tmnxEthRingCommandTable,_e:tmnxEthRingCommandEntry,_A9:tmnxEthRingCommandSwitch,'tmnxEthRingStatistics':tmnxEthRingStatistics,'tmnxEthRingNotifyPrefix':tmnxEthRingNotifyPrefix,'tmnxEthRingNotifications':tmnxEthRingNotifications,'tmnxEthRingOprNotifications':tmnxEthRingOprNotifications,_AA:tmnxEthRingPathFwdStateChange,'tmnxEthRingApsNotifications':tmnxEthRingApsNotifications,_AB:tmnxEthRingApsPrvsnRaiseAlarm,_AC:tmnxEthRingApsPrvsnClearAlarm})