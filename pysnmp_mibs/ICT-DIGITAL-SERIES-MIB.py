#
# PySNMP MIB module ICT-DIGITAL-SERIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ict/ICT-DIGITAL-SERIES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ictPower = MibIdentifier((1, 3, 6, 1, 4, 1, 39145))
digitalSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 39145, 11))
deviceModel = MibScalar((1, 3, 6, 1, 4, 1, 39145, 11, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceModel.setStatus('mandatory')
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 39145, 11, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceName.setStatus('mandatory')
deviceHardware = MibScalar((1, 3, 6, 1, 4, 1, 39145, 11, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHardware.setStatus('mandatory')
deviceFirmware = MibScalar((1, 3, 6, 1, 4, 1, 39145, 11, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceFirmware.setStatus('mandatory')
deviceMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 39145, 11, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceMacAddress.setStatus('mandatory')
inputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 39145, 11, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inputVoltage.setStatus('mandatory')
outputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 39145, 11, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outputVoltage.setStatus('mandatory')
outputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 39145, 11, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outputCurrent.setStatus('mandatory')
outputEnable = MibScalar((1, 3, 6, 1, 4, 1, 39145, 11, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ENABLED", 1), ("DISABLED", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: outputEnable.setStatus('mandatory')
mibBuilder.exportSymbols("ICT-DIGITAL-SERIES-MIB", inputVoltage=inputVoltage, deviceName=deviceName, ictPower=ictPower, deviceFirmware=deviceFirmware, outputCurrent=outputCurrent, deviceHardware=deviceHardware, outputVoltage=outputVoltage, outputEnable=outputEnable, deviceMacAddress=deviceMacAddress, deviceModel=deviceModel, digitalSeries=digitalSeries)
