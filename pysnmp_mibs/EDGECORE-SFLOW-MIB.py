#
# PySNMP MIB module EDGECORE-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/edgecore/EDGECORE-SFLOW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("EDGECORE-MIB", "rnd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlsFlowMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 147))
rlsFlowMib.setRevisions(('2009-10-27 00:00',))
if mibBuilder.loadTexts: rlsFlowMib.setLastUpdated('200910270000Z')
if mibBuilder.loadTexts: rlsFlowMib.setOrganization('Marvell Computer Communications Ltd.')
rlsFlowStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 147, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlsFlowStatisticsTable.setStatus('current')
rlsFlowStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 147, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "EDGECORE-SFLOW-MIB", "rlsFlowDataSource"))
if mibBuilder.loadTexts: rlsFlowStatisticsEntry.setStatus('current')
rlsFlowDataSource = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 147, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlsFlowDataSource.setStatus('current')
rlsFlowStatisticsSampledPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 147, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlsFlowStatisticsSampledPackets.setStatus('current')
rlsFlowStatisticsDatagramSent = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 147, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlsFlowStatisticsDatagramSent.setStatus('current')
rlsFlowStatisticsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 147, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlsFlowStatisticsAction.setStatus('current')
rlsFlowStatisticsReset = MibScalar((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 147, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("clear", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlsFlowStatisticsReset.setStatus('current')
mibBuilder.exportSymbols("EDGECORE-SFLOW-MIB", rlsFlowStatisticsEntry=rlsFlowStatisticsEntry, PYSNMP_MODULE_ID=rlsFlowMib, rlsFlowDataSource=rlsFlowDataSource, rlsFlowStatisticsReset=rlsFlowStatisticsReset, rlsFlowStatisticsDatagramSent=rlsFlowStatisticsDatagramSent, rlsFlowStatisticsAction=rlsFlowStatisticsAction, rlsFlowStatisticsSampledPackets=rlsFlowStatisticsSampledPackets, rlsFlowMib=rlsFlowMib, rlsFlowStatisticsTable=rlsFlowStatisticsTable)
