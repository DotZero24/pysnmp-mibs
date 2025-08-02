_Y='sensorGroupStatusIndex'
_X='pending'
_W='unreliable'
_V='updating'
_U='actorGroupStatusIndex'
_T='sensorListIndex'
_S='actorListIndex'
_R='deviceInformationIndex'
_Q='sensorGroupConfigIndex'
_P='actorGroupConfigIndex'
_O='deviceConfigIndex'
_N='passive'
_M='directorConfigIndex'
_L='manually'
_K='ok'
_J='failed'
_I='enabled'
_H='unknown'
_G='not-accessible'
_F='disabled'
_E='G6-SMARTOFFICE-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
device=ModuleIdentity((1,3,6,1,4,1,3181,10,6,4))
if mibBuilder.loadTexts:device.setRevisions(('2018-02-12 16:19',))
_Smartoffice_ObjectIdentity=ObjectIdentity
smartoffice=_Smartoffice_ObjectIdentity((1,3,6,1,4,1,3181,10,6,4,99))
class _SmartofficeEnableSmartOffice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_I,1)))
_SmartofficeEnableSmartOffice_Type.__name__=_D
_SmartofficeEnableSmartOffice_Object=MibScalar
smartofficeEnableSmartOffice=_SmartofficeEnableSmartOffice_Object((1,3,6,1,4,1,3181,10,6,4,99,1),_SmartofficeEnableSmartOffice_Type())
smartofficeEnableSmartOffice.setMaxAccess(_C)
if mibBuilder.loadTexts:smartofficeEnableSmartOffice.setStatus(_A)
_DirectorConfigTable_Object=MibTable
directorConfigTable=_DirectorConfigTable_Object((1,3,6,1,4,1,3181,10,6,4,99,2))
if mibBuilder.loadTexts:directorConfigTable.setStatus(_A)
_DirectorConfigEntry_Object=MibTableRow
directorConfigEntry=_DirectorConfigEntry_Object((1,3,6,1,4,1,3181,10,6,4,99,2,1))
directorConfigEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:directorConfigEntry.setStatus(_A)
class _DirectorConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_DirectorConfigIndex_Type.__name__=_D
_DirectorConfigIndex_Object=MibTableColumn
directorConfigIndex=_DirectorConfigIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,2,1,1),_DirectorConfigIndex_Type())
directorConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:directorConfigIndex.setStatus(_A)
_DirectorConfigDomainName_Type=DisplayString
_DirectorConfigDomainName_Object=MibTableColumn
directorConfigDomainName=_DirectorConfigDomainName_Object((1,3,6,1,4,1,3181,10,6,4,99,2,1,2),_DirectorConfigDomainName_Type())
directorConfigDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:directorConfigDomainName.setStatus(_A)
class _DirectorConfigGeneralMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('automatic',1),(_N,2)))
_DirectorConfigGeneralMode_Type.__name__=_D
_DirectorConfigGeneralMode_Object=MibTableColumn
directorConfigGeneralMode=_DirectorConfigGeneralMode_Object((1,3,6,1,4,1,3181,10,6,4,99,2,1,3),_DirectorConfigGeneralMode_Type())
directorConfigGeneralMode.setMaxAccess(_C)
if mibBuilder.loadTexts:directorConfigGeneralMode.setStatus(_A)
class _DirectorConfigActOnUngroupedSensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_I,1)))
_DirectorConfigActOnUngroupedSensors_Type.__name__=_D
_DirectorConfigActOnUngroupedSensors_Object=MibTableColumn
directorConfigActOnUngroupedSensors=_DirectorConfigActOnUngroupedSensors_Object((1,3,6,1,4,1,3181,10,6,4,99,2,1,4),_DirectorConfigActOnUngroupedSensors_Type())
directorConfigActOnUngroupedSensors.setMaxAccess(_C)
if mibBuilder.loadTexts:directorConfigActOnUngroupedSensors.setStatus(_A)
_DirectorConfigScanLightControllers_Type=DisplayString
_DirectorConfigScanLightControllers_Object=MibTableColumn
directorConfigScanLightControllers=_DirectorConfigScanLightControllers_Object((1,3,6,1,4,1,3181,10,6,4,99,2,1,5),_DirectorConfigScanLightControllers_Type())
directorConfigScanLightControllers.setMaxAccess(_C)
if mibBuilder.loadTexts:directorConfigScanLightControllers.setStatus(_A)
_DeviceConfigTable_Object=MibTable
deviceConfigTable=_DeviceConfigTable_Object((1,3,6,1,4,1,3181,10,6,4,99,3))
if mibBuilder.loadTexts:deviceConfigTable.setStatus(_A)
_DeviceConfigEntry_Object=MibTableRow
deviceConfigEntry=_DeviceConfigEntry_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1))
deviceConfigEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:deviceConfigEntry.setStatus(_A)
class _DeviceConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_DeviceConfigIndex_Type.__name__=_D
_DeviceConfigIndex_Object=MibTableColumn
deviceConfigIndex=_DeviceConfigIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,1),_DeviceConfigIndex_Type())
deviceConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:deviceConfigIndex.setStatus(_A)
_DeviceConfigDeviceName_Type=DisplayString
_DeviceConfigDeviceName_Object=MibTableColumn
deviceConfigDeviceName=_DeviceConfigDeviceName_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,2),_DeviceConfigDeviceName_Type())
deviceConfigDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigDeviceName.setStatus(_A)
_DeviceConfigLocation_Type=DisplayString
_DeviceConfigLocation_Object=MibTableColumn
deviceConfigLocation=_DeviceConfigLocation_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,3),_DeviceConfigLocation_Type())
deviceConfigLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigLocation.setStatus(_A)
_DeviceConfigLatitude_Type=DisplayString
_DeviceConfigLatitude_Object=MibTableColumn
deviceConfigLatitude=_DeviceConfigLatitude_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,4),_DeviceConfigLatitude_Type())
deviceConfigLatitude.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigLatitude.setStatus(_A)
_DeviceConfigLongitude_Type=DisplayString
_DeviceConfigLongitude_Object=MibTableColumn
deviceConfigLongitude=_DeviceConfigLongitude_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,5),_DeviceConfigLongitude_Type())
deviceConfigLongitude.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigLongitude.setStatus(_A)
_DeviceConfigAltitude_Type=DisplayString
_DeviceConfigAltitude_Object=MibTableColumn
deviceConfigAltitude=_DeviceConfigAltitude_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,6),_DeviceConfigAltitude_Type())
deviceConfigAltitude.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigAltitude.setStatus(_A)
class _DeviceConfigPlacement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('unset',0),('floor',1),('wall',2),('ceiling',3),('duct',4),('outside',5),('desk',6)))
_DeviceConfigPlacement_Type.__name__=_D
_DeviceConfigPlacement_Object=MibTableColumn
deviceConfigPlacement=_DeviceConfigPlacement_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,7),_DeviceConfigPlacement_Type())
deviceConfigPlacement.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigPlacement.setStatus(_A)
class _DeviceConfigProductType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('virtual',0),('smartlightController',1),('directorCascade',2),('hm',3),('fhem',4),('ip500',5),('enocean',6),('knx',7)))
_DeviceConfigProductType_Type.__name__=_D
_DeviceConfigProductType_Object=MibTableColumn
deviceConfigProductType=_DeviceConfigProductType_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,8),_DeviceConfigProductType_Type())
deviceConfigProductType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigProductType.setStatus(_A)
_DeviceConfigDeviceId_Type=DisplayString
_DeviceConfigDeviceId_Object=MibTableColumn
deviceConfigDeviceId=_DeviceConfigDeviceId_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,9),_DeviceConfigDeviceId_Type())
deviceConfigDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigDeviceId.setStatus(_A)
_DeviceConfigNetworkAddress_Type=DisplayString
_DeviceConfigNetworkAddress_Object=MibTableColumn
deviceConfigNetworkAddress=_DeviceConfigNetworkAddress_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,10),_DeviceConfigNetworkAddress_Type())
deviceConfigNetworkAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigNetworkAddress.setStatus(_A)
_DeviceConfigAdditionalParameter_Type=DisplayString
_DeviceConfigAdditionalParameter_Object=MibTableColumn
deviceConfigAdditionalParameter=_DeviceConfigAdditionalParameter_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,11),_DeviceConfigAdditionalParameter_Type())
deviceConfigAdditionalParameter.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigAdditionalParameter.setStatus(_A)
class _DeviceConfigNetworkFailureAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('keepCurrent',0),('off',1),('on',2),('dimmed',3)))
_DeviceConfigNetworkFailureAction_Type.__name__=_D
_DeviceConfigNetworkFailureAction_Object=MibTableColumn
deviceConfigNetworkFailureAction=_DeviceConfigNetworkFailureAction_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,12),_DeviceConfigNetworkFailureAction_Type())
deviceConfigNetworkFailureAction.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigNetworkFailureAction.setStatus(_A)
_DeviceConfigIdentify_Type=DisplayString
_DeviceConfigIdentify_Object=MibTableColumn
deviceConfigIdentify=_DeviceConfigIdentify_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,13),_DeviceConfigIdentify_Type())
deviceConfigIdentify.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigIdentify.setStatus(_A)
_DeviceConfigRestart_Type=DisplayString
_DeviceConfigRestart_Object=MibTableColumn
deviceConfigRestart=_DeviceConfigRestart_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,14),_DeviceConfigRestart_Type())
deviceConfigRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigRestart.setStatus(_A)
_DeviceConfigCalibrate_Type=DisplayString
_DeviceConfigCalibrate_Object=MibTableColumn
deviceConfigCalibrate=_DeviceConfigCalibrate_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,15),_DeviceConfigCalibrate_Type())
deviceConfigCalibrate.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigCalibrate.setStatus(_A)
_DeviceConfigPair_Type=DisplayString
_DeviceConfigPair_Object=MibTableColumn
deviceConfigPair=_DeviceConfigPair_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,16),_DeviceConfigPair_Type())
deviceConfigPair.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigPair.setStatus(_A)
_DeviceConfigUnpair_Type=DisplayString
_DeviceConfigUnpair_Object=MibTableColumn
deviceConfigUnpair=_DeviceConfigUnpair_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,17),_DeviceConfigUnpair_Type())
deviceConfigUnpair.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigUnpair.setStatus(_A)
_DeviceConfigUpdateFirmware_Type=DisplayString
_DeviceConfigUpdateFirmware_Object=MibTableColumn
deviceConfigUpdateFirmware=_DeviceConfigUpdateFirmware_Object((1,3,6,1,4,1,3181,10,6,4,99,3,1,18),_DeviceConfigUpdateFirmware_Type())
deviceConfigUpdateFirmware.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceConfigUpdateFirmware.setStatus(_A)
_ActorGroupConfigTable_Object=MibTable
actorGroupConfigTable=_ActorGroupConfigTable_Object((1,3,6,1,4,1,3181,10,6,4,99,4))
if mibBuilder.loadTexts:actorGroupConfigTable.setStatus(_A)
_ActorGroupConfigEntry_Object=MibTableRow
actorGroupConfigEntry=_ActorGroupConfigEntry_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1))
actorGroupConfigEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:actorGroupConfigEntry.setStatus(_A)
class _ActorGroupConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ActorGroupConfigIndex_Type.__name__=_D
_ActorGroupConfigIndex_Object=MibTableColumn
actorGroupConfigIndex=_ActorGroupConfigIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1,1),_ActorGroupConfigIndex_Type())
actorGroupConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:actorGroupConfigIndex.setStatus(_A)
_ActorGroupConfigGroupName_Type=DisplayString
_ActorGroupConfigGroupName_Object=MibTableColumn
actorGroupConfigGroupName=_ActorGroupConfigGroupName_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1,2),_ActorGroupConfigGroupName_Type())
actorGroupConfigGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:actorGroupConfigGroupName.setStatus(_A)
_ActorGroupConfigAttribute_Type=DisplayString
_ActorGroupConfigAttribute_Object=MibTableColumn
actorGroupConfigAttribute=_ActorGroupConfigAttribute_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1,3),_ActorGroupConfigAttribute_Type())
actorGroupConfigAttribute.setMaxAccess(_C)
if mibBuilder.loadTexts:actorGroupConfigAttribute.setStatus(_A)
_ActorGroupConfigAssociatedDevices_Type=DisplayString
_ActorGroupConfigAssociatedDevices_Object=MibTableColumn
actorGroupConfigAssociatedDevices=_ActorGroupConfigAssociatedDevices_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1,4),_ActorGroupConfigAssociatedDevices_Type())
actorGroupConfigAssociatedDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:actorGroupConfigAssociatedDevices.setStatus(_A)
_ActorGroupConfigAdditionalParameter_Type=DisplayString
_ActorGroupConfigAdditionalParameter_Object=MibTableColumn
actorGroupConfigAdditionalParameter=_ActorGroupConfigAdditionalParameter_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1,5),_ActorGroupConfigAdditionalParameter_Type())
actorGroupConfigAdditionalParameter.setMaxAccess(_C)
if mibBuilder.loadTexts:actorGroupConfigAdditionalParameter.setStatus(_A)
_ActorGroupConfigDefaultValue_Type=DisplayString
_ActorGroupConfigDefaultValue_Object=MibTableColumn
actorGroupConfigDefaultValue=_ActorGroupConfigDefaultValue_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1,6),_ActorGroupConfigDefaultValue_Type())
actorGroupConfigDefaultValue.setMaxAccess(_C)
if mibBuilder.loadTexts:actorGroupConfigDefaultValue.setStatus(_A)
class _ActorGroupConfigValueCaching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_I,1)))
_ActorGroupConfigValueCaching_Type.__name__=_D
_ActorGroupConfigValueCaching_Object=MibTableColumn
actorGroupConfigValueCaching=_ActorGroupConfigValueCaching_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1,7),_ActorGroupConfigValueCaching_Type())
actorGroupConfigValueCaching.setMaxAccess(_C)
if mibBuilder.loadTexts:actorGroupConfigValueCaching.setStatus(_A)
_ActorGroupConfigAdditionalScriptName_Type=DisplayString
_ActorGroupConfigAdditionalScriptName_Object=MibTableColumn
actorGroupConfigAdditionalScriptName=_ActorGroupConfigAdditionalScriptName_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1,8),_ActorGroupConfigAdditionalScriptName_Type())
actorGroupConfigAdditionalScriptName.setMaxAccess(_C)
if mibBuilder.loadTexts:actorGroupConfigAdditionalScriptName.setStatus(_A)
_ActorGroupConfigManualSetValue_Type=DisplayString
_ActorGroupConfigManualSetValue_Object=MibTableColumn
actorGroupConfigManualSetValue=_ActorGroupConfigManualSetValue_Object((1,3,6,1,4,1,3181,10,6,4,99,4,1,9),_ActorGroupConfigManualSetValue_Type())
actorGroupConfigManualSetValue.setMaxAccess(_C)
if mibBuilder.loadTexts:actorGroupConfigManualSetValue.setStatus(_A)
_SensorGroupConfigTable_Object=MibTable
sensorGroupConfigTable=_SensorGroupConfigTable_Object((1,3,6,1,4,1,3181,10,6,4,99,5))
if mibBuilder.loadTexts:sensorGroupConfigTable.setStatus(_A)
_SensorGroupConfigEntry_Object=MibTableRow
sensorGroupConfigEntry=_SensorGroupConfigEntry_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1))
sensorGroupConfigEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:sensorGroupConfigEntry.setStatus(_A)
class _SensorGroupConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SensorGroupConfigIndex_Type.__name__=_D
_SensorGroupConfigIndex_Object=MibTableColumn
sensorGroupConfigIndex=_SensorGroupConfigIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,1),_SensorGroupConfigIndex_Type())
sensorGroupConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sensorGroupConfigIndex.setStatus(_A)
_SensorGroupConfigGroupName_Type=DisplayString
_SensorGroupConfigGroupName_Object=MibTableColumn
sensorGroupConfigGroupName=_SensorGroupConfigGroupName_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,2),_SensorGroupConfigGroupName_Type())
sensorGroupConfigGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigGroupName.setStatus(_A)
_SensorGroupConfigAttribute_Type=DisplayString
_SensorGroupConfigAttribute_Object=MibTableColumn
sensorGroupConfigAttribute=_SensorGroupConfigAttribute_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,3),_SensorGroupConfigAttribute_Type())
sensorGroupConfigAttribute.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigAttribute.setStatus(_A)
_SensorGroupConfigAssociatedDevices_Type=DisplayString
_SensorGroupConfigAssociatedDevices_Object=MibTableColumn
sensorGroupConfigAssociatedDevices=_SensorGroupConfigAssociatedDevices_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,4),_SensorGroupConfigAssociatedDevices_Type())
sensorGroupConfigAssociatedDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigAssociatedDevices.setStatus(_A)
class _SensorGroupConfigValueCaching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_I,1)))
_SensorGroupConfigValueCaching_Type.__name__=_D
_SensorGroupConfigValueCaching_Object=MibTableColumn
sensorGroupConfigValueCaching=_SensorGroupConfigValueCaching_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,5),_SensorGroupConfigValueCaching_Type())
sensorGroupConfigValueCaching.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigValueCaching.setStatus(_A)
class _SensorGroupConfigRunScriptWhen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,0),('anyChange',1),('limitCrossed',2),('avgAbsolute',3),('avgPercent',4),('totalAbsolute',5),('totalPercent',6),('newPeakLevel',7),('anyUpdate',8),('zeroCrossing',9)))
_SensorGroupConfigRunScriptWhen_Type.__name__=_D
_SensorGroupConfigRunScriptWhen_Object=MibTableColumn
sensorGroupConfigRunScriptWhen=_SensorGroupConfigRunScriptWhen_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,6),_SensorGroupConfigRunScriptWhen_Type())
sensorGroupConfigRunScriptWhen.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigRunScriptWhen.setStatus(_A)
_SensorGroupConfigRunScriptDelta_Type=DisplayString
_SensorGroupConfigRunScriptDelta_Object=MibTableColumn
sensorGroupConfigRunScriptDelta=_SensorGroupConfigRunScriptDelta_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,7),_SensorGroupConfigRunScriptDelta_Type())
sensorGroupConfigRunScriptDelta.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigRunScriptDelta.setStatus(_A)
_SensorGroupConfigScriptName_Type=DisplayString
_SensorGroupConfigScriptName_Object=MibTableColumn
sensorGroupConfigScriptName=_SensorGroupConfigScriptName_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,8),_SensorGroupConfigScriptName_Type())
sensorGroupConfigScriptName.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigScriptName.setStatus(_A)
_SensorGroupConfigAdditionalScriptName_Type=DisplayString
_SensorGroupConfigAdditionalScriptName_Object=MibTableColumn
sensorGroupConfigAdditionalScriptName=_SensorGroupConfigAdditionalScriptName_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,9),_SensorGroupConfigAdditionalScriptName_Type())
sensorGroupConfigAdditionalScriptName.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigAdditionalScriptName.setStatus(_A)
class _SensorGroupConfigReportMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_N,1),('deltaPercent',2),('deltaAbsolute',3),('onThreshold',4),('test',5)))
_SensorGroupConfigReportMode_Type.__name__=_D
_SensorGroupConfigReportMode_Object=MibTableColumn
sensorGroupConfigReportMode=_SensorGroupConfigReportMode_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,10),_SensorGroupConfigReportMode_Type())
sensorGroupConfigReportMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigReportMode.setStatus(_A)
_SensorGroupConfigAdditionalParameter_Type=DisplayString
_SensorGroupConfigAdditionalParameter_Object=MibTableColumn
sensorGroupConfigAdditionalParameter=_SensorGroupConfigAdditionalParameter_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,11),_SensorGroupConfigAdditionalParameter_Type())
sensorGroupConfigAdditionalParameter.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigAdditionalParameter.setStatus(_A)
_SensorGroupConfigLowerBoundary_Type=DisplayString
_SensorGroupConfigLowerBoundary_Object=MibTableColumn
sensorGroupConfigLowerBoundary=_SensorGroupConfigLowerBoundary_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,12),_SensorGroupConfigLowerBoundary_Type())
sensorGroupConfigLowerBoundary.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigLowerBoundary.setStatus(_A)
_SensorGroupConfigUpperBoundary_Type=DisplayString
_SensorGroupConfigUpperBoundary_Object=MibTableColumn
sensorGroupConfigUpperBoundary=_SensorGroupConfigUpperBoundary_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,13),_SensorGroupConfigUpperBoundary_Type())
sensorGroupConfigUpperBoundary.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigUpperBoundary.setStatus(_A)
class _SensorGroupConfigBoundaryHysteresis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('low',1),('high',2)))
_SensorGroupConfigBoundaryHysteresis_Type.__name__=_D
_SensorGroupConfigBoundaryHysteresis_Object=MibTableColumn
sensorGroupConfigBoundaryHysteresis=_SensorGroupConfigBoundaryHysteresis_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,14),_SensorGroupConfigBoundaryHysteresis_Type())
sensorGroupConfigBoundaryHysteresis.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigBoundaryHysteresis.setStatus(_A)
_SensorGroupConfigUpdateDelta_Type=DisplayString
_SensorGroupConfigUpdateDelta_Object=MibTableColumn
sensorGroupConfigUpdateDelta=_SensorGroupConfigUpdateDelta_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,15),_SensorGroupConfigUpdateDelta_Type())
sensorGroupConfigUpdateDelta.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigUpdateDelta.setStatus(_A)
_SensorGroupConfigRateLimit_Type=Unsigned32
_SensorGroupConfigRateLimit_Object=MibTableColumn
sensorGroupConfigRateLimit=_SensorGroupConfigRateLimit_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,16),_SensorGroupConfigRateLimit_Type())
sensorGroupConfigRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigRateLimit.setStatus(_A)
_SensorGroupConfigClearValues_Type=DisplayString
_SensorGroupConfigClearValues_Object=MibTableColumn
sensorGroupConfigClearValues=_SensorGroupConfigClearValues_Object((1,3,6,1,4,1,3181,10,6,4,99,5,1,17),_SensorGroupConfigClearValues_Type())
sensorGroupConfigClearValues.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorGroupConfigClearValues.setStatus(_A)
_DeviceInformationTable_Object=MibTable
deviceInformationTable=_DeviceInformationTable_Object((1,3,6,1,4,1,3181,10,6,4,99,100))
if mibBuilder.loadTexts:deviceInformationTable.setStatus(_A)
_DeviceInformationEntry_Object=MibTableRow
deviceInformationEntry=_DeviceInformationEntry_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1))
deviceInformationEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:deviceInformationEntry.setStatus(_A)
class _DeviceInformationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_DeviceInformationIndex_Type.__name__=_D
_DeviceInformationIndex_Object=MibTableColumn
deviceInformationIndex=_DeviceInformationIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,1),_DeviceInformationIndex_Type())
deviceInformationIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:deviceInformationIndex.setStatus(_A)
_DeviceInformationName_Type=DisplayString
_DeviceInformationName_Object=MibTableColumn
deviceInformationName=_DeviceInformationName_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,2),_DeviceInformationName_Type())
deviceInformationName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationName.setStatus(_A)
_DeviceInformationHardwareId_Type=DisplayString
_DeviceInformationHardwareId_Object=MibTableColumn
deviceInformationHardwareId=_DeviceInformationHardwareId_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,3),_DeviceInformationHardwareId_Type())
deviceInformationHardwareId.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationHardwareId.setStatus(_A)
class _DeviceInformationDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unused',0),('sensor',1),('actor',2),('actorSensor',3),('gateway',4),('other',5)))
_DeviceInformationDeviceType_Type.__name__=_D
_DeviceInformationDeviceType_Object=MibTableColumn
deviceInformationDeviceType=_DeviceInformationDeviceType_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,4),_DeviceInformationDeviceType_Type())
deviceInformationDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationDeviceType.setStatus(_A)
class _DeviceInformationOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,0),(_J,1),('normal',2),('testMode',3),('configError',4),('unpaired',5),('notReady',6),('pairing',7),('inConfig',8),('unregistered',9)))
_DeviceInformationOperationalState_Type.__name__=_D
_DeviceInformationOperationalState_Object=MibTableColumn
deviceInformationOperationalState=_DeviceInformationOperationalState_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,5),_DeviceInformationOperationalState_Type())
deviceInformationOperationalState.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationOperationalState.setStatus(_A)
_DeviceInformationActorAttributes_Type=DisplayString
_DeviceInformationActorAttributes_Object=MibTableColumn
deviceInformationActorAttributes=_DeviceInformationActorAttributes_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,6),_DeviceInformationActorAttributes_Type())
deviceInformationActorAttributes.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationActorAttributes.setStatus(_A)
_DeviceInformationSensorAttributes_Type=DisplayString
_DeviceInformationSensorAttributes_Object=MibTableColumn
deviceInformationSensorAttributes=_DeviceInformationSensorAttributes_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,7),_DeviceInformationSensorAttributes_Type())
deviceInformationSensorAttributes.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationSensorAttributes.setStatus(_A)
_DeviceInformationVendorName_Type=DisplayString
_DeviceInformationVendorName_Object=MibTableColumn
deviceInformationVendorName=_DeviceInformationVendorName_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,8),_DeviceInformationVendorName_Type())
deviceInformationVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationVendorName.setStatus(_A)
_DeviceInformationArticleNumber_Type=DisplayString
_DeviceInformationArticleNumber_Object=MibTableColumn
deviceInformationArticleNumber=_DeviceInformationArticleNumber_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,9),_DeviceInformationArticleNumber_Type())
deviceInformationArticleNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationArticleNumber.setStatus(_A)
_DeviceInformationSerialNumber_Type=DisplayString
_DeviceInformationSerialNumber_Object=MibTableColumn
deviceInformationSerialNumber=_DeviceInformationSerialNumber_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,10),_DeviceInformationSerialNumber_Type())
deviceInformationSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationSerialNumber.setStatus(_A)
_DeviceInformationHardwareRevision_Type=DisplayString
_DeviceInformationHardwareRevision_Object=MibTableColumn
deviceInformationHardwareRevision=_DeviceInformationHardwareRevision_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,11),_DeviceInformationHardwareRevision_Type())
deviceInformationHardwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationHardwareRevision.setStatus(_A)
_DeviceInformationSoftwareVersion_Type=DisplayString
_DeviceInformationSoftwareVersion_Object=MibTableColumn
deviceInformationSoftwareVersion=_DeviceInformationSoftwareVersion_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,12),_DeviceInformationSoftwareVersion_Type())
deviceInformationSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationSoftwareVersion.setStatus(_A)
_DeviceInformationAdditionalInfo_Type=DisplayString
_DeviceInformationAdditionalInfo_Object=MibTableColumn
deviceInformationAdditionalInfo=_DeviceInformationAdditionalInfo_Object((1,3,6,1,4,1,3181,10,6,4,99,100,1,13),_DeviceInformationAdditionalInfo_Type())
deviceInformationAdditionalInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceInformationAdditionalInfo.setStatus(_A)
_ActorListTable_Object=MibTable
actorListTable=_ActorListTable_Object((1,3,6,1,4,1,3181,10,6,4,99,101))
if mibBuilder.loadTexts:actorListTable.setStatus(_A)
_ActorListEntry_Object=MibTableRow
actorListEntry=_ActorListEntry_Object((1,3,6,1,4,1,3181,10,6,4,99,101,1))
actorListEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:actorListEntry.setStatus(_A)
class _ActorListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ActorListIndex_Type.__name__=_D
_ActorListIndex_Object=MibTableColumn
actorListIndex=_ActorListIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,101,1,1),_ActorListIndex_Type())
actorListIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:actorListIndex.setStatus(_A)
_ActorListDevice_Type=DisplayString
_ActorListDevice_Object=MibTableColumn
actorListDevice=_ActorListDevice_Object((1,3,6,1,4,1,3181,10,6,4,99,101,1,2),_ActorListDevice_Type())
actorListDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:actorListDevice.setStatus(_A)
_ActorListInstance_Type=DisplayString
_ActorListInstance_Object=MibTableColumn
actorListInstance=_ActorListInstance_Object((1,3,6,1,4,1,3181,10,6,4,99,101,1,3),_ActorListInstance_Type())
actorListInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:actorListInstance.setStatus(_A)
_ActorListAttribute_Type=DisplayString
_ActorListAttribute_Object=MibTableColumn
actorListAttribute=_ActorListAttribute_Object((1,3,6,1,4,1,3181,10,6,4,99,101,1,4),_ActorListAttribute_Type())
actorListAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:actorListAttribute.setStatus(_A)
_ActorListAssociatedGroups_Type=DisplayString
_ActorListAssociatedGroups_Object=MibTableColumn
actorListAssociatedGroups=_ActorListAssociatedGroups_Object((1,3,6,1,4,1,3181,10,6,4,99,101,1,5),_ActorListAssociatedGroups_Type())
actorListAssociatedGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:actorListAssociatedGroups.setStatus(_A)
_ActorListValue_Type=DisplayString
_ActorListValue_Object=MibTableColumn
actorListValue=_ActorListValue_Object((1,3,6,1,4,1,3181,10,6,4,99,101,1,6),_ActorListValue_Type())
actorListValue.setMaxAccess(_B)
if mibBuilder.loadTexts:actorListValue.setStatus(_A)
class _ActorListActorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,0),(_K,1),('requested',2),('retrying',3),('confirmed',4),('denied',5),(_J,6),('restored',7),(_L,8)))
_ActorListActorState_Type.__name__=_D
_ActorListActorState_Object=MibTableColumn
actorListActorState=_ActorListActorState_Object((1,3,6,1,4,1,3181,10,6,4,99,101,1,7),_ActorListActorState_Type())
actorListActorState.setMaxAccess(_B)
if mibBuilder.loadTexts:actorListActorState.setStatus(_A)
_ActorListLastUpdate_Type=Counter32
_ActorListLastUpdate_Object=MibTableColumn
actorListLastUpdate=_ActorListLastUpdate_Object((1,3,6,1,4,1,3181,10,6,4,99,101,1,8),_ActorListLastUpdate_Type())
actorListLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:actorListLastUpdate.setStatus(_A)
_SensorListTable_Object=MibTable
sensorListTable=_SensorListTable_Object((1,3,6,1,4,1,3181,10,6,4,99,102))
if mibBuilder.loadTexts:sensorListTable.setStatus(_A)
_SensorListEntry_Object=MibTableRow
sensorListEntry=_SensorListEntry_Object((1,3,6,1,4,1,3181,10,6,4,99,102,1))
sensorListEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:sensorListEntry.setStatus(_A)
class _SensorListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SensorListIndex_Type.__name__=_D
_SensorListIndex_Object=MibTableColumn
sensorListIndex=_SensorListIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,102,1,1),_SensorListIndex_Type())
sensorListIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sensorListIndex.setStatus(_A)
_SensorListDevice_Type=DisplayString
_SensorListDevice_Object=MibTableColumn
sensorListDevice=_SensorListDevice_Object((1,3,6,1,4,1,3181,10,6,4,99,102,1,2),_SensorListDevice_Type())
sensorListDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorListDevice.setStatus(_A)
_SensorListInstance_Type=DisplayString
_SensorListInstance_Object=MibTableColumn
sensorListInstance=_SensorListInstance_Object((1,3,6,1,4,1,3181,10,6,4,99,102,1,3),_SensorListInstance_Type())
sensorListInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorListInstance.setStatus(_A)
_SensorListAttribute_Type=DisplayString
_SensorListAttribute_Object=MibTableColumn
sensorListAttribute=_SensorListAttribute_Object((1,3,6,1,4,1,3181,10,6,4,99,102,1,4),_SensorListAttribute_Type())
sensorListAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorListAttribute.setStatus(_A)
_SensorListAssociatedGroups_Type=DisplayString
_SensorListAssociatedGroups_Object=MibTableColumn
sensorListAssociatedGroups=_SensorListAssociatedGroups_Object((1,3,6,1,4,1,3181,10,6,4,99,102,1,5),_SensorListAssociatedGroups_Type())
sensorListAssociatedGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorListAssociatedGroups.setStatus(_A)
_SensorListValue_Type=DisplayString
_SensorListValue_Object=MibTableColumn
sensorListValue=_SensorListValue_Object((1,3,6,1,4,1,3181,10,6,4,99,102,1,6),_SensorListValue_Type())
sensorListValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorListValue.setStatus(_A)
class _SensorListSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,8)));namedValues=NamedValues(*((_H,0),(_K,1),('lowBatt',2),('lowerLimit',3),('upperLimit',4),('commFailed',5),('deviceFailed',6),(_L,8)))
_SensorListSensorState_Type.__name__=_D
_SensorListSensorState_Object=MibTableColumn
sensorListSensorState=_SensorListSensorState_Object((1,3,6,1,4,1,3181,10,6,4,99,102,1,7),_SensorListSensorState_Type())
sensorListSensorState.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorListSensorState.setStatus(_A)
_SensorListLastUpdate_Type=Counter32
_SensorListLastUpdate_Object=MibTableColumn
sensorListLastUpdate=_SensorListLastUpdate_Object((1,3,6,1,4,1,3181,10,6,4,99,102,1,8),_SensorListLastUpdate_Type())
sensorListLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorListLastUpdate.setStatus(_A)
_ActorGroupStatusTable_Object=MibTable
actorGroupStatusTable=_ActorGroupStatusTable_Object((1,3,6,1,4,1,3181,10,6,4,99,103))
if mibBuilder.loadTexts:actorGroupStatusTable.setStatus(_A)
_ActorGroupStatusEntry_Object=MibTableRow
actorGroupStatusEntry=_ActorGroupStatusEntry_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1))
actorGroupStatusEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:actorGroupStatusEntry.setStatus(_A)
class _ActorGroupStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ActorGroupStatusIndex_Type.__name__=_D
_ActorGroupStatusIndex_Object=MibTableColumn
actorGroupStatusIndex=_ActorGroupStatusIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,1),_ActorGroupStatusIndex_Type())
actorGroupStatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:actorGroupStatusIndex.setStatus(_A)
_ActorGroupStatusGroupName_Type=DisplayString
_ActorGroupStatusGroupName_Object=MibTableColumn
actorGroupStatusGroupName=_ActorGroupStatusGroupName_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,2),_ActorGroupStatusGroupName_Type())
actorGroupStatusGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusGroupName.setStatus(_A)
_ActorGroupStatusAttribute_Type=DisplayString
_ActorGroupStatusAttribute_Object=MibTableColumn
actorGroupStatusAttribute=_ActorGroupStatusAttribute_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,3),_ActorGroupStatusAttribute_Type())
actorGroupStatusAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusAttribute.setStatus(_A)
class _ActorGroupStatusNumAssignedActors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ActorGroupStatusNumAssignedActors_Type.__name__=_D
_ActorGroupStatusNumAssignedActors_Object=MibTableColumn
actorGroupStatusNumAssignedActors=_ActorGroupStatusNumAssignedActors_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,4),_ActorGroupStatusNumAssignedActors_Type())
actorGroupStatusNumAssignedActors.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusNumAssignedActors.setStatus(_A)
class _ActorGroupStatusNumFailedActors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ActorGroupStatusNumFailedActors_Type.__name__=_D
_ActorGroupStatusNumFailedActors_Object=MibTableColumn
actorGroupStatusNumFailedActors=_ActorGroupStatusNumFailedActors_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,5),_ActorGroupStatusNumFailedActors_Type())
actorGroupStatusNumFailedActors.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusNumFailedActors.setStatus(_A)
class _ActorGroupStatusGroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,8)));namedValues=NamedValues(*((_H,0),(_K,1),(_V,2),(_W,3),(_L,8)))
_ActorGroupStatusGroupState_Type.__name__=_D
_ActorGroupStatusGroupState_Object=MibTableColumn
actorGroupStatusGroupState=_ActorGroupStatusGroupState_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,6),_ActorGroupStatusGroupState_Type())
actorGroupStatusGroupState.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusGroupState.setStatus(_A)
_ActorGroupStatusValue_Type=DisplayString
_ActorGroupStatusValue_Object=MibTableColumn
actorGroupStatusValue=_ActorGroupStatusValue_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,7),_ActorGroupStatusValue_Type())
actorGroupStatusValue.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusValue.setStatus(_A)
_ActorGroupStatusActivePriority_Type=Unsigned32
_ActorGroupStatusActivePriority_Object=MibTableColumn
actorGroupStatusActivePriority=_ActorGroupStatusActivePriority_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,8),_ActorGroupStatusActivePriority_Type())
actorGroupStatusActivePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusActivePriority.setStatus(_A)
_ActorGroupStatusPriorityValueChain_Type=DisplayString
_ActorGroupStatusPriorityValueChain_Object=MibTableColumn
actorGroupStatusPriorityValueChain=_ActorGroupStatusPriorityValueChain_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,9),_ActorGroupStatusPriorityValueChain_Type())
actorGroupStatusPriorityValueChain.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusPriorityValueChain.setStatus(_A)
class _ActorGroupStatusCacheStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),(_F,1),(_X,2),('saved',3),(_J,4)))
_ActorGroupStatusCacheStatus_Type.__name__=_D
_ActorGroupStatusCacheStatus_Object=MibTableColumn
actorGroupStatusCacheStatus=_ActorGroupStatusCacheStatus_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,10),_ActorGroupStatusCacheStatus_Type())
actorGroupStatusCacheStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusCacheStatus.setStatus(_A)
_ActorGroupStatusLastUpdate_Type=Counter32
_ActorGroupStatusLastUpdate_Object=MibTableColumn
actorGroupStatusLastUpdate=_ActorGroupStatusLastUpdate_Object((1,3,6,1,4,1,3181,10,6,4,99,103,1,11),_ActorGroupStatusLastUpdate_Type())
actorGroupStatusLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:actorGroupStatusLastUpdate.setStatus(_A)
_SensorGroupStatusTable_Object=MibTable
sensorGroupStatusTable=_SensorGroupStatusTable_Object((1,3,6,1,4,1,3181,10,6,4,99,104))
if mibBuilder.loadTexts:sensorGroupStatusTable.setStatus(_A)
_SensorGroupStatusEntry_Object=MibTableRow
sensorGroupStatusEntry=_SensorGroupStatusEntry_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1))
sensorGroupStatusEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:sensorGroupStatusEntry.setStatus(_A)
class _SensorGroupStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SensorGroupStatusIndex_Type.__name__=_D
_SensorGroupStatusIndex_Object=MibTableColumn
sensorGroupStatusIndex=_SensorGroupStatusIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,1),_SensorGroupStatusIndex_Type())
sensorGroupStatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sensorGroupStatusIndex.setStatus(_A)
_SensorGroupStatusGroupName_Type=DisplayString
_SensorGroupStatusGroupName_Object=MibTableColumn
sensorGroupStatusGroupName=_SensorGroupStatusGroupName_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,2),_SensorGroupStatusGroupName_Type())
sensorGroupStatusGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusGroupName.setStatus(_A)
_SensorGroupStatusAttribute_Type=DisplayString
_SensorGroupStatusAttribute_Object=MibTableColumn
sensorGroupStatusAttribute=_SensorGroupStatusAttribute_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,3),_SensorGroupStatusAttribute_Type())
sensorGroupStatusAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusAttribute.setStatus(_A)
class _SensorGroupStatusNumAssignedSensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SensorGroupStatusNumAssignedSensors_Type.__name__=_D
_SensorGroupStatusNumAssignedSensors_Object=MibTableColumn
sensorGroupStatusNumAssignedSensors=_SensorGroupStatusNumAssignedSensors_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,4),_SensorGroupStatusNumAssignedSensors_Type())
sensorGroupStatusNumAssignedSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusNumAssignedSensors.setStatus(_A)
class _SensorGroupStatusNumFailedSensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SensorGroupStatusNumFailedSensors_Type.__name__=_D
_SensorGroupStatusNumFailedSensors_Object=MibTableColumn
sensorGroupStatusNumFailedSensors=_SensorGroupStatusNumFailedSensors_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,5),_SensorGroupStatusNumFailedSensors_Type())
sensorGroupStatusNumFailedSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusNumFailedSensors.setStatus(_A)
class _SensorGroupStatusGroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,8)));namedValues=NamedValues(*((_H,0),(_K,1),(_V,2),(_W,3),(_L,8)))
_SensorGroupStatusGroupState_Type.__name__=_D
_SensorGroupStatusGroupState_Object=MibTableColumn
sensorGroupStatusGroupState=_SensorGroupStatusGroupState_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,6),_SensorGroupStatusGroupState_Type())
sensorGroupStatusGroupState.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusGroupState.setStatus(_A)
_SensorGroupStatusMinimumPeakHold_Type=DisplayString
_SensorGroupStatusMinimumPeakHold_Object=MibTableColumn
sensorGroupStatusMinimumPeakHold=_SensorGroupStatusMinimumPeakHold_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,7),_SensorGroupStatusMinimumPeakHold_Type())
sensorGroupStatusMinimumPeakHold.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusMinimumPeakHold.setStatus(_A)
_SensorGroupStatusMinimumValue_Type=DisplayString
_SensorGroupStatusMinimumValue_Object=MibTableColumn
sensorGroupStatusMinimumValue=_SensorGroupStatusMinimumValue_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,8),_SensorGroupStatusMinimumValue_Type())
sensorGroupStatusMinimumValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusMinimumValue.setStatus(_A)
_SensorGroupStatusAverageValue_Type=DisplayString
_SensorGroupStatusAverageValue_Object=MibTableColumn
sensorGroupStatusAverageValue=_SensorGroupStatusAverageValue_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,9),_SensorGroupStatusAverageValue_Type())
sensorGroupStatusAverageValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusAverageValue.setStatus(_A)
_SensorGroupStatusMaximumValue_Type=DisplayString
_SensorGroupStatusMaximumValue_Object=MibTableColumn
sensorGroupStatusMaximumValue=_SensorGroupStatusMaximumValue_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,10),_SensorGroupStatusMaximumValue_Type())
sensorGroupStatusMaximumValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusMaximumValue.setStatus(_A)
_SensorGroupStatusMaximumPeakHold_Type=DisplayString
_SensorGroupStatusMaximumPeakHold_Object=MibTableColumn
sensorGroupStatusMaximumPeakHold=_SensorGroupStatusMaximumPeakHold_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,11),_SensorGroupStatusMaximumPeakHold_Type())
sensorGroupStatusMaximumPeakHold.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusMaximumPeakHold.setStatus(_A)
_SensorGroupStatusTotalValue_Type=DisplayString
_SensorGroupStatusTotalValue_Object=MibTableColumn
sensorGroupStatusTotalValue=_SensorGroupStatusTotalValue_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,12),_SensorGroupStatusTotalValue_Type())
sensorGroupStatusTotalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusTotalValue.setStatus(_A)
class _SensorGroupStatusLowerBoundaryReached_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SensorGroupStatusLowerBoundaryReached_Type.__name__=_D
_SensorGroupStatusLowerBoundaryReached_Object=MibTableColumn
sensorGroupStatusLowerBoundaryReached=_SensorGroupStatusLowerBoundaryReached_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,13),_SensorGroupStatusLowerBoundaryReached_Type())
sensorGroupStatusLowerBoundaryReached.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusLowerBoundaryReached.setStatus(_A)
class _SensorGroupStatusUpperBoundaryReached_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SensorGroupStatusUpperBoundaryReached_Type.__name__=_D
_SensorGroupStatusUpperBoundaryReached_Object=MibTableColumn
sensorGroupStatusUpperBoundaryReached=_SensorGroupStatusUpperBoundaryReached_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,14),_SensorGroupStatusUpperBoundaryReached_Type())
sensorGroupStatusUpperBoundaryReached.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusUpperBoundaryReached.setStatus(_A)
class _SensorGroupStatusUpdatingSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SensorGroupStatusUpdatingSensorIndex_Type.__name__=_D
_SensorGroupStatusUpdatingSensorIndex_Object=MibTableColumn
sensorGroupStatusUpdatingSensorIndex=_SensorGroupStatusUpdatingSensorIndex_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,15),_SensorGroupStatusUpdatingSensorIndex_Type())
sensorGroupStatusUpdatingSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusUpdatingSensorIndex.setStatus(_A)
class _SensorGroupStatusCacheStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),(_F,1),(_X,2),('saved',3),(_J,4)))
_SensorGroupStatusCacheStatus_Type.__name__=_D
_SensorGroupStatusCacheStatus_Object=MibTableColumn
sensorGroupStatusCacheStatus=_SensorGroupStatusCacheStatus_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,16),_SensorGroupStatusCacheStatus_Type())
sensorGroupStatusCacheStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusCacheStatus.setStatus(_A)
_SensorGroupStatusLastUpdate_Type=Counter32
_SensorGroupStatusLastUpdate_Object=MibTableColumn
sensorGroupStatusLastUpdate=_SensorGroupStatusLastUpdate_Object((1,3,6,1,4,1,3181,10,6,4,99,104,1,17),_SensorGroupStatusLastUpdate_Type())
sensorGroupStatusLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorGroupStatusLastUpdate.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'device':device,'smartoffice':smartoffice,'smartofficeEnableSmartOffice':smartofficeEnableSmartOffice,'directorConfigTable':directorConfigTable,'directorConfigEntry':directorConfigEntry,_M:directorConfigIndex,'directorConfigDomainName':directorConfigDomainName,'directorConfigGeneralMode':directorConfigGeneralMode,'directorConfigActOnUngroupedSensors':directorConfigActOnUngroupedSensors,'directorConfigScanLightControllers':directorConfigScanLightControllers,'deviceConfigTable':deviceConfigTable,'deviceConfigEntry':deviceConfigEntry,_O:deviceConfigIndex,'deviceConfigDeviceName':deviceConfigDeviceName,'deviceConfigLocation':deviceConfigLocation,'deviceConfigLatitude':deviceConfigLatitude,'deviceConfigLongitude':deviceConfigLongitude,'deviceConfigAltitude':deviceConfigAltitude,'deviceConfigPlacement':deviceConfigPlacement,'deviceConfigProductType':deviceConfigProductType,'deviceConfigDeviceId':deviceConfigDeviceId,'deviceConfigNetworkAddress':deviceConfigNetworkAddress,'deviceConfigAdditionalParameter':deviceConfigAdditionalParameter,'deviceConfigNetworkFailureAction':deviceConfigNetworkFailureAction,'deviceConfigIdentify':deviceConfigIdentify,'deviceConfigRestart':deviceConfigRestart,'deviceConfigCalibrate':deviceConfigCalibrate,'deviceConfigPair':deviceConfigPair,'deviceConfigUnpair':deviceConfigUnpair,'deviceConfigUpdateFirmware':deviceConfigUpdateFirmware,'actorGroupConfigTable':actorGroupConfigTable,'actorGroupConfigEntry':actorGroupConfigEntry,_P:actorGroupConfigIndex,'actorGroupConfigGroupName':actorGroupConfigGroupName,'actorGroupConfigAttribute':actorGroupConfigAttribute,'actorGroupConfigAssociatedDevices':actorGroupConfigAssociatedDevices,'actorGroupConfigAdditionalParameter':actorGroupConfigAdditionalParameter,'actorGroupConfigDefaultValue':actorGroupConfigDefaultValue,'actorGroupConfigValueCaching':actorGroupConfigValueCaching,'actorGroupConfigAdditionalScriptName':actorGroupConfigAdditionalScriptName,'actorGroupConfigManualSetValue':actorGroupConfigManualSetValue,'sensorGroupConfigTable':sensorGroupConfigTable,'sensorGroupConfigEntry':sensorGroupConfigEntry,_Q:sensorGroupConfigIndex,'sensorGroupConfigGroupName':sensorGroupConfigGroupName,'sensorGroupConfigAttribute':sensorGroupConfigAttribute,'sensorGroupConfigAssociatedDevices':sensorGroupConfigAssociatedDevices,'sensorGroupConfigValueCaching':sensorGroupConfigValueCaching,'sensorGroupConfigRunScriptWhen':sensorGroupConfigRunScriptWhen,'sensorGroupConfigRunScriptDelta':sensorGroupConfigRunScriptDelta,'sensorGroupConfigScriptName':sensorGroupConfigScriptName,'sensorGroupConfigAdditionalScriptName':sensorGroupConfigAdditionalScriptName,'sensorGroupConfigReportMode':sensorGroupConfigReportMode,'sensorGroupConfigAdditionalParameter':sensorGroupConfigAdditionalParameter,'sensorGroupConfigLowerBoundary':sensorGroupConfigLowerBoundary,'sensorGroupConfigUpperBoundary':sensorGroupConfigUpperBoundary,'sensorGroupConfigBoundaryHysteresis':sensorGroupConfigBoundaryHysteresis,'sensorGroupConfigUpdateDelta':sensorGroupConfigUpdateDelta,'sensorGroupConfigRateLimit':sensorGroupConfigRateLimit,'sensorGroupConfigClearValues':sensorGroupConfigClearValues,'deviceInformationTable':deviceInformationTable,'deviceInformationEntry':deviceInformationEntry,_R:deviceInformationIndex,'deviceInformationName':deviceInformationName,'deviceInformationHardwareId':deviceInformationHardwareId,'deviceInformationDeviceType':deviceInformationDeviceType,'deviceInformationOperationalState':deviceInformationOperationalState,'deviceInformationActorAttributes':deviceInformationActorAttributes,'deviceInformationSensorAttributes':deviceInformationSensorAttributes,'deviceInformationVendorName':deviceInformationVendorName,'deviceInformationArticleNumber':deviceInformationArticleNumber,'deviceInformationSerialNumber':deviceInformationSerialNumber,'deviceInformationHardwareRevision':deviceInformationHardwareRevision,'deviceInformationSoftwareVersion':deviceInformationSoftwareVersion,'deviceInformationAdditionalInfo':deviceInformationAdditionalInfo,'actorListTable':actorListTable,'actorListEntry':actorListEntry,_S:actorListIndex,'actorListDevice':actorListDevice,'actorListInstance':actorListInstance,'actorListAttribute':actorListAttribute,'actorListAssociatedGroups':actorListAssociatedGroups,'actorListValue':actorListValue,'actorListActorState':actorListActorState,'actorListLastUpdate':actorListLastUpdate,'sensorListTable':sensorListTable,'sensorListEntry':sensorListEntry,_T:sensorListIndex,'sensorListDevice':sensorListDevice,'sensorListInstance':sensorListInstance,'sensorListAttribute':sensorListAttribute,'sensorListAssociatedGroups':sensorListAssociatedGroups,'sensorListValue':sensorListValue,'sensorListSensorState':sensorListSensorState,'sensorListLastUpdate':sensorListLastUpdate,'actorGroupStatusTable':actorGroupStatusTable,'actorGroupStatusEntry':actorGroupStatusEntry,_U:actorGroupStatusIndex,'actorGroupStatusGroupName':actorGroupStatusGroupName,'actorGroupStatusAttribute':actorGroupStatusAttribute,'actorGroupStatusNumAssignedActors':actorGroupStatusNumAssignedActors,'actorGroupStatusNumFailedActors':actorGroupStatusNumFailedActors,'actorGroupStatusGroupState':actorGroupStatusGroupState,'actorGroupStatusValue':actorGroupStatusValue,'actorGroupStatusActivePriority':actorGroupStatusActivePriority,'actorGroupStatusPriorityValueChain':actorGroupStatusPriorityValueChain,'actorGroupStatusCacheStatus':actorGroupStatusCacheStatus,'actorGroupStatusLastUpdate':actorGroupStatusLastUpdate,'sensorGroupStatusTable':sensorGroupStatusTable,'sensorGroupStatusEntry':sensorGroupStatusEntry,_Y:sensorGroupStatusIndex,'sensorGroupStatusGroupName':sensorGroupStatusGroupName,'sensorGroupStatusAttribute':sensorGroupStatusAttribute,'sensorGroupStatusNumAssignedSensors':sensorGroupStatusNumAssignedSensors,'sensorGroupStatusNumFailedSensors':sensorGroupStatusNumFailedSensors,'sensorGroupStatusGroupState':sensorGroupStatusGroupState,'sensorGroupStatusMinimumPeakHold':sensorGroupStatusMinimumPeakHold,'sensorGroupStatusMinimumValue':sensorGroupStatusMinimumValue,'sensorGroupStatusAverageValue':sensorGroupStatusAverageValue,'sensorGroupStatusMaximumValue':sensorGroupStatusMaximumValue,'sensorGroupStatusMaximumPeakHold':sensorGroupStatusMaximumPeakHold,'sensorGroupStatusTotalValue':sensorGroupStatusTotalValue,'sensorGroupStatusLowerBoundaryReached':sensorGroupStatusLowerBoundaryReached,'sensorGroupStatusUpperBoundaryReached':sensorGroupStatusUpperBoundaryReached,'sensorGroupStatusUpdatingSensorIndex':sensorGroupStatusUpdatingSensorIndex,'sensorGroupStatusCacheStatus':sensorGroupStatusCacheStatus,'sensorGroupStatusLastUpdate':sensorGroupStatusLastUpdate})