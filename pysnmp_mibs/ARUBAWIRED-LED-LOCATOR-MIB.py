#
# PySNMP MIB module ARUBAWIRED-LED-LOCATOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-LED-LOCATOR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
arubaWiredChassisMIB, = mibBuilder.importSymbols("ARUBAWIRED-CHASSIS-MIB", "arubaWiredChassisMIB")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredLedLocator = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7))
arubaWiredLedLocator.setRevisions(('2023-06-06 00:00',))
if mibBuilder.loadTexts: arubaWiredLedLocator.setLastUpdated('202306060000Z')
if mibBuilder.loadTexts: arubaWiredLedLocator.setOrganization('HPE/Aruba Networking Division')
arubaWiredLedLocatorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1))
arubaWiredLedLocatorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2))
arubaWiredLedLocatorDetails = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1))
arubaWiredLedLocatorTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1), )
if mibBuilder.loadTexts: arubaWiredLedLocatorTable.setStatus('current')
arubaWiredLedLocatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1, 1), ).setIndexNames((0, "ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorGroupIndex"))
if mibBuilder.loadTexts: arubaWiredLedLocatorEntry.setStatus('current')
arubaWiredLedLocatorGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: arubaWiredLedLocatorGroupIndex.setStatus('current')
arubaWiredLedLocatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLedLocatorName.setStatus('current')
arubaWiredLedLocatorState = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLedLocatorState.setStatus('current')
arubaWiredLedLocatorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2, 1))
arubaWiredLedLocatorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2, 2))
arubaWiredLedLocatorCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2, 1, 1)).setObjects(("ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorTable"), ("ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLedLocatorCompliance = arubaWiredLedLocatorCompliance.setStatus('current')
arubaWiredLedLocatorTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7, 2, 2, 1)).setObjects(("ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorName"), ("ARUBAWIRED-LED-LOCATOR-MIB", "arubaWiredLedLocatorState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLedLocatorTableGroup = arubaWiredLedLocatorTableGroup.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-LED-LOCATOR-MIB", arubaWiredLedLocatorObjects=arubaWiredLedLocatorObjects, arubaWiredLedLocatorGroupIndex=arubaWiredLedLocatorGroupIndex, arubaWiredLedLocatorCompliances=arubaWiredLedLocatorCompliances, arubaWiredLedLocatorName=arubaWiredLedLocatorName, PYSNMP_MODULE_ID=arubaWiredLedLocator, arubaWiredLedLocatorState=arubaWiredLedLocatorState, arubaWiredLedLocatorTableGroup=arubaWiredLedLocatorTableGroup, arubaWiredLedLocatorConformance=arubaWiredLedLocatorConformance, arubaWiredLedLocatorDetails=arubaWiredLedLocatorDetails, arubaWiredLedLocatorTable=arubaWiredLedLocatorTable, arubaWiredLedLocatorEntry=arubaWiredLedLocatorEntry, arubaWiredLedLocatorGroups=arubaWiredLedLocatorGroups, arubaWiredLedLocatorCompliance=arubaWiredLedLocatorCompliance, arubaWiredLedLocator=arubaWiredLedLocator)
