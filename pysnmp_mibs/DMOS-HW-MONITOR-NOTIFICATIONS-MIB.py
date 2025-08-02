_U='tempCriticalAlarmTrap'
_T='tempErrorAlarmTrap'
_S='tempLowAlarmTrap'
_R='tempHighAlarmTrap'
_Q='fanFailAlarmTrap'
_P='fanErrorAlarmTrap'
_O='fanLowAlarmTrap'
_N='fanHighAlarmTrap'
_M='accessible-for-notify'
_L='dmosHwMonLimitValue'
_K='dmosHwMonValue'
_J='notificationTime'
_I='notificationSourceValue'
_H='notificationSourceType'
_G='notificationSeverity'
_F='notificationName'
_E='notificationInfo'
_D='notificationAlarmState'
_C='current'
_B='DMOS-HW-MONITOR-NOTIFICATIONS-MIB'
_A='DMOS-NOTIFICATIONS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmNotifications,notificationAlarmState,notificationInfo,notificationName,notificationSeverity,notificationSourceType,notificationSourceValue,notificationTime=mibBuilder.importSymbols(_A,'alarmNotifications',_D,_E,_F,_G,_H,_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dmosHwMonNotificationsMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,6,3,3,2))
if mibBuilder.loadTexts:dmosHwMonNotificationsMIB.setRevisions(('2017-01-30 00:00',))
_DmosHwMonNotificationObjects_ObjectIdentity=ObjectIdentity
dmosHwMonNotificationObjects=_DmosHwMonNotificationObjects_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,3,2,1))
_DmosHwMonValue_Type=Integer32
_DmosHwMonValue_Object=MibScalar
dmosHwMonValue=_DmosHwMonValue_Object((1,3,6,1,4,1,3709,3,6,3,3,2,1,1),_DmosHwMonValue_Type())
dmosHwMonValue.setMaxAccess(_M)
if mibBuilder.loadTexts:dmosHwMonValue.setStatus(_C)
_DmosHwMonLimitValue_Type=Integer32
_DmosHwMonLimitValue_Object=MibScalar
dmosHwMonLimitValue=_DmosHwMonLimitValue_Object((1,3,6,1,4,1,3709,3,6,3,3,2,1,2),_DmosHwMonLimitValue_Type())
dmosHwMonLimitValue.setMaxAccess(_M)
if mibBuilder.loadTexts:dmosHwMonLimitValue.setStatus(_C)
_DmosHwMonNotificationGroups_ObjectIdentity=ObjectIdentity
dmosHwMonNotificationGroups=_DmosHwMonNotificationGroups_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,3,2,2))
dmosHwMonAlarmInfoGroup=ObjectGroup((1,3,6,1,4,1,3709,3,6,3,3,2,2,1))
dmosHwMonAlarmInfoGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:dmosHwMonAlarmInfoGroup.setStatus(_C)
fanHighAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,2,3))
fanHighAlarmTrap.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_E),(_A,_D),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:fanHighAlarmTrap.setStatus(_C)
fanLowAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,2,4))
fanLowAlarmTrap.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_E),(_A,_D),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:fanLowAlarmTrap.setStatus(_C)
fanFailAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,2,5))
fanFailAlarmTrap.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:fanFailAlarmTrap.setStatus(_C)
fanErrorAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,2,6))
fanErrorAlarmTrap.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:fanErrorAlarmTrap.setStatus(_C)
tempHighAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,2,7))
tempHighAlarmTrap.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_E),(_A,_D),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:tempHighAlarmTrap.setStatus(_C)
tempLowAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,2,8))
tempLowAlarmTrap.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_E),(_A,_D),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:tempLowAlarmTrap.setStatus(_C)
tempErrorAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,2,9))
tempErrorAlarmTrap.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:tempErrorAlarmTrap.setStatus(_C)
tempCriticalAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,2,10))
tempCriticalAlarmTrap.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_E),(_A,_D),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:tempCriticalAlarmTrap.setStatus(_C)
dmosFanAlarmTrapsGroup=NotificationGroup((1,3,6,1,4,1,3709,3,6,3,3,2,2,2))
dmosFanAlarmTrapsGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:dmosFanAlarmTrapsGroup.setStatus(_C)
dmosTempAlarmTrapsGroup=NotificationGroup((1,3,6,1,4,1,3709,3,6,3,3,2,2,3))
dmosTempAlarmTrapsGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:dmosTempAlarmTrapsGroup.setStatus(_C)
mibBuilder.exportSymbols(_B,**{'dmosHwMonNotificationsMIB':dmosHwMonNotificationsMIB,'dmosHwMonNotificationObjects':dmosHwMonNotificationObjects,_K:dmosHwMonValue,_L:dmosHwMonLimitValue,'dmosHwMonNotificationGroups':dmosHwMonNotificationGroups,'dmosHwMonAlarmInfoGroup':dmosHwMonAlarmInfoGroup,'dmosFanAlarmTrapsGroup':dmosFanAlarmTrapsGroup,'dmosTempAlarmTrapsGroup':dmosTempAlarmTrapsGroup,_N:fanHighAlarmTrap,_O:fanLowAlarmTrap,_Q:fanFailAlarmTrap,_P:fanErrorAlarmTrap,_R:tempHighAlarmTrap,_S:tempLowAlarmTrap,_T:tempErrorAlarmTrap,_U:tempCriticalAlarmTrap})