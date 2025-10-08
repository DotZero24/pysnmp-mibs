#
# PySNMP MIB module MX-LINE-SELECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-LINE-SELECTION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxDigitMap, MxEnableState = mibBuilder.importSymbols("MX-TC", "MxDigitMap", "MxEnableState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-LINE-SELECTION-MIB", lineSelectionMIBObjects=lineSelectionMIBObjects, lineSelectionCompliances=lineSelectionCompliances, lineSelectionGroups=lineSelectionGroups, lineSelectionDigitMap=lineSelectionDigitMap, PYSNMP_MODULE_ID=lineSelectionMIB, lineSelectionIfCustomizationEntry=lineSelectionIfCustomizationEntry, lineSelectionIfCustomizationTable=lineSelectionIfCustomizationTable, lineSelectionCustomizationVer1=lineSelectionCustomizationVer1, lineSelectionComplVer1=lineSelectionComplVer1, lineSelectionEnable=lineSelectionEnable, lineSelectionConformance=lineSelectionConformance, lineSelectionMIB=lineSelectionMIB)
