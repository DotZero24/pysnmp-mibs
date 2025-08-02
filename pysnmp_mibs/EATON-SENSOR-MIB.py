_Ar='sensorNotifyGroup'
_Aq='sensorOptionalGroup'
_Ap='sensorRequiredGroup'
_Ao='notifydigitalInputCommunicationStatus'
_An='notifyDigitalInputAlarm'
_Am='notifyHumidityCommunicationStatus'
_Al='notifyHumidityAlarm'
_Ak='notifyTemperatureCommunicationStatus'
_Aj='notifyTemperatureAlarm'
_Ai='notifySensorCount'
_Ah='notifySensorStatus'
_Ag='digitalInputAlarmGracePeriod'
_Af='digitalInputAlarmSeverity'
_Ae='digitalInputAlarmEnable'
_Ad='digitalInputPolarity'
_Ac='digitalInputEnable'
_Ab='digitalInputConnectionType'
_Aa='humidityResetMinMax'
_AZ='humidityMaxValueSince'
_AY='humidityMaxValue'
_AX='humidityMinValueSince'
_AW='humidityMinValue'
_AV='humidityAlarmGracePeriod'
_AU='humidityThresholdHysteresis'
_AT='humidityThresholdHighCritical'
_AS='humidityThresholdHighWarning'
_AR='humidityThresholdLowCritical'
_AQ='humidityThresholdLowWarning'
_AP='humidityAlarmEnable'
_AO='humidityOffset'
_AN='humidityEnable'
_AM='humidityConnectionType'
_AL='temperatureResetMinMax'
_AK='temperatureMaxValueSince'
_AJ='temperatureMaxValue'
_AI='temperatureMinValueSince'
_AH='temperatureMinValue'
_AG='temperatureAlarmGracePeriod'
_AF='temperatureThresholdHysteresis'
_AE='temperatureThresholdHighCritical'
_AD='temperatureThresholdHighWarning'
_AC='temperatureThresholdLowCritical'
_AB='temperatureThresholdLowWarning'
_AA='temperatureAlarmEnable'
_A9='temperatureOffset'
_A8='temperatureEnable'
_A7='temperatureConnectionType'
_A6='sensorAnalogInputCount'
_A5='sensorUElevation'
_A4='sensorElevation'
_A3='sensorPosition'
_A2='sensorLocation'
_A1='sensorMonitoredBy'
_A0='sensorAddress'
_z='sensorConnectionType'
_y='digitalInputName'
_x='humidityName'
_w='temperatureUnit'
_v='temperatureName'
_u='sensorDigitalInputCount'
_t='sensorHumidityCount'
_s='sensorTemperatureCount'
_r='sensorName'
_q='sensorFirmwareVersion'
_p='sensorSerialNumber'
_o='sensorPartNumber'
_n='sensorModel'
_m='sensorManufacturer'
_l='critical'
_k='warning'
_j='informational'
_i='digitalInputCommunicationStatusSince'
_h='digitalInputCommunicationStatus'
_g='digitalInputAlarmChangeSince'
_f='digitalInputAlarm'
_e='digitalInputStateSince'
_d='digitalInputState'
_c='humidityCommunicationStatusSince'
_b='humidityCommunicationStatus'
_a='humidityAlarmChangeSince'
_Z='humidityAlarm'
_Y='temperatureCommunicationStatusSince'
_X='temperatureCommunicationStatus'
_W='temperatureAlarmChangeSince'
_V='temperatureAlarm'
_U='sensorUuid'
_T='humidityValue'
_S='temperatureValue'
_R='sensorStatusSince'
_Q='sensorStatus'
_P='sensorCount'
_O='undefined'
_N='digitalInputUuid'
_M='humidityUuid'
_L='temperatureUuid'
_K='accessible-for-notify'
_J='digitalInputIndex'
_I='humidityIndex'
_H='temperatureIndex'
_G='Integer32'
_F='OctetString'
_E='sensorIndex'
_D='read-write'
_C='read-only'
_B='current'
_A='EATON-SENSOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sensorAgent,=mibBuilder.importSymbols('EATON-OIDS','sensorAgent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eatonSensor=ModuleIdentity((1,3,6,1,4,1,534,6,8,1))
if mibBuilder.loadTexts:eatonSensor.setRevisions(('2022-05-06 12:00','2018-12-17 12:00'))
class UnixTimeStamp(TextualConvention,Counter32):status=_B;displayHint='dddddddddd'
class PositionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_O,0),('other',1),('rackRear',2),('rackFront',3),('batteryRoom',4)))
class ElevationType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_O,0),('other',1),('bottom',2),('middle',3),('top',4)))
class CommunicationStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('unknown',0),('communicationOK',2),('communicationLost',3)))
class ProbeConnectionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),('internal',1),('wired',2),('wireless',3)))
class EnableType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
class AlarmType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('good',0),('lowWarning',1),('lowCritical',2),('highWarning',3),('highCritical',4)))
class ResetCommandType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('reset',1)))
class PolarityType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normallyOpened',0),('normallyClosed',1)))
class AlarmSeverityType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_j,1),(_k,2),(_l,3)))
class AlarmLevelType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('good',0),(_j,1),(_k,2),(_l,3)))
class StateType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
class TemperatureUnitType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('tenthOfDegKelvin',0),('tenthOfDegCelsius',1),('tenthOfDegFarhenheit',2)))
_Sensor_ObjectIdentity=ObjectIdentity
sensor=_Sensor_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,1))
_SensorNotification_ObjectIdentity=ObjectIdentity
sensorNotification=_SensorNotification_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,1,0))
_SensorCount_Type=Integer32
_SensorCount_Object=MibScalar
sensorCount=_SensorCount_Object((1,3,6,1,4,1,534,6,8,1,1,1),_SensorCount_Type())
sensorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorCount.setStatus(_B)
_SensorIdentificationTable_Object=MibTable
sensorIdentificationTable=_SensorIdentificationTable_Object((1,3,6,1,4,1,534,6,8,1,1,2))
if mibBuilder.loadTexts:sensorIdentificationTable.setStatus(_B)
_SensorIdentificationEntry_Object=MibTableRow
sensorIdentificationEntry=_SensorIdentificationEntry_Object((1,3,6,1,4,1,534,6,8,1,1,2,1))
sensorIdentificationEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:sensorIdentificationEntry.setStatus(_B)
class _SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SensorIndex_Type.__name__=_G
_SensorIndex_Object=MibTableColumn
sensorIndex=_SensorIndex_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,1),_SensorIndex_Type())
sensorIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:sensorIndex.setStatus(_B)
_SensorUuid_Type=OctetString
_SensorUuid_Object=MibTableColumn
sensorUuid=_SensorUuid_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,2),_SensorUuid_Type())
sensorUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorUuid.setStatus(_B)
_SensorConnectionType_Type=ProbeConnectionType
_SensorConnectionType_Object=MibTableColumn
sensorConnectionType=_SensorConnectionType_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,3),_SensorConnectionType_Type())
sensorConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorConnectionType.setStatus(_B)
_SensorAddress_Type=OctetString
_SensorAddress_Object=MibTableColumn
sensorAddress=_SensorAddress_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,4),_SensorAddress_Type())
sensorAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorAddress.setStatus(_B)
_SensorMonitoredBy_Type=ObjectIdentifier
_SensorMonitoredBy_Object=MibTableColumn
sensorMonitoredBy=_SensorMonitoredBy_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,5),_SensorMonitoredBy_Type())
sensorMonitoredBy.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorMonitoredBy.setStatus(_B)
class _SensorManufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_SensorManufacturer_Type.__name__=_F
_SensorManufacturer_Object=MibTableColumn
sensorManufacturer=_SensorManufacturer_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,6),_SensorManufacturer_Type())
sensorManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorManufacturer.setStatus(_B)
class _SensorModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_SensorModel_Type.__name__=_F
_SensorModel_Object=MibTableColumn
sensorModel=_SensorModel_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,7),_SensorModel_Type())
sensorModel.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorModel.setStatus(_B)
class _SensorPartNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_SensorPartNumber_Type.__name__=_F
_SensorPartNumber_Object=MibTableColumn
sensorPartNumber=_SensorPartNumber_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,8),_SensorPartNumber_Type())
sensorPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorPartNumber.setStatus(_B)
class _SensorSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_SensorSerialNumber_Type.__name__=_F
_SensorSerialNumber_Object=MibTableColumn
sensorSerialNumber=_SensorSerialNumber_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,9),_SensorSerialNumber_Type())
sensorSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorSerialNumber.setStatus(_B)
class _SensorFirmwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_SensorFirmwareVersion_Type.__name__=_F
_SensorFirmwareVersion_Object=MibTableColumn
sensorFirmwareVersion=_SensorFirmwareVersion_Object((1,3,6,1,4,1,534,6,8,1,1,2,1,10),_SensorFirmwareVersion_Type())
sensorFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorFirmwareVersion.setStatus(_B)
_SensorConfigurationTable_Object=MibTable
sensorConfigurationTable=_SensorConfigurationTable_Object((1,3,6,1,4,1,534,6,8,1,1,3))
if mibBuilder.loadTexts:sensorConfigurationTable.setStatus(_B)
_SensorConfigurationEntry_Object=MibTableRow
sensorConfigurationEntry=_SensorConfigurationEntry_Object((1,3,6,1,4,1,534,6,8,1,1,3,1))
sensorConfigurationEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:sensorConfigurationEntry.setStatus(_B)
class _SensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_SensorName_Type.__name__=_F
_SensorName_Object=MibTableColumn
sensorName=_SensorName_Object((1,3,6,1,4,1,534,6,8,1,1,3,1,1),_SensorName_Type())
sensorName.setMaxAccess(_D)
if mibBuilder.loadTexts:sensorName.setStatus(_B)
class _SensorLocation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_SensorLocation_Type.__name__=_F
_SensorLocation_Object=MibTableColumn
sensorLocation=_SensorLocation_Object((1,3,6,1,4,1,534,6,8,1,1,3,1,2),_SensorLocation_Type())
sensorLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:sensorLocation.setStatus(_B)
_SensorPosition_Type=PositionType
_SensorPosition_Object=MibTableColumn
sensorPosition=_SensorPosition_Object((1,3,6,1,4,1,534,6,8,1,1,3,1,3),_SensorPosition_Type())
sensorPosition.setMaxAccess(_D)
if mibBuilder.loadTexts:sensorPosition.setStatus(_B)
_SensorElevation_Type=ElevationType
_SensorElevation_Object=MibTableColumn
sensorElevation=_SensorElevation_Object((1,3,6,1,4,1,534,6,8,1,1,3,1,4),_SensorElevation_Type())
sensorElevation.setMaxAccess(_D)
if mibBuilder.loadTexts:sensorElevation.setStatus(_B)
_SensorUElevation_Type=Integer32
_SensorUElevation_Object=MibTableColumn
sensorUElevation=_SensorUElevation_Object((1,3,6,1,4,1,534,6,8,1,1,3,1,5),_SensorUElevation_Type())
sensorUElevation.setMaxAccess(_D)
if mibBuilder.loadTexts:sensorUElevation.setStatus(_B)
_SensorMonitoringTable_Object=MibTable
sensorMonitoringTable=_SensorMonitoringTable_Object((1,3,6,1,4,1,534,6,8,1,1,4))
if mibBuilder.loadTexts:sensorMonitoringTable.setStatus(_B)
_SensorMonitoringEntry_Object=MibTableRow
sensorMonitoringEntry=_SensorMonitoringEntry_Object((1,3,6,1,4,1,534,6,8,1,1,4,1))
sensorMonitoringEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:sensorMonitoringEntry.setStatus(_B)
_SensorStatus_Type=CommunicationStatus
_SensorStatus_Object=MibTableColumn
sensorStatus=_SensorStatus_Object((1,3,6,1,4,1,534,6,8,1,1,4,1,1),_SensorStatus_Type())
sensorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorStatus.setStatus(_B)
_SensorStatusSince_Type=UnixTimeStamp
_SensorStatusSince_Object=MibTableColumn
sensorStatusSince=_SensorStatusSince_Object((1,3,6,1,4,1,534,6,8,1,1,4,1,2),_SensorStatusSince_Type())
sensorStatusSince.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorStatusSince.setStatus(_B)
_SensorTemperatureCount_Type=Integer32
_SensorTemperatureCount_Object=MibTableColumn
sensorTemperatureCount=_SensorTemperatureCount_Object((1,3,6,1,4,1,534,6,8,1,1,4,1,3),_SensorTemperatureCount_Type())
sensorTemperatureCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorTemperatureCount.setStatus(_B)
_SensorHumidityCount_Type=Integer32
_SensorHumidityCount_Object=MibTableColumn
sensorHumidityCount=_SensorHumidityCount_Object((1,3,6,1,4,1,534,6,8,1,1,4,1,4),_SensorHumidityCount_Type())
sensorHumidityCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorHumidityCount.setStatus(_B)
_SensorDigitalInputCount_Type=Integer32
_SensorDigitalInputCount_Object=MibTableColumn
sensorDigitalInputCount=_SensorDigitalInputCount_Object((1,3,6,1,4,1,534,6,8,1,1,4,1,5),_SensorDigitalInputCount_Type())
sensorDigitalInputCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorDigitalInputCount.setStatus(_B)
_SensorAnalogInputCount_Type=Integer32
_SensorAnalogInputCount_Object=MibTableColumn
sensorAnalogInputCount=_SensorAnalogInputCount_Object((1,3,6,1,4,1,534,6,8,1,1,4,1,6),_SensorAnalogInputCount_Type())
sensorAnalogInputCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorAnalogInputCount.setStatus(_B)
_Temperature_ObjectIdentity=ObjectIdentity
temperature=_Temperature_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,2))
_TemperatureNotification_ObjectIdentity=ObjectIdentity
temperatureNotification=_TemperatureNotification_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,2,0))
_TemperatureIdentificationTable_Object=MibTable
temperatureIdentificationTable=_TemperatureIdentificationTable_Object((1,3,6,1,4,1,534,6,8,1,2,1))
if mibBuilder.loadTexts:temperatureIdentificationTable.setStatus(_B)
_TemperatureIdentificationEntry_Object=MibTableRow
temperatureIdentificationEntry=_TemperatureIdentificationEntry_Object((1,3,6,1,4,1,534,6,8,1,2,1,1))
temperatureIdentificationEntry.setIndexNames((0,_A,_E),(0,_A,_H))
if mibBuilder.loadTexts:temperatureIdentificationEntry.setStatus(_B)
class _TemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_TemperatureIndex_Type.__name__=_G
_TemperatureIndex_Object=MibTableColumn
temperatureIndex=_TemperatureIndex_Object((1,3,6,1,4,1,534,6,8,1,2,1,1,1),_TemperatureIndex_Type())
temperatureIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:temperatureIndex.setStatus(_B)
_TemperatureUuid_Type=OctetString
_TemperatureUuid_Object=MibTableColumn
temperatureUuid=_TemperatureUuid_Object((1,3,6,1,4,1,534,6,8,1,2,1,1,2),_TemperatureUuid_Type())
temperatureUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureUuid.setStatus(_B)
_TemperatureConnectionType_Type=ProbeConnectionType
_TemperatureConnectionType_Object=MibTableColumn
temperatureConnectionType=_TemperatureConnectionType_Object((1,3,6,1,4,1,534,6,8,1,2,1,1,3),_TemperatureConnectionType_Type())
temperatureConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureConnectionType.setStatus(_B)
_TemperatureConfigurationTable_Object=MibTable
temperatureConfigurationTable=_TemperatureConfigurationTable_Object((1,3,6,1,4,1,534,6,8,1,2,2))
if mibBuilder.loadTexts:temperatureConfigurationTable.setStatus(_B)
_TemperatureConfigurationEntry_Object=MibTableRow
temperatureConfigurationEntry=_TemperatureConfigurationEntry_Object((1,3,6,1,4,1,534,6,8,1,2,2,1))
temperatureConfigurationEntry.setIndexNames((0,_A,_E),(0,_A,_H))
if mibBuilder.loadTexts:temperatureConfigurationEntry.setStatus(_B)
class _TemperatureName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_TemperatureName_Type.__name__=_F
_TemperatureName_Object=MibTableColumn
temperatureName=_TemperatureName_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,1),_TemperatureName_Type())
temperatureName.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureName.setStatus(_B)
_TemperatureEnable_Type=EnableType
_TemperatureEnable_Object=MibTableColumn
temperatureEnable=_TemperatureEnable_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,2),_TemperatureEnable_Type())
temperatureEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureEnable.setStatus(_B)
_TemperatureOffset_Type=Integer32
_TemperatureOffset_Object=MibTableColumn
temperatureOffset=_TemperatureOffset_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,3),_TemperatureOffset_Type())
temperatureOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureOffset.setStatus(_B)
_TemperatureAlarmEnable_Type=EnableType
_TemperatureAlarmEnable_Object=MibTableColumn
temperatureAlarmEnable=_TemperatureAlarmEnable_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,4),_TemperatureAlarmEnable_Type())
temperatureAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureAlarmEnable.setStatus(_B)
_TemperatureThresholdLowWarning_Type=Integer32
_TemperatureThresholdLowWarning_Object=MibTableColumn
temperatureThresholdLowWarning=_TemperatureThresholdLowWarning_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,5),_TemperatureThresholdLowWarning_Type())
temperatureThresholdLowWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureThresholdLowWarning.setStatus(_B)
_TemperatureThresholdLowCritical_Type=Integer32
_TemperatureThresholdLowCritical_Object=MibTableColumn
temperatureThresholdLowCritical=_TemperatureThresholdLowCritical_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,6),_TemperatureThresholdLowCritical_Type())
temperatureThresholdLowCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureThresholdLowCritical.setStatus(_B)
_TemperatureThresholdHighWarning_Type=Integer32
_TemperatureThresholdHighWarning_Object=MibTableColumn
temperatureThresholdHighWarning=_TemperatureThresholdHighWarning_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,7),_TemperatureThresholdHighWarning_Type())
temperatureThresholdHighWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureThresholdHighWarning.setStatus(_B)
_TemperatureThresholdHighCritical_Type=Integer32
_TemperatureThresholdHighCritical_Object=MibTableColumn
temperatureThresholdHighCritical=_TemperatureThresholdHighCritical_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,8),_TemperatureThresholdHighCritical_Type())
temperatureThresholdHighCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureThresholdHighCritical.setStatus(_B)
_TemperatureThresholdHysteresis_Type=Integer32
_TemperatureThresholdHysteresis_Object=MibTableColumn
temperatureThresholdHysteresis=_TemperatureThresholdHysteresis_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,9),_TemperatureThresholdHysteresis_Type())
temperatureThresholdHysteresis.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureThresholdHysteresis.setStatus(_B)
class _TemperatureAlarmGracePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_TemperatureAlarmGracePeriod_Type.__name__=_G
_TemperatureAlarmGracePeriod_Object=MibTableColumn
temperatureAlarmGracePeriod=_TemperatureAlarmGracePeriod_Object((1,3,6,1,4,1,534,6,8,1,2,2,1,10),_TemperatureAlarmGracePeriod_Type())
temperatureAlarmGracePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureAlarmGracePeriod.setStatus(_B)
_TemperatureMonitoringTable_Object=MibTable
temperatureMonitoringTable=_TemperatureMonitoringTable_Object((1,3,6,1,4,1,534,6,8,1,2,3))
if mibBuilder.loadTexts:temperatureMonitoringTable.setStatus(_B)
_TemperatureMonitoringEntry_Object=MibTableRow
temperatureMonitoringEntry=_TemperatureMonitoringEntry_Object((1,3,6,1,4,1,534,6,8,1,2,3,1))
temperatureMonitoringEntry.setIndexNames((0,_A,_E),(0,_A,_H))
if mibBuilder.loadTexts:temperatureMonitoringEntry.setStatus(_B)
_TemperatureAlarm_Type=AlarmType
_TemperatureAlarm_Object=MibTableColumn
temperatureAlarm=_TemperatureAlarm_Object((1,3,6,1,4,1,534,6,8,1,2,3,1,1),_TemperatureAlarm_Type())
temperatureAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureAlarm.setStatus(_B)
_TemperatureAlarmChangeSince_Type=UnixTimeStamp
_TemperatureAlarmChangeSince_Object=MibTableColumn
temperatureAlarmChangeSince=_TemperatureAlarmChangeSince_Object((1,3,6,1,4,1,534,6,8,1,2,3,1,2),_TemperatureAlarmChangeSince_Type())
temperatureAlarmChangeSince.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureAlarmChangeSince.setStatus(_B)
_TemperatureValue_Type=Integer32
_TemperatureValue_Object=MibTableColumn
temperatureValue=_TemperatureValue_Object((1,3,6,1,4,1,534,6,8,1,2,3,1,3),_TemperatureValue_Type())
temperatureValue.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureValue.setStatus(_B)
_TemperatureCommunicationStatus_Type=CommunicationStatus
_TemperatureCommunicationStatus_Object=MibTableColumn
temperatureCommunicationStatus=_TemperatureCommunicationStatus_Object((1,3,6,1,4,1,534,6,8,1,2,3,1,4),_TemperatureCommunicationStatus_Type())
temperatureCommunicationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureCommunicationStatus.setStatus(_B)
_TemperatureCommunicationStatusSince_Type=UnixTimeStamp
_TemperatureCommunicationStatusSince_Object=MibTableColumn
temperatureCommunicationStatusSince=_TemperatureCommunicationStatusSince_Object((1,3,6,1,4,1,534,6,8,1,2,3,1,5),_TemperatureCommunicationStatusSince_Type())
temperatureCommunicationStatusSince.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureCommunicationStatusSince.setStatus(_B)
_TemperatureMonitoringMinMaxTable_Object=MibTable
temperatureMonitoringMinMaxTable=_TemperatureMonitoringMinMaxTable_Object((1,3,6,1,4,1,534,6,8,1,2,4))
if mibBuilder.loadTexts:temperatureMonitoringMinMaxTable.setStatus(_B)
_TemperatureMonitoringMinMaxEntry_Object=MibTableRow
temperatureMonitoringMinMaxEntry=_TemperatureMonitoringMinMaxEntry_Object((1,3,6,1,4,1,534,6,8,1,2,4,1))
temperatureMonitoringMinMaxEntry.setIndexNames((0,_A,_E),(0,_A,_H))
if mibBuilder.loadTexts:temperatureMonitoringMinMaxEntry.setStatus(_B)
_TemperatureMinValue_Type=Integer32
_TemperatureMinValue_Object=MibTableColumn
temperatureMinValue=_TemperatureMinValue_Object((1,3,6,1,4,1,534,6,8,1,2,4,1,1),_TemperatureMinValue_Type())
temperatureMinValue.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureMinValue.setStatus(_B)
_TemperatureMinValueSince_Type=UnixTimeStamp
_TemperatureMinValueSince_Object=MibTableColumn
temperatureMinValueSince=_TemperatureMinValueSince_Object((1,3,6,1,4,1,534,6,8,1,2,4,1,2),_TemperatureMinValueSince_Type())
temperatureMinValueSince.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureMinValueSince.setStatus(_B)
_TemperatureMaxValue_Type=Integer32
_TemperatureMaxValue_Object=MibTableColumn
temperatureMaxValue=_TemperatureMaxValue_Object((1,3,6,1,4,1,534,6,8,1,2,4,1,3),_TemperatureMaxValue_Type())
temperatureMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureMaxValue.setStatus(_B)
_TemperatureMaxValueSince_Type=UnixTimeStamp
_TemperatureMaxValueSince_Object=MibTableColumn
temperatureMaxValueSince=_TemperatureMaxValueSince_Object((1,3,6,1,4,1,534,6,8,1,2,4,1,4),_TemperatureMaxValueSince_Type())
temperatureMaxValueSince.setMaxAccess(_C)
if mibBuilder.loadTexts:temperatureMaxValueSince.setStatus(_B)
_TemperatureResetMinMax_Type=ResetCommandType
_TemperatureResetMinMax_Object=MibTableColumn
temperatureResetMinMax=_TemperatureResetMinMax_Object((1,3,6,1,4,1,534,6,8,1,2,4,1,5),_TemperatureResetMinMax_Type())
temperatureResetMinMax.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureResetMinMax.setStatus(_B)
_TemperatureUnit_Type=TemperatureUnitType
_TemperatureUnit_Object=MibScalar
temperatureUnit=_TemperatureUnit_Object((1,3,6,1,4,1,534,6,8,1,2,5),_TemperatureUnit_Type())
temperatureUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:temperatureUnit.setStatus(_B)
_Humidity_ObjectIdentity=ObjectIdentity
humidity=_Humidity_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,3))
_HumidityNotification_ObjectIdentity=ObjectIdentity
humidityNotification=_HumidityNotification_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,3,0))
_HumidityIdentificationTable_Object=MibTable
humidityIdentificationTable=_HumidityIdentificationTable_Object((1,3,6,1,4,1,534,6,8,1,3,1))
if mibBuilder.loadTexts:humidityIdentificationTable.setStatus(_B)
_HumidityIdentificationEntry_Object=MibTableRow
humidityIdentificationEntry=_HumidityIdentificationEntry_Object((1,3,6,1,4,1,534,6,8,1,3,1,1))
humidityIdentificationEntry.setIndexNames((0,_A,_E),(0,_A,_I))
if mibBuilder.loadTexts:humidityIdentificationEntry.setStatus(_B)
class _HumidityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_HumidityIndex_Type.__name__=_G
_HumidityIndex_Object=MibTableColumn
humidityIndex=_HumidityIndex_Object((1,3,6,1,4,1,534,6,8,1,3,1,1,1),_HumidityIndex_Type())
humidityIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:humidityIndex.setStatus(_B)
_HumidityUuid_Type=OctetString
_HumidityUuid_Object=MibTableColumn
humidityUuid=_HumidityUuid_Object((1,3,6,1,4,1,534,6,8,1,3,1,1,2),_HumidityUuid_Type())
humidityUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityUuid.setStatus(_B)
_HumidityConnectionType_Type=ProbeConnectionType
_HumidityConnectionType_Object=MibTableColumn
humidityConnectionType=_HumidityConnectionType_Object((1,3,6,1,4,1,534,6,8,1,3,1,1,3),_HumidityConnectionType_Type())
humidityConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityConnectionType.setStatus(_B)
_HumidityConfigurationTable_Object=MibTable
humidityConfigurationTable=_HumidityConfigurationTable_Object((1,3,6,1,4,1,534,6,8,1,3,2))
if mibBuilder.loadTexts:humidityConfigurationTable.setStatus(_B)
_HumidityConfigurationEntry_Object=MibTableRow
humidityConfigurationEntry=_HumidityConfigurationEntry_Object((1,3,6,1,4,1,534,6,8,1,3,2,1))
humidityConfigurationEntry.setIndexNames((0,_A,_E),(0,_A,_I))
if mibBuilder.loadTexts:humidityConfigurationEntry.setStatus(_B)
class _HumidityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HumidityName_Type.__name__=_F
_HumidityName_Object=MibTableColumn
humidityName=_HumidityName_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,1),_HumidityName_Type())
humidityName.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityName.setStatus(_B)
_HumidityEnable_Type=EnableType
_HumidityEnable_Object=MibTableColumn
humidityEnable=_HumidityEnable_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,2),_HumidityEnable_Type())
humidityEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityEnable.setStatus(_B)
_HumidityOffset_Type=Integer32
_HumidityOffset_Object=MibTableColumn
humidityOffset=_HumidityOffset_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,3),_HumidityOffset_Type())
humidityOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityOffset.setStatus(_B)
_HumidityAlarmEnable_Type=EnableType
_HumidityAlarmEnable_Object=MibTableColumn
humidityAlarmEnable=_HumidityAlarmEnable_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,4),_HumidityAlarmEnable_Type())
humidityAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityAlarmEnable.setStatus(_B)
_HumidityThresholdLowWarning_Type=Integer32
_HumidityThresholdLowWarning_Object=MibTableColumn
humidityThresholdLowWarning=_HumidityThresholdLowWarning_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,5),_HumidityThresholdLowWarning_Type())
humidityThresholdLowWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityThresholdLowWarning.setStatus(_B)
_HumidityThresholdLowCritical_Type=Integer32
_HumidityThresholdLowCritical_Object=MibTableColumn
humidityThresholdLowCritical=_HumidityThresholdLowCritical_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,6),_HumidityThresholdLowCritical_Type())
humidityThresholdLowCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityThresholdLowCritical.setStatus(_B)
_HumidityThresholdHighWarning_Type=Integer32
_HumidityThresholdHighWarning_Object=MibTableColumn
humidityThresholdHighWarning=_HumidityThresholdHighWarning_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,7),_HumidityThresholdHighWarning_Type())
humidityThresholdHighWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityThresholdHighWarning.setStatus(_B)
_HumidityThresholdHighCritical_Type=Integer32
_HumidityThresholdHighCritical_Object=MibTableColumn
humidityThresholdHighCritical=_HumidityThresholdHighCritical_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,8),_HumidityThresholdHighCritical_Type())
humidityThresholdHighCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityThresholdHighCritical.setStatus(_B)
_HumidityThresholdHysteresis_Type=Integer32
_HumidityThresholdHysteresis_Object=MibTableColumn
humidityThresholdHysteresis=_HumidityThresholdHysteresis_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,9),_HumidityThresholdHysteresis_Type())
humidityThresholdHysteresis.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityThresholdHysteresis.setStatus(_B)
class _HumidityAlarmGracePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_HumidityAlarmGracePeriod_Type.__name__=_G
_HumidityAlarmGracePeriod_Object=MibTableColumn
humidityAlarmGracePeriod=_HumidityAlarmGracePeriod_Object((1,3,6,1,4,1,534,6,8,1,3,2,1,10),_HumidityAlarmGracePeriod_Type())
humidityAlarmGracePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityAlarmGracePeriod.setStatus(_B)
_HumidityMonitoringTable_Object=MibTable
humidityMonitoringTable=_HumidityMonitoringTable_Object((1,3,6,1,4,1,534,6,8,1,3,3))
if mibBuilder.loadTexts:humidityMonitoringTable.setStatus(_B)
_HumidityMonitoringEntry_Object=MibTableRow
humidityMonitoringEntry=_HumidityMonitoringEntry_Object((1,3,6,1,4,1,534,6,8,1,3,3,1))
humidityMonitoringEntry.setIndexNames((0,_A,_E),(0,_A,_I))
if mibBuilder.loadTexts:humidityMonitoringEntry.setStatus(_B)
_HumidityAlarm_Type=AlarmType
_HumidityAlarm_Object=MibTableColumn
humidityAlarm=_HumidityAlarm_Object((1,3,6,1,4,1,534,6,8,1,3,3,1,1),_HumidityAlarm_Type())
humidityAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityAlarm.setStatus(_B)
_HumidityAlarmChangeSince_Type=UnixTimeStamp
_HumidityAlarmChangeSince_Object=MibTableColumn
humidityAlarmChangeSince=_HumidityAlarmChangeSince_Object((1,3,6,1,4,1,534,6,8,1,3,3,1,2),_HumidityAlarmChangeSince_Type())
humidityAlarmChangeSince.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityAlarmChangeSince.setStatus(_B)
_HumidityValue_Type=Integer32
_HumidityValue_Object=MibTableColumn
humidityValue=_HumidityValue_Object((1,3,6,1,4,1,534,6,8,1,3,3,1,3),_HumidityValue_Type())
humidityValue.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityValue.setStatus(_B)
_HumidityCommunicationStatus_Type=CommunicationStatus
_HumidityCommunicationStatus_Object=MibTableColumn
humidityCommunicationStatus=_HumidityCommunicationStatus_Object((1,3,6,1,4,1,534,6,8,1,3,3,1,4),_HumidityCommunicationStatus_Type())
humidityCommunicationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityCommunicationStatus.setStatus(_B)
_HumidityCommunicationStatusSince_Type=UnixTimeStamp
_HumidityCommunicationStatusSince_Object=MibTableColumn
humidityCommunicationStatusSince=_HumidityCommunicationStatusSince_Object((1,3,6,1,4,1,534,6,8,1,3,3,1,5),_HumidityCommunicationStatusSince_Type())
humidityCommunicationStatusSince.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityCommunicationStatusSince.setStatus(_B)
_HumidityMonitoringMinMaxTable_Object=MibTable
humidityMonitoringMinMaxTable=_HumidityMonitoringMinMaxTable_Object((1,3,6,1,4,1,534,6,8,1,3,4))
if mibBuilder.loadTexts:humidityMonitoringMinMaxTable.setStatus(_B)
_HumidityMonitoringMinMaxEntry_Object=MibTableRow
humidityMonitoringMinMaxEntry=_HumidityMonitoringMinMaxEntry_Object((1,3,6,1,4,1,534,6,8,1,3,4,1))
humidityMonitoringMinMaxEntry.setIndexNames((0,_A,_E),(0,_A,_I))
if mibBuilder.loadTexts:humidityMonitoringMinMaxEntry.setStatus(_B)
_HumidityMinValue_Type=Integer32
_HumidityMinValue_Object=MibTableColumn
humidityMinValue=_HumidityMinValue_Object((1,3,6,1,4,1,534,6,8,1,3,4,1,1),_HumidityMinValue_Type())
humidityMinValue.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityMinValue.setStatus(_B)
_HumidityMinValueSince_Type=UnixTimeStamp
_HumidityMinValueSince_Object=MibTableColumn
humidityMinValueSince=_HumidityMinValueSince_Object((1,3,6,1,4,1,534,6,8,1,3,4,1,2),_HumidityMinValueSince_Type())
humidityMinValueSince.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityMinValueSince.setStatus(_B)
_HumidityMaxValue_Type=Integer32
_HumidityMaxValue_Object=MibTableColumn
humidityMaxValue=_HumidityMaxValue_Object((1,3,6,1,4,1,534,6,8,1,3,4,1,3),_HumidityMaxValue_Type())
humidityMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityMaxValue.setStatus(_B)
_HumidityMaxValueSince_Type=UnixTimeStamp
_HumidityMaxValueSince_Object=MibTableColumn
humidityMaxValueSince=_HumidityMaxValueSince_Object((1,3,6,1,4,1,534,6,8,1,3,4,1,4),_HumidityMaxValueSince_Type())
humidityMaxValueSince.setMaxAccess(_C)
if mibBuilder.loadTexts:humidityMaxValueSince.setStatus(_B)
_HumidityResetMinMax_Type=ResetCommandType
_HumidityResetMinMax_Object=MibTableColumn
humidityResetMinMax=_HumidityResetMinMax_Object((1,3,6,1,4,1,534,6,8,1,3,4,1,5),_HumidityResetMinMax_Type())
humidityResetMinMax.setMaxAccess(_D)
if mibBuilder.loadTexts:humidityResetMinMax.setStatus(_B)
_DigitalInput_ObjectIdentity=ObjectIdentity
digitalInput=_DigitalInput_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,4))
_DigitalInputNotification_ObjectIdentity=ObjectIdentity
digitalInputNotification=_DigitalInputNotification_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,4,0))
_DigitalInputIdentificationTable_Object=MibTable
digitalInputIdentificationTable=_DigitalInputIdentificationTable_Object((1,3,6,1,4,1,534,6,8,1,4,1))
if mibBuilder.loadTexts:digitalInputIdentificationTable.setStatus(_B)
_DigitalInputIdentificationEntry_Object=MibTableRow
digitalInputIdentificationEntry=_DigitalInputIdentificationEntry_Object((1,3,6,1,4,1,534,6,8,1,4,1,1))
digitalInputIdentificationEntry.setIndexNames((0,_A,_E),(0,_A,_J))
if mibBuilder.loadTexts:digitalInputIdentificationEntry.setStatus(_B)
class _DigitalInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DigitalInputIndex_Type.__name__=_G
_DigitalInputIndex_Object=MibTableColumn
digitalInputIndex=_DigitalInputIndex_Object((1,3,6,1,4,1,534,6,8,1,4,1,1,1),_DigitalInputIndex_Type())
digitalInputIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:digitalInputIndex.setStatus(_B)
_DigitalInputUuid_Type=OctetString
_DigitalInputUuid_Object=MibTableColumn
digitalInputUuid=_DigitalInputUuid_Object((1,3,6,1,4,1,534,6,8,1,4,1,1,2),_DigitalInputUuid_Type())
digitalInputUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputUuid.setStatus(_B)
_DigitalInputConnectionType_Type=ProbeConnectionType
_DigitalInputConnectionType_Object=MibTableColumn
digitalInputConnectionType=_DigitalInputConnectionType_Object((1,3,6,1,4,1,534,6,8,1,4,1,1,3),_DigitalInputConnectionType_Type())
digitalInputConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputConnectionType.setStatus(_B)
_DigitalInputConfigurationTable_Object=MibTable
digitalInputConfigurationTable=_DigitalInputConfigurationTable_Object((1,3,6,1,4,1,534,6,8,1,4,2))
if mibBuilder.loadTexts:digitalInputConfigurationTable.setStatus(_B)
_DigitalInputConfigurationEntry_Object=MibTableRow
digitalInputConfigurationEntry=_DigitalInputConfigurationEntry_Object((1,3,6,1,4,1,534,6,8,1,4,2,1))
digitalInputConfigurationEntry.setIndexNames((0,_A,_E),(0,_A,_J))
if mibBuilder.loadTexts:digitalInputConfigurationEntry.setStatus(_B)
class _DigitalInputName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_DigitalInputName_Type.__name__=_F
_DigitalInputName_Object=MibTableColumn
digitalInputName=_DigitalInputName_Object((1,3,6,1,4,1,534,6,8,1,4,2,1,1),_DigitalInputName_Type())
digitalInputName.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInputName.setStatus(_B)
_DigitalInputEnable_Type=EnableType
_DigitalInputEnable_Object=MibTableColumn
digitalInputEnable=_DigitalInputEnable_Object((1,3,6,1,4,1,534,6,8,1,4,2,1,2),_DigitalInputEnable_Type())
digitalInputEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInputEnable.setStatus(_B)
_DigitalInputPolarity_Type=PolarityType
_DigitalInputPolarity_Object=MibTableColumn
digitalInputPolarity=_DigitalInputPolarity_Object((1,3,6,1,4,1,534,6,8,1,4,2,1,3),_DigitalInputPolarity_Type())
digitalInputPolarity.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInputPolarity.setStatus(_B)
_DigitalInputAlarmEnable_Type=EnableType
_DigitalInputAlarmEnable_Object=MibTableColumn
digitalInputAlarmEnable=_DigitalInputAlarmEnable_Object((1,3,6,1,4,1,534,6,8,1,4,2,1,4),_DigitalInputAlarmEnable_Type())
digitalInputAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInputAlarmEnable.setStatus(_B)
_DigitalInputAlarmSeverity_Type=AlarmSeverityType
_DigitalInputAlarmSeverity_Object=MibTableColumn
digitalInputAlarmSeverity=_DigitalInputAlarmSeverity_Object((1,3,6,1,4,1,534,6,8,1,4,2,1,5),_DigitalInputAlarmSeverity_Type())
digitalInputAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInputAlarmSeverity.setStatus(_B)
class _DigitalInputAlarmGracePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_DigitalInputAlarmGracePeriod_Type.__name__=_G
_DigitalInputAlarmGracePeriod_Object=MibTableColumn
digitalInputAlarmGracePeriod=_DigitalInputAlarmGracePeriod_Object((1,3,6,1,4,1,534,6,8,1,4,2,1,6),_DigitalInputAlarmGracePeriod_Type())
digitalInputAlarmGracePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInputAlarmGracePeriod.setStatus(_B)
_DigitalInputMonitoringTable_Object=MibTable
digitalInputMonitoringTable=_DigitalInputMonitoringTable_Object((1,3,6,1,4,1,534,6,8,1,4,3))
if mibBuilder.loadTexts:digitalInputMonitoringTable.setStatus(_B)
_DigitalInputMonitoringEntry_Object=MibTableRow
digitalInputMonitoringEntry=_DigitalInputMonitoringEntry_Object((1,3,6,1,4,1,534,6,8,1,4,3,1))
digitalInputMonitoringEntry.setIndexNames((0,_A,_E),(0,_A,_J))
if mibBuilder.loadTexts:digitalInputMonitoringEntry.setStatus(_B)
_DigitalInputAlarm_Type=AlarmLevelType
_DigitalInputAlarm_Object=MibTableColumn
digitalInputAlarm=_DigitalInputAlarm_Object((1,3,6,1,4,1,534,6,8,1,4,3,1,1),_DigitalInputAlarm_Type())
digitalInputAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputAlarm.setStatus(_B)
_DigitalInputAlarmChangeSince_Type=UnixTimeStamp
_DigitalInputAlarmChangeSince_Object=MibTableColumn
digitalInputAlarmChangeSince=_DigitalInputAlarmChangeSince_Object((1,3,6,1,4,1,534,6,8,1,4,3,1,2),_DigitalInputAlarmChangeSince_Type())
digitalInputAlarmChangeSince.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputAlarmChangeSince.setStatus(_B)
_DigitalInputState_Type=StateType
_DigitalInputState_Object=MibTableColumn
digitalInputState=_DigitalInputState_Object((1,3,6,1,4,1,534,6,8,1,4,3,1,3),_DigitalInputState_Type())
digitalInputState.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputState.setStatus(_B)
_DigitalInputStateSince_Type=UnixTimeStamp
_DigitalInputStateSince_Object=MibTableColumn
digitalInputStateSince=_DigitalInputStateSince_Object((1,3,6,1,4,1,534,6,8,1,4,3,1,4),_DigitalInputStateSince_Type())
digitalInputStateSince.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputStateSince.setStatus(_B)
_DigitalInputCommunicationStatus_Type=CommunicationStatus
_DigitalInputCommunicationStatus_Object=MibTableColumn
digitalInputCommunicationStatus=_DigitalInputCommunicationStatus_Object((1,3,6,1,4,1,534,6,8,1,4,3,1,5),_DigitalInputCommunicationStatus_Type())
digitalInputCommunicationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputCommunicationStatus.setStatus(_B)
_DigitalInputCommunicationStatusSince_Type=UnixTimeStamp
_DigitalInputCommunicationStatusSince_Object=MibTableColumn
digitalInputCommunicationStatusSince=_DigitalInputCommunicationStatusSince_Object((1,3,6,1,4,1,534,6,8,1,4,3,1,6),_DigitalInputCommunicationStatusSince_Type())
digitalInputCommunicationStatusSince.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputCommunicationStatusSince.setStatus(_B)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,10))
_ObjectGroups_ObjectIdentity=ObjectIdentity
objectGroups=_ObjectGroups_ObjectIdentity((1,3,6,1,4,1,534,6,8,1,10,2))
sensorRequiredGroup=ObjectGroup((1,3,6,1,4,1,534,6,8,1,10,2,1))
sensorRequiredGroup.setObjects(*((_A,_P),(_A,_E),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_Q),(_A,_R),(_A,_s),(_A,_t),(_A,_u),(_A,_H),(_A,_v),(_A,_S),(_A,_w),(_A,_I),(_A,_x),(_A,_T),(_A,_J),(_A,_y)))
if mibBuilder.loadTexts:sensorRequiredGroup.setStatus(_B)
sensorOptionalGroup=ObjectGroup((1,3,6,1,4,1,534,6,8,1,10,2,2))
sensorOptionalGroup.setObjects(*((_A,_U),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_L),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_M),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_N),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:sensorOptionalGroup.setStatus(_B)
notifySensorCount=NotificationType((1,3,6,1,4,1,534,6,8,1,1,0,1))
notifySensorCount.setObjects((_A,_P))
if mibBuilder.loadTexts:notifySensorCount.setStatus(_B)
notifySensorStatus=NotificationType((1,3,6,1,4,1,534,6,8,1,1,0,2))
notifySensorStatus.setObjects(*((_A,_E),(_A,_U),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:notifySensorStatus.setStatus(_B)
notifyTemperatureAlarm=NotificationType((1,3,6,1,4,1,534,6,8,1,2,0,1))
notifyTemperatureAlarm.setObjects(*((_A,_E),(_A,_H),(_A,_L),(_A,_V),(_A,_W),(_A,_S)))
if mibBuilder.loadTexts:notifyTemperatureAlarm.setStatus(_B)
notifyTemperatureCommunicationStatus=NotificationType((1,3,6,1,4,1,534,6,8,1,2,0,2))
notifyTemperatureCommunicationStatus.setObjects(*((_A,_E),(_A,_H),(_A,_L),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:notifyTemperatureCommunicationStatus.setStatus(_B)
notifyHumidityAlarm=NotificationType((1,3,6,1,4,1,534,6,8,1,3,0,1))
notifyHumidityAlarm.setObjects(*((_A,_E),(_A,_I),(_A,_M),(_A,_Z),(_A,_a),(_A,_T)))
if mibBuilder.loadTexts:notifyHumidityAlarm.setStatus(_B)
notifyHumidityCommunicationStatus=NotificationType((1,3,6,1,4,1,534,6,8,1,3,0,2))
notifyHumidityCommunicationStatus.setObjects(*((_A,_E),(_A,_I),(_A,_M),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:notifyHumidityCommunicationStatus.setStatus(_B)
notifyDigitalInputAlarm=NotificationType((1,3,6,1,4,1,534,6,8,1,4,0,1))
notifyDigitalInputAlarm.setObjects(*((_A,_E),(_A,_J),(_A,_N),(_A,_f),(_A,_g),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:notifyDigitalInputAlarm.setStatus(_B)
notifydigitalInputCommunicationStatus=NotificationType((1,3,6,1,4,1,534,6,8,1,4,0,2))
notifydigitalInputCommunicationStatus.setObjects(*((_A,_E),(_A,_J),(_A,_N),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:notifydigitalInputCommunicationStatus.setStatus(_B)
sensorNotifyGroup=NotificationGroup((1,3,6,1,4,1,534,6,8,1,10,2,3))
sensorNotifyGroup.setObjects(*((_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:sensorNotifyGroup.setStatus(_B)
eatonSensorCompliances=ModuleCompliance((1,3,6,1,4,1,534,6,8,1,10,1))
eatonSensorCompliances.setObjects(*((_A,_Ap),(_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:eatonSensorCompliances.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'UnixTimeStamp':UnixTimeStamp,'PositionType':PositionType,'ElevationType':ElevationType,'CommunicationStatus':CommunicationStatus,'ProbeConnectionType':ProbeConnectionType,'EnableType':EnableType,'AlarmType':AlarmType,'ResetCommandType':ResetCommandType,'PolarityType':PolarityType,'AlarmSeverityType':AlarmSeverityType,'AlarmLevelType':AlarmLevelType,'StateType':StateType,'TemperatureUnitType':TemperatureUnitType,'eatonSensor':eatonSensor,'sensor':sensor,'sensorNotification':sensorNotification,_Ai:notifySensorCount,_Ah:notifySensorStatus,_P:sensorCount,'sensorIdentificationTable':sensorIdentificationTable,'sensorIdentificationEntry':sensorIdentificationEntry,_E:sensorIndex,_U:sensorUuid,_z:sensorConnectionType,_A0:sensorAddress,_A1:sensorMonitoredBy,_m:sensorManufacturer,_n:sensorModel,_o:sensorPartNumber,_p:sensorSerialNumber,_q:sensorFirmwareVersion,'sensorConfigurationTable':sensorConfigurationTable,'sensorConfigurationEntry':sensorConfigurationEntry,_r:sensorName,_A2:sensorLocation,_A3:sensorPosition,_A4:sensorElevation,_A5:sensorUElevation,'sensorMonitoringTable':sensorMonitoringTable,'sensorMonitoringEntry':sensorMonitoringEntry,_Q:sensorStatus,_R:sensorStatusSince,_s:sensorTemperatureCount,_t:sensorHumidityCount,_u:sensorDigitalInputCount,_A6:sensorAnalogInputCount,'temperature':temperature,'temperatureNotification':temperatureNotification,_Aj:notifyTemperatureAlarm,_Ak:notifyTemperatureCommunicationStatus,'temperatureIdentificationTable':temperatureIdentificationTable,'temperatureIdentificationEntry':temperatureIdentificationEntry,_H:temperatureIndex,_L:temperatureUuid,_A7:temperatureConnectionType,'temperatureConfigurationTable':temperatureConfigurationTable,'temperatureConfigurationEntry':temperatureConfigurationEntry,_v:temperatureName,_A8:temperatureEnable,_A9:temperatureOffset,_AA:temperatureAlarmEnable,_AB:temperatureThresholdLowWarning,_AC:temperatureThresholdLowCritical,_AD:temperatureThresholdHighWarning,_AE:temperatureThresholdHighCritical,_AF:temperatureThresholdHysteresis,_AG:temperatureAlarmGracePeriod,'temperatureMonitoringTable':temperatureMonitoringTable,'temperatureMonitoringEntry':temperatureMonitoringEntry,_V:temperatureAlarm,_W:temperatureAlarmChangeSince,_S:temperatureValue,_X:temperatureCommunicationStatus,_Y:temperatureCommunicationStatusSince,'temperatureMonitoringMinMaxTable':temperatureMonitoringMinMaxTable,'temperatureMonitoringMinMaxEntry':temperatureMonitoringMinMaxEntry,_AH:temperatureMinValue,_AI:temperatureMinValueSince,_AJ:temperatureMaxValue,_AK:temperatureMaxValueSince,_AL:temperatureResetMinMax,_w:temperatureUnit,'humidity':humidity,'humidityNotification':humidityNotification,_Al:notifyHumidityAlarm,_Am:notifyHumidityCommunicationStatus,'humidityIdentificationTable':humidityIdentificationTable,'humidityIdentificationEntry':humidityIdentificationEntry,_I:humidityIndex,_M:humidityUuid,_AM:humidityConnectionType,'humidityConfigurationTable':humidityConfigurationTable,'humidityConfigurationEntry':humidityConfigurationEntry,_x:humidityName,_AN:humidityEnable,_AO:humidityOffset,_AP:humidityAlarmEnable,_AQ:humidityThresholdLowWarning,_AR:humidityThresholdLowCritical,_AS:humidityThresholdHighWarning,_AT:humidityThresholdHighCritical,_AU:humidityThresholdHysteresis,_AV:humidityAlarmGracePeriod,'humidityMonitoringTable':humidityMonitoringTable,'humidityMonitoringEntry':humidityMonitoringEntry,_Z:humidityAlarm,_a:humidityAlarmChangeSince,_T:humidityValue,_b:humidityCommunicationStatus,_c:humidityCommunicationStatusSince,'humidityMonitoringMinMaxTable':humidityMonitoringMinMaxTable,'humidityMonitoringMinMaxEntry':humidityMonitoringMinMaxEntry,_AW:humidityMinValue,_AX:humidityMinValueSince,_AY:humidityMaxValue,_AZ:humidityMaxValueSince,_Aa:humidityResetMinMax,'digitalInput':digitalInput,'digitalInputNotification':digitalInputNotification,_An:notifyDigitalInputAlarm,_Ao:notifydigitalInputCommunicationStatus,'digitalInputIdentificationTable':digitalInputIdentificationTable,'digitalInputIdentificationEntry':digitalInputIdentificationEntry,_J:digitalInputIndex,_N:digitalInputUuid,_Ab:digitalInputConnectionType,'digitalInputConfigurationTable':digitalInputConfigurationTable,'digitalInputConfigurationEntry':digitalInputConfigurationEntry,_y:digitalInputName,_Ac:digitalInputEnable,_Ad:digitalInputPolarity,_Ae:digitalInputAlarmEnable,_Af:digitalInputAlarmSeverity,_Ag:digitalInputAlarmGracePeriod,'digitalInputMonitoringTable':digitalInputMonitoringTable,'digitalInputMonitoringEntry':digitalInputMonitoringEntry,_f:digitalInputAlarm,_g:digitalInputAlarmChangeSince,_d:digitalInputState,_e:digitalInputStateSince,_h:digitalInputCommunicationStatus,_i:digitalInputCommunicationStatusSince,'conformance':conformance,'eatonSensorCompliances':eatonSensorCompliances,'objectGroups':objectGroups,_Ap:sensorRequiredGroup,_Aq:sensorOptionalGroup,_Ar:sensorNotifyGroup})