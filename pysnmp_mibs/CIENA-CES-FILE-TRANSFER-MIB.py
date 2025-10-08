#
# PySNMP MIB module CIENA-CES-FILE-TRANSFER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-CES-FILE-TRANSFER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaGlobalSeverity, cienaGlobalMacAddress = mibBuilder.importSymbols("CIENA-GLOBAL-MIB", "cienaGlobalSeverity", "cienaGlobalMacAddress")
cienaCesConfig, cienaCesNotifications = mibBuilder.importSymbols("CIENA-SMI", "cienaCesConfig", "cienaCesNotifications")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaCesFileTransferMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 2, 1, 15))
cienaCesFileTransferMIB.setRevisions(('2017-06-07 00:00', '2011-02-02 00:00',))
if mibBuilder.loadTexts: cienaCesFileTransferMIB.setLastUpdated('201706070000Z')
if mibBuilder.loadTexts: cienaCesFileTransferMIB.setOrganization('Ciena Corp.')
cienaCesFileTransferMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1))
cienaCesFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1))
cienaCesFileTransferMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 16))
cienaCesFileTransferMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 16, 0))
cienaCesFTransferRemoteFilename = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesFTransferRemoteFilename.setStatus('current')
cienaCesFTransferLocalFilename = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesFTransferLocalFilename.setStatus('current')
cienaCesFTransferNotificationStatus = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0))).clone(namedValues=NamedValues(("fileAlreadyExist", 1), ("tftpServerNotFound", 2), ("fileGetError", 3), ("filePutError", 4), ("fileSystemError", 5), ("fileContentsInvalid", 6), ("flashOffline", 7), ("badFileCrc", 8), ("allFilesSkipped", 9), ("serverIpAddrInvalid", 10), ("filePathInvalid", 11), ("fileNameInvalid", 12), ("sourceNotFound", 13), ("fileNameNeeded", 14), ("notEnoughSpace", 15), ("putSuccessful", 16), ("downloadSuccess", 17), ("internalError", 18), ("noStatus", 0)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesFTransferNotificationStatus.setStatus('current')
cienaCesFTransferNotificationInfo = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesFTransferNotificationInfo.setStatus('current')
cienaCesFTransferCompletion = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 16, 0, 1)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"), ("CIENA-CES-FILE-TRANSFER-MIB", "cienaCesFTransferRemoteFilename"), ("CIENA-CES-FILE-TRANSFER-MIB", "cienaCesFTransferLocalFilename"), ("CIENA-CES-FILE-TRANSFER-MIB", "cienaCesFTransferNotificationStatus"), ("CIENA-CES-FILE-TRANSFER-MIB", "cienaCesFTransferNotificationInfo"))
if mibBuilder.loadTexts: cienaCesFTransferCompletion.setStatus('current')
mibBuilder.exportSymbols("CIENA-CES-FILE-TRANSFER-MIB", cienaCesFileTransfer=cienaCesFileTransfer, cienaCesFTransferNotificationInfo=cienaCesFTransferNotificationInfo, cienaCesFTransferCompletion=cienaCesFTransferCompletion, cienaCesFTransferLocalFilename=cienaCesFTransferLocalFilename, cienaCesFTransferNotificationStatus=cienaCesFTransferNotificationStatus, cienaCesFileTransferMIBNotificationPrefix=cienaCesFileTransferMIBNotificationPrefix, cienaCesFTransferRemoteFilename=cienaCesFTransferRemoteFilename, PYSNMP_MODULE_ID=cienaCesFileTransferMIB, cienaCesFileTransferMIBObjects=cienaCesFileTransferMIBObjects, cienaCesFileTransferMIBNotifications=cienaCesFileTransferMIBNotifications, cienaCesFileTransferMIB=cienaCesFileTransferMIB)
