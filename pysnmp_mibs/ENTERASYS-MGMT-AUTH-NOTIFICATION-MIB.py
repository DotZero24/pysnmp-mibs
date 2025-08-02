_T='etsysMgmtAuthNotificationUserGroup'
_S='etsysMgmtAuthNotificationGroup'
_R='etsysMgmtAuthHistoryGroup'
_Q='etsysMgmtAuthConfigGroup'
_P='etsysMgmtAuthMaxFailNotification'
_O='etsysMgmtAuthMaxAuthAttemptNotification'
_N='etsysMgmtAuthInactiveNotification'
_M='etsysMgmtAuthFailNotificiation'
_L='etsysMgmtAuthSuccessNotificiation'
_K='etsysMgmtAuthNotificationEnabledStatus'
_J='etsysMgmtAuthNotificationsSupported'
_I='EtsysMgmtAuthNotificationTypes'
_H='accessible-for-notify'
_G='etsysMgmtAuthInIfIndex'
_F='etsysMgmtAuthInetAddress'
_E='etsysMgmtAuthInetAddressType'
_D='etsysMgmtAuthUserName'
_C='etsysMgmtAuthType'
_B='current'
_A='ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysMgmtAuthNotificationMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,60))
if mibBuilder.loadTexts:etsysMgmtAuthNotificationMIB.setRevisions(('2011-03-08 20:40','2005-11-14 16:48'))
class EtsysMgmtAuthNotificationTypes(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('cliConsole',0),('cliSsh',1),('cliTelnet',2),('webview',3),('inactiveUser',4),('maxUserAttempt',5),('maxUserFail',6)))
_EtsysMgmtAuthObjects_ObjectIdentity=ObjectIdentity
etsysMgmtAuthObjects=_EtsysMgmtAuthObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,60,1))
_EtsysMgmtAuthNotificationBranch_ObjectIdentity=ObjectIdentity
etsysMgmtAuthNotificationBranch=_EtsysMgmtAuthNotificationBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,60,1,0))
_EtsysMgmtAuthConfigBranch_ObjectIdentity=ObjectIdentity
etsysMgmtAuthConfigBranch=_EtsysMgmtAuthConfigBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,60,1,1))
class _EtsysMgmtAuthNotificationsSupported_Type(EtsysMgmtAuthNotificationTypes):defaultBinValue='0'
_EtsysMgmtAuthNotificationsSupported_Type.__name__=_I
_EtsysMgmtAuthNotificationsSupported_Object=MibScalar
etsysMgmtAuthNotificationsSupported=_EtsysMgmtAuthNotificationsSupported_Object((1,3,6,1,4,1,5624,1,2,60,1,1,1),_EtsysMgmtAuthNotificationsSupported_Type())
etsysMgmtAuthNotificationsSupported.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsysMgmtAuthNotificationsSupported.setStatus(_B)
class _EtsysMgmtAuthNotificationEnabledStatus_Type(EtsysMgmtAuthNotificationTypes):defaultBinValue='0'
_EtsysMgmtAuthNotificationEnabledStatus_Type.__name__=_I
_EtsysMgmtAuthNotificationEnabledStatus_Object=MibScalar
etsysMgmtAuthNotificationEnabledStatus=_EtsysMgmtAuthNotificationEnabledStatus_Object((1,3,6,1,4,1,5624,1,2,60,1,1,2),_EtsysMgmtAuthNotificationEnabledStatus_Type())
etsysMgmtAuthNotificationEnabledStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:etsysMgmtAuthNotificationEnabledStatus.setStatus(_B)
_EtsysMgmtAuthAuthenticationBranch_ObjectIdentity=ObjectIdentity
etsysMgmtAuthAuthenticationBranch=_EtsysMgmtAuthAuthenticationBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,60,1,2))
_EtsysMgmtAuthType_Type=EtsysMgmtAuthNotificationTypes
_EtsysMgmtAuthType_Object=MibScalar
etsysMgmtAuthType=_EtsysMgmtAuthType_Object((1,3,6,1,4,1,5624,1,2,60,1,2,1),_EtsysMgmtAuthType_Type())
etsysMgmtAuthType.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysMgmtAuthType.setStatus(_B)
_EtsysMgmtAuthUserName_Type=DisplayString
_EtsysMgmtAuthUserName_Object=MibScalar
etsysMgmtAuthUserName=_EtsysMgmtAuthUserName_Object((1,3,6,1,4,1,5624,1,2,60,1,2,2),_EtsysMgmtAuthUserName_Type())
etsysMgmtAuthUserName.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysMgmtAuthUserName.setStatus(_B)
_EtsysMgmtAuthInetAddressType_Type=InetAddressType
_EtsysMgmtAuthInetAddressType_Object=MibScalar
etsysMgmtAuthInetAddressType=_EtsysMgmtAuthInetAddressType_Object((1,3,6,1,4,1,5624,1,2,60,1,2,3),_EtsysMgmtAuthInetAddressType_Type())
etsysMgmtAuthInetAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysMgmtAuthInetAddressType.setStatus(_B)
_EtsysMgmtAuthInetAddress_Type=InetAddress
_EtsysMgmtAuthInetAddress_Object=MibScalar
etsysMgmtAuthInetAddress=_EtsysMgmtAuthInetAddress_Object((1,3,6,1,4,1,5624,1,2,60,1,2,4),_EtsysMgmtAuthInetAddress_Type())
etsysMgmtAuthInetAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysMgmtAuthInetAddress.setStatus(_B)
_EtsysMgmtAuthInIfIndex_Type=InterfaceIndexOrZero
_EtsysMgmtAuthInIfIndex_Object=MibScalar
etsysMgmtAuthInIfIndex=_EtsysMgmtAuthInIfIndex_Object((1,3,6,1,4,1,5624,1,2,60,1,2,5),_EtsysMgmtAuthInIfIndex_Type())
etsysMgmtAuthInIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysMgmtAuthInIfIndex.setStatus(_B)
_EtsysMgmtAuthConformance_ObjectIdentity=ObjectIdentity
etsysMgmtAuthConformance=_EtsysMgmtAuthConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,60,2))
_EtsysMgmtAuthGroups_ObjectIdentity=ObjectIdentity
etsysMgmtAuthGroups=_EtsysMgmtAuthGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,60,2,1))
_EtsysMgmtAuthCompliances_ObjectIdentity=ObjectIdentity
etsysMgmtAuthCompliances=_EtsysMgmtAuthCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,60,2,2))
etsysMgmtAuthConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,60,2,1,1))
etsysMgmtAuthConfigGroup.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:etsysMgmtAuthConfigGroup.setStatus(_B)
etsysMgmtAuthHistoryGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,60,2,1,2))
etsysMgmtAuthHistoryGroup.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:etsysMgmtAuthHistoryGroup.setStatus(_B)
etsysMgmtAuthSuccessNotificiation=NotificationType((1,3,6,1,4,1,5624,1,2,60,1,0,1))
etsysMgmtAuthSuccessNotificiation.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:etsysMgmtAuthSuccessNotificiation.setStatus(_B)
etsysMgmtAuthFailNotificiation=NotificationType((1,3,6,1,4,1,5624,1,2,60,1,0,2))
etsysMgmtAuthFailNotificiation.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:etsysMgmtAuthFailNotificiation.setStatus(_B)
etsysMgmtAuthInactiveNotification=NotificationType((1,3,6,1,4,1,5624,1,2,60,1,0,3))
etsysMgmtAuthInactiveNotification.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:etsysMgmtAuthInactiveNotification.setStatus(_B)
etsysMgmtAuthMaxAuthAttemptNotification=NotificationType((1,3,6,1,4,1,5624,1,2,60,1,0,4))
etsysMgmtAuthMaxAuthAttemptNotification.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:etsysMgmtAuthMaxAuthAttemptNotification.setStatus(_B)
etsysMgmtAuthMaxFailNotification=NotificationType((1,3,6,1,4,1,5624,1,2,60,1,0,5))
etsysMgmtAuthMaxFailNotification.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:etsysMgmtAuthMaxFailNotification.setStatus(_B)
etsysMgmtAuthNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,60,2,1,3))
etsysMgmtAuthNotificationGroup.setObjects(*((_A,_L),(_A,_M)))
if mibBuilder.loadTexts:etsysMgmtAuthNotificationGroup.setStatus(_B)
etsysMgmtAuthNotificationUserGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,60,2,1,4))
etsysMgmtAuthNotificationUserGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:etsysMgmtAuthNotificationUserGroup.setStatus(_B)
etsysMgmtAuthCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,60,2,2,1))
etsysMgmtAuthCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:etsysMgmtAuthCompliance.setStatus(_B)
etsysMgmtAuthUserCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,60,2,2,2))
etsysMgmtAuthUserCompliance.setObjects((_A,_T))
if mibBuilder.loadTexts:etsysMgmtAuthUserCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_I:EtsysMgmtAuthNotificationTypes,'etsysMgmtAuthNotificationMIB':etsysMgmtAuthNotificationMIB,'etsysMgmtAuthObjects':etsysMgmtAuthObjects,'etsysMgmtAuthNotificationBranch':etsysMgmtAuthNotificationBranch,_L:etsysMgmtAuthSuccessNotificiation,_M:etsysMgmtAuthFailNotificiation,_N:etsysMgmtAuthInactiveNotification,_O:etsysMgmtAuthMaxAuthAttemptNotification,_P:etsysMgmtAuthMaxFailNotification,'etsysMgmtAuthConfigBranch':etsysMgmtAuthConfigBranch,_J:etsysMgmtAuthNotificationsSupported,_K:etsysMgmtAuthNotificationEnabledStatus,'etsysMgmtAuthAuthenticationBranch':etsysMgmtAuthAuthenticationBranch,_C:etsysMgmtAuthType,_D:etsysMgmtAuthUserName,_E:etsysMgmtAuthInetAddressType,_F:etsysMgmtAuthInetAddress,_G:etsysMgmtAuthInIfIndex,'etsysMgmtAuthConformance':etsysMgmtAuthConformance,'etsysMgmtAuthGroups':etsysMgmtAuthGroups,_Q:etsysMgmtAuthConfigGroup,_R:etsysMgmtAuthHistoryGroup,_S:etsysMgmtAuthNotificationGroup,_T:etsysMgmtAuthNotificationUserGroup,'etsysMgmtAuthCompliances':etsysMgmtAuthCompliances,'etsysMgmtAuthCompliance':etsysMgmtAuthCompliance,'etsysMgmtAuthUserCompliance':etsysMgmtAuthUserCompliance})