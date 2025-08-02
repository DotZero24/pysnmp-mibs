_M='saveInfoIndex'
_L='firmwareIndex'
_K='scriptScheduleIndex'
_J='temporarily'
_I='permanently'
_H='not-accessible'
_G='enabled'
_F='G6-SYSTEM-MIB'
_E='disabled'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
device=ModuleIdentity((1,3,6,1,4,1,3181,10,6,1))
if mibBuilder.loadTexts:device.setRevisions(('2018-02-12 16:19',))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,3181,10,6,1,30))
_SystemShowTimeDate_Type=DisplayString
_SystemShowTimeDate_Object=MibScalar
systemShowTimeDate=_SystemShowTimeDate_Object((1,3,6,1,4,1,3181,10,6,1,30,1),_SystemShowTimeDate_Type())
systemShowTimeDate.setMaxAccess(_B)
if mibBuilder.loadTexts:systemShowTimeDate.setStatus(_A)
_SystemSetTime_Type=DisplayString
_SystemSetTime_Object=MibScalar
systemSetTime=_SystemSetTime_Object((1,3,6,1,4,1,3181,10,6,1,30,2),_SystemSetTime_Type())
systemSetTime.setMaxAccess(_B)
if mibBuilder.loadTexts:systemSetTime.setStatus(_A)
_SystemSetDate_Type=DisplayString
_SystemSetDate_Object=MibScalar
systemSetDate=_SystemSetDate_Object((1,3,6,1,4,1,3181,10,6,1,30,3),_SystemSetDate_Type())
systemSetDate.setMaxAccess(_B)
if mibBuilder.loadTexts:systemSetDate.setStatus(_A)
_SystemShowUtilization_Type=DisplayString
_SystemShowUtilization_Object=MibScalar
systemShowUtilization=_SystemShowUtilization_Object((1,3,6,1,4,1,3181,10,6,1,30,4),_SystemShowUtilization_Type())
systemShowUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:systemShowUtilization.setStatus(_A)
_SystemRebootDevice_Type=DisplayString
_SystemRebootDevice_Object=MibScalar
systemRebootDevice=_SystemRebootDevice_Object((1,3,6,1,4,1,3181,10,6,1,30,5),_SystemRebootDevice_Type())
systemRebootDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:systemRebootDevice.setStatus(_A)
_SystemCreateSnapshot_Type=DisplayString
_SystemCreateSnapshot_Object=MibScalar
systemCreateSnapshot=_SystemCreateSnapshot_Object((1,3,6,1,4,1,3181,10,6,1,30,6),_SystemCreateSnapshot_Type())
systemCreateSnapshot.setMaxAccess(_B)
if mibBuilder.loadTexts:systemCreateSnapshot.setStatus(_A)
_SystemSendWakeOnLanPacket_Type=DisplayString
_SystemSendWakeOnLanPacket_Object=MibScalar
systemSendWakeOnLanPacket=_SystemSendWakeOnLanPacket_Object((1,3,6,1,4,1,3181,10,6,1,30,7),_SystemSendWakeOnLanPacket_Type())
systemSendWakeOnLanPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:systemSendWakeOnLanPacket.setStatus(_A)
_SystemAlternativeMacAddress_Type=MacAddress
_SystemAlternativeMacAddress_Object=MibScalar
systemAlternativeMacAddress=_SystemAlternativeMacAddress_Object((1,3,6,1,4,1,3181,10,6,1,30,8),_SystemAlternativeMacAddress_Type())
systemAlternativeMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:systemAlternativeMacAddress.setStatus(_A)
class _SystemBootPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('sdCardFirst',0),('internalFirst',1),('sdCardOnly',2),('internalOnly',3)))
_SystemBootPreference_Type.__name__=_C
_SystemBootPreference_Object=MibScalar
systemBootPreference=_SystemBootPreference_Object((1,3,6,1,4,1,3181,10,6,1,30,9),_SystemBootPreference_Type())
systemBootPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:systemBootPreference.setStatus(_A)
_SystemInventory_Type=DisplayString
_SystemInventory_Object=MibScalar
systemInventory=_SystemInventory_Object((1,3,6,1,4,1,3181,10,6,1,30,10),_SystemInventory_Type())
systemInventory.setMaxAccess(_B)
if mibBuilder.loadTexts:systemInventory.setStatus(_A)
_SystemAutorunCliScript_Type=DisplayString
_SystemAutorunCliScript_Object=MibScalar
systemAutorunCliScript=_SystemAutorunCliScript_Object((1,3,6,1,4,1,3181,10,6,1,30,11),_SystemAutorunCliScript_Type())
systemAutorunCliScript.setMaxAccess(_B)
if mibBuilder.loadTexts:systemAutorunCliScript.setStatus(_A)
class _SystemSerialPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_E,0),('console',1),('appControlled',2),('terminalServer',3),('smartSensor',4)))
_SystemSerialPort_Type.__name__=_C
_SystemSerialPort_Object=MibScalar
systemSerialPort=_SystemSerialPort_Object((1,3,6,1,4,1,3181,10,6,1,30,12),_SystemSerialPort_Type())
systemSerialPort.setMaxAccess(_B)
if mibBuilder.loadTexts:systemSerialPort.setStatus(_A)
class _SystemPermitDebugAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_SystemPermitDebugAccess_Type.__name__=_C
_SystemPermitDebugAccess_Object=MibScalar
systemPermitDebugAccess=_SystemPermitDebugAccess_Object((1,3,6,1,4,1,3181,10,6,1,30,13),_SystemPermitDebugAccess_Type())
systemPermitDebugAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:systemPermitDebugAccess.setStatus(_A)
class _SystemPermitIncomingAlerts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_SystemPermitIncomingAlerts_Type.__name__=_C
_SystemPermitIncomingAlerts_Object=MibScalar
systemPermitIncomingAlerts=_SystemPermitIncomingAlerts_Object((1,3,6,1,4,1,3181,10,6,1,30,14),_SystemPermitIncomingAlerts_Type())
systemPermitIncomingAlerts.setMaxAccess(_B)
if mibBuilder.loadTexts:systemPermitIncomingAlerts.setStatus(_A)
class _SystemCharacterSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*(('iso88591',1),('iso88595',5)))
_SystemCharacterSet_Type.__name__=_C
_SystemCharacterSet_Object=MibScalar
systemCharacterSet=_SystemCharacterSet_Object((1,3,6,1,4,1,3181,10,6,1,30,15),_SystemCharacterSet_Type())
systemCharacterSet.setMaxAccess(_B)
if mibBuilder.loadTexts:systemCharacterSet.setStatus(_A)
class _SystemConfigurationSaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SystemConfigurationSaveMode_Type.__name__=_C
_SystemConfigurationSaveMode_Object=MibScalar
systemConfigurationSaveMode=_SystemConfigurationSaveMode_Object((1,3,6,1,4,1,3181,10,6,1,30,16),_SystemConfigurationSaveMode_Type())
systemConfigurationSaveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:systemConfigurationSaveMode.setStatus(_A)
_ScriptScheduleTable_Object=MibTable
scriptScheduleTable=_ScriptScheduleTable_Object((1,3,6,1,4,1,3181,10,6,1,30,17))
if mibBuilder.loadTexts:scriptScheduleTable.setStatus(_A)
_ScriptScheduleEntry_Object=MibTableRow
scriptScheduleEntry=_ScriptScheduleEntry_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1))
scriptScheduleEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:scriptScheduleEntry.setStatus(_A)
class _ScriptScheduleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ScriptScheduleIndex_Type.__name__=_C
_ScriptScheduleIndex_Object=MibTableColumn
scriptScheduleIndex=_ScriptScheduleIndex_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1,1),_ScriptScheduleIndex_Type())
scriptScheduleIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:scriptScheduleIndex.setStatus(_A)
_ScriptScheduleName_Type=DisplayString
_ScriptScheduleName_Object=MibTableColumn
scriptScheduleName=_ScriptScheduleName_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1,2),_ScriptScheduleName_Type())
scriptScheduleName.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptScheduleName.setStatus(_A)
class _ScriptScheduleMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_ScriptScheduleMode_Type.__name__=_C
_ScriptScheduleMode_Object=MibTableColumn
scriptScheduleMode=_ScriptScheduleMode_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1,3),_ScriptScheduleMode_Type())
scriptScheduleMode.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptScheduleMode.setStatus(_A)
_ScriptScheduleCliScript_Type=DisplayString
_ScriptScheduleCliScript_Object=MibTableColumn
scriptScheduleCliScript=_ScriptScheduleCliScript_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1,4),_ScriptScheduleCliScript_Type())
scriptScheduleCliScript.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptScheduleCliScript.setStatus(_A)
_ScriptScheduleMinutes_Type=DisplayString
_ScriptScheduleMinutes_Object=MibTableColumn
scriptScheduleMinutes=_ScriptScheduleMinutes_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1,5),_ScriptScheduleMinutes_Type())
scriptScheduleMinutes.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptScheduleMinutes.setStatus(_A)
_ScriptScheduleHours_Type=DisplayString
_ScriptScheduleHours_Object=MibTableColumn
scriptScheduleHours=_ScriptScheduleHours_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1,6),_ScriptScheduleHours_Type())
scriptScheduleHours.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptScheduleHours.setStatus(_A)
_ScriptScheduleDays_Type=DisplayString
_ScriptScheduleDays_Object=MibTableColumn
scriptScheduleDays=_ScriptScheduleDays_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1,7),_ScriptScheduleDays_Type())
scriptScheduleDays.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptScheduleDays.setStatus(_A)
_ScriptScheduleMonths_Type=DisplayString
_ScriptScheduleMonths_Object=MibTableColumn
scriptScheduleMonths=_ScriptScheduleMonths_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1,8),_ScriptScheduleMonths_Type())
scriptScheduleMonths.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptScheduleMonths.setStatus(_A)
_ScriptScheduleWeekdays_Type=DisplayString
_ScriptScheduleWeekdays_Object=MibTableColumn
scriptScheduleWeekdays=_ScriptScheduleWeekdays_Object((1,3,6,1,4,1,3181,10,6,1,30,17,1,9),_ScriptScheduleWeekdays_Type())
scriptScheduleWeekdays.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptScheduleWeekdays.setStatus(_A)
_SystemLastBootTime_Type=DisplayString
_SystemLastBootTime_Object=MibScalar
systemLastBootTime=_SystemLastBootTime_Object((1,3,6,1,4,1,3181,10,6,1,30,100),_SystemLastBootTime_Type())
systemLastBootTime.setMaxAccess(_D)
if mibBuilder.loadTexts:systemLastBootTime.setStatus(_A)
_SystemUptime_Type=Counter32
_SystemUptime_Object=MibScalar
systemUptime=_SystemUptime_Object((1,3,6,1,4,1,3181,10,6,1,30,101),_SystemUptime_Type())
systemUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:systemUptime.setStatus(_A)
_SystemUsedMacAddress_Type=MacAddress
_SystemUsedMacAddress_Object=MibScalar
systemUsedMacAddress=_SystemUsedMacAddress_Object((1,3,6,1,4,1,3181,10,6,1,30,102),_SystemUsedMacAddress_Type())
systemUsedMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:systemUsedMacAddress.setStatus(_A)
class _SystemUsedBootMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('sdCard',0),('internalMemory',1),('nfs',2)))
_SystemUsedBootMedia_Type.__name__=_C
_SystemUsedBootMedia_Object=MibScalar
systemUsedBootMedia=_SystemUsedBootMedia_Object((1,3,6,1,4,1,3181,10,6,1,30,103),_SystemUsedBootMedia_Type())
systemUsedBootMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:systemUsedBootMedia.setStatus(_A)
class _SystemTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SystemTemperature_Type.__name__=_C
_SystemTemperature_Object=MibScalar
systemTemperature=_SystemTemperature_Object((1,3,6,1,4,1,3181,10,6,1,30,104),_SystemTemperature_Type())
systemTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:systemTemperature.setStatus(_A)
class _SystemClimateLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',0),('criticalLow',1),('low',2),('normal',3),('increased',4),('high',5),('criticalHigh',6),('shutdown',7)))
_SystemClimateLevel_Type.__name__=_C
_SystemClimateLevel_Object=MibScalar
systemClimateLevel=_SystemClimateLevel_Object((1,3,6,1,4,1,3181,10,6,1,30,105),_SystemClimateLevel_Type())
systemClimateLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:systemClimateLevel.setStatus(_A)
_FirmwareTable_Object=MibTable
firmwareTable=_FirmwareTable_Object((1,3,6,1,4,1,3181,10,6,1,30,106))
if mibBuilder.loadTexts:firmwareTable.setStatus(_A)
_FirmwareEntry_Object=MibTableRow
firmwareEntry=_FirmwareEntry_Object((1,3,6,1,4,1,3181,10,6,1,30,106,1))
firmwareEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:firmwareEntry.setStatus(_A)
class _FirmwareIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_FirmwareIndex_Type.__name__=_C
_FirmwareIndex_Object=MibTableColumn
firmwareIndex=_FirmwareIndex_Object((1,3,6,1,4,1,3181,10,6,1,30,106,1,1),_FirmwareIndex_Type())
firmwareIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:firmwareIndex.setStatus(_A)
_FirmwareRunningVersion_Type=DisplayString
_FirmwareRunningVersion_Object=MibTableColumn
firmwareRunningVersion=_FirmwareRunningVersion_Object((1,3,6,1,4,1,3181,10,6,1,30,106,1,2),_FirmwareRunningVersion_Type())
firmwareRunningVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareRunningVersion.setStatus(_A)
_FirmwareBuildDate_Type=DisplayString
_FirmwareBuildDate_Object=MibTableColumn
firmwareBuildDate=_FirmwareBuildDate_Object((1,3,6,1,4,1,3181,10,6,1,30,106,1,3),_FirmwareBuildDate_Type())
firmwareBuildDate.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareBuildDate.setStatus(_A)
_FirmwareBuildNumber_Type=Unsigned32
_FirmwareBuildNumber_Object=MibTableColumn
firmwareBuildNumber=_FirmwareBuildNumber_Object((1,3,6,1,4,1,3181,10,6,1,30,106,1,4),_FirmwareBuildNumber_Type())
firmwareBuildNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareBuildNumber.setStatus(_A)
_SaveInfoTable_Object=MibTable
saveInfoTable=_SaveInfoTable_Object((1,3,6,1,4,1,3181,10,6,1,30,107))
if mibBuilder.loadTexts:saveInfoTable.setStatus(_A)
_SaveInfoEntry_Object=MibTableRow
saveInfoEntry=_SaveInfoEntry_Object((1,3,6,1,4,1,3181,10,6,1,30,107,1))
saveInfoEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:saveInfoEntry.setStatus(_A)
class _SaveInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_SaveInfoIndex_Type.__name__=_C
_SaveInfoIndex_Object=MibTableColumn
saveInfoIndex=_SaveInfoIndex_Object((1,3,6,1,4,1,3181,10,6,1,30,107,1,1),_SaveInfoIndex_Type())
saveInfoIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:saveInfoIndex.setStatus(_A)
_SaveInfoLastSavedParameter_Type=DisplayString
_SaveInfoLastSavedParameter_Object=MibTableColumn
saveInfoLastSavedParameter=_SaveInfoLastSavedParameter_Object((1,3,6,1,4,1,3181,10,6,1,30,107,1,2),_SaveInfoLastSavedParameter_Type())
saveInfoLastSavedParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:saveInfoLastSavedParameter.setStatus(_A)
class _SaveInfoSaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SaveInfoSaveMode_Type.__name__=_C
_SaveInfoSaveMode_Object=MibTableColumn
saveInfoSaveMode=_SaveInfoSaveMode_Object((1,3,6,1,4,1,3181,10,6,1,30,107,1,3),_SaveInfoSaveMode_Type())
saveInfoSaveMode.setMaxAccess(_D)
if mibBuilder.loadTexts:saveInfoSaveMode.setStatus(_A)
class _SaveInfoWriteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('nothingToSave',0),('processing',1),('savedToRam',2),('savedToSdcard',3)))
_SaveInfoWriteStatus_Type.__name__=_C
_SaveInfoWriteStatus_Object=MibTableColumn
saveInfoWriteStatus=_SaveInfoWriteStatus_Object((1,3,6,1,4,1,3181,10,6,1,30,107,1,4),_SaveInfoWriteStatus_Type())
saveInfoWriteStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:saveInfoWriteStatus.setStatus(_A)
_SaveInfoTimeStamp_Type=Counter32
_SaveInfoTimeStamp_Object=MibTableColumn
saveInfoTimeStamp=_SaveInfoTimeStamp_Object((1,3,6,1,4,1,3181,10,6,1,30,107,1,5),_SaveInfoTimeStamp_Type())
saveInfoTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:saveInfoTimeStamp.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'device':device,'system':system,'systemShowTimeDate':systemShowTimeDate,'systemSetTime':systemSetTime,'systemSetDate':systemSetDate,'systemShowUtilization':systemShowUtilization,'systemRebootDevice':systemRebootDevice,'systemCreateSnapshot':systemCreateSnapshot,'systemSendWakeOnLanPacket':systemSendWakeOnLanPacket,'systemAlternativeMacAddress':systemAlternativeMacAddress,'systemBootPreference':systemBootPreference,'systemInventory':systemInventory,'systemAutorunCliScript':systemAutorunCliScript,'systemSerialPort':systemSerialPort,'systemPermitDebugAccess':systemPermitDebugAccess,'systemPermitIncomingAlerts':systemPermitIncomingAlerts,'systemCharacterSet':systemCharacterSet,'systemConfigurationSaveMode':systemConfigurationSaveMode,'scriptScheduleTable':scriptScheduleTable,'scriptScheduleEntry':scriptScheduleEntry,_K:scriptScheduleIndex,'scriptScheduleName':scriptScheduleName,'scriptScheduleMode':scriptScheduleMode,'scriptScheduleCliScript':scriptScheduleCliScript,'scriptScheduleMinutes':scriptScheduleMinutes,'scriptScheduleHours':scriptScheduleHours,'scriptScheduleDays':scriptScheduleDays,'scriptScheduleMonths':scriptScheduleMonths,'scriptScheduleWeekdays':scriptScheduleWeekdays,'systemLastBootTime':systemLastBootTime,'systemUptime':systemUptime,'systemUsedMacAddress':systemUsedMacAddress,'systemUsedBootMedia':systemUsedBootMedia,'systemTemperature':systemTemperature,'systemClimateLevel':systemClimateLevel,'firmwareTable':firmwareTable,'firmwareEntry':firmwareEntry,_L:firmwareIndex,'firmwareRunningVersion':firmwareRunningVersion,'firmwareBuildDate':firmwareBuildDate,'firmwareBuildNumber':firmwareBuildNumber,'saveInfoTable':saveInfoTable,'saveInfoEntry':saveInfoEntry,_M:saveInfoIndex,'saveInfoLastSavedParameter':saveInfoLastSavedParameter,'saveInfoSaveMode':saveInfoSaveMode,'saveInfoWriteStatus':saveInfoWriteStatus,'saveInfoTimeStamp':saveInfoTimeStamp})