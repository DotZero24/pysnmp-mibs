#
# PySNMP MIB module Juniper-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-REDUNDANCY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
juniRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74))
juniRedundancyMIB.setRevisions(('2010-03-19 12:31', '2003-12-12 00:00',))
if mibBuilder.loadTexts: juniRedundancyMIB.setLastUpdated('201003191231Z')
if mibBuilder.loadTexts: juniRedundancyMIB.setOrganization('Juniper Networks, Inc.')
class JuniRedundancyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notKnown", 1), ("fileSystemSyncing", 2), ("disabled", 3), ("initializing", 4), ("pending", 5), ("active", 6))

class JuniRedundancyMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fileSystemSynchronization", 1), ("highAvailability", 2))

class JuniRedundancyResetReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("notKnown", 2), ("userInitiated", 3))

class JuniRedundancySystemActivationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("reload", 1), ("coldSwitch", 2), ("warmSwitch", 3))

class JuniRedundancyResetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notKnown", 1), ("srpReload", 2), ("srpSwitchover", 3), ("linecardReload", 4), ("linecardSwitchover", 5))

class JuniRedundancyHistoryCommand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("keep", 1), ("clear", 2))

class JuniLcRedundancySystemActivationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("reload", 1), ("coldSwitch", 2), ("warmSwitch", 3))

class JuniLcRedundancyResetReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("poweron", 1), ("notKnown", 2), ("userInitiated", 3), ("hardware", 4), ("software", 5))

juniRedundancyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0))
juniRedundancyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1))
juniRedundancyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2))
juniRedundancyStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1))
juniRedundancyCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2))
juniRedundancyHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3))
juniLcRedundancyStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 4))
juniRedundancyActiveSlot = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyActiveSlot.setStatus('current')
juniRedundancyActiveSlotState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 2), JuniRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyActiveSlotState.setStatus('current')
juniRedundancyStandbySlot = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyStandbySlot.setStatus('current')
juniRedundancyStandbySlotState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 4), JuniRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyStandbySlotState.setStatus('current')
juniRedundancyLastResetReason = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 5), JuniRedundancyResetReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyLastResetReason.setStatus('current')
juniRedundancyLastSystemActivationTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyLastSystemActivationTime.setStatus('current')
juniRedundancyLastSystemActivationType = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 7), JuniRedundancySystemActivationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyLastSystemActivationType.setStatus('current')
juniRedundancyHaActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHaActiveTime.setStatus('current')
juniLcRedundancyActiveSlot = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniLcRedundancyActiveSlot.setStatus('current')
juniLcRedundancyStandbySlot = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniLcRedundancyStandbySlot.setStatus('current')
juniLcRedundancyLastResetReason = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 4, 3), JuniLcRedundancyResetReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniLcRedundancyLastResetReason.setStatus('current')
juniLcRedundancyActivationType = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 4, 4), JuniLcRedundancySystemActivationType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniLcRedundancyActivationType.setStatus('current')
juniLcRedundancyHaActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 4, 5), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniLcRedundancyHaActiveTime.setStatus('current')
juniLcRedundancySwitchoverTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 4, 6), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniLcRedundancySwitchoverTime.setStatus('current')
juniRedundancyNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancyNotifsEnabled.setStatus('current')
juniRedundancyCfgRedundancyMode = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2, 2), JuniRedundancyMode().clone('fileSystemSynchronization')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancyCfgRedundancyMode.setStatus('current')
juniRedundancySystemActivationHistoryTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryTableMaxLength.setStatus('current')
juniRedundancySystemActivationHistoryCommand = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 2), JuniRedundancyHistoryCommand().clone('keep')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryCommand.setStatus('current')
juniRedundancySystemActivationHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3), )
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryTable.setStatus('current')
juniRedundancySystemActivationHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1), ).setIndexNames((0, "Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryIndex"))
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryEntry.setStatus('current')
juniRedundancySystemActivationHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryIndex.setStatus('current')
juniRedundancyHistoryResetType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 2), JuniRedundancyResetType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryResetType.setStatus('current')
juniRedundancyHistoryActivationType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 3), JuniRedundancySystemActivationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryActivationType.setStatus('current')
juniRedundancyHistoryPrevActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryPrevActiveSlot.setStatus('current')
juniRedundancyHistoryPrevActiveRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryPrevActiveRelease.setStatus('current')
juniRedundancyHistoryCurrActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryCurrActiveSlot.setStatus('current')
juniRedundancyHistoryCurrActiveRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryCurrActiveRelease.setStatus('current')
juniRedundancyHistoryResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 8), JuniRedundancyResetReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryResetReason.setStatus('current')
juniRedundancyHistoryActivationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryActivationTime.setStatus('current')
juniRedundancyHistoryReloads = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryReloads.setStatus('current')
juniRedundancyHistoryColdSwitchovers = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryColdSwitchovers.setStatus('current')
juniRedundancyHistoryWarmSwitchovers = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryWarmSwitchovers.setStatus('current')
juniRedundancyColdSwitchoverNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 1)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"))
if mibBuilder.loadTexts: juniRedundancyColdSwitchoverNotification.setStatus('current')
juniRedundancyWarmSwitchoverNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 2)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"))
if mibBuilder.loadTexts: juniRedundancyWarmSwitchoverNotification.setStatus('current')
juniRedundancyStateEnabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 3)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"))
if mibBuilder.loadTexts: juniRedundancyStateEnabledNotification.setStatus('current')
juniRedundancyStateDisabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 4)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"))
if mibBuilder.loadTexts: juniRedundancyStateDisabledNotification.setStatus('current')
juniRedundancyStatePendingNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 5)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"))
if mibBuilder.loadTexts: juniRedundancyStatePendingNotification.setStatus('current')
juniRedundancyModeNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 6)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgRedundancyMode"))
if mibBuilder.loadTexts: juniRedundancyModeNotification.setStatus('current')
juniLcRedundancySwitchoverNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 7)).setObjects(("Juniper-REDUNDANCY-MIB", "juniLcRedundancyActivationType"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancyLastResetReason"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancyStandbySlot"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancySwitchoverTime"))
if mibBuilder.loadTexts: juniLcRedundancySwitchoverNotification.setStatus('current')
juniLcRedundancyStateEnabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 8)).setObjects(("Juniper-REDUNDANCY-MIB", "juniLcRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancyStandbySlot"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancyHaActiveTime"))
if mibBuilder.loadTexts: juniLcRedundancyStateEnabledNotification.setStatus('current')
juniLcRedundancyStateDisabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 9)).setObjects(("Juniper-REDUNDANCY-MIB", "juniLcRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancyStandbySlot"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancyHaActiveTime"))
if mibBuilder.loadTexts: juniLcRedundancyStateDisabledNotification.setStatus('current')
juniRedundancyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 1))
juniRedundancyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2))
juniRedundancyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 1, 1)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyStatusGroup"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgGroup"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryGroup"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyMIBCompliance = juniRedundancyMIBCompliance.setStatus('current')
juniRedundancyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 1)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlotState"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStandbySlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStandbySlotState"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastSystemActivationTime"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastSystemActivationType"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHaActiveTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyStatusGroup = juniRedundancyStatusGroup.setStatus('current')
juniRedundancyCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 2)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyNotifsEnabled"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgRedundancyMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyCfgGroup = juniRedundancyCfgGroup.setStatus('current')
juniRedundancyHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 3)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryTableMaxLength"), ("Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryCommand"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryResetType"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryActivationType"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryPrevActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryPrevActiveRelease"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryCurrActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryCurrActiveRelease"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryResetReason"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryActivationTime"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryReloads"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryColdSwitchovers"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryWarmSwitchovers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyHistoryGroup = juniRedundancyHistoryGroup.setStatus('current')
juniRedundancyNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 4)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyColdSwitchoverNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyWarmSwitchoverNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStateEnabledNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStateDisabledNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStatePendingNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyModeNotification"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancySwitchoverNotification"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancyStateEnabledNotification"), ("Juniper-REDUNDANCY-MIB", "juniLcRedundancyStateDisabledNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyNotificationGroup = juniRedundancyNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-REDUNDANCY-MIB", juniRedundancySystemActivationHistoryIndex=juniRedundancySystemActivationHistoryIndex, juniRedundancyStateDisabledNotification=juniRedundancyStateDisabledNotification, JuniRedundancyResetType=JuniRedundancyResetType, juniRedundancyActiveSlot=juniRedundancyActiveSlot, juniRedundancySystemActivationHistoryTableMaxLength=juniRedundancySystemActivationHistoryTableMaxLength, juniRedundancyMIBCompliances=juniRedundancyMIBCompliances, JuniRedundancyMode=JuniRedundancyMode, juniRedundancyStateEnabledNotification=juniRedundancyStateEnabledNotification, juniRedundancySystemActivationHistoryTable=juniRedundancySystemActivationHistoryTable, juniRedundancyStandbySlot=juniRedundancyStandbySlot, juniRedundancyNotificationGroup=juniRedundancyNotificationGroup, juniRedundancyStatePendingNotification=juniRedundancyStatePendingNotification, juniRedundancyHistoryReloads=juniRedundancyHistoryReloads, juniRedundancyColdSwitchoverNotification=juniRedundancyColdSwitchoverNotification, juniLcRedundancyHaActiveTime=juniLcRedundancyHaActiveTime, JuniLcRedundancyResetReason=JuniLcRedundancyResetReason, PYSNMP_MODULE_ID=juniRedundancyMIB, juniLcRedundancyLastResetReason=juniLcRedundancyLastResetReason, juniRedundancyHistoryActivationType=juniRedundancyHistoryActivationType, juniRedundancyHistoryResetType=juniRedundancyHistoryResetType, juniRedundancyHistoryActivationTime=juniRedundancyHistoryActivationTime, juniRedundancyHistoryCurrActiveRelease=juniRedundancyHistoryCurrActiveRelease, juniRedundancyMIBGroups=juniRedundancyMIBGroups, juniRedundancyLastSystemActivationType=juniRedundancyLastSystemActivationType, juniRedundancyModeNotification=juniRedundancyModeNotification, juniRedundancyObjects=juniRedundancyObjects, juniRedundancyHistoryCurrActiveSlot=juniRedundancyHistoryCurrActiveSlot, juniRedundancyHaActiveTime=juniRedundancyHaActiveTime, juniRedundancyLastResetReason=juniRedundancyLastResetReason, juniRedundancyStatus=juniRedundancyStatus, juniRedundancyLastSystemActivationTime=juniRedundancyLastSystemActivationTime, juniLcRedundancySwitchoverTime=juniLcRedundancySwitchoverTime, juniRedundancySystemActivationHistoryEntry=juniRedundancySystemActivationHistoryEntry, juniLcRedundancySwitchoverNotification=juniLcRedundancySwitchoverNotification, juniRedundancyNotifications=juniRedundancyNotifications, JuniLcRedundancySystemActivationType=JuniLcRedundancySystemActivationType, juniRedundancyStatusGroup=juniRedundancyStatusGroup, juniRedundancySystemActivationHistoryCommand=juniRedundancySystemActivationHistoryCommand, juniRedundancyMIB=juniRedundancyMIB, juniRedundancyActiveSlotState=juniRedundancyActiveSlotState, juniLcRedundancyStandbySlot=juniLcRedundancyStandbySlot, juniRedundancyCfgRedundancyMode=juniRedundancyCfgRedundancyMode, juniRedundancyHistoryResetReason=juniRedundancyHistoryResetReason, juniRedundancyCfgGroup=juniRedundancyCfgGroup, juniLcRedundancyActivationType=juniLcRedundancyActivationType, juniRedundancyNotifsEnabled=juniRedundancyNotifsEnabled, juniRedundancyWarmSwitchoverNotification=juniRedundancyWarmSwitchoverNotification, juniRedundancyCfg=juniRedundancyCfg, juniRedundancyHistoryPrevActiveSlot=juniRedundancyHistoryPrevActiveSlot, JuniRedundancyResetReason=JuniRedundancyResetReason, juniRedundancyMIBCompliance=juniRedundancyMIBCompliance, juniLcRedundancyStatus=juniLcRedundancyStatus, juniLcRedundancyStateEnabledNotification=juniLcRedundancyStateEnabledNotification, juniRedundancyHistory=juniRedundancyHistory, juniLcRedundancyStateDisabledNotification=juniLcRedundancyStateDisabledNotification, juniRedundancyHistoryPrevActiveRelease=juniRedundancyHistoryPrevActiveRelease, juniRedundancyMIBConformance=juniRedundancyMIBConformance, juniRedundancyHistoryColdSwitchovers=juniRedundancyHistoryColdSwitchovers, juniRedundancyHistoryGroup=juniRedundancyHistoryGroup, JuniRedundancyHistoryCommand=JuniRedundancyHistoryCommand, juniLcRedundancyActiveSlot=juniLcRedundancyActiveSlot, JuniRedundancySystemActivationType=JuniRedundancySystemActivationType, juniRedundancyHistoryWarmSwitchovers=juniRedundancyHistoryWarmSwitchovers, juniRedundancyStandbySlotState=juniRedundancyStandbySlotState, JuniRedundancyState=JuniRedundancyState)
