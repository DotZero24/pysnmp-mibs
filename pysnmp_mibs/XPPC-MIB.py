_O='trapsIndex'
_N='invalidTest'
_M='upsSmartControlTurnOnUpsLoad'
_L='indexOfDevice'
_K='NotificationType'
_J='XPPC-MIB'
_I='unknown'
_H='abnormal'
_G='normal'
_F='yes'
_E='no'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Ppc_ObjectIdentity=ObjectIdentity
ppc=_Ppc_ObjectIdentity((1,3,6,1,4,1,935))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,935,1))
_Hardware_ObjectIdentity=ObjectIdentity
hardware=_Hardware_ObjectIdentity((1,3,6,1,4,1,935,1,1))
_Ups_ObjectIdentity=ObjectIdentity
ups=_Ups_ObjectIdentity((1,3,6,1,4,1,935,1,1,1))
_UpsIdentp_ObjectIdentity=ObjectIdentity
upsIdentp=_UpsIdentp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,1))
_UpsBaseIdent_ObjectIdentity=ObjectIdentity
upsBaseIdent=_UpsBaseIdent_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,1,1))
_UpsBaseIdentModel_Type=DisplayString
_UpsBaseIdentModel_Object=MibScalar
upsBaseIdentModel=_UpsBaseIdentModel_Object((1,3,6,1,4,1,935,1,1,1,1,1,1),_UpsBaseIdentModel_Type())
upsBaseIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBaseIdentModel.setStatus(_A)
_UpsBaseIdentUpsName_Type=DisplayString
_UpsBaseIdentUpsName_Object=MibScalar
upsBaseIdentUpsName=_UpsBaseIdentUpsName_Object((1,3,6,1,4,1,935,1,1,1,1,1,2),_UpsBaseIdentUpsName_Type())
upsBaseIdentUpsName.setMaxAccess(_D)
if mibBuilder.loadTexts:upsBaseIdentUpsName.setStatus(_A)
_UpsSmartIdent_ObjectIdentity=ObjectIdentity
upsSmartIdent=_UpsSmartIdent_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,1,2))
_UpsSmartIdentFirmwareRevision_Type=DisplayString
_UpsSmartIdentFirmwareRevision_Object=MibScalar
upsSmartIdentFirmwareRevision=_UpsSmartIdentFirmwareRevision_Object((1,3,6,1,4,1,935,1,1,1,1,2,1),_UpsSmartIdentFirmwareRevision_Type())
upsSmartIdentFirmwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartIdentFirmwareRevision.setStatus(_A)
_UpsSmartIdentDateOfManufacture_Type=DisplayString
_UpsSmartIdentDateOfManufacture_Object=MibScalar
upsSmartIdentDateOfManufacture=_UpsSmartIdentDateOfManufacture_Object((1,3,6,1,4,1,935,1,1,1,1,2,2),_UpsSmartIdentDateOfManufacture_Type())
upsSmartIdentDateOfManufacture.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartIdentDateOfManufacture.setStatus(_A)
_UpsSmartIdentUpsSerialNumber_Type=DisplayString
_UpsSmartIdentUpsSerialNumber_Object=MibScalar
upsSmartIdentUpsSerialNumber=_UpsSmartIdentUpsSerialNumber_Object((1,3,6,1,4,1,935,1,1,1,1,2,3),_UpsSmartIdentUpsSerialNumber_Type())
upsSmartIdentUpsSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartIdentUpsSerialNumber.setStatus(_A)
_UpsSmartIdentAgentFirmwareRevision_Type=DisplayString
_UpsSmartIdentAgentFirmwareRevision_Object=MibScalar
upsSmartIdentAgentFirmwareRevision=_UpsSmartIdentAgentFirmwareRevision_Object((1,3,6,1,4,1,935,1,1,1,1,2,4),_UpsSmartIdentAgentFirmwareRevision_Type())
upsSmartIdentAgentFirmwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartIdentAgentFirmwareRevision.setStatus(_A)
_UpsBatteryp_ObjectIdentity=ObjectIdentity
upsBatteryp=_UpsBatteryp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,2))
_UpsBaseBattery_ObjectIdentity=ObjectIdentity
upsBaseBattery=_UpsBaseBattery_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,2,1))
class _UpsBaseBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('batteryNormal',2),('batteryLow',3)))
_UpsBaseBatteryStatus_Type.__name__=_C
_UpsBaseBatteryStatus_Object=MibScalar
upsBaseBatteryStatus=_UpsBaseBatteryStatus_Object((1,3,6,1,4,1,935,1,1,1,2,1,1),_UpsBaseBatteryStatus_Type())
upsBaseBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBaseBatteryStatus.setStatus(_A)
_UpsBaseBatteryTimeOnBattery_Type=Integer32
_UpsBaseBatteryTimeOnBattery_Object=MibScalar
upsBaseBatteryTimeOnBattery=_UpsBaseBatteryTimeOnBattery_Object((1,3,6,1,4,1,935,1,1,1,2,1,2),_UpsBaseBatteryTimeOnBattery_Type())
upsBaseBatteryTimeOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBaseBatteryTimeOnBattery.setStatus(_A)
_UpsBaseBatteryLastReplaceDate_Type=DisplayString
_UpsBaseBatteryLastReplaceDate_Object=MibScalar
upsBaseBatteryLastReplaceDate=_UpsBaseBatteryLastReplaceDate_Object((1,3,6,1,4,1,935,1,1,1,2,1,3),_UpsBaseBatteryLastReplaceDate_Type())
upsBaseBatteryLastReplaceDate.setMaxAccess(_D)
if mibBuilder.loadTexts:upsBaseBatteryLastReplaceDate.setStatus(_A)
_UpsSmartBattery_ObjectIdentity=ObjectIdentity
upsSmartBattery=_UpsSmartBattery_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,2,2))
_UpsSmartBatteryCapacity_Type=Integer32
_UpsSmartBatteryCapacity_Object=MibScalar
upsSmartBatteryCapacity=_UpsSmartBatteryCapacity_Object((1,3,6,1,4,1,935,1,1,1,2,2,1),_UpsSmartBatteryCapacity_Type())
upsSmartBatteryCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartBatteryCapacity.setStatus(_A)
_UpsSmartBatteryVoltage_Type=Integer32
_UpsSmartBatteryVoltage_Object=MibScalar
upsSmartBatteryVoltage=_UpsSmartBatteryVoltage_Object((1,3,6,1,4,1,935,1,1,1,2,2,2),_UpsSmartBatteryVoltage_Type())
upsSmartBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartBatteryVoltage.setStatus(_A)
_UpsSmartBatteryTemperature_Type=Integer32
_UpsSmartBatteryTemperature_Object=MibScalar
upsSmartBatteryTemperature=_UpsSmartBatteryTemperature_Object((1,3,6,1,4,1,935,1,1,1,2,2,3),_UpsSmartBatteryTemperature_Type())
upsSmartBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartBatteryTemperature.setStatus(_A)
_UpsSmartBatteryRunTimeRemaining_Type=Integer32
_UpsSmartBatteryRunTimeRemaining_Object=MibScalar
upsSmartBatteryRunTimeRemaining=_UpsSmartBatteryRunTimeRemaining_Object((1,3,6,1,4,1,935,1,1,1,2,2,4),_UpsSmartBatteryRunTimeRemaining_Type())
upsSmartBatteryRunTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartBatteryRunTimeRemaining.setStatus(_A)
class _UpsSmartBatteryReplaceIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noBatteryNeedsReplacing',1),('batteryNeedsReplacing',2)))
_UpsSmartBatteryReplaceIndicator_Type.__name__=_C
_UpsSmartBatteryReplaceIndicator_Object=MibScalar
upsSmartBatteryReplaceIndicator=_UpsSmartBatteryReplaceIndicator_Object((1,3,6,1,4,1,935,1,1,1,2,2,5),_UpsSmartBatteryReplaceIndicator_Type())
upsSmartBatteryReplaceIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartBatteryReplaceIndicator.setStatus(_A)
_UpsSmartBatteryFullChargeVoltage_Type=Integer32
_UpsSmartBatteryFullChargeVoltage_Object=MibScalar
upsSmartBatteryFullChargeVoltage=_UpsSmartBatteryFullChargeVoltage_Object((1,3,6,1,4,1,935,1,1,1,2,2,6),_UpsSmartBatteryFullChargeVoltage_Type())
upsSmartBatteryFullChargeVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartBatteryFullChargeVoltage.setStatus(_A)
_UpsSmartBatteryCurrent_Type=Integer32
_UpsSmartBatteryCurrent_Object=MibScalar
upsSmartBatteryCurrent=_UpsSmartBatteryCurrent_Object((1,3,6,1,4,1,935,1,1,1,2,2,7),_UpsSmartBatteryCurrent_Type())
upsSmartBatteryCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartBatteryCurrent.setStatus(_A)
_UpsInputp_ObjectIdentity=ObjectIdentity
upsInputp=_UpsInputp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,3))
_UpsBaseInput_ObjectIdentity=ObjectIdentity
upsBaseInput=_UpsBaseInput_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,3,1))
_UpsBaseInputPhase_Type=Integer32
_UpsBaseInputPhase_Object=MibScalar
upsBaseInputPhase=_UpsBaseInputPhase_Object((1,3,6,1,4,1,935,1,1,1,3,1,1),_UpsBaseInputPhase_Type())
upsBaseInputPhase.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBaseInputPhase.setStatus(_A)
_UpsSmartInput_ObjectIdentity=ObjectIdentity
upsSmartInput=_UpsSmartInput_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,3,2))
_UpsSmartInputLineVoltage_Type=Integer32
_UpsSmartInputLineVoltage_Object=MibScalar
upsSmartInputLineVoltage=_UpsSmartInputLineVoltage_Object((1,3,6,1,4,1,935,1,1,1,3,2,1),_UpsSmartInputLineVoltage_Type())
upsSmartInputLineVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartInputLineVoltage.setStatus(_A)
_UpsSmartInputMaxLineVoltage_Type=Integer32
_UpsSmartInputMaxLineVoltage_Object=MibScalar
upsSmartInputMaxLineVoltage=_UpsSmartInputMaxLineVoltage_Object((1,3,6,1,4,1,935,1,1,1,3,2,2),_UpsSmartInputMaxLineVoltage_Type())
upsSmartInputMaxLineVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartInputMaxLineVoltage.setStatus(_A)
_UpsSmartInputMinLineVoltage_Type=Integer32
_UpsSmartInputMinLineVoltage_Object=MibScalar
upsSmartInputMinLineVoltage=_UpsSmartInputMinLineVoltage_Object((1,3,6,1,4,1,935,1,1,1,3,2,3),_UpsSmartInputMinLineVoltage_Type())
upsSmartInputMinLineVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartInputMinLineVoltage.setStatus(_A)
_UpsSmartInputFrequency_Type=Integer32
_UpsSmartInputFrequency_Object=MibScalar
upsSmartInputFrequency=_UpsSmartInputFrequency_Object((1,3,6,1,4,1,935,1,1,1,3,2,4),_UpsSmartInputFrequency_Type())
upsSmartInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartInputFrequency.setStatus(_A)
class _UpsSmartInputLineFailCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noTransfer',1),('highLineVoltage',2),('brownout',3),('blackout',4),('smallMomentarySag',5),('deepMomentarySag',6),('smallMomentarySpike',7),('largeMomentarySpike',8)))
_UpsSmartInputLineFailCause_Type.__name__=_C
_UpsSmartInputLineFailCause_Object=MibScalar
upsSmartInputLineFailCause=_UpsSmartInputLineFailCause_Object((1,3,6,1,4,1,935,1,1,1,3,2,5),_UpsSmartInputLineFailCause_Type())
upsSmartInputLineFailCause.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartInputLineFailCause.setStatus(_A)
_UpsOutputp_ObjectIdentity=ObjectIdentity
upsOutputp=_UpsOutputp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,4))
_UpsBaseOutput_ObjectIdentity=ObjectIdentity
upsBaseOutput=_UpsBaseOutput_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,4,1))
class _UpsBaseOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_I,1),('onLine',2),('onBattery',3),('onBoost',4),('sleeping',5),('onBypass',6),('rebooting',7),('standBy',8),('onBuck',9)))
_UpsBaseOutputStatus_Type.__name__=_C
_UpsBaseOutputStatus_Object=MibScalar
upsBaseOutputStatus=_UpsBaseOutputStatus_Object((1,3,6,1,4,1,935,1,1,1,4,1,1),_UpsBaseOutputStatus_Type())
upsBaseOutputStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBaseOutputStatus.setStatus(_A)
_UpsBaseOutputPhase_Type=Integer32
_UpsBaseOutputPhase_Object=MibScalar
upsBaseOutputPhase=_UpsBaseOutputPhase_Object((1,3,6,1,4,1,935,1,1,1,4,1,2),_UpsBaseOutputPhase_Type())
upsBaseOutputPhase.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBaseOutputPhase.setStatus(_A)
_UpsSmartOutput_ObjectIdentity=ObjectIdentity
upsSmartOutput=_UpsSmartOutput_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,4,2))
_UpsSmartOutputVoltage_Type=Integer32
_UpsSmartOutputVoltage_Object=MibScalar
upsSmartOutputVoltage=_UpsSmartOutputVoltage_Object((1,3,6,1,4,1,935,1,1,1,4,2,1),_UpsSmartOutputVoltage_Type())
upsSmartOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartOutputVoltage.setStatus(_A)
_UpsSmartOutputFrequency_Type=Integer32
_UpsSmartOutputFrequency_Object=MibScalar
upsSmartOutputFrequency=_UpsSmartOutputFrequency_Object((1,3,6,1,4,1,935,1,1,1,4,2,2),_UpsSmartOutputFrequency_Type())
upsSmartOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartOutputFrequency.setStatus(_A)
_UpsSmartOutputLoad_Type=Integer32
_UpsSmartOutputLoad_Object=MibScalar
upsSmartOutputLoad=_UpsSmartOutputLoad_Object((1,3,6,1,4,1,935,1,1,1,4,2,3),_UpsSmartOutputLoad_Type())
upsSmartOutputLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartOutputLoad.setStatus(_A)
_UpsConfigp_ObjectIdentity=ObjectIdentity
upsConfigp=_UpsConfigp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,5))
_UpsBaseConfig_ObjectIdentity=ObjectIdentity
upsBaseConfig=_UpsBaseConfig_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,5,1))
_UpsBaseConfigNumDevices_Type=Integer32
_UpsBaseConfigNumDevices_Object=MibScalar
upsBaseConfigNumDevices=_UpsBaseConfigNumDevices_Object((1,3,6,1,4,1,935,1,1,1,5,1,1),_UpsBaseConfigNumDevices_Type())
upsBaseConfigNumDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBaseConfigNumDevices.setStatus(_A)
_UpsBaseConfigDeviceTable_Object=MibTable
upsBaseConfigDeviceTable=_UpsBaseConfigDeviceTable_Object((1,3,6,1,4,1,935,1,1,1,5,1,2))
if mibBuilder.loadTexts:upsBaseConfigDeviceTable.setStatus(_A)
_UpsBaseConfigDeviceEntry_Object=MibTableRow
upsBaseConfigDeviceEntry=_UpsBaseConfigDeviceEntry_Object((1,3,6,1,4,1,935,1,1,1,5,1,2,1))
upsBaseConfigDeviceEntry.setIndexNames((0,_J,_L))
if mibBuilder.loadTexts:upsBaseConfigDeviceEntry.setStatus(_A)
_IndexOfDevice_Type=Integer32
_IndexOfDevice_Object=MibTableColumn
indexOfDevice=_IndexOfDevice_Object((1,3,6,1,4,1,935,1,1,1,5,1,2,1,1),_IndexOfDevice_Type())
indexOfDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:indexOfDevice.setStatus(_A)
_NameOfDevice_Type=DisplayString
_NameOfDevice_Object=MibTableColumn
nameOfDevice=_NameOfDevice_Object((1,3,6,1,4,1,935,1,1,1,5,1,2,1,2),_NameOfDevice_Type())
nameOfDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:nameOfDevice.setStatus(_A)
_VaRatingOfDevice_Type=Integer32
_VaRatingOfDevice_Object=MibTableColumn
vaRatingOfDevice=_VaRatingOfDevice_Object((1,3,6,1,4,1,935,1,1,1,5,1,2,1,3),_VaRatingOfDevice_Type())
vaRatingOfDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:vaRatingOfDevice.setStatus(_A)
class _DeviceAccept_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_DeviceAccept_Type.__name__=_C
_DeviceAccept_Object=MibTableColumn
deviceAccept=_DeviceAccept_Object((1,3,6,1,4,1,935,1,1,1,5,1,2,1,4),_DeviceAccept_Type())
deviceAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceAccept.setStatus(_A)
_UpsSmartConfig_ObjectIdentity=ObjectIdentity
upsSmartConfig=_UpsSmartConfig_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,5,2))
_UpsSmartConfigRatedOutputVoltage_Type=Integer32
_UpsSmartConfigRatedOutputVoltage_Object=MibScalar
upsSmartConfigRatedOutputVoltage=_UpsSmartConfigRatedOutputVoltage_Object((1,3,6,1,4,1,935,1,1,1,5,2,1),_UpsSmartConfigRatedOutputVoltage_Type())
upsSmartConfigRatedOutputVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigRatedOutputVoltage.setStatus(_A)
_UpsSmartConfigHighTransferVolt_Type=Integer32
_UpsSmartConfigHighTransferVolt_Object=MibScalar
upsSmartConfigHighTransferVolt=_UpsSmartConfigHighTransferVolt_Object((1,3,6,1,4,1,935,1,1,1,5,2,2),_UpsSmartConfigHighTransferVolt_Type())
upsSmartConfigHighTransferVolt.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigHighTransferVolt.setStatus(_A)
_UpsSmartConfigLowTransferVolt_Type=Integer32
_UpsSmartConfigLowTransferVolt_Object=MibScalar
upsSmartConfigLowTransferVolt=_UpsSmartConfigLowTransferVolt_Object((1,3,6,1,4,1,935,1,1,1,5,2,3),_UpsSmartConfigLowTransferVolt_Type())
upsSmartConfigLowTransferVolt.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigLowTransferVolt.setStatus(_A)
class _UpsSmartConfigAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('timed',1),('atLowBattery',2),('never',3)))
_UpsSmartConfigAlarm_Type.__name__=_C
_UpsSmartConfigAlarm_Object=MibScalar
upsSmartConfigAlarm=_UpsSmartConfigAlarm_Object((1,3,6,1,4,1,935,1,1,1,5,2,4),_UpsSmartConfigAlarm_Type())
upsSmartConfigAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigAlarm.setStatus(_A)
_UpsSmartConfigAlarmTimer_Type=Integer32
_UpsSmartConfigAlarmTimer_Object=MibScalar
upsSmartConfigAlarmTimer=_UpsSmartConfigAlarmTimer_Object((1,3,6,1,4,1,935,1,1,1,5,2,5),_UpsSmartConfigAlarmTimer_Type())
upsSmartConfigAlarmTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigAlarmTimer.setStatus(_A)
_UpsSmartConfigMinReturnCapacity_Type=Integer32
_UpsSmartConfigMinReturnCapacity_Object=MibScalar
upsSmartConfigMinReturnCapacity=_UpsSmartConfigMinReturnCapacity_Object((1,3,6,1,4,1,935,1,1,1,5,2,6),_UpsSmartConfigMinReturnCapacity_Type())
upsSmartConfigMinReturnCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigMinReturnCapacity.setStatus(_A)
class _UpsSmartConfigSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('low',2),('medium',3),('high',4)))
_UpsSmartConfigSensitivity_Type.__name__=_C
_UpsSmartConfigSensitivity_Object=MibScalar
upsSmartConfigSensitivity=_UpsSmartConfigSensitivity_Object((1,3,6,1,4,1,935,1,1,1,5,2,7),_UpsSmartConfigSensitivity_Type())
upsSmartConfigSensitivity.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigSensitivity.setStatus(_A)
_UpsSmartConfigLowBatteryRunTime_Type=Integer32
_UpsSmartConfigLowBatteryRunTime_Object=MibScalar
upsSmartConfigLowBatteryRunTime=_UpsSmartConfigLowBatteryRunTime_Object((1,3,6,1,4,1,935,1,1,1,5,2,8),_UpsSmartConfigLowBatteryRunTime_Type())
upsSmartConfigLowBatteryRunTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigLowBatteryRunTime.setStatus(_A)
_UpsSmartConfigReturnDelay_Type=Integer32
_UpsSmartConfigReturnDelay_Object=MibScalar
upsSmartConfigReturnDelay=_UpsSmartConfigReturnDelay_Object((1,3,6,1,4,1,935,1,1,1,5,2,9),_UpsSmartConfigReturnDelay_Type())
upsSmartConfigReturnDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigReturnDelay.setStatus(_A)
_UpsSmartConfigShutoffDelay_Type=Integer32
_UpsSmartConfigShutoffDelay_Object=MibScalar
upsSmartConfigShutoffDelay=_UpsSmartConfigShutoffDelay_Object((1,3,6,1,4,1,935,1,1,1,5,2,10),_UpsSmartConfigShutoffDelay_Type())
upsSmartConfigShutoffDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigShutoffDelay.setStatus(_A)
_UpsSmartConfigUpsSleepTime_Type=Integer32
_UpsSmartConfigUpsSleepTime_Object=MibScalar
upsSmartConfigUpsSleepTime=_UpsSmartConfigUpsSleepTime_Object((1,3,6,1,4,1,935,1,1,1,5,2,11),_UpsSmartConfigUpsSleepTime_Type())
upsSmartConfigUpsSleepTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigUpsSleepTime.setStatus(_A)
class _UpsSmartConfigSetEEPROMDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noSetEEPROMDefaults',1),('setEEPROMDefaults',2)))
_UpsSmartConfigSetEEPROMDefaults_Type.__name__=_C
_UpsSmartConfigSetEEPROMDefaults_Object=MibScalar
upsSmartConfigSetEEPROMDefaults=_UpsSmartConfigSetEEPROMDefaults_Object((1,3,6,1,4,1,935,1,1,1,5,2,12),_UpsSmartConfigSetEEPROMDefaults_Type())
upsSmartConfigSetEEPROMDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartConfigSetEEPROMDefaults.setStatus(_A)
_UpsControlp_ObjectIdentity=ObjectIdentity
upsControlp=_UpsControlp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,6))
_UpsBaseControl_ObjectIdentity=ObjectIdentity
upsBaseControl=_UpsBaseControl_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,6,1))
class _UpsBaseControlConserveBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noTurnOffUps',1),('turnUpsOffToConserveBattery',2),('turnUpsOffToConserveBatteryDelay',3)))
_UpsBaseControlConserveBattery_Type.__name__=_C
_UpsBaseControlConserveBattery_Object=MibScalar
upsBaseControlConserveBattery=_UpsBaseControlConserveBattery_Object((1,3,6,1,4,1,935,1,1,1,6,1,1),_UpsBaseControlConserveBattery_Type())
upsBaseControlConserveBattery.setMaxAccess(_D)
if mibBuilder.loadTexts:upsBaseControlConserveBattery.setStatus(_A)
_UpsSmartControl_ObjectIdentity=ObjectIdentity
upsSmartControl=_UpsSmartControl_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,6,2))
class _UpsSmartControlUpsOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noTurnUpsOff',1),('turnUpsOff',2)))
_UpsSmartControlUpsOff_Type.__name__=_C
_UpsSmartControlUpsOff_Object=MibScalar
upsSmartControlUpsOff=_UpsSmartControlUpsOff_Object((1,3,6,1,4,1,935,1,1,1,6,2,1),_UpsSmartControlUpsOff_Type())
upsSmartControlUpsOff.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartControlUpsOff.setStatus(_A)
class _UpsSmartControlRebootUps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noRebootUps',1),('rebootUps',2)))
_UpsSmartControlRebootUps_Type.__name__=_C
_UpsSmartControlRebootUps_Object=MibScalar
upsSmartControlRebootUps=_UpsSmartControlRebootUps_Object((1,3,6,1,4,1,935,1,1,1,6,2,2),_UpsSmartControlRebootUps_Type())
upsSmartControlRebootUps.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartControlRebootUps.setStatus(_A)
class _UpsSmartControlUpsSleep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noPutUpsToSleep',1),('putUpsToSleep',2)))
_UpsSmartControlUpsSleep_Type.__name__=_C
_UpsSmartControlUpsSleep_Object=MibScalar
upsSmartControlUpsSleep=_UpsSmartControlUpsSleep_Object((1,3,6,1,4,1,935,1,1,1,6,2,3),_UpsSmartControlUpsSleep_Type())
upsSmartControlUpsSleep.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartControlUpsSleep.setStatus(_A)
class _UpsSmartControlSimulatePowerFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noSimulatePowerFailure',1),('simulatePowerFailure',2)))
_UpsSmartControlSimulatePowerFail_Type.__name__=_C
_UpsSmartControlSimulatePowerFail_Object=MibScalar
upsSmartControlSimulatePowerFail=_UpsSmartControlSimulatePowerFail_Object((1,3,6,1,4,1,935,1,1,1,6,2,4),_UpsSmartControlSimulatePowerFail_Type())
upsSmartControlSimulatePowerFail.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartControlSimulatePowerFail.setStatus(_A)
class _UpsSmartControlFlashAndBeep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noFlashAndBeep',1),('flashAndBeep',2)))
_UpsSmartControlFlashAndBeep_Type.__name__=_C
_UpsSmartControlFlashAndBeep_Object=MibScalar
upsSmartControlFlashAndBeep=_UpsSmartControlFlashAndBeep_Object((1,3,6,1,4,1,935,1,1,1,6,2,5),_UpsSmartControlFlashAndBeep_Type())
upsSmartControlFlashAndBeep.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartControlFlashAndBeep.setStatus(_A)
class _UpsSmartControlTurnOnUpsLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noUpsSmartControlTurnOnUpsLoad',1),(_M,2)))
_UpsSmartControlTurnOnUpsLoad_Type.__name__=_C
_UpsSmartControlTurnOnUpsLoad_Object=MibScalar
upsSmartControlTurnOnUpsLoad=_UpsSmartControlTurnOnUpsLoad_Object((1,3,6,1,4,1,935,1,1,1,6,2,6),_UpsSmartControlTurnOnUpsLoad_Type())
upsSmartControlTurnOnUpsLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartControlTurnOnUpsLoad.setStatus(_A)
_UpsTestp_ObjectIdentity=ObjectIdentity
upsTestp=_UpsTestp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,7))
_UpsBaseTest_ObjectIdentity=ObjectIdentity
upsBaseTest=_UpsBaseTest_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,7,1))
_UpsSmartTest_ObjectIdentity=ObjectIdentity
upsSmartTest=_UpsSmartTest_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,7,2))
class _UpsSmartTestDiagnosticSchedule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('biweekly',2),('weekly',3),('never',4)))
_UpsSmartTestDiagnosticSchedule_Type.__name__=_C
_UpsSmartTestDiagnosticSchedule_Object=MibScalar
upsSmartTestDiagnosticSchedule=_UpsSmartTestDiagnosticSchedule_Object((1,3,6,1,4,1,935,1,1,1,7,2,1),_UpsSmartTestDiagnosticSchedule_Type())
upsSmartTestDiagnosticSchedule.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartTestDiagnosticSchedule.setStatus(_A)
class _UpsSmartTestDiagnostics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noTestDiagnostics',1),('testDiagnostics',2)))
_UpsSmartTestDiagnostics_Type.__name__=_C
_UpsSmartTestDiagnostics_Object=MibScalar
upsSmartTestDiagnostics=_UpsSmartTestDiagnostics_Object((1,3,6,1,4,1,935,1,1,1,7,2,2),_UpsSmartTestDiagnostics_Type())
upsSmartTestDiagnostics.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartTestDiagnostics.setStatus(_A)
class _UpsSmartTestDiagnosticsResults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('failed',2),(_N,3),('testInProgress',4)))
_UpsSmartTestDiagnosticsResults_Type.__name__=_C
_UpsSmartTestDiagnosticsResults_Object=MibScalar
upsSmartTestDiagnosticsResults=_UpsSmartTestDiagnosticsResults_Object((1,3,6,1,4,1,935,1,1,1,7,2,3),_UpsSmartTestDiagnosticsResults_Type())
upsSmartTestDiagnosticsResults.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartTestDiagnosticsResults.setStatus(_A)
_UpsSmartTestLastDiagnosticsDate_Type=DisplayString
_UpsSmartTestLastDiagnosticsDate_Object=MibScalar
upsSmartTestLastDiagnosticsDate=_UpsSmartTestLastDiagnosticsDate_Object((1,3,6,1,4,1,935,1,1,1,7,2,4),_UpsSmartTestLastDiagnosticsDate_Type())
upsSmartTestLastDiagnosticsDate.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartTestLastDiagnosticsDate.setStatus(_A)
class _UpsSmartTestIndicators_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noTestIndicators',1),('testIndicators',2)))
_UpsSmartTestIndicators_Type.__name__=_C
_UpsSmartTestIndicators_Object=MibScalar
upsSmartTestIndicators=_UpsSmartTestIndicators_Object((1,3,6,1,4,1,935,1,1,1,7,2,5),_UpsSmartTestIndicators_Type())
upsSmartTestIndicators.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartTestIndicators.setStatus(_A)
class _UpsSmartTestRuntimeCalibration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noPerformCalibration',1),('performCalibration',2),('cancelCurrentCalibration',3)))
_UpsSmartTestRuntimeCalibration_Type.__name__=_C
_UpsSmartTestRuntimeCalibration_Object=MibScalar
upsSmartTestRuntimeCalibration=_UpsSmartTestRuntimeCalibration_Object((1,3,6,1,4,1,935,1,1,1,7,2,6),_UpsSmartTestRuntimeCalibration_Type())
upsSmartTestRuntimeCalibration.setMaxAccess(_D)
if mibBuilder.loadTexts:upsSmartTestRuntimeCalibration.setStatus(_A)
class _UpsSmartTestCalibrationResults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),(_N,2),('calibrationInProgress',3)))
_UpsSmartTestCalibrationResults_Type.__name__=_C
_UpsSmartTestCalibrationResults_Object=MibScalar
upsSmartTestCalibrationResults=_UpsSmartTestCalibrationResults_Object((1,3,6,1,4,1,935,1,1,1,7,2,7),_UpsSmartTestCalibrationResults_Type())
upsSmartTestCalibrationResults.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartTestCalibrationResults.setStatus(_A)
_UpsSmartTestCalibrationDate_Type=DisplayString
_UpsSmartTestCalibrationDate_Object=MibScalar
upsSmartTestCalibrationDate=_UpsSmartTestCalibrationDate_Object((1,3,6,1,4,1,935,1,1,1,7,2,8),_UpsSmartTestCalibrationDate_Type())
upsSmartTestCalibrationDate.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSmartTestCalibrationDate.setStatus(_A)
_UpsThreePhase_ObjectIdentity=ObjectIdentity
upsThreePhase=_UpsThreePhase_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,8))
_UpsThreePhaseBatteryGrp_ObjectIdentity=ObjectIdentity
upsThreePhaseBatteryGrp=_UpsThreePhaseBatteryGrp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,8,1))
_UpsThreePhaseBatteryVoltage_Type=Integer32
_UpsThreePhaseBatteryVoltage_Object=MibScalar
upsThreePhaseBatteryVoltage=_UpsThreePhaseBatteryVoltage_Object((1,3,6,1,4,1,935,1,1,1,8,1,1),_UpsThreePhaseBatteryVoltage_Type())
upsThreePhaseBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseBatteryVoltage.setStatus(_A)
_UpsThreePhaseBatteryCapacityPercentage_Type=Integer32
_UpsThreePhaseBatteryCapacityPercentage_Object=MibScalar
upsThreePhaseBatteryCapacityPercentage=_UpsThreePhaseBatteryCapacityPercentage_Object((1,3,6,1,4,1,935,1,1,1,8,1,2),_UpsThreePhaseBatteryCapacityPercentage_Type())
upsThreePhaseBatteryCapacityPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseBatteryCapacityPercentage.setStatus(_A)
_UpsThreePhaseBatteryTimeRemain_Type=Integer32
_UpsThreePhaseBatteryTimeRemain_Object=MibScalar
upsThreePhaseBatteryTimeRemain=_UpsThreePhaseBatteryTimeRemain_Object((1,3,6,1,4,1,935,1,1,1,8,1,3),_UpsThreePhaseBatteryTimeRemain_Type())
upsThreePhaseBatteryTimeRemain.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseBatteryTimeRemain.setStatus(_A)
_UpsThreePhaseBatteryCurrent_Type=Integer32
_UpsThreePhaseBatteryCurrent_Object=MibScalar
upsThreePhaseBatteryCurrent=_UpsThreePhaseBatteryCurrent_Object((1,3,6,1,4,1,935,1,1,1,8,1,4),_UpsThreePhaseBatteryCurrent_Type())
upsThreePhaseBatteryCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseBatteryCurrent.setStatus(_A)
_UpsThreePhaseBatteryTemperature_Type=Integer32
_UpsThreePhaseBatteryTemperature_Object=MibScalar
upsThreePhaseBatteryTemperature=_UpsThreePhaseBatteryTemperature_Object((1,3,6,1,4,1,935,1,1,1,8,1,5),_UpsThreePhaseBatteryTemperature_Type())
upsThreePhaseBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseBatteryTemperature.setStatus(_A)
_UpsThreePhaseInputGrp_ObjectIdentity=ObjectIdentity
upsThreePhaseInputGrp=_UpsThreePhaseInputGrp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,8,2))
_UpsThreePhaseInputFrequency_Type=Integer32
_UpsThreePhaseInputFrequency_Object=MibScalar
upsThreePhaseInputFrequency=_UpsThreePhaseInputFrequency_Object((1,3,6,1,4,1,935,1,1,1,8,2,1),_UpsThreePhaseInputFrequency_Type())
upsThreePhaseInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseInputFrequency.setStatus(_A)
_UpsThreePhaseInputVoltageR_Type=Integer32
_UpsThreePhaseInputVoltageR_Object=MibScalar
upsThreePhaseInputVoltageR=_UpsThreePhaseInputVoltageR_Object((1,3,6,1,4,1,935,1,1,1,8,2,2),_UpsThreePhaseInputVoltageR_Type())
upsThreePhaseInputVoltageR.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseInputVoltageR.setStatus(_A)
_UpsThreePhaseInputVoltageS_Type=Integer32
_UpsThreePhaseInputVoltageS_Object=MibScalar
upsThreePhaseInputVoltageS=_UpsThreePhaseInputVoltageS_Object((1,3,6,1,4,1,935,1,1,1,8,2,3),_UpsThreePhaseInputVoltageS_Type())
upsThreePhaseInputVoltageS.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseInputVoltageS.setStatus(_A)
_UpsThreePhaseInputVoltageT_Type=Integer32
_UpsThreePhaseInputVoltageT_Object=MibScalar
upsThreePhaseInputVoltageT=_UpsThreePhaseInputVoltageT_Object((1,3,6,1,4,1,935,1,1,1,8,2,4),_UpsThreePhaseInputVoltageT_Type())
upsThreePhaseInputVoltageT.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseInputVoltageT.setStatus(_A)
_UpsThreePhaseOutputGrp_ObjectIdentity=ObjectIdentity
upsThreePhaseOutputGrp=_UpsThreePhaseOutputGrp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,8,3))
_UpsThreePhaseOutputFrequency_Type=Integer32
_UpsThreePhaseOutputFrequency_Object=MibScalar
upsThreePhaseOutputFrequency=_UpsThreePhaseOutputFrequency_Object((1,3,6,1,4,1,935,1,1,1,8,3,1),_UpsThreePhaseOutputFrequency_Type())
upsThreePhaseOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseOutputFrequency.setStatus(_A)
_UpsThreePhaseOutputVoltageR_Type=Integer32
_UpsThreePhaseOutputVoltageR_Object=MibScalar
upsThreePhaseOutputVoltageR=_UpsThreePhaseOutputVoltageR_Object((1,3,6,1,4,1,935,1,1,1,8,3,2),_UpsThreePhaseOutputVoltageR_Type())
upsThreePhaseOutputVoltageR.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseOutputVoltageR.setStatus(_A)
_UpsThreePhaseOutputVoltageS_Type=Integer32
_UpsThreePhaseOutputVoltageS_Object=MibScalar
upsThreePhaseOutputVoltageS=_UpsThreePhaseOutputVoltageS_Object((1,3,6,1,4,1,935,1,1,1,8,3,3),_UpsThreePhaseOutputVoltageS_Type())
upsThreePhaseOutputVoltageS.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseOutputVoltageS.setStatus(_A)
_UpsThreePhaseOutputVoltageT_Type=Integer32
_UpsThreePhaseOutputVoltageT_Object=MibScalar
upsThreePhaseOutputVoltageT=_UpsThreePhaseOutputVoltageT_Object((1,3,6,1,4,1,935,1,1,1,8,3,4),_UpsThreePhaseOutputVoltageT_Type())
upsThreePhaseOutputVoltageT.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseOutputVoltageT.setStatus(_A)
_UpsThreePhaseOutputLoadPercentageR_Type=Integer32
_UpsThreePhaseOutputLoadPercentageR_Object=MibScalar
upsThreePhaseOutputLoadPercentageR=_UpsThreePhaseOutputLoadPercentageR_Object((1,3,6,1,4,1,935,1,1,1,8,3,5),_UpsThreePhaseOutputLoadPercentageR_Type())
upsThreePhaseOutputLoadPercentageR.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseOutputLoadPercentageR.setStatus(_A)
_UpsThreePhaseOutputLoadPercentageS_Type=Integer32
_UpsThreePhaseOutputLoadPercentageS_Object=MibScalar
upsThreePhaseOutputLoadPercentageS=_UpsThreePhaseOutputLoadPercentageS_Object((1,3,6,1,4,1,935,1,1,1,8,3,6),_UpsThreePhaseOutputLoadPercentageS_Type())
upsThreePhaseOutputLoadPercentageS.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseOutputLoadPercentageS.setStatus(_A)
_UpsThreePhaseOutputLoadPercentageT_Type=Integer32
_UpsThreePhaseOutputLoadPercentageT_Object=MibScalar
upsThreePhaseOutputLoadPercentageT=_UpsThreePhaseOutputLoadPercentageT_Object((1,3,6,1,4,1,935,1,1,1,8,3,7),_UpsThreePhaseOutputLoadPercentageT_Type())
upsThreePhaseOutputLoadPercentageT.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseOutputLoadPercentageT.setStatus(_A)
_UpsThreePhaseBypassGrp_ObjectIdentity=ObjectIdentity
upsThreePhaseBypassGrp=_UpsThreePhaseBypassGrp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,8,4))
_UpsThreePhaseBypassSourceFrequency_Type=Integer32
_UpsThreePhaseBypassSourceFrequency_Object=MibScalar
upsThreePhaseBypassSourceFrequency=_UpsThreePhaseBypassSourceFrequency_Object((1,3,6,1,4,1,935,1,1,1,8,4,1),_UpsThreePhaseBypassSourceFrequency_Type())
upsThreePhaseBypassSourceFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseBypassSourceFrequency.setStatus(_A)
_UpsThreePhaseBypassSourceVoltageR_Type=Integer32
_UpsThreePhaseBypassSourceVoltageR_Object=MibScalar
upsThreePhaseBypassSourceVoltageR=_UpsThreePhaseBypassSourceVoltageR_Object((1,3,6,1,4,1,935,1,1,1,8,4,2),_UpsThreePhaseBypassSourceVoltageR_Type())
upsThreePhaseBypassSourceVoltageR.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseBypassSourceVoltageR.setStatus(_A)
_UpsThreePhaseBypassSourceVoltageS_Type=Integer32
_UpsThreePhaseBypassSourceVoltageS_Object=MibScalar
upsThreePhaseBypassSourceVoltageS=_UpsThreePhaseBypassSourceVoltageS_Object((1,3,6,1,4,1,935,1,1,1,8,4,3),_UpsThreePhaseBypassSourceVoltageS_Type())
upsThreePhaseBypassSourceVoltageS.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseBypassSourceVoltageS.setStatus(_A)
_UpsThreePhaseBypassSourceVoltageT_Type=Integer32
_UpsThreePhaseBypassSourceVoltageT_Object=MibScalar
upsThreePhaseBypassSourceVoltageT=_UpsThreePhaseBypassSourceVoltageT_Object((1,3,6,1,4,1,935,1,1,1,8,4,4),_UpsThreePhaseBypassSourceVoltageT_Type())
upsThreePhaseBypassSourceVoltageT.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseBypassSourceVoltageT.setStatus(_A)
_UpsThreePhaseDCandRectifierStatusGrp_ObjectIdentity=ObjectIdentity
upsThreePhaseDCandRectifierStatusGrp=_UpsThreePhaseDCandRectifierStatusGrp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,8,5))
class _UpsThreePhaseDCandRectifierStatusRecRotError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseDCandRectifierStatusRecRotError_Type.__name__=_C
_UpsThreePhaseDCandRectifierStatusRecRotError_Object=MibScalar
upsThreePhaseDCandRectifierStatusRecRotError=_UpsThreePhaseDCandRectifierStatusRecRotError_Object((1,3,6,1,4,1,935,1,1,1,8,5,1),_UpsThreePhaseDCandRectifierStatusRecRotError_Type())
upsThreePhaseDCandRectifierStatusRecRotError.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseDCandRectifierStatusRecRotError.setStatus(_A)
class _UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Type.__name__=_C
_UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Object=MibScalar
upsThreePhaseDCandRectifierStatusLowBatteryShutdown=_UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Object((1,3,6,1,4,1,935,1,1,1,8,5,2),_UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Type())
upsThreePhaseDCandRectifierStatusLowBatteryShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseDCandRectifierStatusLowBatteryShutdown.setStatus(_A)
class _UpsThreePhaseDCandRectifierStatusLowBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseDCandRectifierStatusLowBattery_Type.__name__=_C
_UpsThreePhaseDCandRectifierStatusLowBattery_Object=MibScalar
upsThreePhaseDCandRectifierStatusLowBattery=_UpsThreePhaseDCandRectifierStatusLowBattery_Object((1,3,6,1,4,1,935,1,1,1,8,5,3),_UpsThreePhaseDCandRectifierStatusLowBattery_Type())
upsThreePhaseDCandRectifierStatusLowBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseDCandRectifierStatusLowBattery.setStatus(_A)
class _UpsThreePhaseDCandRectifierStatusInAndOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('threeInOneOut',2),('threeInThreeOut',3)))
_UpsThreePhaseDCandRectifierStatusInAndOut_Type.__name__=_C
_UpsThreePhaseDCandRectifierStatusInAndOut_Object=MibScalar
upsThreePhaseDCandRectifierStatusInAndOut=_UpsThreePhaseDCandRectifierStatusInAndOut_Object((1,3,6,1,4,1,935,1,1,1,8,5,4),_UpsThreePhaseDCandRectifierStatusInAndOut_Type())
upsThreePhaseDCandRectifierStatusInAndOut.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseDCandRectifierStatusInAndOut.setStatus(_A)
class _UpsThreePhaseDCandRectifierStatusBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5)));namedValues=NamedValues(*(('backup',4),('acnormal',5)))
_UpsThreePhaseDCandRectifierStatusBatteryStatus_Type.__name__=_C
_UpsThreePhaseDCandRectifierStatusBatteryStatus_Object=MibScalar
upsThreePhaseDCandRectifierStatusBatteryStatus=_UpsThreePhaseDCandRectifierStatusBatteryStatus_Object((1,3,6,1,4,1,935,1,1,1,8,5,5),_UpsThreePhaseDCandRectifierStatusBatteryStatus_Type())
upsThreePhaseDCandRectifierStatusBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseDCandRectifierStatusBatteryStatus.setStatus(_A)
class _UpsThreePhaseDCandRectifierStatusChargeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,7,16)));namedValues=NamedValues(*(('boost',6),('float',7),(_E,16)))
_UpsThreePhaseDCandRectifierStatusChargeStatus_Type.__name__=_C
_UpsThreePhaseDCandRectifierStatusChargeStatus_Object=MibScalar
upsThreePhaseDCandRectifierStatusChargeStatus=_UpsThreePhaseDCandRectifierStatusChargeStatus_Object((1,3,6,1,4,1,935,1,1,1,8,5,6),_UpsThreePhaseDCandRectifierStatusChargeStatus_Type())
upsThreePhaseDCandRectifierStatusChargeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseDCandRectifierStatusChargeStatus.setStatus(_A)
class _UpsThreePhaseDCandRectifierStatusRecOperating_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseDCandRectifierStatusRecOperating_Type.__name__=_C
_UpsThreePhaseDCandRectifierStatusRecOperating_Object=MibScalar
upsThreePhaseDCandRectifierStatusRecOperating=_UpsThreePhaseDCandRectifierStatusRecOperating_Object((1,3,6,1,4,1,935,1,1,1,8,5,7),_UpsThreePhaseDCandRectifierStatusRecOperating_Type())
upsThreePhaseDCandRectifierStatusRecOperating.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseDCandRectifierStatusRecOperating.setStatus(_A)
_UpsThreePhaseUPSStatusGrp_ObjectIdentity=ObjectIdentity
upsThreePhaseUPSStatusGrp=_UpsThreePhaseUPSStatusGrp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,8,6))
class _UpsThreePhaseUPSStatusBypassFreqFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseUPSStatusBypassFreqFail_Type.__name__=_C
_UpsThreePhaseUPSStatusBypassFreqFail_Object=MibScalar
upsThreePhaseUPSStatusBypassFreqFail=_UpsThreePhaseUPSStatusBypassFreqFail_Object((1,3,6,1,4,1,935,1,1,1,8,6,1),_UpsThreePhaseUPSStatusBypassFreqFail_Type())
upsThreePhaseUPSStatusBypassFreqFail.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseUPSStatusBypassFreqFail.setStatus(_A)
class _UpsThreePhaseUPSStatusManualBypassBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,9)));namedValues=NamedValues(*(('close',8),('open',9)))
_UpsThreePhaseUPSStatusManualBypassBreaker_Type.__name__=_C
_UpsThreePhaseUPSStatusManualBypassBreaker_Object=MibScalar
upsThreePhaseUPSStatusManualBypassBreaker=_UpsThreePhaseUPSStatusManualBypassBreaker_Object((1,3,6,1,4,1,935,1,1,1,8,6,2),_UpsThreePhaseUPSStatusManualBypassBreaker_Type())
upsThreePhaseUPSStatusManualBypassBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseUPSStatusManualBypassBreaker.setStatus(_A)
class _UpsThreePhaseUPSStatusACStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,11)));namedValues=NamedValues(*((_G,10),(_H,11)))
_UpsThreePhaseUPSStatusACStatus_Type.__name__=_C
_UpsThreePhaseUPSStatusACStatus_Object=MibScalar
upsThreePhaseUPSStatusACStatus=_UpsThreePhaseUPSStatusACStatus_Object((1,3,6,1,4,1,935,1,1,1,8,6,3),_UpsThreePhaseUPSStatusACStatus_Type())
upsThreePhaseUPSStatusACStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseUPSStatusACStatus.setStatus(_A)
class _UpsThreePhaseUPSStaticSwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(12,13)));namedValues=NamedValues(*(('invermode',12),('bypassmode',13)))
_UpsThreePhaseUPSStaticSwitchMode_Type.__name__=_C
_UpsThreePhaseUPSStaticSwitchMode_Object=MibScalar
upsThreePhaseUPSStaticSwitchMode=_UpsThreePhaseUPSStaticSwitchMode_Object((1,3,6,1,4,1,935,1,1,1,8,6,4),_UpsThreePhaseUPSStaticSwitchMode_Type())
upsThreePhaseUPSStaticSwitchMode.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseUPSStaticSwitchMode.setStatus(_A)
class _UpsThreePhaseUPSStatusInverterOperating_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseUPSStatusInverterOperating_Type.__name__=_C
_UpsThreePhaseUPSStatusInverterOperating_Object=MibScalar
upsThreePhaseUPSStatusInverterOperating=_UpsThreePhaseUPSStatusInverterOperating_Object((1,3,6,1,4,1,935,1,1,1,8,6,5),_UpsThreePhaseUPSStatusInverterOperating_Type())
upsThreePhaseUPSStatusInverterOperating.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseUPSStatusInverterOperating.setStatus(_A)
_UpsThreePhaseFaultStatusGrp_ObjectIdentity=ObjectIdentity
upsThreePhaseFaultStatusGrp=_UpsThreePhaseFaultStatusGrp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,8,7))
class _UpsThreePhaseFaultStatusEmergencyStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseFaultStatusEmergencyStop_Type.__name__=_C
_UpsThreePhaseFaultStatusEmergencyStop_Object=MibScalar
upsThreePhaseFaultStatusEmergencyStop=_UpsThreePhaseFaultStatusEmergencyStop_Object((1,3,6,1,4,1,935,1,1,1,8,7,1),_UpsThreePhaseFaultStatusEmergencyStop_Type())
upsThreePhaseFaultStatusEmergencyStop.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseFaultStatusEmergencyStop.setStatus(_A)
class _UpsThreePhaseFaultStatusHighDCShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseFaultStatusHighDCShutdown_Type.__name__=_C
_UpsThreePhaseFaultStatusHighDCShutdown_Object=MibScalar
upsThreePhaseFaultStatusHighDCShutdown=_UpsThreePhaseFaultStatusHighDCShutdown_Object((1,3,6,1,4,1,935,1,1,1,8,7,2),_UpsThreePhaseFaultStatusHighDCShutdown_Type())
upsThreePhaseFaultStatusHighDCShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseFaultStatusHighDCShutdown.setStatus(_A)
class _UpsThreePhaseFaultStatusBypassBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseFaultStatusBypassBreaker_Type.__name__=_C
_UpsThreePhaseFaultStatusBypassBreaker_Object=MibScalar
upsThreePhaseFaultStatusBypassBreaker=_UpsThreePhaseFaultStatusBypassBreaker_Object((1,3,6,1,4,1,935,1,1,1,8,7,3),_UpsThreePhaseFaultStatusBypassBreaker_Type())
upsThreePhaseFaultStatusBypassBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseFaultStatusBypassBreaker.setStatus(_A)
class _UpsThreePhaseFaultStatusOverLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseFaultStatusOverLoad_Type.__name__=_C
_UpsThreePhaseFaultStatusOverLoad_Object=MibScalar
upsThreePhaseFaultStatusOverLoad=_UpsThreePhaseFaultStatusOverLoad_Object((1,3,6,1,4,1,935,1,1,1,8,7,4),_UpsThreePhaseFaultStatusOverLoad_Type())
upsThreePhaseFaultStatusOverLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseFaultStatusOverLoad.setStatus(_A)
class _UpsThreePhaseFaultStatusInverterOutputFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseFaultStatusInverterOutputFail_Type.__name__=_C
_UpsThreePhaseFaultStatusInverterOutputFail_Object=MibScalar
upsThreePhaseFaultStatusInverterOutputFail=_UpsThreePhaseFaultStatusInverterOutputFail_Object((1,3,6,1,4,1,935,1,1,1,8,7,5),_UpsThreePhaseFaultStatusInverterOutputFail_Type())
upsThreePhaseFaultStatusInverterOutputFail.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseFaultStatusInverterOutputFail.setStatus(_A)
class _UpsThreePhaseFaultStatusOverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseFaultStatusOverTemperature_Type.__name__=_C
_UpsThreePhaseFaultStatusOverTemperature_Object=MibScalar
upsThreePhaseFaultStatusOverTemperature=_UpsThreePhaseFaultStatusOverTemperature_Object((1,3,6,1,4,1,935,1,1,1,8,7,6),_UpsThreePhaseFaultStatusOverTemperature_Type())
upsThreePhaseFaultStatusOverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseFaultStatusOverTemperature.setStatus(_A)
class _UpsThreePhaseFaultStatusShortCircuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(14,16)));namedValues=NamedValues(*((_F,14),(_E,16)))
_UpsThreePhaseFaultStatusShortCircuit_Type.__name__=_C
_UpsThreePhaseFaultStatusShortCircuit_Object=MibScalar
upsThreePhaseFaultStatusShortCircuit=_UpsThreePhaseFaultStatusShortCircuit_Object((1,3,6,1,4,1,935,1,1,1,8,7,7),_UpsThreePhaseFaultStatusShortCircuit_Type())
upsThreePhaseFaultStatusShortCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseFaultStatusShortCircuit.setStatus(_A)
_UpsThreePhaseRatingGrp_ObjectIdentity=ObjectIdentity
upsThreePhaseRatingGrp=_UpsThreePhaseRatingGrp_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,8,8))
_UpsThreePhaseRatingRectifierVoltage_Type=DisplayString
_UpsThreePhaseRatingRectifierVoltage_Object=MibScalar
upsThreePhaseRatingRectifierVoltage=_UpsThreePhaseRatingRectifierVoltage_Object((1,3,6,1,4,1,935,1,1,1,8,8,1),_UpsThreePhaseRatingRectifierVoltage_Type())
upsThreePhaseRatingRectifierVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseRatingRectifierVoltage.setStatus(_A)
_UpsThreePhaseRatingRectifierFrequency_Type=Integer32
_UpsThreePhaseRatingRectifierFrequency_Object=MibScalar
upsThreePhaseRatingRectifierFrequency=_UpsThreePhaseRatingRectifierFrequency_Object((1,3,6,1,4,1,935,1,1,1,8,8,2),_UpsThreePhaseRatingRectifierFrequency_Type())
upsThreePhaseRatingRectifierFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseRatingRectifierFrequency.setStatus(_A)
_UpsThreePhaseRatingBypassVoltage_Type=DisplayString
_UpsThreePhaseRatingBypassVoltage_Object=MibScalar
upsThreePhaseRatingBypassVoltage=_UpsThreePhaseRatingBypassVoltage_Object((1,3,6,1,4,1,935,1,1,1,8,8,3),_UpsThreePhaseRatingBypassVoltage_Type())
upsThreePhaseRatingBypassVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseRatingBypassVoltage.setStatus(_A)
_UpsThreePhaseRatingBypassFrequency_Type=Integer32
_UpsThreePhaseRatingBypassFrequency_Object=MibScalar
upsThreePhaseRatingBypassFrequency=_UpsThreePhaseRatingBypassFrequency_Object((1,3,6,1,4,1,935,1,1,1,8,8,4),_UpsThreePhaseRatingBypassFrequency_Type())
upsThreePhaseRatingBypassFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseRatingBypassFrequency.setStatus(_A)
_UpsThreePhaseRatingOutputVoltage_Type=DisplayString
_UpsThreePhaseRatingOutputVoltage_Object=MibScalar
upsThreePhaseRatingOutputVoltage=_UpsThreePhaseRatingOutputVoltage_Object((1,3,6,1,4,1,935,1,1,1,8,8,5),_UpsThreePhaseRatingOutputVoltage_Type())
upsThreePhaseRatingOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseRatingOutputVoltage.setStatus(_A)
_UpsThreePhaseRatingOutputFrequency_Type=Integer32
_UpsThreePhaseRatingOutputFrequency_Object=MibScalar
upsThreePhaseRatingOutputFrequency=_UpsThreePhaseRatingOutputFrequency_Object((1,3,6,1,4,1,935,1,1,1,8,8,6),_UpsThreePhaseRatingOutputFrequency_Type())
upsThreePhaseRatingOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseRatingOutputFrequency.setStatus(_A)
_UpsThreePhaseRatingBatteryVoltage_Type=Integer32
_UpsThreePhaseRatingBatteryVoltage_Object=MibScalar
upsThreePhaseRatingBatteryVoltage=_UpsThreePhaseRatingBatteryVoltage_Object((1,3,6,1,4,1,935,1,1,1,8,8,7),_UpsThreePhaseRatingBatteryVoltage_Type())
upsThreePhaseRatingBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseRatingBatteryVoltage.setStatus(_A)
_UpsThreePhaseRatingPower_Type=DisplayString
_UpsThreePhaseRatingPower_Object=MibScalar
upsThreePhaseRatingPower=_UpsThreePhaseRatingPower_Object((1,3,6,1,4,1,935,1,1,1,8,8,8),_UpsThreePhaseRatingPower_Type())
upsThreePhaseRatingPower.setMaxAccess(_B)
if mibBuilder.loadTexts:upsThreePhaseRatingPower.setStatus(_A)
_UpsEnvironment_ObjectIdentity=ObjectIdentity
upsEnvironment=_UpsEnvironment_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,9))
_UpsEnvStatus_ObjectIdentity=ObjectIdentity
upsEnvStatus=_UpsEnvStatus_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,9,1))
_UpsEnvTemperature_Type=Integer32
_UpsEnvTemperature_Object=MibScalar
upsEnvTemperature=_UpsEnvTemperature_Object((1,3,6,1,4,1,935,1,1,1,9,1,1),_UpsEnvTemperature_Type())
upsEnvTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvTemperature.setStatus(_A)
_UpsEnvHumidity_Type=Integer32
_UpsEnvHumidity_Object=MibScalar
upsEnvHumidity=_UpsEnvHumidity_Object((1,3,6,1,4,1,935,1,1,1,9,1,2),_UpsEnvHumidity_Type())
upsEnvHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvHumidity.setStatus(_A)
class _UpsEnvWater_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsEnvWater_Type.__name__=_C
_UpsEnvWater_Object=MibScalar
upsEnvWater=_UpsEnvWater_Object((1,3,6,1,4,1,935,1,1,1,9,1,3),_UpsEnvWater_Type())
upsEnvWater.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvWater.setStatus(_A)
class _UpsEnvSmoke_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsEnvSmoke_Type.__name__=_C
_UpsEnvSmoke_Object=MibScalar
upsEnvSmoke=_UpsEnvSmoke_Object((1,3,6,1,4,1,935,1,1,1,9,1,4),_UpsEnvSmoke_Type())
upsEnvSmoke.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvSmoke.setStatus(_A)
class _UpsEnvSecurity1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsEnvSecurity1_Type.__name__=_C
_UpsEnvSecurity1_Object=MibScalar
upsEnvSecurity1=_UpsEnvSecurity1_Object((1,3,6,1,4,1,935,1,1,1,9,1,5),_UpsEnvSecurity1_Type())
upsEnvSecurity1.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvSecurity1.setStatus(_A)
class _UpsEnvSecurity2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsEnvSecurity2_Type.__name__=_C
_UpsEnvSecurity2_Object=MibScalar
upsEnvSecurity2=_UpsEnvSecurity2_Object((1,3,6,1,4,1,935,1,1,1,9,1,6),_UpsEnvSecurity2_Type())
upsEnvSecurity2.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvSecurity2.setStatus(_A)
class _UpsEnvSecurity3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsEnvSecurity3_Type.__name__=_C
_UpsEnvSecurity3_Object=MibScalar
upsEnvSecurity3=_UpsEnvSecurity3_Object((1,3,6,1,4,1,935,1,1,1,9,1,7),_UpsEnvSecurity3_Type())
upsEnvSecurity3.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvSecurity3.setStatus(_A)
class _UpsEnvSecurity4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsEnvSecurity4_Type.__name__=_C
_UpsEnvSecurity4_Object=MibScalar
upsEnvSecurity4=_UpsEnvSecurity4_Object((1,3,6,1,4,1,935,1,1,1,9,1,8),_UpsEnvSecurity4_Type())
upsEnvSecurity4.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvSecurity4.setStatus(_A)
class _UpsEnvSecurity5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsEnvSecurity5_Type.__name__=_C
_UpsEnvSecurity5_Object=MibScalar
upsEnvSecurity5=_UpsEnvSecurity5_Object((1,3,6,1,4,1,935,1,1,1,9,1,9),_UpsEnvSecurity5_Type())
upsEnvSecurity5.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvSecurity5.setStatus(_A)
class _UpsEnvSecurity6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsEnvSecurity6_Type.__name__=_C
_UpsEnvSecurity6_Object=MibScalar
upsEnvSecurity6=_UpsEnvSecurity6_Object((1,3,6,1,4,1,935,1,1,1,9,1,10),_UpsEnvSecurity6_Type())
upsEnvSecurity6.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvSecurity6.setStatus(_A)
class _UpsEnvSecurity7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpsEnvSecurity7_Type.__name__=_C
_UpsEnvSecurity7_Object=MibScalar
upsEnvSecurity7=_UpsEnvSecurity7_Object((1,3,6,1,4,1,935,1,1,1,9,1,11),_UpsEnvSecurity7_Type())
upsEnvSecurity7.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEnvSecurity7.setStatus(_A)
_UpsEnvSetting_ObjectIdentity=ObjectIdentity
upsEnvSetting=_UpsEnvSetting_ObjectIdentity((1,3,6,1,4,1,935,1,1,1,9,2))
_UpsEnvOverTemperature_Type=Integer32
_UpsEnvOverTemperature_Object=MibScalar
upsEnvOverTemperature=_UpsEnvOverTemperature_Object((1,3,6,1,4,1,935,1,1,1,9,2,1),_UpsEnvOverTemperature_Type())
upsEnvOverTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEnvOverTemperature.setStatus(_A)
_UpsEnvUnderTemperature_Type=Integer32
_UpsEnvUnderTemperature_Object=MibScalar
upsEnvUnderTemperature=_UpsEnvUnderTemperature_Object((1,3,6,1,4,1,935,1,1,1,9,2,2),_UpsEnvUnderTemperature_Type())
upsEnvUnderTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEnvUnderTemperature.setStatus(_A)
_UpsEnvOverHumidity_Type=Integer32
_UpsEnvOverHumidity_Object=MibScalar
upsEnvOverHumidity=_UpsEnvOverHumidity_Object((1,3,6,1,4,1,935,1,1,1,9,2,3),_UpsEnvOverHumidity_Type())
upsEnvOverHumidity.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEnvOverHumidity.setStatus(_A)
_UpsEnvUnderHumidity_Type=Integer32
_UpsEnvUnderHumidity_Object=MibScalar
upsEnvUnderHumidity=_UpsEnvUnderHumidity_Object((1,3,6,1,4,1,935,1,1,1,9,2,4),_UpsEnvUnderHumidity_Type())
upsEnvUnderHumidity.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEnvUnderHumidity.setStatus(_A)
_Ppcmgmt_ObjectIdentity=ObjectIdentity
ppcmgmt=_Ppcmgmt_ObjectIdentity((1,3,6,1,4,1,935,2))
_Mconfig_ObjectIdentity=ObjectIdentity
mconfig=_Mconfig_ObjectIdentity((1,3,6,1,4,1,935,2,1))
_MconfigTrapsReceiversNum_Type=Integer32
_MconfigTrapsReceiversNum_Object=MibScalar
mconfigTrapsReceiversNum=_MconfigTrapsReceiversNum_Object((1,3,6,1,4,1,935,2,1,1),_MconfigTrapsReceiversNum_Type())
mconfigTrapsReceiversNum.setMaxAccess(_B)
if mibBuilder.loadTexts:mconfigTrapsReceiversNum.setStatus(_A)
_MconfigTrapsReceiversTable_Object=MibTable
mconfigTrapsReceiversTable=_MconfigTrapsReceiversTable_Object((1,3,6,1,4,1,935,2,1,2))
if mibBuilder.loadTexts:mconfigTrapsReceiversTable.setStatus(_A)
_MconfigTrapsReceiversEntry_Object=MibTableRow
mconfigTrapsReceiversEntry=_MconfigTrapsReceiversEntry_Object((1,3,6,1,4,1,935,2,1,2,1))
mconfigTrapsReceiversEntry.setIndexNames((0,_J,_O))
if mibBuilder.loadTexts:mconfigTrapsReceiversEntry.setStatus(_A)
_TrapsIndex_Type=Integer32
_TrapsIndex_Object=MibTableColumn
trapsIndex=_TrapsIndex_Object((1,3,6,1,4,1,935,2,1,2,1,1),_TrapsIndex_Type())
trapsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trapsIndex.setStatus(_A)
_TrapsReceiverAddr_Type=IpAddress
_TrapsReceiverAddr_Object=MibTableColumn
trapsReceiverAddr=_TrapsReceiverAddr_Object((1,3,6,1,4,1,935,2,1,2,1,2),_TrapsReceiverAddr_Type())
trapsReceiverAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:trapsReceiverAddr.setStatus(_A)
_ReceiverCommunityString_Type=DisplayString
_ReceiverCommunityString_Object=MibTableColumn
receiverCommunityString=_ReceiverCommunityString_Object((1,3,6,1,4,1,935,2,1,2,1,3),_ReceiverCommunityString_Type())
receiverCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:receiverCommunityString.setStatus(_A)
class _SeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('information',1),('warning',2),('severe',3)))
_SeverityLevel_Type.__name__=_C
_SeverityLevel_Object=MibTableColumn
severityLevel=_SeverityLevel_Object((1,3,6,1,4,1,935,2,1,2,1,4),_SeverityLevel_Type())
severityLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:severityLevel.setStatus(_A)
class _ReceiverAccept_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_ReceiverAccept_Type.__name__=_C
_ReceiverAccept_Object=MibTableColumn
receiverAccept=_ReceiverAccept_Object((1,3,6,1,4,1,935,2,1,2,1,5),_ReceiverAccept_Type())
receiverAccept.setMaxAccess(_D)
if mibBuilder.loadTexts:receiverAccept.setStatus(_A)
communicationLost=NotificationType((1,3,6,1,4,1,935,0,1))
if mibBuilder.loadTexts:communicationLost.setStatus('')
upsOverLoad=NotificationType((1,3,6,1,4,1,935,0,2))
if mibBuilder.loadTexts:upsOverLoad.setStatus('')
upsDiagnosticsFailed=NotificationType((1,3,6,1,4,1,935,0,3))
if mibBuilder.loadTexts:upsDiagnosticsFailed.setStatus('')
upsDischarged=NotificationType((1,3,6,1,4,1,935,0,4))
if mibBuilder.loadTexts:upsDischarged.setStatus('')
upsOnBattery=NotificationType((1,3,6,1,4,1,935,0,5))
if mibBuilder.loadTexts:upsOnBattery.setStatus('')
boostOn=NotificationType((1,3,6,1,4,1,935,0,6))
if mibBuilder.loadTexts:boostOn.setStatus('')
lowBattery=NotificationType((1,3,6,1,4,1,935,0,7))
if mibBuilder.loadTexts:lowBattery.setStatus('')
communicationEstablished=NotificationType((1,3,6,1,4,1,935,0,8))
if mibBuilder.loadTexts:communicationEstablished.setStatus('')
powerRestored=NotificationType((1,3,6,1,4,1,935,0,9))
if mibBuilder.loadTexts:powerRestored.setStatus('')
upsDiagnosticsPassed=NotificationType((1,3,6,1,4,1,935,0,10))
if mibBuilder.loadTexts:upsDiagnosticsPassed.setStatus('')
returnFromLowBattery=NotificationType((1,3,6,1,4,1,935,0,11))
if mibBuilder.loadTexts:returnFromLowBattery.setStatus('')
upsTurnedOff=NotificationType((1,3,6,1,4,1,935,0,12))
if mibBuilder.loadTexts:upsTurnedOff.setStatus('')
upsSleeping=NotificationType((1,3,6,1,4,1,935,0,13))
if mibBuilder.loadTexts:upsSleeping.setStatus('')
upsWokeUp=NotificationType((1,3,6,1,4,1,935,0,14))
if mibBuilder.loadTexts:upsWokeUp.setStatus('')
upsRebootStarted=NotificationType((1,3,6,1,4,1,935,0,15))
if mibBuilder.loadTexts:upsRebootStarted.setStatus('')
envOverTemperature=NotificationType((1,3,6,1,4,1,935,0,16))
if mibBuilder.loadTexts:envOverTemperature.setStatus('')
envTemperatureNormal=NotificationType((1,3,6,1,4,1,935,0,17))
if mibBuilder.loadTexts:envTemperatureNormal.setStatus('')
envOverHumidity=NotificationType((1,3,6,1,4,1,935,0,18))
if mibBuilder.loadTexts:envOverHumidity.setStatus('')
envHumidityNormal=NotificationType((1,3,6,1,4,1,935,0,19))
if mibBuilder.loadTexts:envHumidityNormal.setStatus('')
envSmokeAbnormal=NotificationType((1,3,6,1,4,1,935,0,20))
if mibBuilder.loadTexts:envSmokeAbnormal.setStatus('')
envWaterAbnormal=NotificationType((1,3,6,1,4,1,935,0,21))
if mibBuilder.loadTexts:envWaterAbnormal.setStatus('')
envSecurityAbnormal=NotificationType((1,3,6,1,4,1,935,0,22))
if mibBuilder.loadTexts:envSecurityAbnormal.setStatus('')
envWaterNormal=NotificationType((1,3,6,1,4,1,935,0,24))
if mibBuilder.loadTexts:envWaterNormal.setStatus('')
envGasAbnormal=NotificationType((1,3,6,1,4,1,935,0,26))
if mibBuilder.loadTexts:envGasAbnormal.setStatus('')
upsTemp=NotificationType((1,3,6,1,4,1,935,0,27))
if mibBuilder.loadTexts:upsTemp.setStatus('')
upsLoadNormal=NotificationType((1,3,6,1,4,1,935,0,28))
if mibBuilder.loadTexts:upsLoadNormal.setStatus('')
upsTempNormal=NotificationType((1,3,6,1,4,1,935,0,29))
if mibBuilder.loadTexts:upsTempNormal.setStatus('')
envUnderTemperature=NotificationType((1,3,6,1,4,1,935,0,30))
if mibBuilder.loadTexts:envUnderTemperature.setStatus('')
envUnderHumidity=NotificationType((1,3,6,1,4,1,935,0,31))
if mibBuilder.loadTexts:envUnderHumidity.setStatus('')
upsBypass=NotificationType((1,3,6,1,4,1,935,0,32))
if mibBuilder.loadTexts:upsBypass.setStatus('')
envSecurity1=NotificationType((1,3,6,1,4,1,935,0,33))
if mibBuilder.loadTexts:envSecurity1.setStatus('')
envSecurity2=NotificationType((1,3,6,1,4,1,935,0,34))
if mibBuilder.loadTexts:envSecurity2.setStatus('')
envSecurity3=NotificationType((1,3,6,1,4,1,935,0,35))
if mibBuilder.loadTexts:envSecurity3.setStatus('')
envSecurity4=NotificationType((1,3,6,1,4,1,935,0,36))
if mibBuilder.loadTexts:envSecurity4.setStatus('')
envSecurity5=NotificationType((1,3,6,1,4,1,935,0,37))
if mibBuilder.loadTexts:envSecurity5.setStatus('')
envSecurity6=NotificationType((1,3,6,1,4,1,935,0,38))
if mibBuilder.loadTexts:envSecurity6.setStatus('')
envSecurity7=NotificationType((1,3,6,1,4,1,935,0,39))
if mibBuilder.loadTexts:envSecurity7.setStatus('')
upsRecroterror=NotificationType((1,3,6,1,4,1,935,0,47))
if mibBuilder.loadTexts:upsRecroterror.setStatus('')
upsBypassFreFail=NotificationType((1,3,6,1,4,1,935,0,48))
if mibBuilder.loadTexts:upsBypassFreFail.setStatus('')
upsBypassacnormal=NotificationType((1,3,6,1,4,1,935,0,49))
if mibBuilder.loadTexts:upsBypassacnormal.setStatus('')
upsBypassacabnormal=NotificationType((1,3,6,1,4,1,935,0,50))
if mibBuilder.loadTexts:upsBypassacabnormal.setStatus('')
upsTest=NotificationType((1,3,6,1,4,1,935,0,51))
if mibBuilder.loadTexts:upsTest.setStatus('')
upsScheduleShutdown=NotificationType((1,3,6,1,4,1,935,0,52))
if mibBuilder.loadTexts:upsScheduleShutdown.setStatus('')
upsBypassReturn=NotificationType((1,3,6,1,4,1,935,0,53))
if mibBuilder.loadTexts:upsBypassReturn.setStatus('')
upsShortCircuitShutdown=NotificationType((1,3,6,1,4,1,935,0,54))
if mibBuilder.loadTexts:upsShortCircuitShutdown.setStatus('')
upsInverterOutputFailShutdown=NotificationType((1,3,6,1,4,1,935,0,55))
if mibBuilder.loadTexts:upsInverterOutputFailShutdown.setStatus('')
upsBypassBreadkerOnShutdown=NotificationType((1,3,6,1,4,1,935,0,56))
if mibBuilder.loadTexts:upsBypassBreadkerOnShutdown.setStatus('')
upsHighDCShutdown=NotificationType((1,3,6,1,4,1,935,0,57))
if mibBuilder.loadTexts:upsHighDCShutdown.setStatus('')
upsEmergencyStop=NotificationType((1,3,6,1,4,1,935,0,58))
if mibBuilder.loadTexts:upsEmergencyStop.setStatus('')
upsInverterMode=NotificationType((1,3,6,1,4,1,935,0,59))
if mibBuilder.loadTexts:upsInverterMode.setStatus('')
upsBypassMode=NotificationType((1,3,6,1,4,1,935,0,60))
if mibBuilder.loadTexts:upsBypassMode.setStatus('')
upsOverTemperatureShutdown=NotificationType((1,3,6,1,4,1,935,0,61))
if mibBuilder.loadTexts:upsOverTemperatureShutdown.setStatus('')
upsOverLoadShutdown=NotificationType((1,3,6,1,4,1,935,0,62))
if mibBuilder.loadTexts:upsOverLoadShutdown.setStatus('')
upsCapacityUnderrun=NotificationType((1,3,6,1,4,1,935,0,63))
if mibBuilder.loadTexts:upsCapacityUnderrun.setStatus('')
upsCapacityNormal=NotificationType((1,3,6,1,4,1,935,0,64))
if mibBuilder.loadTexts:upsCapacityNormal.setStatus('')
upsLowBatteryShutdown=NotificationType((1,3,6,1,4,1,935,0,67))
if mibBuilder.loadTexts:upsLowBatteryShutdown.setStatus('')
buckOn=NotificationType((1,3,6,1,4,1,935,0,68))
if mibBuilder.loadTexts:buckOn.setStatus('')
returnFromBuck=NotificationType((1,3,6,1,4,1,935,0,69))
if mibBuilder.loadTexts:returnFromBuck.setStatus('')
returnFromBoost=NotificationType((1,3,6,1,4,1,935,0,70))
if mibBuilder.loadTexts:returnFromBoost.setStatus('')
mibBuilder.exportSymbols(_J,**{'ppc':ppc,'communicationLost':communicationLost,'upsOverLoad':upsOverLoad,'upsDiagnosticsFailed':upsDiagnosticsFailed,'upsDischarged':upsDischarged,'upsOnBattery':upsOnBattery,'boostOn':boostOn,'lowBattery':lowBattery,'communicationEstablished':communicationEstablished,'powerRestored':powerRestored,'upsDiagnosticsPassed':upsDiagnosticsPassed,'returnFromLowBattery':returnFromLowBattery,'upsTurnedOff':upsTurnedOff,'upsSleeping':upsSleeping,'upsWokeUp':upsWokeUp,'upsRebootStarted':upsRebootStarted,'envOverTemperature':envOverTemperature,'envTemperatureNormal':envTemperatureNormal,'envOverHumidity':envOverHumidity,'envHumidityNormal':envHumidityNormal,'envSmokeAbnormal':envSmokeAbnormal,'envWaterAbnormal':envWaterAbnormal,'envSecurityAbnormal':envSecurityAbnormal,'envWaterNormal':envWaterNormal,'envGasAbnormal':envGasAbnormal,'upsTemp':upsTemp,'upsLoadNormal':upsLoadNormal,'upsTempNormal':upsTempNormal,'envUnderTemperature':envUnderTemperature,'envUnderHumidity':envUnderHumidity,'upsBypass':upsBypass,'envSecurity1':envSecurity1,'envSecurity2':envSecurity2,'envSecurity3':envSecurity3,'envSecurity4':envSecurity4,'envSecurity5':envSecurity5,'envSecurity6':envSecurity6,'envSecurity7':envSecurity7,'upsRecroterror':upsRecroterror,'upsBypassFreFail':upsBypassFreFail,'upsBypassacnormal':upsBypassacnormal,'upsBypassacabnormal':upsBypassacabnormal,'upsTest':upsTest,'upsScheduleShutdown':upsScheduleShutdown,'upsBypassReturn':upsBypassReturn,'upsShortCircuitShutdown':upsShortCircuitShutdown,'upsInverterOutputFailShutdown':upsInverterOutputFailShutdown,'upsBypassBreadkerOnShutdown':upsBypassBreadkerOnShutdown,'upsHighDCShutdown':upsHighDCShutdown,'upsEmergencyStop':upsEmergencyStop,'upsInverterMode':upsInverterMode,'upsBypassMode':upsBypassMode,'upsOverTemperatureShutdown':upsOverTemperatureShutdown,'upsOverLoadShutdown':upsOverLoadShutdown,'upsCapacityUnderrun':upsCapacityUnderrun,'upsCapacityNormal':upsCapacityNormal,'upsLowBatteryShutdown':upsLowBatteryShutdown,'buckOn':buckOn,'returnFromBuck':returnFromBuck,'returnFromBoost':returnFromBoost,'products':products,'hardware':hardware,'ups':ups,'upsIdentp':upsIdentp,'upsBaseIdent':upsBaseIdent,'upsBaseIdentModel':upsBaseIdentModel,'upsBaseIdentUpsName':upsBaseIdentUpsName,'upsSmartIdent':upsSmartIdent,'upsSmartIdentFirmwareRevision':upsSmartIdentFirmwareRevision,'upsSmartIdentDateOfManufacture':upsSmartIdentDateOfManufacture,'upsSmartIdentUpsSerialNumber':upsSmartIdentUpsSerialNumber,'upsSmartIdentAgentFirmwareRevision':upsSmartIdentAgentFirmwareRevision,'upsBatteryp':upsBatteryp,'upsBaseBattery':upsBaseBattery,'upsBaseBatteryStatus':upsBaseBatteryStatus,'upsBaseBatteryTimeOnBattery':upsBaseBatteryTimeOnBattery,'upsBaseBatteryLastReplaceDate':upsBaseBatteryLastReplaceDate,'upsSmartBattery':upsSmartBattery,'upsSmartBatteryCapacity':upsSmartBatteryCapacity,'upsSmartBatteryVoltage':upsSmartBatteryVoltage,'upsSmartBatteryTemperature':upsSmartBatteryTemperature,'upsSmartBatteryRunTimeRemaining':upsSmartBatteryRunTimeRemaining,'upsSmartBatteryReplaceIndicator':upsSmartBatteryReplaceIndicator,'upsSmartBatteryFullChargeVoltage':upsSmartBatteryFullChargeVoltage,'upsSmartBatteryCurrent':upsSmartBatteryCurrent,'upsInputp':upsInputp,'upsBaseInput':upsBaseInput,'upsBaseInputPhase':upsBaseInputPhase,'upsSmartInput':upsSmartInput,'upsSmartInputLineVoltage':upsSmartInputLineVoltage,'upsSmartInputMaxLineVoltage':upsSmartInputMaxLineVoltage,'upsSmartInputMinLineVoltage':upsSmartInputMinLineVoltage,'upsSmartInputFrequency':upsSmartInputFrequency,'upsSmartInputLineFailCause':upsSmartInputLineFailCause,'upsOutputp':upsOutputp,'upsBaseOutput':upsBaseOutput,'upsBaseOutputStatus':upsBaseOutputStatus,'upsBaseOutputPhase':upsBaseOutputPhase,'upsSmartOutput':upsSmartOutput,'upsSmartOutputVoltage':upsSmartOutputVoltage,'upsSmartOutputFrequency':upsSmartOutputFrequency,'upsSmartOutputLoad':upsSmartOutputLoad,'upsConfigp':upsConfigp,'upsBaseConfig':upsBaseConfig,'upsBaseConfigNumDevices':upsBaseConfigNumDevices,'upsBaseConfigDeviceTable':upsBaseConfigDeviceTable,'upsBaseConfigDeviceEntry':upsBaseConfigDeviceEntry,_L:indexOfDevice,'nameOfDevice':nameOfDevice,'vaRatingOfDevice':vaRatingOfDevice,'deviceAccept':deviceAccept,'upsSmartConfig':upsSmartConfig,'upsSmartConfigRatedOutputVoltage':upsSmartConfigRatedOutputVoltage,'upsSmartConfigHighTransferVolt':upsSmartConfigHighTransferVolt,'upsSmartConfigLowTransferVolt':upsSmartConfigLowTransferVolt,'upsSmartConfigAlarm':upsSmartConfigAlarm,'upsSmartConfigAlarmTimer':upsSmartConfigAlarmTimer,'upsSmartConfigMinReturnCapacity':upsSmartConfigMinReturnCapacity,'upsSmartConfigSensitivity':upsSmartConfigSensitivity,'upsSmartConfigLowBatteryRunTime':upsSmartConfigLowBatteryRunTime,'upsSmartConfigReturnDelay':upsSmartConfigReturnDelay,'upsSmartConfigShutoffDelay':upsSmartConfigShutoffDelay,'upsSmartConfigUpsSleepTime':upsSmartConfigUpsSleepTime,'upsSmartConfigSetEEPROMDefaults':upsSmartConfigSetEEPROMDefaults,'upsControlp':upsControlp,'upsBaseControl':upsBaseControl,'upsBaseControlConserveBattery':upsBaseControlConserveBattery,'upsSmartControl':upsSmartControl,'upsSmartControlUpsOff':upsSmartControlUpsOff,'upsSmartControlRebootUps':upsSmartControlRebootUps,'upsSmartControlUpsSleep':upsSmartControlUpsSleep,'upsSmartControlSimulatePowerFail':upsSmartControlSimulatePowerFail,'upsSmartControlFlashAndBeep':upsSmartControlFlashAndBeep,_M:upsSmartControlTurnOnUpsLoad,'upsTestp':upsTestp,'upsBaseTest':upsBaseTest,'upsSmartTest':upsSmartTest,'upsSmartTestDiagnosticSchedule':upsSmartTestDiagnosticSchedule,'upsSmartTestDiagnostics':upsSmartTestDiagnostics,'upsSmartTestDiagnosticsResults':upsSmartTestDiagnosticsResults,'upsSmartTestLastDiagnosticsDate':upsSmartTestLastDiagnosticsDate,'upsSmartTestIndicators':upsSmartTestIndicators,'upsSmartTestRuntimeCalibration':upsSmartTestRuntimeCalibration,'upsSmartTestCalibrationResults':upsSmartTestCalibrationResults,'upsSmartTestCalibrationDate':upsSmartTestCalibrationDate,'upsThreePhase':upsThreePhase,'upsThreePhaseBatteryGrp':upsThreePhaseBatteryGrp,'upsThreePhaseBatteryVoltage':upsThreePhaseBatteryVoltage,'upsThreePhaseBatteryCapacityPercentage':upsThreePhaseBatteryCapacityPercentage,'upsThreePhaseBatteryTimeRemain':upsThreePhaseBatteryTimeRemain,'upsThreePhaseBatteryCurrent':upsThreePhaseBatteryCurrent,'upsThreePhaseBatteryTemperature':upsThreePhaseBatteryTemperature,'upsThreePhaseInputGrp':upsThreePhaseInputGrp,'upsThreePhaseInputFrequency':upsThreePhaseInputFrequency,'upsThreePhaseInputVoltageR':upsThreePhaseInputVoltageR,'upsThreePhaseInputVoltageS':upsThreePhaseInputVoltageS,'upsThreePhaseInputVoltageT':upsThreePhaseInputVoltageT,'upsThreePhaseOutputGrp':upsThreePhaseOutputGrp,'upsThreePhaseOutputFrequency':upsThreePhaseOutputFrequency,'upsThreePhaseOutputVoltageR':upsThreePhaseOutputVoltageR,'upsThreePhaseOutputVoltageS':upsThreePhaseOutputVoltageS,'upsThreePhaseOutputVoltageT':upsThreePhaseOutputVoltageT,'upsThreePhaseOutputLoadPercentageR':upsThreePhaseOutputLoadPercentageR,'upsThreePhaseOutputLoadPercentageS':upsThreePhaseOutputLoadPercentageS,'upsThreePhaseOutputLoadPercentageT':upsThreePhaseOutputLoadPercentageT,'upsThreePhaseBypassGrp':upsThreePhaseBypassGrp,'upsThreePhaseBypassSourceFrequency':upsThreePhaseBypassSourceFrequency,'upsThreePhaseBypassSourceVoltageR':upsThreePhaseBypassSourceVoltageR,'upsThreePhaseBypassSourceVoltageS':upsThreePhaseBypassSourceVoltageS,'upsThreePhaseBypassSourceVoltageT':upsThreePhaseBypassSourceVoltageT,'upsThreePhaseDCandRectifierStatusGrp':upsThreePhaseDCandRectifierStatusGrp,'upsThreePhaseDCandRectifierStatusRecRotError':upsThreePhaseDCandRectifierStatusRecRotError,'upsThreePhaseDCandRectifierStatusLowBatteryShutdown':upsThreePhaseDCandRectifierStatusLowBatteryShutdown,'upsThreePhaseDCandRectifierStatusLowBattery':upsThreePhaseDCandRectifierStatusLowBattery,'upsThreePhaseDCandRectifierStatusInAndOut':upsThreePhaseDCandRectifierStatusInAndOut,'upsThreePhaseDCandRectifierStatusBatteryStatus':upsThreePhaseDCandRectifierStatusBatteryStatus,'upsThreePhaseDCandRectifierStatusChargeStatus':upsThreePhaseDCandRectifierStatusChargeStatus,'upsThreePhaseDCandRectifierStatusRecOperating':upsThreePhaseDCandRectifierStatusRecOperating,'upsThreePhaseUPSStatusGrp':upsThreePhaseUPSStatusGrp,'upsThreePhaseUPSStatusBypassFreqFail':upsThreePhaseUPSStatusBypassFreqFail,'upsThreePhaseUPSStatusManualBypassBreaker':upsThreePhaseUPSStatusManualBypassBreaker,'upsThreePhaseUPSStatusACStatus':upsThreePhaseUPSStatusACStatus,'upsThreePhaseUPSStaticSwitchMode':upsThreePhaseUPSStaticSwitchMode,'upsThreePhaseUPSStatusInverterOperating':upsThreePhaseUPSStatusInverterOperating,'upsThreePhaseFaultStatusGrp':upsThreePhaseFaultStatusGrp,'upsThreePhaseFaultStatusEmergencyStop':upsThreePhaseFaultStatusEmergencyStop,'upsThreePhaseFaultStatusHighDCShutdown':upsThreePhaseFaultStatusHighDCShutdown,'upsThreePhaseFaultStatusBypassBreaker':upsThreePhaseFaultStatusBypassBreaker,'upsThreePhaseFaultStatusOverLoad':upsThreePhaseFaultStatusOverLoad,'upsThreePhaseFaultStatusInverterOutputFail':upsThreePhaseFaultStatusInverterOutputFail,'upsThreePhaseFaultStatusOverTemperature':upsThreePhaseFaultStatusOverTemperature,'upsThreePhaseFaultStatusShortCircuit':upsThreePhaseFaultStatusShortCircuit,'upsThreePhaseRatingGrp':upsThreePhaseRatingGrp,'upsThreePhaseRatingRectifierVoltage':upsThreePhaseRatingRectifierVoltage,'upsThreePhaseRatingRectifierFrequency':upsThreePhaseRatingRectifierFrequency,'upsThreePhaseRatingBypassVoltage':upsThreePhaseRatingBypassVoltage,'upsThreePhaseRatingBypassFrequency':upsThreePhaseRatingBypassFrequency,'upsThreePhaseRatingOutputVoltage':upsThreePhaseRatingOutputVoltage,'upsThreePhaseRatingOutputFrequency':upsThreePhaseRatingOutputFrequency,'upsThreePhaseRatingBatteryVoltage':upsThreePhaseRatingBatteryVoltage,'upsThreePhaseRatingPower':upsThreePhaseRatingPower,'upsEnvironment':upsEnvironment,'upsEnvStatus':upsEnvStatus,'upsEnvTemperature':upsEnvTemperature,'upsEnvHumidity':upsEnvHumidity,'upsEnvWater':upsEnvWater,'upsEnvSmoke':upsEnvSmoke,'upsEnvSecurity1':upsEnvSecurity1,'upsEnvSecurity2':upsEnvSecurity2,'upsEnvSecurity3':upsEnvSecurity3,'upsEnvSecurity4':upsEnvSecurity4,'upsEnvSecurity5':upsEnvSecurity5,'upsEnvSecurity6':upsEnvSecurity6,'upsEnvSecurity7':upsEnvSecurity7,'upsEnvSetting':upsEnvSetting,'upsEnvOverTemperature':upsEnvOverTemperature,'upsEnvUnderTemperature':upsEnvUnderTemperature,'upsEnvOverHumidity':upsEnvOverHumidity,'upsEnvUnderHumidity':upsEnvUnderHumidity,'ppcmgmt':ppcmgmt,'mconfig':mconfig,'mconfigTrapsReceiversNum':mconfigTrapsReceiversNum,'mconfigTrapsReceiversTable':mconfigTrapsReceiversTable,'mconfigTrapsReceiversEntry':mconfigTrapsReceiversEntry,_O:trapsIndex,'trapsReceiverAddr':trapsReceiverAddr,'receiverCommunityString':receiverCommunityString,'severityLevel':severityLevel,'receiverAccept':receiverAccept})