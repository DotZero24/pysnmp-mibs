#
# PySNMP MIB module LCOS-SX-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/lancom/LCOS-SX-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:43:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lcosSX2, = mibBuilder.importSymbols("LANCOM-REF-MIB", "lcosSX2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lcosSxProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 2356, 16, 8))
lcosSxProducts.setRevisions(('2021-11-19 00:00',))
if mibBuilder.loadTexts: lcosSxProducts.setLastUpdated('202111190000Z')
if mibBuilder.loadTexts: lcosSxProducts.setOrganization('LANCOM Systems GmbH')
lcosSxProductsGS4530X = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 8, 4530))
lcosSxProductsGS4530XP = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 8, 4531))
lcosSxProductsGS4554X = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 8, 4554))
lcosSxProductsGS4554XP = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 8, 4555))
lcosSxProductsXS5110F = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 8, 5110))
lcosSxProductsXS5116QF = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 8, 5116))
lcosSxProductsXS6128QF = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 8, 6128))
mibBuilder.exportSymbols("LCOS-SX-PRODUCTS-MIB", lcosSxProductsXS5116QF=lcosSxProductsXS5116QF, lcosSxProductsGS4530XP=lcosSxProductsGS4530XP, lcosSxProductsXS6128QF=lcosSxProductsXS6128QF, lcosSxProducts=lcosSxProducts, lcosSxProductsGS4530X=lcosSxProductsGS4530X, PYSNMP_MODULE_ID=lcosSxProducts, lcosSxProductsGS4554X=lcosSxProductsGS4554X, lcosSxProductsXS5110F=lcosSxProductsXS5110F, lcosSxProductsGS4554XP=lcosSxProductsGS4554XP)
