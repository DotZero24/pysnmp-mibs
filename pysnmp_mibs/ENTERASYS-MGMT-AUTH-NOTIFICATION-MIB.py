#
# PySNMP MIB module ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysMgmtAuthNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60))
etsysMgmtAuthNotificationMIB.setRevisions(('2011-03-08 20:40', '2005-11-14 16:48',))
if mibBuilder.loadTexts: etsysMgmtAuthNotificationMIB.setLastUpdated('201103082040Z')
if mibBuilder.loadTexts: etsysMgmtAuthNotificationMIB.setOrganization('Enterasys Networks, Inc')
class EtsysMgmtAuthNotificationTypes(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cliConsole", 0), ("cliSsh", 1), ("cliTelnet", 2), ("webview", 3), ("inactiveUser", 4), ("maxUserAttempt", 5), ("maxUserFail", 6))

etsysMgmtAuthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1))
etsysMgmtAuthNotificationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0))
etsysMgmtAuthConfigBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1))
etsysMgmtAuthAuthenticationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2))
etsysMgmtAuthNotificationsSupported = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1, 1), EtsysMgmtAuthNotificationTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMgmtAuthNotificationsSupported.setStatus('current')
etsysMgmtAuthNotificationEnabledStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1, 2), EtsysMgmtAuthNotificationTypes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMgmtAuthNotificationEnabledStatus.setStatus('current')
etsysMgmtAuthType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 1), EtsysMgmtAuthNotificationTypes()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthType.setStatus('current')
etsysMgmtAuthUserName = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthUserName.setStatus('current')
etsysMgmtAuthInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthInetAddressType.setStatus('current')
etsysMgmtAuthInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthInetAddress.setStatus('current')
etsysMgmtAuthInIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 5), InterfaceIndexOrZero()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthInIfIndex.setStatus('current')
etsysMgmtAuthSuccessNotificiation = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 1)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthSuccessNotificiation.setStatus('current')
etsysMgmtAuthFailNotificiation = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 2)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthFailNotificiation.setStatus('current')
etsysMgmtAuthInactiveNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 3)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthInactiveNotification.setStatus('current')
etsysMgmtAuthMaxAuthAttemptNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 4)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthMaxAuthAttemptNotification.setStatus('current')
etsysMgmtAuthMaxFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 5)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthMaxFailNotification.setStatus('current')
etsysMgmtAuthConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2))
etsysMgmtAuthGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1))
etsysMgmtAuthCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2))
etsysMgmtAuthConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 1)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationsSupported"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationEnabledStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthConfigGroup = etsysMgmtAuthConfigGroup.setStatus('current')
etsysMgmtAuthHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 2)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthHistoryGroup = etsysMgmtAuthHistoryGroup.setStatus('current')
etsysMgmtAuthNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 3)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthSuccessNotificiation"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthFailNotificiation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthNotificationGroup = etsysMgmtAuthNotificationGroup.setStatus('current')
etsysMgmtAuthNotificationUserGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 4)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInactiveNotification"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthMaxAuthAttemptNotification"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthMaxFailNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthNotificationUserGroup = etsysMgmtAuthNotificationUserGroup.setStatus('current')
etsysMgmtAuthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2, 1)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthConfigGroup"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthHistoryGroup"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthCompliance = etsysMgmtAuthCompliance.setStatus('current')
etsysMgmtAuthUserCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2, 2)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthUserCompliance = etsysMgmtAuthUserCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", etsysMgmtAuthNotificationBranch=etsysMgmtAuthNotificationBranch, etsysMgmtAuthConformance=etsysMgmtAuthConformance, etsysMgmtAuthNotificationGroup=etsysMgmtAuthNotificationGroup, etsysMgmtAuthInIfIndex=etsysMgmtAuthInIfIndex, etsysMgmtAuthMaxAuthAttemptNotification=etsysMgmtAuthMaxAuthAttemptNotification, etsysMgmtAuthNotificationsSupported=etsysMgmtAuthNotificationsSupported, etsysMgmtAuthInetAddress=etsysMgmtAuthInetAddress, etsysMgmtAuthAuthenticationBranch=etsysMgmtAuthAuthenticationBranch, EtsysMgmtAuthNotificationTypes=EtsysMgmtAuthNotificationTypes, etsysMgmtAuthConfigGroup=etsysMgmtAuthConfigGroup, etsysMgmtAuthMaxFailNotification=etsysMgmtAuthMaxFailNotification, etsysMgmtAuthUserName=etsysMgmtAuthUserName, etsysMgmtAuthNotificationEnabledStatus=etsysMgmtAuthNotificationEnabledStatus, etsysMgmtAuthInetAddressType=etsysMgmtAuthInetAddressType, etsysMgmtAuthInactiveNotification=etsysMgmtAuthInactiveNotification, etsysMgmtAuthConfigBranch=etsysMgmtAuthConfigBranch, etsysMgmtAuthGroups=etsysMgmtAuthGroups, etsysMgmtAuthType=etsysMgmtAuthType, etsysMgmtAuthFailNotificiation=etsysMgmtAuthFailNotificiation, etsysMgmtAuthObjects=etsysMgmtAuthObjects, etsysMgmtAuthCompliance=etsysMgmtAuthCompliance, etsysMgmtAuthSuccessNotificiation=etsysMgmtAuthSuccessNotificiation, PYSNMP_MODULE_ID=etsysMgmtAuthNotificationMIB, etsysMgmtAuthNotificationMIB=etsysMgmtAuthNotificationMIB, etsysMgmtAuthNotificationUserGroup=etsysMgmtAuthNotificationUserGroup, etsysMgmtAuthUserCompliance=etsysMgmtAuthUserCompliance, etsysMgmtAuthHistoryGroup=etsysMgmtAuthHistoryGroup, etsysMgmtAuthCompliances=etsysMgmtAuthCompliances)
