_P='eltexEntitySensorThresholdIndex'
_O='read-write'
_N='read-only'
_M='SyslogSeverity'
_L='EntitySensorValue'
_K='eltexEntitySensorThresholdValue'
_J='eltexEntitySensorThresholdRelation'
_I='eltexEntitySensorThresholdSeverity'
_H='entPhySensorValue'
_G='ENTITY-SENSOR-MIB'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='TruthValue'
_C='read-create'
_B='ELTEX-ENTITY-SENSOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
EltexThresholdRelation,=mibBuilder.importSymbols('ELTEX-TC','EltexThresholdRelation')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
EntitySensorValue,entPhySensorValue=mibBuilder.importSymbols(_G,_L,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
SyslogSeverity,=mibBuilder.importSymbols('SYSLOG-TC-MIB',_M)
eltexEntitySensorMIB=ModuleIdentity((1,3,6,1,4,1,35265,40))
if mibBuilder.loadTexts:eltexEntitySensorMIB.setRevisions(('2017-05-02 00:00',))
_EltexEntitySensorMIBObjects_ObjectIdentity=ObjectIdentity
eltexEntitySensorMIBObjects=_EltexEntitySensorMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,40,1))
_EltexEntitySensorCommon_ObjectIdentity=ObjectIdentity
eltexEntitySensorCommon=_EltexEntitySensorCommon_ObjectIdentity((1,3,6,1,4,1,35265,40,1,1))
_EltexEntitySensorTable_Object=MibTable
eltexEntitySensorTable=_EltexEntitySensorTable_Object((1,3,6,1,4,1,35265,40,1,1,2))
if mibBuilder.loadTexts:eltexEntitySensorTable.setStatus(_A)
_EltexEntitySensorEntry_Object=MibTableRow
eltexEntitySensorEntry=_EltexEntitySensorEntry_Object((1,3,6,1,4,1,35265,40,1,1,2,1))
eltexEntitySensorEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:eltexEntitySensorEntry.setStatus(_A)
_EltexEntitySensorThresholdFreeIndex_Type=Unsigned32
_EltexEntitySensorThresholdFreeIndex_Object=MibTableColumn
eltexEntitySensorThresholdFreeIndex=_EltexEntitySensorThresholdFreeIndex_Object((1,3,6,1,4,1,35265,40,1,1,2,1,1),_EltexEntitySensorThresholdFreeIndex_Type())
eltexEntitySensorThresholdFreeIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:eltexEntitySensorThresholdFreeIndex.setStatus(_A)
_EltexEntitySensorThresholds_ObjectIdentity=ObjectIdentity
eltexEntitySensorThresholds=_EltexEntitySensorThresholds_ObjectIdentity((1,3,6,1,4,1,35265,40,1,2))
class _EltexEntitySensorThresholdNotificationGlobalEnable_Type(TruthValue):defaultValue=2
_EltexEntitySensorThresholdNotificationGlobalEnable_Type.__name__=_D
_EltexEntitySensorThresholdNotificationGlobalEnable_Object=MibScalar
eltexEntitySensorThresholdNotificationGlobalEnable=_EltexEntitySensorThresholdNotificationGlobalEnable_Object((1,3,6,1,4,1,35265,40,1,2,1),_EltexEntitySensorThresholdNotificationGlobalEnable_Type())
eltexEntitySensorThresholdNotificationGlobalEnable.setMaxAccess(_O)
if mibBuilder.loadTexts:eltexEntitySensorThresholdNotificationGlobalEnable.setStatus(_A)
class _EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Type(TruthValue):defaultValue=2
_EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Type.__name__=_D
_EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Object=MibScalar
eltexEntitySensorThresholdRecoveryNotificationGlobalEnable=_EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Object((1,3,6,1,4,1,35265,40,1,2,2),_EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Type())
eltexEntitySensorThresholdRecoveryNotificationGlobalEnable.setMaxAccess(_O)
if mibBuilder.loadTexts:eltexEntitySensorThresholdRecoveryNotificationGlobalEnable.setStatus(_A)
_EltexEntitySensorThresholdTable_Object=MibTable
eltexEntitySensorThresholdTable=_EltexEntitySensorThresholdTable_Object((1,3,6,1,4,1,35265,40,1,2,3))
if mibBuilder.loadTexts:eltexEntitySensorThresholdTable.setStatus(_A)
_EltexEntitySensorThresholdEntry_Object=MibTableRow
eltexEntitySensorThresholdEntry=_EltexEntitySensorThresholdEntry_Object((1,3,6,1,4,1,35265,40,1,2,3,1))
eltexEntitySensorThresholdEntry.setIndexNames((0,_E,_F),(0,_B,_P))
if mibBuilder.loadTexts:eltexEntitySensorThresholdEntry.setStatus(_A)
_EltexEntitySensorThresholdIndex_Type=Unsigned32
_EltexEntitySensorThresholdIndex_Object=MibTableColumn
eltexEntitySensorThresholdIndex=_EltexEntitySensorThresholdIndex_Object((1,3,6,1,4,1,35265,40,1,2,3,1,1),_EltexEntitySensorThresholdIndex_Type())
eltexEntitySensorThresholdIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltexEntitySensorThresholdIndex.setStatus(_A)
_EltexEntitySensorThresholdRowStatus_Type=RowStatus
_EltexEntitySensorThresholdRowStatus_Object=MibTableColumn
eltexEntitySensorThresholdRowStatus=_EltexEntitySensorThresholdRowStatus_Object((1,3,6,1,4,1,35265,40,1,2,3,1,2),_EltexEntitySensorThresholdRowStatus_Type())
eltexEntitySensorThresholdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexEntitySensorThresholdRowStatus.setStatus(_A)
_EltexEntitySensorThresholdValue_Type=EntitySensorValue
_EltexEntitySensorThresholdValue_Object=MibTableColumn
eltexEntitySensorThresholdValue=_EltexEntitySensorThresholdValue_Object((1,3,6,1,4,1,35265,40,1,2,3,1,3),_EltexEntitySensorThresholdValue_Type())
eltexEntitySensorThresholdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexEntitySensorThresholdValue.setStatus(_A)
class _EltexEntitySensorThresholdFlappingInterval_Type(EntitySensorValue):defaultValue=0
_EltexEntitySensorThresholdFlappingInterval_Type.__name__=_L
_EltexEntitySensorThresholdFlappingInterval_Object=MibTableColumn
eltexEntitySensorThresholdFlappingInterval=_EltexEntitySensorThresholdFlappingInterval_Object((1,3,6,1,4,1,35265,40,1,2,3,1,4),_EltexEntitySensorThresholdFlappingInterval_Type())
eltexEntitySensorThresholdFlappingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexEntitySensorThresholdFlappingInterval.setStatus(_A)
class _EltexEntitySensorThresholdSeverity_Type(SyslogSeverity):defaultValue=1
_EltexEntitySensorThresholdSeverity_Type.__name__=_M
_EltexEntitySensorThresholdSeverity_Object=MibTableColumn
eltexEntitySensorThresholdSeverity=_EltexEntitySensorThresholdSeverity_Object((1,3,6,1,4,1,35265,40,1,2,3,1,5),_EltexEntitySensorThresholdSeverity_Type())
eltexEntitySensorThresholdSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexEntitySensorThresholdSeverity.setStatus(_A)
_EltexEntitySensorThresholdRelation_Type=EltexThresholdRelation
_EltexEntitySensorThresholdRelation_Object=MibTableColumn
eltexEntitySensorThresholdRelation=_EltexEntitySensorThresholdRelation_Object((1,3,6,1,4,1,35265,40,1,2,3,1,6),_EltexEntitySensorThresholdRelation_Type())
eltexEntitySensorThresholdRelation.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexEntitySensorThresholdRelation.setStatus(_A)
class _EltexEntitySensorThresholdNotificationEnable_Type(TruthValue):defaultValue=1
_EltexEntitySensorThresholdNotificationEnable_Type.__name__=_D
_EltexEntitySensorThresholdNotificationEnable_Object=MibTableColumn
eltexEntitySensorThresholdNotificationEnable=_EltexEntitySensorThresholdNotificationEnable_Object((1,3,6,1,4,1,35265,40,1,2,3,1,7),_EltexEntitySensorThresholdNotificationEnable_Type())
eltexEntitySensorThresholdNotificationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexEntitySensorThresholdNotificationEnable.setStatus(_A)
class _EltexEntitySensorThresholdRecoveryNotificationEnable_Type(TruthValue):defaultValue=1
_EltexEntitySensorThresholdRecoveryNotificationEnable_Type.__name__=_D
_EltexEntitySensorThresholdRecoveryNotificationEnable_Object=MibTableColumn
eltexEntitySensorThresholdRecoveryNotificationEnable=_EltexEntitySensorThresholdRecoveryNotificationEnable_Object((1,3,6,1,4,1,35265,40,1,2,3,1,8),_EltexEntitySensorThresholdRecoveryNotificationEnable_Type())
eltexEntitySensorThresholdRecoveryNotificationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexEntitySensorThresholdRecoveryNotificationEnable.setStatus(_A)
_EltexEntitySensorThresholdEvaluation_Type=TruthValue
_EltexEntitySensorThresholdEvaluation_Object=MibTableColumn
eltexEntitySensorThresholdEvaluation=_EltexEntitySensorThresholdEvaluation_Object((1,3,6,1,4,1,35265,40,1,2,3,1,9),_EltexEntitySensorThresholdEvaluation_Type())
eltexEntitySensorThresholdEvaluation.setMaxAccess(_N)
if mibBuilder.loadTexts:eltexEntitySensorThresholdEvaluation.setStatus(_A)
_EltexEntitySensorMIBNotifications_ObjectIdentity=ObjectIdentity
eltexEntitySensorMIBNotifications=_EltexEntitySensorMIBNotifications_ObjectIdentity((1,3,6,1,4,1,35265,40,2))
_EltexEntitySensorMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
eltexEntitySensorMIBNotificationsPrefix=_EltexEntitySensorMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,40,2,0))
eltexEntitySensorThresholdNotification=NotificationType((1,3,6,1,4,1,35265,40,2,0,1))
eltexEntitySensorThresholdNotification.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_G,_H)))
if mibBuilder.loadTexts:eltexEntitySensorThresholdNotification.setStatus(_A)
eltexEntitySensorThresholdRecoveryNotification=NotificationType((1,3,6,1,4,1,35265,40,2,0,2))
eltexEntitySensorThresholdRecoveryNotification.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_G,_H)))
if mibBuilder.loadTexts:eltexEntitySensorThresholdRecoveryNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eltexEntitySensorMIB':eltexEntitySensorMIB,'eltexEntitySensorMIBObjects':eltexEntitySensorMIBObjects,'eltexEntitySensorCommon':eltexEntitySensorCommon,'eltexEntitySensorTable':eltexEntitySensorTable,'eltexEntitySensorEntry':eltexEntitySensorEntry,'eltexEntitySensorThresholdFreeIndex':eltexEntitySensorThresholdFreeIndex,'eltexEntitySensorThresholds':eltexEntitySensorThresholds,'eltexEntitySensorThresholdNotificationGlobalEnable':eltexEntitySensorThresholdNotificationGlobalEnable,'eltexEntitySensorThresholdRecoveryNotificationGlobalEnable':eltexEntitySensorThresholdRecoveryNotificationGlobalEnable,'eltexEntitySensorThresholdTable':eltexEntitySensorThresholdTable,'eltexEntitySensorThresholdEntry':eltexEntitySensorThresholdEntry,_P:eltexEntitySensorThresholdIndex,'eltexEntitySensorThresholdRowStatus':eltexEntitySensorThresholdRowStatus,_K:eltexEntitySensorThresholdValue,'eltexEntitySensorThresholdFlappingInterval':eltexEntitySensorThresholdFlappingInterval,_I:eltexEntitySensorThresholdSeverity,_J:eltexEntitySensorThresholdRelation,'eltexEntitySensorThresholdNotificationEnable':eltexEntitySensorThresholdNotificationEnable,'eltexEntitySensorThresholdRecoveryNotificationEnable':eltexEntitySensorThresholdRecoveryNotificationEnable,'eltexEntitySensorThresholdEvaluation':eltexEntitySensorThresholdEvaluation,'eltexEntitySensorMIBNotifications':eltexEntitySensorMIBNotifications,'eltexEntitySensorMIBNotificationsPrefix':eltexEntitySensorMIBNotificationsPrefix,'eltexEntitySensorThresholdNotification':eltexEntitySensorThresholdNotification,'eltexEntitySensorThresholdRecoveryNotification':eltexEntitySensorThresholdRecoveryNotification})