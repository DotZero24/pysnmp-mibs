#
# PySNMP MIB module SW3x12SRPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SW3x12SRPRIMGMT-MIB
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
dlink_Dgs3x12SRSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 55)).setLabel("dlink-Dgs3x12SRSeriesProd")
dlink_Dgs3212SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 55, 1)).setLabel("dlink-Dgs3212SR")
dlink_Dgs3312SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 55, 2)).setLabel("dlink-Dgs3312SR")
dgs3x12SRSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 55))
dgs3212SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 55, 1))
dgs3312SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 55, 2))
mibBuilder.exportSymbols("SW3x12SRPRIMGMT-MIB", dgs3x12SRSeriesProd=dgs3x12SRSeriesProd, dgs3312SR=dgs3312SR, dlink_Dgs3x12SRSeriesProd=dlink_Dgs3x12SRSeriesProd, dlink_Dgs3312SR=dlink_Dgs3312SR, dgs3212SR=dgs3212SR, dlink_Dgs3212SR=dlink_Dgs3212SR)
