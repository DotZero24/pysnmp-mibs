_q='ntcAsiInConfGrpV1Standard'
_p='ntcAsiInNpRangeTimeWindow'
_o='ntcAsiInNpRangeThrMaxRate'
_n='ntcAsiInNpRangeThrEnable'
_m='ntcAsiInInputTsBitRate'
_l='ntcAsiInAlmNoInputDataAsi2'
_k='ntcAsiInAlmNoInputDataAsi1'
_j='ntcAsiInAlmNoInputSignalAsi2'
_i='ntcAsiInAlmNoInputSignalAsi1'
_h='ntcAsiInAlmBufferOverflow'
_g='ntcAsiInAlmInvalidTsBitRate'
_f='ntcAsiInAlmNoInputData'
_e='ntcAsiInAlmNoInputSignal'
_d='ntcAsiInAlmGeneralAsiInput'
_c='ntcAsiInPrbsMonErrorRatio'
_b='ntcAsiInPrbsMonErrorRate'
_a='ntcAsiInPrbsMonErrorCount'
_Z='ntcAsiInPrbsMonSyncSeconds'
_Y='ntcAsiInPrbsMonState'
_X='ntcAsiInPrbsMonPidValue'
_W='ntcAsiInPrbsMonPidHandling'
_V='ntcAsiInPrbsMonEnable'
_U='ntcAsiInPrbsGenNumberNullPkt'
_T='ntcAsiInPrbsGenNumberDataPkt'
_S='ntcAsiInPrbsGenPidValue'
_R='ntcAsiInPrbsGenPidHandling'
_Q='ntcAsiInPrbsGenType'
_P='ntcAsiInPrbsGenTsBitRate'
_O='ntcAsiInInputIfSwitchCount'
_N='ntcAsiInInputFraming'
_M='ntcAsiInMeasuredInputTsBitRate'
_L='ntcAsiInInlineSplitter'
_K='ntcAsiInActiveInput'
_J='ntcAsiInInputSelection'
_I='NtcPid'
_H='bps'
_G='NtcEnable'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='NEWTEC-ASIIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Float32TC,=mibBuilder.importSymbols('FLOAT-TC-MIB','Float32TC')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable,NtcPid=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_G,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcAsiIn=ModuleIdentity((1,3,6,1,4,1,5835,5,2,800))
if mibBuilder.loadTexts:ntcAsiIn.setRevisions(('2018-04-04 10:00','2017-07-10 12:00','2014-09-09 09:00','2012-06-28 12:00'))
_NtcAsiInObjects_ObjectIdentity=ObjectIdentity
ntcAsiInObjects=_NtcAsiInObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,800,1))
if mibBuilder.loadTexts:ntcAsiInObjects.setStatus(_A)
class _NtcAsiInInputSelection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,40,41,42,100)));namedValues=NamedValues(*(('none',0),('asi1',1),('asi2',2),('asi1or2',40),('asi1before2',41),('asi2before1',42),('prbsgenerator',100)))
_NtcAsiInInputSelection_Type.__name__=_E
_NtcAsiInInputSelection_Object=MibScalar
ntcAsiInInputSelection=_NtcAsiInInputSelection_Object((1,3,6,1,4,1,5835,5,2,800,1,1),_NtcAsiInInputSelection_Type())
ntcAsiInInputSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInInputSelection.setStatus(_A)
class _NtcAsiInActiveInput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('asi1',1),('asi2',2)))
_NtcAsiInActiveInput_Type.__name__=_E
_NtcAsiInActiveInput_Object=MibScalar
ntcAsiInActiveInput=_NtcAsiInActiveInput_Object((1,3,6,1,4,1,5835,5,2,800,1,2),_NtcAsiInActiveInput_Type())
ntcAsiInActiveInput.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInActiveInput.setStatus(_A)
class _NtcAsiInInlineSplitter_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('e3dBSplitter',1),('e6dBSplitter',2)))
_NtcAsiInInlineSplitter_Type.__name__=_E
_NtcAsiInInlineSplitter_Object=MibScalar
ntcAsiInInlineSplitter=_NtcAsiInInlineSplitter_Object((1,3,6,1,4,1,5835,5,2,800,1,3),_NtcAsiInInlineSplitter_Type())
ntcAsiInInlineSplitter.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInInlineSplitter.setStatus(_A)
_NtcAsiInMeasuredInputTsBitRate_Type=Unsigned32
_NtcAsiInMeasuredInputTsBitRate_Object=MibScalar
ntcAsiInMeasuredInputTsBitRate=_NtcAsiInMeasuredInputTsBitRate_Object((1,3,6,1,4,1,5835,5,2,800,1,4),_NtcAsiInMeasuredInputTsBitRate_Type())
ntcAsiInMeasuredInputTsBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInMeasuredInputTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcAsiInMeasuredInputTsBitRate.setUnits(_H)
class _NtcAsiInInputFraming_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ts188',0),('ts204',1)))
_NtcAsiInInputFraming_Type.__name__=_E
_NtcAsiInInputFraming_Object=MibScalar
ntcAsiInInputFraming=_NtcAsiInInputFraming_Object((1,3,6,1,4,1,5835,5,2,800,1,5),_NtcAsiInInputFraming_Type())
ntcAsiInInputFraming.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInInputFraming.setStatus(_A)
_NtcAsiInInputIfSwitchCount_Type=Counter32
_NtcAsiInInputIfSwitchCount_Object=MibScalar
ntcAsiInInputIfSwitchCount=_NtcAsiInInputIfSwitchCount_Object((1,3,6,1,4,1,5835,5,2,800,1,6),_NtcAsiInInputIfSwitchCount_Type())
ntcAsiInInputIfSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInInputIfSwitchCount.setStatus(_A)
_NtcAsiInPrbsGenerator_ObjectIdentity=ObjectIdentity
ntcAsiInPrbsGenerator=_NtcAsiInPrbsGenerator_ObjectIdentity((1,3,6,1,4,1,5835,5,2,800,1,7))
if mibBuilder.loadTexts:ntcAsiInPrbsGenerator.setStatus(_A)
class _NtcAsiInPrbsGenTsBitRate_Type(Unsigned32):defaultValue=1000000
_NtcAsiInPrbsGenTsBitRate_Type.__name__=_F
_NtcAsiInPrbsGenTsBitRate_Object=MibScalar
ntcAsiInPrbsGenTsBitRate=_NtcAsiInPrbsGenTsBitRate_Object((1,3,6,1,4,1,5835,5,2,800,1,7,1),_NtcAsiInPrbsGenTsBitRate_Type())
ntcAsiInPrbsGenTsBitRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInPrbsGenTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcAsiInPrbsGenTsBitRate.setUnits(_H)
class _NtcAsiInPrbsGenType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('prbs',0),('counter',1)))
_NtcAsiInPrbsGenType_Type.__name__=_E
_NtcAsiInPrbsGenType_Object=MibScalar
ntcAsiInPrbsGenType=_NtcAsiInPrbsGenType_Object((1,3,6,1,4,1,5835,5,2,800,1,7,2),_NtcAsiInPrbsGenType_Type())
ntcAsiInPrbsGenType.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInPrbsGenType.setStatus(_A)
class _NtcAsiInPrbsGenPidHandling_Type(NtcEnable):defaultValue=0
_NtcAsiInPrbsGenPidHandling_Type.__name__=_G
_NtcAsiInPrbsGenPidHandling_Object=MibScalar
ntcAsiInPrbsGenPidHandling=_NtcAsiInPrbsGenPidHandling_Object((1,3,6,1,4,1,5835,5,2,800,1,7,3),_NtcAsiInPrbsGenPidHandling_Type())
ntcAsiInPrbsGenPidHandling.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInPrbsGenPidHandling.setStatus(_A)
class _NtcAsiInPrbsGenPidValue_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_NtcAsiInPrbsGenPidValue_Type.__name__=_F
_NtcAsiInPrbsGenPidValue_Object=MibScalar
ntcAsiInPrbsGenPidValue=_NtcAsiInPrbsGenPidValue_Object((1,3,6,1,4,1,5835,5,2,800,1,7,4),_NtcAsiInPrbsGenPidValue_Type())
ntcAsiInPrbsGenPidValue.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInPrbsGenPidValue.setStatus(_A)
class _NtcAsiInPrbsGenNumberDataPkt_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NtcAsiInPrbsGenNumberDataPkt_Type.__name__=_F
_NtcAsiInPrbsGenNumberDataPkt_Object=MibScalar
ntcAsiInPrbsGenNumberDataPkt=_NtcAsiInPrbsGenNumberDataPkt_Object((1,3,6,1,4,1,5835,5,2,800,1,7,5),_NtcAsiInPrbsGenNumberDataPkt_Type())
ntcAsiInPrbsGenNumberDataPkt.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInPrbsGenNumberDataPkt.setStatus(_A)
class _NtcAsiInPrbsGenNumberNullPkt_Type(Unsigned32):defaultValue=0
_NtcAsiInPrbsGenNumberNullPkt_Type.__name__=_F
_NtcAsiInPrbsGenNumberNullPkt_Object=MibScalar
ntcAsiInPrbsGenNumberNullPkt=_NtcAsiInPrbsGenNumberNullPkt_Object((1,3,6,1,4,1,5835,5,2,800,1,7,6),_NtcAsiInPrbsGenNumberNullPkt_Type())
ntcAsiInPrbsGenNumberNullPkt.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInPrbsGenNumberNullPkt.setStatus(_A)
_NtcAsiInPrbsMonitor_ObjectIdentity=ObjectIdentity
ntcAsiInPrbsMonitor=_NtcAsiInPrbsMonitor_ObjectIdentity((1,3,6,1,4,1,5835,5,2,800,1,8))
if mibBuilder.loadTexts:ntcAsiInPrbsMonitor.setStatus(_A)
class _NtcAsiInPrbsMonEnable_Type(NtcEnable):defaultValue=0
_NtcAsiInPrbsMonEnable_Type.__name__=_G
_NtcAsiInPrbsMonEnable_Object=MibScalar
ntcAsiInPrbsMonEnable=_NtcAsiInPrbsMonEnable_Object((1,3,6,1,4,1,5835,5,2,800,1,8,1),_NtcAsiInPrbsMonEnable_Type())
ntcAsiInPrbsMonEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInPrbsMonEnable.setStatus(_A)
class _NtcAsiInPrbsMonPidHandling_Type(NtcEnable):defaultValue=0
_NtcAsiInPrbsMonPidHandling_Type.__name__=_G
_NtcAsiInPrbsMonPidHandling_Object=MibScalar
ntcAsiInPrbsMonPidHandling=_NtcAsiInPrbsMonPidHandling_Object((1,3,6,1,4,1,5835,5,2,800,1,8,2),_NtcAsiInPrbsMonPidHandling_Type())
ntcAsiInPrbsMonPidHandling.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInPrbsMonPidHandling.setStatus(_A)
class _NtcAsiInPrbsMonPidValue_Type(NtcPid):defaultValue=1
_NtcAsiInPrbsMonPidValue_Type.__name__=_I
_NtcAsiInPrbsMonPidValue_Object=MibScalar
ntcAsiInPrbsMonPidValue=_NtcAsiInPrbsMonPidValue_Object((1,3,6,1,4,1,5835,5,2,800,1,8,3),_NtcAsiInPrbsMonPidValue_Type())
ntcAsiInPrbsMonPidValue.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInPrbsMonPidValue.setStatus(_A)
class _NtcAsiInPrbsMonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('unsync',1),('prbs',2),('ais',3)))
_NtcAsiInPrbsMonState_Type.__name__=_E
_NtcAsiInPrbsMonState_Object=MibScalar
ntcAsiInPrbsMonState=_NtcAsiInPrbsMonState_Object((1,3,6,1,4,1,5835,5,2,800,1,8,4),_NtcAsiInPrbsMonState_Type())
ntcAsiInPrbsMonState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInPrbsMonState.setStatus(_A)
_NtcAsiInPrbsMonSyncSeconds_Type=Unsigned32
_NtcAsiInPrbsMonSyncSeconds_Object=MibScalar
ntcAsiInPrbsMonSyncSeconds=_NtcAsiInPrbsMonSyncSeconds_Object((1,3,6,1,4,1,5835,5,2,800,1,8,5),_NtcAsiInPrbsMonSyncSeconds_Type())
ntcAsiInPrbsMonSyncSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInPrbsMonSyncSeconds.setStatus(_A)
_NtcAsiInPrbsMonErrorCount_Type=Counter32
_NtcAsiInPrbsMonErrorCount_Object=MibScalar
ntcAsiInPrbsMonErrorCount=_NtcAsiInPrbsMonErrorCount_Object((1,3,6,1,4,1,5835,5,2,800,1,8,6),_NtcAsiInPrbsMonErrorCount_Type())
ntcAsiInPrbsMonErrorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInPrbsMonErrorCount.setStatus(_A)
class _NtcAsiInPrbsMonErrorRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,21474836470))
_NtcAsiInPrbsMonErrorRate_Type.__name__=_F
_NtcAsiInPrbsMonErrorRate_Object=MibScalar
ntcAsiInPrbsMonErrorRate=_NtcAsiInPrbsMonErrorRate_Object((1,3,6,1,4,1,5835,5,2,800,1,8,7),_NtcAsiInPrbsMonErrorRate_Type())
ntcAsiInPrbsMonErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInPrbsMonErrorRate.setStatus(_A)
_NtcAsiInPrbsMonErrorRatio_Type=Float32TC
_NtcAsiInPrbsMonErrorRatio_Object=MibScalar
ntcAsiInPrbsMonErrorRatio=_NtcAsiInPrbsMonErrorRatio_Object((1,3,6,1,4,1,5835,5,2,800,1,8,8),_NtcAsiInPrbsMonErrorRatio_Type())
ntcAsiInPrbsMonErrorRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInPrbsMonErrorRatio.setStatus(_A)
_NtcAsiInAlarm_ObjectIdentity=ObjectIdentity
ntcAsiInAlarm=_NtcAsiInAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,800,1,9))
if mibBuilder.loadTexts:ntcAsiInAlarm.setStatus(_A)
_NtcAsiInAlmGeneralAsiInput_Type=NtcAlarmState
_NtcAsiInAlmGeneralAsiInput_Object=MibScalar
ntcAsiInAlmGeneralAsiInput=_NtcAsiInAlmGeneralAsiInput_Object((1,3,6,1,4,1,5835,5,2,800,1,9,1),_NtcAsiInAlmGeneralAsiInput_Type())
ntcAsiInAlmGeneralAsiInput.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInAlmGeneralAsiInput.setStatus(_A)
_NtcAsiInAlmNoInputSignal_Type=NtcAlarmState
_NtcAsiInAlmNoInputSignal_Object=MibScalar
ntcAsiInAlmNoInputSignal=_NtcAsiInAlmNoInputSignal_Object((1,3,6,1,4,1,5835,5,2,800,1,9,2),_NtcAsiInAlmNoInputSignal_Type())
ntcAsiInAlmNoInputSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInAlmNoInputSignal.setStatus(_A)
_NtcAsiInAlmNoInputData_Type=NtcAlarmState
_NtcAsiInAlmNoInputData_Object=MibScalar
ntcAsiInAlmNoInputData=_NtcAsiInAlmNoInputData_Object((1,3,6,1,4,1,5835,5,2,800,1,9,3),_NtcAsiInAlmNoInputData_Type())
ntcAsiInAlmNoInputData.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInAlmNoInputData.setStatus(_A)
_NtcAsiInAlmInvalidTsBitRate_Type=NtcAlarmState
_NtcAsiInAlmInvalidTsBitRate_Object=MibScalar
ntcAsiInAlmInvalidTsBitRate=_NtcAsiInAlmInvalidTsBitRate_Object((1,3,6,1,4,1,5835,5,2,800,1,9,4),_NtcAsiInAlmInvalidTsBitRate_Type())
ntcAsiInAlmInvalidTsBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInAlmInvalidTsBitRate.setStatus(_A)
_NtcAsiInAlmBufferOverflow_Type=NtcAlarmState
_NtcAsiInAlmBufferOverflow_Object=MibScalar
ntcAsiInAlmBufferOverflow=_NtcAsiInAlmBufferOverflow_Object((1,3,6,1,4,1,5835,5,2,800,1,9,5),_NtcAsiInAlmBufferOverflow_Type())
ntcAsiInAlmBufferOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInAlmBufferOverflow.setStatus(_A)
_NtcAsiInAlmNoInputSignalAsi1_Type=NtcAlarmState
_NtcAsiInAlmNoInputSignalAsi1_Object=MibScalar
ntcAsiInAlmNoInputSignalAsi1=_NtcAsiInAlmNoInputSignalAsi1_Object((1,3,6,1,4,1,5835,5,2,800,1,9,6),_NtcAsiInAlmNoInputSignalAsi1_Type())
ntcAsiInAlmNoInputSignalAsi1.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInAlmNoInputSignalAsi1.setStatus(_A)
_NtcAsiInAlmNoInputSignalAsi2_Type=NtcAlarmState
_NtcAsiInAlmNoInputSignalAsi2_Object=MibScalar
ntcAsiInAlmNoInputSignalAsi2=_NtcAsiInAlmNoInputSignalAsi2_Object((1,3,6,1,4,1,5835,5,2,800,1,9,7),_NtcAsiInAlmNoInputSignalAsi2_Type())
ntcAsiInAlmNoInputSignalAsi2.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInAlmNoInputSignalAsi2.setStatus(_A)
_NtcAsiInAlmNoInputDataAsi1_Type=NtcAlarmState
_NtcAsiInAlmNoInputDataAsi1_Object=MibScalar
ntcAsiInAlmNoInputDataAsi1=_NtcAsiInAlmNoInputDataAsi1_Object((1,3,6,1,4,1,5835,5,2,800,1,9,8),_NtcAsiInAlmNoInputDataAsi1_Type())
ntcAsiInAlmNoInputDataAsi1.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInAlmNoInputDataAsi1.setStatus(_A)
_NtcAsiInAlmNoInputDataAsi2_Type=NtcAlarmState
_NtcAsiInAlmNoInputDataAsi2_Object=MibScalar
ntcAsiInAlmNoInputDataAsi2=_NtcAsiInAlmNoInputDataAsi2_Object((1,3,6,1,4,1,5835,5,2,800,1,9,9),_NtcAsiInAlmNoInputDataAsi2_Type())
ntcAsiInAlmNoInputDataAsi2.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiInAlmNoInputDataAsi2.setStatus(_A)
class _NtcAsiInInputTsBitRate_Type(Unsigned32):defaultValue=1000000
_NtcAsiInInputTsBitRate_Type.__name__=_F
_NtcAsiInInputTsBitRate_Object=MibScalar
ntcAsiInInputTsBitRate=_NtcAsiInInputTsBitRate_Object((1,3,6,1,4,1,5835,5,2,800,1,10),_NtcAsiInInputTsBitRate_Type())
ntcAsiInInputTsBitRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInInputTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcAsiInInputTsBitRate.setUnits(_H)
_NtcAsiInNpRangeThr_ObjectIdentity=ObjectIdentity
ntcAsiInNpRangeThr=_NtcAsiInNpRangeThr_ObjectIdentity((1,3,6,1,4,1,5835,5,2,800,1,11))
if mibBuilder.loadTexts:ntcAsiInNpRangeThr.setStatus(_A)
class _NtcAsiInNpRangeThrEnable_Type(NtcEnable):defaultValue=0
_NtcAsiInNpRangeThrEnable_Type.__name__=_G
_NtcAsiInNpRangeThrEnable_Object=MibScalar
ntcAsiInNpRangeThrEnable=_NtcAsiInNpRangeThrEnable_Object((1,3,6,1,4,1,5835,5,2,800,1,11,1),_NtcAsiInNpRangeThrEnable_Type())
ntcAsiInNpRangeThrEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInNpRangeThrEnable.setStatus(_A)
class _NtcAsiInNpRangeThrMaxRate_Type(Unsigned32):defaultValue=0
_NtcAsiInNpRangeThrMaxRate_Type.__name__=_F
_NtcAsiInNpRangeThrMaxRate_Object=MibScalar
ntcAsiInNpRangeThrMaxRate=_NtcAsiInNpRangeThrMaxRate_Object((1,3,6,1,4,1,5835,5,2,800,1,11,2),_NtcAsiInNpRangeThrMaxRate_Type())
ntcAsiInNpRangeThrMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInNpRangeThrMaxRate.setStatus(_A)
if mibBuilder.loadTexts:ntcAsiInNpRangeThrMaxRate.setUnits(_H)
class _NtcAsiInNpRangeTimeWindow_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_NtcAsiInNpRangeTimeWindow_Type.__name__=_E
_NtcAsiInNpRangeTimeWindow_Object=MibScalar
ntcAsiInNpRangeTimeWindow=_NtcAsiInNpRangeTimeWindow_Object((1,3,6,1,4,1,5835,5,2,800,1,11,3),_NtcAsiInNpRangeTimeWindow_Type())
ntcAsiInNpRangeTimeWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAsiInNpRangeTimeWindow.setStatus(_A)
if mibBuilder.loadTexts:ntcAsiInNpRangeTimeWindow.setUnits('s')
_NtcAsiInConformance_ObjectIdentity=ObjectIdentity
ntcAsiInConformance=_NtcAsiInConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,800,2))
if mibBuilder.loadTexts:ntcAsiInConformance.setStatus(_A)
_NtcAsiInConfCompliance_ObjectIdentity=ObjectIdentity
ntcAsiInConfCompliance=_NtcAsiInConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,800,2,1))
if mibBuilder.loadTexts:ntcAsiInConfCompliance.setStatus(_A)
_NtcAsiInConfGroup_ObjectIdentity=ObjectIdentity
ntcAsiInConfGroup=_NtcAsiInConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,800,2,2))
if mibBuilder.loadTexts:ntcAsiInConfGroup.setStatus(_A)
ntcAsiInConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,800,2,2,1))
ntcAsiInConfGrpV1Standard.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:ntcAsiInConfGrpV1Standard.setStatus(_A)
ntcAsiInConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,800,2,1,1))
ntcAsiInConfCompV1Standard.setObjects((_B,_q))
if mibBuilder.loadTexts:ntcAsiInConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcAsiIn':ntcAsiIn,'ntcAsiInObjects':ntcAsiInObjects,_J:ntcAsiInInputSelection,_K:ntcAsiInActiveInput,_L:ntcAsiInInlineSplitter,_M:ntcAsiInMeasuredInputTsBitRate,_N:ntcAsiInInputFraming,_O:ntcAsiInInputIfSwitchCount,'ntcAsiInPrbsGenerator':ntcAsiInPrbsGenerator,_P:ntcAsiInPrbsGenTsBitRate,_Q:ntcAsiInPrbsGenType,_R:ntcAsiInPrbsGenPidHandling,_S:ntcAsiInPrbsGenPidValue,_T:ntcAsiInPrbsGenNumberDataPkt,_U:ntcAsiInPrbsGenNumberNullPkt,'ntcAsiInPrbsMonitor':ntcAsiInPrbsMonitor,_V:ntcAsiInPrbsMonEnable,_W:ntcAsiInPrbsMonPidHandling,_X:ntcAsiInPrbsMonPidValue,_Y:ntcAsiInPrbsMonState,_Z:ntcAsiInPrbsMonSyncSeconds,_a:ntcAsiInPrbsMonErrorCount,_b:ntcAsiInPrbsMonErrorRate,_c:ntcAsiInPrbsMonErrorRatio,'ntcAsiInAlarm':ntcAsiInAlarm,_d:ntcAsiInAlmGeneralAsiInput,_e:ntcAsiInAlmNoInputSignal,_f:ntcAsiInAlmNoInputData,_g:ntcAsiInAlmInvalidTsBitRate,_h:ntcAsiInAlmBufferOverflow,_i:ntcAsiInAlmNoInputSignalAsi1,_j:ntcAsiInAlmNoInputSignalAsi2,_k:ntcAsiInAlmNoInputDataAsi1,_l:ntcAsiInAlmNoInputDataAsi2,_m:ntcAsiInInputTsBitRate,'ntcAsiInNpRangeThr':ntcAsiInNpRangeThr,_n:ntcAsiInNpRangeThrEnable,_o:ntcAsiInNpRangeThrMaxRate,_p:ntcAsiInNpRangeTimeWindow,'ntcAsiInConformance':ntcAsiInConformance,'ntcAsiInConfCompliance':ntcAsiInConfCompliance,'ntcAsiInConfCompV1Standard':ntcAsiInConfCompV1Standard,'ntcAsiInConfGroup':ntcAsiInConfGroup,_q:ntcAsiInConfGrpV1Standard})