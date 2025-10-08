#
# PySNMP MIB module ZYXEL-PORT-ISOLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-PORT-ISOLATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:21 2025
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
mibBuilder.exportSymbols("ZYXEL-PORT-ISOLATION-MIB", zyPortIsolationSmartIsolationState=zyPortIsolationSmartIsolationState, zyxelPortIsolationPortEntry=zyxelPortIsolationPortEntry, PYSNMP_MODULE_ID=zyxelPortIsolation, zyPortIsolationPortState=zyPortIsolationPortState, zyxelPortIsolationPortTable=zyxelPortIsolationPortTable, zyxelPortIsolation=zyxelPortIsolation, zyxelPortIsolationSetup=zyxelPortIsolationSetup)
