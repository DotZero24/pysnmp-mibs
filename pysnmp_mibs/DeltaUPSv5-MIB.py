_g='dupsPMID'
_f='inProgress'
_e='0.1 Amp DC'
_d='disable'
_c='enable'
_b='NotificationType'
_a='inactive'
_Z='active'
_Y='Second'
_X='warning'
_W='1 Degrees Centigrade'
_V='0.1 Hertz'
_U='1 Percent'
_T='1 Degree Celsius'
_S='Volt'
_R='close'
_Q='open'
_P='DisplayString'
_O='1 Watt'
_N='0.1 Amp'
_M='1 kWh'
_L='0.1 Volt'
_K='read-write'
_J='alarm'
_I='normal'
_H='off'
_G='on'
_F='dupsDescription'
_E='dupsTimeTicks'
_D='Integer32'
_C='DeltaUPSv5-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_b,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_b,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention')
_Delta_ObjectIdentity=ObjectIdentity
delta=_Delta_ObjectIdentity((1,3,6,1,4,1,2254))
_Ups_ObjectIdentity=ObjectIdentity
ups=_Ups_ObjectIdentity((1,3,6,1,4,1,2254,2))
_Upsv5_ObjectIdentity=ObjectIdentity
upsv5=_Upsv5_ObjectIdentity((1,3,6,1,4,1,2254,2,5))
_DupsIdent_ObjectIdentity=ObjectIdentity
dupsIdent=_DupsIdent_ObjectIdentity((1,3,6,1,4,1,2254,2,5,1))
class _DupsIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DupsIdentManufacturer_Type.__name__=_P
_DupsIdentManufacturer_Object=MibScalar
dupsIdentManufacturer=_DupsIdentManufacturer_Object((1,3,6,1,4,1,2254,2,5,1,1),_DupsIdentManufacturer_Type())
dupsIdentManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsIdentManufacturer.setStatus(_A)
class _DupsIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_DupsIdentModel_Type.__name__=_P
_DupsIdentModel_Object=MibScalar
dupsIdentModel=_DupsIdentModel_Object((1,3,6,1,4,1,2254,2,5,1,2),_DupsIdentModel_Type())
dupsIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsIdentModel.setStatus(_A)
class _DupsIdentUPSSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_DupsIdentUPSSoftwareVersion_Type.__name__=_P
_DupsIdentUPSSoftwareVersion_Object=MibScalar
dupsIdentUPSSoftwareVersion=_DupsIdentUPSSoftwareVersion_Object((1,3,6,1,4,1,2254,2,5,1,3),_DupsIdentUPSSoftwareVersion_Type())
dupsIdentUPSSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsIdentUPSSoftwareVersion.setStatus(_A)
class _DupsIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_DupsIdentAgentSoftwareVersion_Type.__name__=_P
_DupsIdentAgentSoftwareVersion_Object=MibScalar
dupsIdentAgentSoftwareVersion=_DupsIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,2254,2,5,1,4),_DupsIdentAgentSoftwareVersion_Type())
dupsIdentAgentSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsIdentAgentSoftwareVersion.setStatus(_A)
class _DupsIdentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_DupsIdentName_Type.__name__=_P
_DupsIdentName_Object=MibScalar
dupsIdentName=_DupsIdentName_Object((1,3,6,1,4,1,2254,2,5,1,5),_DupsIdentName_Type())
dupsIdentName.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsIdentName.setStatus(_A)
class _DupsAttachedDevices_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_DupsAttachedDevices_Type.__name__=_P
_DupsAttachedDevices_Object=MibScalar
dupsAttachedDevices=_DupsAttachedDevices_Object((1,3,6,1,4,1,2254,2,5,1,6),_DupsAttachedDevices_Type())
dupsAttachedDevices.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsAttachedDevices.setStatus(_A)
_DupsRatingOutputVA_Type=Integer32
_DupsRatingOutputVA_Object=MibScalar
dupsRatingOutputVA=_DupsRatingOutputVA_Object((1,3,6,1,4,1,2254,2,5,1,7),_DupsRatingOutputVA_Type())
dupsRatingOutputVA.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsRatingOutputVA.setStatus(_A)
if mibBuilder.loadTexts:dupsRatingOutputVA.setUnits('VA')
_DupsRatingOutputVoltage_Type=Integer32
_DupsRatingOutputVoltage_Object=MibScalar
dupsRatingOutputVoltage=_DupsRatingOutputVoltage_Object((1,3,6,1,4,1,2254,2,5,1,8),_DupsRatingOutputVoltage_Type())
dupsRatingOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsRatingOutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:dupsRatingOutputVoltage.setUnits(_S)
_DupsRatingOutputFrequency_Type=Integer32
_DupsRatingOutputFrequency_Object=MibScalar
dupsRatingOutputFrequency=_DupsRatingOutputFrequency_Object((1,3,6,1,4,1,2254,2,5,1,9),_DupsRatingOutputFrequency_Type())
dupsRatingOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsRatingOutputFrequency.setStatus(_A)
if mibBuilder.loadTexts:dupsRatingOutputFrequency.setUnits('Hz')
_DupsRatingInputVoltage_Type=Integer32
_DupsRatingInputVoltage_Object=MibScalar
dupsRatingInputVoltage=_DupsRatingInputVoltage_Object((1,3,6,1,4,1,2254,2,5,1,10),_DupsRatingInputVoltage_Type())
dupsRatingInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsRatingInputVoltage.setStatus(_A)
if mibBuilder.loadTexts:dupsRatingInputVoltage.setUnits(_S)
_DupsRatingInputFrequency_Type=Integer32
_DupsRatingInputFrequency_Object=MibScalar
dupsRatingInputFrequency=_DupsRatingInputFrequency_Object((1,3,6,1,4,1,2254,2,5,1,11),_DupsRatingInputFrequency_Type())
dupsRatingInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsRatingInputFrequency.setStatus(_A)
if mibBuilder.loadTexts:dupsRatingInputFrequency.setUnits('Hz')
_DupsRatingBatteryVoltage_Type=Integer32
_DupsRatingBatteryVoltage_Object=MibScalar
dupsRatingBatteryVoltage=_DupsRatingBatteryVoltage_Object((1,3,6,1,4,1,2254,2,5,1,12),_DupsRatingBatteryVoltage_Type())
dupsRatingBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsRatingBatteryVoltage.setStatus(_A)
if mibBuilder.loadTexts:dupsRatingBatteryVoltage.setUnits(_S)
_DupsLowTransferVoltUpBound_Type=Integer32
_DupsLowTransferVoltUpBound_Object=MibScalar
dupsLowTransferVoltUpBound=_DupsLowTransferVoltUpBound_Object((1,3,6,1,4,1,2254,2,5,1,13),_DupsLowTransferVoltUpBound_Type())
dupsLowTransferVoltUpBound.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsLowTransferVoltUpBound.setStatus(_A)
if mibBuilder.loadTexts:dupsLowTransferVoltUpBound.setUnits(_S)
_DupsLowTransferVoltLowBound_Type=Integer32
_DupsLowTransferVoltLowBound_Object=MibScalar
dupsLowTransferVoltLowBound=_DupsLowTransferVoltLowBound_Object((1,3,6,1,4,1,2254,2,5,1,14),_DupsLowTransferVoltLowBound_Type())
dupsLowTransferVoltLowBound.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsLowTransferVoltLowBound.setStatus(_A)
if mibBuilder.loadTexts:dupsLowTransferVoltLowBound.setUnits(_S)
_DupsHighTransferVoltUpBound_Type=Integer32
_DupsHighTransferVoltUpBound_Object=MibScalar
dupsHighTransferVoltUpBound=_DupsHighTransferVoltUpBound_Object((1,3,6,1,4,1,2254,2,5,1,15),_DupsHighTransferVoltUpBound_Type())
dupsHighTransferVoltUpBound.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsHighTransferVoltUpBound.setStatus(_A)
if mibBuilder.loadTexts:dupsHighTransferVoltUpBound.setUnits(_S)
_DupsHighTransferVoltLowBound_Type=Integer32
_DupsHighTransferVoltLowBound_Object=MibScalar
dupsHighTransferVoltLowBound=_DupsHighTransferVoltLowBound_Object((1,3,6,1,4,1,2254,2,5,1,16),_DupsHighTransferVoltLowBound_Type())
dupsHighTransferVoltLowBound.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsHighTransferVoltLowBound.setStatus(_A)
if mibBuilder.loadTexts:dupsHighTransferVoltLowBound.setUnits(_S)
_DupsLowBattTime_Type=Integer32
_DupsLowBattTime_Object=MibScalar
dupsLowBattTime=_DupsLowBattTime_Object((1,3,6,1,4,1,2254,2,5,1,17),_DupsLowBattTime_Type())
dupsLowBattTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsLowBattTime.setStatus(_A)
if mibBuilder.loadTexts:dupsLowBattTime.setUnits(_Y)
_DupsOutletRelays_Type=Integer32
_DupsOutletRelays_Object=MibScalar
dupsOutletRelays=_DupsOutletRelays_Object((1,3,6,1,4,1,2254,2,5,1,18),_DupsOutletRelays_Type())
dupsOutletRelays.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutletRelays.setStatus(_A)
class _DupsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('on-line',1),('off-line',2),('line-interactive',3),('three-phase',4),('splite-phase',5)))
_DupsType_Type.__name__=_D
_DupsType_Object=MibScalar
dupsType=_DupsType_Object((1,3,6,1,4,1,2254,2,5,1,19),_DupsType_Type())
dupsType.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsType.setStatus(_A)
_DupsControl_ObjectIdentity=ObjectIdentity
dupsControl=_DupsControl_ObjectIdentity((1,3,6,1,4,1,2254,2,5,2))
class _DupsShutdownType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('output',1),('system',2)))
_DupsShutdownType_Type.__name__=_D
_DupsShutdownType_Object=MibScalar
dupsShutdownType=_DupsShutdownType_Object((1,3,6,1,4,1,2254,2,5,2,1),_DupsShutdownType_Type())
dupsShutdownType.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsShutdownType.setStatus(_A)
class _DupsAutoReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAutoReboot_Type.__name__=_D
_DupsAutoReboot_Object=MibScalar
dupsAutoReboot=_DupsAutoReboot_Object((1,3,6,1,4,1,2254,2,5,2,2),_DupsAutoReboot_Type())
dupsAutoReboot.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsAutoReboot.setStatus(_A)
_DupsShutdownAction_Type=Integer32
_DupsShutdownAction_Object=MibScalar
dupsShutdownAction=_DupsShutdownAction_Object((1,3,6,1,4,1,2254,2,5,2,3),_DupsShutdownAction_Type())
dupsShutdownAction.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsShutdownAction.setStatus(_A)
_DupsRestartAction_Type=Integer32
_DupsRestartAction_Object=MibScalar
dupsRestartAction=_DupsRestartAction_Object((1,3,6,1,4,1,2254,2,5,2,4),_DupsRestartAction_Type())
dupsRestartAction.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsRestartAction.setStatus(_A)
_DupsSetOutletRelay_Type=Integer32
_DupsSetOutletRelay_Object=MibScalar
dupsSetOutletRelay=_DupsSetOutletRelay_Object((1,3,6,1,4,1,2254,2,5,2,5),_DupsSetOutletRelay_Type())
dupsSetOutletRelay.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsSetOutletRelay.setStatus(_A)
_DupsRelayOffDelay_Type=Integer32
_DupsRelayOffDelay_Object=MibScalar
dupsRelayOffDelay=_DupsRelayOffDelay_Object((1,3,6,1,4,1,2254,2,5,2,6),_DupsRelayOffDelay_Type())
dupsRelayOffDelay.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsRelayOffDelay.setStatus(_A)
_DupsRelayOnDelay_Type=Integer32
_DupsRelayOnDelay_Object=MibScalar
dupsRelayOnDelay=_DupsRelayOnDelay_Object((1,3,6,1,4,1,2254,2,5,2,7),_DupsRelayOnDelay_Type())
dupsRelayOnDelay.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsRelayOnDelay.setStatus(_A)
_DupsSmartShutdown_Type=Integer32
_DupsSmartShutdown_Object=MibScalar
dupsSmartShutdown=_DupsSmartShutdown_Object((1,3,6,1,4,1,2254,2,5,2,8),_DupsSmartShutdown_Type())
dupsSmartShutdown.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsSmartShutdown.setStatus(_A)
_DupsClearEnergy_Type=Integer32
_DupsClearEnergy_Object=MibScalar
dupsClearEnergy=_DupsClearEnergy_Object((1,3,6,1,4,1,2254,2,5,2,9),_DupsClearEnergy_Type())
dupsClearEnergy.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsClearEnergy.setStatus(_A)
_DupsConfig_ObjectIdentity=ObjectIdentity
dupsConfig=_DupsConfig_ObjectIdentity((1,3,6,1,4,1,2254,2,5,3))
class _DupsConfigBuzzerAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('silence',2)))
_DupsConfigBuzzerAlarm_Type.__name__=_D
_DupsConfigBuzzerAlarm_Object=MibScalar
dupsConfigBuzzerAlarm=_DupsConfigBuzzerAlarm_Object((1,3,6,1,4,1,2254,2,5,3,1),_DupsConfigBuzzerAlarm_Type())
dupsConfigBuzzerAlarm.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigBuzzerAlarm.setStatus(_A)
class _DupsConfigBuzzerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_DupsConfigBuzzerState_Type.__name__=_D
_DupsConfigBuzzerState_Object=MibScalar
dupsConfigBuzzerState=_DupsConfigBuzzerState_Object((1,3,6,1,4,1,2254,2,5,3,2),_DupsConfigBuzzerState_Type())
dupsConfigBuzzerState.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigBuzzerState.setStatus(_A)
class _DupsConfigSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('reduced',2),('low',3)))
_DupsConfigSensitivity_Type.__name__=_D
_DupsConfigSensitivity_Object=MibScalar
dupsConfigSensitivity=_DupsConfigSensitivity_Object((1,3,6,1,4,1,2254,2,5,3,3),_DupsConfigSensitivity_Type())
dupsConfigSensitivity.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigSensitivity.setStatus(_A)
_DupsConfigLowVoltageTransferPoint_Type=Integer32
_DupsConfigLowVoltageTransferPoint_Object=MibScalar
dupsConfigLowVoltageTransferPoint=_DupsConfigLowVoltageTransferPoint_Object((1,3,6,1,4,1,2254,2,5,3,4),_DupsConfigLowVoltageTransferPoint_Type())
dupsConfigLowVoltageTransferPoint.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigLowVoltageTransferPoint.setStatus(_A)
if mibBuilder.loadTexts:dupsConfigLowVoltageTransferPoint.setUnits(_S)
_DupsConfigHighVoltageTransferPoint_Type=Integer32
_DupsConfigHighVoltageTransferPoint_Object=MibScalar
dupsConfigHighVoltageTransferPoint=_DupsConfigHighVoltageTransferPoint_Object((1,3,6,1,4,1,2254,2,5,3,5),_DupsConfigHighVoltageTransferPoint_Type())
dupsConfigHighVoltageTransferPoint.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigHighVoltageTransferPoint.setStatus(_A)
if mibBuilder.loadTexts:dupsConfigHighVoltageTransferPoint.setUnits(_S)
_DupsConfigUPSBootDelay_Type=Integer32
_DupsConfigUPSBootDelay_Object=MibScalar
dupsConfigUPSBootDelay=_DupsConfigUPSBootDelay_Object((1,3,6,1,4,1,2254,2,5,3,6),_DupsConfigUPSBootDelay_Type())
dupsConfigUPSBootDelay.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigUPSBootDelay.setStatus(_A)
if mibBuilder.loadTexts:dupsConfigUPSBootDelay.setUnits(_Y)
_DupsConfigExternalBatteryPack_Type=Integer32
_DupsConfigExternalBatteryPack_Object=MibScalar
dupsConfigExternalBatteryPack=_DupsConfigExternalBatteryPack_Object((1,3,6,1,4,1,2254,2,5,3,7),_DupsConfigExternalBatteryPack_Type())
dupsConfigExternalBatteryPack.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigExternalBatteryPack.setStatus(_A)
_DupsConfigSmartShutdownOSDelay_Type=Integer32
_DupsConfigSmartShutdownOSDelay_Object=MibScalar
dupsConfigSmartShutdownOSDelay=_DupsConfigSmartShutdownOSDelay_Object((1,3,6,1,4,1,2254,2,5,3,8),_DupsConfigSmartShutdownOSDelay_Type())
dupsConfigSmartShutdownOSDelay.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigSmartShutdownOSDelay.setStatus(_A)
if mibBuilder.loadTexts:dupsConfigSmartShutdownOSDelay.setUnits(_Y)
_DupsConfigSmartShutdownUPSDelay_Type=Integer32
_DupsConfigSmartShutdownUPSDelay_Object=MibScalar
dupsConfigSmartShutdownUPSDelay=_DupsConfigSmartShutdownUPSDelay_Object((1,3,6,1,4,1,2254,2,5,3,9),_DupsConfigSmartShutdownUPSDelay_Type())
dupsConfigSmartShutdownUPSDelay.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigSmartShutdownUPSDelay.setStatus(_A)
if mibBuilder.loadTexts:dupsConfigSmartShutdownUPSDelay.setUnits(_Y)
class _DupsConfigEconomicMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_DupsConfigEconomicMode_Type.__name__=_D
_DupsConfigEconomicMode_Object=MibScalar
dupsConfigEconomicMode=_DupsConfigEconomicMode_Object((1,3,6,1,4,1,2254,2,5,3,10),_DupsConfigEconomicMode_Type())
dupsConfigEconomicMode.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsConfigEconomicMode.setStatus(_A)
_DupsInput_ObjectIdentity=ObjectIdentity
dupsInput=_DupsInput_ObjectIdentity((1,3,6,1,4,1,2254,2,5,4))
_DupsInputNumLines_Type=Integer32
_DupsInputNumLines_Object=MibScalar
dupsInputNumLines=_DupsInputNumLines_Object((1,3,6,1,4,1,2254,2,5,4,1),_DupsInputNumLines_Type())
dupsInputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputNumLines.setStatus(_A)
_DupsInputFrequency1_Type=Integer32
_DupsInputFrequency1_Object=MibScalar
dupsInputFrequency1=_DupsInputFrequency1_Object((1,3,6,1,4,1,2254,2,5,4,2),_DupsInputFrequency1_Type())
dupsInputFrequency1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputFrequency1.setStatus(_A)
if mibBuilder.loadTexts:dupsInputFrequency1.setUnits(_V)
_DupsInputVoltage1_Type=Integer32
_DupsInputVoltage1_Object=MibScalar
dupsInputVoltage1=_DupsInputVoltage1_Object((1,3,6,1,4,1,2254,2,5,4,3),_DupsInputVoltage1_Type())
dupsInputVoltage1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputVoltage1.setStatus(_A)
if mibBuilder.loadTexts:dupsInputVoltage1.setUnits(_L)
_DupsInputVoltage12_Type=Integer32
_DupsInputVoltage12_Object=MibScalar
dupsInputVoltage12=_DupsInputVoltage12_Object((1,3,6,1,4,1,2254,2,5,4,4),_DupsInputVoltage12_Type())
dupsInputVoltage12.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputVoltage12.setStatus(_A)
if mibBuilder.loadTexts:dupsInputVoltage12.setUnits(_L)
_DupsInputCurrent1_Type=Integer32
_DupsInputCurrent1_Object=MibScalar
dupsInputCurrent1=_DupsInputCurrent1_Object((1,3,6,1,4,1,2254,2,5,4,5),_DupsInputCurrent1_Type())
dupsInputCurrent1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputCurrent1.setStatus(_A)
if mibBuilder.loadTexts:dupsInputCurrent1.setUnits(_N)
_DupsInputPower1_Type=Integer32
_DupsInputPower1_Object=MibScalar
dupsInputPower1=_DupsInputPower1_Object((1,3,6,1,4,1,2254,2,5,4,6),_DupsInputPower1_Type())
dupsInputPower1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputPower1.setStatus(_A)
if mibBuilder.loadTexts:dupsInputPower1.setUnits(_O)
_DupsInputFrequency2_Type=Integer32
_DupsInputFrequency2_Object=MibScalar
dupsInputFrequency2=_DupsInputFrequency2_Object((1,3,6,1,4,1,2254,2,5,4,7),_DupsInputFrequency2_Type())
dupsInputFrequency2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputFrequency2.setStatus(_A)
if mibBuilder.loadTexts:dupsInputFrequency2.setUnits(_V)
_DupsInputVoltage2_Type=Integer32
_DupsInputVoltage2_Object=MibScalar
dupsInputVoltage2=_DupsInputVoltage2_Object((1,3,6,1,4,1,2254,2,5,4,8),_DupsInputVoltage2_Type())
dupsInputVoltage2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputVoltage2.setStatus(_A)
if mibBuilder.loadTexts:dupsInputVoltage2.setUnits(_L)
_DupsInputVoltage23_Type=Integer32
_DupsInputVoltage23_Object=MibScalar
dupsInputVoltage23=_DupsInputVoltage23_Object((1,3,6,1,4,1,2254,2,5,4,9),_DupsInputVoltage23_Type())
dupsInputVoltage23.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputVoltage23.setStatus(_A)
if mibBuilder.loadTexts:dupsInputVoltage23.setUnits(_L)
_DupsInputCurrent2_Type=Integer32
_DupsInputCurrent2_Object=MibScalar
dupsInputCurrent2=_DupsInputCurrent2_Object((1,3,6,1,4,1,2254,2,5,4,10),_DupsInputCurrent2_Type())
dupsInputCurrent2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputCurrent2.setStatus(_A)
if mibBuilder.loadTexts:dupsInputCurrent2.setUnits(_N)
_DupsInputPower2_Type=Integer32
_DupsInputPower2_Object=MibScalar
dupsInputPower2=_DupsInputPower2_Object((1,3,6,1,4,1,2254,2,5,4,11),_DupsInputPower2_Type())
dupsInputPower2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputPower2.setStatus(_A)
if mibBuilder.loadTexts:dupsInputPower2.setUnits(_O)
_DupsInputFrequency3_Type=Integer32
_DupsInputFrequency3_Object=MibScalar
dupsInputFrequency3=_DupsInputFrequency3_Object((1,3,6,1,4,1,2254,2,5,4,12),_DupsInputFrequency3_Type())
dupsInputFrequency3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputFrequency3.setStatus(_A)
if mibBuilder.loadTexts:dupsInputFrequency3.setUnits(_V)
_DupsInputVoltage3_Type=Integer32
_DupsInputVoltage3_Object=MibScalar
dupsInputVoltage3=_DupsInputVoltage3_Object((1,3,6,1,4,1,2254,2,5,4,13),_DupsInputVoltage3_Type())
dupsInputVoltage3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputVoltage3.setStatus(_A)
if mibBuilder.loadTexts:dupsInputVoltage3.setUnits(_L)
_DupsInputVoltage31_Type=Integer32
_DupsInputVoltage31_Object=MibScalar
dupsInputVoltage31=_DupsInputVoltage31_Object((1,3,6,1,4,1,2254,2,5,4,14),_DupsInputVoltage31_Type())
dupsInputVoltage31.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputVoltage31.setStatus(_A)
if mibBuilder.loadTexts:dupsInputVoltage31.setUnits(_L)
_DupsInputCurrent3_Type=Integer32
_DupsInputCurrent3_Object=MibScalar
dupsInputCurrent3=_DupsInputCurrent3_Object((1,3,6,1,4,1,2254,2,5,4,15),_DupsInputCurrent3_Type())
dupsInputCurrent3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputCurrent3.setStatus(_A)
if mibBuilder.loadTexts:dupsInputCurrent3.setUnits(_N)
_DupsInputPower3_Type=Integer32
_DupsInputPower3_Object=MibScalar
dupsInputPower3=_DupsInputPower3_Object((1,3,6,1,4,1,2254,2,5,4,16),_DupsInputPower3_Type())
dupsInputPower3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputPower3.setStatus(_A)
if mibBuilder.loadTexts:dupsInputPower3.setUnits(_O)
_DupsInputEnergy1_Type=Integer32
_DupsInputEnergy1_Object=MibScalar
dupsInputEnergy1=_DupsInputEnergy1_Object((1,3,6,1,4,1,2254,2,5,4,17),_DupsInputEnergy1_Type())
dupsInputEnergy1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputEnergy1.setStatus(_A)
if mibBuilder.loadTexts:dupsInputEnergy1.setUnits(_M)
_DupsInputEnergy2_Type=Integer32
_DupsInputEnergy2_Object=MibScalar
dupsInputEnergy2=_DupsInputEnergy2_Object((1,3,6,1,4,1,2254,2,5,4,18),_DupsInputEnergy2_Type())
dupsInputEnergy2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputEnergy2.setStatus(_A)
if mibBuilder.loadTexts:dupsInputEnergy2.setUnits(_M)
_DupsInputEnergy3_Type=Integer32
_DupsInputEnergy3_Object=MibScalar
dupsInputEnergy3=_DupsInputEnergy3_Object((1,3,6,1,4,1,2254,2,5,4,19),_DupsInputEnergy3_Type())
dupsInputEnergy3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputEnergy3.setStatus(_A)
if mibBuilder.loadTexts:dupsInputEnergy3.setUnits(_M)
_DupsInputEnergyTotal_Type=Integer32
_DupsInputEnergyTotal_Object=MibScalar
dupsInputEnergyTotal=_DupsInputEnergyTotal_Object((1,3,6,1,4,1,2254,2,5,4,20),_DupsInputEnergyTotal_Type())
dupsInputEnergyTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputEnergyTotal.setStatus(_A)
if mibBuilder.loadTexts:dupsInputEnergyTotal.setUnits(_M)
class _DupsInputLineFailCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('no',1),('outoftolvolt',2),('outoftolfreq',3),('utilityoff',4)))
_DupsInputLineFailCause_Type.__name__=_D
_DupsInputLineFailCause_Object=MibScalar
dupsInputLineFailCause=_DupsInputLineFailCause_Object((1,3,6,1,4,1,2254,2,5,4,21),_DupsInputLineFailCause_Type())
dupsInputLineFailCause.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputLineFailCause.setStatus(_A)
class _DupsInputBadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_DupsInputBadStatus_Type.__name__=_D
_DupsInputBadStatus_Object=MibScalar
dupsInputBadStatus=_DupsInputBadStatus_Object((1,3,6,1,4,1,2254,2,5,4,22),_DupsInputBadStatus_Type())
dupsInputBadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsInputBadStatus.setStatus(_A)
_DupsOutput_ObjectIdentity=ObjectIdentity
dupsOutput=_DupsOutput_ObjectIdentity((1,3,6,1,4,1,2254,2,5,5))
class _DupsOutputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_I,1),('battery',2),('bypass',3),('reducing',4),('boosting',5),('manualBypass',6),('other',7),('noOutput',8),('onEco',9)))
_DupsOutputSource_Type.__name__=_D
_DupsOutputSource_Object=MibScalar
dupsOutputSource=_DupsOutputSource_Object((1,3,6,1,4,1,2254,2,5,5,1),_DupsOutputSource_Type())
dupsOutputSource.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputSource.setStatus(_A)
_DupsOutputFrequency_Type=Integer32
_DupsOutputFrequency_Object=MibScalar
dupsOutputFrequency=_DupsOutputFrequency_Object((1,3,6,1,4,1,2254,2,5,5,2),_DupsOutputFrequency_Type())
dupsOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputFrequency.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputFrequency.setUnits(_V)
_DupsOutputNumLines_Type=Integer32
_DupsOutputNumLines_Object=MibScalar
dupsOutputNumLines=_DupsOutputNumLines_Object((1,3,6,1,4,1,2254,2,5,5,3),_DupsOutputNumLines_Type())
dupsOutputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputNumLines.setStatus(_A)
_DupsOutputVoltage1_Type=Integer32
_DupsOutputVoltage1_Object=MibScalar
dupsOutputVoltage1=_DupsOutputVoltage1_Object((1,3,6,1,4,1,2254,2,5,5,4),_DupsOutputVoltage1_Type())
dupsOutputVoltage1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputVoltage1.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputVoltage1.setUnits(_L)
_DupsOutputVoltage12_Type=Integer32
_DupsOutputVoltage12_Object=MibScalar
dupsOutputVoltage12=_DupsOutputVoltage12_Object((1,3,6,1,4,1,2254,2,5,5,5),_DupsOutputVoltage12_Type())
dupsOutputVoltage12.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputVoltage12.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputVoltage12.setUnits(_L)
_DupsOutputCurrent1_Type=Integer32
_DupsOutputCurrent1_Object=MibScalar
dupsOutputCurrent1=_DupsOutputCurrent1_Object((1,3,6,1,4,1,2254,2,5,5,6),_DupsOutputCurrent1_Type())
dupsOutputCurrent1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputCurrent1.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputCurrent1.setUnits(_N)
_DupsOutputPower1_Type=Integer32
_DupsOutputPower1_Object=MibScalar
dupsOutputPower1=_DupsOutputPower1_Object((1,3,6,1,4,1,2254,2,5,5,7),_DupsOutputPower1_Type())
dupsOutputPower1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputPower1.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputPower1.setUnits(_O)
_DupsOutputLoad1_Type=Integer32
_DupsOutputLoad1_Object=MibScalar
dupsOutputLoad1=_DupsOutputLoad1_Object((1,3,6,1,4,1,2254,2,5,5,8),_DupsOutputLoad1_Type())
dupsOutputLoad1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputLoad1.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputLoad1.setUnits(_U)
_DupsOutputVoltage2_Type=Integer32
_DupsOutputVoltage2_Object=MibScalar
dupsOutputVoltage2=_DupsOutputVoltage2_Object((1,3,6,1,4,1,2254,2,5,5,9),_DupsOutputVoltage2_Type())
dupsOutputVoltage2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputVoltage2.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputVoltage2.setUnits(_L)
_DupsOutputVoltage23_Type=Integer32
_DupsOutputVoltage23_Object=MibScalar
dupsOutputVoltage23=_DupsOutputVoltage23_Object((1,3,6,1,4,1,2254,2,5,5,10),_DupsOutputVoltage23_Type())
dupsOutputVoltage23.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputVoltage23.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputVoltage23.setUnits(_L)
_DupsOutputCurrent2_Type=Integer32
_DupsOutputCurrent2_Object=MibScalar
dupsOutputCurrent2=_DupsOutputCurrent2_Object((1,3,6,1,4,1,2254,2,5,5,11),_DupsOutputCurrent2_Type())
dupsOutputCurrent2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputCurrent2.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputCurrent2.setUnits(_N)
_DupsOutputPower2_Type=Integer32
_DupsOutputPower2_Object=MibScalar
dupsOutputPower2=_DupsOutputPower2_Object((1,3,6,1,4,1,2254,2,5,5,12),_DupsOutputPower2_Type())
dupsOutputPower2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputPower2.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputPower2.setUnits(_O)
_DupsOutputLoad2_Type=Integer32
_DupsOutputLoad2_Object=MibScalar
dupsOutputLoad2=_DupsOutputLoad2_Object((1,3,6,1,4,1,2254,2,5,5,13),_DupsOutputLoad2_Type())
dupsOutputLoad2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputLoad2.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputLoad2.setUnits(_U)
_DupsOutputVoltage3_Type=Integer32
_DupsOutputVoltage3_Object=MibScalar
dupsOutputVoltage3=_DupsOutputVoltage3_Object((1,3,6,1,4,1,2254,2,5,5,14),_DupsOutputVoltage3_Type())
dupsOutputVoltage3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputVoltage3.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputVoltage3.setUnits(_L)
_DupsOutputVoltage31_Type=Integer32
_DupsOutputVoltage31_Object=MibScalar
dupsOutputVoltage31=_DupsOutputVoltage31_Object((1,3,6,1,4,1,2254,2,5,5,15),_DupsOutputVoltage31_Type())
dupsOutputVoltage31.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputVoltage31.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputVoltage31.setUnits(_L)
_DupsOutputCurrent3_Type=Integer32
_DupsOutputCurrent3_Object=MibScalar
dupsOutputCurrent3=_DupsOutputCurrent3_Object((1,3,6,1,4,1,2254,2,5,5,16),_DupsOutputCurrent3_Type())
dupsOutputCurrent3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputCurrent3.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputCurrent3.setUnits(_N)
_DupsOutputPower3_Type=Integer32
_DupsOutputPower3_Object=MibScalar
dupsOutputPower3=_DupsOutputPower3_Object((1,3,6,1,4,1,2254,2,5,5,17),_DupsOutputPower3_Type())
dupsOutputPower3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputPower3.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputPower3.setUnits(_O)
_DupsOutputLoad3_Type=Integer32
_DupsOutputLoad3_Object=MibScalar
dupsOutputLoad3=_DupsOutputLoad3_Object((1,3,6,1,4,1,2254,2,5,5,18),_DupsOutputLoad3_Type())
dupsOutputLoad3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputLoad3.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputLoad3.setUnits(_U)
_DupsOutputTotalActivePower_Type=Integer32
_DupsOutputTotalActivePower_Object=MibScalar
dupsOutputTotalActivePower=_DupsOutputTotalActivePower_Object((1,3,6,1,4,1,2254,2,5,5,19),_DupsOutputTotalActivePower_Type())
dupsOutputTotalActivePower.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputTotalActivePower.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputTotalActivePower.setUnits('0.1 kW')
_DupsOutputTotalApparentPower_Type=Integer32
_DupsOutputTotalApparentPower_Object=MibScalar
dupsOutputTotalApparentPower=_DupsOutputTotalApparentPower_Object((1,3,6,1,4,1,2254,2,5,5,20),_DupsOutputTotalApparentPower_Type())
dupsOutputTotalApparentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputTotalApparentPower.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputTotalApparentPower.setUnits('0.1 kVA')
_DupsOutputTotalPowerFactor_Type=Integer32
_DupsOutputTotalPowerFactor_Object=MibScalar
dupsOutputTotalPowerFactor=_DupsOutputTotalPowerFactor_Object((1,3,6,1,4,1,2254,2,5,5,21),_DupsOutputTotalPowerFactor_Type())
dupsOutputTotalPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputTotalPowerFactor.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputTotalPowerFactor.setUnits(_U)
_DupsOutputEnergy1_Type=Integer32
_DupsOutputEnergy1_Object=MibScalar
dupsOutputEnergy1=_DupsOutputEnergy1_Object((1,3,6,1,4,1,2254,2,5,5,22),_DupsOutputEnergy1_Type())
dupsOutputEnergy1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputEnergy1.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputEnergy1.setUnits(_M)
_DupsOutputEnergy2_Type=Integer32
_DupsOutputEnergy2_Object=MibScalar
dupsOutputEnergy2=_DupsOutputEnergy2_Object((1,3,6,1,4,1,2254,2,5,5,23),_DupsOutputEnergy2_Type())
dupsOutputEnergy2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputEnergy2.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputEnergy2.setUnits(_M)
_DupsOutputEnergy3_Type=Integer32
_DupsOutputEnergy3_Object=MibScalar
dupsOutputEnergy3=_DupsOutputEnergy3_Object((1,3,6,1,4,1,2254,2,5,5,24),_DupsOutputEnergy3_Type())
dupsOutputEnergy3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputEnergy3.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputEnergy3.setUnits(_M)
_DupsOutputEnergyTotal_Type=Integer32
_DupsOutputEnergyTotal_Object=MibScalar
dupsOutputEnergyTotal=_DupsOutputEnergyTotal_Object((1,3,6,1,4,1,2254,2,5,5,25),_DupsOutputEnergyTotal_Type())
dupsOutputEnergyTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsOutputEnergyTotal.setStatus(_A)
if mibBuilder.loadTexts:dupsOutputEnergyTotal.setUnits(_M)
_DupsBypass_ObjectIdentity=ObjectIdentity
dupsBypass=_DupsBypass_ObjectIdentity((1,3,6,1,4,1,2254,2,5,6))
_DupsBypassFrequency_Type=Integer32
_DupsBypassFrequency_Object=MibScalar
dupsBypassFrequency=_DupsBypassFrequency_Object((1,3,6,1,4,1,2254,2,5,6,1),_DupsBypassFrequency_Type())
dupsBypassFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassFrequency.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassFrequency.setUnits(_V)
_DupsBypassNumLines_Type=Integer32
_DupsBypassNumLines_Object=MibScalar
dupsBypassNumLines=_DupsBypassNumLines_Object((1,3,6,1,4,1,2254,2,5,6,2),_DupsBypassNumLines_Type())
dupsBypassNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassNumLines.setStatus(_A)
_DupsBypassVoltage1_Type=Integer32
_DupsBypassVoltage1_Object=MibScalar
dupsBypassVoltage1=_DupsBypassVoltage1_Object((1,3,6,1,4,1,2254,2,5,6,3),_DupsBypassVoltage1_Type())
dupsBypassVoltage1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassVoltage1.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassVoltage1.setUnits(_L)
_DupsBypassVoltage12_Type=Integer32
_DupsBypassVoltage12_Object=MibScalar
dupsBypassVoltage12=_DupsBypassVoltage12_Object((1,3,6,1,4,1,2254,2,5,6,4),_DupsBypassVoltage12_Type())
dupsBypassVoltage12.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassVoltage12.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassVoltage12.setUnits(_L)
_DupsBypassCurrent1_Type=Integer32
_DupsBypassCurrent1_Object=MibScalar
dupsBypassCurrent1=_DupsBypassCurrent1_Object((1,3,6,1,4,1,2254,2,5,6,5),_DupsBypassCurrent1_Type())
dupsBypassCurrent1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassCurrent1.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassCurrent1.setUnits(_N)
_DupsBypassPower1_Type=Integer32
_DupsBypassPower1_Object=MibScalar
dupsBypassPower1=_DupsBypassPower1_Object((1,3,6,1,4,1,2254,2,5,6,6),_DupsBypassPower1_Type())
dupsBypassPower1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassPower1.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassPower1.setUnits(_O)
_DupsBypassVoltage2_Type=Integer32
_DupsBypassVoltage2_Object=MibScalar
dupsBypassVoltage2=_DupsBypassVoltage2_Object((1,3,6,1,4,1,2254,2,5,6,7),_DupsBypassVoltage2_Type())
dupsBypassVoltage2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassVoltage2.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassVoltage2.setUnits(_L)
_DupsBypassVoltage23_Type=Integer32
_DupsBypassVoltage23_Object=MibScalar
dupsBypassVoltage23=_DupsBypassVoltage23_Object((1,3,6,1,4,1,2254,2,5,6,8),_DupsBypassVoltage23_Type())
dupsBypassVoltage23.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassVoltage23.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassVoltage23.setUnits(_L)
_DupsBypassCurrent2_Type=Integer32
_DupsBypassCurrent2_Object=MibScalar
dupsBypassCurrent2=_DupsBypassCurrent2_Object((1,3,6,1,4,1,2254,2,5,6,9),_DupsBypassCurrent2_Type())
dupsBypassCurrent2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassCurrent2.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassCurrent2.setUnits(_N)
_DupsBypassPower2_Type=Integer32
_DupsBypassPower2_Object=MibScalar
dupsBypassPower2=_DupsBypassPower2_Object((1,3,6,1,4,1,2254,2,5,6,10),_DupsBypassPower2_Type())
dupsBypassPower2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassPower2.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassPower2.setUnits(_O)
_DupsBypassVoltage3_Type=Integer32
_DupsBypassVoltage3_Object=MibScalar
dupsBypassVoltage3=_DupsBypassVoltage3_Object((1,3,6,1,4,1,2254,2,5,6,11),_DupsBypassVoltage3_Type())
dupsBypassVoltage3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassVoltage3.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassVoltage3.setUnits(_L)
_DupsBypassVoltage31_Type=Integer32
_DupsBypassVoltage31_Object=MibScalar
dupsBypassVoltage31=_DupsBypassVoltage31_Object((1,3,6,1,4,1,2254,2,5,6,12),_DupsBypassVoltage31_Type())
dupsBypassVoltage31.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassVoltage31.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassVoltage31.setUnits(_L)
_DupsBypassCurrent3_Type=Integer32
_DupsBypassCurrent3_Object=MibScalar
dupsBypassCurrent3=_DupsBypassCurrent3_Object((1,3,6,1,4,1,2254,2,5,6,13),_DupsBypassCurrent3_Type())
dupsBypassCurrent3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassCurrent3.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassCurrent3.setUnits(_N)
_DupsBypassPower3_Type=Integer32
_DupsBypassPower3_Object=MibScalar
dupsBypassPower3=_DupsBypassPower3_Object((1,3,6,1,4,1,2254,2,5,6,14),_DupsBypassPower3_Type())
dupsBypassPower3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassPower3.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassPower3.setUnits(_O)
_DupsBypassSTSTemperature_Type=Integer32
_DupsBypassSTSTemperature_Object=MibScalar
dupsBypassSTSTemperature=_DupsBypassSTSTemperature_Object((1,3,6,1,4,1,2254,2,5,6,15),_DupsBypassSTSTemperature_Type())
dupsBypassSTSTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBypassSTSTemperature.setStatus(_A)
if mibBuilder.loadTexts:dupsBypassSTSTemperature.setUnits(_T)
_DupsBattery_ObjectIdentity=ObjectIdentity
dupsBattery=_DupsBattery_ObjectIdentity((1,3,6,1,4,1,2254,2,5,7))
class _DupsBatteryCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('good',1),('weak',2),('replace',3)))
_DupsBatteryCondition_Type.__name__=_D
_DupsBatteryCondition_Object=MibScalar
dupsBatteryCondition=_DupsBatteryCondition_Object((1,3,6,1,4,1,2254,2,5,7,1),_DupsBatteryCondition_Type())
dupsBatteryCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryCondition.setStatus(_A)
class _DupsBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('low',2),('depleted',3)))
_DupsBatteryStatus_Type.__name__=_D
_DupsBatteryStatus_Object=MibScalar
dupsBatteryStatus=_DupsBatteryStatus_Object((1,3,6,1,4,1,2254,2,5,7,2),_DupsBatteryStatus_Type())
dupsBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryStatus.setStatus(_A)
class _DupsBatteryCharge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('floating',1),('charging',2),('resting',3),('discharging',4)))
_DupsBatteryCharge_Type.__name__=_D
_DupsBatteryCharge_Object=MibScalar
dupsBatteryCharge=_DupsBatteryCharge_Object((1,3,6,1,4,1,2254,2,5,7,3),_DupsBatteryCharge_Type())
dupsBatteryCharge.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryCharge.setStatus(_A)
_DupsSecondsOnBattery_Type=Integer32
_DupsSecondsOnBattery_Object=MibScalar
dupsSecondsOnBattery=_DupsSecondsOnBattery_Object((1,3,6,1,4,1,2254,2,5,7,4),_DupsSecondsOnBattery_Type())
dupsSecondsOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsSecondsOnBattery.setStatus(_A)
if mibBuilder.loadTexts:dupsSecondsOnBattery.setUnits('1 Second')
_DupsBatteryEstimatedTime_Type=Integer32
_DupsBatteryEstimatedTime_Object=MibScalar
dupsBatteryEstimatedTime=_DupsBatteryEstimatedTime_Object((1,3,6,1,4,1,2254,2,5,7,5),_DupsBatteryEstimatedTime_Type())
dupsBatteryEstimatedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryEstimatedTime.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryEstimatedTime.setUnits('1 Minute')
_DupsBatteryPosVoltage_Type=Integer32
_DupsBatteryPosVoltage_Object=MibScalar
dupsBatteryPosVoltage=_DupsBatteryPosVoltage_Object((1,3,6,1,4,1,2254,2,5,7,6),_DupsBatteryPosVoltage_Type())
dupsBatteryPosVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryPosVoltage.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryPosVoltage.setUnits('0.1 Volt DC')
_DupsBatteryNegVoltage_Type=Integer32
_DupsBatteryNegVoltage_Object=MibScalar
dupsBatteryNegVoltage=_DupsBatteryNegVoltage_Object((1,3,6,1,4,1,2254,2,5,7,7),_DupsBatteryNegVoltage_Type())
dupsBatteryNegVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryNegVoltage.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryNegVoltage.setUnits('-0.1 Volt DC')
_DupsBatteryPosCurrent_Type=Integer32
_DupsBatteryPosCurrent_Object=MibScalar
dupsBatteryPosCurrent=_DupsBatteryPosCurrent_Object((1,3,6,1,4,1,2254,2,5,7,8),_DupsBatteryPosCurrent_Type())
dupsBatteryPosCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryPosCurrent.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryPosCurrent.setUnits(_e)
_DupsBatteryNegCurrent_Type=Integer32
_DupsBatteryNegCurrent_Object=MibScalar
dupsBatteryNegCurrent=_DupsBatteryNegCurrent_Object((1,3,6,1,4,1,2254,2,5,7,9),_DupsBatteryNegCurrent_Type())
dupsBatteryNegCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryNegCurrent.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryNegCurrent.setUnits(_e)
class _DupsBatteryPosCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DupsBatteryPosCapacity_Type.__name__=_D
_DupsBatteryPosCapacity_Object=MibScalar
dupsBatteryPosCapacity=_DupsBatteryPosCapacity_Object((1,3,6,1,4,1,2254,2,5,7,10),_DupsBatteryPosCapacity_Type())
dupsBatteryPosCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryPosCapacity.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryPosCapacity.setUnits(_U)
class _DupsBatteryNegCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DupsBatteryNegCapacity_Type.__name__=_D
_DupsBatteryNegCapacity_Object=MibScalar
dupsBatteryNegCapacity=_DupsBatteryNegCapacity_Object((1,3,6,1,4,1,2254,2,5,7,11),_DupsBatteryNegCapacity_Type())
dupsBatteryNegCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryNegCapacity.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryNegCapacity.setUnits(_U)
_DupsTemperature_Type=Integer32
_DupsTemperature_Object=MibScalar
dupsTemperature=_DupsTemperature_Object((1,3,6,1,4,1,2254,2,5,7,12),_DupsTemperature_Type())
dupsTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsTemperature.setStatus(_A)
if mibBuilder.loadTexts:dupsTemperature.setUnits(_W)
class _DupsLastReplaceDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DupsLastReplaceDate_Type.__name__=_P
_DupsLastReplaceDate_Object=MibScalar
dupsLastReplaceDate=_DupsLastReplaceDate_Object((1,3,6,1,4,1,2254,2,5,7,13),_DupsLastReplaceDate_Type())
dupsLastReplaceDate.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsLastReplaceDate.setStatus(_A)
class _DupsNextReplaceDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DupsNextReplaceDate_Type.__name__=_P
_DupsNextReplaceDate_Object=MibScalar
dupsNextReplaceDate=_DupsNextReplaceDate_Object((1,3,6,1,4,1,2254,2,5,7,14),_DupsNextReplaceDate_Type())
dupsNextReplaceDate.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsNextReplaceDate.setStatus(_A)
class _DupsBatteryBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsBatteryBreaker_Type.__name__=_D
_DupsBatteryBreaker_Object=MibScalar
dupsBatteryBreaker=_DupsBatteryBreaker_Object((1,3,6,1,4,1,2254,2,5,7,15),_DupsBatteryBreaker_Type())
dupsBatteryBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryBreaker.setStatus(_A)
_DupsBatteryCab1Tempurature_Type=Integer32
_DupsBatteryCab1Tempurature_Object=MibScalar
dupsBatteryCab1Tempurature=_DupsBatteryCab1Tempurature_Object((1,3,6,1,4,1,2254,2,5,7,16),_DupsBatteryCab1Tempurature_Type())
dupsBatteryCab1Tempurature.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryCab1Tempurature.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryCab1Tempurature.setUnits(_W)
_DupsBatteryCab2Tempurature_Type=Integer32
_DupsBatteryCab2Tempurature_Object=MibScalar
dupsBatteryCab2Tempurature=_DupsBatteryCab2Tempurature_Object((1,3,6,1,4,1,2254,2,5,7,17),_DupsBatteryCab2Tempurature_Type())
dupsBatteryCab2Tempurature.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryCab2Tempurature.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryCab2Tempurature.setUnits(_W)
_DupsBatteryCab3Tempurature_Type=Integer32
_DupsBatteryCab3Tempurature_Object=MibScalar
dupsBatteryCab3Tempurature=_DupsBatteryCab3Tempurature_Object((1,3,6,1,4,1,2254,2,5,7,18),_DupsBatteryCab3Tempurature_Type())
dupsBatteryCab3Tempurature.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryCab3Tempurature.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryCab3Tempurature.setUnits(_W)
_DupsBatteryCab4Tempurature_Type=Integer32
_DupsBatteryCab4Tempurature_Object=MibScalar
dupsBatteryCab4Tempurature=_DupsBatteryCab4Tempurature_Object((1,3,6,1,4,1,2254,2,5,7,19),_DupsBatteryCab4Tempurature_Type())
dupsBatteryCab4Tempurature.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsBatteryCab4Tempurature.setStatus(_A)
if mibBuilder.loadTexts:dupsBatteryCab4Tempurature.setUnits(_W)
_DupsTest_ObjectIdentity=ObjectIdentity
dupsTest=_DupsTest_ObjectIdentity((1,3,6,1,4,1,2254,2,5,8))
class _DupsTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('abort',1),('generalTest',2),('batteryTest',3),('testFor10sec',4),('testUntilBattlow',5)))
_DupsTestType_Type.__name__=_D
_DupsTestType_Object=MibScalar
dupsTestType=_DupsTestType_Object((1,3,6,1,4,1,2254,2,5,8,1),_DupsTestType_Type())
dupsTestType.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsTestType.setStatus(_A)
class _DupsTestResultsSummary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noTestsInitiated',1),('donePass',2),(_f,3),('generalTestFail',4),('batteryTestFail',5),('deepBatteryTestFail',6)))
_DupsTestResultsSummary_Type.__name__=_D
_DupsTestResultsSummary_Object=MibScalar
dupsTestResultsSummary=_DupsTestResultsSummary_Object((1,3,6,1,4,1,2254,2,5,8,2),_DupsTestResultsSummary_Type())
dupsTestResultsSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsTestResultsSummary.setStatus(_A)
class _DupsTestResultsDetail_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DupsTestResultsDetail_Type.__name__=_P
_DupsTestResultsDetail_Object=MibScalar
dupsTestResultsDetail=_DupsTestResultsDetail_Object((1,3,6,1,4,1,2254,2,5,8,3),_DupsTestResultsDetail_Type())
dupsTestResultsDetail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsTestResultsDetail.setStatus(_A)
class _DupsGeneratorTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('abort',1),('start',2)))
_DupsGeneratorTest_Type.__name__=_D
_DupsGeneratorTest_Object=MibScalar
dupsGeneratorTest=_DupsGeneratorTest_Object((1,3,6,1,4,1,2254,2,5,8,4),_DupsGeneratorTest_Type())
dupsGeneratorTest.setMaxAccess(_K)
if mibBuilder.loadTexts:dupsGeneratorTest.setStatus(_A)
class _DupsGeneratorTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_f,1),('none',2),('inhibitTest',3),('abnormallyTerminate',4),('byInstruction',5),('byTimeout',6)))
_DupsGeneratorTestStatus_Type.__name__=_D
_DupsGeneratorTestStatus_Object=MibScalar
dupsGeneratorTestStatus=_DupsGeneratorTestStatus_Object((1,3,6,1,4,1,2254,2,5,8,5),_DupsGeneratorTestStatus_Type())
dupsGeneratorTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsGeneratorTestStatus.setStatus(_A)
_DupsAlarm_ObjectIdentity=ObjectIdentity
dupsAlarm=_DupsAlarm_ObjectIdentity((1,3,6,1,4,1,2254,2,5,9))
class _DupsAlarmDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmDisconnect_Type.__name__=_D
_DupsAlarmDisconnect_Object=MibScalar
dupsAlarmDisconnect=_DupsAlarmDisconnect_Object((1,3,6,1,4,1,2254,2,5,9,1),_DupsAlarmDisconnect_Type())
dupsAlarmDisconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmDisconnect.setStatus(_A)
class _DupsAlarmInputOutOfRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmInputOutOfRange_Type.__name__=_D
_DupsAlarmInputOutOfRange_Object=MibScalar
dupsAlarmInputOutOfRange=_DupsAlarmInputOutOfRange_Object((1,3,6,1,4,1,2254,2,5,9,2),_DupsAlarmInputOutOfRange_Type())
dupsAlarmInputOutOfRange.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmInputOutOfRange.setStatus(_A)
class _DupsAlarmBatteryLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmBatteryLow_Type.__name__=_D
_DupsAlarmBatteryLow_Object=MibScalar
dupsAlarmBatteryLow=_DupsAlarmBatteryLow_Object((1,3,6,1,4,1,2254,2,5,9,3),_DupsAlarmBatteryLow_Type())
dupsAlarmBatteryLow.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmBatteryLow.setStatus(_A)
class _DupsAlarmLoadOnBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmLoadOnBypass_Type.__name__=_D
_DupsAlarmLoadOnBypass_Object=MibScalar
dupsAlarmLoadOnBypass=_DupsAlarmLoadOnBypass_Object((1,3,6,1,4,1,2254,2,5,9,4),_DupsAlarmLoadOnBypass_Type())
dupsAlarmLoadOnBypass.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmLoadOnBypass.setStatus(_A)
class _DupsAlarmOther_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmOther_Type.__name__=_D
_DupsAlarmOther_Object=MibScalar
dupsAlarmOther=_DupsAlarmOther_Object((1,3,6,1,4,1,2254,2,5,9,5),_DupsAlarmOther_Type())
dupsAlarmOther.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOther.setStatus(_A)
class _DupsAlarmBatteryGroundFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmBatteryGroundFault_Type.__name__=_D
_DupsAlarmBatteryGroundFault_Object=MibScalar
dupsAlarmBatteryGroundFault=_DupsAlarmBatteryGroundFault_Object((1,3,6,1,4,1,2254,2,5,9,6),_DupsAlarmBatteryGroundFault_Type())
dupsAlarmBatteryGroundFault.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmBatteryGroundFault.setStatus(_A)
class _DupsAlarmTestInProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmTestInProgress_Type.__name__=_D
_DupsAlarmTestInProgress_Object=MibScalar
dupsAlarmTestInProgress=_DupsAlarmTestInProgress_Object((1,3,6,1,4,1,2254,2,5,9,7),_DupsAlarmTestInProgress_Type())
dupsAlarmTestInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmTestInProgress.setStatus(_A)
class _DupsAlarmBatteryTestFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmBatteryTestFail_Type.__name__=_D
_DupsAlarmBatteryTestFail_Object=MibScalar
dupsAlarmBatteryTestFail=_DupsAlarmBatteryTestFail_Object((1,3,6,1,4,1,2254,2,5,9,8),_DupsAlarmBatteryTestFail_Type())
dupsAlarmBatteryTestFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmBatteryTestFail.setStatus(_A)
class _DupsAlarmFuseFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmFuseFailure_Type.__name__=_D
_DupsAlarmFuseFailure_Object=MibScalar
dupsAlarmFuseFailure=_DupsAlarmFuseFailure_Object((1,3,6,1,4,1,2254,2,5,9,9),_DupsAlarmFuseFailure_Type())
dupsAlarmFuseFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmFuseFailure.setStatus(_A)
class _DupsAlarmOutputOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmOutputOverload_Type.__name__=_D
_DupsAlarmOutputOverload_Object=MibScalar
dupsAlarmOutputOverload=_DupsAlarmOutputOverload_Object((1,3,6,1,4,1,2254,2,5,9,10),_DupsAlarmOutputOverload_Type())
dupsAlarmOutputOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOutputOverload.setStatus(_A)
class _DupsAlarmInverterAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmInverterAbnormal_Type.__name__=_D
_DupsAlarmInverterAbnormal_Object=MibScalar
dupsAlarmInverterAbnormal=_DupsAlarmInverterAbnormal_Object((1,3,6,1,4,1,2254,2,5,9,11),_DupsAlarmInverterAbnormal_Type())
dupsAlarmInverterAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmInverterAbnormal.setStatus(_A)
class _DupsAlarmLoadOnReserve_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmLoadOnReserve_Type.__name__=_D
_DupsAlarmLoadOnReserve_Object=MibScalar
dupsAlarmLoadOnReserve=_DupsAlarmLoadOnReserve_Object((1,3,6,1,4,1,2254,2,5,9,12),_DupsAlarmLoadOnReserve_Type())
dupsAlarmLoadOnReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmLoadOnReserve.setStatus(_A)
class _DupsAlarmTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmTemperature_Type.__name__=_D
_DupsAlarmTemperature_Object=MibScalar
dupsAlarmTemperature=_DupsAlarmTemperature_Object((1,3,6,1,4,1,2254,2,5,9,13),_DupsAlarmTemperature_Type())
dupsAlarmTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmTemperature.setStatus(_A)
class _DupsAlarmBypassOutOfRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmBypassOutOfRange_Type.__name__=_D
_DupsAlarmBypassOutOfRange_Object=MibScalar
dupsAlarmBypassOutOfRange=_DupsAlarmBypassOutOfRange_Object((1,3,6,1,4,1,2254,2,5,9,14),_DupsAlarmBypassOutOfRange_Type())
dupsAlarmBypassOutOfRange.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmBypassOutOfRange.setStatus(_A)
class _DupsAlarmStandby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmStandby_Type.__name__=_D
_DupsAlarmStandby_Object=MibScalar
dupsAlarmStandby=_DupsAlarmStandby_Object((1,3,6,1,4,1,2254,2,5,9,15),_DupsAlarmStandby_Type())
dupsAlarmStandby.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmStandby.setStatus(_A)
class _DupsAlarmChargerFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmChargerFail_Type.__name__=_D
_DupsAlarmChargerFail_Object=MibScalar
dupsAlarmChargerFail=_DupsAlarmChargerFail_Object((1,3,6,1,4,1,2254,2,5,9,16),_DupsAlarmChargerFail_Type())
dupsAlarmChargerFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmChargerFail.setStatus(_A)
class _DupsAlarmFanFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmFanFail_Type.__name__=_D
_DupsAlarmFanFail_Object=MibScalar
dupsAlarmFanFail=_DupsAlarmFanFail_Object((1,3,6,1,4,1,2254,2,5,9,17),_DupsAlarmFanFail_Type())
dupsAlarmFanFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmFanFail.setStatus(_A)
class _DupsAlarmEconomicMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmEconomicMode_Type.__name__=_D
_DupsAlarmEconomicMode_Object=MibScalar
dupsAlarmEconomicMode=_DupsAlarmEconomicMode_Object((1,3,6,1,4,1,2254,2,5,9,18),_DupsAlarmEconomicMode_Type())
dupsAlarmEconomicMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmEconomicMode.setStatus(_A)
class _DupsAlarmOutputOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmOutputOff_Type.__name__=_D
_DupsAlarmOutputOff_Object=MibScalar
dupsAlarmOutputOff=_DupsAlarmOutputOff_Object((1,3,6,1,4,1,2254,2,5,9,19),_DupsAlarmOutputOff_Type())
dupsAlarmOutputOff.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOutputOff.setStatus(_A)
class _DupsAlarmSmartShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmSmartShutdown_Type.__name__=_D
_DupsAlarmSmartShutdown_Object=MibScalar
dupsAlarmSmartShutdown=_DupsAlarmSmartShutdown_Object((1,3,6,1,4,1,2254,2,5,9,20),_DupsAlarmSmartShutdown_Type())
dupsAlarmSmartShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmSmartShutdown.setStatus(_A)
class _DupsAlarmEmergencyPowerOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmEmergencyPowerOff_Type.__name__=_D
_DupsAlarmEmergencyPowerOff_Object=MibScalar
dupsAlarmEmergencyPowerOff=_DupsAlarmEmergencyPowerOff_Object((1,3,6,1,4,1,2254,2,5,9,21),_DupsAlarmEmergencyPowerOff_Type())
dupsAlarmEmergencyPowerOff.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmEmergencyPowerOff.setStatus(_A)
class _DupsAlarmUPSShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmUPSShutdown_Type.__name__=_D
_DupsAlarmUPSShutdown_Object=MibScalar
dupsAlarmUPSShutdown=_DupsAlarmUPSShutdown_Object((1,3,6,1,4,1,2254,2,5,9,22),_DupsAlarmUPSShutdown_Type())
dupsAlarmUPSShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmUPSShutdown.setStatus(_A)
class _DupsAlarmEPO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmEPO_Type.__name__=_D
_DupsAlarmEPO_Object=MibScalar
dupsAlarmEPO=_DupsAlarmEPO_Object((1,3,6,1,4,1,2254,2,5,9,23),_DupsAlarmEPO_Type())
dupsAlarmEPO.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmEPO.setStatus(_A)
class _DupsAlarmOutVoltOverLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmOutVoltOverLimit_Type.__name__=_D
_DupsAlarmOutVoltOverLimit_Object=MibScalar
dupsAlarmOutVoltOverLimit=_DupsAlarmOutVoltOverLimit_Object((1,3,6,1,4,1,2254,2,5,9,24),_DupsAlarmOutVoltOverLimit_Type())
dupsAlarmOutVoltOverLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOutVoltOverLimit.setStatus(_A)
class _DupsAlarmOutVoltUnderLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmOutVoltUnderLimit_Type.__name__=_D
_DupsAlarmOutVoltUnderLimit_Object=MibScalar
dupsAlarmOutVoltUnderLimit=_DupsAlarmOutVoltUnderLimit_Object((1,3,6,1,4,1,2254,2,5,9,25),_DupsAlarmOutVoltUnderLimit_Type())
dupsAlarmOutVoltUnderLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOutVoltUnderLimit.setStatus(_A)
class _DupsAlarmPowerModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmPowerModule_Type.__name__=_D
_DupsAlarmPowerModule_Object=MibScalar
dupsAlarmPowerModule=_DupsAlarmPowerModule_Object((1,3,6,1,4,1,2254,2,5,9,26),_DupsAlarmPowerModule_Type())
dupsAlarmPowerModule.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmPowerModule.setStatus(_A)
class _DupsAlarmOutputBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsAlarmOutputBreaker_Type.__name__=_D
_DupsAlarmOutputBreaker_Object=MibScalar
dupsAlarmOutputBreaker=_DupsAlarmOutputBreaker_Object((1,3,6,1,4,1,2254,2,5,9,27),_DupsAlarmOutputBreaker_Type())
dupsAlarmOutputBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOutputBreaker.setStatus(_A)
class _DupsAlarmOutletBank1Breaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsAlarmOutletBank1Breaker_Type.__name__=_D
_DupsAlarmOutletBank1Breaker_Object=MibScalar
dupsAlarmOutletBank1Breaker=_DupsAlarmOutletBank1Breaker_Object((1,3,6,1,4,1,2254,2,5,9,28),_DupsAlarmOutletBank1Breaker_Type())
dupsAlarmOutletBank1Breaker.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOutletBank1Breaker.setStatus(_A)
class _DupsAlarmOutletBank2Breaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsAlarmOutletBank2Breaker_Type.__name__=_D
_DupsAlarmOutletBank2Breaker_Object=MibScalar
dupsAlarmOutletBank2Breaker=_DupsAlarmOutletBank2Breaker_Object((1,3,6,1,4,1,2254,2,5,9,29),_DupsAlarmOutletBank2Breaker_Type())
dupsAlarmOutletBank2Breaker.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOutletBank2Breaker.setStatus(_A)
class _DupsAlarmOutletBank3Breaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsAlarmOutletBank3Breaker_Type.__name__=_D
_DupsAlarmOutletBank3Breaker_Object=MibScalar
dupsAlarmOutletBank3Breaker=_DupsAlarmOutletBank3Breaker_Object((1,3,6,1,4,1,2254,2,5,9,30),_DupsAlarmOutletBank3Breaker_Type())
dupsAlarmOutletBank3Breaker.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOutletBank3Breaker.setStatus(_A)
class _DupsAlarmOutletBank4Breaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsAlarmOutletBank4Breaker_Type.__name__=_D
_DupsAlarmOutletBank4Breaker_Object=MibScalar
dupsAlarmOutletBank4Breaker=_DupsAlarmOutletBank4Breaker_Object((1,3,6,1,4,1,2254,2,5,9,31),_DupsAlarmOutletBank4Breaker_Type())
dupsAlarmOutletBank4Breaker.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmOutletBank4Breaker.setStatus(_A)
class _DupsAlarmSummary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('informational',2),(_X,3),(_J,4)))
_DupsAlarmSummary_Type.__name__=_D
_DupsAlarmSummary_Object=MibScalar
dupsAlarmSummary=_DupsAlarmSummary_Object((1,3,6,1,4,1,2254,2,5,9,32),_DupsAlarmSummary_Type())
dupsAlarmSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmSummary.setStatus(_A)
class _DupsAlarmRedundancyLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsAlarmRedundancyLoss_Type.__name__=_D
_DupsAlarmRedundancyLoss_Object=MibScalar
dupsAlarmRedundancyLoss=_DupsAlarmRedundancyLoss_Object((1,3,6,1,4,1,2254,2,5,9,33),_DupsAlarmRedundancyLoss_Type())
dupsAlarmRedundancyLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmRedundancyLoss.setStatus(_A)
class _DupsAlarmPhaseAsynchronous_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('asynchronous',1),('synchronous',2)))
_DupsAlarmPhaseAsynchronous_Type.__name__=_D
_DupsAlarmPhaseAsynchronous_Object=MibScalar
dupsAlarmPhaseAsynchronous=_DupsAlarmPhaseAsynchronous_Object((1,3,6,1,4,1,2254,2,5,9,34),_DupsAlarmPhaseAsynchronous_Type())
dupsAlarmPhaseAsynchronous.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmPhaseAsynchronous.setStatus(_A)
class _DupsAlarmRectifierAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsAlarmRectifierAbnormal_Type.__name__=_D
_DupsAlarmRectifierAbnormal_Object=MibScalar
dupsAlarmRectifierAbnormal=_DupsAlarmRectifierAbnormal_Object((1,3,6,1,4,1,2254,2,5,9,35),_DupsAlarmRectifierAbnormal_Type())
dupsAlarmRectifierAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmRectifierAbnormal.setStatus(_A)
class _DupsAlarmBypassBreakerOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsAlarmBypassBreakerOpen_Type.__name__=_D
_DupsAlarmBypassBreakerOpen_Object=MibScalar
dupsAlarmBypassBreakerOpen=_DupsAlarmBypassBreakerOpen_Object((1,3,6,1,4,1,2254,2,5,9,36),_DupsAlarmBypassBreakerOpen_Type())
dupsAlarmBypassBreakerOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmBypassBreakerOpen.setStatus(_A)
class _DupsAlarmMainInputBreakerOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsAlarmMainInputBreakerOpen_Type.__name__=_D
_DupsAlarmMainInputBreakerOpen_Object=MibScalar
dupsAlarmMainInputBreakerOpen=_DupsAlarmMainInputBreakerOpen_Object((1,3,6,1,4,1,2254,2,5,9,37),_DupsAlarmMainInputBreakerOpen_Type())
dupsAlarmMainInputBreakerOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmMainInputBreakerOpen.setStatus(_A)
class _DupsAlarmManualBypassBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsAlarmManualBypassBreaker_Type.__name__=_D
_DupsAlarmManualBypassBreaker_Object=MibScalar
dupsAlarmManualBypassBreaker=_DupsAlarmManualBypassBreaker_Object((1,3,6,1,4,1,2254,2,5,9,38),_DupsAlarmManualBypassBreaker_Type())
dupsAlarmManualBypassBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsAlarmManualBypassBreaker.setStatus(_A)
_DupsPowerModule_ObjectIdentity=ObjectIdentity
dupsPowerModule=_DupsPowerModule_ObjectIdentity((1,3,6,1,4,1,2254,2,5,10))
class _DupsPMBypassInputAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsPMBypassInputAlarm_Type.__name__=_D
_DupsPMBypassInputAlarm_Object=MibScalar
dupsPMBypassInputAlarm=_DupsPMBypassInputAlarm_Object((1,3,6,1,4,1,2254,2,5,10,1),_DupsPMBypassInputAlarm_Type())
dupsPMBypassInputAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMBypassInputAlarm.setStatus(_A)
class _DupsPMBypassPhaseAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsPMBypassPhaseAlarm_Type.__name__=_D
_DupsPMBypassPhaseAlarm_Object=MibScalar
dupsPMBypassPhaseAlarm=_DupsPMBypassPhaseAlarm_Object((1,3,6,1,4,1,2254,2,5,10,2),_DupsPMBypassPhaseAlarm_Type())
dupsPMBypassPhaseAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMBypassPhaseAlarm.setStatus(_A)
class _DupsPMBypassSTSOverloadAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsPMBypassSTSOverloadAlarm_Type.__name__=_D
_DupsPMBypassSTSOverloadAlarm_Object=MibScalar
dupsPMBypassSTSOverloadAlarm=_DupsPMBypassSTSOverloadAlarm_Object((1,3,6,1,4,1,2254,2,5,10,3),_DupsPMBypassSTSOverloadAlarm_Type())
dupsPMBypassSTSOverloadAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMBypassSTSOverloadAlarm.setStatus(_A)
class _DupsPMBypassSTSOverTempAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsPMBypassSTSOverTempAlarm_Type.__name__=_D
_DupsPMBypassSTSOverTempAlarm_Object=MibScalar
dupsPMBypassSTSOverTempAlarm=_DupsPMBypassSTSOverTempAlarm_Object((1,3,6,1,4,1,2254,2,5,10,4),_DupsPMBypassSTSOverTempAlarm_Type())
dupsPMBypassSTSOverTempAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMBypassSTSOverTempAlarm.setStatus(_A)
class _DupsPMBypassSTSFailAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsPMBypassSTSFailAlarm_Type.__name__=_D
_DupsPMBypassSTSFailAlarm_Object=MibScalar
dupsPMBypassSTSFailAlarm=_DupsPMBypassSTSFailAlarm_Object((1,3,6,1,4,1,2254,2,5,10,5),_DupsPMBypassSTSFailAlarm_Type())
dupsPMBypassSTSFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMBypassSTSFailAlarm.setStatus(_A)
_DupsPMTable_Object=MibTable
dupsPMTable=_DupsPMTable_Object((1,3,6,1,4,1,2254,2,5,10,6))
if mibBuilder.loadTexts:dupsPMTable.setStatus(_A)
_DupsPMEntry_Object=MibTableRow
dupsPMEntry=_DupsPMEntry_Object((1,3,6,1,4,1,2254,2,5,10,6,1))
dupsPMEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:dupsPMEntry.setStatus(_A)
_DupsPMID_Type=Integer32
_DupsPMID_Object=MibTableColumn
dupsPMID=_DupsPMID_Object((1,3,6,1,4,1,2254,2,5,10,6,1,1),_DupsPMID_Type())
dupsPMID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dupsPMID.setStatus(_A)
_DupsPMPFCTemp_Type=Integer32
_DupsPMPFCTemp_Object=MibTableColumn
dupsPMPFCTemp=_DupsPMPFCTemp_Object((1,3,6,1,4,1,2254,2,5,10,6,1,2),_DupsPMPFCTemp_Type())
dupsPMPFCTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMPFCTemp.setStatus(_A)
if mibBuilder.loadTexts:dupsPMPFCTemp.setUnits(_T)
_DupsPMINVTemp_Type=Integer32
_DupsPMINVTemp_Object=MibTableColumn
dupsPMINVTemp=_DupsPMINVTemp_Object((1,3,6,1,4,1,2254,2,5,10,6,1,3),_DupsPMINVTemp_Type())
dupsPMINVTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMINVTemp.setStatus(_A)
if mibBuilder.loadTexts:dupsPMINVTemp.setUnits(_T)
_DupsPMINVTempR_Type=Integer32
_DupsPMINVTempR_Object=MibTableColumn
dupsPMINVTempR=_DupsPMINVTempR_Object((1,3,6,1,4,1,2254,2,5,10,6,1,4),_DupsPMINVTempR_Type())
dupsPMINVTempR.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMINVTempR.setStatus(_A)
if mibBuilder.loadTexts:dupsPMINVTempR.setUnits(_T)
_DupsPMINVTempS_Type=Integer32
_DupsPMINVTempS_Object=MibTableColumn
dupsPMINVTempS=_DupsPMINVTempS_Object((1,3,6,1,4,1,2254,2,5,10,6,1,5),_DupsPMINVTempS_Type())
dupsPMINVTempS.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMINVTempS.setStatus(_A)
if mibBuilder.loadTexts:dupsPMINVTempS.setUnits(_T)
_DupsPMINVTempT_Type=Integer32
_DupsPMINVTempT_Object=MibTableColumn
dupsPMINVTempT=_DupsPMINVTempT_Object((1,3,6,1,4,1,2254,2,5,10,6,1,6),_DupsPMINVTempT_Type())
dupsPMINVTempT.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMINVTempT.setStatus(_A)
if mibBuilder.loadTexts:dupsPMINVTempT.setUnits(_T)
_DupsPMINVVolt1_Type=Integer32
_DupsPMINVVolt1_Object=MibTableColumn
dupsPMINVVolt1=_DupsPMINVVolt1_Object((1,3,6,1,4,1,2254,2,5,10,6,1,7),_DupsPMINVVolt1_Type())
dupsPMINVVolt1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMINVVolt1.setStatus(_A)
if mibBuilder.loadTexts:dupsPMINVVolt1.setUnits(_L)
_DupsPMINVVolt2_Type=Integer32
_DupsPMINVVolt2_Object=MibTableColumn
dupsPMINVVolt2=_DupsPMINVVolt2_Object((1,3,6,1,4,1,2254,2,5,10,6,1,8),_DupsPMINVVolt2_Type())
dupsPMINVVolt2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMINVVolt2.setStatus(_A)
if mibBuilder.loadTexts:dupsPMINVVolt2.setUnits(_L)
_DupsPMINVVolt3_Type=Integer32
_DupsPMINVVolt3_Object=MibTableColumn
dupsPMINVVolt3=_DupsPMINVVolt3_Object((1,3,6,1,4,1,2254,2,5,10,6,1,9),_DupsPMINVVolt3_Type())
dupsPMINVVolt3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMINVVolt3.setStatus(_A)
if mibBuilder.loadTexts:dupsPMINVVolt3.setUnits(_L)
class _DupsPMStsNotExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notExist',1),('existed',2)))
_DupsPMStsNotExist_Type.__name__=_D
_DupsPMStsNotExist_Object=MibTableColumn
dupsPMStsNotExist=_DupsPMStsNotExist_Object((1,3,6,1,4,1,2254,2,5,10,6,1,10),_DupsPMStsNotExist_Type())
dupsPMStsNotExist.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsNotExist.setStatus(_A)
class _DupsPMStsOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pmOff',1),('pmOn',2)))
_DupsPMStsOff_Type.__name__=_D
_DupsPMStsOff_Object=MibTableColumn
dupsPMStsOff=_DupsPMStsOff_Object((1,3,6,1,4,1,2254,2,5,10,6,1,11),_DupsPMStsOff_Type())
dupsPMStsOff.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsOff.setStatus(_A)
class _DupsPMStsRepair_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('repair',1),('notRepair',2)))
_DupsPMStsRepair_Type.__name__=_D
_DupsPMStsRepair_Object=MibTableColumn
dupsPMStsRepair=_DupsPMStsRepair_Object((1,3,6,1,4,1,2254,2,5,10,6,1,12),_DupsPMStsRepair_Type())
dupsPMStsRepair.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsRepair.setStatus(_A)
class _DupsPMStsFaultShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsFaultShutdown_Type.__name__=_D
_DupsPMStsFaultShutdown_Object=MibTableColumn
dupsPMStsFaultShutdown=_DupsPMStsFaultShutdown_Object((1,3,6,1,4,1,2254,2,5,10,6,1,13),_DupsPMStsFaultShutdown_Type())
dupsPMStsFaultShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsFaultShutdown.setStatus(_A)
class _DupsPMStsPFCFuseFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCFuseFail_Type.__name__=_D
_DupsPMStsPFCFuseFail_Object=MibTableColumn
dupsPMStsPFCFuseFail=_DupsPMStsPFCFuseFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,14),_DupsPMStsPFCFuseFail_Type())
dupsPMStsPFCFuseFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCFuseFail.setStatus(_A)
class _DupsPMStsPFCOverTempWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_I,2)))
_DupsPMStsPFCOverTempWarning_Type.__name__=_D
_DupsPMStsPFCOverTempWarning_Object=MibTableColumn
dupsPMStsPFCOverTempWarning=_DupsPMStsPFCOverTempWarning_Object((1,3,6,1,4,1,2254,2,5,10,6,1,15),_DupsPMStsPFCOverTempWarning_Type())
dupsPMStsPFCOverTempWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCOverTempWarning.setStatus(_A)
class _DupsPMStsPFCOverTempShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCOverTempShutdown_Type.__name__=_D
_DupsPMStsPFCOverTempShutdown_Object=MibTableColumn
dupsPMStsPFCOverTempShutdown=_DupsPMStsPFCOverTempShutdown_Object((1,3,6,1,4,1,2254,2,5,10,6,1,16),_DupsPMStsPFCOverTempShutdown_Type())
dupsPMStsPFCOverTempShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCOverTempShutdown.setStatus(_A)
class _DupsPMStsPFCOverVoltWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_I,2)))
_DupsPMStsPFCOverVoltWarning_Type.__name__=_D
_DupsPMStsPFCOverVoltWarning_Object=MibTableColumn
dupsPMStsPFCOverVoltWarning=_DupsPMStsPFCOverVoltWarning_Object((1,3,6,1,4,1,2254,2,5,10,6,1,17),_DupsPMStsPFCOverVoltWarning_Type())
dupsPMStsPFCOverVoltWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCOverVoltWarning.setStatus(_A)
class _DupsPMStsPFCOverVoltShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCOverVoltShutdown_Type.__name__=_D
_DupsPMStsPFCOverVoltShutdown_Object=MibTableColumn
dupsPMStsPFCOverVoltShutdown=_DupsPMStsPFCOverVoltShutdown_Object((1,3,6,1,4,1,2254,2,5,10,6,1,18),_DupsPMStsPFCOverVoltShutdown_Type())
dupsPMStsPFCOverVoltShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCOverVoltShutdown.setStatus(_A)
class _DupsPMStsPFCUnderVoltWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_I,2)))
_DupsPMStsPFCUnderVoltWarning_Type.__name__=_D
_DupsPMStsPFCUnderVoltWarning_Object=MibTableColumn
dupsPMStsPFCUnderVoltWarning=_DupsPMStsPFCUnderVoltWarning_Object((1,3,6,1,4,1,2254,2,5,10,6,1,19),_DupsPMStsPFCUnderVoltWarning_Type())
dupsPMStsPFCUnderVoltWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCUnderVoltWarning.setStatus(_A)
class _DupsPMStsPFCUnderVoltShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCUnderVoltShutdown_Type.__name__=_D
_DupsPMStsPFCUnderVoltShutdown_Object=MibTableColumn
dupsPMStsPFCUnderVoltShutdown=_DupsPMStsPFCUnderVoltShutdown_Object((1,3,6,1,4,1,2254,2,5,10,6,1,20),_DupsPMStsPFCUnderVoltShutdown_Type())
dupsPMStsPFCUnderVoltShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCUnderVoltShutdown.setStatus(_A)
class _DupsPMStsPFCGeneralFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCGeneralFault_Type.__name__=_D
_DupsPMStsPFCGeneralFault_Object=MibTableColumn
dupsPMStsPFCGeneralFault=_DupsPMStsPFCGeneralFault_Object((1,3,6,1,4,1,2254,2,5,10,6,1,21),_DupsPMStsPFCGeneralFault_Type())
dupsPMStsPFCGeneralFault.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCGeneralFault.setStatus(_A)
class _DupsPMStsPFCFanFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCFanFail_Type.__name__=_D
_DupsPMStsPFCFanFail_Object=MibTableColumn
dupsPMStsPFCFanFail=_DupsPMStsPFCFanFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,22),_DupsPMStsPFCFanFail_Type())
dupsPMStsPFCFanFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCFanFail.setStatus(_A)
class _DupsPMStsPFCCurrentLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCCurrentLimit_Type.__name__=_D
_DupsPMStsPFCCurrentLimit_Object=MibTableColumn
dupsPMStsPFCCurrentLimit=_DupsPMStsPFCCurrentLimit_Object((1,3,6,1,4,1,2254,2,5,10,6,1,23),_DupsPMStsPFCCurrentLimit_Type())
dupsPMStsPFCCurrentLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCCurrentLimit.setStatus(_A)
class _DupsPMStsPFCOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCOff_Type.__name__=_D
_DupsPMStsPFCOff_Object=MibTableColumn
dupsPMStsPFCOff=_DupsPMStsPFCOff_Object((1,3,6,1,4,1,2254,2,5,10,6,1,24),_DupsPMStsPFCOff_Type())
dupsPMStsPFCOff.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCOff.setStatus(_A)
class _DupsPMStsPFCInnerCommFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCInnerCommFail_Type.__name__=_D
_DupsPMStsPFCInnerCommFail_Object=MibTableColumn
dupsPMStsPFCInnerCommFail=_DupsPMStsPFCInnerCommFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,25),_DupsPMStsPFCInnerCommFail_Type())
dupsPMStsPFCInnerCommFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCInnerCommFail.setStatus(_A)
class _DupsPMStsPFCNotCalibrated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsPFCNotCalibrated_Type.__name__=_D
_DupsPMStsPFCNotCalibrated_Object=MibTableColumn
dupsPMStsPFCNotCalibrated=_DupsPMStsPFCNotCalibrated_Object((1,3,6,1,4,1,2254,2,5,10,6,1,26),_DupsPMStsPFCNotCalibrated_Type())
dupsPMStsPFCNotCalibrated.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsPFCNotCalibrated.setStatus(_A)
class _DupsPMStsINVFuseFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DupsPMStsINVFuseFail_Type.__name__=_D
_DupsPMStsINVFuseFail_Object=MibTableColumn
dupsPMStsINVFuseFail=_DupsPMStsINVFuseFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,27),_DupsPMStsINVFuseFail_Type())
dupsPMStsINVFuseFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVFuseFail.setStatus(_A)
class _DupsPMStsINVOverTempWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_I,2)))
_DupsPMStsINVOverTempWarning_Type.__name__=_D
_DupsPMStsINVOverTempWarning_Object=MibTableColumn
dupsPMStsINVOverTempWarning=_DupsPMStsINVOverTempWarning_Object((1,3,6,1,4,1,2254,2,5,10,6,1,28),_DupsPMStsINVOverTempWarning_Type())
dupsPMStsINVOverTempWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVOverTempWarning.setStatus(_A)
class _DupsPMStsINVOverTempShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVOverTempShutdown_Type.__name__=_D
_DupsPMStsINVOverTempShutdown_Object=MibTableColumn
dupsPMStsINVOverTempShutdown=_DupsPMStsINVOverTempShutdown_Object((1,3,6,1,4,1,2254,2,5,10,6,1,29),_DupsPMStsINVOverTempShutdown_Type())
dupsPMStsINVOverTempShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVOverTempShutdown.setStatus(_A)
class _DupsPMStsINVFanFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVFanFail_Type.__name__=_D
_DupsPMStsINVFanFail_Object=MibTableColumn
dupsPMStsINVFanFail=_DupsPMStsINVFanFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,30),_DupsPMStsINVFanFail_Type())
dupsPMStsINVFanFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVFanFail.setStatus(_A)
class _DupsPMStsINVShortCircuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVShortCircuit_Type.__name__=_D
_DupsPMStsINVShortCircuit_Object=MibTableColumn
dupsPMStsINVShortCircuit=_DupsPMStsINVShortCircuit_Object((1,3,6,1,4,1,2254,2,5,10,6,1,31),_DupsPMStsINVShortCircuit_Type())
dupsPMStsINVShortCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVShortCircuit.setStatus(_A)
class _DupsPMStsINVSTSFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVSTSFail_Type.__name__=_D
_DupsPMStsINVSTSFail_Object=MibTableColumn
dupsPMStsINVSTSFail=_DupsPMStsINVSTSFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,32),_DupsPMStsINVSTSFail_Type())
dupsPMStsINVSTSFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVSTSFail.setStatus(_A)
class _DupsPMStsINVCircuitFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVCircuitFail_Type.__name__=_D
_DupsPMStsINVCircuitFail_Object=MibTableColumn
dupsPMStsINVCircuitFail=_DupsPMStsINVCircuitFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,33),_DupsPMStsINVCircuitFail_Type())
dupsPMStsINVCircuitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVCircuitFail.setStatus(_A)
class _DupsPMStsINVOverVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVOverVolt_Type.__name__=_D
_DupsPMStsINVOverVolt_Object=MibTableColumn
dupsPMStsINVOverVolt=_DupsPMStsINVOverVolt_Object((1,3,6,1,4,1,2254,2,5,10,6,1,34),_DupsPMStsINVOverVolt_Type())
dupsPMStsINVOverVolt.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVOverVolt.setStatus(_A)
class _DupsPMStsINVOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVOverload_Type.__name__=_D
_DupsPMStsINVOverload_Object=MibTableColumn
dupsPMStsINVOverload=_DupsPMStsINVOverload_Object((1,3,6,1,4,1,2254,2,5,10,6,1,35),_DupsPMStsINVOverload_Type())
dupsPMStsINVOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVOverload.setStatus(_A)
class _DupsPMStsINVInnerCommFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVInnerCommFail_Type.__name__=_D
_DupsPMStsINVInnerCommFail_Object=MibTableColumn
dupsPMStsINVInnerCommFail=_DupsPMStsINVInnerCommFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,36),_DupsPMStsINVInnerCommFail_Type())
dupsPMStsINVInnerCommFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVInnerCommFail.setStatus(_A)
class _DupsPMStsINVEPO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVEPO_Type.__name__=_D
_DupsPMStsINVEPO_Object=MibTableColumn
dupsPMStsINVEPO=_DupsPMStsINVEPO_Object((1,3,6,1,4,1,2254,2,5,10,6,1,37),_DupsPMStsINVEPO_Type())
dupsPMStsINVEPO.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVEPO.setStatus(_A)
class _DupsPMStsINVParallelCommFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVParallelCommFail_Type.__name__=_D
_DupsPMStsINVParallelCommFail_Object=MibTableColumn
dupsPMStsINVParallelCommFail=_DupsPMStsINVParallelCommFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,38),_DupsPMStsINVParallelCommFail_Type())
dupsPMStsINVParallelCommFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVParallelCommFail.setStatus(_A)
class _DupsPMStsINVParallelFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVParallelFail_Type.__name__=_D
_DupsPMStsINVParallelFail_Object=MibTableColumn
dupsPMStsINVParallelFail=_DupsPMStsINVParallelFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,39),_DupsPMStsINVParallelFail_Type())
dupsPMStsINVParallelFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVParallelFail.setStatus(_A)
class _DupsPMStsINVSTSOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DupsPMStsINVSTSOn_Type.__name__=_D
_DupsPMStsINVSTSOn_Object=MibTableColumn
dupsPMStsINVSTSOn=_DupsPMStsINVSTSOn_Object((1,3,6,1,4,1,2254,2,5,10,6,1,40),_DupsPMStsINVSTSOn_Type())
dupsPMStsINVSTSOn.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVSTSOn.setStatus(_A)
class _DupsPMStsINVNotCalibrated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsINVNotCalibrated_Type.__name__=_D
_DupsPMStsINVNotCalibrated_Object=MibTableColumn
dupsPMStsINVNotCalibrated=_DupsPMStsINVNotCalibrated_Object((1,3,6,1,4,1,2254,2,5,10,6,1,41),_DupsPMStsINVNotCalibrated_Type())
dupsPMStsINVNotCalibrated.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsINVNotCalibrated.setStatus(_A)
class _DupsPMStsChargerFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_DupsPMStsChargerFail_Type.__name__=_D
_DupsPMStsChargerFail_Object=MibTableColumn
dupsPMStsChargerFail=_DupsPMStsChargerFail_Object((1,3,6,1,4,1,2254,2,5,10,6,1,42),_DupsPMStsChargerFail_Type())
dupsPMStsChargerFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMStsChargerFail.setStatus(_A)
class _DupsPMSummaryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('abnormal',1),(_I,2)))
_DupsPMSummaryStatus_Type.__name__=_D
_DupsPMSummaryStatus_Object=MibTableColumn
dupsPMSummaryStatus=_DupsPMSummaryStatus_Object((1,3,6,1,4,1,2254,2,5,10,6,1,43),_DupsPMSummaryStatus_Type())
dupsPMSummaryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMSummaryStatus.setStatus(_A)
_DupsPMPFCTempR_Type=Integer32
_DupsPMPFCTempR_Object=MibTableColumn
dupsPMPFCTempR=_DupsPMPFCTempR_Object((1,3,6,1,4,1,2254,2,5,10,6,1,44),_DupsPMPFCTempR_Type())
dupsPMPFCTempR.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMPFCTempR.setStatus(_A)
if mibBuilder.loadTexts:dupsPMPFCTempR.setUnits(_T)
_DupsPMPFCTempS_Type=Integer32
_DupsPMPFCTempS_Object=MibTableColumn
dupsPMPFCTempS=_DupsPMPFCTempS_Object((1,3,6,1,4,1,2254,2,5,10,6,1,45),_DupsPMPFCTempS_Type())
dupsPMPFCTempS.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMPFCTempS.setStatus(_A)
if mibBuilder.loadTexts:dupsPMPFCTempS.setUnits(_T)
_DupsPMPFCTempT_Type=Integer32
_DupsPMPFCTempT_Object=MibTableColumn
dupsPMPFCTempT=_DupsPMPFCTempT_Object((1,3,6,1,4,1,2254,2,5,10,6,1,46),_DupsPMPFCTempT_Type())
dupsPMPFCTempT.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsPMPFCTempT.setStatus(_A)
if mibBuilder.loadTexts:dupsPMPFCTempT.setUnits(_T)
_DupsTrapArgs_ObjectIdentity=ObjectIdentity
dupsTrapArgs=_DupsTrapArgs_ObjectIdentity((1,3,6,1,4,1,2254,2,5,11))
_DupsDescription_Type=DisplayString
_DupsDescription_Object=MibScalar
dupsDescription=_DupsDescription_Object((1,3,6,1,4,1,2254,2,5,11,1),_DupsDescription_Type())
dupsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsDescription.setStatus(_A)
_DupsTimeTicks_Type=TimeTicks
_DupsTimeTicks_Object=MibScalar
dupsTimeTicks=_DupsTimeTicks_Object((1,3,6,1,4,1,2254,2,5,11,2),_DupsTimeTicks_Type())
dupsTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsTimeTicks.setStatus(_A)
_DupsParallel_ObjectIdentity=ObjectIdentity
dupsParallel=_DupsParallel_ObjectIdentity((1,3,6,1,4,1,2254,2,5,12))
_DupsParallelRatingVA_Type=Integer32
_DupsParallelRatingVA_Object=MibScalar
dupsParallelRatingVA=_DupsParallelRatingVA_Object((1,3,6,1,4,1,2254,2,5,12,1),_DupsParallelRatingVA_Type())
dupsParallelRatingVA.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelRatingVA.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelRatingVA.setUnits('1 VA')
_DupsParallelRatingPower_Type=Integer32
_DupsParallelRatingPower_Object=MibScalar
dupsParallelRatingPower=_DupsParallelRatingPower_Object((1,3,6,1,4,1,2254,2,5,12,2),_DupsParallelRatingPower_Type())
dupsParallelRatingPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelRatingPower.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelRatingPower.setUnits(_O)
_DupsParallelInCurrent1_Type=Integer32
_DupsParallelInCurrent1_Object=MibScalar
dupsParallelInCurrent1=_DupsParallelInCurrent1_Object((1,3,6,1,4,1,2254,2,5,12,3),_DupsParallelInCurrent1_Type())
dupsParallelInCurrent1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelInCurrent1.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelInCurrent1.setUnits(_N)
_DupsParallelInCurrent2_Type=Integer32
_DupsParallelInCurrent2_Object=MibScalar
dupsParallelInCurrent2=_DupsParallelInCurrent2_Object((1,3,6,1,4,1,2254,2,5,12,4),_DupsParallelInCurrent2_Type())
dupsParallelInCurrent2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelInCurrent2.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelInCurrent2.setUnits(_N)
_DupsParallelInCurrent3_Type=Integer32
_DupsParallelInCurrent3_Object=MibScalar
dupsParallelInCurrent3=_DupsParallelInCurrent3_Object((1,3,6,1,4,1,2254,2,5,12,5),_DupsParallelInCurrent3_Type())
dupsParallelInCurrent3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelInCurrent3.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelInCurrent3.setUnits(_N)
_DupsParallelOutCurrent1_Type=Integer32
_DupsParallelOutCurrent1_Object=MibScalar
dupsParallelOutCurrent1=_DupsParallelOutCurrent1_Object((1,3,6,1,4,1,2254,2,5,12,6),_DupsParallelOutCurrent1_Type())
dupsParallelOutCurrent1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutCurrent1.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutCurrent1.setUnits(_N)
_DupsParallelOutCurrent2_Type=Integer32
_DupsParallelOutCurrent2_Object=MibScalar
dupsParallelOutCurrent2=_DupsParallelOutCurrent2_Object((1,3,6,1,4,1,2254,2,5,12,7),_DupsParallelOutCurrent2_Type())
dupsParallelOutCurrent2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutCurrent2.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutCurrent2.setUnits(_N)
_DupsParallelOutCurrent3_Type=Integer32
_DupsParallelOutCurrent3_Object=MibScalar
dupsParallelOutCurrent3=_DupsParallelOutCurrent3_Object((1,3,6,1,4,1,2254,2,5,12,8),_DupsParallelOutCurrent3_Type())
dupsParallelOutCurrent3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutCurrent3.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutCurrent3.setUnits(_N)
_DupsParallelOutPower1_Type=Integer32
_DupsParallelOutPower1_Object=MibScalar
dupsParallelOutPower1=_DupsParallelOutPower1_Object((1,3,6,1,4,1,2254,2,5,12,9),_DupsParallelOutPower1_Type())
dupsParallelOutPower1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutPower1.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutPower1.setUnits(_O)
_DupsParallelOutPower2_Type=Integer32
_DupsParallelOutPower2_Object=MibScalar
dupsParallelOutPower2=_DupsParallelOutPower2_Object((1,3,6,1,4,1,2254,2,5,12,10),_DupsParallelOutPower2_Type())
dupsParallelOutPower2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutPower2.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutPower2.setUnits(_O)
_DupsParallelOutPower3_Type=Integer32
_DupsParallelOutPower3_Object=MibScalar
dupsParallelOutPower3=_DupsParallelOutPower3_Object((1,3,6,1,4,1,2254,2,5,12,11),_DupsParallelOutPower3_Type())
dupsParallelOutPower3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutPower3.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutPower3.setUnits(_O)
_DupsParallelInEnergy1_Type=Integer32
_DupsParallelInEnergy1_Object=MibScalar
dupsParallelInEnergy1=_DupsParallelInEnergy1_Object((1,3,6,1,4,1,2254,2,5,12,12),_DupsParallelInEnergy1_Type())
dupsParallelInEnergy1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelInEnergy1.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelInEnergy1.setUnits(_M)
_DupsParallelInEnergy2_Type=Integer32
_DupsParallelInEnergy2_Object=MibScalar
dupsParallelInEnergy2=_DupsParallelInEnergy2_Object((1,3,6,1,4,1,2254,2,5,12,13),_DupsParallelInEnergy2_Type())
dupsParallelInEnergy2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelInEnergy2.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelInEnergy2.setUnits(_M)
_DupsParallelInEnergy3_Type=Integer32
_DupsParallelInEnergy3_Object=MibScalar
dupsParallelInEnergy3=_DupsParallelInEnergy3_Object((1,3,6,1,4,1,2254,2,5,12,14),_DupsParallelInEnergy3_Type())
dupsParallelInEnergy3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelInEnergy3.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelInEnergy3.setUnits(_M)
_DupsParallelInEnergyTotal_Type=Integer32
_DupsParallelInEnergyTotal_Object=MibScalar
dupsParallelInEnergyTotal=_DupsParallelInEnergyTotal_Object((1,3,6,1,4,1,2254,2,5,12,15),_DupsParallelInEnergyTotal_Type())
dupsParallelInEnergyTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelInEnergyTotal.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelInEnergyTotal.setUnits(_M)
_DupsParallelOutEnergy1_Type=Integer32
_DupsParallelOutEnergy1_Object=MibScalar
dupsParallelOutEnergy1=_DupsParallelOutEnergy1_Object((1,3,6,1,4,1,2254,2,5,12,16),_DupsParallelOutEnergy1_Type())
dupsParallelOutEnergy1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutEnergy1.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutEnergy1.setUnits(_M)
_DupsParallelOutEnergy2_Type=Integer32
_DupsParallelOutEnergy2_Object=MibScalar
dupsParallelOutEnergy2=_DupsParallelOutEnergy2_Object((1,3,6,1,4,1,2254,2,5,12,17),_DupsParallelOutEnergy2_Type())
dupsParallelOutEnergy2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutEnergy2.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutEnergy2.setUnits(_M)
_DupsParallelOutEnergy3_Type=Integer32
_DupsParallelOutEnergy3_Object=MibScalar
dupsParallelOutEnergy3=_DupsParallelOutEnergy3_Object((1,3,6,1,4,1,2254,2,5,12,18),_DupsParallelOutEnergy3_Type())
dupsParallelOutEnergy3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutEnergy3.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutEnergy3.setUnits(_M)
_DupsParallelOutEnergyTotal_Type=Integer32
_DupsParallelOutEnergyTotal_Object=MibScalar
dupsParallelOutEnergyTotal=_DupsParallelOutEnergyTotal_Object((1,3,6,1,4,1,2254,2,5,12,19),_DupsParallelOutEnergyTotal_Type())
dupsParallelOutEnergyTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsParallelOutEnergyTotal.setStatus(_A)
if mibBuilder.loadTexts:dupsParallelOutEnergyTotal.setUnits(_M)
_DupsIntegrated_ObjectIdentity=ObjectIdentity
dupsIntegrated=_DupsIntegrated_ObjectIdentity((1,3,6,1,4,1,2254,2,5,13))
class _DupsIntegratedParallel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('parallel',1),('noParallel',2)))
_DupsIntegratedParallel_Type.__name__=_D
_DupsIntegratedParallel_Object=MibScalar
dupsIntegratedParallel=_DupsIntegratedParallel_Object((1,3,6,1,4,1,2254,2,5,13,1),_DupsIntegratedParallel_Type())
dupsIntegratedParallel.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsIntegratedParallel.setStatus(_A)
class _DupsIntegratedDryInput1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_DupsIntegratedDryInput1_Type.__name__=_D
_DupsIntegratedDryInput1_Object=MibScalar
dupsIntegratedDryInput1=_DupsIntegratedDryInput1_Object((1,3,6,1,4,1,2254,2,5,13,2),_DupsIntegratedDryInput1_Type())
dupsIntegratedDryInput1.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsIntegratedDryInput1.setStatus(_A)
class _DupsIntegratedDryInput2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_DupsIntegratedDryInput2_Type.__name__=_D
_DupsIntegratedDryInput2_Object=MibScalar
dupsIntegratedDryInput2=_DupsIntegratedDryInput2_Object((1,3,6,1,4,1,2254,2,5,13,3),_DupsIntegratedDryInput2_Type())
dupsIntegratedDryInput2.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsIntegratedDryInput2.setStatus(_A)
class _DupsIntegratedDryInput3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_DupsIntegratedDryInput3_Type.__name__=_D
_DupsIntegratedDryInput3_Object=MibScalar
dupsIntegratedDryInput3=_DupsIntegratedDryInput3_Object((1,3,6,1,4,1,2254,2,5,13,4),_DupsIntegratedDryInput3_Type())
dupsIntegratedDryInput3.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsIntegratedDryInput3.setStatus(_A)
class _DupsIntegratedDryInput4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_DupsIntegratedDryInput4_Type.__name__=_D
_DupsIntegratedDryInput4_Object=MibScalar
dupsIntegratedDryInput4=_DupsIntegratedDryInput4_Object((1,3,6,1,4,1,2254,2,5,13,5),_DupsIntegratedDryInput4_Type())
dupsIntegratedDryInput4.setMaxAccess(_B)
if mibBuilder.loadTexts:dupsIntegratedDryInput4.setStatus(_A)
_DupsTraps_ObjectIdentity=ObjectIdentity
dupsTraps=_DupsTraps_ObjectIdentity((1,3,6,1,4,1,2254,2,5,20))
dupsCommunicationLost=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,1))
dupsCommunicationLost.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsCommunicationLost.setStatus('')
dupsCommunicationEstablished=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,2))
dupsCommunicationEstablished.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsCommunicationEstablished.setStatus('')
dupsPowerFail=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,3))
dupsPowerFail.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsPowerFail.setStatus('')
dupsPowerRestored=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,4))
dupsPowerRestored.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsPowerRestored.setStatus('')
dupsLowBattery=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,5))
dupsLowBattery.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsLowBattery.setStatus('')
dupsReturnFromLowBattery=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,6))
dupsReturnFromLowBattery.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromLowBattery.setStatus('')
dupsLoadOnBypass=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,7))
dupsLoadOnBypass.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsLoadOnBypass.setStatus('')
dupsNoLongerLoadOnBypass=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,8))
dupsNoLongerLoadOnBypass.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsNoLongerLoadOnBypass.setStatus('')
dupsUPSFault=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,9))
dupsUPSFault.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsUPSFault.setStatus('')
dupsReturnFromUPSFault=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,10))
dupsReturnFromUPSFault.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromUPSFault.setStatus('')
dupsBatteryGroundFault=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,11))
dupsBatteryGroundFault.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsBatteryGroundFault.setStatus('')
dupsNoLongerBatteryFault=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,12))
dupsNoLongerBatteryFault.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsNoLongerBatteryFault.setStatus('')
dupsTestInProgress=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,13))
dupsTestInProgress.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsTestInProgress.setStatus('')
dupsBatteryTestFail=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,14))
dupsBatteryTestFail.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsBatteryTestFail.setStatus('')
dupsFuseFailure=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,15))
dupsFuseFailure.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsFuseFailure.setStatus('')
dupsFuseRecovered=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,16))
dupsFuseRecovered.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsFuseRecovered.setStatus('')
dupsOutputOverload=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,17))
dupsOutputOverload.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsOutputOverload.setStatus('')
dupsNoLongerOverload=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,18))
dupsNoLongerOverload.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsNoLongerOverload.setStatus('')
dupsInverterAbnormal=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,19))
dupsInverterAbnormal.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsInverterAbnormal.setStatus('')
dupsInverterRecovered=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,20))
dupsInverterRecovered.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsInverterRecovered.setStatus('')
dupsSmartShutdownInit=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,21))
dupsSmartShutdownInit.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsSmartShutdownInit.setStatus('')
dupsCancelShutdown=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,22))
dupsCancelShutdown.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsCancelShutdown.setStatus('')
dupsTestCompleted=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,23))
dupsTestCompleted.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsTestCompleted.setStatus('')
dupsEPOON=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,24))
dupsEPOON.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsEPOON.setStatus('')
dupsEPOOFF=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,25))
dupsEPOOFF.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsEPOOFF.setStatus('')
dupsTemperatureAlarm=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,26))
dupsTemperatureAlarm.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsTemperatureAlarm.setStatus('')
dupsTemperatureNormal=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,27))
dupsTemperatureNormal.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsTemperatureNormal.setStatus('')
dupsBattReplace=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,28))
dupsBattReplace.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsBattReplace.setStatus('')
dupsReturnFromBattReplace=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,29))
dupsReturnFromBattReplace.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromBattReplace.setStatus('')
dupsOutputOff=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,30))
dupsOutputOff.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsOutputOff.setStatus('')
dupsReturnFromOutputOff=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,31))
dupsReturnFromOutputOff.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromOutputOff.setStatus('')
dupsShutdown=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,32))
dupsShutdown.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsShutdown.setStatus('')
dupsReturnFromShutdown=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,33))
dupsReturnFromShutdown.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromShutdown.setStatus('')
dupsChargerFail=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,34))
dupsChargerFail.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsChargerFail.setStatus('')
dupsReturnFromChargerFail=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,35))
dupsReturnFromChargerFail.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromChargerFail.setStatus('')
dupsOnStandby=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,36))
dupsOnStandby.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsOnStandby.setStatus('')
dupsReturnFromStandby=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,37))
dupsReturnFromStandby.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromStandby.setStatus('')
dupsFanFail=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,38))
dupsFanFail.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsFanFail.setStatus('')
dupsReturnFromFanFail=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,39))
dupsReturnFromFanFail.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromFanFail.setStatus('')
dupsOnEconomic=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,40))
dupsOnEconomic.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsOnEconomic.setStatus('')
dupsReturnFromEconomic=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,41))
dupsReturnFromEconomic.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromEconomic.setStatus('')
dupsPowerModuleFail=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,42))
dupsPowerModuleFail.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsPowerModuleFail.setStatus('')
dupsReturnFromPowerModuleFail=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,43))
dupsReturnFromPowerModuleFail.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromPowerModuleFail.setStatus('')
dupsOutputBreakerOff=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,44))
dupsOutputBreakerOff.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsOutputBreakerOff.setStatus('')
dupsReturnFromOutputBreakerOff=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,45))
dupsReturnFromOutputBreakerOff.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromOutputBreakerOff.setStatus('')
dupsBatteryDepleted=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,46))
dupsBatteryDepleted.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsBatteryDepleted.setStatus('')
dupsReturnFromBatteryDepleted=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,47))
dupsReturnFromBatteryDepleted.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromBatteryDepleted.setStatus('')
dupsLoadOnManualBypass=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,48))
dupsLoadOnManualBypass.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsLoadOnManualBypass.setStatus('')
dupsNoLongerLoadOnManualBypass=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,49))
dupsNoLongerLoadOnManualBypass.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsNoLongerLoadOnManualBypass.setStatus('')
dupsBatteryBreakerOpen=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,50))
dupsBatteryBreakerOpen.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsBatteryBreakerOpen.setStatus('')
dupsReturnFromBatteryBreakerOpen=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,51))
dupsReturnFromBatteryBreakerOpen.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromBatteryBreakerOpen.setStatus('')
dupsOutletBankOn=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,52))
dupsOutletBankOn.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsOutletBankOn.setStatus('')
dupsOutletBankOff=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,53))
dupsOutletBankOff.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsOutletBankOff.setStatus('')
dupsRedundancyLoss=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,54))
dupsRedundancyLoss.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsRedundancyLoss.setStatus('')
dupsReturnFromRedundancyLoss=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,55))
dupsReturnFromRedundancyLoss.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromRedundancyLoss.setStatus('')
dupsPhaseAsynchronous=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,56))
dupsPhaseAsynchronous.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsPhaseAsynchronous.setStatus('')
dupsReturnFromPhaseAsynchronous=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,57))
dupsReturnFromPhaseAsynchronous.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromPhaseAsynchronous.setStatus('')
dupsRectifierAbnormal=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,58))
dupsRectifierAbnormal.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsRectifierAbnormal.setStatus('')
dupsReturnFromRectifierAbnormal=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,59))
dupsReturnFromRectifierAbnormal.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromRectifierAbnormal.setStatus('')
dupsBypassBreakerOpen=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,60))
dupsBypassBreakerOpen.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsBypassBreakerOpen.setStatus('')
dupsReturnFromBypassBreakerOpen=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,61))
dupsReturnFromBypassBreakerOpen.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromBypassBreakerOpen.setStatus('')
dupsMainInputBreakerOpen=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,62))
dupsMainInputBreakerOpen.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsMainInputBreakerOpen.setStatus('')
dupsReturnFromMainInputBreakerOpen=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,63))
dupsReturnFromMainInputBreakerOpen.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromMainInputBreakerOpen.setStatus('')
dupsManualBypassBreakerOpen=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,64))
dupsManualBypassBreakerOpen.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsManualBypassBreakerOpen.setStatus('')
dupsReturnFromManualBypassBreakerOpen=NotificationType((1,3,6,1,4,1,2254,2,5,20,0,65))
dupsReturnFromManualBypassBreakerOpen.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:dupsReturnFromManualBypassBreakerOpen.setStatus('')
mibBuilder.exportSymbols(_C,**{'delta':delta,'ups':ups,'upsv5':upsv5,'dupsIdent':dupsIdent,'dupsIdentManufacturer':dupsIdentManufacturer,'dupsIdentModel':dupsIdentModel,'dupsIdentUPSSoftwareVersion':dupsIdentUPSSoftwareVersion,'dupsIdentAgentSoftwareVersion':dupsIdentAgentSoftwareVersion,'dupsIdentName':dupsIdentName,'dupsAttachedDevices':dupsAttachedDevices,'dupsRatingOutputVA':dupsRatingOutputVA,'dupsRatingOutputVoltage':dupsRatingOutputVoltage,'dupsRatingOutputFrequency':dupsRatingOutputFrequency,'dupsRatingInputVoltage':dupsRatingInputVoltage,'dupsRatingInputFrequency':dupsRatingInputFrequency,'dupsRatingBatteryVoltage':dupsRatingBatteryVoltage,'dupsLowTransferVoltUpBound':dupsLowTransferVoltUpBound,'dupsLowTransferVoltLowBound':dupsLowTransferVoltLowBound,'dupsHighTransferVoltUpBound':dupsHighTransferVoltUpBound,'dupsHighTransferVoltLowBound':dupsHighTransferVoltLowBound,'dupsLowBattTime':dupsLowBattTime,'dupsOutletRelays':dupsOutletRelays,'dupsType':dupsType,'dupsControl':dupsControl,'dupsShutdownType':dupsShutdownType,'dupsAutoReboot':dupsAutoReboot,'dupsShutdownAction':dupsShutdownAction,'dupsRestartAction':dupsRestartAction,'dupsSetOutletRelay':dupsSetOutletRelay,'dupsRelayOffDelay':dupsRelayOffDelay,'dupsRelayOnDelay':dupsRelayOnDelay,'dupsSmartShutdown':dupsSmartShutdown,'dupsClearEnergy':dupsClearEnergy,'dupsConfig':dupsConfig,'dupsConfigBuzzerAlarm':dupsConfigBuzzerAlarm,'dupsConfigBuzzerState':dupsConfigBuzzerState,'dupsConfigSensitivity':dupsConfigSensitivity,'dupsConfigLowVoltageTransferPoint':dupsConfigLowVoltageTransferPoint,'dupsConfigHighVoltageTransferPoint':dupsConfigHighVoltageTransferPoint,'dupsConfigUPSBootDelay':dupsConfigUPSBootDelay,'dupsConfigExternalBatteryPack':dupsConfigExternalBatteryPack,'dupsConfigSmartShutdownOSDelay':dupsConfigSmartShutdownOSDelay,'dupsConfigSmartShutdownUPSDelay':dupsConfigSmartShutdownUPSDelay,'dupsConfigEconomicMode':dupsConfigEconomicMode,'dupsInput':dupsInput,'dupsInputNumLines':dupsInputNumLines,'dupsInputFrequency1':dupsInputFrequency1,'dupsInputVoltage1':dupsInputVoltage1,'dupsInputVoltage12':dupsInputVoltage12,'dupsInputCurrent1':dupsInputCurrent1,'dupsInputPower1':dupsInputPower1,'dupsInputFrequency2':dupsInputFrequency2,'dupsInputVoltage2':dupsInputVoltage2,'dupsInputVoltage23':dupsInputVoltage23,'dupsInputCurrent2':dupsInputCurrent2,'dupsInputPower2':dupsInputPower2,'dupsInputFrequency3':dupsInputFrequency3,'dupsInputVoltage3':dupsInputVoltage3,'dupsInputVoltage31':dupsInputVoltage31,'dupsInputCurrent3':dupsInputCurrent3,'dupsInputPower3':dupsInputPower3,'dupsInputEnergy1':dupsInputEnergy1,'dupsInputEnergy2':dupsInputEnergy2,'dupsInputEnergy3':dupsInputEnergy3,'dupsInputEnergyTotal':dupsInputEnergyTotal,'dupsInputLineFailCause':dupsInputLineFailCause,'dupsInputBadStatus':dupsInputBadStatus,'dupsOutput':dupsOutput,'dupsOutputSource':dupsOutputSource,'dupsOutputFrequency':dupsOutputFrequency,'dupsOutputNumLines':dupsOutputNumLines,'dupsOutputVoltage1':dupsOutputVoltage1,'dupsOutputVoltage12':dupsOutputVoltage12,'dupsOutputCurrent1':dupsOutputCurrent1,'dupsOutputPower1':dupsOutputPower1,'dupsOutputLoad1':dupsOutputLoad1,'dupsOutputVoltage2':dupsOutputVoltage2,'dupsOutputVoltage23':dupsOutputVoltage23,'dupsOutputCurrent2':dupsOutputCurrent2,'dupsOutputPower2':dupsOutputPower2,'dupsOutputLoad2':dupsOutputLoad2,'dupsOutputVoltage3':dupsOutputVoltage3,'dupsOutputVoltage31':dupsOutputVoltage31,'dupsOutputCurrent3':dupsOutputCurrent3,'dupsOutputPower3':dupsOutputPower3,'dupsOutputLoad3':dupsOutputLoad3,'dupsOutputTotalActivePower':dupsOutputTotalActivePower,'dupsOutputTotalApparentPower':dupsOutputTotalApparentPower,'dupsOutputTotalPowerFactor':dupsOutputTotalPowerFactor,'dupsOutputEnergy1':dupsOutputEnergy1,'dupsOutputEnergy2':dupsOutputEnergy2,'dupsOutputEnergy3':dupsOutputEnergy3,'dupsOutputEnergyTotal':dupsOutputEnergyTotal,'dupsBypass':dupsBypass,'dupsBypassFrequency':dupsBypassFrequency,'dupsBypassNumLines':dupsBypassNumLines,'dupsBypassVoltage1':dupsBypassVoltage1,'dupsBypassVoltage12':dupsBypassVoltage12,'dupsBypassCurrent1':dupsBypassCurrent1,'dupsBypassPower1':dupsBypassPower1,'dupsBypassVoltage2':dupsBypassVoltage2,'dupsBypassVoltage23':dupsBypassVoltage23,'dupsBypassCurrent2':dupsBypassCurrent2,'dupsBypassPower2':dupsBypassPower2,'dupsBypassVoltage3':dupsBypassVoltage3,'dupsBypassVoltage31':dupsBypassVoltage31,'dupsBypassCurrent3':dupsBypassCurrent3,'dupsBypassPower3':dupsBypassPower3,'dupsBypassSTSTemperature':dupsBypassSTSTemperature,'dupsBattery':dupsBattery,'dupsBatteryCondition':dupsBatteryCondition,'dupsBatteryStatus':dupsBatteryStatus,'dupsBatteryCharge':dupsBatteryCharge,'dupsSecondsOnBattery':dupsSecondsOnBattery,'dupsBatteryEstimatedTime':dupsBatteryEstimatedTime,'dupsBatteryPosVoltage':dupsBatteryPosVoltage,'dupsBatteryNegVoltage':dupsBatteryNegVoltage,'dupsBatteryPosCurrent':dupsBatteryPosCurrent,'dupsBatteryNegCurrent':dupsBatteryNegCurrent,'dupsBatteryPosCapacity':dupsBatteryPosCapacity,'dupsBatteryNegCapacity':dupsBatteryNegCapacity,'dupsTemperature':dupsTemperature,'dupsLastReplaceDate':dupsLastReplaceDate,'dupsNextReplaceDate':dupsNextReplaceDate,'dupsBatteryBreaker':dupsBatteryBreaker,'dupsBatteryCab1Tempurature':dupsBatteryCab1Tempurature,'dupsBatteryCab2Tempurature':dupsBatteryCab2Tempurature,'dupsBatteryCab3Tempurature':dupsBatteryCab3Tempurature,'dupsBatteryCab4Tempurature':dupsBatteryCab4Tempurature,'dupsTest':dupsTest,'dupsTestType':dupsTestType,'dupsTestResultsSummary':dupsTestResultsSummary,'dupsTestResultsDetail':dupsTestResultsDetail,'dupsGeneratorTest':dupsGeneratorTest,'dupsGeneratorTestStatus':dupsGeneratorTestStatus,'dupsAlarm':dupsAlarm,'dupsAlarmDisconnect':dupsAlarmDisconnect,'dupsAlarmInputOutOfRange':dupsAlarmInputOutOfRange,'dupsAlarmBatteryLow':dupsAlarmBatteryLow,'dupsAlarmLoadOnBypass':dupsAlarmLoadOnBypass,'dupsAlarmOther':dupsAlarmOther,'dupsAlarmBatteryGroundFault':dupsAlarmBatteryGroundFault,'dupsAlarmTestInProgress':dupsAlarmTestInProgress,'dupsAlarmBatteryTestFail':dupsAlarmBatteryTestFail,'dupsAlarmFuseFailure':dupsAlarmFuseFailure,'dupsAlarmOutputOverload':dupsAlarmOutputOverload,'dupsAlarmInverterAbnormal':dupsAlarmInverterAbnormal,'dupsAlarmLoadOnReserve':dupsAlarmLoadOnReserve,'dupsAlarmTemperature':dupsAlarmTemperature,'dupsAlarmBypassOutOfRange':dupsAlarmBypassOutOfRange,'dupsAlarmStandby':dupsAlarmStandby,'dupsAlarmChargerFail':dupsAlarmChargerFail,'dupsAlarmFanFail':dupsAlarmFanFail,'dupsAlarmEconomicMode':dupsAlarmEconomicMode,'dupsAlarmOutputOff':dupsAlarmOutputOff,'dupsAlarmSmartShutdown':dupsAlarmSmartShutdown,'dupsAlarmEmergencyPowerOff':dupsAlarmEmergencyPowerOff,'dupsAlarmUPSShutdown':dupsAlarmUPSShutdown,'dupsAlarmEPO':dupsAlarmEPO,'dupsAlarmOutVoltOverLimit':dupsAlarmOutVoltOverLimit,'dupsAlarmOutVoltUnderLimit':dupsAlarmOutVoltUnderLimit,'dupsAlarmPowerModule':dupsAlarmPowerModule,'dupsAlarmOutputBreaker':dupsAlarmOutputBreaker,'dupsAlarmOutletBank1Breaker':dupsAlarmOutletBank1Breaker,'dupsAlarmOutletBank2Breaker':dupsAlarmOutletBank2Breaker,'dupsAlarmOutletBank3Breaker':dupsAlarmOutletBank3Breaker,'dupsAlarmOutletBank4Breaker':dupsAlarmOutletBank4Breaker,'dupsAlarmSummary':dupsAlarmSummary,'dupsAlarmRedundancyLoss':dupsAlarmRedundancyLoss,'dupsAlarmPhaseAsynchronous':dupsAlarmPhaseAsynchronous,'dupsAlarmRectifierAbnormal':dupsAlarmRectifierAbnormal,'dupsAlarmBypassBreakerOpen':dupsAlarmBypassBreakerOpen,'dupsAlarmMainInputBreakerOpen':dupsAlarmMainInputBreakerOpen,'dupsAlarmManualBypassBreaker':dupsAlarmManualBypassBreaker,'dupsPowerModule':dupsPowerModule,'dupsPMBypassInputAlarm':dupsPMBypassInputAlarm,'dupsPMBypassPhaseAlarm':dupsPMBypassPhaseAlarm,'dupsPMBypassSTSOverloadAlarm':dupsPMBypassSTSOverloadAlarm,'dupsPMBypassSTSOverTempAlarm':dupsPMBypassSTSOverTempAlarm,'dupsPMBypassSTSFailAlarm':dupsPMBypassSTSFailAlarm,'dupsPMTable':dupsPMTable,'dupsPMEntry':dupsPMEntry,_g:dupsPMID,'dupsPMPFCTemp':dupsPMPFCTemp,'dupsPMINVTemp':dupsPMINVTemp,'dupsPMINVTempR':dupsPMINVTempR,'dupsPMINVTempS':dupsPMINVTempS,'dupsPMINVTempT':dupsPMINVTempT,'dupsPMINVVolt1':dupsPMINVVolt1,'dupsPMINVVolt2':dupsPMINVVolt2,'dupsPMINVVolt3':dupsPMINVVolt3,'dupsPMStsNotExist':dupsPMStsNotExist,'dupsPMStsOff':dupsPMStsOff,'dupsPMStsRepair':dupsPMStsRepair,'dupsPMStsFaultShutdown':dupsPMStsFaultShutdown,'dupsPMStsPFCFuseFail':dupsPMStsPFCFuseFail,'dupsPMStsPFCOverTempWarning':dupsPMStsPFCOverTempWarning,'dupsPMStsPFCOverTempShutdown':dupsPMStsPFCOverTempShutdown,'dupsPMStsPFCOverVoltWarning':dupsPMStsPFCOverVoltWarning,'dupsPMStsPFCOverVoltShutdown':dupsPMStsPFCOverVoltShutdown,'dupsPMStsPFCUnderVoltWarning':dupsPMStsPFCUnderVoltWarning,'dupsPMStsPFCUnderVoltShutdown':dupsPMStsPFCUnderVoltShutdown,'dupsPMStsPFCGeneralFault':dupsPMStsPFCGeneralFault,'dupsPMStsPFCFanFail':dupsPMStsPFCFanFail,'dupsPMStsPFCCurrentLimit':dupsPMStsPFCCurrentLimit,'dupsPMStsPFCOff':dupsPMStsPFCOff,'dupsPMStsPFCInnerCommFail':dupsPMStsPFCInnerCommFail,'dupsPMStsPFCNotCalibrated':dupsPMStsPFCNotCalibrated,'dupsPMStsINVFuseFail':dupsPMStsINVFuseFail,'dupsPMStsINVOverTempWarning':dupsPMStsINVOverTempWarning,'dupsPMStsINVOverTempShutdown':dupsPMStsINVOverTempShutdown,'dupsPMStsINVFanFail':dupsPMStsINVFanFail,'dupsPMStsINVShortCircuit':dupsPMStsINVShortCircuit,'dupsPMStsINVSTSFail':dupsPMStsINVSTSFail,'dupsPMStsINVCircuitFail':dupsPMStsINVCircuitFail,'dupsPMStsINVOverVolt':dupsPMStsINVOverVolt,'dupsPMStsINVOverload':dupsPMStsINVOverload,'dupsPMStsINVInnerCommFail':dupsPMStsINVInnerCommFail,'dupsPMStsINVEPO':dupsPMStsINVEPO,'dupsPMStsINVParallelCommFail':dupsPMStsINVParallelCommFail,'dupsPMStsINVParallelFail':dupsPMStsINVParallelFail,'dupsPMStsINVSTSOn':dupsPMStsINVSTSOn,'dupsPMStsINVNotCalibrated':dupsPMStsINVNotCalibrated,'dupsPMStsChargerFail':dupsPMStsChargerFail,'dupsPMSummaryStatus':dupsPMSummaryStatus,'dupsPMPFCTempR':dupsPMPFCTempR,'dupsPMPFCTempS':dupsPMPFCTempS,'dupsPMPFCTempT':dupsPMPFCTempT,'dupsTrapArgs':dupsTrapArgs,_F:dupsDescription,_E:dupsTimeTicks,'dupsParallel':dupsParallel,'dupsParallelRatingVA':dupsParallelRatingVA,'dupsParallelRatingPower':dupsParallelRatingPower,'dupsParallelInCurrent1':dupsParallelInCurrent1,'dupsParallelInCurrent2':dupsParallelInCurrent2,'dupsParallelInCurrent3':dupsParallelInCurrent3,'dupsParallelOutCurrent1':dupsParallelOutCurrent1,'dupsParallelOutCurrent2':dupsParallelOutCurrent2,'dupsParallelOutCurrent3':dupsParallelOutCurrent3,'dupsParallelOutPower1':dupsParallelOutPower1,'dupsParallelOutPower2':dupsParallelOutPower2,'dupsParallelOutPower3':dupsParallelOutPower3,'dupsParallelInEnergy1':dupsParallelInEnergy1,'dupsParallelInEnergy2':dupsParallelInEnergy2,'dupsParallelInEnergy3':dupsParallelInEnergy3,'dupsParallelInEnergyTotal':dupsParallelInEnergyTotal,'dupsParallelOutEnergy1':dupsParallelOutEnergy1,'dupsParallelOutEnergy2':dupsParallelOutEnergy2,'dupsParallelOutEnergy3':dupsParallelOutEnergy3,'dupsParallelOutEnergyTotal':dupsParallelOutEnergyTotal,'dupsIntegrated':dupsIntegrated,'dupsIntegratedParallel':dupsIntegratedParallel,'dupsIntegratedDryInput1':dupsIntegratedDryInput1,'dupsIntegratedDryInput2':dupsIntegratedDryInput2,'dupsIntegratedDryInput3':dupsIntegratedDryInput3,'dupsIntegratedDryInput4':dupsIntegratedDryInput4,'dupsTraps':dupsTraps,'dupsCommunicationLost':dupsCommunicationLost,'dupsCommunicationEstablished':dupsCommunicationEstablished,'dupsPowerFail':dupsPowerFail,'dupsPowerRestored':dupsPowerRestored,'dupsLowBattery':dupsLowBattery,'dupsReturnFromLowBattery':dupsReturnFromLowBattery,'dupsLoadOnBypass':dupsLoadOnBypass,'dupsNoLongerLoadOnBypass':dupsNoLongerLoadOnBypass,'dupsUPSFault':dupsUPSFault,'dupsReturnFromUPSFault':dupsReturnFromUPSFault,'dupsBatteryGroundFault':dupsBatteryGroundFault,'dupsNoLongerBatteryFault':dupsNoLongerBatteryFault,'dupsTestInProgress':dupsTestInProgress,'dupsBatteryTestFail':dupsBatteryTestFail,'dupsFuseFailure':dupsFuseFailure,'dupsFuseRecovered':dupsFuseRecovered,'dupsOutputOverload':dupsOutputOverload,'dupsNoLongerOverload':dupsNoLongerOverload,'dupsInverterAbnormal':dupsInverterAbnormal,'dupsInverterRecovered':dupsInverterRecovered,'dupsSmartShutdownInit':dupsSmartShutdownInit,'dupsCancelShutdown':dupsCancelShutdown,'dupsTestCompleted':dupsTestCompleted,'dupsEPOON':dupsEPOON,'dupsEPOOFF':dupsEPOOFF,'dupsTemperatureAlarm':dupsTemperatureAlarm,'dupsTemperatureNormal':dupsTemperatureNormal,'dupsBattReplace':dupsBattReplace,'dupsReturnFromBattReplace':dupsReturnFromBattReplace,'dupsOutputOff':dupsOutputOff,'dupsReturnFromOutputOff':dupsReturnFromOutputOff,'dupsShutdown':dupsShutdown,'dupsReturnFromShutdown':dupsReturnFromShutdown,'dupsChargerFail':dupsChargerFail,'dupsReturnFromChargerFail':dupsReturnFromChargerFail,'dupsOnStandby':dupsOnStandby,'dupsReturnFromStandby':dupsReturnFromStandby,'dupsFanFail':dupsFanFail,'dupsReturnFromFanFail':dupsReturnFromFanFail,'dupsOnEconomic':dupsOnEconomic,'dupsReturnFromEconomic':dupsReturnFromEconomic,'dupsPowerModuleFail':dupsPowerModuleFail,'dupsReturnFromPowerModuleFail':dupsReturnFromPowerModuleFail,'dupsOutputBreakerOff':dupsOutputBreakerOff,'dupsReturnFromOutputBreakerOff':dupsReturnFromOutputBreakerOff,'dupsBatteryDepleted':dupsBatteryDepleted,'dupsReturnFromBatteryDepleted':dupsReturnFromBatteryDepleted,'dupsLoadOnManualBypass':dupsLoadOnManualBypass,'dupsNoLongerLoadOnManualBypass':dupsNoLongerLoadOnManualBypass,'dupsBatteryBreakerOpen':dupsBatteryBreakerOpen,'dupsReturnFromBatteryBreakerOpen':dupsReturnFromBatteryBreakerOpen,'dupsOutletBankOn':dupsOutletBankOn,'dupsOutletBankOff':dupsOutletBankOff,'dupsRedundancyLoss':dupsRedundancyLoss,'dupsReturnFromRedundancyLoss':dupsReturnFromRedundancyLoss,'dupsPhaseAsynchronous':dupsPhaseAsynchronous,'dupsReturnFromPhaseAsynchronous':dupsReturnFromPhaseAsynchronous,'dupsRectifierAbnormal':dupsRectifierAbnormal,'dupsReturnFromRectifierAbnormal':dupsReturnFromRectifierAbnormal,'dupsBypassBreakerOpen':dupsBypassBreakerOpen,'dupsReturnFromBypassBreakerOpen':dupsReturnFromBypassBreakerOpen,'dupsMainInputBreakerOpen':dupsMainInputBreakerOpen,'dupsReturnFromMainInputBreakerOpen':dupsReturnFromMainInputBreakerOpen,'dupsManualBypassBreakerOpen':dupsManualBypassBreakerOpen,'dupsReturnFromManualBypassBreakerOpen':dupsReturnFromManualBypassBreakerOpen})