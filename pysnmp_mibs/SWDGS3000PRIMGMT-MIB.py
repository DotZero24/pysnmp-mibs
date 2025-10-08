#
# PySNMP MIB module SWDGS3000PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SWDGS3000PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:41 2025
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
dlink_Dgs3000Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133)).setLabel("dlink-Dgs3000Prod")
dlink_Dgs3000Prod_DGS3000_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 5)).setLabel("dlink-Dgs3000Prod-DGS3000-28SC")
dlink_Dgs3000Prod_DGS3000_28SCax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 5, 1)).setLabel("dlink-Dgs3000Prod-DGS3000-28SCax")
dlink_Dgs3000Proj = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133)).setLabel("dlink-Dgs3000Proj")
dlink_Dgs3000Proj_DGS3000_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 5)).setLabel("dlink-Dgs3000Proj-DGS3000-28SC")
dlink_Dgs3000Proj_DGS3000_28SCax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1)).setLabel("dlink-Dgs3000Proj-DGS3000-28SCax")
mibBuilder.exportSymbols("SWDGS3000PRIMGMT-MIB", dlink_Dgs3000Proj_DGS3000_28SC=dlink_Dgs3000Proj_DGS3000_28SC, dlink_Dgs3000Prod_DGS3000_28SCax=dlink_Dgs3000Prod_DGS3000_28SCax, dlink_Dgs3000Prod=dlink_Dgs3000Prod, dlink_Dgs3000Proj_DGS3000_28SCax=dlink_Dgs3000Proj_DGS3000_28SCax, dlink_Dgs3000Proj=dlink_Dgs3000Proj, dlink_Dgs3000Prod_DGS3000_28SC=dlink_Dgs3000Prod_DGS3000_28SC)
