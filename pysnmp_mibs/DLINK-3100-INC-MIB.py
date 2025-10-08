#
# PySNMP MIB module DLINK-3100-INC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINK-3100-INC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DLINK-3100-INC-MIB", dgs3148_Prod=dgs3148_Prod, dgs3124p_Prod=dgs3124p_Prod, dgs3148p_Prod=dgs3148p_Prod, rnd=rnd, dlink_products=dlink_products, dgs3100_SWL2MGMT_MIB=dgs3100_SWL2MGMT_MIB, dgs3124_Prod=dgs3124_Prod, dlink=dlink, dlink_Dgs3100SeriesProd=dlink_Dgs3100SeriesProd, dgs3124tg_Prod=dgs3124tg_Prod)
