#
# PySNMP MIB module BAY-STACK-ECMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/BAY-STACK-ECMP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BAY-STACK-ECMP-MIB", bsEcmpConfigTable=bsEcmpConfigTable, PYSNMP_MODULE_ID=bayStackEcmpMib, bsEcmpConfigRoutingProtocol=bsEcmpConfigRoutingProtocol, bayStackEcmpMib=bayStackEcmpMib, bsEcmpScalars=bsEcmpScalars, bsEcmpObjects=bsEcmpObjects, bsEcmpNotifications=bsEcmpNotifications, bsEcmpConfigMaxPath=bsEcmpConfigMaxPath, bsEcmpConfigEntry=bsEcmpConfigEntry)
