# SNMP MIB module (QTECH-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-FILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:54 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechFileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11)
)
if mibBuilder.loadTexts:
    qtechFileMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechFileMIBTraps_ObjectIdentity = ObjectIdentity
qtechFileMIBTraps = _QtechFileMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 0)
)
_QtechFileMIBObjects_ObjectIdentity = ObjectIdentity
qtechFileMIBObjects = _QtechFileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1)
)
_QtechFileTransTable_Object = MibTable
qtechFileTransTable = _QtechFileTransTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    qtechFileTransTable.setStatus("current")
_QtechFileTransEntry_Object = MibTableRow
qtechFileTransEntry = _QtechFileTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1)
)
qtechFileTransEntry.setIndexNames(
    (0, "QTECH-FILE-MIB", "qtechFileTransIndex"),
)
if mibBuilder.loadTexts:
    qtechFileTransEntry.setStatus("current")
_QtechFileTransIndex_Type = Integer32
_QtechFileTransIndex_Object = MibTableColumn
qtechFileTransIndex = _QtechFileTransIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 1),
    _QtechFileTransIndex_Type()
)
qtechFileTransIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFileTransIndex.setStatus("current")


class _QtechFileTransMeans_Type(Integer32):
    """Custom type qtechFileTransMeans based on Integer32"""
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


_QtechFileTransMeans_Type.__name__ = "Integer32"
_QtechFileTransMeans_Object = MibTableColumn
qtechFileTransMeans = _QtechFileTransMeans_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 2),
    _QtechFileTransMeans_Type()
)
qtechFileTransMeans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechFileTransMeans.setStatus("current")


class _QtechFileTransOperType_Type(Integer32):
    """Custom type qtechFileTransOperType based on Integer32"""
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


_QtechFileTransOperType_Type.__name__ = "Integer32"
_QtechFileTransOperType_Object = MibTableColumn
qtechFileTransOperType = _QtechFileTransOperType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 3),
    _QtechFileTransOperType_Type()
)
qtechFileTransOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechFileTransOperType.setStatus("current")
_QtechFileTransSrcFileName_Type = DisplayString
_QtechFileTransSrcFileName_Object = MibTableColumn
qtechFileTransSrcFileName = _QtechFileTransSrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 4),
    _QtechFileTransSrcFileName_Type()
)
qtechFileTransSrcFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechFileTransSrcFileName.setStatus("current")
_QtechFileTransDescFileName_Type = DisplayString
_QtechFileTransDescFileName_Object = MibTableColumn
qtechFileTransDescFileName = _QtechFileTransDescFileName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 5),
    _QtechFileTransDescFileName_Type()
)
qtechFileTransDescFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechFileTransDescFileName.setStatus("current")
_QtechFileTransServerAddr_Type = IpAddress
_QtechFileTransServerAddr_Object = MibTableColumn
qtechFileTransServerAddr = _QtechFileTransServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 6),
    _QtechFileTransServerAddr_Type()
)
qtechFileTransServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechFileTransServerAddr.setStatus("current")


class _QtechFileTransResult_Type(Integer32):
    """Custom type qtechFileTransResult based on Integer32"""
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


_QtechFileTransResult_Type.__name__ = "Integer32"
_QtechFileTransResult_Object = MibTableColumn
qtechFileTransResult = _QtechFileTransResult_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 7),
    _QtechFileTransResult_Type()
)
qtechFileTransResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFileTransResult.setStatus("current")
_QtechFileTransComplete_Type = TruthValue
_QtechFileTransComplete_Object = MibTableColumn
qtechFileTransComplete = _QtechFileTransComplete_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 8),
    _QtechFileTransComplete_Type()
)
qtechFileTransComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFileTransComplete.setStatus("current")
_QtechFileTransDataLength_Type = Gauge32
_QtechFileTransDataLength_Object = MibTableColumn
qtechFileTransDataLength = _QtechFileTransDataLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 9),
    _QtechFileTransDataLength_Type()
)
qtechFileTransDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFileTransDataLength.setStatus("current")
_QtechFileTransEntryStatus_Type = RowStatus
_QtechFileTransEntryStatus_Object = MibTableColumn
qtechFileTransEntryStatus = _QtechFileTransEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 10),
    _QtechFileTransEntryStatus_Type()
)
qtechFileTransEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechFileTransEntryStatus.setStatus("current")


class _QtechFileTransServerAddr6_Type(OctetString):
    """Custom type qtechFileTransServerAddr6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechFileTransServerAddr6_Type.__name__ = "OctetString"
_QtechFileTransServerAddr6_Object = MibTableColumn
qtechFileTransServerAddr6 = _QtechFileTransServerAddr6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 11),
    _QtechFileTransServerAddr6_Type()
)
qtechFileTransServerAddr6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechFileTransServerAddr6.setStatus("current")
_QtechFileTransUserName_Type = DisplayString
_QtechFileTransUserName_Object = MibTableColumn
qtechFileTransUserName = _QtechFileTransUserName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 12),
    _QtechFileTransUserName_Type()
)
qtechFileTransUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechFileTransUserName.setStatus("current")
_QtechFileTransPassWord_Type = DisplayString
_QtechFileTransPassWord_Object = MibTableColumn
qtechFileTransPassWord = _QtechFileTransPassWord_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 13),
    _QtechFileTransPassWord_Type()
)
qtechFileTransPassWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechFileTransPassWord.setStatus("current")
_QtechFileTransFailedReason_Type = DisplayString
_QtechFileTransFailedReason_Object = MibTableColumn
qtechFileTransFailedReason = _QtechFileTransFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 14),
    _QtechFileTransFailedReason_Type()
)
qtechFileTransFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFileTransFailedReason.setStatus("current")


class _QtechFileTransFileType_Type(Integer32):
    """Custom type qtechFileTransFileType based on Integer32"""
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


_QtechFileTransFileType_Type.__name__ = "Integer32"
_QtechFileTransFileType_Object = MibTableColumn
qtechFileTransFileType = _QtechFileTransFileType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 15),
    _QtechFileTransFileType_Type()
)
qtechFileTransFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechFileTransFileType.setStatus("current")
_QtechFileTransServerPort_Type = Integer32
_QtechFileTransServerPort_Object = MibTableColumn
qtechFileTransServerPort = _QtechFileTransServerPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 16),
    _QtechFileTransServerPort_Type()
)
qtechFileTransServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechFileTransServerPort.setStatus("current")


class _QtechFileTransPortType_Type(Integer32):
    """Custom type qtechFileTransPortType based on Integer32"""
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


_QtechFileTransPortType_Type.__name__ = "Integer32"
_QtechFileTransPortType_Object = MibTableColumn
qtechFileTransPortType = _QtechFileTransPortType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 1, 1, 17),
    _QtechFileTransPortType_Type()
)
qtechFileTransPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechFileTransPortType.setStatus("current")
_QtechFileSystemMaxRoom_Type = Integer32
_QtechFileSystemMaxRoom_Object = MibScalar
qtechFileSystemMaxRoom = _QtechFileSystemMaxRoom_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 2),
    _QtechFileSystemMaxRoom_Type()
)
qtechFileSystemMaxRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFileSystemMaxRoom.setStatus("current")
_QtechFileSystemAvailableRoom_Type = Integer32
_QtechFileSystemAvailableRoom_Object = MibScalar
qtechFileSystemAvailableRoom = _QtechFileSystemAvailableRoom_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 1, 3),
    _QtechFileSystemAvailableRoom_Type()
)
qtechFileSystemAvailableRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFileSystemAvailableRoom.setStatus("current")
_QtechFileMIBConformance_ObjectIdentity = ObjectIdentity
qtechFileMIBConformance = _QtechFileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 2)
)
_QtechFileMIBCompliances_ObjectIdentity = ObjectIdentity
qtechFileMIBCompliances = _QtechFileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 2, 1)
)
_QtechFileMIBGroups_ObjectIdentity = ObjectIdentity
qtechFileMIBGroups = _QtechFileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 2, 2)
)

# Managed Objects groups

qtechFileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 2, 2, 1)
)
qtechFileMIBGroup.setObjects(
      *(("QTECH-FILE-MIB", "qtechFileTransIndex"),
        ("QTECH-FILE-MIB", "qtechFileTransOperType"),
        ("QTECH-FILE-MIB", "qtechFileTransSrcFileName"),
        ("QTECH-FILE-MIB", "qtechFileTransDescFileName"),
        ("QTECH-FILE-MIB", "qtechFileTransServerAddr"),
        ("QTECH-FILE-MIB", "qtechFileTransResult"),
        ("QTECH-FILE-MIB", "qtechFileTransComplete"),
        ("QTECH-FILE-MIB", "qtechFileTransDataLength"),
        ("QTECH-FILE-MIB", "qtechFileTransEntryStatus"),
        ("QTECH-FILE-MIB", "qtechFileTransServerAddr6"),
        ("QTECH-FILE-MIB", "qtechFileTransUserName"),
        ("QTECH-FILE-MIB", "qtechFileTransPassWord"),
        ("QTECH-FILE-MIB", "qtechFileTransFailedReason"),
        ("QTECH-FILE-MIB", "qtechFileTransFileType"),
        ("QTECH-FILE-MIB", "qtechFileTransServerPort"),
        ("QTECH-FILE-MIB", "qtechFileTransPortType"),
        ("QTECH-FILE-MIB", "qtechFileSystemMaxRoom"),
        ("QTECH-FILE-MIB", "qtechFileSystemAvailableRoom"))
)
if mibBuilder.loadTexts:
    qtechFileMIBGroup.setStatus("current")

qtechFileTransMeansMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 2, 2, 2)
)
qtechFileTransMeansMIBGroup.setObjects(
    ("QTECH-FILE-MIB", "qtechFileTransMeans")
)
if mibBuilder.loadTexts:
    qtechFileTransMeansMIBGroup.setStatus("current")


# Notification objects

qtechFileSystemUpdateFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 0, 1)
)
qtechFileSystemUpdateFailTrap.setObjects(
    ("QTECH-FILE-MIB", "qtechFileTransFailedReason")
)
if mibBuilder.loadTexts:
    qtechFileSystemUpdateFailTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechFileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 11, 2, 1, 1)
)
qtechFileMIBCompliance.setObjects(
      *(("QTECH-FILE-MIB", "qtechFileMIBGroup"),
        ("QTECH-FILE-MIB", "qtechFileTransMeansMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechFileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-FILE-MIB",
    **{"qtechFileMIB": qtechFileMIB,
       "qtechFileMIBTraps": qtechFileMIBTraps,
       "qtechFileSystemUpdateFailTrap": qtechFileSystemUpdateFailTrap,
       "qtechFileMIBObjects": qtechFileMIBObjects,
       "qtechFileTransTable": qtechFileTransTable,
       "qtechFileTransEntry": qtechFileTransEntry,
       "qtechFileTransIndex": qtechFileTransIndex,
       "qtechFileTransMeans": qtechFileTransMeans,
       "qtechFileTransOperType": qtechFileTransOperType,
       "qtechFileTransSrcFileName": qtechFileTransSrcFileName,
       "qtechFileTransDescFileName": qtechFileTransDescFileName,
       "qtechFileTransServerAddr": qtechFileTransServerAddr,
       "qtechFileTransResult": qtechFileTransResult,
       "qtechFileTransComplete": qtechFileTransComplete,
       "qtechFileTransDataLength": qtechFileTransDataLength,
       "qtechFileTransEntryStatus": qtechFileTransEntryStatus,
       "qtechFileTransServerAddr6": qtechFileTransServerAddr6,
       "qtechFileTransUserName": qtechFileTransUserName,
       "qtechFileTransPassWord": qtechFileTransPassWord,
       "qtechFileTransFailedReason": qtechFileTransFailedReason,
       "qtechFileTransFileType": qtechFileTransFileType,
       "qtechFileTransServerPort": qtechFileTransServerPort,
       "qtechFileTransPortType": qtechFileTransPortType,
       "qtechFileSystemMaxRoom": qtechFileSystemMaxRoom,
       "qtechFileSystemAvailableRoom": qtechFileSystemAvailableRoom,
       "qtechFileMIBConformance": qtechFileMIBConformance,
       "qtechFileMIBCompliances": qtechFileMIBCompliances,
       "qtechFileMIBCompliance": qtechFileMIBCompliance,
       "qtechFileMIBGroups": qtechFileMIBGroups,
       "qtechFileMIBGroup": qtechFileMIBGroup,
       "qtechFileTransMeansMIBGroup": qtechFileTransMeansMIBGroup}
)
