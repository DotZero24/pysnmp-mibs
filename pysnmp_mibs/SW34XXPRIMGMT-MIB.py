#
# PySNMP MIB module SW34XXPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SW34XXPRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:44 2025
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
dlink_Dgs3426 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 1)).setLabel("dlink-Dgs3426")
dlink_Dgs3427 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 2)).setLabel("dlink-Dgs3427")
dlink_Dgs3450 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 3)).setLabel("dlink-Dgs3450")
dlink_Dgs3426p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 7)).setLabel("dlink-Dgs3426p")
dgsProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70))
dgs3426 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 1))
dgs3427 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 2))
dgs3450 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 3))
dgs3426p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 7))
mibBuilder.exportSymbols("SW34XXPRIMGMT-MIB", dlink_Dgs3427=dlink_Dgs3427, dlink_Dgs3450=dlink_Dgs3450, dgs3450=dgs3450, dlink_ProjectXStackIISeriesProd=dlink_ProjectXStackIISeriesProd, dgsProjectXStackIISeriesProd=dgsProjectXStackIISeriesProd, dgs3427=dgs3427, dgs3426p=dgs3426p, dlink_Dgs3426=dlink_Dgs3426, dlink_Dgs3426p=dlink_Dgs3426p, dgs3426=dgs3426)
