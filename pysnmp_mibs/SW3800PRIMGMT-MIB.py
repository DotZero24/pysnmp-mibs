#
# PySNMP MIB module SW3800PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SW3800PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:22 2025
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
mibBuilder.exportSymbols("SW3800PRIMGMT-MIB", des3828DC=des3828DC, dlink_des3852Prod=dlink_des3852Prod, des3800SeriesProd=des3800SeriesProd, dlink_des3852PProd=dlink_des3852PProd, des3828=des3828, dlink_des3828PProd=dlink_des3828PProd, dlink_des3800SeriesProd=dlink_des3800SeriesProd, des3828P=des3828P, dlink_des3828DCProd=dlink_des3828DCProd, dlink_des3828Prod=dlink_des3828Prod, des3852=des3852, des3852P=des3852P)
