_Af='cpwCTDMPerf1DayIntervalGroup'
_Ae='cpwCTDMPerfIntervalGroup'
_Ad='cpwCTDMPerfCurrentGroup'
_Ac='cpwCTDMGroup'
_Ab='cpwCTDMPerf1DayIntervalFC'
_Aa='cpwCTDMPerf1DayIntervalUASs'
_AZ='cpwCTDMPerf1DayIntervalSESs'
_AY='cpwCTDMPerf1DayIntervalESs'
_AX='cpwCTDMPerf1DayIntervalMalformedPkt'
_AW='cpwCTDMPerf1DayIntervalMisOrderDropped'
_AV='cpwCTDMPerf1DayIntervalJtrBfrUnderruns'
_AU='cpwCTDMPerf1DayIntervalPktsReOrder'
_AT='cpwCTDMPerf1DayIntervalMissingPkts'
_AS='cpwCTDMPerf1DayIntervalDuration'
_AR='cpwCTDMPerf1DayIntervalValidData'
_AQ='cpwCTDMPerfIntervalFC'
_AP='cpwCTDMPerfIntervalUASs'
_AO='cpwCTDMPerfIntervalSESs'
_AN='cpwCTDMPerfIntervalESs'
_AM='cpwCTDMPerfIntervalMalformedPkt'
_AL='cpwCTDMPerfIntervalMisOrderDropped'
_AK='cpwCTDMPerfIntervalJtrBfrUnderruns'
_AJ='cpwCTDMPerfIntervalPktsReOrder'
_AI='cpwCTDMPerfIntervalMissingPkts'
_AH='cpwCTDMPerfIntervalDuration'
_AG='cpwCTDMPerfIntervalValidData'
_AF='cpwCTDMPerfCurrentFC'
_AE='cpwCTDMPerfCurrentUASs'
_AD='cpwCTDMPerfCurrentSESs'
_AC='cpwCTDMPerfCurrentESs'
_AB='cpwCTDMPerfCurrentMalformedPkt'
_AA='cpwCTDMPerfCurrentMisOrderDropped'
_A9='cpwCTDMPerfCurrentJtrBfrUnderruns'
_A8='cpwCTDMPerfCurrentPktsReOrder'
_A7='cpwCTDMPerfCurrentMissingPkts'
_A6='cpwCTDMCfgStorageType'
_A5='cpwCTDMCfgTimestampMode'
_A4='cpwCTDMCfgMissingPktsToSes'
_A3='cpwCTDMCfgClearAlarmThreshold'
_A2='cpwCTDMCfgAlarmThreshold'
_A1='cpwCTDMCfgExcessivePktLossThreshold'
_A0='cpwCTDMCfgAvePktLossTimeWindow'
_z='cpwCTDMCfgPktReplacePolicy'
_y='cpwCTDMCfgSetUp2SynchTimeOut'
_x='cpwCTDMCfgConsecMissPktsOutSynch'
_w='cpwCTDMCfgConsecPktsInSynch'
_v='cpwCTDMCfgPayloadSuppression'
_u='cpwCTDMCfgJtrBfrDepth'
_t='cpwCTDMCfgRtpHdrUsed'
_s='cpwCTDMCfgPktReorder'
_r='cpwCTDMCfgPayloadSize'
_q='cpwCTDMCfgConfErr'
_p='cpwCTDMCfgRowStatus'
_o='cpwCTDMCfgIndexNext'
_n='cpwCTDMLastEsTimeStamp'
_m='cpwCTDMLatchedIndications'
_l='cpwCTDMCurrentIndications'
_k='cpwCTDMValidDayIntervals'
_j='cpwCTDMValidIntervals'
_i='cpwCTDMTimeElapsed'
_h='cpwCTDMConfigError'
_g='cpwCRelTDMCfgIndex'
_f='cpwCGenTDMCfgIndex'
_e='cpwCTDMIfIndex'
_d='cpwCTDMRate'
_c='cpwCTDMPerf1DayIntervalNumber'
_b='cpwCTDMPerfIntervalNumber'
_a='milliseconds'
_Z='millisecond'
_Y='cpwCTDMCfgIndex'
_X='tdmFault'
_W='packetLoss'
_V='pktMisOrder'
_U='remotePktLoss'
_T='bufferUnderrun'
_S='bufferOverrun'
_R='excessivePktLossRate'
_Q='malformedPacket'
_P='StorageType'
_O='not-accessible'
_N='TruthValue'
_M='other'
_L='read-write'
_K='Bits'
_J='cpwVcIndex'
_I='CISCO-IETF-PW-MIB'
_H='Integer32'
_G='Unsigned32'
_F='seconds'
_E='packets'
_D='read-create'
_C='read-only'
_B='CISCO-IETF-PW-TDM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cpwVcIndex,=mibBuilder.importSymbols(_I,_J)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
PerfCurrentCount,PerfIntervalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_P,'TextualConvention','TimeStamp',_N)
cpwCTDMMIB=ModuleIdentity((1,3,6,1,4,1,9,10,131))
if mibBuilder.loadTexts:cpwCTDMMIB.setRevisions(('2006-07-21 00:00','2006-03-01 00:00','2005-10-23 00:00','2005-07-12 00:00','2004-04-20 00:00'))
class CpwTDMCfgIndex(TextualConvention,Unsigned32):status=_A
_CpwCTDMNotifications_ObjectIdentity=ObjectIdentity
cpwCTDMNotifications=_CpwCTDMNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,131,0))
_CpwCTDMObjects_ObjectIdentity=ObjectIdentity
cpwCTDMObjects=_CpwCTDMObjects_ObjectIdentity((1,3,6,1,4,1,9,10,131,1))
_CpwCTDMTable_Object=MibTable
cpwCTDMTable=_CpwCTDMTable_Object((1,3,6,1,4,1,9,10,131,1,1))
if mibBuilder.loadTexts:cpwCTDMTable.setStatus(_A)
_CpwCTDMEntry_Object=MibTableRow
cpwCTDMEntry=_CpwCTDMEntry_Object((1,3,6,1,4,1,9,10,131,1,1,1))
cpwCTDMEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cpwCTDMEntry.setStatus(_A)
class _CpwCTDMRate_Type(Integer32):defaultValue=32
_CpwCTDMRate_Type.__name__=_H
_CpwCTDMRate_Object=MibTableColumn
cpwCTDMRate=_CpwCTDMRate_Object((1,3,6,1,4,1,9,10,131,1,1,1,1),_CpwCTDMRate_Type())
cpwCTDMRate.setMaxAccess(_L)
if mibBuilder.loadTexts:cpwCTDMRate.setStatus(_A)
_CpwCTDMIfIndex_Type=InterfaceIndexOrZero
_CpwCTDMIfIndex_Object=MibTableColumn
cpwCTDMIfIndex=_CpwCTDMIfIndex_Object((1,3,6,1,4,1,9,10,131,1,1,1,2),_CpwCTDMIfIndex_Type())
cpwCTDMIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cpwCTDMIfIndex.setStatus(_A)
_CpwCGenTDMCfgIndex_Type=CpwTDMCfgIndex
_CpwCGenTDMCfgIndex_Object=MibTableColumn
cpwCGenTDMCfgIndex=_CpwCGenTDMCfgIndex_Object((1,3,6,1,4,1,9,10,131,1,1,1,3),_CpwCGenTDMCfgIndex_Type())
cpwCGenTDMCfgIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cpwCGenTDMCfgIndex.setStatus(_A)
_CpwCRelTDMCfgIndex_Type=CpwTDMCfgIndex
_CpwCRelTDMCfgIndex_Object=MibTableColumn
cpwCRelTDMCfgIndex=_CpwCRelTDMCfgIndex_Object((1,3,6,1,4,1,9,10,131,1,1,1,4),_CpwCRelTDMCfgIndex_Type())
cpwCRelTDMCfgIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cpwCRelTDMCfgIndex.setStatus(_A)
class _CpwCTDMConfigError_Type(Bits):namedValues=NamedValues(*((_M,0),('tdmTypeIncompatible',1),('peerRtpIncompatible',2),('peerPayloadSizeIncompatible',3)))
_CpwCTDMConfigError_Type.__name__=_K
_CpwCTDMConfigError_Object=MibTableColumn
cpwCTDMConfigError=_CpwCTDMConfigError_Object((1,3,6,1,4,1,9,10,131,1,1,1,5),_CpwCTDMConfigError_Type())
cpwCTDMConfigError.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMConfigError.setStatus(_A)
class _CpwCTDMTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_CpwCTDMTimeElapsed_Type.__name__=_H
_CpwCTDMTimeElapsed_Object=MibTableColumn
cpwCTDMTimeElapsed=_CpwCTDMTimeElapsed_Object((1,3,6,1,4,1,9,10,131,1,1,1,6),_CpwCTDMTimeElapsed_Type())
cpwCTDMTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMTimeElapsed.setUnits(_F)
class _CpwCTDMValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_CpwCTDMValidIntervals_Type.__name__=_H
_CpwCTDMValidIntervals_Object=MibTableColumn
cpwCTDMValidIntervals=_CpwCTDMValidIntervals_Object((1,3,6,1,4,1,9,10,131,1,1,1,7),_CpwCTDMValidIntervals_Type())
cpwCTDMValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMValidIntervals.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMValidIntervals.setUnits('minutes')
class _CpwCTDMValidDayIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CpwCTDMValidDayIntervals_Type.__name__=_H
_CpwCTDMValidDayIntervals_Object=MibTableColumn
cpwCTDMValidDayIntervals=_CpwCTDMValidDayIntervals_Object((1,3,6,1,4,1,9,10,131,1,1,1,8),_CpwCTDMValidDayIntervals_Type())
cpwCTDMValidDayIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMValidDayIntervals.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMValidDayIntervals.setUnits('days')
class _CpwCTDMCurrentIndications_Type(Bits):namedValues=NamedValues(*((_M,0),('strayPacket',1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_CpwCTDMCurrentIndications_Type.__name__=_K
_CpwCTDMCurrentIndications_Object=MibTableColumn
cpwCTDMCurrentIndications=_CpwCTDMCurrentIndications_Object((1,3,6,1,4,1,9,10,131,1,1,1,9),_CpwCTDMCurrentIndications_Type())
cpwCTDMCurrentIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMCurrentIndications.setStatus(_A)
class _CpwCTDMLatchedIndications_Type(Bits):namedValues=NamedValues(*((_M,0),('staryPacket',1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9)))
_CpwCTDMLatchedIndications_Type.__name__=_K
_CpwCTDMLatchedIndications_Object=MibTableColumn
cpwCTDMLatchedIndications=_CpwCTDMLatchedIndications_Object((1,3,6,1,4,1,9,10,131,1,1,1,10),_CpwCTDMLatchedIndications_Type())
cpwCTDMLatchedIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMLatchedIndications.setStatus(_A)
_CpwCTDMLastEsTimeStamp_Type=TimeStamp
_CpwCTDMLastEsTimeStamp_Object=MibTableColumn
cpwCTDMLastEsTimeStamp=_CpwCTDMLastEsTimeStamp_Object((1,3,6,1,4,1,9,10,131,1,1,1,11),_CpwCTDMLastEsTimeStamp_Type())
cpwCTDMLastEsTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMLastEsTimeStamp.setStatus(_A)
_CpwCTDMCfgIndexNext_Type=Unsigned32
_CpwCTDMCfgIndexNext_Object=MibScalar
cpwCTDMCfgIndexNext=_CpwCTDMCfgIndexNext_Object((1,3,6,1,4,1,9,10,131,1,2),_CpwCTDMCfgIndexNext_Type())
cpwCTDMCfgIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMCfgIndexNext.setStatus(_A)
_CpwCTDMCfgTable_Object=MibTable
cpwCTDMCfgTable=_CpwCTDMCfgTable_Object((1,3,6,1,4,1,9,10,131,1,3))
if mibBuilder.loadTexts:cpwCTDMCfgTable.setStatus(_A)
_CpwCTDMCfgEntry_Object=MibTableRow
cpwCTDMCfgEntry=_CpwCTDMCfgEntry_Object((1,3,6,1,4,1,9,10,131,1,3,1))
cpwCTDMCfgEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:cpwCTDMCfgEntry.setStatus(_A)
_CpwCTDMCfgIndex_Type=CpwTDMCfgIndex
_CpwCTDMCfgIndex_Object=MibTableColumn
cpwCTDMCfgIndex=_CpwCTDMCfgIndex_Object((1,3,6,1,4,1,9,10,131,1,3,1,1),_CpwCTDMCfgIndex_Type())
cpwCTDMCfgIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:cpwCTDMCfgIndex.setStatus(_A)
class _CpwCTDMCfgConfErr_Type(Bits):namedValues=NamedValues(*((_M,0),('payloadSize',1),('jtrBfrDepth',2)))
_CpwCTDMCfgConfErr_Type.__name__=_K
_CpwCTDMCfgConfErr_Object=MibTableColumn
cpwCTDMCfgConfErr=_CpwCTDMCfgConfErr_Object((1,3,6,1,4,1,9,10,131,1,3,1,2),_CpwCTDMCfgConfErr_Type())
cpwCTDMCfgConfErr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMCfgConfErr.setStatus(_A)
class _CpwCTDMCfgPayloadSize_Type(Unsigned32):defaultValue=32
_CpwCTDMCfgPayloadSize_Type.__name__=_G
_CpwCTDMCfgPayloadSize_Object=MibTableColumn
cpwCTDMCfgPayloadSize=_CpwCTDMCfgPayloadSize_Object((1,3,6,1,4,1,9,10,131,1,3,1,3),_CpwCTDMCfgPayloadSize_Type())
cpwCTDMCfgPayloadSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgPayloadSize.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMCfgPayloadSize.setUnits('bytes')
class _CpwCTDMCfgPktReorder_Type(TruthValue):defaultValue=1
_CpwCTDMCfgPktReorder_Type.__name__=_N
_CpwCTDMCfgPktReorder_Object=MibTableColumn
cpwCTDMCfgPktReorder=_CpwCTDMCfgPktReorder_Object((1,3,6,1,4,1,9,10,131,1,3,1,4),_CpwCTDMCfgPktReorder_Type())
cpwCTDMCfgPktReorder.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgPktReorder.setStatus(_A)
class _CpwCTDMCfgRtpHdrUsed_Type(TruthValue):defaultValue=2
_CpwCTDMCfgRtpHdrUsed_Type.__name__=_N
_CpwCTDMCfgRtpHdrUsed_Object=MibTableColumn
cpwCTDMCfgRtpHdrUsed=_CpwCTDMCfgRtpHdrUsed_Object((1,3,6,1,4,1,9,10,131,1,3,1,5),_CpwCTDMCfgRtpHdrUsed_Type())
cpwCTDMCfgRtpHdrUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgRtpHdrUsed.setStatus(_A)
class _CpwCTDMCfgJtrBfrDepth_Type(Unsigned32):defaultValue=3000
_CpwCTDMCfgJtrBfrDepth_Type.__name__=_G
_CpwCTDMCfgJtrBfrDepth_Object=MibTableColumn
cpwCTDMCfgJtrBfrDepth=_CpwCTDMCfgJtrBfrDepth_Object((1,3,6,1,4,1,9,10,131,1,3,1,6),_CpwCTDMCfgJtrBfrDepth_Type())
cpwCTDMCfgJtrBfrDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgJtrBfrDepth.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMCfgJtrBfrDepth.setUnits('microsecond')
class _CpwCTDMCfgPayloadSuppression_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CpwCTDMCfgPayloadSuppression_Type.__name__=_H
_CpwCTDMCfgPayloadSuppression_Object=MibTableColumn
cpwCTDMCfgPayloadSuppression=_CpwCTDMCfgPayloadSuppression_Object((1,3,6,1,4,1,9,10,131,1,3,1,7),_CpwCTDMCfgPayloadSuppression_Type())
cpwCTDMCfgPayloadSuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgPayloadSuppression.setStatus(_A)
class _CpwCTDMCfgConsecPktsInSynch_Type(Unsigned32):defaultValue=2
_CpwCTDMCfgConsecPktsInSynch_Type.__name__=_G
_CpwCTDMCfgConsecPktsInSynch_Object=MibTableColumn
cpwCTDMCfgConsecPktsInSynch=_CpwCTDMCfgConsecPktsInSynch_Object((1,3,6,1,4,1,9,10,131,1,3,1,8),_CpwCTDMCfgConsecPktsInSynch_Type())
cpwCTDMCfgConsecPktsInSynch.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgConsecPktsInSynch.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMCfgConsecPktsInSynch.setUnits(_E)
class _CpwCTDMCfgConsecMissPktsOutSynch_Type(Unsigned32):defaultValue=10
_CpwCTDMCfgConsecMissPktsOutSynch_Type.__name__=_G
_CpwCTDMCfgConsecMissPktsOutSynch_Object=MibTableColumn
cpwCTDMCfgConsecMissPktsOutSynch=_CpwCTDMCfgConsecMissPktsOutSynch_Object((1,3,6,1,4,1,9,10,131,1,3,1,9),_CpwCTDMCfgConsecMissPktsOutSynch_Type())
cpwCTDMCfgConsecMissPktsOutSynch.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgConsecMissPktsOutSynch.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMCfgConsecMissPktsOutSynch.setUnits(_E)
class _CpwCTDMCfgSetUp2SynchTimeOut_Type(Unsigned32):defaultValue=5000
_CpwCTDMCfgSetUp2SynchTimeOut_Type.__name__=_G
_CpwCTDMCfgSetUp2SynchTimeOut_Object=MibTableColumn
cpwCTDMCfgSetUp2SynchTimeOut=_CpwCTDMCfgSetUp2SynchTimeOut_Object((1,3,6,1,4,1,9,10,131,1,3,1,10),_CpwCTDMCfgSetUp2SynchTimeOut_Type())
cpwCTDMCfgSetUp2SynchTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgSetUp2SynchTimeOut.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMCfgSetUp2SynchTimeOut.setUnits(_Z)
class _CpwCTDMCfgPktReplacePolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ais',1),('implementationSpecific',2)))
_CpwCTDMCfgPktReplacePolicy_Type.__name__=_H
_CpwCTDMCfgPktReplacePolicy_Object=MibTableColumn
cpwCTDMCfgPktReplacePolicy=_CpwCTDMCfgPktReplacePolicy_Object((1,3,6,1,4,1,9,10,131,1,3,1,11),_CpwCTDMCfgPktReplacePolicy_Type())
cpwCTDMCfgPktReplacePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgPktReplacePolicy.setStatus(_A)
class _CpwCTDMCfgAvePktLossTimeWindow_Type(Integer32):defaultValue=20
_CpwCTDMCfgAvePktLossTimeWindow_Type.__name__=_H
_CpwCTDMCfgAvePktLossTimeWindow_Object=MibTableColumn
cpwCTDMCfgAvePktLossTimeWindow=_CpwCTDMCfgAvePktLossTimeWindow_Object((1,3,6,1,4,1,9,10,131,1,3,1,12),_CpwCTDMCfgAvePktLossTimeWindow_Type())
cpwCTDMCfgAvePktLossTimeWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgAvePktLossTimeWindow.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMCfgAvePktLossTimeWindow.setUnits(_Z)
class _CpwCTDMCfgExcessivePktLossThreshold_Type(Unsigned32):defaultValue=2
_CpwCTDMCfgExcessivePktLossThreshold_Type.__name__=_G
_CpwCTDMCfgExcessivePktLossThreshold_Object=MibTableColumn
cpwCTDMCfgExcessivePktLossThreshold=_CpwCTDMCfgExcessivePktLossThreshold_Object((1,3,6,1,4,1,9,10,131,1,3,1,13),_CpwCTDMCfgExcessivePktLossThreshold_Type())
cpwCTDMCfgExcessivePktLossThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgExcessivePktLossThreshold.setStatus(_A)
class _CpwCTDMCfgAlarmThreshold_Type(Unsigned32):defaultValue=2500
_CpwCTDMCfgAlarmThreshold_Type.__name__=_G
_CpwCTDMCfgAlarmThreshold_Object=MibTableColumn
cpwCTDMCfgAlarmThreshold=_CpwCTDMCfgAlarmThreshold_Object((1,3,6,1,4,1,9,10,131,1,3,1,14),_CpwCTDMCfgAlarmThreshold_Type())
cpwCTDMCfgAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMCfgAlarmThreshold.setUnits(_a)
class _CpwCTDMCfgClearAlarmThreshold_Type(Unsigned32):defaultValue=10000
_CpwCTDMCfgClearAlarmThreshold_Type.__name__=_G
_CpwCTDMCfgClearAlarmThreshold_Object=MibTableColumn
cpwCTDMCfgClearAlarmThreshold=_CpwCTDMCfgClearAlarmThreshold_Object((1,3,6,1,4,1,9,10,131,1,3,1,15),_CpwCTDMCfgClearAlarmThreshold_Type())
cpwCTDMCfgClearAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgClearAlarmThreshold.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMCfgClearAlarmThreshold.setUnits(_a)
class _CpwCTDMCfgMissingPktsToSes_Type(Unsigned32):defaultValue=3
_CpwCTDMCfgMissingPktsToSes_Type.__name__=_G
_CpwCTDMCfgMissingPktsToSes_Object=MibTableColumn
cpwCTDMCfgMissingPktsToSes=_CpwCTDMCfgMissingPktsToSes_Object((1,3,6,1,4,1,9,10,131,1,3,1,16),_CpwCTDMCfgMissingPktsToSes_Type())
cpwCTDMCfgMissingPktsToSes.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgMissingPktsToSes.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMCfgMissingPktsToSes.setUnits(_F)
class _CpwCTDMCfgTimestampMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('absolute',2),('differential',3)))
_CpwCTDMCfgTimestampMode_Type.__name__=_H
_CpwCTDMCfgTimestampMode_Object=MibTableColumn
cpwCTDMCfgTimestampMode=_CpwCTDMCfgTimestampMode_Object((1,3,6,1,4,1,9,10,131,1,3,1,17),_CpwCTDMCfgTimestampMode_Type())
cpwCTDMCfgTimestampMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgTimestampMode.setStatus(_A)
class _CpwCTDMCfgStorageType_Type(StorageType):defaultValue=3
_CpwCTDMCfgStorageType_Type.__name__=_P
_CpwCTDMCfgStorageType_Object=MibTableColumn
cpwCTDMCfgStorageType=_CpwCTDMCfgStorageType_Object((1,3,6,1,4,1,9,10,131,1,3,1,18),_CpwCTDMCfgStorageType_Type())
cpwCTDMCfgStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgStorageType.setStatus(_A)
_CpwCTDMCfgRowStatus_Type=RowStatus
_CpwCTDMCfgRowStatus_Object=MibTableColumn
cpwCTDMCfgRowStatus=_CpwCTDMCfgRowStatus_Object((1,3,6,1,4,1,9,10,131,1,3,1,19),_CpwCTDMCfgRowStatus_Type())
cpwCTDMCfgRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwCTDMCfgRowStatus.setStatus(_A)
_CpwCTDMPerfCurrentTable_Object=MibTable
cpwCTDMPerfCurrentTable=_CpwCTDMPerfCurrentTable_Object((1,3,6,1,4,1,9,10,131,1,5))
if mibBuilder.loadTexts:cpwCTDMPerfCurrentTable.setStatus(_A)
_CpwCTDMPerfCurrentEntry_Object=MibTableRow
cpwCTDMPerfCurrentEntry=_CpwCTDMPerfCurrentEntry_Object((1,3,6,1,4,1,9,10,131,1,5,1))
cpwCTDMPerfCurrentEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cpwCTDMPerfCurrentEntry.setStatus(_A)
_CpwCTDMPerfCurrentMissingPkts_Type=PerfCurrentCount
_CpwCTDMPerfCurrentMissingPkts_Object=MibTableColumn
cpwCTDMPerfCurrentMissingPkts=_CpwCTDMPerfCurrentMissingPkts_Object((1,3,6,1,4,1,9,10,131,1,5,1,1),_CpwCTDMPerfCurrentMissingPkts_Type())
cpwCTDMPerfCurrentMissingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentMissingPkts.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentMissingPkts.setUnits(_E)
_CpwCTDMPerfCurrentPktsReOrder_Type=PerfCurrentCount
_CpwCTDMPerfCurrentPktsReOrder_Object=MibTableColumn
cpwCTDMPerfCurrentPktsReOrder=_CpwCTDMPerfCurrentPktsReOrder_Object((1,3,6,1,4,1,9,10,131,1,5,1,2),_CpwCTDMPerfCurrentPktsReOrder_Type())
cpwCTDMPerfCurrentPktsReOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentPktsReOrder.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentPktsReOrder.setUnits(_E)
_CpwCTDMPerfCurrentJtrBfrUnderruns_Type=PerfCurrentCount
_CpwCTDMPerfCurrentJtrBfrUnderruns_Object=MibTableColumn
cpwCTDMPerfCurrentJtrBfrUnderruns=_CpwCTDMPerfCurrentJtrBfrUnderruns_Object((1,3,6,1,4,1,9,10,131,1,5,1,3),_CpwCTDMPerfCurrentJtrBfrUnderruns_Type())
cpwCTDMPerfCurrentJtrBfrUnderruns.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentJtrBfrUnderruns.setStatus(_A)
_CpwCTDMPerfCurrentMisOrderDropped_Type=PerfCurrentCount
_CpwCTDMPerfCurrentMisOrderDropped_Object=MibTableColumn
cpwCTDMPerfCurrentMisOrderDropped=_CpwCTDMPerfCurrentMisOrderDropped_Object((1,3,6,1,4,1,9,10,131,1,5,1,4),_CpwCTDMPerfCurrentMisOrderDropped_Type())
cpwCTDMPerfCurrentMisOrderDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentMisOrderDropped.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentMisOrderDropped.setUnits(_E)
_CpwCTDMPerfCurrentMalformedPkt_Type=PerfCurrentCount
_CpwCTDMPerfCurrentMalformedPkt_Object=MibTableColumn
cpwCTDMPerfCurrentMalformedPkt=_CpwCTDMPerfCurrentMalformedPkt_Object((1,3,6,1,4,1,9,10,131,1,5,1,5),_CpwCTDMPerfCurrentMalformedPkt_Type())
cpwCTDMPerfCurrentMalformedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentMalformedPkt.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentMalformedPkt.setUnits(_E)
_CpwCTDMPerfCurrentESs_Type=PerfCurrentCount
_CpwCTDMPerfCurrentESs_Object=MibTableColumn
cpwCTDMPerfCurrentESs=_CpwCTDMPerfCurrentESs_Object((1,3,6,1,4,1,9,10,131,1,5,1,6),_CpwCTDMPerfCurrentESs_Type())
cpwCTDMPerfCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentESs.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentESs.setUnits(_F)
_CpwCTDMPerfCurrentSESs_Type=PerfCurrentCount
_CpwCTDMPerfCurrentSESs_Object=MibTableColumn
cpwCTDMPerfCurrentSESs=_CpwCTDMPerfCurrentSESs_Object((1,3,6,1,4,1,9,10,131,1,5,1,7),_CpwCTDMPerfCurrentSESs_Type())
cpwCTDMPerfCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentSESs.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentSESs.setUnits(_F)
_CpwCTDMPerfCurrentUASs_Type=PerfCurrentCount
_CpwCTDMPerfCurrentUASs_Object=MibTableColumn
cpwCTDMPerfCurrentUASs=_CpwCTDMPerfCurrentUASs_Object((1,3,6,1,4,1,9,10,131,1,5,1,8),_CpwCTDMPerfCurrentUASs_Type())
cpwCTDMPerfCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentUASs.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentUASs.setUnits(_F)
_CpwCTDMPerfCurrentFC_Type=PerfCurrentCount
_CpwCTDMPerfCurrentFC_Object=MibTableColumn
cpwCTDMPerfCurrentFC=_CpwCTDMPerfCurrentFC_Object((1,3,6,1,4,1,9,10,131,1,5,1,9),_CpwCTDMPerfCurrentFC_Type())
cpwCTDMPerfCurrentFC.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfCurrentFC.setStatus(_A)
_CpwCTDMPerfIntervalTable_Object=MibTable
cpwCTDMPerfIntervalTable=_CpwCTDMPerfIntervalTable_Object((1,3,6,1,4,1,9,10,131,1,6))
if mibBuilder.loadTexts:cpwCTDMPerfIntervalTable.setStatus(_A)
_CpwCTDMPerfIntervalEntry_Object=MibTableRow
cpwCTDMPerfIntervalEntry=_CpwCTDMPerfIntervalEntry_Object((1,3,6,1,4,1,9,10,131,1,6,1))
cpwCTDMPerfIntervalEntry.setIndexNames((0,_I,_J),(0,_B,_b))
if mibBuilder.loadTexts:cpwCTDMPerfIntervalEntry.setStatus(_A)
_CpwCTDMPerfIntervalNumber_Type=Unsigned32
_CpwCTDMPerfIntervalNumber_Object=MibTableColumn
cpwCTDMPerfIntervalNumber=_CpwCTDMPerfIntervalNumber_Object((1,3,6,1,4,1,9,10,131,1,6,1,1),_CpwCTDMPerfIntervalNumber_Type())
cpwCTDMPerfIntervalNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalNumber.setStatus(_A)
_CpwCTDMPerfIntervalValidData_Type=TruthValue
_CpwCTDMPerfIntervalValidData_Object=MibTableColumn
cpwCTDMPerfIntervalValidData=_CpwCTDMPerfIntervalValidData_Object((1,3,6,1,4,1,9,10,131,1,6,1,2),_CpwCTDMPerfIntervalValidData_Type())
cpwCTDMPerfIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalValidData.setStatus(_A)
class _CpwCTDMPerfIntervalDuration_Type(Unsigned32):defaultValue=900
_CpwCTDMPerfIntervalDuration_Type.__name__=_G
_CpwCTDMPerfIntervalDuration_Object=MibTableColumn
cpwCTDMPerfIntervalDuration=_CpwCTDMPerfIntervalDuration_Object((1,3,6,1,4,1,9,10,131,1,6,1,3),_CpwCTDMPerfIntervalDuration_Type())
cpwCTDMPerfIntervalDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalDuration.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalDuration.setUnits(_F)
_CpwCTDMPerfIntervalMissingPkts_Type=PerfIntervalCount
_CpwCTDMPerfIntervalMissingPkts_Object=MibTableColumn
cpwCTDMPerfIntervalMissingPkts=_CpwCTDMPerfIntervalMissingPkts_Object((1,3,6,1,4,1,9,10,131,1,6,1,4),_CpwCTDMPerfIntervalMissingPkts_Type())
cpwCTDMPerfIntervalMissingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalMissingPkts.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalMissingPkts.setUnits(_E)
_CpwCTDMPerfIntervalPktsReOrder_Type=PerfIntervalCount
_CpwCTDMPerfIntervalPktsReOrder_Object=MibTableColumn
cpwCTDMPerfIntervalPktsReOrder=_CpwCTDMPerfIntervalPktsReOrder_Object((1,3,6,1,4,1,9,10,131,1,6,1,5),_CpwCTDMPerfIntervalPktsReOrder_Type())
cpwCTDMPerfIntervalPktsReOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalPktsReOrder.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalPktsReOrder.setUnits(_E)
_CpwCTDMPerfIntervalJtrBfrUnderruns_Type=PerfIntervalCount
_CpwCTDMPerfIntervalJtrBfrUnderruns_Object=MibTableColumn
cpwCTDMPerfIntervalJtrBfrUnderruns=_CpwCTDMPerfIntervalJtrBfrUnderruns_Object((1,3,6,1,4,1,9,10,131,1,6,1,6),_CpwCTDMPerfIntervalJtrBfrUnderruns_Type())
cpwCTDMPerfIntervalJtrBfrUnderruns.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalJtrBfrUnderruns.setStatus(_A)
_CpwCTDMPerfIntervalMisOrderDropped_Type=PerfIntervalCount
_CpwCTDMPerfIntervalMisOrderDropped_Object=MibTableColumn
cpwCTDMPerfIntervalMisOrderDropped=_CpwCTDMPerfIntervalMisOrderDropped_Object((1,3,6,1,4,1,9,10,131,1,6,1,7),_CpwCTDMPerfIntervalMisOrderDropped_Type())
cpwCTDMPerfIntervalMisOrderDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalMisOrderDropped.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalMisOrderDropped.setUnits(_E)
_CpwCTDMPerfIntervalMalformedPkt_Type=PerfIntervalCount
_CpwCTDMPerfIntervalMalformedPkt_Object=MibTableColumn
cpwCTDMPerfIntervalMalformedPkt=_CpwCTDMPerfIntervalMalformedPkt_Object((1,3,6,1,4,1,9,10,131,1,6,1,8),_CpwCTDMPerfIntervalMalformedPkt_Type())
cpwCTDMPerfIntervalMalformedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalMalformedPkt.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalMalformedPkt.setUnits(_E)
_CpwCTDMPerfIntervalESs_Type=PerfIntervalCount
_CpwCTDMPerfIntervalESs_Object=MibTableColumn
cpwCTDMPerfIntervalESs=_CpwCTDMPerfIntervalESs_Object((1,3,6,1,4,1,9,10,131,1,6,1,9),_CpwCTDMPerfIntervalESs_Type())
cpwCTDMPerfIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalESs.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalESs.setUnits(_F)
_CpwCTDMPerfIntervalSESs_Type=PerfIntervalCount
_CpwCTDMPerfIntervalSESs_Object=MibTableColumn
cpwCTDMPerfIntervalSESs=_CpwCTDMPerfIntervalSESs_Object((1,3,6,1,4,1,9,10,131,1,6,1,10),_CpwCTDMPerfIntervalSESs_Type())
cpwCTDMPerfIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalSESs.setStatus(_A)
_CpwCTDMPerfIntervalUASs_Type=PerfIntervalCount
_CpwCTDMPerfIntervalUASs_Object=MibTableColumn
cpwCTDMPerfIntervalUASs=_CpwCTDMPerfIntervalUASs_Object((1,3,6,1,4,1,9,10,131,1,6,1,11),_CpwCTDMPerfIntervalUASs_Type())
cpwCTDMPerfIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalUASs.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalUASs.setUnits(_F)
_CpwCTDMPerfIntervalFC_Type=PerfIntervalCount
_CpwCTDMPerfIntervalFC_Object=MibTableColumn
cpwCTDMPerfIntervalFC=_CpwCTDMPerfIntervalFC_Object((1,3,6,1,4,1,9,10,131,1,6,1,12),_CpwCTDMPerfIntervalFC_Type())
cpwCTDMPerfIntervalFC.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerfIntervalFC.setStatus(_A)
_CpwCTDMPerf1DayIntervalTable_Object=MibTable
cpwCTDMPerf1DayIntervalTable=_CpwCTDMPerf1DayIntervalTable_Object((1,3,6,1,4,1,9,10,131,1,7))
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalTable.setStatus(_A)
_CpwCTDMPerf1DayIntervalEntry_Object=MibTableRow
cpwCTDMPerf1DayIntervalEntry=_CpwCTDMPerf1DayIntervalEntry_Object((1,3,6,1,4,1,9,10,131,1,7,1))
cpwCTDMPerf1DayIntervalEntry.setIndexNames((0,_I,_J),(0,_B,_c))
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalEntry.setStatus(_A)
_CpwCTDMPerf1DayIntervalNumber_Type=Unsigned32
_CpwCTDMPerf1DayIntervalNumber_Object=MibTableColumn
cpwCTDMPerf1DayIntervalNumber=_CpwCTDMPerf1DayIntervalNumber_Object((1,3,6,1,4,1,9,10,131,1,7,1,1),_CpwCTDMPerf1DayIntervalNumber_Type())
cpwCTDMPerf1DayIntervalNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalNumber.setStatus(_A)
_CpwCTDMPerf1DayIntervalValidData_Type=TruthValue
_CpwCTDMPerf1DayIntervalValidData_Object=MibTableColumn
cpwCTDMPerf1DayIntervalValidData=_CpwCTDMPerf1DayIntervalValidData_Object((1,3,6,1,4,1,9,10,131,1,7,1,2),_CpwCTDMPerf1DayIntervalValidData_Type())
cpwCTDMPerf1DayIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalValidData.setStatus(_A)
_CpwCTDMPerf1DayIntervalDuration_Type=Unsigned32
_CpwCTDMPerf1DayIntervalDuration_Object=MibTableColumn
cpwCTDMPerf1DayIntervalDuration=_CpwCTDMPerf1DayIntervalDuration_Object((1,3,6,1,4,1,9,10,131,1,7,1,3),_CpwCTDMPerf1DayIntervalDuration_Type())
cpwCTDMPerf1DayIntervalDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalDuration.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalDuration.setUnits(_F)
_CpwCTDMPerf1DayIntervalMissingPkts_Type=Counter32
_CpwCTDMPerf1DayIntervalMissingPkts_Object=MibTableColumn
cpwCTDMPerf1DayIntervalMissingPkts=_CpwCTDMPerf1DayIntervalMissingPkts_Object((1,3,6,1,4,1,9,10,131,1,7,1,4),_CpwCTDMPerf1DayIntervalMissingPkts_Type())
cpwCTDMPerf1DayIntervalMissingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalMissingPkts.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalMissingPkts.setUnits(_E)
_CpwCTDMPerf1DayIntervalPktsReOrder_Type=Counter32
_CpwCTDMPerf1DayIntervalPktsReOrder_Object=MibTableColumn
cpwCTDMPerf1DayIntervalPktsReOrder=_CpwCTDMPerf1DayIntervalPktsReOrder_Object((1,3,6,1,4,1,9,10,131,1,7,1,5),_CpwCTDMPerf1DayIntervalPktsReOrder_Type())
cpwCTDMPerf1DayIntervalPktsReOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalPktsReOrder.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalPktsReOrder.setUnits(_E)
_CpwCTDMPerf1DayIntervalJtrBfrUnderruns_Type=Counter32
_CpwCTDMPerf1DayIntervalJtrBfrUnderruns_Object=MibTableColumn
cpwCTDMPerf1DayIntervalJtrBfrUnderruns=_CpwCTDMPerf1DayIntervalJtrBfrUnderruns_Object((1,3,6,1,4,1,9,10,131,1,7,1,6),_CpwCTDMPerf1DayIntervalJtrBfrUnderruns_Type())
cpwCTDMPerf1DayIntervalJtrBfrUnderruns.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalJtrBfrUnderruns.setStatus(_A)
_CpwCTDMPerf1DayIntervalMisOrderDropped_Type=Counter32
_CpwCTDMPerf1DayIntervalMisOrderDropped_Object=MibTableColumn
cpwCTDMPerf1DayIntervalMisOrderDropped=_CpwCTDMPerf1DayIntervalMisOrderDropped_Object((1,3,6,1,4,1,9,10,131,1,7,1,7),_CpwCTDMPerf1DayIntervalMisOrderDropped_Type())
cpwCTDMPerf1DayIntervalMisOrderDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalMisOrderDropped.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalMisOrderDropped.setUnits(_E)
_CpwCTDMPerf1DayIntervalMalformedPkt_Type=Counter32
_CpwCTDMPerf1DayIntervalMalformedPkt_Object=MibTableColumn
cpwCTDMPerf1DayIntervalMalformedPkt=_CpwCTDMPerf1DayIntervalMalformedPkt_Object((1,3,6,1,4,1,9,10,131,1,7,1,8),_CpwCTDMPerf1DayIntervalMalformedPkt_Type())
cpwCTDMPerf1DayIntervalMalformedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalMalformedPkt.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalMalformedPkt.setUnits(_E)
_CpwCTDMPerf1DayIntervalESs_Type=Counter32
_CpwCTDMPerf1DayIntervalESs_Object=MibTableColumn
cpwCTDMPerf1DayIntervalESs=_CpwCTDMPerf1DayIntervalESs_Object((1,3,6,1,4,1,9,10,131,1,7,1,9),_CpwCTDMPerf1DayIntervalESs_Type())
cpwCTDMPerf1DayIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalESs.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalESs.setUnits(_F)
_CpwCTDMPerf1DayIntervalSESs_Type=Counter32
_CpwCTDMPerf1DayIntervalSESs_Object=MibTableColumn
cpwCTDMPerf1DayIntervalSESs=_CpwCTDMPerf1DayIntervalSESs_Object((1,3,6,1,4,1,9,10,131,1,7,1,10),_CpwCTDMPerf1DayIntervalSESs_Type())
cpwCTDMPerf1DayIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalSESs.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalSESs.setUnits(_F)
_CpwCTDMPerf1DayIntervalUASs_Type=Counter32
_CpwCTDMPerf1DayIntervalUASs_Object=MibTableColumn
cpwCTDMPerf1DayIntervalUASs=_CpwCTDMPerf1DayIntervalUASs_Object((1,3,6,1,4,1,9,10,131,1,7,1,11),_CpwCTDMPerf1DayIntervalUASs_Type())
cpwCTDMPerf1DayIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalUASs.setStatus(_A)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalUASs.setUnits(_F)
_CpwCTDMPerf1DayIntervalFC_Type=Counter32
_CpwCTDMPerf1DayIntervalFC_Object=MibTableColumn
cpwCTDMPerf1DayIntervalFC=_CpwCTDMPerf1DayIntervalFC_Object((1,3,6,1,4,1,9,10,131,1,7,1,12),_CpwCTDMPerf1DayIntervalFC_Type())
cpwCTDMPerf1DayIntervalFC.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalFC.setStatus(_A)
_CpwCTDMConformance_ObjectIdentity=ObjectIdentity
cpwCTDMConformance=_CpwCTDMConformance_ObjectIdentity((1,3,6,1,4,1,9,10,131,2))
_CpwCTDMGroups_ObjectIdentity=ObjectIdentity
cpwCTDMGroups=_CpwCTDMGroups_ObjectIdentity((1,3,6,1,4,1,9,10,131,2,1))
_CpwCTDMCompliances_ObjectIdentity=ObjectIdentity
cpwCTDMCompliances=_CpwCTDMCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,131,2,2))
cpwCTDMGroup=ObjectGroup((1,3,6,1,4,1,9,10,131,2,1,1))
cpwCTDMGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:cpwCTDMGroup.setStatus(_A)
cpwCTDMPerfCurrentGroup=ObjectGroup((1,3,6,1,4,1,9,10,131,2,1,2))
cpwCTDMPerfCurrentGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:cpwCTDMPerfCurrentGroup.setStatus(_A)
cpwCTDMPerfIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,10,131,2,1,3))
cpwCTDMPerfIntervalGroup.setObjects(*((_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:cpwCTDMPerfIntervalGroup.setStatus(_A)
cpwCTDMPerf1DayIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,10,131,2,1,4))
cpwCTDMPerf1DayIntervalGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:cpwCTDMPerf1DayIntervalGroup.setStatus(_A)
cpwTDMModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,131,2,2,1))
cpwTDMModuleCompliance.setObjects(*((_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:cpwTDMModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CpwTDMCfgIndex':CpwTDMCfgIndex,'cpwCTDMMIB':cpwCTDMMIB,'cpwCTDMNotifications':cpwCTDMNotifications,'cpwCTDMObjects':cpwCTDMObjects,'cpwCTDMTable':cpwCTDMTable,'cpwCTDMEntry':cpwCTDMEntry,_d:cpwCTDMRate,_e:cpwCTDMIfIndex,_f:cpwCGenTDMCfgIndex,_g:cpwCRelTDMCfgIndex,_h:cpwCTDMConfigError,_i:cpwCTDMTimeElapsed,_j:cpwCTDMValidIntervals,_k:cpwCTDMValidDayIntervals,_l:cpwCTDMCurrentIndications,_m:cpwCTDMLatchedIndications,_n:cpwCTDMLastEsTimeStamp,_o:cpwCTDMCfgIndexNext,'cpwCTDMCfgTable':cpwCTDMCfgTable,'cpwCTDMCfgEntry':cpwCTDMCfgEntry,_Y:cpwCTDMCfgIndex,_q:cpwCTDMCfgConfErr,_r:cpwCTDMCfgPayloadSize,_s:cpwCTDMCfgPktReorder,_t:cpwCTDMCfgRtpHdrUsed,_u:cpwCTDMCfgJtrBfrDepth,_v:cpwCTDMCfgPayloadSuppression,_w:cpwCTDMCfgConsecPktsInSynch,_x:cpwCTDMCfgConsecMissPktsOutSynch,_y:cpwCTDMCfgSetUp2SynchTimeOut,_z:cpwCTDMCfgPktReplacePolicy,_A0:cpwCTDMCfgAvePktLossTimeWindow,_A1:cpwCTDMCfgExcessivePktLossThreshold,_A2:cpwCTDMCfgAlarmThreshold,_A3:cpwCTDMCfgClearAlarmThreshold,_A4:cpwCTDMCfgMissingPktsToSes,_A5:cpwCTDMCfgTimestampMode,_A6:cpwCTDMCfgStorageType,_p:cpwCTDMCfgRowStatus,'cpwCTDMPerfCurrentTable':cpwCTDMPerfCurrentTable,'cpwCTDMPerfCurrentEntry':cpwCTDMPerfCurrentEntry,_A7:cpwCTDMPerfCurrentMissingPkts,_A8:cpwCTDMPerfCurrentPktsReOrder,_A9:cpwCTDMPerfCurrentJtrBfrUnderruns,_AA:cpwCTDMPerfCurrentMisOrderDropped,_AB:cpwCTDMPerfCurrentMalformedPkt,_AC:cpwCTDMPerfCurrentESs,_AD:cpwCTDMPerfCurrentSESs,_AE:cpwCTDMPerfCurrentUASs,_AF:cpwCTDMPerfCurrentFC,'cpwCTDMPerfIntervalTable':cpwCTDMPerfIntervalTable,'cpwCTDMPerfIntervalEntry':cpwCTDMPerfIntervalEntry,_b:cpwCTDMPerfIntervalNumber,_AG:cpwCTDMPerfIntervalValidData,_AH:cpwCTDMPerfIntervalDuration,_AI:cpwCTDMPerfIntervalMissingPkts,_AJ:cpwCTDMPerfIntervalPktsReOrder,_AK:cpwCTDMPerfIntervalJtrBfrUnderruns,_AL:cpwCTDMPerfIntervalMisOrderDropped,_AM:cpwCTDMPerfIntervalMalformedPkt,_AN:cpwCTDMPerfIntervalESs,_AO:cpwCTDMPerfIntervalSESs,_AP:cpwCTDMPerfIntervalUASs,_AQ:cpwCTDMPerfIntervalFC,'cpwCTDMPerf1DayIntervalTable':cpwCTDMPerf1DayIntervalTable,'cpwCTDMPerf1DayIntervalEntry':cpwCTDMPerf1DayIntervalEntry,_c:cpwCTDMPerf1DayIntervalNumber,_AR:cpwCTDMPerf1DayIntervalValidData,_AS:cpwCTDMPerf1DayIntervalDuration,_AT:cpwCTDMPerf1DayIntervalMissingPkts,_AU:cpwCTDMPerf1DayIntervalPktsReOrder,_AV:cpwCTDMPerf1DayIntervalJtrBfrUnderruns,_AW:cpwCTDMPerf1DayIntervalMisOrderDropped,_AX:cpwCTDMPerf1DayIntervalMalformedPkt,_AY:cpwCTDMPerf1DayIntervalESs,_AZ:cpwCTDMPerf1DayIntervalSESs,_Aa:cpwCTDMPerf1DayIntervalUASs,_Ab:cpwCTDMPerf1DayIntervalFC,'cpwCTDMConformance':cpwCTDMConformance,'cpwCTDMGroups':cpwCTDMGroups,_Ac:cpwCTDMGroup,_Ad:cpwCTDMPerfCurrentGroup,_Ae:cpwCTDMPerfIntervalGroup,_Af:cpwCTDMPerf1DayIntervalGroup,'cpwCTDMCompliances':cpwCTDMCompliances,'cpwTDMModuleCompliance':cpwTDMModuleCompliance})