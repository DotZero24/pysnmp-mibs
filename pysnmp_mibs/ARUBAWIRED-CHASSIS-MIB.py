#
# PySNMP MIB module ARUBAWIRED-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredChassisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11))
arubaWiredChassisMIB.setRevisions(('2023-06-27 00:00', '2023-06-06 00:00', '2021-01-11 00:00', '2020-02-13 00:00', '2020-01-07 00:00',))
if mibBuilder.loadTexts: arubaWiredChassisMIB.setLastUpdated('202306270000Z')
if mibBuilder.loadTexts: arubaWiredChassisMIB.setOrganization('HPE/Aruba Networking Division')
arubaWiredPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2))
arubaWiredTempSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3))
arubaWiredFanTray = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4))
arubaWiredFan = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5))
arubaWiredModule = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6))
arubaWiredLedLocator = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7))
arubaWiredPowerStat = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8))
mibBuilder.exportSymbols("ARUBAWIRED-CHASSIS-MIB", arubaWiredTempSensor=arubaWiredTempSensor, arubaWiredFan=arubaWiredFan, arubaWiredPowerStat=arubaWiredPowerStat, arubaWiredPowerSupply=arubaWiredPowerSupply, arubaWiredModule=arubaWiredModule, arubaWiredChassisMIB=arubaWiredChassisMIB, arubaWiredLedLocator=arubaWiredLedLocator, PYSNMP_MODULE_ID=arubaWiredChassisMIB, arubaWiredFanTray=arubaWiredFanTray)
