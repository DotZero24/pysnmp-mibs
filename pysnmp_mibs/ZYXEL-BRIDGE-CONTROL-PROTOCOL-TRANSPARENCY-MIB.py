#
# PySNMP MIB module ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelBridgeControlProtocolTransparency = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15))
if mibBuilder.loadTexts: zyxelBridgeControlProtocolTransparency.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelBridgeControlProtocolTransparency.setOrganization('Enterprise Solution ZyXEL')
zyxelBridgeControlProtocolTransparencySetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1))
zyBridgeControlProtocolTransparencyState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyBridgeControlProtocolTransparencyState.setStatus('current')
zyxelBridgeControlProtocolTransparencyPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2), )
if mibBuilder.loadTexts: zyxelBridgeControlProtocolTransparencyPortTable.setStatus('current')
zyxelBridgeControlProtocolTransparencyPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelBridgeControlProtocolTransparencyPortEntry.setStatus('current')
zyBridgeControlProtocolTransparencyPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("peer", 0), ("tunnel", 1), ("discard", 2), ("network", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyBridgeControlProtocolTransparencyPortMode.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB", zyxelBridgeControlProtocolTransparencyPortTable=zyxelBridgeControlProtocolTransparencyPortTable, zyBridgeControlProtocolTransparencyPortMode=zyBridgeControlProtocolTransparencyPortMode, zyxelBridgeControlProtocolTransparencySetup=zyxelBridgeControlProtocolTransparencySetup, zyxelBridgeControlProtocolTransparencyPortEntry=zyxelBridgeControlProtocolTransparencyPortEntry, zyBridgeControlProtocolTransparencyState=zyBridgeControlProtocolTransparencyState, zyxelBridgeControlProtocolTransparency=zyxelBridgeControlProtocolTransparency, PYSNMP_MODULE_ID=zyxelBridgeControlProtocolTransparency)
