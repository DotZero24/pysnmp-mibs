_B7='cmSatGroup'
_B6='satCfmMepSatResponderEnabled'
_B5='satResponderSessionRowStatus'
_B4='satResponderSessionStorageType'
_B3='satResponderSessionMepId'
_B2='satResponderSessionControlMepMacAddr'
_B1='satResponderSessionId'
_B0='satSacProfileRowStatus'
_A_='satSacProfileStorageType'
_Az='satSacProfileFDV'
_Ay='satSacProfileFTD'
_Ax='satSacProfileFLR'
_Aw='satSacProfileAlias'
_Av='satResultStatsIfNegFLT'
_Au='satResultStatsFlTCounts'
_At='satResultStatsFlrTMeasured'
_As='satResultStatsAvgIRT'
_Ar='satResultStatsIfNegFLY'
_Aq='satResultStatsIfNegFLG'
_Ap='satResultStatsISyncErrorsNum'
_Ao='satResultStatsIMaxFDVGMeasured'
_An='satResultStatsIAvgFDVGMeasured'
_Am='satResultStatsIMinFDVGMeasured'
_Al='satResultStatsMaxFTDGMeasured'
_Ak='satResultStatsAvgFTDGMeasured'
_Aj='satResultStatsMinFTDGMeasured'
_Ai='satResultStatsFlrYCounts'
_Ah='satResultStatsFlrGCounts'
_Ag='satResultStatsFlrYMeasured'
_Af='satResultStatsFlrGMeasured'
_Ae='satResultStatsMaxIRYMeasured'
_Ad='satResultStatsAvgIRYMeasured'
_Ac='satResultStatsMinIRYMeasured'
_Ab='satResultStatsMaxIRGMeasured'
_Aa='satResultStatsAvgIRGMeasured'
_AZ='satResultStatsMinIRGMeasured'
_AY='satResultStatsResult'
_AX='satResultStatsStatus'
_AW='satResultStatsEndTime'
_AV='satResultStatsStartTime'
_AU='satResultStatsSessionId'
_AT='satStreamMFactor'
_AS='satStreamDmmPktPriority'
_AR='satControlRowStatus'
_AQ='satControlStorageType'
_AP='satStreamRowStatus'
_AO='satStreamStorageType'
_AN='satStreamEbs'
_AM='satStreamCbs'
_AL='satStreamEirHi'
_AK='satStreamEirLo'
_AJ='satStreamCirHi'
_AI='satStreamCirLo'
_AH='satStreamColorMode'
_AG='satStreamYellowPcp'
_AF='satStreamGreenPcp'
_AE='satStreamDeiEnabled'
_AD='satStreamOuterVlanEtherType'
_AC='satStreamOuterVlanEnabled'
_AB='satStreamOuterVlanPri'
_AA='satStreamOuterVlanId'
_A9='satStreamInner2VlanEtherType'
_A8='satStreamInner2VlanEnabled'
_A7='satStreamInner2VlanPri'
_A6='satStreamInner2VlanId'
_A5='satStreamInner1ValnEtherType'
_A4='satStreamInner1VlanEnabled'
_A3='satStreamInner1VlanPri'
_A2='satStreamInner1VlanId'
_A1='satStreamCurrentConfigCirTestStep'
_A0='satStreamCurrentTestProcedure'
_z='satStreamStatus'
_y='satStreamAction'
_x='satStreamOverallResult'
_w='satStreamDmmPacketInterval'
_v='satStreamDmmPacketSize'
_u='satStreamDestMepMacAddr'
_t='satStreamDestMepId'
_s='satStreamDestMepType'
_r='satStreamSrcMepId'
_q='satStreamSacProfileId'
_p='satStreamFrameSizeList'
_o='satStreamCustomFramePayload'
_n='satStreamFramePayloadType'
_m='satStreamDestMacAddress'
_l='satStreamTestDirection'
_k='satStreamTestPort'
_j='satStreamName'
_i='satControlFlpduTagOverride'
_h='satControlTestStartTime'
_g='satControlFailCause'
_f='satControlAction'
_e='satControlStatus'
_d='satControlPerfTestDuration'
_c='satControlConfigCIRTestStepDuration'
_b='satControlConfigCIRTestStepNum'
_a='satControlConfigTestDuration'
_Z='satControlTestProcedures'
_Y='satControlTestMode'
_X='satControlName'
_W='satCfmMepExtEntry'
_V='networkElementSatParamsEntry'
_U='configTestPolicing'
_T='configTestEbs'
_S='configTestCbs'
_R='configTestEir'
_Q='configTestCir'
_P='satResponderSessionIndex'
_O='satSacProfileIndex'
_N='satResultStatsStepNumber'
_M='satResultStatsTestType'
_L='Integer32'
_K='satStreamIndex'
_J='satControlIndex'
_I='DisplayString'
_H='neIndex'
_G='CM-ENTITY-MIB'
_F='not-accessible'
_E='read-create'
_D='read-only'
_C='read-write'
_B='CM-SAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
AdminState,CmPmBinAction,MepDestinationType,OperationalState,SecondaryState,VlanId,VlanPriority=mibBuilder.importSymbols('CM-COMMON-MIB','AdminState','CmPmBinAction','MepDestinationType','OperationalState','SecondaryState','VlanId','VlanPriority')
neIndex,networkElementEntry,shelfIndex,slotIndex=mibBuilder.importSymbols(_G,_H,'networkElementEntry','shelfIndex','slotIndex')
PolicerColorMode,=mibBuilder.importSymbols('CM-FACILITY-MIB','PolicerColorMode')
EsaProbePktIntervalType,=mibBuilder.importSymbols('CM-SA-MIB','EsaProbePktIntervalType')
Dot1agCfmMepIdOrZero,dot1agCfmMepEntry=mibBuilder.importSymbols('IEEE8021-CFM-MIB','Dot1agCfmMepIdOrZero','dot1agCfmMepEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'MacAddress','PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue','VariablePointer')
cmServiceActivationMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,28))
if mibBuilder.loadTexts:cmServiceActivationMIB.setRevisions(('2013-09-12 00:00',))
class ServiceActivationTestMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneWay',1),('twoWay',2)))
class SatProceduresType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),('performanceTest',7)))
class SatProceduresList(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),('performance',6)))
class SatStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('completed',1),('notStarted',2),('inProgress',3),('failed',4)))
class SatDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('backward',2)))
class SatFramePayloadType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('prbs31',1),('custom',2)))
class SatTestAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),('stop',2),('notApplicable',3)))
class SatResult(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('pass',2),('fail',3)))
_CmServActivationObjects_ObjectIdentity=ObjectIdentity
cmServActivationObjects=_CmServActivationObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,28,1))
_SatControlTable_Object=MibTable
satControlTable=_SatControlTable_Object((1,3,6,1,4,1,2544,1,12,28,1,1))
if mibBuilder.loadTexts:satControlTable.setStatus(_A)
_SatControlEntry_Object=MibTableRow
satControlEntry=_SatControlEntry_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1))
satControlEntry.setIndexNames((0,_G,_H),(0,_B,_J))
if mibBuilder.loadTexts:satControlEntry.setStatus(_A)
_SatControlIndex_Type=Integer32
_SatControlIndex_Object=MibTableColumn
satControlIndex=_SatControlIndex_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,1),_SatControlIndex_Type())
satControlIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:satControlIndex.setStatus(_A)
class _SatControlName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SatControlName_Type.__name__=_I
_SatControlName_Object=MibTableColumn
satControlName=_SatControlName_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,2),_SatControlName_Type())
satControlName.setMaxAccess(_C)
if mibBuilder.loadTexts:satControlName.setStatus(_A)
_SatControlTestMode_Type=ServiceActivationTestMode
_SatControlTestMode_Object=MibTableColumn
satControlTestMode=_SatControlTestMode_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,3),_SatControlTestMode_Type())
satControlTestMode.setMaxAccess(_C)
if mibBuilder.loadTexts:satControlTestMode.setStatus(_A)
_SatControlTestProcedures_Type=SatProceduresList
_SatControlTestProcedures_Object=MibTableColumn
satControlTestProcedures=_SatControlTestProcedures_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,4),_SatControlTestProcedures_Type())
satControlTestProcedures.setMaxAccess(_C)
if mibBuilder.loadTexts:satControlTestProcedures.setStatus(_A)
_SatControlConfigTestDuration_Type=Integer32
_SatControlConfigTestDuration_Object=MibTableColumn
satControlConfigTestDuration=_SatControlConfigTestDuration_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,5),_SatControlConfigTestDuration_Type())
satControlConfigTestDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:satControlConfigTestDuration.setStatus(_A)
class _SatControlConfigCIRTestStepNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SatControlConfigCIRTestStepNum_Type.__name__=_L
_SatControlConfigCIRTestStepNum_Object=MibTableColumn
satControlConfigCIRTestStepNum=_SatControlConfigCIRTestStepNum_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,6),_SatControlConfigCIRTestStepNum_Type())
satControlConfigCIRTestStepNum.setMaxAccess(_C)
if mibBuilder.loadTexts:satControlConfigCIRTestStepNum.setStatus(_A)
class _SatControlConfigCIRTestStepDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_SatControlConfigCIRTestStepDuration_Type.__name__=_L
_SatControlConfigCIRTestStepDuration_Object=MibTableColumn
satControlConfigCIRTestStepDuration=_SatControlConfigCIRTestStepDuration_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,7),_SatControlConfigCIRTestStepDuration_Type())
satControlConfigCIRTestStepDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:satControlConfigCIRTestStepDuration.setStatus(_A)
_SatControlPerfTestDuration_Type=Integer32
_SatControlPerfTestDuration_Object=MibTableColumn
satControlPerfTestDuration=_SatControlPerfTestDuration_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,8),_SatControlPerfTestDuration_Type())
satControlPerfTestDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:satControlPerfTestDuration.setStatus(_A)
_SatControlStatus_Type=SatStatus
_SatControlStatus_Object=MibTableColumn
satControlStatus=_SatControlStatus_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,9),_SatControlStatus_Type())
satControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:satControlStatus.setStatus(_A)
_SatControlAction_Type=SatTestAction
_SatControlAction_Object=MibTableColumn
satControlAction=_SatControlAction_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,10),_SatControlAction_Type())
satControlAction.setMaxAccess(_C)
if mibBuilder.loadTexts:satControlAction.setStatus(_A)
_SatControlStorageType_Type=StorageType
_SatControlStorageType_Object=MibTableColumn
satControlStorageType=_SatControlStorageType_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,11),_SatControlStorageType_Type())
satControlStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:satControlStorageType.setStatus(_A)
_SatControlRowStatus_Type=RowStatus
_SatControlRowStatus_Object=MibTableColumn
satControlRowStatus=_SatControlRowStatus_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,12),_SatControlRowStatus_Type())
satControlRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:satControlRowStatus.setStatus(_A)
_SatControlFailCause_Type=DisplayString
_SatControlFailCause_Object=MibTableColumn
satControlFailCause=_SatControlFailCause_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,13),_SatControlFailCause_Type())
satControlFailCause.setMaxAccess(_D)
if mibBuilder.loadTexts:satControlFailCause.setStatus(_A)
_SatControlTestStartTime_Type=DateAndTime
_SatControlTestStartTime_Object=MibTableColumn
satControlTestStartTime=_SatControlTestStartTime_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,14),_SatControlTestStartTime_Type())
satControlTestStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:satControlTestStartTime.setStatus(_A)
_SatControlFlpduTagOverride_Type=TruthValue
_SatControlFlpduTagOverride_Object=MibTableColumn
satControlFlpduTagOverride=_SatControlFlpduTagOverride_Object((1,3,6,1,4,1,2544,1,12,28,1,1,1,15),_SatControlFlpduTagOverride_Type())
satControlFlpduTagOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:satControlFlpduTagOverride.setStatus(_A)
_SatStreamTable_Object=MibTable
satStreamTable=_SatStreamTable_Object((1,3,6,1,4,1,2544,1,12,28,1,2))
if mibBuilder.loadTexts:satStreamTable.setStatus(_A)
_SatStreamEntry_Object=MibTableRow
satStreamEntry=_SatStreamEntry_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1))
satStreamEntry.setIndexNames((0,_G,_H),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:satStreamEntry.setStatus(_A)
_SatStreamIndex_Type=Integer32
_SatStreamIndex_Object=MibTableColumn
satStreamIndex=_SatStreamIndex_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,1),_SatStreamIndex_Type())
satStreamIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:satStreamIndex.setStatus(_A)
class _SatStreamName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SatStreamName_Type.__name__=_I
_SatStreamName_Object=MibTableColumn
satStreamName=_SatStreamName_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,2),_SatStreamName_Type())
satStreamName.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamName.setStatus(_A)
_SatStreamTestPort_Type=VariablePointer
_SatStreamTestPort_Object=MibTableColumn
satStreamTestPort=_SatStreamTestPort_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,3),_SatStreamTestPort_Type())
satStreamTestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamTestPort.setStatus(_A)
_SatStreamTestDirection_Type=SatDirection
_SatStreamTestDirection_Object=MibTableColumn
satStreamTestDirection=_SatStreamTestDirection_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,4),_SatStreamTestDirection_Type())
satStreamTestDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamTestDirection.setStatus(_A)
_SatStreamDestMacAddress_Type=MacAddress
_SatStreamDestMacAddress_Object=MibTableColumn
satStreamDestMacAddress=_SatStreamDestMacAddress_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,5),_SatStreamDestMacAddress_Type())
satStreamDestMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamDestMacAddress.setStatus(_A)
_SatStreamFramePayloadType_Type=SatFramePayloadType
_SatStreamFramePayloadType_Object=MibTableColumn
satStreamFramePayloadType=_SatStreamFramePayloadType_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,6),_SatStreamFramePayloadType_Type())
satStreamFramePayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamFramePayloadType.setStatus(_A)
class _SatStreamCustomFramePayload_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SatStreamCustomFramePayload_Type.__name__=_I
_SatStreamCustomFramePayload_Object=MibTableColumn
satStreamCustomFramePayload=_SatStreamCustomFramePayload_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,7),_SatStreamCustomFramePayload_Type())
satStreamCustomFramePayload.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamCustomFramePayload.setStatus(_A)
_SatStreamFrameSizeList_Type=DisplayString
_SatStreamFrameSizeList_Object=MibTableColumn
satStreamFrameSizeList=_SatStreamFrameSizeList_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,8),_SatStreamFrameSizeList_Type())
satStreamFrameSizeList.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamFrameSizeList.setStatus(_A)
_SatStreamSacProfileId_Type=VariablePointer
_SatStreamSacProfileId_Object=MibTableColumn
satStreamSacProfileId=_SatStreamSacProfileId_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,9),_SatStreamSacProfileId_Type())
satStreamSacProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamSacProfileId.setStatus(_A)
_SatStreamSrcMepId_Type=VariablePointer
_SatStreamSrcMepId_Object=MibTableColumn
satStreamSrcMepId=_SatStreamSrcMepId_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,10),_SatStreamSrcMepId_Type())
satStreamSrcMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamSrcMepId.setStatus(_A)
_SatStreamDestMepType_Type=MepDestinationType
_SatStreamDestMepType_Object=MibTableColumn
satStreamDestMepType=_SatStreamDestMepType_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,11),_SatStreamDestMepType_Type())
satStreamDestMepType.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamDestMepType.setStatus(_A)
_SatStreamDestMepId_Type=Integer32
_SatStreamDestMepId_Object=MibTableColumn
satStreamDestMepId=_SatStreamDestMepId_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,12),_SatStreamDestMepId_Type())
satStreamDestMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamDestMepId.setStatus(_A)
_SatStreamDestMepMacAddr_Type=MacAddress
_SatStreamDestMepMacAddr_Object=MibTableColumn
satStreamDestMepMacAddr=_SatStreamDestMepMacAddr_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,13),_SatStreamDestMepMacAddr_Type())
satStreamDestMepMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamDestMepMacAddr.setStatus(_A)
_SatStreamDmmPacketSize_Type=Integer32
_SatStreamDmmPacketSize_Object=MibTableColumn
satStreamDmmPacketSize=_SatStreamDmmPacketSize_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,14),_SatStreamDmmPacketSize_Type())
satStreamDmmPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamDmmPacketSize.setStatus(_A)
_SatStreamDmmPacketInterval_Type=EsaProbePktIntervalType
_SatStreamDmmPacketInterval_Object=MibTableColumn
satStreamDmmPacketInterval=_SatStreamDmmPacketInterval_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,15),_SatStreamDmmPacketInterval_Type())
satStreamDmmPacketInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamDmmPacketInterval.setStatus(_A)
_SatStreamOverallResult_Type=SatResult
_SatStreamOverallResult_Object=MibTableColumn
satStreamOverallResult=_SatStreamOverallResult_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,16),_SatStreamOverallResult_Type())
satStreamOverallResult.setMaxAccess(_D)
if mibBuilder.loadTexts:satStreamOverallResult.setStatus(_A)
_SatStreamAction_Type=SatTestAction
_SatStreamAction_Object=MibTableColumn
satStreamAction=_SatStreamAction_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,17),_SatStreamAction_Type())
satStreamAction.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamAction.setStatus(_A)
_SatStreamStatus_Type=SatStatus
_SatStreamStatus_Object=MibTableColumn
satStreamStatus=_SatStreamStatus_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,18),_SatStreamStatus_Type())
satStreamStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:satStreamStatus.setStatus(_A)
_SatStreamCurrentTestProcedure_Type=SatProceduresType
_SatStreamCurrentTestProcedure_Object=MibTableColumn
satStreamCurrentTestProcedure=_SatStreamCurrentTestProcedure_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,19),_SatStreamCurrentTestProcedure_Type())
satStreamCurrentTestProcedure.setMaxAccess(_D)
if mibBuilder.loadTexts:satStreamCurrentTestProcedure.setStatus(_A)
_SatStreamCurrentConfigCirTestStep_Type=Integer32
_SatStreamCurrentConfigCirTestStep_Object=MibTableColumn
satStreamCurrentConfigCirTestStep=_SatStreamCurrentConfigCirTestStep_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,20),_SatStreamCurrentConfigCirTestStep_Type())
satStreamCurrentConfigCirTestStep.setMaxAccess(_D)
if mibBuilder.loadTexts:satStreamCurrentConfigCirTestStep.setStatus(_A)
_SatStreamInner1VlanId_Type=VlanId
_SatStreamInner1VlanId_Object=MibTableColumn
satStreamInner1VlanId=_SatStreamInner1VlanId_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,21),_SatStreamInner1VlanId_Type())
satStreamInner1VlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamInner1VlanId.setStatus(_A)
_SatStreamInner1VlanPri_Type=VlanPriority
_SatStreamInner1VlanPri_Object=MibTableColumn
satStreamInner1VlanPri=_SatStreamInner1VlanPri_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,22),_SatStreamInner1VlanPri_Type())
satStreamInner1VlanPri.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamInner1VlanPri.setStatus(_A)
_SatStreamInner1VlanEnabled_Type=TruthValue
_SatStreamInner1VlanEnabled_Object=MibTableColumn
satStreamInner1VlanEnabled=_SatStreamInner1VlanEnabled_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,23),_SatStreamInner1VlanEnabled_Type())
satStreamInner1VlanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamInner1VlanEnabled.setStatus(_A)
_SatStreamInner1ValnEtherType_Type=Integer32
_SatStreamInner1ValnEtherType_Object=MibTableColumn
satStreamInner1ValnEtherType=_SatStreamInner1ValnEtherType_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,24),_SatStreamInner1ValnEtherType_Type())
satStreamInner1ValnEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamInner1ValnEtherType.setStatus(_A)
_SatStreamInner2VlanId_Type=VlanId
_SatStreamInner2VlanId_Object=MibTableColumn
satStreamInner2VlanId=_SatStreamInner2VlanId_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,25),_SatStreamInner2VlanId_Type())
satStreamInner2VlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamInner2VlanId.setStatus(_A)
_SatStreamInner2VlanPri_Type=VlanPriority
_SatStreamInner2VlanPri_Object=MibTableColumn
satStreamInner2VlanPri=_SatStreamInner2VlanPri_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,26),_SatStreamInner2VlanPri_Type())
satStreamInner2VlanPri.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamInner2VlanPri.setStatus(_A)
_SatStreamInner2VlanEnabled_Type=TruthValue
_SatStreamInner2VlanEnabled_Object=MibTableColumn
satStreamInner2VlanEnabled=_SatStreamInner2VlanEnabled_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,27),_SatStreamInner2VlanEnabled_Type())
satStreamInner2VlanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamInner2VlanEnabled.setStatus(_A)
_SatStreamInner2VlanEtherType_Type=Integer32
_SatStreamInner2VlanEtherType_Object=MibTableColumn
satStreamInner2VlanEtherType=_SatStreamInner2VlanEtherType_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,28),_SatStreamInner2VlanEtherType_Type())
satStreamInner2VlanEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamInner2VlanEtherType.setStatus(_A)
_SatStreamOuterVlanId_Type=VlanId
_SatStreamOuterVlanId_Object=MibTableColumn
satStreamOuterVlanId=_SatStreamOuterVlanId_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,29),_SatStreamOuterVlanId_Type())
satStreamOuterVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamOuterVlanId.setStatus(_A)
_SatStreamOuterVlanPri_Type=VlanPriority
_SatStreamOuterVlanPri_Object=MibTableColumn
satStreamOuterVlanPri=_SatStreamOuterVlanPri_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,30),_SatStreamOuterVlanPri_Type())
satStreamOuterVlanPri.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamOuterVlanPri.setStatus(_A)
_SatStreamOuterVlanEnabled_Type=TruthValue
_SatStreamOuterVlanEnabled_Object=MibTableColumn
satStreamOuterVlanEnabled=_SatStreamOuterVlanEnabled_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,31),_SatStreamOuterVlanEnabled_Type())
satStreamOuterVlanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamOuterVlanEnabled.setStatus(_A)
_SatStreamOuterVlanEtherType_Type=Integer32
_SatStreamOuterVlanEtherType_Object=MibTableColumn
satStreamOuterVlanEtherType=_SatStreamOuterVlanEtherType_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,32),_SatStreamOuterVlanEtherType_Type())
satStreamOuterVlanEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamOuterVlanEtherType.setStatus(_A)
_SatStreamDeiEnabled_Type=TruthValue
_SatStreamDeiEnabled_Object=MibTableColumn
satStreamDeiEnabled=_SatStreamDeiEnabled_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,33),_SatStreamDeiEnabled_Type())
satStreamDeiEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamDeiEnabled.setStatus(_A)
_SatStreamGreenPcp_Type=Integer32
_SatStreamGreenPcp_Object=MibTableColumn
satStreamGreenPcp=_SatStreamGreenPcp_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,34),_SatStreamGreenPcp_Type())
satStreamGreenPcp.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamGreenPcp.setStatus(_A)
_SatStreamYellowPcp_Type=Integer32
_SatStreamYellowPcp_Object=MibTableColumn
satStreamYellowPcp=_SatStreamYellowPcp_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,35),_SatStreamYellowPcp_Type())
satStreamYellowPcp.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamYellowPcp.setStatus(_A)
_SatStreamColorMode_Type=PolicerColorMode
_SatStreamColorMode_Object=MibTableColumn
satStreamColorMode=_SatStreamColorMode_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,36),_SatStreamColorMode_Type())
satStreamColorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamColorMode.setStatus(_A)
_SatStreamCirLo_Type=Unsigned32
_SatStreamCirLo_Object=MibTableColumn
satStreamCirLo=_SatStreamCirLo_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,37),_SatStreamCirLo_Type())
satStreamCirLo.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamCirLo.setStatus(_A)
_SatStreamCirHi_Type=Unsigned32
_SatStreamCirHi_Object=MibTableColumn
satStreamCirHi=_SatStreamCirHi_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,38),_SatStreamCirHi_Type())
satStreamCirHi.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamCirHi.setStatus(_A)
_SatStreamEirLo_Type=Unsigned32
_SatStreamEirLo_Object=MibTableColumn
satStreamEirLo=_SatStreamEirLo_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,39),_SatStreamEirLo_Type())
satStreamEirLo.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamEirLo.setStatus(_A)
_SatStreamEirHi_Type=Unsigned32
_SatStreamEirHi_Object=MibTableColumn
satStreamEirHi=_SatStreamEirHi_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,40),_SatStreamEirHi_Type())
satStreamEirHi.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamEirHi.setStatus(_A)
_SatStreamCbs_Type=Unsigned32
_SatStreamCbs_Object=MibTableColumn
satStreamCbs=_SatStreamCbs_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,41),_SatStreamCbs_Type())
satStreamCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamCbs.setStatus(_A)
_SatStreamEbs_Type=Unsigned32
_SatStreamEbs_Object=MibTableColumn
satStreamEbs=_SatStreamEbs_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,42),_SatStreamEbs_Type())
satStreamEbs.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamEbs.setStatus(_A)
_SatStreamStorageType_Type=StorageType
_SatStreamStorageType_Object=MibTableColumn
satStreamStorageType=_SatStreamStorageType_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,43),_SatStreamStorageType_Type())
satStreamStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:satStreamStorageType.setStatus(_A)
_SatStreamRowStatus_Type=RowStatus
_SatStreamRowStatus_Object=MibTableColumn
satStreamRowStatus=_SatStreamRowStatus_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,44),_SatStreamRowStatus_Type())
satStreamRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:satStreamRowStatus.setStatus(_A)
_SatStreamDmmPktPriority_Type=VlanPriority
_SatStreamDmmPktPriority_Object=MibTableColumn
satStreamDmmPktPriority=_SatStreamDmmPktPriority_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,45),_SatStreamDmmPktPriority_Type())
satStreamDmmPktPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamDmmPktPriority.setStatus(_A)
_SatStreamMFactor_Type=Unsigned32
_SatStreamMFactor_Object=MibTableColumn
satStreamMFactor=_SatStreamMFactor_Object((1,3,6,1,4,1,2544,1,12,28,1,2,1,46),_SatStreamMFactor_Type())
satStreamMFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:satStreamMFactor.setStatus(_A)
_SatResultStatsTable_Object=MibTable
satResultStatsTable=_SatResultStatsTable_Object((1,3,6,1,4,1,2544,1,12,28,1,3))
if mibBuilder.loadTexts:satResultStatsTable.setStatus(_A)
_SatResultStatsEntry_Object=MibTableRow
satResultStatsEntry=_SatResultStatsEntry_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1))
satResultStatsEntry.setIndexNames((0,_G,_H),(0,_B,_J),(0,_B,_K),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:satResultStatsEntry.setStatus(_A)
_SatResultStatsTestType_Type=SatProceduresType
_SatResultStatsTestType_Object=MibTableColumn
satResultStatsTestType=_SatResultStatsTestType_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,1),_SatResultStatsTestType_Type())
satResultStatsTestType.setMaxAccess(_F)
if mibBuilder.loadTexts:satResultStatsTestType.setStatus(_A)
_SatResultStatsStepNumber_Type=Integer32
_SatResultStatsStepNumber_Object=MibTableColumn
satResultStatsStepNumber=_SatResultStatsStepNumber_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,2),_SatResultStatsStepNumber_Type())
satResultStatsStepNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:satResultStatsStepNumber.setStatus(_A)
_SatResultStatsSessionId_Type=Unsigned32
_SatResultStatsSessionId_Object=MibTableColumn
satResultStatsSessionId=_SatResultStatsSessionId_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,3),_SatResultStatsSessionId_Type())
satResultStatsSessionId.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsSessionId.setStatus(_A)
_SatResultStatsStartTime_Type=DateAndTime
_SatResultStatsStartTime_Object=MibTableColumn
satResultStatsStartTime=_SatResultStatsStartTime_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,4),_SatResultStatsStartTime_Type())
satResultStatsStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsStartTime.setStatus(_A)
_SatResultStatsEndTime_Type=DateAndTime
_SatResultStatsEndTime_Object=MibTableColumn
satResultStatsEndTime=_SatResultStatsEndTime_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,5),_SatResultStatsEndTime_Type())
satResultStatsEndTime.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsEndTime.setStatus(_A)
_SatResultStatsStatus_Type=SatStatus
_SatResultStatsStatus_Object=MibTableColumn
satResultStatsStatus=_SatResultStatsStatus_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,6),_SatResultStatsStatus_Type())
satResultStatsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsStatus.setStatus(_A)
_SatResultStatsResult_Type=SatResult
_SatResultStatsResult_Object=MibTableColumn
satResultStatsResult=_SatResultStatsResult_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,7),_SatResultStatsResult_Type())
satResultStatsResult.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsResult.setStatus(_A)
_SatResultStatsMinIRGMeasured_Type=Counter64
_SatResultStatsMinIRGMeasured_Object=MibTableColumn
satResultStatsMinIRGMeasured=_SatResultStatsMinIRGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,8),_SatResultStatsMinIRGMeasured_Type())
satResultStatsMinIRGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsMinIRGMeasured.setStatus(_A)
_SatResultStatsAvgIRGMeasured_Type=Counter64
_SatResultStatsAvgIRGMeasured_Object=MibTableColumn
satResultStatsAvgIRGMeasured=_SatResultStatsAvgIRGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,9),_SatResultStatsAvgIRGMeasured_Type())
satResultStatsAvgIRGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsAvgIRGMeasured.setStatus(_A)
_SatResultStatsMaxIRGMeasured_Type=Counter64
_SatResultStatsMaxIRGMeasured_Object=MibTableColumn
satResultStatsMaxIRGMeasured=_SatResultStatsMaxIRGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,10),_SatResultStatsMaxIRGMeasured_Type())
satResultStatsMaxIRGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsMaxIRGMeasured.setStatus(_A)
_SatResultStatsMinIRYMeasured_Type=Counter64
_SatResultStatsMinIRYMeasured_Object=MibTableColumn
satResultStatsMinIRYMeasured=_SatResultStatsMinIRYMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,11),_SatResultStatsMinIRYMeasured_Type())
satResultStatsMinIRYMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsMinIRYMeasured.setStatus(_A)
_SatResultStatsAvgIRYMeasured_Type=Counter64
_SatResultStatsAvgIRYMeasured_Object=MibTableColumn
satResultStatsAvgIRYMeasured=_SatResultStatsAvgIRYMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,12),_SatResultStatsAvgIRYMeasured_Type())
satResultStatsAvgIRYMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsAvgIRYMeasured.setStatus(_A)
_SatResultStatsMaxIRYMeasured_Type=Counter64
_SatResultStatsMaxIRYMeasured_Object=MibTableColumn
satResultStatsMaxIRYMeasured=_SatResultStatsMaxIRYMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,13),_SatResultStatsMaxIRYMeasured_Type())
satResultStatsMaxIRYMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsMaxIRYMeasured.setStatus(_A)
_SatResultStatsFlrGMeasured_Type=Integer32
_SatResultStatsFlrGMeasured_Object=MibTableColumn
satResultStatsFlrGMeasured=_SatResultStatsFlrGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,14),_SatResultStatsFlrGMeasured_Type())
satResultStatsFlrGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsFlrGMeasured.setStatus(_A)
_SatResultStatsFlrYMeasured_Type=Integer32
_SatResultStatsFlrYMeasured_Object=MibTableColumn
satResultStatsFlrYMeasured=_SatResultStatsFlrYMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,15),_SatResultStatsFlrYMeasured_Type())
satResultStatsFlrYMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsFlrYMeasured.setStatus(_A)
_SatResultStatsFlrGCounts_Type=Counter64
_SatResultStatsFlrGCounts_Object=MibTableColumn
satResultStatsFlrGCounts=_SatResultStatsFlrGCounts_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,16),_SatResultStatsFlrGCounts_Type())
satResultStatsFlrGCounts.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsFlrGCounts.setStatus(_A)
_SatResultStatsFlrYCounts_Type=Counter64
_SatResultStatsFlrYCounts_Object=MibTableColumn
satResultStatsFlrYCounts=_SatResultStatsFlrYCounts_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,17),_SatResultStatsFlrYCounts_Type())
satResultStatsFlrYCounts.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsFlrYCounts.setStatus(_A)
_SatResultStatsMinFTDGMeasured_Type=Unsigned32
_SatResultStatsMinFTDGMeasured_Object=MibTableColumn
satResultStatsMinFTDGMeasured=_SatResultStatsMinFTDGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,18),_SatResultStatsMinFTDGMeasured_Type())
satResultStatsMinFTDGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsMinFTDGMeasured.setStatus(_A)
_SatResultStatsAvgFTDGMeasured_Type=Unsigned32
_SatResultStatsAvgFTDGMeasured_Object=MibTableColumn
satResultStatsAvgFTDGMeasured=_SatResultStatsAvgFTDGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,19),_SatResultStatsAvgFTDGMeasured_Type())
satResultStatsAvgFTDGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsAvgFTDGMeasured.setStatus(_A)
_SatResultStatsMaxFTDGMeasured_Type=Unsigned32
_SatResultStatsMaxFTDGMeasured_Object=MibTableColumn
satResultStatsMaxFTDGMeasured=_SatResultStatsMaxFTDGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,20),_SatResultStatsMaxFTDGMeasured_Type())
satResultStatsMaxFTDGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsMaxFTDGMeasured.setStatus(_A)
_SatResultStatsIMinFDVGMeasured_Type=Unsigned32
_SatResultStatsIMinFDVGMeasured_Object=MibTableColumn
satResultStatsIMinFDVGMeasured=_SatResultStatsIMinFDVGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,21),_SatResultStatsIMinFDVGMeasured_Type())
satResultStatsIMinFDVGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsIMinFDVGMeasured.setStatus(_A)
_SatResultStatsIAvgFDVGMeasured_Type=Unsigned32
_SatResultStatsIAvgFDVGMeasured_Object=MibTableColumn
satResultStatsIAvgFDVGMeasured=_SatResultStatsIAvgFDVGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,22),_SatResultStatsIAvgFDVGMeasured_Type())
satResultStatsIAvgFDVGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsIAvgFDVGMeasured.setStatus(_A)
_SatResultStatsIMaxFDVGMeasured_Type=Unsigned32
_SatResultStatsIMaxFDVGMeasured_Object=MibTableColumn
satResultStatsIMaxFDVGMeasured=_SatResultStatsIMaxFDVGMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,23),_SatResultStatsIMaxFDVGMeasured_Type())
satResultStatsIMaxFDVGMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsIMaxFDVGMeasured.setStatus(_A)
_SatResultStatsISyncErrorsNum_Type=Unsigned32
_SatResultStatsISyncErrorsNum_Object=MibTableColumn
satResultStatsISyncErrorsNum=_SatResultStatsISyncErrorsNum_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,24),_SatResultStatsISyncErrorsNum_Type())
satResultStatsISyncErrorsNum.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsISyncErrorsNum.setStatus(_A)
_SatResultStatsIfNegFLG_Type=TruthValue
_SatResultStatsIfNegFLG_Object=MibTableColumn
satResultStatsIfNegFLG=_SatResultStatsIfNegFLG_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,25),_SatResultStatsIfNegFLG_Type())
satResultStatsIfNegFLG.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsIfNegFLG.setStatus(_A)
_SatResultStatsIfNegFLY_Type=TruthValue
_SatResultStatsIfNegFLY_Object=MibTableColumn
satResultStatsIfNegFLY=_SatResultStatsIfNegFLY_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,26),_SatResultStatsIfNegFLY_Type())
satResultStatsIfNegFLY.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsIfNegFLY.setStatus(_A)
_SatResultStatsAvgIRT_Type=Counter64
_SatResultStatsAvgIRT_Object=MibTableColumn
satResultStatsAvgIRT=_SatResultStatsAvgIRT_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,27),_SatResultStatsAvgIRT_Type())
satResultStatsAvgIRT.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsAvgIRT.setStatus(_A)
_SatResultStatsFlrTMeasured_Type=Integer32
_SatResultStatsFlrTMeasured_Object=MibTableColumn
satResultStatsFlrTMeasured=_SatResultStatsFlrTMeasured_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,28),_SatResultStatsFlrTMeasured_Type())
satResultStatsFlrTMeasured.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsFlrTMeasured.setStatus(_A)
_SatResultStatsFlTCounts_Type=Counter64
_SatResultStatsFlTCounts_Object=MibTableColumn
satResultStatsFlTCounts=_SatResultStatsFlTCounts_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,29),_SatResultStatsFlTCounts_Type())
satResultStatsFlTCounts.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsFlTCounts.setStatus(_A)
_SatResultStatsIfNegFLT_Type=TruthValue
_SatResultStatsIfNegFLT_Object=MibTableColumn
satResultStatsIfNegFLT=_SatResultStatsIfNegFLT_Object((1,3,6,1,4,1,2544,1,12,28,1,3,1,30),_SatResultStatsIfNegFLT_Type())
satResultStatsIfNegFLT.setMaxAccess(_D)
if mibBuilder.loadTexts:satResultStatsIfNegFLT.setStatus(_A)
_SatSacProfileTable_Object=MibTable
satSacProfileTable=_SatSacProfileTable_Object((1,3,6,1,4,1,2544,1,12,28,1,4))
if mibBuilder.loadTexts:satSacProfileTable.setStatus(_A)
_SatSacProfileEntry_Object=MibTableRow
satSacProfileEntry=_SatSacProfileEntry_Object((1,3,6,1,4,1,2544,1,12,28,1,4,1))
satSacProfileEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:satSacProfileEntry.setStatus(_A)
_SatSacProfileIndex_Type=Integer32
_SatSacProfileIndex_Object=MibTableColumn
satSacProfileIndex=_SatSacProfileIndex_Object((1,3,6,1,4,1,2544,1,12,28,1,4,1,1),_SatSacProfileIndex_Type())
satSacProfileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:satSacProfileIndex.setStatus(_A)
class _SatSacProfileAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SatSacProfileAlias_Type.__name__=_I
_SatSacProfileAlias_Object=MibTableColumn
satSacProfileAlias=_SatSacProfileAlias_Object((1,3,6,1,4,1,2544,1,12,28,1,4,1,2),_SatSacProfileAlias_Type())
satSacProfileAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:satSacProfileAlias.setStatus(_A)
_SatSacProfileFLR_Type=Integer32
_SatSacProfileFLR_Object=MibTableColumn
satSacProfileFLR=_SatSacProfileFLR_Object((1,3,6,1,4,1,2544,1,12,28,1,4,1,3),_SatSacProfileFLR_Type())
satSacProfileFLR.setMaxAccess(_C)
if mibBuilder.loadTexts:satSacProfileFLR.setStatus(_A)
_SatSacProfileFTD_Type=Unsigned32
_SatSacProfileFTD_Object=MibTableColumn
satSacProfileFTD=_SatSacProfileFTD_Object((1,3,6,1,4,1,2544,1,12,28,1,4,1,4),_SatSacProfileFTD_Type())
satSacProfileFTD.setMaxAccess(_C)
if mibBuilder.loadTexts:satSacProfileFTD.setStatus(_A)
_SatSacProfileFDV_Type=Unsigned32
_SatSacProfileFDV_Object=MibTableColumn
satSacProfileFDV=_SatSacProfileFDV_Object((1,3,6,1,4,1,2544,1,12,28,1,4,1,5),_SatSacProfileFDV_Type())
satSacProfileFDV.setMaxAccess(_C)
if mibBuilder.loadTexts:satSacProfileFDV.setStatus(_A)
_SatSacProfileStorageType_Type=StorageType
_SatSacProfileStorageType_Object=MibTableColumn
satSacProfileStorageType=_SatSacProfileStorageType_Object((1,3,6,1,4,1,2544,1,12,28,1,4,1,6),_SatSacProfileStorageType_Type())
satSacProfileStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:satSacProfileStorageType.setStatus(_A)
_SatSacProfileRowStatus_Type=RowStatus
_SatSacProfileRowStatus_Object=MibTableColumn
satSacProfileRowStatus=_SatSacProfileRowStatus_Object((1,3,6,1,4,1,2544,1,12,28,1,4,1,7),_SatSacProfileRowStatus_Type())
satSacProfileRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:satSacProfileRowStatus.setStatus(_A)
_SatResponderSessionTable_Object=MibTable
satResponderSessionTable=_SatResponderSessionTable_Object((1,3,6,1,4,1,2544,1,12,28,1,5))
if mibBuilder.loadTexts:satResponderSessionTable.setStatus(_A)
_SatResponderSessionEntry_Object=MibTableRow
satResponderSessionEntry=_SatResponderSessionEntry_Object((1,3,6,1,4,1,2544,1,12,28,1,5,1))
satResponderSessionEntry.setIndexNames((0,_G,_H),(0,_B,_P))
if mibBuilder.loadTexts:satResponderSessionEntry.setStatus(_A)
_SatResponderSessionIndex_Type=Unsigned32
_SatResponderSessionIndex_Object=MibTableColumn
satResponderSessionIndex=_SatResponderSessionIndex_Object((1,3,6,1,4,1,2544,1,12,28,1,5,1,1),_SatResponderSessionIndex_Type())
satResponderSessionIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:satResponderSessionIndex.setStatus(_A)
_SatResponderSessionId_Type=Unsigned32
_SatResponderSessionId_Object=MibTableColumn
satResponderSessionId=_SatResponderSessionId_Object((1,3,6,1,4,1,2544,1,12,28,1,5,1,2),_SatResponderSessionId_Type())
satResponderSessionId.setMaxAccess(_D)
if mibBuilder.loadTexts:satResponderSessionId.setStatus(_A)
_SatResponderSessionControlMepMacAddr_Type=MacAddress
_SatResponderSessionControlMepMacAddr_Object=MibTableColumn
satResponderSessionControlMepMacAddr=_SatResponderSessionControlMepMacAddr_Object((1,3,6,1,4,1,2544,1,12,28,1,5,1,3),_SatResponderSessionControlMepMacAddr_Type())
satResponderSessionControlMepMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:satResponderSessionControlMepMacAddr.setStatus(_A)
_SatResponderSessionMepId_Type=VariablePointer
_SatResponderSessionMepId_Object=MibTableColumn
satResponderSessionMepId=_SatResponderSessionMepId_Object((1,3,6,1,4,1,2544,1,12,28,1,5,1,4),_SatResponderSessionMepId_Type())
satResponderSessionMepId.setMaxAccess(_D)
if mibBuilder.loadTexts:satResponderSessionMepId.setStatus(_A)
_SatResponderSessionStorageType_Type=StorageType
_SatResponderSessionStorageType_Object=MibTableColumn
satResponderSessionStorageType=_SatResponderSessionStorageType_Object((1,3,6,1,4,1,2544,1,12,28,1,5,1,5),_SatResponderSessionStorageType_Type())
satResponderSessionStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:satResponderSessionStorageType.setStatus(_A)
_SatResponderSessionRowStatus_Type=RowStatus
_SatResponderSessionRowStatus_Object=MibTableColumn
satResponderSessionRowStatus=_SatResponderSessionRowStatus_Object((1,3,6,1,4,1,2544,1,12,28,1,5,1,6),_SatResponderSessionRowStatus_Type())
satResponderSessionRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:satResponderSessionRowStatus.setStatus(_A)
_NetworkElementSatParamsTable_Object=MibTable
networkElementSatParamsTable=_NetworkElementSatParamsTable_Object((1,3,6,1,4,1,2544,1,12,28,1,6))
if mibBuilder.loadTexts:networkElementSatParamsTable.setStatus(_A)
_NetworkElementSatParamsEntry_Object=MibTableRow
networkElementSatParamsEntry=_NetworkElementSatParamsEntry_Object((1,3,6,1,4,1,2544,1,12,28,1,6,1))
if mibBuilder.loadTexts:networkElementSatParamsEntry.setStatus(_A)
_NeSatParamsEtherType_Type=Unsigned32
_NeSatParamsEtherType_Object=MibTableColumn
neSatParamsEtherType=_NeSatParamsEtherType_Object((1,3,6,1,4,1,2544,1,12,28,1,6,1,1),_NeSatParamsEtherType_Type())
neSatParamsEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:neSatParamsEtherType.setStatus(_A)
_SatCfmMepExtTable_Object=MibTable
satCfmMepExtTable=_SatCfmMepExtTable_Object((1,3,6,1,4,1,2544,1,12,28,1,7))
if mibBuilder.loadTexts:satCfmMepExtTable.setStatus(_A)
_SatCfmMepExtEntry_Object=MibTableRow
satCfmMepExtEntry=_SatCfmMepExtEntry_Object((1,3,6,1,4,1,2544,1,12,28,1,7,1))
if mibBuilder.loadTexts:satCfmMepExtEntry.setStatus(_A)
_SatCfmMepSatResponderEnabled_Type=TruthValue
_SatCfmMepSatResponderEnabled_Object=MibTableColumn
satCfmMepSatResponderEnabled=_SatCfmMepSatResponderEnabled_Object((1,3,6,1,4,1,2544,1,12,28,1,7,1,1),_SatCfmMepSatResponderEnabled_Type())
satCfmMepSatResponderEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:satCfmMepSatResponderEnabled.setStatus(_A)
_CmServActivationNotifications_ObjectIdentity=ObjectIdentity
cmServActivationNotifications=_CmServActivationNotifications_ObjectIdentity((1,3,6,1,4,1,2544,1,12,28,2))
_CmServActivationConformance_ObjectIdentity=ObjectIdentity
cmServActivationConformance=_CmServActivationConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,28,3))
_CmServActivationCompliances_ObjectIdentity=ObjectIdentity
cmServActivationCompliances=_CmServActivationCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,28,3,1))
_CmServActivationGroups_ObjectIdentity=ObjectIdentity
cmServActivationGroups=_CmServActivationGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,28,3,2))
networkElementEntry.registerAugmentions((_B,_V))
networkElementSatParamsEntry.setIndexNames(*networkElementEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions((_B,_W))
satCfmMepExtEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
cmSatGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,28,3,2,1))
cmSatGroup.setObjects(*((_B,_J),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_K),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_M),(_B,_N),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_O),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_P),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6)))
if mibBuilder.loadTexts:cmSatGroup.setStatus(_A)
cmServActivationCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,28,3,1,1))
cmServActivationCompliance.setObjects((_B,_B7))
if mibBuilder.loadTexts:cmServActivationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ServiceActivationTestMode':ServiceActivationTestMode,'SatProceduresType':SatProceduresType,'SatProceduresList':SatProceduresList,'SatStatus':SatStatus,'SatDirection':SatDirection,'SatFramePayloadType':SatFramePayloadType,'SatTestAction':SatTestAction,'SatResult':SatResult,'cmServiceActivationMIB':cmServiceActivationMIB,'cmServActivationObjects':cmServActivationObjects,'satControlTable':satControlTable,'satControlEntry':satControlEntry,_J:satControlIndex,_X:satControlName,_Y:satControlTestMode,_Z:satControlTestProcedures,_a:satControlConfigTestDuration,_b:satControlConfigCIRTestStepNum,_c:satControlConfigCIRTestStepDuration,_d:satControlPerfTestDuration,_e:satControlStatus,_f:satControlAction,_AQ:satControlStorageType,_AR:satControlRowStatus,_g:satControlFailCause,_h:satControlTestStartTime,_i:satControlFlpduTagOverride,'satStreamTable':satStreamTable,'satStreamEntry':satStreamEntry,_K:satStreamIndex,_j:satStreamName,_k:satStreamTestPort,_l:satStreamTestDirection,_m:satStreamDestMacAddress,_n:satStreamFramePayloadType,_o:satStreamCustomFramePayload,_p:satStreamFrameSizeList,_q:satStreamSacProfileId,_r:satStreamSrcMepId,_s:satStreamDestMepType,_t:satStreamDestMepId,_u:satStreamDestMepMacAddr,_v:satStreamDmmPacketSize,_w:satStreamDmmPacketInterval,_x:satStreamOverallResult,_y:satStreamAction,_z:satStreamStatus,_A0:satStreamCurrentTestProcedure,_A1:satStreamCurrentConfigCirTestStep,_A2:satStreamInner1VlanId,_A3:satStreamInner1VlanPri,_A4:satStreamInner1VlanEnabled,_A5:satStreamInner1ValnEtherType,_A6:satStreamInner2VlanId,_A7:satStreamInner2VlanPri,_A8:satStreamInner2VlanEnabled,_A9:satStreamInner2VlanEtherType,_AA:satStreamOuterVlanId,_AB:satStreamOuterVlanPri,_AC:satStreamOuterVlanEnabled,_AD:satStreamOuterVlanEtherType,_AE:satStreamDeiEnabled,_AF:satStreamGreenPcp,_AG:satStreamYellowPcp,_AH:satStreamColorMode,_AI:satStreamCirLo,_AJ:satStreamCirHi,_AK:satStreamEirLo,_AL:satStreamEirHi,_AM:satStreamCbs,_AN:satStreamEbs,_AO:satStreamStorageType,_AP:satStreamRowStatus,_AS:satStreamDmmPktPriority,_AT:satStreamMFactor,'satResultStatsTable':satResultStatsTable,'satResultStatsEntry':satResultStatsEntry,_M:satResultStatsTestType,_N:satResultStatsStepNumber,_AU:satResultStatsSessionId,_AV:satResultStatsStartTime,_AW:satResultStatsEndTime,_AX:satResultStatsStatus,_AY:satResultStatsResult,_AZ:satResultStatsMinIRGMeasured,_Aa:satResultStatsAvgIRGMeasured,_Ab:satResultStatsMaxIRGMeasured,_Ac:satResultStatsMinIRYMeasured,_Ad:satResultStatsAvgIRYMeasured,_Ae:satResultStatsMaxIRYMeasured,_Af:satResultStatsFlrGMeasured,_Ag:satResultStatsFlrYMeasured,_Ah:satResultStatsFlrGCounts,_Ai:satResultStatsFlrYCounts,_Aj:satResultStatsMinFTDGMeasured,_Ak:satResultStatsAvgFTDGMeasured,_Al:satResultStatsMaxFTDGMeasured,_Am:satResultStatsIMinFDVGMeasured,_An:satResultStatsIAvgFDVGMeasured,_Ao:satResultStatsIMaxFDVGMeasured,_Ap:satResultStatsISyncErrorsNum,_Aq:satResultStatsIfNegFLG,_Ar:satResultStatsIfNegFLY,_As:satResultStatsAvgIRT,_At:satResultStatsFlrTMeasured,_Au:satResultStatsFlTCounts,_Av:satResultStatsIfNegFLT,'satSacProfileTable':satSacProfileTable,'satSacProfileEntry':satSacProfileEntry,_O:satSacProfileIndex,_Aw:satSacProfileAlias,_Ax:satSacProfileFLR,_Ay:satSacProfileFTD,_Az:satSacProfileFDV,_A_:satSacProfileStorageType,_B0:satSacProfileRowStatus,'satResponderSessionTable':satResponderSessionTable,'satResponderSessionEntry':satResponderSessionEntry,_P:satResponderSessionIndex,_B1:satResponderSessionId,_B2:satResponderSessionControlMepMacAddr,_B3:satResponderSessionMepId,_B4:satResponderSessionStorageType,_B5:satResponderSessionRowStatus,'networkElementSatParamsTable':networkElementSatParamsTable,_V:networkElementSatParamsEntry,'neSatParamsEtherType':neSatParamsEtherType,'satCfmMepExtTable':satCfmMepExtTable,_W:satCfmMepExtEntry,_B6:satCfmMepSatResponderEnabled,'cmServActivationNotifications':cmServActivationNotifications,'cmServActivationConformance':cmServActivationConformance,'cmServActivationCompliances':cmServActivationCompliances,'cmServActivationCompliance':cmServActivationCompliance,'cmServActivationGroups':cmServActivationGroups,_B7:cmSatGroup})