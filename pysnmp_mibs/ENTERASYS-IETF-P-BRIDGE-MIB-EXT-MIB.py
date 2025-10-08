#
# PySNMP MIB module ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysIetfpBridgeMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33))
etsysIetfpBridgeMibExtMIB.setRevisions(('2002-12-20 22:16',))
if mibBuilder.loadTexts: etsysIetfpBridgeMibExtMIB.setLastUpdated('200212202216Z')
if mibBuilder.loadTexts: etsysIetfpBridgeMibExtMIB.setOrganization('Enterasys Networks, Inc')
etsysIetfpBridgeMibExt = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1))
etsysDot1dPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1))
etsysDot1dPortPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1), )
if mibBuilder.loadTexts: etsysDot1dPortPriorityTable.setStatus('current')
etsysDot1dPortPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPortPriorityEntry"))
etsysDot1dPortPriorityEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysDot1dPortPriorityEntry.setStatus('current')
etsysDot1dPortPriorityRewrite = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1dPortPriorityRewrite.setStatus('current')
etsysIetfpBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2))
etsysIetfpBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 1))
etsysIetfpBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 2))
etsysDot1dPriorityRewriteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 1, 1)).setObjects(("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPortPriorityRewrite"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot1dPriorityRewriteGroup = etsysDot1dPriorityRewriteGroup.setStatus('current')
etsysIetfpBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 2, 1)).setObjects(("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPriorityRewriteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIetfpBridgeCompliance = etsysIetfpBridgeCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", etsysIetfpBridgeCompliances=etsysIetfpBridgeCompliances, etsysIetfpBridgeConformance=etsysIetfpBridgeConformance, etsysDot1dPriority=etsysDot1dPriority, etsysDot1dPortPriorityRewrite=etsysDot1dPortPriorityRewrite, etsysDot1dPriorityRewriteGroup=etsysDot1dPriorityRewriteGroup, etsysIetfpBridgeMibExtMIB=etsysIetfpBridgeMibExtMIB, PYSNMP_MODULE_ID=etsysIetfpBridgeMibExtMIB, etsysIetfpBridgeGroups=etsysIetfpBridgeGroups, etsysDot1dPortPriorityEntry=etsysDot1dPortPriorityEntry, etsysIetfpBridgeMibExt=etsysIetfpBridgeMibExt, etsysIetfpBridgeCompliance=etsysIetfpBridgeCompliance, etsysDot1dPortPriorityTable=etsysDot1dPortPriorityTable)
