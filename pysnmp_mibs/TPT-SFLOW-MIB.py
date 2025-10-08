#
# PySNMP MIB module TPT-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-SFLOW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_sflow_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18)).setLabel("tpt-sflow-objs")
tpt_sflow_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_sflow_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_sflow_objs.setOrganization('Trend Micro, Inc.')
class SflowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("error", 2), ("not-applicable", 3))

sFlowCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1), )
if mibBuilder.loadTexts: sFlowCollectorTable.setStatus('current')
sFlowCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1), ).setIndexNames((0, "TPT-SFLOW-MIB", "collectorIndex"))
if mibBuilder.loadTexts: sFlowCollectorEntry.setStatus('current')
collectorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: collectorIndex.setStatus('current')
collectorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: collectorAddr.setStatus('current')
udpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpPort.setStatus('current')
collectorAddrV6 = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: collectorAddrV6.setStatus('current')
sFlowStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 2), SflowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sFlowStatus.setStatus('current')
mibBuilder.exportSymbols("TPT-SFLOW-MIB", udpPort=udpPort, tpt_sflow_objs=tpt_sflow_objs, sFlowStatus=sFlowStatus, SflowStatus=SflowStatus, sFlowCollectorEntry=sFlowCollectorEntry, sFlowCollectorTable=sFlowCollectorTable, collectorAddrV6=collectorAddrV6, collectorAddr=collectorAddr, PYSNMP_MODULE_ID=tpt_sflow_objs, collectorIndex=collectorIndex)
