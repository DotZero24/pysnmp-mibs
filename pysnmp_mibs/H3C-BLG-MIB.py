#
# PySNMP MIB module H3C-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-BLG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cBlg = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108))
h3cBlg.setRevisions(('2009-09-15 11:11',))
if mibBuilder.loadTexts: h3cBlg.setLastUpdated('200909151111Z')
if mibBuilder.loadTexts: h3cBlg.setOrganization('H3C Technologies Co., Ltd.')
class CounterClear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

h3cBlgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108, 1))
h3cBlgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108, 1, 1), )
if mibBuilder.loadTexts: h3cBlgStatsTable.setStatus('current')
h3cBlgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108, 1, 1, 1), ).setIndexNames((0, "H3C-BLG-MIB", "h3cBlgIndex"))
if mibBuilder.loadTexts: h3cBlgStatsEntry.setStatus('current')
h3cBlgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cBlgIndex.setStatus('current')
h3cBlgGroupTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupTxPacketCount.setStatus('current')
h3cBlgGroupRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupRxPacketCount.setStatus('current')
h3cBlgGroupTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupTxByteCount.setStatus('current')
h3cBlgGroupRxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupRxByteCount.setStatus('current')
h3cBlgGroupCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 108, 1, 1, 1, 6), CounterClear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBlgGroupCountClear.setStatus('current')
mibBuilder.exportSymbols("H3C-BLG-MIB", h3cBlgObjects=h3cBlgObjects, h3cBlgGroupTxByteCount=h3cBlgGroupTxByteCount, h3cBlgGroupTxPacketCount=h3cBlgGroupTxPacketCount, h3cBlgStatsEntry=h3cBlgStatsEntry, h3cBlgGroupRxPacketCount=h3cBlgGroupRxPacketCount, h3cBlgGroupRxByteCount=h3cBlgGroupRxByteCount, h3cBlg=h3cBlg, PYSNMP_MODULE_ID=h3cBlg, CounterClear=CounterClear, h3cBlgGroupCountClear=h3cBlgGroupCountClear, h3cBlgIndex=h3cBlgIndex, h3cBlgStatsTable=h3cBlgStatsTable)
