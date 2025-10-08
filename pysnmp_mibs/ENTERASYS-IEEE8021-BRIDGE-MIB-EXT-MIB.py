#
# PySNMP MIB module ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ieee8021BridgeBasePort, ieee8021BridgeBasePortEntry = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort", "ieee8021BridgeBasePortEntry")
IEEE8021PbbComponentIdentifier, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PbbComponentIdentifier")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysIeee8021BridgeMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90))
etsysIeee8021BridgeMibExtMIB.setRevisions(('2012-02-07 14:35',))
if mibBuilder.loadTexts: etsysIeee8021BridgeMibExtMIB.setLastUpdated('201202071435Z')
if mibBuilder.loadTexts: etsysIeee8021BridgeMibExtMIB.setOrganization('Enterasys Networks, Inc')
etsysIeee8021BridgeMibExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1))
etsysIeee8021BridgeMibExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2))
etsysIeee8021BridgeBase = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1))
etsysIeee8021BridgeBaseMode = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("customerBridge", 1), ("providerBridge", 2), ("providerBackboneBridge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIeee8021BridgeBaseMode.setStatus('current')
etsysIeee8021BridgeBasePortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1, 2), )
if mibBuilder.loadTexts: etsysIeee8021BridgeBasePortTable.setStatus('current')
etsysIeee8021BridgeBasePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: etsysIeee8021BridgeBasePortEntry.setStatus('current')
etsys8021BridgePortComponentId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1, 2, 1, 1), IEEE8021PbbComponentIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsys8021BridgePortComponentId.setStatus('current')
etsysIeee8021BridgeMibExtMrpBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 2))
etsysIeee8021BridgeMibExtMrpTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 2, 1), )
if mibBuilder.loadTexts: etsysIeee8021BridgeMibExtMrpTable.setStatus('current')
etsysIeee8021BridgeMibExtMrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 2, 1, 1), )
ieee8021BridgeBasePortEntry.registerAugmentions(("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeMibExtMrpEntry"))
etsysIeee8021BridgeMibExtMrpEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysIeee8021BridgeMibExtMrpEntry.setStatus('current')
etsysIeee8021BridgeMibExtMrpPeriodicEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 2, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIeee8021BridgeMibExtMrpPeriodicEnabled.setStatus('current')
etsysIeee8021BridgeMibExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 1))
etsysIeee8021BridgeMibExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 2))
etsysIeee8021BridgeMibExtBaseModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 1, 1)).setObjects(("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeBaseMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021BridgeMibExtBaseModeGroup = etsysIeee8021BridgeMibExtBaseModeGroup.setStatus('current')
etsysIeee8021BridgeMibExtBasePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 1, 2)).setObjects(("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsys8021BridgePortComponentId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021BridgeMibExtBasePortGroup = etsysIeee8021BridgeMibExtBasePortGroup.setStatus('current')
etsysIeee8021BridgeMibExtMrpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 1, 3)).setObjects(("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeMibExtMrpPeriodicEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021BridgeMibExtMrpGroup = etsysIeee8021BridgeMibExtMrpGroup.setStatus('current')
etsysIeee8021BridgeMibExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 2, 1)).setObjects(("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeMibExtBaseModeGroup"), ("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeMibExtBasePortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021BridgeMibExtCompliance = etsysIeee8021BridgeMibExtCompliance.setStatus('current')
etsysIeee8021BridgeMibExtMrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 2, 2)).setObjects(("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeMibExtMrpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021BridgeMibExtMrpCompliance = etsysIeee8021BridgeMibExtMrpCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", etsysIeee8021BridgeMibExtBaseModeGroup=etsysIeee8021BridgeMibExtBaseModeGroup, etsysIeee8021BridgeBasePortTable=etsysIeee8021BridgeBasePortTable, etsysIeee8021BridgeMibExtBasePortGroup=etsysIeee8021BridgeMibExtBasePortGroup, etsysIeee8021BridgeMibExtMrpGroup=etsysIeee8021BridgeMibExtMrpGroup, etsysIeee8021BridgeMibExtMIB=etsysIeee8021BridgeMibExtMIB, etsysIeee8021BridgeMibExtMrpTable=etsysIeee8021BridgeMibExtMrpTable, etsysIeee8021BridgeBasePortEntry=etsysIeee8021BridgeBasePortEntry, etsysIeee8021BridgeMibExtMrpBranch=etsysIeee8021BridgeMibExtMrpBranch, etsysIeee8021BridgeMibExtMrpPeriodicEnabled=etsysIeee8021BridgeMibExtMrpPeriodicEnabled, etsysIeee8021BridgeBase=etsysIeee8021BridgeBase, etsysIeee8021BridgeMibExtConformance=etsysIeee8021BridgeMibExtConformance, etsys8021BridgePortComponentId=etsys8021BridgePortComponentId, etsysIeee8021BridgeMibExtGroups=etsysIeee8021BridgeMibExtGroups, etsysIeee8021BridgeBaseMode=etsysIeee8021BridgeBaseMode, etsysIeee8021BridgeMibExtMrpCompliance=etsysIeee8021BridgeMibExtMrpCompliance, etsysIeee8021BridgeMibExtMrpEntry=etsysIeee8021BridgeMibExtMrpEntry, etsysIeee8021BridgeMibExtCompliances=etsysIeee8021BridgeMibExtCompliances, etsysIeee8021BridgeMibExtObjects=etsysIeee8021BridgeMibExtObjects, PYSNMP_MODULE_ID=etsysIeee8021BridgeMibExtMIB, etsysIeee8021BridgeMibExtCompliance=etsysIeee8021BridgeMibExtCompliance)
