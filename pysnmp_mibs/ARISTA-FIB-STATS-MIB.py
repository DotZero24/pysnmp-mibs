#
# PySNMP MIB module ARISTA-FIB-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arista/ARISTA-FIB-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressPrefixLength, InetVersion = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetVersion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaFIBStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 23))
aristaFIBStatsMIB.setRevisions(('2017-05-19 00:00',))
if mibBuilder.loadTexts: aristaFIBStatsMIB.setLastUpdated('201705190000Z')
if mibBuilder.loadTexts: aristaFIBStatsMIB.setOrganization('Arista Networks, Inc.')
class RouteType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 8, 9, 13, 14, 200, 201, 202, 203, 204, 205))
    namedValues = NamedValues(("other", 1), ("connected", 2), ("static", 3), ("rip", 8), ("isIs", 9), ("ospf", 13), ("bgp", 14), ("ospfv3", 200), ("staticNonPersistent", 201), ("staticNexthopGroup", 202), ("attached", 203), ("vcs", 204), ("internal", 205))

aristaFIBStatsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1))
aristaFIBStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 23, 2))
aristaFIBStatsSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 1), )
if mibBuilder.loadTexts: aristaFIBStatsSummaryTable.setStatus('current')
aristaFIBStatsSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 1, 1), ).setIndexNames((0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsAF"))
if mibBuilder.loadTexts: aristaFIBStatsSummaryEntry.setStatus('current')
aristaFIBStatsAF = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 1, 1, 1), InetVersion())
if mibBuilder.loadTexts: aristaFIBStatsAF.setStatus('current')
aristaFIBStatsTotalRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaFIBStatsTotalRoutes.setStatus('current')
aristaFIBStatsByRouteTypeTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 2), )
if mibBuilder.loadTexts: aristaFIBStatsByRouteTypeTable.setStatus('current')
aristaFIBStatsByRouteTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 2, 1), ).setIndexNames((0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsAF"), (0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsRouteType"))
if mibBuilder.loadTexts: aristaFIBStatsByRouteTypeEntry.setStatus('current')
aristaFIBStatsRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 2, 1, 1), RouteType())
if mibBuilder.loadTexts: aristaFIBStatsRouteType.setStatus('current')
aristaFIBStatsTotalRoutesForRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaFIBStatsTotalRoutesForRouteType.setStatus('current')
aristaFIBStatsByPrefixLenTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 3), )
if mibBuilder.loadTexts: aristaFIBStatsByPrefixLenTable.setStatus('current')
aristaFIBStatsByPrefixLenEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 3, 1), ).setIndexNames((0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsAF"), (0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsPrefixLen"))
if mibBuilder.loadTexts: aristaFIBStatsByPrefixLenEntry.setStatus('current')
aristaFIBStatsPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 3, 1, 1), InetAddressPrefixLength())
if mibBuilder.loadTexts: aristaFIBStatsPrefixLen.setStatus('current')
aristaFIBStatsTotalRoutesForPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 3, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaFIBStatsTotalRoutesForPrefixLen.setStatus('current')
aristaFIBStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 23, 2, 1))
aristaFIBStatsMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 23, 2, 2))
aristaFIBStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 23, 2, 1, 1)).setObjects(("ARISTA-FIB-STATS-MIB", "aristaFIBStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaFIBStatsMibCompliance = aristaFIBStatsMibCompliance.setStatus('current')
aristaFIBStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 23, 2, 2, 1)).setObjects(("ARISTA-FIB-STATS-MIB", "aristaFIBStatsTotalRoutes"), ("ARISTA-FIB-STATS-MIB", "aristaFIBStatsTotalRoutesForRouteType"), ("ARISTA-FIB-STATS-MIB", "aristaFIBStatsTotalRoutesForPrefixLen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaFIBStatsGroup = aristaFIBStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-FIB-STATS-MIB", aristaFIBStatsPrefixLen=aristaFIBStatsPrefixLen, aristaFIBStatsMibGroups=aristaFIBStatsMibGroups, aristaFIBStatsTotalRoutesForRouteType=aristaFIBStatsTotalRoutesForRouteType, RouteType=RouteType, aristaFIBStatsMIB=aristaFIBStatsMIB, aristaFIBStatsSummaryTable=aristaFIBStatsSummaryTable, aristaFIBStatsAF=aristaFIBStatsAF, aristaFIBStatsMibObjects=aristaFIBStatsMibObjects, aristaFIBStatsTotalRoutes=aristaFIBStatsTotalRoutes, aristaFIBStatsByRouteTypeTable=aristaFIBStatsByRouteTypeTable, aristaFIBStatsByPrefixLenEntry=aristaFIBStatsByPrefixLenEntry, aristaFIBStatsByRouteTypeEntry=aristaFIBStatsByRouteTypeEntry, aristaFIBStatsTotalRoutesForPrefixLen=aristaFIBStatsTotalRoutesForPrefixLen, aristaFIBStatsMibConformance=aristaFIBStatsMibConformance, aristaFIBStatsMibCompliance=aristaFIBStatsMibCompliance, aristaFIBStatsByPrefixLenTable=aristaFIBStatsByPrefixLenTable, aristaFIBStatsMibCompliances=aristaFIBStatsMibCompliances, aristaFIBStatsSummaryEntry=aristaFIBStatsSummaryEntry, aristaFIBStatsGroup=aristaFIBStatsGroup, aristaFIBStatsRouteType=aristaFIBStatsRouteType, PYSNMP_MODULE_ID=aristaFIBStatsMIB)
