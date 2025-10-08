#
# PySNMP MIB module ELTEX-MES-ISS-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-COPY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
eltMesIssCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15))
eltMesIssCopyMIB.setRevisions(('2019-05-02 00:00',))
if mibBuilder.loadTexts: eltMesIssCopyMIB.setLastUpdated('201906250000Z')
if mibBuilder.loadTexts: eltMesIssCopyMIB.setOrganization('Eltex Enterprise, Ltd.')
class EltMesCopyLocationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tftp", 1), ("sftp", 2))

class EltMesBackupUserStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("starting", 1), ("stopped", 2))

class EltMesCopyError(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("no-error", 1), ("send-failed", 2), ("save-failed", 3))

eltMesIssCopyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1))
eltMesIssCopyBackup = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1))
eltMesIssCopyGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 2))
eltMesIssBackupConfigs = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1))
eltMesIssBackupStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2))
eltMesLastCopyError = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 2, 1), EltMesCopyError()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesLastCopyError.setStatus('current')
eltMesBackupAutoEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesBackupAutoEnable.setStatus('current')
eltMesBackupAutoTimeout = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 2), Unsigned32().clone(720)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesBackupAutoTimeout.setStatus('current')
eltMesBackupAutoFilePath = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesBackupAutoFilePath.setStatus('current')
eltMesBackupAutoServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesBackupAutoServerAddress.setStatus('current')
eltMesBackupAutoOnWrite = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesBackupAutoOnWrite.setStatus('current')
eltMesBackupUserStartAction = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 6), EltMesBackupUserStatus().clone('stopped')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesBackupUserStartAction.setStatus('current')
eltMesBackupHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesBackupHistoryEnable.setStatus('current')
eltMesBackupClearAction = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("clearNow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesBackupClearAction.setStatus('current')
eltMesBackupHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1), )
if mibBuilder.loadTexts: eltMesBackupHistoryTable.setStatus('current')
eltMesBackupHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1), ).setIndexNames((0, "ELTEX-MES-ISS-COPY-MIB", "eltMesBackupHistoryIndex"))
if mibBuilder.loadTexts: eltMesBackupHistoryEntry.setStatus('current')
eltMesBackupHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: eltMesBackupHistoryIndex.setStatus('current')
eltMesBackupHistoryDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesBackupHistoryDateTime.setStatus('current')
eltMesBackupHistoryDstLocationType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 3), EltMesCopyLocationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesBackupHistoryDstLocationType.setStatus('current')
eltMesBackupHistoryServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesBackupHistoryServerAddr.setStatus('current')
eltMesBackupHistoryFilePath = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesBackupHistoryFilePath.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-COPY-MIB", eltMesIssBackupStatistics=eltMesIssBackupStatistics, eltMesBackupHistoryDateTime=eltMesBackupHistoryDateTime, eltMesLastCopyError=eltMesLastCopyError, eltMesBackupHistoryEnable=eltMesBackupHistoryEnable, eltMesIssCopyGlobal=eltMesIssCopyGlobal, eltMesBackupHistoryServerAddr=eltMesBackupHistoryServerAddr, eltMesBackupAutoTimeout=eltMesBackupAutoTimeout, EltMesCopyLocationType=EltMesCopyLocationType, PYSNMP_MODULE_ID=eltMesIssCopyMIB, eltMesBackupHistoryDstLocationType=eltMesBackupHistoryDstLocationType, EltMesCopyError=EltMesCopyError, eltMesIssCopyBackup=eltMesIssCopyBackup, eltMesIssCopyMIB=eltMesIssCopyMIB, eltMesBackupAutoFilePath=eltMesBackupAutoFilePath, eltMesBackupAutoOnWrite=eltMesBackupAutoOnWrite, eltMesBackupUserStartAction=eltMesBackupUserStartAction, eltMesBackupAutoServerAddress=eltMesBackupAutoServerAddress, eltMesBackupHistoryFilePath=eltMesBackupHistoryFilePath, eltMesBackupHistoryEntry=eltMesBackupHistoryEntry, EltMesBackupUserStatus=EltMesBackupUserStatus, eltMesBackupAutoEnable=eltMesBackupAutoEnable, eltMesBackupHistoryTable=eltMesBackupHistoryTable, eltMesBackupClearAction=eltMesBackupClearAction, eltMesBackupHistoryIndex=eltMesBackupHistoryIndex, eltMesIssBackupConfigs=eltMesIssBackupConfigs, eltMesIssCopyObjects=eltMesIssCopyObjects)
