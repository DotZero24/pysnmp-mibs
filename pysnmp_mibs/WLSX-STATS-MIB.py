#
# PySNMP MIB module WLSX-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aruba/WLSX-STATS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, snmpModules, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "snmpModules", "Gauge32")
TDomain, TAddress, RowStatus, TextualConvention, TimeInterval, MacAddress, StorageType, TestAndIncr, PhysAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "TAddress", "RowStatus", "TextualConvention", "TimeInterval", "MacAddress", "StorageType", "TestAndIncr", "PhysAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("WLSX-STATS-MIB", wlsxStatsRequestTable=wlsxStatsRequestTable, PYSNMP_MODULE_ID=wlsxStatsMIB, wlsxStatsOpGroup=wlsxStatsOpGroup, wlsxStatsInterval=wlsxStatsInterval, wlsxStatsCookie=wlsxStatsCookie, wlsxStatsReqType=wlsxStatsReqType, wlsxStatsMIB=wlsxStatsMIB, wlsxStatsRequestEntry=wlsxStatsRequestEntry, wlsxStatsIndex=wlsxStatsIndex)
