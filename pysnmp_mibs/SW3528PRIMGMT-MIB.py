#
# PySNMP MIB module SW3528PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SW3528PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:17 2025
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
dlink_Des3528Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105)).setLabel("dlink-Des3528Series")
des3528 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 1))
des3528p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 2))
des3552 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 3))
des3552p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 4))
des3528dc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 5))
dlink_Des3528SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105)).setLabel("dlink-Des3528SeriesProd")
des3528Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 1))
des3528pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 2))
des3552Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 3))
des3552pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 4))
des3528dcProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 5))
mibBuilder.exportSymbols("SW3528PRIMGMT-MIB", des3552p=des3552p, des3528dc=des3528dc, des3552=des3552, des3528p=des3528p, dlink_Des3528Series=dlink_Des3528Series, des3528dcProd=des3528dcProd, des3552Prod=des3552Prod, dlink_Des3528SeriesProd=dlink_Des3528SeriesProd, des3528=des3528, des3552pProd=des3552pProd, des3528Prod=des3528Prod, des3528pProd=des3528pProd)
