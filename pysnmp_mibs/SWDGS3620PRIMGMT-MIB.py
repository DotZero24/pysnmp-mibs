#
# PySNMP MIB module SWDGS3620PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SWDGS3620PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:06 2025
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
mibBuilder.exportSymbols("SWDGS3620PRIMGMT-MIB", dlink_Dgs3620Prod_Dgs3620_52T=dlink_Dgs3620Prod_Dgs3620_52T, dlink_Dgs3620Proj_Dgs3620_28PC=dlink_Dgs3620Proj_Dgs3620_28PC, dlink_Dgs3620Proj_Dgs3620_52T=dlink_Dgs3620Proj_Dgs3620_52T, dlink_Dgs3620Prod_Dgs3620_28TC_DC=dlink_Dgs3620Prod_Dgs3620_28TC_DC, dlink_Dgs3620Prod=dlink_Dgs3620Prod, dlink_Dgs3620Proj=dlink_Dgs3620Proj, dlink_Dgs3620Proj_Dgs3620_28SC_DC=dlink_Dgs3620Proj_Dgs3620_28SC_DC, dlink_Dgs3620Prod_Dgs3620_28SC=dlink_Dgs3620Prod_Dgs3620_28SC, dlink_Dgs3620Prod_Dgs3620_28PC=dlink_Dgs3620Prod_Dgs3620_28PC, dlink_Dgs3620Proj_Dgs3620_52P=dlink_Dgs3620Proj_Dgs3620_52P, dlink_Dgs3620Prod_Dgs3620_52P=dlink_Dgs3620Prod_Dgs3620_52P, dlink_Dgs3620Proj_Dgs3620_28SC=dlink_Dgs3620Proj_Dgs3620_28SC, dlink_Dgs3620Prod_Dgs3620_28SC_DC=dlink_Dgs3620Prod_Dgs3620_28SC_DC, dlink_Dgs3620Proj_Dgs3620_28TC=dlink_Dgs3620Proj_Dgs3620_28TC, dlink_Dgs3620Prod_Dgs3620_28TC=dlink_Dgs3620Prod_Dgs3620_28TC, dlink_Dgs3620Proj_Dgs3620_28TC_DC=dlink_Dgs3620Proj_Dgs3620_28TC_DC)
