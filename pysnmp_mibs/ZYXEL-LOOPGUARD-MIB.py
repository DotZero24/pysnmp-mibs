#
# PySNMP MIB module ZYXEL-LOOPGUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-LOOPGUARD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelLoopGuard = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45))
if mibBuilder.loadTexts: zyxelLoopGuard.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelLoopGuard.setOrganization('Enterprise Solution ZyXEL')
zyxelLoopGuardSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1))
zyxelLoopGuardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 2))
zyLoopGuardState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoopGuardState.setStatus('current')
zyxelLoopGuardPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1, 2), )
if mibBuilder.loadTexts: zyxelLoopGuardPortTable.setStatus('current')
zyxelLoopGuardPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelLoopGuardPortEntry.setStatus('current')
zyLoopGuardPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoopGuardPortState.setStatus('current')
zyLoopGuardLoopDetect = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 2, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyLoopGuardLoopDetect.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-LOOPGUARD-MIB", zyLoopGuardState=zyLoopGuardState, zyLoopGuardLoopDetect=zyLoopGuardLoopDetect, zyxelLoopGuard=zyxelLoopGuard, zyxelLoopGuardSetup=zyxelLoopGuardSetup, zyxelLoopGuardNotifications=zyxelLoopGuardNotifications, zyxelLoopGuardPortEntry=zyxelLoopGuardPortEntry, zyLoopGuardPortState=zyLoopGuardPortState, PYSNMP_MODULE_ID=zyxelLoopGuard, zyxelLoopGuardPortTable=zyxelLoopGuardPortTable)
