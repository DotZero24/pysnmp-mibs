_G='inverter'
_F='disabled'
_E='enabled'
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
_Inverter_ObjectIdentity=ObjectIdentity
inverter=_Inverter_ObjectIdentity((1,3,6,1,4,1,39145,12))
_DeviceModel_Type=DisplayString
_DeviceModel_Object=MibScalar
deviceModel=_DeviceModel_Object((1,3,6,1,4,1,39145,12,1),_DeviceModel_Type())
deviceModel.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceModel.setStatus(_A)
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,39145,12,2),_DeviceName_Type())
deviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
class _DeviceHardware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_DeviceHardware_Type.__name__=_C
_DeviceHardware_Object=MibScalar
deviceHardware=_DeviceHardware_Object((1,3,6,1,4,1,39145,12,3),_DeviceHardware_Type())
deviceHardware.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceHardware.setStatus(_A)
_DeviceFirmware_Type=DisplayString
_DeviceFirmware_Object=MibScalar
deviceFirmware=_DeviceFirmware_Object((1,3,6,1,4,1,39145,12,4),_DeviceFirmware_Type())
deviceFirmware.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceFirmware.setStatus(_A)
_DeviceMacAddress_Type=DisplayString
_DeviceMacAddress_Object=MibScalar
deviceMacAddress=_DeviceMacAddress_Object((1,3,6,1,4,1,39145,12,5),_DeviceMacAddress_Type())
deviceMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMacAddress.setStatus(_A)
_BatteryVoltage_Type=DisplayString
_BatteryVoltage_Object=MibScalar
batteryVoltage=_BatteryVoltage_Object((1,3,6,1,4,1,39145,12,6),_BatteryVoltage_Type())
batteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryVoltage.setStatus(_A)
_InverterVoltage_Type=DisplayString
_InverterVoltage_Object=MibScalar
inverterVoltage=_InverterVoltage_Object((1,3,6,1,4,1,39145,12,7),_InverterVoltage_Type())
inverterVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:inverterVoltage.setStatus(_A)
_InverterPower_Type=DisplayString
_InverterPower_Object=MibScalar
inverterPower=_InverterPower_Object((1,3,6,1,4,1,39145,12,8),_InverterPower_Type())
inverterPower.setMaxAccess(_B)
if mibBuilder.loadTexts:inverterPower.setStatus(_A)
class _InverterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_InverterStatus_Type.__name__=_C
_InverterStatus_Object=MibScalar
inverterStatus=_InverterStatus_Object((1,3,6,1,4,1,39145,12,9),_InverterStatus_Type())
inverterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:inverterStatus.setStatus(_A)
class _InverterControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_InverterControl_Type.__name__=_C
_InverterControl_Object=MibScalar
inverterControl=_InverterControl_Object((1,3,6,1,4,1,39145,12,10),_InverterControl_Type())
inverterControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:inverterControl.setStatus(_A)
class _TransferRelayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('grid',2)))
_TransferRelayStatus_Type.__name__=_C
_TransferRelayStatus_Object=MibScalar
transferRelayStatus=_TransferRelayStatus_Object((1,3,6,1,4,1,39145,12,11),_TransferRelayStatus_Type())
transferRelayStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:transferRelayStatus.setStatus(_A)
undervoltageAlarmTrap=NotificationType((1,3,6,1,4,1,39145,12,0,101))
if mibBuilder.loadTexts:undervoltageAlarmTrap.setStatus('')
overvoltageAlarmTrap=NotificationType((1,3,6,1,4,1,39145,12,0,102))
if mibBuilder.loadTexts:overvoltageAlarmTrap.setStatus('')
overtemperatureAlarmTrap=NotificationType((1,3,6,1,4,1,39145,12,0,103))
if mibBuilder.loadTexts:overtemperatureAlarmTrap.setStatus('')
outputFaultAlarmTrap=NotificationType((1,3,6,1,4,1,39145,12,0,104))
if mibBuilder.loadTexts:outputFaultAlarmTrap.setStatus('')
systemFaultAlarmTrap=NotificationType((1,3,6,1,4,1,39145,12,0,105))
if mibBuilder.loadTexts:systemFaultAlarmTrap.setStatus('')
remoteSwitchAlarmTrap=NotificationType((1,3,6,1,4,1,39145,12,0,106))
if mibBuilder.loadTexts:remoteSwitchAlarmTrap.setStatus('')
undervoltageAlarmClear=NotificationType((1,3,6,1,4,1,39145,12,0,111))
if mibBuilder.loadTexts:undervoltageAlarmClear.setStatus('')
overvoltageAlarmClear=NotificationType((1,3,6,1,4,1,39145,12,0,112))
if mibBuilder.loadTexts:overvoltageAlarmClear.setStatus('')
overtemperatureAlarmClear=NotificationType((1,3,6,1,4,1,39145,12,0,113))
if mibBuilder.loadTexts:overtemperatureAlarmClear.setStatus('')
outputFaultAlarmClear=NotificationType((1,3,6,1,4,1,39145,12,0,114))
if mibBuilder.loadTexts:outputFaultAlarmClear.setStatus('')
systemFaultAlarmClear=NotificationType((1,3,6,1,4,1,39145,12,0,115))
if mibBuilder.loadTexts:systemFaultAlarmClear.setStatus('')
remoteSwitchAlarmClear=NotificationType((1,3,6,1,4,1,39145,12,0,116))
if mibBuilder.loadTexts:remoteSwitchAlarmClear.setStatus('')
inverterPowerTrap=NotificationType((1,3,6,1,4,1,39145,12,0,121))
if mibBuilder.loadTexts:inverterPowerTrap.setStatus('')
gridPowerTrap=NotificationType((1,3,6,1,4,1,39145,12,0,122))
if mibBuilder.loadTexts:gridPowerTrap.setStatus('')
mibBuilder.exportSymbols('ICT-SINE-WAVE-MIB',**{'ictPower':ictPower,_G:inverter,'undervoltageAlarmTrap':undervoltageAlarmTrap,'overvoltageAlarmTrap':overvoltageAlarmTrap,'overtemperatureAlarmTrap':overtemperatureAlarmTrap,'outputFaultAlarmTrap':outputFaultAlarmTrap,'systemFaultAlarmTrap':systemFaultAlarmTrap,'remoteSwitchAlarmTrap':remoteSwitchAlarmTrap,'undervoltageAlarmClear':undervoltageAlarmClear,'overvoltageAlarmClear':overvoltageAlarmClear,'overtemperatureAlarmClear':overtemperatureAlarmClear,'outputFaultAlarmClear':outputFaultAlarmClear,'systemFaultAlarmClear':systemFaultAlarmClear,'remoteSwitchAlarmClear':remoteSwitchAlarmClear,'inverterPowerTrap':inverterPowerTrap,'gridPowerTrap':gridPowerTrap,'deviceModel':deviceModel,'deviceName':deviceName,'deviceHardware':deviceHardware,'deviceFirmware':deviceFirmware,'deviceMacAddress':deviceMacAddress,'batteryVoltage':batteryVoltage,'inverterVoltage':inverterVoltage,'inverterPower':inverterPower,'inverterStatus':inverterStatus,'inverterControl':inverterControl,'transferRelayStatus':transferRelayStatus})