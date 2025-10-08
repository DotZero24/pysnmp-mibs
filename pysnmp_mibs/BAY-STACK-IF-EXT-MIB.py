#
# PySNMP MIB module BAY-STACK-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/BAY-STACK-IF-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackIfExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 40))
bayStackIfExtMib.setRevisions(('2012-05-31 00:00', '2010-11-03 00:00',))
if mibBuilder.loadTexts: bayStackIfExtMib.setLastUpdated('201205310000Z')
if mibBuilder.loadTexts: bayStackIfExtMib.setOrganization('Avaya')
bsIfExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 40, 0))
bsIfExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 40, 1))
bsIfExtScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 1))
bsIfExtDirectedBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIfExtDirectedBroadcast.setStatus('current')
bsIfExtIfTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 2), )
if mibBuilder.loadTexts: bsIfExtIfTable.setStatus('current')
bsIfExtIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-IF-EXT-MIB", "bsIfExtIfIndex"))
if mibBuilder.loadTexts: bsIfExtIfEntry.setStatus('current')
bsIfExtIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsIfExtIfIndex.setStatus('current')
bsIfExtIfDirectedBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIfExtIfDirectedBroadcast.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-IF-EXT-MIB", bsIfExtIfEntry=bsIfExtIfEntry, bsIfExtIfDirectedBroadcast=bsIfExtIfDirectedBroadcast, bsIfExtDirectedBroadcast=bsIfExtDirectedBroadcast, bsIfExtNotifications=bsIfExtNotifications, PYSNMP_MODULE_ID=bayStackIfExtMib, bsIfExtScalars=bsIfExtScalars, bsIfExtIfTable=bsIfExtIfTable, bsIfExtIfIndex=bsIfExtIfIndex, bayStackIfExtMib=bayStackIfExtMib, bsIfExtObjects=bsIfExtObjects)
