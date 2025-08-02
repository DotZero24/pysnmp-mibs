_f='hcAlarmNotificationsGroup'
_e='hcAlarmCapabilitiesGroup'
_d='hcAlarmControlGroup'
_c='hcFallingAlarm'
_b='hcRisingAlarm'
_a='hcAlarmCapabilities'
_Z='hcAlarmStatus'
_Y='hcAlarmStorageType'
_X='hcAlarmOwner'
_W='hcAlarmValueFailedAttempts'
_V='hcAlarmStartupAlarm'
_U='hcAlarmInterval'
_T='hcAlarmIndex'
_S='rmonEventGroup'
_R='RMON-MIB'
_Q='hcAlarmFallingEventIndex'
_P='hcAlarmRisingEventIndex'
_O='hcAlarmFallingThresholdValStatus'
_N='hcAlarmFallingThreshAbsValueHi'
_M='hcAlarmFallingThreshAbsValueLo'
_L='hcAlarmRisingThresholdValStatus'
_K='hcAlarmRisingThreshAbsValueHi'
_J='hcAlarmRisingThreshAbsValueLo'
_I='hcAlarmValueStatus'
_H='hcAlarmAbsValue'
_G='hcAlarmSampleType'
_F='hcAlarmVariable'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='current'
_A='HC-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
OwnerString,rmon,rmonEventGroup=mibBuilder.importSymbols(_R,'OwnerString','rmon',_S)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','VariablePointer')
hcAlarmMIB=ModuleIdentity((1,3,6,1,2,1,16,29))
if mibBuilder.loadTexts:hcAlarmMIB.setRevisions(('2002-12-16 00:00',))
class HcValueStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valueNotAvailable',1),('valuePositive',2),('valueNegative',3)))
_HcAlarmObjects_ObjectIdentity=ObjectIdentity
hcAlarmObjects=_HcAlarmObjects_ObjectIdentity((1,3,6,1,2,1,16,29,1))
_HcAlarmControlObjects_ObjectIdentity=ObjectIdentity
hcAlarmControlObjects=_HcAlarmControlObjects_ObjectIdentity((1,3,6,1,2,1,16,29,1,1))
_HcAlarmTable_Object=MibTable
hcAlarmTable=_HcAlarmTable_Object((1,3,6,1,2,1,16,29,1,1,1))
if mibBuilder.loadTexts:hcAlarmTable.setStatus(_B)
_HcAlarmEntry_Object=MibTableRow
hcAlarmEntry=_HcAlarmEntry_Object((1,3,6,1,2,1,16,29,1,1,1,1))
hcAlarmEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:hcAlarmEntry.setStatus(_B)
class _HcAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HcAlarmIndex_Type.__name__=_D
_HcAlarmIndex_Object=MibTableColumn
hcAlarmIndex=_HcAlarmIndex_Object((1,3,6,1,2,1,16,29,1,1,1,1,1),_HcAlarmIndex_Type())
hcAlarmIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hcAlarmIndex.setStatus(_B)
class _HcAlarmInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HcAlarmInterval_Type.__name__=_D
_HcAlarmInterval_Object=MibTableColumn
hcAlarmInterval=_HcAlarmInterval_Object((1,3,6,1,2,1,16,29,1,1,1,1,2),_HcAlarmInterval_Type())
hcAlarmInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmInterval.setStatus(_B)
if mibBuilder.loadTexts:hcAlarmInterval.setUnits('seconds')
_HcAlarmVariable_Type=VariablePointer
_HcAlarmVariable_Object=MibTableColumn
hcAlarmVariable=_HcAlarmVariable_Object((1,3,6,1,2,1,16,29,1,1,1,1,3),_HcAlarmVariable_Type())
hcAlarmVariable.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmVariable.setStatus(_B)
class _HcAlarmSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2)))
_HcAlarmSampleType_Type.__name__=_D
_HcAlarmSampleType_Object=MibTableColumn
hcAlarmSampleType=_HcAlarmSampleType_Object((1,3,6,1,2,1,16,29,1,1,1,1,4),_HcAlarmSampleType_Type())
hcAlarmSampleType.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmSampleType.setStatus(_B)
_HcAlarmAbsValue_Type=CounterBasedGauge64
_HcAlarmAbsValue_Object=MibTableColumn
hcAlarmAbsValue=_HcAlarmAbsValue_Object((1,3,6,1,2,1,16,29,1,1,1,1,5),_HcAlarmAbsValue_Type())
hcAlarmAbsValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hcAlarmAbsValue.setStatus(_B)
_HcAlarmValueStatus_Type=HcValueStatus
_HcAlarmValueStatus_Object=MibTableColumn
hcAlarmValueStatus=_HcAlarmValueStatus_Object((1,3,6,1,2,1,16,29,1,1,1,1,6),_HcAlarmValueStatus_Type())
hcAlarmValueStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hcAlarmValueStatus.setStatus(_B)
class _HcAlarmStartupAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
_HcAlarmStartupAlarm_Type.__name__=_D
_HcAlarmStartupAlarm_Object=MibTableColumn
hcAlarmStartupAlarm=_HcAlarmStartupAlarm_Object((1,3,6,1,2,1,16,29,1,1,1,1,7),_HcAlarmStartupAlarm_Type())
hcAlarmStartupAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmStartupAlarm.setStatus(_B)
_HcAlarmRisingThreshAbsValueLo_Type=Unsigned32
_HcAlarmRisingThreshAbsValueLo_Object=MibTableColumn
hcAlarmRisingThreshAbsValueLo=_HcAlarmRisingThreshAbsValueLo_Object((1,3,6,1,2,1,16,29,1,1,1,1,8),_HcAlarmRisingThreshAbsValueLo_Type())
hcAlarmRisingThreshAbsValueLo.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmRisingThreshAbsValueLo.setStatus(_B)
_HcAlarmRisingThreshAbsValueHi_Type=Unsigned32
_HcAlarmRisingThreshAbsValueHi_Object=MibTableColumn
hcAlarmRisingThreshAbsValueHi=_HcAlarmRisingThreshAbsValueHi_Object((1,3,6,1,2,1,16,29,1,1,1,1,9),_HcAlarmRisingThreshAbsValueHi_Type())
hcAlarmRisingThreshAbsValueHi.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmRisingThreshAbsValueHi.setStatus(_B)
_HcAlarmRisingThresholdValStatus_Type=HcValueStatus
_HcAlarmRisingThresholdValStatus_Object=MibTableColumn
hcAlarmRisingThresholdValStatus=_HcAlarmRisingThresholdValStatus_Object((1,3,6,1,2,1,16,29,1,1,1,1,10),_HcAlarmRisingThresholdValStatus_Type())
hcAlarmRisingThresholdValStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmRisingThresholdValStatus.setStatus(_B)
_HcAlarmFallingThreshAbsValueLo_Type=Unsigned32
_HcAlarmFallingThreshAbsValueLo_Object=MibTableColumn
hcAlarmFallingThreshAbsValueLo=_HcAlarmFallingThreshAbsValueLo_Object((1,3,6,1,2,1,16,29,1,1,1,1,11),_HcAlarmFallingThreshAbsValueLo_Type())
hcAlarmFallingThreshAbsValueLo.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmFallingThreshAbsValueLo.setStatus(_B)
_HcAlarmFallingThreshAbsValueHi_Type=Unsigned32
_HcAlarmFallingThreshAbsValueHi_Object=MibTableColumn
hcAlarmFallingThreshAbsValueHi=_HcAlarmFallingThreshAbsValueHi_Object((1,3,6,1,2,1,16,29,1,1,1,1,12),_HcAlarmFallingThreshAbsValueHi_Type())
hcAlarmFallingThreshAbsValueHi.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmFallingThreshAbsValueHi.setStatus(_B)
_HcAlarmFallingThresholdValStatus_Type=HcValueStatus
_HcAlarmFallingThresholdValStatus_Object=MibTableColumn
hcAlarmFallingThresholdValStatus=_HcAlarmFallingThresholdValStatus_Object((1,3,6,1,2,1,16,29,1,1,1,1,13),_HcAlarmFallingThresholdValStatus_Type())
hcAlarmFallingThresholdValStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmFallingThresholdValStatus.setStatus(_B)
class _HcAlarmRisingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HcAlarmRisingEventIndex_Type.__name__=_D
_HcAlarmRisingEventIndex_Object=MibTableColumn
hcAlarmRisingEventIndex=_HcAlarmRisingEventIndex_Object((1,3,6,1,2,1,16,29,1,1,1,1,14),_HcAlarmRisingEventIndex_Type())
hcAlarmRisingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmRisingEventIndex.setStatus(_B)
class _HcAlarmFallingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HcAlarmFallingEventIndex_Type.__name__=_D
_HcAlarmFallingEventIndex_Object=MibTableColumn
hcAlarmFallingEventIndex=_HcAlarmFallingEventIndex_Object((1,3,6,1,2,1,16,29,1,1,1,1,15),_HcAlarmFallingEventIndex_Type())
hcAlarmFallingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmFallingEventIndex.setStatus(_B)
_HcAlarmValueFailedAttempts_Type=Counter32
_HcAlarmValueFailedAttempts_Object=MibTableColumn
hcAlarmValueFailedAttempts=_HcAlarmValueFailedAttempts_Object((1,3,6,1,2,1,16,29,1,1,1,1,16),_HcAlarmValueFailedAttempts_Type())
hcAlarmValueFailedAttempts.setMaxAccess(_E)
if mibBuilder.loadTexts:hcAlarmValueFailedAttempts.setStatus(_B)
_HcAlarmOwner_Type=OwnerString
_HcAlarmOwner_Object=MibTableColumn
hcAlarmOwner=_HcAlarmOwner_Object((1,3,6,1,2,1,16,29,1,1,1,1,17),_HcAlarmOwner_Type())
hcAlarmOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmOwner.setStatus(_B)
_HcAlarmStorageType_Type=StorageType
_HcAlarmStorageType_Object=MibTableColumn
hcAlarmStorageType=_HcAlarmStorageType_Object((1,3,6,1,2,1,16,29,1,1,1,1,18),_HcAlarmStorageType_Type())
hcAlarmStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmStorageType.setStatus(_B)
_HcAlarmStatus_Type=RowStatus
_HcAlarmStatus_Object=MibTableColumn
hcAlarmStatus=_HcAlarmStatus_Object((1,3,6,1,2,1,16,29,1,1,1,1,19),_HcAlarmStatus_Type())
hcAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hcAlarmStatus.setStatus(_B)
_HcAlarmCapabilitiesObjects_ObjectIdentity=ObjectIdentity
hcAlarmCapabilitiesObjects=_HcAlarmCapabilitiesObjects_ObjectIdentity((1,3,6,1,2,1,16,29,1,2))
class _HcAlarmCapabilities_Type(Bits):namedValues=NamedValues(*(('hcAlarmCreation',0),('hcAlarmNvStorage',1)))
_HcAlarmCapabilities_Type.__name__='Bits'
_HcAlarmCapabilities_Object=MibScalar
hcAlarmCapabilities=_HcAlarmCapabilities_Object((1,3,6,1,2,1,16,29,1,2,1),_HcAlarmCapabilities_Type())
hcAlarmCapabilities.setMaxAccess(_E)
if mibBuilder.loadTexts:hcAlarmCapabilities.setStatus(_B)
_HcAlarmNotifications_ObjectIdentity=ObjectIdentity
hcAlarmNotifications=_HcAlarmNotifications_ObjectIdentity((1,3,6,1,2,1,16,29,2))
_HcAlarmNotifPrefix_ObjectIdentity=ObjectIdentity
hcAlarmNotifPrefix=_HcAlarmNotifPrefix_ObjectIdentity((1,3,6,1,2,1,16,29,2,0))
_HcAlarmConformance_ObjectIdentity=ObjectIdentity
hcAlarmConformance=_HcAlarmConformance_ObjectIdentity((1,3,6,1,2,1,16,29,3))
_HcAlarmCompliances_ObjectIdentity=ObjectIdentity
hcAlarmCompliances=_HcAlarmCompliances_ObjectIdentity((1,3,6,1,2,1,16,29,3,1))
_HcAlarmGroups_ObjectIdentity=ObjectIdentity
hcAlarmGroups=_HcAlarmGroups_ObjectIdentity((1,3,6,1,2,1,16,29,3,2))
hcAlarmControlGroup=ObjectGroup((1,3,6,1,2,1,16,29,3,2,1))
hcAlarmControlGroup.setObjects(*((_A,_U),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_V),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:hcAlarmControlGroup.setStatus(_B)
hcAlarmCapabilitiesGroup=ObjectGroup((1,3,6,1,2,1,16,29,3,2,2))
hcAlarmCapabilitiesGroup.setObjects((_A,_a))
if mibBuilder.loadTexts:hcAlarmCapabilitiesGroup.setStatus(_B)
hcRisingAlarm=NotificationType((1,3,6,1,2,1,16,29,2,0,1))
hcRisingAlarm.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_P)))
if mibBuilder.loadTexts:hcRisingAlarm.setStatus(_B)
hcFallingAlarm=NotificationType((1,3,6,1,2,1,16,29,2,0,2))
hcFallingAlarm.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_M),(_A,_N),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:hcFallingAlarm.setStatus(_B)
hcAlarmNotificationsGroup=NotificationGroup((1,3,6,1,2,1,16,29,3,2,3))
hcAlarmNotificationsGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:hcAlarmNotificationsGroup.setStatus(_B)
hcAlarmCompliance=ModuleCompliance((1,3,6,1,2,1,16,29,3,1,1))
hcAlarmCompliance.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_R,_S)))
if mibBuilder.loadTexts:hcAlarmCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HcValueStatus':HcValueStatus,'hcAlarmMIB':hcAlarmMIB,'hcAlarmObjects':hcAlarmObjects,'hcAlarmControlObjects':hcAlarmControlObjects,'hcAlarmTable':hcAlarmTable,'hcAlarmEntry':hcAlarmEntry,_T:hcAlarmIndex,_U:hcAlarmInterval,_F:hcAlarmVariable,_G:hcAlarmSampleType,_H:hcAlarmAbsValue,_I:hcAlarmValueStatus,_V:hcAlarmStartupAlarm,_J:hcAlarmRisingThreshAbsValueLo,_K:hcAlarmRisingThreshAbsValueHi,_L:hcAlarmRisingThresholdValStatus,_M:hcAlarmFallingThreshAbsValueLo,_N:hcAlarmFallingThreshAbsValueHi,_O:hcAlarmFallingThresholdValStatus,_P:hcAlarmRisingEventIndex,_Q:hcAlarmFallingEventIndex,_W:hcAlarmValueFailedAttempts,_X:hcAlarmOwner,_Y:hcAlarmStorageType,_Z:hcAlarmStatus,'hcAlarmCapabilitiesObjects':hcAlarmCapabilitiesObjects,_a:hcAlarmCapabilities,'hcAlarmNotifications':hcAlarmNotifications,'hcAlarmNotifPrefix':hcAlarmNotifPrefix,_b:hcRisingAlarm,_c:hcFallingAlarm,'hcAlarmConformance':hcAlarmConformance,'hcAlarmCompliances':hcAlarmCompliances,'hcAlarmCompliance':hcAlarmCompliance,'hcAlarmGroups':hcAlarmGroups,_d:hcAlarmControlGroup,_e:hcAlarmCapabilitiesGroup,_f:hcAlarmNotificationsGroup})