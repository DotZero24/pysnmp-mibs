#
# PySNMP MIB module ARUBAWIRED-LED-LOCATOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-LED-LOCATOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
arubaWiredChassisMIB, = mibBuilder.importSymbols("ARUBAWIRED-CHASSIS-MIB", "arubaWiredChassisMIB")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ARUBAWIRED-LED-LOCATOR-MIB", arubaWiredLedLocator=arubaWiredLedLocator, arubaWiredLedLocatorState=arubaWiredLedLocatorState, arubaWiredLedLocatorGroupIndex=arubaWiredLedLocatorGroupIndex, arubaWiredLedLocatorName=arubaWiredLedLocatorName, arubaWiredLedLocatorConformance=arubaWiredLedLocatorConformance, arubaWiredLedLocatorTableGroup=arubaWiredLedLocatorTableGroup, arubaWiredLedLocatorObjects=arubaWiredLedLocatorObjects, arubaWiredLedLocatorTable=arubaWiredLedLocatorTable, arubaWiredLedLocatorEntry=arubaWiredLedLocatorEntry, arubaWiredLedLocatorDetails=arubaWiredLedLocatorDetails, arubaWiredLedLocatorCompliances=arubaWiredLedLocatorCompliances, PYSNMP_MODULE_ID=arubaWiredLedLocator, arubaWiredLedLocatorCompliance=arubaWiredLedLocatorCompliance, arubaWiredLedLocatorGroups=arubaWiredLedLocatorGroups)
