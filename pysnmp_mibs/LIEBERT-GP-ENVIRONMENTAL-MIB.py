_l='lgpEnvRemoteSensorIndex'
_k='lgpEnvSleepDayIndex'
_j='minute'
_i='lgpEnvSleepTimeIndex'
_h='return'
_g='remote'
_f='supply'
_e='lgpEnvOperationTimeIndex'
_d='lgpEnvValveIndex'
_c='not-specified'
_b='lgpEnvComponentStateIndex'
_a='manual'
_Z='lgpEnvHumidityIdRel'
_Y='lgpEnvTemperatureIdDegC'
_X='lgpEnvTemperatureIdDegF'
_W='auto'
_V='.1 percent Relative Humidity'
_U='notLockedOut'
_T='lockedOut'
_S='not-accessible'
_R='enabled'
_Q='.1 degrees Celsius'
_P='.1 degrees Fahrenheit'
_O='seconds'
_N='minutes'
_M='disabled'
_L='LIEBERT-GP-ENVIRONMENTAL-MIB'
_K='percent'
_J='percent Relative Humidity'
_I='degrees Celsius'
_H='degrees Fahrenheit'
_G='off'
_F='on'
_E='hours'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lgpEnvironmental,liebertEnvironmentalModuleReg=mibBuilder.importSymbols('LIEBERT-GP-REGISTRATION-MIB','lgpEnvironmental','liebertEnvironmentalModuleReg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
liebertGlobalProductsEnvironmentalModule=ModuleIdentity((1,3,6,1,4,1,476,1,42,1,5,1))
if mibBuilder.loadTexts:liebertGlobalProductsEnvironmentalModule.setRevisions(('2008-11-17 00:00','2008-07-02 00:00','2008-01-10 00:00','2007-05-29 00:00','2006-08-15 00:00','2006-02-22 00:00'))
_LgpEnvTemperature_ObjectIdentity=ObjectIdentity
lgpEnvTemperature=_LgpEnvTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1))
if mibBuilder.loadTexts:lgpEnvTemperature.setStatus(_A)
_LgpEnvTemperatureWellKnown_ObjectIdentity=ObjectIdentity
lgpEnvTemperatureWellKnown=_LgpEnvTemperatureWellKnown_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1))
if mibBuilder.loadTexts:lgpEnvTemperatureWellKnown.setStatus(_A)
_LgpEnvControlTemperature_ObjectIdentity=ObjectIdentity
lgpEnvControlTemperature=_LgpEnvControlTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,1))
if mibBuilder.loadTexts:lgpEnvControlTemperature.setStatus(_A)
_LgpEnvReturnAirTemperature_ObjectIdentity=ObjectIdentity
lgpEnvReturnAirTemperature=_LgpEnvReturnAirTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,2))
if mibBuilder.loadTexts:lgpEnvReturnAirTemperature.setStatus(_A)
_LgpEnvSupplyAirTemperature_ObjectIdentity=ObjectIdentity
lgpEnvSupplyAirTemperature=_LgpEnvSupplyAirTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,3))
if mibBuilder.loadTexts:lgpEnvSupplyAirTemperature.setStatus(_A)
_LgpAmbientTemperature_ObjectIdentity=ObjectIdentity
lgpAmbientTemperature=_LgpAmbientTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,4))
if mibBuilder.loadTexts:lgpAmbientTemperature.setStatus(_A)
_LgpInverterTemperature_ObjectIdentity=ObjectIdentity
lgpInverterTemperature=_LgpInverterTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,5))
if mibBuilder.loadTexts:lgpInverterTemperature.setStatus(_A)
_LgpBatteryTempterature_ObjectIdentity=ObjectIdentity
lgpBatteryTempterature=_LgpBatteryTempterature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,6))
if mibBuilder.loadTexts:lgpBatteryTempterature.setStatus(_A)
_LgpAcDcConverterTemperature_ObjectIdentity=ObjectIdentity
lgpAcDcConverterTemperature=_LgpAcDcConverterTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,7))
if mibBuilder.loadTexts:lgpAcDcConverterTemperature.setStatus(_A)
_LgpPfcTemperature_ObjectIdentity=ObjectIdentity
lgpPfcTemperature=_LgpPfcTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,8))
if mibBuilder.loadTexts:lgpPfcTemperature.setStatus(_A)
_LgpTransformerTemperature_ObjectIdentity=ObjectIdentity
lgpTransformerTemperature=_LgpTransformerTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,9))
if mibBuilder.loadTexts:lgpTransformerTemperature.setStatus(_A)
_LgpLocalTemperature_ObjectIdentity=ObjectIdentity
lgpLocalTemperature=_LgpLocalTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,10))
if mibBuilder.loadTexts:lgpLocalTemperature.setStatus(_A)
_LgpLocal1Temperature_ObjectIdentity=ObjectIdentity
lgpLocal1Temperature=_LgpLocal1Temperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,10,1))
if mibBuilder.loadTexts:lgpLocal1Temperature.setStatus(_A)
_LgpLocal2Temperature_ObjectIdentity=ObjectIdentity
lgpLocal2Temperature=_LgpLocal2Temperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,10,2))
if mibBuilder.loadTexts:lgpLocal2Temperature.setStatus(_A)
_LgpLocal3Temperature_ObjectIdentity=ObjectIdentity
lgpLocal3Temperature=_LgpLocal3Temperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,10,3))
if mibBuilder.loadTexts:lgpLocal3Temperature.setStatus(_A)
_LgpDigitalScrollCompressorTemperature_ObjectIdentity=ObjectIdentity
lgpDigitalScrollCompressorTemperature=_LgpDigitalScrollCompressorTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,11))
if mibBuilder.loadTexts:lgpDigitalScrollCompressorTemperature.setStatus(_A)
_LgpDigitalScrollCompressor1Temperature_ObjectIdentity=ObjectIdentity
lgpDigitalScrollCompressor1Temperature=_LgpDigitalScrollCompressor1Temperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,11,1))
if mibBuilder.loadTexts:lgpDigitalScrollCompressor1Temperature.setStatus(_A)
_LgpDigitalScrollCompressor2Temperature_ObjectIdentity=ObjectIdentity
lgpDigitalScrollCompressor2Temperature=_LgpDigitalScrollCompressor2Temperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,11,2))
if mibBuilder.loadTexts:lgpDigitalScrollCompressor2Temperature.setStatus(_A)
_LgpChillWaterTemperature_ObjectIdentity=ObjectIdentity
lgpChillWaterTemperature=_LgpChillWaterTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,12))
if mibBuilder.loadTexts:lgpChillWaterTemperature.setStatus(_A)
_LgpCoolantTemperature_ObjectIdentity=ObjectIdentity
lgpCoolantTemperature=_LgpCoolantTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,13))
if mibBuilder.loadTexts:lgpCoolantTemperature.setStatus(_A)
_LgpEnvEnclosureTemperatureSensors_ObjectIdentity=ObjectIdentity
lgpEnvEnclosureTemperatureSensors=_LgpEnvEnclosureTemperatureSensors_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,14))
if mibBuilder.loadTexts:lgpEnvEnclosureTemperatureSensors.setStatus(_A)
_LgpEnvEnclosureTemperatureSensor1_ObjectIdentity=ObjectIdentity
lgpEnvEnclosureTemperatureSensor1=_LgpEnvEnclosureTemperatureSensor1_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,14,1))
if mibBuilder.loadTexts:lgpEnvEnclosureTemperatureSensor1.setStatus(_A)
_LgpEnvEnclosureTemperatureSensor2_ObjectIdentity=ObjectIdentity
lgpEnvEnclosureTemperatureSensor2=_LgpEnvEnclosureTemperatureSensor2_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,14,2))
if mibBuilder.loadTexts:lgpEnvEnclosureTemperatureSensor2.setStatus(_A)
_LgpEnvEnclosureTemperatureSensor3_ObjectIdentity=ObjectIdentity
lgpEnvEnclosureTemperatureSensor3=_LgpEnvEnclosureTemperatureSensor3_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,14,3))
if mibBuilder.loadTexts:lgpEnvEnclosureTemperatureSensor3.setStatus(_A)
_LgpEnvEnclosureTemperatureSensor4_ObjectIdentity=ObjectIdentity
lgpEnvEnclosureTemperatureSensor4=_LgpEnvEnclosureTemperatureSensor4_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,14,4))
if mibBuilder.loadTexts:lgpEnvEnclosureTemperatureSensor4.setStatus(_A)
_LgpEnvValueAmbientRoomTemperature_ObjectIdentity=ObjectIdentity
lgpEnvValueAmbientRoomTemperature=_LgpEnvValueAmbientRoomTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,15))
if mibBuilder.loadTexts:lgpEnvValueAmbientRoomTemperature.setStatus(_A)
_LgpEnvDewPointTemperature_ObjectIdentity=ObjectIdentity
lgpEnvDewPointTemperature=_LgpEnvDewPointTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,16))
if mibBuilder.loadTexts:lgpEnvDewPointTemperature.setStatus(_A)
_LgpEnvEnclosureTemperature_ObjectIdentity=ObjectIdentity
lgpEnvEnclosureTemperature=_LgpEnvEnclosureTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,17))
if mibBuilder.loadTexts:lgpEnvEnclosureTemperature.setStatus(_A)
_LgpEnvAdjustedTemperature_ObjectIdentity=ObjectIdentity
lgpEnvAdjustedTemperature=_LgpEnvAdjustedTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,18))
if mibBuilder.loadTexts:lgpEnvAdjustedTemperature.setStatus(_A)
_LgpEnvExternalSensors_ObjectIdentity=ObjectIdentity
lgpEnvExternalSensors=_LgpEnvExternalSensors_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,19))
if mibBuilder.loadTexts:lgpEnvExternalSensors.setStatus(_A)
_LgpEnvExternalAirSensorA_ObjectIdentity=ObjectIdentity
lgpEnvExternalAirSensorA=_LgpEnvExternalAirSensorA_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,19,1))
if mibBuilder.loadTexts:lgpEnvExternalAirSensorA.setStatus(_A)
_LgpEnvExternalAirSensorADewPoint_ObjectIdentity=ObjectIdentity
lgpEnvExternalAirSensorADewPoint=_LgpEnvExternalAirSensorADewPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,19,2))
if mibBuilder.loadTexts:lgpEnvExternalAirSensorADewPoint.setStatus(_A)
_LgpEnvExternalAirSensorB_ObjectIdentity=ObjectIdentity
lgpEnvExternalAirSensorB=_LgpEnvExternalAirSensorB_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,19,3))
if mibBuilder.loadTexts:lgpEnvExternalAirSensorB.setStatus(_A)
_LgpEnvExternalAirSensorBDewPoint_ObjectIdentity=ObjectIdentity
lgpEnvExternalAirSensorBDewPoint=_LgpEnvExternalAirSensorBDewPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,19,4))
if mibBuilder.loadTexts:lgpEnvExternalAirSensorBDewPoint.setStatus(_A)
_LgpEnvSupplyFluidTemperature_ObjectIdentity=ObjectIdentity
lgpEnvSupplyFluidTemperature=_LgpEnvSupplyFluidTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,20))
if mibBuilder.loadTexts:lgpEnvSupplyFluidTemperature.setStatus(_A)
_LgpEnvSupplyRefrigerantTemperature_ObjectIdentity=ObjectIdentity
lgpEnvSupplyRefrigerantTemperature=_LgpEnvSupplyRefrigerantTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,21))
if mibBuilder.loadTexts:lgpEnvSupplyRefrigerantTemperature.setStatus(_A)
_LgpEnvMinDesiredRoomAirTemperature_ObjectIdentity=ObjectIdentity
lgpEnvMinDesiredRoomAirTemperature=_LgpEnvMinDesiredRoomAirTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,22))
if mibBuilder.loadTexts:lgpEnvMinDesiredRoomAirTemperature.setStatus(_A)
_LgpEnvDewPointTemperatures_ObjectIdentity=ObjectIdentity
lgpEnvDewPointTemperatures=_LgpEnvDewPointTemperatures_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,23))
if mibBuilder.loadTexts:lgpEnvDewPointTemperatures.setStatus(_A)
_LgpEnvInletDewPointTemperature_ObjectIdentity=ObjectIdentity
lgpEnvInletDewPointTemperature=_LgpEnvInletDewPointTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,23,1))
if mibBuilder.loadTexts:lgpEnvInletDewPointTemperature.setStatus(_A)
_LgpEnvReturnFluidTemperature_ObjectIdentity=ObjectIdentity
lgpEnvReturnFluidTemperature=_LgpEnvReturnFluidTemperature_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,1,24))
if mibBuilder.loadTexts:lgpEnvReturnFluidTemperature.setStatus(_A)
_LgpEnvTemperatureFahrenheit_ObjectIdentity=ObjectIdentity
lgpEnvTemperatureFahrenheit=_LgpEnvTemperatureFahrenheit_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,2))
if mibBuilder.loadTexts:lgpEnvTemperatureFahrenheit.setStatus(_A)
_LgpEnvTemperatureSettingDegF_Type=Integer32
_LgpEnvTemperatureSettingDegF_Object=MibScalar
lgpEnvTemperatureSettingDegF=_LgpEnvTemperatureSettingDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,1),_LgpEnvTemperatureSettingDegF_Type())
lgpEnvTemperatureSettingDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureSettingDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureSettingDegF.setUnits(_H)
_LgpEnvTemperatureToleranceDegF_Type=Integer32
_LgpEnvTemperatureToleranceDegF_Object=MibScalar
lgpEnvTemperatureToleranceDegF=_LgpEnvTemperatureToleranceDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,2),_LgpEnvTemperatureToleranceDegF_Type())
lgpEnvTemperatureToleranceDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureToleranceDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureToleranceDegF.setUnits('0.1 degrees Fahrenheit')
_LgpEnvTemperatureTableDegF_Object=MibTable
lgpEnvTemperatureTableDegF=_LgpEnvTemperatureTableDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3))
if mibBuilder.loadTexts:lgpEnvTemperatureTableDegF.setStatus(_A)
_LgpEnvTemperatureEntryDegF_Object=MibTableRow
lgpEnvTemperatureEntryDegF=_LgpEnvTemperatureEntryDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1))
lgpEnvTemperatureEntryDegF.setIndexNames((0,_L,_X))
if mibBuilder.loadTexts:lgpEnvTemperatureEntryDegF.setStatus(_A)
_LgpEnvTemperatureIdDegF_Type=Unsigned32
_LgpEnvTemperatureIdDegF_Object=MibTableColumn
lgpEnvTemperatureIdDegF=_LgpEnvTemperatureIdDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,1),_LgpEnvTemperatureIdDegF_Type())
lgpEnvTemperatureIdDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureIdDegF.setStatus(_A)
_LgpEnvTemperatureDescrDegF_Type=ObjectIdentifier
_LgpEnvTemperatureDescrDegF_Object=MibTableColumn
lgpEnvTemperatureDescrDegF=_LgpEnvTemperatureDescrDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,2),_LgpEnvTemperatureDescrDegF_Type())
lgpEnvTemperatureDescrDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureDescrDegF.setStatus(_A)
_LgpEnvTemperatureMeasurementDegF_Type=Integer32
_LgpEnvTemperatureMeasurementDegF_Object=MibTableColumn
lgpEnvTemperatureMeasurementDegF=_LgpEnvTemperatureMeasurementDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,3),_LgpEnvTemperatureMeasurementDegF_Type())
lgpEnvTemperatureMeasurementDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureMeasurementDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureMeasurementDegF.setUnits(_H)
_LgpEnvTemperatureHighThresholdDegF_Type=Integer32
_LgpEnvTemperatureHighThresholdDegF_Object=MibTableColumn
lgpEnvTemperatureHighThresholdDegF=_LgpEnvTemperatureHighThresholdDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,4),_LgpEnvTemperatureHighThresholdDegF_Type())
lgpEnvTemperatureHighThresholdDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureHighThresholdDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureHighThresholdDegF.setUnits(_H)
_LgpEnvTemperatureLowThresholdDegF_Type=Integer32
_LgpEnvTemperatureLowThresholdDegF_Object=MibTableColumn
lgpEnvTemperatureLowThresholdDegF=_LgpEnvTemperatureLowThresholdDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,5),_LgpEnvTemperatureLowThresholdDegF_Type())
lgpEnvTemperatureLowThresholdDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureLowThresholdDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureLowThresholdDegF.setUnits(_H)
_LgpEnvTemperatureSetPointDegF_Type=Integer32
_LgpEnvTemperatureSetPointDegF_Object=MibTableColumn
lgpEnvTemperatureSetPointDegF=_LgpEnvTemperatureSetPointDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,6),_LgpEnvTemperatureSetPointDegF_Type())
lgpEnvTemperatureSetPointDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureSetPointDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureSetPointDegF.setUnits(_H)
_LgpEnvTemperatureDailyHighDegF_Type=Integer32
_LgpEnvTemperatureDailyHighDegF_Object=MibTableColumn
lgpEnvTemperatureDailyHighDegF=_LgpEnvTemperatureDailyHighDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,7),_LgpEnvTemperatureDailyHighDegF_Type())
lgpEnvTemperatureDailyHighDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureDailyHighDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureDailyHighDegF.setUnits(_H)
_LgpEnvTemperatureDailyLowDegF_Type=Integer32
_LgpEnvTemperatureDailyLowDegF_Object=MibTableColumn
lgpEnvTemperatureDailyLowDegF=_LgpEnvTemperatureDailyLowDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,8),_LgpEnvTemperatureDailyLowDegF_Type())
lgpEnvTemperatureDailyLowDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureDailyLowDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureDailyLowDegF.setUnits(_H)
class _LgpEnvTempDailyHighTimeHourDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_LgpEnvTempDailyHighTimeHourDegF_Type.__name__=_D
_LgpEnvTempDailyHighTimeHourDegF_Object=MibTableColumn
lgpEnvTempDailyHighTimeHourDegF=_LgpEnvTempDailyHighTimeHourDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,9),_LgpEnvTempDailyHighTimeHourDegF_Type())
lgpEnvTempDailyHighTimeHourDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeHourDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeHourDegF.setUnits(_E)
class _LgpEnvTempDailyHighTimeMinuteDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvTempDailyHighTimeMinuteDegF_Type.__name__=_D
_LgpEnvTempDailyHighTimeMinuteDegF_Object=MibTableColumn
lgpEnvTempDailyHighTimeMinuteDegF=_LgpEnvTempDailyHighTimeMinuteDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,10),_LgpEnvTempDailyHighTimeMinuteDegF_Type())
lgpEnvTempDailyHighTimeMinuteDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeMinuteDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeMinuteDegF.setUnits(_N)
class _LgpEnvTempDailyHighTimeSecondDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvTempDailyHighTimeSecondDegF_Type.__name__=_D
_LgpEnvTempDailyHighTimeSecondDegF_Object=MibTableColumn
lgpEnvTempDailyHighTimeSecondDegF=_LgpEnvTempDailyHighTimeSecondDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,11),_LgpEnvTempDailyHighTimeSecondDegF_Type())
lgpEnvTempDailyHighTimeSecondDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeSecondDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeSecondDegF.setUnits(_O)
class _LgpEnvTempDailyLowTimeHourDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_LgpEnvTempDailyLowTimeHourDegF_Type.__name__=_D
_LgpEnvTempDailyLowTimeHourDegF_Object=MibTableColumn
lgpEnvTempDailyLowTimeHourDegF=_LgpEnvTempDailyLowTimeHourDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,12),_LgpEnvTempDailyLowTimeHourDegF_Type())
lgpEnvTempDailyLowTimeHourDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeHourDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeHourDegF.setUnits(_E)
class _LgpEnvTempDailyLowTimeMinuteDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvTempDailyLowTimeMinuteDegF_Type.__name__=_D
_LgpEnvTempDailyLowTimeMinuteDegF_Object=MibTableColumn
lgpEnvTempDailyLowTimeMinuteDegF=_LgpEnvTempDailyLowTimeMinuteDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,13),_LgpEnvTempDailyLowTimeMinuteDegF_Type())
lgpEnvTempDailyLowTimeMinuteDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeMinuteDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeMinuteDegF.setUnits(_N)
class _LgpEnvTempDailyLowTimeSecondDegF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvTempDailyLowTimeSecondDegF_Type.__name__=_D
_LgpEnvTempDailyLowTimeSecondDegF_Object=MibTableColumn
lgpEnvTempDailyLowTimeSecondDegF=_LgpEnvTempDailyLowTimeSecondDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,14),_LgpEnvTempDailyLowTimeSecondDegF_Type())
lgpEnvTempDailyLowTimeSecondDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeSecondDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeSecondDegF.setUnits(_O)
_LgpEnvTemperatureMeasurementTenthsDegF_Type=Integer32
_LgpEnvTemperatureMeasurementTenthsDegF_Object=MibTableColumn
lgpEnvTemperatureMeasurementTenthsDegF=_LgpEnvTemperatureMeasurementTenthsDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,50),_LgpEnvTemperatureMeasurementTenthsDegF_Type())
lgpEnvTemperatureMeasurementTenthsDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureMeasurementTenthsDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureMeasurementTenthsDegF.setUnits(_P)
_LgpEnvTemperatureHighThresholdTenthsDegF_Type=Integer32
_LgpEnvTemperatureHighThresholdTenthsDegF_Object=MibTableColumn
lgpEnvTemperatureHighThresholdTenthsDegF=_LgpEnvTemperatureHighThresholdTenthsDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,51),_LgpEnvTemperatureHighThresholdTenthsDegF_Type())
lgpEnvTemperatureHighThresholdTenthsDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureHighThresholdTenthsDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureHighThresholdTenthsDegF.setUnits(_P)
_LgpEnvTemperatureLowThresholdTenthsDegF_Type=Integer32
_LgpEnvTemperatureLowThresholdTenthsDegF_Object=MibTableColumn
lgpEnvTemperatureLowThresholdTenthsDegF=_LgpEnvTemperatureLowThresholdTenthsDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,52),_LgpEnvTemperatureLowThresholdTenthsDegF_Type())
lgpEnvTemperatureLowThresholdTenthsDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureLowThresholdTenthsDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureLowThresholdTenthsDegF.setUnits(_P)
_LgpEnvTemperatureSetPointTenthsDegF_Type=Integer32
_LgpEnvTemperatureSetPointTenthsDegF_Object=MibTableColumn
lgpEnvTemperatureSetPointTenthsDegF=_LgpEnvTemperatureSetPointTenthsDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,53),_LgpEnvTemperatureSetPointTenthsDegF_Type())
lgpEnvTemperatureSetPointTenthsDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureSetPointTenthsDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureSetPointTenthsDegF.setUnits(_P)
_LgpEnvTemperatureDeadBandTenthsDegF_Type=Integer32
_LgpEnvTemperatureDeadBandTenthsDegF_Object=MibTableColumn
lgpEnvTemperatureDeadBandTenthsDegF=_LgpEnvTemperatureDeadBandTenthsDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,60),_LgpEnvTemperatureDeadBandTenthsDegF_Type())
lgpEnvTemperatureDeadBandTenthsDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureDeadBandTenthsDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureDeadBandTenthsDegF.setUnits(_P)
_LgpEnvTempHeatingPropBandTenthsDegF_Type=Integer32
_LgpEnvTempHeatingPropBandTenthsDegF_Object=MibTableColumn
lgpEnvTempHeatingPropBandTenthsDegF=_LgpEnvTempHeatingPropBandTenthsDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,61),_LgpEnvTempHeatingPropBandTenthsDegF_Type())
lgpEnvTempHeatingPropBandTenthsDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTempHeatingPropBandTenthsDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempHeatingPropBandTenthsDegF.setUnits(_P)
_LgpEnvTempCoolingPropBandTenthsDegF_Type=Integer32
_LgpEnvTempCoolingPropBandTenthsDegF_Object=MibTableColumn
lgpEnvTempCoolingPropBandTenthsDegF=_LgpEnvTempCoolingPropBandTenthsDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,3,1,62),_LgpEnvTempCoolingPropBandTenthsDegF_Type())
lgpEnvTempCoolingPropBandTenthsDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTempCoolingPropBandTenthsDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempCoolingPropBandTenthsDegF.setUnits(_P)
_LgpEnvTemperatureDeadbandRangeDegF_Type=Integer32
_LgpEnvTemperatureDeadbandRangeDegF_Object=MibScalar
lgpEnvTemperatureDeadbandRangeDegF=_LgpEnvTemperatureDeadbandRangeDegF_Object((1,3,6,1,4,1,476,1,42,3,4,1,2,4),_LgpEnvTemperatureDeadbandRangeDegF_Type())
lgpEnvTemperatureDeadbandRangeDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureDeadbandRangeDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureDeadbandRangeDegF.setUnits(_P)
_LgpEnvTemperatureCelsius_ObjectIdentity=ObjectIdentity
lgpEnvTemperatureCelsius=_LgpEnvTemperatureCelsius_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,1,3))
if mibBuilder.loadTexts:lgpEnvTemperatureCelsius.setStatus(_A)
_LgpEnvTemperatureSettingDegC_Type=Integer32
_LgpEnvTemperatureSettingDegC_Object=MibScalar
lgpEnvTemperatureSettingDegC=_LgpEnvTemperatureSettingDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,1),_LgpEnvTemperatureSettingDegC_Type())
lgpEnvTemperatureSettingDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureSettingDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureSettingDegC.setUnits(_I)
_LgpEnvTemperatureToleranceDegC_Type=Integer32
_LgpEnvTemperatureToleranceDegC_Object=MibScalar
lgpEnvTemperatureToleranceDegC=_LgpEnvTemperatureToleranceDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,2),_LgpEnvTemperatureToleranceDegC_Type())
lgpEnvTemperatureToleranceDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureToleranceDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureToleranceDegC.setUnits('0.1 degrees Celsius')
_LgpEnvTemperatureTableDegC_Object=MibTable
lgpEnvTemperatureTableDegC=_LgpEnvTemperatureTableDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3))
if mibBuilder.loadTexts:lgpEnvTemperatureTableDegC.setStatus(_A)
_LgpEnvTemperatureEntryDegC_Object=MibTableRow
lgpEnvTemperatureEntryDegC=_LgpEnvTemperatureEntryDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1))
lgpEnvTemperatureEntryDegC.setIndexNames((0,_L,_Y))
if mibBuilder.loadTexts:lgpEnvTemperatureEntryDegC.setStatus(_A)
_LgpEnvTemperatureIdDegC_Type=Unsigned32
_LgpEnvTemperatureIdDegC_Object=MibTableColumn
lgpEnvTemperatureIdDegC=_LgpEnvTemperatureIdDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,1),_LgpEnvTemperatureIdDegC_Type())
lgpEnvTemperatureIdDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureIdDegC.setStatus(_A)
_LgpEnvTemperatureDescrDegC_Type=ObjectIdentifier
_LgpEnvTemperatureDescrDegC_Object=MibTableColumn
lgpEnvTemperatureDescrDegC=_LgpEnvTemperatureDescrDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,2),_LgpEnvTemperatureDescrDegC_Type())
lgpEnvTemperatureDescrDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureDescrDegC.setStatus(_A)
_LgpEnvTemperatureMeasurementDegC_Type=Integer32
_LgpEnvTemperatureMeasurementDegC_Object=MibTableColumn
lgpEnvTemperatureMeasurementDegC=_LgpEnvTemperatureMeasurementDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,3),_LgpEnvTemperatureMeasurementDegC_Type())
lgpEnvTemperatureMeasurementDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureMeasurementDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureMeasurementDegC.setUnits(_I)
_LgpEnvTemperatureHighThresholdDegC_Type=Integer32
_LgpEnvTemperatureHighThresholdDegC_Object=MibTableColumn
lgpEnvTemperatureHighThresholdDegC=_LgpEnvTemperatureHighThresholdDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,4),_LgpEnvTemperatureHighThresholdDegC_Type())
lgpEnvTemperatureHighThresholdDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureHighThresholdDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureHighThresholdDegC.setUnits(_I)
_LgpEnvTemperatureLowThresholdDegC_Type=Integer32
_LgpEnvTemperatureLowThresholdDegC_Object=MibTableColumn
lgpEnvTemperatureLowThresholdDegC=_LgpEnvTemperatureLowThresholdDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,5),_LgpEnvTemperatureLowThresholdDegC_Type())
lgpEnvTemperatureLowThresholdDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureLowThresholdDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureLowThresholdDegC.setUnits(_I)
_LgpEnvTemperatureSetPointDegC_Type=Integer32
_LgpEnvTemperatureSetPointDegC_Object=MibTableColumn
lgpEnvTemperatureSetPointDegC=_LgpEnvTemperatureSetPointDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,6),_LgpEnvTemperatureSetPointDegC_Type())
lgpEnvTemperatureSetPointDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureSetPointDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureSetPointDegC.setUnits(_I)
_LgpEnvTemperatureDailyHighDegC_Type=Integer32
_LgpEnvTemperatureDailyHighDegC_Object=MibTableColumn
lgpEnvTemperatureDailyHighDegC=_LgpEnvTemperatureDailyHighDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,7),_LgpEnvTemperatureDailyHighDegC_Type())
lgpEnvTemperatureDailyHighDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureDailyHighDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureDailyHighDegC.setUnits(_I)
_LgpEnvTemperatureDailyLowDegC_Type=Integer32
_LgpEnvTemperatureDailyLowDegC_Object=MibTableColumn
lgpEnvTemperatureDailyLowDegC=_LgpEnvTemperatureDailyLowDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,8),_LgpEnvTemperatureDailyLowDegC_Type())
lgpEnvTemperatureDailyLowDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureDailyLowDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureDailyLowDegC.setUnits(_I)
class _LgpEnvTempDailyHighTimeHourDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_LgpEnvTempDailyHighTimeHourDegC_Type.__name__=_D
_LgpEnvTempDailyHighTimeHourDegC_Object=MibTableColumn
lgpEnvTempDailyHighTimeHourDegC=_LgpEnvTempDailyHighTimeHourDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,9),_LgpEnvTempDailyHighTimeHourDegC_Type())
lgpEnvTempDailyHighTimeHourDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeHourDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeHourDegC.setUnits(_E)
class _LgpEnvTempDailyHighTimeMinuteDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvTempDailyHighTimeMinuteDegC_Type.__name__=_D
_LgpEnvTempDailyHighTimeMinuteDegC_Object=MibTableColumn
lgpEnvTempDailyHighTimeMinuteDegC=_LgpEnvTempDailyHighTimeMinuteDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,10),_LgpEnvTempDailyHighTimeMinuteDegC_Type())
lgpEnvTempDailyHighTimeMinuteDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeMinuteDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeMinuteDegC.setUnits(_N)
class _LgpEnvTempDailyHighTimeSecondDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvTempDailyHighTimeSecondDegC_Type.__name__=_D
_LgpEnvTempDailyHighTimeSecondDegC_Object=MibTableColumn
lgpEnvTempDailyHighTimeSecondDegC=_LgpEnvTempDailyHighTimeSecondDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,11),_LgpEnvTempDailyHighTimeSecondDegC_Type())
lgpEnvTempDailyHighTimeSecondDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeSecondDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyHighTimeSecondDegC.setUnits(_O)
class _LgpEnvTempDailyLowTimeHourDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_LgpEnvTempDailyLowTimeHourDegC_Type.__name__=_D
_LgpEnvTempDailyLowTimeHourDegC_Object=MibTableColumn
lgpEnvTempDailyLowTimeHourDegC=_LgpEnvTempDailyLowTimeHourDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,12),_LgpEnvTempDailyLowTimeHourDegC_Type())
lgpEnvTempDailyLowTimeHourDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeHourDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeHourDegC.setUnits(_E)
class _LgpEnvTempDailyLowTimeMinuteDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvTempDailyLowTimeMinuteDegC_Type.__name__=_D
_LgpEnvTempDailyLowTimeMinuteDegC_Object=MibTableColumn
lgpEnvTempDailyLowTimeMinuteDegC=_LgpEnvTempDailyLowTimeMinuteDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,13),_LgpEnvTempDailyLowTimeMinuteDegC_Type())
lgpEnvTempDailyLowTimeMinuteDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeMinuteDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeMinuteDegC.setUnits(_N)
class _LgpEnvTempDailyLowTimeSecondDegC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvTempDailyLowTimeSecondDegC_Type.__name__=_D
_LgpEnvTempDailyLowTimeSecondDegC_Object=MibTableColumn
lgpEnvTempDailyLowTimeSecondDegC=_LgpEnvTempDailyLowTimeSecondDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,14),_LgpEnvTempDailyLowTimeSecondDegC_Type())
lgpEnvTempDailyLowTimeSecondDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeSecondDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempDailyLowTimeSecondDegC.setUnits(_O)
_LgpEnvTemperatureMeasurementTenthsDegC_Type=Integer32
_LgpEnvTemperatureMeasurementTenthsDegC_Object=MibTableColumn
lgpEnvTemperatureMeasurementTenthsDegC=_LgpEnvTemperatureMeasurementTenthsDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,50),_LgpEnvTemperatureMeasurementTenthsDegC_Type())
lgpEnvTemperatureMeasurementTenthsDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureMeasurementTenthsDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureMeasurementTenthsDegC.setUnits(_Q)
_LgpEnvTemperatureHighThresholdTenthsDegC_Type=Integer32
_LgpEnvTemperatureHighThresholdTenthsDegC_Object=MibTableColumn
lgpEnvTemperatureHighThresholdTenthsDegC=_LgpEnvTemperatureHighThresholdTenthsDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,51),_LgpEnvTemperatureHighThresholdTenthsDegC_Type())
lgpEnvTemperatureHighThresholdTenthsDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureHighThresholdTenthsDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureHighThresholdTenthsDegC.setUnits(_Q)
_LgpEnvTemperatureLowThresholdTenthsDegC_Type=Integer32
_LgpEnvTemperatureLowThresholdTenthsDegC_Object=MibTableColumn
lgpEnvTemperatureLowThresholdTenthsDegC=_LgpEnvTemperatureLowThresholdTenthsDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,52),_LgpEnvTemperatureLowThresholdTenthsDegC_Type())
lgpEnvTemperatureLowThresholdTenthsDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureLowThresholdTenthsDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureLowThresholdTenthsDegC.setUnits(_Q)
_LgpEnvTemperatureSetPointTenthsDegC_Type=Integer32
_LgpEnvTemperatureSetPointTenthsDegC_Object=MibTableColumn
lgpEnvTemperatureSetPointTenthsDegC=_LgpEnvTemperatureSetPointTenthsDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,53),_LgpEnvTemperatureSetPointTenthsDegC_Type())
lgpEnvTemperatureSetPointTenthsDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureSetPointTenthsDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureSetPointTenthsDegC.setUnits(_Q)
_LgpEnvTemperatureDeadBandTenthsDegC_Type=Integer32
_LgpEnvTemperatureDeadBandTenthsDegC_Object=MibTableColumn
lgpEnvTemperatureDeadBandTenthsDegC=_LgpEnvTemperatureDeadBandTenthsDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,60),_LgpEnvTemperatureDeadBandTenthsDegC_Type())
lgpEnvTemperatureDeadBandTenthsDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureDeadBandTenthsDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureDeadBandTenthsDegC.setUnits(_Q)
_LgpEnvTempHeatingPropBandTenthsDegC_Type=Integer32
_LgpEnvTempHeatingPropBandTenthsDegC_Object=MibTableColumn
lgpEnvTempHeatingPropBandTenthsDegC=_LgpEnvTempHeatingPropBandTenthsDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,61),_LgpEnvTempHeatingPropBandTenthsDegC_Type())
lgpEnvTempHeatingPropBandTenthsDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTempHeatingPropBandTenthsDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempHeatingPropBandTenthsDegC.setUnits(_Q)
_LgpEnvTempCoolingPropBandTenthsDegC_Type=Integer32
_LgpEnvTempCoolingPropBandTenthsDegC_Object=MibTableColumn
lgpEnvTempCoolingPropBandTenthsDegC=_LgpEnvTempCoolingPropBandTenthsDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,3,1,62),_LgpEnvTempCoolingPropBandTenthsDegC_Type())
lgpEnvTempCoolingPropBandTenthsDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTempCoolingPropBandTenthsDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTempCoolingPropBandTenthsDegC.setUnits(_Q)
_LgpEnvTemperatureDeadbandRangeDegC_Type=Integer32
_LgpEnvTemperatureDeadbandRangeDegC_Object=MibScalar
lgpEnvTemperatureDeadbandRangeDegC=_LgpEnvTemperatureDeadbandRangeDegC_Object((1,3,6,1,4,1,476,1,42,3,4,1,3,4),_LgpEnvTemperatureDeadbandRangeDegC_Type())
lgpEnvTemperatureDeadbandRangeDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvTemperatureDeadbandRangeDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvTemperatureDeadbandRangeDegC.setUnits(_Q)
_LgpEnvTemperatureControlMode_Type=ObjectIdentifier
_LgpEnvTemperatureControlMode_Object=MibScalar
lgpEnvTemperatureControlMode=_LgpEnvTemperatureControlMode_Object((1,3,6,1,4,1,476,1,42,3,4,1,4),_LgpEnvTemperatureControlMode_Type())
lgpEnvTemperatureControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvTemperatureControlMode.setStatus(_A)
_LgpEnvHumidity_ObjectIdentity=ObjectIdentity
lgpEnvHumidity=_LgpEnvHumidity_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,2))
if mibBuilder.loadTexts:lgpEnvHumidity.setStatus(_A)
_LgpEnvHumidityWellKnown_ObjectIdentity=ObjectIdentity
lgpEnvHumidityWellKnown=_LgpEnvHumidityWellKnown_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,2,1))
if mibBuilder.loadTexts:lgpEnvHumidityWellKnown.setStatus(_A)
_LgpEnvControlHumidity_ObjectIdentity=ObjectIdentity
lgpEnvControlHumidity=_LgpEnvControlHumidity_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,2,1,1))
if mibBuilder.loadTexts:lgpEnvControlHumidity.setStatus(_A)
_LgpEnvReturnAirHumidity_ObjectIdentity=ObjectIdentity
lgpEnvReturnAirHumidity=_LgpEnvReturnAirHumidity_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,2,1,2))
if mibBuilder.loadTexts:lgpEnvReturnAirHumidity.setStatus(_A)
_LgpEnvSupplyAirHumidity_ObjectIdentity=ObjectIdentity
lgpEnvSupplyAirHumidity=_LgpEnvSupplyAirHumidity_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,2,1,3))
if mibBuilder.loadTexts:lgpEnvSupplyAirHumidity.setStatus(_A)
_LgpEnvValueAmbientHumidity_ObjectIdentity=ObjectIdentity
lgpEnvValueAmbientHumidity=_LgpEnvValueAmbientHumidity_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,2,1,4))
if mibBuilder.loadTexts:lgpEnvValueAmbientHumidity.setStatus(_A)
_LgpEnvHumidityRelative_ObjectIdentity=ObjectIdentity
lgpEnvHumidityRelative=_LgpEnvHumidityRelative_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,2,2))
if mibBuilder.loadTexts:lgpEnvHumidityRelative.setStatus(_A)
_LgpEnvHumiditySettingRel_Type=Integer32
_LgpEnvHumiditySettingRel_Object=MibScalar
lgpEnvHumiditySettingRel=_LgpEnvHumiditySettingRel_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,1),_LgpEnvHumiditySettingRel_Type())
lgpEnvHumiditySettingRel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumiditySettingRel.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumiditySettingRel.setUnits(_J)
_LgpEnvHumidityToleranceRel_Type=Integer32
_LgpEnvHumidityToleranceRel_Object=MibScalar
lgpEnvHumidityToleranceRel=_LgpEnvHumidityToleranceRel_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,2),_LgpEnvHumidityToleranceRel_Type())
lgpEnvHumidityToleranceRel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumidityToleranceRel.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityToleranceRel.setUnits(_J)
_LgpEnvHumidityTableRel_Object=MibTable
lgpEnvHumidityTableRel=_LgpEnvHumidityTableRel_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3))
if mibBuilder.loadTexts:lgpEnvHumidityTableRel.setStatus(_A)
_LgpEnvHumidityEntryRel_Object=MibTableRow
lgpEnvHumidityEntryRel=_LgpEnvHumidityEntryRel_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1))
lgpEnvHumidityEntryRel.setIndexNames((0,_L,_Z))
if mibBuilder.loadTexts:lgpEnvHumidityEntryRel.setStatus(_A)
_LgpEnvHumidityIdRel_Type=Unsigned32
_LgpEnvHumidityIdRel_Object=MibTableColumn
lgpEnvHumidityIdRel=_LgpEnvHumidityIdRel_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,1),_LgpEnvHumidityIdRel_Type())
lgpEnvHumidityIdRel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityIdRel.setStatus(_A)
_LgpEnvHumidityDescrRel_Type=ObjectIdentifier
_LgpEnvHumidityDescrRel_Object=MibTableColumn
lgpEnvHumidityDescrRel=_LgpEnvHumidityDescrRel_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,2),_LgpEnvHumidityDescrRel_Type())
lgpEnvHumidityDescrRel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityDescrRel.setStatus(_A)
_LgpEnvHumidityMeasurementRel_Type=Integer32
_LgpEnvHumidityMeasurementRel_Object=MibTableColumn
lgpEnvHumidityMeasurementRel=_LgpEnvHumidityMeasurementRel_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,3),_LgpEnvHumidityMeasurementRel_Type())
lgpEnvHumidityMeasurementRel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityMeasurementRel.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityMeasurementRel.setUnits(_J)
_LgpEnvHumidityHighThresholdRel_Type=Integer32
_LgpEnvHumidityHighThresholdRel_Object=MibTableColumn
lgpEnvHumidityHighThresholdRel=_LgpEnvHumidityHighThresholdRel_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,4),_LgpEnvHumidityHighThresholdRel_Type())
lgpEnvHumidityHighThresholdRel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumidityHighThresholdRel.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityHighThresholdRel.setUnits(_J)
_LgpEnvHumidityLowThresholdRel_Type=Integer32
_LgpEnvHumidityLowThresholdRel_Object=MibTableColumn
lgpEnvHumidityLowThresholdRel=_LgpEnvHumidityLowThresholdRel_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,5),_LgpEnvHumidityLowThresholdRel_Type())
lgpEnvHumidityLowThresholdRel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumidityLowThresholdRel.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityLowThresholdRel.setUnits(_J)
_LgpEnvHumiditySetPoint_Type=Integer32
_LgpEnvHumiditySetPoint_Object=MibTableColumn
lgpEnvHumiditySetPoint=_LgpEnvHumiditySetPoint_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,6),_LgpEnvHumiditySetPoint_Type())
lgpEnvHumiditySetPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumiditySetPoint.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumiditySetPoint.setUnits(_J)
_LgpEnvHumidityDailyHigh_Type=Integer32
_LgpEnvHumidityDailyHigh_Object=MibTableColumn
lgpEnvHumidityDailyHigh=_LgpEnvHumidityDailyHigh_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,7),_LgpEnvHumidityDailyHigh_Type())
lgpEnvHumidityDailyHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityDailyHigh.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDailyHigh.setUnits(_J)
_LgpEnvHumidityDailyLow_Type=Integer32
_LgpEnvHumidityDailyLow_Object=MibTableColumn
lgpEnvHumidityDailyLow=_LgpEnvHumidityDailyLow_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,8),_LgpEnvHumidityDailyLow_Type())
lgpEnvHumidityDailyLow.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityDailyLow.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDailyLow.setUnits(_J)
class _LgpEnvHumidityDailyHighTimeHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_LgpEnvHumidityDailyHighTimeHour_Type.__name__=_D
_LgpEnvHumidityDailyHighTimeHour_Object=MibTableColumn
lgpEnvHumidityDailyHighTimeHour=_LgpEnvHumidityDailyHighTimeHour_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,9),_LgpEnvHumidityDailyHighTimeHour_Type())
lgpEnvHumidityDailyHighTimeHour.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityDailyHighTimeHour.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDailyHighTimeHour.setUnits(_E)
class _LgpEnvHumidityDailyHighTimeMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvHumidityDailyHighTimeMinute_Type.__name__=_D
_LgpEnvHumidityDailyHighTimeMinute_Object=MibTableColumn
lgpEnvHumidityDailyHighTimeMinute=_LgpEnvHumidityDailyHighTimeMinute_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,10),_LgpEnvHumidityDailyHighTimeMinute_Type())
lgpEnvHumidityDailyHighTimeMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityDailyHighTimeMinute.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDailyHighTimeMinute.setUnits(_N)
class _LgpEnvHumidityDailyHighTimeSecond_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvHumidityDailyHighTimeSecond_Type.__name__=_D
_LgpEnvHumidityDailyHighTimeSecond_Object=MibTableColumn
lgpEnvHumidityDailyHighTimeSecond=_LgpEnvHumidityDailyHighTimeSecond_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,11),_LgpEnvHumidityDailyHighTimeSecond_Type())
lgpEnvHumidityDailyHighTimeSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityDailyHighTimeSecond.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDailyHighTimeSecond.setUnits(_O)
class _LgpEnvHumidityDailyLowTimeHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_LgpEnvHumidityDailyLowTimeHour_Type.__name__=_D
_LgpEnvHumidityDailyLowTimeHour_Object=MibTableColumn
lgpEnvHumidityDailyLowTimeHour=_LgpEnvHumidityDailyLowTimeHour_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,12),_LgpEnvHumidityDailyLowTimeHour_Type())
lgpEnvHumidityDailyLowTimeHour.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityDailyLowTimeHour.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDailyLowTimeHour.setUnits(_E)
class _LgpEnvHumidityDailyLowTimeMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvHumidityDailyLowTimeMinute_Type.__name__=_D
_LgpEnvHumidityDailyLowTimeMinute_Object=MibTableColumn
lgpEnvHumidityDailyLowTimeMinute=_LgpEnvHumidityDailyLowTimeMinute_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,13),_LgpEnvHumidityDailyLowTimeMinute_Type())
lgpEnvHumidityDailyLowTimeMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityDailyLowTimeMinute.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDailyLowTimeMinute.setUnits(_N)
class _LgpEnvHumidityDailyLowTimeSecond_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvHumidityDailyLowTimeSecond_Type.__name__=_D
_LgpEnvHumidityDailyLowTimeSecond_Object=MibTableColumn
lgpEnvHumidityDailyLowTimeSecond=_LgpEnvHumidityDailyLowTimeSecond_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,14),_LgpEnvHumidityDailyLowTimeSecond_Type())
lgpEnvHumidityDailyLowTimeSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityDailyLowTimeSecond.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDailyLowTimeSecond.setUnits(_O)
_LgpEnvHumidityDeadBand_Type=Integer32
_LgpEnvHumidityDeadBand_Object=MibTableColumn
lgpEnvHumidityDeadBand=_LgpEnvHumidityDeadBand_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,15),_LgpEnvHumidityDeadBand_Type())
lgpEnvHumidityDeadBand.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumidityDeadBand.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDeadBand.setUnits(_J)
_LgpEnvHumidifyPropBand_Type=Integer32
_LgpEnvHumidifyPropBand_Object=MibTableColumn
lgpEnvHumidifyPropBand=_LgpEnvHumidifyPropBand_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,16),_LgpEnvHumidifyPropBand_Type())
lgpEnvHumidifyPropBand.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumidifyPropBand.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidifyPropBand.setUnits(_J)
_LgpEnvDehumidifyPropBand_Type=Integer32
_LgpEnvDehumidifyPropBand_Object=MibTableColumn
lgpEnvDehumidifyPropBand=_LgpEnvDehumidifyPropBand_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,17),_LgpEnvDehumidifyPropBand_Type())
lgpEnvDehumidifyPropBand.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvDehumidifyPropBand.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvDehumidifyPropBand.setUnits(_J)
_LgpEnvHumidityMeasurementRelTenths_Type=Integer32
_LgpEnvHumidityMeasurementRelTenths_Object=MibTableColumn
lgpEnvHumidityMeasurementRelTenths=_LgpEnvHumidityMeasurementRelTenths_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,50),_LgpEnvHumidityMeasurementRelTenths_Type())
lgpEnvHumidityMeasurementRelTenths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvHumidityMeasurementRelTenths.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityMeasurementRelTenths.setUnits(_V)
_LgpEnvHumidityHighThresholdRelTenths_Type=Integer32
_LgpEnvHumidityHighThresholdRelTenths_Object=MibTableColumn
lgpEnvHumidityHighThresholdRelTenths=_LgpEnvHumidityHighThresholdRelTenths_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,51),_LgpEnvHumidityHighThresholdRelTenths_Type())
lgpEnvHumidityHighThresholdRelTenths.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumidityHighThresholdRelTenths.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityHighThresholdRelTenths.setUnits(_V)
_LgpEnvHumidityLowThresholdRelTenths_Type=Integer32
_LgpEnvHumidityLowThresholdRelTenths_Object=MibTableColumn
lgpEnvHumidityLowThresholdRelTenths=_LgpEnvHumidityLowThresholdRelTenths_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,3,1,52),_LgpEnvHumidityLowThresholdRelTenths_Type())
lgpEnvHumidityLowThresholdRelTenths.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumidityLowThresholdRelTenths.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityLowThresholdRelTenths.setUnits(_V)
_LgpEnvHumidityDeadbandRange_Type=Integer32
_LgpEnvHumidityDeadbandRange_Object=MibScalar
lgpEnvHumidityDeadbandRange=_LgpEnvHumidityDeadbandRange_Object((1,3,6,1,4,1,476,1,42,3,4,2,2,4),_LgpEnvHumidityDeadbandRange_Type())
lgpEnvHumidityDeadbandRange.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvHumidityDeadbandRange.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvHumidityDeadbandRange.setUnits('.1 percent RH')
_LgpEnvState_ObjectIdentity=ObjectIdentity
lgpEnvState=_LgpEnvState_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,3))
if mibBuilder.loadTexts:lgpEnvState.setStatus(_A)
class _LgpEnvStateSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),('standby',3)))
_LgpEnvStateSystem_Type.__name__=_D
_LgpEnvStateSystem_Object=MibScalar
lgpEnvStateSystem=_LgpEnvStateSystem_Object((1,3,6,1,4,1,476,1,42,3,4,3,1),_LgpEnvStateSystem_Type())
lgpEnvStateSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateSystem.setStatus(_A)
class _LgpEnvStateCooling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateCooling_Type.__name__=_D
_LgpEnvStateCooling_Object=MibScalar
lgpEnvStateCooling=_LgpEnvStateCooling_Object((1,3,6,1,4,1,476,1,42,3,4,3,2),_LgpEnvStateCooling_Type())
lgpEnvStateCooling.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateCooling.setStatus(_A)
class _LgpEnvStateHeating_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateHeating_Type.__name__=_D
_LgpEnvStateHeating_Object=MibScalar
lgpEnvStateHeating=_LgpEnvStateHeating_Object((1,3,6,1,4,1,476,1,42,3,4,3,3),_LgpEnvStateHeating_Type())
lgpEnvStateHeating.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateHeating.setStatus(_A)
class _LgpEnvStateHumidifying_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateHumidifying_Type.__name__=_D
_LgpEnvStateHumidifying_Object=MibScalar
lgpEnvStateHumidifying=_LgpEnvStateHumidifying_Object((1,3,6,1,4,1,476,1,42,3,4,3,4),_LgpEnvStateHumidifying_Type())
lgpEnvStateHumidifying.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateHumidifying.setStatus(_A)
class _LgpEnvStateDehumidifying_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateDehumidifying_Type.__name__=_D
_LgpEnvStateDehumidifying_Object=MibScalar
lgpEnvStateDehumidifying=_LgpEnvStateDehumidifying_Object((1,3,6,1,4,1,476,1,42,3,4,3,5),_LgpEnvStateDehumidifying_Type())
lgpEnvStateDehumidifying.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateDehumidifying.setStatus(_A)
class _LgpEnvStateEconoCycle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateEconoCycle_Type.__name__=_D
_LgpEnvStateEconoCycle_Object=MibScalar
lgpEnvStateEconoCycle=_LgpEnvStateEconoCycle_Object((1,3,6,1,4,1,476,1,42,3,4,3,6),_LgpEnvStateEconoCycle_Type())
lgpEnvStateEconoCycle.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateEconoCycle.setStatus(_A)
class _LgpEnvStateFan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateFan_Type.__name__=_D
_LgpEnvStateFan_Object=MibScalar
lgpEnvStateFan=_LgpEnvStateFan_Object((1,3,6,1,4,1,476,1,42,3,4,3,7),_LgpEnvStateFan_Type())
lgpEnvStateFan.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateFan.setStatus(_A)
class _LgpEnvStateGeneralAlarmOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateGeneralAlarmOutput_Type.__name__=_D
_LgpEnvStateGeneralAlarmOutput_Object=MibScalar
lgpEnvStateGeneralAlarmOutput=_LgpEnvStateGeneralAlarmOutput_Object((1,3,6,1,4,1,476,1,42,3,4,3,8),_LgpEnvStateGeneralAlarmOutput_Type())
lgpEnvStateGeneralAlarmOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateGeneralAlarmOutput.setStatus(_A)
_LgpEnvStateCoolingCapacity_Type=Unsigned32
_LgpEnvStateCoolingCapacity_Object=MibScalar
lgpEnvStateCoolingCapacity=_LgpEnvStateCoolingCapacity_Object((1,3,6,1,4,1,476,1,42,3,4,3,9),_LgpEnvStateCoolingCapacity_Type())
lgpEnvStateCoolingCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateCoolingCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStateCoolingCapacity.setUnits(_K)
_LgpEnvStateHeatingCapacity_Type=Unsigned32
_LgpEnvStateHeatingCapacity_Object=MibScalar
lgpEnvStateHeatingCapacity=_LgpEnvStateHeatingCapacity_Object((1,3,6,1,4,1,476,1,42,3,4,3,10),_LgpEnvStateHeatingCapacity_Type())
lgpEnvStateHeatingCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateHeatingCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStateHeatingCapacity.setUnits(_K)
class _LgpEnvStateAudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateAudibleAlarm_Type.__name__=_D
_LgpEnvStateAudibleAlarm_Object=MibScalar
lgpEnvStateAudibleAlarm=_LgpEnvStateAudibleAlarm_Object((1,3,6,1,4,1,476,1,42,3,4,3,11),_LgpEnvStateAudibleAlarm_Type())
lgpEnvStateAudibleAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateAudibleAlarm.setStatus(_A)
_LgpEnvStateCoolingUnits_ObjectIdentity=ObjectIdentity
lgpEnvStateCoolingUnits=_LgpEnvStateCoolingUnits_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,3,12))
if mibBuilder.loadTexts:lgpEnvStateCoolingUnits.setStatus(_A)
class _LgpEnvStateCoolingUnit1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateCoolingUnit1_Type.__name__=_D
_LgpEnvStateCoolingUnit1_Object=MibScalar
lgpEnvStateCoolingUnit1=_LgpEnvStateCoolingUnit1_Object((1,3,6,1,4,1,476,1,42,3,4,3,12,2),_LgpEnvStateCoolingUnit1_Type())
lgpEnvStateCoolingUnit1.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateCoolingUnit1.setStatus(_A)
class _LgpEnvStateCoolingUnit2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateCoolingUnit2_Type.__name__=_D
_LgpEnvStateCoolingUnit2_Object=MibScalar
lgpEnvStateCoolingUnit2=_LgpEnvStateCoolingUnit2_Object((1,3,6,1,4,1,476,1,42,3,4,3,12,3),_LgpEnvStateCoolingUnit2_Type())
lgpEnvStateCoolingUnit2.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateCoolingUnit2.setStatus(_A)
class _LgpEnvStateCoolingUnit3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateCoolingUnit3_Type.__name__=_D
_LgpEnvStateCoolingUnit3_Object=MibScalar
lgpEnvStateCoolingUnit3=_LgpEnvStateCoolingUnit3_Object((1,3,6,1,4,1,476,1,42,3,4,3,12,4),_LgpEnvStateCoolingUnit3_Type())
lgpEnvStateCoolingUnit3.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateCoolingUnit3.setStatus(_A)
class _LgpEnvStateCoolingUnit4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateCoolingUnit4_Type.__name__=_D
_LgpEnvStateCoolingUnit4_Object=MibScalar
lgpEnvStateCoolingUnit4=_LgpEnvStateCoolingUnit4_Object((1,3,6,1,4,1,476,1,42,3,4,3,12,5),_LgpEnvStateCoolingUnit4_Type())
lgpEnvStateCoolingUnit4.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateCoolingUnit4.setStatus(_A)
_LgpEnvStateHeatingUnits_ObjectIdentity=ObjectIdentity
lgpEnvStateHeatingUnits=_LgpEnvStateHeatingUnits_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,3,13))
if mibBuilder.loadTexts:lgpEnvStateHeatingUnits.setStatus(_A)
class _LgpEnvStateHeatingUnit1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateHeatingUnit1_Type.__name__=_D
_LgpEnvStateHeatingUnit1_Object=MibScalar
lgpEnvStateHeatingUnit1=_LgpEnvStateHeatingUnit1_Object((1,3,6,1,4,1,476,1,42,3,4,3,13,2),_LgpEnvStateHeatingUnit1_Type())
lgpEnvStateHeatingUnit1.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateHeatingUnit1.setStatus(_A)
class _LgpEnvStateHeatingUnit2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateHeatingUnit2_Type.__name__=_D
_LgpEnvStateHeatingUnit2_Object=MibScalar
lgpEnvStateHeatingUnit2=_LgpEnvStateHeatingUnit2_Object((1,3,6,1,4,1,476,1,42,3,4,3,13,3),_LgpEnvStateHeatingUnit2_Type())
lgpEnvStateHeatingUnit2.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateHeatingUnit2.setStatus(_A)
class _LgpEnvStateHeatingUnit3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateHeatingUnit3_Type.__name__=_D
_LgpEnvStateHeatingUnit3_Object=MibScalar
lgpEnvStateHeatingUnit3=_LgpEnvStateHeatingUnit3_Object((1,3,6,1,4,1,476,1,42,3,4,3,13,4),_LgpEnvStateHeatingUnit3_Type())
lgpEnvStateHeatingUnit3.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateHeatingUnit3.setStatus(_A)
class _LgpEnvStateHeatingUnit4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateHeatingUnit4_Type.__name__=_D
_LgpEnvStateHeatingUnit4_Object=MibScalar
lgpEnvStateHeatingUnit4=_LgpEnvStateHeatingUnit4_Object((1,3,6,1,4,1,476,1,42,3,4,3,13,5),_LgpEnvStateHeatingUnit4_Type())
lgpEnvStateHeatingUnit4.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateHeatingUnit4.setStatus(_A)
class _LgpEnvStateOperatingReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('localUser',2),('alarm',3),('schedule',4),('remoteUser',5),('externalDevice',6),('localDisplay',7)))
_LgpEnvStateOperatingReason_Type.__name__=_D
_LgpEnvStateOperatingReason_Object=MibScalar
lgpEnvStateOperatingReason=_LgpEnvStateOperatingReason_Object((1,3,6,1,4,1,476,1,42,3,4,3,14),_LgpEnvStateOperatingReason_Type())
lgpEnvStateOperatingReason.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateOperatingReason.setStatus(_A)
class _LgpEnvStateOperatingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_a,2)))
_LgpEnvStateOperatingMode_Type.__name__=_D
_LgpEnvStateOperatingMode_Object=MibScalar
lgpEnvStateOperatingMode=_LgpEnvStateOperatingMode_Object((1,3,6,1,4,1,476,1,42,3,4,3,15),_LgpEnvStateOperatingMode_Type())
lgpEnvStateOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateOperatingMode.setStatus(_A)
_LgpEnvStateFanCapacity_Type=Unsigned32
_LgpEnvStateFanCapacity_Object=MibScalar
lgpEnvStateFanCapacity=_LgpEnvStateFanCapacity_Object((1,3,6,1,4,1,476,1,42,3,4,3,16),_LgpEnvStateFanCapacity_Type())
lgpEnvStateFanCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateFanCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStateFanCapacity.setUnits(_K)
_LgpEnvStateFreeCoolingCapacity_Type=Unsigned32
_LgpEnvStateFreeCoolingCapacity_Object=MibScalar
lgpEnvStateFreeCoolingCapacity=_LgpEnvStateFreeCoolingCapacity_Object((1,3,6,1,4,1,476,1,42,3,4,3,17),_LgpEnvStateFreeCoolingCapacity_Type())
lgpEnvStateFreeCoolingCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateFreeCoolingCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStateFreeCoolingCapacity.setUnits(_K)
_LgpEnvStateDehumidifyingCapacity_Type=Unsigned32
_LgpEnvStateDehumidifyingCapacity_Object=MibScalar
lgpEnvStateDehumidifyingCapacity=_LgpEnvStateDehumidifyingCapacity_Object((1,3,6,1,4,1,476,1,42,3,4,3,18),_LgpEnvStateDehumidifyingCapacity_Type())
lgpEnvStateDehumidifyingCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateDehumidifyingCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStateDehumidifyingCapacity.setUnits(_K)
_LgpEnvStateHumidifyingCapacity_Type=Unsigned32
_LgpEnvStateHumidifyingCapacity_Object=MibScalar
lgpEnvStateHumidifyingCapacity=_LgpEnvStateHumidifyingCapacity_Object((1,3,6,1,4,1,476,1,42,3,4,3,19),_LgpEnvStateHumidifyingCapacity_Type())
lgpEnvStateHumidifyingCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateHumidifyingCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStateHumidifyingCapacity.setUnits(_K)
class _LgpEnvStateFreeCooling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),('start',3),('unavailable',4)))
_LgpEnvStateFreeCooling_Type.__name__=_D
_LgpEnvStateFreeCooling_Object=MibScalar
lgpEnvStateFreeCooling=_LgpEnvStateFreeCooling_Object((1,3,6,1,4,1,476,1,42,3,4,3,20),_LgpEnvStateFreeCooling_Type())
lgpEnvStateFreeCooling.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateFreeCooling.setStatus(_A)
class _LgpEnvStateElectricHeater_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateElectricHeater_Type.__name__=_D
_LgpEnvStateElectricHeater_Object=MibScalar
lgpEnvStateElectricHeater=_LgpEnvStateElectricHeater_Object((1,3,6,1,4,1,476,1,42,3,4,3,21),_LgpEnvStateElectricHeater_Type())
lgpEnvStateElectricHeater.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateElectricHeater.setStatus(_A)
class _LgpEnvStateHotWater_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LgpEnvStateHotWater_Type.__name__=_D
_LgpEnvStateHotWater_Object=MibScalar
lgpEnvStateHotWater=_LgpEnvStateHotWater_Object((1,3,6,1,4,1,476,1,42,3,4,3,22),_LgpEnvStateHotWater_Type())
lgpEnvStateHotWater.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateHotWater.setStatus(_A)
_LgpEnvStateOperatingEfficiency_Type=Unsigned32
_LgpEnvStateOperatingEfficiency_Object=MibScalar
lgpEnvStateOperatingEfficiency=_LgpEnvStateOperatingEfficiency_Object((1,3,6,1,4,1,476,1,42,3,4,3,23),_LgpEnvStateOperatingEfficiency_Type())
lgpEnvStateOperatingEfficiency.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStateOperatingEfficiency.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStateOperatingEfficiency.setUnits(_K)
_LgpEnvComponentStateTable_Object=MibTable
lgpEnvComponentStateTable=_LgpEnvComponentStateTable_Object((1,3,6,1,4,1,476,1,42,3,4,3,50))
if mibBuilder.loadTexts:lgpEnvComponentStateTable.setStatus(_A)
_LgpEnvComponentStateEntry_Object=MibTableRow
lgpEnvComponentStateEntry=_LgpEnvComponentStateEntry_Object((1,3,6,1,4,1,476,1,42,3,4,3,50,1))
lgpEnvComponentStateEntry.setIndexNames((0,_L,_b))
if mibBuilder.loadTexts:lgpEnvComponentStateEntry.setStatus(_A)
_LgpEnvComponentStateIndex_Type=Unsigned32
_LgpEnvComponentStateIndex_Object=MibTableColumn
lgpEnvComponentStateIndex=_LgpEnvComponentStateIndex_Object((1,3,6,1,4,1,476,1,42,3,4,3,50,1,1),_LgpEnvComponentStateIndex_Type())
lgpEnvComponentStateIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:lgpEnvComponentStateIndex.setStatus(_A)
_LgpEnvComponentStateDescr_Type=ObjectIdentifier
_LgpEnvComponentStateDescr_Object=MibTableColumn
lgpEnvComponentStateDescr=_LgpEnvComponentStateDescr_Object((1,3,6,1,4,1,476,1,42,3,4,3,50,1,2),_LgpEnvComponentStateDescr_Type())
lgpEnvComponentStateDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvComponentStateDescr.setStatus(_A)
class _LgpEnvComponentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_c,0),(_F,1),(_G,2)))
_LgpEnvComponentState_Type.__name__=_D
_LgpEnvComponentState_Object=MibTableColumn
lgpEnvComponentState=_LgpEnvComponentState_Object((1,3,6,1,4,1,476,1,42,3,4,3,50,1,3),_LgpEnvComponentState_Type())
lgpEnvComponentState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvComponentState.setStatus(_A)
_LgpEnvValveTable_Object=MibTable
lgpEnvValveTable=_LgpEnvValveTable_Object((1,3,6,1,4,1,476,1,42,3,4,3,70))
if mibBuilder.loadTexts:lgpEnvValveTable.setStatus(_A)
_LgpEnvValveEntry_Object=MibTableRow
lgpEnvValveEntry=_LgpEnvValveEntry_Object((1,3,6,1,4,1,476,1,42,3,4,3,70,1))
lgpEnvValveEntry.setIndexNames((0,_L,_d))
if mibBuilder.loadTexts:lgpEnvValveEntry.setStatus(_A)
_LgpEnvValveIndex_Type=Unsigned32
_LgpEnvValveIndex_Object=MibTableColumn
lgpEnvValveIndex=_LgpEnvValveIndex_Object((1,3,6,1,4,1,476,1,42,3,4,3,70,1,1),_LgpEnvValveIndex_Type())
lgpEnvValveIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:lgpEnvValveIndex.setStatus(_A)
_LgpEnvValveDescr_Type=ObjectIdentifier
_LgpEnvValveDescr_Object=MibTableColumn
lgpEnvValveDescr=_LgpEnvValveDescr_Object((1,3,6,1,4,1,476,1,42,3,4,3,70,1,2),_LgpEnvValveDescr_Type())
lgpEnvValveDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvValveDescr.setStatus(_A)
class _LgpEnvValveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_c,0),('open',1),('closed',2)))
_LgpEnvValveState_Type.__name__=_D
_LgpEnvValveState_Object=MibTableColumn
lgpEnvValveState=_LgpEnvValveState_Object((1,3,6,1,4,1,476,1,42,3,4,3,70,1,3),_LgpEnvValveState_Type())
lgpEnvValveState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvValveState.setStatus(_A)
_LgpEnvValvePositionTenths_Type=Unsigned32
_LgpEnvValvePositionTenths_Object=MibTableColumn
lgpEnvValvePositionTenths=_LgpEnvValvePositionTenths_Object((1,3,6,1,4,1,476,1,42,3,4,3,70,1,20),_LgpEnvValvePositionTenths_Type())
lgpEnvValvePositionTenths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvValvePositionTenths.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvValvePositionTenths.setUnits('.1 percent')
_LgpEnvConfig_ObjectIdentity=ObjectIdentity
lgpEnvConfig=_LgpEnvConfig_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,4))
if mibBuilder.loadTexts:lgpEnvConfig.setStatus(_A)
class _LgpEnvConfigReheatLockout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_LgpEnvConfigReheatLockout_Type.__name__=_D
_LgpEnvConfigReheatLockout_Object=MibScalar
lgpEnvConfigReheatLockout=_LgpEnvConfigReheatLockout_Object((1,3,6,1,4,1,476,1,42,3,4,4,1),_LgpEnvConfigReheatLockout_Type())
lgpEnvConfigReheatLockout.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigReheatLockout.setStatus(_A)
class _LgpEnvConfigHumLockout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_LgpEnvConfigHumLockout_Type.__name__=_D
_LgpEnvConfigHumLockout_Object=MibScalar
lgpEnvConfigHumLockout=_LgpEnvConfigHumLockout_Object((1,3,6,1,4,1,476,1,42,3,4,4,2),_LgpEnvConfigHumLockout_Type())
lgpEnvConfigHumLockout.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigHumLockout.setStatus(_A)
_LgpEnvConfigRestartDelay_Type=Unsigned32
_LgpEnvConfigRestartDelay_Object=MibScalar
lgpEnvConfigRestartDelay=_LgpEnvConfigRestartDelay_Object((1,3,6,1,4,1,476,1,42,3,4,4,4),_LgpEnvConfigRestartDelay_Type())
lgpEnvConfigRestartDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigRestartDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigRestartDelay.setUnits(_O)
class _LgpEnvConfigRemoteShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_R,2)))
_LgpEnvConfigRemoteShutdown_Type.__name__=_D
_LgpEnvConfigRemoteShutdown_Object=MibScalar
lgpEnvConfigRemoteShutdown=_LgpEnvConfigRemoteShutdown_Object((1,3,6,1,4,1,476,1,42,3,4,4,7),_LgpEnvConfigRemoteShutdown_Type())
lgpEnvConfigRemoteShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigRemoteShutdown.setStatus(_A)
_LgpEnvConfigCoolingServiceInterval_Type=Unsigned32
_LgpEnvConfigCoolingServiceInterval_Object=MibScalar
lgpEnvConfigCoolingServiceInterval=_LgpEnvConfigCoolingServiceInterval_Object((1,3,6,1,4,1,476,1,42,3,4,4,8),_LgpEnvConfigCoolingServiceInterval_Type())
lgpEnvConfigCoolingServiceInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigCoolingServiceInterval.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigCoolingServiceInterval.setUnits(_E)
_LgpEnvConfigHumidifierServiceInterval_Type=Unsigned32
_LgpEnvConfigHumidifierServiceInterval_Object=MibScalar
lgpEnvConfigHumidifierServiceInterval=_LgpEnvConfigHumidifierServiceInterval_Object((1,3,6,1,4,1,476,1,42,3,4,4,9),_LgpEnvConfigHumidifierServiceInterval_Type())
lgpEnvConfigHumidifierServiceInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigHumidifierServiceInterval.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigHumidifierServiceInterval.setUnits(_E)
_LgpEnvConfigFilterServiceInterval_Type=Unsigned32
_LgpEnvConfigFilterServiceInterval_Object=MibScalar
lgpEnvConfigFilterServiceInterval=_LgpEnvConfigFilterServiceInterval_Object((1,3,6,1,4,1,476,1,42,3,4,4,10),_LgpEnvConfigFilterServiceInterval_Type())
lgpEnvConfigFilterServiceInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigFilterServiceInterval.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigFilterServiceInterval.setUnits(_E)
_LgpEnvConfigSleepModeDeadbandRangeDegC_Type=Integer32
_LgpEnvConfigSleepModeDeadbandRangeDegC_Object=MibScalar
lgpEnvConfigSleepModeDeadbandRangeDegC=_LgpEnvConfigSleepModeDeadbandRangeDegC_Object((1,3,6,1,4,1,476,1,42,3,4,4,11),_LgpEnvConfigSleepModeDeadbandRangeDegC_Type())
lgpEnvConfigSleepModeDeadbandRangeDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigSleepModeDeadbandRangeDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigSleepModeDeadbandRangeDegC.setUnits(_Q)
_LgpEnvConfigSleepModeDeadbandRangeDegF_Type=Integer32
_LgpEnvConfigSleepModeDeadbandRangeDegF_Object=MibScalar
lgpEnvConfigSleepModeDeadbandRangeDegF=_LgpEnvConfigSleepModeDeadbandRangeDegF_Object((1,3,6,1,4,1,476,1,42,3,4,4,12),_LgpEnvConfigSleepModeDeadbandRangeDegF_Type())
lgpEnvConfigSleepModeDeadbandRangeDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigSleepModeDeadbandRangeDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigSleepModeDeadbandRangeDegF.setUnits(_P)
_LgpEnvConfigSupplyTempLowLimitDegF_Type=Integer32
_LgpEnvConfigSupplyTempLowLimitDegF_Object=MibScalar
lgpEnvConfigSupplyTempLowLimitDegF=_LgpEnvConfigSupplyTempLowLimitDegF_Object((1,3,6,1,4,1,476,1,42,3,4,4,13),_LgpEnvConfigSupplyTempLowLimitDegF_Type())
lgpEnvConfigSupplyTempLowLimitDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigSupplyTempLowLimitDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigSupplyTempLowLimitDegF.setUnits(_H)
_LgpEnvConfigSupplyTempLowLimitDegC_Type=Integer32
_LgpEnvConfigSupplyTempLowLimitDegC_Object=MibScalar
lgpEnvConfigSupplyTempLowLimitDegC=_LgpEnvConfigSupplyTempLowLimitDegC_Object((1,3,6,1,4,1,476,1,42,3,4,4,14),_LgpEnvConfigSupplyTempLowLimitDegC_Type())
lgpEnvConfigSupplyTempLowLimitDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigSupplyTempLowLimitDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigSupplyTempLowLimitDegC.setUnits(_I)
_LgpEnvConfigTemperatureIntegTime_Type=Integer32
_LgpEnvConfigTemperatureIntegTime_Object=MibScalar
lgpEnvConfigTemperatureIntegTime=_LgpEnvConfigTemperatureIntegTime_Object((1,3,6,1,4,1,476,1,42,3,4,4,15),_LgpEnvConfigTemperatureIntegTime_Type())
lgpEnvConfigTemperatureIntegTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigTemperatureIntegTime.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigTemperatureIntegTime.setUnits(_N)
class _LgpEnvConfigLocalTemperatureUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('degC',1),('degF',2)))
_LgpEnvConfigLocalTemperatureUnit_Type.__name__=_D
_LgpEnvConfigLocalTemperatureUnit_Object=MibScalar
lgpEnvConfigLocalTemperatureUnit=_LgpEnvConfigLocalTemperatureUnit_Object((1,3,6,1,4,1,476,1,42,3,4,4,16),_LgpEnvConfigLocalTemperatureUnit_Type())
lgpEnvConfigLocalTemperatureUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigLocalTemperatureUnit.setStatus(_A)
class _LgpEnvConfigSleepMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_M,2),(_W,3)))
_LgpEnvConfigSleepMode_Type.__name__=_D
_LgpEnvConfigSleepMode_Object=MibScalar
lgpEnvConfigSleepMode=_LgpEnvConfigSleepMode_Object((1,3,6,1,4,1,476,1,42,3,4,4,17),_LgpEnvConfigSleepMode_Type())
lgpEnvConfigSleepMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigSleepMode.setStatus(_A)
_LgpEnvConfigHumidityIntegTime_Type=Integer32
_LgpEnvConfigHumidityIntegTime_Object=MibScalar
lgpEnvConfigHumidityIntegTime=_LgpEnvConfigHumidityIntegTime_Object((1,3,6,1,4,1,476,1,42,3,4,4,18),_LgpEnvConfigHumidityIntegTime_Type())
lgpEnvConfigHumidityIntegTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigHumidityIntegTime.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigHumidityIntegTime.setUnits(_N)
_LgpEnvConfigFreecoolingDeltaDegF_Type=Integer32
_LgpEnvConfigFreecoolingDeltaDegF_Object=MibScalar
lgpEnvConfigFreecoolingDeltaDegF=_LgpEnvConfigFreecoolingDeltaDegF_Object((1,3,6,1,4,1,476,1,42,3,4,4,19),_LgpEnvConfigFreecoolingDeltaDegF_Type())
lgpEnvConfigFreecoolingDeltaDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigFreecoolingDeltaDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigFreecoolingDeltaDegF.setUnits(_H)
_LgpEnvConfigFreecoolingDeltaDegC_Type=Integer32
_LgpEnvConfigFreecoolingDeltaDegC_Object=MibScalar
lgpEnvConfigFreecoolingDeltaDegC=_LgpEnvConfigFreecoolingDeltaDegC_Object((1,3,6,1,4,1,476,1,42,3,4,4,20),_LgpEnvConfigFreecoolingDeltaDegC_Type())
lgpEnvConfigFreecoolingDeltaDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigFreecoolingDeltaDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigFreecoolingDeltaDegC.setUnits(_I)
class _LgpEnvConfigSupplyTempLowLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_R,2)))
_LgpEnvConfigSupplyTempLowLimit_Type.__name__=_D
_LgpEnvConfigSupplyTempLowLimit_Object=MibScalar
lgpEnvConfigSupplyTempLowLimit=_LgpEnvConfigSupplyTempLowLimit_Object((1,3,6,1,4,1,476,1,42,3,4,4,21),_LgpEnvConfigSupplyTempLowLimit_Type())
lgpEnvConfigSupplyTempLowLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigSupplyTempLowLimit.setStatus(_A)
class _LgpEnvConfigSensorEventsStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_R,2)))
_LgpEnvConfigSensorEventsStandard_Type.__name__=_D
_LgpEnvConfigSensorEventsStandard_Object=MibScalar
lgpEnvConfigSensorEventsStandard=_LgpEnvConfigSensorEventsStandard_Object((1,3,6,1,4,1,476,1,42,3,4,4,22),_LgpEnvConfigSensorEventsStandard_Type())
lgpEnvConfigSensorEventsStandard.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigSensorEventsStandard.setStatus(_A)
class _LgpEnvConfigSensorEvents1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_R,2)))
_LgpEnvConfigSensorEvents1_Type.__name__=_D
_LgpEnvConfigSensorEvents1_Object=MibScalar
lgpEnvConfigSensorEvents1=_LgpEnvConfigSensorEvents1_Object((1,3,6,1,4,1,476,1,42,3,4,4,23),_LgpEnvConfigSensorEvents1_Type())
lgpEnvConfigSensorEvents1.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigSensorEvents1.setStatus(_A)
class _LgpEnvConfigSleepModeDeadbandRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_R,2)))
_LgpEnvConfigSleepModeDeadbandRange_Type.__name__=_D
_LgpEnvConfigSleepModeDeadbandRange_Object=MibScalar
lgpEnvConfigSleepModeDeadbandRange=_LgpEnvConfigSleepModeDeadbandRange_Object((1,3,6,1,4,1,476,1,42,3,4,4,24),_LgpEnvConfigSleepModeDeadbandRange_Type())
lgpEnvConfigSleepModeDeadbandRange.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigSleepModeDeadbandRange.setStatus(_A)
class _LgpEnvConfigAutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_R,2)))
_LgpEnvConfigAutoConfiguration_Type.__name__=_D
_LgpEnvConfigAutoConfiguration_Object=MibScalar
lgpEnvConfigAutoConfiguration=_LgpEnvConfigAutoConfiguration_Object((1,3,6,1,4,1,476,1,42,3,4,4,25),_LgpEnvConfigAutoConfiguration_Type())
lgpEnvConfigAutoConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigAutoConfiguration.setStatus(_A)
class _LgpEnvConfigDeltaGlycolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('contact',2),('value',3)))
_LgpEnvConfigDeltaGlycolType_Type.__name__=_D
_LgpEnvConfigDeltaGlycolType_Object=MibScalar
lgpEnvConfigDeltaGlycolType=_LgpEnvConfigDeltaGlycolType_Object((1,3,6,1,4,1,476,1,42,3,4,4,26),_LgpEnvConfigDeltaGlycolType_Type())
lgpEnvConfigDeltaGlycolType.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigDeltaGlycolType.setStatus(_A)
class _LgpEnvConfigChillWaterControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_R,2)))
_LgpEnvConfigChillWaterControl_Type.__name__=_D
_LgpEnvConfigChillWaterControl_Object=MibScalar
lgpEnvConfigChillWaterControl=_LgpEnvConfigChillWaterControl_Object((1,3,6,1,4,1,476,1,42,3,4,4,27),_LgpEnvConfigChillWaterControl_Type())
lgpEnvConfigChillWaterControl.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigChillWaterControl.setStatus(_A)
_LgpEnvConfigInfaredFlushRate_Type=Unsigned32
_LgpEnvConfigInfaredFlushRate_Object=MibScalar
lgpEnvConfigInfaredFlushRate=_LgpEnvConfigInfaredFlushRate_Object((1,3,6,1,4,1,476,1,42,3,4,4,28),_LgpEnvConfigInfaredFlushRate_Type())
lgpEnvConfigInfaredFlushRate.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigInfaredFlushRate.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigInfaredFlushRate.setUnits(_K)
class _LgpEnvConfigHumidityControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('relative',1),('compensated',2),('predictive',3)))
_LgpEnvConfigHumidityControl_Type.__name__=_D
_LgpEnvConfigHumidityControl_Object=MibScalar
lgpEnvConfigHumidityControl=_LgpEnvConfigHumidityControl_Object((1,3,6,1,4,1,476,1,42,3,4,4,29),_LgpEnvConfigHumidityControl_Type())
lgpEnvConfigHumidityControl.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigHumidityControl.setStatus(_A)
class _LgpEnvConfigCompressorLockout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_LgpEnvConfigCompressorLockout_Type.__name__=_D
_LgpEnvConfigCompressorLockout_Object=MibScalar
lgpEnvConfigCompressorLockout=_LgpEnvConfigCompressorLockout_Object((1,3,6,1,4,1,476,1,42,3,4,4,30),_LgpEnvConfigCompressorLockout_Type())
lgpEnvConfigCompressorLockout.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigCompressorLockout.setStatus(_A)
class _LgpEnvConfigReheatAndHumidifierLockout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_LgpEnvConfigReheatAndHumidifierLockout_Type.__name__=_D
_LgpEnvConfigReheatAndHumidifierLockout_Object=MibScalar
lgpEnvConfigReheatAndHumidifierLockout=_LgpEnvConfigReheatAndHumidifierLockout_Object((1,3,6,1,4,1,476,1,42,3,4,4,31),_LgpEnvConfigReheatAndHumidifierLockout_Type())
lgpEnvConfigReheatAndHumidifierLockout.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigReheatAndHumidifierLockout.setStatus(_A)
_LgpEnvOperationalTimeTable_Object=MibTable
lgpEnvOperationalTimeTable=_LgpEnvOperationalTimeTable_Object((1,3,6,1,4,1,476,1,42,3,4,4,32))
if mibBuilder.loadTexts:lgpEnvOperationalTimeTable.setStatus(_A)
_LgpEnvOperationalTimeEntry_Object=MibTableRow
lgpEnvOperationalTimeEntry=_LgpEnvOperationalTimeEntry_Object((1,3,6,1,4,1,476,1,42,3,4,4,32,1))
lgpEnvOperationalTimeEntry.setIndexNames((0,_L,_e))
if mibBuilder.loadTexts:lgpEnvOperationalTimeEntry.setStatus(_A)
_LgpEnvOperationTimeIndex_Type=Unsigned32
_LgpEnvOperationTimeIndex_Object=MibTableColumn
lgpEnvOperationTimeIndex=_LgpEnvOperationTimeIndex_Object((1,3,6,1,4,1,476,1,42,3,4,4,32,1,1),_LgpEnvOperationTimeIndex_Type())
lgpEnvOperationTimeIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:lgpEnvOperationTimeIndex.setStatus(_A)
_LgpEnvOperationTimePoint_Type=ObjectIdentifier
_LgpEnvOperationTimePoint_Object=MibTableColumn
lgpEnvOperationTimePoint=_LgpEnvOperationTimePoint_Object((1,3,6,1,4,1,476,1,42,3,4,4,32,1,2),_LgpEnvOperationTimePoint_Type())
lgpEnvOperationTimePoint.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvOperationTimePoint.setStatus(_A)
_LgpEnvOperationTimeSubID_Type=Integer32
_LgpEnvOperationTimeSubID_Object=MibTableColumn
lgpEnvOperationTimeSubID=_LgpEnvOperationTimeSubID_Object((1,3,6,1,4,1,476,1,42,3,4,4,32,1,3),_LgpEnvOperationTimeSubID_Type())
lgpEnvOperationTimeSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvOperationTimeSubID.setStatus(_A)
_LgpEnvOperationTimeUnit_Type=ObjectIdentifier
_LgpEnvOperationTimeUnit_Object=MibTableColumn
lgpEnvOperationTimeUnit=_LgpEnvOperationTimeUnit_Object((1,3,6,1,4,1,476,1,42,3,4,4,32,1,4),_LgpEnvOperationTimeUnit_Type())
lgpEnvOperationTimeUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvOperationTimeUnit.setStatus(_A)
_LgpEnvOperationTimeValue_Type=Integer32
_LgpEnvOperationTimeValue_Object=MibTableColumn
lgpEnvOperationTimeValue=_LgpEnvOperationTimeValue_Object((1,3,6,1,4,1,476,1,42,3,4,4,32,1,5),_LgpEnvOperationTimeValue_Type())
lgpEnvOperationTimeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvOperationTimeValue.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvOperationTimeValue.setUnits(_E)
_LgpEnvOperationTimeHighWarning_Type=Integer32
_LgpEnvOperationTimeHighWarning_Object=MibTableColumn
lgpEnvOperationTimeHighWarning=_LgpEnvOperationTimeHighWarning_Object((1,3,6,1,4,1,476,1,42,3,4,4,32,1,6),_LgpEnvOperationTimeHighWarning_Type())
lgpEnvOperationTimeHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvOperationTimeHighWarning.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvOperationTimeHighWarning.setUnits(_E)
class _LgpEnvConfigTempControlAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pi',1),('pid',2),('intelligent',3),('proportional',4)))
_LgpEnvConfigTempControlAlgorithm_Type.__name__=_D
_LgpEnvConfigTempControlAlgorithm_Object=MibScalar
lgpEnvConfigTempControlAlgorithm=_LgpEnvConfigTempControlAlgorithm_Object((1,3,6,1,4,1,476,1,42,3,4,4,33),_LgpEnvConfigTempControlAlgorithm_Type())
lgpEnvConfigTempControlAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigTempControlAlgorithm.setStatus(_A)
class _LgpEnvConfigFanSpeedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_W,2)))
_LgpEnvConfigFanSpeedMode_Type.__name__=_D
_LgpEnvConfigFanSpeedMode_Object=MibScalar
lgpEnvConfigFanSpeedMode=_LgpEnvConfigFanSpeedMode_Object((1,3,6,1,4,1,476,1,42,3,4,4,34),_LgpEnvConfigFanSpeedMode_Type())
lgpEnvConfigFanSpeedMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigFanSpeedMode.setStatus(_A)
_LgpEnvConfigFanSpeedCapacity_Type=Unsigned32
_LgpEnvConfigFanSpeedCapacity_Object=MibScalar
lgpEnvConfigFanSpeedCapacity=_LgpEnvConfigFanSpeedCapacity_Object((1,3,6,1,4,1,476,1,42,3,4,4,35),_LgpEnvConfigFanSpeedCapacity_Type())
lgpEnvConfigFanSpeedCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigFanSpeedCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigFanSpeedCapacity.setUnits(_K)
_LgpEnvConfigBmsResetTimer_Type=Unsigned32
_LgpEnvConfigBmsResetTimer_Object=MibScalar
lgpEnvConfigBmsResetTimer=_LgpEnvConfigBmsResetTimer_Object((1,3,6,1,4,1,476,1,42,3,4,4,36),_LgpEnvConfigBmsResetTimer_Type())
lgpEnvConfigBmsResetTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigBmsResetTimer.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigBmsResetTimer.setUnits(_N)
_LgpEnvConfigDisableSensorOffsetDegC_Type=Integer32
_LgpEnvConfigDisableSensorOffsetDegC_Object=MibScalar
lgpEnvConfigDisableSensorOffsetDegC=_LgpEnvConfigDisableSensorOffsetDegC_Object((1,3,6,1,4,1,476,1,42,3,4,4,37),_LgpEnvConfigDisableSensorOffsetDegC_Type())
lgpEnvConfigDisableSensorOffsetDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigDisableSensorOffsetDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigDisableSensorOffsetDegC.setUnits(_I)
_LgpEnvConfigDisableSensorOffsetDegF_Type=Integer32
_LgpEnvConfigDisableSensorOffsetDegF_Object=MibScalar
lgpEnvConfigDisableSensorOffsetDegF=_LgpEnvConfigDisableSensorOffsetDegF_Object((1,3,6,1,4,1,476,1,42,3,4,4,38),_LgpEnvConfigDisableSensorOffsetDegF_Type())
lgpEnvConfigDisableSensorOffsetDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigDisableSensorOffsetDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigDisableSensorOffsetDegF.setUnits(_H)
class _LgpEnvConfigCabinetSensorAlarms_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_R,1)))
_LgpEnvConfigCabinetSensorAlarms_Type.__name__=_D
_LgpEnvConfigCabinetSensorAlarms_Object=MibScalar
lgpEnvConfigCabinetSensorAlarms=_LgpEnvConfigCabinetSensorAlarms_Object((1,3,6,1,4,1,476,1,42,3,4,4,39),_LgpEnvConfigCabinetSensorAlarms_Type())
lgpEnvConfigCabinetSensorAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigCabinetSensorAlarms.setStatus(_A)
class _LgpEnvConfigAirTemperatureControlSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_g,2),(_h,3)))
_LgpEnvConfigAirTemperatureControlSensor_Type.__name__=_D
_LgpEnvConfigAirTemperatureControlSensor_Object=MibScalar
lgpEnvConfigAirTemperatureControlSensor=_LgpEnvConfigAirTemperatureControlSensor_Object((1,3,6,1,4,1,476,1,42,3,4,4,42),_LgpEnvConfigAirTemperatureControlSensor_Type())
lgpEnvConfigAirTemperatureControlSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigAirTemperatureControlSensor.setStatus(_A)
class _LgpEnvConfigFanSpeedControlSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_g,2),(_h,3)))
_LgpEnvConfigFanSpeedControlSensor_Type.__name__=_D
_LgpEnvConfigFanSpeedControlSensor_Object=MibScalar
lgpEnvConfigFanSpeedControlSensor=_LgpEnvConfigFanSpeedControlSensor_Object((1,3,6,1,4,1,476,1,42,3,4,4,43),_LgpEnvConfigFanSpeedControlSensor_Type())
lgpEnvConfigFanSpeedControlSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigFanSpeedControlSensor.setStatus(_A)
_LgpEnvConfigMinFanSpeed_Type=Unsigned32
_LgpEnvConfigMinFanSpeed_Object=MibScalar
lgpEnvConfigMinFanSpeed=_LgpEnvConfigMinFanSpeed_Object((1,3,6,1,4,1,476,1,42,3,4,4,44),_LgpEnvConfigMinFanSpeed_Type())
lgpEnvConfigMinFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigMinFanSpeed.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigMinFanSpeed.setUnits(_K)
_LgpEnvConfigMaxFanSpeed_Type=Unsigned32
_LgpEnvConfigMaxFanSpeed_Object=MibScalar
lgpEnvConfigMaxFanSpeed=_LgpEnvConfigMaxFanSpeed_Object((1,3,6,1,4,1,476,1,42,3,4,4,45),_LgpEnvConfigMaxFanSpeed_Type())
lgpEnvConfigMaxFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigMaxFanSpeed.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigMaxFanSpeed.setUnits(_K)
_LgpEnvConfigFanSpeedPropBandDegC_Type=Integer32
_LgpEnvConfigFanSpeedPropBandDegC_Object=MibScalar
lgpEnvConfigFanSpeedPropBandDegC=_LgpEnvConfigFanSpeedPropBandDegC_Object((1,3,6,1,4,1,476,1,42,3,4,4,46),_LgpEnvConfigFanSpeedPropBandDegC_Type())
lgpEnvConfigFanSpeedPropBandDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigFanSpeedPropBandDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigFanSpeedPropBandDegC.setUnits(_I)
_LgpEnvConfigFanSpeedPropBandDegF_Type=Integer32
_LgpEnvConfigFanSpeedPropBandDegF_Object=MibScalar
lgpEnvConfigFanSpeedPropBandDegF=_LgpEnvConfigFanSpeedPropBandDegF_Object((1,3,6,1,4,1,476,1,42,3,4,4,47),_LgpEnvConfigFanSpeedPropBandDegF_Type())
lgpEnvConfigFanSpeedPropBandDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvConfigFanSpeedPropBandDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvConfigFanSpeedPropBandDegF.setUnits(_H)
_LgpEnvControl_ObjectIdentity=ObjectIdentity
lgpEnvControl=_LgpEnvControl_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,5))
if mibBuilder.loadTexts:lgpEnvControl.setStatus(_A)
class _LgpEnvControlShutdownAfterDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LgpEnvControlShutdownAfterDelay_Type.__name__=_D
_LgpEnvControlShutdownAfterDelay_Object=MibScalar
lgpEnvControlShutdownAfterDelay=_LgpEnvControlShutdownAfterDelay_Object((1,3,6,1,4,1,476,1,42,3,4,5,1),_LgpEnvControlShutdownAfterDelay_Type())
lgpEnvControlShutdownAfterDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvControlShutdownAfterDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvControlShutdownAfterDelay.setUnits(_O)
class _LgpEnvControlStartupAfterDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LgpEnvControlStartupAfterDelay_Type.__name__=_D
_LgpEnvControlStartupAfterDelay_Object=MibScalar
lgpEnvControlStartupAfterDelay=_LgpEnvControlStartupAfterDelay_Object((1,3,6,1,4,1,476,1,42,3,4,5,2),_LgpEnvControlStartupAfterDelay_Type())
lgpEnvControlStartupAfterDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvControlStartupAfterDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvControlStartupAfterDelay.setUnits(_O)
_LgpEnvSleepIntervalTimeTable_Object=MibTable
lgpEnvSleepIntervalTimeTable=_LgpEnvSleepIntervalTimeTable_Object((1,3,6,1,4,1,476,1,42,3,4,5,3))
if mibBuilder.loadTexts:lgpEnvSleepIntervalTimeTable.setStatus(_A)
_LgpEnvSleepIntervalTimeEntry_Object=MibTableRow
lgpEnvSleepIntervalTimeEntry=_LgpEnvSleepIntervalTimeEntry_Object((1,3,6,1,4,1,476,1,42,3,4,5,3,1))
lgpEnvSleepIntervalTimeEntry.setIndexNames((0,_L,_i))
if mibBuilder.loadTexts:lgpEnvSleepIntervalTimeEntry.setStatus(_A)
_LgpEnvSleepTimeIndex_Type=Unsigned32
_LgpEnvSleepTimeIndex_Object=MibTableColumn
lgpEnvSleepTimeIndex=_LgpEnvSleepTimeIndex_Object((1,3,6,1,4,1,476,1,42,3,4,5,3,1,1),_LgpEnvSleepTimeIndex_Type())
lgpEnvSleepTimeIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:lgpEnvSleepTimeIndex.setStatus(_A)
_LgpEnvSleepTimeSubID_Type=Integer32
_LgpEnvSleepTimeSubID_Object=MibTableColumn
lgpEnvSleepTimeSubID=_LgpEnvSleepTimeSubID_Object((1,3,6,1,4,1,476,1,42,3,4,5,3,1,2),_LgpEnvSleepTimeSubID_Type())
lgpEnvSleepTimeSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvSleepTimeSubID.setStatus(_A)
class _LgpEnvSleepTimeStartHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_LgpEnvSleepTimeStartHour_Type.__name__=_D
_LgpEnvSleepTimeStartHour_Object=MibTableColumn
lgpEnvSleepTimeStartHour=_LgpEnvSleepTimeStartHour_Object((1,3,6,1,4,1,476,1,42,3,4,5,3,1,3),_LgpEnvSleepTimeStartHour_Type())
lgpEnvSleepTimeStartHour.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvSleepTimeStartHour.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvSleepTimeStartHour.setUnits('hour')
class _LgpEnvSleepTimeStartMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvSleepTimeStartMinute_Type.__name__=_D
_LgpEnvSleepTimeStartMinute_Object=MibTableColumn
lgpEnvSleepTimeStartMinute=_LgpEnvSleepTimeStartMinute_Object((1,3,6,1,4,1,476,1,42,3,4,5,3,1,4),_LgpEnvSleepTimeStartMinute_Type())
lgpEnvSleepTimeStartMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvSleepTimeStartMinute.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvSleepTimeStartMinute.setUnits(_j)
class _LgpEnvSleepTimeStopHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_LgpEnvSleepTimeStopHour_Type.__name__=_D
_LgpEnvSleepTimeStopHour_Object=MibTableColumn
lgpEnvSleepTimeStopHour=_LgpEnvSleepTimeStopHour_Object((1,3,6,1,4,1,476,1,42,3,4,5,3,1,5),_LgpEnvSleepTimeStopHour_Type())
lgpEnvSleepTimeStopHour.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvSleepTimeStopHour.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvSleepTimeStopHour.setUnits('hour')
class _LgpEnvSleepTimeStopMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_LgpEnvSleepTimeStopMinute_Type.__name__=_D
_LgpEnvSleepTimeStopMinute_Object=MibTableColumn
lgpEnvSleepTimeStopMinute=_LgpEnvSleepTimeStopMinute_Object((1,3,6,1,4,1,476,1,42,3,4,5,3,1,6),_LgpEnvSleepTimeStopMinute_Type())
lgpEnvSleepTimeStopMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvSleepTimeStopMinute.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvSleepTimeStopMinute.setUnits(_j)
_LgpEnvSleepDayTable_Object=MibTable
lgpEnvSleepDayTable=_LgpEnvSleepDayTable_Object((1,3,6,1,4,1,476,1,42,3,4,5,4))
if mibBuilder.loadTexts:lgpEnvSleepDayTable.setStatus(_A)
_LgpEnvSleepDayEntry_Object=MibTableRow
lgpEnvSleepDayEntry=_LgpEnvSleepDayEntry_Object((1,3,6,1,4,1,476,1,42,3,4,5,4,1))
lgpEnvSleepDayEntry.setIndexNames((0,_L,_k))
if mibBuilder.loadTexts:lgpEnvSleepDayEntry.setStatus(_A)
_LgpEnvSleepDayIndex_Type=Unsigned32
_LgpEnvSleepDayIndex_Object=MibTableColumn
lgpEnvSleepDayIndex=_LgpEnvSleepDayIndex_Object((1,3,6,1,4,1,476,1,42,3,4,5,4,1,1),_LgpEnvSleepDayIndex_Type())
lgpEnvSleepDayIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:lgpEnvSleepDayIndex.setStatus(_A)
class _LgpEnvSleepDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('sunday',1),('monday',2),('tuesday',3),('wednesday',4),('thursday',5),('friday',6),('saturday',7)))
_LgpEnvSleepDay_Type.__name__=_D
_LgpEnvSleepDay_Object=MibTableColumn
lgpEnvSleepDay=_LgpEnvSleepDay_Object((1,3,6,1,4,1,476,1,42,3,4,5,4,1,2),_LgpEnvSleepDay_Type())
lgpEnvSleepDay.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvSleepDay.setStatus(_A)
class _LgpEnvSleepAllDayEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_LgpEnvSleepAllDayEnabled_Type.__name__=_D
_LgpEnvSleepAllDayEnabled_Object=MibTableColumn
lgpEnvSleepAllDayEnabled=_LgpEnvSleepAllDayEnabled_Object((1,3,6,1,4,1,476,1,42,3,4,5,4,1,3),_LgpEnvSleepAllDayEnabled_Type())
lgpEnvSleepAllDayEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvSleepAllDayEnabled.setStatus(_A)
_LgpEnvStatistics_ObjectIdentity=ObjectIdentity
lgpEnvStatistics=_LgpEnvStatistics_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,6))
if mibBuilder.loadTexts:lgpEnvStatistics.setStatus(_A)
_LgpEnvStatisticsComp1RunHr_Type=Unsigned32
_LgpEnvStatisticsComp1RunHr_Object=MibScalar
lgpEnvStatisticsComp1RunHr=_LgpEnvStatisticsComp1RunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,1),_LgpEnvStatisticsComp1RunHr_Type())
lgpEnvStatisticsComp1RunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsComp1RunHr.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsComp1RunHr.setUnits(_E)
_LgpEnvStatisticsComp2RunHr_Type=Unsigned32
_LgpEnvStatisticsComp2RunHr_Object=MibScalar
lgpEnvStatisticsComp2RunHr=_LgpEnvStatisticsComp2RunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,2),_LgpEnvStatisticsComp2RunHr_Type())
lgpEnvStatisticsComp2RunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsComp2RunHr.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsComp2RunHr.setUnits(_E)
_LgpEnvStatisticsFanRunHr_Type=Unsigned32
_LgpEnvStatisticsFanRunHr_Object=MibScalar
lgpEnvStatisticsFanRunHr=_LgpEnvStatisticsFanRunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,3),_LgpEnvStatisticsFanRunHr_Type())
lgpEnvStatisticsFanRunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsFanRunHr.setStatus(_A)
_LgpEnvStatisticsHumRunHr_Type=Unsigned32
_LgpEnvStatisticsHumRunHr_Object=MibScalar
lgpEnvStatisticsHumRunHr=_LgpEnvStatisticsHumRunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,4),_LgpEnvStatisticsHumRunHr_Type())
lgpEnvStatisticsHumRunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsHumRunHr.setStatus(_A)
_LgpEnvStatisticsReheat1RunHr_Type=Unsigned32
_LgpEnvStatisticsReheat1RunHr_Object=MibScalar
lgpEnvStatisticsReheat1RunHr=_LgpEnvStatisticsReheat1RunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,7),_LgpEnvStatisticsReheat1RunHr_Type())
lgpEnvStatisticsReheat1RunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsReheat1RunHr.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsReheat1RunHr.setUnits(_E)
_LgpEnvStatisticsReheat2RunHr_Type=Unsigned32
_LgpEnvStatisticsReheat2RunHr_Object=MibScalar
lgpEnvStatisticsReheat2RunHr=_LgpEnvStatisticsReheat2RunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,8),_LgpEnvStatisticsReheat2RunHr_Type())
lgpEnvStatisticsReheat2RunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsReheat2RunHr.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsReheat2RunHr.setUnits(_E)
_LgpEnvStatisticsReheat3RunHr_Type=Unsigned32
_LgpEnvStatisticsReheat3RunHr_Object=MibScalar
lgpEnvStatisticsReheat3RunHr=_LgpEnvStatisticsReheat3RunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,9),_LgpEnvStatisticsReheat3RunHr_Type())
lgpEnvStatisticsReheat3RunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsReheat3RunHr.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsReheat3RunHr.setUnits(_E)
_LgpEnvStatisticsCoolingModeHrs_Type=Unsigned32
_LgpEnvStatisticsCoolingModeHrs_Object=MibScalar
lgpEnvStatisticsCoolingModeHrs=_LgpEnvStatisticsCoolingModeHrs_Object((1,3,6,1,4,1,476,1,42,3,4,6,10),_LgpEnvStatisticsCoolingModeHrs_Type())
lgpEnvStatisticsCoolingModeHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsCoolingModeHrs.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsCoolingModeHrs.setUnits(_E)
_LgpEnvStatisticsHeatingModeHrs_Type=Unsigned32
_LgpEnvStatisticsHeatingModeHrs_Object=MibScalar
lgpEnvStatisticsHeatingModeHrs=_LgpEnvStatisticsHeatingModeHrs_Object((1,3,6,1,4,1,476,1,42,3,4,6,11),_LgpEnvStatisticsHeatingModeHrs_Type())
lgpEnvStatisticsHeatingModeHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsHeatingModeHrs.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsHeatingModeHrs.setUnits(_E)
_LgpEnvStatisticsHumidifyModeHrs_Type=Unsigned32
_LgpEnvStatisticsHumidifyModeHrs_Object=MibScalar
lgpEnvStatisticsHumidifyModeHrs=_LgpEnvStatisticsHumidifyModeHrs_Object((1,3,6,1,4,1,476,1,42,3,4,6,12),_LgpEnvStatisticsHumidifyModeHrs_Type())
lgpEnvStatisticsHumidifyModeHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsHumidifyModeHrs.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsHumidifyModeHrs.setUnits(_E)
_LgpEnvStatisticsDehumidifyModeHrs_Type=Unsigned32
_LgpEnvStatisticsDehumidifyModeHrs_Object=MibScalar
lgpEnvStatisticsDehumidifyModeHrs=_LgpEnvStatisticsDehumidifyModeHrs_Object((1,3,6,1,4,1,476,1,42,3,4,6,13),_LgpEnvStatisticsDehumidifyModeHrs_Type())
lgpEnvStatisticsDehumidifyModeHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsDehumidifyModeHrs.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsDehumidifyModeHrs.setUnits(_E)
_LgpEnvStatisticsHotGasRunHr_Type=Unsigned32
_LgpEnvStatisticsHotGasRunHr_Object=MibScalar
lgpEnvStatisticsHotGasRunHr=_LgpEnvStatisticsHotGasRunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,14),_LgpEnvStatisticsHotGasRunHr_Type())
lgpEnvStatisticsHotGasRunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsHotGasRunHr.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsHotGasRunHr.setUnits(_E)
_LgpEnvStatisticsHotWaterRunHr_Type=Unsigned32
_LgpEnvStatisticsHotWaterRunHr_Object=MibScalar
lgpEnvStatisticsHotWaterRunHr=_LgpEnvStatisticsHotWaterRunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,15),_LgpEnvStatisticsHotWaterRunHr_Type())
lgpEnvStatisticsHotWaterRunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsHotWaterRunHr.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsHotWaterRunHr.setUnits(_E)
_LgpEnvStatisticsFreeCoolRunHr_Type=Unsigned32
_LgpEnvStatisticsFreeCoolRunHr_Object=MibScalar
lgpEnvStatisticsFreeCoolRunHr=_LgpEnvStatisticsFreeCoolRunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,16),_LgpEnvStatisticsFreeCoolRunHr_Type())
lgpEnvStatisticsFreeCoolRunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsFreeCoolRunHr.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvStatisticsFreeCoolRunHr.setUnits(_E)
_LgpEnvStatisticsComp3RunHr_Type=Unsigned32
_LgpEnvStatisticsComp3RunHr_Object=MibScalar
lgpEnvStatisticsComp3RunHr=_LgpEnvStatisticsComp3RunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,17),_LgpEnvStatisticsComp3RunHr_Type())
lgpEnvStatisticsComp3RunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsComp3RunHr.setStatus(_A)
_LgpEnvStatisticsComp4RunHr_Type=Unsigned32
_LgpEnvStatisticsComp4RunHr_Object=MibScalar
lgpEnvStatisticsComp4RunHr=_LgpEnvStatisticsComp4RunHr_Object((1,3,6,1,4,1,476,1,42,3,4,6,18),_LgpEnvStatisticsComp4RunHr_Type())
lgpEnvStatisticsComp4RunHr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvStatisticsComp4RunHr.setStatus(_A)
_LgpEnvPoints_ObjectIdentity=ObjectIdentity
lgpEnvPoints=_LgpEnvPoints_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7))
if mibBuilder.loadTexts:lgpEnvPoints.setStatus(_A)
_LgpEnvWellKnownPoints_ObjectIdentity=ObjectIdentity
lgpEnvWellKnownPoints=_LgpEnvWellKnownPoints_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1))
if mibBuilder.loadTexts:lgpEnvWellKnownPoints.setStatus(_A)
_LgpEnvFanPoint_ObjectIdentity=ObjectIdentity
lgpEnvFanPoint=_LgpEnvFanPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,1))
if mibBuilder.loadTexts:lgpEnvFanPoint.setStatus(_A)
_LgpEnvCompressorPoint_ObjectIdentity=ObjectIdentity
lgpEnvCompressorPoint=_LgpEnvCompressorPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,2))
if mibBuilder.loadTexts:lgpEnvCompressorPoint.setStatus(_A)
_LgpEnvElectricHeaterPoint_ObjectIdentity=ObjectIdentity
lgpEnvElectricHeaterPoint=_LgpEnvElectricHeaterPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,3))
if mibBuilder.loadTexts:lgpEnvElectricHeaterPoint.setStatus(_A)
_LgpEnvChilledWaterPoint_ObjectIdentity=ObjectIdentity
lgpEnvChilledWaterPoint=_LgpEnvChilledWaterPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,4))
if mibBuilder.loadTexts:lgpEnvChilledWaterPoint.setStatus(_A)
_LgpEnvHumidifierPoint_ObjectIdentity=ObjectIdentity
lgpEnvHumidifierPoint=_LgpEnvHumidifierPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,5))
if mibBuilder.loadTexts:lgpEnvHumidifierPoint.setStatus(_A)
_LgpEnvDehumidifierPoint_ObjectIdentity=ObjectIdentity
lgpEnvDehumidifierPoint=_LgpEnvDehumidifierPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,6))
if mibBuilder.loadTexts:lgpEnvDehumidifierPoint.setStatus(_A)
_LgpEnvFreeCoolingPoint_ObjectIdentity=ObjectIdentity
lgpEnvFreeCoolingPoint=_LgpEnvFreeCoolingPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,7))
if mibBuilder.loadTexts:lgpEnvFreeCoolingPoint.setStatus(_A)
_LgpEnvHotWaterPoint_ObjectIdentity=ObjectIdentity
lgpEnvHotWaterPoint=_LgpEnvHotWaterPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,8))
if mibBuilder.loadTexts:lgpEnvHotWaterPoint.setStatus(_A)
_LgpEnvHotGasPoint_ObjectIdentity=ObjectIdentity
lgpEnvHotGasPoint=_LgpEnvHotGasPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,9))
if mibBuilder.loadTexts:lgpEnvHotGasPoint.setStatus(_A)
_LgpEnvBatteryCabinetPoint_ObjectIdentity=ObjectIdentity
lgpEnvBatteryCabinetPoint=_LgpEnvBatteryCabinetPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,10))
if mibBuilder.loadTexts:lgpEnvBatteryCabinetPoint.setStatus(_A)
_LgpEnvPumpPoints_ObjectIdentity=ObjectIdentity
lgpEnvPumpPoints=_LgpEnvPumpPoints_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,11))
if mibBuilder.loadTexts:lgpEnvPumpPoints.setStatus(_A)
_LgpEnvPump1Point_ObjectIdentity=ObjectIdentity
lgpEnvPump1Point=_LgpEnvPump1Point_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,11,1))
if mibBuilder.loadTexts:lgpEnvPump1Point.setStatus(_A)
_LgpEnvPump2Point_ObjectIdentity=ObjectIdentity
lgpEnvPump2Point=_LgpEnvPump2Point_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,11,2))
if mibBuilder.loadTexts:lgpEnvPump2Point.setStatus(_A)
_LgpEnvCompressorPoints_ObjectIdentity=ObjectIdentity
lgpEnvCompressorPoints=_LgpEnvCompressorPoints_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,12))
if mibBuilder.loadTexts:lgpEnvCompressorPoints.setStatus(_A)
_LgpEnvCompressor1Point_ObjectIdentity=ObjectIdentity
lgpEnvCompressor1Point=_LgpEnvCompressor1Point_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,12,1))
if mibBuilder.loadTexts:lgpEnvCompressor1Point.setStatus(_A)
_LgpEnvCompressor1APoint_ObjectIdentity=ObjectIdentity
lgpEnvCompressor1APoint=_LgpEnvCompressor1APoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,12,1,1))
if mibBuilder.loadTexts:lgpEnvCompressor1APoint.setStatus(_A)
_LgpEnvCompressor1BPoint_ObjectIdentity=ObjectIdentity
lgpEnvCompressor1BPoint=_LgpEnvCompressor1BPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,12,1,2))
if mibBuilder.loadTexts:lgpEnvCompressor1BPoint.setStatus(_A)
_LgpEnvCompressor2Point_ObjectIdentity=ObjectIdentity
lgpEnvCompressor2Point=_LgpEnvCompressor2Point_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,12,2))
if mibBuilder.loadTexts:lgpEnvCompressor2Point.setStatus(_A)
_LgpEnvCompressor2APoint_ObjectIdentity=ObjectIdentity
lgpEnvCompressor2APoint=_LgpEnvCompressor2APoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,12,2,1))
if mibBuilder.loadTexts:lgpEnvCompressor2APoint.setStatus(_A)
_LgpEnvCompressor2BPoint_ObjectIdentity=ObjectIdentity
lgpEnvCompressor2BPoint=_LgpEnvCompressor2BPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,12,2,2))
if mibBuilder.loadTexts:lgpEnvCompressor2BPoint.setStatus(_A)
_LgpEnvValvePoints_ObjectIdentity=ObjectIdentity
lgpEnvValvePoints=_LgpEnvValvePoints_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,13))
if mibBuilder.loadTexts:lgpEnvValvePoints.setStatus(_A)
_LgpEnvHotGasValve1Point_ObjectIdentity=ObjectIdentity
lgpEnvHotGasValve1Point=_LgpEnvHotGasValve1Point_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,13,1))
if mibBuilder.loadTexts:lgpEnvHotGasValve1Point.setStatus(_A)
_LgpEnvHotGasValve2Point_ObjectIdentity=ObjectIdentity
lgpEnvHotGasValve2Point=_LgpEnvHotGasValve2Point_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,13,2))
if mibBuilder.loadTexts:lgpEnvHotGasValve2Point.setStatus(_A)
_LgpEnvRemoteSensorStatisticPoints_ObjectIdentity=ObjectIdentity
lgpEnvRemoteSensorStatisticPoints=_LgpEnvRemoteSensorStatisticPoints_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,14))
if mibBuilder.loadTexts:lgpEnvRemoteSensorStatisticPoints.setStatus(_A)
_LgpEnvRemoteSensorMinimumPoint_ObjectIdentity=ObjectIdentity
lgpEnvRemoteSensorMinimumPoint=_LgpEnvRemoteSensorMinimumPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,14,1))
if mibBuilder.loadTexts:lgpEnvRemoteSensorMinimumPoint.setStatus(_A)
_LgpEnvRemoteSensorMaximumPoint_ObjectIdentity=ObjectIdentity
lgpEnvRemoteSensorMaximumPoint=_LgpEnvRemoteSensorMaximumPoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,14,2))
if mibBuilder.loadTexts:lgpEnvRemoteSensorMaximumPoint.setStatus(_A)
_LgpEnvRemoteSensorAveragePoint_ObjectIdentity=ObjectIdentity
lgpEnvRemoteSensorAveragePoint=_LgpEnvRemoteSensorAveragePoint_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,7,1,14,3))
if mibBuilder.loadTexts:lgpEnvRemoteSensorAveragePoint.setStatus(_A)
_LgpEnvUnits_ObjectIdentity=ObjectIdentity
lgpEnvUnits=_LgpEnvUnits_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,8))
if mibBuilder.loadTexts:lgpEnvUnits.setStatus(_A)
_LgpEnvWellKnownUnits_ObjectIdentity=ObjectIdentity
lgpEnvWellKnownUnits=_LgpEnvWellKnownUnits_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,8,1))
if mibBuilder.loadTexts:lgpEnvWellKnownUnits.setStatus(_A)
_LgpEnvHours_ObjectIdentity=ObjectIdentity
lgpEnvHours=_LgpEnvHours_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,8,1,1))
if mibBuilder.loadTexts:lgpEnvHours.setStatus(_A)
_LgpEnvRemoteSensors_ObjectIdentity=ObjectIdentity
lgpEnvRemoteSensors=_LgpEnvRemoteSensors_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,4,9))
if mibBuilder.loadTexts:lgpEnvRemoteSensors.setStatus(_A)
class _LgpEnvRemoteSensorCalc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('average',1),('maximum',2)))
_LgpEnvRemoteSensorCalc_Type.__name__=_D
_LgpEnvRemoteSensorCalc_Object=MibScalar
lgpEnvRemoteSensorCalc=_LgpEnvRemoteSensorCalc_Object((1,3,6,1,4,1,476,1,42,3,4,9,1),_LgpEnvRemoteSensorCalc_Type())
lgpEnvRemoteSensorCalc.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvRemoteSensorCalc.setStatus(_A)
_LgpEnvRemoteSensorTable_Object=MibTable
lgpEnvRemoteSensorTable=_LgpEnvRemoteSensorTable_Object((1,3,6,1,4,1,476,1,42,3,4,9,10))
if mibBuilder.loadTexts:lgpEnvRemoteSensorTable.setStatus(_A)
_LgpEnvRemoteSensorEntry_Object=MibTableRow
lgpEnvRemoteSensorEntry=_LgpEnvRemoteSensorEntry_Object((1,3,6,1,4,1,476,1,42,3,4,9,10,1))
lgpEnvRemoteSensorEntry.setIndexNames((0,_L,_l))
if mibBuilder.loadTexts:lgpEnvRemoteSensorEntry.setStatus(_A)
_LgpEnvRemoteSensorIndex_Type=Unsigned32
_LgpEnvRemoteSensorIndex_Object=MibTableColumn
lgpEnvRemoteSensorIndex=_LgpEnvRemoteSensorIndex_Object((1,3,6,1,4,1,476,1,42,3,4,9,10,1,1),_LgpEnvRemoteSensorIndex_Type())
lgpEnvRemoteSensorIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:lgpEnvRemoteSensorIndex.setStatus(_A)
_LgpEnvRemoteSensorId_Type=Unsigned32
_LgpEnvRemoteSensorId_Object=MibTableColumn
lgpEnvRemoteSensorId=_LgpEnvRemoteSensorId_Object((1,3,6,1,4,1,476,1,42,3,4,9,10,1,2),_LgpEnvRemoteSensorId_Type())
lgpEnvRemoteSensorId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvRemoteSensorId.setStatus(_A)
class _LgpEnvRemoteSensorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disable',0),('reference',1),('control',2)))
_LgpEnvRemoteSensorMode_Type.__name__=_D
_LgpEnvRemoteSensorMode_Object=MibTableColumn
lgpEnvRemoteSensorMode=_LgpEnvRemoteSensorMode_Object((1,3,6,1,4,1,476,1,42,3,4,9,10,1,3),_LgpEnvRemoteSensorMode_Type())
lgpEnvRemoteSensorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvRemoteSensorMode.setStatus(_A)
_LgpEnvRemoteSensorUsrLabel_Type=DisplayString
_LgpEnvRemoteSensorUsrLabel_Object=MibTableColumn
lgpEnvRemoteSensorUsrLabel=_LgpEnvRemoteSensorUsrLabel_Object((1,3,6,1,4,1,476,1,42,3,4,9,10,1,4),_LgpEnvRemoteSensorUsrLabel_Type())
lgpEnvRemoteSensorUsrLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpEnvRemoteSensorUsrLabel.setStatus(_A)
_LgpEnvRemoteSensorTempMeasurementDegF_Type=Integer32
_LgpEnvRemoteSensorTempMeasurementDegF_Object=MibTableColumn
lgpEnvRemoteSensorTempMeasurementDegF=_LgpEnvRemoteSensorTempMeasurementDegF_Object((1,3,6,1,4,1,476,1,42,3,4,9,10,1,5),_LgpEnvRemoteSensorTempMeasurementDegF_Type())
lgpEnvRemoteSensorTempMeasurementDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvRemoteSensorTempMeasurementDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvRemoteSensorTempMeasurementDegF.setUnits(_H)
_LgpEnvRemoteSensorTempMeasurementDegC_Type=Integer32
_LgpEnvRemoteSensorTempMeasurementDegC_Object=MibTableColumn
lgpEnvRemoteSensorTempMeasurementDegC=_LgpEnvRemoteSensorTempMeasurementDegC_Object((1,3,6,1,4,1,476,1,42,3,4,9,10,1,6),_LgpEnvRemoteSensorTempMeasurementDegC_Type())
lgpEnvRemoteSensorTempMeasurementDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpEnvRemoteSensorTempMeasurementDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpEnvRemoteSensorTempMeasurementDegC.setUnits(_I)
mibBuilder.exportSymbols(_L,**{'liebertGlobalProductsEnvironmentalModule':liebertGlobalProductsEnvironmentalModule,'lgpEnvTemperature':lgpEnvTemperature,'lgpEnvTemperatureWellKnown':lgpEnvTemperatureWellKnown,'lgpEnvControlTemperature':lgpEnvControlTemperature,'lgpEnvReturnAirTemperature':lgpEnvReturnAirTemperature,'lgpEnvSupplyAirTemperature':lgpEnvSupplyAirTemperature,'lgpAmbientTemperature':lgpAmbientTemperature,'lgpInverterTemperature':lgpInverterTemperature,'lgpBatteryTempterature':lgpBatteryTempterature,'lgpAcDcConverterTemperature':lgpAcDcConverterTemperature,'lgpPfcTemperature':lgpPfcTemperature,'lgpTransformerTemperature':lgpTransformerTemperature,'lgpLocalTemperature':lgpLocalTemperature,'lgpLocal1Temperature':lgpLocal1Temperature,'lgpLocal2Temperature':lgpLocal2Temperature,'lgpLocal3Temperature':lgpLocal3Temperature,'lgpDigitalScrollCompressorTemperature':lgpDigitalScrollCompressorTemperature,'lgpDigitalScrollCompressor1Temperature':lgpDigitalScrollCompressor1Temperature,'lgpDigitalScrollCompressor2Temperature':lgpDigitalScrollCompressor2Temperature,'lgpChillWaterTemperature':lgpChillWaterTemperature,'lgpCoolantTemperature':lgpCoolantTemperature,'lgpEnvEnclosureTemperatureSensors':lgpEnvEnclosureTemperatureSensors,'lgpEnvEnclosureTemperatureSensor1':lgpEnvEnclosureTemperatureSensor1,'lgpEnvEnclosureTemperatureSensor2':lgpEnvEnclosureTemperatureSensor2,'lgpEnvEnclosureTemperatureSensor3':lgpEnvEnclosureTemperatureSensor3,'lgpEnvEnclosureTemperatureSensor4':lgpEnvEnclosureTemperatureSensor4,'lgpEnvValueAmbientRoomTemperature':lgpEnvValueAmbientRoomTemperature,'lgpEnvDewPointTemperature':lgpEnvDewPointTemperature,'lgpEnvEnclosureTemperature':lgpEnvEnclosureTemperature,'lgpEnvAdjustedTemperature':lgpEnvAdjustedTemperature,'lgpEnvExternalSensors':lgpEnvExternalSensors,'lgpEnvExternalAirSensorA':lgpEnvExternalAirSensorA,'lgpEnvExternalAirSensorADewPoint':lgpEnvExternalAirSensorADewPoint,'lgpEnvExternalAirSensorB':lgpEnvExternalAirSensorB,'lgpEnvExternalAirSensorBDewPoint':lgpEnvExternalAirSensorBDewPoint,'lgpEnvSupplyFluidTemperature':lgpEnvSupplyFluidTemperature,'lgpEnvSupplyRefrigerantTemperature':lgpEnvSupplyRefrigerantTemperature,'lgpEnvMinDesiredRoomAirTemperature':lgpEnvMinDesiredRoomAirTemperature,'lgpEnvDewPointTemperatures':lgpEnvDewPointTemperatures,'lgpEnvInletDewPointTemperature':lgpEnvInletDewPointTemperature,'lgpEnvReturnFluidTemperature':lgpEnvReturnFluidTemperature,'lgpEnvTemperatureFahrenheit':lgpEnvTemperatureFahrenheit,'lgpEnvTemperatureSettingDegF':lgpEnvTemperatureSettingDegF,'lgpEnvTemperatureToleranceDegF':lgpEnvTemperatureToleranceDegF,'lgpEnvTemperatureTableDegF':lgpEnvTemperatureTableDegF,'lgpEnvTemperatureEntryDegF':lgpEnvTemperatureEntryDegF,_X:lgpEnvTemperatureIdDegF,'lgpEnvTemperatureDescrDegF':lgpEnvTemperatureDescrDegF,'lgpEnvTemperatureMeasurementDegF':lgpEnvTemperatureMeasurementDegF,'lgpEnvTemperatureHighThresholdDegF':lgpEnvTemperatureHighThresholdDegF,'lgpEnvTemperatureLowThresholdDegF':lgpEnvTemperatureLowThresholdDegF,'lgpEnvTemperatureSetPointDegF':lgpEnvTemperatureSetPointDegF,'lgpEnvTemperatureDailyHighDegF':lgpEnvTemperatureDailyHighDegF,'lgpEnvTemperatureDailyLowDegF':lgpEnvTemperatureDailyLowDegF,'lgpEnvTempDailyHighTimeHourDegF':lgpEnvTempDailyHighTimeHourDegF,'lgpEnvTempDailyHighTimeMinuteDegF':lgpEnvTempDailyHighTimeMinuteDegF,'lgpEnvTempDailyHighTimeSecondDegF':lgpEnvTempDailyHighTimeSecondDegF,'lgpEnvTempDailyLowTimeHourDegF':lgpEnvTempDailyLowTimeHourDegF,'lgpEnvTempDailyLowTimeMinuteDegF':lgpEnvTempDailyLowTimeMinuteDegF,'lgpEnvTempDailyLowTimeSecondDegF':lgpEnvTempDailyLowTimeSecondDegF,'lgpEnvTemperatureMeasurementTenthsDegF':lgpEnvTemperatureMeasurementTenthsDegF,'lgpEnvTemperatureHighThresholdTenthsDegF':lgpEnvTemperatureHighThresholdTenthsDegF,'lgpEnvTemperatureLowThresholdTenthsDegF':lgpEnvTemperatureLowThresholdTenthsDegF,'lgpEnvTemperatureSetPointTenthsDegF':lgpEnvTemperatureSetPointTenthsDegF,'lgpEnvTemperatureDeadBandTenthsDegF':lgpEnvTemperatureDeadBandTenthsDegF,'lgpEnvTempHeatingPropBandTenthsDegF':lgpEnvTempHeatingPropBandTenthsDegF,'lgpEnvTempCoolingPropBandTenthsDegF':lgpEnvTempCoolingPropBandTenthsDegF,'lgpEnvTemperatureDeadbandRangeDegF':lgpEnvTemperatureDeadbandRangeDegF,'lgpEnvTemperatureCelsius':lgpEnvTemperatureCelsius,'lgpEnvTemperatureSettingDegC':lgpEnvTemperatureSettingDegC,'lgpEnvTemperatureToleranceDegC':lgpEnvTemperatureToleranceDegC,'lgpEnvTemperatureTableDegC':lgpEnvTemperatureTableDegC,'lgpEnvTemperatureEntryDegC':lgpEnvTemperatureEntryDegC,_Y:lgpEnvTemperatureIdDegC,'lgpEnvTemperatureDescrDegC':lgpEnvTemperatureDescrDegC,'lgpEnvTemperatureMeasurementDegC':lgpEnvTemperatureMeasurementDegC,'lgpEnvTemperatureHighThresholdDegC':lgpEnvTemperatureHighThresholdDegC,'lgpEnvTemperatureLowThresholdDegC':lgpEnvTemperatureLowThresholdDegC,'lgpEnvTemperatureSetPointDegC':lgpEnvTemperatureSetPointDegC,'lgpEnvTemperatureDailyHighDegC':lgpEnvTemperatureDailyHighDegC,'lgpEnvTemperatureDailyLowDegC':lgpEnvTemperatureDailyLowDegC,'lgpEnvTempDailyHighTimeHourDegC':lgpEnvTempDailyHighTimeHourDegC,'lgpEnvTempDailyHighTimeMinuteDegC':lgpEnvTempDailyHighTimeMinuteDegC,'lgpEnvTempDailyHighTimeSecondDegC':lgpEnvTempDailyHighTimeSecondDegC,'lgpEnvTempDailyLowTimeHourDegC':lgpEnvTempDailyLowTimeHourDegC,'lgpEnvTempDailyLowTimeMinuteDegC':lgpEnvTempDailyLowTimeMinuteDegC,'lgpEnvTempDailyLowTimeSecondDegC':lgpEnvTempDailyLowTimeSecondDegC,'lgpEnvTemperatureMeasurementTenthsDegC':lgpEnvTemperatureMeasurementTenthsDegC,'lgpEnvTemperatureHighThresholdTenthsDegC':lgpEnvTemperatureHighThresholdTenthsDegC,'lgpEnvTemperatureLowThresholdTenthsDegC':lgpEnvTemperatureLowThresholdTenthsDegC,'lgpEnvTemperatureSetPointTenthsDegC':lgpEnvTemperatureSetPointTenthsDegC,'lgpEnvTemperatureDeadBandTenthsDegC':lgpEnvTemperatureDeadBandTenthsDegC,'lgpEnvTempHeatingPropBandTenthsDegC':lgpEnvTempHeatingPropBandTenthsDegC,'lgpEnvTempCoolingPropBandTenthsDegC':lgpEnvTempCoolingPropBandTenthsDegC,'lgpEnvTemperatureDeadbandRangeDegC':lgpEnvTemperatureDeadbandRangeDegC,'lgpEnvTemperatureControlMode':lgpEnvTemperatureControlMode,'lgpEnvHumidity':lgpEnvHumidity,'lgpEnvHumidityWellKnown':lgpEnvHumidityWellKnown,'lgpEnvControlHumidity':lgpEnvControlHumidity,'lgpEnvReturnAirHumidity':lgpEnvReturnAirHumidity,'lgpEnvSupplyAirHumidity':lgpEnvSupplyAirHumidity,'lgpEnvValueAmbientHumidity':lgpEnvValueAmbientHumidity,'lgpEnvHumidityRelative':lgpEnvHumidityRelative,'lgpEnvHumiditySettingRel':lgpEnvHumiditySettingRel,'lgpEnvHumidityToleranceRel':lgpEnvHumidityToleranceRel,'lgpEnvHumidityTableRel':lgpEnvHumidityTableRel,'lgpEnvHumidityEntryRel':lgpEnvHumidityEntryRel,_Z:lgpEnvHumidityIdRel,'lgpEnvHumidityDescrRel':lgpEnvHumidityDescrRel,'lgpEnvHumidityMeasurementRel':lgpEnvHumidityMeasurementRel,'lgpEnvHumidityHighThresholdRel':lgpEnvHumidityHighThresholdRel,'lgpEnvHumidityLowThresholdRel':lgpEnvHumidityLowThresholdRel,'lgpEnvHumiditySetPoint':lgpEnvHumiditySetPoint,'lgpEnvHumidityDailyHigh':lgpEnvHumidityDailyHigh,'lgpEnvHumidityDailyLow':lgpEnvHumidityDailyLow,'lgpEnvHumidityDailyHighTimeHour':lgpEnvHumidityDailyHighTimeHour,'lgpEnvHumidityDailyHighTimeMinute':lgpEnvHumidityDailyHighTimeMinute,'lgpEnvHumidityDailyHighTimeSecond':lgpEnvHumidityDailyHighTimeSecond,'lgpEnvHumidityDailyLowTimeHour':lgpEnvHumidityDailyLowTimeHour,'lgpEnvHumidityDailyLowTimeMinute':lgpEnvHumidityDailyLowTimeMinute,'lgpEnvHumidityDailyLowTimeSecond':lgpEnvHumidityDailyLowTimeSecond,'lgpEnvHumidityDeadBand':lgpEnvHumidityDeadBand,'lgpEnvHumidifyPropBand':lgpEnvHumidifyPropBand,'lgpEnvDehumidifyPropBand':lgpEnvDehumidifyPropBand,'lgpEnvHumidityMeasurementRelTenths':lgpEnvHumidityMeasurementRelTenths,'lgpEnvHumidityHighThresholdRelTenths':lgpEnvHumidityHighThresholdRelTenths,'lgpEnvHumidityLowThresholdRelTenths':lgpEnvHumidityLowThresholdRelTenths,'lgpEnvHumidityDeadbandRange':lgpEnvHumidityDeadbandRange,'lgpEnvState':lgpEnvState,'lgpEnvStateSystem':lgpEnvStateSystem,'lgpEnvStateCooling':lgpEnvStateCooling,'lgpEnvStateHeating':lgpEnvStateHeating,'lgpEnvStateHumidifying':lgpEnvStateHumidifying,'lgpEnvStateDehumidifying':lgpEnvStateDehumidifying,'lgpEnvStateEconoCycle':lgpEnvStateEconoCycle,'lgpEnvStateFan':lgpEnvStateFan,'lgpEnvStateGeneralAlarmOutput':lgpEnvStateGeneralAlarmOutput,'lgpEnvStateCoolingCapacity':lgpEnvStateCoolingCapacity,'lgpEnvStateHeatingCapacity':lgpEnvStateHeatingCapacity,'lgpEnvStateAudibleAlarm':lgpEnvStateAudibleAlarm,'lgpEnvStateCoolingUnits':lgpEnvStateCoolingUnits,'lgpEnvStateCoolingUnit1':lgpEnvStateCoolingUnit1,'lgpEnvStateCoolingUnit2':lgpEnvStateCoolingUnit2,'lgpEnvStateCoolingUnit3':lgpEnvStateCoolingUnit3,'lgpEnvStateCoolingUnit4':lgpEnvStateCoolingUnit4,'lgpEnvStateHeatingUnits':lgpEnvStateHeatingUnits,'lgpEnvStateHeatingUnit1':lgpEnvStateHeatingUnit1,'lgpEnvStateHeatingUnit2':lgpEnvStateHeatingUnit2,'lgpEnvStateHeatingUnit3':lgpEnvStateHeatingUnit3,'lgpEnvStateHeatingUnit4':lgpEnvStateHeatingUnit4,'lgpEnvStateOperatingReason':lgpEnvStateOperatingReason,'lgpEnvStateOperatingMode':lgpEnvStateOperatingMode,'lgpEnvStateFanCapacity':lgpEnvStateFanCapacity,'lgpEnvStateFreeCoolingCapacity':lgpEnvStateFreeCoolingCapacity,'lgpEnvStateDehumidifyingCapacity':lgpEnvStateDehumidifyingCapacity,'lgpEnvStateHumidifyingCapacity':lgpEnvStateHumidifyingCapacity,'lgpEnvStateFreeCooling':lgpEnvStateFreeCooling,'lgpEnvStateElectricHeater':lgpEnvStateElectricHeater,'lgpEnvStateHotWater':lgpEnvStateHotWater,'lgpEnvStateOperatingEfficiency':lgpEnvStateOperatingEfficiency,'lgpEnvComponentStateTable':lgpEnvComponentStateTable,'lgpEnvComponentStateEntry':lgpEnvComponentStateEntry,_b:lgpEnvComponentStateIndex,'lgpEnvComponentStateDescr':lgpEnvComponentStateDescr,'lgpEnvComponentState':lgpEnvComponentState,'lgpEnvValveTable':lgpEnvValveTable,'lgpEnvValveEntry':lgpEnvValveEntry,_d:lgpEnvValveIndex,'lgpEnvValveDescr':lgpEnvValveDescr,'lgpEnvValveState':lgpEnvValveState,'lgpEnvValvePositionTenths':lgpEnvValvePositionTenths,'lgpEnvConfig':lgpEnvConfig,'lgpEnvConfigReheatLockout':lgpEnvConfigReheatLockout,'lgpEnvConfigHumLockout':lgpEnvConfigHumLockout,'lgpEnvConfigRestartDelay':lgpEnvConfigRestartDelay,'lgpEnvConfigRemoteShutdown':lgpEnvConfigRemoteShutdown,'lgpEnvConfigCoolingServiceInterval':lgpEnvConfigCoolingServiceInterval,'lgpEnvConfigHumidifierServiceInterval':lgpEnvConfigHumidifierServiceInterval,'lgpEnvConfigFilterServiceInterval':lgpEnvConfigFilterServiceInterval,'lgpEnvConfigSleepModeDeadbandRangeDegC':lgpEnvConfigSleepModeDeadbandRangeDegC,'lgpEnvConfigSleepModeDeadbandRangeDegF':lgpEnvConfigSleepModeDeadbandRangeDegF,'lgpEnvConfigSupplyTempLowLimitDegF':lgpEnvConfigSupplyTempLowLimitDegF,'lgpEnvConfigSupplyTempLowLimitDegC':lgpEnvConfigSupplyTempLowLimitDegC,'lgpEnvConfigTemperatureIntegTime':lgpEnvConfigTemperatureIntegTime,'lgpEnvConfigLocalTemperatureUnit':lgpEnvConfigLocalTemperatureUnit,'lgpEnvConfigSleepMode':lgpEnvConfigSleepMode,'lgpEnvConfigHumidityIntegTime':lgpEnvConfigHumidityIntegTime,'lgpEnvConfigFreecoolingDeltaDegF':lgpEnvConfigFreecoolingDeltaDegF,'lgpEnvConfigFreecoolingDeltaDegC':lgpEnvConfigFreecoolingDeltaDegC,'lgpEnvConfigSupplyTempLowLimit':lgpEnvConfigSupplyTempLowLimit,'lgpEnvConfigSensorEventsStandard':lgpEnvConfigSensorEventsStandard,'lgpEnvConfigSensorEvents1':lgpEnvConfigSensorEvents1,'lgpEnvConfigSleepModeDeadbandRange':lgpEnvConfigSleepModeDeadbandRange,'lgpEnvConfigAutoConfiguration':lgpEnvConfigAutoConfiguration,'lgpEnvConfigDeltaGlycolType':lgpEnvConfigDeltaGlycolType,'lgpEnvConfigChillWaterControl':lgpEnvConfigChillWaterControl,'lgpEnvConfigInfaredFlushRate':lgpEnvConfigInfaredFlushRate,'lgpEnvConfigHumidityControl':lgpEnvConfigHumidityControl,'lgpEnvConfigCompressorLockout':lgpEnvConfigCompressorLockout,'lgpEnvConfigReheatAndHumidifierLockout':lgpEnvConfigReheatAndHumidifierLockout,'lgpEnvOperationalTimeTable':lgpEnvOperationalTimeTable,'lgpEnvOperationalTimeEntry':lgpEnvOperationalTimeEntry,_e:lgpEnvOperationTimeIndex,'lgpEnvOperationTimePoint':lgpEnvOperationTimePoint,'lgpEnvOperationTimeSubID':lgpEnvOperationTimeSubID,'lgpEnvOperationTimeUnit':lgpEnvOperationTimeUnit,'lgpEnvOperationTimeValue':lgpEnvOperationTimeValue,'lgpEnvOperationTimeHighWarning':lgpEnvOperationTimeHighWarning,'lgpEnvConfigTempControlAlgorithm':lgpEnvConfigTempControlAlgorithm,'lgpEnvConfigFanSpeedMode':lgpEnvConfigFanSpeedMode,'lgpEnvConfigFanSpeedCapacity':lgpEnvConfigFanSpeedCapacity,'lgpEnvConfigBmsResetTimer':lgpEnvConfigBmsResetTimer,'lgpEnvConfigDisableSensorOffsetDegC':lgpEnvConfigDisableSensorOffsetDegC,'lgpEnvConfigDisableSensorOffsetDegF':lgpEnvConfigDisableSensorOffsetDegF,'lgpEnvConfigCabinetSensorAlarms':lgpEnvConfigCabinetSensorAlarms,'lgpEnvConfigAirTemperatureControlSensor':lgpEnvConfigAirTemperatureControlSensor,'lgpEnvConfigFanSpeedControlSensor':lgpEnvConfigFanSpeedControlSensor,'lgpEnvConfigMinFanSpeed':lgpEnvConfigMinFanSpeed,'lgpEnvConfigMaxFanSpeed':lgpEnvConfigMaxFanSpeed,'lgpEnvConfigFanSpeedPropBandDegC':lgpEnvConfigFanSpeedPropBandDegC,'lgpEnvConfigFanSpeedPropBandDegF':lgpEnvConfigFanSpeedPropBandDegF,'lgpEnvControl':lgpEnvControl,'lgpEnvControlShutdownAfterDelay':lgpEnvControlShutdownAfterDelay,'lgpEnvControlStartupAfterDelay':lgpEnvControlStartupAfterDelay,'lgpEnvSleepIntervalTimeTable':lgpEnvSleepIntervalTimeTable,'lgpEnvSleepIntervalTimeEntry':lgpEnvSleepIntervalTimeEntry,_i:lgpEnvSleepTimeIndex,'lgpEnvSleepTimeSubID':lgpEnvSleepTimeSubID,'lgpEnvSleepTimeStartHour':lgpEnvSleepTimeStartHour,'lgpEnvSleepTimeStartMinute':lgpEnvSleepTimeStartMinute,'lgpEnvSleepTimeStopHour':lgpEnvSleepTimeStopHour,'lgpEnvSleepTimeStopMinute':lgpEnvSleepTimeStopMinute,'lgpEnvSleepDayTable':lgpEnvSleepDayTable,'lgpEnvSleepDayEntry':lgpEnvSleepDayEntry,_k:lgpEnvSleepDayIndex,'lgpEnvSleepDay':lgpEnvSleepDay,'lgpEnvSleepAllDayEnabled':lgpEnvSleepAllDayEnabled,'lgpEnvStatistics':lgpEnvStatistics,'lgpEnvStatisticsComp1RunHr':lgpEnvStatisticsComp1RunHr,'lgpEnvStatisticsComp2RunHr':lgpEnvStatisticsComp2RunHr,'lgpEnvStatisticsFanRunHr':lgpEnvStatisticsFanRunHr,'lgpEnvStatisticsHumRunHr':lgpEnvStatisticsHumRunHr,'lgpEnvStatisticsReheat1RunHr':lgpEnvStatisticsReheat1RunHr,'lgpEnvStatisticsReheat2RunHr':lgpEnvStatisticsReheat2RunHr,'lgpEnvStatisticsReheat3RunHr':lgpEnvStatisticsReheat3RunHr,'lgpEnvStatisticsCoolingModeHrs':lgpEnvStatisticsCoolingModeHrs,'lgpEnvStatisticsHeatingModeHrs':lgpEnvStatisticsHeatingModeHrs,'lgpEnvStatisticsHumidifyModeHrs':lgpEnvStatisticsHumidifyModeHrs,'lgpEnvStatisticsDehumidifyModeHrs':lgpEnvStatisticsDehumidifyModeHrs,'lgpEnvStatisticsHotGasRunHr':lgpEnvStatisticsHotGasRunHr,'lgpEnvStatisticsHotWaterRunHr':lgpEnvStatisticsHotWaterRunHr,'lgpEnvStatisticsFreeCoolRunHr':lgpEnvStatisticsFreeCoolRunHr,'lgpEnvStatisticsComp3RunHr':lgpEnvStatisticsComp3RunHr,'lgpEnvStatisticsComp4RunHr':lgpEnvStatisticsComp4RunHr,'lgpEnvPoints':lgpEnvPoints,'lgpEnvWellKnownPoints':lgpEnvWellKnownPoints,'lgpEnvFanPoint':lgpEnvFanPoint,'lgpEnvCompressorPoint':lgpEnvCompressorPoint,'lgpEnvElectricHeaterPoint':lgpEnvElectricHeaterPoint,'lgpEnvChilledWaterPoint':lgpEnvChilledWaterPoint,'lgpEnvHumidifierPoint':lgpEnvHumidifierPoint,'lgpEnvDehumidifierPoint':lgpEnvDehumidifierPoint,'lgpEnvFreeCoolingPoint':lgpEnvFreeCoolingPoint,'lgpEnvHotWaterPoint':lgpEnvHotWaterPoint,'lgpEnvHotGasPoint':lgpEnvHotGasPoint,'lgpEnvBatteryCabinetPoint':lgpEnvBatteryCabinetPoint,'lgpEnvPumpPoints':lgpEnvPumpPoints,'lgpEnvPump1Point':lgpEnvPump1Point,'lgpEnvPump2Point':lgpEnvPump2Point,'lgpEnvCompressorPoints':lgpEnvCompressorPoints,'lgpEnvCompressor1Point':lgpEnvCompressor1Point,'lgpEnvCompressor1APoint':lgpEnvCompressor1APoint,'lgpEnvCompressor1BPoint':lgpEnvCompressor1BPoint,'lgpEnvCompressor2Point':lgpEnvCompressor2Point,'lgpEnvCompressor2APoint':lgpEnvCompressor2APoint,'lgpEnvCompressor2BPoint':lgpEnvCompressor2BPoint,'lgpEnvValvePoints':lgpEnvValvePoints,'lgpEnvHotGasValve1Point':lgpEnvHotGasValve1Point,'lgpEnvHotGasValve2Point':lgpEnvHotGasValve2Point,'lgpEnvRemoteSensorStatisticPoints':lgpEnvRemoteSensorStatisticPoints,'lgpEnvRemoteSensorMinimumPoint':lgpEnvRemoteSensorMinimumPoint,'lgpEnvRemoteSensorMaximumPoint':lgpEnvRemoteSensorMaximumPoint,'lgpEnvRemoteSensorAveragePoint':lgpEnvRemoteSensorAveragePoint,'lgpEnvUnits':lgpEnvUnits,'lgpEnvWellKnownUnits':lgpEnvWellKnownUnits,'lgpEnvHours':lgpEnvHours,'lgpEnvRemoteSensors':lgpEnvRemoteSensors,'lgpEnvRemoteSensorCalc':lgpEnvRemoteSensorCalc,'lgpEnvRemoteSensorTable':lgpEnvRemoteSensorTable,'lgpEnvRemoteSensorEntry':lgpEnvRemoteSensorEntry,_l:lgpEnvRemoteSensorIndex,'lgpEnvRemoteSensorId':lgpEnvRemoteSensorId,'lgpEnvRemoteSensorMode':lgpEnvRemoteSensorMode,'lgpEnvRemoteSensorUsrLabel':lgpEnvRemoteSensorUsrLabel,'lgpEnvRemoteSensorTempMeasurementDegF':lgpEnvRemoteSensorTempMeasurementDegF,'lgpEnvRemoteSensorTempMeasurementDegC':lgpEnvRemoteSensorTempMeasurementDegC})