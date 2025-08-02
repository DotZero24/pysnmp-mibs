_J='adicomUpsBypassLineIndex'
_I='adicomUpsOutputLineIndex'
_H='adicomUpsInputLineIndex'
_G='NotificationType'
_F='DisplayString'
_E='Integer32'
_D='adicomUpsAgentTrapString'
_C='SOCOMECUPS-ADICOM-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TestAndIncr,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_F,'PhysAddress','TextualConvention','TestAndIncr','TimeInterval','TimeStamp')
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NonNegativeInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SocomecUPS_ObjectIdentity=ObjectIdentity
socomecUPS=_SocomecUPS_ObjectIdentity((1,3,6,1,4,1,4555))
_Software_ObjectIdentity=ObjectIdentity
software=_Software_ObjectIdentity((1,3,6,1,4,1,4555,1))
_Network_ObjectIdentity=ObjectIdentity
network=_Network_ObjectIdentity((1,3,6,1,4,1,4555,1,1))
_AdicomUps_ObjectIdentity=ObjectIdentity
adicomUps=_AdicomUps_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5))
_AdicomUpsObjects_ObjectIdentity=ObjectIdentity
adicomUpsObjects=_AdicomUpsObjects_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,1))
_AdicomUpsIdent_ObjectIdentity=ObjectIdentity
adicomUpsIdent=_AdicomUpsIdent_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,1,1))
class _AdicomUpsIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AdicomUpsIdentModel_Type.__name__=_F
_AdicomUpsIdentModel_Object=MibScalar
adicomUpsIdentModel=_AdicomUpsIdentModel_Object((1,3,6,1,4,1,4555,1,1,5,1,1,1),_AdicomUpsIdentModel_Type())
adicomUpsIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsIdentModel.setStatus(_A)
class _AdicomUpsIdentSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AdicomUpsIdentSerialNumber_Type.__name__=_F
_AdicomUpsIdentSerialNumber_Object=MibScalar
adicomUpsIdentSerialNumber=_AdicomUpsIdentSerialNumber_Object((1,3,6,1,4,1,4555,1,1,5,1,1,2),_AdicomUpsIdentSerialNumber_Type())
adicomUpsIdentSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsIdentSerialNumber.setStatus(_A)
class _AdicomUpsIdentFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AdicomUpsIdentFirmwareVersion_Type.__name__=_F
_AdicomUpsIdentFirmwareVersion_Object=MibScalar
adicomUpsIdentFirmwareVersion=_AdicomUpsIdentFirmwareVersion_Object((1,3,6,1,4,1,4555,1,1,5,1,1,3),_AdicomUpsIdentFirmwareVersion_Type())
adicomUpsIdentFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsIdentFirmwareVersion.setStatus(_A)
class _AdicomUpsIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AdicomUpsIdentAgentSoftwareVersion_Type.__name__=_F
_AdicomUpsIdentAgentSoftwareVersion_Object=MibScalar
adicomUpsIdentAgentSoftwareVersion=_AdicomUpsIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,4555,1,1,5,1,1,4),_AdicomUpsIdentAgentSoftwareVersion_Type())
adicomUpsIdentAgentSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsIdentAgentSoftwareVersion.setStatus(_A)
_AdicomUpsBattery_ObjectIdentity=ObjectIdentity
adicomUpsBattery=_AdicomUpsBattery_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,1,2))
class _AdicomUpsBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('batteryNormal',2),('batteryLow',3),('batteryDepleted',4),('batteryDischarging',5),('batteryFailure',6)))
_AdicomUpsBatteryStatus_Type.__name__=_E
_AdicomUpsBatteryStatus_Object=MibScalar
adicomUpsBatteryStatus=_AdicomUpsBatteryStatus_Object((1,3,6,1,4,1,4555,1,1,5,1,2,1),_AdicomUpsBatteryStatus_Type())
adicomUpsBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsBatteryStatus.setStatus(_A)
_AdicomUpsSecondsOnBattery_Type=Integer32
_AdicomUpsSecondsOnBattery_Object=MibScalar
adicomUpsSecondsOnBattery=_AdicomUpsSecondsOnBattery_Object((1,3,6,1,4,1,4555,1,1,5,1,2,2),_AdicomUpsSecondsOnBattery_Type())
adicomUpsSecondsOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsSecondsOnBattery.setStatus(_A)
_AdicomUpsEstimatedMinutesRemaining_Type=Integer32
_AdicomUpsEstimatedMinutesRemaining_Object=MibScalar
adicomUpsEstimatedMinutesRemaining=_AdicomUpsEstimatedMinutesRemaining_Object((1,3,6,1,4,1,4555,1,1,5,1,2,3),_AdicomUpsEstimatedMinutesRemaining_Type())
adicomUpsEstimatedMinutesRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsEstimatedMinutesRemaining.setStatus(_A)
_AdicomUpsEstimatedChargeRemaining_Type=Integer32
_AdicomUpsEstimatedChargeRemaining_Object=MibScalar
adicomUpsEstimatedChargeRemaining=_AdicomUpsEstimatedChargeRemaining_Object((1,3,6,1,4,1,4555,1,1,5,1,2,4),_AdicomUpsEstimatedChargeRemaining_Type())
adicomUpsEstimatedChargeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsEstimatedChargeRemaining.setStatus(_A)
_AdicomUpsBatteryVoltage_Type=Integer32
_AdicomUpsBatteryVoltage_Object=MibScalar
adicomUpsBatteryVoltage=_AdicomUpsBatteryVoltage_Object((1,3,6,1,4,1,4555,1,1,5,1,2,5),_AdicomUpsBatteryVoltage_Type())
adicomUpsBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsBatteryVoltage.setStatus(_A)
_AdicomUpsBatteryTemperature_Type=Integer32
_AdicomUpsBatteryTemperature_Object=MibScalar
adicomUpsBatteryTemperature=_AdicomUpsBatteryTemperature_Object((1,3,6,1,4,1,4555,1,1,5,1,2,6),_AdicomUpsBatteryTemperature_Type())
adicomUpsBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsBatteryTemperature.setStatus(_A)
_AdicomUpsInput_ObjectIdentity=ObjectIdentity
adicomUpsInput=_AdicomUpsInput_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,1,3))
_AdicomUpsInputFrequency_Type=Integer32
_AdicomUpsInputFrequency_Object=MibScalar
adicomUpsInputFrequency=_AdicomUpsInputFrequency_Object((1,3,6,1,4,1,4555,1,1,5,1,3,1),_AdicomUpsInputFrequency_Type())
adicomUpsInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsInputFrequency.setStatus(_A)
_AdicomUpsInputNumLines_Type=Integer32
_AdicomUpsInputNumLines_Object=MibScalar
adicomUpsInputNumLines=_AdicomUpsInputNumLines_Object((1,3,6,1,4,1,4555,1,1,5,1,3,2),_AdicomUpsInputNumLines_Type())
adicomUpsInputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsInputNumLines.setStatus(_A)
_AdicomUpsInputTable_Object=MibTable
adicomUpsInputTable=_AdicomUpsInputTable_Object((1,3,6,1,4,1,4555,1,1,5,1,3,3))
if mibBuilder.loadTexts:adicomUpsInputTable.setStatus(_A)
_AdicomUpsInputEntry_Object=MibTableRow
adicomUpsInputEntry=_AdicomUpsInputEntry_Object((1,3,6,1,4,1,4555,1,1,5,1,3,3,1))
adicomUpsInputEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:adicomUpsInputEntry.setStatus(_A)
class _AdicomUpsInputLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdicomUpsInputLineIndex_Type.__name__=_E
_AdicomUpsInputLineIndex_Object=MibTableColumn
adicomUpsInputLineIndex=_AdicomUpsInputLineIndex_Object((1,3,6,1,4,1,4555,1,1,5,1,3,3,1,1),_AdicomUpsInputLineIndex_Type())
adicomUpsInputLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsInputLineIndex.setStatus(_A)
_AdicomUpsInputVoltage_Type=Integer32
_AdicomUpsInputVoltage_Object=MibTableColumn
adicomUpsInputVoltage=_AdicomUpsInputVoltage_Object((1,3,6,1,4,1,4555,1,1,5,1,3,3,1,2),_AdicomUpsInputVoltage_Type())
adicomUpsInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsInputVoltage.setStatus(_A)
_AdicomUpsOutput_ObjectIdentity=ObjectIdentity
adicomUpsOutput=_AdicomUpsOutput_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,1,4))
class _AdicomUpsOutputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',2),('normal',3),('bypass',4),('battery',5),('booster',6),('reducer',7),('standby',8),('eco-mode',9),('e-saver',10)))
_AdicomUpsOutputSource_Type.__name__=_E
_AdicomUpsOutputSource_Object=MibScalar
adicomUpsOutputSource=_AdicomUpsOutputSource_Object((1,3,6,1,4,1,4555,1,1,5,1,4,1),_AdicomUpsOutputSource_Type())
adicomUpsOutputSource.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsOutputSource.setStatus(_A)
_AdicomUpsOutputFrequency_Type=Integer32
_AdicomUpsOutputFrequency_Object=MibScalar
adicomUpsOutputFrequency=_AdicomUpsOutputFrequency_Object((1,3,6,1,4,1,4555,1,1,5,1,4,2),_AdicomUpsOutputFrequency_Type())
adicomUpsOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsOutputFrequency.setStatus(_A)
_AdicomUpsOutputLoadRate_Type=Integer32
_AdicomUpsOutputLoadRate_Object=MibScalar
adicomUpsOutputLoadRate=_AdicomUpsOutputLoadRate_Object((1,3,6,1,4,1,4555,1,1,5,1,4,3),_AdicomUpsOutputLoadRate_Type())
adicomUpsOutputLoadRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsOutputLoadRate.setStatus(_A)
_AdicomUpsOutputkVA_Type=Integer32
_AdicomUpsOutputkVA_Object=MibScalar
adicomUpsOutputkVA=_AdicomUpsOutputkVA_Object((1,3,6,1,4,1,4555,1,1,5,1,4,4),_AdicomUpsOutputkVA_Type())
adicomUpsOutputkVA.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsOutputkVA.setStatus(_A)
_AdicomUpsOutputNumLines_Type=Integer32
_AdicomUpsOutputNumLines_Object=MibScalar
adicomUpsOutputNumLines=_AdicomUpsOutputNumLines_Object((1,3,6,1,4,1,4555,1,1,5,1,4,5),_AdicomUpsOutputNumLines_Type())
adicomUpsOutputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsOutputNumLines.setStatus(_A)
_AdicomUpsOutputTable_Object=MibTable
adicomUpsOutputTable=_AdicomUpsOutputTable_Object((1,3,6,1,4,1,4555,1,1,5,1,4,6))
if mibBuilder.loadTexts:adicomUpsOutputTable.setStatus(_A)
_AdicomUpsOutputEntry_Object=MibTableRow
adicomUpsOutputEntry=_AdicomUpsOutputEntry_Object((1,3,6,1,4,1,4555,1,1,5,1,4,6,1))
adicomUpsOutputEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:adicomUpsOutputEntry.setStatus(_A)
class _AdicomUpsOutputLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdicomUpsOutputLineIndex_Type.__name__=_E
_AdicomUpsOutputLineIndex_Object=MibTableColumn
adicomUpsOutputLineIndex=_AdicomUpsOutputLineIndex_Object((1,3,6,1,4,1,4555,1,1,5,1,4,6,1,1),_AdicomUpsOutputLineIndex_Type())
adicomUpsOutputLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsOutputLineIndex.setStatus(_A)
_AdicomUpsOutputVoltage_Type=Integer32
_AdicomUpsOutputVoltage_Object=MibTableColumn
adicomUpsOutputVoltage=_AdicomUpsOutputVoltage_Object((1,3,6,1,4,1,4555,1,1,5,1,4,6,1,2),_AdicomUpsOutputVoltage_Type())
adicomUpsOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsOutputVoltage.setStatus(_A)
_AdicomUpsOutputCurrent_Type=Integer32
_AdicomUpsOutputCurrent_Object=MibTableColumn
adicomUpsOutputCurrent=_AdicomUpsOutputCurrent_Object((1,3,6,1,4,1,4555,1,1,5,1,4,6,1,3),_AdicomUpsOutputCurrent_Type())
adicomUpsOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsOutputCurrent.setStatus(_A)
_AdicomUpsBypass_ObjectIdentity=ObjectIdentity
adicomUpsBypass=_AdicomUpsBypass_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,1,5))
_AdicomUpsBypassFrequency_Type=Integer32
_AdicomUpsBypassFrequency_Object=MibScalar
adicomUpsBypassFrequency=_AdicomUpsBypassFrequency_Object((1,3,6,1,4,1,4555,1,1,5,1,5,1),_AdicomUpsBypassFrequency_Type())
adicomUpsBypassFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsBypassFrequency.setStatus(_A)
_AdicomUpsBypassNumLines_Type=Integer32
_AdicomUpsBypassNumLines_Object=MibScalar
adicomUpsBypassNumLines=_AdicomUpsBypassNumLines_Object((1,3,6,1,4,1,4555,1,1,5,1,5,2),_AdicomUpsBypassNumLines_Type())
adicomUpsBypassNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsBypassNumLines.setStatus(_A)
_AdicomUpsBypassTable_Object=MibTable
adicomUpsBypassTable=_AdicomUpsBypassTable_Object((1,3,6,1,4,1,4555,1,1,5,1,5,3))
if mibBuilder.loadTexts:adicomUpsBypassTable.setStatus(_A)
_AdicomUpsBypassEntry_Object=MibTableRow
adicomUpsBypassEntry=_AdicomUpsBypassEntry_Object((1,3,6,1,4,1,4555,1,1,5,1,5,3,1))
adicomUpsBypassEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:adicomUpsBypassEntry.setStatus(_A)
class _AdicomUpsBypassLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdicomUpsBypassLineIndex_Type.__name__=_E
_AdicomUpsBypassLineIndex_Object=MibTableColumn
adicomUpsBypassLineIndex=_AdicomUpsBypassLineIndex_Object((1,3,6,1,4,1,4555,1,1,5,1,5,3,1,1),_AdicomUpsBypassLineIndex_Type())
adicomUpsBypassLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsBypassLineIndex.setStatus(_A)
_AdicomUpsBypassVoltage_Type=Integer32
_AdicomUpsBypassVoltage_Object=MibTableColumn
adicomUpsBypassVoltage=_AdicomUpsBypassVoltage_Object((1,3,6,1,4,1,4555,1,1,5,1,5,3,1,2),_AdicomUpsBypassVoltage_Type())
adicomUpsBypassVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsBypassVoltage.setStatus(_A)
_AdicomUpsAlarm_ObjectIdentity=ObjectIdentity
adicomUpsAlarm=_AdicomUpsAlarm_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,1,6))
_AdicomUpsWellKnownAlarms_ObjectIdentity=ObjectIdentity
adicomUpsWellKnownAlarms=_AdicomUpsWellKnownAlarms_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,1,6,1))
_AdicomUpsImminentStop_Type=Integer32
_AdicomUpsImminentStop_Object=MibScalar
adicomUpsImminentStop=_AdicomUpsImminentStop_Object((1,3,6,1,4,1,4555,1,1,5,1,6,1,1),_AdicomUpsImminentStop_Type())
adicomUpsImminentStop.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsImminentStop.setStatus(_A)
_AdicomUpsOverload_Type=Integer32
_AdicomUpsOverload_Object=MibScalar
adicomUpsOverload=_AdicomUpsOverload_Object((1,3,6,1,4,1,4555,1,1,5,1,6,1,2),_AdicomUpsOverload_Type())
adicomUpsOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsOverload.setStatus(_A)
_AdicomUpsTransferImpossible_Type=Integer32
_AdicomUpsTransferImpossible_Object=MibScalar
adicomUpsTransferImpossible=_AdicomUpsTransferImpossible_Object((1,3,6,1,4,1,4555,1,1,5,1,6,1,3),_AdicomUpsTransferImpossible_Type())
adicomUpsTransferImpossible.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsTransferImpossible.setStatus(_A)
_AdicomUpsInsufficientResource_Type=Integer32
_AdicomUpsInsufficientResource_Object=MibScalar
adicomUpsInsufficientResource=_AdicomUpsInsufficientResource_Object((1,3,6,1,4,1,4555,1,1,5,1,6,1,4),_AdicomUpsInsufficientResource_Type())
adicomUpsInsufficientResource.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsInsufficientResource.setStatus(_A)
_AdicomUpsRedundancyLoss_Type=Integer32
_AdicomUpsRedundancyLoss_Object=MibScalar
adicomUpsRedundancyLoss=_AdicomUpsRedundancyLoss_Object((1,3,6,1,4,1,4555,1,1,5,1,6,1,5),_AdicomUpsRedundancyLoss_Type())
adicomUpsRedundancyLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsRedundancyLoss.setStatus(_A)
_AdicomUpsTemperatureAlarm_Type=Integer32
_AdicomUpsTemperatureAlarm_Object=MibScalar
adicomUpsTemperatureAlarm=_AdicomUpsTemperatureAlarm_Object((1,3,6,1,4,1,4555,1,1,5,1,6,1,6),_AdicomUpsTemperatureAlarm_Type())
adicomUpsTemperatureAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsTemperatureAlarm.setStatus(_A)
_AdicomUpsGeneralAlarm_Type=Integer32
_AdicomUpsGeneralAlarm_Object=MibScalar
adicomUpsGeneralAlarm=_AdicomUpsGeneralAlarm_Object((1,3,6,1,4,1,4555,1,1,5,1,6,1,7),_AdicomUpsGeneralAlarm_Type())
adicomUpsGeneralAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsGeneralAlarm.setStatus(_A)
_AdicomUpsAgent_ObjectIdentity=ObjectIdentity
adicomUpsAgent=_AdicomUpsAgent_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,1,7))
_AdicomUpsAgentTrapString_Type=DisplayString
_AdicomUpsAgentTrapString_Object=MibScalar
adicomUpsAgentTrapString=_AdicomUpsAgentTrapString_Object((1,3,6,1,4,1,4555,1,1,5,1,7,1),_AdicomUpsAgentTrapString_Type())
adicomUpsAgentTrapString.setMaxAccess(_B)
if mibBuilder.loadTexts:adicomUpsAgentTrapString.setStatus(_A)
_AdicomUpsTraps_ObjectIdentity=ObjectIdentity
adicomUpsTraps=_AdicomUpsTraps_ObjectIdentity((1,3,6,1,4,1,4555,1,1,5,2))
adicomUpsTrapLoadOnInverter=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,1))
adicomUpsTrapLoadOnInverter.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapLoadOnInverter.setStatus('')
adicomUpsTrapOnBatteryPower=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,2))
adicomUpsTrapOnBatteryPower.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapOnBatteryPower.setStatus('')
adicomUpsTrapBatteryLow=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,3))
adicomUpsTrapBatteryLow.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapBatteryLow.setStatus('')
adicomUpsTrapPowerRestored=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,4))
adicomUpsTrapPowerRestored.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapPowerRestored.setStatus('')
adicomUpsTrapImminentStop=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,5))
adicomUpsTrapImminentStop.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapImminentStop.setStatus('')
adicomUpsTrapOverload=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,6))
adicomUpsTrapOverload.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapOverload.setStatus('')
adicomUpsTrapOutputLoadOFF=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,7))
adicomUpsTrapOutputLoadOFF.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapOutputLoadOFF.setStatus('')
adicomUpsTrapOutputOnBypass=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,8))
adicomUpsTrapOutputOnBypass.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapOutputOnBypass.setStatus('')
adicomUpsTrapGeneralAlarm=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,9))
adicomUpsTrapGeneralAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapGeneralAlarm.setStatus('')
adicomUpsTrapAlarmCancelled=NotificationType((1,3,6,1,4,1,4555,1,1,5,2,0,10))
adicomUpsTrapAlarmCancelled.setObjects((_C,_D))
if mibBuilder.loadTexts:adicomUpsTrapAlarmCancelled.setStatus('')
mibBuilder.exportSymbols(_C,**{'PositiveInteger':PositiveInteger,'NonNegativeInteger':NonNegativeInteger,'socomecUPS':socomecUPS,'software':software,'network':network,'adicomUps':adicomUps,'adicomUpsObjects':adicomUpsObjects,'adicomUpsIdent':adicomUpsIdent,'adicomUpsIdentModel':adicomUpsIdentModel,'adicomUpsIdentSerialNumber':adicomUpsIdentSerialNumber,'adicomUpsIdentFirmwareVersion':adicomUpsIdentFirmwareVersion,'adicomUpsIdentAgentSoftwareVersion':adicomUpsIdentAgentSoftwareVersion,'adicomUpsBattery':adicomUpsBattery,'adicomUpsBatteryStatus':adicomUpsBatteryStatus,'adicomUpsSecondsOnBattery':adicomUpsSecondsOnBattery,'adicomUpsEstimatedMinutesRemaining':adicomUpsEstimatedMinutesRemaining,'adicomUpsEstimatedChargeRemaining':adicomUpsEstimatedChargeRemaining,'adicomUpsBatteryVoltage':adicomUpsBatteryVoltage,'adicomUpsBatteryTemperature':adicomUpsBatteryTemperature,'adicomUpsInput':adicomUpsInput,'adicomUpsInputFrequency':adicomUpsInputFrequency,'adicomUpsInputNumLines':adicomUpsInputNumLines,'adicomUpsInputTable':adicomUpsInputTable,'adicomUpsInputEntry':adicomUpsInputEntry,_H:adicomUpsInputLineIndex,'adicomUpsInputVoltage':adicomUpsInputVoltage,'adicomUpsOutput':adicomUpsOutput,'adicomUpsOutputSource':adicomUpsOutputSource,'adicomUpsOutputFrequency':adicomUpsOutputFrequency,'adicomUpsOutputLoadRate':adicomUpsOutputLoadRate,'adicomUpsOutputkVA':adicomUpsOutputkVA,'adicomUpsOutputNumLines':adicomUpsOutputNumLines,'adicomUpsOutputTable':adicomUpsOutputTable,'adicomUpsOutputEntry':adicomUpsOutputEntry,_I:adicomUpsOutputLineIndex,'adicomUpsOutputVoltage':adicomUpsOutputVoltage,'adicomUpsOutputCurrent':adicomUpsOutputCurrent,'adicomUpsBypass':adicomUpsBypass,'adicomUpsBypassFrequency':adicomUpsBypassFrequency,'adicomUpsBypassNumLines':adicomUpsBypassNumLines,'adicomUpsBypassTable':adicomUpsBypassTable,'adicomUpsBypassEntry':adicomUpsBypassEntry,_J:adicomUpsBypassLineIndex,'adicomUpsBypassVoltage':adicomUpsBypassVoltage,'adicomUpsAlarm':adicomUpsAlarm,'adicomUpsWellKnownAlarms':adicomUpsWellKnownAlarms,'adicomUpsImminentStop':adicomUpsImminentStop,'adicomUpsOverload':adicomUpsOverload,'adicomUpsTransferImpossible':adicomUpsTransferImpossible,'adicomUpsInsufficientResource':adicomUpsInsufficientResource,'adicomUpsRedundancyLoss':adicomUpsRedundancyLoss,'adicomUpsTemperatureAlarm':adicomUpsTemperatureAlarm,'adicomUpsGeneralAlarm':adicomUpsGeneralAlarm,'adicomUpsAgent':adicomUpsAgent,_D:adicomUpsAgentTrapString,'adicomUpsTraps':adicomUpsTraps,'adicomUpsTrapLoadOnInverter':adicomUpsTrapLoadOnInverter,'adicomUpsTrapOnBatteryPower':adicomUpsTrapOnBatteryPower,'adicomUpsTrapBatteryLow':adicomUpsTrapBatteryLow,'adicomUpsTrapPowerRestored':adicomUpsTrapPowerRestored,'adicomUpsTrapImminentStop':adicomUpsTrapImminentStop,'adicomUpsTrapOverload':adicomUpsTrapOverload,'adicomUpsTrapOutputLoadOFF':adicomUpsTrapOutputLoadOFF,'adicomUpsTrapOutputOnBypass':adicomUpsTrapOutputOnBypass,'adicomUpsTrapGeneralAlarm':adicomUpsTrapGeneralAlarm,'adicomUpsTrapAlarmCancelled':adicomUpsTrapAlarmCancelled})