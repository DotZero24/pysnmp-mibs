#
# PySNMP MIB module HIRSCHMANN-WLAN-BATC2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WLAN-BATC2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:55:58 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
batC2, = mibBuilder.importSymbols("HIRSCHMANN-WLAN-LT-MIB", "batC2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, Opaque, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "Opaque", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
batC2MIB = ModuleIdentity((248, 32, 100, 1, 15, 0))
if mibBuilder.loadTexts: batC2MIB.setLastUpdated('201807050000Z')
if mibBuilder.loadTexts: batC2MIB.setOrganization('Hirschmann Automation and Control GmbH')
batc2Trap = MibIdentifier((248, 32, 100, 1, 15, 4))
alarm = NotificationType((248, 32, 100, 1, 15, 4, 1))
if mibBuilder.loadTexts: alarm.setStatus('current')
alarmType = MibScalar((248, 32, 100, 1, 15, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmType.setStatus('current')
alarmValue = MibScalar((248, 32, 100, 1, 15, 4, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmValue.setStatus('current')
mibBuilder.exportSymbols("HIRSCHMANN-WLAN-BATC2-MIB", batc2Trap=batc2Trap, alarm=alarm, alarmValue=alarmValue, alarmType=alarmType, PYSNMP_MODULE_ID=batC2MIB, batC2MIB=batC2MIB)
