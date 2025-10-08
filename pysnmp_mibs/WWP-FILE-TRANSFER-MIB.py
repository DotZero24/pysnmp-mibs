#
# PySNMP MIB module WWP-FILE-TRANSFER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/WWP-FILE-TRANSFER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("WWP-FILE-TRANSFER-MIB", wwpFileTransfer=wwpFileTransfer, FileTransferFailCause=FileTransferFailCause, wwpFTransferRemoteFilename=wwpFTransferRemoteFilename, wwpFTransferCmdParseError=wwpFTransferCmdParseError, wwpFTransferNotificationStatus=wwpFTransferNotificationStatus, wwpFTransferFailCause=wwpFTransferFailCause, wwpFileTransferMIBConformance=wwpFileTransferMIBConformance, PYSNMP_MODULE_ID=wwpFileTransferMIB, wwpFileTransferMIBObjects=wwpFileTransferMIBObjects, wwpFiletransferMIBNotifications=wwpFiletransferMIBNotifications, wwpFTransferOp=wwpFTransferOp, FileTransferState=FileTransferState, wwpFileTransferMIB=wwpFileTransferMIB, wwpFileTransferMIBGroups=wwpFileTransferMIBGroups, wwpFileTransferMIBNotificationPrefix=wwpFileTransferMIBNotificationPrefix, wwpFTransferLocalFilename=wwpFTransferLocalFilename, wwpFileTransferMIBCompliances=wwpFileTransferMIBCompliances, wwpFTransferServerAddr=wwpFTransferServerAddr, wwpFTransferCompletion=wwpFTransferCompletion, wwpFTransferStatus=wwpFTransferStatus, wwpFTransferActivate=wwpFTransferActivate, wwpFTransferNotificationInfo=wwpFTransferNotificationInfo, wwpFTransferNotifOnCompletion=wwpFTransferNotifOnCompletion)
