# SNMP MIB module (AT-FILEv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/AT-FILEv2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:23:40 2025
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

atFilev2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600)
)
if mibBuilder.loadTexts:
    atFilev2.setRevisions(
        ("2008-09-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtFilev2TableOptions_ObjectIdentity = ObjectIdentity
atFilev2TableOptions = _AtFilev2TableOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1)
)


class _AtFilev2Recursive_Type(Integer32):
    """Custom type atFilev2Recursive based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AtFilev2Recursive_Type.__name__ = "Integer32"
_AtFilev2Recursive_Object = MibScalar
atFilev2Recursive = _AtFilev2Recursive_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 1),
    _AtFilev2Recursive_Type()
)
atFilev2Recursive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2Recursive.setStatus("current")


class _AtFilev2AllFiles_Type(Integer32):
    """Custom type atFilev2AllFiles based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AtFilev2AllFiles_Type.__name__ = "Integer32"
_AtFilev2AllFiles_Object = MibScalar
atFilev2AllFiles = _AtFilev2AllFiles_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 2),
    _AtFilev2AllFiles_Type()
)
atFilev2AllFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2AllFiles.setStatus("current")


class _AtFilev2Device_Type(Integer32):
    """Custom type atFilev2Device based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AtFilev2Device_Type.__name__ = "Integer32"
_AtFilev2Device_Object = MibScalar
atFilev2Device = _AtFilev2Device_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 3),
    _AtFilev2Device_Type()
)
atFilev2Device.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2Device.setStatus("current")


class _AtFilev2StackID_Type(Integer32):
    """Custom type atFilev2StackID based on Integer32"""
    defaultValue = 1


_AtFilev2StackID_Type.__name__ = "Integer32"
_AtFilev2StackID_Object = MibScalar
atFilev2StackID = _AtFilev2StackID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 4),
    _AtFilev2StackID_Type()
)
atFilev2StackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2StackID.setStatus("current")
_AtFilev2Table_Object = MibTable
atFilev2Table = _AtFilev2Table_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2)
)
if mibBuilder.loadTexts:
    atFilev2Table.setStatus("current")
_AtFilev2Entry_Object = MibTableRow
atFilev2Entry = _AtFilev2Entry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1)
)
atFilev2Entry.setIndexNames(
    (0, "AT-FILEv2-MIB", "atFilev2Filename"),
)
if mibBuilder.loadTexts:
    atFilev2Entry.setStatus("current")
_AtFilev2Filename_Type = OctetString
_AtFilev2Filename_Object = MibTableColumn
atFilev2Filename = _AtFilev2Filename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 1),
    _AtFilev2Filename_Type()
)
atFilev2Filename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2Filename.setStatus("current")
_AtFilev2FileSize_Type = Integer32
_AtFilev2FileSize_Object = MibTableColumn
atFilev2FileSize = _AtFilev2FileSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 2),
    _AtFilev2FileSize_Type()
)
atFilev2FileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileSize.setStatus("current")
_AtFilev2FileCreationTime_Type = OctetString
_AtFilev2FileCreationTime_Object = MibTableColumn
atFilev2FileCreationTime = _AtFilev2FileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 3),
    _AtFilev2FileCreationTime_Type()
)
atFilev2FileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileCreationTime.setStatus("current")
_AtFilev2FileAttribs_Type = OctetString
_AtFilev2FileAttribs_Object = MibTableColumn
atFilev2FileAttribs = _AtFilev2FileAttribs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 4),
    _AtFilev2FileAttribs_Type()
)
atFilev2FileAttribs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2FileAttribs.setStatus("current")
_AtFilev2FileOperation_ObjectIdentity = ObjectIdentity
atFilev2FileOperation = _AtFilev2FileOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3)
)
_AtFilev2SourceStackID_Type = Integer32
_AtFilev2SourceStackID_Object = MibScalar
atFilev2SourceStackID = _AtFilev2SourceStackID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 1),
    _AtFilev2SourceStackID_Type()
)
atFilev2SourceStackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2SourceStackID.setStatus("current")


class _AtFilev2SourceDevice_Type(Integer32):
    """Custom type atFilev2SourceDevice based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtFilev2SourceDevice_Type.__name__ = "Integer32"
_AtFilev2SourceDevice_Object = MibScalar
atFilev2SourceDevice = _AtFilev2SourceDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 2),
    _AtFilev2SourceDevice_Type()
)
atFilev2SourceDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2SourceDevice.setStatus("current")
_AtFilev2SourceFilename_Type = DisplayString
_AtFilev2SourceFilename_Object = MibScalar
atFilev2SourceFilename = _AtFilev2SourceFilename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 3),
    _AtFilev2SourceFilename_Type()
)
atFilev2SourceFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2SourceFilename.setStatus("current")
_AtFilev2DestinationStackID_Type = Integer32
_AtFilev2DestinationStackID_Object = MibScalar
atFilev2DestinationStackID = _AtFilev2DestinationStackID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 4),
    _AtFilev2DestinationStackID_Type()
)
atFilev2DestinationStackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DestinationStackID.setStatus("current")


class _AtFilev2DestinationDevice_Type(Integer32):
    """Custom type atFilev2DestinationDevice based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtFilev2DestinationDevice_Type.__name__ = "Integer32"
_AtFilev2DestinationDevice_Object = MibScalar
atFilev2DestinationDevice = _AtFilev2DestinationDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 5),
    _AtFilev2DestinationDevice_Type()
)
atFilev2DestinationDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DestinationDevice.setStatus("current")
_AtFilev2DestinationFilename_Type = DisplayString
_AtFilev2DestinationFilename_Object = MibScalar
atFilev2DestinationFilename = _AtFilev2DestinationFilename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 6),
    _AtFilev2DestinationFilename_Type()
)
atFilev2DestinationFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DestinationFilename.setStatus("current")
_AtFilev2CopyBegin_Type = OctetString
_AtFilev2CopyBegin_Object = MibScalar
atFilev2CopyBegin = _AtFilev2CopyBegin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 7),
    _AtFilev2CopyBegin_Type()
)
atFilev2CopyBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2CopyBegin.setStatus("current")
_AtFilev2MoveBegin_Type = OctetString
_AtFilev2MoveBegin_Object = MibScalar
atFilev2MoveBegin = _AtFilev2MoveBegin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 8),
    _AtFilev2MoveBegin_Type()
)
atFilev2MoveBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2MoveBegin.setStatus("current")
_AtFilev2DeleteBegin_Type = OctetString
_AtFilev2DeleteBegin_Object = MibScalar
atFilev2DeleteBegin = _AtFilev2DeleteBegin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 9),
    _AtFilev2DeleteBegin_Type()
)
atFilev2DeleteBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2DeleteBegin.setStatus("current")
_AtFilev2Flash1_ObjectIdentity = ObjectIdentity
atFilev2Flash1 = _AtFilev2Flash1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 10)
)
_AtFilev2Card2_ObjectIdentity = ObjectIdentity
atFilev2Card2 = _AtFilev2Card2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 11)
)
_AtFilev2Nvs3_ObjectIdentity = ObjectIdentity
atFilev2Nvs3 = _AtFilev2Nvs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 12)
)
_AtFilev2Tftp4_ObjectIdentity = ObjectIdentity
atFilev2Tftp4 = _AtFilev2Tftp4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 13)
)
_AtFilev2TftpIPAddr_Type = IpAddress
_AtFilev2TftpIPAddr_Object = MibScalar
atFilev2TftpIPAddr = _AtFilev2TftpIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 13, 1),
    _AtFilev2TftpIPAddr_Type()
)
atFilev2TftpIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atFilev2TftpIPAddr.setStatus("current")
_AtFilev2SDcardTable_Object = MibTable
atFilev2SDcardTable = _AtFilev2SDcardTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4)
)
if mibBuilder.loadTexts:
    atFilev2SDcardTable.setStatus("current")
_AtFilev2SDcardEntry_Object = MibTableRow
atFilev2SDcardEntry = _AtFilev2SDcardEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4, 1)
)
atFilev2SDcardEntry.setIndexNames(
    (0, "AT-FILEv2-MIB", "atFilev2SDcardStackMemberId"),
)
if mibBuilder.loadTexts:
    atFilev2SDcardEntry.setStatus("current")
_AtFilev2SDcardStackMemberId_Type = Unsigned32
_AtFilev2SDcardStackMemberId_Object = MibTableColumn
atFilev2SDcardStackMemberId = _AtFilev2SDcardStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4, 1, 1),
    _AtFilev2SDcardStackMemberId_Type()
)
atFilev2SDcardStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2SDcardStackMemberId.setStatus("current")


class _AtFilev2SDcardPresence_Type(Integer32):
    """Custom type atFilev2SDcardPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_AtFilev2SDcardPresence_Type.__name__ = "Integer32"
_AtFilev2SDcardPresence_Object = MibTableColumn
atFilev2SDcardPresence = _AtFilev2SDcardPresence_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4, 1, 2),
    _AtFilev2SDcardPresence_Type()
)
atFilev2SDcardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atFilev2SDcardPresence.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-FILEv2-MIB",
    **{"atFilev2": atFilev2,
       "atFilev2TableOptions": atFilev2TableOptions,
       "atFilev2Recursive": atFilev2Recursive,
       "atFilev2AllFiles": atFilev2AllFiles,
       "atFilev2Device": atFilev2Device,
       "atFilev2StackID": atFilev2StackID,
       "atFilev2Table": atFilev2Table,
       "atFilev2Entry": atFilev2Entry,
       "atFilev2Filename": atFilev2Filename,
       "atFilev2FileSize": atFilev2FileSize,
       "atFilev2FileCreationTime": atFilev2FileCreationTime,
       "atFilev2FileAttribs": atFilev2FileAttribs,
       "atFilev2FileOperation": atFilev2FileOperation,
       "atFilev2SourceStackID": atFilev2SourceStackID,
       "atFilev2SourceDevice": atFilev2SourceDevice,
       "atFilev2SourceFilename": atFilev2SourceFilename,
       "atFilev2DestinationStackID": atFilev2DestinationStackID,
       "atFilev2DestinationDevice": atFilev2DestinationDevice,
       "atFilev2DestinationFilename": atFilev2DestinationFilename,
       "atFilev2CopyBegin": atFilev2CopyBegin,
       "atFilev2MoveBegin": atFilev2MoveBegin,
       "atFilev2DeleteBegin": atFilev2DeleteBegin,
       "atFilev2Flash1": atFilev2Flash1,
       "atFilev2Card2": atFilev2Card2,
       "atFilev2Nvs3": atFilev2Nvs3,
       "atFilev2Tftp4": atFilev2Tftp4,
       "atFilev2TftpIPAddr": atFilev2TftpIPAddr,
       "atFilev2SDcardTable": atFilev2SDcardTable,
       "atFilev2SDcardEntry": atFilev2SDcardEntry,
       "atFilev2SDcardStackMemberId": atFilev2SDcardStackMemberId,
       "atFilev2SDcardPresence": atFilev2SDcardPresence}
)
