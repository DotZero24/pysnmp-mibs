_A2='jnxSoamPmNotificationObjCurrentState'
_A1='jnxSoamPmNotificationAccTotalFlaps'
_A0='jnxSoamPmNotificationTotalFlaps'
_z='jnxSoamPmNotificationObjThresholdLastValue'
_y='jnxSoamPmNotificationObjSuspect'
_x='jnxSoamPmNotificationObjThresholdValue'
_w='jnxSoamPmNotificationObjCrossingType'
_v='jnxSoamDmCfgSessionStatus'
_u='jnxSoamLmCfgSessionStatus'
_t='jnxSoamPmMepEntry'
_s='clearAlarm'
_r='setAlarm'
_q='aboveAlarm'
_p='jnxSoamDmThresholdCfgIndex'
_o='jnxSoamLmHistoryAvailStatsIndex'
_n='jnxSoamLmThresholdCfgIndex'
_m='jnxSoamLmHistoryStatsIndex'
_l='proactive'
_k='seconds'
_j='bSoamPdusReceived'
_i='bSoamPdusSent'
_h='jnxSoamPmNotificationObjThresholdConfig'
_g='jnxSoamPmNotificationObjThresholdId'
_f='jnxSoamDmHistoryStatsIndex'
_e='not-accessible'
_d='JnxSoamTcTestPatternType'
_c='JnxSoamTcDataPatternType'
_b='Dot1agCfmMepIdOrZero'
_a='jnxSoamPmNotificationObjDateAndTime'
_Z='jnxSoamDmCfgMeasBinNumber'
_Y='jnxSoamDmCfgMeasBinType'
_X='0000010100000000'
_W='jnxSoamPmNotificationObjDestinationMep'
_V='minutes'
_U='JnxSoamTcOperationTimeType'
_T='TimeInterval'
_S='DateAndTime'
_R='Bits'
_Q='OctetString'
_P='Integer32'
_O='jnxSoamLmCfgIndex'
_N='jnxSoamDmCfgIndex'
_M='accessible-for-notify'
_L='TruthValue'
_K='dot1agCfmMepIdentifier'
_J='dot1agCfmMdIndex'
_I='dot1agCfmMaIndex'
_H='read-create'
_G='milli-percent'
_F='IEEE8021-CFM-MIB'
_E='JUNIPER-SOAM-PM-MIB'
_D='microseconds'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1afCfmIndexIntegerNextFree,Dot1agCfmMepIdOrZero,dot1agCfmMaIndex,dot1agCfmMdIndex,dot1agCfmMepEntry,dot1agCfmMepIdentifier=mibBuilder.importSymbols(_F,'Dot1afCfmIndexIntegerNextFree',_b,_I,_J,'dot1agCfmMepEntry',_K)
IEEE8021PriorityValue,IEEE8021VlanIndex,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PriorityValue','IEEE8021VlanIndex','ieee802dot1mibs')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
LldpChassisId,LldpChassisIdSubtype,LldpPortId,LldpPortIdSubtype=mibBuilder.importSymbols('LLDP-MIB','LldpChassisId','LldpChassisIdSubtype','LldpPortId','LldpPortIdSubtype')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_R,'Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TAddress,TDomain,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_S,'DisplayString','MacAddress','PhysAddress','RowStatus','TAddress','TDomain','TextualConvention',_T,'TimeStamp',_L)
jnxSoamPmMib=ModuleIdentity((1,3,6,1,4,1,2636,3,78))
if mibBuilder.loadTexts:jnxSoamPmMib.setRevisions(('2012-01-13 12:00','2016-05-31 00:00'))
class JnxSoamTcTestPatternType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('null',1),('nullCrc32',2),('prbs',3),('prbsCrc32',4)))
class JnxSoamTcDataPatternType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('zeroPattern',1),('onesPattern',2)))
class JnxSoamTcOperationTimeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('immediate',2),('relative',3),('fixed',4)))
class JnxSoamTcAvailabilityType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('available',1),('unavailable',2),('unknown',3)))
class JnxSoamTcDelayMeasurementBinType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('twoWayFrameDelay',1),('forwardFrameDelay',2),('backwardFrameDelay',3),('twoWayIfdv',4),('forwardIfdv',5),('backwardIfdv',6),('twoWayFrameDelayRange',7),('forwardFrameDelayRange',8),('backwardFrameDelayRange',9)))
_JnxSoamPmNotifications_ObjectIdentity=ObjectIdentity
jnxSoamPmNotifications=_JnxSoamPmNotifications_ObjectIdentity((1,3,6,1,4,1,2636,3,78,0))
_JnxSoamPmMibObjects_ObjectIdentity=ObjectIdentity
jnxSoamPmMibObjects=_JnxSoamPmMibObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,78,1))
_JnxSoamPmMep_ObjectIdentity=ObjectIdentity
jnxSoamPmMep=_JnxSoamPmMep_ObjectIdentity((1,3,6,1,4,1,2636,3,78,1,1))
_JnxSoamPmMepTable_Object=MibTable
jnxSoamPmMepTable=_JnxSoamPmMepTable_Object((1,3,6,1,4,1,2636,3,78,1,1,1))
if mibBuilder.loadTexts:jnxSoamPmMepTable.setStatus(_A)
_JnxSoamPmMepEntry_Object=MibTableRow
jnxSoamPmMepEntry=_JnxSoamPmMepEntry_Object((1,3,6,1,4,1,2636,3,78,1,1,1,1))
if mibBuilder.loadTexts:jnxSoamPmMepEntry.setStatus(_A)
_JnxSoamPmMepOperNextIndex_Type=Dot1afCfmIndexIntegerNextFree
_JnxSoamPmMepOperNextIndex_Object=MibTableColumn
jnxSoamPmMepOperNextIndex=_JnxSoamPmMepOperNextIndex_Object((1,3,6,1,4,1,2636,3,78,1,1,1,1,1),_JnxSoamPmMepOperNextIndex_Type())
jnxSoamPmMepOperNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamPmMepOperNextIndex.setStatus(_A)
class _JnxSoamPmMepLmSingleEndedResponder_Type(TruthValue):defaultValue=1
_JnxSoamPmMepLmSingleEndedResponder_Type.__name__=_L
_JnxSoamPmMepLmSingleEndedResponder_Object=MibTableColumn
jnxSoamPmMepLmSingleEndedResponder=_JnxSoamPmMepLmSingleEndedResponder_Object((1,3,6,1,4,1,2636,3,78,1,1,1,1,2),_JnxSoamPmMepLmSingleEndedResponder_Type())
jnxSoamPmMepLmSingleEndedResponder.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamPmMepLmSingleEndedResponder.setStatus(_A)
class _JnxSoamPmMepSlmSingleEndedResponder_Type(TruthValue):defaultValue=1
_JnxSoamPmMepSlmSingleEndedResponder_Type.__name__=_L
_JnxSoamPmMepSlmSingleEndedResponder_Object=MibTableColumn
jnxSoamPmMepSlmSingleEndedResponder=_JnxSoamPmMepSlmSingleEndedResponder_Object((1,3,6,1,4,1,2636,3,78,1,1,1,1,3),_JnxSoamPmMepSlmSingleEndedResponder_Type())
jnxSoamPmMepSlmSingleEndedResponder.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamPmMepSlmSingleEndedResponder.setStatus(_A)
class _JnxSoamPmMepDmSingleEndedResponder_Type(TruthValue):defaultValue=1
_JnxSoamPmMepDmSingleEndedResponder_Type.__name__=_L
_JnxSoamPmMepDmSingleEndedResponder_Object=MibTableColumn
jnxSoamPmMepDmSingleEndedResponder=_JnxSoamPmMepDmSingleEndedResponder_Object((1,3,6,1,4,1,2636,3,78,1,1,1,1,4),_JnxSoamPmMepDmSingleEndedResponder_Type())
jnxSoamPmMepDmSingleEndedResponder.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamPmMepDmSingleEndedResponder.setStatus(_A)
_JnxSoamPmLmObjects_ObjectIdentity=ObjectIdentity
jnxSoamPmLmObjects=_JnxSoamPmLmObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,78,1,2))
_JnxSoamLmCfgTable_Object=MibTable
jnxSoamLmCfgTable=_JnxSoamLmCfgTable_Object((1,3,6,1,4,1,2636,3,78,1,2,1))
if mibBuilder.loadTexts:jnxSoamLmCfgTable.setStatus(_A)
_JnxSoamLmCfgEntry_Object=MibTableRow
jnxSoamLmCfgEntry=_JnxSoamLmCfgEntry_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1))
jnxSoamLmCfgEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_O))
if mibBuilder.loadTexts:jnxSoamLmCfgEntry.setStatus(_A)
class _JnxSoamLmCfgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_JnxSoamLmCfgIndex_Type.__name__=_C
_JnxSoamLmCfgIndex_Object=MibTableColumn
jnxSoamLmCfgIndex=_JnxSoamLmCfgIndex_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,1),_JnxSoamLmCfgIndex_Type())
jnxSoamLmCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgIndex.setStatus(_A)
class _JnxSoamLmCfgType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lmLmm',1),('lmSlm',2),('lmCcm',3)))
_JnxSoamLmCfgType_Type.__name__=_P
_JnxSoamLmCfgType_Object=MibTableColumn
jnxSoamLmCfgType=_JnxSoamLmCfgType_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,2),_JnxSoamLmCfgType_Type())
jnxSoamLmCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgType.setStatus(_A)
class _JnxSoamLmCfgVersion_Type(Unsigned32):defaultValue=0
_JnxSoamLmCfgVersion_Type.__name__=_C
_JnxSoamLmCfgVersion_Object=MibTableColumn
jnxSoamLmCfgVersion=_JnxSoamLmCfgVersion_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,3),_JnxSoamLmCfgVersion_Type())
jnxSoamLmCfgVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgVersion.setStatus(_A)
class _JnxSoamLmCfgEnabled_Type(TruthValue):defaultValue=1
_JnxSoamLmCfgEnabled_Type.__name__=_L
_JnxSoamLmCfgEnabled_Object=MibTableColumn
jnxSoamLmCfgEnabled=_JnxSoamLmCfgEnabled_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,4),_JnxSoamLmCfgEnabled_Type())
jnxSoamLmCfgEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgEnabled.setStatus(_A)
class _JnxSoamLmCfgMeasurementEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('bForwardTransmitedFrames',0),('bForwardReceivedFrames',1),('bForwardMinFlr',2),('bForwardMaxFlr',3),('bForwardAvgFlr',4),('bBackwardTransmitedFrames',5),('bBackwardReceivedFrames',6),('bBackwardMinFlr',7),('bBackwardMaxFlr',8),('bBackwardAvgFlr',9),(_i,10),(_j,11),('bAvailForwardHighLoss',12),('bAvailForwardConsecutiveHighLoss',13),('bAvailForwardAvailable',14),('bAvailForwardUnavailable',15),('bAvailForwardMinFlr',16),('bAvailForwardMaxFlr',17),('bAvailForwardAvgFlr',18),('bAvailBackwardHighLoss',19),('bAvailBackwardConsecutiveHighLoss',20),('bAvailBackwardAvailable',21),('bAvailBackwardUnavailable',22),('bAvailBackwardMinFlr',23),('bAvailBackwardMaxFlr',24),('bAvailBackwardAvgFlr',25),('bMeasuredStatsForwardMeasuredFlr',26),('bMeasuredStatsBackwardMeasuredFlr',27),('bMeasuredStatsAvailForwardStatus',28),('bMeasuredStatsAvailBackwardStatus',29)))
_JnxSoamLmCfgMeasurementEnable_Type.__name__=_R
_JnxSoamLmCfgMeasurementEnable_Object=MibTableColumn
jnxSoamLmCfgMeasurementEnable=_JnxSoamLmCfgMeasurementEnable_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,5),_JnxSoamLmCfgMeasurementEnable_Type())
jnxSoamLmCfgMeasurementEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgMeasurementEnable.setStatus(_A)
class _JnxSoamLmCfgMessagePeriod_Type(Integer32):defaultValue=1000
_JnxSoamLmCfgMessagePeriod_Type.__name__=_P
_JnxSoamLmCfgMessagePeriod_Object=MibTableColumn
jnxSoamLmCfgMessagePeriod=_JnxSoamLmCfgMessagePeriod_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,6),_JnxSoamLmCfgMessagePeriod_Type())
jnxSoamLmCfgMessagePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgMessagePeriod.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCfgMessagePeriod.setUnits('ms')
_JnxSoamLmCfgPriority_Type=IEEE8021PriorityValue
_JnxSoamLmCfgPriority_Object=MibTableColumn
jnxSoamLmCfgPriority=_JnxSoamLmCfgPriority_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,7),_JnxSoamLmCfgPriority_Type())
jnxSoamLmCfgPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgPriority.setStatus(_A)
class _JnxSoamLmCfgFrameSize_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9600))
_JnxSoamLmCfgFrameSize_Type.__name__=_C
_JnxSoamLmCfgFrameSize_Object=MibTableColumn
jnxSoamLmCfgFrameSize=_JnxSoamLmCfgFrameSize_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,8),_JnxSoamLmCfgFrameSize_Type())
jnxSoamLmCfgFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgFrameSize.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCfgFrameSize.setUnits('bytes')
class _JnxSoamLmCfgDataPattern_Type(JnxSoamTcDataPatternType):defaultValue=1
_JnxSoamLmCfgDataPattern_Type.__name__=_c
_JnxSoamLmCfgDataPattern_Object=MibTableColumn
jnxSoamLmCfgDataPattern=_JnxSoamLmCfgDataPattern_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,9),_JnxSoamLmCfgDataPattern_Type())
jnxSoamLmCfgDataPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgDataPattern.setStatus(_A)
class _JnxSoamLmCfgTestTlvIncluded_Type(TruthValue):defaultValue=2
_JnxSoamLmCfgTestTlvIncluded_Type.__name__=_L
_JnxSoamLmCfgTestTlvIncluded_Object=MibTableColumn
jnxSoamLmCfgTestTlvIncluded=_JnxSoamLmCfgTestTlvIncluded_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,10),_JnxSoamLmCfgTestTlvIncluded_Type())
jnxSoamLmCfgTestTlvIncluded.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgTestTlvIncluded.setStatus(_A)
class _JnxSoamLmCfgTestTlvPattern_Type(JnxSoamTcTestPatternType):defaultValue=1
_JnxSoamLmCfgTestTlvPattern_Type.__name__=_d
_JnxSoamLmCfgTestTlvPattern_Object=MibTableColumn
jnxSoamLmCfgTestTlvPattern=_JnxSoamLmCfgTestTlvPattern_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,11),_JnxSoamLmCfgTestTlvPattern_Type())
jnxSoamLmCfgTestTlvPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgTestTlvPattern.setStatus(_A)
class _JnxSoamLmCfgNumIntervalsStored_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_JnxSoamLmCfgNumIntervalsStored_Type.__name__=_C
_JnxSoamLmCfgNumIntervalsStored_Object=MibTableColumn
jnxSoamLmCfgNumIntervalsStored=_JnxSoamLmCfgNumIntervalsStored_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,12),_JnxSoamLmCfgNumIntervalsStored_Type())
jnxSoamLmCfgNumIntervalsStored.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgNumIntervalsStored.setStatus(_A)
class _JnxSoamLmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):defaultValue=0
_JnxSoamLmCfgDestMepId_Type.__name__=_b
_JnxSoamLmCfgDestMepId_Object=MibTableColumn
jnxSoamLmCfgDestMepId=_JnxSoamLmCfgDestMepId_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,13),_JnxSoamLmCfgDestMepId_Type())
jnxSoamLmCfgDestMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgDestMepId.setStatus(_A)
class _JnxSoamLmCfgDestIsMepId_Type(TruthValue):defaultValue=1
_JnxSoamLmCfgDestIsMepId_Type.__name__=_L
_JnxSoamLmCfgDestIsMepId_Object=MibTableColumn
jnxSoamLmCfgDestIsMepId=_JnxSoamLmCfgDestIsMepId_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,14),_JnxSoamLmCfgDestIsMepId_Type())
jnxSoamLmCfgDestIsMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgDestIsMepId.setStatus(_A)
class _JnxSoamLmCfgStartTimeType_Type(JnxSoamTcOperationTimeType):defaultValue=2
_JnxSoamLmCfgStartTimeType_Type.__name__=_U
_JnxSoamLmCfgStartTimeType_Object=MibTableColumn
jnxSoamLmCfgStartTimeType=_JnxSoamLmCfgStartTimeType_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,15),_JnxSoamLmCfgStartTimeType_Type())
jnxSoamLmCfgStartTimeType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgStartTimeType.setStatus(_A)
class _JnxSoamLmCfgFixedStartDateAndTime_Type(DateAndTime):defaultHexValue=_X
_JnxSoamLmCfgFixedStartDateAndTime_Type.__name__=_S
_JnxSoamLmCfgFixedStartDateAndTime_Object=MibTableColumn
jnxSoamLmCfgFixedStartDateAndTime=_JnxSoamLmCfgFixedStartDateAndTime_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,16),_JnxSoamLmCfgFixedStartDateAndTime_Type())
jnxSoamLmCfgFixedStartDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgFixedStartDateAndTime.setStatus(_A)
class _JnxSoamLmCfgRelativeStartTime_Type(TimeInterval):defaultValue=0
_JnxSoamLmCfgRelativeStartTime_Type.__name__=_T
_JnxSoamLmCfgRelativeStartTime_Object=MibTableColumn
jnxSoamLmCfgRelativeStartTime=_JnxSoamLmCfgRelativeStartTime_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,17),_JnxSoamLmCfgRelativeStartTime_Type())
jnxSoamLmCfgRelativeStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgRelativeStartTime.setStatus(_A)
class _JnxSoamLmCfgRepetitionTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31536000))
_JnxSoamLmCfgRepetitionTime_Type.__name__=_C
_JnxSoamLmCfgRepetitionTime_Object=MibTableColumn
jnxSoamLmCfgRepetitionTime=_JnxSoamLmCfgRepetitionTime_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,18),_JnxSoamLmCfgRepetitionTime_Type())
jnxSoamLmCfgRepetitionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgRepetitionTime.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCfgRepetitionTime.setUnits(_k)
class _JnxSoamLmCfgAlignMeasurementIntervals_Type(TruthValue):defaultValue=1
_JnxSoamLmCfgAlignMeasurementIntervals_Type.__name__=_L
_JnxSoamLmCfgAlignMeasurementIntervals_Object=MibTableColumn
jnxSoamLmCfgAlignMeasurementIntervals=_JnxSoamLmCfgAlignMeasurementIntervals_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,19),_JnxSoamLmCfgAlignMeasurementIntervals_Type())
jnxSoamLmCfgAlignMeasurementIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgAlignMeasurementIntervals.setStatus(_A)
class _JnxSoamLmCfgAlignMeasurementOffset_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,525600))
_JnxSoamLmCfgAlignMeasurementOffset_Type.__name__=_C
_JnxSoamLmCfgAlignMeasurementOffset_Object=MibTableColumn
jnxSoamLmCfgAlignMeasurementOffset=_JnxSoamLmCfgAlignMeasurementOffset_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,20),_JnxSoamLmCfgAlignMeasurementOffset_Type())
jnxSoamLmCfgAlignMeasurementOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgAlignMeasurementOffset.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCfgAlignMeasurementOffset.setUnits(_V)
class _JnxSoamLmCfgSessionType_Type(OctetString):defaultValue=OctetString(_l);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,42))
_JnxSoamLmCfgSessionType_Type.__name__=_Q
_JnxSoamLmCfgSessionType_Object=MibTableColumn
jnxSoamLmCfgSessionType=_JnxSoamLmCfgSessionType_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,21),_JnxSoamLmCfgSessionType_Type())
jnxSoamLmCfgSessionType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgSessionType.setStatus(_A)
class _JnxSoamLmCfgSessionStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,44))
_JnxSoamLmCfgSessionStatus_Type.__name__=_Q
_JnxSoamLmCfgSessionStatus_Object=MibTableColumn
jnxSoamLmCfgSessionStatus=_JnxSoamLmCfgSessionStatus_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,22),_JnxSoamLmCfgSessionStatus_Type())
jnxSoamLmCfgSessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgSessionStatus.setStatus(_A)
class _JnxSoamLmCfgHistoryClear_Type(TruthValue):defaultValue=2
_JnxSoamLmCfgHistoryClear_Type.__name__=_L
_JnxSoamLmCfgHistoryClear_Object=MibTableColumn
jnxSoamLmCfgHistoryClear=_JnxSoamLmCfgHistoryClear_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,23),_JnxSoamLmCfgHistoryClear_Type())
jnxSoamLmCfgHistoryClear.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgHistoryClear.setStatus(_A)
_JnxSoamLmCfgRowStatus_Type=RowStatus
_JnxSoamLmCfgRowStatus_Object=MibTableColumn
jnxSoamLmCfgRowStatus=_JnxSoamLmCfgRowStatus_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,24),_JnxSoamLmCfgRowStatus_Type())
jnxSoamLmCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgRowStatus.setStatus(_A)
class _JnxSoamLmCfgMeasurementInterval_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,525600))
_JnxSoamLmCfgMeasurementInterval_Type.__name__=_C
_JnxSoamLmCfgMeasurementInterval_Object=MibTableColumn
jnxSoamLmCfgMeasurementInterval=_JnxSoamLmCfgMeasurementInterval_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,25),_JnxSoamLmCfgMeasurementInterval_Type())
jnxSoamLmCfgMeasurementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgMeasurementInterval.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCfgMeasurementInterval.setUnits(_V)
_JnxSoamLmCfgDestMacAddress_Type=MacAddress
_JnxSoamLmCfgDestMacAddress_Object=MibTableColumn
jnxSoamLmCfgDestMacAddress=_JnxSoamLmCfgDestMacAddress_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,26),_JnxSoamLmCfgDestMacAddress_Type())
jnxSoamLmCfgDestMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamLmCfgDestMacAddress.setStatus(_A)
class _JnxSoamLmCfgStopTimeType_Type(JnxSoamTcOperationTimeType):defaultValue=1
_JnxSoamLmCfgStopTimeType_Type.__name__=_U
_JnxSoamLmCfgStopTimeType_Object=MibTableColumn
jnxSoamLmCfgStopTimeType=_JnxSoamLmCfgStopTimeType_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,27),_JnxSoamLmCfgStopTimeType_Type())
jnxSoamLmCfgStopTimeType.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamLmCfgStopTimeType.setStatus(_A)
class _JnxSoamLmCfgFixedStopDateAndTime_Type(DateAndTime):defaultHexValue=_X
_JnxSoamLmCfgFixedStopDateAndTime_Type.__name__=_S
_JnxSoamLmCfgFixedStopDateAndTime_Object=MibTableColumn
jnxSoamLmCfgFixedStopDateAndTime=_JnxSoamLmCfgFixedStopDateAndTime_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,28),_JnxSoamLmCfgFixedStopDateAndTime_Type())
jnxSoamLmCfgFixedStopDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCfgFixedStopDateAndTime.setStatus(_A)
class _JnxSoamLmCfgRelativeStopTime_Type(TimeInterval):defaultValue=0
_JnxSoamLmCfgRelativeStopTime_Type.__name__=_T
_JnxSoamLmCfgRelativeStopTime_Object=MibTableColumn
jnxSoamLmCfgRelativeStopTime=_JnxSoamLmCfgRelativeStopTime_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,29),_JnxSoamLmCfgRelativeStopTime_Type())
jnxSoamLmCfgRelativeStopTime.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamLmCfgRelativeStopTime.setStatus(_A)
class _JnxSoamLmCfgAvailabilityMeasurementInterval_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,525600))
_JnxSoamLmCfgAvailabilityMeasurementInterval_Type.__name__=_C
_JnxSoamLmCfgAvailabilityMeasurementInterval_Object=MibTableColumn
jnxSoamLmCfgAvailabilityMeasurementInterval=_JnxSoamLmCfgAvailabilityMeasurementInterval_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,30),_JnxSoamLmCfgAvailabilityMeasurementInterval_Type())
jnxSoamLmCfgAvailabilityMeasurementInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamLmCfgAvailabilityMeasurementInterval.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCfgAvailabilityMeasurementInterval.setUnits(_V)
class _JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type.__name__=_C
_JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Object=MibTableColumn
jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus=_JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,31),_JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type())
jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus.setStatus(_A)
class _JnxSoamLmCfgAvailabilityFlrThreshold_Type(Unsigned32):defaultValue=50000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCfgAvailabilityFlrThreshold_Type.__name__=_C
_JnxSoamLmCfgAvailabilityFlrThreshold_Object=MibTableColumn
jnxSoamLmCfgAvailabilityFlrThreshold=_JnxSoamLmCfgAvailabilityFlrThreshold_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,32),_JnxSoamLmCfgAvailabilityFlrThreshold_Type())
jnxSoamLmCfgAvailabilityFlrThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamLmCfgAvailabilityFlrThreshold.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCfgAvailabilityFlrThreshold.setUnits(_G)
class _JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Type.__name__=_C
_JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Object=MibTableColumn
jnxSoamLmCfgAvailabilityNumConsecutiveIntervals=_JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,33),_JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Type())
jnxSoamLmCfgAvailabilityNumConsecutiveIntervals.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamLmCfgAvailabilityNumConsecutiveIntervals.setStatus(_A)
class _JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type.__name__=_C
_JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Object=MibTableColumn
jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr=_JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,1,1,34),_JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type())
jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr.setStatus(_A)
_JnxSoamLmMeasuredStatsTable_Object=MibTable
jnxSoamLmMeasuredStatsTable=_JnxSoamLmMeasuredStatsTable_Object((1,3,6,1,4,1,2636,3,78,1,2,2))
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsTable.setStatus(_A)
_JnxSoamLmMeasuredStatsEntry_Object=MibTableRow
jnxSoamLmMeasuredStatsEntry=_JnxSoamLmMeasuredStatsEntry_Object((1,3,6,1,4,1,2636,3,78,1,2,2,1))
jnxSoamLmMeasuredStatsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_O))
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsEntry.setStatus(_A)
class _JnxSoamLmMeasuredStatsForwardFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmMeasuredStatsForwardFlr_Type.__name__=_C
_JnxSoamLmMeasuredStatsForwardFlr_Object=MibTableColumn
jnxSoamLmMeasuredStatsForwardFlr=_JnxSoamLmMeasuredStatsForwardFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,2,1,1),_JnxSoamLmMeasuredStatsForwardFlr_Type())
jnxSoamLmMeasuredStatsForwardFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsForwardFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsForwardFlr.setUnits(_G)
class _JnxSoamLmMeasuredStatsBackwardFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmMeasuredStatsBackwardFlr_Type.__name__=_C
_JnxSoamLmMeasuredStatsBackwardFlr_Object=MibTableColumn
jnxSoamLmMeasuredStatsBackwardFlr=_JnxSoamLmMeasuredStatsBackwardFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,2,1,2),_JnxSoamLmMeasuredStatsBackwardFlr_Type())
jnxSoamLmMeasuredStatsBackwardFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsBackwardFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsBackwardFlr.setUnits(_G)
_JnxSoamLmMeasuredStatsAvailForwardStatus_Type=JnxSoamTcAvailabilityType
_JnxSoamLmMeasuredStatsAvailForwardStatus_Object=MibTableColumn
jnxSoamLmMeasuredStatsAvailForwardStatus=_JnxSoamLmMeasuredStatsAvailForwardStatus_Object((1,3,6,1,4,1,2636,3,78,1,2,2,1,3),_JnxSoamLmMeasuredStatsAvailForwardStatus_Type())
jnxSoamLmMeasuredStatsAvailForwardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsAvailForwardStatus.setStatus(_A)
_JnxSoamLmMeasuredStatsAvailBackwardStatus_Type=JnxSoamTcAvailabilityType
_JnxSoamLmMeasuredStatsAvailBackwardStatus_Object=MibTableColumn
jnxSoamLmMeasuredStatsAvailBackwardStatus=_JnxSoamLmMeasuredStatsAvailBackwardStatus_Object((1,3,6,1,4,1,2636,3,78,1,2,2,1,4),_JnxSoamLmMeasuredStatsAvailBackwardStatus_Type())
jnxSoamLmMeasuredStatsAvailBackwardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsAvailBackwardStatus.setStatus(_A)
_JnxSoamLmMeasuredStatsAvailForwardLastTransitionTime_Type=DateAndTime
_JnxSoamLmMeasuredStatsAvailForwardLastTransitionTime_Object=MibTableColumn
jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime=_JnxSoamLmMeasuredStatsAvailForwardLastTransitionTime_Object((1,3,6,1,4,1,2636,3,78,1,2,2,1,5),_JnxSoamLmMeasuredStatsAvailForwardLastTransitionTime_Type())
jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime.setStatus(_A)
_JnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Type=DateAndTime
_JnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Object=MibTableColumn
jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime=_JnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Object((1,3,6,1,4,1,2636,3,78,1,2,2,1,6),_JnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Type())
jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime.setStatus(_A)
_JnxSoamLmCurrentStatsTable_Object=MibTable
jnxSoamLmCurrentStatsTable=_JnxSoamLmCurrentStatsTable_Object((1,3,6,1,4,1,2636,3,78,1,2,3))
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsTable.setStatus(_A)
_JnxSoamLmCurrentStatsEntry_Object=MibTableRow
jnxSoamLmCurrentStatsEntry=_JnxSoamLmCurrentStatsEntry_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1))
jnxSoamLmCurrentStatsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_O))
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsEntry.setStatus(_A)
_JnxSoamLmCurrentStatsIndex_Type=Unsigned32
_JnxSoamLmCurrentStatsIndex_Object=MibTableColumn
jnxSoamLmCurrentStatsIndex=_JnxSoamLmCurrentStatsIndex_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,1),_JnxSoamLmCurrentStatsIndex_Type())
jnxSoamLmCurrentStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsIndex.setStatus(_A)
_JnxSoamLmCurrentStatsStartTime_Type=DateAndTime
_JnxSoamLmCurrentStatsStartTime_Object=MibTableColumn
jnxSoamLmCurrentStatsStartTime=_JnxSoamLmCurrentStatsStartTime_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,2),_JnxSoamLmCurrentStatsStartTime_Type())
jnxSoamLmCurrentStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsStartTime.setStatus(_A)
_JnxSoamLmCurrentStatsElapsedTime_Type=TimeInterval
_JnxSoamLmCurrentStatsElapsedTime_Object=MibTableColumn
jnxSoamLmCurrentStatsElapsedTime=_JnxSoamLmCurrentStatsElapsedTime_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,3),_JnxSoamLmCurrentStatsElapsedTime_Type())
jnxSoamLmCurrentStatsElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsElapsedTime.setStatus(_A)
_JnxSoamLmCurrentStatsSuspect_Type=TruthValue
_JnxSoamLmCurrentStatsSuspect_Object=MibTableColumn
jnxSoamLmCurrentStatsSuspect=_JnxSoamLmCurrentStatsSuspect_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,4),_JnxSoamLmCurrentStatsSuspect_Type())
jnxSoamLmCurrentStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsSuspect.setStatus(_A)
_JnxSoamLmCurrentStatsForwardTransmittedFrames_Type=Gauge32
_JnxSoamLmCurrentStatsForwardTransmittedFrames_Object=MibTableColumn
jnxSoamLmCurrentStatsForwardTransmittedFrames=_JnxSoamLmCurrentStatsForwardTransmittedFrames_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,5),_JnxSoamLmCurrentStatsForwardTransmittedFrames_Type())
jnxSoamLmCurrentStatsForwardTransmittedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsForwardTransmittedFrames.setStatus(_A)
_JnxSoamLmCurrentStatsForwardReceivedFrames_Type=Gauge32
_JnxSoamLmCurrentStatsForwardReceivedFrames_Object=MibTableColumn
jnxSoamLmCurrentStatsForwardReceivedFrames=_JnxSoamLmCurrentStatsForwardReceivedFrames_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,6),_JnxSoamLmCurrentStatsForwardReceivedFrames_Type())
jnxSoamLmCurrentStatsForwardReceivedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsForwardReceivedFrames.setStatus(_A)
class _JnxSoamLmCurrentStatsForwardMinFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentStatsForwardMinFlr_Type.__name__=_C
_JnxSoamLmCurrentStatsForwardMinFlr_Object=MibTableColumn
jnxSoamLmCurrentStatsForwardMinFlr=_JnxSoamLmCurrentStatsForwardMinFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,7),_JnxSoamLmCurrentStatsForwardMinFlr_Type())
jnxSoamLmCurrentStatsForwardMinFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsForwardMinFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsForwardMinFlr.setUnits(_G)
class _JnxSoamLmCurrentStatsForwardMaxFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentStatsForwardMaxFlr_Type.__name__=_C
_JnxSoamLmCurrentStatsForwardMaxFlr_Object=MibTableColumn
jnxSoamLmCurrentStatsForwardMaxFlr=_JnxSoamLmCurrentStatsForwardMaxFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,8),_JnxSoamLmCurrentStatsForwardMaxFlr_Type())
jnxSoamLmCurrentStatsForwardMaxFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsForwardMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsForwardMaxFlr.setUnits(_G)
class _JnxSoamLmCurrentStatsForwardAvgFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentStatsForwardAvgFlr_Type.__name__=_C
_JnxSoamLmCurrentStatsForwardAvgFlr_Object=MibTableColumn
jnxSoamLmCurrentStatsForwardAvgFlr=_JnxSoamLmCurrentStatsForwardAvgFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,9),_JnxSoamLmCurrentStatsForwardAvgFlr_Type())
jnxSoamLmCurrentStatsForwardAvgFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsForwardAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsForwardAvgFlr.setUnits(_G)
_JnxSoamLmCurrentStatsBackwardTransmittedFrames_Type=Gauge32
_JnxSoamLmCurrentStatsBackwardTransmittedFrames_Object=MibTableColumn
jnxSoamLmCurrentStatsBackwardTransmittedFrames=_JnxSoamLmCurrentStatsBackwardTransmittedFrames_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,10),_JnxSoamLmCurrentStatsBackwardTransmittedFrames_Type())
jnxSoamLmCurrentStatsBackwardTransmittedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsBackwardTransmittedFrames.setStatus(_A)
_JnxSoamLmCurrentStatsBackwardReceivedFrames_Type=Gauge32
_JnxSoamLmCurrentStatsBackwardReceivedFrames_Object=MibTableColumn
jnxSoamLmCurrentStatsBackwardReceivedFrames=_JnxSoamLmCurrentStatsBackwardReceivedFrames_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,11),_JnxSoamLmCurrentStatsBackwardReceivedFrames_Type())
jnxSoamLmCurrentStatsBackwardReceivedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsBackwardReceivedFrames.setStatus(_A)
class _JnxSoamLmCurrentStatsBackwardMinFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentStatsBackwardMinFlr_Type.__name__=_C
_JnxSoamLmCurrentStatsBackwardMinFlr_Object=MibTableColumn
jnxSoamLmCurrentStatsBackwardMinFlr=_JnxSoamLmCurrentStatsBackwardMinFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,12),_JnxSoamLmCurrentStatsBackwardMinFlr_Type())
jnxSoamLmCurrentStatsBackwardMinFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsBackwardMinFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsBackwardMinFlr.setUnits(_G)
class _JnxSoamLmCurrentStatsBackwardMaxFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentStatsBackwardMaxFlr_Type.__name__=_C
_JnxSoamLmCurrentStatsBackwardMaxFlr_Object=MibTableColumn
jnxSoamLmCurrentStatsBackwardMaxFlr=_JnxSoamLmCurrentStatsBackwardMaxFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,13),_JnxSoamLmCurrentStatsBackwardMaxFlr_Type())
jnxSoamLmCurrentStatsBackwardMaxFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsBackwardMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsBackwardMaxFlr.setUnits(_G)
class _JnxSoamLmCurrentStatsBackwardAvgFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentStatsBackwardAvgFlr_Type.__name__=_C
_JnxSoamLmCurrentStatsBackwardAvgFlr_Object=MibTableColumn
jnxSoamLmCurrentStatsBackwardAvgFlr=_JnxSoamLmCurrentStatsBackwardAvgFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,14),_JnxSoamLmCurrentStatsBackwardAvgFlr_Type())
jnxSoamLmCurrentStatsBackwardAvgFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsBackwardAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsBackwardAvgFlr.setUnits(_G)
_JnxSoamLmCurrentStatsSoamPdusSent_Type=Gauge32
_JnxSoamLmCurrentStatsSoamPdusSent_Object=MibTableColumn
jnxSoamLmCurrentStatsSoamPdusSent=_JnxSoamLmCurrentStatsSoamPdusSent_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,15),_JnxSoamLmCurrentStatsSoamPdusSent_Type())
jnxSoamLmCurrentStatsSoamPdusSent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsSoamPdusSent.setStatus(_A)
_JnxSoamLmCurrentStatsSoamPdusReceived_Type=Gauge32
_JnxSoamLmCurrentStatsSoamPdusReceived_Object=MibTableColumn
jnxSoamLmCurrentStatsSoamPdusReceived=_JnxSoamLmCurrentStatsSoamPdusReceived_Object((1,3,6,1,4,1,2636,3,78,1,2,3,1,16),_JnxSoamLmCurrentStatsSoamPdusReceived_Type())
jnxSoamLmCurrentStatsSoamPdusReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentStatsSoamPdusReceived.setStatus(_A)
_JnxSoamLmHistoryStatsTable_Object=MibTable
jnxSoamLmHistoryStatsTable=_JnxSoamLmHistoryStatsTable_Object((1,3,6,1,4,1,2636,3,78,1,2,4))
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsTable.setStatus(_A)
_JnxSoamLmHistoryStatsEntry_Object=MibTableRow
jnxSoamLmHistoryStatsEntry=_JnxSoamLmHistoryStatsEntry_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1))
jnxSoamLmHistoryStatsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_O),(0,_E,_m))
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsEntry.setStatus(_A)
_JnxSoamLmHistoryStatsIndex_Type=Unsigned32
_JnxSoamLmHistoryStatsIndex_Object=MibTableColumn
jnxSoamLmHistoryStatsIndex=_JnxSoamLmHistoryStatsIndex_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,1),_JnxSoamLmHistoryStatsIndex_Type())
jnxSoamLmHistoryStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsIndex.setStatus(_A)
_JnxSoamLmHistoryStatsEndTime_Type=DateAndTime
_JnxSoamLmHistoryStatsEndTime_Object=MibTableColumn
jnxSoamLmHistoryStatsEndTime=_JnxSoamLmHistoryStatsEndTime_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,2),_JnxSoamLmHistoryStatsEndTime_Type())
jnxSoamLmHistoryStatsEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsEndTime.setStatus(_A)
_JnxSoamLmHistoryStatsElapsedTime_Type=TimeInterval
_JnxSoamLmHistoryStatsElapsedTime_Object=MibTableColumn
jnxSoamLmHistoryStatsElapsedTime=_JnxSoamLmHistoryStatsElapsedTime_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,3),_JnxSoamLmHistoryStatsElapsedTime_Type())
jnxSoamLmHistoryStatsElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsElapsedTime.setStatus(_A)
_JnxSoamLmHistoryStatsSuspect_Type=TruthValue
_JnxSoamLmHistoryStatsSuspect_Object=MibTableColumn
jnxSoamLmHistoryStatsSuspect=_JnxSoamLmHistoryStatsSuspect_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,4),_JnxSoamLmHistoryStatsSuspect_Type())
jnxSoamLmHistoryStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsSuspect.setStatus(_A)
_JnxSoamLmHistoryStatsForwardTransmittedFrames_Type=Gauge32
_JnxSoamLmHistoryStatsForwardTransmittedFrames_Object=MibTableColumn
jnxSoamLmHistoryStatsForwardTransmittedFrames=_JnxSoamLmHistoryStatsForwardTransmittedFrames_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,5),_JnxSoamLmHistoryStatsForwardTransmittedFrames_Type())
jnxSoamLmHistoryStatsForwardTransmittedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsForwardTransmittedFrames.setStatus(_A)
_JnxSoamLmHistoryStatsForwardReceivedFrames_Type=Gauge32
_JnxSoamLmHistoryStatsForwardReceivedFrames_Object=MibTableColumn
jnxSoamLmHistoryStatsForwardReceivedFrames=_JnxSoamLmHistoryStatsForwardReceivedFrames_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,6),_JnxSoamLmHistoryStatsForwardReceivedFrames_Type())
jnxSoamLmHistoryStatsForwardReceivedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsForwardReceivedFrames.setStatus(_A)
class _JnxSoamLmHistoryStatsForwardMinFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryStatsForwardMinFlr_Type.__name__=_C
_JnxSoamLmHistoryStatsForwardMinFlr_Object=MibTableColumn
jnxSoamLmHistoryStatsForwardMinFlr=_JnxSoamLmHistoryStatsForwardMinFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,7),_JnxSoamLmHistoryStatsForwardMinFlr_Type())
jnxSoamLmHistoryStatsForwardMinFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsForwardMinFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsForwardMinFlr.setUnits(_G)
class _JnxSoamLmHistoryStatsForwardMaxFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryStatsForwardMaxFlr_Type.__name__=_C
_JnxSoamLmHistoryStatsForwardMaxFlr_Object=MibTableColumn
jnxSoamLmHistoryStatsForwardMaxFlr=_JnxSoamLmHistoryStatsForwardMaxFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,8),_JnxSoamLmHistoryStatsForwardMaxFlr_Type())
jnxSoamLmHistoryStatsForwardMaxFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsForwardMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsForwardMaxFlr.setUnits(_G)
class _JnxSoamLmHistoryStatsForwardAvgFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryStatsForwardAvgFlr_Type.__name__=_C
_JnxSoamLmHistoryStatsForwardAvgFlr_Object=MibTableColumn
jnxSoamLmHistoryStatsForwardAvgFlr=_JnxSoamLmHistoryStatsForwardAvgFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,9),_JnxSoamLmHistoryStatsForwardAvgFlr_Type())
jnxSoamLmHistoryStatsForwardAvgFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsForwardAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsForwardAvgFlr.setUnits(_G)
_JnxSoamLmHistoryStatsBackwardTransmittedFrames_Type=Gauge32
_JnxSoamLmHistoryStatsBackwardTransmittedFrames_Object=MibTableColumn
jnxSoamLmHistoryStatsBackwardTransmittedFrames=_JnxSoamLmHistoryStatsBackwardTransmittedFrames_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,10),_JnxSoamLmHistoryStatsBackwardTransmittedFrames_Type())
jnxSoamLmHistoryStatsBackwardTransmittedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsBackwardTransmittedFrames.setStatus(_A)
_JnxSoamLmHistoryStatsBackwardReceivedFrames_Type=Gauge32
_JnxSoamLmHistoryStatsBackwardReceivedFrames_Object=MibTableColumn
jnxSoamLmHistoryStatsBackwardReceivedFrames=_JnxSoamLmHistoryStatsBackwardReceivedFrames_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,11),_JnxSoamLmHistoryStatsBackwardReceivedFrames_Type())
jnxSoamLmHistoryStatsBackwardReceivedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsBackwardReceivedFrames.setStatus(_A)
class _JnxSoamLmHistoryStatsBackwardMinFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryStatsBackwardMinFlr_Type.__name__=_C
_JnxSoamLmHistoryStatsBackwardMinFlr_Object=MibTableColumn
jnxSoamLmHistoryStatsBackwardMinFlr=_JnxSoamLmHistoryStatsBackwardMinFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,12),_JnxSoamLmHistoryStatsBackwardMinFlr_Type())
jnxSoamLmHistoryStatsBackwardMinFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsBackwardMinFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsBackwardMinFlr.setUnits(_G)
class _JnxSoamLmHistoryStatsBackwardMaxFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryStatsBackwardMaxFlr_Type.__name__=_C
_JnxSoamLmHistoryStatsBackwardMaxFlr_Object=MibTableColumn
jnxSoamLmHistoryStatsBackwardMaxFlr=_JnxSoamLmHistoryStatsBackwardMaxFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,13),_JnxSoamLmHistoryStatsBackwardMaxFlr_Type())
jnxSoamLmHistoryStatsBackwardMaxFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsBackwardMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsBackwardMaxFlr.setUnits(_G)
class _JnxSoamLmHistoryStatsBackwardAvgFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryStatsBackwardAvgFlr_Type.__name__=_C
_JnxSoamLmHistoryStatsBackwardAvgFlr_Object=MibTableColumn
jnxSoamLmHistoryStatsBackwardAvgFlr=_JnxSoamLmHistoryStatsBackwardAvgFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,14),_JnxSoamLmHistoryStatsBackwardAvgFlr_Type())
jnxSoamLmHistoryStatsBackwardAvgFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsBackwardAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsBackwardAvgFlr.setUnits(_G)
_JnxSoamLmHistoryStatsSoamPdusSent_Type=Gauge32
_JnxSoamLmHistoryStatsSoamPdusSent_Object=MibTableColumn
jnxSoamLmHistoryStatsSoamPdusSent=_JnxSoamLmHistoryStatsSoamPdusSent_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,15),_JnxSoamLmHistoryStatsSoamPdusSent_Type())
jnxSoamLmHistoryStatsSoamPdusSent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsSoamPdusSent.setStatus(_A)
_JnxSoamLmHistoryStatsSoamPdusReceived_Type=Gauge32
_JnxSoamLmHistoryStatsSoamPdusReceived_Object=MibTableColumn
jnxSoamLmHistoryStatsSoamPdusReceived=_JnxSoamLmHistoryStatsSoamPdusReceived_Object((1,3,6,1,4,1,2636,3,78,1,2,4,1,16),_JnxSoamLmHistoryStatsSoamPdusReceived_Type())
jnxSoamLmHistoryStatsSoamPdusReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryStatsSoamPdusReceived.setStatus(_A)
_JnxSoamLmThresholdCfgTable_Object=MibTable
jnxSoamLmThresholdCfgTable=_JnxSoamLmThresholdCfgTable_Object((1,3,6,1,4,1,2636,3,78,1,2,5))
if mibBuilder.loadTexts:jnxSoamLmThresholdCfgTable.setStatus(_A)
_JnxSoamLmThresholdCfgEntry_Object=MibTableRow
jnxSoamLmThresholdCfgEntry=_JnxSoamLmThresholdCfgEntry_Object((1,3,6,1,4,1,2636,3,78,1,2,5,1))
jnxSoamLmThresholdCfgEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_O),(0,_E,_n))
if mibBuilder.loadTexts:jnxSoamLmThresholdCfgEntry.setStatus(_A)
class _JnxSoamLmThresholdCfgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_JnxSoamLmThresholdCfgIndex_Type.__name__=_C
_JnxSoamLmThresholdCfgIndex_Object=MibTableColumn
jnxSoamLmThresholdCfgIndex=_JnxSoamLmThresholdCfgIndex_Object((1,3,6,1,4,1,2636,3,78,1,2,5,1,1),_JnxSoamLmThresholdCfgIndex_Type())
jnxSoamLmThresholdCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmThresholdCfgIndex.setStatus(_A)
class _JnxSoamLmThresholdCfgEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('bJnxSoamLmMeasuredFlrForwardThreshold',0),('bJnxSoamLmMaxFlrForwardThreshold',1),('bJnxSoamLmAvgFlrForwardThreshold',2),('bJnxSoamLmMeasuredFlrBackwardThreshold',3),('bJnxSoamLmMaxFlrBackwardThreshold',4),('bJnxSoamLmAvgFlrBackwardThreshold',5)))
_JnxSoamLmThresholdCfgEnable_Type.__name__=_R
_JnxSoamLmThresholdCfgEnable_Object=MibTableColumn
jnxSoamLmThresholdCfgEnable=_JnxSoamLmThresholdCfgEnable_Object((1,3,6,1,4,1,2636,3,78,1,2,5,1,2),_JnxSoamLmThresholdCfgEnable_Type())
jnxSoamLmThresholdCfgEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmThresholdCfgEnable.setStatus(_A)
class _JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Type(Unsigned32):defaultValue=100000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Type.__name__=_C
_JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Object=MibTableColumn
jnxSoamLmThresholdCfgAvgFlrForwardThreshold=_JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Object((1,3,6,1,4,1,2636,3,78,1,2,5,1,3),_JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Type())
jnxSoamLmThresholdCfgAvgFlrForwardThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmThresholdCfgAvgFlrForwardThreshold.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmThresholdCfgAvgFlrForwardThreshold.setUnits(_G)
class _JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Type(Unsigned32):defaultValue=100000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Type.__name__=_C
_JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Object=MibTableColumn
jnxSoamLmThresholdCfgAvgFlrBackwardThreshold=_JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Object((1,3,6,1,4,1,2636,3,78,1,2,5,1,4),_JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Type())
jnxSoamLmThresholdCfgAvgFlrBackwardThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmThresholdCfgAvgFlrBackwardThreshold.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmThresholdCfgAvgFlrBackwardThreshold.setUnits(_G)
_JnxSoamLmThresholdCfgRowStatus_Type=RowStatus
_JnxSoamLmThresholdCfgRowStatus_Object=MibTableColumn
jnxSoamLmThresholdCfgRowStatus=_JnxSoamLmThresholdCfgRowStatus_Object((1,3,6,1,4,1,2636,3,78,1,2,5,1,5),_JnxSoamLmThresholdCfgRowStatus_Type())
jnxSoamLmThresholdCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmThresholdCfgRowStatus.setStatus(_A)
_JnxSoamLmCurrentAvailStatsTable_Object=MibTable
jnxSoamLmCurrentAvailStatsTable=_JnxSoamLmCurrentAvailStatsTable_Object((1,3,6,1,4,1,2636,3,78,1,2,6))
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsTable.setStatus(_A)
_JnxSoamLmCurrentAvailStatsEntry_Object=MibTableRow
jnxSoamLmCurrentAvailStatsEntry=_JnxSoamLmCurrentAvailStatsEntry_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1))
jnxSoamLmCurrentAvailStatsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_O))
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsEntry.setStatus(_A)
_JnxSoamLmCurrentAvailStatsIndex_Type=Unsigned32
_JnxSoamLmCurrentAvailStatsIndex_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsIndex=_JnxSoamLmCurrentAvailStatsIndex_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,1),_JnxSoamLmCurrentAvailStatsIndex_Type())
jnxSoamLmCurrentAvailStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsIndex.setStatus(_A)
_JnxSoamLmCurrentAvailStatsStartTime_Type=DateAndTime
_JnxSoamLmCurrentAvailStatsStartTime_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsStartTime=_JnxSoamLmCurrentAvailStatsStartTime_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,2),_JnxSoamLmCurrentAvailStatsStartTime_Type())
jnxSoamLmCurrentAvailStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsStartTime.setStatus(_A)
_JnxSoamLmCurrentAvailStatsElapsedTime_Type=TimeInterval
_JnxSoamLmCurrentAvailStatsElapsedTime_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsElapsedTime=_JnxSoamLmCurrentAvailStatsElapsedTime_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,3),_JnxSoamLmCurrentAvailStatsElapsedTime_Type())
jnxSoamLmCurrentAvailStatsElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsElapsedTime.setStatus(_A)
_JnxSoamLmCurrentAvailStatsSuspect_Type=TruthValue
_JnxSoamLmCurrentAvailStatsSuspect_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsSuspect=_JnxSoamLmCurrentAvailStatsSuspect_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,4),_JnxSoamLmCurrentAvailStatsSuspect_Type())
jnxSoamLmCurrentAvailStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsSuspect.setStatus(_A)
_JnxSoamLmCurrentAvailStatsForwardHighLoss_Type=Unsigned32
_JnxSoamLmCurrentAvailStatsForwardHighLoss_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsForwardHighLoss=_JnxSoamLmCurrentAvailStatsForwardHighLoss_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,5),_JnxSoamLmCurrentAvailStatsForwardHighLoss_Type())
jnxSoamLmCurrentAvailStatsForwardHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardHighLoss.setStatus(_A)
_JnxSoamLmCurrentAvailStatsBackwardHighLoss_Type=Unsigned32
_JnxSoamLmCurrentAvailStatsBackwardHighLoss_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardHighLoss=_JnxSoamLmCurrentAvailStatsBackwardHighLoss_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,6),_JnxSoamLmCurrentAvailStatsBackwardHighLoss_Type())
jnxSoamLmCurrentAvailStatsBackwardHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardHighLoss.setStatus(_A)
_JnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Type=Unsigned32
_JnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss=_JnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,7),_JnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Type())
jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss.setStatus(_A)
_JnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Type=Unsigned32
_JnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss=_JnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,8),_JnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Type())
jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss.setStatus(_A)
_JnxSoamLmCurrentAvailStatsForwardAvailable_Type=Gauge32
_JnxSoamLmCurrentAvailStatsForwardAvailable_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsForwardAvailable=_JnxSoamLmCurrentAvailStatsForwardAvailable_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,9),_JnxSoamLmCurrentAvailStatsForwardAvailable_Type())
jnxSoamLmCurrentAvailStatsForwardAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardAvailable.setStatus(_A)
_JnxSoamLmCurrentAvailStatsBackwardAvailable_Type=Gauge32
_JnxSoamLmCurrentAvailStatsBackwardAvailable_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardAvailable=_JnxSoamLmCurrentAvailStatsBackwardAvailable_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,10),_JnxSoamLmCurrentAvailStatsBackwardAvailable_Type())
jnxSoamLmCurrentAvailStatsBackwardAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardAvailable.setStatus(_A)
_JnxSoamLmCurrentAvailStatsForwardUnavailable_Type=Gauge32
_JnxSoamLmCurrentAvailStatsForwardUnavailable_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsForwardUnavailable=_JnxSoamLmCurrentAvailStatsForwardUnavailable_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,11),_JnxSoamLmCurrentAvailStatsForwardUnavailable_Type())
jnxSoamLmCurrentAvailStatsForwardUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardUnavailable.setStatus(_A)
_JnxSoamLmCurrentAvailStatsBackwardUnavailable_Type=Gauge32
_JnxSoamLmCurrentAvailStatsBackwardUnavailable_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardUnavailable=_JnxSoamLmCurrentAvailStatsBackwardUnavailable_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,12),_JnxSoamLmCurrentAvailStatsBackwardUnavailable_Type())
jnxSoamLmCurrentAvailStatsBackwardUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardUnavailable.setStatus(_A)
class _JnxSoamLmCurrentAvailStatsForwardMinFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentAvailStatsForwardMinFlr_Type.__name__=_C
_JnxSoamLmCurrentAvailStatsForwardMinFlr_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsForwardMinFlr=_JnxSoamLmCurrentAvailStatsForwardMinFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,13),_JnxSoamLmCurrentAvailStatsForwardMinFlr_Type())
jnxSoamLmCurrentAvailStatsForwardMinFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardMinFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardMinFlr.setUnits(_G)
class _JnxSoamLmCurrentAvailStatsForwardMaxFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentAvailStatsForwardMaxFlr_Type.__name__=_C
_JnxSoamLmCurrentAvailStatsForwardMaxFlr_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsForwardMaxFlr=_JnxSoamLmCurrentAvailStatsForwardMaxFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,14),_JnxSoamLmCurrentAvailStatsForwardMaxFlr_Type())
jnxSoamLmCurrentAvailStatsForwardMaxFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardMaxFlr.setUnits(_G)
class _JnxSoamLmCurrentAvailStatsForwardAvgFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentAvailStatsForwardAvgFlr_Type.__name__=_C
_JnxSoamLmCurrentAvailStatsForwardAvgFlr_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsForwardAvgFlr=_JnxSoamLmCurrentAvailStatsForwardAvgFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,15),_JnxSoamLmCurrentAvailStatsForwardAvgFlr_Type())
jnxSoamLmCurrentAvailStatsForwardAvgFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsForwardAvgFlr.setUnits(_G)
class _JnxSoamLmCurrentAvailStatsBackwardMinFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentAvailStatsBackwardMinFlr_Type.__name__=_C
_JnxSoamLmCurrentAvailStatsBackwardMinFlr_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardMinFlr=_JnxSoamLmCurrentAvailStatsBackwardMinFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,16),_JnxSoamLmCurrentAvailStatsBackwardMinFlr_Type())
jnxSoamLmCurrentAvailStatsBackwardMinFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardMinFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardMinFlr.setUnits(_G)
class _JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Type.__name__=_C
_JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardMaxFlr=_JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,17),_JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Type())
jnxSoamLmCurrentAvailStatsBackwardMaxFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardMaxFlr.setUnits(_G)
class _JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Type.__name__=_C
_JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Object=MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardAvgFlr=_JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,6,1,18),_JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Type())
jnxSoamLmCurrentAvailStatsBackwardAvgFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmCurrentAvailStatsBackwardAvgFlr.setUnits(_G)
_JnxSoamLmHistoryAvailStatsTable_Object=MibTable
jnxSoamLmHistoryAvailStatsTable=_JnxSoamLmHistoryAvailStatsTable_Object((1,3,6,1,4,1,2636,3,78,1,2,7))
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsTable.setStatus(_A)
_JnxSoamLmHistoryAvailStatsEntry_Object=MibTableRow
jnxSoamLmHistoryAvailStatsEntry=_JnxSoamLmHistoryAvailStatsEntry_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1))
jnxSoamLmHistoryAvailStatsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_O),(0,_E,_o))
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsEntry.setStatus(_A)
_JnxSoamLmHistoryAvailStatsIndex_Type=Unsigned32
_JnxSoamLmHistoryAvailStatsIndex_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsIndex=_JnxSoamLmHistoryAvailStatsIndex_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,1),_JnxSoamLmHistoryAvailStatsIndex_Type())
jnxSoamLmHistoryAvailStatsIndex.setMaxAccess(_e)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsIndex.setStatus(_A)
_JnxSoamLmHistoryAvailStatsEndTime_Type=DateAndTime
_JnxSoamLmHistoryAvailStatsEndTime_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsEndTime=_JnxSoamLmHistoryAvailStatsEndTime_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,2),_JnxSoamLmHistoryAvailStatsEndTime_Type())
jnxSoamLmHistoryAvailStatsEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsEndTime.setStatus(_A)
_JnxSoamLmHistoryAvailStatsElapsedTime_Type=TimeInterval
_JnxSoamLmHistoryAvailStatsElapsedTime_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsElapsedTime=_JnxSoamLmHistoryAvailStatsElapsedTime_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,3),_JnxSoamLmHistoryAvailStatsElapsedTime_Type())
jnxSoamLmHistoryAvailStatsElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsElapsedTime.setStatus(_A)
_JnxSoamLmHistoryAvailStatsSuspect_Type=TruthValue
_JnxSoamLmHistoryAvailStatsSuspect_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsSuspect=_JnxSoamLmHistoryAvailStatsSuspect_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,4),_JnxSoamLmHistoryAvailStatsSuspect_Type())
jnxSoamLmHistoryAvailStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsSuspect.setStatus(_A)
_JnxSoamLmHistoryAvailStatsForwardHighLoss_Type=Unsigned32
_JnxSoamLmHistoryAvailStatsForwardHighLoss_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsForwardHighLoss=_JnxSoamLmHistoryAvailStatsForwardHighLoss_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,5),_JnxSoamLmHistoryAvailStatsForwardHighLoss_Type())
jnxSoamLmHistoryAvailStatsForwardHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardHighLoss.setStatus(_A)
_JnxSoamLmHistoryAvailStatsBackwardHighLoss_Type=Unsigned32
_JnxSoamLmHistoryAvailStatsBackwardHighLoss_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardHighLoss=_JnxSoamLmHistoryAvailStatsBackwardHighLoss_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,6),_JnxSoamLmHistoryAvailStatsBackwardHighLoss_Type())
jnxSoamLmHistoryAvailStatsBackwardHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardHighLoss.setStatus(_A)
_JnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Type=Unsigned32
_JnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss=_JnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,7),_JnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Type())
jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss.setStatus(_A)
_JnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Type=Unsigned32
_JnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss=_JnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,8),_JnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Type())
jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss.setStatus(_A)
_JnxSoamLmHistoryAvailStatsForwardAvailable_Type=Gauge32
_JnxSoamLmHistoryAvailStatsForwardAvailable_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsForwardAvailable=_JnxSoamLmHistoryAvailStatsForwardAvailable_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,9),_JnxSoamLmHistoryAvailStatsForwardAvailable_Type())
jnxSoamLmHistoryAvailStatsForwardAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardAvailable.setStatus(_A)
_JnxSoamLmHistoryAvailStatsBackwardAvailable_Type=Gauge32
_JnxSoamLmHistoryAvailStatsBackwardAvailable_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardAvailable=_JnxSoamLmHistoryAvailStatsBackwardAvailable_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,10),_JnxSoamLmHistoryAvailStatsBackwardAvailable_Type())
jnxSoamLmHistoryAvailStatsBackwardAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardAvailable.setStatus(_A)
_JnxSoamLmHistoryAvailStatsForwardUnavailable_Type=Gauge32
_JnxSoamLmHistoryAvailStatsForwardUnavailable_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsForwardUnavailable=_JnxSoamLmHistoryAvailStatsForwardUnavailable_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,11),_JnxSoamLmHistoryAvailStatsForwardUnavailable_Type())
jnxSoamLmHistoryAvailStatsForwardUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardUnavailable.setStatus(_A)
_JnxSoamLmHistoryAvailStatsBackwardUnavailable_Type=Gauge32
_JnxSoamLmHistoryAvailStatsBackwardUnavailable_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardUnavailable=_JnxSoamLmHistoryAvailStatsBackwardUnavailable_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,12),_JnxSoamLmHistoryAvailStatsBackwardUnavailable_Type())
jnxSoamLmHistoryAvailStatsBackwardUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardUnavailable.setStatus(_A)
class _JnxSoamLmHistoryAvailStatsForwardMinFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryAvailStatsForwardMinFlr_Type.__name__=_C
_JnxSoamLmHistoryAvailStatsForwardMinFlr_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsForwardMinFlr=_JnxSoamLmHistoryAvailStatsForwardMinFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,13),_JnxSoamLmHistoryAvailStatsForwardMinFlr_Type())
jnxSoamLmHistoryAvailStatsForwardMinFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardMinFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardMinFlr.setUnits(_G)
class _JnxSoamLmHistoryAvailStatsForwardMaxFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryAvailStatsForwardMaxFlr_Type.__name__=_C
_JnxSoamLmHistoryAvailStatsForwardMaxFlr_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsForwardMaxFlr=_JnxSoamLmHistoryAvailStatsForwardMaxFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,14),_JnxSoamLmHistoryAvailStatsForwardMaxFlr_Type())
jnxSoamLmHistoryAvailStatsForwardMaxFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardMaxFlr.setUnits(_G)
class _JnxSoamLmHistoryAvailStatsForwardAvgFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryAvailStatsForwardAvgFlr_Type.__name__=_C
_JnxSoamLmHistoryAvailStatsForwardAvgFlr_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsForwardAvgFlr=_JnxSoamLmHistoryAvailStatsForwardAvgFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,15),_JnxSoamLmHistoryAvailStatsForwardAvgFlr_Type())
jnxSoamLmHistoryAvailStatsForwardAvgFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsForwardAvgFlr.setUnits(_G)
class _JnxSoamLmHistoryAvailStatsBackwardMinFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryAvailStatsBackwardMinFlr_Type.__name__=_C
_JnxSoamLmHistoryAvailStatsBackwardMinFlr_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardMinFlr=_JnxSoamLmHistoryAvailStatsBackwardMinFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,16),_JnxSoamLmHistoryAvailStatsBackwardMinFlr_Type())
jnxSoamLmHistoryAvailStatsBackwardMinFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardMinFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardMinFlr.setUnits(_G)
class _JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Type.__name__=_C
_JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardMaxFlr=_JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,17),_JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Type())
jnxSoamLmHistoryAvailStatsBackwardMaxFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardMaxFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardMaxFlr.setUnits(_G)
class _JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Type.__name__=_C
_JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Object=MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardAvgFlr=_JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Object((1,3,6,1,4,1,2636,3,78,1,2,7,1,18),_JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Type())
jnxSoamLmHistoryAvailStatsBackwardAvgFlr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardAvgFlr.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamLmHistoryAvailStatsBackwardAvgFlr.setUnits(_G)
_JnxSoamPmDmObjects_ObjectIdentity=ObjectIdentity
jnxSoamPmDmObjects=_JnxSoamPmDmObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,78,1,3))
_JnxSoamDmCfgTable_Object=MibTable
jnxSoamDmCfgTable=_JnxSoamDmCfgTable_Object((1,3,6,1,4,1,2636,3,78,1,3,1))
if mibBuilder.loadTexts:jnxSoamDmCfgTable.setStatus(_A)
_JnxSoamDmCfgEntry_Object=MibTableRow
jnxSoamDmCfgEntry=_JnxSoamDmCfgEntry_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1))
jnxSoamDmCfgEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_N))
if mibBuilder.loadTexts:jnxSoamDmCfgEntry.setStatus(_A)
class _JnxSoamDmCfgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_JnxSoamDmCfgIndex_Type.__name__=_C
_JnxSoamDmCfgIndex_Object=MibTableColumn
jnxSoamDmCfgIndex=_JnxSoamDmCfgIndex_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,1),_JnxSoamDmCfgIndex_Type())
jnxSoamDmCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgIndex.setStatus(_A)
class _JnxSoamDmCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dmDmm',1),('dm1DmTx',2),('dm1DmRx',3)))
_JnxSoamDmCfgType_Type.__name__=_P
_JnxSoamDmCfgType_Object=MibTableColumn
jnxSoamDmCfgType=_JnxSoamDmCfgType_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,2),_JnxSoamDmCfgType_Type())
jnxSoamDmCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgType.setStatus(_A)
class _JnxSoamDmCfgVersion_Type(Unsigned32):defaultValue=0
_JnxSoamDmCfgVersion_Type.__name__=_C
_JnxSoamDmCfgVersion_Object=MibTableColumn
jnxSoamDmCfgVersion=_JnxSoamDmCfgVersion_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,3),_JnxSoamDmCfgVersion_Type())
jnxSoamDmCfgVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgVersion.setStatus(_A)
class _JnxSoamDmCfgEnabled_Type(TruthValue):defaultValue=1
_JnxSoamDmCfgEnabled_Type.__name__=_L
_JnxSoamDmCfgEnabled_Object=MibTableColumn
jnxSoamDmCfgEnabled=_JnxSoamDmCfgEnabled_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,4),_JnxSoamDmCfgEnabled_Type())
jnxSoamDmCfgEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgEnabled.setStatus(_A)
class _JnxSoamDmCfgMeasurementEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*((_i,0),(_j,1),('bFrameDelayTwoWayBins',2),('bFrameDelayTwoWayMin',3),('bFrameDelayTwoWayMax',4),('bFrameDelayTwoWayAvg',5),('bFrameDelayForwardBins',6),('bFrameDelayForwardMin',7),('bFrameDelayForwardMax',8),('bFrameDelayForwardAvg',9),('bFrameDelayBackwardBins',10),('bFrameDelayBackwardMin',11),('bFrameDelayBackwardMax',12),('bFrameDelayBackwardAvg',13),('bIfdvForwardBins',14),('bIfdvForwardMin',15),('bIfdvForwardMax',16),('bIfdvForwardAvg',17),('bIfdvBackwardBins',18),('bIfdvBackwardMin',19),('bIfdvBackwardMax',20),('bIfdvBackwardAvg',21),('bIfdvTwoWayBins',22),('bIfdvTwoWayMin',23),('bIfdvTwoWayMax',24),('bIfdvTwoWayAvg',25),('bFrameDelayRangeForwardBins',26),('bFrameDelayRangeForwardMax',27),('bFrameDelayRangeForwardAvg',28),('bFrameDelayRangeBackwardBins',29),('bFrameDelayRangeBackwardMax',30),('bFrameDelayRangeBackwardAvg',31),('bFrameDelayRangeTwoWayBins',32),('bFrameDelayRangeTwoWayMax',33),('bFrameDelayRangeTwoWayAvg',34),('bMeasuredStatsFrameDelayTwoWay',35),('bMeasuredStatsFrameDelayForward',36),('bMeasuredStatsFrameDelayBackward',37),('bMeasuredStatsIfdvTwoWay',38),('bMeasuredStatsIfdvForward',39),('bMeasuredStatsIfdvBackward',40)))
_JnxSoamDmCfgMeasurementEnable_Type.__name__=_R
_JnxSoamDmCfgMeasurementEnable_Object=MibTableColumn
jnxSoamDmCfgMeasurementEnable=_JnxSoamDmCfgMeasurementEnable_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,5),_JnxSoamDmCfgMeasurementEnable_Type())
jnxSoamDmCfgMeasurementEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgMeasurementEnable.setStatus(_A)
class _JnxSoamDmCfgMessagePeriod_Type(Integer32):defaultValue=100
_JnxSoamDmCfgMessagePeriod_Type.__name__=_P
_JnxSoamDmCfgMessagePeriod_Object=MibTableColumn
jnxSoamDmCfgMessagePeriod=_JnxSoamDmCfgMessagePeriod_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,6),_JnxSoamDmCfgMessagePeriod_Type())
jnxSoamDmCfgMessagePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgMessagePeriod.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCfgMessagePeriod.setUnits('ms')
_JnxSoamDmCfgPriority_Type=IEEE8021PriorityValue
_JnxSoamDmCfgPriority_Object=MibTableColumn
jnxSoamDmCfgPriority=_JnxSoamDmCfgPriority_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,7),_JnxSoamDmCfgPriority_Type())
jnxSoamDmCfgPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgPriority.setStatus(_A)
class _JnxSoamDmCfgFrameSize_Type(Unsigned32):defaultValue=64
_JnxSoamDmCfgFrameSize_Type.__name__=_C
_JnxSoamDmCfgFrameSize_Object=MibTableColumn
jnxSoamDmCfgFrameSize=_JnxSoamDmCfgFrameSize_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,8),_JnxSoamDmCfgFrameSize_Type())
jnxSoamDmCfgFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgFrameSize.setStatus(_A)
class _JnxSoamDmCfgDataPattern_Type(JnxSoamTcDataPatternType):defaultValue=1
_JnxSoamDmCfgDataPattern_Type.__name__=_c
_JnxSoamDmCfgDataPattern_Object=MibTableColumn
jnxSoamDmCfgDataPattern=_JnxSoamDmCfgDataPattern_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,9),_JnxSoamDmCfgDataPattern_Type())
jnxSoamDmCfgDataPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgDataPattern.setStatus(_A)
class _JnxSoamDmCfgTestTlvIncluded_Type(TruthValue):defaultValue=2
_JnxSoamDmCfgTestTlvIncluded_Type.__name__=_L
_JnxSoamDmCfgTestTlvIncluded_Object=MibTableColumn
jnxSoamDmCfgTestTlvIncluded=_JnxSoamDmCfgTestTlvIncluded_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,10),_JnxSoamDmCfgTestTlvIncluded_Type())
jnxSoamDmCfgTestTlvIncluded.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgTestTlvIncluded.setStatus(_A)
class _JnxSoamDmCfgTestTlvPattern_Type(JnxSoamTcTestPatternType):defaultValue=1
_JnxSoamDmCfgTestTlvPattern_Type.__name__=_d
_JnxSoamDmCfgTestTlvPattern_Object=MibTableColumn
jnxSoamDmCfgTestTlvPattern=_JnxSoamDmCfgTestTlvPattern_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,11),_JnxSoamDmCfgTestTlvPattern_Type())
jnxSoamDmCfgTestTlvPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgTestTlvPattern.setStatus(_A)
class _JnxSoamDmCfgNumIntervalsStored_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_JnxSoamDmCfgNumIntervalsStored_Type.__name__=_C
_JnxSoamDmCfgNumIntervalsStored_Object=MibTableColumn
jnxSoamDmCfgNumIntervalsStored=_JnxSoamDmCfgNumIntervalsStored_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,12),_JnxSoamDmCfgNumIntervalsStored_Type())
jnxSoamDmCfgNumIntervalsStored.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgNumIntervalsStored.setStatus(_A)
class _JnxSoamDmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):defaultValue=0
_JnxSoamDmCfgDestMepId_Type.__name__=_b
_JnxSoamDmCfgDestMepId_Object=MibTableColumn
jnxSoamDmCfgDestMepId=_JnxSoamDmCfgDestMepId_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,13),_JnxSoamDmCfgDestMepId_Type())
jnxSoamDmCfgDestMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgDestMepId.setStatus(_A)
class _JnxSoamDmCfgDestIsMepId_Type(TruthValue):defaultValue=1
_JnxSoamDmCfgDestIsMepId_Type.__name__=_L
_JnxSoamDmCfgDestIsMepId_Object=MibTableColumn
jnxSoamDmCfgDestIsMepId=_JnxSoamDmCfgDestIsMepId_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,14),_JnxSoamDmCfgDestIsMepId_Type())
jnxSoamDmCfgDestIsMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgDestIsMepId.setStatus(_A)
class _JnxSoamDmCfgStartTimeType_Type(JnxSoamTcOperationTimeType):defaultValue=2
_JnxSoamDmCfgStartTimeType_Type.__name__=_U
_JnxSoamDmCfgStartTimeType_Object=MibTableColumn
jnxSoamDmCfgStartTimeType=_JnxSoamDmCfgStartTimeType_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,15),_JnxSoamDmCfgStartTimeType_Type())
jnxSoamDmCfgStartTimeType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgStartTimeType.setStatus(_A)
class _JnxSoamDmCfgRepetitionTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31536000))
_JnxSoamDmCfgRepetitionTime_Type.__name__=_C
_JnxSoamDmCfgRepetitionTime_Object=MibTableColumn
jnxSoamDmCfgRepetitionTime=_JnxSoamDmCfgRepetitionTime_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,16),_JnxSoamDmCfgRepetitionTime_Type())
jnxSoamDmCfgRepetitionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgRepetitionTime.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCfgRepetitionTime.setUnits(_k)
class _JnxSoamDmCfgAlignMeasurementIntervals_Type(TruthValue):defaultValue=1
_JnxSoamDmCfgAlignMeasurementIntervals_Type.__name__=_L
_JnxSoamDmCfgAlignMeasurementIntervals_Object=MibTableColumn
jnxSoamDmCfgAlignMeasurementIntervals=_JnxSoamDmCfgAlignMeasurementIntervals_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,17),_JnxSoamDmCfgAlignMeasurementIntervals_Type())
jnxSoamDmCfgAlignMeasurementIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgAlignMeasurementIntervals.setStatus(_A)
class _JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Type.__name__=_C
_JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Object=MibTableColumn
jnxSoamDmCfgInterFrameDelayVariationSelectionOffset=_JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,18),_JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Type())
jnxSoamDmCfgInterFrameDelayVariationSelectionOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgInterFrameDelayVariationSelectionOffset.setStatus(_A)
class _JnxSoamDmCfgSessionType_Type(OctetString):defaultValue=OctetString(_l);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,42))
_JnxSoamDmCfgSessionType_Type.__name__=_Q
_JnxSoamDmCfgSessionType_Object=MibTableColumn
jnxSoamDmCfgSessionType=_JnxSoamDmCfgSessionType_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,19),_JnxSoamDmCfgSessionType_Type())
jnxSoamDmCfgSessionType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgSessionType.setStatus(_A)
class _JnxSoamDmCfgSessionStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,42))
_JnxSoamDmCfgSessionStatus_Type.__name__=_Q
_JnxSoamDmCfgSessionStatus_Object=MibTableColumn
jnxSoamDmCfgSessionStatus=_JnxSoamDmCfgSessionStatus_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,20),_JnxSoamDmCfgSessionStatus_Type())
jnxSoamDmCfgSessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgSessionStatus.setStatus(_A)
class _JnxSoamDmCfgHistoryClear_Type(TruthValue):defaultValue=2
_JnxSoamDmCfgHistoryClear_Type.__name__=_L
_JnxSoamDmCfgHistoryClear_Object=MibTableColumn
jnxSoamDmCfgHistoryClear=_JnxSoamDmCfgHistoryClear_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,21),_JnxSoamDmCfgHistoryClear_Type())
jnxSoamDmCfgHistoryClear.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgHistoryClear.setStatus(_A)
_JnxSoamDmCfgRowStatus_Type=RowStatus
_JnxSoamDmCfgRowStatus_Object=MibTableColumn
jnxSoamDmCfgRowStatus=_JnxSoamDmCfgRowStatus_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,22),_JnxSoamDmCfgRowStatus_Type())
jnxSoamDmCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCfgRowStatus.setStatus(_A)
class _JnxSoamDmCfgMeasurementInterval_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_JnxSoamDmCfgMeasurementInterval_Type.__name__=_C
_JnxSoamDmCfgMeasurementInterval_Object=MibTableColumn
jnxSoamDmCfgMeasurementInterval=_JnxSoamDmCfgMeasurementInterval_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,23),_JnxSoamDmCfgMeasurementInterval_Type())
jnxSoamDmCfgMeasurementInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgMeasurementInterval.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCfgMeasurementInterval.setUnits(_V)
_JnxSoamDmCfgDestMacAddress_Type=MacAddress
_JnxSoamDmCfgDestMacAddress_Object=MibTableColumn
jnxSoamDmCfgDestMacAddress=_JnxSoamDmCfgDestMacAddress_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,24),_JnxSoamDmCfgDestMacAddress_Type())
jnxSoamDmCfgDestMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgDestMacAddress.setStatus(_A)
_JnxSoamDmCfgSourceMacAddress_Type=MacAddress
_JnxSoamDmCfgSourceMacAddress_Object=MibTableColumn
jnxSoamDmCfgSourceMacAddress=_JnxSoamDmCfgSourceMacAddress_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,25),_JnxSoamDmCfgSourceMacAddress_Type())
jnxSoamDmCfgSourceMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgSourceMacAddress.setStatus(_A)
class _JnxSoamDmCfgFixedStartDateAndTime_Type(DateAndTime):defaultHexValue=_X
_JnxSoamDmCfgFixedStartDateAndTime_Type.__name__=_S
_JnxSoamDmCfgFixedStartDateAndTime_Object=MibTableColumn
jnxSoamDmCfgFixedStartDateAndTime=_JnxSoamDmCfgFixedStartDateAndTime_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,26),_JnxSoamDmCfgFixedStartDateAndTime_Type())
jnxSoamDmCfgFixedStartDateAndTime.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgFixedStartDateAndTime.setStatus(_A)
class _JnxSoamDmCfgRelativeStartTime_Type(TimeInterval):defaultValue=0
_JnxSoamDmCfgRelativeStartTime_Type.__name__=_T
_JnxSoamDmCfgRelativeStartTime_Object=MibTableColumn
jnxSoamDmCfgRelativeStartTime=_JnxSoamDmCfgRelativeStartTime_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,27),_JnxSoamDmCfgRelativeStartTime_Type())
jnxSoamDmCfgRelativeStartTime.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgRelativeStartTime.setStatus(_A)
class _JnxSoamDmCfgStopTimeType_Type(JnxSoamTcOperationTimeType):defaultValue=1
_JnxSoamDmCfgStopTimeType_Type.__name__=_U
_JnxSoamDmCfgStopTimeType_Object=MibTableColumn
jnxSoamDmCfgStopTimeType=_JnxSoamDmCfgStopTimeType_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,28),_JnxSoamDmCfgStopTimeType_Type())
jnxSoamDmCfgStopTimeType.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgStopTimeType.setStatus(_A)
class _JnxSoamDmCfgFixedStopDateAndTime_Type(DateAndTime):defaultHexValue=_X
_JnxSoamDmCfgFixedStopDateAndTime_Type.__name__=_S
_JnxSoamDmCfgFixedStopDateAndTime_Object=MibTableColumn
jnxSoamDmCfgFixedStopDateAndTime=_JnxSoamDmCfgFixedStopDateAndTime_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,29),_JnxSoamDmCfgFixedStopDateAndTime_Type())
jnxSoamDmCfgFixedStopDateAndTime.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgFixedStopDateAndTime.setStatus(_A)
class _JnxSoamDmCfgRelativeStopTime_Type(TimeInterval):defaultValue=0
_JnxSoamDmCfgRelativeStopTime_Type.__name__=_T
_JnxSoamDmCfgRelativeStopTime_Object=MibTableColumn
jnxSoamDmCfgRelativeStopTime=_JnxSoamDmCfgRelativeStopTime_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,30),_JnxSoamDmCfgRelativeStopTime_Type())
jnxSoamDmCfgRelativeStopTime.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgRelativeStopTime.setStatus(_A)
class _JnxSoamDmCfgAlignMeasurementOffset_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,525600))
_JnxSoamDmCfgAlignMeasurementOffset_Type.__name__=_C
_JnxSoamDmCfgAlignMeasurementOffset_Object=MibTableColumn
jnxSoamDmCfgAlignMeasurementOffset=_JnxSoamDmCfgAlignMeasurementOffset_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,31),_JnxSoamDmCfgAlignMeasurementOffset_Type())
jnxSoamDmCfgAlignMeasurementOffset.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgAlignMeasurementOffset.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCfgAlignMeasurementOffset.setUnits(_V)
class _JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,100))
_JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type.__name__=_C
_JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Object=MibTableColumn
jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval=_JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,32),_JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type())
jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval.setStatus(_A)
class _JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,100))
_JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type.__name__=_C
_JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Object=MibTableColumn
jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval=_JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,33),_JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type())
jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval.setStatus(_A)
class _JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,100))
_JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type.__name__=_C
_JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Object=MibTableColumn
jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval=_JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Object((1,3,6,1,4,1,2636,3,78,1,3,1,1,34),_JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type())
jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval.setStatus(_A)
_JnxSoamDmMeasuredStatsTable_Object=MibTable
jnxSoamDmMeasuredStatsTable=_JnxSoamDmMeasuredStatsTable_Object((1,3,6,1,4,1,2636,3,78,1,3,2))
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsTable.setStatus(_A)
_JnxSoamDmMeasuredStatsEntry_Object=MibTableRow
jnxSoamDmMeasuredStatsEntry=_JnxSoamDmMeasuredStatsEntry_Object((1,3,6,1,4,1,2636,3,78,1,3,2,1))
jnxSoamDmMeasuredStatsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_N))
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsEntry.setStatus(_A)
_JnxSoamDmMeasuredStatsFrameDelayTwoWay_Type=Unsigned32
_JnxSoamDmMeasuredStatsFrameDelayTwoWay_Object=MibTableColumn
jnxSoamDmMeasuredStatsFrameDelayTwoWay=_JnxSoamDmMeasuredStatsFrameDelayTwoWay_Object((1,3,6,1,4,1,2636,3,78,1,3,2,1,1),_JnxSoamDmMeasuredStatsFrameDelayTwoWay_Type())
jnxSoamDmMeasuredStatsFrameDelayTwoWay.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsFrameDelayTwoWay.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsFrameDelayTwoWay.setUnits(_D)
_JnxSoamDmMeasuredStatsFrameDelayForward_Type=Unsigned32
_JnxSoamDmMeasuredStatsFrameDelayForward_Object=MibTableColumn
jnxSoamDmMeasuredStatsFrameDelayForward=_JnxSoamDmMeasuredStatsFrameDelayForward_Object((1,3,6,1,4,1,2636,3,78,1,3,2,1,2),_JnxSoamDmMeasuredStatsFrameDelayForward_Type())
jnxSoamDmMeasuredStatsFrameDelayForward.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsFrameDelayForward.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsFrameDelayForward.setUnits(_D)
_JnxSoamDmMeasuredStatsFrameDelayBackward_Type=Unsigned32
_JnxSoamDmMeasuredStatsFrameDelayBackward_Object=MibTableColumn
jnxSoamDmMeasuredStatsFrameDelayBackward=_JnxSoamDmMeasuredStatsFrameDelayBackward_Object((1,3,6,1,4,1,2636,3,78,1,3,2,1,3),_JnxSoamDmMeasuredStatsFrameDelayBackward_Type())
jnxSoamDmMeasuredStatsFrameDelayBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsFrameDelayBackward.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsFrameDelayBackward.setUnits(_D)
_JnxSoamDmMeasuredStatsIfdvTwoWay_Type=Unsigned32
_JnxSoamDmMeasuredStatsIfdvTwoWay_Object=MibTableColumn
jnxSoamDmMeasuredStatsIfdvTwoWay=_JnxSoamDmMeasuredStatsIfdvTwoWay_Object((1,3,6,1,4,1,2636,3,78,1,3,2,1,4),_JnxSoamDmMeasuredStatsIfdvTwoWay_Type())
jnxSoamDmMeasuredStatsIfdvTwoWay.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsIfdvTwoWay.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsIfdvTwoWay.setUnits(_D)
_JnxSoamDmMeasuredStatsIfdvForward_Type=Unsigned32
_JnxSoamDmMeasuredStatsIfdvForward_Object=MibTableColumn
jnxSoamDmMeasuredStatsIfdvForward=_JnxSoamDmMeasuredStatsIfdvForward_Object((1,3,6,1,4,1,2636,3,78,1,3,2,1,5),_JnxSoamDmMeasuredStatsIfdvForward_Type())
jnxSoamDmMeasuredStatsIfdvForward.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsIfdvForward.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsIfdvForward.setUnits(_D)
_JnxSoamDmMeasuredStatsIfdvBackward_Type=Unsigned32
_JnxSoamDmMeasuredStatsIfdvBackward_Object=MibTableColumn
jnxSoamDmMeasuredStatsIfdvBackward=_JnxSoamDmMeasuredStatsIfdvBackward_Object((1,3,6,1,4,1,2636,3,78,1,3,2,1,6),_JnxSoamDmMeasuredStatsIfdvBackward_Type())
jnxSoamDmMeasuredStatsIfdvBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsIfdvBackward.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmMeasuredStatsIfdvBackward.setUnits(_D)
_JnxSoamDmCurrentStatsTable_Object=MibTable
jnxSoamDmCurrentStatsTable=_JnxSoamDmCurrentStatsTable_Object((1,3,6,1,4,1,2636,3,78,1,3,3))
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsTable.setStatus(_A)
_JnxSoamDmCurrentStatsEntry_Object=MibTableRow
jnxSoamDmCurrentStatsEntry=_JnxSoamDmCurrentStatsEntry_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1))
jnxSoamDmCurrentStatsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_N))
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsEntry.setStatus(_A)
_JnxSoamDmCurrentStatsIndex_Type=Unsigned32
_JnxSoamDmCurrentStatsIndex_Object=MibTableColumn
jnxSoamDmCurrentStatsIndex=_JnxSoamDmCurrentStatsIndex_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,1),_JnxSoamDmCurrentStatsIndex_Type())
jnxSoamDmCurrentStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIndex.setStatus(_A)
_JnxSoamDmCurrentStatsStartTime_Type=DateAndTime
_JnxSoamDmCurrentStatsStartTime_Object=MibTableColumn
jnxSoamDmCurrentStatsStartTime=_JnxSoamDmCurrentStatsStartTime_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,2),_JnxSoamDmCurrentStatsStartTime_Type())
jnxSoamDmCurrentStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsStartTime.setStatus(_A)
_JnxSoamDmCurrentStatsElapsedTime_Type=TimeInterval
_JnxSoamDmCurrentStatsElapsedTime_Object=MibTableColumn
jnxSoamDmCurrentStatsElapsedTime=_JnxSoamDmCurrentStatsElapsedTime_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,3),_JnxSoamDmCurrentStatsElapsedTime_Type())
jnxSoamDmCurrentStatsElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsElapsedTime.setStatus(_A)
_JnxSoamDmCurrentStatsSuspect_Type=TruthValue
_JnxSoamDmCurrentStatsSuspect_Object=MibTableColumn
jnxSoamDmCurrentStatsSuspect=_JnxSoamDmCurrentStatsSuspect_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,4),_JnxSoamDmCurrentStatsSuspect_Type())
jnxSoamDmCurrentStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsSuspect.setStatus(_A)
_JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayTwoWayMin=_JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,5),_JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Type())
jnxSoamDmCurrentStatsFrameDelayTwoWayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayTwoWayMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayTwoWayMin.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayTwoWayMax=_JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,6),_JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Type())
jnxSoamDmCurrentStatsFrameDelayTwoWayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayTwoWayMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayTwoWayMax.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayTwoWayAvg=_JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,7),_JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Type())
jnxSoamDmCurrentStatsFrameDelayTwoWayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayTwoWayAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayTwoWayAvg.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayForwardMin_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayForwardMin_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayForwardMin=_JnxSoamDmCurrentStatsFrameDelayForwardMin_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,8),_JnxSoamDmCurrentStatsFrameDelayForwardMin_Type())
jnxSoamDmCurrentStatsFrameDelayForwardMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayForwardMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayForwardMin.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayForwardMax_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayForwardMax_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayForwardMax=_JnxSoamDmCurrentStatsFrameDelayForwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,9),_JnxSoamDmCurrentStatsFrameDelayForwardMax_Type())
jnxSoamDmCurrentStatsFrameDelayForwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayForwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayForwardMax.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayForwardAvg_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayForwardAvg_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayForwardAvg=_JnxSoamDmCurrentStatsFrameDelayForwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,10),_JnxSoamDmCurrentStatsFrameDelayForwardAvg_Type())
jnxSoamDmCurrentStatsFrameDelayForwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayForwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayForwardAvg.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayBackwardMin_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayBackwardMin_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayBackwardMin=_JnxSoamDmCurrentStatsFrameDelayBackwardMin_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,11),_JnxSoamDmCurrentStatsFrameDelayBackwardMin_Type())
jnxSoamDmCurrentStatsFrameDelayBackwardMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayBackwardMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayBackwardMin.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayBackwardMax_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayBackwardMax_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayBackwardMax=_JnxSoamDmCurrentStatsFrameDelayBackwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,12),_JnxSoamDmCurrentStatsFrameDelayBackwardMax_Type())
jnxSoamDmCurrentStatsFrameDelayBackwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayBackwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayBackwardMax.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayBackwardAvg=_JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,13),_JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Type())
jnxSoamDmCurrentStatsFrameDelayBackwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayBackwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayBackwardAvg.setUnits(_D)
_JnxSoamDmCurrentStatsIfdvForwardMin_Type=Unsigned32
_JnxSoamDmCurrentStatsIfdvForwardMin_Object=MibTableColumn
jnxSoamDmCurrentStatsIfdvForwardMin=_JnxSoamDmCurrentStatsIfdvForwardMin_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,14),_JnxSoamDmCurrentStatsIfdvForwardMin_Type())
jnxSoamDmCurrentStatsIfdvForwardMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvForwardMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvForwardMin.setUnits(_D)
_JnxSoamDmCurrentStatsIfdvForwardMax_Type=Unsigned32
_JnxSoamDmCurrentStatsIfdvForwardMax_Object=MibTableColumn
jnxSoamDmCurrentStatsIfdvForwardMax=_JnxSoamDmCurrentStatsIfdvForwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,15),_JnxSoamDmCurrentStatsIfdvForwardMax_Type())
jnxSoamDmCurrentStatsIfdvForwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvForwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvForwardMax.setUnits(_D)
_JnxSoamDmCurrentStatsIfdvForwardAvg_Type=Unsigned32
_JnxSoamDmCurrentStatsIfdvForwardAvg_Object=MibTableColumn
jnxSoamDmCurrentStatsIfdvForwardAvg=_JnxSoamDmCurrentStatsIfdvForwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,16),_JnxSoamDmCurrentStatsIfdvForwardAvg_Type())
jnxSoamDmCurrentStatsIfdvForwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvForwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvForwardAvg.setUnits(_D)
_JnxSoamDmCurrentStatsIfdvBackwardMin_Type=Unsigned32
_JnxSoamDmCurrentStatsIfdvBackwardMin_Object=MibTableColumn
jnxSoamDmCurrentStatsIfdvBackwardMin=_JnxSoamDmCurrentStatsIfdvBackwardMin_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,17),_JnxSoamDmCurrentStatsIfdvBackwardMin_Type())
jnxSoamDmCurrentStatsIfdvBackwardMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvBackwardMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvBackwardMin.setUnits(_D)
_JnxSoamDmCurrentStatsIfdvBackwardMax_Type=Unsigned32
_JnxSoamDmCurrentStatsIfdvBackwardMax_Object=MibTableColumn
jnxSoamDmCurrentStatsIfdvBackwardMax=_JnxSoamDmCurrentStatsIfdvBackwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,18),_JnxSoamDmCurrentStatsIfdvBackwardMax_Type())
jnxSoamDmCurrentStatsIfdvBackwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvBackwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvBackwardMax.setUnits(_D)
_JnxSoamDmCurrentStatsIfdvBackwardAvg_Type=Unsigned32
_JnxSoamDmCurrentStatsIfdvBackwardAvg_Object=MibTableColumn
jnxSoamDmCurrentStatsIfdvBackwardAvg=_JnxSoamDmCurrentStatsIfdvBackwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,19),_JnxSoamDmCurrentStatsIfdvBackwardAvg_Type())
jnxSoamDmCurrentStatsIfdvBackwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvBackwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvBackwardAvg.setUnits(_D)
_JnxSoamDmCurrentStatsIfdvTwoWayMin_Type=Unsigned32
_JnxSoamDmCurrentStatsIfdvTwoWayMin_Object=MibTableColumn
jnxSoamDmCurrentStatsIfdvTwoWayMin=_JnxSoamDmCurrentStatsIfdvTwoWayMin_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,20),_JnxSoamDmCurrentStatsIfdvTwoWayMin_Type())
jnxSoamDmCurrentStatsIfdvTwoWayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvTwoWayMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvTwoWayMin.setUnits(_D)
_JnxSoamDmCurrentStatsIfdvTwoWayMax_Type=Unsigned32
_JnxSoamDmCurrentStatsIfdvTwoWayMax_Object=MibTableColumn
jnxSoamDmCurrentStatsIfdvTwoWayMax=_JnxSoamDmCurrentStatsIfdvTwoWayMax_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,21),_JnxSoamDmCurrentStatsIfdvTwoWayMax_Type())
jnxSoamDmCurrentStatsIfdvTwoWayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvTwoWayMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvTwoWayMax.setUnits(_D)
_JnxSoamDmCurrentStatsIfdvTwoWayAvg_Type=Unsigned32
_JnxSoamDmCurrentStatsIfdvTwoWayAvg_Object=MibTableColumn
jnxSoamDmCurrentStatsIfdvTwoWayAvg=_JnxSoamDmCurrentStatsIfdvTwoWayAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,22),_JnxSoamDmCurrentStatsIfdvTwoWayAvg_Type())
jnxSoamDmCurrentStatsIfdvTwoWayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvTwoWayAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsIfdvTwoWayAvg.setUnits(_D)
_JnxSoamDmCurrentStatsSoamPdusSent_Type=Gauge32
_JnxSoamDmCurrentStatsSoamPdusSent_Object=MibTableColumn
jnxSoamDmCurrentStatsSoamPdusSent=_JnxSoamDmCurrentStatsSoamPdusSent_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,23),_JnxSoamDmCurrentStatsSoamPdusSent_Type())
jnxSoamDmCurrentStatsSoamPdusSent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsSoamPdusSent.setStatus(_A)
_JnxSoamDmCurrentStatsSoamPdusReceived_Type=Gauge32
_JnxSoamDmCurrentStatsSoamPdusReceived_Object=MibTableColumn
jnxSoamDmCurrentStatsSoamPdusReceived=_JnxSoamDmCurrentStatsSoamPdusReceived_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,24),_JnxSoamDmCurrentStatsSoamPdusReceived_Type())
jnxSoamDmCurrentStatsSoamPdusReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsSoamPdusReceived.setStatus(_A)
_JnxSoamDmCurrentStatsFrameDelayRangeForwardMax_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeForwardMax_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeForwardMax=_JnxSoamDmCurrentStatsFrameDelayRangeForwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,25),_JnxSoamDmCurrentStatsFrameDelayRangeForwardMax_Type())
jnxSoamDmCurrentStatsFrameDelayRangeForwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeForwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeForwardMax.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayRangeForwardAvg_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeForwardAvg_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg=_JnxSoamDmCurrentStatsFrameDelayRangeForwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,26),_JnxSoamDmCurrentStatsFrameDelayRangeForwardAvg_Type())
jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayRangeBackwardMax_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeBackwardMax_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax=_JnxSoamDmCurrentStatsFrameDelayRangeBackwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,27),_JnxSoamDmCurrentStatsFrameDelayRangeBackwardMax_Type())
jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg=_JnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,28),_JnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Type())
jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax=_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,29),_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Type())
jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax.setUnits(_D)
_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Type=Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Object=MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg=_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,3,1,30),_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Type())
jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg.setUnits(_D)
_JnxSoamDmHistoryStatsTable_Object=MibTable
jnxSoamDmHistoryStatsTable=_JnxSoamDmHistoryStatsTable_Object((1,3,6,1,4,1,2636,3,78,1,3,4))
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsTable.setStatus(_A)
_JnxSoamDmHistoryStatsEntry_Object=MibTableRow
jnxSoamDmHistoryStatsEntry=_JnxSoamDmHistoryStatsEntry_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1))
jnxSoamDmHistoryStatsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_N),(0,_E,_f))
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsEntry.setStatus(_A)
_JnxSoamDmHistoryStatsIndex_Type=Unsigned32
_JnxSoamDmHistoryStatsIndex_Object=MibTableColumn
jnxSoamDmHistoryStatsIndex=_JnxSoamDmHistoryStatsIndex_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,1),_JnxSoamDmHistoryStatsIndex_Type())
jnxSoamDmHistoryStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIndex.setStatus(_A)
_JnxSoamDmHistoryStatsEndTime_Type=DateAndTime
_JnxSoamDmHistoryStatsEndTime_Object=MibTableColumn
jnxSoamDmHistoryStatsEndTime=_JnxSoamDmHistoryStatsEndTime_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,2),_JnxSoamDmHistoryStatsEndTime_Type())
jnxSoamDmHistoryStatsEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsEndTime.setStatus(_A)
_JnxSoamDmHistoryStatsElapsedTime_Type=TimeInterval
_JnxSoamDmHistoryStatsElapsedTime_Object=MibTableColumn
jnxSoamDmHistoryStatsElapsedTime=_JnxSoamDmHistoryStatsElapsedTime_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,3),_JnxSoamDmHistoryStatsElapsedTime_Type())
jnxSoamDmHistoryStatsElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsElapsedTime.setStatus(_A)
_JnxSoamDmHistoryStatsSuspect_Type=TruthValue
_JnxSoamDmHistoryStatsSuspect_Object=MibTableColumn
jnxSoamDmHistoryStatsSuspect=_JnxSoamDmHistoryStatsSuspect_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,4),_JnxSoamDmHistoryStatsSuspect_Type())
jnxSoamDmHistoryStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsSuspect.setStatus(_A)
_JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayTwoWayMin=_JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,5),_JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Type())
jnxSoamDmHistoryStatsFrameDelayTwoWayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayTwoWayMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayTwoWayMin.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayTwoWayMax=_JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,6),_JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Type())
jnxSoamDmHistoryStatsFrameDelayTwoWayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayTwoWayMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayTwoWayMax.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayTwoWayAvg=_JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,7),_JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Type())
jnxSoamDmHistoryStatsFrameDelayTwoWayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayTwoWayAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayTwoWayAvg.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayForwardMin_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayForwardMin_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayForwardMin=_JnxSoamDmHistoryStatsFrameDelayForwardMin_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,8),_JnxSoamDmHistoryStatsFrameDelayForwardMin_Type())
jnxSoamDmHistoryStatsFrameDelayForwardMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayForwardMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayForwardMin.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayForwardMax_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayForwardMax_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayForwardMax=_JnxSoamDmHistoryStatsFrameDelayForwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,9),_JnxSoamDmHistoryStatsFrameDelayForwardMax_Type())
jnxSoamDmHistoryStatsFrameDelayForwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayForwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayForwardMax.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayForwardAvg_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayForwardAvg_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayForwardAvg=_JnxSoamDmHistoryStatsFrameDelayForwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,10),_JnxSoamDmHistoryStatsFrameDelayForwardAvg_Type())
jnxSoamDmHistoryStatsFrameDelayForwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayForwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayForwardAvg.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayBackwardMin_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayBackwardMin_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayBackwardMin=_JnxSoamDmHistoryStatsFrameDelayBackwardMin_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,11),_JnxSoamDmHistoryStatsFrameDelayBackwardMin_Type())
jnxSoamDmHistoryStatsFrameDelayBackwardMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayBackwardMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayBackwardMin.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayBackwardMax_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayBackwardMax_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayBackwardMax=_JnxSoamDmHistoryStatsFrameDelayBackwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,12),_JnxSoamDmHistoryStatsFrameDelayBackwardMax_Type())
jnxSoamDmHistoryStatsFrameDelayBackwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayBackwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayBackwardMax.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayBackwardAvg=_JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,13),_JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Type())
jnxSoamDmHistoryStatsFrameDelayBackwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayBackwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayBackwardAvg.setUnits(_D)
_JnxSoamDmHistoryStatsIfdvForwardMin_Type=Unsigned32
_JnxSoamDmHistoryStatsIfdvForwardMin_Object=MibTableColumn
jnxSoamDmHistoryStatsIfdvForwardMin=_JnxSoamDmHistoryStatsIfdvForwardMin_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,14),_JnxSoamDmHistoryStatsIfdvForwardMin_Type())
jnxSoamDmHistoryStatsIfdvForwardMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvForwardMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvForwardMin.setUnits(_D)
_JnxSoamDmHistoryStatsIfdvForwardMax_Type=Unsigned32
_JnxSoamDmHistoryStatsIfdvForwardMax_Object=MibTableColumn
jnxSoamDmHistoryStatsIfdvForwardMax=_JnxSoamDmHistoryStatsIfdvForwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,15),_JnxSoamDmHistoryStatsIfdvForwardMax_Type())
jnxSoamDmHistoryStatsIfdvForwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvForwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvForwardMax.setUnits(_D)
_JnxSoamDmHistoryStatsIfdvForwardAvg_Type=Unsigned32
_JnxSoamDmHistoryStatsIfdvForwardAvg_Object=MibTableColumn
jnxSoamDmHistoryStatsIfdvForwardAvg=_JnxSoamDmHistoryStatsIfdvForwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,16),_JnxSoamDmHistoryStatsIfdvForwardAvg_Type())
jnxSoamDmHistoryStatsIfdvForwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvForwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvForwardAvg.setUnits(_D)
_JnxSoamDmHistoryStatsIfdvBackwardMin_Type=Unsigned32
_JnxSoamDmHistoryStatsIfdvBackwardMin_Object=MibTableColumn
jnxSoamDmHistoryStatsIfdvBackwardMin=_JnxSoamDmHistoryStatsIfdvBackwardMin_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,17),_JnxSoamDmHistoryStatsIfdvBackwardMin_Type())
jnxSoamDmHistoryStatsIfdvBackwardMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvBackwardMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvBackwardMin.setUnits(_D)
_JnxSoamDmHistoryStatsIfdvBackwardMax_Type=Unsigned32
_JnxSoamDmHistoryStatsIfdvBackwardMax_Object=MibTableColumn
jnxSoamDmHistoryStatsIfdvBackwardMax=_JnxSoamDmHistoryStatsIfdvBackwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,18),_JnxSoamDmHistoryStatsIfdvBackwardMax_Type())
jnxSoamDmHistoryStatsIfdvBackwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvBackwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvBackwardMax.setUnits(_D)
_JnxSoamDmHistoryStatsIfdvBackwardAvg_Type=Unsigned32
_JnxSoamDmHistoryStatsIfdvBackwardAvg_Object=MibTableColumn
jnxSoamDmHistoryStatsIfdvBackwardAvg=_JnxSoamDmHistoryStatsIfdvBackwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,19),_JnxSoamDmHistoryStatsIfdvBackwardAvg_Type())
jnxSoamDmHistoryStatsIfdvBackwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvBackwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvBackwardAvg.setUnits(_D)
_JnxSoamDmHistoryStatsIfdvTwoWayMin_Type=Unsigned32
_JnxSoamDmHistoryStatsIfdvTwoWayMin_Object=MibTableColumn
jnxSoamDmHistoryStatsIfdvTwoWayMin=_JnxSoamDmHistoryStatsIfdvTwoWayMin_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,20),_JnxSoamDmHistoryStatsIfdvTwoWayMin_Type())
jnxSoamDmHistoryStatsIfdvTwoWayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvTwoWayMin.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvTwoWayMin.setUnits(_D)
_JnxSoamDmHistoryStatsIfdvTwoWayMax_Type=Unsigned32
_JnxSoamDmHistoryStatsIfdvTwoWayMax_Object=MibTableColumn
jnxSoamDmHistoryStatsIfdvTwoWayMax=_JnxSoamDmHistoryStatsIfdvTwoWayMax_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,21),_JnxSoamDmHistoryStatsIfdvTwoWayMax_Type())
jnxSoamDmHistoryStatsIfdvTwoWayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvTwoWayMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvTwoWayMax.setUnits(_D)
_JnxSoamDmHistoryStatsIfdvTwoWayAvg_Type=Unsigned32
_JnxSoamDmHistoryStatsIfdvTwoWayAvg_Object=MibTableColumn
jnxSoamDmHistoryStatsIfdvTwoWayAvg=_JnxSoamDmHistoryStatsIfdvTwoWayAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,22),_JnxSoamDmHistoryStatsIfdvTwoWayAvg_Type())
jnxSoamDmHistoryStatsIfdvTwoWayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvTwoWayAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsIfdvTwoWayAvg.setUnits(_D)
_JnxSoamDmHistoryStatsSoamPdusSent_Type=Gauge32
_JnxSoamDmHistoryStatsSoamPdusSent_Object=MibTableColumn
jnxSoamDmHistoryStatsSoamPdusSent=_JnxSoamDmHistoryStatsSoamPdusSent_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,23),_JnxSoamDmHistoryStatsSoamPdusSent_Type())
jnxSoamDmHistoryStatsSoamPdusSent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsSoamPdusSent.setStatus(_A)
_JnxSoamDmHistoryStatsSoamPdusReceived_Type=Gauge32
_JnxSoamDmHistoryStatsSoamPdusReceived_Object=MibTableColumn
jnxSoamDmHistoryStatsSoamPdusReceived=_JnxSoamDmHistoryStatsSoamPdusReceived_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,24),_JnxSoamDmHistoryStatsSoamPdusReceived_Type())
jnxSoamDmHistoryStatsSoamPdusReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsSoamPdusReceived.setStatus(_A)
_JnxSoamDmHistoryStatsFrameDelayRangeForwardMax_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeForwardMax_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeForwardMax=_JnxSoamDmHistoryStatsFrameDelayRangeForwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,25),_JnxSoamDmHistoryStatsFrameDelayRangeForwardMax_Type())
jnxSoamDmHistoryStatsFrameDelayRangeForwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeForwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeForwardMax.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayRangeForwardAvg_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeForwardAvg_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg=_JnxSoamDmHistoryStatsFrameDelayRangeForwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,26),_JnxSoamDmHistoryStatsFrameDelayRangeForwardAvg_Type())
jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayRangeBackwardMax_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeBackwardMax_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax=_JnxSoamDmHistoryStatsFrameDelayRangeBackwardMax_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,27),_JnxSoamDmHistoryStatsFrameDelayRangeBackwardMax_Type())
jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg=_JnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,28),_JnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Type())
jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax=_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,29),_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Type())
jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax.setUnits(_D)
_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Type=Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Object=MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg=_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Object((1,3,6,1,4,1,2636,3,78,1,3,4,1,30),_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Type())
jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg.setUnits(_D)
_JnxSoamDmThresholdCfgTable_Object=MibTable
jnxSoamDmThresholdCfgTable=_JnxSoamDmThresholdCfgTable_Object((1,3,6,1,4,1,2636,3,78,1,3,5))
if mibBuilder.loadTexts:jnxSoamDmThresholdCfgTable.setStatus(_A)
_JnxSoamDmThresholdCfgEntry_Object=MibTableRow
jnxSoamDmThresholdCfgEntry=_JnxSoamDmThresholdCfgEntry_Object((1,3,6,1,4,1,2636,3,78,1,3,5,1))
jnxSoamDmThresholdCfgEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_N),(0,_E,_p))
if mibBuilder.loadTexts:jnxSoamDmThresholdCfgEntry.setStatus(_A)
class _JnxSoamDmThresholdCfgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_JnxSoamDmThresholdCfgIndex_Type.__name__=_C
_JnxSoamDmThresholdCfgIndex_Object=MibTableColumn
jnxSoamDmThresholdCfgIndex=_JnxSoamDmThresholdCfgIndex_Object((1,3,6,1,4,1,2636,3,78,1,3,5,1,1),_JnxSoamDmThresholdCfgIndex_Type())
jnxSoamDmThresholdCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmThresholdCfgIndex.setStatus(_A)
class _JnxSoamDmThresholdCfgEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('bJnxSoamDmMeasuredFrameDelayTwoWayThreshold',0),('bJnxSoamDmMaxFrameDelayTwoWayThreshold',1),('bJnxSoamDmAvgFrameDelayTwoWayThreshold',2),('bJnxSoamDmMeasuredIfdvTwoWayThreshold',3),('bJnxSoamDmMaxIfdvTwoWayThreshold',4),('bJnxSoamDmAvgIfdvTwoWayThreshold',5),('bJnxSoamDmMaxFrameDelayRangeTwoWayThreshold',6),('bJnxSoamDmAvgFrameDelayRangeTwoWayThreshold',7),('bJnxSoamDmMeasuredFrameDelayForwardThreshold',8),('bJnxSoamDmMaxFrameDelayForwardThreshold',9),('bJnxSoamDmAvgFrameDelayForwardThreshold',10),('bJnxSoamDmMeasuredIfdvForwardThreshold',11),('bJnxSoamDmMaxIfdvForwardThreshold',12),('bJnxSoamDmAvgIfdvForwardThreshold',13),('bJnxSoamDmMaxFrameDelayRangeForwardThreshold',14),('bJnxSoamDmAvgFrameDelayRangeForwardThreshold',15),('bJnxSoamDmMeasuredFrameDelayBackwardThreshold',16),('bJnxSoamDmMaxFrameDelayBackwardThreshold',17),('bJnxSoamDmAvgFrameDelayBackwardThreshold',18),('bJnxSoamDmMeasuredIfdvBackwardThreshold',19),('bJnxSoamDmMaxIfdvBackwardThreshold',20),('bJnxSoamDmAvgIfdvBackwardThreshold',21),('bJnxSoamDmMaxFrameDelayRangeBackwardThreshold',22),('bJnxSoamDmAvgFrameDelayRangeBackwardThreshold',23)))
_JnxSoamDmThresholdCfgEnable_Type.__name__=_R
_JnxSoamDmThresholdCfgEnable_Object=MibTableColumn
jnxSoamDmThresholdCfgEnable=_JnxSoamDmThresholdCfgEnable_Object((1,3,6,1,4,1,2636,3,78,1,3,5,1,2),_JnxSoamDmThresholdCfgEnable_Type())
jnxSoamDmThresholdCfgEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmThresholdCfgEnable.setStatus(_A)
class _JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type(Unsigned32):defaultValue=4294967295
_JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type.__name__=_C
_JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Object=MibTableColumn
jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold=_JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Object((1,3,6,1,4,1,2636,3,78,1,3,5,1,3),_JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type())
jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setUnits(_D)
class _JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type(Unsigned32):defaultValue=4294967295
_JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type.__name__=_C
_JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Object=MibTableColumn
jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold=_JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Object((1,3,6,1,4,1,2636,3,78,1,3,5,1,4),_JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type())
jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setUnits(_D)
_JnxSoamDmThresholdCfgRowStatus_Type=RowStatus
_JnxSoamDmThresholdCfgRowStatus_Object=MibTableColumn
jnxSoamDmThresholdCfgRowStatus=_JnxSoamDmThresholdCfgRowStatus_Object((1,3,6,1,4,1,2636,3,78,1,3,5,1,5),_JnxSoamDmThresholdCfgRowStatus_Type())
jnxSoamDmThresholdCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmThresholdCfgRowStatus.setStatus(_A)
_JnxSoamDmCfgMeasBinTable_Object=MibTable
jnxSoamDmCfgMeasBinTable=_JnxSoamDmCfgMeasBinTable_Object((1,3,6,1,4,1,2636,3,78,1,3,6))
if mibBuilder.loadTexts:jnxSoamDmCfgMeasBinTable.setStatus(_A)
_JnxSoamDmCfgMeasBinEntry_Object=MibTableRow
jnxSoamDmCfgMeasBinEntry=_JnxSoamDmCfgMeasBinEntry_Object((1,3,6,1,4,1,2636,3,78,1,3,6,1))
jnxSoamDmCfgMeasBinEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_N),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:jnxSoamDmCfgMeasBinEntry.setStatus(_A)
_JnxSoamDmCfgMeasBinType_Type=JnxSoamTcDelayMeasurementBinType
_JnxSoamDmCfgMeasBinType_Object=MibTableColumn
jnxSoamDmCfgMeasBinType=_JnxSoamDmCfgMeasBinType_Object((1,3,6,1,4,1,2636,3,78,1,3,6,1,1),_JnxSoamDmCfgMeasBinType_Type())
jnxSoamDmCfgMeasBinType.setMaxAccess(_e)
if mibBuilder.loadTexts:jnxSoamDmCfgMeasBinType.setStatus(_A)
_JnxSoamDmCfgMeasBinNumber_Type=Unsigned32
_JnxSoamDmCfgMeasBinNumber_Object=MibTableColumn
jnxSoamDmCfgMeasBinNumber=_JnxSoamDmCfgMeasBinNumber_Object((1,3,6,1,4,1,2636,3,78,1,3,6,1,2),_JnxSoamDmCfgMeasBinNumber_Type())
jnxSoamDmCfgMeasBinNumber.setMaxAccess(_e)
if mibBuilder.loadTexts:jnxSoamDmCfgMeasBinNumber.setStatus(_A)
_JnxSoamDmCfgMeasBinLowerBound_Type=Unsigned32
_JnxSoamDmCfgMeasBinLowerBound_Object=MibTableColumn
jnxSoamDmCfgMeasBinLowerBound=_JnxSoamDmCfgMeasBinLowerBound_Object((1,3,6,1,4,1,2636,3,78,1,3,6,1,3),_JnxSoamDmCfgMeasBinLowerBound_Type())
jnxSoamDmCfgMeasBinLowerBound.setMaxAccess('read-write')
if mibBuilder.loadTexts:jnxSoamDmCfgMeasBinLowerBound.setStatus(_A)
if mibBuilder.loadTexts:jnxSoamDmCfgMeasBinLowerBound.setUnits('microseconds (us)')
_JnxSoamDmCurrentStatsBinsTable_Object=MibTable
jnxSoamDmCurrentStatsBinsTable=_JnxSoamDmCurrentStatsBinsTable_Object((1,3,6,1,4,1,2636,3,78,1,3,7))
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsBinsTable.setStatus(_A)
_JnxSoamDmCurrentStatsBinsEntry_Object=MibTableRow
jnxSoamDmCurrentStatsBinsEntry=_JnxSoamDmCurrentStatsBinsEntry_Object((1,3,6,1,4,1,2636,3,78,1,3,7,1))
jnxSoamDmCurrentStatsBinsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_N),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsBinsEntry.setStatus(_A)
_JnxSoamDmCurrentStatsBinsCounter_Type=Gauge32
_JnxSoamDmCurrentStatsBinsCounter_Object=MibTableColumn
jnxSoamDmCurrentStatsBinsCounter=_JnxSoamDmCurrentStatsBinsCounter_Object((1,3,6,1,4,1,2636,3,78,1,3,7,1,1),_JnxSoamDmCurrentStatsBinsCounter_Type())
jnxSoamDmCurrentStatsBinsCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmCurrentStatsBinsCounter.setStatus(_A)
_JnxSoamDmHistoryStatsBinsTable_Object=MibTable
jnxSoamDmHistoryStatsBinsTable=_JnxSoamDmHistoryStatsBinsTable_Object((1,3,6,1,4,1,2636,3,78,1,3,8))
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsBinsTable.setStatus(_A)
_JnxSoamDmHistoryStatsBinsEntry_Object=MibTableRow
jnxSoamDmHistoryStatsBinsEntry=_JnxSoamDmHistoryStatsBinsEntry_Object((1,3,6,1,4,1,2636,3,78,1,3,8,1))
jnxSoamDmHistoryStatsBinsEntry.setIndexNames((0,_F,_J),(0,_F,_I),(0,_F,_K),(0,_E,_N),(0,_E,_f),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsBinsEntry.setStatus(_A)
_JnxSoamDmHistoryStatsBinsCounter_Type=Gauge32
_JnxSoamDmHistoryStatsBinsCounter_Object=MibTableColumn
jnxSoamDmHistoryStatsBinsCounter=_JnxSoamDmHistoryStatsBinsCounter_Object((1,3,6,1,4,1,2636,3,78,1,3,8,1,1),_JnxSoamDmHistoryStatsBinsCounter_Type())
jnxSoamDmHistoryStatsBinsCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxSoamDmHistoryStatsBinsCounter.setStatus(_A)
_JnxSoamPmNotificationCfg_ObjectIdentity=ObjectIdentity
jnxSoamPmNotificationCfg=_JnxSoamPmNotificationCfg_ObjectIdentity((1,3,6,1,4,1,2636,3,78,1,4))
_JnxSoamPmNotificationObj_ObjectIdentity=ObjectIdentity
jnxSoamPmNotificationObj=_JnxSoamPmNotificationObj_ObjectIdentity((1,3,6,1,4,1,2636,3,78,1,5))
_JnxSoamPmNotificationObjDateAndTime_Type=DateAndTime
_JnxSoamPmNotificationObjDateAndTime_Object=MibScalar
jnxSoamPmNotificationObjDateAndTime=_JnxSoamPmNotificationObjDateAndTime_Object((1,3,6,1,4,1,2636,3,78,1,5,1),_JnxSoamPmNotificationObjDateAndTime_Type())
jnxSoamPmNotificationObjDateAndTime.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjDateAndTime.setStatus(_A)
_JnxSoamPmNotificationObjThresholdId_Type=ObjectIdentifier
_JnxSoamPmNotificationObjThresholdId_Object=MibScalar
jnxSoamPmNotificationObjThresholdId=_JnxSoamPmNotificationObjThresholdId_Object((1,3,6,1,4,1,2636,3,78,1,5,2),_JnxSoamPmNotificationObjThresholdId_Type())
jnxSoamPmNotificationObjThresholdId.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjThresholdId.setStatus(_A)
_JnxSoamPmNotificationObjThresholdConfig_Type=Unsigned32
_JnxSoamPmNotificationObjThresholdConfig_Object=MibScalar
jnxSoamPmNotificationObjThresholdConfig=_JnxSoamPmNotificationObjThresholdConfig_Object((1,3,6,1,4,1,2636,3,78,1,5,3),_JnxSoamPmNotificationObjThresholdConfig_Type())
jnxSoamPmNotificationObjThresholdConfig.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjThresholdConfig.setStatus(_A)
_JnxSoamPmNotificationObjThresholdValue_Type=Unsigned32
_JnxSoamPmNotificationObjThresholdValue_Object=MibScalar
jnxSoamPmNotificationObjThresholdValue=_JnxSoamPmNotificationObjThresholdValue_Object((1,3,6,1,4,1,2636,3,78,1,5,4),_JnxSoamPmNotificationObjThresholdValue_Type())
jnxSoamPmNotificationObjThresholdValue.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjThresholdValue.setStatus(_A)
_JnxSoamPmNotificationObjSuspect_Type=TruthValue
_JnxSoamPmNotificationObjSuspect_Object=MibScalar
jnxSoamPmNotificationObjSuspect=_JnxSoamPmNotificationObjSuspect_Object((1,3,6,1,4,1,2636,3,78,1,5,5),_JnxSoamPmNotificationObjSuspect_Type())
jnxSoamPmNotificationObjSuspect.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjSuspect.setStatus(_A)
class _JnxSoamPmNotificationObjCrossingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3)))
_JnxSoamPmNotificationObjCrossingType_Type.__name__=_P
_JnxSoamPmNotificationObjCrossingType_Object=MibScalar
jnxSoamPmNotificationObjCrossingType=_JnxSoamPmNotificationObjCrossingType_Object((1,3,6,1,4,1,2636,3,78,1,5,6),_JnxSoamPmNotificationObjCrossingType_Type())
jnxSoamPmNotificationObjCrossingType.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjCrossingType.setStatus(_A)
_JnxSoamPmNotificationObjDestinationMep_Type=MacAddress
_JnxSoamPmNotificationObjDestinationMep_Object=MibScalar
jnxSoamPmNotificationObjDestinationMep=_JnxSoamPmNotificationObjDestinationMep_Object((1,3,6,1,4,1,2636,3,78,1,5,7),_JnxSoamPmNotificationObjDestinationMep_Type())
jnxSoamPmNotificationObjDestinationMep.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjDestinationMep.setStatus(_A)
_JnxSoamPmNotificationObjPriority_Type=MacAddress
_JnxSoamPmNotificationObjPriority_Object=MibScalar
jnxSoamPmNotificationObjPriority=_JnxSoamPmNotificationObjPriority_Object((1,3,6,1,4,1,2636,3,78,1,5,8),_JnxSoamPmNotificationObjPriority_Type())
jnxSoamPmNotificationObjPriority.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjPriority.setStatus(_A)
_JnxSoamPmNotificationTotalFlaps_Type=Unsigned32
_JnxSoamPmNotificationTotalFlaps_Object=MibScalar
jnxSoamPmNotificationTotalFlaps=_JnxSoamPmNotificationTotalFlaps_Object((1,3,6,1,4,1,2636,3,78,1,5,9),_JnxSoamPmNotificationTotalFlaps_Type())
jnxSoamPmNotificationTotalFlaps.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationTotalFlaps.setStatus(_A)
_JnxSoamPmNotificationAccTotalFlaps_Type=Unsigned32
_JnxSoamPmNotificationAccTotalFlaps_Object=MibScalar
jnxSoamPmNotificationAccTotalFlaps=_JnxSoamPmNotificationAccTotalFlaps_Object((1,3,6,1,4,1,2636,3,78,1,5,10),_JnxSoamPmNotificationAccTotalFlaps_Type())
jnxSoamPmNotificationAccTotalFlaps.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationAccTotalFlaps.setStatus(_A)
_JnxSoamPmNotificationObjThresholdLastValue_Type=Unsigned32
_JnxSoamPmNotificationObjThresholdLastValue_Object=MibScalar
jnxSoamPmNotificationObjThresholdLastValue=_JnxSoamPmNotificationObjThresholdLastValue_Object((1,3,6,1,4,1,2636,3,78,1,5,11),_JnxSoamPmNotificationObjThresholdLastValue_Type())
jnxSoamPmNotificationObjThresholdLastValue.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjThresholdLastValue.setStatus(_A)
class _JnxSoamPmNotificationObjCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3)))
_JnxSoamPmNotificationObjCurrentState_Type.__name__=_P
_JnxSoamPmNotificationObjCurrentState_Object=MibScalar
jnxSoamPmNotificationObjCurrentState=_JnxSoamPmNotificationObjCurrentState_Object((1,3,6,1,4,1,2636,3,78,1,5,12),_JnxSoamPmNotificationObjCurrentState_Type())
jnxSoamPmNotificationObjCurrentState.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjCurrentState.setStatus(_A)
_JnxSoamPmNotificationObjLastDateAndTime_Type=DateAndTime
_JnxSoamPmNotificationObjLastDateAndTime_Object=MibScalar
jnxSoamPmNotificationObjLastDateAndTime=_JnxSoamPmNotificationObjLastDateAndTime_Object((1,3,6,1,4,1,2636,3,78,1,5,13),_JnxSoamPmNotificationObjLastDateAndTime_Type())
jnxSoamPmNotificationObjLastDateAndTime.setMaxAccess(_M)
if mibBuilder.loadTexts:jnxSoamPmNotificationObjLastDateAndTime.setStatus(_A)
_JnxSoamPmMibConformance_ObjectIdentity=ObjectIdentity
jnxSoamPmMibConformance=_JnxSoamPmMibConformance_ObjectIdentity((1,3,6,1,4,1,2636,3,78,2))
dot1agCfmMepEntry.registerAugmentions((_E,_t))
jnxSoamPmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
jnxSoamLmSessionStartStopAlarm=NotificationType((1,3,6,1,4,1,2636,3,78,0,1))
jnxSoamLmSessionStartStopAlarm.setObjects(*((_E,_u),(_E,_a),(_E,_W)))
if mibBuilder.loadTexts:jnxSoamLmSessionStartStopAlarm.setStatus(_A)
jnxSoamDmSessionStartStopAlarm=NotificationType((1,3,6,1,4,1,2636,3,78,0,2))
jnxSoamDmSessionStartStopAlarm.setObjects(*((_E,_v),(_E,_a),(_E,_W)))
if mibBuilder.loadTexts:jnxSoamDmSessionStartStopAlarm.setStatus(_A)
jnxSoamPmThresholdCrossingAlarm=NotificationType((1,3,6,1,4,1,2636,3,78,0,3))
jnxSoamPmThresholdCrossingAlarm.setObjects(*((_E,_w),(_E,_g),(_E,_h),(_E,_x),(_E,_y),(_E,_a),(_E,_W)))
if mibBuilder.loadTexts:jnxSoamPmThresholdCrossingAlarm.setStatus(_A)
jnxSoamPmThresholdFlapAlarm=NotificationType((1,3,6,1,4,1,2636,3,78,0,4))
jnxSoamPmThresholdFlapAlarm.setObjects(*((_E,_g),(_E,_h),(_E,_z),(_E,_A0),(_E,_A1),(_E,_A2),(_E,_W)))
if mibBuilder.loadTexts:jnxSoamPmThresholdFlapAlarm.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_d:JnxSoamTcTestPatternType,_c:JnxSoamTcDataPatternType,_U:JnxSoamTcOperationTimeType,'JnxSoamTcAvailabilityType':JnxSoamTcAvailabilityType,'JnxSoamTcDelayMeasurementBinType':JnxSoamTcDelayMeasurementBinType,'jnxSoamPmMib':jnxSoamPmMib,'jnxSoamPmNotifications':jnxSoamPmNotifications,'jnxSoamLmSessionStartStopAlarm':jnxSoamLmSessionStartStopAlarm,'jnxSoamDmSessionStartStopAlarm':jnxSoamDmSessionStartStopAlarm,'jnxSoamPmThresholdCrossingAlarm':jnxSoamPmThresholdCrossingAlarm,'jnxSoamPmThresholdFlapAlarm':jnxSoamPmThresholdFlapAlarm,'jnxSoamPmMibObjects':jnxSoamPmMibObjects,'jnxSoamPmMep':jnxSoamPmMep,'jnxSoamPmMepTable':jnxSoamPmMepTable,_t:jnxSoamPmMepEntry,'jnxSoamPmMepOperNextIndex':jnxSoamPmMepOperNextIndex,'jnxSoamPmMepLmSingleEndedResponder':jnxSoamPmMepLmSingleEndedResponder,'jnxSoamPmMepSlmSingleEndedResponder':jnxSoamPmMepSlmSingleEndedResponder,'jnxSoamPmMepDmSingleEndedResponder':jnxSoamPmMepDmSingleEndedResponder,'jnxSoamPmLmObjects':jnxSoamPmLmObjects,'jnxSoamLmCfgTable':jnxSoamLmCfgTable,'jnxSoamLmCfgEntry':jnxSoamLmCfgEntry,_O:jnxSoamLmCfgIndex,'jnxSoamLmCfgType':jnxSoamLmCfgType,'jnxSoamLmCfgVersion':jnxSoamLmCfgVersion,'jnxSoamLmCfgEnabled':jnxSoamLmCfgEnabled,'jnxSoamLmCfgMeasurementEnable':jnxSoamLmCfgMeasurementEnable,'jnxSoamLmCfgMessagePeriod':jnxSoamLmCfgMessagePeriod,'jnxSoamLmCfgPriority':jnxSoamLmCfgPriority,'jnxSoamLmCfgFrameSize':jnxSoamLmCfgFrameSize,'jnxSoamLmCfgDataPattern':jnxSoamLmCfgDataPattern,'jnxSoamLmCfgTestTlvIncluded':jnxSoamLmCfgTestTlvIncluded,'jnxSoamLmCfgTestTlvPattern':jnxSoamLmCfgTestTlvPattern,'jnxSoamLmCfgNumIntervalsStored':jnxSoamLmCfgNumIntervalsStored,'jnxSoamLmCfgDestMepId':jnxSoamLmCfgDestMepId,'jnxSoamLmCfgDestIsMepId':jnxSoamLmCfgDestIsMepId,'jnxSoamLmCfgStartTimeType':jnxSoamLmCfgStartTimeType,'jnxSoamLmCfgFixedStartDateAndTime':jnxSoamLmCfgFixedStartDateAndTime,'jnxSoamLmCfgRelativeStartTime':jnxSoamLmCfgRelativeStartTime,'jnxSoamLmCfgRepetitionTime':jnxSoamLmCfgRepetitionTime,'jnxSoamLmCfgAlignMeasurementIntervals':jnxSoamLmCfgAlignMeasurementIntervals,'jnxSoamLmCfgAlignMeasurementOffset':jnxSoamLmCfgAlignMeasurementOffset,'jnxSoamLmCfgSessionType':jnxSoamLmCfgSessionType,_u:jnxSoamLmCfgSessionStatus,'jnxSoamLmCfgHistoryClear':jnxSoamLmCfgHistoryClear,'jnxSoamLmCfgRowStatus':jnxSoamLmCfgRowStatus,'jnxSoamLmCfgMeasurementInterval':jnxSoamLmCfgMeasurementInterval,'jnxSoamLmCfgDestMacAddress':jnxSoamLmCfgDestMacAddress,'jnxSoamLmCfgStopTimeType':jnxSoamLmCfgStopTimeType,'jnxSoamLmCfgFixedStopDateAndTime':jnxSoamLmCfgFixedStopDateAndTime,'jnxSoamLmCfgRelativeStopTime':jnxSoamLmCfgRelativeStopTime,'jnxSoamLmCfgAvailabilityMeasurementInterval':jnxSoamLmCfgAvailabilityMeasurementInterval,'jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus':jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus,'jnxSoamLmCfgAvailabilityFlrThreshold':jnxSoamLmCfgAvailabilityFlrThreshold,'jnxSoamLmCfgAvailabilityNumConsecutiveIntervals':jnxSoamLmCfgAvailabilityNumConsecutiveIntervals,'jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr':jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr,'jnxSoamLmMeasuredStatsTable':jnxSoamLmMeasuredStatsTable,'jnxSoamLmMeasuredStatsEntry':jnxSoamLmMeasuredStatsEntry,'jnxSoamLmMeasuredStatsForwardFlr':jnxSoamLmMeasuredStatsForwardFlr,'jnxSoamLmMeasuredStatsBackwardFlr':jnxSoamLmMeasuredStatsBackwardFlr,'jnxSoamLmMeasuredStatsAvailForwardStatus':jnxSoamLmMeasuredStatsAvailForwardStatus,'jnxSoamLmMeasuredStatsAvailBackwardStatus':jnxSoamLmMeasuredStatsAvailBackwardStatus,'jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime':jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime,'jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime':jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime,'jnxSoamLmCurrentStatsTable':jnxSoamLmCurrentStatsTable,'jnxSoamLmCurrentStatsEntry':jnxSoamLmCurrentStatsEntry,'jnxSoamLmCurrentStatsIndex':jnxSoamLmCurrentStatsIndex,'jnxSoamLmCurrentStatsStartTime':jnxSoamLmCurrentStatsStartTime,'jnxSoamLmCurrentStatsElapsedTime':jnxSoamLmCurrentStatsElapsedTime,'jnxSoamLmCurrentStatsSuspect':jnxSoamLmCurrentStatsSuspect,'jnxSoamLmCurrentStatsForwardTransmittedFrames':jnxSoamLmCurrentStatsForwardTransmittedFrames,'jnxSoamLmCurrentStatsForwardReceivedFrames':jnxSoamLmCurrentStatsForwardReceivedFrames,'jnxSoamLmCurrentStatsForwardMinFlr':jnxSoamLmCurrentStatsForwardMinFlr,'jnxSoamLmCurrentStatsForwardMaxFlr':jnxSoamLmCurrentStatsForwardMaxFlr,'jnxSoamLmCurrentStatsForwardAvgFlr':jnxSoamLmCurrentStatsForwardAvgFlr,'jnxSoamLmCurrentStatsBackwardTransmittedFrames':jnxSoamLmCurrentStatsBackwardTransmittedFrames,'jnxSoamLmCurrentStatsBackwardReceivedFrames':jnxSoamLmCurrentStatsBackwardReceivedFrames,'jnxSoamLmCurrentStatsBackwardMinFlr':jnxSoamLmCurrentStatsBackwardMinFlr,'jnxSoamLmCurrentStatsBackwardMaxFlr':jnxSoamLmCurrentStatsBackwardMaxFlr,'jnxSoamLmCurrentStatsBackwardAvgFlr':jnxSoamLmCurrentStatsBackwardAvgFlr,'jnxSoamLmCurrentStatsSoamPdusSent':jnxSoamLmCurrentStatsSoamPdusSent,'jnxSoamLmCurrentStatsSoamPdusReceived':jnxSoamLmCurrentStatsSoamPdusReceived,'jnxSoamLmHistoryStatsTable':jnxSoamLmHistoryStatsTable,'jnxSoamLmHistoryStatsEntry':jnxSoamLmHistoryStatsEntry,_m:jnxSoamLmHistoryStatsIndex,'jnxSoamLmHistoryStatsEndTime':jnxSoamLmHistoryStatsEndTime,'jnxSoamLmHistoryStatsElapsedTime':jnxSoamLmHistoryStatsElapsedTime,'jnxSoamLmHistoryStatsSuspect':jnxSoamLmHistoryStatsSuspect,'jnxSoamLmHistoryStatsForwardTransmittedFrames':jnxSoamLmHistoryStatsForwardTransmittedFrames,'jnxSoamLmHistoryStatsForwardReceivedFrames':jnxSoamLmHistoryStatsForwardReceivedFrames,'jnxSoamLmHistoryStatsForwardMinFlr':jnxSoamLmHistoryStatsForwardMinFlr,'jnxSoamLmHistoryStatsForwardMaxFlr':jnxSoamLmHistoryStatsForwardMaxFlr,'jnxSoamLmHistoryStatsForwardAvgFlr':jnxSoamLmHistoryStatsForwardAvgFlr,'jnxSoamLmHistoryStatsBackwardTransmittedFrames':jnxSoamLmHistoryStatsBackwardTransmittedFrames,'jnxSoamLmHistoryStatsBackwardReceivedFrames':jnxSoamLmHistoryStatsBackwardReceivedFrames,'jnxSoamLmHistoryStatsBackwardMinFlr':jnxSoamLmHistoryStatsBackwardMinFlr,'jnxSoamLmHistoryStatsBackwardMaxFlr':jnxSoamLmHistoryStatsBackwardMaxFlr,'jnxSoamLmHistoryStatsBackwardAvgFlr':jnxSoamLmHistoryStatsBackwardAvgFlr,'jnxSoamLmHistoryStatsSoamPdusSent':jnxSoamLmHistoryStatsSoamPdusSent,'jnxSoamLmHistoryStatsSoamPdusReceived':jnxSoamLmHistoryStatsSoamPdusReceived,'jnxSoamLmThresholdCfgTable':jnxSoamLmThresholdCfgTable,'jnxSoamLmThresholdCfgEntry':jnxSoamLmThresholdCfgEntry,_n:jnxSoamLmThresholdCfgIndex,'jnxSoamLmThresholdCfgEnable':jnxSoamLmThresholdCfgEnable,'jnxSoamLmThresholdCfgAvgFlrForwardThreshold':jnxSoamLmThresholdCfgAvgFlrForwardThreshold,'jnxSoamLmThresholdCfgAvgFlrBackwardThreshold':jnxSoamLmThresholdCfgAvgFlrBackwardThreshold,'jnxSoamLmThresholdCfgRowStatus':jnxSoamLmThresholdCfgRowStatus,'jnxSoamLmCurrentAvailStatsTable':jnxSoamLmCurrentAvailStatsTable,'jnxSoamLmCurrentAvailStatsEntry':jnxSoamLmCurrentAvailStatsEntry,'jnxSoamLmCurrentAvailStatsIndex':jnxSoamLmCurrentAvailStatsIndex,'jnxSoamLmCurrentAvailStatsStartTime':jnxSoamLmCurrentAvailStatsStartTime,'jnxSoamLmCurrentAvailStatsElapsedTime':jnxSoamLmCurrentAvailStatsElapsedTime,'jnxSoamLmCurrentAvailStatsSuspect':jnxSoamLmCurrentAvailStatsSuspect,'jnxSoamLmCurrentAvailStatsForwardHighLoss':jnxSoamLmCurrentAvailStatsForwardHighLoss,'jnxSoamLmCurrentAvailStatsBackwardHighLoss':jnxSoamLmCurrentAvailStatsBackwardHighLoss,'jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss':jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss,'jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss':jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss,'jnxSoamLmCurrentAvailStatsForwardAvailable':jnxSoamLmCurrentAvailStatsForwardAvailable,'jnxSoamLmCurrentAvailStatsBackwardAvailable':jnxSoamLmCurrentAvailStatsBackwardAvailable,'jnxSoamLmCurrentAvailStatsForwardUnavailable':jnxSoamLmCurrentAvailStatsForwardUnavailable,'jnxSoamLmCurrentAvailStatsBackwardUnavailable':jnxSoamLmCurrentAvailStatsBackwardUnavailable,'jnxSoamLmCurrentAvailStatsForwardMinFlr':jnxSoamLmCurrentAvailStatsForwardMinFlr,'jnxSoamLmCurrentAvailStatsForwardMaxFlr':jnxSoamLmCurrentAvailStatsForwardMaxFlr,'jnxSoamLmCurrentAvailStatsForwardAvgFlr':jnxSoamLmCurrentAvailStatsForwardAvgFlr,'jnxSoamLmCurrentAvailStatsBackwardMinFlr':jnxSoamLmCurrentAvailStatsBackwardMinFlr,'jnxSoamLmCurrentAvailStatsBackwardMaxFlr':jnxSoamLmCurrentAvailStatsBackwardMaxFlr,'jnxSoamLmCurrentAvailStatsBackwardAvgFlr':jnxSoamLmCurrentAvailStatsBackwardAvgFlr,'jnxSoamLmHistoryAvailStatsTable':jnxSoamLmHistoryAvailStatsTable,'jnxSoamLmHistoryAvailStatsEntry':jnxSoamLmHistoryAvailStatsEntry,_o:jnxSoamLmHistoryAvailStatsIndex,'jnxSoamLmHistoryAvailStatsEndTime':jnxSoamLmHistoryAvailStatsEndTime,'jnxSoamLmHistoryAvailStatsElapsedTime':jnxSoamLmHistoryAvailStatsElapsedTime,'jnxSoamLmHistoryAvailStatsSuspect':jnxSoamLmHistoryAvailStatsSuspect,'jnxSoamLmHistoryAvailStatsForwardHighLoss':jnxSoamLmHistoryAvailStatsForwardHighLoss,'jnxSoamLmHistoryAvailStatsBackwardHighLoss':jnxSoamLmHistoryAvailStatsBackwardHighLoss,'jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss':jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss,'jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss':jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss,'jnxSoamLmHistoryAvailStatsForwardAvailable':jnxSoamLmHistoryAvailStatsForwardAvailable,'jnxSoamLmHistoryAvailStatsBackwardAvailable':jnxSoamLmHistoryAvailStatsBackwardAvailable,'jnxSoamLmHistoryAvailStatsForwardUnavailable':jnxSoamLmHistoryAvailStatsForwardUnavailable,'jnxSoamLmHistoryAvailStatsBackwardUnavailable':jnxSoamLmHistoryAvailStatsBackwardUnavailable,'jnxSoamLmHistoryAvailStatsForwardMinFlr':jnxSoamLmHistoryAvailStatsForwardMinFlr,'jnxSoamLmHistoryAvailStatsForwardMaxFlr':jnxSoamLmHistoryAvailStatsForwardMaxFlr,'jnxSoamLmHistoryAvailStatsForwardAvgFlr':jnxSoamLmHistoryAvailStatsForwardAvgFlr,'jnxSoamLmHistoryAvailStatsBackwardMinFlr':jnxSoamLmHistoryAvailStatsBackwardMinFlr,'jnxSoamLmHistoryAvailStatsBackwardMaxFlr':jnxSoamLmHistoryAvailStatsBackwardMaxFlr,'jnxSoamLmHistoryAvailStatsBackwardAvgFlr':jnxSoamLmHistoryAvailStatsBackwardAvgFlr,'jnxSoamPmDmObjects':jnxSoamPmDmObjects,'jnxSoamDmCfgTable':jnxSoamDmCfgTable,'jnxSoamDmCfgEntry':jnxSoamDmCfgEntry,_N:jnxSoamDmCfgIndex,'jnxSoamDmCfgType':jnxSoamDmCfgType,'jnxSoamDmCfgVersion':jnxSoamDmCfgVersion,'jnxSoamDmCfgEnabled':jnxSoamDmCfgEnabled,'jnxSoamDmCfgMeasurementEnable':jnxSoamDmCfgMeasurementEnable,'jnxSoamDmCfgMessagePeriod':jnxSoamDmCfgMessagePeriod,'jnxSoamDmCfgPriority':jnxSoamDmCfgPriority,'jnxSoamDmCfgFrameSize':jnxSoamDmCfgFrameSize,'jnxSoamDmCfgDataPattern':jnxSoamDmCfgDataPattern,'jnxSoamDmCfgTestTlvIncluded':jnxSoamDmCfgTestTlvIncluded,'jnxSoamDmCfgTestTlvPattern':jnxSoamDmCfgTestTlvPattern,'jnxSoamDmCfgNumIntervalsStored':jnxSoamDmCfgNumIntervalsStored,'jnxSoamDmCfgDestMepId':jnxSoamDmCfgDestMepId,'jnxSoamDmCfgDestIsMepId':jnxSoamDmCfgDestIsMepId,'jnxSoamDmCfgStartTimeType':jnxSoamDmCfgStartTimeType,'jnxSoamDmCfgRepetitionTime':jnxSoamDmCfgRepetitionTime,'jnxSoamDmCfgAlignMeasurementIntervals':jnxSoamDmCfgAlignMeasurementIntervals,'jnxSoamDmCfgInterFrameDelayVariationSelectionOffset':jnxSoamDmCfgInterFrameDelayVariationSelectionOffset,'jnxSoamDmCfgSessionType':jnxSoamDmCfgSessionType,_v:jnxSoamDmCfgSessionStatus,'jnxSoamDmCfgHistoryClear':jnxSoamDmCfgHistoryClear,'jnxSoamDmCfgRowStatus':jnxSoamDmCfgRowStatus,'jnxSoamDmCfgMeasurementInterval':jnxSoamDmCfgMeasurementInterval,'jnxSoamDmCfgDestMacAddress':jnxSoamDmCfgDestMacAddress,'jnxSoamDmCfgSourceMacAddress':jnxSoamDmCfgSourceMacAddress,'jnxSoamDmCfgFixedStartDateAndTime':jnxSoamDmCfgFixedStartDateAndTime,'jnxSoamDmCfgRelativeStartTime':jnxSoamDmCfgRelativeStartTime,'jnxSoamDmCfgStopTimeType':jnxSoamDmCfgStopTimeType,'jnxSoamDmCfgFixedStopDateAndTime':jnxSoamDmCfgFixedStopDateAndTime,'jnxSoamDmCfgRelativeStopTime':jnxSoamDmCfgRelativeStopTime,'jnxSoamDmCfgAlignMeasurementOffset':jnxSoamDmCfgAlignMeasurementOffset,'jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval':jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval,'jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval':jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval,'jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval':jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval,'jnxSoamDmMeasuredStatsTable':jnxSoamDmMeasuredStatsTable,'jnxSoamDmMeasuredStatsEntry':jnxSoamDmMeasuredStatsEntry,'jnxSoamDmMeasuredStatsFrameDelayTwoWay':jnxSoamDmMeasuredStatsFrameDelayTwoWay,'jnxSoamDmMeasuredStatsFrameDelayForward':jnxSoamDmMeasuredStatsFrameDelayForward,'jnxSoamDmMeasuredStatsFrameDelayBackward':jnxSoamDmMeasuredStatsFrameDelayBackward,'jnxSoamDmMeasuredStatsIfdvTwoWay':jnxSoamDmMeasuredStatsIfdvTwoWay,'jnxSoamDmMeasuredStatsIfdvForward':jnxSoamDmMeasuredStatsIfdvForward,'jnxSoamDmMeasuredStatsIfdvBackward':jnxSoamDmMeasuredStatsIfdvBackward,'jnxSoamDmCurrentStatsTable':jnxSoamDmCurrentStatsTable,'jnxSoamDmCurrentStatsEntry':jnxSoamDmCurrentStatsEntry,'jnxSoamDmCurrentStatsIndex':jnxSoamDmCurrentStatsIndex,'jnxSoamDmCurrentStatsStartTime':jnxSoamDmCurrentStatsStartTime,'jnxSoamDmCurrentStatsElapsedTime':jnxSoamDmCurrentStatsElapsedTime,'jnxSoamDmCurrentStatsSuspect':jnxSoamDmCurrentStatsSuspect,'jnxSoamDmCurrentStatsFrameDelayTwoWayMin':jnxSoamDmCurrentStatsFrameDelayTwoWayMin,'jnxSoamDmCurrentStatsFrameDelayTwoWayMax':jnxSoamDmCurrentStatsFrameDelayTwoWayMax,'jnxSoamDmCurrentStatsFrameDelayTwoWayAvg':jnxSoamDmCurrentStatsFrameDelayTwoWayAvg,'jnxSoamDmCurrentStatsFrameDelayForwardMin':jnxSoamDmCurrentStatsFrameDelayForwardMin,'jnxSoamDmCurrentStatsFrameDelayForwardMax':jnxSoamDmCurrentStatsFrameDelayForwardMax,'jnxSoamDmCurrentStatsFrameDelayForwardAvg':jnxSoamDmCurrentStatsFrameDelayForwardAvg,'jnxSoamDmCurrentStatsFrameDelayBackwardMin':jnxSoamDmCurrentStatsFrameDelayBackwardMin,'jnxSoamDmCurrentStatsFrameDelayBackwardMax':jnxSoamDmCurrentStatsFrameDelayBackwardMax,'jnxSoamDmCurrentStatsFrameDelayBackwardAvg':jnxSoamDmCurrentStatsFrameDelayBackwardAvg,'jnxSoamDmCurrentStatsIfdvForwardMin':jnxSoamDmCurrentStatsIfdvForwardMin,'jnxSoamDmCurrentStatsIfdvForwardMax':jnxSoamDmCurrentStatsIfdvForwardMax,'jnxSoamDmCurrentStatsIfdvForwardAvg':jnxSoamDmCurrentStatsIfdvForwardAvg,'jnxSoamDmCurrentStatsIfdvBackwardMin':jnxSoamDmCurrentStatsIfdvBackwardMin,'jnxSoamDmCurrentStatsIfdvBackwardMax':jnxSoamDmCurrentStatsIfdvBackwardMax,'jnxSoamDmCurrentStatsIfdvBackwardAvg':jnxSoamDmCurrentStatsIfdvBackwardAvg,'jnxSoamDmCurrentStatsIfdvTwoWayMin':jnxSoamDmCurrentStatsIfdvTwoWayMin,'jnxSoamDmCurrentStatsIfdvTwoWayMax':jnxSoamDmCurrentStatsIfdvTwoWayMax,'jnxSoamDmCurrentStatsIfdvTwoWayAvg':jnxSoamDmCurrentStatsIfdvTwoWayAvg,'jnxSoamDmCurrentStatsSoamPdusSent':jnxSoamDmCurrentStatsSoamPdusSent,'jnxSoamDmCurrentStatsSoamPdusReceived':jnxSoamDmCurrentStatsSoamPdusReceived,'jnxSoamDmCurrentStatsFrameDelayRangeForwardMax':jnxSoamDmCurrentStatsFrameDelayRangeForwardMax,'jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg':jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg,'jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax':jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax,'jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg':jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg,'jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax':jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax,'jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg':jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg,'jnxSoamDmHistoryStatsTable':jnxSoamDmHistoryStatsTable,'jnxSoamDmHistoryStatsEntry':jnxSoamDmHistoryStatsEntry,_f:jnxSoamDmHistoryStatsIndex,'jnxSoamDmHistoryStatsEndTime':jnxSoamDmHistoryStatsEndTime,'jnxSoamDmHistoryStatsElapsedTime':jnxSoamDmHistoryStatsElapsedTime,'jnxSoamDmHistoryStatsSuspect':jnxSoamDmHistoryStatsSuspect,'jnxSoamDmHistoryStatsFrameDelayTwoWayMin':jnxSoamDmHistoryStatsFrameDelayTwoWayMin,'jnxSoamDmHistoryStatsFrameDelayTwoWayMax':jnxSoamDmHistoryStatsFrameDelayTwoWayMax,'jnxSoamDmHistoryStatsFrameDelayTwoWayAvg':jnxSoamDmHistoryStatsFrameDelayTwoWayAvg,'jnxSoamDmHistoryStatsFrameDelayForwardMin':jnxSoamDmHistoryStatsFrameDelayForwardMin,'jnxSoamDmHistoryStatsFrameDelayForwardMax':jnxSoamDmHistoryStatsFrameDelayForwardMax,'jnxSoamDmHistoryStatsFrameDelayForwardAvg':jnxSoamDmHistoryStatsFrameDelayForwardAvg,'jnxSoamDmHistoryStatsFrameDelayBackwardMin':jnxSoamDmHistoryStatsFrameDelayBackwardMin,'jnxSoamDmHistoryStatsFrameDelayBackwardMax':jnxSoamDmHistoryStatsFrameDelayBackwardMax,'jnxSoamDmHistoryStatsFrameDelayBackwardAvg':jnxSoamDmHistoryStatsFrameDelayBackwardAvg,'jnxSoamDmHistoryStatsIfdvForwardMin':jnxSoamDmHistoryStatsIfdvForwardMin,'jnxSoamDmHistoryStatsIfdvForwardMax':jnxSoamDmHistoryStatsIfdvForwardMax,'jnxSoamDmHistoryStatsIfdvForwardAvg':jnxSoamDmHistoryStatsIfdvForwardAvg,'jnxSoamDmHistoryStatsIfdvBackwardMin':jnxSoamDmHistoryStatsIfdvBackwardMin,'jnxSoamDmHistoryStatsIfdvBackwardMax':jnxSoamDmHistoryStatsIfdvBackwardMax,'jnxSoamDmHistoryStatsIfdvBackwardAvg':jnxSoamDmHistoryStatsIfdvBackwardAvg,'jnxSoamDmHistoryStatsIfdvTwoWayMin':jnxSoamDmHistoryStatsIfdvTwoWayMin,'jnxSoamDmHistoryStatsIfdvTwoWayMax':jnxSoamDmHistoryStatsIfdvTwoWayMax,'jnxSoamDmHistoryStatsIfdvTwoWayAvg':jnxSoamDmHistoryStatsIfdvTwoWayAvg,'jnxSoamDmHistoryStatsSoamPdusSent':jnxSoamDmHistoryStatsSoamPdusSent,'jnxSoamDmHistoryStatsSoamPdusReceived':jnxSoamDmHistoryStatsSoamPdusReceived,'jnxSoamDmHistoryStatsFrameDelayRangeForwardMax':jnxSoamDmHistoryStatsFrameDelayRangeForwardMax,'jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg':jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg,'jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax':jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax,'jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg':jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg,'jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax':jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax,'jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg':jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg,'jnxSoamDmThresholdCfgTable':jnxSoamDmThresholdCfgTable,'jnxSoamDmThresholdCfgEntry':jnxSoamDmThresholdCfgEntry,_p:jnxSoamDmThresholdCfgIndex,'jnxSoamDmThresholdCfgEnable':jnxSoamDmThresholdCfgEnable,'jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold':jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold,'jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold':jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold,'jnxSoamDmThresholdCfgRowStatus':jnxSoamDmThresholdCfgRowStatus,'jnxSoamDmCfgMeasBinTable':jnxSoamDmCfgMeasBinTable,'jnxSoamDmCfgMeasBinEntry':jnxSoamDmCfgMeasBinEntry,_Y:jnxSoamDmCfgMeasBinType,_Z:jnxSoamDmCfgMeasBinNumber,'jnxSoamDmCfgMeasBinLowerBound':jnxSoamDmCfgMeasBinLowerBound,'jnxSoamDmCurrentStatsBinsTable':jnxSoamDmCurrentStatsBinsTable,'jnxSoamDmCurrentStatsBinsEntry':jnxSoamDmCurrentStatsBinsEntry,'jnxSoamDmCurrentStatsBinsCounter':jnxSoamDmCurrentStatsBinsCounter,'jnxSoamDmHistoryStatsBinsTable':jnxSoamDmHistoryStatsBinsTable,'jnxSoamDmHistoryStatsBinsEntry':jnxSoamDmHistoryStatsBinsEntry,'jnxSoamDmHistoryStatsBinsCounter':jnxSoamDmHistoryStatsBinsCounter,'jnxSoamPmNotificationCfg':jnxSoamPmNotificationCfg,'jnxSoamPmNotificationObj':jnxSoamPmNotificationObj,_a:jnxSoamPmNotificationObjDateAndTime,_g:jnxSoamPmNotificationObjThresholdId,_h:jnxSoamPmNotificationObjThresholdConfig,_x:jnxSoamPmNotificationObjThresholdValue,_y:jnxSoamPmNotificationObjSuspect,_w:jnxSoamPmNotificationObjCrossingType,_W:jnxSoamPmNotificationObjDestinationMep,'jnxSoamPmNotificationObjPriority':jnxSoamPmNotificationObjPriority,_A0:jnxSoamPmNotificationTotalFlaps,_A1:jnxSoamPmNotificationAccTotalFlaps,_z:jnxSoamPmNotificationObjThresholdLastValue,_A2:jnxSoamPmNotificationObjCurrentState,'jnxSoamPmNotificationObjLastDateAndTime':jnxSoamPmNotificationObjLastDateAndTime,'jnxSoamPmMibConformance':jnxSoamPmMibConformance})