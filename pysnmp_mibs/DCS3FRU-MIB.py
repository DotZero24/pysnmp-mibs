#
# PySNMP MIB module DCS3FRU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dell/DCS3FRU-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DCS3FRU-MIB", fruTable=fruTable, fruInformationState=fruInformationState, fruAssetTagName=fruAssetTagName, DellUnsigned8BitRange=DellUnsigned8BitRange, DellUnsigned32BitRange=DellUnsigned32BitRange, fruDeviceName=fruDeviceName, DellStatus=DellStatus, dell=dell, fruManufacturingDateName=fruManufacturingDateName, fruManufacturerName=fruManufacturerName, fruRevisionName=fruRevisionName, fruIndex=fruIndex, fruPartNumberName=fruPartNumberName, DellUnsigned16BitRange=DellUnsigned16BitRange, fruSerialNumberName=fruSerialNumberName, DellObjectRange=DellObjectRange, fruInformationStatus=fruInformationStatus, baseboardGroup=baseboardGroup, DellDateName=DellDateName, fruGroup=fruGroup, fruChassisIndex=fruChassisIndex, fruTableEntry=fruTableEntry, DellFRUInformationState=DellFRUInformationState, server3=server3)
