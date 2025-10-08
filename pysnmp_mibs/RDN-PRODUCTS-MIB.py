#
# PySNMP MIB module RDN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/riverdelta/RDN-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 1))
rdnProducts.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-17 00:00',))
if mibBuilder.loadTexts: rdnProducts.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnProducts.setOrganization('Motorola')
rdnProductsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 0))
rdnProductsBSR64000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 1))
rdnProductsBSR1000B = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 2))
rdnProductsBSR1000R = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 3))
rdnProductsOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 1, 4))
mibBuilder.exportSymbols("RDN-PRODUCTS-MIB", rdnProductsBSR1000B=rdnProductsBSR1000B, rdnProductsUnknown=rdnProductsUnknown, rdnProductsBSR1000R=rdnProductsBSR1000R, rdnProductsOSR2000=rdnProductsOSR2000, rdnProductsBSR64000=rdnProductsBSR64000, PYSNMP_MODULE_ID=rdnProducts, rdnProducts=rdnProducts)
