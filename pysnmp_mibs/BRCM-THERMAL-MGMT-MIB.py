#
# PySNMP MIB module BRCM-THERMAL-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-THERMAL-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataMgmtMIBObjects, = mibBuilder.importSymbols("BRCM-CABLEDATA-MGMT-MIB", "cableDataMgmtMIBObjects")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BRCM-THERMAL-MGMT-MIB", thermalNotificationDelay=thermalNotificationDelay, thermalPowerOnThreshold=thermalPowerOnThreshold, thermalMgmt=thermalMgmt, PYSNMP_MODULE_ID=thermalMgmt, thermalPowerOffDelay=thermalPowerOffDelay, thermalCurrentTemperature=thermalCurrentTemperature, thermalPowerOnDelay=thermalPowerOnDelay, thermalMgmtBase=thermalMgmtBase, thermalPowerOffThreshold=thermalPowerOffThreshold, thermalMonitorInitialized=thermalMonitorInitialized)
