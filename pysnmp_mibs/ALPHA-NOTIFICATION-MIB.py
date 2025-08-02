_S='alphaNotificationsGroup'
_R='alphaParameterGroup'
_Q='alphaAlarmClearState'
_P='alphaAlarmActiveState'
_O='controllerInfoName'
_N='componentListStaticName'
_M='componentListReference'
_L='alarmModelDescription'
_K='alarmActiveResourceId'
_J='alarmActiveModelPointer'
_I='alarmAdditionalInformation'
_H='alarmPriority'
_G='alarmCustomDescription'
_F='alarmSeverity'
_E='read-only'
_D='ALPHA-RESOURCE-MIB'
_C='ALARM-MIB'
_B='current'
_A='ALPHA-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmActiveModelPointer,alarmActiveResourceId,alarmModelDescription=mibBuilder.importSymbols(_C,_J,_K,_L)
alpha,componentListReference,componentListStaticName,controllerInfoName=mibBuilder.importSymbols(_D,'alpha',_M,_N,_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alphaAlarmNotifications=ModuleIdentity((1,3,6,1,4,1,7309,100))
if mibBuilder.loadTexts:alphaAlarmNotifications.setRevisions(('2017-07-31 00:00','2015-07-28 00:00','2015-07-23 00:00','2015-06-23 00:00'))
_AlphaAlarmNotificationConformance_ObjectIdentity=ObjectIdentity
alphaAlarmNotificationConformance=_AlphaAlarmNotificationConformance_ObjectIdentity((1,3,6,1,4,1,7309,100,102))
_AlphaAlarmNotificationCompliances_ObjectIdentity=ObjectIdentity
alphaAlarmNotificationCompliances=_AlphaAlarmNotificationCompliances_ObjectIdentity((1,3,6,1,4,1,7309,100,102,1))
_AlphaAlarmNotificationGroups_ObjectIdentity=ObjectIdentity
alphaAlarmNotificationGroups=_AlphaAlarmNotificationGroups_ObjectIdentity((1,3,6,1,4,1,7309,100,102,1,2))
_AlphaAlarmNotificationsExtension_ObjectIdentity=ObjectIdentity
alphaAlarmNotificationsExtension=_AlphaAlarmNotificationsExtension_ObjectIdentity((1,3,6,1,4,1,7309,101))
_AlarmSeverity_Type=Integer32
_AlarmSeverity_Object=MibScalar
alarmSeverity=_AlarmSeverity_Object((1,3,6,1,4,1,7309,101,1),_AlarmSeverity_Type())
alarmSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:alarmSeverity.setStatus(_B)
_AlarmCustomDescription_Type=OctetString
_AlarmCustomDescription_Object=MibScalar
alarmCustomDescription=_AlarmCustomDescription_Object((1,3,6,1,4,1,7309,101,2),_AlarmCustomDescription_Type())
alarmCustomDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:alarmCustomDescription.setStatus(_B)
_AlarmPriority_Type=OctetString
_AlarmPriority_Object=MibScalar
alarmPriority=_AlarmPriority_Object((1,3,6,1,4,1,7309,101,3),_AlarmPriority_Type())
alarmPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:alarmPriority.setStatus(_B)
_AlarmAdditionalInformation_Type=OctetString
_AlarmAdditionalInformation_Object=MibScalar
alarmAdditionalInformation=_AlarmAdditionalInformation_Object((1,3,6,1,4,1,7309,101,4),_AlarmAdditionalInformation_Type())
alarmAdditionalInformation.setMaxAccess(_E)
if mibBuilder.loadTexts:alarmAdditionalInformation.setStatus(_B)
alphaParameterGroup=ObjectGroup((1,3,6,1,4,1,7309,100,102,1,2,1))
alphaParameterGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:alphaParameterGroup.setStatus(_B)
alphaAlarmActiveState=NotificationType((1,3,6,1,4,1,7309,100,1))
alphaAlarmActiveState.setObjects(*((_C,_J),(_C,_K),(_A,_H),(_C,_L),(_D,_N),(_D,_M),(_A,_F),(_D,_O),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:alphaAlarmActiveState.setStatus(_B)
alphaAlarmClearState=NotificationType((1,3,6,1,4,1,7309,100,2))
alphaAlarmClearState.setObjects(*((_C,_J),(_C,_K),(_A,_H),(_C,_L),(_D,_N),(_D,_M),(_A,_F),(_D,_O),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:alphaAlarmClearState.setStatus(_B)
alphaNotificationsGroup=NotificationGroup((1,3,6,1,4,1,7309,100,102,1,2,2))
alphaNotificationsGroup.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:alphaNotificationsGroup.setStatus(_B)
alphaAlarmNotificationCompliance=ModuleCompliance((1,3,6,1,4,1,7309,100,102,1,1))
alphaAlarmNotificationCompliance.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:alphaAlarmNotificationCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alphaAlarmNotifications':alphaAlarmNotifications,_P:alphaAlarmActiveState,_Q:alphaAlarmClearState,'alphaAlarmNotificationConformance':alphaAlarmNotificationConformance,'alphaAlarmNotificationCompliances':alphaAlarmNotificationCompliances,'alphaAlarmNotificationCompliance':alphaAlarmNotificationCompliance,'alphaAlarmNotificationGroups':alphaAlarmNotificationGroups,_R:alphaParameterGroup,_S:alphaNotificationsGroup,'alphaAlarmNotificationsExtension':alphaAlarmNotificationsExtension,_F:alarmSeverity,_G:alarmCustomDescription,_H:alarmPriority,_I:alarmAdditionalInformation})