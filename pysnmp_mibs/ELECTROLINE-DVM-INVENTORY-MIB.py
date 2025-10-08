#
# PySNMP MIB module ELECTROLINE-DVM-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DVM-INVENTORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dvmInventory, = mibBuilder.importSymbols("ELECTROLINE-DVM-ROOT-MIB", "dvmInventory")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
dvmInvHwType = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmInvHwType.setStatus('current')
dvmInvHwMinorRev = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmInvHwMinorRev.setStatus('current')
dvmInvHwMajorRev = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmInvHwMajorRev.setStatus('current')
dvmInvHwDrvRev = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmInvHwDrvRev.setStatus('current')
dvmModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmModelNumber.setStatus('current')
dvmManufacturingInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 10))
if mibBuilder.loadTexts: dvmManufacturingInfo.setStatus('current')
dvmMfcDateTime = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 10, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmMfcDateTime.setStatus('current')
dvmMfcTestSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 10, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmMfcTestSwVersion.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-DVM-INVENTORY-MIB", dvmMfcDateTime=dvmMfcDateTime, dvmModelNumber=dvmModelNumber, dvmInvHwType=dvmInvHwType, dvmInvHwDrvRev=dvmInvHwDrvRev, dvmInvHwMajorRev=dvmInvHwMajorRev, dvmMfcTestSwVersion=dvmMfcTestSwVersion, dvmManufacturingInfo=dvmManufacturingInfo, dvmInvHwMinorRev=dvmInvHwMinorRev)
