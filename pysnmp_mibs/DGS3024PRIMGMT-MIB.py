#
# PySNMP MIB module DGS3024PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DGS3024PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:58 2025
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
dgs_3024SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68)).setLabel("dgs-3024SeriesProd")
dgs_3024 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68, 1)).setLabel("dgs-3024")
dgs_3024SeriesProd_Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68)).setLabel("dgs-3024SeriesProd-Mgmt")
dgs_3024Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68, 1)).setLabel("dgs-3024Mgmt")
mibBuilder.exportSymbols("DGS3024PRIMGMT-MIB", dgs_3024SeriesProd_Mgmt=dgs_3024SeriesProd_Mgmt, dgs_3024SeriesProd=dgs_3024SeriesProd, dgs_3024Mgmt=dgs_3024Mgmt, dgs_3024=dgs_3024)
