#
# PySNMP MIB module ZYXEL-PORT-ISOLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-PORT-ISOLATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:28 2025
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
zyxelPortIsolation = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64))
if mibBuilder.loadTexts: zyxelPortIsolation.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelPortIsolation.setOrganization('Enterprise Solution ZyXEL')
zyxelPortIsolationSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1))
zyxelPortIsolationPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 1), )
if mibBuilder.loadTexts: zyxelPortIsolationPortTable.setStatus('current')
zyxelPortIsolationPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelPortIsolationPortEntry.setStatus('current')
zyPortIsolationPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortIsolationPortState.setStatus('current')
zyPortIsolationSmartIsolationState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 64, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPortIsolationSmartIsolationState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-PORT-ISOLATION-MIB", zyxelPortIsolationSetup=zyxelPortIsolationSetup, zyxelPortIsolationPortEntry=zyxelPortIsolationPortEntry, zyxelPortIsolationPortTable=zyxelPortIsolationPortTable, PYSNMP_MODULE_ID=zyxelPortIsolation, zyPortIsolationPortState=zyPortIsolationPortState, zyPortIsolationSmartIsolationState=zyPortIsolationSmartIsolationState, zyxelPortIsolation=zyxelPortIsolation)
