#
# PySNMP MIB module QTECH-TEMP-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-TEMP-FAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
qtechSystemTemperatureCurrent, = mibBuilder.importSymbols("QTECH-SYSTEM-MIB", "qtechSystemTemperatureCurrent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-TEMP-FAN-MIB", qtechTempFanMIB=qtechTempFanMIB, temperatureTooHighTrap=temperatureTooHighTrap, temperTooHighRecovTrap=temperTooHighRecovTrap, qtechTempFanTraps=qtechTempFanTraps, PYSNMP_MODULE_ID=qtechTempFanMIB, fanFailure=fanFailure)
