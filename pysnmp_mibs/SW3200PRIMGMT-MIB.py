#
# PySNMP MIB module SW3200PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SW3200PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:45 2025
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
dlink_Dgs3200Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101)).setLabel("dlink-Dgs3200Series")
dgs3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 1))
dgs3216 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 2))
dgs3224 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 3))
dlink_Dgs3200SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101)).setLabel("dlink-Dgs3200SeriesProd")
dgs3200_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 1)).setLabel("dgs3200-Prod")
dgs3216_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 2)).setLabel("dgs3216-Prod")
dgs3224_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 3)).setLabel("dgs3224-Prod")
mibBuilder.exportSymbols("SW3200PRIMGMT-MIB", dlink_Dgs3200SeriesProd=dlink_Dgs3200SeriesProd, dgs3216_Prod=dgs3216_Prod, dlink_Dgs3200Series=dlink_Dgs3200Series, dgs3200_Prod=dgs3200_Prod, dgs3224_Prod=dgs3224_Prod, dgs3216=dgs3216, dgs3200=dgs3200, dgs3224=dgs3224)
