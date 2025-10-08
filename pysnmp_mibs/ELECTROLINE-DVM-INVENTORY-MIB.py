#
# PySNMP MIB module ELECTROLINE-DVM-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DVM-INVENTORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dvmInventory, = mibBuilder.importSymbols("ELECTROLINE-DVM-ROOT-MIB", "dvmInventory")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("ELECTROLINE-DVM-INVENTORY-MIB", dvmInvHwDrvRev=dvmInvHwDrvRev, dvmModelNumber=dvmModelNumber, dvmMfcTestSwVersion=dvmMfcTestSwVersion, dvmMfcDateTime=dvmMfcDateTime, dvmInvHwType=dvmInvHwType, dvmInvHwMinorRev=dvmInvHwMinorRev, dvmInvHwMajorRev=dvmInvHwMajorRev, dvmManufacturingInfo=dvmManufacturingInfo)
