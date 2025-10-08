#
# PySNMP MIB module SW36XXPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SW36XXPRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:26 2025
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
mibBuilder.exportSymbols("SW36XXPRIMGMT-MIB", dlink_Dgs3627g=dlink_Dgs3627g, dgs3612g=dgs3612g, dgsProjectXStackIISeriesProd=dgsProjectXStackIISeriesProd, dlink_Dgs3650=dlink_Dgs3650, dlink_ProjectXStackIISeriesProd=dlink_ProjectXStackIISeriesProd, dlink_Dgs3612=dlink_Dgs3612, dgs3627=dgs3627, dgs3612=dgs3612, dgs3650=dgs3650, dgs3627g=dgs3627g, dlink_Dgs3627=dlink_Dgs3627, dlink_Dgs3612g=dlink_Dgs3612g)
