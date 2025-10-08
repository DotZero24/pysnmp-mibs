#
# PySNMP MIB module MARVELL-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/MARVELL-SPAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
rnd, rndNotifications = mibBuilder.importSymbols("RADLAN-MIB", "rnd", "rndNotifications")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
class SpanDestinationPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

class SpanSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("port", 1), ("vlan", 2), ("flow", 3), ("remote-vlan", 4))

class SpanSourceDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("both", 3))

rlSpan = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 219))
rlSpan.setRevisions(('2015-03-25 00:00',))
if mibBuilder.loadTexts: rlSpan.setLastUpdated('201503250000Z')
if mibBuilder.loadTexts: rlSpan.setOrganization('Marvell Computer Communications Ltd.')
rlSpanMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 219, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpanMibVersion.setStatus('current')
rlSpanDestinationTable = MibTable((1, 3, 6, 1, 4, 1, 89, 219, 2), )
if mibBuilder.loadTexts: rlSpanDestinationTable.setStatus('current')
rlSpanDestinationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 219, 2, 1), ).setIndexNames((0, "MARVELL-SPAN-MIB", "rlSpanDestinationSessionId"))
if mibBuilder.loadTexts: rlSpanDestinationEntry.setStatus('current')
rlSpanDestinationSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanDestinationSessionId.setStatus('current')
rlSpanDestinationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIfIndex.setStatus('current')
rlSpanDestinationIsReflector = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIsReflector.setStatus('current')
rlSpanDestinationPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 4), SpanDestinationPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationPortType.setStatus('current')
rlSpanDestinationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationRowStatus.setStatus('current')
rlSpanSourceTable = MibTable((1, 3, 6, 1, 4, 1, 89, 219, 3), )
if mibBuilder.loadTexts: rlSpanSourceTable.setStatus('current')
rlSpanSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 219, 3, 1), ).setIndexNames((0, "MARVELL-SPAN-MIB", "rlSpanSourceSessionId"), (0, "MARVELL-SPAN-MIB", "rlSpanSourceType"), (0, "MARVELL-SPAN-MIB", "rlSpanSourceIndex"))
if mibBuilder.loadTexts: rlSpanSourceEntry.setStatus('current')
rlSpanSourceSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanSourceSessionId.setStatus('current')
rlSpanSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 2), SpanSourceType())
if mibBuilder.loadTexts: rlSpanSourceType.setStatus('current')
rlSpanSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: rlSpanSourceIndex.setStatus('current')
rlSpanSourceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 4), SpanSourceDirection()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceDirection.setStatus('current')
rlSpanSourceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceRowStatus.setStatus('current')
mibBuilder.exportSymbols("MARVELL-SPAN-MIB", rlSpanDestinationIsReflector=rlSpanDestinationIsReflector, SpanDestinationPortType=SpanDestinationPortType, rlSpanDestinationIfIndex=rlSpanDestinationIfIndex, rlSpanDestinationEntry=rlSpanDestinationEntry, rlSpanSourceType=rlSpanSourceType, SpanSourceDirection=SpanSourceDirection, rlSpanDestinationSessionId=rlSpanDestinationSessionId, rlSpanSourceSessionId=rlSpanSourceSessionId, rlSpanSourceRowStatus=rlSpanSourceRowStatus, rlSpanDestinationTable=rlSpanDestinationTable, rlSpanSourceIndex=rlSpanSourceIndex, rlSpanMibVersion=rlSpanMibVersion, rlSpan=rlSpan, rlSpanDestinationRowStatus=rlSpanDestinationRowStatus, rlSpanDestinationPortType=rlSpanDestinationPortType, PYSNMP_MODULE_ID=rlSpan, rlSpanSourceEntry=rlSpanSourceEntry, SpanSourceType=SpanSourceType, rlSpanSourceTable=rlSpanSourceTable, rlSpanSourceDirection=rlSpanSourceDirection)
