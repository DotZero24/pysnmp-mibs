#
# PySNMP MIB module SWDGS3620PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SWDGS3620PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:07 2025
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
dlink_Dgs3620Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 118)).setLabel("dlink-Dgs3620Prod")
dlink_Dgs3620Prod_Dgs3620_28TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 118, 1)).setLabel("dlink-Dgs3620Prod-Dgs3620-28TC")
dlink_Dgs3620Prod_Dgs3620_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 118, 2)).setLabel("dlink-Dgs3620Prod-Dgs3620-28SC")
dlink_Dgs3620Prod_Dgs3620_28PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 118, 3)).setLabel("dlink-Dgs3620Prod-Dgs3620-28PC")
dlink_Dgs3620Prod_Dgs3620_52T = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 118, 4)).setLabel("dlink-Dgs3620Prod-Dgs3620-52T")
dlink_Dgs3620Prod_Dgs3620_52P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 118, 5)).setLabel("dlink-Dgs3620Prod-Dgs3620-52P")
dlink_Dgs3620Prod_Dgs3620_28TC_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 118, 8)).setLabel("dlink-Dgs3620Prod-Dgs3620-28TC-DC")
dlink_Dgs3620Prod_Dgs3620_28SC_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 118, 9)).setLabel("dlink-Dgs3620Prod-Dgs3620-28SC-DC")
dlink_Dgs3620Proj = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118)).setLabel("dlink-Dgs3620Proj")
dlink_Dgs3620Proj_Dgs3620_28TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1)).setLabel("dlink-Dgs3620Proj-Dgs3620-28TC")
dlink_Dgs3620Proj_Dgs3620_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 2)).setLabel("dlink-Dgs3620Proj-Dgs3620-28SC")
dlink_Dgs3620Proj_Dgs3620_28PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 3)).setLabel("dlink-Dgs3620Proj-Dgs3620-28PC")
dlink_Dgs3620Proj_Dgs3620_52T = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 4)).setLabel("dlink-Dgs3620Proj-Dgs3620-52T")
dlink_Dgs3620Proj_Dgs3620_52P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 5)).setLabel("dlink-Dgs3620Proj-Dgs3620-52P")
dlink_Dgs3620Proj_Dgs3620_28TC_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 8)).setLabel("dlink-Dgs3620Proj-Dgs3620-28TC-DC")
dlink_Dgs3620Proj_Dgs3620_28SC_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 9)).setLabel("dlink-Dgs3620Proj-Dgs3620-28SC-DC")
mibBuilder.exportSymbols("SWDGS3620PRIMGMT-MIB", dlink_Dgs3620Proj_Dgs3620_52T=dlink_Dgs3620Proj_Dgs3620_52T, dlink_Dgs3620Proj=dlink_Dgs3620Proj, dlink_Dgs3620Prod_Dgs3620_52P=dlink_Dgs3620Prod_Dgs3620_52P, dlink_Dgs3620Prod_Dgs3620_28TC=dlink_Dgs3620Prod_Dgs3620_28TC, dlink_Dgs3620Prod_Dgs3620_28SC_DC=dlink_Dgs3620Prod_Dgs3620_28SC_DC, dlink_Dgs3620Proj_Dgs3620_28TC=dlink_Dgs3620Proj_Dgs3620_28TC, dlink_Dgs3620Prod=dlink_Dgs3620Prod, dlink_Dgs3620Proj_Dgs3620_28SC_DC=dlink_Dgs3620Proj_Dgs3620_28SC_DC, dlink_Dgs3620Proj_Dgs3620_28PC=dlink_Dgs3620Proj_Dgs3620_28PC, dlink_Dgs3620Proj_Dgs3620_28TC_DC=dlink_Dgs3620Proj_Dgs3620_28TC_DC, dlink_Dgs3620Prod_Dgs3620_28PC=dlink_Dgs3620Prod_Dgs3620_28PC, dlink_Dgs3620Prod_Dgs3620_28SC=dlink_Dgs3620Prod_Dgs3620_28SC, dlink_Dgs3620Prod_Dgs3620_28TC_DC=dlink_Dgs3620Prod_Dgs3620_28TC_DC, dlink_Dgs3620Proj_Dgs3620_28SC=dlink_Dgs3620Proj_Dgs3620_28SC, dlink_Dgs3620Prod_Dgs3620_52T=dlink_Dgs3620Prod_Dgs3620_52T, dlink_Dgs3620Proj_Dgs3620_52P=dlink_Dgs3620Proj_Dgs3620_52P)
