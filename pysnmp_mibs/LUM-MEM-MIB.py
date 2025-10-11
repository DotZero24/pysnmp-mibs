# SNMP MIB module (LUM-MEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-MEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:24 2025
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

(lumMemMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumMemMIB",
    "lumModules")

(MgmtNameString,) = mibBuilder.importSymbols(
    "LUM-TC",
    "MgmtNameString")

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


# MODULE-IDENTITY

lumMemMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 22)
)
if mibBuilder.loadTexts:
    lumMemMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2003-01-09 00:00",
         "2002-11-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumMemConfs_ObjectIdentity = ObjectIdentity
lumMemConfs = _LumMemConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1)
)
_LumMemGroups_ObjectIdentity = ObjectIdentity
lumMemGroups = _LumMemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 1)
)
_LumMemCompl_ObjectIdentity = ObjectIdentity
lumMemCompl = _LumMemCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 2)
)
_LumMemMIBObjects_ObjectIdentity = ObjectIdentity
lumMemMIBObjects = _LumMemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2)
)
_MemGeneral_ObjectIdentity = ObjectIdentity
memGeneral = _MemGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 1)
)
_MemGeneralLastChangeTime_Type = DateAndTime
_MemGeneralLastChangeTime_Object = MibScalar
memGeneralLastChangeTime = _MemGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 1, 1),
    _MemGeneralLastChangeTime_Type()
)
memGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memGeneralLastChangeTime.setStatus("current")
_MemGeneralStateLastChangeTime_Type = DateAndTime
_MemGeneralStateLastChangeTime_Object = MibScalar
memGeneralStateLastChangeTime = _MemGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 1, 2),
    _MemGeneralStateLastChangeTime_Type()
)
memGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memGeneralStateLastChangeTime.setStatus("current")
_MemProcessList_ObjectIdentity = ObjectIdentity
memProcessList = _MemProcessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2)
)
_MemProcessTable_Object = MibTable
memProcessTable = _MemProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1)
)
if mibBuilder.loadTexts:
    memProcessTable.setStatus("current")
_MemProcessEntry_Object = MibTableRow
memProcessEntry = _MemProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1)
)
memProcessEntry.setIndexNames(
    (0, "LUM-MEM-MIB", "memProcessIndex"),
)
if mibBuilder.loadTexts:
    memProcessEntry.setStatus("current")


class _MemProcessIndex_Type(Unsigned32):
    """Custom type memProcessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemProcessIndex_Type.__name__ = "Unsigned32"
_MemProcessIndex_Object = MibTableColumn
memProcessIndex = _MemProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 1),
    _MemProcessIndex_Type()
)
memProcessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessIndex.setStatus("current")
_MemProcessName_Type = MgmtNameString
_MemProcessName_Object = MibTableColumn
memProcessName = _MemProcessName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 2),
    _MemProcessName_Type()
)
memProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessName.setStatus("current")
_MemProcessPid_Type = Unsigned32
_MemProcessPid_Object = MibTableColumn
memProcessPid = _MemProcessPid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 3),
    _MemProcessPid_Type()
)
memProcessPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessPid.setStatus("current")
_MemProcessCurSize_Type = Unsigned32
_MemProcessCurSize_Object = MibTableColumn
memProcessCurSize = _MemProcessCurSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 4),
    _MemProcessCurSize_Type()
)
memProcessCurSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessCurSize.setStatus("current")
_MemProcessMaxSizeTotal_Type = Unsigned32
_MemProcessMaxSizeTotal_Object = MibTableColumn
memProcessMaxSizeTotal = _MemProcessMaxSizeTotal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 5),
    _MemProcessMaxSizeTotal_Type()
)
memProcessMaxSizeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessMaxSizeTotal.setStatus("current")
_MemProcessMinSizeTotal_Type = Unsigned32
_MemProcessMinSizeTotal_Object = MibTableColumn
memProcessMinSizeTotal = _MemProcessMinSizeTotal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 6),
    _MemProcessMinSizeTotal_Type()
)
memProcessMinSizeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessMinSizeTotal.setStatus("current")
_MemProcessStartSizePeriod_Type = Unsigned32
_MemProcessStartSizePeriod_Object = MibTableColumn
memProcessStartSizePeriod = _MemProcessStartSizePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 7),
    _MemProcessStartSizePeriod_Type()
)
memProcessStartSizePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessStartSizePeriod.setStatus("current")
_MemProcessMaxSizePeriod_Type = Unsigned32
_MemProcessMaxSizePeriod_Object = MibTableColumn
memProcessMaxSizePeriod = _MemProcessMaxSizePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 8),
    _MemProcessMaxSizePeriod_Type()
)
memProcessMaxSizePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessMaxSizePeriod.setStatus("current")
_MemProcessMinSizePeriod_Type = Unsigned32
_MemProcessMinSizePeriod_Object = MibTableColumn
memProcessMinSizePeriod = _MemProcessMinSizePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 9),
    _MemProcessMinSizePeriod_Type()
)
memProcessMinSizePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessMinSizePeriod.setStatus("current")
_MemProcessIncrSizePeriod_Type = Unsigned32
_MemProcessIncrSizePeriod_Object = MibTableColumn
memProcessIncrSizePeriod = _MemProcessIncrSizePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 10),
    _MemProcessIncrSizePeriod_Type()
)
memProcessIncrSizePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessIncrSizePeriod.setStatus("current")
_MemProcessStartTime_Type = DateAndTime
_MemProcessStartTime_Object = MibTableColumn
memProcessStartTime = _MemProcessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 11),
    _MemProcessStartTime_Type()
)
memProcessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessStartTime.setStatus("current")
_MemProcessMaxTotalTime_Type = DateAndTime
_MemProcessMaxTotalTime_Object = MibTableColumn
memProcessMaxTotalTime = _MemProcessMaxTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 12),
    _MemProcessMaxTotalTime_Type()
)
memProcessMaxTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessMaxTotalTime.setStatus("current")
_MemProcessStartPeriodTime_Type = DateAndTime
_MemProcessStartPeriodTime_Object = MibTableColumn
memProcessStartPeriodTime = _MemProcessStartPeriodTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 13),
    _MemProcessStartPeriodTime_Type()
)
memProcessStartPeriodTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessStartPeriodTime.setStatus("current")
_MemProcessMaxPeriodTime_Type = DateAndTime
_MemProcessMaxPeriodTime_Object = MibTableColumn
memProcessMaxPeriodTime = _MemProcessMaxPeriodTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 14),
    _MemProcessMaxPeriodTime_Type()
)
memProcessMaxPeriodTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessMaxPeriodTime.setStatus("current")


class _MemProcessResetPeriodAction_Type(Integer32):
    """Custom type memProcessResetPeriodAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_MemProcessResetPeriodAction_Type.__name__ = "Integer32"
_MemProcessResetPeriodAction_Object = MibTableColumn
memProcessResetPeriodAction = _MemProcessResetPeriodAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 15),
    _MemProcessResetPeriodAction_Type()
)
memProcessResetPeriodAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memProcessResetPeriodAction.setStatus("current")


class _MemProcessState_Type(Integer32):
    """Custom type memProcessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2))
    )


_MemProcessState_Type.__name__ = "Integer32"
_MemProcessState_Object = MibTableColumn
memProcessState = _MemProcessState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 16),
    _MemProcessState_Type()
)
memProcessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memProcessState.setStatus("current")


class _MemProcessHistory_Type(DisplayString):
    """Custom type memProcessHistory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MemProcessHistory_Type.__name__ = "DisplayString"
_MemProcessHistory_Object = MibTableColumn
memProcessHistory = _MemProcessHistory_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 17),
    _MemProcessHistory_Type()
)
memProcessHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessHistory.setStatus("current")
_MemProcessLatestSampleTime_Type = DateAndTime
_MemProcessLatestSampleTime_Object = MibTableColumn
memProcessLatestSampleTime = _MemProcessLatestSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 2, 1, 1, 18),
    _MemProcessLatestSampleTime_Type()
)
memProcessLatestSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memProcessLatestSampleTime.setStatus("current")
_MemBoardList_ObjectIdentity = ObjectIdentity
memBoardList = _MemBoardList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3)
)
_MemBoardTable_Object = MibTable
memBoardTable = _MemBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1)
)
if mibBuilder.loadTexts:
    memBoardTable.setStatus("current")
_MemBoardEntry_Object = MibTableRow
memBoardEntry = _MemBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1)
)
memBoardEntry.setIndexNames(
    (0, "LUM-MEM-MIB", "memBoardIndex"),
)
if mibBuilder.loadTexts:
    memBoardEntry.setStatus("current")


class _MemBoardIndex_Type(Unsigned32):
    """Custom type memBoardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemBoardIndex_Type.__name__ = "Unsigned32"
_MemBoardIndex_Object = MibTableColumn
memBoardIndex = _MemBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1, 1),
    _MemBoardIndex_Type()
)
memBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBoardIndex.setStatus("current")
_MemBoardName_Type = MgmtNameString
_MemBoardName_Object = MibTableColumn
memBoardName = _MemBoardName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1, 2),
    _MemBoardName_Type()
)
memBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBoardName.setStatus("current")


class _MemBoardProcessSupervision_Type(Integer32):
    """Custom type memBoardProcessSupervision based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MemBoardProcessSupervision_Type.__name__ = "Integer32"
_MemBoardProcessSupervision_Object = MibTableColumn
memBoardProcessSupervision = _MemBoardProcessSupervision_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1, 3),
    _MemBoardProcessSupervision_Type()
)
memBoardProcessSupervision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memBoardProcessSupervision.setStatus("current")


class _MemBoardReportMode_Type(Integer32):
    """Custom type memBoardReportMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MemBoardReportMode_Type.__name__ = "Integer32"
_MemBoardReportMode_Object = MibTableColumn
memBoardReportMode = _MemBoardReportMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1, 4),
    _MemBoardReportMode_Type()
)
memBoardReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memBoardReportMode.setStatus("current")


class _MemBoardResetPeriodAction_Type(Integer32):
    """Custom type memBoardResetPeriodAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_MemBoardResetPeriodAction_Type.__name__ = "Integer32"
_MemBoardResetPeriodAction_Object = MibTableColumn
memBoardResetPeriodAction = _MemBoardResetPeriodAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1, 5),
    _MemBoardResetPeriodAction_Type()
)
memBoardResetPeriodAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memBoardResetPeriodAction.setStatus("current")
_MemBoardTotalMemUsed_Type = Unsigned32
_MemBoardTotalMemUsed_Object = MibTableColumn
memBoardTotalMemUsed = _MemBoardTotalMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1, 6),
    _MemBoardTotalMemUsed_Type()
)
memBoardTotalMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBoardTotalMemUsed.setStatus("current")
_MemBoardTotalMemFree_Type = Unsigned32
_MemBoardTotalMemFree_Object = MibTableColumn
memBoardTotalMemFree = _MemBoardTotalMemFree_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1, 7),
    _MemBoardTotalMemFree_Type()
)
memBoardTotalMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBoardTotalMemFree.setStatus("current")
_MemBoardTotalMemFreePercent_Type = Unsigned32
_MemBoardTotalMemFreePercent_Object = MibTableColumn
memBoardTotalMemFreePercent = _MemBoardTotalMemFreePercent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1, 8),
    _MemBoardTotalMemFreePercent_Type()
)
memBoardTotalMemFreePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBoardTotalMemFreePercent.setStatus("current")


class _MemBoardHistory_Type(DisplayString):
    """Custom type memBoardHistory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MemBoardHistory_Type.__name__ = "DisplayString"
_MemBoardHistory_Object = MibTableColumn
memBoardHistory = _MemBoardHistory_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 3, 1, 1, 9),
    _MemBoardHistory_Type()
)
memBoardHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBoardHistory.setStatus("current")
_MemControl_ObjectIdentity = ObjectIdentity
memControl = _MemControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 4)
)


class _MemControlSampleInterval_Type(Unsigned32):
    """Custom type memControlSampleInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_MemControlSampleInterval_Type.__name__ = "Unsigned32"
_MemControlSampleInterval_Object = MibScalar
memControlSampleInterval = _MemControlSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 4, 1),
    _MemControlSampleInterval_Type()
)
memControlSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memControlSampleInterval.setStatus("current")


class _MemControlReportInterval_Type(Unsigned32):
    """Custom type memControlReportInterval based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_MemControlReportInterval_Type.__name__ = "Unsigned32"
_MemControlReportInterval_Object = MibScalar
memControlReportInterval = _MemControlReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 4, 2),
    _MemControlReportInterval_Type()
)
memControlReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memControlReportInterval.setStatus("current")


class _MemControlMaxReportFiles_Type(Integer32):
    """Custom type memControlMaxReportFiles based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_MemControlMaxReportFiles_Type.__name__ = "Integer32"
_MemControlMaxReportFiles_Object = MibScalar
memControlMaxReportFiles = _MemControlMaxReportFiles_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 2, 4, 3),
    _MemControlMaxReportFiles_Type()
)
memControlMaxReportFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memControlMaxReportFiles.setStatus("current")

# Managed Objects groups

memGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 1, 1)
)
memGeneralGroup.setObjects(
      *(("LUM-MEM-MIB", "memGeneralLastChangeTime"),
        ("LUM-MEM-MIB", "memGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    memGeneralGroup.setStatus("current")

memProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 1, 2)
)
memProcessGroup.setObjects(
      *(("LUM-MEM-MIB", "memProcessIndex"),
        ("LUM-MEM-MIB", "memProcessName"),
        ("LUM-MEM-MIB", "memProcessPid"),
        ("LUM-MEM-MIB", "memProcessCurSize"),
        ("LUM-MEM-MIB", "memProcessMaxSizeTotal"),
        ("LUM-MEM-MIB", "memProcessMinSizeTotal"),
        ("LUM-MEM-MIB", "memProcessStartSizePeriod"),
        ("LUM-MEM-MIB", "memProcessMaxSizePeriod"),
        ("LUM-MEM-MIB", "memProcessMinSizePeriod"),
        ("LUM-MEM-MIB", "memProcessIncrSizePeriod"),
        ("LUM-MEM-MIB", "memProcessStartTime"),
        ("LUM-MEM-MIB", "memProcessMaxTotalTime"),
        ("LUM-MEM-MIB", "memProcessStartPeriodTime"),
        ("LUM-MEM-MIB", "memProcessMaxPeriodTime"),
        ("LUM-MEM-MIB", "memProcessResetPeriodAction"),
        ("LUM-MEM-MIB", "memProcessState"),
        ("LUM-MEM-MIB", "memProcessHistory"))
)
if mibBuilder.loadTexts:
    memProcessGroup.setStatus("deprecated")

memBoardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 1, 3)
)
memBoardGroup.setObjects(
      *(("LUM-MEM-MIB", "memBoardIndex"),
        ("LUM-MEM-MIB", "memBoardName"),
        ("LUM-MEM-MIB", "memBoardProcessSupervision"),
        ("LUM-MEM-MIB", "memBoardReportMode"),
        ("LUM-MEM-MIB", "memBoardResetPeriodAction"),
        ("LUM-MEM-MIB", "memBoardTotalMemUsed"),
        ("LUM-MEM-MIB", "memBoardTotalMemFree"),
        ("LUM-MEM-MIB", "memBoardTotalMemFreePercent"),
        ("LUM-MEM-MIB", "memBoardHistory"))
)
if mibBuilder.loadTexts:
    memBoardGroup.setStatus("current")

memControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 1, 4)
)
memControlGroup.setObjects(
      *(("LUM-MEM-MIB", "memControlSampleInterval"),
        ("LUM-MEM-MIB", "memControlReportInterval"))
)
if mibBuilder.loadTexts:
    memControlGroup.setStatus("current")

memControlGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 1, 5)
)
memControlGroupV2.setObjects(
      *(("LUM-MEM-MIB", "memControlSampleInterval"),
        ("LUM-MEM-MIB", "memControlReportInterval"),
        ("LUM-MEM-MIB", "memControlMaxReportFiles"))
)
if mibBuilder.loadTexts:
    memControlGroupV2.setStatus("current")

memProcessGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 1, 6)
)
memProcessGroupV2.setObjects(
      *(("LUM-MEM-MIB", "memProcessIndex"),
        ("LUM-MEM-MIB", "memProcessName"),
        ("LUM-MEM-MIB", "memProcessPid"),
        ("LUM-MEM-MIB", "memProcessCurSize"),
        ("LUM-MEM-MIB", "memProcessMaxSizeTotal"),
        ("LUM-MEM-MIB", "memProcessMinSizeTotal"),
        ("LUM-MEM-MIB", "memProcessStartSizePeriod"),
        ("LUM-MEM-MIB", "memProcessMaxSizePeriod"),
        ("LUM-MEM-MIB", "memProcessMinSizePeriod"),
        ("LUM-MEM-MIB", "memProcessIncrSizePeriod"),
        ("LUM-MEM-MIB", "memProcessStartTime"),
        ("LUM-MEM-MIB", "memProcessMaxTotalTime"),
        ("LUM-MEM-MIB", "memProcessStartPeriodTime"),
        ("LUM-MEM-MIB", "memProcessMaxPeriodTime"),
        ("LUM-MEM-MIB", "memProcessResetPeriodAction"),
        ("LUM-MEM-MIB", "memProcessState"),
        ("LUM-MEM-MIB", "memProcessHistory"),
        ("LUM-MEM-MIB", "memProcessLatestSampleTime"))
)
if mibBuilder.loadTexts:
    memProcessGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumMemBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 2, 1)
)
lumMemBasicComplV1.setObjects(
      *(("LUM-MEM-MIB", "memGeneralGroup"),
        ("LUM-MEM-MIB", "memProcessGroup"),
        ("LUM-MEM-MIB", "memBoardGroup"),
        ("LUM-MEM-MIB", "memControlGroup"))
)
if mibBuilder.loadTexts:
    lumMemBasicComplV1.setStatus(
        "deprecated"
    )

lumMemBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 2, 2)
)
lumMemBasicComplV2.setObjects(
      *(("LUM-MEM-MIB", "memGeneralGroup"),
        ("LUM-MEM-MIB", "memProcessGroup"),
        ("LUM-MEM-MIB", "memBoardGroup"),
        ("LUM-MEM-MIB", "memControlGroupV2"))
)
if mibBuilder.loadTexts:
    lumMemBasicComplV2.setStatus(
        "deprecated"
    )

lumMemBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21, 1, 2, 3)
)
lumMemBasicComplV3.setObjects(
      *(("LUM-MEM-MIB", "memGeneralGroup"),
        ("LUM-MEM-MIB", "memProcessGroupV2"),
        ("LUM-MEM-MIB", "memBoardGroup"),
        ("LUM-MEM-MIB", "memControlGroupV2"))
)
if mibBuilder.loadTexts:
    lumMemBasicComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-MEM-MIB",
    **{"lumMemMIBModule": lumMemMIBModule,
       "lumMemConfs": lumMemConfs,
       "lumMemGroups": lumMemGroups,
       "memGeneralGroup": memGeneralGroup,
       "memProcessGroup": memProcessGroup,
       "memBoardGroup": memBoardGroup,
       "memControlGroup": memControlGroup,
       "memControlGroupV2": memControlGroupV2,
       "memProcessGroupV2": memProcessGroupV2,
       "lumMemCompl": lumMemCompl,
       "lumMemBasicComplV1": lumMemBasicComplV1,
       "lumMemBasicComplV2": lumMemBasicComplV2,
       "lumMemBasicComplV3": lumMemBasicComplV3,
       "lumMemMIBObjects": lumMemMIBObjects,
       "memGeneral": memGeneral,
       "memGeneralLastChangeTime": memGeneralLastChangeTime,
       "memGeneralStateLastChangeTime": memGeneralStateLastChangeTime,
       "memProcessList": memProcessList,
       "memProcessTable": memProcessTable,
       "memProcessEntry": memProcessEntry,
       "memProcessIndex": memProcessIndex,
       "memProcessName": memProcessName,
       "memProcessPid": memProcessPid,
       "memProcessCurSize": memProcessCurSize,
       "memProcessMaxSizeTotal": memProcessMaxSizeTotal,
       "memProcessMinSizeTotal": memProcessMinSizeTotal,
       "memProcessStartSizePeriod": memProcessStartSizePeriod,
       "memProcessMaxSizePeriod": memProcessMaxSizePeriod,
       "memProcessMinSizePeriod": memProcessMinSizePeriod,
       "memProcessIncrSizePeriod": memProcessIncrSizePeriod,
       "memProcessStartTime": memProcessStartTime,
       "memProcessMaxTotalTime": memProcessMaxTotalTime,
       "memProcessStartPeriodTime": memProcessStartPeriodTime,
       "memProcessMaxPeriodTime": memProcessMaxPeriodTime,
       "memProcessResetPeriodAction": memProcessResetPeriodAction,
       "memProcessState": memProcessState,
       "memProcessHistory": memProcessHistory,
       "memProcessLatestSampleTime": memProcessLatestSampleTime,
       "memBoardList": memBoardList,
       "memBoardTable": memBoardTable,
       "memBoardEntry": memBoardEntry,
       "memBoardIndex": memBoardIndex,
       "memBoardName": memBoardName,
       "memBoardProcessSupervision": memBoardProcessSupervision,
       "memBoardReportMode": memBoardReportMode,
       "memBoardResetPeriodAction": memBoardResetPeriodAction,
       "memBoardTotalMemUsed": memBoardTotalMemUsed,
       "memBoardTotalMemFree": memBoardTotalMemFree,
       "memBoardTotalMemFreePercent": memBoardTotalMemFreePercent,
       "memBoardHistory": memBoardHistory,
       "memControl": memControl,
       "memControlSampleInterval": memControlSampleInterval,
       "memControlReportInterval": memControlReportInterval,
       "memControlMaxReportFiles": memControlMaxReportFiles}
)
