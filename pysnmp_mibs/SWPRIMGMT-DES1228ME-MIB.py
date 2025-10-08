#
# PySNMP MIB module SWPRIMGMT-DES1228ME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SWPRIMGMT-DES1228ME-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:59 2025
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
dlink_des1228MEproductProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116)).setLabel("dlink-des1228MEproductProd")
dlink_des1228MEProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116, 1)).setLabel("dlink-des1228MEProd")
dlink_des1228MEv2Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116, 2)).setLabel("dlink-des1228MEv2Prod")
des1228MESeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116))
des1228ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116, 1))
des1228MEv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116, 2))
mibBuilder.exportSymbols("SWPRIMGMT-DES1228ME-MIB", dlink_des1228MEv2Prod=dlink_des1228MEv2Prod, dlink_des1228MEproductProd=dlink_des1228MEproductProd, des1228MESeriesProd=des1228MESeriesProd, dlink_des1228MEProd=dlink_des1228MEProd, des1228ME=des1228ME, des1228MEv2=des1228MEv2)
