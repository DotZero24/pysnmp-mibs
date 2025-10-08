#
# PySNMP MIB module HIRSCHMANN-WLAN-BATC2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WLAN-BATC2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:55:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
batC2, = mibBuilder.importSymbols("HIRSCHMANN-WLAN-LT-MIB", "batC2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32, Opaque = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "Opaque")
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
mibBuilder.exportSymbols("HIRSCHMANN-WLAN-BATC2-MIB", alarmValue=alarmValue, alarm=alarm, batC2MIB=batC2MIB, batc2Trap=batc2Trap, alarmType=alarmType, PYSNMP_MODULE_ID=batC2MIB)
