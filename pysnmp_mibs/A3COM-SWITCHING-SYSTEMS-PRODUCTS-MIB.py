#
# PySNMP MIB module A3COM-SWITCHING-SYSTEMS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-SWITCHING-SYSTEMS-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1))
switches = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16))
corebuilderProductsIII = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 1))
superstackProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 2))
corebuilderModularProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 1))
corebuilderSystemProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 2))
corebuilderChassisProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 3))
cbModular3500Family = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 1, 1))
cbSystem9400Family = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 2, 1))
cb3500 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 1, 1, 1))
cb9400 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 2, 1, 1))
superstackModularProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 1))
superstackSystemProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2))
superstackChassisProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 3))
ssSystem3900Family = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 1))
ssSystem9300Family = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 2))
ss3900_24 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 1, 1)).setLabel("ss3900-24")
ss3900_36 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 1, 2)).setLabel("ss3900-36")
ss9300 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 2, 1))
mibBuilder.exportSymbols("A3COM-SWITCHING-SYSTEMS-PRODUCTS-MIB", ss3900_36=ss3900_36, superstackChassisProducts=superstackChassisProducts, cbSystem9400Family=cbSystem9400Family, ssSystem3900Family=ssSystem3900Family, ssSystem9300Family=ssSystem9300Family, a3Com=a3Com, superstackModularProducts=superstackModularProducts, cb9400=cb9400, ss3900_24=ss3900_24, switches=switches, corebuilderModularProducts=corebuilderModularProducts, superstackSystemProducts=superstackSystemProducts, corebuilderProductsIII=corebuilderProductsIII, corebuilderSystemProducts=corebuilderSystemProducts, corebuilderChassisProducts=corebuilderChassisProducts, products=products, ss9300=ss9300, superstackProducts=superstackProducts, cbModular3500Family=cbModular3500Family, cb3500=cb3500)
