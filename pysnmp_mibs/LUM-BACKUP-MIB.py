# SNMP MIB module (LUM-BACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-BACKUP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:03 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(lumBackupMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumBackupMIB",
    "lumModules")

(CommandString,
 FaultStatus) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "FaultStatus")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

lumBackupMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 7)
)
if mibBuilder.loadTexts:
    lumBackupMIBModule.setRevisions(
        ("2017-12-15 00:00",
         "2017-06-15 00:00",
         "2016-01-11 00:00",
         "2007-01-11 00:00",
         "2005-12-05 00:00",
         "2004-12-21 00:00",
         "2004-12-20 00:00",
         "2004-11-09 00:00",
         "2004-10-28 00:00",
         "2004-09-30 00:00",
         "2004-06-17 00:00",
         "2002-10-29 00:00",
         "2001-10-30 00:00",
         "2001-08-16 00:00",
         "2001-08-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumBackupConfs_ObjectIdentity = ObjectIdentity
lumBackupConfs = _LumBackupConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1)
)
_LumBackupGroups_ObjectIdentity = ObjectIdentity
lumBackupGroups = _LumBackupGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1)
)
_LumBackupCompl_ObjectIdentity = ObjectIdentity
lumBackupCompl = _LumBackupCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2)
)
_LumBackupMinimalGroups_ObjectIdentity = ObjectIdentity
lumBackupMinimalGroups = _LumBackupMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3)
)
_LumBackupMinimalCompl_ObjectIdentity = ObjectIdentity
lumBackupMinimalCompl = _LumBackupMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4)
)
_LumBackupMIBObjects_ObjectIdentity = ObjectIdentity
lumBackupMIBObjects = _LumBackupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2)
)
_BackupGeneral_ObjectIdentity = ObjectIdentity
backupGeneral = _BackupGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1)
)
_BackupGeneralTestAndIncr_Type = TestAndIncr
_BackupGeneralTestAndIncr_Object = MibScalar
backupGeneralTestAndIncr = _BackupGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 1),
    _BackupGeneralTestAndIncr_Type()
)
backupGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupGeneralTestAndIncr.setStatus("current")


class _BackupGeneralMibSpecVersion_Type(DisplayString):
    """Custom type backupGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_BackupGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_BackupGeneralMibSpecVersion_Object = MibScalar
backupGeneralMibSpecVersion = _BackupGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 2),
    _BackupGeneralMibSpecVersion_Type()
)
backupGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupGeneralMibSpecVersion.setStatus("current")


class _BackupGeneralMibImplVersion_Type(DisplayString):
    """Custom type backupGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_BackupGeneralMibImplVersion_Type.__name__ = "DisplayString"
_BackupGeneralMibImplVersion_Object = MibScalar
backupGeneralMibImplVersion = _BackupGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 3),
    _BackupGeneralMibImplVersion_Type()
)
backupGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupGeneralMibImplVersion.setStatus("current")
_BackupGeneralLastChangeTime_Type = DateAndTime
_BackupGeneralLastChangeTime_Object = MibScalar
backupGeneralLastChangeTime = _BackupGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 4),
    _BackupGeneralLastChangeTime_Type()
)
backupGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralLastChangeTime.setStatus("current")
_BackupGeneralConfigLastChangeTime_Type = DateAndTime
_BackupGeneralConfigLastChangeTime_Object = MibScalar
backupGeneralConfigLastChangeTime = _BackupGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 5),
    _BackupGeneralConfigLastChangeTime_Type()
)
backupGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralConfigLastChangeTime.setStatus("current")
_BackupGeneralUnsavedChanges_Type = TruthValue
_BackupGeneralUnsavedChanges_Object = MibScalar
backupGeneralUnsavedChanges = _BackupGeneralUnsavedChanges_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 6),
    _BackupGeneralUnsavedChanges_Type()
)
backupGeneralUnsavedChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralUnsavedChanges.setStatus("current")
_BackupGeneralFileTableSize_Type = Unsigned32
_BackupGeneralFileTableSize_Object = MibScalar
backupGeneralFileTableSize = _BackupGeneralFileTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 7),
    _BackupGeneralFileTableSize_Type()
)
backupGeneralFileTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralFileTableSize.setStatus("current")
_BackupGeneralPersistentFileTableSize_Type = Unsigned32
_BackupGeneralPersistentFileTableSize_Object = MibScalar
backupGeneralPersistentFileTableSize = _BackupGeneralPersistentFileTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 8),
    _BackupGeneralPersistentFileTableSize_Type()
)
backupGeneralPersistentFileTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralPersistentFileTableSize.setStatus("current")
_BackupGeneralInstallConfigFile_Type = CommandString
_BackupGeneralInstallConfigFile_Object = MibScalar
backupGeneralInstallConfigFile = _BackupGeneralInstallConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 9),
    _BackupGeneralInstallConfigFile_Type()
)
backupGeneralInstallConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupGeneralInstallConfigFile.setStatus("deprecated")
_BackupGeneralGlobalStateLastChangeTime_Type = DateAndTime
_BackupGeneralGlobalStateLastChangeTime_Object = MibScalar
backupGeneralGlobalStateLastChangeTime = _BackupGeneralGlobalStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 10),
    _BackupGeneralGlobalStateLastChangeTime_Type()
)
backupGeneralGlobalStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralGlobalStateLastChangeTime.setStatus("current")
_BackupGeneralGlobalConfigLastChangeTime_Type = DateAndTime
_BackupGeneralGlobalConfigLastChangeTime_Object = MibScalar
backupGeneralGlobalConfigLastChangeTime = _BackupGeneralGlobalConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 11),
    _BackupGeneralGlobalConfigLastChangeTime_Type()
)
backupGeneralGlobalConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralGlobalConfigLastChangeTime.setStatus("current")
_BackupGeneralPrimaryFileName_Type = DisplayString
_BackupGeneralPrimaryFileName_Object = MibScalar
backupGeneralPrimaryFileName = _BackupGeneralPrimaryFileName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 12),
    _BackupGeneralPrimaryFileName_Type()
)
backupGeneralPrimaryFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralPrimaryFileName.setStatus("current")


class _BackupGeneralWarnForUnsaved_Type(Integer32):
    """Custom type backupGeneralWarnForUnsaved based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BackupGeneralWarnForUnsaved_Type.__name__ = "Integer32"
_BackupGeneralWarnForUnsaved_Object = MibScalar
backupGeneralWarnForUnsaved = _BackupGeneralWarnForUnsaved_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 13),
    _BackupGeneralWarnForUnsaved_Type()
)
backupGeneralWarnForUnsaved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupGeneralWarnForUnsaved.setStatus("current")


class _BackupGeneralWarnUnsavedDelay_Type(Unsigned32):
    """Custom type backupGeneralWarnUnsavedDelay based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_BackupGeneralWarnUnsavedDelay_Type.__name__ = "Unsigned32"
_BackupGeneralWarnUnsavedDelay_Object = MibScalar
backupGeneralWarnUnsavedDelay = _BackupGeneralWarnUnsavedDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 14),
    _BackupGeneralWarnUnsavedDelay_Type()
)
backupGeneralWarnUnsavedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupGeneralWarnUnsavedDelay.setStatus("current")
_BackupGeneralUnsavedChangesAlarm_Type = FaultStatus
_BackupGeneralUnsavedChangesAlarm_Object = MibScalar
backupGeneralUnsavedChangesAlarm = _BackupGeneralUnsavedChangesAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 15),
    _BackupGeneralUnsavedChangesAlarm_Type()
)
backupGeneralUnsavedChangesAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralUnsavedChangesAlarm.setStatus("current")


class _BackupGeneralSavedConfigurationGenerationId_Type(Unsigned32):
    """Custom type backupGeneralSavedConfigurationGenerationId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BackupGeneralSavedConfigurationGenerationId_Type.__name__ = "Unsigned32"
_BackupGeneralSavedConfigurationGenerationId_Object = MibScalar
backupGeneralSavedConfigurationGenerationId = _BackupGeneralSavedConfigurationGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 16),
    _BackupGeneralSavedConfigurationGenerationId_Type()
)
backupGeneralSavedConfigurationGenerationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupGeneralSavedConfigurationGenerationId.setStatus("current")


class _BackupGeneralBackupScheme_Type(Integer32):
    """Custom type backupGeneralBackupScheme based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("sftp", 2))
    )


_BackupGeneralBackupScheme_Type.__name__ = "Integer32"
_BackupGeneralBackupScheme_Object = MibScalar
backupGeneralBackupScheme = _BackupGeneralBackupScheme_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 1, 17),
    _BackupGeneralBackupScheme_Type()
)
backupGeneralBackupScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupGeneralBackupScheme.setStatus("current")
_BackupFileList_ObjectIdentity = ObjectIdentity
backupFileList = _BackupFileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2)
)
_BackupFileTable_Object = MibTable
backupFileTable = _BackupFileTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    backupFileTable.setStatus("current")
_BackupFileEntry_Object = MibTableRow
backupFileEntry = _BackupFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1)
)
backupFileEntry.setIndexNames(
    (0, "LUM-BACKUP-MIB", "backupFileIndex"),
)
if mibBuilder.loadTexts:
    backupFileEntry.setStatus("current")


class _BackupFileIndex_Type(Unsigned32):
    """Custom type backupFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BackupFileIndex_Type.__name__ = "Unsigned32"
_BackupFileIndex_Object = MibTableColumn
backupFileIndex = _BackupFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 1),
    _BackupFileIndex_Type()
)
backupFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupFileIndex.setStatus("current")
_BackupFileName_Type = DisplayString
_BackupFileName_Object = MibTableColumn
backupFileName = _BackupFileName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 2),
    _BackupFileName_Type()
)
backupFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupFileName.setStatus("current")


class _BackupFileDescr_Type(DisplayString):
    """Custom type backupFileDescr based on DisplayString"""
    defaultValue = OctetString("")


_BackupFileDescr_Type.__name__ = "DisplayString"
_BackupFileDescr_Object = MibTableColumn
backupFileDescr = _BackupFileDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 3),
    _BackupFileDescr_Type()
)
backupFileDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupFileDescr.setStatus("current")
_BackupFileLastChangeTime_Type = DateAndTime
_BackupFileLastChangeTime_Object = MibTableColumn
backupFileLastChangeTime = _BackupFileLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 4),
    _BackupFileLastChangeTime_Type()
)
backupFileLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupFileLastChangeTime.setStatus("current")


class _BackupFileAdminStatus_Type(Integer32):
    """Custom type backupFileAdminStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("secondary", 2),
          ("primary", 3))
    )


_BackupFileAdminStatus_Type.__name__ = "Integer32"
_BackupFileAdminStatus_Object = MibTableColumn
backupFileAdminStatus = _BackupFileAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 5),
    _BackupFileAdminStatus_Type()
)
backupFileAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupFileAdminStatus.setStatus("current")


class _BackupFileOperStatus_Type(Integer32):
    """Custom type backupFileOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("running", 2))
    )


_BackupFileOperStatus_Type.__name__ = "Integer32"
_BackupFileOperStatus_Object = MibTableColumn
backupFileOperStatus = _BackupFileOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 6),
    _BackupFileOperStatus_Type()
)
backupFileOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupFileOperStatus.setStatus("current")
_BackupFileRowStatus_Type = RowStatus
_BackupFileRowStatus_Object = MibTableColumn
backupFileRowStatus = _BackupFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 7),
    _BackupFileRowStatus_Type()
)
backupFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupFileRowStatus.setStatus("current")
_BackupFileUrl_Type = DisplayString
_BackupFileUrl_Object = MibTableColumn
backupFileUrl = _BackupFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 2, 1, 1, 8),
    _BackupFileUrl_Type()
)
backupFileUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupFileUrl.setStatus("current")
_BackupCommand_ObjectIdentity = ObjectIdentity
backupCommand = _BackupCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3)
)


class _BackupCommandName_Type(DisplayString):
    """Custom type backupCommandName based on DisplayString"""
    defaultValue = OctetString("")


_BackupCommandName_Type.__name__ = "DisplayString"
_BackupCommandName_Object = MibScalar
backupCommandName = _BackupCommandName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 1),
    _BackupCommandName_Type()
)
backupCommandName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupCommandName.setStatus("current")


class _BackupCommandDescr_Type(DisplayString):
    """Custom type backupCommandDescr based on DisplayString"""
    defaultValue = OctetString("")


_BackupCommandDescr_Type.__name__ = "DisplayString"
_BackupCommandDescr_Object = MibScalar
backupCommandDescr = _BackupCommandDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 2),
    _BackupCommandDescr_Type()
)
backupCommandDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupCommandDescr.setStatus("current")


class _BackupCommandAdminStatus_Type(Integer32):
    """Custom type backupCommandAdminStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("secondary", 2),
          ("primary", 3))
    )


_BackupCommandAdminStatus_Type.__name__ = "Integer32"
_BackupCommandAdminStatus_Object = MibScalar
backupCommandAdminStatus = _BackupCommandAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 3),
    _BackupCommandAdminStatus_Type()
)
backupCommandAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupCommandAdminStatus.setStatus("current")


class _BackupCommandAction_Type(Integer32):
    """Custom type backupCommandAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("saveTofile", 2),
          ("busy", 3))
    )


_BackupCommandAction_Type.__name__ = "Integer32"
_BackupCommandAction_Object = MibScalar
backupCommandAction = _BackupCommandAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 4),
    _BackupCommandAction_Type()
)
backupCommandAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupCommandAction.setStatus("current")


class _BackupCommandResult_Type(Integer32):
    """Custom type backupCommandResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("success", 2),
          ("failed", 3))
    )


_BackupCommandResult_Type.__name__ = "Integer32"
_BackupCommandResult_Object = MibScalar
backupCommandResult = _BackupCommandResult_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 3, 5),
    _BackupCommandResult_Type()
)
backupCommandResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupCommandResult.setStatus("current")
_BackupPersistentFileList_ObjectIdentity = ObjectIdentity
backupPersistentFileList = _BackupPersistentFileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4)
)
_BackupPersistentFileTable_Object = MibTable
backupPersistentFileTable = _BackupPersistentFileTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    backupPersistentFileTable.setStatus("current")
_BackupPersistentFileEntry_Object = MibTableRow
backupPersistentFileEntry = _BackupPersistentFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1, 1)
)
backupPersistentFileEntry.setIndexNames(
    (0, "LUM-BACKUP-MIB", "backupPersistentFileIndex"),
)
if mibBuilder.loadTexts:
    backupPersistentFileEntry.setStatus("current")


class _BackupPersistentFileIndex_Type(Unsigned32):
    """Custom type backupPersistentFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BackupPersistentFileIndex_Type.__name__ = "Unsigned32"
_BackupPersistentFileIndex_Object = MibTableColumn
backupPersistentFileIndex = _BackupPersistentFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1, 1, 1),
    _BackupPersistentFileIndex_Type()
)
backupPersistentFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupPersistentFileIndex.setStatus("current")
_BackupPersistentFileName_Type = DisplayString
_BackupPersistentFileName_Object = MibTableColumn
backupPersistentFileName = _BackupPersistentFileName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1, 1, 2),
    _BackupPersistentFileName_Type()
)
backupPersistentFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupPersistentFileName.setStatus("current")
_BackupPersistentFileDescr_Type = DisplayString
_BackupPersistentFileDescr_Object = MibTableColumn
backupPersistentFileDescr = _BackupPersistentFileDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 4, 1, 1, 3),
    _BackupPersistentFileDescr_Type()
)
backupPersistentFileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupPersistentFileDescr.setStatus("current")
_BackupUpload_ObjectIdentity = ObjectIdentity
backupUpload = _BackupUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5)
)
_BackupUploadServerAddr_Type = IpAddress
_BackupUploadServerAddr_Object = MibScalar
backupUploadServerAddr = _BackupUploadServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 1),
    _BackupUploadServerAddr_Type()
)
backupUploadServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupUploadServerAddr.setStatus("current")


class _BackupUploadServerPath_Type(DisplayString):
    """Custom type backupUploadServerPath based on DisplayString"""
    defaultValue = OctetString("/upload")


_BackupUploadServerPath_Type.__name__ = "DisplayString"
_BackupUploadServerPath_Object = MibScalar
backupUploadServerPath = _BackupUploadServerPath_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 2),
    _BackupUploadServerPath_Type()
)
backupUploadServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupUploadServerPath.setStatus("current")


class _BackupUploadTimeHour_Type(Unsigned32):
    """Custom type backupUploadTimeHour based on Unsigned32"""
    defaultValue = 23

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_BackupUploadTimeHour_Type.__name__ = "Unsigned32"
_BackupUploadTimeHour_Object = MibScalar
backupUploadTimeHour = _BackupUploadTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 3),
    _BackupUploadTimeHour_Type()
)
backupUploadTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupUploadTimeHour.setStatus("current")


class _BackupUploadAction_Type(Integer32):
    """Custom type backupUploadAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("pending", 2),
          ("upload", 3),
          ("busy", 4))
    )


_BackupUploadAction_Type.__name__ = "Integer32"
_BackupUploadAction_Object = MibScalar
backupUploadAction = _BackupUploadAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 4),
    _BackupUploadAction_Type()
)
backupUploadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupUploadAction.setStatus("current")


class _BackupUploadResult_Type(Integer32):
    """Custom type backupUploadResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("success", 2),
          ("failed", 3))
    )


_BackupUploadResult_Type.__name__ = "Integer32"
_BackupUploadResult_Object = MibScalar
backupUploadResult = _BackupUploadResult_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 5),
    _BackupUploadResult_Type()
)
backupUploadResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupUploadResult.setStatus("current")
_BackupUploadLastChangeTime_Type = DateAndTime
_BackupUploadLastChangeTime_Object = MibScalar
backupUploadLastChangeTime = _BackupUploadLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 6),
    _BackupUploadLastChangeTime_Type()
)
backupUploadLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupUploadLastChangeTime.setStatus("current")
_BackupUploadFailure_Type = FaultStatus
_BackupUploadFailure_Object = MibScalar
backupUploadFailure = _BackupUploadFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 7),
    _BackupUploadFailure_Type()
)
backupUploadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupUploadFailure.setStatus("current")
_BackupUploadNextTime_Type = DateAndTime
_BackupUploadNextTime_Object = MibScalar
backupUploadNextTime = _BackupUploadNextTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 8),
    _BackupUploadNextTime_Type()
)
backupUploadNextTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupUploadNextTime.setStatus("current")
_BackupUploadInstallUploadFile_Type = CommandString
_BackupUploadInstallUploadFile_Object = MibScalar
backupUploadInstallUploadFile = _BackupUploadInstallUploadFile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 9),
    _BackupUploadInstallUploadFile_Type()
)
backupUploadInstallUploadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupUploadInstallUploadFile.setStatus("current")


class _BackupUploadStatus_Type(Integer32):
    """Custom type backupUploadStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("pending", 2),
          ("busy", 3))
    )


_BackupUploadStatus_Type.__name__ = "Integer32"
_BackupUploadStatus_Object = MibScalar
backupUploadStatus = _BackupUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 10),
    _BackupUploadStatus_Type()
)
backupUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupUploadStatus.setStatus("current")
_BackupUploadUploadNow_Type = CommandString
_BackupUploadUploadNow_Object = MibScalar
backupUploadUploadNow = _BackupUploadUploadNow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 11),
    _BackupUploadUploadNow_Type()
)
backupUploadUploadNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupUploadUploadNow.setStatus("current")


class _BackupUploadLocalFile_Type(DisplayString):
    """Custom type backupUploadLocalFile based on DisplayString"""
    defaultValue = OctetString("")


_BackupUploadLocalFile_Type.__name__ = "DisplayString"
_BackupUploadLocalFile_Object = MibScalar
backupUploadLocalFile = _BackupUploadLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 5, 12),
    _BackupUploadLocalFile_Type()
)
backupUploadLocalFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupUploadLocalFile.setStatus("current")
_BackupSftpUpload_ObjectIdentity = ObjectIdentity
backupSftpUpload = _BackupSftpUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6)
)


class _BackupSftpUploadBackupEntityAvailability_Type(Integer32):
    """Custom type backupSftpUploadBackupEntityAvailability based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("availableOutdated", 2),
          ("notAvailable", 3))
    )


_BackupSftpUploadBackupEntityAvailability_Type.__name__ = "Integer32"
_BackupSftpUploadBackupEntityAvailability_Object = MibScalar
backupSftpUploadBackupEntityAvailability = _BackupSftpUploadBackupEntityAvailability_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 1),
    _BackupSftpUploadBackupEntityAvailability_Type()
)
backupSftpUploadBackupEntityAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSftpUploadBackupEntityAvailability.setStatus("current")
_BackupSftpUploadBackupEntityCompressionTimestamp_Type = DateAndTime
_BackupSftpUploadBackupEntityCompressionTimestamp_Object = MibScalar
backupSftpUploadBackupEntityCompressionTimestamp = _BackupSftpUploadBackupEntityCompressionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 2),
    _BackupSftpUploadBackupEntityCompressionTimestamp_Type()
)
backupSftpUploadBackupEntityCompressionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSftpUploadBackupEntityCompressionTimestamp.setStatus("current")


class _BackupSftpUploadBackupEntityCrc_Type(Unsigned32):
    """Custom type backupSftpUploadBackupEntityCrc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BackupSftpUploadBackupEntityCrc_Type.__name__ = "Unsigned32"
_BackupSftpUploadBackupEntityCrc_Object = MibScalar
backupSftpUploadBackupEntityCrc = _BackupSftpUploadBackupEntityCrc_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 3),
    _BackupSftpUploadBackupEntityCrc_Type()
)
backupSftpUploadBackupEntityCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSftpUploadBackupEntityCrc.setStatus("current")


class _BackupSftpUploadRestoreEntityAction_Type(Integer32):
    """Custom type backupSftpUploadRestoreEntityAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("busy", 2),
          ("restoreNow", 3))
    )


_BackupSftpUploadRestoreEntityAction_Type.__name__ = "Integer32"
_BackupSftpUploadRestoreEntityAction_Object = MibScalar
backupSftpUploadRestoreEntityAction = _BackupSftpUploadRestoreEntityAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 5),
    _BackupSftpUploadRestoreEntityAction_Type()
)
backupSftpUploadRestoreEntityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupSftpUploadRestoreEntityAction.setStatus("current")
_BackupSftpUploadBackupEntityFilePath_Type = DisplayString
_BackupSftpUploadBackupEntityFilePath_Object = MibScalar
backupSftpUploadBackupEntityFilePath = _BackupSftpUploadBackupEntityFilePath_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 6),
    _BackupSftpUploadBackupEntityFilePath_Type()
)
backupSftpUploadBackupEntityFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSftpUploadBackupEntityFilePath.setStatus("current")


class _BackupSftpUploadRestoreEntityFilePath_Type(DisplayString):
    """Custom type backupSftpUploadRestoreEntityFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BackupSftpUploadRestoreEntityFilePath_Type.__name__ = "DisplayString"
_BackupSftpUploadRestoreEntityFilePath_Object = MibScalar
backupSftpUploadRestoreEntityFilePath = _BackupSftpUploadRestoreEntityFilePath_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 7),
    _BackupSftpUploadRestoreEntityFilePath_Type()
)
backupSftpUploadRestoreEntityFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupSftpUploadRestoreEntityFilePath.setStatus("current")


class _BackupSftpUploadRestoreEntityRestoreNow_Type(Integer32):
    """Custom type backupSftpUploadRestoreEntityRestoreNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("restore", 2))
    )


_BackupSftpUploadRestoreEntityRestoreNow_Type.__name__ = "Integer32"
_BackupSftpUploadRestoreEntityRestoreNow_Object = MibScalar
backupSftpUploadRestoreEntityRestoreNow = _BackupSftpUploadRestoreEntityRestoreNow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 2, 6, 8),
    _BackupSftpUploadRestoreEntityRestoreNow_Type()
)
backupSftpUploadRestoreEntityRestoreNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupSftpUploadRestoreEntityRestoreNow.setStatus("current")

# Managed Objects groups

backupGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 1)
)
backupGeneralGroup.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralTestAndIncr"),
        ("LUM-BACKUP-MIB", "backupGeneralMibSpecVersion"),
        ("LUM-BACKUP-MIB", "backupGeneralMibImplVersion"))
)
if mibBuilder.loadTexts:
    backupGeneralGroup.setStatus("deprecated")

backupFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 2)
)
backupFileGroup.setObjects(
      *(("LUM-BACKUP-MIB", "backupFileIndex"),
        ("LUM-BACKUP-MIB", "backupFileName"),
        ("LUM-BACKUP-MIB", "backupFileDescr"),
        ("LUM-BACKUP-MIB", "backupFileLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupFileAdminStatus"),
        ("LUM-BACKUP-MIB", "backupFileOperStatus"),
        ("LUM-BACKUP-MIB", "backupFileRowStatus"))
)
if mibBuilder.loadTexts:
    backupFileGroup.setStatus("deprecated")

backupCommandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 3)
)
backupCommandGroup.setObjects(
      *(("LUM-BACKUP-MIB", "backupCommandName"),
        ("LUM-BACKUP-MIB", "backupCommandDescr"),
        ("LUM-BACKUP-MIB", "backupCommandAdminStatus"),
        ("LUM-BACKUP-MIB", "backupCommandAction"),
        ("LUM-BACKUP-MIB", "backupCommandResult"))
)
if mibBuilder.loadTexts:
    backupCommandGroup.setStatus("current")

backupGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 4)
)
backupGeneralGroupV2.setObjects(
    ("LUM-BACKUP-MIB", "backupGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    backupGeneralGroupV2.setStatus("deprecated")

backupGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 5)
)
backupGeneralGroupV3.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    backupGeneralGroupV3.setStatus("deprecated")

backupPersistentFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 6)
)
backupPersistentFileGroup.setObjects(
      *(("LUM-BACKUP-MIB", "backupPersistentFileIndex"),
        ("LUM-BACKUP-MIB", "backupPersistentFileName"),
        ("LUM-BACKUP-MIB", "backupPersistentFileDescr"))
)
if mibBuilder.loadTexts:
    backupPersistentFileGroup.setStatus("current")

backupFileGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 7)
)
backupFileGroupV2.setObjects(
      *(("LUM-BACKUP-MIB", "backupFileIndex"),
        ("LUM-BACKUP-MIB", "backupFileName"),
        ("LUM-BACKUP-MIB", "backupFileDescr"),
        ("LUM-BACKUP-MIB", "backupFileLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupFileAdminStatus"),
        ("LUM-BACKUP-MIB", "backupFileOperStatus"),
        ("LUM-BACKUP-MIB", "backupFileRowStatus"),
        ("LUM-BACKUP-MIB", "backupFileUrl"))
)
if mibBuilder.loadTexts:
    backupFileGroupV2.setStatus("current")

backupGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 8)
)
backupGeneralGroupV4.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"))
)
if mibBuilder.loadTexts:
    backupGeneralGroupV4.setStatus("deprecated")

backupGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 9)
)
backupGeneralGroupV5.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"),
        ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralInstallConfigFile"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"))
)
if mibBuilder.loadTexts:
    backupGeneralGroupV5.setStatus("deprecated")

backupUploadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 10)
)
backupUploadGroup.setObjects(
      *(("LUM-BACKUP-MIB", "backupUploadServerAddr"),
        ("LUM-BACKUP-MIB", "backupUploadServerPath"),
        ("LUM-BACKUP-MIB", "backupUploadTimeHour"),
        ("LUM-BACKUP-MIB", "backupUploadAction"),
        ("LUM-BACKUP-MIB", "backupUploadResult"),
        ("LUM-BACKUP-MIB", "backupUploadLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupUploadFailure"),
        ("LUM-BACKUP-MIB", "backupUploadNextTime"),
        ("LUM-BACKUP-MIB", "backupUploadInstallUploadFile"))
)
if mibBuilder.loadTexts:
    backupUploadGroup.setStatus("deprecated")

backupGeneralGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 11)
)
backupGeneralGroupV6.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"),
        ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralInstallConfigFile"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"),
        ("LUM-BACKUP-MIB", "backupGeneralWarnForUnsaved"),
        ("LUM-BACKUP-MIB", "backupGeneralWarnUnsavedDelay"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChangesAlarm"))
)
if mibBuilder.loadTexts:
    backupGeneralGroupV6.setStatus("deprecated")

backupUploadGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 12)
)
backupUploadGroupV2.setObjects(
      *(("LUM-BACKUP-MIB", "backupUploadServerAddr"),
        ("LUM-BACKUP-MIB", "backupUploadServerPath"),
        ("LUM-BACKUP-MIB", "backupUploadTimeHour"),
        ("LUM-BACKUP-MIB", "backupUploadAction"),
        ("LUM-BACKUP-MIB", "backupUploadResult"),
        ("LUM-BACKUP-MIB", "backupUploadLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupUploadFailure"),
        ("LUM-BACKUP-MIB", "backupUploadNextTime"),
        ("LUM-BACKUP-MIB", "backupUploadInstallUploadFile"))
)
if mibBuilder.loadTexts:
    backupUploadGroupV2.setStatus("current")

backupUploadGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 13)
)
backupUploadGroupV3.setObjects(
      *(("LUM-BACKUP-MIB", "backupUploadServerAddr"),
        ("LUM-BACKUP-MIB", "backupUploadServerPath"),
        ("LUM-BACKUP-MIB", "backupUploadTimeHour"),
        ("LUM-BACKUP-MIB", "backupUploadAction"),
        ("LUM-BACKUP-MIB", "backupUploadResult"),
        ("LUM-BACKUP-MIB", "backupUploadLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupUploadFailure"),
        ("LUM-BACKUP-MIB", "backupUploadNextTime"),
        ("LUM-BACKUP-MIB", "backupUploadInstallUploadFile"),
        ("LUM-BACKUP-MIB", "backupUploadUploadNow"),
        ("LUM-BACKUP-MIB", "backupUploadStatus"),
        ("LUM-BACKUP-MIB", "backupUploadLocalFile"))
)
if mibBuilder.loadTexts:
    backupUploadGroupV3.setStatus("current")

backupGeneralGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 14)
)
backupGeneralGroupV7.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"),
        ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralInstallConfigFile"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"),
        ("LUM-BACKUP-MIB", "backupGeneralWarnForUnsaved"),
        ("LUM-BACKUP-MIB", "backupGeneralWarnUnsavedDelay"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChangesAlarm"),
        ("LUM-BACKUP-MIB", "backupGeneralSavedConfigurationGenerationId"))
)
if mibBuilder.loadTexts:
    backupGeneralGroupV7.setStatus("deprecated")

backupGeneralGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 15)
)
backupGeneralGroupV8.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"),
        ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralInstallConfigFile"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"),
        ("LUM-BACKUP-MIB", "backupGeneralWarnForUnsaved"),
        ("LUM-BACKUP-MIB", "backupGeneralWarnUnsavedDelay"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChangesAlarm"),
        ("LUM-BACKUP-MIB", "backupGeneralSavedConfigurationGenerationId"),
        ("LUM-BACKUP-MIB", "backupGeneralBackupScheme"))
)
if mibBuilder.loadTexts:
    backupGeneralGroupV8.setStatus("deprecated")

backupSftpUploadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 16)
)
backupSftpUploadGroup.setObjects(
      *(("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityAvailability"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCompressionTimestamp"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCrc"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityAction"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityFilePath"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityFilePath"))
)
if mibBuilder.loadTexts:
    backupSftpUploadGroup.setStatus("deprecated")

backupGeneralGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 17)
)
backupGeneralGroupV9.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChanges"),
        ("LUM-BACKUP-MIB", "backupGeneralFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralPersistentFileTableSize"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralPrimaryFileName"),
        ("LUM-BACKUP-MIB", "backupGeneralWarnForUnsaved"),
        ("LUM-BACKUP-MIB", "backupGeneralWarnUnsavedDelay"),
        ("LUM-BACKUP-MIB", "backupGeneralUnsavedChangesAlarm"),
        ("LUM-BACKUP-MIB", "backupGeneralSavedConfigurationGenerationId"),
        ("LUM-BACKUP-MIB", "backupGeneralBackupScheme"))
)
if mibBuilder.loadTexts:
    backupGeneralGroupV9.setStatus("current")

backupSftpUploadGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 1, 18)
)
backupSftpUploadGroupV2.setObjects(
      *(("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityAvailability"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCompressionTimestamp"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCrc"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityAction"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityFilePath"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityFilePath"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityRestoreNow"))
)
if mibBuilder.loadTexts:
    backupSftpUploadGroupV2.setStatus("current")

backupGeneralMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3, 1)
)
backupGeneralMinimalGroupV1.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralConfigLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalStateLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupGeneralGlobalConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    backupGeneralMinimalGroupV1.setStatus("current")

backupUploadMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3, 2)
)
backupUploadMinimalGroupV1.setObjects(
      *(("LUM-BACKUP-MIB", "backupUploadServerAddr"),
        ("LUM-BACKUP-MIB", "backupUploadTimeHour"),
        ("LUM-BACKUP-MIB", "backupUploadAction"),
        ("LUM-BACKUP-MIB", "backupUploadResult"),
        ("LUM-BACKUP-MIB", "backupUploadLastChangeTime"),
        ("LUM-BACKUP-MIB", "backupUploadFailure"),
        ("LUM-BACKUP-MIB", "backupUploadNextTime"),
        ("LUM-BACKUP-MIB", "backupUploadLocalFile"))
)
if mibBuilder.loadTexts:
    backupUploadMinimalGroupV1.setStatus("current")

backupSftpUploadMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3, 3)
)
backupSftpUploadMinimalGroupV1.setObjects(
      *(("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityAvailability"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCompressionTimestamp"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCrc"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityAction"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityFilePath"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityFilePath"))
)
if mibBuilder.loadTexts:
    backupSftpUploadMinimalGroupV1.setStatus("deprecated")

backupSftpUploadMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 3, 4)
)
backupSftpUploadMinimalGroupV2.setObjects(
      *(("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityAvailability"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCompressionTimestamp"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityCrc"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityAction"),
        ("LUM-BACKUP-MIB", "backupSftpUploadBackupEntityFilePath"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityFilePath"),
        ("LUM-BACKUP-MIB", "backupSftpUploadRestoreEntityRestoreNow"))
)
if mibBuilder.loadTexts:
    backupSftpUploadMinimalGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumBackupBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 1)
)
lumBackupBasicComplV1.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroup"),
        ("LUM-BACKUP-MIB", "backupFileGroup"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV1.setStatus(
        "deprecated"
    )

lumBackupBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 2)
)
lumBackupBasicComplV2.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV2"),
        ("LUM-BACKUP-MIB", "backupFileGroup"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV2.setStatus(
        "deprecated"
    )

lumBackupBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 3)
)
lumBackupBasicComplV3.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV3"),
        ("LUM-BACKUP-MIB", "backupFileGroup"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV3.setStatus(
        "deprecated"
    )

lumBackupBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 4)
)
lumBackupBasicComplV4.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV3"),
        ("LUM-BACKUP-MIB", "backupFileGroup"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV4.setStatus(
        "deprecated"
    )

lumBackupBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 5)
)
lumBackupBasicComplV5.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV3"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV5.setStatus(
        "deprecated"
    )

lumBackupBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 6)
)
lumBackupBasicComplV6.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV4"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV6.setStatus(
        "deprecated"
    )

lumBackupBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 7)
)
lumBackupBasicComplV7.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV5"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"),
        ("LUM-BACKUP-MIB", "backupUploadGroup"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV7.setStatus(
        "deprecated"
    )

lumBackupBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 8)
)
lumBackupBasicComplV8.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV5"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"),
        ("LUM-BACKUP-MIB", "backupUploadGroup"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV8.setStatus(
        "deprecated"
    )

lumBackupBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 9)
)
lumBackupBasicComplV9.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV6"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"),
        ("LUM-BACKUP-MIB", "backupUploadGroupV2"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV9.setStatus(
        "deprecated"
    )

lumBackupBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 10)
)
lumBackupBasicComplV10.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV6"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"),
        ("LUM-BACKUP-MIB", "backupUploadGroupV3"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV10.setStatus(
        "deprecated"
    )

lumBackupBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 11)
)
lumBackupBasicComplV11.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV7"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"),
        ("LUM-BACKUP-MIB", "backupUploadGroupV3"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV11.setStatus(
        "deprecated"
    )

lumBackupBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 12)
)
lumBackupBasicComplV12.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV8"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"),
        ("LUM-BACKUP-MIB", "backupUploadGroupV3"),
        ("LUM-BACKUP-MIB", "backupSftpUploadGroup"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV12.setStatus(
        "deprecated"
    )

lumBackupBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 13)
)
lumBackupBasicComplV13.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV9"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"),
        ("LUM-BACKUP-MIB", "backupUploadGroupV3"),
        ("LUM-BACKUP-MIB", "backupSftpUploadGroupV2"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV13.setStatus(
        "deprecated"
    )

lumBackupBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 2, 14)
)
lumBackupBasicComplV14.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralGroupV9"),
        ("LUM-BACKUP-MIB", "backupFileGroupV2"),
        ("LUM-BACKUP-MIB", "backupCommandGroup"),
        ("LUM-BACKUP-MIB", "backupPersistentFileGroup"),
        ("LUM-BACKUP-MIB", "backupUploadGroupV3"),
        ("LUM-BACKUP-MIB", "backupSftpUploadGroupV2"))
)
if mibBuilder.loadTexts:
    lumBackupBasicComplV14.setStatus(
        "current"
    )

lumBackupMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4, 1)
)
lumBackupMinimalComplV1.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralMinimalGroupV1"),
        ("LUM-BACKUP-MIB", "backupUploadMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumBackupMinimalComplV1.setStatus(
        "deprecated"
    )

lumBackupMinimalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4, 2)
)
lumBackupMinimalComplV2.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralMinimalGroupV1"),
        ("LUM-BACKUP-MIB", "backupUploadMinimalGroupV1"),
        ("LUM-BACKUP-MIB", "backupSftpUploadMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumBackupMinimalComplV2.setStatus(
        "deprecated"
    )

lumBackupMinimalComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4, 3)
)
lumBackupMinimalComplV3.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralMinimalGroupV1"),
        ("LUM-BACKUP-MIB", "backupUploadMinimalGroupV1"),
        ("LUM-BACKUP-MIB", "backupSftpUploadMinimalGroupV2"))
)
if mibBuilder.loadTexts:
    lumBackupMinimalComplV3.setStatus(
        "deprecated"
    )

lumBackupMinimalComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5, 1, 4, 4)
)
lumBackupMinimalComplV4.setObjects(
      *(("LUM-BACKUP-MIB", "backupGeneralMinimalGroupV1"),
        ("LUM-BACKUP-MIB", "backupUploadMinimalGroupV1"),
        ("LUM-BACKUP-MIB", "backupSftpUploadMinimalGroupV2"))
)
if mibBuilder.loadTexts:
    lumBackupMinimalComplV4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-BACKUP-MIB",
    **{"lumBackupMIBModule": lumBackupMIBModule,
       "lumBackupConfs": lumBackupConfs,
       "lumBackupGroups": lumBackupGroups,
       "backupGeneralGroup": backupGeneralGroup,
       "backupFileGroup": backupFileGroup,
       "backupCommandGroup": backupCommandGroup,
       "backupGeneralGroupV2": backupGeneralGroupV2,
       "backupGeneralGroupV3": backupGeneralGroupV3,
       "backupPersistentFileGroup": backupPersistentFileGroup,
       "backupFileGroupV2": backupFileGroupV2,
       "backupGeneralGroupV4": backupGeneralGroupV4,
       "backupGeneralGroupV5": backupGeneralGroupV5,
       "backupUploadGroup": backupUploadGroup,
       "backupGeneralGroupV6": backupGeneralGroupV6,
       "backupUploadGroupV2": backupUploadGroupV2,
       "backupUploadGroupV3": backupUploadGroupV3,
       "backupGeneralGroupV7": backupGeneralGroupV7,
       "backupGeneralGroupV8": backupGeneralGroupV8,
       "backupSftpUploadGroup": backupSftpUploadGroup,
       "backupGeneralGroupV9": backupGeneralGroupV9,
       "backupSftpUploadGroupV2": backupSftpUploadGroupV2,
       "lumBackupCompl": lumBackupCompl,
       "lumBackupBasicComplV1": lumBackupBasicComplV1,
       "lumBackupBasicComplV2": lumBackupBasicComplV2,
       "lumBackupBasicComplV3": lumBackupBasicComplV3,
       "lumBackupBasicComplV4": lumBackupBasicComplV4,
       "lumBackupBasicComplV5": lumBackupBasicComplV5,
       "lumBackupBasicComplV6": lumBackupBasicComplV6,
       "lumBackupBasicComplV7": lumBackupBasicComplV7,
       "lumBackupBasicComplV8": lumBackupBasicComplV8,
       "lumBackupBasicComplV9": lumBackupBasicComplV9,
       "lumBackupBasicComplV10": lumBackupBasicComplV10,
       "lumBackupBasicComplV11": lumBackupBasicComplV11,
       "lumBackupBasicComplV12": lumBackupBasicComplV12,
       "lumBackupBasicComplV13": lumBackupBasicComplV13,
       "lumBackupBasicComplV14": lumBackupBasicComplV14,
       "lumBackupMinimalGroups": lumBackupMinimalGroups,
       "backupGeneralMinimalGroupV1": backupGeneralMinimalGroupV1,
       "backupUploadMinimalGroupV1": backupUploadMinimalGroupV1,
       "backupSftpUploadMinimalGroupV1": backupSftpUploadMinimalGroupV1,
       "backupSftpUploadMinimalGroupV2": backupSftpUploadMinimalGroupV2,
       "lumBackupMinimalCompl": lumBackupMinimalCompl,
       "lumBackupMinimalComplV1": lumBackupMinimalComplV1,
       "lumBackupMinimalComplV2": lumBackupMinimalComplV2,
       "lumBackupMinimalComplV3": lumBackupMinimalComplV3,
       "lumBackupMinimalComplV4": lumBackupMinimalComplV4,
       "lumBackupMIBObjects": lumBackupMIBObjects,
       "backupGeneral": backupGeneral,
       "backupGeneralTestAndIncr": backupGeneralTestAndIncr,
       "backupGeneralMibSpecVersion": backupGeneralMibSpecVersion,
       "backupGeneralMibImplVersion": backupGeneralMibImplVersion,
       "backupGeneralLastChangeTime": backupGeneralLastChangeTime,
       "backupGeneralConfigLastChangeTime": backupGeneralConfigLastChangeTime,
       "backupGeneralUnsavedChanges": backupGeneralUnsavedChanges,
       "backupGeneralFileTableSize": backupGeneralFileTableSize,
       "backupGeneralPersistentFileTableSize": backupGeneralPersistentFileTableSize,
       "backupGeneralInstallConfigFile": backupGeneralInstallConfigFile,
       "backupGeneralGlobalStateLastChangeTime": backupGeneralGlobalStateLastChangeTime,
       "backupGeneralGlobalConfigLastChangeTime": backupGeneralGlobalConfigLastChangeTime,
       "backupGeneralPrimaryFileName": backupGeneralPrimaryFileName,
       "backupGeneralWarnForUnsaved": backupGeneralWarnForUnsaved,
       "backupGeneralWarnUnsavedDelay": backupGeneralWarnUnsavedDelay,
       "backupGeneralUnsavedChangesAlarm": backupGeneralUnsavedChangesAlarm,
       "backupGeneralSavedConfigurationGenerationId": backupGeneralSavedConfigurationGenerationId,
       "backupGeneralBackupScheme": backupGeneralBackupScheme,
       "backupFileList": backupFileList,
       "backupFileTable": backupFileTable,
       "backupFileEntry": backupFileEntry,
       "backupFileIndex": backupFileIndex,
       "backupFileName": backupFileName,
       "backupFileDescr": backupFileDescr,
       "backupFileLastChangeTime": backupFileLastChangeTime,
       "backupFileAdminStatus": backupFileAdminStatus,
       "backupFileOperStatus": backupFileOperStatus,
       "backupFileRowStatus": backupFileRowStatus,
       "backupFileUrl": backupFileUrl,
       "backupCommand": backupCommand,
       "backupCommandName": backupCommandName,
       "backupCommandDescr": backupCommandDescr,
       "backupCommandAdminStatus": backupCommandAdminStatus,
       "backupCommandAction": backupCommandAction,
       "backupCommandResult": backupCommandResult,
       "backupPersistentFileList": backupPersistentFileList,
       "backupPersistentFileTable": backupPersistentFileTable,
       "backupPersistentFileEntry": backupPersistentFileEntry,
       "backupPersistentFileIndex": backupPersistentFileIndex,
       "backupPersistentFileName": backupPersistentFileName,
       "backupPersistentFileDescr": backupPersistentFileDescr,
       "backupUpload": backupUpload,
       "backupUploadServerAddr": backupUploadServerAddr,
       "backupUploadServerPath": backupUploadServerPath,
       "backupUploadTimeHour": backupUploadTimeHour,
       "backupUploadAction": backupUploadAction,
       "backupUploadResult": backupUploadResult,
       "backupUploadLastChangeTime": backupUploadLastChangeTime,
       "backupUploadFailure": backupUploadFailure,
       "backupUploadNextTime": backupUploadNextTime,
       "backupUploadInstallUploadFile": backupUploadInstallUploadFile,
       "backupUploadStatus": backupUploadStatus,
       "backupUploadUploadNow": backupUploadUploadNow,
       "backupUploadLocalFile": backupUploadLocalFile,
       "backupSftpUpload": backupSftpUpload,
       "backupSftpUploadBackupEntityAvailability": backupSftpUploadBackupEntityAvailability,
       "backupSftpUploadBackupEntityCompressionTimestamp": backupSftpUploadBackupEntityCompressionTimestamp,
       "backupSftpUploadBackupEntityCrc": backupSftpUploadBackupEntityCrc,
       "backupSftpUploadRestoreEntityAction": backupSftpUploadRestoreEntityAction,
       "backupSftpUploadBackupEntityFilePath": backupSftpUploadBackupEntityFilePath,
       "backupSftpUploadRestoreEntityFilePath": backupSftpUploadRestoreEntityFilePath,
       "backupSftpUploadRestoreEntityRestoreNow": backupSftpUploadRestoreEntityRestoreNow}
)
