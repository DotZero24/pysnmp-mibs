_f='cdtVariableOwnerName'
_e='cdtVariableOwnerId'
_d='cdtVariableTranslation'
_c='cdtVariableValue'
_b='cdtVariableName'
_a='cdtVariableId'
_Z='cdtMessageText'
_Y='cdtWorkflowName'
_X='cdtWorkflowId'
_W='cdtMessageCategory'
_V='riZoneProjectChangeTime'
_U='riZoneProjectName'
_T='customDefinedTrapIndex'
_S='variableIndex'
_R='componentIndex'
_Q='failed'
_P='NotificationType'
_O='sysName'
_N='sysLocation'
_M='sysContact'
_L='undefined'
_K='timeout'
_J='SNMPv2-MIB'
_I='DisplayString'
_H='alarm'
_G='notAvail'
_F='warning'
_E='RITTAL-RIZONE-MIB'
_D='ok'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysContact,sysLocation,sysName=mibBuilder.importSymbols(_J,_M,_N,_O)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_P,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_P,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
_Rittal_ObjectIdentity=ObjectIdentity
rittal=_Rittal_ObjectIdentity((1,3,6,1,4,1,2606))
_RiZone_ObjectIdentity=ObjectIdentity
riZone=_RiZone_ObjectIdentity((1,3,6,1,4,1,2606,6))
_RiZoneMibRev_ObjectIdentity=ObjectIdentity
riZoneMibRev=_RiZoneMibRev_ObjectIdentity((1,3,6,1,4,1,2606,6,1))
_RiZoneMibMajRev_Type=Integer32
_RiZoneMibMajRev_Object=MibScalar
riZoneMibMajRev=_RiZoneMibMajRev_Object((1,3,6,1,4,1,2606,6,1,1),_RiZoneMibMajRev_Type())
riZoneMibMajRev.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneMibMajRev.setStatus(_A)
_RiZoneMibMinRev_Type=Integer32
_RiZoneMibMinRev_Object=MibScalar
riZoneMibMinRev=_RiZoneMibMinRev_Object((1,3,6,1,4,1,2606,6,1,2),_RiZoneMibMinRev_Type())
riZoneMibMinRev.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneMibMinRev.setStatus(_A)
class _RiZoneMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),(_D,2),('degraded',3),(_Q,4),('configChanged',5),(_K,6)))
_RiZoneMibCondition_Type.__name__=_C
_RiZoneMibCondition_Object=MibScalar
riZoneMibCondition=_RiZoneMibCondition_Object((1,3,6,1,4,1,2606,6,1,3),_RiZoneMibCondition_Type())
riZoneMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneMibCondition.setStatus(_A)
_RiZoneModules_ObjectIdentity=ObjectIdentity
riZoneModules=_RiZoneModules_ObjectIdentity((1,3,6,1,4,1,2606,6,2))
class _RiZoneCoreState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_D,2)))
_RiZoneCoreState_Type.__name__=_C
_RiZoneCoreState_Object=MibScalar
riZoneCoreState=_RiZoneCoreState_Object((1,3,6,1,4,1,2606,6,2,1),_RiZoneCoreState_Type())
riZoneCoreState.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneCoreState.setStatus(_A)
class _RiZoneCoreVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_RiZoneCoreVersion_Type.__name__=_I
_RiZoneCoreVersion_Object=MibScalar
riZoneCoreVersion=_RiZoneCoreVersion_Object((1,3,6,1,4,1,2606,6,2,2),_RiZoneCoreVersion_Type())
riZoneCoreVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneCoreVersion.setStatus(_A)
_RiZoneProject_ObjectIdentity=ObjectIdentity
riZoneProject=_RiZoneProject_ObjectIdentity((1,3,6,1,4,1,2606,6,3))
class _RiZoneProjectName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_RiZoneProjectName_Type.__name__=_I
_RiZoneProjectName_Object=MibScalar
riZoneProjectName=_RiZoneProjectName_Object((1,3,6,1,4,1,2606,6,3,1),_RiZoneProjectName_Type())
riZoneProjectName.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneProjectName.setStatus(_A)
class _RiZoneProjectChangeTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_RiZoneProjectChangeTime_Type.__name__=_I
_RiZoneProjectChangeTime_Object=MibScalar
riZoneProjectChangeTime=_RiZoneProjectChangeTime_Object((1,3,6,1,4,1,2606,6,3,2),_RiZoneProjectChangeTime_Type())
riZoneProjectChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneProjectChangeTime.setStatus(_A)
_RiZoneStatus_ObjectIdentity=ObjectIdentity
riZoneStatus=_RiZoneStatus_ObjectIdentity((1,3,6,1,4,1,2606,6,4))
_RiZoneComponents_ObjectIdentity=ObjectIdentity
riZoneComponents=_RiZoneComponents_ObjectIdentity((1,3,6,1,4,1,2606,6,4,1))
_RiZoneNumberOfComponents_Type=Integer32
_RiZoneNumberOfComponents_Object=MibScalar
riZoneNumberOfComponents=_RiZoneNumberOfComponents_Object((1,3,6,1,4,1,2606,6,4,1,1),_RiZoneNumberOfComponents_Type())
riZoneNumberOfComponents.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneNumberOfComponents.setStatus(_A)
_RiZoneComponentTable_Object=MibTable
riZoneComponentTable=_RiZoneComponentTable_Object((1,3,6,1,4,1,2606,6,4,1,2))
if mibBuilder.loadTexts:riZoneComponentTable.setStatus(_A)
_RiZoneComponentEntry_Object=MibTableRow
riZoneComponentEntry=_RiZoneComponentEntry_Object((1,3,6,1,4,1,2606,6,4,1,2,1))
riZoneComponentEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:riZoneComponentEntry.setStatus(_A)
class _ComponentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ComponentIndex_Type.__name__=_C
_ComponentIndex_Object=MibTableColumn
componentIndex=_ComponentIndex_Object((1,3,6,1,4,1,2606,6,4,1,2,1,1),_ComponentIndex_Type())
componentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:componentIndex.setStatus(_A)
_ComponentId_Type=Integer32
_ComponentId_Object=MibTableColumn
componentId=_ComponentId_Object((1,3,6,1,4,1,2606,6,4,1,2,1,2),_ComponentId_Type())
componentId.setMaxAccess(_B)
if mibBuilder.loadTexts:componentId.setStatus(_A)
class _ComponentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_ComponentName_Type.__name__=_I
_ComponentName_Object=MibTableColumn
componentName=_ComponentName_Object((1,3,6,1,4,1,2606,6,4,1,2,1,3),_ComponentName_Type())
componentName.setMaxAccess(_B)
if mibBuilder.loadTexts:componentName.setStatus(_A)
class _ComponentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('removed',1),('domain',2),('location',3),('building',4),('room',5),('rackrow',6),('rack',7),('device',8),('rackitem',9)))
_ComponentType_Type.__name__=_C
_ComponentType_Object=MibTableColumn
componentType=_ComponentType_Object((1,3,6,1,4,1,2606,6,4,1,2,1,4),_ComponentType_Type())
componentType.setMaxAccess(_B)
if mibBuilder.loadTexts:componentType.setStatus(_A)
_ComponentParent_Type=Integer32
_ComponentParent_Object=MibTableColumn
componentParent=_ComponentParent_Object((1,3,6,1,4,1,2606,6,4,1,2,1,5),_ComponentParent_Type())
componentParent.setMaxAccess(_B)
if mibBuilder.loadTexts:componentParent.setStatus(_A)
class _ComponentStatusTotal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4),(_K,5)))
_ComponentStatusTotal_Type.__name__=_C
_ComponentStatusTotal_Object=MibTableColumn
componentStatusTotal=_ComponentStatusTotal_Object((1,3,6,1,4,1,2606,6,4,1,2,1,6),_ComponentStatusTotal_Type())
componentStatusTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:componentStatusTotal.setStatus(_A)
class _ComponentStatusAvailability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4),(_K,5)))
_ComponentStatusAvailability_Type.__name__=_C
_ComponentStatusAvailability_Object=MibTableColumn
componentStatusAvailability=_ComponentStatusAvailability_Object((1,3,6,1,4,1,2606,6,4,1,2,1,7),_ComponentStatusAvailability_Type())
componentStatusAvailability.setMaxAccess(_B)
if mibBuilder.loadTexts:componentStatusAvailability.setStatus(_A)
class _ComponentStatusCooling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_ComponentStatusCooling_Type.__name__=_C
_ComponentStatusCooling_Object=MibTableColumn
componentStatusCooling=_ComponentStatusCooling_Object((1,3,6,1,4,1,2606,6,4,1,2,1,8),_ComponentStatusCooling_Type())
componentStatusCooling.setMaxAccess(_B)
if mibBuilder.loadTexts:componentStatusCooling.setStatus(_A)
class _ComponentStatusPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_ComponentStatusPower_Type.__name__=_C
_ComponentStatusPower_Object=MibTableColumn
componentStatusPower=_ComponentStatusPower_Object((1,3,6,1,4,1,2606,6,4,1,2,1,9),_ComponentStatusPower_Type())
componentStatusPower.setMaxAccess(_B)
if mibBuilder.loadTexts:componentStatusPower.setStatus(_A)
class _ComponentStatusMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_ComponentStatusMonitoring_Type.__name__=_C
_ComponentStatusMonitoring_Object=MibTableColumn
componentStatusMonitoring=_ComponentStatusMonitoring_Object((1,3,6,1,4,1,2606,6,4,1,2,1,10),_ComponentStatusMonitoring_Type())
componentStatusMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:componentStatusMonitoring.setStatus(_A)
class _ComponentStatusSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_ComponentStatusSecurity_Type.__name__=_C
_ComponentStatusSecurity_Object=MibTableColumn
componentStatusSecurity=_ComponentStatusSecurity_Object((1,3,6,1,4,1,2606,6,4,1,2,1,11),_ComponentStatusSecurity_Type())
componentStatusSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:componentStatusSecurity.setStatus(_A)
class _ComponentStatusCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_ComponentStatusCapacity_Type.__name__=_C
_ComponentStatusCapacity_Object=MibTableColumn
componentStatusCapacity=_ComponentStatusCapacity_Object((1,3,6,1,4,1,2606,6,4,1,2,1,12),_ComponentStatusCapacity_Type())
componentStatusCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:componentStatusCapacity.setStatus(_A)
class _ComponentStatusRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_ComponentStatusRack_Type.__name__=_C
_ComponentStatusRack_Object=MibTableColumn
componentStatusRack=_ComponentStatusRack_Object((1,3,6,1,4,1,2606,6,4,1,2,1,13),_ComponentStatusRack_Type())
componentStatusRack.setMaxAccess(_B)
if mibBuilder.loadTexts:componentStatusRack.setStatus(_A)
_RiZoneVariables_ObjectIdentity=ObjectIdentity
riZoneVariables=_RiZoneVariables_ObjectIdentity((1,3,6,1,4,1,2606,6,4,2))
_RiZoneNumberOfVariables_Type=Integer32
_RiZoneNumberOfVariables_Object=MibScalar
riZoneNumberOfVariables=_RiZoneNumberOfVariables_Object((1,3,6,1,4,1,2606,6,4,2,1),_RiZoneNumberOfVariables_Type())
riZoneNumberOfVariables.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneNumberOfVariables.setStatus(_A)
_RiZoneVariableTable_Object=MibTable
riZoneVariableTable=_RiZoneVariableTable_Object((1,3,6,1,4,1,2606,6,4,2,2))
if mibBuilder.loadTexts:riZoneVariableTable.setStatus(_A)
_RiZoneVariableEntry_Object=MibTableRow
riZoneVariableEntry=_RiZoneVariableEntry_Object((1,3,6,1,4,1,2606,6,4,2,2,1))
riZoneVariableEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:riZoneVariableEntry.setStatus(_A)
class _VariableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VariableIndex_Type.__name__=_C
_VariableIndex_Object=MibTableColumn
variableIndex=_VariableIndex_Object((1,3,6,1,4,1,2606,6,4,2,2,1,1),_VariableIndex_Type())
variableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:variableIndex.setStatus(_A)
_VariableId_Type=Integer32
_VariableId_Object=MibTableColumn
variableId=_VariableId_Object((1,3,6,1,4,1,2606,6,4,2,2,1,2),_VariableId_Type())
variableId.setMaxAccess(_B)
if mibBuilder.loadTexts:variableId.setStatus(_A)
class _VariableName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_VariableName_Type.__name__=_I
_VariableName_Object=MibTableColumn
variableName=_VariableName_Object((1,3,6,1,4,1,2606,6,4,2,2,1,3),_VariableName_Type())
variableName.setMaxAccess(_B)
if mibBuilder.loadTexts:variableName.setStatus(_A)
class _VariableMaintenanceGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64,128,256)));namedValues=NamedValues(*((_L,1),('cooling',2),('power',4),('rack',8),('monitoring',16),('remoting',32),('availability',64),('security',128),('capacity',256)))
_VariableMaintenanceGroup_Type.__name__=_C
_VariableMaintenanceGroup_Object=MibTableColumn
variableMaintenanceGroup=_VariableMaintenanceGroup_Object((1,3,6,1,4,1,2606,6,4,2,2,1,4),_VariableMaintenanceGroup_Type())
variableMaintenanceGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:variableMaintenanceGroup.setStatus(_A)
class _VariableMeasurand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,34,35,36,37)));namedValues=NamedValues(*((_L,1),('temperature',2),('current',3),('power',4),('effectivePower',5),('humidity',6),('voltage',7),('energy',8),('frequency',9),('access',10),('leakage',11),('percent',12),('rpm',13),('co2',14),('pue',15),('flow',16),('time',17),('costs',18),('imp',19),('heatCapacity',20),('constant',21),('temperatureDiff',22),('timespan',23),('cycles',24),('pulseRate',34),('pressure',35),('acceleration',36),('timeSpanTicks',37)))
_VariableMeasurand_Type.__name__=_C
_VariableMeasurand_Object=MibTableColumn
variableMeasurand=_VariableMeasurand_Object((1,3,6,1,4,1,2606,6,4,2,2,1,5),_VariableMeasurand_Type())
variableMeasurand.setMaxAccess(_B)
if mibBuilder.loadTexts:variableMeasurand.setStatus(_A)
_VariableParentId_Type=Integer32
_VariableParentId_Object=MibTableColumn
variableParentId=_VariableParentId_Object((1,3,6,1,4,1,2606,6,4,2,2,1,6),_VariableParentId_Type())
variableParentId.setMaxAccess(_B)
if mibBuilder.loadTexts:variableParentId.setStatus(_A)
class _VariableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('number',1),('string',2),('enum',3)))
_VariableType_Type.__name__=_C
_VariableType_Object=MibTableColumn
variableType=_VariableType_Object((1,3,6,1,4,1,2606,6,4,2,2,1,7),_VariableType_Type())
variableType.setMaxAccess(_B)
if mibBuilder.loadTexts:variableType.setStatus(_A)
class _VariableQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('good',2),('bad',3)))
_VariableQuality_Type.__name__=_C
_VariableQuality_Object=MibTableColumn
variableQuality=_VariableQuality_Object((1,3,6,1,4,1,2606,6,4,2,2,1,8),_VariableQuality_Type())
variableQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:variableQuality.setStatus(_A)
_VariableValueInt_Type=Integer32
_VariableValueInt_Object=MibTableColumn
variableValueInt=_VariableValueInt_Object((1,3,6,1,4,1,2606,6,4,2,2,1,9),_VariableValueInt_Type())
variableValueInt.setMaxAccess(_B)
if mibBuilder.loadTexts:variableValueInt.setStatus(_A)
class _VariableValueString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_VariableValueString_Type.__name__=_I
_VariableValueString_Object=MibTableColumn
variableValueString=_VariableValueString_Object((1,3,6,1,4,1,2606,6,4,2,2,1,10),_VariableValueString_Type())
variableValueString.setMaxAccess('read-write')
if mibBuilder.loadTexts:variableValueString.setStatus(_A)
class _VariableValueUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_VariableValueUnit_Type.__name__=_I
_VariableValueUnit_Object=MibTableColumn
variableValueUnit=_VariableValueUnit_Object((1,3,6,1,4,1,2606,6,4,2,2,1,11),_VariableValueUnit_Type())
variableValueUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:variableValueUnit.setStatus(_A)
_VariableDivisor_Type=Integer32
_VariableDivisor_Object=MibTableColumn
variableDivisor=_VariableDivisor_Object((1,3,6,1,4,1,2606,6,4,2,2,1,12),_VariableDivisor_Type())
variableDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:variableDivisor.setStatus(_A)
_VariableMultiplicator_Type=Integer32
_VariableMultiplicator_Object=MibTableColumn
variableMultiplicator=_VariableMultiplicator_Object((1,3,6,1,4,1,2606,6,4,2,2,1,13),_VariableMultiplicator_Type())
variableMultiplicator.setMaxAccess(_B)
if mibBuilder.loadTexts:variableMultiplicator.setStatus(_A)
class _RiZoneStatusAvailability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4),(_K,5)))
_RiZoneStatusAvailability_Type.__name__=_C
_RiZoneStatusAvailability_Object=MibScalar
riZoneStatusAvailability=_RiZoneStatusAvailability_Object((1,3,6,1,4,1,2606,6,4,3),_RiZoneStatusAvailability_Type())
riZoneStatusAvailability.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneStatusAvailability.setStatus(_A)
class _RiZoneStatusCooling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_RiZoneStatusCooling_Type.__name__=_C
_RiZoneStatusCooling_Object=MibScalar
riZoneStatusCooling=_RiZoneStatusCooling_Object((1,3,6,1,4,1,2606,6,4,4),_RiZoneStatusCooling_Type())
riZoneStatusCooling.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneStatusCooling.setStatus(_A)
class _RiZoneStatusPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_RiZoneStatusPower_Type.__name__=_C
_RiZoneStatusPower_Object=MibScalar
riZoneStatusPower=_RiZoneStatusPower_Object((1,3,6,1,4,1,2606,6,4,5),_RiZoneStatusPower_Type())
riZoneStatusPower.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneStatusPower.setStatus(_A)
class _RiZoneStatusMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_RiZoneStatusMonitoring_Type.__name__=_C
_RiZoneStatusMonitoring_Object=MibScalar
riZoneStatusMonitoring=_RiZoneStatusMonitoring_Object((1,3,6,1,4,1,2606,6,4,6),_RiZoneStatusMonitoring_Type())
riZoneStatusMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneStatusMonitoring.setStatus(_A)
class _RiZoneStatusSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_RiZoneStatusSecurity_Type.__name__=_C
_RiZoneStatusSecurity_Object=MibScalar
riZoneStatusSecurity=_RiZoneStatusSecurity_Object((1,3,6,1,4,1,2606,6,4,7),_RiZoneStatusSecurity_Type())
riZoneStatusSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneStatusSecurity.setStatus(_A)
class _RiZoneStatusCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_RiZoneStatusCapacity_Type.__name__=_C
_RiZoneStatusCapacity_Object=MibScalar
riZoneStatusCapacity=_RiZoneStatusCapacity_Object((1,3,6,1,4,1,2606,6,4,8),_RiZoneStatusCapacity_Type())
riZoneStatusCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneStatusCapacity.setStatus(_A)
class _RiZoneStatusRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_D,2),(_F,3),(_H,4)))
_RiZoneStatusRack_Type.__name__=_C
_RiZoneStatusRack_Object=MibScalar
riZoneStatusRack=_RiZoneStatusRack_Object((1,3,6,1,4,1,2606,6,4,9),_RiZoneStatusRack_Type())
riZoneStatusRack.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneStatusRack.setStatus(_A)
_RiZoneCustomDefines_ObjectIdentity=ObjectIdentity
riZoneCustomDefines=_RiZoneCustomDefines_ObjectIdentity((1,3,6,1,4,1,2606,6,5))
_RiZoneCustomDefinedTraps_ObjectIdentity=ObjectIdentity
riZoneCustomDefinedTraps=_RiZoneCustomDefinedTraps_ObjectIdentity((1,3,6,1,4,1,2606,6,5,1))
_RiZoneNumberOfTraps_Type=Integer32
_RiZoneNumberOfTraps_Object=MibScalar
riZoneNumberOfTraps=_RiZoneNumberOfTraps_Object((1,3,6,1,4,1,2606,6,5,1,1),_RiZoneNumberOfTraps_Type())
riZoneNumberOfTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:riZoneNumberOfTraps.setStatus(_A)
_RiZoneCustomDefinedTrapsTable_Object=MibTable
riZoneCustomDefinedTrapsTable=_RiZoneCustomDefinedTrapsTable_Object((1,3,6,1,4,1,2606,6,5,1,2))
if mibBuilder.loadTexts:riZoneCustomDefinedTrapsTable.setStatus(_A)
_RiZoneCustomDefinedTrapsEntry_Object=MibTableRow
riZoneCustomDefinedTrapsEntry=_RiZoneCustomDefinedTrapsEntry_Object((1,3,6,1,4,1,2606,6,5,1,2,1))
riZoneCustomDefinedTrapsEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:riZoneCustomDefinedTrapsEntry.setStatus(_A)
class _CustomDefinedTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CustomDefinedTrapIndex_Type.__name__=_C
_CustomDefinedTrapIndex_Object=MibTableColumn
customDefinedTrapIndex=_CustomDefinedTrapIndex_Object((1,3,6,1,4,1,2606,6,5,1,2,1,1),_CustomDefinedTrapIndex_Type())
customDefinedTrapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:customDefinedTrapIndex.setStatus(_A)
class _CdtMessageCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('na',1),('info',2),(_F,3),('error',4),(_D,5)))
_CdtMessageCategory_Type.__name__=_C
_CdtMessageCategory_Object=MibTableColumn
cdtMessageCategory=_CdtMessageCategory_Object((1,3,6,1,4,1,2606,6,5,1,2,1,2),_CdtMessageCategory_Type())
cdtMessageCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtMessageCategory.setStatus(_A)
class _CdtWorkflowId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CdtWorkflowId_Type.__name__=_C
_CdtWorkflowId_Object=MibTableColumn
cdtWorkflowId=_CdtWorkflowId_Object((1,3,6,1,4,1,2606,6,5,1,2,1,3),_CdtWorkflowId_Type())
cdtWorkflowId.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtWorkflowId.setStatus(_A)
class _CdtWorkflowName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CdtWorkflowName_Type.__name__=_I
_CdtWorkflowName_Object=MibTableColumn
cdtWorkflowName=_CdtWorkflowName_Object((1,3,6,1,4,1,2606,6,5,1,2,1,4),_CdtWorkflowName_Type())
cdtWorkflowName.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtWorkflowName.setStatus(_A)
class _CdtFlowElementId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CdtFlowElementId_Type.__name__=_I
_CdtFlowElementId_Object=MibTableColumn
cdtFlowElementId=_CdtFlowElementId_Object((1,3,6,1,4,1,2606,6,5,1,2,1,5),_CdtFlowElementId_Type())
cdtFlowElementId.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtFlowElementId.setStatus(_A)
class _CdtMessageText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CdtMessageText_Type.__name__=_I
_CdtMessageText_Object=MibTableColumn
cdtMessageText=_CdtMessageText_Object((1,3,6,1,4,1,2606,6,5,1,2,1,6),_CdtMessageText_Type())
cdtMessageText.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtMessageText.setStatus(_A)
class _CdtVariableId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CdtVariableId_Type.__name__=_C
_CdtVariableId_Object=MibTableColumn
cdtVariableId=_CdtVariableId_Object((1,3,6,1,4,1,2606,6,5,1,2,1,7),_CdtVariableId_Type())
cdtVariableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtVariableId.setStatus(_A)
class _CdtVariableName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CdtVariableName_Type.__name__=_I
_CdtVariableName_Object=MibTableColumn
cdtVariableName=_CdtVariableName_Object((1,3,6,1,4,1,2606,6,5,1,2,1,8),_CdtVariableName_Type())
cdtVariableName.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtVariableName.setStatus(_A)
class _CdtVariableValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CdtVariableValue_Type.__name__=_C
_CdtVariableValue_Object=MibTableColumn
cdtVariableValue=_CdtVariableValue_Object((1,3,6,1,4,1,2606,6,5,1,2,1,9),_CdtVariableValue_Type())
cdtVariableValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtVariableValue.setStatus(_A)
class _CdtVariableTranslation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CdtVariableTranslation_Type.__name__=_I
_CdtVariableTranslation_Object=MibTableColumn
cdtVariableTranslation=_CdtVariableTranslation_Object((1,3,6,1,4,1,2606,6,5,1,2,1,10),_CdtVariableTranslation_Type())
cdtVariableTranslation.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtVariableTranslation.setStatus(_A)
class _CdtVariableOwnerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CdtVariableOwnerId_Type.__name__=_C
_CdtVariableOwnerId_Object=MibTableColumn
cdtVariableOwnerId=_CdtVariableOwnerId_Object((1,3,6,1,4,1,2606,6,5,1,2,1,11),_CdtVariableOwnerId_Type())
cdtVariableOwnerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtVariableOwnerId.setStatus(_A)
class _CdtVariableOwnerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CdtVariableOwnerName_Type.__name__=_I
_CdtVariableOwnerName_Object=MibTableColumn
cdtVariableOwnerName=_CdtVariableOwnerName_Object((1,3,6,1,4,1,2606,6,5,1,2,1,12),_CdtVariableOwnerName_Type())
cdtVariableOwnerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cdtVariableOwnerName.setStatus(_A)
projectUpload=NotificationType((1,3,6,1,4,1,2606,6,0,1))
projectUpload.setObjects(*((_J,_O),(_J,_N),(_J,_M),(_E,_U),(_E,_V)))
if mibBuilder.loadTexts:projectUpload.setStatus('')
customDefinedTrap=NotificationType((1,3,6,1,4,1,2606,6,0,2))
customDefinedTrap.setObjects(*((_E,_W),(_E,_X),(_E,_Y),(_E,_Z),(_E,_a),(_E,_b),(_E,_c),(_E,_d),(_E,_e),(_E,_f)))
if mibBuilder.loadTexts:customDefinedTrap.setStatus('')
mibBuilder.exportSymbols(_E,**{'rittal':rittal,'riZone':riZone,'projectUpload':projectUpload,'customDefinedTrap':customDefinedTrap,'riZoneMibRev':riZoneMibRev,'riZoneMibMajRev':riZoneMibMajRev,'riZoneMibMinRev':riZoneMibMinRev,'riZoneMibCondition':riZoneMibCondition,'riZoneModules':riZoneModules,'riZoneCoreState':riZoneCoreState,'riZoneCoreVersion':riZoneCoreVersion,'riZoneProject':riZoneProject,_U:riZoneProjectName,_V:riZoneProjectChangeTime,'riZoneStatus':riZoneStatus,'riZoneComponents':riZoneComponents,'riZoneNumberOfComponents':riZoneNumberOfComponents,'riZoneComponentTable':riZoneComponentTable,'riZoneComponentEntry':riZoneComponentEntry,_R:componentIndex,'componentId':componentId,'componentName':componentName,'componentType':componentType,'componentParent':componentParent,'componentStatusTotal':componentStatusTotal,'componentStatusAvailability':componentStatusAvailability,'componentStatusCooling':componentStatusCooling,'componentStatusPower':componentStatusPower,'componentStatusMonitoring':componentStatusMonitoring,'componentStatusSecurity':componentStatusSecurity,'componentStatusCapacity':componentStatusCapacity,'componentStatusRack':componentStatusRack,'riZoneVariables':riZoneVariables,'riZoneNumberOfVariables':riZoneNumberOfVariables,'riZoneVariableTable':riZoneVariableTable,'riZoneVariableEntry':riZoneVariableEntry,_S:variableIndex,'variableId':variableId,'variableName':variableName,'variableMaintenanceGroup':variableMaintenanceGroup,'variableMeasurand':variableMeasurand,'variableParentId':variableParentId,'variableType':variableType,'variableQuality':variableQuality,'variableValueInt':variableValueInt,'variableValueString':variableValueString,'variableValueUnit':variableValueUnit,'variableDivisor':variableDivisor,'variableMultiplicator':variableMultiplicator,'riZoneStatusAvailability':riZoneStatusAvailability,'riZoneStatusCooling':riZoneStatusCooling,'riZoneStatusPower':riZoneStatusPower,'riZoneStatusMonitoring':riZoneStatusMonitoring,'riZoneStatusSecurity':riZoneStatusSecurity,'riZoneStatusCapacity':riZoneStatusCapacity,'riZoneStatusRack':riZoneStatusRack,'riZoneCustomDefines':riZoneCustomDefines,'riZoneCustomDefinedTraps':riZoneCustomDefinedTraps,'riZoneNumberOfTraps':riZoneNumberOfTraps,'riZoneCustomDefinedTrapsTable':riZoneCustomDefinedTrapsTable,'riZoneCustomDefinedTrapsEntry':riZoneCustomDefinedTrapsEntry,_T:customDefinedTrapIndex,_W:cdtMessageCategory,_X:cdtWorkflowId,_Y:cdtWorkflowName,'cdtFlowElementId':cdtFlowElementId,_Z:cdtMessageText,_a:cdtVariableId,_b:cdtVariableName,_c:cdtVariableValue,_d:cdtVariableTranslation,_e:cdtVariableOwnerId,_f:cdtVariableOwnerName})