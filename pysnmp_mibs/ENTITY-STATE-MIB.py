#
# PySNMP MIB module ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/ENTITY-STATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ENTITY-STATE-MIB", entStateNotificationsGroup=entStateNotificationsGroup, entStateTable=entStateTable, EntityOperState=EntityOperState, EntityUsageState=EntityUsageState, entStateCompliance=entStateCompliance, entStateEntry=entStateEntry, EntityAdminState=EntityAdminState, entStateUsage=entStateUsage, entStateAdmin=entStateAdmin, entStateOperEnabled=entStateOperEnabled, entStateGroup=entStateGroup, entStateAlarm=entStateAlarm, EntityStandbyStatus=EntityStandbyStatus, entStateConformance=entStateConformance, entStateOperDisabled=entStateOperDisabled, EntityAlarmStatus=EntityAlarmStatus, entStateStandby=entStateStandby, entityStateMIB=entityStateMIB, entStateObjects=entStateObjects, entStateLastChanged=entStateLastChanged, entStateGroups=entStateGroups, entStateCompliances=entStateCompliances, entStateOper=entStateOper, PYSNMP_MODULE_ID=entityStateMIB, entStateNotifications=entStateNotifications)
