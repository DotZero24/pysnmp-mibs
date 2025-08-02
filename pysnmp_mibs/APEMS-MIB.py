_T='apEMSNodeUnreachableClear'
_S='apEMSNodeUnreachable'
_R='apEMSInvalidConfigDiscovered'
_Q='apEMSActivateFailure'
_P='apEMSSaveFailure'
_O='apEMSDiscoveryFailure'
_N='reDiscovery'
_M='discovery'
_L='unknown'
_K='apEMSFunction'
_J='apEMSDiscoveryMode'
_I='Integer32'
_H='apEMSDeviceAddress'
_G='apEMSUser'
_F='apEMSStartTime'
_E='apEMSNodeID'
_D='accessible-for-notify'
_C='apEMSDateTime'
_B='current'
_A='APEMS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
apEMSModule=ModuleIdentity((1,3,6,1,4,1,9148,3,8))
if mibBuilder.loadTexts:apEMSModule.setRevisions(('2012-07-16 00:00',))
_ApEMSMIBObjects_ObjectIdentity=ObjectIdentity
apEMSMIBObjects=_ApEMSMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,8,1))
_ApEMSNotificationObjects_ObjectIdentity=ObjectIdentity
apEMSNotificationObjects=_ApEMSNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,8,2))
class _ApEMSDiscoveryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2)))
_ApEMSDiscoveryMode_Type.__name__=_I
_ApEMSDiscoveryMode_Object=MibScalar
apEMSDiscoveryMode=_ApEMSDiscoveryMode_Object((1,3,6,1,4,1,9148,3,8,2,1),_ApEMSDiscoveryMode_Type())
apEMSDiscoveryMode.setMaxAccess(_D)
if mibBuilder.loadTexts:apEMSDiscoveryMode.setStatus(_B)
_ApEMSNodeID_Type=DisplayString
_ApEMSNodeID_Object=MibScalar
apEMSNodeID=_ApEMSNodeID_Object((1,3,6,1,4,1,9148,3,8,2,2),_ApEMSNodeID_Type())
apEMSNodeID.setMaxAccess(_D)
if mibBuilder.loadTexts:apEMSNodeID.setStatus(_B)
_ApEMSStartTime_Type=DisplayString
_ApEMSStartTime_Object=MibScalar
apEMSStartTime=_ApEMSStartTime_Object((1,3,6,1,4,1,9148,3,8,2,3),_ApEMSStartTime_Type())
apEMSStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:apEMSStartTime.setStatus(_B)
_ApEMSDateTime_Type=DisplayString
_ApEMSDateTime_Object=MibScalar
apEMSDateTime=_ApEMSDateTime_Object((1,3,6,1,4,1,9148,3,8,2,4),_ApEMSDateTime_Type())
apEMSDateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:apEMSDateTime.setStatus(_B)
_ApEMSUser_Type=DisplayString
_ApEMSUser_Object=MibScalar
apEMSUser=_ApEMSUser_Object((1,3,6,1,4,1,9148,3,8,2,5),_ApEMSUser_Type())
apEMSUser.setMaxAccess(_D)
if mibBuilder.loadTexts:apEMSUser.setStatus(_B)
_ApEMSDeviceAddress_Type=DisplayString
_ApEMSDeviceAddress_Object=MibScalar
apEMSDeviceAddress=_ApEMSDeviceAddress_Object((1,3,6,1,4,1,9148,3,8,2,6),_ApEMSDeviceAddress_Type())
apEMSDeviceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:apEMSDeviceAddress.setStatus(_B)
class _ApEMSFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),('save',3)))
_ApEMSFunction_Type.__name__=_I
_ApEMSFunction_Object=MibScalar
apEMSFunction=_ApEMSFunction_Object((1,3,6,1,4,1,9148,3,8,2,7),_ApEMSFunction_Type())
apEMSFunction.setMaxAccess(_D)
if mibBuilder.loadTexts:apEMSFunction.setStatus(_B)
_ApEMSNotifications_ObjectIdentity=ObjectIdentity
apEMSNotifications=_ApEMSNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,8,3))
_ApEMSConfigNotificationsPrefix_ObjectIdentity=ObjectIdentity
apEMSConfigNotificationsPrefix=_ApEMSConfigNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,8,3,1))
_ApEMSConfigNotifications_ObjectIdentity=ObjectIdentity
apEMSConfigNotifications=_ApEMSConfigNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,8,3,1,0))
_ApEMSDeviceHealthNotificationsPrefix_ObjectIdentity=ObjectIdentity
apEMSDeviceHealthNotificationsPrefix=_ApEMSDeviceHealthNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,8,3,2))
_ApEMSDeviceHealthNotifications_ObjectIdentity=ObjectIdentity
apEMSDeviceHealthNotifications=_ApEMSDeviceHealthNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,8,3,2,0))
_ApEMSModuleConformance_ObjectIdentity=ObjectIdentity
apEMSModuleConformance=_ApEMSModuleConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,8,4))
_ApEMSGroups_ObjectIdentity=ObjectIdentity
apEMSGroups=_ApEMSGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,8,4,1))
_ApEMSNotificationsGroups_ObjectIdentity=ObjectIdentity
apEMSNotificationsGroups=_ApEMSNotificationsGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,8,4,2))
_ApEMSNotificationObjectsGroups_ObjectIdentity=ObjectIdentity
apEMSNotificationObjectsGroups=_ApEMSNotificationObjectsGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,8,4,3))
apEMSNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,8,4,3,1))
apEMSNotificationObjectsGroup.setObjects(*((_A,_J),(_A,_E),(_A,_F),(_A,_C),(_A,_G),(_A,_H),(_A,_K)))
if mibBuilder.loadTexts:apEMSNotificationObjectsGroup.setStatus(_B)
apEMSDiscoveryFailure=NotificationType((1,3,6,1,4,1,9148,3,8,3,1,0,1))
apEMSDiscoveryFailure.setObjects(*((_A,_J),(_A,_E),(_A,_F),(_A,_C),(_A,_G)))
if mibBuilder.loadTexts:apEMSDiscoveryFailure.setStatus(_B)
apEMSSaveFailure=NotificationType((1,3,6,1,4,1,9148,3,8,3,1,0,2))
apEMSSaveFailure.setObjects(*((_A,_E),(_A,_F),(_A,_C),(_A,_G)))
if mibBuilder.loadTexts:apEMSSaveFailure.setStatus(_B)
apEMSActivateFailure=NotificationType((1,3,6,1,4,1,9148,3,8,3,1,0,3))
apEMSActivateFailure.setObjects(*((_A,_E),(_A,_F),(_A,_C),(_A,_G)))
if mibBuilder.loadTexts:apEMSActivateFailure.setStatus(_B)
apEMSInvalidConfigDiscovered=NotificationType((1,3,6,1,4,1,9148,3,8,3,1,0,4))
apEMSInvalidConfigDiscovered.setObjects(*((_A,_E),(_A,_C)))
if mibBuilder.loadTexts:apEMSInvalidConfigDiscovered.setStatus(_B)
apEMSInvalidConfigInventory=NotificationType((1,3,6,1,4,1,9148,3,8,3,1,0,5))
apEMSInvalidConfigInventory.setObjects(*((_A,_K),(_A,_E),(_A,_F),(_A,_C),(_A,_G)))
if mibBuilder.loadTexts:apEMSInvalidConfigInventory.setStatus(_B)
apEMSNodeUnreachable=NotificationType((1,3,6,1,4,1,9148,3,8,3,2,0,1))
apEMSNodeUnreachable.setObjects(*((_A,_H),(_A,_C)))
if mibBuilder.loadTexts:apEMSNodeUnreachable.setStatus(_B)
apEMSNodeUnreachableClear=NotificationType((1,3,6,1,4,1,9148,3,8,3,2,0,2))
apEMSNodeUnreachableClear.setObjects(*((_A,_H),(_A,_C)))
if mibBuilder.loadTexts:apEMSNodeUnreachableClear.setStatus(_B)
apEMSConfigNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,8,4,2,1))
apEMSConfigNotificationsGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:apEMSConfigNotificationsGroup.setStatus(_B)
apEMSDeviceHealthNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,8,4,2,2))
apEMSDeviceHealthNotificationsGroup.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:apEMSDeviceHealthNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'apEMSModule':apEMSModule,'apEMSMIBObjects':apEMSMIBObjects,'apEMSNotificationObjects':apEMSNotificationObjects,_J:apEMSDiscoveryMode,_E:apEMSNodeID,_F:apEMSStartTime,_C:apEMSDateTime,_G:apEMSUser,_H:apEMSDeviceAddress,_K:apEMSFunction,'apEMSNotifications':apEMSNotifications,'apEMSConfigNotificationsPrefix':apEMSConfigNotificationsPrefix,'apEMSConfigNotifications':apEMSConfigNotifications,_O:apEMSDiscoveryFailure,_P:apEMSSaveFailure,_Q:apEMSActivateFailure,_R:apEMSInvalidConfigDiscovered,'apEMSInvalidConfigInventory':apEMSInvalidConfigInventory,'apEMSDeviceHealthNotificationsPrefix':apEMSDeviceHealthNotificationsPrefix,'apEMSDeviceHealthNotifications':apEMSDeviceHealthNotifications,_S:apEMSNodeUnreachable,_T:apEMSNodeUnreachableClear,'apEMSModuleConformance':apEMSModuleConformance,'apEMSGroups':apEMSGroups,'apEMSNotificationsGroups':apEMSNotificationsGroups,'apEMSConfigNotificationsGroup':apEMSConfigNotificationsGroup,'apEMSDeviceHealthNotificationsGroup':apEMSDeviceHealthNotificationsGroup,'apEMSNotificationObjectsGroups':apEMSNotificationObjectsGroups,'apEMSNotificationObjectsGroup':apEMSNotificationObjectsGroup})