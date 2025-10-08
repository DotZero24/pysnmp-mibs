#
# PySNMP MIB module SW3700PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SW3700PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_Dgs3700Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102)).setLabel("dlink-Dgs3700Series")
dgs3700 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1))
dgs3712 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1))
dgs3712g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2))
dgs3710 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 3))
dgs3710s = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 4))
dgs3712c = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 5))
dlink_Dgs3700SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 102)).setLabel("dlink-Dgs3700SeriesProd")
dgs3712Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 102, 1))
dgs3712pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 102, 2))
mibBuilder.exportSymbols("SW3700PRIMGMT-MIB", dgs3710s=dgs3710s, dgs3712Prod=dgs3712Prod, dgs3712pProd=dgs3712pProd, dlink_Dgs3700Series=dlink_Dgs3700Series, dlink_Dgs3700SeriesProd=dlink_Dgs3700SeriesProd, dgs3710=dgs3710, dgs3712g=dgs3712g, dgs3700=dgs3700, dgs3712c=dgs3712c, dgs3712=dgs3712)
