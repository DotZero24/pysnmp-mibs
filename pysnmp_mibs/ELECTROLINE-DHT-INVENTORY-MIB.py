#
# PySNMP MIB module ELECTROLINE-DHT-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DHT-INVENTORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dhtInventory, = mibBuilder.importSymbols("ELECTROLINE-DHT-ROOT-MIB", "dhtInventory")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("ELECTROLINE-DHT-INVENTORY-MIB", dhtMfcDateTime=dhtMfcDateTime, dhtManufacturingInfo=dhtManufacturingInfo, dhtInvHwDrvRev=dhtInvHwDrvRev, dhtModelNumber=dhtModelNumber, dhtInvHwMinorRev=dhtInvHwMinorRev, dhtMfcTestSwVersion=dhtMfcTestSwVersion, dhtInvHwMajorRev=dhtInvHwMajorRev, dhtInvHwType=dhtInvHwType, dhtMfcJobNumber=dhtMfcJobNumber)
