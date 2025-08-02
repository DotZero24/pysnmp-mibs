_N='cardMismatchAlarmTrap'
_M='cardRemovedAlarmTrap'
_L='cardNotPresentAlarmTrap'
_K='cardNotProvisionedAlarmTrap'
_J='DMOS-CARDMGR-NOTIFICATIONS-MIB'
_I='notificationSeverity'
_H='notificationAlarmState'
_G='current'
_F='notificationTime'
_E='notificationSourceValue'
_D='notificationSourceType'
_C='notificationName'
_B='notificationInfo'
_A='DMOS-NOTIFICATIONS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmNotifications,notificationAlarmState,notificationInfo,notificationName,notificationSeverity,notificationSourceType,notificationSourceValue,notificationTime=mibBuilder.importSymbols(_A,'alarmNotifications',_H,_B,_C,_I,_D,_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dmosCardmgrNotificationsMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,6,3,3,3))
if mibBuilder.loadTexts:dmosCardmgrNotificationsMIB.setRevisions(('2017-11-27 00:00',))
_DmosCardmgrNotificationGroups_ObjectIdentity=ObjectIdentity
dmosCardmgrNotificationGroups=_DmosCardmgrNotificationGroups_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,3,3,1))
cardNotProvisionedAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,3,2))
cardNotProvisionedAlarmTrap.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_I),(_A,_B),(_A,_H)))
if mibBuilder.loadTexts:cardNotProvisionedAlarmTrap.setStatus(_G)
cardNotPresentAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,3,3))
cardNotPresentAlarmTrap.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_I),(_A,_B),(_A,_H)))
if mibBuilder.loadTexts:cardNotPresentAlarmTrap.setStatus(_G)
cardRemovedAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,3,4))
cardRemovedAlarmTrap.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_I),(_A,_B),(_A,_H)))
if mibBuilder.loadTexts:cardRemovedAlarmTrap.setStatus(_G)
cardMismatchAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,3,5))
cardMismatchAlarmTrap.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_I),(_A,_B),(_A,_H)))
if mibBuilder.loadTexts:cardMismatchAlarmTrap.setStatus(_G)
cardInsertedTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,3,6))
cardInsertedTrap.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_B)))
if mibBuilder.loadTexts:cardInsertedTrap.setStatus(_G)
cardRemovedTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,3,7))
cardRemovedTrap.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_B)))
if mibBuilder.loadTexts:cardRemovedTrap.setStatus(_G)
dmosCardmgrAlarmTrapsGroup=NotificationGroup((1,3,6,1,4,1,3709,3,6,3,3,3,1,1))
dmosCardmgrAlarmTrapsGroup.setObjects(*((_J,_K),(_J,_L),(_J,_M),(_J,_N)))
if mibBuilder.loadTexts:dmosCardmgrAlarmTrapsGroup.setStatus(_G)
mibBuilder.exportSymbols(_J,**{'dmosCardmgrNotificationsMIB':dmosCardmgrNotificationsMIB,'dmosCardmgrNotificationGroups':dmosCardmgrNotificationGroups,'dmosCardmgrAlarmTrapsGroup':dmosCardmgrAlarmTrapsGroup,_K:cardNotProvisionedAlarmTrap,_L:cardNotPresentAlarmTrap,_M:cardRemovedAlarmTrap,_N:cardMismatchAlarmTrap,'cardInsertedTrap':cardInsertedTrap,'cardRemovedTrap':cardRemovedTrap})