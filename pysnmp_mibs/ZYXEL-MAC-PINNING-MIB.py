#
# PySNMP MIB module ZYXEL-MAC-PINNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-MAC-PINNING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:56 2025
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
zyxelMacPinning = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92))
if mibBuilder.loadTexts: zyxelMacPinning.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMacPinning.setOrganization('Enterprise Solution ZyXEL')
zyxelMacPinningSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1))
zyMacPinningState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacPinningState.setStatus('current')
zyxelMacPinningPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2), )
if mibBuilder.loadTexts: zyxelMacPinningPortTable.setStatus('current')
zyxelMacPinningPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMacPinningPortEntry.setStatus('current')
zyMacPinningPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacPinningPortState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-MAC-PINNING-MIB", zyxelMacPinning=zyxelMacPinning, PYSNMP_MODULE_ID=zyxelMacPinning, zyxelMacPinningSetup=zyxelMacPinningSetup, zyMacPinningState=zyMacPinningState, zyMacPinningPortState=zyMacPinningPortState, zyxelMacPinningPortTable=zyxelMacPinningPortTable, zyxelMacPinningPortEntry=zyxelMacPinningPortEntry)
