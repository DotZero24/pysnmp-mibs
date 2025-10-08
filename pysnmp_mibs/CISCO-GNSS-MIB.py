#
# PySNMP MIB module CISCO-GNSS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-GNSS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGnssMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 862))
ciscoGnssMIB.setRevisions(('2019-05-22 00:00',))
if mibBuilder.loadTexts: ciscoGnssMIB.setLastUpdated('201909060000Z')
if mibBuilder.loadTexts: ciscoGnssMIB.setOrganization('Cisco Systems, Inc.')
class OpenCircuitAlarmStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("raise", 1), ("clear", 2))

class ShortCircuitAlarmStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("raise", 1), ("clear", 2))

class SVCnt(TextualConvention, Integer32):
    status = 'current'

class GnssSvVisibilityStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bad", 1), ("good", 2))

class SlotState(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1)

class SlotInfo(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1)

class GnssModuleLockStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("down", 1), ("up", 2))

class GnssModulePresenceStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("absent", 1), ("present", 2))

ciscoGnssMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 862, 0))
ciscoGnssMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 862, 1))
ciscoGnssMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 862, 2))
cGnssModuleLockStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 1), GnssModuleLockStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cGnssModuleLockStatus.setStatus('current')
cGnssModulePresenceStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 2), GnssModulePresenceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cGnssModulePresenceStatus.setStatus('current')
cGnssModuleSlotInfo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 3), SlotInfo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cGnssModuleSlotInfo.setStatus('current')
cGnssModuleSlotState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 4), SlotState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cGnssModuleSlotState.setStatus('current')
cGnssSatelliteVisibilityStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 5), GnssSvVisibilityStatus().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cGnssSatelliteVisibilityStatus.setStatus('current')
cGnssModuleSatelliteCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 6), SVCnt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cGnssModuleSatelliteCount.setStatus('current')
cGnssModuleSvIdSNR = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cGnssModuleSvIdSNR.setStatus('current')
cGnssModuleSCAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 8), ShortCircuitAlarmStatus().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cGnssModuleSCAlarmStatus.setStatus('current')
cGnssModuleOCAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 9), OpenCircuitAlarmStatus().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cGnssModuleOCAlarmStatus.setStatus('current')
ciscoGnssModuleLockStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 1)).setObjects(("CISCO-GNSS-MIB", "cGnssModuleLockStatus"), ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
if mibBuilder.loadTexts: ciscoGnssModuleLockStatus.setStatus('current')
ciscoGnssModuleLockClear = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 2)).setObjects(("CISCO-GNSS-MIB", "cGnssModuleLockStatus"), ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
if mibBuilder.loadTexts: ciscoGnssModuleLockClear.setStatus('current')
ciscoGnssModulePresenceStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 3)).setObjects(("CISCO-GNSS-MIB", "cGnssModulePresenceStatus"), ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
if mibBuilder.loadTexts: ciscoGnssModulePresenceStatus.setStatus('current')
ciscoGnssModulePresenceClear = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 4)).setObjects(("CISCO-GNSS-MIB", "cGnssModulePresenceStatus"), ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
if mibBuilder.loadTexts: ciscoGnssModulePresenceClear.setStatus('current')
ciscoGnssAntennaSCAlarmStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 5)).setObjects(("CISCO-GNSS-MIB", "cGnssModuleSCAlarmStatus"), ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
if mibBuilder.loadTexts: ciscoGnssAntennaSCAlarmStatus.setStatus('current')
ciscoGnssAntennaSCAlarmClear = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 6)).setObjects(("CISCO-GNSS-MIB", "cGnssModuleSCAlarmStatus"), ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
if mibBuilder.loadTexts: ciscoGnssAntennaSCAlarmClear.setStatus('current')
ciscoGnssAntennaOCAlarmStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 7)).setObjects(("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"), ("CISCO-GNSS-MIB", "cGnssModuleOCAlarmStatus"))
if mibBuilder.loadTexts: ciscoGnssAntennaOCAlarmStatus.setStatus('current')
ciscoGnssAntennaOCAlarmClear = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 8)).setObjects(("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"), ("CISCO-GNSS-MIB", "cGnssModuleOCAlarmStatus"))
if mibBuilder.loadTexts: ciscoGnssAntennaOCAlarmClear.setStatus('current')
ciscoGnssSatelliteVisibilityStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 9)).setObjects(("CISCO-GNSS-MIB", "cGnssSatelliteVisibilityStatus"), ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
if mibBuilder.loadTexts: ciscoGnssSatelliteVisibilityStatus.setStatus('current')
ciscoGnssSatelliteVisibilityClear = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 10)).setObjects(("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"), ("CISCO-GNSS-MIB", "cGnssModuleSlotState"), ("CISCO-GNSS-MIB", "cGnssSatelliteVisibilityStatus"))
if mibBuilder.loadTexts: ciscoGnssSatelliteVisibilityClear.setStatus('current')
ciscoGnssMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 1))
ciscoGnssMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 2))
ciscoGnssMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 1, 1)).setObjects(("CISCO-GNSS-MIB", "ciscoGnssMIBMainObjectGroup"), ("CISCO-GNSS-MIB", "ciscoGnssMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGnssMIBCompliance = ciscoGnssMIBCompliance.setStatus('current')
ciscoGnssMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 2, 1)).setObjects(("CISCO-GNSS-MIB", "cGnssModuleLockStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGnssMIBMainObjectGroup = ciscoGnssMIBMainObjectGroup.setStatus('current')
ciscoGnssMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 2, 2)).setObjects(("CISCO-GNSS-MIB", "ciscoGnssModuleLockStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGnssMIBNotificationGroup = ciscoGnssMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-GNSS-MIB", ciscoGnssModuleLockStatus=ciscoGnssModuleLockStatus, ciscoGnssModuleLockClear=ciscoGnssModuleLockClear, ciscoGnssMIBCompliances=ciscoGnssMIBCompliances, cGnssModuleSvIdSNR=cGnssModuleSvIdSNR, cGnssModuleLockStatus=cGnssModuleLockStatus, ciscoGnssMIBNotificationGroup=ciscoGnssMIBNotificationGroup, cGnssModuleSatelliteCount=cGnssModuleSatelliteCount, SlotInfo=SlotInfo, ciscoGnssMIBConform=ciscoGnssMIBConform, ciscoGnssSatelliteVisibilityStatus=ciscoGnssSatelliteVisibilityStatus, ciscoGnssMIBGroups=ciscoGnssMIBGroups, ciscoGnssMIBNotifs=ciscoGnssMIBNotifs, ciscoGnssMIBMainObjectGroup=ciscoGnssMIBMainObjectGroup, SVCnt=SVCnt, ciscoGnssAntennaSCAlarmStatus=ciscoGnssAntennaSCAlarmStatus, ciscoGnssMIBObjects=ciscoGnssMIBObjects, ciscoGnssAntennaOCAlarmClear=ciscoGnssAntennaOCAlarmClear, cGnssModuleOCAlarmStatus=cGnssModuleOCAlarmStatus, SlotState=SlotState, OpenCircuitAlarmStatus=OpenCircuitAlarmStatus, ciscoGnssModulePresenceClear=ciscoGnssModulePresenceClear, cGnssSatelliteVisibilityStatus=cGnssSatelliteVisibilityStatus, GnssModuleLockStatus=GnssModuleLockStatus, ciscoGnssSatelliteVisibilityClear=ciscoGnssSatelliteVisibilityClear, ciscoGnssMIBCompliance=ciscoGnssMIBCompliance, cGnssModuleSlotState=cGnssModuleSlotState, cGnssModuleSlotInfo=cGnssModuleSlotInfo, ciscoGnssModulePresenceStatus=ciscoGnssModulePresenceStatus, cGnssModulePresenceStatus=cGnssModulePresenceStatus, ShortCircuitAlarmStatus=ShortCircuitAlarmStatus, PYSNMP_MODULE_ID=ciscoGnssMIB, ciscoGnssAntennaSCAlarmClear=ciscoGnssAntennaSCAlarmClear, GnssSvVisibilityStatus=GnssSvVisibilityStatus, ciscoGnssAntennaOCAlarmStatus=ciscoGnssAntennaOCAlarmStatus, ciscoGnssMIB=ciscoGnssMIB, GnssModulePresenceStatus=GnssModulePresenceStatus, cGnssModuleSCAlarmStatus=cGnssModuleSCAlarmStatus)
