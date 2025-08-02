_K='unitId'
_J='SIAE-UNIT-MIB'
_I='Integer32'
_H='AutonomousType'
_G='read-write'
_F='read-create'
_E='DisplayString'
_D='AlarmStatus'
_C='AlarmSeverityCode'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_C,_D)
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
unitTypeUnequipped,=mibBuilder.importSymbols('SIAE-UNITYPE-MIB','unitTypeUnequipped')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,_E,'PhysAddress','RowStatus','TextualConvention')
unit=ModuleIdentity((1,3,6,1,4,1,3373,1103,6))
if mibBuilder.loadTexts:unit.setRevisions(('2014-02-03 00:00','2013-04-16 00:00'))
class _UnitMibVersion_Type(Integer32):defaultValue=1
_UnitMibVersion_Type.__name__=_I
_UnitMibVersion_Object=MibScalar
unitMibVersion=_UnitMibVersion_Object((1,3,6,1,4,1,3373,1103,6,1),_UnitMibVersion_Type())
unitMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:unitMibVersion.setStatus(_A)
_UnitTable_Object=MibTable
unitTable=_UnitTable_Object((1,3,6,1,4,1,3373,1103,6,2))
if mibBuilder.loadTexts:unitTable.setStatus(_A)
_UnitRecord_Object=MibTableRow
unitRecord=_UnitRecord_Object((1,3,6,1,4,1,3373,1103,6,2,1))
unitRecord.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:unitRecord.setStatus(_A)
_UnitId_Type=Integer32
_UnitId_Object=MibTableColumn
unitId=_UnitId_Object((1,3,6,1,4,1,3373,1103,6,2,1,1),_UnitId_Type())
unitId.setMaxAccess(_B)
if mibBuilder.loadTexts:unitId.setStatus(_A)
class _UnitExpectedType_Type(AutonomousType):defaultValue=1,3,6,1,4,1,3373,1103,6,3,1
_UnitExpectedType_Type.__name__=_H
_UnitExpectedType_Object=MibTableColumn
unitExpectedType=_UnitExpectedType_Object((1,3,6,1,4,1,3373,1103,6,2,1,2),_UnitExpectedType_Type())
unitExpectedType.setMaxAccess(_F)
if mibBuilder.loadTexts:unitExpectedType.setStatus(_A)
class _UnitActualType_Type(AutonomousType):defaultValue=1,3,6,1,4,1,3373,1103,6,3,1
_UnitActualType_Type.__name__=_H
_UnitActualType_Object=MibTableColumn
unitActualType=_UnitActualType_Object((1,3,6,1,4,1,3373,1103,6,2,1,3),_UnitActualType_Type())
unitActualType.setMaxAccess(_B)
if mibBuilder.loadTexts:unitActualType.setStatus(_A)
class _UnitLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_UnitLabel_Type.__name__=_E
_UnitLabel_Object=MibTableColumn
unitLabel=_UnitLabel_Object((1,3,6,1,4,1,3373,1103,6,2,1,4),_UnitLabel_Type())
unitLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:unitLabel.setStatus(_A)
class _UnitFailAlarm_Type(AlarmStatus):defaultValue=5
_UnitFailAlarm_Type.__name__=_D
_UnitFailAlarm_Object=MibTableColumn
unitFailAlarm=_UnitFailAlarm_Object((1,3,6,1,4,1,3373,1103,6,2,1,5),_UnitFailAlarm_Type())
unitFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:unitFailAlarm.setStatus(_A)
class _UnitMissingAlarm_Type(AlarmStatus):defaultValue=5
_UnitMissingAlarm_Type.__name__=_D
_UnitMissingAlarm_Object=MibTableColumn
unitMissingAlarm=_UnitMissingAlarm_Object((1,3,6,1,4,1,3373,1103,6,2,1,6),_UnitMissingAlarm_Type())
unitMissingAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:unitMissingAlarm.setStatus(_A)
class _UnitNotRespondingAlarm_Type(AlarmStatus):defaultValue=5
_UnitNotRespondingAlarm_Type.__name__=_D
_UnitNotRespondingAlarm_Object=MibTableColumn
unitNotRespondingAlarm=_UnitNotRespondingAlarm_Object((1,3,6,1,4,1,3373,1103,6,2,1,7),_UnitNotRespondingAlarm_Type())
unitNotRespondingAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:unitNotRespondingAlarm.setStatus(_A)
class _UnitHwMismatchAlarm_Type(AlarmStatus):defaultValue=5
_UnitHwMismatchAlarm_Type.__name__=_D
_UnitHwMismatchAlarm_Object=MibTableColumn
unitHwMismatchAlarm=_UnitHwMismatchAlarm_Object((1,3,6,1,4,1,3373,1103,6,2,1,8),_UnitHwMismatchAlarm_Type())
unitHwMismatchAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:unitHwMismatchAlarm.setStatus(_A)
class _UnitSwMismatchAlarm_Type(AlarmStatus):defaultValue=5
_UnitSwMismatchAlarm_Type.__name__=_D
_UnitSwMismatchAlarm_Object=MibTableColumn
unitSwMismatchAlarm=_UnitSwMismatchAlarm_Object((1,3,6,1,4,1,3373,1103,6,2,1,9),_UnitSwMismatchAlarm_Type())
unitSwMismatchAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:unitSwMismatchAlarm.setStatus(_A)
class _UnitHwEdition_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_UnitHwEdition_Type.__name__=_E
_UnitHwEdition_Object=MibTableColumn
unitHwEdition=_UnitHwEdition_Object((1,3,6,1,4,1,3373,1103,6,2,1,10),_UnitHwEdition_Type())
unitHwEdition.setMaxAccess(_F)
if mibBuilder.loadTexts:unitHwEdition.setStatus(_A)
class _UnitPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_UnitPartNumber_Type.__name__=_E
_UnitPartNumber_Object=MibTableColumn
unitPartNumber=_UnitPartNumber_Object((1,3,6,1,4,1,3373,1103,6,2,1,11),_UnitPartNumber_Type())
unitPartNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:unitPartNumber.setStatus(_A)
class _UnitParentPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_UnitParentPartNumber_Type.__name__=_E
_UnitParentPartNumber_Object=MibTableColumn
unitParentPartNumber=_UnitParentPartNumber_Object((1,3,6,1,4,1,3373,1103,6,2,1,12),_UnitParentPartNumber_Type())
unitParentPartNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:unitParentPartNumber.setStatus(_A)
class _UnitParentSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_UnitParentSerialNumber_Type.__name__=_E
_UnitParentSerialNumber_Object=MibTableColumn
unitParentSerialNumber=_UnitParentSerialNumber_Object((1,3,6,1,4,1,3373,1103,6,2,1,13),_UnitParentSerialNumber_Type())
unitParentSerialNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:unitParentSerialNumber.setStatus(_A)
_UnitRowStatus_Type=RowStatus
_UnitRowStatus_Object=MibTableColumn
unitRowStatus=_UnitRowStatus_Object((1,3,6,1,4,1,3373,1103,6,2,1,14),_UnitRowStatus_Type())
unitRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:unitRowStatus.setStatus(_A)
class _UnitFailAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_UnitFailAlarmSeverityCode_Type.__name__=_C
_UnitFailAlarmSeverityCode_Object=MibScalar
unitFailAlarmSeverityCode=_UnitFailAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,6,4),_UnitFailAlarmSeverityCode_Type())
unitFailAlarmSeverityCode.setMaxAccess(_G)
if mibBuilder.loadTexts:unitFailAlarmSeverityCode.setStatus(_A)
class _UnitMissingAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_UnitMissingAlarmSeverityCode_Type.__name__=_C
_UnitMissingAlarmSeverityCode_Object=MibScalar
unitMissingAlarmSeverityCode=_UnitMissingAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,6,5),_UnitMissingAlarmSeverityCode_Type())
unitMissingAlarmSeverityCode.setMaxAccess(_G)
if mibBuilder.loadTexts:unitMissingAlarmSeverityCode.setStatus(_A)
class _UnitNotRespondingAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_UnitNotRespondingAlarmSeverityCode_Type.__name__=_C
_UnitNotRespondingAlarmSeverityCode_Object=MibScalar
unitNotRespondingAlarmSeverityCode=_UnitNotRespondingAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,6,6),_UnitNotRespondingAlarmSeverityCode_Type())
unitNotRespondingAlarmSeverityCode.setMaxAccess(_G)
if mibBuilder.loadTexts:unitNotRespondingAlarmSeverityCode.setStatus(_A)
class _UnitHwMismatchAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_UnitHwMismatchAlarmSeverityCode_Type.__name__=_C
_UnitHwMismatchAlarmSeverityCode_Object=MibScalar
unitHwMismatchAlarmSeverityCode=_UnitHwMismatchAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,6,7),_UnitHwMismatchAlarmSeverityCode_Type())
unitHwMismatchAlarmSeverityCode.setMaxAccess(_G)
if mibBuilder.loadTexts:unitHwMismatchAlarmSeverityCode.setStatus(_A)
class _UnitSwMismatchAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_UnitSwMismatchAlarmSeverityCode_Type.__name__=_C
_UnitSwMismatchAlarmSeverityCode_Object=MibScalar
unitSwMismatchAlarmSeverityCode=_UnitSwMismatchAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,6,8),_UnitSwMismatchAlarmSeverityCode_Type())
unitSwMismatchAlarmSeverityCode.setMaxAccess(_G)
if mibBuilder.loadTexts:unitSwMismatchAlarmSeverityCode.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'unit':unit,'unitMibVersion':unitMibVersion,'unitTable':unitTable,'unitRecord':unitRecord,_K:unitId,'unitExpectedType':unitExpectedType,'unitActualType':unitActualType,'unitLabel':unitLabel,'unitFailAlarm':unitFailAlarm,'unitMissingAlarm':unitMissingAlarm,'unitNotRespondingAlarm':unitNotRespondingAlarm,'unitHwMismatchAlarm':unitHwMismatchAlarm,'unitSwMismatchAlarm':unitSwMismatchAlarm,'unitHwEdition':unitHwEdition,'unitPartNumber':unitPartNumber,'unitParentPartNumber':unitParentPartNumber,'unitParentSerialNumber':unitParentSerialNumber,'unitRowStatus':unitRowStatus,'unitFailAlarmSeverityCode':unitFailAlarmSeverityCode,'unitMissingAlarmSeverityCode':unitMissingAlarmSeverityCode,'unitNotRespondingAlarmSeverityCode':unitNotRespondingAlarmSeverityCode,'unitHwMismatchAlarmSeverityCode':unitHwMismatchAlarmSeverityCode,'unitSwMismatchAlarmSeverityCode':unitSwMismatchAlarmSeverityCode})