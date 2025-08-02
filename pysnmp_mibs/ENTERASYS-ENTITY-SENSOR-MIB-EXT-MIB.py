_h='etsysEntitySfpSensorNotificationGroup'
_g='etsysEntitySfpSensorGroup'
_f='etsysEntityTempSensorNotificationGroup'
_e='etsysEntityTempSensorGroup'
_d='etsysEntitySfpSensorStateChng'
_c='etsysEntityTempSensorStateChng'
_b='etsysEntitySfpSensorTrapEnable'
_a='etsysEntitySfpSensorLowAlarm'
_Z='etsysEntitySfpSensorLowWarning'
_Y='etsysEntitySfpSensorHighWarning'
_X='etsysEntitySfpSensorHighAlarm'
_W='etsysEntityTempSensorTrapEnable'
_V='etsysEntityTempSensorColdTemp'
_U='etsysEntityTempSensorCoolTemp'
_T='etsysEntityTempSensorWarmTemp'
_S='etsysEntityTempSensorHotTemp'
_R='read-write'
_Q='normal'
_P='unknown'
_O='etsysEntitySfpSensorState'
_N='etsysEntityTempSensorState'
_M='Integer32'
_L='EnabledStatus'
_K='entPhySensorValue'
_J='entPhySensorUnitsDisplay'
_I='entPhySensorScale'
_H='entPhySensorPrecision'
_G='entPhySensorOperStatus'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='ENTITY-SENSOR-MIB'
_B='ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
EntitySensorValue,entPhySensorOperStatus,entPhySensorPrecision,entPhySensorScale,entPhySensorUnitsDisplay,entPhySensorValue=mibBuilder.importSymbols(_C,'EntitySensorValue',_G,_H,_I,_J,_K)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysEntitySensorExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,85))
if mibBuilder.loadTexts:etsysEntitySensorExtMIB.setRevisions(('2014-05-13 12:06','2011-10-14 14:49'))
_EtsysEntitySensorExtObjects_ObjectIdentity=ObjectIdentity
etsysEntitySensorExtObjects=_EtsysEntitySensorExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,85,1))
_EtsysEntitySensorExtNotifications_ObjectIdentity=ObjectIdentity
etsysEntitySensorExtNotifications=_EtsysEntitySensorExtNotifications_ObjectIdentity((1,3,6,1,4,1,5624,1,2,85,1,0))
_EtsysEntityTempSensorExt_ObjectIdentity=ObjectIdentity
etsysEntityTempSensorExt=_EtsysEntityTempSensorExt_ObjectIdentity((1,3,6,1,4,1,5624,1,2,85,1,1))
_EtsysEntityTempSensorExtTable_Object=MibTable
etsysEntityTempSensorExtTable=_EtsysEntityTempSensorExtTable_Object((1,3,6,1,4,1,5624,1,2,85,1,1,1))
if mibBuilder.loadTexts:etsysEntityTempSensorExtTable.setStatus(_A)
_EtsysEntityTempSensorExtEntry_Object=MibTableRow
etsysEntityTempSensorExtEntry=_EtsysEntityTempSensorExtEntry_Object((1,3,6,1,4,1,5624,1,2,85,1,1,1,1))
etsysEntityTempSensorExtEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:etsysEntityTempSensorExtEntry.setStatus(_A)
class _EtsysEntityTempSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),('cold',2),('cool',3),(_Q,4),('warm',5),('hot',6)))
_EtsysEntityTempSensorState_Type.__name__=_M
_EtsysEntityTempSensorState_Object=MibTableColumn
etsysEntityTempSensorState=_EtsysEntityTempSensorState_Object((1,3,6,1,4,1,5624,1,2,85,1,1,1,1,1),_EtsysEntityTempSensorState_Type())
etsysEntityTempSensorState.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntityTempSensorState.setStatus(_A)
_EtsysEntityTempSensorHotTemp_Type=EntitySensorValue
_EtsysEntityTempSensorHotTemp_Object=MibTableColumn
etsysEntityTempSensorHotTemp=_EtsysEntityTempSensorHotTemp_Object((1,3,6,1,4,1,5624,1,2,85,1,1,1,1,2),_EtsysEntityTempSensorHotTemp_Type())
etsysEntityTempSensorHotTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntityTempSensorHotTemp.setStatus(_A)
_EtsysEntityTempSensorWarmTemp_Type=EntitySensorValue
_EtsysEntityTempSensorWarmTemp_Object=MibTableColumn
etsysEntityTempSensorWarmTemp=_EtsysEntityTempSensorWarmTemp_Object((1,3,6,1,4,1,5624,1,2,85,1,1,1,1,3),_EtsysEntityTempSensorWarmTemp_Type())
etsysEntityTempSensorWarmTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntityTempSensorWarmTemp.setStatus(_A)
_EtsysEntityTempSensorCoolTemp_Type=EntitySensorValue
_EtsysEntityTempSensorCoolTemp_Object=MibTableColumn
etsysEntityTempSensorCoolTemp=_EtsysEntityTempSensorCoolTemp_Object((1,3,6,1,4,1,5624,1,2,85,1,1,1,1,4),_EtsysEntityTempSensorCoolTemp_Type())
etsysEntityTempSensorCoolTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntityTempSensorCoolTemp.setStatus(_A)
_EtsysEntityTempSensorColdTemp_Type=EntitySensorValue
_EtsysEntityTempSensorColdTemp_Object=MibTableColumn
etsysEntityTempSensorColdTemp=_EtsysEntityTempSensorColdTemp_Object((1,3,6,1,4,1,5624,1,2,85,1,1,1,1,5),_EtsysEntityTempSensorColdTemp_Type())
etsysEntityTempSensorColdTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntityTempSensorColdTemp.setStatus(_A)
class _EtsysEntityTempSensorTrapEnable_Type(EnabledStatus):defaultValue=1
_EtsysEntityTempSensorTrapEnable_Type.__name__=_L
_EtsysEntityTempSensorTrapEnable_Object=MibTableColumn
etsysEntityTempSensorTrapEnable=_EtsysEntityTempSensorTrapEnable_Object((1,3,6,1,4,1,5624,1,2,85,1,1,1,1,6),_EtsysEntityTempSensorTrapEnable_Type())
etsysEntityTempSensorTrapEnable.setMaxAccess(_R)
if mibBuilder.loadTexts:etsysEntityTempSensorTrapEnable.setStatus(_A)
_EtsysEntitySfpSensorExt_ObjectIdentity=ObjectIdentity
etsysEntitySfpSensorExt=_EtsysEntitySfpSensorExt_ObjectIdentity((1,3,6,1,4,1,5624,1,2,85,1,2))
_EtsysEntitySfpSensorExtTable_Object=MibTable
etsysEntitySfpSensorExtTable=_EtsysEntitySfpSensorExtTable_Object((1,3,6,1,4,1,5624,1,2,85,1,2,1))
if mibBuilder.loadTexts:etsysEntitySfpSensorExtTable.setStatus(_A)
_EtsysEntitySfpSensorExtEntry_Object=MibTableRow
etsysEntitySfpSensorExtEntry=_EtsysEntitySfpSensorExtEntry_Object((1,3,6,1,4,1,5624,1,2,85,1,2,1,1))
etsysEntitySfpSensorExtEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:etsysEntitySfpSensorExtEntry.setStatus(_A)
class _EtsysEntitySfpSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),('lowAlarm',2),('lowWarning',3),(_Q,4),('highWarning',5),('highAlarm',6)))
_EtsysEntitySfpSensorState_Type.__name__=_M
_EtsysEntitySfpSensorState_Object=MibTableColumn
etsysEntitySfpSensorState=_EtsysEntitySfpSensorState_Object((1,3,6,1,4,1,5624,1,2,85,1,2,1,1,1),_EtsysEntitySfpSensorState_Type())
etsysEntitySfpSensorState.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntitySfpSensorState.setStatus(_A)
_EtsysEntitySfpSensorHighAlarm_Type=EntitySensorValue
_EtsysEntitySfpSensorHighAlarm_Object=MibTableColumn
etsysEntitySfpSensorHighAlarm=_EtsysEntitySfpSensorHighAlarm_Object((1,3,6,1,4,1,5624,1,2,85,1,2,1,1,2),_EtsysEntitySfpSensorHighAlarm_Type())
etsysEntitySfpSensorHighAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntitySfpSensorHighAlarm.setStatus(_A)
_EtsysEntitySfpSensorHighWarning_Type=EntitySensorValue
_EtsysEntitySfpSensorHighWarning_Object=MibTableColumn
etsysEntitySfpSensorHighWarning=_EtsysEntitySfpSensorHighWarning_Object((1,3,6,1,4,1,5624,1,2,85,1,2,1,1,3),_EtsysEntitySfpSensorHighWarning_Type())
etsysEntitySfpSensorHighWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntitySfpSensorHighWarning.setStatus(_A)
_EtsysEntitySfpSensorLowWarning_Type=EntitySensorValue
_EtsysEntitySfpSensorLowWarning_Object=MibTableColumn
etsysEntitySfpSensorLowWarning=_EtsysEntitySfpSensorLowWarning_Object((1,3,6,1,4,1,5624,1,2,85,1,2,1,1,4),_EtsysEntitySfpSensorLowWarning_Type())
etsysEntitySfpSensorLowWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntitySfpSensorLowWarning.setStatus(_A)
_EtsysEntitySfpSensorLowAlarm_Type=EntitySensorValue
_EtsysEntitySfpSensorLowAlarm_Object=MibTableColumn
etsysEntitySfpSensorLowAlarm=_EtsysEntitySfpSensorLowAlarm_Object((1,3,6,1,4,1,5624,1,2,85,1,2,1,1,5),_EtsysEntitySfpSensorLowAlarm_Type())
etsysEntitySfpSensorLowAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEntitySfpSensorLowAlarm.setStatus(_A)
class _EtsysEntitySfpSensorTrapEnable_Type(EnabledStatus):defaultValue=1
_EtsysEntitySfpSensorTrapEnable_Type.__name__=_L
_EtsysEntitySfpSensorTrapEnable_Object=MibScalar
etsysEntitySfpSensorTrapEnable=_EtsysEntitySfpSensorTrapEnable_Object((1,3,6,1,4,1,5624,1,2,85,1,2,2),_EtsysEntitySfpSensorTrapEnable_Type())
etsysEntitySfpSensorTrapEnable.setMaxAccess(_R)
if mibBuilder.loadTexts:etsysEntitySfpSensorTrapEnable.setStatus(_A)
_EtsysEntitySensorExtConformance_ObjectIdentity=ObjectIdentity
etsysEntitySensorExtConformance=_EtsysEntitySensorExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,85,2))
_EtsysEntitySensorExtGroups_ObjectIdentity=ObjectIdentity
etsysEntitySensorExtGroups=_EtsysEntitySensorExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,85,2,1))
_EtsysEntitySensorExtCompliances_ObjectIdentity=ObjectIdentity
etsysEntitySensorExtCompliances=_EtsysEntitySensorExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,85,2,2))
etsysEntityTempSensorGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,85,2,1,1))
etsysEntityTempSensorGroup.setObjects(*((_B,_N),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:etsysEntityTempSensorGroup.setStatus(_A)
etsysEntitySfpSensorGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,85,2,1,3))
etsysEntitySfpSensorGroup.setObjects(*((_B,_O),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:etsysEntitySfpSensorGroup.setStatus(_A)
etsysEntityTempSensorStateChng=NotificationType((1,3,6,1,4,1,5624,1,2,85,1,0,1))
etsysEntityTempSensorStateChng.setObjects(*((_B,_N),(_C,_G),(_C,_I),(_C,_H),(_C,_K),(_C,_J)))
if mibBuilder.loadTexts:etsysEntityTempSensorStateChng.setStatus(_A)
etsysEntitySfpSensorStateChng=NotificationType((1,3,6,1,4,1,5624,1,2,85,1,0,2))
etsysEntitySfpSensorStateChng.setObjects(*((_B,_O),(_C,_G),(_C,_I),(_C,_H),(_C,_K),(_C,_J)))
if mibBuilder.loadTexts:etsysEntitySfpSensorStateChng.setStatus(_A)
etsysEntityTempSensorNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,85,2,1,2))
etsysEntityTempSensorNotificationGroup.setObjects((_B,_c))
if mibBuilder.loadTexts:etsysEntityTempSensorNotificationGroup.setStatus(_A)
etsysEntitySfpSensorNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,85,2,1,4))
etsysEntitySfpSensorNotificationGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:etsysEntitySfpSensorNotificationGroup.setStatus(_A)
etsysEntitySensorExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,85,2,2,1))
etsysEntitySensorExtCompliance.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:etsysEntitySensorExtCompliance.setStatus(_A)
etsysEntitySensorSfpExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,85,2,2,2))
etsysEntitySensorSfpExtCompliance.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:etsysEntitySensorSfpExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysEntitySensorExtMIB':etsysEntitySensorExtMIB,'etsysEntitySensorExtObjects':etsysEntitySensorExtObjects,'etsysEntitySensorExtNotifications':etsysEntitySensorExtNotifications,_c:etsysEntityTempSensorStateChng,_d:etsysEntitySfpSensorStateChng,'etsysEntityTempSensorExt':etsysEntityTempSensorExt,'etsysEntityTempSensorExtTable':etsysEntityTempSensorExtTable,'etsysEntityTempSensorExtEntry':etsysEntityTempSensorExtEntry,_N:etsysEntityTempSensorState,_S:etsysEntityTempSensorHotTemp,_T:etsysEntityTempSensorWarmTemp,_U:etsysEntityTempSensorCoolTemp,_V:etsysEntityTempSensorColdTemp,_W:etsysEntityTempSensorTrapEnable,'etsysEntitySfpSensorExt':etsysEntitySfpSensorExt,'etsysEntitySfpSensorExtTable':etsysEntitySfpSensorExtTable,'etsysEntitySfpSensorExtEntry':etsysEntitySfpSensorExtEntry,_O:etsysEntitySfpSensorState,_X:etsysEntitySfpSensorHighAlarm,_Y:etsysEntitySfpSensorHighWarning,_Z:etsysEntitySfpSensorLowWarning,_a:etsysEntitySfpSensorLowAlarm,_b:etsysEntitySfpSensorTrapEnable,'etsysEntitySensorExtConformance':etsysEntitySensorExtConformance,'etsysEntitySensorExtGroups':etsysEntitySensorExtGroups,_e:etsysEntityTempSensorGroup,_f:etsysEntityTempSensorNotificationGroup,_g:etsysEntitySfpSensorGroup,_h:etsysEntitySfpSensorNotificationGroup,'etsysEntitySensorExtCompliances':etsysEntitySensorExtCompliances,'etsysEntitySensorExtCompliance':etsysEntitySensorExtCompliance,'etsysEntitySensorSfpExtCompliance':etsysEntitySensorSfpExtCompliance})