_K='notificationAlarmState'
_J='notificationSeverity'
_I='notificationInfo'
_H='notificationSourceValue'
_G='notificationSourceType'
_F='notificationName'
_E='notificationTime'
_D='Integer32'
_C='accessible-for-notify'
_B='DMOS-NOTIFICATIONS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
datacomDevicesMIBs,=mibBuilder.importSymbols('DATACOM-SMI','datacomDevicesMIBs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
dmosNotificationsMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,6,3))
if mibBuilder.loadTexts:dmosNotificationsMIB.setRevisions(('2016-10-20 00:00',))
_NotificationObjects_ObjectIdentity=ObjectIdentity
notificationObjects=_NotificationObjects_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,1))
_NotificationTime_Type=DateAndTime
_NotificationTime_Object=MibScalar
notificationTime=_NotificationTime_Object((1,3,6,1,4,1,3709,3,6,3,1,1),_NotificationTime_Type())
notificationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:notificationTime.setStatus(_A)
_NotificationName_Type=DisplayString
_NotificationName_Object=MibScalar
notificationName=_NotificationName_Object((1,3,6,1,4,1,3709,3,6,3,1,2),_NotificationName_Type())
notificationName.setMaxAccess(_C)
if mibBuilder.loadTexts:notificationName.setStatus(_A)
_NotificationSourceType_Type=DisplayString
_NotificationSourceType_Object=MibScalar
notificationSourceType=_NotificationSourceType_Object((1,3,6,1,4,1,3709,3,6,3,1,3),_NotificationSourceType_Type())
notificationSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:notificationSourceType.setStatus(_A)
_NotificationSourceValue_Type=DisplayString
_NotificationSourceValue_Object=MibScalar
notificationSourceValue=_NotificationSourceValue_Object((1,3,6,1,4,1,3709,3,6,3,1,4),_NotificationSourceValue_Type())
notificationSourceValue.setMaxAccess(_C)
if mibBuilder.loadTexts:notificationSourceValue.setStatus(_A)
_NotificationSeverity_Type=DisplayString
_NotificationSeverity_Object=MibScalar
notificationSeverity=_NotificationSeverity_Object((1,3,6,1,4,1,3709,3,6,3,1,5),_NotificationSeverity_Type())
notificationSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:notificationSeverity.setStatus(_A)
_NotificationInfo_Type=DisplayString
_NotificationInfo_Object=MibScalar
notificationInfo=_NotificationInfo_Object((1,3,6,1,4,1,3709,3,6,3,1,6),_NotificationInfo_Type())
notificationInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:notificationInfo.setStatus(_A)
class _NotificationAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('clear',1),('set',2),('unstable',3)))
_NotificationAlarmState_Type.__name__=_D
_NotificationAlarmState_Object=MibScalar
notificationAlarmState=_NotificationAlarmState_Object((1,3,6,1,4,1,3709,3,6,3,1,7),_NotificationAlarmState_Type())
notificationAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:notificationAlarmState.setStatus(_A)
_NotificationGroups_ObjectIdentity=ObjectIdentity
notificationGroups=_NotificationGroups_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,2))
_AlarmNotifications_ObjectIdentity=ObjectIdentity
alarmNotifications=_AlarmNotifications_ObjectIdentity((1,3,6,1,4,1,3709,3,6,3,3))
infoNotificationGroup=ObjectGroup((1,3,6,1,4,1,3709,3,6,3,2,1))
infoNotificationGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:infoNotificationGroup.setStatus(_A)
alarmNotificationGroup=ObjectGroup((1,3,6,1,4,1,3709,3,6,3,2,2))
alarmNotificationGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:alarmNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dmosNotificationsMIB':dmosNotificationsMIB,'notificationObjects':notificationObjects,_E:notificationTime,_F:notificationName,_G:notificationSourceType,_H:notificationSourceValue,_J:notificationSeverity,_I:notificationInfo,_K:notificationAlarmState,'notificationGroups':notificationGroups,'infoNotificationGroup':infoNotificationGroup,'alarmNotificationGroup':alarmNotificationGroup,'alarmNotifications':alarmNotifications})