#
# PySNMP MIB module MELLANOX-ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mellanox/MELLANOX-ENTITY-STATE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mellanoxEntState, = mibBuilder.importSymbols("MELLANOX-SMI-MIB", "mellanoxEntState")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("MELLANOX-ENTITY-STATE-MIB", mellanoxEntStateMibObjects=mellanoxEntStateMibObjects, mellanoxEntStateChangeAlarm=mellanoxEntStateChangeAlarm, mellanoxEntStateModuleCurrentState=mellanoxEntStateModuleCurrentState, mellanoxEntStateMibNotifications=mellanoxEntStateMibNotifications, mellanoxEntStateModuleStateDescr=mellanoxEntStateModuleStateDescr, mellanoxEntStateTable=mellanoxEntStateTable, ModuleStateType=ModuleStateType, mellanoxEntStateEntry=mellanoxEntStateEntry, mellanoxEntStateModulePreviousState=mellanoxEntStateModulePreviousState, PYSNMP_MODULE_ID=mellanoxEntStateMib, mellanoxEntStateMib=mellanoxEntStateMib)
