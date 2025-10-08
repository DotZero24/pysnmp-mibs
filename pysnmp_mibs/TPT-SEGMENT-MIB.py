#
# PySNMP MIB module TPT-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-SEGMENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:28 2025
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
tpt_segment_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19)).setLabel("tpt-segment-objs")
tpt_segment_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_segment_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_segment_objs.setOrganization('Trend Micro, Inc.')
class SegmentSflowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("error", 2), ("not-applicable", 3))

segmentTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1), )
if mibBuilder.loadTexts: segmentTable.setStatus('current')
segmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1), ).setIndexNames((0, "TPT-SEGMENT-MIB", "slotIndex"), (0, "TPT-SEGMENT-MIB", "segmentIndex"))
if mibBuilder.loadTexts: segmentEntry.setStatus('current')
slotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotIndex.setStatus('current')
segmentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentIndex.setStatus('current')
segmentSflowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 3), SegmentSflowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentSflowStatus.setStatus('current')
sFlowDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sFlowDivisor.setStatus('current')
mibBuilder.exportSymbols("TPT-SEGMENT-MIB", segmentSflowStatus=segmentSflowStatus, tpt_segment_objs=tpt_segment_objs, segmentIndex=segmentIndex, segmentTable=segmentTable, PYSNMP_MODULE_ID=tpt_segment_objs, sFlowDivisor=sFlowDivisor, segmentEntry=segmentEntry, slotIndex=slotIndex, SegmentSflowStatus=SegmentSflowStatus)
