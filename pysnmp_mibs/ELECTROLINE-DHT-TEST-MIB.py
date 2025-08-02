_K='passed'
_J='failed'
_I='controlPortId'
_H='statusPortId'
_G='analogCalibrationPortId'
_F='analogPortId'
_E='ELECTROLINE-DHT-TEST-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dhtPrivate,=mibBuilder.importSymbols('ELECTROLINE-DHT-ROOT-MIB','dhtPrivate')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
_DhtTest_ObjectIdentity=ObjectIdentity
dhtTest=_DhtTest_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,4,1))
_DhtAnalogPorts_ObjectIdentity=ObjectIdentity
dhtAnalogPorts=_DhtAnalogPorts_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,4,1,1))
_CurrentAnalogValueTable_Object=MibTable
currentAnalogValueTable=_CurrentAnalogValueTable_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,1))
if mibBuilder.loadTexts:currentAnalogValueTable.setStatus(_A)
_CurrentAnalogValueEntry_Object=MibTableRow
currentAnalogValueEntry=_CurrentAnalogValueEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,1,1))
currentAnalogValueEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:currentAnalogValueEntry.setStatus(_A)
_AnalogPortId_Type=Integer32
_AnalogPortId_Object=MibTableColumn
analogPortId=_AnalogPortId_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,1,1,1),_AnalogPortId_Type())
analogPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:analogPortId.setStatus(_A)
_AnalogValue_Type=Integer32
_AnalogValue_Object=MibTableColumn
analogValue=_AnalogValue_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,1,1,2),_AnalogValue_Type())
analogValue.setMaxAccess(_B)
if mibBuilder.loadTexts:analogValue.setStatus(_A)
_AnalogPortIdDesc_Type=OctetString
_AnalogPortIdDesc_Object=MibTableColumn
analogPortIdDesc=_AnalogPortIdDesc_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,1,1,3),_AnalogPortIdDesc_Type())
analogPortIdDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:analogPortIdDesc.setStatus(_A)
_AnalogCalibrationValue_Type=Integer32
_AnalogCalibrationValue_Object=MibScalar
analogCalibrationValue=_AnalogCalibrationValue_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,2),_AnalogCalibrationValue_Type())
analogCalibrationValue.setMaxAccess(_C)
if mibBuilder.loadTexts:analogCalibrationValue.setStatus(_A)
_AnalogPortToCalibrate_Type=Integer32
_AnalogPortToCalibrate_Object=MibScalar
analogPortToCalibrate=_AnalogPortToCalibrate_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,3),_AnalogPortToCalibrate_Type())
analogPortToCalibrate.setMaxAccess(_C)
if mibBuilder.loadTexts:analogPortToCalibrate.setStatus(_A)
class _AnalogCalibrationCommit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AnalogCalibrationCommit_Type.__name__=_D
_AnalogCalibrationCommit_Object=MibScalar
analogCalibrationCommit=_AnalogCalibrationCommit_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,4),_AnalogCalibrationCommit_Type())
analogCalibrationCommit.setMaxAccess(_C)
if mibBuilder.loadTexts:analogCalibrationCommit.setStatus(_A)
class _AnalogCalibrationSetDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AnalogCalibrationSetDefault_Type.__name__=_D
_AnalogCalibrationSetDefault_Object=MibScalar
analogCalibrationSetDefault=_AnalogCalibrationSetDefault_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,5),_AnalogCalibrationSetDefault_Type())
analogCalibrationSetDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:analogCalibrationSetDefault.setStatus(_A)
_CurrentCalibrationValueTable_Object=MibTable
currentCalibrationValueTable=_CurrentCalibrationValueTable_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,6))
if mibBuilder.loadTexts:currentCalibrationValueTable.setStatus(_A)
_CurrentCalibrationValueEntry_Object=MibTableRow
currentCalibrationValueEntry=_CurrentCalibrationValueEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,6,1))
currentCalibrationValueEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:currentCalibrationValueEntry.setStatus(_A)
_AnalogCalibrationPortId_Type=Integer32
_AnalogCalibrationPortId_Object=MibTableColumn
analogCalibrationPortId=_AnalogCalibrationPortId_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,6,1,1),_AnalogCalibrationPortId_Type())
analogCalibrationPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:analogCalibrationPortId.setStatus(_A)
_RawValue_Type=Integer32
_RawValue_Object=MibTableColumn
rawValue=_RawValue_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,6,1,2),_RawValue_Type())
rawValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rawValue.setStatus(_A)
_CalibratedValue_Type=Integer32
_CalibratedValue_Object=MibTableColumn
calibratedValue=_CalibratedValue_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,6,1,3),_CalibratedValue_Type())
calibratedValue.setMaxAccess(_B)
if mibBuilder.loadTexts:calibratedValue.setStatus(_A)
_CalibratedPortIdDesc_Type=OctetString
_CalibratedPortIdDesc_Object=MibTableColumn
calibratedPortIdDesc=_CalibratedPortIdDesc_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,1,6,1,4),_CalibratedPortIdDesc_Type())
calibratedPortIdDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:calibratedPortIdDesc.setStatus(_A)
_DhtDigitalPorts_ObjectIdentity=ObjectIdentity
dhtDigitalPorts=_DhtDigitalPorts_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,4,1,2))
_CurrentDigitalStatusTable_Object=MibTable
currentDigitalStatusTable=_CurrentDigitalStatusTable_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,1))
if mibBuilder.loadTexts:currentDigitalStatusTable.setStatus(_A)
_CurrentDigitalStatusEntry_Object=MibTableRow
currentDigitalStatusEntry=_CurrentDigitalStatusEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,1,1))
currentDigitalStatusEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:currentDigitalStatusEntry.setStatus(_A)
_StatusPortId_Type=Integer32
_StatusPortId_Object=MibTableColumn
statusPortId=_StatusPortId_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,1,1,1),_StatusPortId_Type())
statusPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:statusPortId.setStatus(_A)
_StatusValue_Type=Integer32
_StatusValue_Object=MibTableColumn
statusValue=_StatusValue_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,1,1,2),_StatusValue_Type())
statusValue.setMaxAccess(_B)
if mibBuilder.loadTexts:statusValue.setStatus(_A)
_StatusPortIdDesc_Type=OctetString
_StatusPortIdDesc_Object=MibTableColumn
statusPortIdDesc=_StatusPortIdDesc_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,1,1,3),_StatusPortIdDesc_Type())
statusPortIdDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:statusPortIdDesc.setStatus(_A)
_CurrentDigitalControlTable_Object=MibTable
currentDigitalControlTable=_CurrentDigitalControlTable_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,2))
if mibBuilder.loadTexts:currentDigitalControlTable.setStatus(_A)
_CurrentDigitalControlEntry_Object=MibTableRow
currentDigitalControlEntry=_CurrentDigitalControlEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,2,1))
currentDigitalControlEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:currentDigitalControlEntry.setStatus(_A)
_ControlPortId_Type=Integer32
_ControlPortId_Object=MibTableColumn
controlPortId=_ControlPortId_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,2,1,1),_ControlPortId_Type())
controlPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:controlPortId.setStatus(_A)
_ControlValue_Type=Integer32
_ControlValue_Object=MibTableColumn
controlValue=_ControlValue_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,2,1,2),_ControlValue_Type())
controlValue.setMaxAccess(_C)
if mibBuilder.loadTexts:controlValue.setStatus(_A)
_ControlPortIdDesc_Type=OctetString
_ControlPortIdDesc_Object=MibTableColumn
controlPortIdDesc=_ControlPortIdDesc_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,2,2,1,3),_ControlPortIdDesc_Type())
controlPortIdDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:controlPortIdDesc.setStatus(_A)
_DhtMicroControllers_ObjectIdentity=ObjectIdentity
dhtMicroControllers=_DhtMicroControllers_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,4,1,3))
_UsmFirmwareVersion_Type=OctetString
_UsmFirmwareVersion_Object=MibScalar
usmFirmwareVersion=_UsmFirmwareVersion_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,3,1),_UsmFirmwareVersion_Type())
usmFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:usmFirmwareVersion.setStatus(_A)
_BatFirmwareVersion_Type=OctetString
_BatFirmwareVersion_Object=MibScalar
batFirmwareVersion=_BatFirmwareVersion_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,3,2),_BatFirmwareVersion_Type())
batFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:batFirmwareVersion.setStatus(_A)
class _Reset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Reset_Type.__name__=_D
_Reset_Object=MibScalar
reset=_Reset_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,3,3),_Reset_Type())
reset.setMaxAccess(_C)
if mibBuilder.loadTexts:reset.setStatus(_A)
_WakeUpVoltage_Type=Integer32
_WakeUpVoltage_Object=MibScalar
wakeUpVoltage=_WakeUpVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,3,4),_WakeUpVoltage_Type())
wakeUpVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:wakeUpVoltage.setStatus(_A)
_WakeUpPortId_Type=Integer32
_WakeUpPortId_Object=MibScalar
wakeUpPortId=_WakeUpPortId_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,3,5),_WakeUpPortId_Type())
wakeUpPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wakeUpPortId.setStatus(_A)
_DhtExternalDevices_ObjectIdentity=ObjectIdentity
dhtExternalDevices=_DhtExternalDevices_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,4,1,4))
class _SpiExternalTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SpiExternalTest_Type.__name__=_D
_SpiExternalTest_Object=MibScalar
spiExternalTest=_SpiExternalTest_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,4,1),_SpiExternalTest_Type())
spiExternalTest.setMaxAccess(_B)
if mibBuilder.loadTexts:spiExternalTest.setStatus(_A)
class _CprTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_CprTest_Type.__name__=_D
_CprTest_Object=MibScalar
cprTest=_CprTest_Object((1,3,6,1,4,1,5802,1,3,1,2,4,1,4,2),_CprTest_Type())
cprTest.setMaxAccess(_B)
if mibBuilder.loadTexts:cprTest.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'dhtTest':dhtTest,'dhtAnalogPorts':dhtAnalogPorts,'currentAnalogValueTable':currentAnalogValueTable,'currentAnalogValueEntry':currentAnalogValueEntry,_F:analogPortId,'analogValue':analogValue,'analogPortIdDesc':analogPortIdDesc,'analogCalibrationValue':analogCalibrationValue,'analogPortToCalibrate':analogPortToCalibrate,'analogCalibrationCommit':analogCalibrationCommit,'analogCalibrationSetDefault':analogCalibrationSetDefault,'currentCalibrationValueTable':currentCalibrationValueTable,'currentCalibrationValueEntry':currentCalibrationValueEntry,_G:analogCalibrationPortId,'rawValue':rawValue,'calibratedValue':calibratedValue,'calibratedPortIdDesc':calibratedPortIdDesc,'dhtDigitalPorts':dhtDigitalPorts,'currentDigitalStatusTable':currentDigitalStatusTable,'currentDigitalStatusEntry':currentDigitalStatusEntry,_H:statusPortId,'statusValue':statusValue,'statusPortIdDesc':statusPortIdDesc,'currentDigitalControlTable':currentDigitalControlTable,'currentDigitalControlEntry':currentDigitalControlEntry,_I:controlPortId,'controlValue':controlValue,'controlPortIdDesc':controlPortIdDesc,'dhtMicroControllers':dhtMicroControllers,'usmFirmwareVersion':usmFirmwareVersion,'batFirmwareVersion':batFirmwareVersion,'reset':reset,'wakeUpVoltage':wakeUpVoltage,'wakeUpPortId':wakeUpPortId,'dhtExternalDevices':dhtExternalDevices,'spiExternalTest':spiExternalTest,'cprTest':cprTest})