_v='rectifierGroup'
_u='rectMaxRectifierAmbientTemperature'
_t='rectNumberOfRectifiersInBootloader'
_s='rectNumberOfFanFailRectifiers'
_r='rectNumberOfRectifiersInCurrentLimit'
_q='rectNumberOfRectifiersInPowerLimit'
_p='rectNumberOfRectifiersWithConfigError'
_o='rectNumberOfACFailedRectifiers'
_n='rectNumberOfCommsNormalRectifiers'
_m='rectNumberOfCommsLostRectifiers'
_l='rectNumberOfMinorAlertRectifiers'
_k='rectNumberOfFailedRectifiers'
_j='rectNumberOfSourcingRectifiers'
_i='rectNumberOfAcquiredRectifiers'
_h='rectSysEstimatedBatteryHealthPercent'
_g='rectSysEstimatedBatteryRuntime'
_f='rectSysEstimatedSOCPercent'
_e='rectSysEstimatedCapacityRemainingPower'
_d='rectSysEstimatedCapacityRemainingCurrent'
_c='rectSysModulesInStandby'
_b='rectSysModulesSupplyingPower'
_a='rectSysPowerAveragePower'
_Z='rectSysEstimatedStandbyCapacityInAmps'
_Y='rectSysEstimatedStandbyCapacityInWatts'
_X='rectSysEstimatedRedundantCapacityInAmps'
_W='rectSysEstimatedRedundantCapacityInWatts'
_V='rectSysEstimatedAvailableCapacityInAmps'
_U='rectSysEstimatedAvailableCapacityInWatts'
_T='rectSysEstimatedRequiredCapacityInAmps'
_S='rectSysEstimatedRequiredCapacityInWatts'
_R='rectSysSystemNumber'
_Q='rectSysBatteryTemperature'
_P='rectSysBatteryCurrent'
_O='rectSysBatteryVoltage'
_N='rectSysTotalLoadCurrent'
_M='rectSysSystemVoltage'
_L='rectSysAveragePhase3Voltage'
_K='rectSysAveragePhase2Voltage'
_J='rectSysAveragePhase1Voltage'
_I='rectSysAverageRectifierACInputVoltage'
_H='rectSysAverageRectifierOutputVoltage'
_G='rectSysTotalCapacityInstalledPower'
_F='rectSysTotalCapacityInstalledAmps'
_E='rectSysTotalOutputPower'
_D='rectSysTotalOutputCurrent'
_C='read-only'
_B='ALPHA-RECTIFIER-SYS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ScaledNumber,simple=mibBuilder.importSymbols('ALPHA-RESOURCE-MIB','ScaledNumber','simple')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rectifierSystem=ModuleIdentity((1,3,6,1,4,1,7309,5,3,1))
if mibBuilder.loadTexts:rectifierSystem.setRevisions(('2019-12-12 00:00','2017-04-06 00:00','2015-07-28 00:00','2015-07-23 00:00','2015-06-23 00:00'))
_RectSysTotalOutputCurrent_Type=ScaledNumber
_RectSysTotalOutputCurrent_Object=MibScalar
rectSysTotalOutputCurrent=_RectSysTotalOutputCurrent_Object((1,3,6,1,4,1,7309,5,3,1,1),_RectSysTotalOutputCurrent_Type())
rectSysTotalOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysTotalOutputCurrent.setStatus(_A)
_RectSysTotalOutputPower_Type=ScaledNumber
_RectSysTotalOutputPower_Object=MibScalar
rectSysTotalOutputPower=_RectSysTotalOutputPower_Object((1,3,6,1,4,1,7309,5,3,1,2),_RectSysTotalOutputPower_Type())
rectSysTotalOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysTotalOutputPower.setStatus(_A)
_RectSysTotalCapacityInstalledAmps_Type=ScaledNumber
_RectSysTotalCapacityInstalledAmps_Object=MibScalar
rectSysTotalCapacityInstalledAmps=_RectSysTotalCapacityInstalledAmps_Object((1,3,6,1,4,1,7309,5,3,1,3),_RectSysTotalCapacityInstalledAmps_Type())
rectSysTotalCapacityInstalledAmps.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysTotalCapacityInstalledAmps.setStatus(_A)
_RectSysTotalCapacityInstalledPower_Type=ScaledNumber
_RectSysTotalCapacityInstalledPower_Object=MibScalar
rectSysTotalCapacityInstalledPower=_RectSysTotalCapacityInstalledPower_Object((1,3,6,1,4,1,7309,5,3,1,4),_RectSysTotalCapacityInstalledPower_Type())
rectSysTotalCapacityInstalledPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysTotalCapacityInstalledPower.setStatus(_A)
_RectSysAverageRectifierOutputVoltage_Type=ScaledNumber
_RectSysAverageRectifierOutputVoltage_Object=MibScalar
rectSysAverageRectifierOutputVoltage=_RectSysAverageRectifierOutputVoltage_Object((1,3,6,1,4,1,7309,5,3,1,5),_RectSysAverageRectifierOutputVoltage_Type())
rectSysAverageRectifierOutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysAverageRectifierOutputVoltage.setStatus(_A)
_RectSysAverageRectifierACInputVoltage_Type=ScaledNumber
_RectSysAverageRectifierACInputVoltage_Object=MibScalar
rectSysAverageRectifierACInputVoltage=_RectSysAverageRectifierACInputVoltage_Object((1,3,6,1,4,1,7309,5,3,1,6),_RectSysAverageRectifierACInputVoltage_Type())
rectSysAverageRectifierACInputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysAverageRectifierACInputVoltage.setStatus(_A)
_RectSysAveragePhase1Voltage_Type=ScaledNumber
_RectSysAveragePhase1Voltage_Object=MibScalar
rectSysAveragePhase1Voltage=_RectSysAveragePhase1Voltage_Object((1,3,6,1,4,1,7309,5,3,1,7),_RectSysAveragePhase1Voltage_Type())
rectSysAveragePhase1Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysAveragePhase1Voltage.setStatus(_A)
_RectSysAveragePhase2Voltage_Type=ScaledNumber
_RectSysAveragePhase2Voltage_Object=MibScalar
rectSysAveragePhase2Voltage=_RectSysAveragePhase2Voltage_Object((1,3,6,1,4,1,7309,5,3,1,8),_RectSysAveragePhase2Voltage_Type())
rectSysAveragePhase2Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysAveragePhase2Voltage.setStatus(_A)
_RectSysAveragePhase3Voltage_Type=ScaledNumber
_RectSysAveragePhase3Voltage_Object=MibScalar
rectSysAveragePhase3Voltage=_RectSysAveragePhase3Voltage_Object((1,3,6,1,4,1,7309,5,3,1,9),_RectSysAveragePhase3Voltage_Type())
rectSysAveragePhase3Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysAveragePhase3Voltage.setStatus(_A)
_RectSysSystemVoltage_Type=ScaledNumber
_RectSysSystemVoltage_Object=MibScalar
rectSysSystemVoltage=_RectSysSystemVoltage_Object((1,3,6,1,4,1,7309,5,3,1,10),_RectSysSystemVoltage_Type())
rectSysSystemVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysSystemVoltage.setStatus(_A)
_RectSysTotalLoadCurrent_Type=ScaledNumber
_RectSysTotalLoadCurrent_Object=MibScalar
rectSysTotalLoadCurrent=_RectSysTotalLoadCurrent_Object((1,3,6,1,4,1,7309,5,3,1,11),_RectSysTotalLoadCurrent_Type())
rectSysTotalLoadCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysTotalLoadCurrent.setStatus(_A)
_RectSysBatteryVoltage_Type=ScaledNumber
_RectSysBatteryVoltage_Object=MibScalar
rectSysBatteryVoltage=_RectSysBatteryVoltage_Object((1,3,6,1,4,1,7309,5,3,1,12),_RectSysBatteryVoltage_Type())
rectSysBatteryVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysBatteryVoltage.setStatus(_A)
_RectSysBatteryCurrent_Type=ScaledNumber
_RectSysBatteryCurrent_Object=MibScalar
rectSysBatteryCurrent=_RectSysBatteryCurrent_Object((1,3,6,1,4,1,7309,5,3,1,13),_RectSysBatteryCurrent_Type())
rectSysBatteryCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysBatteryCurrent.setStatus(_A)
_RectSysBatteryTemperature_Type=ScaledNumber
_RectSysBatteryTemperature_Object=MibScalar
rectSysBatteryTemperature=_RectSysBatteryTemperature_Object((1,3,6,1,4,1,7309,5,3,1,14),_RectSysBatteryTemperature_Type())
rectSysBatteryTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysBatteryTemperature.setStatus(_A)
_RectSysSystemNumber_Type=ScaledNumber
_RectSysSystemNumber_Object=MibScalar
rectSysSystemNumber=_RectSysSystemNumber_Object((1,3,6,1,4,1,7309,5,3,1,15),_RectSysSystemNumber_Type())
rectSysSystemNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysSystemNumber.setStatus(_A)
_RectSysEstimatedRequiredCapacityInWatts_Type=ScaledNumber
_RectSysEstimatedRequiredCapacityInWatts_Object=MibScalar
rectSysEstimatedRequiredCapacityInWatts=_RectSysEstimatedRequiredCapacityInWatts_Object((1,3,6,1,4,1,7309,5,3,1,16),_RectSysEstimatedRequiredCapacityInWatts_Type())
rectSysEstimatedRequiredCapacityInWatts.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedRequiredCapacityInWatts.setStatus(_A)
_RectSysEstimatedRequiredCapacityInAmps_Type=ScaledNumber
_RectSysEstimatedRequiredCapacityInAmps_Object=MibScalar
rectSysEstimatedRequiredCapacityInAmps=_RectSysEstimatedRequiredCapacityInAmps_Object((1,3,6,1,4,1,7309,5,3,1,17),_RectSysEstimatedRequiredCapacityInAmps_Type())
rectSysEstimatedRequiredCapacityInAmps.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedRequiredCapacityInAmps.setStatus(_A)
_RectSysEstimatedAvailableCapacityInWatts_Type=ScaledNumber
_RectSysEstimatedAvailableCapacityInWatts_Object=MibScalar
rectSysEstimatedAvailableCapacityInWatts=_RectSysEstimatedAvailableCapacityInWatts_Object((1,3,6,1,4,1,7309,5,3,1,18),_RectSysEstimatedAvailableCapacityInWatts_Type())
rectSysEstimatedAvailableCapacityInWatts.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedAvailableCapacityInWatts.setStatus(_A)
_RectSysEstimatedAvailableCapacityInAmps_Type=ScaledNumber
_RectSysEstimatedAvailableCapacityInAmps_Object=MibScalar
rectSysEstimatedAvailableCapacityInAmps=_RectSysEstimatedAvailableCapacityInAmps_Object((1,3,6,1,4,1,7309,5,3,1,19),_RectSysEstimatedAvailableCapacityInAmps_Type())
rectSysEstimatedAvailableCapacityInAmps.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedAvailableCapacityInAmps.setStatus(_A)
_RectSysEstimatedRedundantCapacityInWatts_Type=ScaledNumber
_RectSysEstimatedRedundantCapacityInWatts_Object=MibScalar
rectSysEstimatedRedundantCapacityInWatts=_RectSysEstimatedRedundantCapacityInWatts_Object((1,3,6,1,4,1,7309,5,3,1,20),_RectSysEstimatedRedundantCapacityInWatts_Type())
rectSysEstimatedRedundantCapacityInWatts.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedRedundantCapacityInWatts.setStatus(_A)
_RectSysEstimatedRedundantCapacityInAmps_Type=ScaledNumber
_RectSysEstimatedRedundantCapacityInAmps_Object=MibScalar
rectSysEstimatedRedundantCapacityInAmps=_RectSysEstimatedRedundantCapacityInAmps_Object((1,3,6,1,4,1,7309,5,3,1,21),_RectSysEstimatedRedundantCapacityInAmps_Type())
rectSysEstimatedRedundantCapacityInAmps.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedRedundantCapacityInAmps.setStatus(_A)
_RectSysEstimatedStandbyCapacityInWatts_Type=ScaledNumber
_RectSysEstimatedStandbyCapacityInWatts_Object=MibScalar
rectSysEstimatedStandbyCapacityInWatts=_RectSysEstimatedStandbyCapacityInWatts_Object((1,3,6,1,4,1,7309,5,3,1,22),_RectSysEstimatedStandbyCapacityInWatts_Type())
rectSysEstimatedStandbyCapacityInWatts.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedStandbyCapacityInWatts.setStatus(_A)
_RectSysEstimatedStandbyCapacityInAmps_Type=ScaledNumber
_RectSysEstimatedStandbyCapacityInAmps_Object=MibScalar
rectSysEstimatedStandbyCapacityInAmps=_RectSysEstimatedStandbyCapacityInAmps_Object((1,3,6,1,4,1,7309,5,3,1,23),_RectSysEstimatedStandbyCapacityInAmps_Type())
rectSysEstimatedStandbyCapacityInAmps.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedStandbyCapacityInAmps.setStatus(_A)
_RectSysPowerAveragePower_Type=ScaledNumber
_RectSysPowerAveragePower_Object=MibScalar
rectSysPowerAveragePower=_RectSysPowerAveragePower_Object((1,3,6,1,4,1,7309,5,3,1,24),_RectSysPowerAveragePower_Type())
rectSysPowerAveragePower.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysPowerAveragePower.setStatus(_A)
_RectSysModulesSupplyingPower_Type=ScaledNumber
_RectSysModulesSupplyingPower_Object=MibScalar
rectSysModulesSupplyingPower=_RectSysModulesSupplyingPower_Object((1,3,6,1,4,1,7309,5,3,1,25),_RectSysModulesSupplyingPower_Type())
rectSysModulesSupplyingPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysModulesSupplyingPower.setStatus(_A)
_RectSysModulesInStandby_Type=ScaledNumber
_RectSysModulesInStandby_Object=MibScalar
rectSysModulesInStandby=_RectSysModulesInStandby_Object((1,3,6,1,4,1,7309,5,3,1,26),_RectSysModulesInStandby_Type())
rectSysModulesInStandby.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysModulesInStandby.setStatus(_A)
_RectSysEstimatedCapacityRemainingCurrent_Type=ScaledNumber
_RectSysEstimatedCapacityRemainingCurrent_Object=MibScalar
rectSysEstimatedCapacityRemainingCurrent=_RectSysEstimatedCapacityRemainingCurrent_Object((1,3,6,1,4,1,7309,5,3,1,28),_RectSysEstimatedCapacityRemainingCurrent_Type())
rectSysEstimatedCapacityRemainingCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedCapacityRemainingCurrent.setStatus(_A)
_RectSysEstimatedCapacityRemainingPower_Type=ScaledNumber
_RectSysEstimatedCapacityRemainingPower_Object=MibScalar
rectSysEstimatedCapacityRemainingPower=_RectSysEstimatedCapacityRemainingPower_Object((1,3,6,1,4,1,7309,5,3,1,29),_RectSysEstimatedCapacityRemainingPower_Type())
rectSysEstimatedCapacityRemainingPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedCapacityRemainingPower.setStatus(_A)
_RectSysEstimatedSOCPercent_Type=ScaledNumber
_RectSysEstimatedSOCPercent_Object=MibScalar
rectSysEstimatedSOCPercent=_RectSysEstimatedSOCPercent_Object((1,3,6,1,4,1,7309,5,3,1,30),_RectSysEstimatedSOCPercent_Type())
rectSysEstimatedSOCPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedSOCPercent.setStatus(_A)
_RectSysEstimatedBatteryRuntime_Type=ScaledNumber
_RectSysEstimatedBatteryRuntime_Object=MibScalar
rectSysEstimatedBatteryRuntime=_RectSysEstimatedBatteryRuntime_Object((1,3,6,1,4,1,7309,5,3,1,31),_RectSysEstimatedBatteryRuntime_Type())
rectSysEstimatedBatteryRuntime.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedBatteryRuntime.setStatus(_A)
_RectSysEstimatedBatteryHealthPercent_Type=ScaledNumber
_RectSysEstimatedBatteryHealthPercent_Object=MibScalar
rectSysEstimatedBatteryHealthPercent=_RectSysEstimatedBatteryHealthPercent_Object((1,3,6,1,4,1,7309,5,3,1,32),_RectSysEstimatedBatteryHealthPercent_Type())
rectSysEstimatedBatteryHealthPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectSysEstimatedBatteryHealthPercent.setStatus(_A)
_RectNumberOfAcquiredRectifiers_Type=ScaledNumber
_RectNumberOfAcquiredRectifiers_Object=MibScalar
rectNumberOfAcquiredRectifiers=_RectNumberOfAcquiredRectifiers_Object((1,3,6,1,4,1,7309,5,3,1,33),_RectNumberOfAcquiredRectifiers_Type())
rectNumberOfAcquiredRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfAcquiredRectifiers.setStatus(_A)
_RectNumberOfSourcingRectifiers_Type=ScaledNumber
_RectNumberOfSourcingRectifiers_Object=MibScalar
rectNumberOfSourcingRectifiers=_RectNumberOfSourcingRectifiers_Object((1,3,6,1,4,1,7309,5,3,1,34),_RectNumberOfSourcingRectifiers_Type())
rectNumberOfSourcingRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfSourcingRectifiers.setStatus(_A)
_RectNumberOfFailedRectifiers_Type=ScaledNumber
_RectNumberOfFailedRectifiers_Object=MibScalar
rectNumberOfFailedRectifiers=_RectNumberOfFailedRectifiers_Object((1,3,6,1,4,1,7309,5,3,1,35),_RectNumberOfFailedRectifiers_Type())
rectNumberOfFailedRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfFailedRectifiers.setStatus(_A)
_RectNumberOfMinorAlertRectifiers_Type=ScaledNumber
_RectNumberOfMinorAlertRectifiers_Object=MibScalar
rectNumberOfMinorAlertRectifiers=_RectNumberOfMinorAlertRectifiers_Object((1,3,6,1,4,1,7309,5,3,1,36),_RectNumberOfMinorAlertRectifiers_Type())
rectNumberOfMinorAlertRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfMinorAlertRectifiers.setStatus(_A)
_RectNumberOfCommsLostRectifiers_Type=ScaledNumber
_RectNumberOfCommsLostRectifiers_Object=MibScalar
rectNumberOfCommsLostRectifiers=_RectNumberOfCommsLostRectifiers_Object((1,3,6,1,4,1,7309,5,3,1,37),_RectNumberOfCommsLostRectifiers_Type())
rectNumberOfCommsLostRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfCommsLostRectifiers.setStatus(_A)
_RectNumberOfCommsNormalRectifiers_Type=ScaledNumber
_RectNumberOfCommsNormalRectifiers_Object=MibScalar
rectNumberOfCommsNormalRectifiers=_RectNumberOfCommsNormalRectifiers_Object((1,3,6,1,4,1,7309,5,3,1,38),_RectNumberOfCommsNormalRectifiers_Type())
rectNumberOfCommsNormalRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfCommsNormalRectifiers.setStatus(_A)
_RectNumberOfACFailedRectifiers_Type=ScaledNumber
_RectNumberOfACFailedRectifiers_Object=MibScalar
rectNumberOfACFailedRectifiers=_RectNumberOfACFailedRectifiers_Object((1,3,6,1,4,1,7309,5,3,1,39),_RectNumberOfACFailedRectifiers_Type())
rectNumberOfACFailedRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfACFailedRectifiers.setStatus(_A)
_RectNumberOfRectifiersWithConfigError_Type=ScaledNumber
_RectNumberOfRectifiersWithConfigError_Object=MibScalar
rectNumberOfRectifiersWithConfigError=_RectNumberOfRectifiersWithConfigError_Object((1,3,6,1,4,1,7309,5,3,1,40),_RectNumberOfRectifiersWithConfigError_Type())
rectNumberOfRectifiersWithConfigError.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfRectifiersWithConfigError.setStatus(_A)
_RectNumberOfRectifiersInPowerLimit_Type=ScaledNumber
_RectNumberOfRectifiersInPowerLimit_Object=MibScalar
rectNumberOfRectifiersInPowerLimit=_RectNumberOfRectifiersInPowerLimit_Object((1,3,6,1,4,1,7309,5,3,1,41),_RectNumberOfRectifiersInPowerLimit_Type())
rectNumberOfRectifiersInPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfRectifiersInPowerLimit.setStatus(_A)
_RectNumberOfRectifiersInCurrentLimit_Type=ScaledNumber
_RectNumberOfRectifiersInCurrentLimit_Object=MibScalar
rectNumberOfRectifiersInCurrentLimit=_RectNumberOfRectifiersInCurrentLimit_Object((1,3,6,1,4,1,7309,5,3,1,42),_RectNumberOfRectifiersInCurrentLimit_Type())
rectNumberOfRectifiersInCurrentLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfRectifiersInCurrentLimit.setStatus(_A)
_RectNumberOfFanFailRectifiers_Type=ScaledNumber
_RectNumberOfFanFailRectifiers_Object=MibScalar
rectNumberOfFanFailRectifiers=_RectNumberOfFanFailRectifiers_Object((1,3,6,1,4,1,7309,5,3,1,43),_RectNumberOfFanFailRectifiers_Type())
rectNumberOfFanFailRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfFanFailRectifiers.setStatus(_A)
_RectNumberOfRectifiersInBootloader_Type=ScaledNumber
_RectNumberOfRectifiersInBootloader_Object=MibScalar
rectNumberOfRectifiersInBootloader=_RectNumberOfRectifiersInBootloader_Object((1,3,6,1,4,1,7309,5,3,1,44),_RectNumberOfRectifiersInBootloader_Type())
rectNumberOfRectifiersInBootloader.setMaxAccess(_C)
if mibBuilder.loadTexts:rectNumberOfRectifiersInBootloader.setStatus(_A)
_RectMaxRectifierAmbientTemperature_Type=ScaledNumber
_RectMaxRectifierAmbientTemperature_Object=MibScalar
rectMaxRectifierAmbientTemperature=_RectMaxRectifierAmbientTemperature_Object((1,3,6,1,4,1,7309,5,3,1,45),_RectMaxRectifierAmbientTemperature_Type())
rectMaxRectifierAmbientTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:rectMaxRectifierAmbientTemperature.setStatus(_A)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,7309,5,3,1,100))
_Compliances_ObjectIdentity=ObjectIdentity
compliances=_Compliances_ObjectIdentity((1,3,6,1,4,1,7309,5,3,1,100,1))
_RectifierGroups_ObjectIdentity=ObjectIdentity
rectifierGroups=_RectifierGroups_ObjectIdentity((1,3,6,1,4,1,7309,5,3,1,100,2))
rectifierGroup=ObjectGroup((1,3,6,1,4,1,7309,5,3,1,100,2,1))
rectifierGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:rectifierGroup.setStatus(_A)
compliance=ModuleCompliance((1,3,6,1,4,1,7309,5,3,1,100,1,1))
compliance.setObjects((_B,_v))
if mibBuilder.loadTexts:compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rectifierSystem':rectifierSystem,_D:rectSysTotalOutputCurrent,_E:rectSysTotalOutputPower,_F:rectSysTotalCapacityInstalledAmps,_G:rectSysTotalCapacityInstalledPower,_H:rectSysAverageRectifierOutputVoltage,_I:rectSysAverageRectifierACInputVoltage,_J:rectSysAveragePhase1Voltage,_K:rectSysAveragePhase2Voltage,_L:rectSysAveragePhase3Voltage,_M:rectSysSystemVoltage,_N:rectSysTotalLoadCurrent,_O:rectSysBatteryVoltage,_P:rectSysBatteryCurrent,_Q:rectSysBatteryTemperature,_R:rectSysSystemNumber,_S:rectSysEstimatedRequiredCapacityInWatts,_T:rectSysEstimatedRequiredCapacityInAmps,_U:rectSysEstimatedAvailableCapacityInWatts,_V:rectSysEstimatedAvailableCapacityInAmps,_W:rectSysEstimatedRedundantCapacityInWatts,_X:rectSysEstimatedRedundantCapacityInAmps,_Y:rectSysEstimatedStandbyCapacityInWatts,_Z:rectSysEstimatedStandbyCapacityInAmps,_a:rectSysPowerAveragePower,_b:rectSysModulesSupplyingPower,_c:rectSysModulesInStandby,_d:rectSysEstimatedCapacityRemainingCurrent,_e:rectSysEstimatedCapacityRemainingPower,_f:rectSysEstimatedSOCPercent,_g:rectSysEstimatedBatteryRuntime,_h:rectSysEstimatedBatteryHealthPercent,_i:rectNumberOfAcquiredRectifiers,_j:rectNumberOfSourcingRectifiers,_k:rectNumberOfFailedRectifiers,_l:rectNumberOfMinorAlertRectifiers,_m:rectNumberOfCommsLostRectifiers,_n:rectNumberOfCommsNormalRectifiers,_o:rectNumberOfACFailedRectifiers,_p:rectNumberOfRectifiersWithConfigError,_q:rectNumberOfRectifiersInPowerLimit,_r:rectNumberOfRectifiersInCurrentLimit,_s:rectNumberOfFanFailRectifiers,_t:rectNumberOfRectifiersInBootloader,_u:rectMaxRectifierAmbientTemperature,'conformance':conformance,'compliances':compliances,'compliance':compliance,'rectifierGroups':rectifierGroups,_v:rectifierGroup})