#
# PySNMP MIB module SW3500PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SW3500PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:49 2025
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
dlink_des3500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 64)).setLabel("dlink-des3500SeriesProd")
dlink_des3526Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 64, 1)).setLabel("dlink-des3526Prod")
dlink_des3550Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 64, 2)).setLabel("dlink-des3550Prod")
des3500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 64))
des3526 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 64, 1))
des3550 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 64, 2))
mibBuilder.exportSymbols("SW3500PRIMGMT-MIB", des3550=des3550, des3500SeriesProd=des3500SeriesProd, des3526=des3526, dlink_des3500SeriesProd=dlink_des3500SeriesProd, dlink_des3550Prod=dlink_des3550Prod, dlink_des3526Prod=dlink_des3526Prod)
