#
# PySNMP MIB module DCS3FRU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DCS3FRU-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
server3 = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10892))
baseboardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10892, 1))
fruGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000))
class DellObjectRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 128)

class DellUnsigned8BitRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class DellUnsigned16BitRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DellUnsigned32BitRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class DellDateName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(25, 25)
    fixedLength = 25

class DellStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("ok", 3), ("nonCritical", 4), ("critical", 5), ("nonRecoverable", 6))

class DellFRUInformationState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ok", 1), ("notSupported", 2), ("notAvailable", 3), ("checksumInvalid", 4), ("corrupted", 5))

fruTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10), )
if mibBuilder.loadTexts: fruTable.setStatus('mandatory')
fruTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1), ).setIndexNames((0, "DCS3FRU-MIB", "fruChassisIndex"), (0, "DCS3FRU-MIB", "fruIndex"))
if mibBuilder.loadTexts: fruTableEntry.setStatus('mandatory')
fruChassisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 1), DellObjectRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruChassisIndex.setStatus('mandatory')
fruIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 2), DellObjectRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruIndex.setStatus('mandatory')
fruInformationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 3), DellStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruInformationStatus.setStatus('mandatory')
fruInformationState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 4), DellFRUInformationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruInformationState.setStatus('mandatory')
fruDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruDeviceName.setStatus('mandatory')
fruManufacturerName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruManufacturerName.setStatus('mandatory')
fruSerialNumberName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruSerialNumberName.setStatus('mandatory')
fruPartNumberName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruPartNumberName.setStatus('mandatory')
fruRevisionName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruRevisionName.setStatus('mandatory')
fruManufacturingDateName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 10), DellDateName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruManufacturingDateName.setStatus('mandatory')
fruAssetTagName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruAssetTagName.setStatus('mandatory')
mibBuilder.exportSymbols("DCS3FRU-MIB", fruTable=fruTable, fruInformationState=fruInformationState, baseboardGroup=baseboardGroup, dell=dell, fruManufacturingDateName=fruManufacturingDateName, DellFRUInformationState=DellFRUInformationState, fruAssetTagName=fruAssetTagName, DellUnsigned16BitRange=DellUnsigned16BitRange, fruChassisIndex=fruChassisIndex, server3=server3, fruSerialNumberName=fruSerialNumberName, DellStatus=DellStatus, DellUnsigned32BitRange=DellUnsigned32BitRange, fruManufacturerName=fruManufacturerName, DellUnsigned8BitRange=DellUnsigned8BitRange, fruTableEntry=fruTableEntry, fruIndex=fruIndex, fruGroup=fruGroup, DellDateName=DellDateName, DellObjectRange=DellObjectRange, fruRevisionName=fruRevisionName, fruInformationStatus=fruInformationStatus, fruPartNumberName=fruPartNumberName, fruDeviceName=fruDeviceName)
