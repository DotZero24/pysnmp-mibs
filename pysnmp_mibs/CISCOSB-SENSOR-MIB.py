_O='entitySensorValueGroup'
_N='entPhySensorValueUpdateRate'
_M='entPhySensorValueTimeStamp'
_L='entPhySensorUnitsDisplay'
_K='entPhySensorOperStatus'
_J='entPhySensorValue'
_I='entPhySensorPrecision'
_H='entPhySensorScale'
_G='entPhySensorType'
_F='entityPhysicalGroup'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='CISCOSB-SENSOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rlEnv,=mibBuilder.importSymbols('CISCOSB-MIB','rlEnv')
entPhysicalIndex,entityPhysicalGroup=mibBuilder.importSymbols(_D,_E,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
entitySensorMIB=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,83,2))
if mibBuilder.loadTexts:entitySensorMIB.setRevisions(('2002-10-16 00:00',))
class EntitySensorDataType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),('unknown',2),('voltsAC',3),('voltsDC',4),('amperes',5),('watts',6),('hertz',7),('celsius',8),('percentRH',9),('rpm',10),('cmm',11),('truthvalue',12)))
class EntitySensorDataScale(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('yocto',1),('zepto',2),('atto',3),('femto',4),('pico',5),('nano',6),('micro',7),('milli',8),('units',9),('kilo',10),('mega',11),('giga',12),('tera',13),('exa',14),('peta',15),('zetta',16),('yotta',17)))
class EntitySensorPrecision(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-8,9))
class EntitySensorValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
class EntitySensorStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('unavailable',2),('nonoperational',3)))
_EntitySensorObjects_ObjectIdentity=ObjectIdentity
entitySensorObjects=_EntitySensorObjects_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,83,2,1))
_EntPhySensorTable_Object=MibTable
entPhySensorTable=_EntPhySensorTable_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1))
if mibBuilder.loadTexts:entPhySensorTable.setStatus(_A)
_EntPhySensorEntry_Object=MibTableRow
entPhySensorEntry=_EntPhySensorEntry_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1,1))
entPhySensorEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:entPhySensorEntry.setStatus(_A)
_EntPhySensorType_Type=EntitySensorDataType
_EntPhySensorType_Object=MibTableColumn
entPhySensorType=_EntPhySensorType_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1,1,1),_EntPhySensorType_Type())
entPhySensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhySensorType.setStatus(_A)
_EntPhySensorScale_Type=EntitySensorDataScale
_EntPhySensorScale_Object=MibTableColumn
entPhySensorScale=_EntPhySensorScale_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1,1,2),_EntPhySensorScale_Type())
entPhySensorScale.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhySensorScale.setStatus(_A)
_EntPhySensorPrecision_Type=EntitySensorPrecision
_EntPhySensorPrecision_Object=MibTableColumn
entPhySensorPrecision=_EntPhySensorPrecision_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1,1,3),_EntPhySensorPrecision_Type())
entPhySensorPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhySensorPrecision.setStatus(_A)
_EntPhySensorValue_Type=EntitySensorValue
_EntPhySensorValue_Object=MibTableColumn
entPhySensorValue=_EntPhySensorValue_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1,1,4),_EntPhySensorValue_Type())
entPhySensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhySensorValue.setStatus(_A)
_EntPhySensorOperStatus_Type=EntitySensorStatus
_EntPhySensorOperStatus_Object=MibTableColumn
entPhySensorOperStatus=_EntPhySensorOperStatus_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1,1,5),_EntPhySensorOperStatus_Type())
entPhySensorOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhySensorOperStatus.setStatus(_A)
_EntPhySensorUnitsDisplay_Type=SnmpAdminString
_EntPhySensorUnitsDisplay_Object=MibTableColumn
entPhySensorUnitsDisplay=_EntPhySensorUnitsDisplay_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1,1,6),_EntPhySensorUnitsDisplay_Type())
entPhySensorUnitsDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhySensorUnitsDisplay.setStatus(_A)
_EntPhySensorValueTimeStamp_Type=TimeStamp
_EntPhySensorValueTimeStamp_Object=MibTableColumn
entPhySensorValueTimeStamp=_EntPhySensorValueTimeStamp_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1,1,7),_EntPhySensorValueTimeStamp_Type())
entPhySensorValueTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhySensorValueTimeStamp.setStatus(_A)
_EntPhySensorValueUpdateRate_Type=Unsigned32
_EntPhySensorValueUpdateRate_Object=MibTableColumn
entPhySensorValueUpdateRate=_EntPhySensorValueUpdateRate_Object((1,3,6,1,4,1,9,6,1,101,83,2,1,1,1,8),_EntPhySensorValueUpdateRate_Type())
entPhySensorValueUpdateRate.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhySensorValueUpdateRate.setStatus(_A)
if mibBuilder.loadTexts:entPhySensorValueUpdateRate.setUnits('milliseconds')
_EntitySensorConformance_ObjectIdentity=ObjectIdentity
entitySensorConformance=_EntitySensorConformance_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,83,2,3))
_EntitySensorCompliances_ObjectIdentity=ObjectIdentity
entitySensorCompliances=_EntitySensorCompliances_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,83,2,3,1))
_EntitySensorGroups_ObjectIdentity=ObjectIdentity
entitySensorGroups=_EntitySensorGroups_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,83,2,3,2))
entitySensorValueGroup=ObjectGroup((1,3,6,1,4,1,9,6,1,101,83,2,3,2,1))
entitySensorValueGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:entitySensorValueGroup.setStatus(_A)
entitySensorCompliance=ModuleCompliance((1,3,6,1,4,1,9,6,1,101,83,2,3,1,1))
entitySensorCompliance.setObjects(*((_B,_O),(_D,_F)))
if mibBuilder.loadTexts:entitySensorCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EntitySensorDataType':EntitySensorDataType,'EntitySensorDataScale':EntitySensorDataScale,'EntitySensorPrecision':EntitySensorPrecision,'EntitySensorValue':EntitySensorValue,'EntitySensorStatus':EntitySensorStatus,'entitySensorMIB':entitySensorMIB,'entitySensorObjects':entitySensorObjects,'entPhySensorTable':entPhySensorTable,'entPhySensorEntry':entPhySensorEntry,_G:entPhySensorType,_H:entPhySensorScale,_I:entPhySensorPrecision,_J:entPhySensorValue,_K:entPhySensorOperStatus,_L:entPhySensorUnitsDisplay,_M:entPhySensorValueTimeStamp,_N:entPhySensorValueUpdateRate,'entitySensorConformance':entitySensorConformance,'entitySensorCompliances':entitySensorCompliances,'entitySensorCompliance':entitySensorCompliance,'entitySensorGroups':entitySensorGroups,_O:entitySensorValueGroup})