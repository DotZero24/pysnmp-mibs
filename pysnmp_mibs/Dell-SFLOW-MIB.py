#
# PySNMP MIB module Dell-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dell/Dell-SFLOW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlsFlowMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 147))
rlsFlowMib.setRevisions(('2009-10-27 00:00',))
if mibBuilder.loadTexts: rlsFlowMib.setLastUpdated('200910270000Z')
if mibBuilder.loadTexts: rlsFlowMib.setOrganization('Dell')
rlsFlowStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 147, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlsFlowStatisticsTable.setStatus('current')
rlsFlowStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 147, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "Dell-SFLOW-MIB", "rlsFlowDataSource"))
if mibBuilder.loadTexts: rlsFlowStatisticsEntry.setStatus('current')
rlsFlowDataSource = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 147, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlsFlowDataSource.setStatus('current')
rlsFlowStatisticsSampledPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 147, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlsFlowStatisticsSampledPackets.setStatus('current')
rlsFlowStatisticsDatagramSent = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 147, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlsFlowStatisticsDatagramSent.setStatus('current')
rlsFlowStatisticsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 147, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlsFlowStatisticsAction.setStatus('current')
rlsFlowStatisticsReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 147, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("clear", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlsFlowStatisticsReset.setStatus('current')
mibBuilder.exportSymbols("Dell-SFLOW-MIB", rlsFlowStatisticsReset=rlsFlowStatisticsReset, rlsFlowMib=rlsFlowMib, rlsFlowStatisticsSampledPackets=rlsFlowStatisticsSampledPackets, rlsFlowDataSource=rlsFlowDataSource, rlsFlowStatisticsTable=rlsFlowStatisticsTable, rlsFlowStatisticsAction=rlsFlowStatisticsAction, rlsFlowStatisticsDatagramSent=rlsFlowStatisticsDatagramSent, PYSNMP_MODULE_ID=rlsFlowMib, rlsFlowStatisticsEntry=rlsFlowStatisticsEntry)
