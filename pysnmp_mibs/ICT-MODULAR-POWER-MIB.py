_K='notInstalled'
_J='NotificationType'
_I='alarmNumber'
_H='moduleNumber'
_G='read-write'
_F='disabled'
_E='enabled'
_D='ICT-MODULAR-POWER-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_IctPower_ObjectIdentity=ObjectIdentity
ictPower=_IctPower_ObjectIdentity((1,3,6,1,4,1,39145))
_PowerSystem_ObjectIdentity=ObjectIdentity
powerSystem=_PowerSystem_ObjectIdentity((1,3,6,1,4,1,39145,13))
_DeviceModel_Type=DisplayString
_DeviceModel_Object=MibScalar
deviceModel=_DeviceModel_Object((1,3,6,1,4,1,39145,13,1),_DeviceModel_Type())
deviceModel.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceModel.setStatus(_A)
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,39145,13,2),_DeviceName_Type())
deviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
class _DeviceHardware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_DeviceHardware_Type.__name__=_C
_DeviceHardware_Object=MibScalar
deviceHardware=_DeviceHardware_Object((1,3,6,1,4,1,39145,13,3),_DeviceHardware_Type())
deviceHardware.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceHardware.setStatus(_A)
_DeviceFirmware_Type=DisplayString
_DeviceFirmware_Object=MibScalar
deviceFirmware=_DeviceFirmware_Object((1,3,6,1,4,1,39145,13,4),_DeviceFirmware_Type())
deviceFirmware.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceFirmware.setStatus(_A)
_DeviceMacAddress_Type=DisplayString
_DeviceMacAddress_Object=MibScalar
deviceMacAddress=_DeviceMacAddress_Object((1,3,6,1,4,1,39145,13,5),_DeviceMacAddress_Type())
deviceMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMacAddress.setStatus(_A)
_InputVoltage_Type=DisplayString
_InputVoltage_Object=MibScalar
inputVoltage=_InputVoltage_Object((1,3,6,1,4,1,39145,13,6),_InputVoltage_Type())
inputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:inputVoltage.setStatus(_A)
_OutputVoltage_Type=DisplayString
_OutputVoltage_Object=MibScalar
outputVoltage=_OutputVoltage_Object((1,3,6,1,4,1,39145,13,7),_OutputVoltage_Type())
outputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:outputVoltage.setStatus(_A)
_OutputCurrent_Type=DisplayString
_OutputCurrent_Object=MibScalar
outputCurrent=_OutputCurrent_Object((1,3,6,1,4,1,39145,13,8),_OutputCurrent_Type())
outputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:outputCurrent.setStatus(_A)
class _OutputEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OutputEnable_Type.__name__=_C
_OutputEnable_Object=MibScalar
outputEnable=_OutputEnable_Object((1,3,6,1,4,1,39145,13,9),_OutputEnable_Type())
outputEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:outputEnable.setStatus(_A)
_ModuleTable_Object=MibTable
moduleTable=_ModuleTable_Object((1,3,6,1,4,1,39145,13,10))
if mibBuilder.loadTexts:moduleTable.setStatus(_A)
_ModuleEntry_Object=MibTableRow
moduleEntry=_ModuleEntry_Object((1,3,6,1,4,1,39145,13,10,1))
moduleEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:moduleEntry.setStatus(_A)
class _ModuleNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ModuleNumber_Type.__name__=_C
_ModuleNumber_Object=MibTableColumn
moduleNumber=_ModuleNumber_Object((1,3,6,1,4,1,39145,13,10,1,1),_ModuleNumber_Type())
moduleNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleNumber.setStatus(_A)
class _ModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('ok',2),('alarm',3)))
_ModuleStatus_Type.__name__=_C
_ModuleStatus_Object=MibTableColumn
moduleStatus=_ModuleStatus_Object((1,3,6,1,4,1,39145,13,10,1,2),_ModuleStatus_Type())
moduleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleStatus.setStatus(_A)
class _ModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),('power',2),('battery',3),('distribution',4),('converter',5)))
_ModuleType_Type.__name__=_C
_ModuleType_Object=MibTableColumn
moduleType=_ModuleType_Object((1,3,6,1,4,1,39145,13,10,1,3),_ModuleType_Type())
moduleType.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleType.setStatus(_A)
_ModuleVoltage_Type=DisplayString
_ModuleVoltage_Object=MibTableColumn
moduleVoltage=_ModuleVoltage_Object((1,3,6,1,4,1,39145,13,10,1,4),_ModuleVoltage_Type())
moduleVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleVoltage.setStatus(_A)
_ModuleCurrentA_Type=DisplayString
_ModuleCurrentA_Object=MibTableColumn
moduleCurrentA=_ModuleCurrentA_Object((1,3,6,1,4,1,39145,13,10,1,5),_ModuleCurrentA_Type())
moduleCurrentA.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCurrentA.setStatus(_A)
_ModuleCurrentB_Type=DisplayString
_ModuleCurrentB_Object=MibTableColumn
moduleCurrentB=_ModuleCurrentB_Object((1,3,6,1,4,1,39145,13,10,1,6),_ModuleCurrentB_Type())
moduleCurrentB.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCurrentB.setStatus(_A)
_ModuleCurrentC_Type=DisplayString
_ModuleCurrentC_Object=MibTableColumn
moduleCurrentC=_ModuleCurrentC_Object((1,3,6,1,4,1,39145,13,10,1,7),_ModuleCurrentC_Type())
moduleCurrentC.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCurrentC.setStatus(_A)
_ModuleCurrentD_Type=DisplayString
_ModuleCurrentD_Object=MibTableColumn
moduleCurrentD=_ModuleCurrentD_Object((1,3,6,1,4,1,39145,13,10,1,8),_ModuleCurrentD_Type())
moduleCurrentD.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCurrentD.setStatus(_A)
class _ModuleControlA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ModuleControlA_Type.__name__=_C
_ModuleControlA_Object=MibTableColumn
moduleControlA=_ModuleControlA_Object((1,3,6,1,4,1,39145,13,10,1,9),_ModuleControlA_Type())
moduleControlA.setMaxAccess(_G)
if mibBuilder.loadTexts:moduleControlA.setStatus(_A)
class _ModuleControlB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ModuleControlB_Type.__name__=_C
_ModuleControlB_Object=MibTableColumn
moduleControlB=_ModuleControlB_Object((1,3,6,1,4,1,39145,13,10,1,10),_ModuleControlB_Type())
moduleControlB.setMaxAccess(_G)
if mibBuilder.loadTexts:moduleControlB.setStatus(_A)
class _ModuleControlC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ModuleControlC_Type.__name__=_C
_ModuleControlC_Object=MibTableColumn
moduleControlC=_ModuleControlC_Object((1,3,6,1,4,1,39145,13,10,1,11),_ModuleControlC_Type())
moduleControlC.setMaxAccess(_G)
if mibBuilder.loadTexts:moduleControlC.setStatus(_A)
class _ModuleControlD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ModuleControlD_Type.__name__=_C
_ModuleControlD_Object=MibTableColumn
moduleControlD=_ModuleControlD_Object((1,3,6,1,4,1,39145,13,10,1,12),_ModuleControlD_Type())
moduleControlD.setMaxAccess(_G)
if mibBuilder.loadTexts:moduleControlD.setStatus(_A)
_AlarmTable_Object=MibTable
alarmTable=_AlarmTable_Object((1,3,6,1,4,1,39145,13,11))
if mibBuilder.loadTexts:alarmTable.setStatus(_A)
_AlarmEntry_Object=MibTableRow
alarmEntry=_AlarmEntry_Object((1,3,6,1,4,1,39145,13,11,1))
alarmEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:alarmEntry.setStatus(_A)
class _AlarmNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AlarmNumber_Type.__name__=_C
_AlarmNumber_Object=MibTableColumn
alarmNumber=_AlarmNumber_Object((1,3,6,1,4,1,39145,13,11,1,1),_AlarmNumber_Type())
alarmNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmNumber.setStatus(_A)
_AlarmName_Type=DisplayString
_AlarmName_Object=MibTableColumn
alarmName=_AlarmName_Object((1,3,6,1,4,1,39145,13,11,1,2),_AlarmName_Type())
alarmName.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmName.setStatus(_A)
class _AlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),('ready',2),('alarm',3)))
_AlarmStatus_Type.__name__=_C
_AlarmStatus_Object=MibTableColumn
alarmStatus=_AlarmStatus_Object((1,3,6,1,4,1,39145,13,11,1,3),_AlarmStatus_Type())
alarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmStatus.setStatus(_A)
_BatteryTemperature_Type=Integer32
_BatteryTemperature_Object=MibScalar
batteryTemperature=_BatteryTemperature_Object((1,3,6,1,4,1,39145,13,12),_BatteryTemperature_Type())
batteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryTemperature.setStatus(_A)
class _BatterySoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BatterySoc_Type.__name__=_C
_BatterySoc_Object=MibScalar
batterySoc=_BatterySoc_Object((1,3,6,1,4,1,39145,13,13),_BatterySoc_Type())
batterySoc.setMaxAccess(_B)
if mibBuilder.loadTexts:batterySoc.setStatus(_A)
_BatteryNetAh_Type=Integer32
_BatteryNetAh_Object=MibScalar
batteryNetAh=_BatteryNetAh_Object((1,3,6,1,4,1,39145,13,14),_BatteryNetAh_Type())
batteryNetAh.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryNetAh.setStatus(_A)
_BatteryRunTime_Type=Integer32
_BatteryRunTime_Object=MibScalar
batteryRunTime=_BatteryRunTime_Object((1,3,6,1,4,1,39145,13,15),_BatteryRunTime_Type())
batteryRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:batteryRunTime.setStatus(_A)
moduleAlarmTrap=NotificationType((1,3,6,1,4,1,39145,13,0,101))
moduleAlarmTrap.setObjects((_D,_H))
if mibBuilder.loadTexts:moduleAlarmTrap.setStatus('')
alarmInputTrap=NotificationType((1,3,6,1,4,1,39145,13,0,102))
alarmInputTrap.setObjects((_D,_I))
if mibBuilder.loadTexts:alarmInputTrap.setStatus('')
acFailAlarmTrap=NotificationType((1,3,6,1,4,1,39145,13,0,103))
if mibBuilder.loadTexts:acFailAlarmTrap.setStatus('')
sysCurrentLimitTrap=NotificationType((1,3,6,1,4,1,39145,13,0,104))
if mibBuilder.loadTexts:sysCurrentLimitTrap.setStatus('')
moduleAlarmClear=NotificationType((1,3,6,1,4,1,39145,13,0,111))
moduleAlarmClear.setObjects((_D,_H))
if mibBuilder.loadTexts:moduleAlarmClear.setStatus('')
alarmInputClear=NotificationType((1,3,6,1,4,1,39145,13,0,112))
alarmInputClear.setObjects((_D,_I))
if mibBuilder.loadTexts:alarmInputClear.setStatus('')
acFailAlarmClear=NotificationType((1,3,6,1,4,1,39145,13,0,113))
if mibBuilder.loadTexts:acFailAlarmClear.setStatus('')
sysCurrentLimitClear=NotificationType((1,3,6,1,4,1,39145,13,0,114))
if mibBuilder.loadTexts:sysCurrentLimitClear.setStatus('')
batteryTestStart=NotificationType((1,3,6,1,4,1,39145,13,0,121))
if mibBuilder.loadTexts:batteryTestStart.setStatus('')
batteryTestComplete=NotificationType((1,3,6,1,4,1,39145,13,0,122))
if mibBuilder.loadTexts:batteryTestComplete.setStatus('')
batteryTestFail=NotificationType((1,3,6,1,4,1,39145,13,0,123))
if mibBuilder.loadTexts:batteryTestFail.setStatus('')
batteryEqualiseStart=NotificationType((1,3,6,1,4,1,39145,13,0,124))
if mibBuilder.loadTexts:batteryEqualiseStart.setStatus('')
batteryEqualiseComplete=NotificationType((1,3,6,1,4,1,39145,13,0,125))
if mibBuilder.loadTexts:batteryEqualiseComplete.setStatus('')
mibBuilder.exportSymbols(_D,**{'ictPower':ictPower,'powerSystem':powerSystem,'moduleAlarmTrap':moduleAlarmTrap,'alarmInputTrap':alarmInputTrap,'acFailAlarmTrap':acFailAlarmTrap,'sysCurrentLimitTrap':sysCurrentLimitTrap,'moduleAlarmClear':moduleAlarmClear,'alarmInputClear':alarmInputClear,'acFailAlarmClear':acFailAlarmClear,'sysCurrentLimitClear':sysCurrentLimitClear,'batteryTestStart':batteryTestStart,'batteryTestComplete':batteryTestComplete,'batteryTestFail':batteryTestFail,'batteryEqualiseStart':batteryEqualiseStart,'batteryEqualiseComplete':batteryEqualiseComplete,'deviceModel':deviceModel,'deviceName':deviceName,'deviceHardware':deviceHardware,'deviceFirmware':deviceFirmware,'deviceMacAddress':deviceMacAddress,'inputVoltage':inputVoltage,'outputVoltage':outputVoltage,'outputCurrent':outputCurrent,'outputEnable':outputEnable,'moduleTable':moduleTable,'moduleEntry':moduleEntry,_H:moduleNumber,'moduleStatus':moduleStatus,'moduleType':moduleType,'moduleVoltage':moduleVoltage,'moduleCurrentA':moduleCurrentA,'moduleCurrentB':moduleCurrentB,'moduleCurrentC':moduleCurrentC,'moduleCurrentD':moduleCurrentD,'moduleControlA':moduleControlA,'moduleControlB':moduleControlB,'moduleControlC':moduleControlC,'moduleControlD':moduleControlD,'alarmTable':alarmTable,'alarmEntry':alarmEntry,_I:alarmNumber,'alarmName':alarmName,'alarmStatus':alarmStatus,'batteryTemperature':batteryTemperature,'batterySoc':batterySoc,'batteryNetAh':batteryNetAh,'batteryRunTime':batteryRunTime})