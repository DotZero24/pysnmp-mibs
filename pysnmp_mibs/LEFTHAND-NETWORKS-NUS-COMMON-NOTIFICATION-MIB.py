_F='userNotification'
_E='notificationMessage'
_D='notificationIndex'
_C='LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG','lhnModules')
lhnNusCommonEvents,lhnNusCommonGroups,lhnNusCommonNotification=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NUS-COMMON-MIB','lhnNusCommonEvents','lhnNusCommonGroups','lhnNusCommonNotification')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lhnNusCommonNotificationModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,15))
_NotificationMessageCount_Type=Integer32
_NotificationMessageCount_Object=MibScalar
notificationMessageCount=_NotificationMessageCount_Object((1,3,6,1,4,1,9804,3,1,1,2,13,1),_NotificationMessageCount_Type())
notificationMessageCount.setMaxAccess(_B)
if mibBuilder.loadTexts:notificationMessageCount.setStatus(_A)
_NotificationMessageTable_Object=MibTable
notificationMessageTable=_NotificationMessageTable_Object((1,3,6,1,4,1,9804,3,1,1,2,13,2))
if mibBuilder.loadTexts:notificationMessageTable.setStatus(_A)
_NotificationMessageEntry_Object=MibTableRow
notificationMessageEntry=_NotificationMessageEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,13,2,1))
notificationMessageEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:notificationMessageEntry.setStatus(_A)
_NotificationIndex_Type=Integer32
_NotificationIndex_Object=MibTableColumn
notificationIndex=_NotificationIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,13,2,1,1),_NotificationIndex_Type())
notificationIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:notificationIndex.setStatus(_A)
_NotificationMessage_Type=OctetString
_NotificationMessage_Object=MibTableColumn
notificationMessage=_NotificationMessage_Object((1,3,6,1,4,1,9804,3,1,1,2,13,2,1,2),_NotificationMessage_Type())
notificationMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:notificationMessage.setStatus(_A)
_NotificationTime_Type=DateAndTime
_NotificationTime_Object=MibTableColumn
notificationTime=_NotificationTime_Object((1,3,6,1,4,1,9804,3,1,1,2,13,2,1,3),_NotificationTime_Type())
notificationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:notificationTime.setStatus(_A)
userNotification=NotificationType((1,3,6,1,4,1,9804,3,1,1,3,1))
userNotification.setObjects((_C,_E))
if mibBuilder.loadTexts:userNotification.setStatus(_A)
lhnNusCommonEventGroup=NotificationGroup((1,3,6,1,4,1,9804,3,1,1,1,1,2))
lhnNusCommonEventGroup.setObjects((_C,_F))
if mibBuilder.loadTexts:lhnNusCommonEventGroup.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'lhnNusCommonNotificationModule':lhnNusCommonNotificationModule,'lhnNusCommonEventGroup':lhnNusCommonEventGroup,'notificationMessageCount':notificationMessageCount,'notificationMessageTable':notificationMessageTable,'notificationMessageEntry':notificationMessageEntry,_D:notificationIndex,_E:notificationMessage,'notificationTime':notificationTime,_F:userNotification})