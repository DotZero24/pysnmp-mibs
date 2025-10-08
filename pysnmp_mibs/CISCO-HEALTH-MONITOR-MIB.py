#
# PySNMP MIB module CISCO-HEALTH-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-HEALTH-MONITOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoHealthMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 243))
ciscoHealthMonitorMIB.setRevisions(('2003-09-12 12:30',))
if mibBuilder.loadTexts: ciscoHealthMonitorMIB.setLastUpdated('200309121230Z')
if mibBuilder.loadTexts: ciscoHealthMonitorMIB.setOrganization('Cisco Systems, Inc.')
ciscoHealthMonitorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 1))
class HealthLevel(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 10000)

ciscoHealthMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1), )
if mibBuilder.loadTexts: ciscoHealthMonitorTable.setStatus('current')
ciscoHealthMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (1, "CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorSubsysName"))
if mibBuilder.loadTexts: ciscoHealthMonitorEntry.setStatus('current')
ciscoHealthMonitorSubsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128)))
if mibBuilder.loadTexts: ciscoHealthMonitorSubsysName.setStatus('current')
ciscoHealthMonitorHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 2), HealthLevel()).setUnits('0.01 percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorHealth.setStatus('current')
ciscoHealthMonitorHealthNotifyEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoHealthMonitorHealthNotifyEnable.setStatus('current')
ciscoHealthMonitorHealthNotifyHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 4), HealthLevel().clone(10000)).setUnits('0.01 percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoHealthMonitorHealthNotifyHighThreshold.setStatus('current')
ciscoHealthMonitorHealthNotifyLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 5), HealthLevel()).setUnits('0.01 percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoHealthMonitorHealthNotifyLowThreshold.setStatus('current')
ciscoHealthMonitorCatastrophicFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorCatastrophicFaults.setStatus('current')
ciscoHealthMonitorCriticalFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorCriticalFaults.setStatus('current')
ciscoHealthMonitorHighSeverityFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorHighSeverityFaults.setStatus('current')
ciscoHealthMonitorMediumSeverityFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorMediumSeverityFaults.setStatus('current')
ciscoHealthMonitorLowSeverityFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorLowSeverityFaults.setStatus('current')
ciscoHealthMonitorPositiveEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorPositiveEvents.setStatus('current')
ciscoHealthMonitorMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 0))
ciscoHealthMonitorHealthLevel = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 243, 0, 1)).setObjects(("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealth"))
if mibBuilder.loadTexts: ciscoHealthMonitorHealthLevel.setStatus('current')
ciscoHealthMonitorMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 2))
ciscoHealthMonitorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 1))
ciscoHealthMonitorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 2))
ciscoHealthMonitorMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 1, 1)).setObjects(("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHealthMonitorMIBCompliance = ciscoHealthMonitorMIBCompliance.setStatus('current')
ciscoHealthMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 2, 1)).setObjects(("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealth"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthNotifyEnable"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthNotifyHighThreshold"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthNotifyLowThreshold"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorCatastrophicFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorCriticalFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHighSeverityFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorMediumSeverityFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorLowSeverityFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorPositiveEvents"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHealthMonitorGroup = ciscoHealthMonitorGroup.setStatus('current')
ciscoHealthMonitorMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 2, 2)).setObjects(("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHealthMonitorMIBNotificationGroup = ciscoHealthMonitorMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-HEALTH-MONITOR-MIB", ciscoHealthMonitorHealthLevel=ciscoHealthMonitorHealthLevel, ciscoHealthMonitorMediumSeverityFaults=ciscoHealthMonitorMediumSeverityFaults, ciscoHealthMonitorMIBNotifs=ciscoHealthMonitorMIBNotifs, ciscoHealthMonitorTable=ciscoHealthMonitorTable, ciscoHealthMonitorMIBCompliances=ciscoHealthMonitorMIBCompliances, ciscoHealthMonitorMIBGroups=ciscoHealthMonitorMIBGroups, PYSNMP_MODULE_ID=ciscoHealthMonitorMIB, ciscoHealthMonitorMIBObjects=ciscoHealthMonitorMIBObjects, ciscoHealthMonitorEntry=ciscoHealthMonitorEntry, ciscoHealthMonitorHighSeverityFaults=ciscoHealthMonitorHighSeverityFaults, ciscoHealthMonitorMIBConform=ciscoHealthMonitorMIBConform, ciscoHealthMonitorHealthNotifyEnable=ciscoHealthMonitorHealthNotifyEnable, ciscoHealthMonitorMIBNotificationGroup=ciscoHealthMonitorMIBNotificationGroup, ciscoHealthMonitorMIB=ciscoHealthMonitorMIB, HealthLevel=HealthLevel, ciscoHealthMonitorHealthNotifyHighThreshold=ciscoHealthMonitorHealthNotifyHighThreshold, ciscoHealthMonitorPositiveEvents=ciscoHealthMonitorPositiveEvents, ciscoHealthMonitorCriticalFaults=ciscoHealthMonitorCriticalFaults, ciscoHealthMonitorHealth=ciscoHealthMonitorHealth, ciscoHealthMonitorMIBCompliance=ciscoHealthMonitorMIBCompliance, ciscoHealthMonitorGroup=ciscoHealthMonitorGroup, ciscoHealthMonitorLowSeverityFaults=ciscoHealthMonitorLowSeverityFaults, ciscoHealthMonitorCatastrophicFaults=ciscoHealthMonitorCatastrophicFaults, ciscoHealthMonitorHealthNotifyLowThreshold=ciscoHealthMonitorHealthNotifyLowThreshold, ciscoHealthMonitorSubsysName=ciscoHealthMonitorSubsysName)
