# SNMP MIB module (RAD-CopyFile-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-CopyFile-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:25 2025
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(fileTransfer,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "fileTransfer")

(FileType,) = mibBuilder.importSymbols(
    "RAD-TC",
    "FileType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

copyFileGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CopyFileNotifications_ObjectIdentity = ObjectIdentity
copyFileNotifications = _CopyFileNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 0)
)
if mibBuilder.loadTexts:
    copyFileNotifications.setStatus("current")
_CopyFileTable_Object = MibTable
copyFileTable = _CopyFileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1)
)
if mibBuilder.loadTexts:
    copyFileTable.setStatus("current")
_CopyFileEntry_Object = MibTableRow
copyFileEntry = _CopyFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1)
)
copyFileEntry.setIndexNames(
    (0, "RAD-CopyFile-MIB", "copyFileIdx"),
)
if mibBuilder.loadTexts:
    copyFileEntry.setStatus("current")
_CopyFileIdx_Type = Integer32
_CopyFileIdx_Object = MibTableColumn
copyFileIdx = _CopyFileIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 1),
    _CopyFileIdx_Type()
)
copyFileIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copyFileIdx.setStatus("current")
_CopyFileRowStatus_Type = RowStatus
_CopyFileRowStatus_Object = MibTableColumn
copyFileRowStatus = _CopyFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 2),
    _CopyFileRowStatus_Type()
)
copyFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileRowStatus.setStatus("current")


class _CopyFileProtocol_Type(Integer32):
    """Custom type copyFileProtocol based on Integer32"""
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
        *(("undefined", 1),
          ("tftp", 2),
          ("sftp", 3),
          ("xmodem", 4),
          ("localFile", 5))
    )


_CopyFileProtocol_Type.__name__ = "Integer32"
_CopyFileProtocol_Object = MibTableColumn
copyFileProtocol = _CopyFileProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 3),
    _CopyFileProtocol_Type()
)
copyFileProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileProtocol.setStatus("current")
_CopyFileAddressType_Type = InetAddressType
_CopyFileAddressType_Object = MibTableColumn
copyFileAddressType = _CopyFileAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 4),
    _CopyFileAddressType_Type()
)
copyFileAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileAddressType.setStatus("current")
_CopyFileAddress_Type = InetAddress
_CopyFileAddress_Object = MibTableColumn
copyFileAddress = _CopyFileAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 5),
    _CopyFileAddress_Type()
)
copyFileAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileAddress.setStatus("current")
_CopyFilePort_Type = InetPortNumber
_CopyFilePort_Object = MibTableColumn
copyFilePort = _CopyFilePort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 6),
    _CopyFilePort_Type()
)
copyFilePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFilePort.setStatus("current")
_CopyFileUserName_Type = SnmpAdminString
_CopyFileUserName_Object = MibTableColumn
copyFileUserName = _CopyFileUserName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 7),
    _CopyFileUserName_Type()
)
copyFileUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileUserName.setStatus("current")
_CopyFilePassword_Type = SnmpAdminString
_CopyFilePassword_Object = MibTableColumn
copyFilePassword = _CopyFilePassword_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 8),
    _CopyFilePassword_Type()
)
copyFilePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFilePassword.setStatus("current")
_CopyFileSrcType_Type = FileType
_CopyFileSrcType_Object = MibTableColumn
copyFileSrcType = _CopyFileSrcType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 9),
    _CopyFileSrcType_Type()
)
copyFileSrcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileSrcType.setStatus("current")
_CopyFileSrcFilePath_Type = SnmpAdminString
_CopyFileSrcFilePath_Object = MibTableColumn
copyFileSrcFilePath = _CopyFileSrcFilePath_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 10),
    _CopyFileSrcFilePath_Type()
)
copyFileSrcFilePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileSrcFilePath.setStatus("current")
_CopyFileSrcFileName_Type = SnmpAdminString
_CopyFileSrcFileName_Object = MibTableColumn
copyFileSrcFileName = _CopyFileSrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 11),
    _CopyFileSrcFileName_Type()
)
copyFileSrcFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileSrcFileName.setStatus("current")
_CopyFileDstType_Type = FileType
_CopyFileDstType_Object = MibTableColumn
copyFileDstType = _CopyFileDstType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 12),
    _CopyFileDstType_Type()
)
copyFileDstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileDstType.setStatus("current")
_CopyFileDstFilePath_Type = SnmpAdminString
_CopyFileDstFilePath_Object = MibTableColumn
copyFileDstFilePath = _CopyFileDstFilePath_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 13),
    _CopyFileDstFilePath_Type()
)
copyFileDstFilePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileDstFilePath.setStatus("current")
_CopyFileDstFileName_Type = SnmpAdminString
_CopyFileDstFileName_Object = MibTableColumn
copyFileDstFileName = _CopyFileDstFileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 14),
    _CopyFileDstFileName_Type()
)
copyFileDstFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileDstFileName.setStatus("current")


class _CopyFileStatus_Type(Integer32):
    """Custom type copyFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 2),
          ("authenticating", 3),
          ("connecting", 4),
          ("transferringData", 5),
          ("endedOk", 6),
          ("error", 7),
          ("errorOveridden", 8))
    )


_CopyFileStatus_Type.__name__ = "Integer32"
_CopyFileStatus_Object = MibTableColumn
copyFileStatus = _CopyFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 15),
    _CopyFileStatus_Type()
)
copyFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyFileStatus.setStatus("current")


class _CopyFileError_Type(Integer32):
    """Custom type copyFileError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              14,
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("serverNotResponding", 2),
          ("fileNotFound", 3),
          ("accessViolationDst", 4),
          ("invalidSrcFile", 5),
          ("invalidRollbackSrc", 6),
          ("connectionFail", 8),
          ("lackOfSpace", 9),
          ("lackOfInternalResources", 10),
          ("endedTimeout", 11),
          ("accessViolationSrc", 14),
          ("transferToStandbyFailed", 15),
          ("otherError", 255))
    )


_CopyFileError_Type.__name__ = "Integer32"
_CopyFileError_Object = MibTableColumn
copyFileError = _CopyFileError_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 16),
    _CopyFileError_Type()
)
copyFileError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyFileError.setStatus("current")
_CopyFileStartTime_Type = DateAndTime
_CopyFileStartTime_Object = MibTableColumn
copyFileStartTime = _CopyFileStartTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 17),
    _CopyFileStartTime_Type()
)
copyFileStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyFileStartTime.setStatus("current")
_CopyFileEndTime_Type = DateAndTime
_CopyFileEndTime_Object = MibTableColumn
copyFileEndTime = _CopyFileEndTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 18),
    _CopyFileEndTime_Type()
)
copyFileEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyFileEndTime.setStatus("current")
_CopyFileProgressBytes_Type = Unsigned32
_CopyFileProgressBytes_Object = MibTableColumn
copyFileProgressBytes = _CopyFileProgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 19),
    _CopyFileProgressBytes_Type()
)
copyFileProgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyFileProgressBytes.setStatus("current")


class _CopyFileDirection_Type(Integer32):
    """Custom type copyFileDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkToDevice", 1),
          ("deviceToNetwork", 2),
          ("deviceLocally", 3))
    )


_CopyFileDirection_Type.__name__ = "Integer32"
_CopyFileDirection_Object = MibTableColumn
copyFileDirection = _CopyFileDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 1, 1, 20),
    _CopyFileDirection_Type()
)
copyFileDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyFileDirection.setStatus("current")

# Managed Objects groups


# Notification objects

systemDownloadEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 18, 0, 2)
)
systemDownloadEnd.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-CopyFile-MIB", "copyFileSrcType"),
        ("RAD-CopyFile-MIB", "copyFileSrcFilePath"),
        ("RAD-CopyFile-MIB", "copyFileSrcFileName"),
        ("RAD-CopyFile-MIB", "copyFileDstType"),
        ("RAD-CopyFile-MIB", "copyFileDstFilePath"),
        ("RAD-CopyFile-MIB", "copyFileDstFileName"),
        ("RAD-CopyFile-MIB", "copyFileAddress"),
        ("RAD-CopyFile-MIB", "copyFilePort"),
        ("RAD-CopyFile-MIB", "copyFileError"))
)
if mibBuilder.loadTexts:
    systemDownloadEnd.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-CopyFile-MIB",
    **{"copyFileGroup": copyFileGroup,
       "copyFileNotifications": copyFileNotifications,
       "systemDownloadEnd": systemDownloadEnd,
       "copyFileTable": copyFileTable,
       "copyFileEntry": copyFileEntry,
       "copyFileIdx": copyFileIdx,
       "copyFileRowStatus": copyFileRowStatus,
       "copyFileProtocol": copyFileProtocol,
       "copyFileAddressType": copyFileAddressType,
       "copyFileAddress": copyFileAddress,
       "copyFilePort": copyFilePort,
       "copyFileUserName": copyFileUserName,
       "copyFilePassword": copyFilePassword,
       "copyFileSrcType": copyFileSrcType,
       "copyFileSrcFilePath": copyFileSrcFilePath,
       "copyFileSrcFileName": copyFileSrcFileName,
       "copyFileDstType": copyFileDstType,
       "copyFileDstFilePath": copyFileDstFilePath,
       "copyFileDstFileName": copyFileDstFileName,
       "copyFileStatus": copyFileStatus,
       "copyFileError": copyFileError,
       "copyFileStartTime": copyFileStartTime,
       "copyFileEndTime": copyFileEndTime,
       "copyFileProgressBytes": copyFileProgressBytes,
       "copyFileDirection": copyFileDirection}
)
