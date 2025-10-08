#
# PySNMP MIB module RDN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/riverdelta/RDN-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rdnProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 1))
rdnProducts.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-17 00:00',))
if mibBuilder.loadTexts: rdnProducts.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnProducts.setOrganization('Motorola')
rdnProductsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 0))
rdnProductsBSR64000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 1))
rdnProductsBSR1000B = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 2))
rdnProductsBSR1000R = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 3))
rdnProductsOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 4))
mibBuilder.exportSymbols("RDN-PRODUCTS-MIB", PYSNMP_MODULE_ID=rdnProducts, rdnProductsBSR1000R=rdnProductsBSR1000R, rdnProductsOSR2000=rdnProductsOSR2000, rdnProducts=rdnProducts, rdnProductsUnknown=rdnProductsUnknown, rdnProductsBSR1000B=rdnProductsBSR1000B, rdnProductsBSR64000=rdnProductsBSR64000)
