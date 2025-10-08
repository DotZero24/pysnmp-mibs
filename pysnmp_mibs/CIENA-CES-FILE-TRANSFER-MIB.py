#
# PySNMP MIB module CIENA-CES-FILE-TRANSFER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-CES-FILE-TRANSFER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaGlobalMacAddress, cienaGlobalSeverity = mibBuilder.importSymbols("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress", "cienaGlobalSeverity")
cienaCesNotifications, cienaCesConfig = mibBuilder.importSymbols("CIENA-SMI", "cienaCesNotifications", "cienaCesConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CIENA-CES-FILE-TRANSFER-MIB", cienaCesFTransferNotificationInfo=cienaCesFTransferNotificationInfo, cienaCesFileTransferMIBNotificationPrefix=cienaCesFileTransferMIBNotificationPrefix, PYSNMP_MODULE_ID=cienaCesFileTransferMIB, cienaCesFileTransferMIB=cienaCesFileTransferMIB, cienaCesFileTransferMIBNotifications=cienaCesFileTransferMIBNotifications, cienaCesFTransferCompletion=cienaCesFTransferCompletion, cienaCesFTransferRemoteFilename=cienaCesFTransferRemoteFilename, cienaCesFileTransferMIBObjects=cienaCesFileTransferMIBObjects, cienaCesFTransferNotificationStatus=cienaCesFTransferNotificationStatus, cienaCesFTransferLocalFilename=cienaCesFTransferLocalFilename, cienaCesFileTransfer=cienaCesFileTransfer)
