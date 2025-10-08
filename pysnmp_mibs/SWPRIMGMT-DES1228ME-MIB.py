#
# PySNMP MIB module SWPRIMGMT-DES1228ME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SWPRIMGMT-DES1228ME-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:59 2025
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
dlink_des1228MEproductProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116)).setLabel("dlink-des1228MEproductProd")
dlink_des1228MEProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116, 1)).setLabel("dlink-des1228MEProd")
dlink_des1228MEv2Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116, 2)).setLabel("dlink-des1228MEv2Prod")
des1228MESeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116))
des1228ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116, 1))
des1228MEv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116, 2))
mibBuilder.exportSymbols("SWPRIMGMT-DES1228ME-MIB", des1228MESeriesProd=des1228MESeriesProd, dlink_des1228MEProd=dlink_des1228MEProd, dlink_des1228MEv2Prod=dlink_des1228MEv2Prod, dlink_des1228MEproductProd=dlink_des1228MEproductProd, des1228MEv2=des1228MEv2, des1228ME=des1228ME)
