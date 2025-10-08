#
# PySNMP MIB module CISCO-ENTITY-SENSOR-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-SENSOR-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalDescr, entPhysicalName, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalDescr", "entPhysicalName", "entPhysicalIndex")
entPhySensorType, entPhySensorValue, EntitySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "entPhySensorType", "entPhySensorValue", "EntitySensorValue")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-EXT-MIB", ceSensorExtThresholdTable=ceSensorExtThresholdTable, ceSensorExtThresholdRelation=ceSensorExtThresholdRelation, ceSensorExtThresholdIndex=ceSensorExtThresholdIndex, ciscoEntSensorExtMIBGroups=ciscoEntSensorExtMIBGroups, ceSensorExtThresholdSeverity=ceSensorExtThresholdSeverity, ceSensorExtThresholdNotification=ceSensorExtThresholdNotification, ciscoEntSensorExtGlobalObjects=ciscoEntSensorExtGlobalObjects, ceSensorExtThresholdEntry=ceSensorExtThresholdEntry, ciscoEntitySensorExtMIBNotifs=ciscoEntitySensorExtMIBNotifs, ciscoEntitySensorExtMIB=ciscoEntitySensorExtMIB, ciscoEntSensorExtNotificationGroup=ciscoEntSensorExtNotificationGroup, ciscoEntSensorExtThresholdGroup=ciscoEntSensorExtThresholdGroup, ciscoEntSensorExtMIBCompliance=ciscoEntSensorExtMIBCompliance, ciscoEntitySensorExtMIBConform=ciscoEntitySensorExtMIBConform, ceSensorExtThresholdNotifEnable=ceSensorExtThresholdNotifEnable, ciscoEntitySensorExtMIBObjects=ciscoEntitySensorExtMIBObjects, CiscoSensorThresholdRelation=CiscoSensorThresholdRelation, ceSensorExtThresholdValue=ceSensorExtThresholdValue, ceSensorExtThresholdNotifGlobalEnable=ceSensorExtThresholdNotifGlobalEnable, ceSensorExtThresholdEvaluation=ceSensorExtThresholdEvaluation, CiscoSensorThresholdSeverity=CiscoSensorThresholdSeverity, ciscoEntSensorExtMIBCompliances=ciscoEntSensorExtMIBCompliances, ciscoEntSensorExtNotificationCtrlGroup=ciscoEntSensorExtNotificationCtrlGroup, PYSNMP_MODULE_ID=ciscoEntitySensorExtMIB)
