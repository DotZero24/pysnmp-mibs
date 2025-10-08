#
# PySNMP MIB module CISCO-PORT-STORM-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-PORT-STORM-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TruthValue", "TextualConvention")
ciscoPortStormControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 362))
ciscoPortStormControlMIB.setRevisions(('2007-10-19 00:00', '2003-07-03 00:00',))
if mibBuilder.loadTexts: ciscoPortStormControlMIB.setLastUpdated('200710190000Z')
if mibBuilder.loadTexts: ciscoPortStormControlMIB.setOrganization('Cisco Systems, Inc.')
ciscoPortStormControlMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 0))
ciscoPortStormControlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 1))
ciscoPortStormControlMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 2))
cpscConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1))
cpscStatusObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2))
class CPortStormControlTrafficType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("broadcast", 1), ("multicast", 2), ("unicast", 3), ("all", 4))

class CPortStormControlActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("filter", 1), ("shutdown", 2))

class CPortStormControlStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("inactive", 1), ("forwarding", 2), ("trafficTypeFiltered", 3), ("allTrafficFiltered", 4), ("shutdown", 5))

cpscThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1), )
if mibBuilder.loadTexts: cpscThresholdTable.setStatus('current')
cpscThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscTrafficType"))
if mibBuilder.loadTexts: cpscThresholdEntry.setStatus('current')
cpscTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1, 1), CPortStormControlTrafficType())
if mibBuilder.loadTexts: cpscTrafficType.setStatus('current')
cpscUpperThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('0.01 Percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscUpperThreshold.setStatus('current')
cpscLowerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('0.01 Percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscLowerThreshold.setStatus('current')
cpscActionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2), )
if mibBuilder.loadTexts: cpscActionTable.setStatus('current')
cpscActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cpscActionEntry.setStatus('current')
cpscAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2, 1, 1), CPortStormControlActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscAction.setStatus('current')
cpscNotificationControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("stormOccurred", 2), ("stormCleared", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscNotificationControl.setStatus('current')
cpscNotificationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('Notifications per Minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscNotificationThreshold.setStatus('current')
cpscStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1), )
if mibBuilder.loadTexts: cpscStatusTable.setStatus('current')
cpscStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscTrafficType"))
if mibBuilder.loadTexts: cpscStatusEntry.setStatus('current')
cpscStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1, 1), CPortStormControlStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscStatus.setStatus('current')
cpscCurrentLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('0.01 Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscCurrentLevel.setStatus('current')
cpscSuppressedPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscSuppressedPacket.setStatus('current')
cpscHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2), )
if mibBuilder.loadTexts: cpscHistoryTable.setStatus('current')
cpscHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryTrafficType"), (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryIndex"))
if mibBuilder.loadTexts: cpscHistoryEntry.setStatus('current')
cpscHistoryTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 1), CPortStormControlTrafficType())
if mibBuilder.loadTexts: cpscHistoryTrafficType.setStatus('current')
cpscHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: cpscHistoryIndex.setStatus('current')
cpscHistoryStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscHistoryStartTime.setStatus('current')
cpscHistoryEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscHistoryEndTime.setStatus('current')
cpscNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 0, 1))
cpscEventRev1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 362, 0, 2)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatus"))
if mibBuilder.loadTexts: cpscEventRev1.setStatus('current')
cpscEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 362, 0, 1, 1)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatus"))
if mibBuilder.loadTexts: cpscEvent.setStatus('deprecated')
ciscoPortStormControlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 1))
ciscoPortStormControlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2))
ciscoPortStormControlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 1, 1)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscConfigurationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotifConfigurationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatusGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatisticsGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortStormControlMIBCompliance = ciscoPortStormControlMIBCompliance.setStatus('deprecated')
ciscoPortStormControlMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 1, 2)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscConfigurationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotifConfigurationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationGroupRev1"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatusGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatisticsGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortStormControlMIBComplianceRev1 = ciscoPortStormControlMIBComplianceRev1.setStatus('current')
cpscConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 1)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscUpperThreshold"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscLowerThreshold"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscConfigurationGroup = cpscConfigurationGroup.setStatus('current')
cpscStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 2)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatus"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscCurrentLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscStatusGroup = cpscStatusGroup.setStatus('current')
cpscNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 3)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscNotificationGroup = cpscNotificationGroup.setStatus('deprecated')
cpscNotifConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 4)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationControl"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscNotifConfigurationGroup = cpscNotifConfigurationGroup.setStatus('current')
cpscStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 5)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscSuppressedPacket"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscStatisticsGroup = cpscStatisticsGroup.setStatus('current')
cpscHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 6)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryStartTime"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryEndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscHistoryGroup = cpscHistoryGroup.setStatus('current')
cpscNotificationGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 7)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscEventRev1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscNotificationGroupRev1 = cpscNotificationGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-PORT-STORM-CONTROL-MIB", cpscNotificationControl=cpscNotificationControl, cpscCurrentLevel=cpscCurrentLevel, cpscEventRev1=cpscEventRev1, cpscActionTable=cpscActionTable, ciscoPortStormControlMIBNotifs=ciscoPortStormControlMIBNotifs, cpscSuppressedPacket=cpscSuppressedPacket, ciscoPortStormControlMIBComplianceRev1=ciscoPortStormControlMIBComplianceRev1, cpscStatus=cpscStatus, cpscStatusEntry=cpscStatusEntry, cpscNotificationThreshold=cpscNotificationThreshold, cpscHistoryStartTime=cpscHistoryStartTime, cpscUpperThreshold=cpscUpperThreshold, CPortStormControlTrafficType=CPortStormControlTrafficType, cpscTrafficType=cpscTrafficType, ciscoPortStormControlMIBCompliances=ciscoPortStormControlMIBCompliances, cpscNotifConfigurationGroup=cpscNotifConfigurationGroup, cpscThresholdTable=cpscThresholdTable, cpscThresholdEntry=cpscThresholdEntry, ciscoPortStormControlMIBConform=ciscoPortStormControlMIBConform, cpscStatusObjects=cpscStatusObjects, cpscConfigObjects=cpscConfigObjects, cpscStatisticsGroup=cpscStatisticsGroup, cpscAction=cpscAction, cpscHistoryEntry=cpscHistoryEntry, cpscHistoryTable=cpscHistoryTable, ciscoPortStormControlMIBCompliance=ciscoPortStormControlMIBCompliance, ciscoPortStormControlMIBObjects=ciscoPortStormControlMIBObjects, PYSNMP_MODULE_ID=ciscoPortStormControlMIB, CPortStormControlActionType=CPortStormControlActionType, cpscStatusTable=cpscStatusTable, cpscHistoryEndTime=cpscHistoryEndTime, ciscoPortStormControlMIBGroups=ciscoPortStormControlMIBGroups, cpscNotificationGroup=cpscNotificationGroup, cpscStatusGroup=cpscStatusGroup, cpscNotificationsPrefix=cpscNotificationsPrefix, cpscEvent=cpscEvent, CPortStormControlStatusType=CPortStormControlStatusType, cpscHistoryIndex=cpscHistoryIndex, cpscHistoryGroup=cpscHistoryGroup, cpscConfigurationGroup=cpscConfigurationGroup, cpscNotificationGroupRev1=cpscNotificationGroupRev1, cpscHistoryTrafficType=cpscHistoryTrafficType, cpscActionEntry=cpscActionEntry, ciscoPortStormControlMIB=ciscoPortStormControlMIB, cpscLowerThreshold=cpscLowerThreshold)
