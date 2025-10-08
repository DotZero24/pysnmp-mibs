#
# PySNMP MIB module CISCO-ENTITY-SENSOR-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-SENSOR-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:27:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, entPhysicalName, entPhysicalDescr = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalName", "entPhysicalDescr")
entPhySensorType, entPhySensorValue, EntitySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "entPhySensorType", "entPhySensorValue", "EntitySensorValue")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoEntitySensorExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 745))
ciscoEntitySensorExtMIB.setRevisions(('2010-06-09 00:00',))
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setLastUpdated('201006100000Z')
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoEntitySensorExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 0))
ciscoEntitySensorExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 1))
ciscoEntitySensorExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2))
class CiscoSensorThresholdSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30))
    namedValues = NamedValues(("other", 1), ("minor", 10), ("major", 20), ("critical", 30))

class CiscoSensorThresholdRelation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("lessThan", 1), ("lessOrEqual", 2), ("greaterThan", 3), ("greaterOrEqual", 4), ("equalTo", 5), ("notEqualTo", 6))

ceSensorExtThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1), )
if mibBuilder.loadTexts: ceSensorExtThresholdTable.setStatus('current')
ceSensorExtThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdIndex"))
if mibBuilder.loadTexts: ceSensorExtThresholdEntry.setStatus('current')
ceSensorExtThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ceSensorExtThresholdIndex.setStatus('current')
ceSensorExtThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 2), CiscoSensorThresholdSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdSeverity.setStatus('current')
ceSensorExtThresholdRelation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 3), CiscoSensorThresholdRelation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdRelation.setStatus('current')
ceSensorExtThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdValue.setStatus('current')
ceSensorExtThresholdEvaluation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceSensorExtThresholdEvaluation.setStatus('current')
ceSensorExtThresholdNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("transparent", 3))).clone('transparent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdNotifEnable.setStatus('current')
ciscoEntSensorExtGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2))
ceSensorExtThresholdNotifGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdNotifGlobalEnable.setStatus('current')
ceSensorExtThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 745, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("ENTITY-SENSOR-MIB", "entPhySensorType"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"))
if mibBuilder.loadTexts: ceSensorExtThresholdNotification.setStatus('current')
ciscoEntSensorExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1))
ciscoEntSensorExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2))
ciscoEntSensorExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtThresholdGroup"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtNotificationCtrlGroup"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtMIBCompliance = ciscoEntSensorExtMIBCompliance.setStatus('current')
ciscoEntSensorExtThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdSeverity"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdRelation"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdEvaluation"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtThresholdGroup = ciscoEntSensorExtThresholdGroup.setStatus('current')
ciscoEntSensorExtNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtNotificationGroup = ciscoEntSensorExtNotificationGroup.setStatus('current')
ciscoEntSensorExtNotificationCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 3)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifGlobalEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtNotificationCtrlGroup = ciscoEntSensorExtNotificationCtrlGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-EXT-MIB", ciscoEntitySensorExtMIB=ciscoEntitySensorExtMIB, PYSNMP_MODULE_ID=ciscoEntitySensorExtMIB, ciscoEntSensorExtMIBCompliance=ciscoEntSensorExtMIBCompliance, ceSensorExtThresholdRelation=ceSensorExtThresholdRelation, ceSensorExtThresholdSeverity=ceSensorExtThresholdSeverity, ceSensorExtThresholdEntry=ceSensorExtThresholdEntry, ceSensorExtThresholdValue=ceSensorExtThresholdValue, ceSensorExtThresholdTable=ceSensorExtThresholdTable, ceSensorExtThresholdNotifEnable=ceSensorExtThresholdNotifEnable, ciscoEntSensorExtNotificationGroup=ciscoEntSensorExtNotificationGroup, ceSensorExtThresholdNotifGlobalEnable=ceSensorExtThresholdNotifGlobalEnable, ciscoEntitySensorExtMIBObjects=ciscoEntitySensorExtMIBObjects, ciscoEntitySensorExtMIBNotifs=ciscoEntitySensorExtMIBNotifs, ciscoEntSensorExtGlobalObjects=ciscoEntSensorExtGlobalObjects, ceSensorExtThresholdNotification=ceSensorExtThresholdNotification, ciscoEntSensorExtThresholdGroup=ciscoEntSensorExtThresholdGroup, ceSensorExtThresholdEvaluation=ceSensorExtThresholdEvaluation, ciscoEntSensorExtMIBCompliances=ciscoEntSensorExtMIBCompliances, ciscoEntSensorExtMIBGroups=ciscoEntSensorExtMIBGroups, CiscoSensorThresholdRelation=CiscoSensorThresholdRelation, CiscoSensorThresholdSeverity=CiscoSensorThresholdSeverity, ciscoEntitySensorExtMIBConform=ciscoEntitySensorExtMIBConform, ciscoEntSensorExtNotificationCtrlGroup=ciscoEntSensorExtNotificationCtrlGroup, ceSensorExtThresholdIndex=ceSensorExtThresholdIndex)
