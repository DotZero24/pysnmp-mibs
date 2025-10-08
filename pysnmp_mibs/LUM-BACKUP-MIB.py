#
# PySNMP MIB module LUM-BACKUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-BACKUP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumBackupMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumBackupMIB", "lumModules")
FaultStatus, CommandString = mibBuilder.importSymbols("LUM-TC", "FaultStatus", "CommandString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TestAndIncr, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TestAndIncr", "TruthValue", "DisplayString")
lumBackupMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 7))
lumBackupMIBModule.setRevisions(('2017-12-15 00:00', '2017-06-15 00:00', '2016-01-11 00:00', '2007-01-11 00:00', '2005-12-05 00:00', '2004-12-21 00:00', '2004-12-20 00:00', '2004-11-09 00:00', '2004-10-28 00:00', '2004-09-30 00:00', '2004-06-17 00:00', '2002-10-29 00:00', '2001-10-30 00:00', '2001-08-16 00:00', '2001-08-01 00:00',))
if mibBuilder.loadTexts: lumBackupMIBModule.setLastUpdated('201712150000Z')
if mibBuilder.loadTexts: lumBackupMIBModule.setOrganization('Infinera Corporation')
lumBackupConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1))
lumBackupGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1))
lumBackupCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2))
lumBackupMinimalGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3))
lumBackupMinimalCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4))
lumBackupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2))
backupGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1))
backupFileList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2))
backupCommand = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3))
backupPersistentFileList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4))
backupUpload = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5))
backupSftpUpload = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6))
backupGeneralTestAndIncr = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupGeneralTestAndIncr.setStatus('current')
backupGeneralMibSpecVersion = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupGeneralMibSpecVersion.setStatus('current')
backupGeneralMibImplVersion = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupGeneralMibImplVersion.setStatus('current')
backupGeneralLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralLastChangeTime.setStatus('current')
backupGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralConfigLastChangeTime.setStatus('current')
backupGeneralUnsavedChanges = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralUnsavedChanges.setStatus('current')
backupGeneralFileTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralFileTableSize.setStatus('current')
backupGeneralPersistentFileTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralPersistentFileTableSize.setStatus('current')
backupGeneralInstallConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 9), CommandString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupGeneralInstallConfigFile.setStatus('deprecated')
backupGeneralGlobalStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralGlobalStateLastChangeTime.setStatus('current')
backupGeneralGlobalConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralGlobalConfigLastChangeTime.setStatus('current')
backupGeneralPrimaryFileName = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralPrimaryFileName.setStatus('current')
backupGeneralWarnForUnsaved = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupGeneralWarnForUnsaved.setStatus('current')
backupGeneralWarnUnsavedDelay = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupGeneralWarnUnsavedDelay.setStatus('current')
backupGeneralUnsavedChangesAlarm = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 15), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralUnsavedChangesAlarm.setStatus('current')
backupGeneralSavedConfigurationGenerationId = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupGeneralSavedConfigurationGenerationId.setStatus('current')
backupGeneralBackupScheme = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tftp", 1), ("sftp", 2))).clone('tftp')).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupGeneralBackupScheme.setStatus('current')
backupFileTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1), )
if mibBuilder.loadTexts: backupFileTable.setStatus('current')
backupFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1), ).setIndexNames((0, "LUM-BACKUP-MIB", "backupFileIndex"))
if mibBuilder.loadTexts: backupFileEntry.setStatus('current')
backupFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupFileIndex.setStatus('current')
backupFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupFileName.setStatus('current')
backupFileDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupFileDescr.setStatus('current')
backupFileLastChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupFileLastChangeTime.setStatus('current')
backupFileAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("secondary", 2), ("primary", 3))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupFileAdminStatus.setStatus('current')
backupFileOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("running", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupFileOperStatus.setStatus('current')
backupFileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupFileRowStatus.setStatus('current')
backupFileUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupFileUrl.setStatus('current')
backupCommandName = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupCommandName.setStatus('current')
backupCommandDescr = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupCommandDescr.setStatus('current')
backupCommandAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("secondary", 2), ("primary", 3))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupCommandAdminStatus.setStatus('current')
backupCommandAction = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("saveTofile", 2), ("busy", 3))).clone('idle')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupCommandAction.setStatus('current')
backupCommandResult = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("success", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupCommandResult.setStatus('current')
backupUploadServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupUploadServerAddr.setStatus('current')
backupUploadServerPath = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 2), DisplayString().clone('/upload')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupUploadServerPath.setStatus('current')
backupUploadTimeHour = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)).clone(23)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupUploadTimeHour.setStatus('current')
backupUploadAction = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("pending", 2), ("upload", 3), ("busy", 4))).clone('idle')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupUploadAction.setStatus('current')
backupUploadResult = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("success", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupUploadResult.setStatus('current')
backupUploadLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupUploadLastChangeTime.setStatus('current')
backupUploadFailure = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 7), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupUploadFailure.setStatus('current')
backupUploadNextTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupUploadNextTime.setStatus('current')
backupUploadInstallUploadFile = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 9), CommandString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupUploadInstallUploadFile.setStatus('current')
backupUploadStatus = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("pending", 2), ("busy", 3))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupUploadStatus.setStatus('current')
backupUploadUploadNow = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 11), CommandString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupUploadUploadNow.setStatus('current')
backupUploadLocalFile = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupUploadLocalFile.setStatus('current')
backupSftpUploadBackupEntityAvailability = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("available", 1), ("availableOutdated", 2), ("notAvailable", 3))).clone('notAvailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSftpUploadBackupEntityAvailability.setStatus('current')
backupSftpUploadBackupEntityCompressionTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSftpUploadBackupEntityCompressionTimestamp.setStatus('current')
backupSftpUploadBackupEntityCrc = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSftpUploadBackupEntityCrc.setStatus('current')
backupSftpUploadRestoreEntityAction = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ready", 1), ("busy", 2), ("restoreNow", 3))).clone('ready')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupSftpUploadRestoreEntityAction.setStatus('current')
backupSftpUploadBackupEntityFilePath = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSftpUploadBackupEntityFilePath.setStatus('current')
backupSftpUploadRestoreEntityFilePath = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupSftpUploadRestoreEntityFilePath.setStatus('current')
backupSftpUploadRestoreEntityRestoreNow = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("restore", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupSftpUploadRestoreEntityRestoreNow.setStatus('current')
backupPersistentFileTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1), )
if mibBuilder.loadTexts: backupPersistentFileTable.setStatus('current')
backupPersistentFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1, 1), ).setIndexNames((0, "LUM-BACKUP-MIB", "backupPersistentFileIndex"))
if mibBuilder.loadTexts: backupPersistentFileEntry.setStatus('current')
backupPersistentFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupPersistentFileIndex.setStatus('current')
backupPersistentFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupPersistentFileName.setStatus('current')
backupPersistentFileDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupPersistentFileDescr.setStatus('current')
backupGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 1)).setObjects(("LUM-BACKUP-MIB", "backupGeneralTestAndIncr"), ("LUM-BACKUP-MIB", "backupGeneralMibSpecVersion"), ("LUM-BACKUP-MIB", "backupGeneralMibImplVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralGroup = backupGeneralGroup.setStatus('deprecated')
backupFileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 2)).setObjects(("LUM-BACKUP-MIB", "backupFileIndex"), ("LUM-BACKUP-MIB", "backupFileName"), ("LUM-BACKUP-MIB", "backupFileDescr"), ("LUM-BACKUP-MIB", "backupFileLastChangeTime"), ("LUM-BACKUP-MIB", "backupFileAdminStatus"), ("LUM-BACKUP-MIB", "backupFileOperStatus"), ("LUM-BACKUP-MIB", "backupFileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupFileGroup = backupFileGroup.setStatus('deprecated')
backupCommandGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 3)).setObjects(("LUM-BACKUP-MIB", "backupCommandName"), ("LUM-BACKUP-MIB", "backupCommandDescr"), ("LUM-BACKUP-MIB", "backupCommandAdminStatus"), ("LUM-BACKUP-MIB", "backupCommandAction"), ("LUM-BACKUP-MIB", "backupCommandResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupCommandGroup = backupCommandGroup.setStatus('current')
backupGeneralGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 4)).setObjects(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralGroupV2 = backupGeneralGroupV2.setStatus('deprecated')
backupGeneralGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 5)).setObjects(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralGroupV3 = backupGeneralGroupV3.setStatus('deprecated')
backupPersistentFileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 6)).setObjects(("LUM-BACKUP-MIB", "backupPersistentFileIndex"), ("LUM-BACKUP-MIB", "backupPersistentFileName"), ("LUM-BACKUP-MIB", "backupPersistentFileDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupPersistentFileGroup = backupPersistentFileGroup.setStatus('current')
backupFileGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 7)).setObjects(("LUM-BACKUP-MIB", "backupFileIndex"), ("LUM-BACKUP-MIB", "backupFileName"), ("LUM-BACKUP-MIB", "backupFileDescr"), ("LUM-BACKUP-MIB", "backupFileLastChangeTime"), ("LUM-BACKUP-MIB", "backupFileAdminStatus"), ("LUM-BACKUP-MIB", "backupFileOperStatus"), ("LUM-BACKUP-MIB", "backupFileRowStatus"), ("LUM-BACKUP-MIB", "backupFileUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupFileGroupV2 = backupFileGroupV2.setStatus('current')
backupGeneralGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 8)).setObjects(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralGroupV4 = backupGeneralGroupV4.setStatus('deprecated')
backupGeneralGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 9)).setObjects(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"), ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralInstallConfigFile"), ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralGroupV5 = backupGeneralGroupV5.setStatus('deprecated')
backupUploadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 10)).setObjects(("LUM-BACKUP-MIB", "backupUploadServerAddr"), ("LUM-BACKUP-MIB", "backupUploadServerPath"), ("LUM-BACKUP-MIB", "backupUploadTimeHour"), ("LUM-BACKUP-MIB", "backupUploadAction"), ("LUM-BACKUP-MIB", "backupUploadResult"), ("LUM-BACKUP-MIB", "backupUploadLastChangeTime"), ("LUM-BACKUP-MIB", "backupUploadFailure"), ("LUM-BACKUP-MIB", "backupUploadNextTime"), ("LUM-BACKUP-MIB", "backupUploadInstallUploadFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupUploadGroup = backupUploadGroup.setStatus('deprecated')
backupGeneralGroupV6 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 11)).setObjects(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"), ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralInstallConfigFile"), ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"), ("LUM-BACKUP-MIB", "backupGeneralWarnForUnsaved"), ("LUM-BACKUP-MIB", "backupGeneralWarnUnsavedDelay"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChangesAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralGroupV6 = backupGeneralGroupV6.setStatus('deprecated')
backupUploadGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 12)).setObjects(("LUM-BACKUP-MIB", "backupUploadServerAddr"), ("LUM-BACKUP-MIB", "backupUploadServerPath"), ("LUM-BACKUP-MIB", "backupUploadTimeHour"), ("LUM-BACKUP-MIB", "backupUploadAction"), ("LUM-BACKUP-MIB", "backupUploadResult"), ("LUM-BACKUP-MIB", "backupUploadLastChangeTime"), ("LUM-BACKUP-MIB", "backupUploadFailure"), ("LUM-BACKUP-MIB", "backupUploadNextTime"), ("LUM-BACKUP-MIB", "backupUploadInstallUploadFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupUploadGroupV2 = backupUploadGroupV2.setStatus('current')
backupUploadGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 13)).setObjects(("LUM-BACKUP-MIB", "backupUploadServerAddr"), ("LUM-BACKUP-MIB", "backupUploadServerPath"), ("LUM-BACKUP-MIB", "backupUploadTimeHour"), ("LUM-BACKUP-MIB", "backupUploadAction"), ("LUM-BACKUP-MIB", "backupUploadResult"), ("LUM-BACKUP-MIB", "backupUploadLastChangeTime"), ("LUM-BACKUP-MIB", "backupUploadFailure"), ("LUM-BACKUP-MIB", "backupUploadNextTime"), ("LUM-BACKUP-MIB", "backupUploadInstallUploadFile"), ("LUM-BACKUP-MIB", "backupUploadUploadNow"), ("LUM-BACKUP-MIB", "backupUploadStatus"), ("LUM-BACKUP-MIB", "backupUploadLocalFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupUploadGroupV3 = backupUploadGroupV3.setStatus('current')
backupGeneralGroupV7 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 14)).setObjects(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"), ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralInstallConfigFile"), ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"), ("LUM-BACKUP-MIB", "backupGeneralWarnForUnsaved"), ("LUM-BACKUP-MIB", "backupGeneralWarnUnsavedDelay"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChangesAlarm"), ("LUM-BACKUP-MIB", "backupGeneralSavedConfigurationGenerationId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralGroupV7 = backupGeneralGroupV7.setStatus('deprecated')
backupGeneralGroupV8 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 15)).setObjects(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"), ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralInstallConfigFile"), ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"), ("LUM-BACKUP-MIB", "backupGeneralWarnForUnsaved"), ("LUM-BACKUP-MIB", "backupGeneralWarnUnsavedDelay"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChangesAlarm"), ("LUM-BACKUP-MIB", "backupGeneralSavedConfigurationGenerationId"), ("LUM-BACKUP-MIB", "backupGeneralBackupScheme"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralGroupV8 = backupGeneralGroupV8.setStatus('deprecated')
backupSftpUploadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 16)).setObjects(("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityAvailability"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCompressionTimestamp"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCrc"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityAction"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityFilePath"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityFilePath"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupSftpUploadGroup = backupSftpUploadGroup.setStatus('deprecated')
backupGeneralGroupV9 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 17)).setObjects(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"), ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"), ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"), ("LUM-BACKUP-MIB", "backupGeneralWarnForUnsaved"), ("LUM-BACKUP-MIB", "backupGeneralWarnUnsavedDelay"), ("LUM-BACKUP-MIB", "backupGeneralUnsavedChangesAlarm"), ("LUM-BACKUP-MIB", "backupGeneralSavedConfigurationGenerationId"), ("LUM-BACKUP-MIB", "backupGeneralBackupScheme"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralGroupV9 = backupGeneralGroupV9.setStatus('current')
backupSftpUploadGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 18)).setObjects(("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityAvailability"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCompressionTimestamp"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCrc"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityAction"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityFilePath"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityFilePath"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityRestoreNow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupSftpUploadGroupV2 = backupSftpUploadGroupV2.setStatus('current')
lumBackupBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 1)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroup"), ("LUM-BACKUP-MIB", "backupFileGroup"), ("LUM-BACKUP-MIB", "backupCommandGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV1 = lumBackupBasicComplV1.setStatus('deprecated')
lumBackupBasicComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 2)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV2"), ("LUM-BACKUP-MIB", "backupFileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV2 = lumBackupBasicComplV2.setStatus('deprecated')
lumBackupBasicComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 3)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV3"), ("LUM-BACKUP-MIB", "backupFileGroup"), ("LUM-BACKUP-MIB", "backupCommandGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV3 = lumBackupBasicComplV3.setStatus('deprecated')
lumBackupBasicComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 4)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV3"), ("LUM-BACKUP-MIB", "backupFileGroup"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV4 = lumBackupBasicComplV4.setStatus('deprecated')
lumBackupBasicComplV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 5)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV3"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV5 = lumBackupBasicComplV5.setStatus('deprecated')
lumBackupBasicComplV6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 6)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV4"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV6 = lumBackupBasicComplV6.setStatus('deprecated')
lumBackupBasicComplV7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 7)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV5"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"), ("LUM-BACKUP-MIB", "backupUploadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV7 = lumBackupBasicComplV7.setStatus('deprecated')
lumBackupBasicComplV8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 8)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV5"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"), ("LUM-BACKUP-MIB", "backupUploadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV8 = lumBackupBasicComplV8.setStatus('deprecated')
lumBackupBasicComplV9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 9)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV6"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"), ("LUM-BACKUP-MIB", "backupUploadGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV9 = lumBackupBasicComplV9.setStatus('deprecated')
lumBackupBasicComplV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 10)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV6"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"), ("LUM-BACKUP-MIB", "backupUploadGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV10 = lumBackupBasicComplV10.setStatus('deprecated')
lumBackupBasicComplV11 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 11)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV7"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"), ("LUM-BACKUP-MIB", "backupUploadGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV11 = lumBackupBasicComplV11.setStatus('deprecated')
lumBackupBasicComplV12 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 12)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV8"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"), ("LUM-BACKUP-MIB", "backupUploadGroupV3"), ("LUM-BACKUP-MIB", "backupSftpUploadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV12 = lumBackupBasicComplV12.setStatus('deprecated')
lumBackupBasicComplV13 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 13)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV9"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"), ("LUM-BACKUP-MIB", "backupUploadGroupV3"), ("LUM-BACKUP-MIB", "backupSftpUploadGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV13 = lumBackupBasicComplV13.setStatus('deprecated')
lumBackupBasicComplV14 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 14)).setObjects(("LUM-BACKUP-MIB", "backupGeneralGroupV9"), ("LUM-BACKUP-MIB", "backupFileGroupV2"), ("LUM-BACKUP-MIB", "backupCommandGroup"), ("LUM-BACKUP-MIB", "backupPersistentFileGroup"), ("LUM-BACKUP-MIB", "backupUploadGroupV3"), ("LUM-BACKUP-MIB", "backupSftpUploadGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupBasicComplV14 = lumBackupBasicComplV14.setStatus('current')
backupGeneralMinimalGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3, 1)).setObjects(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"), ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupGeneralMinimalGroupV1 = backupGeneralMinimalGroupV1.setStatus('current')
backupUploadMinimalGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3, 2)).setObjects(("LUM-BACKUP-MIB", "backupUploadServerAddr"), ("LUM-BACKUP-MIB", "backupUploadTimeHour"), ("LUM-BACKUP-MIB", "backupUploadAction"), ("LUM-BACKUP-MIB", "backupUploadResult"), ("LUM-BACKUP-MIB", "backupUploadLastChangeTime"), ("LUM-BACKUP-MIB", "backupUploadFailure"), ("LUM-BACKUP-MIB", "backupUploadNextTime"), ("LUM-BACKUP-MIB", "backupUploadLocalFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupUploadMinimalGroupV1 = backupUploadMinimalGroupV1.setStatus('current')
backupSftpUploadMinimalGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3, 3)).setObjects(("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityAvailability"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCompressionTimestamp"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCrc"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityAction"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityFilePath"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityFilePath"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupSftpUploadMinimalGroupV1 = backupSftpUploadMinimalGroupV1.setStatus('deprecated')
backupSftpUploadMinimalGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3, 4)).setObjects(("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityAvailability"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCompressionTimestamp"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCrc"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityAction"), ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityFilePath"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityFilePath"), ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityRestoreNow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    backupSftpUploadMinimalGroupV2 = backupSftpUploadMinimalGroupV2.setStatus('current')
lumBackupMinimalComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4, 1)).setObjects(("LUM-BACKUP-MIB", "backupGeneralMinimalGroupV1"), ("LUM-BACKUP-MIB", "backupUploadMinimalGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupMinimalComplV1 = lumBackupMinimalComplV1.setStatus('deprecated')
lumBackupMinimalComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4, 2)).setObjects(("LUM-BACKUP-MIB", "backupGeneralMinimalGroupV1"), ("LUM-BACKUP-MIB", "backupUploadMinimalGroupV1"), ("LUM-BACKUP-MIB", "backupSftpUploadMinimalGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupMinimalComplV2 = lumBackupMinimalComplV2.setStatus('deprecated')
lumBackupMinimalComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4, 3)).setObjects(("LUM-BACKUP-MIB", "backupGeneralMinimalGroupV1"), ("LUM-BACKUP-MIB", "backupUploadMinimalGroupV1"), ("LUM-BACKUP-MIB", "backupSftpUploadMinimalGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupMinimalComplV3 = lumBackupMinimalComplV3.setStatus('deprecated')
lumBackupMinimalComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4, 4)).setObjects(("LUM-BACKUP-MIB", "backupGeneralMinimalGroupV1"), ("LUM-BACKUP-MIB", "backupUploadMinimalGroupV1"), ("LUM-BACKUP-MIB", "backupSftpUploadMinimalGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumBackupMinimalComplV4 = lumBackupMinimalComplV4.setStatus('current')
mibBuilder.exportSymbols("LUM-BACKUP-MIB", lumBackupMinimalComplV1=lumBackupMinimalComplV1, lumBackupBasicComplV4=lumBackupBasicComplV4, lumBackupBasicComplV14=lumBackupBasicComplV14, backupUploadGroupV2=backupUploadGroupV2, backupSftpUploadBackupEntityCrc=backupSftpUploadBackupEntityCrc, backupUploadLastChangeTime=backupUploadLastChangeTime, backupGeneralConfigLastChangeTime=backupGeneralConfigLastChangeTime, backupUploadInstallUploadFile=backupUploadInstallUploadFile, backupGeneralGroupV7=backupGeneralGroupV7, backupSftpUploadBackupEntityFilePath=backupSftpUploadBackupEntityFilePath, PYSNMP_MODULE_ID=lumBackupMIBModule, backupUploadUploadNow=backupUploadUploadNow, backupGeneralPersistentFileTableSize=backupGeneralPersistentFileTableSize, backupSftpUploadBackupEntityCompressionTimestamp=backupSftpUploadBackupEntityCompressionTimestamp, backupFileDescr=backupFileDescr, backupGeneralPrimaryFileName=backupGeneralPrimaryFileName, backupUploadLocalFile=backupUploadLocalFile, backupSftpUploadGroupV2=backupSftpUploadGroupV2, lumBackupBasicComplV8=lumBackupBasicComplV8, lumBackupMinimalComplV4=lumBackupMinimalComplV4, backupFileGroup=backupFileGroup, backupCommandAdminStatus=backupCommandAdminStatus, lumBackupBasicComplV3=lumBackupBasicComplV3, backupSftpUpload=backupSftpUpload, backupUploadStatus=backupUploadStatus, backupSftpUploadRestoreEntityRestoreNow=backupSftpUploadRestoreEntityRestoreNow, backupUpload=backupUpload, backupCommandResult=backupCommandResult, backupSftpUploadMinimalGroupV1=backupSftpUploadMinimalGroupV1, backupFileEntry=backupFileEntry, backupUploadServerAddr=backupUploadServerAddr, lumBackupCompl=lumBackupCompl, backupUploadNextTime=backupUploadNextTime, backupUploadAction=backupUploadAction, backupSftpUploadRestoreEntityAction=backupSftpUploadRestoreEntityAction, lumBackupBasicComplV13=lumBackupBasicComplV13, backupFileLastChangeTime=backupFileLastChangeTime, lumBackupMinimalGroups=lumBackupMinimalGroups, backupUploadGroupV3=backupUploadGroupV3, backupPersistentFileName=backupPersistentFileName, lumBackupBasicComplV9=lumBackupBasicComplV9, backupGeneralLastChangeTime=backupGeneralLastChangeTime, backupCommand=backupCommand, backupGeneralUnsavedChanges=backupGeneralUnsavedChanges, backupGeneralGroupV5=backupGeneralGroupV5, backupSftpUploadRestoreEntityFilePath=backupSftpUploadRestoreEntityFilePath, backupCommandGroup=backupCommandGroup, lumBackupGroups=lumBackupGroups, lumBackupBasicComplV2=lumBackupBasicComplV2, backupFileTable=backupFileTable, backupGeneralBackupScheme=backupGeneralBackupScheme, backupGeneralMibImplVersion=backupGeneralMibImplVersion, backupCommandAction=backupCommandAction, backupSftpUploadGroup=backupSftpUploadGroup, lumBackupBasicComplV1=lumBackupBasicComplV1, backupPersistentFileIndex=backupPersistentFileIndex, lumBackupMinimalComplV2=lumBackupMinimalComplV2, lumBackupBasicComplV11=lumBackupBasicComplV11, backupFileRowStatus=backupFileRowStatus, backupUploadFailure=backupUploadFailure, backupGeneralUnsavedChangesAlarm=backupGeneralUnsavedChangesAlarm, backupFileIndex=backupFileIndex, backupUploadServerPath=backupUploadServerPath, backupPersistentFileEntry=backupPersistentFileEntry, backupGeneralMinimalGroupV1=backupGeneralMinimalGroupV1, backupGeneralGlobalStateLastChangeTime=backupGeneralGlobalStateLastChangeTime, backupGeneralWarnForUnsaved=backupGeneralWarnForUnsaved, backupUploadResult=backupUploadResult, backupGeneralWarnUnsavedDelay=backupGeneralWarnUnsavedDelay, backupUploadMinimalGroupV1=backupUploadMinimalGroupV1, lumBackupConfs=lumBackupConfs, backupGeneralGroup=backupGeneralGroup, lumBackupMIBModule=lumBackupMIBModule, backupGeneralGroupV2=backupGeneralGroupV2, backupFileList=backupFileList, backupCommandName=backupCommandName, lumBackupBasicComplV12=lumBackupBasicComplV12, backupFileUrl=backupFileUrl, lumBackupBasicComplV10=lumBackupBasicComplV10, backupGeneralMibSpecVersion=backupGeneralMibSpecVersion, backupCommandDescr=backupCommandDescr, backupGeneralInstallConfigFile=backupGeneralInstallConfigFile, backupGeneralGroupV6=backupGeneralGroupV6, backupPersistentFileTable=backupPersistentFileTable, backupGeneralGlobalConfigLastChangeTime=backupGeneralGlobalConfigLastChangeTime, backupUploadTimeHour=backupUploadTimeHour, lumBackupBasicComplV6=lumBackupBasicComplV6, backupFileGroupV2=backupFileGroupV2, backupPersistentFileGroup=backupPersistentFileGroup, lumBackupMinimalComplV3=lumBackupMinimalComplV3, backupFileAdminStatus=backupFileAdminStatus, backupUploadGroup=backupUploadGroup, lumBackupBasicComplV5=lumBackupBasicComplV5, backupGeneralFileTableSize=backupGeneralFileTableSize, lumBackupMIBObjects=lumBackupMIBObjects, backupGeneral=backupGeneral, backupPersistentFileList=backupPersistentFileList, backupGeneralGroupV8=backupGeneralGroupV8, backupGeneralGroupV4=backupGeneralGroupV4, lumBackupMinimalCompl=lumBackupMinimalCompl, backupFileName=backupFileName, backupGeneralSavedConfigurationGenerationId=backupGeneralSavedConfigurationGenerationId, backupGeneralGroupV9=backupGeneralGroupV9, backupSftpUploadBackupEntityAvailability=backupSftpUploadBackupEntityAvailability, backupPersistentFileDescr=backupPersistentFileDescr, backupFileOperStatus=backupFileOperStatus, backupSftpUploadMinimalGroupV2=backupSftpUploadMinimalGroupV2, backupGeneralGroupV3=backupGeneralGroupV3, lumBackupBasicComplV7=lumBackupBasicComplV7, backupGeneralTestAndIncr=backupGeneralTestAndIncr)
