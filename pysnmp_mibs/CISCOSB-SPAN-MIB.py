#
# PySNMP MIB module CISCOSB-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciscosb/CISCOSB-SPAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
rndNotifications, = mibBuilder.importSymbols("CISCOSB-TRAPS-MIB", "rndNotifications")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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

class SpanDestinationReflectorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("span", 1), ("rspan-start", 2), ("rspan-final", 3))

rlSpan = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219))
rlSpan.setRevisions(('2015-03-25 00:00',))
if mibBuilder.loadTexts: rlSpan.setLastUpdated('201503250000Z')
if mibBuilder.loadTexts: rlSpan.setOrganization('Cisco Systems, Inc.')
rlSpanMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpanMibVersion.setStatus('current')
rlSpanDestinationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2), )
if mibBuilder.loadTexts: rlSpanDestinationTable.setStatus('current')
rlSpanDestinationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1), ).setIndexNames((0, "CISCOSB-SPAN-MIB", "rlSpanDestinationSessionId"))
if mibBuilder.loadTexts: rlSpanDestinationEntry.setStatus('current')
rlSpanDestinationSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanDestinationSessionId.setStatus('current')
rlSpanDestinationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIfIndex.setStatus('current')
rlSpanDestinationIsReflector = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 3), SpanDestinationReflectorType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIsReflector.setStatus('current')
rlSpanDestinationPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 4), SpanDestinationPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationPortType.setStatus('current')
rlSpanDestinationRemoteVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 5), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationRemoteVlanId.setStatus('current')
rlSpanDestinationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationRowStatus.setStatus('current')
rlSpanSourceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3), )
if mibBuilder.loadTexts: rlSpanSourceTable.setStatus('current')
rlSpanSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1), ).setIndexNames((0, "CISCOSB-SPAN-MIB", "rlSpanSourceSessionId"), (0, "CISCOSB-SPAN-MIB", "rlSpanSourceType"), (0, "CISCOSB-SPAN-MIB", "rlSpanSourceIndex"))
if mibBuilder.loadTexts: rlSpanSourceEntry.setStatus('current')
rlSpanSourceSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanSourceSessionId.setStatus('current')
rlSpanSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 2), SpanSourceType())
if mibBuilder.loadTexts: rlSpanSourceType.setStatus('current')
rlSpanSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: rlSpanSourceIndex.setStatus('current')
rlSpanSourceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 4), SpanSourceDirection()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceDirection.setStatus('current')
rlSpanSourceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceRowStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SPAN-MIB", rlSpanDestinationEntry=rlSpanDestinationEntry, PYSNMP_MODULE_ID=rlSpan, SpanDestinationPortType=SpanDestinationPortType, SpanSourceType=SpanSourceType, rlSpanDestinationTable=rlSpanDestinationTable, rlSpanSourceDirection=rlSpanSourceDirection, rlSpanSourceType=rlSpanSourceType, rlSpanDestinationSessionId=rlSpanDestinationSessionId, rlSpanDestinationRowStatus=rlSpanDestinationRowStatus, rlSpanDestinationIfIndex=rlSpanDestinationIfIndex, rlSpan=rlSpan, rlSpanSourceIndex=rlSpanSourceIndex, rlSpanDestinationIsReflector=rlSpanDestinationIsReflector, SpanSourceDirection=SpanSourceDirection, rlSpanSourceRowStatus=rlSpanSourceRowStatus, rlSpanDestinationRemoteVlanId=rlSpanDestinationRemoteVlanId, rlSpanSourceSessionId=rlSpanSourceSessionId, rlSpanSourceEntry=rlSpanSourceEntry, rlSpanDestinationPortType=rlSpanDestinationPortType, SpanDestinationReflectorType=SpanDestinationReflectorType, rlSpanMibVersion=rlSpanMibVersion, rlSpanSourceTable=rlSpanSourceTable)
