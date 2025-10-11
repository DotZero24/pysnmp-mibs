# SNMP MIB module (FS-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-FILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:21 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsFileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11)
)
if mibBuilder.loadTexts:
    fsFileMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsFileMIBTraps_ObjectIdentity = ObjectIdentity
fsFileMIBTraps = _FsFileMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 0)
)
_FsFileMIBObjects_ObjectIdentity = ObjectIdentity
fsFileMIBObjects = _FsFileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1)
)
_FsFileTransTable_Object = MibTable
fsFileTransTable = _FsFileTransTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    fsFileTransTable.setStatus("current")
_FsFileTransEntry_Object = MibTableRow
fsFileTransEntry = _FsFileTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1)
)
fsFileTransEntry.setIndexNames(
    (0, "FS-FILE-MIB", "fsFileTransIndex"),
)
if mibBuilder.loadTexts:
    fsFileTransEntry.setStatus("current")
_FsFileTransIndex_Type = Integer32
_FsFileTransIndex_Object = MibTableColumn
fsFileTransIndex = _FsFileTransIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 1),
    _FsFileTransIndex_Type()
)
fsFileTransIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileTransIndex.setStatus("current")


class _FsFileTransMeans_Type(Integer32):
    """Custom type fsFileTransMeans based on Integer32"""
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
        *(("tftp", 1),
          ("xmodem", 2),
          ("other", 3))
    )


_FsFileTransMeans_Type.__name__ = "Integer32"
_FsFileTransMeans_Object = MibTableColumn
fsFileTransMeans = _FsFileTransMeans_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 2),
    _FsFileTransMeans_Type()
)
fsFileTransMeans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsFileTransMeans.setStatus("current")


class _FsFileTransOperType_Type(Integer32):
    """Custom type fsFileTransOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upload", 1),
          ("download", 2),
          ("synchronize", 3))
    )


_FsFileTransOperType_Type.__name__ = "Integer32"
_FsFileTransOperType_Object = MibTableColumn
fsFileTransOperType = _FsFileTransOperType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 3),
    _FsFileTransOperType_Type()
)
fsFileTransOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsFileTransOperType.setStatus("current")
_FsFileTransSrcFileName_Type = DisplayString
_FsFileTransSrcFileName_Object = MibTableColumn
fsFileTransSrcFileName = _FsFileTransSrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 4),
    _FsFileTransSrcFileName_Type()
)
fsFileTransSrcFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsFileTransSrcFileName.setStatus("current")
_FsFileTransDescFileName_Type = DisplayString
_FsFileTransDescFileName_Object = MibTableColumn
fsFileTransDescFileName = _FsFileTransDescFileName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 5),
    _FsFileTransDescFileName_Type()
)
fsFileTransDescFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsFileTransDescFileName.setStatus("current")
_FsFileTransServerAddr_Type = IpAddress
_FsFileTransServerAddr_Object = MibTableColumn
fsFileTransServerAddr = _FsFileTransServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 6),
    _FsFileTransServerAddr_Type()
)
fsFileTransServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsFileTransServerAddr.setStatus("current")


class _FsFileTransResult_Type(Integer32):
    """Custom type fsFileTransResult based on Integer32"""
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
        *(("success", 1),
          ("failure", 2),
          ("parametersIllegel", 3),
          ("timeout", 4))
    )


_FsFileTransResult_Type.__name__ = "Integer32"
_FsFileTransResult_Object = MibTableColumn
fsFileTransResult = _FsFileTransResult_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 7),
    _FsFileTransResult_Type()
)
fsFileTransResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileTransResult.setStatus("current")
_FsFileTransComplete_Type = TruthValue
_FsFileTransComplete_Object = MibTableColumn
fsFileTransComplete = _FsFileTransComplete_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 8),
    _FsFileTransComplete_Type()
)
fsFileTransComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileTransComplete.setStatus("current")
_FsFileTransDataLength_Type = Gauge32
_FsFileTransDataLength_Object = MibTableColumn
fsFileTransDataLength = _FsFileTransDataLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 9),
    _FsFileTransDataLength_Type()
)
fsFileTransDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileTransDataLength.setStatus("current")
_FsFileTransEntryStatus_Type = RowStatus
_FsFileTransEntryStatus_Object = MibTableColumn
fsFileTransEntryStatus = _FsFileTransEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 10),
    _FsFileTransEntryStatus_Type()
)
fsFileTransEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsFileTransEntryStatus.setStatus("current")


class _FsFileTransServerAddr6_Type(OctetString):
    """Custom type fsFileTransServerAddr6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsFileTransServerAddr6_Type.__name__ = "OctetString"
_FsFileTransServerAddr6_Object = MibTableColumn
fsFileTransServerAddr6 = _FsFileTransServerAddr6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 11),
    _FsFileTransServerAddr6_Type()
)
fsFileTransServerAddr6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsFileTransServerAddr6.setStatus("current")
_FsFileTransUserName_Type = DisplayString
_FsFileTransUserName_Object = MibTableColumn
fsFileTransUserName = _FsFileTransUserName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 12),
    _FsFileTransUserName_Type()
)
fsFileTransUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsFileTransUserName.setStatus("current")
_FsFileTransPassWord_Type = DisplayString
_FsFileTransPassWord_Object = MibTableColumn
fsFileTransPassWord = _FsFileTransPassWord_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 13),
    _FsFileTransPassWord_Type()
)
fsFileTransPassWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsFileTransPassWord.setStatus("current")
_FsFileTransFailedReason_Type = DisplayString
_FsFileTransFailedReason_Object = MibTableColumn
fsFileTransFailedReason = _FsFileTransFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 14),
    _FsFileTransFailedReason_Type()
)
fsFileTransFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileTransFailedReason.setStatus("current")


class _FsFileTransFileType_Type(Integer32):
    """Custom type fsFileTransFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("software-version-file", 1),
          ("config-file", 2),
          ("log-file", 3))
    )


_FsFileTransFileType_Type.__name__ = "Integer32"
_FsFileTransFileType_Object = MibTableColumn
fsFileTransFileType = _FsFileTransFileType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 15),
    _FsFileTransFileType_Type()
)
fsFileTransFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFileTransFileType.setStatus("current")
_FsFileTransServerPort_Type = Integer32
_FsFileTransServerPort_Object = MibTableColumn
fsFileTransServerPort = _FsFileTransServerPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 16),
    _FsFileTransServerPort_Type()
)
fsFileTransServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFileTransServerPort.setStatus("current")


class _FsFileTransPortType_Type(Integer32):
    """Custom type fsFileTransPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byInterfacePort", 1),
          ("byMgmtPort", 2))
    )


_FsFileTransPortType_Type.__name__ = "Integer32"
_FsFileTransPortType_Object = MibTableColumn
fsFileTransPortType = _FsFileTransPortType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 1, 1, 17),
    _FsFileTransPortType_Type()
)
fsFileTransPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFileTransPortType.setStatus("current")
_FsFileSystemMaxRoom_Type = Integer32
_FsFileSystemMaxRoom_Object = MibScalar
fsFileSystemMaxRoom = _FsFileSystemMaxRoom_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 2),
    _FsFileSystemMaxRoom_Type()
)
fsFileSystemMaxRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileSystemMaxRoom.setStatus("current")
_FsFileSystemAvailableRoom_Type = Integer32
_FsFileSystemAvailableRoom_Object = MibScalar
fsFileSystemAvailableRoom = _FsFileSystemAvailableRoom_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 1, 3),
    _FsFileSystemAvailableRoom_Type()
)
fsFileSystemAvailableRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFileSystemAvailableRoom.setStatus("current")
_FsFileMIBConformance_ObjectIdentity = ObjectIdentity
fsFileMIBConformance = _FsFileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 2)
)
_FsFileMIBCompliances_ObjectIdentity = ObjectIdentity
fsFileMIBCompliances = _FsFileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 2, 1)
)
_FsFileMIBGroups_ObjectIdentity = ObjectIdentity
fsFileMIBGroups = _FsFileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 2, 2)
)

# Managed Objects groups

fsFileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 2, 2, 1)
)
fsFileMIBGroup.setObjects(
      *(("FS-FILE-MIB", "fsFileTransIndex"),
        ("FS-FILE-MIB", "fsFileTransOperType"),
        ("FS-FILE-MIB", "fsFileTransSrcFileName"),
        ("FS-FILE-MIB", "fsFileTransDescFileName"),
        ("FS-FILE-MIB", "fsFileTransServerAddr"),
        ("FS-FILE-MIB", "fsFileTransResult"),
        ("FS-FILE-MIB", "fsFileTransComplete"),
        ("FS-FILE-MIB", "fsFileTransDataLength"),
        ("FS-FILE-MIB", "fsFileTransEntryStatus"),
        ("FS-FILE-MIB", "fsFileTransServerAddr6"),
        ("FS-FILE-MIB", "fsFileTransUserName"),
        ("FS-FILE-MIB", "fsFileTransPassWord"),
        ("FS-FILE-MIB", "fsFileTransFailedReason"),
        ("FS-FILE-MIB", "fsFileTransFileType"),
        ("FS-FILE-MIB", "fsFileTransServerPort"),
        ("FS-FILE-MIB", "fsFileTransPortType"),
        ("FS-FILE-MIB", "fsFileSystemMaxRoom"),
        ("FS-FILE-MIB", "fsFileSystemAvailableRoom"))
)
if mibBuilder.loadTexts:
    fsFileMIBGroup.setStatus("current")

fsFileTransMeansMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 2, 2, 2)
)
fsFileTransMeansMIBGroup.setObjects(
    ("FS-FILE-MIB", "fsFileTransMeans")
)
if mibBuilder.loadTexts:
    fsFileTransMeansMIBGroup.setStatus("current")


# Notification objects

fsFileSystemUpdateFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 0, 1)
)
fsFileSystemUpdateFailTrap.setObjects(
    ("FS-FILE-MIB", "fsFileTransFailedReason")
)
if mibBuilder.loadTexts:
    fsFileSystemUpdateFailTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsFileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 11, 2, 1, 1)
)
fsFileMIBCompliance.setObjects(
      *(("FS-FILE-MIB", "fsFileMIBGroup"),
        ("FS-FILE-MIB", "fsFileTransMeansMIBGroup"))
)
if mibBuilder.loadTexts:
    fsFileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-FILE-MIB",
    **{"fsFileMIB": fsFileMIB,
       "fsFileMIBTraps": fsFileMIBTraps,
       "fsFileSystemUpdateFailTrap": fsFileSystemUpdateFailTrap,
       "fsFileMIBObjects": fsFileMIBObjects,
       "fsFileTransTable": fsFileTransTable,
       "fsFileTransEntry": fsFileTransEntry,
       "fsFileTransIndex": fsFileTransIndex,
       "fsFileTransMeans": fsFileTransMeans,
       "fsFileTransOperType": fsFileTransOperType,
       "fsFileTransSrcFileName": fsFileTransSrcFileName,
       "fsFileTransDescFileName": fsFileTransDescFileName,
       "fsFileTransServerAddr": fsFileTransServerAddr,
       "fsFileTransResult": fsFileTransResult,
       "fsFileTransComplete": fsFileTransComplete,
       "fsFileTransDataLength": fsFileTransDataLength,
       "fsFileTransEntryStatus": fsFileTransEntryStatus,
       "fsFileTransServerAddr6": fsFileTransServerAddr6,
       "fsFileTransUserName": fsFileTransUserName,
       "fsFileTransPassWord": fsFileTransPassWord,
       "fsFileTransFailedReason": fsFileTransFailedReason,
       "fsFileTransFileType": fsFileTransFileType,
       "fsFileTransServerPort": fsFileTransServerPort,
       "fsFileTransPortType": fsFileTransPortType,
       "fsFileSystemMaxRoom": fsFileSystemMaxRoom,
       "fsFileSystemAvailableRoom": fsFileSystemAvailableRoom,
       "fsFileMIBConformance": fsFileMIBConformance,
       "fsFileMIBCompliances": fsFileMIBCompliances,
       "fsFileMIBCompliance": fsFileMIBCompliance,
       "fsFileMIBGroups": fsFileMIBGroups,
       "fsFileMIBGroup": fsFileMIBGroup,
       "fsFileTransMeansMIBGroup": fsFileTransMeansMIBGroup}
)
