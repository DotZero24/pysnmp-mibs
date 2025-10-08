#
# PySNMP MIB module ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ieee8021BridgeBasePortEntry, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortEntry")
IEEE8021VlanIndex, IEEE8021PbbComponentIdentifier = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021VlanIndex", "IEEE8021PbbComponentIdentifier")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysIeee8021QBridgeMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88))
etsysIeee8021QBridgeMibExtMIB.setRevisions(('2013-02-15 18:53', '2012-02-07 13:59',))
if mibBuilder.loadTexts: etsysIeee8021QBridgeMibExtMIB.setLastUpdated('201302151853Z')
if mibBuilder.loadTexts: etsysIeee8021QBridgeMibExtMIB.setOrganization('Enterasys Networks, Inc')
class EtsysIeee8021QBridgeFdbEntries(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(4096, 8192, 16384, 32768, 65536, 131072))
    namedValues = NamedValues(("is4K", 4096), ("is8K", 8192), ("is16K", 16384), ("is32K", 32768), ("is64K", 65536), ("is128K", 131072))

etsysIeee8021QBridgeMibExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1))
etsysIeee8021QBridgeMibExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 2))
etsysIeee8021QBridgeMibExtMvrpBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 1))
etsysIeee8021QBridgeMibExtPortVlanBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 2))
etsysIeee8021QBridgeMibExtFdbBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 3))
etsysIeee8021QVlanMvrpRestrictedTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 1, 1), )
if mibBuilder.loadTexts: etsysIeee8021QVlanMvrpRestrictedTable.setStatus('current')
etsysIeee8021QVlanMvrpRestrictedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 1, 1, 1), ).setIndexNames((0, "ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QVlanMvrpRestrictedComponentId"), (0, "ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QVlanMvrpRestrictedIndex"))
if mibBuilder.loadTexts: etsysIeee8021QVlanMvrpRestrictedEntry.setStatus('current')
etsysIeee8021QVlanMvrpRestrictedComponentId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 1, 1, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: etsysIeee8021QVlanMvrpRestrictedComponentId.setStatus('current')
etsysIeee8021QVlanMvrpRestrictedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 1, 1, 1, 2), IEEE8021VlanIndex())
if mibBuilder.loadTexts: etsysIeee8021QVlanMvrpRestrictedIndex.setStatus('current')
etsysIeee8021QVlanMvrpRestrictedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 1, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIeee8021QVlanMvrpRestrictedStatus.setStatus('current')
etsysIeee8021QBridgeMibExtPortVlanTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 2, 1), )
if mibBuilder.loadTexts: etsysIeee8021QBridgeMibExtPortVlanTable.setStatus('current')
etsysIeee8021QBridgeMibExtPortVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 2, 1, 1), )
ieee8021BridgeBasePortEntry.registerAugmentions(("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QBridgeMibExtPortVlanEntry"))
etsysIeee8021QBridgeMibExtPortVlanEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysIeee8021QBridgeMibExtPortVlanEntry.setStatus('current')
etsysIeee8021QBridgePortMvrpRxVidTranslationErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 2, 1, 1, 1), Counter64()).setUnits('MVRP receive VID translation errors').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysIeee8021QBridgePortMvrpRxVidTranslationErrors.setStatus('current')
etsysIeee8021QBridgePortMvrpTxVidTranslationErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 2, 1, 1, 2), Counter64()).setUnits('MVRP transmit VID translation errors').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysIeee8021QBridgePortMvrpTxVidTranslationErrors.setStatus('current')
etsysIeee8021QBridgeFdb = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 3, 1))
etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 3, 1, 1), Bits().clone(namedValues=NamedValues(("fdbMaxNumEntries4K", 0), ("fdbMaxNumEntries8K", 1), ("fdbMaxNumEntries16K", 2), ("fdbMaxNumEntries32K", 3), ("fdbMaxNumEntries64K", 4), ("fdbMaxNumEntries128K", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities.setStatus('current')
etsysIeee8021QBridgeFdbMaxNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 3, 1, 2), EtsysIeee8021QBridgeFdbEntries()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIeee8021QBridgeFdbMaxNumEntries.setStatus('current')
etsysIeee8021QBridgeFdbOperMaxNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 1, 3, 1, 3), EtsysIeee8021QBridgeFdbEntries()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysIeee8021QBridgeFdbOperMaxNumEntries.setStatus('current')
etsysIeee8021QBridgeMibExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 2, 1))
etsysIeee8021QBridgeMibExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 2, 2))
etsysIeee8021QBridgeMibExtMvrpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 2, 1, 1)).setObjects(("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QVlanMvrpRestrictedStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021QBridgeMibExtMvrpGroup = etsysIeee8021QBridgeMibExtMvrpGroup.setStatus('current')
etsysIeee8021QBridgeMibExtPortVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 2, 1, 2)).setObjects(("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QBridgePortMvrpRxVidTranslationErrors"), ("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QBridgePortMvrpTxVidTranslationErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021QBridgeMibExtPortVlanGroup = etsysIeee8021QBridgeMibExtPortVlanGroup.setStatus('current')
etsysIeee8021QBridgeMibExtFdbGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 2, 1, 3)).setObjects(("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities"), ("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QBridgeFdbMaxNumEntries"), ("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QBridgeFdbOperMaxNumEntries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021QBridgeMibExtFdbGroup = etsysIeee8021QBridgeMibExtFdbGroup.setStatus('current')
etsysIeee8021QBridgeMibExtMvrp = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 2, 2, 1)).setObjects(("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QBridgeMibExtMvrpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021QBridgeMibExtMvrp = etsysIeee8021QBridgeMibExtMvrp.setStatus('current')
etsysIeee8021QBridgeMibExtPortVlan = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 2, 2, 2)).setObjects(("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QBridgeMibExtPortVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021QBridgeMibExtPortVlan = etsysIeee8021QBridgeMibExtPortVlan.setStatus('current')
etsysIeee8021QBridgeMibExtFdb = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 88, 2, 2, 3)).setObjects(("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", "etsysIeee8021QBridgeMibExtFdbGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8021QBridgeMibExtFdb = etsysIeee8021QBridgeMibExtFdb.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB", etsysIeee8021QBridgeMibExtFdbBranch=etsysIeee8021QBridgeMibExtFdbBranch, etsysIeee8021QVlanMvrpRestrictedIndex=etsysIeee8021QVlanMvrpRestrictedIndex, etsysIeee8021QBridgeMibExtGroups=etsysIeee8021QBridgeMibExtGroups, etsysIeee8021QBridgeMibExtConformance=etsysIeee8021QBridgeMibExtConformance, etsysIeee8021QBridgeMibExtPortVlanBranch=etsysIeee8021QBridgeMibExtPortVlanBranch, etsysIeee8021QVlanMvrpRestrictedComponentId=etsysIeee8021QVlanMvrpRestrictedComponentId, etsysIeee8021QVlanMvrpRestrictedEntry=etsysIeee8021QVlanMvrpRestrictedEntry, etsysIeee8021QBridgeMibExtObjects=etsysIeee8021QBridgeMibExtObjects, etsysIeee8021QBridgeFdbOperMaxNumEntries=etsysIeee8021QBridgeFdbOperMaxNumEntries, etsysIeee8021QBridgeMibExtMvrpBranch=etsysIeee8021QBridgeMibExtMvrpBranch, etsysIeee8021QVlanMvrpRestrictedStatus=etsysIeee8021QVlanMvrpRestrictedStatus, EtsysIeee8021QBridgeFdbEntries=EtsysIeee8021QBridgeFdbEntries, etsysIeee8021QBridgeMibExtFdbGroup=etsysIeee8021QBridgeMibExtFdbGroup, PYSNMP_MODULE_ID=etsysIeee8021QBridgeMibExtMIB, etsysIeee8021QBridgeMibExtMvrp=etsysIeee8021QBridgeMibExtMvrp, etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities=etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities, etsysIeee8021QVlanMvrpRestrictedTable=etsysIeee8021QVlanMvrpRestrictedTable, etsysIeee8021QBridgeFdbMaxNumEntries=etsysIeee8021QBridgeFdbMaxNumEntries, etsysIeee8021QBridgeMibExtCompliances=etsysIeee8021QBridgeMibExtCompliances, etsysIeee8021QBridgeMibExtFdb=etsysIeee8021QBridgeMibExtFdb, etsysIeee8021QBridgePortMvrpTxVidTranslationErrors=etsysIeee8021QBridgePortMvrpTxVidTranslationErrors, etsysIeee8021QBridgeMibExtPortVlan=etsysIeee8021QBridgeMibExtPortVlan, etsysIeee8021QBridgeMibExtMIB=etsysIeee8021QBridgeMibExtMIB, etsysIeee8021QBridgeFdb=etsysIeee8021QBridgeFdb, etsysIeee8021QBridgePortMvrpRxVidTranslationErrors=etsysIeee8021QBridgePortMvrpRxVidTranslationErrors, etsysIeee8021QBridgeMibExtPortVlanTable=etsysIeee8021QBridgeMibExtPortVlanTable, etsysIeee8021QBridgeMibExtPortVlanEntry=etsysIeee8021QBridgeMibExtPortVlanEntry, etsysIeee8021QBridgeMibExtMvrpGroup=etsysIeee8021QBridgeMibExtMvrpGroup, etsysIeee8021QBridgeMibExtPortVlanGroup=etsysIeee8021QBridgeMibExtPortVlanGroup)
