#
# PySNMP MIB module PDN-IF-EXT-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-IF-EXT-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdnIfExt, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnIfExt")
pdnIfExtConfig, = mibBuilder.importSymbols("PDN-IFEXT-MIB", "pdnIfExtConfig")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnIfExtEncapConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3))
pdnIfExtEncapConfig.setRevisions(('2003-12-16 09:00', '2001-11-13 00:00', '2001-11-12 00:00', '2000-05-11 00:00', '2000-05-03 00:00', '2000-05-02 00:00',))
if mibBuilder.loadTexts: pdnIfExtEncapConfig.setLastUpdated('200312160900Z')
if mibBuilder.loadTexts: pdnIfExtEncapConfig.setOrganization('Paradyne Networks MIB Working Group')
class PdnLinkRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("uplink", 1), ("other", 2))

pdnIfMultiprotocolEncapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1), )
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigTable.setStatus('current')
pdnIfMultiprotocolEncapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigEntry.setStatus('current')
pdnIfMultiprotocolEncapConfigIPRoutedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("llcSnap", 2), ("vcBasedMultiplexing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigIPRoutedPDUs.setStatus('current')
pdnIfMultiprotocolEncapConfigBridgedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("llcSnap", 2), ("vcBasedMultiplexing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigBridgedPDUs.setStatus('current')
pdnIfXLinkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3), )
if mibBuilder.loadTexts: pdnIfXLinkConfigTable.setStatus('current')
pdnIfXLinkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnIfXLinkConfigEntry.setStatus('current')
pdnIfXLinkConfigRole = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3, 1, 1), PdnLinkRole()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIfXLinkConfigRole.setStatus('current')
pdnIfMultiprotocolEncapMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2))
pdnIfMultiprotocolEncapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 1))
pdnIfMultiprotocolEncapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 2))
pdnIfXConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4))
pdnIfXConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4, 1))
pdnIfMultiprotocolEncapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 2, 1)).setObjects(("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapsulationOptionalGroup"), ("PDN-IF-EXT-CONFIG-MIB", "pdnIfXLinkConfigOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfMultiprotocolEncapCompliance = pdnIfMultiprotocolEncapCompliance.setStatus('current')
pdnIfMultiprotocolEncapsulationOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 1, 1)).setObjects(("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapConfigIPRoutedPDUs"), ("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapConfigBridgedPDUs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfMultiprotocolEncapsulationOptionalGroup = pdnIfMultiprotocolEncapsulationOptionalGroup.setStatus('current')
pdnIfXLinkConfigOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4, 1, 1)).setObjects(("PDN-IF-EXT-CONFIG-MIB", "pdnIfXLinkConfigRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfXLinkConfigOptionalGroup = pdnIfXLinkConfigOptionalGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-IF-EXT-CONFIG-MIB", pdnIfXConfigMIBConformance=pdnIfXConfigMIBConformance, pdnIfXConfigMIBGroups=pdnIfXConfigMIBGroups, PdnLinkRole=PdnLinkRole, pdnIfMultiprotocolEncapMIBGroups=pdnIfMultiprotocolEncapMIBGroups, pdnIfXLinkConfigTable=pdnIfXLinkConfigTable, pdnIfXLinkConfigOptionalGroup=pdnIfXLinkConfigOptionalGroup, pdnIfMultiprotocolEncapConfigIPRoutedPDUs=pdnIfMultiprotocolEncapConfigIPRoutedPDUs, pdnIfMultiprotocolEncapConfigBridgedPDUs=pdnIfMultiprotocolEncapConfigBridgedPDUs, pdnIfMultiprotocolEncapsulationOptionalGroup=pdnIfMultiprotocolEncapsulationOptionalGroup, pdnIfExtEncapConfig=pdnIfExtEncapConfig, pdnIfMultiprotocolEncapConfigTable=pdnIfMultiprotocolEncapConfigTable, pdnIfXLinkConfigEntry=pdnIfXLinkConfigEntry, pdnIfMultiprotocolEncapCompliances=pdnIfMultiprotocolEncapCompliances, PYSNMP_MODULE_ID=pdnIfExtEncapConfig, pdnIfMultiprotocolEncapMIBConformance=pdnIfMultiprotocolEncapMIBConformance, pdnIfMultiprotocolEncapCompliance=pdnIfMultiprotocolEncapCompliance, pdnIfMultiprotocolEncapConfigEntry=pdnIfMultiprotocolEncapConfigEntry, pdnIfXLinkConfigRole=pdnIfXLinkConfigRole)
