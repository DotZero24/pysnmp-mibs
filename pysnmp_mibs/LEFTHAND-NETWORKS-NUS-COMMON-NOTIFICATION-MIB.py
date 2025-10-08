#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lhnModules, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnModules")
lhnNusCommonGroups, lhnNusCommonNotification, lhnNusCommonEvents = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonGroups", "lhnNusCommonNotification", "lhnNusCommonEvents")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", lhnNusCommonEventGroup=lhnNusCommonEventGroup, notificationMessage=notificationMessage, notificationMessageEntry=notificationMessageEntry, notificationMessageCount=notificationMessageCount, notificationIndex=notificationIndex, notificationTime=notificationTime, lhnNusCommonNotificationModule=lhnNusCommonNotificationModule, PYSNMP_MODULE_ID=lhnNusCommonNotificationModule, notificationMessageTable=notificationMessageTable, userNotification=userNotification)
