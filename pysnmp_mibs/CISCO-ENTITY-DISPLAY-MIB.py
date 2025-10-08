#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-DISPLAY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoEntityDisplayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 344))
ciscoEntityDisplayMIB.setRevisions(('2009-10-05 00:00', '2003-03-20 00:00',))
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setLastUpdated('200910050000Z')
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setOrganization('Cisco Systems, Inc.')
class CDisplayType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("led", 1), ("alphanumeric", 2))

class CDisplayColor(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("white", 2), ("red", 3), ("green", 4), ("yellow", 5), ("amber", 6), ("blue", 7), ("greenAndAmber", 8))

class CDisplayState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("off", 2), ("on", 3), ("blinking", 4))

ciscoEntityDisplayMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 1))
ceDisplayTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1), )
if mibBuilder.loadTexts: ceDisplayTable.setStatus('current')
ceDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"))
if mibBuilder.loadTexts: ceDisplayEntry.setStatus('current')
ceDisplayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: ceDisplayIndex.setStatus('current')
ceDisplayType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 2), CDisplayType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayType.setStatus('current')
ceDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayName.setStatus('current')
ceDisplayState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 4), CDisplayState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayState.setStatus('current')
ceDisplayColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 5), CDisplayColor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayColor.setStatus('current')
ceDisplayText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayText.setStatus('current')
ceDisplayBeaconTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2), )
if mibBuilder.loadTexts: ceDisplayBeaconTable.setStatus('current')
ceDisplayBeaconEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"))
if mibBuilder.loadTexts: ceDisplayBeaconEntry.setStatus('current')
ceDisplayBeaconEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceDisplayBeaconEnabled.setStatus('current')
ceDisplayMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2))
ceDisplayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1))
ceDisplayMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2))
ceDisplayMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 1)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayLEDGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayAlphaNumericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayMIBCompliance = ceDisplayMIBCompliance.setStatus('deprecated')
ceDisplayMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 2)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayLEDGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayAlphaNumericGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayBeaconGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayMIBCompliance2 = ceDisplayMIBCompliance2.setStatus('current')
ceDisplayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 1)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayType"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayName"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayGroup = ceDisplayGroup.setStatus('current')
ceDisplayLEDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 2)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayLEDGroup = ceDisplayLEDGroup.setStatus('current')
ceDisplayAlphaNumericGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 3)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayAlphaNumericGroup = ceDisplayAlphaNumericGroup.setStatus('current')
ceDisplayBeaconGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 4)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayBeaconEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayBeaconGroup = ceDisplayBeaconGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-MIB", ceDisplayBeaconGroup=ceDisplayBeaconGroup, ceDisplayTable=ceDisplayTable, ceDisplayName=ceDisplayName, ceDisplayType=ceDisplayType, ciscoEntityDisplayMIB=ciscoEntityDisplayMIB, ceDisplayLEDGroup=ceDisplayLEDGroup, ceDisplayMIBCompliance2=ceDisplayMIBCompliance2, CDisplayColor=CDisplayColor, ceDisplayBeaconTable=ceDisplayBeaconTable, ceDisplayMIBCompliances=ceDisplayMIBCompliances, ciscoEntityDisplayMIBObjects=ciscoEntityDisplayMIBObjects, ceDisplayMIBCompliance=ceDisplayMIBCompliance, ceDisplayBeaconEnabled=ceDisplayBeaconEnabled, ceDisplayColor=ceDisplayColor, ceDisplayAlphaNumericGroup=ceDisplayAlphaNumericGroup, CDisplayType=CDisplayType, ceDisplayState=ceDisplayState, ceDisplayMIBConformance=ceDisplayMIBConformance, ceDisplayMIBGroups=ceDisplayMIBGroups, PYSNMP_MODULE_ID=ciscoEntityDisplayMIB, ceDisplayGroup=ceDisplayGroup, ceDisplayEntry=ceDisplayEntry, CDisplayState=CDisplayState, ceDisplayText=ceDisplayText, ceDisplayBeaconEntry=ceDisplayBeaconEntry, ceDisplayIndex=ceDisplayIndex)
