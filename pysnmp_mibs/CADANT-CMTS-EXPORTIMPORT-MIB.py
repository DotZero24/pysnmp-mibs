#
# PySNMP MIB module CADANT-CMTS-EXPORTIMPORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/arris/CADANT-CMTS-EXPORTIMPORT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
trapCounter, trapSeverity = mibBuilder.importSymbols("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter", "trapSeverity")
cadExperimental, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadExperimental")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
cadExportImportMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1))
cadExportImportMib.setRevisions(('2001-03-09 00:00', '2004-02-13 00:00', '2004-02-16 00:00',))
if mibBuilder.loadTexts: cadExportImportMib.setLastUpdated('200402160000Z')
if mibBuilder.loadTexts: cadExportImportMib.setOrganization('Arris International Inc.')
class ExportImportAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("noop", 0), ("export", 1), ("import", 2), ("pCmCertExport", 3), ("caCertExport", 4))

class ExportResult(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("success", 1), ("fileNameTooLong", 2), ("invalidCharactersInFilename", 3), ("fileSystemFull", 4), ("otherError", 5))

class ImportResult(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("success", 1), ("fileNotFound", 2), ("fileDecodingError", 3), ("otherError", 4))

cadCmtsExportImportGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1))
cadCmtsExportImportFilename = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 1), DisplayString().clone('update:/export.txt')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportFilename.setStatus('current')
cadCmtsExportImportAction = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 2), ExportImportAction().clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportAction.setStatus('current')
cadCmtsExportResult = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 3), ExportResult().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCmtsExportResult.setStatus('current')
cadCmtsImportResult = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 4), ImportResult().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCmtsImportResult.setStatus('current')
cadCmtsExportImportWithLineNums = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportWithLineNums.setStatus('current')
cadCmtsExportImportWithDefaults = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportWithDefaults.setStatus('current')
cadCmtsExportImportNested = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportNested.setStatus('current')
cadCmtsExportImportWithCertificates = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportWithCertificates.setStatus('current')
cadCmtsExportImportIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 9), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportIfIndex.setStatus('current')
cadCmtsExportImportTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 0))
cadCmtsExportNotification = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 0, 1)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-EXPORTIMPORT-MIB", "cadCmtsExportResult"))
if mibBuilder.loadTexts: cadCmtsExportNotification.setStatus('current')
cadCmtsImportNotification = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 0, 2)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-EXPORTIMPORT-MIB", "cadCmtsImportResult"))
if mibBuilder.loadTexts: cadCmtsImportNotification.setStatus('current')
mibBuilder.exportSymbols("CADANT-CMTS-EXPORTIMPORT-MIB", cadExportImportMib=cadExportImportMib, cadCmtsExportImportIfIndex=cadCmtsExportImportIfIndex, cadCmtsExportNotification=cadCmtsExportNotification, ImportResult=ImportResult, cadCmtsImportResult=cadCmtsImportResult, ExportResult=ExportResult, PYSNMP_MODULE_ID=cadExportImportMib, cadCmtsExportImportWithLineNums=cadCmtsExportImportWithLineNums, ExportImportAction=ExportImportAction, cadCmtsExportImportGroup=cadCmtsExportImportGroup, cadCmtsExportImportWithCertificates=cadCmtsExportImportWithCertificates, cadCmtsExportImportTraps=cadCmtsExportImportTraps, cadCmtsExportResult=cadCmtsExportResult, cadCmtsExportImportWithDefaults=cadCmtsExportImportWithDefaults, cadCmtsExportImportNested=cadCmtsExportImportNested, cadCmtsExportImportAction=cadCmtsExportImportAction, cadCmtsExportImportFilename=cadCmtsExportImportFilename, cadCmtsImportNotification=cadCmtsImportNotification)
