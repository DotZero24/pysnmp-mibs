#
# PySNMP MIB module SW3800PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SW3800PRIMGMT-MIB
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
dlink_des3800SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69)).setLabel("dlink-des3800SeriesProd")
dlink_des3828Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 1)).setLabel("dlink-des3828Prod")
dlink_des3828DCProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 2)).setLabel("dlink-des3828DCProd")
dlink_des3828PProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 3)).setLabel("dlink-des3828PProd")
dlink_des3852Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 4)).setLabel("dlink-des3852Prod")
dlink_des3852PProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 5)).setLabel("dlink-des3852PProd")
des3800SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69))
des3828 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 1))
des3828DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 2))
des3828P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 3))
des3852 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 4))
des3852P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 5))
mibBuilder.exportSymbols("SW3800PRIMGMT-MIB", des3828P=des3828P, dlink_des3852Prod=dlink_des3852Prod, des3852=des3852, dlink_des3800SeriesProd=dlink_des3800SeriesProd, dlink_des3828PProd=dlink_des3828PProd, dlink_des3852PProd=dlink_des3852PProd, des3828=des3828, des3852P=des3852P, des3800SeriesProd=des3800SeriesProd, dlink_des3828DCProd=dlink_des3828DCProd, dlink_des3828Prod=dlink_des3828Prod, des3828DC=des3828DC)
