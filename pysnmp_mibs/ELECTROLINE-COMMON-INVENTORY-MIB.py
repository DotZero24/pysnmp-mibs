#
# PySNMP MIB module ELECTROLINE-COMMON-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/ELECTROLINE-COMMON-INVENTORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
commonInventory, = mibBuilder.importSymbols("ELECTROLINE-COMMON-ROOT-MIB", "commonInventory")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELECTROLINE-COMMON-INVENTORY-MIB", invHwMinorRev=invHwMinorRev, invHwMajorRev=invHwMajorRev, invHwType=invHwType, manufacturingInfo=manufacturingInfo, mfcTestSwVersion=mfcTestSwVersion, invHwDrvRev=invHwDrvRev, modelNumber=modelNumber, mfcDateTime=mfcDateTime)
