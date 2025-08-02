_x='threePhase4WireL1L2L3WithNeutral'
_w='threePhase3WireL1L2L3'
_v='twoPhase3WireL1L2WithNeutral'
_u='twoPhase2WireL1L2'
_t='singlePhase2WireL1WithReturn'
_s='lgpPwrLoadCircuitIndex'
_r='lgpPwrThresholdIndex'
_q='battery'
_p='utility'
_o='lgpPwrDcMeasurementPointIndex'
_n='lgpPwrLineMeasurementIndex'
_m='lgpPwrMeasurementPtIndex'
_l='lagging'
_k='leading'
_j='0.1 Amp'
_i='Watt-Hour'
_h='.01 Power Factor'
_g='lgpPwrMeasurementPointIndex'
_f='0.1 Degrees'
_e='0.1 Percent'
_d='Amp-hour'
_c='installed'
_b='bypass'
_a='Watt'
_Z='marginalHigh'
_Y='marginalLow'
_X='fail'
_W='none'
_V='Amp'
_U='Volt-Amp'
_T='not-accessible'
_S='percent'
_R='unknown'
_Q='minutes'
_P='normal'
_O='LIEBERT-GP-POWER-MIB'
_N='Volt'
_M='seconds'
_L='off'
_K='on'
_J='open'
_I='closed'
_H='Count'
_G='yes'
_F='no'
_E='notInstalled'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lgpPower,liebertPowerModuleReg=mibBuilder.importSymbols('LIEBERT-GP-REGISTRATION-MIB','lgpPower','liebertPowerModuleReg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
liebertGlobalProductsPowerModule=ModuleIdentity((1,3,6,1,4,1,476,1,42,1,6,1))
if mibBuilder.loadTexts:liebertGlobalProductsPowerModule.setRevisions(('2013-07-10 00:00','2008-11-17 00:00','2008-07-02 00:00','2008-01-10 00:00','2006-02-22 00:00'))
_LgpPwrBattery_ObjectIdentity=ObjectIdentity
lgpPwrBattery=_LgpPwrBattery_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,1))
if mibBuilder.loadTexts:lgpPwrBattery.setStatus(_A)
_LgpPwrNumberInstalledBatteryModules_Type=Integer32
_LgpPwrNumberInstalledBatteryModules_Object=MibScalar
lgpPwrNumberInstalledBatteryModules=_LgpPwrNumberInstalledBatteryModules_Object((1,3,6,1,4,1,476,1,42,3,5,1,1),_LgpPwrNumberInstalledBatteryModules_Type())
lgpPwrNumberInstalledBatteryModules.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberInstalledBatteryModules.setStatus(_A)
_LgpPwrNumberFailedBatteryModules_Type=Integer32
_LgpPwrNumberFailedBatteryModules_Object=MibScalar
lgpPwrNumberFailedBatteryModules=_LgpPwrNumberFailedBatteryModules_Object((1,3,6,1,4,1,476,1,42,3,5,1,2),_LgpPwrNumberFailedBatteryModules_Type())
lgpPwrNumberFailedBatteryModules.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberFailedBatteryModules.setStatus(_A)
_LgpPwrNumberRedundantBatteryModules_Type=Integer32
_LgpPwrNumberRedundantBatteryModules_Object=MibScalar
lgpPwrNumberRedundantBatteryModules=_LgpPwrNumberRedundantBatteryModules_Object((1,3,6,1,4,1,476,1,42,3,5,1,3),_LgpPwrNumberRedundantBatteryModules_Type())
lgpPwrNumberRedundantBatteryModules.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberRedundantBatteryModules.setStatus(_A)
_LgpPwrNumberActiveBatteryModules_Type=Integer32
_LgpPwrNumberActiveBatteryModules_Object=MibScalar
lgpPwrNumberActiveBatteryModules=_LgpPwrNumberActiveBatteryModules_Object((1,3,6,1,4,1,476,1,42,3,5,1,4),_LgpPwrNumberActiveBatteryModules_Type())
lgpPwrNumberActiveBatteryModules.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberActiveBatteryModules.setStatus(_A)
_LgpPwrConfigLowBatteryWarningTime_Type=Integer32
_LgpPwrConfigLowBatteryWarningTime_Object=MibScalar
lgpPwrConfigLowBatteryWarningTime=_LgpPwrConfigLowBatteryWarningTime_Object((1,3,6,1,4,1,476,1,42,3,5,1,5),_LgpPwrConfigLowBatteryWarningTime_Type())
lgpPwrConfigLowBatteryWarningTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrConfigLowBatteryWarningTime.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrConfigLowBatteryWarningTime.setUnits(_Q)
_LgpPwrNumberBatteryModuleWarnings_Type=Integer32
_LgpPwrNumberBatteryModuleWarnings_Object=MibScalar
lgpPwrNumberBatteryModuleWarnings=_LgpPwrNumberBatteryModuleWarnings_Object((1,3,6,1,4,1,476,1,42,3,5,1,6),_LgpPwrNumberBatteryModuleWarnings_Type())
lgpPwrNumberBatteryModuleWarnings.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberBatteryModuleWarnings.setStatus(_A)
_LgpPwrBatteryCount_Type=Integer32
_LgpPwrBatteryCount_Object=MibScalar
lgpPwrBatteryCount=_LgpPwrBatteryCount_Object((1,3,6,1,4,1,476,1,42,3,5,1,7),_LgpPwrBatteryCount_Type())
lgpPwrBatteryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryCount.setUnits(_H)
class _LgpPwrBatteryTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('passed',2),('failed',3),('inProgress',4),('systemFailure',5),('inhibited',6)))
_LgpPwrBatteryTestResult_Type.__name__=_C
_LgpPwrBatteryTestResult_Object=MibScalar
lgpPwrBatteryTestResult=_LgpPwrBatteryTestResult_Object((1,3,6,1,4,1,476,1,42,3,5,1,8),_LgpPwrBatteryTestResult_Type())
lgpPwrBatteryTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryTestResult.setStatus(_A)
_LgpPwrNominalBatteryCapacity_Type=Integer32
_LgpPwrNominalBatteryCapacity_Object=MibScalar
lgpPwrNominalBatteryCapacity=_LgpPwrNominalBatteryCapacity_Object((1,3,6,1,4,1,476,1,42,3,5,1,9),_LgpPwrNominalBatteryCapacity_Type())
lgpPwrNominalBatteryCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrNominalBatteryCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNominalBatteryCapacity.setUnits(_Q)
_LgpPwrBatteryFloatVoltage_Type=Integer32
_LgpPwrBatteryFloatVoltage_Object=MibScalar
lgpPwrBatteryFloatVoltage=_LgpPwrBatteryFloatVoltage_Object((1,3,6,1,4,1,476,1,42,3,5,1,10),_LgpPwrBatteryFloatVoltage_Type())
lgpPwrBatteryFloatVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryFloatVoltage.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryFloatVoltage.setUnits(_N)
_LgpPwrBatteryEndOfDischargeVoltage_Type=Integer32
_LgpPwrBatteryEndOfDischargeVoltage_Object=MibScalar
lgpPwrBatteryEndOfDischargeVoltage=_LgpPwrBatteryEndOfDischargeVoltage_Object((1,3,6,1,4,1,476,1,42,3,5,1,11),_LgpPwrBatteryEndOfDischargeVoltage_Type())
lgpPwrBatteryEndOfDischargeVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryEndOfDischargeVoltage.setStatus(_A)
_LgpPwrAutomaticBatteryTestInterval_Type=Integer32
_LgpPwrAutomaticBatteryTestInterval_Object=MibScalar
lgpPwrAutomaticBatteryTestInterval=_LgpPwrAutomaticBatteryTestInterval_Object((1,3,6,1,4,1,476,1,42,3,5,1,12),_LgpPwrAutomaticBatteryTestInterval_Type())
lgpPwrAutomaticBatteryTestInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrAutomaticBatteryTestInterval.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrAutomaticBatteryTestInterval.setUnits('hours')
_LgpPwrAutomaticBatteryTestCountdown_Type=Integer32
_LgpPwrAutomaticBatteryTestCountdown_Object=MibScalar
lgpPwrAutomaticBatteryTestCountdown=_LgpPwrAutomaticBatteryTestCountdown_Object((1,3,6,1,4,1,476,1,42,3,5,1,13),_LgpPwrAutomaticBatteryTestCountdown_Type())
lgpPwrAutomaticBatteryTestCountdown.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrAutomaticBatteryTestCountdown.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrAutomaticBatteryTestCountdown.setUnits(_Q)
class _LgpPwrBatteryChargeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fullycharged',1),('notfullycharged',2),('charging',3),('discharging',4)))
_LgpPwrBatteryChargeStatus_Type.__name__=_C
_LgpPwrBatteryChargeStatus_Object=MibScalar
lgpPwrBatteryChargeStatus=_LgpPwrBatteryChargeStatus_Object((1,3,6,1,4,1,476,1,42,3,5,1,14),_LgpPwrBatteryChargeStatus_Type())
lgpPwrBatteryChargeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryChargeStatus.setStatus(_A)
class _LgpPwrBatteryLifeEnhancer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrBatteryLifeEnhancer_Type.__name__=_C
_LgpPwrBatteryLifeEnhancer_Object=MibScalar
lgpPwrBatteryLifeEnhancer=_LgpPwrBatteryLifeEnhancer_Object((1,3,6,1,4,1,476,1,42,3,5,1,15),_LgpPwrBatteryLifeEnhancer_Type())
lgpPwrBatteryLifeEnhancer.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryLifeEnhancer.setStatus(_A)
class _LgpPwrBatteryCharger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrBatteryCharger_Type.__name__=_C
_LgpPwrBatteryCharger_Object=MibScalar
lgpPwrBatteryCharger=_LgpPwrBatteryCharger_Object((1,3,6,1,4,1,476,1,42,3,5,1,16),_LgpPwrBatteryCharger_Type())
lgpPwrBatteryCharger.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryCharger.setStatus(_A)
class _LgpPwrBatteryChargeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('float',1),('equalize',2)))
_LgpPwrBatteryChargeMode_Type.__name__=_C
_LgpPwrBatteryChargeMode_Object=MibScalar
lgpPwrBatteryChargeMode=_LgpPwrBatteryChargeMode_Object((1,3,6,1,4,1,476,1,42,3,5,1,17),_LgpPwrBatteryChargeMode_Type())
lgpPwrBatteryChargeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryChargeMode.setStatus(_A)
_LgpPwrBatteryTimeRemaining_Type=Integer32
_LgpPwrBatteryTimeRemaining_Object=MibScalar
lgpPwrBatteryTimeRemaining=_LgpPwrBatteryTimeRemaining_Object((1,3,6,1,4,1,476,1,42,3,5,1,18),_LgpPwrBatteryTimeRemaining_Type())
lgpPwrBatteryTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryTimeRemaining.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryTimeRemaining.setUnits(_Q)
_LgpPwrBatteryCapacity_Type=Integer32
_LgpPwrBatteryCapacity_Object=MibScalar
lgpPwrBatteryCapacity=_LgpPwrBatteryCapacity_Object((1,3,6,1,4,1,476,1,42,3,5,1,19),_LgpPwrBatteryCapacity_Type())
lgpPwrBatteryCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryCapacity.setUnits(_S)
_LgpPwrBatteryCabinet_ObjectIdentity=ObjectIdentity
lgpPwrBatteryCabinet=_LgpPwrBatteryCabinet_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,1,20))
if mibBuilder.loadTexts:lgpPwrBatteryCabinet.setStatus(_A)
_LgpPwrBatteryCabinetCount_Type=Integer32
_LgpPwrBatteryCabinetCount_Object=MibScalar
lgpPwrBatteryCabinetCount=_LgpPwrBatteryCabinetCount_Object((1,3,6,1,4,1,476,1,42,3,5,1,20,1),_LgpPwrBatteryCabinetCount_Type())
lgpPwrBatteryCabinetCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryCabinetCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryCabinetCount.setUnits(_H)
class _LgpPwrBatteryCabinetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notSpecified',1),('internal',2),('external',3),('lrt',4)))
_LgpPwrBatteryCabinetType_Type.__name__=_C
_LgpPwrBatteryCabinetType_Object=MibScalar
lgpPwrBatteryCabinetType=_LgpPwrBatteryCabinetType_Object((1,3,6,1,4,1,476,1,42,3,5,1,20,2),_LgpPwrBatteryCabinetType_Type())
lgpPwrBatteryCabinetType.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryCabinetType.setStatus(_A)
_LgpPwrBatteryCabinetRatedCapacity_Type=Integer32
_LgpPwrBatteryCabinetRatedCapacity_Object=MibScalar
lgpPwrBatteryCabinetRatedCapacity=_LgpPwrBatteryCabinetRatedCapacity_Object((1,3,6,1,4,1,476,1,42,3,5,1,20,3),_LgpPwrBatteryCabinetRatedCapacity_Type())
lgpPwrBatteryCabinetRatedCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryCabinetRatedCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryCabinetRatedCapacity.setUnits('0.1 Amp-hour')
_LgpPwrBatteryLeadAcidCellCount_Type=Integer32
_LgpPwrBatteryLeadAcidCellCount_Object=MibScalar
lgpPwrBatteryLeadAcidCellCount=_LgpPwrBatteryLeadAcidCellCount_Object((1,3,6,1,4,1,476,1,42,3,5,1,20,4),_LgpPwrBatteryLeadAcidCellCount_Type())
lgpPwrBatteryLeadAcidCellCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryLeadAcidCellCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryLeadAcidCellCount.setUnits(_H)
_LgpPwrBatteryNiCadCellCount_Type=Integer32
_LgpPwrBatteryNiCadCellCount_Object=MibScalar
lgpPwrBatteryNiCadCellCount=_LgpPwrBatteryNiCadCellCount_Object((1,3,6,1,4,1,476,1,42,3,5,1,20,5),_LgpPwrBatteryNiCadCellCount_Type())
lgpPwrBatteryNiCadCellCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryNiCadCellCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryNiCadCellCount.setUnits(_H)
_LgpPwrBatteryAmpHoursConsumed_Type=Integer32
_LgpPwrBatteryAmpHoursConsumed_Object=MibScalar
lgpPwrBatteryAmpHoursConsumed=_LgpPwrBatteryAmpHoursConsumed_Object((1,3,6,1,4,1,476,1,42,3,5,1,21),_LgpPwrBatteryAmpHoursConsumed_Type())
lgpPwrBatteryAmpHoursConsumed.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryAmpHoursConsumed.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryAmpHoursConsumed.setUnits(_d)
_LgpPwrBatteryAmpHoursDischargeConsumed_Type=Integer32
_LgpPwrBatteryAmpHoursDischargeConsumed_Object=MibScalar
lgpPwrBatteryAmpHoursDischargeConsumed=_LgpPwrBatteryAmpHoursDischargeConsumed_Object((1,3,6,1,4,1,476,1,42,3,5,1,22),_LgpPwrBatteryAmpHoursDischargeConsumed_Type())
lgpPwrBatteryAmpHoursDischargeConsumed.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryAmpHoursDischargeConsumed.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryAmpHoursDischargeConsumed.setUnits(_d)
_LgpPwrBatteryLastDischargeTime_Type=Unsigned32
_LgpPwrBatteryLastDischargeTime_Object=MibScalar
lgpPwrBatteryLastDischargeTime=_LgpPwrBatteryLastDischargeTime_Object((1,3,6,1,4,1,476,1,42,3,5,1,23),_LgpPwrBatteryLastDischargeTime_Type())
lgpPwrBatteryLastDischargeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryLastDischargeTime.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryLastDischargeTime.setUnits(_M)
_LgpPwrBatteryLastCommissionTime_Type=Unsigned32
_LgpPwrBatteryLastCommissionTime_Object=MibScalar
lgpPwrBatteryLastCommissionTime=_LgpPwrBatteryLastCommissionTime_Object((1,3,6,1,4,1,476,1,42,3,5,1,24),_LgpPwrBatteryLastCommissionTime_Type())
lgpPwrBatteryLastCommissionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryLastCommissionTime.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryLastCommissionTime.setUnits(_M)
_LgpPwrBatteryPresentDischargeTime_Type=Integer32
_LgpPwrBatteryPresentDischargeTime_Object=MibScalar
lgpPwrBatteryPresentDischargeTime=_LgpPwrBatteryPresentDischargeTime_Object((1,3,6,1,4,1,476,1,42,3,5,1,25),_LgpPwrBatteryPresentDischargeTime_Type())
lgpPwrBatteryPresentDischargeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryPresentDischargeTime.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryPresentDischargeTime.setUnits(_M)
class _LgpPwrBatteryCapacityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('batteryNormal',2),('batteryLow',3),('batteryDepleted',4)))
_LgpPwrBatteryCapacityStatus_Type.__name__=_C
_LgpPwrBatteryCapacityStatus_Object=MibScalar
lgpPwrBatteryCapacityStatus=_LgpPwrBatteryCapacityStatus_Object((1,3,6,1,4,1,476,1,42,3,5,1,26),_LgpPwrBatteryCapacityStatus_Type())
lgpPwrBatteryCapacityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryCapacityStatus.setStatus(_A)
class _LgpPwrBatteryCircuitBreakerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),(_J,1),(_I,2)))
_LgpPwrBatteryCircuitBreakerState_Type.__name__=_C
_LgpPwrBatteryCircuitBreakerState_Object=MibScalar
lgpPwrBatteryCircuitBreakerState=_LgpPwrBatteryCircuitBreakerState_Object((1,3,6,1,4,1,476,1,42,3,5,1,27),_LgpPwrBatteryCircuitBreakerState_Type())
lgpPwrBatteryCircuitBreakerState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryCircuitBreakerState.setStatus(_A)
_LgpPwrMeasurements_ObjectIdentity=ObjectIdentity
lgpPwrMeasurements=_LgpPwrMeasurements_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2))
if mibBuilder.loadTexts:lgpPwrMeasurements.setStatus(_A)
_LgpPwrWellKnownMeasurementPoints_ObjectIdentity=ObjectIdentity
lgpPwrWellKnownMeasurementPoints=_LgpPwrWellKnownMeasurementPoints_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1))
if mibBuilder.loadTexts:lgpPwrWellKnownMeasurementPoints.setStatus(_A)
_LgpPwrSource1Input_ObjectIdentity=ObjectIdentity
lgpPwrSource1Input=_LgpPwrSource1Input_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,1))
if mibBuilder.loadTexts:lgpPwrSource1Input.setStatus(_A)
_LgpPwrSource2Input_ObjectIdentity=ObjectIdentity
lgpPwrSource2Input=_LgpPwrSource2Input_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,2))
if mibBuilder.loadTexts:lgpPwrSource2Input.setStatus(_A)
_LgpPwrSourcePdu1Input_ObjectIdentity=ObjectIdentity
lgpPwrSourcePdu1Input=_LgpPwrSourcePdu1Input_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,3))
if mibBuilder.loadTexts:lgpPwrSourcePdu1Input.setStatus(_A)
_LgpPwrSourcePdu2Input_ObjectIdentity=ObjectIdentity
lgpPwrSourcePdu2Input=_LgpPwrSourcePdu2Input_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,4))
if mibBuilder.loadTexts:lgpPwrSourcePdu2Input.setStatus(_A)
_LgpPwrOutputToLoad_ObjectIdentity=ObjectIdentity
lgpPwrOutputToLoad=_LgpPwrOutputToLoad_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,5))
if mibBuilder.loadTexts:lgpPwrOutputToLoad.setStatus(_A)
_LgpPwrMeasBattery_ObjectIdentity=ObjectIdentity
lgpPwrMeasBattery=_LgpPwrMeasBattery_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,6))
if mibBuilder.loadTexts:lgpPwrMeasBattery.setStatus(_A)
_LgpPwrMeasBypass_ObjectIdentity=ObjectIdentity
lgpPwrMeasBypass=_LgpPwrMeasBypass_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,7))
if mibBuilder.loadTexts:lgpPwrMeasBypass.setStatus(_A)
_LgpPwrMeasDcBus_ObjectIdentity=ObjectIdentity
lgpPwrMeasDcBus=_LgpPwrMeasDcBus_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,8))
if mibBuilder.loadTexts:lgpPwrMeasDcBus.setStatus(_A)
_LgpPwrMeasSystemOutput_ObjectIdentity=ObjectIdentity
lgpPwrMeasSystemOutput=_LgpPwrMeasSystemOutput_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,9))
if mibBuilder.loadTexts:lgpPwrMeasSystemOutput.setStatus(_A)
_LgpPwrMeasBatteryCabinet_ObjectIdentity=ObjectIdentity
lgpPwrMeasBatteryCabinet=_LgpPwrMeasBatteryCabinet_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,1,10))
if mibBuilder.loadTexts:lgpPwrMeasBatteryCabinet.setStatus(_A)
_LgpPwrMeasurementPointTable_Object=MibTable
lgpPwrMeasurementPointTable=_LgpPwrMeasurementPointTable_Object((1,3,6,1,4,1,476,1,42,3,5,2,2))
if mibBuilder.loadTexts:lgpPwrMeasurementPointTable.setStatus(_A)
_LgpPwrMeasurementPointEntry_Object=MibTableRow
lgpPwrMeasurementPointEntry=_LgpPwrMeasurementPointEntry_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1))
lgpPwrMeasurementPointEntry.setIndexNames((0,_O,_g))
if mibBuilder.loadTexts:lgpPwrMeasurementPointEntry.setStatus(_A)
_LgpPwrMeasurementPointIndex_Type=Unsigned32
_LgpPwrMeasurementPointIndex_Object=MibTableColumn
lgpPwrMeasurementPointIndex=_LgpPwrMeasurementPointIndex_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,1),_LgpPwrMeasurementPointIndex_Type())
lgpPwrMeasurementPointIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:lgpPwrMeasurementPointIndex.setStatus(_A)
_LgpPwrMeasurementPointId_Type=ObjectIdentifier
_LgpPwrMeasurementPointId_Object=MibTableColumn
lgpPwrMeasurementPointId=_LgpPwrMeasurementPointId_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,2),_LgpPwrMeasurementPointId_Type())
lgpPwrMeasurementPointId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointId.setStatus(_A)
_LgpPwrMeasurementPointNumLines_Type=Integer32
_LgpPwrMeasurementPointNumLines_Object=MibTableColumn
lgpPwrMeasurementPointNumLines=_LgpPwrMeasurementPointNumLines_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,3),_LgpPwrMeasurementPointNumLines_Type())
lgpPwrMeasurementPointNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNumLines.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNumLines.setUnits(_H)
_LgpPwrMeasurementPointNomVolts_Type=Integer32
_LgpPwrMeasurementPointNomVolts_Object=MibTableColumn
lgpPwrMeasurementPointNomVolts=_LgpPwrMeasurementPointNomVolts_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,4),_LgpPwrMeasurementPointNomVolts_Type())
lgpPwrMeasurementPointNomVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomVolts.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomVolts.setUnits(_N)
_LgpPwrMeasurementPointNomFrequency_Type=Integer32
_LgpPwrMeasurementPointNomFrequency_Object=MibTableColumn
lgpPwrMeasurementPointNomFrequency=_LgpPwrMeasurementPointNomFrequency_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,5),_LgpPwrMeasurementPointNomFrequency_Type())
lgpPwrMeasurementPointNomFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomFrequency.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomFrequency.setUnits('Hertz')
_LgpPwrMeasurementPointFrequency_Type=Integer32
_LgpPwrMeasurementPointFrequency_Object=MibTableColumn
lgpPwrMeasurementPointFrequency=_LgpPwrMeasurementPointFrequency_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,6),_LgpPwrMeasurementPointFrequency_Type())
lgpPwrMeasurementPointFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointFrequency.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointFrequency.setUnits('Hertz')
_LgpPwrMeasurementPointApparentPower_Type=Integer32
_LgpPwrMeasurementPointApparentPower_Object=MibTableColumn
lgpPwrMeasurementPointApparentPower=_LgpPwrMeasurementPointApparentPower_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,7),_LgpPwrMeasurementPointApparentPower_Type())
lgpPwrMeasurementPointApparentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointApparentPower.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointApparentPower.setUnits(_U)
_LgpPwrMeasurementPointTruePower_Type=Integer32
_LgpPwrMeasurementPointTruePower_Object=MibTableColumn
lgpPwrMeasurementPointTruePower=_LgpPwrMeasurementPointTruePower_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,8),_LgpPwrMeasurementPointTruePower_Type())
lgpPwrMeasurementPointTruePower.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointTruePower.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointTruePower.setUnits(_a)
_LgpPwrMeasurementPointPowerFactor_Type=Integer32
_LgpPwrMeasurementPointPowerFactor_Object=MibTableColumn
lgpPwrMeasurementPointPowerFactor=_LgpPwrMeasurementPointPowerFactor_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,9),_LgpPwrMeasurementPointPowerFactor_Type())
lgpPwrMeasurementPointPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointPowerFactor.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointPowerFactor.setUnits(_h)
_LgpPwrMeasurementPointWattHours_Type=Integer32
_LgpPwrMeasurementPointWattHours_Object=MibTableColumn
lgpPwrMeasurementPointWattHours=_LgpPwrMeasurementPointWattHours_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,10),_LgpPwrMeasurementPointWattHours_Type())
lgpPwrMeasurementPointWattHours.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointWattHours.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointWattHours.setUnits(_i)
_LgpPwrMeasurementPointVAPercent_Type=Integer32
_LgpPwrMeasurementPointVAPercent_Object=MibTableColumn
lgpPwrMeasurementPointVAPercent=_LgpPwrMeasurementPointVAPercent_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,11),_LgpPwrMeasurementPointVAPercent_Type())
lgpPwrMeasurementPointVAPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointVAPercent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointVAPercent.setUnits(_e)
_LgpPwrMeasurementPointNeutralCurrent_Type=Integer32
_LgpPwrMeasurementPointNeutralCurrent_Object=MibTableColumn
lgpPwrMeasurementPointNeutralCurrent=_LgpPwrMeasurementPointNeutralCurrent_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,12),_LgpPwrMeasurementPointNeutralCurrent_Type())
lgpPwrMeasurementPointNeutralCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNeutralCurrent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNeutralCurrent.setUnits(_V)
_LgpPwrMeasurementPointGroundCurrent_Type=Integer32
_LgpPwrMeasurementPointGroundCurrent_Object=MibTableColumn
lgpPwrMeasurementPointGroundCurrent=_LgpPwrMeasurementPointGroundCurrent_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,13),_LgpPwrMeasurementPointGroundCurrent_Type())
lgpPwrMeasurementPointGroundCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointGroundCurrent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointGroundCurrent.setUnits(_j)
_LgpPwrMeasurementPointNomCurrent_Type=Integer32
_LgpPwrMeasurementPointNomCurrent_Object=MibTableColumn
lgpPwrMeasurementPointNomCurrent=_LgpPwrMeasurementPointNomCurrent_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,14),_LgpPwrMeasurementPointNomCurrent_Type())
lgpPwrMeasurementPointNomCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomCurrent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomCurrent.setUnits(_j)
_LgpPwrMeasurementPointNomPowerFactor_Type=Integer32
_LgpPwrMeasurementPointNomPowerFactor_Object=MibTableColumn
lgpPwrMeasurementPointNomPowerFactor=_LgpPwrMeasurementPointNomPowerFactor_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,15),_LgpPwrMeasurementPointNomPowerFactor_Type())
lgpPwrMeasurementPointNomPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomPowerFactor.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomPowerFactor.setUnits(_h)
_LgpPwrMeasurementPointNomVA_Type=Integer32
_LgpPwrMeasurementPointNomVA_Object=MibTableColumn
lgpPwrMeasurementPointNomVA=_LgpPwrMeasurementPointNomVA_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,16),_LgpPwrMeasurementPointNomVA_Type())
lgpPwrMeasurementPointNomVA.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomVA.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomVA.setUnits(_U)
_LgpPwrMeasurementPointNomW_Type=Integer32
_LgpPwrMeasurementPointNomW_Object=MibTableColumn
lgpPwrMeasurementPointNomW=_LgpPwrMeasurementPointNomW_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,17),_LgpPwrMeasurementPointNomW_Type())
lgpPwrMeasurementPointNomW.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomW.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMeasurementPointNomW.setUnits(_a)
class _LgpPwrMeasurementPointPowerFactorTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_LgpPwrMeasurementPointPowerFactorTag_Type.__name__=_C
_LgpPwrMeasurementPointPowerFactorTag_Object=MibTableColumn
lgpPwrMeasurementPointPowerFactorTag=_LgpPwrMeasurementPointPowerFactorTag_Object((1,3,6,1,4,1,476,1,42,3,5,2,2,1,19),_LgpPwrMeasurementPointPowerFactorTag_Type())
lgpPwrMeasurementPointPowerFactorTag.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPointPowerFactorTag.setStatus(_A)
_LgpPwrLineMeasurementTable_Object=MibTable
lgpPwrLineMeasurementTable=_LgpPwrLineMeasurementTable_Object((1,3,6,1,4,1,476,1,42,3,5,2,3))
if mibBuilder.loadTexts:lgpPwrLineMeasurementTable.setStatus(_A)
_LgpPwrLineMeasurementEntry_Object=MibTableRow
lgpPwrLineMeasurementEntry=_LgpPwrLineMeasurementEntry_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1))
lgpPwrLineMeasurementEntry.setIndexNames((0,_O,_m),(0,_O,_n))
if mibBuilder.loadTexts:lgpPwrLineMeasurementEntry.setStatus(_A)
_LgpPwrMeasurementPtIndex_Type=Unsigned32
_LgpPwrMeasurementPtIndex_Object=MibTableColumn
lgpPwrMeasurementPtIndex=_LgpPwrMeasurementPtIndex_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,1),_LgpPwrMeasurementPtIndex_Type())
lgpPwrMeasurementPtIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:lgpPwrMeasurementPtIndex.setStatus(_A)
_LgpPwrLineMeasurementIndex_Type=Unsigned32
_LgpPwrLineMeasurementIndex_Object=MibTableColumn
lgpPwrLineMeasurementIndex=_LgpPwrLineMeasurementIndex_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,2),_LgpPwrLineMeasurementIndex_Type())
lgpPwrLineMeasurementIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:lgpPwrLineMeasurementIndex.setStatus(_A)
_LgpPwrMeasurementPoint_Type=ObjectIdentifier
_LgpPwrMeasurementPoint_Object=MibTableColumn
lgpPwrMeasurementPoint=_LgpPwrMeasurementPoint_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,3),_LgpPwrMeasurementPoint_Type())
lgpPwrMeasurementPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMeasurementPoint.setStatus(_A)
_LgpPwrLineMeasurementVoltsLL_Type=Integer32
_LgpPwrLineMeasurementVoltsLL_Object=MibTableColumn
lgpPwrLineMeasurementVoltsLL=_LgpPwrLineMeasurementVoltsLL_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,4),_LgpPwrLineMeasurementVoltsLL_Type())
lgpPwrLineMeasurementVoltsLL.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVoltsLL.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVoltsLL.setUnits(_N)
_LgpPwrLineMeasurementVoltsLN_Type=Integer32
_LgpPwrLineMeasurementVoltsLN_Object=MibTableColumn
lgpPwrLineMeasurementVoltsLN=_LgpPwrLineMeasurementVoltsLN_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,5),_LgpPwrLineMeasurementVoltsLN_Type())
lgpPwrLineMeasurementVoltsLN.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVoltsLN.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVoltsLN.setUnits(_N)
_LgpPwrLineMeasurementCurrent_Type=Integer32
_LgpPwrLineMeasurementCurrent_Object=MibTableColumn
lgpPwrLineMeasurementCurrent=_LgpPwrLineMeasurementCurrent_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,6),_LgpPwrLineMeasurementCurrent_Type())
lgpPwrLineMeasurementCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementCurrent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementCurrent.setUnits(_V)
_LgpPwrLineMeasurementCapacity_Type=Integer32
_LgpPwrLineMeasurementCapacity_Object=MibTableColumn
lgpPwrLineMeasurementCapacity=_LgpPwrLineMeasurementCapacity_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,7),_LgpPwrLineMeasurementCapacity_Type())
lgpPwrLineMeasurementCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementCapacity.setUnits(_S)
_LgpPwrLineMeasurementVA_Type=Integer32
_LgpPwrLineMeasurementVA_Object=MibTableColumn
lgpPwrLineMeasurementVA=_LgpPwrLineMeasurementVA_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,8),_LgpPwrLineMeasurementVA_Type())
lgpPwrLineMeasurementVA.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVA.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVA.setUnits(_U)
_LgpPwrLineMeasurementTruePower_Type=Integer32
_LgpPwrLineMeasurementTruePower_Object=MibTableColumn
lgpPwrLineMeasurementTruePower=_LgpPwrLineMeasurementTruePower_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,9),_LgpPwrLineMeasurementTruePower_Type())
lgpPwrLineMeasurementTruePower.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementTruePower.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementTruePower.setUnits(_a)
_LgpPwrLineMeasurementVoltageTHD_Type=Integer32
_LgpPwrLineMeasurementVoltageTHD_Object=MibTableColumn
lgpPwrLineMeasurementVoltageTHD=_LgpPwrLineMeasurementVoltageTHD_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,10),_LgpPwrLineMeasurementVoltageTHD_Type())
lgpPwrLineMeasurementVoltageTHD.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVoltageTHD.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVoltageTHD.setUnits(_e)
_LgpPwrLineMeasurementCurrentTHD_Type=Integer32
_LgpPwrLineMeasurementCurrentTHD_Object=MibTableColumn
lgpPwrLineMeasurementCurrentTHD=_LgpPwrLineMeasurementCurrentTHD_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,11),_LgpPwrLineMeasurementCurrentTHD_Type())
lgpPwrLineMeasurementCurrentTHD.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementCurrentTHD.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementCurrentTHD.setUnits(_e)
_LgpPwrLineMeasurementKFactorCurrent_Type=Integer32
_LgpPwrLineMeasurementKFactorCurrent_Object=MibTableColumn
lgpPwrLineMeasurementKFactorCurrent=_LgpPwrLineMeasurementKFactorCurrent_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,12),_LgpPwrLineMeasurementKFactorCurrent_Type())
lgpPwrLineMeasurementKFactorCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementKFactorCurrent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementKFactorCurrent.setUnits('0.1 K Factor')
_LgpPwrLineMeasurementCrestFactorCurrent_Type=Integer32
_LgpPwrLineMeasurementCrestFactorCurrent_Object=MibTableColumn
lgpPwrLineMeasurementCrestFactorCurrent=_LgpPwrLineMeasurementCrestFactorCurrent_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,13),_LgpPwrLineMeasurementCrestFactorCurrent_Type())
lgpPwrLineMeasurementCrestFactorCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementCrestFactorCurrent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementCrestFactorCurrent.setUnits('0.1 Crest Factor')
_LgpPwrLineMeasurementPowerFactor_Type=Integer32
_LgpPwrLineMeasurementPowerFactor_Object=MibTableColumn
lgpPwrLineMeasurementPowerFactor=_LgpPwrLineMeasurementPowerFactor_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,14),_LgpPwrLineMeasurementPowerFactor_Type())
lgpPwrLineMeasurementPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementPowerFactor.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementPowerFactor.setUnits('0.01 Power Factor')
class _LgpPwrLineMeasurementPowerFactorTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_LgpPwrLineMeasurementPowerFactorTag_Type.__name__=_C
_LgpPwrLineMeasurementPowerFactorTag_Object=MibTableColumn
lgpPwrLineMeasurementPowerFactorTag=_LgpPwrLineMeasurementPowerFactorTag_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,15),_LgpPwrLineMeasurementPowerFactorTag_Type())
lgpPwrLineMeasurementPowerFactorTag.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementPowerFactorTag.setStatus(_A)
_LgpPwrLineMeasurementMaxVolts_Type=Integer32
_LgpPwrLineMeasurementMaxVolts_Object=MibTableColumn
lgpPwrLineMeasurementMaxVolts=_LgpPwrLineMeasurementMaxVolts_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,16),_LgpPwrLineMeasurementMaxVolts_Type())
lgpPwrLineMeasurementMaxVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementMaxVolts.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementMaxVolts.setUnits(_N)
_LgpPwrLineMeasurementMinVolts_Type=Integer32
_LgpPwrLineMeasurementMinVolts_Object=MibTableColumn
lgpPwrLineMeasurementMinVolts=_LgpPwrLineMeasurementMinVolts_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,17),_LgpPwrLineMeasurementMinVolts_Type())
lgpPwrLineMeasurementMinVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementMinVolts.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementMinVolts.setUnits(_N)
_LgpPwrLineMeasurementVAR_Type=Integer32
_LgpPwrLineMeasurementVAR_Object=MibTableColumn
lgpPwrLineMeasurementVAR=_LgpPwrLineMeasurementVAR_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,18),_LgpPwrLineMeasurementVAR_Type())
lgpPwrLineMeasurementVAR.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVAR.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVAR.setUnits('Volt-Amp-Reactive')
_LgpPwrLineMeasurementPercentLoad_Type=Integer32
_LgpPwrLineMeasurementPercentLoad_Object=MibTableColumn
lgpPwrLineMeasurementPercentLoad=_LgpPwrLineMeasurementPercentLoad_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,19),_LgpPwrLineMeasurementPercentLoad_Type())
lgpPwrLineMeasurementPercentLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementPercentLoad.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementPercentLoad.setUnits(_S)
_LgpPwrLineMeasurementVolts_Type=Integer32
_LgpPwrLineMeasurementVolts_Object=MibTableColumn
lgpPwrLineMeasurementVolts=_LgpPwrLineMeasurementVolts_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,20),_LgpPwrLineMeasurementVolts_Type())
lgpPwrLineMeasurementVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVolts.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVolts.setUnits(_N)
_LgpPwrLineMeasurementVACapacity_Type=Integer32
_LgpPwrLineMeasurementVACapacity_Object=MibTableColumn
lgpPwrLineMeasurementVACapacity=_LgpPwrLineMeasurementVACapacity_Object((1,3,6,1,4,1,476,1,42,3,5,2,3,1,21),_LgpPwrLineMeasurementVACapacity_Type())
lgpPwrLineMeasurementVACapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVACapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrLineMeasurementVACapacity.setUnits(_S)
_LgpPwrDcMeasurementPointTable_Object=MibTable
lgpPwrDcMeasurementPointTable=_LgpPwrDcMeasurementPointTable_Object((1,3,6,1,4,1,476,1,42,3,5,2,4))
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointTable.setStatus(_A)
_LgpPwrDcMeasurementPointEntry_Object=MibTableRow
lgpPwrDcMeasurementPointEntry=_LgpPwrDcMeasurementPointEntry_Object((1,3,6,1,4,1,476,1,42,3,5,2,4,1))
lgpPwrDcMeasurementPointEntry.setIndexNames((0,_O,_o))
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointEntry.setStatus(_A)
_LgpPwrDcMeasurementPointIndex_Type=Unsigned32
_LgpPwrDcMeasurementPointIndex_Object=MibTableColumn
lgpPwrDcMeasurementPointIndex=_LgpPwrDcMeasurementPointIndex_Object((1,3,6,1,4,1,476,1,42,3,5,2,4,1,1),_LgpPwrDcMeasurementPointIndex_Type())
lgpPwrDcMeasurementPointIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointIndex.setStatus(_A)
_LgpPwrDcMeasurementPointId_Type=ObjectIdentifier
_LgpPwrDcMeasurementPointId_Object=MibTableColumn
lgpPwrDcMeasurementPointId=_LgpPwrDcMeasurementPointId_Object((1,3,6,1,4,1,476,1,42,3,5,2,4,1,2),_LgpPwrDcMeasurementPointId_Type())
lgpPwrDcMeasurementPointId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointId.setStatus(_A)
_LgpPwrDcMeasurementPointSubID_Type=Integer32
_LgpPwrDcMeasurementPointSubID_Object=MibTableColumn
lgpPwrDcMeasurementPointSubID=_LgpPwrDcMeasurementPointSubID_Object((1,3,6,1,4,1,476,1,42,3,5,2,4,1,3),_LgpPwrDcMeasurementPointSubID_Type())
lgpPwrDcMeasurementPointSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointSubID.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointSubID.setUnits(_H)
_LgpPwrDcMeasurementPointVolts_Type=Integer32
_LgpPwrDcMeasurementPointVolts_Object=MibTableColumn
lgpPwrDcMeasurementPointVolts=_LgpPwrDcMeasurementPointVolts_Object((1,3,6,1,4,1,476,1,42,3,5,2,4,1,4),_LgpPwrDcMeasurementPointVolts_Type())
lgpPwrDcMeasurementPointVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointVolts.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointVolts.setUnits(_N)
_LgpPwrDcMeasurementPointCurrent_Type=Integer32
_LgpPwrDcMeasurementPointCurrent_Object=MibTableColumn
lgpPwrDcMeasurementPointCurrent=_LgpPwrDcMeasurementPointCurrent_Object((1,3,6,1,4,1,476,1,42,3,5,2,4,1,5),_LgpPwrDcMeasurementPointCurrent_Type())
lgpPwrDcMeasurementPointCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointCurrent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointCurrent.setUnits(_V)
_LgpPwrDcMeasurementPointNomVolts_Type=Integer32
_LgpPwrDcMeasurementPointNomVolts_Object=MibTableColumn
lgpPwrDcMeasurementPointNomVolts=_LgpPwrDcMeasurementPointNomVolts_Object((1,3,6,1,4,1,476,1,42,3,5,2,4,1,6),_LgpPwrDcMeasurementPointNomVolts_Type())
lgpPwrDcMeasurementPointNomVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointNomVolts.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointNomVolts.setUnits(_N)
_LgpPwrDcMeasurementPointTruePower_Type=Integer32
_LgpPwrDcMeasurementPointTruePower_Object=MibTableColumn
lgpPwrDcMeasurementPointTruePower=_LgpPwrDcMeasurementPointTruePower_Object((1,3,6,1,4,1,476,1,42,3,5,2,4,1,7),_LgpPwrDcMeasurementPointTruePower_Type())
lgpPwrDcMeasurementPointTruePower.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointTruePower.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrDcMeasurementPointTruePower.setUnits(_a)
_LgpPwrWellKnownMeasurementTypes_ObjectIdentity=ObjectIdentity
lgpPwrWellKnownMeasurementTypes=_LgpPwrWellKnownMeasurementTypes_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,5))
if mibBuilder.loadTexts:lgpPwrWellKnownMeasurementTypes.setStatus(_A)
_LgpPwrVoltsAc_ObjectIdentity=ObjectIdentity
lgpPwrVoltsAc=_LgpPwrVoltsAc_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,5,1))
if mibBuilder.loadTexts:lgpPwrVoltsAc.setStatus(_A)
_LgpPwrVoltsDc_ObjectIdentity=ObjectIdentity
lgpPwrVoltsDc=_LgpPwrVoltsDc_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,5,2))
if mibBuilder.loadTexts:lgpPwrVoltsDc.setStatus(_A)
_LgpPwrAmpsNeutral_ObjectIdentity=ObjectIdentity
lgpPwrAmpsNeutral=_LgpPwrAmpsNeutral_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,2,5,3))
if mibBuilder.loadTexts:lgpPwrAmpsNeutral.setStatus(_A)
_LgpPwrStatus_ObjectIdentity=ObjectIdentity
lgpPwrStatus=_LgpPwrStatus_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,3))
if mibBuilder.loadTexts:lgpPwrStatus.setStatus(_A)
_LgpPwrTransferCount_Type=Integer32
_LgpPwrTransferCount_Object=MibScalar
lgpPwrTransferCount=_LgpPwrTransferCount_Object((1,3,6,1,4,1,476,1,42,3,5,3,1),_LgpPwrTransferCount_Type())
lgpPwrTransferCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrTransferCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrTransferCount.setUnits(_H)
_LgpPwrAutoTransferTimer_Type=Integer32
_LgpPwrAutoTransferTimer_Object=MibScalar
lgpPwrAutoTransferTimer=_LgpPwrAutoTransferTimer_Object((1,3,6,1,4,1,476,1,42,3,5,3,2),_LgpPwrAutoTransferTimer_Type())
lgpPwrAutoTransferTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrAutoTransferTimer.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrAutoTransferTimer.setUnits(_M)
class _LgpPwrAutoReTransferEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_LgpPwrAutoReTransferEnabled_Type.__name__=_C
_LgpPwrAutoReTransferEnabled_Object=MibScalar
lgpPwrAutoReTransferEnabled=_LgpPwrAutoReTransferEnabled_Object((1,3,6,1,4,1,476,1,42,3,5,3,3),_LgpPwrAutoReTransferEnabled_Type())
lgpPwrAutoReTransferEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrAutoReTransferEnabled.setStatus(_A)
class _LgpPwrSyncPhaseAngle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3600,3600))
_LgpPwrSyncPhaseAngle_Type.__name__=_C
_LgpPwrSyncPhaseAngle_Object=MibScalar
lgpPwrSyncPhaseAngle=_LgpPwrSyncPhaseAngle_Object((1,3,6,1,4,1,476,1,42,3,5,3,4),_LgpPwrSyncPhaseAngle_Type())
lgpPwrSyncPhaseAngle.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrSyncPhaseAngle.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrSyncPhaseAngle.setUnits(_f)
class _LgpPwrParallelSystemOutputToLoadSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_R,0),(_p,1),(_q,2),(_b,3),(_W,4)))
_LgpPwrParallelSystemOutputToLoadSource_Type.__name__=_C
_LgpPwrParallelSystemOutputToLoadSource_Object=MibScalar
lgpPwrParallelSystemOutputToLoadSource=_LgpPwrParallelSystemOutputToLoadSource_Object((1,3,6,1,4,1,476,1,42,3,5,3,5),_LgpPwrParallelSystemOutputToLoadSource_Type())
lgpPwrParallelSystemOutputToLoadSource.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrParallelSystemOutputToLoadSource.setStatus(_A)
class _LgpPwrDcToDcConverter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrDcToDcConverter_Type.__name__=_C
_LgpPwrDcToDcConverter_Object=MibScalar
lgpPwrDcToDcConverter=_LgpPwrDcToDcConverter_Object((1,3,6,1,4,1,476,1,42,3,5,3,6),_LgpPwrDcToDcConverter_Type())
lgpPwrDcToDcConverter.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrDcToDcConverter.setStatus(_A)
class _LgpPwrOutputToLoadOnInverter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrOutputToLoadOnInverter_Type.__name__=_C
_LgpPwrOutputToLoadOnInverter_Object=MibScalar
lgpPwrOutputToLoadOnInverter=_LgpPwrOutputToLoadOnInverter_Object((1,3,6,1,4,1,476,1,42,3,5,3,7),_LgpPwrOutputToLoadOnInverter_Type())
lgpPwrOutputToLoadOnInverter.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrOutputToLoadOnInverter.setStatus(_A)
class _LgpPwrBatteryChargeCompensating_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrBatteryChargeCompensating_Type.__name__=_C
_LgpPwrBatteryChargeCompensating_Object=MibScalar
lgpPwrBatteryChargeCompensating=_LgpPwrBatteryChargeCompensating_Object((1,3,6,1,4,1,476,1,42,3,5,3,8),_LgpPwrBatteryChargeCompensating_Type())
lgpPwrBatteryChargeCompensating.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryChargeCompensating.setStatus(_A)
class _LgpPwrInverterReady_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrInverterReady_Type.__name__=_C
_LgpPwrInverterReady_Object=MibScalar
lgpPwrInverterReady=_LgpPwrInverterReady_Object((1,3,6,1,4,1,476,1,42,3,5,3,9),_LgpPwrInverterReady_Type())
lgpPwrInverterReady.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrInverterReady.setStatus(_A)
class _LgpPwrOutputToLoadOnBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrOutputToLoadOnBypass_Type.__name__=_C
_LgpPwrOutputToLoadOnBypass_Object=MibScalar
lgpPwrOutputToLoadOnBypass=_LgpPwrOutputToLoadOnBypass_Object((1,3,6,1,4,1,476,1,42,3,5,3,10),_LgpPwrOutputToLoadOnBypass_Type())
lgpPwrOutputToLoadOnBypass.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrOutputToLoadOnBypass.setStatus(_A)
class _LgpPwrBoost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrBoost_Type.__name__=_C
_LgpPwrBoost_Object=MibScalar
lgpPwrBoost=_LgpPwrBoost_Object((1,3,6,1,4,1,476,1,42,3,5,3,11),_LgpPwrBoost_Type())
lgpPwrBoost.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBoost.setStatus(_A)
class _LgpPwrBuck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrBuck_Type.__name__=_C
_LgpPwrBuck_Object=MibScalar
lgpPwrBuck=_LgpPwrBuck_Object((1,3,6,1,4,1,476,1,42,3,5,3,12),_LgpPwrBuck_Type())
lgpPwrBuck.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBuck.setStatus(_A)
class _LgpPwrShutdownOverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownOverTemperature_Type.__name__=_C
_LgpPwrShutdownOverTemperature_Object=MibScalar
lgpPwrShutdownOverTemperature=_LgpPwrShutdownOverTemperature_Object((1,3,6,1,4,1,476,1,42,3,5,3,13),_LgpPwrShutdownOverTemperature_Type())
lgpPwrShutdownOverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownOverTemperature.setStatus(_A)
class _LgpPwrShutdownOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownOverload_Type.__name__=_C
_LgpPwrShutdownOverload_Object=MibScalar
lgpPwrShutdownOverload=_LgpPwrShutdownOverload_Object((1,3,6,1,4,1,476,1,42,3,5,3,14),_LgpPwrShutdownOverload_Type())
lgpPwrShutdownOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownOverload.setStatus(_A)
class _LgpPwrShutdownDcBusOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownDcBusOverload_Type.__name__=_C
_LgpPwrShutdownDcBusOverload_Object=MibScalar
lgpPwrShutdownDcBusOverload=_LgpPwrShutdownDcBusOverload_Object((1,3,6,1,4,1,476,1,42,3,5,3,15),_LgpPwrShutdownDcBusOverload_Type())
lgpPwrShutdownDcBusOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownDcBusOverload.setStatus(_A)
class _LgpPwrShutdownOutputShort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownOutputShort_Type.__name__=_C
_LgpPwrShutdownOutputShort_Object=MibScalar
lgpPwrShutdownOutputShort=_LgpPwrShutdownOutputShort_Object((1,3,6,1,4,1,476,1,42,3,5,3,16),_LgpPwrShutdownOutputShort_Type())
lgpPwrShutdownOutputShort.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownOutputShort.setStatus(_A)
class _LgpPwrShutdownLineSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownLineSwap_Type.__name__=_C
_LgpPwrShutdownLineSwap_Object=MibScalar
lgpPwrShutdownLineSwap=_LgpPwrShutdownLineSwap_Object((1,3,6,1,4,1,476,1,42,3,5,3,17),_LgpPwrShutdownLineSwap_Type())
lgpPwrShutdownLineSwap.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownLineSwap.setStatus(_A)
class _LgpPwrShutdownLowBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownLowBattery_Type.__name__=_C
_LgpPwrShutdownLowBattery_Object=MibScalar
lgpPwrShutdownLowBattery=_LgpPwrShutdownLowBattery_Object((1,3,6,1,4,1,476,1,42,3,5,3,18),_LgpPwrShutdownLowBattery_Type())
lgpPwrShutdownLowBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownLowBattery.setStatus(_A)
class _LgpPwrShutdownRemote_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownRemote_Type.__name__=_C
_LgpPwrShutdownRemote_Object=MibScalar
lgpPwrShutdownRemote=_LgpPwrShutdownRemote_Object((1,3,6,1,4,1,476,1,42,3,5,3,19),_LgpPwrShutdownRemote_Type())
lgpPwrShutdownRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownRemote.setStatus(_A)
class _LgpPwrShutdownInputUnderVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownInputUnderVoltage_Type.__name__=_C
_LgpPwrShutdownInputUnderVoltage_Object=MibScalar
lgpPwrShutdownInputUnderVoltage=_LgpPwrShutdownInputUnderVoltage_Object((1,3,6,1,4,1,476,1,42,3,5,3,20),_LgpPwrShutdownInputUnderVoltage_Type())
lgpPwrShutdownInputUnderVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownInputUnderVoltage.setStatus(_A)
class _LgpPwrShutdownPowerFactorCorrectionFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownPowerFactorCorrectionFailure_Type.__name__=_C
_LgpPwrShutdownPowerFactorCorrectionFailure_Object=MibScalar
lgpPwrShutdownPowerFactorCorrectionFailure=_LgpPwrShutdownPowerFactorCorrectionFailure_Object((1,3,6,1,4,1,476,1,42,3,5,3,21),_LgpPwrShutdownPowerFactorCorrectionFailure_Type())
lgpPwrShutdownPowerFactorCorrectionFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownPowerFactorCorrectionFailure.setStatus(_A)
class _LgpPwrShutdownHardware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrShutdownHardware_Type.__name__=_C
_LgpPwrShutdownHardware_Object=MibScalar
lgpPwrShutdownHardware=_LgpPwrShutdownHardware_Object((1,3,6,1,4,1,476,1,42,3,5,3,22),_LgpPwrShutdownHardware_Type())
lgpPwrShutdownHardware.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrShutdownHardware.setStatus(_A)
class _LgpPwrRedundantSubModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrRedundantSubModule_Type.__name__=_C
_LgpPwrRedundantSubModule_Object=MibScalar
lgpPwrRedundantSubModule=_LgpPwrRedundantSubModule_Object((1,3,6,1,4,1,476,1,42,3,5,3,23),_LgpPwrRedundantSubModule_Type())
lgpPwrRedundantSubModule.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrRedundantSubModule.setStatus(_A)
class _LgpPwrBypassReady_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrBypassReady_Type.__name__=_C
_LgpPwrBypassReady_Object=MibScalar
lgpPwrBypassReady=_LgpPwrBypassReady_Object((1,3,6,1,4,1,476,1,42,3,5,3,24),_LgpPwrBypassReady_Type())
lgpPwrBypassReady.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBypassReady.setStatus(_A)
class _LgpPwrGeneratorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('disconnected',2)))
_LgpPwrGeneratorStatus_Type.__name__=_C
_LgpPwrGeneratorStatus_Object=MibScalar
lgpPwrGeneratorStatus=_LgpPwrGeneratorStatus_Object((1,3,6,1,4,1,476,1,42,3,5,3,25),_LgpPwrGeneratorStatus_Type())
lgpPwrGeneratorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrGeneratorStatus.setStatus(_A)
class _LgpPwrRotaryBreakerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),(_I,2),('test',3),(_P,4),(_b,5),('maintenance',6)))
_LgpPwrRotaryBreakerStatus_Type.__name__=_C
_LgpPwrRotaryBreakerStatus_Object=MibScalar
lgpPwrRotaryBreakerStatus=_LgpPwrRotaryBreakerStatus_Object((1,3,6,1,4,1,476,1,42,3,5,3,26),_LgpPwrRotaryBreakerStatus_Type())
lgpPwrRotaryBreakerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrRotaryBreakerStatus.setStatus(_A)
class _LgpPwrPowerFactorCorrection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrPowerFactorCorrection_Type.__name__=_C
_LgpPwrPowerFactorCorrection_Object=MibScalar
lgpPwrPowerFactorCorrection=_LgpPwrPowerFactorCorrection_Object((1,3,6,1,4,1,476,1,42,3,5,3,27),_LgpPwrPowerFactorCorrection_Type())
lgpPwrPowerFactorCorrection.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrPowerFactorCorrection.setStatus(_A)
_LgpPwrBypassSyncDiff_Type=Integer32
_LgpPwrBypassSyncDiff_Object=MibScalar
lgpPwrBypassSyncDiff=_LgpPwrBypassSyncDiff_Object((1,3,6,1,4,1,476,1,42,3,5,3,28),_LgpPwrBypassSyncDiff_Type())
lgpPwrBypassSyncDiff.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBypassSyncDiff.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBypassSyncDiff.setUnits(_f)
_LgpPwrBypassOverloadShutdownTime_Type=Integer32
_LgpPwrBypassOverloadShutdownTime_Object=MibScalar
lgpPwrBypassOverloadShutdownTime=_LgpPwrBypassOverloadShutdownTime_Object((1,3,6,1,4,1,476,1,42,3,5,3,29),_LgpPwrBypassOverloadShutdownTime_Type())
lgpPwrBypassOverloadShutdownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBypassOverloadShutdownTime.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBypassOverloadShutdownTime.setUnits(_M)
_LgpPwrInverterOverloadShutdownTime_Type=Integer32
_LgpPwrInverterOverloadShutdownTime_Object=MibScalar
lgpPwrInverterOverloadShutdownTime=_LgpPwrInverterOverloadShutdownTime_Object((1,3,6,1,4,1,476,1,42,3,5,3,30),_LgpPwrInverterOverloadShutdownTime_Type())
lgpPwrInverterOverloadShutdownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrInverterOverloadShutdownTime.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrInverterOverloadShutdownTime.setUnits(_M)
class _LgpPwrStateOutputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),('inverter',2),(_b,3),('maintenanceBypass',4)))
_LgpPwrStateOutputSource_Type.__name__=_C
_LgpPwrStateOutputSource_Object=MibScalar
lgpPwrStateOutputSource=_LgpPwrStateOutputSource_Object((1,3,6,1,4,1,476,1,42,3,5,3,31),_LgpPwrStateOutputSource_Type())
lgpPwrStateOutputSource.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateOutputSource.setStatus(_A)
class _LgpPwrStateInputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_p,2),('generator',3)))
_LgpPwrStateInputSource_Type.__name__=_C
_LgpPwrStateInputSource_Object=MibScalar
lgpPwrStateInputSource=_LgpPwrStateInputSource_Object((1,3,6,1,4,1,476,1,42,3,5,3,32),_LgpPwrStateInputSource_Type())
lgpPwrStateInputSource.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateInputSource.setStatus(_A)
class _LgpPwrStateInputQualification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_Y,2),(_P,3),(_Z,4)))
_LgpPwrStateInputQualification_Type.__name__=_C
_LgpPwrStateInputQualification_Object=MibScalar
lgpPwrStateInputQualification=_LgpPwrStateInputQualification_Object((1,3,6,1,4,1,476,1,42,3,5,3,33),_LgpPwrStateInputQualification_Type())
lgpPwrStateInputQualification.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateInputQualification.setStatus(_A)
class _LgpPwrStateBypassStaticSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrStateBypassStaticSwitchState_Type.__name__=_C
_LgpPwrStateBypassStaticSwitchState_Object=MibScalar
lgpPwrStateBypassStaticSwitchState=_LgpPwrStateBypassStaticSwitchState_Object((1,3,6,1,4,1,476,1,42,3,5,3,34),_LgpPwrStateBypassStaticSwitchState_Type())
lgpPwrStateBypassStaticSwitchState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateBypassStaticSwitchState.setStatus(_A)
class _LgpPwrStateBypassQualification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_Y,2),(_P,3),(_Z,4)))
_LgpPwrStateBypassQualification_Type.__name__=_C
_LgpPwrStateBypassQualification_Object=MibScalar
lgpPwrStateBypassQualification=_LgpPwrStateBypassQualification_Object((1,3,6,1,4,1,476,1,42,3,5,3,35),_LgpPwrStateBypassQualification_Type())
lgpPwrStateBypassQualification.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateBypassQualification.setStatus(_A)
class _LgpPwrStateDCBusQualification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_Y,2),(_P,3),(_Z,4)))
_LgpPwrStateDCBusQualification_Type.__name__=_C
_LgpPwrStateDCBusQualification_Object=MibScalar
lgpPwrStateDCBusQualification=_LgpPwrStateDCBusQualification_Object((1,3,6,1,4,1,476,1,42,3,5,3,36),_LgpPwrStateDCBusQualification_Type())
lgpPwrStateDCBusQualification.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateDCBusQualification.setStatus(_A)
class _LgpPwrStateOutQualification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_Y,2),(_P,3),(_Z,4)))
_LgpPwrStateOutQualification_Type.__name__=_C
_LgpPwrStateOutQualification_Object=MibScalar
lgpPwrStateOutQualification=_LgpPwrStateOutQualification_Object((1,3,6,1,4,1,476,1,42,3,5,3,37),_LgpPwrStateOutQualification_Type())
lgpPwrStateOutQualification.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateOutQualification.setStatus(_A)
class _LgpPwrStateInverterQualification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_Y,2),(_P,3),(_Z,4)))
_LgpPwrStateInverterQualification_Type.__name__=_C
_LgpPwrStateInverterQualification_Object=MibScalar
lgpPwrStateInverterQualification=_LgpPwrStateInverterQualification_Object((1,3,6,1,4,1,476,1,42,3,5,3,38),_LgpPwrStateInverterQualification_Type())
lgpPwrStateInverterQualification.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateInverterQualification.setStatus(_A)
class _LgpPwrStateInverterState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrStateInverterState_Type.__name__=_C
_LgpPwrStateInverterState_Object=MibScalar
lgpPwrStateInverterState=_LgpPwrStateInverterState_Object((1,3,6,1,4,1,476,1,42,3,5,3,39),_LgpPwrStateInverterState_Type())
lgpPwrStateInverterState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateInverterState.setStatus(_A)
class _LgpPwrStateRectifierState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrStateRectifierState_Type.__name__=_C
_LgpPwrStateRectifierState_Object=MibScalar
lgpPwrStateRectifierState=_LgpPwrStateRectifierState_Object((1,3,6,1,4,1,476,1,42,3,5,3,40),_LgpPwrStateRectifierState_Type())
lgpPwrStateRectifierState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateRectifierState.setStatus(_A)
_LgpPwrStateModuleGroup_ObjectIdentity=ObjectIdentity
lgpPwrStateModuleGroup=_LgpPwrStateModuleGroup_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,3,41))
if mibBuilder.loadTexts:lgpPwrStateModuleGroup.setStatus(_A)
_LgpPwrStateUpsModuleCount_Type=Integer32
_LgpPwrStateUpsModuleCount_Object=MibScalar
lgpPwrStateUpsModuleCount=_LgpPwrStateUpsModuleCount_Object((1,3,6,1,4,1,476,1,42,3,5,3,41,1),_LgpPwrStateUpsModuleCount_Type())
lgpPwrStateUpsModuleCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrStateUpsModuleCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrStateUpsModuleCount.setUnits(_H)
_LgpPwrStateUpsModuleRedundantCount_Type=Integer32
_LgpPwrStateUpsModuleRedundantCount_Object=MibScalar
lgpPwrStateUpsModuleRedundantCount=_LgpPwrStateUpsModuleRedundantCount_Object((1,3,6,1,4,1,476,1,42,3,5,3,41,2),_LgpPwrStateUpsModuleRedundantCount_Type())
lgpPwrStateUpsModuleRedundantCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateUpsModuleRedundantCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrStateUpsModuleRedundantCount.setUnits(_H)
class _LgpPwrStateBackfeedBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateBackfeedBrkrState_Type.__name__=_C
_LgpPwrStateBackfeedBrkrState_Object=MibScalar
lgpPwrStateBackfeedBrkrState=_LgpPwrStateBackfeedBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,42),_LgpPwrStateBackfeedBrkrState_Type())
lgpPwrStateBackfeedBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateBackfeedBrkrState.setStatus(_A)
class _LgpPwrStateLoadDisconnectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateLoadDisconnectState_Type.__name__=_C
_LgpPwrStateLoadDisconnectState_Object=MibScalar
lgpPwrStateLoadDisconnectState=_LgpPwrStateLoadDisconnectState_Object((1,3,6,1,4,1,476,1,42,3,5,3,43),_LgpPwrStateLoadDisconnectState_Type())
lgpPwrStateLoadDisconnectState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateLoadDisconnectState.setStatus(_A)
class _LgpPwrStateInputBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateInputBrkrState_Type.__name__=_C
_LgpPwrStateInputBrkrState_Object=MibScalar
lgpPwrStateInputBrkrState=_LgpPwrStateInputBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,44),_LgpPwrStateInputBrkrState_Type())
lgpPwrStateInputBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateInputBrkrState.setStatus(_A)
class _LgpPwrStateTrapFilterBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateTrapFilterBrkrState_Type.__name__=_C
_LgpPwrStateTrapFilterBrkrState_Object=MibScalar
lgpPwrStateTrapFilterBrkrState=_LgpPwrStateTrapFilterBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,45),_LgpPwrStateTrapFilterBrkrState_Type())
lgpPwrStateTrapFilterBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateTrapFilterBrkrState.setStatus(_A)
class _LgpPwrStateInvOutputBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateInvOutputBrkrState_Type.__name__=_C
_LgpPwrStateInvOutputBrkrState_Object=MibScalar
lgpPwrStateInvOutputBrkrState=_LgpPwrStateInvOutputBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,46),_LgpPwrStateInvOutputBrkrState_Type())
lgpPwrStateInvOutputBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateInvOutputBrkrState.setStatus(_A)
class _LgpPwrStateIntBypassBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateIntBypassBrkrState_Type.__name__=_C
_LgpPwrStateIntBypassBrkrState_Object=MibScalar
lgpPwrStateIntBypassBrkrState=_LgpPwrStateIntBypassBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,47),_LgpPwrStateIntBypassBrkrState_Type())
lgpPwrStateIntBypassBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateIntBypassBrkrState.setStatus(_A)
class _LgpPwrStateBypassIsolBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateBypassIsolBrkrState_Type.__name__=_C
_LgpPwrStateBypassIsolBrkrState_Object=MibScalar
lgpPwrStateBypassIsolBrkrState=_LgpPwrStateBypassIsolBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,48),_LgpPwrStateBypassIsolBrkrState_Type())
lgpPwrStateBypassIsolBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateBypassIsolBrkrState.setStatus(_A)
class _LgpPwrStateRectifierIsolBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateRectifierIsolBrkrState_Type.__name__=_C
_LgpPwrStateRectifierIsolBrkrState_Object=MibScalar
lgpPwrStateRectifierIsolBrkrState=_LgpPwrStateRectifierIsolBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,49),_LgpPwrStateRectifierIsolBrkrState_Type())
lgpPwrStateRectifierIsolBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateRectifierIsolBrkrState.setStatus(_A)
class _LgpPwrStateMaintBypassBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateMaintBypassBrkrState_Type.__name__=_C
_LgpPwrStateMaintBypassBrkrState_Object=MibScalar
lgpPwrStateMaintBypassBrkrState=_LgpPwrStateMaintBypassBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,50),_LgpPwrStateMaintBypassBrkrState_Type())
lgpPwrStateMaintBypassBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateMaintBypassBrkrState.setStatus(_A)
class _LgpPwrStateMaintIsolBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateMaintIsolBrkrState_Type.__name__=_C
_LgpPwrStateMaintIsolBrkrState_Object=MibScalar
lgpPwrStateMaintIsolBrkrState=_LgpPwrStateMaintIsolBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,51),_LgpPwrStateMaintIsolBrkrState_Type())
lgpPwrStateMaintIsolBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateMaintIsolBrkrState.setStatus(_A)
class _LgpPwrStateOutStaticSwState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_K,2),(_E,3)))
_LgpPwrStateOutStaticSwState_Type.__name__=_C
_LgpPwrStateOutStaticSwState_Object=MibScalar
lgpPwrStateOutStaticSwState=_LgpPwrStateOutStaticSwState_Object((1,3,6,1,4,1,476,1,42,3,5,3,52),_LgpPwrStateOutStaticSwState_Type())
lgpPwrStateOutStaticSwState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateOutStaticSwState.setStatus(_A)
class _LgpPwrStateModuleOutBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateModuleOutBrkrState_Type.__name__=_C
_LgpPwrStateModuleOutBrkrState_Object=MibScalar
lgpPwrStateModuleOutBrkrState=_LgpPwrStateModuleOutBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,53),_LgpPwrStateModuleOutBrkrState_Type())
lgpPwrStateModuleOutBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateModuleOutBrkrState.setStatus(_A)
_LgpPwrBypassReXfrRemainTime_Type=Integer32
_LgpPwrBypassReXfrRemainTime_Object=MibScalar
lgpPwrBypassReXfrRemainTime=_LgpPwrBypassReXfrRemainTime_Object((1,3,6,1,4,1,476,1,42,3,5,3,54),_LgpPwrBypassReXfrRemainTime_Type())
lgpPwrBypassReXfrRemainTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBypassReXfrRemainTime.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBypassReXfrRemainTime.setUnits(_M)
class _LgpPwrStateUpsOutputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),(_W,2),(_P,3),(_b,4),(_q,5),('booster',6),('reducer',7)))
_LgpPwrStateUpsOutputSource_Type.__name__=_C
_LgpPwrStateUpsOutputSource_Object=MibScalar
lgpPwrStateUpsOutputSource=_LgpPwrStateUpsOutputSource_Object((1,3,6,1,4,1,476,1,42,3,5,3,55),_LgpPwrStateUpsOutputSource_Type())
lgpPwrStateUpsOutputSource.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateUpsOutputSource.setStatus(_A)
class _LgpPwrStateLoadBusSynchronization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('active',1),('abnormal',2)))
_LgpPwrStateLoadBusSynchronization_Type.__name__=_C
_LgpPwrStateLoadBusSynchronization_Object=MibScalar
lgpPwrStateLoadBusSynchronization=_LgpPwrStateLoadBusSynchronization_Object((1,3,6,1,4,1,476,1,42,3,5,3,56),_LgpPwrStateLoadBusSynchronization_Type())
lgpPwrStateLoadBusSynchronization.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateLoadBusSynchronization.setStatus(_A)
_LgpPwrStateCircuitBrkrStateGroup_ObjectIdentity=ObjectIdentity
lgpPwrStateCircuitBrkrStateGroup=_LgpPwrStateCircuitBrkrStateGroup_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,3,57))
if mibBuilder.loadTexts:lgpPwrStateCircuitBrkrStateGroup.setStatus(_A)
class _LgpPwrStateSource1InputBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateSource1InputBrkrState_Type.__name__=_C
_LgpPwrStateSource1InputBrkrState_Object=MibScalar
lgpPwrStateSource1InputBrkrState=_LgpPwrStateSource1InputBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,57,1),_LgpPwrStateSource1InputBrkrState_Type())
lgpPwrStateSource1InputBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateSource1InputBrkrState.setStatus(_A)
class _LgpPwrStateSource2InputBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateSource2InputBrkrState_Type.__name__=_C
_LgpPwrStateSource2InputBrkrState_Object=MibScalar
lgpPwrStateSource2InputBrkrState=_LgpPwrStateSource2InputBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,57,2),_LgpPwrStateSource2InputBrkrState_Type())
lgpPwrStateSource2InputBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateSource2InputBrkrState.setStatus(_A)
class _LgpPwrStateSource1BypassBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateSource1BypassBrkrState_Type.__name__=_C
_LgpPwrStateSource1BypassBrkrState_Object=MibScalar
lgpPwrStateSource1BypassBrkrState=_LgpPwrStateSource1BypassBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,57,3),_LgpPwrStateSource1BypassBrkrState_Type())
lgpPwrStateSource1BypassBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateSource1BypassBrkrState.setStatus(_A)
class _LgpPwrStateSource2BypassBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateSource2BypassBrkrState_Type.__name__=_C
_LgpPwrStateSource2BypassBrkrState_Object=MibScalar
lgpPwrStateSource2BypassBrkrState=_LgpPwrStateSource2BypassBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,57,4),_LgpPwrStateSource2BypassBrkrState_Type())
lgpPwrStateSource2BypassBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateSource2BypassBrkrState.setStatus(_A)
class _LgpPwrStateOutputBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateOutputBrkrState_Type.__name__=_C
_LgpPwrStateOutputBrkrState_Object=MibScalar
lgpPwrStateOutputBrkrState=_LgpPwrStateOutputBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,57,5),_LgpPwrStateOutputBrkrState_Type())
lgpPwrStateOutputBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateOutputBrkrState.setStatus(_A)
class _LgpPwrStateAuxOutputBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateAuxOutputBrkrState_Type.__name__=_C
_LgpPwrStateAuxOutputBrkrState_Object=MibScalar
lgpPwrStateAuxOutputBrkrState=_LgpPwrStateAuxOutputBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,57,6),_LgpPwrStateAuxOutputBrkrState_Type())
lgpPwrStateAuxOutputBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateAuxOutputBrkrState.setStatus(_A)
class _LgpPwrStateSource1PduInputBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateSource1PduInputBrkrState_Type.__name__=_C
_LgpPwrStateSource1PduInputBrkrState_Object=MibScalar
lgpPwrStateSource1PduInputBrkrState=_LgpPwrStateSource1PduInputBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,57,7),_LgpPwrStateSource1PduInputBrkrState_Type())
lgpPwrStateSource1PduInputBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateSource1PduInputBrkrState.setStatus(_A)
class _LgpPwrStateSource2PduInputBrkrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_I,2),(_E,3)))
_LgpPwrStateSource2PduInputBrkrState_Type.__name__=_C
_LgpPwrStateSource2PduInputBrkrState_Object=MibScalar
lgpPwrStateSource2PduInputBrkrState=_LgpPwrStateSource2PduInputBrkrState_Object((1,3,6,1,4,1,476,1,42,3,5,3,57,8),_LgpPwrStateSource2PduInputBrkrState_Type())
lgpPwrStateSource2PduInputBrkrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateSource2PduInputBrkrState.setStatus(_A)
class _LgpPwrEconomicOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_K,1)))
_LgpPwrEconomicOperation_Type.__name__=_C
_LgpPwrEconomicOperation_Object=MibScalar
lgpPwrEconomicOperation=_LgpPwrEconomicOperation_Object((1,3,6,1,4,1,476,1,42,3,5,3,58),_LgpPwrEconomicOperation_Type())
lgpPwrEconomicOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrEconomicOperation.setStatus(_A)
_LgpPwrSettings_ObjectIdentity=ObjectIdentity
lgpPwrSettings=_LgpPwrSettings_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,4))
if mibBuilder.loadTexts:lgpPwrSettings.setStatus(_A)
_LgpPwrPreferredSource_Type=ObjectIdentifier
_LgpPwrPreferredSource_Object=MibScalar
lgpPwrPreferredSource=_LgpPwrPreferredSource_Object((1,3,6,1,4,1,476,1,42,3,5,4,1),_LgpPwrPreferredSource_Type())
lgpPwrPreferredSource.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrPreferredSource.setStatus(_A)
_LgpPwrLoadOnSource_Type=ObjectIdentifier
_LgpPwrLoadOnSource_Object=MibScalar
lgpPwrLoadOnSource=_LgpPwrLoadOnSource_Object((1,3,6,1,4,1,476,1,42,3,5,4,2),_LgpPwrLoadOnSource_Type())
lgpPwrLoadOnSource.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLoadOnSource.setStatus(_A)
_LgpPwrNominalVoltageDeviation_Type=Integer32
_LgpPwrNominalVoltageDeviation_Object=MibScalar
lgpPwrNominalVoltageDeviation=_LgpPwrNominalVoltageDeviation_Object((1,3,6,1,4,1,476,1,42,3,5,4,3),_LgpPwrNominalVoltageDeviation_Type())
lgpPwrNominalVoltageDeviation.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNominalVoltageDeviation.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNominalVoltageDeviation.setUnits(_N)
_LgpPwrNominalVoltageDeviationPercent_Type=Integer32
_LgpPwrNominalVoltageDeviationPercent_Object=MibScalar
lgpPwrNominalVoltageDeviationPercent=_LgpPwrNominalVoltageDeviationPercent_Object((1,3,6,1,4,1,476,1,42,3,5,4,4),_LgpPwrNominalVoltageDeviationPercent_Type())
lgpPwrNominalVoltageDeviationPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNominalVoltageDeviationPercent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNominalVoltageDeviationPercent.setUnits(_S)
_LgpPwrPhaseDifferenceLimit_Type=Integer32
_LgpPwrPhaseDifferenceLimit_Object=MibScalar
lgpPwrPhaseDifferenceLimit=_LgpPwrPhaseDifferenceLimit_Object((1,3,6,1,4,1,476,1,42,3,5,4,5),_LgpPwrPhaseDifferenceLimit_Type())
lgpPwrPhaseDifferenceLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrPhaseDifferenceLimit.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrPhaseDifferenceLimit.setUnits(_f)
_LgpPwrFrequencyDeviationLimit_Type=Integer32
_LgpPwrFrequencyDeviationLimit_Object=MibScalar
lgpPwrFrequencyDeviationLimit=_LgpPwrFrequencyDeviationLimit_Object((1,3,6,1,4,1,476,1,42,3,5,4,6),_LgpPwrFrequencyDeviationLimit_Type())
lgpPwrFrequencyDeviationLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrFrequencyDeviationLimit.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrFrequencyDeviationLimit.setUnits('0.1 Hertz')
_LgpPwrThresholdTable_Object=MibTable
lgpPwrThresholdTable=_LgpPwrThresholdTable_Object((1,3,6,1,4,1,476,1,42,3,5,4,7))
if mibBuilder.loadTexts:lgpPwrThresholdTable.setStatus(_A)
_LgpPwrThresholdEntry_Object=MibTableRow
lgpPwrThresholdEntry=_LgpPwrThresholdEntry_Object((1,3,6,1,4,1,476,1,42,3,5,4,7,1))
lgpPwrThresholdEntry.setIndexNames((0,_O,_r))
if mibBuilder.loadTexts:lgpPwrThresholdEntry.setStatus(_A)
_LgpPwrThresholdIndex_Type=Unsigned32
_LgpPwrThresholdIndex_Object=MibTableColumn
lgpPwrThresholdIndex=_LgpPwrThresholdIndex_Object((1,3,6,1,4,1,476,1,42,3,5,4,7,1,1),_LgpPwrThresholdIndex_Type())
lgpPwrThresholdIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:lgpPwrThresholdIndex.setStatus(_A)
_LgpPwrThresholdPoint_Type=ObjectIdentifier
_LgpPwrThresholdPoint_Object=MibTableColumn
lgpPwrThresholdPoint=_LgpPwrThresholdPoint_Object((1,3,6,1,4,1,476,1,42,3,5,4,7,1,2),_LgpPwrThresholdPoint_Type())
lgpPwrThresholdPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrThresholdPoint.setStatus(_A)
_LgpPwrThresholdSubID_Type=Unsigned32
_LgpPwrThresholdSubID_Object=MibTableColumn
lgpPwrThresholdSubID=_LgpPwrThresholdSubID_Object((1,3,6,1,4,1,476,1,42,3,5,4,7,1,3),_LgpPwrThresholdSubID_Type())
lgpPwrThresholdSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrThresholdSubID.setStatus(_A)
_LgpPwrThresholdType_Type=ObjectIdentifier
_LgpPwrThresholdType_Object=MibTableColumn
lgpPwrThresholdType=_LgpPwrThresholdType_Object((1,3,6,1,4,1,476,1,42,3,5,4,7,1,4),_LgpPwrThresholdType_Type())
lgpPwrThresholdType.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrThresholdType.setStatus(_A)
_LgpPwrThresholdHighWarning_Type=Integer32
_LgpPwrThresholdHighWarning_Object=MibTableColumn
lgpPwrThresholdHighWarning=_LgpPwrThresholdHighWarning_Object((1,3,6,1,4,1,476,1,42,3,5,4,7,1,5),_LgpPwrThresholdHighWarning_Type())
lgpPwrThresholdHighWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrThresholdHighWarning.setStatus(_A)
_LgpPwrThresholdHighFailure_Type=Integer32
_LgpPwrThresholdHighFailure_Object=MibTableColumn
lgpPwrThresholdHighFailure=_LgpPwrThresholdHighFailure_Object((1,3,6,1,4,1,476,1,42,3,5,4,7,1,6),_LgpPwrThresholdHighFailure_Type())
lgpPwrThresholdHighFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrThresholdHighFailure.setStatus(_A)
_LgpPwrThresholdLowWarning_Type=Integer32
_LgpPwrThresholdLowWarning_Object=MibTableColumn
lgpPwrThresholdLowWarning=_LgpPwrThresholdLowWarning_Object((1,3,6,1,4,1,476,1,42,3,5,4,7,1,7),_LgpPwrThresholdLowWarning_Type())
lgpPwrThresholdLowWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrThresholdLowWarning.setStatus(_A)
_LgpPwrThresholdLowFailure_Type=Integer32
_LgpPwrThresholdLowFailure_Object=MibTableColumn
lgpPwrThresholdLowFailure=_LgpPwrThresholdLowFailure_Object((1,3,6,1,4,1,476,1,42,3,5,4,7,1,8),_LgpPwrThresholdLowFailure_Type())
lgpPwrThresholdLowFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrThresholdLowFailure.setStatus(_A)
class _LgpPwrUpsAutoRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrUpsAutoRestart_Type.__name__=_C
_LgpPwrUpsAutoRestart_Object=MibScalar
lgpPwrUpsAutoRestart=_LgpPwrUpsAutoRestart_Object((1,3,6,1,4,1,476,1,42,3,5,4,8),_LgpPwrUpsAutoRestart_Type())
lgpPwrUpsAutoRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrUpsAutoRestart.setStatus(_A)
_LgpPwrUpsAutoRestartDelay_Type=Integer32
_LgpPwrUpsAutoRestartDelay_Object=MibScalar
lgpPwrUpsAutoRestartDelay=_LgpPwrUpsAutoRestartDelay_Object((1,3,6,1,4,1,476,1,42,3,5,4,9),_LgpPwrUpsAutoRestartDelay_Type())
lgpPwrUpsAutoRestartDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrUpsAutoRestartDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrUpsAutoRestartDelay.setUnits(_M)
_LgpPwrAutoRestartBatteryChargeThreshold_Type=Integer32
_LgpPwrAutoRestartBatteryChargeThreshold_Object=MibScalar
lgpPwrAutoRestartBatteryChargeThreshold=_LgpPwrAutoRestartBatteryChargeThreshold_Object((1,3,6,1,4,1,476,1,42,3,5,4,10),_LgpPwrAutoRestartBatteryChargeThreshold_Type())
lgpPwrAutoRestartBatteryChargeThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrAutoRestartBatteryChargeThreshold.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrAutoRestartBatteryChargeThreshold.setUnits(_S)
_LgpPwrParallelModuleCount_Type=Integer32
_LgpPwrParallelModuleCount_Object=MibScalar
lgpPwrParallelModuleCount=_LgpPwrParallelModuleCount_Object((1,3,6,1,4,1,476,1,42,3,5,4,11),_LgpPwrParallelModuleCount_Type())
lgpPwrParallelModuleCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrParallelModuleCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrParallelModuleCount.setUnits(_H)
_LgpPwrParallelRedundancyCount_Type=Integer32
_LgpPwrParallelRedundancyCount_Object=MibScalar
lgpPwrParallelRedundancyCount=_LgpPwrParallelRedundancyCount_Object((1,3,6,1,4,1,476,1,42,3,5,4,12),_LgpPwrParallelRedundancyCount_Type())
lgpPwrParallelRedundancyCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrParallelRedundancyCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrParallelRedundancyCount.setUnits(_H)
class _LgpPwrLoadBusSyncMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),(_W,3)))
_LgpPwrLoadBusSyncMode_Type.__name__=_C
_LgpPwrLoadBusSyncMode_Object=MibScalar
lgpPwrLoadBusSyncMode=_LgpPwrLoadBusSyncMode_Object((1,3,6,1,4,1,476,1,42,3,5,4,13),_LgpPwrLoadBusSyncMode_Type())
lgpPwrLoadBusSyncMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrLoadBusSyncMode.setStatus(_A)
class _LgpPwrEconomicOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrEconomicOperationMode_Type.__name__=_C
_LgpPwrEconomicOperationMode_Object=MibScalar
lgpPwrEconomicOperationMode=_LgpPwrEconomicOperationMode_Object((1,3,6,1,4,1,476,1,42,3,5,4,14),_LgpPwrEconomicOperationMode_Type())
lgpPwrEconomicOperationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrEconomicOperationMode.setStatus(_A)
class _LgpPwrAutomaticBatteryTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrAutomaticBatteryTest_Type.__name__=_C
_LgpPwrAutomaticBatteryTest_Object=MibScalar
lgpPwrAutomaticBatteryTest=_LgpPwrAutomaticBatteryTest_Object((1,3,6,1,4,1,476,1,42,3,5,4,15),_LgpPwrAutomaticBatteryTest_Type())
lgpPwrAutomaticBatteryTest.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrAutomaticBatteryTest.setStatus(_A)
_LgpPwrMinimumRedundantPowerModule_Type=Integer32
_LgpPwrMinimumRedundantPowerModule_Object=MibScalar
lgpPwrMinimumRedundantPowerModule=_LgpPwrMinimumRedundantPowerModule_Object((1,3,6,1,4,1,476,1,42,3,5,4,16),_LgpPwrMinimumRedundantPowerModule_Type())
lgpPwrMinimumRedundantPowerModule.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrMinimumRedundantPowerModule.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMinimumRedundantPowerModule.setUnits(_H)
_LgpPwrMinimumRedundantBatteryModule_Type=Integer32
_LgpPwrMinimumRedundantBatteryModule_Object=MibScalar
lgpPwrMinimumRedundantBatteryModule=_LgpPwrMinimumRedundantBatteryModule_Object((1,3,6,1,4,1,476,1,42,3,5,4,17),_LgpPwrMinimumRedundantBatteryModule_Type())
lgpPwrMinimumRedundantBatteryModule.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrMinimumRedundantBatteryModule.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMinimumRedundantBatteryModule.setUnits(_H)
_LgpPwrOutputToLoadUserOverloadLimit_Type=Integer32
_LgpPwrOutputToLoadUserOverloadLimit_Object=MibScalar
lgpPwrOutputToLoadUserOverloadLimit=_LgpPwrOutputToLoadUserOverloadLimit_Object((1,3,6,1,4,1,476,1,42,3,5,4,18),_LgpPwrOutputToLoadUserOverloadLimit_Type())
lgpPwrOutputToLoadUserOverloadLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrOutputToLoadUserOverloadLimit.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrOutputToLoadUserOverloadLimit.setUnits(_U)
_LgpPwrNoLoadWarningLimit_Type=Integer32
_LgpPwrNoLoadWarningLimit_Object=MibScalar
lgpPwrNoLoadWarningLimit=_LgpPwrNoLoadWarningLimit_Object((1,3,6,1,4,1,476,1,42,3,5,4,19),_LgpPwrNoLoadWarningLimit_Type())
lgpPwrNoLoadWarningLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrNoLoadWarningLimit.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNoLoadWarningLimit.setUnits(_V)
class _LgpPwrNoLoadWarningDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_LgpPwrNoLoadWarningDelay_Type.__name__=_C
_LgpPwrNoLoadWarningDelay_Object=MibScalar
lgpPwrNoLoadWarningDelay=_LgpPwrNoLoadWarningDelay_Object((1,3,6,1,4,1,476,1,42,3,5,4,20),_LgpPwrNoLoadWarningDelay_Type())
lgpPwrNoLoadWarningDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrNoLoadWarningDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNoLoadWarningDelay.setUnits(_Q)
class _LgpPwrEconomicOperationModeControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('mode1',1),('mode2',2)))
_LgpPwrEconomicOperationModeControl_Type.__name__=_C
_LgpPwrEconomicOperationModeControl_Object=MibScalar
lgpPwrEconomicOperationModeControl=_LgpPwrEconomicOperationModeControl_Object((1,3,6,1,4,1,476,1,42,3,5,4,21),_LgpPwrEconomicOperationModeControl_Type())
lgpPwrEconomicOperationModeControl.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrEconomicOperationModeControl.setStatus(_A)
_LgpPwrConversion_ObjectIdentity=ObjectIdentity
lgpPwrConversion=_LgpPwrConversion_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,5))
if mibBuilder.loadTexts:lgpPwrConversion.setStatus(_A)
_LgpPwrNumberInstalledPowerModules_Type=Integer32
_LgpPwrNumberInstalledPowerModules_Object=MibScalar
lgpPwrNumberInstalledPowerModules=_LgpPwrNumberInstalledPowerModules_Object((1,3,6,1,4,1,476,1,42,3,5,5,1),_LgpPwrNumberInstalledPowerModules_Type())
lgpPwrNumberInstalledPowerModules.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberInstalledPowerModules.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNumberInstalledPowerModules.setUnits(_H)
_LgpPwrNumberFailedPowerModules_Type=Integer32
_LgpPwrNumberFailedPowerModules_Object=MibScalar
lgpPwrNumberFailedPowerModules=_LgpPwrNumberFailedPowerModules_Object((1,3,6,1,4,1,476,1,42,3,5,5,2),_LgpPwrNumberFailedPowerModules_Type())
lgpPwrNumberFailedPowerModules.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberFailedPowerModules.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNumberFailedPowerModules.setUnits(_H)
_LgpPwrNumberRedundantPowerModules_Type=Integer32
_LgpPwrNumberRedundantPowerModules_Object=MibScalar
lgpPwrNumberRedundantPowerModules=_LgpPwrNumberRedundantPowerModules_Object((1,3,6,1,4,1,476,1,42,3,5,5,3),_LgpPwrNumberRedundantPowerModules_Type())
lgpPwrNumberRedundantPowerModules.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberRedundantPowerModules.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNumberRedundantPowerModules.setUnits(_H)
_LgpPwrNumberActivePowerModules_Type=Integer32
_LgpPwrNumberActivePowerModules_Object=MibScalar
lgpPwrNumberActivePowerModules=_LgpPwrNumberActivePowerModules_Object((1,3,6,1,4,1,476,1,42,3,5,5,4),_LgpPwrNumberActivePowerModules_Type())
lgpPwrNumberActivePowerModules.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberActivePowerModules.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNumberActivePowerModules.setUnits(_H)
_LgpPwrNumberPowerModuleWarnings_Type=Integer32
_LgpPwrNumberPowerModuleWarnings_Object=MibScalar
lgpPwrNumberPowerModuleWarnings=_LgpPwrNumberPowerModuleWarnings_Object((1,3,6,1,4,1,476,1,42,3,5,5,6),_LgpPwrNumberPowerModuleWarnings_Type())
lgpPwrNumberPowerModuleWarnings.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrNumberPowerModuleWarnings.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrNumberPowerModuleWarnings.setUnits(_H)
class _LgpPwrUpsInverterStandby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LgpPwrUpsInverterStandby_Type.__name__=_C
_LgpPwrUpsInverterStandby_Object=MibScalar
lgpPwrUpsInverterStandby=_LgpPwrUpsInverterStandby_Object((1,3,6,1,4,1,476,1,42,3,5,5,7),_LgpPwrUpsInverterStandby_Type())
lgpPwrUpsInverterStandby.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrUpsInverterStandby.setStatus(_A)
_LgpPwrControl_ObjectIdentity=ObjectIdentity
lgpPwrControl=_LgpPwrControl_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,6))
if mibBuilder.loadTexts:lgpPwrControl.setStatus(_A)
_LgpPwrWellKnownControlPoints_ObjectIdentity=ObjectIdentity
lgpPwrWellKnownControlPoints=_LgpPwrWellKnownControlPoints_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,6,1))
if mibBuilder.loadTexts:lgpPwrWellKnownControlPoints.setStatus(_A)
_LgpPwrLoadCircuit_ObjectIdentity=ObjectIdentity
lgpPwrLoadCircuit=_LgpPwrLoadCircuit_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,6,1,1))
if mibBuilder.loadTexts:lgpPwrLoadCircuit.setStatus(_A)
_LgpPwrLoadCircuitTable_Object=MibTable
lgpPwrLoadCircuitTable=_LgpPwrLoadCircuitTable_Object((1,3,6,1,4,1,476,1,42,3,5,6,2))
if mibBuilder.loadTexts:lgpPwrLoadCircuitTable.setStatus(_A)
_LgpPwrLoadCircuitEntry_Object=MibTableRow
lgpPwrLoadCircuitEntry=_LgpPwrLoadCircuitEntry_Object((1,3,6,1,4,1,476,1,42,3,5,6,2,1))
lgpPwrLoadCircuitEntry.setIndexNames((0,_O,_s))
if mibBuilder.loadTexts:lgpPwrLoadCircuitEntry.setStatus(_A)
_LgpPwrLoadCircuitIndex_Type=Unsigned32
_LgpPwrLoadCircuitIndex_Object=MibTableColumn
lgpPwrLoadCircuitIndex=_LgpPwrLoadCircuitIndex_Object((1,3,6,1,4,1,476,1,42,3,5,6,2,1,1),_LgpPwrLoadCircuitIndex_Type())
lgpPwrLoadCircuitIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:lgpPwrLoadCircuitIndex.setStatus(_A)
_LgpPwrLoadCircuitId_Type=ObjectIdentifier
_LgpPwrLoadCircuitId_Object=MibTableColumn
lgpPwrLoadCircuitId=_LgpPwrLoadCircuitId_Object((1,3,6,1,4,1,476,1,42,3,5,6,2,1,2),_LgpPwrLoadCircuitId_Type())
lgpPwrLoadCircuitId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLoadCircuitId.setStatus(_A)
_LgpPwrLoadCircuitSubID_Type=Unsigned32
_LgpPwrLoadCircuitSubID_Object=MibTableColumn
lgpPwrLoadCircuitSubID=_LgpPwrLoadCircuitSubID_Object((1,3,6,1,4,1,476,1,42,3,5,6,2,1,3),_LgpPwrLoadCircuitSubID_Type())
lgpPwrLoadCircuitSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrLoadCircuitSubID.setStatus(_A)
class _LgpPwrLoadCircuitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),('default',3)))
_LgpPwrLoadCircuitState_Type.__name__=_C
_LgpPwrLoadCircuitState_Object=MibTableColumn
lgpPwrLoadCircuitState=_LgpPwrLoadCircuitState_Object((1,3,6,1,4,1,476,1,42,3,5,6,2,1,4),_LgpPwrLoadCircuitState_Type())
lgpPwrLoadCircuitState.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrLoadCircuitState.setStatus(_A)
class _LgpPwrLoadCircuitStateAndControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_K,1),('reboot',2)))
_LgpPwrLoadCircuitStateAndControl_Type.__name__=_C
_LgpPwrLoadCircuitStateAndControl_Object=MibTableColumn
lgpPwrLoadCircuitStateAndControl=_LgpPwrLoadCircuitStateAndControl_Object((1,3,6,1,4,1,476,1,42,3,5,6,2,1,5),_LgpPwrLoadCircuitStateAndControl_Type())
lgpPwrLoadCircuitStateAndControl.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrLoadCircuitStateAndControl.setStatus(_A)
_LgpPwrAlarmSilence_Type=Integer32
_LgpPwrAlarmSilence_Object=MibScalar
lgpPwrAlarmSilence=_LgpPwrAlarmSilence_Object((1,3,6,1,4,1,476,1,42,3,5,6,3),_LgpPwrAlarmSilence_Type())
lgpPwrAlarmSilence.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrAlarmSilence.setStatus(_A)
class _LgpPwrBatteryTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('abort',2)))
_LgpPwrBatteryTest_Type.__name__=_C
_LgpPwrBatteryTest_Object=MibScalar
lgpPwrBatteryTest=_LgpPwrBatteryTest_Object((1,3,6,1,4,1,476,1,42,3,5,6,4),_LgpPwrBatteryTest_Type())
lgpPwrBatteryTest.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryTest.setStatus(_A)
_LgpPwrUpsAbortCommand_Type=Integer32
_LgpPwrUpsAbortCommand_Object=MibScalar
lgpPwrUpsAbortCommand=_LgpPwrUpsAbortCommand_Object((1,3,6,1,4,1,476,1,42,3,5,6,5),_LgpPwrUpsAbortCommand_Type())
lgpPwrUpsAbortCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrUpsAbortCommand.setStatus(_A)
_LgpPwrTransferToBypass_Type=Integer32
_LgpPwrTransferToBypass_Object=MibScalar
lgpPwrTransferToBypass=_LgpPwrTransferToBypass_Object((1,3,6,1,4,1,476,1,42,3,5,6,6),_LgpPwrTransferToBypass_Type())
lgpPwrTransferToBypass.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrTransferToBypass.setStatus(_A)
_LgpPwrTransferToInverter_Type=Integer32
_LgpPwrTransferToInverter_Object=MibScalar
lgpPwrTransferToInverter=_LgpPwrTransferToInverter_Object((1,3,6,1,4,1,476,1,42,3,5,6,7),_LgpPwrTransferToInverter_Type())
lgpPwrTransferToInverter.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrTransferToInverter.setStatus(_A)
_LgpPwrOutputOnDelay_Type=Integer32
_LgpPwrOutputOnDelay_Object=MibScalar
lgpPwrOutputOnDelay=_LgpPwrOutputOnDelay_Object((1,3,6,1,4,1,476,1,42,3,5,6,8),_LgpPwrOutputOnDelay_Type())
lgpPwrOutputOnDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrOutputOnDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrOutputOnDelay.setUnits(_M)
_LgpPwrOutputOffDelayWithRestart_Type=Integer32
_LgpPwrOutputOffDelayWithRestart_Object=MibScalar
lgpPwrOutputOffDelayWithRestart=_LgpPwrOutputOffDelayWithRestart_Object((1,3,6,1,4,1,476,1,42,3,5,6,9),_LgpPwrOutputOffDelayWithRestart_Type())
lgpPwrOutputOffDelayWithRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrOutputOffDelayWithRestart.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrOutputOffDelayWithRestart.setUnits(_M)
_LgpPwrOutputOffDelayWithoutRestart_Type=Integer32
_LgpPwrOutputOffDelayWithoutRestart_Object=MibScalar
lgpPwrOutputOffDelayWithoutRestart=_LgpPwrOutputOffDelayWithoutRestart_Object((1,3,6,1,4,1,476,1,42,3,5,6,10),_LgpPwrOutputOffDelayWithoutRestart_Type())
lgpPwrOutputOffDelayWithoutRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrOutputOffDelayWithoutRestart.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrOutputOffDelayWithoutRestart.setUnits(_M)
_LgpPwrTopology_ObjectIdentity=ObjectIdentity
lgpPwrTopology=_LgpPwrTopology_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,7))
if mibBuilder.loadTexts:lgpPwrTopology.setStatus(_A)
class _LgpPwrUpsTopOffline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrUpsTopOffline_Type.__name__=_C
_LgpPwrUpsTopOffline_Object=MibScalar
lgpPwrUpsTopOffline=_LgpPwrUpsTopOffline_Object((1,3,6,1,4,1,476,1,42,3,5,7,1),_LgpPwrUpsTopOffline_Type())
lgpPwrUpsTopOffline.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrUpsTopOffline.setStatus(_A)
class _LgpPwrUpsTopLineInteractive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrUpsTopLineInteractive_Type.__name__=_C
_LgpPwrUpsTopLineInteractive_Object=MibScalar
lgpPwrUpsTopLineInteractive=_LgpPwrUpsTopLineInteractive_Object((1,3,6,1,4,1,476,1,42,3,5,7,2),_LgpPwrUpsTopLineInteractive_Type())
lgpPwrUpsTopLineInteractive.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrUpsTopLineInteractive.setStatus(_A)
class _LgpPwrUPSTopDualInput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrUPSTopDualInput_Type.__name__=_C
_LgpPwrUPSTopDualInput_Object=MibScalar
lgpPwrUPSTopDualInput=_LgpPwrUPSTopDualInput_Object((1,3,6,1,4,1,476,1,42,3,5,7,3),_LgpPwrUPSTopDualInput_Type())
lgpPwrUPSTopDualInput.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrUPSTopDualInput.setStatus(_A)
class _LgpPwrTopFrequencyConverter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrTopFrequencyConverter_Type.__name__=_C
_LgpPwrTopFrequencyConverter_Object=MibScalar
lgpPwrTopFrequencyConverter=_LgpPwrTopFrequencyConverter_Object((1,3,6,1,4,1,476,1,42,3,5,7,4),_LgpPwrTopFrequencyConverter_Type())
lgpPwrTopFrequencyConverter.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrTopFrequencyConverter.setStatus(_A)
class _LgpPwrTopVoltageConverter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrTopVoltageConverter_Type.__name__=_C
_LgpPwrTopVoltageConverter_Object=MibScalar
lgpPwrTopVoltageConverter=_LgpPwrTopVoltageConverter_Object((1,3,6,1,4,1,476,1,42,3,5,7,5),_LgpPwrTopVoltageConverter_Type())
lgpPwrTopVoltageConverter.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrTopVoltageConverter.setStatus(_A)
_LgpPwrTopMaximumFrameCapacity_Type=Integer32
_LgpPwrTopMaximumFrameCapacity_Object=MibScalar
lgpPwrTopMaximumFrameCapacity=_LgpPwrTopMaximumFrameCapacity_Object((1,3,6,1,4,1,476,1,42,3,5,7,6),_LgpPwrTopMaximumFrameCapacity_Type())
lgpPwrTopMaximumFrameCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrTopMaximumFrameCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrTopMaximumFrameCapacity.setUnits(_U)
class _LgpPwrTopRedundantControlModules_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_LgpPwrTopRedundantControlModules_Type.__name__=_C
_LgpPwrTopRedundantControlModules_Object=MibScalar
lgpPwrTopRedundantControlModules=_LgpPwrTopRedundantControlModules_Object((1,3,6,1,4,1,476,1,42,3,5,7,7),_LgpPwrTopRedundantControlModules_Type())
lgpPwrTopRedundantControlModules.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrTopRedundantControlModules.setStatus(_A)
class _LgpPwrInputIsolationTransformerInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_c,2)))
_LgpPwrInputIsolationTransformerInstalled_Type.__name__=_C
_LgpPwrInputIsolationTransformerInstalled_Object=MibScalar
lgpPwrInputIsolationTransformerInstalled=_LgpPwrInputIsolationTransformerInstalled_Object((1,3,6,1,4,1,476,1,42,3,5,7,8),_LgpPwrInputIsolationTransformerInstalled_Type())
lgpPwrInputIsolationTransformerInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrInputIsolationTransformerInstalled.setStatus(_A)
class _LgpPwrStateStaticSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('continuousDuty',2),('momentaryDuty',3)))
_LgpPwrStateStaticSwitchType_Type.__name__=_C
_LgpPwrStateStaticSwitchType_Object=MibScalar
lgpPwrStateStaticSwitchType=_LgpPwrStateStaticSwitchType_Object((1,3,6,1,4,1,476,1,42,3,5,7,9),_LgpPwrStateStaticSwitchType_Type())
lgpPwrStateStaticSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateStaticSwitchType.setStatus(_A)
class _LgpPwrStateModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('singleModuleSystem',1),('module1plus1',2),('module1plusN',3),('moduleNplus1',4),('systemControlCabinet',5),('mainStaticSwitch',6)))
_LgpPwrStateModuleType_Type.__name__=_C
_LgpPwrStateModuleType_Object=MibScalar
lgpPwrStateModuleType=_LgpPwrStateModuleType_Object((1,3,6,1,4,1,476,1,42,3,5,7,10),_LgpPwrStateModuleType_Type())
lgpPwrStateModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateModuleType.setStatus(_A)
class _LgpPwrStateBypassInputConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_t,1),(_u,2),(_v,3),(_w,4),(_x,5)))
_LgpPwrStateBypassInputConfig_Type.__name__=_C
_LgpPwrStateBypassInputConfig_Object=MibScalar
lgpPwrStateBypassInputConfig=_LgpPwrStateBypassInputConfig_Object((1,3,6,1,4,1,476,1,42,3,5,7,11),_LgpPwrStateBypassInputConfig_Type())
lgpPwrStateBypassInputConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateBypassInputConfig.setStatus(_A)
class _LgpPwrStateOutputConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_t,1),(_u,2),(_v,3),(_w,4),(_x,5)))
_LgpPwrStateOutputConfig_Type.__name__=_C
_LgpPwrStateOutputConfig_Object=MibScalar
lgpPwrStateOutputConfig=_LgpPwrStateOutputConfig_Object((1,3,6,1,4,1,476,1,42,3,5,7,12),_LgpPwrStateOutputConfig_Type())
lgpPwrStateOutputConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrStateOutputConfig.setStatus(_A)
class _LgpPwrRectifierPassiveFilterInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_c,2)))
_LgpPwrRectifierPassiveFilterInstalled_Type.__name__=_C
_LgpPwrRectifierPassiveFilterInstalled_Object=MibScalar
lgpPwrRectifierPassiveFilterInstalled=_LgpPwrRectifierPassiveFilterInstalled_Object((1,3,6,1,4,1,476,1,42,3,5,7,13),_LgpPwrRectifierPassiveFilterInstalled_Type())
lgpPwrRectifierPassiveFilterInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrRectifierPassiveFilterInstalled.setStatus(_A)
class _LgpPwrRectifierTrapInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_c,2)))
_LgpPwrRectifierTrapInstalled_Type.__name__=_C
_LgpPwrRectifierTrapInstalled_Object=MibScalar
lgpPwrRectifierTrapInstalled=_LgpPwrRectifierTrapInstalled_Object((1,3,6,1,4,1,476,1,42,3,5,7,14),_LgpPwrRectifierTrapInstalled_Type())
lgpPwrRectifierTrapInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrRectifierTrapInstalled.setStatus(_A)
class _LgpPwrRectifierActiveFilterInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_c,2)))
_LgpPwrRectifierActiveFilterInstalled_Type.__name__=_C
_LgpPwrRectifierActiveFilterInstalled_Object=MibScalar
lgpPwrRectifierActiveFilterInstalled=_LgpPwrRectifierActiveFilterInstalled_Object((1,3,6,1,4,1,476,1,42,3,5,7,15),_LgpPwrRectifierActiveFilterInstalled_Type())
lgpPwrRectifierActiveFilterInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrRectifierActiveFilterInstalled.setStatus(_A)
_LgpPwrStatistic_ObjectIdentity=ObjectIdentity
lgpPwrStatistic=_LgpPwrStatistic_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,8))
if mibBuilder.loadTexts:lgpPwrStatistic.setStatus(_A)
_LgpPwrBrownOutCount_Type=Integer32
_LgpPwrBrownOutCount_Object=MibScalar
lgpPwrBrownOutCount=_LgpPwrBrownOutCount_Object((1,3,6,1,4,1,476,1,42,3,5,8,1),_LgpPwrBrownOutCount_Type())
lgpPwrBrownOutCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBrownOutCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBrownOutCount.setUnits(_H)
_LgpPwrBlackOutCount_Type=Integer32
_LgpPwrBlackOutCount_Object=MibScalar
lgpPwrBlackOutCount=_LgpPwrBlackOutCount_Object((1,3,6,1,4,1,476,1,42,3,5,8,2),_LgpPwrBlackOutCount_Type())
lgpPwrBlackOutCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBlackOutCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBlackOutCount.setUnits(_H)
_LgpPwrTransientCount_Type=Integer32
_LgpPwrTransientCount_Object=MibScalar
lgpPwrTransientCount=_LgpPwrTransientCount_Object((1,3,6,1,4,1,476,1,42,3,5,8,3),_LgpPwrTransientCount_Type())
lgpPwrTransientCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrTransientCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrTransientCount.setUnits(_H)
_LgpPwrBatteryDischargeCount_Type=Integer32
_LgpPwrBatteryDischargeCount_Object=MibScalar
lgpPwrBatteryDischargeCount=_LgpPwrBatteryDischargeCount_Object((1,3,6,1,4,1,476,1,42,3,5,8,4),_LgpPwrBatteryDischargeCount_Type())
lgpPwrBatteryDischargeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryDischargeCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryDischargeCount.setUnits(_H)
_LgpPwrBatteryDischargeTime_Type=Integer32
_LgpPwrBatteryDischargeTime_Object=MibScalar
lgpPwrBatteryDischargeTime=_LgpPwrBatteryDischargeTime_Object((1,3,6,1,4,1,476,1,42,3,5,8,5),_LgpPwrBatteryDischargeTime_Type())
lgpPwrBatteryDischargeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryDischargeTime.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryDischargeTime.setUnits(_Q)
_LgpPwrBatteryAmpHours_Type=Integer32
_LgpPwrBatteryAmpHours_Object=MibScalar
lgpPwrBatteryAmpHours=_LgpPwrBatteryAmpHours_Object((1,3,6,1,4,1,476,1,42,3,5,8,6),_LgpPwrBatteryAmpHours_Type())
lgpPwrBatteryAmpHours.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryAmpHours.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryAmpHours.setUnits(_d)
_LgpPwrBatteryWattHours_Type=Integer32
_LgpPwrBatteryWattHours_Object=MibScalar
lgpPwrBatteryWattHours=_LgpPwrBatteryWattHours_Object((1,3,6,1,4,1,476,1,42,3,5,8,7),_LgpPwrBatteryWattHours_Type())
lgpPwrBatteryWattHours.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrBatteryWattHours.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrBatteryWattHours.setUnits(_i)
_LgpPwrBatteryStatisticsReset_Type=Integer32
_LgpPwrBatteryStatisticsReset_Object=MibScalar
lgpPwrBatteryStatisticsReset=_LgpPwrBatteryStatisticsReset_Object((1,3,6,1,4,1,476,1,42,3,5,8,8),_LgpPwrBatteryStatisticsReset_Type())
lgpPwrBatteryStatisticsReset.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrBatteryStatisticsReset.setStatus(_A)
_LgpPwrStatisticsReset_Type=Integer32
_LgpPwrStatisticsReset_Object=MibScalar
lgpPwrStatisticsReset=_LgpPwrStatisticsReset_Object((1,3,6,1,4,1,476,1,42,3,5,8,9),_LgpPwrStatisticsReset_Type())
lgpPwrStatisticsReset.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrStatisticsReset.setStatus(_A)
_LgpPwrConfig_ObjectIdentity=ObjectIdentity
lgpPwrConfig=_LgpPwrConfig_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,5,9))
if mibBuilder.loadTexts:lgpPwrConfig.setStatus(_A)
_LgpPwrSysCapacity_Type=Integer32
_LgpPwrSysCapacity_Object=MibScalar
lgpPwrSysCapacity=_LgpPwrSysCapacity_Object((1,3,6,1,4,1,476,1,42,3,5,9,1),_LgpPwrSysCapacity_Type())
lgpPwrSysCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrSysCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrSysCapacity.setUnits(_U)
class _LgpPwrUPSModuleMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('single',1),('parallel',2),('hotmaster',3),('hotslave',4)))
_LgpPwrUPSModuleMode_Type.__name__=_C
_LgpPwrUPSModuleMode_Object=MibScalar
lgpPwrUPSModuleMode=_LgpPwrUPSModuleMode_Object((1,3,6,1,4,1,476,1,42,3,5,9,2),_LgpPwrUPSModuleMode_Type())
lgpPwrUPSModuleMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpPwrUPSModuleMode.setStatus(_A)
_LgpPwrMaxRatedCurrent_Type=Integer32
_LgpPwrMaxRatedCurrent_Object=MibScalar
lgpPwrMaxRatedCurrent=_LgpPwrMaxRatedCurrent_Object((1,3,6,1,4,1,476,1,42,3,5,9,3),_LgpPwrMaxRatedCurrent_Type())
lgpPwrMaxRatedCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrMaxRatedCurrent.setStatus(_A)
if mibBuilder.loadTexts:lgpPwrMaxRatedCurrent.setUnits(_V)
class _LgpPwrRectifierPulseCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sixPulse',1),('twelvePulse',2),('eighteenPulse',3),('twentyFourPulse',4)))
_LgpPwrRectifierPulseCount_Type.__name__=_C
_LgpPwrRectifierPulseCount_Object=MibScalar
lgpPwrRectifierPulseCount=_LgpPwrRectifierPulseCount_Object((1,3,6,1,4,1,476,1,42,3,5,9,4),_LgpPwrRectifierPulseCount_Type())
lgpPwrRectifierPulseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPwrRectifierPulseCount.setStatus(_A)
mibBuilder.exportSymbols(_O,**{'liebertGlobalProductsPowerModule':liebertGlobalProductsPowerModule,'lgpPwrBattery':lgpPwrBattery,'lgpPwrNumberInstalledBatteryModules':lgpPwrNumberInstalledBatteryModules,'lgpPwrNumberFailedBatteryModules':lgpPwrNumberFailedBatteryModules,'lgpPwrNumberRedundantBatteryModules':lgpPwrNumberRedundantBatteryModules,'lgpPwrNumberActiveBatteryModules':lgpPwrNumberActiveBatteryModules,'lgpPwrConfigLowBatteryWarningTime':lgpPwrConfigLowBatteryWarningTime,'lgpPwrNumberBatteryModuleWarnings':lgpPwrNumberBatteryModuleWarnings,'lgpPwrBatteryCount':lgpPwrBatteryCount,'lgpPwrBatteryTestResult':lgpPwrBatteryTestResult,'lgpPwrNominalBatteryCapacity':lgpPwrNominalBatteryCapacity,'lgpPwrBatteryFloatVoltage':lgpPwrBatteryFloatVoltage,'lgpPwrBatteryEndOfDischargeVoltage':lgpPwrBatteryEndOfDischargeVoltage,'lgpPwrAutomaticBatteryTestInterval':lgpPwrAutomaticBatteryTestInterval,'lgpPwrAutomaticBatteryTestCountdown':lgpPwrAutomaticBatteryTestCountdown,'lgpPwrBatteryChargeStatus':lgpPwrBatteryChargeStatus,'lgpPwrBatteryLifeEnhancer':lgpPwrBatteryLifeEnhancer,'lgpPwrBatteryCharger':lgpPwrBatteryCharger,'lgpPwrBatteryChargeMode':lgpPwrBatteryChargeMode,'lgpPwrBatteryTimeRemaining':lgpPwrBatteryTimeRemaining,'lgpPwrBatteryCapacity':lgpPwrBatteryCapacity,'lgpPwrBatteryCabinet':lgpPwrBatteryCabinet,'lgpPwrBatteryCabinetCount':lgpPwrBatteryCabinetCount,'lgpPwrBatteryCabinetType':lgpPwrBatteryCabinetType,'lgpPwrBatteryCabinetRatedCapacity':lgpPwrBatteryCabinetRatedCapacity,'lgpPwrBatteryLeadAcidCellCount':lgpPwrBatteryLeadAcidCellCount,'lgpPwrBatteryNiCadCellCount':lgpPwrBatteryNiCadCellCount,'lgpPwrBatteryAmpHoursConsumed':lgpPwrBatteryAmpHoursConsumed,'lgpPwrBatteryAmpHoursDischargeConsumed':lgpPwrBatteryAmpHoursDischargeConsumed,'lgpPwrBatteryLastDischargeTime':lgpPwrBatteryLastDischargeTime,'lgpPwrBatteryLastCommissionTime':lgpPwrBatteryLastCommissionTime,'lgpPwrBatteryPresentDischargeTime':lgpPwrBatteryPresentDischargeTime,'lgpPwrBatteryCapacityStatus':lgpPwrBatteryCapacityStatus,'lgpPwrBatteryCircuitBreakerState':lgpPwrBatteryCircuitBreakerState,'lgpPwrMeasurements':lgpPwrMeasurements,'lgpPwrWellKnownMeasurementPoints':lgpPwrWellKnownMeasurementPoints,'lgpPwrSource1Input':lgpPwrSource1Input,'lgpPwrSource2Input':lgpPwrSource2Input,'lgpPwrSourcePdu1Input':lgpPwrSourcePdu1Input,'lgpPwrSourcePdu2Input':lgpPwrSourcePdu2Input,'lgpPwrOutputToLoad':lgpPwrOutputToLoad,'lgpPwrMeasBattery':lgpPwrMeasBattery,'lgpPwrMeasBypass':lgpPwrMeasBypass,'lgpPwrMeasDcBus':lgpPwrMeasDcBus,'lgpPwrMeasSystemOutput':lgpPwrMeasSystemOutput,'lgpPwrMeasBatteryCabinet':lgpPwrMeasBatteryCabinet,'lgpPwrMeasurementPointTable':lgpPwrMeasurementPointTable,'lgpPwrMeasurementPointEntry':lgpPwrMeasurementPointEntry,_g:lgpPwrMeasurementPointIndex,'lgpPwrMeasurementPointId':lgpPwrMeasurementPointId,'lgpPwrMeasurementPointNumLines':lgpPwrMeasurementPointNumLines,'lgpPwrMeasurementPointNomVolts':lgpPwrMeasurementPointNomVolts,'lgpPwrMeasurementPointNomFrequency':lgpPwrMeasurementPointNomFrequency,'lgpPwrMeasurementPointFrequency':lgpPwrMeasurementPointFrequency,'lgpPwrMeasurementPointApparentPower':lgpPwrMeasurementPointApparentPower,'lgpPwrMeasurementPointTruePower':lgpPwrMeasurementPointTruePower,'lgpPwrMeasurementPointPowerFactor':lgpPwrMeasurementPointPowerFactor,'lgpPwrMeasurementPointWattHours':lgpPwrMeasurementPointWattHours,'lgpPwrMeasurementPointVAPercent':lgpPwrMeasurementPointVAPercent,'lgpPwrMeasurementPointNeutralCurrent':lgpPwrMeasurementPointNeutralCurrent,'lgpPwrMeasurementPointGroundCurrent':lgpPwrMeasurementPointGroundCurrent,'lgpPwrMeasurementPointNomCurrent':lgpPwrMeasurementPointNomCurrent,'lgpPwrMeasurementPointNomPowerFactor':lgpPwrMeasurementPointNomPowerFactor,'lgpPwrMeasurementPointNomVA':lgpPwrMeasurementPointNomVA,'lgpPwrMeasurementPointNomW':lgpPwrMeasurementPointNomW,'lgpPwrMeasurementPointPowerFactorTag':lgpPwrMeasurementPointPowerFactorTag,'lgpPwrLineMeasurementTable':lgpPwrLineMeasurementTable,'lgpPwrLineMeasurementEntry':lgpPwrLineMeasurementEntry,_m:lgpPwrMeasurementPtIndex,_n:lgpPwrLineMeasurementIndex,'lgpPwrMeasurementPoint':lgpPwrMeasurementPoint,'lgpPwrLineMeasurementVoltsLL':lgpPwrLineMeasurementVoltsLL,'lgpPwrLineMeasurementVoltsLN':lgpPwrLineMeasurementVoltsLN,'lgpPwrLineMeasurementCurrent':lgpPwrLineMeasurementCurrent,'lgpPwrLineMeasurementCapacity':lgpPwrLineMeasurementCapacity,'lgpPwrLineMeasurementVA':lgpPwrLineMeasurementVA,'lgpPwrLineMeasurementTruePower':lgpPwrLineMeasurementTruePower,'lgpPwrLineMeasurementVoltageTHD':lgpPwrLineMeasurementVoltageTHD,'lgpPwrLineMeasurementCurrentTHD':lgpPwrLineMeasurementCurrentTHD,'lgpPwrLineMeasurementKFactorCurrent':lgpPwrLineMeasurementKFactorCurrent,'lgpPwrLineMeasurementCrestFactorCurrent':lgpPwrLineMeasurementCrestFactorCurrent,'lgpPwrLineMeasurementPowerFactor':lgpPwrLineMeasurementPowerFactor,'lgpPwrLineMeasurementPowerFactorTag':lgpPwrLineMeasurementPowerFactorTag,'lgpPwrLineMeasurementMaxVolts':lgpPwrLineMeasurementMaxVolts,'lgpPwrLineMeasurementMinVolts':lgpPwrLineMeasurementMinVolts,'lgpPwrLineMeasurementVAR':lgpPwrLineMeasurementVAR,'lgpPwrLineMeasurementPercentLoad':lgpPwrLineMeasurementPercentLoad,'lgpPwrLineMeasurementVolts':lgpPwrLineMeasurementVolts,'lgpPwrLineMeasurementVACapacity':lgpPwrLineMeasurementVACapacity,'lgpPwrDcMeasurementPointTable':lgpPwrDcMeasurementPointTable,'lgpPwrDcMeasurementPointEntry':lgpPwrDcMeasurementPointEntry,_o:lgpPwrDcMeasurementPointIndex,'lgpPwrDcMeasurementPointId':lgpPwrDcMeasurementPointId,'lgpPwrDcMeasurementPointSubID':lgpPwrDcMeasurementPointSubID,'lgpPwrDcMeasurementPointVolts':lgpPwrDcMeasurementPointVolts,'lgpPwrDcMeasurementPointCurrent':lgpPwrDcMeasurementPointCurrent,'lgpPwrDcMeasurementPointNomVolts':lgpPwrDcMeasurementPointNomVolts,'lgpPwrDcMeasurementPointTruePower':lgpPwrDcMeasurementPointTruePower,'lgpPwrWellKnownMeasurementTypes':lgpPwrWellKnownMeasurementTypes,'lgpPwrVoltsAc':lgpPwrVoltsAc,'lgpPwrVoltsDc':lgpPwrVoltsDc,'lgpPwrAmpsNeutral':lgpPwrAmpsNeutral,'lgpPwrStatus':lgpPwrStatus,'lgpPwrTransferCount':lgpPwrTransferCount,'lgpPwrAutoTransferTimer':lgpPwrAutoTransferTimer,'lgpPwrAutoReTransferEnabled':lgpPwrAutoReTransferEnabled,'lgpPwrSyncPhaseAngle':lgpPwrSyncPhaseAngle,'lgpPwrParallelSystemOutputToLoadSource':lgpPwrParallelSystemOutputToLoadSource,'lgpPwrDcToDcConverter':lgpPwrDcToDcConverter,'lgpPwrOutputToLoadOnInverter':lgpPwrOutputToLoadOnInverter,'lgpPwrBatteryChargeCompensating':lgpPwrBatteryChargeCompensating,'lgpPwrInverterReady':lgpPwrInverterReady,'lgpPwrOutputToLoadOnBypass':lgpPwrOutputToLoadOnBypass,'lgpPwrBoost':lgpPwrBoost,'lgpPwrBuck':lgpPwrBuck,'lgpPwrShutdownOverTemperature':lgpPwrShutdownOverTemperature,'lgpPwrShutdownOverload':lgpPwrShutdownOverload,'lgpPwrShutdownDcBusOverload':lgpPwrShutdownDcBusOverload,'lgpPwrShutdownOutputShort':lgpPwrShutdownOutputShort,'lgpPwrShutdownLineSwap':lgpPwrShutdownLineSwap,'lgpPwrShutdownLowBattery':lgpPwrShutdownLowBattery,'lgpPwrShutdownRemote':lgpPwrShutdownRemote,'lgpPwrShutdownInputUnderVoltage':lgpPwrShutdownInputUnderVoltage,'lgpPwrShutdownPowerFactorCorrectionFailure':lgpPwrShutdownPowerFactorCorrectionFailure,'lgpPwrShutdownHardware':lgpPwrShutdownHardware,'lgpPwrRedundantSubModule':lgpPwrRedundantSubModule,'lgpPwrBypassReady':lgpPwrBypassReady,'lgpPwrGeneratorStatus':lgpPwrGeneratorStatus,'lgpPwrRotaryBreakerStatus':lgpPwrRotaryBreakerStatus,'lgpPwrPowerFactorCorrection':lgpPwrPowerFactorCorrection,'lgpPwrBypassSyncDiff':lgpPwrBypassSyncDiff,'lgpPwrBypassOverloadShutdownTime':lgpPwrBypassOverloadShutdownTime,'lgpPwrInverterOverloadShutdownTime':lgpPwrInverterOverloadShutdownTime,'lgpPwrStateOutputSource':lgpPwrStateOutputSource,'lgpPwrStateInputSource':lgpPwrStateInputSource,'lgpPwrStateInputQualification':lgpPwrStateInputQualification,'lgpPwrStateBypassStaticSwitchState':lgpPwrStateBypassStaticSwitchState,'lgpPwrStateBypassQualification':lgpPwrStateBypassQualification,'lgpPwrStateDCBusQualification':lgpPwrStateDCBusQualification,'lgpPwrStateOutQualification':lgpPwrStateOutQualification,'lgpPwrStateInverterQualification':lgpPwrStateInverterQualification,'lgpPwrStateInverterState':lgpPwrStateInverterState,'lgpPwrStateRectifierState':lgpPwrStateRectifierState,'lgpPwrStateModuleGroup':lgpPwrStateModuleGroup,'lgpPwrStateUpsModuleCount':lgpPwrStateUpsModuleCount,'lgpPwrStateUpsModuleRedundantCount':lgpPwrStateUpsModuleRedundantCount,'lgpPwrStateBackfeedBrkrState':lgpPwrStateBackfeedBrkrState,'lgpPwrStateLoadDisconnectState':lgpPwrStateLoadDisconnectState,'lgpPwrStateInputBrkrState':lgpPwrStateInputBrkrState,'lgpPwrStateTrapFilterBrkrState':lgpPwrStateTrapFilterBrkrState,'lgpPwrStateInvOutputBrkrState':lgpPwrStateInvOutputBrkrState,'lgpPwrStateIntBypassBrkrState':lgpPwrStateIntBypassBrkrState,'lgpPwrStateBypassIsolBrkrState':lgpPwrStateBypassIsolBrkrState,'lgpPwrStateRectifierIsolBrkrState':lgpPwrStateRectifierIsolBrkrState,'lgpPwrStateMaintBypassBrkrState':lgpPwrStateMaintBypassBrkrState,'lgpPwrStateMaintIsolBrkrState':lgpPwrStateMaintIsolBrkrState,'lgpPwrStateOutStaticSwState':lgpPwrStateOutStaticSwState,'lgpPwrStateModuleOutBrkrState':lgpPwrStateModuleOutBrkrState,'lgpPwrBypassReXfrRemainTime':lgpPwrBypassReXfrRemainTime,'lgpPwrStateUpsOutputSource':lgpPwrStateUpsOutputSource,'lgpPwrStateLoadBusSynchronization':lgpPwrStateLoadBusSynchronization,'lgpPwrStateCircuitBrkrStateGroup':lgpPwrStateCircuitBrkrStateGroup,'lgpPwrStateSource1InputBrkrState':lgpPwrStateSource1InputBrkrState,'lgpPwrStateSource2InputBrkrState':lgpPwrStateSource2InputBrkrState,'lgpPwrStateSource1BypassBrkrState':lgpPwrStateSource1BypassBrkrState,'lgpPwrStateSource2BypassBrkrState':lgpPwrStateSource2BypassBrkrState,'lgpPwrStateOutputBrkrState':lgpPwrStateOutputBrkrState,'lgpPwrStateAuxOutputBrkrState':lgpPwrStateAuxOutputBrkrState,'lgpPwrStateSource1PduInputBrkrState':lgpPwrStateSource1PduInputBrkrState,'lgpPwrStateSource2PduInputBrkrState':lgpPwrStateSource2PduInputBrkrState,'lgpPwrEconomicOperation':lgpPwrEconomicOperation,'lgpPwrSettings':lgpPwrSettings,'lgpPwrPreferredSource':lgpPwrPreferredSource,'lgpPwrLoadOnSource':lgpPwrLoadOnSource,'lgpPwrNominalVoltageDeviation':lgpPwrNominalVoltageDeviation,'lgpPwrNominalVoltageDeviationPercent':lgpPwrNominalVoltageDeviationPercent,'lgpPwrPhaseDifferenceLimit':lgpPwrPhaseDifferenceLimit,'lgpPwrFrequencyDeviationLimit':lgpPwrFrequencyDeviationLimit,'lgpPwrThresholdTable':lgpPwrThresholdTable,'lgpPwrThresholdEntry':lgpPwrThresholdEntry,_r:lgpPwrThresholdIndex,'lgpPwrThresholdPoint':lgpPwrThresholdPoint,'lgpPwrThresholdSubID':lgpPwrThresholdSubID,'lgpPwrThresholdType':lgpPwrThresholdType,'lgpPwrThresholdHighWarning':lgpPwrThresholdHighWarning,'lgpPwrThresholdHighFailure':lgpPwrThresholdHighFailure,'lgpPwrThresholdLowWarning':lgpPwrThresholdLowWarning,'lgpPwrThresholdLowFailure':lgpPwrThresholdLowFailure,'lgpPwrUpsAutoRestart':lgpPwrUpsAutoRestart,'lgpPwrUpsAutoRestartDelay':lgpPwrUpsAutoRestartDelay,'lgpPwrAutoRestartBatteryChargeThreshold':lgpPwrAutoRestartBatteryChargeThreshold,'lgpPwrParallelModuleCount':lgpPwrParallelModuleCount,'lgpPwrParallelRedundancyCount':lgpPwrParallelRedundancyCount,'lgpPwrLoadBusSyncMode':lgpPwrLoadBusSyncMode,'lgpPwrEconomicOperationMode':lgpPwrEconomicOperationMode,'lgpPwrAutomaticBatteryTest':lgpPwrAutomaticBatteryTest,'lgpPwrMinimumRedundantPowerModule':lgpPwrMinimumRedundantPowerModule,'lgpPwrMinimumRedundantBatteryModule':lgpPwrMinimumRedundantBatteryModule,'lgpPwrOutputToLoadUserOverloadLimit':lgpPwrOutputToLoadUserOverloadLimit,'lgpPwrNoLoadWarningLimit':lgpPwrNoLoadWarningLimit,'lgpPwrNoLoadWarningDelay':lgpPwrNoLoadWarningDelay,'lgpPwrEconomicOperationModeControl':lgpPwrEconomicOperationModeControl,'lgpPwrConversion':lgpPwrConversion,'lgpPwrNumberInstalledPowerModules':lgpPwrNumberInstalledPowerModules,'lgpPwrNumberFailedPowerModules':lgpPwrNumberFailedPowerModules,'lgpPwrNumberRedundantPowerModules':lgpPwrNumberRedundantPowerModules,'lgpPwrNumberActivePowerModules':lgpPwrNumberActivePowerModules,'lgpPwrNumberPowerModuleWarnings':lgpPwrNumberPowerModuleWarnings,'lgpPwrUpsInverterStandby':lgpPwrUpsInverterStandby,'lgpPwrControl':lgpPwrControl,'lgpPwrWellKnownControlPoints':lgpPwrWellKnownControlPoints,'lgpPwrLoadCircuit':lgpPwrLoadCircuit,'lgpPwrLoadCircuitTable':lgpPwrLoadCircuitTable,'lgpPwrLoadCircuitEntry':lgpPwrLoadCircuitEntry,_s:lgpPwrLoadCircuitIndex,'lgpPwrLoadCircuitId':lgpPwrLoadCircuitId,'lgpPwrLoadCircuitSubID':lgpPwrLoadCircuitSubID,'lgpPwrLoadCircuitState':lgpPwrLoadCircuitState,'lgpPwrLoadCircuitStateAndControl':lgpPwrLoadCircuitStateAndControl,'lgpPwrAlarmSilence':lgpPwrAlarmSilence,'lgpPwrBatteryTest':lgpPwrBatteryTest,'lgpPwrUpsAbortCommand':lgpPwrUpsAbortCommand,'lgpPwrTransferToBypass':lgpPwrTransferToBypass,'lgpPwrTransferToInverter':lgpPwrTransferToInverter,'lgpPwrOutputOnDelay':lgpPwrOutputOnDelay,'lgpPwrOutputOffDelayWithRestart':lgpPwrOutputOffDelayWithRestart,'lgpPwrOutputOffDelayWithoutRestart':lgpPwrOutputOffDelayWithoutRestart,'lgpPwrTopology':lgpPwrTopology,'lgpPwrUpsTopOffline':lgpPwrUpsTopOffline,'lgpPwrUpsTopLineInteractive':lgpPwrUpsTopLineInteractive,'lgpPwrUPSTopDualInput':lgpPwrUPSTopDualInput,'lgpPwrTopFrequencyConverter':lgpPwrTopFrequencyConverter,'lgpPwrTopVoltageConverter':lgpPwrTopVoltageConverter,'lgpPwrTopMaximumFrameCapacity':lgpPwrTopMaximumFrameCapacity,'lgpPwrTopRedundantControlModules':lgpPwrTopRedundantControlModules,'lgpPwrInputIsolationTransformerInstalled':lgpPwrInputIsolationTransformerInstalled,'lgpPwrStateStaticSwitchType':lgpPwrStateStaticSwitchType,'lgpPwrStateModuleType':lgpPwrStateModuleType,'lgpPwrStateBypassInputConfig':lgpPwrStateBypassInputConfig,'lgpPwrStateOutputConfig':lgpPwrStateOutputConfig,'lgpPwrRectifierPassiveFilterInstalled':lgpPwrRectifierPassiveFilterInstalled,'lgpPwrRectifierTrapInstalled':lgpPwrRectifierTrapInstalled,'lgpPwrRectifierActiveFilterInstalled':lgpPwrRectifierActiveFilterInstalled,'lgpPwrStatistic':lgpPwrStatistic,'lgpPwrBrownOutCount':lgpPwrBrownOutCount,'lgpPwrBlackOutCount':lgpPwrBlackOutCount,'lgpPwrTransientCount':lgpPwrTransientCount,'lgpPwrBatteryDischargeCount':lgpPwrBatteryDischargeCount,'lgpPwrBatteryDischargeTime':lgpPwrBatteryDischargeTime,'lgpPwrBatteryAmpHours':lgpPwrBatteryAmpHours,'lgpPwrBatteryWattHours':lgpPwrBatteryWattHours,'lgpPwrBatteryStatisticsReset':lgpPwrBatteryStatisticsReset,'lgpPwrStatisticsReset':lgpPwrStatisticsReset,'lgpPwrConfig':lgpPwrConfig,'lgpPwrSysCapacity':lgpPwrSysCapacity,'lgpPwrUPSModuleMode':lgpPwrUPSModuleMode,'lgpPwrMaxRatedCurrent':lgpPwrMaxRatedCurrent,'lgpPwrRectifierPulseCount':lgpPwrRectifierPulseCount})