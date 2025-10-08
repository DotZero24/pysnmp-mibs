#
# PySNMP MIB module SW34XXPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SW34XXPRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:33 2025
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
dlink_Dgs3426 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 1)).setLabel("dlink-Dgs3426")
dlink_Dgs3427 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 2)).setLabel("dlink-Dgs3427")
dlink_Dgs3450 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 3)).setLabel("dlink-Dgs3450")
dlink_Dgs3426p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 7)).setLabel("dlink-Dgs3426p")
dgsProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70))
dgs3426 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 1))
dgs3427 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 2))
dgs3450 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 3))
dgs3426p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 7))
mibBuilder.exportSymbols("SW34XXPRIMGMT-MIB", dlink_Dgs3426p=dlink_Dgs3426p, dlink_Dgs3427=dlink_Dgs3427, dgsProjectXStackIISeriesProd=dgsProjectXStackIISeriesProd, dgs3426=dgs3426, dlink_ProjectXStackIISeriesProd=dlink_ProjectXStackIISeriesProd, dlink_Dgs3426=dlink_Dgs3426, dgs3450=dgs3450, dgs3427=dgs3427, dlink_Dgs3450=dlink_Dgs3450, dgs3426p=dgs3426p)
