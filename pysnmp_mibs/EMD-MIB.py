_Bs='controlGroup'
_Br='trapsGroup'
_Bq='trapInformationGroup'
_Bp='measurementsGroup'
_Bo='configGroup'
_Bn='smsMessageTransmissionFailure'
_Bm='peripheralDeviceFirmwareUpdate'
_Bl='unknownPeripheralDeviceAttached'
_Bk='serverReachabilityError'
_Bj='radiusError'
_Bi='serverConnectivityUnrecoverable'
_Bh='webcamRemoved'
_Bg='webcamInserted'
_Bf='deviceSettingsRestored'
_Be='deviceSettingsSaved'
_Bd='userDeclinedRestrictedServiceAgreement'
_Bc='userAcceptedRestrictedServiceAgreement'
_Bb='lhxSupportChanged'
_Ba='usbSlaveDisconnected'
_BZ='usbSlaveConnected'
_BY='deviceIdentificationChanged'
_BX='serverReachable'
_BW='serverNotReachable'
_BV='pingServerDisabled'
_BU='pingServerEnabled'
_BT='deviceUpdateFailed'
_BS='ldapError'
_BR='smtpMessageTransmissionFailure'
_BQ='externalSensorStateChange'
_BP='bulkConfigurationCopied'
_BO='bulkConfigurationSaved'
_BN='logFileCleared'
_BM='firmwareValidationFailed'
_BL='passwordSettingsChanged'
_BK='userPasswordChanged'
_BJ='userBlocked'
_BI='deviceUpdateCompleted'
_BH='deviceUpdateStarted'
_BG='roleDeleted'
_BF='roleModified'
_BE='roleAdded'
_BD='userDeleted'
_BC='userModified'
_BB='userAdded'
_BA='userSessionTimeout'
_B9='userAuthenticationFailure'
_B8='userLogout'
_B7='userLogin'
_B6='systemReset'
_B5='systemStarted'
_B4='actuatorState'
_B3='logExternalSensorMinValue'
_B2='logExternalSensorMaxValue'
_B1='logExternalSensorAvgValue'
_B0='logExternalSensorState'
_A_='logExternalSensorDataAvailable'
_Az='dataLoggingEnableForAllSensors'
_Ay='logTimeStamp'
_Ax='newestLogID'
_Aw='oldestLogID'
_Av='dataLogging'
_Au='measurementsExternalSensorIsAvailable'
_At='secondNTPServerAddress'
_As='secondNTPServerAddressType'
_Ar='firstNTPServerAddress'
_Aq='firstNTPServerAddressType'
_Ap='useDHCPProvidedNTPServer'
_Ao='synchronizeWithNTPServer'
_An='externalSensorAlarmedToNormalDelay'
_Am='peripheralDevicesAutoManagement'
_Al='peripheralDevicePackageState'
_Ak='peripheralDevicePackageFirmwareTimeStamp'
_Aj='peripheralDevicePackageMinFirmwareVersion'
_Ai='peripheralDevicePackageModel'
_Ah='cascadedDeviceConnected'
_Ag='measurementsPerLogEntry'
_Af='measurementPeriod'
_Ae='serverPingEnabled'
_Ad='serverCount'
_Ac='managedExternalSensorCount'
_Ab='externalSensorTypeDefaultEnabledThresholds'
_Aa='externalSensorTypeDefaultUpperWarningThreshold'
_AZ='externalSensorTypeDefaultUpperCriticalThreshold'
_AY='externalSensorTypeDefaultLowerWarningThreshold'
_AX='externalSensorTypeDefaultLowerCriticalThreshold'
_AW='externalSensorTypeDefaultStateChangeDelay'
_AV='externalSensorTypeDefaultHysteresis'
_AU='externalSensorUseDefaultThresholds'
_AT='externalSensorIsActuator'
_AS='externalSensorsZCoordinateUnits'
_AR='externalSensorPort'
_AQ='externalSensorEnabledThresholds'
_AP='externalSensorUpperWarningThreshold'
_AO='externalSensorUpperCriticalThreshold'
_AN='externalSensorLowerWarningThreshold'
_AM='externalSensorLowerCriticalThreshold'
_AL='externalSensorStateChangeDelay'
_AK='externalSensorHysteresis'
_AJ='externalSensorMinimum'
_AI='externalSensorMaximum'
_AH='externalSensorTolerance'
_AG='externalSensorResolution'
_AF='externalSensorAccuracy'
_AE='externalSensorDecimalDigits'
_AD='externalSensorUnits'
_AC='externalSensorZCoordinate'
_AB='externalSensorYCoordinate'
_AA='externalSensorXCoordinate'
_A9='externalSensorDescription'
_A8='externalSensorName'
_A7='firmwareVersion'
_A6='hardwareVersion'
_A5='utcOffset'
_A4='deviceMACAddress'
_A3='deviceInetGateway'
_A2='deviceInetNetmask'
_A1='externalSensorCount'
_A0='peripheralDevicePackageId'
_z='upperCritical'
_y='upperWarning'
_x='lowerWarning'
_w='lowerCritical'
_v='phoneNumber'
_u='peripheralDeviceFirmwareUpdateState'
_t='peripheralDeviceRomcode'
_s='lhxSupportEnabled'
_r='changedParameterNewValue'
_q='deviceChangedParameter'
_p='smtpServer'
_o='smtpMessageRecipients'
_n='typeOfSensor'
_m='externalSensorNumber'
_l='oldSensorState'
_k='measurementsExternalSensorTimeStamp'
_j='measurementsExternalSensorValue'
_i='measurementsExternalSensorState'
_h='peripheralDevicePackagePosition'
_g='peripheralDevicePackageFirmwareVersion'
_f='peripheralDevicePackageSerialNumber'
_e='externalOnOffSensorSubtype'
_d='externalSensorChannelNumber'
_c='externalSensorSerialNumber'
_b='logIndex'
_a='externalSensorType'
_Z='Bits'
_Y='InetAddressType'
_X='webcamConnectionPort'
_W='webcamModel'
_V='not-accessible'
_U='errorDescription'
_T='roleName'
_S='imageVersion'
_R='sensorID'
_Q='targetUser'
_P='serverIPAddress'
_O='Integer32'
_N='accessible-for-notify'
_M='userName'
_L='read-write'
_K='agentInetPortNumber'
_J='deviceInetIPAddress'
_I='deviceInetAddressType'
_H='sysName'
_G='sysLocation'
_F='sysContact'
_E='deviceName'
_D='read-only'
_C='SNMPv2-MIB'
_B='current'
_A='EMD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_Y,'InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysContact,sysLocation,sysName=mibBuilder.importSymbols(_C,_F,_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_Z,'Counter32','Counter64','Gauge32',_O,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
raritan=ModuleIdentity((1,3,6,1,4,1,13742))
if mibBuilder.loadTexts:raritan.setRevisions(('2015-10-26 00:00','2014-09-29 00:00','2014-02-21 00:00','2013-12-17 00:00','2012-10-01 00:00','2012-07-11 00:00','2012-05-25 00:00','2012-01-25 00:00','2011-12-14 00:00','2011-12-12 00:00','2011-11-04 00:00','2011-08-26 00:00','2011-08-05 00:00','2011-06-30 00:00','2011-03-30 00:00','2011-03-10 00:00','2011-02-14 00:00'))
class SensorTypeEnumeration(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,28,30,31,42,43,44,45)));namedValues=NamedValues(*(('rmsCurrent',1),('peakCurrent',2),('unbalancedCurrent',3),('rmsVoltage',4),('activePower',5),('apparentPower',6),('powerFactor',7),('activeEnergy',8),('apparentEnergy',9),('temperature',10),('humidity',11),('airFlow',12),('airPressure',13),('onOff',14),('trip',15),('vibration',16),('waterDetection',17),('smokeDetection',18),('binary',19),('contact',20),('fanSpeed',21),('absoluteHumidity',28),('other',30),('none',31),('illuminance',42),('doorContact',43),('tamperDetection',44),('motionDetection',45)))
class SensorStateEnumeration(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('unavailable',-1),('open',0),('closed',1),('belowLowerCritical',2),('belowLowerWarning',3),('normal',4),('aboveUpperWarning',5),('aboveUpperCritical',6),('on',7),('off',8),('detected',9),('notDetected',10),('alarmed',11)))
class SensorUnitsEnumeration(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('none',-1),('other',0),('volt',1),('amp',2),('watt',3),('voltamp',4),('wattHour',5),('voltampHour',6),('degreeC',7),('hertz',8),('percent',9),('meterpersec',10),('pascal',11),('psi',12),('g',13),('degreeF',14),('feet',15),('inches',16),('cm',17),('meters',18),('rpm',19),('degrees',20),('lux',21),('grampercubicmeter',22),('voltampReactive',23)))
class ExternalSensorsZCoordinateUnitsEnumeration(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('rackUnits',0),('text',1)))
class HundredthsOfAPercentage(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
class DeviceIdentificationParameterEnumeration(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),(_F,1),(_H,2),(_G,3)))
class PeripheralDeviceFirmwareUpdateStateEnumeration(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('started',1),('successful',2),('failed',3)))
_Emd_ObjectIdentity=ObjectIdentity
emd=_Emd_ObjectIdentity((1,3,6,1,4,1,13742,8))
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,13742,8,0))
_TrapInformation_ObjectIdentity=ObjectIdentity
trapInformation=_TrapInformation_ObjectIdentity((1,3,6,1,4,1,13742,8,0,0))
_UserName_Type=DisplayString
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,13742,8,0,0,1),_UserName_Type())
userName.setMaxAccess(_D)
if mibBuilder.loadTexts:userName.setStatus(_B)
_TargetUser_Type=DisplayString
_TargetUser_Object=MibScalar
targetUser=_TargetUser_Object((1,3,6,1,4,1,13742,8,0,0,2),_TargetUser_Type())
targetUser.setMaxAccess(_D)
if mibBuilder.loadTexts:targetUser.setStatus(_B)
_ImageVersion_Type=DisplayString
_ImageVersion_Object=MibScalar
imageVersion=_ImageVersion_Object((1,3,6,1,4,1,13742,8,0,0,3),_ImageVersion_Type())
imageVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:imageVersion.setStatus(_B)
_RoleName_Type=DisplayString
_RoleName_Object=MibScalar
roleName=_RoleName_Object((1,3,6,1,4,1,13742,8,0,0,4),_RoleName_Type())
roleName.setMaxAccess(_D)
if mibBuilder.loadTexts:roleName.setStatus(_B)
_SmtpMessageRecipients_Type=DisplayString
_SmtpMessageRecipients_Object=MibScalar
smtpMessageRecipients=_SmtpMessageRecipients_Object((1,3,6,1,4,1,13742,8,0,0,5),_SmtpMessageRecipients_Type())
smtpMessageRecipients.setMaxAccess(_D)
if mibBuilder.loadTexts:smtpMessageRecipients.setStatus(_B)
_SmtpServer_Type=DisplayString
_SmtpServer_Object=MibScalar
smtpServer=_SmtpServer_Object((1,3,6,1,4,1,13742,8,0,0,6),_SmtpServer_Type())
smtpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:smtpServer.setStatus(_B)
_OldSensorState_Type=SensorStateEnumeration
_OldSensorState_Object=MibScalar
oldSensorState=_OldSensorState_Object((1,3,6,1,4,1,13742,8,0,0,7),_OldSensorState_Type())
oldSensorState.setMaxAccess(_N)
if mibBuilder.loadTexts:oldSensorState.setStatus(_B)
class _ExternalSensorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ExternalSensorNumber_Type.__name__=_O
_ExternalSensorNumber_Object=MibScalar
externalSensorNumber=_ExternalSensorNumber_Object((1,3,6,1,4,1,13742,8,0,0,8),_ExternalSensorNumber_Type())
externalSensorNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:externalSensorNumber.setStatus(_B)
_TypeOfSensor_Type=SensorTypeEnumeration
_TypeOfSensor_Object=MibScalar
typeOfSensor=_TypeOfSensor_Object((1,3,6,1,4,1,13742,8,0,0,9),_TypeOfSensor_Type())
typeOfSensor.setMaxAccess(_N)
if mibBuilder.loadTexts:typeOfSensor.setStatus(_B)
_ErrorDescription_Type=DisplayString
_ErrorDescription_Object=MibScalar
errorDescription=_ErrorDescription_Object((1,3,6,1,4,1,13742,8,0,0,10),_ErrorDescription_Type())
errorDescription.setMaxAccess(_N)
if mibBuilder.loadTexts:errorDescription.setStatus(_B)
_DeviceChangedParameter_Type=DeviceIdentificationParameterEnumeration
_DeviceChangedParameter_Object=MibScalar
deviceChangedParameter=_DeviceChangedParameter_Object((1,3,6,1,4,1,13742,8,0,0,11),_DeviceChangedParameter_Type())
deviceChangedParameter.setMaxAccess(_N)
if mibBuilder.loadTexts:deviceChangedParameter.setStatus(_B)
_ChangedParameterNewValue_Type=DisplayString
_ChangedParameterNewValue_Object=MibScalar
changedParameterNewValue=_ChangedParameterNewValue_Object((1,3,6,1,4,1,13742,8,0,0,12),_ChangedParameterNewValue_Type())
changedParameterNewValue.setMaxAccess(_N)
if mibBuilder.loadTexts:changedParameterNewValue.setStatus(_B)
_LhxSupportEnabled_Type=TruthValue
_LhxSupportEnabled_Object=MibScalar
lhxSupportEnabled=_LhxSupportEnabled_Object((1,3,6,1,4,1,13742,8,0,0,13),_LhxSupportEnabled_Type())
lhxSupportEnabled.setMaxAccess(_N)
if mibBuilder.loadTexts:lhxSupportEnabled.setStatus(_B)
_WebcamModel_Type=DisplayString
_WebcamModel_Object=MibScalar
webcamModel=_WebcamModel_Object((1,3,6,1,4,1,13742,8,0,0,14),_WebcamModel_Type())
webcamModel.setMaxAccess(_N)
if mibBuilder.loadTexts:webcamModel.setStatus(_B)
_WebcamConnectionPort_Type=DisplayString
_WebcamConnectionPort_Object=MibScalar
webcamConnectionPort=_WebcamConnectionPort_Object((1,3,6,1,4,1,13742,8,0,0,15),_WebcamConnectionPort_Type())
webcamConnectionPort.setMaxAccess(_N)
if mibBuilder.loadTexts:webcamConnectionPort.setStatus(_B)
_PeripheralDeviceRomcode_Type=DisplayString
_PeripheralDeviceRomcode_Object=MibScalar
peripheralDeviceRomcode=_PeripheralDeviceRomcode_Object((1,3,6,1,4,1,13742,8,0,0,16),_PeripheralDeviceRomcode_Type())
peripheralDeviceRomcode.setMaxAccess(_N)
if mibBuilder.loadTexts:peripheralDeviceRomcode.setStatus(_B)
_PeripheralDeviceFirmwareUpdateState_Type=PeripheralDeviceFirmwareUpdateStateEnumeration
_PeripheralDeviceFirmwareUpdateState_Object=MibScalar
peripheralDeviceFirmwareUpdateState=_PeripheralDeviceFirmwareUpdateState_Object((1,3,6,1,4,1,13742,8,0,0,17),_PeripheralDeviceFirmwareUpdateState_Type())
peripheralDeviceFirmwareUpdateState.setMaxAccess(_N)
if mibBuilder.loadTexts:peripheralDeviceFirmwareUpdateState.setStatus(_B)
_AgentInetPortNumber_Type=InetPortNumber
_AgentInetPortNumber_Object=MibScalar
agentInetPortNumber=_AgentInetPortNumber_Object((1,3,6,1,4,1,13742,8,0,0,18),_AgentInetPortNumber_Type())
agentInetPortNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:agentInetPortNumber.setStatus(_B)
_PhoneNumber_Type=DisplayString
_PhoneNumber_Object=MibScalar
phoneNumber=_PhoneNumber_Object((1,3,6,1,4,1,13742,8,0,0,19),_PhoneNumber_Type())
phoneNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:phoneNumber.setStatus(_B)
_Configuration_ObjectIdentity=ObjectIdentity
configuration=_Configuration_ObjectIdentity((1,3,6,1,4,1,13742,8,1))
_Unit_ObjectIdentity=ObjectIdentity
unit=_Unit_ObjectIdentity((1,3,6,1,4,1,13742,8,1,1))
_UnitConfiguration_ObjectIdentity=ObjectIdentity
unitConfiguration=_UnitConfiguration_ObjectIdentity((1,3,6,1,4,1,13742,8,1,1,1))
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,13742,8,1,1,1,1),_DeviceName_Type())
deviceName.setMaxAccess(_L)
if mibBuilder.loadTexts:deviceName.setStatus(_B)
_HardwareVersion_Type=DisplayString
_HardwareVersion_Object=MibScalar
hardwareVersion=_HardwareVersion_Object((1,3,6,1,4,1,13742,8,1,1,1,2),_HardwareVersion_Type())
hardwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hardwareVersion.setStatus(_B)
_FirmwareVersion_Type=DisplayString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,13742,8,1,1,1,3),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_B)
_UtcOffset_Type=DisplayString
_UtcOffset_Object=MibScalar
utcOffset=_UtcOffset_Object((1,3,6,1,4,1,13742,8,1,1,1,4),_UtcOffset_Type())
utcOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:utcOffset.setStatus(_B)
class _ExternalSensorCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExternalSensorCount_Type.__name__=_O
_ExternalSensorCount_Object=MibScalar
externalSensorCount=_ExternalSensorCount_Object((1,3,6,1,4,1,13742,8,1,1,1,5),_ExternalSensorCount_Type())
externalSensorCount.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorCount.setStatus(_B)
class _ManagedExternalSensorCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ManagedExternalSensorCount_Type.__name__=_O
_ManagedExternalSensorCount_Object=MibScalar
managedExternalSensorCount=_ManagedExternalSensorCount_Object((1,3,6,1,4,1,13742,8,1,1,1,6),_ManagedExternalSensorCount_Type())
managedExternalSensorCount.setMaxAccess(_D)
if mibBuilder.loadTexts:managedExternalSensorCount.setStatus(_B)
_ExternalSensorsZCoordinateUnits_Type=ExternalSensorsZCoordinateUnitsEnumeration
_ExternalSensorsZCoordinateUnits_Object=MibScalar
externalSensorsZCoordinateUnits=_ExternalSensorsZCoordinateUnits_Object((1,3,6,1,4,1,13742,8,1,1,1,7),_ExternalSensorsZCoordinateUnits_Type())
externalSensorsZCoordinateUnits.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorsZCoordinateUnits.setStatus(_B)
_DeviceMACAddress_Type=MacAddress
_DeviceMACAddress_Object=MibScalar
deviceMACAddress=_DeviceMACAddress_Object((1,3,6,1,4,1,13742,8,1,1,1,8),_DeviceMACAddress_Type())
deviceMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceMACAddress.setStatus(_B)
_DeviceInetAddressType_Type=InetAddressType
_DeviceInetAddressType_Object=MibScalar
deviceInetAddressType=_DeviceInetAddressType_Object((1,3,6,1,4,1,13742,8,1,1,1,9),_DeviceInetAddressType_Type())
deviceInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceInetAddressType.setStatus(_B)
_DeviceInetIPAddress_Type=InetAddress
_DeviceInetIPAddress_Object=MibScalar
deviceInetIPAddress=_DeviceInetIPAddress_Object((1,3,6,1,4,1,13742,8,1,1,1,10),_DeviceInetIPAddress_Type())
deviceInetIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceInetIPAddress.setStatus(_B)
_DeviceInetNetmask_Type=InetAddress
_DeviceInetNetmask_Object=MibScalar
deviceInetNetmask=_DeviceInetNetmask_Object((1,3,6,1,4,1,13742,8,1,1,1,11),_DeviceInetNetmask_Type())
deviceInetNetmask.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceInetNetmask.setStatus(_B)
_DeviceInetGateway_Type=InetAddress
_DeviceInetGateway_Object=MibScalar
deviceInetGateway=_DeviceInetGateway_Object((1,3,6,1,4,1,13742,8,1,1,1,12),_DeviceInetGateway_Type())
deviceInetGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceInetGateway.setStatus(_B)
class _ServerCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ServerCount_Type.__name__=_O
_ServerCount_Object=MibScalar
serverCount=_ServerCount_Object((1,3,6,1,4,1,13742,8,1,1,1,13),_ServerCount_Type())
serverCount.setMaxAccess(_D)
if mibBuilder.loadTexts:serverCount.setStatus(_B)
_Model_Type=DisplayString
_Model_Object=MibScalar
model=_Model_Object((1,3,6,1,4,1,13742,8,1,1,1,14),_Model_Type())
model.setMaxAccess(_D)
if mibBuilder.loadTexts:model.setStatus(_B)
_CascadedDeviceConnected_Type=TruthValue
_CascadedDeviceConnected_Object=MibScalar
cascadedDeviceConnected=_CascadedDeviceConnected_Object((1,3,6,1,4,1,13742,8,1,1,1,15),_CascadedDeviceConnected_Type())
cascadedDeviceConnected.setMaxAccess(_D)
if mibBuilder.loadTexts:cascadedDeviceConnected.setStatus(_B)
_PeripheralDevicesAutoManagement_Type=TruthValue
_PeripheralDevicesAutoManagement_Object=MibScalar
peripheralDevicesAutoManagement=_PeripheralDevicesAutoManagement_Object((1,3,6,1,4,1,13742,8,1,1,1,16),_PeripheralDevicesAutoManagement_Type())
peripheralDevicesAutoManagement.setMaxAccess(_L)
if mibBuilder.loadTexts:peripheralDevicesAutoManagement.setStatus(_B)
_SynchronizeWithNTPServer_Type=TruthValue
_SynchronizeWithNTPServer_Object=MibScalar
synchronizeWithNTPServer=_SynchronizeWithNTPServer_Object((1,3,6,1,4,1,13742,8,1,1,1,17),_SynchronizeWithNTPServer_Type())
synchronizeWithNTPServer.setMaxAccess(_L)
if mibBuilder.loadTexts:synchronizeWithNTPServer.setStatus(_B)
_UseDHCPProvidedNTPServer_Type=TruthValue
_UseDHCPProvidedNTPServer_Object=MibScalar
useDHCPProvidedNTPServer=_UseDHCPProvidedNTPServer_Object((1,3,6,1,4,1,13742,8,1,1,1,18),_UseDHCPProvidedNTPServer_Type())
useDHCPProvidedNTPServer.setMaxAccess(_L)
if mibBuilder.loadTexts:useDHCPProvidedNTPServer.setStatus(_B)
class _FirstNTPServerAddressType_Type(InetAddressType):defaultValue=1
_FirstNTPServerAddressType_Type.__name__=_Y
_FirstNTPServerAddressType_Object=MibScalar
firstNTPServerAddressType=_FirstNTPServerAddressType_Object((1,3,6,1,4,1,13742,8,1,1,1,19),_FirstNTPServerAddressType_Type())
firstNTPServerAddressType.setMaxAccess(_L)
if mibBuilder.loadTexts:firstNTPServerAddressType.setStatus(_B)
_FirstNTPServerAddress_Type=InetAddress
_FirstNTPServerAddress_Object=MibScalar
firstNTPServerAddress=_FirstNTPServerAddress_Object((1,3,6,1,4,1,13742,8,1,1,1,20),_FirstNTPServerAddress_Type())
firstNTPServerAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:firstNTPServerAddress.setStatus(_B)
class _SecondNTPServerAddressType_Type(InetAddressType):defaultValue=1
_SecondNTPServerAddressType_Type.__name__=_Y
_SecondNTPServerAddressType_Object=MibScalar
secondNTPServerAddressType=_SecondNTPServerAddressType_Object((1,3,6,1,4,1,13742,8,1,1,1,21),_SecondNTPServerAddressType_Type())
secondNTPServerAddressType.setMaxAccess(_L)
if mibBuilder.loadTexts:secondNTPServerAddressType.setStatus(_B)
_SecondNTPServerAddress_Type=InetAddress
_SecondNTPServerAddress_Object=MibScalar
secondNTPServerAddress=_SecondNTPServerAddress_Object((1,3,6,1,4,1,13742,8,1,1,1,22),_SecondNTPServerAddress_Type())
secondNTPServerAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:secondNTPServerAddress.setStatus(_B)
_LogConfiguration_ObjectIdentity=ObjectIdentity
logConfiguration=_LogConfiguration_ObjectIdentity((1,3,6,1,4,1,13742,8,1,1,2))
_DataLogging_Type=TruthValue
_DataLogging_Object=MibScalar
dataLogging=_DataLogging_Object((1,3,6,1,4,1,13742,8,1,1,2,1),_DataLogging_Type())
dataLogging.setMaxAccess(_L)
if mibBuilder.loadTexts:dataLogging.setStatus(_B)
_MeasurementPeriod_Type=Integer32
_MeasurementPeriod_Object=MibScalar
measurementPeriod=_MeasurementPeriod_Object((1,3,6,1,4,1,13742,8,1,1,2,2),_MeasurementPeriod_Type())
measurementPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:measurementPeriod.setStatus(_B)
_MeasurementsPerLogEntry_Type=Integer32
_MeasurementsPerLogEntry_Object=MibScalar
measurementsPerLogEntry=_MeasurementsPerLogEntry_Object((1,3,6,1,4,1,13742,8,1,1,2,3),_MeasurementsPerLogEntry_Type())
measurementsPerLogEntry.setMaxAccess(_L)
if mibBuilder.loadTexts:measurementsPerLogEntry.setStatus(_B)
_LogSize_Type=Integer32
_LogSize_Object=MibScalar
logSize=_LogSize_Object((1,3,6,1,4,1,13742,8,1,1,2,4),_LogSize_Type())
logSize.setMaxAccess(_D)
if mibBuilder.loadTexts:logSize.setStatus(_B)
_DataLoggingEnableForAllSensors_Type=TruthValue
_DataLoggingEnableForAllSensors_Object=MibScalar
dataLoggingEnableForAllSensors=_DataLoggingEnableForAllSensors_Object((1,3,6,1,4,1,13742,8,1,1,2,5),_DataLoggingEnableForAllSensors_Type())
dataLoggingEnableForAllSensors.setMaxAccess(_L)
if mibBuilder.loadTexts:dataLoggingEnableForAllSensors.setStatus(_B)
_ExternalSensors_ObjectIdentity=ObjectIdentity
externalSensors=_ExternalSensors_ObjectIdentity((1,3,6,1,4,1,13742,8,1,2))
_ExternalSensorConfigurationTable_Object=MibTable
externalSensorConfigurationTable=_ExternalSensorConfigurationTable_Object((1,3,6,1,4,1,13742,8,1,2,1))
if mibBuilder.loadTexts:externalSensorConfigurationTable.setStatus(_B)
_ExternalSensorConfigurationEntry_Object=MibTableRow
externalSensorConfigurationEntry=_ExternalSensorConfigurationEntry_Object((1,3,6,1,4,1,13742,8,1,2,1,1))
externalSensorConfigurationEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:externalSensorConfigurationEntry.setStatus(_B)
class _SensorID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_SensorID_Type.__name__=_O
_SensorID_Object=MibTableColumn
sensorID=_SensorID_Object((1,3,6,1,4,1,13742,8,1,2,1,1,1),_SensorID_Type())
sensorID.setMaxAccess(_V)
if mibBuilder.loadTexts:sensorID.setStatus(_B)
_ExternalSensorType_Type=SensorTypeEnumeration
_ExternalSensorType_Object=MibTableColumn
externalSensorType=_ExternalSensorType_Object((1,3,6,1,4,1,13742,8,1,2,1,1,2),_ExternalSensorType_Type())
externalSensorType.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorType.setStatus(_B)
_ExternalSensorSerialNumber_Type=DisplayString
_ExternalSensorSerialNumber_Object=MibTableColumn
externalSensorSerialNumber=_ExternalSensorSerialNumber_Object((1,3,6,1,4,1,13742,8,1,2,1,1,3),_ExternalSensorSerialNumber_Type())
externalSensorSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorSerialNumber.setStatus(_B)
_ExternalSensorName_Type=DisplayString
_ExternalSensorName_Object=MibTableColumn
externalSensorName=_ExternalSensorName_Object((1,3,6,1,4,1,13742,8,1,2,1,1,4),_ExternalSensorName_Type())
externalSensorName.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorName.setStatus(_B)
_ExternalSensorDescription_Type=DisplayString
_ExternalSensorDescription_Object=MibTableColumn
externalSensorDescription=_ExternalSensorDescription_Object((1,3,6,1,4,1,13742,8,1,2,1,1,5),_ExternalSensorDescription_Type())
externalSensorDescription.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorDescription.setStatus(_B)
_ExternalSensorXCoordinate_Type=DisplayString
_ExternalSensorXCoordinate_Object=MibTableColumn
externalSensorXCoordinate=_ExternalSensorXCoordinate_Object((1,3,6,1,4,1,13742,8,1,2,1,1,6),_ExternalSensorXCoordinate_Type())
externalSensorXCoordinate.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorXCoordinate.setStatus(_B)
_ExternalSensorYCoordinate_Type=DisplayString
_ExternalSensorYCoordinate_Object=MibTableColumn
externalSensorYCoordinate=_ExternalSensorYCoordinate_Object((1,3,6,1,4,1,13742,8,1,2,1,1,7),_ExternalSensorYCoordinate_Type())
externalSensorYCoordinate.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorYCoordinate.setStatus(_B)
_ExternalSensorZCoordinate_Type=DisplayString
_ExternalSensorZCoordinate_Object=MibTableColumn
externalSensorZCoordinate=_ExternalSensorZCoordinate_Object((1,3,6,1,4,1,13742,8,1,2,1,1,8),_ExternalSensorZCoordinate_Type())
externalSensorZCoordinate.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorZCoordinate.setStatus(_B)
_ExternalSensorChannelNumber_Type=Integer32
_ExternalSensorChannelNumber_Object=MibTableColumn
externalSensorChannelNumber=_ExternalSensorChannelNumber_Object((1,3,6,1,4,1,13742,8,1,2,1,1,9),_ExternalSensorChannelNumber_Type())
externalSensorChannelNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorChannelNumber.setStatus(_B)
_ExternalOnOffSensorSubtype_Type=SensorTypeEnumeration
_ExternalOnOffSensorSubtype_Object=MibTableColumn
externalOnOffSensorSubtype=_ExternalOnOffSensorSubtype_Object((1,3,6,1,4,1,13742,8,1,2,1,1,10),_ExternalOnOffSensorSubtype_Type())
externalOnOffSensorSubtype.setMaxAccess(_L)
if mibBuilder.loadTexts:externalOnOffSensorSubtype.setStatus(_B)
_ExternalSensorUnits_Type=SensorUnitsEnumeration
_ExternalSensorUnits_Object=MibTableColumn
externalSensorUnits=_ExternalSensorUnits_Object((1,3,6,1,4,1,13742,8,1,2,1,1,11),_ExternalSensorUnits_Type())
externalSensorUnits.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorUnits.setStatus(_B)
_ExternalSensorDecimalDigits_Type=Unsigned32
_ExternalSensorDecimalDigits_Object=MibTableColumn
externalSensorDecimalDigits=_ExternalSensorDecimalDigits_Object((1,3,6,1,4,1,13742,8,1,2,1,1,12),_ExternalSensorDecimalDigits_Type())
externalSensorDecimalDigits.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorDecimalDigits.setStatus(_B)
_ExternalSensorAccuracy_Type=HundredthsOfAPercentage
_ExternalSensorAccuracy_Object=MibTableColumn
externalSensorAccuracy=_ExternalSensorAccuracy_Object((1,3,6,1,4,1,13742,8,1,2,1,1,13),_ExternalSensorAccuracy_Type())
externalSensorAccuracy.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorAccuracy.setStatus(_B)
_ExternalSensorResolution_Type=Unsigned32
_ExternalSensorResolution_Object=MibTableColumn
externalSensorResolution=_ExternalSensorResolution_Object((1,3,6,1,4,1,13742,8,1,2,1,1,14),_ExternalSensorResolution_Type())
externalSensorResolution.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorResolution.setStatus(_B)
_ExternalSensorTolerance_Type=Unsigned32
_ExternalSensorTolerance_Object=MibTableColumn
externalSensorTolerance=_ExternalSensorTolerance_Object((1,3,6,1,4,1,13742,8,1,2,1,1,15),_ExternalSensorTolerance_Type())
externalSensorTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorTolerance.setStatus(_B)
_ExternalSensorMaximum_Type=Integer32
_ExternalSensorMaximum_Object=MibTableColumn
externalSensorMaximum=_ExternalSensorMaximum_Object((1,3,6,1,4,1,13742,8,1,2,1,1,16),_ExternalSensorMaximum_Type())
externalSensorMaximum.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorMaximum.setStatus(_B)
_ExternalSensorMinimum_Type=Integer32
_ExternalSensorMinimum_Object=MibTableColumn
externalSensorMinimum=_ExternalSensorMinimum_Object((1,3,6,1,4,1,13742,8,1,2,1,1,17),_ExternalSensorMinimum_Type())
externalSensorMinimum.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorMinimum.setStatus(_B)
_ExternalSensorHysteresis_Type=Unsigned32
_ExternalSensorHysteresis_Object=MibTableColumn
externalSensorHysteresis=_ExternalSensorHysteresis_Object((1,3,6,1,4,1,13742,8,1,2,1,1,18),_ExternalSensorHysteresis_Type())
externalSensorHysteresis.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorHysteresis.setStatus(_B)
_ExternalSensorStateChangeDelay_Type=Unsigned32
_ExternalSensorStateChangeDelay_Object=MibTableColumn
externalSensorStateChangeDelay=_ExternalSensorStateChangeDelay_Object((1,3,6,1,4,1,13742,8,1,2,1,1,19),_ExternalSensorStateChangeDelay_Type())
externalSensorStateChangeDelay.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorStateChangeDelay.setStatus(_B)
_ExternalSensorLowerCriticalThreshold_Type=Integer32
_ExternalSensorLowerCriticalThreshold_Object=MibTableColumn
externalSensorLowerCriticalThreshold=_ExternalSensorLowerCriticalThreshold_Object((1,3,6,1,4,1,13742,8,1,2,1,1,20),_ExternalSensorLowerCriticalThreshold_Type())
externalSensorLowerCriticalThreshold.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorLowerCriticalThreshold.setStatus(_B)
_ExternalSensorLowerWarningThreshold_Type=Integer32
_ExternalSensorLowerWarningThreshold_Object=MibTableColumn
externalSensorLowerWarningThreshold=_ExternalSensorLowerWarningThreshold_Object((1,3,6,1,4,1,13742,8,1,2,1,1,21),_ExternalSensorLowerWarningThreshold_Type())
externalSensorLowerWarningThreshold.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorLowerWarningThreshold.setStatus(_B)
_ExternalSensorUpperCriticalThreshold_Type=Integer32
_ExternalSensorUpperCriticalThreshold_Object=MibTableColumn
externalSensorUpperCriticalThreshold=_ExternalSensorUpperCriticalThreshold_Object((1,3,6,1,4,1,13742,8,1,2,1,1,22),_ExternalSensorUpperCriticalThreshold_Type())
externalSensorUpperCriticalThreshold.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorUpperCriticalThreshold.setStatus(_B)
_ExternalSensorUpperWarningThreshold_Type=Integer32
_ExternalSensorUpperWarningThreshold_Object=MibTableColumn
externalSensorUpperWarningThreshold=_ExternalSensorUpperWarningThreshold_Object((1,3,6,1,4,1,13742,8,1,2,1,1,23),_ExternalSensorUpperWarningThreshold_Type())
externalSensorUpperWarningThreshold.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorUpperWarningThreshold.setStatus(_B)
class _ExternalSensorEnabledThresholds_Type(Bits):namedValues=NamedValues(*((_w,0),(_x,1),(_y,2),(_z,3)))
_ExternalSensorEnabledThresholds_Type.__name__=_Z
_ExternalSensorEnabledThresholds_Object=MibTableColumn
externalSensorEnabledThresholds=_ExternalSensorEnabledThresholds_Object((1,3,6,1,4,1,13742,8,1,2,1,1,24),_ExternalSensorEnabledThresholds_Type())
externalSensorEnabledThresholds.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorEnabledThresholds.setStatus(_B)
_ExternalSensorPort_Type=DisplayString
_ExternalSensorPort_Object=MibTableColumn
externalSensorPort=_ExternalSensorPort_Object((1,3,6,1,4,1,13742,8,1,2,1,1,25),_ExternalSensorPort_Type())
externalSensorPort.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorPort.setStatus(_B)
_ExternalSensorIsActuator_Type=TruthValue
_ExternalSensorIsActuator_Object=MibTableColumn
externalSensorIsActuator=_ExternalSensorIsActuator_Object((1,3,6,1,4,1,13742,8,1,2,1,1,26),_ExternalSensorIsActuator_Type())
externalSensorIsActuator.setMaxAccess(_D)
if mibBuilder.loadTexts:externalSensorIsActuator.setStatus(_B)
_ExternalSensorAlarmedToNormalDelay_Type=Integer32
_ExternalSensorAlarmedToNormalDelay_Object=MibTableColumn
externalSensorAlarmedToNormalDelay=_ExternalSensorAlarmedToNormalDelay_Object((1,3,6,1,4,1,13742,8,1,2,1,1,27),_ExternalSensorAlarmedToNormalDelay_Type())
externalSensorAlarmedToNormalDelay.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorAlarmedToNormalDelay.setStatus(_B)
_ExternalSensorUseDefaultThresholds_Type=TruthValue
_ExternalSensorUseDefaultThresholds_Object=MibTableColumn
externalSensorUseDefaultThresholds=_ExternalSensorUseDefaultThresholds_Object((1,3,6,1,4,1,13742,8,1,2,1,1,28),_ExternalSensorUseDefaultThresholds_Type())
externalSensorUseDefaultThresholds.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorUseDefaultThresholds.setStatus(_B)
_ExternalSensorTypeDefaultThresholdsTable_Object=MibTable
externalSensorTypeDefaultThresholdsTable=_ExternalSensorTypeDefaultThresholdsTable_Object((1,3,6,1,4,1,13742,8,1,2,4))
if mibBuilder.loadTexts:externalSensorTypeDefaultThresholdsTable.setStatus(_B)
_ExternalSensorTypeDefaultThresholdsEntry_Object=MibTableRow
externalSensorTypeDefaultThresholdsEntry=_ExternalSensorTypeDefaultThresholdsEntry_Object((1,3,6,1,4,1,13742,8,1,2,4,1))
externalSensorTypeDefaultThresholdsEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:externalSensorTypeDefaultThresholdsEntry.setStatus(_B)
_ExternalSensorTypeDefaultHysteresis_Type=Unsigned32
_ExternalSensorTypeDefaultHysteresis_Object=MibTableColumn
externalSensorTypeDefaultHysteresis=_ExternalSensorTypeDefaultHysteresis_Object((1,3,6,1,4,1,13742,8,1,2,4,1,3),_ExternalSensorTypeDefaultHysteresis_Type())
externalSensorTypeDefaultHysteresis.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorTypeDefaultHysteresis.setStatus(_B)
_ExternalSensorTypeDefaultStateChangeDelay_Type=Unsigned32
_ExternalSensorTypeDefaultStateChangeDelay_Object=MibTableColumn
externalSensorTypeDefaultStateChangeDelay=_ExternalSensorTypeDefaultStateChangeDelay_Object((1,3,6,1,4,1,13742,8,1,2,4,1,4),_ExternalSensorTypeDefaultStateChangeDelay_Type())
externalSensorTypeDefaultStateChangeDelay.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorTypeDefaultStateChangeDelay.setStatus(_B)
_ExternalSensorTypeDefaultLowerCriticalThreshold_Type=Integer32
_ExternalSensorTypeDefaultLowerCriticalThreshold_Object=MibTableColumn
externalSensorTypeDefaultLowerCriticalThreshold=_ExternalSensorTypeDefaultLowerCriticalThreshold_Object((1,3,6,1,4,1,13742,8,1,2,4,1,5),_ExternalSensorTypeDefaultLowerCriticalThreshold_Type())
externalSensorTypeDefaultLowerCriticalThreshold.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorTypeDefaultLowerCriticalThreshold.setStatus(_B)
_ExternalSensorTypeDefaultLowerWarningThreshold_Type=Integer32
_ExternalSensorTypeDefaultLowerWarningThreshold_Object=MibTableColumn
externalSensorTypeDefaultLowerWarningThreshold=_ExternalSensorTypeDefaultLowerWarningThreshold_Object((1,3,6,1,4,1,13742,8,1,2,4,1,6),_ExternalSensorTypeDefaultLowerWarningThreshold_Type())
externalSensorTypeDefaultLowerWarningThreshold.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorTypeDefaultLowerWarningThreshold.setStatus(_B)
_ExternalSensorTypeDefaultUpperCriticalThreshold_Type=Integer32
_ExternalSensorTypeDefaultUpperCriticalThreshold_Object=MibTableColumn
externalSensorTypeDefaultUpperCriticalThreshold=_ExternalSensorTypeDefaultUpperCriticalThreshold_Object((1,3,6,1,4,1,13742,8,1,2,4,1,7),_ExternalSensorTypeDefaultUpperCriticalThreshold_Type())
externalSensorTypeDefaultUpperCriticalThreshold.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorTypeDefaultUpperCriticalThreshold.setStatus(_B)
_ExternalSensorTypeDefaultUpperWarningThreshold_Type=Integer32
_ExternalSensorTypeDefaultUpperWarningThreshold_Object=MibTableColumn
externalSensorTypeDefaultUpperWarningThreshold=_ExternalSensorTypeDefaultUpperWarningThreshold_Object((1,3,6,1,4,1,13742,8,1,2,4,1,8),_ExternalSensorTypeDefaultUpperWarningThreshold_Type())
externalSensorTypeDefaultUpperWarningThreshold.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorTypeDefaultUpperWarningThreshold.setStatus(_B)
class _ExternalSensorTypeDefaultEnabledThresholds_Type(Bits):namedValues=NamedValues(*((_w,0),(_x,1),(_y,2),(_z,3)))
_ExternalSensorTypeDefaultEnabledThresholds_Type.__name__=_Z
_ExternalSensorTypeDefaultEnabledThresholds_Object=MibTableColumn
externalSensorTypeDefaultEnabledThresholds=_ExternalSensorTypeDefaultEnabledThresholds_Object((1,3,6,1,4,1,13742,8,1,2,4,1,9),_ExternalSensorTypeDefaultEnabledThresholds_Type())
externalSensorTypeDefaultEnabledThresholds.setMaxAccess(_L)
if mibBuilder.loadTexts:externalSensorTypeDefaultEnabledThresholds.setStatus(_B)
_PeripheralDevicePackageTable_Object=MibTable
peripheralDevicePackageTable=_PeripheralDevicePackageTable_Object((1,3,6,1,4,1,13742,8,1,2,5))
if mibBuilder.loadTexts:peripheralDevicePackageTable.setStatus(_B)
_PeripheralDevicePackageEntry_Object=MibTableRow
peripheralDevicePackageEntry=_PeripheralDevicePackageEntry_Object((1,3,6,1,4,1,13742,8,1,2,5,1))
peripheralDevicePackageEntry.setIndexNames((0,_A,_A0))
if mibBuilder.loadTexts:peripheralDevicePackageEntry.setStatus(_B)
class _PeripheralDevicePackageId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_PeripheralDevicePackageId_Type.__name__=_O
_PeripheralDevicePackageId_Object=MibTableColumn
peripheralDevicePackageId=_PeripheralDevicePackageId_Object((1,3,6,1,4,1,13742,8,1,2,5,1,1),_PeripheralDevicePackageId_Type())
peripheralDevicePackageId.setMaxAccess(_V)
if mibBuilder.loadTexts:peripheralDevicePackageId.setStatus(_B)
_PeripheralDevicePackageSerialNumber_Type=DisplayString
_PeripheralDevicePackageSerialNumber_Object=MibTableColumn
peripheralDevicePackageSerialNumber=_PeripheralDevicePackageSerialNumber_Object((1,3,6,1,4,1,13742,8,1,2,5,1,3),_PeripheralDevicePackageSerialNumber_Type())
peripheralDevicePackageSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:peripheralDevicePackageSerialNumber.setStatus(_B)
_PeripheralDevicePackageModel_Type=DisplayString
_PeripheralDevicePackageModel_Object=MibTableColumn
peripheralDevicePackageModel=_PeripheralDevicePackageModel_Object((1,3,6,1,4,1,13742,8,1,2,5,1,4),_PeripheralDevicePackageModel_Type())
peripheralDevicePackageModel.setMaxAccess(_D)
if mibBuilder.loadTexts:peripheralDevicePackageModel.setStatus(_B)
_PeripheralDevicePackageFirmwareVersion_Type=DisplayString
_PeripheralDevicePackageFirmwareVersion_Object=MibTableColumn
peripheralDevicePackageFirmwareVersion=_PeripheralDevicePackageFirmwareVersion_Object((1,3,6,1,4,1,13742,8,1,2,5,1,5),_PeripheralDevicePackageFirmwareVersion_Type())
peripheralDevicePackageFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:peripheralDevicePackageFirmwareVersion.setStatus(_B)
_PeripheralDevicePackageMinFirmwareVersion_Type=DisplayString
_PeripheralDevicePackageMinFirmwareVersion_Object=MibTableColumn
peripheralDevicePackageMinFirmwareVersion=_PeripheralDevicePackageMinFirmwareVersion_Object((1,3,6,1,4,1,13742,8,1,2,5,1,6),_PeripheralDevicePackageMinFirmwareVersion_Type())
peripheralDevicePackageMinFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:peripheralDevicePackageMinFirmwareVersion.setStatus(_B)
_PeripheralDevicePackageFirmwareTimeStamp_Type=Unsigned32
_PeripheralDevicePackageFirmwareTimeStamp_Object=MibTableColumn
peripheralDevicePackageFirmwareTimeStamp=_PeripheralDevicePackageFirmwareTimeStamp_Object((1,3,6,1,4,1,13742,8,1,2,5,1,7),_PeripheralDevicePackageFirmwareTimeStamp_Type())
peripheralDevicePackageFirmwareTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:peripheralDevicePackageFirmwareTimeStamp.setStatus(_B)
_PeripheralDevicePackagePosition_Type=DisplayString
_PeripheralDevicePackagePosition_Object=MibTableColumn
peripheralDevicePackagePosition=_PeripheralDevicePackagePosition_Object((1,3,6,1,4,1,13742,8,1,2,5,1,8),_PeripheralDevicePackagePosition_Type())
peripheralDevicePackagePosition.setMaxAccess(_D)
if mibBuilder.loadTexts:peripheralDevicePackagePosition.setStatus(_B)
_PeripheralDevicePackageState_Type=DisplayString
_PeripheralDevicePackageState_Object=MibTableColumn
peripheralDevicePackageState=_PeripheralDevicePackageState_Object((1,3,6,1,4,1,13742,8,1,2,5,1,9),_PeripheralDevicePackageState_Type())
peripheralDevicePackageState.setMaxAccess(_D)
if mibBuilder.loadTexts:peripheralDevicePackageState.setStatus(_B)
_ServerReachability_ObjectIdentity=ObjectIdentity
serverReachability=_ServerReachability_ObjectIdentity((1,3,6,1,4,1,13742,8,1,3))
_ServerReachabilityTable_Object=MibTable
serverReachabilityTable=_ServerReachabilityTable_Object((1,3,6,1,4,1,13742,8,1,3,1))
if mibBuilder.loadTexts:serverReachabilityTable.setStatus(_B)
_ServerReachabilityEntry_Object=MibTableRow
serverReachabilityEntry=_ServerReachabilityEntry_Object((1,3,6,1,4,1,13742,8,1,3,1,1))
serverReachabilityEntry.setIndexNames((0,_A,'serverID'))
if mibBuilder.loadTexts:serverReachabilityEntry.setStatus(_B)
class _ServerID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ServerID_Type.__name__=_O
_ServerID_Object=MibTableColumn
serverID=_ServerID_Object((1,3,6,1,4,1,13742,8,1,3,1,1,1),_ServerID_Type())
serverID.setMaxAccess(_V)
if mibBuilder.loadTexts:serverID.setStatus(_B)
_ServerIPAddress_Type=DisplayString
_ServerIPAddress_Object=MibTableColumn
serverIPAddress=_ServerIPAddress_Object((1,3,6,1,4,1,13742,8,1,3,1,1,2),_ServerIPAddress_Type())
serverIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:serverIPAddress.setStatus(_B)
_ServerPingEnabled_Type=TruthValue
_ServerPingEnabled_Object=MibTableColumn
serverPingEnabled=_ServerPingEnabled_Object((1,3,6,1,4,1,13742,8,1,3,1,1,3),_ServerPingEnabled_Type())
serverPingEnabled.setMaxAccess(_L)
if mibBuilder.loadTexts:serverPingEnabled.setStatus(_B)
_Measurements_ObjectIdentity=ObjectIdentity
measurements=_Measurements_ObjectIdentity((1,3,6,1,4,1,13742,8,2))
_MeasurementsExternalSensor_ObjectIdentity=ObjectIdentity
measurementsExternalSensor=_MeasurementsExternalSensor_ObjectIdentity((1,3,6,1,4,1,13742,8,2,1))
_ExternalSensorMeasurementsTable_Object=MibTable
externalSensorMeasurementsTable=_ExternalSensorMeasurementsTable_Object((1,3,6,1,4,1,13742,8,2,1,1))
if mibBuilder.loadTexts:externalSensorMeasurementsTable.setStatus(_B)
_ExternalSensorMeasurementsEntry_Object=MibTableRow
externalSensorMeasurementsEntry=_ExternalSensorMeasurementsEntry_Object((1,3,6,1,4,1,13742,8,2,1,1,1))
externalSensorMeasurementsEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:externalSensorMeasurementsEntry.setStatus(_B)
_MeasurementsExternalSensorIsAvailable_Type=TruthValue
_MeasurementsExternalSensorIsAvailable_Object=MibTableColumn
measurementsExternalSensorIsAvailable=_MeasurementsExternalSensorIsAvailable_Object((1,3,6,1,4,1,13742,8,2,1,1,1,1),_MeasurementsExternalSensorIsAvailable_Type())
measurementsExternalSensorIsAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:measurementsExternalSensorIsAvailable.setStatus(_B)
_MeasurementsExternalSensorState_Type=SensorStateEnumeration
_MeasurementsExternalSensorState_Object=MibTableColumn
measurementsExternalSensorState=_MeasurementsExternalSensorState_Object((1,3,6,1,4,1,13742,8,2,1,1,1,2),_MeasurementsExternalSensorState_Type())
measurementsExternalSensorState.setMaxAccess(_D)
if mibBuilder.loadTexts:measurementsExternalSensorState.setStatus(_B)
_MeasurementsExternalSensorValue_Type=Integer32
_MeasurementsExternalSensorValue_Object=MibTableColumn
measurementsExternalSensorValue=_MeasurementsExternalSensorValue_Object((1,3,6,1,4,1,13742,8,2,1,1,1,3),_MeasurementsExternalSensorValue_Type())
measurementsExternalSensorValue.setMaxAccess(_D)
if mibBuilder.loadTexts:measurementsExternalSensorValue.setStatus(_B)
_MeasurementsExternalSensorTimeStamp_Type=Unsigned32
_MeasurementsExternalSensorTimeStamp_Object=MibTableColumn
measurementsExternalSensorTimeStamp=_MeasurementsExternalSensorTimeStamp_Object((1,3,6,1,4,1,13742,8,2,1,1,1,4),_MeasurementsExternalSensorTimeStamp_Type())
measurementsExternalSensorTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:measurementsExternalSensorTimeStamp.setStatus(_B)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,13742,8,3))
_Compliances_ObjectIdentity=ObjectIdentity
compliances=_Compliances_ObjectIdentity((1,3,6,1,4,1,13742,8,3,1))
_Groups_ObjectIdentity=ObjectIdentity
groups=_Groups_ObjectIdentity((1,3,6,1,4,1,13742,8,3,2))
_Log_ObjectIdentity=ObjectIdentity
log=_Log_ObjectIdentity((1,3,6,1,4,1,13742,8,4))
_LogUnit_ObjectIdentity=ObjectIdentity
logUnit=_LogUnit_ObjectIdentity((1,3,6,1,4,1,13742,8,4,1))
_OldestLogID_Type=Integer32
_OldestLogID_Object=MibScalar
oldestLogID=_OldestLogID_Object((1,3,6,1,4,1,13742,8,4,1,1),_OldestLogID_Type())
oldestLogID.setMaxAccess(_D)
if mibBuilder.loadTexts:oldestLogID.setStatus(_B)
_NewestLogID_Type=Integer32
_NewestLogID_Object=MibScalar
newestLogID=_NewestLogID_Object((1,3,6,1,4,1,13742,8,4,1,2),_NewestLogID_Type())
newestLogID.setMaxAccess(_D)
if mibBuilder.loadTexts:newestLogID.setStatus(_B)
_LogTimeStampTable_Object=MibTable
logTimeStampTable=_LogTimeStampTable_Object((1,3,6,1,4,1,13742,8,4,1,3))
if mibBuilder.loadTexts:logTimeStampTable.setStatus(_B)
_LogTimeStampEntry_Object=MibTableRow
logTimeStampEntry=_LogTimeStampEntry_Object((1,3,6,1,4,1,13742,8,4,1,3,1))
logTimeStampEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:logTimeStampEntry.setStatus(_B)
class _LogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_LogIndex_Type.__name__=_O
_LogIndex_Object=MibTableColumn
logIndex=_LogIndex_Object((1,3,6,1,4,1,13742,8,4,1,3,1,1),_LogIndex_Type())
logIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:logIndex.setStatus(_B)
_LogTimeStamp_Type=Unsigned32
_LogTimeStamp_Object=MibTableColumn
logTimeStamp=_LogTimeStamp_Object((1,3,6,1,4,1,13742,8,4,1,3,1,2),_LogTimeStamp_Type())
logTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:logTimeStamp.setStatus(_B)
_LogExternalSensor_ObjectIdentity=ObjectIdentity
logExternalSensor=_LogExternalSensor_ObjectIdentity((1,3,6,1,4,1,13742,8,4,2))
_ExternalSensorLogTable_Object=MibTable
externalSensorLogTable=_ExternalSensorLogTable_Object((1,3,6,1,4,1,13742,8,4,2,1))
if mibBuilder.loadTexts:externalSensorLogTable.setStatus(_B)
_ExternalSensorLogEntry_Object=MibTableRow
externalSensorLogEntry=_ExternalSensorLogEntry_Object((1,3,6,1,4,1,13742,8,4,2,1,1))
externalSensorLogEntry.setIndexNames((0,_A,_R),(0,_A,_b))
if mibBuilder.loadTexts:externalSensorLogEntry.setStatus(_B)
_LogExternalSensorDataAvailable_Type=TruthValue
_LogExternalSensorDataAvailable_Object=MibTableColumn
logExternalSensorDataAvailable=_LogExternalSensorDataAvailable_Object((1,3,6,1,4,1,13742,8,4,2,1,1,2),_LogExternalSensorDataAvailable_Type())
logExternalSensorDataAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:logExternalSensorDataAvailable.setStatus(_B)
_LogExternalSensorState_Type=SensorStateEnumeration
_LogExternalSensorState_Object=MibTableColumn
logExternalSensorState=_LogExternalSensorState_Object((1,3,6,1,4,1,13742,8,4,2,1,1,3),_LogExternalSensorState_Type())
logExternalSensorState.setMaxAccess(_D)
if mibBuilder.loadTexts:logExternalSensorState.setStatus(_B)
_LogExternalSensorAvgValue_Type=Integer32
_LogExternalSensorAvgValue_Object=MibTableColumn
logExternalSensorAvgValue=_LogExternalSensorAvgValue_Object((1,3,6,1,4,1,13742,8,4,2,1,1,4),_LogExternalSensorAvgValue_Type())
logExternalSensorAvgValue.setMaxAccess(_D)
if mibBuilder.loadTexts:logExternalSensorAvgValue.setStatus(_B)
_LogExternalSensorMaxValue_Type=Integer32
_LogExternalSensorMaxValue_Object=MibTableColumn
logExternalSensorMaxValue=_LogExternalSensorMaxValue_Object((1,3,6,1,4,1,13742,8,4,2,1,1,5),_LogExternalSensorMaxValue_Type())
logExternalSensorMaxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:logExternalSensorMaxValue.setStatus(_B)
_LogExternalSensorMinValue_Type=Integer32
_LogExternalSensorMinValue_Object=MibTableColumn
logExternalSensorMinValue=_LogExternalSensorMinValue_Object((1,3,6,1,4,1,13742,8,4,2,1,1,6),_LogExternalSensorMinValue_Type())
logExternalSensorMinValue.setMaxAccess(_D)
if mibBuilder.loadTexts:logExternalSensorMinValue.setStatus(_B)
_Control_ObjectIdentity=ObjectIdentity
control=_Control_ObjectIdentity((1,3,6,1,4,1,13742,8,5))
_ActuatorControl_ObjectIdentity=ObjectIdentity
actuatorControl=_ActuatorControl_ObjectIdentity((1,3,6,1,4,1,13742,8,5,1))
_ActuatorControlTable_Object=MibTable
actuatorControlTable=_ActuatorControlTable_Object((1,3,6,1,4,1,13742,8,5,1,1))
if mibBuilder.loadTexts:actuatorControlTable.setStatus(_B)
_ActuatorControlEntry_Object=MibTableRow
actuatorControlEntry=_ActuatorControlEntry_Object((1,3,6,1,4,1,13742,8,5,1,1,1))
actuatorControlEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:actuatorControlEntry.setStatus(_B)
_ActuatorState_Type=SensorStateEnumeration
_ActuatorState_Object=MibTableColumn
actuatorState=_ActuatorState_Object((1,3,6,1,4,1,13742,8,5,1,1,1,1),_ActuatorState_Type())
actuatorState.setMaxAccess(_L)
if mibBuilder.loadTexts:actuatorState.setStatus(_B)
configGroup=ObjectGroup((1,3,6,1,4,1,13742,8,3,2,1))
configGroup.setObjects(*((_A,_A1),(_A,_I),(_A,_J),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,'model'),(_A,_E),(_A,_A6),(_A,_A7),(_A,_a),(_A,_c),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_d),(_A,_e),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_P),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,'logSize'),(_A,_Ah),(_A,_f),(_A,_Ai),(_A,_g),(_A,_Aj),(_A,_Ak),(_A,_h),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At)))
if mibBuilder.loadTexts:configGroup.setStatus(_B)
measurementsGroup=ObjectGroup((1,3,6,1,4,1,13742,8,3,2,2))
measurementsGroup.setObjects(*((_A,_Au),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:measurementsGroup.setStatus(_B)
trapInformationGroup=ObjectGroup((1,3,6,1,4,1,13742,8,3,2,3))
trapInformationGroup.setObjects(*((_A,_M),(_A,_Q),(_A,_S),(_A,_T),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_U),(_A,_q),(_A,_r),(_A,_s),(_A,_W),(_A,_X),(_A,_t),(_A,_u),(_A,_K),(_A,_v)))
if mibBuilder.loadTexts:trapInformationGroup.setStatus(_B)
logGroup=ObjectGroup((1,3,6,1,4,1,13742,8,3,2,5))
logGroup.setObjects(*((_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3)))
if mibBuilder.loadTexts:logGroup.setStatus(_B)
controlGroup=ObjectGroup((1,3,6,1,4,1,13742,8,3,2,6))
controlGroup.setObjects((_A,_B4))
if mibBuilder.loadTexts:controlGroup.setStatus(_B)
systemStarted=NotificationType((1,3,6,1,4,1,13742,8,0,1))
systemStarted.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:systemStarted.setStatus(_B)
systemReset=NotificationType((1,3,6,1,4,1,13742,8,0,2))
systemReset.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:systemReset.setStatus(_B)
userLogin=NotificationType((1,3,6,1,4,1,13742,8,0,3))
userLogin.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userLogin.setStatus(_B)
userLogout=NotificationType((1,3,6,1,4,1,13742,8,0,4))
userLogout.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userLogout.setStatus(_B)
userAuthenticationFailure=NotificationType((1,3,6,1,4,1,13742,8,0,5))
userAuthenticationFailure.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userAuthenticationFailure.setStatus(_B)
userSessionTimeout=NotificationType((1,3,6,1,4,1,13742,8,0,6))
userSessionTimeout.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userSessionTimeout.setStatus(_B)
userAdded=NotificationType((1,3,6,1,4,1,13742,8,0,7))
userAdded.setObjects(*((_A,_E),(_A,_M),(_A,_Q),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userAdded.setStatus(_B)
userModified=NotificationType((1,3,6,1,4,1,13742,8,0,8))
userModified.setObjects(*((_A,_E),(_A,_M),(_A,_Q),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userModified.setStatus(_B)
userDeleted=NotificationType((1,3,6,1,4,1,13742,8,0,9))
userDeleted.setObjects(*((_A,_E),(_A,_M),(_A,_Q),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userDeleted.setStatus(_B)
roleAdded=NotificationType((1,3,6,1,4,1,13742,8,0,10))
roleAdded.setObjects(*((_A,_E),(_A,_M),(_A,_T),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:roleAdded.setStatus(_B)
roleModified=NotificationType((1,3,6,1,4,1,13742,8,0,11))
roleModified.setObjects(*((_A,_E),(_A,_M),(_A,_T),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:roleModified.setStatus(_B)
roleDeleted=NotificationType((1,3,6,1,4,1,13742,8,0,12))
roleDeleted.setObjects(*((_A,_E),(_A,_M),(_A,_T),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:roleDeleted.setStatus(_B)
deviceUpdateStarted=NotificationType((1,3,6,1,4,1,13742,8,0,13))
deviceUpdateStarted.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_A,_S),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:deviceUpdateStarted.setStatus(_B)
deviceUpdateCompleted=NotificationType((1,3,6,1,4,1,13742,8,0,14))
deviceUpdateCompleted.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_A,_S),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:deviceUpdateCompleted.setStatus(_B)
userBlocked=NotificationType((1,3,6,1,4,1,13742,8,0,15))
userBlocked.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userBlocked.setStatus(_B)
userPasswordChanged=NotificationType((1,3,6,1,4,1,13742,8,0,16))
userPasswordChanged.setObjects(*((_A,_E),(_A,_M),(_A,_Q),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userPasswordChanged.setStatus(_B)
passwordSettingsChanged=NotificationType((1,3,6,1,4,1,13742,8,0,17))
passwordSettingsChanged.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:passwordSettingsChanged.setStatus(_B)
firmwareValidationFailed=NotificationType((1,3,6,1,4,1,13742,8,0,18))
firmwareValidationFailed.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:firmwareValidationFailed.setStatus(_B)
logFileCleared=NotificationType((1,3,6,1,4,1,13742,8,0,19))
logFileCleared.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:logFileCleared.setStatus(_B)
bulkConfigurationSaved=NotificationType((1,3,6,1,4,1,13742,8,0,20))
bulkConfigurationSaved.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:bulkConfigurationSaved.setStatus(_B)
bulkConfigurationCopied=NotificationType((1,3,6,1,4,1,13742,8,0,21))
bulkConfigurationCopied.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:bulkConfigurationCopied.setStatus(_B)
externalSensorStateChange=NotificationType((1,3,6,1,4,1,13742,8,0,22))
externalSensorStateChange.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_m),(_A,_n),(_A,_k),(_A,_j),(_A,_i),(_A,_l),(_A,_c),(_A,_e),(_A,_d),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:externalSensorStateChange.setStatus(_B)
smtpMessageTransmissionFailure=NotificationType((1,3,6,1,4,1,13742,8,0,23))
smtpMessageTransmissionFailure.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_o),(_A,_p),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:smtpMessageTransmissionFailure.setStatus(_B)
ldapError=NotificationType((1,3,6,1,4,1,13742,8,0,24))
ldapError.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_U),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:ldapError.setStatus(_B)
deviceUpdateFailed=NotificationType((1,3,6,1,4,1,13742,8,0,25))
deviceUpdateFailed.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_A,_S),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:deviceUpdateFailed.setStatus(_B)
pingServerEnabled=NotificationType((1,3,6,1,4,1,13742,8,0,26))
pingServerEnabled.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_A,_P),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pingServerEnabled.setStatus(_B)
pingServerDisabled=NotificationType((1,3,6,1,4,1,13742,8,0,27))
pingServerDisabled.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_A,_P),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pingServerDisabled.setStatus(_B)
serverNotReachable=NotificationType((1,3,6,1,4,1,13742,8,0,28))
serverNotReachable.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_P),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:serverNotReachable.setStatus(_B)
serverReachable=NotificationType((1,3,6,1,4,1,13742,8,0,29))
serverReachable.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_P),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:serverReachable.setStatus(_B)
deviceIdentificationChanged=NotificationType((1,3,6,1,4,1,13742,8,0,30))
deviceIdentificationChanged.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_q),(_A,_r),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:deviceIdentificationChanged.setStatus(_B)
usbSlaveConnected=NotificationType((1,3,6,1,4,1,13742,8,0,31))
usbSlaveConnected.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:usbSlaveConnected.setStatus(_B)
usbSlaveDisconnected=NotificationType((1,3,6,1,4,1,13742,8,0,32))
usbSlaveDisconnected.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:usbSlaveDisconnected.setStatus(_B)
lhxSupportChanged=NotificationType((1,3,6,1,4,1,13742,8,0,33))
lhxSupportChanged.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G),(_A,_s)))
if mibBuilder.loadTexts:lhxSupportChanged.setStatus(_B)
userAcceptedRestrictedServiceAgreement=NotificationType((1,3,6,1,4,1,13742,8,0,34))
userAcceptedRestrictedServiceAgreement.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userAcceptedRestrictedServiceAgreement.setStatus(_B)
userDeclinedRestrictedServiceAgreement=NotificationType((1,3,6,1,4,1,13742,8,0,35))
userDeclinedRestrictedServiceAgreement.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:userDeclinedRestrictedServiceAgreement.setStatus(_B)
deviceSettingsSaved=NotificationType((1,3,6,1,4,1,13742,8,0,36))
deviceSettingsSaved.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:deviceSettingsSaved.setStatus(_B)
deviceSettingsRestored=NotificationType((1,3,6,1,4,1,13742,8,0,37))
deviceSettingsRestored.setObjects(*((_A,_E),(_A,_M),(_A,_I),(_A,_J),(_A,_K),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:deviceSettingsRestored.setStatus(_B)
webcamInserted=NotificationType((1,3,6,1,4,1,13742,8,0,38))
webcamInserted.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_W),(_A,_X),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:webcamInserted.setStatus(_B)
webcamRemoved=NotificationType((1,3,6,1,4,1,13742,8,0,39))
webcamRemoved.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_W),(_A,_X),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:webcamRemoved.setStatus(_B)
serverConnectivityUnrecoverable=NotificationType((1,3,6,1,4,1,13742,8,0,40))
serverConnectivityUnrecoverable.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_P),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:serverConnectivityUnrecoverable.setStatus(_B)
radiusError=NotificationType((1,3,6,1,4,1,13742,8,0,41))
radiusError.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_U),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:radiusError.setStatus(_B)
serverReachabilityError=NotificationType((1,3,6,1,4,1,13742,8,0,42))
serverReachabilityError.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_P),(_A,_U),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:serverReachabilityError.setStatus(_B)
unknownPeripheralDeviceAttached=NotificationType((1,3,6,1,4,1,13742,8,0,43))
unknownPeripheralDeviceAttached.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_t),(_A,_h),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:unknownPeripheralDeviceAttached.setStatus(_B)
peripheralDeviceFirmwareUpdate=NotificationType((1,3,6,1,4,1,13742,8,0,44))
peripheralDeviceFirmwareUpdate.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_f),(_A,_u),(_A,_g),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:peripheralDeviceFirmwareUpdate.setStatus(_B)
smsMessageTransmissionFailure=NotificationType((1,3,6,1,4,1,13742,8,0,45))
smsMessageTransmissionFailure.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_v),(_C,_F),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:smsMessageTransmissionFailure.setStatus(_B)
trapsGroup=NotificationGroup((1,3,6,1,4,1,13742,8,3,2,4))
trapsGroup.setObjects(*((_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG),(_A,_BH),(_A,_BI),(_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM),(_A,_BN),(_A,_BO),(_A,_BP),(_A,_BQ),(_A,_BR),(_A,_BS),(_A,_BT),(_A,_BU),(_A,_BV),(_A,_BW),(_A,_BX),(_A,_BY),(_A,_BZ),(_A,_Ba),(_A,_Bb),(_A,_Bc),(_A,_Bd),(_A,_Be),(_A,_Bf),(_A,_Bg),(_A,_Bh),(_A,_Bi),(_A,_Bj),(_A,_Bk),(_A,_Bl),(_A,_Bm),(_A,_Bn)))
if mibBuilder.loadTexts:trapsGroup.setStatus(_B)
complianceRev1=ModuleCompliance((1,3,6,1,4,1,13742,8,3,1,1))
complianceRev1.setObjects(*((_A,_Bo),(_A,_Bp),(_A,_Bq),(_A,_Br),(_A,'logGroup'),(_A,_Bs)))
if mibBuilder.loadTexts:complianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SensorTypeEnumeration':SensorTypeEnumeration,'SensorStateEnumeration':SensorStateEnumeration,'SensorUnitsEnumeration':SensorUnitsEnumeration,'ExternalSensorsZCoordinateUnitsEnumeration':ExternalSensorsZCoordinateUnitsEnumeration,'HundredthsOfAPercentage':HundredthsOfAPercentage,'DeviceIdentificationParameterEnumeration':DeviceIdentificationParameterEnumeration,'PeripheralDeviceFirmwareUpdateStateEnumeration':PeripheralDeviceFirmwareUpdateStateEnumeration,'raritan':raritan,'emd':emd,'traps':traps,'trapInformation':trapInformation,_M:userName,_Q:targetUser,_S:imageVersion,_T:roleName,_o:smtpMessageRecipients,_p:smtpServer,_l:oldSensorState,_m:externalSensorNumber,_n:typeOfSensor,_U:errorDescription,_q:deviceChangedParameter,_r:changedParameterNewValue,_s:lhxSupportEnabled,_W:webcamModel,_X:webcamConnectionPort,_t:peripheralDeviceRomcode,_u:peripheralDeviceFirmwareUpdateState,_K:agentInetPortNumber,_v:phoneNumber,_B5:systemStarted,_B6:systemReset,_B7:userLogin,_B8:userLogout,_B9:userAuthenticationFailure,_BA:userSessionTimeout,_BB:userAdded,_BC:userModified,_BD:userDeleted,_BE:roleAdded,_BF:roleModified,_BG:roleDeleted,_BH:deviceUpdateStarted,_BI:deviceUpdateCompleted,_BJ:userBlocked,_BK:userPasswordChanged,_BL:passwordSettingsChanged,_BM:firmwareValidationFailed,_BN:logFileCleared,_BO:bulkConfigurationSaved,_BP:bulkConfigurationCopied,_BQ:externalSensorStateChange,_BR:smtpMessageTransmissionFailure,_BS:ldapError,_BT:deviceUpdateFailed,_BU:pingServerEnabled,_BV:pingServerDisabled,_BW:serverNotReachable,_BX:serverReachable,_BY:deviceIdentificationChanged,_BZ:usbSlaveConnected,_Ba:usbSlaveDisconnected,_Bb:lhxSupportChanged,_Bc:userAcceptedRestrictedServiceAgreement,_Bd:userDeclinedRestrictedServiceAgreement,_Be:deviceSettingsSaved,_Bf:deviceSettingsRestored,_Bg:webcamInserted,_Bh:webcamRemoved,_Bi:serverConnectivityUnrecoverable,_Bj:radiusError,_Bk:serverReachabilityError,_Bl:unknownPeripheralDeviceAttached,_Bm:peripheralDeviceFirmwareUpdate,_Bn:smsMessageTransmissionFailure,'configuration':configuration,'unit':unit,'unitConfiguration':unitConfiguration,_E:deviceName,_A6:hardwareVersion,_A7:firmwareVersion,_A5:utcOffset,_A1:externalSensorCount,_Ac:managedExternalSensorCount,_AS:externalSensorsZCoordinateUnits,_A4:deviceMACAddress,_I:deviceInetAddressType,_J:deviceInetIPAddress,_A2:deviceInetNetmask,_A3:deviceInetGateway,_Ad:serverCount,'model':model,_Ah:cascadedDeviceConnected,_Am:peripheralDevicesAutoManagement,_Ao:synchronizeWithNTPServer,_Ap:useDHCPProvidedNTPServer,_Aq:firstNTPServerAddressType,_Ar:firstNTPServerAddress,_As:secondNTPServerAddressType,_At:secondNTPServerAddress,'logConfiguration':logConfiguration,_Av:dataLogging,_Af:measurementPeriod,_Ag:measurementsPerLogEntry,'logSize':logSize,_Az:dataLoggingEnableForAllSensors,'externalSensors':externalSensors,'externalSensorConfigurationTable':externalSensorConfigurationTable,'externalSensorConfigurationEntry':externalSensorConfigurationEntry,_R:sensorID,_a:externalSensorType,_c:externalSensorSerialNumber,_A8:externalSensorName,_A9:externalSensorDescription,_AA:externalSensorXCoordinate,_AB:externalSensorYCoordinate,_AC:externalSensorZCoordinate,_d:externalSensorChannelNumber,_e:externalOnOffSensorSubtype,_AD:externalSensorUnits,_AE:externalSensorDecimalDigits,_AF:externalSensorAccuracy,_AG:externalSensorResolution,_AH:externalSensorTolerance,_AI:externalSensorMaximum,_AJ:externalSensorMinimum,_AK:externalSensorHysteresis,_AL:externalSensorStateChangeDelay,_AM:externalSensorLowerCriticalThreshold,_AN:externalSensorLowerWarningThreshold,_AO:externalSensorUpperCriticalThreshold,_AP:externalSensorUpperWarningThreshold,_AQ:externalSensorEnabledThresholds,_AR:externalSensorPort,_AT:externalSensorIsActuator,_An:externalSensorAlarmedToNormalDelay,_AU:externalSensorUseDefaultThresholds,'externalSensorTypeDefaultThresholdsTable':externalSensorTypeDefaultThresholdsTable,'externalSensorTypeDefaultThresholdsEntry':externalSensorTypeDefaultThresholdsEntry,_AV:externalSensorTypeDefaultHysteresis,_AW:externalSensorTypeDefaultStateChangeDelay,_AX:externalSensorTypeDefaultLowerCriticalThreshold,_AY:externalSensorTypeDefaultLowerWarningThreshold,_AZ:externalSensorTypeDefaultUpperCriticalThreshold,_Aa:externalSensorTypeDefaultUpperWarningThreshold,_Ab:externalSensorTypeDefaultEnabledThresholds,'peripheralDevicePackageTable':peripheralDevicePackageTable,'peripheralDevicePackageEntry':peripheralDevicePackageEntry,_A0:peripheralDevicePackageId,_f:peripheralDevicePackageSerialNumber,_Ai:peripheralDevicePackageModel,_g:peripheralDevicePackageFirmwareVersion,_Aj:peripheralDevicePackageMinFirmwareVersion,_Ak:peripheralDevicePackageFirmwareTimeStamp,_h:peripheralDevicePackagePosition,_Al:peripheralDevicePackageState,'serverReachability':serverReachability,'serverReachabilityTable':serverReachabilityTable,'serverReachabilityEntry':serverReachabilityEntry,'serverID':serverID,_P:serverIPAddress,_Ae:serverPingEnabled,'measurements':measurements,'measurementsExternalSensor':measurementsExternalSensor,'externalSensorMeasurementsTable':externalSensorMeasurementsTable,'externalSensorMeasurementsEntry':externalSensorMeasurementsEntry,_Au:measurementsExternalSensorIsAvailable,_i:measurementsExternalSensorState,_j:measurementsExternalSensorValue,_k:measurementsExternalSensorTimeStamp,'conformance':conformance,'compliances':compliances,'complianceRev1':complianceRev1,'groups':groups,_Bo:configGroup,_Bp:measurementsGroup,_Bq:trapInformationGroup,_Br:trapsGroup,'logGroup':logGroup,_Bs:controlGroup,'log':log,'logUnit':logUnit,_Aw:oldestLogID,_Ax:newestLogID,'logTimeStampTable':logTimeStampTable,'logTimeStampEntry':logTimeStampEntry,_b:logIndex,_Ay:logTimeStamp,'logExternalSensor':logExternalSensor,'externalSensorLogTable':externalSensorLogTable,'externalSensorLogEntry':externalSensorLogEntry,_A_:logExternalSensorDataAvailable,_B0:logExternalSensorState,_B1:logExternalSensorAvgValue,_B2:logExternalSensorMaxValue,_B3:logExternalSensorMinValue,'control':control,'actuatorControl':actuatorControl,'actuatorControlTable':actuatorControlTable,'actuatorControlEntry':actuatorControlEntry,_B4:actuatorState})