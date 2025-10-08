#
# PySNMP MIB module DLINK-SWPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINK-SWPRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:22 2025
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
mibBuilder.exportSymbols("DLINK-SWPRIMGMT-MIB", des3016=des3016, des3010f=des3010f, des3010g=des3010g, des3010=des3010, des30xxSeriesProd=des30xxSeriesProd, dlink_des30xxproductProd=dlink_des30xxproductProd, dlink_des3010xProd=dlink_des3010xProd, dlink_des3010FLProd=dlink_des3010FLProd, des3018=des3018, dlink_des3010GProd=dlink_des3010GProd, dlink_des3026Prod=dlink_des3026Prod, dlink_des3016Prod=dlink_des3016Prod, des3010fl=des3010fl, dlink_des3018Prod=dlink_des3018Prod, dlink_des3010FProd=dlink_des3010FProd, des3026=des3026)
