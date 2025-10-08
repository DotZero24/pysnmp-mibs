#
# PySNMP MIB module CUMULUS-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cumulus/CUMULUS-SENSOR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cumulusMib, = mibBuilder.importSymbols("CUMULUS-SNMP-MIB", "cumulusMib")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
agentSwitchSensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 40310, 6))
if mibBuilder.loadTexts: agentSwitchSensorMIB.setLastUpdated('200212160000Z')
if mibBuilder.loadTexts: agentSwitchSensorMIB.setOrganization('Cumulus sensor MIB')
entitySensorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 40310, 6, 1))
class EntitySensorDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), ("rpm", 10), ("cmm", 11), ("truthvalue", 12))

class EntitySensorDataScale(TextualConvention, Integer32):
    reference = 'The International System of Units (SI), National Institute of Standards and Technology, Spec. Publ. 330, August 1991.'
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

class EntitySensorAlarm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("normal", 3), ("warning", 4), ("alert", 5), ("critical", 6), ("NotPresent", 7), ("NotOperational", 8), ("unavailable", 9))

class EntityAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("off", 0), ("on", 1), ("notApplicable", 2))

entPhySensorTable = MibTable((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1), )
if mibBuilder.loadTexts: entPhySensorTable.setStatus('current')
entPhySensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1), ).setIndexNames((0, "CUMULUS-SENSOR-MIB", "entPhySensorIndex"))
if mibBuilder.loadTexts: entPhySensorEntry.setStatus('current')
entPhySensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorIndex.setStatus('current')
entPhySensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 2), EntitySensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorType.setStatus('current')
entPhySensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 3), EntitySensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorScale.setStatus('current')
entPhySensorPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 4), EntitySensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorPrecision.setStatus('current')
entPhySensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 5), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValue.setStatus('current')
entPhySensorOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 6), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorOperStatus.setStatus('current')
entPhySensorUnitsDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorUnitsDisplay.setStatus('current')
entPhySensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueTimeStamp.setStatus('current')
entPhySensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 9), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueUpdateRate.setStatus('current')
entPhySensorDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorDescr.setStatus('current')
entPhySensorMin = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 11), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorMin.setStatus('current')
entPhySensorMax = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 12), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorMax.setStatus('current')
entPhySensorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 13), EntitySensorAlarm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorAlarm.setStatus('current')
entPhySensorAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 14), EntityAdminStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorAdminStatus.setStatus('current')
mibBuilder.exportSymbols("CUMULUS-SENSOR-MIB", entPhySensorAdminStatus=entPhySensorAdminStatus, entPhySensorPrecision=entPhySensorPrecision, EntitySensorPrecision=EntitySensorPrecision, entPhySensorMin=entPhySensorMin, EntitySensorDataType=EntitySensorDataType, PYSNMP_MODULE_ID=agentSwitchSensorMIB, entPhySensorIndex=entPhySensorIndex, entPhySensorUnitsDisplay=entPhySensorUnitsDisplay, entPhySensorTable=entPhySensorTable, entPhySensorMax=entPhySensorMax, entPhySensorScale=entPhySensorScale, EntitySensorStatus=EntitySensorStatus, entitySensorObjects=entitySensorObjects, entPhySensorValueUpdateRate=entPhySensorValueUpdateRate, EntitySensorAlarm=EntitySensorAlarm, agentSwitchSensorMIB=agentSwitchSensorMIB, entPhySensorDescr=entPhySensorDescr, entPhySensorEntry=entPhySensorEntry, entPhySensorOperStatus=entPhySensorOperStatus, entPhySensorValue=entPhySensorValue, entPhySensorType=entPhySensorType, EntityAdminStatus=EntityAdminStatus, entPhySensorAlarm=entPhySensorAlarm, EntitySensorDataScale=EntitySensorDataScale, EntitySensorValue=EntitySensorValue, entPhySensorValueTimeStamp=entPhySensorValueTimeStamp)
