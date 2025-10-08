#
# PySNMP MIB module ENTERASYS-HIGH-AVAILABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-HIGH-AVAILABILITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TimeInterval, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "DateAndTime", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ENTERASYS-HIGH-AVAILABILITY-MIB", PYSNMP_MODULE_ID=etsysHighAvailabilityUpgradeMIB, etsysHauSystem=etsysHauSystem, etsysHauStatsErrorSlotList=etsysHauStatsErrorSlotList, etsysHauStatsOriginalImage=etsysHauStatsOriginalImage, etsysHauModuleGroupId=etsysHauModuleGroupId, HauSlot=HauSlot, etsysHauObjects=etsysHauObjects, etsysHauSystemInterGroupDelay=etsysHauSystemInterGroupDelay, etsysHauCompliances=etsysHauCompliances, EtsysHauSystemStatus=EtsysHauSystemStatus, etsysHauStatsTargetImage=etsysHauStatsTargetImage, etsysHauModuleEntry=etsysHauModuleEntry, etsysHauModuleSlot=etsysHauModuleSlot, etsysHauModule=etsysHauModule, etsysHauGroups=etsysHauGroups, etsysHauModuleEntRef=etsysHauModuleEntRef, etsysHauStatsPendingSlotList=etsysHauStatsPendingSlotList, etsysHauStatsInProgressSlotList=etsysHauStatsInProgressSlotList, etsysHauSystemGroup=etsysHauSystemGroup, etsysHauCompliance=etsysHauCompliance, etsysHauStatsUpgradedSlotList=etsysHauStatsUpgradedSlotList, etsysHauStatsStatus=etsysHauStatsStatus, HauSlotList=HauSlotList, etsysHauSystemHauMode=etsysHauSystemHauMode, etsysHauStatsStartTime=etsysHauStatsStartTime, EtsysHauMode=EtsysHauMode, etsysHauModuleTable=etsysHauModuleTable, etsysHauModuleGroup=etsysHauModuleGroup, etsysHauConformance=etsysHauConformance, etsysHauStatsDuration=etsysHauStatsDuration, etsysHighAvailabilityUpgradeMIB=etsysHighAvailabilityUpgradeMIB, etsysHauStats=etsysHauStats)
