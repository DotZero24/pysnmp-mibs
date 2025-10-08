#
# PySNMP MIB module A3COM-SWITCHING-SYSTEMS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-SWITCHING-SYSTEMS-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("A3COM-SWITCHING-SYSTEMS-PRODUCTS-MIB", superstackSystemProducts=superstackSystemProducts, superstackProducts=superstackProducts, superstackModularProducts=superstackModularProducts, superstackChassisProducts=superstackChassisProducts, corebuilderModularProducts=corebuilderModularProducts, corebuilderChassisProducts=corebuilderChassisProducts, ssSystem3900Family=ssSystem3900Family, cb9400=cb9400, cbSystem9400Family=cbSystem9400Family, ss9300=ss9300, ssSystem9300Family=ssSystem9300Family, switches=switches, cb3500=cb3500, ss3900_24=ss3900_24, products=products, ss3900_36=ss3900_36, cbModular3500Family=cbModular3500Family, corebuilderProductsIII=corebuilderProductsIII, corebuilderSystemProducts=corebuilderSystemProducts, a3Com=a3Com)
