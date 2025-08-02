_Y='ciscoEntSensorExtNotificationGroup'
_X='ciscoEntSensorExtNotificationCtrlGroup'
_W='ciscoEntSensorExtThresholdGroup'
_V='ceSensorExtThresholdNotification'
_U='ceSensorExtThresholdNotifGlobalEnable'
_T='ceSensorExtThresholdNotifEnable'
_S='ceSensorExtThresholdEvaluation'
_R='ceSensorExtThresholdRelation'
_Q='ceSensorExtThresholdSeverity'
_P='disabled'
_O='enabled'
_N='ceSensorExtThresholdIndex'
_M='Unsigned32'
_L='entPhySensorValue'
_K='entPhySensorType'
_J='entPhysicalName'
_I='entPhysicalIndex'
_H='entPhysicalDescr'
_G='ceSensorExtThresholdValue'
_F='Integer32'
_E='ENTITY-SENSOR-MIB'
_D='ENTITY-MIB'
_C='read-write'
_B='CISCO-ENTITY-SENSOR-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalDescr,entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_D,_H,_I,_J)
EntitySensorValue,entPhySensorType,entPhySensorValue=mibBuilder.importSymbols(_E,'EntitySensorValue',_K,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoEntitySensorExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,745))
if mibBuilder.loadTexts:ciscoEntitySensorExtMIB.setRevisions(('2010-06-09 00:00',))
class CiscoSensorThresholdSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,20,30)));namedValues=NamedValues(*(('other',1),('minor',10),('major',20),('critical',30)))
class CiscoSensorThresholdRelation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('lessThan',1),('lessOrEqual',2),('greaterThan',3),('greaterOrEqual',4),('equalTo',5),('notEqualTo',6)))
_CiscoEntitySensorExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoEntitySensorExtMIBNotifs=_CiscoEntitySensorExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,745,0))
_CiscoEntitySensorExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntitySensorExtMIBObjects=_CiscoEntitySensorExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,745,1))
_CeSensorExtThresholdTable_Object=MibTable
ceSensorExtThresholdTable=_CeSensorExtThresholdTable_Object((1,3,6,1,4,1,9,9,745,1,1))
if mibBuilder.loadTexts:ceSensorExtThresholdTable.setStatus(_A)
_CeSensorExtThresholdEntry_Object=MibTableRow
ceSensorExtThresholdEntry=_CeSensorExtThresholdEntry_Object((1,3,6,1,4,1,9,9,745,1,1,1))
ceSensorExtThresholdEntry.setIndexNames((0,_D,_I),(0,_B,_N))
if mibBuilder.loadTexts:ceSensorExtThresholdEntry.setStatus(_A)
class _CeSensorExtThresholdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CeSensorExtThresholdIndex_Type.__name__=_M
_CeSensorExtThresholdIndex_Object=MibTableColumn
ceSensorExtThresholdIndex=_CeSensorExtThresholdIndex_Object((1,3,6,1,4,1,9,9,745,1,1,1,1),_CeSensorExtThresholdIndex_Type())
ceSensorExtThresholdIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ceSensorExtThresholdIndex.setStatus(_A)
_CeSensorExtThresholdSeverity_Type=CiscoSensorThresholdSeverity
_CeSensorExtThresholdSeverity_Object=MibTableColumn
ceSensorExtThresholdSeverity=_CeSensorExtThresholdSeverity_Object((1,3,6,1,4,1,9,9,745,1,1,1,2),_CeSensorExtThresholdSeverity_Type())
ceSensorExtThresholdSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSensorExtThresholdSeverity.setStatus(_A)
_CeSensorExtThresholdRelation_Type=CiscoSensorThresholdRelation
_CeSensorExtThresholdRelation_Object=MibTableColumn
ceSensorExtThresholdRelation=_CeSensorExtThresholdRelation_Object((1,3,6,1,4,1,9,9,745,1,1,1,3),_CeSensorExtThresholdRelation_Type())
ceSensorExtThresholdRelation.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSensorExtThresholdRelation.setStatus(_A)
_CeSensorExtThresholdValue_Type=EntitySensorValue
_CeSensorExtThresholdValue_Object=MibTableColumn
ceSensorExtThresholdValue=_CeSensorExtThresholdValue_Object((1,3,6,1,4,1,9,9,745,1,1,1,4),_CeSensorExtThresholdValue_Type())
ceSensorExtThresholdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSensorExtThresholdValue.setStatus(_A)
_CeSensorExtThresholdEvaluation_Type=TruthValue
_CeSensorExtThresholdEvaluation_Object=MibTableColumn
ceSensorExtThresholdEvaluation=_CeSensorExtThresholdEvaluation_Object((1,3,6,1,4,1,9,9,745,1,1,1,5),_CeSensorExtThresholdEvaluation_Type())
ceSensorExtThresholdEvaluation.setMaxAccess('read-only')
if mibBuilder.loadTexts:ceSensorExtThresholdEvaluation.setStatus(_A)
class _CeSensorExtThresholdNotifEnable_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),('transparent',3)))
_CeSensorExtThresholdNotifEnable_Type.__name__=_F
_CeSensorExtThresholdNotifEnable_Object=MibTableColumn
ceSensorExtThresholdNotifEnable=_CeSensorExtThresholdNotifEnable_Object((1,3,6,1,4,1,9,9,745,1,1,1,6),_CeSensorExtThresholdNotifEnable_Type())
ceSensorExtThresholdNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSensorExtThresholdNotifEnable.setStatus(_A)
_CiscoEntSensorExtGlobalObjects_ObjectIdentity=ObjectIdentity
ciscoEntSensorExtGlobalObjects=_CiscoEntSensorExtGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,745,1,2))
class _CeSensorExtThresholdNotifGlobalEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_CeSensorExtThresholdNotifGlobalEnable_Type.__name__=_F
_CeSensorExtThresholdNotifGlobalEnable_Object=MibScalar
ceSensorExtThresholdNotifGlobalEnable=_CeSensorExtThresholdNotifGlobalEnable_Object((1,3,6,1,4,1,9,9,745,1,2,1),_CeSensorExtThresholdNotifGlobalEnable_Type())
ceSensorExtThresholdNotifGlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSensorExtThresholdNotifGlobalEnable.setStatus(_A)
_CiscoEntitySensorExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoEntitySensorExtMIBConform=_CiscoEntitySensorExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,745,2))
_CiscoEntSensorExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEntSensorExtMIBCompliances=_CiscoEntSensorExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,745,2,1))
_CiscoEntSensorExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEntSensorExtMIBGroups=_CiscoEntSensorExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,745,2,2))
ciscoEntSensorExtThresholdGroup=ObjectGroup((1,3,6,1,4,1,9,9,745,2,2,1))
ciscoEntSensorExtThresholdGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_G),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoEntSensorExtThresholdGroup.setStatus(_A)
ciscoEntSensorExtNotificationCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,9,745,2,2,3))
ciscoEntSensorExtNotificationCtrlGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:ciscoEntSensorExtNotificationCtrlGroup.setStatus(_A)
ceSensorExtThresholdNotification=NotificationType((1,3,6,1,4,1,9,9,745,0,1))
ceSensorExtThresholdNotification.setObjects(*((_D,_J),(_D,_H),(_E,_L),(_E,_K),(_B,_G)))
if mibBuilder.loadTexts:ceSensorExtThresholdNotification.setStatus(_A)
ciscoEntSensorExtNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,745,2,2,2))
ciscoEntSensorExtNotificationGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:ciscoEntSensorExtNotificationGroup.setStatus(_A)
ciscoEntSensorExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,745,2,1,1))
ciscoEntSensorExtMIBCompliance.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoEntSensorExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoSensorThresholdSeverity':CiscoSensorThresholdSeverity,'CiscoSensorThresholdRelation':CiscoSensorThresholdRelation,'ciscoEntitySensorExtMIB':ciscoEntitySensorExtMIB,'ciscoEntitySensorExtMIBNotifs':ciscoEntitySensorExtMIBNotifs,_V:ceSensorExtThresholdNotification,'ciscoEntitySensorExtMIBObjects':ciscoEntitySensorExtMIBObjects,'ceSensorExtThresholdTable':ceSensorExtThresholdTable,'ceSensorExtThresholdEntry':ceSensorExtThresholdEntry,_N:ceSensorExtThresholdIndex,_Q:ceSensorExtThresholdSeverity,_R:ceSensorExtThresholdRelation,_G:ceSensorExtThresholdValue,_S:ceSensorExtThresholdEvaluation,_T:ceSensorExtThresholdNotifEnable,'ciscoEntSensorExtGlobalObjects':ciscoEntSensorExtGlobalObjects,_U:ceSensorExtThresholdNotifGlobalEnable,'ciscoEntitySensorExtMIBConform':ciscoEntitySensorExtMIBConform,'ciscoEntSensorExtMIBCompliances':ciscoEntSensorExtMIBCompliances,'ciscoEntSensorExtMIBCompliance':ciscoEntSensorExtMIBCompliance,'ciscoEntSensorExtMIBGroups':ciscoEntSensorExtMIBGroups,_W:ciscoEntSensorExtThresholdGroup,_Y:ciscoEntSensorExtNotificationGroup,_X:ciscoEntSensorExtNotificationCtrlGroup})