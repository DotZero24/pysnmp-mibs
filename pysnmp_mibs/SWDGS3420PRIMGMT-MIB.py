#
# PySNMP MIB module SWDGS3420PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SWDGS3420PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:31 2025
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
dlink_Dgs3420Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119)).setLabel("dlink-Dgs3420Prod")
dlink_Dgs3420Prod_Dgs3420_28TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 1)).setLabel("dlink-Dgs3420Prod-Dgs3420-28TC")
dlink_Dgs3420Prod_Dgs3420_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 2)).setLabel("dlink-Dgs3420Prod-Dgs3420-28SC")
dlink_Dgs3420Prod_Dgs3420_28PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 3)).setLabel("dlink-Dgs3420Prod-Dgs3420-28PC")
dlink_Dgs3420Prod_Dgs3420_52T = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 4)).setLabel("dlink-Dgs3420Prod-Dgs3420-52T")
dlink_Dgs3420Prod_Dgs3420_52P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 5)).setLabel("dlink-Dgs3420Prod-Dgs3420-52P")
dlink_Dgs3420Prod_Dgs3420_26SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 6)).setLabel("dlink-Dgs3420Prod-Dgs3420-26SC")
dlink_Dgs3420Proj = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119)).setLabel("dlink-Dgs3420Proj")
dlink_Dgs3420Proj_Dgs3420_28TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 1)).setLabel("dlink-Dgs3420Proj-Dgs3420-28TC")
dlink_Dgs3420Proj_Dgs3420_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 2)).setLabel("dlink-Dgs3420Proj-Dgs3420-28SC")
dlink_Dgs3420Proj_Dgs3420_28PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 3)).setLabel("dlink-Dgs3420Proj-Dgs3420-28PC")
dlink_Dgs3420Proj_Dgs3420_52T = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 4)).setLabel("dlink-Dgs3420Proj-Dgs3420-52T")
dlink_Dgs3420Proj_Dgs3420_52P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 5)).setLabel("dlink-Dgs3420Proj-Dgs3420-52P")
dlink_Dgs3420Proj_Dgs3420_26SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 6)).setLabel("dlink-Dgs3420Proj-Dgs3420-26SC")
mibBuilder.exportSymbols("SWDGS3420PRIMGMT-MIB", dlink_Dgs3420Proj_Dgs3420_28SC=dlink_Dgs3420Proj_Dgs3420_28SC, dlink_Dgs3420Proj=dlink_Dgs3420Proj, dlink_Dgs3420Prod_Dgs3420_28SC=dlink_Dgs3420Prod_Dgs3420_28SC, dlink_Dgs3420Prod_Dgs3420_28TC=dlink_Dgs3420Prod_Dgs3420_28TC, dlink_Dgs3420Prod_Dgs3420_52T=dlink_Dgs3420Prod_Dgs3420_52T, dlink_Dgs3420Prod_Dgs3420_26SC=dlink_Dgs3420Prod_Dgs3420_26SC, dlink_Dgs3420Proj_Dgs3420_28TC=dlink_Dgs3420Proj_Dgs3420_28TC, dlink_Dgs3420Prod=dlink_Dgs3420Prod, dlink_Dgs3420Prod_Dgs3420_28PC=dlink_Dgs3420Prod_Dgs3420_28PC, dlink_Dgs3420Proj_Dgs3420_52T=dlink_Dgs3420Proj_Dgs3420_52T, dlink_Dgs3420Prod_Dgs3420_52P=dlink_Dgs3420Prod_Dgs3420_52P, dlink_Dgs3420Proj_Dgs3420_52P=dlink_Dgs3420Proj_Dgs3420_52P, dlink_Dgs3420Proj_Dgs3420_28PC=dlink_Dgs3420Proj_Dgs3420_28PC, dlink_Dgs3420Proj_Dgs3420_26SC=dlink_Dgs3420Proj_Dgs3420_26SC)
