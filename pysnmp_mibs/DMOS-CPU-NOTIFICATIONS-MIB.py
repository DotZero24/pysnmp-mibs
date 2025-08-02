_Q='cpuCoreHighTrap'
_P='cpuLoadHighTrap'
_O='dmosCpuNotificationCoreId'
_N='notificationTime'
_M='notificationSourceValue'
_L='notificationSourceType'
_K='notificationSeverity'
_J='notificationName'
_I='notificationInfo'
_H='notificationAlarmState'
_G='dmosCpuNotificationValue'
_F='dmosCpuNotificationInterval'
_E='dmosCpuNotificationThreshold'
_D='accessible-for-notify'
_C='current'
_B='DMOS-CPU-NOTIFICATIONS-MIB'
_A='DMOS-NOTIFICATIONS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmNotifications,notificationAlarmState,notificationInfo,notificationName,notificationSeverity,notificationSourceType,notificationSourceValue,notificationTime=mibBuilder.importSymbols(_A,'alarmNotifications',_H,_I,_J,_K,_L,_M,_N)
UnsignedPercent,=mibBuilder.importSymbols('DMOS-TC-MIB','UnsignedPercent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dmosCpuNotificationsMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,6,3,3,0))
if mibBuilder.loadTexts:dmosCpuNotificationsMIB.setRevisions(('2016-10-20 00:00',))
_DmosCpuNotificationObjects_ObjectIdentity=ObjectIdentity
dmosCpuNotificationObjects=_DmosCpuNotificationObjects_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,3,0,1))
_DmosCpuNotificationThreshold_Type=UnsignedPercent
_DmosCpuNotificationThreshold_Object=MibScalar
dmosCpuNotificationThreshold=_DmosCpuNotificationThreshold_Object((1,3,6,1,4,1,3709,3,6,3,3,0,1,1),_DmosCpuNotificationThreshold_Type())
dmosCpuNotificationThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dmosCpuNotificationThreshold.setStatus(_C)
if mibBuilder.loadTexts:dmosCpuNotificationThreshold.setUnits('%')
_DmosCpuNotificationInterval_Type=Gauge32
_DmosCpuNotificationInterval_Object=MibScalar
dmosCpuNotificationInterval=_DmosCpuNotificationInterval_Object((1,3,6,1,4,1,3709,3,6,3,3,0,1,2),_DmosCpuNotificationInterval_Type())
dmosCpuNotificationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dmosCpuNotificationInterval.setStatus(_C)
if mibBuilder.loadTexts:dmosCpuNotificationInterval.setUnits('seconds')
_DmosCpuNotificationValue_Type=UnsignedPercent
_DmosCpuNotificationValue_Object=MibScalar
dmosCpuNotificationValue=_DmosCpuNotificationValue_Object((1,3,6,1,4,1,3709,3,6,3,3,0,1,3),_DmosCpuNotificationValue_Type())
dmosCpuNotificationValue.setMaxAccess(_D)
if mibBuilder.loadTexts:dmosCpuNotificationValue.setStatus(_C)
if mibBuilder.loadTexts:dmosCpuNotificationValue.setUnits('%')
_DmosCpuNotificationCoreId_Type=Gauge32
_DmosCpuNotificationCoreId_Object=MibScalar
dmosCpuNotificationCoreId=_DmosCpuNotificationCoreId_Object((1,3,6,1,4,1,3709,3,6,3,3,0,1,4),_DmosCpuNotificationCoreId_Type())
dmosCpuNotificationCoreId.setMaxAccess(_D)
if mibBuilder.loadTexts:dmosCpuNotificationCoreId.setStatus(_C)
if mibBuilder.loadTexts:dmosCpuNotificationCoreId.setUnits('ID')
_DmosCpuNotificationGroups_ObjectIdentity=ObjectIdentity
dmosCpuNotificationGroups=_DmosCpuNotificationGroups_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,3,0,2))
dmosCpuAlarmInfoGroup=ObjectGroup((1,3,6,1,4,1,3709,3,6,3,3,0,2,1))
dmosCpuAlarmInfoGroup.setObjects(*((_B,_E),(_B,_F),(_B,_O),(_B,_G)))
if mibBuilder.loadTexts:dmosCpuAlarmInfoGroup.setStatus(_C)
cpuLoadHighTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,0,3))
cpuLoadHighTrap.setObjects(*((_A,_N),(_A,_J),(_A,_L),(_A,_M),(_A,_K),(_A,_I),(_A,_H),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:cpuLoadHighTrap.setStatus(_C)
cpuCoreHighTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,0,4))
cpuCoreHighTrap.setObjects(*((_A,_N),(_A,_J),(_A,_L),(_A,_M),(_A,_K),(_A,_I),(_A,_H),(_B,_E),(_B,_F),(_B,_O),(_B,_G)))
if mibBuilder.loadTexts:cpuCoreHighTrap.setStatus(_C)
dmosCpuAlarmTrapsGroup=NotificationGroup((1,3,6,1,4,1,3709,3,6,3,3,0,2,2))
dmosCpuAlarmTrapsGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:dmosCpuAlarmTrapsGroup.setStatus(_C)
mibBuilder.exportSymbols(_B,**{'dmosCpuNotificationsMIB':dmosCpuNotificationsMIB,'dmosCpuNotificationObjects':dmosCpuNotificationObjects,_E:dmosCpuNotificationThreshold,_F:dmosCpuNotificationInterval,_G:dmosCpuNotificationValue,_O:dmosCpuNotificationCoreId,'dmosCpuNotificationGroups':dmosCpuNotificationGroups,'dmosCpuAlarmInfoGroup':dmosCpuAlarmInfoGroup,'dmosCpuAlarmTrapsGroup':dmosCpuAlarmTrapsGroup,_P:cpuLoadHighTrap,_Q:cpuCoreHighTrap})