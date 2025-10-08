#
# PySNMP MIB module SW3200PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SW3200PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:34 2025
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
dlink_Dgs3200Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101)).setLabel("dlink-Dgs3200Series")
dgs3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 1))
dgs3216 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 2))
dgs3224 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 3))
dlink_Dgs3200SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101)).setLabel("dlink-Dgs3200SeriesProd")
dgs3200_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 1)).setLabel("dgs3200-Prod")
dgs3216_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 2)).setLabel("dgs3216-Prod")
dgs3224_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 3)).setLabel("dgs3224-Prod")
mibBuilder.exportSymbols("SW3200PRIMGMT-MIB", dgs3216=dgs3216, dlink_Dgs3200Series=dlink_Dgs3200Series, dgs3200=dgs3200, dgs3216_Prod=dgs3216_Prod, dgs3200_Prod=dgs3200_Prod, dgs3224=dgs3224, dlink_Dgs3200SeriesProd=dlink_Dgs3200SeriesProd, dgs3224_Prod=dgs3224_Prod)
