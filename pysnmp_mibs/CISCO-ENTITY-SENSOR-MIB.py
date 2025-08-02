_e='entitySensorNotificationGroup'
_d='entSensorThresholdRecoveryNotification'
_c='entSensorThreshNotifGlobalEnable'
_b='entSensorMeasuredEntity'
_a='entSensorThresholdNotificationEnable'
_Z='entSensorThresholdEvaluation'
_Y='entSensorThresholdRelation'
_X='entSensorValueUpdateRate'
_W='entSensorValueTimeStamp'
_V='entSensorStatus'
_U='entSensorPrecision'
_T='entSensorScale'
_S='entSensorType'
_R='entSensorThresholdIndex'
_Q='Integer32'
_P='entitySensorNotifCtrlGlobalGroup'
_O='entSensorThresholdNotification'
_N='entPhysicalIndex'
_M='ENTITY-MIB'
_L='entitySensorValueGroupSup1'
_K='entSensorThresholdValue'
_J='entSensorThresholdSeverity'
_I='entSensorValue'
_H='entitySensorThresholdNotificationGroup'
_G='deprecated'
_F='read-write'
_E='entitySensorThresholdGroup'
_D='entitySensorValueGroup'
_C='read-only'
_B='current'
_A='CISCO-ENTITY-SENSOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
entPhysicalIndex,=mibBuilder.importSymbols(_M,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Q,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoEntitySensorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,91))
if mibBuilder.loadTexts:ciscoEntitySensorMIB.setRevisions(('2017-01-19 00:00','2015-01-15 00:00','2013-09-21 00:00','2007-11-12 00:00','2006-01-01 00:00','2005-09-08 00:00','2003-01-07 00:00','2002-10-16 00:00','2000-06-20 00:00'))
class SensorDataType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('other',1),('unknown',2),('voltsAC',3),('voltsDC',4),('amperes',5),('watts',6),('hertz',7),('celsius',8),('percentRH',9),('rpm',10),('cmm',11),('truthvalue',12),('specialEnum',13),('dBm',14),('dB',15)))
class SensorDataScale(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('yocto',1),('zepto',2),('atto',3),('femto',4),('pico',5),('nano',6),('micro',7),('milli',8),('units',9),('kilo',10),('mega',11),('giga',12),('tera',13),('exa',14),('peta',15),('zetta',16),('yotta',17)))
class SensorPrecision(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-8,9))
class SensorValue(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
class SensorStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('unavailable',2),('nonoperational',3)))
class SensorValueUpdateRate(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999999))
class SensorThresholdSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,20,30)));namedValues=NamedValues(*(('other',1),('minor',10),('major',20),('critical',30)))
class SensorThresholdRelation(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('lessThan',1),('lessOrEqual',2),('greaterThan',3),('greaterOrEqual',4),('equalTo',5),('notEqualTo',6)))
_EntitySensorMIBObjects_ObjectIdentity=ObjectIdentity
entitySensorMIBObjects=_EntitySensorMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,91,1))
_EntSensorValues_ObjectIdentity=ObjectIdentity
entSensorValues=_EntSensorValues_ObjectIdentity((1,3,6,1,4,1,9,9,91,1,1))
_EntSensorValueTable_Object=MibTable
entSensorValueTable=_EntSensorValueTable_Object((1,3,6,1,4,1,9,9,91,1,1,1))
if mibBuilder.loadTexts:entSensorValueTable.setStatus(_B)
_EntSensorValueEntry_Object=MibTableRow
entSensorValueEntry=_EntSensorValueEntry_Object((1,3,6,1,4,1,9,9,91,1,1,1,1))
entSensorValueEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:entSensorValueEntry.setStatus(_B)
_EntSensorType_Type=SensorDataType
_EntSensorType_Object=MibTableColumn
entSensorType=_EntSensorType_Object((1,3,6,1,4,1,9,9,91,1,1,1,1,1),_EntSensorType_Type())
entSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:entSensorType.setStatus(_B)
_EntSensorScale_Type=SensorDataScale
_EntSensorScale_Object=MibTableColumn
entSensorScale=_EntSensorScale_Object((1,3,6,1,4,1,9,9,91,1,1,1,1,2),_EntSensorScale_Type())
entSensorScale.setMaxAccess(_C)
if mibBuilder.loadTexts:entSensorScale.setStatus(_B)
_EntSensorPrecision_Type=SensorPrecision
_EntSensorPrecision_Object=MibTableColumn
entSensorPrecision=_EntSensorPrecision_Object((1,3,6,1,4,1,9,9,91,1,1,1,1,3),_EntSensorPrecision_Type())
entSensorPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:entSensorPrecision.setStatus(_B)
_EntSensorValue_Type=SensorValue
_EntSensorValue_Object=MibTableColumn
entSensorValue=_EntSensorValue_Object((1,3,6,1,4,1,9,9,91,1,1,1,1,4),_EntSensorValue_Type())
entSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:entSensorValue.setStatus(_B)
_EntSensorStatus_Type=SensorStatus
_EntSensorStatus_Object=MibTableColumn
entSensorStatus=_EntSensorStatus_Object((1,3,6,1,4,1,9,9,91,1,1,1,1,5),_EntSensorStatus_Type())
entSensorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:entSensorStatus.setStatus(_B)
_EntSensorValueTimeStamp_Type=TimeStamp
_EntSensorValueTimeStamp_Object=MibTableColumn
entSensorValueTimeStamp=_EntSensorValueTimeStamp_Object((1,3,6,1,4,1,9,9,91,1,1,1,1,6),_EntSensorValueTimeStamp_Type())
entSensorValueTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:entSensorValueTimeStamp.setStatus(_B)
_EntSensorValueUpdateRate_Type=SensorValueUpdateRate
_EntSensorValueUpdateRate_Object=MibTableColumn
entSensorValueUpdateRate=_EntSensorValueUpdateRate_Object((1,3,6,1,4,1,9,9,91,1,1,1,1,7),_EntSensorValueUpdateRate_Type())
entSensorValueUpdateRate.setMaxAccess(_C)
if mibBuilder.loadTexts:entSensorValueUpdateRate.setStatus(_B)
if mibBuilder.loadTexts:entSensorValueUpdateRate.setUnits('seconds')
_EntSensorMeasuredEntity_Type=EntPhysicalIndexOrZero
_EntSensorMeasuredEntity_Object=MibTableColumn
entSensorMeasuredEntity=_EntSensorMeasuredEntity_Object((1,3,6,1,4,1,9,9,91,1,1,1,1,8),_EntSensorMeasuredEntity_Type())
entSensorMeasuredEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:entSensorMeasuredEntity.setStatus(_B)
_EntSensorThresholds_ObjectIdentity=ObjectIdentity
entSensorThresholds=_EntSensorThresholds_ObjectIdentity((1,3,6,1,4,1,9,9,91,1,2))
_EntSensorThresholdTable_Object=MibTable
entSensorThresholdTable=_EntSensorThresholdTable_Object((1,3,6,1,4,1,9,9,91,1,2,1))
if mibBuilder.loadTexts:entSensorThresholdTable.setStatus(_B)
_EntSensorThresholdEntry_Object=MibTableRow
entSensorThresholdEntry=_EntSensorThresholdEntry_Object((1,3,6,1,4,1,9,9,91,1,2,1,1))
entSensorThresholdEntry.setIndexNames((0,_M,_N),(0,_A,_R))
if mibBuilder.loadTexts:entSensorThresholdEntry.setStatus(_B)
class _EntSensorThresholdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99999999))
_EntSensorThresholdIndex_Type.__name__=_Q
_EntSensorThresholdIndex_Object=MibTableColumn
entSensorThresholdIndex=_EntSensorThresholdIndex_Object((1,3,6,1,4,1,9,9,91,1,2,1,1,1),_EntSensorThresholdIndex_Type())
entSensorThresholdIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:entSensorThresholdIndex.setStatus(_B)
_EntSensorThresholdSeverity_Type=SensorThresholdSeverity
_EntSensorThresholdSeverity_Object=MibTableColumn
entSensorThresholdSeverity=_EntSensorThresholdSeverity_Object((1,3,6,1,4,1,9,9,91,1,2,1,1,2),_EntSensorThresholdSeverity_Type())
entSensorThresholdSeverity.setMaxAccess(_F)
if mibBuilder.loadTexts:entSensorThresholdSeverity.setStatus(_B)
_EntSensorThresholdRelation_Type=SensorThresholdRelation
_EntSensorThresholdRelation_Object=MibTableColumn
entSensorThresholdRelation=_EntSensorThresholdRelation_Object((1,3,6,1,4,1,9,9,91,1,2,1,1,3),_EntSensorThresholdRelation_Type())
entSensorThresholdRelation.setMaxAccess(_F)
if mibBuilder.loadTexts:entSensorThresholdRelation.setStatus(_B)
_EntSensorThresholdValue_Type=SensorValue
_EntSensorThresholdValue_Object=MibTableColumn
entSensorThresholdValue=_EntSensorThresholdValue_Object((1,3,6,1,4,1,9,9,91,1,2,1,1,4),_EntSensorThresholdValue_Type())
entSensorThresholdValue.setMaxAccess(_F)
if mibBuilder.loadTexts:entSensorThresholdValue.setStatus(_B)
_EntSensorThresholdEvaluation_Type=TruthValue
_EntSensorThresholdEvaluation_Object=MibTableColumn
entSensorThresholdEvaluation=_EntSensorThresholdEvaluation_Object((1,3,6,1,4,1,9,9,91,1,2,1,1,5),_EntSensorThresholdEvaluation_Type())
entSensorThresholdEvaluation.setMaxAccess(_C)
if mibBuilder.loadTexts:entSensorThresholdEvaluation.setStatus(_B)
_EntSensorThresholdNotificationEnable_Type=TruthValue
_EntSensorThresholdNotificationEnable_Object=MibTableColumn
entSensorThresholdNotificationEnable=_EntSensorThresholdNotificationEnable_Object((1,3,6,1,4,1,9,9,91,1,2,1,1,6),_EntSensorThresholdNotificationEnable_Type())
entSensorThresholdNotificationEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:entSensorThresholdNotificationEnable.setStatus(_B)
_EntSensorGlobalObjects_ObjectIdentity=ObjectIdentity
entSensorGlobalObjects=_EntSensorGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,91,1,3))
_EntSensorThreshNotifGlobalEnable_Type=TruthValue
_EntSensorThreshNotifGlobalEnable_Object=MibScalar
entSensorThreshNotifGlobalEnable=_EntSensorThreshNotifGlobalEnable_Object((1,3,6,1,4,1,9,9,91,1,3,1),_EntSensorThreshNotifGlobalEnable_Type())
entSensorThreshNotifGlobalEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:entSensorThreshNotifGlobalEnable.setStatus(_B)
_EntitySensorMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
entitySensorMIBNotificationPrefix=_EntitySensorMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,91,2))
_EntitySensorMIBNotifications_ObjectIdentity=ObjectIdentity
entitySensorMIBNotifications=_EntitySensorMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,91,2,0))
_EntitySensorMIBConformance_ObjectIdentity=ObjectIdentity
entitySensorMIBConformance=_EntitySensorMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,91,3))
_EntitySensorMIBCompliances_ObjectIdentity=ObjectIdentity
entitySensorMIBCompliances=_EntitySensorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,91,3,1))
_EntitySensorMIBGroups_ObjectIdentity=ObjectIdentity
entitySensorMIBGroups=_EntitySensorMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,91,3,2))
entitySensorValueGroup=ObjectGroup((1,3,6,1,4,1,9,9,91,3,2,1))
entitySensorValueGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_I),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:entitySensorValueGroup.setStatus(_B)
entitySensorThresholdGroup=ObjectGroup((1,3,6,1,4,1,9,9,91,3,2,2))
entitySensorThresholdGroup.setObjects(*((_A,_J),(_A,_Y),(_A,_K),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:entitySensorThresholdGroup.setStatus(_B)
entitySensorValueGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,91,3,2,4))
entitySensorValueGroupSup1.setObjects((_A,_b))
if mibBuilder.loadTexts:entitySensorValueGroupSup1.setStatus(_B)
entitySensorNotifCtrlGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,91,3,2,5))
entitySensorNotifCtrlGlobalGroup.setObjects((_A,_c))
if mibBuilder.loadTexts:entitySensorNotifCtrlGlobalGroup.setStatus(_B)
entSensorThresholdNotification=NotificationType((1,3,6,1,4,1,9,9,91,2,0,1))
entSensorThresholdNotification.setObjects(*((_A,_K),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:entSensorThresholdNotification.setStatus(_B)
entSensorThresholdRecoveryNotification=NotificationType((1,3,6,1,4,1,9,9,91,2,0,2))
entSensorThresholdRecoveryNotification.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:entSensorThresholdRecoveryNotification.setStatus(_B)
entitySensorThresholdNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,91,3,2,3))
entitySensorThresholdNotificationGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:entitySensorThresholdNotificationGroup.setStatus(_G)
entitySensorNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,91,3,2,6))
entitySensorNotificationGroup.setObjects(*((_A,_O),(_A,_d)))
if mibBuilder.loadTexts:entitySensorNotificationGroup.setStatus(_B)
entitySensorMIBComplianceV01=ModuleCompliance((1,3,6,1,4,1,9,9,91,3,1,1))
entitySensorMIBComplianceV01.setObjects(*((_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:entitySensorMIBComplianceV01.setStatus(_G)
entitySensorMIBComplianceV02=ModuleCompliance((1,3,6,1,4,1,9,9,91,3,1,2))
entitySensorMIBComplianceV02.setObjects(*((_A,_E),(_A,_D),(_A,_H)))
if mibBuilder.loadTexts:entitySensorMIBComplianceV02.setStatus(_G)
entitySensorMIBComplianceV03=ModuleCompliance((1,3,6,1,4,1,9,9,91,3,1,3))
entitySensorMIBComplianceV03.setObjects(*((_A,_E),(_A,_D),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:entitySensorMIBComplianceV03.setStatus(_G)
entitySensorMIBComplianceV04=ModuleCompliance((1,3,6,1,4,1,9,9,91,3,1,4))
entitySensorMIBComplianceV04.setObjects(*((_A,_E),(_A,_D),(_A,_H),(_A,_L),(_A,_P)))
if mibBuilder.loadTexts:entitySensorMIBComplianceV04.setStatus(_G)
entitySensorMIBComplianceV05=ModuleCompliance((1,3,6,1,4,1,9,9,91,3,1,5))
entitySensorMIBComplianceV05.setObjects(*((_A,_E),(_A,_D),(_A,_L),(_A,_P),(_A,_e)))
if mibBuilder.loadTexts:entitySensorMIBComplianceV05.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SensorDataType':SensorDataType,'SensorDataScale':SensorDataScale,'SensorPrecision':SensorPrecision,'SensorValue':SensorValue,'SensorStatus':SensorStatus,'SensorValueUpdateRate':SensorValueUpdateRate,'SensorThresholdSeverity':SensorThresholdSeverity,'SensorThresholdRelation':SensorThresholdRelation,'ciscoEntitySensorMIB':ciscoEntitySensorMIB,'entitySensorMIBObjects':entitySensorMIBObjects,'entSensorValues':entSensorValues,'entSensorValueTable':entSensorValueTable,'entSensorValueEntry':entSensorValueEntry,_S:entSensorType,_T:entSensorScale,_U:entSensorPrecision,_I:entSensorValue,_V:entSensorStatus,_W:entSensorValueTimeStamp,_X:entSensorValueUpdateRate,_b:entSensorMeasuredEntity,'entSensorThresholds':entSensorThresholds,'entSensorThresholdTable':entSensorThresholdTable,'entSensorThresholdEntry':entSensorThresholdEntry,_R:entSensorThresholdIndex,_J:entSensorThresholdSeverity,_Y:entSensorThresholdRelation,_K:entSensorThresholdValue,_Z:entSensorThresholdEvaluation,_a:entSensorThresholdNotificationEnable,'entSensorGlobalObjects':entSensorGlobalObjects,_c:entSensorThreshNotifGlobalEnable,'entitySensorMIBNotificationPrefix':entitySensorMIBNotificationPrefix,'entitySensorMIBNotifications':entitySensorMIBNotifications,_O:entSensorThresholdNotification,_d:entSensorThresholdRecoveryNotification,'entitySensorMIBConformance':entitySensorMIBConformance,'entitySensorMIBCompliances':entitySensorMIBCompliances,'entitySensorMIBComplianceV01':entitySensorMIBComplianceV01,'entitySensorMIBComplianceV02':entitySensorMIBComplianceV02,'entitySensorMIBComplianceV03':entitySensorMIBComplianceV03,'entitySensorMIBComplianceV04':entitySensorMIBComplianceV04,'entitySensorMIBComplianceV05':entitySensorMIBComplianceV05,'entitySensorMIBGroups':entitySensorMIBGroups,_D:entitySensorValueGroup,_E:entitySensorThresholdGroup,_H:entitySensorThresholdNotificationGroup,_L:entitySensorValueGroupSup1,_P:entitySensorNotifCtrlGlobalGroup,_e:entitySensorNotificationGroup})