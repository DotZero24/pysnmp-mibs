#
# PySNMP MIB module DGS1100PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DGS1100PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:28 2025
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
mibBuilder.exportSymbols("DGS1100PRIMGMT-MIB", dgs1100_18ME=dgs1100_18ME, dgs1100SeriesProd=dgs1100SeriesProd, dgs1100_26=dgs1100_26, dgs1100_16ME=dgs1100_16ME, dgs1100_24=dgs1100_24, dgs1100_24P=dgs1100_24P, dgs1100_16=dgs1100_16, dgs1100_24ME=dgs1100_24ME, dgs1100_24PME=dgs1100_24PME, dgs1100_18=dgs1100_18, dgs1100_26ME=dgs1100_26ME)
