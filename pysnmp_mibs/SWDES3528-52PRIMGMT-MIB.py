#
# PySNMP MIB module SWDES3528-52PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SWDES3528-52PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:43 2025
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
dlink_Des3500Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105)).setLabel("dlink-Des3500Series")
des3528 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 1))
des3528p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 2))
des3552 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 3))
des3552p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 4))
des3528dc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 5))
dlink_Des3500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105)).setLabel("dlink-Des3500SeriesProd")
des3528Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 1))
des3528pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 2))
des3552Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 3))
des3552pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 4))
des3528dcProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 5))
mibBuilder.exportSymbols("SWDES3528-52PRIMGMT-MIB", des3552pProd=des3552pProd, dlink_Des3500Series=dlink_Des3500Series, des3528p=des3528p, des3552=des3552, des3528dc=des3528dc, des3528Prod=des3528Prod, des3552Prod=des3552Prod, des3552p=des3552p, des3528=des3528, des3528pProd=des3528pProd, dlink_Des3500SeriesProd=dlink_Des3500SeriesProd, des3528dcProd=des3528dcProd)
