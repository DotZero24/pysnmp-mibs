_B3='ds1FarEndNGroup'
_B2='dsx1LineStatusChange'
_B1='dsx1LineImpedance'
_B0='dsx1ChanMappedIfIndex'
_A_='dsx1LineStatusChangeTrapEnable'
_Az='dsx1FracIfIndex'
_Ay='dsx1IfIndex'
_Ax='dsx1FarEndTotalDMs'
_Aw='dsx1FarEndIntervalDMs'
_Av='dsx1FarEndCurrentDMs'
_Au='dsx1TotalDMs'
_At='dsx1IntervalDMs'
_As='dsx1CurrentDMs'
_Ar='notApplicable'
_Aq='DisplayString'
_Ap='ds1NearEndOptionalTrapGroup'
_Ao='ds1FarEndGroup'
_An='dsx1LineBuildOut'
_Am='dsx1LineMode'
_Al='dsx1LineStatusLastChange'
_Ak='dsx1FarEndTotalBESs'
_Aj='dsx1FarEndTotalPCVs'
_Ai='dsx1FarEndTotalLESs'
_Ah='dsx1FarEndTotalCSSs'
_Ag='dsx1FarEndTotalUASs'
_Af='dsx1FarEndTotalSEFSs'
_Ae='dsx1FarEndTotalSESs'
_Ad='dsx1FarEndTotalESs'
_Ac='dsx1FarEndIntervalValidData'
_Ab='dsx1FarEndIntervalBESs'
_Aa='dsx1FarEndIntervalPCVs'
_AZ='dsx1FarEndIntervalLESs'
_AY='dsx1FarEndIntervalCSSs'
_AX='dsx1FarEndIntervalUASs'
_AW='dsx1FarEndIntervalSEFSs'
_AV='dsx1FarEndIntervalSESs'
_AU='dsx1FarEndIntervalESs'
_AT='dsx1FarEndInvalidIntervals'
_AS='dsx1FarEndCurrentBESs'
_AR='dsx1FarEndCurrentPCVs'
_AQ='dsx1FarEndCurrentLESs'
_AP='dsx1FarEndCurrentCSSs'
_AO='dsx1FarEndCurrentUASs'
_AN='dsx1FarEndCurrentSEFSs'
_AM='dsx1FarEndCurrentSESs'
_AL='dsx1FarEndCurrentESs'
_AK='dsx1FarEndValidIntervals'
_AJ='dsx1FarEndTimeElapsed'
_AI='dsx1TotalLCVs'
_AH='dsx1TotalBESs'
_AG='dsx1TotalLESs'
_AF='dsx1TotalPCVs'
_AE='dsx1TotalCSSs'
_AD='dsx1TotalSEFSs'
_AC='dsx1IntervalValidData'
_AB='dsx1IntervalLCVs'
_AA='dsx1IntervalBESs'
_A9='dsx1IntervalLESs'
_A8='dsx1IntervalPCVs'
_A7='dsx1IntervalCSSs'
_A6='dsx1IntervalSEFSs'
_A5='dsx1CurrentLCVs'
_A4='dsx1CurrentBESs'
_A3='dsx1CurrentLESs'
_A2='dsx1CurrentPCVs'
_A1='dsx1CurrentCSSs'
_A0='dsx1CurrentSEFSs'
_z='dsx1FracNumber'
_y='dsx1FracIndex'
_x='other'
_w='ds1NearEndStatGroup'
_v='ds1NearEndCfgGroup'
_u='ds1NearEndConfigurationGroup'
_t='ds1ChanMappingGroup'
_s='ds1TransStatsGroup'
_r='ds1NearEndOptionalConfigGroup'
_q='ds1NearEndConfigGroup'
_p='dsx1TotalUASs'
_o='dsx1TotalSESs'
_n='dsx1TotalESs'
_m='dsx1IntervalUASs'
_l='dsx1IntervalSESs'
_k='dsx1IntervalESs'
_j='dsx1CurrentUASs'
_i='dsx1CurrentSESs'
_h='dsx1CurrentESs'
_g='dsx1LoopbackStatus'
_f='dsx1LineLength'
_e='dsx1InvalidIntervals'
_d='dsx1Fdl'
_c='dsx1LoopbackConfig'
_b='dsx1CircuitIdentifier'
_a='dsx1ValidIntervals'
_Z='dsx1TimeElapsed'
_Y='dsx1FarEndTotalIndex'
_X='dsx1FarEndIntervalNumber'
_W='dsx1FarEndIntervalIndex'
_V='dsx1FarEndCurrentIndex'
_U='dsx1TotalIndex'
_T='dsx1IntervalNumber'
_S='dsx1IntervalIndex'
_R='dsx1CurrentIndex'
_Q='ds1DS2Group'
_P='dsx1Channelization'
_O='dsx1TransmitClockSource'
_N='dsx1SignalMode'
_M='dsx1SendCode'
_L='dsx1LineCoding'
_K='dsx1LineType'
_J='dsx1Ds1ChannelNumber'
_I='dsx1LineStatus'
_H='dsx1LineIndex'
_G='ds1NearEndStatisticsGroup'
_F='read-write'
_E='deprecated'
_D='Integer32'
_C='read-only'
_B='current'
_A='DS1-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_Aq,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
ds1=ModuleIdentity((1,3,6,1,2,1,10,18))
if mibBuilder.loadTexts:ds1.setRevisions(('2007-03-05 00:00','2004-09-09 00:00','1998-08-01 18:30','1993-01-25 20:28'))
_Dsx1ConfigTable_Object=MibTable
dsx1ConfigTable=_Dsx1ConfigTable_Object((1,3,6,1,2,1,10,18,6))
if mibBuilder.loadTexts:dsx1ConfigTable.setStatus(_B)
_Dsx1ConfigEntry_Object=MibTableRow
dsx1ConfigEntry=_Dsx1ConfigEntry_Object((1,3,6,1,2,1,10,18,6,1))
dsx1ConfigEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dsx1ConfigEntry.setStatus(_B)
_Dsx1LineIndex_Type=InterfaceIndex
_Dsx1LineIndex_Object=MibTableColumn
dsx1LineIndex=_Dsx1LineIndex_Object((1,3,6,1,2,1,10,18,6,1,1),_Dsx1LineIndex_Type())
dsx1LineIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1LineIndex.setStatus(_B)
_Dsx1IfIndex_Type=InterfaceIndex
_Dsx1IfIndex_Object=MibTableColumn
dsx1IfIndex=_Dsx1IfIndex_Object((1,3,6,1,2,1,10,18,6,1,2),_Dsx1IfIndex_Type())
dsx1IfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IfIndex.setStatus(_E)
class _Dsx1TimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_Dsx1TimeElapsed_Type.__name__=_D
_Dsx1TimeElapsed_Object=MibTableColumn
dsx1TimeElapsed=_Dsx1TimeElapsed_Object((1,3,6,1,2,1,10,18,6,1,3),_Dsx1TimeElapsed_Type())
dsx1TimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TimeElapsed.setStatus(_B)
class _Dsx1ValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_Dsx1ValidIntervals_Type.__name__=_D
_Dsx1ValidIntervals_Object=MibTableColumn
dsx1ValidIntervals=_Dsx1ValidIntervals_Object((1,3,6,1,2,1,10,18,6,1,4),_Dsx1ValidIntervals_Type())
dsx1ValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1ValidIntervals.setStatus(_B)
class _Dsx1LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,16)));namedValues=NamedValues(*((_x,1),('dsx1ESF',2),('dsx1D4',3),('dsx1E1',4),('dsx1E1CRC',5),('dsx1E1MF',6),('dsx1E1CRCMF',7),('dsx1Unframed',8),('dsx1E1Unframed',9),('dsx1DS2M12',10),('dsx1E2',11),('dsx1E1Q50',12),('dsx1E1Q50CRC',13),('dsx1J1ESF',14),('dsx1J1Unframed',16)))
_Dsx1LineType_Type.__name__=_D
_Dsx1LineType_Object=MibTableColumn
dsx1LineType=_Dsx1LineType_Object((1,3,6,1,2,1,10,18,6,1,5),_Dsx1LineType_Type())
dsx1LineType.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1LineType.setStatus(_B)
class _Dsx1LineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('dsx1JBZS',1),('dsx1B8ZS',2),('dsx1HDB3',3),('dsx1ZBTSI',4),('dsx1AMI',5),(_x,6),('dsx1B6ZS',7)))
_Dsx1LineCoding_Type.__name__=_D
_Dsx1LineCoding_Object=MibTableColumn
dsx1LineCoding=_Dsx1LineCoding_Object((1,3,6,1,2,1,10,18,6,1,6),_Dsx1LineCoding_Type())
dsx1LineCoding.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1LineCoding.setStatus(_B)
class _Dsx1SendCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('dsx1SendNoCode',1),('dsx1SendLineCode',2),('dsx1SendPayloadCode',3),('dsx1SendResetCode',4),('dsx1SendQRS',5),('dsx1Send511Pattern',6),('dsx1Send3in24Pattern',7),('dsx1SendOtherTestPattern',8)))
_Dsx1SendCode_Type.__name__=_D
_Dsx1SendCode_Object=MibTableColumn
dsx1SendCode=_Dsx1SendCode_Object((1,3,6,1,2,1,10,18,6,1,7),_Dsx1SendCode_Type())
dsx1SendCode.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1SendCode.setStatus(_B)
class _Dsx1CircuitIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Dsx1CircuitIdentifier_Type.__name__=_Aq
_Dsx1CircuitIdentifier_Object=MibTableColumn
dsx1CircuitIdentifier=_Dsx1CircuitIdentifier_Object((1,3,6,1,2,1,10,18,6,1,8),_Dsx1CircuitIdentifier_Type())
dsx1CircuitIdentifier.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1CircuitIdentifier.setStatus(_B)
class _Dsx1LoopbackConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dsx1NoLoop',1),('dsx1PayloadLoop',2),('dsx1LineLoop',3),('dsx1OtherLoop',4),('dsx1InwardLoop',5),('dsx1DualLoop',6)))
_Dsx1LoopbackConfig_Type.__name__=_D
_Dsx1LoopbackConfig_Object=MibTableColumn
dsx1LoopbackConfig=_Dsx1LoopbackConfig_Object((1,3,6,1,2,1,10,18,6,1,9),_Dsx1LoopbackConfig_Type())
dsx1LoopbackConfig.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1LoopbackConfig.setStatus(_B)
class _Dsx1LineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,131071))
_Dsx1LineStatus_Type.__name__=_D
_Dsx1LineStatus_Object=MibTableColumn
dsx1LineStatus=_Dsx1LineStatus_Object((1,3,6,1,2,1,10,18,6,1,10),_Dsx1LineStatus_Type())
dsx1LineStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1LineStatus.setStatus(_B)
class _Dsx1SignalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('robbedBit',2),('bitOriented',3),('messageOriented',4),(_x,5)))
_Dsx1SignalMode_Type.__name__=_D
_Dsx1SignalMode_Object=MibTableColumn
dsx1SignalMode=_Dsx1SignalMode_Object((1,3,6,1,2,1,10,18,6,1,11),_Dsx1SignalMode_Type())
dsx1SignalMode.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1SignalMode.setStatus(_B)
class _Dsx1TransmitClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2),('throughTiming',3),('adaptive',4)))
_Dsx1TransmitClockSource_Type.__name__=_D
_Dsx1TransmitClockSource_Object=MibTableColumn
dsx1TransmitClockSource=_Dsx1TransmitClockSource_Object((1,3,6,1,2,1,10,18,6,1,12),_Dsx1TransmitClockSource_Type())
dsx1TransmitClockSource.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1TransmitClockSource.setStatus(_B)
class _Dsx1Fdl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Dsx1Fdl_Type.__name__=_D
_Dsx1Fdl_Object=MibTableColumn
dsx1Fdl=_Dsx1Fdl_Object((1,3,6,1,2,1,10,18,6,1,13),_Dsx1Fdl_Type())
dsx1Fdl.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1Fdl.setStatus(_B)
class _Dsx1InvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_Dsx1InvalidIntervals_Type.__name__=_D
_Dsx1InvalidIntervals_Object=MibTableColumn
dsx1InvalidIntervals=_Dsx1InvalidIntervals_Object((1,3,6,1,2,1,10,18,6,1,14),_Dsx1InvalidIntervals_Type())
dsx1InvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1InvalidIntervals.setStatus(_B)
class _Dsx1LineLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64000))
_Dsx1LineLength_Type.__name__=_D
_Dsx1LineLength_Object=MibTableColumn
dsx1LineLength=_Dsx1LineLength_Object((1,3,6,1,2,1,10,18,6,1,15),_Dsx1LineLength_Type())
dsx1LineLength.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1LineLength.setStatus(_B)
if mibBuilder.loadTexts:dsx1LineLength.setUnits('meters')
_Dsx1LineStatusLastChange_Type=TimeStamp
_Dsx1LineStatusLastChange_Object=MibTableColumn
dsx1LineStatusLastChange=_Dsx1LineStatusLastChange_Object((1,3,6,1,2,1,10,18,6,1,16),_Dsx1LineStatusLastChange_Type())
dsx1LineStatusLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1LineStatusLastChange.setStatus(_B)
class _Dsx1LineStatusChangeTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Dsx1LineStatusChangeTrapEnable_Type.__name__=_D
_Dsx1LineStatusChangeTrapEnable_Object=MibTableColumn
dsx1LineStatusChangeTrapEnable=_Dsx1LineStatusChangeTrapEnable_Object((1,3,6,1,2,1,10,18,6,1,17),_Dsx1LineStatusChangeTrapEnable_Type())
dsx1LineStatusChangeTrapEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1LineStatusChangeTrapEnable.setStatus(_B)
class _Dsx1LoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_Dsx1LoopbackStatus_Type.__name__=_D
_Dsx1LoopbackStatus_Object=MibTableColumn
dsx1LoopbackStatus=_Dsx1LoopbackStatus_Object((1,3,6,1,2,1,10,18,6,1,18),_Dsx1LoopbackStatus_Type())
dsx1LoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1LoopbackStatus.setStatus(_B)
class _Dsx1Ds1ChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_Dsx1Ds1ChannelNumber_Type.__name__=_D
_Dsx1Ds1ChannelNumber_Object=MibTableColumn
dsx1Ds1ChannelNumber=_Dsx1Ds1ChannelNumber_Object((1,3,6,1,2,1,10,18,6,1,19),_Dsx1Ds1ChannelNumber_Type())
dsx1Ds1ChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1Ds1ChannelNumber.setStatus(_B)
class _Dsx1Channelization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('enabledDs0',2),('enabledDs1',3)))
_Dsx1Channelization_Type.__name__=_D
_Dsx1Channelization_Object=MibTableColumn
dsx1Channelization=_Dsx1Channelization_Object((1,3,6,1,2,1,10,18,6,1,20),_Dsx1Channelization_Type())
dsx1Channelization.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1Channelization.setStatus(_B)
class _Dsx1LineMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('csu',1),('dsu',2)))
_Dsx1LineMode_Type.__name__=_D
_Dsx1LineMode_Object=MibTableColumn
dsx1LineMode=_Dsx1LineMode_Object((1,3,6,1,2,1,10,18,6,1,21),_Dsx1LineMode_Type())
dsx1LineMode.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1LineMode.setStatus(_B)
class _Dsx1LineBuildOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Ar,1),('neg75dB',2),('neg15dB',3),('neg225dB',4),('zerodB',5)))
_Dsx1LineBuildOut_Type.__name__=_D
_Dsx1LineBuildOut_Object=MibTableColumn
dsx1LineBuildOut=_Dsx1LineBuildOut_Object((1,3,6,1,2,1,10,18,6,1,22),_Dsx1LineBuildOut_Type())
dsx1LineBuildOut.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1LineBuildOut.setStatus(_B)
class _Dsx1LineImpedance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Ar,1),('unbalanced75ohms',2),('balanced100ohms',3),('balanced120ohms',4)))
_Dsx1LineImpedance_Type.__name__=_D
_Dsx1LineImpedance_Object=MibTableColumn
dsx1LineImpedance=_Dsx1LineImpedance_Object((1,3,6,1,2,1,10,18,6,1,23),_Dsx1LineImpedance_Type())
dsx1LineImpedance.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1LineImpedance.setStatus(_B)
_Dsx1CurrentTable_Object=MibTable
dsx1CurrentTable=_Dsx1CurrentTable_Object((1,3,6,1,2,1,10,18,7))
if mibBuilder.loadTexts:dsx1CurrentTable.setStatus(_B)
_Dsx1CurrentEntry_Object=MibTableRow
dsx1CurrentEntry=_Dsx1CurrentEntry_Object((1,3,6,1,2,1,10,18,7,1))
dsx1CurrentEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:dsx1CurrentEntry.setStatus(_B)
_Dsx1CurrentIndex_Type=InterfaceIndex
_Dsx1CurrentIndex_Object=MibTableColumn
dsx1CurrentIndex=_Dsx1CurrentIndex_Object((1,3,6,1,2,1,10,18,7,1,1),_Dsx1CurrentIndex_Type())
dsx1CurrentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentIndex.setStatus(_B)
_Dsx1CurrentESs_Type=PerfCurrentCount
_Dsx1CurrentESs_Object=MibTableColumn
dsx1CurrentESs=_Dsx1CurrentESs_Object((1,3,6,1,2,1,10,18,7,1,2),_Dsx1CurrentESs_Type())
dsx1CurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentESs.setStatus(_B)
_Dsx1CurrentSESs_Type=PerfCurrentCount
_Dsx1CurrentSESs_Object=MibTableColumn
dsx1CurrentSESs=_Dsx1CurrentSESs_Object((1,3,6,1,2,1,10,18,7,1,3),_Dsx1CurrentSESs_Type())
dsx1CurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentSESs.setStatus(_B)
_Dsx1CurrentSEFSs_Type=PerfCurrentCount
_Dsx1CurrentSEFSs_Object=MibTableColumn
dsx1CurrentSEFSs=_Dsx1CurrentSEFSs_Object((1,3,6,1,2,1,10,18,7,1,4),_Dsx1CurrentSEFSs_Type())
dsx1CurrentSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentSEFSs.setStatus(_B)
_Dsx1CurrentUASs_Type=PerfCurrentCount
_Dsx1CurrentUASs_Object=MibTableColumn
dsx1CurrentUASs=_Dsx1CurrentUASs_Object((1,3,6,1,2,1,10,18,7,1,5),_Dsx1CurrentUASs_Type())
dsx1CurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentUASs.setStatus(_B)
_Dsx1CurrentCSSs_Type=PerfCurrentCount
_Dsx1CurrentCSSs_Object=MibTableColumn
dsx1CurrentCSSs=_Dsx1CurrentCSSs_Object((1,3,6,1,2,1,10,18,7,1,6),_Dsx1CurrentCSSs_Type())
dsx1CurrentCSSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentCSSs.setStatus(_B)
_Dsx1CurrentPCVs_Type=PerfCurrentCount
_Dsx1CurrentPCVs_Object=MibTableColumn
dsx1CurrentPCVs=_Dsx1CurrentPCVs_Object((1,3,6,1,2,1,10,18,7,1,7),_Dsx1CurrentPCVs_Type())
dsx1CurrentPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentPCVs.setStatus(_B)
_Dsx1CurrentLESs_Type=PerfCurrentCount
_Dsx1CurrentLESs_Object=MibTableColumn
dsx1CurrentLESs=_Dsx1CurrentLESs_Object((1,3,6,1,2,1,10,18,7,1,8),_Dsx1CurrentLESs_Type())
dsx1CurrentLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentLESs.setStatus(_B)
_Dsx1CurrentBESs_Type=PerfCurrentCount
_Dsx1CurrentBESs_Object=MibTableColumn
dsx1CurrentBESs=_Dsx1CurrentBESs_Object((1,3,6,1,2,1,10,18,7,1,9),_Dsx1CurrentBESs_Type())
dsx1CurrentBESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentBESs.setStatus(_B)
_Dsx1CurrentDMs_Type=PerfCurrentCount
_Dsx1CurrentDMs_Object=MibTableColumn
dsx1CurrentDMs=_Dsx1CurrentDMs_Object((1,3,6,1,2,1,10,18,7,1,10),_Dsx1CurrentDMs_Type())
dsx1CurrentDMs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentDMs.setStatus(_E)
_Dsx1CurrentLCVs_Type=PerfCurrentCount
_Dsx1CurrentLCVs_Object=MibTableColumn
dsx1CurrentLCVs=_Dsx1CurrentLCVs_Object((1,3,6,1,2,1,10,18,7,1,11),_Dsx1CurrentLCVs_Type())
dsx1CurrentLCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentLCVs.setStatus(_B)
_Dsx1IntervalTable_Object=MibTable
dsx1IntervalTable=_Dsx1IntervalTable_Object((1,3,6,1,2,1,10,18,8))
if mibBuilder.loadTexts:dsx1IntervalTable.setStatus(_B)
_Dsx1IntervalEntry_Object=MibTableRow
dsx1IntervalEntry=_Dsx1IntervalEntry_Object((1,3,6,1,2,1,10,18,8,1))
dsx1IntervalEntry.setIndexNames((0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:dsx1IntervalEntry.setStatus(_B)
_Dsx1IntervalIndex_Type=InterfaceIndex
_Dsx1IntervalIndex_Object=MibTableColumn
dsx1IntervalIndex=_Dsx1IntervalIndex_Object((1,3,6,1,2,1,10,18,8,1,1),_Dsx1IntervalIndex_Type())
dsx1IntervalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalIndex.setStatus(_B)
class _Dsx1IntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_Dsx1IntervalNumber_Type.__name__=_D
_Dsx1IntervalNumber_Object=MibTableColumn
dsx1IntervalNumber=_Dsx1IntervalNumber_Object((1,3,6,1,2,1,10,18,8,1,2),_Dsx1IntervalNumber_Type())
dsx1IntervalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalNumber.setStatus(_B)
_Dsx1IntervalESs_Type=PerfIntervalCount
_Dsx1IntervalESs_Object=MibTableColumn
dsx1IntervalESs=_Dsx1IntervalESs_Object((1,3,6,1,2,1,10,18,8,1,3),_Dsx1IntervalESs_Type())
dsx1IntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalESs.setStatus(_B)
_Dsx1IntervalSESs_Type=PerfIntervalCount
_Dsx1IntervalSESs_Object=MibTableColumn
dsx1IntervalSESs=_Dsx1IntervalSESs_Object((1,3,6,1,2,1,10,18,8,1,4),_Dsx1IntervalSESs_Type())
dsx1IntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalSESs.setStatus(_B)
_Dsx1IntervalSEFSs_Type=PerfIntervalCount
_Dsx1IntervalSEFSs_Object=MibTableColumn
dsx1IntervalSEFSs=_Dsx1IntervalSEFSs_Object((1,3,6,1,2,1,10,18,8,1,5),_Dsx1IntervalSEFSs_Type())
dsx1IntervalSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalSEFSs.setStatus(_B)
_Dsx1IntervalUASs_Type=PerfIntervalCount
_Dsx1IntervalUASs_Object=MibTableColumn
dsx1IntervalUASs=_Dsx1IntervalUASs_Object((1,3,6,1,2,1,10,18,8,1,6),_Dsx1IntervalUASs_Type())
dsx1IntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalUASs.setStatus(_B)
_Dsx1IntervalCSSs_Type=PerfIntervalCount
_Dsx1IntervalCSSs_Object=MibTableColumn
dsx1IntervalCSSs=_Dsx1IntervalCSSs_Object((1,3,6,1,2,1,10,18,8,1,7),_Dsx1IntervalCSSs_Type())
dsx1IntervalCSSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalCSSs.setStatus(_B)
_Dsx1IntervalPCVs_Type=PerfIntervalCount
_Dsx1IntervalPCVs_Object=MibTableColumn
dsx1IntervalPCVs=_Dsx1IntervalPCVs_Object((1,3,6,1,2,1,10,18,8,1,8),_Dsx1IntervalPCVs_Type())
dsx1IntervalPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalPCVs.setStatus(_B)
_Dsx1IntervalLESs_Type=PerfIntervalCount
_Dsx1IntervalLESs_Object=MibTableColumn
dsx1IntervalLESs=_Dsx1IntervalLESs_Object((1,3,6,1,2,1,10,18,8,1,9),_Dsx1IntervalLESs_Type())
dsx1IntervalLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalLESs.setStatus(_B)
_Dsx1IntervalBESs_Type=PerfIntervalCount
_Dsx1IntervalBESs_Object=MibTableColumn
dsx1IntervalBESs=_Dsx1IntervalBESs_Object((1,3,6,1,2,1,10,18,8,1,10),_Dsx1IntervalBESs_Type())
dsx1IntervalBESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalBESs.setStatus(_B)
_Dsx1IntervalDMs_Type=PerfIntervalCount
_Dsx1IntervalDMs_Object=MibTableColumn
dsx1IntervalDMs=_Dsx1IntervalDMs_Object((1,3,6,1,2,1,10,18,8,1,11),_Dsx1IntervalDMs_Type())
dsx1IntervalDMs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalDMs.setStatus(_E)
_Dsx1IntervalLCVs_Type=PerfIntervalCount
_Dsx1IntervalLCVs_Object=MibTableColumn
dsx1IntervalLCVs=_Dsx1IntervalLCVs_Object((1,3,6,1,2,1,10,18,8,1,12),_Dsx1IntervalLCVs_Type())
dsx1IntervalLCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalLCVs.setStatus(_B)
_Dsx1IntervalValidData_Type=TruthValue
_Dsx1IntervalValidData_Object=MibTableColumn
dsx1IntervalValidData=_Dsx1IntervalValidData_Object((1,3,6,1,2,1,10,18,8,1,13),_Dsx1IntervalValidData_Type())
dsx1IntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalValidData.setStatus(_B)
_Dsx1TotalTable_Object=MibTable
dsx1TotalTable=_Dsx1TotalTable_Object((1,3,6,1,2,1,10,18,9))
if mibBuilder.loadTexts:dsx1TotalTable.setStatus(_B)
_Dsx1TotalEntry_Object=MibTableRow
dsx1TotalEntry=_Dsx1TotalEntry_Object((1,3,6,1,2,1,10,18,9,1))
dsx1TotalEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:dsx1TotalEntry.setStatus(_B)
_Dsx1TotalIndex_Type=InterfaceIndex
_Dsx1TotalIndex_Object=MibTableColumn
dsx1TotalIndex=_Dsx1TotalIndex_Object((1,3,6,1,2,1,10,18,9,1,1),_Dsx1TotalIndex_Type())
dsx1TotalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalIndex.setStatus(_B)
_Dsx1TotalESs_Type=PerfTotalCount
_Dsx1TotalESs_Object=MibTableColumn
dsx1TotalESs=_Dsx1TotalESs_Object((1,3,6,1,2,1,10,18,9,1,2),_Dsx1TotalESs_Type())
dsx1TotalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalESs.setStatus(_B)
_Dsx1TotalSESs_Type=PerfTotalCount
_Dsx1TotalSESs_Object=MibTableColumn
dsx1TotalSESs=_Dsx1TotalSESs_Object((1,3,6,1,2,1,10,18,9,1,3),_Dsx1TotalSESs_Type())
dsx1TotalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalSESs.setStatus(_B)
_Dsx1TotalSEFSs_Type=PerfTotalCount
_Dsx1TotalSEFSs_Object=MibTableColumn
dsx1TotalSEFSs=_Dsx1TotalSEFSs_Object((1,3,6,1,2,1,10,18,9,1,4),_Dsx1TotalSEFSs_Type())
dsx1TotalSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalSEFSs.setStatus(_B)
_Dsx1TotalUASs_Type=PerfTotalCount
_Dsx1TotalUASs_Object=MibTableColumn
dsx1TotalUASs=_Dsx1TotalUASs_Object((1,3,6,1,2,1,10,18,9,1,5),_Dsx1TotalUASs_Type())
dsx1TotalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalUASs.setStatus(_B)
_Dsx1TotalCSSs_Type=PerfTotalCount
_Dsx1TotalCSSs_Object=MibTableColumn
dsx1TotalCSSs=_Dsx1TotalCSSs_Object((1,3,6,1,2,1,10,18,9,1,6),_Dsx1TotalCSSs_Type())
dsx1TotalCSSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalCSSs.setStatus(_B)
_Dsx1TotalPCVs_Type=PerfTotalCount
_Dsx1TotalPCVs_Object=MibTableColumn
dsx1TotalPCVs=_Dsx1TotalPCVs_Object((1,3,6,1,2,1,10,18,9,1,7),_Dsx1TotalPCVs_Type())
dsx1TotalPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalPCVs.setStatus(_B)
_Dsx1TotalLESs_Type=PerfTotalCount
_Dsx1TotalLESs_Object=MibTableColumn
dsx1TotalLESs=_Dsx1TotalLESs_Object((1,3,6,1,2,1,10,18,9,1,8),_Dsx1TotalLESs_Type())
dsx1TotalLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalLESs.setStatus(_B)
_Dsx1TotalBESs_Type=PerfTotalCount
_Dsx1TotalBESs_Object=MibTableColumn
dsx1TotalBESs=_Dsx1TotalBESs_Object((1,3,6,1,2,1,10,18,9,1,9),_Dsx1TotalBESs_Type())
dsx1TotalBESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalBESs.setStatus(_B)
_Dsx1TotalDMs_Type=PerfTotalCount
_Dsx1TotalDMs_Object=MibTableColumn
dsx1TotalDMs=_Dsx1TotalDMs_Object((1,3,6,1,2,1,10,18,9,1,10),_Dsx1TotalDMs_Type())
dsx1TotalDMs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalDMs.setStatus(_E)
_Dsx1TotalLCVs_Type=PerfTotalCount
_Dsx1TotalLCVs_Object=MibTableColumn
dsx1TotalLCVs=_Dsx1TotalLCVs_Object((1,3,6,1,2,1,10,18,9,1,11),_Dsx1TotalLCVs_Type())
dsx1TotalLCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalLCVs.setStatus(_B)
_Dsx1FarEndCurrentTable_Object=MibTable
dsx1FarEndCurrentTable=_Dsx1FarEndCurrentTable_Object((1,3,6,1,2,1,10,18,10))
if mibBuilder.loadTexts:dsx1FarEndCurrentTable.setStatus(_B)
_Dsx1FarEndCurrentEntry_Object=MibTableRow
dsx1FarEndCurrentEntry=_Dsx1FarEndCurrentEntry_Object((1,3,6,1,2,1,10,18,10,1))
dsx1FarEndCurrentEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:dsx1FarEndCurrentEntry.setStatus(_B)
_Dsx1FarEndCurrentIndex_Type=InterfaceIndex
_Dsx1FarEndCurrentIndex_Object=MibTableColumn
dsx1FarEndCurrentIndex=_Dsx1FarEndCurrentIndex_Object((1,3,6,1,2,1,10,18,10,1,1),_Dsx1FarEndCurrentIndex_Type())
dsx1FarEndCurrentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentIndex.setStatus(_B)
class _Dsx1FarEndTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_Dsx1FarEndTimeElapsed_Type.__name__=_D
_Dsx1FarEndTimeElapsed_Object=MibTableColumn
dsx1FarEndTimeElapsed=_Dsx1FarEndTimeElapsed_Object((1,3,6,1,2,1,10,18,10,1,2),_Dsx1FarEndTimeElapsed_Type())
dsx1FarEndTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTimeElapsed.setStatus(_B)
class _Dsx1FarEndValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_Dsx1FarEndValidIntervals_Type.__name__=_D
_Dsx1FarEndValidIntervals_Object=MibTableColumn
dsx1FarEndValidIntervals=_Dsx1FarEndValidIntervals_Object((1,3,6,1,2,1,10,18,10,1,3),_Dsx1FarEndValidIntervals_Type())
dsx1FarEndValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndValidIntervals.setStatus(_B)
_Dsx1FarEndCurrentESs_Type=PerfCurrentCount
_Dsx1FarEndCurrentESs_Object=MibTableColumn
dsx1FarEndCurrentESs=_Dsx1FarEndCurrentESs_Object((1,3,6,1,2,1,10,18,10,1,4),_Dsx1FarEndCurrentESs_Type())
dsx1FarEndCurrentESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentESs.setStatus(_B)
_Dsx1FarEndCurrentSESs_Type=PerfCurrentCount
_Dsx1FarEndCurrentSESs_Object=MibTableColumn
dsx1FarEndCurrentSESs=_Dsx1FarEndCurrentSESs_Object((1,3,6,1,2,1,10,18,10,1,5),_Dsx1FarEndCurrentSESs_Type())
dsx1FarEndCurrentSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentSESs.setStatus(_B)
_Dsx1FarEndCurrentSEFSs_Type=PerfCurrentCount
_Dsx1FarEndCurrentSEFSs_Object=MibTableColumn
dsx1FarEndCurrentSEFSs=_Dsx1FarEndCurrentSEFSs_Object((1,3,6,1,2,1,10,18,10,1,6),_Dsx1FarEndCurrentSEFSs_Type())
dsx1FarEndCurrentSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentSEFSs.setStatus(_B)
_Dsx1FarEndCurrentUASs_Type=PerfCurrentCount
_Dsx1FarEndCurrentUASs_Object=MibTableColumn
dsx1FarEndCurrentUASs=_Dsx1FarEndCurrentUASs_Object((1,3,6,1,2,1,10,18,10,1,7),_Dsx1FarEndCurrentUASs_Type())
dsx1FarEndCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentUASs.setStatus(_B)
_Dsx1FarEndCurrentCSSs_Type=PerfCurrentCount
_Dsx1FarEndCurrentCSSs_Object=MibTableColumn
dsx1FarEndCurrentCSSs=_Dsx1FarEndCurrentCSSs_Object((1,3,6,1,2,1,10,18,10,1,8),_Dsx1FarEndCurrentCSSs_Type())
dsx1FarEndCurrentCSSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentCSSs.setStatus(_B)
_Dsx1FarEndCurrentLESs_Type=PerfCurrentCount
_Dsx1FarEndCurrentLESs_Object=MibTableColumn
dsx1FarEndCurrentLESs=_Dsx1FarEndCurrentLESs_Object((1,3,6,1,2,1,10,18,10,1,9),_Dsx1FarEndCurrentLESs_Type())
dsx1FarEndCurrentLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentLESs.setStatus(_B)
_Dsx1FarEndCurrentPCVs_Type=PerfCurrentCount
_Dsx1FarEndCurrentPCVs_Object=MibTableColumn
dsx1FarEndCurrentPCVs=_Dsx1FarEndCurrentPCVs_Object((1,3,6,1,2,1,10,18,10,1,10),_Dsx1FarEndCurrentPCVs_Type())
dsx1FarEndCurrentPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentPCVs.setStatus(_B)
_Dsx1FarEndCurrentBESs_Type=PerfCurrentCount
_Dsx1FarEndCurrentBESs_Object=MibTableColumn
dsx1FarEndCurrentBESs=_Dsx1FarEndCurrentBESs_Object((1,3,6,1,2,1,10,18,10,1,11),_Dsx1FarEndCurrentBESs_Type())
dsx1FarEndCurrentBESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentBESs.setStatus(_B)
_Dsx1FarEndCurrentDMs_Type=PerfCurrentCount
_Dsx1FarEndCurrentDMs_Object=MibTableColumn
dsx1FarEndCurrentDMs=_Dsx1FarEndCurrentDMs_Object((1,3,6,1,2,1,10,18,10,1,12),_Dsx1FarEndCurrentDMs_Type())
dsx1FarEndCurrentDMs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndCurrentDMs.setStatus(_E)
class _Dsx1FarEndInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_Dsx1FarEndInvalidIntervals_Type.__name__=_D
_Dsx1FarEndInvalidIntervals_Object=MibTableColumn
dsx1FarEndInvalidIntervals=_Dsx1FarEndInvalidIntervals_Object((1,3,6,1,2,1,10,18,10,1,13),_Dsx1FarEndInvalidIntervals_Type())
dsx1FarEndInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndInvalidIntervals.setStatus(_B)
_Dsx1FarEndIntervalTable_Object=MibTable
dsx1FarEndIntervalTable=_Dsx1FarEndIntervalTable_Object((1,3,6,1,2,1,10,18,11))
if mibBuilder.loadTexts:dsx1FarEndIntervalTable.setStatus(_B)
_Dsx1FarEndIntervalEntry_Object=MibTableRow
dsx1FarEndIntervalEntry=_Dsx1FarEndIntervalEntry_Object((1,3,6,1,2,1,10,18,11,1))
dsx1FarEndIntervalEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:dsx1FarEndIntervalEntry.setStatus(_B)
_Dsx1FarEndIntervalIndex_Type=InterfaceIndex
_Dsx1FarEndIntervalIndex_Object=MibTableColumn
dsx1FarEndIntervalIndex=_Dsx1FarEndIntervalIndex_Object((1,3,6,1,2,1,10,18,11,1,1),_Dsx1FarEndIntervalIndex_Type())
dsx1FarEndIntervalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalIndex.setStatus(_B)
class _Dsx1FarEndIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_Dsx1FarEndIntervalNumber_Type.__name__=_D
_Dsx1FarEndIntervalNumber_Object=MibTableColumn
dsx1FarEndIntervalNumber=_Dsx1FarEndIntervalNumber_Object((1,3,6,1,2,1,10,18,11,1,2),_Dsx1FarEndIntervalNumber_Type())
dsx1FarEndIntervalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalNumber.setStatus(_B)
_Dsx1FarEndIntervalESs_Type=PerfIntervalCount
_Dsx1FarEndIntervalESs_Object=MibTableColumn
dsx1FarEndIntervalESs=_Dsx1FarEndIntervalESs_Object((1,3,6,1,2,1,10,18,11,1,3),_Dsx1FarEndIntervalESs_Type())
dsx1FarEndIntervalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalESs.setStatus(_B)
_Dsx1FarEndIntervalSESs_Type=PerfIntervalCount
_Dsx1FarEndIntervalSESs_Object=MibTableColumn
dsx1FarEndIntervalSESs=_Dsx1FarEndIntervalSESs_Object((1,3,6,1,2,1,10,18,11,1,4),_Dsx1FarEndIntervalSESs_Type())
dsx1FarEndIntervalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalSESs.setStatus(_B)
_Dsx1FarEndIntervalSEFSs_Type=PerfIntervalCount
_Dsx1FarEndIntervalSEFSs_Object=MibTableColumn
dsx1FarEndIntervalSEFSs=_Dsx1FarEndIntervalSEFSs_Object((1,3,6,1,2,1,10,18,11,1,5),_Dsx1FarEndIntervalSEFSs_Type())
dsx1FarEndIntervalSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalSEFSs.setStatus(_B)
_Dsx1FarEndIntervalUASs_Type=PerfIntervalCount
_Dsx1FarEndIntervalUASs_Object=MibTableColumn
dsx1FarEndIntervalUASs=_Dsx1FarEndIntervalUASs_Object((1,3,6,1,2,1,10,18,11,1,6),_Dsx1FarEndIntervalUASs_Type())
dsx1FarEndIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalUASs.setStatus(_B)
_Dsx1FarEndIntervalCSSs_Type=PerfIntervalCount
_Dsx1FarEndIntervalCSSs_Object=MibTableColumn
dsx1FarEndIntervalCSSs=_Dsx1FarEndIntervalCSSs_Object((1,3,6,1,2,1,10,18,11,1,7),_Dsx1FarEndIntervalCSSs_Type())
dsx1FarEndIntervalCSSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalCSSs.setStatus(_B)
_Dsx1FarEndIntervalLESs_Type=PerfIntervalCount
_Dsx1FarEndIntervalLESs_Object=MibTableColumn
dsx1FarEndIntervalLESs=_Dsx1FarEndIntervalLESs_Object((1,3,6,1,2,1,10,18,11,1,8),_Dsx1FarEndIntervalLESs_Type())
dsx1FarEndIntervalLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalLESs.setStatus(_B)
_Dsx1FarEndIntervalPCVs_Type=PerfIntervalCount
_Dsx1FarEndIntervalPCVs_Object=MibTableColumn
dsx1FarEndIntervalPCVs=_Dsx1FarEndIntervalPCVs_Object((1,3,6,1,2,1,10,18,11,1,9),_Dsx1FarEndIntervalPCVs_Type())
dsx1FarEndIntervalPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalPCVs.setStatus(_B)
_Dsx1FarEndIntervalBESs_Type=PerfIntervalCount
_Dsx1FarEndIntervalBESs_Object=MibTableColumn
dsx1FarEndIntervalBESs=_Dsx1FarEndIntervalBESs_Object((1,3,6,1,2,1,10,18,11,1,10),_Dsx1FarEndIntervalBESs_Type())
dsx1FarEndIntervalBESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalBESs.setStatus(_B)
_Dsx1FarEndIntervalDMs_Type=PerfIntervalCount
_Dsx1FarEndIntervalDMs_Object=MibTableColumn
dsx1FarEndIntervalDMs=_Dsx1FarEndIntervalDMs_Object((1,3,6,1,2,1,10,18,11,1,11),_Dsx1FarEndIntervalDMs_Type())
dsx1FarEndIntervalDMs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalDMs.setStatus(_E)
_Dsx1FarEndIntervalValidData_Type=TruthValue
_Dsx1FarEndIntervalValidData_Object=MibTableColumn
dsx1FarEndIntervalValidData=_Dsx1FarEndIntervalValidData_Object((1,3,6,1,2,1,10,18,11,1,12),_Dsx1FarEndIntervalValidData_Type())
dsx1FarEndIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndIntervalValidData.setStatus(_B)
_Dsx1FarEndTotalTable_Object=MibTable
dsx1FarEndTotalTable=_Dsx1FarEndTotalTable_Object((1,3,6,1,2,1,10,18,12))
if mibBuilder.loadTexts:dsx1FarEndTotalTable.setStatus(_B)
_Dsx1FarEndTotalEntry_Object=MibTableRow
dsx1FarEndTotalEntry=_Dsx1FarEndTotalEntry_Object((1,3,6,1,2,1,10,18,12,1))
dsx1FarEndTotalEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:dsx1FarEndTotalEntry.setStatus(_B)
_Dsx1FarEndTotalIndex_Type=InterfaceIndex
_Dsx1FarEndTotalIndex_Object=MibTableColumn
dsx1FarEndTotalIndex=_Dsx1FarEndTotalIndex_Object((1,3,6,1,2,1,10,18,12,1,1),_Dsx1FarEndTotalIndex_Type())
dsx1FarEndTotalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalIndex.setStatus(_B)
_Dsx1FarEndTotalESs_Type=PerfTotalCount
_Dsx1FarEndTotalESs_Object=MibTableColumn
dsx1FarEndTotalESs=_Dsx1FarEndTotalESs_Object((1,3,6,1,2,1,10,18,12,1,2),_Dsx1FarEndTotalESs_Type())
dsx1FarEndTotalESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalESs.setStatus(_B)
_Dsx1FarEndTotalSESs_Type=PerfTotalCount
_Dsx1FarEndTotalSESs_Object=MibTableColumn
dsx1FarEndTotalSESs=_Dsx1FarEndTotalSESs_Object((1,3,6,1,2,1,10,18,12,1,3),_Dsx1FarEndTotalSESs_Type())
dsx1FarEndTotalSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalSESs.setStatus(_B)
_Dsx1FarEndTotalSEFSs_Type=PerfTotalCount
_Dsx1FarEndTotalSEFSs_Object=MibTableColumn
dsx1FarEndTotalSEFSs=_Dsx1FarEndTotalSEFSs_Object((1,3,6,1,2,1,10,18,12,1,4),_Dsx1FarEndTotalSEFSs_Type())
dsx1FarEndTotalSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalSEFSs.setStatus(_B)
_Dsx1FarEndTotalUASs_Type=PerfTotalCount
_Dsx1FarEndTotalUASs_Object=MibTableColumn
dsx1FarEndTotalUASs=_Dsx1FarEndTotalUASs_Object((1,3,6,1,2,1,10,18,12,1,5),_Dsx1FarEndTotalUASs_Type())
dsx1FarEndTotalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalUASs.setStatus(_B)
_Dsx1FarEndTotalCSSs_Type=PerfTotalCount
_Dsx1FarEndTotalCSSs_Object=MibTableColumn
dsx1FarEndTotalCSSs=_Dsx1FarEndTotalCSSs_Object((1,3,6,1,2,1,10,18,12,1,6),_Dsx1FarEndTotalCSSs_Type())
dsx1FarEndTotalCSSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalCSSs.setStatus(_B)
_Dsx1FarEndTotalLESs_Type=PerfTotalCount
_Dsx1FarEndTotalLESs_Object=MibTableColumn
dsx1FarEndTotalLESs=_Dsx1FarEndTotalLESs_Object((1,3,6,1,2,1,10,18,12,1,7),_Dsx1FarEndTotalLESs_Type())
dsx1FarEndTotalLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalLESs.setStatus(_B)
_Dsx1FarEndTotalPCVs_Type=PerfTotalCount
_Dsx1FarEndTotalPCVs_Object=MibTableColumn
dsx1FarEndTotalPCVs=_Dsx1FarEndTotalPCVs_Object((1,3,6,1,2,1,10,18,12,1,8),_Dsx1FarEndTotalPCVs_Type())
dsx1FarEndTotalPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalPCVs.setStatus(_B)
_Dsx1FarEndTotalBESs_Type=PerfTotalCount
_Dsx1FarEndTotalBESs_Object=MibTableColumn
dsx1FarEndTotalBESs=_Dsx1FarEndTotalBESs_Object((1,3,6,1,2,1,10,18,12,1,9),_Dsx1FarEndTotalBESs_Type())
dsx1FarEndTotalBESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalBESs.setStatus(_B)
_Dsx1FarEndTotalDMs_Type=PerfTotalCount
_Dsx1FarEndTotalDMs_Object=MibTableColumn
dsx1FarEndTotalDMs=_Dsx1FarEndTotalDMs_Object((1,3,6,1,2,1,10,18,12,1,10),_Dsx1FarEndTotalDMs_Type())
dsx1FarEndTotalDMs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FarEndTotalDMs.setStatus(_E)
_Dsx1FracTable_Object=MibTable
dsx1FracTable=_Dsx1FracTable_Object((1,3,6,1,2,1,10,18,13))
if mibBuilder.loadTexts:dsx1FracTable.setStatus(_E)
_Dsx1FracEntry_Object=MibTableRow
dsx1FracEntry=_Dsx1FracEntry_Object((1,3,6,1,2,1,10,18,13,1))
dsx1FracEntry.setIndexNames((0,_A,_y),(0,_A,_z))
if mibBuilder.loadTexts:dsx1FracEntry.setStatus(_E)
class _Dsx1FracIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Dsx1FracIndex_Type.__name__=_D
_Dsx1FracIndex_Object=MibTableColumn
dsx1FracIndex=_Dsx1FracIndex_Object((1,3,6,1,2,1,10,18,13,1,1),_Dsx1FracIndex_Type())
dsx1FracIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FracIndex.setStatus(_E)
class _Dsx1FracNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_Dsx1FracNumber_Type.__name__=_D
_Dsx1FracNumber_Object=MibTableColumn
dsx1FracNumber=_Dsx1FracNumber_Object((1,3,6,1,2,1,10,18,13,1,2),_Dsx1FracNumber_Type())
dsx1FracNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1FracNumber.setStatus(_E)
class _Dsx1FracIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dsx1FracIfIndex_Type.__name__=_D
_Dsx1FracIfIndex_Object=MibTableColumn
dsx1FracIfIndex=_Dsx1FracIfIndex_Object((1,3,6,1,2,1,10,18,13,1,3),_Dsx1FracIfIndex_Type())
dsx1FracIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:dsx1FracIfIndex.setStatus(_E)
_Ds1Conformance_ObjectIdentity=ObjectIdentity
ds1Conformance=_Ds1Conformance_ObjectIdentity((1,3,6,1,2,1,10,18,14))
_Ds1Groups_ObjectIdentity=ObjectIdentity
ds1Groups=_Ds1Groups_ObjectIdentity((1,3,6,1,2,1,10,18,14,1))
_Ds1Compliances_ObjectIdentity=ObjectIdentity
ds1Compliances=_Ds1Compliances_ObjectIdentity((1,3,6,1,2,1,10,18,14,2))
_Ds1Traps_ObjectIdentity=ObjectIdentity
ds1Traps=_Ds1Traps_ObjectIdentity((1,3,6,1,2,1,10,18,15))
_Dsx1ChanMappingTable_Object=MibTable
dsx1ChanMappingTable=_Dsx1ChanMappingTable_Object((1,3,6,1,2,1,10,18,16))
if mibBuilder.loadTexts:dsx1ChanMappingTable.setStatus(_B)
_Dsx1ChanMappingEntry_Object=MibTableRow
dsx1ChanMappingEntry=_Dsx1ChanMappingEntry_Object((1,3,6,1,2,1,10,18,16,1))
dsx1ChanMappingEntry.setIndexNames((0,'IF-MIB','ifIndex'),(0,_A,_J))
if mibBuilder.loadTexts:dsx1ChanMappingEntry.setStatus(_B)
_Dsx1ChanMappedIfIndex_Type=InterfaceIndex
_Dsx1ChanMappedIfIndex_Object=MibTableColumn
dsx1ChanMappedIfIndex=_Dsx1ChanMappedIfIndex_Object((1,3,6,1,2,1,10,18,16,1,1),_Dsx1ChanMappedIfIndex_Type())
dsx1ChanMappedIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1ChanMappedIfIndex.setStatus(_B)
ds1NearEndConfigGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,1))
ds1NearEndConfigGroup.setObjects(*((_A,_H),(_A,_Z),(_A,_a),(_A,_K),(_A,_L),(_A,_M),(_A,_b),(_A,_c),(_A,_I),(_A,_N),(_A,_O),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_J),(_A,_P)))
if mibBuilder.loadTexts:ds1NearEndConfigGroup.setStatus(_E)
ds1NearEndStatisticsGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,2))
ds1NearEndStatisticsGroup.setObjects(*((_A,_R),(_A,_h),(_A,_i),(_A,_A0),(_A,_j),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_As),(_A,_A5),(_A,_S),(_A,_T),(_A,_k),(_A,_l),(_A,_A6),(_A,_m),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_At),(_A,_AB),(_A,_AC),(_A,_U),(_A,_n),(_A,_o),(_A,_AD),(_A,_p),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_Au),(_A,_AI)))
if mibBuilder.loadTexts:ds1NearEndStatisticsGroup.setStatus(_E)
ds1FarEndGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,3))
ds1FarEndGroup.setObjects(*((_A,_V),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_Av),(_A,_AT),(_A,_W),(_A,_X),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Aw),(_A,_Ac),(_A,_Y),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Ax)))
if mibBuilder.loadTexts:ds1FarEndGroup.setStatus(_E)
ds1DeprecatedGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,4))
ds1DeprecatedGroup.setObjects(*((_A,_Ay),(_A,_y),(_A,_z),(_A,_Az)))
if mibBuilder.loadTexts:ds1DeprecatedGroup.setStatus(_E)
ds1NearEndOptionalConfigGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,5))
ds1NearEndOptionalConfigGroup.setObjects(*((_A,_Al),(_A,_A_)))
if mibBuilder.loadTexts:ds1NearEndOptionalConfigGroup.setStatus(_B)
ds1DS2Group=ObjectGroup((1,3,6,1,2,1,10,18,14,1,6))
ds1DS2Group.setObjects(*((_A,_H),(_A,_K),(_A,_L),(_A,_M),(_A,_I),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ds1DS2Group.setStatus(_B)
ds1TransStatsGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,7))
ds1TransStatsGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ds1TransStatsGroup.setStatus(_B)
ds1ChanMappingGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,9))
ds1ChanMappingGroup.setObjects((_A,_B0))
if mibBuilder.loadTexts:ds1ChanMappingGroup.setStatus(_B)
ds1NearEndConfigurationGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,10))
ds1NearEndConfigurationGroup.setObjects(*((_A,_H),(_A,_Z),(_A,_a),(_A,_K),(_A,_L),(_A,_M),(_A,_b),(_A,_c),(_A,_I),(_A,_N),(_A,_O),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_J),(_A,_P),(_A,_Am),(_A,_An)))
if mibBuilder.loadTexts:ds1NearEndConfigurationGroup.setStatus(_E)
ds1NearEndCfgGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,11))
ds1NearEndCfgGroup.setObjects(*((_A,_H),(_A,_Z),(_A,_a),(_A,_K),(_A,_L),(_A,_M),(_A,_b),(_A,_c),(_A,_I),(_A,_N),(_A,_O),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_J),(_A,_P),(_A,_Am),(_A,_An),(_A,_B1)))
if mibBuilder.loadTexts:ds1NearEndCfgGroup.setStatus(_B)
ds1NearEndStatGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,12))
ds1NearEndStatGroup.setObjects(*((_A,_R),(_A,_h),(_A,_i),(_A,_A0),(_A,_j),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_S),(_A,_T),(_A,_k),(_A,_l),(_A,_A6),(_A,_m),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_U),(_A,_n),(_A,_o),(_A,_AD),(_A,_p),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:ds1NearEndStatGroup.setStatus(_B)
ds1FarEndNGroup=ObjectGroup((1,3,6,1,2,1,10,18,14,1,13))
ds1FarEndNGroup.setObjects(*((_A,_V),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_W),(_A,_X),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Y),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:ds1FarEndNGroup.setStatus(_B)
dsx1LineStatusChange=NotificationType((1,3,6,1,2,1,10,18,15,0,1))
dsx1LineStatusChange.setObjects(*((_A,_I),(_A,_Al)))
if mibBuilder.loadTexts:dsx1LineStatusChange.setStatus(_B)
ds1NearEndOptionalTrapGroup=NotificationGroup((1,3,6,1,2,1,10,18,14,1,8))
ds1NearEndOptionalTrapGroup.setObjects((_A,_B2))
if mibBuilder.loadTexts:ds1NearEndOptionalTrapGroup.setStatus(_B)
ds1Compliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,1))
ds1Compliance.setObjects(*((_A,_q),(_A,_G),(_A,_Ao),(_A,_r),(_A,_Q),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:ds1Compliance.setStatus(_E)
ds1MibT1PriCompliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,2))
ds1MibT1PriCompliance.setObjects(*((_A,_q),(_A,_G)))
if mibBuilder.loadTexts:ds1MibT1PriCompliance.setStatus(_E)
ds1MibE1PriCompliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,3))
ds1MibE1PriCompliance.setObjects(*((_A,_q),(_A,_G)))
if mibBuilder.loadTexts:ds1MibE1PriCompliance.setStatus(_E)
ds1Ds2Compliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,4))
ds1Ds2Compliance.setObjects((_A,_Q))
if mibBuilder.loadTexts:ds1Ds2Compliance.setStatus(_B)
ds1NCompliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,5))
ds1NCompliance.setObjects(*((_A,_u),(_A,_G),(_A,_Ao),(_A,_Ap),(_A,_r),(_A,_Q),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:ds1NCompliance.setStatus(_E)
ds1MibT1PriNCompliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,6))
ds1MibT1PriNCompliance.setObjects(*((_A,_u),(_A,_G)))
if mibBuilder.loadTexts:ds1MibT1PriNCompliance.setStatus(_E)
ds1MibE1PriNCompliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,7))
ds1MibE1PriNCompliance.setObjects(*((_A,_u),(_A,_G)))
if mibBuilder.loadTexts:ds1MibE1PriNCompliance.setStatus(_E)
ds1J1Compliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,8))
ds1J1Compliance.setObjects(*((_A,_v),(_A,_w),(_A,_B3),(_A,_Ap),(_A,_r),(_A,_Q),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:ds1J1Compliance.setStatus(_B)
ds1NMibT1PriNCompliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,9))
ds1NMibT1PriNCompliance.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:ds1NMibT1PriNCompliance.setStatus(_B)
ds1NMibE1PriNCompliance=ModuleCompliance((1,3,6,1,2,1,10,18,14,2,10))
ds1NMibE1PriNCompliance.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:ds1NMibE1PriNCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ds1':ds1,'dsx1ConfigTable':dsx1ConfigTable,'dsx1ConfigEntry':dsx1ConfigEntry,_H:dsx1LineIndex,_Ay:dsx1IfIndex,_Z:dsx1TimeElapsed,_a:dsx1ValidIntervals,_K:dsx1LineType,_L:dsx1LineCoding,_M:dsx1SendCode,_b:dsx1CircuitIdentifier,_c:dsx1LoopbackConfig,_I:dsx1LineStatus,_N:dsx1SignalMode,_O:dsx1TransmitClockSource,_d:dsx1Fdl,_e:dsx1InvalidIntervals,_f:dsx1LineLength,_Al:dsx1LineStatusLastChange,_A_:dsx1LineStatusChangeTrapEnable,_g:dsx1LoopbackStatus,_J:dsx1Ds1ChannelNumber,_P:dsx1Channelization,_Am:dsx1LineMode,_An:dsx1LineBuildOut,_B1:dsx1LineImpedance,'dsx1CurrentTable':dsx1CurrentTable,'dsx1CurrentEntry':dsx1CurrentEntry,_R:dsx1CurrentIndex,_h:dsx1CurrentESs,_i:dsx1CurrentSESs,_A0:dsx1CurrentSEFSs,_j:dsx1CurrentUASs,_A1:dsx1CurrentCSSs,_A2:dsx1CurrentPCVs,_A3:dsx1CurrentLESs,_A4:dsx1CurrentBESs,_As:dsx1CurrentDMs,_A5:dsx1CurrentLCVs,'dsx1IntervalTable':dsx1IntervalTable,'dsx1IntervalEntry':dsx1IntervalEntry,_S:dsx1IntervalIndex,_T:dsx1IntervalNumber,_k:dsx1IntervalESs,_l:dsx1IntervalSESs,_A6:dsx1IntervalSEFSs,_m:dsx1IntervalUASs,_A7:dsx1IntervalCSSs,_A8:dsx1IntervalPCVs,_A9:dsx1IntervalLESs,_AA:dsx1IntervalBESs,_At:dsx1IntervalDMs,_AB:dsx1IntervalLCVs,_AC:dsx1IntervalValidData,'dsx1TotalTable':dsx1TotalTable,'dsx1TotalEntry':dsx1TotalEntry,_U:dsx1TotalIndex,_n:dsx1TotalESs,_o:dsx1TotalSESs,_AD:dsx1TotalSEFSs,_p:dsx1TotalUASs,_AE:dsx1TotalCSSs,_AF:dsx1TotalPCVs,_AG:dsx1TotalLESs,_AH:dsx1TotalBESs,_Au:dsx1TotalDMs,_AI:dsx1TotalLCVs,'dsx1FarEndCurrentTable':dsx1FarEndCurrentTable,'dsx1FarEndCurrentEntry':dsx1FarEndCurrentEntry,_V:dsx1FarEndCurrentIndex,_AJ:dsx1FarEndTimeElapsed,_AK:dsx1FarEndValidIntervals,_AL:dsx1FarEndCurrentESs,_AM:dsx1FarEndCurrentSESs,_AN:dsx1FarEndCurrentSEFSs,_AO:dsx1FarEndCurrentUASs,_AP:dsx1FarEndCurrentCSSs,_AQ:dsx1FarEndCurrentLESs,_AR:dsx1FarEndCurrentPCVs,_AS:dsx1FarEndCurrentBESs,_Av:dsx1FarEndCurrentDMs,_AT:dsx1FarEndInvalidIntervals,'dsx1FarEndIntervalTable':dsx1FarEndIntervalTable,'dsx1FarEndIntervalEntry':dsx1FarEndIntervalEntry,_W:dsx1FarEndIntervalIndex,_X:dsx1FarEndIntervalNumber,_AU:dsx1FarEndIntervalESs,_AV:dsx1FarEndIntervalSESs,_AW:dsx1FarEndIntervalSEFSs,_AX:dsx1FarEndIntervalUASs,_AY:dsx1FarEndIntervalCSSs,_AZ:dsx1FarEndIntervalLESs,_Aa:dsx1FarEndIntervalPCVs,_Ab:dsx1FarEndIntervalBESs,_Aw:dsx1FarEndIntervalDMs,_Ac:dsx1FarEndIntervalValidData,'dsx1FarEndTotalTable':dsx1FarEndTotalTable,'dsx1FarEndTotalEntry':dsx1FarEndTotalEntry,_Y:dsx1FarEndTotalIndex,_Ad:dsx1FarEndTotalESs,_Ae:dsx1FarEndTotalSESs,_Af:dsx1FarEndTotalSEFSs,_Ag:dsx1FarEndTotalUASs,_Ah:dsx1FarEndTotalCSSs,_Ai:dsx1FarEndTotalLESs,_Aj:dsx1FarEndTotalPCVs,_Ak:dsx1FarEndTotalBESs,_Ax:dsx1FarEndTotalDMs,'dsx1FracTable':dsx1FracTable,'dsx1FracEntry':dsx1FracEntry,_y:dsx1FracIndex,_z:dsx1FracNumber,_Az:dsx1FracIfIndex,'ds1Conformance':ds1Conformance,'ds1Groups':ds1Groups,_q:ds1NearEndConfigGroup,_G:ds1NearEndStatisticsGroup,_Ao:ds1FarEndGroup,'ds1DeprecatedGroup':ds1DeprecatedGroup,_r:ds1NearEndOptionalConfigGroup,_Q:ds1DS2Group,_s:ds1TransStatsGroup,_Ap:ds1NearEndOptionalTrapGroup,_t:ds1ChanMappingGroup,_u:ds1NearEndConfigurationGroup,_v:ds1NearEndCfgGroup,_w:ds1NearEndStatGroup,_B3:ds1FarEndNGroup,'ds1Compliances':ds1Compliances,'ds1Compliance':ds1Compliance,'ds1MibT1PriCompliance':ds1MibT1PriCompliance,'ds1MibE1PriCompliance':ds1MibE1PriCompliance,'ds1Ds2Compliance':ds1Ds2Compliance,'ds1NCompliance':ds1NCompliance,'ds1MibT1PriNCompliance':ds1MibT1PriNCompliance,'ds1MibE1PriNCompliance':ds1MibE1PriNCompliance,'ds1J1Compliance':ds1J1Compliance,'ds1NMibT1PriNCompliance':ds1NMibT1PriNCompliance,'ds1NMibE1PriNCompliance':ds1NMibE1PriNCompliance,'ds1Traps':ds1Traps,_B2:dsx1LineStatusChange,'dsx1ChanMappingTable':dsx1ChanMappingTable,'dsx1ChanMappingEntry':dsx1ChanMappingEntry,_B0:dsx1ChanMappedIfIndex})