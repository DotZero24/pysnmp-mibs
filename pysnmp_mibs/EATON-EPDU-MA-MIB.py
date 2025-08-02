_Ax='trapsGroup'
_Aw='externalHumidityGroup'
_Av='externalTemperatureGroup'
_Au='unitSensorsGroup'
_At='outletsGroup'
_As='infoGroup'
_Ar='outletGroupingConnectivityLost'
_Aq='thresholdAlarm'
_Ap='logFileCleared'
_Ao='securityViolation'
_An='firmwareValidationFailed'
_Am='firmwareFileDiscarded'
_Al='passwordSettingsChanged'
_Ak='userPasswordChanged'
_Aj='powerControl'
_Ai='userBlocked'
_Ah='deviceUpdateStarted'
_Ag='groupDeleted'
_Af='groupModified'
_Ae='groupAdded'
_Ad='userDeleted'
_Ac='userModified'
_Ab='userAdded'
_Aa='userSessionTimeout'
_AZ='userAuthenticationFailure'
_AY='userLogout'
_AX='userLogin'
_AW='rebootCompleted'
_AV='rebootStarted'
_AU='humidityUpperCriticalReset'
_AT='humidityLowerCriticalReset'
_AS='humidityUpperWarningReset'
_AR='humidityLowerWarningReset'
_AQ='humidityUpperCritical'
_AP='humidityLowerCritical'
_AO='humidityUpperWarning'
_AN='humidityLowerWarning'
_AM='humiditySensorLabel'
_AL='humiditySensorCount'
_AK='tempUpperCriticalReset'
_AJ='tempLowerCriticalReset'
_AI='tempUpperWarningReset'
_AH='tempLowerWarningReset'
_AG='tempUpperCritical'
_AF='tempLowerCritical'
_AE='tempUpperWarning'
_AD='tempLowerWarning'
_AC='temperature'
_AB='tempSensorLabel'
_AA='tempSensorCount'
_A9='unitTempUpperCritical'
_A8='unitTempLowerCritical'
_A7='unitTempUpperWarning'
_A6='unitTempLowerWarning'
_A5='unitCurrentUpperCritical'
_A4='unitCurrentUpperWarning'
_A3='unitVoltageUpperCritical'
_A2='unitVoltageLowerCritical'
_A1='unitVoltageUpperWarning'
_A0='unitVoltageLowerWarning'
_z='unitCircuitBreak2Current'
_y='unitCircuitBreak1Current'
_x='unitCircuitBreak0Current'
_w='unitCircuitBreak2State'
_v='unitCircuitBreak1State'
_u='unitCircuitBreak0State'
_t='unitCpuTemp'
_s='unitApparentPower'
_r='unitActivePower'
_q='unitVoltage'
_p='unitCurrent'
_o='outletCurrentUpperCritical'
_n='outletCurrentUpperWarning'
_m='outletPowerFactor'
_l='outletApparentPower'
_k='outletActivePower'
_j='outletVoltage'
_i='outletMaxCurrent'
_h='outletCurrent'
_g='outletCount'
_f='hardwareRev'
_e='gateway'
_d='netmask'
_c='serialNumber'
_b='firmwareVersion'
_a='humiditySensorIndex'
_Z='tempSensorIndex'
_Y='outletIndex'
_X='outletOperationalState'
_W='outletLabel'
_V='slaveIpAddress'
_U='status'
_T='thresholdEventType'
_S='thresholdSeverity'
_R='thresholdDescr'
_Q='sensorDescr'
_P='imageVersion'
_O='tripped'
_N='unavailable'
_M='not-accessible'
_L='groupName'
_K='targetUser'
_J='Integer32'
_I='accessible-for-notify'
_H='ipAddress'
_G='userName'
_F='objectInstance'
_E='objectName'
_D='read-write'
_C='read-only'
_B='current'
_A='EATON-EPDU-MA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pduAgent,=mibBuilder.importSymbols('EATON-OIDS','pduAgent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
eatonEpduMa=ModuleIdentity((1,3,6,1,4,1,534,6,6,6))
if mibBuilder.loadTexts:eatonEpduMa.setRevisions(('2008-11-12 00:00','2008-03-14 00:00','2007-02-14 00:00'))
class MilliAmps(TextualConvention,Unsigned32):status=_B;displayHint='d milliamps'
class MilliVolts(TextualConvention,Unsigned32):status=_B;displayHint='d millivolts'
class Watts(TextualConvention,Unsigned32):status=_B;displayHint='d watt'
class VoltAmps(TextualConvention,Unsigned32):status=_B;displayHint='d volt-amp'
class DegreesCelsius(TextualConvention,Unsigned32):status=_B;displayHint='d degree Celsius'
class RelativeHumidity(TextualConvention,Unsigned32):status=_B;displayHint='d %';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class PowerFactorPercentage(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,0))
_Board_ObjectIdentity=ObjectIdentity
board=_Board_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,1))
_Info_ObjectIdentity=ObjectIdentity
info=_Info_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,1,1))
_FirmwareVersion_Type=DisplayString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,534,6,6,6,1,1,1),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_B)
_SerialNumber_Type=DisplayString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,534,6,6,6,1,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:serialNumber.setStatus(_B)
_IpAddress_Type=IpAddress
_IpAddress_Object=MibScalar
ipAddress=_IpAddress_Object((1,3,6,1,4,1,534,6,6,6,1,1,3),_IpAddress_Type())
ipAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipAddress.setStatus(_B)
_Netmask_Type=IpAddress
_Netmask_Object=MibScalar
netmask=_Netmask_Object((1,3,6,1,4,1,534,6,6,6,1,1,4),_Netmask_Type())
netmask.setMaxAccess(_C)
if mibBuilder.loadTexts:netmask.setStatus(_B)
_Gateway_Type=IpAddress
_Gateway_Object=MibScalar
gateway=_Gateway_Object((1,3,6,1,4,1,534,6,6,6,1,1,5),_Gateway_Type())
gateway.setMaxAccess(_C)
if mibBuilder.loadTexts:gateway.setStatus(_B)
_Mac_Type=MacAddress
_Mac_Object=MibScalar
mac=_Mac_Object((1,3,6,1,4,1,534,6,6,6,1,1,6),_Mac_Type())
mac.setMaxAccess(_C)
if mibBuilder.loadTexts:mac.setStatus(_B)
class _HardwareRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HardwareRev_Type.__name__=_J
_HardwareRev_Object=MibScalar
hardwareRev=_HardwareRev_Object((1,3,6,1,4,1,534,6,6,6,1,1,7),_HardwareRev_Type())
hardwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareRev.setStatus(_B)
_UserName_Type=DisplayString
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,534,6,6,6,1,1,10),_UserName_Type())
userName.setMaxAccess(_I)
if mibBuilder.loadTexts:userName.setStatus(_B)
_ObjectName_Type=DisplayString
_ObjectName_Object=MibScalar
objectName=_ObjectName_Object((1,3,6,1,4,1,534,6,6,6,1,1,12),_ObjectName_Type())
objectName.setMaxAccess(_I)
if mibBuilder.loadTexts:objectName.setStatus(_B)
_ObjectInstance_Type=DisplayString
_ObjectInstance_Object=MibScalar
objectInstance=_ObjectInstance_Object((1,3,6,1,4,1,534,6,6,6,1,1,13),_ObjectInstance_Type())
objectInstance.setMaxAccess(_I)
if mibBuilder.loadTexts:objectInstance.setStatus(_B)
_TargetUser_Type=DisplayString
_TargetUser_Object=MibScalar
targetUser=_TargetUser_Object((1,3,6,1,4,1,534,6,6,6,1,1,14),_TargetUser_Type())
targetUser.setMaxAccess(_I)
if mibBuilder.loadTexts:targetUser.setStatus(_B)
_GroupName_Type=DisplayString
_GroupName_Object=MibScalar
groupName=_GroupName_Object((1,3,6,1,4,1,534,6,6,6,1,1,15),_GroupName_Type())
groupName.setMaxAccess(_I)
if mibBuilder.loadTexts:groupName.setStatus(_B)
_ImageVersion_Type=DisplayString
_ImageVersion_Object=MibScalar
imageVersion=_ImageVersion_Object((1,3,6,1,4,1,534,6,6,6,1,1,18),_ImageVersion_Type())
imageVersion.setMaxAccess(_I)
if mibBuilder.loadTexts:imageVersion.setStatus(_B)
_SensorDescr_Type=DisplayString
_SensorDescr_Object=MibScalar
sensorDescr=_SensorDescr_Object((1,3,6,1,4,1,534,6,6,6,1,1,19),_SensorDescr_Type())
sensorDescr.setMaxAccess(_I)
if mibBuilder.loadTexts:sensorDescr.setStatus(_B)
_ThresholdDescr_Type=DisplayString
_ThresholdDescr_Object=MibScalar
thresholdDescr=_ThresholdDescr_Object((1,3,6,1,4,1,534,6,6,6,1,1,20),_ThresholdDescr_Type())
thresholdDescr.setMaxAccess(_I)
if mibBuilder.loadTexts:thresholdDescr.setStatus(_B)
_ThresholdSeverity_Type=DisplayString
_ThresholdSeverity_Object=MibScalar
thresholdSeverity=_ThresholdSeverity_Object((1,3,6,1,4,1,534,6,6,6,1,1,21),_ThresholdSeverity_Type())
thresholdSeverity.setMaxAccess(_I)
if mibBuilder.loadTexts:thresholdSeverity.setStatus(_B)
_ThresholdEventType_Type=DisplayString
_ThresholdEventType_Object=MibScalar
thresholdEventType=_ThresholdEventType_Object((1,3,6,1,4,1,534,6,6,6,1,1,22),_ThresholdEventType_Type())
thresholdEventType.setMaxAccess(_I)
if mibBuilder.loadTexts:thresholdEventType.setStatus(_B)
_Status_Type=DisplayString
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,534,6,6,6,1,1,23),_Status_Type())
status.setMaxAccess(_I)
if mibBuilder.loadTexts:status.setStatus(_B)
_SlaveIpAddress_Type=IpAddress
_SlaveIpAddress_Object=MibScalar
slaveIpAddress=_SlaveIpAddress_Object((1,3,6,1,4,1,534,6,6,6,1,1,24),_SlaveIpAddress_Type())
slaveIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:slaveIpAddress.setStatus(_B)
_Outlets_ObjectIdentity=ObjectIdentity
outlets=_Outlets_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,1,2))
_OutletCount_Type=Integer32
_OutletCount_Object=MibScalar
outletCount=_OutletCount_Object((1,3,6,1,4,1,534,6,6,6,1,2,1),_OutletCount_Type())
outletCount.setMaxAccess(_C)
if mibBuilder.loadTexts:outletCount.setStatus(_B)
_OutletTable_Object=MibTable
outletTable=_OutletTable_Object((1,3,6,1,4,1,534,6,6,6,1,2,2))
if mibBuilder.loadTexts:outletTable.setStatus(_B)
_OutletEntry_Object=MibTableRow
outletEntry=_OutletEntry_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1))
outletEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:outletEntry.setStatus(_B)
class _OutletIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OutletIndex_Type.__name__=_J
_OutletIndex_Object=MibTableColumn
outletIndex=_OutletIndex_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,1),_OutletIndex_Type())
outletIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:outletIndex.setStatus(_B)
_OutletLabel_Type=DisplayString
_OutletLabel_Object=MibTableColumn
outletLabel=_OutletLabel_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,2),_OutletLabel_Type())
outletLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:outletLabel.setStatus(_B)
class _OutletOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*(('error',-1),('off',0),('on',1),('cycling',2)))
_OutletOperationalState_Type.__name__=_J
_OutletOperationalState_Object=MibTableColumn
outletOperationalState=_OutletOperationalState_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,3),_OutletOperationalState_Type())
outletOperationalState.setMaxAccess(_D)
if mibBuilder.loadTexts:outletOperationalState.setStatus(_B)
_OutletCurrent_Type=MilliAmps
_OutletCurrent_Object=MibTableColumn
outletCurrent=_OutletCurrent_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,4),_OutletCurrent_Type())
outletCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:outletCurrent.setStatus(_B)
_OutletMaxCurrent_Type=MilliAmps
_OutletMaxCurrent_Object=MibTableColumn
outletMaxCurrent=_OutletMaxCurrent_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,5),_OutletMaxCurrent_Type())
outletMaxCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:outletMaxCurrent.setStatus(_B)
_OutletVoltage_Type=MilliVolts
_OutletVoltage_Object=MibTableColumn
outletVoltage=_OutletVoltage_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,6),_OutletVoltage_Type())
outletVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:outletVoltage.setStatus(_B)
_OutletActivePower_Type=Watts
_OutletActivePower_Object=MibTableColumn
outletActivePower=_OutletActivePower_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,7),_OutletActivePower_Type())
outletActivePower.setMaxAccess(_C)
if mibBuilder.loadTexts:outletActivePower.setStatus(_B)
_OutletApparentPower_Type=VoltAmps
_OutletApparentPower_Object=MibTableColumn
outletApparentPower=_OutletApparentPower_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,8),_OutletApparentPower_Type())
outletApparentPower.setMaxAccess(_C)
if mibBuilder.loadTexts:outletApparentPower.setStatus(_B)
_OutletPowerFactor_Type=PowerFactorPercentage
_OutletPowerFactor_Object=MibTableColumn
outletPowerFactor=_OutletPowerFactor_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,9),_OutletPowerFactor_Type())
outletPowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:outletPowerFactor.setStatus(_B)
_OutletCurrentUpperWarning_Type=MilliAmps
_OutletCurrentUpperWarning_Object=MibTableColumn
outletCurrentUpperWarning=_OutletCurrentUpperWarning_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,21),_OutletCurrentUpperWarning_Type())
outletCurrentUpperWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:outletCurrentUpperWarning.setStatus(_B)
_OutletCurrentUpperCritical_Type=MilliAmps
_OutletCurrentUpperCritical_Object=MibTableColumn
outletCurrentUpperCritical=_OutletCurrentUpperCritical_Object((1,3,6,1,4,1,534,6,6,6,1,2,2,1,23),_OutletCurrentUpperCritical_Type())
outletCurrentUpperCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:outletCurrentUpperCritical.setStatus(_B)
_Unit_ObjectIdentity=ObjectIdentity
unit=_Unit_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,1,3))
_UnitReadings_ObjectIdentity=ObjectIdentity
unitReadings=_UnitReadings_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,1,3,1))
_UnitCurrent_Type=MilliAmps
_UnitCurrent_Object=MibScalar
unitCurrent=_UnitCurrent_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,1),_UnitCurrent_Type())
unitCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:unitCurrent.setStatus(_B)
_UnitVoltage_Type=MilliVolts
_UnitVoltage_Object=MibScalar
unitVoltage=_UnitVoltage_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,2),_UnitVoltage_Type())
unitVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:unitVoltage.setStatus(_B)
_UnitActivePower_Type=Watts
_UnitActivePower_Object=MibScalar
unitActivePower=_UnitActivePower_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,3),_UnitActivePower_Type())
unitActivePower.setMaxAccess(_C)
if mibBuilder.loadTexts:unitActivePower.setStatus(_B)
_UnitApparentPower_Type=Watts
_UnitApparentPower_Object=MibScalar
unitApparentPower=_UnitApparentPower_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,4),_UnitApparentPower_Type())
unitApparentPower.setMaxAccess(_C)
if mibBuilder.loadTexts:unitApparentPower.setStatus(_B)
_UnitCpuTemp_Type=DegreesCelsius
_UnitCpuTemp_Object=MibScalar
unitCpuTemp=_UnitCpuTemp_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,5),_UnitCpuTemp_Type())
unitCpuTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:unitCpuTemp.setStatus(_B)
class _UnitCircuitBreak0State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_N,-1),('ok',0),(_O,1)))
_UnitCircuitBreak0State_Type.__name__=_J
_UnitCircuitBreak0State_Object=MibScalar
unitCircuitBreak0State=_UnitCircuitBreak0State_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,20),_UnitCircuitBreak0State_Type())
unitCircuitBreak0State.setMaxAccess(_C)
if mibBuilder.loadTexts:unitCircuitBreak0State.setStatus(_B)
class _UnitCircuitBreak1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_N,-1),('ok',0),(_O,1)))
_UnitCircuitBreak1State_Type.__name__=_J
_UnitCircuitBreak1State_Object=MibScalar
unitCircuitBreak1State=_UnitCircuitBreak1State_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,21),_UnitCircuitBreak1State_Type())
unitCircuitBreak1State.setMaxAccess(_C)
if mibBuilder.loadTexts:unitCircuitBreak1State.setStatus(_B)
class _UnitCircuitBreak2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_N,-1),('ok',0),(_O,1)))
_UnitCircuitBreak2State_Type.__name__=_J
_UnitCircuitBreak2State_Object=MibScalar
unitCircuitBreak2State=_UnitCircuitBreak2State_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,22),_UnitCircuitBreak2State_Type())
unitCircuitBreak2State.setMaxAccess(_C)
if mibBuilder.loadTexts:unitCircuitBreak2State.setStatus(_B)
_UnitCircuitBreak0Current_Type=MilliAmps
_UnitCircuitBreak0Current_Object=MibScalar
unitCircuitBreak0Current=_UnitCircuitBreak0Current_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,40),_UnitCircuitBreak0Current_Type())
unitCircuitBreak0Current.setMaxAccess(_C)
if mibBuilder.loadTexts:unitCircuitBreak0Current.setStatus(_B)
_UnitCircuitBreak1Current_Type=MilliAmps
_UnitCircuitBreak1Current_Object=MibScalar
unitCircuitBreak1Current=_UnitCircuitBreak1Current_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,41),_UnitCircuitBreak1Current_Type())
unitCircuitBreak1Current.setMaxAccess(_C)
if mibBuilder.loadTexts:unitCircuitBreak1Current.setStatus(_B)
_UnitCircuitBreak2Current_Type=MilliAmps
_UnitCircuitBreak2Current_Object=MibScalar
unitCircuitBreak2Current=_UnitCircuitBreak2Current_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,42),_UnitCircuitBreak2Current_Type())
unitCircuitBreak2Current.setMaxAccess(_C)
if mibBuilder.loadTexts:unitCircuitBreak2Current.setStatus(_B)
_UnitVoltageLowerWarning_Type=MilliVolts
_UnitVoltageLowerWarning_Object=MibScalar
unitVoltageLowerWarning=_UnitVoltageLowerWarning_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,60),_UnitVoltageLowerWarning_Type())
unitVoltageLowerWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:unitVoltageLowerWarning.setStatus(_B)
_UnitVoltageLowerCritical_Type=MilliVolts
_UnitVoltageLowerCritical_Object=MibScalar
unitVoltageLowerCritical=_UnitVoltageLowerCritical_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,61),_UnitVoltageLowerCritical_Type())
unitVoltageLowerCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:unitVoltageLowerCritical.setStatus(_B)
_UnitVoltageUpperWarning_Type=MilliVolts
_UnitVoltageUpperWarning_Object=MibScalar
unitVoltageUpperWarning=_UnitVoltageUpperWarning_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,62),_UnitVoltageUpperWarning_Type())
unitVoltageUpperWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:unitVoltageUpperWarning.setStatus(_B)
_UnitVoltageUpperCritical_Type=MilliVolts
_UnitVoltageUpperCritical_Object=MibScalar
unitVoltageUpperCritical=_UnitVoltageUpperCritical_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,63),_UnitVoltageUpperCritical_Type())
unitVoltageUpperCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:unitVoltageUpperCritical.setStatus(_B)
_UnitCurrentUpperWarning_Type=MilliAmps
_UnitCurrentUpperWarning_Object=MibScalar
unitCurrentUpperWarning=_UnitCurrentUpperWarning_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,70),_UnitCurrentUpperWarning_Type())
unitCurrentUpperWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:unitCurrentUpperWarning.setStatus(_B)
_UnitCurrentUpperCritical_Type=MilliAmps
_UnitCurrentUpperCritical_Object=MibScalar
unitCurrentUpperCritical=_UnitCurrentUpperCritical_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,71),_UnitCurrentUpperCritical_Type())
unitCurrentUpperCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:unitCurrentUpperCritical.setStatus(_B)
_UnitTempLowerWarning_Type=DegreesCelsius
_UnitTempLowerWarning_Object=MibScalar
unitTempLowerWarning=_UnitTempLowerWarning_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,80),_UnitTempLowerWarning_Type())
unitTempLowerWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:unitTempLowerWarning.setStatus(_B)
_UnitTempLowerCritical_Type=DegreesCelsius
_UnitTempLowerCritical_Object=MibScalar
unitTempLowerCritical=_UnitTempLowerCritical_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,81),_UnitTempLowerCritical_Type())
unitTempLowerCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:unitTempLowerCritical.setStatus(_B)
_UnitTempUpperWarning_Type=DegreesCelsius
_UnitTempUpperWarning_Object=MibScalar
unitTempUpperWarning=_UnitTempUpperWarning_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,82),_UnitTempUpperWarning_Type())
unitTempUpperWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:unitTempUpperWarning.setStatus(_B)
_UnitTempUpperCritical_Type=DegreesCelsius
_UnitTempUpperCritical_Object=MibScalar
unitTempUpperCritical=_UnitTempUpperCritical_Object((1,3,6,1,4,1,534,6,6,6,1,3,1,83),_UnitTempUpperCritical_Type())
unitTempUpperCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:unitTempUpperCritical.setStatus(_B)
_Environmental_ObjectIdentity=ObjectIdentity
environmental=_Environmental_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,2))
_TempSensorCount_Type=Integer32
_TempSensorCount_Object=MibScalar
tempSensorCount=_TempSensorCount_Object((1,3,6,1,4,1,534,6,6,6,2,1),_TempSensorCount_Type())
tempSensorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tempSensorCount.setStatus(_B)
_TempSensorTable_Object=MibTable
tempSensorTable=_TempSensorTable_Object((1,3,6,1,4,1,534,6,6,6,2,2))
if mibBuilder.loadTexts:tempSensorTable.setStatus(_B)
_TempSensorEntry_Object=MibTableRow
tempSensorEntry=_TempSensorEntry_Object((1,3,6,1,4,1,534,6,6,6,2,2,1))
tempSensorEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:tempSensorEntry.setStatus(_B)
class _TempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TempSensorIndex_Type.__name__=_J
_TempSensorIndex_Object=MibTableColumn
tempSensorIndex=_TempSensorIndex_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,1),_TempSensorIndex_Type())
tempSensorIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:tempSensorIndex.setStatus(_B)
_TempSensorLabel_Type=DisplayString
_TempSensorLabel_Object=MibTableColumn
tempSensorLabel=_TempSensorLabel_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,2),_TempSensorLabel_Type())
tempSensorLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:tempSensorLabel.setStatus(_B)
_Temperature_Type=DegreesCelsius
_Temperature_Object=MibTableColumn
temperature=_Temperature_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,3),_Temperature_Type())
temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:temperature.setStatus(_B)
_TempLowerWarning_Type=DegreesCelsius
_TempLowerWarning_Object=MibTableColumn
tempLowerWarning=_TempLowerWarning_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,4),_TempLowerWarning_Type())
tempLowerWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:tempLowerWarning.setStatus(_B)
_TempUpperWarning_Type=DegreesCelsius
_TempUpperWarning_Object=MibTableColumn
tempUpperWarning=_TempUpperWarning_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,5),_TempUpperWarning_Type())
tempUpperWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:tempUpperWarning.setStatus(_B)
_TempLowerCritical_Type=DegreesCelsius
_TempLowerCritical_Object=MibTableColumn
tempLowerCritical=_TempLowerCritical_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,6),_TempLowerCritical_Type())
tempLowerCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:tempLowerCritical.setStatus(_B)
_TempUpperCritical_Type=DegreesCelsius
_TempUpperCritical_Object=MibTableColumn
tempUpperCritical=_TempUpperCritical_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,7),_TempUpperCritical_Type())
tempUpperCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:tempUpperCritical.setStatus(_B)
_TempLowerWarningReset_Type=DegreesCelsius
_TempLowerWarningReset_Object=MibTableColumn
tempLowerWarningReset=_TempLowerWarningReset_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,8),_TempLowerWarningReset_Type())
tempLowerWarningReset.setMaxAccess(_D)
if mibBuilder.loadTexts:tempLowerWarningReset.setStatus(_B)
_TempUpperWarningReset_Type=DegreesCelsius
_TempUpperWarningReset_Object=MibTableColumn
tempUpperWarningReset=_TempUpperWarningReset_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,9),_TempUpperWarningReset_Type())
tempUpperWarningReset.setMaxAccess(_D)
if mibBuilder.loadTexts:tempUpperWarningReset.setStatus(_B)
_TempLowerCriticalReset_Type=DegreesCelsius
_TempLowerCriticalReset_Object=MibTableColumn
tempLowerCriticalReset=_TempLowerCriticalReset_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,10),_TempLowerCriticalReset_Type())
tempLowerCriticalReset.setMaxAccess(_D)
if mibBuilder.loadTexts:tempLowerCriticalReset.setStatus(_B)
_TempUpperCriticalReset_Type=DegreesCelsius
_TempUpperCriticalReset_Object=MibTableColumn
tempUpperCriticalReset=_TempUpperCriticalReset_Object((1,3,6,1,4,1,534,6,6,6,2,2,1,11),_TempUpperCriticalReset_Type())
tempUpperCriticalReset.setMaxAccess(_D)
if mibBuilder.loadTexts:tempUpperCriticalReset.setStatus(_B)
_HumiditySensorCount_Type=Integer32
_HumiditySensorCount_Object=MibScalar
humiditySensorCount=_HumiditySensorCount_Object((1,3,6,1,4,1,534,6,6,6,2,3),_HumiditySensorCount_Type())
humiditySensorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:humiditySensorCount.setStatus(_B)
_HumiditySensorTable_Object=MibTable
humiditySensorTable=_HumiditySensorTable_Object((1,3,6,1,4,1,534,6,6,6,2,4))
if mibBuilder.loadTexts:humiditySensorTable.setStatus(_B)
_HumiditySensorEntry_Object=MibTableRow
humiditySensorEntry=_HumiditySensorEntry_Object((1,3,6,1,4,1,534,6,6,6,2,4,1))
humiditySensorEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:humiditySensorEntry.setStatus(_B)
class _HumiditySensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HumiditySensorIndex_Type.__name__=_J
_HumiditySensorIndex_Object=MibTableColumn
humiditySensorIndex=_HumiditySensorIndex_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,1),_HumiditySensorIndex_Type())
humiditySensorIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:humiditySensorIndex.setStatus(_B)
_HumiditySensorLabel_Type=DisplayString
_HumiditySensorLabel_Object=MibTableColumn
humiditySensorLabel=_HumiditySensorLabel_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,2),_HumiditySensorLabel_Type())
humiditySensorLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:humiditySensorLabel.setStatus(_B)
_Humidity_Type=RelativeHumidity
_Humidity_Object=MibTableColumn
humidity=_Humidity_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,3),_Humidity_Type())
humidity.setMaxAccess(_C)
if mibBuilder.loadTexts:humidity.setStatus(_B)
_HumidityLowerWarning_Type=RelativeHumidity
_HumidityLowerWarning_Object=MibTableColumn
humidityLowerWarning=_HumidityLowerWarning_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,4),_HumidityLowerWarning_Type())
humidityLowerWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityLowerWarning.setStatus(_B)
_HumidityUpperWarning_Type=RelativeHumidity
_HumidityUpperWarning_Object=MibTableColumn
humidityUpperWarning=_HumidityUpperWarning_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,5),_HumidityUpperWarning_Type())
humidityUpperWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityUpperWarning.setStatus(_B)
_HumidityLowerCritical_Type=RelativeHumidity
_HumidityLowerCritical_Object=MibTableColumn
humidityLowerCritical=_HumidityLowerCritical_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,6),_HumidityLowerCritical_Type())
humidityLowerCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityLowerCritical.setStatus(_B)
_HumidityUpperCritical_Type=RelativeHumidity
_HumidityUpperCritical_Object=MibTableColumn
humidityUpperCritical=_HumidityUpperCritical_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,7),_HumidityUpperCritical_Type())
humidityUpperCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityUpperCritical.setStatus(_B)
_HumidityLowerWarningReset_Type=RelativeHumidity
_HumidityLowerWarningReset_Object=MibTableColumn
humidityLowerWarningReset=_HumidityLowerWarningReset_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,8),_HumidityLowerWarningReset_Type())
humidityLowerWarningReset.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityLowerWarningReset.setStatus(_B)
_HumidityUpperWarningReset_Type=RelativeHumidity
_HumidityUpperWarningReset_Object=MibTableColumn
humidityUpperWarningReset=_HumidityUpperWarningReset_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,9),_HumidityUpperWarningReset_Type())
humidityUpperWarningReset.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityUpperWarningReset.setStatus(_B)
_HumidityLowerCriticalReset_Type=RelativeHumidity
_HumidityLowerCriticalReset_Object=MibTableColumn
humidityLowerCriticalReset=_HumidityLowerCriticalReset_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,10),_HumidityLowerCriticalReset_Type())
humidityLowerCriticalReset.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityLowerCriticalReset.setStatus(_B)
_HumidityUpperCriticalReset_Type=RelativeHumidity
_HumidityUpperCriticalReset_Object=MibTableColumn
humidityUpperCriticalReset=_HumidityUpperCriticalReset_Object((1,3,6,1,4,1,534,6,6,6,2,4,1,11),_HumidityUpperCriticalReset_Type())
humidityUpperCriticalReset.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityUpperCriticalReset.setStatus(_B)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,9))
_Compliances_ObjectIdentity=ObjectIdentity
compliances=_Compliances_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,9,1))
_Groups_ObjectIdentity=ObjectIdentity
groups=_Groups_ObjectIdentity((1,3,6,1,4,1,534,6,6,6,9,2))
infoGroup=ObjectGroup((1,3,6,1,4,1,534,6,6,6,9,2,1))
infoGroup.setObjects(*((_A,_b),(_A,_c),(_A,_H),(_A,_d),(_A,_e),(_A,'mac'),(_A,_f),(_A,_G),(_A,_E),(_A,_F),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:infoGroup.setStatus(_B)
outletsGroup=ObjectGroup((1,3,6,1,4,1,534,6,6,6,9,2,2))
outletsGroup.setObjects(*((_A,_g),(_A,_W),(_A,_X),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:outletsGroup.setStatus(_B)
unitSensorsGroup=ObjectGroup((1,3,6,1,4,1,534,6,6,6,9,2,4))
unitSensorsGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:unitSensorsGroup.setStatus(_B)
externalTemperatureGroup=ObjectGroup((1,3,6,1,4,1,534,6,6,6,9,2,6))
externalTemperatureGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:externalTemperatureGroup.setStatus(_B)
externalHumidityGroup=ObjectGroup((1,3,6,1,4,1,534,6,6,6,9,2,7))
externalHumidityGroup.setObjects(*((_A,_AL),(_A,_AM),(_A,'humidity'),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:externalHumidityGroup.setStatus(_B)
rebootStarted=NotificationType((1,3,6,1,4,1,534,6,6,6,0,1))
rebootStarted.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:rebootStarted.setStatus(_B)
rebootCompleted=NotificationType((1,3,6,1,4,1,534,6,6,6,0,2))
rebootCompleted.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:rebootCompleted.setStatus(_B)
userLogin=NotificationType((1,3,6,1,4,1,534,6,6,6,0,3))
userLogin.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:userLogin.setStatus(_B)
userLogout=NotificationType((1,3,6,1,4,1,534,6,6,6,0,4))
userLogout.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:userLogout.setStatus(_B)
userAuthenticationFailure=NotificationType((1,3,6,1,4,1,534,6,6,6,0,5))
userAuthenticationFailure.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:userAuthenticationFailure.setStatus(_B)
userSessionTimeout=NotificationType((1,3,6,1,4,1,534,6,6,6,0,8))
userSessionTimeout.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:userSessionTimeout.setStatus(_B)
userAdded=NotificationType((1,3,6,1,4,1,534,6,6,6,0,11))
userAdded.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:userAdded.setStatus(_B)
userModified=NotificationType((1,3,6,1,4,1,534,6,6,6,0,12))
userModified.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:userModified.setStatus(_B)
userDeleted=NotificationType((1,3,6,1,4,1,534,6,6,6,0,13))
userDeleted.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:userDeleted.setStatus(_B)
groupAdded=NotificationType((1,3,6,1,4,1,534,6,6,6,0,14))
groupAdded.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:groupAdded.setStatus(_B)
groupModified=NotificationType((1,3,6,1,4,1,534,6,6,6,0,15))
groupModified.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:groupModified.setStatus(_B)
groupDeleted=NotificationType((1,3,6,1,4,1,534,6,6,6,0,16))
groupDeleted.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:groupDeleted.setStatus(_B)
deviceUpdateStarted=NotificationType((1,3,6,1,4,1,534,6,6,6,0,20))
deviceUpdateStarted.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_P)))
if mibBuilder.loadTexts:deviceUpdateStarted.setStatus(_B)
userBlocked=NotificationType((1,3,6,1,4,1,534,6,6,6,0,22))
userBlocked.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:userBlocked.setStatus(_B)
powerControl=NotificationType((1,3,6,1,4,1,534,6,6,6,0,23))
powerControl.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:powerControl.setStatus(_B)
userPasswordChanged=NotificationType((1,3,6,1,4,1,534,6,6,6,0,24))
userPasswordChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:userPasswordChanged.setStatus(_B)
passwordSettingsChanged=NotificationType((1,3,6,1,4,1,534,6,6,6,0,28))
passwordSettingsChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_U)))
if mibBuilder.loadTexts:passwordSettingsChanged.setStatus(_B)
firmwareFileDiscarded=NotificationType((1,3,6,1,4,1,534,6,6,6,0,36))
firmwareFileDiscarded.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:firmwareFileDiscarded.setStatus(_B)
firmwareValidationFailed=NotificationType((1,3,6,1,4,1,534,6,6,6,0,38))
firmwareValidationFailed.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:firmwareValidationFailed.setStatus(_B)
securityViolation=NotificationType((1,3,6,1,4,1,534,6,6,6,0,39))
securityViolation.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:securityViolation.setStatus(_B)
logFileCleared=NotificationType((1,3,6,1,4,1,534,6,6,6,0,41))
logFileCleared.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:logFileCleared.setStatus(_B)
thresholdAlarm=NotificationType((1,3,6,1,4,1,534,6,6,6,0,45))
thresholdAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:thresholdAlarm.setStatus(_B)
outletGroupingConnectivityLost=NotificationType((1,3,6,1,4,1,534,6,6,6,0,50))
outletGroupingConnectivityLost.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_V)))
if mibBuilder.loadTexts:outletGroupingConnectivityLost.setStatus(_B)
trapsGroup=NotificationGroup((1,3,6,1,4,1,534,6,6,6,9,2,9))
trapsGroup.setObjects(*((_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:trapsGroup.setStatus(_B)
compliance=ModuleCompliance((1,3,6,1,4,1,534,6,6,6,9,1,1))
compliance.setObjects(*((_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'MilliAmps':MilliAmps,'MilliVolts':MilliVolts,'Watts':Watts,'VoltAmps':VoltAmps,'DegreesCelsius':DegreesCelsius,'RelativeHumidity':RelativeHumidity,'PowerFactorPercentage':PowerFactorPercentage,'eatonEpduMa':eatonEpduMa,'traps':traps,_AV:rebootStarted,_AW:rebootCompleted,_AX:userLogin,_AY:userLogout,_AZ:userAuthenticationFailure,_Aa:userSessionTimeout,_Ab:userAdded,_Ac:userModified,_Ad:userDeleted,_Ae:groupAdded,_Af:groupModified,_Ag:groupDeleted,_Ah:deviceUpdateStarted,_Ai:userBlocked,_Aj:powerControl,_Ak:userPasswordChanged,_Al:passwordSettingsChanged,_Am:firmwareFileDiscarded,_An:firmwareValidationFailed,_Ao:securityViolation,_Ap:logFileCleared,_Aq:thresholdAlarm,_Ar:outletGroupingConnectivityLost,'board':board,'info':info,_b:firmwareVersion,_c:serialNumber,_H:ipAddress,_d:netmask,_e:gateway,'mac':mac,_f:hardwareRev,_G:userName,_E:objectName,_F:objectInstance,_K:targetUser,_L:groupName,_P:imageVersion,_Q:sensorDescr,_R:thresholdDescr,_S:thresholdSeverity,_T:thresholdEventType,_U:status,_V:slaveIpAddress,'outlets':outlets,_g:outletCount,'outletTable':outletTable,'outletEntry':outletEntry,_Y:outletIndex,_W:outletLabel,_X:outletOperationalState,_h:outletCurrent,_i:outletMaxCurrent,_j:outletVoltage,_k:outletActivePower,_l:outletApparentPower,_m:outletPowerFactor,_n:outletCurrentUpperWarning,_o:outletCurrentUpperCritical,'unit':unit,'unitReadings':unitReadings,_p:unitCurrent,_q:unitVoltage,_r:unitActivePower,_s:unitApparentPower,_t:unitCpuTemp,_u:unitCircuitBreak0State,_v:unitCircuitBreak1State,_w:unitCircuitBreak2State,_x:unitCircuitBreak0Current,_y:unitCircuitBreak1Current,_z:unitCircuitBreak2Current,_A0:unitVoltageLowerWarning,_A2:unitVoltageLowerCritical,_A1:unitVoltageUpperWarning,_A3:unitVoltageUpperCritical,_A4:unitCurrentUpperWarning,_A5:unitCurrentUpperCritical,_A6:unitTempLowerWarning,_A8:unitTempLowerCritical,_A7:unitTempUpperWarning,_A9:unitTempUpperCritical,'environmental':environmental,_AA:tempSensorCount,'tempSensorTable':tempSensorTable,'tempSensorEntry':tempSensorEntry,_Z:tempSensorIndex,_AB:tempSensorLabel,_AC:temperature,_AD:tempLowerWarning,_AE:tempUpperWarning,_AF:tempLowerCritical,_AG:tempUpperCritical,_AH:tempLowerWarningReset,_AI:tempUpperWarningReset,_AJ:tempLowerCriticalReset,_AK:tempUpperCriticalReset,_AL:humiditySensorCount,'humiditySensorTable':humiditySensorTable,'humiditySensorEntry':humiditySensorEntry,_a:humiditySensorIndex,_AM:humiditySensorLabel,'humidity':humidity,_AN:humidityLowerWarning,_AO:humidityUpperWarning,_AP:humidityLowerCritical,_AQ:humidityUpperCritical,_AR:humidityLowerWarningReset,_AS:humidityUpperWarningReset,_AT:humidityLowerCriticalReset,_AU:humidityUpperCriticalReset,'conformance':conformance,'compliances':compliances,'compliance':compliance,'groups':groups,_As:infoGroup,_At:outletsGroup,_Au:unitSensorsGroup,_Av:externalTemperatureGroup,_Aw:externalHumidityGroup,_Ax:trapsGroup})