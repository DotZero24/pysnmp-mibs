_N='vpwrTrapIpIndex'
_M='sysAlarmIndex'
_L='vpwrAlarmIndex'
_K='vpwrBatteryTempIndex'
_J='vpwrModuleIndex'
_I='vpwrShelfIndex'
_H='degrees Centigrade'
_G='Integer32'
_F='DisplayString'
_E='vpwrTrapsMsgString'
_D='read-write'
_C='read-only'
_B='VPWR-DC-POWER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysUpTime,=mibBuilder.importSymbols('SNMPv2-MIB','sysUpTime')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TestAndIncr,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_F,'PhysAddress','TextualConvention','TestAndIncr','TimeInterval','TimeStamp')
valereDcPowerMgt=ModuleIdentity((1,3,6,1,4,1,13858))
class PositiveInteger(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NonNegativeInteger(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VpwrDcPowerProducts_ObjectIdentity=ObjectIdentity
vpwrDcPowerProducts=_VpwrDcPowerProducts_ObjectIdentity((1,3,6,1,4,1,13858,1))
_VpwrDcPowerSystem_ObjectIdentity=ObjectIdentity
vpwrDcPowerSystem=_VpwrDcPowerSystem_ObjectIdentity((1,3,6,1,4,1,13858,2))
_VpwrSystemIdentGroup_ObjectIdentity=ObjectIdentity
vpwrSystemIdentGroup=_VpwrSystemIdentGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,1))
class _VpwrIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_VpwrIdentManufacturer_Type.__name__=_F
_VpwrIdentManufacturer_Object=MibScalar
vpwrIdentManufacturer=_VpwrIdentManufacturer_Object((1,3,6,1,4,1,13858,2,1,1),_VpwrIdentManufacturer_Type())
vpwrIdentManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrIdentManufacturer.setStatus(_A)
class _VpwrIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VpwrIdentModel_Type.__name__=_F
_VpwrIdentModel_Object=MibScalar
vpwrIdentModel=_VpwrIdentModel_Object((1,3,6,1,4,1,13858,2,1,2),_VpwrIdentModel_Type())
vpwrIdentModel.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrIdentModel.setStatus(_A)
class _VpwrIdentControllerVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VpwrIdentControllerVersion_Type.__name__=_F
_VpwrIdentControllerVersion_Object=MibScalar
vpwrIdentControllerVersion=_VpwrIdentControllerVersion_Object((1,3,6,1,4,1,13858,2,1,3),_VpwrIdentControllerVersion_Type())
vpwrIdentControllerVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrIdentControllerVersion.setStatus(_A)
class _VpwrIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VpwrIdentAgentSoftwareVersion_Type.__name__=_F
_VpwrIdentAgentSoftwareVersion_Object=MibScalar
vpwrIdentAgentSoftwareVersion=_VpwrIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,13858,2,1,4),_VpwrIdentAgentSoftwareVersion_Type())
vpwrIdentAgentSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrIdentAgentSoftwareVersion.setStatus(_A)
class _VpwrIdentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_VpwrIdentName_Type.__name__=_F
_VpwrIdentName_Object=MibScalar
vpwrIdentName=_VpwrIdentName_Object((1,3,6,1,4,1,13858,2,1,5),_VpwrIdentName_Type())
vpwrIdentName.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrIdentName.setStatus(_A)
_VpwrSystemIdentTable_Object=MibTable
vpwrSystemIdentTable=_VpwrSystemIdentTable_Object((1,3,6,1,4,1,13858,2,1,6))
if mibBuilder.loadTexts:vpwrSystemIdentTable.setStatus(_A)
_VpwrSystemIdentEntry_Object=MibTableRow
vpwrSystemIdentEntry=_VpwrSystemIdentEntry_Object((1,3,6,1,4,1,13858,2,1,6,1))
vpwrSystemIdentEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:vpwrSystemIdentEntry.setStatus(_A)
_VpwrShelfIndex_Type=PositiveInteger
_VpwrShelfIndex_Object=MibTableColumn
vpwrShelfIndex=_VpwrShelfIndex_Object((1,3,6,1,4,1,13858,2,1,6,1,1),_VpwrShelfIndex_Type())
vpwrShelfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrShelfIndex.setStatus(_A)
_VpwrModuleIndex_Type=PositiveInteger
_VpwrModuleIndex_Object=MibTableColumn
vpwrModuleIndex=_VpwrModuleIndex_Object((1,3,6,1,4,1,13858,2,1,6,1,2),_VpwrModuleIndex_Type())
vpwrModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrModuleIndex.setStatus(_A)
_VpwrModuleOID_Type=ObjectIdentifier
_VpwrModuleOID_Object=MibTableColumn
vpwrModuleOID=_VpwrModuleOID_Object((1,3,6,1,4,1,13858,2,1,6,1,3),_VpwrModuleOID_Type())
vpwrModuleOID.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrModuleOID.setStatus(_A)
_VpwrModuleParameter_Type=Integer32
_VpwrModuleParameter_Object=MibTableColumn
vpwrModuleParameter=_VpwrModuleParameter_Object((1,3,6,1,4,1,13858,2,1,6,1,4),_VpwrModuleParameter_Type())
vpwrModuleParameter.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrModuleParameter.setStatus(_A)
class _VpwrModuleOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('moduleStatusOK',0),('moduleStatusAlarm',1)))
_VpwrModuleOperStatus_Type.__name__=_G
_VpwrModuleOperStatus_Object=MibTableColumn
vpwrModuleOperStatus=_VpwrModuleOperStatus_Object((1,3,6,1,4,1,13858,2,1,6,1,5),_VpwrModuleOperStatus_Type())
vpwrModuleOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrModuleOperStatus.setStatus(_A)
_VpwrModuleCapacity_Type=Integer32
_VpwrModuleCapacity_Object=MibTableColumn
vpwrModuleCapacity=_VpwrModuleCapacity_Object((1,3,6,1,4,1,13858,2,1,6,1,6),_VpwrModuleCapacity_Type())
vpwrModuleCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrModuleCapacity.setStatus(_A)
_VpwrSystemConfigGroup_ObjectIdentity=ObjectIdentity
vpwrSystemConfigGroup=_VpwrSystemConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,2))
class _VpwrSystemTempCompensation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('tempCompDisabled',0),('tempCompEnabled',1)))
_VpwrSystemTempCompensation_Type.__name__=_G
_VpwrSystemTempCompensation_Object=MibScalar
vpwrSystemTempCompensation=_VpwrSystemTempCompensation_Object((1,3,6,1,4,1,13858,2,2,1),_VpwrSystemTempCompensation_Type())
vpwrSystemTempCompensation.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemTempCompensation.setStatus(_A)
class _VpwrSystemTempCompStartTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,60))
_VpwrSystemTempCompStartTemperature_Type.__name__=_G
_VpwrSystemTempCompStartTemperature_Object=MibScalar
vpwrSystemTempCompStartTemperature=_VpwrSystemTempCompStartTemperature_Object((1,3,6,1,4,1,13858,2,2,2),_VpwrSystemTempCompStartTemperature_Type())
vpwrSystemTempCompStartTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemTempCompStartTemperature.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemTempCompStartTemperature.setUnits(_H)
_VpwrSystemTempCompStopVoltage_Type=Integer32
_VpwrSystemTempCompStopVoltage_Object=MibScalar
vpwrSystemTempCompStopVoltage=_VpwrSystemTempCompStopVoltage_Object((1,3,6,1,4,1,13858,2,2,3),_VpwrSystemTempCompStopVoltage_Type())
vpwrSystemTempCompStopVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemTempCompStopVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemTempCompStopVoltage.setUnits(' vpwrSystemTempCompStopVoltage *.01 Volts')
class _VpwrSystemTempCompensationSlope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_VpwrSystemTempCompensationSlope_Type.__name__=_G
_VpwrSystemTempCompensationSlope_Object=MibScalar
vpwrSystemTempCompensationSlope=_VpwrSystemTempCompensationSlope_Object((1,3,6,1,4,1,13858,2,2,4),_VpwrSystemTempCompensationSlope_Type())
vpwrSystemTempCompensationSlope.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemTempCompensationSlope.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemTempCompensationSlope.setUnits(' milli-Volts per degrees Centigrade')
class _VpwrSystemThermalSenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('external',0),('internal',1)))
_VpwrSystemThermalSenseType_Type.__name__=_G
_VpwrSystemThermalSenseType_Object=MibScalar
vpwrSystemThermalSenseType=_VpwrSystemThermalSenseType_Object((1,3,6,1,4,1,13858,2,2,5),_VpwrSystemThermalSenseType_Type())
vpwrSystemThermalSenseType.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemThermalSenseType.setStatus(_A)
_VpwrSystemHVAlarmSetpoint_Type=Integer32
_VpwrSystemHVAlarmSetpoint_Object=MibScalar
vpwrSystemHVAlarmSetpoint=_VpwrSystemHVAlarmSetpoint_Object((1,3,6,1,4,1,13858,2,2,6),_VpwrSystemHVAlarmSetpoint_Type())
vpwrSystemHVAlarmSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemHVAlarmSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemHVAlarmSetpoint.setUnits(' vpwrSystemHVAlarmSetpoint *.01 Volts')
_VpwrSystemBDAlarmSetpoint_Type=Integer32
_VpwrSystemBDAlarmSetpoint_Object=MibScalar
vpwrSystemBDAlarmSetpoint=_VpwrSystemBDAlarmSetpoint_Object((1,3,6,1,4,1,13858,2,2,7),_VpwrSystemBDAlarmSetpoint_Type())
vpwrSystemBDAlarmSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemBDAlarmSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemBDAlarmSetpoint.setUnits(' vpwrSystemBDAlarmSetpoint *.01 Volts')
_VpwrSystemInternalTempLThreshold_Type=Integer32
_VpwrSystemInternalTempLThreshold_Object=MibScalar
vpwrSystemInternalTempLThreshold=_VpwrSystemInternalTempLThreshold_Object((1,3,6,1,4,1,13858,2,2,8),_VpwrSystemInternalTempLThreshold_Type())
vpwrSystemInternalTempLThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemInternalTempLThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemInternalTempLThreshold.setUnits(_H)
_VpwrSystemInternalTempUThreshold_Type=Integer32
_VpwrSystemInternalTempUThreshold_Object=MibScalar
vpwrSystemInternalTempUThreshold=_VpwrSystemInternalTempUThreshold_Object((1,3,6,1,4,1,13858,2,2,9),_VpwrSystemInternalTempUThreshold_Type())
vpwrSystemInternalTempUThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemInternalTempUThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemInternalTempUThreshold.setUnits(_H)
_VpwrSystemParameterGroup_ObjectIdentity=ObjectIdentity
vpwrSystemParameterGroup=_VpwrSystemParameterGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,3))
class _VpwrSystemShelfCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_VpwrSystemShelfCapacity_Type.__name__=_G
_VpwrSystemShelfCapacity_Object=MibScalar
vpwrSystemShelfCapacity=_VpwrSystemShelfCapacity_Object((1,3,6,1,4,1,13858,2,3,1),_VpwrSystemShelfCapacity_Type())
vpwrSystemShelfCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemShelfCapacity.setStatus(_A)
_VpwrSystemVoltage_Type=Integer32
_VpwrSystemVoltage_Object=MibScalar
vpwrSystemVoltage=_VpwrSystemVoltage_Object((1,3,6,1,4,1,13858,2,3,2),_VpwrSystemVoltage_Type())
vpwrSystemVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemVoltage.setUnits(' vpwrSystemVoltage *.01 Volts')
_VpwrSystemCurrent_Type=Integer32
_VpwrSystemCurrent_Object=MibScalar
vpwrSystemCurrent=_VpwrSystemCurrent_Object((1,3,6,1,4,1,13858,2,3,3),_VpwrSystemCurrent_Type())
vpwrSystemCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemCurrent.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemCurrent.setUnits(' Amperes')
class _VpwrSystemControllerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('systemControllerStateUnknown',0),('systemControllerStateNormal',1),('systemControllerStateChange',2),('systemControllerStateAlarm',3),('systemControllerStateMenu',4),('systemControllerStateIrActive',5)))
_VpwrSystemControllerState_Type.__name__=_G
_VpwrSystemControllerState_Object=MibScalar
vpwrSystemControllerState=_VpwrSystemControllerState_Object((1,3,6,1,4,1,13858,2,3,4),_VpwrSystemControllerState_Type())
vpwrSystemControllerState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemControllerState.setStatus(_A)
_VpwrSystemInternalTemperature_Type=Integer32
_VpwrSystemInternalTemperature_Object=MibScalar
vpwrSystemInternalTemperature=_VpwrSystemInternalTemperature_Object((1,3,6,1,4,1,13858,2,3,5),_VpwrSystemInternalTemperature_Type())
vpwrSystemInternalTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemInternalTemperature.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemInternalTemperature.setUnits(_H)
class _VpwrSystemTempCompensationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('systemTempCompInactive',0),('systemTempCompActive',1)))
_VpwrSystemTempCompensationState_Type.__name__=_G
_VpwrSystemTempCompensationState_Object=MibScalar
vpwrSystemTempCompensationState=_VpwrSystemTempCompensationState_Object((1,3,6,1,4,1,13858,2,3,6),_VpwrSystemTempCompensationState_Type())
vpwrSystemTempCompensationState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemTempCompensationState.setStatus(_A)
class _VpwrSystemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('sysType48V',0),('sysType24V',1)))
_VpwrSystemType_Type.__name__=_G
_VpwrSystemType_Object=MibScalar
vpwrSystemType=_VpwrSystemType_Object((1,3,6,1,4,1,13858,2,3,7),_VpwrSystemType_Type())
vpwrSystemType.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemType.setStatus(_A)
_VpwrDcPowerRectifier_ObjectIdentity=ObjectIdentity
vpwrDcPowerRectifier=_VpwrDcPowerRectifier_ObjectIdentity((1,3,6,1,4,1,13858,3))
_VpwrRectifierConfigGroup_ObjectIdentity=ObjectIdentity
vpwrRectifierConfigGroup=_VpwrRectifierConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,3,1))
_VpwrRectifierFVSetpoint_Type=Integer32
_VpwrRectifierFVSetpoint_Object=MibScalar
vpwrRectifierFVSetpoint=_VpwrRectifierFVSetpoint_Object((1,3,6,1,4,1,13858,3,1,1),_VpwrRectifierFVSetpoint_Type())
vpwrRectifierFVSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRectifierFVSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrRectifierFVSetpoint.setUnits(' vpwrRectifierFVSetpoint *.01 Volts')
_VpwrRectifierHVSDSetpoint_Type=Integer32
_VpwrRectifierHVSDSetpoint_Object=MibScalar
vpwrRectifierHVSDSetpoint=_VpwrRectifierHVSDSetpoint_Object((1,3,6,1,4,1,13858,3,1,2),_VpwrRectifierHVSDSetpoint_Type())
vpwrRectifierHVSDSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRectifierHVSDSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrRectifierHVSDSetpoint.setUnits(' vpwrRectifierHVSDSetpoint *.01 Volts')
_VpwrRectifierAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrRectifierAlarmGroup=_VpwrRectifierAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,3,2))
_VpwrRectAlarmDCFail_ObjectIdentity=ObjectIdentity
vpwrRectAlarmDCFail=_VpwrRectAlarmDCFail_ObjectIdentity((1,3,6,1,4,1,13858,3,2,1))
if mibBuilder.loadTexts:vpwrRectAlarmDCFail.setStatus(_A)
_VpwrRectAlarmBoostFail_ObjectIdentity=ObjectIdentity
vpwrRectAlarmBoostFail=_VpwrRectAlarmBoostFail_ObjectIdentity((1,3,6,1,4,1,13858,3,2,2))
if mibBuilder.loadTexts:vpwrRectAlarmBoostFail.setStatus(_A)
_VpwrRectAlarmACFail_ObjectIdentity=ObjectIdentity
vpwrRectAlarmACFail=_VpwrRectAlarmACFail_ObjectIdentity((1,3,6,1,4,1,13858,3,2,3))
if mibBuilder.loadTexts:vpwrRectAlarmACFail.setStatus(_A)
_VpwrRectAlarmHVSD_ObjectIdentity=ObjectIdentity
vpwrRectAlarmHVSD=_VpwrRectAlarmHVSD_ObjectIdentity((1,3,6,1,4,1,13858,3,2,4))
if mibBuilder.loadTexts:vpwrRectAlarmHVSD.setStatus(_A)
_VpwrRectAlarmFanFail_ObjectIdentity=ObjectIdentity
vpwrRectAlarmFanFail=_VpwrRectAlarmFanFail_ObjectIdentity((1,3,6,1,4,1,13858,3,2,5))
if mibBuilder.loadTexts:vpwrRectAlarmFanFail.setStatus(_A)
_VpwrRectAlarmAmbTemp_ObjectIdentity=ObjectIdentity
vpwrRectAlarmAmbTemp=_VpwrRectAlarmAmbTemp_ObjectIdentity((1,3,6,1,4,1,13858,3,2,6))
if mibBuilder.loadTexts:vpwrRectAlarmAmbTemp.setStatus(_A)
_VpwrRectAlarmIntTemp_ObjectIdentity=ObjectIdentity
vpwrRectAlarmIntTemp=_VpwrRectAlarmIntTemp_ObjectIdentity((1,3,6,1,4,1,13858,3,2,7))
if mibBuilder.loadTexts:vpwrRectAlarmIntTemp.setStatus(_A)
_VpwrRectAlarmIShare_ObjectIdentity=ObjectIdentity
vpwrRectAlarmIShare=_VpwrRectAlarmIShare_ObjectIdentity((1,3,6,1,4,1,13858,3,2,8))
if mibBuilder.loadTexts:vpwrRectAlarmIShare.setStatus(_A)
_VpwrRectAlarmUV_ObjectIdentity=ObjectIdentity
vpwrRectAlarmUV=_VpwrRectAlarmUV_ObjectIdentity((1,3,6,1,4,1,13858,3,2,9))
if mibBuilder.loadTexts:vpwrRectAlarmUV.setStatus(_A)
_VpwrRectAlarmLowVoltage_ObjectIdentity=ObjectIdentity
vpwrRectAlarmLowVoltage=_VpwrRectAlarmLowVoltage_ObjectIdentity((1,3,6,1,4,1,13858,3,2,10))
if mibBuilder.loadTexts:vpwrRectAlarmLowVoltage.setStatus(_A)
_VpwrRectAlarmReserved_ObjectIdentity=ObjectIdentity
vpwrRectAlarmReserved=_VpwrRectAlarmReserved_ObjectIdentity((1,3,6,1,4,1,13858,3,2,11))
if mibBuilder.loadTexts:vpwrRectAlarmReserved.setStatus(_A)
_VpwrRectAlarmDCEnable_ObjectIdentity=ObjectIdentity
vpwrRectAlarmDCEnable=_VpwrRectAlarmDCEnable_ObjectIdentity((1,3,6,1,4,1,13858,3,2,12))
if mibBuilder.loadTexts:vpwrRectAlarmDCEnable.setStatus(_A)
_VpwrRectAlarmRemoteShutdown_ObjectIdentity=ObjectIdentity
vpwrRectAlarmRemoteShutdown=_VpwrRectAlarmRemoteShutdown_ObjectIdentity((1,3,6,1,4,1,13858,3,2,13))
if mibBuilder.loadTexts:vpwrRectAlarmRemoteShutdown.setStatus(_A)
_VpwrRectAlarmModDisableShutdown_ObjectIdentity=ObjectIdentity
vpwrRectAlarmModDisableShutdown=_VpwrRectAlarmModDisableShutdown_ObjectIdentity((1,3,6,1,4,1,13858,3,2,14))
if mibBuilder.loadTexts:vpwrRectAlarmModDisableShutdown.setStatus(_A)
_VpwrRectAlarmShortPinShutdown_ObjectIdentity=ObjectIdentity
vpwrRectAlarmShortPinShutdown=_VpwrRectAlarmShortPinShutdown_ObjectIdentity((1,3,6,1,4,1,13858,3,2,15))
if mibBuilder.loadTexts:vpwrRectAlarmShortPinShutdown.setStatus(_A)
_VpwrRectAlarmBoostComm_ObjectIdentity=ObjectIdentity
vpwrRectAlarmBoostComm=_VpwrRectAlarmBoostComm_ObjectIdentity((1,3,6,1,4,1,13858,3,2,16))
if mibBuilder.loadTexts:vpwrRectAlarmBoostComm.setStatus(_A)
_VpwrRectifierTestGroup_ObjectIdentity=ObjectIdentity
vpwrRectifierTestGroup=_VpwrRectifierTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,3,3))
_VpwrDcPowerLvd_ObjectIdentity=ObjectIdentity
vpwrDcPowerLvd=_VpwrDcPowerLvd_ObjectIdentity((1,3,6,1,4,1,13858,4))
_VpwrLvdConfigGroup_ObjectIdentity=ObjectIdentity
vpwrLvdConfigGroup=_VpwrLvdConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,4,1))
_VpwrLvdWarningSetpoint_Type=Integer32
_VpwrLvdWarningSetpoint_Object=MibScalar
vpwrLvdWarningSetpoint=_VpwrLvdWarningSetpoint_Object((1,3,6,1,4,1,13858,4,1,1),_VpwrLvdWarningSetpoint_Type())
vpwrLvdWarningSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvdWarningSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdWarningSetpoint.setUnits(' vpwrLvdWarningSetpoint * .01 Volts')
_VpwrLvdDisconnectSetpoint_Type=Integer32
_VpwrLvdDisconnectSetpoint_Object=MibScalar
vpwrLvdDisconnectSetpoint=_VpwrLvdDisconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,2),_VpwrLvdDisconnectSetpoint_Type())
vpwrLvdDisconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvdDisconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdDisconnectSetpoint.setUnits(' vpwrLvdDisconnectSetpoint *.01 Volts')
_VpwrLvdReconnectSetpoint_Type=Integer32
_VpwrLvdReconnectSetpoint_Object=MibScalar
vpwrLvdReconnectSetpoint=_VpwrLvdReconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,3),_VpwrLvdReconnectSetpoint_Type())
vpwrLvdReconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvdReconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdReconnectSetpoint.setUnits(' vpwrLvdReconnectSetpoint *.01 Volts')
class _VpwrLvdReconnectDelayTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,240))
_VpwrLvdReconnectDelayTimer_Type.__name__=_G
_VpwrLvdReconnectDelayTimer_Object=MibScalar
vpwrLvdReconnectDelayTimer=_VpwrLvdReconnectDelayTimer_Object((1,3,6,1,4,1,13858,4,1,4),_VpwrLvdReconnectDelayTimer_Type())
vpwrLvdReconnectDelayTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvdReconnectDelayTimer.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdReconnectDelayTimer.setUnits(' Seconds')
_VpwrLvdAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrLvdAlarmGroup=_VpwrLvdAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,4,2))
_VpwrLvdAlarmContactorOpen_ObjectIdentity=ObjectIdentity
vpwrLvdAlarmContactorOpen=_VpwrLvdAlarmContactorOpen_ObjectIdentity((1,3,6,1,4,1,13858,4,2,1))
if mibBuilder.loadTexts:vpwrLvdAlarmContactorOpen.setStatus(_A)
_VpwrLvdAlarmCBOpen_ObjectIdentity=ObjectIdentity
vpwrLvdAlarmCBOpen=_VpwrLvdAlarmCBOpen_ObjectIdentity((1,3,6,1,4,1,13858,4,2,2))
if mibBuilder.loadTexts:vpwrLvdAlarmCBOpen.setStatus(_A)
_VpwrTrapLvdFuseOpen_ObjectIdentity=ObjectIdentity
vpwrTrapLvdFuseOpen=_VpwrTrapLvdFuseOpen_ObjectIdentity((1,3,6,1,4,1,13858,4,2,3))
if mibBuilder.loadTexts:vpwrTrapLvdFuseOpen.setStatus(_A)
_VpwrLvdAlarmWarning_ObjectIdentity=ObjectIdentity
vpwrLvdAlarmWarning=_VpwrLvdAlarmWarning_ObjectIdentity((1,3,6,1,4,1,13858,4,2,4))
if mibBuilder.loadTexts:vpwrLvdAlarmWarning.setStatus(_A)
_VpwrLvdTestGroup_ObjectIdentity=ObjectIdentity
vpwrLvdTestGroup=_VpwrLvdTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,4,3))
_VpwrDcPowerTest_ObjectIdentity=ObjectIdentity
vpwrDcPowerTest=_VpwrDcPowerTest_ObjectIdentity((1,3,6,1,4,1,13858,5))
_VpwrDcPowerModuleIdent_ObjectIdentity=ObjectIdentity
vpwrDcPowerModuleIdent=_VpwrDcPowerModuleIdent_ObjectIdentity((1,3,6,1,4,1,13858,6))
_VpwrDcPowerBatteryGroup_ObjectIdentity=ObjectIdentity
vpwrDcPowerBatteryGroup=_VpwrDcPowerBatteryGroup_ObjectIdentity((1,3,6,1,4,1,13858,7))
_VpwrBatteryTempGroup_ObjectIdentity=ObjectIdentity
vpwrBatteryTempGroup=_VpwrBatteryTempGroup_ObjectIdentity((1,3,6,1,4,1,13858,7,1))
_VpwrBatteryTempTable_Object=MibTable
vpwrBatteryTempTable=_VpwrBatteryTempTable_Object((1,3,6,1,4,1,13858,7,1,1))
if mibBuilder.loadTexts:vpwrBatteryTempTable.setStatus(_A)
_VpwrBatteryTempTableEntry_Object=MibTableRow
vpwrBatteryTempTableEntry=_VpwrBatteryTempTableEntry_Object((1,3,6,1,4,1,13858,7,1,1,1))
vpwrBatteryTempTableEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:vpwrBatteryTempTableEntry.setStatus(_A)
_VpwrBatteryTempIndex_Type=Integer32
_VpwrBatteryTempIndex_Object=MibTableColumn
vpwrBatteryTempIndex=_VpwrBatteryTempIndex_Object((1,3,6,1,4,1,13858,7,1,1,1,1),_VpwrBatteryTempIndex_Type())
vpwrBatteryTempIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBatteryTempIndex.setStatus(_A)
class _VpwrBatteryTempName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_VpwrBatteryTempName_Type.__name__=_F
_VpwrBatteryTempName_Object=MibTableColumn
vpwrBatteryTempName=_VpwrBatteryTempName_Object((1,3,6,1,4,1,13858,7,1,1,1,2),_VpwrBatteryTempName_Type())
vpwrBatteryTempName.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryTempName.setStatus(_A)
_VpwrBatteryTemp_Type=Integer32
_VpwrBatteryTemp_Object=MibTableColumn
vpwrBatteryTemp=_VpwrBatteryTemp_Object((1,3,6,1,4,1,13858,7,1,1,1,3),_VpwrBatteryTemp_Type())
vpwrBatteryTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBatteryTemp.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryTemp.setUnits(_H)
_VpwrBatteryTempLThreshold_Type=Integer32
_VpwrBatteryTempLThreshold_Object=MibScalar
vpwrBatteryTempLThreshold=_VpwrBatteryTempLThreshold_Object((1,3,6,1,4,1,13858,7,1,2),_VpwrBatteryTempLThreshold_Type())
vpwrBatteryTempLThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryTempLThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryTempLThreshold.setUnits(_H)
_VpwrBatteryTempUThreshold_Type=Integer32
_VpwrBatteryTempUThreshold_Object=MibScalar
vpwrBatteryTempUThreshold=_VpwrBatteryTempUThreshold_Object((1,3,6,1,4,1,13858,7,1,3),_VpwrBatteryTempUThreshold_Type())
vpwrBatteryTempUThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryTempUThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryTempUThreshold.setUnits(_H)
_VpwrDcPowerAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrDcPowerAlarmGroup=_VpwrDcPowerAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,8))
_VpwrAlarmsPresent_Type=Gauge32
_VpwrAlarmsPresent_Object=MibScalar
vpwrAlarmsPresent=_VpwrAlarmsPresent_Object((1,3,6,1,4,1,13858,8,1),_VpwrAlarmsPresent_Type())
vpwrAlarmsPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrAlarmsPresent.setStatus(_A)
_VpwrAlarmTable_Object=MibTable
vpwrAlarmTable=_VpwrAlarmTable_Object((1,3,6,1,4,1,13858,8,2))
if mibBuilder.loadTexts:vpwrAlarmTable.setStatus(_A)
_VpwrAlarmEntry_Object=MibTableRow
vpwrAlarmEntry=_VpwrAlarmEntry_Object((1,3,6,1,4,1,13858,8,2,1))
vpwrAlarmEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_L))
if mibBuilder.loadTexts:vpwrAlarmEntry.setStatus(_A)
_VpwrAlarmIndex_Type=PositiveInteger
_VpwrAlarmIndex_Object=MibTableColumn
vpwrAlarmIndex=_VpwrAlarmIndex_Object((1,3,6,1,4,1,13858,8,2,1,1),_VpwrAlarmIndex_Type())
vpwrAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrAlarmIndex.setStatus(_A)
_VpwrAlarmDescr_Type=AutonomousType
_VpwrAlarmDescr_Object=MibTableColumn
vpwrAlarmDescr=_VpwrAlarmDescr_Object((1,3,6,1,4,1,13858,8,2,1,2),_VpwrAlarmDescr_Type())
vpwrAlarmDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrAlarmDescr.setStatus(_A)
_VpwrAlarmTime_Type=TimeStamp
_VpwrAlarmTime_Object=MibTableColumn
vpwrAlarmTime=_VpwrAlarmTime_Object((1,3,6,1,4,1,13858,8,2,1,3),_VpwrAlarmTime_Type())
vpwrAlarmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrAlarmTime.setStatus(_A)
_SysAlarmConfigTable_Object=MibTable
sysAlarmConfigTable=_SysAlarmConfigTable_Object((1,3,6,1,4,1,13858,8,4))
if mibBuilder.loadTexts:sysAlarmConfigTable.setStatus(_A)
_SysAlarmConfigEntry_Object=MibTableRow
sysAlarmConfigEntry=_SysAlarmConfigEntry_Object((1,3,6,1,4,1,13858,8,4,1))
sysAlarmConfigEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:sysAlarmConfigEntry.setStatus(_A)
_SysAlarmIndex_Type=Integer32
_SysAlarmIndex_Object=MibTableColumn
sysAlarmIndex=_SysAlarmIndex_Object((1,3,6,1,4,1,13858,8,4,1,1),_SysAlarmIndex_Type())
sysAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmIndex.setStatus(_A)
class _SysAlarmDefaultName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAlarmDefaultName_Type.__name__=_F
_SysAlarmDefaultName_Object=MibTableColumn
sysAlarmDefaultName=_SysAlarmDefaultName_Object((1,3,6,1,4,1,13858,8,4,1,2),_SysAlarmDefaultName_Type())
sysAlarmDefaultName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmDefaultName.setStatus(_A)
class _SysAlarmCustomName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAlarmCustomName_Type.__name__=_F
_SysAlarmCustomName_Object=MibTableColumn
sysAlarmCustomName=_SysAlarmCustomName_Object((1,3,6,1,4,1,13858,8,4,1,3),_SysAlarmCustomName_Type())
sysAlarmCustomName.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmCustomName.setStatus(_A)
class _SysAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('major',1),('minor',2),('majorAndMinor',3)))
_SysAlarmSeverity_Type.__name__=_G
_SysAlarmSeverity_Object=MibTableColumn
sysAlarmSeverity=_SysAlarmSeverity_Object((1,3,6,1,4,1,13858,8,4,1,4),_SysAlarmSeverity_Type())
sysAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmSeverity.setStatus(_A)
class _SysAlarmToRelayMapping_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAlarmToRelayMapping_Type.__name__=_F
_SysAlarmToRelayMapping_Object=MibTableColumn
sysAlarmToRelayMapping=_SysAlarmToRelayMapping_Object((1,3,6,1,4,1,13858,8,4,1,5),_SysAlarmToRelayMapping_Type())
sysAlarmToRelayMapping.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmToRelayMapping.setStatus(_A)
class _SysAlarmOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
_SysAlarmOperStatus_Type.__name__=_G
_SysAlarmOperStatus_Object=MibTableColumn
sysAlarmOperStatus=_SysAlarmOperStatus_Object((1,3,6,1,4,1,13858,8,4,1,6),_SysAlarmOperStatus_Type())
sysAlarmOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmOperStatus.setStatus(_A)
_VpwrDcPowerSnmpConfig_ObjectIdentity=ObjectIdentity
vpwrDcPowerSnmpConfig=_VpwrDcPowerSnmpConfig_ObjectIdentity((1,3,6,1,4,1,13858,9))
_VpwrTrapTable_Object=MibTable
vpwrTrapTable=_VpwrTrapTable_Object((1,3,6,1,4,1,13858,9,1))
if mibBuilder.loadTexts:vpwrTrapTable.setStatus(_A)
_VpwrTrapTableEntry_Object=MibTableRow
vpwrTrapTableEntry=_VpwrTrapTableEntry_Object((1,3,6,1,4,1,13858,9,1,1))
vpwrTrapTableEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:vpwrTrapTableEntry.setStatus(_A)
_VpwrTrapIpIndex_Type=Integer32
_VpwrTrapIpIndex_Object=MibTableColumn
vpwrTrapIpIndex=_VpwrTrapIpIndex_Object((1,3,6,1,4,1,13858,9,1,1,1),_VpwrTrapIpIndex_Type())
vpwrTrapIpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrTrapIpIndex.setStatus(_A)
_VpwrTrapIpAddress_Type=IpAddress
_VpwrTrapIpAddress_Object=MibTableColumn
vpwrTrapIpAddress=_VpwrTrapIpAddress_Object((1,3,6,1,4,1,13858,9,1,1,2),_VpwrTrapIpAddress_Type())
vpwrTrapIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrTrapIpAddress.setStatus(_A)
_VpwrTrapCriticality_Type=Integer32
_VpwrTrapCriticality_Object=MibTableColumn
vpwrTrapCriticality=_VpwrTrapCriticality_Object((1,3,6,1,4,1,13858,9,1,1,3),_VpwrTrapCriticality_Type())
vpwrTrapCriticality.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrTrapCriticality.setStatus(_A)
class _VpwrReadCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,8))
_VpwrReadCommunityString_Type.__name__=_F
_VpwrReadCommunityString_Object=MibScalar
vpwrReadCommunityString=_VpwrReadCommunityString_Object((1,3,6,1,4,1,13858,9,2),_VpwrReadCommunityString_Type())
vpwrReadCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrReadCommunityString.setStatus(_A)
class _VpwrWriteCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,8))
_VpwrWriteCommunityString_Type.__name__=_F
_VpwrWriteCommunityString_Object=MibScalar
vpwrWriteCommunityString=_VpwrWriteCommunityString_Object((1,3,6,1,4,1,13858,9,3),_VpwrWriteCommunityString_Type())
vpwrWriteCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrWriteCommunityString.setStatus(_A)
class _VpwrTrapCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,8))
_VpwrTrapCommunityString_Type.__name__=_F
_VpwrTrapCommunityString_Object=MibScalar
vpwrTrapCommunityString=_VpwrTrapCommunityString_Object((1,3,6,1,4,1,13858,9,4),_VpwrTrapCommunityString_Type())
vpwrTrapCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrTrapCommunityString.setStatus(_A)
_VpwrDcPowerTraps_ObjectIdentity=ObjectIdentity
vpwrDcPowerTraps=_VpwrDcPowerTraps_ObjectIdentity((1,3,6,1,4,1,13858,10))
_VpwrDcPowerTrapsMsgString_ObjectIdentity=ObjectIdentity
vpwrDcPowerTrapsMsgString=_VpwrDcPowerTrapsMsgString_ObjectIdentity((1,3,6,1,4,1,13858,11))
class _VpwrTrapsMsgString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_VpwrTrapsMsgString_Type.__name__=_F
_VpwrTrapsMsgString_Object=MibScalar
vpwrTrapsMsgString=_VpwrTrapsMsgString_Object((1,3,6,1,4,1,13858,11,1),_VpwrTrapsMsgString_Type())
vpwrTrapsMsgString.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vpwrTrapsMsgString.setStatus(_A)
vpwrTrapPowerMajorAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,1))
vpwrTrapPowerMajorAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapPowerMajorAlarm.setStatus('')
vpwrTrapPowerMinorAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,2))
vpwrTrapPowerMinorAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapPowerMinorAlarm.setStatus('')
vpwrTrapACFAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,3))
vpwrTrapACFAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapACFAlarm.setStatus('')
vpwrTrapHVAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,4))
vpwrTrapHVAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapHVAlarm.setStatus('')
vpwrTrapHVSDAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,5))
vpwrTrapHVSDAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapHVSDAlarm.setStatus('')
vpwrTrapBDAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,6))
vpwrTrapBDAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapBDAlarm.setStatus('')
vpwrTrapLVDWarningAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,7))
vpwrTrapLVDWarningAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapLVDWarningAlarm.setStatus('')
vpwrTrapLVDOpenAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,8))
vpwrTrapLVDOpenAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapLVDOpenAlarm.setStatus('')
vpwrTrapDistAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,9))
vpwrTrapDistAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapDistAlarm.setStatus('')
vpwrTrapAuxAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,10))
vpwrTrapAuxAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapAuxAlarm.setStatus('')
vpwrTrapSystemRedundancyAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,11))
vpwrTrapSystemRedundancyAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapSystemRedundancyAlarm.setStatus('')
vpwrTrapIShareAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,12))
vpwrTrapIShareAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapIShareAlarm.setStatus('')
vpwrTrapModuleFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,13))
vpwrTrapModuleFailAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapModuleFailAlarm.setStatus('')
vpwrTrapMultipleModuleFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,14))
vpwrTrapMultipleModuleFailAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapMultipleModuleFailAlarm.setStatus('')
vpwrTrapModuleCommAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,15))
vpwrTrapModuleCommAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapModuleCommAlarm.setStatus('')
vpwrTrapSystemOverTemperatureAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,16))
vpwrTrapSystemOverTemperatureAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapSystemOverTemperatureAlarm.setStatus('')
vpwrTrapSystemOK=NotificationType((1,3,6,1,4,1,13858,10,0,17))
vpwrTrapSystemOK.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapSystemOK.setStatus('')
vpwrTrapModuleInserted=NotificationType((1,3,6,1,4,1,13858,10,0,18))
vpwrTrapModuleInserted.setObjects(*((_B,_E),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:vpwrTrapModuleInserted.setStatus('')
vpwrTrapModuleRemoved=NotificationType((1,3,6,1,4,1,13858,10,0,19))
vpwrTrapModuleRemoved.setObjects(*((_B,_E),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:vpwrTrapModuleRemoved.setStatus('')
vpwrTrapThermalCompActive=NotificationType((1,3,6,1,4,1,13858,10,0,20))
vpwrTrapThermalCompActive.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapThermalCompActive.setStatus('')
vpwrTrapThermalCompInactive=NotificationType((1,3,6,1,4,1,13858,10,0,21))
vpwrTrapThermalCompInactive.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapThermalCompInactive.setStatus('')
vpwrTrapInternalTempAlarmSet=NotificationType((1,3,6,1,4,1,13858,10,0,22))
vpwrTrapInternalTempAlarmSet.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapInternalTempAlarmSet.setStatus('')
vpwrTrapInternalTempAlarmCleared=NotificationType((1,3,6,1,4,1,13858,10,0,23))
vpwrTrapInternalTempAlarmCleared.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapInternalTempAlarmCleared.setStatus('')
vpwrTrapBatteryTempAlarmSet=NotificationType((1,3,6,1,4,1,13858,10,0,24))
vpwrTrapBatteryTempAlarmSet.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapBatteryTempAlarmSet.setStatus('')
vpwrTrapBatteryTempAlarmCleared=NotificationType((1,3,6,1,4,1,13858,10,0,25))
vpwrTrapBatteryTempAlarmCleared.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapBatteryTempAlarmCleared.setStatus('')
mibBuilder.exportSymbols(_B,**{'PositiveInteger':PositiveInteger,'NonNegativeInteger':NonNegativeInteger,'valereDcPowerMgt':valereDcPowerMgt,'vpwrDcPowerProducts':vpwrDcPowerProducts,'vpwrDcPowerSystem':vpwrDcPowerSystem,'vpwrSystemIdentGroup':vpwrSystemIdentGroup,'vpwrIdentManufacturer':vpwrIdentManufacturer,'vpwrIdentModel':vpwrIdentModel,'vpwrIdentControllerVersion':vpwrIdentControllerVersion,'vpwrIdentAgentSoftwareVersion':vpwrIdentAgentSoftwareVersion,'vpwrIdentName':vpwrIdentName,'vpwrSystemIdentTable':vpwrSystemIdentTable,'vpwrSystemIdentEntry':vpwrSystemIdentEntry,_I:vpwrShelfIndex,_J:vpwrModuleIndex,'vpwrModuleOID':vpwrModuleOID,'vpwrModuleParameter':vpwrModuleParameter,'vpwrModuleOperStatus':vpwrModuleOperStatus,'vpwrModuleCapacity':vpwrModuleCapacity,'vpwrSystemConfigGroup':vpwrSystemConfigGroup,'vpwrSystemTempCompensation':vpwrSystemTempCompensation,'vpwrSystemTempCompStartTemperature':vpwrSystemTempCompStartTemperature,'vpwrSystemTempCompStopVoltage':vpwrSystemTempCompStopVoltage,'vpwrSystemTempCompensationSlope':vpwrSystemTempCompensationSlope,'vpwrSystemThermalSenseType':vpwrSystemThermalSenseType,'vpwrSystemHVAlarmSetpoint':vpwrSystemHVAlarmSetpoint,'vpwrSystemBDAlarmSetpoint':vpwrSystemBDAlarmSetpoint,'vpwrSystemInternalTempLThreshold':vpwrSystemInternalTempLThreshold,'vpwrSystemInternalTempUThreshold':vpwrSystemInternalTempUThreshold,'vpwrSystemParameterGroup':vpwrSystemParameterGroup,'vpwrSystemShelfCapacity':vpwrSystemShelfCapacity,'vpwrSystemVoltage':vpwrSystemVoltage,'vpwrSystemCurrent':vpwrSystemCurrent,'vpwrSystemControllerState':vpwrSystemControllerState,'vpwrSystemInternalTemperature':vpwrSystemInternalTemperature,'vpwrSystemTempCompensationState':vpwrSystemTempCompensationState,'vpwrSystemType':vpwrSystemType,'vpwrDcPowerRectifier':vpwrDcPowerRectifier,'vpwrRectifierConfigGroup':vpwrRectifierConfigGroup,'vpwrRectifierFVSetpoint':vpwrRectifierFVSetpoint,'vpwrRectifierHVSDSetpoint':vpwrRectifierHVSDSetpoint,'vpwrRectifierAlarmGroup':vpwrRectifierAlarmGroup,'vpwrRectAlarmDCFail':vpwrRectAlarmDCFail,'vpwrRectAlarmBoostFail':vpwrRectAlarmBoostFail,'vpwrRectAlarmACFail':vpwrRectAlarmACFail,'vpwrRectAlarmHVSD':vpwrRectAlarmHVSD,'vpwrRectAlarmFanFail':vpwrRectAlarmFanFail,'vpwrRectAlarmAmbTemp':vpwrRectAlarmAmbTemp,'vpwrRectAlarmIntTemp':vpwrRectAlarmIntTemp,'vpwrRectAlarmIShare':vpwrRectAlarmIShare,'vpwrRectAlarmUV':vpwrRectAlarmUV,'vpwrRectAlarmLowVoltage':vpwrRectAlarmLowVoltage,'vpwrRectAlarmReserved':vpwrRectAlarmReserved,'vpwrRectAlarmDCEnable':vpwrRectAlarmDCEnable,'vpwrRectAlarmRemoteShutdown':vpwrRectAlarmRemoteShutdown,'vpwrRectAlarmModDisableShutdown':vpwrRectAlarmModDisableShutdown,'vpwrRectAlarmShortPinShutdown':vpwrRectAlarmShortPinShutdown,'vpwrRectAlarmBoostComm':vpwrRectAlarmBoostComm,'vpwrRectifierTestGroup':vpwrRectifierTestGroup,'vpwrDcPowerLvd':vpwrDcPowerLvd,'vpwrLvdConfigGroup':vpwrLvdConfigGroup,'vpwrLvdWarningSetpoint':vpwrLvdWarningSetpoint,'vpwrLvdDisconnectSetpoint':vpwrLvdDisconnectSetpoint,'vpwrLvdReconnectSetpoint':vpwrLvdReconnectSetpoint,'vpwrLvdReconnectDelayTimer':vpwrLvdReconnectDelayTimer,'vpwrLvdAlarmGroup':vpwrLvdAlarmGroup,'vpwrLvdAlarmContactorOpen':vpwrLvdAlarmContactorOpen,'vpwrLvdAlarmCBOpen':vpwrLvdAlarmCBOpen,'vpwrTrapLvdFuseOpen':vpwrTrapLvdFuseOpen,'vpwrLvdAlarmWarning':vpwrLvdAlarmWarning,'vpwrLvdTestGroup':vpwrLvdTestGroup,'vpwrDcPowerTest':vpwrDcPowerTest,'vpwrDcPowerModuleIdent':vpwrDcPowerModuleIdent,'vpwrDcPowerBatteryGroup':vpwrDcPowerBatteryGroup,'vpwrBatteryTempGroup':vpwrBatteryTempGroup,'vpwrBatteryTempTable':vpwrBatteryTempTable,'vpwrBatteryTempTableEntry':vpwrBatteryTempTableEntry,_K:vpwrBatteryTempIndex,'vpwrBatteryTempName':vpwrBatteryTempName,'vpwrBatteryTemp':vpwrBatteryTemp,'vpwrBatteryTempLThreshold':vpwrBatteryTempLThreshold,'vpwrBatteryTempUThreshold':vpwrBatteryTempUThreshold,'vpwrDcPowerAlarmGroup':vpwrDcPowerAlarmGroup,'vpwrAlarmsPresent':vpwrAlarmsPresent,'vpwrAlarmTable':vpwrAlarmTable,'vpwrAlarmEntry':vpwrAlarmEntry,_L:vpwrAlarmIndex,'vpwrAlarmDescr':vpwrAlarmDescr,'vpwrAlarmTime':vpwrAlarmTime,'sysAlarmConfigTable':sysAlarmConfigTable,'sysAlarmConfigEntry':sysAlarmConfigEntry,_M:sysAlarmIndex,'sysAlarmDefaultName':sysAlarmDefaultName,'sysAlarmCustomName':sysAlarmCustomName,'sysAlarmSeverity':sysAlarmSeverity,'sysAlarmToRelayMapping':sysAlarmToRelayMapping,'sysAlarmOperStatus':sysAlarmOperStatus,'vpwrDcPowerSnmpConfig':vpwrDcPowerSnmpConfig,'vpwrTrapTable':vpwrTrapTable,'vpwrTrapTableEntry':vpwrTrapTableEntry,_N:vpwrTrapIpIndex,'vpwrTrapIpAddress':vpwrTrapIpAddress,'vpwrTrapCriticality':vpwrTrapCriticality,'vpwrReadCommunityString':vpwrReadCommunityString,'vpwrWriteCommunityString':vpwrWriteCommunityString,'vpwrTrapCommunityString':vpwrTrapCommunityString,'vpwrDcPowerTraps':vpwrDcPowerTraps,'vpwrTrapPowerMajorAlarm':vpwrTrapPowerMajorAlarm,'vpwrTrapPowerMinorAlarm':vpwrTrapPowerMinorAlarm,'vpwrTrapACFAlarm':vpwrTrapACFAlarm,'vpwrTrapHVAlarm':vpwrTrapHVAlarm,'vpwrTrapHVSDAlarm':vpwrTrapHVSDAlarm,'vpwrTrapBDAlarm':vpwrTrapBDAlarm,'vpwrTrapLVDWarningAlarm':vpwrTrapLVDWarningAlarm,'vpwrTrapLVDOpenAlarm':vpwrTrapLVDOpenAlarm,'vpwrTrapDistAlarm':vpwrTrapDistAlarm,'vpwrTrapAuxAlarm':vpwrTrapAuxAlarm,'vpwrTrapSystemRedundancyAlarm':vpwrTrapSystemRedundancyAlarm,'vpwrTrapIShareAlarm':vpwrTrapIShareAlarm,'vpwrTrapModuleFailAlarm':vpwrTrapModuleFailAlarm,'vpwrTrapMultipleModuleFailAlarm':vpwrTrapMultipleModuleFailAlarm,'vpwrTrapModuleCommAlarm':vpwrTrapModuleCommAlarm,'vpwrTrapSystemOverTemperatureAlarm':vpwrTrapSystemOverTemperatureAlarm,'vpwrTrapSystemOK':vpwrTrapSystemOK,'vpwrTrapModuleInserted':vpwrTrapModuleInserted,'vpwrTrapModuleRemoved':vpwrTrapModuleRemoved,'vpwrTrapThermalCompActive':vpwrTrapThermalCompActive,'vpwrTrapThermalCompInactive':vpwrTrapThermalCompInactive,'vpwrTrapInternalTempAlarmSet':vpwrTrapInternalTempAlarmSet,'vpwrTrapInternalTempAlarmCleared':vpwrTrapInternalTempAlarmCleared,'vpwrTrapBatteryTempAlarmSet':vpwrTrapBatteryTempAlarmSet,'vpwrTrapBatteryTempAlarmCleared':vpwrTrapBatteryTempAlarmCleared,'vpwrDcPowerTrapsMsgString':vpwrDcPowerTrapsMsgString,_E:vpwrTrapsMsgString})