#
# PySNMP MIB module ARISTA-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arista/ARISTA-TEST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ZeroBasedCounter32, = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaTestMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 3))
aristaTestMIB.setRevisions(('2014-08-15 00:00', '2011-03-31 13:00', '2010-12-01 00:00',))
if mibBuilder.loadTexts: aristaTestMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaTestMIB.setOrganization('Arista Networks, Inc.')
aristaTestNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0))
aristaTestObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1))
aristaTestConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2))
aristaTestNotificationCounter = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 1), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaTestNotificationCounter.setStatus('current')
aristaTestNotificationComment = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaTestNotificationComment.setStatus('current')
aristaTestNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0))
aristaTestNotification = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0, 1)).setObjects(("ARISTA-TEST-MIB", "aristaTestNotificationCounter"), ("ARISTA-TEST-MIB", "aristaTestNotificationComment"))
if mibBuilder.loadTexts: aristaTestNotification.setStatus('current')
aristaTestCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1))
aristaTestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2))
aristaTestCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1, 1)).setObjects(("ARISTA-TEST-MIB", "aristaTestObjectsGroup"), ("ARISTA-TEST-MIB", "aristaTestNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaTestCompliance = aristaTestCompliance.setStatus('current')
aristaTestObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 1)).setObjects(("ARISTA-TEST-MIB", "aristaTestNotificationCounter"), ("ARISTA-TEST-MIB", "aristaTestNotificationComment"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaTestObjectsGroup = aristaTestObjectsGroup.setStatus('current')
aristaTestNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 2)).setObjects(("ARISTA-TEST-MIB", "aristaTestNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaTestNotificationsGroup = aristaTestNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-TEST-MIB", aristaTestGroups=aristaTestGroups, aristaTestNotificationPrefix=aristaTestNotificationPrefix, aristaTestNotifications=aristaTestNotifications, aristaTestNotification=aristaTestNotification, aristaTestObjectsGroup=aristaTestObjectsGroup, aristaTestMIB=aristaTestMIB, aristaTestNotificationCounter=aristaTestNotificationCounter, aristaTestNotificationsGroup=aristaTestNotificationsGroup, aristaTestCompliances=aristaTestCompliances, aristaTestCompliance=aristaTestCompliance, PYSNMP_MODULE_ID=aristaTestMIB, aristaTestConformance=aristaTestConformance, aristaTestNotificationComment=aristaTestNotificationComment, aristaTestObjects=aristaTestObjects)
