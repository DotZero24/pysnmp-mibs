#
# PySNMP MIB module HP-ICF-JUMBO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-JUMBO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpicfObjectModules, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfObjectModules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfJumboMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13))
hpicfJumboMIB.setRevisions(('2004-08-22 10:30',))
if mibBuilder.loadTexts: hpicfJumboMIB.setLastUpdated('200408221030Z')
if mibBuilder.loadTexts: hpicfJumboMIB.setOrganization('HP Networking')
hpicfJumboObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1))
hpJumboStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1))
hpJumboStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1), )
if mibBuilder.loadTexts: hpJumboStatsTable.setStatus('current')
hpJumboStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1), ).setIndexNames((0, "HP-ICF-JUMBO-MIB", "hpJumboStatsIndex"))
if mibBuilder.loadTexts: hpJumboStatsEntry.setStatus('current')
hpJumboStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpJumboStatsIndex.setStatus('current')
hpJumboStatsPkts1523to2047Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpJumboStatsPkts1523to2047Octets.setStatus('current')
hpJumboStatsPkts2048to4095Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpJumboStatsPkts2048to4095Octets.setStatus('current')
hpJumboStatsPkts4096to9216Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpJumboStatsPkts4096to9216Octets.setStatus('current')
hpicfJumboConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2))
hpicfJumboGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 1))
hpicfJumboCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 2))
hpicfJumboStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 1, 1)).setObjects(("HP-ICF-JUMBO-MIB", "hpJumboStatsIndex"), ("HP-ICF-JUMBO-MIB", "hpJumboStatsPkts1523to2047Octets"), ("HP-ICF-JUMBO-MIB", "hpJumboStatsPkts2048to4095Octets"), ("HP-ICF-JUMBO-MIB", "hpJumboStatsPkts4096to9216Octets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJumboStatsGroup = hpicfJumboStatsGroup.setStatus('current')
hpicfJumboCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 2, 1)).setObjects(("HP-ICF-JUMBO-MIB", "hpicfJumboStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJumboCompliance = hpicfJumboCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-JUMBO-MIB", hpicfJumboCompliance=hpicfJumboCompliance, hpJumboStatsTable=hpJumboStatsTable, hpJumboStats=hpJumboStats, hpJumboStatsPkts4096to9216Octets=hpJumboStatsPkts4096to9216Octets, PYSNMP_MODULE_ID=hpicfJumboMIB, hpicfJumboMIB=hpicfJumboMIB, hpJumboStatsPkts1523to2047Octets=hpJumboStatsPkts1523to2047Octets, hpicfJumboConformance=hpicfJumboConformance, hpJumboStatsIndex=hpJumboStatsIndex, hpicfJumboCompliances=hpicfJumboCompliances, hpicfJumboGroups=hpicfJumboGroups, hpicfJumboObjects=hpicfJumboObjects, hpJumboStatsEntry=hpJumboStatsEntry, hpicfJumboStatsGroup=hpicfJumboStatsGroup, hpJumboStatsPkts2048to4095Octets=hpJumboStatsPkts2048to4095Octets)
