# SNMP MIB module (LUM-SOFTWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-SOFTWARE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:01 2025
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

(lumModules,
 lumSoftwareMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumSoftwareMIB")

(BoardOrInterfaceAdminStatus,
 CommandString,
 FaultStatus) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
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
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

lumSoftwareMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 28)
)
if mibBuilder.loadTexts:
    lumSoftwareMIBModule.setRevisions(
        ("2018-09-28 00:00",
         "2017-06-15 00:00",
         "2015-04-28 00:00",
         "2013-12-22 00:00",
         "2013-11-12 00:00",
         "2011-12-20 00:00",
         "2010-01-29 00:00",
         "2004-11-22 00:00",
         "2004-06-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumSoftwareConfs_ObjectIdentity = ObjectIdentity
lumSoftwareConfs = _LumSoftwareConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1)
)
_LumSoftwareGroups_ObjectIdentity = ObjectIdentity
lumSoftwareGroups = _LumSoftwareGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1)
)
_LumSoftwareCompl_ObjectIdentity = ObjectIdentity
lumSoftwareCompl = _LumSoftwareCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 2)
)
_LumSoftwareMIBObjects_ObjectIdentity = ObjectIdentity
lumSoftwareMIBObjects = _LumSoftwareMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2)
)
_SoftwareGeneral_ObjectIdentity = ObjectIdentity
softwareGeneral = _SoftwareGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 1)
)
_SoftwareGeneralLastChangeTime_Type = DateAndTime
_SoftwareGeneralLastChangeTime_Object = MibScalar
softwareGeneralLastChangeTime = _SoftwareGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 1, 1),
    _SoftwareGeneralLastChangeTime_Type()
)
softwareGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareGeneralLastChangeTime.setStatus("current")
_SoftwareGeneralConfigLastChangeTime_Type = DateAndTime
_SoftwareGeneralConfigLastChangeTime_Object = MibScalar
softwareGeneralConfigLastChangeTime = _SoftwareGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 1, 2),
    _SoftwareGeneralConfigLastChangeTime_Type()
)
softwareGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareGeneralConfigLastChangeTime.setStatus("current")
_SoftwareGeneralSoftwareVersionTableSize_Type = Unsigned32
_SoftwareGeneralSoftwareVersionTableSize_Object = MibScalar
softwareGeneralSoftwareVersionTableSize = _SoftwareGeneralSoftwareVersionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 1, 3),
    _SoftwareGeneralSoftwareVersionTableSize_Type()
)
softwareGeneralSoftwareVersionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareGeneralSoftwareVersionTableSize.setStatus("current")
_SoftwareGeneralSoftwareLogTableSize_Type = Unsigned32
_SoftwareGeneralSoftwareLogTableSize_Object = MibScalar
softwareGeneralSoftwareLogTableSize = _SoftwareGeneralSoftwareLogTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 1, 4),
    _SoftwareGeneralSoftwareLogTableSize_Type()
)
softwareGeneralSoftwareLogTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareGeneralSoftwareLogTableSize.setStatus("current")
_SoftwareGeneralSoftwareExpectedSwTableSize_Type = Unsigned32
_SoftwareGeneralSoftwareExpectedSwTableSize_Object = MibScalar
softwareGeneralSoftwareExpectedSwTableSize = _SoftwareGeneralSoftwareExpectedSwTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 1, 5),
    _SoftwareGeneralSoftwareExpectedSwTableSize_Type()
)
softwareGeneralSoftwareExpectedSwTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareGeneralSoftwareExpectedSwTableSize.setStatus("current")
_SoftwareVersionList_ObjectIdentity = ObjectIdentity
softwareVersionList = _SoftwareVersionList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2)
)
_SoftwareVersionTable_Object = MibTable
softwareVersionTable = _SoftwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2, 1)
)
if mibBuilder.loadTexts:
    softwareVersionTable.setStatus("current")
_SoftwareVersionEntry_Object = MibTableRow
softwareVersionEntry = _SoftwareVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2, 1, 1)
)
softwareVersionEntry.setIndexNames(
    (0, "LUM-SOFTWARE-MIB", "softwareVersionIndex"),
)
if mibBuilder.loadTexts:
    softwareVersionEntry.setStatus("current")


class _SoftwareVersionIndex_Type(Unsigned32):
    """Custom type softwareVersionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SoftwareVersionIndex_Type.__name__ = "Unsigned32"
_SoftwareVersionIndex_Object = MibTableColumn
softwareVersionIndex = _SoftwareVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2, 1, 1, 1),
    _SoftwareVersionIndex_Type()
)
softwareVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionIndex.setStatus("current")
_SoftwareVersionName_Type = DisplayString
_SoftwareVersionName_Object = MibTableColumn
softwareVersionName = _SoftwareVersionName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2, 1, 1, 2),
    _SoftwareVersionName_Type()
)
softwareVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionName.setStatus("current")
_SoftwareVersionSubrack_Type = Unsigned32
_SoftwareVersionSubrack_Object = MibTableColumn
softwareVersionSubrack = _SoftwareVersionSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2, 1, 1, 3),
    _SoftwareVersionSubrack_Type()
)
softwareVersionSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionSubrack.setStatus("current")
_SoftwareVersionSlot_Type = Unsigned32
_SoftwareVersionSlot_Object = MibTableColumn
softwareVersionSlot = _SoftwareVersionSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2, 1, 1, 4),
    _SoftwareVersionSlot_Type()
)
softwareVersionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionSlot.setStatus("current")


class _SoftwareVersionCategory_Type(Integer32):
    """Custom type softwareVersionCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot", 0),
          ("kernel", 1),
          ("appl", 2),
          ("fs", 3))
    )


_SoftwareVersionCategory_Type.__name__ = "Integer32"
_SoftwareVersionCategory_Object = MibTableColumn
softwareVersionCategory = _SoftwareVersionCategory_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2, 1, 1, 5),
    _SoftwareVersionCategory_Type()
)
softwareVersionCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionCategory.setStatus("current")
_SoftwareVersionVersion_Type = DisplayString
_SoftwareVersionVersion_Object = MibTableColumn
softwareVersionVersion = _SoftwareVersionVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2, 1, 1, 6),
    _SoftwareVersionVersion_Type()
)
softwareVersionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionVersion.setStatus("current")
_SoftwareVersionStatus_Type = Unsigned32
_SoftwareVersionStatus_Object = MibTableColumn
softwareVersionStatus = _SoftwareVersionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 2, 1, 1, 7),
    _SoftwareVersionStatus_Type()
)
softwareVersionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionStatus.setStatus("current")
_SoftwareCommand_ObjectIdentity = ObjectIdentity
softwareCommand = _SoftwareCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3)
)
_SoftwareCommandServerIp_Type = IpAddress
_SoftwareCommandServerIp_Object = MibScalar
softwareCommandServerIp = _SoftwareCommandServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 1),
    _SoftwareCommandServerIp_Type()
)
softwareCommandServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandServerIp.setStatus("current")


class _SoftwareCommandEnmFile_Type(DisplayString):
    """Custom type softwareCommandEnmFile based on DisplayString"""
    defaultValue = OctetString("")


_SoftwareCommandEnmFile_Type.__name__ = "DisplayString"
_SoftwareCommandEnmFile_Object = MibScalar
softwareCommandEnmFile = _SoftwareCommandEnmFile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 2),
    _SoftwareCommandEnmFile_Type()
)
softwareCommandEnmFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandEnmFile.setStatus("current")


class _SoftwareCommandIncludeFs_Type(Integer32):
    """Custom type softwareCommandIncludeFs based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SoftwareCommandIncludeFs_Type.__name__ = "Integer32"
_SoftwareCommandIncludeFs_Object = MibScalar
softwareCommandIncludeFs = _SoftwareCommandIncludeFs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 3),
    _SoftwareCommandIncludeFs_Type()
)
softwareCommandIncludeFs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandIncludeFs.setStatus("current")


class _SoftwareCommandCleanFirst_Type(Integer32):
    """Custom type softwareCommandCleanFirst based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noClean", 1),
          ("normalClean", 2),
          ("culessClean", 3))
    )


_SoftwareCommandCleanFirst_Type.__name__ = "Integer32"
_SoftwareCommandCleanFirst_Object = MibScalar
softwareCommandCleanFirst = _SoftwareCommandCleanFirst_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 4),
    _SoftwareCommandCleanFirst_Type()
)
softwareCommandCleanFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandCleanFirst.setStatus("current")


class _SoftwareCommandForce_Type(Integer32):
    """Custom type softwareCommandForce based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SoftwareCommandForce_Type.__name__ = "Integer32"
_SoftwareCommandForce_Object = MibScalar
softwareCommandForce = _SoftwareCommandForce_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 5),
    _SoftwareCommandForce_Type()
)
softwareCommandForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandForce.setStatus("current")


class _SoftwareCommandOperation_Type(Integer32):
    """Custom type softwareCommandOperation based on Integer32"""
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
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("test", 1),
          ("check", 2),
          ("install", 3),
          ("upgrade", 4),
          ("rebootAfter", 5),
          ("rebootCu", 6),
          ("rebootAll", 7),
          ("revert", 8),
          ("abort", 9),
          ("unlock", 10),
          ("clean", 11),
          ("forcedUnlock", 12),
          ("rebootAllCold", 13),
          ("rebootExpr", 14),
          ("rebootCold", 15),
          ("rebootPendingBoards", 16))
    )


_SoftwareCommandOperation_Type.__name__ = "Integer32"
_SoftwareCommandOperation_Object = MibScalar
softwareCommandOperation = _SoftwareCommandOperation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 6),
    _SoftwareCommandOperation_Type()
)
softwareCommandOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandOperation.setStatus("current")


class _SoftwareCommandOperationTimeout_Type(Unsigned32):
    """Custom type softwareCommandOperationTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SoftwareCommandOperationTimeout_Type.__name__ = "Unsigned32"
_SoftwareCommandOperationTimeout_Object = MibScalar
softwareCommandOperationTimeout = _SoftwareCommandOperationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 7),
    _SoftwareCommandOperationTimeout_Type()
)
softwareCommandOperationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandOperationTimeout.setStatus("current")


class _SoftwareCommandTestAndIncr_Type(TestAndIncr):
    """Custom type softwareCommandTestAndIncr based on TestAndIncr"""
    defaultValue = 0


_SoftwareCommandTestAndIncr_Type.__name__ = "TestAndIncr"
_SoftwareCommandTestAndIncr_Object = MibScalar
softwareCommandTestAndIncr = _SoftwareCommandTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 8),
    _SoftwareCommandTestAndIncr_Type()
)
softwareCommandTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandTestAndIncr.setStatus("current")


class _SoftwareCommandSemaphore_Type(Integer32):
    """Custom type softwareCommandSemaphore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("locked", 2))
    )


_SoftwareCommandSemaphore_Type.__name__ = "Integer32"
_SoftwareCommandSemaphore_Object = MibScalar
softwareCommandSemaphore = _SoftwareCommandSemaphore_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 9),
    _SoftwareCommandSemaphore_Type()
)
softwareCommandSemaphore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandSemaphore.setStatus("current")


class _SoftwareCommandOperationState_Type(Integer32):
    """Custom type softwareCommandOperationState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("pending", 2),
          ("cleaning", 3),
          ("checking", 4),
          ("downloading", 5),
          ("installing", 6),
          ("preparing", 7),
          ("activating", 8),
          ("installingFs", 9),
          ("reverting", 10),
          ("rebooting", 11))
    )


_SoftwareCommandOperationState_Type.__name__ = "Integer32"
_SoftwareCommandOperationState_Object = MibScalar
softwareCommandOperationState = _SoftwareCommandOperationState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 10),
    _SoftwareCommandOperationState_Type()
)
softwareCommandOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandOperationState.setStatus("current")
_SoftwareCommandProgressMax_Type = Unsigned32
_SoftwareCommandProgressMax_Object = MibScalar
softwareCommandProgressMax = _SoftwareCommandProgressMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 11),
    _SoftwareCommandProgressMax_Type()
)
softwareCommandProgressMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandProgressMax.setStatus("current")


class _SoftwareCommandResult_Type(Integer32):
    """Custom type softwareCommandResult based on Integer32"""
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
          ("success", 2),
          ("failed", 3))
    )


_SoftwareCommandResult_Type.__name__ = "Integer32"
_SoftwareCommandResult_Object = MibScalar
softwareCommandResult = _SoftwareCommandResult_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 12),
    _SoftwareCommandResult_Type()
)
softwareCommandResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandResult.setStatus("current")


class _SoftwareCommandEnmState_Type(Integer32):
    """Custom type softwareCommandEnmState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("upToDate", 2),
          ("rebootNeeded", 3),
          ("activateNeeded", 4),
          ("upgradeNeeded", 5),
          ("done", 6),
          ("filesNeeded", 7),
          ("upgradeWithoutRebootNeeded", 8),
          ("removeBoardNeeded", 9))
    )


_SoftwareCommandEnmState_Type.__name__ = "Integer32"
_SoftwareCommandEnmState_Object = MibScalar
softwareCommandEnmState = _SoftwareCommandEnmState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 13),
    _SoftwareCommandEnmState_Type()
)
softwareCommandEnmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandEnmState.setStatus("current")
_SoftwareCommandErrorCount_Type = Unsigned32
_SoftwareCommandErrorCount_Object = MibScalar
softwareCommandErrorCount = _SoftwareCommandErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 14),
    _SoftwareCommandErrorCount_Type()
)
softwareCommandErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandErrorCount.setStatus("current")
_SoftwareCommandProgressCounter_Type = Unsigned32
_SoftwareCommandProgressCounter_Object = MibScalar
softwareCommandProgressCounter = _SoftwareCommandProgressCounter_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 15),
    _SoftwareCommandProgressCounter_Type()
)
softwareCommandProgressCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandProgressCounter.setStatus("current")


class _SoftwareCommandNewPassword_Type(Unsigned32):
    """Custom type softwareCommandNewPassword based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SoftwareCommandNewPassword_Type.__name__ = "Unsigned32"
_SoftwareCommandNewPassword_Object = MibScalar
softwareCommandNewPassword = _SoftwareCommandNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 16),
    _SoftwareCommandNewPassword_Type()
)
softwareCommandNewPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandNewPassword.setStatus("current")


class _SoftwareCommandPassword_Type(Unsigned32):
    """Custom type softwareCommandPassword based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SoftwareCommandPassword_Type.__name__ = "Unsigned32"
_SoftwareCommandPassword_Object = MibScalar
softwareCommandPassword = _SoftwareCommandPassword_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 17),
    _SoftwareCommandPassword_Type()
)
softwareCommandPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandPassword.setStatus("current")


class _SoftwareCommandReleaseAfterOperation_Type(Integer32):
    """Custom type softwareCommandReleaseAfterOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SoftwareCommandReleaseAfterOperation_Type.__name__ = "Integer32"
_SoftwareCommandReleaseAfterOperation_Object = MibScalar
softwareCommandReleaseAfterOperation = _SoftwareCommandReleaseAfterOperation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 18),
    _SoftwareCommandReleaseAfterOperation_Type()
)
softwareCommandReleaseAfterOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandReleaseAfterOperation.setStatus("current")


class _SoftwareCommandSendTraps_Type(Integer32):
    """Custom type softwareCommandSendTraps based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SoftwareCommandSendTraps_Type.__name__ = "Integer32"
_SoftwareCommandSendTraps_Object = MibScalar
softwareCommandSendTraps = _SoftwareCommandSendTraps_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 19),
    _SoftwareCommandSendTraps_Type()
)
softwareCommandSendTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandSendTraps.setStatus("current")


class _SoftwareCommandClientOperationId_Type(Unsigned32):
    """Custom type softwareCommandClientOperationId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SoftwareCommandClientOperationId_Type.__name__ = "Unsigned32"
_SoftwareCommandClientOperationId_Object = MibScalar
softwareCommandClientOperationId = _SoftwareCommandClientOperationId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 20),
    _SoftwareCommandClientOperationId_Type()
)
softwareCommandClientOperationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandClientOperationId.setStatus("current")


class _SoftwareCommandTftpTimeout_Type(Unsigned32):
    """Custom type softwareCommandTftpTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_SoftwareCommandTftpTimeout_Type.__name__ = "Unsigned32"
_SoftwareCommandTftpTimeout_Object = MibScalar
softwareCommandTftpTimeout = _SoftwareCommandTftpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 21),
    _SoftwareCommandTftpTimeout_Type()
)
softwareCommandTftpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandTftpTimeout.setStatus("current")


class _SoftwareCommandLocalFtpDirectory_Type(DisplayString):
    """Custom type softwareCommandLocalFtpDirectory based on DisplayString"""
    defaultValue = OctetString("")


_SoftwareCommandLocalFtpDirectory_Type.__name__ = "DisplayString"
_SoftwareCommandLocalFtpDirectory_Object = MibScalar
softwareCommandLocalFtpDirectory = _SoftwareCommandLocalFtpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 22),
    _SoftwareCommandLocalFtpDirectory_Type()
)
softwareCommandLocalFtpDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandLocalFtpDirectory.setStatus("current")
_SoftwareCommandWarningCount_Type = Unsigned32
_SoftwareCommandWarningCount_Object = MibScalar
softwareCommandWarningCount = _SoftwareCommandWarningCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 23),
    _SoftwareCommandWarningCount_Type()
)
softwareCommandWarningCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandWarningCount.setStatus("current")


class _SoftwareCommandEnmRelease_Type(DisplayString):
    """Custom type softwareCommandEnmRelease based on DisplayString"""
    defaultValue = OctetString("")


_SoftwareCommandEnmRelease_Type.__name__ = "DisplayString"
_SoftwareCommandEnmRelease_Object = MibScalar
softwareCommandEnmRelease = _SoftwareCommandEnmRelease_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 24),
    _SoftwareCommandEnmRelease_Type()
)
softwareCommandEnmRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCommandEnmRelease.setStatus("current")


class _SoftwareCommandSubrackSlotExpr_Type(DisplayString):
    """Custom type softwareCommandSubrackSlotExpr based on DisplayString"""
    defaultValue = OctetString("")


_SoftwareCommandSubrackSlotExpr_Type.__name__ = "DisplayString"
_SoftwareCommandSubrackSlotExpr_Object = MibScalar
softwareCommandSubrackSlotExpr = _SoftwareCommandSubrackSlotExpr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 3, 25),
    _SoftwareCommandSubrackSlotExpr_Type()
)
softwareCommandSubrackSlotExpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCommandSubrackSlotExpr.setStatus("current")
_SoftwareLogList_ObjectIdentity = ObjectIdentity
softwareLogList = _SoftwareLogList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 4)
)
_SoftwareLogTable_Object = MibTable
softwareLogTable = _SoftwareLogTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 4, 1)
)
if mibBuilder.loadTexts:
    softwareLogTable.setStatus("current")
_SoftwareLogEntry_Object = MibTableRow
softwareLogEntry = _SoftwareLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 4, 1, 1)
)
softwareLogEntry.setIndexNames(
    (0, "LUM-SOFTWARE-MIB", "softwareLogIndex"),
)
if mibBuilder.loadTexts:
    softwareLogEntry.setStatus("current")


class _SoftwareLogIndex_Type(Unsigned32):
    """Custom type softwareLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SoftwareLogIndex_Type.__name__ = "Unsigned32"
_SoftwareLogIndex_Object = MibTableColumn
softwareLogIndex = _SoftwareLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 4, 1, 1, 1),
    _SoftwareLogIndex_Type()
)
softwareLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareLogIndex.setStatus("current")
_SoftwareLogName_Type = DisplayString
_SoftwareLogName_Object = MibTableColumn
softwareLogName = _SoftwareLogName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 4, 1, 1, 2),
    _SoftwareLogName_Type()
)
softwareLogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareLogName.setStatus("current")
_SoftwareLogTransaction_Type = Unsigned32
_SoftwareLogTransaction_Object = MibTableColumn
softwareLogTransaction = _SoftwareLogTransaction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 4, 1, 1, 3),
    _SoftwareLogTransaction_Type()
)
softwareLogTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareLogTransaction.setStatus("current")
_SoftwareLogString_Type = DisplayString
_SoftwareLogString_Object = MibTableColumn
softwareLogString = _SoftwareLogString_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 4, 1, 1, 4),
    _SoftwareLogString_Type()
)
softwareLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareLogString.setStatus("current")
_LumentisSoftwareNotifications_ObjectIdentity = ObjectIdentity
lumentisSoftwareNotifications = _LumentisSoftwareNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 5)
)
_SoftwareNotifyPrefix_ObjectIdentity = ObjectIdentity
softwareNotifyPrefix = _SoftwareNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 5, 0)
)
_SoftwareSpare_ObjectIdentity = ObjectIdentity
softwareSpare = _SoftwareSpare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6)
)
_SoftwareSpareBoardAddr_Type = IpAddress
_SoftwareSpareBoardAddr_Object = MibScalar
softwareSpareBoardAddr = _SoftwareSpareBoardAddr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 1),
    _SoftwareSpareBoardAddr_Type()
)
softwareSpareBoardAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareSpareBoardAddr.setStatus("current")
_SoftwareSpareBoardMask_Type = IpAddress
_SoftwareSpareBoardMask_Object = MibScalar
softwareSpareBoardMask = _SoftwareSpareBoardMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 2),
    _SoftwareSpareBoardMask_Type()
)
softwareSpareBoardMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareSpareBoardMask.setStatus("current")
_SoftwareSpareMasterAddr_Type = IpAddress
_SoftwareSpareMasterAddr_Object = MibScalar
softwareSpareMasterAddr = _SoftwareSpareMasterAddr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 3),
    _SoftwareSpareMasterAddr_Type()
)
softwareSpareMasterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareSpareMasterAddr.setStatus("current")


class _SoftwareSpareMode_Type(Integer32):
    """Custom type softwareSpareMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undef", 0),
          ("tu", 1),
          ("standalone", 2),
          ("slave", 3))
    )


_SoftwareSpareMode_Type.__name__ = "Integer32"
_SoftwareSpareMode_Object = MibScalar
softwareSpareMode = _SoftwareSpareMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 4),
    _SoftwareSpareMode_Type()
)
softwareSpareMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareSpareMode.setStatus("current")
_SoftwareSpareBackupServer_Type = IpAddress
_SoftwareSpareBackupServer_Object = MibScalar
softwareSpareBackupServer = _SoftwareSpareBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 5),
    _SoftwareSpareBackupServer_Type()
)
softwareSpareBackupServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareSpareBackupServer.setStatus("current")
_SoftwareSpareBackupFile_Type = DisplayString
_SoftwareSpareBackupFile_Object = MibScalar
softwareSpareBackupFile = _SoftwareSpareBackupFile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 6),
    _SoftwareSpareBackupFile_Type()
)
softwareSpareBackupFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareSpareBackupFile.setStatus("current")


class _SoftwareSpareState_Type(Integer32):
    """Custom type softwareSpareState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("undef", 0),
          ("waiting", 1),
          ("contactingCu", 2),
          ("installBoot", 3),
          ("installKernel", 4),
          ("installAppl", 5),
          ("installFs", 6),
          ("activating", 7),
          ("clearSparepart", 8),
          ("done", 9),
          ("publicAddress", 10))
    )


_SoftwareSpareState_Type.__name__ = "Integer32"
_SoftwareSpareState_Object = MibScalar
softwareSpareState = _SoftwareSpareState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 7),
    _SoftwareSpareState_Type()
)
softwareSpareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareSpareState.setStatus("current")


class _SoftwareSpareResult_Type(Integer32):
    """Custom type softwareSpareResult based on Integer32"""
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
          ("ok", 2),
          ("cuNotFound", 3),
          ("autoUpgradeNotSupported", 4),
          ("bootNotFound", 5),
          ("kernelNotFound", 6),
          ("applNotFound", 7),
          ("fsNotFound", 8),
          ("bootActivateFailed", 9),
          ("kernelActivateFailed", 10),
          ("applActivateFailed", 11),
          ("flashUpdateFailed", 12))
    )


_SoftwareSpareResult_Type.__name__ = "Integer32"
_SoftwareSpareResult_Object = MibScalar
softwareSpareResult = _SoftwareSpareResult_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 8),
    _SoftwareSpareResult_Type()
)
softwareSpareResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareSpareResult.setStatus("current")
_SoftwareSpareCommentString_Type = DisplayString
_SoftwareSpareCommentString_Object = MibScalar
softwareSpareCommentString = _SoftwareSpareCommentString_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 9),
    _SoftwareSpareCommentString_Type()
)
softwareSpareCommentString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareSpareCommentString.setStatus("current")
_SoftwareSpareConfigure_Type = CommandString
_SoftwareSpareConfigure_Object = MibScalar
softwareSpareConfigure = _SoftwareSpareConfigure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 6, 10),
    _SoftwareSpareConfigure_Type()
)
softwareSpareConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareSpareConfigure.setStatus("current")
_SoftwareExpectedSwList_ObjectIdentity = ObjectIdentity
softwareExpectedSwList = _SoftwareExpectedSwList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 7)
)
_SoftwareExpectedSwTable_Object = MibTable
softwareExpectedSwTable = _SoftwareExpectedSwTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 7, 1)
)
if mibBuilder.loadTexts:
    softwareExpectedSwTable.setStatus("current")
_SoftwareExpectedSwEntry_Object = MibTableRow
softwareExpectedSwEntry = _SoftwareExpectedSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 7, 1, 1)
)
softwareExpectedSwEntry.setIndexNames(
    (0, "LUM-SOFTWARE-MIB", "softwareExpectedSwIndex"),
)
if mibBuilder.loadTexts:
    softwareExpectedSwEntry.setStatus("current")


class _SoftwareExpectedSwIndex_Type(Unsigned32):
    """Custom type softwareExpectedSwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SoftwareExpectedSwIndex_Type.__name__ = "Unsigned32"
_SoftwareExpectedSwIndex_Object = MibTableColumn
softwareExpectedSwIndex = _SoftwareExpectedSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 7, 1, 1, 1),
    _SoftwareExpectedSwIndex_Type()
)
softwareExpectedSwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareExpectedSwIndex.setStatus("current")
_SoftwareExpectedSwName_Type = DisplayString
_SoftwareExpectedSwName_Object = MibTableColumn
softwareExpectedSwName = _SoftwareExpectedSwName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 7, 1, 1, 2),
    _SoftwareExpectedSwName_Type()
)
softwareExpectedSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareExpectedSwName.setStatus("current")


class _SoftwareExpectedSwCategory_Type(Integer32):
    """Custom type softwareExpectedSwCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot", 0),
          ("kernel", 1),
          ("appl", 2),
          ("fs", 3))
    )


_SoftwareExpectedSwCategory_Type.__name__ = "Integer32"
_SoftwareExpectedSwCategory_Object = MibTableColumn
softwareExpectedSwCategory = _SoftwareExpectedSwCategory_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 7, 1, 1, 3),
    _SoftwareExpectedSwCategory_Type()
)
softwareExpectedSwCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareExpectedSwCategory.setStatus("current")


class _SoftwareExpectedSwBoardType_Type(Integer32):
    """Custom type softwareExpectedSwBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cu", 0),
          ("tu", 1),
          ("all", 2))
    )


_SoftwareExpectedSwBoardType_Type.__name__ = "Integer32"
_SoftwareExpectedSwBoardType_Object = MibTableColumn
softwareExpectedSwBoardType = _SoftwareExpectedSwBoardType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 7, 1, 1, 4),
    _SoftwareExpectedSwBoardType_Type()
)
softwareExpectedSwBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareExpectedSwBoardType.setStatus("current")
_SoftwareExpectedSwFileName_Type = DisplayString
_SoftwareExpectedSwFileName_Object = MibTableColumn
softwareExpectedSwFileName = _SoftwareExpectedSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 7, 1, 1, 5),
    _SoftwareExpectedSwFileName_Type()
)
softwareExpectedSwFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareExpectedSwFileName.setStatus("current")


class _SoftwareExpectedSwPresent_Type(Integer32):
    """Custom type softwareExpectedSwPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SoftwareExpectedSwPresent_Type.__name__ = "Integer32"
_SoftwareExpectedSwPresent_Object = MibTableColumn
softwareExpectedSwPresent = _SoftwareExpectedSwPresent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 7, 1, 1, 6),
    _SoftwareExpectedSwPresent_Type()
)
softwareExpectedSwPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareExpectedSwPresent.setStatus("current")
_SoftwareCuRep_ObjectIdentity = ObjectIdentity
softwareCuRep = _SoftwareCuRep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 8)
)


class _SoftwareCuRepAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type softwareCuRepAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_SoftwareCuRepAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_SoftwareCuRepAdminStatus_Object = MibScalar
softwareCuRepAdminStatus = _SoftwareCuRepAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 8, 1),
    _SoftwareCuRepAdminStatus_Type()
)
softwareCuRepAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCuRepAdminStatus.setStatus("current")


class _SoftwareCuRepUnSaved_Type(Integer32):
    """Custom type softwareCuRepUnSaved based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SoftwareCuRepUnSaved_Type.__name__ = "Integer32"
_SoftwareCuRepUnSaved_Object = MibScalar
softwareCuRepUnSaved = _SoftwareCuRepUnSaved_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 8, 2),
    _SoftwareCuRepUnSaved_Type()
)
softwareCuRepUnSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCuRepUnSaved.setStatus("current")


class _SoftwareCuRepSystemMode_Type(Unsigned32):
    """Custom type softwareCuRepSystemMode based on Unsigned32"""
    defaultValue = 1


_SoftwareCuRepSystemMode_Type.__name__ = "Unsigned32"
_SoftwareCuRepSystemMode_Object = MibScalar
softwareCuRepSystemMode = _SoftwareCuRepSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 8, 3),
    _SoftwareCuRepSystemMode_Type()
)
softwareCuRepSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCuRepSystemMode.setStatus("current")


class _SoftwareCuRepRebootCu_Type(Integer32):
    """Custom type softwareCuRepRebootCu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SoftwareCuRepRebootCu_Type.__name__ = "Integer32"
_SoftwareCuRepRebootCu_Object = MibScalar
softwareCuRepRebootCu = _SoftwareCuRepRebootCu_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 8, 4),
    _SoftwareCuRepRebootCu_Type()
)
softwareCuRepRebootCu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCuRepRebootCu.setStatus("current")
_SoftwareCuRepOkConfigure_Type = CommandString
_SoftwareCuRepOkConfigure_Object = MibScalar
softwareCuRepOkConfigure = _SoftwareCuRepOkConfigure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 8, 5),
    _SoftwareCuRepOkConfigure_Type()
)
softwareCuRepOkConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCuRepOkConfigure.setStatus("current")
_SoftwareCuRepSwPackagesMissing_Type = FaultStatus
_SoftwareCuRepSwPackagesMissing_Object = MibScalar
softwareCuRepSwPackagesMissing = _SoftwareCuRepSwPackagesMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 8, 6),
    _SoftwareCuRepSwPackagesMissing_Type()
)
softwareCuRepSwPackagesMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCuRepSwPackagesMissing.setStatus("current")
_SoftwareCuRepSwNotDistributed_Type = FaultStatus
_SoftwareCuRepSwNotDistributed_Object = MibScalar
softwareCuRepSwNotDistributed = _SoftwareCuRepSwNotDistributed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 8, 7),
    _SoftwareCuRepSwNotDistributed_Type()
)
softwareCuRepSwNotDistributed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCuRepSwNotDistributed.setStatus("current")


class _SoftwareCuRepSupportedReplacements_Type(Integer32):
    """Custom type softwareCuRepSupportedReplacements based on Integer32"""
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
        *(("all", 1),
          ("cuSfp", 2),
          ("cuSfpii", 3),
          ("cuSfpiii", 4))
    )


_SoftwareCuRepSupportedReplacements_Type.__name__ = "Integer32"
_SoftwareCuRepSupportedReplacements_Object = MibScalar
softwareCuRepSupportedReplacements = _SoftwareCuRepSupportedReplacements_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 8, 8),
    _SoftwareCuRepSupportedReplacements_Type()
)
softwareCuRepSupportedReplacements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareCuRepSupportedReplacements.setStatus("current")

# Managed Objects groups

softwareGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 1)
)
softwareGeneralGroup.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralLastChangeTime"),
        ("LUM-SOFTWARE-MIB", "softwareGeneralConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    softwareGeneralGroup.setStatus("deprecated")

softwareVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 2)
)
softwareVersionGroup.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareVersionIndex"),
        ("LUM-SOFTWARE-MIB", "softwareVersionName"),
        ("LUM-SOFTWARE-MIB", "softwareVersionSubrack"),
        ("LUM-SOFTWARE-MIB", "softwareVersionSlot"),
        ("LUM-SOFTWARE-MIB", "softwareVersionCategory"),
        ("LUM-SOFTWARE-MIB", "softwareVersionVersion"),
        ("LUM-SOFTWARE-MIB", "softwareVersionStatus"))
)
if mibBuilder.loadTexts:
    softwareVersionGroup.setStatus("current")

softwareCommandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 3)
)
softwareCommandGroup.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareCommandServerIp"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmFile"),
        ("LUM-SOFTWARE-MIB", "softwareCommandIncludeFs"),
        ("LUM-SOFTWARE-MIB", "softwareCommandCleanFirst"),
        ("LUM-SOFTWARE-MIB", "softwareCommandForce"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperation"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperationTimeout"),
        ("LUM-SOFTWARE-MIB", "softwareCommandTestAndIncr"),
        ("LUM-SOFTWARE-MIB", "softwareCommandSemaphore"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperationState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandProgressCounter"),
        ("LUM-SOFTWARE-MIB", "softwareCommandResult"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandErrorCount"))
)
if mibBuilder.loadTexts:
    softwareCommandGroup.setStatus("deprecated")

softwareLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 4)
)
softwareLogGroup.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareLogIndex"),
        ("LUM-SOFTWARE-MIB", "softwareLogName"),
        ("LUM-SOFTWARE-MIB", "softwareLogTransaction"),
        ("LUM-SOFTWARE-MIB", "softwareLogString"))
)
if mibBuilder.loadTexts:
    softwareLogGroup.setStatus("current")

softwareCommandGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 5)
)
softwareCommandGroupV2.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareCommandServerIp"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmFile"),
        ("LUM-SOFTWARE-MIB", "softwareCommandIncludeFs"),
        ("LUM-SOFTWARE-MIB", "softwareCommandCleanFirst"),
        ("LUM-SOFTWARE-MIB", "softwareCommandForce"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperation"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperationTimeout"),
        ("LUM-SOFTWARE-MIB", "softwareCommandTestAndIncr"),
        ("LUM-SOFTWARE-MIB", "softwareCommandSemaphore"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperationState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandProgressMax"),
        ("LUM-SOFTWARE-MIB", "softwareCommandResult"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandErrorCount"),
        ("LUM-SOFTWARE-MIB", "softwareCommandProgressCounter"),
        ("LUM-SOFTWARE-MIB", "softwareCommandNewPassword"),
        ("LUM-SOFTWARE-MIB", "softwareCommandPassword"),
        ("LUM-SOFTWARE-MIB", "softwareCommandReleaseAfterOperation"),
        ("LUM-SOFTWARE-MIB", "softwareCommandSendTraps"),
        ("LUM-SOFTWARE-MIB", "softwareCommandClientOperationId"),
        ("LUM-SOFTWARE-MIB", "softwareCommandTftpTimeout"))
)
if mibBuilder.loadTexts:
    softwareCommandGroupV2.setStatus("deprecated")

softwareSpareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 6)
)
softwareSpareGroup.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareSpareBoardAddr"),
        ("LUM-SOFTWARE-MIB", "softwareSpareBoardMask"),
        ("LUM-SOFTWARE-MIB", "softwareSpareMasterAddr"),
        ("LUM-SOFTWARE-MIB", "softwareSpareMode"),
        ("LUM-SOFTWARE-MIB", "softwareSpareBackupServer"),
        ("LUM-SOFTWARE-MIB", "softwareSpareBackupFile"),
        ("LUM-SOFTWARE-MIB", "softwareSpareState"),
        ("LUM-SOFTWARE-MIB", "softwareSpareResult"),
        ("LUM-SOFTWARE-MIB", "softwareSpareCommentString"),
        ("LUM-SOFTWARE-MIB", "softwareSpareConfigure"))
)
if mibBuilder.loadTexts:
    softwareSpareGroup.setStatus("current")

softwareGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 7)
)
softwareGeneralGroupV2.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralLastChangeTime"),
        ("LUM-SOFTWARE-MIB", "softwareGeneralConfigLastChangeTime"),
        ("LUM-SOFTWARE-MIB", "softwareGeneralSoftwareVersionTableSize"),
        ("LUM-SOFTWARE-MIB", "softwareGeneralSoftwareLogTableSize"))
)
if mibBuilder.loadTexts:
    softwareGeneralGroupV2.setStatus("deprecated")

softwareGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 8)
)
softwareGeneralGroupV3.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralLastChangeTime"),
        ("LUM-SOFTWARE-MIB", "softwareGeneralConfigLastChangeTime"),
        ("LUM-SOFTWARE-MIB", "softwareGeneralSoftwareVersionTableSize"),
        ("LUM-SOFTWARE-MIB", "softwareGeneralSoftwareLogTableSize"),
        ("LUM-SOFTWARE-MIB", "softwareGeneralSoftwareExpectedSwTableSize"))
)
if mibBuilder.loadTexts:
    softwareGeneralGroupV3.setStatus("current")

softwareCommandGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 9)
)
softwareCommandGroupV3.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareCommandServerIp"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmFile"),
        ("LUM-SOFTWARE-MIB", "softwareCommandIncludeFs"),
        ("LUM-SOFTWARE-MIB", "softwareCommandCleanFirst"),
        ("LUM-SOFTWARE-MIB", "softwareCommandForce"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperation"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperationTimeout"),
        ("LUM-SOFTWARE-MIB", "softwareCommandTestAndIncr"),
        ("LUM-SOFTWARE-MIB", "softwareCommandSemaphore"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperationState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandProgressMax"),
        ("LUM-SOFTWARE-MIB", "softwareCommandResult"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandErrorCount"),
        ("LUM-SOFTWARE-MIB", "softwareCommandProgressCounter"),
        ("LUM-SOFTWARE-MIB", "softwareCommandNewPassword"),
        ("LUM-SOFTWARE-MIB", "softwareCommandPassword"),
        ("LUM-SOFTWARE-MIB", "softwareCommandReleaseAfterOperation"),
        ("LUM-SOFTWARE-MIB", "softwareCommandSendTraps"),
        ("LUM-SOFTWARE-MIB", "softwareCommandClientOperationId"),
        ("LUM-SOFTWARE-MIB", "softwareCommandTftpTimeout"),
        ("LUM-SOFTWARE-MIB", "softwareCommandLocalFtpDirectory"),
        ("LUM-SOFTWARE-MIB", "softwareCommandWarningCount"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmRelease"))
)
if mibBuilder.loadTexts:
    softwareCommandGroupV3.setStatus("deprecated")

softwareExpectedSwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 10)
)
softwareExpectedSwGroup.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareExpectedSwIndex"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwName"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwCategory"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwBoardType"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwFileName"))
)
if mibBuilder.loadTexts:
    softwareExpectedSwGroup.setStatus("deprecated")

softwareExpectedSwGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 11)
)
softwareExpectedSwGroupV2.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareExpectedSwIndex"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwName"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwCategory"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwBoardType"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwFileName"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwPresent"))
)
if mibBuilder.loadTexts:
    softwareExpectedSwGroupV2.setStatus("current")

softwareCuRepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 12)
)
softwareCuRepGroup.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareCuRepAdminStatus"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepUnSaved"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepSystemMode"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepRebootCu"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepOkConfigure"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepSwPackagesMissing"))
)
if mibBuilder.loadTexts:
    softwareCuRepGroup.setStatus("deprecated")

softwareCuRepGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 13)
)
softwareCuRepGroupV2.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareCuRepAdminStatus"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepUnSaved"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepSystemMode"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepRebootCu"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepOkConfigure"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepSwPackagesMissing"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepSwNotDistributed"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepSupportedReplacements"))
)
if mibBuilder.loadTexts:
    softwareCuRepGroupV2.setStatus("current")

softwareCommandGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 1, 14)
)
softwareCommandGroupV4.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareCommandServerIp"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmFile"),
        ("LUM-SOFTWARE-MIB", "softwareCommandIncludeFs"),
        ("LUM-SOFTWARE-MIB", "softwareCommandCleanFirst"),
        ("LUM-SOFTWARE-MIB", "softwareCommandForce"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperation"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperationTimeout"),
        ("LUM-SOFTWARE-MIB", "softwareCommandTestAndIncr"),
        ("LUM-SOFTWARE-MIB", "softwareCommandSemaphore"),
        ("LUM-SOFTWARE-MIB", "softwareCommandOperationState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandProgressMax"),
        ("LUM-SOFTWARE-MIB", "softwareCommandResult"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandErrorCount"),
        ("LUM-SOFTWARE-MIB", "softwareCommandProgressCounter"),
        ("LUM-SOFTWARE-MIB", "softwareCommandNewPassword"),
        ("LUM-SOFTWARE-MIB", "softwareCommandPassword"),
        ("LUM-SOFTWARE-MIB", "softwareCommandReleaseAfterOperation"),
        ("LUM-SOFTWARE-MIB", "softwareCommandSendTraps"),
        ("LUM-SOFTWARE-MIB", "softwareCommandClientOperationId"),
        ("LUM-SOFTWARE-MIB", "softwareCommandTftpTimeout"),
        ("LUM-SOFTWARE-MIB", "softwareCommandLocalFtpDirectory"),
        ("LUM-SOFTWARE-MIB", "softwareCommandWarningCount"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmRelease"),
        ("LUM-SOFTWARE-MIB", "softwareCommandSubrackSlotExpr"))
)
if mibBuilder.loadTexts:
    softwareCommandGroupV4.setStatus("current")


# Notification objects

softwareResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 2, 5, 0, 1)
)
softwareResultTrap.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareCommandOperationState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandProgressMax"),
        ("LUM-SOFTWARE-MIB", "softwareCommandResult"),
        ("LUM-SOFTWARE-MIB", "softwareCommandEnmState"),
        ("LUM-SOFTWARE-MIB", "softwareCommandErrorCount"),
        ("LUM-SOFTWARE-MIB", "softwareCommandProgressCounter"),
        ("LUM-SOFTWARE-MIB", "softwareCommandNewPassword"),
        ("LUM-SOFTWARE-MIB", "softwareCommandClientOperationId"))
)
if mibBuilder.loadTexts:
    softwareResultTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

lumSoftwareBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 2, 1)
)
lumSoftwareBasicComplV1.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralGroup"),
        ("LUM-SOFTWARE-MIB", "softwareVersionGroup"),
        ("LUM-SOFTWARE-MIB", "softwareCommandGroup"),
        ("LUM-SOFTWARE-MIB", "softwareLogGroup"))
)
if mibBuilder.loadTexts:
    lumSoftwareBasicComplV1.setStatus(
        "deprecated"
    )

lumSoftwareBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 2, 2)
)
lumSoftwareBasicComplV2.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralGroupV2"),
        ("LUM-SOFTWARE-MIB", "softwareVersionGroup"),
        ("LUM-SOFTWARE-MIB", "softwareCommandGroupV2"),
        ("LUM-SOFTWARE-MIB", "softwareLogGroup"),
        ("LUM-SOFTWARE-MIB", "softwareSpareGroup"))
)
if mibBuilder.loadTexts:
    lumSoftwareBasicComplV2.setStatus(
        "deprecated"
    )

lumSoftwareBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 2, 3)
)
lumSoftwareBasicComplV3.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareVersionGroup"),
        ("LUM-SOFTWARE-MIB", "softwareCommandGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareLogGroup"),
        ("LUM-SOFTWARE-MIB", "softwareSpareGroup"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwGroup"))
)
if mibBuilder.loadTexts:
    lumSoftwareBasicComplV3.setStatus(
        "deprecated"
    )

lumSoftwareBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 2, 4)
)
lumSoftwareBasicComplV4.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareVersionGroup"),
        ("LUM-SOFTWARE-MIB", "softwareCommandGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareLogGroup"),
        ("LUM-SOFTWARE-MIB", "softwareSpareGroup"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwGroupV2"))
)
if mibBuilder.loadTexts:
    lumSoftwareBasicComplV4.setStatus(
        "deprecated"
    )

lumSoftwareBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 2, 5)
)
lumSoftwareBasicComplV5.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareVersionGroup"),
        ("LUM-SOFTWARE-MIB", "softwareCommandGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareLogGroup"),
        ("LUM-SOFTWARE-MIB", "softwareSpareGroup"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwGroupV2"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepGroup"))
)
if mibBuilder.loadTexts:
    lumSoftwareBasicComplV5.setStatus(
        "deprecated"
    )

lumSoftwareBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 2, 6)
)
lumSoftwareBasicComplV6.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareVersionGroup"),
        ("LUM-SOFTWARE-MIB", "softwareCommandGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareLogGroup"),
        ("LUM-SOFTWARE-MIB", "softwareSpareGroup"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwGroupV2"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepGroupV2"))
)
if mibBuilder.loadTexts:
    lumSoftwareBasicComplV6.setStatus(
        "deprecated"
    )

lumSoftwareBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 2, 7)
)
lumSoftwareBasicComplV7.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareVersionGroup"),
        ("LUM-SOFTWARE-MIB", "softwareCommandGroupV4"),
        ("LUM-SOFTWARE-MIB", "softwareLogGroup"),
        ("LUM-SOFTWARE-MIB", "softwareSpareGroup"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwGroupV2"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepGroupV2"))
)
if mibBuilder.loadTexts:
    lumSoftwareBasicComplV7.setStatus(
        "deprecated"
    )

lumSoftwareBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28, 1, 2, 8)
)
lumSoftwareBasicComplV8.setObjects(
      *(("LUM-SOFTWARE-MIB", "softwareGeneralGroupV3"),
        ("LUM-SOFTWARE-MIB", "softwareVersionGroup"),
        ("LUM-SOFTWARE-MIB", "softwareCommandGroupV4"),
        ("LUM-SOFTWARE-MIB", "softwareLogGroup"),
        ("LUM-SOFTWARE-MIB", "softwareSpareGroup"),
        ("LUM-SOFTWARE-MIB", "softwareExpectedSwGroupV2"),
        ("LUM-SOFTWARE-MIB", "softwareCuRepGroupV2"))
)
if mibBuilder.loadTexts:
    lumSoftwareBasicComplV8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-SOFTWARE-MIB",
    **{"lumSoftwareMIBModule": lumSoftwareMIBModule,
       "lumSoftwareConfs": lumSoftwareConfs,
       "lumSoftwareGroups": lumSoftwareGroups,
       "softwareGeneralGroup": softwareGeneralGroup,
       "softwareVersionGroup": softwareVersionGroup,
       "softwareCommandGroup": softwareCommandGroup,
       "softwareLogGroup": softwareLogGroup,
       "softwareCommandGroupV2": softwareCommandGroupV2,
       "softwareSpareGroup": softwareSpareGroup,
       "softwareGeneralGroupV2": softwareGeneralGroupV2,
       "softwareGeneralGroupV3": softwareGeneralGroupV3,
       "softwareCommandGroupV3": softwareCommandGroupV3,
       "softwareExpectedSwGroup": softwareExpectedSwGroup,
       "softwareExpectedSwGroupV2": softwareExpectedSwGroupV2,
       "softwareCuRepGroup": softwareCuRepGroup,
       "softwareCuRepGroupV2": softwareCuRepGroupV2,
       "softwareCommandGroupV4": softwareCommandGroupV4,
       "lumSoftwareCompl": lumSoftwareCompl,
       "lumSoftwareBasicComplV1": lumSoftwareBasicComplV1,
       "lumSoftwareBasicComplV2": lumSoftwareBasicComplV2,
       "lumSoftwareBasicComplV3": lumSoftwareBasicComplV3,
       "lumSoftwareBasicComplV4": lumSoftwareBasicComplV4,
       "lumSoftwareBasicComplV5": lumSoftwareBasicComplV5,
       "lumSoftwareBasicComplV6": lumSoftwareBasicComplV6,
       "lumSoftwareBasicComplV7": lumSoftwareBasicComplV7,
       "lumSoftwareBasicComplV8": lumSoftwareBasicComplV8,
       "lumSoftwareMIBObjects": lumSoftwareMIBObjects,
       "softwareGeneral": softwareGeneral,
       "softwareGeneralLastChangeTime": softwareGeneralLastChangeTime,
       "softwareGeneralConfigLastChangeTime": softwareGeneralConfigLastChangeTime,
       "softwareGeneralSoftwareVersionTableSize": softwareGeneralSoftwareVersionTableSize,
       "softwareGeneralSoftwareLogTableSize": softwareGeneralSoftwareLogTableSize,
       "softwareGeneralSoftwareExpectedSwTableSize": softwareGeneralSoftwareExpectedSwTableSize,
       "softwareVersionList": softwareVersionList,
       "softwareVersionTable": softwareVersionTable,
       "softwareVersionEntry": softwareVersionEntry,
       "softwareVersionIndex": softwareVersionIndex,
       "softwareVersionName": softwareVersionName,
       "softwareVersionSubrack": softwareVersionSubrack,
       "softwareVersionSlot": softwareVersionSlot,
       "softwareVersionCategory": softwareVersionCategory,
       "softwareVersionVersion": softwareVersionVersion,
       "softwareVersionStatus": softwareVersionStatus,
       "softwareCommand": softwareCommand,
       "softwareCommandServerIp": softwareCommandServerIp,
       "softwareCommandEnmFile": softwareCommandEnmFile,
       "softwareCommandIncludeFs": softwareCommandIncludeFs,
       "softwareCommandCleanFirst": softwareCommandCleanFirst,
       "softwareCommandForce": softwareCommandForce,
       "softwareCommandOperation": softwareCommandOperation,
       "softwareCommandOperationTimeout": softwareCommandOperationTimeout,
       "softwareCommandTestAndIncr": softwareCommandTestAndIncr,
       "softwareCommandSemaphore": softwareCommandSemaphore,
       "softwareCommandOperationState": softwareCommandOperationState,
       "softwareCommandProgressMax": softwareCommandProgressMax,
       "softwareCommandResult": softwareCommandResult,
       "softwareCommandEnmState": softwareCommandEnmState,
       "softwareCommandErrorCount": softwareCommandErrorCount,
       "softwareCommandProgressCounter": softwareCommandProgressCounter,
       "softwareCommandNewPassword": softwareCommandNewPassword,
       "softwareCommandPassword": softwareCommandPassword,
       "softwareCommandReleaseAfterOperation": softwareCommandReleaseAfterOperation,
       "softwareCommandSendTraps": softwareCommandSendTraps,
       "softwareCommandClientOperationId": softwareCommandClientOperationId,
       "softwareCommandTftpTimeout": softwareCommandTftpTimeout,
       "softwareCommandLocalFtpDirectory": softwareCommandLocalFtpDirectory,
       "softwareCommandWarningCount": softwareCommandWarningCount,
       "softwareCommandEnmRelease": softwareCommandEnmRelease,
       "softwareCommandSubrackSlotExpr": softwareCommandSubrackSlotExpr,
       "softwareLogList": softwareLogList,
       "softwareLogTable": softwareLogTable,
       "softwareLogEntry": softwareLogEntry,
       "softwareLogIndex": softwareLogIndex,
       "softwareLogName": softwareLogName,
       "softwareLogTransaction": softwareLogTransaction,
       "softwareLogString": softwareLogString,
       "lumentisSoftwareNotifications": lumentisSoftwareNotifications,
       "softwareNotifyPrefix": softwareNotifyPrefix,
       "softwareResultTrap": softwareResultTrap,
       "softwareSpare": softwareSpare,
       "softwareSpareBoardAddr": softwareSpareBoardAddr,
       "softwareSpareBoardMask": softwareSpareBoardMask,
       "softwareSpareMasterAddr": softwareSpareMasterAddr,
       "softwareSpareMode": softwareSpareMode,
       "softwareSpareBackupServer": softwareSpareBackupServer,
       "softwareSpareBackupFile": softwareSpareBackupFile,
       "softwareSpareState": softwareSpareState,
       "softwareSpareResult": softwareSpareResult,
       "softwareSpareCommentString": softwareSpareCommentString,
       "softwareSpareConfigure": softwareSpareConfigure,
       "softwareExpectedSwList": softwareExpectedSwList,
       "softwareExpectedSwTable": softwareExpectedSwTable,
       "softwareExpectedSwEntry": softwareExpectedSwEntry,
       "softwareExpectedSwIndex": softwareExpectedSwIndex,
       "softwareExpectedSwName": softwareExpectedSwName,
       "softwareExpectedSwCategory": softwareExpectedSwCategory,
       "softwareExpectedSwBoardType": softwareExpectedSwBoardType,
       "softwareExpectedSwFileName": softwareExpectedSwFileName,
       "softwareExpectedSwPresent": softwareExpectedSwPresent,
       "softwareCuRep": softwareCuRep,
       "softwareCuRepAdminStatus": softwareCuRepAdminStatus,
       "softwareCuRepUnSaved": softwareCuRepUnSaved,
       "softwareCuRepSystemMode": softwareCuRepSystemMode,
       "softwareCuRepRebootCu": softwareCuRepRebootCu,
       "softwareCuRepOkConfigure": softwareCuRepOkConfigure,
       "softwareCuRepSwPackagesMissing": softwareCuRepSwPackagesMissing,
       "softwareCuRepSwNotDistributed": softwareCuRepSwNotDistributed,
       "softwareCuRepSupportedReplacements": softwareCuRepSupportedReplacements}
)
