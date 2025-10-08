#
# PySNMP MIB module SW36XXPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SW36XXPRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:34 2025
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
dlink_ProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70)).setLabel("dlink-ProjectXStackIISeriesProd")
dlink_Dgs3650 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 5)).setLabel("dlink-Dgs3650")
dlink_Dgs3627 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 6)).setLabel("dlink-Dgs3627")
dlink_Dgs3627g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 8)).setLabel("dlink-Dgs3627g")
dlink_Dgs3612g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 9)).setLabel("dlink-Dgs3612g")
dlink_Dgs3612 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 10)).setLabel("dlink-Dgs3612")
dgsProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70))
dgs3650 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 5))
dgs3627 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 6))
dgs3627g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 8))
dgs3612g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 9))
dgs3612 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 10))
mibBuilder.exportSymbols("SW36XXPRIMGMT-MIB", dgs3612=dgs3612, dgs3612g=dgs3612g, dlink_Dgs3650=dlink_Dgs3650, dlink_ProjectXStackIISeriesProd=dlink_ProjectXStackIISeriesProd, dgsProjectXStackIISeriesProd=dgsProjectXStackIISeriesProd, dlink_Dgs3627g=dlink_Dgs3627g, dgs3627=dgs3627, dlink_Dgs3612g=dlink_Dgs3612g, dgs3627g=dgs3627g, dlink_Dgs3612=dlink_Dgs3612, dlink_Dgs3627=dlink_Dgs3627, dgs3650=dgs3650)
