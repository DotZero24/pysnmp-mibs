#
# PySNMP MIB module CISCOSB-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciscosb/CISCOSB-SENSOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:56:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rlEnv, = mibBuilder.importSymbols("CISCOSB-MIB", "rlEnv")
entityPhysicalGroup, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entityPhysicalGroup", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
entitySensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2))
entitySensorMIB.setRevisions(('2002-10-16 00:00',))
if mibBuilder.loadTexts: entitySensorMIB.setLastUpdated('200210160000Z')
if mibBuilder.loadTexts: entitySensorMIB.setOrganization('Cisco Systems, Inc.')
entitySensorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1))
entitySensorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 3))
class EntitySensorDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), ("rpm", 10), ("cmm", 11), ("truthvalue", 12))

class EntitySensorDataScale(TextualConvention, Integer32):
    reference = 'TBD'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class EntitySensorPrecision(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-8, 9)

class EntitySensorValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class EntitySensorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3))

entPhySensorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1), )
if mibBuilder.loadTexts: entPhySensorTable.setStatus('current')
entPhySensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entPhySensorEntry.setStatus('current')
entPhySensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1, 1, 1), EntitySensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorType.setStatus('current')
entPhySensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1, 1, 2), EntitySensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorScale.setStatus('current')
entPhySensorPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1, 1, 3), EntitySensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorPrecision.setStatus('current')
entPhySensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValue.setStatus('current')
entPhySensorOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1, 1, 5), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorOperStatus.setStatus('current')
entPhySensorUnitsDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorUnitsDisplay.setStatus('current')
entPhySensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueTimeStamp.setStatus('current')
entPhySensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 1, 1, 1, 8), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueUpdateRate.setStatus('current')
entitySensorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 3, 1))
entitySensorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 3, 2))
entitySensorCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 3, 1, 1)).setObjects(("CISCOSB-SENSOR-MIB", "entitySensorValueGroup"), ("ENTITY-MIB", "entityPhysicalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorCompliance = entitySensorCompliance.setStatus('current')
entitySensorValueGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 2, 3, 2, 1)).setObjects(("CISCOSB-SENSOR-MIB", "entPhySensorType"), ("CISCOSB-SENSOR-MIB", "entPhySensorScale"), ("CISCOSB-SENSOR-MIB", "entPhySensorPrecision"), ("CISCOSB-SENSOR-MIB", "entPhySensorValue"), ("CISCOSB-SENSOR-MIB", "entPhySensorOperStatus"), ("CISCOSB-SENSOR-MIB", "entPhySensorUnitsDisplay"), ("CISCOSB-SENSOR-MIB", "entPhySensorValueTimeStamp"), ("CISCOSB-SENSOR-MIB", "entPhySensorValueUpdateRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroup = entitySensorValueGroup.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SENSOR-MIB", entitySensorCompliance=entitySensorCompliance, entPhySensorType=entPhySensorType, entPhySensorValue=entPhySensorValue, EntitySensorValue=EntitySensorValue, entPhySensorScale=entPhySensorScale, entitySensorCompliances=entitySensorCompliances, EntitySensorPrecision=EntitySensorPrecision, entPhySensorOperStatus=entPhySensorOperStatus, entitySensorValueGroup=entitySensorValueGroup, EntitySensorDataScale=EntitySensorDataScale, entitySensorConformance=entitySensorConformance, PYSNMP_MODULE_ID=entitySensorMIB, entPhySensorEntry=entPhySensorEntry, entPhySensorPrecision=entPhySensorPrecision, EntitySensorStatus=EntitySensorStatus, entPhySensorValueTimeStamp=entPhySensorValueTimeStamp, entPhySensorValueUpdateRate=entPhySensorValueUpdateRate, entitySensorMIB=entitySensorMIB, entPhySensorUnitsDisplay=entPhySensorUnitsDisplay, entitySensorGroups=entitySensorGroups, entitySensorObjects=entitySensorObjects, EntitySensorDataType=EntitySensorDataType, entPhySensorTable=entPhySensorTable)
