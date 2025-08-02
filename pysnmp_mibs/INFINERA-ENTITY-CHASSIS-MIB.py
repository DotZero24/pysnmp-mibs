_A9='chassisGroup'
_A8='chassisTTLCurrentDays'
_A7='chassisTTLMax'
_A6='chassisOutletTemperature'
_A5='chassisPluggablePromSerialNumber'
_A4='chassisHasPluggableEeprom'
_A3='chassisInletTemperatureOffset'
_A2='chassisPmHistStatsEnable'
_A1='chassisBaffleType'
_A0='chassisPowerSupplyType'
_z='chassisFruInsertionDate'
_y='chassisAcliSessionAdminState'
_x='chassisSerialPortCLIAccess'
_w='chassisUnreachableFromManagement'
_v='chassisAcceptableEquipmentTypeList'
_u='chassisHolderState'
_t='chassisHolderType'
_s='chassisPON'
_r='chassisPartNumber'
_q='chassisManufacturedDate'
_p='chassisHardwareVersion'
_o='chassisCLEI'
_n='chassisRebootTime'
_m='chassisPduCktBreakerRating'
_l='chassisSkewBudget'
_k='chassisConfiguredAmbientTemp'
_j='chassisOperatingTemperatureThreshold'
_i='chassisActvTimingSource'
_h='chassisMaxAvailablePower'
_g='chassisSwitchingMode'
_f='chassisIsNCChassis'
_e='chassisRowStatus'
_d='chassisConfiguredPemRating'
_c='chassiscurrentInstalledPowerDraw'
_b='chassisPowerControl'
_a='chassisScmMigrationInProgress'
_Z='chassisScmMigrationAllowed'
_Y='chassisEqptMaxPowerDraw'
_X='chassisCurrentEstimatedPowerDraw'
_W='chassisConfiguredMaxPowerDraw'
_V='chassisBayLevelSummaryAlarmReporting'
_U='chassisAcoState'
_T='chassisInletTemperature'
_S='chassisSwitchCapabilityMode'
_R='chassisRUlocationInRack'
_Q='chassisRackName'
_P='chassisInstalledSerialNumber'
_O='chassisProvSerialNumber'
_N='chassisInstalledChassisType'
_M='chassisProvChassisType'
_L='chassisMoId'
_K='unknown'
_J='entLPPhysicalIndex'
_I='ENTITY-MIB'
_H='enabled'
_G='disabled'
_F='read-write'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='INFINERA-ENTITY-CHASSIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_I,_J)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatArbitraryPrecision,FloatHundredths,FloatTenths,FloatThousandths,InfnChassisSwitchingMode,InfnChassisType,InfnEnableDisable,InfnPmHistStatsControl=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths','FloatTenths','FloatThousandths','InfnChassisSwitchingMode','InfnChassisType','InfnEnableDisable','InfnPmHistStatsControl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
chassisMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,13))
_ChassisTable_Object=MibTable
chassisTable=_ChassisTable_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1))
if mibBuilder.loadTexts:chassisTable.setStatus(_A)
_ChassisEntry_Object=MibTableRow
chassisEntry=_ChassisEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1))
chassisEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:chassisEntry.setStatus(_A)
_ChassisMoId_Type=DisplayString
_ChassisMoId_Object=MibTableColumn
chassisMoId=_ChassisMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,1),_ChassisMoId_Type())
chassisMoId.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisMoId.setStatus(_A)
_ChassisProvChassisType_Type=InfnChassisType
_ChassisProvChassisType_Object=MibTableColumn
chassisProvChassisType=_ChassisProvChassisType_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,2),_ChassisProvChassisType_Type())
chassisProvChassisType.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisProvChassisType.setStatus(_A)
_ChassisInstalledChassisType_Type=InfnChassisType
_ChassisInstalledChassisType_Object=MibTableColumn
chassisInstalledChassisType=_ChassisInstalledChassisType_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,3),_ChassisInstalledChassisType_Type())
chassisInstalledChassisType.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisInstalledChassisType.setStatus(_A)
_ChassisProvSerialNumber_Type=DisplayString
_ChassisProvSerialNumber_Object=MibTableColumn
chassisProvSerialNumber=_ChassisProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,4),_ChassisProvSerialNumber_Type())
chassisProvSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisProvSerialNumber.setStatus(_A)
_ChassisInstalledSerialNumber_Type=DisplayString
_ChassisInstalledSerialNumber_Object=MibTableColumn
chassisInstalledSerialNumber=_ChassisInstalledSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,5),_ChassisInstalledSerialNumber_Type())
chassisInstalledSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisInstalledSerialNumber.setStatus(_A)
_ChassisRackName_Type=DisplayString
_ChassisRackName_Object=MibTableColumn
chassisRackName=_ChassisRackName_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,6),_ChassisRackName_Type())
chassisRackName.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisRackName.setStatus(_A)
_ChassisRUlocationInRack_Type=Unsigned32
_ChassisRUlocationInRack_Object=MibTableColumn
chassisRUlocationInRack=_ChassisRUlocationInRack_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,7),_ChassisRUlocationInRack_Type())
chassisRUlocationInRack.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisRUlocationInRack.setStatus(_A)
class _ChassisSwitchCapabilityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ring',1),('mesh',2)))
_ChassisSwitchCapabilityMode_Type.__name__=_E
_ChassisSwitchCapabilityMode_Object=MibTableColumn
chassisSwitchCapabilityMode=_ChassisSwitchCapabilityMode_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,8),_ChassisSwitchCapabilityMode_Type())
chassisSwitchCapabilityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisSwitchCapabilityMode.setStatus(_A)
_ChassisInletTemperature_Type=FloatArbitraryPrecision
_ChassisInletTemperature_Object=MibTableColumn
chassisInletTemperature=_ChassisInletTemperature_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,9),_ChassisInletTemperature_Type())
chassisInletTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisInletTemperature.setStatus(_A)
class _ChassisAcoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ChassisAcoState_Type.__name__=_E
_ChassisAcoState_Object=MibTableColumn
chassisAcoState=_ChassisAcoState_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,10),_ChassisAcoState_Type())
chassisAcoState.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisAcoState.setStatus(_A)
class _ChassisBayLevelSummaryAlarmReporting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ChassisBayLevelSummaryAlarmReporting_Type.__name__=_E
_ChassisBayLevelSummaryAlarmReporting_Object=MibTableColumn
chassisBayLevelSummaryAlarmReporting=_ChassisBayLevelSummaryAlarmReporting_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,11),_ChassisBayLevelSummaryAlarmReporting_Type())
chassisBayLevelSummaryAlarmReporting.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisBayLevelSummaryAlarmReporting.setStatus(_A)
_ChassisConfiguredMaxPowerDraw_Type=FloatThousandths
_ChassisConfiguredMaxPowerDraw_Object=MibTableColumn
chassisConfiguredMaxPowerDraw=_ChassisConfiguredMaxPowerDraw_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,12),_ChassisConfiguredMaxPowerDraw_Type())
chassisConfiguredMaxPowerDraw.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisConfiguredMaxPowerDraw.setStatus(_A)
_ChassisCurrentEstimatedPowerDraw_Type=FloatThousandths
_ChassisCurrentEstimatedPowerDraw_Object=MibTableColumn
chassisCurrentEstimatedPowerDraw=_ChassisCurrentEstimatedPowerDraw_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,13),_ChassisCurrentEstimatedPowerDraw_Type())
chassisCurrentEstimatedPowerDraw.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisCurrentEstimatedPowerDraw.setStatus(_A)
_ChassisEqptMaxPowerDraw_Type=FloatHundredths
_ChassisEqptMaxPowerDraw_Object=MibTableColumn
chassisEqptMaxPowerDraw=_ChassisEqptMaxPowerDraw_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,14),_ChassisEqptMaxPowerDraw_Type())
chassisEqptMaxPowerDraw.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisEqptMaxPowerDraw.setStatus(_A)
_ChassisScmMigrationAllowed_Type=TruthValue
_ChassisScmMigrationAllowed_Object=MibTableColumn
chassisScmMigrationAllowed=_ChassisScmMigrationAllowed_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,15),_ChassisScmMigrationAllowed_Type())
chassisScmMigrationAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisScmMigrationAllowed.setStatus(_A)
_ChassisScmMigrationInProgress_Type=TruthValue
_ChassisScmMigrationInProgress_Object=MibTableColumn
chassisScmMigrationInProgress=_ChassisScmMigrationInProgress_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,16),_ChassisScmMigrationInProgress_Type())
chassisScmMigrationInProgress.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisScmMigrationInProgress.setStatus(_A)
class _ChassisPowerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ChassisPowerControl_Type.__name__=_E
_ChassisPowerControl_Object=MibTableColumn
chassisPowerControl=_ChassisPowerControl_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,17),_ChassisPowerControl_Type())
chassisPowerControl.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPowerControl.setStatus(_A)
_ChassiscurrentInstalledPowerDraw_Type=FloatThousandths
_ChassiscurrentInstalledPowerDraw_Object=MibTableColumn
chassiscurrentInstalledPowerDraw=_ChassiscurrentInstalledPowerDraw_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,18),_ChassiscurrentInstalledPowerDraw_Type())
chassiscurrentInstalledPowerDraw.setMaxAccess(_C)
if mibBuilder.loadTexts:chassiscurrentInstalledPowerDraw.setStatus(_A)
_ChassisConfiguredPemRating_Type=Unsigned32
_ChassisConfiguredPemRating_Object=MibTableColumn
chassisConfiguredPemRating=_ChassisConfiguredPemRating_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,19),_ChassisConfiguredPemRating_Type())
chassisConfiguredPemRating.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisConfiguredPemRating.setStatus(_A)
_ChassisRowStatus_Type=RowStatus
_ChassisRowStatus_Object=MibTableColumn
chassisRowStatus=_ChassisRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,20),_ChassisRowStatus_Type())
chassisRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisRowStatus.setStatus(_A)
_ChassisIsNCChassis_Type=TruthValue
_ChassisIsNCChassis_Object=MibTableColumn
chassisIsNCChassis=_ChassisIsNCChassis_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,21),_ChassisIsNCChassis_Type())
chassisIsNCChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisIsNCChassis.setStatus(_A)
_ChassisSwitchingMode_Type=InfnChassisSwitchingMode
_ChassisSwitchingMode_Object=MibTableColumn
chassisSwitchingMode=_ChassisSwitchingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,22),_ChassisSwitchingMode_Type())
chassisSwitchingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisSwitchingMode.setStatus(_A)
_ChassisMaxAvailablePower_Type=FloatThousandths
_ChassisMaxAvailablePower_Object=MibTableColumn
chassisMaxAvailablePower=_ChassisMaxAvailablePower_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,23),_ChassisMaxAvailablePower_Type())
chassisMaxAvailablePower.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisMaxAvailablePower.setStatus(_A)
_ChassisActvTimingSource_Type=DisplayString
_ChassisActvTimingSource_Object=MibTableColumn
chassisActvTimingSource=_ChassisActvTimingSource_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,24),_ChassisActvTimingSource_Type())
chassisActvTimingSource.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisActvTimingSource.setStatus(_A)
_ChassisOperatingTemperatureThreshold_Type=Integer32
_ChassisOperatingTemperatureThreshold_Object=MibTableColumn
chassisOperatingTemperatureThreshold=_ChassisOperatingTemperatureThreshold_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,25),_ChassisOperatingTemperatureThreshold_Type())
chassisOperatingTemperatureThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:chassisOperatingTemperatureThreshold.setStatus(_A)
_ChassisConfiguredAmbientTemp_Type=Unsigned32
_ChassisConfiguredAmbientTemp_Object=MibTableColumn
chassisConfiguredAmbientTemp=_ChassisConfiguredAmbientTemp_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,26),_ChassisConfiguredAmbientTemp_Type())
chassisConfiguredAmbientTemp.setMaxAccess(_F)
if mibBuilder.loadTexts:chassisConfiguredAmbientTemp.setStatus(_A)
class _ChassisSkewBudget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('low',2),('high',3)))
_ChassisSkewBudget_Type.__name__=_E
_ChassisSkewBudget_Object=MibTableColumn
chassisSkewBudget=_ChassisSkewBudget_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,27),_ChassisSkewBudget_Type())
chassisSkewBudget.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisSkewBudget.setStatus(_A)
_ChassisPduCktBreakerRating_Type=FloatArbitraryPrecision
_ChassisPduCktBreakerRating_Object=MibTableColumn
chassisPduCktBreakerRating=_ChassisPduCktBreakerRating_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,28),_ChassisPduCktBreakerRating_Type())
chassisPduCktBreakerRating.setMaxAccess(_F)
if mibBuilder.loadTexts:chassisPduCktBreakerRating.setStatus(_A)
_ChassisRebootTime_Type=Integer32
_ChassisRebootTime_Object=MibTableColumn
chassisRebootTime=_ChassisRebootTime_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,29),_ChassisRebootTime_Type())
chassisRebootTime.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisRebootTime.setStatus(_A)
_ChassisCLEI_Type=DisplayString
_ChassisCLEI_Object=MibTableColumn
chassisCLEI=_ChassisCLEI_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,30),_ChassisCLEI_Type())
chassisCLEI.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisCLEI.setStatus(_A)
_ChassisHardwareVersion_Type=DisplayString
_ChassisHardwareVersion_Object=MibTableColumn
chassisHardwareVersion=_ChassisHardwareVersion_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,31),_ChassisHardwareVersion_Type())
chassisHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisHardwareVersion.setStatus(_A)
_ChassisManufacturedDate_Type=DisplayString
_ChassisManufacturedDate_Object=MibTableColumn
chassisManufacturedDate=_ChassisManufacturedDate_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,32),_ChassisManufacturedDate_Type())
chassisManufacturedDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisManufacturedDate.setStatus(_A)
_ChassisPartNumber_Type=DisplayString
_ChassisPartNumber_Object=MibTableColumn
chassisPartNumber=_ChassisPartNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,33),_ChassisPartNumber_Type())
chassisPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPartNumber.setStatus(_A)
_ChassisPON_Type=DisplayString
_ChassisPON_Object=MibTableColumn
chassisPON=_ChassisPON_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,34),_ChassisPON_Type())
chassisPON.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPON.setStatus(_A)
class _ChassisHolderType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('chassis',1),('self',2),('slot',3),('subSlot',4),(_K,5)))
_ChassisHolderType_Type.__name__=_E
_ChassisHolderType_Object=MibTableColumn
chassisHolderType=_ChassisHolderType_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,35),_ChassisHolderType_Type())
chassisHolderType.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisHolderType.setStatus(_A)
class _ChassisHolderState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('empty',1),('plugIn',2),('installed',3),('installedAndExpected',4),('mismatchOfInstalledAndExpected',5),(_K,6)))
_ChassisHolderState_Type.__name__=_E
_ChassisHolderState_Object=MibTableColumn
chassisHolderState=_ChassisHolderState_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,36),_ChassisHolderState_Type())
chassisHolderState.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisHolderState.setStatus(_A)
_ChassisAcceptableEquipmentTypeList_Type=DisplayString
_ChassisAcceptableEquipmentTypeList_Object=MibTableColumn
chassisAcceptableEquipmentTypeList=_ChassisAcceptableEquipmentTypeList_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,37),_ChassisAcceptableEquipmentTypeList_Type())
chassisAcceptableEquipmentTypeList.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisAcceptableEquipmentTypeList.setStatus(_A)
_ChassisUnreachableFromManagement_Type=TruthValue
_ChassisUnreachableFromManagement_Object=MibTableColumn
chassisUnreachableFromManagement=_ChassisUnreachableFromManagement_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,38),_ChassisUnreachableFromManagement_Type())
chassisUnreachableFromManagement.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisUnreachableFromManagement.setStatus(_A)
_ChassisSerialPortCLIAccess_Type=InfnEnableDisable
_ChassisSerialPortCLIAccess_Object=MibTableColumn
chassisSerialPortCLIAccess=_ChassisSerialPortCLIAccess_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,39),_ChassisSerialPortCLIAccess_Type())
chassisSerialPortCLIAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:chassisSerialPortCLIAccess.setStatus(_A)
_ChassisAcliSessionAdminState_Type=InfnEnableDisable
_ChassisAcliSessionAdminState_Object=MibTableColumn
chassisAcliSessionAdminState=_ChassisAcliSessionAdminState_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,40),_ChassisAcliSessionAdminState_Type())
chassisAcliSessionAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:chassisAcliSessionAdminState.setStatus(_A)
_ChassisFruInsertionDate_Type=DisplayString
_ChassisFruInsertionDate_Object=MibTableColumn
chassisFruInsertionDate=_ChassisFruInsertionDate_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,41),_ChassisFruInsertionDate_Type())
chassisFruInsertionDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisFruInsertionDate.setStatus(_A)
class _ChassisPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('native',1),('unmanaged3rdparty',2)))
_ChassisPowerSupplyType_Type.__name__=_E
_ChassisPowerSupplyType_Object=MibTableColumn
chassisPowerSupplyType=_ChassisPowerSupplyType_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,42),_ChassisPowerSupplyType_Type())
chassisPowerSupplyType.setMaxAccess(_F)
if mibBuilder.loadTexts:chassisPowerSupplyType.setStatus(_A)
class _ChassisBaffleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('mtc9AirBaffle',2),('mtc9AirBaffle2',3)))
_ChassisBaffleType_Type.__name__=_E
_ChassisBaffleType_Object=MibTableColumn
chassisBaffleType=_ChassisBaffleType_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,43),_ChassisBaffleType_Type())
chassisBaffleType.setMaxAccess(_F)
if mibBuilder.loadTexts:chassisBaffleType.setStatus(_A)
_ChassisPmHistStatsEnable_Type=InfnPmHistStatsControl
_ChassisPmHistStatsEnable_Object=MibTableColumn
chassisPmHistStatsEnable=_ChassisPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,44),_ChassisPmHistStatsEnable_Type())
chassisPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPmHistStatsEnable.setStatus(_A)
_ChassisInletTemperatureOffset_Type=FloatTenths
_ChassisInletTemperatureOffset_Object=MibTableColumn
chassisInletTemperatureOffset=_ChassisInletTemperatureOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,45),_ChassisInletTemperatureOffset_Type())
chassisInletTemperatureOffset.setMaxAccess(_F)
if mibBuilder.loadTexts:chassisInletTemperatureOffset.setStatus(_A)
_ChassisHasPluggableEeprom_Type=TruthValue
_ChassisHasPluggableEeprom_Object=MibTableColumn
chassisHasPluggableEeprom=_ChassisHasPluggableEeprom_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,46),_ChassisHasPluggableEeprom_Type())
chassisHasPluggableEeprom.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisHasPluggableEeprom.setStatus(_A)
_ChassisPluggablePromSerialNumber_Type=DisplayString
_ChassisPluggablePromSerialNumber_Object=MibTableColumn
chassisPluggablePromSerialNumber=_ChassisPluggablePromSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,47),_ChassisPluggablePromSerialNumber_Type())
chassisPluggablePromSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPluggablePromSerialNumber.setStatus(_A)
_ChassisOutletTemperature_Type=FloatArbitraryPrecision
_ChassisOutletTemperature_Object=MibTableColumn
chassisOutletTemperature=_ChassisOutletTemperature_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,48),_ChassisOutletTemperature_Type())
chassisOutletTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisOutletTemperature.setStatus(_A)
_ChassisTTLMax_Type=Integer32
_ChassisTTLMax_Object=MibTableColumn
chassisTTLMax=_ChassisTTLMax_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,49),_ChassisTTLMax_Type())
chassisTTLMax.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisTTLMax.setStatus(_A)
_ChassisTTLCurrentDays_Type=Integer32
_ChassisTTLCurrentDays_Object=MibTableColumn
chassisTTLCurrentDays=_ChassisTTLCurrentDays_Object((1,3,6,1,4,1,21296,2,2,2,1,13,1,1,50),_ChassisTTLCurrentDays_Type())
chassisTTLCurrentDays.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisTTLCurrentDays.setStatus(_A)
_ChassisConformance_ObjectIdentity=ObjectIdentity
chassisConformance=_ChassisConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,13,3))
_ChassisCompliances_ObjectIdentity=ObjectIdentity
chassisCompliances=_ChassisCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,13,3,1))
_ChassisGroups_ObjectIdentity=ObjectIdentity
chassisGroups=_ChassisGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,13,3,2))
chassisGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,13,3,2,1))
chassisGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:chassisGroup.setStatus(_A)
chassisCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,13,3,1,1))
chassisCompliance.setObjects((_B,_A9))
if mibBuilder.loadTexts:chassisCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'chassisMIB':chassisMIB,'chassisTable':chassisTable,'chassisEntry':chassisEntry,_L:chassisMoId,_M:chassisProvChassisType,_N:chassisInstalledChassisType,_O:chassisProvSerialNumber,_P:chassisInstalledSerialNumber,_Q:chassisRackName,_R:chassisRUlocationInRack,_S:chassisSwitchCapabilityMode,_T:chassisInletTemperature,_U:chassisAcoState,_V:chassisBayLevelSummaryAlarmReporting,_W:chassisConfiguredMaxPowerDraw,_X:chassisCurrentEstimatedPowerDraw,_Y:chassisEqptMaxPowerDraw,_Z:chassisScmMigrationAllowed,_a:chassisScmMigrationInProgress,_b:chassisPowerControl,_c:chassiscurrentInstalledPowerDraw,_d:chassisConfiguredPemRating,_e:chassisRowStatus,_f:chassisIsNCChassis,_g:chassisSwitchingMode,_h:chassisMaxAvailablePower,_i:chassisActvTimingSource,_j:chassisOperatingTemperatureThreshold,_k:chassisConfiguredAmbientTemp,_l:chassisSkewBudget,_m:chassisPduCktBreakerRating,_n:chassisRebootTime,_o:chassisCLEI,_p:chassisHardwareVersion,_q:chassisManufacturedDate,_r:chassisPartNumber,_s:chassisPON,_t:chassisHolderType,_u:chassisHolderState,_v:chassisAcceptableEquipmentTypeList,_w:chassisUnreachableFromManagement,_x:chassisSerialPortCLIAccess,_y:chassisAcliSessionAdminState,_z:chassisFruInsertionDate,_A0:chassisPowerSupplyType,_A1:chassisBaffleType,_A2:chassisPmHistStatsEnable,_A3:chassisInletTemperatureOffset,_A4:chassisHasPluggableEeprom,_A5:chassisPluggablePromSerialNumber,_A6:chassisOutletTemperature,_A7:chassisTTLMax,_A8:chassisTTLCurrentDays,'chassisConformance':chassisConformance,'chassisCompliances':chassisCompliances,'chassisCompliance':chassisCompliance,'chassisGroups':chassisGroups,_A9:chassisGroup})