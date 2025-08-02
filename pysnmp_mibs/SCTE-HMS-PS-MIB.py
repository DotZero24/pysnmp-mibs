_T='psTemperatureSensor'
_S='psTempDeviceAddress'
_R='psOutput'
_Q='psOutputDeviceAddress'
_P='psBattery'
_O='psBatteryString'
_N='psBatteryDeviceAddress'
_M='psString'
_L='psStringDeviceAddress'
_K='noAlarm'
_J='psDeviceAddress'
_I='DisplayString'
_H='OctetString'
_G='supported'
_F='none'
_E='SCTE-HMS-PS-MIB'
_D='optional'
_C='mandatory'
_B='Integer32'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
psIdent,=mibBuilder.importSymbols('SCTE-HMS-ROOTS','psIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
class _PsMonitored_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_PsMonitored_Type.__name__=_B
_PsMonitored_Object=MibScalar
psMonitored=_PsMonitored_Object((1,3,6,1,4,1,5591,1,4,1),_PsMonitored_Type())
psMonitored.setMaxAccess(_A)
if mibBuilder.loadTexts:psMonitored.setStatus(_C)
_PsDeviceTable_Object=MibTable
psDeviceTable=_PsDeviceTable_Object((1,3,6,1,4,1,5591,1,4,2))
if mibBuilder.loadTexts:psDeviceTable.setStatus(_C)
_PsDeviceEntry_Object=MibTableRow
psDeviceEntry=_PsDeviceEntry_Object((1,3,6,1,4,1,5591,1,4,2,1))
psDeviceEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:psDeviceEntry.setStatus(_C)
class _PsDeviceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PsDeviceAddress_Type.__name__=_B
_PsDeviceAddress_Object=MibTableColumn
psDeviceAddress=_PsDeviceAddress_Object((1,3,6,1,4,1,5591,1,4,2,1,1),_PsDeviceAddress_Type())
psDeviceAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:psDeviceAddress.setStatus(_C)
class _PsProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_PsProtocolVersion_Type.__name__=_B
_PsProtocolVersion_Object=MibTableColumn
psProtocolVersion=_PsProtocolVersion_Object((1,3,6,1,4,1,5591,1,4,2,1,2),_PsProtocolVersion_Type())
psProtocolVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:psProtocolVersion.setStatus(_C)
class _PsSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PsSoftwareVersion_Type.__name__=_I
_PsSoftwareVersion_Object=MibTableColumn
psSoftwareVersion=_PsSoftwareVersion_Object((1,3,6,1,4,1,5591,1,4,2,1,3),_PsSoftwareVersion_Type())
psSoftwareVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:psSoftwareVersion.setStatus(_C)
class _PsDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_PsDeviceId_Type.__name__=_H
_PsDeviceId_Object=MibTableColumn
psDeviceId=_PsDeviceId_Object((1,3,6,1,4,1,5591,1,4,2,1,4),_PsDeviceId_Type())
psDeviceId.setMaxAccess(_A)
if mibBuilder.loadTexts:psDeviceId.setStatus(_C)
class _PsBatteries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_PsBatteries_Type.__name__=_B
_PsBatteries_Object=MibTableColumn
psBatteries=_PsBatteries_Object((1,3,6,1,4,1,5591,1,4,2,1,5),_PsBatteries_Type())
psBatteries.setMaxAccess(_A)
if mibBuilder.loadTexts:psBatteries.setStatus(_C)
class _PsBatteryStrings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_PsBatteryStrings_Type.__name__=_B
_PsBatteryStrings_Object=MibTableColumn
psBatteryStrings=_PsBatteryStrings_Object((1,3,6,1,4,1,5591,1,4,2,1,6),_PsBatteryStrings_Type())
psBatteryStrings.setMaxAccess(_A)
if mibBuilder.loadTexts:psBatteryStrings.setStatus(_C)
class _PsTempSensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_PsTempSensors_Type.__name__=_B
_PsTempSensors_Object=MibTableColumn
psTempSensors=_PsTempSensors_Object((1,3,6,1,4,1,5591,1,4,2,1,7),_PsTempSensors_Type())
psTempSensors.setMaxAccess(_A)
if mibBuilder.loadTexts:psTempSensors.setStatus(_C)
class _PsOutputs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_PsOutputs_Type.__name__=_B
_PsOutputs_Object=MibTableColumn
psOutputs=_PsOutputs_Object((1,3,6,1,4,1,5591,1,4,2,1,8),_PsOutputs_Type())
psOutputs.setMaxAccess(_A)
if mibBuilder.loadTexts:psOutputs.setStatus(_C)
_PsBatteryCurrentSupport_Type=Integer32
_PsBatteryCurrentSupport_Object=MibTableColumn
psBatteryCurrentSupport=_PsBatteryCurrentSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,9),_PsBatteryCurrentSupport_Type())
psBatteryCurrentSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psBatteryCurrentSupport.setStatus(_C)
_PsFloatCurrentSupport_Type=Integer32
_PsFloatCurrentSupport_Object=MibTableColumn
psFloatCurrentSupport=_PsFloatCurrentSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,10),_PsFloatCurrentSupport_Type())
psFloatCurrentSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psFloatCurrentSupport.setStatus(_C)
class _PsOutputVoltageSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PsOutputVoltageSupport_Type.__name__=_B
_PsOutputVoltageSupport_Object=MibTableColumn
psOutputVoltageSupport=_PsOutputVoltageSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,11),_PsOutputVoltageSupport_Type())
psOutputVoltageSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psOutputVoltageSupport.setStatus(_C)
class _PsInputVoltageSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('binary',2),('analog',3)))
_PsInputVoltageSupport_Type.__name__=_B
_PsInputVoltageSupport_Object=MibTableColumn
psInputVoltageSupport=_PsInputVoltageSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,12),_PsInputVoltageSupport_Type())
psInputVoltageSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psInputVoltageSupport.setStatus(_C)
class _PsPowerSupplyTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PsPowerSupplyTest_Type.__name__=_B
_PsPowerSupplyTest_Object=MibTableColumn
psPowerSupplyTest=_PsPowerSupplyTest_Object((1,3,6,1,4,1,5591,1,4,2,1,13),_PsPowerSupplyTest_Type())
psPowerSupplyTest.setMaxAccess(_A)
if mibBuilder.loadTexts:psPowerSupplyTest.setStatus(_C)
class _PsMajorAlarmSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PsMajorAlarmSupport_Type.__name__=_B
_PsMajorAlarmSupport_Object=MibTableColumn
psMajorAlarmSupport=_PsMajorAlarmSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,14),_PsMajorAlarmSupport_Type())
psMajorAlarmSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psMajorAlarmSupport.setStatus(_C)
class _PsMinorAlarmSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PsMinorAlarmSupport_Type.__name__=_B
_PsMinorAlarmSupport_Object=MibTableColumn
psMinorAlarmSupport=_PsMinorAlarmSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,15),_PsMinorAlarmSupport_Type())
psMinorAlarmSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psMinorAlarmSupport.setStatus(_C)
class _PsTamperSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PsTamperSupport_Type.__name__=_B
_PsTamperSupport_Object=MibTableColumn
psTamperSupport=_PsTamperSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,16),_PsTamperSupport_Type())
psTamperSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psTamperSupport.setStatus(_C)
class _PsBatteryVoltageSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noMonitoring',1),('totalString',2),('both',3)))
_PsBatteryVoltageSupport_Type.__name__=_B
_PsBatteryVoltageSupport_Object=MibTableColumn
psBatteryVoltageSupport=_PsBatteryVoltageSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,17),_PsBatteryVoltageSupport_Type())
psBatteryVoltageSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psBatteryVoltageSupport.setStatus(_C)
class _PsOutputPowerSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PsOutputPowerSupport_Type.__name__=_B
_PsOutputPowerSupport_Object=MibTableColumn
psOutputPowerSupport=_PsOutputPowerSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,18),_PsOutputPowerSupport_Type())
psOutputPowerSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psOutputPowerSupport.setStatus(_C)
class _PsOutputFrequencySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PsOutputFrequencySupport_Type.__name__=_B
_PsOutputFrequencySupport_Object=MibTableColumn
psOutputFrequencySupport=_PsOutputFrequencySupport_Object((1,3,6,1,4,1,5591,1,4,2,1,19),_PsOutputFrequencySupport_Type())
psOutputFrequencySupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psOutputFrequencySupport.setStatus(_C)
class _PsInputCurrentSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PsInputCurrentSupport_Type.__name__=_B
_PsInputCurrentSupport_Object=MibTableColumn
psInputCurrentSupport=_PsInputCurrentSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,20),_PsInputCurrentSupport_Type())
psInputCurrentSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psInputCurrentSupport.setStatus(_C)
class _PsInputPowerSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PsInputPowerSupport_Type.__name__=_B
_PsInputPowerSupport_Object=MibTableColumn
psInputPowerSupport=_PsInputPowerSupport_Object((1,3,6,1,4,1,5591,1,4,2,1,21),_PsInputPowerSupport_Type())
psInputPowerSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:psInputPowerSupport.setStatus(_C)
class _PsOutputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsOutputVoltage_Type.__name__=_B
_PsOutputVoltage_Object=MibTableColumn
psOutputVoltage=_PsOutputVoltage_Object((1,3,6,1,4,1,5591,1,4,2,1,22),_PsOutputVoltage_Type())
psOutputVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:psOutputVoltage.setStatus(_C)
class _PsInputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsInputVoltage_Type.__name__=_B
_PsInputVoltage_Object=MibTableColumn
psInputVoltage=_PsInputVoltage_Object((1,3,6,1,4,1,5591,1,4,2,1,23),_PsInputVoltage_Type())
psInputVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:psInputVoltage.setStatus(_D)
class _PsInverterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('off',1),('lineFail',2),('testCycle',3),('testStarted',4),('testFailed',5)))
_PsInverterStatus_Type.__name__=_B
_PsInverterStatus_Object=MibTableColumn
psInverterStatus=_PsInverterStatus_Object((1,3,6,1,4,1,5591,1,4,2,1,24),_PsInverterStatus_Type())
psInverterStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:psInverterStatus.setStatus(_D)
class _PsMajorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('alarm',2)))
_PsMajorAlarm_Type.__name__=_B
_PsMajorAlarm_Object=MibTableColumn
psMajorAlarm=_PsMajorAlarm_Object((1,3,6,1,4,1,5591,1,4,2,1,25),_PsMajorAlarm_Type())
psMajorAlarm.setMaxAccess(_A)
if mibBuilder.loadTexts:psMajorAlarm.setStatus(_D)
class _PsMinorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('alarm',2)))
_PsMinorAlarm_Type.__name__=_B
_PsMinorAlarm_Object=MibTableColumn
psMinorAlarm=_PsMinorAlarm_Object((1,3,6,1,4,1,5591,1,4,2,1,26),_PsMinorAlarm_Type())
psMinorAlarm.setMaxAccess(_A)
if mibBuilder.loadTexts:psMinorAlarm.setStatus(_D)
class _PsTamper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('closed',1),('open',2)))
_PsTamper_Type.__name__=_B
_PsTamper_Object=MibTableColumn
psTamper=_PsTamper_Object((1,3,6,1,4,1,5591,1,4,2,1,27),_PsTamper_Type())
psTamper.setMaxAccess(_A)
if mibBuilder.loadTexts:psTamper.setStatus(_D)
class _PsTotalStringVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsTotalStringVoltage_Type.__name__=_B
_PsTotalStringVoltage_Object=MibTableColumn
psTotalStringVoltage=_PsTotalStringVoltage_Object((1,3,6,1,4,1,5591,1,4,2,1,28),_PsTotalStringVoltage_Type())
psTotalStringVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:psTotalStringVoltage.setStatus(_D)
class _PsEquipmentControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stopTest',1),('startTest',2)))
_PsEquipmentControl_Type.__name__=_B
_PsEquipmentControl_Object=MibTableColumn
psEquipmentControl=_PsEquipmentControl_Object((1,3,6,1,4,1,5591,1,4,2,1,29),_PsEquipmentControl_Type())
psEquipmentControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:psEquipmentControl.setStatus(_D)
class _PsPowerOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsPowerOut_Type.__name__=_B
_PsPowerOut_Object=MibTableColumn
psPowerOut=_PsPowerOut_Object((1,3,6,1,4,1,5591,1,4,2,1,30),_PsPowerOut_Type())
psPowerOut.setMaxAccess(_A)
if mibBuilder.loadTexts:psPowerOut.setStatus(_D)
class _PsFrequencyOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsFrequencyOut_Type.__name__=_B
_PsFrequencyOut_Object=MibTableColumn
psFrequencyOut=_PsFrequencyOut_Object((1,3,6,1,4,1,5591,1,4,2,1,31),_PsFrequencyOut_Type())
psFrequencyOut.setMaxAccess(_A)
if mibBuilder.loadTexts:psFrequencyOut.setStatus(_D)
class _PsRMSCurrentIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsRMSCurrentIn_Type.__name__=_B
_PsRMSCurrentIn_Object=MibTableColumn
psRMSCurrentIn=_PsRMSCurrentIn_Object((1,3,6,1,4,1,5591,1,4,2,1,32),_PsRMSCurrentIn_Type())
psRMSCurrentIn.setMaxAccess(_A)
if mibBuilder.loadTexts:psRMSCurrentIn.setStatus(_D)
class _PsPowerIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsPowerIn_Type.__name__=_B
_PsPowerIn_Object=MibTableColumn
psPowerIn=_PsPowerIn_Object((1,3,6,1,4,1,5591,1,4,2,1,33),_PsPowerIn_Type())
psPowerIn.setMaxAccess(_A)
if mibBuilder.loadTexts:psPowerIn.setStatus(_D)
class _PsInputVoltagePresence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lost',1),('ok',2)))
_PsInputVoltagePresence_Type.__name__=_B
_PsInputVoltagePresence_Object=MibTableColumn
psInputVoltagePresence=_PsInputVoltagePresence_Object((1,3,6,1,4,1,5591,1,4,2,1,34),_PsInputVoltagePresence_Type())
psInputVoltagePresence.setMaxAccess(_A)
if mibBuilder.loadTexts:psInputVoltagePresence.setStatus(_D)
class _PsFrequencyIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fiftyHz',1),('sixtyHz',2)))
_PsFrequencyIn_Type.__name__=_B
_PsFrequencyIn_Object=MibTableColumn
psFrequencyIn=_PsFrequencyIn_Object((1,3,6,1,4,1,5591,1,4,2,1,35),_PsFrequencyIn_Type())
psFrequencyIn.setMaxAccess(_A)
if mibBuilder.loadTexts:psFrequencyIn.setStatus(_C)
_PsStringTable_Object=MibTable
psStringTable=_PsStringTable_Object((1,3,6,1,4,1,5591,1,4,3))
if mibBuilder.loadTexts:psStringTable.setStatus(_C)
_PsStringEntry_Object=MibTableRow
psStringEntry=_PsStringEntry_Object((1,3,6,1,4,1,5591,1,4,3,1))
psStringEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:psStringEntry.setStatus(_C)
class _PsStringDeviceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PsStringDeviceAddress_Type.__name__=_B
_PsStringDeviceAddress_Object=MibTableColumn
psStringDeviceAddress=_PsStringDeviceAddress_Object((1,3,6,1,4,1,5591,1,4,3,1,1),_PsStringDeviceAddress_Type())
psStringDeviceAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:psStringDeviceAddress.setStatus(_C)
class _PsString_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_PsString_Type.__name__=_B
_PsString_Object=MibTableColumn
psString=_PsString_Object((1,3,6,1,4,1,5591,1,4,3,1,2),_PsString_Type())
psString.setMaxAccess(_A)
if mibBuilder.loadTexts:psString.setStatus(_C)
class _PsStringChargeCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsStringChargeCurrent_Type.__name__=_B
_PsStringChargeCurrent_Object=MibTableColumn
psStringChargeCurrent=_PsStringChargeCurrent_Object((1,3,6,1,4,1,5591,1,4,3,1,3),_PsStringChargeCurrent_Type())
psStringChargeCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:psStringChargeCurrent.setStatus(_D)
class _PsStringDischargeCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsStringDischargeCurrent_Type.__name__=_B
_PsStringDischargeCurrent_Object=MibTableColumn
psStringDischargeCurrent=_PsStringDischargeCurrent_Object((1,3,6,1,4,1,5591,1,4,3,1,4),_PsStringDischargeCurrent_Type())
psStringDischargeCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:psStringDischargeCurrent.setStatus(_D)
class _PsStringFloat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsStringFloat_Type.__name__=_B
_PsStringFloat_Object=MibTableColumn
psStringFloat=_PsStringFloat_Object((1,3,6,1,4,1,5591,1,4,3,1,5),_PsStringFloat_Type())
psStringFloat.setMaxAccess(_A)
if mibBuilder.loadTexts:psStringFloat.setStatus(_D)
_PsBatteryTable_Object=MibTable
psBatteryTable=_PsBatteryTable_Object((1,3,6,1,4,1,5591,1,4,4))
if mibBuilder.loadTexts:psBatteryTable.setStatus(_C)
_PsBatteryEntry_Object=MibTableRow
psBatteryEntry=_PsBatteryEntry_Object((1,3,6,1,4,1,5591,1,4,4,1))
psBatteryEntry.setIndexNames((0,_E,_N),(0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:psBatteryEntry.setStatus(_C)
class _PsBatteryDeviceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PsBatteryDeviceAddress_Type.__name__=_B
_PsBatteryDeviceAddress_Object=MibTableColumn
psBatteryDeviceAddress=_PsBatteryDeviceAddress_Object((1,3,6,1,4,1,5591,1,4,4,1,1),_PsBatteryDeviceAddress_Type())
psBatteryDeviceAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:psBatteryDeviceAddress.setStatus(_C)
class _PsBatteryString_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_PsBatteryString_Type.__name__=_B
_PsBatteryString_Object=MibTableColumn
psBatteryString=_PsBatteryString_Object((1,3,6,1,4,1,5591,1,4,4,1,2),_PsBatteryString_Type())
psBatteryString.setMaxAccess(_A)
if mibBuilder.loadTexts:psBatteryString.setStatus(_C)
class _PsBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PsBattery_Type.__name__=_B
_PsBattery_Object=MibTableColumn
psBattery=_PsBattery_Object((1,3,6,1,4,1,5591,1,4,4,1,3),_PsBattery_Type())
psBattery.setMaxAccess(_A)
if mibBuilder.loadTexts:psBattery.setStatus(_C)
class _PsBatteryVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsBatteryVoltage_Type.__name__=_B
_PsBatteryVoltage_Object=MibTableColumn
psBatteryVoltage=_PsBatteryVoltage_Object((1,3,6,1,4,1,5591,1,4,4,1,4),_PsBatteryVoltage_Type())
psBatteryVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:psBatteryVoltage.setStatus(_D)
_PsOutputTable_Object=MibTable
psOutputTable=_PsOutputTable_Object((1,3,6,1,4,1,5591,1,4,5))
if mibBuilder.loadTexts:psOutputTable.setStatus(_C)
_PsOutputEntry_Object=MibTableRow
psOutputEntry=_PsOutputEntry_Object((1,3,6,1,4,1,5591,1,4,5,1))
psOutputEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:psOutputEntry.setStatus(_C)
class _PsOutputDeviceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PsOutputDeviceAddress_Type.__name__=_B
_PsOutputDeviceAddress_Object=MibTableColumn
psOutputDeviceAddress=_PsOutputDeviceAddress_Object((1,3,6,1,4,1,5591,1,4,5,1,1),_PsOutputDeviceAddress_Type())
psOutputDeviceAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:psOutputDeviceAddress.setStatus(_C)
class _PsOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_PsOutput_Type.__name__=_B
_PsOutput_Object=MibTableColumn
psOutput=_PsOutput_Object((1,3,6,1,4,1,5591,1,4,5,1,2),_PsOutput_Type())
psOutput.setMaxAccess(_A)
if mibBuilder.loadTexts:psOutput.setStatus(_C)
class _PsOutputCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsOutputCurrent_Type.__name__=_B
_PsOutputCurrent_Object=MibTableColumn
psOutputCurrent=_PsOutputCurrent_Object((1,3,6,1,4,1,5591,1,4,5,1,3),_PsOutputCurrent_Type())
psOutputCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:psOutputCurrent.setStatus(_D)
_PsTemperatureSensorTable_Object=MibTable
psTemperatureSensorTable=_PsTemperatureSensorTable_Object((1,3,6,1,4,1,5591,1,4,6))
if mibBuilder.loadTexts:psTemperatureSensorTable.setStatus(_C)
_PsTemperatureSensorEntry_Object=MibTableRow
psTemperatureSensorEntry=_PsTemperatureSensorEntry_Object((1,3,6,1,4,1,5591,1,4,6,1))
psTemperatureSensorEntry.setIndexNames((0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:psTemperatureSensorEntry.setStatus(_C)
class _PsTempDeviceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PsTempDeviceAddress_Type.__name__=_B
_PsTempDeviceAddress_Object=MibTableColumn
psTempDeviceAddress=_PsTempDeviceAddress_Object((1,3,6,1,4,1,5591,1,4,6,1,1),_PsTempDeviceAddress_Type())
psTempDeviceAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:psTempDeviceAddress.setStatus(_C)
class _PsTemperatureSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_PsTemperatureSensor_Type.__name__=_B
_PsTemperatureSensor_Object=MibTableColumn
psTemperatureSensor=_PsTemperatureSensor_Object((1,3,6,1,4,1,5591,1,4,6,1,2),_PsTemperatureSensor_Type())
psTemperatureSensor.setMaxAccess(_A)
if mibBuilder.loadTexts:psTemperatureSensor.setStatus(_C)
class _PsTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,80))
_PsTemperature_Type.__name__=_B
_PsTemperature_Object=MibTableColumn
psTemperature=_PsTemperature_Object((1,3,6,1,4,1,5591,1,4,6,1,3),_PsTemperature_Type())
psTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:psTemperature.setStatus(_D)
mibBuilder.exportSymbols(_E,**{'psMonitored':psMonitored,'psDeviceTable':psDeviceTable,'psDeviceEntry':psDeviceEntry,_J:psDeviceAddress,'psProtocolVersion':psProtocolVersion,'psSoftwareVersion':psSoftwareVersion,'psDeviceId':psDeviceId,'psBatteries':psBatteries,'psBatteryStrings':psBatteryStrings,'psTempSensors':psTempSensors,'psOutputs':psOutputs,'psBatteryCurrentSupport':psBatteryCurrentSupport,'psFloatCurrentSupport':psFloatCurrentSupport,'psOutputVoltageSupport':psOutputVoltageSupport,'psInputVoltageSupport':psInputVoltageSupport,'psPowerSupplyTest':psPowerSupplyTest,'psMajorAlarmSupport':psMajorAlarmSupport,'psMinorAlarmSupport':psMinorAlarmSupport,'psTamperSupport':psTamperSupport,'psBatteryVoltageSupport':psBatteryVoltageSupport,'psOutputPowerSupport':psOutputPowerSupport,'psOutputFrequencySupport':psOutputFrequencySupport,'psInputCurrentSupport':psInputCurrentSupport,'psInputPowerSupport':psInputPowerSupport,'psOutputVoltage':psOutputVoltage,'psInputVoltage':psInputVoltage,'psInverterStatus':psInverterStatus,'psMajorAlarm':psMajorAlarm,'psMinorAlarm':psMinorAlarm,'psTamper':psTamper,'psTotalStringVoltage':psTotalStringVoltage,'psEquipmentControl':psEquipmentControl,'psPowerOut':psPowerOut,'psFrequencyOut':psFrequencyOut,'psRMSCurrentIn':psRMSCurrentIn,'psPowerIn':psPowerIn,'psInputVoltagePresence':psInputVoltagePresence,'psFrequencyIn':psFrequencyIn,'psStringTable':psStringTable,'psStringEntry':psStringEntry,_L:psStringDeviceAddress,_M:psString,'psStringChargeCurrent':psStringChargeCurrent,'psStringDischargeCurrent':psStringDischargeCurrent,'psStringFloat':psStringFloat,'psBatteryTable':psBatteryTable,'psBatteryEntry':psBatteryEntry,_N:psBatteryDeviceAddress,_O:psBatteryString,_P:psBattery,'psBatteryVoltage':psBatteryVoltage,'psOutputTable':psOutputTable,'psOutputEntry':psOutputEntry,_Q:psOutputDeviceAddress,_R:psOutput,'psOutputCurrent':psOutputCurrent,'psTemperatureSensorTable':psTemperatureSensorTable,'psTemperatureSensorEntry':psTemperatureSensorEntry,_S:psTempDeviceAddress,_T:psTemperatureSensor,'psTemperature':psTemperature})