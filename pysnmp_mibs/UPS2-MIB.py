_J='vac220'
_I='DisplayString'
_H='disable'
_G='enable'
_F='upsIndex'
_E='UPS2-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctUPS,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctUPS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
_UpsSystem_ObjectIdentity=ObjectIdentity
upsSystem=_UpsSystem_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,10,1))
class _UpsNumUPSs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_UpsNumUPSs_Type.__name__=_C
_UpsNumUPSs_Object=MibScalar
upsNumUPSs=_UpsNumUPSs_Object((1,3,6,1,4,1,52,4,1,1,10,1,1),_UpsNumUPSs_Type())
upsNumUPSs.setMaxAccess(_B)
if mibBuilder.loadTexts:upsNumUPSs.setStatus(_A)
_UpsId_ObjectIdentity=ObjectIdentity
upsId=_UpsId_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,10,2))
_UpsIdTable_Object=MibTable
upsIdTable=_UpsIdTable_Object((1,3,6,1,4,1,52,4,1,1,10,2,1))
if mibBuilder.loadTexts:upsIdTable.setStatus(_A)
_UpsIdEntry_Object=MibTableRow
upsIdEntry=_UpsIdEntry_Object((1,3,6,1,4,1,52,4,1,1,10,2,1,1))
upsIdEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:upsIdEntry.setStatus(_A)
_UpsIndex_Type=Integer32
_UpsIndex_Object=MibTableColumn
upsIndex=_UpsIndex_Object((1,3,6,1,4,1,52,4,1,1,10,2,1,1,1),_UpsIndex_Type())
upsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIndex.setStatus(_A)
class _UpsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_UpsName_Type.__name__=_I
_UpsName_Object=MibTableColumn
upsName=_UpsName_Object((1,3,6,1,4,1,52,4,1,1,10,2,1,1,2),_UpsName_Type())
upsName.setMaxAccess(_D)
if mibBuilder.loadTexts:upsName.setStatus(_A)
class _UpsModelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('smartUps250',1),('smartUps400',2),('smartUps600',3),('smartUps900',4),('smartUps1250',5),('smartUps2000',6),('matrixUps3000',7),('matrixUps5000',8),('other',9)))
_UpsModelType_Type.__name__=_C
_UpsModelType_Object=MibTableColumn
upsModelType=_UpsModelType_Object((1,3,6,1,4,1,52,4,1,1,10,2,1,1,3),_UpsModelType_Type())
upsModelType.setMaxAccess(_B)
if mibBuilder.loadTexts:upsModelType.setStatus(_A)
class _UpsFwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_UpsFwVersion_Type.__name__=_I
_UpsFwVersion_Object=MibTableColumn
upsFwVersion=_UpsFwVersion_Object((1,3,6,1,4,1,52,4,1,1,10,2,1,1,4),_UpsFwVersion_Type())
upsFwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsFwVersion.setStatus(_A)
class _UpsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_UpsSerialNumber_Type.__name__=_I
_UpsSerialNumber_Object=MibTableColumn
upsSerialNumber=_UpsSerialNumber_Object((1,3,6,1,4,1,52,4,1,1,10,2,1,1,5),_UpsSerialNumber_Type())
upsSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSerialNumber.setStatus(_A)
class _UpsManufDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_UpsManufDate_Type.__name__=_I
_UpsManufDate_Object=MibTableColumn
upsManufDate=_UpsManufDate_Object((1,3,6,1,4,1,52,4,1,1,10,2,1,1,6),_UpsManufDate_Type())
upsManufDate.setMaxAccess(_B)
if mibBuilder.loadTexts:upsManufDate.setStatus(_A)
_UpsBattery_ObjectIdentity=ObjectIdentity
upsBattery=_UpsBattery_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,10,3))
_UpsBatteryTable_Object=MibTable
upsBatteryTable=_UpsBatteryTable_Object((1,3,6,1,4,1,52,4,1,1,10,3,1))
if mibBuilder.loadTexts:upsBatteryTable.setStatus(_A)
_UpsBatteryEntry_Object=MibTableRow
upsBatteryEntry=_UpsBatteryEntry_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1))
upsBatteryEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:upsBatteryEntry.setStatus(_A)
_UpsBatteryCapacity_Type=Integer32
_UpsBatteryCapacity_Object=MibTableColumn
upsBatteryCapacity=_UpsBatteryCapacity_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1,1),_UpsBatteryCapacity_Type())
upsBatteryCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryCapacity.setStatus(_A)
_UpsBatteryVoltage_Type=Integer32
_UpsBatteryVoltage_Object=MibTableColumn
upsBatteryVoltage=_UpsBatteryVoltage_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1,2),_UpsBatteryVoltage_Type())
upsBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryVoltage.setStatus(_A)
class _UpsBatteryTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('initiateTest',1))
_UpsBatteryTest_Type.__name__=_C
_UpsBatteryTest_Object=MibTableColumn
upsBatteryTest=_UpsBatteryTest_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1,3),_UpsBatteryTest_Type())
upsBatteryTest.setMaxAccess(_D)
if mibBuilder.loadTexts:upsBatteryTest.setStatus(_A)
class _UpsBatteryTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('batteryOK',1),('batteryBad',2),('noRecentTest',3),('invalidTestDueToOverload',4)))
_UpsBatteryTestResult_Type.__name__=_C
_UpsBatteryTestResult_Object=MibTableColumn
upsBatteryTestResult=_UpsBatteryTestResult_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1,4),_UpsBatteryTestResult_Type())
upsBatteryTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryTestResult.setStatus(_A)
class _UpsRunTimeCalibration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('performTest',1),('abortTest',2),('testInProgress',3),('testNotInProgress',4)))
_UpsRunTimeCalibration_Type.__name__=_C
_UpsRunTimeCalibration_Object=MibTableColumn
upsRunTimeCalibration=_UpsRunTimeCalibration_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1,5),_UpsRunTimeCalibration_Type())
upsRunTimeCalibration.setMaxAccess(_D)
if mibBuilder.loadTexts:upsRunTimeCalibration.setStatus(_A)
_UpsEstimatedRunTimeRemaining_Type=Integer32
_UpsEstimatedRunTimeRemaining_Object=MibTableColumn
upsEstimatedRunTimeRemaining=_UpsEstimatedRunTimeRemaining_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1,6),_UpsEstimatedRunTimeRemaining_Type())
upsEstimatedRunTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEstimatedRunTimeRemaining.setStatus(_A)
class _UpsTransferCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noTransfer',1),('selfTest',2),('inputLineSpike',3),('inputLowVoltage',4),('inputHighVoltage',5),('inputLineFrequencyBad',6)))
_UpsTransferCause_Type.__name__=_C
_UpsTransferCause_Object=MibTableColumn
upsTransferCause=_UpsTransferCause_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1,7),_UpsTransferCause_Type())
upsTransferCause.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTransferCause.setStatus(_A)
class _UpsBatteryTestTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('twoWeeks',1),('oneWeek',2),('startupOnly',3),('off',4)))
_UpsBatteryTestTime_Type.__name__=_C
_UpsBatteryTestTime_Object=MibTableColumn
upsBatteryTestTime=_UpsBatteryTestTime_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1,8),_UpsBatteryTestTime_Type())
upsBatteryTestTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsBatteryTestTime.setStatus(_A)
class _UpsLowBatteryWarning_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('twoMinutes',1),('fiveMinutes',2),('sevenMinutes',3),('tenMinutes',4)))
_UpsLowBatteryWarning_Type.__name__=_C
_UpsLowBatteryWarning_Object=MibTableColumn
upsLowBatteryWarning=_UpsLowBatteryWarning_Object((1,3,6,1,4,1,52,4,1,1,10,3,1,1,9),_UpsLowBatteryWarning_Type())
upsLowBatteryWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:upsLowBatteryWarning.setStatus(_A)
_UpsInput_ObjectIdentity=ObjectIdentity
upsInput=_UpsInput_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,10,4))
_UpsInputTable_Object=MibTable
upsInputTable=_UpsInputTable_Object((1,3,6,1,4,1,52,4,1,1,10,4,1))
if mibBuilder.loadTexts:upsInputTable.setStatus(_A)
_UpsInputEntry_Object=MibTableRow
upsInputEntry=_UpsInputEntry_Object((1,3,6,1,4,1,52,4,1,1,10,4,1,1))
upsInputEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:upsInputEntry.setStatus(_A)
class _UpsInputUtilityVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vac100',1),('vac120',2),('vac208',3),(_J,4)))
_UpsInputUtilityVoltage_Type.__name__=_C
_UpsInputUtilityVoltage_Object=MibTableColumn
upsInputUtilityVoltage=_UpsInputUtilityVoltage_Object((1,3,6,1,4,1,52,4,1,1,10,4,1,1,1),_UpsInputUtilityVoltage_Type())
upsInputUtilityVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputUtilityVoltage.setStatus(_A)
_UpsInputVoltage_Type=Integer32
_UpsInputVoltage_Object=MibTableColumn
upsInputVoltage=_UpsInputVoltage_Object((1,3,6,1,4,1,52,4,1,1,10,4,1,1,2),_UpsInputVoltage_Type())
upsInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVoltage.setStatus(_A)
class _UpsInputFailureSensitivity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('high',1),('medium',2),('low',3),('auto',4)))
_UpsInputFailureSensitivity_Type.__name__=_C
_UpsInputFailureSensitivity_Object=MibTableColumn
upsInputFailureSensitivity=_UpsInputFailureSensitivity_Object((1,3,6,1,4,1,52,4,1,1,10,4,1,1,3),_UpsInputFailureSensitivity_Type())
upsInputFailureSensitivity.setMaxAccess(_D)
if mibBuilder.loadTexts:upsInputFailureSensitivity.setStatus(_A)
_UpsInputMaxVoltage_Type=Integer32
_UpsInputMaxVoltage_Object=MibTableColumn
upsInputMaxVoltage=_UpsInputMaxVoltage_Object((1,3,6,1,4,1,52,4,1,1,10,4,1,1,4),_UpsInputMaxVoltage_Type())
upsInputMaxVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputMaxVoltage.setStatus(_A)
_UpsInputMinVoltage_Type=Integer32
_UpsInputMinVoltage_Object=MibTableColumn
upsInputMinVoltage=_UpsInputMinVoltage_Object((1,3,6,1,4,1,52,4,1,1,10,4,1,1,5),_UpsInputMinVoltage_Type())
upsInputMinVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputMinVoltage.setStatus(_A)
_UpsInputFrequency_Type=Integer32
_UpsInputFrequency_Object=MibTableColumn
upsInputFrequency=_UpsInputFrequency_Object((1,3,6,1,4,1,52,4,1,1,10,4,1,1,6),_UpsInputFrequency_Type())
upsInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputFrequency.setStatus(_A)
_UpsOutput_ObjectIdentity=ObjectIdentity
upsOutput=_UpsOutput_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,10,5))
_UpsOutputTable_Object=MibTable
upsOutputTable=_UpsOutputTable_Object((1,3,6,1,4,1,52,4,1,1,10,5,1))
if mibBuilder.loadTexts:upsOutputTable.setStatus(_A)
_UpsOutputEntry_Object=MibTableRow
upsOutputEntry=_UpsOutputEntry_Object((1,3,6,1,4,1,52,4,1,1,10,5,1,1))
upsOutputEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:upsOutputEntry.setStatus(_A)
_UpsOutputVoltage_Type=Integer32
_UpsOutputVoltage_Object=MibTableColumn
upsOutputVoltage=_UpsOutputVoltage_Object((1,3,6,1,4,1,52,4,1,1,10,5,1,1,1),_UpsOutputVoltage_Type())
upsOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputVoltage.setStatus(_A)
class _UpsOutputUtilityVoltage_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vac225',1),('vac230',2),('vac240',3),(_J,4)))
_UpsOutputUtilityVoltage_Type.__name__=_C
_UpsOutputUtilityVoltage_Object=MibTableColumn
upsOutputUtilityVoltage=_UpsOutputUtilityVoltage_Object((1,3,6,1,4,1,52,4,1,1,10,5,1,1,2),_UpsOutputUtilityVoltage_Type())
upsOutputUtilityVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:upsOutputUtilityVoltage.setStatus(_A)
_UpsOutputPower_Type=Integer32
_UpsOutputPower_Object=MibTableColumn
upsOutputPower=_UpsOutputPower_Object((1,3,6,1,4,1,52,4,1,1,10,5,1,1,3),_UpsOutputPower_Type())
upsOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPower.setStatus(_A)
_UpsStatus_ObjectIdentity=ObjectIdentity
upsStatus=_UpsStatus_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,10,6))
_UpsStatusTable_Object=MibTable
upsStatusTable=_UpsStatusTable_Object((1,3,6,1,4,1,52,4,1,1,10,6,1))
if mibBuilder.loadTexts:upsStatusTable.setStatus(_A)
_UpsStatusEntry_Object=MibTableRow
upsStatusEntry=_UpsStatusEntry_Object((1,3,6,1,4,1,52,4,1,1,10,6,1,1))
upsStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:upsStatusEntry.setStatus(_A)
_UpsStatusOperational_Type=Integer32
_UpsStatusOperational_Object=MibTableColumn
upsStatusOperational=_UpsStatusOperational_Object((1,3,6,1,4,1,52,4,1,1,10,6,1,1,1),_UpsStatusOperational_Type())
upsStatusOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:upsStatusOperational.setStatus(_A)
_UpsStatusFault_Type=Integer32
_UpsStatusFault_Object=MibTableColumn
upsStatusFault=_UpsStatusFault_Object((1,3,6,1,4,1,52,4,1,1,10,6,1,1,2),_UpsStatusFault_Type())
upsStatusFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsStatusFault.setStatus(_A)
_UpsStatusTemp_Type=Integer32
_UpsStatusTemp_Object=MibTableColumn
upsStatusTemp=_UpsStatusTemp_Object((1,3,6,1,4,1,52,4,1,1,10,6,1,1,3),_UpsStatusTemp_Type())
upsStatusTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:upsStatusTemp.setStatus(_A)
_UpsConfig_ObjectIdentity=ObjectIdentity
upsConfig=_UpsConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,10,7))
_UpsConfigTable_Object=MibTable
upsConfigTable=_UpsConfigTable_Object((1,3,6,1,4,1,52,4,1,1,10,7,1))
if mibBuilder.loadTexts:upsConfigTable.setStatus(_A)
_UpsConfigEntry_Object=MibTableRow
upsConfigEntry=_UpsConfigEntry_Object((1,3,6,1,4,1,52,4,1,1,10,7,1,1))
upsConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:upsConfigEntry.setStatus(_A)
class _UpsConfigAlarm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('uponUtilityFailure',1),('thirtySecondsAfterUtilityFailure',2),('lowBatteryOnly',3),('noAudibleAlarm',4)))
_UpsConfigAlarm_Type.__name__=_C
_UpsConfigAlarm_Object=MibTableColumn
upsConfigAlarm=_UpsConfigAlarm_Object((1,3,6,1,4,1,52,4,1,1,10,7,1,1,1),_UpsConfigAlarm_Type())
upsConfigAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigAlarm.setStatus(_A)
class _UpsConfigRestoreDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restoreDefaults',1))
_UpsConfigRestoreDefaults_Type.__name__=_C
_UpsConfigRestoreDefaults_Object=MibTableColumn
upsConfigRestoreDefaults=_UpsConfigRestoreDefaults_Object((1,3,6,1,4,1,52,4,1,1,10,7,1,1,2),_UpsConfigRestoreDefaults_Type())
upsConfigRestoreDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:upsConfigRestoreDefaults.setStatus(_A)
_UpsExtMeas_ObjectIdentity=ObjectIdentity
upsExtMeas=_UpsExtMeas_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,10,8))
_UpsExtMeasTable_Object=MibTable
upsExtMeasTable=_UpsExtMeasTable_Object((1,3,6,1,4,1,52,4,1,1,10,8,1))
if mibBuilder.loadTexts:upsExtMeasTable.setStatus(_A)
_UpsExtMeasEntry_Object=MibTableRow
upsExtMeasEntry=_UpsExtMeasEntry_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1))
upsExtMeasEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:upsExtMeasEntry.setStatus(_A)
class _UpsExtMeasFwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_UpsExtMeasFwVersion_Type.__name__=_I
_UpsExtMeasFwVersion_Object=MibTableColumn
upsExtMeasFwVersion=_UpsExtMeasFwVersion_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,1),_UpsExtMeasFwVersion_Type())
upsExtMeasFwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsExtMeasFwVersion.setStatus(_A)
_UpsExtMeasTemp_Type=Integer32
_UpsExtMeasTemp_Object=MibTableColumn
upsExtMeasTemp=_UpsExtMeasTemp_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,2),_UpsExtMeasTemp_Type())
upsExtMeasTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:upsExtMeasTemp.setStatus(_A)
_UpsExtMeasHumidity_Type=Integer32
_UpsExtMeasHumidity_Object=MibTableColumn
upsExtMeasHumidity=_UpsExtMeasHumidity_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,3),_UpsExtMeasHumidity_Type())
upsExtMeasHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:upsExtMeasHumidity.setStatus(_A)
_UpsExtMeasAlarmStatus_Type=Integer32
_UpsExtMeasAlarmStatus_Object=MibTableColumn
upsExtMeasAlarmStatus=_UpsExtMeasAlarmStatus_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,4),_UpsExtMeasAlarmStatus_Type())
upsExtMeasAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsExtMeasAlarmStatus.setStatus(_A)
class _UpsExtMeasMaxTemp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ninetyDegreesF',1),('oneHundredFifteenDegreesF',2),('oneHundredThirtyDegreesF',3),('oneHundredSeventyFiveDegreesF',4)))
_UpsExtMeasMaxTemp_Type.__name__=_C
_UpsExtMeasMaxTemp_Object=MibTableColumn
upsExtMeasMaxTemp=_UpsExtMeasMaxTemp_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,5),_UpsExtMeasMaxTemp_Type())
upsExtMeasMaxTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasMaxTemp.setStatus(_A)
class _UpsExtMeasMinTemp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fortyDegreesF',1),('fiftyDegreesF',2),('fiftyEightDegreesF',3),('sixtyFiveDegreesF',4)))
_UpsExtMeasMinTemp_Type.__name__=_C
_UpsExtMeasMinTemp_Object=MibTableColumn
upsExtMeasMinTemp=_UpsExtMeasMinTemp_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,6),_UpsExtMeasMinTemp_Type())
upsExtMeasMinTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasMinTemp.setStatus(_A)
class _UpsExtMeasMaxHumidity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('seventyPercent',1),('eightyPercent',2),('eightyFivePercent',3),('ninetyPercent',4)))
_UpsExtMeasMaxHumidity_Type.__name__=_C
_UpsExtMeasMaxHumidity_Object=MibTableColumn
upsExtMeasMaxHumidity=_UpsExtMeasMaxHumidity_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,7),_UpsExtMeasMaxHumidity_Type())
upsExtMeasMaxHumidity.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasMaxHumidity.setStatus(_A)
class _UpsExtMeasMinHumidity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tenPercent',1),('twentyPercent',2),('thirtyPercent',3),('fortyPercent',4)))
_UpsExtMeasMinHumidity_Type.__name__=_C
_UpsExtMeasMinHumidity_Object=MibTableColumn
upsExtMeasMinHumidity=_UpsExtMeasMinHumidity_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,8),_UpsExtMeasMinHumidity_Type())
upsExtMeasMinHumidity.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasMinHumidity.setStatus(_A)
class _UpsExtMeasContact1AlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsExtMeasContact1AlarmControl_Type.__name__=_C
_UpsExtMeasContact1AlarmControl_Object=MibTableColumn
upsExtMeasContact1AlarmControl=_UpsExtMeasContact1AlarmControl_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,9),_UpsExtMeasContact1AlarmControl_Type())
upsExtMeasContact1AlarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasContact1AlarmControl.setStatus(_A)
class _UpsExtMeasContact2AlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsExtMeasContact2AlarmControl_Type.__name__=_C
_UpsExtMeasContact2AlarmControl_Object=MibTableColumn
upsExtMeasContact2AlarmControl=_UpsExtMeasContact2AlarmControl_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,10),_UpsExtMeasContact2AlarmControl_Type())
upsExtMeasContact2AlarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasContact2AlarmControl.setStatus(_A)
class _UpsExtMeasContact3AlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsExtMeasContact3AlarmControl_Type.__name__=_C
_UpsExtMeasContact3AlarmControl_Object=MibTableColumn
upsExtMeasContact3AlarmControl=_UpsExtMeasContact3AlarmControl_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,11),_UpsExtMeasContact3AlarmControl_Type())
upsExtMeasContact3AlarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasContact3AlarmControl.setStatus(_A)
class _UpsExtMeasContact4AlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsExtMeasContact4AlarmControl_Type.__name__=_C
_UpsExtMeasContact4AlarmControl_Object=MibTableColumn
upsExtMeasContact4AlarmControl=_UpsExtMeasContact4AlarmControl_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,12),_UpsExtMeasContact4AlarmControl_Type())
upsExtMeasContact4AlarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasContact4AlarmControl.setStatus(_A)
class _UpsExtMeasMaxTempAlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsExtMeasMaxTempAlarmControl_Type.__name__=_C
_UpsExtMeasMaxTempAlarmControl_Object=MibTableColumn
upsExtMeasMaxTempAlarmControl=_UpsExtMeasMaxTempAlarmControl_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,13),_UpsExtMeasMaxTempAlarmControl_Type())
upsExtMeasMaxTempAlarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasMaxTempAlarmControl.setStatus(_A)
class _UpsExtMeasMinTempAlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsExtMeasMinTempAlarmControl_Type.__name__=_C
_UpsExtMeasMinTempAlarmControl_Object=MibTableColumn
upsExtMeasMinTempAlarmControl=_UpsExtMeasMinTempAlarmControl_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,14),_UpsExtMeasMinTempAlarmControl_Type())
upsExtMeasMinTempAlarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasMinTempAlarmControl.setStatus(_A)
class _UpsExtMeasMaxHumidityAlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsExtMeasMaxHumidityAlarmControl_Type.__name__=_C
_UpsExtMeasMaxHumidityAlarmControl_Object=MibTableColumn
upsExtMeasMaxHumidityAlarmControl=_UpsExtMeasMaxHumidityAlarmControl_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,15),_UpsExtMeasMaxHumidityAlarmControl_Type())
upsExtMeasMaxHumidityAlarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasMaxHumidityAlarmControl.setStatus(_A)
class _UpsExtMeasMinHumidityAlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsExtMeasMinHumidityAlarmControl_Type.__name__=_C
_UpsExtMeasMinHumidityAlarmControl_Object=MibTableColumn
upsExtMeasMinHumidityAlarmControl=_UpsExtMeasMinHumidityAlarmControl_Object((1,3,6,1,4,1,52,4,1,1,10,8,1,1,16),_UpsExtMeasMinHumidityAlarmControl_Type())
upsExtMeasMinHumidityAlarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsExtMeasMinHumidityAlarmControl.setStatus(_A)
_UpsAddlFuncs_ObjectIdentity=ObjectIdentity
upsAddlFuncs=_UpsAddlFuncs_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,10,9))
_UpsAddlFuncsTable_Object=MibTable
upsAddlFuncsTable=_UpsAddlFuncsTable_Object((1,3,6,1,4,1,52,4,1,1,10,9,1))
if mibBuilder.loadTexts:upsAddlFuncsTable.setStatus(_A)
_UpsAddlFuncsEntry_Object=MibTableRow
upsAddlFuncsEntry=_UpsAddlFuncsEntry_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1))
upsAddlFuncsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:upsAddlFuncsEntry.setStatus(_A)
_UpsAddlFuncsNumBatteryPacks_Type=Integer32
_UpsAddlFuncsNumBatteryPacks_Object=MibTableColumn
upsAddlFuncsNumBatteryPacks=_UpsAddlFuncsNumBatteryPacks_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1,1),_UpsAddlFuncsNumBatteryPacks_Type())
upsAddlFuncsNumBatteryPacks.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAddlFuncsNumBatteryPacks.setStatus(_A)
_UpsAddlFuncsNumBadBatteryPacks_Type=Integer32
_UpsAddlFuncsNumBadBatteryPacks_Object=MibTableColumn
upsAddlFuncsNumBadBatteryPacks=_UpsAddlFuncsNumBadBatteryPacks_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1,2),_UpsAddlFuncsNumBadBatteryPacks_Type())
upsAddlFuncsNumBadBatteryPacks.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAddlFuncsNumBadBatteryPacks.setStatus(_A)
_UpsAddlFuncsOutputCurrent_Type=Integer32
_UpsAddlFuncsOutputCurrent_Object=MibTableColumn
upsAddlFuncsOutputCurrent=_UpsAddlFuncsOutputCurrent_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1,3),_UpsAddlFuncsOutputCurrent_Type())
upsAddlFuncsOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAddlFuncsOutputCurrent.setStatus(_A)
_UpsAddlFuncsOutputApparentPower_Type=Integer32
_UpsAddlFuncsOutputApparentPower_Object=MibTableColumn
upsAddlFuncsOutputApparentPower=_UpsAddlFuncsOutputApparentPower_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1,4),_UpsAddlFuncsOutputApparentPower_Type())
upsAddlFuncsOutputApparentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAddlFuncsOutputApparentPower.setStatus(_A)
_UpsAddlFuncsStatusOperational_Type=Integer32
_UpsAddlFuncsStatusOperational_Object=MibTableColumn
upsAddlFuncsStatusOperational=_UpsAddlFuncsStatusOperational_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1,5),_UpsAddlFuncsStatusOperational_Type())
upsAddlFuncsStatusOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAddlFuncsStatusOperational.setStatus(_A)
_UpsAddlFuncsStatusFault_Type=Integer32
_UpsAddlFuncsStatusFault_Object=MibTableColumn
upsAddlFuncsStatusFault=_UpsAddlFuncsStatusFault_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1,6),_UpsAddlFuncsStatusFault_Type())
upsAddlFuncsStatusFault.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAddlFuncsStatusFault.setStatus(_A)
_UpsAddlFuncsConfigPassword_Type=OctetString
_UpsAddlFuncsConfigPassword_Object=MibTableColumn
upsAddlFuncsConfigPassword=_UpsAddlFuncsConfigPassword_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1,7),_UpsAddlFuncsConfigPassword_Type())
upsAddlFuncsConfigPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAddlFuncsConfigPassword.setStatus(_A)
class _UpsAddlFuncsConfigDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('disableUps',1))
_UpsAddlFuncsConfigDisable_Type.__name__=_C
_UpsAddlFuncsConfigDisable_Object=MibTableColumn
upsAddlFuncsConfigDisable=_UpsAddlFuncsConfigDisable_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1,8),_UpsAddlFuncsConfigDisable_Type())
upsAddlFuncsConfigDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAddlFuncsConfigDisable.setStatus(_A)
class _UpsAddlFuncsConfigBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bypassMode',1),('exitBypassMode',2)))
_UpsAddlFuncsConfigBypass_Type.__name__=_C
_UpsAddlFuncsConfigBypass_Object=MibTableColumn
upsAddlFuncsConfigBypass=_UpsAddlFuncsConfigBypass_Object((1,3,6,1,4,1,52,4,1,1,10,9,1,1,9),_UpsAddlFuncsConfigBypass_Type())
upsAddlFuncsConfigBypass.setMaxAccess(_D)
if mibBuilder.loadTexts:upsAddlFuncsConfigBypass.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'upsSystem':upsSystem,'upsNumUPSs':upsNumUPSs,'upsId':upsId,'upsIdTable':upsIdTable,'upsIdEntry':upsIdEntry,_F:upsIndex,'upsName':upsName,'upsModelType':upsModelType,'upsFwVersion':upsFwVersion,'upsSerialNumber':upsSerialNumber,'upsManufDate':upsManufDate,'upsBattery':upsBattery,'upsBatteryTable':upsBatteryTable,'upsBatteryEntry':upsBatteryEntry,'upsBatteryCapacity':upsBatteryCapacity,'upsBatteryVoltage':upsBatteryVoltage,'upsBatteryTest':upsBatteryTest,'upsBatteryTestResult':upsBatteryTestResult,'upsRunTimeCalibration':upsRunTimeCalibration,'upsEstimatedRunTimeRemaining':upsEstimatedRunTimeRemaining,'upsTransferCause':upsTransferCause,'upsBatteryTestTime':upsBatteryTestTime,'upsLowBatteryWarning':upsLowBatteryWarning,'upsInput':upsInput,'upsInputTable':upsInputTable,'upsInputEntry':upsInputEntry,'upsInputUtilityVoltage':upsInputUtilityVoltage,'upsInputVoltage':upsInputVoltage,'upsInputFailureSensitivity':upsInputFailureSensitivity,'upsInputMaxVoltage':upsInputMaxVoltage,'upsInputMinVoltage':upsInputMinVoltage,'upsInputFrequency':upsInputFrequency,'upsOutput':upsOutput,'upsOutputTable':upsOutputTable,'upsOutputEntry':upsOutputEntry,'upsOutputVoltage':upsOutputVoltage,'upsOutputUtilityVoltage':upsOutputUtilityVoltage,'upsOutputPower':upsOutputPower,'upsStatus':upsStatus,'upsStatusTable':upsStatusTable,'upsStatusEntry':upsStatusEntry,'upsStatusOperational':upsStatusOperational,'upsStatusFault':upsStatusFault,'upsStatusTemp':upsStatusTemp,'upsConfig':upsConfig,'upsConfigTable':upsConfigTable,'upsConfigEntry':upsConfigEntry,'upsConfigAlarm':upsConfigAlarm,'upsConfigRestoreDefaults':upsConfigRestoreDefaults,'upsExtMeas':upsExtMeas,'upsExtMeasTable':upsExtMeasTable,'upsExtMeasEntry':upsExtMeasEntry,'upsExtMeasFwVersion':upsExtMeasFwVersion,'upsExtMeasTemp':upsExtMeasTemp,'upsExtMeasHumidity':upsExtMeasHumidity,'upsExtMeasAlarmStatus':upsExtMeasAlarmStatus,'upsExtMeasMaxTemp':upsExtMeasMaxTemp,'upsExtMeasMinTemp':upsExtMeasMinTemp,'upsExtMeasMaxHumidity':upsExtMeasMaxHumidity,'upsExtMeasMinHumidity':upsExtMeasMinHumidity,'upsExtMeasContact1AlarmControl':upsExtMeasContact1AlarmControl,'upsExtMeasContact2AlarmControl':upsExtMeasContact2AlarmControl,'upsExtMeasContact3AlarmControl':upsExtMeasContact3AlarmControl,'upsExtMeasContact4AlarmControl':upsExtMeasContact4AlarmControl,'upsExtMeasMaxTempAlarmControl':upsExtMeasMaxTempAlarmControl,'upsExtMeasMinTempAlarmControl':upsExtMeasMinTempAlarmControl,'upsExtMeasMaxHumidityAlarmControl':upsExtMeasMaxHumidityAlarmControl,'upsExtMeasMinHumidityAlarmControl':upsExtMeasMinHumidityAlarmControl,'upsAddlFuncs':upsAddlFuncs,'upsAddlFuncsTable':upsAddlFuncsTable,'upsAddlFuncsEntry':upsAddlFuncsEntry,'upsAddlFuncsNumBatteryPacks':upsAddlFuncsNumBatteryPacks,'upsAddlFuncsNumBadBatteryPacks':upsAddlFuncsNumBadBatteryPacks,'upsAddlFuncsOutputCurrent':upsAddlFuncsOutputCurrent,'upsAddlFuncsOutputApparentPower':upsAddlFuncsOutputApparentPower,'upsAddlFuncsStatusOperational':upsAddlFuncsStatusOperational,'upsAddlFuncsStatusFault':upsAddlFuncsStatusFault,'upsAddlFuncsConfigPassword':upsAddlFuncsConfigPassword,'upsAddlFuncsConfigDisable':upsAddlFuncsConfigDisable,'upsAddlFuncsConfigBypass':upsAddlFuncsConfigBypass})