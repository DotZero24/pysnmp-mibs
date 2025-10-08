#
# PySNMP MIB module ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", etsysIetfpBridgeMibExtMIB=etsysIetfpBridgeMibExtMIB, etsysDot1dPortPriorityTable=etsysDot1dPortPriorityTable, etsysDot1dPortPriorityRewrite=etsysDot1dPortPriorityRewrite, etsysIetfpBridgeConformance=etsysIetfpBridgeConformance, etsysDot1dPriorityRewriteGroup=etsysDot1dPriorityRewriteGroup, etsysIetfpBridgeMibExt=etsysIetfpBridgeMibExt, etsysIetfpBridgeCompliance=etsysIetfpBridgeCompliance, etsysDot1dPortPriorityEntry=etsysDot1dPortPriorityEntry, PYSNMP_MODULE_ID=etsysIetfpBridgeMibExtMIB, etsysIetfpBridgeCompliances=etsysIetfpBridgeCompliances, etsysIetfpBridgeGroups=etsysIetfpBridgeGroups, etsysDot1dPriority=etsysDot1dPriority)
