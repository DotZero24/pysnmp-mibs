#
# PySNMP MIB module ZYXEL-PORT-BASED-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-PORT-BASED-VLAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelPortBasedVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63))
if mibBuilder.loadTexts: zyxelPortBasedVlan.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelPortBasedVlan.setOrganization('Enterprise Solution ZyXEL')
zyxelPortBasedVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1))
zyxelPortBasedVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1, 1), )
if mibBuilder.loadTexts: zyxelPortBasedVlanTable.setStatus('current')
zyxelPortBasedVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelPortBasedVlanEntry.setStatus('current')
zyPortBasedVlanPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1, 1, 1, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortBasedVlanPorts.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-PORT-BASED-VLAN-MIB", zyxelPortBasedVlanTable=zyxelPortBasedVlanTable, zyPortBasedVlanPorts=zyPortBasedVlanPorts, zyxelPortBasedVlanEntry=zyxelPortBasedVlanEntry, zyxelPortBasedVlanSetup=zyxelPortBasedVlanSetup, PYSNMP_MODULE_ID=zyxelPortBasedVlan, zyxelPortBasedVlan=zyxelPortBasedVlan)
