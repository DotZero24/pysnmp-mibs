#
# PySNMP MIB module QTECH-TEMP-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-TEMP-FAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
qtechSystemTemperatureCurrent, = mibBuilder.importSymbols("QTECH-SYSTEM-MIB", "qtechSystemTemperatureCurrent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechTempFanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109))
qtechTempFanMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: qtechTempFanMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: qtechTempFanMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechTempFanTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109, 1))
temperatureTooHighTrap = NotificationType((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109, 1, 1)).setObjects(("QTECH-SYSTEM-MIB", "qtechSystemTemperatureCurrent"))
if mibBuilder.loadTexts: temperatureTooHighTrap.setStatus('current')
temperTooHighRecovTrap = NotificationType((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109, 1, 2)).setObjects(("QTECH-SYSTEM-MIB", "qtechSystemTemperatureCurrent"))
if mibBuilder.loadTexts: temperTooHighRecovTrap.setStatus('current')
fanFailure = NotificationType((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109, 1, 3))
if mibBuilder.loadTexts: fanFailure.setStatus('current')
mibBuilder.exportSymbols("QTECH-TEMP-FAN-MIB", fanFailure=fanFailure, qtechTempFanTraps=qtechTempFanTraps, PYSNMP_MODULE_ID=qtechTempFanMIB, qtechTempFanMIB=qtechTempFanMIB, temperatureTooHighTrap=temperatureTooHighTrap, temperTooHighRecovTrap=temperTooHighRecovTrap)
