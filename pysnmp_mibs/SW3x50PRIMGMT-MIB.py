#
# PySNMP MIB module SW3x50PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SW3x50PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:16 2025
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
dlink_Des3x50SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52)).setLabel("dlink-Des3x50SeriesProd")
dlink_Des3x50Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 1)).setLabel("dlink-Des3x50Prod")
dlink_Des3x50Prod_Des3250 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 1, 1)).setLabel("dlink-Des3x50Prod-Des3250")
dlink_Des3x50Prod_Des3350 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 1, 2)).setLabel("dlink-Des3x50Prod-Des3350")
dlink_Des3x50Prod_Des3550 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 1, 3)).setLabel("dlink-Des3x50Prod-Des3550")
des3x50DevRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 2))
des3x50Device = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 2, 1))
des3x50UnitRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 3))
des3x50Unit = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 3, 1))
des3x50ModuleRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 4))
des3x50_Module_Mainboard_48Port = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 4, 1)).setLabel("des3x50-Module-Mainboard-48Port")
des3x50_Module_1_Port_GBIC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 4, 2)).setLabel("des3x50-Module-1-Port-GBIC")
des3x50PortRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 5))
des3x50_Port_10_100_TX = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 5, 1)).setLabel("des3x50-Port-10-100-TX")
des3x50_Port_1000_SX_GBIC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 5, 2)).setLabel("des3x50-Port-1000-SX-GBIC")
des3x50_Port_1000_LX_GBIC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 5, 3)).setLabel("des3x50-Port-1000-LX-GBIC")
des3x50_Port_1000_TX = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 5, 4)).setLabel("des3x50-Port-1000-TX")
des3x50SlotRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 6))
des3x50Slot1 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 52, 6, 1))
mibBuilder.exportSymbols("SW3x50PRIMGMT-MIB", dlink_Des3x50Prod=dlink_Des3x50Prod, dlink_Des3x50Prod_Des3550=dlink_Des3x50Prod_Des3550, dlink_Des3x50SeriesProd=dlink_Des3x50SeriesProd, des3x50PortRegistration=des3x50PortRegistration, des3x50_Port_1000_LX_GBIC=des3x50_Port_1000_LX_GBIC, des3x50_Port_10_100_TX=des3x50_Port_10_100_TX, dlink_Des3x50Prod_Des3250=dlink_Des3x50Prod_Des3250, des3x50UnitRegistration=des3x50UnitRegistration, des3x50SlotRegistration=des3x50SlotRegistration, dlink_Des3x50Prod_Des3350=dlink_Des3x50Prod_Des3350, des3x50_Module_1_Port_GBIC=des3x50_Module_1_Port_GBIC, des3x50Slot1=des3x50Slot1, des3x50_Port_1000_TX=des3x50_Port_1000_TX, des3x50ModuleRegistration=des3x50ModuleRegistration, des3x50Device=des3x50Device, des3x50Unit=des3x50Unit, des3x50_Module_Mainboard_48Port=des3x50_Module_Mainboard_48Port, des3x50_Port_1000_SX_GBIC=des3x50_Port_1000_SX_GBIC, des3x50DevRegistration=des3x50DevRegistration)
