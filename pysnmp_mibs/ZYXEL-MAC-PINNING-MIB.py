#
# PySNMP MIB module ZYXEL-MAC-PINNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-MAC-PINNING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ZYXEL-MAC-PINNING-MIB", zyxelMacPinningSetup=zyxelMacPinningSetup, zyxelMacPinningPortEntry=zyxelMacPinningPortEntry, zyMacPinningState=zyMacPinningState, zyxelMacPinning=zyxelMacPinning, zyxelMacPinningPortTable=zyxelMacPinningPortTable, PYSNMP_MODULE_ID=zyxelMacPinning, zyMacPinningPortState=zyMacPinningPortState)
