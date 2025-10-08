#
# PySNMP MIB module ICT-DIGITAL-SERIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ict/ICT-DIGITAL-SERIES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ICT-DIGITAL-SERIES-MIB", deviceMacAddress=deviceMacAddress, outputCurrent=outputCurrent, digitalSeries=digitalSeries, deviceName=deviceName, deviceFirmware=deviceFirmware, inputVoltage=inputVoltage, outputEnable=outputEnable, ictPower=ictPower, outputVoltage=outputVoltage, deviceHardware=deviceHardware, deviceModel=deviceModel)
