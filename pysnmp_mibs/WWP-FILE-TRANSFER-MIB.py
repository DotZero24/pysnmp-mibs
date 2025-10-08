#
# PySNMP MIB module WWP-FILE-TRANSFER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/WWP-FILE-TRANSFER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpFileTransferMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 7))
wwpFileTransferMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpFileTransferMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpFileTransferMIB.setOrganization('World Wide Packets, Inc')
wwpFileTransferMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1))
wwpFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1))
wwpFileTransferMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 2))
wwpFiletransferMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 2, 0))
wwpFileTransferMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 3))
wwpFileTransferMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 3, 1))
wwpFileTransferMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 3, 2))
class FileTransferState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("idle", 1), ("sending", 2), ("receiving", 3), ("transferComplete", 4), ("failed", 5))

class FileTransferFailCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noStatus", 1), ("timeout", 2), ("networkError", 3), ("noSpace", 4), ("invalidFileName", 5), ("commandCompleted", 6), ("internalError", 7), ("commandFileParseError", 8))

wwpFTransferOp = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("sendFile", 1), ("getFile", 2), ("getCmdFile", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferOp.setStatus('current')
wwpFTransferServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferServerAddr.setStatus('current')
wwpFTransferRemoteFilename = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferRemoteFilename.setStatus('current')
wwpFTransferLocalFilename = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferLocalFilename.setStatus('current')
wwpFTransferActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferActivate.setStatus('current')
wwpFTransferNotifOnCompletion = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferNotifOnCompletion.setStatus('current')
wwpFTransferStatus = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 7), FileTransferState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpFTransferStatus.setStatus('current')
wwpFTransferFailCause = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 8), FileTransferFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpFTransferFailCause.setStatus('current')
wwpFTransferNotificationStatus = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("downloadSuccess", 0), ("tftpServerNotFound", 1), ("couldNotGetFile", 2), ("cmdFileParseError", 3), ("internalFilesystemError", 4), ("inValidFileContents", 5), ("flashOffline", 6), ("noStatus", 7), ("putSuccessful", 8), ("couldNotPutFile", 9), ("badFileCrc", 10), ("allFilesSkipped", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpFTransferNotificationStatus.setStatus('current')
wwpFTransferNotificationInfo = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpFTransferNotificationInfo.setStatus('current')
wwpFTransferCompletion = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 7, 2, 0, 1)).setObjects(("WWP-FILE-TRANSFER-MIB", "wwpFTransferRemoteFilename"), ("WWP-FILE-TRANSFER-MIB", "wwpFTransferLocalFilename"), ("WWP-FILE-TRANSFER-MIB", "wwpFTransferNotificationStatus"), ("WWP-FILE-TRANSFER-MIB", "wwpFTransferNotificationInfo"))
if mibBuilder.loadTexts: wwpFTransferCompletion.setStatus('current')
wwpFTransferCmdParseError = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 7, 2, 0, 2)).setObjects(("WWP-FILE-TRANSFER-MIB", "wwpFTransferRemoteFilename"))
if mibBuilder.loadTexts: wwpFTransferCmdParseError.setStatus('deprecated')
mibBuilder.exportSymbols("WWP-FILE-TRANSFER-MIB", wwpFTransferNotifOnCompletion=wwpFTransferNotifOnCompletion, wwpFiletransferMIBNotifications=wwpFiletransferMIBNotifications, wwpFileTransferMIBConformance=wwpFileTransferMIBConformance, FileTransferFailCause=FileTransferFailCause, wwpFTransferFailCause=wwpFTransferFailCause, wwpFileTransferMIBCompliances=wwpFileTransferMIBCompliances, wwpFTransferServerAddr=wwpFTransferServerAddr, wwpFTransferStatus=wwpFTransferStatus, wwpFTransferCmdParseError=wwpFTransferCmdParseError, wwpFTransferOp=wwpFTransferOp, wwpFileTransferMIBGroups=wwpFileTransferMIBGroups, wwpFTransferNotificationStatus=wwpFTransferNotificationStatus, wwpFTransferLocalFilename=wwpFTransferLocalFilename, wwpFTransferNotificationInfo=wwpFTransferNotificationInfo, wwpFTransferActivate=wwpFTransferActivate, wwpFileTransferMIBObjects=wwpFileTransferMIBObjects, PYSNMP_MODULE_ID=wwpFileTransferMIB, wwpFileTransferMIB=wwpFileTransferMIB, wwpFTransferCompletion=wwpFTransferCompletion, FileTransferState=FileTransferState, wwpFileTransferMIBNotificationPrefix=wwpFileTransferMIBNotificationPrefix, wwpFileTransfer=wwpFileTransfer, wwpFTransferRemoteFilename=wwpFTransferRemoteFilename)
