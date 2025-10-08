#
# PySNMP MIB module HPN-ICF-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-BLG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
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
mibBuilder.exportSymbols("HPN-ICF-BLG-MIB", hpnicfBlgGroupTxPacketCount=hpnicfBlgGroupTxPacketCount, hpnicfBlgObjects=hpnicfBlgObjects, hpnicfBlgGroupRxPacketCount=hpnicfBlgGroupRxPacketCount, hpnicfBlgGroupTxByteCount=hpnicfBlgGroupTxByteCount, hpnicfBlgStatsTable=hpnicfBlgStatsTable, hpnicfBlg=hpnicfBlg, hpnicfBlgGroupRxByteCount=hpnicfBlgGroupRxByteCount, PYSNMP_MODULE_ID=hpnicfBlg, CounterClear=CounterClear, hpnicfBlgStatsEntry=hpnicfBlgStatsEntry, hpnicfBlgGroupCountClear=hpnicfBlgGroupCountClear, hpnicfBlgIndex=hpnicfBlgIndex)
