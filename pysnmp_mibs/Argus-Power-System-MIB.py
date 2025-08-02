_U='volttenth'
_T='seconds'
_S='upsAlarmId'
_R='percent'
_Q='upsOutputLineIndex'
_P='0.1 RMS Volts'
_O='upsInputLineIndex'
_N='0.1 Amp DC'
_M='PhysAddress'
_L='upsIdentSiteName'
_K='not-accessible'
_J='upsExtraName'
_I='upsExtraStringValue'
_H='upsExtraIntegerValue'
_G='upsExtraIndex'
_F='Integer32'
_E='read-write'
_D='Argus-Power-System-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,_M,'TextualConvention')
argus=ModuleIdentity((1,3,6,1,4,1,7309))
if mibBuilder.loadTexts:argus.setRevisions(('2016-12-09 00:00',))
class DisplayString(OctetString):0
class PhysAddress(OctetString):0
class PositiveInteger(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NonNegativeInteger(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_UpsPower_ObjectIdentity=ObjectIdentity
upsPower=_UpsPower_ObjectIdentity((1,3,6,1,4,1,7309,6))
_UpsDevice_ObjectIdentity=ObjectIdentity
upsDevice=_UpsDevice_ObjectIdentity((1,3,6,1,4,1,7309,6,1))
_UpsIdent_ObjectIdentity=ObjectIdentity
upsIdent=_UpsIdent_ObjectIdentity((1,3,6,1,4,1,7309,6,1,1))
class _UpsIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentManufacturer_Type.__name__=_C
_UpsIdentManufacturer_Object=MibScalar
upsIdentManufacturer=_UpsIdentManufacturer_Object((1,3,6,1,4,1,7309,6,1,1,1),_UpsIdentManufacturer_Type())
upsIdentManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentManufacturer.setStatus(_A)
class _UpsIdentProductCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentProductCode_Type.__name__=_C
_UpsIdentProductCode_Object=MibScalar
upsIdentProductCode=_UpsIdentProductCode_Object((1,3,6,1,4,1,7309,6,1,1,2),_UpsIdentProductCode_Type())
upsIdentProductCode.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentProductCode.setStatus(_A)
class _UpsIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentModel_Type.__name__=_C
_UpsIdentModel_Object=MibScalar
upsIdentModel=_UpsIdentModel_Object((1,3,6,1,4,1,7309,6,1,1,3),_UpsIdentModel_Type())
upsIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentModel.setStatus(_A)
class _UpsIdentUPSSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentUPSSoftwareVersion_Type.__name__=_C
_UpsIdentUPSSoftwareVersion_Object=MibScalar
upsIdentUPSSoftwareVersion=_UpsIdentUPSSoftwareVersion_Object((1,3,6,1,4,1,7309,6,1,1,4),_UpsIdentUPSSoftwareVersion_Type())
upsIdentUPSSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentUPSSoftwareVersion.setStatus(_A)
class _UpsIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentAgentSoftwareVersion_Type.__name__=_C
_UpsIdentAgentSoftwareVersion_Object=MibScalar
upsIdentAgentSoftwareVersion=_UpsIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,7309,6,1,1,5),_UpsIdentAgentSoftwareVersion_Type())
upsIdentAgentSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentAgentSoftwareVersion.setStatus(_A)
class _UpsIdentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentName_Type.__name__=_C
_UpsIdentName_Object=MibScalar
upsIdentName=_UpsIdentName_Object((1,3,6,1,4,1,7309,6,1,1,6),_UpsIdentName_Type())
upsIdentName.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentName.setStatus(_A)
class _UpsIdentAttachedDevices_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentAttachedDevices_Type.__name__=_C
_UpsIdentAttachedDevices_Object=MibScalar
upsIdentAttachedDevices=_UpsIdentAttachedDevices_Object((1,3,6,1,4,1,7309,6,1,1,7),_UpsIdentAttachedDevices_Type())
upsIdentAttachedDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentAttachedDevices.setStatus(_A)
class _UpsIdentSiteName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentSiteName_Type.__name__=_C
_UpsIdentSiteName_Object=MibScalar
upsIdentSiteName=_UpsIdentSiteName_Object((1,3,6,1,4,1,7309,6,1,1,8),_UpsIdentSiteName_Type())
upsIdentSiteName.setMaxAccess(_E)
if mibBuilder.loadTexts:upsIdentSiteName.setStatus(_A)
class _UpsIdentSiteCity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentSiteCity_Type.__name__=_C
_UpsIdentSiteCity_Object=MibScalar
upsIdentSiteCity=_UpsIdentSiteCity_Object((1,3,6,1,4,1,7309,6,1,1,9),_UpsIdentSiteCity_Type())
upsIdentSiteCity.setMaxAccess(_E)
if mibBuilder.loadTexts:upsIdentSiteCity.setStatus(_A)
class _UpsIdentSiteRegion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentSiteRegion_Type.__name__=_C
_UpsIdentSiteRegion_Object=MibScalar
upsIdentSiteRegion=_UpsIdentSiteRegion_Object((1,3,6,1,4,1,7309,6,1,1,10),_UpsIdentSiteRegion_Type())
upsIdentSiteRegion.setMaxAccess(_E)
if mibBuilder.loadTexts:upsIdentSiteRegion.setStatus(_A)
class _UpsIdentSiteCountry_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentSiteCountry_Type.__name__=_C
_UpsIdentSiteCountry_Object=MibScalar
upsIdentSiteCountry=_UpsIdentSiteCountry_Object((1,3,6,1,4,1,7309,6,1,1,11),_UpsIdentSiteCountry_Type())
upsIdentSiteCountry.setMaxAccess(_E)
if mibBuilder.loadTexts:upsIdentSiteCountry.setStatus(_A)
class _UpsIdentContactName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentContactName_Type.__name__=_C
_UpsIdentContactName_Object=MibScalar
upsIdentContactName=_UpsIdentContactName_Object((1,3,6,1,4,1,7309,6,1,1,12),_UpsIdentContactName_Type())
upsIdentContactName.setMaxAccess(_E)
if mibBuilder.loadTexts:upsIdentContactName.setStatus(_A)
class _UpsIdentPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentPhoneNumber_Type.__name__=_C
_UpsIdentPhoneNumber_Object=MibScalar
upsIdentPhoneNumber=_UpsIdentPhoneNumber_Object((1,3,6,1,4,1,7309,6,1,1,13),_UpsIdentPhoneNumber_Type())
upsIdentPhoneNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:upsIdentPhoneNumber.setStatus(_A)
class _UpsIdentDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentDate_Type.__name__=_C
_UpsIdentDate_Object=MibScalar
upsIdentDate=_UpsIdentDate_Object((1,3,6,1,4,1,7309,6,1,1,14),_UpsIdentDate_Type())
upsIdentDate.setMaxAccess(_E)
if mibBuilder.loadTexts:upsIdentDate.setStatus(_A)
class _UpsIdentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsIdentTime_Type.__name__=_C
_UpsIdentTime_Object=MibScalar
upsIdentTime=_UpsIdentTime_Object((1,3,6,1,4,1,7309,6,1,1,15),_UpsIdentTime_Type())
upsIdentTime.setMaxAccess(_E)
if mibBuilder.loadTexts:upsIdentTime.setStatus(_A)
_UpsBattery_ObjectIdentity=ObjectIdentity
upsBattery=_UpsBattery_ObjectIdentity((1,3,6,1,4,1,7309,6,1,2))
class _UpsBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('batteryNormal',2),('batteryLow',3),('batteryDepleted',4)))
_UpsBatteryStatus_Type.__name__=_F
_UpsBatteryStatus_Object=MibScalar
upsBatteryStatus=_UpsBatteryStatus_Object((1,3,6,1,4,1,7309,6,1,2,1),_UpsBatteryStatus_Type())
upsBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryStatus.setStatus(_A)
_UpsMinutesOnBattery_Type=Integer32
_UpsMinutesOnBattery_Object=MibScalar
upsMinutesOnBattery=_UpsMinutesOnBattery_Object((1,3,6,1,4,1,7309,6,1,2,2),_UpsMinutesOnBattery_Type())
upsMinutesOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsMinutesOnBattery.setStatus(_A)
if mibBuilder.loadTexts:upsMinutesOnBattery.setUnits('minutes')
_UpsBatteryVoltage_Type=Integer32
_UpsBatteryVoltage_Object=MibScalar
upsBatteryVoltage=_UpsBatteryVoltage_Object((1,3,6,1,4,1,7309,6,1,2,3),_UpsBatteryVoltage_Type())
upsBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryVoltage.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryVoltage.setUnits('0.1 Volt DC')
_UpsBatteryChargingCurrent_Type=Integer32
_UpsBatteryChargingCurrent_Object=MibScalar
upsBatteryChargingCurrent=_UpsBatteryChargingCurrent_Object((1,3,6,1,4,1,7309,6,1,2,4),_UpsBatteryChargingCurrent_Type())
upsBatteryChargingCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryChargingCurrent.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryChargingCurrent.setUnits(_N)
_UpsBatteryCapacity_Type=Integer32
_UpsBatteryCapacity_Object=MibScalar
upsBatteryCapacity=_UpsBatteryCapacity_Object((1,3,6,1,4,1,7309,6,1,2,5),_UpsBatteryCapacity_Type())
upsBatteryCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryCapacity.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryCapacity.setUnits(_N)
_UpsBatteryTemperature_Type=Integer32
_UpsBatteryTemperature_Object=MibScalar
upsBatteryTemperature=_UpsBatteryTemperature_Object((1,3,6,1,4,1,7309,6,1,2,6),_UpsBatteryTemperature_Type())
upsBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryTemperature.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryTemperature.setUnits('degrees Centigrade')
_UpsBatteryLowWarning_Type=Integer32
_UpsBatteryLowWarning_Object=MibScalar
upsBatteryLowWarning=_UpsBatteryLowWarning_Object((1,3,6,1,4,1,7309,6,1,2,7),_UpsBatteryLowWarning_Type())
upsBatteryLowWarning.setMaxAccess(_E)
if mibBuilder.loadTexts:upsBatteryLowWarning.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryLowWarning.setUnits('percentage')
_UpsInput_ObjectIdentity=ObjectIdentity
upsInput=_UpsInput_ObjectIdentity((1,3,6,1,4,1,7309,6,1,3))
_UpsInputNumLines_Type=Integer32
_UpsInputNumLines_Object=MibScalar
upsInputNumLines=_UpsInputNumLines_Object((1,3,6,1,4,1,7309,6,1,3,1),_UpsInputNumLines_Type())
upsInputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputNumLines.setStatus(_A)
_UpsInputTable_Object=MibTable
upsInputTable=_UpsInputTable_Object((1,3,6,1,4,1,7309,6,1,3,2))
if mibBuilder.loadTexts:upsInputTable.setStatus(_A)
_UpsInputEntry_Object=MibTableRow
upsInputEntry=_UpsInputEntry_Object((1,3,6,1,4,1,7309,6,1,3,2,1))
upsInputEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:upsInputEntry.setStatus(_A)
_UpsInputLineIndex_Type=Integer32
_UpsInputLineIndex_Object=MibTableColumn
upsInputLineIndex=_UpsInputLineIndex_Object((1,3,6,1,4,1,7309,6,1,3,2,1,1),_UpsInputLineIndex_Type())
upsInputLineIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:upsInputLineIndex.setStatus(_A)
_UpsInputFrequency_Type=Integer32
_UpsInputFrequency_Object=MibTableColumn
upsInputFrequency=_UpsInputFrequency_Object((1,3,6,1,4,1,7309,6,1,3,2,1,2),_UpsInputFrequency_Type())
upsInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputFrequency.setStatus(_A)
if mibBuilder.loadTexts:upsInputFrequency.setUnits('Hertz')
_UpsInputVoltage_Type=Integer32
_UpsInputVoltage_Object=MibTableColumn
upsInputVoltage=_UpsInputVoltage_Object((1,3,6,1,4,1,7309,6,1,3,2,1,3),_UpsInputVoltage_Type())
upsInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVoltage.setStatus(_A)
if mibBuilder.loadTexts:upsInputVoltage.setUnits(_P)
_UpsOutput_ObjectIdentity=ObjectIdentity
upsOutput=_UpsOutput_ObjectIdentity((1,3,6,1,4,1,7309,6,1,4))
class _UpsOutputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('standby',1),('line',2),('boost2',3),('boost1',4),('buck1',5),('buck2',6),('inverter',7),('retransfer',8),('transfer',9),('shutdown',10),('bypass',11)))
_UpsOutputSource_Type.__name__=_F
_UpsOutputSource_Object=MibScalar
upsOutputSource=_UpsOutputSource_Object((1,3,6,1,4,1,7309,6,1,4,1),_UpsOutputSource_Type())
upsOutputSource.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputSource.setStatus(_A)
_UpsOutputFrequency_Type=Integer32
_UpsOutputFrequency_Object=MibScalar
upsOutputFrequency=_UpsOutputFrequency_Object((1,3,6,1,4,1,7309,6,1,4,2),_UpsOutputFrequency_Type())
upsOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputFrequency.setStatus(_A)
if mibBuilder.loadTexts:upsOutputFrequency.setUnits('0.1 Hertz')
_UpsOutputNumLines_Type=Integer32
_UpsOutputNumLines_Object=MibScalar
upsOutputNumLines=_UpsOutputNumLines_Object((1,3,6,1,4,1,7309,6,1,4,3),_UpsOutputNumLines_Type())
upsOutputNumLines.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputNumLines.setStatus(_A)
_UpsOutputTable_Object=MibTable
upsOutputTable=_UpsOutputTable_Object((1,3,6,1,4,1,7309,6,1,4,4))
if mibBuilder.loadTexts:upsOutputTable.setStatus(_A)
_UpsOutputEntry_Object=MibTableRow
upsOutputEntry=_UpsOutputEntry_Object((1,3,6,1,4,1,7309,6,1,4,4,1))
upsOutputEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:upsOutputEntry.setStatus(_A)
_UpsOutputLineIndex_Type=Integer32
_UpsOutputLineIndex_Object=MibTableColumn
upsOutputLineIndex=_UpsOutputLineIndex_Object((1,3,6,1,4,1,7309,6,1,4,4,1,1),_UpsOutputLineIndex_Type())
upsOutputLineIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:upsOutputLineIndex.setStatus(_A)
_UpsOutputVoltage_Type=Integer32
_UpsOutputVoltage_Object=MibTableColumn
upsOutputVoltage=_UpsOutputVoltage_Object((1,3,6,1,4,1,7309,6,1,4,4,1,2),_UpsOutputVoltage_Type())
upsOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:upsOutputVoltage.setUnits(_P)
_UpsOutputCurrent_Type=Integer32
_UpsOutputCurrent_Object=MibTableColumn
upsOutputCurrent=_UpsOutputCurrent_Object((1,3,6,1,4,1,7309,6,1,4,4,1,3),_UpsOutputCurrent_Type())
upsOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:upsOutputCurrent.setUnits('0.1 RMS Amp')
_UpsOutputPowerVA_Type=Integer32
_UpsOutputPowerVA_Object=MibTableColumn
upsOutputPowerVA=_UpsOutputPowerVA_Object((1,3,6,1,4,1,7309,6,1,4,4,1,4),_UpsOutputPowerVA_Type())
upsOutputPowerVA.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPowerVA.setStatus(_A)
if mibBuilder.loadTexts:upsOutputPowerVA.setUnits('VA')
_UpsOutputPowerWatt_Type=Integer32
_UpsOutputPowerWatt_Object=MibTableColumn
upsOutputPowerWatt=_UpsOutputPowerWatt_Object((1,3,6,1,4,1,7309,6,1,4,4,1,5),_UpsOutputPowerWatt_Type())
upsOutputPowerWatt.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPowerWatt.setStatus(_A)
if mibBuilder.loadTexts:upsOutputPowerWatt.setUnits('Watts')
_UpsPowerFactor_Type=Integer32
_UpsPowerFactor_Object=MibTableColumn
upsPowerFactor=_UpsPowerFactor_Object((1,3,6,1,4,1,7309,6,1,4,4,1,6),_UpsPowerFactor_Type())
upsPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:upsPowerFactor.setStatus(_A)
if mibBuilder.loadTexts:upsPowerFactor.setUnits(_R)
class _UpsOutputPercentLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_UpsOutputPercentLoad_Type.__name__=_F
_UpsOutputPercentLoad_Object=MibTableColumn
upsOutputPercentLoad=_UpsOutputPercentLoad_Object((1,3,6,1,4,1,7309,6,1,4,4,1,7),_UpsOutputPercentLoad_Type())
upsOutputPercentLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPercentLoad.setStatus(_A)
if mibBuilder.loadTexts:upsOutputPercentLoad.setUnits(_R)
_UpsAlarm_ObjectIdentity=ObjectIdentity
upsAlarm=_UpsAlarm_ObjectIdentity((1,3,6,1,4,1,7309,6,1,5))
_UpsAlarmsPresent_Type=Integer32
_UpsAlarmsPresent_Object=MibScalar
upsAlarmsPresent=_UpsAlarmsPresent_Object((1,3,6,1,4,1,7309,6,1,5,1),_UpsAlarmsPresent_Type())
upsAlarmsPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmsPresent.setStatus(_A)
_UpsAlarmTable_Object=MibTable
upsAlarmTable=_UpsAlarmTable_Object((1,3,6,1,4,1,7309,6,1,5,2))
if mibBuilder.loadTexts:upsAlarmTable.setStatus(_A)
_UpsAlarmEntry_Object=MibTableRow
upsAlarmEntry=_UpsAlarmEntry_Object((1,3,6,1,4,1,7309,6,1,5,2,1))
upsAlarmEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:upsAlarmEntry.setStatus(_A)
_UpsAlarmId_Type=Integer32
_UpsAlarmId_Object=MibTableColumn
upsAlarmId=_UpsAlarmId_Object((1,3,6,1,4,1,7309,6,1,5,2,1,1),_UpsAlarmId_Type())
upsAlarmId.setMaxAccess(_K)
if mibBuilder.loadTexts:upsAlarmId.setStatus(_A)
class _UpsAlarmDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsAlarmDescr_Type.__name__=_C
_UpsAlarmDescr_Object=MibTableColumn
upsAlarmDescr=_UpsAlarmDescr_Object((1,3,6,1,4,1,7309,6,1,5,2,1,2),_UpsAlarmDescr_Type())
upsAlarmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDescr.setStatus(_A)
_UpsAlarmStatus_Type=Integer32
_UpsAlarmStatus_Object=MibTableColumn
upsAlarmStatus=_UpsAlarmStatus_Object((1,3,6,1,4,1,7309,6,1,5,2,1,3),_UpsAlarmStatus_Type())
upsAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmStatus.setStatus(_A)
_UpsConfig_ObjectIdentity=ObjectIdentity
upsConfig=_UpsConfig_ObjectIdentity((1,3,6,1,4,1,7309,6,1,6))
_UpsConfigLineQualifyTime_Type=Integer32
_UpsConfigLineQualifyTime_Object=MibScalar
upsConfigLineQualifyTime=_UpsConfigLineQualifyTime_Object((1,3,6,1,4,1,7309,6,1,6,1),_UpsConfigLineQualifyTime_Type())
upsConfigLineQualifyTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigLineQualifyTime.setStatus(_A)
if mibBuilder.loadTexts:upsConfigLineQualifyTime.setUnits(_T)
_UpsConfigLineOutputVoltageHighLimit_Type=Integer32
_UpsConfigLineOutputVoltageHighLimit_Object=MibScalar
upsConfigLineOutputVoltageHighLimit=_UpsConfigLineOutputVoltageHighLimit_Object((1,3,6,1,4,1,7309,6,1,6,2),_UpsConfigLineOutputVoltageHighLimit_Type())
upsConfigLineOutputVoltageHighLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigLineOutputVoltageHighLimit.setStatus(_A)
if mibBuilder.loadTexts:upsConfigLineOutputVoltageHighLimit.setUnits(_U)
_UpsConfigLineOutputVoltageLowLimit_Type=Integer32
_UpsConfigLineOutputVoltageLowLimit_Object=MibScalar
upsConfigLineOutputVoltageLowLimit=_UpsConfigLineOutputVoltageLowLimit_Object((1,3,6,1,4,1,7309,6,1,6,3),_UpsConfigLineOutputVoltageLowLimit_Type())
upsConfigLineOutputVoltageLowLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigLineOutputVoltageLowLimit.setStatus(_A)
if mibBuilder.loadTexts:upsConfigLineOutputVoltageLowLimit.setUnits(_U)
_UpsConfigFanOnTemperature_Type=Integer32
_UpsConfigFanOnTemperature_Object=MibScalar
upsConfigFanOnTemperature=_UpsConfigFanOnTemperature_Object((1,3,6,1,4,1,7309,6,1,6,4),_UpsConfigFanOnTemperature_Type())
upsConfigFanOnTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigFanOnTemperature.setStatus(_A)
if mibBuilder.loadTexts:upsConfigFanOnTemperature.setUnits('degreeC')
_UpsShutdownStatus_Type=Integer32
_UpsShutdownStatus_Object=MibScalar
upsShutdownStatus=_UpsShutdownStatus_Object((1,3,6,1,4,1,7309,6,1,6,5),_UpsShutdownStatus_Type())
upsShutdownStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:upsShutdownStatus.setStatus(_A)
_UpsInverterOffDelayTime_Type=Integer32
_UpsInverterOffDelayTime_Object=MibScalar
upsInverterOffDelayTime=_UpsInverterOffDelayTime_Object((1,3,6,1,4,1,7309,6,1,6,6),_UpsInverterOffDelayTime_Type())
upsInverterOffDelayTime.setMaxAccess(_E)
if mibBuilder.loadTexts:upsInverterOffDelayTime.setStatus(_A)
if mibBuilder.loadTexts:upsInverterOffDelayTime.setUnits(_T)
class _UpsConfigIPAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsConfigIPAddress_Type.__name__=_C
_UpsConfigIPAddress_Object=MibScalar
upsConfigIPAddress=_UpsConfigIPAddress_Object((1,3,6,1,4,1,7309,6,1,6,7),_UpsConfigIPAddress_Type())
upsConfigIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:upsConfigIPAddress.setStatus(_A)
class _UpsConfigNetMask_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsConfigNetMask_Type.__name__=_C
_UpsConfigNetMask_Object=MibScalar
upsConfigNetMask=_UpsConfigNetMask_Object((1,3,6,1,4,1,7309,6,1,6,8),_UpsConfigNetMask_Type())
upsConfigNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:upsConfigNetMask.setStatus(_A)
class _UpsConfigGateway_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsConfigGateway_Type.__name__=_C
_UpsConfigGateway_Object=MibScalar
upsConfigGateway=_UpsConfigGateway_Object((1,3,6,1,4,1,7309,6,1,6,9),_UpsConfigGateway_Type())
upsConfigGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:upsConfigGateway.setStatus(_A)
class _UpsConfigSnmpCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsConfigSnmpCommunity_Type.__name__=_C
_UpsConfigSnmpCommunity_Object=MibScalar
upsConfigSnmpCommunity=_UpsConfigSnmpCommunity_Object((1,3,6,1,4,1,7309,6,1,6,10),_UpsConfigSnmpCommunity_Type())
upsConfigSnmpCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:upsConfigSnmpCommunity.setStatus(_A)
class _UpsConfigSnmpTrapIPDestination_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsConfigSnmpTrapIPDestination_Type.__name__=_C
_UpsConfigSnmpTrapIPDestination_Object=MibScalar
upsConfigSnmpTrapIPDestination=_UpsConfigSnmpTrapIPDestination_Object((1,3,6,1,4,1,7309,6,1,6,11),_UpsConfigSnmpTrapIPDestination_Type())
upsConfigSnmpTrapIPDestination.setMaxAccess(_E)
if mibBuilder.loadTexts:upsConfigSnmpTrapIPDestination.setStatus(_A)
_UpsTraps_ObjectIdentity=ObjectIdentity
upsTraps=_UpsTraps_ObjectIdentity((1,3,6,1,4,1,7309,6,1,7))
_UpsTrap_ObjectIdentity=ObjectIdentity
upsTrap=_UpsTrap_ObjectIdentity((1,3,6,1,4,1,7309,6,1,7,0))
_UpsExtra_ObjectIdentity=ObjectIdentity
upsExtra=_UpsExtra_ObjectIdentity((1,3,6,1,4,1,7309,6,1,8))
class _UpsExtraCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UpsExtraCount_Type.__name__=_F
_UpsExtraCount_Object=MibScalar
upsExtraCount=_UpsExtraCount_Object((1,3,6,1,4,1,7309,6,1,8,1),_UpsExtraCount_Type())
upsExtraCount.setMaxAccess(_B)
if mibBuilder.loadTexts:upsExtraCount.setStatus(_A)
_UpsExtraTable_Object=MibTable
upsExtraTable=_UpsExtraTable_Object((1,3,6,1,4,1,7309,6,1,8,2))
if mibBuilder.loadTexts:upsExtraTable.setStatus(_A)
_UpsExtraEntry_Object=MibTableRow
upsExtraEntry=_UpsExtraEntry_Object((1,3,6,1,4,1,7309,6,1,8,2,1))
upsExtraEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:upsExtraEntry.setStatus(_A)
class _UpsExtraIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UpsExtraIndex_Type.__name__=_F
_UpsExtraIndex_Object=MibTableColumn
upsExtraIndex=_UpsExtraIndex_Object((1,3,6,1,4,1,7309,6,1,8,2,1,1),_UpsExtraIndex_Type())
upsExtraIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:upsExtraIndex.setStatus(_A)
class _UpsExtraName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_UpsExtraName_Type.__name__=_C
_UpsExtraName_Object=MibTableColumn
upsExtraName=_UpsExtraName_Object((1,3,6,1,4,1,7309,6,1,8,2,1,2),_UpsExtraName_Type())
upsExtraName.setMaxAccess(_B)
if mibBuilder.loadTexts:upsExtraName.setStatus(_A)
class _UpsExtraIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_UpsExtraIntegerValue_Type.__name__=_F
_UpsExtraIntegerValue_Object=MibTableColumn
upsExtraIntegerValue=_UpsExtraIntegerValue_Object((1,3,6,1,4,1,7309,6,1,8,2,1,3),_UpsExtraIntegerValue_Type())
upsExtraIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:upsExtraIntegerValue.setStatus(_A)
class _UpsExtraStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpsExtraStringValue_Type.__name__=_C
_UpsExtraStringValue_Object=MibTableColumn
upsExtraStringValue=_UpsExtraStringValue_Object((1,3,6,1,4,1,7309,6,1,8,2,1,4),_UpsExtraStringValue_Type())
upsExtraStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:upsExtraStringValue.setStatus(_A)
upsAlarmTrap=NotificationType((1,3,6,1,4,1,7309,6,1,7,0,1))
upsAlarmTrap.setObjects(*((_D,_H),(_D,_I),(_D,_G),(_D,_J)))
if mibBuilder.loadTexts:upsAlarmTrap.setStatus(_A)
upsAgentStartupTrap=NotificationType((1,3,6,1,4,1,7309,6,1,7,0,2))
upsAgentStartupTrap.setObjects((_D,_L))
if mibBuilder.loadTexts:upsAgentStartupTrap.setStatus(_A)
upsAgentShutdownTrap=NotificationType((1,3,6,1,4,1,7309,6,1,7,0,3))
upsAgentShutdownTrap.setObjects((_D,_L))
if mibBuilder.loadTexts:upsAgentShutdownTrap.setStatus(_A)
upsAgentFaultTrap=NotificationType((1,3,6,1,4,1,7309,6,1,7,0,4))
upsAgentFaultTrap.setObjects(*((_D,_H),(_D,_I),(_D,_G),(_D,_J)))
if mibBuilder.loadTexts:upsAgentFaultTrap.setStatus(_A)
upsAgentEventTrap=NotificationType((1,3,6,1,4,1,7309,6,1,7,0,5))
upsAgentEventTrap.setObjects(*((_D,_H),(_D,_I),(_D,_G),(_D,_J)))
if mibBuilder.loadTexts:upsAgentEventTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PositiveInteger':PositiveInteger,'NonNegativeInteger':NonNegativeInteger,_C:DisplayString,_M:PhysAddress,'argus':argus,'upsPower':upsPower,'upsDevice':upsDevice,'upsIdent':upsIdent,'upsIdentManufacturer':upsIdentManufacturer,'upsIdentProductCode':upsIdentProductCode,'upsIdentModel':upsIdentModel,'upsIdentUPSSoftwareVersion':upsIdentUPSSoftwareVersion,'upsIdentAgentSoftwareVersion':upsIdentAgentSoftwareVersion,'upsIdentName':upsIdentName,'upsIdentAttachedDevices':upsIdentAttachedDevices,_L:upsIdentSiteName,'upsIdentSiteCity':upsIdentSiteCity,'upsIdentSiteRegion':upsIdentSiteRegion,'upsIdentSiteCountry':upsIdentSiteCountry,'upsIdentContactName':upsIdentContactName,'upsIdentPhoneNumber':upsIdentPhoneNumber,'upsIdentDate':upsIdentDate,'upsIdentTime':upsIdentTime,'upsBattery':upsBattery,'upsBatteryStatus':upsBatteryStatus,'upsMinutesOnBattery':upsMinutesOnBattery,'upsBatteryVoltage':upsBatteryVoltage,'upsBatteryChargingCurrent':upsBatteryChargingCurrent,'upsBatteryCapacity':upsBatteryCapacity,'upsBatteryTemperature':upsBatteryTemperature,'upsBatteryLowWarning':upsBatteryLowWarning,'upsInput':upsInput,'upsInputNumLines':upsInputNumLines,'upsInputTable':upsInputTable,'upsInputEntry':upsInputEntry,_O:upsInputLineIndex,'upsInputFrequency':upsInputFrequency,'upsInputVoltage':upsInputVoltage,'upsOutput':upsOutput,'upsOutputSource':upsOutputSource,'upsOutputFrequency':upsOutputFrequency,'upsOutputNumLines':upsOutputNumLines,'upsOutputTable':upsOutputTable,'upsOutputEntry':upsOutputEntry,_Q:upsOutputLineIndex,'upsOutputVoltage':upsOutputVoltage,'upsOutputCurrent':upsOutputCurrent,'upsOutputPowerVA':upsOutputPowerVA,'upsOutputPowerWatt':upsOutputPowerWatt,'upsPowerFactor':upsPowerFactor,'upsOutputPercentLoad':upsOutputPercentLoad,'upsAlarm':upsAlarm,'upsAlarmsPresent':upsAlarmsPresent,'upsAlarmTable':upsAlarmTable,'upsAlarmEntry':upsAlarmEntry,_S:upsAlarmId,'upsAlarmDescr':upsAlarmDescr,'upsAlarmStatus':upsAlarmStatus,'upsConfig':upsConfig,'upsConfigLineQualifyTime':upsConfigLineQualifyTime,'upsConfigLineOutputVoltageHighLimit':upsConfigLineOutputVoltageHighLimit,'upsConfigLineOutputVoltageLowLimit':upsConfigLineOutputVoltageLowLimit,'upsConfigFanOnTemperature':upsConfigFanOnTemperature,'upsShutdownStatus':upsShutdownStatus,'upsInverterOffDelayTime':upsInverterOffDelayTime,'upsConfigIPAddress':upsConfigIPAddress,'upsConfigNetMask':upsConfigNetMask,'upsConfigGateway':upsConfigGateway,'upsConfigSnmpCommunity':upsConfigSnmpCommunity,'upsConfigSnmpTrapIPDestination':upsConfigSnmpTrapIPDestination,'upsTraps':upsTraps,'upsTrap':upsTrap,'upsAlarmTrap':upsAlarmTrap,'upsAgentStartupTrap':upsAgentStartupTrap,'upsAgentShutdownTrap':upsAgentShutdownTrap,'upsAgentFaultTrap':upsAgentFaultTrap,'upsAgentEventTrap':upsAgentEventTrap,'upsExtra':upsExtra,'upsExtraCount':upsExtraCount,'upsExtraTable':upsExtraTable,'upsExtraEntry':upsExtraEntry,_G:upsExtraIndex,_J:upsExtraName,_H:upsExtraIntegerValue,_I:upsExtraStringValue})