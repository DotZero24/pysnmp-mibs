_I='apNNCServerUnreachableClear'
_H='apNNCServerUnreachable'
_G='apNNCServerNameRemote'
_F='apNNCServerAddressRemote'
_E='apNNCServerNameLocal'
_D='apNNCServerAddressLocal'
_C='accessible-for-notify'
_B='current'
_A='APNNC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
apEMSModule,=mibBuilder.importSymbols('APEMS-MIB','apEMSModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
apNNCModule=ModuleIdentity((1,3,6,1,4,1,9148,3,8,5))
if mibBuilder.loadTexts:apNNCModule.setRevisions(('2012-07-16 00:00',))
_ApNNCMIBObjects_ObjectIdentity=ObjectIdentity
apNNCMIBObjects=_ApNNCMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,1))
_ApNNCNotificationObjects_ObjectIdentity=ObjectIdentity
apNNCNotificationObjects=_ApNNCNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,2))
_ApNNCServerAddressRemote_Type=DisplayString
_ApNNCServerAddressRemote_Object=MibScalar
apNNCServerAddressRemote=_ApNNCServerAddressRemote_Object((1,3,6,1,4,1,9148,3,8,5,2,1),_ApNNCServerAddressRemote_Type())
apNNCServerAddressRemote.setMaxAccess(_C)
if mibBuilder.loadTexts:apNNCServerAddressRemote.setStatus(_B)
_ApNNCServerNameRemote_Type=DisplayString
_ApNNCServerNameRemote_Object=MibScalar
apNNCServerNameRemote=_ApNNCServerNameRemote_Object((1,3,6,1,4,1,9148,3,8,5,2,2),_ApNNCServerNameRemote_Type())
apNNCServerNameRemote.setMaxAccess(_C)
if mibBuilder.loadTexts:apNNCServerNameRemote.setStatus(_B)
_ApNNCServerAddressLocal_Type=DisplayString
_ApNNCServerAddressLocal_Object=MibScalar
apNNCServerAddressLocal=_ApNNCServerAddressLocal_Object((1,3,6,1,4,1,9148,3,8,5,2,3),_ApNNCServerAddressLocal_Type())
apNNCServerAddressLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:apNNCServerAddressLocal.setStatus(_B)
_ApNNCServerNameLocal_Type=DisplayString
_ApNNCServerNameLocal_Object=MibScalar
apNNCServerNameLocal=_ApNNCServerNameLocal_Object((1,3,6,1,4,1,9148,3,8,5,2,4),_ApNNCServerNameLocal_Type())
apNNCServerNameLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:apNNCServerNameLocal.setStatus(_B)
_ApNNCNotifications_ObjectIdentity=ObjectIdentity
apNNCNotifications=_ApNNCNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,3))
_ApNNCConfigNotificationsPrefix_ObjectIdentity=ObjectIdentity
apNNCConfigNotificationsPrefix=_ApNNCConfigNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,3,1))
_ApNNCServerHealthNotificationsPrefix_ObjectIdentity=ObjectIdentity
apNNCServerHealthNotificationsPrefix=_ApNNCServerHealthNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,3,1))
_ApNNCConfigNotifications_ObjectIdentity=ObjectIdentity
apNNCConfigNotifications=_ApNNCConfigNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,3,1,0))
_ApNNCServerHealthNotifications_ObjectIdentity=ObjectIdentity
apNNCServerHealthNotifications=_ApNNCServerHealthNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,3,1,0))
_ApNNCModuleConformance_ObjectIdentity=ObjectIdentity
apNNCModuleConformance=_ApNNCModuleConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,4))
_ApNNCGroups_ObjectIdentity=ObjectIdentity
apNNCGroups=_ApNNCGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,4,1))
_ApNNCNotificationsGroups_ObjectIdentity=ObjectIdentity
apNNCNotificationsGroups=_ApNNCNotificationsGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,4,2))
_ApNNCNotificationObjectsGroups_ObjectIdentity=ObjectIdentity
apNNCNotificationObjectsGroups=_ApNNCNotificationObjectsGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,8,5,4,3))
apNNCServerHealthObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,8,5,4,3,1))
apNNCServerHealthObjectsGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:apNNCServerHealthObjectsGroup.setStatus(_B)
apNNCServerUnreachable=NotificationType((1,3,6,1,4,1,9148,3,8,5,3,1,0,1))
apNNCServerUnreachable.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:apNNCServerUnreachable.setStatus(_B)
apNNCServerUnreachableClear=NotificationType((1,3,6,1,4,1,9148,3,8,5,3,1,0,2))
apNNCServerUnreachableClear.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:apNNCServerUnreachableClear.setStatus(_B)
apNNCServerHealthNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,8,5,4,2,1))
apNNCServerHealthNotificationsGroup.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:apNNCServerHealthNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'apNNCModule':apNNCModule,'apNNCMIBObjects':apNNCMIBObjects,'apNNCNotificationObjects':apNNCNotificationObjects,_F:apNNCServerAddressRemote,_G:apNNCServerNameRemote,_D:apNNCServerAddressLocal,_E:apNNCServerNameLocal,'apNNCNotifications':apNNCNotifications,'apNNCConfigNotificationsPrefix':apNNCConfigNotificationsPrefix,'apNNCServerHealthNotificationsPrefix':apNNCServerHealthNotificationsPrefix,'apNNCConfigNotifications':apNNCConfigNotifications,'apNNCServerHealthNotifications':apNNCServerHealthNotifications,_H:apNNCServerUnreachable,_I:apNNCServerUnreachableClear,'apNNCModuleConformance':apNNCModuleConformance,'apNNCGroups':apNNCGroups,'apNNCNotificationsGroups':apNNCNotificationsGroups,'apNNCServerHealthNotificationsGroup':apNNCServerHealthNotificationsGroup,'apNNCNotificationObjectsGroups':apNNCNotificationObjectsGroups,'apNNCServerHealthObjectsGroup':apNNCServerHealthObjectsGroup})