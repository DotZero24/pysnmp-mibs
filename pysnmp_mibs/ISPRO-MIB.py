_U='isDeviceDigitalOutIndex'
_T='isDeviceConfigDigitalInIndex'
_S='isDeviceConfigHumidityIndex'
_R='isDeviceConfigTemperatureIndex'
_Q='isDeviceConfigIndex'
_P='isDeviceMonitorDigitalInIndex'
_O='isDeviceMonitorHumidityIndex'
_N='isDeviceMonitorTemperatureIndex'
_M='isAccessIndex'
_L='isReceiverIndex'
_K='normal'
_J='disable'
_I='unknown'
_H='nothing'
_G='disabled'
_F='ISPRO-MIB'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class IsproEnuEnable(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_G,2)))
class IsproEnuReset(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_H,2)))
class IsproEnuRestart(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),(_H,2)))
class IsproEnuSeverity(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('information',1),('warning',2),('severe',3)))
class IsproEnuAccess(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAccess',1),('readonly',2),('readwrite',3)))
class IsproEnuTempUnit(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('celsius',1),('fahrenheit',2)))
class IsproEnuDateFormat(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dd-mm-yyyy',1),('mm-dd-yyyy',2)))
class IsproEnuTimeZone(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28)));namedValues=NamedValues(*(('gMT-1200',1),('gMT-1100',2),('gMT-1000',3),('gMT-0900',4),('gMT-0800',5),('gMT-0700',6),('gMT-0600',7),('gMT-0500',8),('gMT-0400',9),('gMT-0330',10),('gMT-0300',11),('gMT-0200',12),('gMT-0100',13),('gMT-0000',14),('gMT0100',15),('gMT0200',16),('gMT0300',17),('gMT0330',18),('gMT0400',19),('gMT0500',20),('gMT0530',21),('gMT0600',22),('gMT0700',23),('gMT0800',24),('gMT0900',25),('gMT1000',26),('gMT1100',27),('gMT1200',28)))
class IsproEnuSensorType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('sensorHT',2)))
class IsproEnuThresholdStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),('below-low-warning',4),('below-low-critical',5),('above-high-warning',6),('above-high-critical',7)))
class IsproEnuDigitalStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
class IsproTriggerStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('triggered',2)))
class IsproEnuSensorState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_J,2)))
class IsproEnuTempCalibration(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('temperatureIncrease0Point0',1),('temperatureIncrease0Point5',2),('temperatureIncrease1Point0',3),('temperatureIncrease1Point5',4),('temperatureIncrease2Point0',5),('temperatureIncrease2Point5',6),('temperatureIncrease3Point0',7),('temperatureDecrease0Point5',8),('temperatureDecrease1Point0',9),('temperatureDecrease1Point5',10),('temperatureDecrease2Point0',11),('temperatureDecrease2Point5',12),('temperatureDecrease3Point0',13)))
class IsproEnuHumidityCalibration(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('humidityIncrease0Point0',1),('humidityIncrease0Point5',2),('humidityIncrease1Point0',3),('humidityIncrease1Point5',4),('humidityIncrease2Point0',5),('humidityIncrease2Point5',6),('humidityIncrease3Point0',7),('humidityDecrease0Point5',8),('humidityDecrease1Point0',9),('humidityDecrease1Point5',10),('humidityDecrease2Point0',11),('humidityDecrease2Point5',12),('humidityDecrease3Point0',13)))
class IsproEnuAlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('normalOpen',2),('normalClose',3)))
class IsproEnuOnOff(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
class IsproEnuTurnOnOff(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('turnOn',1),('turnOff',2)))
class IsproEnuPresent(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('present',1),('absent',2)))
class IsproEnuDO(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('digitalOutput1',2),('digitalOutput2',3)))
class IsproEnuHighLow(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
class IsproLogType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('historyLog',1),('extendedLog',2),('deviceEventLog',3),('systemEventLog',4)))
_Jacarta_ObjectIdentity=ObjectIdentity
jacarta=_Jacarta_ObjectIdentity((1,3,6,1,4,1,19011))
_Product_ObjectIdentity=ObjectIdentity
product=_Product_ObjectIdentity((1,3,6,1,4,1,19011,1))
_WebAppliance_ObjectIdentity=ObjectIdentity
webAppliance=_WebAppliance_ObjectIdentity((1,3,6,1,4,1,19011,1,3))
_Ispro_ObjectIdentity=ObjectIdentity
ispro=_Ispro_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2))
_IsObjects_ObjectIdentity=ObjectIdentity
isObjects=_IsObjects_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1))
_IsIdent_ObjectIdentity=ObjectIdentity
isIdent=_IsIdent_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,1))
class _IsIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_IsIdentManufacturer_Type.__name__=_E
_IsIdentManufacturer_Object=MibScalar
isIdentManufacturer=_IsIdentManufacturer_Object((1,3,6,1,4,1,19011,1,3,2,1,1,1),_IsIdentManufacturer_Type())
isIdentManufacturer.setMaxAccess(_D)
if mibBuilder.loadTexts:isIdentManufacturer.setStatus(_A)
class _IsIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_IsIdentModel_Type.__name__=_E
_IsIdentModel_Object=MibScalar
isIdentModel=_IsIdentModel_Object((1,3,6,1,4,1,19011,1,3,2,1,1,2),_IsIdentModel_Type())
isIdentModel.setMaxAccess(_D)
if mibBuilder.loadTexts:isIdentModel.setStatus(_A)
class _IsIdentAgentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_IsIdentAgentSoftwareVersion_Type.__name__=_E
_IsIdentAgentSoftwareVersion_Object=MibScalar
isIdentAgentSoftwareVersion=_IsIdentAgentSoftwareVersion_Object((1,3,6,1,4,1,19011,1,3,2,1,1,3),_IsIdentAgentSoftwareVersion_Type())
isIdentAgentSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:isIdentAgentSoftwareVersion.setStatus(_A)
class _IsIdentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_IsIdentName_Type.__name__=_E
_IsIdentName_Object=MibScalar
isIdentName=_IsIdentName_Object((1,3,6,1,4,1,19011,1,3,2,1,1,4),_IsIdentName_Type())
isIdentName.setMaxAccess(_B)
if mibBuilder.loadTexts:isIdentName.setStatus(_A)
_IsConfig_ObjectIdentity=ObjectIdentity
isConfig=_IsConfig_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,2))
class _IsConfigMibVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_IsConfigMibVersion_Type.__name__=_E
_IsConfigMibVersion_Object=MibScalar
isConfigMibVersion=_IsConfigMibVersion_Object((1,3,6,1,4,1,19011,1,3,2,1,2,1),_IsConfigMibVersion_Type())
isConfigMibVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:isConfigMibVersion.setStatus(_A)
_IsConfigNetwork_ObjectIdentity=ObjectIdentity
isConfigNetwork=_IsConfigNetwork_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,2,2))
_IsConfigIpAddress_Type=IpAddress
_IsConfigIpAddress_Object=MibScalar
isConfigIpAddress=_IsConfigIpAddress_Object((1,3,6,1,4,1,19011,1,3,2,1,2,2,1),_IsConfigIpAddress_Type())
isConfigIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigIpAddress.setStatus(_A)
_IsConfigGateway_Type=IpAddress
_IsConfigGateway_Object=MibScalar
isConfigGateway=_IsConfigGateway_Object((1,3,6,1,4,1,19011,1,3,2,1,2,2,2),_IsConfigGateway_Type())
isConfigGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigGateway.setStatus(_A)
_IsConfigSubnetMask_Type=IpAddress
_IsConfigSubnetMask_Object=MibScalar
isConfigSubnetMask=_IsConfigSubnetMask_Object((1,3,6,1,4,1,19011,1,3,2,1,2,2,3),_IsConfigSubnetMask_Type())
isConfigSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigSubnetMask.setStatus(_A)
_IsConfigDateTime_ObjectIdentity=ObjectIdentity
isConfigDateTime=_IsConfigDateTime_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,2,3))
class _IsConfigDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_IsConfigDate_Type.__name__=_E
_IsConfigDate_Object=MibScalar
isConfigDate=_IsConfigDate_Object((1,3,6,1,4,1,19011,1,3,2,1,2,3,1),_IsConfigDate_Type())
isConfigDate.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigDate.setStatus(_A)
class _IsConfigTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_IsConfigTime_Type.__name__=_E
_IsConfigTime_Object=MibScalar
isConfigTime=_IsConfigTime_Object((1,3,6,1,4,1,19011,1,3,2,1,2,3,2),_IsConfigTime_Type())
isConfigTime.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigTime.setStatus(_A)
_IsConfigTimeFromNtp_Type=IsproEnuEnable
_IsConfigTimeFromNtp_Object=MibScalar
isConfigTimeFromNtp=_IsConfigTimeFromNtp_Object((1,3,6,1,4,1,19011,1,3,2,1,2,3,3),_IsConfigTimeFromNtp_Type())
isConfigTimeFromNtp.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigTimeFromNtp.setStatus(_A)
class _IsConfigNtpIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_IsConfigNtpIpAddress_Type.__name__=_E
_IsConfigNtpIpAddress_Object=MibScalar
isConfigNtpIpAddress=_IsConfigNtpIpAddress_Object((1,3,6,1,4,1,19011,1,3,2,1,2,3,4),_IsConfigNtpIpAddress_Type())
isConfigNtpIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigNtpIpAddress.setStatus(_A)
_IsConfigNtpTimeZone_Type=IsproEnuTimeZone
_IsConfigNtpTimeZone_Object=MibScalar
isConfigNtpTimeZone=_IsConfigNtpTimeZone_Object((1,3,6,1,4,1,19011,1,3,2,1,2,3,5),_IsConfigNtpTimeZone_Type())
isConfigNtpTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigNtpTimeZone.setStatus(_A)
_IsConfigDayLightSaving_Type=IsproEnuEnable
_IsConfigDayLightSaving_Object=MibScalar
isConfigDayLightSaving=_IsConfigDayLightSaving_Object((1,3,6,1,4,1,19011,1,3,2,1,2,3,6),_IsConfigDayLightSaving_Type())
isConfigDayLightSaving.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigDayLightSaving.setStatus(_A)
_IsConfigLog_ObjectIdentity=ObjectIdentity
isConfigLog=_IsConfigLog_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,2,4))
class _IsConfigHistoryLogFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_IsConfigHistoryLogFrequency_Type.__name__=_C
_IsConfigHistoryLogFrequency_Object=MibScalar
isConfigHistoryLogFrequency=_IsConfigHistoryLogFrequency_Object((1,3,6,1,4,1,19011,1,3,2,1,2,4,1),_IsConfigHistoryLogFrequency_Type())
isConfigHistoryLogFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigHistoryLogFrequency.setStatus(_A)
class _IsConfigExtHistoryLogFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,720))
_IsConfigExtHistoryLogFrequency_Type.__name__=_C
_IsConfigExtHistoryLogFrequency_Object=MibScalar
isConfigExtHistoryLogFrequency=_IsConfigExtHistoryLogFrequency_Object((1,3,6,1,4,1,19011,1,3,2,1,2,4,2),_IsConfigExtHistoryLogFrequency_Type())
isConfigExtHistoryLogFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigExtHistoryLogFrequency.setStatus(_A)
_IsConfigConfigurationLog_Type=IsproEnuEnable
_IsConfigConfigurationLog_Object=MibScalar
isConfigConfigurationLog=_IsConfigConfigurationLog_Object((1,3,6,1,4,1,19011,1,3,2,1,2,4,3),_IsConfigConfigurationLog_Type())
isConfigConfigurationLog.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigConfigurationLog.setStatus(_A)
_IsConfigLogType_Type=IsproLogType
_IsConfigLogType_Object=MibScalar
isConfigLogType=_IsConfigLogType_Object((1,3,6,1,4,1,19011,1,3,2,1,2,4,4),_IsConfigLogType_Type())
isConfigLogType.setMaxAccess(_D)
if mibBuilder.loadTexts:isConfigLogType.setStatus(_A)
_IsConfigDhcpState_Type=IsproEnuEnable
_IsConfigDhcpState_Object=MibScalar
isConfigDhcpState=_IsConfigDhcpState_Object((1,3,6,1,4,1,19011,1,3,2,1,2,5),_IsConfigDhcpState_Type())
isConfigDhcpState.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigDhcpState.setStatus(_A)
_IsConfigPingState_Type=IsproEnuEnable
_IsConfigPingState_Object=MibScalar
isConfigPingState=_IsConfigPingState_Object((1,3,6,1,4,1,19011,1,3,2,1,2,6),_IsConfigPingState_Type())
isConfigPingState.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigPingState.setStatus(_A)
_IsConfigTftpState_Type=IsproEnuEnable
_IsConfigTftpState_Object=MibScalar
isConfigTftpState=_IsConfigTftpState_Object((1,3,6,1,4,1,19011,1,3,2,1,2,7),_IsConfigTftpState_Type())
isConfigTftpState.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigTftpState.setStatus(_A)
_IsConfigTelnet_ObjectIdentity=ObjectIdentity
isConfigTelnet=_IsConfigTelnet_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,2,8))
_IsConfigTelnetState_Type=IsproEnuEnable
_IsConfigTelnetState_Object=MibScalar
isConfigTelnetState=_IsConfigTelnetState_Object((1,3,6,1,4,1,19011,1,3,2,1,2,8,1),_IsConfigTelnetState_Type())
isConfigTelnetState.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigTelnetState.setStatus(_A)
class _IsConfigTelnetPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IsConfigTelnetPortNumber_Type.__name__=_C
_IsConfigTelnetPortNumber_Object=MibScalar
isConfigTelnetPortNumber=_IsConfigTelnetPortNumber_Object((1,3,6,1,4,1,19011,1,3,2,1,2,8,2),_IsConfigTelnetPortNumber_Type())
isConfigTelnetPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigTelnetPortNumber.setStatus(_A)
_IsConfigHttp_ObjectIdentity=ObjectIdentity
isConfigHttp=_IsConfigHttp_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,2,9))
_IsConfigHttpState_Type=IsproEnuEnable
_IsConfigHttpState_Object=MibScalar
isConfigHttpState=_IsConfigHttpState_Object((1,3,6,1,4,1,19011,1,3,2,1,2,9,1),_IsConfigHttpState_Type())
isConfigHttpState.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigHttpState.setStatus(_A)
class _IsConfigHttpPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IsConfigHttpPortNumber_Type.__name__=_C
_IsConfigHttpPortNumber_Object=MibScalar
isConfigHttpPortNumber=_IsConfigHttpPortNumber_Object((1,3,6,1,4,1,19011,1,3,2,1,2,9,2),_IsConfigHttpPortNumber_Type())
isConfigHttpPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigHttpPortNumber.setStatus(_A)
_IsConfigHttpSecurity_Type=IsproEnuEnable
_IsConfigHttpSecurity_Object=MibScalar
isConfigHttpSecurity=_IsConfigHttpSecurity_Object((1,3,6,1,4,1,19011,1,3,2,1,2,9,3),_IsConfigHttpSecurity_Type())
isConfigHttpSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigHttpSecurity.setStatus(_A)
_IsConfigSnmp_ObjectIdentity=ObjectIdentity
isConfigSnmp=_IsConfigSnmp_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,2,10))
_IsConfigSnmpState_Type=IsproEnuEnable
_IsConfigSnmpState_Object=MibScalar
isConfigSnmpState=_IsConfigSnmpState_Object((1,3,6,1,4,1,19011,1,3,2,1,2,10,1),_IsConfigSnmpState_Type())
isConfigSnmpState.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigSnmpState.setStatus(_A)
class _IsConfigSnmpPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IsConfigSnmpPortNumber_Type.__name__=_C
_IsConfigSnmpPortNumber_Object=MibScalar
isConfigSnmpPortNumber=_IsConfigSnmpPortNumber_Object((1,3,6,1,4,1,19011,1,3,2,1,2,10,2),_IsConfigSnmpPortNumber_Type())
isConfigSnmpPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigSnmpPortNumber.setStatus(_A)
_IsConfigControl_ObjectIdentity=ObjectIdentity
isConfigControl=_IsConfigControl_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,2,11))
_IsConfigResetToDefault_Type=IsproEnuReset
_IsConfigResetToDefault_Object=MibScalar
isConfigResetToDefault=_IsConfigResetToDefault_Object((1,3,6,1,4,1,19011,1,3,2,1,2,11,1),_IsConfigResetToDefault_Type())
isConfigResetToDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigResetToDefault.setStatus(_A)
_IsConfigRestart_Type=IsproEnuRestart
_IsConfigRestart_Object=MibScalar
isConfigRestart=_IsConfigRestart_Object((1,3,6,1,4,1,19011,1,3,2,1,2,11,2),_IsConfigRestart_Type())
isConfigRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigRestart.setStatus(_A)
_IsConfigTrap_ObjectIdentity=ObjectIdentity
isConfigTrap=_IsConfigTrap_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,2,12))
class _IsConfigTrapRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IsConfigTrapRetryCount_Type.__name__=_C
_IsConfigTrapRetryCount_Object=MibScalar
isConfigTrapRetryCount=_IsConfigTrapRetryCount_Object((1,3,6,1,4,1,19011,1,3,2,1,2,12,1),_IsConfigTrapRetryCount_Type())
isConfigTrapRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigTrapRetryCount.setStatus(_A)
class _IsConfigTrapRetryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IsConfigTrapRetryTime_Type.__name__=_C
_IsConfigTrapRetryTime_Object=MibScalar
isConfigTrapRetryTime=_IsConfigTrapRetryTime_Object((1,3,6,1,4,1,19011,1,3,2,1,2,12,2),_IsConfigTrapRetryTime_Type())
isConfigTrapRetryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigTrapRetryTime.setStatus(_A)
class _IsConfigTrapAckSignature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IsConfigTrapAckSignature_Type.__name__=_C
_IsConfigTrapAckSignature_Object=MibScalar
isConfigTrapAckSignature=_IsConfigTrapAckSignature_Object((1,3,6,1,4,1,19011,1,3,2,1,2,12,3),_IsConfigTrapAckSignature_Type())
isConfigTrapAckSignature.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigTrapAckSignature.setStatus(_A)
class _IsConfigRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_IsConfigRefreshRate_Type.__name__=_C
_IsConfigRefreshRate_Object=MibScalar
isConfigRefreshRate=_IsConfigRefreshRate_Object((1,3,6,1,4,1,19011,1,3,2,1,2,13),_IsConfigRefreshRate_Type())
isConfigRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigRefreshRate.setStatus(_A)
_IsConfigTrapReceiverTable_Object=MibTable
isConfigTrapReceiverTable=_IsConfigTrapReceiverTable_Object((1,3,6,1,4,1,19011,1,3,2,1,2,14))
if mibBuilder.loadTexts:isConfigTrapReceiverTable.setStatus(_A)
_IsConfigTrapReceiverEntry_Object=MibTableRow
isConfigTrapReceiverEntry=_IsConfigTrapReceiverEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,2,14,1))
isConfigTrapReceiverEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:isConfigTrapReceiverEntry.setStatus(_A)
class _IsReceiverIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IsReceiverIndex_Type.__name__=_C
_IsReceiverIndex_Object=MibTableColumn
isReceiverIndex=_IsReceiverIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,2,14,1,1),_IsReceiverIndex_Type())
isReceiverIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isReceiverIndex.setStatus(_A)
_IsReceiverAddr_Type=IpAddress
_IsReceiverAddr_Object=MibTableColumn
isReceiverAddr=_IsReceiverAddr_Object((1,3,6,1,4,1,19011,1,3,2,1,2,14,1,2),_IsReceiverAddr_Type())
isReceiverAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:isReceiverAddr.setStatus(_A)
class _IsReceiverCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_IsReceiverCommunityString_Type.__name__=_E
_IsReceiverCommunityString_Object=MibTableColumn
isReceiverCommunityString=_IsReceiverCommunityString_Object((1,3,6,1,4,1,19011,1,3,2,1,2,14,1,3),_IsReceiverCommunityString_Type())
isReceiverCommunityString.setMaxAccess(_B)
if mibBuilder.loadTexts:isReceiverCommunityString.setStatus(_A)
_IsReceiverSeverityLevel_Type=IsproEnuSeverity
_IsReceiverSeverityLevel_Object=MibTableColumn
isReceiverSeverityLevel=_IsReceiverSeverityLevel_Object((1,3,6,1,4,1,19011,1,3,2,1,2,14,1,4),_IsReceiverSeverityLevel_Type())
isReceiverSeverityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:isReceiverSeverityLevel.setStatus(_A)
class _IsReceiverDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_IsReceiverDescription_Type.__name__=_E
_IsReceiverDescription_Object=MibTableColumn
isReceiverDescription=_IsReceiverDescription_Object((1,3,6,1,4,1,19011,1,3,2,1,2,14,1,5),_IsReceiverDescription_Type())
isReceiverDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:isReceiverDescription.setStatus(_A)
_IsConfigAccessControlTable_Object=MibTable
isConfigAccessControlTable=_IsConfigAccessControlTable_Object((1,3,6,1,4,1,19011,1,3,2,1,2,15))
if mibBuilder.loadTexts:isConfigAccessControlTable.setStatus(_A)
_IsConfigAccessControlEntry_Object=MibTableRow
isConfigAccessControlEntry=_IsConfigAccessControlEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,2,15,1))
isConfigAccessControlEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:isConfigAccessControlEntry.setStatus(_A)
class _IsAccessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IsAccessIndex_Type.__name__=_C
_IsAccessIndex_Object=MibTableColumn
isAccessIndex=_IsAccessIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,2,15,1,1),_IsAccessIndex_Type())
isAccessIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isAccessIndex.setStatus(_A)
_IsAccessControlAddr_Type=IpAddress
_IsAccessControlAddr_Object=MibTableColumn
isAccessControlAddr=_IsAccessControlAddr_Object((1,3,6,1,4,1,19011,1,3,2,1,2,15,1,2),_IsAccessControlAddr_Type())
isAccessControlAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:isAccessControlAddr.setStatus(_A)
class _IsAccessCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IsAccessCommunityString_Type.__name__=_E
_IsAccessCommunityString_Object=MibTableColumn
isAccessCommunityString=_IsAccessCommunityString_Object((1,3,6,1,4,1,19011,1,3,2,1,2,15,1,3),_IsAccessCommunityString_Type())
isAccessCommunityString.setMaxAccess(_B)
if mibBuilder.loadTexts:isAccessCommunityString.setStatus(_A)
_IsAccessControlMode_Type=IsproEnuAccess
_IsAccessControlMode_Object=MibTableColumn
isAccessControlMode=_IsAccessControlMode_Object((1,3,6,1,4,1,19011,1,3,2,1,2,15,1,4),_IsAccessControlMode_Type())
isAccessControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:isAccessControlMode.setStatus(_A)
class _IsAccessAccount_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_IsAccessAccount_Type.__name__=_E
_IsAccessAccount_Object=MibTableColumn
isAccessAccount=_IsAccessAccount_Object((1,3,6,1,4,1,19011,1,3,2,1,2,15,1,5),_IsAccessAccount_Type())
isAccessAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:isAccessAccount.setStatus(_A)
_IsConfigTemperatureUnit_Type=IsproEnuTempUnit
_IsConfigTemperatureUnit_Object=MibScalar
isConfigTemperatureUnit=_IsConfigTemperatureUnit_Object((1,3,6,1,4,1,19011,1,3,2,1,2,16),_IsConfigTemperatureUnit_Type())
isConfigTemperatureUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigTemperatureUnit.setStatus(_A)
_IsConfigDateFormat_Type=IsproEnuDateFormat
_IsConfigDateFormat_Object=MibScalar
isConfigDateFormat=_IsConfigDateFormat_Object((1,3,6,1,4,1,19011,1,3,2,1,2,17),_IsConfigDateFormat_Type())
isConfigDateFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:isConfigDateFormat.setStatus(_A)
_IsDevice_ObjectIdentity=ObjectIdentity
isDevice=_IsDevice_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,3))
_IsDeviceMonitor_ObjectIdentity=ObjectIdentity
isDeviceMonitor=_IsDeviceMonitor_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,3,1))
_IsDeviceMonitorTemperatureTable_Object=MibTable
isDeviceMonitorTemperatureTable=_IsDeviceMonitorTemperatureTable_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,1))
if mibBuilder.loadTexts:isDeviceMonitorTemperatureTable.setStatus(_A)
_IsDeviceMonitorTemperatureEntry_Object=MibTableRow
isDeviceMonitorTemperatureEntry=_IsDeviceMonitorTemperatureEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,1,1))
isDeviceMonitorTemperatureEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:isDeviceMonitorTemperatureEntry.setStatus(_A)
class _IsDeviceMonitorTemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_IsDeviceMonitorTemperatureIndex_Type.__name__=_C
_IsDeviceMonitorTemperatureIndex_Object=MibTableColumn
isDeviceMonitorTemperatureIndex=_IsDeviceMonitorTemperatureIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,1,1,1),_IsDeviceMonitorTemperatureIndex_Type())
isDeviceMonitorTemperatureIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorTemperatureIndex.setStatus(_A)
class _IsDeviceMonitorTemperatureName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IsDeviceMonitorTemperatureName_Type.__name__=_E
_IsDeviceMonitorTemperatureName_Object=MibTableColumn
isDeviceMonitorTemperatureName=_IsDeviceMonitorTemperatureName_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,1,1,2),_IsDeviceMonitorTemperatureName_Type())
isDeviceMonitorTemperatureName.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorTemperatureName.setStatus(_A)
_IsDeviceMonitorTemperature_Type=Integer32
_IsDeviceMonitorTemperature_Object=MibTableColumn
isDeviceMonitorTemperature=_IsDeviceMonitorTemperature_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,1,1,3),_IsDeviceMonitorTemperature_Type())
isDeviceMonitorTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorTemperature.setStatus(_A)
_IsDeviceMonitorTemperatureAlarm_Type=IsproEnuThresholdStatus
_IsDeviceMonitorTemperatureAlarm_Object=MibTableColumn
isDeviceMonitorTemperatureAlarm=_IsDeviceMonitorTemperatureAlarm_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,1,1,4),_IsDeviceMonitorTemperatureAlarm_Type())
isDeviceMonitorTemperatureAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorTemperatureAlarm.setStatus(_A)
_IsDeviceMonitorHumidityTable_Object=MibTable
isDeviceMonitorHumidityTable=_IsDeviceMonitorHumidityTable_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,2))
if mibBuilder.loadTexts:isDeviceMonitorHumidityTable.setStatus(_A)
_IsDeviceMonitorHumidityEntry_Object=MibTableRow
isDeviceMonitorHumidityEntry=_IsDeviceMonitorHumidityEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,2,1))
isDeviceMonitorHumidityEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:isDeviceMonitorHumidityEntry.setStatus(_A)
class _IsDeviceMonitorHumidityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_IsDeviceMonitorHumidityIndex_Type.__name__=_C
_IsDeviceMonitorHumidityIndex_Object=MibTableColumn
isDeviceMonitorHumidityIndex=_IsDeviceMonitorHumidityIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,2,1,1),_IsDeviceMonitorHumidityIndex_Type())
isDeviceMonitorHumidityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorHumidityIndex.setStatus(_A)
class _IsDeviceMonitorHumidityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IsDeviceMonitorHumidityName_Type.__name__=_E
_IsDeviceMonitorHumidityName_Object=MibTableColumn
isDeviceMonitorHumidityName=_IsDeviceMonitorHumidityName_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,2,1,2),_IsDeviceMonitorHumidityName_Type())
isDeviceMonitorHumidityName.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorHumidityName.setStatus(_A)
_IsDeviceMonitorHumidity_Type=Integer32
_IsDeviceMonitorHumidity_Object=MibTableColumn
isDeviceMonitorHumidity=_IsDeviceMonitorHumidity_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,2,1,3),_IsDeviceMonitorHumidity_Type())
isDeviceMonitorHumidity.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorHumidity.setStatus(_A)
_IsDeviceMonitorHumidityAlarm_Type=IsproEnuThresholdStatus
_IsDeviceMonitorHumidityAlarm_Object=MibTableColumn
isDeviceMonitorHumidityAlarm=_IsDeviceMonitorHumidityAlarm_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,2,1,4),_IsDeviceMonitorHumidityAlarm_Type())
isDeviceMonitorHumidityAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorHumidityAlarm.setStatus(_A)
_IsDeviceMonitorDigitalInTable_Object=MibTable
isDeviceMonitorDigitalInTable=_IsDeviceMonitorDigitalInTable_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,3))
if mibBuilder.loadTexts:isDeviceMonitorDigitalInTable.setStatus(_A)
_IsDeviceMonitorDigitalInEntry_Object=MibTableRow
isDeviceMonitorDigitalInEntry=_IsDeviceMonitorDigitalInEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,3,1))
isDeviceMonitorDigitalInEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:isDeviceMonitorDigitalInEntry.setStatus(_A)
class _IsDeviceMonitorDigitalInIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IsDeviceMonitorDigitalInIndex_Type.__name__=_C
_IsDeviceMonitorDigitalInIndex_Object=MibTableColumn
isDeviceMonitorDigitalInIndex=_IsDeviceMonitorDigitalInIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,3,1,1),_IsDeviceMonitorDigitalInIndex_Type())
isDeviceMonitorDigitalInIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorDigitalInIndex.setStatus(_A)
class _IsDeviceMonitorDigitalInName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IsDeviceMonitorDigitalInName_Type.__name__=_E
_IsDeviceMonitorDigitalInName_Object=MibTableColumn
isDeviceMonitorDigitalInName=_IsDeviceMonitorDigitalInName_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,3,1,2),_IsDeviceMonitorDigitalInName_Type())
isDeviceMonitorDigitalInName.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorDigitalInName.setStatus(_A)
_IsDeviceMonitorDigitalIn_Type=IsproEnuDigitalStatus
_IsDeviceMonitorDigitalIn_Object=MibTableColumn
isDeviceMonitorDigitalIn=_IsDeviceMonitorDigitalIn_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,3,1,3),_IsDeviceMonitorDigitalIn_Type())
isDeviceMonitorDigitalIn.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorDigitalIn.setStatus(_A)
_IsDeviceMonitorDigitalInAlarm_Type=IsproTriggerStatus
_IsDeviceMonitorDigitalInAlarm_Object=MibTableColumn
isDeviceMonitorDigitalInAlarm=_IsDeviceMonitorDigitalInAlarm_Object((1,3,6,1,4,1,19011,1,3,2,1,3,1,3,1,4),_IsDeviceMonitorDigitalInAlarm_Type())
isDeviceMonitorDigitalInAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceMonitorDigitalInAlarm.setStatus(_A)
_IsDeviceConfig_ObjectIdentity=ObjectIdentity
isDeviceConfig=_IsDeviceConfig_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,1,3,2))
_IsDeviceConfigTable_Object=MibTable
isDeviceConfigTable=_IsDeviceConfigTable_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,1))
if mibBuilder.loadTexts:isDeviceConfigTable.setStatus(_A)
_IsDeviceConfigEntry_Object=MibTableRow
isDeviceConfigEntry=_IsDeviceConfigEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,1,1))
isDeviceConfigEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:isDeviceConfigEntry.setStatus(_A)
class _IsDeviceConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_IsDeviceConfigIndex_Type.__name__=_C
_IsDeviceConfigIndex_Object=MibTableColumn
isDeviceConfigIndex=_IsDeviceConfigIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,1,1,1),_IsDeviceConfigIndex_Type())
isDeviceConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceConfigIndex.setStatus(_A)
class _IsDeviceConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IsDeviceConfigName_Type.__name__=_E
_IsDeviceConfigName_Object=MibTableColumn
isDeviceConfigName=_IsDeviceConfigName_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,1,1,2),_IsDeviceConfigName_Type())
isDeviceConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigName.setStatus(_A)
_IsDeviceConfigState_Type=IsproEnuSensorState
_IsDeviceConfigState_Object=MibTableColumn
isDeviceConfigState=_IsDeviceConfigState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,1,1,3),_IsDeviceConfigState_Type())
isDeviceConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigState.setStatus(_A)
_IsDeviceConfigDisplay_Type=IsproEnuEnable
_IsDeviceConfigDisplay_Object=MibTableColumn
isDeviceConfigDisplay=_IsDeviceConfigDisplay_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,1,1,4),_IsDeviceConfigDisplay_Type())
isDeviceConfigDisplay.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigDisplay.setStatus(_A)
_IsDeviceConfigTemperatureTable_Object=MibTable
isDeviceConfigTemperatureTable=_IsDeviceConfigTemperatureTable_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2))
if mibBuilder.loadTexts:isDeviceConfigTemperatureTable.setStatus(_A)
_IsDeviceConfigTemperatureEntry_Object=MibTableRow
isDeviceConfigTemperatureEntry=_IsDeviceConfigTemperatureEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1))
isDeviceConfigTemperatureEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:isDeviceConfigTemperatureEntry.setStatus(_A)
class _IsDeviceConfigTemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_IsDeviceConfigTemperatureIndex_Type.__name__=_C
_IsDeviceConfigTemperatureIndex_Object=MibTableColumn
isDeviceConfigTemperatureIndex=_IsDeviceConfigTemperatureIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,1),_IsDeviceConfigTemperatureIndex_Type())
isDeviceConfigTemperatureIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceConfigTemperatureIndex.setStatus(_A)
class _IsDeviceConfigTemperatureName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IsDeviceConfigTemperatureName_Type.__name__=_E
_IsDeviceConfigTemperatureName_Object=MibTableColumn
isDeviceConfigTemperatureName=_IsDeviceConfigTemperatureName_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,2),_IsDeviceConfigTemperatureName_Type())
isDeviceConfigTemperatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureName.setStatus(_A)
class _IsDeviceConfigTemperatureLowWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1500,6500))
_IsDeviceConfigTemperatureLowWarning_Type.__name__=_C
_IsDeviceConfigTemperatureLowWarning_Object=MibTableColumn
isDeviceConfigTemperatureLowWarning=_IsDeviceConfigTemperatureLowWarning_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,3),_IsDeviceConfigTemperatureLowWarning_Type())
isDeviceConfigTemperatureLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureLowWarning.setStatus(_A)
class _IsDeviceConfigTemperatureLowCritical_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1500,6500))
_IsDeviceConfigTemperatureLowCritical_Type.__name__=_C
_IsDeviceConfigTemperatureLowCritical_Object=MibTableColumn
isDeviceConfigTemperatureLowCritical=_IsDeviceConfigTemperatureLowCritical_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,4),_IsDeviceConfigTemperatureLowCritical_Type())
isDeviceConfigTemperatureLowCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureLowCritical.setStatus(_A)
class _IsDeviceConfigTemperatureHighWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1500,6500))
_IsDeviceConfigTemperatureHighWarning_Type.__name__=_C
_IsDeviceConfigTemperatureHighWarning_Object=MibTableColumn
isDeviceConfigTemperatureHighWarning=_IsDeviceConfigTemperatureHighWarning_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,5),_IsDeviceConfigTemperatureHighWarning_Type())
isDeviceConfigTemperatureHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureHighWarning.setStatus(_A)
class _IsDeviceConfigTemperatureHighCritical_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1500,6500))
_IsDeviceConfigTemperatureHighCritical_Type.__name__=_C
_IsDeviceConfigTemperatureHighCritical_Object=MibTableColumn
isDeviceConfigTemperatureHighCritical=_IsDeviceConfigTemperatureHighCritical_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,6),_IsDeviceConfigTemperatureHighCritical_Type())
isDeviceConfigTemperatureHighCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureHighCritical.setStatus(_A)
_IsDeviceConfigTemperatureHysteresis_Type=Integer32
_IsDeviceConfigTemperatureHysteresis_Object=MibTableColumn
isDeviceConfigTemperatureHysteresis=_IsDeviceConfigTemperatureHysteresis_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,7),_IsDeviceConfigTemperatureHysteresis_Type())
isDeviceConfigTemperatureHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureHysteresis.setStatus(_A)
_IsDeviceConfigTemperatureCalibration_Type=IsproEnuTempCalibration
_IsDeviceConfigTemperatureCalibration_Object=MibTableColumn
isDeviceConfigTemperatureCalibration=_IsDeviceConfigTemperatureCalibration_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,8),_IsDeviceConfigTemperatureCalibration_Type())
isDeviceConfigTemperatureCalibration.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureCalibration.setStatus(_A)
_IsDeviceConfigTemperatureLowWarningState_Type=IsproEnuEnable
_IsDeviceConfigTemperatureLowWarningState_Object=MibTableColumn
isDeviceConfigTemperatureLowWarningState=_IsDeviceConfigTemperatureLowWarningState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,9),_IsDeviceConfigTemperatureLowWarningState_Type())
isDeviceConfigTemperatureLowWarningState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureLowWarningState.setStatus(_A)
_IsDeviceConfigTemperatureLowCriticalState_Type=IsproEnuEnable
_IsDeviceConfigTemperatureLowCriticalState_Object=MibTableColumn
isDeviceConfigTemperatureLowCriticalState=_IsDeviceConfigTemperatureLowCriticalState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,10),_IsDeviceConfigTemperatureLowCriticalState_Type())
isDeviceConfigTemperatureLowCriticalState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureLowCriticalState.setStatus(_A)
_IsDeviceConfigTemperatureHighWarningState_Type=IsproEnuEnable
_IsDeviceConfigTemperatureHighWarningState_Object=MibTableColumn
isDeviceConfigTemperatureHighWarningState=_IsDeviceConfigTemperatureHighWarningState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,11),_IsDeviceConfigTemperatureHighWarningState_Type())
isDeviceConfigTemperatureHighWarningState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureHighWarningState.setStatus(_A)
_IsDeviceConfigTemperatureHighCriticalState_Type=IsproEnuEnable
_IsDeviceConfigTemperatureHighCriticalState_Object=MibTableColumn
isDeviceConfigTemperatureHighCriticalState=_IsDeviceConfigTemperatureHighCriticalState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,12),_IsDeviceConfigTemperatureHighCriticalState_Type())
isDeviceConfigTemperatureHighCriticalState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureHighCriticalState.setStatus(_A)
_IsDeviceConfigTemperatureEventDO_Type=IsproEnuDO
_IsDeviceConfigTemperatureEventDO_Object=MibTableColumn
isDeviceConfigTemperatureEventDO=_IsDeviceConfigTemperatureEventDO_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,2,1,13),_IsDeviceConfigTemperatureEventDO_Type())
isDeviceConfigTemperatureEventDO.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigTemperatureEventDO.setStatus(_A)
_IsDeviceConfigHumidityTable_Object=MibTable
isDeviceConfigHumidityTable=_IsDeviceConfigHumidityTable_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3))
if mibBuilder.loadTexts:isDeviceConfigHumidityTable.setStatus(_A)
_IsDeviceConfigHumidityEntry_Object=MibTableRow
isDeviceConfigHumidityEntry=_IsDeviceConfigHumidityEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1))
isDeviceConfigHumidityEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:isDeviceConfigHumidityEntry.setStatus(_A)
class _IsDeviceConfigHumidityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_IsDeviceConfigHumidityIndex_Type.__name__=_C
_IsDeviceConfigHumidityIndex_Object=MibTableColumn
isDeviceConfigHumidityIndex=_IsDeviceConfigHumidityIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,1),_IsDeviceConfigHumidityIndex_Type())
isDeviceConfigHumidityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceConfigHumidityIndex.setStatus(_A)
class _IsDeviceConfigHumidityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IsDeviceConfigHumidityName_Type.__name__=_E
_IsDeviceConfigHumidityName_Object=MibTableColumn
isDeviceConfigHumidityName=_IsDeviceConfigHumidityName_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,2),_IsDeviceConfigHumidityName_Type())
isDeviceConfigHumidityName.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityName.setStatus(_A)
class _IsDeviceConfigHumidityLowWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,9500))
_IsDeviceConfigHumidityLowWarning_Type.__name__=_C
_IsDeviceConfigHumidityLowWarning_Object=MibTableColumn
isDeviceConfigHumidityLowWarning=_IsDeviceConfigHumidityLowWarning_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,3),_IsDeviceConfigHumidityLowWarning_Type())
isDeviceConfigHumidityLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityLowWarning.setStatus(_A)
class _IsDeviceConfigHumidityLowCritical_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,9500))
_IsDeviceConfigHumidityLowCritical_Type.__name__=_C
_IsDeviceConfigHumidityLowCritical_Object=MibTableColumn
isDeviceConfigHumidityLowCritical=_IsDeviceConfigHumidityLowCritical_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,4),_IsDeviceConfigHumidityLowCritical_Type())
isDeviceConfigHumidityLowCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityLowCritical.setStatus(_A)
class _IsDeviceConfigHumidityHighWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,9500))
_IsDeviceConfigHumidityHighWarning_Type.__name__=_C
_IsDeviceConfigHumidityHighWarning_Object=MibTableColumn
isDeviceConfigHumidityHighWarning=_IsDeviceConfigHumidityHighWarning_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,5),_IsDeviceConfigHumidityHighWarning_Type())
isDeviceConfigHumidityHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityHighWarning.setStatus(_A)
class _IsDeviceConfigHumidityHighCritical_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,9500))
_IsDeviceConfigHumidityHighCritical_Type.__name__=_C
_IsDeviceConfigHumidityHighCritical_Object=MibTableColumn
isDeviceConfigHumidityHighCritical=_IsDeviceConfigHumidityHighCritical_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,6),_IsDeviceConfigHumidityHighCritical_Type())
isDeviceConfigHumidityHighCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityHighCritical.setStatus(_A)
_IsDeviceConfigHumidityHysteresis_Type=Integer32
_IsDeviceConfigHumidityHysteresis_Object=MibTableColumn
isDeviceConfigHumidityHysteresis=_IsDeviceConfigHumidityHysteresis_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,7),_IsDeviceConfigHumidityHysteresis_Type())
isDeviceConfigHumidityHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityHysteresis.setStatus(_A)
_IsDeviceConfigHumidityCalibration_Type=IsproEnuHumidityCalibration
_IsDeviceConfigHumidityCalibration_Object=MibTableColumn
isDeviceConfigHumidityCalibration=_IsDeviceConfigHumidityCalibration_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,8),_IsDeviceConfigHumidityCalibration_Type())
isDeviceConfigHumidityCalibration.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityCalibration.setStatus(_A)
_IsDeviceConfigHumidityLowWarningState_Type=IsproEnuEnable
_IsDeviceConfigHumidityLowWarningState_Object=MibTableColumn
isDeviceConfigHumidityLowWarningState=_IsDeviceConfigHumidityLowWarningState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,9),_IsDeviceConfigHumidityLowWarningState_Type())
isDeviceConfigHumidityLowWarningState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityLowWarningState.setStatus(_A)
_IsDeviceConfigHumidityLowCriticalState_Type=IsproEnuEnable
_IsDeviceConfigHumidityLowCriticalState_Object=MibTableColumn
isDeviceConfigHumidityLowCriticalState=_IsDeviceConfigHumidityLowCriticalState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,10),_IsDeviceConfigHumidityLowCriticalState_Type())
isDeviceConfigHumidityLowCriticalState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityLowCriticalState.setStatus(_A)
_IsDeviceConfigHumidityHighWarningState_Type=IsproEnuEnable
_IsDeviceConfigHumidityHighWarningState_Object=MibTableColumn
isDeviceConfigHumidityHighWarningState=_IsDeviceConfigHumidityHighWarningState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,11),_IsDeviceConfigHumidityHighWarningState_Type())
isDeviceConfigHumidityHighWarningState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityHighWarningState.setStatus(_A)
_IsDeviceConfigHumidityHighCriticalState_Type=IsproEnuEnable
_IsDeviceConfigHumidityHighCriticalState_Object=MibTableColumn
isDeviceConfigHumidityHighCriticalState=_IsDeviceConfigHumidityHighCriticalState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,12),_IsDeviceConfigHumidityHighCriticalState_Type())
isDeviceConfigHumidityHighCriticalState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityHighCriticalState.setStatus(_A)
_IsDeviceConfigHumidityEventDO_Type=IsproEnuDO
_IsDeviceConfigHumidityEventDO_Object=MibTableColumn
isDeviceConfigHumidityEventDO=_IsDeviceConfigHumidityEventDO_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,3,1,13),_IsDeviceConfigHumidityEventDO_Type())
isDeviceConfigHumidityEventDO.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigHumidityEventDO.setStatus(_A)
_IsDeviceConfigDigitalInTable_Object=MibTable
isDeviceConfigDigitalInTable=_IsDeviceConfigDigitalInTable_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,4))
if mibBuilder.loadTexts:isDeviceConfigDigitalInTable.setStatus(_A)
_IsDeviceConfigDigitalInEntry_Object=MibTableRow
isDeviceConfigDigitalInEntry=_IsDeviceConfigDigitalInEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,4,1))
isDeviceConfigDigitalInEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:isDeviceConfigDigitalInEntry.setStatus(_A)
class _IsDeviceConfigDigitalInIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IsDeviceConfigDigitalInIndex_Type.__name__=_C
_IsDeviceConfigDigitalInIndex_Object=MibTableColumn
isDeviceConfigDigitalInIndex=_IsDeviceConfigDigitalInIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,4,1,1),_IsDeviceConfigDigitalInIndex_Type())
isDeviceConfigDigitalInIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceConfigDigitalInIndex.setStatus(_A)
class _IsDeviceConfigDigitalInName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IsDeviceConfigDigitalInName_Type.__name__=_E
_IsDeviceConfigDigitalInName_Object=MibTableColumn
isDeviceConfigDigitalInName=_IsDeviceConfigDigitalInName_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,4,1,2),_IsDeviceConfigDigitalInName_Type())
isDeviceConfigDigitalInName.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigDigitalInName.setStatus(_A)
_IsDeviceConfigDigitalInState_Type=IsproEnuAlarmState
_IsDeviceConfigDigitalInState_Object=MibTableColumn
isDeviceConfigDigitalInState=_IsDeviceConfigDigitalInState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,4,1,3),_IsDeviceConfigDigitalInState_Type())
isDeviceConfigDigitalInState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigDigitalInState.setStatus(_A)
_IsDeviceConfigDigitalInHysteresis_Type=Integer32
_IsDeviceConfigDigitalInHysteresis_Object=MibTableColumn
isDeviceConfigDigitalInHysteresis=_IsDeviceConfigDigitalInHysteresis_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,4,1,4),_IsDeviceConfigDigitalInHysteresis_Type())
isDeviceConfigDigitalInHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigDigitalInHysteresis.setStatus(_A)
_IsDeviceConfigDigitalInEventDO_Type=IsproEnuDO
_IsDeviceConfigDigitalInEventDO_Object=MibTableColumn
isDeviceConfigDigitalInEventDO=_IsDeviceConfigDigitalInEventDO_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,4,1,5),_IsDeviceConfigDigitalInEventDO_Type())
isDeviceConfigDigitalInEventDO.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceConfigDigitalInEventDO.setStatus(_A)
_IsDeviceDigitalOutTable_Object=MibTable
isDeviceDigitalOutTable=_IsDeviceDigitalOutTable_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,5))
if mibBuilder.loadTexts:isDeviceDigitalOutTable.setStatus(_A)
_IsDeviceDigitalOutEntry_Object=MibTableRow
isDeviceDigitalOutEntry=_IsDeviceDigitalOutEntry_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,5,1))
isDeviceDigitalOutEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:isDeviceDigitalOutEntry.setStatus(_A)
class _IsDeviceDigitalOutIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_IsDeviceDigitalOutIndex_Type.__name__=_C
_IsDeviceDigitalOutIndex_Object=MibTableColumn
isDeviceDigitalOutIndex=_IsDeviceDigitalOutIndex_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,5,1,1),_IsDeviceDigitalOutIndex_Type())
isDeviceDigitalOutIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceDigitalOutIndex.setStatus(_A)
_IsDeviceDigitalOutStartState_Type=IsproEnuOnOff
_IsDeviceDigitalOutStartState_Object=MibTableColumn
isDeviceDigitalOutStartState=_IsDeviceDigitalOutStartState_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,5,1,2),_IsDeviceDigitalOutStartState_Type())
isDeviceDigitalOutStartState.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceDigitalOutStartState.setStatus(_A)
_IsDeviceDigitalOutEventAction_Type=IsproEnuEnable
_IsDeviceDigitalOutEventAction_Object=MibTableColumn
isDeviceDigitalOutEventAction=_IsDeviceDigitalOutEventAction_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,5,1,3),_IsDeviceDigitalOutEventAction_Type())
isDeviceDigitalOutEventAction.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceDigitalOutEventAction.setStatus(_A)
_IsDeviceDigitalOutManualControl_Type=IsproEnuTurnOnOff
_IsDeviceDigitalOutManualControl_Object=MibTableColumn
isDeviceDigitalOutManualControl=_IsDeviceDigitalOutManualControl_Object((1,3,6,1,4,1,19011,1,3,2,1,3,2,5,1,4),_IsDeviceDigitalOutManualControl_Type())
isDeviceDigitalOutManualControl.setMaxAccess(_B)
if mibBuilder.loadTexts:isDeviceDigitalOutManualControl.setStatus(_A)
class _IsDeviceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_IsDeviceID_Type.__name__=_C
_IsDeviceID_Object=MibScalar
isDeviceID=_IsDeviceID_Object((1,3,6,1,4,1,19011,1,3,2,1,3,3),_IsDeviceID_Type())
isDeviceID.setMaxAccess(_D)
if mibBuilder.loadTexts:isDeviceID.setStatus(_A)
_IsTraps_ObjectIdentity=ObjectIdentity
isTraps=_IsTraps_ObjectIdentity((1,3,6,1,4,1,19011,1,3,2,2))
class _IsTrapsDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IsTrapsDescription_Type.__name__=_E
_IsTrapsDescription_Object=MibScalar
isTrapsDescription=_IsTrapsDescription_Object((1,3,6,1,4,1,19011,1,3,2,2,1),_IsTrapsDescription_Type())
isTrapsDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:isTrapsDescription.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'IsproEnuEnable':IsproEnuEnable,'IsproEnuReset':IsproEnuReset,'IsproEnuRestart':IsproEnuRestart,'IsproEnuSeverity':IsproEnuSeverity,'IsproEnuAccess':IsproEnuAccess,'IsproEnuTempUnit':IsproEnuTempUnit,'IsproEnuDateFormat':IsproEnuDateFormat,'IsproEnuTimeZone':IsproEnuTimeZone,'IsproEnuSensorType':IsproEnuSensorType,'IsproEnuThresholdStatus':IsproEnuThresholdStatus,'IsproEnuDigitalStatus':IsproEnuDigitalStatus,'IsproTriggerStatus':IsproTriggerStatus,'IsproEnuSensorState':IsproEnuSensorState,'IsproEnuTempCalibration':IsproEnuTempCalibration,'IsproEnuHumidityCalibration':IsproEnuHumidityCalibration,'IsproEnuAlarmState':IsproEnuAlarmState,'IsproEnuOnOff':IsproEnuOnOff,'IsproEnuTurnOnOff':IsproEnuTurnOnOff,'IsproEnuPresent':IsproEnuPresent,'IsproEnuDO':IsproEnuDO,'IsproEnuHighLow':IsproEnuHighLow,'IsproLogType':IsproLogType,'jacarta':jacarta,'product':product,'webAppliance':webAppliance,'ispro':ispro,'isObjects':isObjects,'isIdent':isIdent,'isIdentManufacturer':isIdentManufacturer,'isIdentModel':isIdentModel,'isIdentAgentSoftwareVersion':isIdentAgentSoftwareVersion,'isIdentName':isIdentName,'isConfig':isConfig,'isConfigMibVersion':isConfigMibVersion,'isConfigNetwork':isConfigNetwork,'isConfigIpAddress':isConfigIpAddress,'isConfigGateway':isConfigGateway,'isConfigSubnetMask':isConfigSubnetMask,'isConfigDateTime':isConfigDateTime,'isConfigDate':isConfigDate,'isConfigTime':isConfigTime,'isConfigTimeFromNtp':isConfigTimeFromNtp,'isConfigNtpIpAddress':isConfigNtpIpAddress,'isConfigNtpTimeZone':isConfigNtpTimeZone,'isConfigDayLightSaving':isConfigDayLightSaving,'isConfigLog':isConfigLog,'isConfigHistoryLogFrequency':isConfigHistoryLogFrequency,'isConfigExtHistoryLogFrequency':isConfigExtHistoryLogFrequency,'isConfigConfigurationLog':isConfigConfigurationLog,'isConfigLogType':isConfigLogType,'isConfigDhcpState':isConfigDhcpState,'isConfigPingState':isConfigPingState,'isConfigTftpState':isConfigTftpState,'isConfigTelnet':isConfigTelnet,'isConfigTelnetState':isConfigTelnetState,'isConfigTelnetPortNumber':isConfigTelnetPortNumber,'isConfigHttp':isConfigHttp,'isConfigHttpState':isConfigHttpState,'isConfigHttpPortNumber':isConfigHttpPortNumber,'isConfigHttpSecurity':isConfigHttpSecurity,'isConfigSnmp':isConfigSnmp,'isConfigSnmpState':isConfigSnmpState,'isConfigSnmpPortNumber':isConfigSnmpPortNumber,'isConfigControl':isConfigControl,'isConfigResetToDefault':isConfigResetToDefault,'isConfigRestart':isConfigRestart,'isConfigTrap':isConfigTrap,'isConfigTrapRetryCount':isConfigTrapRetryCount,'isConfigTrapRetryTime':isConfigTrapRetryTime,'isConfigTrapAckSignature':isConfigTrapAckSignature,'isConfigRefreshRate':isConfigRefreshRate,'isConfigTrapReceiverTable':isConfigTrapReceiverTable,'isConfigTrapReceiverEntry':isConfigTrapReceiverEntry,_L:isReceiverIndex,'isReceiverAddr':isReceiverAddr,'isReceiverCommunityString':isReceiverCommunityString,'isReceiverSeverityLevel':isReceiverSeverityLevel,'isReceiverDescription':isReceiverDescription,'isConfigAccessControlTable':isConfigAccessControlTable,'isConfigAccessControlEntry':isConfigAccessControlEntry,_M:isAccessIndex,'isAccessControlAddr':isAccessControlAddr,'isAccessCommunityString':isAccessCommunityString,'isAccessControlMode':isAccessControlMode,'isAccessAccount':isAccessAccount,'isConfigTemperatureUnit':isConfigTemperatureUnit,'isConfigDateFormat':isConfigDateFormat,'isDevice':isDevice,'isDeviceMonitor':isDeviceMonitor,'isDeviceMonitorTemperatureTable':isDeviceMonitorTemperatureTable,'isDeviceMonitorTemperatureEntry':isDeviceMonitorTemperatureEntry,_N:isDeviceMonitorTemperatureIndex,'isDeviceMonitorTemperatureName':isDeviceMonitorTemperatureName,'isDeviceMonitorTemperature':isDeviceMonitorTemperature,'isDeviceMonitorTemperatureAlarm':isDeviceMonitorTemperatureAlarm,'isDeviceMonitorHumidityTable':isDeviceMonitorHumidityTable,'isDeviceMonitorHumidityEntry':isDeviceMonitorHumidityEntry,_O:isDeviceMonitorHumidityIndex,'isDeviceMonitorHumidityName':isDeviceMonitorHumidityName,'isDeviceMonitorHumidity':isDeviceMonitorHumidity,'isDeviceMonitorHumidityAlarm':isDeviceMonitorHumidityAlarm,'isDeviceMonitorDigitalInTable':isDeviceMonitorDigitalInTable,'isDeviceMonitorDigitalInEntry':isDeviceMonitorDigitalInEntry,_P:isDeviceMonitorDigitalInIndex,'isDeviceMonitorDigitalInName':isDeviceMonitorDigitalInName,'isDeviceMonitorDigitalIn':isDeviceMonitorDigitalIn,'isDeviceMonitorDigitalInAlarm':isDeviceMonitorDigitalInAlarm,'isDeviceConfig':isDeviceConfig,'isDeviceConfigTable':isDeviceConfigTable,'isDeviceConfigEntry':isDeviceConfigEntry,_Q:isDeviceConfigIndex,'isDeviceConfigName':isDeviceConfigName,'isDeviceConfigState':isDeviceConfigState,'isDeviceConfigDisplay':isDeviceConfigDisplay,'isDeviceConfigTemperatureTable':isDeviceConfigTemperatureTable,'isDeviceConfigTemperatureEntry':isDeviceConfigTemperatureEntry,_R:isDeviceConfigTemperatureIndex,'isDeviceConfigTemperatureName':isDeviceConfigTemperatureName,'isDeviceConfigTemperatureLowWarning':isDeviceConfigTemperatureLowWarning,'isDeviceConfigTemperatureLowCritical':isDeviceConfigTemperatureLowCritical,'isDeviceConfigTemperatureHighWarning':isDeviceConfigTemperatureHighWarning,'isDeviceConfigTemperatureHighCritical':isDeviceConfigTemperatureHighCritical,'isDeviceConfigTemperatureHysteresis':isDeviceConfigTemperatureHysteresis,'isDeviceConfigTemperatureCalibration':isDeviceConfigTemperatureCalibration,'isDeviceConfigTemperatureLowWarningState':isDeviceConfigTemperatureLowWarningState,'isDeviceConfigTemperatureLowCriticalState':isDeviceConfigTemperatureLowCriticalState,'isDeviceConfigTemperatureHighWarningState':isDeviceConfigTemperatureHighWarningState,'isDeviceConfigTemperatureHighCriticalState':isDeviceConfigTemperatureHighCriticalState,'isDeviceConfigTemperatureEventDO':isDeviceConfigTemperatureEventDO,'isDeviceConfigHumidityTable':isDeviceConfigHumidityTable,'isDeviceConfigHumidityEntry':isDeviceConfigHumidityEntry,_S:isDeviceConfigHumidityIndex,'isDeviceConfigHumidityName':isDeviceConfigHumidityName,'isDeviceConfigHumidityLowWarning':isDeviceConfigHumidityLowWarning,'isDeviceConfigHumidityLowCritical':isDeviceConfigHumidityLowCritical,'isDeviceConfigHumidityHighWarning':isDeviceConfigHumidityHighWarning,'isDeviceConfigHumidityHighCritical':isDeviceConfigHumidityHighCritical,'isDeviceConfigHumidityHysteresis':isDeviceConfigHumidityHysteresis,'isDeviceConfigHumidityCalibration':isDeviceConfigHumidityCalibration,'isDeviceConfigHumidityLowWarningState':isDeviceConfigHumidityLowWarningState,'isDeviceConfigHumidityLowCriticalState':isDeviceConfigHumidityLowCriticalState,'isDeviceConfigHumidityHighWarningState':isDeviceConfigHumidityHighWarningState,'isDeviceConfigHumidityHighCriticalState':isDeviceConfigHumidityHighCriticalState,'isDeviceConfigHumidityEventDO':isDeviceConfigHumidityEventDO,'isDeviceConfigDigitalInTable':isDeviceConfigDigitalInTable,'isDeviceConfigDigitalInEntry':isDeviceConfigDigitalInEntry,_T:isDeviceConfigDigitalInIndex,'isDeviceConfigDigitalInName':isDeviceConfigDigitalInName,'isDeviceConfigDigitalInState':isDeviceConfigDigitalInState,'isDeviceConfigDigitalInHysteresis':isDeviceConfigDigitalInHysteresis,'isDeviceConfigDigitalInEventDO':isDeviceConfigDigitalInEventDO,'isDeviceDigitalOutTable':isDeviceDigitalOutTable,'isDeviceDigitalOutEntry':isDeviceDigitalOutEntry,_U:isDeviceDigitalOutIndex,'isDeviceDigitalOutStartState':isDeviceDigitalOutStartState,'isDeviceDigitalOutEventAction':isDeviceDigitalOutEventAction,'isDeviceDigitalOutManualControl':isDeviceDigitalOutManualControl,'isDeviceID':isDeviceID,'isTraps':isTraps,'isTrapsDescription':isTrapsDescription})