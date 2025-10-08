#
# PySNMP MIB module BRCM-THERMAL-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-THERMAL-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataMgmtMIBObjects, = mibBuilder.importSymbols("BRCM-CABLEDATA-MGMT-MIB", "cableDataMgmtMIBObjects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "DateAndTime", "TextualConvention")
thermalMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11))
thermalMgmt.setRevisions(('2007-02-05 00:00', '2006-10-04 00:00',))
if mibBuilder.loadTexts: thermalMgmt.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: thermalMgmt.setOrganization('Broadcom Corporation')
thermalMgmtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1))
thermalCurrentTemperature = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 1), Integer32()).setUnits('degrees C').setMaxAccess("readonly")
if mibBuilder.loadTexts: thermalCurrentTemperature.setStatus('current')
thermalPowerOffThreshold = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(40, 120))).setUnits('degrees C').setMaxAccess("readwrite")
if mibBuilder.loadTexts: thermalPowerOffThreshold.setStatus('current')
thermalPowerOnThreshold = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(40, 120))).setUnits('degrees C').setMaxAccess("readwrite")
if mibBuilder.loadTexts: thermalPowerOnThreshold.setStatus('current')
thermalPowerOnDelay = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 50))).setUnits('250 Milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: thermalPowerOnDelay.setStatus('current')
thermalPowerOffDelay = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 60))).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: thermalPowerOffDelay.setStatus('current')
thermalNotificationDelay = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 60))).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: thermalNotificationDelay.setStatus('current')
thermalMonitorInitialized = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: thermalMonitorInitialized.setStatus('current')
mibBuilder.exportSymbols("BRCM-THERMAL-MGMT-MIB", thermalCurrentTemperature=thermalCurrentTemperature, thermalMgmt=thermalMgmt, thermalPowerOnThreshold=thermalPowerOnThreshold, thermalMonitorInitialized=thermalMonitorInitialized, thermalPowerOnDelay=thermalPowerOnDelay, thermalPowerOffThreshold=thermalPowerOffThreshold, thermalNotificationDelay=thermalNotificationDelay, thermalPowerOffDelay=thermalPowerOffDelay, PYSNMP_MODULE_ID=thermalMgmt, thermalMgmtBase=thermalMgmtBase)
