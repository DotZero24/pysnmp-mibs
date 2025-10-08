#
# PySNMP MIB module ONEACCESS-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-EVENTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
oneAccess, oacMIBModules, oacExpIMEvents = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oneAccess", "oacMIBModules", "oacExpIMEvents")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacEventsMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 6600))
oacEventsMIBModule.setRevisions(('2011-06-15 00:00',))
if mibBuilder.loadTexts: oacEventsMIBModule.setLastUpdated('201106150000Z')
if mibBuilder.loadTexts: oacEventsMIBModule.setOrganization(' OneAccess ')
oacEventsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1))
oacEventsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 2))
oacEventsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3))
oacEventText = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacEventText.setStatus('current')
oacEventSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 2), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: oacEventSeverityLevel.setStatus('current')
oacEventSeverity = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3))
oacEventSeverityAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 1))
oacEventSeverityCritical = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 2))
oacEventSeverityErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 3))
oacEventSeverityWarnings = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 4))
oacEventSeverityNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 5))
oacEventSeverityInformational = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 6))
oacEventSeverityDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 7))
oacEvent = NotificationType((1, 3, 6, 1, 4, 1, 13191) + (0,1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
oacEventsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 1))
oacEventsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 2))
oacEventsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 2, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventsGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacEventsCompliance = oacEventsCompliance.setStatus('current')
oacEventsGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 1, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacEventsGeneralGroup = oacEventsGeneralGroup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-EVENTS-MIB", PYSNMP_MODULE_ID=oacEventsMIBModule, oacEventsGeneralGroup=oacEventsGeneralGroup, oacEventSeverityInformational=oacEventSeverityInformational, oacEventsCompliance=oacEventsCompliance, oacEventsGroups=oacEventsGroups, oacEventSeverityAlerts=oacEventSeverityAlerts, oacEventText=oacEventText, oacEventSeverityNotifications=oacEventSeverityNotifications, oacEventsMIBModule=oacEventsMIBModule, oacEventSeverityCritical=oacEventSeverityCritical, oacEventsCompliances=oacEventsCompliances, oacEventsNotifications=oacEventsNotifications, oacEventSeverityDebug=oacEventSeverityDebug, oacEventSeverityWarnings=oacEventSeverityWarnings, oacEventSeverityErrors=oacEventSeverityErrors, oacEventSeverityLevel=oacEventSeverityLevel, oacEvent=oacEvent, oacEventsConformance=oacEventsConformance, oacEventsObjects=oacEventsObjects, oacEventSeverity=oacEventSeverity)
