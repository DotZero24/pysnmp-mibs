#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lhnModules, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnModules")
lhnNusCommonGroups, lhnNusCommonNotification, lhnNusCommonEvents = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonGroups", "lhnNusCommonNotification", "lhnNusCommonEvents")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
lhnNusCommonNotificationModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1, 1, 15))
if mibBuilder.loadTexts: lhnNusCommonNotificationModule.setLastUpdated('0206250000Z')
if mibBuilder.loadTexts: lhnNusCommonNotificationModule.setOrganization('LeftHand Networks, Inc.')
notificationMessageCount = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationMessageCount.setStatus('current')
notificationMessageTable = MibTable((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2), )
if mibBuilder.loadTexts: notificationMessageTable.setStatus('current')
notificationMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1), ).setIndexNames((0, "LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "notificationIndex"))
if mibBuilder.loadTexts: notificationMessageEntry.setStatus('current')
notificationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationIndex.setStatus('current')
notificationMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationMessage.setStatus('current')
notificationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationTime.setStatus('current')
userNotification = NotificationType((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3, 1)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "notificationMessage"))
if mibBuilder.loadTexts: userNotification.setStatus('current')
lhnNusCommonEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1, 2)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "userNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lhnNusCommonEventGroup = lhnNusCommonEventGroup.setStatus('current')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", notificationMessage=notificationMessage, notificationMessageTable=notificationMessageTable, notificationMessageEntry=notificationMessageEntry, userNotification=userNotification, PYSNMP_MODULE_ID=lhnNusCommonNotificationModule, notificationMessageCount=notificationMessageCount, notificationIndex=notificationIndex, lhnNusCommonEventGroup=lhnNusCommonEventGroup, notificationTime=notificationTime, lhnNusCommonNotificationModule=lhnNusCommonNotificationModule)
