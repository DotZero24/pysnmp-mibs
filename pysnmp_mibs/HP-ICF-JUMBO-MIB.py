#
# PySNMP MIB module HP-ICF-JUMBO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-JUMBO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpicfObjectModules, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfObjectModules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HP-ICF-JUMBO-MIB", hpJumboStatsTable=hpJumboStatsTable, hpJumboStatsEntry=hpJumboStatsEntry, hpicfJumboObjects=hpicfJumboObjects, hpicfJumboConformance=hpicfJumboConformance, hpicfJumboCompliances=hpicfJumboCompliances, hpicfJumboStatsGroup=hpicfJumboStatsGroup, hpicfJumboMIB=hpicfJumboMIB, hpJumboStatsPkts4096to9216Octets=hpJumboStatsPkts4096to9216Octets, hpJumboStatsPkts1523to2047Octets=hpJumboStatsPkts1523to2047Octets, hpJumboStatsPkts2048to4095Octets=hpJumboStatsPkts2048to4095Octets, hpJumboStats=hpJumboStats, hpicfJumboGroups=hpicfJumboGroups, hpJumboStatsIndex=hpJumboStatsIndex, hpicfJumboCompliance=hpicfJumboCompliance, PYSNMP_MODULE_ID=hpicfJumboMIB)
