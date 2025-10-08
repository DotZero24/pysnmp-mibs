#
# PySNMP MIB module BAY-STACK-ECMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/BAY-STACK-ECMP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackEcmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 15))
bayStackEcmpMib.setRevisions(('2016-09-06 00:00', '2012-06-01 00:00', '2005-09-09 00:00',))
if mibBuilder.loadTexts: bayStackEcmpMib.setLastUpdated('201609060000Z')
if mibBuilder.loadTexts: bayStackEcmpMib.setOrganization('Nortel Networks')
bsEcmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 15, 0))
bsEcmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 15, 1))
bsEcmpScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 1))
bsEcmpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2), )
if mibBuilder.loadTexts: bsEcmpConfigTable.setStatus('current')
bsEcmpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-ECMP-MIB", "bsEcmpConfigRoutingProtocol"))
if mibBuilder.loadTexts: bsEcmpConfigEntry.setStatus('current')
bsEcmpConfigRoutingProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("static", 1), ("rip", 2), ("ospf", 3), ("bgp", 4), ("isis", 5))))
if mibBuilder.loadTexts: bsEcmpConfigRoutingProtocol.setStatus('current')
bsEcmpConfigMaxPath = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsEcmpConfigMaxPath.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-ECMP-MIB", bsEcmpObjects=bsEcmpObjects, bsEcmpNotifications=bsEcmpNotifications, bsEcmpConfigTable=bsEcmpConfigTable, bsEcmpConfigEntry=bsEcmpConfigEntry, bsEcmpScalars=bsEcmpScalars, bayStackEcmpMib=bayStackEcmpMib, bsEcmpConfigRoutingProtocol=bsEcmpConfigRoutingProtocol, PYSNMP_MODULE_ID=bayStackEcmpMib, bsEcmpConfigMaxPath=bsEcmpConfigMaxPath)
