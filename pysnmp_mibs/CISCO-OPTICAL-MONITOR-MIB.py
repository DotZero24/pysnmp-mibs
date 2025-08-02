_AA='cOpticalMonThreshSourceGroup'
_A9='cOpticalMIBIntervalConfigGroup'
_A8='cOpticalMIBEnableConfigGroup'
_A7='cOpticalMonIfTimeGroup'
_A6='cOpticalMonParameterStatus'
_A5='cOpticalParamThreshSource'
_A4='cOpticalMonPollInterval'
_A3='cOpticalMonEnable'
_A2='cOpticalMonIfTimeInSlot'
_A1='cOpticalNotifyEnable'
_A0='cOpticalPMIntervalUnavailSecs'
_z='cOpticalPMIntervalMeanParam'
_y='cOpticalPMIntervalMinParam'
_x='cOpticalPMIntervalMaxParam'
_w='cOpticalPMCurrentUnavailSecs'
_v='cOpticalPMCurrentMeanParam'
_u='cOpticalPMCurrentMinParam'
_t='cOpticalPMCurrentMaxParam'
_s='cOpticalMon24HrValidIntervals'
_r='cOpticalMon15MinValidIntervals'
_q='cOpticalParamLowWarningSev'
_p='cOpticalParamLowAlarmSev'
_o='cOpticalParamHighWarningSev'
_n='cOpticalParamHighAlarmSev'
_m='cOpticalParamLowWarningThresh'
_l='cOpticalParamLowAlarmThresh'
_k='cOpticalParamHighWarningThresh'
_j='cOpticalParamHighAlarmThresh'
_i='cOpticalPMIntervalParamType'
_h='cOpticalPMIntervalLocation'
_g='cOpticalPMIntervalDirection'
_f='cOpticalPMIntervalNumber'
_e='cOpticalPMIntervalPeriod'
_d='cOpticalPMCurrentParamType'
_c='cOpticalPMCurrentLocation'
_b='cOpticalPMCurrentDirection'
_a='cOpticalPMCurrentPeriod'
_Z='OpticalAlarmSeverityOrZero'
_Y='cOpticalMonParameterType'
_X='cOpticalMonLocation'
_W='cOpticalMonDirection'
_V='notApplicable'
_U='cOpticalMIBNotifGroup'
_T='cOpticalMIBNotifyEnableGroup'
_S='cOpticalMIBPMGroup'
_R='cOpticalMIBSeverityGroup'
_Q='cOpticalMIBThresholdGroup'
_P='cOpticalMIBMonGroup'
_O='cOpticalParamAlarmCurMaxSev'
_N='cOpticalParamAlarmLastChange'
_M='cOpticalParamAlarmCurMaxThresh'
_L='cOpticalParamAlarmStatus'
_K='cOpticalParameterValue'
_J='Unsigned32'
_I='Bits'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='not-accessible'
_C='read-only'
_B='CISCO-OPTICAL-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoOpticalMonitorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,264))
if mibBuilder.loadTexts:ciscoOpticalMonitorMIB.setRevisions(('2007-01-02 00:00','2002-05-10 00:00'))
class OpticalParameterType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('power',1),('acPower',2),('ambientTemp',3),('laserTemp',4),('biasCurrent',5),('peltierCurrent',6),('xcvrVoltage',7)))
class OpticalParameterValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000,1000000))
class OpticalIfDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('receive',1),('transmit',2),(_V,3)))
class OpticalIfMonLocation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('beforeAdjustment',1),('afterAdjustment',2),(_V,3)))
class OpticalAlarmStatus(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
class OpticalAlarmSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('critical',1),('major',2),('minor',3),('notAlarmed',4),('notReported',5),('cleared',6)))
class OpticalAlarmSeverityOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
class OpticalPMPeriod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMin',1),('twentyFourHour',2)))
_COpticalMonitorMIBObjects_ObjectIdentity=ObjectIdentity
cOpticalMonitorMIBObjects=_COpticalMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,264,1))
_COpticalMonGroup_ObjectIdentity=ObjectIdentity
cOpticalMonGroup=_COpticalMonGroup_ObjectIdentity((1,3,6,1,4,1,9,9,264,1,1))
_COpticalMonTable_Object=MibTable
cOpticalMonTable=_COpticalMonTable_Object((1,3,6,1,4,1,9,9,264,1,1,1))
if mibBuilder.loadTexts:cOpticalMonTable.setStatus(_A)
_COpticalMonEntry_Object=MibTableRow
cOpticalMonEntry=_COpticalMonEntry_Object((1,3,6,1,4,1,9,9,264,1,1,1,1))
cOpticalMonEntry.setIndexNames((0,_F,_G),(0,_B,_W),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:cOpticalMonEntry.setStatus(_A)
_COpticalMonDirection_Type=OpticalIfDirection
_COpticalMonDirection_Object=MibTableColumn
cOpticalMonDirection=_COpticalMonDirection_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,1),_COpticalMonDirection_Type())
cOpticalMonDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalMonDirection.setStatus(_A)
_COpticalMonLocation_Type=OpticalIfMonLocation
_COpticalMonLocation_Object=MibTableColumn
cOpticalMonLocation=_COpticalMonLocation_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,2),_COpticalMonLocation_Type())
cOpticalMonLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalMonLocation.setStatus(_A)
_COpticalMonParameterType_Type=OpticalParameterType
_COpticalMonParameterType_Object=MibTableColumn
cOpticalMonParameterType=_COpticalMonParameterType_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,3),_COpticalMonParameterType_Type())
cOpticalMonParameterType.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalMonParameterType.setStatus(_A)
_COpticalParameterValue_Type=OpticalParameterValue
_COpticalParameterValue_Object=MibTableColumn
cOpticalParameterValue=_COpticalParameterValue_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,4),_COpticalParameterValue_Type())
cOpticalParameterValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalParameterValue.setStatus(_A)
_COpticalParamHighAlarmThresh_Type=OpticalParameterValue
_COpticalParamHighAlarmThresh_Object=MibTableColumn
cOpticalParamHighAlarmThresh=_COpticalParamHighAlarmThresh_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,5),_COpticalParamHighAlarmThresh_Type())
cOpticalParamHighAlarmThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamHighAlarmThresh.setStatus(_A)
_COpticalParamHighAlarmSev_Type=OpticalAlarmSeverity
_COpticalParamHighAlarmSev_Object=MibTableColumn
cOpticalParamHighAlarmSev=_COpticalParamHighAlarmSev_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,6),_COpticalParamHighAlarmSev_Type())
cOpticalParamHighAlarmSev.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamHighAlarmSev.setStatus(_A)
_COpticalParamHighWarningThresh_Type=OpticalParameterValue
_COpticalParamHighWarningThresh_Object=MibTableColumn
cOpticalParamHighWarningThresh=_COpticalParamHighWarningThresh_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,7),_COpticalParamHighWarningThresh_Type())
cOpticalParamHighWarningThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamHighWarningThresh.setStatus(_A)
_COpticalParamHighWarningSev_Type=OpticalAlarmSeverity
_COpticalParamHighWarningSev_Object=MibTableColumn
cOpticalParamHighWarningSev=_COpticalParamHighWarningSev_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,8),_COpticalParamHighWarningSev_Type())
cOpticalParamHighWarningSev.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamHighWarningSev.setStatus(_A)
_COpticalParamLowAlarmThresh_Type=OpticalParameterValue
_COpticalParamLowAlarmThresh_Object=MibTableColumn
cOpticalParamLowAlarmThresh=_COpticalParamLowAlarmThresh_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,9),_COpticalParamLowAlarmThresh_Type())
cOpticalParamLowAlarmThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamLowAlarmThresh.setStatus(_A)
_COpticalParamLowAlarmSev_Type=OpticalAlarmSeverity
_COpticalParamLowAlarmSev_Object=MibTableColumn
cOpticalParamLowAlarmSev=_COpticalParamLowAlarmSev_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,10),_COpticalParamLowAlarmSev_Type())
cOpticalParamLowAlarmSev.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamLowAlarmSev.setStatus(_A)
_COpticalParamLowWarningThresh_Type=OpticalParameterValue
_COpticalParamLowWarningThresh_Object=MibTableColumn
cOpticalParamLowWarningThresh=_COpticalParamLowWarningThresh_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,11),_COpticalParamLowWarningThresh_Type())
cOpticalParamLowWarningThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamLowWarningThresh.setStatus(_A)
_COpticalParamLowWarningSev_Type=OpticalAlarmSeverity
_COpticalParamLowWarningSev_Object=MibTableColumn
cOpticalParamLowWarningSev=_COpticalParamLowWarningSev_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,12),_COpticalParamLowWarningSev_Type())
cOpticalParamLowWarningSev.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamLowWarningSev.setStatus(_A)
_COpticalParamAlarmStatus_Type=OpticalAlarmStatus
_COpticalParamAlarmStatus_Object=MibTableColumn
cOpticalParamAlarmStatus=_COpticalParamAlarmStatus_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,13),_COpticalParamAlarmStatus_Type())
cOpticalParamAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalParamAlarmStatus.setStatus(_A)
_COpticalParamAlarmCurMaxThresh_Type=OpticalParameterValue
_COpticalParamAlarmCurMaxThresh_Object=MibTableColumn
cOpticalParamAlarmCurMaxThresh=_COpticalParamAlarmCurMaxThresh_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,14),_COpticalParamAlarmCurMaxThresh_Type())
cOpticalParamAlarmCurMaxThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalParamAlarmCurMaxThresh.setStatus(_A)
_COpticalParamAlarmCurMaxSev_Type=OpticalAlarmSeverity
_COpticalParamAlarmCurMaxSev_Object=MibTableColumn
cOpticalParamAlarmCurMaxSev=_COpticalParamAlarmCurMaxSev_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,15),_COpticalParamAlarmCurMaxSev_Type())
cOpticalParamAlarmCurMaxSev.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalParamAlarmCurMaxSev.setStatus(_A)
_COpticalParamAlarmLastChange_Type=TimeStamp
_COpticalParamAlarmLastChange_Object=MibTableColumn
cOpticalParamAlarmLastChange=_COpticalParamAlarmLastChange_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,16),_COpticalParamAlarmLastChange_Type())
cOpticalParamAlarmLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalParamAlarmLastChange.setStatus(_A)
class _COpticalMon15MinValidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_COpticalMon15MinValidIntervals_Type.__name__=_J
_COpticalMon15MinValidIntervals_Object=MibTableColumn
cOpticalMon15MinValidIntervals=_COpticalMon15MinValidIntervals_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,17),_COpticalMon15MinValidIntervals_Type())
cOpticalMon15MinValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalMon15MinValidIntervals.setStatus(_A)
class _COpticalMon24HrValidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_COpticalMon24HrValidIntervals_Type.__name__=_J
_COpticalMon24HrValidIntervals_Object=MibTableColumn
cOpticalMon24HrValidIntervals=_COpticalMon24HrValidIntervals_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,18),_COpticalMon24HrValidIntervals_Type())
cOpticalMon24HrValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalMon24HrValidIntervals.setStatus(_A)
class _COpticalParamThreshSource_Type(Bits):namedValues=NamedValues(*(('highAlarmDefThresh',0),('highWarnDefThresh',1),('lowAlarmDefThresh',2),('lowWarnDefThresh',3)))
_COpticalParamThreshSource_Type.__name__=_I
_COpticalParamThreshSource_Object=MibTableColumn
cOpticalParamThreshSource=_COpticalParamThreshSource_Object((1,3,6,1,4,1,9,9,264,1,1,1,1,19),_COpticalParamThreshSource_Type())
cOpticalParamThreshSource.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamThreshSource.setStatus(_A)
class _COpticalNotifyEnable_Type(OpticalAlarmSeverityOrZero):defaultValue=0
_COpticalNotifyEnable_Type.__name__=_Z
_COpticalNotifyEnable_Object=MibScalar
cOpticalNotifyEnable=_COpticalNotifyEnable_Object((1,3,6,1,4,1,9,9,264,1,1,2),_COpticalNotifyEnable_Type())
cOpticalNotifyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalNotifyEnable.setStatus(_A)
class _COpticalMonEnable_Type(Bits):namedValues=NamedValues(('all',0))
_COpticalMonEnable_Type.__name__=_I
_COpticalMonEnable_Object=MibScalar
cOpticalMonEnable=_COpticalMonEnable_Object((1,3,6,1,4,1,9,9,264,1,1,3),_COpticalMonEnable_Type())
cOpticalMonEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalMonEnable.setStatus(_A)
_COpticalMonPollInterval_Type=Unsigned32
_COpticalMonPollInterval_Object=MibScalar
cOpticalMonPollInterval=_COpticalMonPollInterval_Object((1,3,6,1,4,1,9,9,264,1,1,4),_COpticalMonPollInterval_Type())
cOpticalMonPollInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalMonPollInterval.setStatus(_A)
if mibBuilder.loadTexts:cOpticalMonPollInterval.setUnits('minutes')
_COpticalMonIfTable_Object=MibTable
cOpticalMonIfTable=_COpticalMonIfTable_Object((1,3,6,1,4,1,9,9,264,1,1,5))
if mibBuilder.loadTexts:cOpticalMonIfTable.setStatus(_A)
_COpticalMonIfEntry_Object=MibTableRow
cOpticalMonIfEntry=_COpticalMonIfEntry_Object((1,3,6,1,4,1,9,9,264,1,1,5,1))
cOpticalMonIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cOpticalMonIfEntry.setStatus(_A)
_COpticalMonIfTimeInSlot_Type=Unsigned32
_COpticalMonIfTimeInSlot_Object=MibTableColumn
cOpticalMonIfTimeInSlot=_COpticalMonIfTimeInSlot_Object((1,3,6,1,4,1,9,9,264,1,1,5,1,1),_COpticalMonIfTimeInSlot_Type())
cOpticalMonIfTimeInSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalMonIfTimeInSlot.setStatus(_A)
if mibBuilder.loadTexts:cOpticalMonIfTimeInSlot.setUnits('seconds')
_COpticalPMGroup_ObjectIdentity=ObjectIdentity
cOpticalPMGroup=_COpticalPMGroup_ObjectIdentity((1,3,6,1,4,1,9,9,264,1,2))
_COpticalPMCurrentTable_Object=MibTable
cOpticalPMCurrentTable=_COpticalPMCurrentTable_Object((1,3,6,1,4,1,9,9,264,1,2,1))
if mibBuilder.loadTexts:cOpticalPMCurrentTable.setStatus(_A)
_COpticalPMCurrentEntry_Object=MibTableRow
cOpticalPMCurrentEntry=_COpticalPMCurrentEntry_Object((1,3,6,1,4,1,9,9,264,1,2,1,1))
cOpticalPMCurrentEntry.setIndexNames((0,_B,_a),(0,_F,_G),(0,_B,_b),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:cOpticalPMCurrentEntry.setStatus(_A)
_COpticalPMCurrentPeriod_Type=OpticalPMPeriod
_COpticalPMCurrentPeriod_Object=MibTableColumn
cOpticalPMCurrentPeriod=_COpticalPMCurrentPeriod_Object((1,3,6,1,4,1,9,9,264,1,2,1,1,1),_COpticalPMCurrentPeriod_Type())
cOpticalPMCurrentPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMCurrentPeriod.setStatus(_A)
_COpticalPMCurrentDirection_Type=OpticalIfDirection
_COpticalPMCurrentDirection_Object=MibTableColumn
cOpticalPMCurrentDirection=_COpticalPMCurrentDirection_Object((1,3,6,1,4,1,9,9,264,1,2,1,1,2),_COpticalPMCurrentDirection_Type())
cOpticalPMCurrentDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMCurrentDirection.setStatus(_A)
_COpticalPMCurrentLocation_Type=OpticalIfMonLocation
_COpticalPMCurrentLocation_Object=MibTableColumn
cOpticalPMCurrentLocation=_COpticalPMCurrentLocation_Object((1,3,6,1,4,1,9,9,264,1,2,1,1,3),_COpticalPMCurrentLocation_Type())
cOpticalPMCurrentLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMCurrentLocation.setStatus(_A)
_COpticalPMCurrentParamType_Type=OpticalParameterType
_COpticalPMCurrentParamType_Object=MibTableColumn
cOpticalPMCurrentParamType=_COpticalPMCurrentParamType_Object((1,3,6,1,4,1,9,9,264,1,2,1,1,4),_COpticalPMCurrentParamType_Type())
cOpticalPMCurrentParamType.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMCurrentParamType.setStatus(_A)
_COpticalPMCurrentMaxParam_Type=OpticalParameterValue
_COpticalPMCurrentMaxParam_Object=MibTableColumn
cOpticalPMCurrentMaxParam=_COpticalPMCurrentMaxParam_Object((1,3,6,1,4,1,9,9,264,1,2,1,1,5),_COpticalPMCurrentMaxParam_Type())
cOpticalPMCurrentMaxParam.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMCurrentMaxParam.setStatus(_A)
_COpticalPMCurrentMinParam_Type=OpticalParameterValue
_COpticalPMCurrentMinParam_Object=MibTableColumn
cOpticalPMCurrentMinParam=_COpticalPMCurrentMinParam_Object((1,3,6,1,4,1,9,9,264,1,2,1,1,6),_COpticalPMCurrentMinParam_Type())
cOpticalPMCurrentMinParam.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMCurrentMinParam.setStatus(_A)
_COpticalPMCurrentMeanParam_Type=OpticalParameterValue
_COpticalPMCurrentMeanParam_Object=MibTableColumn
cOpticalPMCurrentMeanParam=_COpticalPMCurrentMeanParam_Object((1,3,6,1,4,1,9,9,264,1,2,1,1,7),_COpticalPMCurrentMeanParam_Type())
cOpticalPMCurrentMeanParam.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMCurrentMeanParam.setStatus(_A)
class _COpticalPMCurrentUnavailSecs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_COpticalPMCurrentUnavailSecs_Type.__name__=_H
_COpticalPMCurrentUnavailSecs_Object=MibTableColumn
cOpticalPMCurrentUnavailSecs=_COpticalPMCurrentUnavailSecs_Object((1,3,6,1,4,1,9,9,264,1,2,1,1,8),_COpticalPMCurrentUnavailSecs_Type())
cOpticalPMCurrentUnavailSecs.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMCurrentUnavailSecs.setStatus(_A)
_COpticalPMIntervalTable_Object=MibTable
cOpticalPMIntervalTable=_COpticalPMIntervalTable_Object((1,3,6,1,4,1,9,9,264,1,2,2))
if mibBuilder.loadTexts:cOpticalPMIntervalTable.setStatus(_A)
_COpticalPMIntervalEntry_Object=MibTableRow
cOpticalPMIntervalEntry=_COpticalPMIntervalEntry_Object((1,3,6,1,4,1,9,9,264,1,2,2,1))
cOpticalPMIntervalEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_F,_G),(0,_B,_g),(0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:cOpticalPMIntervalEntry.setStatus(_A)
_COpticalPMIntervalPeriod_Type=OpticalPMPeriod
_COpticalPMIntervalPeriod_Object=MibTableColumn
cOpticalPMIntervalPeriod=_COpticalPMIntervalPeriod_Object((1,3,6,1,4,1,9,9,264,1,2,2,1,1),_COpticalPMIntervalPeriod_Type())
cOpticalPMIntervalPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMIntervalPeriod.setStatus(_A)
class _COpticalPMIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_COpticalPMIntervalNumber_Type.__name__=_H
_COpticalPMIntervalNumber_Object=MibTableColumn
cOpticalPMIntervalNumber=_COpticalPMIntervalNumber_Object((1,3,6,1,4,1,9,9,264,1,2,2,1,2),_COpticalPMIntervalNumber_Type())
cOpticalPMIntervalNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMIntervalNumber.setStatus(_A)
_COpticalPMIntervalDirection_Type=OpticalIfDirection
_COpticalPMIntervalDirection_Object=MibTableColumn
cOpticalPMIntervalDirection=_COpticalPMIntervalDirection_Object((1,3,6,1,4,1,9,9,264,1,2,2,1,3),_COpticalPMIntervalDirection_Type())
cOpticalPMIntervalDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMIntervalDirection.setStatus(_A)
_COpticalPMIntervalLocation_Type=OpticalIfMonLocation
_COpticalPMIntervalLocation_Object=MibTableColumn
cOpticalPMIntervalLocation=_COpticalPMIntervalLocation_Object((1,3,6,1,4,1,9,9,264,1,2,2,1,4),_COpticalPMIntervalLocation_Type())
cOpticalPMIntervalLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMIntervalLocation.setStatus(_A)
_COpticalPMIntervalParamType_Type=OpticalParameterType
_COpticalPMIntervalParamType_Object=MibTableColumn
cOpticalPMIntervalParamType=_COpticalPMIntervalParamType_Object((1,3,6,1,4,1,9,9,264,1,2,2,1,5),_COpticalPMIntervalParamType_Type())
cOpticalPMIntervalParamType.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMIntervalParamType.setStatus(_A)
_COpticalPMIntervalMaxParam_Type=OpticalParameterValue
_COpticalPMIntervalMaxParam_Object=MibTableColumn
cOpticalPMIntervalMaxParam=_COpticalPMIntervalMaxParam_Object((1,3,6,1,4,1,9,9,264,1,2,2,1,6),_COpticalPMIntervalMaxParam_Type())
cOpticalPMIntervalMaxParam.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMIntervalMaxParam.setStatus(_A)
_COpticalPMIntervalMinParam_Type=OpticalParameterValue
_COpticalPMIntervalMinParam_Object=MibTableColumn
cOpticalPMIntervalMinParam=_COpticalPMIntervalMinParam_Object((1,3,6,1,4,1,9,9,264,1,2,2,1,7),_COpticalPMIntervalMinParam_Type())
cOpticalPMIntervalMinParam.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMIntervalMinParam.setStatus(_A)
_COpticalPMIntervalMeanParam_Type=OpticalParameterValue
_COpticalPMIntervalMeanParam_Object=MibTableColumn
cOpticalPMIntervalMeanParam=_COpticalPMIntervalMeanParam_Object((1,3,6,1,4,1,9,9,264,1,2,2,1,8),_COpticalPMIntervalMeanParam_Type())
cOpticalPMIntervalMeanParam.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMIntervalMeanParam.setStatus(_A)
class _COpticalPMIntervalUnavailSecs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_COpticalPMIntervalUnavailSecs_Type.__name__=_H
_COpticalPMIntervalUnavailSecs_Object=MibTableColumn
cOpticalPMIntervalUnavailSecs=_COpticalPMIntervalUnavailSecs_Object((1,3,6,1,4,1,9,9,264,1,2,2,1,9),_COpticalPMIntervalUnavailSecs_Type())
cOpticalPMIntervalUnavailSecs.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMIntervalUnavailSecs.setStatus(_A)
_COpticalMonitorMIBNotifications_ObjectIdentity=ObjectIdentity
cOpticalMonitorMIBNotifications=_COpticalMonitorMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,264,2))
_COpticalMonNotificationPrefix_ObjectIdentity=ObjectIdentity
cOpticalMonNotificationPrefix=_COpticalMonNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,264,2,0))
_COpticalMonitorMIBConformance_ObjectIdentity=ObjectIdentity
cOpticalMonitorMIBConformance=_COpticalMonitorMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,264,3))
_COpticalMonitorMIBCompliances_ObjectIdentity=ObjectIdentity
cOpticalMonitorMIBCompliances=_COpticalMonitorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,264,3,1))
_COpticalMonitorMIBGroups_ObjectIdentity=ObjectIdentity
cOpticalMonitorMIBGroups=_COpticalMonitorMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,264,3,2))
cOpticalMIBMonGroup=ObjectGroup((1,3,6,1,4,1,9,9,264,3,2,1))
cOpticalMIBMonGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:cOpticalMIBMonGroup.setStatus(_A)
cOpticalMIBThresholdGroup=ObjectGroup((1,3,6,1,4,1,9,9,264,3,2,2))
cOpticalMIBThresholdGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cOpticalMIBThresholdGroup.setStatus(_A)
cOpticalMIBSeverityGroup=ObjectGroup((1,3,6,1,4,1,9,9,264,3,2,3))
cOpticalMIBSeverityGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_O)))
if mibBuilder.loadTexts:cOpticalMIBSeverityGroup.setStatus(_A)
cOpticalMIBPMGroup=ObjectGroup((1,3,6,1,4,1,9,9,264,3,2,4))
cOpticalMIBPMGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cOpticalMIBPMGroup.setStatus(_A)
cOpticalMIBNotifyEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,264,3,2,5))
cOpticalMIBNotifyEnableGroup.setObjects((_B,_A1))
if mibBuilder.loadTexts:cOpticalMIBNotifyEnableGroup.setStatus(_A)
cOpticalMonIfTimeGroup=ObjectGroup((1,3,6,1,4,1,9,9,264,3,2,7))
cOpticalMonIfTimeGroup.setObjects((_B,_A2))
if mibBuilder.loadTexts:cOpticalMonIfTimeGroup.setStatus(_A)
cOpticalMIBEnableConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,264,3,2,8))
cOpticalMIBEnableConfigGroup.setObjects((_B,_A3))
if mibBuilder.loadTexts:cOpticalMIBEnableConfigGroup.setStatus(_A)
cOpticalMIBIntervalConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,264,3,2,9))
cOpticalMIBIntervalConfigGroup.setObjects((_B,_A4))
if mibBuilder.loadTexts:cOpticalMIBIntervalConfigGroup.setStatus(_A)
cOpticalMonThreshSourceGroup=ObjectGroup((1,3,6,1,4,1,9,9,264,3,2,10))
cOpticalMonThreshSourceGroup.setObjects((_B,_A5))
if mibBuilder.loadTexts:cOpticalMonThreshSourceGroup.setStatus(_A)
cOpticalMonParameterStatus=NotificationType((1,3,6,1,4,1,9,9,264,2,0,1))
cOpticalMonParameterStatus.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_O),(_B,_N)))
if mibBuilder.loadTexts:cOpticalMonParameterStatus.setStatus(_A)
cOpticalMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,264,3,2,6))
cOpticalMIBNotifGroup.setObjects((_B,_A6))
if mibBuilder.loadTexts:cOpticalMIBNotifGroup.setStatus(_A)
cOpticalMonitorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,264,3,1,1))
cOpticalMonitorMIBCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cOpticalMonitorMIBCompliance.setStatus('deprecated')
cOpticalMonitorMIBComplianceRev=ModuleCompliance((1,3,6,1,4,1,9,9,264,3,1,2))
cOpticalMonitorMIBComplianceRev.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_A7),(_B,_T),(_B,_U),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:cOpticalMonitorMIBComplianceRev.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OpticalParameterType':OpticalParameterType,'OpticalParameterValue':OpticalParameterValue,'OpticalIfDirection':OpticalIfDirection,'OpticalIfMonLocation':OpticalIfMonLocation,'OpticalAlarmStatus':OpticalAlarmStatus,'OpticalAlarmSeverity':OpticalAlarmSeverity,_Z:OpticalAlarmSeverityOrZero,'OpticalPMPeriod':OpticalPMPeriod,'ciscoOpticalMonitorMIB':ciscoOpticalMonitorMIB,'cOpticalMonitorMIBObjects':cOpticalMonitorMIBObjects,'cOpticalMonGroup':cOpticalMonGroup,'cOpticalMonTable':cOpticalMonTable,'cOpticalMonEntry':cOpticalMonEntry,_W:cOpticalMonDirection,_X:cOpticalMonLocation,_Y:cOpticalMonParameterType,_K:cOpticalParameterValue,_j:cOpticalParamHighAlarmThresh,_n:cOpticalParamHighAlarmSev,_k:cOpticalParamHighWarningThresh,_o:cOpticalParamHighWarningSev,_l:cOpticalParamLowAlarmThresh,_p:cOpticalParamLowAlarmSev,_m:cOpticalParamLowWarningThresh,_q:cOpticalParamLowWarningSev,_L:cOpticalParamAlarmStatus,_M:cOpticalParamAlarmCurMaxThresh,_O:cOpticalParamAlarmCurMaxSev,_N:cOpticalParamAlarmLastChange,_r:cOpticalMon15MinValidIntervals,_s:cOpticalMon24HrValidIntervals,_A5:cOpticalParamThreshSource,_A1:cOpticalNotifyEnable,_A3:cOpticalMonEnable,_A4:cOpticalMonPollInterval,'cOpticalMonIfTable':cOpticalMonIfTable,'cOpticalMonIfEntry':cOpticalMonIfEntry,_A2:cOpticalMonIfTimeInSlot,'cOpticalPMGroup':cOpticalPMGroup,'cOpticalPMCurrentTable':cOpticalPMCurrentTable,'cOpticalPMCurrentEntry':cOpticalPMCurrentEntry,_a:cOpticalPMCurrentPeriod,_b:cOpticalPMCurrentDirection,_c:cOpticalPMCurrentLocation,_d:cOpticalPMCurrentParamType,_t:cOpticalPMCurrentMaxParam,_u:cOpticalPMCurrentMinParam,_v:cOpticalPMCurrentMeanParam,_w:cOpticalPMCurrentUnavailSecs,'cOpticalPMIntervalTable':cOpticalPMIntervalTable,'cOpticalPMIntervalEntry':cOpticalPMIntervalEntry,_e:cOpticalPMIntervalPeriod,_f:cOpticalPMIntervalNumber,_g:cOpticalPMIntervalDirection,_h:cOpticalPMIntervalLocation,_i:cOpticalPMIntervalParamType,_x:cOpticalPMIntervalMaxParam,_y:cOpticalPMIntervalMinParam,_z:cOpticalPMIntervalMeanParam,_A0:cOpticalPMIntervalUnavailSecs,'cOpticalMonitorMIBNotifications':cOpticalMonitorMIBNotifications,'cOpticalMonNotificationPrefix':cOpticalMonNotificationPrefix,_A6:cOpticalMonParameterStatus,'cOpticalMonitorMIBConformance':cOpticalMonitorMIBConformance,'cOpticalMonitorMIBCompliances':cOpticalMonitorMIBCompliances,'cOpticalMonitorMIBCompliance':cOpticalMonitorMIBCompliance,'cOpticalMonitorMIBComplianceRev':cOpticalMonitorMIBComplianceRev,'cOpticalMonitorMIBGroups':cOpticalMonitorMIBGroups,_P:cOpticalMIBMonGroup,_Q:cOpticalMIBThresholdGroup,_R:cOpticalMIBSeverityGroup,_S:cOpticalMIBPMGroup,_T:cOpticalMIBNotifyEnableGroup,_U:cOpticalMIBNotifGroup,_A7:cOpticalMonIfTimeGroup,_A8:cOpticalMIBEnableConfigGroup,_A9:cOpticalMIBIntervalConfigGroup,_AA:cOpticalMonThreshSourceGroup})