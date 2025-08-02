_f='cHcAlarmNotificationsGroup'
_e='cHcAlarmCapabilitiesGroup'
_d='cHcAlarmControlGroup'
_c='cHcFallingAlarm'
_b='cHcRisingAlarm'
_a='cHcAlarmCapabilities'
_Z='cHcAlarmStatus'
_Y='cHcAlarmStorageType'
_X='cHcAlarmOwner'
_W='cHcAlarmValueFailedAttempts'
_V='cHcAlarmStartupAlarm'
_U='cHcAlarmInterval'
_T='cHcAlarmIndex'
_S='rmonEventGroup'
_R='RMON-MIB'
_Q='cHcAlarmFallingEventIndex'
_P='cHcAlarmRisingEventIndex'
_O='cHcAlarmFallingThrsholdValStatus'
_N='cHcAlarmFallingThreshAbsValueHi'
_M='cHcAlarmFallingThreshAbsValueLo'
_L='cHcAlarmRisingThresholdValStatus'
_K='cHcAlarmRisingThreshAbsValueHi'
_J='cHcAlarmRisingThreshAbsValueLo'
_I='cHcAlarmValueStatus'
_H='cHcAlarmAbsValue'
_G='cHcAlarmSampleType'
_F='cHcAlarmVariable'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='current'
_A='CISCO-HC-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
OwnerString,rmonEventGroup=mibBuilder.importSymbols(_R,'OwnerString',_S)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','VariablePointer')
ciscoHcAlarmMIB=ModuleIdentity((1,3,6,1,4,1,9,10,93))
if mibBuilder.loadTexts:ciscoHcAlarmMIB.setRevisions(('2002-10-05 00:00',))
class CHcValueStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valueNotAvailable',1),('valuePositive',2),('valueNegative',3)))
_CHcAlarmObjects_ObjectIdentity=ObjectIdentity
cHcAlarmObjects=_CHcAlarmObjects_ObjectIdentity((1,3,6,1,4,1,9,10,93,1))
_CHcAlarmControlObjects_ObjectIdentity=ObjectIdentity
cHcAlarmControlObjects=_CHcAlarmControlObjects_ObjectIdentity((1,3,6,1,4,1,9,10,93,1,1))
_CHcAlarmTable_Object=MibTable
cHcAlarmTable=_CHcAlarmTable_Object((1,3,6,1,4,1,9,10,93,1,1,1))
if mibBuilder.loadTexts:cHcAlarmTable.setStatus(_B)
_CHcAlarmEntry_Object=MibTableRow
cHcAlarmEntry=_CHcAlarmEntry_Object((1,3,6,1,4,1,9,10,93,1,1,1,1))
cHcAlarmEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:cHcAlarmEntry.setStatus(_B)
class _CHcAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CHcAlarmIndex_Type.__name__=_D
_CHcAlarmIndex_Object=MibTableColumn
cHcAlarmIndex=_CHcAlarmIndex_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,1),_CHcAlarmIndex_Type())
cHcAlarmIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cHcAlarmIndex.setStatus(_B)
class _CHcAlarmInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CHcAlarmInterval_Type.__name__=_D
_CHcAlarmInterval_Object=MibTableColumn
cHcAlarmInterval=_CHcAlarmInterval_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,2),_CHcAlarmInterval_Type())
cHcAlarmInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmInterval.setStatus(_B)
if mibBuilder.loadTexts:cHcAlarmInterval.setUnits('seconds')
_CHcAlarmVariable_Type=VariablePointer
_CHcAlarmVariable_Object=MibTableColumn
cHcAlarmVariable=_CHcAlarmVariable_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,3),_CHcAlarmVariable_Type())
cHcAlarmVariable.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmVariable.setStatus(_B)
class _CHcAlarmSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2)))
_CHcAlarmSampleType_Type.__name__=_D
_CHcAlarmSampleType_Object=MibTableColumn
cHcAlarmSampleType=_CHcAlarmSampleType_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,4),_CHcAlarmSampleType_Type())
cHcAlarmSampleType.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmSampleType.setStatus(_B)
_CHcAlarmAbsValue_Type=CounterBasedGauge64
_CHcAlarmAbsValue_Object=MibTableColumn
cHcAlarmAbsValue=_CHcAlarmAbsValue_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,5),_CHcAlarmAbsValue_Type())
cHcAlarmAbsValue.setMaxAccess(_E)
if mibBuilder.loadTexts:cHcAlarmAbsValue.setStatus(_B)
_CHcAlarmValueStatus_Type=CHcValueStatus
_CHcAlarmValueStatus_Object=MibTableColumn
cHcAlarmValueStatus=_CHcAlarmValueStatus_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,6),_CHcAlarmValueStatus_Type())
cHcAlarmValueStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cHcAlarmValueStatus.setStatus(_B)
class _CHcAlarmStartupAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
_CHcAlarmStartupAlarm_Type.__name__=_D
_CHcAlarmStartupAlarm_Object=MibTableColumn
cHcAlarmStartupAlarm=_CHcAlarmStartupAlarm_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,7),_CHcAlarmStartupAlarm_Type())
cHcAlarmStartupAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmStartupAlarm.setStatus(_B)
_CHcAlarmRisingThreshAbsValueLo_Type=Unsigned32
_CHcAlarmRisingThreshAbsValueLo_Object=MibTableColumn
cHcAlarmRisingThreshAbsValueLo=_CHcAlarmRisingThreshAbsValueLo_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,8),_CHcAlarmRisingThreshAbsValueLo_Type())
cHcAlarmRisingThreshAbsValueLo.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmRisingThreshAbsValueLo.setStatus(_B)
_CHcAlarmRisingThreshAbsValueHi_Type=Unsigned32
_CHcAlarmRisingThreshAbsValueHi_Object=MibTableColumn
cHcAlarmRisingThreshAbsValueHi=_CHcAlarmRisingThreshAbsValueHi_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,9),_CHcAlarmRisingThreshAbsValueHi_Type())
cHcAlarmRisingThreshAbsValueHi.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmRisingThreshAbsValueHi.setStatus(_B)
_CHcAlarmRisingThresholdValStatus_Type=CHcValueStatus
_CHcAlarmRisingThresholdValStatus_Object=MibTableColumn
cHcAlarmRisingThresholdValStatus=_CHcAlarmRisingThresholdValStatus_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,10),_CHcAlarmRisingThresholdValStatus_Type())
cHcAlarmRisingThresholdValStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmRisingThresholdValStatus.setStatus(_B)
_CHcAlarmFallingThreshAbsValueLo_Type=Unsigned32
_CHcAlarmFallingThreshAbsValueLo_Object=MibTableColumn
cHcAlarmFallingThreshAbsValueLo=_CHcAlarmFallingThreshAbsValueLo_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,11),_CHcAlarmFallingThreshAbsValueLo_Type())
cHcAlarmFallingThreshAbsValueLo.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmFallingThreshAbsValueLo.setStatus(_B)
_CHcAlarmFallingThreshAbsValueHi_Type=Unsigned32
_CHcAlarmFallingThreshAbsValueHi_Object=MibTableColumn
cHcAlarmFallingThreshAbsValueHi=_CHcAlarmFallingThreshAbsValueHi_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,12),_CHcAlarmFallingThreshAbsValueHi_Type())
cHcAlarmFallingThreshAbsValueHi.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmFallingThreshAbsValueHi.setStatus(_B)
_CHcAlarmFallingThrsholdValStatus_Type=CHcValueStatus
_CHcAlarmFallingThrsholdValStatus_Object=MibTableColumn
cHcAlarmFallingThrsholdValStatus=_CHcAlarmFallingThrsholdValStatus_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,13),_CHcAlarmFallingThrsholdValStatus_Type())
cHcAlarmFallingThrsholdValStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmFallingThrsholdValStatus.setStatus(_B)
class _CHcAlarmRisingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CHcAlarmRisingEventIndex_Type.__name__=_D
_CHcAlarmRisingEventIndex_Object=MibTableColumn
cHcAlarmRisingEventIndex=_CHcAlarmRisingEventIndex_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,14),_CHcAlarmRisingEventIndex_Type())
cHcAlarmRisingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmRisingEventIndex.setStatus(_B)
class _CHcAlarmFallingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CHcAlarmFallingEventIndex_Type.__name__=_D
_CHcAlarmFallingEventIndex_Object=MibTableColumn
cHcAlarmFallingEventIndex=_CHcAlarmFallingEventIndex_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,15),_CHcAlarmFallingEventIndex_Type())
cHcAlarmFallingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmFallingEventIndex.setStatus(_B)
_CHcAlarmValueFailedAttempts_Type=Counter32
_CHcAlarmValueFailedAttempts_Object=MibTableColumn
cHcAlarmValueFailedAttempts=_CHcAlarmValueFailedAttempts_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,16),_CHcAlarmValueFailedAttempts_Type())
cHcAlarmValueFailedAttempts.setMaxAccess(_E)
if mibBuilder.loadTexts:cHcAlarmValueFailedAttempts.setStatus(_B)
_CHcAlarmOwner_Type=OwnerString
_CHcAlarmOwner_Object=MibTableColumn
cHcAlarmOwner=_CHcAlarmOwner_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,17),_CHcAlarmOwner_Type())
cHcAlarmOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmOwner.setStatus(_B)
_CHcAlarmStorageType_Type=StorageType
_CHcAlarmStorageType_Object=MibTableColumn
cHcAlarmStorageType=_CHcAlarmStorageType_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,18),_CHcAlarmStorageType_Type())
cHcAlarmStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmStorageType.setStatus(_B)
_CHcAlarmStatus_Type=RowStatus
_CHcAlarmStatus_Object=MibTableColumn
cHcAlarmStatus=_CHcAlarmStatus_Object((1,3,6,1,4,1,9,10,93,1,1,1,1,19),_CHcAlarmStatus_Type())
cHcAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cHcAlarmStatus.setStatus(_B)
_CHcAlarmCapabilitiesObjects_ObjectIdentity=ObjectIdentity
cHcAlarmCapabilitiesObjects=_CHcAlarmCapabilitiesObjects_ObjectIdentity((1,3,6,1,4,1,9,10,93,1,2))
class _CHcAlarmCapabilities_Type(Bits):namedValues=NamedValues(*(('cHcAlarmCreation',0),('cHcAlarmNvStorage',1)))
_CHcAlarmCapabilities_Type.__name__='Bits'
_CHcAlarmCapabilities_Object=MibScalar
cHcAlarmCapabilities=_CHcAlarmCapabilities_Object((1,3,6,1,4,1,9,10,93,1,2,1),_CHcAlarmCapabilities_Type())
cHcAlarmCapabilities.setMaxAccess(_E)
if mibBuilder.loadTexts:cHcAlarmCapabilities.setStatus(_B)
_CHcAlarmNotifications_ObjectIdentity=ObjectIdentity
cHcAlarmNotifications=_CHcAlarmNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,93,2))
_CHcAlarmNotifPrefix_ObjectIdentity=ObjectIdentity
cHcAlarmNotifPrefix=_CHcAlarmNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,93,2,0))
_CHcAlarmConformance_ObjectIdentity=ObjectIdentity
cHcAlarmConformance=_CHcAlarmConformance_ObjectIdentity((1,3,6,1,4,1,9,10,93,3))
_CHcAlarmCompliances_ObjectIdentity=ObjectIdentity
cHcAlarmCompliances=_CHcAlarmCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,93,3,1))
_CHcAlarmGroups_ObjectIdentity=ObjectIdentity
cHcAlarmGroups=_CHcAlarmGroups_ObjectIdentity((1,3,6,1,4,1,9,10,93,3,2))
cHcAlarmControlGroup=ObjectGroup((1,3,6,1,4,1,9,10,93,3,2,1))
cHcAlarmControlGroup.setObjects(*((_A,_U),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_V),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cHcAlarmControlGroup.setStatus(_B)
cHcAlarmCapabilitiesGroup=ObjectGroup((1,3,6,1,4,1,9,10,93,3,2,2))
cHcAlarmCapabilitiesGroup.setObjects((_A,_a))
if mibBuilder.loadTexts:cHcAlarmCapabilitiesGroup.setStatus(_B)
cHcRisingAlarm=NotificationType((1,3,6,1,4,1,9,10,93,2,0,1))
cHcRisingAlarm.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_P)))
if mibBuilder.loadTexts:cHcRisingAlarm.setStatus(_B)
cHcFallingAlarm=NotificationType((1,3,6,1,4,1,9,10,93,2,0,2))
cHcFallingAlarm.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_M),(_A,_N),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:cHcFallingAlarm.setStatus(_B)
cHcAlarmNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,10,93,3,2,3))
cHcAlarmNotificationsGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:cHcAlarmNotificationsGroup.setStatus(_B)
cHcAlarmCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,93,3,1,1))
cHcAlarmCompliance.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_R,_S)))
if mibBuilder.loadTexts:cHcAlarmCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CHcValueStatus':CHcValueStatus,'ciscoHcAlarmMIB':ciscoHcAlarmMIB,'cHcAlarmObjects':cHcAlarmObjects,'cHcAlarmControlObjects':cHcAlarmControlObjects,'cHcAlarmTable':cHcAlarmTable,'cHcAlarmEntry':cHcAlarmEntry,_T:cHcAlarmIndex,_U:cHcAlarmInterval,_F:cHcAlarmVariable,_G:cHcAlarmSampleType,_H:cHcAlarmAbsValue,_I:cHcAlarmValueStatus,_V:cHcAlarmStartupAlarm,_J:cHcAlarmRisingThreshAbsValueLo,_K:cHcAlarmRisingThreshAbsValueHi,_L:cHcAlarmRisingThresholdValStatus,_M:cHcAlarmFallingThreshAbsValueLo,_N:cHcAlarmFallingThreshAbsValueHi,_O:cHcAlarmFallingThrsholdValStatus,_P:cHcAlarmRisingEventIndex,_Q:cHcAlarmFallingEventIndex,_W:cHcAlarmValueFailedAttempts,_X:cHcAlarmOwner,_Y:cHcAlarmStorageType,_Z:cHcAlarmStatus,'cHcAlarmCapabilitiesObjects':cHcAlarmCapabilitiesObjects,_a:cHcAlarmCapabilities,'cHcAlarmNotifications':cHcAlarmNotifications,'cHcAlarmNotifPrefix':cHcAlarmNotifPrefix,_b:cHcRisingAlarm,_c:cHcFallingAlarm,'cHcAlarmConformance':cHcAlarmConformance,'cHcAlarmCompliances':cHcAlarmCompliances,'cHcAlarmCompliance':cHcAlarmCompliance,'cHcAlarmGroups':cHcAlarmGroups,_d:cHcAlarmControlGroup,_e:cHcAlarmCapabilitiesGroup,_f:cHcAlarmNotificationsGroup})