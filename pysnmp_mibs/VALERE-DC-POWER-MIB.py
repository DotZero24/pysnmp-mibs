_q='thermalProbeEntry'
_p='vpwrBayctrlModuleIdentEntry'
_o='vpwrPanelModuleIdentEntry'
_n='vpwrModuleIdentEntry'
_m='vpwrRingerIndex'
_l='vpwrTrapIpIndex'
_k='enabled'
_j='sysAuxAlarmIndex'
_i='majorAndMinor'
_h='sysAlarmIndex'
_g='sysRelayIndex'
_f='vpwrAlarmIndex'
_e='Ampere'
_d='vpwrBatteryTempIndex'
_c='PositiveInteger'
_b='vpwrLvdContactorIndex'
_a=' Seconds'
_Z=' * .01 Volts'
_Y='vpwrBayctrlIndex'
_X='vpwrPanelModuleIndex'
_W='vpwrPanelBayIndex'
_V='internal'
_U='external'
_T='tempCompEnabled'
_S='tempCompDisabled'
_R='not-accessible'
_Q='disabled'
_P='active'
_O='inactive'
_N=' milli-Volts per degrees Centigrade'
_M='moduleStatusAlarm'
_L='moduleStatusOK'
_K='vpwrBayIndex'
_J='vpwrModuleIndex'
_I='degrees Centigrade'
_H=' *.01 Volts'
_G='DisplayString'
_F='Integer32'
_E='vpwrTrapsMsgString'
_D='read-only'
_C='read-write'
_B='VALERE-DC-POWER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysUpTime,=mibBuilder.importSymbols('SNMPv2-MIB','sysUpTime')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TestAndIncr,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_G,'PhysAddress','TextualConvention','TestAndIncr','TimeInterval','TimeStamp')
vpwrDcPowerMgt=ModuleIdentity((1,3,6,1,4,1,13858))
class PositiveInteger(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NonNegativeInteger(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VpwrDcPowerProducts_ObjectIdentity=ObjectIdentity
vpwrDcPowerProducts=_VpwrDcPowerProducts_ObjectIdentity((1,3,6,1,4,1,13858,1))
_VpwrDcPowerSystem_ObjectIdentity=ObjectIdentity
vpwrDcPowerSystem=_VpwrDcPowerSystem_ObjectIdentity((1,3,6,1,4,1,13858,2))
_VpwrSystemIdentGroup_ObjectIdentity=ObjectIdentity
vpwrSystemIdentGroup=_VpwrSystemIdentGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,1))
class _VpwrIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_VpwrIdentManufacturer_Type.__name__=_G
_VpwrIdentManufacturer_Object=MibScalar
vpwrIdentManufacturer=_VpwrIdentManufacturer_Object((1,3,6,1,4,1,13858,2,1,1),_VpwrIdentManufacturer_Type())
vpwrIdentManufacturer.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrIdentManufacturer.setStatus(_A)
class _VpwrIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VpwrIdentModel_Type.__name__=_G
_VpwrIdentModel_Object=MibScalar
vpwrIdentModel=_VpwrIdentModel_Object((1,3,6,1,4,1,13858,2,1,2),_VpwrIdentModel_Type())
vpwrIdentModel.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrIdentModel.setStatus(_A)
class _VpwrIdentControllerVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VpwrIdentControllerVersion_Type.__name__=_G
_VpwrIdentControllerVersion_Object=MibScalar
vpwrIdentControllerVersion=_VpwrIdentControllerVersion_Object((1,3,6,1,4,1,13858,2,1,3),_VpwrIdentControllerVersion_Type())
vpwrIdentControllerVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrIdentControllerVersion.setStatus(_A)
class _VpwrIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VpwrIdentAgentSoftwareVersion_Type.__name__=_G
_VpwrIdentAgentSoftwareVersion_Object=MibScalar
vpwrIdentAgentSoftwareVersion=_VpwrIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,13858,2,1,4),_VpwrIdentAgentSoftwareVersion_Type())
vpwrIdentAgentSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrIdentAgentSoftwareVersion.setStatus(_A)
class _VpwrIdentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_VpwrIdentName_Type.__name__=_G
_VpwrIdentName_Object=MibScalar
vpwrIdentName=_VpwrIdentName_Object((1,3,6,1,4,1,13858,2,1,5),_VpwrIdentName_Type())
vpwrIdentName.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrIdentName.setStatus(_A)
_VpwrSystemIdentTable_Object=MibTable
vpwrSystemIdentTable=_VpwrSystemIdentTable_Object((1,3,6,1,4,1,13858,2,1,6))
if mibBuilder.loadTexts:vpwrSystemIdentTable.setStatus(_A)
_VpwrSystemIdentEntry_Object=MibTableRow
vpwrSystemIdentEntry=_VpwrSystemIdentEntry_Object((1,3,6,1,4,1,13858,2,1,6,1))
vpwrSystemIdentEntry.setIndexNames((0,_B,_K),(0,_B,_J))
if mibBuilder.loadTexts:vpwrSystemIdentEntry.setStatus(_A)
_VpwrBayIndex_Type=PositiveInteger
_VpwrBayIndex_Object=MibTableColumn
vpwrBayIndex=_VpwrBayIndex_Object((1,3,6,1,4,1,13858,2,1,6,1,1),_VpwrBayIndex_Type())
vpwrBayIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayIndex.setStatus(_A)
_VpwrModuleIndex_Type=PositiveInteger
_VpwrModuleIndex_Object=MibTableColumn
vpwrModuleIndex=_VpwrModuleIndex_Object((1,3,6,1,4,1,13858,2,1,6,1,2),_VpwrModuleIndex_Type())
vpwrModuleIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleIndex.setStatus(_A)
_VpwrModuleOID_Type=ObjectIdentifier
_VpwrModuleOID_Object=MibTableColumn
vpwrModuleOID=_VpwrModuleOID_Object((1,3,6,1,4,1,13858,2,1,6,1,3),_VpwrModuleOID_Type())
vpwrModuleOID.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleOID.setStatus(_A)
_VpwrModuleCurrent_Type=Integer32
_VpwrModuleCurrent_Object=MibTableColumn
vpwrModuleCurrent=_VpwrModuleCurrent_Object((1,3,6,1,4,1,13858,2,1,6,1,4),_VpwrModuleCurrent_Type())
vpwrModuleCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleCurrent.setStatus(_A)
class _VpwrModuleOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_L,0),(_M,1),('moduleStatusDisabled',2),('moduleStatusRingerAOn',3),('moduleStatusRingerBOn',4),('moduleStatusUnknown',5)))
_VpwrModuleOperStatus_Type.__name__=_F
_VpwrModuleOperStatus_Object=MibTableColumn
vpwrModuleOperStatus=_VpwrModuleOperStatus_Object((1,3,6,1,4,1,13858,2,1,6,1,5),_VpwrModuleOperStatus_Type())
vpwrModuleOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleOperStatus.setStatus(_A)
_VpwrModuleCapacity_Type=Integer32
_VpwrModuleCapacity_Object=MibTableColumn
vpwrModuleCapacity=_VpwrModuleCapacity_Object((1,3,6,1,4,1,13858,2,1,6,1,6),_VpwrModuleCapacity_Type())
vpwrModuleCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleCapacity.setStatus(_A)
_VpwrSystemConfigGroup_ObjectIdentity=ObjectIdentity
vpwrSystemConfigGroup=_VpwrSystemConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,2))
class _VpwrSystemTempCompensation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_VpwrSystemTempCompensation_Type.__name__=_F
_VpwrSystemTempCompensation_Object=MibScalar
vpwrSystemTempCompensation=_VpwrSystemTempCompensation_Object((1,3,6,1,4,1,13858,2,2,1),_VpwrSystemTempCompensation_Type())
vpwrSystemTempCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemTempCompensation.setStatus(_A)
class _VpwrSystemTempCompStartTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,60))
_VpwrSystemTempCompStartTemperature_Type.__name__=_F
_VpwrSystemTempCompStartTemperature_Object=MibScalar
vpwrSystemTempCompStartTemperature=_VpwrSystemTempCompStartTemperature_Object((1,3,6,1,4,1,13858,2,2,2),_VpwrSystemTempCompStartTemperature_Type())
vpwrSystemTempCompStartTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemTempCompStartTemperature.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemTempCompStartTemperature.setUnits(_I)
_VpwrSystemTempCompStopVoltage_Type=Integer32
_VpwrSystemTempCompStopVoltage_Object=MibScalar
vpwrSystemTempCompStopVoltage=_VpwrSystemTempCompStopVoltage_Object((1,3,6,1,4,1,13858,2,2,3),_VpwrSystemTempCompStopVoltage_Type())
vpwrSystemTempCompStopVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemTempCompStopVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemTempCompStopVoltage.setUnits(_H)
class _VpwrSystemTempCompensationSlope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_VpwrSystemTempCompensationSlope_Type.__name__=_F
_VpwrSystemTempCompensationSlope_Object=MibScalar
vpwrSystemTempCompensationSlope=_VpwrSystemTempCompensationSlope_Object((1,3,6,1,4,1,13858,2,2,4),_VpwrSystemTempCompensationSlope_Type())
vpwrSystemTempCompensationSlope.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemTempCompensationSlope.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemTempCompensationSlope.setUnits(_N)
class _VpwrSystemThermalSenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_VpwrSystemThermalSenseType_Type.__name__=_F
_VpwrSystemThermalSenseType_Object=MibScalar
vpwrSystemThermalSenseType=_VpwrSystemThermalSenseType_Object((1,3,6,1,4,1,13858,2,2,5),_VpwrSystemThermalSenseType_Type())
vpwrSystemThermalSenseType.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemThermalSenseType.setStatus(_A)
_VpwrSystemHVAlarmSetpoint_Type=Integer32
_VpwrSystemHVAlarmSetpoint_Object=MibScalar
vpwrSystemHVAlarmSetpoint=_VpwrSystemHVAlarmSetpoint_Object((1,3,6,1,4,1,13858,2,2,6),_VpwrSystemHVAlarmSetpoint_Type())
vpwrSystemHVAlarmSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemHVAlarmSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemHVAlarmSetpoint.setUnits(_H)
_VpwrSystemBDAlarmSetpoint_Type=Integer32
_VpwrSystemBDAlarmSetpoint_Object=MibScalar
vpwrSystemBDAlarmSetpoint=_VpwrSystemBDAlarmSetpoint_Object((1,3,6,1,4,1,13858,2,2,7),_VpwrSystemBDAlarmSetpoint_Type())
vpwrSystemBDAlarmSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemBDAlarmSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemBDAlarmSetpoint.setUnits(_H)
_VpwrSystemInternalTempLThreshold_Type=Integer32
_VpwrSystemInternalTempLThreshold_Object=MibScalar
vpwrSystemInternalTempLThreshold=_VpwrSystemInternalTempLThreshold_Object((1,3,6,1,4,1,13858,2,2,8),_VpwrSystemInternalTempLThreshold_Type())
vpwrSystemInternalTempLThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemInternalTempLThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemInternalTempLThreshold.setUnits(_I)
_VpwrSystemInternalTempUThreshold_Type=Integer32
_VpwrSystemInternalTempUThreshold_Object=MibScalar
vpwrSystemInternalTempUThreshold=_VpwrSystemInternalTempUThreshold_Object((1,3,6,1,4,1,13858,2,2,9),_VpwrSystemInternalTempUThreshold_Type())
vpwrSystemInternalTempUThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrSystemInternalTempUThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemInternalTempUThreshold.setUnits(_I)
_VpwrSystemParameterGroup_ObjectIdentity=ObjectIdentity
vpwrSystemParameterGroup=_VpwrSystemParameterGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,3))
class _VpwrSystemShelfCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_VpwrSystemShelfCapacity_Type.__name__=_F
_VpwrSystemShelfCapacity_Object=MibScalar
vpwrSystemShelfCapacity=_VpwrSystemShelfCapacity_Object((1,3,6,1,4,1,13858,2,3,1),_VpwrSystemShelfCapacity_Type())
vpwrSystemShelfCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemShelfCapacity.setStatus(_A)
_VpwrSystemVoltage_Type=Integer32
_VpwrSystemVoltage_Object=MibScalar
vpwrSystemVoltage=_VpwrSystemVoltage_Object((1,3,6,1,4,1,13858,2,3,2),_VpwrSystemVoltage_Type())
vpwrSystemVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemVoltage.setUnits(_H)
_VpwrSystemCurrent_Type=Integer32
_VpwrSystemCurrent_Object=MibScalar
vpwrSystemCurrent=_VpwrSystemCurrent_Object((1,3,6,1,4,1,13858,2,3,3),_VpwrSystemCurrent_Type())
vpwrSystemCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemCurrent.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemCurrent.setUnits(' Amperes')
class _VpwrSystemControllerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('systemControllerStateUnknown',0),('systemControllerStateNormal',1),('systemControllerStateChange',2),('systemControllerStateAlarm',3),('systemControllerStateMenu',4),('systemControllerStateIrActive',5)))
_VpwrSystemControllerState_Type.__name__=_F
_VpwrSystemControllerState_Object=MibScalar
vpwrSystemControllerState=_VpwrSystemControllerState_Object((1,3,6,1,4,1,13858,2,3,4),_VpwrSystemControllerState_Type())
vpwrSystemControllerState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemControllerState.setStatus(_A)
_VpwrSystemInternalTemperature_Type=Integer32
_VpwrSystemInternalTemperature_Object=MibScalar
vpwrSystemInternalTemperature=_VpwrSystemInternalTemperature_Object((1,3,6,1,4,1,13858,2,3,5),_VpwrSystemInternalTemperature_Type())
vpwrSystemInternalTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemInternalTemperature.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemInternalTemperature.setUnits(_I)
class _VpwrSystemTempCompensationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('systemTempCompInactive',0),('systemTempCompActive',1)))
_VpwrSystemTempCompensationState_Type.__name__=_F
_VpwrSystemTempCompensationState_Object=MibScalar
vpwrSystemTempCompensationState=_VpwrSystemTempCompensationState_Object((1,3,6,1,4,1,13858,2,3,6),_VpwrSystemTempCompensationState_Type())
vpwrSystemTempCompensationState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemTempCompensationState.setStatus(_A)
class _VpwrSystemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('sysTypeUnknow',0),('sysType48V',1),('sysType24V',2),('sysType12V',3)))
_VpwrSystemType_Type.__name__=_F
_VpwrSystemType_Object=MibScalar
vpwrSystemType=_VpwrSystemType_Object((1,3,6,1,4,1,13858,2,3,7),_VpwrSystemType_Type())
vpwrSystemType.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemType.setStatus(_A)
_VpwrSystemPanelIdentGroup_ObjectIdentity=ObjectIdentity
vpwrSystemPanelIdentGroup=_VpwrSystemPanelIdentGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,4))
_VpwrPanelIdentTable_Object=MibTable
vpwrPanelIdentTable=_VpwrPanelIdentTable_Object((1,3,6,1,4,1,13858,2,4,1))
if mibBuilder.loadTexts:vpwrPanelIdentTable.setStatus(_A)
_VpwrPanelIdentEntry_Object=MibTableRow
vpwrPanelIdentEntry=_VpwrPanelIdentEntry_Object((1,3,6,1,4,1,13858,2,4,1,1))
vpwrPanelIdentEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:vpwrPanelIdentEntry.setStatus(_A)
_VpwrPanelBayIndex_Type=PositiveInteger
_VpwrPanelBayIndex_Object=MibTableColumn
vpwrPanelBayIndex=_VpwrPanelBayIndex_Object((1,3,6,1,4,1,13858,2,4,1,1,1),_VpwrPanelBayIndex_Type())
vpwrPanelBayIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelBayIndex.setStatus(_A)
_VpwrPanelModuleIndex_Type=PositiveInteger
_VpwrPanelModuleIndex_Object=MibTableColumn
vpwrPanelModuleIndex=_VpwrPanelModuleIndex_Object((1,3,6,1,4,1,13858,2,4,1,1,2),_VpwrPanelModuleIndex_Type())
vpwrPanelModuleIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleIndex.setStatus(_A)
_VpwrPanelModuleOID_Type=ObjectIdentifier
_VpwrPanelModuleOID_Object=MibTableColumn
vpwrPanelModuleOID=_VpwrPanelModuleOID_Object((1,3,6,1,4,1,13858,2,4,1,1,3),_VpwrPanelModuleOID_Type())
vpwrPanelModuleOID.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleOID.setStatus(_A)
_VpwrPanelModuleCurrent_Type=Integer32
_VpwrPanelModuleCurrent_Object=MibTableColumn
vpwrPanelModuleCurrent=_VpwrPanelModuleCurrent_Object((1,3,6,1,4,1,13858,2,4,1,1,4),_VpwrPanelModuleCurrent_Type())
vpwrPanelModuleCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleCurrent.setStatus(_A)
class _VpwrPanelModuleOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_VpwrPanelModuleOperStatus_Type.__name__=_F
_VpwrPanelModuleOperStatus_Object=MibTableColumn
vpwrPanelModuleOperStatus=_VpwrPanelModuleOperStatus_Object((1,3,6,1,4,1,13858,2,4,1,1,5),_VpwrPanelModuleOperStatus_Type())
vpwrPanelModuleOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleOperStatus.setStatus(_A)
_VpwrPanelModuleCapacity_Type=Integer32
_VpwrPanelModuleCapacity_Object=MibTableColumn
vpwrPanelModuleCapacity=_VpwrPanelModuleCapacity_Object((1,3,6,1,4,1,13858,2,4,1,1,6),_VpwrPanelModuleCapacity_Type())
vpwrPanelModuleCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleCapacity.setStatus(_A)
_VpwrSystemBayctrlIdentGroup_ObjectIdentity=ObjectIdentity
vpwrSystemBayctrlIdentGroup=_VpwrSystemBayctrlIdentGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,5))
_VpwrBayctrlIdentTable_Object=MibTable
vpwrBayctrlIdentTable=_VpwrBayctrlIdentTable_Object((1,3,6,1,4,1,13858,2,5,1))
if mibBuilder.loadTexts:vpwrBayctrlIdentTable.setStatus(_A)
_VpwrBayctrlIdentEntry_Object=MibTableRow
vpwrBayctrlIdentEntry=_VpwrBayctrlIdentEntry_Object((1,3,6,1,4,1,13858,2,5,1,1))
vpwrBayctrlIdentEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:vpwrBayctrlIdentEntry.setStatus(_A)
_VpwrBayctrlIndex_Type=PositiveInteger
_VpwrBayctrlIndex_Object=MibTableColumn
vpwrBayctrlIndex=_VpwrBayctrlIndex_Object((1,3,6,1,4,1,13858,2,5,1,1,1),_VpwrBayctrlIndex_Type())
vpwrBayctrlIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlIndex.setStatus(_A)
_VpwrBayctrlOID_Type=ObjectIdentifier
_VpwrBayctrlOID_Object=MibTableColumn
vpwrBayctrlOID=_VpwrBayctrlOID_Object((1,3,6,1,4,1,13858,2,5,1,1,2),_VpwrBayctrlOID_Type())
vpwrBayctrlOID.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlOID.setStatus(_A)
_VpwrBayctrlCurrent_Type=Integer32
_VpwrBayctrlCurrent_Object=MibTableColumn
vpwrBayctrlCurrent=_VpwrBayctrlCurrent_Object((1,3,6,1,4,1,13858,2,5,1,1,3),_VpwrBayctrlCurrent_Type())
vpwrBayctrlCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlCurrent.setStatus(_A)
class _VpwrBayctrlOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_VpwrBayctrlOperStatus_Type.__name__=_F
_VpwrBayctrlOperStatus_Object=MibTableColumn
vpwrBayctrlOperStatus=_VpwrBayctrlOperStatus_Object((1,3,6,1,4,1,13858,2,5,1,1,4),_VpwrBayctrlOperStatus_Type())
vpwrBayctrlOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlOperStatus.setStatus(_A)
_VpwrBayctrlCapacity_Type=Integer32
_VpwrBayctrlCapacity_Object=MibTableColumn
vpwrBayctrlCapacity=_VpwrBayctrlCapacity_Object((1,3,6,1,4,1,13858,2,5,1,1,5),_VpwrBayctrlCapacity_Type())
vpwrBayctrlCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlCapacity.setStatus(_A)
_VpwrDcPowerRectifier_ObjectIdentity=ObjectIdentity
vpwrDcPowerRectifier=_VpwrDcPowerRectifier_ObjectIdentity((1,3,6,1,4,1,13858,3))
_VpwrRectifierConfigGroup_ObjectIdentity=ObjectIdentity
vpwrRectifierConfigGroup=_VpwrRectifierConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,3,1))
_VpwrRectifierFVSetpoint_Type=Integer32
_VpwrRectifierFVSetpoint_Object=MibScalar
vpwrRectifierFVSetpoint=_VpwrRectifierFVSetpoint_Object((1,3,6,1,4,1,13858,3,1,1),_VpwrRectifierFVSetpoint_Type())
vpwrRectifierFVSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrRectifierFVSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrRectifierFVSetpoint.setUnits(_H)
_VpwrRectifierHVSDSetpoint_Type=Integer32
_VpwrRectifierHVSDSetpoint_Object=MibScalar
vpwrRectifierHVSDSetpoint=_VpwrRectifierHVSDSetpoint_Object((1,3,6,1,4,1,13858,3,1,2),_VpwrRectifierHVSDSetpoint_Type())
vpwrRectifierHVSDSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrRectifierHVSDSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrRectifierHVSDSetpoint.setUnits(_H)
class _VpwrRectifierCurrentLimitAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('rectCurrentLimitDisabled',0),('rectCurrentLimitEnabled',1)))
_VpwrRectifierCurrentLimitAdminState_Type.__name__=_F
_VpwrRectifierCurrentLimitAdminState_Object=MibScalar
vpwrRectifierCurrentLimitAdminState=_VpwrRectifierCurrentLimitAdminState_Object((1,3,6,1,4,1,13858,3,1,3),_VpwrRectifierCurrentLimitAdminState_Type())
vpwrRectifierCurrentLimitAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrRectifierCurrentLimitAdminState.setStatus(_A)
class _VpwrRectifierCurrentLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,200))
_VpwrRectifierCurrentLimit_Type.__name__=_F
_VpwrRectifierCurrentLimit_Object=MibScalar
vpwrRectifierCurrentLimit=_VpwrRectifierCurrentLimit_Object((1,3,6,1,4,1,13858,3,1,4),_VpwrRectifierCurrentLimit_Type())
vpwrRectifierCurrentLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrRectifierCurrentLimit.setStatus(_A)
if mibBuilder.loadTexts:vpwrRectifierCurrentLimit.setUnits('Amperes')
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
vpwrLvdWarningSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrLvdWarningSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdWarningSetpoint.setUnits(_Z)
_VpwrLvdDisconnectSetpoint_Type=Integer32
_VpwrLvdDisconnectSetpoint_Object=MibScalar
vpwrLvdDisconnectSetpoint=_VpwrLvdDisconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,2),_VpwrLvdDisconnectSetpoint_Type())
vpwrLvdDisconnectSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrLvdDisconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdDisconnectSetpoint.setUnits(_H)
_VpwrLvdReconnectSetpoint_Type=Integer32
_VpwrLvdReconnectSetpoint_Object=MibScalar
vpwrLvdReconnectSetpoint=_VpwrLvdReconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,3),_VpwrLvdReconnectSetpoint_Type())
vpwrLvdReconnectSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrLvdReconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdReconnectSetpoint.setUnits(_H)
class _VpwrLvdReconnectDelayTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,240))
_VpwrLvdReconnectDelayTimer_Type.__name__=_F
_VpwrLvdReconnectDelayTimer_Object=MibScalar
vpwrLvdReconnectDelayTimer=_VpwrLvdReconnectDelayTimer_Object((1,3,6,1,4,1,13858,4,1,4),_VpwrLvdReconnectDelayTimer_Type())
vpwrLvdReconnectDelayTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrLvdReconnectDelayTimer.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdReconnectDelayTimer.setUnits(_a)
_VpwrLvdContactorConfigTable_Object=MibTable
vpwrLvdContactorConfigTable=_VpwrLvdContactorConfigTable_Object((1,3,6,1,4,1,13858,4,1,5))
if mibBuilder.loadTexts:vpwrLvdContactorConfigTable.setStatus(_A)
_VpwrLvdContactorConfigEntry_Object=MibTableRow
vpwrLvdContactorConfigEntry=_VpwrLvdContactorConfigEntry_Object((1,3,6,1,4,1,13858,4,1,5,1))
vpwrLvdContactorConfigEntry.setIndexNames((0,_B,_K),(0,_B,_J),(0,_B,_b))
if mibBuilder.loadTexts:vpwrLvdContactorConfigEntry.setStatus(_A)
_VpwrLvdContactorIndex_Type=PositiveInteger
_VpwrLvdContactorIndex_Object=MibTableColumn
vpwrLvdContactorIndex=_VpwrLvdContactorIndex_Object((1,3,6,1,4,1,13858,4,1,5,1,1),_VpwrLvdContactorIndex_Type())
vpwrLvdContactorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvdContactorIndex.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdContactorIndex.setUnits(' None')
_VpwrLvdContactorWarningSetpoint_Type=PositiveInteger
_VpwrLvdContactorWarningSetpoint_Object=MibTableColumn
vpwrLvdContactorWarningSetpoint=_VpwrLvdContactorWarningSetpoint_Object((1,3,6,1,4,1,13858,4,1,5,1,2),_VpwrLvdContactorWarningSetpoint_Type())
vpwrLvdContactorWarningSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrLvdContactorWarningSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdContactorWarningSetpoint.setUnits(_Z)
_VpwrLvdContactorDisconnectSetpoint_Type=PositiveInteger
_VpwrLvdContactorDisconnectSetpoint_Object=MibTableColumn
vpwrLvdContactorDisconnectSetpoint=_VpwrLvdContactorDisconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,5,1,3),_VpwrLvdContactorDisconnectSetpoint_Type())
vpwrLvdContactorDisconnectSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrLvdContactorDisconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdContactorDisconnectSetpoint.setUnits(_H)
_VpwrLvdContactorReconnectSetpoint_Type=PositiveInteger
_VpwrLvdContactorReconnectSetpoint_Object=MibTableColumn
vpwrLvdContactorReconnectSetpoint=_VpwrLvdContactorReconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,5,1,4),_VpwrLvdContactorReconnectSetpoint_Type())
vpwrLvdContactorReconnectSetpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrLvdContactorReconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdContactorReconnectSetpoint.setUnits(_H)
class _VpwrLvdContactorReconnectDelayTimer_Type(PositiveInteger):subtypeSpec=PositiveInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_VpwrLvdContactorReconnectDelayTimer_Type.__name__=_c
_VpwrLvdContactorReconnectDelayTimer_Object=MibTableColumn
vpwrLvdContactorReconnectDelayTimer=_VpwrLvdContactorReconnectDelayTimer_Object((1,3,6,1,4,1,13858,4,1,5,1,5),_VpwrLvdContactorReconnectDelayTimer_Type())
vpwrLvdContactorReconnectDelayTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrLvdContactorReconnectDelayTimer.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdContactorReconnectDelayTimer.setUnits(_a)
class _VpwrLvdContactorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('contactorOpen',0),('contactorClose',1)))
_VpwrLvdContactorState_Type.__name__=_F
_VpwrLvdContactorState_Object=MibTableColumn
vpwrLvdContactorState=_VpwrLvdContactorState_Object((1,3,6,1,4,1,13858,4,1,5,1,6),_VpwrLvdContactorState_Type())
vpwrLvdContactorState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrLvdContactorState.setStatus(_A)
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
_VpwrModuleIdentTable_Object=MibTable
vpwrModuleIdentTable=_VpwrModuleIdentTable_Object((1,3,6,1,4,1,13858,6,1))
if mibBuilder.loadTexts:vpwrModuleIdentTable.setStatus(_A)
_VpwrModuleIdentEntry_Object=MibTableRow
vpwrModuleIdentEntry=_VpwrModuleIdentEntry_Object((1,3,6,1,4,1,13858,6,1,1))
if mibBuilder.loadTexts:vpwrModuleIdentEntry.setStatus(_A)
_VpwrModuleSerialNumber_Type=DisplayString
_VpwrModuleSerialNumber_Object=MibTableColumn
vpwrModuleSerialNumber=_VpwrModuleSerialNumber_Object((1,3,6,1,4,1,13858,6,1,1,1),_VpwrModuleSerialNumber_Type())
vpwrModuleSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleSerialNumber.setStatus(_A)
_VpwrModuleModelNumber_Type=DisplayString
_VpwrModuleModelNumber_Object=MibTableColumn
vpwrModuleModelNumber=_VpwrModuleModelNumber_Object((1,3,6,1,4,1,13858,6,1,1,2),_VpwrModuleModelNumber_Type())
vpwrModuleModelNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleModelNumber.setStatus(_A)
_VpwrModuleFwVersion_Type=DisplayString
_VpwrModuleFwVersion_Object=MibTableColumn
vpwrModuleFwVersion=_VpwrModuleFwVersion_Object((1,3,6,1,4,1,13858,6,1,1,3),_VpwrModuleFwVersion_Type())
vpwrModuleFwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleFwVersion.setStatus(_A)
_VpwrModuleTestDate_Type=DisplayString
_VpwrModuleTestDate_Object=MibTableColumn
vpwrModuleTestDate=_VpwrModuleTestDate_Object((1,3,6,1,4,1,13858,6,1,1,4),_VpwrModuleTestDate_Type())
vpwrModuleTestDate.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleTestDate.setStatus(_A)
_VpwrModuleOperHours_Type=Counter32
_VpwrModuleOperHours_Object=MibTableColumn
vpwrModuleOperHours=_VpwrModuleOperHours_Object((1,3,6,1,4,1,13858,6,1,1,5),_VpwrModuleOperHours_Type())
vpwrModuleOperHours.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrModuleOperHours.setStatus(_A)
_VpwrPanelModuleIdentTable_Object=MibTable
vpwrPanelModuleIdentTable=_VpwrPanelModuleIdentTable_Object((1,3,6,1,4,1,13858,6,2))
if mibBuilder.loadTexts:vpwrPanelModuleIdentTable.setStatus(_A)
_VpwrPanelModuleIdentEntry_Object=MibTableRow
vpwrPanelModuleIdentEntry=_VpwrPanelModuleIdentEntry_Object((1,3,6,1,4,1,13858,6,2,1))
if mibBuilder.loadTexts:vpwrPanelModuleIdentEntry.setStatus(_A)
_VpwrPanelModuleSerialNumber_Type=DisplayString
_VpwrPanelModuleSerialNumber_Object=MibTableColumn
vpwrPanelModuleSerialNumber=_VpwrPanelModuleSerialNumber_Object((1,3,6,1,4,1,13858,6,2,1,1),_VpwrPanelModuleSerialNumber_Type())
vpwrPanelModuleSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleSerialNumber.setStatus(_A)
_VpwrPanelModuleModelNumber_Type=DisplayString
_VpwrPanelModuleModelNumber_Object=MibTableColumn
vpwrPanelModuleModelNumber=_VpwrPanelModuleModelNumber_Object((1,3,6,1,4,1,13858,6,2,1,2),_VpwrPanelModuleModelNumber_Type())
vpwrPanelModuleModelNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleModelNumber.setStatus(_A)
_VpwrPanelModuleFwVersion_Type=DisplayString
_VpwrPanelModuleFwVersion_Object=MibTableColumn
vpwrPanelModuleFwVersion=_VpwrPanelModuleFwVersion_Object((1,3,6,1,4,1,13858,6,2,1,3),_VpwrPanelModuleFwVersion_Type())
vpwrPanelModuleFwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleFwVersion.setStatus(_A)
_VpwrPanelModuleTestDate_Type=DisplayString
_VpwrPanelModuleTestDate_Object=MibTableColumn
vpwrPanelModuleTestDate=_VpwrPanelModuleTestDate_Object((1,3,6,1,4,1,13858,6,2,1,4),_VpwrPanelModuleTestDate_Type())
vpwrPanelModuleTestDate.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleTestDate.setStatus(_A)
_VpwrPanelModuleOperHours_Type=Counter32
_VpwrPanelModuleOperHours_Object=MibTableColumn
vpwrPanelModuleOperHours=_VpwrPanelModuleOperHours_Object((1,3,6,1,4,1,13858,6,2,1,5),_VpwrPanelModuleOperHours_Type())
vpwrPanelModuleOperHours.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPanelModuleOperHours.setStatus(_A)
_VpwrBayctrlModuleIdentTable_Object=MibTable
vpwrBayctrlModuleIdentTable=_VpwrBayctrlModuleIdentTable_Object((1,3,6,1,4,1,13858,6,3))
if mibBuilder.loadTexts:vpwrBayctrlModuleIdentTable.setStatus(_A)
_VpwrBayctrlModuleIdentEntry_Object=MibTableRow
vpwrBayctrlModuleIdentEntry=_VpwrBayctrlModuleIdentEntry_Object((1,3,6,1,4,1,13858,6,3,1))
if mibBuilder.loadTexts:vpwrBayctrlModuleIdentEntry.setStatus(_A)
_VpwrBayctrlSerialNumber_Type=DisplayString
_VpwrBayctrlSerialNumber_Object=MibTableColumn
vpwrBayctrlSerialNumber=_VpwrBayctrlSerialNumber_Object((1,3,6,1,4,1,13858,6,3,1,1),_VpwrBayctrlSerialNumber_Type())
vpwrBayctrlSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlSerialNumber.setStatus(_A)
_VpwrBayctrlModelNumber_Type=DisplayString
_VpwrBayctrlModelNumber_Object=MibTableColumn
vpwrBayctrlModelNumber=_VpwrBayctrlModelNumber_Object((1,3,6,1,4,1,13858,6,3,1,2),_VpwrBayctrlModelNumber_Type())
vpwrBayctrlModelNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlModelNumber.setStatus(_A)
_VpwrBayctrlFwVersion_Type=DisplayString
_VpwrBayctrlFwVersion_Object=MibTableColumn
vpwrBayctrlFwVersion=_VpwrBayctrlFwVersion_Object((1,3,6,1,4,1,13858,6,3,1,3),_VpwrBayctrlFwVersion_Type())
vpwrBayctrlFwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlFwVersion.setStatus(_A)
_VpwrBayctrlTestDate_Type=DisplayString
_VpwrBayctrlTestDate_Object=MibTableColumn
vpwrBayctrlTestDate=_VpwrBayctrlTestDate_Object((1,3,6,1,4,1,13858,6,3,1,4),_VpwrBayctrlTestDate_Type())
vpwrBayctrlTestDate.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlTestDate.setStatus(_A)
_VpwrBayctrlOperHours_Type=Counter32
_VpwrBayctrlOperHours_Object=MibTableColumn
vpwrBayctrlOperHours=_VpwrBayctrlOperHours_Object((1,3,6,1,4,1,13858,6,3,1,5),_VpwrBayctrlOperHours_Type())
vpwrBayctrlOperHours.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBayctrlOperHours.setStatus(_A)
_VpwrDcPowerBatteryGroup_ObjectIdentity=ObjectIdentity
vpwrDcPowerBatteryGroup=_VpwrDcPowerBatteryGroup_ObjectIdentity((1,3,6,1,4,1,13858,7))
_VpwrBatteryTempGroup_ObjectIdentity=ObjectIdentity
vpwrBatteryTempGroup=_VpwrBatteryTempGroup_ObjectIdentity((1,3,6,1,4,1,13858,7,1))
_VpwrBatteryTempTable_Object=MibTable
vpwrBatteryTempTable=_VpwrBatteryTempTable_Object((1,3,6,1,4,1,13858,7,1,1))
if mibBuilder.loadTexts:vpwrBatteryTempTable.setStatus(_A)
_VpwrBatteryTempEntry_Object=MibTableRow
vpwrBatteryTempEntry=_VpwrBatteryTempEntry_Object((1,3,6,1,4,1,13858,7,1,1,1))
vpwrBatteryTempEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:vpwrBatteryTempEntry.setStatus(_A)
_VpwrBatteryTempIndex_Type=Integer32
_VpwrBatteryTempIndex_Object=MibTableColumn
vpwrBatteryTempIndex=_VpwrBatteryTempIndex_Object((1,3,6,1,4,1,13858,7,1,1,1,1),_VpwrBatteryTempIndex_Type())
vpwrBatteryTempIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryTempIndex.setStatus(_A)
class _VpwrBatteryTempName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_VpwrBatteryTempName_Type.__name__=_G
_VpwrBatteryTempName_Object=MibTableColumn
vpwrBatteryTempName=_VpwrBatteryTempName_Object((1,3,6,1,4,1,13858,7,1,1,1,2),_VpwrBatteryTempName_Type())
vpwrBatteryTempName.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBatteryTempName.setStatus(_A)
_VpwrBatteryTemp_Type=Integer32
_VpwrBatteryTemp_Object=MibTableColumn
vpwrBatteryTemp=_VpwrBatteryTemp_Object((1,3,6,1,4,1,13858,7,1,1,1,3),_VpwrBatteryTemp_Type())
vpwrBatteryTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryTemp.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryTemp.setUnits(_I)
_VpwrBatteryTempLThreshold_Type=Integer32
_VpwrBatteryTempLThreshold_Object=MibScalar
vpwrBatteryTempLThreshold=_VpwrBatteryTempLThreshold_Object((1,3,6,1,4,1,13858,7,1,2),_VpwrBatteryTempLThreshold_Type())
vpwrBatteryTempLThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBatteryTempLThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryTempLThreshold.setUnits(_I)
_VpwrBatteryTempUThreshold_Type=Integer32
_VpwrBatteryTempUThreshold_Object=MibScalar
vpwrBatteryTempUThreshold=_VpwrBatteryTempUThreshold_Object((1,3,6,1,4,1,13858,7,1,3),_VpwrBatteryTempUThreshold_Type())
vpwrBatteryTempUThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBatteryTempUThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryTempUThreshold.setUnits(_I)
class _BatteryTempCompensation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_BatteryTempCompensation_Type.__name__=_F
_BatteryTempCompensation_Object=MibScalar
batteryTempCompensation=_BatteryTempCompensation_Object((1,3,6,1,4,1,13858,7,1,4),_BatteryTempCompensation_Type())
batteryTempCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompensation.setStatus(_A)
class _BatteryTempCompHighStartTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,60))
_BatteryTempCompHighStartTemperature_Type.__name__=_F
_BatteryTempCompHighStartTemperature_Object=MibScalar
batteryTempCompHighStartTemperature=_BatteryTempCompHighStartTemperature_Object((1,3,6,1,4,1,13858,7,1,5),_BatteryTempCompHighStartTemperature_Type())
batteryTempCompHighStartTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompHighStartTemperature.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompHighStartTemperature.setUnits(_I)
_BatteryTempCompHighStopVoltage_Type=Integer32
_BatteryTempCompHighStopVoltage_Object=MibScalar
batteryTempCompHighStopVoltage=_BatteryTempCompHighStopVoltage_Object((1,3,6,1,4,1,13858,7,1,6),_BatteryTempCompHighStopVoltage_Type())
batteryTempCompHighStopVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompHighStopVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompHighStopVoltage.setUnits(_H)
class _BatteryTempCompHighSlope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_BatteryTempCompHighSlope_Type.__name__=_F
_BatteryTempCompHighSlope_Object=MibScalar
batteryTempCompHighSlope=_BatteryTempCompHighSlope_Object((1,3,6,1,4,1,13858,7,1,7),_BatteryTempCompHighSlope_Type())
batteryTempCompHighSlope.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompHighSlope.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompHighSlope.setUnits(_N)
_BatteryTempCompLowStartTemperature_Type=Integer32
_BatteryTempCompLowStartTemperature_Object=MibScalar
batteryTempCompLowStartTemperature=_BatteryTempCompLowStartTemperature_Object((1,3,6,1,4,1,13858,7,1,8),_BatteryTempCompLowStartTemperature_Type())
batteryTempCompLowStartTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompLowStartTemperature.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompLowStartTemperature.setUnits(_I)
_BatteryTempCompLowStopVoltage_Type=Integer32
_BatteryTempCompLowStopVoltage_Object=MibScalar
batteryTempCompLowStopVoltage=_BatteryTempCompLowStopVoltage_Object((1,3,6,1,4,1,13858,7,1,9),_BatteryTempCompLowStopVoltage_Type())
batteryTempCompLowStopVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompLowStopVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompLowStopVoltage.setUnits(_H)
class _BatteryTempCompLowSlope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_BatteryTempCompLowSlope_Type.__name__=_F
_BatteryTempCompLowSlope_Object=MibScalar
batteryTempCompLowSlope=_BatteryTempCompLowSlope_Object((1,3,6,1,4,1,13858,7,1,10),_BatteryTempCompLowSlope_Type())
batteryTempCompLowSlope.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompLowSlope.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompLowSlope.setUnits(_N)
class _BatteryTempCompRunawayTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,60))
_BatteryTempCompRunawayTemperature_Type.__name__=_F
_BatteryTempCompRunawayTemperature_Object=MibScalar
batteryTempCompRunawayTemperature=_BatteryTempCompRunawayTemperature_Object((1,3,6,1,4,1,13858,7,1,11),_BatteryTempCompRunawayTemperature_Type())
batteryTempCompRunawayTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompRunawayTemperature.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompRunawayTemperature.setUnits(_I)
_BatteryTempCompRunawayStopVoltage_Type=Integer32
_BatteryTempCompRunawayStopVoltage_Object=MibScalar
batteryTempCompRunawayStopVoltage=_BatteryTempCompRunawayStopVoltage_Object((1,3,6,1,4,1,13858,7,1,12),_BatteryTempCompRunawayStopVoltage_Type())
batteryTempCompRunawayStopVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompRunawayStopVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompRunawayStopVoltage.setUnits(_H)
class _BatteryTempCompSenseSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_BatteryTempCompSenseSource_Type.__name__=_F
_BatteryTempCompSenseSource_Object=MibScalar
batteryTempCompSenseSource=_BatteryTempCompSenseSource_Object((1,3,6,1,4,1,13858,7,1,13),_BatteryTempCompSenseSource_Type())
batteryTempCompSenseSource.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTempCompSenseSource.setStatus(_A)
class _BatteryTempCompRunawayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_BatteryTempCompRunawayState_Type.__name__=_F
_BatteryTempCompRunawayState_Object=MibScalar
batteryTempCompRunawayState=_BatteryTempCompRunawayState_Object((1,3,6,1,4,1,13858,7,1,14),_BatteryTempCompRunawayState_Type())
batteryTempCompRunawayState.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompRunawayState.setStatus(_A)
_ThermalProbeTable_Object=MibTable
thermalProbeTable=_ThermalProbeTable_Object((1,3,6,1,4,1,13858,7,1,15))
if mibBuilder.loadTexts:thermalProbeTable.setStatus(_A)
_ThermalProbeEntry_Object=MibTableRow
thermalProbeEntry=_ThermalProbeEntry_Object((1,3,6,1,4,1,13858,7,1,15,1))
if mibBuilder.loadTexts:thermalProbeEntry.setStatus(_A)
class _ThermalProbeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notPresent',0),('present',1),('removed',2),('shorted',3)))
_ThermalProbeState_Type.__name__=_F
_ThermalProbeState_Object=MibTableColumn
thermalProbeState=_ThermalProbeState_Object((1,3,6,1,4,1,13858,7,1,15,1,1),_ThermalProbeState_Type())
thermalProbeState.setMaxAccess(_D)
if mibBuilder.loadTexts:thermalProbeState.setStatus(_A)
_VpwrBatteryCurrentGroup_ObjectIdentity=ObjectIdentity
vpwrBatteryCurrentGroup=_VpwrBatteryCurrentGroup_ObjectIdentity((1,3,6,1,4,1,13858,7,2))
class _VpwrBatteryCurrentLimitAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('battetyCurrentLimitDisabled',0),('battetyCurrentLimitEnabled',1)))
_VpwrBatteryCurrentLimitAdminState_Type.__name__=_F
_VpwrBatteryCurrentLimitAdminState_Object=MibScalar
vpwrBatteryCurrentLimitAdminState=_VpwrBatteryCurrentLimitAdminState_Object((1,3,6,1,4,1,13858,7,2,1),_VpwrBatteryCurrentLimitAdminState_Type())
vpwrBatteryCurrentLimitAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBatteryCurrentLimitAdminState.setStatus(_A)
class _VpwrBattetyCurrentLimitValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,40))
_VpwrBattetyCurrentLimitValue_Type.__name__=_F
_VpwrBattetyCurrentLimitValue_Object=MibScalar
vpwrBattetyCurrentLimitValue=_VpwrBattetyCurrentLimitValue_Object((1,3,6,1,4,1,13858,7,2,2),_VpwrBattetyCurrentLimitValue_Type())
vpwrBattetyCurrentLimitValue.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBattetyCurrentLimitValue.setStatus(_A)
if mibBuilder.loadTexts:vpwrBattetyCurrentLimitValue.setUnits(_e)
class _VpwrBattetyCurrentValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,40))
_VpwrBattetyCurrentValue_Type.__name__=_F
_VpwrBattetyCurrentValue_Object=MibScalar
vpwrBattetyCurrentValue=_VpwrBattetyCurrentValue_Object((1,3,6,1,4,1,13858,7,2,3),_VpwrBattetyCurrentValue_Type())
vpwrBattetyCurrentValue.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBattetyCurrentValue.setStatus(_A)
if mibBuilder.loadTexts:vpwrBattetyCurrentValue.setUnits(_e)
_VpwrBatteryBoostGroup_ObjectIdentity=ObjectIdentity
vpwrBatteryBoostGroup=_VpwrBatteryBoostGroup_ObjectIdentity((1,3,6,1,4,1,13858,7,3))
class _VpwrBoostAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('boostDisabled',0),('boostEnabled',1)))
_VpwrBoostAdminState_Type.__name__=_F
_VpwrBoostAdminState_Object=MibScalar
vpwrBoostAdminState=_VpwrBoostAdminState_Object((1,3,6,1,4,1,13858,7,3,1),_VpwrBoostAdminState_Type())
vpwrBoostAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBoostAdminState.setStatus(_A)
class _VpwrBoostVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7000,11000))
_VpwrBoostVoltage_Type.__name__=_F
_VpwrBoostVoltage_Object=MibScalar
vpwrBoostVoltage=_VpwrBoostVoltage_Object((1,3,6,1,4,1,13858,7,3,2),_VpwrBoostVoltage_Type())
vpwrBoostVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBoostVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBoostVoltage.setUnits(_H)
class _VpwrBoostDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VpwrBoostDuration_Type.__name__=_F
_VpwrBoostDuration_Object=MibScalar
vpwrBoostDuration=_VpwrBoostDuration_Object((1,3,6,1,4,1,13858,7,3,3),_VpwrBoostDuration_Type())
vpwrBoostDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBoostDuration.setStatus(_A)
if mibBuilder.loadTexts:vpwrBoostDuration.setUnits('Hours')
class _VpwrBoostOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('boostInactive',0),('boostActive',1)))
_VpwrBoostOperState_Type.__name__=_F
_VpwrBoostOperState_Object=MibScalar
vpwrBoostOperState=_VpwrBoostOperState_Object((1,3,6,1,4,1,13858,7,3,4),_VpwrBoostOperState_Type())
vpwrBoostOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBoostOperState.setStatus(_A)
_VpwrBatteryDischargeTestGroup_ObjectIdentity=ObjectIdentity
vpwrBatteryDischargeTestGroup=_VpwrBatteryDischargeTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,7,4))
class _VpwrBDTAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bdtDisabled',0),('bdtEnabled',1)))
_VpwrBDTAdminState_Type.__name__=_F
_VpwrBDTAdminState_Object=MibScalar
vpwrBDTAdminState=_VpwrBDTAdminState_Object((1,3,6,1,4,1,13858,7,4,1),_VpwrBDTAdminState_Type())
vpwrBDTAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBDTAdminState.setStatus(_A)
class _VpwrBDTDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(17,50))
_VpwrBDTDuration_Type.__name__=_F
_VpwrBDTDuration_Object=MibScalar
vpwrBDTDuration=_VpwrBDTDuration_Object((1,3,6,1,4,1,13858,7,4,2),_VpwrBDTDuration_Type())
vpwrBDTDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBDTDuration.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTDuration.setUnits('Minutes')
class _VpwrBDTAlarmVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7000,11000))
_VpwrBDTAlarmVoltage_Type.__name__=_F
_VpwrBDTAlarmVoltage_Object=MibScalar
vpwrBDTAlarmVoltage=_VpwrBDTAlarmVoltage_Object((1,3,6,1,4,1,13858,7,4,3),_VpwrBDTAlarmVoltage_Type())
vpwrBDTAlarmVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBDTAlarmVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTAlarmVoltage.setUnits(_H)
class _VpwrBDTAbortVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5600))
_VpwrBDTAbortVoltage_Type.__name__=_F
_VpwrBDTAbortVoltage_Object=MibScalar
vpwrBDTAbortVoltage=_VpwrBDTAbortVoltage_Object((1,3,6,1,4,1,13858,7,4,4),_VpwrBDTAbortVoltage_Type())
vpwrBDTAbortVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBDTAbortVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTAbortVoltage.setUnits(_H)
class _VpwrBDTAlarmCoefficient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_VpwrBDTAlarmCoefficient_Type.__name__=_F
_VpwrBDTAlarmCoefficient_Object=MibScalar
vpwrBDTAlarmCoefficient=_VpwrBDTAlarmCoefficient_Object((1,3,6,1,4,1,13858,7,4,5),_VpwrBDTAlarmCoefficient_Type())
vpwrBDTAlarmCoefficient.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBDTAlarmCoefficient.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTAlarmCoefficient.setUnits('None')
class _VpwrBDTOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bdtInactive',0),('bdtActive',1)))
_VpwrBDTOperState_Type.__name__=_F
_VpwrBDTOperState_Object=MibScalar
vpwrBDTOperState=_VpwrBDTOperState_Object((1,3,6,1,4,1,13858,7,4,6),_VpwrBDTOperState_Type())
vpwrBDTOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBDTOperState.setStatus(_A)
class _VpwrBDTClearAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bdtNoAlarm',0),('bdtAlarmPresent',1)))
_VpwrBDTClearAlarm_Type.__name__=_F
_VpwrBDTClearAlarm_Object=MibScalar
vpwrBDTClearAlarm=_VpwrBDTClearAlarm_Object((1,3,6,1,4,1,13858,7,4,7),_VpwrBDTClearAlarm_Type())
vpwrBDTClearAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrBDTClearAlarm.setStatus(_A)
_VpwrDcPowerAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrDcPowerAlarmGroup=_VpwrDcPowerAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,8))
_VpwrAlarmsPresent_Type=Gauge32
_VpwrAlarmsPresent_Object=MibScalar
vpwrAlarmsPresent=_VpwrAlarmsPresent_Object((1,3,6,1,4,1,13858,8,1),_VpwrAlarmsPresent_Type())
vpwrAlarmsPresent.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrAlarmsPresent.setStatus(_A)
_VpwrAlarmTable_Object=MibTable
vpwrAlarmTable=_VpwrAlarmTable_Object((1,3,6,1,4,1,13858,8,2))
if mibBuilder.loadTexts:vpwrAlarmTable.setStatus(_A)
_VpwrAlarmEntry_Object=MibTableRow
vpwrAlarmEntry=_VpwrAlarmEntry_Object((1,3,6,1,4,1,13858,8,2,1))
vpwrAlarmEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:vpwrAlarmEntry.setStatus(_A)
_VpwrAlarmIndex_Type=PositiveInteger
_VpwrAlarmIndex_Object=MibTableColumn
vpwrAlarmIndex=_VpwrAlarmIndex_Object((1,3,6,1,4,1,13858,8,2,1,1),_VpwrAlarmIndex_Type())
vpwrAlarmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrAlarmIndex.setStatus(_A)
_VpwrAlarmDescr_Type=AutonomousType
_VpwrAlarmDescr_Object=MibTableColumn
vpwrAlarmDescr=_VpwrAlarmDescr_Object((1,3,6,1,4,1,13858,8,2,1,2),_VpwrAlarmDescr_Type())
vpwrAlarmDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrAlarmDescr.setStatus(_A)
_VpwrAlarmTime_Type=TimeStamp
_VpwrAlarmTime_Object=MibTableColumn
vpwrAlarmTime=_VpwrAlarmTime_Object((1,3,6,1,4,1,13858,8,2,1,3),_VpwrAlarmTime_Type())
vpwrAlarmTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrAlarmTime.setStatus(_A)
_SysRelayConfigTable_Object=MibTable
sysRelayConfigTable=_SysRelayConfigTable_Object((1,3,6,1,4,1,13858,8,3))
if mibBuilder.loadTexts:sysRelayConfigTable.setStatus(_A)
_SysRelayConfigEntry_Object=MibTableRow
sysRelayConfigEntry=_SysRelayConfigEntry_Object((1,3,6,1,4,1,13858,8,3,1))
sysRelayConfigEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:sysRelayConfigEntry.setStatus(_A)
_SysRelayIndex_Type=Integer32
_SysRelayIndex_Object=MibTableColumn
sysRelayIndex=_SysRelayIndex_Object((1,3,6,1,4,1,13858,8,3,1,1),_SysRelayIndex_Type())
sysRelayIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sysRelayIndex.setStatus(_A)
class _SysRelayDefaultName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysRelayDefaultName_Type.__name__=_G
_SysRelayDefaultName_Object=MibTableColumn
sysRelayDefaultName=_SysRelayDefaultName_Object((1,3,6,1,4,1,13858,8,3,1,2),_SysRelayDefaultName_Type())
sysRelayDefaultName.setMaxAccess(_D)
if mibBuilder.loadTexts:sysRelayDefaultName.setStatus(_A)
class _SysRelayCustomName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysRelayCustomName_Type.__name__=_G
_SysRelayCustomName_Object=MibTableColumn
sysRelayCustomName=_SysRelayCustomName_Object((1,3,6,1,4,1,13858,8,3,1,3),_SysRelayCustomName_Type())
sysRelayCustomName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysRelayCustomName.setStatus(_A)
class _SysRelayAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('alarmNone',0),('alarmMajor',1),('alarmMinor',2),('alarmMajorAndMinor',3)))
_SysRelayAlarmSeverity_Type.__name__=_F
_SysRelayAlarmSeverity_Object=MibTableColumn
sysRelayAlarmSeverity=_SysRelayAlarmSeverity_Object((1,3,6,1,4,1,13858,8,3,1,4),_SysRelayAlarmSeverity_Type())
sysRelayAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:sysRelayAlarmSeverity.setStatus(_A)
_SysAlarmConfigTable_Object=MibTable
sysAlarmConfigTable=_SysAlarmConfigTable_Object((1,3,6,1,4,1,13858,8,4))
if mibBuilder.loadTexts:sysAlarmConfigTable.setStatus(_A)
_SysAlarmConfigEntry_Object=MibTableRow
sysAlarmConfigEntry=_SysAlarmConfigEntry_Object((1,3,6,1,4,1,13858,8,4,1))
sysAlarmConfigEntry.setIndexNames((0,_B,_h))
if mibBuilder.loadTexts:sysAlarmConfigEntry.setStatus(_A)
_SysAlarmIndex_Type=Integer32
_SysAlarmIndex_Object=MibTableColumn
sysAlarmIndex=_SysAlarmIndex_Object((1,3,6,1,4,1,13858,8,4,1,1),_SysAlarmIndex_Type())
sysAlarmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmIndex.setStatus(_A)
class _SysAlarmDefaultName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAlarmDefaultName_Type.__name__=_G
_SysAlarmDefaultName_Object=MibTableColumn
sysAlarmDefaultName=_SysAlarmDefaultName_Object((1,3,6,1,4,1,13858,8,4,1,2),_SysAlarmDefaultName_Type())
sysAlarmDefaultName.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmDefaultName.setStatus(_A)
class _SysAlarmCustomName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAlarmCustomName_Type.__name__=_G
_SysAlarmCustomName_Object=MibTableColumn
sysAlarmCustomName=_SysAlarmCustomName_Object((1,3,6,1,4,1,13858,8,4,1,3),_SysAlarmCustomName_Type())
sysAlarmCustomName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmCustomName.setStatus(_A)
class _SysAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('major',1),('minor',2),(_i,3)))
_SysAlarmSeverity_Type.__name__=_F
_SysAlarmSeverity_Object=MibTableColumn
sysAlarmSeverity=_SysAlarmSeverity_Object((1,3,6,1,4,1,13858,8,4,1,4),_SysAlarmSeverity_Type())
sysAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmSeverity.setStatus(_A)
class _SysAlarmToRelayMapping_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAlarmToRelayMapping_Type.__name__=_G
_SysAlarmToRelayMapping_Object=MibTableColumn
sysAlarmToRelayMapping=_SysAlarmToRelayMapping_Object((1,3,6,1,4,1,13858,8,4,1,5),_SysAlarmToRelayMapping_Type())
sysAlarmToRelayMapping.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmToRelayMapping.setStatus(_A)
class _SysAlarmOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_SysAlarmOperStatus_Type.__name__=_F
_SysAlarmOperStatus_Object=MibTableColumn
sysAlarmOperStatus=_SysAlarmOperStatus_Object((1,3,6,1,4,1,13858,8,4,1,6),_SysAlarmOperStatus_Type())
sysAlarmOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmOperStatus.setStatus(_A)
_SysAuxAlarmConfigTable_Object=MibTable
sysAuxAlarmConfigTable=_SysAuxAlarmConfigTable_Object((1,3,6,1,4,1,13858,8,5))
if mibBuilder.loadTexts:sysAuxAlarmConfigTable.setStatus(_A)
_SysAuxAlarmConfigEntry_Object=MibTableRow
sysAuxAlarmConfigEntry=_SysAuxAlarmConfigEntry_Object((1,3,6,1,4,1,13858,8,5,1))
sysAuxAlarmConfigEntry.setIndexNames((0,_B,_j))
if mibBuilder.loadTexts:sysAuxAlarmConfigEntry.setStatus(_A)
_SysAuxAlarmIndex_Type=Integer32
_SysAuxAlarmIndex_Object=MibTableColumn
sysAuxAlarmIndex=_SysAuxAlarmIndex_Object((1,3,6,1,4,1,13858,8,5,1,1),_SysAuxAlarmIndex_Type())
sysAuxAlarmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAuxAlarmIndex.setStatus(_A)
class _SysAuxAlarmDefaultName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAuxAlarmDefaultName_Type.__name__=_G
_SysAuxAlarmDefaultName_Object=MibTableColumn
sysAuxAlarmDefaultName=_SysAuxAlarmDefaultName_Object((1,3,6,1,4,1,13858,8,5,1,2),_SysAuxAlarmDefaultName_Type())
sysAuxAlarmDefaultName.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAuxAlarmDefaultName.setStatus(_A)
class _SysAuxAlarmCustomName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAuxAlarmCustomName_Type.__name__=_G
_SysAuxAlarmCustomName_Object=MibTableColumn
sysAuxAlarmCustomName=_SysAuxAlarmCustomName_Object((1,3,6,1,4,1,13858,8,5,1,3),_SysAuxAlarmCustomName_Type())
sysAuxAlarmCustomName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAuxAlarmCustomName.setStatus(_A)
class _SysAuxAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('major',1),('minor',2),(_i,3)))
_SysAuxAlarmSeverity_Type.__name__=_F
_SysAuxAlarmSeverity_Object=MibTableColumn
sysAuxAlarmSeverity=_SysAuxAlarmSeverity_Object((1,3,6,1,4,1,13858,8,5,1,4),_SysAuxAlarmSeverity_Type())
sysAuxAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAuxAlarmSeverity.setStatus(_A)
class _SysAuxAlarmToRelayMapping_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAuxAlarmToRelayMapping_Type.__name__=_G
_SysAuxAlarmToRelayMapping_Object=MibTableColumn
sysAuxAlarmToRelayMapping=_SysAuxAlarmToRelayMapping_Object((1,3,6,1,4,1,13858,8,5,1,5),_SysAuxAlarmToRelayMapping_Type())
sysAuxAlarmToRelayMapping.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAuxAlarmToRelayMapping.setStatus(_A)
class _SysAuxAlarmPolarity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('alarmOnOpen',0),('alarmOnClose',1)))
_SysAuxAlarmPolarity_Type.__name__=_F
_SysAuxAlarmPolarity_Object=MibTableColumn
sysAuxAlarmPolarity=_SysAuxAlarmPolarity_Object((1,3,6,1,4,1,13858,8,5,1,6),_SysAuxAlarmPolarity_Type())
sysAuxAlarmPolarity.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAuxAlarmPolarity.setStatus(_A)
class _SysAuxAlarmOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_SysAuxAlarmOperStatus_Type.__name__=_F
_SysAuxAlarmOperStatus_Object=MibTableColumn
sysAuxAlarmOperStatus=_SysAuxAlarmOperStatus_Object((1,3,6,1,4,1,13858,8,5,1,7),_SysAuxAlarmOperStatus_Type())
sysAuxAlarmOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAuxAlarmOperStatus.setStatus(_A)
class _SysAlarmComFailState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),(_k,1),('other',2)))
_SysAlarmComFailState_Type.__name__=_F
_SysAlarmComFailState_Object=MibScalar
sysAlarmComFailState=_SysAlarmComFailState_Object((1,3,6,1,4,1,13858,8,6),_SysAlarmComFailState_Type())
sysAlarmComFailState.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmComFailState.setStatus(_A)
class _SysAlarmIShareState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),(_k,1),('other',2)))
_SysAlarmIShareState_Type.__name__=_F
_SysAlarmIShareState_Object=MibScalar
sysAlarmIShareState=_SysAlarmIShareState_Object((1,3,6,1,4,1,13858,8,7),_SysAlarmIShareState_Type())
sysAlarmIShareState.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmIShareState.setStatus(_A)
class _SysAlarmRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('nPlus1',1),('nPlus2',2)))
_SysAlarmRedundancyState_Type.__name__=_F
_SysAlarmRedundancyState_Object=MibScalar
sysAlarmRedundancyState=_SysAlarmRedundancyState_Object((1,3,6,1,4,1,13858,8,8),_SysAlarmRedundancyState_Type())
sysAlarmRedundancyState.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmRedundancyState.setStatus(_A)
_VpwrDcPowerSnmpConfig_ObjectIdentity=ObjectIdentity
vpwrDcPowerSnmpConfig=_VpwrDcPowerSnmpConfig_ObjectIdentity((1,3,6,1,4,1,13858,9))
_VpwrTrapTable_Object=MibTable
vpwrTrapTable=_VpwrTrapTable_Object((1,3,6,1,4,1,13858,9,1))
if mibBuilder.loadTexts:vpwrTrapTable.setStatus(_A)
_VpwrTrapEntry_Object=MibTableRow
vpwrTrapEntry=_VpwrTrapEntry_Object((1,3,6,1,4,1,13858,9,1,1))
vpwrTrapEntry.setIndexNames((0,_B,_l))
if mibBuilder.loadTexts:vpwrTrapEntry.setStatus(_A)
_VpwrTrapIpIndex_Type=Integer32
_VpwrTrapIpIndex_Object=MibTableColumn
vpwrTrapIpIndex=_VpwrTrapIpIndex_Object((1,3,6,1,4,1,13858,9,1,1,1),_VpwrTrapIpIndex_Type())
vpwrTrapIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrTrapIpIndex.setStatus(_A)
_VpwrTrapIpAddress_Type=IpAddress
_VpwrTrapIpAddress_Object=MibTableColumn
vpwrTrapIpAddress=_VpwrTrapIpAddress_Object((1,3,6,1,4,1,13858,9,1,1,2),_VpwrTrapIpAddress_Type())
vpwrTrapIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrTrapIpAddress.setStatus(_A)
_VpwrTrapCriticality_Type=Integer32
_VpwrTrapCriticality_Object=MibTableColumn
vpwrTrapCriticality=_VpwrTrapCriticality_Object((1,3,6,1,4,1,13858,9,1,1,3),_VpwrTrapCriticality_Type())
vpwrTrapCriticality.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrTrapCriticality.setStatus(_A)
class _VpwrReadCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,8))
_VpwrReadCommunityString_Type.__name__=_G
_VpwrReadCommunityString_Object=MibScalar
vpwrReadCommunityString=_VpwrReadCommunityString_Object((1,3,6,1,4,1,13858,9,2),_VpwrReadCommunityString_Type())
vpwrReadCommunityString.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrReadCommunityString.setStatus(_A)
class _VpwrWriteCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,8))
_VpwrWriteCommunityString_Type.__name__=_G
_VpwrWriteCommunityString_Object=MibScalar
vpwrWriteCommunityString=_VpwrWriteCommunityString_Object((1,3,6,1,4,1,13858,9,3),_VpwrWriteCommunityString_Type())
vpwrWriteCommunityString.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrWriteCommunityString.setStatus(_A)
class _VpwrTrapCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,8))
_VpwrTrapCommunityString_Type.__name__=_G
_VpwrTrapCommunityString_Object=MibScalar
vpwrTrapCommunityString=_VpwrTrapCommunityString_Object((1,3,6,1,4,1,13858,9,4),_VpwrTrapCommunityString_Type())
vpwrTrapCommunityString.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrTrapCommunityString.setStatus(_A)
_VpwrDcPowerTraps_ObjectIdentity=ObjectIdentity
vpwrDcPowerTraps=_VpwrDcPowerTraps_ObjectIdentity((1,3,6,1,4,1,13858,10))
_VpwrDcPowerTrapsMsgString_ObjectIdentity=ObjectIdentity
vpwrDcPowerTrapsMsgString=_VpwrDcPowerTrapsMsgString_ObjectIdentity((1,3,6,1,4,1,13858,11))
class _VpwrTrapsMsgString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_VpwrTrapsMsgString_Type.__name__=_G
_VpwrTrapsMsgString_Object=MibScalar
vpwrTrapsMsgString=_VpwrTrapsMsgString_Object((1,3,6,1,4,1,13858,11,1),_VpwrTrapsMsgString_Type())
vpwrTrapsMsgString.setMaxAccess(_R)
if mibBuilder.loadTexts:vpwrTrapsMsgString.setStatus(_A)
_VpwrTrapUserIpAddress_Type=IpAddress
_VpwrTrapUserIpAddress_Object=MibScalar
vpwrTrapUserIpAddress=_VpwrTrapUserIpAddress_Object((1,3,6,1,4,1,13858,11,2),_VpwrTrapUserIpAddress_Type())
vpwrTrapUserIpAddress.setMaxAccess(_R)
if mibBuilder.loadTexts:vpwrTrapUserIpAddress.setStatus(_A)
_VpwrTrapEventTimeStamp_Type=IpAddress
_VpwrTrapEventTimeStamp_Object=MibScalar
vpwrTrapEventTimeStamp=_VpwrTrapEventTimeStamp_Object((1,3,6,1,4,1,13858,11,3),_VpwrTrapEventTimeStamp_Type())
vpwrTrapEventTimeStamp.setMaxAccess(_R)
if mibBuilder.loadTexts:vpwrTrapEventTimeStamp.setStatus(_A)
_VpwrDcPowerRinger_ObjectIdentity=ObjectIdentity
vpwrDcPowerRinger=_VpwrDcPowerRinger_ObjectIdentity((1,3,6,1,4,1,13858,12))
_VpwrRingerConfigGroup_ObjectIdentity=ObjectIdentity
vpwrRingerConfigGroup=_VpwrRingerConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,12,1))
_VpwrRingerParameterTable_Object=MibTable
vpwrRingerParameterTable=_VpwrRingerParameterTable_Object((1,3,6,1,4,1,13858,12,1,1))
if mibBuilder.loadTexts:vpwrRingerParameterTable.setStatus(_A)
_VpwrRingerParameterEntry_Object=MibTableRow
vpwrRingerParameterEntry=_VpwrRingerParameterEntry_Object((1,3,6,1,4,1,13858,12,1,1,1))
vpwrRingerParameterEntry.setIndexNames((0,_B,_J),(0,_B,_m))
if mibBuilder.loadTexts:vpwrRingerParameterEntry.setStatus(_A)
_VpwrRingerIndex_Type=Integer32
_VpwrRingerIndex_Object=MibTableColumn
vpwrRingerIndex=_VpwrRingerIndex_Object((1,3,6,1,4,1,13858,12,1,1,1,1),_VpwrRingerIndex_Type())
vpwrRingerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRingerIndex.setStatus(_A)
class _VpwrRingerParameterAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ringerDisabled',0),('ringerAOn',1),('ringerBOn',2)))
_VpwrRingerParameterAdminState_Type.__name__=_F
_VpwrRingerParameterAdminState_Object=MibTableColumn
vpwrRingerParameterAdminState=_VpwrRingerParameterAdminState_Object((1,3,6,1,4,1,13858,12,1,1,1,2),_VpwrRingerParameterAdminState_Type())
vpwrRingerParameterAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrRingerParameterAdminState.setStatus(_A)
class _VpwrRingerParameterAcVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7000,11000))
_VpwrRingerParameterAcVoltage_Type.__name__=_F
_VpwrRingerParameterAcVoltage_Object=MibTableColumn
vpwrRingerParameterAcVoltage=_VpwrRingerParameterAcVoltage_Object((1,3,6,1,4,1,13858,12,1,1,1,3),_VpwrRingerParameterAcVoltage_Type())
vpwrRingerParameterAcVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrRingerParameterAcVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrRingerParameterAcVoltage.setUnits(_H)
class _VpwrRingerParameterDcVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5600))
_VpwrRingerParameterDcVoltage_Type.__name__=_F
_VpwrRingerParameterDcVoltage_Object=MibTableColumn
vpwrRingerParameterDcVoltage=_VpwrRingerParameterDcVoltage_Object((1,3,6,1,4,1,13858,12,1,1,1,4),_VpwrRingerParameterDcVoltage_Type())
vpwrRingerParameterDcVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrRingerParameterDcVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrRingerParameterDcVoltage.setUnits(_H)
class _VpwrRingerParameterFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(17,50))
_VpwrRingerParameterFrequency_Type.__name__=_F
_VpwrRingerParameterFrequency_Object=MibTableColumn
vpwrRingerParameterFrequency=_VpwrRingerParameterFrequency_Object((1,3,6,1,4,1,13858,12,1,1,1,5),_VpwrRingerParameterFrequency_Type())
vpwrRingerParameterFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwrRingerParameterFrequency.setStatus(_A)
if mibBuilder.loadTexts:vpwrRingerParameterFrequency.setUnits(' Hz')
_VpwrRingerNumberPresent_Type=Gauge32
_VpwrRingerNumberPresent_Object=MibScalar
vpwrRingerNumberPresent=_VpwrRingerNumberPresent_Object((1,3,6,1,4,1,13858,12,1,2),_VpwrRingerNumberPresent_Type())
vpwrRingerNumberPresent.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRingerNumberPresent.setStatus(_A)
_VpwrRingerAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmGroup=_VpwrRingerAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,12,2))
_VpwrRingerAlarmaAFailed_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmaAFailed=_VpwrRingerAlarmaAFailed_ObjectIdentity((1,3,6,1,4,1,13858,12,2,1))
if mibBuilder.loadTexts:vpwrRingerAlarmaAFailed.setStatus(_A)
_VpwrRingerAlarmAOTemp_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmAOTemp=_VpwrRingerAlarmAOTemp_ObjectIdentity((1,3,6,1,4,1,13858,12,2,2))
if mibBuilder.loadTexts:vpwrRingerAlarmAOTemp.setStatus(_A)
_VpwrRingerAlarmAOCurrent_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmAOCurrent=_VpwrRingerAlarmAOCurrent_ObjectIdentity((1,3,6,1,4,1,13858,12,2,3))
if mibBuilder.loadTexts:vpwrRingerAlarmAOCurrent.setStatus(_A)
_VpwrRingerAlarmaBFailed_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmaBFailed=_VpwrRingerAlarmaBFailed_ObjectIdentity((1,3,6,1,4,1,13858,12,2,4))
if mibBuilder.loadTexts:vpwrRingerAlarmaBFailed.setStatus(_A)
_VpwrRingerAlarmBOverTemp_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmBOverTemp=_VpwrRingerAlarmBOverTemp_ObjectIdentity((1,3,6,1,4,1,13858,12,2,5))
if mibBuilder.loadTexts:vpwrRingerAlarmBOverTemp.setStatus(_A)
_VpwrRingerAlarmBOverCurrent_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmBOverCurrent=_VpwrRingerAlarmBOverCurrent_ObjectIdentity((1,3,6,1,4,1,13858,12,2,6))
if mibBuilder.loadTexts:vpwrRingerAlarmBOverCurrent.setStatus(_A)
_VpwrRingerTestGroup_ObjectIdentity=ObjectIdentity
vpwrRingerTestGroup=_VpwrRingerTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,12,3))
_VpwrDcPowerDcDcConverter_ObjectIdentity=ObjectIdentity
vpwrDcPowerDcDcConverter=_VpwrDcPowerDcDcConverter_ObjectIdentity((1,3,6,1,4,1,13858,13))
_VpwrDcDcConverterConfigGroup_ObjectIdentity=ObjectIdentity
vpwrDcDcConverterConfigGroup=_VpwrDcDcConverterConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,13,1))
_VpwrDcDcConverterAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrDcDcConverterAlarmGroup=_VpwrDcDcConverterAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,13,2))
_VpwrDcDcConverterTestGroup_ObjectIdentity=ObjectIdentity
vpwrDcDcConverterTestGroup=_VpwrDcDcConverterTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,13,3))
_VpwrDcPowerDcAcInverter_ObjectIdentity=ObjectIdentity
vpwrDcPowerDcAcInverter=_VpwrDcPowerDcAcInverter_ObjectIdentity((1,3,6,1,4,1,13858,14))
_VpwrDcAcInverterConfigGroup_ObjectIdentity=ObjectIdentity
vpwrDcAcInverterConfigGroup=_VpwrDcAcInverterConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,14,1))
_VpwrDcAcInverterAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrDcAcInverterAlarmGroup=_VpwrDcAcInverterAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,14,2))
_VpwrDcAcInverterTestGroup_ObjectIdentity=ObjectIdentity
vpwrDcAcInverterTestGroup=_VpwrDcAcInverterTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,14,3))
_VpwrDcPowerBayController_ObjectIdentity=ObjectIdentity
vpwrDcPowerBayController=_VpwrDcPowerBayController_ObjectIdentity((1,3,6,1,4,1,13858,15))
_VpwrDcPowerIoModule_ObjectIdentity=ObjectIdentity
vpwrDcPowerIoModule=_VpwrDcPowerIoModule_ObjectIdentity((1,3,6,1,4,1,13858,16))
_VpwrIoModuleConfigGroup_ObjectIdentity=ObjectIdentity
vpwrIoModuleConfigGroup=_VpwrIoModuleConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,16,1))
_VpwrIoModuleAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrIoModuleAlarmGroup=_VpwrIoModuleAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,16,2))
_VpwrIoModuleTestGroup_ObjectIdentity=ObjectIdentity
vpwrIoModuleTestGroup=_VpwrIoModuleTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,16,3))
_VpwrDcPowerDist_ObjectIdentity=ObjectIdentity
vpwrDcPowerDist=_VpwrDcPowerDist_ObjectIdentity((1,3,6,1,4,1,13858,17))
_VpwrDcPowerTrio_ObjectIdentity=ObjectIdentity
vpwrDcPowerTrio=_VpwrDcPowerTrio_ObjectIdentity((1,3,6,1,4,1,13858,18))
vpwrSystemIdentEntry.registerAugmentions((_B,_n))
vpwrModuleIdentEntry.setIndexNames(*vpwrSystemIdentEntry.getIndexNames())
VpwrPanelIdentEntry.registerAugmentions((_B,_o))
vpwrPanelModuleIdentEntry.setIndexNames(*VpwrPanelIdentEntry.getIndexNames())
VpwrBayctrlIdentEntry.registerAugmentions((_B,_p))
vpwrBayctrlModuleIdentEntry.setIndexNames(*VpwrBayctrlIdentEntry.getIndexNames())
vpwrBatteryTempEntry.registerAugmentions((_B,_q))
thermalProbeEntry.setIndexNames(*vpwrBatteryTempEntry.getIndexNames())
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
vpwrTrapModuleInserted.setObjects(*((_B,_E),(_B,_K),(_B,_J)))
if mibBuilder.loadTexts:vpwrTrapModuleInserted.setStatus('')
vpwrTrapModuleRemoved=NotificationType((1,3,6,1,4,1,13858,10,0,19))
vpwrTrapModuleRemoved.setObjects(*((_B,_E),(_B,_K),(_B,_J)))
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
vpwrTrapLoginFail=NotificationType((1,3,6,1,4,1,13858,10,0,26))
vpwrTrapLoginFail.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapLoginFail.setStatus('')
vpwrTrapLoginSuccess=NotificationType((1,3,6,1,4,1,13858,10,0,27))
vpwrTrapLoginSuccess.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapLoginSuccess.setStatus('')
vpwrTrapLogout=NotificationType((1,3,6,1,4,1,13858,10,0,28))
vpwrTrapLogout.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapLogout.setStatus('')
vpwrTrapAdminPwdChange=NotificationType((1,3,6,1,4,1,13858,10,0,29))
vpwrTrapAdminPwdChange.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapAdminPwdChange.setStatus('')
vpwrTrapIllegalConfigSubmit=NotificationType((1,3,6,1,4,1,13858,10,0,30))
vpwrTrapIllegalConfigSubmit.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapIllegalConfigSubmit.setStatus('')
vpwrTrapCfgChange=NotificationType((1,3,6,1,4,1,13858,10,0,31))
vpwrTrapCfgChange.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapCfgChange.setStatus('')
vpwrTrapClearEventHistory=NotificationType((1,3,6,1,4,1,13858,10,0,32))
vpwrTrapClearEventHistory.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapClearEventHistory.setStatus('')
vpwrTrapSwDownloadNoReboot=NotificationType((1,3,6,1,4,1,13858,10,0,33))
vpwrTrapSwDownloadNoReboot.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapSwDownloadNoReboot.setStatus('')
vpwrTrapSwDownloadAndReboot=NotificationType((1,3,6,1,4,1,13858,10,0,34))
vpwrTrapSwDownloadAndReboot.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapSwDownloadAndReboot.setStatus('')
vpwrTrapSystemClockChange=NotificationType((1,3,6,1,4,1,13858,10,0,35))
vpwrTrapSystemClockChange.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapSystemClockChange.setStatus('')
vpwrTrapModuleAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,36))
vpwrTrapModuleAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapModuleAlarm.setStatus('')
vpwrTrapOIDChange=NotificationType((1,3,6,1,4,1,13858,10,0,37))
vpwrTrapOIDChange.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapOIDChange.setStatus('')
vpwrTrapThermalRunaway=NotificationType((1,3,6,1,4,1,13858,10,0,38))
vpwrTrapThermalRunaway.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapThermalRunaway.setStatus('')
vpwrTrapBatteryDischargeTestAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,39))
vpwrTrapBatteryDischargeTestAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapBatteryDischargeTestAlarm.setStatus('')
vpwrTrapRingerAAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,40))
vpwrTrapRingerAAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapRingerAAlarm.setStatus('')
vpwrTrapRingerBAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,41))
vpwrTrapRingerBAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapRingerBAlarm.setStatus('')
vpwrTrapSingleRingerAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,42))
vpwrTrapSingleRingerAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapSingleRingerAlarm.setStatus('')
vpwrTrapMultipleRingerAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,43))
vpwrTrapMultipleRingerAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapMultipleRingerAlarm.setStatus('')
vpwrTrapThermalProbeAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,44))
vpwrTrapThermalProbeAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapThermalProbeAlarm.setStatus('')
vpwrTrapRingerCommAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,45))
vpwrTrapRingerCommAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapRingerCommAlarm.setStatus('')
vpwrTrapDistributionCommAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,46))
vpwrTrapDistributionCommAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapDistributionCommAlarm.setStatus('')
vpwrTrapConverterAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,47))
vpwrTrapConverterAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapConverterAlarm.setStatus('')
vpwrTrapMultipleConvFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,48))
vpwrTrapMultipleConvFailAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapMultipleConvFailAlarm.setStatus('')
vpwrTrapUnmappedAddressAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,49))
vpwrTrapUnmappedAddressAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapUnmappedAddressAlarm.setStatus('')
vpwrTrapConfigErrorAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,50))
vpwrTrapConfigErrorAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapConfigErrorAlarm.setStatus('')
vpwrTrapDisplayFirmwareMismatchAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,51))
vpwrTrapDisplayFirmwareMismatchAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapDisplayFirmwareMismatchAlarm.setStatus('')
vpwrTrapConverterInputFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,52))
vpwrTrapConverterInputFailAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapConverterInputFailAlarm.setStatus('')
vpwrTrapBatteryRechgIlimitFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,0,53))
vpwrTrapBatteryRechgIlimitFailAlarm.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapBatteryRechgIlimitFailAlarm.setStatus('')
vpwrTrapSystemAlive=NotificationType((1,3,6,1,4,1,13858,10,0,54))
vpwrTrapSystemAlive.setObjects((_B,_E))
if mibBuilder.loadTexts:vpwrTrapSystemAlive.setStatus('')
mibBuilder.exportSymbols(_B,**{_c:PositiveInteger,'NonNegativeInteger':NonNegativeInteger,'vpwrDcPowerMgt':vpwrDcPowerMgt,'vpwrDcPowerProducts':vpwrDcPowerProducts,'vpwrDcPowerSystem':vpwrDcPowerSystem,'vpwrSystemIdentGroup':vpwrSystemIdentGroup,'vpwrIdentManufacturer':vpwrIdentManufacturer,'vpwrIdentModel':vpwrIdentModel,'vpwrIdentControllerVersion':vpwrIdentControllerVersion,'vpwrIdentAgentSoftwareVersion':vpwrIdentAgentSoftwareVersion,'vpwrIdentName':vpwrIdentName,'vpwrSystemIdentTable':vpwrSystemIdentTable,'vpwrSystemIdentEntry':vpwrSystemIdentEntry,_K:vpwrBayIndex,_J:vpwrModuleIndex,'vpwrModuleOID':vpwrModuleOID,'vpwrModuleCurrent':vpwrModuleCurrent,'vpwrModuleOperStatus':vpwrModuleOperStatus,'vpwrModuleCapacity':vpwrModuleCapacity,'vpwrSystemConfigGroup':vpwrSystemConfigGroup,'vpwrSystemTempCompensation':vpwrSystemTempCompensation,'vpwrSystemTempCompStartTemperature':vpwrSystemTempCompStartTemperature,'vpwrSystemTempCompStopVoltage':vpwrSystemTempCompStopVoltage,'vpwrSystemTempCompensationSlope':vpwrSystemTempCompensationSlope,'vpwrSystemThermalSenseType':vpwrSystemThermalSenseType,'vpwrSystemHVAlarmSetpoint':vpwrSystemHVAlarmSetpoint,'vpwrSystemBDAlarmSetpoint':vpwrSystemBDAlarmSetpoint,'vpwrSystemInternalTempLThreshold':vpwrSystemInternalTempLThreshold,'vpwrSystemInternalTempUThreshold':vpwrSystemInternalTempUThreshold,'vpwrSystemParameterGroup':vpwrSystemParameterGroup,'vpwrSystemShelfCapacity':vpwrSystemShelfCapacity,'vpwrSystemVoltage':vpwrSystemVoltage,'vpwrSystemCurrent':vpwrSystemCurrent,'vpwrSystemControllerState':vpwrSystemControllerState,'vpwrSystemInternalTemperature':vpwrSystemInternalTemperature,'vpwrSystemTempCompensationState':vpwrSystemTempCompensationState,'vpwrSystemType':vpwrSystemType,'vpwrSystemPanelIdentGroup':vpwrSystemPanelIdentGroup,'vpwrPanelIdentTable':vpwrPanelIdentTable,'vpwrPanelIdentEntry':vpwrPanelIdentEntry,_W:vpwrPanelBayIndex,_X:vpwrPanelModuleIndex,'vpwrPanelModuleOID':vpwrPanelModuleOID,'vpwrPanelModuleCurrent':vpwrPanelModuleCurrent,'vpwrPanelModuleOperStatus':vpwrPanelModuleOperStatus,'vpwrPanelModuleCapacity':vpwrPanelModuleCapacity,'vpwrSystemBayctrlIdentGroup':vpwrSystemBayctrlIdentGroup,'vpwrBayctrlIdentTable':vpwrBayctrlIdentTable,'vpwrBayctrlIdentEntry':vpwrBayctrlIdentEntry,_Y:vpwrBayctrlIndex,'vpwrBayctrlOID':vpwrBayctrlOID,'vpwrBayctrlCurrent':vpwrBayctrlCurrent,'vpwrBayctrlOperStatus':vpwrBayctrlOperStatus,'vpwrBayctrlCapacity':vpwrBayctrlCapacity,'vpwrDcPowerRectifier':vpwrDcPowerRectifier,'vpwrRectifierConfigGroup':vpwrRectifierConfigGroup,'vpwrRectifierFVSetpoint':vpwrRectifierFVSetpoint,'vpwrRectifierHVSDSetpoint':vpwrRectifierHVSDSetpoint,'vpwrRectifierCurrentLimitAdminState':vpwrRectifierCurrentLimitAdminState,'vpwrRectifierCurrentLimit':vpwrRectifierCurrentLimit,'vpwrRectifierAlarmGroup':vpwrRectifierAlarmGroup,'vpwrRectAlarmDCFail':vpwrRectAlarmDCFail,'vpwrRectAlarmBoostFail':vpwrRectAlarmBoostFail,'vpwrRectAlarmACFail':vpwrRectAlarmACFail,'vpwrRectAlarmHVSD':vpwrRectAlarmHVSD,'vpwrRectAlarmFanFail':vpwrRectAlarmFanFail,'vpwrRectAlarmAmbTemp':vpwrRectAlarmAmbTemp,'vpwrRectAlarmIntTemp':vpwrRectAlarmIntTemp,'vpwrRectAlarmIShare':vpwrRectAlarmIShare,'vpwrRectAlarmUV':vpwrRectAlarmUV,'vpwrRectAlarmLowVoltage':vpwrRectAlarmLowVoltage,'vpwrRectAlarmReserved':vpwrRectAlarmReserved,'vpwrRectAlarmDCEnable':vpwrRectAlarmDCEnable,'vpwrRectAlarmRemoteShutdown':vpwrRectAlarmRemoteShutdown,'vpwrRectAlarmModDisableShutdown':vpwrRectAlarmModDisableShutdown,'vpwrRectAlarmShortPinShutdown':vpwrRectAlarmShortPinShutdown,'vpwrRectAlarmBoostComm':vpwrRectAlarmBoostComm,'vpwrRectifierTestGroup':vpwrRectifierTestGroup,'vpwrDcPowerLvd':vpwrDcPowerLvd,'vpwrLvdConfigGroup':vpwrLvdConfigGroup,'vpwrLvdWarningSetpoint':vpwrLvdWarningSetpoint,'vpwrLvdDisconnectSetpoint':vpwrLvdDisconnectSetpoint,'vpwrLvdReconnectSetpoint':vpwrLvdReconnectSetpoint,'vpwrLvdReconnectDelayTimer':vpwrLvdReconnectDelayTimer,'vpwrLvdContactorConfigTable':vpwrLvdContactorConfigTable,'vpwrLvdContactorConfigEntry':vpwrLvdContactorConfigEntry,_b:vpwrLvdContactorIndex,'vpwrLvdContactorWarningSetpoint':vpwrLvdContactorWarningSetpoint,'vpwrLvdContactorDisconnectSetpoint':vpwrLvdContactorDisconnectSetpoint,'vpwrLvdContactorReconnectSetpoint':vpwrLvdContactorReconnectSetpoint,'vpwrLvdContactorReconnectDelayTimer':vpwrLvdContactorReconnectDelayTimer,'vpwrLvdContactorState':vpwrLvdContactorState,'vpwrLvdAlarmGroup':vpwrLvdAlarmGroup,'vpwrLvdAlarmContactorOpen':vpwrLvdAlarmContactorOpen,'vpwrLvdAlarmCBOpen':vpwrLvdAlarmCBOpen,'vpwrTrapLvdFuseOpen':vpwrTrapLvdFuseOpen,'vpwrLvdAlarmWarning':vpwrLvdAlarmWarning,'vpwrLvdTestGroup':vpwrLvdTestGroup,'vpwrDcPowerTest':vpwrDcPowerTest,'vpwrDcPowerModuleIdent':vpwrDcPowerModuleIdent,'vpwrModuleIdentTable':vpwrModuleIdentTable,_n:vpwrModuleIdentEntry,'vpwrModuleSerialNumber':vpwrModuleSerialNumber,'vpwrModuleModelNumber':vpwrModuleModelNumber,'vpwrModuleFwVersion':vpwrModuleFwVersion,'vpwrModuleTestDate':vpwrModuleTestDate,'vpwrModuleOperHours':vpwrModuleOperHours,'vpwrPanelModuleIdentTable':vpwrPanelModuleIdentTable,_o:vpwrPanelModuleIdentEntry,'vpwrPanelModuleSerialNumber':vpwrPanelModuleSerialNumber,'vpwrPanelModuleModelNumber':vpwrPanelModuleModelNumber,'vpwrPanelModuleFwVersion':vpwrPanelModuleFwVersion,'vpwrPanelModuleTestDate':vpwrPanelModuleTestDate,'vpwrPanelModuleOperHours':vpwrPanelModuleOperHours,'vpwrBayctrlModuleIdentTable':vpwrBayctrlModuleIdentTable,_p:vpwrBayctrlModuleIdentEntry,'vpwrBayctrlSerialNumber':vpwrBayctrlSerialNumber,'vpwrBayctrlModelNumber':vpwrBayctrlModelNumber,'vpwrBayctrlFwVersion':vpwrBayctrlFwVersion,'vpwrBayctrlTestDate':vpwrBayctrlTestDate,'vpwrBayctrlOperHours':vpwrBayctrlOperHours,'vpwrDcPowerBatteryGroup':vpwrDcPowerBatteryGroup,'vpwrBatteryTempGroup':vpwrBatteryTempGroup,'vpwrBatteryTempTable':vpwrBatteryTempTable,'vpwrBatteryTempEntry':vpwrBatteryTempEntry,_d:vpwrBatteryTempIndex,'vpwrBatteryTempName':vpwrBatteryTempName,'vpwrBatteryTemp':vpwrBatteryTemp,'vpwrBatteryTempLThreshold':vpwrBatteryTempLThreshold,'vpwrBatteryTempUThreshold':vpwrBatteryTempUThreshold,'batteryTempCompensation':batteryTempCompensation,'batteryTempCompHighStartTemperature':batteryTempCompHighStartTemperature,'batteryTempCompHighStopVoltage':batteryTempCompHighStopVoltage,'batteryTempCompHighSlope':batteryTempCompHighSlope,'batteryTempCompLowStartTemperature':batteryTempCompLowStartTemperature,'batteryTempCompLowStopVoltage':batteryTempCompLowStopVoltage,'batteryTempCompLowSlope':batteryTempCompLowSlope,'batteryTempCompRunawayTemperature':batteryTempCompRunawayTemperature,'batteryTempCompRunawayStopVoltage':batteryTempCompRunawayStopVoltage,'batteryTempCompSenseSource':batteryTempCompSenseSource,'batteryTempCompRunawayState':batteryTempCompRunawayState,'thermalProbeTable':thermalProbeTable,_q:thermalProbeEntry,'thermalProbeState':thermalProbeState,'vpwrBatteryCurrentGroup':vpwrBatteryCurrentGroup,'vpwrBatteryCurrentLimitAdminState':vpwrBatteryCurrentLimitAdminState,'vpwrBattetyCurrentLimitValue':vpwrBattetyCurrentLimitValue,'vpwrBattetyCurrentValue':vpwrBattetyCurrentValue,'vpwrBatteryBoostGroup':vpwrBatteryBoostGroup,'vpwrBoostAdminState':vpwrBoostAdminState,'vpwrBoostVoltage':vpwrBoostVoltage,'vpwrBoostDuration':vpwrBoostDuration,'vpwrBoostOperState':vpwrBoostOperState,'vpwrBatteryDischargeTestGroup':vpwrBatteryDischargeTestGroup,'vpwrBDTAdminState':vpwrBDTAdminState,'vpwrBDTDuration':vpwrBDTDuration,'vpwrBDTAlarmVoltage':vpwrBDTAlarmVoltage,'vpwrBDTAbortVoltage':vpwrBDTAbortVoltage,'vpwrBDTAlarmCoefficient':vpwrBDTAlarmCoefficient,'vpwrBDTOperState':vpwrBDTOperState,'vpwrBDTClearAlarm':vpwrBDTClearAlarm,'vpwrDcPowerAlarmGroup':vpwrDcPowerAlarmGroup,'vpwrAlarmsPresent':vpwrAlarmsPresent,'vpwrAlarmTable':vpwrAlarmTable,'vpwrAlarmEntry':vpwrAlarmEntry,_f:vpwrAlarmIndex,'vpwrAlarmDescr':vpwrAlarmDescr,'vpwrAlarmTime':vpwrAlarmTime,'sysRelayConfigTable':sysRelayConfigTable,'sysRelayConfigEntry':sysRelayConfigEntry,_g:sysRelayIndex,'sysRelayDefaultName':sysRelayDefaultName,'sysRelayCustomName':sysRelayCustomName,'sysRelayAlarmSeverity':sysRelayAlarmSeverity,'sysAlarmConfigTable':sysAlarmConfigTable,'sysAlarmConfigEntry':sysAlarmConfigEntry,_h:sysAlarmIndex,'sysAlarmDefaultName':sysAlarmDefaultName,'sysAlarmCustomName':sysAlarmCustomName,'sysAlarmSeverity':sysAlarmSeverity,'sysAlarmToRelayMapping':sysAlarmToRelayMapping,'sysAlarmOperStatus':sysAlarmOperStatus,'sysAuxAlarmConfigTable':sysAuxAlarmConfigTable,'sysAuxAlarmConfigEntry':sysAuxAlarmConfigEntry,_j:sysAuxAlarmIndex,'sysAuxAlarmDefaultName':sysAuxAlarmDefaultName,'sysAuxAlarmCustomName':sysAuxAlarmCustomName,'sysAuxAlarmSeverity':sysAuxAlarmSeverity,'sysAuxAlarmToRelayMapping':sysAuxAlarmToRelayMapping,'sysAuxAlarmPolarity':sysAuxAlarmPolarity,'sysAuxAlarmOperStatus':sysAuxAlarmOperStatus,'sysAlarmComFailState':sysAlarmComFailState,'sysAlarmIShareState':sysAlarmIShareState,'sysAlarmRedundancyState':sysAlarmRedundancyState,'vpwrDcPowerSnmpConfig':vpwrDcPowerSnmpConfig,'vpwrTrapTable':vpwrTrapTable,'vpwrTrapEntry':vpwrTrapEntry,_l:vpwrTrapIpIndex,'vpwrTrapIpAddress':vpwrTrapIpAddress,'vpwrTrapCriticality':vpwrTrapCriticality,'vpwrReadCommunityString':vpwrReadCommunityString,'vpwrWriteCommunityString':vpwrWriteCommunityString,'vpwrTrapCommunityString':vpwrTrapCommunityString,'vpwrDcPowerTraps':vpwrDcPowerTraps,'vpwrTrapPowerMajorAlarm':vpwrTrapPowerMajorAlarm,'vpwrTrapPowerMinorAlarm':vpwrTrapPowerMinorAlarm,'vpwrTrapACFAlarm':vpwrTrapACFAlarm,'vpwrTrapHVAlarm':vpwrTrapHVAlarm,'vpwrTrapHVSDAlarm':vpwrTrapHVSDAlarm,'vpwrTrapBDAlarm':vpwrTrapBDAlarm,'vpwrTrapLVDWarningAlarm':vpwrTrapLVDWarningAlarm,'vpwrTrapLVDOpenAlarm':vpwrTrapLVDOpenAlarm,'vpwrTrapDistAlarm':vpwrTrapDistAlarm,'vpwrTrapAuxAlarm':vpwrTrapAuxAlarm,'vpwrTrapSystemRedundancyAlarm':vpwrTrapSystemRedundancyAlarm,'vpwrTrapIShareAlarm':vpwrTrapIShareAlarm,'vpwrTrapModuleFailAlarm':vpwrTrapModuleFailAlarm,'vpwrTrapMultipleModuleFailAlarm':vpwrTrapMultipleModuleFailAlarm,'vpwrTrapModuleCommAlarm':vpwrTrapModuleCommAlarm,'vpwrTrapSystemOverTemperatureAlarm':vpwrTrapSystemOverTemperatureAlarm,'vpwrTrapSystemOK':vpwrTrapSystemOK,'vpwrTrapModuleInserted':vpwrTrapModuleInserted,'vpwrTrapModuleRemoved':vpwrTrapModuleRemoved,'vpwrTrapThermalCompActive':vpwrTrapThermalCompActive,'vpwrTrapThermalCompInactive':vpwrTrapThermalCompInactive,'vpwrTrapInternalTempAlarmSet':vpwrTrapInternalTempAlarmSet,'vpwrTrapInternalTempAlarmCleared':vpwrTrapInternalTempAlarmCleared,'vpwrTrapBatteryTempAlarmSet':vpwrTrapBatteryTempAlarmSet,'vpwrTrapBatteryTempAlarmCleared':vpwrTrapBatteryTempAlarmCleared,'vpwrTrapLoginFail':vpwrTrapLoginFail,'vpwrTrapLoginSuccess':vpwrTrapLoginSuccess,'vpwrTrapLogout':vpwrTrapLogout,'vpwrTrapAdminPwdChange':vpwrTrapAdminPwdChange,'vpwrTrapIllegalConfigSubmit':vpwrTrapIllegalConfigSubmit,'vpwrTrapCfgChange':vpwrTrapCfgChange,'vpwrTrapClearEventHistory':vpwrTrapClearEventHistory,'vpwrTrapSwDownloadNoReboot':vpwrTrapSwDownloadNoReboot,'vpwrTrapSwDownloadAndReboot':vpwrTrapSwDownloadAndReboot,'vpwrTrapSystemClockChange':vpwrTrapSystemClockChange,'vpwrTrapModuleAlarm':vpwrTrapModuleAlarm,'vpwrTrapOIDChange':vpwrTrapOIDChange,'vpwrTrapThermalRunaway':vpwrTrapThermalRunaway,'vpwrTrapBatteryDischargeTestAlarm':vpwrTrapBatteryDischargeTestAlarm,'vpwrTrapRingerAAlarm':vpwrTrapRingerAAlarm,'vpwrTrapRingerBAlarm':vpwrTrapRingerBAlarm,'vpwrTrapSingleRingerAlarm':vpwrTrapSingleRingerAlarm,'vpwrTrapMultipleRingerAlarm':vpwrTrapMultipleRingerAlarm,'vpwrTrapThermalProbeAlarm':vpwrTrapThermalProbeAlarm,'vpwrTrapRingerCommAlarm':vpwrTrapRingerCommAlarm,'vpwrTrapDistributionCommAlarm':vpwrTrapDistributionCommAlarm,'vpwrTrapConverterAlarm':vpwrTrapConverterAlarm,'vpwrTrapMultipleConvFailAlarm':vpwrTrapMultipleConvFailAlarm,'vpwrTrapUnmappedAddressAlarm':vpwrTrapUnmappedAddressAlarm,'vpwrTrapConfigErrorAlarm':vpwrTrapConfigErrorAlarm,'vpwrTrapDisplayFirmwareMismatchAlarm':vpwrTrapDisplayFirmwareMismatchAlarm,'vpwrTrapConverterInputFailAlarm':vpwrTrapConverterInputFailAlarm,'vpwrTrapBatteryRechgIlimitFailAlarm':vpwrTrapBatteryRechgIlimitFailAlarm,'vpwrTrapSystemAlive':vpwrTrapSystemAlive,'vpwrDcPowerTrapsMsgString':vpwrDcPowerTrapsMsgString,_E:vpwrTrapsMsgString,'vpwrTrapUserIpAddress':vpwrTrapUserIpAddress,'vpwrTrapEventTimeStamp':vpwrTrapEventTimeStamp,'vpwrDcPowerRinger':vpwrDcPowerRinger,'vpwrRingerConfigGroup':vpwrRingerConfigGroup,'vpwrRingerParameterTable':vpwrRingerParameterTable,'vpwrRingerParameterEntry':vpwrRingerParameterEntry,_m:vpwrRingerIndex,'vpwrRingerParameterAdminState':vpwrRingerParameterAdminState,'vpwrRingerParameterAcVoltage':vpwrRingerParameterAcVoltage,'vpwrRingerParameterDcVoltage':vpwrRingerParameterDcVoltage,'vpwrRingerParameterFrequency':vpwrRingerParameterFrequency,'vpwrRingerNumberPresent':vpwrRingerNumberPresent,'vpwrRingerAlarmGroup':vpwrRingerAlarmGroup,'vpwrRingerAlarmaAFailed':vpwrRingerAlarmaAFailed,'vpwrRingerAlarmAOTemp':vpwrRingerAlarmAOTemp,'vpwrRingerAlarmAOCurrent':vpwrRingerAlarmAOCurrent,'vpwrRingerAlarmaBFailed':vpwrRingerAlarmaBFailed,'vpwrRingerAlarmBOverTemp':vpwrRingerAlarmBOverTemp,'vpwrRingerAlarmBOverCurrent':vpwrRingerAlarmBOverCurrent,'vpwrRingerTestGroup':vpwrRingerTestGroup,'vpwrDcPowerDcDcConverter':vpwrDcPowerDcDcConverter,'vpwrDcDcConverterConfigGroup':vpwrDcDcConverterConfigGroup,'vpwrDcDcConverterAlarmGroup':vpwrDcDcConverterAlarmGroup,'vpwrDcDcConverterTestGroup':vpwrDcDcConverterTestGroup,'vpwrDcPowerDcAcInverter':vpwrDcPowerDcAcInverter,'vpwrDcAcInverterConfigGroup':vpwrDcAcInverterConfigGroup,'vpwrDcAcInverterAlarmGroup':vpwrDcAcInverterAlarmGroup,'vpwrDcAcInverterTestGroup':vpwrDcAcInverterTestGroup,'vpwrDcPowerBayController':vpwrDcPowerBayController,'vpwrDcPowerIoModule':vpwrDcPowerIoModule,'vpwrIoModuleConfigGroup':vpwrIoModuleConfigGroup,'vpwrIoModuleAlarmGroup':vpwrIoModuleAlarmGroup,'vpwrIoModuleTestGroup':vpwrIoModuleTestGroup,'vpwrDcPowerDist':vpwrDcPowerDist,'vpwrDcPowerTrio':vpwrDcPowerTrio})