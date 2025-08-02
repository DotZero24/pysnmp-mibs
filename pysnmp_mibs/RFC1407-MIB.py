_Ah='ds3NearEndOptionalConfigGroup'
_Ag='ds3NearEndOptionalTrapGroup'
_Af='ds3FarEndGroup'
_Ae='ds3NearEndStatisticsGroup'
_Ad='ds3NearEndConfigGroup'
_Ac='dsx3LineStatusChange'
_Ab='dsx3LineStatusChangeTrapEnable'
_Aa='dsx3FracIfIndex'
_AZ='dsx3IfIndex'
_AY='dsx3FarEndTotalUASs'
_AX='dsx3FarEndTotalCCVs'
_AW='dsx3FarEndTotalCSESs'
_AV='dsx3FarEndTotalCESs'
_AU='dsx3FarEndIntervalValidData'
_AT='dsx3FarEndIntervalUASs'
_AS='dsx3FarEndIntervalCCVs'
_AR='dsx3FarEndIntervalCSESs'
_AQ='dsx3FarEndIntervalCESs'
_AP='dsx3FarEndInvalidIntervals'
_AO='dsx3FarEndCurrentUASs'
_AN='dsx3FarEndCurrentCCVs'
_AM='dsx3FarEndCurrentCSESs'
_AL='dsx3FarEndCurrentCESs'
_AK='dsx3FarEndValidIntervals'
_AJ='dsx3FarEndTimeElapsed'
_AI='dsx3FarEndFacilityIDCode'
_AH='dsx3FarEndUnitCode'
_AG='dsx3FarEndFrameIDCode'
_AF='dsx3FarEndLocationIDCode'
_AE='dsx3FarEndEquipCode'
_AD='dsx3TotalCSESs'
_AC='dsx3TotalCESs'
_AB='dsx3TotalCCVs'
_AA='dsx3TotalLESs'
_A9='dsx3TotalPCVs'
_A8='dsx3TotalLCVs'
_A7='dsx3TotalUASs'
_A6='dsx3TotalSEFSs'
_A5='dsx3TotalPSESs'
_A4='dsx3TotalPESs'
_A3='dsx3IntervalValidData'
_A2='dsx3IntervalCSESs'
_A1='dsx3IntervalCESs'
_A0='dsx3IntervalCCVs'
_z='dsx3IntervalLESs'
_y='dsx3IntervalPCVs'
_x='dsx3IntervalLCVs'
_w='dsx3IntervalUASs'
_v='dsx3IntervalSEFSs'
_u='dsx3IntervalPSESs'
_t='dsx3IntervalPESs'
_s='dsx3CurrentCSESs'
_r='dsx3CurrentCESs'
_q='dsx3CurrentCCVs'
_p='dsx3CurrentLESs'
_o='dsx3CurrentPCVs'
_n='dsx3CurrentLCVs'
_m='dsx3CurrentUASs'
_l='dsx3CurrentSEFSs'
_k='dsx3CurrentPSESs'
_j='dsx3CurrentPESs'
_i='dsx3Ds1ForRemoteLoop'
_h='dsx3Channelization'
_g='dsx3LoopbackStatus'
_f='dsx3LineLength'
_e='dsx3InvalidIntervals'
_d='dsx3TransmitClockSource'
_c='dsx3LoopbackConfig'
_b='dsx3CircuitIdentifier'
_a='dsx3SendCode'
_Z='dsx3LineCoding'
_Y='dsx3LineType'
_X='dsx3ValidIntervals'
_W='dsx3TimeElapsed'
_V='disabled'
_U='dsx3LineStatusLastChange'
_T='dsx3LineStatus'
_S='dsx3FracNumber'
_R='dsx3FracIndex'
_Q='dsx3FarEndTotalIndex'
_P='dsx3FarEndIntervalNumber'
_O='dsx3FarEndIntervalIndex'
_N='dsx3FarEndCurrentIndex'
_M='dsx3FarEndLineIndex'
_L='dsx3TotalIndex'
_K='dsx3IntervalNumber'
_J='dsx3IntervalIndex'
_I='dsx3CurrentIndex'
_H='dsx3LineIndex'
_G='deprecated'
_F='DisplayString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='RFC1407-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
ds3=ModuleIdentity((1,3,6,1,2,1,10,30))
if mibBuilder.loadTexts:ds3.setRevisions(('2004-09-08 00:00','1998-08-01 21:30','1993-01-25 20:28'))
_Dsx3ConfigTable_Object=MibTable
dsx3ConfigTable=_Dsx3ConfigTable_Object((1,3,6,1,2,1,10,30,5))
if mibBuilder.loadTexts:dsx3ConfigTable.setStatus(_B)
_Dsx3ConfigEntry_Object=MibTableRow
dsx3ConfigEntry=_Dsx3ConfigEntry_Object((1,3,6,1,2,1,10,30,5,1))
dsx3ConfigEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dsx3ConfigEntry.setStatus(_B)
_Dsx3LineIndex_Type=InterfaceIndex
_Dsx3LineIndex_Object=MibTableColumn
dsx3LineIndex=_Dsx3LineIndex_Object((1,3,6,1,2,1,10,30,5,1,1),_Dsx3LineIndex_Type())
dsx3LineIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3LineIndex.setStatus(_B)
_Dsx3IfIndex_Type=InterfaceIndex
_Dsx3IfIndex_Object=MibTableColumn
dsx3IfIndex=_Dsx3IfIndex_Object((1,3,6,1,2,1,10,30,5,1,2),_Dsx3IfIndex_Type())
dsx3IfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IfIndex.setStatus(_G)
class _Dsx3TimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_Dsx3TimeElapsed_Type.__name__=_D
_Dsx3TimeElapsed_Object=MibTableColumn
dsx3TimeElapsed=_Dsx3TimeElapsed_Object((1,3,6,1,2,1,10,30,5,1,3),_Dsx3TimeElapsed_Type())
dsx3TimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TimeElapsed.setStatus(_B)
class _Dsx3ValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_Dsx3ValidIntervals_Type.__name__=_D
_Dsx3ValidIntervals_Object=MibTableColumn
dsx3ValidIntervals=_Dsx3ValidIntervals_Object((1,3,6,1,2,1,10,30,5,1,4),_Dsx3ValidIntervals_Type())
dsx3ValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3ValidIntervals.setStatus(_B)
class _Dsx3LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('dsx3other',1),('dsx3M23',2),('dsx3SYNTRAN',3),('dsx3CbitParity',4),('dsx3ClearChannel',5),('e3other',6),('e3Framed',7),('e3Plcp',8),('dsx3M13',9)))
_Dsx3LineType_Type.__name__=_D
_Dsx3LineType_Object=MibTableColumn
dsx3LineType=_Dsx3LineType_Object((1,3,6,1,2,1,10,30,5,1,5),_Dsx3LineType_Type())
dsx3LineType.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3LineType.setStatus(_B)
class _Dsx3LineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dsx3Other',1),('dsx3B3ZS',2),('e3HDB3',3)))
_Dsx3LineCoding_Type.__name__=_D
_Dsx3LineCoding_Object=MibTableColumn
dsx3LineCoding=_Dsx3LineCoding_Object((1,3,6,1,2,1,10,30,5,1,6),_Dsx3LineCoding_Type())
dsx3LineCoding.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3LineCoding.setStatus(_B)
class _Dsx3SendCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dsx3SendNoCode',1),('dsx3SendLineCode',2),('dsx3SendPayloadCode',3),('dsx3SendResetCode',4),('dsx3SendDS1LoopCode',5),('dsx3SendTestPattern',6)))
_Dsx3SendCode_Type.__name__=_D
_Dsx3SendCode_Object=MibTableColumn
dsx3SendCode=_Dsx3SendCode_Object((1,3,6,1,2,1,10,30,5,1,7),_Dsx3SendCode_Type())
dsx3SendCode.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3SendCode.setStatus(_B)
class _Dsx3CircuitIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Dsx3CircuitIdentifier_Type.__name__=_F
_Dsx3CircuitIdentifier_Object=MibTableColumn
dsx3CircuitIdentifier=_Dsx3CircuitIdentifier_Object((1,3,6,1,2,1,10,30,5,1,8),_Dsx3CircuitIdentifier_Type())
dsx3CircuitIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3CircuitIdentifier.setStatus(_B)
class _Dsx3LoopbackConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dsx3NoLoop',1),('dsx3PayloadLoop',2),('dsx3LineLoop',3),('dsx3OtherLoop',4),('dsx3InwardLoop',5),('dsx3DualLoop',6)))
_Dsx3LoopbackConfig_Type.__name__=_D
_Dsx3LoopbackConfig_Object=MibTableColumn
dsx3LoopbackConfig=_Dsx3LoopbackConfig_Object((1,3,6,1,2,1,10,30,5,1,9),_Dsx3LoopbackConfig_Type())
dsx3LoopbackConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3LoopbackConfig.setStatus(_B)
class _Dsx3LineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Dsx3LineStatus_Type.__name__=_D
_Dsx3LineStatus_Object=MibTableColumn
dsx3LineStatus=_Dsx3LineStatus_Object((1,3,6,1,2,1,10,30,5,1,10),_Dsx3LineStatus_Type())
dsx3LineStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3LineStatus.setStatus(_B)
class _Dsx3TransmitClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2),('throughTiming',3)))
_Dsx3TransmitClockSource_Type.__name__=_D
_Dsx3TransmitClockSource_Object=MibTableColumn
dsx3TransmitClockSource=_Dsx3TransmitClockSource_Object((1,3,6,1,2,1,10,30,5,1,11),_Dsx3TransmitClockSource_Type())
dsx3TransmitClockSource.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3TransmitClockSource.setStatus(_B)
class _Dsx3InvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_Dsx3InvalidIntervals_Type.__name__=_D
_Dsx3InvalidIntervals_Object=MibTableColumn
dsx3InvalidIntervals=_Dsx3InvalidIntervals_Object((1,3,6,1,2,1,10,30,5,1,12),_Dsx3InvalidIntervals_Type())
dsx3InvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3InvalidIntervals.setStatus(_B)
class _Dsx3LineLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64000))
_Dsx3LineLength_Type.__name__=_D
_Dsx3LineLength_Object=MibTableColumn
dsx3LineLength=_Dsx3LineLength_Object((1,3,6,1,2,1,10,30,5,1,13),_Dsx3LineLength_Type())
dsx3LineLength.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3LineLength.setStatus(_B)
if mibBuilder.loadTexts:dsx3LineLength.setUnits('meters')
_Dsx3LineStatusLastChange_Type=TimeStamp
_Dsx3LineStatusLastChange_Object=MibTableColumn
dsx3LineStatusLastChange=_Dsx3LineStatusLastChange_Object((1,3,6,1,2,1,10,30,5,1,14),_Dsx3LineStatusLastChange_Type())
dsx3LineStatusLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3LineStatusLastChange.setStatus(_B)
class _Dsx3LineStatusChangeTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_V,2)))
_Dsx3LineStatusChangeTrapEnable_Type.__name__=_D
_Dsx3LineStatusChangeTrapEnable_Object=MibTableColumn
dsx3LineStatusChangeTrapEnable=_Dsx3LineStatusChangeTrapEnable_Object((1,3,6,1,2,1,10,30,5,1,15),_Dsx3LineStatusChangeTrapEnable_Type())
dsx3LineStatusChangeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3LineStatusChangeTrapEnable.setStatus(_B)
class _Dsx3LoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_Dsx3LoopbackStatus_Type.__name__=_D
_Dsx3LoopbackStatus_Object=MibTableColumn
dsx3LoopbackStatus=_Dsx3LoopbackStatus_Object((1,3,6,1,2,1,10,30,5,1,16),_Dsx3LoopbackStatus_Type())
dsx3LoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3LoopbackStatus.setStatus(_B)
class _Dsx3Channelization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),('enabledDs1',2),('enabledDs2',3)))
_Dsx3Channelization_Type.__name__=_D
_Dsx3Channelization_Object=MibTableColumn
dsx3Channelization=_Dsx3Channelization_Object((1,3,6,1,2,1,10,30,5,1,17),_Dsx3Channelization_Type())
dsx3Channelization.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3Channelization.setStatus(_B)
class _Dsx3Ds1ForRemoteLoop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,29))
_Dsx3Ds1ForRemoteLoop_Type.__name__=_D
_Dsx3Ds1ForRemoteLoop_Object=MibTableColumn
dsx3Ds1ForRemoteLoop=_Dsx3Ds1ForRemoteLoop_Object((1,3,6,1,2,1,10,30,5,1,18),_Dsx3Ds1ForRemoteLoop_Type())
dsx3Ds1ForRemoteLoop.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3Ds1ForRemoteLoop.setStatus(_B)
_Dsx3CurrentTable_Object=MibTable
dsx3CurrentTable=_Dsx3CurrentTable_Object((1,3,6,1,2,1,10,30,6))
if mibBuilder.loadTexts:dsx3CurrentTable.setStatus(_B)
_Dsx3CurrentEntry_Object=MibTableRow
dsx3CurrentEntry=_Dsx3CurrentEntry_Object((1,3,6,1,2,1,10,30,6,1))
dsx3CurrentEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:dsx3CurrentEntry.setStatus(_B)
_Dsx3CurrentIndex_Type=InterfaceIndex
_Dsx3CurrentIndex_Object=MibTableColumn
dsx3CurrentIndex=_Dsx3CurrentIndex_Object((1,3,6,1,2,1,10,30,6,1,1),_Dsx3CurrentIndex_Type())
dsx3CurrentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentIndex.setStatus(_B)
_Dsx3CurrentPESs_Type=PerfCurrentCount
_Dsx3CurrentPESs_Object=MibTableColumn
dsx3CurrentPESs=_Dsx3CurrentPESs_Object((1,3,6,1,2,1,10,30,6,1,2),_Dsx3CurrentPESs_Type())
dsx3CurrentPESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentPESs.setStatus(_B)
_Dsx3CurrentPSESs_Type=PerfCurrentCount
_Dsx3CurrentPSESs_Object=MibTableColumn
dsx3CurrentPSESs=_Dsx3CurrentPSESs_Object((1,3,6,1,2,1,10,30,6,1,3),_Dsx3CurrentPSESs_Type())
dsx3CurrentPSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentPSESs.setStatus(_B)
_Dsx3CurrentSEFSs_Type=PerfCurrentCount
_Dsx3CurrentSEFSs_Object=MibTableColumn
dsx3CurrentSEFSs=_Dsx3CurrentSEFSs_Object((1,3,6,1,2,1,10,30,6,1,4),_Dsx3CurrentSEFSs_Type())
dsx3CurrentSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentSEFSs.setStatus(_B)
_Dsx3CurrentUASs_Type=PerfCurrentCount
_Dsx3CurrentUASs_Object=MibTableColumn
dsx3CurrentUASs=_Dsx3CurrentUASs_Object((1,3,6,1,2,1,10,30,6,1,5),_Dsx3CurrentUASs_Type())
dsx3CurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentUASs.setStatus(_B)
_Dsx3CurrentLCVs_Type=PerfCurrentCount
_Dsx3CurrentLCVs_Object=MibTableColumn
dsx3CurrentLCVs=_Dsx3CurrentLCVs_Object((1,3,6,1,2,1,10,30,6,1,6),_Dsx3CurrentLCVs_Type())
dsx3CurrentLCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentLCVs.setStatus(_B)
_Dsx3CurrentPCVs_Type=PerfCurrentCount
_Dsx3CurrentPCVs_Object=MibTableColumn
dsx3CurrentPCVs=_Dsx3CurrentPCVs_Object((1,3,6,1,2,1,10,30,6,1,7),_Dsx3CurrentPCVs_Type())
dsx3CurrentPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentPCVs.setStatus(_B)
_Dsx3CurrentLESs_Type=PerfCurrentCount
_Dsx3CurrentLESs_Object=MibTableColumn
dsx3CurrentLESs=_Dsx3CurrentLESs_Object((1,3,6,1,2,1,10,30,6,1,8),_Dsx3CurrentLESs_Type())
dsx3CurrentLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentLESs.setStatus(_B)
_Dsx3CurrentCCVs_Type=PerfCurrentCount
_Dsx3CurrentCCVs_Object=MibTableColumn
dsx3CurrentCCVs=_Dsx3CurrentCCVs_Object((1,3,6,1,2,1,10,30,6,1,9),_Dsx3CurrentCCVs_Type())
dsx3CurrentCCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentCCVs.setStatus(_B)
_Dsx3CurrentCESs_Type=PerfCurrentCount
_Dsx3CurrentCESs_Object=MibTableColumn
dsx3CurrentCESs=_Dsx3CurrentCESs_Object((1,3,6,1,2,1,10,30,6,1,10),_Dsx3CurrentCESs_Type())
dsx3CurrentCESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentCESs.setStatus(_B)
_Dsx3CurrentCSESs_Type=PerfCurrentCount
_Dsx3CurrentCSESs_Object=MibTableColumn
dsx3CurrentCSESs=_Dsx3CurrentCSESs_Object((1,3,6,1,2,1,10,30,6,1,11),_Dsx3CurrentCSESs_Type())
dsx3CurrentCSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3CurrentCSESs.setStatus(_B)
_Dsx3IntervalTable_Object=MibTable
dsx3IntervalTable=_Dsx3IntervalTable_Object((1,3,6,1,2,1,10,30,7))
if mibBuilder.loadTexts:dsx3IntervalTable.setStatus(_B)
_Dsx3IntervalEntry_Object=MibTableRow
dsx3IntervalEntry=_Dsx3IntervalEntry_Object((1,3,6,1,2,1,10,30,7,1))
dsx3IntervalEntry.setIndexNames((0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:dsx3IntervalEntry.setStatus(_B)
_Dsx3IntervalIndex_Type=InterfaceIndex
_Dsx3IntervalIndex_Object=MibTableColumn
dsx3IntervalIndex=_Dsx3IntervalIndex_Object((1,3,6,1,2,1,10,30,7,1,1),_Dsx3IntervalIndex_Type())
dsx3IntervalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalIndex.setStatus(_B)
class _Dsx3IntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_Dsx3IntervalNumber_Type.__name__=_D
_Dsx3IntervalNumber_Object=MibTableColumn
dsx3IntervalNumber=_Dsx3IntervalNumber_Object((1,3,6,1,2,1,10,30,7,1,2),_Dsx3IntervalNumber_Type())
dsx3IntervalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalNumber.setStatus(_B)
_Dsx3IntervalPESs_Type=PerfIntervalCount
_Dsx3IntervalPESs_Object=MibTableColumn
dsx3IntervalPESs=_Dsx3IntervalPESs_Object((1,3,6,1,2,1,10,30,7,1,3),_Dsx3IntervalPESs_Type())
dsx3IntervalPESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalPESs.setStatus(_B)
_Dsx3IntervalPSESs_Type=PerfIntervalCount
_Dsx3IntervalPSESs_Object=MibTableColumn
dsx3IntervalPSESs=_Dsx3IntervalPSESs_Object((1,3,6,1,2,1,10,30,7,1,4),_Dsx3IntervalPSESs_Type())
dsx3IntervalPSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalPSESs.setStatus(_B)
_Dsx3IntervalSEFSs_Type=PerfIntervalCount
_Dsx3IntervalSEFSs_Object=MibTableColumn
dsx3IntervalSEFSs=_Dsx3IntervalSEFSs_Object((1,3,6,1,2,1,10,30,7,1,5),_Dsx3IntervalSEFSs_Type())
dsx3IntervalSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalSEFSs.setStatus(_B)
_Dsx3IntervalUASs_Type=PerfIntervalCount
_Dsx3IntervalUASs_Object=MibTableColumn
dsx3IntervalUASs=_Dsx3IntervalUASs_Object((1,3,6,1,2,1,10,30,7,1,6),_Dsx3IntervalUASs_Type())
dsx3IntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalUASs.setStatus(_B)
_Dsx3IntervalLCVs_Type=PerfIntervalCount
_Dsx3IntervalLCVs_Object=MibTableColumn
dsx3IntervalLCVs=_Dsx3IntervalLCVs_Object((1,3,6,1,2,1,10,30,7,1,7),_Dsx3IntervalLCVs_Type())
dsx3IntervalLCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalLCVs.setStatus(_B)
_Dsx3IntervalPCVs_Type=PerfIntervalCount
_Dsx3IntervalPCVs_Object=MibTableColumn
dsx3IntervalPCVs=_Dsx3IntervalPCVs_Object((1,3,6,1,2,1,10,30,7,1,8),_Dsx3IntervalPCVs_Type())
dsx3IntervalPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalPCVs.setStatus(_B)
_Dsx3IntervalLESs_Type=PerfIntervalCount
_Dsx3IntervalLESs_Object=MibTableColumn
dsx3IntervalLESs=_Dsx3IntervalLESs_Object((1,3,6,1,2,1,10,30,7,1,9),_Dsx3IntervalLESs_Type())
dsx3IntervalLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalLESs.setStatus(_B)
_Dsx3IntervalCCVs_Type=PerfIntervalCount
_Dsx3IntervalCCVs_Object=MibTableColumn
dsx3IntervalCCVs=_Dsx3IntervalCCVs_Object((1,3,6,1,2,1,10,30,7,1,10),_Dsx3IntervalCCVs_Type())
dsx3IntervalCCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalCCVs.setStatus(_B)
_Dsx3IntervalCESs_Type=PerfIntervalCount
_Dsx3IntervalCESs_Object=MibTableColumn
dsx3IntervalCESs=_Dsx3IntervalCESs_Object((1,3,6,1,2,1,10,30,7,1,11),_Dsx3IntervalCESs_Type())
dsx3IntervalCESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalCESs.setStatus(_B)
_Dsx3IntervalCSESs_Type=PerfIntervalCount
_Dsx3IntervalCSESs_Object=MibTableColumn
dsx3IntervalCSESs=_Dsx3IntervalCSESs_Object((1,3,6,1,2,1,10,30,7,1,12),_Dsx3IntervalCSESs_Type())
dsx3IntervalCSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalCSESs.setStatus(_B)
_Dsx3IntervalValidData_Type=TruthValue
_Dsx3IntervalValidData_Object=MibTableColumn
dsx3IntervalValidData=_Dsx3IntervalValidData_Object((1,3,6,1,2,1,10,30,7,1,13),_Dsx3IntervalValidData_Type())
dsx3IntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3IntervalValidData.setStatus(_B)
_Dsx3TotalTable_Object=MibTable
dsx3TotalTable=_Dsx3TotalTable_Object((1,3,6,1,2,1,10,30,8))
if mibBuilder.loadTexts:dsx3TotalTable.setStatus(_B)
_Dsx3TotalEntry_Object=MibTableRow
dsx3TotalEntry=_Dsx3TotalEntry_Object((1,3,6,1,2,1,10,30,8,1))
dsx3TotalEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:dsx3TotalEntry.setStatus(_B)
_Dsx3TotalIndex_Type=InterfaceIndex
_Dsx3TotalIndex_Object=MibTableColumn
dsx3TotalIndex=_Dsx3TotalIndex_Object((1,3,6,1,2,1,10,30,8,1,1),_Dsx3TotalIndex_Type())
dsx3TotalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalIndex.setStatus(_B)
_Dsx3TotalPESs_Type=PerfTotalCount
_Dsx3TotalPESs_Object=MibTableColumn
dsx3TotalPESs=_Dsx3TotalPESs_Object((1,3,6,1,2,1,10,30,8,1,2),_Dsx3TotalPESs_Type())
dsx3TotalPESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalPESs.setStatus(_B)
_Dsx3TotalPSESs_Type=PerfTotalCount
_Dsx3TotalPSESs_Object=MibTableColumn
dsx3TotalPSESs=_Dsx3TotalPSESs_Object((1,3,6,1,2,1,10,30,8,1,3),_Dsx3TotalPSESs_Type())
dsx3TotalPSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalPSESs.setStatus(_B)
_Dsx3TotalSEFSs_Type=PerfTotalCount
_Dsx3TotalSEFSs_Object=MibTableColumn
dsx3TotalSEFSs=_Dsx3TotalSEFSs_Object((1,3,6,1,2,1,10,30,8,1,4),_Dsx3TotalSEFSs_Type())
dsx3TotalSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalSEFSs.setStatus(_B)
_Dsx3TotalUASs_Type=PerfTotalCount
_Dsx3TotalUASs_Object=MibTableColumn
dsx3TotalUASs=_Dsx3TotalUASs_Object((1,3,6,1,2,1,10,30,8,1,5),_Dsx3TotalUASs_Type())
dsx3TotalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalUASs.setStatus(_B)
_Dsx3TotalLCVs_Type=PerfTotalCount
_Dsx3TotalLCVs_Object=MibTableColumn
dsx3TotalLCVs=_Dsx3TotalLCVs_Object((1,3,6,1,2,1,10,30,8,1,6),_Dsx3TotalLCVs_Type())
dsx3TotalLCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalLCVs.setStatus(_B)
_Dsx3TotalPCVs_Type=PerfTotalCount
_Dsx3TotalPCVs_Object=MibTableColumn
dsx3TotalPCVs=_Dsx3TotalPCVs_Object((1,3,6,1,2,1,10,30,8,1,7),_Dsx3TotalPCVs_Type())
dsx3TotalPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalPCVs.setStatus(_B)
_Dsx3TotalLESs_Type=PerfTotalCount
_Dsx3TotalLESs_Object=MibTableColumn
dsx3TotalLESs=_Dsx3TotalLESs_Object((1,3,6,1,2,1,10,30,8,1,8),_Dsx3TotalLESs_Type())
dsx3TotalLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalLESs.setStatus(_B)
_Dsx3TotalCCVs_Type=PerfTotalCount
_Dsx3TotalCCVs_Object=MibTableColumn
dsx3TotalCCVs=_Dsx3TotalCCVs_Object((1,3,6,1,2,1,10,30,8,1,9),_Dsx3TotalCCVs_Type())
dsx3TotalCCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalCCVs.setStatus(_B)
_Dsx3TotalCESs_Type=PerfTotalCount
_Dsx3TotalCESs_Object=MibTableColumn
dsx3TotalCESs=_Dsx3TotalCESs_Object((1,3,6,1,2,1,10,30,8,1,10),_Dsx3TotalCESs_Type())
dsx3TotalCESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalCESs.setStatus(_B)
_Dsx3TotalCSESs_Type=PerfTotalCount
_Dsx3TotalCSESs_Object=MibTableColumn
dsx3TotalCSESs=_Dsx3TotalCSESs_Object((1,3,6,1,2,1,10,30,8,1,11),_Dsx3TotalCSESs_Type())
dsx3TotalCSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3TotalCSESs.setStatus(_B)
_Dsx3FarEndConfigTable_Object=MibTable
dsx3FarEndConfigTable=_Dsx3FarEndConfigTable_Object((1,3,6,1,2,1,10,30,9))
if mibBuilder.loadTexts:dsx3FarEndConfigTable.setStatus(_B)
_Dsx3FarEndConfigEntry_Object=MibTableRow
dsx3FarEndConfigEntry=_Dsx3FarEndConfigEntry_Object((1,3,6,1,2,1,10,30,9,1))
dsx3FarEndConfigEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:dsx3FarEndConfigEntry.setStatus(_B)
_Dsx3FarEndLineIndex_Type=InterfaceIndex
_Dsx3FarEndLineIndex_Object=MibTableColumn
dsx3FarEndLineIndex=_Dsx3FarEndLineIndex_Object((1,3,6,1,2,1,10,30,9,1,1),_Dsx3FarEndLineIndex_Type())
dsx3FarEndLineIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndLineIndex.setStatus(_B)
class _Dsx3FarEndEquipCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Dsx3FarEndEquipCode_Type.__name__=_F
_Dsx3FarEndEquipCode_Object=MibTableColumn
dsx3FarEndEquipCode=_Dsx3FarEndEquipCode_Object((1,3,6,1,2,1,10,30,9,1,2),_Dsx3FarEndEquipCode_Type())
dsx3FarEndEquipCode.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3FarEndEquipCode.setStatus(_B)
class _Dsx3FarEndLocationIDCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Dsx3FarEndLocationIDCode_Type.__name__=_F
_Dsx3FarEndLocationIDCode_Object=MibTableColumn
dsx3FarEndLocationIDCode=_Dsx3FarEndLocationIDCode_Object((1,3,6,1,2,1,10,30,9,1,3),_Dsx3FarEndLocationIDCode_Type())
dsx3FarEndLocationIDCode.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3FarEndLocationIDCode.setStatus(_B)
class _Dsx3FarEndFrameIDCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Dsx3FarEndFrameIDCode_Type.__name__=_F
_Dsx3FarEndFrameIDCode_Object=MibTableColumn
dsx3FarEndFrameIDCode=_Dsx3FarEndFrameIDCode_Object((1,3,6,1,2,1,10,30,9,1,4),_Dsx3FarEndFrameIDCode_Type())
dsx3FarEndFrameIDCode.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3FarEndFrameIDCode.setStatus(_B)
class _Dsx3FarEndUnitCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_Dsx3FarEndUnitCode_Type.__name__=_F
_Dsx3FarEndUnitCode_Object=MibTableColumn
dsx3FarEndUnitCode=_Dsx3FarEndUnitCode_Object((1,3,6,1,2,1,10,30,9,1,5),_Dsx3FarEndUnitCode_Type())
dsx3FarEndUnitCode.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3FarEndUnitCode.setStatus(_B)
class _Dsx3FarEndFacilityIDCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_Dsx3FarEndFacilityIDCode_Type.__name__=_F
_Dsx3FarEndFacilityIDCode_Object=MibTableColumn
dsx3FarEndFacilityIDCode=_Dsx3FarEndFacilityIDCode_Object((1,3,6,1,2,1,10,30,9,1,6),_Dsx3FarEndFacilityIDCode_Type())
dsx3FarEndFacilityIDCode.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3FarEndFacilityIDCode.setStatus(_B)
_Dsx3FarEndCurrentTable_Object=MibTable
dsx3FarEndCurrentTable=_Dsx3FarEndCurrentTable_Object((1,3,6,1,2,1,10,30,10))
if mibBuilder.loadTexts:dsx3FarEndCurrentTable.setStatus(_B)
_Dsx3FarEndCurrentEntry_Object=MibTableRow
dsx3FarEndCurrentEntry=_Dsx3FarEndCurrentEntry_Object((1,3,6,1,2,1,10,30,10,1))
dsx3FarEndCurrentEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:dsx3FarEndCurrentEntry.setStatus(_B)
_Dsx3FarEndCurrentIndex_Type=InterfaceIndex
_Dsx3FarEndCurrentIndex_Object=MibTableColumn
dsx3FarEndCurrentIndex=_Dsx3FarEndCurrentIndex_Object((1,3,6,1,2,1,10,30,10,1,1),_Dsx3FarEndCurrentIndex_Type())
dsx3FarEndCurrentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndCurrentIndex.setStatus(_B)
class _Dsx3FarEndTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_Dsx3FarEndTimeElapsed_Type.__name__=_D
_Dsx3FarEndTimeElapsed_Object=MibTableColumn
dsx3FarEndTimeElapsed=_Dsx3FarEndTimeElapsed_Object((1,3,6,1,2,1,10,30,10,1,2),_Dsx3FarEndTimeElapsed_Type())
dsx3FarEndTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndTimeElapsed.setStatus(_B)
class _Dsx3FarEndValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_Dsx3FarEndValidIntervals_Type.__name__=_D
_Dsx3FarEndValidIntervals_Object=MibTableColumn
dsx3FarEndValidIntervals=_Dsx3FarEndValidIntervals_Object((1,3,6,1,2,1,10,30,10,1,3),_Dsx3FarEndValidIntervals_Type())
dsx3FarEndValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndValidIntervals.setStatus(_B)
_Dsx3FarEndCurrentCESs_Type=PerfCurrentCount
_Dsx3FarEndCurrentCESs_Object=MibTableColumn
dsx3FarEndCurrentCESs=_Dsx3FarEndCurrentCESs_Object((1,3,6,1,2,1,10,30,10,1,4),_Dsx3FarEndCurrentCESs_Type())
dsx3FarEndCurrentCESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndCurrentCESs.setStatus(_B)
_Dsx3FarEndCurrentCSESs_Type=PerfCurrentCount
_Dsx3FarEndCurrentCSESs_Object=MibTableColumn
dsx3FarEndCurrentCSESs=_Dsx3FarEndCurrentCSESs_Object((1,3,6,1,2,1,10,30,10,1,5),_Dsx3FarEndCurrentCSESs_Type())
dsx3FarEndCurrentCSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndCurrentCSESs.setStatus(_B)
_Dsx3FarEndCurrentCCVs_Type=PerfCurrentCount
_Dsx3FarEndCurrentCCVs_Object=MibTableColumn
dsx3FarEndCurrentCCVs=_Dsx3FarEndCurrentCCVs_Object((1,3,6,1,2,1,10,30,10,1,6),_Dsx3FarEndCurrentCCVs_Type())
dsx3FarEndCurrentCCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndCurrentCCVs.setStatus(_B)
_Dsx3FarEndCurrentUASs_Type=PerfCurrentCount
_Dsx3FarEndCurrentUASs_Object=MibTableColumn
dsx3FarEndCurrentUASs=_Dsx3FarEndCurrentUASs_Object((1,3,6,1,2,1,10,30,10,1,7),_Dsx3FarEndCurrentUASs_Type())
dsx3FarEndCurrentUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndCurrentUASs.setStatus(_B)
class _Dsx3FarEndInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_Dsx3FarEndInvalidIntervals_Type.__name__=_D
_Dsx3FarEndInvalidIntervals_Object=MibTableColumn
dsx3FarEndInvalidIntervals=_Dsx3FarEndInvalidIntervals_Object((1,3,6,1,2,1,10,30,10,1,8),_Dsx3FarEndInvalidIntervals_Type())
dsx3FarEndInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndInvalidIntervals.setStatus(_B)
_Dsx3FarEndIntervalTable_Object=MibTable
dsx3FarEndIntervalTable=_Dsx3FarEndIntervalTable_Object((1,3,6,1,2,1,10,30,11))
if mibBuilder.loadTexts:dsx3FarEndIntervalTable.setStatus(_B)
_Dsx3FarEndIntervalEntry_Object=MibTableRow
dsx3FarEndIntervalEntry=_Dsx3FarEndIntervalEntry_Object((1,3,6,1,2,1,10,30,11,1))
dsx3FarEndIntervalEntry.setIndexNames((0,_A,_O),(0,_A,_P))
if mibBuilder.loadTexts:dsx3FarEndIntervalEntry.setStatus(_B)
_Dsx3FarEndIntervalIndex_Type=InterfaceIndex
_Dsx3FarEndIntervalIndex_Object=MibTableColumn
dsx3FarEndIntervalIndex=_Dsx3FarEndIntervalIndex_Object((1,3,6,1,2,1,10,30,11,1,1),_Dsx3FarEndIntervalIndex_Type())
dsx3FarEndIntervalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndIntervalIndex.setStatus(_B)
class _Dsx3FarEndIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_Dsx3FarEndIntervalNumber_Type.__name__=_D
_Dsx3FarEndIntervalNumber_Object=MibTableColumn
dsx3FarEndIntervalNumber=_Dsx3FarEndIntervalNumber_Object((1,3,6,1,2,1,10,30,11,1,2),_Dsx3FarEndIntervalNumber_Type())
dsx3FarEndIntervalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndIntervalNumber.setStatus(_B)
_Dsx3FarEndIntervalCESs_Type=PerfIntervalCount
_Dsx3FarEndIntervalCESs_Object=MibTableColumn
dsx3FarEndIntervalCESs=_Dsx3FarEndIntervalCESs_Object((1,3,6,1,2,1,10,30,11,1,3),_Dsx3FarEndIntervalCESs_Type())
dsx3FarEndIntervalCESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndIntervalCESs.setStatus(_B)
_Dsx3FarEndIntervalCSESs_Type=PerfIntervalCount
_Dsx3FarEndIntervalCSESs_Object=MibTableColumn
dsx3FarEndIntervalCSESs=_Dsx3FarEndIntervalCSESs_Object((1,3,6,1,2,1,10,30,11,1,4),_Dsx3FarEndIntervalCSESs_Type())
dsx3FarEndIntervalCSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndIntervalCSESs.setStatus(_B)
_Dsx3FarEndIntervalCCVs_Type=PerfIntervalCount
_Dsx3FarEndIntervalCCVs_Object=MibTableColumn
dsx3FarEndIntervalCCVs=_Dsx3FarEndIntervalCCVs_Object((1,3,6,1,2,1,10,30,11,1,5),_Dsx3FarEndIntervalCCVs_Type())
dsx3FarEndIntervalCCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndIntervalCCVs.setStatus(_B)
_Dsx3FarEndIntervalUASs_Type=PerfIntervalCount
_Dsx3FarEndIntervalUASs_Object=MibTableColumn
dsx3FarEndIntervalUASs=_Dsx3FarEndIntervalUASs_Object((1,3,6,1,2,1,10,30,11,1,6),_Dsx3FarEndIntervalUASs_Type())
dsx3FarEndIntervalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndIntervalUASs.setStatus(_B)
_Dsx3FarEndIntervalValidData_Type=TruthValue
_Dsx3FarEndIntervalValidData_Object=MibTableColumn
dsx3FarEndIntervalValidData=_Dsx3FarEndIntervalValidData_Object((1,3,6,1,2,1,10,30,11,1,7),_Dsx3FarEndIntervalValidData_Type())
dsx3FarEndIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndIntervalValidData.setStatus(_B)
_Dsx3FarEndTotalTable_Object=MibTable
dsx3FarEndTotalTable=_Dsx3FarEndTotalTable_Object((1,3,6,1,2,1,10,30,12))
if mibBuilder.loadTexts:dsx3FarEndTotalTable.setStatus(_B)
_Dsx3FarEndTotalEntry_Object=MibTableRow
dsx3FarEndTotalEntry=_Dsx3FarEndTotalEntry_Object((1,3,6,1,2,1,10,30,12,1))
dsx3FarEndTotalEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:dsx3FarEndTotalEntry.setStatus(_B)
_Dsx3FarEndTotalIndex_Type=InterfaceIndex
_Dsx3FarEndTotalIndex_Object=MibTableColumn
dsx3FarEndTotalIndex=_Dsx3FarEndTotalIndex_Object((1,3,6,1,2,1,10,30,12,1,1),_Dsx3FarEndTotalIndex_Type())
dsx3FarEndTotalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndTotalIndex.setStatus(_B)
_Dsx3FarEndTotalCESs_Type=PerfTotalCount
_Dsx3FarEndTotalCESs_Object=MibTableColumn
dsx3FarEndTotalCESs=_Dsx3FarEndTotalCESs_Object((1,3,6,1,2,1,10,30,12,1,2),_Dsx3FarEndTotalCESs_Type())
dsx3FarEndTotalCESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndTotalCESs.setStatus(_B)
_Dsx3FarEndTotalCSESs_Type=PerfTotalCount
_Dsx3FarEndTotalCSESs_Object=MibTableColumn
dsx3FarEndTotalCSESs=_Dsx3FarEndTotalCSESs_Object((1,3,6,1,2,1,10,30,12,1,3),_Dsx3FarEndTotalCSESs_Type())
dsx3FarEndTotalCSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndTotalCSESs.setStatus(_B)
_Dsx3FarEndTotalCCVs_Type=PerfTotalCount
_Dsx3FarEndTotalCCVs_Object=MibTableColumn
dsx3FarEndTotalCCVs=_Dsx3FarEndTotalCCVs_Object((1,3,6,1,2,1,10,30,12,1,4),_Dsx3FarEndTotalCCVs_Type())
dsx3FarEndTotalCCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndTotalCCVs.setStatus(_B)
_Dsx3FarEndTotalUASs_Type=PerfTotalCount
_Dsx3FarEndTotalUASs_Object=MibTableColumn
dsx3FarEndTotalUASs=_Dsx3FarEndTotalUASs_Object((1,3,6,1,2,1,10,30,12,1,5),_Dsx3FarEndTotalUASs_Type())
dsx3FarEndTotalUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FarEndTotalUASs.setStatus(_B)
_Dsx3FracTable_Object=MibTable
dsx3FracTable=_Dsx3FracTable_Object((1,3,6,1,2,1,10,30,13))
if mibBuilder.loadTexts:dsx3FracTable.setStatus(_G)
_Dsx3FracEntry_Object=MibTableRow
dsx3FracEntry=_Dsx3FracEntry_Object((1,3,6,1,2,1,10,30,13,1))
dsx3FracEntry.setIndexNames((0,_A,_R),(0,_A,_S))
if mibBuilder.loadTexts:dsx3FracEntry.setStatus(_G)
class _Dsx3FracIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Dsx3FracIndex_Type.__name__=_D
_Dsx3FracIndex_Object=MibTableColumn
dsx3FracIndex=_Dsx3FracIndex_Object((1,3,6,1,2,1,10,30,13,1,1),_Dsx3FracIndex_Type())
dsx3FracIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FracIndex.setStatus(_G)
class _Dsx3FracNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_Dsx3FracNumber_Type.__name__=_D
_Dsx3FracNumber_Object=MibTableColumn
dsx3FracNumber=_Dsx3FracNumber_Object((1,3,6,1,2,1,10,30,13,1,2),_Dsx3FracNumber_Type())
dsx3FracNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx3FracNumber.setStatus(_G)
class _Dsx3FracIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dsx3FracIfIndex_Type.__name__=_D
_Dsx3FracIfIndex_Object=MibTableColumn
dsx3FracIfIndex=_Dsx3FracIfIndex_Object((1,3,6,1,2,1,10,30,13,1,3),_Dsx3FracIfIndex_Type())
dsx3FracIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3FracIfIndex.setStatus(_G)
_Ds3Conformance_ObjectIdentity=ObjectIdentity
ds3Conformance=_Ds3Conformance_ObjectIdentity((1,3,6,1,2,1,10,30,14))
_Ds3Groups_ObjectIdentity=ObjectIdentity
ds3Groups=_Ds3Groups_ObjectIdentity((1,3,6,1,2,1,10,30,14,1))
_Ds3Compliances_ObjectIdentity=ObjectIdentity
ds3Compliances=_Ds3Compliances_ObjectIdentity((1,3,6,1,2,1,10,30,14,2))
_Ds3Traps_ObjectIdentity=ObjectIdentity
ds3Traps=_Ds3Traps_ObjectIdentity((1,3,6,1,2,1,10,30,15))
ds3NearEndConfigGroup=ObjectGroup((1,3,6,1,2,1,10,30,14,1,1))
ds3NearEndConfigGroup.setObjects(*((_A,_H),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_T),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ds3NearEndConfigGroup.setStatus(_B)
ds3NearEndStatisticsGroup=ObjectGroup((1,3,6,1,2,1,10,30,14,1,2))
ds3NearEndStatisticsGroup.setObjects(*((_A,_I),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_J),(_A,_K),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_L),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:ds3NearEndStatisticsGroup.setStatus(_B)
ds3FarEndGroup=ObjectGroup((1,3,6,1,2,1,10,30,14,1,3))
ds3FarEndGroup.setObjects(*((_A,_M),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_N),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_O),(_A,_P),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_Q),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:ds3FarEndGroup.setStatus(_B)
ds3DeprecatedGroup=ObjectGroup((1,3,6,1,2,1,10,30,14,1,4))
ds3DeprecatedGroup.setObjects(*((_A,_AZ),(_A,_R),(_A,_S),(_A,_Aa)))
if mibBuilder.loadTexts:ds3DeprecatedGroup.setStatus(_G)
ds3NearEndOptionalConfigGroup=ObjectGroup((1,3,6,1,2,1,10,30,14,1,5))
ds3NearEndOptionalConfigGroup.setObjects(*((_A,_U),(_A,_Ab)))
if mibBuilder.loadTexts:ds3NearEndOptionalConfigGroup.setStatus(_B)
dsx3LineStatusChange=NotificationType((1,3,6,1,2,1,10,30,15,0,1))
dsx3LineStatusChange.setObjects(*((_A,_T),(_A,_U)))
if mibBuilder.loadTexts:dsx3LineStatusChange.setStatus(_B)
ds3NearEndOptionalTrapGroup=NotificationGroup((1,3,6,1,2,1,10,30,14,1,6))
ds3NearEndOptionalTrapGroup.setObjects((_A,_Ac))
if mibBuilder.loadTexts:ds3NearEndOptionalTrapGroup.setStatus(_B)
ds3Compliance=ModuleCompliance((1,3,6,1,2,1,10,30,14,2,1))
ds3Compliance.setObjects(*((_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:ds3Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ds3':ds3,'dsx3ConfigTable':dsx3ConfigTable,'dsx3ConfigEntry':dsx3ConfigEntry,_H:dsx3LineIndex,_AZ:dsx3IfIndex,_W:dsx3TimeElapsed,_X:dsx3ValidIntervals,_Y:dsx3LineType,_Z:dsx3LineCoding,_a:dsx3SendCode,_b:dsx3CircuitIdentifier,_c:dsx3LoopbackConfig,_T:dsx3LineStatus,_d:dsx3TransmitClockSource,_e:dsx3InvalidIntervals,_f:dsx3LineLength,_U:dsx3LineStatusLastChange,_Ab:dsx3LineStatusChangeTrapEnable,_g:dsx3LoopbackStatus,_h:dsx3Channelization,_i:dsx3Ds1ForRemoteLoop,'dsx3CurrentTable':dsx3CurrentTable,'dsx3CurrentEntry':dsx3CurrentEntry,_I:dsx3CurrentIndex,_j:dsx3CurrentPESs,_k:dsx3CurrentPSESs,_l:dsx3CurrentSEFSs,_m:dsx3CurrentUASs,_n:dsx3CurrentLCVs,_o:dsx3CurrentPCVs,_p:dsx3CurrentLESs,_q:dsx3CurrentCCVs,_r:dsx3CurrentCESs,_s:dsx3CurrentCSESs,'dsx3IntervalTable':dsx3IntervalTable,'dsx3IntervalEntry':dsx3IntervalEntry,_J:dsx3IntervalIndex,_K:dsx3IntervalNumber,_t:dsx3IntervalPESs,_u:dsx3IntervalPSESs,_v:dsx3IntervalSEFSs,_w:dsx3IntervalUASs,_x:dsx3IntervalLCVs,_y:dsx3IntervalPCVs,_z:dsx3IntervalLESs,_A0:dsx3IntervalCCVs,_A1:dsx3IntervalCESs,_A2:dsx3IntervalCSESs,_A3:dsx3IntervalValidData,'dsx3TotalTable':dsx3TotalTable,'dsx3TotalEntry':dsx3TotalEntry,_L:dsx3TotalIndex,_A4:dsx3TotalPESs,_A5:dsx3TotalPSESs,_A6:dsx3TotalSEFSs,_A7:dsx3TotalUASs,_A8:dsx3TotalLCVs,_A9:dsx3TotalPCVs,_AA:dsx3TotalLESs,_AB:dsx3TotalCCVs,_AC:dsx3TotalCESs,_AD:dsx3TotalCSESs,'dsx3FarEndConfigTable':dsx3FarEndConfigTable,'dsx3FarEndConfigEntry':dsx3FarEndConfigEntry,_M:dsx3FarEndLineIndex,_AE:dsx3FarEndEquipCode,_AF:dsx3FarEndLocationIDCode,_AG:dsx3FarEndFrameIDCode,_AH:dsx3FarEndUnitCode,_AI:dsx3FarEndFacilityIDCode,'dsx3FarEndCurrentTable':dsx3FarEndCurrentTable,'dsx3FarEndCurrentEntry':dsx3FarEndCurrentEntry,_N:dsx3FarEndCurrentIndex,_AJ:dsx3FarEndTimeElapsed,_AK:dsx3FarEndValidIntervals,_AL:dsx3FarEndCurrentCESs,_AM:dsx3FarEndCurrentCSESs,_AN:dsx3FarEndCurrentCCVs,_AO:dsx3FarEndCurrentUASs,_AP:dsx3FarEndInvalidIntervals,'dsx3FarEndIntervalTable':dsx3FarEndIntervalTable,'dsx3FarEndIntervalEntry':dsx3FarEndIntervalEntry,_O:dsx3FarEndIntervalIndex,_P:dsx3FarEndIntervalNumber,_AQ:dsx3FarEndIntervalCESs,_AR:dsx3FarEndIntervalCSESs,_AS:dsx3FarEndIntervalCCVs,_AT:dsx3FarEndIntervalUASs,_AU:dsx3FarEndIntervalValidData,'dsx3FarEndTotalTable':dsx3FarEndTotalTable,'dsx3FarEndTotalEntry':dsx3FarEndTotalEntry,_Q:dsx3FarEndTotalIndex,_AV:dsx3FarEndTotalCESs,_AW:dsx3FarEndTotalCSESs,_AX:dsx3FarEndTotalCCVs,_AY:dsx3FarEndTotalUASs,'dsx3FracTable':dsx3FracTable,'dsx3FracEntry':dsx3FracEntry,_R:dsx3FracIndex,_S:dsx3FracNumber,_Aa:dsx3FracIfIndex,'ds3Conformance':ds3Conformance,'ds3Groups':ds3Groups,_Ad:ds3NearEndConfigGroup,_Ae:ds3NearEndStatisticsGroup,_Af:ds3FarEndGroup,'ds3DeprecatedGroup':ds3DeprecatedGroup,_Ah:ds3NearEndOptionalConfigGroup,_Ag:ds3NearEndOptionalTrapGroup,'ds3Compliances':ds3Compliances,'ds3Compliance':ds3Compliance,'ds3Traps':ds3Traps,_Ac:dsx3LineStatusChange})