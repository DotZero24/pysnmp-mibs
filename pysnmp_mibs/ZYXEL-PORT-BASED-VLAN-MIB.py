#
# PySNMP MIB module ZYXEL-PORT-BASED-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-PORT-BASED-VLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZYXEL-PORT-BASED-VLAN-MIB", zyxelPortBasedVlan=zyxelPortBasedVlan, zyxelPortBasedVlanEntry=zyxelPortBasedVlanEntry, zyxelPortBasedVlanSetup=zyxelPortBasedVlanSetup, PYSNMP_MODULE_ID=zyxelPortBasedVlan, zyxelPortBasedVlanTable=zyxelPortBasedVlanTable, zyPortBasedVlanPorts=zyPortBasedVlanPorts)
