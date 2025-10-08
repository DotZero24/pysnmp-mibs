#
# PySNMP MIB module BAY-STACK-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/BAY-STACK-IF-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("BAY-STACK-IF-EXT-MIB", bsIfExtObjects=bsIfExtObjects, bsIfExtIfDirectedBroadcast=bsIfExtIfDirectedBroadcast, bsIfExtScalars=bsIfExtScalars, PYSNMP_MODULE_ID=bayStackIfExtMib, bsIfExtIfEntry=bsIfExtIfEntry, bsIfExtNotifications=bsIfExtNotifications, bsIfExtIfIndex=bsIfExtIfIndex, bsIfExtIfTable=bsIfExtIfTable, bayStackIfExtMib=bayStackIfExtMib, bsIfExtDirectedBroadcast=bsIfExtDirectedBroadcast)
