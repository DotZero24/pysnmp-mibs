#
# PySNMP MIB module ARISTA-CONFIG-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arista/ARISTA-CONFIG-MAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaConfigManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 9))
aristaConfigManMIB.setRevisions(('2014-08-15 00:00', '2014-05-06 13:00', '2012-08-23 13:00',))
if mibBuilder.loadTexts: aristaConfigManMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaConfigManMIB.setOrganization('Arista Networks, Inc.')
class ConfigHistoryEventMedium(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("erase", 1), ("commandSource", 2), ("running", 3), ("startup", 4), ("url", 5), ("session", 6))

aristaConfigManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1))
aristaConfigManMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2))
aristaCmdHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1))
aristaCmdHistoryRunningLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryRunningLastChanged.setStatus('current')
aristaCmdHistoryEventTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2), )
if mibBuilder.loadTexts: aristaCmdHistoryEventTable.setStatus('current')
aristaCmdHistoryEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1), ).setIndexNames((0, "ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventIndex"))
if mibBuilder.loadTexts: aristaCmdHistoryEventEntry.setStatus('current')
aristaCmdHistoryEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaCmdHistoryEventIndex.setStatus('current')
aristaCmdHistoryEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventTime.setStatus('current')
aristaCmdHistoryEventCommandSource = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("commandLine", 0), ("snmp", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventCommandSource.setStatus('current')
aristaCmdHistoryEventConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 4), ConfigHistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventConfigSource.setStatus('current')
aristaCmdHistoryEventConfigDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 5), ConfigHistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventConfigDestination.setStatus('current')
aristaCmdHistoryEventConfigSourceURLScheme = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventConfigSourceURLScheme.setStatus('current')
aristaCmdHistoryEventConfigDestURLScheme = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventConfigDestURLScheme.setStatus('current')
aristaConfigManMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 3))
aristaConfigManMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 3, 0))
aristaConfigManEvent = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 9, 3, 0, 1)).setObjects(("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventCommandSource"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSource"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestination"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSourceURLScheme"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestURLScheme"))
if mibBuilder.loadTexts: aristaConfigManEvent.setStatus('current')
aristaConfigManMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1))
aristaConfigManMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 2))
aristaConfigManMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 1)).setObjects(("ARISTA-CONFIG-MAN-MIB", "aristaConfigEventDetailGroup"), ("ARISTA-CONFIG-MAN-MIB", "aristaConfigManMibNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigManMibCompliance = aristaConfigManMibCompliance.setStatus('current')
aristaConfigEventDetailGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 2, 1)).setObjects(("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryRunningLastChanged"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventTime"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventCommandSource"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSource"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestination"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSourceURLScheme"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestURLScheme"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigEventDetailGroup = aristaConfigEventDetailGroup.setStatus('current')
aristaConfigManMibNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 2, 2)).setObjects(("ARISTA-CONFIG-MAN-MIB", "aristaConfigManEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigManMibNotificationsGroup = aristaConfigManMibNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-CONFIG-MAN-MIB", aristaConfigManMibNotificationsGroup=aristaConfigManMibNotificationsGroup, aristaCmdHistory=aristaCmdHistory, aristaCmdHistoryEventCommandSource=aristaCmdHistoryEventCommandSource, aristaConfigManMibConformance=aristaConfigManMibConformance, aristaCmdHistoryEventConfigDestination=aristaCmdHistoryEventConfigDestination, aristaCmdHistoryEventTime=aristaCmdHistoryEventTime, ConfigHistoryEventMedium=ConfigHistoryEventMedium, aristaConfigManEvent=aristaConfigManEvent, aristaCmdHistoryEventConfigSource=aristaCmdHistoryEventConfigSource, aristaCmdHistoryEventConfigDestURLScheme=aristaCmdHistoryEventConfigDestURLScheme, aristaConfigManMibCompliance=aristaConfigManMibCompliance, aristaConfigManMIBNotifications=aristaConfigManMIBNotifications, aristaConfigEventDetailGroup=aristaConfigEventDetailGroup, aristaCmdHistoryEventEntry=aristaCmdHistoryEventEntry, aristaConfigManMIBNotificationPrefix=aristaConfigManMIBNotificationPrefix, aristaCmdHistoryEventIndex=aristaCmdHistoryEventIndex, aristaConfigManMibGroups=aristaConfigManMibGroups, aristaCmdHistoryRunningLastChanged=aristaCmdHistoryRunningLastChanged, aristaConfigManMibCompliances=aristaConfigManMibCompliances, aristaCmdHistoryEventConfigSourceURLScheme=aristaCmdHistoryEventConfigSourceURLScheme, aristaConfigManMIB=aristaConfigManMIB, aristaCmdHistoryEventTable=aristaCmdHistoryEventTable, aristaConfigManMIBObjects=aristaConfigManMIBObjects, PYSNMP_MODULE_ID=aristaConfigManMIB)
