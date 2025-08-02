_n='raisecomOpticalMIBNotifGroup'
_m='raisecomOpticalMIBNotifyEnableGroup'
_l='raisecomOpticalMIBPMGroup'
_k='raisecomOpticalMIBThresholdGroup'
_j='raisecomOpticalMIBMonGroup'
_i='raisecomOpticalMonParameterStatus'
_h='raisecomOpticalNotifyEnable'
_g='raisecomOpticalPMIntervalMeanParam'
_f='raisecomOpticalPMIntervalMinParam'
_e='raisecomOpticalPMIntervalMaxParam'
_d='raisecomOpticalPMCurrentMeanParam'
_c='raisecomOpticalPMCurrentMinParam'
_b='raisecomOpticalPMCurrentMaxParam'
_a='raisecomOpticalMon24HrValidIntervals'
_Z='raisecomOpticalMon15MinValidIntervals'
_Y='raisecomOpticalParamAlarmLastChange'
_X='raisecomOpticalParamAlarmLastValue'
_W='raisecomOpticalParamLowWarningThresh'
_V='raisecomOpticalParamLowAlarmThresh'
_U='raisecomOpticalParamHighWarningThresh'
_T='raisecomOpticalParamHighAlarmThresh'
_S='raisecomOpticalPMIntervalParamType'
_R='raisecomOpticalPMIntervalNumber'
_Q='raisecomOpticalPMIntervalPeriod'
_P='raisecomOpticalPMCurrentParamType'
_O='raisecomOpticalPMCurrentPeriod'
_N='read-write'
_M='raisecomOpticalMonParameterType'
_L='TimeTicks'
_K='raisecomOpticalParamAlarmStatus'
_J='raisecomOpticalParameterValue'
_I='EnableVar'
_H='Unsigned32'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='not-accessible'
_C='read-only'
_B='RAISECOM-OPTICAL-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,_H,'iso')
DisplayString,PhysAddress,TextualConvention,TimeTicks=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_L)
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_I)
raisecomOpticalMonitorMIB=ModuleIdentity((1,3,6,1,4,1,8886,1,9))
if mibBuilder.loadTexts:raisecomOpticalMonitorMIB.setRevisions(('2006-06-06 00:00',))
class OpticalParameterType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('temperature',1),('supplyVoltage',2),('biasCurrent',3),('txOutputPower',4),('receivedPower',5)))
class OpticalParameterValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000,65535))
class OpticalPMPeriod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMin',1),('twentyFourHour',2)))
_RaisecomOpticalMonitorMIBObjects_ObjectIdentity=ObjectIdentity
raisecomOpticalMonitorMIBObjects=_RaisecomOpticalMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,9,1))
_RaisecomOpticalMonGroup_ObjectIdentity=ObjectIdentity
raisecomOpticalMonGroup=_RaisecomOpticalMonGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,9,1,1))
_RaisecomOpticalMonTable_Object=MibTable
raisecomOpticalMonTable=_RaisecomOpticalMonTable_Object((1,3,6,1,4,1,8886,1,9,1,1,1))
if mibBuilder.loadTexts:raisecomOpticalMonTable.setStatus(_A)
_RaisecomOpticalMonEntry_Object=MibTableRow
raisecomOpticalMonEntry=_RaisecomOpticalMonEntry_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1))
raisecomOpticalMonEntry.setIndexNames((0,_E,_F),(0,_B,_M))
if mibBuilder.loadTexts:raisecomOpticalMonEntry.setStatus(_A)
_RaisecomOpticalMonParameterType_Type=OpticalParameterType
_RaisecomOpticalMonParameterType_Object=MibTableColumn
raisecomOpticalMonParameterType=_RaisecomOpticalMonParameterType_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,1),_RaisecomOpticalMonParameterType_Type())
raisecomOpticalMonParameterType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOpticalMonParameterType.setStatus(_A)
_RaisecomOpticalParameterValue_Type=OpticalParameterValue
_RaisecomOpticalParameterValue_Object=MibTableColumn
raisecomOpticalParameterValue=_RaisecomOpticalParameterValue_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,2),_RaisecomOpticalParameterValue_Type())
raisecomOpticalParameterValue.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalParameterValue.setStatus(_A)
_RaisecomOpticalParamHighAlarmThresh_Type=OpticalParameterValue
_RaisecomOpticalParamHighAlarmThresh_Object=MibTableColumn
raisecomOpticalParamHighAlarmThresh=_RaisecomOpticalParamHighAlarmThresh_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,3),_RaisecomOpticalParamHighAlarmThresh_Type())
raisecomOpticalParamHighAlarmThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalParamHighAlarmThresh.setStatus(_A)
_RaisecomOpticalParamHighWarningThresh_Type=OpticalParameterValue
_RaisecomOpticalParamHighWarningThresh_Object=MibTableColumn
raisecomOpticalParamHighWarningThresh=_RaisecomOpticalParamHighWarningThresh_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,4),_RaisecomOpticalParamHighWarningThresh_Type())
raisecomOpticalParamHighWarningThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalParamHighWarningThresh.setStatus(_A)
_RaisecomOpticalParamLowAlarmThresh_Type=OpticalParameterValue
_RaisecomOpticalParamLowAlarmThresh_Object=MibTableColumn
raisecomOpticalParamLowAlarmThresh=_RaisecomOpticalParamLowAlarmThresh_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,5),_RaisecomOpticalParamLowAlarmThresh_Type())
raisecomOpticalParamLowAlarmThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalParamLowAlarmThresh.setStatus(_A)
_RaisecomOpticalParamLowWarningThresh_Type=OpticalParameterValue
_RaisecomOpticalParamLowWarningThresh_Object=MibTableColumn
raisecomOpticalParamLowWarningThresh=_RaisecomOpticalParamLowWarningThresh_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,6),_RaisecomOpticalParamLowWarningThresh_Type())
raisecomOpticalParamLowWarningThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalParamLowWarningThresh.setStatus(_A)
class _RaisecomOpticalParamAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('high-alarm-threshold',1),('high-warning-threshold',2),('low-alarm-threshold',3),('low-warning-threshold',4)))
_RaisecomOpticalParamAlarmStatus_Type.__name__=_G
_RaisecomOpticalParamAlarmStatus_Object=MibTableColumn
raisecomOpticalParamAlarmStatus=_RaisecomOpticalParamAlarmStatus_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,7),_RaisecomOpticalParamAlarmStatus_Type())
raisecomOpticalParamAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalParamAlarmStatus.setStatus(_A)
_RaisecomOpticalParamAlarmLastValue_Type=OpticalParameterValue
_RaisecomOpticalParamAlarmLastValue_Object=MibTableColumn
raisecomOpticalParamAlarmLastValue=_RaisecomOpticalParamAlarmLastValue_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,8),_RaisecomOpticalParamAlarmLastValue_Type())
raisecomOpticalParamAlarmLastValue.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalParamAlarmLastValue.setStatus(_A)
_RaisecomOpticalParamAlarmLastChange_Type=TimeTicks
_RaisecomOpticalParamAlarmLastChange_Object=MibTableColumn
raisecomOpticalParamAlarmLastChange=_RaisecomOpticalParamAlarmLastChange_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,9),_RaisecomOpticalParamAlarmLastChange_Type())
raisecomOpticalParamAlarmLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalParamAlarmLastChange.setStatus(_A)
class _RaisecomOpticalMon15MinValidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_RaisecomOpticalMon15MinValidIntervals_Type.__name__=_H
_RaisecomOpticalMon15MinValidIntervals_Object=MibTableColumn
raisecomOpticalMon15MinValidIntervals=_RaisecomOpticalMon15MinValidIntervals_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,10),_RaisecomOpticalMon15MinValidIntervals_Type())
raisecomOpticalMon15MinValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalMon15MinValidIntervals.setStatus(_A)
class _RaisecomOpticalMon24HrValidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_RaisecomOpticalMon24HrValidIntervals_Type.__name__=_H
_RaisecomOpticalMon24HrValidIntervals_Object=MibTableColumn
raisecomOpticalMon24HrValidIntervals=_RaisecomOpticalMon24HrValidIntervals_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,11),_RaisecomOpticalMon24HrValidIntervals_Type())
raisecomOpticalMon24HrValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalMon24HrValidIntervals.setStatus(_A)
class _RaisecomOpticalMonValidStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_RaisecomOpticalMonValidStatus_Type.__name__=_G
_RaisecomOpticalMonValidStatus_Object=MibTableColumn
raisecomOpticalMonValidStatus=_RaisecomOpticalMonValidStatus_Object((1,3,6,1,4,1,8886,1,9,1,1,1,1,12),_RaisecomOpticalMonValidStatus_Type())
raisecomOpticalMonValidStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalMonValidStatus.setStatus(_A)
class _RaisecomOpticalNotifyEnable_Type(EnableVar):defaultValue=1
_RaisecomOpticalNotifyEnable_Type.__name__=_I
_RaisecomOpticalNotifyEnable_Object=MibScalar
raisecomOpticalNotifyEnable=_RaisecomOpticalNotifyEnable_Object((1,3,6,1,4,1,8886,1,9,1,1,2),_RaisecomOpticalNotifyEnable_Type())
raisecomOpticalNotifyEnable.setMaxAccess(_N)
if mibBuilder.loadTexts:raisecomOpticalNotifyEnable.setStatus(_A)
class _RaisecomOpticalDigitalDiagnoticEnable_Type(EnableVar):defaultValue=2
_RaisecomOpticalDigitalDiagnoticEnable_Type.__name__=_I
_RaisecomOpticalDigitalDiagnoticEnable_Object=MibScalar
raisecomOpticalDigitalDiagnoticEnable=_RaisecomOpticalDigitalDiagnoticEnable_Object((1,3,6,1,4,1,8886,1,9,1,1,3),_RaisecomOpticalDigitalDiagnoticEnable_Type())
raisecomOpticalDigitalDiagnoticEnable.setMaxAccess(_N)
if mibBuilder.loadTexts:raisecomOpticalDigitalDiagnoticEnable.setStatus(_A)
_RaisecomOpticalPMGroup_ObjectIdentity=ObjectIdentity
raisecomOpticalPMGroup=_RaisecomOpticalPMGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,9,1,2))
_RaisecomOpticalPMCurrentTable_Object=MibTable
raisecomOpticalPMCurrentTable=_RaisecomOpticalPMCurrentTable_Object((1,3,6,1,4,1,8886,1,9,1,2,1))
if mibBuilder.loadTexts:raisecomOpticalPMCurrentTable.setStatus(_A)
_RaisecomOpticalPMCurrentEntry_Object=MibTableRow
raisecomOpticalPMCurrentEntry=_RaisecomOpticalPMCurrentEntry_Object((1,3,6,1,4,1,8886,1,9,1,2,1,1))
raisecomOpticalPMCurrentEntry.setIndexNames((0,_E,_F),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:raisecomOpticalPMCurrentEntry.setStatus(_A)
_RaisecomOpticalPMCurrentPeriod_Type=OpticalPMPeriod
_RaisecomOpticalPMCurrentPeriod_Object=MibTableColumn
raisecomOpticalPMCurrentPeriod=_RaisecomOpticalPMCurrentPeriod_Object((1,3,6,1,4,1,8886,1,9,1,2,1,1,1),_RaisecomOpticalPMCurrentPeriod_Type())
raisecomOpticalPMCurrentPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOpticalPMCurrentPeriod.setStatus(_A)
_RaisecomOpticalPMCurrentParamType_Type=OpticalParameterType
_RaisecomOpticalPMCurrentParamType_Object=MibTableColumn
raisecomOpticalPMCurrentParamType=_RaisecomOpticalPMCurrentParamType_Object((1,3,6,1,4,1,8886,1,9,1,2,1,1,2),_RaisecomOpticalPMCurrentParamType_Type())
raisecomOpticalPMCurrentParamType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOpticalPMCurrentParamType.setStatus(_A)
_RaisecomOpticalPMCurrentMaxParam_Type=OpticalParameterValue
_RaisecomOpticalPMCurrentMaxParam_Object=MibTableColumn
raisecomOpticalPMCurrentMaxParam=_RaisecomOpticalPMCurrentMaxParam_Object((1,3,6,1,4,1,8886,1,9,1,2,1,1,3),_RaisecomOpticalPMCurrentMaxParam_Type())
raisecomOpticalPMCurrentMaxParam.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalPMCurrentMaxParam.setStatus(_A)
_RaisecomOpticalPMCurrentMinParam_Type=OpticalParameterValue
_RaisecomOpticalPMCurrentMinParam_Object=MibTableColumn
raisecomOpticalPMCurrentMinParam=_RaisecomOpticalPMCurrentMinParam_Object((1,3,6,1,4,1,8886,1,9,1,2,1,1,4),_RaisecomOpticalPMCurrentMinParam_Type())
raisecomOpticalPMCurrentMinParam.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalPMCurrentMinParam.setStatus(_A)
_RaisecomOpticalPMCurrentMeanParam_Type=OpticalParameterValue
_RaisecomOpticalPMCurrentMeanParam_Object=MibTableColumn
raisecomOpticalPMCurrentMeanParam=_RaisecomOpticalPMCurrentMeanParam_Object((1,3,6,1,4,1,8886,1,9,1,2,1,1,5),_RaisecomOpticalPMCurrentMeanParam_Type())
raisecomOpticalPMCurrentMeanParam.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalPMCurrentMeanParam.setStatus(_A)
_RaisecomOpticalPMIntervalTable_Object=MibTable
raisecomOpticalPMIntervalTable=_RaisecomOpticalPMIntervalTable_Object((1,3,6,1,4,1,8886,1,9,1,2,2))
if mibBuilder.loadTexts:raisecomOpticalPMIntervalTable.setStatus(_A)
_RaisecomOpticalPMIntervalEntry_Object=MibTableRow
raisecomOpticalPMIntervalEntry=_RaisecomOpticalPMIntervalEntry_Object((1,3,6,1,4,1,8886,1,9,1,2,2,1))
raisecomOpticalPMIntervalEntry.setIndexNames((0,_E,_F),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:raisecomOpticalPMIntervalEntry.setStatus(_A)
_RaisecomOpticalPMIntervalPeriod_Type=OpticalPMPeriod
_RaisecomOpticalPMIntervalPeriod_Object=MibTableColumn
raisecomOpticalPMIntervalPeriod=_RaisecomOpticalPMIntervalPeriod_Object((1,3,6,1,4,1,8886,1,9,1,2,2,1,1),_RaisecomOpticalPMIntervalPeriod_Type())
raisecomOpticalPMIntervalPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOpticalPMIntervalPeriod.setStatus(_A)
class _RaisecomOpticalPMIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_RaisecomOpticalPMIntervalNumber_Type.__name__=_G
_RaisecomOpticalPMIntervalNumber_Object=MibTableColumn
raisecomOpticalPMIntervalNumber=_RaisecomOpticalPMIntervalNumber_Object((1,3,6,1,4,1,8886,1,9,1,2,2,1,2),_RaisecomOpticalPMIntervalNumber_Type())
raisecomOpticalPMIntervalNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOpticalPMIntervalNumber.setStatus(_A)
_RaisecomOpticalPMIntervalParamType_Type=OpticalParameterType
_RaisecomOpticalPMIntervalParamType_Object=MibTableColumn
raisecomOpticalPMIntervalParamType=_RaisecomOpticalPMIntervalParamType_Object((1,3,6,1,4,1,8886,1,9,1,2,2,1,3),_RaisecomOpticalPMIntervalParamType_Type())
raisecomOpticalPMIntervalParamType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOpticalPMIntervalParamType.setStatus(_A)
_RaisecomOpticalPMIntervalMaxParam_Type=OpticalParameterValue
_RaisecomOpticalPMIntervalMaxParam_Object=MibTableColumn
raisecomOpticalPMIntervalMaxParam=_RaisecomOpticalPMIntervalMaxParam_Object((1,3,6,1,4,1,8886,1,9,1,2,2,1,4),_RaisecomOpticalPMIntervalMaxParam_Type())
raisecomOpticalPMIntervalMaxParam.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalPMIntervalMaxParam.setStatus(_A)
_RaisecomOpticalPMIntervalMinParam_Type=OpticalParameterValue
_RaisecomOpticalPMIntervalMinParam_Object=MibTableColumn
raisecomOpticalPMIntervalMinParam=_RaisecomOpticalPMIntervalMinParam_Object((1,3,6,1,4,1,8886,1,9,1,2,2,1,5),_RaisecomOpticalPMIntervalMinParam_Type())
raisecomOpticalPMIntervalMinParam.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalPMIntervalMinParam.setStatus(_A)
_RaisecomOpticalPMIntervalMeanParam_Type=OpticalParameterValue
_RaisecomOpticalPMIntervalMeanParam_Object=MibTableColumn
raisecomOpticalPMIntervalMeanParam=_RaisecomOpticalPMIntervalMeanParam_Object((1,3,6,1,4,1,8886,1,9,1,2,2,1,6),_RaisecomOpticalPMIntervalMeanParam_Type())
raisecomOpticalPMIntervalMeanParam.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOpticalPMIntervalMeanParam.setStatus(_A)
_RaisecomTranceiverInfoTable_Object=MibTable
raisecomTranceiverInfoTable=_RaisecomTranceiverInfoTable_Object((1,3,6,1,4,1,8886,1,9,1,4))
if mibBuilder.loadTexts:raisecomTranceiverInfoTable.setStatus(_A)
_RaisecomTranceiverInfoEntry_Object=MibTableRow
raisecomTranceiverInfoEntry=_RaisecomTranceiverInfoEntry_Object((1,3,6,1,4,1,8886,1,9,1,4,1))
raisecomTranceiverInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomTranceiverInfoEntry.setStatus(_A)
_RaisecomTranceiverType_Type=OctetString
_RaisecomTranceiverType_Object=MibTableColumn
raisecomTranceiverType=_RaisecomTranceiverType_Object((1,3,6,1,4,1,8886,1,9,1,4,1,1),_RaisecomTranceiverType_Type())
raisecomTranceiverType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomTranceiverType.setStatus(_A)
_RaisecomTranceiverConnectorType_Type=OctetString
_RaisecomTranceiverConnectorType_Object=MibTableColumn
raisecomTranceiverConnectorType=_RaisecomTranceiverConnectorType_Object((1,3,6,1,4,1,8886,1,9,1,4,1,2),_RaisecomTranceiverConnectorType_Type())
raisecomTranceiverConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomTranceiverConnectorType.setStatus(_A)
_RaisecomTranceiverWavelength_Type=Integer32
_RaisecomTranceiverWavelength_Object=MibTableColumn
raisecomTranceiverWavelength=_RaisecomTranceiverWavelength_Object((1,3,6,1,4,1,8886,1,9,1,4,1,3),_RaisecomTranceiverWavelength_Type())
raisecomTranceiverWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomTranceiverWavelength.setStatus(_A)
_RaisecomTranceiverVendorName_Type=OctetString
_RaisecomTranceiverVendorName_Object=MibTableColumn
raisecomTranceiverVendorName=_RaisecomTranceiverVendorName_Object((1,3,6,1,4,1,8886,1,9,1,4,1,4),_RaisecomTranceiverVendorName_Type())
raisecomTranceiverVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomTranceiverVendorName.setStatus(_A)
_RaisecomTranceiverVendorPN_Type=OctetString
_RaisecomTranceiverVendorPN_Object=MibTableColumn
raisecomTranceiverVendorPN=_RaisecomTranceiverVendorPN_Object((1,3,6,1,4,1,8886,1,9,1,4,1,5),_RaisecomTranceiverVendorPN_Type())
raisecomTranceiverVendorPN.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomTranceiverVendorPN.setStatus(_A)
_RaisecomTranceiverVendorSN_Type=OctetString
_RaisecomTranceiverVendorSN_Object=MibTableColumn
raisecomTranceiverVendorSN=_RaisecomTranceiverVendorSN_Object((1,3,6,1,4,1,8886,1,9,1,4,1,6),_RaisecomTranceiverVendorSN_Type())
raisecomTranceiverVendorSN.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomTranceiverVendorSN.setStatus(_A)
class _RaisecomTransceiverFiberType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('single-mode',1),('multi-mode',2),('none',3)))
_RaisecomTransceiverFiberType_Type.__name__=_G
_RaisecomTransceiverFiberType_Object=MibTableColumn
raisecomTransceiverFiberType=_RaisecomTransceiverFiberType_Object((1,3,6,1,4,1,8886,1,9,1,4,1,7),_RaisecomTransceiverFiberType_Type())
raisecomTransceiverFiberType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomTransceiverFiberType.setStatus(_A)
_RaisecomTransceiverTransferDistance_Type=Integer32
_RaisecomTransceiverTransferDistance_Object=MibTableColumn
raisecomTransceiverTransferDistance=_RaisecomTransceiverTransferDistance_Object((1,3,6,1,4,1,8886,1,9,1,4,1,8),_RaisecomTransceiverTransferDistance_Type())
raisecomTransceiverTransferDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomTransceiverTransferDistance.setStatus(_A)
_RaisecomOpticalMonitorMIBNotifications_ObjectIdentity=ObjectIdentity
raisecomOpticalMonitorMIBNotifications=_RaisecomOpticalMonitorMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8886,1,9,2))
_RaisecomOpticalMonitorMIBConformance_ObjectIdentity=ObjectIdentity
raisecomOpticalMonitorMIBConformance=_RaisecomOpticalMonitorMIBConformance_ObjectIdentity((1,3,6,1,4,1,8886,1,9,3))
_RaisecomOpticalMonitorMIBCompliances_ObjectIdentity=ObjectIdentity
raisecomOpticalMonitorMIBCompliances=_RaisecomOpticalMonitorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8886,1,9,3,1))
_RaisecomOpticalMonitorMIBGroups_ObjectIdentity=ObjectIdentity
raisecomOpticalMonitorMIBGroups=_RaisecomOpticalMonitorMIBGroups_ObjectIdentity((1,3,6,1,4,1,8886,1,9,3,2))
raisecomOpticalMIBMonGroup=ObjectGroup((1,3,6,1,4,1,8886,1,9,3,2,1))
raisecomOpticalMIBMonGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:raisecomOpticalMIBMonGroup.setStatus(_A)
raisecomOpticalMIBThresholdGroup=ObjectGroup((1,3,6,1,4,1,8886,1,9,3,2,2))
raisecomOpticalMIBThresholdGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_K),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:raisecomOpticalMIBThresholdGroup.setStatus(_A)
raisecomOpticalMIBPMGroup=ObjectGroup((1,3,6,1,4,1,8886,1,9,3,2,3))
raisecomOpticalMIBPMGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:raisecomOpticalMIBPMGroup.setStatus(_A)
raisecomOpticalMIBNotifyEnableGroup=ObjectGroup((1,3,6,1,4,1,8886,1,9,3,2,4))
raisecomOpticalMIBNotifyEnableGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:raisecomOpticalMIBNotifyEnableGroup.setStatus(_A)
raisecomOpticalMonParameterStatus=NotificationType((1,3,6,1,4,1,8886,1,9,2,1))
raisecomOpticalMonParameterStatus.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:raisecomOpticalMonParameterStatus.setStatus(_A)
raisecomOpticalMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,8886,1,9,3,2,5))
raisecomOpticalMIBNotifGroup.setObjects((_B,_i))
if mibBuilder.loadTexts:raisecomOpticalMIBNotifGroup.setStatus(_A)
raisecomOpticalMonitorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8886,1,9,3,1,1))
raisecomOpticalMonitorMIBCompliance.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:raisecomOpticalMonitorMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OpticalParameterType':OpticalParameterType,'OpticalParameterValue':OpticalParameterValue,'OpticalPMPeriod':OpticalPMPeriod,'raisecomOpticalMonitorMIB':raisecomOpticalMonitorMIB,'raisecomOpticalMonitorMIBObjects':raisecomOpticalMonitorMIBObjects,'raisecomOpticalMonGroup':raisecomOpticalMonGroup,'raisecomOpticalMonTable':raisecomOpticalMonTable,'raisecomOpticalMonEntry':raisecomOpticalMonEntry,_M:raisecomOpticalMonParameterType,_J:raisecomOpticalParameterValue,_T:raisecomOpticalParamHighAlarmThresh,_U:raisecomOpticalParamHighWarningThresh,_V:raisecomOpticalParamLowAlarmThresh,_W:raisecomOpticalParamLowWarningThresh,_K:raisecomOpticalParamAlarmStatus,_X:raisecomOpticalParamAlarmLastValue,_Y:raisecomOpticalParamAlarmLastChange,_Z:raisecomOpticalMon15MinValidIntervals,_a:raisecomOpticalMon24HrValidIntervals,'raisecomOpticalMonValidStatus':raisecomOpticalMonValidStatus,_h:raisecomOpticalNotifyEnable,'raisecomOpticalDigitalDiagnoticEnable':raisecomOpticalDigitalDiagnoticEnable,'raisecomOpticalPMGroup':raisecomOpticalPMGroup,'raisecomOpticalPMCurrentTable':raisecomOpticalPMCurrentTable,'raisecomOpticalPMCurrentEntry':raisecomOpticalPMCurrentEntry,_O:raisecomOpticalPMCurrentPeriod,_P:raisecomOpticalPMCurrentParamType,_b:raisecomOpticalPMCurrentMaxParam,_c:raisecomOpticalPMCurrentMinParam,_d:raisecomOpticalPMCurrentMeanParam,'raisecomOpticalPMIntervalTable':raisecomOpticalPMIntervalTable,'raisecomOpticalPMIntervalEntry':raisecomOpticalPMIntervalEntry,_Q:raisecomOpticalPMIntervalPeriod,_R:raisecomOpticalPMIntervalNumber,_S:raisecomOpticalPMIntervalParamType,_e:raisecomOpticalPMIntervalMaxParam,_f:raisecomOpticalPMIntervalMinParam,_g:raisecomOpticalPMIntervalMeanParam,'raisecomTranceiverInfoTable':raisecomTranceiverInfoTable,'raisecomTranceiverInfoEntry':raisecomTranceiverInfoEntry,'raisecomTranceiverType':raisecomTranceiverType,'raisecomTranceiverConnectorType':raisecomTranceiverConnectorType,'raisecomTranceiverWavelength':raisecomTranceiverWavelength,'raisecomTranceiverVendorName':raisecomTranceiverVendorName,'raisecomTranceiverVendorPN':raisecomTranceiverVendorPN,'raisecomTranceiverVendorSN':raisecomTranceiverVendorSN,'raisecomTransceiverFiberType':raisecomTransceiverFiberType,'raisecomTransceiverTransferDistance':raisecomTransceiverTransferDistance,'raisecomOpticalMonitorMIBNotifications':raisecomOpticalMonitorMIBNotifications,_i:raisecomOpticalMonParameterStatus,'raisecomOpticalMonitorMIBConformance':raisecomOpticalMonitorMIBConformance,'raisecomOpticalMonitorMIBCompliances':raisecomOpticalMonitorMIBCompliances,'raisecomOpticalMonitorMIBCompliance':raisecomOpticalMonitorMIBCompliance,'raisecomOpticalMonitorMIBGroups':raisecomOpticalMonitorMIBGroups,_j:raisecomOpticalMIBMonGroup,_k:raisecomOpticalMIBThresholdGroup,_l:raisecomOpticalMIBPMGroup,_m:raisecomOpticalMIBNotifyEnableGroup,_n:raisecomOpticalMIBNotifGroup})