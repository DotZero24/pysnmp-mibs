_Av='cds1NEOptionalNotificationsGroup'
_Au='ciscoDs1CallGroup'
_At='cds1StatThresholdAlarm'
_As='cds1CallTrunkConditionEnable'
_Ar='cds1RepetitionResult'
_Aq='cds1RepetitionOwner'
_Ap='cds1Repetition'
_Ao='cds1FECounts'
_An='cds1RAICounts'
_Am='cds1OOFCounts'
_Al='cds1LOSCounts'
_Ak='cds1Previous24HrLSESs'
_Aj='cds1Previous24HrLCVs'
_Ai='cds1Previous24HrDMs'
_Ah='cds1Previous24HrBESs'
_Ag='cds1Previous24HrLESs'
_Af='cds1Previous24HrPCVs'
_Ae='cds1Previous24HrCSSs'
_Ad='cds1Previous24HrUASs'
_Ac='cds1Previous24HrSEFSs'
_Ab='cds1Previous24HrSESs'
_Aa='cds1Previous24HrESs'
_AZ='cds1Current24HrLCVs'
_AY='cds1Current24HrDMs'
_AX='cds1Current24HrBESs'
_AW='cds1Current24HrLESs'
_AV='cds1Current24HrPCVs'
_AU='cds1Current24HrCSSs'
_AT='cds1Current24HrUASs'
_AS='cds1Current24HrSEFSs'
_AR='cds1Current24HrSESs'
_AQ='cds1Current24HrESs'
_AP='cds1AlarmThresholdActiveGroup'
_AO='cds1AlarmThreshold'
_AN='cds1AlarmDownCount'
_AM='cds1AlarmUpCount'
_AL='cds1StatisticalAlarmSeverity'
_AK='cds1FarEndTotalLOFCs'
_AJ='cds1FarEndIntervalLOFCs'
_AI='cds1FarEndCurrentLOFCs'
_AH='cds1TotalPSASs'
_AG='cds1TotalLSESs'
_AF='cds1IntervalPSASs'
_AE='cds1IntervalLSESs'
_AD='cds1CurrentPSASs'
_AC='cds1CurrentLSESs'
_AB='cds1LoopbackCodeDetection'
_AA='cds1LineType'
_A9='cds1FarEndTotalEntry'
_A8='cds1FarEndIntervalEntry'
_A7='cds1FarEndCurrentEntry'
_A6='cds1TotalEntry'
_A5='cds1IntervalEntry'
_A4='cds1CurrentEntry'
_A3='cds1AlarmConfigEntry'
_A2='cds1CallConfigEntry'
_A1='cds1ConfigEntry'
_A0='cds1AlarmThresholdGroupIndex'
_z='ConfigIterator'
_y='ciscoDs1Alarm24HrThreshGroupRev1'
_x='ciscoDs1Alarm15MinThreshGroupRev1'
_w='ciscoDs1AlarmThreshGroup'
_v='ciscoDs1Alarm24HrThreshGroup'
_u='ciscoDs1Alarm15MinThreshGroup'
_t='cds1Current24HrPSASsThreshold'
_s='cds1Current24HrESsThreshold'
_r='cds1Current24HrDMsThreshold'
_q='cds1Current24HrCSSsThreshold'
_p='cds1Current24HrBESsThreshold'
_o='cds1Current24HrSESsThreshold'
_n='cds1Current24HrLSESsThreshold'
_m='cds1Current24HrUASsThreshold'
_l='cds1Current24HrSEFSsThreshold'
_k='cds1Current24HrPCVsThreshold'
_j='cds1Current24HrLESsThreshold'
_i='cds1Current24HrLCVsThreshold'
_h='cds1Current15MinPSASsThreshold'
_g='cds1Current15MinCSSsThreshold'
_f='cds1Current15MinESsThreshold'
_e='cds1Current15MinDMsThreshold'
_d='cds1Current15MinBESsThreshold'
_c='cds1Current15MinSESsThreshold'
_b='cds1Current15MinLSESsThreshold'
_a='cds1Current15MinUASsThreshold'
_Z='cds1Current15MinSEFSsThreshold'
_Y='cds1Current15MinPCVsThreshold'
_X='cds1Current15MinLESsThreshold'
_W='cds1Current15MinLCVsThreshold'
_V='cds1StatisticalAlarmState'
_U='TruthValue'
_T='ciscoDs1BulkConfGroup'
_S='cds1AlarmThresholdGroupRowStatus'
_R='ifIndex'
_Q='IF-MIB'
_P='ciscoDs1FarEndStatsMIBGroup'
_O='ciscoDs1StatsMIBGroup'
_N='ciscoDs1TotalMIBGroup'
_M='ciscoDs1IntervalMIBGroup'
_L='ciscoDs1Previous24HrMIBGroup'
_K='ciscoDs1Current24HrMIBGroup'
_J='ciscoDs1AlarmConfigGroup'
_I='ciscoDs1CurrentMIBGroup'
_H='ciscoDs1ConfMIBGroup'
_G='deprecated'
_F='read-write'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-DS1-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
BulkConfigResult,ConfigIterator=mibBuilder.importSymbols('CISCO-TC','BulkConfigResult',_z)
dsx1ConfigEntry,dsx1CurrentEntry,dsx1FarEndCurrentEntry,dsx1FarEndIntervalEntry,dsx1FarEndTotalEntry,dsx1IntervalEntry,dsx1TotalEntry=mibBuilder.importSymbols('DS1-MIB','dsx1ConfigEntry','dsx1CurrentEntry','dsx1FarEndCurrentEntry','dsx1FarEndIntervalEntry','dsx1FarEndTotalEntry','dsx1IntervalEntry','dsx1TotalEntry')
ifIndex,=mibBuilder.importSymbols(_Q,_R)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
OwnerString,=mibBuilder.importSymbols('RMON-MIB','OwnerString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_U)
ciscoDs1ExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,229))
if mibBuilder.loadTexts:ciscoDs1ExtMIB.setRevisions(('2003-02-25 00:00','2002-12-30 00:00','2001-09-13 00:00'))
class PerfCurrent24HourCount(TextualConvention,Gauge32):status=_B
class PerfPrevious24HourCount(TextualConvention,Gauge32):status=_B
_CiscoDs1MIBObjects_ObjectIdentity=ObjectIdentity
ciscoDs1MIBObjects=_CiscoDs1MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,229,1))
_Cds1Config_ObjectIdentity=ObjectIdentity
cds1Config=_Cds1Config_ObjectIdentity((1,3,6,1,4,1,9,9,229,1,1))
_Cds1ConfigTable_Object=MibTable
cds1ConfigTable=_Cds1ConfigTable_Object((1,3,6,1,4,1,9,9,229,1,1,1))
if mibBuilder.loadTexts:cds1ConfigTable.setStatus(_B)
_Cds1ConfigEntry_Object=MibTableRow
cds1ConfigEntry=_Cds1ConfigEntry_Object((1,3,6,1,4,1,9,9,229,1,1,1,1))
if mibBuilder.loadTexts:cds1ConfigEntry.setStatus(_B)
class _Cds1LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,20,21)));namedValues=NamedValues(*(('other',1),('dsx1ESF',2),('dsx1D4',3),('dsx1E1',4),('dsx1E1CRC',5),('dsx1E1MF',6),('dsx1E1CRCMF',7),('dsx1Unframed',8),('dsx1E1Unframed',9),('dsx1DS2M12',10),('dsx2E2',11),('dsx1E1Q50',20),('dsx1E1Q50CRC',21)))
_Cds1LineType_Type.__name__=_D
_Cds1LineType_Object=MibTableColumn
cds1LineType=_Cds1LineType_Object((1,3,6,1,4,1,9,9,229,1,1,1,1,1),_Cds1LineType_Type())
cds1LineType.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1LineType.setStatus(_B)
class _Cds1LoopbackCodeDetection_Type(TruthValue):defaultValue=2
_Cds1LoopbackCodeDetection_Type.__name__=_U
_Cds1LoopbackCodeDetection_Object=MibTableColumn
cds1LoopbackCodeDetection=_Cds1LoopbackCodeDetection_Object((1,3,6,1,4,1,9,9,229,1,1,1,1,2),_Cds1LoopbackCodeDetection_Type())
cds1LoopbackCodeDetection.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1LoopbackCodeDetection.setStatus(_B)
class _Cds1Repetition_Type(ConfigIterator):defaultValue=1
_Cds1Repetition_Type.__name__=_z
_Cds1Repetition_Object=MibTableColumn
cds1Repetition=_Cds1Repetition_Object((1,3,6,1,4,1,9,9,229,1,1,1,1,3),_Cds1Repetition_Type())
cds1Repetition.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1Repetition.setStatus(_B)
_Cds1RepetitionOwner_Type=OwnerString
_Cds1RepetitionOwner_Object=MibTableColumn
cds1RepetitionOwner=_Cds1RepetitionOwner_Object((1,3,6,1,4,1,9,9,229,1,1,1,1,4),_Cds1RepetitionOwner_Type())
cds1RepetitionOwner.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1RepetitionOwner.setStatus(_B)
_Cds1RepetitionResult_Type=BulkConfigResult
_Cds1RepetitionResult_Object=MibTableColumn
cds1RepetitionResult=_Cds1RepetitionResult_Object((1,3,6,1,4,1,9,9,229,1,1,1,1,5),_Cds1RepetitionResult_Type())
cds1RepetitionResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1RepetitionResult.setStatus(_B)
_Cds1CallConfigTable_Object=MibTable
cds1CallConfigTable=_Cds1CallConfigTable_Object((1,3,6,1,4,1,9,9,229,1,1,2))
if mibBuilder.loadTexts:cds1CallConfigTable.setStatus(_B)
_Cds1CallConfigEntry_Object=MibTableRow
cds1CallConfigEntry=_Cds1CallConfigEntry_Object((1,3,6,1,4,1,9,9,229,1,1,2,1))
if mibBuilder.loadTexts:cds1CallConfigEntry.setStatus(_B)
class _Cds1CallTrunkConditionEnable_Type(TruthValue):defaultValue=2
_Cds1CallTrunkConditionEnable_Type.__name__=_U
_Cds1CallTrunkConditionEnable_Object=MibTableColumn
cds1CallTrunkConditionEnable=_Cds1CallTrunkConditionEnable_Object((1,3,6,1,4,1,9,9,229,1,1,2,1,1),_Cds1CallTrunkConditionEnable_Type())
cds1CallTrunkConditionEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1CallTrunkConditionEnable.setStatus(_B)
_Cds1Alarm_ObjectIdentity=ObjectIdentity
cds1Alarm=_Cds1Alarm_ObjectIdentity((1,3,6,1,4,1,9,9,229,1,2))
_Cds1AlarmThresholdGroupTable_Object=MibTable
cds1AlarmThresholdGroupTable=_Cds1AlarmThresholdGroupTable_Object((1,3,6,1,4,1,9,9,229,1,2,1))
if mibBuilder.loadTexts:cds1AlarmThresholdGroupTable.setStatus(_B)
_Cds1AlarmThresholdGroupEntry_Object=MibTableRow
cds1AlarmThresholdGroupEntry=_Cds1AlarmThresholdGroupEntry_Object((1,3,6,1,4,1,9,9,229,1,2,1,1))
cds1AlarmThresholdGroupEntry.setIndexNames((0,_A,_A0))
if mibBuilder.loadTexts:cds1AlarmThresholdGroupEntry.setStatus(_B)
class _Cds1AlarmThresholdGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Cds1AlarmThresholdGroupIndex_Type.__name__=_D
_Cds1AlarmThresholdGroupIndex_Object=MibTableColumn
cds1AlarmThresholdGroupIndex=_Cds1AlarmThresholdGroupIndex_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,1),_Cds1AlarmThresholdGroupIndex_Type())
cds1AlarmThresholdGroupIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cds1AlarmThresholdGroupIndex.setStatus(_B)
class _Cds1Current15MinBESsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinBESsThreshold_Type.__name__=_D
_Cds1Current15MinBESsThreshold_Object=MibTableColumn
cds1Current15MinBESsThreshold=_Cds1Current15MinBESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,2),_Cds1Current15MinBESsThreshold_Type())
cds1Current15MinBESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinBESsThreshold.setStatus(_B)
class _Cds1Current24HrBESsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrBESsThreshold_Type.__name__=_D
_Cds1Current24HrBESsThreshold_Object=MibTableColumn
cds1Current24HrBESsThreshold=_Cds1Current24HrBESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,3),_Cds1Current24HrBESsThreshold_Type())
cds1Current24HrBESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrBESsThreshold.setStatus(_B)
class _Cds1Current15MinCSSsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinCSSsThreshold_Type.__name__=_D
_Cds1Current15MinCSSsThreshold_Object=MibTableColumn
cds1Current15MinCSSsThreshold=_Cds1Current15MinCSSsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,4),_Cds1Current15MinCSSsThreshold_Type())
cds1Current15MinCSSsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinCSSsThreshold.setStatus(_B)
class _Cds1Current24HrCSSsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrCSSsThreshold_Type.__name__=_D
_Cds1Current24HrCSSsThreshold_Object=MibTableColumn
cds1Current24HrCSSsThreshold=_Cds1Current24HrCSSsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,5),_Cds1Current24HrCSSsThreshold_Type())
cds1Current24HrCSSsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrCSSsThreshold.setStatus(_B)
class _Cds1Current15MinDMsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinDMsThreshold_Type.__name__=_D
_Cds1Current15MinDMsThreshold_Object=MibTableColumn
cds1Current15MinDMsThreshold=_Cds1Current15MinDMsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,6),_Cds1Current15MinDMsThreshold_Type())
cds1Current15MinDMsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinDMsThreshold.setStatus(_B)
class _Cds1Current24HrDMsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrDMsThreshold_Type.__name__=_D
_Cds1Current24HrDMsThreshold_Object=MibTableColumn
cds1Current24HrDMsThreshold=_Cds1Current24HrDMsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,7),_Cds1Current24HrDMsThreshold_Type())
cds1Current24HrDMsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrDMsThreshold.setStatus(_B)
class _Cds1Current15MinESsThreshold_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinESsThreshold_Type.__name__=_D
_Cds1Current15MinESsThreshold_Object=MibTableColumn
cds1Current15MinESsThreshold=_Cds1Current15MinESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,8),_Cds1Current15MinESsThreshold_Type())
cds1Current15MinESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinESsThreshold.setStatus(_B)
class _Cds1Current24HrESsThreshold_Type(Integer32):defaultValue=121;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrESsThreshold_Type.__name__=_D
_Cds1Current24HrESsThreshold_Object=MibTableColumn
cds1Current24HrESsThreshold=_Cds1Current24HrESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,9),_Cds1Current24HrESsThreshold_Type())
cds1Current24HrESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrESsThreshold.setStatus(_B)
class _Cds1Current15MinLCVsThreshold_Type(Integer32):defaultValue=14;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinLCVsThreshold_Type.__name__=_D
_Cds1Current15MinLCVsThreshold_Object=MibTableColumn
cds1Current15MinLCVsThreshold=_Cds1Current15MinLCVsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,10),_Cds1Current15MinLCVsThreshold_Type())
cds1Current15MinLCVsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinLCVsThreshold.setStatus(_B)
class _Cds1Current24HrLCVsThreshold_Type(Integer32):defaultValue=134;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrLCVsThreshold_Type.__name__=_D
_Cds1Current24HrLCVsThreshold_Object=MibTableColumn
cds1Current24HrLCVsThreshold=_Cds1Current24HrLCVsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,11),_Cds1Current24HrLCVsThreshold_Type())
cds1Current24HrLCVsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrLCVsThreshold.setStatus(_B)
class _Cds1Current15MinLESsThreshold_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinLESsThreshold_Type.__name__=_D
_Cds1Current15MinLESsThreshold_Object=MibTableColumn
cds1Current15MinLESsThreshold=_Cds1Current15MinLESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,12),_Cds1Current15MinLESsThreshold_Type())
cds1Current15MinLESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinLESsThreshold.setStatus(_B)
class _Cds1Current24HrLESsThreshold_Type(Integer32):defaultValue=121;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrLESsThreshold_Type.__name__=_D
_Cds1Current24HrLESsThreshold_Object=MibTableColumn
cds1Current24HrLESsThreshold=_Cds1Current24HrLESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,13),_Cds1Current24HrLESsThreshold_Type())
cds1Current24HrLESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrLESsThreshold.setStatus(_B)
class _Cds1Current15MinLSESsThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinLSESsThreshold_Type.__name__=_D
_Cds1Current15MinLSESsThreshold_Object=MibTableColumn
cds1Current15MinLSESsThreshold=_Cds1Current15MinLSESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,14),_Cds1Current15MinLSESsThreshold_Type())
cds1Current15MinLSESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinLSESsThreshold.setStatus(_B)
class _Cds1Current24HrLSESsThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrLSESsThreshold_Type.__name__=_D
_Cds1Current24HrLSESsThreshold_Object=MibTableColumn
cds1Current24HrLSESsThreshold=_Cds1Current24HrLSESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,15),_Cds1Current24HrLSESsThreshold_Type())
cds1Current24HrLSESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrLSESsThreshold.setStatus(_B)
class _Cds1Current15MinPCVsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinPCVsThreshold_Type.__name__=_D
_Cds1Current15MinPCVsThreshold_Object=MibTableColumn
cds1Current15MinPCVsThreshold=_Cds1Current15MinPCVsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,16),_Cds1Current15MinPCVsThreshold_Type())
cds1Current15MinPCVsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinPCVsThreshold.setStatus(_B)
class _Cds1Current24HrPCVsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrPCVsThreshold_Type.__name__=_D
_Cds1Current24HrPCVsThreshold_Object=MibTableColumn
cds1Current24HrPCVsThreshold=_Cds1Current24HrPCVsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,17),_Cds1Current24HrPCVsThreshold_Type())
cds1Current24HrPCVsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrPCVsThreshold.setStatus(_B)
class _Cds1Current15MinPSASsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinPSASsThreshold_Type.__name__=_D
_Cds1Current15MinPSASsThreshold_Object=MibTableColumn
cds1Current15MinPSASsThreshold=_Cds1Current15MinPSASsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,18),_Cds1Current15MinPSASsThreshold_Type())
cds1Current15MinPSASsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinPSASsThreshold.setStatus(_B)
class _Cds1Current24HrPSASsThreshold_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrPSASsThreshold_Type.__name__=_D
_Cds1Current24HrPSASsThreshold_Object=MibTableColumn
cds1Current24HrPSASsThreshold=_Cds1Current24HrPSASsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,19),_Cds1Current24HrPSASsThreshold_Type())
cds1Current24HrPSASsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrPSASsThreshold.setStatus(_B)
class _Cds1Current15MinSESsThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinSESsThreshold_Type.__name__=_D
_Cds1Current15MinSESsThreshold_Object=MibTableColumn
cds1Current15MinSESsThreshold=_Cds1Current15MinSESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,20),_Cds1Current15MinSESsThreshold_Type())
cds1Current15MinSESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinSESsThreshold.setStatus(_B)
class _Cds1Current24HrSESsThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrSESsThreshold_Type.__name__=_D
_Cds1Current24HrSESsThreshold_Object=MibTableColumn
cds1Current24HrSESsThreshold=_Cds1Current24HrSESsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,21),_Cds1Current24HrSESsThreshold_Type())
cds1Current24HrSESsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrSESsThreshold.setStatus(_B)
class _Cds1Current15MinSEFSsThreshold_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinSEFSsThreshold_Type.__name__=_D
_Cds1Current15MinSEFSsThreshold_Object=MibTableColumn
cds1Current15MinSEFSsThreshold=_Cds1Current15MinSEFSsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,22),_Cds1Current15MinSEFSsThreshold_Type())
cds1Current15MinSEFSsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinSEFSsThreshold.setStatus(_B)
class _Cds1Current24HrSEFSsThreshold_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrSEFSsThreshold_Type.__name__=_D
_Cds1Current24HrSEFSsThreshold_Object=MibTableColumn
cds1Current24HrSEFSsThreshold=_Cds1Current24HrSEFSsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,23),_Cds1Current24HrSEFSsThreshold_Type())
cds1Current24HrSEFSsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrSEFSsThreshold.setStatus(_B)
class _Cds1Current15MinUASsThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current15MinUASsThreshold_Type.__name__=_D
_Cds1Current15MinUASsThreshold_Object=MibTableColumn
cds1Current15MinUASsThreshold=_Cds1Current15MinUASsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,24),_Cds1Current15MinUASsThreshold_Type())
cds1Current15MinUASsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current15MinUASsThreshold.setStatus(_B)
class _Cds1Current24HrUASsThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1Current24HrUASsThreshold_Type.__name__=_D
_Cds1Current24HrUASsThreshold_Object=MibTableColumn
cds1Current24HrUASsThreshold=_Cds1Current24HrUASsThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,25),_Cds1Current24HrUASsThreshold_Type())
cds1Current24HrUASsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1Current24HrUASsThreshold.setStatus(_B)
_Cds1AlarmThresholdGroupRowStatus_Type=RowStatus
_Cds1AlarmThresholdGroupRowStatus_Object=MibTableColumn
cds1AlarmThresholdGroupRowStatus=_Cds1AlarmThresholdGroupRowStatus_Object((1,3,6,1,4,1,9,9,229,1,2,1,1,26),_Cds1AlarmThresholdGroupRowStatus_Type())
cds1AlarmThresholdGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cds1AlarmThresholdGroupRowStatus.setStatus(_B)
_Cds1AlarmConfigTable_Object=MibTable
cds1AlarmConfigTable=_Cds1AlarmConfigTable_Object((1,3,6,1,4,1,9,9,229,1,2,2))
if mibBuilder.loadTexts:cds1AlarmConfigTable.setStatus(_B)
_Cds1AlarmConfigEntry_Object=MibTableRow
cds1AlarmConfigEntry=_Cds1AlarmConfigEntry_Object((1,3,6,1,4,1,9,9,229,1,2,2,1))
if mibBuilder.loadTexts:cds1AlarmConfigEntry.setStatus(_B)
class _Cds1StatisticalAlarmSeverity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('minor',1),('major',2),('none',3)))
_Cds1StatisticalAlarmSeverity_Type.__name__=_D
_Cds1StatisticalAlarmSeverity_Object=MibTableColumn
cds1StatisticalAlarmSeverity=_Cds1StatisticalAlarmSeverity_Object((1,3,6,1,4,1,9,9,229,1,2,2,1,1),_Cds1StatisticalAlarmSeverity_Type())
cds1StatisticalAlarmSeverity.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1StatisticalAlarmSeverity.setStatus(_B)
class _Cds1StatisticalAlarmState_Type(Bits):namedValues=NamedValues(*(('cds1BES15Min',0),('cds1BES24Hr',1),('cds1CSS15Min',2),('cds1CSS24Hr',3),('cds1DM15Min',4),('cds1DM24Hr',5),('cds1ES15Min',6),('cds1ES24Hr',7),('cds1PCV15Min',8),('cds1PCV24Hr',9),('cds1LCV15Min',10),('cds1LCV24Hr',11),('cds1LES15Min',12),('cds1LES24Hr',13),('cds1LSES15Min',14),('cds1LSES24Hr',15),('cds1PSAS15Min',16),('cds1PSAS24Hr',17),('cds1SES15Min',18),('cds1SES24Hr',19),('cds1SEFS15Min',20),('cds1SEFS24Hr',21),('cds1UAS15Min',22),('cds1UAS24Hr',23)))
_Cds1StatisticalAlarmState_Type.__name__='Bits'
_Cds1StatisticalAlarmState_Object=MibTableColumn
cds1StatisticalAlarmState=_Cds1StatisticalAlarmState_Object((1,3,6,1,4,1,9,9,229,1,2,2,1,2),_Cds1StatisticalAlarmState_Type())
cds1StatisticalAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1StatisticalAlarmState.setStatus(_B)
class _Cds1AlarmUpCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1AlarmUpCount_Type.__name__=_D
_Cds1AlarmUpCount_Object=MibTableColumn
cds1AlarmUpCount=_Cds1AlarmUpCount_Object((1,3,6,1,4,1,9,9,229,1,2,2,1,3),_Cds1AlarmUpCount_Type())
cds1AlarmUpCount.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1AlarmUpCount.setStatus(_B)
class _Cds1AlarmDownCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1AlarmDownCount_Type.__name__=_D
_Cds1AlarmDownCount_Object=MibTableColumn
cds1AlarmDownCount=_Cds1AlarmDownCount_Object((1,3,6,1,4,1,9,9,229,1,2,2,1,4),_Cds1AlarmDownCount_Type())
cds1AlarmDownCount.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1AlarmDownCount.setStatus(_B)
class _Cds1AlarmThreshold_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds1AlarmThreshold_Type.__name__=_D
_Cds1AlarmThreshold_Object=MibTableColumn
cds1AlarmThreshold=_Cds1AlarmThreshold_Object((1,3,6,1,4,1,9,9,229,1,2,2,1,5),_Cds1AlarmThreshold_Type())
cds1AlarmThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1AlarmThreshold.setStatus(_B)
class _Cds1AlarmThresholdActiveGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Cds1AlarmThresholdActiveGroup_Type.__name__=_D
_Cds1AlarmThresholdActiveGroup_Object=MibTableColumn
cds1AlarmThresholdActiveGroup=_Cds1AlarmThresholdActiveGroup_Object((1,3,6,1,4,1,9,9,229,1,2,2,1,6),_Cds1AlarmThresholdActiveGroup_Type())
cds1AlarmThresholdActiveGroup.setMaxAccess(_F)
if mibBuilder.loadTexts:cds1AlarmThresholdActiveGroup.setStatus(_B)
_Cds1Stats_ObjectIdentity=ObjectIdentity
cds1Stats=_Cds1Stats_ObjectIdentity((1,3,6,1,4,1,9,9,229,1,3))
_Cds1CurrentTable_Object=MibTable
cds1CurrentTable=_Cds1CurrentTable_Object((1,3,6,1,4,1,9,9,229,1,3,1))
if mibBuilder.loadTexts:cds1CurrentTable.setStatus(_B)
_Cds1CurrentEntry_Object=MibTableRow
cds1CurrentEntry=_Cds1CurrentEntry_Object((1,3,6,1,4,1,9,9,229,1,3,1,1))
if mibBuilder.loadTexts:cds1CurrentEntry.setStatus(_B)
_Cds1CurrentLSESs_Type=PerfCurrentCount
_Cds1CurrentLSESs_Object=MibTableColumn
cds1CurrentLSESs=_Cds1CurrentLSESs_Object((1,3,6,1,4,1,9,9,229,1,3,1,1,1),_Cds1CurrentLSESs_Type())
cds1CurrentLSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1CurrentLSESs.setStatus(_B)
_Cds1CurrentPSASs_Type=PerfCurrentCount
_Cds1CurrentPSASs_Object=MibTableColumn
cds1CurrentPSASs=_Cds1CurrentPSASs_Object((1,3,6,1,4,1,9,9,229,1,3,1,1,2),_Cds1CurrentPSASs_Type())
cds1CurrentPSASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1CurrentPSASs.setStatus(_B)
_Cds1IntervalTable_Object=MibTable
cds1IntervalTable=_Cds1IntervalTable_Object((1,3,6,1,4,1,9,9,229,1,3,2))
if mibBuilder.loadTexts:cds1IntervalTable.setStatus(_B)
_Cds1IntervalEntry_Object=MibTableRow
cds1IntervalEntry=_Cds1IntervalEntry_Object((1,3,6,1,4,1,9,9,229,1,3,2,1))
if mibBuilder.loadTexts:cds1IntervalEntry.setStatus(_B)
_Cds1IntervalLSESs_Type=PerfIntervalCount
_Cds1IntervalLSESs_Object=MibTableColumn
cds1IntervalLSESs=_Cds1IntervalLSESs_Object((1,3,6,1,4,1,9,9,229,1,3,2,1,1),_Cds1IntervalLSESs_Type())
cds1IntervalLSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1IntervalLSESs.setStatus(_B)
_Cds1IntervalPSASs_Type=PerfIntervalCount
_Cds1IntervalPSASs_Object=MibTableColumn
cds1IntervalPSASs=_Cds1IntervalPSASs_Object((1,3,6,1,4,1,9,9,229,1,3,2,1,2),_Cds1IntervalPSASs_Type())
cds1IntervalPSASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1IntervalPSASs.setStatus(_B)
_Cds1TotalTable_Object=MibTable
cds1TotalTable=_Cds1TotalTable_Object((1,3,6,1,4,1,9,9,229,1,3,3))
if mibBuilder.loadTexts:cds1TotalTable.setStatus(_B)
_Cds1TotalEntry_Object=MibTableRow
cds1TotalEntry=_Cds1TotalEntry_Object((1,3,6,1,4,1,9,9,229,1,3,3,1))
if mibBuilder.loadTexts:cds1TotalEntry.setStatus(_B)
_Cds1TotalLSESs_Type=PerfTotalCount
_Cds1TotalLSESs_Object=MibTableColumn
cds1TotalLSESs=_Cds1TotalLSESs_Object((1,3,6,1,4,1,9,9,229,1,3,3,1,1),_Cds1TotalLSESs_Type())
cds1TotalLSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1TotalLSESs.setStatus(_B)
_Cds1TotalPSASs_Type=PerfTotalCount
_Cds1TotalPSASs_Object=MibTableColumn
cds1TotalPSASs=_Cds1TotalPSASs_Object((1,3,6,1,4,1,9,9,229,1,3,3,1,2),_Cds1TotalPSASs_Type())
cds1TotalPSASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1TotalPSASs.setStatus(_B)
_Cds1FarEndCurrentTable_Object=MibTable
cds1FarEndCurrentTable=_Cds1FarEndCurrentTable_Object((1,3,6,1,4,1,9,9,229,1,3,4))
if mibBuilder.loadTexts:cds1FarEndCurrentTable.setStatus(_B)
_Cds1FarEndCurrentEntry_Object=MibTableRow
cds1FarEndCurrentEntry=_Cds1FarEndCurrentEntry_Object((1,3,6,1,4,1,9,9,229,1,3,4,1))
if mibBuilder.loadTexts:cds1FarEndCurrentEntry.setStatus(_B)
_Cds1FarEndCurrentLOFCs_Type=PerfCurrentCount
_Cds1FarEndCurrentLOFCs_Object=MibTableColumn
cds1FarEndCurrentLOFCs=_Cds1FarEndCurrentLOFCs_Object((1,3,6,1,4,1,9,9,229,1,3,4,1,1),_Cds1FarEndCurrentLOFCs_Type())
cds1FarEndCurrentLOFCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1FarEndCurrentLOFCs.setStatus(_B)
_Cds1FarEndIntervalTable_Object=MibTable
cds1FarEndIntervalTable=_Cds1FarEndIntervalTable_Object((1,3,6,1,4,1,9,9,229,1,3,5))
if mibBuilder.loadTexts:cds1FarEndIntervalTable.setStatus(_B)
_Cds1FarEndIntervalEntry_Object=MibTableRow
cds1FarEndIntervalEntry=_Cds1FarEndIntervalEntry_Object((1,3,6,1,4,1,9,9,229,1,3,5,1))
if mibBuilder.loadTexts:cds1FarEndIntervalEntry.setStatus(_B)
_Cds1FarEndIntervalLOFCs_Type=PerfIntervalCount
_Cds1FarEndIntervalLOFCs_Object=MibTableColumn
cds1FarEndIntervalLOFCs=_Cds1FarEndIntervalLOFCs_Object((1,3,6,1,4,1,9,9,229,1,3,5,1,1),_Cds1FarEndIntervalLOFCs_Type())
cds1FarEndIntervalLOFCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1FarEndIntervalLOFCs.setStatus(_B)
_Cds1FarEndTotalTable_Object=MibTable
cds1FarEndTotalTable=_Cds1FarEndTotalTable_Object((1,3,6,1,4,1,9,9,229,1,3,6))
if mibBuilder.loadTexts:cds1FarEndTotalTable.setStatus(_B)
_Cds1FarEndTotalEntry_Object=MibTableRow
cds1FarEndTotalEntry=_Cds1FarEndTotalEntry_Object((1,3,6,1,4,1,9,9,229,1,3,6,1))
if mibBuilder.loadTexts:cds1FarEndTotalEntry.setStatus(_B)
_Cds1FarEndTotalLOFCs_Type=PerfTotalCount
_Cds1FarEndTotalLOFCs_Object=MibTableColumn
cds1FarEndTotalLOFCs=_Cds1FarEndTotalLOFCs_Object((1,3,6,1,4,1,9,9,229,1,3,6,1,1),_Cds1FarEndTotalLOFCs_Type())
cds1FarEndTotalLOFCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1FarEndTotalLOFCs.setStatus(_B)
_Cds1Current24HrStatsTable_Object=MibTable
cds1Current24HrStatsTable=_Cds1Current24HrStatsTable_Object((1,3,6,1,4,1,9,9,229,1,3,7))
if mibBuilder.loadTexts:cds1Current24HrStatsTable.setStatus(_B)
_Cds1Current24HrStatsEntry_Object=MibTableRow
cds1Current24HrStatsEntry=_Cds1Current24HrStatsEntry_Object((1,3,6,1,4,1,9,9,229,1,3,7,1))
cds1Current24HrStatsEntry.setIndexNames((0,_Q,_R))
if mibBuilder.loadTexts:cds1Current24HrStatsEntry.setStatus(_B)
_Cds1Current24HrESs_Type=PerfCurrent24HourCount
_Cds1Current24HrESs_Object=MibTableColumn
cds1Current24HrESs=_Cds1Current24HrESs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,1),_Cds1Current24HrESs_Type())
cds1Current24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrESs.setStatus(_B)
_Cds1Current24HrSESs_Type=PerfCurrent24HourCount
_Cds1Current24HrSESs_Object=MibTableColumn
cds1Current24HrSESs=_Cds1Current24HrSESs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,2),_Cds1Current24HrSESs_Type())
cds1Current24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrSESs.setStatus(_B)
_Cds1Current24HrSEFSs_Type=PerfCurrent24HourCount
_Cds1Current24HrSEFSs_Object=MibTableColumn
cds1Current24HrSEFSs=_Cds1Current24HrSEFSs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,3),_Cds1Current24HrSEFSs_Type())
cds1Current24HrSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrSEFSs.setStatus(_B)
_Cds1Current24HrUASs_Type=PerfCurrent24HourCount
_Cds1Current24HrUASs_Object=MibTableColumn
cds1Current24HrUASs=_Cds1Current24HrUASs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,4),_Cds1Current24HrUASs_Type())
cds1Current24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrUASs.setStatus(_B)
_Cds1Current24HrCSSs_Type=PerfCurrent24HourCount
_Cds1Current24HrCSSs_Object=MibTableColumn
cds1Current24HrCSSs=_Cds1Current24HrCSSs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,5),_Cds1Current24HrCSSs_Type())
cds1Current24HrCSSs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrCSSs.setStatus(_B)
_Cds1Current24HrPCVs_Type=PerfCurrent24HourCount
_Cds1Current24HrPCVs_Object=MibTableColumn
cds1Current24HrPCVs=_Cds1Current24HrPCVs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,6),_Cds1Current24HrPCVs_Type())
cds1Current24HrPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrPCVs.setStatus(_B)
_Cds1Current24HrLESs_Type=PerfCurrent24HourCount
_Cds1Current24HrLESs_Object=MibTableColumn
cds1Current24HrLESs=_Cds1Current24HrLESs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,7),_Cds1Current24HrLESs_Type())
cds1Current24HrLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrLESs.setStatus(_B)
_Cds1Current24HrBESs_Type=PerfCurrent24HourCount
_Cds1Current24HrBESs_Object=MibTableColumn
cds1Current24HrBESs=_Cds1Current24HrBESs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,8),_Cds1Current24HrBESs_Type())
cds1Current24HrBESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrBESs.setStatus(_B)
_Cds1Current24HrDMs_Type=PerfCurrent24HourCount
_Cds1Current24HrDMs_Object=MibTableColumn
cds1Current24HrDMs=_Cds1Current24HrDMs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,9),_Cds1Current24HrDMs_Type())
cds1Current24HrDMs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrDMs.setStatus(_B)
_Cds1Current24HrLCVs_Type=PerfCurrent24HourCount
_Cds1Current24HrLCVs_Object=MibTableColumn
cds1Current24HrLCVs=_Cds1Current24HrLCVs_Object((1,3,6,1,4,1,9,9,229,1,3,7,1,10),_Cds1Current24HrLCVs_Type())
cds1Current24HrLCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Current24HrLCVs.setStatus(_B)
_Cds1Previous24HrStatsTable_Object=MibTable
cds1Previous24HrStatsTable=_Cds1Previous24HrStatsTable_Object((1,3,6,1,4,1,9,9,229,1,3,8))
if mibBuilder.loadTexts:cds1Previous24HrStatsTable.setStatus(_B)
_Cds1Previous24HrStatsEntry_Object=MibTableRow
cds1Previous24HrStatsEntry=_Cds1Previous24HrStatsEntry_Object((1,3,6,1,4,1,9,9,229,1,3,8,1))
cds1Previous24HrStatsEntry.setIndexNames((0,_Q,_R))
if mibBuilder.loadTexts:cds1Previous24HrStatsEntry.setStatus(_B)
_Cds1Previous24HrESs_Type=PerfPrevious24HourCount
_Cds1Previous24HrESs_Object=MibTableColumn
cds1Previous24HrESs=_Cds1Previous24HrESs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,1),_Cds1Previous24HrESs_Type())
cds1Previous24HrESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrESs.setStatus(_B)
_Cds1Previous24HrSESs_Type=PerfPrevious24HourCount
_Cds1Previous24HrSESs_Object=MibTableColumn
cds1Previous24HrSESs=_Cds1Previous24HrSESs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,2),_Cds1Previous24HrSESs_Type())
cds1Previous24HrSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrSESs.setStatus(_B)
_Cds1Previous24HrSEFSs_Type=PerfPrevious24HourCount
_Cds1Previous24HrSEFSs_Object=MibTableColumn
cds1Previous24HrSEFSs=_Cds1Previous24HrSEFSs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,3),_Cds1Previous24HrSEFSs_Type())
cds1Previous24HrSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrSEFSs.setStatus(_B)
_Cds1Previous24HrUASs_Type=PerfPrevious24HourCount
_Cds1Previous24HrUASs_Object=MibTableColumn
cds1Previous24HrUASs=_Cds1Previous24HrUASs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,4),_Cds1Previous24HrUASs_Type())
cds1Previous24HrUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrUASs.setStatus(_B)
_Cds1Previous24HrCSSs_Type=PerfPrevious24HourCount
_Cds1Previous24HrCSSs_Object=MibTableColumn
cds1Previous24HrCSSs=_Cds1Previous24HrCSSs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,5),_Cds1Previous24HrCSSs_Type())
cds1Previous24HrCSSs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrCSSs.setStatus(_B)
_Cds1Previous24HrPCVs_Type=PerfPrevious24HourCount
_Cds1Previous24HrPCVs_Object=MibTableColumn
cds1Previous24HrPCVs=_Cds1Previous24HrPCVs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,6),_Cds1Previous24HrPCVs_Type())
cds1Previous24HrPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrPCVs.setStatus(_B)
_Cds1Previous24HrLESs_Type=PerfPrevious24HourCount
_Cds1Previous24HrLESs_Object=MibTableColumn
cds1Previous24HrLESs=_Cds1Previous24HrLESs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,7),_Cds1Previous24HrLESs_Type())
cds1Previous24HrLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrLESs.setStatus(_B)
_Cds1Previous24HrBESs_Type=PerfPrevious24HourCount
_Cds1Previous24HrBESs_Object=MibTableColumn
cds1Previous24HrBESs=_Cds1Previous24HrBESs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,8),_Cds1Previous24HrBESs_Type())
cds1Previous24HrBESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrBESs.setStatus(_B)
_Cds1Previous24HrDMs_Type=PerfPrevious24HourCount
_Cds1Previous24HrDMs_Object=MibTableColumn
cds1Previous24HrDMs=_Cds1Previous24HrDMs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,9),_Cds1Previous24HrDMs_Type())
cds1Previous24HrDMs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrDMs.setStatus(_B)
_Cds1Previous24HrLCVs_Type=PerfPrevious24HourCount
_Cds1Previous24HrLCVs_Object=MibTableColumn
cds1Previous24HrLCVs=_Cds1Previous24HrLCVs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,10),_Cds1Previous24HrLCVs_Type())
cds1Previous24HrLCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrLCVs.setStatus(_B)
_Cds1Previous24HrLSESs_Type=PerfPrevious24HourCount
_Cds1Previous24HrLSESs_Object=MibTableColumn
cds1Previous24HrLSESs=_Cds1Previous24HrLSESs_Object((1,3,6,1,4,1,9,9,229,1,3,8,1,11),_Cds1Previous24HrLSESs_Type())
cds1Previous24HrLSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1Previous24HrLSESs.setStatus(_B)
_Cds1ErrStatsTable_Object=MibTable
cds1ErrStatsTable=_Cds1ErrStatsTable_Object((1,3,6,1,4,1,9,9,229,1,3,9))
if mibBuilder.loadTexts:cds1ErrStatsTable.setStatus(_B)
_Cds1ErrStatsEntry_Object=MibTableRow
cds1ErrStatsEntry=_Cds1ErrStatsEntry_Object((1,3,6,1,4,1,9,9,229,1,3,9,1))
cds1ErrStatsEntry.setIndexNames((0,_Q,_R))
if mibBuilder.loadTexts:cds1ErrStatsEntry.setStatus(_B)
_Cds1LOSCounts_Type=Counter32
_Cds1LOSCounts_Object=MibTableColumn
cds1LOSCounts=_Cds1LOSCounts_Object((1,3,6,1,4,1,9,9,229,1,3,9,1,1),_Cds1LOSCounts_Type())
cds1LOSCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1LOSCounts.setStatus(_B)
_Cds1OOFCounts_Type=Counter32
_Cds1OOFCounts_Object=MibTableColumn
cds1OOFCounts=_Cds1OOFCounts_Object((1,3,6,1,4,1,9,9,229,1,3,9,1,2),_Cds1OOFCounts_Type())
cds1OOFCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1OOFCounts.setStatus(_B)
_Cds1RAICounts_Type=Counter32
_Cds1RAICounts_Object=MibTableColumn
cds1RAICounts=_Cds1RAICounts_Object((1,3,6,1,4,1,9,9,229,1,3,9,1,3),_Cds1RAICounts_Type())
cds1RAICounts.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1RAICounts.setStatus(_B)
_Cds1FECounts_Type=Counter32
_Cds1FECounts_Object=MibTableColumn
cds1FECounts=_Cds1FECounts_Object((1,3,6,1,4,1,9,9,229,1,3,9,1,4),_Cds1FECounts_Type())
cds1FECounts.setMaxAccess(_C)
if mibBuilder.loadTexts:cds1FECounts.setStatus(_B)
_Cds1NotificationPrefix_ObjectIdentity=ObjectIdentity
cds1NotificationPrefix=_Cds1NotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,229,1,4))
_Cds1Notifications_ObjectIdentity=ObjectIdentity
cds1Notifications=_Cds1Notifications_ObjectIdentity((1,3,6,1,4,1,9,9,229,1,4,0))
_CiscoDs1MIBConformance_ObjectIdentity=ObjectIdentity
ciscoDs1MIBConformance=_CiscoDs1MIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,229,3))
_CiscoDs1MIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDs1MIBCompliances=_CiscoDs1MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,229,3,1))
_CiscoDs1MIBGroups_ObjectIdentity=ObjectIdentity
ciscoDs1MIBGroups=_CiscoDs1MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,229,3,2))
dsx1ConfigEntry.registerAugmentions((_A,_A1))
cds1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
dsx1ConfigEntry.registerAugmentions((_A,_A2))
cds1CallConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
dsx1ConfigEntry.registerAugmentions((_A,_A3))
cds1AlarmConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
dsx1CurrentEntry.registerAugmentions((_A,_A4))
cds1CurrentEntry.setIndexNames(*dsx1CurrentEntry.getIndexNames())
dsx1IntervalEntry.registerAugmentions((_A,_A5))
cds1IntervalEntry.setIndexNames(*dsx1IntervalEntry.getIndexNames())
dsx1TotalEntry.registerAugmentions((_A,_A6))
cds1TotalEntry.setIndexNames(*dsx1TotalEntry.getIndexNames())
dsx1FarEndCurrentEntry.registerAugmentions((_A,_A7))
cds1FarEndCurrentEntry.setIndexNames(*dsx1FarEndCurrentEntry.getIndexNames())
dsx1FarEndIntervalEntry.registerAugmentions((_A,_A8))
cds1FarEndIntervalEntry.setIndexNames(*dsx1FarEndIntervalEntry.getIndexNames())
dsx1FarEndTotalEntry.registerAugmentions((_A,_A9))
cds1FarEndTotalEntry.setIndexNames(*dsx1FarEndTotalEntry.getIndexNames())
ciscoDs1ConfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,1))
ciscoDs1ConfMIBGroup.setObjects(*((_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ciscoDs1ConfMIBGroup.setStatus(_B)
ciscoDs1CurrentMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,2))
ciscoDs1CurrentMIBGroup.setObjects(*((_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:ciscoDs1CurrentMIBGroup.setStatus(_B)
ciscoDs1IntervalMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,3))
ciscoDs1IntervalMIBGroup.setObjects(*((_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:ciscoDs1IntervalMIBGroup.setStatus(_B)
ciscoDs1TotalMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,4))
ciscoDs1TotalMIBGroup.setObjects(*((_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:ciscoDs1TotalMIBGroup.setStatus(_B)
ciscoDs1FarEndStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,5))
ciscoDs1FarEndStatsMIBGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:ciscoDs1FarEndStatsMIBGroup.setStatus(_B)
ciscoDs1AlarmConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,6))
ciscoDs1AlarmConfigGroup.setObjects(*((_A,_AL),(_A,_V),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:ciscoDs1AlarmConfigGroup.setStatus(_B)
ciscoDs1Alarm15MinThreshGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,7))
ciscoDs1Alarm15MinThreshGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_S)))
if mibBuilder.loadTexts:ciscoDs1Alarm15MinThreshGroup.setStatus(_G)
ciscoDs1Alarm24HrThreshGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,8))
ciscoDs1Alarm24HrThreshGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_S)))
if mibBuilder.loadTexts:ciscoDs1Alarm24HrThreshGroup.setStatus(_G)
ciscoDs1Current24HrMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,9))
ciscoDs1Current24HrMIBGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:ciscoDs1Current24HrMIBGroup.setStatus(_B)
ciscoDs1Previous24HrMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,10))
ciscoDs1Previous24HrMIBGroup.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:ciscoDs1Previous24HrMIBGroup.setStatus(_B)
ciscoDs1StatsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,11))
ciscoDs1StatsMIBGroup.setObjects(*((_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:ciscoDs1StatsMIBGroup.setStatus(_B)
ciscoDs1BulkConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,13))
ciscoDs1BulkConfGroup.setObjects(*((_A,_Ap),(_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:ciscoDs1BulkConfGroup.setStatus(_B)
ciscoDs1AlarmThreshGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,14))
ciscoDs1AlarmThreshGroup.setObjects((_A,_S))
if mibBuilder.loadTexts:ciscoDs1AlarmThreshGroup.setStatus(_B)
ciscoDs1Alarm15MinThreshGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,15))
ciscoDs1Alarm15MinThreshGroupRev1.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ciscoDs1Alarm15MinThreshGroupRev1.setStatus(_B)
ciscoDs1Alarm24HrThreshGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,16))
ciscoDs1Alarm24HrThreshGroupRev1.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:ciscoDs1Alarm24HrThreshGroupRev1.setStatus(_B)
ciscoDs1CallGroup=ObjectGroup((1,3,6,1,4,1,9,9,229,3,2,17))
ciscoDs1CallGroup.setObjects((_A,_As))
if mibBuilder.loadTexts:ciscoDs1CallGroup.setStatus(_B)
cds1StatThresholdAlarm=NotificationType((1,3,6,1,4,1,9,9,229,1,4,0,1))
cds1StatThresholdAlarm.setObjects((_A,_V))
if mibBuilder.loadTexts:cds1StatThresholdAlarm.setStatus(_B)
cds1NEOptionalNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,229,3,2,12))
cds1NEOptionalNotificationsGroup.setObjects((_A,_At))
if mibBuilder.loadTexts:cds1NEOptionalNotificationsGroup.setStatus(_B)
ciscoDs1MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,229,3,1,1))
ciscoDs1MIBCompliance.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_u),(_A,_v),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoDs1MIBCompliance.setStatus(_G)
ciscoDs1MIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,229,3,1,2))
ciscoDs1MIBComplianceRev1.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_u),(_A,_v),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_T)))
if mibBuilder.loadTexts:ciscoDs1MIBComplianceRev1.setStatus(_G)
ciscoDs1MIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,229,3,1,3))
ciscoDs1MIBComplianceRev2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_w),(_A,_x),(_A,_y),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_T)))
if mibBuilder.loadTexts:ciscoDs1MIBComplianceRev2.setStatus(_G)
ciscoDs1MIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,229,3,1,4))
ciscoDs1MIBComplianceRev3.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_w),(_A,_x),(_A,_y),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_T),(_A,_Au),(_A,_Av)))
if mibBuilder.loadTexts:ciscoDs1MIBComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PerfCurrent24HourCount':PerfCurrent24HourCount,'PerfPrevious24HourCount':PerfPrevious24HourCount,'ciscoDs1ExtMIB':ciscoDs1ExtMIB,'ciscoDs1MIBObjects':ciscoDs1MIBObjects,'cds1Config':cds1Config,'cds1ConfigTable':cds1ConfigTable,_A1:cds1ConfigEntry,_AA:cds1LineType,_AB:cds1LoopbackCodeDetection,_Ap:cds1Repetition,_Aq:cds1RepetitionOwner,_Ar:cds1RepetitionResult,'cds1CallConfigTable':cds1CallConfigTable,_A2:cds1CallConfigEntry,_As:cds1CallTrunkConditionEnable,'cds1Alarm':cds1Alarm,'cds1AlarmThresholdGroupTable':cds1AlarmThresholdGroupTable,'cds1AlarmThresholdGroupEntry':cds1AlarmThresholdGroupEntry,_A0:cds1AlarmThresholdGroupIndex,_d:cds1Current15MinBESsThreshold,_p:cds1Current24HrBESsThreshold,_g:cds1Current15MinCSSsThreshold,_q:cds1Current24HrCSSsThreshold,_e:cds1Current15MinDMsThreshold,_r:cds1Current24HrDMsThreshold,_f:cds1Current15MinESsThreshold,_s:cds1Current24HrESsThreshold,_W:cds1Current15MinLCVsThreshold,_i:cds1Current24HrLCVsThreshold,_X:cds1Current15MinLESsThreshold,_j:cds1Current24HrLESsThreshold,_b:cds1Current15MinLSESsThreshold,_n:cds1Current24HrLSESsThreshold,_Y:cds1Current15MinPCVsThreshold,_k:cds1Current24HrPCVsThreshold,_h:cds1Current15MinPSASsThreshold,_t:cds1Current24HrPSASsThreshold,_c:cds1Current15MinSESsThreshold,_o:cds1Current24HrSESsThreshold,_Z:cds1Current15MinSEFSsThreshold,_l:cds1Current24HrSEFSsThreshold,_a:cds1Current15MinUASsThreshold,_m:cds1Current24HrUASsThreshold,_S:cds1AlarmThresholdGroupRowStatus,'cds1AlarmConfigTable':cds1AlarmConfigTable,_A3:cds1AlarmConfigEntry,_AL:cds1StatisticalAlarmSeverity,_V:cds1StatisticalAlarmState,_AM:cds1AlarmUpCount,_AN:cds1AlarmDownCount,_AO:cds1AlarmThreshold,_AP:cds1AlarmThresholdActiveGroup,'cds1Stats':cds1Stats,'cds1CurrentTable':cds1CurrentTable,_A4:cds1CurrentEntry,_AC:cds1CurrentLSESs,_AD:cds1CurrentPSASs,'cds1IntervalTable':cds1IntervalTable,_A5:cds1IntervalEntry,_AE:cds1IntervalLSESs,_AF:cds1IntervalPSASs,'cds1TotalTable':cds1TotalTable,_A6:cds1TotalEntry,_AG:cds1TotalLSESs,_AH:cds1TotalPSASs,'cds1FarEndCurrentTable':cds1FarEndCurrentTable,_A7:cds1FarEndCurrentEntry,_AI:cds1FarEndCurrentLOFCs,'cds1FarEndIntervalTable':cds1FarEndIntervalTable,_A8:cds1FarEndIntervalEntry,_AJ:cds1FarEndIntervalLOFCs,'cds1FarEndTotalTable':cds1FarEndTotalTable,_A9:cds1FarEndTotalEntry,_AK:cds1FarEndTotalLOFCs,'cds1Current24HrStatsTable':cds1Current24HrStatsTable,'cds1Current24HrStatsEntry':cds1Current24HrStatsEntry,_AQ:cds1Current24HrESs,_AR:cds1Current24HrSESs,_AS:cds1Current24HrSEFSs,_AT:cds1Current24HrUASs,_AU:cds1Current24HrCSSs,_AV:cds1Current24HrPCVs,_AW:cds1Current24HrLESs,_AX:cds1Current24HrBESs,_AY:cds1Current24HrDMs,_AZ:cds1Current24HrLCVs,'cds1Previous24HrStatsTable':cds1Previous24HrStatsTable,'cds1Previous24HrStatsEntry':cds1Previous24HrStatsEntry,_Aa:cds1Previous24HrESs,_Ab:cds1Previous24HrSESs,_Ac:cds1Previous24HrSEFSs,_Ad:cds1Previous24HrUASs,_Ae:cds1Previous24HrCSSs,_Af:cds1Previous24HrPCVs,_Ag:cds1Previous24HrLESs,_Ah:cds1Previous24HrBESs,_Ai:cds1Previous24HrDMs,_Aj:cds1Previous24HrLCVs,_Ak:cds1Previous24HrLSESs,'cds1ErrStatsTable':cds1ErrStatsTable,'cds1ErrStatsEntry':cds1ErrStatsEntry,_Al:cds1LOSCounts,_Am:cds1OOFCounts,_An:cds1RAICounts,_Ao:cds1FECounts,'cds1NotificationPrefix':cds1NotificationPrefix,'cds1Notifications':cds1Notifications,_At:cds1StatThresholdAlarm,'ciscoDs1MIBConformance':ciscoDs1MIBConformance,'ciscoDs1MIBCompliances':ciscoDs1MIBCompliances,'ciscoDs1MIBCompliance':ciscoDs1MIBCompliance,'ciscoDs1MIBComplianceRev1':ciscoDs1MIBComplianceRev1,'ciscoDs1MIBComplianceRev2':ciscoDs1MIBComplianceRev2,'ciscoDs1MIBComplianceRev3':ciscoDs1MIBComplianceRev3,'ciscoDs1MIBGroups':ciscoDs1MIBGroups,_H:ciscoDs1ConfMIBGroup,_I:ciscoDs1CurrentMIBGroup,_M:ciscoDs1IntervalMIBGroup,_N:ciscoDs1TotalMIBGroup,_P:ciscoDs1FarEndStatsMIBGroup,_J:ciscoDs1AlarmConfigGroup,_u:ciscoDs1Alarm15MinThreshGroup,_v:ciscoDs1Alarm24HrThreshGroup,_K:ciscoDs1Current24HrMIBGroup,_L:ciscoDs1Previous24HrMIBGroup,_O:ciscoDs1StatsMIBGroup,_Av:cds1NEOptionalNotificationsGroup,_T:ciscoDs1BulkConfGroup,_w:ciscoDs1AlarmThreshGroup,_x:ciscoDs1Alarm15MinThreshGroupRev1,_y:ciscoDs1Alarm24HrThreshGroupRev1,_Au:ciscoDs1CallGroup})