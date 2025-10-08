#
# PySNMP MIB module PDN-IF-EXT-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-IF-EXT-CONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdnIfExt, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnIfExt")
pdnIfExtConfig, = mibBuilder.importSymbols("PDN-IFEXT-MIB", "pdnIfExtConfig")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("PDN-IF-EXT-CONFIG-MIB", pdnIfExtEncapConfig=pdnIfExtEncapConfig, PdnLinkRole=PdnLinkRole, pdnIfMultiprotocolEncapConfigEntry=pdnIfMultiprotocolEncapConfigEntry, pdnIfMultiprotocolEncapConfigBridgedPDUs=pdnIfMultiprotocolEncapConfigBridgedPDUs, pdnIfXLinkConfigEntry=pdnIfXLinkConfigEntry, pdnIfMultiprotocolEncapMIBGroups=pdnIfMultiprotocolEncapMIBGroups, pdnIfXConfigMIBConformance=pdnIfXConfigMIBConformance, pdnIfMultiprotocolEncapConfigIPRoutedPDUs=pdnIfMultiprotocolEncapConfigIPRoutedPDUs, pdnIfMultiprotocolEncapCompliance=pdnIfMultiprotocolEncapCompliance, pdnIfXConfigMIBGroups=pdnIfXConfigMIBGroups, pdnIfMultiprotocolEncapCompliances=pdnIfMultiprotocolEncapCompliances, PYSNMP_MODULE_ID=pdnIfExtEncapConfig, pdnIfXLinkConfigTable=pdnIfXLinkConfigTable, pdnIfMultiprotocolEncapsulationOptionalGroup=pdnIfMultiprotocolEncapsulationOptionalGroup, pdnIfMultiprotocolEncapMIBConformance=pdnIfMultiprotocolEncapMIBConformance, pdnIfXLinkConfigOptionalGroup=pdnIfXLinkConfigOptionalGroup, pdnIfMultiprotocolEncapConfigTable=pdnIfMultiprotocolEncapConfigTable, pdnIfXLinkConfigRole=pdnIfXLinkConfigRole)
