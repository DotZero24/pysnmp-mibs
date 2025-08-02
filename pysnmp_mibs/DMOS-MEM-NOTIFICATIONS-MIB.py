_N='memAvailableLowTrap'
_M='accessible-for-notify'
_L='notificationTime'
_K='notificationSourceValue'
_J='notificationSourceType'
_I='notificationSeverity'
_H='notificationName'
_G='notificationInfo'
_F='notificationAlarmState'
_E='dmosMemNotificationInterval'
_D='dmosMemNotificationThreshold'
_C='current'
_B='DMOS-MEM-NOTIFICATIONS-MIB'
_A='DMOS-NOTIFICATIONS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmNotifications,notificationAlarmState,notificationInfo,notificationName,notificationSeverity,notificationSourceType,notificationSourceValue,notificationTime=mibBuilder.importSymbols(_A,'alarmNotifications',_F,_G,_H,_I,_J,_K,_L)
UnsignedPercent,=mibBuilder.importSymbols('DMOS-TC-MIB','UnsignedPercent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dmosMemNotificationsMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,6,3,3,1))
if mibBuilder.loadTexts:dmosMemNotificationsMIB.setRevisions(('2016-10-20 00:00',))
_DmosMemNotificationObjects_ObjectIdentity=ObjectIdentity
dmosMemNotificationObjects=_DmosMemNotificationObjects_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,3,1,1))
_DmosMemNotificationThreshold_Type=Gauge32
_DmosMemNotificationThreshold_Object=MibScalar
dmosMemNotificationThreshold=_DmosMemNotificationThreshold_Object((1,3,6,1,4,1,3709,3,6,3,3,1,1,1),_DmosMemNotificationThreshold_Type())
dmosMemNotificationThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:dmosMemNotificationThreshold.setStatus(_C)
if mibBuilder.loadTexts:dmosMemNotificationThreshold.setUnits('Bytes')
_DmosMemNotificationInterval_Type=Gauge32
_DmosMemNotificationInterval_Object=MibScalar
dmosMemNotificationInterval=_DmosMemNotificationInterval_Object((1,3,6,1,4,1,3709,3,6,3,3,1,1,2),_DmosMemNotificationInterval_Type())
dmosMemNotificationInterval.setMaxAccess(_M)
if mibBuilder.loadTexts:dmosMemNotificationInterval.setStatus(_C)
if mibBuilder.loadTexts:dmosMemNotificationInterval.setUnits('seconds')
_DmosMemNotificationGroups_ObjectIdentity=ObjectIdentity
dmosMemNotificationGroups=_DmosMemNotificationGroups_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,3,1,2))
dmosMemAlarmInfoGroup=ObjectGroup((1,3,6,1,4,1,3709,3,6,3,3,1,2,1))
dmosMemAlarmInfoGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:dmosMemAlarmInfoGroup.setStatus(_C)
memAvailableLowTrap=NotificationType((1,3,6,1,4,1,3709,3,6,3,3,1,3))
memAvailableLowTrap.setObjects(*((_A,_L),(_A,_H),(_A,_J),(_A,_K),(_A,_I),(_A,_G),(_A,_F),(_B,_D),(_B,_E)))
if mibBuilder.loadTexts:memAvailableLowTrap.setStatus(_C)
dmosMemAlarmTrapsGroup=NotificationGroup((1,3,6,1,4,1,3709,3,6,3,3,1,2,2))
dmosMemAlarmTrapsGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:dmosMemAlarmTrapsGroup.setStatus(_C)
mibBuilder.exportSymbols(_B,**{'dmosMemNotificationsMIB':dmosMemNotificationsMIB,'dmosMemNotificationObjects':dmosMemNotificationObjects,_D:dmosMemNotificationThreshold,_E:dmosMemNotificationInterval,'dmosMemNotificationGroups':dmosMemNotificationGroups,'dmosMemAlarmInfoGroup':dmosMemAlarmInfoGroup,'dmosMemAlarmTrapsGroup':dmosMemAlarmTrapsGroup,_N:memAvailableLowTrap})