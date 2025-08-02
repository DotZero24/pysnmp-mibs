_K='hysteresis'
_J='alarmed'
_I='cleared'
_H='DisplayString'
_G='sensorTempIndex'
_F='SIAE-SENSOR-TEMP-MIB'
_E='AlarmSeverityCode'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_E,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
sensorTemp=ModuleIdentity((1,3,6,1,4,1,3373,1103,77))
if mibBuilder.loadTexts:sensorTemp.setRevisions(('2016-05-03 00:00','2014-03-31 00:00'))
_SensorTempMibVersion_Type=Integer32
_SensorTempMibVersion_Object=MibScalar
sensorTempMibVersion=_SensorTempMibVersion_Object((1,3,6,1,4,1,3373,1103,77,1),_SensorTempMibVersion_Type())
sensorTempMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempMibVersion.setStatus(_A)
_SensorTempTable_Object=MibTable
sensorTempTable=_SensorTempTable_Object((1,3,6,1,4,1,3373,1103,77,2))
if mibBuilder.loadTexts:sensorTempTable.setStatus(_A)
_SensorTempEntry_Object=MibTableRow
sensorTempEntry=_SensorTempEntry_Object((1,3,6,1,4,1,3373,1103,77,2,1))
sensorTempEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sensorTempEntry.setStatus(_A)
_SensorTempIndex_Type=Integer32
_SensorTempIndex_Object=MibTableColumn
sensorTempIndex=_SensorTempIndex_Object((1,3,6,1,4,1,3373,1103,77,2,1,1),_SensorTempIndex_Type())
sensorTempIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempIndex.setStatus(_A)
_SensorTempValue_Type=Integer32
_SensorTempValue_Object=MibTableColumn
sensorTempValue=_SensorTempValue_Object((1,3,6,1,4,1,3373,1103,77,2,1,2),_SensorTempValue_Type())
sensorTempValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempValue.setStatus(_A)
_SensorTempThreshold1_Type=Integer32
_SensorTempThreshold1_Object=MibTableColumn
sensorTempThreshold1=_SensorTempThreshold1_Object((1,3,6,1,4,1,3373,1103,77,2,1,3),_SensorTempThreshold1_Type())
sensorTempThreshold1.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempThreshold1.setStatus(_A)
_SensorTempThreshold2_Type=Integer32
_SensorTempThreshold2_Object=MibTableColumn
sensorTempThreshold2=_SensorTempThreshold2_Object((1,3,6,1,4,1,3373,1103,77,2,1,4),_SensorTempThreshold2_Type())
sensorTempThreshold2.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempThreshold2.setStatus(_A)
_SensorTempHysteresis1_Type=Integer32
_SensorTempHysteresis1_Object=MibTableColumn
sensorTempHysteresis1=_SensorTempHysteresis1_Object((1,3,6,1,4,1,3373,1103,77,2,1,5),_SensorTempHysteresis1_Type())
sensorTempHysteresis1.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempHysteresis1.setStatus(_A)
_SensorTempHysteresis2_Type=Integer32
_SensorTempHysteresis2_Object=MibTableColumn
sensorTempHysteresis2=_SensorTempHysteresis2_Object((1,3,6,1,4,1,3373,1103,77,2,1,6),_SensorTempHysteresis2_Type())
sensorTempHysteresis2.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempHysteresis2.setStatus(_A)
class _SensorTempStatus1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_SensorTempStatus1_Type.__name__=_C
_SensorTempStatus1_Object=MibTableColumn
sensorTempStatus1=_SensorTempStatus1_Object((1,3,6,1,4,1,3373,1103,77,2,1,7),_SensorTempStatus1_Type())
sensorTempStatus1.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempStatus1.setStatus(_A)
class _SensorTempStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_SensorTempStatus2_Type.__name__=_C
_SensorTempStatus2_Object=MibTableColumn
sensorTempStatus2=_SensorTempStatus2_Object((1,3,6,1,4,1,3373,1103,77,2,1,8),_SensorTempStatus2_Type())
sensorTempStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempStatus2.setStatus(_A)
class _SensorTempLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SensorTempLabel_Type.__name__=_H
_SensorTempLabel_Object=MibTableColumn
sensorTempLabel=_SensorTempLabel_Object((1,3,6,1,4,1,3373,1103,77,2,1,9),_SensorTempLabel_Type())
sensorTempLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempLabel.setStatus(_A)
_SensorTempAlarmThreshold1_Type=AlarmStatus
_SensorTempAlarmThreshold1_Object=MibScalar
sensorTempAlarmThreshold1=_SensorTempAlarmThreshold1_Object((1,3,6,1,4,1,3373,1103,77,3),_SensorTempAlarmThreshold1_Type())
sensorTempAlarmThreshold1.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempAlarmThreshold1.setStatus(_A)
_SensorTempAlarmThreshold2_Type=AlarmStatus
_SensorTempAlarmThreshold2_Object=MibScalar
sensorTempAlarmThreshold2=_SensorTempAlarmThreshold2_Object((1,3,6,1,4,1,3373,1103,77,4),_SensorTempAlarmThreshold2_Type())
sensorTempAlarmThreshold2.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempAlarmThreshold2.setStatus(_A)
class _SensorTempAlarmThreshold1Severity_Type(AlarmSeverityCode):defaultValue=3
_SensorTempAlarmThreshold1Severity_Type.__name__=_E
_SensorTempAlarmThreshold1Severity_Object=MibScalar
sensorTempAlarmThreshold1Severity=_SensorTempAlarmThreshold1Severity_Object((1,3,6,1,4,1,3373,1103,77,5),_SensorTempAlarmThreshold1Severity_Type())
sensorTempAlarmThreshold1Severity.setMaxAccess(_D)
if mibBuilder.loadTexts:sensorTempAlarmThreshold1Severity.setStatus(_A)
class _SensorTempAlarmThreshold2Severity_Type(AlarmSeverityCode):defaultValue=6
_SensorTempAlarmThreshold2Severity_Type.__name__=_E
_SensorTempAlarmThreshold2Severity_Object=MibScalar
sensorTempAlarmThreshold2Severity=_SensorTempAlarmThreshold2Severity_Object((1,3,6,1,4,1,3373,1103,77,6),_SensorTempAlarmThreshold2Severity_Type())
sensorTempAlarmThreshold2Severity.setMaxAccess(_D)
if mibBuilder.loadTexts:sensorTempAlarmThreshold2Severity.setStatus(_A)
_SensorTempMonitorTable_Object=MibTable
sensorTempMonitorTable=_SensorTempMonitorTable_Object((1,3,6,1,4,1,3373,1103,77,7))
if mibBuilder.loadTexts:sensorTempMonitorTable.setStatus(_A)
_SensorTempMonitorEntry_Object=MibTableRow
sensorTempMonitorEntry=_SensorTempMonitorEntry_Object((1,3,6,1,4,1,3373,1103,77,7,1))
sensorTempMonitorEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sensorTempMonitorEntry.setStatus(_A)
class _SensorTempMonitorAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SensorTempMonitorAdminStatus_Type.__name__=_C
_SensorTempMonitorAdminStatus_Object=MibTableColumn
sensorTempMonitorAdminStatus=_SensorTempMonitorAdminStatus_Object((1,3,6,1,4,1,3373,1103,77,7,1,1),_SensorTempMonitorAdminStatus_Type())
sensorTempMonitorAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sensorTempMonitorAdminStatus.setStatus(_A)
class _SensorTempMonitorOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SensorTempMonitorOperStatus_Type.__name__=_C
_SensorTempMonitorOperStatus_Object=MibTableColumn
sensorTempMonitorOperStatus=_SensorTempMonitorOperStatus_Object((1,3,6,1,4,1,3373,1103,77,7,1,2),_SensorTempMonitorOperStatus_Type())
sensorTempMonitorOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempMonitorOperStatus.setStatus(_A)
_SensorTempMonitorMinTemp_Type=Integer32
_SensorTempMonitorMinTemp_Object=MibTableColumn
sensorTempMonitorMinTemp=_SensorTempMonitorMinTemp_Object((1,3,6,1,4,1,3373,1103,77,7,1,3),_SensorTempMonitorMinTemp_Type())
sensorTempMonitorMinTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempMonitorMinTemp.setStatus(_A)
_SensorTempMonitorMaxTemp_Type=Integer32
_SensorTempMonitorMaxTemp_Object=MibTableColumn
sensorTempMonitorMaxTemp=_SensorTempMonitorMaxTemp_Object((1,3,6,1,4,1,3373,1103,77,7,1,4),_SensorTempMonitorMaxTemp_Type())
sensorTempMonitorMaxTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempMonitorMaxTemp.setStatus(_A)
_SensorTempMonitorAverageTemp_Type=Integer32
_SensorTempMonitorAverageTemp_Object=MibTableColumn
sensorTempMonitorAverageTemp=_SensorTempMonitorAverageTemp_Object((1,3,6,1,4,1,3373,1103,77,7,1,5),_SensorTempMonitorAverageTemp_Type())
sensorTempMonitorAverageTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTempMonitorAverageTemp.setStatus(_A)
class _SensorTempMonitorSystemControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_SensorTempMonitorSystemControl_Type.__name__=_C
_SensorTempMonitorSystemControl_Object=MibScalar
sensorTempMonitorSystemControl=_SensorTempMonitorSystemControl_Object((1,3,6,1,4,1,3373,1103,77,8),_SensorTempMonitorSystemControl_Type())
sensorTempMonitorSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:sensorTempMonitorSystemControl.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'sensorTemp':sensorTemp,'sensorTempMibVersion':sensorTempMibVersion,'sensorTempTable':sensorTempTable,'sensorTempEntry':sensorTempEntry,_G:sensorTempIndex,'sensorTempValue':sensorTempValue,'sensorTempThreshold1':sensorTempThreshold1,'sensorTempThreshold2':sensorTempThreshold2,'sensorTempHysteresis1':sensorTempHysteresis1,'sensorTempHysteresis2':sensorTempHysteresis2,'sensorTempStatus1':sensorTempStatus1,'sensorTempStatus2':sensorTempStatus2,'sensorTempLabel':sensorTempLabel,'sensorTempAlarmThreshold1':sensorTempAlarmThreshold1,'sensorTempAlarmThreshold2':sensorTempAlarmThreshold2,'sensorTempAlarmThreshold1Severity':sensorTempAlarmThreshold1Severity,'sensorTempAlarmThreshold2Severity':sensorTempAlarmThreshold2Severity,'sensorTempMonitorTable':sensorTempMonitorTable,'sensorTempMonitorEntry':sensorTempMonitorEntry,'sensorTempMonitorAdminStatus':sensorTempMonitorAdminStatus,'sensorTempMonitorOperStatus':sensorTempMonitorOperStatus,'sensorTempMonitorMinTemp':sensorTempMonitorMinTemp,'sensorTempMonitorMaxTemp':sensorTempMonitorMaxTemp,'sensorTempMonitorAverageTemp':sensorTempMonitorAverageTemp,'sensorTempMonitorSystemControl':sensorTempMonitorSystemControl})