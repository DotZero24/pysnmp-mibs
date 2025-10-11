# SNMP MIB module (OA-DEV-UPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-DEV-UPGRADE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:51 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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
 enterprises,
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
    "enterprises",
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

oaDevUpgrade = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20)
)
if mibBuilder.loadTexts:
    oaDevUpgrade.setRevisions(
        ("2010-11-25 00:00",
         "2010-04-26 00:00",
         "2009-04-22 00:00",
         "2006-11-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PeriodicityDateAndTime(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d,1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
    )



# MIB Managed Objects in the order of their OIDs

_NbDeviceConfig_ObjectIdentity = ObjectIdentity
nbDeviceConfig = _NbDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11)
)
_NbDevGen_ObjectIdentity = ObjectIdentity
nbDevGen = _NbDevGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1)
)
_OaDevUpgrNotifications_ObjectIdentity = ObjectIdentity
oaDevUpgrNotifications = _OaDevUpgrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 0)
)


class _OaDevUpgrGenSupport_Type(Integer32):
    """Custom type oaDevUpgrGenSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OaDevUpgrGenSupport_Type.__name__ = "Integer32"
_OaDevUpgrGenSupport_Object = MibScalar
oaDevUpgrGenSupport = _OaDevUpgrGenSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 1),
    _OaDevUpgrGenSupport_Type()
)
oaDevUpgrGenSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevUpgrGenSupport.setStatus("current")
_OaDevUpgrTable_Object = MibTable
oaDevUpgrTable = _OaDevUpgrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2)
)
if mibBuilder.loadTexts:
    oaDevUpgrTable.setStatus("current")
_OaDevUpgrEntry_Object = MibTableRow
oaDevUpgrEntry = _OaDevUpgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1)
)
oaDevUpgrEntry.setIndexNames(
    (0, "OA-DEV-UPGRADE-MIB", "oaDevUpgrType"),
)
if mibBuilder.loadTexts:
    oaDevUpgrEntry.setStatus("current")


class _OaDevUpgrType_Type(Integer32):
    """Custom type oaDevUpgrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("upgradeSoftware", 1),
          ("getStartupConfig", 2),
          ("putStartupConfig", 3),
          ("getRunningConfig", 4),
          ("putRunningConfig", 5),
          ("resetDevice", 6),
          ("upgradeFpga", 7))
    )


_OaDevUpgrType_Type.__name__ = "Integer32"
_OaDevUpgrType_Object = MibTableColumn
oaDevUpgrType = _OaDevUpgrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 1),
    _OaDevUpgrType_Type()
)
oaDevUpgrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oaDevUpgrType.setStatus("current")


class _OaDevUpgrProtocolApp_Type(Integer32):
    """Custom type oaDevUpgrProtocolApp based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tftpClient", 2),
          ("ftpClient", 3),
          ("scpClient", 4),
          ("sftpClient", 5),
          ("localFile", 6))
    )


_OaDevUpgrProtocolApp_Type.__name__ = "Integer32"
_OaDevUpgrProtocolApp_Object = MibTableColumn
oaDevUpgrProtocolApp = _OaDevUpgrProtocolApp_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 2),
    _OaDevUpgrProtocolApp_Type()
)
oaDevUpgrProtocolApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrProtocolApp.setStatus("current")


class _OaDevUpgrServerAddressType_Type(InetAddressType):
    """Custom type oaDevUpgrServerAddressType based on InetAddressType"""
    defaultValue = 0


_OaDevUpgrServerAddressType_Type.__name__ = "InetAddressType"
_OaDevUpgrServerAddressType_Object = MibTableColumn
oaDevUpgrServerAddressType = _OaDevUpgrServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 3),
    _OaDevUpgrServerAddressType_Type()
)
oaDevUpgrServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrServerAddressType.setStatus("current")


class _OaDevUpgrServerAddress_Type(InetAddress):
    """Custom type oaDevUpgrServerAddress based on InetAddress"""
    defaultHexValue = ""


_OaDevUpgrServerAddress_Type.__name__ = "InetAddress"
_OaDevUpgrServerAddress_Object = MibTableColumn
oaDevUpgrServerAddress = _OaDevUpgrServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 4),
    _OaDevUpgrServerAddress_Type()
)
oaDevUpgrServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrServerAddress.setStatus("current")
_OaDevUpgrRemoteDir_Type = DisplayString
_OaDevUpgrRemoteDir_Object = MibTableColumn
oaDevUpgrRemoteDir = _OaDevUpgrRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 5),
    _OaDevUpgrRemoteDir_Type()
)
oaDevUpgrRemoteDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrRemoteDir.setStatus("current")
_OaDevUpgrRemoteFileName_Type = DisplayString
_OaDevUpgrRemoteFileName_Object = MibTableColumn
oaDevUpgrRemoteFileName = _OaDevUpgrRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 6),
    _OaDevUpgrRemoteFileName_Type()
)
oaDevUpgrRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrRemoteFileName.setStatus("current")


class _OaDevUpgrPeriodicity_Type(Integer32):
    """Custom type oaDevUpgrPeriodicity based on Integer32"""
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
        *(("once", 1),
          ("everyMonth", 2),
          ("everyWeek", 3),
          ("everyDay", 4))
    )


_OaDevUpgrPeriodicity_Type.__name__ = "Integer32"
_OaDevUpgrPeriodicity_Object = MibTableColumn
oaDevUpgrPeriodicity = _OaDevUpgrPeriodicity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 7),
    _OaDevUpgrPeriodicity_Type()
)
oaDevUpgrPeriodicity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrPeriodicity.setStatus("current")
_OaDevUpgrPeriodDateTime_Type = PeriodicityDateAndTime
_OaDevUpgrPeriodDateTime_Object = MibTableColumn
oaDevUpgrPeriodDateTime = _OaDevUpgrPeriodDateTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 8),
    _OaDevUpgrPeriodDateTime_Type()
)
oaDevUpgrPeriodDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrPeriodDateTime.setStatus("current")


class _OaDevUpgrResetDevice_Type(Integer32):
    """Custom type oaDevUpgrResetDevice based on Integer32"""
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
        *(("other", 1),
          ("resetDeviceAfterAction", 2),
          ("dontResetDeviceAfterAction", 3),
          ("resetDeviceWithDelay", 4))
    )


_OaDevUpgrResetDevice_Type.__name__ = "Integer32"
_OaDevUpgrResetDevice_Object = MibTableColumn
oaDevUpgrResetDevice = _OaDevUpgrResetDevice_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 9),
    _OaDevUpgrResetDevice_Type()
)
oaDevUpgrResetDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrResetDevice.setStatus("current")


class _OaDevUpgrOperStatus_Type(Integer32):
    """Custom type oaDevUpgrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("waitForSchedule", 2),
          ("actionInProcess", 3),
          ("actionCompletedOk", 4),
          ("actionError", 5),
          ("actionCanceled", 6))
    )


_OaDevUpgrOperStatus_Type.__name__ = "Integer32"
_OaDevUpgrOperStatus_Object = MibTableColumn
oaDevUpgrOperStatus = _OaDevUpgrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 10),
    _OaDevUpgrOperStatus_Type()
)
oaDevUpgrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevUpgrOperStatus.setStatus("current")


class _OaDevUpgrAdminStatus_Type(Integer32):
    """Custom type oaDevUpgrAdminStatus based on Integer32"""
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
          ("startNow", 2),
          ("scheduleAction", 3),
          ("cancelScheduledAction", 4),
          ("removeLocalFile", 5))
    )


_OaDevUpgrAdminStatus_Type.__name__ = "Integer32"
_OaDevUpgrAdminStatus_Object = MibTableColumn
oaDevUpgrAdminStatus = _OaDevUpgrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 11),
    _OaDevUpgrAdminStatus_Type()
)
oaDevUpgrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrAdminStatus.setStatus("current")
_OaDevUpgrUsername_Type = DisplayString
_OaDevUpgrUsername_Object = MibTableColumn
oaDevUpgrUsername = _OaDevUpgrUsername_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 12),
    _OaDevUpgrUsername_Type()
)
oaDevUpgrUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrUsername.setStatus("current")
_OaDevUpgrPassword_Type = DisplayString
_OaDevUpgrPassword_Object = MibTableColumn
oaDevUpgrPassword = _OaDevUpgrPassword_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 13),
    _OaDevUpgrPassword_Type()
)
oaDevUpgrPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrPassword.setStatus("current")
_OaDevUpgrServerAddressText_Type = DisplayString
_OaDevUpgrServerAddressText_Object = MibTableColumn
oaDevUpgrServerAddressText = _OaDevUpgrServerAddressText_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 14),
    _OaDevUpgrServerAddressText_Type()
)
oaDevUpgrServerAddressText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevUpgrServerAddressText.setStatus("current")


class _OaDevUpgrErrorStatus_Type(Integer32):
    """Custom type oaDevUpgrErrorStatus based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("operationNotPermitted", 2),
          ("invalidBootPartition", 3),
          ("mergeScriptFailure", 4),
          ("mergeScriptMissing", 5),
          ("invalidAction", 6),
          ("missingParameters", 7),
          ("serverUnavailable", 8),
          ("cannotGetGateway", 9),
          ("cannotGetNetworkMask", 10),
          ("invalidGetMethod", 11),
          ("fileTransferFailure", 12),
          ("invalidSoftwareVersionType", 13),
          ("mupgradeScriptMissing", 14),
          ("invalidConfigFileType", 15),
          ("missingRemoteUserParameter", 16),
          ("loginFailure", 17),
          ("noSuchFile", 18),
          ("cannotSetBootpart", 19),
          ("cannotGetBootpart", 20),
          ("resetFailure", 21),
          ("postResetFailure", 22),
          ("wrongUpgrType", 23),
          ("emptyFileName", 24),
          ("unknownError", 25),
          ("startProcessFailed", 26),
          ("getPartitionToogleFlagFailed", 27),
          ("setPartitionToogleFlagFailed", 28),
          ("tooLongCommandError", 29),
          ("backupCurrentStartupConfigError", 30),
          ("unsupportedAppProtocol", 31),
          ("invalidFileFormat", 32),
          ("writeRunningConfigFileFailed", 33),
          ("downloadFpgaImageFailed", 34))
    )


_OaDevUpgrErrorStatus_Type.__name__ = "Integer32"
_OaDevUpgrErrorStatus_Object = MibTableColumn
oaDevUpgrErrorStatus = _OaDevUpgrErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 15),
    _OaDevUpgrErrorStatus_Type()
)
oaDevUpgrErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevUpgrErrorStatus.setStatus("current")


class _OaDevUpgrResetDelay_Type(Integer32):
    """Custom type oaDevUpgrResetDelay based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_OaDevUpgrResetDelay_Type.__name__ = "Integer32"
_OaDevUpgrResetDelay_Object = MibTableColumn
oaDevUpgrResetDelay = _OaDevUpgrResetDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 2, 1, 16),
    _OaDevUpgrResetDelay_Type()
)
oaDevUpgrResetDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevUpgrResetDelay.setStatus("current")
if mibBuilder.loadTexts:
    oaDevUpgrResetDelay.setUnits("Seconds")
_OaDevConfigAudit_ObjectIdentity = ObjectIdentity
oaDevConfigAudit = _OaDevConfigAudit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10)
)


class _OaDevConfigAuditAdminStatus_Type(Integer32):
    """Custom type oaDevConfigAuditAdminStatus based on Integer32"""
    defaultValue = 1

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
          ("markCurrentConfigAsValid", 2),
          ("compareWithValidConfig", 3),
          ("scheduleCompare", 4),
          ("cancelScheduledCompare", 5))
    )


_OaDevConfigAuditAdminStatus_Type.__name__ = "Integer32"
_OaDevConfigAuditAdminStatus_Object = MibScalar
oaDevConfigAuditAdminStatus = _OaDevConfigAuditAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 1),
    _OaDevConfigAuditAdminStatus_Type()
)
oaDevConfigAuditAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevConfigAuditAdminStatus.setStatus("current")


class _OaDevConfigAuditOperStatus_Type(Integer32):
    """Custom type oaDevConfigAuditOperStatus based on Integer32"""
    defaultValue = 1

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
          ("actionInProcess", 2),
          ("actionCompletedOk", 3),
          ("actionCompletedWithDiff", 4),
          ("actionCouldNotCompleted", 5))
    )


_OaDevConfigAuditOperStatus_Type.__name__ = "Integer32"
_OaDevConfigAuditOperStatus_Object = MibScalar
oaDevConfigAuditOperStatus = _OaDevConfigAuditOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 2),
    _OaDevConfigAuditOperStatus_Type()
)
oaDevConfigAuditOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevConfigAuditOperStatus.setStatus("current")


class _OaDevConfigAuditErrorStatus_Type(Integer32):
    """Custom type oaDevConfigAuditErrorStatus based on Integer32"""
    defaultValue = 1

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("operationNotPermitted", 2),
          ("operationCanceledByUser", 3),
          ("getCurrentConfigFailure", 4),
          ("compareFailure", 5),
          ("configurationChanged", 6),
          ("noValidConfiguration", 7),
          ("operationInProcess", 8),
          ("anotherSchedulerAlreadyActive", 9),
          ("noActiveScheduler", 10),
          ("addSchedulerError", 11),
          ("deleteSchedulerError", 12))
    )


_OaDevConfigAuditErrorStatus_Type.__name__ = "Integer32"
_OaDevConfigAuditErrorStatus_Object = MibScalar
oaDevConfigAuditErrorStatus = _OaDevConfigAuditErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 3),
    _OaDevConfigAuditErrorStatus_Type()
)
oaDevConfigAuditErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevConfigAuditErrorStatus.setStatus("current")


class _OaDevConfigAuditPeriodicity_Type(Integer32):
    """Custom type oaDevConfigAuditPeriodicity based on Integer32"""
    defaultValue = 1

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("once", 1),
          ("everyMonth", 2),
          ("everyWeek", 3),
          ("everyDay", 4),
          ("every12Hours", 5),
          ("every8Hours", 6),
          ("every6Hours", 7),
          ("every4Hours", 8),
          ("every2Hours", 9),
          ("everyHour", 10),
          ("every30Minutes", 11),
          ("every15Minutes", 12))
    )


_OaDevConfigAuditPeriodicity_Type.__name__ = "Integer32"
_OaDevConfigAuditPeriodicity_Object = MibScalar
oaDevConfigAuditPeriodicity = _OaDevConfigAuditPeriodicity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 4),
    _OaDevConfigAuditPeriodicity_Type()
)
oaDevConfigAuditPeriodicity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevConfigAuditPeriodicity.setStatus("current")
_OaDevConfigAuditStartTime_Type = PeriodicityDateAndTime
_OaDevConfigAuditStartTime_Object = MibScalar
oaDevConfigAuditStartTime = _OaDevConfigAuditStartTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 5),
    _OaDevConfigAuditStartTime_Type()
)
oaDevConfigAuditStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevConfigAuditStartTime.setStatus("current")


class _OaDevConfigAuditSchedulerStatus_Type(Integer32):
    """Custom type oaDevConfigAuditSchedulerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_OaDevConfigAuditSchedulerStatus_Type.__name__ = "Integer32"
_OaDevConfigAuditSchedulerStatus_Object = MibScalar
oaDevConfigAuditSchedulerStatus = _OaDevConfigAuditSchedulerStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 6),
    _OaDevConfigAuditSchedulerStatus_Type()
)
oaDevConfigAuditSchedulerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevConfigAuditSchedulerStatus.setStatus("current")


class _OaDevConfigAuditTrapMode_Type(Integer32):
    """Custom type oaDevConfigAuditTrapMode based on Integer32"""
    defaultValue = 3

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
        *(("noSendConfigAuditTrap", 1),
          ("sendConfAuditTrapOnChangeOnly", 2),
          ("sendConfAuditTrapOnChangeOrDiff", 3),
          ("sendConfAuditTrapForEachCompare", 4))
    )


_OaDevConfigAuditTrapMode_Type.__name__ = "Integer32"
_OaDevConfigAuditTrapMode_Object = MibScalar
oaDevConfigAuditTrapMode = _OaDevConfigAuditTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 7),
    _OaDevConfigAuditTrapMode_Type()
)
oaDevConfigAuditTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevConfigAuditTrapMode.setStatus("current")
_OaAuditTable_Object = MibTable
oaAuditTable = _OaAuditTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10)
)
if mibBuilder.loadTexts:
    oaAuditTable.setStatus("current")
_OaAuditEntry_Object = MibTableRow
oaAuditEntry = _OaAuditEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10, 1)
)
oaAuditEntry.setIndexNames(
    (0, "OA-DEV-UPGRADE-MIB", "oaAuditSubType"),
)
if mibBuilder.loadTexts:
    oaAuditEntry.setStatus("current")


class _OaAuditSubType_Type(Integer32):
    """Custom type oaAuditSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("osEthServTable", 1),
          ("osEthServFlowTable", 2),
          ("osEthServClassTable", 3))
    )


_OaAuditSubType_Type.__name__ = "Integer32"
_OaAuditSubType_Object = MibTableColumn
oaAuditSubType = _OaAuditSubType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10, 1, 1),
    _OaAuditSubType_Type()
)
oaAuditSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaAuditSubType.setStatus("current")


class _OaAuditAdminStatus_Type(Integer32):
    """Custom type oaAuditAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("computeNow", 2),
          ("computeValid", 3))
    )


_OaAuditAdminStatus_Type.__name__ = "Integer32"
_OaAuditAdminStatus_Object = MibTableColumn
oaAuditAdminStatus = _OaAuditAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10, 1, 2),
    _OaAuditAdminStatus_Type()
)
oaAuditAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaAuditAdminStatus.setStatus("current")


class _OaAuditOperStatus_Type(Integer32):
    """Custom type oaAuditOperStatus based on Integer32"""
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
        *(("none", 1),
          ("computeInProcess", 2),
          ("computeFinishedOK", 3),
          ("computeError", 4))
    )


_OaAuditOperStatus_Type.__name__ = "Integer32"
_OaAuditOperStatus_Object = MibTableColumn
oaAuditOperStatus = _OaAuditOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10, 1, 4),
    _OaAuditOperStatus_Type()
)
oaAuditOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaAuditOperStatus.setStatus("current")
_OaAuditChecksum_Type = Unsigned32
_OaAuditChecksum_Object = MibTableColumn
oaAuditChecksum = _OaAuditChecksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10, 1, 5),
    _OaAuditChecksum_Type()
)
oaAuditChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaAuditChecksum.setStatus("current")
_OaAuditChecksumTime_Type = DateAndTime
_OaAuditChecksumTime_Object = MibTableColumn
oaAuditChecksumTime = _OaAuditChecksumTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10, 1, 6),
    _OaAuditChecksumTime_Type()
)
oaAuditChecksumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaAuditChecksumTime.setStatus("current")
_OaAuditValidChecksum_Type = Unsigned32
_OaAuditValidChecksum_Object = MibTableColumn
oaAuditValidChecksum = _OaAuditValidChecksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10, 1, 7),
    _OaAuditValidChecksum_Type()
)
oaAuditValidChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaAuditValidChecksum.setStatus("current")
_OaAuditValidChecksumTime_Type = DateAndTime
_OaAuditValidChecksumTime_Object = MibTableColumn
oaAuditValidChecksumTime = _OaAuditValidChecksumTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10, 1, 8),
    _OaAuditValidChecksumTime_Type()
)
oaAuditValidChecksumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaAuditValidChecksumTime.setStatus("current")


class _OaAuditLastError_Type(DisplayString):
    """Custom type oaAuditLastError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 160),
    )


_OaAuditLastError_Type.__name__ = "DisplayString"
_OaAuditLastError_Object = MibTableColumn
oaAuditLastError = _OaAuditLastError_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 10, 1, 100),
    _OaAuditLastError_Type()
)
oaAuditLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaAuditLastError.setStatus("current")
_OaAuditScheduleParams_ObjectIdentity = ObjectIdentity
oaAuditScheduleParams = _OaAuditScheduleParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 11)
)
_OaAuditScheduleStart_Type = PeriodicityDateAndTime
_OaAuditScheduleStart_Object = MibScalar
oaAuditScheduleStart = _OaAuditScheduleStart_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 11, 1),
    _OaAuditScheduleStart_Type()
)
oaAuditScheduleStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaAuditScheduleStart.setStatus("current")


class _OaAuditSchedulePeriod_Type(Integer32):
    """Custom type oaAuditSchedulePeriod based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44640),
    )


_OaAuditSchedulePeriod_Type.__name__ = "Integer32"
_OaAuditSchedulePeriod_Object = MibScalar
oaAuditSchedulePeriod = _OaAuditSchedulePeriod_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 11, 2),
    _OaAuditSchedulePeriod_Type()
)
oaAuditSchedulePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaAuditSchedulePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oaAuditSchedulePeriod.setUnits("minutes")


class _OaAuditScheduleStatus_Type(Integer32):
    """Custom type oaAuditScheduleStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_OaAuditScheduleStatus_Type.__name__ = "Integer32"
_OaAuditScheduleStatus_Object = MibScalar
oaAuditScheduleStatus = _OaAuditScheduleStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 11, 3),
    _OaAuditScheduleStatus_Type()
)
oaAuditScheduleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaAuditScheduleStatus.setStatus("current")


class _OaAuditScheduleError_Type(DisplayString):
    """Custom type oaAuditScheduleError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 160),
    )


_OaAuditScheduleError_Type.__name__ = "DisplayString"
_OaAuditScheduleError_Object = MibScalar
oaAuditScheduleError = _OaAuditScheduleError_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 11, 4),
    _OaAuditScheduleError_Type()
)
oaAuditScheduleError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaAuditScheduleError.setStatus("current")


class _OaAuditMinSchedulePeriod_Type(Integer32):
    """Custom type oaAuditMinSchedulePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44640),
    )


_OaAuditMinSchedulePeriod_Type.__name__ = "Integer32"
_OaAuditMinSchedulePeriod_Object = MibScalar
oaAuditMinSchedulePeriod = _OaAuditMinSchedulePeriod_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 10, 11, 5),
    _OaAuditMinSchedulePeriod_Type()
)
oaAuditMinSchedulePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaAuditMinSchedulePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oaAuditMinSchedulePeriod.setUnits("minutes")
_OaDevUpgrConformance_ObjectIdentity = ObjectIdentity
oaDevUpgrConformance = _OaDevUpgrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 101)
)
_OaDevUpgrMIBCompliances_ObjectIdentity = ObjectIdentity
oaDevUpgrMIBCompliances = _OaDevUpgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 101, 1)
)
_OaDevUpgrMIBGroups_ObjectIdentity = ObjectIdentity
oaDevUpgrMIBGroups = _OaDevUpgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 101, 2)
)

# Managed Objects groups

oaDevUpgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 101, 2, 1)
)
oaDevUpgrGroup.setObjects(
      *(("OA-DEV-UPGRADE-MIB", "oaDevUpgrGenSupport"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrType"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrProtocolApp"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrServerAddressType"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrServerAddress"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrRemoteDir"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrRemoteFileName"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrPeriodicity"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrPeriodDateTime"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrResetDevice"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrOperStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrAdminStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrUsername"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrPassword"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrServerAddressText"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrErrorStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrResetDelay"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditAdminStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditOperStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditErrorStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditPeriodicity"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditStartTime"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditSchedulerStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditTrapMode"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditAdminStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditOperStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditChecksum"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditChecksumTime"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditValidChecksum"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditValidChecksumTime"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditLastError"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditScheduleStart"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditSchedulePeriod"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditScheduleStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditScheduleError"),
        ("OA-DEV-UPGRADE-MIB", "oaAuditMinSchedulePeriod"))
)
if mibBuilder.loadTexts:
    oaDevUpgrGroup.setStatus("current")


# Notification objects

oaDevConfigAuditCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 0, 94)
)
oaDevConfigAuditCompleted.setObjects(
      *(("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditAdminStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditOperStatus"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditErrorStatus"))
)
if mibBuilder.loadTexts:
    oaDevConfigAuditCompleted.setStatus(
        "current"
    )

oaDevUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 0, 101)
)
oaDevUpgradeStarted.setObjects(
      *(("OA-DEV-UPGRADE-MIB", "oaDevUpgrType"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrProtocolApp"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrServerAddressText"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrRemoteDir"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrRemoteFileName"))
)
if mibBuilder.loadTexts:
    oaDevUpgradeStarted.setStatus(
        "current"
    )

oaDevUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 0, 102)
)
oaDevUpgradeFailed.setObjects(
      *(("OA-DEV-UPGRADE-MIB", "oaDevUpgrType"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrProtocolApp"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrServerAddressText"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrRemoteDir"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrRemoteFileName"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrErrorStatus"))
)
if mibBuilder.loadTexts:
    oaDevUpgradeFailed.setStatus(
        "current"
    )

oaDevUpgradeCompletedOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 0, 103)
)
oaDevUpgradeCompletedOk.setObjects(
      *(("OA-DEV-UPGRADE-MIB", "oaDevUpgrType"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrProtocolApp"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrServerAddressText"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrRemoteDir"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrRemoteFileName"))
)
if mibBuilder.loadTexts:
    oaDevUpgradeCompletedOk.setStatus(
        "current"
    )


# Notifications groups

oaDevUpgrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 101, 2, 2)
)
oaDevUpgrNotificationsGroup.setObjects(
      *(("OA-DEV-UPGRADE-MIB", "oaDevUpgradeStarted"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgradeFailed"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgradeCompletedOk"),
        ("OA-DEV-UPGRADE-MIB", "oaDevConfigAuditCompleted"))
)
if mibBuilder.loadTexts:
    oaDevUpgrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

oaDevUpgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 20, 101, 1, 1)
)
oaDevUpgrMIBCompliance.setObjects(
      *(("OA-DEV-UPGRADE-MIB", "oaDevUpgrGroup"),
        ("OA-DEV-UPGRADE-MIB", "oaDevUpgrNotificationsGroup"))
)
if mibBuilder.loadTexts:
    oaDevUpgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-DEV-UPGRADE-MIB",
    **{"PeriodicityDateAndTime": PeriodicityDateAndTime,
       "nbDeviceConfig": nbDeviceConfig,
       "nbDevGen": nbDevGen,
       "oaDevUpgrade": oaDevUpgrade,
       "oaDevUpgrNotifications": oaDevUpgrNotifications,
       "oaDevConfigAuditCompleted": oaDevConfigAuditCompleted,
       "oaDevUpgradeStarted": oaDevUpgradeStarted,
       "oaDevUpgradeFailed": oaDevUpgradeFailed,
       "oaDevUpgradeCompletedOk": oaDevUpgradeCompletedOk,
       "oaDevUpgrGenSupport": oaDevUpgrGenSupport,
       "oaDevUpgrTable": oaDevUpgrTable,
       "oaDevUpgrEntry": oaDevUpgrEntry,
       "oaDevUpgrType": oaDevUpgrType,
       "oaDevUpgrProtocolApp": oaDevUpgrProtocolApp,
       "oaDevUpgrServerAddressType": oaDevUpgrServerAddressType,
       "oaDevUpgrServerAddress": oaDevUpgrServerAddress,
       "oaDevUpgrRemoteDir": oaDevUpgrRemoteDir,
       "oaDevUpgrRemoteFileName": oaDevUpgrRemoteFileName,
       "oaDevUpgrPeriodicity": oaDevUpgrPeriodicity,
       "oaDevUpgrPeriodDateTime": oaDevUpgrPeriodDateTime,
       "oaDevUpgrResetDevice": oaDevUpgrResetDevice,
       "oaDevUpgrOperStatus": oaDevUpgrOperStatus,
       "oaDevUpgrAdminStatus": oaDevUpgrAdminStatus,
       "oaDevUpgrUsername": oaDevUpgrUsername,
       "oaDevUpgrPassword": oaDevUpgrPassword,
       "oaDevUpgrServerAddressText": oaDevUpgrServerAddressText,
       "oaDevUpgrErrorStatus": oaDevUpgrErrorStatus,
       "oaDevUpgrResetDelay": oaDevUpgrResetDelay,
       "oaDevConfigAudit": oaDevConfigAudit,
       "oaDevConfigAuditAdminStatus": oaDevConfigAuditAdminStatus,
       "oaDevConfigAuditOperStatus": oaDevConfigAuditOperStatus,
       "oaDevConfigAuditErrorStatus": oaDevConfigAuditErrorStatus,
       "oaDevConfigAuditPeriodicity": oaDevConfigAuditPeriodicity,
       "oaDevConfigAuditStartTime": oaDevConfigAuditStartTime,
       "oaDevConfigAuditSchedulerStatus": oaDevConfigAuditSchedulerStatus,
       "oaDevConfigAuditTrapMode": oaDevConfigAuditTrapMode,
       "oaAuditTable": oaAuditTable,
       "oaAuditEntry": oaAuditEntry,
       "oaAuditSubType": oaAuditSubType,
       "oaAuditAdminStatus": oaAuditAdminStatus,
       "oaAuditOperStatus": oaAuditOperStatus,
       "oaAuditChecksum": oaAuditChecksum,
       "oaAuditChecksumTime": oaAuditChecksumTime,
       "oaAuditValidChecksum": oaAuditValidChecksum,
       "oaAuditValidChecksumTime": oaAuditValidChecksumTime,
       "oaAuditLastError": oaAuditLastError,
       "oaAuditScheduleParams": oaAuditScheduleParams,
       "oaAuditScheduleStart": oaAuditScheduleStart,
       "oaAuditSchedulePeriod": oaAuditSchedulePeriod,
       "oaAuditScheduleStatus": oaAuditScheduleStatus,
       "oaAuditScheduleError": oaAuditScheduleError,
       "oaAuditMinSchedulePeriod": oaAuditMinSchedulePeriod,
       "oaDevUpgrConformance": oaDevUpgrConformance,
       "oaDevUpgrMIBCompliances": oaDevUpgrMIBCompliances,
       "oaDevUpgrMIBCompliance": oaDevUpgrMIBCompliance,
       "oaDevUpgrMIBGroups": oaDevUpgrMIBGroups,
       "oaDevUpgrGroup": oaDevUpgrGroup,
       "oaDevUpgrNotificationsGroup": oaDevUpgrNotificationsGroup}
)
