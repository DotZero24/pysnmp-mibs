#
# PySNMP MIB module MX-LINE-SELECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-LINE-SELECTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxEnableState, MxDigitMap = mibBuilder.importSymbols("MX-TC", "MxEnableState", "MxDigitMap")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lineSelectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 15, 90))
lineSelectionMIB.setRevisions(('1903-03-19 00:00',))
if mibBuilder.loadTexts: lineSelectionMIB.setLastUpdated('0303190000Z')
if mibBuilder.loadTexts: lineSelectionMIB.setOrganization('Mediatrix Telecom, Inc.')
lineSelectionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 90, 1))
lineSelectionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 90, 5))
lineSelectionIfCustomizationTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 15, 90, 1, 10), )
if mibBuilder.loadTexts: lineSelectionIfCustomizationTable.setStatus('current')
lineSelectionIfCustomizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 15, 90, 1, 10, 5), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: lineSelectionIfCustomizationEntry.setStatus('current')
lineSelectionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 90, 1, 10, 5, 5), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lineSelectionEnable.setStatus('current')
lineSelectionDigitMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 90, 1, 10, 5, 10), MxDigitMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lineSelectionDigitMap.setStatus('current')
lineSelectionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 90, 5, 1))
lineSelectionComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 15, 90, 5, 1, 1)).setObjects(("MX-LINE-SELECTION-MIB", "lineSelectionCustomizationVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lineSelectionComplVer1 = lineSelectionComplVer1.setStatus('current')
lineSelectionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 90, 5, 5))
lineSelectionCustomizationVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 15, 90, 5, 5, 10)).setObjects(("MX-LINE-SELECTION-MIB", "lineSelectionEnable"), ("MX-LINE-SELECTION-MIB", "lineSelectionDigitMap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lineSelectionCustomizationVer1 = lineSelectionCustomizationVer1.setStatus('current')
mibBuilder.exportSymbols("MX-LINE-SELECTION-MIB", lineSelectionMIBObjects=lineSelectionMIBObjects, lineSelectionIfCustomizationEntry=lineSelectionIfCustomizationEntry, lineSelectionComplVer1=lineSelectionComplVer1, lineSelectionMIB=lineSelectionMIB, lineSelectionIfCustomizationTable=lineSelectionIfCustomizationTable, lineSelectionCompliances=lineSelectionCompliances, lineSelectionDigitMap=lineSelectionDigitMap, lineSelectionCustomizationVer1=lineSelectionCustomizationVer1, lineSelectionGroups=lineSelectionGroups, lineSelectionConformance=lineSelectionConformance, lineSelectionEnable=lineSelectionEnable, PYSNMP_MODULE_ID=lineSelectionMIB)
