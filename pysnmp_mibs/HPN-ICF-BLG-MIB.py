#
# PySNMP MIB module HPN-ICF-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-BLG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfBlg = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108))
hpnicfBlg.setRevisions(('2009-09-15 11:11',))
if mibBuilder.loadTexts: hpnicfBlg.setLastUpdated('200909151111Z')
if mibBuilder.loadTexts: hpnicfBlg.setOrganization('')
class CounterClear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

hpnicfBlgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1))
hpnicfBlgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1), )
if mibBuilder.loadTexts: hpnicfBlgStatsTable.setStatus('current')
hpnicfBlgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-BLG-MIB", "hpnicfBlgIndex"))
if mibBuilder.loadTexts: hpnicfBlgStatsEntry.setStatus('current')
hpnicfBlgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfBlgIndex.setStatus('current')
hpnicfBlgGroupTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupTxPacketCount.setStatus('current')
hpnicfBlgGroupRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupRxPacketCount.setStatus('current')
hpnicfBlgGroupTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupTxByteCount.setStatus('current')
hpnicfBlgGroupRxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupRxByteCount.setStatus('current')
hpnicfBlgGroupCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 6), CounterClear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfBlgGroupCountClear.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-BLG-MIB", hpnicfBlgStatsEntry=hpnicfBlgStatsEntry, hpnicfBlgGroupCountClear=hpnicfBlgGroupCountClear, hpnicfBlg=hpnicfBlg, hpnicfBlgGroupRxPacketCount=hpnicfBlgGroupRxPacketCount, hpnicfBlgObjects=hpnicfBlgObjects, hpnicfBlgGroupRxByteCount=hpnicfBlgGroupRxByteCount, CounterClear=CounterClear, hpnicfBlgGroupTxPacketCount=hpnicfBlgGroupTxPacketCount, PYSNMP_MODULE_ID=hpnicfBlg, hpnicfBlgStatsTable=hpnicfBlgStatsTable, hpnicfBlgGroupTxByteCount=hpnicfBlgGroupTxByteCount, hpnicfBlgIndex=hpnicfBlgIndex)
