#
# PySNMP MIB module LCOS-SX-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/lancom/LCOS-SX-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:11:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lcosSX2, = mibBuilder.importSymbols("LANCOM-REF-MIB", "lcosSX2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LCOS-SX-PRODUCTS-MIB", lcosSxProductsGS4554XP=lcosSxProductsGS4554XP, lcosSxProductsXS6128QF=lcosSxProductsXS6128QF, PYSNMP_MODULE_ID=lcosSxProducts, lcosSxProducts=lcosSxProducts, lcosSxProductsGS4530X=lcosSxProductsGS4530X, lcosSxProductsGS4554X=lcosSxProductsGS4554X, lcosSxProductsGS4530XP=lcosSxProductsGS4530XP, lcosSxProductsXS5116QF=lcosSxProductsXS5116QF, lcosSxProductsXS5110F=lcosSxProductsXS5110F)
