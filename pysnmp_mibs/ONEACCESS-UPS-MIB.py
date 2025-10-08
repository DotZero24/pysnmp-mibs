#
# PySNMP MIB module ONEACCESS-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-UPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
oacExpIMManagement, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMManagement")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeInterval, TimeStamp, AutonomousType, TestAndIncr, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeInterval", "TimeStamp", "AutonomousType", "TestAndIncr", "TextualConvention")
oacUpsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225))
if mibBuilder.loadTexts: oacUpsMIB.setLastUpdated('9402230000Z')
if mibBuilder.loadTexts: oacUpsMIB.setOrganization('IETF UPS MIB Working Group')
oacUpsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1))
oacUpsBattery = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 1))
oacUpsBatteryStatus = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("batteryNormal", 2), ("batteryLow", 3), ("batteryDepleted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacUpsBatteryStatus.setStatus('current')
oacUpsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2))
oacUpsAlarmsPresent = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacUpsAlarmsPresent.setStatus('current')
oacUpsAlarmDescr = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2, 2), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacUpsAlarmDescr.setStatus('current')
oacUpsAlarmTime = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacUpsAlarmTime.setStatus('current')
oacUpsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 2))
oacUpsTrapAlarmEntryAdded = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 2, 0)).setObjects(("ONEACCESS-UPS-MIB", "oacUpsAlarmDescr"))
if mibBuilder.loadTexts: oacUpsTrapAlarmEntryAdded.setStatus('current')
oacUpsTrapAlarmEntryRemoved = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 2, 1)).setObjects(("ONEACCESS-UPS-MIB", "oacUpsAlarmDescr"))
if mibBuilder.loadTexts: oacUpsTrapAlarmEntryRemoved.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-UPS-MIB", oacUpsAlarmsPresent=oacUpsAlarmsPresent, oacUpsMIB=oacUpsMIB, oacUpsTraps=oacUpsTraps, oacUpsBatteryStatus=oacUpsBatteryStatus, oacUpsAlarmDescr=oacUpsAlarmDescr, oacUpsTrapAlarmEntryRemoved=oacUpsTrapAlarmEntryRemoved, oacUpsMIBObjects=oacUpsMIBObjects, oacUpsBattery=oacUpsBattery, oacUpsAlarm=oacUpsAlarm, oacUpsTrapAlarmEntryAdded=oacUpsTrapAlarmEntryAdded, oacUpsAlarmTime=oacUpsAlarmTime, PYSNMP_MODULE_ID=oacUpsMIB)
