# SNMP MIB module (ZTE-AN-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-FILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:51 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnFileMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnFileStorageDevMgmt_ObjectIdentity = ObjectIdentity
zxAnFileStorageDevMgmt = _ZxAnFileStorageDevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1)
)
_ZxAnFileStorageDevTable_Object = MibTable
zxAnFileStorageDevTable = _ZxAnFileStorageDevTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnFileStorageDevTable.setStatus("current")
_ZxAnFileStorageDevEntry_Object = MibTableRow
zxAnFileStorageDevEntry = _ZxAnFileStorageDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1)
)
zxAnFileStorageDevEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevRack"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevShelf"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSlot"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSubCard"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevType"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevId"),
)
if mibBuilder.loadTexts:
    zxAnFileStorageDevEntry.setStatus("current")
_ZxAnFileStorageDevRack_Type = Integer32
_ZxAnFileStorageDevRack_Object = MibTableColumn
zxAnFileStorageDevRack = _ZxAnFileStorageDevRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 1),
    _ZxAnFileStorageDevRack_Type()
)
zxAnFileStorageDevRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileStorageDevRack.setStatus("current")
_ZxAnFileStorageDevShelf_Type = Integer32
_ZxAnFileStorageDevShelf_Object = MibTableColumn
zxAnFileStorageDevShelf = _ZxAnFileStorageDevShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 2),
    _ZxAnFileStorageDevShelf_Type()
)
zxAnFileStorageDevShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileStorageDevShelf.setStatus("current")
_ZxAnFileStorageDevSlot_Type = Integer32
_ZxAnFileStorageDevSlot_Object = MibTableColumn
zxAnFileStorageDevSlot = _ZxAnFileStorageDevSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 3),
    _ZxAnFileStorageDevSlot_Type()
)
zxAnFileStorageDevSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileStorageDevSlot.setStatus("current")
_ZxAnFileStorageDevSubCard_Type = Integer32
_ZxAnFileStorageDevSubCard_Object = MibTableColumn
zxAnFileStorageDevSubCard = _ZxAnFileStorageDevSubCard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 4),
    _ZxAnFileStorageDevSubCard_Type()
)
zxAnFileStorageDevSubCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileStorageDevSubCard.setStatus("current")


class _ZxAnFileStorageDevType_Type(DisplayString):
    """Custom type zxAnFileStorageDevType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnFileStorageDevType_Type.__name__ = "DisplayString"
_ZxAnFileStorageDevType_Object = MibTableColumn
zxAnFileStorageDevType = _ZxAnFileStorageDevType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 5),
    _ZxAnFileStorageDevType_Type()
)
zxAnFileStorageDevType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileStorageDevType.setStatus("current")
_ZxAnFileStorageDevId_Type = Integer32
_ZxAnFileStorageDevId_Object = MibTableColumn
zxAnFileStorageDevId = _ZxAnFileStorageDevId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 6),
    _ZxAnFileStorageDevId_Type()
)
zxAnFileStorageDevId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileStorageDevId.setStatus("current")
_ZxAnFileStorageDevTotalSpace_Type = Integer32
_ZxAnFileStorageDevTotalSpace_Object = MibTableColumn
zxAnFileStorageDevTotalSpace = _ZxAnFileStorageDevTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 7),
    _ZxAnFileStorageDevTotalSpace_Type()
)
zxAnFileStorageDevTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileStorageDevTotalSpace.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFileStorageDevTotalSpace.setUnits("KB")
_ZxAnFileStorageDevAvailableSpace_Type = Integer32
_ZxAnFileStorageDevAvailableSpace_Object = MibTableColumn
zxAnFileStorageDevAvailableSpace = _ZxAnFileStorageDevAvailableSpace_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 8),
    _ZxAnFileStorageDevAvailableSpace_Type()
)
zxAnFileStorageDevAvailableSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileStorageDevAvailableSpace.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFileStorageDevAvailableSpace.setUnits("KB")


class _ZxAnFileStorageDevOperStatus_Type(Integer32):
    """Custom type zxAnFileStorageDevOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("notReady", 2))
    )


_ZxAnFileStorageDevOperStatus_Type.__name__ = "Integer32"
_ZxAnFileStorageDevOperStatus_Object = MibTableColumn
zxAnFileStorageDevOperStatus = _ZxAnFileStorageDevOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 9),
    _ZxAnFileStorageDevOperStatus_Type()
)
zxAnFileStorageDevOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileStorageDevOperStatus.setStatus("current")


class _ZxAnFileStorageDevAdminStatus_Type(Integer32):
    """Custom type zxAnFileStorageDevAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("remove", 1)
    )


_ZxAnFileStorageDevAdminStatus_Type.__name__ = "Integer32"
_ZxAnFileStorageDevAdminStatus_Object = MibTableColumn
zxAnFileStorageDevAdminStatus = _ZxAnFileStorageDevAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 1, 1, 10),
    _ZxAnFileStorageDevAdminStatus_Type()
)
zxAnFileStorageDevAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileStorageDevAdminStatus.setStatus("current")
_ZxAnStartupSeqTable_Object = MibTable
zxAnStartupSeqTable = _ZxAnStartupSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnStartupSeqTable.setStatus("current")
_ZxAnStartupSeqEntry_Object = MibTableRow
zxAnStartupSeqEntry = _ZxAnStartupSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 5, 1)
)
zxAnStartupSeqEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnStartupSeqIndex"),
)
if mibBuilder.loadTexts:
    zxAnStartupSeqEntry.setStatus("current")
_ZxAnStartupSeqIndex_Type = Integer32
_ZxAnStartupSeqIndex_Object = MibTableColumn
zxAnStartupSeqIndex = _ZxAnStartupSeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 5, 1, 1),
    _ZxAnStartupSeqIndex_Type()
)
zxAnStartupSeqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnStartupSeqIndex.setStatus("current")
_ZxAnStartupSeqRack_Type = Integer32
_ZxAnStartupSeqRack_Object = MibTableColumn
zxAnStartupSeqRack = _ZxAnStartupSeqRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 5, 1, 2),
    _ZxAnStartupSeqRack_Type()
)
zxAnStartupSeqRack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnStartupSeqRack.setStatus("current")
_ZxAnStartupSeqShelf_Type = Integer32
_ZxAnStartupSeqShelf_Object = MibTableColumn
zxAnStartupSeqShelf = _ZxAnStartupSeqShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 5, 1, 3),
    _ZxAnStartupSeqShelf_Type()
)
zxAnStartupSeqShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnStartupSeqShelf.setStatus("current")
_ZxAnStartupSeqSlot_Type = Integer32
_ZxAnStartupSeqSlot_Object = MibTableColumn
zxAnStartupSeqSlot = _ZxAnStartupSeqSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 5, 1, 4),
    _ZxAnStartupSeqSlot_Type()
)
zxAnStartupSeqSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnStartupSeqSlot.setStatus("current")


class _ZxAnStartupSeqSubCard_Type(Integer32):
    """Custom type zxAnStartupSeqSubCard based on Integer32"""
    defaultValue = 0


_ZxAnStartupSeqSubCard_Type.__name__ = "Integer32"
_ZxAnStartupSeqSubCard_Object = MibTableColumn
zxAnStartupSeqSubCard = _ZxAnStartupSeqSubCard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 5, 1, 5),
    _ZxAnStartupSeqSubCard_Type()
)
zxAnStartupSeqSubCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnStartupSeqSubCard.setStatus("current")


class _ZxAnStartupSeqDevType_Type(DisplayString):
    """Custom type zxAnStartupSeqDevType based on DisplayString"""
    defaultValue = OctetString("flash")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnStartupSeqDevType_Type.__name__ = "DisplayString"
_ZxAnStartupSeqDevType_Object = MibTableColumn
zxAnStartupSeqDevType = _ZxAnStartupSeqDevType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 5, 1, 6),
    _ZxAnStartupSeqDevType_Type()
)
zxAnStartupSeqDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnStartupSeqDevType.setStatus("current")
_ZxAnStartupSeqDevId_Type = Integer32
_ZxAnStartupSeqDevId_Object = MibTableColumn
zxAnStartupSeqDevId = _ZxAnStartupSeqDevId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 1, 5, 1, 7),
    _ZxAnStartupSeqDevId_Type()
)
zxAnStartupSeqDevId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnStartupSeqDevId.setStatus("current")
_ZxAnFileMgmt_ObjectIdentity = ObjectIdentity
zxAnFileMgmt = _ZxAnFileMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2)
)
_ZxAnFileTable_Object = MibTable
zxAnFileTable = _ZxAnFileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnFileTable.setStatus("current")
_ZxAnFileEntry_Object = MibTableRow
zxAnFileEntry = _ZxAnFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1, 1)
)
zxAnFileEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevRack"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevShelf"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSlot"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSubCard"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevType"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevId"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileName"),
)
if mibBuilder.loadTexts:
    zxAnFileEntry.setStatus("current")


class _ZxAnFileName_Type(DisplayString):
    """Custom type zxAnFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnFileName_Type.__name__ = "DisplayString"
_ZxAnFileName_Object = MibTableColumn
zxAnFileName = _ZxAnFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1, 1, 1),
    _ZxAnFileName_Type()
)
zxAnFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileName.setStatus("current")


class _ZxAnFileType_Type(Integer32):
    """Custom type zxAnFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("directory", 2))
    )


_ZxAnFileType_Type.__name__ = "Integer32"
_ZxAnFileType_Object = MibTableColumn
zxAnFileType = _ZxAnFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1, 1, 2),
    _ZxAnFileType_Type()
)
zxAnFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileType.setStatus("current")
_ZxAnFileSize_Type = Integer32
_ZxAnFileSize_Object = MibTableColumn
zxAnFileSize = _ZxAnFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1, 1, 3),
    _ZxAnFileSize_Type()
)
zxAnFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFileSize.setUnits("byte")


class _ZxAnFileModifyTime_Type(DisplayString):
    """Custom type zxAnFileModifyTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnFileModifyTime_Type.__name__ = "DisplayString"
_ZxAnFileModifyTime_Object = MibTableColumn
zxAnFileModifyTime = _ZxAnFileModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1, 1, 4),
    _ZxAnFileModifyTime_Type()
)
zxAnFileModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileModifyTime.setStatus("current")


class _ZxAnFilePermissions_Type(Bits):
    """Custom type zxAnFilePermissions based on Bits"""
    namedValues = NamedValues(
        *(("read", 0),
          ("write", 1),
          ("execute", 2))
    )

_ZxAnFilePermissions_Type.__name__ = "Bits"
_ZxAnFilePermissions_Object = MibTableColumn
zxAnFilePermissions = _ZxAnFilePermissions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1, 1, 5),
    _ZxAnFilePermissions_Type()
)
zxAnFilePermissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFilePermissions.setStatus("current")


class _ZxAnDirOwner_Type(Integer32):
    """Custom type zxAnDirOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("user", 2))
    )


_ZxAnDirOwner_Type.__name__ = "Integer32"
_ZxAnDirOwner_Object = MibTableColumn
zxAnDirOwner = _ZxAnDirOwner_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1, 1, 6),
    _ZxAnDirOwner_Type()
)
zxAnDirOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDirOwner.setStatus("current")
_ZxAnDirTotalFilesCount_Type = Integer32
_ZxAnDirTotalFilesCount_Object = MibTableColumn
zxAnDirTotalFilesCount = _ZxAnDirTotalFilesCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1, 1, 7),
    _ZxAnDirTotalFilesCount_Type()
)
zxAnDirTotalFilesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDirTotalFilesCount.setStatus("current")


class _ZxAnFileAdminStatus_Type(Integer32):
    """Custom type zxAnFileAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erase", 1),
          ("synchToSlave", 2),
          ("cancelSynchToSlave", 3))
    )


_ZxAnFileAdminStatus_Type.__name__ = "Integer32"
_ZxAnFileAdminStatus_Object = MibTableColumn
zxAnFileAdminStatus = _ZxAnFileAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 1, 1, 8),
    _ZxAnFileAdminStatus_Type()
)
zxAnFileAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileAdminStatus.setStatus("current")
_ZxAnFileCopyMgmt_ObjectIdentity = ObjectIdentity
zxAnFileCopyMgmt = _ZxAnFileCopyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20)
)
_ZxAnFileCopySrcFileSpecific_Type = ObjectIdentifier
_ZxAnFileCopySrcFileSpecific_Object = MibScalar
zxAnFileCopySrcFileSpecific = _ZxAnFileCopySrcFileSpecific_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20, 1),
    _ZxAnFileCopySrcFileSpecific_Type()
)
zxAnFileCopySrcFileSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileCopySrcFileSpecific.setStatus("current")
_ZxAnFileCopyDestDirSpecific_Type = ObjectIdentifier
_ZxAnFileCopyDestDirSpecific_Object = MibScalar
zxAnFileCopyDestDirSpecific = _ZxAnFileCopyDestDirSpecific_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20, 2),
    _ZxAnFileCopyDestDirSpecific_Type()
)
zxAnFileCopyDestDirSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileCopyDestDirSpecific.setStatus("current")


class _ZxAnFileCopyCancel_Type(Integer32):
    """Custom type zxAnFileCopyCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cancel", 1)
    )


_ZxAnFileCopyCancel_Type.__name__ = "Integer32"
_ZxAnFileCopyCancel_Object = MibScalar
zxAnFileCopyCancel = _ZxAnFileCopyCancel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20, 3),
    _ZxAnFileCopyCancel_Type()
)
zxAnFileCopyCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileCopyCancel.setStatus("current")
_ZxAnFileCopyStatusTable_Object = MibTable
zxAnFileCopyStatusTable = _ZxAnFileCopyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20, 15)
)
if mibBuilder.loadTexts:
    zxAnFileCopyStatusTable.setStatus("current")
_ZxAnFileCopyStatusEntry_Object = MibTableRow
zxAnFileCopyStatusEntry = _ZxAnFileCopyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20, 15, 1)
)
zxAnFileCopyStatusEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevRack"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevShelf"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSlot"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSubCard"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevType"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevId"),
    (0, "ZTE-AN-FILE-MIB", "zxAnCopyFileName"),
)
if mibBuilder.loadTexts:
    zxAnFileCopyStatusEntry.setStatus("current")


class _ZxAnCopyFileName_Type(DisplayString):
    """Custom type zxAnCopyFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCopyFileName_Type.__name__ = "DisplayString"
_ZxAnCopyFileName_Object = MibTableColumn
zxAnCopyFileName = _ZxAnCopyFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20, 15, 1, 1),
    _ZxAnCopyFileName_Type()
)
zxAnCopyFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCopyFileName.setStatus("current")


class _ZxAnFileCopyStatus_Type(Integer32):
    """Custom type zxAnFileCopyStatus based on Integer32"""
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
          ("inprogress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnFileCopyStatus_Type.__name__ = "Integer32"
_ZxAnFileCopyStatus_Object = MibTableColumn
zxAnFileCopyStatus = _ZxAnFileCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20, 15, 1, 2),
    _ZxAnFileCopyStatus_Type()
)
zxAnFileCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileCopyStatus.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFileCopyStatus.setUnits("byte")


class _ZxAnFileCopyProgress_Type(Integer32):
    """Custom type zxAnFileCopyProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnFileCopyProgress_Type.__name__ = "Integer32"
_ZxAnFileCopyProgress_Object = MibTableColumn
zxAnFileCopyProgress = _ZxAnFileCopyProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20, 15, 1, 3),
    _ZxAnFileCopyProgress_Type()
)
zxAnFileCopyProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileCopyProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFileCopyProgress.setUnits("%")


class _ZxAnFileCopyFailedReason_Type(DisplayString):
    """Custom type zxAnFileCopyFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnFileCopyFailedReason_Type.__name__ = "DisplayString"
_ZxAnFileCopyFailedReason_Object = MibTableColumn
zxAnFileCopyFailedReason = _ZxAnFileCopyFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 20, 15, 1, 4),
    _ZxAnFileCopyFailedReason_Type()
)
zxAnFileCopyFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileCopyFailedReason.setStatus("current")
_ZxAnFileSynchMgmt_ObjectIdentity = ObjectIdentity
zxAnFileSynchMgmt = _ZxAnFileSynchMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 30)
)
_ZxAnFileSyncStatusTable_Object = MibTable
zxAnFileSyncStatusTable = _ZxAnFileSyncStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 30, 9)
)
if mibBuilder.loadTexts:
    zxAnFileSyncStatusTable.setStatus("current")
_ZxAnFileSyncStatusEntry_Object = MibTableRow
zxAnFileSyncStatusEntry = _ZxAnFileSyncStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 30, 9, 1)
)
zxAnFileSyncStatusEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevRack"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevShelf"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSlot"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSubCard"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevType"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevId"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileSyncFileName"),
)
if mibBuilder.loadTexts:
    zxAnFileSyncStatusEntry.setStatus("current")


class _ZxAnFileSyncFileName_Type(DisplayString):
    """Custom type zxAnFileSyncFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnFileSyncFileName_Type.__name__ = "DisplayString"
_ZxAnFileSyncFileName_Object = MibTableColumn
zxAnFileSyncFileName = _ZxAnFileSyncFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 30, 9, 1, 1),
    _ZxAnFileSyncFileName_Type()
)
zxAnFileSyncFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileSyncFileName.setStatus("current")


class _ZxAnFileSyncStatus_Type(Integer32):
    """Custom type zxAnFileSyncStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("processing", 2),
          ("failed", 3),
          ("success", 4),
          ("sameversion", 5))
    )


_ZxAnFileSyncStatus_Type.__name__ = "Integer32"
_ZxAnFileSyncStatus_Object = MibTableColumn
zxAnFileSyncStatus = _ZxAnFileSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 30, 9, 1, 2),
    _ZxAnFileSyncStatus_Type()
)
zxAnFileSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileSyncStatus.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFileSyncStatus.setUnits("byte")


class _ZxAnFileSyncProgress_Type(Integer32):
    """Custom type zxAnFileSyncProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnFileSyncProgress_Type.__name__ = "Integer32"
_ZxAnFileSyncProgress_Object = MibTableColumn
zxAnFileSyncProgress = _ZxAnFileSyncProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 30, 9, 1, 3),
    _ZxAnFileSyncProgress_Type()
)
zxAnFileSyncProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileSyncProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFileSyncProgress.setUnits("%")


class _ZxAnFileSyncFailedReason_Type(DisplayString):
    """Custom type zxAnFileSyncFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnFileSyncFailedReason_Type.__name__ = "DisplayString"
_ZxAnFileSyncFailedReason_Object = MibTableColumn
zxAnFileSyncFailedReason = _ZxAnFileSyncFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 30, 9, 1, 4),
    _ZxAnFileSyncFailedReason_Type()
)
zxAnFileSyncFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFileSyncFailedReason.setStatus("current")
_ZxAnSoftwareMgmt_ObjectIdentity = ObjectIdentity
zxAnSoftwareMgmt = _ZxAnSoftwareMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50)
)
_ZxAnSoftwareVersionTable_Object = MibTable
zxAnSoftwareVersionTable = _ZxAnSoftwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2)
)
if mibBuilder.loadTexts:
    zxAnSoftwareVersionTable.setStatus("current")
_ZxAnSoftwareVersionEntry_Object = MibTableRow
zxAnSoftwareVersionEntry = _ZxAnSoftwareVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2, 1)
)
zxAnSoftwareVersionEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevRack"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevShelf"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSlot"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSubCard"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevType"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevId"),
    (0, "ZTE-AN-FILE-MIB", "zxAnSwVersionFileName"),
)
if mibBuilder.loadTexts:
    zxAnSoftwareVersionEntry.setStatus("current")


class _ZxAnSwVersionFileName_Type(DisplayString):
    """Custom type zxAnSwVersionFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwVersionFileName_Type.__name__ = "DisplayString"
_ZxAnSwVersionFileName_Object = MibTableColumn
zxAnSwVersionFileName = _ZxAnSwVersionFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2, 1, 1),
    _ZxAnSwVersionFileName_Type()
)
zxAnSwVersionFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwVersionFileName.setStatus("current")


class _ZxAnSwVersionType_Type(DisplayString):
    """Custom type zxAnSwVersionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwVersionType_Type.__name__ = "DisplayString"
_ZxAnSwVersionType_Object = MibTableColumn
zxAnSwVersionType = _ZxAnSwVersionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2, 1, 2),
    _ZxAnSwVersionType_Type()
)
zxAnSwVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVersionType.setStatus("current")


class _ZxAnSwVersion_Type(DisplayString):
    """Custom type zxAnSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwVersion_Type.__name__ = "DisplayString"
_ZxAnSwVersion_Object = MibTableColumn
zxAnSwVersion = _ZxAnSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2, 1, 3),
    _ZxAnSwVersion_Type()
)
zxAnSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVersion.setStatus("current")
_ZxAnSwVersionFileSize_Type = Integer32
_ZxAnSwVersionFileSize_Object = MibTableColumn
zxAnSwVersionFileSize = _ZxAnSwVersionFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2, 1, 4),
    _ZxAnSwVersionFileSize_Type()
)
zxAnSwVersionFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVersionFileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwVersionFileSize.setUnits("byte")


class _ZxAnSwVersionBuildTime_Type(DisplayString):
    """Custom type zxAnSwVersionBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwVersionBuildTime_Type.__name__ = "DisplayString"
_ZxAnSwVersionBuildTime_Object = MibTableColumn
zxAnSwVersionBuildTime = _ZxAnSwVersionBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2, 1, 5),
    _ZxAnSwVersionBuildTime_Type()
)
zxAnSwVersionBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVersionBuildTime.setStatus("current")


class _ZxAnSwVersionActiveStatus_Type(Integer32):
    """Custom type zxAnSwVersionActiveStatus based on Integer32"""
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
        *(("activeAndRunning", 1),
          ("activeButNotRunning", 2),
          ("deactiveButRunning", 3),
          ("deactiveAndNotRunning", 4),
          ("na", 5))
    )


_ZxAnSwVersionActiveStatus_Type.__name__ = "Integer32"
_ZxAnSwVersionActiveStatus_Object = MibTableColumn
zxAnSwVersionActiveStatus = _ZxAnSwVersionActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2, 1, 6),
    _ZxAnSwVersionActiveStatus_Type()
)
zxAnSwVersionActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVersionActiveStatus.setStatus("current")


class _ZxAnSwVersionAdminStatus_Type(Integer32):
    """Custom type zxAnSwVersionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activate", 1)
    )


_ZxAnSwVersionAdminStatus_Type.__name__ = "Integer32"
_ZxAnSwVersionAdminStatus_Object = MibTableColumn
zxAnSwVersionAdminStatus = _ZxAnSwVersionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2, 1, 7),
    _ZxAnSwVersionAdminStatus_Type()
)
zxAnSwVersionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwVersionAdminStatus.setStatus("current")


class _ZxAnSwVersionActivatedTime_Type(DisplayString):
    """Custom type zxAnSwVersionActivatedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwVersionActivatedTime_Type.__name__ = "DisplayString"
_ZxAnSwVersionActivatedTime_Object = MibTableColumn
zxAnSwVersionActivatedTime = _ZxAnSwVersionActivatedTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 2, 1, 8),
    _ZxAnSwVersionActivatedTime_Type()
)
zxAnSwVersionActivatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVersionActivatedTime.setStatus("current")
_ZxAnCardRunningVersionTable_Object = MibTable
zxAnCardRunningVersionTable = _ZxAnCardRunningVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3)
)
if mibBuilder.loadTexts:
    zxAnCardRunningVersionTable.setStatus("current")
_ZxAnCardRunningVersionEntry_Object = MibTableRow
zxAnCardRunningVersionEntry = _ZxAnCardRunningVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1)
)
zxAnCardRunningVersionEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnCardSwRack"),
    (0, "ZTE-AN-FILE-MIB", "zxAnCardSwShelf"),
    (0, "ZTE-AN-FILE-MIB", "zxAnCardSwSlot"),
    (0, "ZTE-AN-FILE-MIB", "zxAnCardSwSubCard"),
)
if mibBuilder.loadTexts:
    zxAnCardRunningVersionEntry.setStatus("current")
_ZxAnCardSwRack_Type = Integer32
_ZxAnCardSwRack_Object = MibTableColumn
zxAnCardSwRack = _ZxAnCardSwRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 1),
    _ZxAnCardSwRack_Type()
)
zxAnCardSwRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCardSwRack.setStatus("current")
_ZxAnCardSwShelf_Type = Integer32
_ZxAnCardSwShelf_Object = MibTableColumn
zxAnCardSwShelf = _ZxAnCardSwShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 2),
    _ZxAnCardSwShelf_Type()
)
zxAnCardSwShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCardSwShelf.setStatus("current")
_ZxAnCardSwSlot_Type = Integer32
_ZxAnCardSwSlot_Object = MibTableColumn
zxAnCardSwSlot = _ZxAnCardSwSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 3),
    _ZxAnCardSwSlot_Type()
)
zxAnCardSwSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCardSwSlot.setStatus("current")
_ZxAnCardSwSubCard_Type = Integer32
_ZxAnCardSwSubCard_Object = MibTableColumn
zxAnCardSwSubCard = _ZxAnCardSwSubCard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 4),
    _ZxAnCardSwSubCard_Type()
)
zxAnCardSwSubCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCardSwSubCard.setStatus("current")


class _ZxAnCardRunningVerStorageDevType_Type(DisplayString):
    """Custom type zxAnCardRunningVerStorageDevType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnCardRunningVerStorageDevType_Type.__name__ = "DisplayString"
_ZxAnCardRunningVerStorageDevType_Object = MibTableColumn
zxAnCardRunningVerStorageDevType = _ZxAnCardRunningVerStorageDevType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 5),
    _ZxAnCardRunningVerStorageDevType_Type()
)
zxAnCardRunningVerStorageDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningVerStorageDevType.setStatus("current")
_ZxAnCardRunningVerStorageDevId_Type = Integer32
_ZxAnCardRunningVerStorageDevId_Object = MibTableColumn
zxAnCardRunningVerStorageDevId = _ZxAnCardRunningVerStorageDevId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 6),
    _ZxAnCardRunningVerStorageDevId_Type()
)
zxAnCardRunningVerStorageDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningVerStorageDevId.setStatus("current")


class _ZxAnCardRunningHwVersion_Type(DisplayString):
    """Custom type zxAnCardRunningHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningHwVersion_Type.__name__ = "DisplayString"
_ZxAnCardRunningHwVersion_Object = MibTableColumn
zxAnCardRunningHwVersion = _ZxAnCardRunningHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 7),
    _ZxAnCardRunningHwVersion_Type()
)
zxAnCardRunningHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningHwVersion.setStatus("current")


class _ZxAnCardRunningSwVersion_Type(DisplayString):
    """Custom type zxAnCardRunningSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwVersion_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwVersion_Object = MibTableColumn
zxAnCardRunningSwVersion = _ZxAnCardRunningSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 8),
    _ZxAnCardRunningSwVersion_Type()
)
zxAnCardRunningSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwVersion.setStatus("current")


class _ZxAnCardRunningSwVerFileName_Type(DisplayString):
    """Custom type zxAnCardRunningSwVerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwVerFileName_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwVerFileName_Object = MibTableColumn
zxAnCardRunningSwVerFileName = _ZxAnCardRunningSwVerFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 9),
    _ZxAnCardRunningSwVerFileName_Type()
)
zxAnCardRunningSwVerFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwVerFileName.setStatus("current")


class _ZxAnCardRunningSwVersionType_Type(DisplayString):
    """Custom type zxAnCardRunningSwVersionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwVersionType_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwVersionType_Object = MibTableColumn
zxAnCardRunningSwVersionType = _ZxAnCardRunningSwVersionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 10),
    _ZxAnCardRunningSwVersionType_Type()
)
zxAnCardRunningSwVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwVersionType.setStatus("current")
_ZxAnCardRunningSwVerFileSize_Type = Integer32
_ZxAnCardRunningSwVerFileSize_Object = MibTableColumn
zxAnCardRunningSwVerFileSize = _ZxAnCardRunningSwVerFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 11),
    _ZxAnCardRunningSwVerFileSize_Type()
)
zxAnCardRunningSwVerFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwVerFileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardRunningSwVerFileSize.setUnits("byte")


class _ZxAnCardRunningSwVerBuildTime_Type(DisplayString):
    """Custom type zxAnCardRunningSwVerBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnCardRunningSwVerBuildTime_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwVerBuildTime_Object = MibTableColumn
zxAnCardRunningSwVerBuildTime = _ZxAnCardRunningSwVerBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 12),
    _ZxAnCardRunningSwVerBuildTime_Type()
)
zxAnCardRunningSwVerBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwVerBuildTime.setStatus("current")


class _ZxAnCardRunningSwBootFileName_Type(DisplayString):
    """Custom type zxAnCardRunningSwBootFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwBootFileName_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwBootFileName_Object = MibTableColumn
zxAnCardRunningSwBootFileName = _ZxAnCardRunningSwBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 17),
    _ZxAnCardRunningSwBootFileName_Type()
)
zxAnCardRunningSwBootFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwBootFileName.setStatus("current")


class _ZxAnCardRunningSwBootVersionType_Type(DisplayString):
    """Custom type zxAnCardRunningSwBootVersionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwBootVersionType_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwBootVersionType_Object = MibTableColumn
zxAnCardRunningSwBootVersionType = _ZxAnCardRunningSwBootVersionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 18),
    _ZxAnCardRunningSwBootVersionType_Type()
)
zxAnCardRunningSwBootVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwBootVersionType.setStatus("current")


class _ZxAnCardRunningSwBootVersion_Type(DisplayString):
    """Custom type zxAnCardRunningSwBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwBootVersion_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwBootVersion_Object = MibTableColumn
zxAnCardRunningSwBootVersion = _ZxAnCardRunningSwBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 19),
    _ZxAnCardRunningSwBootVersion_Type()
)
zxAnCardRunningSwBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwBootVersion.setStatus("current")
_ZxAnCardRunningSwBootFileSize_Type = Integer32
_ZxAnCardRunningSwBootFileSize_Object = MibTableColumn
zxAnCardRunningSwBootFileSize = _ZxAnCardRunningSwBootFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 20),
    _ZxAnCardRunningSwBootFileSize_Type()
)
zxAnCardRunningSwBootFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwBootFileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardRunningSwBootFileSize.setUnits("byte")


class _ZxAnCardRunningSwBootBuildTime_Type(DisplayString):
    """Custom type zxAnCardRunningSwBootBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnCardRunningSwBootBuildTime_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwBootBuildTime_Object = MibTableColumn
zxAnCardRunningSwBootBuildTime = _ZxAnCardRunningSwBootBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 21),
    _ZxAnCardRunningSwBootBuildTime_Type()
)
zxAnCardRunningSwBootBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwBootBuildTime.setStatus("current")


class _ZxAnCardRunningSwFw1FileName_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw1FileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwFw1FileName_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw1FileName_Object = MibTableColumn
zxAnCardRunningSwFw1FileName = _ZxAnCardRunningSwFw1FileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 26),
    _ZxAnCardRunningSwFw1FileName_Type()
)
zxAnCardRunningSwFw1FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw1FileName.setStatus("current")


class _ZxAnCardRunningSwFw1VersionType_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw1VersionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwFw1VersionType_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw1VersionType_Object = MibTableColumn
zxAnCardRunningSwFw1VersionType = _ZxAnCardRunningSwFw1VersionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 27),
    _ZxAnCardRunningSwFw1VersionType_Type()
)
zxAnCardRunningSwFw1VersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw1VersionType.setStatus("current")


class _ZxAnCardRunningSwFw1Version_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw1Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwFw1Version_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw1Version_Object = MibTableColumn
zxAnCardRunningSwFw1Version = _ZxAnCardRunningSwFw1Version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 28),
    _ZxAnCardRunningSwFw1Version_Type()
)
zxAnCardRunningSwFw1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw1Version.setStatus("current")
_ZxAnCardRunningSwFw1FileSize_Type = Integer32
_ZxAnCardRunningSwFw1FileSize_Object = MibTableColumn
zxAnCardRunningSwFw1FileSize = _ZxAnCardRunningSwFw1FileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 29),
    _ZxAnCardRunningSwFw1FileSize_Type()
)
zxAnCardRunningSwFw1FileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw1FileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw1FileSize.setUnits("byte")


class _ZxAnCardRunningSwFw1BuildTime_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw1BuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnCardRunningSwFw1BuildTime_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw1BuildTime_Object = MibTableColumn
zxAnCardRunningSwFw1BuildTime = _ZxAnCardRunningSwFw1BuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 30),
    _ZxAnCardRunningSwFw1BuildTime_Type()
)
zxAnCardRunningSwFw1BuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw1BuildTime.setStatus("current")


class _ZxAnCardRunningSwFw2FileName_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw2FileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwFw2FileName_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw2FileName_Object = MibTableColumn
zxAnCardRunningSwFw2FileName = _ZxAnCardRunningSwFw2FileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 35),
    _ZxAnCardRunningSwFw2FileName_Type()
)
zxAnCardRunningSwFw2FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw2FileName.setStatus("current")


class _ZxAnCardRunningSwFw2VersionType_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw2VersionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwFw2VersionType_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw2VersionType_Object = MibTableColumn
zxAnCardRunningSwFw2VersionType = _ZxAnCardRunningSwFw2VersionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 36),
    _ZxAnCardRunningSwFw2VersionType_Type()
)
zxAnCardRunningSwFw2VersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw2VersionType.setStatus("current")


class _ZxAnCardRunningSwFw2Version_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw2Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwFw2Version_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw2Version_Object = MibTableColumn
zxAnCardRunningSwFw2Version = _ZxAnCardRunningSwFw2Version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 37),
    _ZxAnCardRunningSwFw2Version_Type()
)
zxAnCardRunningSwFw2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw2Version.setStatus("current")
_ZxAnCardRunningSwFw2FileSize_Type = Integer32
_ZxAnCardRunningSwFw2FileSize_Object = MibTableColumn
zxAnCardRunningSwFw2FileSize = _ZxAnCardRunningSwFw2FileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 38),
    _ZxAnCardRunningSwFw2FileSize_Type()
)
zxAnCardRunningSwFw2FileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw2FileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw2FileSize.setUnits("byte")


class _ZxAnCardRunningSwFw2BuildTime_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw2BuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnCardRunningSwFw2BuildTime_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw2BuildTime_Object = MibTableColumn
zxAnCardRunningSwFw2BuildTime = _ZxAnCardRunningSwFw2BuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 39),
    _ZxAnCardRunningSwFw2BuildTime_Type()
)
zxAnCardRunningSwFw2BuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw2BuildTime.setStatus("current")


class _ZxAnCardRunningSwFw3FileName_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw3FileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwFw3FileName_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw3FileName_Object = MibTableColumn
zxAnCardRunningSwFw3FileName = _ZxAnCardRunningSwFw3FileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 44),
    _ZxAnCardRunningSwFw3FileName_Type()
)
zxAnCardRunningSwFw3FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw3FileName.setStatus("current")


class _ZxAnCardRunningSwFw3VersionType_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw3VersionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwFw3VersionType_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw3VersionType_Object = MibTableColumn
zxAnCardRunningSwFw3VersionType = _ZxAnCardRunningSwFw3VersionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 45),
    _ZxAnCardRunningSwFw3VersionType_Type()
)
zxAnCardRunningSwFw3VersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw3VersionType.setStatus("current")


class _ZxAnCardRunningSwFw3Version_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw3Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardRunningSwFw3Version_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw3Version_Object = MibTableColumn
zxAnCardRunningSwFw3Version = _ZxAnCardRunningSwFw3Version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 46),
    _ZxAnCardRunningSwFw3Version_Type()
)
zxAnCardRunningSwFw3Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw3Version.setStatus("current")
_ZxAnCardRunningSwFw3FileSize_Type = Integer32
_ZxAnCardRunningSwFw3FileSize_Object = MibTableColumn
zxAnCardRunningSwFw3FileSize = _ZxAnCardRunningSwFw3FileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 47),
    _ZxAnCardRunningSwFw3FileSize_Type()
)
zxAnCardRunningSwFw3FileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw3FileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw3FileSize.setUnits("byte")


class _ZxAnCardRunningSwFw3BuildTime_Type(DisplayString):
    """Custom type zxAnCardRunningSwFw3BuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnCardRunningSwFw3BuildTime_Type.__name__ = "DisplayString"
_ZxAnCardRunningSwFw3BuildTime_Object = MibTableColumn
zxAnCardRunningSwFw3BuildTime = _ZxAnCardRunningSwFw3BuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 3, 1, 48),
    _ZxAnCardRunningSwFw3BuildTime_Type()
)
zxAnCardRunningSwFw3BuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardRunningSwFw3BuildTime.setStatus("current")
_ZxAnSoftwarePatchTable_Object = MibTable
zxAnSoftwarePatchTable = _ZxAnSoftwarePatchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4)
)
if mibBuilder.loadTexts:
    zxAnSoftwarePatchTable.setStatus("current")
_ZxAnSoftwarePatchEntry_Object = MibTableRow
zxAnSoftwarePatchEntry = _ZxAnSoftwarePatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1)
)
zxAnSoftwarePatchEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevRack"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevShelf"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSlot"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSubCard"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevType"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevId"),
    (0, "ZTE-AN-FILE-MIB", "zxAnSwPatchName"),
)
if mibBuilder.loadTexts:
    zxAnSoftwarePatchEntry.setStatus("current")


class _ZxAnSwPatchName_Type(DisplayString):
    """Custom type zxAnSwPatchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwPatchName_Type.__name__ = "DisplayString"
_ZxAnSwPatchName_Object = MibTableColumn
zxAnSwPatchName = _ZxAnSwPatchName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1, 1),
    _ZxAnSwPatchName_Type()
)
zxAnSwPatchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwPatchName.setStatus("current")


class _ZxAnSwPatchOwnerSwVersion_Type(DisplayString):
    """Custom type zxAnSwPatchOwnerSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnSwPatchOwnerSwVersion_Type.__name__ = "DisplayString"
_ZxAnSwPatchOwnerSwVersion_Object = MibTableColumn
zxAnSwPatchOwnerSwVersion = _ZxAnSwPatchOwnerSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1, 2),
    _ZxAnSwPatchOwnerSwVersion_Type()
)
zxAnSwPatchOwnerSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchOwnerSwVersion.setStatus("current")


class _ZxAnSwPatchVersion_Type(DisplayString):
    """Custom type zxAnSwPatchVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnSwPatchVersion_Type.__name__ = "DisplayString"
_ZxAnSwPatchVersion_Object = MibTableColumn
zxAnSwPatchVersion = _ZxAnSwPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1, 3),
    _ZxAnSwPatchVersion_Type()
)
zxAnSwPatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchVersion.setStatus("current")
_ZxAnSwPatchSize_Type = Integer32
_ZxAnSwPatchSize_Object = MibTableColumn
zxAnSwPatchSize = _ZxAnSwPatchSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1, 4),
    _ZxAnSwPatchSize_Type()
)
zxAnSwPatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwPatchSize.setUnits("byte")


class _ZxAnSwPatchBuildTime_Type(DisplayString):
    """Custom type zxAnSwPatchBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSwPatchBuildTime_Type.__name__ = "DisplayString"
_ZxAnSwPatchBuildTime_Object = MibTableColumn
zxAnSwPatchBuildTime = _ZxAnSwPatchBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1, 5),
    _ZxAnSwPatchBuildTime_Type()
)
zxAnSwPatchBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchBuildTime.setStatus("current")


class _ZxAnSwPatchDesc_Type(DisplayString):
    """Custom type zxAnSwPatchDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnSwPatchDesc_Type.__name__ = "DisplayString"
_ZxAnSwPatchDesc_Object = MibTableColumn
zxAnSwPatchDesc = _ZxAnSwPatchDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1, 6),
    _ZxAnSwPatchDesc_Type()
)
zxAnSwPatchDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchDesc.setStatus("current")


class _ZxAnSwPatchAdminStatus_Type(Integer32):
    """Custom type zxAnSwPatchAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2),
          ("temporarilyactivate", 3))
    )


_ZxAnSwPatchAdminStatus_Type.__name__ = "Integer32"
_ZxAnSwPatchAdminStatus_Object = MibTableColumn
zxAnSwPatchAdminStatus = _ZxAnSwPatchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1, 7),
    _ZxAnSwPatchAdminStatus_Type()
)
zxAnSwPatchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwPatchAdminStatus.setStatus("current")


class _ZxAnSwPatchActiveStatus_Type(Integer32):
    """Custom type zxAnSwPatchActiveStatus based on Integer32"""
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
        *(("inactive", 1),
          ("activating", 2),
          ("partialActivated", 3),
          ("activated", 4),
          ("activeFailed", 5))
    )


_ZxAnSwPatchActiveStatus_Type.__name__ = "Integer32"
_ZxAnSwPatchActiveStatus_Object = MibTableColumn
zxAnSwPatchActiveStatus = _ZxAnSwPatchActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1, 8),
    _ZxAnSwPatchActiveStatus_Type()
)
zxAnSwPatchActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchActiveStatus.setStatus("current")


class _ZxAnSwPatchOperFailedReason_Type(Integer32):
    """Custom type zxAnSwPatchOperFailedReason based on Integer32"""
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
          ("invalidPatchName", 2),
          ("patchTooBig", 3),
          ("patchCheckFailed", 4),
          ("timeout", 5),
          ("otherOperationInProgress", 6),
          ("versionMismatch", 7),
          ("alreadyInactive", 8),
          ("alreadyActivated", 9),
          ("otherErrors", 255))
    )


_ZxAnSwPatchOperFailedReason_Type.__name__ = "Integer32"
_ZxAnSwPatchOperFailedReason_Object = MibTableColumn
zxAnSwPatchOperFailedReason = _ZxAnSwPatchOperFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 4, 1, 9),
    _ZxAnSwPatchOperFailedReason_Type()
)
zxAnSwPatchOperFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchOperFailedReason.setStatus("current")
_ZxAnSoftwareRunningPatchTable_Object = MibTable
zxAnSoftwareRunningPatchTable = _ZxAnSoftwareRunningPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 5)
)
if mibBuilder.loadTexts:
    zxAnSoftwareRunningPatchTable.setStatus("current")
_ZxAnSoftwareRunningPatchEntry_Object = MibTableRow
zxAnSoftwareRunningPatchEntry = _ZxAnSoftwareRunningPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 5, 1)
)
zxAnSoftwareRunningPatchEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevRack"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevShelf"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSlot"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevSubCard"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevType"),
    (0, "ZTE-AN-FILE-MIB", "zxAnFileStorageDevId"),
    (0, "ZTE-AN-FILE-MIB", "zxAnRunningPatchName"),
)
if mibBuilder.loadTexts:
    zxAnSoftwareRunningPatchEntry.setStatus("current")


class _ZxAnRunningPatchName_Type(DisplayString):
    """Custom type zxAnRunningPatchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnRunningPatchName_Type.__name__ = "DisplayString"
_ZxAnRunningPatchName_Object = MibTableColumn
zxAnRunningPatchName = _ZxAnRunningPatchName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 5, 1, 1),
    _ZxAnRunningPatchName_Type()
)
zxAnRunningPatchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRunningPatchName.setStatus("current")


class _ZxAnRunningPatchOwnerSwVersion_Type(DisplayString):
    """Custom type zxAnRunningPatchOwnerSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnRunningPatchOwnerSwVersion_Type.__name__ = "DisplayString"
_ZxAnRunningPatchOwnerSwVersion_Object = MibTableColumn
zxAnRunningPatchOwnerSwVersion = _ZxAnRunningPatchOwnerSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 5, 1, 2),
    _ZxAnRunningPatchOwnerSwVersion_Type()
)
zxAnRunningPatchOwnerSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRunningPatchOwnerSwVersion.setStatus("current")


class _ZxAnRunningPatchVersion_Type(DisplayString):
    """Custom type zxAnRunningPatchVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnRunningPatchVersion_Type.__name__ = "DisplayString"
_ZxAnRunningPatchVersion_Object = MibTableColumn
zxAnRunningPatchVersion = _ZxAnRunningPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 5, 1, 3),
    _ZxAnRunningPatchVersion_Type()
)
zxAnRunningPatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRunningPatchVersion.setStatus("current")
_ZxAnRunningPatchSize_Type = Integer32
_ZxAnRunningPatchSize_Object = MibTableColumn
zxAnRunningPatchSize = _ZxAnRunningPatchSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 5, 1, 4),
    _ZxAnRunningPatchSize_Type()
)
zxAnRunningPatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRunningPatchSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnRunningPatchSize.setUnits("byte")


class _ZxAnRunningPatchBuildTime_Type(DisplayString):
    """Custom type zxAnRunningPatchBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnRunningPatchBuildTime_Type.__name__ = "DisplayString"
_ZxAnRunningPatchBuildTime_Object = MibTableColumn
zxAnRunningPatchBuildTime = _ZxAnRunningPatchBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 5, 1, 5),
    _ZxAnRunningPatchBuildTime_Type()
)
zxAnRunningPatchBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRunningPatchBuildTime.setStatus("current")


class _ZxAnRunningPatchActivatedTime_Type(DisplayString):
    """Custom type zxAnRunningPatchActivatedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnRunningPatchActivatedTime_Type.__name__ = "DisplayString"
_ZxAnRunningPatchActivatedTime_Object = MibTableColumn
zxAnRunningPatchActivatedTime = _ZxAnRunningPatchActivatedTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 5, 1, 6),
    _ZxAnRunningPatchActivatedTime_Type()
)
zxAnRunningPatchActivatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRunningPatchActivatedTime.setStatus("current")


class _ZxAnRunningPatchDesc_Type(DisplayString):
    """Custom type zxAnRunningPatchDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnRunningPatchDesc_Type.__name__ = "DisplayString"
_ZxAnRunningPatchDesc_Object = MibTableColumn
zxAnRunningPatchDesc = _ZxAnRunningPatchDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 5, 1, 7),
    _ZxAnRunningPatchDesc_Type()
)
zxAnRunningPatchDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRunningPatchDesc.setStatus("current")
_ZxAnCardUpdateObjects_ObjectIdentity = ObjectIdentity
zxAnCardUpdateObjects = _ZxAnCardUpdateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 6)
)
_ZxAnCardUpdateGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnCardUpdateGlobalObjects = _ZxAnCardUpdateGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 6, 1)
)
_ZxAnCardBootSoftwareUpdate_Type = ObjectIdentifier
_ZxAnCardBootSoftwareUpdate_Object = MibScalar
zxAnCardBootSoftwareUpdate = _ZxAnCardBootSoftwareUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 6, 1, 1),
    _ZxAnCardBootSoftwareUpdate_Type()
)
zxAnCardBootSoftwareUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCardBootSoftwareUpdate.setStatus("current")
_ZxAnCardSwUpdateStatusTable_Object = MibTable
zxAnCardSwUpdateStatusTable = _ZxAnCardSwUpdateStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 6, 2)
)
if mibBuilder.loadTexts:
    zxAnCardSwUpdateStatusTable.setStatus("current")
_ZxAnCardSwUpdateStatusEntry_Object = MibTableRow
zxAnCardSwUpdateStatusEntry = _ZxAnCardSwUpdateStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 6, 2, 1)
)
zxAnCardSwUpdateStatusEntry.setIndexNames(
    (0, "ZTE-AN-FILE-MIB", "zxAnCardSwRack"),
    (0, "ZTE-AN-FILE-MIB", "zxAnCardSwShelf"),
    (0, "ZTE-AN-FILE-MIB", "zxAnCardSwSlot"),
    (0, "ZTE-AN-FILE-MIB", "zxAnCardSwSubCard"),
)
if mibBuilder.loadTexts:
    zxAnCardSwUpdateStatusEntry.setStatus("current")


class _ZxAnCardSoftwareUpdateStatus_Type(Integer32):
    """Custom type zxAnCardSoftwareUpdateStatus based on Integer32"""
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
          ("processing", 2),
          ("failed", 3),
          ("success", 4))
    )


_ZxAnCardSoftwareUpdateStatus_Type.__name__ = "Integer32"
_ZxAnCardSoftwareUpdateStatus_Object = MibTableColumn
zxAnCardSoftwareUpdateStatus = _ZxAnCardSoftwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 6, 2, 1, 1),
    _ZxAnCardSoftwareUpdateStatus_Type()
)
zxAnCardSoftwareUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardSoftwareUpdateStatus.setStatus("current")


class _ZxAnCardSoftwareUpdateProgress_Type(Integer32):
    """Custom type zxAnCardSoftwareUpdateProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnCardSoftwareUpdateProgress_Type.__name__ = "Integer32"
_ZxAnCardSoftwareUpdateProgress_Object = MibTableColumn
zxAnCardSoftwareUpdateProgress = _ZxAnCardSoftwareUpdateProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 6, 2, 1, 2),
    _ZxAnCardSoftwareUpdateProgress_Type()
)
zxAnCardSoftwareUpdateProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardSoftwareUpdateProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardSoftwareUpdateProgress.setUnits("%")


class _ZxAnCardSwUpdateFailedReason_Type(DisplayString):
    """Custom type zxAnCardSwUpdateFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnCardSwUpdateFailedReason_Type.__name__ = "DisplayString"
_ZxAnCardSwUpdateFailedReason_Object = MibTableColumn
zxAnCardSwUpdateFailedReason = _ZxAnCardSwUpdateFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 6, 2, 1, 3),
    _ZxAnCardSwUpdateFailedReason_Type()
)
zxAnCardSwUpdateFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardSwUpdateFailedReason.setStatus("current")
_ZxAnSwAutoUpdateMgmt_ObjectIdentity = ObjectIdentity
zxAnSwAutoUpdateMgmt = _ZxAnSwAutoUpdateMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7)
)
_ZxAnSwAutoUpdateChkGroup_ObjectIdentity = ObjectIdentity
zxAnSwAutoUpdateChkGroup = _ZxAnSwAutoUpdateChkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 1)
)


class _ZxAnSwAutoUpdateChkEnable_Type(Integer32):
    """Custom type zxAnSwAutoUpdateChkEnable based on Integer32"""
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


_ZxAnSwAutoUpdateChkEnable_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateChkEnable_Object = MibScalar
zxAnSwAutoUpdateChkEnable = _ZxAnSwAutoUpdateChkEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 1, 1),
    _ZxAnSwAutoUpdateChkEnable_Type()
)
zxAnSwAutoUpdateChkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkEnable.setStatus("current")


class _ZxAnSwAutoUpdateChkStartTime_Type(DisplayString):
    """Custom type zxAnSwAutoUpdateChkStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ZxAnSwAutoUpdateChkStartTime_Type.__name__ = "DisplayString"
_ZxAnSwAutoUpdateChkStartTime_Object = MibScalar
zxAnSwAutoUpdateChkStartTime = _ZxAnSwAutoUpdateChkStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 1, 2),
    _ZxAnSwAutoUpdateChkStartTime_Type()
)
zxAnSwAutoUpdateChkStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkStartTime.setStatus("current")


class _ZxAnSwAutoUpdateChkInterval_Type(Integer32):
    """Custom type zxAnSwAutoUpdateChkInterval based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8760),
    )


_ZxAnSwAutoUpdateChkInterval_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateChkInterval_Object = MibScalar
zxAnSwAutoUpdateChkInterval = _ZxAnSwAutoUpdateChkInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 1, 3),
    _ZxAnSwAutoUpdateChkInterval_Type()
)
zxAnSwAutoUpdateChkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkInterval.setUnits("hours")


class _ZxAnSwAutoUpdateCurrChkStartTime_Type(DisplayString):
    """Custom type zxAnSwAutoUpdateCurrChkStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ZxAnSwAutoUpdateCurrChkStartTime_Type.__name__ = "DisplayString"
_ZxAnSwAutoUpdateCurrChkStartTime_Object = MibScalar
zxAnSwAutoUpdateCurrChkStartTime = _ZxAnSwAutoUpdateCurrChkStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 1, 4),
    _ZxAnSwAutoUpdateCurrChkStartTime_Type()
)
zxAnSwAutoUpdateCurrChkStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrChkStartTime.setStatus("current")


class _ZxAnSwAutoUpdateChkDifferFiles_Type(DisplayString):
    """Custom type zxAnSwAutoUpdateChkDifferFiles based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnSwAutoUpdateChkDifferFiles_Type.__name__ = "DisplayString"
_ZxAnSwAutoUpdateChkDifferFiles_Object = MibScalar
zxAnSwAutoUpdateChkDifferFiles = _ZxAnSwAutoUpdateChkDifferFiles_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 1, 5),
    _ZxAnSwAutoUpdateChkDifferFiles_Type()
)
zxAnSwAutoUpdateChkDifferFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkDifferFiles.setStatus("current")


class _ZxAnSwAutoUpdateChkStatus_Type(Integer32):
    """Custom type zxAnSwAutoUpdateChkStatus based on Integer32"""
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


_ZxAnSwAutoUpdateChkStatus_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateChkStatus_Object = MibScalar
zxAnSwAutoUpdateChkStatus = _ZxAnSwAutoUpdateChkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 1, 6),
    _ZxAnSwAutoUpdateChkStatus_Type()
)
zxAnSwAutoUpdateChkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkStatus.setStatus("current")


class _ZxAnSwAutoUpdateChkFailedReason_Type(Integer32):
    """Custom type zxAnSwAutoUpdateChkFailedReason based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("fileServerUnconfigured", 2),
          ("fileServerConnectFailed", 3),
          ("fileServerLoginFailed", 4),
          ("fileServerPathError", 5),
          ("fileServerProtocolTypeError", 6),
          ("deviceCheckFailed", 7),
          ("otherErrors", 255))
    )


_ZxAnSwAutoUpdateChkFailedReason_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateChkFailedReason_Object = MibScalar
zxAnSwAutoUpdateChkFailedReason = _ZxAnSwAutoUpdateChkFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 1, 7),
    _ZxAnSwAutoUpdateChkFailedReason_Type()
)
zxAnSwAutoUpdateChkFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkFailedReason.setStatus("current")
_ZxAnSwAutoUpdateGroup_ObjectIdentity = ObjectIdentity
zxAnSwAutoUpdateGroup = _ZxAnSwAutoUpdateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2)
)


class _ZxAnSwAutoUpdateAction_Type(Integer32):
    """Custom type zxAnSwAutoUpdateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_ZxAnSwAutoUpdateAction_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateAction_Object = MibScalar
zxAnSwAutoUpdateAction = _ZxAnSwAutoUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 1),
    _ZxAnSwAutoUpdateAction_Type()
)
zxAnSwAutoUpdateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateAction.setStatus("current")


class _ZxAnSwAutoUpdateActiveEnable_Type(Integer32):
    """Custom type zxAnSwAutoUpdateActiveEnable based on Integer32"""
    defaultValue = 1

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


_ZxAnSwAutoUpdateActiveEnable_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateActiveEnable_Object = MibScalar
zxAnSwAutoUpdateActiveEnable = _ZxAnSwAutoUpdateActiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 2),
    _ZxAnSwAutoUpdateActiveEnable_Type()
)
zxAnSwAutoUpdateActiveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateActiveEnable.setStatus("current")


class _ZxAnSwAutoUpdateVerBackupEnable_Type(Integer32):
    """Custom type zxAnSwAutoUpdateVerBackupEnable based on Integer32"""
    defaultValue = 1

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


_ZxAnSwAutoUpdateVerBackupEnable_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateVerBackupEnable_Object = MibScalar
zxAnSwAutoUpdateVerBackupEnable = _ZxAnSwAutoUpdateVerBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 3),
    _ZxAnSwAutoUpdateVerBackupEnable_Type()
)
zxAnSwAutoUpdateVerBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateVerBackupEnable.setStatus("current")


class _ZxAnSwAutoUpdateStatus_Type(Integer32):
    """Custom type zxAnSwAutoUpdateStatus based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 1),
          ("updateStarting", 2),
          ("backingUpFile", 3),
          ("versionFileAnalyzing", 4),
          ("versionFileDownloading", 5),
          ("versionFileDownloadComplete", 6),
          ("masterSlaveSynchronizing", 7),
          ("masterSlaveSyncComplete", 8),
          ("versionFileLoading", 9),
          ("bootUpdating", 10),
          ("bootUpdateComplete", 11),
          ("updateSuccess", 12),
          ("readyToReboot", 13),
          ("sameVersion", 14),
          ("updateFailed", 255))
    )


_ZxAnSwAutoUpdateStatus_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateStatus_Object = MibScalar
zxAnSwAutoUpdateStatus = _ZxAnSwAutoUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 4),
    _ZxAnSwAutoUpdateStatus_Type()
)
zxAnSwAutoUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateStatus.setStatus("current")


class _ZxAnSwAutoUpdateCurrFileName_Type(DisplayString):
    """Custom type zxAnSwAutoUpdateCurrFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwAutoUpdateCurrFileName_Type.__name__ = "DisplayString"
_ZxAnSwAutoUpdateCurrFileName_Object = MibScalar
zxAnSwAutoUpdateCurrFileName = _ZxAnSwAutoUpdateCurrFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 5),
    _ZxAnSwAutoUpdateCurrFileName_Type()
)
zxAnSwAutoUpdateCurrFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileName.setStatus("current")
_ZxAnSwAutoUpdateCurrFileSize_Type = Integer32
_ZxAnSwAutoUpdateCurrFileSize_Object = MibScalar
zxAnSwAutoUpdateCurrFileSize = _ZxAnSwAutoUpdateCurrFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 6),
    _ZxAnSwAutoUpdateCurrFileSize_Type()
)
zxAnSwAutoUpdateCurrFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileSize.setUnits("bytes")


class _ZxAnSwAutoUpdateCurrFileProgress_Type(Integer32):
    """Custom type zxAnSwAutoUpdateCurrFileProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSwAutoUpdateCurrFileProgress_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateCurrFileProgress_Object = MibScalar
zxAnSwAutoUpdateCurrFileProgress = _ZxAnSwAutoUpdateCurrFileProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 7),
    _ZxAnSwAutoUpdateCurrFileProgress_Type()
)
zxAnSwAutoUpdateCurrFileProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileProgress.setUnits("percent")
_ZxAnSwAutoUpdateTotalFiles_Type = Integer32
_ZxAnSwAutoUpdateTotalFiles_Object = MibScalar
zxAnSwAutoUpdateTotalFiles = _ZxAnSwAutoUpdateTotalFiles_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 8),
    _ZxAnSwAutoUpdateTotalFiles_Type()
)
zxAnSwAutoUpdateTotalFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateTotalFiles.setStatus("current")
_ZxAnSwAutoUpdateSuccessFiles_Type = Integer32
_ZxAnSwAutoUpdateSuccessFiles_Object = MibScalar
zxAnSwAutoUpdateSuccessFiles = _ZxAnSwAutoUpdateSuccessFiles_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 9),
    _ZxAnSwAutoUpdateSuccessFiles_Type()
)
zxAnSwAutoUpdateSuccessFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateSuccessFiles.setStatus("current")


class _ZxAnSwAutoUpdateFailedReason_Type(Integer32):
    """Custom type zxAnSwAutoUpdateFailedReason based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("backupDataError", 2),
          ("backupLogError", 3),
          ("backupConfigurationError", 4),
          ("backupVersionFileError", 5),
          ("backupOtherError", 6),
          ("analyzingConfigurationError", 7),
          ("analyzingVersionFileError", 8),
          ("diskFull", 9),
          ("downloadingVersionFileError", 10),
          ("updateVersionFileError", 11),
          ("updateBootError", 12),
          ("masterSlaveSynchronizeError", 13),
          ("updateConflict", 14),
          ("unavailableServer", 15),
          ("slaveCardNotInService", 16),
          ("otherErrors", 255))
    )


_ZxAnSwAutoUpdateFailedReason_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateFailedReason_Object = MibScalar
zxAnSwAutoUpdateFailedReason = _ZxAnSwAutoUpdateFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 2, 50, 7, 2, 10),
    _ZxAnSwAutoUpdateFailedReason_Type()
)
zxAnSwAutoUpdateFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateFailedReason.setStatus("current")
_ZxAnFileTrapObjects_ObjectIdentity = ObjectIdentity
zxAnFileTrapObjects = _ZxAnFileTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 10)
)
_ZxAnSwUpdateTrapGroup_ObjectIdentity = ObjectIdentity
zxAnSwUpdateTrapGroup = _ZxAnSwUpdateTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 10, 2)
)

# Managed Objects groups


# Notification objects

zxAnSwAutoUpdateFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 10, 2, 1)
)
zxAnSwAutoUpdateFinished.setObjects(
      *(("ZTE-AN-FILE-MIB", "zxAnSwAutoUpdateStatus"),
        ("ZTE-AN-FILE-MIB", "zxAnSwAutoUpdateFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateFinished.setStatus(
        "current"
    )

zxAnSwAutoUpdateVersionDiffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 10, 2, 2)
)
zxAnSwAutoUpdateVersionDiffer.setObjects(
      *(("ZTE-AN-FILE-MIB", "zxAnSwAutoUpdateCurrChkStartTime"),
        ("ZTE-AN-FILE-MIB", "zxAnSwAutoUpdateChkDifferFiles"))
)
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateVersionDiffer.setStatus(
        "current"
    )

zxAnSwAutoUpdateVersionChkFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 14, 10, 2, 3)
)
zxAnSwAutoUpdateVersionChkFailed.setObjects(
      *(("ZTE-AN-FILE-MIB", "zxAnSwAutoUpdateCurrChkStartTime"),
        ("ZTE-AN-FILE-MIB", "zxAnSwAutoUpdateChkFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateVersionChkFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-FILE-MIB",
    **{"zxAnFileMib": zxAnFileMib,
       "zxAnFileStorageDevMgmt": zxAnFileStorageDevMgmt,
       "zxAnFileStorageDevTable": zxAnFileStorageDevTable,
       "zxAnFileStorageDevEntry": zxAnFileStorageDevEntry,
       "zxAnFileStorageDevRack": zxAnFileStorageDevRack,
       "zxAnFileStorageDevShelf": zxAnFileStorageDevShelf,
       "zxAnFileStorageDevSlot": zxAnFileStorageDevSlot,
       "zxAnFileStorageDevSubCard": zxAnFileStorageDevSubCard,
       "zxAnFileStorageDevType": zxAnFileStorageDevType,
       "zxAnFileStorageDevId": zxAnFileStorageDevId,
       "zxAnFileStorageDevTotalSpace": zxAnFileStorageDevTotalSpace,
       "zxAnFileStorageDevAvailableSpace": zxAnFileStorageDevAvailableSpace,
       "zxAnFileStorageDevOperStatus": zxAnFileStorageDevOperStatus,
       "zxAnFileStorageDevAdminStatus": zxAnFileStorageDevAdminStatus,
       "zxAnStartupSeqTable": zxAnStartupSeqTable,
       "zxAnStartupSeqEntry": zxAnStartupSeqEntry,
       "zxAnStartupSeqIndex": zxAnStartupSeqIndex,
       "zxAnStartupSeqRack": zxAnStartupSeqRack,
       "zxAnStartupSeqShelf": zxAnStartupSeqShelf,
       "zxAnStartupSeqSlot": zxAnStartupSeqSlot,
       "zxAnStartupSeqSubCard": zxAnStartupSeqSubCard,
       "zxAnStartupSeqDevType": zxAnStartupSeqDevType,
       "zxAnStartupSeqDevId": zxAnStartupSeqDevId,
       "zxAnFileMgmt": zxAnFileMgmt,
       "zxAnFileTable": zxAnFileTable,
       "zxAnFileEntry": zxAnFileEntry,
       "zxAnFileName": zxAnFileName,
       "zxAnFileType": zxAnFileType,
       "zxAnFileSize": zxAnFileSize,
       "zxAnFileModifyTime": zxAnFileModifyTime,
       "zxAnFilePermissions": zxAnFilePermissions,
       "zxAnDirOwner": zxAnDirOwner,
       "zxAnDirTotalFilesCount": zxAnDirTotalFilesCount,
       "zxAnFileAdminStatus": zxAnFileAdminStatus,
       "zxAnFileCopyMgmt": zxAnFileCopyMgmt,
       "zxAnFileCopySrcFileSpecific": zxAnFileCopySrcFileSpecific,
       "zxAnFileCopyDestDirSpecific": zxAnFileCopyDestDirSpecific,
       "zxAnFileCopyCancel": zxAnFileCopyCancel,
       "zxAnFileCopyStatusTable": zxAnFileCopyStatusTable,
       "zxAnFileCopyStatusEntry": zxAnFileCopyStatusEntry,
       "zxAnCopyFileName": zxAnCopyFileName,
       "zxAnFileCopyStatus": zxAnFileCopyStatus,
       "zxAnFileCopyProgress": zxAnFileCopyProgress,
       "zxAnFileCopyFailedReason": zxAnFileCopyFailedReason,
       "zxAnFileSynchMgmt": zxAnFileSynchMgmt,
       "zxAnFileSyncStatusTable": zxAnFileSyncStatusTable,
       "zxAnFileSyncStatusEntry": zxAnFileSyncStatusEntry,
       "zxAnFileSyncFileName": zxAnFileSyncFileName,
       "zxAnFileSyncStatus": zxAnFileSyncStatus,
       "zxAnFileSyncProgress": zxAnFileSyncProgress,
       "zxAnFileSyncFailedReason": zxAnFileSyncFailedReason,
       "zxAnSoftwareMgmt": zxAnSoftwareMgmt,
       "zxAnSoftwareVersionTable": zxAnSoftwareVersionTable,
       "zxAnSoftwareVersionEntry": zxAnSoftwareVersionEntry,
       "zxAnSwVersionFileName": zxAnSwVersionFileName,
       "zxAnSwVersionType": zxAnSwVersionType,
       "zxAnSwVersion": zxAnSwVersion,
       "zxAnSwVersionFileSize": zxAnSwVersionFileSize,
       "zxAnSwVersionBuildTime": zxAnSwVersionBuildTime,
       "zxAnSwVersionActiveStatus": zxAnSwVersionActiveStatus,
       "zxAnSwVersionAdminStatus": zxAnSwVersionAdminStatus,
       "zxAnSwVersionActivatedTime": zxAnSwVersionActivatedTime,
       "zxAnCardRunningVersionTable": zxAnCardRunningVersionTable,
       "zxAnCardRunningVersionEntry": zxAnCardRunningVersionEntry,
       "zxAnCardSwRack": zxAnCardSwRack,
       "zxAnCardSwShelf": zxAnCardSwShelf,
       "zxAnCardSwSlot": zxAnCardSwSlot,
       "zxAnCardSwSubCard": zxAnCardSwSubCard,
       "zxAnCardRunningVerStorageDevType": zxAnCardRunningVerStorageDevType,
       "zxAnCardRunningVerStorageDevId": zxAnCardRunningVerStorageDevId,
       "zxAnCardRunningHwVersion": zxAnCardRunningHwVersion,
       "zxAnCardRunningSwVersion": zxAnCardRunningSwVersion,
       "zxAnCardRunningSwVerFileName": zxAnCardRunningSwVerFileName,
       "zxAnCardRunningSwVersionType": zxAnCardRunningSwVersionType,
       "zxAnCardRunningSwVerFileSize": zxAnCardRunningSwVerFileSize,
       "zxAnCardRunningSwVerBuildTime": zxAnCardRunningSwVerBuildTime,
       "zxAnCardRunningSwBootFileName": zxAnCardRunningSwBootFileName,
       "zxAnCardRunningSwBootVersionType": zxAnCardRunningSwBootVersionType,
       "zxAnCardRunningSwBootVersion": zxAnCardRunningSwBootVersion,
       "zxAnCardRunningSwBootFileSize": zxAnCardRunningSwBootFileSize,
       "zxAnCardRunningSwBootBuildTime": zxAnCardRunningSwBootBuildTime,
       "zxAnCardRunningSwFw1FileName": zxAnCardRunningSwFw1FileName,
       "zxAnCardRunningSwFw1VersionType": zxAnCardRunningSwFw1VersionType,
       "zxAnCardRunningSwFw1Version": zxAnCardRunningSwFw1Version,
       "zxAnCardRunningSwFw1FileSize": zxAnCardRunningSwFw1FileSize,
       "zxAnCardRunningSwFw1BuildTime": zxAnCardRunningSwFw1BuildTime,
       "zxAnCardRunningSwFw2FileName": zxAnCardRunningSwFw2FileName,
       "zxAnCardRunningSwFw2VersionType": zxAnCardRunningSwFw2VersionType,
       "zxAnCardRunningSwFw2Version": zxAnCardRunningSwFw2Version,
       "zxAnCardRunningSwFw2FileSize": zxAnCardRunningSwFw2FileSize,
       "zxAnCardRunningSwFw2BuildTime": zxAnCardRunningSwFw2BuildTime,
       "zxAnCardRunningSwFw3FileName": zxAnCardRunningSwFw3FileName,
       "zxAnCardRunningSwFw3VersionType": zxAnCardRunningSwFw3VersionType,
       "zxAnCardRunningSwFw3Version": zxAnCardRunningSwFw3Version,
       "zxAnCardRunningSwFw3FileSize": zxAnCardRunningSwFw3FileSize,
       "zxAnCardRunningSwFw3BuildTime": zxAnCardRunningSwFw3BuildTime,
       "zxAnSoftwarePatchTable": zxAnSoftwarePatchTable,
       "zxAnSoftwarePatchEntry": zxAnSoftwarePatchEntry,
       "zxAnSwPatchName": zxAnSwPatchName,
       "zxAnSwPatchOwnerSwVersion": zxAnSwPatchOwnerSwVersion,
       "zxAnSwPatchVersion": zxAnSwPatchVersion,
       "zxAnSwPatchSize": zxAnSwPatchSize,
       "zxAnSwPatchBuildTime": zxAnSwPatchBuildTime,
       "zxAnSwPatchDesc": zxAnSwPatchDesc,
       "zxAnSwPatchAdminStatus": zxAnSwPatchAdminStatus,
       "zxAnSwPatchActiveStatus": zxAnSwPatchActiveStatus,
       "zxAnSwPatchOperFailedReason": zxAnSwPatchOperFailedReason,
       "zxAnSoftwareRunningPatchTable": zxAnSoftwareRunningPatchTable,
       "zxAnSoftwareRunningPatchEntry": zxAnSoftwareRunningPatchEntry,
       "zxAnRunningPatchName": zxAnRunningPatchName,
       "zxAnRunningPatchOwnerSwVersion": zxAnRunningPatchOwnerSwVersion,
       "zxAnRunningPatchVersion": zxAnRunningPatchVersion,
       "zxAnRunningPatchSize": zxAnRunningPatchSize,
       "zxAnRunningPatchBuildTime": zxAnRunningPatchBuildTime,
       "zxAnRunningPatchActivatedTime": zxAnRunningPatchActivatedTime,
       "zxAnRunningPatchDesc": zxAnRunningPatchDesc,
       "zxAnCardUpdateObjects": zxAnCardUpdateObjects,
       "zxAnCardUpdateGlobalObjects": zxAnCardUpdateGlobalObjects,
       "zxAnCardBootSoftwareUpdate": zxAnCardBootSoftwareUpdate,
       "zxAnCardSwUpdateStatusTable": zxAnCardSwUpdateStatusTable,
       "zxAnCardSwUpdateStatusEntry": zxAnCardSwUpdateStatusEntry,
       "zxAnCardSoftwareUpdateStatus": zxAnCardSoftwareUpdateStatus,
       "zxAnCardSoftwareUpdateProgress": zxAnCardSoftwareUpdateProgress,
       "zxAnCardSwUpdateFailedReason": zxAnCardSwUpdateFailedReason,
       "zxAnSwAutoUpdateMgmt": zxAnSwAutoUpdateMgmt,
       "zxAnSwAutoUpdateChkGroup": zxAnSwAutoUpdateChkGroup,
       "zxAnSwAutoUpdateChkEnable": zxAnSwAutoUpdateChkEnable,
       "zxAnSwAutoUpdateChkStartTime": zxAnSwAutoUpdateChkStartTime,
       "zxAnSwAutoUpdateChkInterval": zxAnSwAutoUpdateChkInterval,
       "zxAnSwAutoUpdateCurrChkStartTime": zxAnSwAutoUpdateCurrChkStartTime,
       "zxAnSwAutoUpdateChkDifferFiles": zxAnSwAutoUpdateChkDifferFiles,
       "zxAnSwAutoUpdateChkStatus": zxAnSwAutoUpdateChkStatus,
       "zxAnSwAutoUpdateChkFailedReason": zxAnSwAutoUpdateChkFailedReason,
       "zxAnSwAutoUpdateGroup": zxAnSwAutoUpdateGroup,
       "zxAnSwAutoUpdateAction": zxAnSwAutoUpdateAction,
       "zxAnSwAutoUpdateActiveEnable": zxAnSwAutoUpdateActiveEnable,
       "zxAnSwAutoUpdateVerBackupEnable": zxAnSwAutoUpdateVerBackupEnable,
       "zxAnSwAutoUpdateStatus": zxAnSwAutoUpdateStatus,
       "zxAnSwAutoUpdateCurrFileName": zxAnSwAutoUpdateCurrFileName,
       "zxAnSwAutoUpdateCurrFileSize": zxAnSwAutoUpdateCurrFileSize,
       "zxAnSwAutoUpdateCurrFileProgress": zxAnSwAutoUpdateCurrFileProgress,
       "zxAnSwAutoUpdateTotalFiles": zxAnSwAutoUpdateTotalFiles,
       "zxAnSwAutoUpdateSuccessFiles": zxAnSwAutoUpdateSuccessFiles,
       "zxAnSwAutoUpdateFailedReason": zxAnSwAutoUpdateFailedReason,
       "zxAnFileTrapObjects": zxAnFileTrapObjects,
       "zxAnSwUpdateTrapGroup": zxAnSwUpdateTrapGroup,
       "zxAnSwAutoUpdateFinished": zxAnSwAutoUpdateFinished,
       "zxAnSwAutoUpdateVersionDiffer": zxAnSwAutoUpdateVersionDiffer,
       "zxAnSwAutoUpdateVersionChkFailed": zxAnSwAutoUpdateVersionChkFailed}
)
