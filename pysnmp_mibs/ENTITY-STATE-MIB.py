#
# PySNMP MIB module ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/ENTITY-STATE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
entityStateMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 131))
entityStateMIB.setRevisions(('2006-09-06 00:00',))
if mibBuilder.loadTexts: entityStateMIB.setLastUpdated('200609060000Z')
if mibBuilder.loadTexts: entityStateMIB.setOrganization('IETF Entity MIB Working Group')
entStateObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 1))
class EntityAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("locked", 2), ("shuttingDown", 3), ("unlocked", 4))

class EntityOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3), ("testing", 4))

class EntityUsageState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("idle", 2), ("active", 3), ("busy", 4))

class EntityAlarmStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("unknown", 0), ("underRepair", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("indeterminate", 6))

class EntityStandbyStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("hotStandby", 2), ("coldStandby", 3), ("providingService", 4))

entStateTable = MibTable((1, 3, 6, 1, 2, 1, 131, 1, 1), )
if mibBuilder.loadTexts: entStateTable.setStatus('current')
entStateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 131, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entStateEntry.setStatus('current')
entStateLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateLastChanged.setStatus('current')
entStateAdmin = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 2), EntityAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entStateAdmin.setStatus('current')
entStateOper = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 3), EntityOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateOper.setStatus('current')
entStateUsage = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 4), EntityUsageState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateUsage.setStatus('current')
entStateAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 5), EntityAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateAlarm.setStatus('current')
entStateStandby = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 6), EntityStandbyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateStandby.setStatus('current')
entStateNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 0))
entStateOperEnabled = NotificationType((1, 3, 6, 1, 2, 1, 131, 0, 1)).setObjects(("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: entStateOperEnabled.setStatus('current')
entStateOperDisabled = NotificationType((1, 3, 6, 1, 2, 1, 131, 0, 2)).setObjects(("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: entStateOperDisabled.setStatus('current')
entStateConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2))
entStateCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2, 1))
entStateCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 131, 2, 1, 1)).setObjects(("ENTITY-STATE-MIB", "entStateGroup"), ("ENTITY-STATE-MIB", "entStateNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateCompliance = entStateCompliance.setStatus('current')
entStateGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2, 2))
entStateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 131, 2, 2, 1)).setObjects(("ENTITY-STATE-MIB", "entStateLastChanged"), ("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateOper"), ("ENTITY-STATE-MIB", "entStateUsage"), ("ENTITY-STATE-MIB", "entStateAlarm"), ("ENTITY-STATE-MIB", "entStateStandby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateGroup = entStateGroup.setStatus('current')
entStateNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 131, 2, 2, 2)).setObjects(("ENTITY-STATE-MIB", "entStateOperEnabled"), ("ENTITY-STATE-MIB", "entStateOperDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateNotificationsGroup = entStateNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ENTITY-STATE-MIB", EntityAlarmStatus=EntityAlarmStatus, entStateEntry=entStateEntry, EntityOperState=EntityOperState, entityStateMIB=entityStateMIB, entStateUsage=entStateUsage, entStateOper=entStateOper, entStateOperDisabled=entStateOperDisabled, entStateNotificationsGroup=entStateNotificationsGroup, entStateAdmin=entStateAdmin, entStateObjects=entStateObjects, entStateOperEnabled=entStateOperEnabled, entStateLastChanged=entStateLastChanged, entStateNotifications=entStateNotifications, entStateAlarm=entStateAlarm, entStateCompliances=entStateCompliances, entStateGroups=entStateGroups, entStateCompliance=entStateCompliance, EntityStandbyStatus=EntityStandbyStatus, PYSNMP_MODULE_ID=entityStateMIB, entStateTable=entStateTable, entStateStandby=entStateStandby, EntityUsageState=EntityUsageState, entStateGroup=entStateGroup, EntityAdminState=EntityAdminState, entStateConformance=entStateConformance)
