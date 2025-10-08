#
# PySNMP MIB module CISCO-ENTITY-SENSOR-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-SENSOR-HISTORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
EntitySensorValue, = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
ciscoEntitySensorHistoryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 768))
ciscoEntitySensorHistoryMIB.setRevisions(('2011-03-04 00:00',))
if mibBuilder.loadTexts: ciscoEntitySensorHistoryMIB.setLastUpdated('201103040000Z')
if mibBuilder.loadTexts: ciscoEntitySensorHistoryMIB.setOrganization('Cisco Systems, Inc.')
class SensorHistoryCollectionAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("measured", 3), ("algoSMA", 4))

ciscoEntitySensorHistoryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 768, 0))
ciscoEntitySensorHistoryMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 768, 1))
ceshCollectionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1), )
if mibBuilder.loadTexts: ceshCollectionTable.setStatus('current')
ceshCollectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalTime"))
if mibBuilder.loadTexts: ceshCollectionEntry.setStatus('current')
ceshCollectionIntervalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('seconds')
if mibBuilder.loadTexts: ceshCollectionIntervalTime.setStatus('current')
ceshCollectionIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 2), Gauge32()).setUnits('intervals').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionIntervals.setStatus('current')
ceshCollectionInvalidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 3), Gauge32()).setUnits('intervals').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionInvalidIntervals.setStatus('current')
ceshCollectionMaxIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('intervals').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionMaxIntervals.setStatus('current')
ceshCollectionElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 5), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionElapsedTime.setStatus('current')
ceshCollectionAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 6), SensorHistoryCollectionAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionAlgorithm.setStatus('current')
ceshCollectionIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2), )
if mibBuilder.loadTexts: ceshCollectionIntervalTable.setStatus('current')
ceshCollectionIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalTime"), (0, "CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalNumber"))
if mibBuilder.loadTexts: ceshCollectionIntervalEntry.setStatus('current')
ceshCollectionIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ceshCollectionIntervalNumber.setStatus('current')
ceshCollectionIntervalSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1, 2), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionIntervalSensorValue.setStatus('current')
ceshCollectionIntervalTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionIntervalTimeStamp.setStatus('current')
ciscoEntitySensorHistoryMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 1))
ciscoEntitySensorHistoryMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 2))
ciscoEntitySensorHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionGroup"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntitySensorHistoryCompliance = ciscoEntitySensorHistoryCompliance.setStatus('current')
ceshCollectionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionElapsedTime"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervals"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionInvalidIntervals"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionAlgorithm"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionMaxIntervals"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceshCollectionGroup = ceshCollectionGroup.setStatus('current')
ceshCollectionIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalTimeStamp"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalSensorValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceshCollectionIntervalGroup = ceshCollectionIntervalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-HISTORY-MIB", ceshCollectionTable=ceshCollectionTable, ceshCollectionGroup=ceshCollectionGroup, ceshCollectionIntervalSensorValue=ceshCollectionIntervalSensorValue, ceshCollectionIntervalTime=ceshCollectionIntervalTime, PYSNMP_MODULE_ID=ciscoEntitySensorHistoryMIB, ciscoEntitySensorHistoryMIBObjects=ciscoEntitySensorHistoryMIBObjects, ciscoEntitySensorHistoryMIBGroups=ciscoEntitySensorHistoryMIBGroups, ceshCollectionIntervalGroup=ceshCollectionIntervalGroup, ceshCollectionAlgorithm=ceshCollectionAlgorithm, ceshCollectionIntervalTimeStamp=ceshCollectionIntervalTimeStamp, ciscoEntitySensorHistoryMIB=ciscoEntitySensorHistoryMIB, ciscoEntitySensorHistoryMIBCompliances=ciscoEntitySensorHistoryMIBCompliances, ceshCollectionElapsedTime=ceshCollectionElapsedTime, ceshCollectionEntry=ceshCollectionEntry, SensorHistoryCollectionAlgorithm=SensorHistoryCollectionAlgorithm, ceshCollectionInvalidIntervals=ceshCollectionInvalidIntervals, ceshCollectionMaxIntervals=ceshCollectionMaxIntervals, ceshCollectionIntervals=ceshCollectionIntervals, ceshCollectionIntervalEntry=ceshCollectionIntervalEntry, ciscoEntitySensorHistoryMIBConform=ciscoEntitySensorHistoryMIBConform, ciscoEntitySensorHistoryCompliance=ciscoEntitySensorHistoryCompliance, ceshCollectionIntervalTable=ceshCollectionIntervalTable, ceshCollectionIntervalNumber=ceshCollectionIntervalNumber)
