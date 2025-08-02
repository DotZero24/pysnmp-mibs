_H='NotificationType'
_G='alarmNumber'
_F='busNumber'
_E='Integer32'
_D='outputNumber'
_C='read-only'
_B='ICT-DISTRIBUTION-PANEL-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_IctPower_ObjectIdentity=ObjectIdentity
ictPower=_IctPower_ObjectIdentity((1,3,6,1,4,1,39145))
_DistPanel_ObjectIdentity=ObjectIdentity
distPanel=_DistPanel_ObjectIdentity((1,3,6,1,4,1,39145,10))
_DeviceModel_Type=DisplayString
_DeviceModel_Object=MibScalar
deviceModel=_DeviceModel_Object((1,3,6,1,4,1,39145,10,1),_DeviceModel_Type())
deviceModel.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceModel.setStatus(_A)
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,39145,10,2),_DeviceName_Type())
deviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
class _DeviceHardware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_DeviceHardware_Type.__name__=_E
_DeviceHardware_Object=MibScalar
deviceHardware=_DeviceHardware_Object((1,3,6,1,4,1,39145,10,3),_DeviceHardware_Type())
deviceHardware.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceHardware.setStatus(_A)
_DeviceFirmware_Type=DisplayString
_DeviceFirmware_Object=MibScalar
deviceFirmware=_DeviceFirmware_Object((1,3,6,1,4,1,39145,10,4),_DeviceFirmware_Type())
deviceFirmware.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceFirmware.setStatus(_A)
_DeviceMacAddress_Type=DisplayString
_DeviceMacAddress_Object=MibScalar
deviceMacAddress=_DeviceMacAddress_Object((1,3,6,1,4,1,39145,10,5),_DeviceMacAddress_Type())
deviceMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceMacAddress.setStatus(_A)
_SystemVoltage_Type=DisplayString
_SystemVoltage_Object=MibScalar
systemVoltage=_SystemVoltage_Object((1,3,6,1,4,1,39145,10,6),_SystemVoltage_Type())
systemVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:systemVoltage.setStatus(_A)
_SystemCurrent_Type=DisplayString
_SystemCurrent_Object=MibScalar
systemCurrent=_SystemCurrent_Object((1,3,6,1,4,1,39145,10,7),_SystemCurrent_Type())
systemCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:systemCurrent.setStatus(_A)
_OutputTable_Object=MibTable
outputTable=_OutputTable_Object((1,3,6,1,4,1,39145,10,8))
if mibBuilder.loadTexts:outputTable.setStatus(_A)
_OutputEntry_Object=MibTableRow
outputEntry=_OutputEntry_Object((1,3,6,1,4,1,39145,10,8,1))
outputEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:outputEntry.setStatus(_A)
class _OutputNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_OutputNumber_Type.__name__=_E
_OutputNumber_Object=MibTableColumn
outputNumber=_OutputNumber_Object((1,3,6,1,4,1,39145,10,8,1,1),_OutputNumber_Type())
outputNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:outputNumber.setStatus(_A)
_OutputName_Type=DisplayString
_OutputName_Object=MibTableColumn
outputName=_OutputName_Object((1,3,6,1,4,1,39145,10,8,1,2),_OutputName_Type())
outputName.setMaxAccess(_C)
if mibBuilder.loadTexts:outputName.setStatus(_A)
_OutputCurrent_Type=DisplayString
_OutputCurrent_Object=MibTableColumn
outputCurrent=_OutputCurrent_Object((1,3,6,1,4,1,39145,10,8,1,3),_OutputCurrent_Type())
outputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:outputCurrent.setStatus(_A)
class _OutputFuseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('open',2)))
_OutputFuseStatus_Type.__name__=_E
_OutputFuseStatus_Object=MibTableColumn
outputFuseStatus=_OutputFuseStatus_Object((1,3,6,1,4,1,39145,10,8,1,4),_OutputFuseStatus_Type())
outputFuseStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:outputFuseStatus.setStatus(_A)
class _OutputEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_OutputEnable_Type.__name__=_E
_OutputEnable_Object=MibTableColumn
outputEnable=_OutputEnable_Object((1,3,6,1,4,1,39145,10,8,1,5),_OutputEnable_Type())
outputEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:outputEnable.setStatus(_A)
_AlarmTable_Object=MibTable
alarmTable=_AlarmTable_Object((1,3,6,1,4,1,39145,10,9))
if mibBuilder.loadTexts:alarmTable.setStatus(_A)
_AlarmEntry_Object=MibTableRow
alarmEntry=_AlarmEntry_Object((1,3,6,1,4,1,39145,10,9,1))
alarmEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:alarmEntry.setStatus(_A)
class _AlarmNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AlarmNumber_Type.__name__=_E
_AlarmNumber_Object=MibTableColumn
alarmNumber=_AlarmNumber_Object((1,3,6,1,4,1,39145,10,9,1,1),_AlarmNumber_Type())
alarmNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmNumber.setStatus(_A)
_AlarmName_Type=DisplayString
_AlarmName_Object=MibTableColumn
alarmName=_AlarmName_Object((1,3,6,1,4,1,39145,10,9,1,2),_AlarmName_Type())
alarmName.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmName.setStatus(_A)
class _AlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),('ready',2),('alarm',3)))
_AlarmStatus_Type.__name__=_E
_AlarmStatus_Object=MibTableColumn
alarmStatus=_AlarmStatus_Object((1,3,6,1,4,1,39145,10,9,1,3),_AlarmStatus_Type())
alarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmStatus.setStatus(_A)
_BusTable_Object=MibTable
busTable=_BusTable_Object((1,3,6,1,4,1,39145,10,10))
if mibBuilder.loadTexts:busTable.setStatus(_A)
_BusEntry_Object=MibTableRow
busEntry=_BusEntry_Object((1,3,6,1,4,1,39145,10,10,1))
busEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:busEntry.setStatus(_A)
class _BusNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BusNumber_Type.__name__=_E
_BusNumber_Object=MibTableColumn
busNumber=_BusNumber_Object((1,3,6,1,4,1,39145,10,10,1,1),_BusNumber_Type())
busNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:busNumber.setStatus(_A)
_BusName_Type=DisplayString
_BusName_Object=MibTableColumn
busName=_BusName_Object((1,3,6,1,4,1,39145,10,10,1,2),_BusName_Type())
busName.setMaxAccess(_C)
if mibBuilder.loadTexts:busName.setStatus(_A)
_BusVoltage_Type=DisplayString
_BusVoltage_Object=MibTableColumn
busVoltage=_BusVoltage_Object((1,3,6,1,4,1,39145,10,10,1,3),_BusVoltage_Type())
busVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:busVoltage.setStatus(_A)
_BusCurrent_Type=DisplayString
_BusCurrent_Object=MibTableColumn
busCurrent=_BusCurrent_Object((1,3,6,1,4,1,39145,10,10,1,4),_BusCurrent_Type())
busCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:busCurrent.setStatus(_A)
sysUndervoltageAlarmTrap=NotificationType((1,3,6,1,4,1,39145,10,0,101))
sysUndervoltageAlarmTrap.setObjects((_B,_F))
if mibBuilder.loadTexts:sysUndervoltageAlarmTrap.setStatus('')
sysOvervoltageAlarmTrap=NotificationType((1,3,6,1,4,1,39145,10,0,102))
sysOvervoltageAlarmTrap.setObjects((_B,_F))
if mibBuilder.loadTexts:sysOvervoltageAlarmTrap.setStatus('')
sysOvercurrentAlarmTrap=NotificationType((1,3,6,1,4,1,39145,10,0,103))
sysOvercurrentAlarmTrap.setObjects((_B,_F))
if mibBuilder.loadTexts:sysOvercurrentAlarmTrap.setStatus('')
fuseAlarmTrap=NotificationType((1,3,6,1,4,1,39145,10,0,104))
fuseAlarmTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:fuseAlarmTrap.setStatus('')
undercurrentAlarmTrap=NotificationType((1,3,6,1,4,1,39145,10,0,105))
undercurrentAlarmTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:undercurrentAlarmTrap.setStatus('')
overcurrentAlarmTrap=NotificationType((1,3,6,1,4,1,39145,10,0,106))
overcurrentAlarmTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:overcurrentAlarmTrap.setStatus('')
loadshedTrap=NotificationType((1,3,6,1,4,1,39145,10,0,107))
loadshedTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:loadshedTrap.setStatus('')
alarmInputTrap=NotificationType((1,3,6,1,4,1,39145,10,0,108))
alarmInputTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:alarmInputTrap.setStatus('')
sysUndervoltageAlarmClear=NotificationType((1,3,6,1,4,1,39145,10,0,111))
sysUndervoltageAlarmClear.setObjects((_B,_F))
if mibBuilder.loadTexts:sysUndervoltageAlarmClear.setStatus('')
sysOvervoltageAlarmClear=NotificationType((1,3,6,1,4,1,39145,10,0,112))
sysOvervoltageAlarmClear.setObjects((_B,_F))
if mibBuilder.loadTexts:sysOvervoltageAlarmClear.setStatus('')
sysOvercurrentAlarmClear=NotificationType((1,3,6,1,4,1,39145,10,0,113))
sysOvercurrentAlarmClear.setObjects((_B,_F))
if mibBuilder.loadTexts:sysOvercurrentAlarmClear.setStatus('')
fuseAlarmClear=NotificationType((1,3,6,1,4,1,39145,10,0,114))
fuseAlarmClear.setObjects((_B,_D))
if mibBuilder.loadTexts:fuseAlarmClear.setStatus('')
undercurrentAlarmClear=NotificationType((1,3,6,1,4,1,39145,10,0,115))
undercurrentAlarmClear.setObjects((_B,_D))
if mibBuilder.loadTexts:undercurrentAlarmClear.setStatus('')
overcurrentAlarmClear=NotificationType((1,3,6,1,4,1,39145,10,0,116))
overcurrentAlarmClear.setObjects((_B,_D))
if mibBuilder.loadTexts:overcurrentAlarmClear.setStatus('')
loadshedClear=NotificationType((1,3,6,1,4,1,39145,10,0,117))
loadshedClear.setObjects((_B,_D))
if mibBuilder.loadTexts:loadshedClear.setStatus('')
alarmInputClear=NotificationType((1,3,6,1,4,1,39145,10,0,118))
alarmInputClear.setObjects((_B,_G))
if mibBuilder.loadTexts:alarmInputClear.setStatus('')
mibBuilder.exportSymbols(_B,**{'ictPower':ictPower,'distPanel':distPanel,'sysUndervoltageAlarmTrap':sysUndervoltageAlarmTrap,'sysOvervoltageAlarmTrap':sysOvervoltageAlarmTrap,'sysOvercurrentAlarmTrap':sysOvercurrentAlarmTrap,'fuseAlarmTrap':fuseAlarmTrap,'undercurrentAlarmTrap':undercurrentAlarmTrap,'overcurrentAlarmTrap':overcurrentAlarmTrap,'loadshedTrap':loadshedTrap,'alarmInputTrap':alarmInputTrap,'sysUndervoltageAlarmClear':sysUndervoltageAlarmClear,'sysOvervoltageAlarmClear':sysOvervoltageAlarmClear,'sysOvercurrentAlarmClear':sysOvercurrentAlarmClear,'fuseAlarmClear':fuseAlarmClear,'undercurrentAlarmClear':undercurrentAlarmClear,'overcurrentAlarmClear':overcurrentAlarmClear,'loadshedClear':loadshedClear,'alarmInputClear':alarmInputClear,'deviceModel':deviceModel,'deviceName':deviceName,'deviceHardware':deviceHardware,'deviceFirmware':deviceFirmware,'deviceMacAddress':deviceMacAddress,'systemVoltage':systemVoltage,'systemCurrent':systemCurrent,'outputTable':outputTable,'outputEntry':outputEntry,_D:outputNumber,'outputName':outputName,'outputCurrent':outputCurrent,'outputFuseStatus':outputFuseStatus,'outputEnable':outputEnable,'alarmTable':alarmTable,'alarmEntry':alarmEntry,_G:alarmNumber,'alarmName':alarmName,'alarmStatus':alarmStatus,'busTable':busTable,'busEntry':busEntry,_F:busNumber,'busName':busName,'busVoltage':busVoltage,'busCurrent':busCurrent})