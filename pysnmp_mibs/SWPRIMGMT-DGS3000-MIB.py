#
# PySNMP MIB module SWPRIMGMT-DGS3000-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SWPRIMGMT-DGS3000-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:01 2025
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
mibBuilder.exportSymbols("SWPRIMGMT-DGS3000-MIB", dgs3000_26_tc=dgs3000_26_tc, dgs_3000_10_tc=dgs_3000_10_tc, dgs3000_10_tc=dgs3000_10_tc, dgs_3000_24_tcax=dgs_3000_24_tcax, dgs_3000_26_tc=dgs_3000_26_tc, dgs3000_24_tcax=dgs3000_24_tcax, dgs_3000_24tc=dgs_3000_24tc, dgs3000SeriesProd=dgs3000SeriesProd, dgs_3000_26tc=dgs_3000_26tc, dgs3000_26tc=dgs3000_26tc, dgs3000_24tc=dgs3000_24tc, dgs_3000_10tc=dgs_3000_10tc, dlink_dgs3000SeriesProd=dlink_dgs3000SeriesProd, dgs3000_10tc=dgs3000_10tc)
