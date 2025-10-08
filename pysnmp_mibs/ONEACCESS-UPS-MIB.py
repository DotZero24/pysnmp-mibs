#
# PySNMP MIB module ONEACCESS-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-UPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
oacExpIMManagement, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMManagement")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, TimeInterval, TestAndIncr, AutonomousType, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeInterval", "TestAndIncr", "AutonomousType", "TimeStamp", "DisplayString")
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
mibBuilder.exportSymbols("ONEACCESS-UPS-MIB", oacUpsMIB=oacUpsMIB, oacUpsBatteryStatus=oacUpsBatteryStatus, oacUpsTrapAlarmEntryAdded=oacUpsTrapAlarmEntryAdded, oacUpsAlarmDescr=oacUpsAlarmDescr, oacUpsAlarmTime=oacUpsAlarmTime, oacUpsAlarmsPresent=oacUpsAlarmsPresent, oacUpsBattery=oacUpsBattery, oacUpsMIBObjects=oacUpsMIBObjects, oacUpsAlarm=oacUpsAlarm, PYSNMP_MODULE_ID=oacUpsMIB, oacUpsTrapAlarmEntryRemoved=oacUpsTrapAlarmEntryRemoved, oacUpsTraps=oacUpsTraps)
