_AW='osEthOamLsMandatoryGroup'
_AV='osEthOamLsLastPriority'
_AU='osEthOamLsLastFarEndFlr'
_AT='osEthOamLsLastNearEndFlr'
_AS='osEthOamLsLastFarEndMsgLoss'
_AR='osEthOamLsLastNearEndMsgLoss'
_AQ='osEthOamLsLastDestMepMac'
_AP='osEthOamLsLastDestMepId'
_AO='osEthOamLsLastBurstStarted'
_AN='osEthOamLsLastTestStarted'
_AM='osEthOamLsLastNumLmrOut'
_AL='osEthOamLsLastNumLmrIn'
_AK='osEthOamLsLastNumLmmIn'
_AJ='osEthOamLsLastNumLmmOut'
_AI='osEthOamLsLastFeAvgFlr'
_AH='osEthOamLsLastFeMaxFlr'
_AG='osEthOamLsLastFeMinFlr'
_AF='osEthOamLsLastFeTotFlr'
_AE='osEthOamLsLastFeTotLostFrames'
_AD='osEthOamLsLastFeTotTxFrames'
_AC='osEthOamLsLastNeAvgFlr'
_AB='osEthOamLsLastNeMaxFlr'
_AA='osEthOamLsLastNeMinFlr'
_A9='osEthOamLsLastNeTotFlr'
_A8='osEthOamLsLastNeTotLostFrames'
_A7='osEthOamLsLastNeTotTxFrames'
_A6='osEthOamLsHistPriority'
_A5='osEthOamLsHistFarEndFlr'
_A4='osEthOamLsHistNearEndFlr'
_A3='osEthOamLsHistFarEndMsgLoss'
_A2='osEthOamLsHistNearEndMsgLoss'
_A1='osEthOamLsHistFarEndMsgReceived'
_A0='osEthOamLsHistFarEndMsgTx'
_z='osEthOamLsHistNearEndMsgReceived'
_y='osEthOamLsHistNearEndMsgTx'
_x='osEthOamLsHistDestMepMac'
_w='osEthOamLsHistDestMepId'
_v='osEthOamLsHistBurstStarted'
_u='osEthOamLsHistTestStarted'
_t='osEthOamLsHistNumLmrOut'
_s='osEthOamLsHistNumLmrIn'
_r='osEthOamLsHistNumLmmIn'
_q='osEthOamLsHistNumLmmOut'
_p='osEthOamLsHistFeAvgFlr'
_o='osEthOamLsHistFeMaxFlr'
_n='osEthOamLsHistFeMinFlr'
_m='osEthOamLsHistFeTotFlr'
_l='osEthOamLsHistFeTotLostFrames'
_k='osEthOamLsHistFeTotTxFrames'
_j='osEthOamLsHistNeAvgFlr'
_i='osEthOamLsHistNeMaxFlr'
_h='osEthOamLsHistNeMinFlr'
_g='osEthOamLsHistNeTotFlr'
_f='osEthOamLsHistNeTotLostFrames'
_e='osEthOamLsHistNeTotTxFrames'
_d='osEthOamLsConfTimeout'
_c='osEthOamLsConfHistorySize'
_b='osEthOamLsConfDestMepList'
_a='osEthOamLsConfDestMepMac'
_Z='osEthOamLsConfDestMepId'
_Y='osEthOamLsConfDestType'
_X='osEthOamLsMeasurementInterval'
_W='osEthOamLsFramePattern'
_V='osEthOamLsFrameSize'
_U='osEthOamLsPriority'
_T='osEthOamLsInterval'
_S='osEthOamLsCounterEnable'
_R='osEthOamLsEnabled'
_Q='osEthOamLsHistSampleIndex'
_P='read-create'
_O='TruthValue'
_N='OctetString'
_M='Integer32'
_L='not-accessible'
_K='osEthOamMepIdentifier'
_J='osEthOamMaIndex'
_I='osEthOamMdIndex'
_H='read-write'
_G='packets'
_F='Unsigned32'
_E='0.01%'
_D='Counter32'
_C='read-only'
_B='OA-ETH-OAM-LM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MepList,oaOptiSwitch=mibBuilder.importSymbols('OS-COMMON-TC-MIB','MepList','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_D,'Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention',_O)
osEthOamLs=ModuleIdentity((1,3,6,1,4,1,6926,2,18))
if mibBuilder.loadTexts:osEthOamLs.setRevisions(('2011-09-22 00:00','2010-08-29 00:00'))
class OsEthOamMepId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
class OsEthOamMepIdOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,8191))
_OsEthOamLsCapabilities_ObjectIdentity=ObjectIdentity
osEthOamLsCapabilities=_OsEthOamLsCapabilities_ObjectIdentity((1,3,6,1,4,1,6926,2,18,1))
_OsEthOamLsConfTable_Object=MibTable
osEthOamLsConfTable=_OsEthOamLsConfTable_Object((1,3,6,1,4,1,6926,2,18,2))
if mibBuilder.loadTexts:osEthOamLsConfTable.setStatus(_A)
_OsEthOamLsConfEntry_Object=MibTableRow
osEthOamLsConfEntry=_OsEthOamLsConfEntry_Object((1,3,6,1,4,1,6926,2,18,2,1))
osEthOamLsConfEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:osEthOamLsConfEntry.setStatus(_A)
class _OsEthOamMdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OsEthOamMdIndex_Type.__name__=_F
_OsEthOamMdIndex_Object=MibTableColumn
osEthOamMdIndex=_OsEthOamMdIndex_Object((1,3,6,1,4,1,6926,2,18,2,1,1),_OsEthOamMdIndex_Type())
osEthOamMdIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:osEthOamMdIndex.setStatus(_A)
class _OsEthOamMaIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_OsEthOamMaIndex_Type.__name__=_F
_OsEthOamMaIndex_Object=MibTableColumn
osEthOamMaIndex=_OsEthOamMaIndex_Object((1,3,6,1,4,1,6926,2,18,2,1,2),_OsEthOamMaIndex_Type())
osEthOamMaIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:osEthOamMaIndex.setStatus(_A)
_OsEthOamMepIdentifier_Type=OsEthOamMepId
_OsEthOamMepIdentifier_Object=MibTableColumn
osEthOamMepIdentifier=_OsEthOamMepIdentifier_Object((1,3,6,1,4,1,6926,2,18,2,1,3),_OsEthOamMepIdentifier_Type())
osEthOamMepIdentifier.setMaxAccess(_L)
if mibBuilder.loadTexts:osEthOamMepIdentifier.setStatus(_A)
class _OsEthOamLsEnabled_Type(TruthValue):defaultValue=1
_OsEthOamLsEnabled_Type.__name__=_O
_OsEthOamLsEnabled_Object=MibTableColumn
osEthOamLsEnabled=_OsEthOamLsEnabled_Object((1,3,6,1,4,1,6926,2,18,2,1,4),_OsEthOamLsEnabled_Type())
osEthOamLsEnabled.setMaxAccess(_P)
if mibBuilder.loadTexts:osEthOamLsEnabled.setStatus(_A)
class _OsEthOamLsCounterEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('bTimeOfDayTimestamp',0),('bMeasurementIntervalElapsedTime',1),('bInitiatedMeasurementCounter',2),('bCompleteMeasurementCounter',3),('bTransmitFrameCountForward',4),('bReceiveFrameCountForward',6),('bTransmitFrameCountBackward',7),('bReceiveFrameCountBackward',8),('bAvailabilityIndicatorForward',9),('bAvailabilityIndicatorBackward',10),('bUnavailabilityIndicatorForward',11),('bUnavailabilityIndicatorBackward',12),('bFrameLossRatioForwardMin',13),('bFrameLossRatioForwardMax',14),('bFrameLossRatioForwardAve',15),('bFrameLossRatioBackwardMin',16),('bFrameLossRatioBackwardMax',17),('bFrameLossRatioBackwardAve',18)))
_OsEthOamLsCounterEnable_Type.__name__='Bits'
_OsEthOamLsCounterEnable_Object=MibTableColumn
osEthOamLsCounterEnable=_OsEthOamLsCounterEnable_Object((1,3,6,1,4,1,6926,2,18,2,1,5),_OsEthOamLsCounterEnable_Type())
osEthOamLsCounterEnable.setMaxAccess(_P)
if mibBuilder.loadTexts:osEthOamLsCounterEnable.setStatus(_A)
class _OsEthOamLsInterval_Type(Unsigned32):defaultValue=1000
_OsEthOamLsInterval_Type.__name__=_F
_OsEthOamLsInterval_Object=MibTableColumn
osEthOamLsInterval=_OsEthOamLsInterval_Object((1,3,6,1,4,1,6926,2,18,2,1,6),_OsEthOamLsInterval_Type())
osEthOamLsInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsInterval.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsInterval.setUnits('ms')
class _OsEthOamLsPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(8,8))
_OsEthOamLsPriority_Type.__name__=_F
_OsEthOamLsPriority_Object=MibTableColumn
osEthOamLsPriority=_OsEthOamLsPriority_Object((1,3,6,1,4,1,6926,2,18,2,1,7),_OsEthOamLsPriority_Type())
osEthOamLsPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsPriority.setStatus(_A)
class _OsEthOamLsFrameSize_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9600))
_OsEthOamLsFrameSize_Type.__name__=_F
_OsEthOamLsFrameSize_Object=MibTableColumn
osEthOamLsFrameSize=_OsEthOamLsFrameSize_Object((1,3,6,1,4,1,6926,2,18,2,1,8),_OsEthOamLsFrameSize_Type())
osEthOamLsFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsFrameSize.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsFrameSize.setUnits('bytes')
class _OsEthOamLsFramePattern_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1436))
_OsEthOamLsFramePattern_Type.__name__=_N
_OsEthOamLsFramePattern_Object=MibTableColumn
osEthOamLsFramePattern=_OsEthOamLsFramePattern_Object((1,3,6,1,4,1,6926,2,18,2,1,9),_OsEthOamLsFramePattern_Type())
osEthOamLsFramePattern.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsFramePattern.setStatus(_A)
class _OsEthOamLsMeasurementInterval_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_OsEthOamLsMeasurementInterval_Type.__name__=_M
_OsEthOamLsMeasurementInterval_Object=MibTableColumn
osEthOamLsMeasurementInterval=_OsEthOamLsMeasurementInterval_Object((1,3,6,1,4,1,6926,2,18,2,1,10),_OsEthOamLsMeasurementInterval_Type())
osEthOamLsMeasurementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsMeasurementInterval.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsMeasurementInterval.setUnits('seconds')
class _OsEthOamLsConfDestType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('singleRMepId',1),('macAddress',2),('listOfRMeps',3)))
_OsEthOamLsConfDestType_Type.__name__=_M
_OsEthOamLsConfDestType_Object=MibTableColumn
osEthOamLsConfDestType=_OsEthOamLsConfDestType_Object((1,3,6,1,4,1,6926,2,18,2,1,11),_OsEthOamLsConfDestType_Type())
osEthOamLsConfDestType.setMaxAccess(_H)
if mibBuilder.loadTexts:osEthOamLsConfDestType.setStatus(_A)
_OsEthOamLsConfDestMepId_Type=OsEthOamMepIdOrZero
_OsEthOamLsConfDestMepId_Object=MibTableColumn
osEthOamLsConfDestMepId=_OsEthOamLsConfDestMepId_Object((1,3,6,1,4,1,6926,2,18,2,1,12),_OsEthOamLsConfDestMepId_Type())
osEthOamLsConfDestMepId.setMaxAccess(_H)
if mibBuilder.loadTexts:osEthOamLsConfDestMepId.setStatus(_A)
_OsEthOamLsConfDestMepMac_Type=MacAddress
_OsEthOamLsConfDestMepMac_Object=MibTableColumn
osEthOamLsConfDestMepMac=_OsEthOamLsConfDestMepMac_Object((1,3,6,1,4,1,6926,2,18,2,1,13),_OsEthOamLsConfDestMepMac_Type())
osEthOamLsConfDestMepMac.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsConfDestMepMac.setStatus(_A)
_OsEthOamLsConfDestMepList_Type=MepList
_OsEthOamLsConfDestMepList_Object=MibTableColumn
osEthOamLsConfDestMepList=_OsEthOamLsConfDestMepList_Object((1,3,6,1,4,1,6926,2,18,2,1,14),_OsEthOamLsConfDestMepList_Type())
osEthOamLsConfDestMepList.setMaxAccess(_H)
if mibBuilder.loadTexts:osEthOamLsConfDestMepList.setStatus(_A)
class _OsEthOamLsConfHistorySize_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,65535))
_OsEthOamLsConfHistorySize_Type.__name__=_F
_OsEthOamLsConfHistorySize_Object=MibTableColumn
osEthOamLsConfHistorySize=_OsEthOamLsConfHistorySize_Object((1,3,6,1,4,1,6926,2,18,2,1,15),_OsEthOamLsConfHistorySize_Type())
osEthOamLsConfHistorySize.setMaxAccess(_H)
if mibBuilder.loadTexts:osEthOamLsConfHistorySize.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsConfHistorySize.setUnits('lines')
class _OsEthOamLsConfTimeout_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_OsEthOamLsConfTimeout_Type.__name__=_F
_OsEthOamLsConfTimeout_Object=MibTableColumn
osEthOamLsConfTimeout=_OsEthOamLsConfTimeout_Object((1,3,6,1,4,1,6926,2,18,2,1,16),_OsEthOamLsConfTimeout_Type())
osEthOamLsConfTimeout.setMaxAccess(_H)
if mibBuilder.loadTexts:osEthOamLsConfTimeout.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsConfTimeout.setUnits('milliseconds')
_OsEthOamLsHistTable_Object=MibTable
osEthOamLsHistTable=_OsEthOamLsHistTable_Object((1,3,6,1,4,1,6926,2,18,3))
if mibBuilder.loadTexts:osEthOamLsHistTable.setStatus(_A)
_OsEthOamLsHistEntry_Object=MibTableRow
osEthOamLsHistEntry=_OsEthOamLsHistEntry_Object((1,3,6,1,4,1,6926,2,18,3,1))
osEthOamLsHistEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_Q))
if mibBuilder.loadTexts:osEthOamLsHistEntry.setStatus(_A)
class _OsEthOamLsHistSampleIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_OsEthOamLsHistSampleIndex_Type.__name__=_F
_OsEthOamLsHistSampleIndex_Object=MibTableColumn
osEthOamLsHistSampleIndex=_OsEthOamLsHistSampleIndex_Object((1,3,6,1,4,1,6926,2,18,3,1,1),_OsEthOamLsHistSampleIndex_Type())
osEthOamLsHistSampleIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:osEthOamLsHistSampleIndex.setStatus(_A)
class _OsEthOamLsHistNeTotTxFrames_Type(Counter32):defaultValue=0
_OsEthOamLsHistNeTotTxFrames_Type.__name__=_D
_OsEthOamLsHistNeTotTxFrames_Object=MibTableColumn
osEthOamLsHistNeTotTxFrames=_OsEthOamLsHistNeTotTxFrames_Object((1,3,6,1,4,1,6926,2,18,3,1,2),_OsEthOamLsHistNeTotTxFrames_Type())
osEthOamLsHistNeTotTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNeTotTxFrames.setStatus(_A)
class _OsEthOamLsHistNeTotLostFrames_Type(Counter32):defaultValue=0
_OsEthOamLsHistNeTotLostFrames_Type.__name__=_D
_OsEthOamLsHistNeTotLostFrames_Object=MibTableColumn
osEthOamLsHistNeTotLostFrames=_OsEthOamLsHistNeTotLostFrames_Object((1,3,6,1,4,1,6926,2,18,3,1,3),_OsEthOamLsHistNeTotLostFrames_Type())
osEthOamLsHistNeTotLostFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNeTotLostFrames.setStatus(_A)
class _OsEthOamLsHistNeTotFlr_Type(Counter32):defaultValue=0
_OsEthOamLsHistNeTotFlr_Type.__name__=_D
_OsEthOamLsHistNeTotFlr_Object=MibTableColumn
osEthOamLsHistNeTotFlr=_OsEthOamLsHistNeTotFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,4),_OsEthOamLsHistNeTotFlr_Type())
osEthOamLsHistNeTotFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNeTotFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistNeTotFlr.setUnits(_E)
class _OsEthOamLsHistNeMinFlr_Type(Counter32):defaultValue=0
_OsEthOamLsHistNeMinFlr_Type.__name__=_D
_OsEthOamLsHistNeMinFlr_Object=MibTableColumn
osEthOamLsHistNeMinFlr=_OsEthOamLsHistNeMinFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,5),_OsEthOamLsHistNeMinFlr_Type())
osEthOamLsHistNeMinFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNeMinFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistNeMinFlr.setUnits(_E)
class _OsEthOamLsHistNeMaxFlr_Type(Counter32):defaultValue=0
_OsEthOamLsHistNeMaxFlr_Type.__name__=_D
_OsEthOamLsHistNeMaxFlr_Object=MibTableColumn
osEthOamLsHistNeMaxFlr=_OsEthOamLsHistNeMaxFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,6),_OsEthOamLsHistNeMaxFlr_Type())
osEthOamLsHistNeMaxFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNeMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistNeMaxFlr.setUnits(_E)
class _OsEthOamLsHistNeAvgFlr_Type(Counter32):defaultValue=0
_OsEthOamLsHistNeAvgFlr_Type.__name__=_D
_OsEthOamLsHistNeAvgFlr_Object=MibTableColumn
osEthOamLsHistNeAvgFlr=_OsEthOamLsHistNeAvgFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,7),_OsEthOamLsHistNeAvgFlr_Type())
osEthOamLsHistNeAvgFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNeAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistNeAvgFlr.setUnits(_E)
class _OsEthOamLsHistFeTotTxFrames_Type(Counter32):defaultValue=0
_OsEthOamLsHistFeTotTxFrames_Type.__name__=_D
_OsEthOamLsHistFeTotTxFrames_Object=MibTableColumn
osEthOamLsHistFeTotTxFrames=_OsEthOamLsHistFeTotTxFrames_Object((1,3,6,1,4,1,6926,2,18,3,1,8),_OsEthOamLsHistFeTotTxFrames_Type())
osEthOamLsHistFeTotTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFeTotTxFrames.setStatus(_A)
class _OsEthOamLsHistFeTotLostFrames_Type(Counter32):defaultValue=0
_OsEthOamLsHistFeTotLostFrames_Type.__name__=_D
_OsEthOamLsHistFeTotLostFrames_Object=MibTableColumn
osEthOamLsHistFeTotLostFrames=_OsEthOamLsHistFeTotLostFrames_Object((1,3,6,1,4,1,6926,2,18,3,1,9),_OsEthOamLsHistFeTotLostFrames_Type())
osEthOamLsHistFeTotLostFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFeTotLostFrames.setStatus(_A)
class _OsEthOamLsHistFeTotFlr_Type(Counter32):defaultValue=0
_OsEthOamLsHistFeTotFlr_Type.__name__=_D
_OsEthOamLsHistFeTotFlr_Object=MibTableColumn
osEthOamLsHistFeTotFlr=_OsEthOamLsHistFeTotFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,10),_OsEthOamLsHistFeTotFlr_Type())
osEthOamLsHistFeTotFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFeTotFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistFeTotFlr.setUnits(_E)
class _OsEthOamLsHistFeMinFlr_Type(Counter32):defaultValue=0
_OsEthOamLsHistFeMinFlr_Type.__name__=_D
_OsEthOamLsHistFeMinFlr_Object=MibTableColumn
osEthOamLsHistFeMinFlr=_OsEthOamLsHistFeMinFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,11),_OsEthOamLsHistFeMinFlr_Type())
osEthOamLsHistFeMinFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFeMinFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistFeMinFlr.setUnits(_E)
class _OsEthOamLsHistFeMaxFlr_Type(Counter32):defaultValue=0
_OsEthOamLsHistFeMaxFlr_Type.__name__=_D
_OsEthOamLsHistFeMaxFlr_Object=MibTableColumn
osEthOamLsHistFeMaxFlr=_OsEthOamLsHistFeMaxFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,12),_OsEthOamLsHistFeMaxFlr_Type())
osEthOamLsHistFeMaxFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFeMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistFeMaxFlr.setUnits(_E)
class _OsEthOamLsHistFeAvgFlr_Type(Counter32):defaultValue=0
_OsEthOamLsHistFeAvgFlr_Type.__name__=_D
_OsEthOamLsHistFeAvgFlr_Object=MibTableColumn
osEthOamLsHistFeAvgFlr=_OsEthOamLsHistFeAvgFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,13),_OsEthOamLsHistFeAvgFlr_Type())
osEthOamLsHistFeAvgFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFeAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistFeAvgFlr.setUnits(_E)
class _OsEthOamLsHistNumLmmOut_Type(Counter32):defaultValue=0
_OsEthOamLsHistNumLmmOut_Type.__name__=_D
_OsEthOamLsHistNumLmmOut_Object=MibTableColumn
osEthOamLsHistNumLmmOut=_OsEthOamLsHistNumLmmOut_Object((1,3,6,1,4,1,6926,2,18,3,1,14),_OsEthOamLsHistNumLmmOut_Type())
osEthOamLsHistNumLmmOut.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNumLmmOut.setStatus(_A)
class _OsEthOamLsHistNumLmmIn_Type(Counter32):defaultValue=0
_OsEthOamLsHistNumLmmIn_Type.__name__=_D
_OsEthOamLsHistNumLmmIn_Object=MibTableColumn
osEthOamLsHistNumLmmIn=_OsEthOamLsHistNumLmmIn_Object((1,3,6,1,4,1,6926,2,18,3,1,15),_OsEthOamLsHistNumLmmIn_Type())
osEthOamLsHistNumLmmIn.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNumLmmIn.setStatus(_A)
class _OsEthOamLsHistNumLmrIn_Type(Counter32):defaultValue=0
_OsEthOamLsHistNumLmrIn_Type.__name__=_D
_OsEthOamLsHistNumLmrIn_Object=MibTableColumn
osEthOamLsHistNumLmrIn=_OsEthOamLsHistNumLmrIn_Object((1,3,6,1,4,1,6926,2,18,3,1,16),_OsEthOamLsHistNumLmrIn_Type())
osEthOamLsHistNumLmrIn.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNumLmrIn.setStatus(_A)
class _OsEthOamLsHistNumLmrOut_Type(Counter32):defaultValue=0
_OsEthOamLsHistNumLmrOut_Type.__name__=_D
_OsEthOamLsHistNumLmrOut_Object=MibTableColumn
osEthOamLsHistNumLmrOut=_OsEthOamLsHistNumLmrOut_Object((1,3,6,1,4,1,6926,2,18,3,1,17),_OsEthOamLsHistNumLmrOut_Type())
osEthOamLsHistNumLmrOut.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNumLmrOut.setStatus(_A)
_OsEthOamLsHistTestStarted_Type=DateAndTime
_OsEthOamLsHistTestStarted_Object=MibTableColumn
osEthOamLsHistTestStarted=_OsEthOamLsHistTestStarted_Object((1,3,6,1,4,1,6926,2,18,3,1,18),_OsEthOamLsHistTestStarted_Type())
osEthOamLsHistTestStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistTestStarted.setStatus(_A)
_OsEthOamLsHistBurstStarted_Type=DateAndTime
_OsEthOamLsHistBurstStarted_Object=MibTableColumn
osEthOamLsHistBurstStarted=_OsEthOamLsHistBurstStarted_Object((1,3,6,1,4,1,6926,2,18,3,1,19),_OsEthOamLsHistBurstStarted_Type())
osEthOamLsHistBurstStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistBurstStarted.setStatus(_A)
_OsEthOamLsHistDestMepId_Type=OsEthOamMepIdOrZero
_OsEthOamLsHistDestMepId_Object=MibTableColumn
osEthOamLsHistDestMepId=_OsEthOamLsHistDestMepId_Object((1,3,6,1,4,1,6926,2,18,3,1,20),_OsEthOamLsHistDestMepId_Type())
osEthOamLsHistDestMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistDestMepId.setStatus(_A)
_OsEthOamLsHistDestMepMac_Type=MacAddress
_OsEthOamLsHistDestMepMac_Object=MibTableColumn
osEthOamLsHistDestMepMac=_OsEthOamLsHistDestMepMac_Object((1,3,6,1,4,1,6926,2,18,3,1,21),_OsEthOamLsHistDestMepMac_Type())
osEthOamLsHistDestMepMac.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistDestMepMac.setStatus(_A)
_OsEthOamLsHistNearEndMsgTx_Type=Unsigned32
_OsEthOamLsHistNearEndMsgTx_Object=MibTableColumn
osEthOamLsHistNearEndMsgTx=_OsEthOamLsHistNearEndMsgTx_Object((1,3,6,1,4,1,6926,2,18,3,1,22),_OsEthOamLsHistNearEndMsgTx_Type())
osEthOamLsHistNearEndMsgTx.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNearEndMsgTx.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistNearEndMsgTx.setUnits(_G)
_OsEthOamLsHistNearEndMsgReceived_Type=Unsigned32
_OsEthOamLsHistNearEndMsgReceived_Object=MibTableColumn
osEthOamLsHistNearEndMsgReceived=_OsEthOamLsHistNearEndMsgReceived_Object((1,3,6,1,4,1,6926,2,18,3,1,23),_OsEthOamLsHistNearEndMsgReceived_Type())
osEthOamLsHistNearEndMsgReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNearEndMsgReceived.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistNearEndMsgReceived.setUnits(_G)
_OsEthOamLsHistFarEndMsgTx_Type=Unsigned32
_OsEthOamLsHistFarEndMsgTx_Object=MibTableColumn
osEthOamLsHistFarEndMsgTx=_OsEthOamLsHistFarEndMsgTx_Object((1,3,6,1,4,1,6926,2,18,3,1,24),_OsEthOamLsHistFarEndMsgTx_Type())
osEthOamLsHistFarEndMsgTx.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFarEndMsgTx.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistFarEndMsgTx.setUnits(_G)
_OsEthOamLsHistFarEndMsgReceived_Type=Unsigned32
_OsEthOamLsHistFarEndMsgReceived_Object=MibTableColumn
osEthOamLsHistFarEndMsgReceived=_OsEthOamLsHistFarEndMsgReceived_Object((1,3,6,1,4,1,6926,2,18,3,1,25),_OsEthOamLsHistFarEndMsgReceived_Type())
osEthOamLsHistFarEndMsgReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFarEndMsgReceived.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistFarEndMsgReceived.setUnits(_G)
_OsEthOamLsHistNearEndMsgLoss_Type=Unsigned32
_OsEthOamLsHistNearEndMsgLoss_Object=MibTableColumn
osEthOamLsHistNearEndMsgLoss=_OsEthOamLsHistNearEndMsgLoss_Object((1,3,6,1,4,1,6926,2,18,3,1,26),_OsEthOamLsHistNearEndMsgLoss_Type())
osEthOamLsHistNearEndMsgLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNearEndMsgLoss.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistNearEndMsgLoss.setUnits(_G)
_OsEthOamLsHistFarEndMsgLoss_Type=Unsigned32
_OsEthOamLsHistFarEndMsgLoss_Object=MibTableColumn
osEthOamLsHistFarEndMsgLoss=_OsEthOamLsHistFarEndMsgLoss_Object((1,3,6,1,4,1,6926,2,18,3,1,27),_OsEthOamLsHistFarEndMsgLoss_Type())
osEthOamLsHistFarEndMsgLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFarEndMsgLoss.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistFarEndMsgLoss.setUnits(_G)
_OsEthOamLsHistNearEndFlr_Type=Counter32
_OsEthOamLsHistNearEndFlr_Object=MibTableColumn
osEthOamLsHistNearEndFlr=_OsEthOamLsHistNearEndFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,28),_OsEthOamLsHistNearEndFlr_Type())
osEthOamLsHistNearEndFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistNearEndFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistNearEndFlr.setUnits(_E)
_OsEthOamLsHistFarEndFlr_Type=Counter32
_OsEthOamLsHistFarEndFlr_Object=MibTableColumn
osEthOamLsHistFarEndFlr=_OsEthOamLsHistFarEndFlr_Object((1,3,6,1,4,1,6926,2,18,3,1,29),_OsEthOamLsHistFarEndFlr_Type())
osEthOamLsHistFarEndFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistFarEndFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsHistFarEndFlr.setUnits(_E)
class _OsEthOamLsHistPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OsEthOamLsHistPriority_Type.__name__=_F
_OsEthOamLsHistPriority_Object=MibTableColumn
osEthOamLsHistPriority=_OsEthOamLsHistPriority_Object((1,3,6,1,4,1,6926,2,18,3,1,30),_OsEthOamLsHistPriority_Type())
osEthOamLsHistPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsHistPriority.setStatus(_A)
_OsEthOamLsLastTable_Object=MibTable
osEthOamLsLastTable=_OsEthOamLsLastTable_Object((1,3,6,1,4,1,6926,2,18,4))
if mibBuilder.loadTexts:osEthOamLsLastTable.setStatus(_A)
_OsEthOamLsLastEntry_Object=MibTableRow
osEthOamLsLastEntry=_OsEthOamLsLastEntry_Object((1,3,6,1,4,1,6926,2,18,4,1))
osEthOamLsLastEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:osEthOamLsLastEntry.setStatus(_A)
class _OsEthOamLsLastNeTotTxFrames_Type(Counter32):defaultValue=0
_OsEthOamLsLastNeTotTxFrames_Type.__name__=_D
_OsEthOamLsLastNeTotTxFrames_Object=MibTableColumn
osEthOamLsLastNeTotTxFrames=_OsEthOamLsLastNeTotTxFrames_Object((1,3,6,1,4,1,6926,2,18,4,1,1),_OsEthOamLsLastNeTotTxFrames_Type())
osEthOamLsLastNeTotTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNeTotTxFrames.setStatus(_A)
class _OsEthOamLsLastNeTotLostFrames_Type(Counter32):defaultValue=0
_OsEthOamLsLastNeTotLostFrames_Type.__name__=_D
_OsEthOamLsLastNeTotLostFrames_Object=MibTableColumn
osEthOamLsLastNeTotLostFrames=_OsEthOamLsLastNeTotLostFrames_Object((1,3,6,1,4,1,6926,2,18,4,1,2),_OsEthOamLsLastNeTotLostFrames_Type())
osEthOamLsLastNeTotLostFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNeTotLostFrames.setStatus(_A)
class _OsEthOamLsLastNeTotFlr_Type(Counter32):defaultValue=0
_OsEthOamLsLastNeTotFlr_Type.__name__=_D
_OsEthOamLsLastNeTotFlr_Object=MibTableColumn
osEthOamLsLastNeTotFlr=_OsEthOamLsLastNeTotFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,3),_OsEthOamLsLastNeTotFlr_Type())
osEthOamLsLastNeTotFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNeTotFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastNeTotFlr.setUnits(_E)
class _OsEthOamLsLastNeMinFlr_Type(Counter32):defaultValue=0
_OsEthOamLsLastNeMinFlr_Type.__name__=_D
_OsEthOamLsLastNeMinFlr_Object=MibTableColumn
osEthOamLsLastNeMinFlr=_OsEthOamLsLastNeMinFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,4),_OsEthOamLsLastNeMinFlr_Type())
osEthOamLsLastNeMinFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNeMinFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastNeMinFlr.setUnits(_E)
class _OsEthOamLsLastNeMaxFlr_Type(Counter32):defaultValue=0
_OsEthOamLsLastNeMaxFlr_Type.__name__=_D
_OsEthOamLsLastNeMaxFlr_Object=MibTableColumn
osEthOamLsLastNeMaxFlr=_OsEthOamLsLastNeMaxFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,5),_OsEthOamLsLastNeMaxFlr_Type())
osEthOamLsLastNeMaxFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNeMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastNeMaxFlr.setUnits(_E)
class _OsEthOamLsLastNeAvgFlr_Type(Counter32):defaultValue=0
_OsEthOamLsLastNeAvgFlr_Type.__name__=_D
_OsEthOamLsLastNeAvgFlr_Object=MibTableColumn
osEthOamLsLastNeAvgFlr=_OsEthOamLsLastNeAvgFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,6),_OsEthOamLsLastNeAvgFlr_Type())
osEthOamLsLastNeAvgFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNeAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastNeAvgFlr.setUnits(_E)
class _OsEthOamLsLastFeTotTxFrames_Type(Counter32):defaultValue=0
_OsEthOamLsLastFeTotTxFrames_Type.__name__=_D
_OsEthOamLsLastFeTotTxFrames_Object=MibTableColumn
osEthOamLsLastFeTotTxFrames=_OsEthOamLsLastFeTotTxFrames_Object((1,3,6,1,4,1,6926,2,18,4,1,7),_OsEthOamLsLastFeTotTxFrames_Type())
osEthOamLsLastFeTotTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastFeTotTxFrames.setStatus(_A)
class _OsEthOamLsLastFeTotLostFrames_Type(Counter32):defaultValue=0
_OsEthOamLsLastFeTotLostFrames_Type.__name__=_D
_OsEthOamLsLastFeTotLostFrames_Object=MibTableColumn
osEthOamLsLastFeTotLostFrames=_OsEthOamLsLastFeTotLostFrames_Object((1,3,6,1,4,1,6926,2,18,4,1,8),_OsEthOamLsLastFeTotLostFrames_Type())
osEthOamLsLastFeTotLostFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastFeTotLostFrames.setStatus(_A)
class _OsEthOamLsLastFeTotFlr_Type(Counter32):defaultValue=0
_OsEthOamLsLastFeTotFlr_Type.__name__=_D
_OsEthOamLsLastFeTotFlr_Object=MibTableColumn
osEthOamLsLastFeTotFlr=_OsEthOamLsLastFeTotFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,9),_OsEthOamLsLastFeTotFlr_Type())
osEthOamLsLastFeTotFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastFeTotFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastFeTotFlr.setUnits(_E)
class _OsEthOamLsLastFeMinFlr_Type(Counter32):defaultValue=0
_OsEthOamLsLastFeMinFlr_Type.__name__=_D
_OsEthOamLsLastFeMinFlr_Object=MibTableColumn
osEthOamLsLastFeMinFlr=_OsEthOamLsLastFeMinFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,10),_OsEthOamLsLastFeMinFlr_Type())
osEthOamLsLastFeMinFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastFeMinFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastFeMinFlr.setUnits(_E)
class _OsEthOamLsLastFeMaxFlr_Type(Counter32):defaultValue=0
_OsEthOamLsLastFeMaxFlr_Type.__name__=_D
_OsEthOamLsLastFeMaxFlr_Object=MibTableColumn
osEthOamLsLastFeMaxFlr=_OsEthOamLsLastFeMaxFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,11),_OsEthOamLsLastFeMaxFlr_Type())
osEthOamLsLastFeMaxFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastFeMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastFeMaxFlr.setUnits(_E)
class _OsEthOamLsLastFeAvgFlr_Type(Counter32):defaultValue=0
_OsEthOamLsLastFeAvgFlr_Type.__name__=_D
_OsEthOamLsLastFeAvgFlr_Object=MibTableColumn
osEthOamLsLastFeAvgFlr=_OsEthOamLsLastFeAvgFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,12),_OsEthOamLsLastFeAvgFlr_Type())
osEthOamLsLastFeAvgFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastFeAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastFeAvgFlr.setUnits(_E)
class _OsEthOamLsLastNumLmmOut_Type(Counter32):defaultValue=0
_OsEthOamLsLastNumLmmOut_Type.__name__=_D
_OsEthOamLsLastNumLmmOut_Object=MibTableColumn
osEthOamLsLastNumLmmOut=_OsEthOamLsLastNumLmmOut_Object((1,3,6,1,4,1,6926,2,18,4,1,13),_OsEthOamLsLastNumLmmOut_Type())
osEthOamLsLastNumLmmOut.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNumLmmOut.setStatus(_A)
class _OsEthOamLsLastNumLmmIn_Type(Counter32):defaultValue=0
_OsEthOamLsLastNumLmmIn_Type.__name__=_D
_OsEthOamLsLastNumLmmIn_Object=MibTableColumn
osEthOamLsLastNumLmmIn=_OsEthOamLsLastNumLmmIn_Object((1,3,6,1,4,1,6926,2,18,4,1,14),_OsEthOamLsLastNumLmmIn_Type())
osEthOamLsLastNumLmmIn.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNumLmmIn.setStatus(_A)
class _OsEthOamLsLastNumLmrIn_Type(Counter32):defaultValue=0
_OsEthOamLsLastNumLmrIn_Type.__name__=_D
_OsEthOamLsLastNumLmrIn_Object=MibTableColumn
osEthOamLsLastNumLmrIn=_OsEthOamLsLastNumLmrIn_Object((1,3,6,1,4,1,6926,2,18,4,1,15),_OsEthOamLsLastNumLmrIn_Type())
osEthOamLsLastNumLmrIn.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNumLmrIn.setStatus(_A)
class _OsEthOamLsLastNumLmrOut_Type(Counter32):defaultValue=0
_OsEthOamLsLastNumLmrOut_Type.__name__=_D
_OsEthOamLsLastNumLmrOut_Object=MibTableColumn
osEthOamLsLastNumLmrOut=_OsEthOamLsLastNumLmrOut_Object((1,3,6,1,4,1,6926,2,18,4,1,16),_OsEthOamLsLastNumLmrOut_Type())
osEthOamLsLastNumLmrOut.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNumLmrOut.setStatus(_A)
_OsEthOamLsLastTestStarted_Type=DateAndTime
_OsEthOamLsLastTestStarted_Object=MibTableColumn
osEthOamLsLastTestStarted=_OsEthOamLsLastTestStarted_Object((1,3,6,1,4,1,6926,2,18,4,1,17),_OsEthOamLsLastTestStarted_Type())
osEthOamLsLastTestStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastTestStarted.setStatus(_A)
_OsEthOamLsLastBurstStarted_Type=DateAndTime
_OsEthOamLsLastBurstStarted_Object=MibTableColumn
osEthOamLsLastBurstStarted=_OsEthOamLsLastBurstStarted_Object((1,3,6,1,4,1,6926,2,18,4,1,18),_OsEthOamLsLastBurstStarted_Type())
osEthOamLsLastBurstStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastBurstStarted.setStatus(_A)
_OsEthOamLsLastDestMepId_Type=OsEthOamMepIdOrZero
_OsEthOamLsLastDestMepId_Object=MibTableColumn
osEthOamLsLastDestMepId=_OsEthOamLsLastDestMepId_Object((1,3,6,1,4,1,6926,2,18,4,1,19),_OsEthOamLsLastDestMepId_Type())
osEthOamLsLastDestMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastDestMepId.setStatus(_A)
_OsEthOamLsLastDestMepMac_Type=MacAddress
_OsEthOamLsLastDestMepMac_Object=MibTableColumn
osEthOamLsLastDestMepMac=_OsEthOamLsLastDestMepMac_Object((1,3,6,1,4,1,6926,2,18,4,1,20),_OsEthOamLsLastDestMepMac_Type())
osEthOamLsLastDestMepMac.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastDestMepMac.setStatus(_A)
_OsEthOamLsLastNearEndMsgLoss_Type=Unsigned32
_OsEthOamLsLastNearEndMsgLoss_Object=MibTableColumn
osEthOamLsLastNearEndMsgLoss=_OsEthOamLsLastNearEndMsgLoss_Object((1,3,6,1,4,1,6926,2,18,4,1,21),_OsEthOamLsLastNearEndMsgLoss_Type())
osEthOamLsLastNearEndMsgLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNearEndMsgLoss.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastNearEndMsgLoss.setUnits(_G)
_OsEthOamLsLastFarEndMsgLoss_Type=Unsigned32
_OsEthOamLsLastFarEndMsgLoss_Object=MibTableColumn
osEthOamLsLastFarEndMsgLoss=_OsEthOamLsLastFarEndMsgLoss_Object((1,3,6,1,4,1,6926,2,18,4,1,22),_OsEthOamLsLastFarEndMsgLoss_Type())
osEthOamLsLastFarEndMsgLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastFarEndMsgLoss.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastFarEndMsgLoss.setUnits(_G)
_OsEthOamLsLastNearEndFlr_Type=Counter32
_OsEthOamLsLastNearEndFlr_Object=MibTableColumn
osEthOamLsLastNearEndFlr=_OsEthOamLsLastNearEndFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,23),_OsEthOamLsLastNearEndFlr_Type())
osEthOamLsLastNearEndFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastNearEndFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastNearEndFlr.setUnits(_E)
_OsEthOamLsLastFarEndFlr_Type=Counter32
_OsEthOamLsLastFarEndFlr_Object=MibTableColumn
osEthOamLsLastFarEndFlr=_OsEthOamLsLastFarEndFlr_Object((1,3,6,1,4,1,6926,2,18,4,1,24),_OsEthOamLsLastFarEndFlr_Type())
osEthOamLsLastFarEndFlr.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastFarEndFlr.setStatus(_A)
if mibBuilder.loadTexts:osEthOamLsLastFarEndFlr.setUnits(_E)
class _OsEthOamLsLastPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OsEthOamLsLastPriority_Type.__name__=_F
_OsEthOamLsLastPriority_Object=MibTableColumn
osEthOamLsLastPriority=_OsEthOamLsLastPriority_Object((1,3,6,1,4,1,6926,2,18,4,1,25),_OsEthOamLsLastPriority_Type())
osEthOamLsLastPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:osEthOamLsLastPriority.setStatus(_A)
_OsEthOamLsConformance_ObjectIdentity=ObjectIdentity
osEthOamLsConformance=_OsEthOamLsConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,18,100))
_OsEthOamLsCompliances_ObjectIdentity=ObjectIdentity
osEthOamLsCompliances=_OsEthOamLsCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,18,100,1))
_OsEthOamLsGroups_ObjectIdentity=ObjectIdentity
osEthOamLsGroups=_OsEthOamLsGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,18,100,2))
osEthOamLsMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,18,100,2,1))
osEthOamLsMandatoryGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:osEthOamLsMandatoryGroup.setStatus(_A)
nbEthOamMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,18,100,1,1))
nbEthOamMIBCompliance.setObjects((_B,_AW))
if mibBuilder.loadTexts:nbEthOamMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OsEthOamMepId':OsEthOamMepId,'OsEthOamMepIdOrZero':OsEthOamMepIdOrZero,'osEthOamLs':osEthOamLs,'osEthOamLsCapabilities':osEthOamLsCapabilities,'osEthOamLsConfTable':osEthOamLsConfTable,'osEthOamLsConfEntry':osEthOamLsConfEntry,_I:osEthOamMdIndex,_J:osEthOamMaIndex,_K:osEthOamMepIdentifier,_R:osEthOamLsEnabled,_S:osEthOamLsCounterEnable,_T:osEthOamLsInterval,_U:osEthOamLsPriority,_V:osEthOamLsFrameSize,_W:osEthOamLsFramePattern,_X:osEthOamLsMeasurementInterval,_Y:osEthOamLsConfDestType,_Z:osEthOamLsConfDestMepId,_a:osEthOamLsConfDestMepMac,_b:osEthOamLsConfDestMepList,_c:osEthOamLsConfHistorySize,_d:osEthOamLsConfTimeout,'osEthOamLsHistTable':osEthOamLsHistTable,'osEthOamLsHistEntry':osEthOamLsHistEntry,_Q:osEthOamLsHistSampleIndex,_e:osEthOamLsHistNeTotTxFrames,_f:osEthOamLsHistNeTotLostFrames,_g:osEthOamLsHistNeTotFlr,_h:osEthOamLsHistNeMinFlr,_i:osEthOamLsHistNeMaxFlr,_j:osEthOamLsHistNeAvgFlr,_k:osEthOamLsHistFeTotTxFrames,_l:osEthOamLsHistFeTotLostFrames,_m:osEthOamLsHistFeTotFlr,_n:osEthOamLsHistFeMinFlr,_o:osEthOamLsHistFeMaxFlr,_p:osEthOamLsHistFeAvgFlr,_q:osEthOamLsHistNumLmmOut,_r:osEthOamLsHistNumLmmIn,_s:osEthOamLsHistNumLmrIn,_t:osEthOamLsHistNumLmrOut,_u:osEthOamLsHistTestStarted,_v:osEthOamLsHistBurstStarted,_w:osEthOamLsHistDestMepId,_x:osEthOamLsHistDestMepMac,_y:osEthOamLsHistNearEndMsgTx,_z:osEthOamLsHistNearEndMsgReceived,_A0:osEthOamLsHistFarEndMsgTx,_A1:osEthOamLsHistFarEndMsgReceived,_A2:osEthOamLsHistNearEndMsgLoss,_A3:osEthOamLsHistFarEndMsgLoss,_A4:osEthOamLsHistNearEndFlr,_A5:osEthOamLsHistFarEndFlr,_A6:osEthOamLsHistPriority,'osEthOamLsLastTable':osEthOamLsLastTable,'osEthOamLsLastEntry':osEthOamLsLastEntry,_A7:osEthOamLsLastNeTotTxFrames,_A8:osEthOamLsLastNeTotLostFrames,_A9:osEthOamLsLastNeTotFlr,_AA:osEthOamLsLastNeMinFlr,_AB:osEthOamLsLastNeMaxFlr,_AC:osEthOamLsLastNeAvgFlr,_AD:osEthOamLsLastFeTotTxFrames,_AE:osEthOamLsLastFeTotLostFrames,_AF:osEthOamLsLastFeTotFlr,_AG:osEthOamLsLastFeMinFlr,_AH:osEthOamLsLastFeMaxFlr,_AI:osEthOamLsLastFeAvgFlr,_AJ:osEthOamLsLastNumLmmOut,_AK:osEthOamLsLastNumLmmIn,_AL:osEthOamLsLastNumLmrIn,_AM:osEthOamLsLastNumLmrOut,_AN:osEthOamLsLastTestStarted,_AO:osEthOamLsLastBurstStarted,_AP:osEthOamLsLastDestMepId,_AQ:osEthOamLsLastDestMepMac,_AR:osEthOamLsLastNearEndMsgLoss,_AS:osEthOamLsLastFarEndMsgLoss,_AT:osEthOamLsLastNearEndFlr,_AU:osEthOamLsLastFarEndFlr,_AV:osEthOamLsLastPriority,'osEthOamLsConformance':osEthOamLsConformance,'osEthOamLsCompliances':osEthOamLsCompliances,'nbEthOamMIBCompliance':nbEthOamMIBCompliance,'osEthOamLsGroups':osEthOamLsGroups,_AW:osEthOamLsMandatoryGroup})