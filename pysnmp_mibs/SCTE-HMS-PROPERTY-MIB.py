_X='discreteAlarmsGroup'
_W='currentAlarmsGroup'
_V='analogAlarmsGroup'
_U='currentAlarmAlarmValue'
_T='currentAlarmAlarmState'
_S='discreteAlarmState'
_R='discreteAlarmEnable'
_Q='analogAlarmDeadband'
_P='analogAlarmLOLO'
_O='analogAlarmLO'
_N='analogAlarmHI'
_M='analogAlarmHIHI'
_L='currentAlarmState'
_K='alarmEnable'
_J='OctetString'
_I='discreteAlarmValue'
_H='discreteParameterOID'
_G='currentAlarmOID'
_F='parameterOID'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='SCTE-HMS-PROPERTY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
propertyIdent,=mibBuilder.importSymbols('SCTE-HMS-ROOTS','propertyIdent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
propertyModuleIdentity=ModuleIdentity((1,3,6,1,4,1,5591,1,1,4))
if mibBuilder.loadTexts:propertyModuleIdentity.setRevisions(('2004-03-29 00:00',))
_PropertyTable_Object=MibTable
propertyTable=_PropertyTable_Object((1,3,6,1,4,1,5591,1,1,1))
if mibBuilder.loadTexts:propertyTable.setStatus(_A)
_PropertyEntry_Object=MibTableRow
propertyEntry=_PropertyEntry_Object((1,3,6,1,4,1,5591,1,1,1,1))
propertyEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:propertyEntry.setStatus(_A)
_ParameterOID_Type=ObjectIdentifier
_ParameterOID_Object=MibTableColumn
parameterOID=_ParameterOID_Object((1,3,6,1,4,1,5591,1,1,1,1,1),_ParameterOID_Type())
parameterOID.setMaxAccess(_C)
if mibBuilder.loadTexts:parameterOID.setStatus(_A)
class _AlarmEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_AlarmEnable_Type.__name__=_J
_AlarmEnable_Object=MibTableColumn
alarmEnable=_AlarmEnable_Object((1,3,6,1,4,1,5591,1,1,1,1,2),_AlarmEnable_Type())
alarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmEnable.setStatus(_A)
class _CurrentAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('casNominal',1),('casHIHI',2),('casHI',3),('casLO',4),('casLOLO',5)))
_CurrentAlarmState_Type.__name__=_E
_CurrentAlarmState_Object=MibTableColumn
currentAlarmState=_CurrentAlarmState_Object((1,3,6,1,4,1,5591,1,1,1,1,3),_CurrentAlarmState_Type())
currentAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmState.setStatus(_A)
_AnalogAlarmHIHI_Type=Integer32
_AnalogAlarmHIHI_Object=MibTableColumn
analogAlarmHIHI=_AnalogAlarmHIHI_Object((1,3,6,1,4,1,5591,1,1,1,1,4),_AnalogAlarmHIHI_Type())
analogAlarmHIHI.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmHIHI.setStatus(_A)
_AnalogAlarmHI_Type=Integer32
_AnalogAlarmHI_Object=MibTableColumn
analogAlarmHI=_AnalogAlarmHI_Object((1,3,6,1,4,1,5591,1,1,1,1,5),_AnalogAlarmHI_Type())
analogAlarmHI.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmHI.setStatus(_A)
_AnalogAlarmLO_Type=Integer32
_AnalogAlarmLO_Object=MibTableColumn
analogAlarmLO=_AnalogAlarmLO_Object((1,3,6,1,4,1,5591,1,1,1,1,6),_AnalogAlarmLO_Type())
analogAlarmLO.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmLO.setStatus(_A)
_AnalogAlarmLOLO_Type=Integer32
_AnalogAlarmLOLO_Object=MibTableColumn
analogAlarmLOLO=_AnalogAlarmLOLO_Object((1,3,6,1,4,1,5591,1,1,1,1,7),_AnalogAlarmLOLO_Type())
analogAlarmLOLO.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmLOLO.setStatus(_A)
_AnalogAlarmDeadband_Type=Integer32
_AnalogAlarmDeadband_Object=MibTableColumn
analogAlarmDeadband=_AnalogAlarmDeadband_Object((1,3,6,1,4,1,5591,1,1,1,1,9),_AnalogAlarmDeadband_Type())
analogAlarmDeadband.setMaxAccess(_D)
if mibBuilder.loadTexts:analogAlarmDeadband.setStatus(_A)
_CurrentAlarmTable_Object=MibTable
currentAlarmTable=_CurrentAlarmTable_Object((1,3,6,1,4,1,5591,1,1,2))
if mibBuilder.loadTexts:currentAlarmTable.setStatus(_A)
_CurrentAlarmEntry_Object=MibTableRow
currentAlarmEntry=_CurrentAlarmEntry_Object((1,3,6,1,4,1,5591,1,1,2,1))
currentAlarmEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:currentAlarmEntry.setStatus(_A)
_CurrentAlarmOID_Type=ObjectIdentifier
_CurrentAlarmOID_Object=MibTableColumn
currentAlarmOID=_CurrentAlarmOID_Object((1,3,6,1,4,1,5591,1,1,2,1,1),_CurrentAlarmOID_Type())
currentAlarmOID.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmOID.setStatus(_A)
class _CurrentAlarmAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*(('caasHIHI',2),('caasHI',3),('caasLO',4),('caasLOLO',5),('caasDiscreteMajor',6),('caasDiscreteMinor',7)))
_CurrentAlarmAlarmState_Type.__name__=_E
_CurrentAlarmAlarmState_Object=MibTableColumn
currentAlarmAlarmState=_CurrentAlarmAlarmState_Object((1,3,6,1,4,1,5591,1,1,2,1,2),_CurrentAlarmAlarmState_Type())
currentAlarmAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmAlarmState.setStatus(_A)
_CurrentAlarmAlarmValue_Type=Integer32
_CurrentAlarmAlarmValue_Object=MibTableColumn
currentAlarmAlarmValue=_CurrentAlarmAlarmValue_Object((1,3,6,1,4,1,5591,1,1,2,1,3),_CurrentAlarmAlarmValue_Type())
currentAlarmAlarmValue.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmAlarmValue.setStatus(_A)
_DiscretePropertyTable_Object=MibTable
discretePropertyTable=_DiscretePropertyTable_Object((1,3,6,1,4,1,5591,1,1,3))
if mibBuilder.loadTexts:discretePropertyTable.setStatus(_A)
_DiscretePropertyEntry_Object=MibTableRow
discretePropertyEntry=_DiscretePropertyEntry_Object((1,3,6,1,4,1,5591,1,1,3,1))
discretePropertyEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:discretePropertyEntry.setStatus(_A)
_DiscreteParameterOID_Type=ObjectIdentifier
_DiscreteParameterOID_Object=MibTableColumn
discreteParameterOID=_DiscreteParameterOID_Object((1,3,6,1,4,1,5591,1,1,3,1,1),_DiscreteParameterOID_Type())
discreteParameterOID.setMaxAccess(_C)
if mibBuilder.loadTexts:discreteParameterOID.setStatus(_A)
class _DiscreteAlarmValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DiscreteAlarmValue_Type.__name__=_E
_DiscreteAlarmValue_Object=MibTableColumn
discreteAlarmValue=_DiscreteAlarmValue_Object((1,3,6,1,4,1,5591,1,1,3,1,2),_DiscreteAlarmValue_Type())
discreteAlarmValue.setMaxAccess(_C)
if mibBuilder.loadTexts:discreteAlarmValue.setStatus(_A)
class _DiscreteAlarmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('enableMajor',2),('enableMinor',3)))
_DiscreteAlarmEnable_Type.__name__=_E
_DiscreteAlarmEnable_Object=MibTableColumn
discreteAlarmEnable=_DiscreteAlarmEnable_Object((1,3,6,1,4,1,5591,1,1,3,1,3),_DiscreteAlarmEnable_Type())
discreteAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:discreteAlarmEnable.setStatus(_A)
class _DiscreteAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,7)));namedValues=NamedValues(*(('dasNominal',1),('dasDiscreteMajor',6),('dasDiscreteMinor',7)))
_DiscreteAlarmState_Type.__name__=_E
_DiscreteAlarmState_Object=MibTableColumn
discreteAlarmState=_DiscreteAlarmState_Object((1,3,6,1,4,1,5591,1,1,3,1,4),_DiscreteAlarmState_Type())
discreteAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:discreteAlarmState.setStatus(_A)
_PropertyMIBConformance_ObjectIdentity=ObjectIdentity
propertyMIBConformance=_PropertyMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,1,4,1))
_PropertyMIBCompliances_ObjectIdentity=ObjectIdentity
propertyMIBCompliances=_PropertyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,1,4,1,1))
_PropertyMIBGroups_ObjectIdentity=ObjectIdentity
propertyMIBGroups=_PropertyMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,1,4,1,2))
analogAlarmsGroup=ObjectGroup((1,3,6,1,4,1,5591,1,1,4,1,2,1))
analogAlarmsGroup.setObjects(*((_B,_F),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:analogAlarmsGroup.setStatus(_A)
discreteAlarmsGroup=ObjectGroup((1,3,6,1,4,1,5591,1,1,4,1,2,2))
discreteAlarmsGroup.setObjects(*((_B,_H),(_B,_I),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:discreteAlarmsGroup.setStatus(_A)
currentAlarmsGroup=ObjectGroup((1,3,6,1,4,1,5591,1,1,4,1,2,3))
currentAlarmsGroup.setObjects(*((_B,_T),(_B,_U),(_B,_G)))
if mibBuilder.loadTexts:currentAlarmsGroup.setStatus(_A)
propertyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,1,4,1,1,1))
propertyMIBCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:propertyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'propertyTable':propertyTable,'propertyEntry':propertyEntry,_F:parameterOID,_K:alarmEnable,_L:currentAlarmState,_M:analogAlarmHIHI,_N:analogAlarmHI,_O:analogAlarmLO,_P:analogAlarmLOLO,_Q:analogAlarmDeadband,'currentAlarmTable':currentAlarmTable,'currentAlarmEntry':currentAlarmEntry,_G:currentAlarmOID,_T:currentAlarmAlarmState,_U:currentAlarmAlarmValue,'discretePropertyTable':discretePropertyTable,'discretePropertyEntry':discretePropertyEntry,_H:discreteParameterOID,_I:discreteAlarmValue,_R:discreteAlarmEnable,_S:discreteAlarmState,'propertyModuleIdentity':propertyModuleIdentity,'propertyMIBConformance':propertyMIBConformance,'propertyMIBCompliances':propertyMIBCompliances,'propertyMIBCompliance':propertyMIBCompliance,'propertyMIBGroups':propertyMIBGroups,_V:analogAlarmsGroup,_X:discreteAlarmsGroup,_W:currentAlarmsGroup})