#
# PySNMP MIB module DGS1100PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DGS1100PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:37 2025
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
dgs1100SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134))
dgs1100_16 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 3)).setLabel("dgs1100-16")
dgs1100_16ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 4)).setLabel("dgs1100-16ME")
dgs1100_18 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 5)).setLabel("dgs1100-18")
dgs1100_18ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 6)).setLabel("dgs1100-18ME")
dgs1100_24 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 7)).setLabel("dgs1100-24")
dgs1100_24ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 8)).setLabel("dgs1100-24ME")
dgs1100_24P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 9)).setLabel("dgs1100-24P")
dgs1100_24PME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 10)).setLabel("dgs1100-24PME")
dgs1100_26 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 11)).setLabel("dgs1100-26")
dgs1100_26ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 12)).setLabel("dgs1100-26ME")
mibBuilder.exportSymbols("DGS1100PRIMGMT-MIB", dgs1100SeriesProd=dgs1100SeriesProd, dgs1100_24=dgs1100_24, dgs1100_26ME=dgs1100_26ME, dgs1100_24PME=dgs1100_24PME, dgs1100_16=dgs1100_16, dgs1100_16ME=dgs1100_16ME, dgs1100_26=dgs1100_26, dgs1100_24ME=dgs1100_24ME, dgs1100_18ME=dgs1100_18ME, dgs1100_18=dgs1100_18, dgs1100_24P=dgs1100_24P)
