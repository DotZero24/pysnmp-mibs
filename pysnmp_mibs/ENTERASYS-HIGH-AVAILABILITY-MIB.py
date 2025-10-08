#
# PySNMP MIB module ENTERASYS-HIGH-AVAILABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-HIGH-AVAILABILITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "TimeInterval")
etsysHighAvailabilityUpgradeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84))
etsysHighAvailabilityUpgradeMIB.setRevisions(('2011-12-12 15:14',))
if mibBuilder.loadTexts: etsysHighAvailabilityUpgradeMIB.setLastUpdated('201112121514Z')
if mibBuilder.loadTexts: etsysHighAvailabilityUpgradeMIB.setOrganization('Enterasys Networks, Inc')
class EtsysHauSystemStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("hauDisabled", 1), ("hauPending", 2), ("hauRunning", 3), ("hauHalted", 4), ("hauSuccess", 5), ("hauError", 6), ("hauForceComplete", 7))

class EtsysHauMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("hauNever", 1), ("hauIfPossible", 2), ("hauAlways", 3))

class HauSlotList(TextualConvention, OctetString):
    status = 'current'

class HauSlot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 128)

etsysHauObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1))
etsysHauStats = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1))
etsysHauSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 2))
etsysHauModule = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3))
etsysHauStatsStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 1), EtsysHauSystemStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauStatsStatus.setStatus('current')
etsysHauStatsOriginalImage = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauStatsOriginalImage.setStatus('current')
etsysHauStatsTargetImage = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauStatsTargetImage.setStatus('current')
etsysHauStatsPendingSlotList = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 4), HauSlotList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauStatsPendingSlotList.setStatus('current')
etsysHauStatsInProgressSlotList = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 5), HauSlotList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauStatsInProgressSlotList.setStatus('current')
etsysHauStatsUpgradedSlotList = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 6), HauSlotList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauStatsUpgradedSlotList.setStatus('current')
etsysHauStatsErrorSlotList = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 7), HauSlotList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauStatsErrorSlotList.setStatus('current')
etsysHauStatsStartTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauStatsStartTime.setStatus('current')
etsysHauStatsDuration = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 9), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauStatsDuration.setStatus('current')
etsysHauSystemInterGroupDelay = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 2, 1), Unsigned32().clone(15)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysHauSystemInterGroupDelay.setStatus('current')
etsysHauSystemHauMode = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 2, 2), EtsysHauMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysHauSystemHauMode.setStatus('current')
etsysHauModuleTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1), )
if mibBuilder.loadTexts: etsysHauModuleTable.setStatus('current')
etsysHauModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1, 1), ).setIndexNames((0, "ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauModuleSlot"))
if mibBuilder.loadTexts: etsysHauModuleEntry.setStatus('current')
etsysHauModuleSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1, 1, 1), HauSlot())
if mibBuilder.loadTexts: etsysHauModuleSlot.setStatus('current')
etsysHauModuleEntRef = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1, 1, 2), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysHauModuleEntRef.setStatus('current')
etsysHauModuleGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysHauModuleGroupId.setStatus('current')
etsysHauConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2))
etsysHauGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 1))
etsysHauCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 2))
etsysHauSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 1, 1)).setObjects(("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauSystemInterGroupDelay"), ("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauSystemHauMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysHauSystemGroup = etsysHauSystemGroup.setStatus('current')
etsysHauModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 1, 2)).setObjects(("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauModuleGroupId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysHauModuleGroup = etsysHauModuleGroup.setStatus('current')
etsysHauCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 2, 1)).setObjects(("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauSystemGroup"), ("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauModuleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysHauCompliance = etsysHauCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-HIGH-AVAILABILITY-MIB", etsysHauSystemHauMode=etsysHauSystemHauMode, etsysHauStatsStatus=etsysHauStatsStatus, etsysHauModuleGroupId=etsysHauModuleGroupId, etsysHauObjects=etsysHauObjects, etsysHauStatsStartTime=etsysHauStatsStartTime, etsysHauStatsUpgradedSlotList=etsysHauStatsUpgradedSlotList, etsysHauModuleEntRef=etsysHauModuleEntRef, etsysHauStats=etsysHauStats, etsysHauStatsOriginalImage=etsysHauStatsOriginalImage, etsysHauConformance=etsysHauConformance, PYSNMP_MODULE_ID=etsysHighAvailabilityUpgradeMIB, etsysHauStatsDuration=etsysHauStatsDuration, HauSlot=HauSlot, etsysHauModule=etsysHauModule, etsysHauModuleEntry=etsysHauModuleEntry, etsysHauGroups=etsysHauGroups, etsysHauModuleGroup=etsysHauModuleGroup, etsysHauModuleSlot=etsysHauModuleSlot, etsysHauSystem=etsysHauSystem, etsysHauSystemInterGroupDelay=etsysHauSystemInterGroupDelay, etsysHauCompliance=etsysHauCompliance, HauSlotList=HauSlotList, etsysHauCompliances=etsysHauCompliances, etsysHauStatsPendingSlotList=etsysHauStatsPendingSlotList, etsysHauStatsErrorSlotList=etsysHauStatsErrorSlotList, etsysHauStatsTargetImage=etsysHauStatsTargetImage, EtsysHauMode=EtsysHauMode, etsysHauModuleTable=etsysHauModuleTable, etsysHighAvailabilityUpgradeMIB=etsysHighAvailabilityUpgradeMIB, etsysHauSystemGroup=etsysHauSystemGroup, etsysHauStatsInProgressSlotList=etsysHauStatsInProgressSlotList, EtsysHauSystemStatus=EtsysHauSystemStatus)
