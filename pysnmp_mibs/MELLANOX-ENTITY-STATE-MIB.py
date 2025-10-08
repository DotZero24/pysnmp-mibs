#
# PySNMP MIB module MELLANOX-ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mellanox/MELLANOX-ENTITY-STATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mellanoxEntState, = mibBuilder.importSymbols("MELLANOX-SMI-MIB", "mellanoxEntState")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mellanoxEntStateMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 33049, 7, 1))
mellanoxEntStateMib.setRevisions(('2017-07-25 00:00',))
if mibBuilder.loadTexts: mellanoxEntStateMib.setLastUpdated('201707250000Z')
if mibBuilder.loadTexts: mellanoxEntStateMib.setOrganization('Mellanox Technologies, Inc.')
mellanoxEntStateMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 33049, 7, 1, 0))
mellanoxEntStateMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 33049, 7, 1, 1))
class ModuleStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("ok", 1), ("disabled", 2), ("reset", 3), ("missing", 4), ("criticalFault", 5), ("nonCriticalFault", 6), ("unknown", 7))

mellanoxEntStateTable = MibTable((1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1), )
if mibBuilder.loadTexts: mellanoxEntStateTable.setStatus('current')
mellanoxEntStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mellanoxEntStateEntry.setStatus('current')
mellanoxEntStateModuleCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1, 1, 1), ModuleStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mellanoxEntStateModuleCurrentState.setStatus('current')
mellanoxEntStateModulePreviousState = MibTableColumn((1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1, 1, 2), ModuleStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mellanoxEntStateModulePreviousState.setStatus('current')
mellanoxEntStateModuleStateDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mellanoxEntStateModuleStateDescr.setStatus('current')
mellanoxEntStateChangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33049, 7, 1, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalIndex"), ("MELLANOX-ENTITY-STATE-MIB", "entPhysicalDescr"), ("MELLANOX-ENTITY-STATE-MIB", "entPhysicalName"), ("MELLANOX-ENTITY-STATE-MIB", "mellanoxEntStateModuleCurrentState"), ("MELLANOX-ENTITY-STATE-MIB", "mellanoxEntStateModulePreviousState"), ("MELLANOX-ENTITY-STATE-MIB", "mellanoxEntStateModuleStateDescr"), ("MELLANOX-ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: mellanoxEntStateChangeAlarm.setStatus('current')
mibBuilder.exportSymbols("MELLANOX-ENTITY-STATE-MIB", mellanoxEntStateEntry=mellanoxEntStateEntry, PYSNMP_MODULE_ID=mellanoxEntStateMib, mellanoxEntStateModuleCurrentState=mellanoxEntStateModuleCurrentState, mellanoxEntStateMib=mellanoxEntStateMib, ModuleStateType=ModuleStateType, mellanoxEntStateModuleStateDescr=mellanoxEntStateModuleStateDescr, mellanoxEntStateMibObjects=mellanoxEntStateMibObjects, mellanoxEntStateChangeAlarm=mellanoxEntStateChangeAlarm, mellanoxEntStateMibNotifications=mellanoxEntStateMibNotifications, mellanoxEntStateTable=mellanoxEntStateTable, mellanoxEntStateModulePreviousState=mellanoxEntStateModulePreviousState)
