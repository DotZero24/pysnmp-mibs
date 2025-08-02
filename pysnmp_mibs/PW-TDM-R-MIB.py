_Ag='pwTDMPerf1DayIntervalGroup'
_Af='pwTDMPerfIntervalGroup'
_Ae='pwTDMPerfCurrentGroup'
_Ad='pwTDMGroup'
_Ac='pwTDMPerf1DayIntervalFC'
_Ab='pwTDMPerf1DayIntervalUASs'
_Aa='pwTDMPerf1DayIntervalSESs'
_AZ='pwTDMPerf1DayIntervalESs'
_AY='pwTDMPerf1DayIntervalMalformedPkt'
_AX='pwTDMPerf1DayIntervalMisOrderDropped'
_AW='pwTDMPerf1DayIntervalJtrBfrUnderruns'
_AV='pwTDMPerf1DayIntervalPktsReOrder'
_AU='pwTDMPerf1DayIntervalMissingPkts'
_AT='pwTDMPerf1DayIntervalDuration'
_AS='pwTDMPerf1DayIntervalValidData'
_AR='pwTDMPerfIntervalFC'
_AQ='pwTDMPerfIntervalUASs'
_AP='pwTDMPerfIntervalSESs'
_AO='pwTDMPerfIntervalESs'
_AN='pwTDMPerfIntervalMalformedPkt'
_AM='pwTDMPerfIntervalMisOrderDropped'
_AL='pwTDMPerfIntervalJtrBfrUnderruns'
_AK='pwTDMPerfIntervalPktsReOrder'
_AJ='pwTDMPerfIntervalMissingPkts'
_AI='pwTDMPerfIntervalDuration'
_AH='pwTDMPerfIntervalValidData'
_AG='pwTDMPerfCurrentFC'
_AF='pwTDMPerfCurrentUASs'
_AE='pwTDMPerfCurrentSESs'
_AD='pwTDMPerfCurrentESs'
_AC='pwTDMPerfCurrentMalformedPkt'
_AB='pwTDMPerfCurrentMisOrderDropped'
_AA='pwTDMPerfCurrentJtrBfrUnderruns'
_A9='pwTDMPerfCurrentPktsReOrder'
_A8='pwTDMPerfCurrentMissingPkts'
_A7='pwTDMCfgConfErr'
_A6='pwTDMLatchedIndications'
_A5='pwTDMCurrentIndications'
_A4='pwTDMCfgName'
_A3='pwTDMCfgPktFiller'
_A2='pwTDMCfgStorageType'
_A1='pwTDMCfgTimestampMode'
_A0='pwTDMCfgMissingPktsToSes'
_z='pwTDMCfgClearAlarmThreshold'
_y='pwTDMCfgAlarmThreshold'
_x='pwTDMCfgExcessivePktLossThreshold'
_w='pwTDMCfgAvePktLossTimeWindow'
_v='pwTDMCfgPktReplacePolicy'
_u='pwTDMCfgSetUp2SynchTimeOut'
_t='pwTDMCfgConsecMissPktsOutSynch'
_s='pwTDMCfgConsecPktsInSynch'
_r='pwTDMCfgPayloadSuppression'
_q='pwTDMCfgJtrBfrDepth'
_p='pwTDMCfgRtpHdrUsed'
_o='pwTDMCfgPktReorder'
_n='pwTDMCfgPayloadSize'
_m='pwTDMCfgRowStatus'
_l='pwTDMCfgIndexNext'
_k='pwTDMLastEsTimeStamp'
_j='pwTDMValidDayIntervals'
_i='pwTDMValidIntervals'
_h='pwTDMTimeElapsed'
_g='pwTDMConfigError'
_f='pwRelTDMCfgIndex'
_e='pwGenTDMCfgIndex'
_d='pwTDMIfIndex'
_c='pwTDMRate'
_b='pwTDMPerf1DayIntervalNumber'
_a='pwTDMPerfIntervalNumber'
_Z='Percent'
_Y='millisecond'
_X='pwTDMCfgIndex'
_W='tdmFault'
_V='packetLoss'
_U='pktMisOrder'
_T='remotePktLoss'
_S='bufferUnderrun'
_R='bufferOverrun'
_Q='excessivePktLossRate'
_P='malformedPacket'
_O='strayPacket'
_N='TruthValue'
_M='not-accessible'
_L='deprecated'
_K='notApplicable'
_J='read-write'
_I='Bits'
_H='pwIndex'
_G='PW-STD-R-MIB'
_F='Integer32'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='PW-TDM-R-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
pwIndex,=mibBuilder.importSymbols(_G,_H)
PwCfgIndexOrzero,=mibBuilder.importSymbols('PW-TC-STD-R-MIB','PwCfgIndexOrzero')
PerfCurrentCount,PerfIntervalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_N)
pwTDMMIBR=ModuleIdentity((1,3,6,1,4,1,164,20,13))
if mibBuilder.loadTexts:pwTDMMIBR.setRevisions(('2007-02-04 00:00','2006-09-10 00:00','2006-03-01 00:00','2005-10-23 00:00','2005-07-12 00:00','2004-04-20 00:00'))
class PwTDMCfgIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RadExperimental_ObjectIdentity=ObjectIdentity
radExperimental=_RadExperimental_ObjectIdentity((1,3,6,1,4,1,164,20))
_PwTDMObjects_ObjectIdentity=ObjectIdentity
pwTDMObjects=_PwTDMObjects_ObjectIdentity((1,3,6,1,4,1,164,20,13,1))
_PwTDMTable_Object=MibTable
pwTDMTable=_PwTDMTable_Object((1,3,6,1,4,1,164,20,13,1,1))
if mibBuilder.loadTexts:pwTDMTable.setStatus(_A)
_PwTDMEntry_Object=MibTableRow
pwTDMEntry=_PwTDMEntry_Object((1,3,6,1,4,1,164,20,13,1,1,1))
pwTDMEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pwTDMEntry.setStatus(_A)
class _PwTDMRate_Type(Integer32):defaultValue=32
_PwTDMRate_Type.__name__=_F
_PwTDMRate_Object=MibTableColumn
pwTDMRate=_PwTDMRate_Object((1,3,6,1,4,1,164,20,13,1,1,1,1),_PwTDMRate_Type())
pwTDMRate.setMaxAccess(_J)
if mibBuilder.loadTexts:pwTDMRate.setStatus(_A)
_PwTDMIfIndex_Type=InterfaceIndexOrZero
_PwTDMIfIndex_Object=MibTableColumn
pwTDMIfIndex=_PwTDMIfIndex_Object((1,3,6,1,4,1,164,20,13,1,1,1,2),_PwTDMIfIndex_Type())
pwTDMIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pwTDMIfIndex.setStatus(_A)
_PwGenTDMCfgIndex_Type=PwCfgIndexOrzero
_PwGenTDMCfgIndex_Object=MibTableColumn
pwGenTDMCfgIndex=_PwGenTDMCfgIndex_Object((1,3,6,1,4,1,164,20,13,1,1,1,3),_PwGenTDMCfgIndex_Type())
pwGenTDMCfgIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pwGenTDMCfgIndex.setStatus(_A)
_PwRelTDMCfgIndex_Type=PwCfgIndexOrzero
_PwRelTDMCfgIndex_Object=MibTableColumn
pwRelTDMCfgIndex=_PwRelTDMCfgIndex_Object((1,3,6,1,4,1,164,20,13,1,1,1,4),_PwRelTDMCfgIndex_Type())
pwRelTDMCfgIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pwRelTDMCfgIndex.setStatus(_A)
class _PwTDMConfigError_Type(Bits):namedValues=NamedValues(*((_K,0),('tdmTypeIncompatible',1),('peerRtpIncompatible',2),('peerPayloadSizeIncompatible',3)))
_PwTDMConfigError_Type.__name__=_I
_PwTDMConfigError_Object=MibTableColumn
pwTDMConfigError=_PwTDMConfigError_Object((1,3,6,1,4,1,164,20,13,1,1,1,5),_PwTDMConfigError_Type())
pwTDMConfigError.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMConfigError.setStatus(_A)
class _PwTDMTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_PwTDMTimeElapsed_Type.__name__=_F
_PwTDMTimeElapsed_Object=MibTableColumn
pwTDMTimeElapsed=_PwTDMTimeElapsed_Object((1,3,6,1,4,1,164,20,13,1,1,1,6),_PwTDMTimeElapsed_Type())
pwTDMTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMTimeElapsed.setStatus(_A)
class _PwTDMValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_PwTDMValidIntervals_Type.__name__=_F
_PwTDMValidIntervals_Object=MibTableColumn
pwTDMValidIntervals=_PwTDMValidIntervals_Object((1,3,6,1,4,1,164,20,13,1,1,1,7),_PwTDMValidIntervals_Type())
pwTDMValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMValidIntervals.setStatus(_A)
class _PwTDMValidDayIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_PwTDMValidDayIntervals_Type.__name__=_F
_PwTDMValidDayIntervals_Object=MibTableColumn
pwTDMValidDayIntervals=_PwTDMValidDayIntervals_Object((1,3,6,1,4,1,164,20,13,1,1,1,8),_PwTDMValidDayIntervals_Type())
pwTDMValidDayIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMValidDayIntervals.setStatus(_A)
class _PwTDMCurrentIndications_Type(Bits):namedValues=NamedValues(*(('other',0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9)))
_PwTDMCurrentIndications_Type.__name__=_I
_PwTDMCurrentIndications_Object=MibTableColumn
pwTDMCurrentIndications=_PwTDMCurrentIndications_Object((1,3,6,1,4,1,164,20,13,1,1,1,9),_PwTDMCurrentIndications_Type())
pwTDMCurrentIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMCurrentIndications.setStatus(_L)
class _PwTDMLatchedIndications_Type(Bits):namedValues=NamedValues(*(('other',0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9)))
_PwTDMLatchedIndications_Type.__name__=_I
_PwTDMLatchedIndications_Object=MibTableColumn
pwTDMLatchedIndications=_PwTDMLatchedIndications_Object((1,3,6,1,4,1,164,20,13,1,1,1,10),_PwTDMLatchedIndications_Type())
pwTDMLatchedIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMLatchedIndications.setStatus(_L)
_PwTDMLastEsTimeStamp_Type=TimeStamp
_PwTDMLastEsTimeStamp_Object=MibTableColumn
pwTDMLastEsTimeStamp=_PwTDMLastEsTimeStamp_Object((1,3,6,1,4,1,164,20,13,1,1,1,11),_PwTDMLastEsTimeStamp_Type())
pwTDMLastEsTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMLastEsTimeStamp.setStatus(_A)
_PwTDMCfgIndexNext_Type=Unsigned32
_PwTDMCfgIndexNext_Object=MibScalar
pwTDMCfgIndexNext=_PwTDMCfgIndexNext_Object((1,3,6,1,4,1,164,20,13,1,2),_PwTDMCfgIndexNext_Type())
pwTDMCfgIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMCfgIndexNext.setStatus(_A)
_PwTDMCfgTable_Object=MibTable
pwTDMCfgTable=_PwTDMCfgTable_Object((1,3,6,1,4,1,164,20,13,1,3))
if mibBuilder.loadTexts:pwTDMCfgTable.setStatus(_A)
_PwTDMCfgEntry_Object=MibTableRow
pwTDMCfgEntry=_PwTDMCfgEntry_Object((1,3,6,1,4,1,164,20,13,1,3,1))
pwTDMCfgEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:pwTDMCfgEntry.setStatus(_A)
_PwTDMCfgIndex_Type=PwTDMCfgIndex
_PwTDMCfgIndex_Object=MibTableColumn
pwTDMCfgIndex=_PwTDMCfgIndex_Object((1,3,6,1,4,1,164,20,13,1,3,1,1),_PwTDMCfgIndex_Type())
pwTDMCfgIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:pwTDMCfgIndex.setStatus(_A)
_PwTDMCfgRowStatus_Type=RowStatus
_PwTDMCfgRowStatus_Object=MibTableColumn
pwTDMCfgRowStatus=_PwTDMCfgRowStatus_Object((1,3,6,1,4,1,164,20,13,1,3,1,2),_PwTDMCfgRowStatus_Type())
pwTDMCfgRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgRowStatus.setStatus(_A)
class _PwTDMCfgConfErr_Type(Bits):namedValues=NamedValues(*((_K,0),('payloadSize',1),('jtrBfrDepth',2)))
_PwTDMCfgConfErr_Type.__name__=_I
_PwTDMCfgConfErr_Object=MibTableColumn
pwTDMCfgConfErr=_PwTDMCfgConfErr_Object((1,3,6,1,4,1,164,20,13,1,3,1,3),_PwTDMCfgConfErr_Type())
pwTDMCfgConfErr.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMCfgConfErr.setStatus(_L)
_PwTDMCfgPayloadSize_Type=Unsigned32
_PwTDMCfgPayloadSize_Object=MibTableColumn
pwTDMCfgPayloadSize=_PwTDMCfgPayloadSize_Object((1,3,6,1,4,1,164,20,13,1,3,1,4),_PwTDMCfgPayloadSize_Type())
pwTDMCfgPayloadSize.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgPayloadSize.setStatus(_A)
_PwTDMCfgPktReorder_Type=TruthValue
_PwTDMCfgPktReorder_Object=MibTableColumn
pwTDMCfgPktReorder=_PwTDMCfgPktReorder_Object((1,3,6,1,4,1,164,20,13,1,3,1,5),_PwTDMCfgPktReorder_Type())
pwTDMCfgPktReorder.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgPktReorder.setStatus(_A)
class _PwTDMCfgRtpHdrUsed_Type(TruthValue):defaultValue=2
_PwTDMCfgRtpHdrUsed_Type.__name__=_N
_PwTDMCfgRtpHdrUsed_Object=MibTableColumn
pwTDMCfgRtpHdrUsed=_PwTDMCfgRtpHdrUsed_Object((1,3,6,1,4,1,164,20,13,1,3,1,6),_PwTDMCfgRtpHdrUsed_Type())
pwTDMCfgRtpHdrUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgRtpHdrUsed.setStatus(_A)
class _PwTDMCfgJtrBfrDepth_Type(Unsigned32):defaultValue=3000
_PwTDMCfgJtrBfrDepth_Type.__name__=_E
_PwTDMCfgJtrBfrDepth_Object=MibTableColumn
pwTDMCfgJtrBfrDepth=_PwTDMCfgJtrBfrDepth_Object((1,3,6,1,4,1,164,20,13,1,3,1,7),_PwTDMCfgJtrBfrDepth_Type())
pwTDMCfgJtrBfrDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgJtrBfrDepth.setStatus(_A)
if mibBuilder.loadTexts:pwTDMCfgJtrBfrDepth.setUnits('microsecond')
class _PwTDMCfgPayloadSuppression_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_PwTDMCfgPayloadSuppression_Type.__name__=_F
_PwTDMCfgPayloadSuppression_Object=MibTableColumn
pwTDMCfgPayloadSuppression=_PwTDMCfgPayloadSuppression_Object((1,3,6,1,4,1,164,20,13,1,3,1,8),_PwTDMCfgPayloadSuppression_Type())
pwTDMCfgPayloadSuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgPayloadSuppression.setStatus(_A)
class _PwTDMCfgConsecPktsInSynch_Type(Unsigned32):defaultValue=2
_PwTDMCfgConsecPktsInSynch_Type.__name__=_E
_PwTDMCfgConsecPktsInSynch_Object=MibTableColumn
pwTDMCfgConsecPktsInSynch=_PwTDMCfgConsecPktsInSynch_Object((1,3,6,1,4,1,164,20,13,1,3,1,9),_PwTDMCfgConsecPktsInSynch_Type())
pwTDMCfgConsecPktsInSynch.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgConsecPktsInSynch.setStatus(_A)
class _PwTDMCfgConsecMissPktsOutSynch_Type(Unsigned32):defaultValue=10
_PwTDMCfgConsecMissPktsOutSynch_Type.__name__=_E
_PwTDMCfgConsecMissPktsOutSynch_Object=MibTableColumn
pwTDMCfgConsecMissPktsOutSynch=_PwTDMCfgConsecMissPktsOutSynch_Object((1,3,6,1,4,1,164,20,13,1,3,1,10),_PwTDMCfgConsecMissPktsOutSynch_Type())
pwTDMCfgConsecMissPktsOutSynch.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgConsecMissPktsOutSynch.setStatus(_A)
class _PwTDMCfgSetUp2SynchTimeOut_Type(Unsigned32):defaultValue=5000
_PwTDMCfgSetUp2SynchTimeOut_Type.__name__=_E
_PwTDMCfgSetUp2SynchTimeOut_Object=MibTableColumn
pwTDMCfgSetUp2SynchTimeOut=_PwTDMCfgSetUp2SynchTimeOut_Object((1,3,6,1,4,1,164,20,13,1,3,1,11),_PwTDMCfgSetUp2SynchTimeOut_Type())
pwTDMCfgSetUp2SynchTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgSetUp2SynchTimeOut.setStatus(_A)
if mibBuilder.loadTexts:pwTDMCfgSetUp2SynchTimeOut.setUnits(_Y)
class _PwTDMCfgPktReplacePolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allOnes',1),('implementationSpecific',2),('filler',3)))
_PwTDMCfgPktReplacePolicy_Type.__name__=_F
_PwTDMCfgPktReplacePolicy_Object=MibTableColumn
pwTDMCfgPktReplacePolicy=_PwTDMCfgPktReplacePolicy_Object((1,3,6,1,4,1,164,20,13,1,3,1,12),_PwTDMCfgPktReplacePolicy_Type())
pwTDMCfgPktReplacePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgPktReplacePolicy.setStatus(_A)
_PwTDMCfgAvePktLossTimeWindow_Type=Integer32
_PwTDMCfgAvePktLossTimeWindow_Object=MibTableColumn
pwTDMCfgAvePktLossTimeWindow=_PwTDMCfgAvePktLossTimeWindow_Object((1,3,6,1,4,1,164,20,13,1,3,1,13),_PwTDMCfgAvePktLossTimeWindow_Type())
pwTDMCfgAvePktLossTimeWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgAvePktLossTimeWindow.setStatus(_A)
if mibBuilder.loadTexts:pwTDMCfgAvePktLossTimeWindow.setUnits(_Y)
_PwTDMCfgExcessivePktLossThreshold_Type=Unsigned32
_PwTDMCfgExcessivePktLossThreshold_Object=MibTableColumn
pwTDMCfgExcessivePktLossThreshold=_PwTDMCfgExcessivePktLossThreshold_Object((1,3,6,1,4,1,164,20,13,1,3,1,14),_PwTDMCfgExcessivePktLossThreshold_Type())
pwTDMCfgExcessivePktLossThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgExcessivePktLossThreshold.setStatus(_A)
if mibBuilder.loadTexts:pwTDMCfgExcessivePktLossThreshold.setUnits(_Z)
class _PwTDMCfgAlarmThreshold_Type(Unsigned32):defaultValue=2500
_PwTDMCfgAlarmThreshold_Type.__name__=_E
_PwTDMCfgAlarmThreshold_Object=MibTableColumn
pwTDMCfgAlarmThreshold=_PwTDMCfgAlarmThreshold_Object((1,3,6,1,4,1,164,20,13,1,3,1,15),_PwTDMCfgAlarmThreshold_Type())
pwTDMCfgAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgAlarmThreshold.setStatus(_A)
class _PwTDMCfgClearAlarmThreshold_Type(Unsigned32):defaultValue=10000
_PwTDMCfgClearAlarmThreshold_Type.__name__=_E
_PwTDMCfgClearAlarmThreshold_Object=MibTableColumn
pwTDMCfgClearAlarmThreshold=_PwTDMCfgClearAlarmThreshold_Object((1,3,6,1,4,1,164,20,13,1,3,1,16),_PwTDMCfgClearAlarmThreshold_Type())
pwTDMCfgClearAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgClearAlarmThreshold.setStatus(_A)
class _PwTDMCfgMissingPktsToSes_Type(Unsigned32):defaultValue=30
_PwTDMCfgMissingPktsToSes_Type.__name__=_E
_PwTDMCfgMissingPktsToSes_Object=MibTableColumn
pwTDMCfgMissingPktsToSes=_PwTDMCfgMissingPktsToSes_Object((1,3,6,1,4,1,164,20,13,1,3,1,17),_PwTDMCfgMissingPktsToSes_Type())
pwTDMCfgMissingPktsToSes.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgMissingPktsToSes.setStatus(_A)
if mibBuilder.loadTexts:pwTDMCfgMissingPktsToSes.setUnits(_Z)
class _PwTDMCfgTimestampMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('absolute',2),('differential',3)))
_PwTDMCfgTimestampMode_Type.__name__=_F
_PwTDMCfgTimestampMode_Object=MibTableColumn
pwTDMCfgTimestampMode=_PwTDMCfgTimestampMode_Object((1,3,6,1,4,1,164,20,13,1,3,1,18),_PwTDMCfgTimestampMode_Type())
pwTDMCfgTimestampMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgTimestampMode.setStatus(_A)
_PwTDMCfgStorageType_Type=StorageType
_PwTDMCfgStorageType_Object=MibTableColumn
pwTDMCfgStorageType=_PwTDMCfgStorageType_Object((1,3,6,1,4,1,164,20,13,1,3,1,19),_PwTDMCfgStorageType_Type())
pwTDMCfgStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgStorageType.setStatus(_A)
class _PwTDMCfgPktFiller_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PwTDMCfgPktFiller_Type.__name__=_E
_PwTDMCfgPktFiller_Object=MibTableColumn
pwTDMCfgPktFiller=_PwTDMCfgPktFiller_Object((1,3,6,1,4,1,164,20,13,1,3,1,20),_PwTDMCfgPktFiller_Type())
pwTDMCfgPktFiller.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgPktFiller.setStatus(_A)
_PwTDMCfgName_Type=SnmpAdminString
_PwTDMCfgName_Object=MibTableColumn
pwTDMCfgName=_PwTDMCfgName_Object((1,3,6,1,4,1,164,20,13,1,3,1,21),_PwTDMCfgName_Type())
pwTDMCfgName.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTDMCfgName.setStatus(_A)
_PwTDMPerfCurrentTable_Object=MibTable
pwTDMPerfCurrentTable=_PwTDMPerfCurrentTable_Object((1,3,6,1,4,1,164,20,13,1,5))
if mibBuilder.loadTexts:pwTDMPerfCurrentTable.setStatus(_A)
_PwTDMPerfCurrentEntry_Object=MibTableRow
pwTDMPerfCurrentEntry=_PwTDMPerfCurrentEntry_Object((1,3,6,1,4,1,164,20,13,1,5,1))
pwTDMPerfCurrentEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pwTDMPerfCurrentEntry.setStatus(_A)
_PwTDMPerfCurrentMissingPkts_Type=PerfCurrentCount
_PwTDMPerfCurrentMissingPkts_Object=MibTableColumn
pwTDMPerfCurrentMissingPkts=_PwTDMPerfCurrentMissingPkts_Object((1,3,6,1,4,1,164,20,13,1,5,1,1),_PwTDMPerfCurrentMissingPkts_Type())
pwTDMPerfCurrentMissingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfCurrentMissingPkts.setStatus(_A)
_PwTDMPerfCurrentPktsReOrder_Type=PerfCurrentCount
_PwTDMPerfCurrentPktsReOrder_Object=MibTableColumn
pwTDMPerfCurrentPktsReOrder=_PwTDMPerfCurrentPktsReOrder_Object((1,3,6,1,4,1,164,20,13,1,5,1,2),_PwTDMPerfCurrentPktsReOrder_Type())
pwTDMPerfCurrentPktsReOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfCurrentPktsReOrder.setStatus(_A)
_PwTDMPerfCurrentJtrBfrUnderruns_Type=PerfCurrentCount
_PwTDMPerfCurrentJtrBfrUnderruns_Object=MibTableColumn
pwTDMPerfCurrentJtrBfrUnderruns=_PwTDMPerfCurrentJtrBfrUnderruns_Object((1,3,6,1,4,1,164,20,13,1,5,1,3),_PwTDMPerfCurrentJtrBfrUnderruns_Type())
pwTDMPerfCurrentJtrBfrUnderruns.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfCurrentJtrBfrUnderruns.setStatus(_A)
_PwTDMPerfCurrentMisOrderDropped_Type=PerfCurrentCount
_PwTDMPerfCurrentMisOrderDropped_Object=MibTableColumn
pwTDMPerfCurrentMisOrderDropped=_PwTDMPerfCurrentMisOrderDropped_Object((1,3,6,1,4,1,164,20,13,1,5,1,4),_PwTDMPerfCurrentMisOrderDropped_Type())
pwTDMPerfCurrentMisOrderDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfCurrentMisOrderDropped.setStatus(_A)
_PwTDMPerfCurrentMalformedPkt_Type=PerfCurrentCount
_PwTDMPerfCurrentMalformedPkt_Object=MibTableColumn
pwTDMPerfCurrentMalformedPkt=_PwTDMPerfCurrentMalformedPkt_Object((1,3,6,1,4,1,164,20,13,1,5,1,5),_PwTDMPerfCurrentMalformedPkt_Type())
pwTDMPerfCurrentMalformedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfCurrentMalformedPkt.setStatus(_A)
_PwTDMPerfCurrentESs_Type=PerfCurrentCount
_PwTDMPerfCurrentESs_Object=MibTableColumn
pwTDMPerfCurrentESs=_PwTDMPerfCurrentESs_Object((1,3,6,1,4,1,164,20,13,1,5,1,6),_PwTDMPerfCurrentESs_Type())
pwTDMPerfCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfCurrentESs.setStatus(_A)
_PwTDMPerfCurrentSESs_Type=PerfCurrentCount
_PwTDMPerfCurrentSESs_Object=MibTableColumn
pwTDMPerfCurrentSESs=_PwTDMPerfCurrentSESs_Object((1,3,6,1,4,1,164,20,13,1,5,1,7),_PwTDMPerfCurrentSESs_Type())
pwTDMPerfCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfCurrentSESs.setStatus(_A)
_PwTDMPerfCurrentUASs_Type=PerfCurrentCount
_PwTDMPerfCurrentUASs_Object=MibTableColumn
pwTDMPerfCurrentUASs=_PwTDMPerfCurrentUASs_Object((1,3,6,1,4,1,164,20,13,1,5,1,8),_PwTDMPerfCurrentUASs_Type())
pwTDMPerfCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfCurrentUASs.setStatus(_A)
_PwTDMPerfCurrentFC_Type=PerfCurrentCount
_PwTDMPerfCurrentFC_Object=MibTableColumn
pwTDMPerfCurrentFC=_PwTDMPerfCurrentFC_Object((1,3,6,1,4,1,164,20,13,1,5,1,9),_PwTDMPerfCurrentFC_Type())
pwTDMPerfCurrentFC.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfCurrentFC.setStatus(_A)
_PwTDMPerfIntervalTable_Object=MibTable
pwTDMPerfIntervalTable=_PwTDMPerfIntervalTable_Object((1,3,6,1,4,1,164,20,13,1,6))
if mibBuilder.loadTexts:pwTDMPerfIntervalTable.setStatus(_A)
_PwTDMPerfIntervalEntry_Object=MibTableRow
pwTDMPerfIntervalEntry=_PwTDMPerfIntervalEntry_Object((1,3,6,1,4,1,164,20,13,1,6,1))
pwTDMPerfIntervalEntry.setIndexNames((0,_G,_H),(0,_B,_a))
if mibBuilder.loadTexts:pwTDMPerfIntervalEntry.setStatus(_A)
_PwTDMPerfIntervalNumber_Type=Unsigned32
_PwTDMPerfIntervalNumber_Object=MibTableColumn
pwTDMPerfIntervalNumber=_PwTDMPerfIntervalNumber_Object((1,3,6,1,4,1,164,20,13,1,6,1,1),_PwTDMPerfIntervalNumber_Type())
pwTDMPerfIntervalNumber.setMaxAccess(_M)
if mibBuilder.loadTexts:pwTDMPerfIntervalNumber.setStatus(_A)
_PwTDMPerfIntervalValidData_Type=TruthValue
_PwTDMPerfIntervalValidData_Object=MibTableColumn
pwTDMPerfIntervalValidData=_PwTDMPerfIntervalValidData_Object((1,3,6,1,4,1,164,20,13,1,6,1,2),_PwTDMPerfIntervalValidData_Type())
pwTDMPerfIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalValidData.setStatus(_A)
_PwTDMPerfIntervalDuration_Type=Unsigned32
_PwTDMPerfIntervalDuration_Object=MibTableColumn
pwTDMPerfIntervalDuration=_PwTDMPerfIntervalDuration_Object((1,3,6,1,4,1,164,20,13,1,6,1,3),_PwTDMPerfIntervalDuration_Type())
pwTDMPerfIntervalDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalDuration.setStatus(_A)
_PwTDMPerfIntervalMissingPkts_Type=PerfIntervalCount
_PwTDMPerfIntervalMissingPkts_Object=MibTableColumn
pwTDMPerfIntervalMissingPkts=_PwTDMPerfIntervalMissingPkts_Object((1,3,6,1,4,1,164,20,13,1,6,1,4),_PwTDMPerfIntervalMissingPkts_Type())
pwTDMPerfIntervalMissingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalMissingPkts.setStatus(_A)
_PwTDMPerfIntervalPktsReOrder_Type=PerfIntervalCount
_PwTDMPerfIntervalPktsReOrder_Object=MibTableColumn
pwTDMPerfIntervalPktsReOrder=_PwTDMPerfIntervalPktsReOrder_Object((1,3,6,1,4,1,164,20,13,1,6,1,5),_PwTDMPerfIntervalPktsReOrder_Type())
pwTDMPerfIntervalPktsReOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalPktsReOrder.setStatus(_A)
_PwTDMPerfIntervalJtrBfrUnderruns_Type=PerfIntervalCount
_PwTDMPerfIntervalJtrBfrUnderruns_Object=MibTableColumn
pwTDMPerfIntervalJtrBfrUnderruns=_PwTDMPerfIntervalJtrBfrUnderruns_Object((1,3,6,1,4,1,164,20,13,1,6,1,6),_PwTDMPerfIntervalJtrBfrUnderruns_Type())
pwTDMPerfIntervalJtrBfrUnderruns.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalJtrBfrUnderruns.setStatus(_A)
_PwTDMPerfIntervalMisOrderDropped_Type=PerfIntervalCount
_PwTDMPerfIntervalMisOrderDropped_Object=MibTableColumn
pwTDMPerfIntervalMisOrderDropped=_PwTDMPerfIntervalMisOrderDropped_Object((1,3,6,1,4,1,164,20,13,1,6,1,7),_PwTDMPerfIntervalMisOrderDropped_Type())
pwTDMPerfIntervalMisOrderDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalMisOrderDropped.setStatus(_A)
_PwTDMPerfIntervalMalformedPkt_Type=PerfIntervalCount
_PwTDMPerfIntervalMalformedPkt_Object=MibTableColumn
pwTDMPerfIntervalMalformedPkt=_PwTDMPerfIntervalMalformedPkt_Object((1,3,6,1,4,1,164,20,13,1,6,1,8),_PwTDMPerfIntervalMalformedPkt_Type())
pwTDMPerfIntervalMalformedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalMalformedPkt.setStatus(_A)
_PwTDMPerfIntervalESs_Type=PerfIntervalCount
_PwTDMPerfIntervalESs_Object=MibTableColumn
pwTDMPerfIntervalESs=_PwTDMPerfIntervalESs_Object((1,3,6,1,4,1,164,20,13,1,6,1,9),_PwTDMPerfIntervalESs_Type())
pwTDMPerfIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalESs.setStatus(_A)
_PwTDMPerfIntervalSESs_Type=PerfIntervalCount
_PwTDMPerfIntervalSESs_Object=MibTableColumn
pwTDMPerfIntervalSESs=_PwTDMPerfIntervalSESs_Object((1,3,6,1,4,1,164,20,13,1,6,1,10),_PwTDMPerfIntervalSESs_Type())
pwTDMPerfIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalSESs.setStatus(_A)
_PwTDMPerfIntervalUASs_Type=PerfIntervalCount
_PwTDMPerfIntervalUASs_Object=MibTableColumn
pwTDMPerfIntervalUASs=_PwTDMPerfIntervalUASs_Object((1,3,6,1,4,1,164,20,13,1,6,1,11),_PwTDMPerfIntervalUASs_Type())
pwTDMPerfIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalUASs.setStatus(_A)
_PwTDMPerfIntervalFC_Type=PerfIntervalCount
_PwTDMPerfIntervalFC_Object=MibTableColumn
pwTDMPerfIntervalFC=_PwTDMPerfIntervalFC_Object((1,3,6,1,4,1,164,20,13,1,6,1,12),_PwTDMPerfIntervalFC_Type())
pwTDMPerfIntervalFC.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerfIntervalFC.setStatus(_A)
_PwTDMPerf1DayIntervalTable_Object=MibTable
pwTDMPerf1DayIntervalTable=_PwTDMPerf1DayIntervalTable_Object((1,3,6,1,4,1,164,20,13,1,7))
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalTable.setStatus(_A)
_PwTDMPerf1DayIntervalEntry_Object=MibTableRow
pwTDMPerf1DayIntervalEntry=_PwTDMPerf1DayIntervalEntry_Object((1,3,6,1,4,1,164,20,13,1,7,1))
pwTDMPerf1DayIntervalEntry.setIndexNames((0,_G,_H),(0,_B,_b))
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalEntry.setStatus(_A)
_PwTDMPerf1DayIntervalNumber_Type=Unsigned32
_PwTDMPerf1DayIntervalNumber_Object=MibTableColumn
pwTDMPerf1DayIntervalNumber=_PwTDMPerf1DayIntervalNumber_Object((1,3,6,1,4,1,164,20,13,1,7,1,1),_PwTDMPerf1DayIntervalNumber_Type())
pwTDMPerf1DayIntervalNumber.setMaxAccess(_M)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalNumber.setStatus(_A)
_PwTDMPerf1DayIntervalValidData_Type=TruthValue
_PwTDMPerf1DayIntervalValidData_Object=MibTableColumn
pwTDMPerf1DayIntervalValidData=_PwTDMPerf1DayIntervalValidData_Object((1,3,6,1,4,1,164,20,13,1,7,1,2),_PwTDMPerf1DayIntervalValidData_Type())
pwTDMPerf1DayIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalValidData.setStatus(_A)
_PwTDMPerf1DayIntervalDuration_Type=Unsigned32
_PwTDMPerf1DayIntervalDuration_Object=MibTableColumn
pwTDMPerf1DayIntervalDuration=_PwTDMPerf1DayIntervalDuration_Object((1,3,6,1,4,1,164,20,13,1,7,1,3),_PwTDMPerf1DayIntervalDuration_Type())
pwTDMPerf1DayIntervalDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalDuration.setStatus(_A)
_PwTDMPerf1DayIntervalMissingPkts_Type=Counter32
_PwTDMPerf1DayIntervalMissingPkts_Object=MibTableColumn
pwTDMPerf1DayIntervalMissingPkts=_PwTDMPerf1DayIntervalMissingPkts_Object((1,3,6,1,4,1,164,20,13,1,7,1,4),_PwTDMPerf1DayIntervalMissingPkts_Type())
pwTDMPerf1DayIntervalMissingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalMissingPkts.setStatus(_A)
_PwTDMPerf1DayIntervalPktsReOrder_Type=Counter32
_PwTDMPerf1DayIntervalPktsReOrder_Object=MibTableColumn
pwTDMPerf1DayIntervalPktsReOrder=_PwTDMPerf1DayIntervalPktsReOrder_Object((1,3,6,1,4,1,164,20,13,1,7,1,5),_PwTDMPerf1DayIntervalPktsReOrder_Type())
pwTDMPerf1DayIntervalPktsReOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalPktsReOrder.setStatus(_A)
_PwTDMPerf1DayIntervalJtrBfrUnderruns_Type=Counter32
_PwTDMPerf1DayIntervalJtrBfrUnderruns_Object=MibTableColumn
pwTDMPerf1DayIntervalJtrBfrUnderruns=_PwTDMPerf1DayIntervalJtrBfrUnderruns_Object((1,3,6,1,4,1,164,20,13,1,7,1,6),_PwTDMPerf1DayIntervalJtrBfrUnderruns_Type())
pwTDMPerf1DayIntervalJtrBfrUnderruns.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalJtrBfrUnderruns.setStatus(_A)
_PwTDMPerf1DayIntervalMisOrderDropped_Type=Counter32
_PwTDMPerf1DayIntervalMisOrderDropped_Object=MibTableColumn
pwTDMPerf1DayIntervalMisOrderDropped=_PwTDMPerf1DayIntervalMisOrderDropped_Object((1,3,6,1,4,1,164,20,13,1,7,1,7),_PwTDMPerf1DayIntervalMisOrderDropped_Type())
pwTDMPerf1DayIntervalMisOrderDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalMisOrderDropped.setStatus(_A)
_PwTDMPerf1DayIntervalMalformedPkt_Type=Counter32
_PwTDMPerf1DayIntervalMalformedPkt_Object=MibTableColumn
pwTDMPerf1DayIntervalMalformedPkt=_PwTDMPerf1DayIntervalMalformedPkt_Object((1,3,6,1,4,1,164,20,13,1,7,1,8),_PwTDMPerf1DayIntervalMalformedPkt_Type())
pwTDMPerf1DayIntervalMalformedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalMalformedPkt.setStatus(_A)
_PwTDMPerf1DayIntervalESs_Type=Counter32
_PwTDMPerf1DayIntervalESs_Object=MibTableColumn
pwTDMPerf1DayIntervalESs=_PwTDMPerf1DayIntervalESs_Object((1,3,6,1,4,1,164,20,13,1,7,1,9),_PwTDMPerf1DayIntervalESs_Type())
pwTDMPerf1DayIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalESs.setStatus(_A)
_PwTDMPerf1DayIntervalSESs_Type=Counter32
_PwTDMPerf1DayIntervalSESs_Object=MibTableColumn
pwTDMPerf1DayIntervalSESs=_PwTDMPerf1DayIntervalSESs_Object((1,3,6,1,4,1,164,20,13,1,7,1,10),_PwTDMPerf1DayIntervalSESs_Type())
pwTDMPerf1DayIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalSESs.setStatus(_A)
_PwTDMPerf1DayIntervalUASs_Type=Counter32
_PwTDMPerf1DayIntervalUASs_Object=MibTableColumn
pwTDMPerf1DayIntervalUASs=_PwTDMPerf1DayIntervalUASs_Object((1,3,6,1,4,1,164,20,13,1,7,1,11),_PwTDMPerf1DayIntervalUASs_Type())
pwTDMPerf1DayIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalUASs.setStatus(_A)
_PwTDMPerf1DayIntervalFC_Type=Counter32
_PwTDMPerf1DayIntervalFC_Object=MibTableColumn
pwTDMPerf1DayIntervalFC=_PwTDMPerf1DayIntervalFC_Object((1,3,6,1,4,1,164,20,13,1,7,1,12),_PwTDMPerf1DayIntervalFC_Type())
pwTDMPerf1DayIntervalFC.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalFC.setStatus(_A)
_PwTDMNotifications_ObjectIdentity=ObjectIdentity
pwTDMNotifications=_PwTDMNotifications_ObjectIdentity((1,3,6,1,4,1,164,20,13,2))
_PwTDMConformance_ObjectIdentity=ObjectIdentity
pwTDMConformance=_PwTDMConformance_ObjectIdentity((1,3,6,1,4,1,164,20,13,3))
_PwTDMGroups_ObjectIdentity=ObjectIdentity
pwTDMGroups=_PwTDMGroups_ObjectIdentity((1,3,6,1,4,1,164,20,13,3,1))
_PwTDMCompliances_ObjectIdentity=ObjectIdentity
pwTDMCompliances=_PwTDMCompliances_ObjectIdentity((1,3,6,1,4,1,164,20,13,3,2))
pwTDMGroup=ObjectGroup((1,3,6,1,4,1,164,20,13,3,1,1))
pwTDMGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:pwTDMGroup.setStatus(_A)
pwTDMPerfCurrentGroup=ObjectGroup((1,3,6,1,4,1,164,20,13,3,1,2))
pwTDMPerfCurrentGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:pwTDMPerfCurrentGroup.setStatus(_A)
pwTDMPerfIntervalGroup=ObjectGroup((1,3,6,1,4,1,164,20,13,3,1,3))
pwTDMPerfIntervalGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:pwTDMPerfIntervalGroup.setStatus(_A)
pwTDMPerf1DayIntervalGroup=ObjectGroup((1,3,6,1,4,1,164,20,13,3,1,4))
pwTDMPerf1DayIntervalGroup.setObjects(*((_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:pwTDMPerf1DayIntervalGroup.setStatus(_A)
pwTDMModuleCompliance=ModuleCompliance((1,3,6,1,4,1,164,20,13,3,2,1))
pwTDMModuleCompliance.setObjects(*((_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:pwTDMModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PwTDMCfgIndex':PwTDMCfgIndex,'radExperimental':radExperimental,'pwTDMMIBR':pwTDMMIBR,'pwTDMObjects':pwTDMObjects,'pwTDMTable':pwTDMTable,'pwTDMEntry':pwTDMEntry,_c:pwTDMRate,_d:pwTDMIfIndex,_e:pwGenTDMCfgIndex,_f:pwRelTDMCfgIndex,_g:pwTDMConfigError,_h:pwTDMTimeElapsed,_i:pwTDMValidIntervals,_j:pwTDMValidDayIntervals,_A5:pwTDMCurrentIndications,_A6:pwTDMLatchedIndications,_k:pwTDMLastEsTimeStamp,_l:pwTDMCfgIndexNext,'pwTDMCfgTable':pwTDMCfgTable,'pwTDMCfgEntry':pwTDMCfgEntry,_X:pwTDMCfgIndex,_m:pwTDMCfgRowStatus,_A7:pwTDMCfgConfErr,_n:pwTDMCfgPayloadSize,_o:pwTDMCfgPktReorder,_p:pwTDMCfgRtpHdrUsed,_q:pwTDMCfgJtrBfrDepth,_r:pwTDMCfgPayloadSuppression,_s:pwTDMCfgConsecPktsInSynch,_t:pwTDMCfgConsecMissPktsOutSynch,_u:pwTDMCfgSetUp2SynchTimeOut,_v:pwTDMCfgPktReplacePolicy,_w:pwTDMCfgAvePktLossTimeWindow,_x:pwTDMCfgExcessivePktLossThreshold,_y:pwTDMCfgAlarmThreshold,_z:pwTDMCfgClearAlarmThreshold,_A0:pwTDMCfgMissingPktsToSes,_A1:pwTDMCfgTimestampMode,_A2:pwTDMCfgStorageType,_A3:pwTDMCfgPktFiller,_A4:pwTDMCfgName,'pwTDMPerfCurrentTable':pwTDMPerfCurrentTable,'pwTDMPerfCurrentEntry':pwTDMPerfCurrentEntry,_A8:pwTDMPerfCurrentMissingPkts,_A9:pwTDMPerfCurrentPktsReOrder,_AA:pwTDMPerfCurrentJtrBfrUnderruns,_AB:pwTDMPerfCurrentMisOrderDropped,_AC:pwTDMPerfCurrentMalformedPkt,_AD:pwTDMPerfCurrentESs,_AE:pwTDMPerfCurrentSESs,_AF:pwTDMPerfCurrentUASs,_AG:pwTDMPerfCurrentFC,'pwTDMPerfIntervalTable':pwTDMPerfIntervalTable,'pwTDMPerfIntervalEntry':pwTDMPerfIntervalEntry,_a:pwTDMPerfIntervalNumber,_AH:pwTDMPerfIntervalValidData,_AI:pwTDMPerfIntervalDuration,_AJ:pwTDMPerfIntervalMissingPkts,_AK:pwTDMPerfIntervalPktsReOrder,_AL:pwTDMPerfIntervalJtrBfrUnderruns,_AM:pwTDMPerfIntervalMisOrderDropped,_AN:pwTDMPerfIntervalMalformedPkt,_AO:pwTDMPerfIntervalESs,_AP:pwTDMPerfIntervalSESs,_AQ:pwTDMPerfIntervalUASs,_AR:pwTDMPerfIntervalFC,'pwTDMPerf1DayIntervalTable':pwTDMPerf1DayIntervalTable,'pwTDMPerf1DayIntervalEntry':pwTDMPerf1DayIntervalEntry,_b:pwTDMPerf1DayIntervalNumber,_AS:pwTDMPerf1DayIntervalValidData,_AT:pwTDMPerf1DayIntervalDuration,_AU:pwTDMPerf1DayIntervalMissingPkts,_AV:pwTDMPerf1DayIntervalPktsReOrder,_AW:pwTDMPerf1DayIntervalJtrBfrUnderruns,_AX:pwTDMPerf1DayIntervalMisOrderDropped,_AY:pwTDMPerf1DayIntervalMalformedPkt,_AZ:pwTDMPerf1DayIntervalESs,_Aa:pwTDMPerf1DayIntervalSESs,_Ab:pwTDMPerf1DayIntervalUASs,_Ac:pwTDMPerf1DayIntervalFC,'pwTDMNotifications':pwTDMNotifications,'pwTDMConformance':pwTDMConformance,'pwTDMGroups':pwTDMGroups,_Ad:pwTDMGroup,_Ae:pwTDMPerfCurrentGroup,_Af:pwTDMPerfIntervalGroup,_Ag:pwTDMPerf1DayIntervalGroup,'pwTDMCompliances':pwTDMCompliances,'pwTDMModuleCompliance':pwTDMModuleCompliance})