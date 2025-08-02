_K='flAtomicClockTemperatureAlarmState'
_J='flAtomicClockState'
_I='warning'
_H='normal'
_G='flAtomicClockModuleId'
_F='other'
_E='FIBROLAN-ATOMIC-CLOCK-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fibrolanGeneric,=mibBuilder.importSymbols('FIBROLAN-COMMON-MIB','fibrolanGeneric')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
flAtomicClock=ModuleIdentity((1,3,6,1,4,1,4467,1000,220))
if mibBuilder.loadTexts:flAtomicClock.setRevisions(('2015-09-15 00:00','2015-08-15 00:00'))
_FlAtomicClockNotifications_ObjectIdentity=ObjectIdentity
flAtomicClockNotifications=_FlAtomicClockNotifications_ObjectIdentity((1,3,6,1,4,1,4467,1000,220,0))
_FlAtomicClockMIBObjects_ObjectIdentity=ObjectIdentity
flAtomicClockMIBObjects=_FlAtomicClockMIBObjects_ObjectIdentity((1,3,6,1,4,1,4467,1000,220,1))
_FlAtomicClockTable_Object=MibTable
flAtomicClockTable=_FlAtomicClockTable_Object((1,3,6,1,4,1,4467,1000,220,1,10))
if mibBuilder.loadTexts:flAtomicClockTable.setStatus(_A)
_FlAtomicClockEntry_Object=MibTableRow
flAtomicClockEntry=_FlAtomicClockEntry_Object((1,3,6,1,4,1,4467,1000,220,1,10,1))
flAtomicClockEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:flAtomicClockEntry.setStatus(_A)
class _FlAtomicClockModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FlAtomicClockModuleId_Type.__name__=_C
_FlAtomicClockModuleId_Object=MibTableColumn
flAtomicClockModuleId=_FlAtomicClockModuleId_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,1),_FlAtomicClockModuleId_Type())
flAtomicClockModuleId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:flAtomicClockModuleId.setStatus(_A)
class _FlAtomicClockModuleType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlAtomicClockModuleType_Type.__name__=_D
_FlAtomicClockModuleType_Object=MibTableColumn
flAtomicClockModuleType=_FlAtomicClockModuleType_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,2),_FlAtomicClockModuleType_Type())
flAtomicClockModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockModuleType.setStatus(_A)
class _FlAtomicClockModulePartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlAtomicClockModulePartNumber_Type.__name__=_D
_FlAtomicClockModulePartNumber_Object=MibTableColumn
flAtomicClockModulePartNumber=_FlAtomicClockModulePartNumber_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,3),_FlAtomicClockModulePartNumber_Type())
flAtomicClockModulePartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockModulePartNumber.setStatus(_A)
class _FlAtomicClockModuleSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlAtomicClockModuleSerialNumber_Type.__name__=_D
_FlAtomicClockModuleSerialNumber_Object=MibTableColumn
flAtomicClockModuleSerialNumber=_FlAtomicClockModuleSerialNumber_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,4),_FlAtomicClockModuleSerialNumber_Type())
flAtomicClockModuleSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockModuleSerialNumber.setStatus(_A)
class _FlAtomicClockOscillatorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('rubidium',1),('cesium',2),(_F,99)))
_FlAtomicClockOscillatorType_Type.__name__=_C
_FlAtomicClockOscillatorType_Object=MibTableColumn
flAtomicClockOscillatorType=_FlAtomicClockOscillatorType_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,5),_FlAtomicClockOscillatorType_Type())
flAtomicClockOscillatorType.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockOscillatorType.setStatus(_A)
class _FlAtomicClockOscillatorPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlAtomicClockOscillatorPartNumber_Type.__name__=_D
_FlAtomicClockOscillatorPartNumber_Object=MibTableColumn
flAtomicClockOscillatorPartNumber=_FlAtomicClockOscillatorPartNumber_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,6),_FlAtomicClockOscillatorPartNumber_Type())
flAtomicClockOscillatorPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockOscillatorPartNumber.setStatus(_A)
class _FlAtomicClockOscillatorSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlAtomicClockOscillatorSerialNumber_Type.__name__=_D
_FlAtomicClockOscillatorSerialNumber_Object=MibTableColumn
flAtomicClockOscillatorSerialNumber=_FlAtomicClockOscillatorSerialNumber_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,7),_FlAtomicClockOscillatorSerialNumber_Type())
flAtomicClockOscillatorSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockOscillatorSerialNumber.setStatus(_A)
class _FlAtomicClockOscillatorFwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlAtomicClockOscillatorFwVersion_Type.__name__=_D
_FlAtomicClockOscillatorFwVersion_Object=MibTableColumn
flAtomicClockOscillatorFwVersion=_FlAtomicClockOscillatorFwVersion_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,8),_FlAtomicClockOscillatorFwVersion_Type())
flAtomicClockOscillatorFwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockOscillatorFwVersion.setStatus(_A)
class _FlAtomicClockState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,99)));namedValues=NamedValues(*(('unplugged',1),('warming',2),('ppsShifting',3),('shortTermSteering',4),('averaging',5),('longTermSteering',6),('holdover',7),('holdoverRecovery',8),('freeRunning',9),(_F,99)))
_FlAtomicClockState_Type.__name__=_C
_FlAtomicClockState_Object=MibTableColumn
flAtomicClockState=_FlAtomicClockState_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,9),_FlAtomicClockState_Type())
flAtomicClockState.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockState.setStatus(_A)
_FlAtomicClockStateLastChange_Type=TimeTicks
_FlAtomicClockStateLastChange_Object=MibTableColumn
flAtomicClockStateLastChange=_FlAtomicClockStateLastChange_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,10),_FlAtomicClockStateLastChange_Type())
flAtomicClockStateLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockStateLastChange.setStatus(_A)
class _FlAtomicClockTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_FlAtomicClockTemperature_Type.__name__=_C
_FlAtomicClockTemperature_Object=MibTableColumn
flAtomicClockTemperature=_FlAtomicClockTemperature_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,11),_FlAtomicClockTemperature_Type())
flAtomicClockTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockTemperature.setStatus(_A)
class _FlAtomicClockTemperatureAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*((_H,1),(_I,2),('error',3),(_F,99)))
_FlAtomicClockTemperatureAlarmState_Type.__name__=_C
_FlAtomicClockTemperatureAlarmState_Object=MibTableColumn
flAtomicClockTemperatureAlarmState=_FlAtomicClockTemperatureAlarmState_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,12),_FlAtomicClockTemperatureAlarmState_Type())
flAtomicClockTemperatureAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockTemperatureAlarmState.setStatus(_A)
class _FlAtomicClockCellHeaterCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3000))
_FlAtomicClockCellHeaterCurrent_Type.__name__=_C
_FlAtomicClockCellHeaterCurrent_Object=MibTableColumn
flAtomicClockCellHeaterCurrent=_FlAtomicClockCellHeaterCurrent_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,13),_FlAtomicClockCellHeaterCurrent_Type())
flAtomicClockCellHeaterCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockCellHeaterCurrent.setStatus(_A)
class _FlAtomicClockCellHeaterCurrentAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*((_H,1),(_I,2),('error',3),(_F,99)))
_FlAtomicClockCellHeaterCurrentAlarmState_Type.__name__=_C
_FlAtomicClockCellHeaterCurrentAlarmState_Object=MibTableColumn
flAtomicClockCellHeaterCurrentAlarmState=_FlAtomicClockCellHeaterCurrentAlarmState_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,14),_FlAtomicClockCellHeaterCurrentAlarmState_Type())
flAtomicClockCellHeaterCurrentAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockCellHeaterCurrentAlarmState.setStatus(_A)
class _FlAtomicClockAdjustPp15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10000000,10000000))
_FlAtomicClockAdjustPp15_Type.__name__=_C
_FlAtomicClockAdjustPp15_Object=MibTableColumn
flAtomicClockAdjustPp15=_FlAtomicClockAdjustPp15_Object((1,3,6,1,4,1,4467,1000,220,1,10,1,15),_FlAtomicClockAdjustPp15_Type())
flAtomicClockAdjustPp15.setMaxAccess(_B)
if mibBuilder.loadTexts:flAtomicClockAdjustPp15.setStatus(_A)
flAtomicClockStateChange=NotificationType((1,3,6,1,4,1,4467,1000,220,0,10))
flAtomicClockStateChange.setObjects((_E,_J))
if mibBuilder.loadTexts:flAtomicClockStateChange.setStatus(_A)
flAtomicClockTemperatureAlarmStateChange=NotificationType((1,3,6,1,4,1,4467,1000,220,0,20))
flAtomicClockTemperatureAlarmStateChange.setObjects((_E,_K))
if mibBuilder.loadTexts:flAtomicClockTemperatureAlarmStateChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'flAtomicClock':flAtomicClock,'flAtomicClockNotifications':flAtomicClockNotifications,'flAtomicClockStateChange':flAtomicClockStateChange,'flAtomicClockTemperatureAlarmStateChange':flAtomicClockTemperatureAlarmStateChange,'flAtomicClockMIBObjects':flAtomicClockMIBObjects,'flAtomicClockTable':flAtomicClockTable,'flAtomicClockEntry':flAtomicClockEntry,_G:flAtomicClockModuleId,'flAtomicClockModuleType':flAtomicClockModuleType,'flAtomicClockModulePartNumber':flAtomicClockModulePartNumber,'flAtomicClockModuleSerialNumber':flAtomicClockModuleSerialNumber,'flAtomicClockOscillatorType':flAtomicClockOscillatorType,'flAtomicClockOscillatorPartNumber':flAtomicClockOscillatorPartNumber,'flAtomicClockOscillatorSerialNumber':flAtomicClockOscillatorSerialNumber,'flAtomicClockOscillatorFwVersion':flAtomicClockOscillatorFwVersion,_J:flAtomicClockState,'flAtomicClockStateLastChange':flAtomicClockStateLastChange,'flAtomicClockTemperature':flAtomicClockTemperature,_K:flAtomicClockTemperatureAlarmState,'flAtomicClockCellHeaterCurrent':flAtomicClockCellHeaterCurrent,'flAtomicClockCellHeaterCurrentAlarmState':flAtomicClockCellHeaterCurrentAlarmState,'flAtomicClockAdjustPp15':flAtomicClockAdjustPp15})