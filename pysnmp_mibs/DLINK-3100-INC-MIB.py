#
# PySNMP MIB module DLINK-3100-INC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINK-3100-INC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 171))
dlink_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10)).setLabel("dlink-products")
dlink_Dgs3100SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94)).setLabel("dlink-Dgs3100SeriesProd")
dgs3124_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 1)).setLabel("dgs3124-Prod")
dgs3124p_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 2)).setLabel("dgs3124p-Prod")
dgs3148_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 3)).setLabel("dgs3148-Prod")
dgs3148p_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 4)).setLabel("dgs3148p-Prod")
dgs3124tg_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 5)).setLabel("dgs3124tg-Prod")
dgs3100_SWL2MGMT_MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89)).setLabel("dgs3100-SWL2MGMT-MIB")
rnd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89))
mibBuilder.exportSymbols("DLINK-3100-INC-MIB", dlink_Dgs3100SeriesProd=dlink_Dgs3100SeriesProd, dgs3100_SWL2MGMT_MIB=dgs3100_SWL2MGMT_MIB, dgs3148_Prod=dgs3148_Prod, dlink_products=dlink_products, dgs3124p_Prod=dgs3124p_Prod, dgs3124tg_Prod=dgs3124tg_Prod, dlink=dlink, dgs3148p_Prod=dgs3148p_Prod, rnd=rnd, dgs3124_Prod=dgs3124_Prod)
