#
# PySNMP MIB module DLINK-SWPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINK-SWPRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:28 2025
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
dlink_des30xxproductProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63)).setLabel("dlink-des30xxproductProd")
dlink_des3010xProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 1)).setLabel("dlink-des3010xProd")
dlink_des3010FProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 1, 1)).setLabel("dlink-des3010FProd")
dlink_des3010GProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 1, 2)).setLabel("dlink-des3010GProd")
dlink_des3018Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 2)).setLabel("dlink-des3018Prod")
dlink_des3026Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 3)).setLabel("dlink-des3026Prod")
dlink_des3010FLProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 4)).setLabel("dlink-des3010FLProd")
dlink_des3016Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 10)).setLabel("dlink-des3016Prod")
des30xxSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63))
des3010 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 1))
des3010f = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 1, 1))
des3010g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 1, 2))
des3018 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 2))
des3026 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 3))
des3010fl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 4))
des3016 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 10))
mibBuilder.exportSymbols("DLINK-SWPRIMGMT-MIB", des3018=des3018, dlink_des3010GProd=dlink_des3010GProd, dlink_des3010FLProd=dlink_des3010FLProd, des3026=des3026, dlink_des3026Prod=dlink_des3026Prod, des3010g=des3010g, dlink_des30xxproductProd=dlink_des30xxproductProd, des30xxSeriesProd=des30xxSeriesProd, des3016=des3016, des3010fl=des3010fl, dlink_des3010FProd=dlink_des3010FProd, des3010=des3010, des3010f=des3010f, dlink_des3018Prod=dlink_des3018Prod, dlink_des3010xProd=dlink_des3010xProd, dlink_des3016Prod=dlink_des3016Prod)
