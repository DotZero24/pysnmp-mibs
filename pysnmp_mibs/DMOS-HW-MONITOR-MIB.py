_H='temperatureSensorId'
_G='Integer32'
_F='not-accessible'
_E='environmentSlotId'
_D='environmentChassisId'
_C='DMOS-HW-MONITOR-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
datacomDevicesMIBs,=mibBuilder.importSymbols('DATACOM-SMI','datacomDevicesMIBs')
UnsignedPercent,=mibBuilder.importSymbols('DMOS-TC-MIB','UnsignedPercent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dmosHwMonitorMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,6,6))
if mibBuilder.loadTexts:dmosHwMonitorMIB.setRevisions(('2017-01-02 00:00',))
class EnvironmentSensorTemperature(TextualConvention,Integer32):status=_A;displayHint='d-1'
class EnvironmentSensorStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,-1,0,1,2,3)));namedValues=NamedValues(*(('fail',-2),('error',-1),('normal',0),('high',1),('low',2),('critical',3)))
_Environment_ObjectIdentity=ObjectIdentity
environment=_Environment_ObjectIdentity((1,3,6,1,4,1,3709,3,6,6,1))
_EnvironmentChassisTable_Object=MibTable
environmentChassisTable=_EnvironmentChassisTable_Object((1,3,6,1,4,1,3709,3,6,6,1,1))
if mibBuilder.loadTexts:environmentChassisTable.setStatus(_A)
_EnvironmentChassisEntry_Object=MibTableRow
environmentChassisEntry=_EnvironmentChassisEntry_Object((1,3,6,1,4,1,3709,3,6,6,1,1,1))
environmentChassisEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:environmentChassisEntry.setStatus(_A)
_EnvironmentChassisId_Type=Unsigned32
_EnvironmentChassisId_Object=MibTableColumn
environmentChassisId=_EnvironmentChassisId_Object((1,3,6,1,4,1,3709,3,6,6,1,1,1,1),_EnvironmentChassisId_Type())
environmentChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentChassisId.setStatus(_A)
_EnvironmentSlotTable_Object=MibTable
environmentSlotTable=_EnvironmentSlotTable_Object((1,3,6,1,4,1,3709,3,6,6,1,2))
if mibBuilder.loadTexts:environmentSlotTable.setStatus(_A)
_EnvironmentSlotEntry_Object=MibTableRow
environmentSlotEntry=_EnvironmentSlotEntry_Object((1,3,6,1,4,1,3709,3,6,6,1,2,1))
environmentSlotEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:environmentSlotEntry.setStatus(_A)
_EnvironmentSlotId_Type=DisplayString
_EnvironmentSlotId_Object=MibTableColumn
environmentSlotId=_EnvironmentSlotId_Object((1,3,6,1,4,1,3709,3,6,6,1,2,1,1),_EnvironmentSlotId_Type())
environmentSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentSlotId.setStatus(_A)
_TemperatureSensorTable_Object=MibTable
temperatureSensorTable=_TemperatureSensorTable_Object((1,3,6,1,4,1,3709,3,6,6,1,3))
if mibBuilder.loadTexts:temperatureSensorTable.setStatus(_A)
_TemperatureSensorEntry_Object=MibTableRow
temperatureSensorEntry=_TemperatureSensorEntry_Object((1,3,6,1,4,1,3709,3,6,6,1,3,1))
temperatureSensorEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_H))
if mibBuilder.loadTexts:temperatureSensorEntry.setStatus(_A)
_TemperatureSensorId_Type=DisplayString
_TemperatureSensorId_Object=MibTableColumn
temperatureSensorId=_TemperatureSensorId_Object((1,3,6,1,4,1,3709,3,6,6,1,3,1,1),_TemperatureSensorId_Type())
temperatureSensorId.setMaxAccess(_F)
if mibBuilder.loadTexts:temperatureSensorId.setStatus(_A)
_TemperatureSensorDescription_Type=DisplayString
_TemperatureSensorDescription_Object=MibTableColumn
temperatureSensorDescription=_TemperatureSensorDescription_Object((1,3,6,1,4,1,3709,3,6,6,1,3,1,2),_TemperatureSensorDescription_Type())
temperatureSensorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureSensorDescription.setStatus(_A)
_TemperatureSensorMaxTemperature_Type=EnvironmentSensorTemperature
_TemperatureSensorMaxTemperature_Object=MibTableColumn
temperatureSensorMaxTemperature=_TemperatureSensorMaxTemperature_Object((1,3,6,1,4,1,3709,3,6,6,1,3,1,3),_TemperatureSensorMaxTemperature_Type())
temperatureSensorMaxTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureSensorMaxTemperature.setStatus(_A)
if mibBuilder.loadTexts:temperatureSensorMaxTemperature.setUnits('C')
_TemperatureSensorMinTemperature_Type=EnvironmentSensorTemperature
_TemperatureSensorMinTemperature_Object=MibTableColumn
temperatureSensorMinTemperature=_TemperatureSensorMinTemperature_Object((1,3,6,1,4,1,3709,3,6,6,1,3,1,4),_TemperatureSensorMinTemperature_Type())
temperatureSensorMinTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureSensorMinTemperature.setStatus(_A)
if mibBuilder.loadTexts:temperatureSensorMinTemperature.setUnits('C')
_TemperatureSensorHysteresis_Type=EnvironmentSensorTemperature
_TemperatureSensorHysteresis_Object=MibTableColumn
temperatureSensorHysteresis=_TemperatureSensorHysteresis_Object((1,3,6,1,4,1,3709,3,6,6,1,3,1,5),_TemperatureSensorHysteresis_Type())
temperatureSensorHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureSensorHysteresis.setStatus(_A)
if mibBuilder.loadTexts:temperatureSensorHysteresis.setUnits('C')
_TemperatureSensorCurrentTemperature_Type=EnvironmentSensorTemperature
_TemperatureSensorCurrentTemperature_Object=MibTableColumn
temperatureSensorCurrentTemperature=_TemperatureSensorCurrentTemperature_Object((1,3,6,1,4,1,3709,3,6,6,1,3,1,6),_TemperatureSensorCurrentTemperature_Type())
temperatureSensorCurrentTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureSensorCurrentTemperature.setStatus(_A)
if mibBuilder.loadTexts:temperatureSensorCurrentTemperature.setUnits('C')
_TemperatureSensorTemperatureReadError_Type=TruthValue
_TemperatureSensorTemperatureReadError_Object=MibTableColumn
temperatureSensorTemperatureReadError=_TemperatureSensorTemperatureReadError_Object((1,3,6,1,4,1,3709,3,6,6,1,3,1,7),_TemperatureSensorTemperatureReadError_Type())
temperatureSensorTemperatureReadError.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureSensorTemperatureReadError.setStatus(_A)
_TemperatureSensorTemperatureStatus_Type=EnvironmentSensorStatus
_TemperatureSensorTemperatureStatus_Object=MibTableColumn
temperatureSensorTemperatureStatus=_TemperatureSensorTemperatureStatus_Object((1,3,6,1,4,1,3709,3,6,6,1,3,1,8),_TemperatureSensorTemperatureStatus_Type())
temperatureSensorTemperatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureSensorTemperatureStatus.setStatus(_A)
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,3709,3,6,6,1,4))
if mibBuilder.loadTexts:fanTable.setStatus(_A)
_FanEntry_Object=MibTableRow
fanEntry=_FanEntry_Object((1,3,6,1,4,1,3709,3,6,6,1,4,1))
fanEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,'fanId'))
if mibBuilder.loadTexts:fanEntry.setStatus(_A)
_FanId_Type=DisplayString
_FanId_Object=MibTableColumn
fanId=_FanId_Object((1,3,6,1,4,1,3709,3,6,6,1,4,1,1),_FanId_Type())
fanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fanId.setStatus(_A)
_FanDescription_Type=DisplayString
_FanDescription_Object=MibTableColumn
fanDescription=_FanDescription_Object((1,3,6,1,4,1,3709,3,6,6,1,4,1,2),_FanDescription_Type())
fanDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:fanDescription.setStatus(_A)
_FanControl_Type=UnsignedPercent
_FanControl_Object=MibTableColumn
fanControl=_FanControl_Object((1,3,6,1,4,1,3709,3,6,6,1,4,1,3),_FanControl_Type())
fanControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fanControl.setStatus(_A)
if mibBuilder.loadTexts:fanControl.setUnits('%')
_FanSpeed_Type=Unsigned32
_FanSpeed_Object=MibTableColumn
fanSpeed=_FanSpeed_Object((1,3,6,1,4,1,3709,3,6,6,1,4,1,4),_FanSpeed_Type())
fanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fanSpeed.setStatus(_A)
if mibBuilder.loadTexts:fanSpeed.setUnits('RPM')
_FanSpeedReadError_Type=TruthValue
_FanSpeedReadError_Object=MibTableColumn
fanSpeedReadError=_FanSpeedReadError_Object((1,3,6,1,4,1,3709,3,6,6,1,4,1,5),_FanSpeedReadError_Type())
fanSpeedReadError.setMaxAccess(_B)
if mibBuilder.loadTexts:fanSpeedReadError.setStatus(_A)
_FanSpeedStatus_Type=EnvironmentSensorStatus
_FanSpeedStatus_Object=MibTableColumn
fanSpeedStatus=_FanSpeedStatus_Object((1,3,6,1,4,1,3709,3,6,6,1,4,1,6),_FanSpeedStatus_Type())
fanSpeedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanSpeedStatus.setStatus(_A)
_PsuTable_Object=MibTable
psuTable=_PsuTable_Object((1,3,6,1,4,1,3709,3,6,6,1,5))
if mibBuilder.loadTexts:psuTable.setStatus(_A)
_PsuEntry_Object=MibTableRow
psuEntry=_PsuEntry_Object((1,3,6,1,4,1,3709,3,6,6,1,5,1))
psuEntry.setIndexNames((1,_C,'psuId'))
if mibBuilder.loadTexts:psuEntry.setStatus(_A)
_PsuId_Type=DisplayString
_PsuId_Object=MibTableColumn
psuId=_PsuId_Object((1,3,6,1,4,1,3709,3,6,6,1,5,1,1),_PsuId_Type())
psuId.setMaxAccess(_F)
if mibBuilder.loadTexts:psuId.setStatus(_A)
class _PsuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ok',0),('powerInputFailure',1),('fuseFailure',2),('error',3)))
_PsuStatus_Type.__name__=_G
_PsuStatus_Object=MibTableColumn
psuStatus=_PsuStatus_Object((1,3,6,1,4,1,3709,3,6,6,1,5,1,2),_PsuStatus_Type())
psuStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:psuStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EnvironmentSensorTemperature':EnvironmentSensorTemperature,'EnvironmentSensorStatus':EnvironmentSensorStatus,'dmosHwMonitorMIB':dmosHwMonitorMIB,'environment':environment,'environmentChassisTable':environmentChassisTable,'environmentChassisEntry':environmentChassisEntry,_D:environmentChassisId,'environmentSlotTable':environmentSlotTable,'environmentSlotEntry':environmentSlotEntry,_E:environmentSlotId,'temperatureSensorTable':temperatureSensorTable,'temperatureSensorEntry':temperatureSensorEntry,_H:temperatureSensorId,'temperatureSensorDescription':temperatureSensorDescription,'temperatureSensorMaxTemperature':temperatureSensorMaxTemperature,'temperatureSensorMinTemperature':temperatureSensorMinTemperature,'temperatureSensorHysteresis':temperatureSensorHysteresis,'temperatureSensorCurrentTemperature':temperatureSensorCurrentTemperature,'temperatureSensorTemperatureReadError':temperatureSensorTemperatureReadError,'temperatureSensorTemperatureStatus':temperatureSensorTemperatureStatus,'fanTable':fanTable,'fanEntry':fanEntry,'fanId':fanId,'fanDescription':fanDescription,'fanControl':fanControl,'fanSpeed':fanSpeed,'fanSpeedReadError':fanSpeedReadError,'fanSpeedStatus':fanSpeedStatus,'psuTable':psuTable,'psuEntry':psuEntry,'psuId':psuId,'psuStatus':psuStatus})