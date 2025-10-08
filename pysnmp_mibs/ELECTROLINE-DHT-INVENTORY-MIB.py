#
# PySNMP MIB module ELECTROLINE-DHT-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DHT-INVENTORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dhtInventory, = mibBuilder.importSymbols("ELECTROLINE-DHT-ROOT-MIB", "dhtInventory")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
dhtInvHwType = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtInvHwType.setStatus('current')
dhtInvHwMinorRev = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtInvHwMinorRev.setStatus('current')
dhtInvHwMajorRev = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtInvHwMajorRev.setStatus('current')
dhtInvHwDrvRev = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtInvHwDrvRev.setStatus('current')
dhtModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtModelNumber.setStatus('current')
dhtManufacturingInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 10))
if mibBuilder.loadTexts: dhtManufacturingInfo.setStatus('current')
dhtMfcDateTime = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 10, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtMfcDateTime.setStatus('current')
dhtMfcTestSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 10, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtMfcTestSwVersion.setStatus('current')
dhtMfcJobNumber = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 10, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtMfcJobNumber.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-DHT-INVENTORY-MIB", dhtInvHwType=dhtInvHwType, dhtMfcTestSwVersion=dhtMfcTestSwVersion, dhtInvHwDrvRev=dhtInvHwDrvRev, dhtMfcDateTime=dhtMfcDateTime, dhtInvHwMinorRev=dhtInvHwMinorRev, dhtManufacturingInfo=dhtManufacturingInfo, dhtMfcJobNumber=dhtMfcJobNumber, dhtModelNumber=dhtModelNumber, dhtInvHwMajorRev=dhtInvHwMajorRev)
