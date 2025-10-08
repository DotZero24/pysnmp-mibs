#
# PySNMP MIB module SWPRIMGMT-DGS3000-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SWPRIMGMT-DGS3000-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:00 2025
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
dlink_dgs3000SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133)).setLabel("dlink-dgs3000SeriesProd")
dgs_3000_10tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 1)).setLabel("dgs-3000-10tc")
dgs_3000_26tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 2)).setLabel("dgs-3000-26tc")
dgs_3000_24tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 4)).setLabel("dgs-3000-24tc")
dgs_3000_10_tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 1, 1)).setLabel("dgs-3000-10-tc")
dgs_3000_26_tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 2, 1)).setLabel("dgs-3000-26-tc")
dgs_3000_24_tcax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 4, 1)).setLabel("dgs-3000-24-tcax")
dgs3000SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133))
dgs3000_10tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 1)).setLabel("dgs3000-10tc")
dgs3000_26tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 2)).setLabel("dgs3000-26tc")
dgs3000_24tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 4)).setLabel("dgs3000-24tc")
dgs3000_10_tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 1, 1)).setLabel("dgs3000-10-tc")
dgs3000_26_tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 2, 1)).setLabel("dgs3000-26-tc")
dgs3000_24_tcax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 4, 1)).setLabel("dgs3000-24-tcax")
mibBuilder.exportSymbols("SWPRIMGMT-DGS3000-MIB", dgs3000_10_tc=dgs3000_10_tc, dgs_3000_26tc=dgs_3000_26tc, dlink_dgs3000SeriesProd=dlink_dgs3000SeriesProd, dgs_3000_10tc=dgs_3000_10tc, dgs_3000_24tc=dgs_3000_24tc, dgs_3000_24_tcax=dgs_3000_24_tcax, dgs3000_10tc=dgs3000_10tc, dgs_3000_26_tc=dgs_3000_26_tc, dgs3000_26_tc=dgs3000_26_tc, dgs3000_24_tcax=dgs3000_24_tcax, dgs_3000_10_tc=dgs_3000_10_tc, dgs3000_24tc=dgs3000_24tc, dgs3000SeriesProd=dgs3000SeriesProd, dgs3000_26tc=dgs3000_26tc)
