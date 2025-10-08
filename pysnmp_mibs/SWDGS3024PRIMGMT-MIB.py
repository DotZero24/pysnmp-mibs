#
# PySNMP MIB module SWDGS3024PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SWDGS3024PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:25 2025
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
dgs_3024SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68)).setLabel("dgs-3024SeriesProd")
dgs_3024 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68, 1)).setLabel("dgs-3024")
dgs_3024SeriesProd_Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68)).setLabel("dgs-3024SeriesProd-Mgmt")
dgs_3024Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68, 1)).setLabel("dgs-3024Mgmt")
mibBuilder.exportSymbols("SWDGS3024PRIMGMT-MIB", dgs_3024Mgmt=dgs_3024Mgmt, dgs_3024=dgs_3024, dgs_3024SeriesProd_Mgmt=dgs_3024SeriesProd_Mgmt, dgs_3024SeriesProd=dgs_3024SeriesProd)
