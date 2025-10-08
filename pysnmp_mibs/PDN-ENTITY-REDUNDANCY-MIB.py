#
# PySNMP MIB module PDN-ENTITY-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-ENTITY-REDUNDANCY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
pdnEntityRedundancy, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnEntityRedundancy")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnEntRedunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1))
pdnEntRedunMIB.setRevisions(('2003-07-25 13:00', '2003-05-22 10:00', '2003-05-04 17:00', '2003-03-03 15:00',))
if mibBuilder.loadTexts: pdnEntRedunMIB.setLastUpdated('200301121100Z')
if mibBuilder.loadTexts: pdnEntRedunMIB.setOrganization('Paradyne Corporation MIB Working Group')
class PdnRedunStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("activeState", 1), ("activeAlarmState", 2), ("standbyState", 3), ("standbyAlarmState", 4))

class PdnRedunCmd(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noCmd", 1), ("switch", 2), ("forcedswitch", 3))

class PdnRedunAlarmStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("noAlarm", 0), ("linkDefect", 1), ("hwFailure", 2), ("hwMissing", 3), ("hwIncompatible", 4), ("fwIncompatible", 5), ("cfgIncompatible", 6))

class PdnRedunGeneralAlarmStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("noAlarm", 0), ("noActiveModule", 1), ("standbyAlarmOrReset", 2))

pdnEntityRedundancyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1))
pdnEntityRedundancyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2))
pdnEntityRedundancyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3))
pdnEntityRedundancySelection = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnEntityRedundancySelection.setStatus('current')
pdnYCableSelection = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnYCableSelection.setStatus('current')
pdnRedunGeneralAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 3), PdnRedunGeneralAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnRedunGeneralAlarmStatus.setStatus('current')
pdnRedunGeneralNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 6), PdnRedunGeneralAlarmStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnRedunGeneralNotificationEnable.setStatus('current')
pdnRedunCmdTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 4), )
if mibBuilder.loadTexts: pdnRedunCmdTable.setStatus('current')
pdnRedunCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: pdnRedunCmdEntry.setStatus('current')
pdnRedunCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 4, 1, 1), PdnRedunCmd()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnRedunCommand.setStatus('current')
pdnRedunStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5), )
if mibBuilder.loadTexts: pdnRedunStatusTable.setStatus('current')
pdnRedunStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: pdnRedunStatusEntry.setStatus('current')
pdnRedunEntityState = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1, 1), PdnRedunStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnRedunEntityState.setStatus('current')
pdnRedunAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1, 2), PdnRedunAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnRedunAlarmStatus.setStatus('current')
pdnRedunNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1, 3), PdnRedunAlarmStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnRedunNotificationEnable.setStatus('current')
pdnRedunNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0))
pdnRedunEventNoActiveModule = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 1)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventNoActiveModule.setStatus('current')
pdnRedunEventHwIncompatible = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 2)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventHwIncompatible.setStatus('current')
pdnRedunEventStandbyAlarmOrReset = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 3)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventStandbyAlarmOrReset.setStatus('current')
pdnRedunEventFwIncompatible = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 4)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventFwIncompatible.setStatus('current')
pdnRedunEventCfgIncompatible = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 5)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventCfgIncompatible.setStatus('current')
pdnRedunEventLinkDefect = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 6)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventLinkDefect.setStatus('current')
pdnRedunEventHwFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 7)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventHwFailure.setStatus('current')
pdnRedunEventHwMissingHwFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 8)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventHwMissingHwFailure.setStatus('current')
pdnEntityRedundancyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 1))
pdnEntityRedundancyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2))
pdnEntityRedundancyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 1, 1)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedundancyGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEntityRedundancyCompliance = pdnEntityRedundancyCompliance.setStatus('current')
pdnRedundancyGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2, 1)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnEntityRedundancySelection"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnYCableSelection"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralAlarmStatus"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnRedundancyGeneralGroup = pdnRedundancyGeneralGroup.setStatus('current')
pdnEntityRedundancyOptGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2, 2)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunCommand"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunNotificationEnable"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEntityState"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEntityRedundancyOptGroup = pdnEntityRedundancyOptGroup.setStatus('current')
pdnEntityRedundancyEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2, 3)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventNoActiveModule"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventHwIncompatible"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventStandbyAlarmOrReset"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventFwIncompatible"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventCfgIncompatible"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventLinkDefect"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventHwFailure"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventHwMissingHwFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEntityRedundancyEventGroup = pdnEntityRedundancyEventGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-ENTITY-REDUNDANCY-MIB", pdnEntityRedundancyGroups=pdnEntityRedundancyGroups, pdnRedunEventStandbyAlarmOrReset=pdnRedunEventStandbyAlarmOrReset, pdnRedunEventLinkDefect=pdnRedunEventLinkDefect, pdnRedunAlarmStatus=pdnRedunAlarmStatus, pdnRedunEventFwIncompatible=pdnRedunEventFwIncompatible, pdnEntityRedundancyCompliance=pdnEntityRedundancyCompliance, pdnYCableSelection=pdnYCableSelection, pdnEntityRedundancyEventGroup=pdnEntityRedundancyEventGroup, pdnRedunEventHwMissingHwFailure=pdnRedunEventHwMissingHwFailure, pdnRedunNotificationsPrefix=pdnRedunNotificationsPrefix, pdnRedunNotificationEnable=pdnRedunNotificationEnable, pdnRedunEventHwIncompatible=pdnRedunEventHwIncompatible, pdnRedundancyGeneralGroup=pdnRedundancyGeneralGroup, pdnRedunStatusTable=pdnRedunStatusTable, pdnEntRedunMIB=pdnEntRedunMIB, pdnEntityRedundancyNotifications=pdnEntityRedundancyNotifications, pdnRedunEventHwFailure=pdnRedunEventHwFailure, pdnRedunEventCfgIncompatible=pdnRedunEventCfgIncompatible, pdnEntityRedundancyCompliances=pdnEntityRedundancyCompliances, pdnEntityRedundancyMIBObjects=pdnEntityRedundancyMIBObjects, pdnRedunCmdTable=pdnRedunCmdTable, pdnRedunCmdEntry=pdnRedunCmdEntry, pdnEntityRedundancyOptGroup=pdnEntityRedundancyOptGroup, PYSNMP_MODULE_ID=pdnEntRedunMIB, pdnRedunGeneralNotificationEnable=pdnRedunGeneralNotificationEnable, pdnEntityRedundancyConformance=pdnEntityRedundancyConformance, pdnRedunCommand=pdnRedunCommand, pdnEntityRedundancySelection=pdnEntityRedundancySelection, pdnRedunEntityState=pdnRedunEntityState, PdnRedunAlarmStatus=PdnRedunAlarmStatus, pdnRedunGeneralAlarmStatus=pdnRedunGeneralAlarmStatus, pdnRedunEventNoActiveModule=pdnRedunEventNoActiveModule, PdnRedunCmd=PdnRedunCmd, PdnRedunStates=PdnRedunStates, pdnRedunStatusEntry=pdnRedunStatusEntry, PdnRedunGeneralAlarmStatus=PdnRedunGeneralAlarmStatus)
