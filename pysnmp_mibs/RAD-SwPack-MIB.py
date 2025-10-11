# SNMP MIB module (RAD-SwPack-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-SwPack-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:39 2025
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

(agnFiles,
 alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason,
 fileSystemObjName,
 fileSystemObjType,
 fileSystemPath,
 fileSystemValidIndication,
 systemsEvents) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "agnFiles",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason",
    "fileSystemObjName",
    "fileSystemObjType",
    "fileSystemPath",
    "fileSystemValidIndication",
    "systemsEvents")

(FileType,
 SlotType) = mibBuilder.importSymbols(
    "RAD-TC",
    "FileType",
    "SlotType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

swPack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwPackTable_Object = MibTable
swPackTable = _SwPackTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 1)
)
if mibBuilder.loadTexts:
    swPackTable.setStatus("current")
_SwPackEntry_Object = MibTableRow
swPackEntry = _SwPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 1, 1)
)
swPackEntry.setIndexNames(
    (0, "RAD-GEN-MIB", "fileSystemPath"),
    (0, "RAD-GEN-MIB", "fileSystemObjType"),
    (0, "RAD-GEN-MIB", "fileSystemObjName"),
)
if mibBuilder.loadTexts:
    swPackEntry.setStatus("current")
_SwPackVersion_Type = SnmpAdminString
_SwPackVersion_Object = MibTableColumn
swPackVersion = _SwPackVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 1, 1, 1),
    _SwPackVersion_Type()
)
swPackVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackVersion.setStatus("current")


class _SwPackActivityState_Type(Integer32):
    """Custom type swPackActivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("ready", 2),
          ("previousActive", 3))
    )


_SwPackActivityState_Type.__name__ = "Integer32"
_SwPackActivityState_Object = MibTableColumn
swPackActivityState = _SwPackActivityState_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 1, 1, 2),
    _SwPackActivityState_Type()
)
swPackActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackActivityState.setStatus("current")
_SwPackCreateTime_Type = DateAndTime
_SwPackCreateTime_Object = MibTableColumn
swPackCreateTime = _SwPackCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 1, 1, 3),
    _SwPackCreateTime_Type()
)
swPackCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackCreateTime.setStatus("current")
_SwPackNumberOfFiles_Type = Unsigned32
_SwPackNumberOfFiles_Object = MibTableColumn
swPackNumberOfFiles = _SwPackNumberOfFiles_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 1, 1, 4),
    _SwPackNumberOfFiles_Type()
)
swPackNumberOfFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackNumberOfFiles.setStatus("current")
_SwPackFileTable_Object = MibTable
swPackFileTable = _SwPackFileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 2)
)
if mibBuilder.loadTexts:
    swPackFileTable.setStatus("current")
_SwPackFileEntry_Object = MibTableRow
swPackFileEntry = _SwPackFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 2, 1)
)
swPackFileEntry.setIndexNames(
    (0, "RAD-GEN-MIB", "fileSystemPath"),
    (0, "RAD-GEN-MIB", "fileSystemObjType"),
    (0, "RAD-GEN-MIB", "fileSystemObjName"),
    (0, "RAD-SwPack-MIB", "swPackFileIdx"),
)
if mibBuilder.loadTexts:
    swPackFileEntry.setStatus("current")
_SwPackFileIdx_Type = Unsigned32
_SwPackFileIdx_Object = MibTableColumn
swPackFileIdx = _SwPackFileIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 2, 1, 1),
    _SwPackFileIdx_Type()
)
swPackFileIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPackFileIdx.setStatus("current")
_SwPackFileType_Type = SnmpAdminString
_SwPackFileType_Object = MibTableColumn
swPackFileType = _SwPackFileType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 2, 1, 2),
    _SwPackFileType_Type()
)
swPackFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackFileType.setStatus("current")
_SwPackFileName_Type = SnmpAdminString
_SwPackFileName_Object = MibTableColumn
swPackFileName = _SwPackFileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 2, 1, 3),
    _SwPackFileName_Type()
)
swPackFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackFileName.setStatus("current")
_SwPackFileVer_Type = SnmpAdminString
_SwPackFileVer_Object = MibTableColumn
swPackFileVer = _SwPackFileVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 2, 1, 4),
    _SwPackFileVer_Type()
)
swPackFileVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackFileVer.setStatus("current")
_SwPackFileHwVer_Type = SnmpAdminString
_SwPackFileHwVer_Object = MibTableColumn
swPackFileHwVer = _SwPackFileHwVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 2, 1, 5),
    _SwPackFileHwVer_Type()
)
swPackFileHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackFileHwVer.setStatus("current")
_SwPackFileSize_Type = Unsigned32
_SwPackFileSize_Object = MibTableColumn
swPackFileSize = _SwPackFileSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 2, 1, 6),
    _SwPackFileSize_Type()
)
swPackFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackFileSize.setStatus("current")
_SwPackHandleTable_Object = MibTable
swPackHandleTable = _SwPackHandleTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3)
)
if mibBuilder.loadTexts:
    swPackHandleTable.setStatus("current")
_SwPackHandleEntry_Object = MibTableRow
swPackHandleEntry = _SwPackHandleEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1)
)
swPackHandleEntry.setIndexNames(
    (0, "RAD-SwPack-MIB", "swPackHandleIdx"),
)
if mibBuilder.loadTexts:
    swPackHandleEntry.setStatus("current")
_SwPackHandleIdx_Type = Unsigned32
_SwPackHandleIdx_Object = MibTableColumn
swPackHandleIdx = _SwPackHandleIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 1),
    _SwPackHandleIdx_Type()
)
swPackHandleIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPackHandleIdx.setStatus("current")
_SwPackHandlePath_Type = SnmpAdminString
_SwPackHandlePath_Object = MibTableColumn
swPackHandlePath = _SwPackHandlePath_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 2),
    _SwPackHandlePath_Type()
)
swPackHandlePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPackHandlePath.setStatus("current")
_SwPackHandleType_Type = FileType
_SwPackHandleType_Object = MibTableColumn
swPackHandleType = _SwPackHandleType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 3),
    _SwPackHandleType_Type()
)
swPackHandleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPackHandleType.setStatus("current")
_SwPackHandleName_Type = SnmpAdminString
_SwPackHandleName_Object = MibTableColumn
swPackHandleName = _SwPackHandleName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 4),
    _SwPackHandleName_Type()
)
swPackHandleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPackHandleName.setStatus("current")


class _SwPackHandleCmd_Type(Integer32):
    """Custom type swPackHandleCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("installIoManualReset", 2),
          ("undoInstall", 3),
          ("installAndReboot", 4),
          ("installAndRebootNoRestore", 5))
    )


_SwPackHandleCmd_Type.__name__ = "Integer32"
_SwPackHandleCmd_Object = MibTableColumn
swPackHandleCmd = _SwPackHandleCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 5),
    _SwPackHandleCmd_Type()
)
swPackHandleCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPackHandleCmd.setStatus("current")


class _SwPackHandleStatus_Type(Integer32):
    """Custom type swPackHandleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("endedOk", 2),
          ("inProgress", 3),
          ("slotFailure", 4),
          ("mainCardResetFailure", 5),
          ("configMigrationError", 6),
          ("otherFailure", 7),
          ("abortedByUser", 8),
          ("swUnconfirmed", 9),
          ("swUnconfirmedButUsed", 10),
          ("awaitingConfirmation", 11),
          ("awaitingIoCardReset", 12),
          ("inProgressReset", 13),
          ("swInstalledFromBoot", 14),
          ("swHwConflict", 15))
    )


_SwPackHandleStatus_Type.__name__ = "Integer32"
_SwPackHandleStatus_Object = MibTableColumn
swPackHandleStatus = _SwPackHandleStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 6),
    _SwPackHandleStatus_Type()
)
swPackHandleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackHandleStatus.setStatus("current")


class _SwPackHandleSlotMap_Type(OctetString):
    """Custom type swPackHandleSlotMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwPackHandleSlotMap_Type.__name__ = "OctetString"
_SwPackHandleSlotMap_Object = MibTableColumn
swPackHandleSlotMap = _SwPackHandleSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 7),
    _SwPackHandleSlotMap_Type()
)
swPackHandleSlotMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPackHandleSlotMap.setStatus("current")


class _SwPackHandleConfirmRequestCmd_Type(Integer32):
    """Custom type swPackHandleConfirmRequestCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SwPackHandleConfirmRequestCmd_Type.__name__ = "Integer32"
_SwPackHandleConfirmRequestCmd_Object = MibTableColumn
swPackHandleConfirmRequestCmd = _SwPackHandleConfirmRequestCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 8),
    _SwPackHandleConfirmRequestCmd_Type()
)
swPackHandleConfirmRequestCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPackHandleConfirmRequestCmd.setStatus("current")


class _SwPackHandleConfirmCmd_Type(Integer32):
    """Custom type swPackHandleConfirmCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("pending", 3),
          ("offError", 5))
    )


_SwPackHandleConfirmCmd_Type.__name__ = "Integer32"
_SwPackHandleConfirmCmd_Object = MibTableColumn
swPackHandleConfirmCmd = _SwPackHandleConfirmCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 9),
    _SwPackHandleConfirmCmd_Type()
)
swPackHandleConfirmCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPackHandleConfirmCmd.setStatus("current")


class _SwPackHandleConfirmTimer_Type(Unsigned32):
    """Custom type swPackHandleConfirmTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_SwPackHandleConfirmTimer_Type.__name__ = "Unsigned32"
_SwPackHandleConfirmTimer_Object = MibTableColumn
swPackHandleConfirmTimer = _SwPackHandleConfirmTimer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 10),
    _SwPackHandleConfirmTimer_Type()
)
swPackHandleConfirmTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPackHandleConfirmTimer.setStatus("current")
_SwPackHandleConfirmRemainingTime_Type = Unsigned32
_SwPackHandleConfirmRemainingTime_Object = MibTableColumn
swPackHandleConfirmRemainingTime = _SwPackHandleConfirmRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 3, 1, 11),
    _SwPackHandleConfirmRemainingTime_Type()
)
swPackHandleConfirmRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackHandleConfirmRemainingTime.setStatus("current")
_SwPackInstallationTable_Object = MibTable
swPackInstallationTable = _SwPackInstallationTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 4)
)
if mibBuilder.loadTexts:
    swPackInstallationTable.setStatus("current")
_SwPackInstallationEntry_Object = MibTableRow
swPackInstallationEntry = _SwPackInstallationEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 4, 1)
)
swPackInstallationEntry.setIndexNames(
    (0, "RAD-SwPack-MIB", "swPackInstallationSlotIdx"),
)
if mibBuilder.loadTexts:
    swPackInstallationEntry.setStatus("current")
_SwPackInstallationSlotIdx_Type = SlotType
_SwPackInstallationSlotIdx_Object = MibTableColumn
swPackInstallationSlotIdx = _SwPackInstallationSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 4, 1, 1),
    _SwPackInstallationSlotIdx_Type()
)
swPackInstallationSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPackInstallationSlotIdx.setStatus("current")


class _SwPackInstallationSlotStatus_Type(Integer32):
    """Custom type swPackInstallationSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("empty", 2),
          ("inProgress", 3),
          ("manualResetWait", 4),
          ("failure", 5))
    )


_SwPackInstallationSlotStatus_Type.__name__ = "Integer32"
_SwPackInstallationSlotStatus_Object = MibTableColumn
swPackInstallationSlotStatus = _SwPackInstallationSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 67, 4, 4, 1, 2),
    _SwPackInstallationSlotStatus_Type()
)
swPackInstallationSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPackInstallationSlotStatus.setStatus("current")

# Managed Objects groups


# Notification objects

systemSoftwareInstallStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 42)
)
systemSoftwareInstallStart.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-SwPack-MIB", "swPackHandleCmd"),
        ("RAD-SwPack-MIB", "swPackVersion"))
)
if mibBuilder.loadTexts:
    systemSoftwareInstallStart.setStatus(
        "current"
    )

systemSoftwareInstallEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 43)
)
systemSoftwareInstallEnd.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-GEN-MIB", "fileSystemValidIndication"),
        ("RAD-SwPack-MIB", "swPackHandleStatus"),
        ("RAD-SwPack-MIB", "swPackVersion"))
)
if mibBuilder.loadTexts:
    systemSoftwareInstallEnd.setStatus(
        "current"
    )

systemSwPackCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 61)
)
systemSwPackCorrupted.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-SwPack-MIB", "swPackHandleName"))
)
if mibBuilder.loadTexts:
    systemSwPackCorrupted.setStatus(
        "current"
    )

systemActiveSoftwareChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 83)
)
systemActiveSoftwareChanged.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-SwPack-MIB", "swPackVersion"))
)
if mibBuilder.loadTexts:
    systemActiveSoftwareChanged.setStatus(
        "current"
    )

systemRunningConfigSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 84)
)
systemRunningConfigSaved.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    systemRunningConfigSaved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-SwPack-MIB",
    **{"systemSoftwareInstallStart": systemSoftwareInstallStart,
       "systemSoftwareInstallEnd": systemSoftwareInstallEnd,
       "systemSwPackCorrupted": systemSwPackCorrupted,
       "systemActiveSoftwareChanged": systemActiveSoftwareChanged,
       "systemRunningConfigSaved": systemRunningConfigSaved,
       "swPack": swPack,
       "swPackTable": swPackTable,
       "swPackEntry": swPackEntry,
       "swPackVersion": swPackVersion,
       "swPackActivityState": swPackActivityState,
       "swPackCreateTime": swPackCreateTime,
       "swPackNumberOfFiles": swPackNumberOfFiles,
       "swPackFileTable": swPackFileTable,
       "swPackFileEntry": swPackFileEntry,
       "swPackFileIdx": swPackFileIdx,
       "swPackFileType": swPackFileType,
       "swPackFileName": swPackFileName,
       "swPackFileVer": swPackFileVer,
       "swPackFileHwVer": swPackFileHwVer,
       "swPackFileSize": swPackFileSize,
       "swPackHandleTable": swPackHandleTable,
       "swPackHandleEntry": swPackHandleEntry,
       "swPackHandleIdx": swPackHandleIdx,
       "swPackHandlePath": swPackHandlePath,
       "swPackHandleType": swPackHandleType,
       "swPackHandleName": swPackHandleName,
       "swPackHandleCmd": swPackHandleCmd,
       "swPackHandleStatus": swPackHandleStatus,
       "swPackHandleSlotMap": swPackHandleSlotMap,
       "swPackHandleConfirmRequestCmd": swPackHandleConfirmRequestCmd,
       "swPackHandleConfirmCmd": swPackHandleConfirmCmd,
       "swPackHandleConfirmTimer": swPackHandleConfirmTimer,
       "swPackHandleConfirmRemainingTime": swPackHandleConfirmRemainingTime,
       "swPackInstallationTable": swPackInstallationTable,
       "swPackInstallationEntry": swPackInstallationEntry,
       "swPackInstallationSlotIdx": swPackInstallationSlotIdx,
       "swPackInstallationSlotStatus": swPackInstallationSlotStatus}
)
