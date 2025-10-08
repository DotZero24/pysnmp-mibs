#
# PySNMP MIB module ONEACCESS-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-EVENTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
oneAccess, oacMIBModules, oacExpIMEvents = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oneAccess", "oacMIBModules", "oacExpIMEvents")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ONEACCESS-EVENTS-MIB", oacEventSeverity=oacEventSeverity, oacEventsCompliances=oacEventsCompliances, oacEventsObjects=oacEventsObjects, oacEventSeverityNotifications=oacEventSeverityNotifications, oacEventSeverityInformational=oacEventSeverityInformational, oacEventsGeneralGroup=oacEventsGeneralGroup, oacEventSeverityAlerts=oacEventSeverityAlerts, oacEventsMIBModule=oacEventsMIBModule, oacEventSeverityDebug=oacEventSeverityDebug, oacEvent=oacEvent, oacEventSeverityLevel=oacEventSeverityLevel, PYSNMP_MODULE_ID=oacEventsMIBModule, oacEventSeverityErrors=oacEventSeverityErrors, oacEventsCompliance=oacEventsCompliance, oacEventSeverityWarnings=oacEventSeverityWarnings, oacEventSeverityCritical=oacEventSeverityCritical, oacEventText=oacEventText, oacEventsNotifications=oacEventsNotifications, oacEventsConformance=oacEventsConformance, oacEventsGroups=oacEventsGroups)
