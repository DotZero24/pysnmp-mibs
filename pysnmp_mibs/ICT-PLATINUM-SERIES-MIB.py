_D='NotificationType'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_IctPower_ObjectIdentity=ObjectIdentity
ictPower=_IctPower_ObjectIdentity((1,3,6,1,4,1,39145))
_PlatinumSeries_ObjectIdentity=ObjectIdentity
platinumSeries=_PlatinumSeries_ObjectIdentity((1,3,6,1,4,1,39145,11))
_DeviceModel_Type=DisplayString
_DeviceModel_Object=MibScalar
deviceModel=_DeviceModel_Object((1,3,6,1,4,1,39145,11,1),_DeviceModel_Type())
deviceModel.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceModel.setStatus(_A)
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,39145,11,2),_DeviceName_Type())
deviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
class _DeviceHardware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_DeviceHardware_Type.__name__=_C
_DeviceHardware_Object=MibScalar
deviceHardware=_DeviceHardware_Object((1,3,6,1,4,1,39145,11,3),_DeviceHardware_Type())
deviceHardware.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceHardware.setStatus(_A)
_DeviceFirmware_Type=DisplayString
_DeviceFirmware_Object=MibScalar
deviceFirmware=_DeviceFirmware_Object((1,3,6,1,4,1,39145,11,4),_DeviceFirmware_Type())
deviceFirmware.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceFirmware.setStatus(_A)
_DeviceMacAddress_Type=DisplayString
_DeviceMacAddress_Object=MibScalar
deviceMacAddress=_DeviceMacAddress_Object((1,3,6,1,4,1,39145,11,5),_DeviceMacAddress_Type())
deviceMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMacAddress.setStatus(_A)
_InputVoltage_Type=DisplayString
_InputVoltage_Object=MibScalar
inputVoltage=_InputVoltage_Object((1,3,6,1,4,1,39145,11,6),_InputVoltage_Type())
inputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:inputVoltage.setStatus(_A)
_OutputVoltage_Type=DisplayString
_OutputVoltage_Object=MibScalar
outputVoltage=_OutputVoltage_Object((1,3,6,1,4,1,39145,11,7),_OutputVoltage_Type())
outputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:outputVoltage.setStatus(_A)
_OutputCurrent_Type=DisplayString
_OutputCurrent_Object=MibScalar
outputCurrent=_OutputCurrent_Object((1,3,6,1,4,1,39145,11,8),_OutputCurrent_Type())
outputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:outputCurrent.setStatus(_A)
class _OutputEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_OutputEnable_Type.__name__=_C
_OutputEnable_Object=MibScalar
outputEnable=_OutputEnable_Object((1,3,6,1,4,1,39145,11,9),_OutputEnable_Type())
outputEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:outputEnable.setStatus(_A)
_BatteryVoltage_Type=DisplayString
_BatteryVoltage_Object=MibScalar
batteryVoltage=_BatteryVoltage_Object((1,3,6,1,4,1,39145,11,10),_BatteryVoltage_Type())
batteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryVoltage.setStatus(_A)
_BatteryCurrent_Type=DisplayString
_BatteryCurrent_Object=MibScalar
batteryCurrent=_BatteryCurrent_Object((1,3,6,1,4,1,39145,11,11),_BatteryCurrent_Type())
batteryCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryCurrent.setStatus(_A)
_BatteryTemperature_Type=Integer32
_BatteryTemperature_Object=MibScalar
batteryTemperature=_BatteryTemperature_Object((1,3,6,1,4,1,39145,11,12),_BatteryTemperature_Type())
batteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryTemperature.setStatus(_A)
class _BatterySoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BatterySoc_Type.__name__=_C
_BatterySoc_Object=MibScalar
batterySoc=_BatterySoc_Object((1,3,6,1,4,1,39145,11,13),_BatterySoc_Type())
batterySoc.setMaxAccess(_B)
if mibBuilder.loadTexts:batterySoc.setStatus(_A)
_BatteryNetAh_Type=Integer32
_BatteryNetAh_Object=MibScalar
batteryNetAh=_BatteryNetAh_Object((1,3,6,1,4,1,39145,11,14),_BatteryNetAh_Type())
batteryNetAh.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryNetAh.setStatus(_A)
_BatteryRunTime_Type=Integer32
_BatteryRunTime_Object=MibScalar
batteryRunTime=_BatteryRunTime_Object((1,3,6,1,4,1,39145,11,15),_BatteryRunTime_Type())
batteryRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryRunTime.setStatus(_A)
_InputVoltageX1_Type=Integer32
_InputVoltageX1_Object=MibScalar
inputVoltageX1=_InputVoltageX1_Object((1,3,6,1,4,1,39145,11,16),_InputVoltageX1_Type())
inputVoltageX1.setMaxAccess(_B)
if mibBuilder.loadTexts:inputVoltageX1.setStatus(_A)
_OutputVoltageX100_Type=Integer32
_OutputVoltageX100_Object=MibScalar
outputVoltageX100=_OutputVoltageX100_Object((1,3,6,1,4,1,39145,11,17),_OutputVoltageX100_Type())
outputVoltageX100.setMaxAccess(_B)
if mibBuilder.loadTexts:outputVoltageX100.setStatus(_A)
_OutputCurrentX100_Type=Integer32
_OutputCurrentX100_Object=MibScalar
outputCurrentX100=_OutputCurrentX100_Object((1,3,6,1,4,1,39145,11,18),_OutputCurrentX100_Type())
outputCurrentX100.setMaxAccess(_B)
if mibBuilder.loadTexts:outputCurrentX100.setStatus(_A)
_BatteryVoltageX100_Type=Integer32
_BatteryVoltageX100_Object=MibScalar
batteryVoltageX100=_BatteryVoltageX100_Object((1,3,6,1,4,1,39145,11,19),_BatteryVoltageX100_Type())
batteryVoltageX100.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryVoltageX100.setStatus(_A)
_BatteryCurrentX100_Type=Integer32
_BatteryCurrentX100_Object=MibScalar
batteryCurrentX100=_BatteryCurrentX100_Object((1,3,6,1,4,1,39145,11,20),_BatteryCurrentX100_Type())
batteryCurrentX100.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryCurrentX100.setStatus(_A)
acFailAlarmTrap=NotificationType((1,3,6,1,4,1,39145,11,0,101))
if mibBuilder.loadTexts:acFailAlarmTrap.setStatus('')
dcFailAlarmTrap=NotificationType((1,3,6,1,4,1,39145,11,0,102))
if mibBuilder.loadTexts:dcFailAlarmTrap.setStatus('')
sysFailAlarmTrap=NotificationType((1,3,6,1,4,1,39145,11,0,103))
if mibBuilder.loadTexts:sysFailAlarmTrap.setStatus('')
overtemperatureAlarmTrap=NotificationType((1,3,6,1,4,1,39145,11,0,104))
if mibBuilder.loadTexts:overtemperatureAlarmTrap.setStatus('')
commFailAlarmTrap=NotificationType((1,3,6,1,4,1,39145,11,0,105))
if mibBuilder.loadTexts:commFailAlarmTrap.setStatus('')
fanFailAlarmTrap=NotificationType((1,3,6,1,4,1,39145,11,0,106))
if mibBuilder.loadTexts:fanFailAlarmTrap.setStatus('')
batteryAlarmTrap=NotificationType((1,3,6,1,4,1,39145,11,0,107))
if mibBuilder.loadTexts:batteryAlarmTrap.setStatus('')
batteryCurrentAlarmTrap=NotificationType((1,3,6,1,4,1,39145,11,0,108))
if mibBuilder.loadTexts:batteryCurrentAlarmTrap.setStatus('')
acFailAlarmClear=NotificationType((1,3,6,1,4,1,39145,11,0,111))
if mibBuilder.loadTexts:acFailAlarmClear.setStatus('')
dcFailAlarmClear=NotificationType((1,3,6,1,4,1,39145,11,0,112))
if mibBuilder.loadTexts:dcFailAlarmClear.setStatus('')
sysFailAlarmClear=NotificationType((1,3,6,1,4,1,39145,11,0,113))
if mibBuilder.loadTexts:sysFailAlarmClear.setStatus('')
overtemperatureAlarmClear=NotificationType((1,3,6,1,4,1,39145,11,0,114))
if mibBuilder.loadTexts:overtemperatureAlarmClear.setStatus('')
commFailAlarmClear=NotificationType((1,3,6,1,4,1,39145,11,0,115))
if mibBuilder.loadTexts:commFailAlarmClear.setStatus('')
fanFailAlarmClear=NotificationType((1,3,6,1,4,1,39145,11,0,116))
if mibBuilder.loadTexts:fanFailAlarmClear.setStatus('')
batteryAlarmClear=NotificationType((1,3,6,1,4,1,39145,11,0,117))
if mibBuilder.loadTexts:batteryAlarmClear.setStatus('')
batteryTestStart=NotificationType((1,3,6,1,4,1,39145,11,0,121))
if mibBuilder.loadTexts:batteryTestStart.setStatus('')
batteryTestComplete=NotificationType((1,3,6,1,4,1,39145,11,0,122))
if mibBuilder.loadTexts:batteryTestComplete.setStatus('')
batteryTestFail=NotificationType((1,3,6,1,4,1,39145,11,0,123))
if mibBuilder.loadTexts:batteryTestFail.setStatus('')
batteryEqualizeStart=NotificationType((1,3,6,1,4,1,39145,11,0,124))
if mibBuilder.loadTexts:batteryEqualizeStart.setStatus('')
batteryEqualizeComplete=NotificationType((1,3,6,1,4,1,39145,11,0,125))
if mibBuilder.loadTexts:batteryEqualizeComplete.setStatus('')
mibBuilder.exportSymbols('ICT-PLATINUM-SERIES-MIB',**{'ictPower':ictPower,'platinumSeries':platinumSeries,'acFailAlarmTrap':acFailAlarmTrap,'dcFailAlarmTrap':dcFailAlarmTrap,'sysFailAlarmTrap':sysFailAlarmTrap,'overtemperatureAlarmTrap':overtemperatureAlarmTrap,'commFailAlarmTrap':commFailAlarmTrap,'fanFailAlarmTrap':fanFailAlarmTrap,'batteryAlarmTrap':batteryAlarmTrap,'batteryCurrentAlarmTrap':batteryCurrentAlarmTrap,'acFailAlarmClear':acFailAlarmClear,'dcFailAlarmClear':dcFailAlarmClear,'sysFailAlarmClear':sysFailAlarmClear,'overtemperatureAlarmClear':overtemperatureAlarmClear,'commFailAlarmClear':commFailAlarmClear,'fanFailAlarmClear':fanFailAlarmClear,'batteryAlarmClear':batteryAlarmClear,'batteryTestStart':batteryTestStart,'batteryTestComplete':batteryTestComplete,'batteryTestFail':batteryTestFail,'batteryEqualizeStart':batteryEqualizeStart,'batteryEqualizeComplete':batteryEqualizeComplete,'deviceModel':deviceModel,'deviceName':deviceName,'deviceHardware':deviceHardware,'deviceFirmware':deviceFirmware,'deviceMacAddress':deviceMacAddress,'inputVoltage':inputVoltage,'outputVoltage':outputVoltage,'outputCurrent':outputCurrent,'outputEnable':outputEnable,'batteryVoltage':batteryVoltage,'batteryCurrent':batteryCurrent,'batteryTemperature':batteryTemperature,'batterySoc':batterySoc,'batteryNetAh':batteryNetAh,'batteryRunTime':batteryRunTime,'inputVoltageX1':inputVoltageX1,'outputVoltageX100':outputVoltageX100,'outputCurrentX100':outputCurrentX100,'batteryVoltageX100':batteryVoltageX100,'batteryCurrentX100':batteryCurrentX100})