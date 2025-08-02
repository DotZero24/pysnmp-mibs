_F='entPhySensorIndex'
_E='CUMULUS-SENSOR-MIB'
_D='unavailable'
_C='unknown'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cumulusMib,=mibBuilder.importSymbols('CUMULUS-SNMP-MIB','cumulusMib')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
agentSwitchSensorMIB=ModuleIdentity((1,3,6,1,4,1,40310,6))
class EntitySensorDataType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),(_C,2),('voltsAC',3),('voltsDC',4),('amperes',5),('watts',6),('hertz',7),('celsius',8),('percentRH',9),('rpm',10),('cmm',11),('truthvalue',12)))
class EntitySensorDataScale(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('yocto',1),('zepto',2),('atto',3),('femto',4),('pico',5),('nano',6),('micro',7),('milli',8),('units',9),('kilo',10),('mega',11),('giga',12),('tera',13),('exa',14),('peta',15),('zetta',16),('yotta',17)))
class EntitySensorPrecision(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-8,9))
class EntitySensorValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
class EntitySensorStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),(_D,2),('nonoperational',3)))
class EntitySensorAlarm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('other',1),(_C,2),('normal',3),('warning',4),('alert',5),('critical',6),('NotPresent',7),('NotOperational',8),(_D,9)))
class EntityAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),('notApplicable',2)))
_EntitySensorObjects_ObjectIdentity=ObjectIdentity
entitySensorObjects=_EntitySensorObjects_ObjectIdentity((1,3,6,1,4,1,40310,6,1))
_EntPhySensorTable_Object=MibTable
entPhySensorTable=_EntPhySensorTable_Object((1,3,6,1,4,1,40310,6,1,1))
if mibBuilder.loadTexts:entPhySensorTable.setStatus(_A)
_EntPhySensorEntry_Object=MibTableRow
entPhySensorEntry=_EntPhySensorEntry_Object((1,3,6,1,4,1,40310,6,1,1,1))
entPhySensorEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:entPhySensorEntry.setStatus(_A)
_EntPhySensorIndex_Type=Integer32
_EntPhySensorIndex_Object=MibTableColumn
entPhySensorIndex=_EntPhySensorIndex_Object((1,3,6,1,4,1,40310,6,1,1,1,1),_EntPhySensorIndex_Type())
entPhySensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorIndex.setStatus(_A)
_EntPhySensorType_Type=EntitySensorDataType
_EntPhySensorType_Object=MibTableColumn
entPhySensorType=_EntPhySensorType_Object((1,3,6,1,4,1,40310,6,1,1,1,2),_EntPhySensorType_Type())
entPhySensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorType.setStatus(_A)
_EntPhySensorScale_Type=EntitySensorDataScale
_EntPhySensorScale_Object=MibTableColumn
entPhySensorScale=_EntPhySensorScale_Object((1,3,6,1,4,1,40310,6,1,1,1,3),_EntPhySensorScale_Type())
entPhySensorScale.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorScale.setStatus(_A)
_EntPhySensorPrecision_Type=EntitySensorPrecision
_EntPhySensorPrecision_Object=MibTableColumn
entPhySensorPrecision=_EntPhySensorPrecision_Object((1,3,6,1,4,1,40310,6,1,1,1,4),_EntPhySensorPrecision_Type())
entPhySensorPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorPrecision.setStatus(_A)
_EntPhySensorValue_Type=EntitySensorValue
_EntPhySensorValue_Object=MibTableColumn
entPhySensorValue=_EntPhySensorValue_Object((1,3,6,1,4,1,40310,6,1,1,1,5),_EntPhySensorValue_Type())
entPhySensorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorValue.setStatus(_A)
_EntPhySensorOperStatus_Type=EntitySensorStatus
_EntPhySensorOperStatus_Object=MibTableColumn
entPhySensorOperStatus=_EntPhySensorOperStatus_Object((1,3,6,1,4,1,40310,6,1,1,1,6),_EntPhySensorOperStatus_Type())
entPhySensorOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorOperStatus.setStatus(_A)
_EntPhySensorUnitsDisplay_Type=SnmpAdminString
_EntPhySensorUnitsDisplay_Object=MibTableColumn
entPhySensorUnitsDisplay=_EntPhySensorUnitsDisplay_Object((1,3,6,1,4,1,40310,6,1,1,1,7),_EntPhySensorUnitsDisplay_Type())
entPhySensorUnitsDisplay.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorUnitsDisplay.setStatus(_A)
_EntPhySensorValueTimeStamp_Type=TimeStamp
_EntPhySensorValueTimeStamp_Object=MibTableColumn
entPhySensorValueTimeStamp=_EntPhySensorValueTimeStamp_Object((1,3,6,1,4,1,40310,6,1,1,1,8),_EntPhySensorValueTimeStamp_Type())
entPhySensorValueTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorValueTimeStamp.setStatus(_A)
_EntPhySensorValueUpdateRate_Type=Unsigned32
_EntPhySensorValueUpdateRate_Object=MibTableColumn
entPhySensorValueUpdateRate=_EntPhySensorValueUpdateRate_Object((1,3,6,1,4,1,40310,6,1,1,1,9),_EntPhySensorValueUpdateRate_Type())
entPhySensorValueUpdateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorValueUpdateRate.setStatus(_A)
if mibBuilder.loadTexts:entPhySensorValueUpdateRate.setUnits('milliseconds')
_EntPhySensorDescr_Type=SnmpAdminString
_EntPhySensorDescr_Object=MibTableColumn
entPhySensorDescr=_EntPhySensorDescr_Object((1,3,6,1,4,1,40310,6,1,1,1,10),_EntPhySensorDescr_Type())
entPhySensorDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorDescr.setStatus(_A)
_EntPhySensorMin_Type=EntitySensorValue
_EntPhySensorMin_Object=MibTableColumn
entPhySensorMin=_EntPhySensorMin_Object((1,3,6,1,4,1,40310,6,1,1,1,11),_EntPhySensorMin_Type())
entPhySensorMin.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorMin.setStatus(_A)
_EntPhySensorMax_Type=EntitySensorValue
_EntPhySensorMax_Object=MibTableColumn
entPhySensorMax=_EntPhySensorMax_Object((1,3,6,1,4,1,40310,6,1,1,1,12),_EntPhySensorMax_Type())
entPhySensorMax.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorMax.setStatus(_A)
_EntPhySensorAlarm_Type=EntitySensorAlarm
_EntPhySensorAlarm_Object=MibTableColumn
entPhySensorAlarm=_EntPhySensorAlarm_Object((1,3,6,1,4,1,40310,6,1,1,1,13),_EntPhySensorAlarm_Type())
entPhySensorAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorAlarm.setStatus(_A)
_EntPhySensorAdminStatus_Type=EntityAdminStatus
_EntPhySensorAdminStatus_Object=MibTableColumn
entPhySensorAdminStatus=_EntPhySensorAdminStatus_Object((1,3,6,1,4,1,40310,6,1,1,1,14),_EntPhySensorAdminStatus_Type())
entPhySensorAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:entPhySensorAdminStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'EntitySensorDataType':EntitySensorDataType,'EntitySensorDataScale':EntitySensorDataScale,'EntitySensorPrecision':EntitySensorPrecision,'EntitySensorValue':EntitySensorValue,'EntitySensorStatus':EntitySensorStatus,'EntitySensorAlarm':EntitySensorAlarm,'EntityAdminStatus':EntityAdminStatus,'agentSwitchSensorMIB':agentSwitchSensorMIB,'entitySensorObjects':entitySensorObjects,'entPhySensorTable':entPhySensorTable,'entPhySensorEntry':entPhySensorEntry,_F:entPhySensorIndex,'entPhySensorType':entPhySensorType,'entPhySensorScale':entPhySensorScale,'entPhySensorPrecision':entPhySensorPrecision,'entPhySensorValue':entPhySensorValue,'entPhySensorOperStatus':entPhySensorOperStatus,'entPhySensorUnitsDisplay':entPhySensorUnitsDisplay,'entPhySensorValueTimeStamp':entPhySensorValueTimeStamp,'entPhySensorValueUpdateRate':entPhySensorValueUpdateRate,'entPhySensorDescr':entPhySensorDescr,'entPhySensorMin':entPhySensorMin,'entPhySensorMax':entPhySensorMax,'entPhySensorAlarm':entPhySensorAlarm,'entPhySensorAdminStatus':entPhySensorAdminStatus})