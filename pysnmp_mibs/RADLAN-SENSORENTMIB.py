_D='rlEntPhySensorEntry'
_C='RADLAN-SENSORENTMIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,entityPhysicalGroup=mibBuilder.importSymbols('ENTITY-MIB','entPhysicalIndex','entityPhysicalGroup')
EntitySensorValue,entPhySensorEntry=mibBuilder.importSymbols('ENTITY-SENSOR-MIB','EntitySensorValue','entPhySensorEntry')
rlEnv,=mibBuilder.importSymbols('RADLAN-HWENVIROMENT','rlEnv')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
rlSensor=ModuleIdentity((1,3,6,1,4,1,89,83,4))
if mibBuilder.loadTexts:rlSensor.setRevisions(('2003-09-21 00:00',))
_RlEntPhySensorTable_Object=MibTable
rlEntPhySensorTable=_RlEntPhySensorTable_Object((1,3,6,1,4,1,89,83,3))
if mibBuilder.loadTexts:rlEntPhySensorTable.setStatus(_A)
_RlEntPhySensorEntry_Object=MibTableRow
rlEntPhySensorEntry=_RlEntPhySensorEntry_Object((1,3,6,1,4,1,89,83,3,1))
if mibBuilder.loadTexts:rlEntPhySensorEntry.setStatus(_A)
_RlEnvPhySensorMinValue_Type=EntitySensorValue
_RlEnvPhySensorMinValue_Object=MibTableColumn
rlEnvPhySensorMinValue=_RlEnvPhySensorMinValue_Object((1,3,6,1,4,1,89,83,3,1,1),_RlEnvPhySensorMinValue_Type())
rlEnvPhySensorMinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvPhySensorMinValue.setStatus(_A)
_RlEnvPhySensorMaxValue_Type=EntitySensorValue
_RlEnvPhySensorMaxValue_Object=MibTableColumn
rlEnvPhySensorMaxValue=_RlEnvPhySensorMaxValue_Object((1,3,6,1,4,1,89,83,3,1,2),_RlEnvPhySensorMaxValue_Type())
rlEnvPhySensorMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvPhySensorMaxValue.setStatus(_A)
_RlEnvPhySensorTestValue_Type=EntitySensorValue
_RlEnvPhySensorTestValue_Object=MibTableColumn
rlEnvPhySensorTestValue=_RlEnvPhySensorTestValue_Object((1,3,6,1,4,1,89,83,3,1,3),_RlEnvPhySensorTestValue_Type())
rlEnvPhySensorTestValue.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlEnvPhySensorTestValue.setStatus(_A)
entPhySensorEntry.registerAugmentions((_C,_D))
rlEntPhySensorEntry.setIndexNames(*entPhySensorEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'rlEntPhySensorTable':rlEntPhySensorTable,_D:rlEntPhySensorEntry,'rlEnvPhySensorMinValue':rlEnvPhySensorMinValue,'rlEnvPhySensorMaxValue':rlEnvPhySensorMaxValue,'rlEnvPhySensorTestValue':rlEnvPhySensorTestValue,'rlSensor':rlSensor})