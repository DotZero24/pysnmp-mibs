#
# PySNMP MIB module CISCO-GNSS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-GNSS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("CISCO-GNSS-MIB", cGnssSatelliteVisibilityStatus=cGnssSatelliteVisibilityStatus, cGnssModulePresenceStatus=cGnssModulePresenceStatus, ciscoGnssMIBCompliances=ciscoGnssMIBCompliances, cGnssModuleLockStatus=cGnssModuleLockStatus, SlotState=SlotState, PYSNMP_MODULE_ID=ciscoGnssMIB, ciscoGnssMIBNotifs=ciscoGnssMIBNotifs, ciscoGnssMIBConform=ciscoGnssMIBConform, OpenCircuitAlarmStatus=OpenCircuitAlarmStatus, ciscoGnssModuleLockClear=ciscoGnssModuleLockClear, GnssSvVisibilityStatus=GnssSvVisibilityStatus, ciscoGnssMIBMainObjectGroup=ciscoGnssMIBMainObjectGroup, ciscoGnssModulePresenceStatus=ciscoGnssModulePresenceStatus, ciscoGnssMIBObjects=ciscoGnssMIBObjects, SVCnt=SVCnt, ciscoGnssModuleLockStatus=ciscoGnssModuleLockStatus, cGnssModuleSCAlarmStatus=cGnssModuleSCAlarmStatus, ciscoGnssAntennaSCAlarmStatus=ciscoGnssAntennaSCAlarmStatus, GnssModuleLockStatus=GnssModuleLockStatus, ciscoGnssAntennaOCAlarmClear=ciscoGnssAntennaOCAlarmClear, cGnssModuleSvIdSNR=cGnssModuleSvIdSNR, ciscoGnssMIBGroups=ciscoGnssMIBGroups, ciscoGnssMIBCompliance=ciscoGnssMIBCompliance, ciscoGnssMIB=ciscoGnssMIB, ciscoGnssAntennaSCAlarmClear=ciscoGnssAntennaSCAlarmClear, cGnssModuleSatelliteCount=cGnssModuleSatelliteCount, ciscoGnssAntennaOCAlarmStatus=ciscoGnssAntennaOCAlarmStatus, ciscoGnssMIBNotificationGroup=ciscoGnssMIBNotificationGroup, ciscoGnssModulePresenceClear=ciscoGnssModulePresenceClear, ciscoGnssSatelliteVisibilityClear=ciscoGnssSatelliteVisibilityClear, ShortCircuitAlarmStatus=ShortCircuitAlarmStatus, cGnssModuleSlotState=cGnssModuleSlotState, GnssModulePresenceStatus=GnssModulePresenceStatus, cGnssModuleSlotInfo=cGnssModuleSlotInfo, ciscoGnssSatelliteVisibilityStatus=ciscoGnssSatelliteVisibilityStatus, SlotInfo=SlotInfo, cGnssModuleOCAlarmStatus=cGnssModuleOCAlarmStatus)
