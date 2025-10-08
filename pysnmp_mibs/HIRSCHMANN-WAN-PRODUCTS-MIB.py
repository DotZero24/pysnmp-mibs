#
# PySNMP MIB module HIRSCHMANN-WAN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WAN-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:55:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hmWanMgmt, = mibBuilder.importSymbols("HIRSCHMANN-WAN-MIB", "hmWanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmWanProductsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 40, 1, 1))
hmWanProductsMib.setRevisions(('2016-08-09 00:00',))
if mibBuilder.loadTexts: hmWanProductsMib.setLastUpdated('201608090000Z')
if mibBuilder.loadTexts: hmWanProductsMib.setOrganization('Hirschmann Automation and Control GmbH')
owl_3g = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 40, 1, 1, 1)).setLabel("owl-3g")
owl_LTE = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 40, 1, 1, 2)).setLabel("owl-LTE")
owl_LTE_M12 = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 40, 1, 1, 3)).setLabel("owl-LTE-M12")
mibBuilder.exportSymbols("HIRSCHMANN-WAN-PRODUCTS-MIB", PYSNMP_MODULE_ID=hmWanProductsMib, owl_LTE_M12=owl_LTE_M12, owl_LTE=owl_LTE, hmWanProductsMib=hmWanProductsMib, owl_3g=owl_3g)
