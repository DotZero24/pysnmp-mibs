_W='millisecond'
_V='zxPwCTDMCfgIndex'
_U='ZXPW-TDM-MIB'
_T='tdmFault'
_S='packetLoss'
_R='pktMisOrder'
_Q='remotePktLoss'
_P='bufferUnderrun'
_O='bufferOverrun'
_N='excessivePktLossRate'
_M='malformedPacket'
_L='zxPwIndex'
_K='ZXPW-STD-MIB'
_J='TruthValue'
_I='DisplayString'
_H='other'
_G='read-write'
_F='Bits'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_J)
zxPwCTDM,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxPwCTDM')
zxPwIndex,=mibBuilder.importSymbols(_K,_L)
zxPwCTDMMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,2,1,2))
class PwTDMCfgIndex(TextualConvention,Unsigned32):status=_A
_ZxPwCTDMObjects_ObjectIdentity=ObjectIdentity
zxPwCTDMObjects=_ZxPwCTDMObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,2,1,2,1))
_ZxPwCTDMTable_Object=MibTable
zxPwCTDMTable=_ZxPwCTDMTable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1))
if mibBuilder.loadTexts:zxPwCTDMTable.setStatus(_A)
_ZxPwCTDMEntry_Object=MibTableRow
zxPwCTDMEntry=_ZxPwCTDMEntry_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1))
zxPwCTDMEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:zxPwCTDMEntry.setStatus(_A)
class _ZxPwCTDMRate_Type(Integer32):defaultValue=32
_ZxPwCTDMRate_Type.__name__=_D
_ZxPwCTDMRate_Object=MibTableColumn
zxPwCTDMRate=_ZxPwCTDMRate_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,1),_ZxPwCTDMRate_Type())
zxPwCTDMRate.setMaxAccess(_G)
if mibBuilder.loadTexts:zxPwCTDMRate.setStatus(_A)
_ZxPwCTDMIfIndex_Type=InterfaceIndexOrZero
_ZxPwCTDMIfIndex_Object=MibTableColumn
zxPwCTDMIfIndex=_ZxPwCTDMIfIndex_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,2),_ZxPwCTDMIfIndex_Type())
zxPwCTDMIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxPwCTDMIfIndex.setStatus(_A)
_ZxPwCGenTDMCfgIndex_Type=PwTDMCfgIndex
_ZxPwCGenTDMCfgIndex_Object=MibTableColumn
zxPwCGenTDMCfgIndex=_ZxPwCGenTDMCfgIndex_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,3),_ZxPwCGenTDMCfgIndex_Type())
zxPwCGenTDMCfgIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxPwCGenTDMCfgIndex.setStatus(_A)
_ZxPwCRelTDMCfgIndex_Type=PwTDMCfgIndex
_ZxPwCRelTDMCfgIndex_Object=MibTableColumn
zxPwCRelTDMCfgIndex=_ZxPwCRelTDMCfgIndex_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,4),_ZxPwCRelTDMCfgIndex_Type())
zxPwCRelTDMCfgIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxPwCRelTDMCfgIndex.setStatus(_A)
class _ZxPwCTDMConfigError_Type(Bits):namedValues=NamedValues(*((_H,0),('tdmTypeIncompatible',1),('peerRtpIncompatible',2),('peerPayloadSizeIncompatible',3)))
_ZxPwCTDMConfigError_Type.__name__=_F
_ZxPwCTDMConfigError_Object=MibTableColumn
zxPwCTDMConfigError=_ZxPwCTDMConfigError_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,5),_ZxPwCTDMConfigError_Type())
zxPwCTDMConfigError.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMConfigError.setStatus(_A)
class _ZxPwCTDMTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_ZxPwCTDMTimeElapsed_Type.__name__=_D
_ZxPwCTDMTimeElapsed_Object=MibTableColumn
zxPwCTDMTimeElapsed=_ZxPwCTDMTimeElapsed_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,6),_ZxPwCTDMTimeElapsed_Type())
zxPwCTDMTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMTimeElapsed.setStatus(_A)
class _ZxPwCTDMValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ZxPwCTDMValidIntervals_Type.__name__=_D
_ZxPwCTDMValidIntervals_Object=MibTableColumn
zxPwCTDMValidIntervals=_ZxPwCTDMValidIntervals_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,7),_ZxPwCTDMValidIntervals_Type())
zxPwCTDMValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMValidIntervals.setStatus(_A)
class _ZxPwCTDMValidDayIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_ZxPwCTDMValidDayIntervals_Type.__name__=_D
_ZxPwCTDMValidDayIntervals_Object=MibTableColumn
zxPwCTDMValidDayIntervals=_ZxPwCTDMValidDayIntervals_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,8),_ZxPwCTDMValidDayIntervals_Type())
zxPwCTDMValidDayIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMValidDayIntervals.setStatus(_A)
class _ZxPwCTDMCurrentIndications_Type(Bits):namedValues=NamedValues(*((_H,0),('strayPacket',1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,9)))
_ZxPwCTDMCurrentIndications_Type.__name__=_F
_ZxPwCTDMCurrentIndications_Object=MibTableColumn
zxPwCTDMCurrentIndications=_ZxPwCTDMCurrentIndications_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,9),_ZxPwCTDMCurrentIndications_Type())
zxPwCTDMCurrentIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMCurrentIndications.setStatus(_A)
class _ZxPwCTDMLatchedIndications_Type(Bits):namedValues=NamedValues(*((_H,0),('staryPacket',1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,9)))
_ZxPwCTDMLatchedIndications_Type.__name__=_F
_ZxPwCTDMLatchedIndications_Object=MibTableColumn
zxPwCTDMLatchedIndications=_ZxPwCTDMLatchedIndications_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,10),_ZxPwCTDMLatchedIndications_Type())
zxPwCTDMLatchedIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMLatchedIndications.setStatus(_A)
_ZxPwCTDMLastEsTimeStamp_Type=TimeStamp
_ZxPwCTDMLastEsTimeStamp_Object=MibTableColumn
zxPwCTDMLastEsTimeStamp=_ZxPwCTDMLastEsTimeStamp_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,1,1,11),_ZxPwCTDMLastEsTimeStamp_Type())
zxPwCTDMLastEsTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMLastEsTimeStamp.setStatus(_A)
_ZxPwCTDMCfgIndexNext_Type=Unsigned32
_ZxPwCTDMCfgIndexNext_Object=MibScalar
zxPwCTDMCfgIndexNext=_ZxPwCTDMCfgIndexNext_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,2),_ZxPwCTDMCfgIndexNext_Type())
zxPwCTDMCfgIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMCfgIndexNext.setStatus(_A)
_ZxPwCTDMCfgTable_Object=MibTable
zxPwCTDMCfgTable=_ZxPwCTDMCfgTable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3))
if mibBuilder.loadTexts:zxPwCTDMCfgTable.setStatus(_A)
_ZxPwCTDMCfgEntry_Object=MibTableRow
zxPwCTDMCfgEntry=_ZxPwCTDMCfgEntry_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1))
zxPwCTDMCfgEntry.setIndexNames((0,_U,_V))
if mibBuilder.loadTexts:zxPwCTDMCfgEntry.setStatus(_A)
_ZxPwCTDMCfgIndex_Type=PwTDMCfgIndex
_ZxPwCTDMCfgIndex_Object=MibTableColumn
zxPwCTDMCfgIndex=_ZxPwCTDMCfgIndex_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,1),_ZxPwCTDMCfgIndex_Type())
zxPwCTDMCfgIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxPwCTDMCfgIndex.setStatus(_A)
_ZxPwCTDMCfgRowStatus_Type=RowStatus
_ZxPwCTDMCfgRowStatus_Object=MibTableColumn
zxPwCTDMCfgRowStatus=_ZxPwCTDMCfgRowStatus_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,2),_ZxPwCTDMCfgRowStatus_Type())
zxPwCTDMCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgRowStatus.setStatus(_A)
class _ZxPwCTDMCfgConfErr_Type(Bits):namedValues=NamedValues(*((_H,0),('payloadSize',1),('jtrBfrDepth',2)))
_ZxPwCTDMCfgConfErr_Type.__name__=_F
_ZxPwCTDMCfgConfErr_Object=MibTableColumn
zxPwCTDMCfgConfErr=_ZxPwCTDMCfgConfErr_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,3),_ZxPwCTDMCfgConfErr_Type())
zxPwCTDMCfgConfErr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMCfgConfErr.setStatus(_A)
_ZxPwCTDMCfgPayloadSize_Type=Unsigned32
_ZxPwCTDMCfgPayloadSize_Object=MibTableColumn
zxPwCTDMCfgPayloadSize=_ZxPwCTDMCfgPayloadSize_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,4),_ZxPwCTDMCfgPayloadSize_Type())
zxPwCTDMCfgPayloadSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgPayloadSize.setStatus(_A)
_ZxPwCTDMCfgPktReorder_Type=TruthValue
_ZxPwCTDMCfgPktReorder_Object=MibTableColumn
zxPwCTDMCfgPktReorder=_ZxPwCTDMCfgPktReorder_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,5),_ZxPwCTDMCfgPktReorder_Type())
zxPwCTDMCfgPktReorder.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgPktReorder.setStatus(_A)
class _ZxPwCTDMCfgRtpHdrUsed_Type(TruthValue):defaultValue=2
_ZxPwCTDMCfgRtpHdrUsed_Type.__name__=_J
_ZxPwCTDMCfgRtpHdrUsed_Object=MibTableColumn
zxPwCTDMCfgRtpHdrUsed=_ZxPwCTDMCfgRtpHdrUsed_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,6),_ZxPwCTDMCfgRtpHdrUsed_Type())
zxPwCTDMCfgRtpHdrUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgRtpHdrUsed.setStatus(_A)
class _ZxPwCTDMCfgJtrBfrDepth_Type(Unsigned32):defaultValue=3000
_ZxPwCTDMCfgJtrBfrDepth_Type.__name__=_E
_ZxPwCTDMCfgJtrBfrDepth_Object=MibTableColumn
zxPwCTDMCfgJtrBfrDepth=_ZxPwCTDMCfgJtrBfrDepth_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,7),_ZxPwCTDMCfgJtrBfrDepth_Type())
zxPwCTDMCfgJtrBfrDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgJtrBfrDepth.setStatus(_A)
if mibBuilder.loadTexts:zxPwCTDMCfgJtrBfrDepth.setUnits('microsecond')
class _ZxPwCTDMCfgPayloadSuppression_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxPwCTDMCfgPayloadSuppression_Type.__name__=_D
_ZxPwCTDMCfgPayloadSuppression_Object=MibTableColumn
zxPwCTDMCfgPayloadSuppression=_ZxPwCTDMCfgPayloadSuppression_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,8),_ZxPwCTDMCfgPayloadSuppression_Type())
zxPwCTDMCfgPayloadSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgPayloadSuppression.setStatus(_A)
class _ZxPwCTDMCfgConsecPktsInSynch_Type(Unsigned32):defaultValue=2
_ZxPwCTDMCfgConsecPktsInSynch_Type.__name__=_E
_ZxPwCTDMCfgConsecPktsInSynch_Object=MibTableColumn
zxPwCTDMCfgConsecPktsInSynch=_ZxPwCTDMCfgConsecPktsInSynch_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,9),_ZxPwCTDMCfgConsecPktsInSynch_Type())
zxPwCTDMCfgConsecPktsInSynch.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgConsecPktsInSynch.setStatus(_A)
class _ZxPwCTDMCfgConsecMissPktsOutSynch_Type(Unsigned32):defaultValue=10
_ZxPwCTDMCfgConsecMissPktsOutSynch_Type.__name__=_E
_ZxPwCTDMCfgConsecMissPktsOutSynch_Object=MibTableColumn
zxPwCTDMCfgConsecMissPktsOutSynch=_ZxPwCTDMCfgConsecMissPktsOutSynch_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,10),_ZxPwCTDMCfgConsecMissPktsOutSynch_Type())
zxPwCTDMCfgConsecMissPktsOutSynch.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgConsecMissPktsOutSynch.setStatus(_A)
class _ZxPwCTDMCfgSetUp2SynchTimeOut_Type(Unsigned32):defaultValue=5000
_ZxPwCTDMCfgSetUp2SynchTimeOut_Type.__name__=_E
_ZxPwCTDMCfgSetUp2SynchTimeOut_Object=MibTableColumn
zxPwCTDMCfgSetUp2SynchTimeOut=_ZxPwCTDMCfgSetUp2SynchTimeOut_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,11),_ZxPwCTDMCfgSetUp2SynchTimeOut_Type())
zxPwCTDMCfgSetUp2SynchTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgSetUp2SynchTimeOut.setStatus(_A)
if mibBuilder.loadTexts:zxPwCTDMCfgSetUp2SynchTimeOut.setUnits(_W)
class _ZxPwCTDMCfgPktReplacePolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ais',1),('implementationSpecific',2)))
_ZxPwCTDMCfgPktReplacePolicy_Type.__name__=_D
_ZxPwCTDMCfgPktReplacePolicy_Object=MibTableColumn
zxPwCTDMCfgPktReplacePolicy=_ZxPwCTDMCfgPktReplacePolicy_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,12),_ZxPwCTDMCfgPktReplacePolicy_Type())
zxPwCTDMCfgPktReplacePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgPktReplacePolicy.setStatus(_A)
_ZxPwCTDMCfgAvePktLossTimeWindow_Type=Integer32
_ZxPwCTDMCfgAvePktLossTimeWindow_Object=MibTableColumn
zxPwCTDMCfgAvePktLossTimeWindow=_ZxPwCTDMCfgAvePktLossTimeWindow_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,13),_ZxPwCTDMCfgAvePktLossTimeWindow_Type())
zxPwCTDMCfgAvePktLossTimeWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgAvePktLossTimeWindow.setStatus(_A)
if mibBuilder.loadTexts:zxPwCTDMCfgAvePktLossTimeWindow.setUnits(_W)
_ZxPwCTDMCfgExcessivePktLossThreshold_Type=Unsigned32
_ZxPwCTDMCfgExcessivePktLossThreshold_Object=MibTableColumn
zxPwCTDMCfgExcessivePktLossThreshold=_ZxPwCTDMCfgExcessivePktLossThreshold_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,14),_ZxPwCTDMCfgExcessivePktLossThreshold_Type())
zxPwCTDMCfgExcessivePktLossThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgExcessivePktLossThreshold.setStatus(_A)
class _ZxPwCTDMCfgAlarmThreshold_Type(Unsigned32):defaultValue=2500
_ZxPwCTDMCfgAlarmThreshold_Type.__name__=_E
_ZxPwCTDMCfgAlarmThreshold_Object=MibTableColumn
zxPwCTDMCfgAlarmThreshold=_ZxPwCTDMCfgAlarmThreshold_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,15),_ZxPwCTDMCfgAlarmThreshold_Type())
zxPwCTDMCfgAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgAlarmThreshold.setStatus(_A)
class _ZxPwCTDMCfgClearAlarmThreshold_Type(Unsigned32):defaultValue=10000
_ZxPwCTDMCfgClearAlarmThreshold_Type.__name__=_E
_ZxPwCTDMCfgClearAlarmThreshold_Object=MibTableColumn
zxPwCTDMCfgClearAlarmThreshold=_ZxPwCTDMCfgClearAlarmThreshold_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,16),_ZxPwCTDMCfgClearAlarmThreshold_Type())
zxPwCTDMCfgClearAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgClearAlarmThreshold.setStatus(_A)
class _ZxPwCTDMCfgMissingPktsToSes_Type(Unsigned32):defaultValue=3
_ZxPwCTDMCfgMissingPktsToSes_Type.__name__=_E
_ZxPwCTDMCfgMissingPktsToSes_Object=MibTableColumn
zxPwCTDMCfgMissingPktsToSes=_ZxPwCTDMCfgMissingPktsToSes_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,17),_ZxPwCTDMCfgMissingPktsToSes_Type())
zxPwCTDMCfgMissingPktsToSes.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgMissingPktsToSes.setStatus(_A)
if mibBuilder.loadTexts:zxPwCTDMCfgMissingPktsToSes.setUnits('seconds')
class _ZxPwCTDMCfgTimestampMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('absolute',2),('differential',3)))
_ZxPwCTDMCfgTimestampMode_Type.__name__=_D
_ZxPwCTDMCfgTimestampMode_Object=MibTableColumn
zxPwCTDMCfgTimestampMode=_ZxPwCTDMCfgTimestampMode_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,18),_ZxPwCTDMCfgTimestampMode_Type())
zxPwCTDMCfgTimestampMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgTimestampMode.setStatus(_A)
_ZxPwCTDMCfgQueueSize_Type=Unsigned32
_ZxPwCTDMCfgQueueSize_Object=MibTableColumn
zxPwCTDMCfgQueueSize=_ZxPwCTDMCfgQueueSize_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,19),_ZxPwCTDMCfgQueueSize_Type())
zxPwCTDMCfgQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgQueueSize.setStatus(_A)
class _ZxPwCTDMCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxPwCTDMCfgName_Type.__name__=_I
_ZxPwCTDMCfgName_Object=MibTableColumn
zxPwCTDMCfgName=_ZxPwCTDMCfgName_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,20),_ZxPwCTDMCfgName_Type())
zxPwCTDMCfgName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgName.setStatus(_A)
_ZxPwCTDMCfgSSRC_Type=Unsigned32
_ZxPwCTDMCfgSSRC_Object=MibTableColumn
zxPwCTDMCfgSSRC=_ZxPwCTDMCfgSSRC_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,21),_ZxPwCTDMCfgSSRC_Type())
zxPwCTDMCfgSSRC.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgSSRC.setStatus(_A)
_ZxPwCTDMCfgStorageType_Type=StorageType
_ZxPwCTDMCfgStorageType_Object=MibTableColumn
zxPwCTDMCfgStorageType=_ZxPwCTDMCfgStorageType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,3,1,22),_ZxPwCTDMCfgStorageType_Type())
zxPwCTDMCfgStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCTDMCfgStorageType.setStatus(_A)
_ZxPwCTDMGlobalObjects_ObjectIdentity=ObjectIdentity
zxPwCTDMGlobalObjects=_ZxPwCTDMGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,50))
class _ZxPwCTDMCompatible_Type(Bits):namedValues=NamedValues(('structuredCes',0))
_ZxPwCTDMCompatible_Type.__name__=_F
_ZxPwCTDMCompatible_Object=MibScalar
zxPwCTDMCompatible=_ZxPwCTDMCompatible_Object((1,3,6,1,4,1,3902,1015,1013,2,1,2,1,50,1),_ZxPwCTDMCompatible_Type())
zxPwCTDMCompatible.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCTDMCompatible.setStatus(_A)
mibBuilder.exportSymbols(_U,**{'PwTDMCfgIndex':PwTDMCfgIndex,'zxPwCTDMMIB':zxPwCTDMMIB,'zxPwCTDMObjects':zxPwCTDMObjects,'zxPwCTDMTable':zxPwCTDMTable,'zxPwCTDMEntry':zxPwCTDMEntry,'zxPwCTDMRate':zxPwCTDMRate,'zxPwCTDMIfIndex':zxPwCTDMIfIndex,'zxPwCGenTDMCfgIndex':zxPwCGenTDMCfgIndex,'zxPwCRelTDMCfgIndex':zxPwCRelTDMCfgIndex,'zxPwCTDMConfigError':zxPwCTDMConfigError,'zxPwCTDMTimeElapsed':zxPwCTDMTimeElapsed,'zxPwCTDMValidIntervals':zxPwCTDMValidIntervals,'zxPwCTDMValidDayIntervals':zxPwCTDMValidDayIntervals,'zxPwCTDMCurrentIndications':zxPwCTDMCurrentIndications,'zxPwCTDMLatchedIndications':zxPwCTDMLatchedIndications,'zxPwCTDMLastEsTimeStamp':zxPwCTDMLastEsTimeStamp,'zxPwCTDMCfgIndexNext':zxPwCTDMCfgIndexNext,'zxPwCTDMCfgTable':zxPwCTDMCfgTable,'zxPwCTDMCfgEntry':zxPwCTDMCfgEntry,_V:zxPwCTDMCfgIndex,'zxPwCTDMCfgRowStatus':zxPwCTDMCfgRowStatus,'zxPwCTDMCfgConfErr':zxPwCTDMCfgConfErr,'zxPwCTDMCfgPayloadSize':zxPwCTDMCfgPayloadSize,'zxPwCTDMCfgPktReorder':zxPwCTDMCfgPktReorder,'zxPwCTDMCfgRtpHdrUsed':zxPwCTDMCfgRtpHdrUsed,'zxPwCTDMCfgJtrBfrDepth':zxPwCTDMCfgJtrBfrDepth,'zxPwCTDMCfgPayloadSuppression':zxPwCTDMCfgPayloadSuppression,'zxPwCTDMCfgConsecPktsInSynch':zxPwCTDMCfgConsecPktsInSynch,'zxPwCTDMCfgConsecMissPktsOutSynch':zxPwCTDMCfgConsecMissPktsOutSynch,'zxPwCTDMCfgSetUp2SynchTimeOut':zxPwCTDMCfgSetUp2SynchTimeOut,'zxPwCTDMCfgPktReplacePolicy':zxPwCTDMCfgPktReplacePolicy,'zxPwCTDMCfgAvePktLossTimeWindow':zxPwCTDMCfgAvePktLossTimeWindow,'zxPwCTDMCfgExcessivePktLossThreshold':zxPwCTDMCfgExcessivePktLossThreshold,'zxPwCTDMCfgAlarmThreshold':zxPwCTDMCfgAlarmThreshold,'zxPwCTDMCfgClearAlarmThreshold':zxPwCTDMCfgClearAlarmThreshold,'zxPwCTDMCfgMissingPktsToSes':zxPwCTDMCfgMissingPktsToSes,'zxPwCTDMCfgTimestampMode':zxPwCTDMCfgTimestampMode,'zxPwCTDMCfgQueueSize':zxPwCTDMCfgQueueSize,'zxPwCTDMCfgName':zxPwCTDMCfgName,'zxPwCTDMCfgSSRC':zxPwCTDMCfgSSRC,'zxPwCTDMCfgStorageType':zxPwCTDMCfgStorageType,'zxPwCTDMGlobalObjects':zxPwCTDMGlobalObjects,'zxPwCTDMCompatible':zxPwCTDMCompatible})