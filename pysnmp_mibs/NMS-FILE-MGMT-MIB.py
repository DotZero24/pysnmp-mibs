# SNMP MIB module (NMS-FILE-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bdcom/NMS-FILE-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:56 2025
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

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

nmsFileMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FileTransferManagement_ObjectIdentity = ObjectIdentity
fileTransferManagement = _FileTransferManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1)
)
if mibBuilder.loadTexts:
    fileTransferManagement.setStatus("current")
_FileTransferTable_Object = MibTable
fileTransferTable = _FileTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1)
)
if mibBuilder.loadTexts:
    fileTransferTable.setStatus("current")
_FileTransferEntry_Object = MibTableRow
fileTransferEntry = _FileTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1)
)
fileTransferEntry.setIndexNames(
    (0, "NMS-FILE-MGMT-MIB", "fileTransferIndex"),
)
if mibBuilder.loadTexts:
    fileTransferEntry.setStatus("current")


class _FileTransferIndex_Type(Integer32):
    """Custom type fileTransferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FileTransferIndex_Type.__name__ = "Integer32"
_FileTransferIndex_Object = MibTableColumn
fileTransferIndex = _FileTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1, 1),
    _FileTransferIndex_Type()
)
fileTransferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileTransferIndex.setStatus("current")


class _FileTransferProtocolType_Type(Integer32):
    """Custom type fileTransferProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("tftp", 2))
    )


_FileTransferProtocolType_Type.__name__ = "Integer32"
_FileTransferProtocolType_Object = MibTableColumn
fileTransferProtocolType = _FileTransferProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1, 2),
    _FileTransferProtocolType_Type()
)
fileTransferProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferProtocolType.setStatus("current")
_ServerIpAddress_Type = IpAddress
_ServerIpAddress_Object = MibTableColumn
serverIpAddress = _ServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1, 3),
    _ServerIpAddress_Type()
)
serverIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverIpAddress.setStatus("current")
_FtpUserName_Type = DisplayString
_FtpUserName_Object = MibTableColumn
ftpUserName = _FtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1, 4),
    _FtpUserName_Type()
)
ftpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUserName.setStatus("current")
_FtpUserPassword_Type = DisplayString
_FtpUserPassword_Object = MibTableColumn
ftpUserPassword = _FtpUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1, 5),
    _FtpUserPassword_Type()
)
ftpUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUserPassword.setStatus("current")
_TransferFileSrcNamePath_Type = DisplayString
_TransferFileSrcNamePath_Object = MibTableColumn
transferFileSrcNamePath = _TransferFileSrcNamePath_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1, 6),
    _TransferFileSrcNamePath_Type()
)
transferFileSrcNamePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferFileSrcNamePath.setStatus("current")
_TransferFileDstNamePath_Type = DisplayString
_TransferFileDstNamePath_Object = MibTableColumn
transferFileDstNamePath = _TransferFileDstNamePath_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1, 7),
    _TransferFileDstNamePath_Type()
)
transferFileDstNamePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferFileDstNamePath.setStatus("current")


class _TransferAction_Type(Integer32):
    """Custom type transferAction based on Integer32"""
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
        *(("noOperation", 1),
          ("put", 2),
          ("get", 3),
          ("halt", 4))
    )


_TransferAction_Type.__name__ = "Integer32"
_TransferAction_Object = MibTableColumn
transferAction = _TransferAction_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1, 8),
    _TransferAction_Type()
)
transferAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferAction.setStatus("current")


class _TransferStatus_Type(Integer32):
    """Custom type transferStatus based on Integer32"""
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
          ("inProgress", 2),
          ("success", 3),
          ("failure", 4))
    )


_TransferStatus_Type.__name__ = "Integer32"
_TransferStatus_Object = MibTableColumn
transferStatus = _TransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 1, 1, 9),
    _TransferStatus_Type()
)
transferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferStatus.setStatus("current")
_FileInfoManagementTable_Object = MibTable
fileInfoManagementTable = _FileInfoManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 2)
)
if mibBuilder.loadTexts:
    fileInfoManagementTable.setStatus("current")
_FileInfoManagementEntry_Object = MibTableRow
fileInfoManagementEntry = _FileInfoManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 2, 1)
)
fileInfoManagementEntry.setIndexNames(
    (0, "NMS-FILE-MGMT-MIB", "filePath"),
    (0, "NMS-FILE-MGMT-MIB", "fileName"),
)
if mibBuilder.loadTexts:
    fileInfoManagementEntry.setStatus("current")
_FilePath_Type = DisplayString
_FilePath_Object = MibTableColumn
filePath = _FilePath_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 2, 1, 1),
    _FilePath_Type()
)
filePath.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filePath.setStatus("current")
_FileName_Type = DisplayString
_FileName_Object = MibTableColumn
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 2, 1, 2),
    _FileName_Type()
)
fileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileName.setStatus("current")
_FileSize_Type = Counter32
_FileSize_Object = MibTableColumn
fileSize = _FileSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 2, 1, 3),
    _FileSize_Type()
)
fileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSize.setStatus("current")
if mibBuilder.loadTexts:
    fileSize.setUnits("bytes")
_FileModifyTime_Type = DateAndTime
_FileModifyTime_Object = MibTableColumn
fileModifyTime = _FileModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 2, 1, 4),
    _FileModifyTime_Type()
)
fileModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileModifyTime.setStatus("current")


class _FileManagementAction_Type(Integer32):
    """Custom type fileManagementAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("erase", 2))
    )


_FileManagementAction_Type.__name__ = "Integer32"
_FileManagementAction_Object = MibTableColumn
fileManagementAction = _FileManagementAction_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 2, 1, 5),
    _FileManagementAction_Type()
)
fileManagementAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileManagementAction.setStatus("current")


class _FileAttribute_Type(Integer32):
    """Custom type fileAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("dir", 2))
    )


_FileAttribute_Type.__name__ = "Integer32"
_FileAttribute_Object = MibTableColumn
fileAttribute = _FileAttribute_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 185, 1, 2, 1, 6),
    _FileAttribute_Type()
)
fileAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAttribute.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-FILE-MGMT-MIB",
    **{"nmsFileMgmtMIB": nmsFileMgmtMIB,
       "fileTransferManagement": fileTransferManagement,
       "fileTransferTable": fileTransferTable,
       "fileTransferEntry": fileTransferEntry,
       "fileTransferIndex": fileTransferIndex,
       "fileTransferProtocolType": fileTransferProtocolType,
       "serverIpAddress": serverIpAddress,
       "ftpUserName": ftpUserName,
       "ftpUserPassword": ftpUserPassword,
       "transferFileSrcNamePath": transferFileSrcNamePath,
       "transferFileDstNamePath": transferFileDstNamePath,
       "transferAction": transferAction,
       "transferStatus": transferStatus,
       "fileInfoManagementTable": fileInfoManagementTable,
       "fileInfoManagementEntry": fileInfoManagementEntry,
       "filePath": filePath,
       "fileName": fileName,
       "fileSize": fileSize,
       "fileModifyTime": fileModifyTime,
       "fileManagementAction": fileManagementAction,
       "fileAttribute": fileAttribute}
)
