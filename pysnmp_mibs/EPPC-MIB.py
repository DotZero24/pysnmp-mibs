_AI='upsESystemConfigBelowRemainTimeLimit'
_AH='upsESystemConfigBelowCapacityLimit'
_AG='upsEBatteryEstimatedChargeRemaining'
_AF='upsEControlOutputOnDelay'
_AE='upsEBatteryTestStartTime'
_AD='upsEBatteryTestResult'
_AC='upsEBatteryTestSettingTime'
_AB='upsEBatteryTestStart'
_AA='upsESecondsOnBattery'
_A9='upsETrapsReceiversIndex'
_A8='upsEControlSpecialDayScheduleIndex'
_A7='wednesday'
_A6='upsEControlWeeklyScheduleIndex'
_A5='upsEOverTemperature'
_A4='upsEOverLoad'
_A3='upsEShutdownEvent'
_A2='upsEBatteryTestScheduleIndex'
_A1='batteryTestWithTime'
_A0='batteryTestUntilLow'
_z='upsEEnvironmentContactIndex'
_y='not-support'
_x='on-pending'
_w='off-pending'
_v='upsEModulesNum'
_u='chargerModulesNum'
_t='batteryLow'
_s='unknown'
_r='upsESystemBypassPhase'
_q='upsESystemOutputPhase'
_p='upsESystemInputPhase'
_o='on-reducer'
_n='on-booster'
_m='converter'
_l='battery-test'
_k='battery'
_j='by-pass'
_i='stand-by'
_h='power-on'
_g='NotificationType'
_f='upsEEnvironmentHumidityLowSetPoint'
_e='upsEEnvironmentHumidityHighSetPoint'
_d='upsEEnvironmentTemperatureLowSetPoint'
_c='upsEEnvironmentTemperatureHighSetPoint'
_b='upsESystemConfigOutputLoadHighSetPoint'
_a='upsESystemOutputLoad'
_Z='upsESystemConfigOverTemperatureSetPoint'
_Y='upsESystemTemperature'
_X='upsEBatteryEstimatedMinutesRemaining'
_W='sunday'
_V='saturday'
_U='friday'
_T='tuesday'
_S='monday'
_R='shutdown'
_Q='fault'
_P='NonNegativeInteger'
_O='enable'
_N='upsEEnvironmentContactDescription'
_M='upsEEnvironmentContactType'
_L='upsEEnvironmentCurrentHumidity'
_K='upsEEnvironmentCurrentTemperature'
_J='disable'
_I='none'
_H='PositiveInteger'
_G='not-accessible'
_F='Integer32'
_E='DisplayString'
_D='read-write'
_C='EPPC-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_g,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_g,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
NonNegativeInteger,PositiveInteger=mibBuilder.importSymbols('UPS-MIB',_P,_H)
_Ppc_ObjectIdentity=ObjectIdentity
ppc=_Ppc_ObjectIdentity((1,3,6,1,4,1,935))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,935,10))
_UpsAgent_ObjectIdentity=ObjectIdentity
upsAgent=_UpsAgent_ObjectIdentity((1,3,6,1,4,1,935,10,1))
_UpsE_ObjectIdentity=ObjectIdentity
upsE=_UpsE_ObjectIdentity((1,3,6,1,4,1,935,10,1,1))
_UpsEIdentity_ObjectIdentity=ObjectIdentity
upsEIdentity=_UpsEIdentity_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,1))
class _UpsEIdentityManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsEIdentityManufacturer_Type.__name__=_E
_UpsEIdentityManufacturer_Object=MibScalar
upsEIdentityManufacturer=_UpsEIdentityManufacturer_Object((1,3,6,1,4,1,935,10,1,1,1,1),_UpsEIdentityManufacturer_Type())
upsEIdentityManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEIdentityManufacturer.setStatus(_A)
class _UpsEIdentityModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsEIdentityModel_Type.__name__=_E
_UpsEIdentityModel_Object=MibScalar
upsEIdentityModel=_UpsEIdentityModel_Object((1,3,6,1,4,1,935,10,1,1,1,2),_UpsEIdentityModel_Type())
upsEIdentityModel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEIdentityModel.setStatus(_A)
class _UpsEIdentityUPSFirmwareVerison_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsEIdentityUPSFirmwareVerison_Type.__name__=_E
_UpsEIdentityUPSFirmwareVerison_Object=MibScalar
upsEIdentityUPSFirmwareVerison=_UpsEIdentityUPSFirmwareVerison_Object((1,3,6,1,4,1,935,10,1,1,1,3),_UpsEIdentityUPSFirmwareVerison_Type())
upsEIdentityUPSFirmwareVerison.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEIdentityUPSFirmwareVerison.setStatus(_A)
class _UpsEIndentityUPSSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsEIndentityUPSSerialNumber_Type.__name__=_E
_UpsEIndentityUPSSerialNumber_Object=MibScalar
upsEIndentityUPSSerialNumber=_UpsEIndentityUPSSerialNumber_Object((1,3,6,1,4,1,935,10,1,1,1,4),_UpsEIndentityUPSSerialNumber_Type())
upsEIndentityUPSSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEIndentityUPSSerialNumber.setStatus(_A)
class _UpsEIdentityDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsEIdentityDescription_Type.__name__=_E
_UpsEIdentityDescription_Object=MibScalar
upsEIdentityDescription=_UpsEIdentityDescription_Object((1,3,6,1,4,1,935,10,1,1,1,5),_UpsEIdentityDescription_Type())
upsEIdentityDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEIdentityDescription.setStatus(_A)
class _UpsEIdentityAgentSoftwareVerison_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsEIdentityAgentSoftwareVerison_Type.__name__=_E
_UpsEIdentityAgentSoftwareVerison_Object=MibScalar
upsEIdentityAgentSoftwareVerison=_UpsEIdentityAgentSoftwareVerison_Object((1,3,6,1,4,1,935,10,1,1,1,6),_UpsEIdentityAgentSoftwareVerison_Type())
upsEIdentityAgentSoftwareVerison.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEIdentityAgentSoftwareVerison.setStatus(_A)
class _UpsEIdentityAttachedDevices_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsEIdentityAttachedDevices_Type.__name__=_E
_UpsEIdentityAttachedDevices_Object=MibScalar
upsEIdentityAttachedDevices=_UpsEIdentityAttachedDevices_Object((1,3,6,1,4,1,935,10,1,1,1,7),_UpsEIdentityAttachedDevices_Type())
upsEIdentityAttachedDevices.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEIdentityAttachedDevices.setStatus(_A)
_UpsESystemSummary_ObjectIdentity=ObjectIdentity
upsESystemSummary=_UpsESystemSummary_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,2))
class _UpsESystemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),('line',4),(_k,5),(_l,6),(_Q,7),(_m,8),('eco',9),(_R,10),(_n,11),(_o,12),('other',13)))
_UpsESystemStatus_Type.__name__=_F
_UpsESystemStatus_Object=MibScalar
upsESystemStatus=_UpsESystemStatus_Object((1,3,6,1,4,1,935,10,1,1,2,1),_UpsESystemStatus_Type())
upsESystemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemStatus.setStatus(_A)
_UpsESystemTemperature_Type=Integer32
_UpsESystemTemperature_Object=MibScalar
upsESystemTemperature=_UpsESystemTemperature_Object((1,3,6,1,4,1,935,10,1,1,2,2),_UpsESystemTemperature_Type())
upsESystemTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemTemperature.setStatus(_A)
class _UpsESystemWarningCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_UpsESystemWarningCode_Type.__name__=_E
_UpsESystemWarningCode_Object=MibScalar
upsESystemWarningCode=_UpsESystemWarningCode_Object((1,3,6,1,4,1,935,10,1,1,2,3),_UpsESystemWarningCode_Type())
upsESystemWarningCode.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemWarningCode.setStatus(_A)
class _UpsESystemFaultCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_UpsESystemFaultCode_Type.__name__=_E
_UpsESystemFaultCode_Object=MibScalar
upsESystemFaultCode=_UpsESystemFaultCode_Object((1,3,6,1,4,1,935,10,1,1,2,4),_UpsESystemFaultCode_Type())
upsESystemFaultCode.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemFaultCode.setStatus(_A)
_UpsESystemConfigInputVoltage_Type=NonNegativeInteger
_UpsESystemConfigInputVoltage_Object=MibScalar
upsESystemConfigInputVoltage=_UpsESystemConfigInputVoltage_Object((1,3,6,1,4,1,935,10,1,1,2,5),_UpsESystemConfigInputVoltage_Type())
upsESystemConfigInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemConfigInputVoltage.setStatus(_A)
_UpsESystemConfigInputFrequence_Type=NonNegativeInteger
_UpsESystemConfigInputFrequence_Object=MibScalar
upsESystemConfigInputFrequence=_UpsESystemConfigInputFrequence_Object((1,3,6,1,4,1,935,10,1,1,2,6),_UpsESystemConfigInputFrequence_Type())
upsESystemConfigInputFrequence.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemConfigInputFrequence.setStatus(_A)
_UpsESystemConfigOutputVoltage_Type=NonNegativeInteger
_UpsESystemConfigOutputVoltage_Object=MibScalar
upsESystemConfigOutputVoltage=_UpsESystemConfigOutputVoltage_Object((1,3,6,1,4,1,935,10,1,1,2,7),_UpsESystemConfigOutputVoltage_Type())
upsESystemConfigOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemConfigOutputVoltage.setStatus(_A)
_UpsESystemConfigOutputFrequency_Type=NonNegativeInteger
_UpsESystemConfigOutputFrequency_Object=MibScalar
upsESystemConfigOutputFrequency=_UpsESystemConfigOutputFrequency_Object((1,3,6,1,4,1,935,10,1,1,2,8),_UpsESystemConfigOutputFrequency_Type())
upsESystemConfigOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemConfigOutputFrequency.setStatus(_A)
_UpsESystemConfigOutputVA_Type=NonNegativeInteger
_UpsESystemConfigOutputVA_Object=MibScalar
upsESystemConfigOutputVA=_UpsESystemConfigOutputVA_Object((1,3,6,1,4,1,935,10,1,1,2,9),_UpsESystemConfigOutputVA_Type())
upsESystemConfigOutputVA.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemConfigOutputVA.setStatus(_A)
_UpsESystemConfigOutputPower_Type=NonNegativeInteger
_UpsESystemConfigOutputPower_Object=MibScalar
upsESystemConfigOutputPower=_UpsESystemConfigOutputPower_Object((1,3,6,1,4,1,935,10,1,1,2,10),_UpsESystemConfigOutputPower_Type())
upsESystemConfigOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemConfigOutputPower.setStatus(_A)
_UpsESystemConfigOutputLoadHighSetPoint_Type=NonNegativeInteger
_UpsESystemConfigOutputLoadHighSetPoint_Object=MibScalar
upsESystemConfigOutputLoadHighSetPoint=_UpsESystemConfigOutputLoadHighSetPoint_Object((1,3,6,1,4,1,935,10,1,1,2,11),_UpsESystemConfigOutputLoadHighSetPoint_Type())
upsESystemConfigOutputLoadHighSetPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:upsESystemConfigOutputLoadHighSetPoint.setStatus(_A)
_UpsESystemConfigOverTemperatureSetPoint_Type=NonNegativeInteger
_UpsESystemConfigOverTemperatureSetPoint_Object=MibScalar
upsESystemConfigOverTemperatureSetPoint=_UpsESystemConfigOverTemperatureSetPoint_Object((1,3,6,1,4,1,935,10,1,1,2,12),_UpsESystemConfigOverTemperatureSetPoint_Type())
upsESystemConfigOverTemperatureSetPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:upsESystemConfigOverTemperatureSetPoint.setStatus(_A)
_UpsESystemInputSourceNum_Type=Integer32
_UpsESystemInputSourceNum_Object=MibScalar
upsESystemInputSourceNum=_UpsESystemInputSourceNum_Object((1,3,6,1,4,1,935,10,1,1,2,13),_UpsESystemInputSourceNum_Type())
upsESystemInputSourceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemInputSourceNum.setStatus(_A)
_UpsESystemInputLineBads_Type=Counter32
_UpsESystemInputLineBads_Object=MibScalar
upsESystemInputLineBads=_UpsESystemInputLineBads_Object((1,3,6,1,4,1,935,10,1,1,2,14),_UpsESystemInputLineBads_Type())
upsESystemInputLineBads.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemInputLineBads.setStatus(_A)
class _UpsESystemInputNumPhases_Type(PositiveInteger):subtypeSpec=PositiveInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_UpsESystemInputNumPhases_Type.__name__=_H
_UpsESystemInputNumPhases_Object=MibScalar
upsESystemInputNumPhases=_UpsESystemInputNumPhases_Object((1,3,6,1,4,1,935,10,1,1,2,15),_UpsESystemInputNumPhases_Type())
upsESystemInputNumPhases.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemInputNumPhases.setStatus(_A)
_UpsESystemInputTable_Object=MibTable
upsESystemInputTable=_UpsESystemInputTable_Object((1,3,6,1,4,1,935,10,1,1,2,16))
if mibBuilder.loadTexts:upsESystemInputTable.setStatus(_A)
_UpsESystemInputEntry_Object=MibTableRow
upsESystemInputEntry=_UpsESystemInputEntry_Object((1,3,6,1,4,1,935,10,1,1,2,16,1))
upsESystemInputEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:upsESystemInputEntry.setStatus(_A)
class _UpsESystemInputPhase_Type(PositiveInteger):subtypeSpec=PositiveInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_UpsESystemInputPhase_Type.__name__=_H
_UpsESystemInputPhase_Object=MibTableColumn
upsESystemInputPhase=_UpsESystemInputPhase_Object((1,3,6,1,4,1,935,10,1,1,2,16,1,1),_UpsESystemInputPhase_Type())
upsESystemInputPhase.setMaxAccess(_G)
if mibBuilder.loadTexts:upsESystemInputPhase.setStatus(_A)
_UpsESystemInputFrequency_Type=NonNegativeInteger
_UpsESystemInputFrequency_Object=MibTableColumn
upsESystemInputFrequency=_UpsESystemInputFrequency_Object((1,3,6,1,4,1,935,10,1,1,2,16,1,2),_UpsESystemInputFrequency_Type())
upsESystemInputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemInputFrequency.setStatus(_A)
_UpsESystemInputVoltage_Type=NonNegativeInteger
_UpsESystemInputVoltage_Object=MibTableColumn
upsESystemInputVoltage=_UpsESystemInputVoltage_Object((1,3,6,1,4,1,935,10,1,1,2,16,1,3),_UpsESystemInputVoltage_Type())
upsESystemInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemInputVoltage.setStatus(_A)
_UpsESystemInputCurrent_Type=NonNegativeInteger
_UpsESystemInputCurrent_Object=MibTableColumn
upsESystemInputCurrent=_UpsESystemInputCurrent_Object((1,3,6,1,4,1,935,10,1,1,2,16,1,4),_UpsESystemInputCurrent_Type())
upsESystemInputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemInputCurrent.setStatus(_A)
_UpsESystemInputWatts_Type=NonNegativeInteger
_UpsESystemInputWatts_Object=MibTableColumn
upsESystemInputWatts=_UpsESystemInputWatts_Object((1,3,6,1,4,1,935,10,1,1,2,16,1,5),_UpsESystemInputWatts_Type())
upsESystemInputWatts.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemInputWatts.setStatus(_A)
class _UpsESystemOutputNumPhase_Type(PositiveInteger):subtypeSpec=PositiveInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_UpsESystemOutputNumPhase_Type.__name__=_H
_UpsESystemOutputNumPhase_Object=MibScalar
upsESystemOutputNumPhase=_UpsESystemOutputNumPhase_Object((1,3,6,1,4,1,935,10,1,1,2,17),_UpsESystemOutputNumPhase_Type())
upsESystemOutputNumPhase.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemOutputNumPhase.setStatus(_A)
_UpsESystemOutputTable_Object=MibTable
upsESystemOutputTable=_UpsESystemOutputTable_Object((1,3,6,1,4,1,935,10,1,1,2,18))
if mibBuilder.loadTexts:upsESystemOutputTable.setStatus(_A)
_UpsESystemOutputEntry_Object=MibTableRow
upsESystemOutputEntry=_UpsESystemOutputEntry_Object((1,3,6,1,4,1,935,10,1,1,2,18,1))
upsESystemOutputEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:upsESystemOutputEntry.setStatus(_A)
class _UpsESystemOutputPhase_Type(PositiveInteger):subtypeSpec=PositiveInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_UpsESystemOutputPhase_Type.__name__=_H
_UpsESystemOutputPhase_Object=MibTableColumn
upsESystemOutputPhase=_UpsESystemOutputPhase_Object((1,3,6,1,4,1,935,10,1,1,2,18,1,1),_UpsESystemOutputPhase_Type())
upsESystemOutputPhase.setMaxAccess(_G)
if mibBuilder.loadTexts:upsESystemOutputPhase.setStatus(_A)
_UpsESystemOutputFrequency_Type=NonNegativeInteger
_UpsESystemOutputFrequency_Object=MibTableColumn
upsESystemOutputFrequency=_UpsESystemOutputFrequency_Object((1,3,6,1,4,1,935,10,1,1,2,18,1,2),_UpsESystemOutputFrequency_Type())
upsESystemOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemOutputFrequency.setStatus(_A)
_UpsESystemOutputVoltage_Type=NonNegativeInteger
_UpsESystemOutputVoltage_Object=MibTableColumn
upsESystemOutputVoltage=_UpsESystemOutputVoltage_Object((1,3,6,1,4,1,935,10,1,1,2,18,1,3),_UpsESystemOutputVoltage_Type())
upsESystemOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemOutputVoltage.setStatus(_A)
_UpsESystemOutputCurrent_Type=NonNegativeInteger
_UpsESystemOutputCurrent_Object=MibTableColumn
upsESystemOutputCurrent=_UpsESystemOutputCurrent_Object((1,3,6,1,4,1,935,10,1,1,2,18,1,4),_UpsESystemOutputCurrent_Type())
upsESystemOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemOutputCurrent.setStatus(_A)
_UpsESystemOutputWatts_Type=NonNegativeInteger
_UpsESystemOutputWatts_Object=MibTableColumn
upsESystemOutputWatts=_UpsESystemOutputWatts_Object((1,3,6,1,4,1,935,10,1,1,2,18,1,5),_UpsESystemOutputWatts_Type())
upsESystemOutputWatts.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemOutputWatts.setStatus(_A)
_UpsESystemOutputVA_Type=NonNegativeInteger
_UpsESystemOutputVA_Object=MibTableColumn
upsESystemOutputVA=_UpsESystemOutputVA_Object((1,3,6,1,4,1,935,10,1,1,2,18,1,6),_UpsESystemOutputVA_Type())
upsESystemOutputVA.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemOutputVA.setStatus(_A)
_UpsESystemOutputLoad_Type=NonNegativeInteger
_UpsESystemOutputLoad_Object=MibTableColumn
upsESystemOutputLoad=_UpsESystemOutputLoad_Object((1,3,6,1,4,1,935,10,1,1,2,18,1,7),_UpsESystemOutputLoad_Type())
upsESystemOutputLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemOutputLoad.setStatus(_A)
class _UpsESystemBypassNumPhase_Type(PositiveInteger):subtypeSpec=PositiveInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_UpsESystemBypassNumPhase_Type.__name__=_H
_UpsESystemBypassNumPhase_Object=MibScalar
upsESystemBypassNumPhase=_UpsESystemBypassNumPhase_Object((1,3,6,1,4,1,935,10,1,1,2,19),_UpsESystemBypassNumPhase_Type())
upsESystemBypassNumPhase.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemBypassNumPhase.setStatus(_A)
_UpsESystemBypassTable_Object=MibTable
upsESystemBypassTable=_UpsESystemBypassTable_Object((1,3,6,1,4,1,935,10,1,1,2,20))
if mibBuilder.loadTexts:upsESystemBypassTable.setStatus(_A)
_UpsESystemBypassEntry_Object=MibTableRow
upsESystemBypassEntry=_UpsESystemBypassEntry_Object((1,3,6,1,4,1,935,10,1,1,2,20,1))
upsESystemBypassEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:upsESystemBypassEntry.setStatus(_A)
class _UpsESystemBypassPhase_Type(PositiveInteger):subtypeSpec=PositiveInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_UpsESystemBypassPhase_Type.__name__=_H
_UpsESystemBypassPhase_Object=MibTableColumn
upsESystemBypassPhase=_UpsESystemBypassPhase_Object((1,3,6,1,4,1,935,10,1,1,2,20,1,1),_UpsESystemBypassPhase_Type())
upsESystemBypassPhase.setMaxAccess(_G)
if mibBuilder.loadTexts:upsESystemBypassPhase.setStatus(_A)
_UpsESystemBypassFrequency_Type=NonNegativeInteger
_UpsESystemBypassFrequency_Object=MibTableColumn
upsESystemBypassFrequency=_UpsESystemBypassFrequency_Object((1,3,6,1,4,1,935,10,1,1,2,20,1,2),_UpsESystemBypassFrequency_Type())
upsESystemBypassFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemBypassFrequency.setStatus(_A)
_UpsESystemBypassVoltage_Type=NonNegativeInteger
_UpsESystemBypassVoltage_Object=MibTableColumn
upsESystemBypassVoltage=_UpsESystemBypassVoltage_Object((1,3,6,1,4,1,935,10,1,1,2,20,1,3),_UpsESystemBypassVoltage_Type())
upsESystemBypassVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemBypassVoltage.setStatus(_A)
_UpsESystemBypassCurrent_Type=NonNegativeInteger
_UpsESystemBypassCurrent_Object=MibTableColumn
upsESystemBypassCurrent=_UpsESystemBypassCurrent_Object((1,3,6,1,4,1,935,10,1,1,2,20,1,4),_UpsESystemBypassCurrent_Type())
upsESystemBypassCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemBypassCurrent.setStatus(_A)
_UpsESystemBypassWatts_Type=NonNegativeInteger
_UpsESystemBypassWatts_Object=MibTableColumn
upsESystemBypassWatts=_UpsESystemBypassWatts_Object((1,3,6,1,4,1,935,10,1,1,2,20,1,5),_UpsESystemBypassWatts_Type())
upsESystemBypassWatts.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemBypassWatts.setStatus(_A)
_UpsESystemConfigBelowCapacityLimit_Type=NonNegativeInteger
_UpsESystemConfigBelowCapacityLimit_Object=MibScalar
upsESystemConfigBelowCapacityLimit=_UpsESystemConfigBelowCapacityLimit_Object((1,3,6,1,4,1,935,10,1,1,2,21),_UpsESystemConfigBelowCapacityLimit_Type())
upsESystemConfigBelowCapacityLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:upsESystemConfigBelowCapacityLimit.setStatus(_A)
_UpsESystemConfigBelowRemainTimeLimit_Type=NonNegativeInteger
_UpsESystemConfigBelowRemainTimeLimit_Object=MibScalar
upsESystemConfigBelowRemainTimeLimit=_UpsESystemConfigBelowRemainTimeLimit_Object((1,3,6,1,4,1,935,10,1,1,2,22),_UpsESystemConfigBelowRemainTimeLimit_Type())
upsESystemConfigBelowRemainTimeLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:upsESystemConfigBelowRemainTimeLimit.setStatus(_A)
_UpsEBatterySystem_ObjectIdentity=ObjectIdentity
upsEBatterySystem=_UpsEBatterySystem_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,3))
class _UpsEBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_s,1),('batteryNormal',2),(_t,3),('batteryDepleted',4),('batteryDischarging',5),('batteryFailure',6)))
_UpsEBatteryStatus_Type.__name__=_F
_UpsEBatteryStatus_Object=MibScalar
upsEBatteryStatus=_UpsEBatteryStatus_Object((1,3,6,1,4,1,935,10,1,1,3,1),_UpsEBatteryStatus_Type())
upsEBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryStatus.setStatus(_A)
_UpsESecondsOnBattery_Type=NonNegativeInteger
_UpsESecondsOnBattery_Object=MibScalar
upsESecondsOnBattery=_UpsESecondsOnBattery_Object((1,3,6,1,4,1,935,10,1,1,3,2),_UpsESecondsOnBattery_Type())
upsESecondsOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESecondsOnBattery.setStatus(_A)
_UpsEBatteryEstimatedMinutesRemaining_Type=PositiveInteger
_UpsEBatteryEstimatedMinutesRemaining_Object=MibScalar
upsEBatteryEstimatedMinutesRemaining=_UpsEBatteryEstimatedMinutesRemaining_Object((1,3,6,1,4,1,935,10,1,1,3,3),_UpsEBatteryEstimatedMinutesRemaining_Type())
upsEBatteryEstimatedMinutesRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryEstimatedMinutesRemaining.setStatus(_A)
class _UpsEBatteryEstimatedChargeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_UpsEBatteryEstimatedChargeRemaining_Type.__name__=_F
_UpsEBatteryEstimatedChargeRemaining_Object=MibScalar
upsEBatteryEstimatedChargeRemaining=_UpsEBatteryEstimatedChargeRemaining_Object((1,3,6,1,4,1,935,10,1,1,3,4),_UpsEBatteryEstimatedChargeRemaining_Type())
upsEBatteryEstimatedChargeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryEstimatedChargeRemaining.setStatus(_A)
_UpsEPositiveBatteryVoltage_Type=NonNegativeInteger
_UpsEPositiveBatteryVoltage_Object=MibScalar
upsEPositiveBatteryVoltage=_UpsEPositiveBatteryVoltage_Object((1,3,6,1,4,1,935,10,1,1,3,5),_UpsEPositiveBatteryVoltage_Type())
upsEPositiveBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEPositiveBatteryVoltage.setStatus(_A)
_UpsENegativeBatteryVoltage_Type=NonNegativeInteger
_UpsENegativeBatteryVoltage_Object=MibScalar
upsENegativeBatteryVoltage=_UpsENegativeBatteryVoltage_Object((1,3,6,1,4,1,935,10,1,1,3,6),_UpsENegativeBatteryVoltage_Type())
upsENegativeBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsENegativeBatteryVoltage.setStatus(_A)
_UpsEBatteryCellNumber_Type=NonNegativeInteger
_UpsEBatteryCellNumber_Object=MibScalar
upsEBatteryCellNumber=_UpsEBatteryCellNumber_Object((1,3,6,1,4,1,935,10,1,1,3,7),_UpsEBatteryCellNumber_Type())
upsEBatteryCellNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryCellNumber.setStatus(_A)
_UpsEBatteryTemperature_Type=Integer32
_UpsEBatteryTemperature_Object=MibScalar
upsEBatteryTemperature=_UpsEBatteryTemperature_Object((1,3,6,1,4,1,935,10,1,1,3,8),_UpsEBatteryTemperature_Type())
upsEBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryTemperature.setStatus(_A)
class _UpsEBatteryLastReplacedDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_UpsEBatteryLastReplacedDate_Type.__name__=_E
_UpsEBatteryLastReplacedDate_Object=MibScalar
upsEBatteryLastReplacedDate=_UpsEBatteryLastReplacedDate_Object((1,3,6,1,4,1,935,10,1,1,3,9),_UpsEBatteryLastReplacedDate_Type())
upsEBatteryLastReplacedDate.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryLastReplacedDate.setStatus(_A)
class _UpsEBatteryABMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('charge',1),('float',2),('rest',3),('discharge',4),(_J,5)))
_UpsEBatteryABMStatus_Type.__name__=_F
_UpsEBatteryABMStatus_Object=MibScalar
upsEBatteryABMStatus=_UpsEBatteryABMStatus_Object((1,3,6,1,4,1,935,10,1,1,3,10),_UpsEBatteryABMStatus_Type())
upsEBatteryABMStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryABMStatus.setStatus(_A)
class _UpsEChargerModulesNum_Type(NonNegativeInteger):subtypeSpec=NonNegativeInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_UpsEChargerModulesNum_Type.__name__=_P
_UpsEChargerModulesNum_Object=MibScalar
upsEChargerModulesNum=_UpsEChargerModulesNum_Object((1,3,6,1,4,1,935,10,1,1,3,11),_UpsEChargerModulesNum_Type())
upsEChargerModulesNum.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEChargerModulesNum.setStatus(_A)
_UpsEChargerModulesTable_Object=MibTable
upsEChargerModulesTable=_UpsEChargerModulesTable_Object((1,3,6,1,4,1,935,10,1,1,3,12))
if mibBuilder.loadTexts:upsEChargerModulesTable.setStatus(_A)
_UpsEChargerModulesEntry_Object=MibTableRow
upsEChargerModulesEntry=_UpsEChargerModulesEntry_Object((1,3,6,1,4,1,935,10,1,1,3,12,1))
upsEChargerModulesEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:upsEChargerModulesEntry.setStatus(_A)
class _ChargerModulesNum_Type(PositiveInteger):subtypeSpec=PositiveInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ChargerModulesNum_Type.__name__=_H
_ChargerModulesNum_Object=MibTableColumn
chargerModulesNum=_ChargerModulesNum_Object((1,3,6,1,4,1,935,10,1,1,3,12,1,1),_ChargerModulesNum_Type())
chargerModulesNum.setMaxAccess(_G)
if mibBuilder.loadTexts:chargerModulesNum.setStatus(_A)
_ChargerModulesAddress_Type=NonNegativeInteger
_ChargerModulesAddress_Object=MibTableColumn
chargerModulesAddress=_ChargerModulesAddress_Object((1,3,6,1,4,1,935,10,1,1,3,12,1,2),_ChargerModulesAddress_Type())
chargerModulesAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chargerModulesAddress.setStatus(_A)
_PositiveChargeVotlage_Type=NonNegativeInteger
_PositiveChargeVotlage_Object=MibTableColumn
positiveChargeVotlage=_PositiveChargeVotlage_Object((1,3,6,1,4,1,935,10,1,1,3,12,1,3),_PositiveChargeVotlage_Type())
positiveChargeVotlage.setMaxAccess(_B)
if mibBuilder.loadTexts:positiveChargeVotlage.setStatus(_A)
_NegativeChargeVoltage_Type=NonNegativeInteger
_NegativeChargeVoltage_Object=MibTableColumn
negativeChargeVoltage=_NegativeChargeVoltage_Object((1,3,6,1,4,1,935,10,1,1,3,12,1,4),_NegativeChargeVoltage_Type())
negativeChargeVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:negativeChargeVoltage.setStatus(_A)
_PositiveChargeCurrent_Type=NonNegativeInteger
_PositiveChargeCurrent_Object=MibTableColumn
positiveChargeCurrent=_PositiveChargeCurrent_Object((1,3,6,1,4,1,935,10,1,1,3,12,1,5),_PositiveChargeCurrent_Type())
positiveChargeCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:positiveChargeCurrent.setStatus(_A)
_NegativeChargeCurrent_Type=NonNegativeInteger
_NegativeChargeCurrent_Object=MibTableColumn
negativeChargeCurrent=_NegativeChargeCurrent_Object((1,3,6,1,4,1,935,10,1,1,3,12,1,6),_NegativeChargeCurrent_Type())
negativeChargeCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:negativeChargeCurrent.setStatus(_A)
_ChargerModulesTemperature_Type=Integer32
_ChargerModulesTemperature_Object=MibTableColumn
chargerModulesTemperature=_ChargerModulesTemperature_Object((1,3,6,1,4,1,935,10,1,1,3,12,1,7),_ChargerModulesTemperature_Type())
chargerModulesTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:chargerModulesTemperature.setStatus(_A)
class _ChargerModulesMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('powerOn',1),('standyby',2),(_Q,3),(_R,4),('running',5),('suicide',6),(_s,7)))
_ChargerModulesMode_Type.__name__=_F
_ChargerModulesMode_Object=MibTableColumn
chargerModulesMode=_ChargerModulesMode_Object((1,3,6,1,4,1,935,10,1,1,3,12,1,8),_ChargerModulesMode_Type())
chargerModulesMode.setMaxAccess(_B)
if mibBuilder.loadTexts:chargerModulesMode.setStatus(_A)
_UpsEPowerConverterSystem_ObjectIdentity=ObjectIdentity
upsEPowerConverterSystem=_UpsEPowerConverterSystem_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,4))
class _UpsEUPSModulesNum_Type(NonNegativeInteger):subtypeSpec=NonNegativeInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_UpsEUPSModulesNum_Type.__name__=_P
_UpsEUPSModulesNum_Object=MibScalar
upsEUPSModulesNum=_UpsEUPSModulesNum_Object((1,3,6,1,4,1,935,10,1,1,4,1),_UpsEUPSModulesNum_Type())
upsEUPSModulesNum.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEUPSModulesNum.setStatus(_A)
_UpsEModulesTable_Object=MibTable
upsEModulesTable=_UpsEModulesTable_Object((1,3,6,1,4,1,935,10,1,1,4,2))
if mibBuilder.loadTexts:upsEModulesTable.setStatus(_A)
_UpsEModulesEntry_Object=MibTableRow
upsEModulesEntry=_UpsEModulesEntry_Object((1,3,6,1,4,1,935,10,1,1,4,2,1))
upsEModulesEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:upsEModulesEntry.setStatus(_A)
class _UpsEModulesNum_Type(PositiveInteger):subtypeSpec=PositiveInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_UpsEModulesNum_Type.__name__=_H
_UpsEModulesNum_Object=MibTableColumn
upsEModulesNum=_UpsEModulesNum_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,1),_UpsEModulesNum_Type())
upsEModulesNum.setMaxAccess(_G)
if mibBuilder.loadTexts:upsEModulesNum.setStatus(_A)
_UpsEModuleAddress_Type=Integer32
_UpsEModuleAddress_Object=MibTableColumn
upsEModuleAddress=_UpsEModuleAddress_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,2),_UpsEModuleAddress_Type())
upsEModuleAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleAddress.setStatus(_A)
_UpsEModulePositiveBusVolt_Type=NonNegativeInteger
_UpsEModulePositiveBusVolt_Object=MibTableColumn
upsEModulePositiveBusVolt=_UpsEModulePositiveBusVolt_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,3),_UpsEModulePositiveBusVolt_Type())
upsEModulePositiveBusVolt.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModulePositiveBusVolt.setStatus(_A)
_UpsEModuleNegativeBusVolt_Type=NonNegativeInteger
_UpsEModuleNegativeBusVolt_Object=MibTableColumn
upsEModuleNegativeBusVolt=_UpsEModuleNegativeBusVolt_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,4),_UpsEModuleNegativeBusVolt_Type())
upsEModuleNegativeBusVolt.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleNegativeBusVolt.setStatus(_A)
_UpsEModuleTemperature_Type=Integer32
_UpsEModuleTemperature_Object=MibTableColumn
upsEModuleTemperature=_UpsEModuleTemperature_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,5),_UpsEModuleTemperature_Type())
upsEModuleTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleTemperature.setStatus(_A)
class _UpsEModuleWorkingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),('line',4),(_k,5),(_l,6),(_Q,7),(_m,8),('eco',9),(_R,10),(_n,11),(_o,12),('other',13)))
_UpsEModuleWorkingMode_Type.__name__=_F
_UpsEModuleWorkingMode_Object=MibTableColumn
upsEModuleWorkingMode=_UpsEModuleWorkingMode_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,6),_UpsEModuleWorkingMode_Type())
upsEModuleWorkingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleWorkingMode.setStatus(_A)
_UpsEModuleOutputCurrentR_Type=NonNegativeInteger
_UpsEModuleOutputCurrentR_Object=MibTableColumn
upsEModuleOutputCurrentR=_UpsEModuleOutputCurrentR_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,7),_UpsEModuleOutputCurrentR_Type())
upsEModuleOutputCurrentR.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputCurrentR.setStatus(_A)
_UpsEModuleOutputWattR_Type=NonNegativeInteger
_UpsEModuleOutputWattR_Object=MibTableColumn
upsEModuleOutputWattR=_UpsEModuleOutputWattR_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,8),_UpsEModuleOutputWattR_Type())
upsEModuleOutputWattR.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputWattR.setStatus(_A)
_UpsEModuleOutputLoadR_Type=Integer32
_UpsEModuleOutputLoadR_Object=MibTableColumn
upsEModuleOutputLoadR=_UpsEModuleOutputLoadR_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,9),_UpsEModuleOutputLoadR_Type())
upsEModuleOutputLoadR.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputLoadR.setStatus(_A)
class _UpsEModuleWarningCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_UpsEModuleWarningCode_Type.__name__=_E
_UpsEModuleWarningCode_Object=MibTableColumn
upsEModuleWarningCode=_UpsEModuleWarningCode_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,10),_UpsEModuleWarningCode_Type())
upsEModuleWarningCode.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleWarningCode.setStatus(_A)
class _UpsEModuleFaultCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_UpsEModuleFaultCode_Type.__name__=_E
_UpsEModuleFaultCode_Object=MibTableColumn
upsEModuleFaultCode=_UpsEModuleFaultCode_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,11),_UpsEModuleFaultCode_Type())
upsEModuleFaultCode.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleFaultCode.setStatus(_A)
class _UpsEModuleTrapState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_UpsEModuleTrapState_Type.__name__=_E
_UpsEModuleTrapState_Object=MibTableColumn
upsEModuleTrapState=_UpsEModuleTrapState_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,12),_UpsEModuleTrapState_Type())
upsEModuleTrapState.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleTrapState.setStatus(_A)
_UpsEModuleConfigOutputVA_Type=NonNegativeInteger
_UpsEModuleConfigOutputVA_Object=MibTableColumn
upsEModuleConfigOutputVA=_UpsEModuleConfigOutputVA_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,13),_UpsEModuleConfigOutputVA_Type())
upsEModuleConfigOutputVA.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleConfigOutputVA.setStatus(_A)
_UpsEModuleOutputCurrentS_Type=NonNegativeInteger
_UpsEModuleOutputCurrentS_Object=MibTableColumn
upsEModuleOutputCurrentS=_UpsEModuleOutputCurrentS_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,14),_UpsEModuleOutputCurrentS_Type())
upsEModuleOutputCurrentS.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputCurrentS.setStatus(_A)
_UpsEModuleOutputCurrentT_Type=NonNegativeInteger
_UpsEModuleOutputCurrentT_Object=MibTableColumn
upsEModuleOutputCurrentT=_UpsEModuleOutputCurrentT_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,15),_UpsEModuleOutputCurrentT_Type())
upsEModuleOutputCurrentT.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputCurrentT.setStatus(_A)
_UpsEModuleOutputWattS_Type=NonNegativeInteger
_UpsEModuleOutputWattS_Object=MibTableColumn
upsEModuleOutputWattS=_UpsEModuleOutputWattS_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,16),_UpsEModuleOutputWattS_Type())
upsEModuleOutputWattS.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputWattS.setStatus(_A)
_UpsEModuleOutputWattT_Type=NonNegativeInteger
_UpsEModuleOutputWattT_Object=MibTableColumn
upsEModuleOutputWattT=_UpsEModuleOutputWattT_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,17),_UpsEModuleOutputWattT_Type())
upsEModuleOutputWattT.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputWattT.setStatus(_A)
_UpsEModuleOutputLoadS_Type=Integer32
_UpsEModuleOutputLoadS_Object=MibTableColumn
upsEModuleOutputLoadS=_UpsEModuleOutputLoadS_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,18),_UpsEModuleOutputLoadS_Type())
upsEModuleOutputLoadS.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputLoadS.setStatus(_A)
_UpsEModuleOutputLoadT_Type=Integer32
_UpsEModuleOutputLoadT_Object=MibTableColumn
upsEModuleOutputLoadT=_UpsEModuleOutputLoadT_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,19),_UpsEModuleOutputLoadT_Type())
upsEModuleOutputLoadT.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputLoadT.setStatus(_A)
_UpsEModuleOutputVAR_Type=NonNegativeInteger
_UpsEModuleOutputVAR_Object=MibTableColumn
upsEModuleOutputVAR=_UpsEModuleOutputVAR_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,20),_UpsEModuleOutputVAR_Type())
upsEModuleOutputVAR.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputVAR.setStatus(_A)
_UpsEModuleOutputVAS_Type=NonNegativeInteger
_UpsEModuleOutputVAS_Object=MibTableColumn
upsEModuleOutputVAS=_UpsEModuleOutputVAS_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,21),_UpsEModuleOutputVAS_Type())
upsEModuleOutputVAS.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputVAS.setStatus(_A)
_UpsEModuleOutputVAT_Type=NonNegativeInteger
_UpsEModuleOutputVAT_Object=MibTableColumn
upsEModuleOutputVAT=_UpsEModuleOutputVAT_Object((1,3,6,1,4,1,935,10,1,1,4,2,1,22),_UpsEModuleOutputVAT_Type())
upsEModuleOutputVAT.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEModuleOutputVAT.setStatus(_A)
_UpsELoadSegment_ObjectIdentity=ObjectIdentity
upsELoadSegment=_UpsELoadSegment_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,5))
_UpsELoadSegment1OffDelay_Type=Integer32
_UpsELoadSegment1OffDelay_Object=MibScalar
upsELoadSegment1OffDelay=_UpsELoadSegment1OffDelay_Object((1,3,6,1,4,1,935,10,1,1,5,1),_UpsELoadSegment1OffDelay_Type())
upsELoadSegment1OffDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsELoadSegment1OffDelay.setStatus(_A)
_UpsELoadSegment1OnDelay_Type=Integer32
_UpsELoadSegment1OnDelay_Object=MibScalar
upsELoadSegment1OnDelay=_UpsELoadSegment1OnDelay_Object((1,3,6,1,4,1,935,10,1,1,5,2),_UpsELoadSegment1OnDelay_Type())
upsELoadSegment1OnDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsELoadSegment1OnDelay.setStatus(_A)
_UpsELoadSegment1AutoOffTimer_Type=Integer32
_UpsELoadSegment1AutoOffTimer_Object=MibScalar
upsELoadSegment1AutoOffTimer=_UpsELoadSegment1AutoOffTimer_Object((1,3,6,1,4,1,935,10,1,1,5,3),_UpsELoadSegment1AutoOffTimer_Type())
upsELoadSegment1AutoOffTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:upsELoadSegment1AutoOffTimer.setStatus(_A)
_UpsELoadSegment1AutoOnTimer_Type=Integer32
_UpsELoadSegment1AutoOnTimer_Object=MibScalar
upsELoadSegment1AutoOnTimer=_UpsELoadSegment1AutoOnTimer_Object((1,3,6,1,4,1,935,10,1,1,5,4),_UpsELoadSegment1AutoOnTimer_Type())
upsELoadSegment1AutoOnTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:upsELoadSegment1AutoOnTimer.setStatus(_A)
class _UpsELoadSegment1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('off',1),('on',2),(_w,3),(_x,4),(_y,5)))
_UpsELoadSegment1State_Type.__name__=_F
_UpsELoadSegment1State_Object=MibScalar
upsELoadSegment1State=_UpsELoadSegment1State_Object((1,3,6,1,4,1,935,10,1,1,5,5),_UpsELoadSegment1State_Type())
upsELoadSegment1State.setMaxAccess(_B)
if mibBuilder.loadTexts:upsELoadSegment1State.setStatus(_A)
_UpsELoadSegment2OffDelay_Type=Integer32
_UpsELoadSegment2OffDelay_Object=MibScalar
upsELoadSegment2OffDelay=_UpsELoadSegment2OffDelay_Object((1,3,6,1,4,1,935,10,1,1,5,6),_UpsELoadSegment2OffDelay_Type())
upsELoadSegment2OffDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsELoadSegment2OffDelay.setStatus(_A)
_UpsELoadSegment2OnDelay_Type=Integer32
_UpsELoadSegment2OnDelay_Object=MibScalar
upsELoadSegment2OnDelay=_UpsELoadSegment2OnDelay_Object((1,3,6,1,4,1,935,10,1,1,5,7),_UpsELoadSegment2OnDelay_Type())
upsELoadSegment2OnDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsELoadSegment2OnDelay.setStatus(_A)
_UpsELoadSegment2AutoOffTimer_Type=Integer32
_UpsELoadSegment2AutoOffTimer_Object=MibScalar
upsELoadSegment2AutoOffTimer=_UpsELoadSegment2AutoOffTimer_Object((1,3,6,1,4,1,935,10,1,1,5,8),_UpsELoadSegment2AutoOffTimer_Type())
upsELoadSegment2AutoOffTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:upsELoadSegment2AutoOffTimer.setStatus(_A)
_UpsELoadSegment2AutoOnTimer_Type=Integer32
_UpsELoadSegment2AutoOnTimer_Object=MibScalar
upsELoadSegment2AutoOnTimer=_UpsELoadSegment2AutoOnTimer_Object((1,3,6,1,4,1,935,10,1,1,5,9),_UpsELoadSegment2AutoOnTimer_Type())
upsELoadSegment2AutoOnTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:upsELoadSegment2AutoOnTimer.setStatus(_A)
class _UpsELoadSegment2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('off',1),('on',2),(_w,3),(_x,4),(_y,5)))
_UpsELoadSegment2State_Type.__name__=_F
_UpsELoadSegment2State_Object=MibScalar
upsELoadSegment2State=_UpsELoadSegment2State_Object((1,3,6,1,4,1,935,10,1,1,5,10),_UpsELoadSegment2State_Type())
upsELoadSegment2State.setMaxAccess(_B)
if mibBuilder.loadTexts:upsELoadSegment2State.setStatus(_A)
_UpsEEnvironment_ObjectIdentity=ObjectIdentity
upsEEnvironment=_UpsEEnvironment_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,6))
_UpsEEnvironmentTemperature_ObjectIdentity=ObjectIdentity
upsEEnvironmentTemperature=_UpsEEnvironmentTemperature_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,6,1))
_UpsEEnvironmentCurrentTemperature_Type=Integer32
_UpsEEnvironmentCurrentTemperature_Object=MibScalar
upsEEnvironmentCurrentTemperature=_UpsEEnvironmentCurrentTemperature_Object((1,3,6,1,4,1,935,10,1,1,6,1,1),_UpsEEnvironmentCurrentTemperature_Type())
upsEEnvironmentCurrentTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEEnvironmentCurrentTemperature.setStatus(_A)
_UpsEEnvironmentTemperatureHighSetPoint_Type=Integer32
_UpsEEnvironmentTemperatureHighSetPoint_Object=MibScalar
upsEEnvironmentTemperatureHighSetPoint=_UpsEEnvironmentTemperatureHighSetPoint_Object((1,3,6,1,4,1,935,10,1,1,6,1,2),_UpsEEnvironmentTemperatureHighSetPoint_Type())
upsEEnvironmentTemperatureHighSetPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentTemperatureHighSetPoint.setStatus(_A)
class _UpsEEnvironmentTemperatureHighStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_J,2)))
_UpsEEnvironmentTemperatureHighStatus_Type.__name__=_F
_UpsEEnvironmentTemperatureHighStatus_Object=MibScalar
upsEEnvironmentTemperatureHighStatus=_UpsEEnvironmentTemperatureHighStatus_Object((1,3,6,1,4,1,935,10,1,1,6,1,3),_UpsEEnvironmentTemperatureHighStatus_Type())
upsEEnvironmentTemperatureHighStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentTemperatureHighStatus.setStatus(_A)
_UpsEEnvironmentTemperatureLowSetPoint_Type=Integer32
_UpsEEnvironmentTemperatureLowSetPoint_Object=MibScalar
upsEEnvironmentTemperatureLowSetPoint=_UpsEEnvironmentTemperatureLowSetPoint_Object((1,3,6,1,4,1,935,10,1,1,6,1,4),_UpsEEnvironmentTemperatureLowSetPoint_Type())
upsEEnvironmentTemperatureLowSetPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentTemperatureLowSetPoint.setStatus(_A)
class _UpsEEnvironmentTemperatureLowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_J,2)))
_UpsEEnvironmentTemperatureLowStatus_Type.__name__=_F
_UpsEEnvironmentTemperatureLowStatus_Object=MibScalar
upsEEnvironmentTemperatureLowStatus=_UpsEEnvironmentTemperatureLowStatus_Object((1,3,6,1,4,1,935,10,1,1,6,1,5),_UpsEEnvironmentTemperatureLowStatus_Type())
upsEEnvironmentTemperatureLowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentTemperatureLowStatus.setStatus(_A)
_UpsEEnvironmentTemperatureOffset_Type=Integer32
_UpsEEnvironmentTemperatureOffset_Object=MibScalar
upsEEnvironmentTemperatureOffset=_UpsEEnvironmentTemperatureOffset_Object((1,3,6,1,4,1,935,10,1,1,6,1,6),_UpsEEnvironmentTemperatureOffset_Type())
upsEEnvironmentTemperatureOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentTemperatureOffset.setStatus(_A)
_UpsEEnvironmentHumidity_ObjectIdentity=ObjectIdentity
upsEEnvironmentHumidity=_UpsEEnvironmentHumidity_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,6,2))
_UpsEEnvironmentCurrentHumidity_Type=Integer32
_UpsEEnvironmentCurrentHumidity_Object=MibScalar
upsEEnvironmentCurrentHumidity=_UpsEEnvironmentCurrentHumidity_Object((1,3,6,1,4,1,935,10,1,1,6,2,1),_UpsEEnvironmentCurrentHumidity_Type())
upsEEnvironmentCurrentHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEEnvironmentCurrentHumidity.setStatus(_A)
_UpsEEnvironmentHumidityHighSetPoint_Type=Integer32
_UpsEEnvironmentHumidityHighSetPoint_Object=MibScalar
upsEEnvironmentHumidityHighSetPoint=_UpsEEnvironmentHumidityHighSetPoint_Object((1,3,6,1,4,1,935,10,1,1,6,2,2),_UpsEEnvironmentHumidityHighSetPoint_Type())
upsEEnvironmentHumidityHighSetPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentHumidityHighSetPoint.setStatus(_A)
class _UpsEEnvironmentHumidityHighStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_J,2)))
_UpsEEnvironmentHumidityHighStatus_Type.__name__=_F
_UpsEEnvironmentHumidityHighStatus_Object=MibScalar
upsEEnvironmentHumidityHighStatus=_UpsEEnvironmentHumidityHighStatus_Object((1,3,6,1,4,1,935,10,1,1,6,2,3),_UpsEEnvironmentHumidityHighStatus_Type())
upsEEnvironmentHumidityHighStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentHumidityHighStatus.setStatus(_A)
_UpsEEnvironmentHumidityLowSetPoint_Type=Integer32
_UpsEEnvironmentHumidityLowSetPoint_Object=MibScalar
upsEEnvironmentHumidityLowSetPoint=_UpsEEnvironmentHumidityLowSetPoint_Object((1,3,6,1,4,1,935,10,1,1,6,2,4),_UpsEEnvironmentHumidityLowSetPoint_Type())
upsEEnvironmentHumidityLowSetPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentHumidityLowSetPoint.setStatus(_A)
class _UpsEEnvironmentHumidityLowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_J,2)))
_UpsEEnvironmentHumidityLowStatus_Type.__name__=_F
_UpsEEnvironmentHumidityLowStatus_Object=MibScalar
upsEEnvironmentHumidityLowStatus=_UpsEEnvironmentHumidityLowStatus_Object((1,3,6,1,4,1,935,10,1,1,6,2,5),_UpsEEnvironmentHumidityLowStatus_Type())
upsEEnvironmentHumidityLowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentHumidityLowStatus.setStatus(_A)
_UpsEEnvironmentHumidityOffset_Type=Integer32
_UpsEEnvironmentHumidityOffset_Object=MibScalar
upsEEnvironmentHumidityOffset=_UpsEEnvironmentHumidityOffset_Object((1,3,6,1,4,1,935,10,1,1,6,2,6),_UpsEEnvironmentHumidityOffset_Type())
upsEEnvironmentHumidityOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentHumidityOffset.setStatus(_A)
_UpsEEnvironmentContactsNum_Type=NonNegativeInteger
_UpsEEnvironmentContactsNum_Object=MibScalar
upsEEnvironmentContactsNum=_UpsEEnvironmentContactsNum_Object((1,3,6,1,4,1,935,10,1,1,6,3),_UpsEEnvironmentContactsNum_Type())
upsEEnvironmentContactsNum.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEEnvironmentContactsNum.setStatus(_A)
_UpsEEnvironmentContactTable_Object=MibTable
upsEEnvironmentContactTable=_UpsEEnvironmentContactTable_Object((1,3,6,1,4,1,935,10,1,1,6,4))
if mibBuilder.loadTexts:upsEEnvironmentContactTable.setStatus(_A)
_UpsEEnvironmentContactEntry_Object=MibTableRow
upsEEnvironmentContactEntry=_UpsEEnvironmentContactEntry_Object((1,3,6,1,4,1,935,10,1,1,6,4,1))
upsEEnvironmentContactEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:upsEEnvironmentContactEntry.setStatus(_A)
_UpsEEnvironmentContactIndex_Type=PositiveInteger
_UpsEEnvironmentContactIndex_Object=MibTableColumn
upsEEnvironmentContactIndex=_UpsEEnvironmentContactIndex_Object((1,3,6,1,4,1,935,10,1,1,6,4,1,1),_UpsEEnvironmentContactIndex_Type())
upsEEnvironmentContactIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:upsEEnvironmentContactIndex.setStatus(_A)
class _UpsEEnvironmentContactType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normallyOpen',1),('normallyClosed',2),('notUsed',3)))
_UpsEEnvironmentContactType_Type.__name__=_F
_UpsEEnvironmentContactType_Object=MibTableColumn
upsEEnvironmentContactType=_UpsEEnvironmentContactType_Object((1,3,6,1,4,1,935,10,1,1,6,4,1,2),_UpsEEnvironmentContactType_Type())
upsEEnvironmentContactType.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentContactType.setStatus(_A)
class _UpsEEnvironmentContactState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('open',1),('closed',2),('openWithNotice',3),('closedWithNotice',4)))
_UpsEEnvironmentContactState_Type.__name__=_F
_UpsEEnvironmentContactState_Object=MibTableColumn
upsEEnvironmentContactState=_UpsEEnvironmentContactState_Object((1,3,6,1,4,1,935,10,1,1,6,4,1,3),_UpsEEnvironmentContactState_Type())
upsEEnvironmentContactState.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEEnvironmentContactState.setStatus(_A)
class _UpsEEnvironmentContactDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsEEnvironmentContactDescription_Type.__name__=_E
_UpsEEnvironmentContactDescription_Object=MibTableColumn
upsEEnvironmentContactDescription=_UpsEEnvironmentContactDescription_Object((1,3,6,1,4,1,935,10,1,1,6,4,1,4),_UpsEEnvironmentContactDescription_Type())
upsEEnvironmentContactDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEEnvironmentContactDescription.setStatus(_A)
_UpsEBatteryTest_ObjectIdentity=ObjectIdentity
upsEBatteryTest=_UpsEBatteryTest_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,7))
class _UpsEBatteryTestStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('batteryTest10Sec',2),(_A0,3),(_A1,4),('cancelBatteryTest',5),('clearBatteryInfo',6)))
_UpsEBatteryTestStart_Type.__name__=_F
_UpsEBatteryTestStart_Object=MibScalar
upsEBatteryTestStart=_UpsEBatteryTestStart_Object((1,3,6,1,4,1,935,10,1,1,7,1),_UpsEBatteryTestStart_Type())
upsEBatteryTestStart.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEBatteryTestStart.setStatus(_A)
_UpsEBatteryTestSettingTime_Type=NonNegativeInteger
_UpsEBatteryTestSettingTime_Object=MibScalar
upsEBatteryTestSettingTime=_UpsEBatteryTestSettingTime_Object((1,3,6,1,4,1,935,10,1,1,7,2),_UpsEBatteryTestSettingTime_Type())
upsEBatteryTestSettingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEBatteryTestSettingTime.setStatus(_A)
class _UpsEBatteryTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('processing',2),('noFailure',3),('failureOrWarning',4),('notPossible',5),('testCancel',6)))
_UpsEBatteryTestResult_Type.__name__=_F
_UpsEBatteryTestResult_Object=MibScalar
upsEBatteryTestResult=_UpsEBatteryTestResult_Object((1,3,6,1,4,1,935,10,1,1,7,3),_UpsEBatteryTestResult_Type())
upsEBatteryTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryTestResult.setStatus(_A)
class _UpsEBatteryTestStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(19,19));fixedLength=19
_UpsEBatteryTestStartTime_Type.__name__=_E
_UpsEBatteryTestStartTime_Object=MibScalar
upsEBatteryTestStartTime=_UpsEBatteryTestStartTime_Object((1,3,6,1,4,1,935,10,1,1,7,4),_UpsEBatteryTestStartTime_Type())
upsEBatteryTestStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryTestStartTime.setStatus(_A)
class _UpsEBatteryTestElapsedTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_UpsEBatteryTestElapsedTime_Type.__name__=_E
_UpsEBatteryTestElapsedTime_Object=MibScalar
upsEBatteryTestElapsedTime=_UpsEBatteryTestElapsedTime_Object((1,3,6,1,4,1,935,10,1,1,7,5),_UpsEBatteryTestElapsedTime_Type())
upsEBatteryTestElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEBatteryTestElapsedTime.setStatus(_A)
_UpsEBatteryTestScheduleTable_Object=MibTable
upsEBatteryTestScheduleTable=_UpsEBatteryTestScheduleTable_Object((1,3,6,1,4,1,935,10,1,1,7,6))
if mibBuilder.loadTexts:upsEBatteryTestScheduleTable.setStatus(_A)
_UpsEBatteryTestScheduleEntry_Object=MibTableRow
upsEBatteryTestScheduleEntry=_UpsEBatteryTestScheduleEntry_Object((1,3,6,1,4,1,935,10,1,1,7,6,1))
upsEBatteryTestScheduleEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:upsEBatteryTestScheduleEntry.setStatus(_A)
_UpsEBatteryTestScheduleIndex_Type=PositiveInteger
_UpsEBatteryTestScheduleIndex_Object=MibTableColumn
upsEBatteryTestScheduleIndex=_UpsEBatteryTestScheduleIndex_Object((1,3,6,1,4,1,935,10,1,1,7,6,1,1),_UpsEBatteryTestScheduleIndex_Type())
upsEBatteryTestScheduleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:upsEBatteryTestScheduleIndex.setStatus(_A)
class _UpsEBatteryTestScheduleDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_S,1),(_T,2),('wednsday',3),('thusday',4),(_U,5),(_V,6),(_W,7),('specialday',8),(_I,9)))
_UpsEBatteryTestScheduleDay_Type.__name__=_F
_UpsEBatteryTestScheduleDay_Object=MibTableColumn
upsEBatteryTestScheduleDay=_UpsEBatteryTestScheduleDay_Object((1,3,6,1,4,1,935,10,1,1,7,6,1,2),_UpsEBatteryTestScheduleDay_Type())
upsEBatteryTestScheduleDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEBatteryTestScheduleDay.setStatus(_A)
class _UpsEBatteryTestScheduleTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsEBatteryTestScheduleTime_Type.__name__=_E
_UpsEBatteryTestScheduleTime_Object=MibTableColumn
upsEBatteryTestScheduleTime=_UpsEBatteryTestScheduleTime_Object((1,3,6,1,4,1,935,10,1,1,7,6,1,3),_UpsEBatteryTestScheduleTime_Type())
upsEBatteryTestScheduleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEBatteryTestScheduleTime.setStatus(_A)
class _UpsEBatteryTestScheduleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('batteryTest10sec',2),(_A0,3),(_A1,4)))
_UpsEBatteryTestScheduleType_Type.__name__=_F
_UpsEBatteryTestScheduleType_Object=MibTableColumn
upsEBatteryTestScheduleType=_UpsEBatteryTestScheduleType_Object((1,3,6,1,4,1,935,10,1,1,7,6,1,5),_UpsEBatteryTestScheduleType_Type())
upsEBatteryTestScheduleType.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEBatteryTestScheduleType.setStatus(_A)
_UpsEBatteryTestScheduleTestWithTime_Type=NonNegativeInteger
_UpsEBatteryTestScheduleTestWithTime_Object=MibTableColumn
upsEBatteryTestScheduleTestWithTime=_UpsEBatteryTestScheduleTestWithTime_Object((1,3,6,1,4,1,935,10,1,1,7,6,1,6),_UpsEBatteryTestScheduleTestWithTime_Type())
upsEBatteryTestScheduleTestWithTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEBatteryTestScheduleTestWithTime.setStatus(_A)
class _UpsEBatteryTestScheduleSpecialDay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_UpsEBatteryTestScheduleSpecialDay_Type.__name__=_E
_UpsEBatteryTestScheduleSpecialDay_Object=MibTableColumn
upsEBatteryTestScheduleSpecialDay=_UpsEBatteryTestScheduleSpecialDay_Object((1,3,6,1,4,1,935,10,1,1,7,6,1,7),_UpsEBatteryTestScheduleSpecialDay_Type())
upsEBatteryTestScheduleSpecialDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEBatteryTestScheduleSpecialDay.setStatus(_A)
_UpsEControl_ObjectIdentity=ObjectIdentity
upsEControl=_UpsEControl_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,8))
_UpsEControlOutputOffDelay_Type=NonNegativeInteger
_UpsEControlOutputOffDelay_Object=MibScalar
upsEControlOutputOffDelay=_UpsEControlOutputOffDelay_Object((1,3,6,1,4,1,935,10,1,1,8,1),_UpsEControlOutputOffDelay_Type())
upsEControlOutputOffDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEControlOutputOffDelay.setStatus(_A)
_UpsEControlOutputOnDelay_Type=NonNegativeInteger
_UpsEControlOutputOnDelay_Object=MibScalar
upsEControlOutputOnDelay=_UpsEControlOutputOnDelay_Object((1,3,6,1,4,1,935,10,1,1,8,2),_UpsEControlOutputOnDelay_Type())
upsEControlOutputOnDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEControlOutputOnDelay.setStatus(_A)
class _UpsEControlOutputOnOffControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('upsEOutputOff',1),('upsEOutputOffCancel',2),('upsESleep',3),(_I,4)))
_UpsEControlOutputOnOffControl_Type.__name__=_F
_UpsEControlOutputOnOffControl_Object=MibScalar
upsEControlOutputOnOffControl=_UpsEControlOutputOnOffControl_Object((1,3,6,1,4,1,935,10,1,1,8,3),_UpsEControlOutputOnOffControl_Type())
upsEControlOutputOnOffControl.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEControlOutputOnOffControl.setStatus(_A)
_UpsEShutdownEventsTable_Object=MibTable
upsEShutdownEventsTable=_UpsEShutdownEventsTable_Object((1,3,6,1,4,1,935,10,1,1,8,4))
if mibBuilder.loadTexts:upsEShutdownEventsTable.setStatus(_A)
_UpsEShutdownEventsEntry_Object=MibTableRow
upsEShutdownEventsEntry=_UpsEShutdownEventsEntry_Object((1,3,6,1,4,1,935,10,1,1,8,4,1))
upsEShutdownEventsEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:upsEShutdownEventsEntry.setStatus(_A)
class _UpsEShutdownEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('acFail',1),(_t,2),(_A4,3),(_A5,4),('upsEWeeklySchedule',5),('upsESpecialSchedule',6),('environmentTemperatureOverThreshold',7),('environmentHumidityOverThreshold',8),('environmentContact1Alarm',9),('environmentContact2Alarm',10),('belowCapacityLimit',11),('belowRemainTimeLimit',12)))
_UpsEShutdownEvent_Type.__name__=_F
_UpsEShutdownEvent_Object=MibTableColumn
upsEShutdownEvent=_UpsEShutdownEvent_Object((1,3,6,1,4,1,935,10,1,1,8,4,1,1),_UpsEShutdownEvent_Type())
upsEShutdownEvent.setMaxAccess(_G)
if mibBuilder.loadTexts:upsEShutdownEvent.setStatus(_A)
class _UpsEShutdownEventAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('warning',2),('shutdownClient',3),('shutdownUPS',4)))
_UpsEShutdownEventAction_Type.__name__=_F
_UpsEShutdownEventAction_Object=MibTableColumn
upsEShutdownEventAction=_UpsEShutdownEventAction_Object((1,3,6,1,4,1,935,10,1,1,8,4,1,2),_UpsEShutdownEventAction_Type())
upsEShutdownEventAction.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEShutdownEventAction.setStatus(_A)
_UpsEShutdownwarningPeriodTime_Type=NonNegativeInteger
_UpsEShutdownwarningPeriodTime_Object=MibTableColumn
upsEShutdownwarningPeriodTime=_UpsEShutdownwarningPeriodTime_Object((1,3,6,1,4,1,935,10,1,1,8,4,1,3),_UpsEShutdownwarningPeriodTime_Type())
upsEShutdownwarningPeriodTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEShutdownwarningPeriodTime.setStatus(_A)
_UpsEShutdownWarningPeriodInterval_Type=NonNegativeInteger
_UpsEShutdownWarningPeriodInterval_Object=MibTableColumn
upsEShutdownWarningPeriodInterval=_UpsEShutdownWarningPeriodInterval_Object((1,3,6,1,4,1,935,10,1,1,8,4,1,4),_UpsEShutdownWarningPeriodInterval_Type())
upsEShutdownWarningPeriodInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEShutdownWarningPeriodInterval.setStatus(_A)
_UpsEControlWeeklyScheduleTable_Object=MibTable
upsEControlWeeklyScheduleTable=_UpsEControlWeeklyScheduleTable_Object((1,3,6,1,4,1,935,10,1,1,8,5))
if mibBuilder.loadTexts:upsEControlWeeklyScheduleTable.setStatus(_A)
_UpsEControlWeeklyScheduleEntry_Object=MibTableRow
upsEControlWeeklyScheduleEntry=_UpsEControlWeeklyScheduleEntry_Object((1,3,6,1,4,1,935,10,1,1,8,5,1))
upsEControlWeeklyScheduleEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:upsEControlWeeklyScheduleEntry.setStatus(_A)
_UpsEControlWeeklyScheduleIndex_Type=PositiveInteger
_UpsEControlWeeklyScheduleIndex_Object=MibTableColumn
upsEControlWeeklyScheduleIndex=_UpsEControlWeeklyScheduleIndex_Object((1,3,6,1,4,1,935,10,1,1,8,5,1,1),_UpsEControlWeeklyScheduleIndex_Type())
upsEControlWeeklyScheduleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:upsEControlWeeklyScheduleIndex.setStatus(_A)
class _UpsEWeeklyScheduleShutdownDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,1),(_T,2),(_A7,3),('thursday',4),(_U,5),(_V,6),(_W,7),(_I,8)))
_UpsEWeeklyScheduleShutdownDay_Type.__name__=_F
_UpsEWeeklyScheduleShutdownDay_Object=MibTableColumn
upsEWeeklyScheduleShutdownDay=_UpsEWeeklyScheduleShutdownDay_Object((1,3,6,1,4,1,935,10,1,1,8,5,1,2),_UpsEWeeklyScheduleShutdownDay_Type())
upsEWeeklyScheduleShutdownDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEWeeklyScheduleShutdownDay.setStatus(_A)
class _UpsEWeeklyScheduleShutdownTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsEWeeklyScheduleShutdownTime_Type.__name__=_E
_UpsEWeeklyScheduleShutdownTime_Object=MibTableColumn
upsEWeeklyScheduleShutdownTime=_UpsEWeeklyScheduleShutdownTime_Object((1,3,6,1,4,1,935,10,1,1,8,5,1,3),_UpsEWeeklyScheduleShutdownTime_Type())
upsEWeeklyScheduleShutdownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEWeeklyScheduleShutdownTime.setStatus(_A)
class _UpsEWeeklyScheduleRestartDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,1),(_T,2),(_A7,3),('thursday',4),(_U,5),(_V,6),(_W,7),(_I,8)))
_UpsEWeeklyScheduleRestartDay_Type.__name__=_F
_UpsEWeeklyScheduleRestartDay_Object=MibTableColumn
upsEWeeklyScheduleRestartDay=_UpsEWeeklyScheduleRestartDay_Object((1,3,6,1,4,1,935,10,1,1,8,5,1,4),_UpsEWeeklyScheduleRestartDay_Type())
upsEWeeklyScheduleRestartDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEWeeklyScheduleRestartDay.setStatus(_A)
class _UpsEWeeklyScheduleRestartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsEWeeklyScheduleRestartTime_Type.__name__=_E
_UpsEWeeklyScheduleRestartTime_Object=MibTableColumn
upsEWeeklyScheduleRestartTime=_UpsEWeeklyScheduleRestartTime_Object((1,3,6,1,4,1,935,10,1,1,8,5,1,5),_UpsEWeeklyScheduleRestartTime_Type())
upsEWeeklyScheduleRestartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsEWeeklyScheduleRestartTime.setStatus(_A)
_UpsEControlSpecialDayScheduleTable_Object=MibTable
upsEControlSpecialDayScheduleTable=_UpsEControlSpecialDayScheduleTable_Object((1,3,6,1,4,1,935,10,1,1,8,6))
if mibBuilder.loadTexts:upsEControlSpecialDayScheduleTable.setStatus(_A)
_UpsEControlSpecialDayScheduleEntry_Object=MibTableRow
upsEControlSpecialDayScheduleEntry=_UpsEControlSpecialDayScheduleEntry_Object((1,3,6,1,4,1,935,10,1,1,8,6,1))
upsEControlSpecialDayScheduleEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:upsEControlSpecialDayScheduleEntry.setStatus(_A)
_UpsEControlSpecialDayScheduleIndex_Type=PositiveInteger
_UpsEControlSpecialDayScheduleIndex_Object=MibTableColumn
upsEControlSpecialDayScheduleIndex=_UpsEControlSpecialDayScheduleIndex_Object((1,3,6,1,4,1,935,10,1,1,8,6,1,1),_UpsEControlSpecialDayScheduleIndex_Type())
upsEControlSpecialDayScheduleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:upsEControlSpecialDayScheduleIndex.setStatus(_A)
class _UpsESpecialDayScheduleShutdownDay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_UpsESpecialDayScheduleShutdownDay_Type.__name__=_E
_UpsESpecialDayScheduleShutdownDay_Object=MibTableColumn
upsESpecialDayScheduleShutdownDay=_UpsESpecialDayScheduleShutdownDay_Object((1,3,6,1,4,1,935,10,1,1,8,6,1,2),_UpsESpecialDayScheduleShutdownDay_Type())
upsESpecialDayScheduleShutdownDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsESpecialDayScheduleShutdownDay.setStatus(_A)
class _UpsESpecialDayScheduleShutdownTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsESpecialDayScheduleShutdownTime_Type.__name__=_E
_UpsESpecialDayScheduleShutdownTime_Object=MibTableColumn
upsESpecialDayScheduleShutdownTime=_UpsESpecialDayScheduleShutdownTime_Object((1,3,6,1,4,1,935,10,1,1,8,6,1,3),_UpsESpecialDayScheduleShutdownTime_Type())
upsESpecialDayScheduleShutdownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsESpecialDayScheduleShutdownTime.setStatus(_A)
class _UpsESpecialDayScheduleRestartDay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_UpsESpecialDayScheduleRestartDay_Type.__name__=_E
_UpsESpecialDayScheduleRestartDay_Object=MibTableColumn
upsESpecialDayScheduleRestartDay=_UpsESpecialDayScheduleRestartDay_Object((1,3,6,1,4,1,935,10,1,1,8,6,1,4),_UpsESpecialDayScheduleRestartDay_Type())
upsESpecialDayScheduleRestartDay.setMaxAccess(_D)
if mibBuilder.loadTexts:upsESpecialDayScheduleRestartDay.setStatus(_A)
class _UpsESpecialDayScheduleRestartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_UpsESpecialDayScheduleRestartTime_Type.__name__=_E
_UpsESpecialDayScheduleRestartTime_Object=MibTableColumn
upsESpecialDayScheduleRestartTime=_UpsESpecialDayScheduleRestartTime_Object((1,3,6,1,4,1,935,10,1,1,8,6,1,5),_UpsESpecialDayScheduleRestartTime_Type())
upsESpecialDayScheduleRestartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:upsESpecialDayScheduleRestartTime.setStatus(_A)
_UpsESystemMasterOffDelay_Type=Integer32
_UpsESystemMasterOffDelay_Object=MibScalar
upsESystemMasterOffDelay=_UpsESystemMasterOffDelay_Object((1,3,6,1,4,1,935,10,1,1,8,7),_UpsESystemMasterOffDelay_Type())
upsESystemMasterOffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemMasterOffDelay.setStatus(_A)
_UpsESystemMasterOnDelay_Type=Integer32
_UpsESystemMasterOnDelay_Object=MibScalar
upsESystemMasterOnDelay=_UpsESystemMasterOnDelay_Object((1,3,6,1,4,1,935,10,1,1,8,8),_UpsESystemMasterOnDelay_Type())
upsESystemMasterOnDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:upsESystemMasterOnDelay.setStatus(_A)
_UpsETrapControl_ObjectIdentity=ObjectIdentity
upsETrapControl=_UpsETrapControl_ObjectIdentity((1,3,6,1,4,1,935,10,1,1,9))
_UpsETrapsReceiversTable_Object=MibTable
upsETrapsReceiversTable=_UpsETrapsReceiversTable_Object((1,3,6,1,4,1,935,10,1,1,9,1))
if mibBuilder.loadTexts:upsETrapsReceiversTable.setStatus(_A)
_UpsETrapsReceiversEntry_Object=MibTableRow
upsETrapsReceiversEntry=_UpsETrapsReceiversEntry_Object((1,3,6,1,4,1,935,10,1,1,9,1,1))
upsETrapsReceiversEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:upsETrapsReceiversEntry.setStatus(_A)
_UpsETrapsReceiversIndex_Type=PositiveInteger
_UpsETrapsReceiversIndex_Object=MibTableColumn
upsETrapsReceiversIndex=_UpsETrapsReceiversIndex_Object((1,3,6,1,4,1,935,10,1,1,9,1,1,1),_UpsETrapsReceiversIndex_Type())
upsETrapsReceiversIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:upsETrapsReceiversIndex.setStatus(_A)
class _UpsETrapsReceiverAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,45))
_UpsETrapsReceiverAddress_Type.__name__=_E
_UpsETrapsReceiverAddress_Object=MibTableColumn
upsETrapsReceiverAddress=_UpsETrapsReceiverAddress_Object((1,3,6,1,4,1,935,10,1,1,9,1,1,2),_UpsETrapsReceiverAddress_Type())
upsETrapsReceiverAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:upsETrapsReceiverAddress.setStatus(_A)
class _UpsETrapReceiverCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsETrapReceiverCommunityString_Type.__name__=_E
_UpsETrapReceiverCommunityString_Object=MibTableColumn
upsETrapReceiverCommunityString=_UpsETrapReceiverCommunityString_Object((1,3,6,1,4,1,935,10,1,1,9,1,1,3),_UpsETrapReceiverCommunityString_Type())
upsETrapReceiverCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:upsETrapReceiverCommunityString.setStatus(_A)
class _UpsETrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('rfc1628Trap',2),('eppcTrap',3)))
_UpsETrapType_Type.__name__=_F
_UpsETrapType_Object=MibTableColumn
upsETrapType=_UpsETrapType_Object((1,3,6,1,4,1,935,10,1,1,9,1,1,4),_UpsETrapType_Type())
upsETrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:upsETrapType.setStatus(_A)
class _UpsETrapsSeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('informational',1),('warning',2),('severe',3)))
_UpsETrapsSeverityLevel_Type.__name__=_F
_UpsETrapsSeverityLevel_Object=MibTableColumn
upsETrapsSeverityLevel=_UpsETrapsSeverityLevel_Object((1,3,6,1,4,1,935,10,1,1,9,1,1,5),_UpsETrapsSeverityLevel_Type())
upsETrapsSeverityLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:upsETrapsSeverityLevel.setStatus(_A)
class _UpsETrapReceiverDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsETrapReceiverDescription_Type.__name__=_E
_UpsETrapReceiverDescription_Object=MibTableColumn
upsETrapReceiverDescription=_UpsETrapReceiverDescription_Object((1,3,6,1,4,1,935,10,1,1,9,1,1,6),_UpsETrapReceiverDescription_Type())
upsETrapReceiverDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:upsETrapReceiverDescription.setStatus(_A)
class _UpsETrapState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_UpsETrapState_Type.__name__=_E
_UpsETrapState_Object=MibScalar
upsETrapState=_UpsETrapState_Object((1,3,6,1,4,1,935,10,1,1,9,2),_UpsETrapState_Type())
upsETrapState.setMaxAccess(_B)
if mibBuilder.loadTexts:upsETrapState.setStatus(_A)
_UpsETraps_ObjectIdentity=ObjectIdentity
upsETraps=_UpsETraps_ObjectIdentity((1,3,6,1,4,1,935,10,1,2))
upsEPowerFail=NotificationType((1,3,6,1,4,1,935,10,1,2,0,1))
if mibBuilder.loadTexts:upsEPowerFail.setStatus('')
upsEPowerRestored=NotificationType((1,3,6,1,4,1,935,10,1,2,0,2))
if mibBuilder.loadTexts:upsEPowerRestored.setStatus('')
upsELowBattery=NotificationType((1,3,6,1,4,1,935,10,1,2,0,3))
if mibBuilder.loadTexts:upsELowBattery.setStatus('')
upsEReturnFromLowBattery=NotificationType((1,3,6,1,4,1,935,10,1,2,0,4))
if mibBuilder.loadTexts:upsEReturnFromLowBattery.setStatus('')
upsEFailed=NotificationType((1,3,6,1,4,1,935,10,1,2,0,5))
if mibBuilder.loadTexts:upsEFailed.setStatus('')
upsEOk=NotificationType((1,3,6,1,4,1,935,10,1,2,0,6))
if mibBuilder.loadTexts:upsEOk.setStatus('')
upsEOnBattery=NotificationType((1,3,6,1,4,1,935,10,1,2,0,7))
upsEOnBattery.setObjects(*((_C,_X),(_C,_AA)))
if mibBuilder.loadTexts:upsEOnBattery.setStatus('')
upsENotOnBattery=NotificationType((1,3,6,1,4,1,935,10,1,2,0,8))
if mibBuilder.loadTexts:upsENotOnBattery.setStatus('')
upsETestInProgress=NotificationType((1,3,6,1,4,1,935,10,1,2,0,9))
if mibBuilder.loadTexts:upsETestInProgress.setStatus('')
upsETestOver=NotificationType((1,3,6,1,4,1,935,10,1,2,0,10))
upsETestOver.setObjects(*((_C,_AB),(_C,_AC),(_C,_AD),(_C,_AE)))
if mibBuilder.loadTexts:upsETestOver.setStatus('')
upsEBypassOn=NotificationType((1,3,6,1,4,1,935,10,1,2,0,11))
if mibBuilder.loadTexts:upsEBypassOn.setStatus('')
upsEOnline=NotificationType((1,3,6,1,4,1,935,10,1,2,0,12))
if mibBuilder.loadTexts:upsEOnline.setStatus('')
upsECommunicationLost=NotificationType((1,3,6,1,4,1,935,10,1,2,0,13))
if mibBuilder.loadTexts:upsECommunicationLost.setStatus('')
upsECommunicationEstablished=NotificationType((1,3,6,1,4,1,935,10,1,2,0,14))
if mibBuilder.loadTexts:upsECommunicationEstablished.setStatus('')
upsEGoingShutdown=NotificationType((1,3,6,1,4,1,935,10,1,2,0,15))
if mibBuilder.loadTexts:upsEGoingShutdown.setStatus('')
upsEShutdownCancelled=NotificationType((1,3,6,1,4,1,935,10,1,2,0,16))
if mibBuilder.loadTexts:upsEShutdownCancelled.setStatus('')
upsEOutlet1GoingShutdown=NotificationType((1,3,6,1,4,1,935,10,1,2,0,17))
if mibBuilder.loadTexts:upsEOutlet1GoingShutdown.setStatus('')
upsEOutlet1ShutdownCancelled=NotificationType((1,3,6,1,4,1,935,10,1,2,0,18))
if mibBuilder.loadTexts:upsEOutlet1ShutdownCancelled.setStatus('')
upsEOutlet2GoingShutdown=NotificationType((1,3,6,1,4,1,935,10,1,2,0,19))
if mibBuilder.loadTexts:upsEOutlet2GoingShutdown.setStatus('')
upsEOutlet2ShutdownCancelled=NotificationType((1,3,6,1,4,1,935,10,1,2,0,20))
if mibBuilder.loadTexts:upsEOutlet2ShutdownCancelled.setStatus('')
upsESleeping=NotificationType((1,3,6,1,4,1,935,10,1,2,0,21))
upsESleeping.setObjects((_C,_AF))
if mibBuilder.loadTexts:upsESleeping.setStatus('')
upsEWokeUp=NotificationType((1,3,6,1,4,1,935,10,1,2,0,22))
if mibBuilder.loadTexts:upsEWokeUp.setStatus('')
upsEOverTemperature=NotificationType((1,3,6,1,4,1,935,10,1,2,0,23))
upsEOverTemperature.setObjects(*((_C,_Y),(_C,_Z)))
if mibBuilder.loadTexts:upsEOverTemperature.setStatus('')
upsENotOverTemperature=NotificationType((1,3,6,1,4,1,935,10,1,2,0,24))
upsENotOverTemperature.setObjects(*((_C,_Y),(_C,_Z)))
if mibBuilder.loadTexts:upsENotOverTemperature.setStatus('')
upsEOverLoad=NotificationType((1,3,6,1,4,1,935,10,1,2,0,25))
upsEOverLoad.setObjects(*((_C,_a),(_C,_b)))
if mibBuilder.loadTexts:upsEOverLoad.setStatus('')
upsENotOverLoad=NotificationType((1,3,6,1,4,1,935,10,1,2,0,26))
upsENotOverLoad.setObjects(*((_C,_a),(_C,_b)))
if mibBuilder.loadTexts:upsENotOverLoad.setStatus('')
upsEModuleInserted=NotificationType((1,3,6,1,4,1,935,10,1,2,0,27))
if mibBuilder.loadTexts:upsEModuleInserted.setStatus('')
upsEModuleRemoved=NotificationType((1,3,6,1,4,1,935,10,1,2,0,28))
if mibBuilder.loadTexts:upsEModuleRemoved.setStatus('')
sensorTemperatureTooHigh=NotificationType((1,3,6,1,4,1,935,10,1,2,0,29))
sensorTemperatureTooHigh.setObjects(*((_C,_c),(_C,_K)))
if mibBuilder.loadTexts:sensorTemperatureTooHigh.setStatus('')
sensorTemperatureNotHigh=NotificationType((1,3,6,1,4,1,935,10,1,2,0,30))
sensorTemperatureNotHigh.setObjects(*((_C,_c),(_C,_K)))
if mibBuilder.loadTexts:sensorTemperatureNotHigh.setStatus('')
sensorTemperatureTooLow=NotificationType((1,3,6,1,4,1,935,10,1,2,0,31))
sensorTemperatureTooLow.setObjects(*((_C,_d),(_C,_K)))
if mibBuilder.loadTexts:sensorTemperatureTooLow.setStatus('')
sensorTemperatureNotLow=NotificationType((1,3,6,1,4,1,935,10,1,2,0,32))
sensorTemperatureNotLow.setObjects(*((_C,_d),(_C,_K)))
if mibBuilder.loadTexts:sensorTemperatureNotLow.setStatus('')
sensorHumidityTooHigh=NotificationType((1,3,6,1,4,1,935,10,1,2,0,33))
sensorHumidityTooHigh.setObjects(*((_C,_e),(_C,_L)))
if mibBuilder.loadTexts:sensorHumidityTooHigh.setStatus('')
sensorHumidityNotHigh=NotificationType((1,3,6,1,4,1,935,10,1,2,0,34))
sensorHumidityNotHigh.setObjects(*((_C,_e),(_C,_L)))
if mibBuilder.loadTexts:sensorHumidityNotHigh.setStatus('')
sensorHumidityTooLow=NotificationType((1,3,6,1,4,1,935,10,1,2,0,35))
sensorHumidityTooLow.setObjects(*((_C,_f),(_C,_L)))
if mibBuilder.loadTexts:sensorHumidityTooLow.setStatus('')
sensorHumidityNotLow=NotificationType((1,3,6,1,4,1,935,10,1,2,0,36))
sensorHumidityNotLow.setObjects(*((_C,_f),(_C,_L)))
if mibBuilder.loadTexts:sensorHumidityNotLow.setStatus('')
contactAlarm1Active=NotificationType((1,3,6,1,4,1,935,10,1,2,0,37))
contactAlarm1Active.setObjects(*((_C,_M),(_C,_N)))
if mibBuilder.loadTexts:contactAlarm1Active.setStatus('')
concactAlarm1Normal=NotificationType((1,3,6,1,4,1,935,10,1,2,0,38))
concactAlarm1Normal.setObjects(*((_C,_M),(_C,_N)))
if mibBuilder.loadTexts:concactAlarm1Normal.setStatus('')
contactAlarm2Active=NotificationType((1,3,6,1,4,1,935,10,1,2,0,39))
contactAlarm2Active.setObjects(*((_C,_M),(_C,_N)))
if mibBuilder.loadTexts:contactAlarm2Active.setStatus('')
contactAlarm2Normal=NotificationType((1,3,6,1,4,1,935,10,1,2,0,40))
contactAlarm2Normal.setObjects(*((_C,_M),(_C,_N)))
if mibBuilder.loadTexts:contactAlarm2Normal.setStatus('')
upsEInternalwarning=NotificationType((1,3,6,1,4,1,935,10,1,2,0,41))
if mibBuilder.loadTexts:upsEInternalwarning.setStatus('')
upsEReturnFromInternalwarning=NotificationType((1,3,6,1,4,1,935,10,1,2,0,42))
if mibBuilder.loadTexts:upsEReturnFromInternalwarning.setStatus('')
upsEEPOActive=NotificationType((1,3,6,1,4,1,935,10,1,2,0,43))
if mibBuilder.loadTexts:upsEEPOActive.setStatus('')
upsEReturnFromEPOActive=NotificationType((1,3,6,1,4,1,935,10,1,2,0,44))
if mibBuilder.loadTexts:upsEReturnFromEPOActive.setStatus('')
upsEModuleUnlock=NotificationType((1,3,6,1,4,1,935,10,1,2,0,45))
if mibBuilder.loadTexts:upsEModuleUnlock.setStatus('')
upsEReturnFromModuleUnlock=NotificationType((1,3,6,1,4,1,935,10,1,2,0,46))
if mibBuilder.loadTexts:upsEReturnFromModuleUnlock.setStatus('')
upsEMain1Neutralloss=NotificationType((1,3,6,1,4,1,935,10,1,2,0,47))
if mibBuilder.loadTexts:upsEMain1Neutralloss.setStatus('')
upsEReturnFromMain1Neutralloss=NotificationType((1,3,6,1,4,1,935,10,1,2,0,48))
if mibBuilder.loadTexts:upsEReturnFromMain1Neutralloss.setStatus('')
upsEMain1phaseerror=NotificationType((1,3,6,1,4,1,935,10,1,2,0,49))
if mibBuilder.loadTexts:upsEMain1phaseerror.setStatus('')
upsEReturnFromMain1phaseerror=NotificationType((1,3,6,1,4,1,935,10,1,2,0,50))
if mibBuilder.loadTexts:upsEReturnFromMain1phaseerror.setStatus('')
upsESitefault=NotificationType((1,3,6,1,4,1,935,10,1,2,0,51))
if mibBuilder.loadTexts:upsESitefault.setStatus('')
upsEReturnFromSitefault=NotificationType((1,3,6,1,4,1,935,10,1,2,0,52))
if mibBuilder.loadTexts:upsEReturnFromSitefault.setStatus('')
upsEBypassAbnormal=NotificationType((1,3,6,1,4,1,935,10,1,2,0,53))
if mibBuilder.loadTexts:upsEBypassAbnormal.setStatus('')
upsEReturnFromBypassAbnormal=NotificationType((1,3,6,1,4,1,935,10,1,2,0,54))
if mibBuilder.loadTexts:upsEReturnFromBypassAbnormal.setStatus('')
upsEBypassPhaseError=NotificationType((1,3,6,1,4,1,935,10,1,2,0,55))
if mibBuilder.loadTexts:upsEBypassPhaseError.setStatus('')
upsEReturnFromBypassPhaseError=NotificationType((1,3,6,1,4,1,935,10,1,2,0,56))
if mibBuilder.loadTexts:upsEReturnFromBypassPhaseError.setStatus('')
upsEBatteryOpen=NotificationType((1,3,6,1,4,1,935,10,1,2,0,57))
if mibBuilder.loadTexts:upsEBatteryOpen.setStatus('')
upsEReturnFromBatteryOpen=NotificationType((1,3,6,1,4,1,935,10,1,2,0,58))
if mibBuilder.loadTexts:upsEReturnFromBatteryOpen.setStatus('')
upsEBatteryOverCharge=NotificationType((1,3,6,1,4,1,935,10,1,2,0,59))
if mibBuilder.loadTexts:upsEBatteryOverCharge.setStatus('')
upsEReturnFromBatteryOverCharge=NotificationType((1,3,6,1,4,1,935,10,1,2,0,60))
if mibBuilder.loadTexts:upsEReturnFromBatteryOverCharge.setStatus('')
upsEBatteryReverse=NotificationType((1,3,6,1,4,1,935,10,1,2,0,61))
if mibBuilder.loadTexts:upsEBatteryReverse.setStatus('')
upsEReturnFromBatteryReverse=NotificationType((1,3,6,1,4,1,935,10,1,2,0,62))
if mibBuilder.loadTexts:upsEReturnFromBatteryReverse.setStatus('')
upsEOverloadforewarning=NotificationType((1,3,6,1,4,1,935,10,1,2,0,63))
if mibBuilder.loadTexts:upsEOverloadforewarning.setStatus('')
upsEReturnFromOverloadforewarning=NotificationType((1,3,6,1,4,1,935,10,1,2,0,64))
if mibBuilder.loadTexts:upsEReturnFromOverloadforewarning.setStatus('')
upsEOverloadWarning=NotificationType((1,3,6,1,4,1,935,10,1,2,0,65))
if mibBuilder.loadTexts:upsEOverloadWarning.setStatus('')
upsEReturnFromOverloadWarning=NotificationType((1,3,6,1,4,1,935,10,1,2,0,66))
if mibBuilder.loadTexts:upsEReturnFromOverloadWarning.setStatus('')
upsEFanLock=NotificationType((1,3,6,1,4,1,935,10,1,2,0,67))
if mibBuilder.loadTexts:upsEFanLock.setStatus('')
upsEReturnFromFanLock=NotificationType((1,3,6,1,4,1,935,10,1,2,0,68))
if mibBuilder.loadTexts:upsEReturnFromFanLock.setStatus('')
upsEMaintaincoverisopen=NotificationType((1,3,6,1,4,1,935,10,1,2,0,69))
if mibBuilder.loadTexts:upsEMaintaincoverisopen.setStatus('')
upsEReturnFromMaintaincoverisopen=NotificationType((1,3,6,1,4,1,935,10,1,2,0,70))
if mibBuilder.loadTexts:upsEReturnFromMaintaincoverisopen.setStatus('')
upsEChargerfault=NotificationType((1,3,6,1,4,1,935,10,1,2,0,71))
if mibBuilder.loadTexts:upsEChargerfault.setStatus('')
upsEReturnFromChargerfault=NotificationType((1,3,6,1,4,1,935,10,1,2,0,72))
if mibBuilder.loadTexts:upsEReturnFromChargerfault.setStatus('')
upsEModulelocationerror=NotificationType((1,3,6,1,4,1,935,10,1,2,0,73))
if mibBuilder.loadTexts:upsEModulelocationerror.setStatus('')
upsEReturnFromModulelocationerror=NotificationType((1,3,6,1,4,1,935,10,1,2,0,74))
if mibBuilder.loadTexts:upsEReturnFromModulelocationerror.setStatus('')
upsETurnonabnormal=NotificationType((1,3,6,1,4,1,935,10,1,2,0,75))
if mibBuilder.loadTexts:upsETurnonabnormal.setStatus('')
upsEReturnFromTurnonabnormal=NotificationType((1,3,6,1,4,1,935,10,1,2,0,76))
if mibBuilder.loadTexts:upsEReturnFromTurnonabnormal.setStatus('')
upsERedundancyloss=NotificationType((1,3,6,1,4,1,935,10,1,2,0,77))
if mibBuilder.loadTexts:upsERedundancyloss.setStatus('')
upsEReturnFromRedundancyloss=NotificationType((1,3,6,1,4,1,935,10,1,2,0,78))
if mibBuilder.loadTexts:upsEReturnFromRedundancyloss.setStatus('')
upsEHotSwapActived=NotificationType((1,3,6,1,4,1,935,10,1,2,0,79))
if mibBuilder.loadTexts:upsEHotSwapActived.setStatus('')
upsEReturnFromHotSwapActived=NotificationType((1,3,6,1,4,1,935,10,1,2,0,80))
if mibBuilder.loadTexts:upsEReturnFromHotSwapActived.setStatus('')
upsEBatteryInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,81))
if mibBuilder.loadTexts:upsEBatteryInform.setStatus('')
upsEReturnFromBatteryInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,82))
if mibBuilder.loadTexts:upsEReturnFromBatteryInform.setStatus('')
upsEInspectionInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,83))
if mibBuilder.loadTexts:upsEInspectionInform.setStatus('')
upsEReturnFromInspectionInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,84))
if mibBuilder.loadTexts:upsEReturnFromInspectionInform.setStatus('')
upsEGuaranteeInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,85))
if mibBuilder.loadTexts:upsEGuaranteeInform.setStatus('')
upsEReturnFromGuaranteeInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,86))
if mibBuilder.loadTexts:upsEReturnFromGuaranteeInform.setStatus('')
upsETemperatureLow=NotificationType((1,3,6,1,4,1,935,10,1,2,0,87))
if mibBuilder.loadTexts:upsETemperatureLow.setStatus('')
upsEReturnFromTemperatureLow=NotificationType((1,3,6,1,4,1,935,10,1,2,0,88))
if mibBuilder.loadTexts:upsEReturnFromTemperatureLow.setStatus('')
upsETemperatureHigh=NotificationType((1,3,6,1,4,1,935,10,1,2,0,89))
if mibBuilder.loadTexts:upsETemperatureHigh.setStatus('')
upsEReturnFromTemperatureHigh=NotificationType((1,3,6,1,4,1,935,10,1,2,0,90))
if mibBuilder.loadTexts:upsEReturnFromTemperatureHigh.setStatus('')
upsEBatteryOverTemperature=NotificationType((1,3,6,1,4,1,935,10,1,2,0,91))
if mibBuilder.loadTexts:upsEBatteryOverTemperature.setStatus('')
upsEReturnFromBatteryOverTemperature=NotificationType((1,3,6,1,4,1,935,10,1,2,0,92))
if mibBuilder.loadTexts:upsEReturnFromBatteryOverTemperature.setStatus('')
upsEFanMaintainInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,93))
if mibBuilder.loadTexts:upsEFanMaintainInform.setStatus('')
upsEReturnFromFanMaintainInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,94))
if mibBuilder.loadTexts:upsEReturnFromFanMaintainInform.setStatus('')
upsEBusCapacitanceMaintainInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,95))
if mibBuilder.loadTexts:upsEBusCapacitanceMaintainInform.setStatus('')
upsEReturnFromBusCapacitanceMaintainInform=NotificationType((1,3,6,1,4,1,935,10,1,2,0,96))
if mibBuilder.loadTexts:upsEReturnFromBusCapacitanceMaintainInform.setStatus('')
upsESystemOverCapacity=NotificationType((1,3,6,1,4,1,935,10,1,2,0,97))
if mibBuilder.loadTexts:upsESystemOverCapacity.setStatus('')
upsEReturnFromSystemOverCapacity=NotificationType((1,3,6,1,4,1,935,10,1,2,0,98))
if mibBuilder.loadTexts:upsEReturnFromSystemOverCapacity.setStatus('')
upsEBelowCapacityLimit=NotificationType((1,3,6,1,4,1,935,10,1,2,0,123))
upsEBelowCapacityLimit.setObjects(*((_C,_AG),(_C,_AH)))
if mibBuilder.loadTexts:upsEBelowCapacityLimit.setStatus('')
upsENotBelowCapacityLimit=NotificationType((1,3,6,1,4,1,935,10,1,2,0,124))
if mibBuilder.loadTexts:upsENotBelowCapacityLimit.setStatus('')
upsEBelowRemainTimeLimit=NotificationType((1,3,6,1,4,1,935,10,1,2,0,125))
upsEBelowRemainTimeLimit.setObjects(*((_C,_X),(_C,_AI)))
if mibBuilder.loadTexts:upsEBelowRemainTimeLimit.setStatus('')
upsENotBelowRemainTimeLimit=NotificationType((1,3,6,1,4,1,935,10,1,2,0,126))
if mibBuilder.loadTexts:upsENotBelowRemainTimeLimit.setStatus('')
upsELoadSegment1Off=NotificationType((1,3,6,1,4,1,935,10,1,2,0,127))
if mibBuilder.loadTexts:upsELoadSegment1Off.setStatus('')
upsELoadSegment1On=NotificationType((1,3,6,1,4,1,935,10,1,2,0,128))
if mibBuilder.loadTexts:upsELoadSegment1On.setStatus('')
upsELoadSegment2Off=NotificationType((1,3,6,1,4,1,935,10,1,2,0,129))
if mibBuilder.loadTexts:upsELoadSegment2Off.setStatus('')
upsELoadSegment2On=NotificationType((1,3,6,1,4,1,935,10,1,2,0,130))
if mibBuilder.loadTexts:upsELoadSegment2On.setStatus('')
mibBuilder.exportSymbols(_C,**{'ppc':ppc,'device':device,'upsAgent':upsAgent,'upsE':upsE,'upsEIdentity':upsEIdentity,'upsEIdentityManufacturer':upsEIdentityManufacturer,'upsEIdentityModel':upsEIdentityModel,'upsEIdentityUPSFirmwareVerison':upsEIdentityUPSFirmwareVerison,'upsEIndentityUPSSerialNumber':upsEIndentityUPSSerialNumber,'upsEIdentityDescription':upsEIdentityDescription,'upsEIdentityAgentSoftwareVerison':upsEIdentityAgentSoftwareVerison,'upsEIdentityAttachedDevices':upsEIdentityAttachedDevices,'upsESystemSummary':upsESystemSummary,'upsESystemStatus':upsESystemStatus,_Y:upsESystemTemperature,'upsESystemWarningCode':upsESystemWarningCode,'upsESystemFaultCode':upsESystemFaultCode,'upsESystemConfigInputVoltage':upsESystemConfigInputVoltage,'upsESystemConfigInputFrequence':upsESystemConfigInputFrequence,'upsESystemConfigOutputVoltage':upsESystemConfigOutputVoltage,'upsESystemConfigOutputFrequency':upsESystemConfigOutputFrequency,'upsESystemConfigOutputVA':upsESystemConfigOutputVA,'upsESystemConfigOutputPower':upsESystemConfigOutputPower,_b:upsESystemConfigOutputLoadHighSetPoint,_Z:upsESystemConfigOverTemperatureSetPoint,'upsESystemInputSourceNum':upsESystemInputSourceNum,'upsESystemInputLineBads':upsESystemInputLineBads,'upsESystemInputNumPhases':upsESystemInputNumPhases,'upsESystemInputTable':upsESystemInputTable,'upsESystemInputEntry':upsESystemInputEntry,_p:upsESystemInputPhase,'upsESystemInputFrequency':upsESystemInputFrequency,'upsESystemInputVoltage':upsESystemInputVoltage,'upsESystemInputCurrent':upsESystemInputCurrent,'upsESystemInputWatts':upsESystemInputWatts,'upsESystemOutputNumPhase':upsESystemOutputNumPhase,'upsESystemOutputTable':upsESystemOutputTable,'upsESystemOutputEntry':upsESystemOutputEntry,_q:upsESystemOutputPhase,'upsESystemOutputFrequency':upsESystemOutputFrequency,'upsESystemOutputVoltage':upsESystemOutputVoltage,'upsESystemOutputCurrent':upsESystemOutputCurrent,'upsESystemOutputWatts':upsESystemOutputWatts,'upsESystemOutputVA':upsESystemOutputVA,_a:upsESystemOutputLoad,'upsESystemBypassNumPhase':upsESystemBypassNumPhase,'upsESystemBypassTable':upsESystemBypassTable,'upsESystemBypassEntry':upsESystemBypassEntry,_r:upsESystemBypassPhase,'upsESystemBypassFrequency':upsESystemBypassFrequency,'upsESystemBypassVoltage':upsESystemBypassVoltage,'upsESystemBypassCurrent':upsESystemBypassCurrent,'upsESystemBypassWatts':upsESystemBypassWatts,_AH:upsESystemConfigBelowCapacityLimit,_AI:upsESystemConfigBelowRemainTimeLimit,'upsEBatterySystem':upsEBatterySystem,'upsEBatteryStatus':upsEBatteryStatus,_AA:upsESecondsOnBattery,_X:upsEBatteryEstimatedMinutesRemaining,_AG:upsEBatteryEstimatedChargeRemaining,'upsEPositiveBatteryVoltage':upsEPositiveBatteryVoltage,'upsENegativeBatteryVoltage':upsENegativeBatteryVoltage,'upsEBatteryCellNumber':upsEBatteryCellNumber,'upsEBatteryTemperature':upsEBatteryTemperature,'upsEBatteryLastReplacedDate':upsEBatteryLastReplacedDate,'upsEBatteryABMStatus':upsEBatteryABMStatus,'upsEChargerModulesNum':upsEChargerModulesNum,'upsEChargerModulesTable':upsEChargerModulesTable,'upsEChargerModulesEntry':upsEChargerModulesEntry,_u:chargerModulesNum,'chargerModulesAddress':chargerModulesAddress,'positiveChargeVotlage':positiveChargeVotlage,'negativeChargeVoltage':negativeChargeVoltage,'positiveChargeCurrent':positiveChargeCurrent,'negativeChargeCurrent':negativeChargeCurrent,'chargerModulesTemperature':chargerModulesTemperature,'chargerModulesMode':chargerModulesMode,'upsEPowerConverterSystem':upsEPowerConverterSystem,'upsEUPSModulesNum':upsEUPSModulesNum,'upsEModulesTable':upsEModulesTable,'upsEModulesEntry':upsEModulesEntry,_v:upsEModulesNum,'upsEModuleAddress':upsEModuleAddress,'upsEModulePositiveBusVolt':upsEModulePositiveBusVolt,'upsEModuleNegativeBusVolt':upsEModuleNegativeBusVolt,'upsEModuleTemperature':upsEModuleTemperature,'upsEModuleWorkingMode':upsEModuleWorkingMode,'upsEModuleOutputCurrentR':upsEModuleOutputCurrentR,'upsEModuleOutputWattR':upsEModuleOutputWattR,'upsEModuleOutputLoadR':upsEModuleOutputLoadR,'upsEModuleWarningCode':upsEModuleWarningCode,'upsEModuleFaultCode':upsEModuleFaultCode,'upsEModuleTrapState':upsEModuleTrapState,'upsEModuleConfigOutputVA':upsEModuleConfigOutputVA,'upsEModuleOutputCurrentS':upsEModuleOutputCurrentS,'upsEModuleOutputCurrentT':upsEModuleOutputCurrentT,'upsEModuleOutputWattS':upsEModuleOutputWattS,'upsEModuleOutputWattT':upsEModuleOutputWattT,'upsEModuleOutputLoadS':upsEModuleOutputLoadS,'upsEModuleOutputLoadT':upsEModuleOutputLoadT,'upsEModuleOutputVAR':upsEModuleOutputVAR,'upsEModuleOutputVAS':upsEModuleOutputVAS,'upsEModuleOutputVAT':upsEModuleOutputVAT,'upsELoadSegment':upsELoadSegment,'upsELoadSegment1OffDelay':upsELoadSegment1OffDelay,'upsELoadSegment1OnDelay':upsELoadSegment1OnDelay,'upsELoadSegment1AutoOffTimer':upsELoadSegment1AutoOffTimer,'upsELoadSegment1AutoOnTimer':upsELoadSegment1AutoOnTimer,'upsELoadSegment1State':upsELoadSegment1State,'upsELoadSegment2OffDelay':upsELoadSegment2OffDelay,'upsELoadSegment2OnDelay':upsELoadSegment2OnDelay,'upsELoadSegment2AutoOffTimer':upsELoadSegment2AutoOffTimer,'upsELoadSegment2AutoOnTimer':upsELoadSegment2AutoOnTimer,'upsELoadSegment2State':upsELoadSegment2State,'upsEEnvironment':upsEEnvironment,'upsEEnvironmentTemperature':upsEEnvironmentTemperature,_K:upsEEnvironmentCurrentTemperature,_c:upsEEnvironmentTemperatureHighSetPoint,'upsEEnvironmentTemperatureHighStatus':upsEEnvironmentTemperatureHighStatus,_d:upsEEnvironmentTemperatureLowSetPoint,'upsEEnvironmentTemperatureLowStatus':upsEEnvironmentTemperatureLowStatus,'upsEEnvironmentTemperatureOffset':upsEEnvironmentTemperatureOffset,'upsEEnvironmentHumidity':upsEEnvironmentHumidity,_L:upsEEnvironmentCurrentHumidity,_e:upsEEnvironmentHumidityHighSetPoint,'upsEEnvironmentHumidityHighStatus':upsEEnvironmentHumidityHighStatus,_f:upsEEnvironmentHumidityLowSetPoint,'upsEEnvironmentHumidityLowStatus':upsEEnvironmentHumidityLowStatus,'upsEEnvironmentHumidityOffset':upsEEnvironmentHumidityOffset,'upsEEnvironmentContactsNum':upsEEnvironmentContactsNum,'upsEEnvironmentContactTable':upsEEnvironmentContactTable,'upsEEnvironmentContactEntry':upsEEnvironmentContactEntry,_z:upsEEnvironmentContactIndex,_M:upsEEnvironmentContactType,'upsEEnvironmentContactState':upsEEnvironmentContactState,_N:upsEEnvironmentContactDescription,'upsEBatteryTest':upsEBatteryTest,_AB:upsEBatteryTestStart,_AC:upsEBatteryTestSettingTime,_AD:upsEBatteryTestResult,_AE:upsEBatteryTestStartTime,'upsEBatteryTestElapsedTime':upsEBatteryTestElapsedTime,'upsEBatteryTestScheduleTable':upsEBatteryTestScheduleTable,'upsEBatteryTestScheduleEntry':upsEBatteryTestScheduleEntry,_A2:upsEBatteryTestScheduleIndex,'upsEBatteryTestScheduleDay':upsEBatteryTestScheduleDay,'upsEBatteryTestScheduleTime':upsEBatteryTestScheduleTime,'upsEBatteryTestScheduleType':upsEBatteryTestScheduleType,'upsEBatteryTestScheduleTestWithTime':upsEBatteryTestScheduleTestWithTime,'upsEBatteryTestScheduleSpecialDay':upsEBatteryTestScheduleSpecialDay,'upsEControl':upsEControl,'upsEControlOutputOffDelay':upsEControlOutputOffDelay,_AF:upsEControlOutputOnDelay,'upsEControlOutputOnOffControl':upsEControlOutputOnOffControl,'upsEShutdownEventsTable':upsEShutdownEventsTable,'upsEShutdownEventsEntry':upsEShutdownEventsEntry,_A3:upsEShutdownEvent,'upsEShutdownEventAction':upsEShutdownEventAction,'upsEShutdownwarningPeriodTime':upsEShutdownwarningPeriodTime,'upsEShutdownWarningPeriodInterval':upsEShutdownWarningPeriodInterval,'upsEControlWeeklyScheduleTable':upsEControlWeeklyScheduleTable,'upsEControlWeeklyScheduleEntry':upsEControlWeeklyScheduleEntry,_A6:upsEControlWeeklyScheduleIndex,'upsEWeeklyScheduleShutdownDay':upsEWeeklyScheduleShutdownDay,'upsEWeeklyScheduleShutdownTime':upsEWeeklyScheduleShutdownTime,'upsEWeeklyScheduleRestartDay':upsEWeeklyScheduleRestartDay,'upsEWeeklyScheduleRestartTime':upsEWeeklyScheduleRestartTime,'upsEControlSpecialDayScheduleTable':upsEControlSpecialDayScheduleTable,'upsEControlSpecialDayScheduleEntry':upsEControlSpecialDayScheduleEntry,_A8:upsEControlSpecialDayScheduleIndex,'upsESpecialDayScheduleShutdownDay':upsESpecialDayScheduleShutdownDay,'upsESpecialDayScheduleShutdownTime':upsESpecialDayScheduleShutdownTime,'upsESpecialDayScheduleRestartDay':upsESpecialDayScheduleRestartDay,'upsESpecialDayScheduleRestartTime':upsESpecialDayScheduleRestartTime,'upsESystemMasterOffDelay':upsESystemMasterOffDelay,'upsESystemMasterOnDelay':upsESystemMasterOnDelay,'upsETrapControl':upsETrapControl,'upsETrapsReceiversTable':upsETrapsReceiversTable,'upsETrapsReceiversEntry':upsETrapsReceiversEntry,_A9:upsETrapsReceiversIndex,'upsETrapsReceiverAddress':upsETrapsReceiverAddress,'upsETrapReceiverCommunityString':upsETrapReceiverCommunityString,'upsETrapType':upsETrapType,'upsETrapsSeverityLevel':upsETrapsSeverityLevel,'upsETrapReceiverDescription':upsETrapReceiverDescription,'upsETrapState':upsETrapState,'upsETraps':upsETraps,'upsEPowerFail':upsEPowerFail,'upsEPowerRestored':upsEPowerRestored,'upsELowBattery':upsELowBattery,'upsEReturnFromLowBattery':upsEReturnFromLowBattery,'upsEFailed':upsEFailed,'upsEOk':upsEOk,'upsEOnBattery':upsEOnBattery,'upsENotOnBattery':upsENotOnBattery,'upsETestInProgress':upsETestInProgress,'upsETestOver':upsETestOver,'upsEBypassOn':upsEBypassOn,'upsEOnline':upsEOnline,'upsECommunicationLost':upsECommunicationLost,'upsECommunicationEstablished':upsECommunicationEstablished,'upsEGoingShutdown':upsEGoingShutdown,'upsEShutdownCancelled':upsEShutdownCancelled,'upsEOutlet1GoingShutdown':upsEOutlet1GoingShutdown,'upsEOutlet1ShutdownCancelled':upsEOutlet1ShutdownCancelled,'upsEOutlet2GoingShutdown':upsEOutlet2GoingShutdown,'upsEOutlet2ShutdownCancelled':upsEOutlet2ShutdownCancelled,'upsESleeping':upsESleeping,'upsEWokeUp':upsEWokeUp,_A5:upsEOverTemperature,'upsENotOverTemperature':upsENotOverTemperature,_A4:upsEOverLoad,'upsENotOverLoad':upsENotOverLoad,'upsEModuleInserted':upsEModuleInserted,'upsEModuleRemoved':upsEModuleRemoved,'sensorTemperatureTooHigh':sensorTemperatureTooHigh,'sensorTemperatureNotHigh':sensorTemperatureNotHigh,'sensorTemperatureTooLow':sensorTemperatureTooLow,'sensorTemperatureNotLow':sensorTemperatureNotLow,'sensorHumidityTooHigh':sensorHumidityTooHigh,'sensorHumidityNotHigh':sensorHumidityNotHigh,'sensorHumidityTooLow':sensorHumidityTooLow,'sensorHumidityNotLow':sensorHumidityNotLow,'contactAlarm1Active':contactAlarm1Active,'concactAlarm1Normal':concactAlarm1Normal,'contactAlarm2Active':contactAlarm2Active,'contactAlarm2Normal':contactAlarm2Normal,'upsEInternalwarning':upsEInternalwarning,'upsEReturnFromInternalwarning':upsEReturnFromInternalwarning,'upsEEPOActive':upsEEPOActive,'upsEReturnFromEPOActive':upsEReturnFromEPOActive,'upsEModuleUnlock':upsEModuleUnlock,'upsEReturnFromModuleUnlock':upsEReturnFromModuleUnlock,'upsEMain1Neutralloss':upsEMain1Neutralloss,'upsEReturnFromMain1Neutralloss':upsEReturnFromMain1Neutralloss,'upsEMain1phaseerror':upsEMain1phaseerror,'upsEReturnFromMain1phaseerror':upsEReturnFromMain1phaseerror,'upsESitefault':upsESitefault,'upsEReturnFromSitefault':upsEReturnFromSitefault,'upsEBypassAbnormal':upsEBypassAbnormal,'upsEReturnFromBypassAbnormal':upsEReturnFromBypassAbnormal,'upsEBypassPhaseError':upsEBypassPhaseError,'upsEReturnFromBypassPhaseError':upsEReturnFromBypassPhaseError,'upsEBatteryOpen':upsEBatteryOpen,'upsEReturnFromBatteryOpen':upsEReturnFromBatteryOpen,'upsEBatteryOverCharge':upsEBatteryOverCharge,'upsEReturnFromBatteryOverCharge':upsEReturnFromBatteryOverCharge,'upsEBatteryReverse':upsEBatteryReverse,'upsEReturnFromBatteryReverse':upsEReturnFromBatteryReverse,'upsEOverloadforewarning':upsEOverloadforewarning,'upsEReturnFromOverloadforewarning':upsEReturnFromOverloadforewarning,'upsEOverloadWarning':upsEOverloadWarning,'upsEReturnFromOverloadWarning':upsEReturnFromOverloadWarning,'upsEFanLock':upsEFanLock,'upsEReturnFromFanLock':upsEReturnFromFanLock,'upsEMaintaincoverisopen':upsEMaintaincoverisopen,'upsEReturnFromMaintaincoverisopen':upsEReturnFromMaintaincoverisopen,'upsEChargerfault':upsEChargerfault,'upsEReturnFromChargerfault':upsEReturnFromChargerfault,'upsEModulelocationerror':upsEModulelocationerror,'upsEReturnFromModulelocationerror':upsEReturnFromModulelocationerror,'upsETurnonabnormal':upsETurnonabnormal,'upsEReturnFromTurnonabnormal':upsEReturnFromTurnonabnormal,'upsERedundancyloss':upsERedundancyloss,'upsEReturnFromRedundancyloss':upsEReturnFromRedundancyloss,'upsEHotSwapActived':upsEHotSwapActived,'upsEReturnFromHotSwapActived':upsEReturnFromHotSwapActived,'upsEBatteryInform':upsEBatteryInform,'upsEReturnFromBatteryInform':upsEReturnFromBatteryInform,'upsEInspectionInform':upsEInspectionInform,'upsEReturnFromInspectionInform':upsEReturnFromInspectionInform,'upsEGuaranteeInform':upsEGuaranteeInform,'upsEReturnFromGuaranteeInform':upsEReturnFromGuaranteeInform,'upsETemperatureLow':upsETemperatureLow,'upsEReturnFromTemperatureLow':upsEReturnFromTemperatureLow,'upsETemperatureHigh':upsETemperatureHigh,'upsEReturnFromTemperatureHigh':upsEReturnFromTemperatureHigh,'upsEBatteryOverTemperature':upsEBatteryOverTemperature,'upsEReturnFromBatteryOverTemperature':upsEReturnFromBatteryOverTemperature,'upsEFanMaintainInform':upsEFanMaintainInform,'upsEReturnFromFanMaintainInform':upsEReturnFromFanMaintainInform,'upsEBusCapacitanceMaintainInform':upsEBusCapacitanceMaintainInform,'upsEReturnFromBusCapacitanceMaintainInform':upsEReturnFromBusCapacitanceMaintainInform,'upsESystemOverCapacity':upsESystemOverCapacity,'upsEReturnFromSystemOverCapacity':upsEReturnFromSystemOverCapacity,'upsEBelowCapacityLimit':upsEBelowCapacityLimit,'upsENotBelowCapacityLimit':upsENotBelowCapacityLimit,'upsEBelowRemainTimeLimit':upsEBelowRemainTimeLimit,'upsENotBelowRemainTimeLimit':upsENotBelowRemainTimeLimit,'upsELoadSegment1Off':upsELoadSegment1Off,'upsELoadSegment1On':upsELoadSegment1On,'upsELoadSegment2Off':upsELoadSegment2Off,'upsELoadSegment2On':upsELoadSegment2On})