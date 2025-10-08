#
# PySNMP MIB module WESTERMO-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/westermo/WESTERMO-OID-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
westermo = ModuleIdentity((1, 3, 6, 1, 4, 1, 16177))
westermo.setRevisions(('2010-10-20 00:00', '2009-05-28 00:00', '2009-05-18 00:00',))
if mibBuilder.loadTexts: westermo.setLastUpdated('201010200000Z')
if mibBuilder.loadTexts: westermo.setOrganization('Westermo Teleindustri AB')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 2))
i_line = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 300)).setLabel("i-line")
mibBuilder.exportSymbols("WESTERMO-OID-MIB", westermo=westermo, PYSNMP_MODULE_ID=westermo, common=common, i_line=i_line, products=products)
