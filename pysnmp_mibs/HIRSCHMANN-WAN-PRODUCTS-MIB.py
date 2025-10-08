#
# PySNMP MIB module HIRSCHMANN-WAN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WAN-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hmWanMgmt, = mibBuilder.importSymbols("HIRSCHMANN-WAN-MIB", "hmWanMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hmWanProductsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 40, 1, 1))
hmWanProductsMib.setRevisions(('2016-08-09 00:00',))
if mibBuilder.loadTexts: hmWanProductsMib.setLastUpdated('201608090000Z')
if mibBuilder.loadTexts: hmWanProductsMib.setOrganization('Hirschmann Automation and Control GmbH')
owl_3g = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 40, 1, 1, 1)).setLabel("owl-3g")
owl_LTE = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 40, 1, 1, 2)).setLabel("owl-LTE")
owl_LTE_M12 = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 40, 1, 1, 3)).setLabel("owl-LTE-M12")
mibBuilder.exportSymbols("HIRSCHMANN-WAN-PRODUCTS-MIB", PYSNMP_MODULE_ID=hmWanProductsMib, owl_3g=owl_3g, hmWanProductsMib=hmWanProductsMib, owl_LTE=owl_LTE, owl_LTE_M12=owl_LTE_M12)
