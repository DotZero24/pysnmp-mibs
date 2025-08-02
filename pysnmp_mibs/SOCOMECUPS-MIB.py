_p='upsTestElapsedTime'
_o='upsTestStartTime'
_n='upsTestResultsDetail'
_m='upsTestResultsSummary'
_l='upsTestSpinLock'
_k='upsTestId'
_j='upsSecondsOnBattery'
_i='upsEstimatedMinutesRemaining'
_h='indexOfDevice'
_g='upsControlEcoModeIndex'
_f='upsControlSpecialIndex'
_e='upsControlWeeklyIndex'
_d='upsControlEventDescr'
_c='disable'
_b='enable'
_a='upsBypassLineIndex'
_Z='upsOutputLineIndex'
_Y='upsInputLineIndex'
_X='unknown'
_W='NotificationType'
_V='upsAlarmDescr'
_U='trapsIndex'
_T='disabled'
_S='enabled'
_R='clear'
_Q='saturday'
_P='friday'
_O='thursday'
_N='wednesday'
_M='tuesday'
_L='monday'
_K='sunday'
_J='upsAlarmId'
_I='none'
_H='nothing'
_G='DisplayString'
_F='upsAgentTrapString'
_E='Integer32'
_D='read-write'
_C='SOCOMECUPS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_W,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_W,'TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TestAndIncr,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_G,'PhysAddress','TextualConvention','TestAndIncr','TimeInterval','TimeStamp')
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NonNegativeInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SocomecSicon_ObjectIdentity=ObjectIdentity
socomecSicon=_SocomecSicon_ObjectIdentity((1,3,6,1,4,1,4555))
_Software_ObjectIdentity=ObjectIdentity
software=_Software_ObjectIdentity((1,3,6,1,4,1,4555,1))
_Network_ObjectIdentity=ObjectIdentity
network=_Network_ObjectIdentity((1,3,6,1,4,1,4555,1,1))
_Netvision_ObjectIdentity=ObjectIdentity
netvision=_Netvision_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1))
_UpsObjects_ObjectIdentity=ObjectIdentity
upsObjects=_UpsObjects_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1))
_UpsIdent_ObjectIdentity=ObjectIdentity
upsIdent=_UpsIdent_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,1))
class _UpsIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentModel_Type.__name__=_G
_UpsIdentModel_Object=MibScalar
upsIdentModel=_UpsIdentModel_Object((1,3,6,1,4,1,4555,1,1,1,1,1,1),_UpsIdentModel_Type())
upsIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentModel.setStatus(_A)
class _UpsIdentUPSFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentUPSFirmwareVersion_Type.__name__=_G
_UpsIdentUPSFirmwareVersion_Object=MibScalar
upsIdentUPSFirmwareVersion=_UpsIdentUPSFirmwareVersion_Object((1,3,6,1,4,1,4555,1,1,1,1,1,2),_UpsIdentUPSFirmwareVersion_Type())
upsIdentUPSFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentUPSFirmwareVersion.setStatus(_A)
class _UpsIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsIdentAgentSoftwareVersion_Type.__name__=_G
_UpsIdentAgentSoftwareVersion_Object=MibScalar
upsIdentAgentSoftwareVersion=_UpsIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,4555,1,1,1,1,1,3),_UpsIdentAgentSoftwareVersion_Type())
upsIdentAgentSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentAgentSoftwareVersion.setStatus(_A)
class _UpsIdentUpsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_UpsIdentUpsSerialNumber_Type.__name__=_G
_UpsIdentUpsSerialNumber_Object=MibScalar
upsIdentUpsSerialNumber=_UpsIdentUpsSerialNumber_Object((1,3,6,1,4,1,4555,1,1,1,1,1,4),_UpsIdentUpsSerialNumber_Type())
upsIdentUpsSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentUpsSerialNumber.setStatus(_A)
_UpsBattery_ObjectIdentity=ObjectIdentity
upsBattery=_UpsBattery_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,2))
class _UpsBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_X,1),('batteryNormal',2),('batteryLow',3),('batteryDepleted',4),('batteryDischarging',5),('batteryFailure',6),('batteryDisconnected',7)))
_UpsBatteryStatus_Type.__name__=_E
_UpsBatteryStatus_Object=MibScalar
upsBatteryStatus=_UpsBatteryStatus_Object((1,3,6,1,4,1,4555,1,1,1,1,2,1),_UpsBatteryStatus_Type())
upsBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryStatus.setStatus(_A)
_UpsSecondsOnBattery_Type=Integer32
_UpsSecondsOnBattery_Object=MibScalar
upsSecondsOnBattery=_UpsSecondsOnBattery_Object((1,3,6,1,4,1,4555,1,1,1,1,2,2),_UpsSecondsOnBattery_Type())
upsSecondsOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSecondsOnBattery.setStatus(_A)
_UpsEstimatedMinutesRemaining_Type=Integer32
_UpsEstimatedMinutesRemaining_Object=MibScalar
upsEstimatedMinutesRemaining=_UpsEstimatedMinutesRemaining_Object((1,3,6,1,4,1,4555,1,1,1,1,2,3),_UpsEstimatedMinutesRemaining_Type())
upsEstimatedMinutesRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEstimatedMinutesRemaining.setStatus(_A)
_UpsEstimatedChargeRemaining_Type=Integer32
_UpsEstimatedChargeRemaining_Object=MibScalar
upsEstimatedChargeRemaining=_UpsEstimatedChargeRemaining_Object((1,3,6,1,4,1,4555,1,1,1,1,2,4),_UpsEstimatedChargeRemaining_Type())
upsEstimatedChargeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEstimatedChargeRemaining.setStatus(_A)
_UpsBatteryVoltage_Type=Integer32
_UpsBatteryVoltage_Object=MibScalar
upsBatteryVoltage=_UpsBatteryVoltage_Object((1,3,6,1,4,1,4555,1,1,1,1,2,5),_UpsBatteryVoltage_Type())
upsBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryVoltage.setStatus(_A)
_UpsBatteryTemperature_Type=Integer32
_UpsBatteryTemperature_Object=MibScalar
upsBatteryTemperature=_UpsBatteryTemperature_Object((1,3,6,1,4,1,4555,1,1,1,1,2,6),_UpsBatteryTemperature_Type())
upsBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryTemperature.setStatus(_A)
_UpsInput_ObjectIdentity=ObjectIdentity
upsInput=_UpsInput_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,3))
_UpsInputNumLines_Type=Integer32
_UpsInputNumLines_Object=MibScalar
upsInputNumLines=_UpsInputNumLines_Object((1,3,6,1,4,1,4555,1,1,1,1,3,1),_UpsInputNumLines_Type())
upsInputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputNumLines.setStatus(_A)
_UpsInputFrequency_Type=Integer32
_UpsInputFrequency_Object=MibScalar
upsInputFrequency=_UpsInputFrequency_Object((1,3,6,1,4,1,4555,1,1,1,1,3,2),_UpsInputFrequency_Type())
upsInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputFrequency.setStatus(_A)
_UpsInputTable_Object=MibTable
upsInputTable=_UpsInputTable_Object((1,3,6,1,4,1,4555,1,1,1,1,3,3))
if mibBuilder.loadTexts:upsInputTable.setStatus(_A)
_UpsInputEntry_Object=MibTableRow
upsInputEntry=_UpsInputEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,3,3,1))
upsInputEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:upsInputEntry.setStatus(_A)
class _UpsInputLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UpsInputLineIndex_Type.__name__=_E
_UpsInputLineIndex_Object=MibTableColumn
upsInputLineIndex=_UpsInputLineIndex_Object((1,3,6,1,4,1,4555,1,1,1,1,3,3,1,1),_UpsInputLineIndex_Type())
upsInputLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputLineIndex.setStatus(_A)
_UpsInputVoltage_Type=Integer32
_UpsInputVoltage_Object=MibTableColumn
upsInputVoltage=_UpsInputVoltage_Object((1,3,6,1,4,1,4555,1,1,1,1,3,3,1,2),_UpsInputVoltage_Type())
upsInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVoltage.setStatus(_A)
_UpsInputCurrent_Type=Integer32
_UpsInputCurrent_Object=MibTableColumn
upsInputCurrent=_UpsInputCurrent_Object((1,3,6,1,4,1,4555,1,1,1,1,3,3,1,3),_UpsInputCurrent_Type())
upsInputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputCurrent.setStatus(_A)
_UpsInputVoltageMax_Type=Integer32
_UpsInputVoltageMax_Object=MibTableColumn
upsInputVoltageMax=_UpsInputVoltageMax_Object((1,3,6,1,4,1,4555,1,1,1,1,3,3,1,4),_UpsInputVoltageMax_Type())
upsInputVoltageMax.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVoltageMax.setStatus(_A)
_UpsInputVoltageMin_Type=Integer32
_UpsInputVoltageMin_Object=MibTableColumn
upsInputVoltageMin=_UpsInputVoltageMin_Object((1,3,6,1,4,1,4555,1,1,1,1,3,3,1,5),_UpsInputVoltageMin_Type())
upsInputVoltageMin.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVoltageMin.setStatus(_A)
_UpsOutput_ObjectIdentity=ObjectIdentity
upsOutput=_UpsOutput_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,4))
class _UpsOutputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_X,1),('onInverter',2),('onMains',3),('ecoMode',4),('onBypass',5),('standby',6),('onMaintenanceBypass',7),('upsOff',8),('normalMode',9)))
_UpsOutputSource_Type.__name__=_E
_UpsOutputSource_Object=MibScalar
upsOutputSource=_UpsOutputSource_Object((1,3,6,1,4,1,4555,1,1,1,1,4,1),_UpsOutputSource_Type())
upsOutputSource.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputSource.setStatus(_A)
_UpsOutputFrequency_Type=Integer32
_UpsOutputFrequency_Object=MibScalar
upsOutputFrequency=_UpsOutputFrequency_Object((1,3,6,1,4,1,4555,1,1,1,1,4,2),_UpsOutputFrequency_Type())
upsOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputFrequency.setStatus(_A)
_UpsOutputNumLines_Type=Integer32
_UpsOutputNumLines_Object=MibScalar
upsOutputNumLines=_UpsOutputNumLines_Object((1,3,6,1,4,1,4555,1,1,1,1,4,3),_UpsOutputNumLines_Type())
upsOutputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputNumLines.setStatus(_A)
_UpsOutputTable_Object=MibTable
upsOutputTable=_UpsOutputTable_Object((1,3,6,1,4,1,4555,1,1,1,1,4,4))
if mibBuilder.loadTexts:upsOutputTable.setStatus(_A)
_UpsOutputEntry_Object=MibTableRow
upsOutputEntry=_UpsOutputEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,4,4,1))
upsOutputEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:upsOutputEntry.setStatus(_A)
class _UpsOutputLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UpsOutputLineIndex_Type.__name__=_E
_UpsOutputLineIndex_Object=MibTableColumn
upsOutputLineIndex=_UpsOutputLineIndex_Object((1,3,6,1,4,1,4555,1,1,1,1,4,4,1,1),_UpsOutputLineIndex_Type())
upsOutputLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputLineIndex.setStatus(_A)
_UpsOutputVoltage_Type=Integer32
_UpsOutputVoltage_Object=MibTableColumn
upsOutputVoltage=_UpsOutputVoltage_Object((1,3,6,1,4,1,4555,1,1,1,1,4,4,1,2),_UpsOutputVoltage_Type())
upsOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputVoltage.setStatus(_A)
_UpsOutputCurrent_Type=Integer32
_UpsOutputCurrent_Object=MibTableColumn
upsOutputCurrent=_UpsOutputCurrent_Object((1,3,6,1,4,1,4555,1,1,1,1,4,4,1,3),_UpsOutputCurrent_Type())
upsOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputCurrent.setStatus(_A)
_UpsOutputPercentLoad_Type=Integer32
_UpsOutputPercentLoad_Object=MibTableColumn
upsOutputPercentLoad=_UpsOutputPercentLoad_Object((1,3,6,1,4,1,4555,1,1,1,1,4,4,1,4),_UpsOutputPercentLoad_Type())
upsOutputPercentLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPercentLoad.setStatus(_A)
_UpsOutputKva_Type=Integer32
_UpsOutputKva_Object=MibTableColumn
upsOutputKva=_UpsOutputKva_Object((1,3,6,1,4,1,4555,1,1,1,1,4,4,1,5),_UpsOutputKva_Type())
upsOutputKva.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputKva.setStatus(_A)
_UpsBypass_ObjectIdentity=ObjectIdentity
upsBypass=_UpsBypass_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,5))
_UpsBypassFrequency_Type=Integer32
_UpsBypassFrequency_Object=MibScalar
upsBypassFrequency=_UpsBypassFrequency_Object((1,3,6,1,4,1,4555,1,1,1,1,5,1),_UpsBypassFrequency_Type())
upsBypassFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassFrequency.setStatus(_A)
_UpsBypassNumLines_Type=Integer32
_UpsBypassNumLines_Object=MibScalar
upsBypassNumLines=_UpsBypassNumLines_Object((1,3,6,1,4,1,4555,1,1,1,1,5,2),_UpsBypassNumLines_Type())
upsBypassNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassNumLines.setStatus(_A)
_UpsBypassTable_Object=MibTable
upsBypassTable=_UpsBypassTable_Object((1,3,6,1,4,1,4555,1,1,1,1,5,3))
if mibBuilder.loadTexts:upsBypassTable.setStatus(_A)
_UpsBypassEntry_Object=MibTableRow
upsBypassEntry=_UpsBypassEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,5,3,1))
upsBypassEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:upsBypassEntry.setStatus(_A)
class _UpsBypassLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UpsBypassLineIndex_Type.__name__=_E
_UpsBypassLineIndex_Object=MibTableColumn
upsBypassLineIndex=_UpsBypassLineIndex_Object((1,3,6,1,4,1,4555,1,1,1,1,5,3,1,1),_UpsBypassLineIndex_Type())
upsBypassLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassLineIndex.setStatus(_A)
_UpsBypassVoltage_Type=Integer32
_UpsBypassVoltage_Object=MibTableColumn
upsBypassVoltage=_UpsBypassVoltage_Object((1,3,6,1,4,1,4555,1,1,1,1,5,3,1,2),_UpsBypassVoltage_Type())
upsBypassVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassVoltage.setStatus(_A)
_UpsBypassCurrent_Type=Integer32
_UpsBypassCurrent_Object=MibTableColumn
upsBypassCurrent=_UpsBypassCurrent_Object((1,3,6,1,4,1,4555,1,1,1,1,5,3,1,3),_UpsBypassCurrent_Type())
upsBypassCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassCurrent.setStatus(_A)
_UpsAlarm_ObjectIdentity=ObjectIdentity
upsAlarm=_UpsAlarm_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,6))
_UpsAlarmsPresent_Type=Integer32
_UpsAlarmsPresent_Object=MibScalar
upsAlarmsPresent=_UpsAlarmsPresent_Object((1,3,6,1,4,1,4555,1,1,1,1,6,1),_UpsAlarmsPresent_Type())
upsAlarmsPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmsPresent.setStatus(_A)
_UpsAlarmTable_Object=MibTable
upsAlarmTable=_UpsAlarmTable_Object((1,3,6,1,4,1,4555,1,1,1,1,6,2))
if mibBuilder.loadTexts:upsAlarmTable.setStatus(_A)
_UpsAlarmEntry_Object=MibTableRow
upsAlarmEntry=_UpsAlarmEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,6,2,1))
upsAlarmEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:upsAlarmEntry.setStatus(_A)
_UpsAlarmId_Type=PositiveInteger
_UpsAlarmId_Object=MibTableColumn
upsAlarmId=_UpsAlarmId_Object((1,3,6,1,4,1,4555,1,1,1,1,6,2,1,1),_UpsAlarmId_Type())
upsAlarmId.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmId.setStatus(_A)
_UpsAlarmDescr_Type=AutonomousType
_UpsAlarmDescr_Object=MibTableColumn
upsAlarmDescr=_UpsAlarmDescr_Object((1,3,6,1,4,1,4555,1,1,1,1,6,2,1,2),_UpsAlarmDescr_Type())
upsAlarmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDescr.setStatus(_A)
_UpsAlarmTime_Type=TimeStamp
_UpsAlarmTime_Object=MibTableColumn
upsAlarmTime=_UpsAlarmTime_Object((1,3,6,1,4,1,4555,1,1,1,1,6,2,1,3),_UpsAlarmTime_Type())
upsAlarmTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmTime.setStatus(_A)
_UpsAlarmExtDes_Type=DisplayString
_UpsAlarmExtDes_Object=MibTableColumn
upsAlarmExtDes=_UpsAlarmExtDes_Object((1,3,6,1,4,1,4555,1,1,1,1,6,2,1,4),_UpsAlarmExtDes_Type())
upsAlarmExtDes.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmExtDes.setStatus(_A)
_UpsWellKnownAlarms_ObjectIdentity=ObjectIdentity
upsWellKnownAlarms=_UpsWellKnownAlarms_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,6,3))
_UpsAlarmBatteryBad_Type=Integer32
_UpsAlarmBatteryBad_Object=MibScalar
upsAlarmBatteryBad=_UpsAlarmBatteryBad_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,1),_UpsAlarmBatteryBad_Type())
upsAlarmBatteryBad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBatteryBad.setStatus(_A)
_UpsAlarmOnBattery_Type=Integer32
_UpsAlarmOnBattery_Object=MibScalar
upsAlarmOnBattery=_UpsAlarmOnBattery_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,2),_UpsAlarmOnBattery_Type())
upsAlarmOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOnBattery.setStatus(_A)
_UpsAlarmLowBattery_Type=Integer32
_UpsAlarmLowBattery_Object=MibScalar
upsAlarmLowBattery=_UpsAlarmLowBattery_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,3),_UpsAlarmLowBattery_Type())
upsAlarmLowBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmLowBattery.setStatus(_A)
_UpsAlarmDepletedBattery_Type=Integer32
_UpsAlarmDepletedBattery_Object=MibScalar
upsAlarmDepletedBattery=_UpsAlarmDepletedBattery_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,4),_UpsAlarmDepletedBattery_Type())
upsAlarmDepletedBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDepletedBattery.setStatus(_A)
_UpsAlarmTempBad_Type=Integer32
_UpsAlarmTempBad_Object=MibScalar
upsAlarmTempBad=_UpsAlarmTempBad_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,5),_UpsAlarmTempBad_Type())
upsAlarmTempBad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmTempBad.setStatus(_A)
_UpsAlarmInputBad_Type=Integer32
_UpsAlarmInputBad_Object=MibScalar
upsAlarmInputBad=_UpsAlarmInputBad_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,6),_UpsAlarmInputBad_Type())
upsAlarmInputBad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmInputBad.setStatus(_A)
_UpsAlarmOutputBad_Type=Integer32
_UpsAlarmOutputBad_Object=MibScalar
upsAlarmOutputBad=_UpsAlarmOutputBad_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,7),_UpsAlarmOutputBad_Type())
upsAlarmOutputBad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOutputBad.setStatus(_A)
_UpsAlarmOutputOverload_Type=Integer32
_UpsAlarmOutputOverload_Object=MibScalar
upsAlarmOutputOverload=_UpsAlarmOutputOverload_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,8),_UpsAlarmOutputOverload_Type())
upsAlarmOutputOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOutputOverload.setStatus(_A)
_UpsAlarmOnBypass_Type=Integer32
_UpsAlarmOnBypass_Object=MibScalar
upsAlarmOnBypass=_UpsAlarmOnBypass_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,9),_UpsAlarmOnBypass_Type())
upsAlarmOnBypass.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOnBypass.setStatus(_A)
_UpsAlarmBypassBad_Type=Integer32
_UpsAlarmBypassBad_Object=MibScalar
upsAlarmBypassBad=_UpsAlarmBypassBad_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,10),_UpsAlarmBypassBad_Type())
upsAlarmBypassBad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBypassBad.setStatus(_A)
_UpsAlarmOutputOffAsRequested_Type=Integer32
_UpsAlarmOutputOffAsRequested_Object=MibScalar
upsAlarmOutputOffAsRequested=_UpsAlarmOutputOffAsRequested_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,11),_UpsAlarmOutputOffAsRequested_Type())
upsAlarmOutputOffAsRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOutputOffAsRequested.setStatus(_A)
_UpsAlarmUpsOffAsRequested_Type=Integer32
_UpsAlarmUpsOffAsRequested_Object=MibScalar
upsAlarmUpsOffAsRequested=_UpsAlarmUpsOffAsRequested_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,12),_UpsAlarmUpsOffAsRequested_Type())
upsAlarmUpsOffAsRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmUpsOffAsRequested.setStatus(_A)
_UpsAlarmChargerFailed_Type=Integer32
_UpsAlarmChargerFailed_Object=MibScalar
upsAlarmChargerFailed=_UpsAlarmChargerFailed_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,13),_UpsAlarmChargerFailed_Type())
upsAlarmChargerFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmChargerFailed.setStatus(_A)
_UpsAlarmUpsOutputOff_Type=Integer32
_UpsAlarmUpsOutputOff_Object=MibScalar
upsAlarmUpsOutputOff=_UpsAlarmUpsOutputOff_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,14),_UpsAlarmUpsOutputOff_Type())
upsAlarmUpsOutputOff.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmUpsOutputOff.setStatus(_A)
_UpsAlarmUpsSystemOff_Type=Integer32
_UpsAlarmUpsSystemOff_Object=MibScalar
upsAlarmUpsSystemOff=_UpsAlarmUpsSystemOff_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,15),_UpsAlarmUpsSystemOff_Type())
upsAlarmUpsSystemOff.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmUpsSystemOff.setStatus(_A)
_UpsAlarmFanFailure_Type=Integer32
_UpsAlarmFanFailure_Object=MibScalar
upsAlarmFanFailure=_UpsAlarmFanFailure_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,16),_UpsAlarmFanFailure_Type())
upsAlarmFanFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmFanFailure.setStatus(_A)
_UpsAlarmFuseFailure_Type=Integer32
_UpsAlarmFuseFailure_Object=MibScalar
upsAlarmFuseFailure=_UpsAlarmFuseFailure_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,17),_UpsAlarmFuseFailure_Type())
upsAlarmFuseFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmFuseFailure.setStatus(_A)
_UpsAlarmGeneralFault_Type=Integer32
_UpsAlarmGeneralFault_Object=MibScalar
upsAlarmGeneralFault=_UpsAlarmGeneralFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,18),_UpsAlarmGeneralFault_Type())
upsAlarmGeneralFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmGeneralFault.setStatus(_A)
_UpsAlarmDiagnosticTestFailed_Type=Integer32
_UpsAlarmDiagnosticTestFailed_Object=MibScalar
upsAlarmDiagnosticTestFailed=_UpsAlarmDiagnosticTestFailed_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,19),_UpsAlarmDiagnosticTestFailed_Type())
upsAlarmDiagnosticTestFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDiagnosticTestFailed.setStatus(_A)
_UpsAlarmCommunicationLost_Type=Integer32
_UpsAlarmCommunicationLost_Object=MibScalar
upsAlarmCommunicationLost=_UpsAlarmCommunicationLost_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,20),_UpsAlarmCommunicationLost_Type())
upsAlarmCommunicationLost.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmCommunicationLost.setStatus(_A)
_UpsAlarmAwaitingPower_Type=Integer32
_UpsAlarmAwaitingPower_Object=MibScalar
upsAlarmAwaitingPower=_UpsAlarmAwaitingPower_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,21),_UpsAlarmAwaitingPower_Type())
upsAlarmAwaitingPower.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmAwaitingPower.setStatus(_A)
_UpsAlarmShutdownPending_Type=Integer32
_UpsAlarmShutdownPending_Object=MibScalar
upsAlarmShutdownPending=_UpsAlarmShutdownPending_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,22),_UpsAlarmShutdownPending_Type())
upsAlarmShutdownPending.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmShutdownPending.setStatus(_A)
_UpsAlarmShutdownImminent_Type=Integer32
_UpsAlarmShutdownImminent_Object=MibScalar
upsAlarmShutdownImminent=_UpsAlarmShutdownImminent_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,23),_UpsAlarmShutdownImminent_Type())
upsAlarmShutdownImminent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmShutdownImminent.setStatus(_A)
_UpsAlarmTestInProgress_Type=Integer32
_UpsAlarmTestInProgress_Object=MibScalar
upsAlarmTestInProgress=_UpsAlarmTestInProgress_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,24),_UpsAlarmTestInProgress_Type())
upsAlarmTestInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmTestInProgress.setStatus(_A)
_UpsAlarmPowerSupplyFault_Type=Integer32
_UpsAlarmPowerSupplyFault_Object=MibScalar
upsAlarmPowerSupplyFault=_UpsAlarmPowerSupplyFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,25),_UpsAlarmPowerSupplyFault_Type())
upsAlarmPowerSupplyFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmPowerSupplyFault.setStatus(_A)
_UpsAlarmAuxMainFail_Type=Integer32
_UpsAlarmAuxMainFail_Object=MibScalar
upsAlarmAuxMainFail=_UpsAlarmAuxMainFail_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,26),_UpsAlarmAuxMainFail_Type())
upsAlarmAuxMainFail.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmAuxMainFail.setStatus(_A)
_UpsAlarmManualBypassClose_Type=Integer32
_UpsAlarmManualBypassClose_Object=MibScalar
upsAlarmManualBypassClose=_UpsAlarmManualBypassClose_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,27),_UpsAlarmManualBypassClose_Type())
upsAlarmManualBypassClose.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmManualBypassClose.setStatus(_A)
_UpsAlarmShortCircuit_Type=Integer32
_UpsAlarmShortCircuit_Object=MibScalar
upsAlarmShortCircuit=_UpsAlarmShortCircuit_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,28),_UpsAlarmShortCircuit_Type())
upsAlarmShortCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmShortCircuit.setStatus(_A)
_UpsAlarmBatteryChargerFailure_Type=Integer32
_UpsAlarmBatteryChargerFailure_Object=MibScalar
upsAlarmBatteryChargerFailure=_UpsAlarmBatteryChargerFailure_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,29),_UpsAlarmBatteryChargerFailure_Type())
upsAlarmBatteryChargerFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBatteryChargerFailure.setStatus(_A)
_UpsAlarmInverterOverCurrent_Type=Integer32
_UpsAlarmInverterOverCurrent_Object=MibScalar
upsAlarmInverterOverCurrent=_UpsAlarmInverterOverCurrent_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,30),_UpsAlarmInverterOverCurrent_Type())
upsAlarmInverterOverCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmInverterOverCurrent.setStatus(_A)
_UpsAlarmInverterDistorsion_Type=Integer32
_UpsAlarmInverterDistorsion_Object=MibScalar
upsAlarmInverterDistorsion=_UpsAlarmInverterDistorsion_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,31),_UpsAlarmInverterDistorsion_Type())
upsAlarmInverterDistorsion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmInverterDistorsion.setStatus(_A)
_UpsAlarmPrechargeVoltageFail_Type=Integer32
_UpsAlarmPrechargeVoltageFail_Object=MibScalar
upsAlarmPrechargeVoltageFail=_UpsAlarmPrechargeVoltageFail_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,32),_UpsAlarmPrechargeVoltageFail_Type())
upsAlarmPrechargeVoltageFail.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmPrechargeVoltageFail.setStatus(_A)
_UpsAlarmBoostTooLow_Type=Integer32
_UpsAlarmBoostTooLow_Object=MibScalar
upsAlarmBoostTooLow=_UpsAlarmBoostTooLow_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,33),_UpsAlarmBoostTooLow_Type())
upsAlarmBoostTooLow.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBoostTooLow.setStatus(_A)
_UpsAlarmBoostTooHigh_Type=Integer32
_UpsAlarmBoostTooHigh_Object=MibScalar
upsAlarmBoostTooHigh=_UpsAlarmBoostTooHigh_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,34),_UpsAlarmBoostTooHigh_Type())
upsAlarmBoostTooHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBoostTooHigh.setStatus(_A)
_UpsAlarmBatteryTooHigh_Type=Integer32
_UpsAlarmBatteryTooHigh_Object=MibScalar
upsAlarmBatteryTooHigh=_UpsAlarmBatteryTooHigh_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,35),_UpsAlarmBatteryTooHigh_Type())
upsAlarmBatteryTooHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBatteryTooHigh.setStatus(_A)
_UpsAlarmImproperCondition_Type=Integer32
_UpsAlarmImproperCondition_Object=MibScalar
upsAlarmImproperCondition=_UpsAlarmImproperCondition_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,36),_UpsAlarmImproperCondition_Type())
upsAlarmImproperCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmImproperCondition.setStatus(_A)
_UpsAlarmOverloadTimeout_Type=Integer32
_UpsAlarmOverloadTimeout_Object=MibScalar
upsAlarmOverloadTimeout=_UpsAlarmOverloadTimeout_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,37),_UpsAlarmOverloadTimeout_Type())
upsAlarmOverloadTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOverloadTimeout.setStatus(_A)
_UpsAlarmControlSystemFailure_Type=Integer32
_UpsAlarmControlSystemFailure_Object=MibScalar
upsAlarmControlSystemFailure=_UpsAlarmControlSystemFailure_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,38),_UpsAlarmControlSystemFailure_Type())
upsAlarmControlSystemFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmControlSystemFailure.setStatus(_A)
_UpsAlarmDataCorrupted_Type=Integer32
_UpsAlarmDataCorrupted_Object=MibScalar
upsAlarmDataCorrupted=_UpsAlarmDataCorrupted_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,39),_UpsAlarmDataCorrupted_Type())
upsAlarmDataCorrupted.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDataCorrupted.setStatus(_A)
_UpsAlarmPllFault_Type=Integer32
_UpsAlarmPllFault_Object=MibScalar
upsAlarmPllFault=_UpsAlarmPllFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,40),_UpsAlarmPllFault_Type())
upsAlarmPllFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmPllFault.setStatus(_A)
_UpsAlarmInputGeneralAlarm_Type=Integer32
_UpsAlarmInputGeneralAlarm_Object=MibScalar
upsAlarmInputGeneralAlarm=_UpsAlarmInputGeneralAlarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,41),_UpsAlarmInputGeneralAlarm_Type())
upsAlarmInputGeneralAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmInputGeneralAlarm.setStatus(_A)
_UpsAlarmRectifierGeneralAlarm_Type=Integer32
_UpsAlarmRectifierGeneralAlarm_Object=MibScalar
upsAlarmRectifierGeneralAlarm=_UpsAlarmRectifierGeneralAlarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,42),_UpsAlarmRectifierGeneralAlarm_Type())
upsAlarmRectifierGeneralAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmRectifierGeneralAlarm.setStatus(_A)
_UpsAlarmBoostGeneralAlarm_Type=Integer32
_UpsAlarmBoostGeneralAlarm_Object=MibScalar
upsAlarmBoostGeneralAlarm=_UpsAlarmBoostGeneralAlarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,43),_UpsAlarmBoostGeneralAlarm_Type())
upsAlarmBoostGeneralAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBoostGeneralAlarm.setStatus(_A)
_UpsAlarmInverterGeneralAlarm_Type=Integer32
_UpsAlarmInverterGeneralAlarm_Object=MibScalar
upsAlarmInverterGeneralAlarm=_UpsAlarmInverterGeneralAlarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,44),_UpsAlarmInverterGeneralAlarm_Type())
upsAlarmInverterGeneralAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmInverterGeneralAlarm.setStatus(_A)
_UpsAlarmBatteryGeneralAlarm_Type=Integer32
_UpsAlarmBatteryGeneralAlarm_Object=MibScalar
upsAlarmBatteryGeneralAlarm=_UpsAlarmBatteryGeneralAlarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,45),_UpsAlarmBatteryGeneralAlarm_Type())
upsAlarmBatteryGeneralAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBatteryGeneralAlarm.setStatus(_A)
_UpsAlarmOutputOver_Type=Integer32
_UpsAlarmOutputOver_Object=MibScalar
upsAlarmOutputOver=_UpsAlarmOutputOver_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,46),_UpsAlarmOutputOver_Type())
upsAlarmOutputOver.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOutputOver.setStatus(_A)
_UpsAlarmOutputUnder_Type=Integer32
_UpsAlarmOutputUnder_Object=MibScalar
upsAlarmOutputUnder=_UpsAlarmOutputUnder_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,47),_UpsAlarmOutputUnder_Type())
upsAlarmOutputUnder.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOutputUnder.setStatus(_A)
_UpsAlarmBypassGeneralAlarm_Type=Integer32
_UpsAlarmBypassGeneralAlarm_Object=MibScalar
upsAlarmBypassGeneralAlarm=_UpsAlarmBypassGeneralAlarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,48),_UpsAlarmBypassGeneralAlarm_Type())
upsAlarmBypassGeneralAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBypassGeneralAlarm.setStatus(_A)
_UpsAlarmStopForOverload_Type=Integer32
_UpsAlarmStopForOverload_Object=MibScalar
upsAlarmStopForOverload=_UpsAlarmStopForOverload_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,49),_UpsAlarmStopForOverload_Type())
upsAlarmStopForOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmStopForOverload.setStatus(_A)
_UpsAlarmImminentStop_Type=Integer32
_UpsAlarmImminentStop_Object=MibScalar
upsAlarmImminentStop=_UpsAlarmImminentStop_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,50),_UpsAlarmImminentStop_Type())
upsAlarmImminentStop.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmImminentStop.setStatus(_A)
_UpsAlarmModule1Alarm_Type=Integer32
_UpsAlarmModule1Alarm_Object=MibScalar
upsAlarmModule1Alarm=_UpsAlarmModule1Alarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,51),_UpsAlarmModule1Alarm_Type())
upsAlarmModule1Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmModule1Alarm.setStatus(_A)
_UpsAlarmModule2Alarm_Type=Integer32
_UpsAlarmModule2Alarm_Object=MibScalar
upsAlarmModule2Alarm=_UpsAlarmModule2Alarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,52),_UpsAlarmModule2Alarm_Type())
upsAlarmModule2Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmModule2Alarm.setStatus(_A)
_UpsAlarmModule3Alarm_Type=Integer32
_UpsAlarmModule3Alarm_Object=MibScalar
upsAlarmModule3Alarm=_UpsAlarmModule3Alarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,53),_UpsAlarmModule3Alarm_Type())
upsAlarmModule3Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmModule3Alarm.setStatus(_A)
_UpsAlarmModule4Alarm_Type=Integer32
_UpsAlarmModule4Alarm_Object=MibScalar
upsAlarmModule4Alarm=_UpsAlarmModule4Alarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,54),_UpsAlarmModule4Alarm_Type())
upsAlarmModule4Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmModule4Alarm.setStatus(_A)
_UpsAlarmModule5Alarm_Type=Integer32
_UpsAlarmModule5Alarm_Object=MibScalar
upsAlarmModule5Alarm=_UpsAlarmModule5Alarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,55),_UpsAlarmModule5Alarm_Type())
upsAlarmModule5Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmModule5Alarm.setStatus(_A)
_UpsAlarmModule6Alarm_Type=Integer32
_UpsAlarmModule6Alarm_Object=MibScalar
upsAlarmModule6Alarm=_UpsAlarmModule6Alarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,56),_UpsAlarmModule6Alarm_Type())
upsAlarmModule6Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmModule6Alarm.setStatus(_A)
_UpsAlarmExternalAlarm1_Type=Integer32
_UpsAlarmExternalAlarm1_Object=MibScalar
upsAlarmExternalAlarm1=_UpsAlarmExternalAlarm1_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,57),_UpsAlarmExternalAlarm1_Type())
upsAlarmExternalAlarm1.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmExternalAlarm1.setStatus(_A)
_UpsAlarmExternalAlarm2_Type=Integer32
_UpsAlarmExternalAlarm2_Object=MibScalar
upsAlarmExternalAlarm2=_UpsAlarmExternalAlarm2_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,58),_UpsAlarmExternalAlarm2_Type())
upsAlarmExternalAlarm2.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmExternalAlarm2.setStatus(_A)
_UpsAlarmExternalAlarm3_Type=Integer32
_UpsAlarmExternalAlarm3_Object=MibScalar
upsAlarmExternalAlarm3=_UpsAlarmExternalAlarm3_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,59),_UpsAlarmExternalAlarm3_Type())
upsAlarmExternalAlarm3.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmExternalAlarm3.setStatus(_A)
_UpsAlarmExternalAlarm4_Type=Integer32
_UpsAlarmExternalAlarm4_Object=MibScalar
upsAlarmExternalAlarm4=_UpsAlarmExternalAlarm4_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,60),_UpsAlarmExternalAlarm4_Type())
upsAlarmExternalAlarm4.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmExternalAlarm4.setStatus(_A)
_UpsAlarmEService_Type=Integer32
_UpsAlarmEService_Object=MibScalar
upsAlarmEService=_UpsAlarmEService_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,61),_UpsAlarmEService_Type())
upsAlarmEService.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmEService.setStatus(_A)
_UpsAlarmRedundancyLost_Type=Integer32
_UpsAlarmRedundancyLost_Object=MibScalar
upsAlarmRedundancyLost=_UpsAlarmRedundancyLost_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,62),_UpsAlarmRedundancyLost_Type())
upsAlarmRedundancyLost.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmRedundancyLost.setStatus(_A)
_UpsAlarmPeriodicServiceCheck_Type=Integer32
_UpsAlarmPeriodicServiceCheck_Object=MibScalar
upsAlarmPeriodicServiceCheck=_UpsAlarmPeriodicServiceCheck_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,63),_UpsAlarmPeriodicServiceCheck_Type())
upsAlarmPeriodicServiceCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmPeriodicServiceCheck.setStatus(_A)
_UpsAlarmAllTransferDisabled_Type=Integer32
_UpsAlarmAllTransferDisabled_Object=MibScalar
upsAlarmAllTransferDisabled=_UpsAlarmAllTransferDisabled_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,64),_UpsAlarmAllTransferDisabled_Type())
upsAlarmAllTransferDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmAllTransferDisabled.setStatus(_A)
_UpsAlarmAutoTransferDisabled_Type=Integer32
_UpsAlarmAutoTransferDisabled_Object=MibScalar
upsAlarmAutoTransferDisabled=_UpsAlarmAutoTransferDisabled_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,65),_UpsAlarmAutoTransferDisabled_Type())
upsAlarmAutoTransferDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmAutoTransferDisabled.setStatus(_A)
_UpsAlarmBatteryRoom_Type=Integer32
_UpsAlarmBatteryRoom_Object=MibScalar
upsAlarmBatteryRoom=_UpsAlarmBatteryRoom_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,66),_UpsAlarmBatteryRoom_Type())
upsAlarmBatteryRoom.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBatteryRoom.setStatus(_A)
_UpsAlarmManualBypass_Type=Integer32
_UpsAlarmManualBypass_Object=MibScalar
upsAlarmManualBypass=_UpsAlarmManualBypass_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,67),_UpsAlarmManualBypass_Type())
upsAlarmManualBypass.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmManualBypass.setStatus(_A)
_UpsAlarmBatteryDischarged_Type=Integer32
_UpsAlarmBatteryDischarged_Object=MibScalar
upsAlarmBatteryDischarged=_UpsAlarmBatteryDischarged_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,68),_UpsAlarmBatteryDischarged_Type())
upsAlarmBatteryDischarged.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBatteryDischarged.setStatus(_A)
_UpsAlarmInsufficientResources_Type=Integer32
_UpsAlarmInsufficientResources_Object=MibScalar
upsAlarmInsufficientResources=_UpsAlarmInsufficientResources_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,69),_UpsAlarmInsufficientResources_Type())
upsAlarmInsufficientResources.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmInsufficientResources.setStatus(_A)
_UpsAlarmOptionalBoards_Type=Integer32
_UpsAlarmOptionalBoards_Object=MibScalar
upsAlarmOptionalBoards=_UpsAlarmOptionalBoards_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,70),_UpsAlarmOptionalBoards_Type())
upsAlarmOptionalBoards.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmOptionalBoards.setStatus(_A)
_UpsAlarmRectifierFault_Type=Integer32
_UpsAlarmRectifierFault_Object=MibScalar
upsAlarmRectifierFault=_UpsAlarmRectifierFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,71),_UpsAlarmRectifierFault_Type())
upsAlarmRectifierFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmRectifierFault.setStatus(_A)
_UpsAlarmBoostFault_Type=Integer32
_UpsAlarmBoostFault_Object=MibScalar
upsAlarmBoostFault=_UpsAlarmBoostFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,72),_UpsAlarmBoostFault_Type())
upsAlarmBoostFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBoostFault.setStatus(_A)
_UpsAlarmInverterFault_Type=Integer32
_UpsAlarmInverterFault_Object=MibScalar
upsAlarmInverterFault=_UpsAlarmInverterFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,73),_UpsAlarmInverterFault_Type())
upsAlarmInverterFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmInverterFault.setStatus(_A)
_UpsAlarmParallelModuleFault_Type=Integer32
_UpsAlarmParallelModuleFault_Object=MibScalar
upsAlarmParallelModuleFault=_UpsAlarmParallelModuleFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,74),_UpsAlarmParallelModuleFault_Type())
upsAlarmParallelModuleFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmParallelModuleFault.setStatus(_A)
_UpsAlarmGenSetGeneral_Type=Integer32
_UpsAlarmGenSetGeneral_Object=MibScalar
upsAlarmGenSetGeneral=_UpsAlarmGenSetGeneral_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,75),_UpsAlarmGenSetGeneral_Type())
upsAlarmGenSetGeneral.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmGenSetGeneral.setStatus(_A)
_UpsAlarmGenSetFault_Type=Integer32
_UpsAlarmGenSetFault_Object=MibScalar
upsAlarmGenSetFault=_UpsAlarmGenSetFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,76),_UpsAlarmGenSetFault_Type())
upsAlarmGenSetFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmGenSetFault.setStatus(_A)
_UpsAlarmEmergencyStopActive_Type=Integer32
_UpsAlarmEmergencyStopActive_Object=MibScalar
upsAlarmEmergencyStopActive=_UpsAlarmEmergencyStopActive_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,77),_UpsAlarmEmergencyStopActive_Type())
upsAlarmEmergencyStopActive.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmEmergencyStopActive.setStatus(_A)
_UpsAlarmBatteryCircuitOpen_Type=Integer32
_UpsAlarmBatteryCircuitOpen_Object=MibScalar
upsAlarmBatteryCircuitOpen=_UpsAlarmBatteryCircuitOpen_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,78),_UpsAlarmBatteryCircuitOpen_Type())
upsAlarmBatteryCircuitOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBatteryCircuitOpen.setStatus(_A)
_UpsAlarmFansFailure_Type=Integer32
_UpsAlarmFansFailure_Object=MibScalar
upsAlarmFansFailure=_UpsAlarmFansFailure_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,79),_UpsAlarmFansFailure_Type())
upsAlarmFansFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmFansFailure.setStatus(_A)
_UpsAlarmPhaseRotationFault_Type=Integer32
_UpsAlarmPhaseRotationFault_Object=MibScalar
upsAlarmPhaseRotationFault=_UpsAlarmPhaseRotationFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,80),_UpsAlarmPhaseRotationFault_Type())
upsAlarmPhaseRotationFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmPhaseRotationFault.setStatus(_A)
_UpsAlarmBypassFault_Type=Integer32
_UpsAlarmBypassFault_Object=MibScalar
upsAlarmBypassFault=_UpsAlarmBypassFault_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,81),_UpsAlarmBypassFault_Type())
upsAlarmBypassFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBypassFault.setStatus(_A)
_UpsAlarmA63_Type=Integer32
_UpsAlarmA63_Object=MibScalar
upsAlarmA63=_UpsAlarmA63_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,82),_UpsAlarmA63_Type())
upsAlarmA63.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmA63.setStatus(_A)
_UpsAlarmModule7Alarm_Type=Integer32
_UpsAlarmModule7Alarm_Object=MibScalar
upsAlarmModule7Alarm=_UpsAlarmModule7Alarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,83),_UpsAlarmModule7Alarm_Type())
upsAlarmModule7Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmModule7Alarm.setStatus(_A)
_UpsAlarmModule8Alarm_Type=Integer32
_UpsAlarmModule8Alarm_Object=MibScalar
upsAlarmModule8Alarm=_UpsAlarmModule8Alarm_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,84),_UpsAlarmModule8Alarm_Type())
upsAlarmModule8Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmModule8Alarm.setStatus(_A)
_UpsAlarmBatteryTemperature_Type=Integer32
_UpsAlarmBatteryTemperature_Object=MibScalar
upsAlarmBatteryTemperature=_UpsAlarmBatteryTemperature_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,85),_UpsAlarmBatteryTemperature_Type())
upsAlarmBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmBatteryTemperature.setStatus(_A)
_UpsAlarmRecRedundancy_Type=Integer32
_UpsAlarmRecRedundancy_Object=MibScalar
upsAlarmRecRedundancy=_UpsAlarmRecRedundancy_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,86),_UpsAlarmRecRedundancy_Type())
upsAlarmRecRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmRecRedundancy.setStatus(_A)
_UpsAlarmInvRedundancy_Type=Integer32
_UpsAlarmInvRedundancy_Object=MibScalar
upsAlarmInvRedundancy=_UpsAlarmInvRedundancy_Object((1,3,6,1,4,1,4555,1,1,1,1,6,3,87),_UpsAlarmInvRedundancy_Type())
upsAlarmInvRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmInvRedundancy.setStatus(_A)
_UpsTest_ObjectIdentity=ObjectIdentity
upsTest=_UpsTest_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,7))
_UpsTestId_Type=ObjectIdentifier
_UpsTestId_Object=MibScalar
upsTestId=_UpsTestId_Object((1,3,6,1,4,1,4555,1,1,1,1,7,1),_UpsTestId_Type())
upsTestId.setMaxAccess(_D)
if mibBuilder.loadTexts:upsTestId.setStatus(_A)
_UpsTestSpinLock_Type=TestAndIncr
_UpsTestSpinLock_Object=MibScalar
upsTestSpinLock=_UpsTestSpinLock_Object((1,3,6,1,4,1,4555,1,1,1,1,7,2),_UpsTestSpinLock_Type())
upsTestSpinLock.setMaxAccess(_D)
if mibBuilder.loadTexts:upsTestSpinLock.setStatus(_A)
class _UpsTestResultsSummary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notActive',1),('inProgress',2),('byPass',3),('failed',4)))
_UpsTestResultsSummary_Type.__name__=_E
_UpsTestResultsSummary_Object=MibScalar
upsTestResultsSummary=_UpsTestResultsSummary_Object((1,3,6,1,4,1,4555,1,1,1,1,7,3),_UpsTestResultsSummary_Type())
upsTestResultsSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestResultsSummary.setStatus(_A)
_UpsTestResultsDetail_Type=DisplayString
_UpsTestResultsDetail_Object=MibScalar
upsTestResultsDetail=_UpsTestResultsDetail_Object((1,3,6,1,4,1,4555,1,1,1,1,7,4),_UpsTestResultsDetail_Type())
upsTestResultsDetail.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestResultsDetail.setStatus(_A)
_UpsTestStartTime_Type=TimeStamp
_UpsTestStartTime_Object=MibScalar
upsTestStartTime=_UpsTestStartTime_Object((1,3,6,1,4,1,4555,1,1,1,1,7,5),_UpsTestStartTime_Type())
upsTestStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestStartTime.setStatus(_A)
_UpsTestElapsedTime_Type=TimeInterval
_UpsTestElapsedTime_Object=MibScalar
upsTestElapsedTime=_UpsTestElapsedTime_Object((1,3,6,1,4,1,4555,1,1,1,1,7,6),_UpsTestElapsedTime_Type())
upsTestElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestElapsedTime.setStatus(_A)
_UpsWellKnownTests_ObjectIdentity=ObjectIdentity
upsWellKnownTests=_UpsWellKnownTests_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,7,7))
_UpsTestNoTestsInitiated_Type=Integer32
_UpsTestNoTestsInitiated_Object=MibScalar
upsTestNoTestsInitiated=_UpsTestNoTestsInitiated_Object((1,3,6,1,4,1,4555,1,1,1,1,7,7,1),_UpsTestNoTestsInitiated_Type())
upsTestNoTestsInitiated.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestNoTestsInitiated.setStatus(_A)
_UpsTestAbortTestInProgress_Type=Integer32
_UpsTestAbortTestInProgress_Object=MibScalar
upsTestAbortTestInProgress=_UpsTestAbortTestInProgress_Object((1,3,6,1,4,1,4555,1,1,1,1,7,7,2),_UpsTestAbortTestInProgress_Type())
upsTestAbortTestInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestAbortTestInProgress.setStatus(_A)
_UpsTestGeneralSystemsTest_Type=Integer32
_UpsTestGeneralSystemsTest_Object=MibScalar
upsTestGeneralSystemsTest=_UpsTestGeneralSystemsTest_Object((1,3,6,1,4,1,4555,1,1,1,1,7,7,3),_UpsTestGeneralSystemsTest_Type())
upsTestGeneralSystemsTest.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestGeneralSystemsTest.setStatus(_A)
_UpsTestQuickBatteryTest_Type=Integer32
_UpsTestQuickBatteryTest_Object=MibScalar
upsTestQuickBatteryTest=_UpsTestQuickBatteryTest_Object((1,3,6,1,4,1,4555,1,1,1,1,7,7,4),_UpsTestQuickBatteryTest_Type())
upsTestQuickBatteryTest.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestQuickBatteryTest.setStatus(_A)
_UpsDeepBatteryCalibration_Type=Integer32
_UpsDeepBatteryCalibration_Object=MibScalar
upsDeepBatteryCalibration=_UpsDeepBatteryCalibration_Object((1,3,6,1,4,1,4555,1,1,1,1,7,7,5),_UpsDeepBatteryCalibration_Type())
upsDeepBatteryCalibration.setMaxAccess(_B)
if mibBuilder.loadTexts:upsDeepBatteryCalibration.setStatus(_A)
_UpsControl_ObjectIdentity=ObjectIdentity
upsControl=_UpsControl_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,8))
class _UpsControlStatusControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('upsStandbyOn',1),('upsStandbyOff',2),('upsEcoMode',3),('upsNormalMode',4),('upsAlarmReset',5),('upsCommandReset',6),('upsBuzzerOff',7),('upsOnBypass',8),('upsOnInverter',9)))
_UpsControlStatusControl_Type.__name__=_E
_UpsControlStatusControl_Object=MibScalar
upsControlStatusControl=_UpsControlStatusControl_Object((1,3,6,1,4,1,4555,1,1,1,1,8,1),_UpsControlStatusControl_Type())
upsControlStatusControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlStatusControl.setStatus(_A)
_UpsShutdownDelay_Type=Integer32
_UpsShutdownDelay_Object=MibScalar
upsShutdownDelay=_UpsShutdownDelay_Object((1,3,6,1,4,1,4555,1,1,1,1,8,2),_UpsShutdownDelay_Type())
upsShutdownDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsShutdownDelay.setStatus(_A)
class _UpsTurnOffAfterShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_UpsTurnOffAfterShutdown_Type.__name__=_E
_UpsTurnOffAfterShutdown_Object=MibScalar
upsTurnOffAfterShutdown=_UpsTurnOffAfterShutdown_Object((1,3,6,1,4,1,4555,1,1,1,1,8,3),_UpsTurnOffAfterShutdown_Type())
upsTurnOffAfterShutdown.setMaxAccess(_D)
if mibBuilder.loadTexts:upsTurnOffAfterShutdown.setStatus(_A)
_UpsControlShutdownParametersTable_Object=MibTable
upsControlShutdownParametersTable=_UpsControlShutdownParametersTable_Object((1,3,6,1,4,1,4555,1,1,1,1,8,4))
if mibBuilder.loadTexts:upsControlShutdownParametersTable.setStatus(_A)
_ShutdownParametersEntry_Object=MibTableRow
shutdownParametersEntry=_ShutdownParametersEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,8,4,1))
shutdownParametersEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:shutdownParametersEntry.setStatus(_A)
_UpsControlEventDescr_Type=DisplayString
_UpsControlEventDescr_Object=MibTableColumn
upsControlEventDescr=_UpsControlEventDescr_Object((1,3,6,1,4,1,4555,1,1,1,1,8,4,1,1),_UpsControlEventDescr_Type())
upsControlEventDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:upsControlEventDescr.setStatus(_A)
class _UpsControlEventStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_UpsControlEventStatus_Type.__name__=_E
_UpsControlEventStatus_Object=MibTableColumn
upsControlEventStatus=_UpsControlEventStatus_Object((1,3,6,1,4,1,4555,1,1,1,1,8,4,1,2),_UpsControlEventStatus_Type())
upsControlEventStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlEventStatus.setStatus(_A)
class _UpsControlDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_UpsControlDelay_Type.__name__=_E
_UpsControlDelay_Object=MibTableColumn
upsControlDelay=_UpsControlDelay_Object((1,3,6,1,4,1,4555,1,1,1,1,8,4,1,3),_UpsControlDelay_Type())
upsControlDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlDelay.setStatus(_A)
class _UpsControlFirstWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_UpsControlFirstWarning_Type.__name__=_E
_UpsControlFirstWarning_Object=MibTableColumn
upsControlFirstWarning=_UpsControlFirstWarning_Object((1,3,6,1,4,1,4555,1,1,1,1,8,4,1,4),_UpsControlFirstWarning_Type())
upsControlFirstWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlFirstWarning.setStatus(_A)
class _UpsControlWarningInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_UpsControlWarningInterval_Type.__name__=_E
_UpsControlWarningInterval_Object=MibTableColumn
upsControlWarningInterval=_UpsControlWarningInterval_Object((1,3,6,1,4,1,4555,1,1,1,1,8,4,1,5),_UpsControlWarningInterval_Type())
upsControlWarningInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlWarningInterval.setStatus(_A)
_UpsControlWeeklyScheduleTable_Object=MibTable
upsControlWeeklyScheduleTable=_UpsControlWeeklyScheduleTable_Object((1,3,6,1,4,1,4555,1,1,1,1,8,5))
if mibBuilder.loadTexts:upsControlWeeklyScheduleTable.setStatus(_A)
_UpsControlWeeklyScheduleEntry_Object=MibTableRow
upsControlWeeklyScheduleEntry=_UpsControlWeeklyScheduleEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,8,5,1))
upsControlWeeklyScheduleEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:upsControlWeeklyScheduleEntry.setStatus(_A)
class _UpsControlWeeklyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_UpsControlWeeklyIndex_Type.__name__=_E
_UpsControlWeeklyIndex_Object=MibTableColumn
upsControlWeeklyIndex=_UpsControlWeeklyIndex_Object((1,3,6,1,4,1,4555,1,1,1,1,8,5,1,1),_UpsControlWeeklyIndex_Type())
upsControlWeeklyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsControlWeeklyIndex.setStatus(_A)
class _UpsControlWeeklyShutdownDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_I,8)))
_UpsControlWeeklyShutdownDay_Type.__name__=_E
_UpsControlWeeklyShutdownDay_Object=MibTableColumn
upsControlWeeklyShutdownDay=_UpsControlWeeklyShutdownDay_Object((1,3,6,1,4,1,4555,1,1,1,1,8,5,1,2),_UpsControlWeeklyShutdownDay_Type())
upsControlWeeklyShutdownDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlWeeklyShutdownDay.setStatus(_A)
class _UpsControlWeeklyShutdownTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsControlWeeklyShutdownTime_Type.__name__=_G
_UpsControlWeeklyShutdownTime_Object=MibTableColumn
upsControlWeeklyShutdownTime=_UpsControlWeeklyShutdownTime_Object((1,3,6,1,4,1,4555,1,1,1,1,8,5,1,3),_UpsControlWeeklyShutdownTime_Type())
upsControlWeeklyShutdownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlWeeklyShutdownTime.setStatus(_A)
class _UpsControlWeeklyRestartDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_I,8)))
_UpsControlWeeklyRestartDay_Type.__name__=_E
_UpsControlWeeklyRestartDay_Object=MibTableColumn
upsControlWeeklyRestartDay=_UpsControlWeeklyRestartDay_Object((1,3,6,1,4,1,4555,1,1,1,1,8,5,1,4),_UpsControlWeeklyRestartDay_Type())
upsControlWeeklyRestartDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlWeeklyRestartDay.setStatus(_A)
class _UpsControlWeeklyRestartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsControlWeeklyRestartTime_Type.__name__=_G
_UpsControlWeeklyRestartTime_Object=MibTableColumn
upsControlWeeklyRestartTime=_UpsControlWeeklyRestartTime_Object((1,3,6,1,4,1,4555,1,1,1,1,8,5,1,5),_UpsControlWeeklyRestartTime_Type())
upsControlWeeklyRestartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlWeeklyRestartTime.setStatus(_A)
_UpsControlSpecialScheduleTable_Object=MibTable
upsControlSpecialScheduleTable=_UpsControlSpecialScheduleTable_Object((1,3,6,1,4,1,4555,1,1,1,1,8,6))
if mibBuilder.loadTexts:upsControlSpecialScheduleTable.setStatus(_A)
_UpsControlSpecialScheduleEntry_Object=MibTableRow
upsControlSpecialScheduleEntry=_UpsControlSpecialScheduleEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,8,6,1))
upsControlSpecialScheduleEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:upsControlSpecialScheduleEntry.setStatus(_A)
class _UpsControlSpecialIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_UpsControlSpecialIndex_Type.__name__=_E
_UpsControlSpecialIndex_Object=MibTableColumn
upsControlSpecialIndex=_UpsControlSpecialIndex_Object((1,3,6,1,4,1,4555,1,1,1,1,8,6,1,1),_UpsControlSpecialIndex_Type())
upsControlSpecialIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsControlSpecialIndex.setStatus(_A)
class _UpsControlSpecialShutdownDay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_UpsControlSpecialShutdownDay_Type.__name__=_G
_UpsControlSpecialShutdownDay_Object=MibTableColumn
upsControlSpecialShutdownDay=_UpsControlSpecialShutdownDay_Object((1,3,6,1,4,1,4555,1,1,1,1,8,6,1,2),_UpsControlSpecialShutdownDay_Type())
upsControlSpecialShutdownDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlSpecialShutdownDay.setStatus(_A)
class _UpsControlSpecialShutdownTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsControlSpecialShutdownTime_Type.__name__=_G
_UpsControlSpecialShutdownTime_Object=MibTableColumn
upsControlSpecialShutdownTime=_UpsControlSpecialShutdownTime_Object((1,3,6,1,4,1,4555,1,1,1,1,8,6,1,3),_UpsControlSpecialShutdownTime_Type())
upsControlSpecialShutdownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlSpecialShutdownTime.setStatus(_A)
class _UpsControlSpecialRestartDay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_UpsControlSpecialRestartDay_Type.__name__=_G
_UpsControlSpecialRestartDay_Object=MibTableColumn
upsControlSpecialRestartDay=_UpsControlSpecialRestartDay_Object((1,3,6,1,4,1,4555,1,1,1,1,8,6,1,4),_UpsControlSpecialRestartDay_Type())
upsControlSpecialRestartDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlSpecialRestartDay.setStatus(_A)
class _UpsControlSpecialRestartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsControlSpecialRestartTime_Type.__name__=_G
_UpsControlSpecialRestartTime_Object=MibTableColumn
upsControlSpecialRestartTime=_UpsControlSpecialRestartTime_Object((1,3,6,1,4,1,4555,1,1,1,1,8,6,1,5),_UpsControlSpecialRestartTime_Type())
upsControlSpecialRestartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlSpecialRestartTime.setStatus(_A)
_UpsControlEcoModeScheduleTable_Object=MibTable
upsControlEcoModeScheduleTable=_UpsControlEcoModeScheduleTable_Object((1,3,6,1,4,1,4555,1,1,1,1,8,7))
if mibBuilder.loadTexts:upsControlEcoModeScheduleTable.setStatus(_A)
_UpsControlEcoModeScheduleEntry_Object=MibTableRow
upsControlEcoModeScheduleEntry=_UpsControlEcoModeScheduleEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,8,7,1))
upsControlEcoModeScheduleEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:upsControlEcoModeScheduleEntry.setStatus(_A)
class _UpsControlEcoModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_UpsControlEcoModeIndex_Type.__name__=_E
_UpsControlEcoModeIndex_Object=MibTableColumn
upsControlEcoModeIndex=_UpsControlEcoModeIndex_Object((1,3,6,1,4,1,4555,1,1,1,1,8,7,1,1),_UpsControlEcoModeIndex_Type())
upsControlEcoModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsControlEcoModeIndex.setStatus(_A)
class _UpsControlEcoModeStartDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_I,8)))
_UpsControlEcoModeStartDay_Type.__name__=_E
_UpsControlEcoModeStartDay_Object=MibTableColumn
upsControlEcoModeStartDay=_UpsControlEcoModeStartDay_Object((1,3,6,1,4,1,4555,1,1,1,1,8,7,1,2),_UpsControlEcoModeStartDay_Type())
upsControlEcoModeStartDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlEcoModeStartDay.setStatus(_A)
class _UpsControlEcoModeStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsControlEcoModeStartTime_Type.__name__=_G
_UpsControlEcoModeStartTime_Object=MibTableColumn
upsControlEcoModeStartTime=_UpsControlEcoModeStartTime_Object((1,3,6,1,4,1,4555,1,1,1,1,8,7,1,3),_UpsControlEcoModeStartTime_Type())
upsControlEcoModeStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlEcoModeStartTime.setStatus(_A)
class _UpsControlEcoModeEndDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_I,8)))
_UpsControlEcoModeEndDay_Type.__name__=_E
_UpsControlEcoModeEndDay_Object=MibTableColumn
upsControlEcoModeEndDay=_UpsControlEcoModeEndDay_Object((1,3,6,1,4,1,4555,1,1,1,1,8,7,1,4),_UpsControlEcoModeEndDay_Type())
upsControlEcoModeEndDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlEcoModeEndDay.setStatus(_A)
class _UpsControlEcoModeEndTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsControlEcoModeEndTime_Type.__name__=_G
_UpsControlEcoModeEndTime_Object=MibTableColumn
upsControlEcoModeEndTime=_UpsControlEcoModeEndTime_Object((1,3,6,1,4,1,4555,1,1,1,1,8,7,1,5),_UpsControlEcoModeEndTime_Type())
upsControlEcoModeEndTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsControlEcoModeEndTime.setStatus(_A)
_UpsConfig_ObjectIdentity=ObjectIdentity
upsConfig=_UpsConfig_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,9))
_UpsConfigInputVoltage_Type=Integer32
_UpsConfigInputVoltage_Object=MibScalar
upsConfigInputVoltage=_UpsConfigInputVoltage_Object((1,3,6,1,4,1,4555,1,1,1,1,9,1),_UpsConfigInputVoltage_Type())
upsConfigInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigInputVoltage.setStatus(_A)
_UpsConfigInputFreq_Type=Integer32
_UpsConfigInputFreq_Object=MibScalar
upsConfigInputFreq=_UpsConfigInputFreq_Object((1,3,6,1,4,1,4555,1,1,1,1,9,2),_UpsConfigInputFreq_Type())
upsConfigInputFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigInputFreq.setStatus(_A)
_UpsConfigOutputVoltage_Type=Integer32
_UpsConfigOutputVoltage_Object=MibScalar
upsConfigOutputVoltage=_UpsConfigOutputVoltage_Object((1,3,6,1,4,1,4555,1,1,1,1,9,3),_UpsConfigOutputVoltage_Type())
upsConfigOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigOutputVoltage.setStatus(_A)
_UpsConfigOutputFreq_Type=Integer32
_UpsConfigOutputFreq_Object=MibScalar
upsConfigOutputFreq=_UpsConfigOutputFreq_Object((1,3,6,1,4,1,4555,1,1,1,1,9,4),_UpsConfigOutputFreq_Type())
upsConfigOutputFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigOutputFreq.setStatus(_A)
_UpsDevicesTable_Object=MibTable
upsDevicesTable=_UpsDevicesTable_Object((1,3,6,1,4,1,4555,1,1,1,1,9,5))
if mibBuilder.loadTexts:upsDevicesTable.setStatus(_A)
_UpsDevicesEntry_Object=MibTableRow
upsDevicesEntry=_UpsDevicesEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,9,5,1))
upsDevicesEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:upsDevicesEntry.setStatus(_A)
class _IndexOfDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IndexOfDevice_Type.__name__=_E
_IndexOfDevice_Object=MibTableColumn
indexOfDevice=_IndexOfDevice_Object((1,3,6,1,4,1,4555,1,1,1,1,9,5,1,1),_IndexOfDevice_Type())
indexOfDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:indexOfDevice.setStatus(_A)
_AddrOfDevice_Type=IpAddress
_AddrOfDevice_Object=MibTableColumn
addrOfDevice=_AddrOfDevice_Object((1,3,6,1,4,1,4555,1,1,1,1,9,5,1,2),_AddrOfDevice_Type())
addrOfDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:addrOfDevice.setStatus(_A)
class _NameOfDevice_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_NameOfDevice_Type.__name__=_G
_NameOfDevice_Object=MibTableColumn
nameOfDevice=_NameOfDevice_Object((1,3,6,1,4,1,4555,1,1,1,1,9,5,1,3),_NameOfDevice_Type())
nameOfDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:nameOfDevice.setStatus(_A)
_TimeOfConnection_Type=DisplayString
_TimeOfConnection_Object=MibTableColumn
timeOfConnection=_TimeOfConnection_Object((1,3,6,1,4,1,4555,1,1,1,1,9,5,1,4),_TimeOfConnection_Type())
timeOfConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:timeOfConnection.setStatus(_A)
_StatusOfConnection_Type=Integer32
_StatusOfConnection_Object=MibTableColumn
statusOfConnection=_StatusOfConnection_Object((1,3,6,1,4,1,4555,1,1,1,1,9,5,1,5),_StatusOfConnection_Type())
statusOfConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:statusOfConnection.setStatus(_A)
_SeverityOfConnection_Type=Integer32
_SeverityOfConnection_Object=MibTableColumn
severityOfConnection=_SeverityOfConnection_Object((1,3,6,1,4,1,4555,1,1,1,1,9,5,1,6),_SeverityOfConnection_Type())
severityOfConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:severityOfConnection.setStatus(_A)
_UpsAgent_ObjectIdentity=ObjectIdentity
upsAgent=_UpsAgent_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,10))
_UpsAgentIpaddress_Type=IpAddress
_UpsAgentIpaddress_Object=MibScalar
upsAgentIpaddress=_UpsAgentIpaddress_Object((1,3,6,1,4,1,4555,1,1,1,1,10,1),_UpsAgentIpaddress_Type())
upsAgentIpaddress.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentIpaddress.setStatus(_A)
_UpsAgentGateway_Type=IpAddress
_UpsAgentGateway_Object=MibScalar
upsAgentGateway=_UpsAgentGateway_Object((1,3,6,1,4,1,4555,1,1,1,1,10,2),_UpsAgentGateway_Type())
upsAgentGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentGateway.setStatus(_A)
_UpsAgentSubnetMask_Type=IpAddress
_UpsAgentSubnetMask_Object=MibScalar
upsAgentSubnetMask=_UpsAgentSubnetMask_Object((1,3,6,1,4,1,4555,1,1,1,1,10,3),_UpsAgentSubnetMask_Type())
upsAgentSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentSubnetMask.setStatus(_A)
class _UpsAgentDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_UpsAgentDate_Type.__name__=_G
_UpsAgentDate_Object=MibScalar
upsAgentDate=_UpsAgentDate_Object((1,3,6,1,4,1,4555,1,1,1,1,10,4),_UpsAgentDate_Type())
upsAgentDate.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentDate.setStatus(_A)
class _UpsAgentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_UpsAgentTime_Type.__name__=_G
_UpsAgentTime_Object=MibScalar
upsAgentTime=_UpsAgentTime_Object((1,3,6,1,4,1,4555,1,1,1,1,10,5),_UpsAgentTime_Type())
upsAgentTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentTime.setStatus(_A)
_UpsAgentNtpTimeServer_Type=DisplayString
_UpsAgentNtpTimeServer_Object=MibScalar
upsAgentNtpTimeServer=_UpsAgentNtpTimeServer_Object((1,3,6,1,4,1,4555,1,1,1,1,10,6),_UpsAgentNtpTimeServer_Type())
upsAgentNtpTimeServer.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentNtpTimeServer.setStatus(_A)
class _UpsAgentNtpTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77)));namedValues=NamedValues(*(('gmt1200dateLineWest',1),('gmt1200kwajalein',2),('gmt1100samoa',3),('gmt1000hawaii',4),('gmt0900alaska',5),('gmt0800tijuana',6),('gmt0700arizona',7),('gmt0700chihuahua',8),('gmt0700mountain',9),('gmt0600camerica',10),('gmt0600ctime',11),('gmt0600guadalajara',12),('gmt0600saskatchewan',13),('gmt0500quito',14),('gmt0500etime',15),('gmt0500indiana',16),('gmt0400atime',17),('gmt0400caracas',18),('gmt0400santiago',19),('gmt0300newfoundland',20),('gmt0300brasilia',21),('gmt0300georgetown',22),('gmt0300greenland',23),('gmt0200atlantic',24),('gmt0100azores',25),('gmt0100cvi',26),('gmt0000monrovia',27),('gmt0000london',28),('gmt0100vienna',29),('gmt0100prague',30),('gmt0100paris',31),('gmt0100zagreb',32),('gmt0100wcafrica',33),('gmt0200minsk',34),('gmt0200bucharest',35),('gmt0200cairo',36),('gmt0200pretoria',37),('gmt0200vilnius',38),('gmt0200jerusalem',39),('gmt0300maghdad',40),('gmt0300riyadh',41),('gmt0300volgograd',42),('gmt0300nairobi',43),('gmt0300tehran',44),('gmt0400muscat',45),('gmt0400yerevan',46),('gmt0400kabul',47),('gmt0500ekaterinburg',48),('gmt0500tashkent',49),('gmt0500calcutta',50),('gmt0500mumbai',51),('gmt0500kathmandu',52),('gmt0600novosibirsk',53),('gmt0600dhaka',54),('gmt0600jayawardenepura',55),('gmt0600rangoon',56),('gmt0700bangkok',57),('gmt0700krasnoyarsk',58),('gmt0800beijing',59),('gmt0800irkutsk',60),('gmt0800singapore',61),('gmt0800perth',62),('gmt0800taipei',63),('gmt0900tokyo',64),('gmt0900seoul',65),('gmt0900yakutsk',66),('gmt0900adelaide',67),('gmt0900darwin',68),('gmt1000brisbane',69),('gmt1000canberra',70),('gmt1000guam',71),('gmt1000hobart',72),('gmt1000vladivostok',73),('gmt1100magadan',74),('gmt1200auckland',75),('gmt1200fiji',76),('gmt1300alofa',77)))
_UpsAgentNtpTimeZone_Type.__name__=_E
_UpsAgentNtpTimeZone_Object=MibScalar
upsAgentNtpTimeZone=_UpsAgentNtpTimeZone_Object((1,3,6,1,4,1,4555,1,1,1,1,10,7),_UpsAgentNtpTimeZone_Type())
upsAgentNtpTimeZone.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentNtpTimeZone.setStatus(_A)
class _UpsAgentHistoryLogFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,21600))
_UpsAgentHistoryLogFrequency_Type.__name__=_E
_UpsAgentHistoryLogFrequency_Object=MibScalar
upsAgentHistoryLogFrequency=_UpsAgentHistoryLogFrequency_Object((1,3,6,1,4,1,4555,1,1,1,1,10,8),_UpsAgentHistoryLogFrequency_Type())
upsAgentHistoryLogFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentHistoryLogFrequency.setStatus(_A)
class _UpsAgentExtHistoryLogFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10080))
_UpsAgentExtHistoryLogFrequency_Type.__name__=_E
_UpsAgentExtHistoryLogFrequency_Object=MibScalar
upsAgentExtHistoryLogFrequency=_UpsAgentExtHistoryLogFrequency_Object((1,3,6,1,4,1,4555,1,1,1,1,10,9),_UpsAgentExtHistoryLogFrequency_Type())
upsAgentExtHistoryLogFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentExtHistoryLogFrequency.setStatus(_A)
class _UpsAgentPollRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,60))
_UpsAgentPollRate_Type.__name__=_E
_UpsAgentPollRate_Object=MibScalar
upsAgentPollRate=_UpsAgentPollRate_Object((1,3,6,1,4,1,4555,1,1,1,1,10,10),_UpsAgentPollRate_Type())
upsAgentPollRate.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentPollRate.setStatus(_A)
class _UpsAgentBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('br2400',1),('br9600',2),('br19200',3)))
_UpsAgentBaudRate_Type.__name__=_E
_UpsAgentBaudRate_Object=MibScalar
upsAgentBaudRate=_UpsAgentBaudRate_Object((1,3,6,1,4,1,4555,1,1,1,1,10,11),_UpsAgentBaudRate_Type())
upsAgentBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentBaudRate.setStatus(_A)
class _UpsAgentDhcpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_UpsAgentDhcpStatus_Type.__name__=_E
_UpsAgentDhcpStatus_Object=MibScalar
upsAgentDhcpStatus=_UpsAgentDhcpStatus_Object((1,3,6,1,4,1,4555,1,1,1,1,10,12),_UpsAgentDhcpStatus_Type())
upsAgentDhcpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentDhcpStatus.setStatus(_A)
class _UpsAgentTelnetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_UpsAgentTelnetStatus_Type.__name__=_E
_UpsAgentTelnetStatus_Object=MibScalar
upsAgentTelnetStatus=_UpsAgentTelnetStatus_Object((1,3,6,1,4,1,4555,1,1,1,1,10,13),_UpsAgentTelnetStatus_Type())
upsAgentTelnetStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentTelnetStatus.setStatus(_A)
class _UpsAgentTftpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_UpsAgentTftpStatus_Type.__name__=_E
_UpsAgentTftpStatus_Object=MibScalar
upsAgentTftpStatus=_UpsAgentTftpStatus_Object((1,3,6,1,4,1,4555,1,1,1,1,10,14),_UpsAgentTftpStatus_Type())
upsAgentTftpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentTftpStatus.setStatus(_A)
class _UpsAgentResetToDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_H,2)))
_UpsAgentResetToDefault_Type.__name__=_E
_UpsAgentResetToDefault_Object=MibScalar
upsAgentResetToDefault=_UpsAgentResetToDefault_Object((1,3,6,1,4,1,4555,1,1,1,1,10,15),_UpsAgentResetToDefault_Type())
upsAgentResetToDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentResetToDefault.setStatus(_A)
class _UpsAgentRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),(_H,2)))
_UpsAgentRestart_Type.__name__=_E
_UpsAgentRestart_Object=MibScalar
upsAgentRestart=_UpsAgentRestart_Object((1,3,6,1,4,1,4555,1,1,1,1,10,16),_UpsAgentRestart_Type())
upsAgentRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentRestart.setStatus(_A)
class _UpsAgentClearAgentLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_H,2)))
_UpsAgentClearAgentLog_Type.__name__=_E
_UpsAgentClearAgentLog_Object=MibScalar
upsAgentClearAgentLog=_UpsAgentClearAgentLog_Object((1,3,6,1,4,1,4555,1,1,1,1,10,17),_UpsAgentClearAgentLog_Type())
upsAgentClearAgentLog.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentClearAgentLog.setStatus(_A)
class _UpsAgentClearEventLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_H,2)))
_UpsAgentClearEventLog_Type.__name__=_E
_UpsAgentClearEventLog_Object=MibScalar
upsAgentClearEventLog=_UpsAgentClearEventLog_Object((1,3,6,1,4,1,4555,1,1,1,1,10,18),_UpsAgentClearEventLog_Type())
upsAgentClearEventLog.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentClearEventLog.setStatus(_A)
class _UpsAgentClearExtHistoryLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_H,2)))
_UpsAgentClearExtHistoryLog_Type.__name__=_E
_UpsAgentClearExtHistoryLog_Object=MibScalar
upsAgentClearExtHistoryLog=_UpsAgentClearExtHistoryLog_Object((1,3,6,1,4,1,4555,1,1,1,1,10,19),_UpsAgentClearExtHistoryLog_Type())
upsAgentClearExtHistoryLog.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentClearExtHistoryLog.setStatus(_A)
class _UpsAgentClearHistoryLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_H,2)))
_UpsAgentClearHistoryLog_Type.__name__=_E
_UpsAgentClearHistoryLog_Object=MibScalar
upsAgentClearHistoryLog=_UpsAgentClearHistoryLog_Object((1,3,6,1,4,1,4555,1,1,1,1,10,20),_UpsAgentClearHistoryLog_Type())
upsAgentClearHistoryLog.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAgentClearHistoryLog.setStatus(_A)
_UpsAgentTrapsReceiversTable_Object=MibTable
upsAgentTrapsReceiversTable=_UpsAgentTrapsReceiversTable_Object((1,3,6,1,4,1,4555,1,1,1,1,10,21))
if mibBuilder.loadTexts:upsAgentTrapsReceiversTable.setStatus(_A)
_UpsAgentTrapsReceiversEntry_Object=MibTableRow
upsAgentTrapsReceiversEntry=_UpsAgentTrapsReceiversEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,10,21,1))
upsAgentTrapsReceiversEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:upsAgentTrapsReceiversEntry.setStatus(_A)
class _TrapsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TrapsIndex_Type.__name__=_E
_TrapsIndex_Object=MibTableColumn
trapsIndex=_TrapsIndex_Object((1,3,6,1,4,1,4555,1,1,1,1,10,21,1,1),_TrapsIndex_Type())
trapsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trapsIndex.setStatus(_A)
_TrapsReceiverAddr_Type=DisplayString
_TrapsReceiverAddr_Object=MibTableColumn
trapsReceiverAddr=_TrapsReceiverAddr_Object((1,3,6,1,4,1,4555,1,1,1,1,10,21,1,2),_TrapsReceiverAddr_Type())
trapsReceiverAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:trapsReceiverAddr.setStatus(_A)
class _ReceiverCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ReceiverCommunityString_Type.__name__=_G
_ReceiverCommunityString_Object=MibTableColumn
receiverCommunityString=_ReceiverCommunityString_Object((1,3,6,1,4,1,4555,1,1,1,1,10,21,1,3),_ReceiverCommunityString_Type())
receiverCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:receiverCommunityString.setStatus(_A)
class _ReceiverNmstype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('netVision-trap',2),('rfc1628-trap',3)))
_ReceiverNmstype_Type.__name__=_E
_ReceiverNmstype_Object=MibTableColumn
receiverNmstype=_ReceiverNmstype_Object((1,3,6,1,4,1,4555,1,1,1,1,10,21,1,4),_ReceiverNmstype_Type())
receiverNmstype.setMaxAccess(_D)
if mibBuilder.loadTexts:receiverNmstype.setStatus(_A)
_UpsAgentAccessControlTable_Object=MibTable
upsAgentAccessControlTable=_UpsAgentAccessControlTable_Object((1,3,6,1,4,1,4555,1,1,1,1,10,22))
if mibBuilder.loadTexts:upsAgentAccessControlTable.setStatus(_A)
_UpsAgentAccessControlEntry_Object=MibTableRow
upsAgentAccessControlEntry=_UpsAgentAccessControlEntry_Object((1,3,6,1,4,1,4555,1,1,1,1,10,22,1))
upsAgentAccessControlEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:upsAgentAccessControlEntry.setStatus(_A)
_AccessIndex_Type=Integer32
_AccessIndex_Object=MibTableColumn
accessIndex=_AccessIndex_Object((1,3,6,1,4,1,4555,1,1,1,1,10,22,1,1),_AccessIndex_Type())
accessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:accessIndex.setStatus(_A)
_AccessControlAddr_Type=DisplayString
_AccessControlAddr_Object=MibTableColumn
accessControlAddr=_AccessControlAddr_Object((1,3,6,1,4,1,4555,1,1,1,1,10,22,1,2),_AccessControlAddr_Type())
accessControlAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:accessControlAddr.setStatus(_A)
class _AccessCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AccessCommunityString_Type.__name__=_G
_AccessCommunityString_Object=MibTableColumn
accessCommunityString=_AccessCommunityString_Object((1,3,6,1,4,1,4555,1,1,1,1,10,22,1,3),_AccessCommunityString_Type())
accessCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:accessCommunityString.setStatus(_A)
class _AccessControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2),('notAccess',3)))
_AccessControlMode_Type.__name__=_E
_AccessControlMode_Object=MibTableColumn
accessControlMode=_AccessControlMode_Object((1,3,6,1,4,1,4555,1,1,1,1,10,22,1,4),_AccessControlMode_Type())
accessControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:accessControlMode.setStatus(_A)
_UpsAgentMibVersion_Type=Integer32
_UpsAgentMibVersion_Object=MibScalar
upsAgentMibVersion=_UpsAgentMibVersion_Object((1,3,6,1,4,1,4555,1,1,1,1,10,23),_UpsAgentMibVersion_Type())
upsAgentMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAgentMibVersion.setStatus(_A)
_UpsAgentTrapString_Type=DisplayString
_UpsAgentTrapString_Object=MibScalar
upsAgentTrapString=_UpsAgentTrapString_Object((1,3,6,1,4,1,4555,1,1,1,1,10,50),_UpsAgentTrapString_Type())
upsAgentTrapString.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAgentTrapString.setStatus(_A)
_EmdStatus_ObjectIdentity=ObjectIdentity
emdStatus=_EmdStatus_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,1,11))
_EmdSatatusTemperature_Type=Integer32
_EmdSatatusTemperature_Object=MibScalar
emdSatatusTemperature=_EmdSatatusTemperature_Object((1,3,6,1,4,1,4555,1,1,1,1,11,1),_EmdSatatusTemperature_Type())
emdSatatusTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:emdSatatusTemperature.setStatus(_A)
_EmdSatatusHumidity_Type=Integer32
_EmdSatatusHumidity_Object=MibScalar
emdSatatusHumidity=_EmdSatatusHumidity_Object((1,3,6,1,4,1,4555,1,1,1,1,11,2),_EmdSatatusHumidity_Type())
emdSatatusHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:emdSatatusHumidity.setStatus(_A)
_UpsTraps_ObjectIdentity=ObjectIdentity
upsTraps=_UpsTraps_ObjectIdentity((1,3,6,1,4,1,4555,1,1,1,2))
upsTrapOnBattery=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,1))
upsTrapOnBattery.setObjects(*((_C,_i),(_C,_j)))
if mibBuilder.loadTexts:upsTrapOnBattery.setStatus('')
upsTrapTestCompleted=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,2))
upsTrapTestCompleted.setObjects(*((_C,_k),(_C,_l),(_C,_m),(_C,_n),(_C,_o),(_C,_p)))
if mibBuilder.loadTexts:upsTrapTestCompleted.setStatus('')
upsTrapAlarmEntryAdded=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,3))
upsTrapAlarmEntryAdded.setObjects(*((_C,_J),(_C,_V)))
if mibBuilder.loadTexts:upsTrapAlarmEntryAdded.setStatus('')
upsTrapAlarmEntryRemoved=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,4))
upsTrapAlarmEntryRemoved.setObjects(*((_C,_J),(_C,_V)))
if mibBuilder.loadTexts:upsTrapAlarmEntryRemoved.setStatus('')
upsTrapUpsNormal=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,5))
upsTrapUpsNormal.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapUpsNormal.setStatus('')
upsTrapUpsBattTestFailed=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,6))
upsTrapUpsBattTestFailed.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapUpsBattTestFailed.setStatus('')
upsTrapOnBatteryPower=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,7))
upsTrapOnBatteryPower.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapOnBatteryPower.setStatus('')
upsTrapBatteryLow=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,8))
upsTrapBatteryLow.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapBatteryLow.setStatus('')
upsTrapPowerRestored=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,9))
upsTrapPowerRestored.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapPowerRestored.setStatus('')
upsTrapImminentStop=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,10))
upsTrapImminentStop.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapImminentStop.setStatus('')
upsTrapTurnedOff=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,11))
upsTrapTurnedOff.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapTurnedOff.setStatus('')
upsTrapOverTemperature=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,12))
upsTrapOverTemperature.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapOverTemperature.setStatus('')
upsTrapOverload=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,13))
upsTrapOverload.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapOverload.setStatus('')
upsTrapOnMains=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,14))
upsTrapOnMains.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapOnMains.setStatus('')
upsTrapRedoundancyLost=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,15))
upsTrapRedoundancyLost.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapRedoundancyLost.setStatus('')
upsTrapEmdTempLow=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,16))
upsTrapEmdTempLow.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdTempLow.setStatus('')
upsTrapEmdTempNotLow=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,17))
upsTrapEmdTempNotLow.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdTempNotLow.setStatus('')
upsTrapEmdTempHigh=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,18))
upsTrapEmdTempHigh.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdTempHigh.setStatus('')
upsTrapEmdTempNotHigh=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,19))
upsTrapEmdTempNotHigh.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdTempNotHigh.setStatus('')
upsTrapEmdHumidityLow=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,20))
upsTrapEmdHumidityLow.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdHumidityLow.setStatus('')
upsTrapEmdHumidityNotLow=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,21))
upsTrapEmdHumidityNotLow.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdHumidityNotLow.setStatus('')
upsTrapEmdHumidityHigh=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,22))
upsTrapEmdHumidityHigh.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdHumidityHigh.setStatus('')
upsTrapEmdHumidityNotHigh=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,23))
upsTrapEmdHumidityNotHigh.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdHumidityNotHigh.setStatus('')
upsTrapEmdFirstInputActive=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,24))
upsTrapEmdFirstInputActive.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdFirstInputActive.setStatus('')
upsTrapEmdFirstInputRestored=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,25))
upsTrapEmdFirstInputRestored.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdFirstInputRestored.setStatus('')
upsTrapEmdSecondInputActive=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,26))
upsTrapEmdSecondInputActive.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdSecondInputActive.setStatus('')
upsTrapEmdSecondInputRestored=NotificationType((1,3,6,1,4,1,4555,1,1,1,2,0,27))
upsTrapEmdSecondInputRestored.setObjects((_C,_F))
if mibBuilder.loadTexts:upsTrapEmdSecondInputRestored.setStatus('')
mibBuilder.exportSymbols(_C,**{'PositiveInteger':PositiveInteger,'NonNegativeInteger':NonNegativeInteger,'socomecSicon':socomecSicon,'software':software,'network':network,'netvision':netvision,'upsObjects':upsObjects,'upsIdent':upsIdent,'upsIdentModel':upsIdentModel,'upsIdentUPSFirmwareVersion':upsIdentUPSFirmwareVersion,'upsIdentAgentSoftwareVersion':upsIdentAgentSoftwareVersion,'upsIdentUpsSerialNumber':upsIdentUpsSerialNumber,'upsBattery':upsBattery,'upsBatteryStatus':upsBatteryStatus,_j:upsSecondsOnBattery,_i:upsEstimatedMinutesRemaining,'upsEstimatedChargeRemaining':upsEstimatedChargeRemaining,'upsBatteryVoltage':upsBatteryVoltage,'upsBatteryTemperature':upsBatteryTemperature,'upsInput':upsInput,'upsInputNumLines':upsInputNumLines,'upsInputFrequency':upsInputFrequency,'upsInputTable':upsInputTable,'upsInputEntry':upsInputEntry,_Y:upsInputLineIndex,'upsInputVoltage':upsInputVoltage,'upsInputCurrent':upsInputCurrent,'upsInputVoltageMax':upsInputVoltageMax,'upsInputVoltageMin':upsInputVoltageMin,'upsOutput':upsOutput,'upsOutputSource':upsOutputSource,'upsOutputFrequency':upsOutputFrequency,'upsOutputNumLines':upsOutputNumLines,'upsOutputTable':upsOutputTable,'upsOutputEntry':upsOutputEntry,_Z:upsOutputLineIndex,'upsOutputVoltage':upsOutputVoltage,'upsOutputCurrent':upsOutputCurrent,'upsOutputPercentLoad':upsOutputPercentLoad,'upsOutputKva':upsOutputKva,'upsBypass':upsBypass,'upsBypassFrequency':upsBypassFrequency,'upsBypassNumLines':upsBypassNumLines,'upsBypassTable':upsBypassTable,'upsBypassEntry':upsBypassEntry,_a:upsBypassLineIndex,'upsBypassVoltage':upsBypassVoltage,'upsBypassCurrent':upsBypassCurrent,'upsAlarm':upsAlarm,'upsAlarmsPresent':upsAlarmsPresent,'upsAlarmTable':upsAlarmTable,'upsAlarmEntry':upsAlarmEntry,_J:upsAlarmId,_V:upsAlarmDescr,'upsAlarmTime':upsAlarmTime,'upsAlarmExtDes':upsAlarmExtDes,'upsWellKnownAlarms':upsWellKnownAlarms,'upsAlarmBatteryBad':upsAlarmBatteryBad,'upsAlarmOnBattery':upsAlarmOnBattery,'upsAlarmLowBattery':upsAlarmLowBattery,'upsAlarmDepletedBattery':upsAlarmDepletedBattery,'upsAlarmTempBad':upsAlarmTempBad,'upsAlarmInputBad':upsAlarmInputBad,'upsAlarmOutputBad':upsAlarmOutputBad,'upsAlarmOutputOverload':upsAlarmOutputOverload,'upsAlarmOnBypass':upsAlarmOnBypass,'upsAlarmBypassBad':upsAlarmBypassBad,'upsAlarmOutputOffAsRequested':upsAlarmOutputOffAsRequested,'upsAlarmUpsOffAsRequested':upsAlarmUpsOffAsRequested,'upsAlarmChargerFailed':upsAlarmChargerFailed,'upsAlarmUpsOutputOff':upsAlarmUpsOutputOff,'upsAlarmUpsSystemOff':upsAlarmUpsSystemOff,'upsAlarmFanFailure':upsAlarmFanFailure,'upsAlarmFuseFailure':upsAlarmFuseFailure,'upsAlarmGeneralFault':upsAlarmGeneralFault,'upsAlarmDiagnosticTestFailed':upsAlarmDiagnosticTestFailed,'upsAlarmCommunicationLost':upsAlarmCommunicationLost,'upsAlarmAwaitingPower':upsAlarmAwaitingPower,'upsAlarmShutdownPending':upsAlarmShutdownPending,'upsAlarmShutdownImminent':upsAlarmShutdownImminent,'upsAlarmTestInProgress':upsAlarmTestInProgress,'upsAlarmPowerSupplyFault':upsAlarmPowerSupplyFault,'upsAlarmAuxMainFail':upsAlarmAuxMainFail,'upsAlarmManualBypassClose':upsAlarmManualBypassClose,'upsAlarmShortCircuit':upsAlarmShortCircuit,'upsAlarmBatteryChargerFailure':upsAlarmBatteryChargerFailure,'upsAlarmInverterOverCurrent':upsAlarmInverterOverCurrent,'upsAlarmInverterDistorsion':upsAlarmInverterDistorsion,'upsAlarmPrechargeVoltageFail':upsAlarmPrechargeVoltageFail,'upsAlarmBoostTooLow':upsAlarmBoostTooLow,'upsAlarmBoostTooHigh':upsAlarmBoostTooHigh,'upsAlarmBatteryTooHigh':upsAlarmBatteryTooHigh,'upsAlarmImproperCondition':upsAlarmImproperCondition,'upsAlarmOverloadTimeout':upsAlarmOverloadTimeout,'upsAlarmControlSystemFailure':upsAlarmControlSystemFailure,'upsAlarmDataCorrupted':upsAlarmDataCorrupted,'upsAlarmPllFault':upsAlarmPllFault,'upsAlarmInputGeneralAlarm':upsAlarmInputGeneralAlarm,'upsAlarmRectifierGeneralAlarm':upsAlarmRectifierGeneralAlarm,'upsAlarmBoostGeneralAlarm':upsAlarmBoostGeneralAlarm,'upsAlarmInverterGeneralAlarm':upsAlarmInverterGeneralAlarm,'upsAlarmBatteryGeneralAlarm':upsAlarmBatteryGeneralAlarm,'upsAlarmOutputOver':upsAlarmOutputOver,'upsAlarmOutputUnder':upsAlarmOutputUnder,'upsAlarmBypassGeneralAlarm':upsAlarmBypassGeneralAlarm,'upsAlarmStopForOverload':upsAlarmStopForOverload,'upsAlarmImminentStop':upsAlarmImminentStop,'upsAlarmModule1Alarm':upsAlarmModule1Alarm,'upsAlarmModule2Alarm':upsAlarmModule2Alarm,'upsAlarmModule3Alarm':upsAlarmModule3Alarm,'upsAlarmModule4Alarm':upsAlarmModule4Alarm,'upsAlarmModule5Alarm':upsAlarmModule5Alarm,'upsAlarmModule6Alarm':upsAlarmModule6Alarm,'upsAlarmExternalAlarm1':upsAlarmExternalAlarm1,'upsAlarmExternalAlarm2':upsAlarmExternalAlarm2,'upsAlarmExternalAlarm3':upsAlarmExternalAlarm3,'upsAlarmExternalAlarm4':upsAlarmExternalAlarm4,'upsAlarmEService':upsAlarmEService,'upsAlarmRedundancyLost':upsAlarmRedundancyLost,'upsAlarmPeriodicServiceCheck':upsAlarmPeriodicServiceCheck,'upsAlarmAllTransferDisabled':upsAlarmAllTransferDisabled,'upsAlarmAutoTransferDisabled':upsAlarmAutoTransferDisabled,'upsAlarmBatteryRoom':upsAlarmBatteryRoom,'upsAlarmManualBypass':upsAlarmManualBypass,'upsAlarmBatteryDischarged':upsAlarmBatteryDischarged,'upsAlarmInsufficientResources':upsAlarmInsufficientResources,'upsAlarmOptionalBoards':upsAlarmOptionalBoards,'upsAlarmRectifierFault':upsAlarmRectifierFault,'upsAlarmBoostFault':upsAlarmBoostFault,'upsAlarmInverterFault':upsAlarmInverterFault,'upsAlarmParallelModuleFault':upsAlarmParallelModuleFault,'upsAlarmGenSetGeneral':upsAlarmGenSetGeneral,'upsAlarmGenSetFault':upsAlarmGenSetFault,'upsAlarmEmergencyStopActive':upsAlarmEmergencyStopActive,'upsAlarmBatteryCircuitOpen':upsAlarmBatteryCircuitOpen,'upsAlarmFansFailure':upsAlarmFansFailure,'upsAlarmPhaseRotationFault':upsAlarmPhaseRotationFault,'upsAlarmBypassFault':upsAlarmBypassFault,'upsAlarmA63':upsAlarmA63,'upsAlarmModule7Alarm':upsAlarmModule7Alarm,'upsAlarmModule8Alarm':upsAlarmModule8Alarm,'upsAlarmBatteryTemperature':upsAlarmBatteryTemperature,'upsAlarmRecRedundancy':upsAlarmRecRedundancy,'upsAlarmInvRedundancy':upsAlarmInvRedundancy,'upsTest':upsTest,_k:upsTestId,_l:upsTestSpinLock,_m:upsTestResultsSummary,_n:upsTestResultsDetail,_o:upsTestStartTime,_p:upsTestElapsedTime,'upsWellKnownTests':upsWellKnownTests,'upsTestNoTestsInitiated':upsTestNoTestsInitiated,'upsTestAbortTestInProgress':upsTestAbortTestInProgress,'upsTestGeneralSystemsTest':upsTestGeneralSystemsTest,'upsTestQuickBatteryTest':upsTestQuickBatteryTest,'upsDeepBatteryCalibration':upsDeepBatteryCalibration,'upsControl':upsControl,'upsControlStatusControl':upsControlStatusControl,'upsShutdownDelay':upsShutdownDelay,'upsTurnOffAfterShutdown':upsTurnOffAfterShutdown,'upsControlShutdownParametersTable':upsControlShutdownParametersTable,'shutdownParametersEntry':shutdownParametersEntry,_d:upsControlEventDescr,'upsControlEventStatus':upsControlEventStatus,'upsControlDelay':upsControlDelay,'upsControlFirstWarning':upsControlFirstWarning,'upsControlWarningInterval':upsControlWarningInterval,'upsControlWeeklyScheduleTable':upsControlWeeklyScheduleTable,'upsControlWeeklyScheduleEntry':upsControlWeeklyScheduleEntry,_e:upsControlWeeklyIndex,'upsControlWeeklyShutdownDay':upsControlWeeklyShutdownDay,'upsControlWeeklyShutdownTime':upsControlWeeklyShutdownTime,'upsControlWeeklyRestartDay':upsControlWeeklyRestartDay,'upsControlWeeklyRestartTime':upsControlWeeklyRestartTime,'upsControlSpecialScheduleTable':upsControlSpecialScheduleTable,'upsControlSpecialScheduleEntry':upsControlSpecialScheduleEntry,_f:upsControlSpecialIndex,'upsControlSpecialShutdownDay':upsControlSpecialShutdownDay,'upsControlSpecialShutdownTime':upsControlSpecialShutdownTime,'upsControlSpecialRestartDay':upsControlSpecialRestartDay,'upsControlSpecialRestartTime':upsControlSpecialRestartTime,'upsControlEcoModeScheduleTable':upsControlEcoModeScheduleTable,'upsControlEcoModeScheduleEntry':upsControlEcoModeScheduleEntry,_g:upsControlEcoModeIndex,'upsControlEcoModeStartDay':upsControlEcoModeStartDay,'upsControlEcoModeStartTime':upsControlEcoModeStartTime,'upsControlEcoModeEndDay':upsControlEcoModeEndDay,'upsControlEcoModeEndTime':upsControlEcoModeEndTime,'upsConfig':upsConfig,'upsConfigInputVoltage':upsConfigInputVoltage,'upsConfigInputFreq':upsConfigInputFreq,'upsConfigOutputVoltage':upsConfigOutputVoltage,'upsConfigOutputFreq':upsConfigOutputFreq,'upsDevicesTable':upsDevicesTable,'upsDevicesEntry':upsDevicesEntry,_h:indexOfDevice,'addrOfDevice':addrOfDevice,'nameOfDevice':nameOfDevice,'timeOfConnection':timeOfConnection,'statusOfConnection':statusOfConnection,'severityOfConnection':severityOfConnection,'upsAgent':upsAgent,'upsAgentIpaddress':upsAgentIpaddress,'upsAgentGateway':upsAgentGateway,'upsAgentSubnetMask':upsAgentSubnetMask,'upsAgentDate':upsAgentDate,'upsAgentTime':upsAgentTime,'upsAgentNtpTimeServer':upsAgentNtpTimeServer,'upsAgentNtpTimeZone':upsAgentNtpTimeZone,'upsAgentHistoryLogFrequency':upsAgentHistoryLogFrequency,'upsAgentExtHistoryLogFrequency':upsAgentExtHistoryLogFrequency,'upsAgentPollRate':upsAgentPollRate,'upsAgentBaudRate':upsAgentBaudRate,'upsAgentDhcpStatus':upsAgentDhcpStatus,'upsAgentTelnetStatus':upsAgentTelnetStatus,'upsAgentTftpStatus':upsAgentTftpStatus,'upsAgentResetToDefault':upsAgentResetToDefault,'upsAgentRestart':upsAgentRestart,'upsAgentClearAgentLog':upsAgentClearAgentLog,'upsAgentClearEventLog':upsAgentClearEventLog,'upsAgentClearExtHistoryLog':upsAgentClearExtHistoryLog,'upsAgentClearHistoryLog':upsAgentClearHistoryLog,'upsAgentTrapsReceiversTable':upsAgentTrapsReceiversTable,'upsAgentTrapsReceiversEntry':upsAgentTrapsReceiversEntry,_U:trapsIndex,'trapsReceiverAddr':trapsReceiverAddr,'receiverCommunityString':receiverCommunityString,'receiverNmstype':receiverNmstype,'upsAgentAccessControlTable':upsAgentAccessControlTable,'upsAgentAccessControlEntry':upsAgentAccessControlEntry,'accessIndex':accessIndex,'accessControlAddr':accessControlAddr,'accessCommunityString':accessCommunityString,'accessControlMode':accessControlMode,'upsAgentMibVersion':upsAgentMibVersion,_F:upsAgentTrapString,'emdStatus':emdStatus,'emdSatatusTemperature':emdSatatusTemperature,'emdSatatusHumidity':emdSatatusHumidity,'upsTraps':upsTraps,'upsTrapOnBattery':upsTrapOnBattery,'upsTrapTestCompleted':upsTrapTestCompleted,'upsTrapAlarmEntryAdded':upsTrapAlarmEntryAdded,'upsTrapAlarmEntryRemoved':upsTrapAlarmEntryRemoved,'upsTrapUpsNormal':upsTrapUpsNormal,'upsTrapUpsBattTestFailed':upsTrapUpsBattTestFailed,'upsTrapOnBatteryPower':upsTrapOnBatteryPower,'upsTrapBatteryLow':upsTrapBatteryLow,'upsTrapPowerRestored':upsTrapPowerRestored,'upsTrapImminentStop':upsTrapImminentStop,'upsTrapTurnedOff':upsTrapTurnedOff,'upsTrapOverTemperature':upsTrapOverTemperature,'upsTrapOverload':upsTrapOverload,'upsTrapOnMains':upsTrapOnMains,'upsTrapRedoundancyLost':upsTrapRedoundancyLost,'upsTrapEmdTempLow':upsTrapEmdTempLow,'upsTrapEmdTempNotLow':upsTrapEmdTempNotLow,'upsTrapEmdTempHigh':upsTrapEmdTempHigh,'upsTrapEmdTempNotHigh':upsTrapEmdTempNotHigh,'upsTrapEmdHumidityLow':upsTrapEmdHumidityLow,'upsTrapEmdHumidityNotLow':upsTrapEmdHumidityNotLow,'upsTrapEmdHumidityHigh':upsTrapEmdHumidityHigh,'upsTrapEmdHumidityNotHigh':upsTrapEmdHumidityNotHigh,'upsTrapEmdFirstInputActive':upsTrapEmdFirstInputActive,'upsTrapEmdFirstInputRestored':upsTrapEmdFirstInputRestored,'upsTrapEmdSecondInputActive':upsTrapEmdSecondInputActive,'upsTrapEmdSecondInputRestored':upsTrapEmdSecondInputRestored})