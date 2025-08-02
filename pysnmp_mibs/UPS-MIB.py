_AW='upsFullConfigGroup'
_AV='upsFullControlGroup'
_AU='upsFullTestGroup'
_AT='upsFullAlarmGroup'
_AS='upsFullOutputGroup'
_AR='upsFullInputGroup'
_AQ='upsFullBatteryGroup'
_AP='upsFullIdentGroup'
_AO='upsBasicConfigGroup'
_AN='upsBasicControlGroup'
_AM='upsBasicTestGroup'
_AL='upsBasicAlarmGroup'
_AK='upsBasicOutputGroup'
_AJ='upsBasicInputGroup'
_AI='upsBasicBatteryGroup'
_AH='upsBasicIdentGroup'
_AG='upsSubsetConfigGroup'
_AF='upsSubsetControlGroup'
_AE='upsSubsetAlarmGroup'
_AD='upsSubsetOutputGroup'
_AC='upsSubsetInputGroup'
_AB='upsSubsetBatteryGroup'
_AA='upsSubsetIdentGroup'
_A9='upsOutputPercentLoad'
_A8='upsOutputPower'
_A7='upsOutputCurrent'
_A6='upsEstimatedChargeRemaining'
_A5='upsBypassLineIndex'
_A4='upsOutputLineIndex'
_A3='upsInputLineIndex'
_A2='upsEstimatedMinutesRemaining'
_A1='upsConfigAudibleStatus'
_A0='upsRebootWithDuration'
_z='upsStartupAfterDelay'
_y='upsBypassVoltage'
_x='upsBypassNumLines'
_w='upsBypassFrequency'
_v='upsOutputVoltage'
_u='upsOutputNumLines'
_t='upsOutputFrequency'
_s='upsInputVoltage'
_r='upsInputFrequency'
_q='upsInputNumLines'
_p='upsIdentUPSSoftwareVersion'
_o='upsIdentAttachedDevices'
_n='0.1 RMS Amp'
_m='upsConfigLowBattTime'
_l='upsTestElapsedTime'
_k='upsTestStartTime'
_j='upsTestResultsDetail'
_i='upsTestResultsSummary'
_h='upsTestSpinLock'
_g='upsTestId'
_f='upsConfigOutputPower'
_e='upsConfigOutputVA'
_d='upsConfigOutputFreq'
_c='upsConfigOutputVoltage'
_b='upsConfigInputFreq'
_a='upsConfigInputVoltage'
_Z='upsAutoRestart'
_Y='upsShutdownAfterDelay'
_X='upsShutdownType'
_W='upsAlarmTime'
_V='upsAlarmsPresent'
_U='upsOutputSource'
_T='upsInputLineBads'
_S='upsBatteryStatus'
_R='upsIdentName'
_Q='upsIdentAgentSoftwareVersion'
_P='upsIdentModel'
_O='upsIdentManufacturer'
_N='upsAlarmId'
_M='Watts'
_L='not-accessible'
_K='seconds'
_J='upsSecondsOnBattery'
_I='0.1 Hertz'
_H='upsAlarmDescr'
_G='RMS Volts'
_F='DisplayString'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='UPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TestAndIncr,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_F,'PhysAddress','TextualConvention','TestAndIncr','TimeInterval','TimeStamp')
upsMIB=ModuleIdentity((1,3,6,1,2,1,33))
if mibBuilder.loadTexts:upsMIB.setRevisions(('2005-10-14 00:00',))
class PositiveInteger(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NonNegativeInteger(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_UpsObjects_ObjectIdentity=ObjectIdentity
upsObjects=_UpsObjects_ObjectIdentity((1,3,6,1,2,1,33,1))
_UpsIdent_ObjectIdentity=ObjectIdentity
upsIdent=_UpsIdent_ObjectIdentity((1,3,6,1,2,1,33,1,1))
class _UpsIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsIdentManufacturer_Type.__name__=_F
_UpsIdentManufacturer_Object=MibScalar
upsIdentManufacturer=_UpsIdentManufacturer_Object((1,3,6,1,2,1,33,1,1,1),_UpsIdentManufacturer_Type())
upsIdentManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:upsIdentManufacturer.setStatus(_B)
class _UpsIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentModel_Type.__name__=_F
_UpsIdentModel_Object=MibScalar
upsIdentModel=_UpsIdentModel_Object((1,3,6,1,2,1,33,1,1,2),_UpsIdentModel_Type())
upsIdentModel.setMaxAccess(_C)
if mibBuilder.loadTexts:upsIdentModel.setStatus(_B)
class _UpsIdentUPSSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentUPSSoftwareVersion_Type.__name__=_F
_UpsIdentUPSSoftwareVersion_Object=MibScalar
upsIdentUPSSoftwareVersion=_UpsIdentUPSSoftwareVersion_Object((1,3,6,1,2,1,33,1,1,3),_UpsIdentUPSSoftwareVersion_Type())
upsIdentUPSSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:upsIdentUPSSoftwareVersion.setStatus(_B)
class _UpsIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentAgentSoftwareVersion_Type.__name__=_F
_UpsIdentAgentSoftwareVersion_Object=MibScalar
upsIdentAgentSoftwareVersion=_UpsIdentAgentSoftwareVersion_Object((1,3,6,1,2,1,33,1,1,4),_UpsIdentAgentSoftwareVersion_Type())
upsIdentAgentSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:upsIdentAgentSoftwareVersion.setStatus(_B)
class _UpsIdentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentName_Type.__name__=_F
_UpsIdentName_Object=MibScalar
upsIdentName=_UpsIdentName_Object((1,3,6,1,2,1,33,1,1,5),_UpsIdentName_Type())
upsIdentName.setMaxAccess(_D)
if mibBuilder.loadTexts:upsIdentName.setStatus(_B)
class _UpsIdentAttachedDevices_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsIdentAttachedDevices_Type.__name__=_F
_UpsIdentAttachedDevices_Object=MibScalar
upsIdentAttachedDevices=_UpsIdentAttachedDevices_Object((1,3,6,1,2,1,33,1,1,6),_UpsIdentAttachedDevices_Type())
upsIdentAttachedDevices.setMaxAccess(_D)
if mibBuilder.loadTexts:upsIdentAttachedDevices.setStatus(_B)
_UpsBattery_ObjectIdentity=ObjectIdentity
upsBattery=_UpsBattery_ObjectIdentity((1,3,6,1,2,1,33,1,2))
class _UpsBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('batteryNormal',2),('batteryLow',3),('batteryDepleted',4)))
_UpsBatteryStatus_Type.__name__=_E
_UpsBatteryStatus_Object=MibScalar
upsBatteryStatus=_UpsBatteryStatus_Object((1,3,6,1,2,1,33,1,2,1),_UpsBatteryStatus_Type())
upsBatteryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryStatus.setStatus(_B)
_UpsSecondsOnBattery_Type=NonNegativeInteger
_UpsSecondsOnBattery_Object=MibScalar
upsSecondsOnBattery=_UpsSecondsOnBattery_Object((1,3,6,1,2,1,33,1,2,2),_UpsSecondsOnBattery_Type())
upsSecondsOnBattery.setMaxAccess(_C)
if mibBuilder.loadTexts:upsSecondsOnBattery.setStatus(_B)
if mibBuilder.loadTexts:upsSecondsOnBattery.setUnits(_K)
_UpsEstimatedMinutesRemaining_Type=PositiveInteger
_UpsEstimatedMinutesRemaining_Object=MibScalar
upsEstimatedMinutesRemaining=_UpsEstimatedMinutesRemaining_Object((1,3,6,1,2,1,33,1,2,3),_UpsEstimatedMinutesRemaining_Type())
upsEstimatedMinutesRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:upsEstimatedMinutesRemaining.setStatus(_B)
if mibBuilder.loadTexts:upsEstimatedMinutesRemaining.setUnits('minutes')
class _UpsEstimatedChargeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_UpsEstimatedChargeRemaining_Type.__name__=_E
_UpsEstimatedChargeRemaining_Object=MibScalar
upsEstimatedChargeRemaining=_UpsEstimatedChargeRemaining_Object((1,3,6,1,2,1,33,1,2,4),_UpsEstimatedChargeRemaining_Type())
upsEstimatedChargeRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:upsEstimatedChargeRemaining.setStatus(_B)
if mibBuilder.loadTexts:upsEstimatedChargeRemaining.setUnits('percent')
_UpsBatteryVoltage_Type=NonNegativeInteger
_UpsBatteryVoltage_Object=MibScalar
upsBatteryVoltage=_UpsBatteryVoltage_Object((1,3,6,1,2,1,33,1,2,5),_UpsBatteryVoltage_Type())
upsBatteryVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryVoltage.setStatus(_B)
if mibBuilder.loadTexts:upsBatteryVoltage.setUnits('0.1 Volt DC')
_UpsBatteryCurrent_Type=Integer32
_UpsBatteryCurrent_Object=MibScalar
upsBatteryCurrent=_UpsBatteryCurrent_Object((1,3,6,1,2,1,33,1,2,6),_UpsBatteryCurrent_Type())
upsBatteryCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryCurrent.setStatus(_B)
if mibBuilder.loadTexts:upsBatteryCurrent.setUnits('0.1 Amp DC')
_UpsBatteryTemperature_Type=Integer32
_UpsBatteryTemperature_Object=MibScalar
upsBatteryTemperature=_UpsBatteryTemperature_Object((1,3,6,1,2,1,33,1,2,7),_UpsBatteryTemperature_Type())
upsBatteryTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryTemperature.setStatus(_B)
if mibBuilder.loadTexts:upsBatteryTemperature.setUnits('degrees Centigrade')
_UpsInput_ObjectIdentity=ObjectIdentity
upsInput=_UpsInput_ObjectIdentity((1,3,6,1,2,1,33,1,3))
_UpsInputLineBads_Type=Counter32
_UpsInputLineBads_Object=MibScalar
upsInputLineBads=_UpsInputLineBads_Object((1,3,6,1,2,1,33,1,3,1),_UpsInputLineBads_Type())
upsInputLineBads.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputLineBads.setStatus(_B)
_UpsInputNumLines_Type=NonNegativeInteger
_UpsInputNumLines_Object=MibScalar
upsInputNumLines=_UpsInputNumLines_Object((1,3,6,1,2,1,33,1,3,2),_UpsInputNumLines_Type())
upsInputNumLines.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputNumLines.setStatus(_B)
_UpsInputTable_Object=MibTable
upsInputTable=_UpsInputTable_Object((1,3,6,1,2,1,33,1,3,3))
if mibBuilder.loadTexts:upsInputTable.setStatus(_B)
_UpsInputEntry_Object=MibTableRow
upsInputEntry=_UpsInputEntry_Object((1,3,6,1,2,1,33,1,3,3,1))
upsInputEntry.setIndexNames((0,_A,_A3))
if mibBuilder.loadTexts:upsInputEntry.setStatus(_B)
_UpsInputLineIndex_Type=PositiveInteger
_UpsInputLineIndex_Object=MibTableColumn
upsInputLineIndex=_UpsInputLineIndex_Object((1,3,6,1,2,1,33,1,3,3,1,1),_UpsInputLineIndex_Type())
upsInputLineIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:upsInputLineIndex.setStatus(_B)
_UpsInputFrequency_Type=NonNegativeInteger
_UpsInputFrequency_Object=MibTableColumn
upsInputFrequency=_UpsInputFrequency_Object((1,3,6,1,2,1,33,1,3,3,1,2),_UpsInputFrequency_Type())
upsInputFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputFrequency.setStatus(_B)
if mibBuilder.loadTexts:upsInputFrequency.setUnits(_I)
_UpsInputVoltage_Type=NonNegativeInteger
_UpsInputVoltage_Object=MibTableColumn
upsInputVoltage=_UpsInputVoltage_Object((1,3,6,1,2,1,33,1,3,3,1,3),_UpsInputVoltage_Type())
upsInputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputVoltage.setStatus(_B)
if mibBuilder.loadTexts:upsInputVoltage.setUnits(_G)
_UpsInputCurrent_Type=NonNegativeInteger
_UpsInputCurrent_Object=MibTableColumn
upsInputCurrent=_UpsInputCurrent_Object((1,3,6,1,2,1,33,1,3,3,1,4),_UpsInputCurrent_Type())
upsInputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputCurrent.setStatus(_B)
if mibBuilder.loadTexts:upsInputCurrent.setUnits(_n)
_UpsInputTruePower_Type=NonNegativeInteger
_UpsInputTruePower_Object=MibTableColumn
upsInputTruePower=_UpsInputTruePower_Object((1,3,6,1,2,1,33,1,3,3,1,5),_UpsInputTruePower_Type())
upsInputTruePower.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTruePower.setStatus(_B)
if mibBuilder.loadTexts:upsInputTruePower.setUnits(_M)
_UpsOutput_ObjectIdentity=ObjectIdentity
upsOutput=_UpsOutput_ObjectIdentity((1,3,6,1,2,1,33,1,4))
class _UpsOutputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('none',2),('normal',3),('bypass',4),('battery',5),('booster',6),('reducer',7)))
_UpsOutputSource_Type.__name__=_E
_UpsOutputSource_Object=MibScalar
upsOutputSource=_UpsOutputSource_Object((1,3,6,1,2,1,33,1,4,1),_UpsOutputSource_Type())
upsOutputSource.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputSource.setStatus(_B)
_UpsOutputFrequency_Type=NonNegativeInteger
_UpsOutputFrequency_Object=MibScalar
upsOutputFrequency=_UpsOutputFrequency_Object((1,3,6,1,2,1,33,1,4,2),_UpsOutputFrequency_Type())
upsOutputFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputFrequency.setStatus(_B)
if mibBuilder.loadTexts:upsOutputFrequency.setUnits(_I)
_UpsOutputNumLines_Type=NonNegativeInteger
_UpsOutputNumLines_Object=MibScalar
upsOutputNumLines=_UpsOutputNumLines_Object((1,3,6,1,2,1,33,1,4,3),_UpsOutputNumLines_Type())
upsOutputNumLines.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputNumLines.setStatus(_B)
_UpsOutputTable_Object=MibTable
upsOutputTable=_UpsOutputTable_Object((1,3,6,1,2,1,33,1,4,4))
if mibBuilder.loadTexts:upsOutputTable.setStatus(_B)
_UpsOutputEntry_Object=MibTableRow
upsOutputEntry=_UpsOutputEntry_Object((1,3,6,1,2,1,33,1,4,4,1))
upsOutputEntry.setIndexNames((0,_A,_A4))
if mibBuilder.loadTexts:upsOutputEntry.setStatus(_B)
_UpsOutputLineIndex_Type=PositiveInteger
_UpsOutputLineIndex_Object=MibTableColumn
upsOutputLineIndex=_UpsOutputLineIndex_Object((1,3,6,1,2,1,33,1,4,4,1,1),_UpsOutputLineIndex_Type())
upsOutputLineIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:upsOutputLineIndex.setStatus(_B)
_UpsOutputVoltage_Type=NonNegativeInteger
_UpsOutputVoltage_Object=MibTableColumn
upsOutputVoltage=_UpsOutputVoltage_Object((1,3,6,1,2,1,33,1,4,4,1,2),_UpsOutputVoltage_Type())
upsOutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputVoltage.setStatus(_B)
if mibBuilder.loadTexts:upsOutputVoltage.setUnits(_G)
_UpsOutputCurrent_Type=NonNegativeInteger
_UpsOutputCurrent_Object=MibTableColumn
upsOutputCurrent=_UpsOutputCurrent_Object((1,3,6,1,2,1,33,1,4,4,1,3),_UpsOutputCurrent_Type())
upsOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputCurrent.setStatus(_B)
if mibBuilder.loadTexts:upsOutputCurrent.setUnits(_n)
_UpsOutputPower_Type=NonNegativeInteger
_UpsOutputPower_Object=MibTableColumn
upsOutputPower=_UpsOutputPower_Object((1,3,6,1,2,1,33,1,4,4,1,4),_UpsOutputPower_Type())
upsOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputPower.setStatus(_B)
if mibBuilder.loadTexts:upsOutputPower.setUnits(_M)
class _UpsOutputPercentLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_UpsOutputPercentLoad_Type.__name__=_E
_UpsOutputPercentLoad_Object=MibTableColumn
upsOutputPercentLoad=_UpsOutputPercentLoad_Object((1,3,6,1,2,1,33,1,4,4,1,5),_UpsOutputPercentLoad_Type())
upsOutputPercentLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputPercentLoad.setStatus(_B)
if mibBuilder.loadTexts:upsOutputPercentLoad.setUnits('percent')
_UpsBypass_ObjectIdentity=ObjectIdentity
upsBypass=_UpsBypass_ObjectIdentity((1,3,6,1,2,1,33,1,5))
_UpsBypassFrequency_Type=NonNegativeInteger
_UpsBypassFrequency_Object=MibScalar
upsBypassFrequency=_UpsBypassFrequency_Object((1,3,6,1,2,1,33,1,5,1),_UpsBypassFrequency_Type())
upsBypassFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBypassFrequency.setStatus(_B)
if mibBuilder.loadTexts:upsBypassFrequency.setUnits(_I)
_UpsBypassNumLines_Type=NonNegativeInteger
_UpsBypassNumLines_Object=MibScalar
upsBypassNumLines=_UpsBypassNumLines_Object((1,3,6,1,2,1,33,1,5,2),_UpsBypassNumLines_Type())
upsBypassNumLines.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBypassNumLines.setStatus(_B)
_UpsBypassTable_Object=MibTable
upsBypassTable=_UpsBypassTable_Object((1,3,6,1,2,1,33,1,5,3))
if mibBuilder.loadTexts:upsBypassTable.setStatus(_B)
_UpsBypassEntry_Object=MibTableRow
upsBypassEntry=_UpsBypassEntry_Object((1,3,6,1,2,1,33,1,5,3,1))
upsBypassEntry.setIndexNames((0,_A,_A5))
if mibBuilder.loadTexts:upsBypassEntry.setStatus(_B)
_UpsBypassLineIndex_Type=PositiveInteger
_UpsBypassLineIndex_Object=MibTableColumn
upsBypassLineIndex=_UpsBypassLineIndex_Object((1,3,6,1,2,1,33,1,5,3,1,1),_UpsBypassLineIndex_Type())
upsBypassLineIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:upsBypassLineIndex.setStatus(_B)
_UpsBypassVoltage_Type=NonNegativeInteger
_UpsBypassVoltage_Object=MibTableColumn
upsBypassVoltage=_UpsBypassVoltage_Object((1,3,6,1,2,1,33,1,5,3,1,2),_UpsBypassVoltage_Type())
upsBypassVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBypassVoltage.setStatus(_B)
if mibBuilder.loadTexts:upsBypassVoltage.setUnits(_G)
_UpsBypassCurrent_Type=NonNegativeInteger
_UpsBypassCurrent_Object=MibTableColumn
upsBypassCurrent=_UpsBypassCurrent_Object((1,3,6,1,2,1,33,1,5,3,1,3),_UpsBypassCurrent_Type())
upsBypassCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBypassCurrent.setStatus(_B)
if mibBuilder.loadTexts:upsBypassCurrent.setUnits(_n)
_UpsBypassPower_Type=NonNegativeInteger
_UpsBypassPower_Object=MibTableColumn
upsBypassPower=_UpsBypassPower_Object((1,3,6,1,2,1,33,1,5,3,1,4),_UpsBypassPower_Type())
upsBypassPower.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBypassPower.setStatus(_B)
if mibBuilder.loadTexts:upsBypassPower.setUnits(_M)
_UpsAlarm_ObjectIdentity=ObjectIdentity
upsAlarm=_UpsAlarm_ObjectIdentity((1,3,6,1,2,1,33,1,6))
_UpsAlarmsPresent_Type=Gauge32
_UpsAlarmsPresent_Object=MibScalar
upsAlarmsPresent=_UpsAlarmsPresent_Object((1,3,6,1,2,1,33,1,6,1),_UpsAlarmsPresent_Type())
upsAlarmsPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAlarmsPresent.setStatus(_B)
_UpsAlarmTable_Object=MibTable
upsAlarmTable=_UpsAlarmTable_Object((1,3,6,1,2,1,33,1,6,2))
if mibBuilder.loadTexts:upsAlarmTable.setStatus(_B)
_UpsAlarmEntry_Object=MibTableRow
upsAlarmEntry=_UpsAlarmEntry_Object((1,3,6,1,2,1,33,1,6,2,1))
upsAlarmEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:upsAlarmEntry.setStatus(_B)
_UpsAlarmId_Type=PositiveInteger
_UpsAlarmId_Object=MibTableColumn
upsAlarmId=_UpsAlarmId_Object((1,3,6,1,2,1,33,1,6,2,1,1),_UpsAlarmId_Type())
upsAlarmId.setMaxAccess(_L)
if mibBuilder.loadTexts:upsAlarmId.setStatus(_B)
_UpsAlarmDescr_Type=AutonomousType
_UpsAlarmDescr_Object=MibTableColumn
upsAlarmDescr=_UpsAlarmDescr_Object((1,3,6,1,2,1,33,1,6,2,1,2),_UpsAlarmDescr_Type())
upsAlarmDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAlarmDescr.setStatus(_B)
_UpsAlarmTime_Type=TimeStamp
_UpsAlarmTime_Object=MibTableColumn
upsAlarmTime=_UpsAlarmTime_Object((1,3,6,1,2,1,33,1,6,2,1,3),_UpsAlarmTime_Type())
upsAlarmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAlarmTime.setStatus(_B)
_UpsWellKnownAlarms_ObjectIdentity=ObjectIdentity
upsWellKnownAlarms=_UpsWellKnownAlarms_ObjectIdentity((1,3,6,1,2,1,33,1,6,3))
_UpsAlarmBatteryBad_ObjectIdentity=ObjectIdentity
upsAlarmBatteryBad=_UpsAlarmBatteryBad_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,1))
if mibBuilder.loadTexts:upsAlarmBatteryBad.setStatus(_B)
_UpsAlarmOnBattery_ObjectIdentity=ObjectIdentity
upsAlarmOnBattery=_UpsAlarmOnBattery_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,2))
if mibBuilder.loadTexts:upsAlarmOnBattery.setStatus(_B)
_UpsAlarmLowBattery_ObjectIdentity=ObjectIdentity
upsAlarmLowBattery=_UpsAlarmLowBattery_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,3))
if mibBuilder.loadTexts:upsAlarmLowBattery.setStatus(_B)
_UpsAlarmDepletedBattery_ObjectIdentity=ObjectIdentity
upsAlarmDepletedBattery=_UpsAlarmDepletedBattery_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,4))
if mibBuilder.loadTexts:upsAlarmDepletedBattery.setStatus(_B)
_UpsAlarmTempBad_ObjectIdentity=ObjectIdentity
upsAlarmTempBad=_UpsAlarmTempBad_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,5))
if mibBuilder.loadTexts:upsAlarmTempBad.setStatus(_B)
_UpsAlarmInputBad_ObjectIdentity=ObjectIdentity
upsAlarmInputBad=_UpsAlarmInputBad_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,6))
if mibBuilder.loadTexts:upsAlarmInputBad.setStatus(_B)
_UpsAlarmOutputBad_ObjectIdentity=ObjectIdentity
upsAlarmOutputBad=_UpsAlarmOutputBad_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,7))
if mibBuilder.loadTexts:upsAlarmOutputBad.setStatus(_B)
_UpsAlarmOutputOverload_ObjectIdentity=ObjectIdentity
upsAlarmOutputOverload=_UpsAlarmOutputOverload_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,8))
if mibBuilder.loadTexts:upsAlarmOutputOverload.setStatus(_B)
_UpsAlarmOnBypass_ObjectIdentity=ObjectIdentity
upsAlarmOnBypass=_UpsAlarmOnBypass_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,9))
if mibBuilder.loadTexts:upsAlarmOnBypass.setStatus(_B)
_UpsAlarmBypassBad_ObjectIdentity=ObjectIdentity
upsAlarmBypassBad=_UpsAlarmBypassBad_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,10))
if mibBuilder.loadTexts:upsAlarmBypassBad.setStatus(_B)
_UpsAlarmOutputOffAsRequested_ObjectIdentity=ObjectIdentity
upsAlarmOutputOffAsRequested=_UpsAlarmOutputOffAsRequested_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,11))
if mibBuilder.loadTexts:upsAlarmOutputOffAsRequested.setStatus(_B)
_UpsAlarmUpsOffAsRequested_ObjectIdentity=ObjectIdentity
upsAlarmUpsOffAsRequested=_UpsAlarmUpsOffAsRequested_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,12))
if mibBuilder.loadTexts:upsAlarmUpsOffAsRequested.setStatus(_B)
_UpsAlarmChargerFailed_ObjectIdentity=ObjectIdentity
upsAlarmChargerFailed=_UpsAlarmChargerFailed_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,13))
if mibBuilder.loadTexts:upsAlarmChargerFailed.setStatus(_B)
_UpsAlarmUpsOutputOff_ObjectIdentity=ObjectIdentity
upsAlarmUpsOutputOff=_UpsAlarmUpsOutputOff_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,14))
if mibBuilder.loadTexts:upsAlarmUpsOutputOff.setStatus(_B)
_UpsAlarmUpsSystemOff_ObjectIdentity=ObjectIdentity
upsAlarmUpsSystemOff=_UpsAlarmUpsSystemOff_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,15))
if mibBuilder.loadTexts:upsAlarmUpsSystemOff.setStatus(_B)
_UpsAlarmFanFailure_ObjectIdentity=ObjectIdentity
upsAlarmFanFailure=_UpsAlarmFanFailure_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,16))
if mibBuilder.loadTexts:upsAlarmFanFailure.setStatus(_B)
_UpsAlarmFuseFailure_ObjectIdentity=ObjectIdentity
upsAlarmFuseFailure=_UpsAlarmFuseFailure_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,17))
if mibBuilder.loadTexts:upsAlarmFuseFailure.setStatus(_B)
_UpsAlarmGeneralFault_ObjectIdentity=ObjectIdentity
upsAlarmGeneralFault=_UpsAlarmGeneralFault_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,18))
if mibBuilder.loadTexts:upsAlarmGeneralFault.setStatus(_B)
_UpsAlarmDiagnosticTestFailed_ObjectIdentity=ObjectIdentity
upsAlarmDiagnosticTestFailed=_UpsAlarmDiagnosticTestFailed_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,19))
if mibBuilder.loadTexts:upsAlarmDiagnosticTestFailed.setStatus(_B)
_UpsAlarmCommunicationsLost_ObjectIdentity=ObjectIdentity
upsAlarmCommunicationsLost=_UpsAlarmCommunicationsLost_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,20))
if mibBuilder.loadTexts:upsAlarmCommunicationsLost.setStatus(_B)
_UpsAlarmAwaitingPower_ObjectIdentity=ObjectIdentity
upsAlarmAwaitingPower=_UpsAlarmAwaitingPower_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,21))
if mibBuilder.loadTexts:upsAlarmAwaitingPower.setStatus(_B)
_UpsAlarmShutdownPending_ObjectIdentity=ObjectIdentity
upsAlarmShutdownPending=_UpsAlarmShutdownPending_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,22))
if mibBuilder.loadTexts:upsAlarmShutdownPending.setStatus(_B)
_UpsAlarmShutdownImminent_ObjectIdentity=ObjectIdentity
upsAlarmShutdownImminent=_UpsAlarmShutdownImminent_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,23))
if mibBuilder.loadTexts:upsAlarmShutdownImminent.setStatus(_B)
_UpsAlarmTestInProgress_ObjectIdentity=ObjectIdentity
upsAlarmTestInProgress=_UpsAlarmTestInProgress_ObjectIdentity((1,3,6,1,2,1,33,1,6,3,24))
if mibBuilder.loadTexts:upsAlarmTestInProgress.setStatus(_B)
_UpsTest_ObjectIdentity=ObjectIdentity
upsTest=_UpsTest_ObjectIdentity((1,3,6,1,2,1,33,1,7))
_UpsTestId_Type=ObjectIdentifier
_UpsTestId_Object=MibScalar
upsTestId=_UpsTestId_Object((1,3,6,1,2,1,33,1,7,1),_UpsTestId_Type())
upsTestId.setMaxAccess(_D)
if mibBuilder.loadTexts:upsTestId.setStatus(_B)
_UpsTestSpinLock_Type=TestAndIncr
_UpsTestSpinLock_Object=MibScalar
upsTestSpinLock=_UpsTestSpinLock_Object((1,3,6,1,2,1,33,1,7,2),_UpsTestSpinLock_Type())
upsTestSpinLock.setMaxAccess(_D)
if mibBuilder.loadTexts:upsTestSpinLock.setStatus(_B)
class _UpsTestResultsSummary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('donePass',1),('doneWarning',2),('doneError',3),('aborted',4),('inProgress',5),('noTestsInitiated',6)))
_UpsTestResultsSummary_Type.__name__=_E
_UpsTestResultsSummary_Object=MibScalar
upsTestResultsSummary=_UpsTestResultsSummary_Object((1,3,6,1,2,1,33,1,7,3),_UpsTestResultsSummary_Type())
upsTestResultsSummary.setMaxAccess(_C)
if mibBuilder.loadTexts:upsTestResultsSummary.setStatus(_B)
class _UpsTestResultsDetail_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsTestResultsDetail_Type.__name__=_F
_UpsTestResultsDetail_Object=MibScalar
upsTestResultsDetail=_UpsTestResultsDetail_Object((1,3,6,1,2,1,33,1,7,4),_UpsTestResultsDetail_Type())
upsTestResultsDetail.setMaxAccess(_C)
if mibBuilder.loadTexts:upsTestResultsDetail.setStatus(_B)
_UpsTestStartTime_Type=TimeStamp
_UpsTestStartTime_Object=MibScalar
upsTestStartTime=_UpsTestStartTime_Object((1,3,6,1,2,1,33,1,7,5),_UpsTestStartTime_Type())
upsTestStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:upsTestStartTime.setStatus(_B)
_UpsTestElapsedTime_Type=TimeInterval
_UpsTestElapsedTime_Object=MibScalar
upsTestElapsedTime=_UpsTestElapsedTime_Object((1,3,6,1,2,1,33,1,7,6),_UpsTestElapsedTime_Type())
upsTestElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:upsTestElapsedTime.setStatus(_B)
_UpsWellKnownTests_ObjectIdentity=ObjectIdentity
upsWellKnownTests=_UpsWellKnownTests_ObjectIdentity((1,3,6,1,2,1,33,1,7,7))
_UpsTestNoTestsInitiated_ObjectIdentity=ObjectIdentity
upsTestNoTestsInitiated=_UpsTestNoTestsInitiated_ObjectIdentity((1,3,6,1,2,1,33,1,7,7,1))
if mibBuilder.loadTexts:upsTestNoTestsInitiated.setStatus(_B)
_UpsTestAbortTestInProgress_ObjectIdentity=ObjectIdentity
upsTestAbortTestInProgress=_UpsTestAbortTestInProgress_ObjectIdentity((1,3,6,1,2,1,33,1,7,7,2))
if mibBuilder.loadTexts:upsTestAbortTestInProgress.setStatus(_B)
_UpsTestGeneralSystemsTest_ObjectIdentity=ObjectIdentity
upsTestGeneralSystemsTest=_UpsTestGeneralSystemsTest_ObjectIdentity((1,3,6,1,2,1,33,1,7,7,3))
if mibBuilder.loadTexts:upsTestGeneralSystemsTest.setStatus(_B)
_UpsTestQuickBatteryTest_ObjectIdentity=ObjectIdentity
upsTestQuickBatteryTest=_UpsTestQuickBatteryTest_ObjectIdentity((1,3,6,1,2,1,33,1,7,7,4))
if mibBuilder.loadTexts:upsTestQuickBatteryTest.setStatus(_B)
_UpsTestDeepBatteryCalibration_ObjectIdentity=ObjectIdentity
upsTestDeepBatteryCalibration=_UpsTestDeepBatteryCalibration_ObjectIdentity((1,3,6,1,2,1,33,1,7,7,5))
if mibBuilder.loadTexts:upsTestDeepBatteryCalibration.setStatus(_B)
_UpsControl_ObjectIdentity=ObjectIdentity
upsControl=_UpsControl_ObjectIdentity((1,3,6,1,2,1,33,1,8))
class _UpsShutdownType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('output',1),('system',2)))
_UpsShutdownType_Type.__name__=_E
_UpsShutdownType_Object=MibScalar
upsShutdownType=_UpsShutdownType_Object((1,3,6,1,2,1,33,1,8,1),_UpsShutdownType_Type())
upsShutdownType.setMaxAccess(_D)
if mibBuilder.loadTexts:upsShutdownType.setStatus(_B)
class _UpsShutdownAfterDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_UpsShutdownAfterDelay_Type.__name__=_E
_UpsShutdownAfterDelay_Object=MibScalar
upsShutdownAfterDelay=_UpsShutdownAfterDelay_Object((1,3,6,1,2,1,33,1,8,2),_UpsShutdownAfterDelay_Type())
upsShutdownAfterDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsShutdownAfterDelay.setStatus(_B)
if mibBuilder.loadTexts:upsShutdownAfterDelay.setUnits(_K)
class _UpsStartupAfterDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_UpsStartupAfterDelay_Type.__name__=_E
_UpsStartupAfterDelay_Object=MibScalar
upsStartupAfterDelay=_UpsStartupAfterDelay_Object((1,3,6,1,2,1,33,1,8,3),_UpsStartupAfterDelay_Type())
upsStartupAfterDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsStartupAfterDelay.setStatus(_B)
if mibBuilder.loadTexts:upsStartupAfterDelay.setUnits(_K)
class _UpsRebootWithDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_UpsRebootWithDuration_Type.__name__=_E
_UpsRebootWithDuration_Object=MibScalar
upsRebootWithDuration=_UpsRebootWithDuration_Object((1,3,6,1,2,1,33,1,8,4),_UpsRebootWithDuration_Type())
upsRebootWithDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:upsRebootWithDuration.setStatus(_B)
if mibBuilder.loadTexts:upsRebootWithDuration.setUnits(_K)
class _UpsAutoRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_UpsAutoRestart_Type.__name__=_E
_UpsAutoRestart_Object=MibScalar
upsAutoRestart=_UpsAutoRestart_Object((1,3,6,1,2,1,33,1,8,5),_UpsAutoRestart_Type())
upsAutoRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAutoRestart.setStatus(_B)
_UpsConfig_ObjectIdentity=ObjectIdentity
upsConfig=_UpsConfig_ObjectIdentity((1,3,6,1,2,1,33,1,9))
_UpsConfigInputVoltage_Type=NonNegativeInteger
_UpsConfigInputVoltage_Object=MibScalar
upsConfigInputVoltage=_UpsConfigInputVoltage_Object((1,3,6,1,2,1,33,1,9,1),_UpsConfigInputVoltage_Type())
upsConfigInputVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigInputVoltage.setStatus(_B)
if mibBuilder.loadTexts:upsConfigInputVoltage.setUnits(_G)
_UpsConfigInputFreq_Type=NonNegativeInteger
_UpsConfigInputFreq_Object=MibScalar
upsConfigInputFreq=_UpsConfigInputFreq_Object((1,3,6,1,2,1,33,1,9,2),_UpsConfigInputFreq_Type())
upsConfigInputFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigInputFreq.setStatus(_B)
if mibBuilder.loadTexts:upsConfigInputFreq.setUnits(_I)
_UpsConfigOutputVoltage_Type=NonNegativeInteger
_UpsConfigOutputVoltage_Object=MibScalar
upsConfigOutputVoltage=_UpsConfigOutputVoltage_Object((1,3,6,1,2,1,33,1,9,3),_UpsConfigOutputVoltage_Type())
upsConfigOutputVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigOutputVoltage.setStatus(_B)
if mibBuilder.loadTexts:upsConfigOutputVoltage.setUnits(_G)
_UpsConfigOutputFreq_Type=NonNegativeInteger
_UpsConfigOutputFreq_Object=MibScalar
upsConfigOutputFreq=_UpsConfigOutputFreq_Object((1,3,6,1,2,1,33,1,9,4),_UpsConfigOutputFreq_Type())
upsConfigOutputFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigOutputFreq.setStatus(_B)
if mibBuilder.loadTexts:upsConfigOutputFreq.setUnits(_I)
_UpsConfigOutputVA_Type=NonNegativeInteger
_UpsConfigOutputVA_Object=MibScalar
upsConfigOutputVA=_UpsConfigOutputVA_Object((1,3,6,1,2,1,33,1,9,5),_UpsConfigOutputVA_Type())
upsConfigOutputVA.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigOutputVA.setStatus(_B)
if mibBuilder.loadTexts:upsConfigOutputVA.setUnits('Volt-Amps')
_UpsConfigOutputPower_Type=NonNegativeInteger
_UpsConfigOutputPower_Object=MibScalar
upsConfigOutputPower=_UpsConfigOutputPower_Object((1,3,6,1,2,1,33,1,9,6),_UpsConfigOutputPower_Type())
upsConfigOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigOutputPower.setStatus(_B)
if mibBuilder.loadTexts:upsConfigOutputPower.setUnits(_M)
_UpsConfigLowBattTime_Type=NonNegativeInteger
_UpsConfigLowBattTime_Object=MibScalar
upsConfigLowBattTime=_UpsConfigLowBattTime_Object((1,3,6,1,2,1,33,1,9,7),_UpsConfigLowBattTime_Type())
upsConfigLowBattTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigLowBattTime.setStatus(_B)
if mibBuilder.loadTexts:upsConfigLowBattTime.setUnits('minutes')
class _UpsConfigAudibleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('enabled',2),('muted',3)))
_UpsConfigAudibleStatus_Type.__name__=_E
_UpsConfigAudibleStatus_Object=MibScalar
upsConfigAudibleStatus=_UpsConfigAudibleStatus_Object((1,3,6,1,2,1,33,1,9,8),_UpsConfigAudibleStatus_Type())
upsConfigAudibleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigAudibleStatus.setStatus(_B)
_UpsConfigLowVoltageTransferPoint_Type=NonNegativeInteger
_UpsConfigLowVoltageTransferPoint_Object=MibScalar
upsConfigLowVoltageTransferPoint=_UpsConfigLowVoltageTransferPoint_Object((1,3,6,1,2,1,33,1,9,9),_UpsConfigLowVoltageTransferPoint_Type())
upsConfigLowVoltageTransferPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigLowVoltageTransferPoint.setStatus(_B)
if mibBuilder.loadTexts:upsConfigLowVoltageTransferPoint.setUnits(_G)
_UpsConfigHighVoltageTransferPoint_Type=NonNegativeInteger
_UpsConfigHighVoltageTransferPoint_Object=MibScalar
upsConfigHighVoltageTransferPoint=_UpsConfigHighVoltageTransferPoint_Object((1,3,6,1,2,1,33,1,9,10),_UpsConfigHighVoltageTransferPoint_Type())
upsConfigHighVoltageTransferPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigHighVoltageTransferPoint.setStatus(_B)
if mibBuilder.loadTexts:upsConfigHighVoltageTransferPoint.setUnits(_G)
_UpsTraps_ObjectIdentity=ObjectIdentity
upsTraps=_UpsTraps_ObjectIdentity((1,3,6,1,2,1,33,2))
_UpsConformance_ObjectIdentity=ObjectIdentity
upsConformance=_UpsConformance_ObjectIdentity((1,3,6,1,2,1,33,3))
_UpsCompliances_ObjectIdentity=ObjectIdentity
upsCompliances=_UpsCompliances_ObjectIdentity((1,3,6,1,2,1,33,3,1))
_UpsGroups_ObjectIdentity=ObjectIdentity
upsGroups=_UpsGroups_ObjectIdentity((1,3,6,1,2,1,33,3,2))
_UpsSubsetGroups_ObjectIdentity=ObjectIdentity
upsSubsetGroups=_UpsSubsetGroups_ObjectIdentity((1,3,6,1,2,1,33,3,2,1))
_UpsBasicGroups_ObjectIdentity=ObjectIdentity
upsBasicGroups=_UpsBasicGroups_ObjectIdentity((1,3,6,1,2,1,33,3,2,2))
_UpsFullGroups_ObjectIdentity=ObjectIdentity
upsFullGroups=_UpsFullGroups_ObjectIdentity((1,3,6,1,2,1,33,3,2,3))
upsSubsetIdentGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,1,1))
upsSubsetIdentGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_o)))
if mibBuilder.loadTexts:upsSubsetIdentGroup.setStatus(_B)
upsSubsetBatteryGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,1,2))
upsSubsetBatteryGroup.setObjects(*((_A,_S),(_A,_J)))
if mibBuilder.loadTexts:upsSubsetBatteryGroup.setStatus(_B)
upsSubsetInputGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,1,3))
upsSubsetInputGroup.setObjects((_A,_T))
if mibBuilder.loadTexts:upsSubsetInputGroup.setStatus(_B)
upsSubsetOutputGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,1,4))
upsSubsetOutputGroup.setObjects((_A,_U))
if mibBuilder.loadTexts:upsSubsetOutputGroup.setStatus(_B)
upsSubsetAlarmGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,1,6))
upsSubsetAlarmGroup.setObjects(*((_A,_V),(_A,_H),(_A,_W)))
if mibBuilder.loadTexts:upsSubsetAlarmGroup.setStatus(_B)
upsSubsetControlGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,1,8))
upsSubsetControlGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:upsSubsetControlGroup.setStatus(_B)
upsSubsetConfigGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,1,9))
upsSubsetConfigGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:upsSubsetConfigGroup.setStatus(_B)
upsBasicIdentGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,2,1))
upsBasicIdentGroup.setObjects(*((_A,_O),(_A,_P),(_A,_p),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:upsBasicIdentGroup.setStatus(_B)
upsBasicBatteryGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,2,2))
upsBasicBatteryGroup.setObjects(*((_A,_S),(_A,_J)))
if mibBuilder.loadTexts:upsBasicBatteryGroup.setStatus(_B)
upsBasicInputGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,2,3))
upsBasicInputGroup.setObjects(*((_A,_T),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:upsBasicInputGroup.setStatus(_B)
upsBasicOutputGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,2,4))
upsBasicOutputGroup.setObjects(*((_A,_U),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:upsBasicOutputGroup.setStatus(_B)
upsBasicBypassGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,2,5))
upsBasicBypassGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:upsBasicBypassGroup.setStatus(_B)
upsBasicAlarmGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,2,6))
upsBasicAlarmGroup.setObjects(*((_A,_V),(_A,_H),(_A,_W)))
if mibBuilder.loadTexts:upsBasicAlarmGroup.setStatus(_B)
upsBasicTestGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,2,7))
upsBasicTestGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:upsBasicTestGroup.setStatus(_B)
upsBasicControlGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,2,8))
upsBasicControlGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_z),(_A,_A0),(_A,_Z)))
if mibBuilder.loadTexts:upsBasicControlGroup.setStatus(_B)
upsBasicConfigGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,2,9))
upsBasicConfigGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_m),(_A,_A1)))
if mibBuilder.loadTexts:upsBasicConfigGroup.setStatus(_B)
upsFullIdentGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,3,1))
upsFullIdentGroup.setObjects(*((_A,_O),(_A,_P),(_A,_p),(_A,_Q),(_A,_R),(_A,_o)))
if mibBuilder.loadTexts:upsFullIdentGroup.setStatus(_B)
upsFullBatteryGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,3,2))
upsFullBatteryGroup.setObjects(*((_A,_S),(_A,_J),(_A,_A2),(_A,_A6)))
if mibBuilder.loadTexts:upsFullBatteryGroup.setStatus(_B)
upsFullInputGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,3,3))
upsFullInputGroup.setObjects(*((_A,_T),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:upsFullInputGroup.setStatus(_B)
upsFullOutputGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,3,4))
upsFullOutputGroup.setObjects(*((_A,_U),(_A,_t),(_A,_u),(_A,_v),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:upsFullOutputGroup.setStatus(_B)
upsFullBypassGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,3,5))
upsFullBypassGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:upsFullBypassGroup.setStatus(_B)
upsFullAlarmGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,3,6))
upsFullAlarmGroup.setObjects(*((_A,_V),(_A,_H),(_A,_W)))
if mibBuilder.loadTexts:upsFullAlarmGroup.setStatus(_B)
upsFullTestGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,3,7))
upsFullTestGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:upsFullTestGroup.setStatus(_B)
upsFullControlGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,3,8))
upsFullControlGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_z),(_A,_A0),(_A,_Z)))
if mibBuilder.loadTexts:upsFullControlGroup.setStatus(_B)
upsFullConfigGroup=ObjectGroup((1,3,6,1,2,1,33,3,2,3,9))
upsFullConfigGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_m),(_A,_A1)))
if mibBuilder.loadTexts:upsFullConfigGroup.setStatus(_B)
upsTrapOnBattery=NotificationType((1,3,6,1,2,1,33,2,1))
upsTrapOnBattery.setObjects(*((_A,_A2),(_A,_J),(_A,_m)))
if mibBuilder.loadTexts:upsTrapOnBattery.setStatus(_B)
upsTrapTestCompleted=NotificationType((1,3,6,1,2,1,33,2,2))
upsTrapTestCompleted.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:upsTrapTestCompleted.setStatus(_B)
upsTrapAlarmEntryAdded=NotificationType((1,3,6,1,2,1,33,2,3))
upsTrapAlarmEntryAdded.setObjects(*((_A,_N),(_A,_H)))
if mibBuilder.loadTexts:upsTrapAlarmEntryAdded.setStatus(_B)
upsTrapAlarmEntryRemoved=NotificationType((1,3,6,1,2,1,33,2,4))
upsTrapAlarmEntryRemoved.setObjects(*((_A,_N),(_A,_H)))
if mibBuilder.loadTexts:upsTrapAlarmEntryRemoved.setStatus(_B)
upsSubsetCompliance=ModuleCompliance((1,3,6,1,2,1,33,3,1,1))
upsSubsetCompliance.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:upsSubsetCompliance.setStatus(_B)
upsBasicCompliance=ModuleCompliance((1,3,6,1,2,1,33,3,1,2))
upsBasicCompliance.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:upsBasicCompliance.setStatus(_B)
upsFullCompliance=ModuleCompliance((1,3,6,1,2,1,33,3,1,3))
upsFullCompliance.setObjects(*((_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:upsFullCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PositiveInteger':PositiveInteger,'NonNegativeInteger':NonNegativeInteger,'upsMIB':upsMIB,'upsObjects':upsObjects,'upsIdent':upsIdent,_O:upsIdentManufacturer,_P:upsIdentModel,_p:upsIdentUPSSoftwareVersion,_Q:upsIdentAgentSoftwareVersion,_R:upsIdentName,_o:upsIdentAttachedDevices,'upsBattery':upsBattery,_S:upsBatteryStatus,_J:upsSecondsOnBattery,_A2:upsEstimatedMinutesRemaining,_A6:upsEstimatedChargeRemaining,'upsBatteryVoltage':upsBatteryVoltage,'upsBatteryCurrent':upsBatteryCurrent,'upsBatteryTemperature':upsBatteryTemperature,'upsInput':upsInput,_T:upsInputLineBads,_q:upsInputNumLines,'upsInputTable':upsInputTable,'upsInputEntry':upsInputEntry,_A3:upsInputLineIndex,_r:upsInputFrequency,_s:upsInputVoltage,'upsInputCurrent':upsInputCurrent,'upsInputTruePower':upsInputTruePower,'upsOutput':upsOutput,_U:upsOutputSource,_t:upsOutputFrequency,_u:upsOutputNumLines,'upsOutputTable':upsOutputTable,'upsOutputEntry':upsOutputEntry,_A4:upsOutputLineIndex,_v:upsOutputVoltage,_A7:upsOutputCurrent,_A8:upsOutputPower,_A9:upsOutputPercentLoad,'upsBypass':upsBypass,_w:upsBypassFrequency,_x:upsBypassNumLines,'upsBypassTable':upsBypassTable,'upsBypassEntry':upsBypassEntry,_A5:upsBypassLineIndex,_y:upsBypassVoltage,'upsBypassCurrent':upsBypassCurrent,'upsBypassPower':upsBypassPower,'upsAlarm':upsAlarm,_V:upsAlarmsPresent,'upsAlarmTable':upsAlarmTable,'upsAlarmEntry':upsAlarmEntry,_N:upsAlarmId,_H:upsAlarmDescr,_W:upsAlarmTime,'upsWellKnownAlarms':upsWellKnownAlarms,'upsAlarmBatteryBad':upsAlarmBatteryBad,'upsAlarmOnBattery':upsAlarmOnBattery,'upsAlarmLowBattery':upsAlarmLowBattery,'upsAlarmDepletedBattery':upsAlarmDepletedBattery,'upsAlarmTempBad':upsAlarmTempBad,'upsAlarmInputBad':upsAlarmInputBad,'upsAlarmOutputBad':upsAlarmOutputBad,'upsAlarmOutputOverload':upsAlarmOutputOverload,'upsAlarmOnBypass':upsAlarmOnBypass,'upsAlarmBypassBad':upsAlarmBypassBad,'upsAlarmOutputOffAsRequested':upsAlarmOutputOffAsRequested,'upsAlarmUpsOffAsRequested':upsAlarmUpsOffAsRequested,'upsAlarmChargerFailed':upsAlarmChargerFailed,'upsAlarmUpsOutputOff':upsAlarmUpsOutputOff,'upsAlarmUpsSystemOff':upsAlarmUpsSystemOff,'upsAlarmFanFailure':upsAlarmFanFailure,'upsAlarmFuseFailure':upsAlarmFuseFailure,'upsAlarmGeneralFault':upsAlarmGeneralFault,'upsAlarmDiagnosticTestFailed':upsAlarmDiagnosticTestFailed,'upsAlarmCommunicationsLost':upsAlarmCommunicationsLost,'upsAlarmAwaitingPower':upsAlarmAwaitingPower,'upsAlarmShutdownPending':upsAlarmShutdownPending,'upsAlarmShutdownImminent':upsAlarmShutdownImminent,'upsAlarmTestInProgress':upsAlarmTestInProgress,'upsTest':upsTest,_g:upsTestId,_h:upsTestSpinLock,_i:upsTestResultsSummary,_j:upsTestResultsDetail,_k:upsTestStartTime,_l:upsTestElapsedTime,'upsWellKnownTests':upsWellKnownTests,'upsTestNoTestsInitiated':upsTestNoTestsInitiated,'upsTestAbortTestInProgress':upsTestAbortTestInProgress,'upsTestGeneralSystemsTest':upsTestGeneralSystemsTest,'upsTestQuickBatteryTest':upsTestQuickBatteryTest,'upsTestDeepBatteryCalibration':upsTestDeepBatteryCalibration,'upsControl':upsControl,_X:upsShutdownType,_Y:upsShutdownAfterDelay,_z:upsStartupAfterDelay,_A0:upsRebootWithDuration,_Z:upsAutoRestart,'upsConfig':upsConfig,_a:upsConfigInputVoltage,_b:upsConfigInputFreq,_c:upsConfigOutputVoltage,_d:upsConfigOutputFreq,_e:upsConfigOutputVA,_f:upsConfigOutputPower,_m:upsConfigLowBattTime,_A1:upsConfigAudibleStatus,'upsConfigLowVoltageTransferPoint':upsConfigLowVoltageTransferPoint,'upsConfigHighVoltageTransferPoint':upsConfigHighVoltageTransferPoint,'upsTraps':upsTraps,'upsTrapOnBattery':upsTrapOnBattery,'upsTrapTestCompleted':upsTrapTestCompleted,'upsTrapAlarmEntryAdded':upsTrapAlarmEntryAdded,'upsTrapAlarmEntryRemoved':upsTrapAlarmEntryRemoved,'upsConformance':upsConformance,'upsCompliances':upsCompliances,'upsSubsetCompliance':upsSubsetCompliance,'upsBasicCompliance':upsBasicCompliance,'upsFullCompliance':upsFullCompliance,'upsGroups':upsGroups,'upsSubsetGroups':upsSubsetGroups,_AA:upsSubsetIdentGroup,_AB:upsSubsetBatteryGroup,_AC:upsSubsetInputGroup,_AD:upsSubsetOutputGroup,_AE:upsSubsetAlarmGroup,_AF:upsSubsetControlGroup,_AG:upsSubsetConfigGroup,'upsBasicGroups':upsBasicGroups,_AH:upsBasicIdentGroup,_AI:upsBasicBatteryGroup,_AJ:upsBasicInputGroup,_AK:upsBasicOutputGroup,'upsBasicBypassGroup':upsBasicBypassGroup,_AL:upsBasicAlarmGroup,_AM:upsBasicTestGroup,_AN:upsBasicControlGroup,_AO:upsBasicConfigGroup,'upsFullGroups':upsFullGroups,_AP:upsFullIdentGroup,_AQ:upsFullBatteryGroup,_AR:upsFullInputGroup,_AS:upsFullOutputGroup,'upsFullBypassGroup':upsFullBypassGroup,_AT:upsFullAlarmGroup,_AU:upsFullTestGroup,_AV:upsFullControlGroup,_AW:upsFullConfigGroup})