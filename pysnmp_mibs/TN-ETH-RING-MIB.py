_d='tnEthRingPathFwdState'
_c='tnEthRingCommandEntry'
_b='tnEthRingPathIndex'
_a='manualSwitch'
_Z='TnEthRingRplNodeType'
_Y='seconds'
_X='deciseconds'
_W='not-accessible'
_V='TnEthRingIndex'
_U='TItemDescription'
_T='tnSvcId'
_S='TN-SERV-MIB'
_R='tnSapPortId'
_Q='tnSapEncapValue'
_P='TruthValue'
_O='tnEthRingDefectStatus'
_N='tnEthRingPathRxApsPdu'
_M='tnEthRingTxApsPdu'
_L='tnEthRingIndex'
_K='TmnxAdminState'
_J='TN-SAP-MIB'
_I='OctetString'
_H='tnSysSwitchId'
_G='TROPIC-SYSTEM-MIB'
_F='Unsigned32'
_E='Integer32'
_D='TN-ETH-RING-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_P)
tnSapEncapValue,tnSapPortId=mibBuilder.importSymbols(_J,_Q,_R)
tnSvcId,=mibBuilder.importSymbols(_S,_T)
TItemDescription,TmnxAdminState,TmnxEncapVal,TmnxOperState=mibBuilder.importSymbols('TN-TC-MIB',_U,_K,'TmnxEncapVal','TmnxOperState')
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_G,_H)
tnEthRingMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,72))
if mibBuilder.loadTexts:tnEthRingMIBModule.setRevisions(('2020-06-19 00:00','2020-01-10 00:00','2016-03-15 00:00','2015-01-22 00:00','2013-06-28 00:00','2012-12-05 00:00','2010-01-01 00:00'))
class TnEthRingIndex(TextualConvention,Unsigned32):status=_A
class TnEthRingPathIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('pathA',0),('pathB',1)))
class TnEthRingRplNodeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('rplNone',0),('rplOwner',1),('rplNeighbor',2)))
class TnEthRingApsInfoType(TextualConvention,OctetString):status=_A;displayHint='1x-1x [1x:1x:1x:1x:1x:1x] 24x-';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,32))
_TnEthRingObjs_ObjectIdentity=ObjectIdentity
tnEthRingObjs=_TnEthRingObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,72))
_TnEthRingConfigurations_ObjectIdentity=ObjectIdentity
tnEthRingConfigurations=_TnEthRingConfigurations_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,72,1))
_TnEthRingConfigTable_Object=MibTable
tnEthRingConfigTable=_TnEthRingConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1))
if mibBuilder.loadTexts:tnEthRingConfigTable.setStatus(_A)
_TnEthRingConfigEntry_Object=MibTableRow
tnEthRingConfigEntry=_TnEthRingConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1))
tnEthRingConfigEntry.setIndexNames((0,_G,_H),(0,_D,_L))
if mibBuilder.loadTexts:tnEthRingConfigEntry.setStatus(_A)
class _TnEthRingIndex_Type(TnEthRingIndex):subtypeSpec=TnEthRingIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TnEthRingIndex_Type.__name__=_V
_TnEthRingIndex_Object=MibTableColumn
tnEthRingIndex=_TnEthRingIndex_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,1),_TnEthRingIndex_Type())
tnEthRingIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:tnEthRingIndex.setStatus(_A)
_TnEthRingRowStatus_Type=RowStatus
_TnEthRingRowStatus_Object=MibTableColumn
tnEthRingRowStatus=_TnEthRingRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,2),_TnEthRingRowStatus_Type())
tnEthRingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingRowStatus.setStatus(_A)
_TnEthRingTimeStamp_Type=TimeStamp
_TnEthRingTimeStamp_Object=MibTableColumn
tnEthRingTimeStamp=_TnEthRingTimeStamp_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,3),_TnEthRingTimeStamp_Type())
tnEthRingTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingTimeStamp.setStatus(_A)
class _TnEthRingDescription_Type(TItemDescription):defaultValue=OctetString('')
_TnEthRingDescription_Type.__name__=_U
_TnEthRingDescription_Object=MibTableColumn
tnEthRingDescription=_TnEthRingDescription_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,4),_TnEthRingDescription_Type())
tnEthRingDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingDescription.setStatus(_A)
class _TnEthRingAdminState_Type(TmnxAdminState):defaultValue=3
_TnEthRingAdminState_Type.__name__=_K
_TnEthRingAdminState_Object=MibTableColumn
tnEthRingAdminState=_TnEthRingAdminState_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,5),_TnEthRingAdminState_Type())
tnEthRingAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingAdminState.setStatus(_A)
_TnEthRingOperState_Type=TmnxOperState
_TnEthRingOperState_Object=MibTableColumn
tnEthRingOperState=_TnEthRingOperState_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,6),_TnEthRingOperState_Type())
tnEthRingOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingOperState.setStatus(_A)
class _TnEthRingGuardTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_TnEthRingGuardTime_Type.__name__=_F
_TnEthRingGuardTime_Object=MibTableColumn
tnEthRingGuardTime=_TnEthRingGuardTime_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,7),_TnEthRingGuardTime_Type())
tnEthRingGuardTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingGuardTime.setStatus(_A)
if mibBuilder.loadTexts:tnEthRingGuardTime.setUnits(_X)
class _TnEthRingRevertTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_TnEthRingRevertTime_Type.__name__=_F
_TnEthRingRevertTime_Object=MibTableColumn
tnEthRingRevertTime=_TnEthRingRevertTime_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,8),_TnEthRingRevertTime_Type())
tnEthRingRevertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingRevertTime.setStatus(_A)
if mibBuilder.loadTexts:tnEthRingRevertTime.setUnits(_Y)
class _TnEthRingRevertTimeCountDn_Type(Unsigned32):defaultValue=0
_TnEthRingRevertTimeCountDn_Type.__name__=_F
_TnEthRingRevertTimeCountDn_Object=MibTableColumn
tnEthRingRevertTimeCountDn=_TnEthRingRevertTimeCountDn_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,9),_TnEthRingRevertTimeCountDn_Type())
tnEthRingRevertTimeCountDn.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingRevertTimeCountDn.setStatus(_A)
if mibBuilder.loadTexts:tnEthRingRevertTimeCountDn.setUnits(_Y)
class _TnEthRingCcmHoldDownTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_TnEthRingCcmHoldDownTime_Type.__name__=_F
_TnEthRingCcmHoldDownTime_Object=MibTableColumn
tnEthRingCcmHoldDownTime=_TnEthRingCcmHoldDownTime_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,10),_TnEthRingCcmHoldDownTime_Type())
tnEthRingCcmHoldDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingCcmHoldDownTime.setStatus(_A)
if mibBuilder.loadTexts:tnEthRingCcmHoldDownTime.setUnits('centiseconds')
class _TnEthRingCcmHoldUpTime_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_TnEthRingCcmHoldUpTime_Type.__name__=_F
_TnEthRingCcmHoldUpTime_Object=MibTableColumn
tnEthRingCcmHoldUpTime=_TnEthRingCcmHoldUpTime_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,11),_TnEthRingCcmHoldUpTime_Type())
tnEthRingCcmHoldUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingCcmHoldUpTime.setStatus(_A)
if mibBuilder.loadTexts:tnEthRingCcmHoldUpTime.setUnits(_X)
class _TnEthRingRplNode_Type(TnEthRingRplNodeType):defaultValue=0
_TnEthRingRplNode_Type.__name__=_Z
_TnEthRingRplNode_Object=MibTableColumn
tnEthRingRplNode=_TnEthRingRplNode_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,12),_TnEthRingRplNode_Type())
tnEthRingRplNode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingRplNode.setStatus(_A)
_TnEthRingNodeId_Type=MacAddress
_TnEthRingNodeId_Object=MibTableColumn
tnEthRingNodeId=_TnEthRingNodeId_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,13),_TnEthRingNodeId_Type())
tnEthRingNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingNodeId.setStatus(_A)
_TnEthRingTxApsPdu_Type=TnEthRingApsInfoType
_TnEthRingTxApsPdu_Object=MibTableColumn
tnEthRingTxApsPdu=_TnEthRingTxApsPdu_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,14),_TnEthRingTxApsPdu_Type())
tnEthRingTxApsPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingTxApsPdu.setStatus(_A)
class _TnEthRingDefectStatus_Type(Bits):namedValues=NamedValues(('dFopPM',0))
_TnEthRingDefectStatus_Type.__name__='Bits'
_TnEthRingDefectStatus_Object=MibTableColumn
tnEthRingDefectStatus=_TnEthRingDefectStatus_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,15),_TnEthRingDefectStatus_Type())
tnEthRingDefectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingDefectStatus.setStatus(_A)
class _TnEthRingSubRingType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('virtualLink',1),('nonVirtualLink',2)))
_TnEthRingSubRingType_Type.__name__=_E
_TnEthRingSubRingType_Object=MibTableColumn
tnEthRingSubRingType=_TnEthRingSubRingType_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,16),_TnEthRingSubRingType_Type())
tnEthRingSubRingType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingSubRingType.setStatus(_A)
class _TnEthRingSubRingInterconnectId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967294),ValueRangeConstraint(4294967295,4294967295))
_TnEthRingSubRingInterconnectId_Type.__name__=_F
_TnEthRingSubRingInterconnectId_Object=MibTableColumn
tnEthRingSubRingInterconnectId=_TnEthRingSubRingInterconnectId_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,17),_TnEthRingSubRingInterconnectId_Type())
tnEthRingSubRingInterconnectId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingSubRingInterconnectId.setStatus(_A)
class _TnEthRingSubRingPropTopChange_Type(TruthValue):defaultValue=2
_TnEthRingSubRingPropTopChange_Type.__name__=_P
_TnEthRingSubRingPropTopChange_Object=MibTableColumn
tnEthRingSubRingPropTopChange=_TnEthRingSubRingPropTopChange_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,18),_TnEthRingSubRingPropTopChange_Type())
tnEthRingSubRingPropTopChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingSubRingPropTopChange.setStatus(_A)
class _TnEthRingCompatibleVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version1',1),('version2',2)))
_TnEthRingCompatibleVersion_Type.__name__=_E
_TnEthRingCompatibleVersion_Object=MibTableColumn
tnEthRingCompatibleVersion=_TnEthRingCompatibleVersion_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,19),_TnEthRingCompatibleVersion_Type())
tnEthRingCompatibleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingCompatibleVersion.setStatus(_A)
class _TnEthRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('deactivated',0),('idle',1),('protection',2),(_a,3),('forcedSwitch',4),('pending',5)))
_TnEthRingState_Type.__name__=_E
_TnEthRingState_Object=MibTableColumn
tnEthRingState=_TnEthRingState_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,20),_TnEthRingState_Type())
tnEthRingState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingState.setStatus(_A)
class _TnEthRingAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnEthRingAlmProfName_Type.__name__=_I
_TnEthRingAlmProfName_Object=MibTableColumn
tnEthRingAlmProfName=_TnEthRingAlmProfName_Object((1,3,6,1,4,1,7483,6,1,2,72,1,1,1,21),_TnEthRingAlmProfName_Type())
tnEthRingAlmProfName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingAlmProfName.setStatus(_A)
_TnEthRingPathTable_Object=MibTable
tnEthRingPathTable=_TnEthRingPathTable_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3))
if mibBuilder.loadTexts:tnEthRingPathTable.setStatus(_A)
_TnEthRingPathEntry_Object=MibTableRow
tnEthRingPathEntry=_TnEthRingPathEntry_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1))
tnEthRingPathEntry.setIndexNames((0,_G,_H),(0,_D,_L),(0,_D,_b))
if mibBuilder.loadTexts:tnEthRingPathEntry.setStatus(_A)
_TnEthRingPathIndex_Type=TnEthRingPathIndex
_TnEthRingPathIndex_Object=MibTableColumn
tnEthRingPathIndex=_TnEthRingPathIndex_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,1),_TnEthRingPathIndex_Type())
tnEthRingPathIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:tnEthRingPathIndex.setStatus(_A)
_TnEthRingPathRowStatus_Type=RowStatus
_TnEthRingPathRowStatus_Object=MibTableColumn
tnEthRingPathRowStatus=_TnEthRingPathRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,2),_TnEthRingPathRowStatus_Type())
tnEthRingPathRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingPathRowStatus.setStatus(_A)
_TnEthRingPathTimeStamp_Type=TimeStamp
_TnEthRingPathTimeStamp_Object=MibTableColumn
tnEthRingPathTimeStamp=_TnEthRingPathTimeStamp_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,3),_TnEthRingPathTimeStamp_Type())
tnEthRingPathTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingPathTimeStamp.setStatus(_A)
_TnEthRingPathIfIndex_Type=InterfaceIndexOrZero
_TnEthRingPathIfIndex_Object=MibTableColumn
tnEthRingPathIfIndex=_TnEthRingPathIfIndex_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,4),_TnEthRingPathIfIndex_Type())
tnEthRingPathIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingPathIfIndex.setStatus(_A)
_TnEthRingPathIfRapsCcTag_Type=TmnxEncapVal
_TnEthRingPathIfRapsCcTag_Object=MibTableColumn
tnEthRingPathIfRapsCcTag=_TnEthRingPathIfRapsCcTag_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,5),_TnEthRingPathIfRapsCcTag_Type())
tnEthRingPathIfRapsCcTag.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingPathIfRapsCcTag.setStatus(_A)
_TnEthRingPathDescription_Type=TItemDescription
_TnEthRingPathDescription_Object=MibTableColumn
tnEthRingPathDescription=_TnEthRingPathDescription_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,6),_TnEthRingPathDescription_Type())
tnEthRingPathDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingPathDescription.setStatus(_A)
class _TnEthRingPathAdminStatus_Type(TmnxAdminState):defaultValue=3
_TnEthRingPathAdminStatus_Type.__name__=_K
_TnEthRingPathAdminStatus_Object=MibTableColumn
tnEthRingPathAdminStatus=_TnEthRingPathAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,7),_TnEthRingPathAdminStatus_Type())
tnEthRingPathAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingPathAdminStatus.setStatus(_A)
_TnEthRingPathOperStatus_Type=TmnxOperState
_TnEthRingPathOperStatus_Object=MibTableColumn
tnEthRingPathOperStatus=_TnEthRingPathOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,8),_TnEthRingPathOperStatus_Type())
tnEthRingPathOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingPathOperStatus.setStatus(_A)
class _TnEthRingPathType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('rplEnd',1)))
_TnEthRingPathType_Type.__name__=_E
_TnEthRingPathType_Object=MibTableColumn
tnEthRingPathType=_TnEthRingPathType_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,9),_TnEthRingPathType_Type())
tnEthRingPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingPathType.setStatus(_A)
class _TnEthRingPathFwdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unblocked',0),('blocked',1)))
_TnEthRingPathFwdState_Type.__name__=_E
_TnEthRingPathFwdState_Object=MibTableColumn
tnEthRingPathFwdState=_TnEthRingPathFwdState_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,10),_TnEthRingPathFwdState_Type())
tnEthRingPathFwdState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingPathFwdState.setStatus(_A)
_TnEthRingPathFwdStateChgTime_Type=TimeStamp
_TnEthRingPathFwdStateChgTime_Object=MibTableColumn
tnEthRingPathFwdStateChgTime=_TnEthRingPathFwdStateChgTime_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,11),_TnEthRingPathFwdStateChgTime_Type())
tnEthRingPathFwdStateChgTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingPathFwdStateChgTime.setStatus(_A)
_TnEthRingPathRxApsPdu_Type=TnEthRingApsInfoType
_TnEthRingPathRxApsPdu_Object=MibTableColumn
tnEthRingPathRxApsPdu=_TnEthRingPathRxApsPdu_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,12),_TnEthRingPathRxApsPdu_Type())
tnEthRingPathRxApsPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingPathRxApsPdu.setStatus(_A)
class _TnEthRingPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('portDisabled',0),('portNormal',1),('portForcedSwitched',2),('portManualSwitched',3),('portFailedSF',4),('na',5)))
_TnEthRingPortState_Type.__name__=_E
_TnEthRingPortState_Object=MibTableColumn
tnEthRingPortState=_TnEthRingPortState_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,13),_TnEthRingPortState_Type())
tnEthRingPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingPortState.setStatus(_A)
class _TnEthRingPathAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnEthRingPathAlmProfName_Type.__name__=_I
_TnEthRingPathAlmProfName_Object=MibTableColumn
tnEthRingPathAlmProfName=_TnEthRingPathAlmProfName_Object((1,3,6,1,4,1,7483,6,1,2,72,1,3,1,14),_TnEthRingPathAlmProfName_Type())
tnEthRingPathAlmProfName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingPathAlmProfName.setStatus(_A)
_TnEthRingSAPConfigs_ObjectIdentity=ObjectIdentity
tnEthRingSAPConfigs=_TnEthRingSAPConfigs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,72,1,4))
_TnEthRingSAPPathTable_Object=MibTable
tnEthRingSAPPathTable=_TnEthRingSAPPathTable_Object((1,3,6,1,4,1,7483,6,1,2,72,1,4,1))
if mibBuilder.loadTexts:tnEthRingSAPPathTable.setStatus(_A)
_TnEthRingSAPPathEntry_Object=MibTableRow
tnEthRingSAPPathEntry=_TnEthRingSAPPathEntry_Object((1,3,6,1,4,1,7483,6,1,2,72,1,4,1,1))
tnEthRingSAPPathEntry.setIndexNames((0,_G,_H),(0,_S,_T),(0,_J,_R),(0,_J,_Q))
if mibBuilder.loadTexts:tnEthRingSAPPathEntry.setStatus(_A)
_TnEthRingSAPPathIndex_Type=Unsigned32
_TnEthRingSAPPathIndex_Object=MibTableColumn
tnEthRingSAPPathIndex=_TnEthRingSAPPathIndex_Object((1,3,6,1,4,1,7483,6,1,2,72,1,4,1,1,1),_TnEthRingSAPPathIndex_Type())
tnEthRingSAPPathIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingSAPPathIndex.setStatus(_A)
_TnEthRingSAPPathControlFlag_Type=TruthValue
_TnEthRingSAPPathControlFlag_Object=MibTableColumn
tnEthRingSAPPathControlFlag=_TnEthRingSAPPathControlFlag_Object((1,3,6,1,4,1,7483,6,1,2,72,1,4,1,1,2),_TnEthRingSAPPathControlFlag_Type())
tnEthRingSAPPathControlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingSAPPathControlFlag.setStatus(_A)
_TnEthRingCommandTable_Object=MibTable
tnEthRingCommandTable=_TnEthRingCommandTable_Object((1,3,6,1,4,1,7483,6,1,2,72,1,5))
if mibBuilder.loadTexts:tnEthRingCommandTable.setStatus(_A)
_TnEthRingCommandEntry_Object=MibTableRow
tnEthRingCommandEntry=_TnEthRingCommandEntry_Object((1,3,6,1,4,1,7483,6,1,2,72,1,5,1))
if mibBuilder.loadTexts:tnEthRingCommandEntry.setStatus(_A)
class _TnEthRingCommandSwitch_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noCmd',0),('clear',1),('forceSwitch',2),(_a,3)))
_TnEthRingCommandSwitch_Type.__name__=_E
_TnEthRingCommandSwitch_Object=MibTableColumn
tnEthRingCommandSwitch=_TnEthRingCommandSwitch_Object((1,3,6,1,4,1,7483,6,1,2,72,1,5,1,1),_TnEthRingCommandSwitch_Type())
tnEthRingCommandSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthRingCommandSwitch.setStatus(_A)
_TnEthRingConfigurationsScalar1_Type=Unsigned32
_TnEthRingConfigurationsScalar1_Object=MibScalar
tnEthRingConfigurationsScalar1=_TnEthRingConfigurationsScalar1_Object((1,3,6,1,4,1,7483,6,1,2,72,1,101),_TnEthRingConfigurationsScalar1_Type())
tnEthRingConfigurationsScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingConfigurationsScalar1.setStatus(_A)
_TnEthRingConfigurationsScalar2_Type=Unsigned32
_TnEthRingConfigurationsScalar2_Object=MibScalar
tnEthRingConfigurationsScalar2=_TnEthRingConfigurationsScalar2_Object((1,3,6,1,4,1,7483,6,1,2,72,1,102),_TnEthRingConfigurationsScalar2_Type())
tnEthRingConfigurationsScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEthRingConfigurationsScalar2.setStatus(_A)
_TnEthRingNotifyPrefix_ObjectIdentity=ObjectIdentity
tnEthRingNotifyPrefix=_TnEthRingNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,72))
_TnEthRingNotifications_ObjectIdentity=ObjectIdentity
tnEthRingNotifications=_TnEthRingNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,72,0))
_TnEthRingOprNotifications_ObjectIdentity=ObjectIdentity
tnEthRingOprNotifications=_TnEthRingOprNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,72,0,1))
_TnEthRingApsNotifications_ObjectIdentity=ObjectIdentity
tnEthRingApsNotifications=_TnEthRingApsNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,72,0,2))
tnEthRingPathEntry.registerAugmentions((_D,_c))
tnEthRingCommandEntry.setIndexNames(*tnEthRingPathEntry.getIndexNames())
tnEthRingPathFwdStateChange=NotificationType((1,3,6,1,4,1,7483,6,1,3,72,0,1,1))
tnEthRingPathFwdStateChange.setObjects((_D,_d))
if mibBuilder.loadTexts:tnEthRingPathFwdStateChange.setStatus(_A)
tnEthRingApsPrvsnRaiseAlarm=NotificationType((1,3,6,1,4,1,7483,6,1,3,72,0,2,1))
tnEthRingApsPrvsnRaiseAlarm.setObjects(*((_D,_M),(_D,_N),(_D,_O)))
if mibBuilder.loadTexts:tnEthRingApsPrvsnRaiseAlarm.setStatus(_A)
tnEthRingApsPrvsnClearAlarm=NotificationType((1,3,6,1,4,1,7483,6,1,3,72,0,2,2))
tnEthRingApsPrvsnClearAlarm.setObjects(*((_D,_M),(_D,_N),(_D,_O)))
if mibBuilder.loadTexts:tnEthRingApsPrvsnClearAlarm.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_V:TnEthRingIndex,'TnEthRingPathIndex':TnEthRingPathIndex,_Z:TnEthRingRplNodeType,'TnEthRingApsInfoType':TnEthRingApsInfoType,'tnEthRingMIBModule':tnEthRingMIBModule,'tnEthRingObjs':tnEthRingObjs,'tnEthRingConfigurations':tnEthRingConfigurations,'tnEthRingConfigTable':tnEthRingConfigTable,'tnEthRingConfigEntry':tnEthRingConfigEntry,_L:tnEthRingIndex,'tnEthRingRowStatus':tnEthRingRowStatus,'tnEthRingTimeStamp':tnEthRingTimeStamp,'tnEthRingDescription':tnEthRingDescription,'tnEthRingAdminState':tnEthRingAdminState,'tnEthRingOperState':tnEthRingOperState,'tnEthRingGuardTime':tnEthRingGuardTime,'tnEthRingRevertTime':tnEthRingRevertTime,'tnEthRingRevertTimeCountDn':tnEthRingRevertTimeCountDn,'tnEthRingCcmHoldDownTime':tnEthRingCcmHoldDownTime,'tnEthRingCcmHoldUpTime':tnEthRingCcmHoldUpTime,'tnEthRingRplNode':tnEthRingRplNode,'tnEthRingNodeId':tnEthRingNodeId,_M:tnEthRingTxApsPdu,_O:tnEthRingDefectStatus,'tnEthRingSubRingType':tnEthRingSubRingType,'tnEthRingSubRingInterconnectId':tnEthRingSubRingInterconnectId,'tnEthRingSubRingPropTopChange':tnEthRingSubRingPropTopChange,'tnEthRingCompatibleVersion':tnEthRingCompatibleVersion,'tnEthRingState':tnEthRingState,'tnEthRingAlmProfName':tnEthRingAlmProfName,'tnEthRingPathTable':tnEthRingPathTable,'tnEthRingPathEntry':tnEthRingPathEntry,_b:tnEthRingPathIndex,'tnEthRingPathRowStatus':tnEthRingPathRowStatus,'tnEthRingPathTimeStamp':tnEthRingPathTimeStamp,'tnEthRingPathIfIndex':tnEthRingPathIfIndex,'tnEthRingPathIfRapsCcTag':tnEthRingPathIfRapsCcTag,'tnEthRingPathDescription':tnEthRingPathDescription,'tnEthRingPathAdminStatus':tnEthRingPathAdminStatus,'tnEthRingPathOperStatus':tnEthRingPathOperStatus,'tnEthRingPathType':tnEthRingPathType,_d:tnEthRingPathFwdState,'tnEthRingPathFwdStateChgTime':tnEthRingPathFwdStateChgTime,_N:tnEthRingPathRxApsPdu,'tnEthRingPortState':tnEthRingPortState,'tnEthRingPathAlmProfName':tnEthRingPathAlmProfName,'tnEthRingSAPConfigs':tnEthRingSAPConfigs,'tnEthRingSAPPathTable':tnEthRingSAPPathTable,'tnEthRingSAPPathEntry':tnEthRingSAPPathEntry,'tnEthRingSAPPathIndex':tnEthRingSAPPathIndex,'tnEthRingSAPPathControlFlag':tnEthRingSAPPathControlFlag,'tnEthRingCommandTable':tnEthRingCommandTable,_c:tnEthRingCommandEntry,'tnEthRingCommandSwitch':tnEthRingCommandSwitch,'tnEthRingConfigurationsScalar1':tnEthRingConfigurationsScalar1,'tnEthRingConfigurationsScalar2':tnEthRingConfigurationsScalar2,'tnEthRingNotifyPrefix':tnEthRingNotifyPrefix,'tnEthRingNotifications':tnEthRingNotifications,'tnEthRingOprNotifications':tnEthRingOprNotifications,'tnEthRingPathFwdStateChange':tnEthRingPathFwdStateChange,'tnEthRingApsNotifications':tnEthRingApsNotifications,'tnEthRingApsPrvsnRaiseAlarm':tnEthRingApsPrvsnRaiseAlarm,'tnEthRingApsPrvsnClearAlarm':tnEthRingApsPrvsnClearAlarm})