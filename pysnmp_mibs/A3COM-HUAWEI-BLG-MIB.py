#
# PySNMP MIB module A3COM-HUAWEI-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-BLG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cBlg = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108))
h3cBlg.setRevisions(('2009-09-15 11:11',))
if mibBuilder.loadTexts: h3cBlg.setLastUpdated('200909151111Z')
if mibBuilder.loadTexts: h3cBlg.setOrganization('H3C Technologies Co., Ltd.')
class CounterClear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

h3cBlgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1))
h3cBlgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1), )
if mibBuilder.loadTexts: h3cBlgStatsTable.setStatus('current')
h3cBlgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-BLG-MIB", "h3cBlgIndex"))
if mibBuilder.loadTexts: h3cBlgStatsEntry.setStatus('current')
h3cBlgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cBlgIndex.setStatus('current')
h3cBlgGroupTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupTxPacketCount.setStatus('current')
h3cBlgGroupRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupRxPacketCount.setStatus('current')
h3cBlgGroupTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupTxByteCount.setStatus('current')
h3cBlgGroupRxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupRxByteCount.setStatus('current')
h3cBlgGroupCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 6), CounterClear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBlgGroupCountClear.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-BLG-MIB", h3cBlgGroupCountClear=h3cBlgGroupCountClear, h3cBlg=h3cBlg, h3cBlgStatsEntry=h3cBlgStatsEntry, PYSNMP_MODULE_ID=h3cBlg, h3cBlgGroupRxPacketCount=h3cBlgGroupRxPacketCount, h3cBlgIndex=h3cBlgIndex, h3cBlgGroupTxPacketCount=h3cBlgGroupTxPacketCount, h3cBlgObjects=h3cBlgObjects, CounterClear=CounterClear, h3cBlgStatsTable=h3cBlgStatsTable, h3cBlgGroupTxByteCount=h3cBlgGroupTxByteCount, h3cBlgGroupRxByteCount=h3cBlgGroupRxByteCount)
