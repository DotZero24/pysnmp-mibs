#
# PySNMP MIB module CADANT-CMTS-EXPORTIMPORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arris/CADANT-CMTS-EXPORTIMPORT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
trapSeverity, trapCounter = mibBuilder.importSymbols("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity", "trapCounter")
cadExperimental, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadExperimental")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("CADANT-CMTS-EXPORTIMPORT-MIB", ExportResult=ExportResult, cadCmtsExportResult=cadCmtsExportResult, cadCmtsImportResult=cadCmtsImportResult, cadCmtsExportImportIfIndex=cadCmtsExportImportIfIndex, cadCmtsExportNotification=cadCmtsExportNotification, cadCmtsExportImportFilename=cadCmtsExportImportFilename, cadCmtsExportImportNested=cadCmtsExportImportNested, cadCmtsImportNotification=cadCmtsImportNotification, cadCmtsExportImportTraps=cadCmtsExportImportTraps, cadExportImportMib=cadExportImportMib, cadCmtsExportImportWithLineNums=cadCmtsExportImportWithLineNums, cadCmtsExportImportAction=cadCmtsExportImportAction, cadCmtsExportImportGroup=cadCmtsExportImportGroup, ExportImportAction=ExportImportAction, PYSNMP_MODULE_ID=cadExportImportMib, cadCmtsExportImportWithCertificates=cadCmtsExportImportWithCertificates, ImportResult=ImportResult, cadCmtsExportImportWithDefaults=cadCmtsExportImportWithDefaults)
