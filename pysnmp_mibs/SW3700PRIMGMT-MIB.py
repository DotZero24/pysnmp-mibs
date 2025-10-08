#
# PySNMP MIB module SW3700PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SW3700PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SW3700PRIMGMT-MIB", dlink_Dgs3700Series=dlink_Dgs3700Series, dgs3710s=dgs3710s, dgs3700=dgs3700, dlink_Dgs3700SeriesProd=dlink_Dgs3700SeriesProd, dgs3712=dgs3712, dgs3712Prod=dgs3712Prod, dgs3710=dgs3710, dgs3712g=dgs3712g, dgs3712c=dgs3712c, dgs3712pProd=dgs3712pProd)
