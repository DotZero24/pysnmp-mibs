_I='deviceSensorCode'
_H='deviceSensorValue'
_G='deviceSensorName'
_F='deviceSensorIndex'
_E='notInstalled'
_D='Integer32'
_C='BLUECOAT-SG-SENSOR-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
deviceSensorMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,1))
if mibBuilder.loadTexts:deviceSensorMIB.setRevisions(('2015-11-26 03:00','2013-07-11 03:00','2007-11-05 03:00','2002-11-06 03:00'))
class SensorUnits(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('truthvalue',2),('specialEnum',3),('volts',4),('celsius',5),('rpm',6)))
class SensorCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('ok',1),('unknown',2),(_E,3),('voltageLowWarning',4),('voltageLowCritical',5),('noPower',6),('voltageHighWarning',7),('voltageHighCritical',8),('voltageHighSevere',9),('temperatureHighWarning',10),('temperatureHighCritical',11),('temperatureHighSevere',12),('fanSlowWarning',13),('fanSlowCritical',14),('fanStopped',15)))
class ExpBase10(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-24,24))
class SensorValue(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
class SensorStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('unavailable',2),('nonoperational',3),(_E,4)))
_DeviceSensorMIBObjects_ObjectIdentity=ObjectIdentity
deviceSensorMIBObjects=_DeviceSensorMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,1,1))
_DeviceSensorValues_ObjectIdentity=ObjectIdentity
deviceSensorValues=_DeviceSensorValues_ObjectIdentity((1,3,6,1,4,1,3417,2,1,1,1))
_DeviceSensorValueTable_Object=MibTable
deviceSensorValueTable=_DeviceSensorValueTable_Object((1,3,6,1,4,1,3417,2,1,1,1,1))
if mibBuilder.loadTexts:deviceSensorValueTable.setStatus(_A)
_DeviceSensorValueEntry_Object=MibTableRow
deviceSensorValueEntry=_DeviceSensorValueEntry_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1))
deviceSensorValueEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:deviceSensorValueEntry.setStatus(_A)
class _DeviceSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DeviceSensorIndex_Type.__name__=_D
_DeviceSensorIndex_Object=MibTableColumn
deviceSensorIndex=_DeviceSensorIndex_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1,1),_DeviceSensorIndex_Type())
deviceSensorIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:deviceSensorIndex.setStatus(_A)
_DeviceSensorTrapEnabled_Type=TruthValue
_DeviceSensorTrapEnabled_Object=MibTableColumn
deviceSensorTrapEnabled=_DeviceSensorTrapEnabled_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1,2),_DeviceSensorTrapEnabled_Type())
deviceSensorTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSensorTrapEnabled.setStatus(_A)
_DeviceSensorUnits_Type=SensorUnits
_DeviceSensorUnits_Object=MibTableColumn
deviceSensorUnits=_DeviceSensorUnits_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1,3),_DeviceSensorUnits_Type())
deviceSensorUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSensorUnits.setStatus(_A)
_DeviceSensorScale_Type=ExpBase10
_DeviceSensorScale_Object=MibTableColumn
deviceSensorScale=_DeviceSensorScale_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1,4),_DeviceSensorScale_Type())
deviceSensorScale.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSensorScale.setStatus(_A)
_DeviceSensorValue_Type=SensorValue
_DeviceSensorValue_Object=MibTableColumn
deviceSensorValue=_DeviceSensorValue_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1,5),_DeviceSensorValue_Type())
deviceSensorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSensorValue.setStatus(_A)
_DeviceSensorCode_Type=SensorCode
_DeviceSensorCode_Object=MibTableColumn
deviceSensorCode=_DeviceSensorCode_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1,6),_DeviceSensorCode_Type())
deviceSensorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSensorCode.setStatus(_A)
_DeviceSensorStatus_Type=SensorStatus
_DeviceSensorStatus_Object=MibTableColumn
deviceSensorStatus=_DeviceSensorStatus_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1,7),_DeviceSensorStatus_Type())
deviceSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSensorStatus.setStatus(_A)
_DeviceSensorTimeStamp_Type=TimeStamp
_DeviceSensorTimeStamp_Object=MibTableColumn
deviceSensorTimeStamp=_DeviceSensorTimeStamp_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1,8),_DeviceSensorTimeStamp_Type())
deviceSensorTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSensorTimeStamp.setStatus(_A)
if mibBuilder.loadTexts:deviceSensorTimeStamp.setUnits('Hundredths of seconds')
_DeviceSensorName_Type=DisplayString
_DeviceSensorName_Object=MibTableColumn
deviceSensorName=_DeviceSensorName_Object((1,3,6,1,4,1,3417,2,1,1,1,1,1,9),_DeviceSensorName_Type())
deviceSensorName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSensorName.setStatus(_A)
_DeviceSensorMIBNotifications_ObjectIdentity=ObjectIdentity
deviceSensorMIBNotifications=_DeviceSensorMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,1,2))
_DeviceSensorMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
deviceSensorMIBNotificationsPrefix=_DeviceSensorMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,1,2,0))
deviceSensorTrap=NotificationType((1,3,6,1,4,1,3417,2,1,2,0,1))
deviceSensorTrap.setObjects(*((_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:deviceSensorTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'SensorUnits':SensorUnits,'SensorCode':SensorCode,'ExpBase10':ExpBase10,'SensorValue':SensorValue,'SensorStatus':SensorStatus,'deviceSensorMIB':deviceSensorMIB,'deviceSensorMIBObjects':deviceSensorMIBObjects,'deviceSensorValues':deviceSensorValues,'deviceSensorValueTable':deviceSensorValueTable,'deviceSensorValueEntry':deviceSensorValueEntry,_F:deviceSensorIndex,'deviceSensorTrapEnabled':deviceSensorTrapEnabled,'deviceSensorUnits':deviceSensorUnits,'deviceSensorScale':deviceSensorScale,_H:deviceSensorValue,_I:deviceSensorCode,'deviceSensorStatus':deviceSensorStatus,'deviceSensorTimeStamp':deviceSensorTimeStamp,_G:deviceSensorName,'deviceSensorMIBNotifications':deviceSensorMIBNotifications,'deviceSensorMIBNotificationsPrefix':deviceSensorMIBNotificationsPrefix,'deviceSensorTrap':deviceSensorTrap})