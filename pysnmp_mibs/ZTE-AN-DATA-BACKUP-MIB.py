# SNMP MIB module (ZTE-AN-DATA-BACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-DATA-BACKUP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:36 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnDataBackupMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18)
)
if mibBuilder.loadTexts:
    zxAnDataBackupMib.setRevisions(
        ("2011-05-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnDataBackupObjects_ObjectIdentity = ObjectIdentity
zxAnDataBackupObjects = _ZxAnDataBackupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2)
)
_ZxAnDataAutoBackupConfTable_Object = MibTable
zxAnDataAutoBackupConfTable = _ZxAnDataAutoBackupConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnDataAutoBackupConfTable.setStatus("current")
_ZxAnDataAutoBackupConfEntry_Object = MibTableRow
zxAnDataAutoBackupConfEntry = _ZxAnDataAutoBackupConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 5, 1)
)
zxAnDataAutoBackupConfEntry.setIndexNames(
    (0, "ZTE-AN-DATA-BACKUP-MIB", "zxAnDataAutoBackupType"),
)
if mibBuilder.loadTexts:
    zxAnDataAutoBackupConfEntry.setStatus("current")


class _ZxAnDataAutoBackupType_Type(Integer32):
    """Custom type zxAnDataAutoBackupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              31)
        )
    )
    namedValues = NamedValues(
        *(("periodBackupConfiguration", 1),
          ("periodBackupLog", 3),
          ("periodBackupSoftware", 5),
          ("backupConfigurationWhenChanged", 31))
    )


_ZxAnDataAutoBackupType_Type.__name__ = "Integer32"
_ZxAnDataAutoBackupType_Object = MibTableColumn
zxAnDataAutoBackupType = _ZxAnDataAutoBackupType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 5, 1, 1),
    _ZxAnDataAutoBackupType_Type()
)
zxAnDataAutoBackupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDataAutoBackupType.setStatus("current")


class _ZxAnDataAutoBackupEnable_Type(Integer32):
    """Custom type zxAnDataAutoBackupEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnDataAutoBackupEnable_Type.__name__ = "Integer32"
_ZxAnDataAutoBackupEnable_Object = MibTableColumn
zxAnDataAutoBackupEnable = _ZxAnDataAutoBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 5, 1, 2),
    _ZxAnDataAutoBackupEnable_Type()
)
zxAnDataAutoBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDataAutoBackupEnable.setStatus("current")
_ZxAnDataAutoBackupStartTime_Type = DateAndTime
_ZxAnDataAutoBackupStartTime_Object = MibTableColumn
zxAnDataAutoBackupStartTime = _ZxAnDataAutoBackupStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 5, 1, 3),
    _ZxAnDataAutoBackupStartTime_Type()
)
zxAnDataAutoBackupStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDataAutoBackupStartTime.setStatus("current")


class _ZxAnDataAutoBackupInterval_Type(Integer32):
    """Custom type zxAnDataAutoBackupInterval based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8760),
    )


_ZxAnDataAutoBackupInterval_Type.__name__ = "Integer32"
_ZxAnDataAutoBackupInterval_Object = MibTableColumn
zxAnDataAutoBackupInterval = _ZxAnDataAutoBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 5, 1, 4),
    _ZxAnDataAutoBackupInterval_Type()
)
zxAnDataAutoBackupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDataAutoBackupInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnDataAutoBackupInterval.setUnits("hours")


class _ZxAnDataAutoBackupHoldOffTime_Type(Integer32):
    """Custom type zxAnDataAutoBackupHoldOffTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8760),
    )


_ZxAnDataAutoBackupHoldOffTime_Type.__name__ = "Integer32"
_ZxAnDataAutoBackupHoldOffTime_Object = MibTableColumn
zxAnDataAutoBackupHoldOffTime = _ZxAnDataAutoBackupHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 5, 1, 5),
    _ZxAnDataAutoBackupHoldOffTime_Type()
)
zxAnDataAutoBackupHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDataAutoBackupHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnDataAutoBackupHoldOffTime.setUnits("hours")


class _ZxAnDataAutoBackupMaxHoldOffTime_Type(Integer32):
    """Custom type zxAnDataAutoBackupMaxHoldOffTime based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8760),
    )


_ZxAnDataAutoBackupMaxHoldOffTime_Type.__name__ = "Integer32"
_ZxAnDataAutoBackupMaxHoldOffTime_Object = MibTableColumn
zxAnDataAutoBackupMaxHoldOffTime = _ZxAnDataAutoBackupMaxHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 5, 1, 6),
    _ZxAnDataAutoBackupMaxHoldOffTime_Type()
)
zxAnDataAutoBackupMaxHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDataAutoBackupMaxHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnDataAutoBackupMaxHoldOffTime.setUnits("hours")
_ZxAnDataManualBackupConfTable_Object = MibTable
zxAnDataManualBackupConfTable = _ZxAnDataManualBackupConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 6)
)
if mibBuilder.loadTexts:
    zxAnDataManualBackupConfTable.setStatus("current")
_ZxAnDataManualBackupConfEntry_Object = MibTableRow
zxAnDataManualBackupConfEntry = _ZxAnDataManualBackupConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 6, 1)
)
zxAnDataManualBackupConfEntry.setIndexNames(
    (0, "ZTE-AN-DATA-BACKUP-MIB", "zxAnDataManualBackupType"),
)
if mibBuilder.loadTexts:
    zxAnDataManualBackupConfEntry.setStatus("current")


class _ZxAnDataManualBackupType_Type(Integer32):
    """Custom type zxAnDataManualBackupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("manualBackupConfiguration", 2),
          ("manualBackupLog", 4),
          ("manualBackupSoftware", 6))
    )


_ZxAnDataManualBackupType_Type.__name__ = "Integer32"
_ZxAnDataManualBackupType_Object = MibTableColumn
zxAnDataManualBackupType = _ZxAnDataManualBackupType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 6, 1, 1),
    _ZxAnDataManualBackupType_Type()
)
zxAnDataManualBackupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDataManualBackupType.setStatus("current")


class _ZxAnDataManualBackupAction_Type(Integer32):
    """Custom type zxAnDataManualBackupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_ZxAnDataManualBackupAction_Type.__name__ = "Integer32"
_ZxAnDataManualBackupAction_Object = MibTableColumn
zxAnDataManualBackupAction = _ZxAnDataManualBackupAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 6, 1, 2),
    _ZxAnDataManualBackupAction_Type()
)
zxAnDataManualBackupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDataManualBackupAction.setStatus("current")
_ZxAnDataBackupStatusTable_Object = MibTable
zxAnDataBackupStatusTable = _ZxAnDataBackupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7)
)
if mibBuilder.loadTexts:
    zxAnDataBackupStatusTable.setStatus("current")
_ZxAnDataBackupStatusEntry_Object = MibTableRow
zxAnDataBackupStatusEntry = _ZxAnDataBackupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1)
)
zxAnDataBackupStatusEntry.setIndexNames(
    (0, "ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupType"),
)
if mibBuilder.loadTexts:
    zxAnDataBackupStatusEntry.setStatus("current")


class _ZxAnDataBackupType_Type(Integer32):
    """Custom type zxAnDataBackupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              31)
        )
    )
    namedValues = NamedValues(
        *(("periodBackupConfiguration", 1),
          ("manualBackupConfiguration", 2),
          ("periodBackupLog", 3),
          ("manualBackupLog", 4),
          ("periodBackupSoftware", 5),
          ("manualBackupSoftware", 6),
          ("backupConfigurationWhenChanged", 31))
    )


_ZxAnDataBackupType_Type.__name__ = "Integer32"
_ZxAnDataBackupType_Object = MibTableColumn
zxAnDataBackupType = _ZxAnDataBackupType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1, 1),
    _ZxAnDataBackupType_Type()
)
zxAnDataBackupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDataBackupType.setStatus("current")
_ZxAnDataBackupCurrStartTime_Type = DateAndTime
_ZxAnDataBackupCurrStartTime_Object = MibTableColumn
zxAnDataBackupCurrStartTime = _ZxAnDataBackupCurrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1, 2),
    _ZxAnDataBackupCurrStartTime_Type()
)
zxAnDataBackupCurrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDataBackupCurrStartTime.setStatus("current")


class _ZxAnDataBackupCurrFileName_Type(DisplayString):
    """Custom type zxAnDataBackupCurrFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnDataBackupCurrFileName_Type.__name__ = "DisplayString"
_ZxAnDataBackupCurrFileName_Object = MibTableColumn
zxAnDataBackupCurrFileName = _ZxAnDataBackupCurrFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1, 3),
    _ZxAnDataBackupCurrFileName_Type()
)
zxAnDataBackupCurrFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDataBackupCurrFileName.setStatus("current")
_ZxAnDataBackupCurrFileSize_Type = Integer32
_ZxAnDataBackupCurrFileSize_Object = MibTableColumn
zxAnDataBackupCurrFileSize = _ZxAnDataBackupCurrFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1, 4),
    _ZxAnDataBackupCurrFileSize_Type()
)
zxAnDataBackupCurrFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDataBackupCurrFileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnDataBackupCurrFileSize.setUnits("bytes")


class _ZxAnDataBackupCurrFileProgress_Type(Integer32):
    """Custom type zxAnDataBackupCurrFileProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnDataBackupCurrFileProgress_Type.__name__ = "Integer32"
_ZxAnDataBackupCurrFileProgress_Object = MibTableColumn
zxAnDataBackupCurrFileProgress = _ZxAnDataBackupCurrFileProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1, 5),
    _ZxAnDataBackupCurrFileProgress_Type()
)
zxAnDataBackupCurrFileProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDataBackupCurrFileProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnDataBackupCurrFileProgress.setUnits("percent")
_ZxAnDataBackupTotalFiles_Type = Integer32
_ZxAnDataBackupTotalFiles_Object = MibTableColumn
zxAnDataBackupTotalFiles = _ZxAnDataBackupTotalFiles_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1, 6),
    _ZxAnDataBackupTotalFiles_Type()
)
zxAnDataBackupTotalFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDataBackupTotalFiles.setStatus("current")
_ZxAnDataBackupSuccessFiles_Type = Integer32
_ZxAnDataBackupSuccessFiles_Object = MibTableColumn
zxAnDataBackupSuccessFiles = _ZxAnDataBackupSuccessFiles_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1, 7),
    _ZxAnDataBackupSuccessFiles_Type()
)
zxAnDataBackupSuccessFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDataBackupSuccessFiles.setStatus("current")


class _ZxAnDataBackupStatus_Type(Integer32):
    """Custom type zxAnDataBackupStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnDataBackupStatus_Type.__name__ = "Integer32"
_ZxAnDataBackupStatus_Object = MibTableColumn
zxAnDataBackupStatus = _ZxAnDataBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1, 8),
    _ZxAnDataBackupStatus_Type()
)
zxAnDataBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDataBackupStatus.setStatus("current")


class _ZxAnDataBackupFailedReason_Type(Integer32):
    """Custom type zxAnDataBackupFailedReason based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("configSaving", 2),
          ("backupInProgress", 3),
          ("fileServerUnconfigured", 4),
          ("fileServerConnectFailed", 5),
          ("fileServerLoginFailed", 6),
          ("fileServerPathError", 7),
          ("fileServerProtocolTypeError", 8),
          ("fileAccessError", 9),
          ("otherErrors", 255))
    )


_ZxAnDataBackupFailedReason_Type.__name__ = "Integer32"
_ZxAnDataBackupFailedReason_Object = MibTableColumn
zxAnDataBackupFailedReason = _ZxAnDataBackupFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 2, 7, 1, 9),
    _ZxAnDataBackupFailedReason_Type()
)
zxAnDataBackupFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDataBackupFailedReason.setStatus("current")
_ZxAnDataBackupNotifications_ObjectIdentity = ObjectIdentity
zxAnDataBackupNotifications = _ZxAnDataBackupNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 3)
)
_ZxAnDataBackupConformance_ObjectIdentity = ObjectIdentity
zxAnDataBackupConformance = _ZxAnDataBackupConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 4)
)
_ZxAnDataBackupCompliances_ObjectIdentity = ObjectIdentity
zxAnDataBackupCompliances = _ZxAnDataBackupCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 4, 1)
)
_ZxAnDataBackupGroups_ObjectIdentity = ObjectIdentity
zxAnDataBackupGroups = _ZxAnDataBackupGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 4, 2)
)

# Managed Objects groups

zxAnDataAutoBackupConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 4, 2, 1)
)
zxAnDataAutoBackupConfGroup.setObjects(
      *(("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataAutoBackupEnable"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataAutoBackupStartTime"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataAutoBackupInterval"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataAutoBackupHoldOffTime"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataAutoBackupMaxHoldOffTime"))
)
if mibBuilder.loadTexts:
    zxAnDataAutoBackupConfGroup.setStatus("current")

zxAnDataManualBackupConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 4, 2, 2)
)
zxAnDataManualBackupConfGroup.setObjects(
    ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataManualBackupAction")
)
if mibBuilder.loadTexts:
    zxAnDataManualBackupConfGroup.setStatus("current")

zxAnDataBackupStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 4, 2, 3)
)
zxAnDataBackupStatusGroup.setObjects(
      *(("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupCurrStartTime"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupCurrFileName"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupCurrFileSize"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupCurrFileProgress"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupTotalFiles"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupSuccessFiles"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupStatus"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnDataBackupStatusGroup.setStatus("current")

zxAnDataBackuptrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 4, 2, 4)
)
zxAnDataBackuptrapsGroup.setObjects(
    ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupFinished")
)
if mibBuilder.loadTexts:
    zxAnDataBackuptrapsGroup.setStatus("current")


# Notification objects

zxAnDataBackupFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 3, 1)
)
zxAnDataBackupFinished.setObjects(
      *(("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupCurrStartTime"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupStatus"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnDataBackupFinished.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

zxAnDataBackupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 18, 4, 1, 1)
)
zxAnDataBackupCompliance.setObjects(
      *(("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataAutoBackupConfGroup"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataManualBackupConfGroup"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackupStatusGroup"),
        ("ZTE-AN-DATA-BACKUP-MIB", "zxAnDataBackuptrapsGroup"))
)
if mibBuilder.loadTexts:
    zxAnDataBackupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-DATA-BACKUP-MIB",
    **{"zxAnDataBackupMib": zxAnDataBackupMib,
       "zxAnDataBackupObjects": zxAnDataBackupObjects,
       "zxAnDataAutoBackupConfTable": zxAnDataAutoBackupConfTable,
       "zxAnDataAutoBackupConfEntry": zxAnDataAutoBackupConfEntry,
       "zxAnDataAutoBackupType": zxAnDataAutoBackupType,
       "zxAnDataAutoBackupEnable": zxAnDataAutoBackupEnable,
       "zxAnDataAutoBackupStartTime": zxAnDataAutoBackupStartTime,
       "zxAnDataAutoBackupInterval": zxAnDataAutoBackupInterval,
       "zxAnDataAutoBackupHoldOffTime": zxAnDataAutoBackupHoldOffTime,
       "zxAnDataAutoBackupMaxHoldOffTime": zxAnDataAutoBackupMaxHoldOffTime,
       "zxAnDataManualBackupConfTable": zxAnDataManualBackupConfTable,
       "zxAnDataManualBackupConfEntry": zxAnDataManualBackupConfEntry,
       "zxAnDataManualBackupType": zxAnDataManualBackupType,
       "zxAnDataManualBackupAction": zxAnDataManualBackupAction,
       "zxAnDataBackupStatusTable": zxAnDataBackupStatusTable,
       "zxAnDataBackupStatusEntry": zxAnDataBackupStatusEntry,
       "zxAnDataBackupType": zxAnDataBackupType,
       "zxAnDataBackupCurrStartTime": zxAnDataBackupCurrStartTime,
       "zxAnDataBackupCurrFileName": zxAnDataBackupCurrFileName,
       "zxAnDataBackupCurrFileSize": zxAnDataBackupCurrFileSize,
       "zxAnDataBackupCurrFileProgress": zxAnDataBackupCurrFileProgress,
       "zxAnDataBackupTotalFiles": zxAnDataBackupTotalFiles,
       "zxAnDataBackupSuccessFiles": zxAnDataBackupSuccessFiles,
       "zxAnDataBackupStatus": zxAnDataBackupStatus,
       "zxAnDataBackupFailedReason": zxAnDataBackupFailedReason,
       "zxAnDataBackupNotifications": zxAnDataBackupNotifications,
       "zxAnDataBackupFinished": zxAnDataBackupFinished,
       "zxAnDataBackupConformance": zxAnDataBackupConformance,
       "zxAnDataBackupCompliances": zxAnDataBackupCompliances,
       "zxAnDataBackupCompliance": zxAnDataBackupCompliance,
       "zxAnDataBackupGroups": zxAnDataBackupGroups,
       "zxAnDataAutoBackupConfGroup": zxAnDataAutoBackupConfGroup,
       "zxAnDataManualBackupConfGroup": zxAnDataManualBackupConfGroup,
       "zxAnDataBackupStatusGroup": zxAnDataBackupStatusGroup,
       "zxAnDataBackuptrapsGroup": zxAnDataBackuptrapsGroup}
)
