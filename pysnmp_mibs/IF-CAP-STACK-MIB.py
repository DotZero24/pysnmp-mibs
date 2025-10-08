#
# PySNMP MIB module IF-CAP-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/IF-CAP-STACK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifInvStackGroup, = mibBuilder.importSymbols("IF-INVERTED-STACK-MIB", "ifInvStackGroup")
ifStackGroup2, ifStackLowerLayer, ifStackHigherLayer = mibBuilder.importSymbols("IF-MIB", "ifStackGroup2", "ifStackLowerLayer", "ifStackHigherLayer")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ifCapStackMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 166))
ifCapStackMIB.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: ifCapStackMIB.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: ifCapStackMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
ifCapStackObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 166, 1))
ifCapStackConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 166, 2))
ifCapStackTable = MibTable((1, 3, 6, 1, 2, 1, 166, 1, 1), )
if mibBuilder.loadTexts: ifCapStackTable.setStatus('current')
ifCapStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 166, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifStackHigherLayer"), (0, "IF-MIB", "ifStackLowerLayer"))
if mibBuilder.loadTexts: ifCapStackEntry.setStatus('current')
ifCapStackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 166, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCapStackStatus.setStatus('current')
ifInvCapStackTable = MibTable((1, 3, 6, 1, 2, 1, 166, 1, 2), )
if mibBuilder.loadTexts: ifInvCapStackTable.setStatus('current')
ifInvCapStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 166, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: ifInvCapStackEntry.setStatus('current')
ifInvCapStackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 166, 1, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInvCapStackStatus.setStatus('current')
ifCapStackGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 166, 2, 1))
ifCapStackCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 166, 2, 2))
ifCapStackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 166, 2, 1, 1)).setObjects(("IF-CAP-STACK-MIB", "ifCapStackStatus"), ("IF-CAP-STACK-MIB", "ifInvCapStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifCapStackGroup = ifCapStackGroup.setStatus('current')
ifCapStackCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 166, 2, 2, 1)).setObjects(("IF-CAP-STACK-MIB", "ifCapStackGroup"), ("IF-MIB", "ifStackGroup2"), ("IF-INVERTED-STACK-MIB", "ifInvStackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifCapStackCompliance = ifCapStackCompliance.setStatus('current')
mibBuilder.exportSymbols("IF-CAP-STACK-MIB", ifCapStackTable=ifCapStackTable, PYSNMP_MODULE_ID=ifCapStackMIB, ifCapStackGroups=ifCapStackGroups, ifCapStackMIB=ifCapStackMIB, ifInvCapStackTable=ifInvCapStackTable, ifCapStackCompliances=ifCapStackCompliances, ifCapStackConformance=ifCapStackConformance, ifCapStackGroup=ifCapStackGroup, ifCapStackObjects=ifCapStackObjects, ifCapStackCompliance=ifCapStackCompliance, ifCapStackStatus=ifCapStackStatus, ifInvCapStackEntry=ifInvCapStackEntry, ifInvCapStackStatus=ifInvCapStackStatus, ifCapStackEntry=ifCapStackEntry)
