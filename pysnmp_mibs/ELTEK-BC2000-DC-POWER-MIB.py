_AB='vpwrBatteryRemainingTime'
_AA='vpwrBatteryCurrentCapacity'
_A9='vpwrSystemCurrent'
_A8='vpwrPMIndex2'
_A7='vpwrPMIndex1'
_A6='vpwrPMIndex'
_A5='not-accessible'
_A4='vpwrTrapIpIndex'
_A3='sysAlarmIndex'
_A2='vpwrAlarmIndex'
_A1='vpwrBDTSchedIndex'
_A0='vpwrBDTHistIndex'
_z='active'
_y='inactive'
_x=' milli-Volts per degrees Celsius'
_w='vpwrBatteryTempIndex'
_v='vpwrDCModuleIndex'
_u='vpwrShelfIndex1'
_t='vpwrSysHistAlarmIndex'
_s='vpwrPanelModuleIndex'
_r='vpwrPanelIndex'
_q='vpwrPanelStatusModuleIndex'
_p='vpwrPanelStatusIndex'
_o='sysType12V'
_n='sysType24V'
_m='sysType48V'
_l='systemTempCompActive'
_k='systemTempCompInactive'
_j='external'
_i='internal'
_h='tempCompEnabled'
_g='tempCompDisabled'
_f='moduleStatusUnknown'
_e='moduleStatusRingerBOn'
_d='moduleStatusRingerAOn'
_c='moduleStatusDisabled'
_b='moduleStatusAlarm'
_a='moduleStatusOK'
_Z='bdtACFailStart'
_Y='bdtManualStart'
_X='bdtInactive'
_W='vpwrTrapAcfDuration'
_V='vpwrAlarmingSubModuleBitMap'
_U='vpwrAlarmingModuleIndex'
_T='vpwrAlarmingModuleOID'
_S='minutes'
_R=' Seconds'
_Q='degrees Centigrade'
_P='enabled'
_O='vpwrPMRelayOn'
_N='vpwrPMRelayOff'
_M='degrees Celsius'
_L='vpwrModuleIndex'
_K='vpwrShelfIndex'
_J='undefined'
_I='disabled'
_H='DisplayString'
_G=' *.01 Volts'
_F='Integer32'
_E='vpwrTrapsMsgString'
_D='read-write'
_C='ELTEK-BC2000-DC-POWER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_H,'PhysAddress','TextualConvention','TimeStamp')
eltek=ModuleIdentity((1,3,6,1,4,1,13858))
if mibBuilder.loadTexts:eltek.setRevisions(('2014-03-27 10:38',))
class PositiveInteger(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NonNegativeInteger(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class GenericEnableDisableTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_P,1)))
class SysInputValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-127,-126,-125,-124,-123,-122,-121,255)));namedValues=NamedValues(*((_I,-127),('removed',-126),('shorted',-125),('auxAlarm',-124),('auxNormal',-123),('distAlarm',-122),('distNormal',-121),(_J,255)))
class VpwrPMCnfgValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,255)));namedValues=NamedValues(*((_I,0),('tProbe',1),('auxNO',2),('auxNC',3),('distNO',4),('distNC',5),(_J,255)))
class BDTStartSourceTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_X,0),(_Y,1),('bdtSched01Start1',2),('bdtSched02Start2',3),('bdtSched03Start3',4),('bdtSched04Start4',5),('bdtSched05Start5',6),('bdtSched06Start6',7),('bdtSched07Start7',8),('bdtSched08Start8',9),('bdtSched09Start9',10),('bdtSched10Start10',11),('bdtSched11Start11',12),('bdtSched12Start12',13),(_Z,14)))
class BDTResultTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('bdtResultCleared',0),('bdtResultPassed',1),('bdtResultFailed',2),('bdtResultStopped',3),('bdtResultAborted',4),('bdtResultInProgress',5)))
_VpwrDcPowerSystem_ObjectIdentity=ObjectIdentity
vpwrDcPowerSystem=_VpwrDcPowerSystem_ObjectIdentity((1,3,6,1,4,1,13858,2))
_VpwrSystemIdentGroup_ObjectIdentity=ObjectIdentity
vpwrSystemIdentGroup=_VpwrSystemIdentGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,1))
class _VpwrIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_VpwrIdentManufacturer_Type.__name__=_H
_VpwrIdentManufacturer_Object=MibScalar
vpwrIdentManufacturer=_VpwrIdentManufacturer_Object((1,3,6,1,4,1,13858,2,1,1),_VpwrIdentManufacturer_Type())
vpwrIdentManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrIdentManufacturer.setStatus(_A)
class _VpwrIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VpwrIdentModel_Type.__name__=_H
_VpwrIdentModel_Object=MibScalar
vpwrIdentModel=_VpwrIdentModel_Object((1,3,6,1,4,1,13858,2,1,2),_VpwrIdentModel_Type())
vpwrIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrIdentModel.setStatus(_A)
class _VpwrIdentControllerVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VpwrIdentControllerVersion_Type.__name__=_H
_VpwrIdentControllerVersion_Object=MibScalar
vpwrIdentControllerVersion=_VpwrIdentControllerVersion_Object((1,3,6,1,4,1,13858,2,1,3),_VpwrIdentControllerVersion_Type())
vpwrIdentControllerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrIdentControllerVersion.setStatus(_A)
class _VpwrIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VpwrIdentAgentSoftwareVersion_Type.__name__=_H
_VpwrIdentAgentSoftwareVersion_Object=MibScalar
vpwrIdentAgentSoftwareVersion=_VpwrIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,13858,2,1,4),_VpwrIdentAgentSoftwareVersion_Type())
vpwrIdentAgentSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrIdentAgentSoftwareVersion.setStatus(_A)
class _VpwrIdentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_VpwrIdentName_Type.__name__=_H
_VpwrIdentName_Object=MibScalar
vpwrIdentName=_VpwrIdentName_Object((1,3,6,1,4,1,13858,2,1,5),_VpwrIdentName_Type())
vpwrIdentName.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrIdentName.setStatus(_A)
_VpwrSystemIdentTable_Object=MibTable
vpwrSystemIdentTable=_VpwrSystemIdentTable_Object((1,3,6,1,4,1,13858,2,1,6))
if mibBuilder.loadTexts:vpwrSystemIdentTable.setStatus(_A)
_VpwrSystemIdentEntry_Object=MibTableRow
vpwrSystemIdentEntry=_VpwrSystemIdentEntry_Object((1,3,6,1,4,1,13858,2,1,6,1))
vpwrSystemIdentEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:vpwrSystemIdentEntry.setStatus(_A)
_VpwrShelfIndex_Type=PositiveInteger
_VpwrShelfIndex_Object=MibTableColumn
vpwrShelfIndex=_VpwrShelfIndex_Object((1,3,6,1,4,1,13858,2,1,6,1,1),_VpwrShelfIndex_Type())
vpwrShelfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrShelfIndex.setStatus(_A)
_VpwrModuleIndex_Type=PositiveInteger
_VpwrModuleIndex_Object=MibTableColumn
vpwrModuleIndex=_VpwrModuleIndex_Object((1,3,6,1,4,1,13858,2,1,6,1,2),_VpwrModuleIndex_Type())
vpwrModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleIndex.setStatus(_A)
_VpwrModuleOID_Type=ObjectIdentifier
_VpwrModuleOID_Object=MibTableColumn
vpwrModuleOID=_VpwrModuleOID_Object((1,3,6,1,4,1,13858,2,1,6,1,3),_VpwrModuleOID_Type())
vpwrModuleOID.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleOID.setStatus(_A)
_VpwrModuleCurrent_Type=Integer32
_VpwrModuleCurrent_Object=MibTableColumn
vpwrModuleCurrent=_VpwrModuleCurrent_Object((1,3,6,1,4,1,13858,2,1,6,1,4),_VpwrModuleCurrent_Type())
vpwrModuleCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleCurrent.setStatus(_A)
class _VpwrModuleOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_a,0),(_b,1),(_c,2),(_d,3),(_e,4),(_f,5)))
_VpwrModuleOperStatus_Type.__name__=_F
_VpwrModuleOperStatus_Object=MibTableColumn
vpwrModuleOperStatus=_VpwrModuleOperStatus_Object((1,3,6,1,4,1,13858,2,1,6,1,5),_VpwrModuleOperStatus_Type())
vpwrModuleOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleOperStatus.setStatus(_A)
_VpwrModuleCapacity_Type=Integer32
_VpwrModuleCapacity_Object=MibTableColumn
vpwrModuleCapacity=_VpwrModuleCapacity_Object((1,3,6,1,4,1,13858,2,1,6,1,6),_VpwrModuleCapacity_Type())
vpwrModuleCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleCapacity.setStatus(_A)
_VpwrSystemConfigGroup_ObjectIdentity=ObjectIdentity
vpwrSystemConfigGroup=_VpwrSystemConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,2))
class _VpwrSystemTempCompensation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_g,0),(_h,1)))
_VpwrSystemTempCompensation_Type.__name__=_F
_VpwrSystemTempCompensation_Object=MibScalar
vpwrSystemTempCompensation=_VpwrSystemTempCompensation_Object((1,3,6,1,4,1,13858,2,2,1),_VpwrSystemTempCompensation_Type())
vpwrSystemTempCompensation.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemTempCompensation.setStatus(_A)
class _VpwrSystemTempCompStartTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,60))
_VpwrSystemTempCompStartTemperature_Type.__name__=_F
_VpwrSystemTempCompStartTemperature_Object=MibScalar
vpwrSystemTempCompStartTemperature=_VpwrSystemTempCompStartTemperature_Object((1,3,6,1,4,1,13858,2,2,2),_VpwrSystemTempCompStartTemperature_Type())
vpwrSystemTempCompStartTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemTempCompStartTemperature.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemTempCompStartTemperature.setUnits(_Q)
_VpwrSystemTempCompStopVoltage_Type=Integer32
_VpwrSystemTempCompStopVoltage_Object=MibScalar
vpwrSystemTempCompStopVoltage=_VpwrSystemTempCompStopVoltage_Object((1,3,6,1,4,1,13858,2,2,3),_VpwrSystemTempCompStopVoltage_Type())
vpwrSystemTempCompStopVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemTempCompStopVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemTempCompStopVoltage.setUnits(_G)
class _VpwrSystemTempCompensationSlope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_VpwrSystemTempCompensationSlope_Type.__name__=_F
_VpwrSystemTempCompensationSlope_Object=MibScalar
vpwrSystemTempCompensationSlope=_VpwrSystemTempCompensationSlope_Object((1,3,6,1,4,1,13858,2,2,4),_VpwrSystemTempCompensationSlope_Type())
vpwrSystemTempCompensationSlope.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemTempCompensationSlope.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemTempCompensationSlope.setUnits(' milli-Volts per degrees Centigrade')
class _VpwrSystemThermalSenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_i,0),(_j,1)))
_VpwrSystemThermalSenseType_Type.__name__=_F
_VpwrSystemThermalSenseType_Object=MibScalar
vpwrSystemThermalSenseType=_VpwrSystemThermalSenseType_Object((1,3,6,1,4,1,13858,2,2,5),_VpwrSystemThermalSenseType_Type())
vpwrSystemThermalSenseType.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemThermalSenseType.setStatus(_A)
_VpwrSystemHVAlarmSetpoint_Type=Integer32
_VpwrSystemHVAlarmSetpoint_Object=MibScalar
vpwrSystemHVAlarmSetpoint=_VpwrSystemHVAlarmSetpoint_Object((1,3,6,1,4,1,13858,2,2,6),_VpwrSystemHVAlarmSetpoint_Type())
vpwrSystemHVAlarmSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemHVAlarmSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemHVAlarmSetpoint.setUnits(_G)
_VpwrSystemBDAlarmSetpoint_Type=Integer32
_VpwrSystemBDAlarmSetpoint_Object=MibScalar
vpwrSystemBDAlarmSetpoint=_VpwrSystemBDAlarmSetpoint_Object((1,3,6,1,4,1,13858,2,2,7),_VpwrSystemBDAlarmSetpoint_Type())
vpwrSystemBDAlarmSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemBDAlarmSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemBDAlarmSetpoint.setUnits(_G)
_VpwrSystemInternalTempLThreshold_Type=Integer32
_VpwrSystemInternalTempLThreshold_Object=MibScalar
vpwrSystemInternalTempLThreshold=_VpwrSystemInternalTempLThreshold_Object((1,3,6,1,4,1,13858,2,2,8),_VpwrSystemInternalTempLThreshold_Type())
vpwrSystemInternalTempLThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemInternalTempLThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemInternalTempLThreshold.setUnits(_Q)
_VpwrSystemInternalTempUThreshold_Type=Integer32
_VpwrSystemInternalTempUThreshold_Object=MibScalar
vpwrSystemInternalTempUThreshold=_VpwrSystemInternalTempUThreshold_Object((1,3,6,1,4,1,13858,2,2,9),_VpwrSystemInternalTempUThreshold_Type())
vpwrSystemInternalTempUThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrSystemInternalTempUThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemInternalTempUThreshold.setUnits(_Q)
_VpwrSystemParameterGroup_ObjectIdentity=ObjectIdentity
vpwrSystemParameterGroup=_VpwrSystemParameterGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,3))
class _VpwrSystemShelfCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_VpwrSystemShelfCapacity_Type.__name__=_F
_VpwrSystemShelfCapacity_Object=MibScalar
vpwrSystemShelfCapacity=_VpwrSystemShelfCapacity_Object((1,3,6,1,4,1,13858,2,3,1),_VpwrSystemShelfCapacity_Type())
vpwrSystemShelfCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemShelfCapacity.setStatus(_A)
_VpwrSystemVoltage_Type=Integer32
_VpwrSystemVoltage_Object=MibScalar
vpwrSystemVoltage=_VpwrSystemVoltage_Object((1,3,6,1,4,1,13858,2,3,2),_VpwrSystemVoltage_Type())
vpwrSystemVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemVoltage.setUnits(_G)
_VpwrSystemCurrent_Type=Integer32
_VpwrSystemCurrent_Object=MibScalar
vpwrSystemCurrent=_VpwrSystemCurrent_Object((1,3,6,1,4,1,13858,2,3,3),_VpwrSystemCurrent_Type())
vpwrSystemCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemCurrent.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemCurrent.setUnits(' Amperes')
class _VpwrSystemControllerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('systemControllerStateUnknown',0),('systemControllerStateNormal',1),('systemControllerStateChange',2),('systemControllerStateAlarm',3),('systemControllerStateMenu',4),('systemControllerStateIrActive',5)))
_VpwrSystemControllerState_Type.__name__=_F
_VpwrSystemControllerState_Object=MibScalar
vpwrSystemControllerState=_VpwrSystemControllerState_Object((1,3,6,1,4,1,13858,2,3,4),_VpwrSystemControllerState_Type())
vpwrSystemControllerState.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemControllerState.setStatus(_A)
_VpwrSystemInternalTemperature_Type=Integer32
_VpwrSystemInternalTemperature_Object=MibScalar
vpwrSystemInternalTemperature=_VpwrSystemInternalTemperature_Object((1,3,6,1,4,1,13858,2,3,5),_VpwrSystemInternalTemperature_Type())
vpwrSystemInternalTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemInternalTemperature.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemInternalTemperature.setUnits(_Q)
class _VpwrSystemTempCompensationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_k,0),(_l,1)))
_VpwrSystemTempCompensationState_Type.__name__=_F
_VpwrSystemTempCompensationState_Object=MibScalar
vpwrSystemTempCompensationState=_VpwrSystemTempCompensationState_Object((1,3,6,1,4,1,13858,2,3,6),_VpwrSystemTempCompensationState_Type())
vpwrSystemTempCompensationState.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemTempCompensationState.setStatus(_A)
class _VpwrSystemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_m,0),(_n,1),(_o,2)))
_VpwrSystemType_Type.__name__=_F
_VpwrSystemType_Object=MibScalar
vpwrSystemType=_VpwrSystemType_Object((1,3,6,1,4,1,13858,2,3,7),_VpwrSystemType_Type())
vpwrSystemType.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemType.setStatus(_A)
_VpwrSystemCumulativeUpTime_Type=Gauge32
_VpwrSystemCumulativeUpTime_Object=MibScalar
vpwrSystemCumulativeUpTime=_VpwrSystemCumulativeUpTime_Object((1,3,6,1,4,1,13858,2,3,8),_VpwrSystemCumulativeUpTime_Type())
vpwrSystemCumulativeUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemCumulativeUpTime.setStatus(_A)
_VpwrSystemBatteryRemainingTime_Type=PositiveInteger
_VpwrSystemBatteryRemainingTime_Object=MibScalar
vpwrSystemBatteryRemainingTime=_VpwrSystemBatteryRemainingTime_Object((1,3,6,1,4,1,13858,2,3,9),_VpwrSystemBatteryRemainingTime_Type())
vpwrSystemBatteryRemainingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemBatteryRemainingTime.setStatus(_A)
if mibBuilder.loadTexts:vpwrSystemBatteryRemainingTime.setUnits('Hours')
_VpwrSystemPanelIdentGroup_ObjectIdentity=ObjectIdentity
vpwrSystemPanelIdentGroup=_VpwrSystemPanelIdentGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,4))
_VpwrPanelStatusTable_Object=MibTable
vpwrPanelStatusTable=_VpwrPanelStatusTable_Object((1,3,6,1,4,1,13858,2,4,1))
if mibBuilder.loadTexts:vpwrPanelStatusTable.setStatus(_A)
_VpwrPanelStatus_Object=MibTableRow
vpwrPanelStatus=_VpwrPanelStatus_Object((1,3,6,1,4,1,13858,2,4,1,1))
vpwrPanelStatus.setIndexNames((0,_C,_p),(0,_C,_q))
if mibBuilder.loadTexts:vpwrPanelStatus.setStatus(_A)
_VpwrPanelStatusIndex_Type=PositiveInteger
_VpwrPanelStatusIndex_Object=MibTableColumn
vpwrPanelStatusIndex=_VpwrPanelStatusIndex_Object((1,3,6,1,4,1,13858,2,4,1,1,1),_VpwrPanelStatusIndex_Type())
vpwrPanelStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelStatusIndex.setStatus(_A)
_VpwrPanelStatusModuleIndex_Type=PositiveInteger
_VpwrPanelStatusModuleIndex_Object=MibTableColumn
vpwrPanelStatusModuleIndex=_VpwrPanelStatusModuleIndex_Object((1,3,6,1,4,1,13858,2,4,1,1,2),_VpwrPanelStatusModuleIndex_Type())
vpwrPanelStatusModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelStatusModuleIndex.setStatus(_A)
_VpwrPanelStatusModuleOID_Type=ObjectIdentifier
_VpwrPanelStatusModuleOID_Object=MibTableColumn
vpwrPanelStatusModuleOID=_VpwrPanelStatusModuleOID_Object((1,3,6,1,4,1,13858,2,4,1,1,3),_VpwrPanelStatusModuleOID_Type())
vpwrPanelStatusModuleOID.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelStatusModuleOID.setStatus(_A)
_VpwrPanelStatusModuleCurrent_Type=Integer32
_VpwrPanelStatusModuleCurrent_Object=MibTableColumn
vpwrPanelStatusModuleCurrent=_VpwrPanelStatusModuleCurrent_Object((1,3,6,1,4,1,13858,2,4,1,1,4),_VpwrPanelStatusModuleCurrent_Type())
vpwrPanelStatusModuleCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelStatusModuleCurrent.setStatus(_A)
class _VpwrpanelStatusModuleOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_a,0),(_b,1),(_c,2),(_d,3),(_e,4),(_f,5)))
_VpwrpanelStatusModuleOperStatus_Type.__name__=_F
_VpwrpanelStatusModuleOperStatus_Object=MibTableColumn
vpwrpanelStatusModuleOperStatus=_VpwrpanelStatusModuleOperStatus_Object((1,3,6,1,4,1,13858,2,4,1,1,5),_VpwrpanelStatusModuleOperStatus_Type())
vpwrpanelStatusModuleOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrpanelStatusModuleOperStatus.setStatus(_A)
_VpwrPanelStatusModuleCapacity_Type=Integer32
_VpwrPanelStatusModuleCapacity_Object=MibTableColumn
vpwrPanelStatusModuleCapacity=_VpwrPanelStatusModuleCapacity_Object((1,3,6,1,4,1,13858,2,4,1,1,6),_VpwrPanelStatusModuleCapacity_Type())
vpwrPanelStatusModuleCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelStatusModuleCapacity.setStatus(_A)
_VpwrPanelIdentTable_Object=MibTable
vpwrPanelIdentTable=_VpwrPanelIdentTable_Object((1,3,6,1,4,1,13858,2,4,2))
if mibBuilder.loadTexts:vpwrPanelIdentTable.setStatus(_A)
_VpwrPanelIdentEntry_Object=MibTableRow
vpwrPanelIdentEntry=_VpwrPanelIdentEntry_Object((1,3,6,1,4,1,13858,2,4,2,1))
vpwrPanelIdentEntry.setIndexNames((0,_C,_r),(0,_C,_s))
if mibBuilder.loadTexts:vpwrPanelIdentEntry.setStatus(_A)
_VpwrPanelIndex_Type=PositiveInteger
_VpwrPanelIndex_Object=MibTableColumn
vpwrPanelIndex=_VpwrPanelIndex_Object((1,3,6,1,4,1,13858,2,4,2,1,1),_VpwrPanelIndex_Type())
vpwrPanelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelIndex.setStatus(_A)
_VpwrPanelModuleIndex_Type=PositiveInteger
_VpwrPanelModuleIndex_Object=MibTableColumn
vpwrPanelModuleIndex=_VpwrPanelModuleIndex_Object((1,3,6,1,4,1,13858,2,4,2,1,2),_VpwrPanelModuleIndex_Type())
vpwrPanelModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelModuleIndex.setStatus(_A)
_VpwrPanelModuleSerNum_Type=ObjectIdentifier
_VpwrPanelModuleSerNum_Object=MibTableColumn
vpwrPanelModuleSerNum=_VpwrPanelModuleSerNum_Object((1,3,6,1,4,1,13858,2,4,2,1,3),_VpwrPanelModuleSerNum_Type())
vpwrPanelModuleSerNum.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelModuleSerNum.setStatus(_A)
_VpwrPanelModuleModelName_Type=ObjectIdentifier
_VpwrPanelModuleModelName_Object=MibTableColumn
vpwrPanelModuleModelName=_VpwrPanelModuleModelName_Object((1,3,6,1,4,1,13858,2,4,2,1,4),_VpwrPanelModuleModelName_Type())
vpwrPanelModuleModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelModuleModelName.setStatus(_A)
_VpwrPanelModuleFWVer_Type=ObjectIdentifier
_VpwrPanelModuleFWVer_Object=MibTableColumn
vpwrPanelModuleFWVer=_VpwrPanelModuleFWVer_Object((1,3,6,1,4,1,13858,2,4,2,1,5),_VpwrPanelModuleFWVer_Type())
vpwrPanelModuleFWVer.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelModuleFWVer.setStatus(_A)
_VpwrPanelModuleTestDate_Type=Integer32
_VpwrPanelModuleTestDate_Object=MibTableColumn
vpwrPanelModuleTestDate=_VpwrPanelModuleTestDate_Object((1,3,6,1,4,1,13858,2,4,2,1,6),_VpwrPanelModuleTestDate_Type())
vpwrPanelModuleTestDate.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPanelModuleTestDate.setStatus(_A)
_VpwrSystemHistoryGroup_ObjectIdentity=ObjectIdentity
vpwrSystemHistoryGroup=_VpwrSystemHistoryGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,5))
_VpwrSysHistAlarmTable_Object=MibTable
vpwrSysHistAlarmTable=_VpwrSysHistAlarmTable_Object((1,3,6,1,4,1,13858,2,5,1))
if mibBuilder.loadTexts:vpwrSysHistAlarmTable.setStatus(_A)
_VpwrSysHistAlarmEntry_Object=MibTableRow
vpwrSysHistAlarmEntry=_VpwrSysHistAlarmEntry_Object((1,3,6,1,4,1,13858,2,5,1,1))
vpwrSysHistAlarmEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:vpwrSysHistAlarmEntry.setStatus(_A)
_VpwrSysHistAlarmIndex_Type=PositiveInteger
_VpwrSysHistAlarmIndex_Object=MibTableColumn
vpwrSysHistAlarmIndex=_VpwrSysHistAlarmIndex_Object((1,3,6,1,4,1,13858,2,5,1,1,1),_VpwrSysHistAlarmIndex_Type())
vpwrSysHistAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSysHistAlarmIndex.setStatus(_A)
_VpwrSysHistAlarmDescription_Type=DisplayString
_VpwrSysHistAlarmDescription_Object=MibTableColumn
vpwrSysHistAlarmDescription=_VpwrSysHistAlarmDescription_Object((1,3,6,1,4,1,13858,2,5,1,1,2),_VpwrSysHistAlarmDescription_Type())
vpwrSysHistAlarmDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSysHistAlarmDescription.setStatus(_A)
_VpwrSystemAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrSystemAlarmGroup=_VpwrSystemAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,2,6))
_VpwrSystemAlarmMajor_Type=Integer32
_VpwrSystemAlarmMajor_Object=MibScalar
vpwrSystemAlarmMajor=_VpwrSystemAlarmMajor_Object((1,3,6,1,4,1,13858,2,6,1),_VpwrSystemAlarmMajor_Type())
vpwrSystemAlarmMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemAlarmMajor.setStatus(_A)
_VpwrSystemAlarmMinor_Type=Integer32
_VpwrSystemAlarmMinor_Object=MibScalar
vpwrSystemAlarmMinor=_VpwrSystemAlarmMinor_Object((1,3,6,1,4,1,13858,2,6,2),_VpwrSystemAlarmMinor_Type())
vpwrSystemAlarmMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemAlarmMinor.setStatus(_A)
_VpwrSystemACFailAlarm_Type=Integer32
_VpwrSystemACFailAlarm_Object=MibScalar
vpwrSystemACFailAlarm=_VpwrSystemACFailAlarm_Object((1,3,6,1,4,1,13858,2,6,3),_VpwrSystemACFailAlarm_Type())
vpwrSystemACFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemACFailAlarm.setStatus(_A)
_VpwrSystemHighVoltageWarningAlarm_Type=Integer32
_VpwrSystemHighVoltageWarningAlarm_Object=MibScalar
vpwrSystemHighVoltageWarningAlarm=_VpwrSystemHighVoltageWarningAlarm_Object((1,3,6,1,4,1,13858,2,6,4),_VpwrSystemHighVoltageWarningAlarm_Type())
vpwrSystemHighVoltageWarningAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemHighVoltageWarningAlarm.setStatus(_A)
_VpwrSystemHighVoltageShutdownAlarm_Type=Integer32
_VpwrSystemHighVoltageShutdownAlarm_Object=MibScalar
vpwrSystemHighVoltageShutdownAlarm=_VpwrSystemHighVoltageShutdownAlarm_Object((1,3,6,1,4,1,13858,2,6,5),_VpwrSystemHighVoltageShutdownAlarm_Type())
vpwrSystemHighVoltageShutdownAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemHighVoltageShutdownAlarm.setStatus(_A)
class _VpwrSystemBatteryonDischargeAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_k,0),(_l,1)))
_VpwrSystemBatteryonDischargeAlarm_Type.__name__=_F
_VpwrSystemBatteryonDischargeAlarm_Object=MibScalar
vpwrSystemBatteryonDischargeAlarm=_VpwrSystemBatteryonDischargeAlarm_Object((1,3,6,1,4,1,13858,2,6,6),_VpwrSystemBatteryonDischargeAlarm_Type())
vpwrSystemBatteryonDischargeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemBatteryonDischargeAlarm.setStatus(_A)
class _VpwrSystemLowVoltageWarningAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_m,0),(_n,1),(_o,2)))
_VpwrSystemLowVoltageWarningAlarm_Type.__name__=_F
_VpwrSystemLowVoltageWarningAlarm_Object=MibScalar
vpwrSystemLowVoltageWarningAlarm=_VpwrSystemLowVoltageWarningAlarm_Object((1,3,6,1,4,1,13858,2,6,7),_VpwrSystemLowVoltageWarningAlarm_Type())
vpwrSystemLowVoltageWarningAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemLowVoltageWarningAlarm.setStatus(_A)
_VpwrSystemLVDOpenAlarm_Type=Gauge32
_VpwrSystemLVDOpenAlarm_Object=MibScalar
vpwrSystemLVDOpenAlarm=_VpwrSystemLVDOpenAlarm_Object((1,3,6,1,4,1,13858,2,6,8),_VpwrSystemLVDOpenAlarm_Type())
vpwrSystemLVDOpenAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemLVDOpenAlarm.setStatus(_A)
_VpwrSystemDistributionAlarm_Type=PositiveInteger
_VpwrSystemDistributionAlarm_Object=MibScalar
vpwrSystemDistributionAlarm=_VpwrSystemDistributionAlarm_Object((1,3,6,1,4,1,13858,2,6,9),_VpwrSystemDistributionAlarm_Type())
vpwrSystemDistributionAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemDistributionAlarm.setStatus(_A)
_VpwrSystemAuxiliaryAlarm_Type=PositiveInteger
_VpwrSystemAuxiliaryAlarm_Object=MibScalar
vpwrSystemAuxiliaryAlarm=_VpwrSystemAuxiliaryAlarm_Object((1,3,6,1,4,1,13858,2,6,10),_VpwrSystemAuxiliaryAlarm_Type())
vpwrSystemAuxiliaryAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemAuxiliaryAlarm.setStatus(_A)
_VpwrSystemRedundantCapAlarm_Type=PositiveInteger
_VpwrSystemRedundantCapAlarm_Object=MibScalar
vpwrSystemRedundantCapAlarm=_VpwrSystemRedundantCapAlarm_Object((1,3,6,1,4,1,13858,2,6,11),_VpwrSystemRedundantCapAlarm_Type())
vpwrSystemRedundantCapAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemRedundantCapAlarm.setStatus(_A)
_VpwrSystemRectIShareAlarm_Type=PositiveInteger
_VpwrSystemRectIShareAlarm_Object=MibScalar
vpwrSystemRectIShareAlarm=_VpwrSystemRectIShareAlarm_Object((1,3,6,1,4,1,13858,2,6,12),_VpwrSystemRectIShareAlarm_Type())
vpwrSystemRectIShareAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemRectIShareAlarm.setStatus(_A)
_VpwrSystemSnglRectAlarm_Type=PositiveInteger
_VpwrSystemSnglRectAlarm_Object=MibScalar
vpwrSystemSnglRectAlarm=_VpwrSystemSnglRectAlarm_Object((1,3,6,1,4,1,13858,2,6,13),_VpwrSystemSnglRectAlarm_Type())
vpwrSystemSnglRectAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemSnglRectAlarm.setStatus(_A)
_VpwrSystemMultRectAlarm_Type=PositiveInteger
_VpwrSystemMultRectAlarm_Object=MibScalar
vpwrSystemMultRectAlarm=_VpwrSystemMultRectAlarm_Object((1,3,6,1,4,1,13858,2,6,14),_VpwrSystemMultRectAlarm_Type())
vpwrSystemMultRectAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemMultRectAlarm.setStatus(_A)
_VpwrSystemModlCommAlarm_Type=PositiveInteger
_VpwrSystemModlCommAlarm_Object=MibScalar
vpwrSystemModlCommAlarm=_VpwrSystemModlCommAlarm_Object((1,3,6,1,4,1,13858,2,6,15),_VpwrSystemModlCommAlarm_Type())
vpwrSystemModlCommAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemModlCommAlarm.setStatus(_A)
_VpwrSystemOverTempAlarm_Type=PositiveInteger
_VpwrSystemOverTempAlarm_Object=MibScalar
vpwrSystemOverTempAlarm=_VpwrSystemOverTempAlarm_Object((1,3,6,1,4,1,13858,2,6,16),_VpwrSystemOverTempAlarm_Type())
vpwrSystemOverTempAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemOverTempAlarm.setStatus(_A)
_VpwrSystemThermRAAlarm_Type=PositiveInteger
_VpwrSystemThermRAAlarm_Object=MibScalar
vpwrSystemThermRAAlarm=_VpwrSystemThermRAAlarm_Object((1,3,6,1,4,1,13858,2,6,17),_VpwrSystemThermRAAlarm_Type())
vpwrSystemThermRAAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemThermRAAlarm.setStatus(_A)
_VpwrSystemBDTAlarm_Type=PositiveInteger
_VpwrSystemBDTAlarm_Object=MibScalar
vpwrSystemBDTAlarm=_VpwrSystemBDTAlarm_Object((1,3,6,1,4,1,13858,2,6,18),_VpwrSystemBDTAlarm_Type())
vpwrSystemBDTAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemBDTAlarm.setStatus(_A)
_VpwrSystemRectUVAlarm_Type=PositiveInteger
_VpwrSystemRectUVAlarm_Object=MibScalar
vpwrSystemRectUVAlarm=_VpwrSystemRectUVAlarm_Object((1,3,6,1,4,1,13858,2,6,19),_VpwrSystemRectUVAlarm_Type())
vpwrSystemRectUVAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemRectUVAlarm.setStatus(_A)
_VpwrSystemMultRectUVAlarm_Type=PositiveInteger
_VpwrSystemMultRectUVAlarm_Object=MibScalar
vpwrSystemMultRectUVAlarm=_VpwrSystemMultRectUVAlarm_Object((1,3,6,1,4,1,13858,2,6,20),_VpwrSystemMultRectUVAlarm_Type())
vpwrSystemMultRectUVAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemMultRectUVAlarm.setStatus(_A)
_VpwrSystemSnglRngrAlarm_Type=PositiveInteger
_VpwrSystemSnglRngrAlarm_Object=MibScalar
vpwrSystemSnglRngrAlarm=_VpwrSystemSnglRngrAlarm_Object((1,3,6,1,4,1,13858,2,6,21),_VpwrSystemSnglRngrAlarm_Type())
vpwrSystemSnglRngrAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemSnglRngrAlarm.setStatus(_A)
_VpwrSystemMultRngrAlarm_Type=PositiveInteger
_VpwrSystemMultRngrAlarm_Object=MibScalar
vpwrSystemMultRngrAlarm=_VpwrSystemMultRngrAlarm_Object((1,3,6,1,4,1,13858,2,6,22),_VpwrSystemMultRngrAlarm_Type())
vpwrSystemMultRngrAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemMultRngrAlarm.setStatus(_A)
_VpwrSystemTempProbeAlarm_Type=PositiveInteger
_VpwrSystemTempProbeAlarm_Object=MibScalar
vpwrSystemTempProbeAlarm=_VpwrSystemTempProbeAlarm_Object((1,3,6,1,4,1,13858,2,6,23),_VpwrSystemTempProbeAlarm_Type())
vpwrSystemTempProbeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemTempProbeAlarm.setStatus(_A)
_VpwrSystemRngrCommAlarm_Type=PositiveInteger
_VpwrSystemRngrCommAlarm_Object=MibScalar
vpwrSystemRngrCommAlarm=_VpwrSystemRngrCommAlarm_Object((1,3,6,1,4,1,13858,2,6,24),_VpwrSystemRngrCommAlarm_Type())
vpwrSystemRngrCommAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemRngrCommAlarm.setStatus(_A)
_VpwrSystemDistPMCommAlarm_Type=PositiveInteger
_VpwrSystemDistPMCommAlarm_Object=MibScalar
vpwrSystemDistPMCommAlarm=_VpwrSystemDistPMCommAlarm_Object((1,3,6,1,4,1,13858,2,6,25),_VpwrSystemDistPMCommAlarm_Type())
vpwrSystemDistPMCommAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemDistPMCommAlarm.setStatus(_A)
_VpwrSystemRectILimitAlarm_Type=PositiveInteger
_VpwrSystemRectILimitAlarm_Object=MibScalar
vpwrSystemRectILimitAlarm=_VpwrSystemRectILimitAlarm_Object((1,3,6,1,4,1,13858,2,6,26),_VpwrSystemRectILimitAlarm_Type())
vpwrSystemRectILimitAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemRectILimitAlarm.setStatus(_A)
_VpwrSystemMultRectILimitAlarm_Type=PositiveInteger
_VpwrSystemMultRectILimitAlarm_Object=MibScalar
vpwrSystemMultRectILimitAlarm=_VpwrSystemMultRectILimitAlarm_Object((1,3,6,1,4,1,13858,2,6,27),_VpwrSystemMultRectILimitAlarm_Type())
vpwrSystemMultRectILimitAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemMultRectILimitAlarm.setStatus(_A)
_VpwrSystemUnmappedI2CCANAlarm_Type=PositiveInteger
_VpwrSystemUnmappedI2CCANAlarm_Object=MibScalar
vpwrSystemUnmappedI2CCANAlarm=_VpwrSystemUnmappedI2CCANAlarm_Object((1,3,6,1,4,1,13858,2,6,28),_VpwrSystemUnmappedI2CCANAlarm_Type())
vpwrSystemUnmappedI2CCANAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemUnmappedI2CCANAlarm.setStatus(_A)
_VpwrSystemConfigErrAlarm_Type=PositiveInteger
_VpwrSystemConfigErrAlarm_Object=MibScalar
vpwrSystemConfigErrAlarm=_VpwrSystemConfigErrAlarm_Object((1,3,6,1,4,1,13858,2,6,29),_VpwrSystemConfigErrAlarm_Type())
vpwrSystemConfigErrAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemConfigErrAlarm.setStatus(_A)
_VpwrSystemDispFWAlarm_Type=PositiveInteger
_VpwrSystemDispFWAlarm_Object=MibScalar
vpwrSystemDispFWAlarm=_VpwrSystemDispFWAlarm_Object((1,3,6,1,4,1,13858,2,6,30),_VpwrSystemDispFWAlarm_Type())
vpwrSystemDispFWAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemDispFWAlarm.setStatus(_A)
_VpwrSystemUndefinedAlarm_Type=PositiveInteger
_VpwrSystemUndefinedAlarm_Object=MibScalar
vpwrSystemUndefinedAlarm=_VpwrSystemUndefinedAlarm_Object((1,3,6,1,4,1,13858,2,6,31),_VpwrSystemUndefinedAlarm_Type())
vpwrSystemUndefinedAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrSystemUndefinedAlarm.setStatus(_A)
_VpwrDcPowerRectifier_ObjectIdentity=ObjectIdentity
vpwrDcPowerRectifier=_VpwrDcPowerRectifier_ObjectIdentity((1,3,6,1,4,1,13858,3))
_VpwrRectifierConfigGroup_ObjectIdentity=ObjectIdentity
vpwrRectifierConfigGroup=_VpwrRectifierConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,3,1))
_VpwrRectifierFVSetpoint_Type=Integer32
_VpwrRectifierFVSetpoint_Object=MibScalar
vpwrRectifierFVSetpoint=_VpwrRectifierFVSetpoint_Object((1,3,6,1,4,1,13858,3,1,1),_VpwrRectifierFVSetpoint_Type())
vpwrRectifierFVSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRectifierFVSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrRectifierFVSetpoint.setUnits(_G)
_VpwrRectifierHVSDSetpoint_Type=Integer32
_VpwrRectifierHVSDSetpoint_Object=MibScalar
vpwrRectifierHVSDSetpoint=_VpwrRectifierHVSDSetpoint_Object((1,3,6,1,4,1,13858,3,1,2),_VpwrRectifierHVSDSetpoint_Type())
vpwrRectifierHVSDSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRectifierHVSDSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrRectifierHVSDSetpoint.setUnits(_G)
class _VpwrRectifierCurrentLimitAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('rectCurrentLimitDisabled',0),('rectCurrentLimitEnabled',1)))
_VpwrRectifierCurrentLimitAdminState_Type.__name__=_F
_VpwrRectifierCurrentLimitAdminState_Object=MibScalar
vpwrRectifierCurrentLimitAdminState=_VpwrRectifierCurrentLimitAdminState_Object((1,3,6,1,4,1,13858,3,1,3),_VpwrRectifierCurrentLimitAdminState_Type())
vpwrRectifierCurrentLimitAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRectifierCurrentLimitAdminState.setStatus(_A)
class _VpwrRectifierCurrentLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,220))
_VpwrRectifierCurrentLimit_Type.__name__=_F
_VpwrRectifierCurrentLimit_Object=MibScalar
vpwrRectifierCurrentLimit=_VpwrRectifierCurrentLimit_Object((1,3,6,1,4,1,13858,3,1,4),_VpwrRectifierCurrentLimit_Type())
vpwrRectifierCurrentLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRectifierCurrentLimit.setStatus(_A)
if mibBuilder.loadTexts:vpwrRectifierCurrentLimit.setUnits('Amperes')
_VpwrRectifierFallbackAdminState_Type=GenericEnableDisableTC
_VpwrRectifierFallbackAdminState_Object=MibScalar
vpwrRectifierFallbackAdminState=_VpwrRectifierFallbackAdminState_Object((1,3,6,1,4,1,13858,3,1,5),_VpwrRectifierFallbackAdminState_Type())
vpwrRectifierFallbackAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRectifierFallbackAdminState.setStatus(_A)
_VpwrRectifierFallbackVoltage_Type=Integer32
_VpwrRectifierFallbackVoltage_Object=MibScalar
vpwrRectifierFallbackVoltage=_VpwrRectifierFallbackVoltage_Object((1,3,6,1,4,1,13858,3,1,6),_VpwrRectifierFallbackVoltage_Type())
vpwrRectifierFallbackVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRectifierFallbackVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrRectifierFallbackVoltage.setUnits(_G)
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
_VpwrDcPowerLvd_ObjectIdentity=ObjectIdentity
vpwrDcPowerLvd=_VpwrDcPowerLvd_ObjectIdentity((1,3,6,1,4,1,13858,4))
_VpwrLvdConfigGroup_ObjectIdentity=ObjectIdentity
vpwrLvdConfigGroup=_VpwrLvdConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,4,1))
_VpwrLvdWarningSetpoint_Type=Integer32
_VpwrLvdWarningSetpoint_Object=MibScalar
vpwrLvdWarningSetpoint=_VpwrLvdWarningSetpoint_Object((1,3,6,1,4,1,13858,4,1,1),_VpwrLvdWarningSetpoint_Type())
vpwrLvdWarningSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvdWarningSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdWarningSetpoint.setUnits(' * .01 Volts')
_VpwrLvdDisconnectSetpoint_Type=Integer32
_VpwrLvdDisconnectSetpoint_Object=MibScalar
vpwrLvdDisconnectSetpoint=_VpwrLvdDisconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,2),_VpwrLvdDisconnectSetpoint_Type())
vpwrLvdDisconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvdDisconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdDisconnectSetpoint.setUnits(_G)
_VpwrLvdReconnectSetpoint_Type=Integer32
_VpwrLvdReconnectSetpoint_Object=MibScalar
vpwrLvdReconnectSetpoint=_VpwrLvdReconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,3),_VpwrLvdReconnectSetpoint_Type())
vpwrLvdReconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvdReconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdReconnectSetpoint.setUnits(_G)
class _VpwrLvdReconnectDelayTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,240))
_VpwrLvdReconnectDelayTimer_Type.__name__=_F
_VpwrLvdReconnectDelayTimer_Object=MibScalar
vpwrLvdReconnectDelayTimer=_VpwrLvdReconnectDelayTimer_Object((1,3,6,1,4,1,13858,4,1,4),_VpwrLvdReconnectDelayTimer_Type())
vpwrLvdReconnectDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrLvdReconnectDelayTimer.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvdReconnectDelayTimer.setUnits(_R)
_VpwrLvd2DisconnectSetpoint_Type=Integer32
_VpwrLvd2DisconnectSetpoint_Object=MibScalar
vpwrLvd2DisconnectSetpoint=_VpwrLvd2DisconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,7),_VpwrLvd2DisconnectSetpoint_Type())
vpwrLvd2DisconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvd2DisconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvd2DisconnectSetpoint.setUnits(_G)
_VpwrLvd2ReconnectSetpoint_Type=Integer32
_VpwrLvd2ReconnectSetpoint_Object=MibScalar
vpwrLvd2ReconnectSetpoint=_VpwrLvd2ReconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,8),_VpwrLvd2ReconnectSetpoint_Type())
vpwrLvd2ReconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvd2ReconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvd2ReconnectSetpoint.setUnits(_G)
class _VpwrLvd2ReconnectDelayTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,240))
_VpwrLvd2ReconnectDelayTimer_Type.__name__=_F
_VpwrLvd2ReconnectDelayTimer_Object=MibScalar
vpwrLvd2ReconnectDelayTimer=_VpwrLvd2ReconnectDelayTimer_Object((1,3,6,1,4,1,13858,4,1,9),_VpwrLvd2ReconnectDelayTimer_Type())
vpwrLvd2ReconnectDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrLvd2ReconnectDelayTimer.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvd2ReconnectDelayTimer.setUnits(_R)
_VpwrLvd3DisconnectSetpoint_Type=Integer32
_VpwrLvd3DisconnectSetpoint_Object=MibScalar
vpwrLvd3DisconnectSetpoint=_VpwrLvd3DisconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,11),_VpwrLvd3DisconnectSetpoint_Type())
vpwrLvd3DisconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvd3DisconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvd3DisconnectSetpoint.setUnits(_G)
_VpwrLvd3ReconnectSetpoint_Type=Integer32
_VpwrLvd3ReconnectSetpoint_Object=MibScalar
vpwrLvd3ReconnectSetpoint=_VpwrLvd3ReconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,12),_VpwrLvd3ReconnectSetpoint_Type())
vpwrLvd3ReconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvd3ReconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvd3ReconnectSetpoint.setUnits(_G)
class _VpwrLvd3ReconnectDelayTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,240))
_VpwrLvd3ReconnectDelayTimer_Type.__name__=_F
_VpwrLvd3ReconnectDelayTimer_Object=MibScalar
vpwrLvd3ReconnectDelayTimer=_VpwrLvd3ReconnectDelayTimer_Object((1,3,6,1,4,1,13858,4,1,13),_VpwrLvd3ReconnectDelayTimer_Type())
vpwrLvd3ReconnectDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrLvd3ReconnectDelayTimer.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvd3ReconnectDelayTimer.setUnits(_R)
_VpwrLvd4DisconnectSetpoint_Type=Integer32
_VpwrLvd4DisconnectSetpoint_Object=MibScalar
vpwrLvd4DisconnectSetpoint=_VpwrLvd4DisconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,15),_VpwrLvd4DisconnectSetpoint_Type())
vpwrLvd4DisconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvd4DisconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvd4DisconnectSetpoint.setUnits(_G)
_VpwrLvd4ReconnectSetpoint_Type=Integer32
_VpwrLvd4ReconnectSetpoint_Object=MibScalar
vpwrLvd4ReconnectSetpoint=_VpwrLvd4ReconnectSetpoint_Object((1,3,6,1,4,1,13858,4,1,16),_VpwrLvd4ReconnectSetpoint_Type())
vpwrLvd4ReconnectSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrLvd4ReconnectSetpoint.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvd4ReconnectSetpoint.setUnits(_G)
class _VpwrLvd4ReconnectDelayTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,240))
_VpwrLvd4ReconnectDelayTimer_Type.__name__=_F
_VpwrLvd4ReconnectDelayTimer_Object=MibScalar
vpwrLvd4ReconnectDelayTimer=_VpwrLvd4ReconnectDelayTimer_Object((1,3,6,1,4,1,13858,4,1,17),_VpwrLvd4ReconnectDelayTimer_Type())
vpwrLvd4ReconnectDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrLvd4ReconnectDelayTimer.setStatus(_A)
if mibBuilder.loadTexts:vpwrLvd4ReconnectDelayTimer.setUnits(_R)
class _VpwrDCPowerLampTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_P,1)))
_VpwrDCPowerLampTest_Type.__name__=_F
_VpwrDCPowerLampTest_Object=MibScalar
vpwrDCPowerLampTest=_VpwrDCPowerLampTest_Object((1,3,6,1,4,1,13858,5),_VpwrDCPowerLampTest_Type())
vpwrDCPowerLampTest.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrDCPowerLampTest.setStatus(_A)
_VpwrDcPowerModuleIdent_ObjectIdentity=ObjectIdentity
vpwrDcPowerModuleIdent=_VpwrDcPowerModuleIdent_ObjectIdentity((1,3,6,1,4,1,13858,6))
_VpwrDcPowerModuleIdentTable_Object=MibTable
vpwrDcPowerModuleIdentTable=_VpwrDcPowerModuleIdentTable_Object((1,3,6,1,4,1,13858,6,1))
if mibBuilder.loadTexts:vpwrDcPowerModuleIdentTable.setStatus(_A)
_VpwrDcPowerModuleIdentEntry_Object=MibTableRow
vpwrDcPowerModuleIdentEntry=_VpwrDcPowerModuleIdentEntry_Object((1,3,6,1,4,1,13858,6,1,1))
vpwrDcPowerModuleIdentEntry.setIndexNames((0,_C,_u),(0,_C,_v))
if mibBuilder.loadTexts:vpwrDcPowerModuleIdentEntry.setStatus(_A)
_VpwrShelfIndex1_Type=PositiveInteger
_VpwrShelfIndex1_Object=MibTableColumn
vpwrShelfIndex1=_VpwrShelfIndex1_Object((1,3,6,1,4,1,13858,6,1,1,1),_VpwrShelfIndex1_Type())
vpwrShelfIndex1.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrShelfIndex1.setStatus(_A)
_VpwrDCModuleIndex_Type=PositiveInteger
_VpwrDCModuleIndex_Object=MibTableColumn
vpwrDCModuleIndex=_VpwrDCModuleIndex_Object((1,3,6,1,4,1,13858,6,1,1,2),_VpwrDCModuleIndex_Type())
vpwrDCModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrDCModuleIndex.setStatus(_A)
_VpwrModuleSerialNumber_Type=DisplayString
_VpwrModuleSerialNumber_Object=MibTableColumn
vpwrModuleSerialNumber=_VpwrModuleSerialNumber_Object((1,3,6,1,4,1,13858,6,1,1,3),_VpwrModuleSerialNumber_Type())
vpwrModuleSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleSerialNumber.setStatus(_A)
_VpwrModuleModelNumber_Type=DisplayString
_VpwrModuleModelNumber_Object=MibTableColumn
vpwrModuleModelNumber=_VpwrModuleModelNumber_Object((1,3,6,1,4,1,13858,6,1,1,4),_VpwrModuleModelNumber_Type())
vpwrModuleModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleModelNumber.setStatus(_A)
_VpwrModuleFwVersion_Type=DisplayString
_VpwrModuleFwVersion_Object=MibTableColumn
vpwrModuleFwVersion=_VpwrModuleFwVersion_Object((1,3,6,1,4,1,13858,6,1,1,5),_VpwrModuleFwVersion_Type())
vpwrModuleFwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleFwVersion.setStatus(_A)
_VpwrModuleTestDate_Type=DisplayString
_VpwrModuleTestDate_Object=MibTableColumn
vpwrModuleTestDate=_VpwrModuleTestDate_Object((1,3,6,1,4,1,13858,6,1,1,6),_VpwrModuleTestDate_Type())
vpwrModuleTestDate.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleTestDate.setStatus(_A)
_VpwrModuleOperHours_Type=Counter32
_VpwrModuleOperHours_Object=MibTableColumn
vpwrModuleOperHours=_VpwrModuleOperHours_Object((1,3,6,1,4,1,13858,6,1,1,7),_VpwrModuleOperHours_Type())
vpwrModuleOperHours.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrModuleOperHours.setStatus(_A)
_VpwrDcPowerBatteryGroup_ObjectIdentity=ObjectIdentity
vpwrDcPowerBatteryGroup=_VpwrDcPowerBatteryGroup_ObjectIdentity((1,3,6,1,4,1,13858,7))
_VpwrBatteryTempGroup_ObjectIdentity=ObjectIdentity
vpwrBatteryTempGroup=_VpwrBatteryTempGroup_ObjectIdentity((1,3,6,1,4,1,13858,7,1))
_VpwrBatteryTempTable_Object=MibTable
vpwrBatteryTempTable=_VpwrBatteryTempTable_Object((1,3,6,1,4,1,13858,7,1,1))
if mibBuilder.loadTexts:vpwrBatteryTempTable.setStatus(_A)
_VpwrBatteryTempEntry_Object=MibTableRow
vpwrBatteryTempEntry=_VpwrBatteryTempEntry_Object((1,3,6,1,4,1,13858,7,1,1,1))
vpwrBatteryTempEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:vpwrBatteryTempEntry.setStatus(_A)
class _VpwrBatteryTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VpwrBatteryTempIndex_Type.__name__=_F
_VpwrBatteryTempIndex_Object=MibTableColumn
vpwrBatteryTempIndex=_VpwrBatteryTempIndex_Object((1,3,6,1,4,1,13858,7,1,1,1,1),_VpwrBatteryTempIndex_Type())
vpwrBatteryTempIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBatteryTempIndex.setStatus(_A)
class _VpwrBatteryTempName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_VpwrBatteryTempName_Type.__name__=_H
_VpwrBatteryTempName_Object=MibTableColumn
vpwrBatteryTempName=_VpwrBatteryTempName_Object((1,3,6,1,4,1,13858,7,1,1,1,2),_VpwrBatteryTempName_Type())
vpwrBatteryTempName.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryTempName.setStatus(_A)
_VpwrBatteryTemp_Type=SysInputValue
_VpwrBatteryTemp_Object=MibTableColumn
vpwrBatteryTemp=_VpwrBatteryTemp_Object((1,3,6,1,4,1,13858,7,1,1,1,3),_VpwrBatteryTemp_Type())
vpwrBatteryTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBatteryTemp.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryTemp.setUnits(_M)
_VpwrBatteryTempLThreshold_Type=Integer32
_VpwrBatteryTempLThreshold_Object=MibScalar
vpwrBatteryTempLThreshold=_VpwrBatteryTempLThreshold_Object((1,3,6,1,4,1,13858,7,1,2),_VpwrBatteryTempLThreshold_Type())
vpwrBatteryTempLThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryTempLThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryTempLThreshold.setUnits(_M)
_VpwrBatteryTempUThreshold_Type=Integer32
_VpwrBatteryTempUThreshold_Object=MibScalar
vpwrBatteryTempUThreshold=_VpwrBatteryTempUThreshold_Object((1,3,6,1,4,1,13858,7,1,3),_VpwrBatteryTempUThreshold_Type())
vpwrBatteryTempUThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryTempUThreshold.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryTempUThreshold.setUnits(_M)
class _BatteryTempCompensation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_g,0),(_h,1)))
_BatteryTempCompensation_Type.__name__=_F
_BatteryTempCompensation_Object=MibScalar
batteryTempCompensation=_BatteryTempCompensation_Object((1,3,6,1,4,1,13858,7,1,4),_BatteryTempCompensation_Type())
batteryTempCompensation.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompensation.setStatus(_A)
class _BatteryTempCompHighStartTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,60))
_BatteryTempCompHighStartTemperature_Type.__name__=_F
_BatteryTempCompHighStartTemperature_Object=MibScalar
batteryTempCompHighStartTemperature=_BatteryTempCompHighStartTemperature_Object((1,3,6,1,4,1,13858,7,1,5),_BatteryTempCompHighStartTemperature_Type())
batteryTempCompHighStartTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompHighStartTemperature.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompHighStartTemperature.setUnits(_M)
_BatteryTempCompHighStopVoltage_Type=Integer32
_BatteryTempCompHighStopVoltage_Object=MibScalar
batteryTempCompHighStopVoltage=_BatteryTempCompHighStopVoltage_Object((1,3,6,1,4,1,13858,7,1,6),_BatteryTempCompHighStopVoltage_Type())
batteryTempCompHighStopVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompHighStopVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompHighStopVoltage.setUnits(_G)
class _BatteryTempCompHighSlope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_BatteryTempCompHighSlope_Type.__name__=_F
_BatteryTempCompHighSlope_Object=MibScalar
batteryTempCompHighSlope=_BatteryTempCompHighSlope_Object((1,3,6,1,4,1,13858,7,1,7),_BatteryTempCompHighSlope_Type())
batteryTempCompHighSlope.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompHighSlope.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompHighSlope.setUnits(_x)
_BatteryTempCompLowStartTemperature_Type=Integer32
_BatteryTempCompLowStartTemperature_Object=MibScalar
batteryTempCompLowStartTemperature=_BatteryTempCompLowStartTemperature_Object((1,3,6,1,4,1,13858,7,1,8),_BatteryTempCompLowStartTemperature_Type())
batteryTempCompLowStartTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompLowStartTemperature.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompLowStartTemperature.setUnits(_M)
_BatteryTempCompLowStopVoltage_Type=Integer32
_BatteryTempCompLowStopVoltage_Object=MibScalar
batteryTempCompLowStopVoltage=_BatteryTempCompLowStopVoltage_Object((1,3,6,1,4,1,13858,7,1,9),_BatteryTempCompLowStopVoltage_Type())
batteryTempCompLowStopVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompLowStopVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompLowStopVoltage.setUnits(_G)
class _BatteryTempCompLowSlope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_BatteryTempCompLowSlope_Type.__name__=_F
_BatteryTempCompLowSlope_Object=MibScalar
batteryTempCompLowSlope=_BatteryTempCompLowSlope_Object((1,3,6,1,4,1,13858,7,1,10),_BatteryTempCompLowSlope_Type())
batteryTempCompLowSlope.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompLowSlope.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompLowSlope.setUnits(_x)
class _BatteryTempCompRunawayTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,60))
_BatteryTempCompRunawayTemperature_Type.__name__=_F
_BatteryTempCompRunawayTemperature_Object=MibScalar
batteryTempCompRunawayTemperature=_BatteryTempCompRunawayTemperature_Object((1,3,6,1,4,1,13858,7,1,11),_BatteryTempCompRunawayTemperature_Type())
batteryTempCompRunawayTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompRunawayTemperature.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompRunawayTemperature.setUnits(_M)
_BatteryTempCompRunawayStopVoltage_Type=Integer32
_BatteryTempCompRunawayStopVoltage_Object=MibScalar
batteryTempCompRunawayStopVoltage=_BatteryTempCompRunawayStopVoltage_Object((1,3,6,1,4,1,13858,7,1,12),_BatteryTempCompRunawayStopVoltage_Type())
batteryTempCompRunawayStopVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompRunawayStopVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryTempCompRunawayStopVoltage.setUnits(_G)
class _BatteryTempCompSenseSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_i,0),(_j,1)))
_BatteryTempCompSenseSource_Type.__name__=_F
_BatteryTempCompSenseSource_Object=MibScalar
batteryTempCompSenseSource=_BatteryTempCompSenseSource_Object((1,3,6,1,4,1,13858,7,1,13),_BatteryTempCompSenseSource_Type())
batteryTempCompSenseSource.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryTempCompSenseSource.setStatus(_A)
class _BatteryTempCompRunawayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_y,0),(_z,1)))
_BatteryTempCompRunawayState_Type.__name__=_F
_BatteryTempCompRunawayState_Object=MibScalar
batteryTempCompRunawayState=_BatteryTempCompRunawayState_Object((1,3,6,1,4,1,13858,7,1,14),_BatteryTempCompRunawayState_Type())
batteryTempCompRunawayState.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryTempCompRunawayState.setStatus(_A)
_VpwrBatteryCurrentGroup_ObjectIdentity=ObjectIdentity
vpwrBatteryCurrentGroup=_VpwrBatteryCurrentGroup_ObjectIdentity((1,3,6,1,4,1,13858,7,2))
class _VpwrBatteryCurrentLimitAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('batteryCurrentLimitDisabled',0),('batteryCurrentLimitEnabled',1)))
_VpwrBatteryCurrentLimitAdminState_Type.__name__=_F
_VpwrBatteryCurrentLimitAdminState_Object=MibScalar
vpwrBatteryCurrentLimitAdminState=_VpwrBatteryCurrentLimitAdminState_Object((1,3,6,1,4,1,13858,7,2,1),_VpwrBatteryCurrentLimitAdminState_Type())
vpwrBatteryCurrentLimitAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryCurrentLimitAdminState.setStatus(_A)
class _VpwrBatteryCurrentLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_VpwrBatteryCurrentLimit_Type.__name__=_F
_VpwrBatteryCurrentLimit_Object=MibScalar
vpwrBatteryCurrentLimit=_VpwrBatteryCurrentLimit_Object((1,3,6,1,4,1,13858,7,2,2),_VpwrBatteryCurrentLimit_Type())
vpwrBatteryCurrentLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBatteryCurrentLimit.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryCurrentLimit.setUnits('Ampere')
_VpwrBatteryCurrent_Type=Integer32
_VpwrBatteryCurrent_Object=MibScalar
vpwrBatteryCurrent=_VpwrBatteryCurrent_Object((1,3,6,1,4,1,13858,7,2,3),_VpwrBatteryCurrent_Type())
vpwrBatteryCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBatteryCurrent.setStatus(_A)
if mibBuilder.loadTexts:vpwrBatteryCurrent.setUnits('Ampere')
_VpwrBatteryBoostGroup_ObjectIdentity=ObjectIdentity
vpwrBatteryBoostGroup=_VpwrBatteryBoostGroup_ObjectIdentity((1,3,6,1,4,1,13858,7,3))
class _VpwrBoostAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('boostDisabled',0),('boostEnabled',1)))
_VpwrBoostAdminState_Type.__name__=_F
_VpwrBoostAdminState_Object=MibScalar
vpwrBoostAdminState=_VpwrBoostAdminState_Object((1,3,6,1,4,1,13858,7,3,1),_VpwrBoostAdminState_Type())
vpwrBoostAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBoostAdminState.setStatus(_A)
_VpwrBoostVoltage_Type=Integer32
_VpwrBoostVoltage_Object=MibScalar
vpwrBoostVoltage=_VpwrBoostVoltage_Object((1,3,6,1,4,1,13858,7,3,2),_VpwrBoostVoltage_Type())
vpwrBoostVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBoostVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBoostVoltage.setUnits(_G)
class _VpwrBoostDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,921599))
_VpwrBoostDuration_Type.__name__=_F
_VpwrBoostDuration_Object=MibScalar
vpwrBoostDuration=_VpwrBoostDuration_Object((1,3,6,1,4,1,13858,7,3,3),_VpwrBoostDuration_Type())
vpwrBoostDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBoostDuration.setStatus(_A)
if mibBuilder.loadTexts:vpwrBoostDuration.setUnits('Seconds')
class _VpwrBoostOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('boostInactive',0),('boostActive',1)))
_VpwrBoostOperState_Type.__name__=_F
_VpwrBoostOperState_Object=MibScalar
vpwrBoostOperState=_VpwrBoostOperState_Object((1,3,6,1,4,1,13858,7,3,4),_VpwrBoostOperState_Type())
vpwrBoostOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBoostOperState.setStatus(_A)
_VpwrBatteryDischargeTestGroup_ObjectIdentity=ObjectIdentity
vpwrBatteryDischargeTestGroup=_VpwrBatteryDischargeTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,7,4))
class _VpwrBDTAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bdtManualDisabled',0),('bdtManualEnabled',1)))
_VpwrBDTAdminState_Type.__name__=_F
_VpwrBDTAdminState_Object=MibScalar
vpwrBDTAdminState=_VpwrBDTAdminState_Object((1,3,6,1,4,1,13858,7,4,1),_VpwrBDTAdminState_Type())
vpwrBDTAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBDTAdminState.setStatus(_A)
class _VpwrBDTDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64799))
_VpwrBDTDuration_Type.__name__=_F
_VpwrBDTDuration_Object=MibScalar
vpwrBDTDuration=_VpwrBDTDuration_Object((1,3,6,1,4,1,13858,7,4,2),_VpwrBDTDuration_Type())
vpwrBDTDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTDuration.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTDuration.setUnits('Seconds')
_VpwrBDTAlarmVoltage_Type=Integer32
_VpwrBDTAlarmVoltage_Object=MibScalar
vpwrBDTAlarmVoltage=_VpwrBDTAlarmVoltage_Object((1,3,6,1,4,1,13858,7,4,3),_VpwrBDTAlarmVoltage_Type())
vpwrBDTAlarmVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBDTAlarmVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTAlarmVoltage.setUnits(_G)
_VpwrBDTAbortVoltage_Type=Integer32
_VpwrBDTAbortVoltage_Object=MibScalar
vpwrBDTAbortVoltage=_VpwrBDTAbortVoltage_Object((1,3,6,1,4,1,13858,7,4,4),_VpwrBDTAbortVoltage_Type())
vpwrBDTAbortVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBDTAbortVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTAbortVoltage.setUnits(_G)
_VpwrBDTAlarmCoefficient_Type=Integer32
_VpwrBDTAlarmCoefficient_Object=MibScalar
vpwrBDTAlarmCoefficient=_VpwrBDTAlarmCoefficient_Object((1,3,6,1,4,1,13858,7,4,5),_VpwrBDTAlarmCoefficient_Type())
vpwrBDTAlarmCoefficient.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTAlarmCoefficient.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTAlarmCoefficient.setUnits('None')
class _VpwrBDTOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,14)));namedValues=NamedValues(*((_X,0),(_Y,1),(_Z,14)))
_VpwrBDTOperState_Type.__name__=_F
_VpwrBDTOperState_Object=MibScalar
vpwrBDTOperState=_VpwrBDTOperState_Object((1,3,6,1,4,1,13858,7,4,6),_VpwrBDTOperState_Type())
vpwrBDTOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTOperState.setStatus(_A)
class _VpwrBDTClearAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bdtNoAlarm',0),('bdtAlarmPresent',1)))
_VpwrBDTClearAlarm_Type.__name__=_F
_VpwrBDTClearAlarm_Object=MibScalar
vpwrBDTClearAlarm=_VpwrBDTClearAlarm_Object((1,3,6,1,4,1,13858,7,4,7),_VpwrBDTClearAlarm_Type())
vpwrBDTClearAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTClearAlarm.setStatus(_A)
_VpwrBDTActualTime_Type=Integer32
_VpwrBDTActualTime_Object=MibScalar
vpwrBDTActualTime=_VpwrBDTActualTime_Object((1,3,6,1,4,1,13858,7,4,8),_VpwrBDTActualTime_Type())
vpwrBDTActualTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTActualTime.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTActualTime.setUnits(_S)
_VpwrBDTAlarmDelay_Type=Integer32
_VpwrBDTAlarmDelay_Object=MibScalar
vpwrBDTAlarmDelay=_VpwrBDTAlarmDelay_Object((1,3,6,1,4,1,13858,7,4,9),_VpwrBDTAlarmDelay_Type())
vpwrBDTAlarmDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTAlarmDelay.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTAlarmDelay.setUnits(_S)
_VpwrBDTResult_Type=BDTResultTC
_VpwrBDTResult_Object=MibScalar
vpwrBDTResult=_VpwrBDTResult_Object((1,3,6,1,4,1,13858,7,4,10),_VpwrBDTResult_Type())
vpwrBDTResult.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTResult.setStatus(_A)
class _VpwrBDTAutoAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bdtAutoDisabled',0),('bdtAutoEnabled',1)))
_VpwrBDTAutoAdminState_Type.__name__=_F
_VpwrBDTAutoAdminState_Object=MibScalar
vpwrBDTAutoAdminState=_VpwrBDTAutoAdminState_Object((1,3,6,1,4,1,13858,7,4,11),_VpwrBDTAutoAdminState_Type())
vpwrBDTAutoAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBDTAutoAdminState.setStatus(_A)
_VpwrBDTHistTable_Object=MibTable
vpwrBDTHistTable=_VpwrBDTHistTable_Object((1,3,6,1,4,1,13858,7,4,12))
if mibBuilder.loadTexts:vpwrBDTHistTable.setStatus(_A)
_VpwrBDTHistEntry_Object=MibTableRow
vpwrBDTHistEntry=_VpwrBDTHistEntry_Object((1,3,6,1,4,1,13858,7,4,12,1))
vpwrBDTHistEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:vpwrBDTHistEntry.setStatus(_A)
_VpwrBDTHistIndex_Type=PositiveInteger
_VpwrBDTHistIndex_Object=MibTableColumn
vpwrBDTHistIndex=_VpwrBDTHistIndex_Object((1,3,6,1,4,1,13858,7,4,12,1,1),_VpwrBDTHistIndex_Type())
vpwrBDTHistIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTHistIndex.setStatus(_A)
_VpwrBDTHistDateTime_Type=DisplayString
_VpwrBDTHistDateTime_Object=MibTableColumn
vpwrBDTHistDateTime=_VpwrBDTHistDateTime_Object((1,3,6,1,4,1,13858,7,4,12,1,2),_VpwrBDTHistDateTime_Type())
vpwrBDTHistDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTHistDateTime.setStatus(_A)
_VpwrBDTHistDuration_Type=PositiveInteger
_VpwrBDTHistDuration_Object=MibTableColumn
vpwrBDTHistDuration=_VpwrBDTHistDuration_Object((1,3,6,1,4,1,13858,7,4,12,1,3),_VpwrBDTHistDuration_Type())
vpwrBDTHistDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTHistDuration.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTHistDuration.setUnits('Minutes')
_VpwrBDTHistAlarmVoltage_Type=PositiveInteger
_VpwrBDTHistAlarmVoltage_Object=MibTableColumn
vpwrBDTHistAlarmVoltage=_VpwrBDTHistAlarmVoltage_Object((1,3,6,1,4,1,13858,7,4,12,1,4),_VpwrBDTHistAlarmVoltage_Type())
vpwrBDTHistAlarmVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBDTHistAlarmVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTHistAlarmVoltage.setUnits(_G)
_VpwrBDTHistAbortVoltage_Type=PositiveInteger
_VpwrBDTHistAbortVoltage_Object=MibTableColumn
vpwrBDTHistAbortVoltage=_VpwrBDTHistAbortVoltage_Object((1,3,6,1,4,1,13858,7,4,12,1,5),_VpwrBDTHistAbortVoltage_Type())
vpwrBDTHistAbortVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTHistAbortVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTHistAbortVoltage.setUnits(_G)
_VpwrBDTHistStartMethod_Type=BDTStartSourceTC
_VpwrBDTHistStartMethod_Object=MibTableColumn
vpwrBDTHistStartMethod=_VpwrBDTHistStartMethod_Object((1,3,6,1,4,1,13858,7,4,12,1,6),_VpwrBDTHistStartMethod_Type())
vpwrBDTHistStartMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTHistStartMethod.setStatus(_A)
_VpwrBDTHistResult_Type=BDTResultTC
_VpwrBDTHistResult_Object=MibTableColumn
vpwrBDTHistResult=_VpwrBDTHistResult_Object((1,3,6,1,4,1,13858,7,4,12,1,7),_VpwrBDTHistResult_Type())
vpwrBDTHistResult.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTHistResult.setStatus(_A)
_VpwrBDTHistActualTime_Type=PositiveInteger
_VpwrBDTHistActualTime_Object=MibTableColumn
vpwrBDTHistActualTime=_VpwrBDTHistActualTime_Object((1,3,6,1,4,1,13858,7,4,12,1,8),_VpwrBDTHistActualTime_Type())
vpwrBDTHistActualTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTHistActualTime.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTHistActualTime.setUnits(_S)
_VpwrBDTHistStartVoltage_Type=PositiveInteger
_VpwrBDTHistStartVoltage_Object=MibTableColumn
vpwrBDTHistStartVoltage=_VpwrBDTHistStartVoltage_Object((1,3,6,1,4,1,13858,7,4,12,1,9),_VpwrBDTHistStartVoltage_Type())
vpwrBDTHistStartVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTHistStartVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTHistStartVoltage.setUnits(_G)
_VpwrBDTHistEndVoltage_Type=PositiveInteger
_VpwrBDTHistEndVoltage_Object=MibTableColumn
vpwrBDTHistEndVoltage=_VpwrBDTHistEndVoltage_Object((1,3,6,1,4,1,13858,7,4,12,1,10),_VpwrBDTHistEndVoltage_Type())
vpwrBDTHistEndVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTHistEndVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrBDTHistEndVoltage.setUnits(_G)
_VpwrBDTSchedTable_Object=MibTable
vpwrBDTSchedTable=_VpwrBDTSchedTable_Object((1,3,6,1,4,1,13858,7,4,13))
if mibBuilder.loadTexts:vpwrBDTSchedTable.setStatus(_A)
_VpwrBDTSchedEntry_Object=MibTableRow
vpwrBDTSchedEntry=_VpwrBDTSchedEntry_Object((1,3,6,1,4,1,13858,7,4,13,1))
vpwrBDTSchedEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:vpwrBDTSchedEntry.setStatus(_A)
_VpwrBDTSchedIndex_Type=PositiveInteger
_VpwrBDTSchedIndex_Object=MibTableColumn
vpwrBDTSchedIndex=_VpwrBDTSchedIndex_Object((1,3,6,1,4,1,13858,7,4,13,1,1),_VpwrBDTSchedIndex_Type())
vpwrBDTSchedIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBDTSchedIndex.setStatus(_A)
_VpwrBDTSchedDay_Type=PositiveInteger
_VpwrBDTSchedDay_Object=MibTableColumn
vpwrBDTSchedDay=_VpwrBDTSchedDay_Object((1,3,6,1,4,1,13858,7,4,13,1,2),_VpwrBDTSchedDay_Type())
vpwrBDTSchedDay.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBDTSchedDay.setStatus(_A)
_VpwrBDTSchedMonth_Type=PositiveInteger
_VpwrBDTSchedMonth_Object=MibTableColumn
vpwrBDTSchedMonth=_VpwrBDTSchedMonth_Object((1,3,6,1,4,1,13858,7,4,13,1,3),_VpwrBDTSchedMonth_Type())
vpwrBDTSchedMonth.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBDTSchedMonth.setStatus(_A)
_VpwrBDTSchedHour_Type=PositiveInteger
_VpwrBDTSchedHour_Object=MibTableColumn
vpwrBDTSchedHour=_VpwrBDTSchedHour_Object((1,3,6,1,4,1,13858,7,4,13,1,4),_VpwrBDTSchedHour_Type())
vpwrBDTSchedHour.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBDTSchedHour.setStatus(_A)
_VpwrBDTSchedMinute_Type=PositiveInteger
_VpwrBDTSchedMinute_Object=MibTableColumn
vpwrBDTSchedMinute=_VpwrBDTSchedMinute_Object((1,3,6,1,4,1,13858,7,4,13,1,5),_VpwrBDTSchedMinute_Type())
vpwrBDTSchedMinute.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrBDTSchedMinute.setStatus(_A)
_VpwrDcPowerAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrDcPowerAlarmGroup=_VpwrDcPowerAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,8))
_VpwrAlarmsPresent_Type=Gauge32
_VpwrAlarmsPresent_Object=MibScalar
vpwrAlarmsPresent=_VpwrAlarmsPresent_Object((1,3,6,1,4,1,13858,8,1),_VpwrAlarmsPresent_Type())
vpwrAlarmsPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrAlarmsPresent.setStatus(_A)
_VpwrAlarmTable_Object=MibTable
vpwrAlarmTable=_VpwrAlarmTable_Object((1,3,6,1,4,1,13858,8,2))
if mibBuilder.loadTexts:vpwrAlarmTable.setStatus(_A)
_VpwrAlarmEntry_Object=MibTableRow
vpwrAlarmEntry=_VpwrAlarmEntry_Object((1,3,6,1,4,1,13858,8,2,1))
vpwrAlarmEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_A2))
if mibBuilder.loadTexts:vpwrAlarmEntry.setStatus(_A)
_VpwrAlarmIndex_Type=PositiveInteger
_VpwrAlarmIndex_Object=MibTableColumn
vpwrAlarmIndex=_VpwrAlarmIndex_Object((1,3,6,1,4,1,13858,8,2,1,1),_VpwrAlarmIndex_Type())
vpwrAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrAlarmIndex.setStatus(_A)
_VpwrAlarmDescr_Type=AutonomousType
_VpwrAlarmDescr_Object=MibTableColumn
vpwrAlarmDescr=_VpwrAlarmDescr_Object((1,3,6,1,4,1,13858,8,2,1,2),_VpwrAlarmDescr_Type())
vpwrAlarmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrAlarmDescr.setStatus(_A)
_VpwrAlarmTime_Type=TimeStamp
_VpwrAlarmTime_Object=MibTableColumn
vpwrAlarmTime=_VpwrAlarmTime_Object((1,3,6,1,4,1,13858,8,2,1,3),_VpwrAlarmTime_Type())
vpwrAlarmTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrAlarmTime.setStatus(_A)
_SysAlarmConfigTable_Object=MibTable
sysAlarmConfigTable=_SysAlarmConfigTable_Object((1,3,6,1,4,1,13858,8,3))
if mibBuilder.loadTexts:sysAlarmConfigTable.setStatus(_A)
_SysAlarmConfigEntry_Object=MibTableRow
sysAlarmConfigEntry=_SysAlarmConfigEntry_Object((1,3,6,1,4,1,13858,8,3,1))
sysAlarmConfigEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:sysAlarmConfigEntry.setStatus(_A)
class _SysAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SysAlarmIndex_Type.__name__=_F
_SysAlarmIndex_Object=MibTableColumn
sysAlarmIndex=_SysAlarmIndex_Object((1,3,6,1,4,1,13858,8,3,1,1),_SysAlarmIndex_Type())
sysAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sysAlarmIndex.setStatus(_A)
class _SysAlarmDefaultName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAlarmDefaultName_Type.__name__=_H
_SysAlarmDefaultName_Object=MibTableColumn
sysAlarmDefaultName=_SysAlarmDefaultName_Object((1,3,6,1,4,1,13858,8,3,1,2),_SysAlarmDefaultName_Type())
sysAlarmDefaultName.setMaxAccess(_B)
if mibBuilder.loadTexts:sysAlarmDefaultName.setStatus(_A)
class _SysAlarmCustomName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAlarmCustomName_Type.__name__=_H
_SysAlarmCustomName_Object=MibTableColumn
sysAlarmCustomName=_SysAlarmCustomName_Object((1,3,6,1,4,1,13858,8,3,1,3),_SysAlarmCustomName_Type())
sysAlarmCustomName.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmCustomName.setStatus(_A)
class _SysAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('major',1),('minor',2),('majorAndMinor',3)))
_SysAlarmSeverity_Type.__name__=_F
_SysAlarmSeverity_Object=MibTableColumn
sysAlarmSeverity=_SysAlarmSeverity_Object((1,3,6,1,4,1,13858,8,3,1,4),_SysAlarmSeverity_Type())
sysAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmSeverity.setStatus(_A)
class _SysAlarmToRelayMapping_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SysAlarmToRelayMapping_Type.__name__=_H
_SysAlarmToRelayMapping_Object=MibTableColumn
sysAlarmToRelayMapping=_SysAlarmToRelayMapping_Object((1,3,6,1,4,1,13858,8,3,1,5),_SysAlarmToRelayMapping_Type())
sysAlarmToRelayMapping.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmToRelayMapping.setStatus(_A)
class _SysAlarmOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_y,0),(_z,1)))
_SysAlarmOperStatus_Type.__name__=_F
_SysAlarmOperStatus_Object=MibTableColumn
sysAlarmOperStatus=_SysAlarmOperStatus_Object((1,3,6,1,4,1,13858,8,3,1,6),_SysAlarmOperStatus_Type())
sysAlarmOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysAlarmOperStatus.setStatus(_A)
class _SysAlarmComFailState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_P,1),('other',2)))
_SysAlarmComFailState_Type.__name__=_F
_SysAlarmComFailState_Object=MibScalar
sysAlarmComFailState=_SysAlarmComFailState_Object((1,3,6,1,4,1,13858,8,4),_SysAlarmComFailState_Type())
sysAlarmComFailState.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmComFailState.setStatus(_A)
class _SysAlarmIShareState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_P,1),('other',2)))
_SysAlarmIShareState_Type.__name__=_F
_SysAlarmIShareState_Object=MibScalar
sysAlarmIShareState=_SysAlarmIShareState_Object((1,3,6,1,4,1,13858,8,5),_SysAlarmIShareState_Type())
sysAlarmIShareState.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmIShareState.setStatus(_A)
class _SysAlarmRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('nPlus1',1),('nPlus2',2)))
_SysAlarmRedundancyState_Type.__name__=_F
_SysAlarmRedundancyState_Object=MibScalar
sysAlarmRedundancyState=_SysAlarmRedundancyState_Object((1,3,6,1,4,1,13858,8,6),_SysAlarmRedundancyState_Type())
sysAlarmRedundancyState.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmRedundancyState.setStatus(_A)
class _SysAlarmComFailToACFailState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_P,1)))
_SysAlarmComFailToACFailState_Type.__name__=_F
_SysAlarmComFailToACFailState_Object=MibScalar
sysAlarmComFailToACFailState=_SysAlarmComFailToACFailState_Object((1,3,6,1,4,1,13858,8,7),_SysAlarmComFailToACFailState_Type())
sysAlarmComFailToACFailState.setMaxAccess(_D)
if mibBuilder.loadTexts:sysAlarmComFailToACFailState.setStatus(_A)
_VpwrDcPowerSnmpConfig_ObjectIdentity=ObjectIdentity
vpwrDcPowerSnmpConfig=_VpwrDcPowerSnmpConfig_ObjectIdentity((1,3,6,1,4,1,13858,9))
_VpwrTrapTable_Object=MibTable
vpwrTrapTable=_VpwrTrapTable_Object((1,3,6,1,4,1,13858,9,1))
if mibBuilder.loadTexts:vpwrTrapTable.setStatus(_A)
_VpwrTrapEntry_Object=MibTableRow
vpwrTrapEntry=_VpwrTrapEntry_Object((1,3,6,1,4,1,13858,9,1,1))
vpwrTrapEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:vpwrTrapEntry.setStatus(_A)
class _VpwrTrapIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VpwrTrapIpIndex_Type.__name__=_F
_VpwrTrapIpIndex_Object=MibTableColumn
vpwrTrapIpIndex=_VpwrTrapIpIndex_Object((1,3,6,1,4,1,13858,9,1,1,1),_VpwrTrapIpIndex_Type())
vpwrTrapIpIndex.setMaxAccess(_B)
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
_VpwrReadCommunityString_Type.__name__=_H
_VpwrReadCommunityString_Object=MibScalar
vpwrReadCommunityString=_VpwrReadCommunityString_Object((1,3,6,1,4,1,13858,9,2),_VpwrReadCommunityString_Type())
vpwrReadCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrReadCommunityString.setStatus(_A)
class _VpwrWriteCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,8))
_VpwrWriteCommunityString_Type.__name__=_H
_VpwrWriteCommunityString_Object=MibScalar
vpwrWriteCommunityString=_VpwrWriteCommunityString_Object((1,3,6,1,4,1,13858,9,3),_VpwrWriteCommunityString_Type())
vpwrWriteCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrWriteCommunityString.setStatus(_A)
class _VpwrTrapCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,8))
_VpwrTrapCommunityString_Type.__name__=_H
_VpwrTrapCommunityString_Object=MibScalar
vpwrTrapCommunityString=_VpwrTrapCommunityString_Object((1,3,6,1,4,1,13858,9,4),_VpwrTrapCommunityString_Type())
vpwrTrapCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrTrapCommunityString.setStatus(_A)
_VpwrTrapVersion_Type=Integer32
_VpwrTrapVersion_Object=MibScalar
vpwrTrapVersion=_VpwrTrapVersion_Object((1,3,6,1,4,1,13858,9,5),_VpwrTrapVersion_Type())
vpwrTrapVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrTrapVersion.setStatus(_A)
_VpwrDcPowerTraps_ObjectIdentity=ObjectIdentity
vpwrDcPowerTraps=_VpwrDcPowerTraps_ObjectIdentity((1,3,6,1,4,1,13858,10))
_VpwrDcPowerTrapVars_ObjectIdentity=ObjectIdentity
vpwrDcPowerTrapVars=_VpwrDcPowerTrapVars_ObjectIdentity((1,3,6,1,4,1,13858,11))
class _VpwrTrapsMsgString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_VpwrTrapsMsgString_Type.__name__=_H
_VpwrTrapsMsgString_Object=MibScalar
vpwrTrapsMsgString=_VpwrTrapsMsgString_Object((1,3,6,1,4,1,13858,11,1),_VpwrTrapsMsgString_Type())
vpwrTrapsMsgString.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrTrapsMsgString.setStatus(_A)
_VpwrTrapUserIpAddress_Type=IpAddress
_VpwrTrapUserIpAddress_Object=MibScalar
vpwrTrapUserIpAddress=_VpwrTrapUserIpAddress_Object((1,3,6,1,4,1,13858,11,2),_VpwrTrapUserIpAddress_Type())
vpwrTrapUserIpAddress.setMaxAccess(_A5)
if mibBuilder.loadTexts:vpwrTrapUserIpAddress.setStatus(_A)
_VpwrTrapAcfDuration_Type=NonNegativeInteger
_VpwrTrapAcfDuration_Object=MibScalar
vpwrTrapAcfDuration=_VpwrTrapAcfDuration_Object((1,3,6,1,4,1,13858,11,3),_VpwrTrapAcfDuration_Type())
vpwrTrapAcfDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrTrapAcfDuration.setStatus(_A)
_VpwrAlarmingSubModuleBitMap_Type=PositiveInteger
_VpwrAlarmingSubModuleBitMap_Object=MibScalar
vpwrAlarmingSubModuleBitMap=_VpwrAlarmingSubModuleBitMap_Object((1,3,6,1,4,1,13858,11,4),_VpwrAlarmingSubModuleBitMap_Type())
vpwrAlarmingSubModuleBitMap.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrAlarmingSubModuleBitMap.setStatus(_A)
_VpwrBatteryCurrentCapacity_Type=PositiveInteger
_VpwrBatteryCurrentCapacity_Object=MibScalar
vpwrBatteryCurrentCapacity=_VpwrBatteryCurrentCapacity_Object((1,3,6,1,4,1,13858,11,5),_VpwrBatteryCurrentCapacity_Type())
vpwrBatteryCurrentCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBatteryCurrentCapacity.setStatus(_A)
_VpwrAlarmingModuleIndex_Type=PositiveInteger
_VpwrAlarmingModuleIndex_Object=MibScalar
vpwrAlarmingModuleIndex=_VpwrAlarmingModuleIndex_Object((1,3,6,1,4,1,13858,11,6),_VpwrAlarmingModuleIndex_Type())
vpwrAlarmingModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrAlarmingModuleIndex.setStatus(_A)
_VpwrAlarmingModuleOID_Type=ObjectIdentifier
_VpwrAlarmingModuleOID_Object=MibScalar
vpwrAlarmingModuleOID=_VpwrAlarmingModuleOID_Object((1,3,6,1,4,1,13858,11,7),_VpwrAlarmingModuleOID_Type())
vpwrAlarmingModuleOID.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrAlarmingModuleOID.setStatus(_A)
_VpwrAlarmingModuleBitMap_Type=PositiveInteger
_VpwrAlarmingModuleBitMap_Object=MibScalar
vpwrAlarmingModuleBitMap=_VpwrAlarmingModuleBitMap_Object((1,3,6,1,4,1,13858,11,8),_VpwrAlarmingModuleBitMap_Type())
vpwrAlarmingModuleBitMap.setMaxAccess(_A5)
if mibBuilder.loadTexts:vpwrAlarmingModuleBitMap.setStatus(_A)
_VpwrBatteryRemainingTime_Type=PositiveInteger
_VpwrBatteryRemainingTime_Object=MibScalar
vpwrBatteryRemainingTime=_VpwrBatteryRemainingTime_Object((1,3,6,1,4,1,13858,11,9),_VpwrBatteryRemainingTime_Type())
vpwrBatteryRemainingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrBatteryRemainingTime.setStatus(_A)
_VpwrDcPowerRinger_ObjectIdentity=ObjectIdentity
vpwrDcPowerRinger=_VpwrDcPowerRinger_ObjectIdentity((1,3,6,1,4,1,13858,12))
_VpwrRingerConfigGroup_ObjectIdentity=ObjectIdentity
vpwrRingerConfigGroup=_VpwrRingerConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,12,1))
class _VpwrRingerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_VpwrRingerIndex_Type.__name__=_F
_VpwrRingerIndex_Object=MibScalar
vpwrRingerIndex=_VpwrRingerIndex_Object((1,3,6,1,4,1,13858,12,1,1),_VpwrRingerIndex_Type())
vpwrRingerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRingerIndex.setStatus(_A)
class _VpwrRingerParameterAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ringerDisabled',0),('ringerAOn',1),('ringerBOn',2)))
_VpwrRingerParameterAdminState_Type.__name__=_F
_VpwrRingerParameterAdminState_Object=MibScalar
vpwrRingerParameterAdminState=_VpwrRingerParameterAdminState_Object((1,3,6,1,4,1,13858,12,1,2),_VpwrRingerParameterAdminState_Type())
vpwrRingerParameterAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRingerParameterAdminState.setStatus(_A)
class _VpwrRingerParameterAcVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7000,10000))
_VpwrRingerParameterAcVoltage_Type.__name__=_F
_VpwrRingerParameterAcVoltage_Object=MibScalar
vpwrRingerParameterAcVoltage=_VpwrRingerParameterAcVoltage_Object((1,3,6,1,4,1,13858,12,1,3),_VpwrRingerParameterAcVoltage_Type())
vpwrRingerParameterAcVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRingerParameterAcVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrRingerParameterAcVoltage.setUnits(_G)
class _VpwrRingerParameterDcVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5500))
_VpwrRingerParameterDcVoltage_Type.__name__=_F
_VpwrRingerParameterDcVoltage_Object=MibScalar
vpwrRingerParameterDcVoltage=_VpwrRingerParameterDcVoltage_Object((1,3,6,1,4,1,13858,12,1,4),_VpwrRingerParameterDcVoltage_Type())
vpwrRingerParameterDcVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRingerParameterDcVoltage.setStatus(_A)
if mibBuilder.loadTexts:vpwrRingerParameterDcVoltage.setUnits(_G)
class _VpwrRingerParameterFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(17,50))
_VpwrRingerParameterFrequency_Type.__name__=_F
_VpwrRingerParameterFrequency_Object=MibScalar
vpwrRingerParameterFrequency=_VpwrRingerParameterFrequency_Object((1,3,6,1,4,1,13858,12,1,5),_VpwrRingerParameterFrequency_Type())
vpwrRingerParameterFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrRingerParameterFrequency.setStatus(_A)
if mibBuilder.loadTexts:vpwrRingerParameterFrequency.setUnits(' Hz')
_VpwrRingerNumberPresent_Type=Gauge32
_VpwrRingerNumberPresent_Object=MibScalar
vpwrRingerNumberPresent=_VpwrRingerNumberPresent_Object((1,3,6,1,4,1,13858,12,1,6),_VpwrRingerNumberPresent_Type())
vpwrRingerNumberPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrRingerNumberPresent.setStatus(_A)
_VpwrRingerAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmGroup=_VpwrRingerAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,12,2))
_VpwrRingerAlarmAFailed_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmAFailed=_VpwrRingerAlarmAFailed_ObjectIdentity((1,3,6,1,4,1,13858,12,2,1))
if mibBuilder.loadTexts:vpwrRingerAlarmAFailed.setStatus(_A)
_VpwrRingerAlarmAOverTemp_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmAOverTemp=_VpwrRingerAlarmAOverTemp_ObjectIdentity((1,3,6,1,4,1,13858,12,2,2))
if mibBuilder.loadTexts:vpwrRingerAlarmAOverTemp.setStatus(_A)
_VpwrRingerAlarmAOverCurrent_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmAOverCurrent=_VpwrRingerAlarmAOverCurrent_ObjectIdentity((1,3,6,1,4,1,13858,12,2,3))
if mibBuilder.loadTexts:vpwrRingerAlarmAOverCurrent.setStatus(_A)
_VpwrRingerAlarmBFailed_ObjectIdentity=ObjectIdentity
vpwrRingerAlarmBFailed=_VpwrRingerAlarmBFailed_ObjectIdentity((1,3,6,1,4,1,13858,12,2,4))
if mibBuilder.loadTexts:vpwrRingerAlarmBFailed.setStatus(_A)
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
_VpwrDcPowerAcLineModule_ObjectIdentity=ObjectIdentity
vpwrDcPowerAcLineModule=_VpwrDcPowerAcLineModule_ObjectIdentity((1,3,6,1,4,1,13858,15))
_VpwrAcLineModuleConfigGroup_ObjectIdentity=ObjectIdentity
vpwrAcLineModuleConfigGroup=_VpwrAcLineModuleConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,15,1))
_VpwrAcLineModuleAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrAcLineModuleAlarmGroup=_VpwrAcLineModuleAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,15,2))
_VpwrAcLineModuleTestGroup_ObjectIdentity=ObjectIdentity
vpwrAcLineModuleTestGroup=_VpwrAcLineModuleTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,15,3))
_VpwrDcPowerIoModule_ObjectIdentity=ObjectIdentity
vpwrDcPowerIoModule=_VpwrDcPowerIoModule_ObjectIdentity((1,3,6,1,4,1,13858,16))
_VpwrIoModuleConfigGroup_ObjectIdentity=ObjectIdentity
vpwrIoModuleConfigGroup=_VpwrIoModuleConfigGroup_ObjectIdentity((1,3,6,1,4,1,13858,16,1))
_VpwrIoModuleAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrIoModuleAlarmGroup=_VpwrIoModuleAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,16,2))
_VpwrIoModuleTestGroup_ObjectIdentity=ObjectIdentity
vpwrIoModuleTestGroup=_VpwrIoModuleTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,16,3))
_VpwrDcPowerPMModule_ObjectIdentity=ObjectIdentity
vpwrDcPowerPMModule=_VpwrDcPowerPMModule_ObjectIdentity((1,3,6,1,4,1,13858,17))
_VpwrPMCnfgTable_Object=MibTable
vpwrPMCnfgTable=_VpwrPMCnfgTable_Object((1,3,6,1,4,1,13858,17,1))
if mibBuilder.loadTexts:vpwrPMCnfgTable.setStatus(_A)
_VpwrPMCnfgEntry_Object=MibTableRow
vpwrPMCnfgEntry=_VpwrPMCnfgEntry_Object((1,3,6,1,4,1,13858,17,1,1))
vpwrPMCnfgEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:vpwrPMCnfgEntry.setStatus(_A)
_VpwrPMIndex_Type=NonNegativeInteger
_VpwrPMIndex_Object=MibTableColumn
vpwrPMIndex=_VpwrPMIndex_Object((1,3,6,1,4,1,13858,17,1,1,1),_VpwrPMIndex_Type())
vpwrPMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMIndex.setStatus(_A)
_VpwrPMDescription_Type=DisplayString
_VpwrPMDescription_Object=MibTableColumn
vpwrPMDescription=_VpwrPMDescription_Object((1,3,6,1,4,1,13858,17,1,1,2),_VpwrPMDescription_Type())
vpwrPMDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMDescription.setStatus(_A)
_VpwrPMCnfg1_Type=VpwrPMCnfgValue
_VpwrPMCnfg1_Object=MibTableColumn
vpwrPMCnfg1=_VpwrPMCnfg1_Object((1,3,6,1,4,1,13858,17,1,1,3),_VpwrPMCnfg1_Type())
vpwrPMCnfg1.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMCnfg1.setStatus(_A)
_VpwrPMCnfg2_Type=VpwrPMCnfgValue
_VpwrPMCnfg2_Object=MibTableColumn
vpwrPMCnfg2=_VpwrPMCnfg2_Object((1,3,6,1,4,1,13858,17,1,1,4),_VpwrPMCnfg2_Type())
vpwrPMCnfg2.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMCnfg2.setStatus(_A)
_VpwrPMCnfg3_Type=VpwrPMCnfgValue
_VpwrPMCnfg3_Object=MibTableColumn
vpwrPMCnfg3=_VpwrPMCnfg3_Object((1,3,6,1,4,1,13858,17,1,1,5),_VpwrPMCnfg3_Type())
vpwrPMCnfg3.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMCnfg3.setStatus(_A)
_VpwrPMCnfg4_Type=VpwrPMCnfgValue
_VpwrPMCnfg4_Object=MibTableColumn
vpwrPMCnfg4=_VpwrPMCnfg4_Object((1,3,6,1,4,1,13858,17,1,1,6),_VpwrPMCnfg4_Type())
vpwrPMCnfg4.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMCnfg4.setStatus(_A)
_VpwrPMCnfg5_Type=VpwrPMCnfgValue
_VpwrPMCnfg5_Object=MibTableColumn
vpwrPMCnfg5=_VpwrPMCnfg5_Object((1,3,6,1,4,1,13858,17,1,1,7),_VpwrPMCnfg5_Type())
vpwrPMCnfg5.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMCnfg5.setStatus(_A)
_VpwrPMCnfg6_Type=VpwrPMCnfgValue
_VpwrPMCnfg6_Object=MibTableColumn
vpwrPMCnfg6=_VpwrPMCnfg6_Object((1,3,6,1,4,1,13858,17,1,1,8),_VpwrPMCnfg6_Type())
vpwrPMCnfg6.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMCnfg6.setStatus(_A)
_VpwrPMCnfg7_Type=VpwrPMCnfgValue
_VpwrPMCnfg7_Object=MibTableColumn
vpwrPMCnfg7=_VpwrPMCnfg7_Object((1,3,6,1,4,1,13858,17,1,1,9),_VpwrPMCnfg7_Type())
vpwrPMCnfg7.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMCnfg7.setStatus(_A)
_VpwrPMCnfg8_Type=VpwrPMCnfgValue
_VpwrPMCnfg8_Object=MibTableColumn
vpwrPMCnfg8=_VpwrPMCnfg8_Object((1,3,6,1,4,1,13858,17,1,1,10),_VpwrPMCnfg8_Type())
vpwrPMCnfg8.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMCnfg8.setStatus(_A)
_VpwrPMInputStatusTable_Object=MibTable
vpwrPMInputStatusTable=_VpwrPMInputStatusTable_Object((1,3,6,1,4,1,13858,17,2))
if mibBuilder.loadTexts:vpwrPMInputStatusTable.setStatus(_A)
_VpwrPMInputStatusEntry_Object=MibTableRow
vpwrPMInputStatusEntry=_VpwrPMInputStatusEntry_Object((1,3,6,1,4,1,13858,17,2,1))
vpwrPMInputStatusEntry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:vpwrPMInputStatusEntry.setStatus(_A)
_VpwrPMIndex1_Type=NonNegativeInteger
_VpwrPMIndex1_Object=MibTableColumn
vpwrPMIndex1=_VpwrPMIndex1_Object((1,3,6,1,4,1,13858,17,2,1,1),_VpwrPMIndex1_Type())
vpwrPMIndex1.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMIndex1.setStatus(_A)
_VpwrPMDescription1_Type=DisplayString
_VpwrPMDescription1_Object=MibTableColumn
vpwrPMDescription1=_VpwrPMDescription1_Object((1,3,6,1,4,1,13858,17,2,1,2),_VpwrPMDescription1_Type())
vpwrPMDescription1.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMDescription1.setStatus(_A)
_VpwrPMInput1State_Type=SysInputValue
_VpwrPMInput1State_Object=MibTableColumn
vpwrPMInput1State=_VpwrPMInput1State_Object((1,3,6,1,4,1,13858,17,2,1,3),_VpwrPMInput1State_Type())
vpwrPMInput1State.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMInput1State.setStatus(_A)
_VpwrPMInput2State_Type=SysInputValue
_VpwrPMInput2State_Object=MibTableColumn
vpwrPMInput2State=_VpwrPMInput2State_Object((1,3,6,1,4,1,13858,17,2,1,4),_VpwrPMInput2State_Type())
vpwrPMInput2State.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMInput2State.setStatus(_A)
_VpwrPMInput3State_Type=SysInputValue
_VpwrPMInput3State_Object=MibTableColumn
vpwrPMInput3State=_VpwrPMInput3State_Object((1,3,6,1,4,1,13858,17,2,1,5),_VpwrPMInput3State_Type())
vpwrPMInput3State.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMInput3State.setStatus(_A)
_VpwrPMInput4State_Type=SysInputValue
_VpwrPMInput4State_Object=MibTableColumn
vpwrPMInput4State=_VpwrPMInput4State_Object((1,3,6,1,4,1,13858,17,2,1,6),_VpwrPMInput4State_Type())
vpwrPMInput4State.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMInput4State.setStatus(_A)
_VpwrPMInput5State_Type=SysInputValue
_VpwrPMInput5State_Object=MibTableColumn
vpwrPMInput5State=_VpwrPMInput5State_Object((1,3,6,1,4,1,13858,17,2,1,7),_VpwrPMInput5State_Type())
vpwrPMInput5State.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMInput5State.setStatus(_A)
_VpwrPMInput6State_Type=SysInputValue
_VpwrPMInput6State_Object=MibTableColumn
vpwrPMInput6State=_VpwrPMInput6State_Object((1,3,6,1,4,1,13858,17,2,1,8),_VpwrPMInput6State_Type())
vpwrPMInput6State.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMInput6State.setStatus(_A)
_VpwrPMInput7State_Type=SysInputValue
_VpwrPMInput7State_Object=MibTableColumn
vpwrPMInput7State=_VpwrPMInput7State_Object((1,3,6,1,4,1,13858,17,2,1,9),_VpwrPMInput7State_Type())
vpwrPMInput7State.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMInput7State.setStatus(_A)
_VpwrPMInput8State_Type=SysInputValue
_VpwrPMInput8State_Object=MibTableColumn
vpwrPMInput8State=_VpwrPMInput8State_Object((1,3,6,1,4,1,13858,17,2,1,10),_VpwrPMInput8State_Type())
vpwrPMInput8State.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMInput8State.setStatus(_A)
_VpwrPMRelayCtrlTable_Object=MibTable
vpwrPMRelayCtrlTable=_VpwrPMRelayCtrlTable_Object((1,3,6,1,4,1,13858,17,3))
if mibBuilder.loadTexts:vpwrPMRelayCtrlTable.setStatus(_A)
_VpwrPMRelayCtrlEntry_Object=MibTableRow
vpwrPMRelayCtrlEntry=_VpwrPMRelayCtrlEntry_Object((1,3,6,1,4,1,13858,17,3,1))
vpwrPMRelayCtrlEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:vpwrPMRelayCtrlEntry.setStatus(_A)
_VpwrPMIndex2_Type=NonNegativeInteger
_VpwrPMIndex2_Object=MibTableColumn
vpwrPMIndex2=_VpwrPMIndex2_Object((1,3,6,1,4,1,13858,17,3,1,1),_VpwrPMIndex2_Type())
vpwrPMIndex2.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMIndex2.setStatus(_A)
_VpwrPMDescription2_Type=DisplayString
_VpwrPMDescription2_Object=MibTableColumn
vpwrPMDescription2=_VpwrPMDescription2_Object((1,3,6,1,4,1,13858,17,3,1,2),_VpwrPMDescription2_Type())
vpwrPMDescription2.setMaxAccess(_B)
if mibBuilder.loadTexts:vpwrPMDescription2.setStatus(_A)
class _VpwrPMRelay1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_N,0),(_O,1),(_J,255)))
_VpwrPMRelay1State_Type.__name__=_F
_VpwrPMRelay1State_Object=MibTableColumn
vpwrPMRelay1State=_VpwrPMRelay1State_Object((1,3,6,1,4,1,13858,17,3,1,3),_VpwrPMRelay1State_Type())
vpwrPMRelay1State.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMRelay1State.setStatus(_A)
class _VpwrPMRelay2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_N,0),(_O,1),(_J,255)))
_VpwrPMRelay2State_Type.__name__=_F
_VpwrPMRelay2State_Object=MibTableColumn
vpwrPMRelay2State=_VpwrPMRelay2State_Object((1,3,6,1,4,1,13858,17,3,1,4),_VpwrPMRelay2State_Type())
vpwrPMRelay2State.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMRelay2State.setStatus(_A)
class _VpwrPMRelay3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_N,0),(_O,1),(_J,255)))
_VpwrPMRelay3State_Type.__name__=_F
_VpwrPMRelay3State_Object=MibTableColumn
vpwrPMRelay3State=_VpwrPMRelay3State_Object((1,3,6,1,4,1,13858,17,3,1,5),_VpwrPMRelay3State_Type())
vpwrPMRelay3State.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMRelay3State.setStatus(_A)
class _VpwrPMRelay4State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_N,0),(_O,1),(_J,255)))
_VpwrPMRelay4State_Type.__name__=_F
_VpwrPMRelay4State_Object=MibTableColumn
vpwrPMRelay4State=_VpwrPMRelay4State_Object((1,3,6,1,4,1,13858,17,3,1,6),_VpwrPMRelay4State_Type())
vpwrPMRelay4State.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMRelay4State.setStatus(_A)
class _VpwrPMRelay5State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_N,0),(_O,1),(_J,255)))
_VpwrPMRelay5State_Type.__name__=_F
_VpwrPMRelay5State_Object=MibTableColumn
vpwrPMRelay5State=_VpwrPMRelay5State_Object((1,3,6,1,4,1,13858,17,3,1,7),_VpwrPMRelay5State_Type())
vpwrPMRelay5State.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMRelay5State.setStatus(_A)
class _VpwrPMRelay6State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_N,0),(_O,1),(_J,255)))
_VpwrPMRelay6State_Type.__name__=_F
_VpwrPMRelay6State_Object=MibTableColumn
vpwrPMRelay6State=_VpwrPMRelay6State_Object((1,3,6,1,4,1,13858,17,3,1,8),_VpwrPMRelay6State_Type())
vpwrPMRelay6State.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwrPMRelay6State.setStatus(_A)
_VpwrPMModuleAlarmGroup_ObjectIdentity=ObjectIdentity
vpwrPMModuleAlarmGroup=_VpwrPMModuleAlarmGroup_ObjectIdentity((1,3,6,1,4,1,13858,17,4))
_VpwrPMModuleTestGroup_ObjectIdentity=ObjectIdentity
vpwrPMModuleTestGroup=_VpwrPMModuleTestGroup_ObjectIdentity((1,3,6,1,4,1,13858,17,5))
_VpwrDcPowerDistModule_ObjectIdentity=ObjectIdentity
vpwrDcPowerDistModule=_VpwrDcPowerDistModule_ObjectIdentity((1,3,6,1,4,1,13858,18))
_VpwrDcPowerBattery_ObjectIdentity=ObjectIdentity
vpwrDcPowerBattery=_VpwrDcPowerBattery_ObjectIdentity((1,3,6,1,4,1,13858,19))
_VpwrDcPowerController_ObjectIdentity=ObjectIdentity
vpwrDcPowerController=_VpwrDcPowerController_ObjectIdentity((1,3,6,1,4,1,13858,20))
_VpwrDcPowerUnkModule_ObjectIdentity=ObjectIdentity
vpwrDcPowerUnkModule=_VpwrDcPowerUnkModule_ObjectIdentity((1,3,6,1,4,1,13858,499))
_ThirdPartyProduct_ObjectIdentity=ObjectIdentity
thirdPartyProduct=_ThirdPartyProduct_ObjectIdentity((1,3,6,1,4,1,13858,500))
vpwrTrapPowerMajorAlarm=NotificationType((1,3,6,1,4,1,13858,10,1))
vpwrTrapPowerMajorAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapPowerMajorAlarm.setStatus(_A)
vpwrTrapPowerMinorAlarm=NotificationType((1,3,6,1,4,1,13858,10,2))
vpwrTrapPowerMinorAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapPowerMinorAlarm.setStatus(_A)
vpwrTrapACFAlarm=NotificationType((1,3,6,1,4,1,13858,10,3))
vpwrTrapACFAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapACFAlarm.setStatus(_A)
vpwrTrapHVAlarm=NotificationType((1,3,6,1,4,1,13858,10,4))
vpwrTrapHVAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapHVAlarm.setStatus(_A)
vpwrTrapHVSDAlarm=NotificationType((1,3,6,1,4,1,13858,10,5))
vpwrTrapHVSDAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapHVSDAlarm.setStatus(_A)
vpwrTrapBDAlarm=NotificationType((1,3,6,1,4,1,13858,10,6))
vpwrTrapBDAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapBDAlarm.setStatus(_A)
vpwrTrapLVDWarningAlarm=NotificationType((1,3,6,1,4,1,13858,10,7))
vpwrTrapLVDWarningAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapLVDWarningAlarm.setStatus(_A)
vpwrTrapLVDOpenAlarm=NotificationType((1,3,6,1,4,1,13858,10,8))
vpwrTrapLVDOpenAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapLVDOpenAlarm.setStatus(_A)
vpwrTrapDistAlarm=NotificationType((1,3,6,1,4,1,13858,10,9))
vpwrTrapDistAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapDistAlarm.setStatus(_A)
vpwrTrapAuxAlarm=NotificationType((1,3,6,1,4,1,13858,10,10))
vpwrTrapAuxAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapAuxAlarm.setStatus(_A)
vpwrTrapSystemRedundancyAlarm=NotificationType((1,3,6,1,4,1,13858,10,11))
vpwrTrapSystemRedundancyAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapSystemRedundancyAlarm.setStatus(_A)
vpwrTrapIShareAlarm=NotificationType((1,3,6,1,4,1,13858,10,12))
vpwrTrapIShareAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapIShareAlarm.setStatus(_A)
vpwrTrapModuleFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,13))
vpwrTrapModuleFailAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapModuleFailAlarm.setStatus(_A)
vpwrTrapMultipleModuleFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,14))
vpwrTrapMultipleModuleFailAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapMultipleModuleFailAlarm.setStatus(_A)
vpwrTrapModuleCommAlarm=NotificationType((1,3,6,1,4,1,13858,10,15))
vpwrTrapModuleCommAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapModuleCommAlarm.setStatus(_A)
vpwrTrapSystemOverTemperatureAlarm=NotificationType((1,3,6,1,4,1,13858,10,16))
vpwrTrapSystemOverTemperatureAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapSystemOverTemperatureAlarm.setStatus(_A)
vpwrTrapSystemOK=NotificationType((1,3,6,1,4,1,13858,10,17))
vpwrTrapSystemOK.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapSystemOK.setStatus(_A)
vpwrTrapModuleInserted=NotificationType((1,3,6,1,4,1,13858,10,18))
vpwrTrapModuleInserted.setObjects(*((_C,_E),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:vpwrTrapModuleInserted.setStatus(_A)
vpwrTrapModuleRemoved=NotificationType((1,3,6,1,4,1,13858,10,19))
vpwrTrapModuleRemoved.setObjects(*((_C,_E),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:vpwrTrapModuleRemoved.setStatus(_A)
vpwrTrapThermalCompActive=NotificationType((1,3,6,1,4,1,13858,10,20))
vpwrTrapThermalCompActive.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapThermalCompActive.setStatus(_A)
vpwrTrapThermalCompInactive=NotificationType((1,3,6,1,4,1,13858,10,21))
vpwrTrapThermalCompInactive.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapThermalCompInactive.setStatus(_A)
vpwrTrapInternalTempAlarmSet=NotificationType((1,3,6,1,4,1,13858,10,22))
vpwrTrapInternalTempAlarmSet.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapInternalTempAlarmSet.setStatus(_A)
vpwrTrapInternalTempAlarmCleared=NotificationType((1,3,6,1,4,1,13858,10,23))
vpwrTrapInternalTempAlarmCleared.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapInternalTempAlarmCleared.setStatus(_A)
vpwrTrapBatteryTempAlarmSet=NotificationType((1,3,6,1,4,1,13858,10,24))
vpwrTrapBatteryTempAlarmSet.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapBatteryTempAlarmSet.setStatus(_A)
vpwrTrapBatteryTempAlarmCleared=NotificationType((1,3,6,1,4,1,13858,10,25))
vpwrTrapBatteryTempAlarmCleared.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapBatteryTempAlarmCleared.setStatus(_A)
vpwrTrapLoginFail=NotificationType((1,3,6,1,4,1,13858,10,26))
vpwrTrapLoginFail.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapLoginFail.setStatus(_A)
vpwrTrapLoginSuccess=NotificationType((1,3,6,1,4,1,13858,10,27))
vpwrTrapLoginSuccess.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapLoginSuccess.setStatus(_A)
vpwrTrapLogout=NotificationType((1,3,6,1,4,1,13858,10,28))
vpwrTrapLogout.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapLogout.setStatus(_A)
vpwrTrapAdminPwdChange=NotificationType((1,3,6,1,4,1,13858,10,29))
vpwrTrapAdminPwdChange.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapAdminPwdChange.setStatus(_A)
vpwrTrapIllegalConfigSubmit=NotificationType((1,3,6,1,4,1,13858,10,30))
vpwrTrapIllegalConfigSubmit.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapIllegalConfigSubmit.setStatus(_A)
vpwrTrapCfgChange=NotificationType((1,3,6,1,4,1,13858,10,31))
vpwrTrapCfgChange.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapCfgChange.setStatus(_A)
vpwrTrapClearEventHistory=NotificationType((1,3,6,1,4,1,13858,10,32))
vpwrTrapClearEventHistory.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapClearEventHistory.setStatus(_A)
vpwrTrapSwDownloadNoReboot=NotificationType((1,3,6,1,4,1,13858,10,33))
vpwrTrapSwDownloadNoReboot.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapSwDownloadNoReboot.setStatus(_A)
vpwrTrapSwDownloadAndReboot=NotificationType((1,3,6,1,4,1,13858,10,34))
vpwrTrapSwDownloadAndReboot.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapSwDownloadAndReboot.setStatus(_A)
vpwrTrapSystemClockChange=NotificationType((1,3,6,1,4,1,13858,10,35))
vpwrTrapSystemClockChange.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapSystemClockChange.setStatus(_A)
vpwrTrapModuleAlarm=NotificationType((1,3,6,1,4,1,13858,10,36))
vpwrTrapModuleAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapModuleAlarm.setStatus(_A)
vpwrTrapOIDChange=NotificationType((1,3,6,1,4,1,13858,10,37))
vpwrTrapOIDChange.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapOIDChange.setStatus(_A)
vpwrTrapThermalRunaway=NotificationType((1,3,6,1,4,1,13858,10,38))
vpwrTrapThermalRunaway.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapThermalRunaway.setStatus(_A)
vpwrTrapBatteryDischargeTestAlarm=NotificationType((1,3,6,1,4,1,13858,10,39))
vpwrTrapBatteryDischargeTestAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapBatteryDischargeTestAlarm.setStatus(_A)
vpwrTrapBayUnnameAlarm=NotificationType((1,3,6,1,4,1,13858,10,40))
vpwrTrapBayUnnameAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapBayUnnameAlarm.setStatus(_A)
vpwrTrapPMComFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,41))
vpwrTrapPMComFailAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapPMComFailAlarm.setStatus(_A)
vpwrTrapFuseOverloadAlarm=NotificationType((1,3,6,1,4,1,13858,10,42))
vpwrTrapFuseOverloadAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapFuseOverloadAlarm.setStatus(_A)
vpwrTrapPeripheralAlarm=NotificationType((1,3,6,1,4,1,13858,10,43))
vpwrTrapPeripheralAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapPeripheralAlarm.setStatus(_A)
vpwrTrapThermalProbeAlarm=NotificationType((1,3,6,1,4,1,13858,10,44))
vpwrTrapThermalProbeAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapThermalProbeAlarm.setStatus(_A)
vpwrTrapBayCommAlarm=NotificationType((1,3,6,1,4,1,13858,10,45))
vpwrTrapBayCommAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapBayCommAlarm.setStatus(_A)
vpwrTrapDistributionCommAlarm=NotificationType((1,3,6,1,4,1,13858,10,46))
vpwrTrapDistributionCommAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapDistributionCommAlarm.setStatus(_A)
vpwrTrapConverterAlarm=NotificationType((1,3,6,1,4,1,13858,10,47))
vpwrTrapConverterAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapConverterAlarm.setStatus(_A)
vpwrTrapMultipleConvFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,48))
vpwrTrapMultipleConvFailAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapMultipleConvFailAlarm.setStatus(_A)
vpwrTrapDGUAlarm=NotificationType((1,3,6,1,4,1,13858,10,49))
vpwrTrapDGUAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapDGUAlarm.setStatus(_A)
vpwrTrapConfigErrorAlarm=NotificationType((1,3,6,1,4,1,13858,10,50))
vpwrTrapConfigErrorAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapConfigErrorAlarm.setStatus(_A)
vpwrTrapDisplayFirmwareMismatchAlarm=NotificationType((1,3,6,1,4,1,13858,10,51))
vpwrTrapDisplayFirmwareMismatchAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapDisplayFirmwareMismatchAlarm.setStatus(_A)
vpwrTrapConverterInputFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,52))
vpwrTrapConverterInputFailAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapConverterInputFailAlarm.setStatus(_A)
vpwrTrapBatteryRechgIlimitFailAlarm=NotificationType((1,3,6,1,4,1,13858,10,53))
vpwrTrapBatteryRechgIlimitFailAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapBatteryRechgIlimitFailAlarm.setStatus(_A)
vpwrTrapSystemAlive=NotificationType((1,3,6,1,4,1,13858,10,54))
vpwrTrapSystemAlive.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapSystemAlive.setStatus(_A)
vpwrTrapSystemAuxAlmSource=NotificationType((1,3,6,1,4,1,13858,10,55))
vpwrTrapSystemAuxAlmSource.setObjects(*((_C,_E),(_C,_T),(_C,_U),(_C,_V)))
if mibBuilder.loadTexts:vpwrTrapSystemAuxAlmSource.setStatus(_A)
vpwrTrapSystemDistAlmSource=NotificationType((1,3,6,1,4,1,13858,10,56))
vpwrTrapSystemDistAlmSource.setObjects(*((_C,_E),(_C,_T),(_C,_U),(_C,_V)))
if mibBuilder.loadTexts:vpwrTrapSystemDistAlmSource.setStatus(_A)
vpwrTrapSystemBatCapacityAlarm=NotificationType((1,3,6,1,4,1,13858,10,58))
vpwrTrapSystemBatCapacityAlarm.setObjects(*((_C,_E),(_C,_A9),(_C,_AA)))
if mibBuilder.loadTexts:vpwrTrapSystemBatCapacityAlarm.setStatus(_A)
vpwrTrapSystemACFClearAlarm=NotificationType((1,3,6,1,4,1,13858,10,61))
vpwrTrapSystemACFClearAlarm.setObjects(*((_C,_E),(_C,_W)))
if mibBuilder.loadTexts:vpwrTrapSystemACFClearAlarm.setStatus(_A)
vpwrTrapSystemACFSetAlarm=NotificationType((1,3,6,1,4,1,13858,10,62))
vpwrTrapSystemACFSetAlarm.setObjects(*((_C,_E),(_C,_W)))
if mibBuilder.loadTexts:vpwrTrapSystemACFSetAlarm.setStatus(_A)
vpwrTrapSystemBatCapacityLeft=NotificationType((1,3,6,1,4,1,13858,10,64))
vpwrTrapSystemBatCapacityLeft.setObjects(*((_C,_E),(_C,_AB)))
if mibBuilder.loadTexts:vpwrTrapSystemBatCapacityLeft.setStatus(_A)
vpwrTrapRectifierUVAlarm=NotificationType((1,3,6,1,4,1,13858,10,65))
vpwrTrapRectifierUVAlarm.setObjects(*((_C,_E),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:vpwrTrapRectifierUVAlarm.setStatus(_A)
vpwrTrapMultRectifierUVAlarm=NotificationType((1,3,6,1,4,1,13858,10,66))
vpwrTrapMultRectifierUVAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapMultRectifierUVAlarm.setStatus(_A)
vpwrTrapRingerAlarm=NotificationType((1,3,6,1,4,1,13858,10,67))
vpwrTrapRingerAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapRingerAlarm.setStatus(_A)
vpwrTrapMultRingerAlarm=NotificationType((1,3,6,1,4,1,13858,10,68))
vpwrTrapMultRingerAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapMultRingerAlarm.setStatus(_A)
vpwrTrapI2CCANAlarm=NotificationType((1,3,6,1,4,1,13858,10,69))
vpwrTrapI2CCANAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapI2CCANAlarm.setStatus(_A)
vpwrTrapRectifierIlimitAlarm=NotificationType((1,3,6,1,4,1,13858,10,70))
vpwrTrapRectifierIlimitAlarm.setObjects(*((_C,_E),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:vpwrTrapRectifierIlimitAlarm.setStatus(_A)
vpwrTrapMultRectifierIlimitAlarm=NotificationType((1,3,6,1,4,1,13858,10,71))
vpwrTrapMultRectifierIlimitAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapMultRectifierIlimitAlarm.setStatus(_A)
vpwrTrapRingerCommAlarm=NotificationType((1,3,6,1,4,1,13858,10,72))
vpwrTrapRingerCommAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapRingerCommAlarm.setStatus(_A)
vpwrTrapUnassignedAlarm=NotificationType((1,3,6,1,4,1,13858,10,99))
vpwrTrapUnassignedAlarm.setObjects((_C,_E))
if mibBuilder.loadTexts:vpwrTrapUnassignedAlarm.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PositiveInteger':PositiveInteger,'NonNegativeInteger':NonNegativeInteger,'GenericEnableDisableTC':GenericEnableDisableTC,'SysInputValue':SysInputValue,'VpwrPMCnfgValue':VpwrPMCnfgValue,'BDTStartSourceTC':BDTStartSourceTC,'BDTResultTC':BDTResultTC,'eltek':eltek,'vpwrDcPowerSystem':vpwrDcPowerSystem,'vpwrSystemIdentGroup':vpwrSystemIdentGroup,'vpwrIdentManufacturer':vpwrIdentManufacturer,'vpwrIdentModel':vpwrIdentModel,'vpwrIdentControllerVersion':vpwrIdentControllerVersion,'vpwrIdentAgentSoftwareVersion':vpwrIdentAgentSoftwareVersion,'vpwrIdentName':vpwrIdentName,'vpwrSystemIdentTable':vpwrSystemIdentTable,'vpwrSystemIdentEntry':vpwrSystemIdentEntry,_K:vpwrShelfIndex,_L:vpwrModuleIndex,'vpwrModuleOID':vpwrModuleOID,'vpwrModuleCurrent':vpwrModuleCurrent,'vpwrModuleOperStatus':vpwrModuleOperStatus,'vpwrModuleCapacity':vpwrModuleCapacity,'vpwrSystemConfigGroup':vpwrSystemConfigGroup,'vpwrSystemTempCompensation':vpwrSystemTempCompensation,'vpwrSystemTempCompStartTemperature':vpwrSystemTempCompStartTemperature,'vpwrSystemTempCompStopVoltage':vpwrSystemTempCompStopVoltage,'vpwrSystemTempCompensationSlope':vpwrSystemTempCompensationSlope,'vpwrSystemThermalSenseType':vpwrSystemThermalSenseType,'vpwrSystemHVAlarmSetpoint':vpwrSystemHVAlarmSetpoint,'vpwrSystemBDAlarmSetpoint':vpwrSystemBDAlarmSetpoint,'vpwrSystemInternalTempLThreshold':vpwrSystemInternalTempLThreshold,'vpwrSystemInternalTempUThreshold':vpwrSystemInternalTempUThreshold,'vpwrSystemParameterGroup':vpwrSystemParameterGroup,'vpwrSystemShelfCapacity':vpwrSystemShelfCapacity,'vpwrSystemVoltage':vpwrSystemVoltage,_A9:vpwrSystemCurrent,'vpwrSystemControllerState':vpwrSystemControllerState,'vpwrSystemInternalTemperature':vpwrSystemInternalTemperature,'vpwrSystemTempCompensationState':vpwrSystemTempCompensationState,'vpwrSystemType':vpwrSystemType,'vpwrSystemCumulativeUpTime':vpwrSystemCumulativeUpTime,'vpwrSystemBatteryRemainingTime':vpwrSystemBatteryRemainingTime,'vpwrSystemPanelIdentGroup':vpwrSystemPanelIdentGroup,'vpwrPanelStatusTable':vpwrPanelStatusTable,'vpwrPanelStatus':vpwrPanelStatus,_p:vpwrPanelStatusIndex,_q:vpwrPanelStatusModuleIndex,'vpwrPanelStatusModuleOID':vpwrPanelStatusModuleOID,'vpwrPanelStatusModuleCurrent':vpwrPanelStatusModuleCurrent,'vpwrpanelStatusModuleOperStatus':vpwrpanelStatusModuleOperStatus,'vpwrPanelStatusModuleCapacity':vpwrPanelStatusModuleCapacity,'vpwrPanelIdentTable':vpwrPanelIdentTable,'vpwrPanelIdentEntry':vpwrPanelIdentEntry,_r:vpwrPanelIndex,_s:vpwrPanelModuleIndex,'vpwrPanelModuleSerNum':vpwrPanelModuleSerNum,'vpwrPanelModuleModelName':vpwrPanelModuleModelName,'vpwrPanelModuleFWVer':vpwrPanelModuleFWVer,'vpwrPanelModuleTestDate':vpwrPanelModuleTestDate,'vpwrSystemHistoryGroup':vpwrSystemHistoryGroup,'vpwrSysHistAlarmTable':vpwrSysHistAlarmTable,'vpwrSysHistAlarmEntry':vpwrSysHistAlarmEntry,_t:vpwrSysHistAlarmIndex,'vpwrSysHistAlarmDescription':vpwrSysHistAlarmDescription,'vpwrSystemAlarmGroup':vpwrSystemAlarmGroup,'vpwrSystemAlarmMajor':vpwrSystemAlarmMajor,'vpwrSystemAlarmMinor':vpwrSystemAlarmMinor,'vpwrSystemACFailAlarm':vpwrSystemACFailAlarm,'vpwrSystemHighVoltageWarningAlarm':vpwrSystemHighVoltageWarningAlarm,'vpwrSystemHighVoltageShutdownAlarm':vpwrSystemHighVoltageShutdownAlarm,'vpwrSystemBatteryonDischargeAlarm':vpwrSystemBatteryonDischargeAlarm,'vpwrSystemLowVoltageWarningAlarm':vpwrSystemLowVoltageWarningAlarm,'vpwrSystemLVDOpenAlarm':vpwrSystemLVDOpenAlarm,'vpwrSystemDistributionAlarm':vpwrSystemDistributionAlarm,'vpwrSystemAuxiliaryAlarm':vpwrSystemAuxiliaryAlarm,'vpwrSystemRedundantCapAlarm':vpwrSystemRedundantCapAlarm,'vpwrSystemRectIShareAlarm':vpwrSystemRectIShareAlarm,'vpwrSystemSnglRectAlarm':vpwrSystemSnglRectAlarm,'vpwrSystemMultRectAlarm':vpwrSystemMultRectAlarm,'vpwrSystemModlCommAlarm':vpwrSystemModlCommAlarm,'vpwrSystemOverTempAlarm':vpwrSystemOverTempAlarm,'vpwrSystemThermRAAlarm':vpwrSystemThermRAAlarm,'vpwrSystemBDTAlarm':vpwrSystemBDTAlarm,'vpwrSystemRectUVAlarm':vpwrSystemRectUVAlarm,'vpwrSystemMultRectUVAlarm':vpwrSystemMultRectUVAlarm,'vpwrSystemSnglRngrAlarm':vpwrSystemSnglRngrAlarm,'vpwrSystemMultRngrAlarm':vpwrSystemMultRngrAlarm,'vpwrSystemTempProbeAlarm':vpwrSystemTempProbeAlarm,'vpwrSystemRngrCommAlarm':vpwrSystemRngrCommAlarm,'vpwrSystemDistPMCommAlarm':vpwrSystemDistPMCommAlarm,'vpwrSystemRectILimitAlarm':vpwrSystemRectILimitAlarm,'vpwrSystemMultRectILimitAlarm':vpwrSystemMultRectILimitAlarm,'vpwrSystemUnmappedI2CCANAlarm':vpwrSystemUnmappedI2CCANAlarm,'vpwrSystemConfigErrAlarm':vpwrSystemConfigErrAlarm,'vpwrSystemDispFWAlarm':vpwrSystemDispFWAlarm,'vpwrSystemUndefinedAlarm':vpwrSystemUndefinedAlarm,'vpwrDcPowerRectifier':vpwrDcPowerRectifier,'vpwrRectifierConfigGroup':vpwrRectifierConfigGroup,'vpwrRectifierFVSetpoint':vpwrRectifierFVSetpoint,'vpwrRectifierHVSDSetpoint':vpwrRectifierHVSDSetpoint,'vpwrRectifierCurrentLimitAdminState':vpwrRectifierCurrentLimitAdminState,'vpwrRectifierCurrentLimit':vpwrRectifierCurrentLimit,'vpwrRectifierFallbackAdminState':vpwrRectifierFallbackAdminState,'vpwrRectifierFallbackVoltage':vpwrRectifierFallbackVoltage,'vpwrRectifierAlarmGroup':vpwrRectifierAlarmGroup,'vpwrRectAlarmDCFail':vpwrRectAlarmDCFail,'vpwrRectAlarmBoostFail':vpwrRectAlarmBoostFail,'vpwrRectAlarmACFail':vpwrRectAlarmACFail,'vpwrRectAlarmHVSD':vpwrRectAlarmHVSD,'vpwrRectAlarmFanFail':vpwrRectAlarmFanFail,'vpwrRectAlarmAmbTemp':vpwrRectAlarmAmbTemp,'vpwrRectAlarmIntTemp':vpwrRectAlarmIntTemp,'vpwrRectAlarmIShare':vpwrRectAlarmIShare,'vpwrRectAlarmUV':vpwrRectAlarmUV,'vpwrRectAlarmLowVoltage':vpwrRectAlarmLowVoltage,'vpwrRectAlarmReserved':vpwrRectAlarmReserved,'vpwrRectAlarmDCEnable':vpwrRectAlarmDCEnable,'vpwrRectAlarmRemoteShutdown':vpwrRectAlarmRemoteShutdown,'vpwrRectAlarmModDisableShutdown':vpwrRectAlarmModDisableShutdown,'vpwrRectAlarmShortPinShutdown':vpwrRectAlarmShortPinShutdown,'vpwrRectAlarmBoostComm':vpwrRectAlarmBoostComm,'vpwrDcPowerLvd':vpwrDcPowerLvd,'vpwrLvdConfigGroup':vpwrLvdConfigGroup,'vpwrLvdWarningSetpoint':vpwrLvdWarningSetpoint,'vpwrLvdDisconnectSetpoint':vpwrLvdDisconnectSetpoint,'vpwrLvdReconnectSetpoint':vpwrLvdReconnectSetpoint,'vpwrLvdReconnectDelayTimer':vpwrLvdReconnectDelayTimer,'vpwrLvd2DisconnectSetpoint':vpwrLvd2DisconnectSetpoint,'vpwrLvd2ReconnectSetpoint':vpwrLvd2ReconnectSetpoint,'vpwrLvd2ReconnectDelayTimer':vpwrLvd2ReconnectDelayTimer,'vpwrLvd3DisconnectSetpoint':vpwrLvd3DisconnectSetpoint,'vpwrLvd3ReconnectSetpoint':vpwrLvd3ReconnectSetpoint,'vpwrLvd3ReconnectDelayTimer':vpwrLvd3ReconnectDelayTimer,'vpwrLvd4DisconnectSetpoint':vpwrLvd4DisconnectSetpoint,'vpwrLvd4ReconnectSetpoint':vpwrLvd4ReconnectSetpoint,'vpwrLvd4ReconnectDelayTimer':vpwrLvd4ReconnectDelayTimer,'vpwrDCPowerLampTest':vpwrDCPowerLampTest,'vpwrDcPowerModuleIdent':vpwrDcPowerModuleIdent,'vpwrDcPowerModuleIdentTable':vpwrDcPowerModuleIdentTable,'vpwrDcPowerModuleIdentEntry':vpwrDcPowerModuleIdentEntry,_u:vpwrShelfIndex1,_v:vpwrDCModuleIndex,'vpwrModuleSerialNumber':vpwrModuleSerialNumber,'vpwrModuleModelNumber':vpwrModuleModelNumber,'vpwrModuleFwVersion':vpwrModuleFwVersion,'vpwrModuleTestDate':vpwrModuleTestDate,'vpwrModuleOperHours':vpwrModuleOperHours,'vpwrDcPowerBatteryGroup':vpwrDcPowerBatteryGroup,'vpwrBatteryTempGroup':vpwrBatteryTempGroup,'vpwrBatteryTempTable':vpwrBatteryTempTable,'vpwrBatteryTempEntry':vpwrBatteryTempEntry,_w:vpwrBatteryTempIndex,'vpwrBatteryTempName':vpwrBatteryTempName,'vpwrBatteryTemp':vpwrBatteryTemp,'vpwrBatteryTempLThreshold':vpwrBatteryTempLThreshold,'vpwrBatteryTempUThreshold':vpwrBatteryTempUThreshold,'batteryTempCompensation':batteryTempCompensation,'batteryTempCompHighStartTemperature':batteryTempCompHighStartTemperature,'batteryTempCompHighStopVoltage':batteryTempCompHighStopVoltage,'batteryTempCompHighSlope':batteryTempCompHighSlope,'batteryTempCompLowStartTemperature':batteryTempCompLowStartTemperature,'batteryTempCompLowStopVoltage':batteryTempCompLowStopVoltage,'batteryTempCompLowSlope':batteryTempCompLowSlope,'batteryTempCompRunawayTemperature':batteryTempCompRunawayTemperature,'batteryTempCompRunawayStopVoltage':batteryTempCompRunawayStopVoltage,'batteryTempCompSenseSource':batteryTempCompSenseSource,'batteryTempCompRunawayState':batteryTempCompRunawayState,'vpwrBatteryCurrentGroup':vpwrBatteryCurrentGroup,'vpwrBatteryCurrentLimitAdminState':vpwrBatteryCurrentLimitAdminState,'vpwrBatteryCurrentLimit':vpwrBatteryCurrentLimit,'vpwrBatteryCurrent':vpwrBatteryCurrent,'vpwrBatteryBoostGroup':vpwrBatteryBoostGroup,'vpwrBoostAdminState':vpwrBoostAdminState,'vpwrBoostVoltage':vpwrBoostVoltage,'vpwrBoostDuration':vpwrBoostDuration,'vpwrBoostOperState':vpwrBoostOperState,'vpwrBatteryDischargeTestGroup':vpwrBatteryDischargeTestGroup,'vpwrBDTAdminState':vpwrBDTAdminState,'vpwrBDTDuration':vpwrBDTDuration,'vpwrBDTAlarmVoltage':vpwrBDTAlarmVoltage,'vpwrBDTAbortVoltage':vpwrBDTAbortVoltage,'vpwrBDTAlarmCoefficient':vpwrBDTAlarmCoefficient,'vpwrBDTOperState':vpwrBDTOperState,'vpwrBDTClearAlarm':vpwrBDTClearAlarm,'vpwrBDTActualTime':vpwrBDTActualTime,'vpwrBDTAlarmDelay':vpwrBDTAlarmDelay,'vpwrBDTResult':vpwrBDTResult,'vpwrBDTAutoAdminState':vpwrBDTAutoAdminState,'vpwrBDTHistTable':vpwrBDTHistTable,'vpwrBDTHistEntry':vpwrBDTHistEntry,_A0:vpwrBDTHistIndex,'vpwrBDTHistDateTime':vpwrBDTHistDateTime,'vpwrBDTHistDuration':vpwrBDTHistDuration,'vpwrBDTHistAlarmVoltage':vpwrBDTHistAlarmVoltage,'vpwrBDTHistAbortVoltage':vpwrBDTHistAbortVoltage,'vpwrBDTHistStartMethod':vpwrBDTHistStartMethod,'vpwrBDTHistResult':vpwrBDTHistResult,'vpwrBDTHistActualTime':vpwrBDTHistActualTime,'vpwrBDTHistStartVoltage':vpwrBDTHistStartVoltage,'vpwrBDTHistEndVoltage':vpwrBDTHistEndVoltage,'vpwrBDTSchedTable':vpwrBDTSchedTable,'vpwrBDTSchedEntry':vpwrBDTSchedEntry,_A1:vpwrBDTSchedIndex,'vpwrBDTSchedDay':vpwrBDTSchedDay,'vpwrBDTSchedMonth':vpwrBDTSchedMonth,'vpwrBDTSchedHour':vpwrBDTSchedHour,'vpwrBDTSchedMinute':vpwrBDTSchedMinute,'vpwrDcPowerAlarmGroup':vpwrDcPowerAlarmGroup,'vpwrAlarmsPresent':vpwrAlarmsPresent,'vpwrAlarmTable':vpwrAlarmTable,'vpwrAlarmEntry':vpwrAlarmEntry,_A2:vpwrAlarmIndex,'vpwrAlarmDescr':vpwrAlarmDescr,'vpwrAlarmTime':vpwrAlarmTime,'sysAlarmConfigTable':sysAlarmConfigTable,'sysAlarmConfigEntry':sysAlarmConfigEntry,_A3:sysAlarmIndex,'sysAlarmDefaultName':sysAlarmDefaultName,'sysAlarmCustomName':sysAlarmCustomName,'sysAlarmSeverity':sysAlarmSeverity,'sysAlarmToRelayMapping':sysAlarmToRelayMapping,'sysAlarmOperStatus':sysAlarmOperStatus,'sysAlarmComFailState':sysAlarmComFailState,'sysAlarmIShareState':sysAlarmIShareState,'sysAlarmRedundancyState':sysAlarmRedundancyState,'sysAlarmComFailToACFailState':sysAlarmComFailToACFailState,'vpwrDcPowerSnmpConfig':vpwrDcPowerSnmpConfig,'vpwrTrapTable':vpwrTrapTable,'vpwrTrapEntry':vpwrTrapEntry,_A4:vpwrTrapIpIndex,'vpwrTrapIpAddress':vpwrTrapIpAddress,'vpwrTrapCriticality':vpwrTrapCriticality,'vpwrReadCommunityString':vpwrReadCommunityString,'vpwrWriteCommunityString':vpwrWriteCommunityString,'vpwrTrapCommunityString':vpwrTrapCommunityString,'vpwrTrapVersion':vpwrTrapVersion,'vpwrDcPowerTraps':vpwrDcPowerTraps,'vpwrTrapPowerMajorAlarm':vpwrTrapPowerMajorAlarm,'vpwrTrapPowerMinorAlarm':vpwrTrapPowerMinorAlarm,'vpwrTrapACFAlarm':vpwrTrapACFAlarm,'vpwrTrapHVAlarm':vpwrTrapHVAlarm,'vpwrTrapHVSDAlarm':vpwrTrapHVSDAlarm,'vpwrTrapBDAlarm':vpwrTrapBDAlarm,'vpwrTrapLVDWarningAlarm':vpwrTrapLVDWarningAlarm,'vpwrTrapLVDOpenAlarm':vpwrTrapLVDOpenAlarm,'vpwrTrapDistAlarm':vpwrTrapDistAlarm,'vpwrTrapAuxAlarm':vpwrTrapAuxAlarm,'vpwrTrapSystemRedundancyAlarm':vpwrTrapSystemRedundancyAlarm,'vpwrTrapIShareAlarm':vpwrTrapIShareAlarm,'vpwrTrapModuleFailAlarm':vpwrTrapModuleFailAlarm,'vpwrTrapMultipleModuleFailAlarm':vpwrTrapMultipleModuleFailAlarm,'vpwrTrapModuleCommAlarm':vpwrTrapModuleCommAlarm,'vpwrTrapSystemOverTemperatureAlarm':vpwrTrapSystemOverTemperatureAlarm,'vpwrTrapSystemOK':vpwrTrapSystemOK,'vpwrTrapModuleInserted':vpwrTrapModuleInserted,'vpwrTrapModuleRemoved':vpwrTrapModuleRemoved,'vpwrTrapThermalCompActive':vpwrTrapThermalCompActive,'vpwrTrapThermalCompInactive':vpwrTrapThermalCompInactive,'vpwrTrapInternalTempAlarmSet':vpwrTrapInternalTempAlarmSet,'vpwrTrapInternalTempAlarmCleared':vpwrTrapInternalTempAlarmCleared,'vpwrTrapBatteryTempAlarmSet':vpwrTrapBatteryTempAlarmSet,'vpwrTrapBatteryTempAlarmCleared':vpwrTrapBatteryTempAlarmCleared,'vpwrTrapLoginFail':vpwrTrapLoginFail,'vpwrTrapLoginSuccess':vpwrTrapLoginSuccess,'vpwrTrapLogout':vpwrTrapLogout,'vpwrTrapAdminPwdChange':vpwrTrapAdminPwdChange,'vpwrTrapIllegalConfigSubmit':vpwrTrapIllegalConfigSubmit,'vpwrTrapCfgChange':vpwrTrapCfgChange,'vpwrTrapClearEventHistory':vpwrTrapClearEventHistory,'vpwrTrapSwDownloadNoReboot':vpwrTrapSwDownloadNoReboot,'vpwrTrapSwDownloadAndReboot':vpwrTrapSwDownloadAndReboot,'vpwrTrapSystemClockChange':vpwrTrapSystemClockChange,'vpwrTrapModuleAlarm':vpwrTrapModuleAlarm,'vpwrTrapOIDChange':vpwrTrapOIDChange,'vpwrTrapThermalRunaway':vpwrTrapThermalRunaway,'vpwrTrapBatteryDischargeTestAlarm':vpwrTrapBatteryDischargeTestAlarm,'vpwrTrapBayUnnameAlarm':vpwrTrapBayUnnameAlarm,'vpwrTrapPMComFailAlarm':vpwrTrapPMComFailAlarm,'vpwrTrapFuseOverloadAlarm':vpwrTrapFuseOverloadAlarm,'vpwrTrapPeripheralAlarm':vpwrTrapPeripheralAlarm,'vpwrTrapThermalProbeAlarm':vpwrTrapThermalProbeAlarm,'vpwrTrapBayCommAlarm':vpwrTrapBayCommAlarm,'vpwrTrapDistributionCommAlarm':vpwrTrapDistributionCommAlarm,'vpwrTrapConverterAlarm':vpwrTrapConverterAlarm,'vpwrTrapMultipleConvFailAlarm':vpwrTrapMultipleConvFailAlarm,'vpwrTrapDGUAlarm':vpwrTrapDGUAlarm,'vpwrTrapConfigErrorAlarm':vpwrTrapConfigErrorAlarm,'vpwrTrapDisplayFirmwareMismatchAlarm':vpwrTrapDisplayFirmwareMismatchAlarm,'vpwrTrapConverterInputFailAlarm':vpwrTrapConverterInputFailAlarm,'vpwrTrapBatteryRechgIlimitFailAlarm':vpwrTrapBatteryRechgIlimitFailAlarm,'vpwrTrapSystemAlive':vpwrTrapSystemAlive,'vpwrTrapSystemAuxAlmSource':vpwrTrapSystemAuxAlmSource,'vpwrTrapSystemDistAlmSource':vpwrTrapSystemDistAlmSource,'vpwrTrapSystemBatCapacityAlarm':vpwrTrapSystemBatCapacityAlarm,'vpwrTrapSystemACFClearAlarm':vpwrTrapSystemACFClearAlarm,'vpwrTrapSystemACFSetAlarm':vpwrTrapSystemACFSetAlarm,'vpwrTrapSystemBatCapacityLeft':vpwrTrapSystemBatCapacityLeft,'vpwrTrapRectifierUVAlarm':vpwrTrapRectifierUVAlarm,'vpwrTrapMultRectifierUVAlarm':vpwrTrapMultRectifierUVAlarm,'vpwrTrapRingerAlarm':vpwrTrapRingerAlarm,'vpwrTrapMultRingerAlarm':vpwrTrapMultRingerAlarm,'vpwrTrapI2CCANAlarm':vpwrTrapI2CCANAlarm,'vpwrTrapRectifierIlimitAlarm':vpwrTrapRectifierIlimitAlarm,'vpwrTrapMultRectifierIlimitAlarm':vpwrTrapMultRectifierIlimitAlarm,'vpwrTrapRingerCommAlarm':vpwrTrapRingerCommAlarm,'vpwrTrapUnassignedAlarm':vpwrTrapUnassignedAlarm,'vpwrDcPowerTrapVars':vpwrDcPowerTrapVars,_E:vpwrTrapsMsgString,'vpwrTrapUserIpAddress':vpwrTrapUserIpAddress,_W:vpwrTrapAcfDuration,_V:vpwrAlarmingSubModuleBitMap,_AA:vpwrBatteryCurrentCapacity,_U:vpwrAlarmingModuleIndex,_T:vpwrAlarmingModuleOID,'vpwrAlarmingModuleBitMap':vpwrAlarmingModuleBitMap,_AB:vpwrBatteryRemainingTime,'vpwrDcPowerRinger':vpwrDcPowerRinger,'vpwrRingerConfigGroup':vpwrRingerConfigGroup,'vpwrRingerIndex':vpwrRingerIndex,'vpwrRingerParameterAdminState':vpwrRingerParameterAdminState,'vpwrRingerParameterAcVoltage':vpwrRingerParameterAcVoltage,'vpwrRingerParameterDcVoltage':vpwrRingerParameterDcVoltage,'vpwrRingerParameterFrequency':vpwrRingerParameterFrequency,'vpwrRingerNumberPresent':vpwrRingerNumberPresent,'vpwrRingerAlarmGroup':vpwrRingerAlarmGroup,'vpwrRingerAlarmAFailed':vpwrRingerAlarmAFailed,'vpwrRingerAlarmAOverTemp':vpwrRingerAlarmAOverTemp,'vpwrRingerAlarmAOverCurrent':vpwrRingerAlarmAOverCurrent,'vpwrRingerAlarmBFailed':vpwrRingerAlarmBFailed,'vpwrRingerAlarmBOverTemp':vpwrRingerAlarmBOverTemp,'vpwrRingerAlarmBOverCurrent':vpwrRingerAlarmBOverCurrent,'vpwrRingerTestGroup':vpwrRingerTestGroup,'vpwrDcPowerDcDcConverter':vpwrDcPowerDcDcConverter,'vpwrDcDcConverterConfigGroup':vpwrDcDcConverterConfigGroup,'vpwrDcDcConverterAlarmGroup':vpwrDcDcConverterAlarmGroup,'vpwrDcDcConverterTestGroup':vpwrDcDcConverterTestGroup,'vpwrDcPowerDcAcInverter':vpwrDcPowerDcAcInverter,'vpwrDcAcInverterConfigGroup':vpwrDcAcInverterConfigGroup,'vpwrDcAcInverterAlarmGroup':vpwrDcAcInverterAlarmGroup,'vpwrDcAcInverterTestGroup':vpwrDcAcInverterTestGroup,'vpwrDcPowerAcLineModule':vpwrDcPowerAcLineModule,'vpwrAcLineModuleConfigGroup':vpwrAcLineModuleConfigGroup,'vpwrAcLineModuleAlarmGroup':vpwrAcLineModuleAlarmGroup,'vpwrAcLineModuleTestGroup':vpwrAcLineModuleTestGroup,'vpwrDcPowerIoModule':vpwrDcPowerIoModule,'vpwrIoModuleConfigGroup':vpwrIoModuleConfigGroup,'vpwrIoModuleAlarmGroup':vpwrIoModuleAlarmGroup,'vpwrIoModuleTestGroup':vpwrIoModuleTestGroup,'vpwrDcPowerPMModule':vpwrDcPowerPMModule,'vpwrPMCnfgTable':vpwrPMCnfgTable,'vpwrPMCnfgEntry':vpwrPMCnfgEntry,_A6:vpwrPMIndex,'vpwrPMDescription':vpwrPMDescription,'vpwrPMCnfg1':vpwrPMCnfg1,'vpwrPMCnfg2':vpwrPMCnfg2,'vpwrPMCnfg3':vpwrPMCnfg3,'vpwrPMCnfg4':vpwrPMCnfg4,'vpwrPMCnfg5':vpwrPMCnfg5,'vpwrPMCnfg6':vpwrPMCnfg6,'vpwrPMCnfg7':vpwrPMCnfg7,'vpwrPMCnfg8':vpwrPMCnfg8,'vpwrPMInputStatusTable':vpwrPMInputStatusTable,'vpwrPMInputStatusEntry':vpwrPMInputStatusEntry,_A7:vpwrPMIndex1,'vpwrPMDescription1':vpwrPMDescription1,'vpwrPMInput1State':vpwrPMInput1State,'vpwrPMInput2State':vpwrPMInput2State,'vpwrPMInput3State':vpwrPMInput3State,'vpwrPMInput4State':vpwrPMInput4State,'vpwrPMInput5State':vpwrPMInput5State,'vpwrPMInput6State':vpwrPMInput6State,'vpwrPMInput7State':vpwrPMInput7State,'vpwrPMInput8State':vpwrPMInput8State,'vpwrPMRelayCtrlTable':vpwrPMRelayCtrlTable,'vpwrPMRelayCtrlEntry':vpwrPMRelayCtrlEntry,_A8:vpwrPMIndex2,'vpwrPMDescription2':vpwrPMDescription2,'vpwrPMRelay1State':vpwrPMRelay1State,'vpwrPMRelay2State':vpwrPMRelay2State,'vpwrPMRelay3State':vpwrPMRelay3State,'vpwrPMRelay4State':vpwrPMRelay4State,'vpwrPMRelay5State':vpwrPMRelay5State,'vpwrPMRelay6State':vpwrPMRelay6State,'vpwrPMModuleAlarmGroup':vpwrPMModuleAlarmGroup,'vpwrPMModuleTestGroup':vpwrPMModuleTestGroup,'vpwrDcPowerDistModule':vpwrDcPowerDistModule,'vpwrDcPowerBattery':vpwrDcPowerBattery,'vpwrDcPowerController':vpwrDcPowerController,'vpwrDcPowerUnkModule':vpwrDcPowerUnkModule,'thirdPartyProduct':thirdPartyProduct})