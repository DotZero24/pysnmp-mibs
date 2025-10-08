#
# PySNMP MIB module WLSX-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/WLSX-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TDomain, TimeInterval, RowStatus, StorageType, TAddress, TestAndIncr, PhysAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TDomain", "TimeInterval", "RowStatus", "StorageType", "TAddress", "TestAndIncr", "PhysAddress", "TruthValue", "TextualConvention")
wlsxStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15))
wlsxStatsMIB.setRevisions(('2020-08-14 17:45',))
if mibBuilder.loadTexts: wlsxStatsMIB.setLastUpdated('202008141745Z')
if mibBuilder.loadTexts: wlsxStatsMIB.setOrganization('Aruba, a Hewlett Packard Enterprise company')
wlsxStatsOpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1))
wlsxStatsRequestTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1), )
if mibBuilder.loadTexts: wlsxStatsRequestTable.setStatus('current')
wlsxStatsRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1), ).setIndexNames((0, "WLSX-STATS-MIB", "wlsxStatsIndex"))
if mibBuilder.loadTexts: wlsxStatsRequestEntry.setStatus('current')
wlsxStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: wlsxStatsIndex.setStatus('current')
wlsxStatsReqType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsReqType.setStatus('current')
wlsxStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsInterval.setStatus('current')
wlsxStatsCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsCookie.setStatus('current')
mibBuilder.exportSymbols("WLSX-STATS-MIB", wlsxStatsOpGroup=wlsxStatsOpGroup, wlsxStatsRequestTable=wlsxStatsRequestTable, PYSNMP_MODULE_ID=wlsxStatsMIB, wlsxStatsRequestEntry=wlsxStatsRequestEntry, wlsxStatsReqType=wlsxStatsReqType, wlsxStatsCookie=wlsxStatsCookie, wlsxStatsIndex=wlsxStatsIndex, wlsxStatsInterval=wlsxStatsInterval, wlsxStatsMIB=wlsxStatsMIB)
