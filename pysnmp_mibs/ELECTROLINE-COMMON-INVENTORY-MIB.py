#
# PySNMP MIB module ELECTROLINE-COMMON-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/electroline/ELECTROLINE-COMMON-INVENTORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
commonInventory, = mibBuilder.importSymbols("ELECTROLINE-COMMON-ROOT-MIB", "commonInventory")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
invHwType = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invHwType.setStatus('current')
invHwMinorRev = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invHwMinorRev.setStatus('current')
invHwMajorRev = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invHwMajorRev.setStatus('current')
invHwDrvRev = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invHwDrvRev.setStatus('current')
modelNumber = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: modelNumber.setStatus('current')
manufacturingInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 10))
if mibBuilder.loadTexts: manufacturingInfo.setStatus('current')
mfcDateTime = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 10, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mfcDateTime.setStatus('current')
mfcTestSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 10, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mfcTestSwVersion.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-COMMON-INVENTORY-MIB", mfcTestSwVersion=mfcTestSwVersion, modelNumber=modelNumber, invHwType=invHwType, invHwDrvRev=invHwDrvRev, mfcDateTime=mfcDateTime, manufacturingInfo=manufacturingInfo, invHwMinorRev=invHwMinorRev, invHwMajorRev=invHwMajorRev)
