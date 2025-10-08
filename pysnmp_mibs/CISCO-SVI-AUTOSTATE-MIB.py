#
# PySNMP MIB module CISCO-SVI-AUTOSTATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-SVI-AUTOSTATE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoSVIAutostateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 376))
ciscoSVIAutostateMIB.setRevisions(('2004-04-06 00:00',))
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setLastUpdated('200404060000Z')
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setOrganization('Cisco Systems, Inc.')
ciscoSVIAutostateMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 0))
ciscoSVIAutostateMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1))
ciscoSVIAutostateMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2))
csaGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1))
csaInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2))
csaFeatureEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaFeatureEnable.setStatus('current')
csaTrackedVlansLow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansLow.setStatus('current')
csaTrackedVlansHigh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansHigh.setStatus('current')
csaIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1), )
if mibBuilder.loadTexts: csaIfConfigTable.setStatus('current')
csaIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: csaIfConfigEntry.setStatus('current')
csaInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("exclude", 2), ("track", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaInterfaceMode.setStatus('current')
csaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1))
csaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2))
csaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVIAutostateGroup"), ("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVITrackedVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaMIBCompliance = csaMIBCompliance.setStatus('current')
ciscoSVIAutostateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaFeatureEnable"), ("CISCO-SVI-AUTOSTATE-MIB", "csaInterfaceMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVIAutostateGroup = ciscoSVIAutostateGroup.setStatus('current')
ciscoSVITrackedVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 2)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansLow"), ("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansHigh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVITrackedVlanGroup = ciscoSVITrackedVlanGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SVI-AUTOSTATE-MIB", csaInterface=csaInterface, csaTrackedVlansLow=csaTrackedVlansLow, ciscoSVITrackedVlanGroup=ciscoSVITrackedVlanGroup, csaIfConfigEntry=csaIfConfigEntry, ciscoSVIAutostateMIBNotifs=ciscoSVIAutostateMIBNotifs, csaGlobal=csaGlobal, ciscoSVIAutostateMIBConformance=ciscoSVIAutostateMIBConformance, csaInterfaceMode=csaInterfaceMode, ciscoSVIAutostateMIBObjects=ciscoSVIAutostateMIBObjects, ciscoSVIAutostateMIB=ciscoSVIAutostateMIB, csaIfConfigTable=csaIfConfigTable, csaMIBCompliances=csaMIBCompliances, csaMIBGroups=csaMIBGroups, csaMIBCompliance=csaMIBCompliance, PYSNMP_MODULE_ID=ciscoSVIAutostateMIB, csaFeatureEnable=csaFeatureEnable, ciscoSVIAutostateGroup=ciscoSVIAutostateGroup, csaTrackedVlansHigh=csaTrackedVlansHigh)
