#
# PySNMP MIB module ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
dot3adAggPortEntry, = mibBuilder.importSymbols("IEEE8023-LAG-MIB", "dot3adAggPortEntry")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysIeee8023LagMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35))
etsysIeee8023LagMibExtMIB.setRevisions(('2004-09-03 15:14', '2003-01-31 23:16',))
if mibBuilder.loadTexts: etsysIeee8023LagMibExtMIB.setLastUpdated('200409031514Z')
if mibBuilder.loadTexts: etsysIeee8023LagMibExtMIB.setOrganization('Enterasys Networks, Inc')
etsysIeee8023LagMibExt = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1))
etsysDot3adAggGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 1))
etsysDot3adAggPort = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2))
etsysDot3adAggGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 1, 1), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3adAggGlobalEnable.setStatus('current')
etsysDot3adAggGlobalFormSinglePortLags = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3adAggGlobalFormSinglePortLags.setStatus('current')
etsysDot3adAggPortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2, 1), )
if mibBuilder.loadTexts: etsysDot3adAggPortTable.setStatus('current')
etsysDot3adAggPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2, 1, 1), )
dot3adAggPortEntry.registerAugmentions(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggPortEntry"))
etsysDot3adAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysDot3adAggPortEntry.setStatus('current')
etsysDot3adAggPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2, 1, 1, 1), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3adAggPortEnable.setStatus('current')
etsysIeee8023LagConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2))
etsysIeee8023LagGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1))
etsysIeee8023LagCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 2))
etsysDot3adAggGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1, 1)).setObjects(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot3adAggGlobalGroup = etsysDot3adAggGlobalGroup.setStatus('current')
etsysDot3adAggPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1, 2)).setObjects(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggPortEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot3adAggPortGroup = etsysDot3adAggPortGroup.setStatus('current')
etsysDot3adAggGlobalSinglePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1, 3)).setObjects(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalFormSinglePortLags"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot3adAggGlobalSinglePortGroup = etsysDot3adAggGlobalSinglePortGroup.setStatus('current')
etsysIeee8023LagCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 2, 1)).setObjects(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalGroup"), ("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggPortGroup"), ("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalSinglePortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8023LagCompliance = etsysIeee8023LagCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", PYSNMP_MODULE_ID=etsysIeee8023LagMibExtMIB, etsysDot3adAggGlobalGroup=etsysDot3adAggGlobalGroup, etsysIeee8023LagMibExtMIB=etsysIeee8023LagMibExtMIB, etsysDot3adAggPort=etsysDot3adAggPort, etsysIeee8023LagGroups=etsysIeee8023LagGroups, etsysIeee8023LagMibExt=etsysIeee8023LagMibExt, etsysDot3adAggPortTable=etsysDot3adAggPortTable, etsysIeee8023LagConformance=etsysIeee8023LagConformance, etsysDot3adAggGlobal=etsysDot3adAggGlobal, etsysDot3adAggPortEnable=etsysDot3adAggPortEnable, etsysDot3adAggGlobalSinglePortGroup=etsysDot3adAggGlobalSinglePortGroup, etsysIeee8023LagCompliances=etsysIeee8023LagCompliances, etsysDot3adAggGlobalEnable=etsysDot3adAggGlobalEnable, etsysDot3adAggPortGroup=etsysDot3adAggPortGroup, etsysDot3adAggGlobalFormSinglePortLags=etsysDot3adAggGlobalFormSinglePortLags, etsysIeee8023LagCompliance=etsysIeee8023LagCompliance, etsysDot3adAggPortEntry=etsysDot3adAggPortEntry)
