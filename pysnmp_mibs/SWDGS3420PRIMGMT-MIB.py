#
# PySNMP MIB module SWDGS3420PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SWDGS3420PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:42 2025
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
mibBuilder.exportSymbols("SWDGS3420PRIMGMT-MIB", dlink_Dgs3420Prod_Dgs3420_28PC=dlink_Dgs3420Prod_Dgs3420_28PC, dlink_Dgs3420Prod_Dgs3420_28TC=dlink_Dgs3420Prod_Dgs3420_28TC, dlink_Dgs3420Proj_Dgs3420_26SC=dlink_Dgs3420Proj_Dgs3420_26SC, dlink_Dgs3420Proj_Dgs3420_52T=dlink_Dgs3420Proj_Dgs3420_52T, dlink_Dgs3420Proj=dlink_Dgs3420Proj, dlink_Dgs3420Proj_Dgs3420_52P=dlink_Dgs3420Proj_Dgs3420_52P, dlink_Dgs3420Prod_Dgs3420_52P=dlink_Dgs3420Prod_Dgs3420_52P, dlink_Dgs3420Prod_Dgs3420_26SC=dlink_Dgs3420Prod_Dgs3420_26SC, dlink_Dgs3420Proj_Dgs3420_28PC=dlink_Dgs3420Proj_Dgs3420_28PC, dlink_Dgs3420Prod_Dgs3420_28SC=dlink_Dgs3420Prod_Dgs3420_28SC, dlink_Dgs3420Prod_Dgs3420_52T=dlink_Dgs3420Prod_Dgs3420_52T, dlink_Dgs3420Proj_Dgs3420_28TC=dlink_Dgs3420Proj_Dgs3420_28TC, dlink_Dgs3420Prod=dlink_Dgs3420Prod, dlink_Dgs3420Proj_Dgs3420_28SC=dlink_Dgs3420Proj_Dgs3420_28SC)
