# SNMP MIB module (ARICENT-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-IGMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:18 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsigmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 36)
)
if mibBuilder.loadTexts:
    fsigmpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fsigmp_ObjectIdentity = ObjectIdentity
fsigmp = _Fsigmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1)
)


class _FsIgmpGlobalStatus_Type(Integer32):
    """Custom type fsIgmpGlobalStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsIgmpGlobalStatus_Type.__name__ = "Integer32"
_FsIgmpGlobalStatus_Object = MibScalar
fsIgmpGlobalStatus = _FsIgmpGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 1),
    _FsIgmpGlobalStatus_Type()
)
fsIgmpGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpGlobalStatus.setStatus("current")


class _FsIgmpTraceLevel_Type(Integer32):
    """Custom type fsIgmpTraceLevel based on Integer32"""
    defaultValue = 0


_FsIgmpTraceLevel_Type.__name__ = "Integer32"
_FsIgmpTraceLevel_Object = MibScalar
fsIgmpTraceLevel = _FsIgmpTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 2),
    _FsIgmpTraceLevel_Type()
)
fsIgmpTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpTraceLevel.setStatus("current")


class _FsIgmpDebugLevel_Type(Integer32):
    """Custom type fsIgmpDebugLevel based on Integer32"""
    defaultValue = 0


_FsIgmpDebugLevel_Type.__name__ = "Integer32"
_FsIgmpDebugLevel_Object = MibScalar
fsIgmpDebugLevel = _FsIgmpDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 3),
    _FsIgmpDebugLevel_Type()
)
fsIgmpDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpDebugLevel.setStatus("current")
_FsIgmpInterfaceTable_Object = MibTable
fsIgmpInterfaceTable = _FsIgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4)
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceTable.setStatus("current")
_FsIgmpInterfaceEntry_Object = MibTableRow
fsIgmpInterfaceEntry = _FsIgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1)
)
fsIgmpInterfaceEntry.setIndexNames(
    (0, "ARICENT-IGMP-MIB", "fsIgmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpInterfaceEntry.setStatus("current")
_FsIgmpInterfaceIfIndex_Type = InterfaceIndex
_FsIgmpInterfaceIfIndex_Object = MibTableColumn
fsIgmpInterfaceIfIndex = _FsIgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 1),
    _FsIgmpInterfaceIfIndex_Type()
)
fsIgmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIfIndex.setStatus("current")


class _FsIgmpInterfaceAdminStatus_Type(Integer32):
    """Custom type fsIgmpInterfaceAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FsIgmpInterfaceAdminStatus_Type.__name__ = "Integer32"
_FsIgmpInterfaceAdminStatus_Object = MibTableColumn
fsIgmpInterfaceAdminStatus = _FsIgmpInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 2),
    _FsIgmpInterfaceAdminStatus_Type()
)
fsIgmpInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceAdminStatus.setStatus("current")


class _FsIgmpInterfaceFastLeaveStatus_Type(Integer32):
    """Custom type fsIgmpInterfaceFastLeaveStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsIgmpInterfaceFastLeaveStatus_Type.__name__ = "Integer32"
_FsIgmpInterfaceFastLeaveStatus_Object = MibTableColumn
fsIgmpInterfaceFastLeaveStatus = _FsIgmpInterfaceFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 3),
    _FsIgmpInterfaceFastLeaveStatus_Type()
)
fsIgmpInterfaceFastLeaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceFastLeaveStatus.setStatus("current")


class _FsIgmpInterfaceOperStatus_Type(Integer32):
    """Custom type fsIgmpInterfaceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FsIgmpInterfaceOperStatus_Type.__name__ = "Integer32"
_FsIgmpInterfaceOperStatus_Object = MibTableColumn
fsIgmpInterfaceOperStatus = _FsIgmpInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 4),
    _FsIgmpInterfaceOperStatus_Type()
)
fsIgmpInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceOperStatus.setStatus("current")
_FsIgmpInterfaceIncomingPkts_Type = Counter32
_FsIgmpInterfaceIncomingPkts_Object = MibTableColumn
fsIgmpInterfaceIncomingPkts = _FsIgmpInterfaceIncomingPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 5),
    _FsIgmpInterfaceIncomingPkts_Type()
)
fsIgmpInterfaceIncomingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIncomingPkts.setStatus("current")
_FsIgmpInterfaceIncomingJoins_Type = Counter32
_FsIgmpInterfaceIncomingJoins_Object = MibTableColumn
fsIgmpInterfaceIncomingJoins = _FsIgmpInterfaceIncomingJoins_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 6),
    _FsIgmpInterfaceIncomingJoins_Type()
)
fsIgmpInterfaceIncomingJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIncomingJoins.setStatus("current")
_FsIgmpInterfaceIncomingLeaves_Type = Counter32
_FsIgmpInterfaceIncomingLeaves_Object = MibTableColumn
fsIgmpInterfaceIncomingLeaves = _FsIgmpInterfaceIncomingLeaves_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 7),
    _FsIgmpInterfaceIncomingLeaves_Type()
)
fsIgmpInterfaceIncomingLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIncomingLeaves.setStatus("current")
_FsIgmpInterfaceIncomingQueries_Type = Counter32
_FsIgmpInterfaceIncomingQueries_Object = MibTableColumn
fsIgmpInterfaceIncomingQueries = _FsIgmpInterfaceIncomingQueries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 8),
    _FsIgmpInterfaceIncomingQueries_Type()
)
fsIgmpInterfaceIncomingQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIncomingQueries.setStatus("current")
_FsIgmpInterfaceOutgoingQueries_Type = Counter32
_FsIgmpInterfaceOutgoingQueries_Object = MibTableColumn
fsIgmpInterfaceOutgoingQueries = _FsIgmpInterfaceOutgoingQueries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 9),
    _FsIgmpInterfaceOutgoingQueries_Type()
)
fsIgmpInterfaceOutgoingQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceOutgoingQueries.setStatus("current")
_FsIgmpInterfaceRxGenQueries_Type = Counter32
_FsIgmpInterfaceRxGenQueries_Object = MibTableColumn
fsIgmpInterfaceRxGenQueries = _FsIgmpInterfaceRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 10),
    _FsIgmpInterfaceRxGenQueries_Type()
)
fsIgmpInterfaceRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxGenQueries.setStatus("current")
_FsIgmpInterfaceRxGrpQueries_Type = Counter32
_FsIgmpInterfaceRxGrpQueries_Object = MibTableColumn
fsIgmpInterfaceRxGrpQueries = _FsIgmpInterfaceRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 11),
    _FsIgmpInterfaceRxGrpQueries_Type()
)
fsIgmpInterfaceRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxGrpQueries.setStatus("current")
_FsIgmpInterfaceRxGrpAndSrcQueries_Type = Counter32
_FsIgmpInterfaceRxGrpAndSrcQueries_Object = MibTableColumn
fsIgmpInterfaceRxGrpAndSrcQueries = _FsIgmpInterfaceRxGrpAndSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 12),
    _FsIgmpInterfaceRxGrpAndSrcQueries_Type()
)
fsIgmpInterfaceRxGrpAndSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxGrpAndSrcQueries.setStatus("current")
_FsIgmpInterfaceRxv1v2Reports_Type = Counter32
_FsIgmpInterfaceRxv1v2Reports_Object = MibTableColumn
fsIgmpInterfaceRxv1v2Reports = _FsIgmpInterfaceRxv1v2Reports_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 13),
    _FsIgmpInterfaceRxv1v2Reports_Type()
)
fsIgmpInterfaceRxv1v2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxv1v2Reports.setStatus("current")
_FsIgmpInterfaceRxv3Reports_Type = Counter32
_FsIgmpInterfaceRxv3Reports_Object = MibTableColumn
fsIgmpInterfaceRxv3Reports = _FsIgmpInterfaceRxv3Reports_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 14),
    _FsIgmpInterfaceRxv3Reports_Type()
)
fsIgmpInterfaceRxv3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRxv3Reports.setStatus("current")
_FsIgmpInterfaceTxGenQueries_Type = Counter32
_FsIgmpInterfaceTxGenQueries_Object = MibTableColumn
fsIgmpInterfaceTxGenQueries = _FsIgmpInterfaceTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 15),
    _FsIgmpInterfaceTxGenQueries_Type()
)
fsIgmpInterfaceTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxGenQueries.setStatus("current")
_FsIgmpInterfaceTxGrpQueries_Type = Counter32
_FsIgmpInterfaceTxGrpQueries_Object = MibTableColumn
fsIgmpInterfaceTxGrpQueries = _FsIgmpInterfaceTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 16),
    _FsIgmpInterfaceTxGrpQueries_Type()
)
fsIgmpInterfaceTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxGrpQueries.setStatus("current")
_FsIgmpInterfaceTxGrpAndSrcQueries_Type = Counter32
_FsIgmpInterfaceTxGrpAndSrcQueries_Object = MibTableColumn
fsIgmpInterfaceTxGrpAndSrcQueries = _FsIgmpInterfaceTxGrpAndSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 17),
    _FsIgmpInterfaceTxGrpAndSrcQueries_Type()
)
fsIgmpInterfaceTxGrpAndSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxGrpAndSrcQueries.setStatus("current")
_FsIgmpInterfaceTxv1v2Reports_Type = Counter32
_FsIgmpInterfaceTxv1v2Reports_Object = MibTableColumn
fsIgmpInterfaceTxv1v2Reports = _FsIgmpInterfaceTxv1v2Reports_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 18),
    _FsIgmpInterfaceTxv1v2Reports_Type()
)
fsIgmpInterfaceTxv1v2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxv1v2Reports.setStatus("current")
_FsIgmpInterfaceTxv3Reports_Type = Counter32
_FsIgmpInterfaceTxv3Reports_Object = MibTableColumn
fsIgmpInterfaceTxv3Reports = _FsIgmpInterfaceTxv3Reports_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 19),
    _FsIgmpInterfaceTxv3Reports_Type()
)
fsIgmpInterfaceTxv3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxv3Reports.setStatus("current")
_FsIgmpInterfaceTxv2Leaves_Type = Counter32
_FsIgmpInterfaceTxv2Leaves_Object = MibTableColumn
fsIgmpInterfaceTxv2Leaves = _FsIgmpInterfaceTxv2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 20),
    _FsIgmpInterfaceTxv2Leaves_Type()
)
fsIgmpInterfaceTxv2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceTxv2Leaves.setStatus("current")


class _FsIgmpInterfaceChannelTrackStatus_Type(Integer32):
    """Custom type fsIgmpInterfaceChannelTrackStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsIgmpInterfaceChannelTrackStatus_Type.__name__ = "Integer32"
_FsIgmpInterfaceChannelTrackStatus_Object = MibTableColumn
fsIgmpInterfaceChannelTrackStatus = _FsIgmpInterfaceChannelTrackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 21),
    _FsIgmpInterfaceChannelTrackStatus_Type()
)
fsIgmpInterfaceChannelTrackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceChannelTrackStatus.setStatus("current")


class _FsIgmpInterfaceGroupListId_Type(Unsigned32):
    """Custom type fsIgmpInterfaceGroupListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsIgmpInterfaceGroupListId_Type.__name__ = "Unsigned32"
_FsIgmpInterfaceGroupListId_Object = MibTableColumn
fsIgmpInterfaceGroupListId = _FsIgmpInterfaceGroupListId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 22),
    _FsIgmpInterfaceGroupListId_Type()
)
fsIgmpInterfaceGroupListId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceGroupListId.setStatus("current")


class _FsIgmpInterfaceLimit_Type(Unsigned32):
    """Custom type fsIgmpInterfaceLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsIgmpInterfaceLimit_Type.__name__ = "Unsigned32"
_FsIgmpInterfaceLimit_Object = MibTableColumn
fsIgmpInterfaceLimit = _FsIgmpInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 23),
    _FsIgmpInterfaceLimit_Type()
)
fsIgmpInterfaceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceLimit.setStatus("current")


class _FsIgmpInterfaceCurGrpCount_Type(Unsigned32):
    """Custom type fsIgmpInterfaceCurGrpCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsIgmpInterfaceCurGrpCount_Type.__name__ = "Unsigned32"
_FsIgmpInterfaceCurGrpCount_Object = MibTableColumn
fsIgmpInterfaceCurGrpCount = _FsIgmpInterfaceCurGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 24),
    _FsIgmpInterfaceCurGrpCount_Type()
)
fsIgmpInterfaceCurGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceCurGrpCount.setStatus("current")
_FsIgmpInterfaceCKSumError_Type = Counter32
_FsIgmpInterfaceCKSumError_Object = MibTableColumn
fsIgmpInterfaceCKSumError = _FsIgmpInterfaceCKSumError_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 25),
    _FsIgmpInterfaceCKSumError_Type()
)
fsIgmpInterfaceCKSumError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceCKSumError.setStatus("current")
_FsIgmpInterfacePktLenError_Type = Counter32
_FsIgmpInterfacePktLenError_Object = MibTableColumn
fsIgmpInterfacePktLenError = _FsIgmpInterfacePktLenError_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 26),
    _FsIgmpInterfacePktLenError_Type()
)
fsIgmpInterfacePktLenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfacePktLenError.setStatus("current")
_FsIgmpInterfacePktsWithLocalIP_Type = Counter32
_FsIgmpInterfacePktsWithLocalIP_Object = MibTableColumn
fsIgmpInterfacePktsWithLocalIP = _FsIgmpInterfacePktsWithLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 27),
    _FsIgmpInterfacePktsWithLocalIP_Type()
)
fsIgmpInterfacePktsWithLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfacePktsWithLocalIP.setStatus("current")
_FsIgmpInterfaceSubnetCheckFailure_Type = Counter32
_FsIgmpInterfaceSubnetCheckFailure_Object = MibTableColumn
fsIgmpInterfaceSubnetCheckFailure = _FsIgmpInterfaceSubnetCheckFailure_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 28),
    _FsIgmpInterfaceSubnetCheckFailure_Type()
)
fsIgmpInterfaceSubnetCheckFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceSubnetCheckFailure.setStatus("current")
_FsIgmpInterfaceQryFromNonQuerier_Type = Counter32
_FsIgmpInterfaceQryFromNonQuerier_Object = MibTableColumn
fsIgmpInterfaceQryFromNonQuerier = _FsIgmpInterfaceQryFromNonQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 29),
    _FsIgmpInterfaceQryFromNonQuerier_Type()
)
fsIgmpInterfaceQryFromNonQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQryFromNonQuerier.setStatus("current")
_FsIgmpInterfaceReportVersionMisMatch_Type = Counter32
_FsIgmpInterfaceReportVersionMisMatch_Object = MibTableColumn
fsIgmpInterfaceReportVersionMisMatch = _FsIgmpInterfaceReportVersionMisMatch_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 30),
    _FsIgmpInterfaceReportVersionMisMatch_Type()
)
fsIgmpInterfaceReportVersionMisMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceReportVersionMisMatch.setStatus("current")
_FsIgmpInterfaceQryVersionMisMatch_Type = Counter32
_FsIgmpInterfaceQryVersionMisMatch_Object = MibTableColumn
fsIgmpInterfaceQryVersionMisMatch = _FsIgmpInterfaceQryVersionMisMatch_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 31),
    _FsIgmpInterfaceQryVersionMisMatch_Type()
)
fsIgmpInterfaceQryVersionMisMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceQryVersionMisMatch.setStatus("current")
_FsIgmpInterfaceUnknownMsgType_Type = Counter32
_FsIgmpInterfaceUnknownMsgType_Object = MibTableColumn
fsIgmpInterfaceUnknownMsgType = _FsIgmpInterfaceUnknownMsgType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 32),
    _FsIgmpInterfaceUnknownMsgType_Type()
)
fsIgmpInterfaceUnknownMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceUnknownMsgType.setStatus("current")
_FsIgmpInterfaceInvalidV1Report_Type = Counter32
_FsIgmpInterfaceInvalidV1Report_Object = MibTableColumn
fsIgmpInterfaceInvalidV1Report = _FsIgmpInterfaceInvalidV1Report_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 33),
    _FsIgmpInterfaceInvalidV1Report_Type()
)
fsIgmpInterfaceInvalidV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceInvalidV1Report.setStatus("current")
_FsIgmpInterfaceInvalidV2Report_Type = Counter32
_FsIgmpInterfaceInvalidV2Report_Object = MibTableColumn
fsIgmpInterfaceInvalidV2Report = _FsIgmpInterfaceInvalidV2Report_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 34),
    _FsIgmpInterfaceInvalidV2Report_Type()
)
fsIgmpInterfaceInvalidV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceInvalidV2Report.setStatus("current")
_FsIgmpInterfaceInvalidV3Report_Type = Counter32
_FsIgmpInterfaceInvalidV3Report_Object = MibTableColumn
fsIgmpInterfaceInvalidV3Report = _FsIgmpInterfaceInvalidV3Report_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 35),
    _FsIgmpInterfaceInvalidV3Report_Type()
)
fsIgmpInterfaceInvalidV3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceInvalidV3Report.setStatus("current")
_FsIgmpInterfaceRouterAlertCheckFailure_Type = Counter32
_FsIgmpInterfaceRouterAlertCheckFailure_Object = MibTableColumn
fsIgmpInterfaceRouterAlertCheckFailure = _FsIgmpInterfaceRouterAlertCheckFailure_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 36),
    _FsIgmpInterfaceRouterAlertCheckFailure_Type()
)
fsIgmpInterfaceRouterAlertCheckFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceRouterAlertCheckFailure.setStatus("current")
_FsIgmpInterfaceIncomingSSMPkts_Type = Counter32
_FsIgmpInterfaceIncomingSSMPkts_Object = MibTableColumn
fsIgmpInterfaceIncomingSSMPkts = _FsIgmpInterfaceIncomingSSMPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 37),
    _FsIgmpInterfaceIncomingSSMPkts_Type()
)
fsIgmpInterfaceIncomingSSMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceIncomingSSMPkts.setStatus("current")
_FsIgmpInterfaceInvalidSSMPkts_Type = Counter32
_FsIgmpInterfaceInvalidSSMPkts_Object = MibTableColumn
fsIgmpInterfaceInvalidSSMPkts = _FsIgmpInterfaceInvalidSSMPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 38),
    _FsIgmpInterfaceInvalidSSMPkts_Type()
)
fsIgmpInterfaceInvalidSSMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpInterfaceInvalidSSMPkts.setStatus("current")


class _FsIgmpInterfaceJoinPktRate_Type(Integer32):
    """Custom type fsIgmpInterfaceJoinPktRate based on Integer32"""
    defaultValue = 0


_FsIgmpInterfaceJoinPktRate_Type.__name__ = "Integer32"
_FsIgmpInterfaceJoinPktRate_Object = MibTableColumn
fsIgmpInterfaceJoinPktRate = _FsIgmpInterfaceJoinPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 4, 1, 39),
    _FsIgmpInterfaceJoinPktRate_Type()
)
fsIgmpInterfaceJoinPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpInterfaceJoinPktRate.setStatus("current")
_FsIgmpCacheTable_Object = MibTable
fsIgmpCacheTable = _FsIgmpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 5)
)
if mibBuilder.loadTexts:
    fsIgmpCacheTable.setStatus("current")
_FsIgmpCacheEntry_Object = MibTableRow
fsIgmpCacheEntry = _FsIgmpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 5, 1)
)
fsIgmpCacheEntry.setIndexNames(
    (0, "ARICENT-IGMP-MIB", "fsIgmpCacheAddress"),
    (0, "ARICENT-IGMP-MIB", "fsIgmpCacheIfIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpCacheEntry.setStatus("current")
_FsIgmpCacheAddress_Type = IpAddress
_FsIgmpCacheAddress_Object = MibTableColumn
fsIgmpCacheAddress = _FsIgmpCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 5, 1, 1),
    _FsIgmpCacheAddress_Type()
)
fsIgmpCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpCacheAddress.setStatus("current")
_FsIgmpCacheIfIndex_Type = InterfaceIndex
_FsIgmpCacheIfIndex_Object = MibTableColumn
fsIgmpCacheIfIndex = _FsIgmpCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 5, 1, 2),
    _FsIgmpCacheIfIndex_Type()
)
fsIgmpCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpCacheIfIndex.setStatus("current")
_FsIgmpCacheGroupCompMode_Type = Integer32
_FsIgmpCacheGroupCompMode_Object = MibTableColumn
fsIgmpCacheGroupCompMode = _FsIgmpCacheGroupCompMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 5, 1, 3),
    _FsIgmpCacheGroupCompMode_Type()
)
fsIgmpCacheGroupCompMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpCacheGroupCompMode.setStatus("current")
_FsIgmpGroupListTable_Object = MibTable
fsIgmpGroupListTable = _FsIgmpGroupListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 6)
)
if mibBuilder.loadTexts:
    fsIgmpGroupListTable.setStatus("current")
_FsIgmpGroupListEntry_Object = MibTableRow
fsIgmpGroupListEntry = _FsIgmpGroupListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 6, 1)
)
fsIgmpGroupListEntry.setIndexNames(
    (0, "ARICENT-IGMP-MIB", "fsIgmpGrpListId"),
    (0, "ARICENT-IGMP-MIB", "fsIgmpGrpIP"),
    (0, "ARICENT-IGMP-MIB", "fsIgmpGrpPrefixLen"),
)
if mibBuilder.loadTexts:
    fsIgmpGroupListEntry.setStatus("current")


class _FsIgmpGrpListId_Type(Unsigned32):
    """Custom type fsIgmpGrpListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsIgmpGrpListId_Type.__name__ = "Unsigned32"
_FsIgmpGrpListId_Object = MibTableColumn
fsIgmpGrpListId = _FsIgmpGrpListId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 6, 1, 1),
    _FsIgmpGrpListId_Type()
)
fsIgmpGrpListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpGrpListId.setStatus("current")
_FsIgmpGrpIP_Type = IpAddress
_FsIgmpGrpIP_Object = MibTableColumn
fsIgmpGrpIP = _FsIgmpGrpIP_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 6, 1, 2),
    _FsIgmpGrpIP_Type()
)
fsIgmpGrpIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpGrpIP.setStatus("current")
_FsIgmpGrpPrefixLen_Type = IpAddress
_FsIgmpGrpPrefixLen_Object = MibTableColumn
fsIgmpGrpPrefixLen = _FsIgmpGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 6, 1, 3),
    _FsIgmpGrpPrefixLen_Type()
)
fsIgmpGrpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpGrpPrefixLen.setStatus("current")
_FsIgmpGrpListRowStatus_Type = RowStatus
_FsIgmpGrpListRowStatus_Object = MibTableColumn
fsIgmpGrpListRowStatus = _FsIgmpGrpListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 6, 1, 4),
    _FsIgmpGrpListRowStatus_Type()
)
fsIgmpGrpListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpGrpListRowStatus.setStatus("current")
_FsIgmpScalarGroup_ObjectIdentity = ObjectIdentity
fsIgmpScalarGroup = _FsIgmpScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 7)
)


class _FsIgmpGlobalLimit_Type(Unsigned32):
    """Custom type fsIgmpGlobalLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsIgmpGlobalLimit_Type.__name__ = "Unsigned32"
_FsIgmpGlobalLimit_Object = MibScalar
fsIgmpGlobalLimit = _FsIgmpGlobalLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 7, 1),
    _FsIgmpGlobalLimit_Type()
)
fsIgmpGlobalLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpGlobalLimit.setStatus("current")


class _FsIgmpGlobalCurGrpCount_Type(Unsigned32):
    """Custom type fsIgmpGlobalCurGrpCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsIgmpGlobalCurGrpCount_Type.__name__ = "Unsigned32"
_FsIgmpGlobalCurGrpCount_Object = MibScalar
fsIgmpGlobalCurGrpCount = _FsIgmpGlobalCurGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 7, 2),
    _FsIgmpGlobalCurGrpCount_Type()
)
fsIgmpGlobalCurGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpGlobalCurGrpCount.setStatus("current")


class _FsIgmpSSMMapStatus_Type(Integer32):
    """Custom type fsIgmpSSMMapStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsIgmpSSMMapStatus_Type.__name__ = "Integer32"
_FsIgmpSSMMapStatus_Object = MibScalar
fsIgmpSSMMapStatus = _FsIgmpSSMMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 7, 3),
    _FsIgmpSSMMapStatus_Type()
)
fsIgmpSSMMapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSSMMapStatus.setStatus("current")
_FsIgmpSSMMapGroupTable_Object = MibTable
fsIgmpSSMMapGroupTable = _FsIgmpSSMMapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 8)
)
if mibBuilder.loadTexts:
    fsIgmpSSMMapGroupTable.setStatus("current")
_FsIgmpSSMMapGroupEntry_Object = MibTableRow
fsIgmpSSMMapGroupEntry = _FsIgmpSSMMapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 8, 1)
)
fsIgmpSSMMapGroupEntry.setIndexNames(
    (0, "ARICENT-IGMP-MIB", "fsIgmpSSMMapStartGrpAddress"),
    (0, "ARICENT-IGMP-MIB", "fsIgmpSSMMapEndGrpAddress"),
    (0, "ARICENT-IGMP-MIB", "fsIgmpSSMMapSourceAddress"),
)
if mibBuilder.loadTexts:
    fsIgmpSSMMapGroupEntry.setStatus("current")
_FsIgmpSSMMapStartGrpAddress_Type = IpAddress
_FsIgmpSSMMapStartGrpAddress_Object = MibTableColumn
fsIgmpSSMMapStartGrpAddress = _FsIgmpSSMMapStartGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 8, 1, 1),
    _FsIgmpSSMMapStartGrpAddress_Type()
)
fsIgmpSSMMapStartGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpSSMMapStartGrpAddress.setStatus("current")
_FsIgmpSSMMapEndGrpAddress_Type = IpAddress
_FsIgmpSSMMapEndGrpAddress_Object = MibTableColumn
fsIgmpSSMMapEndGrpAddress = _FsIgmpSSMMapEndGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 8, 1, 2),
    _FsIgmpSSMMapEndGrpAddress_Type()
)
fsIgmpSSMMapEndGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpSSMMapEndGrpAddress.setStatus("current")
_FsIgmpSSMMapSourceAddress_Type = IpAddress
_FsIgmpSSMMapSourceAddress_Object = MibTableColumn
fsIgmpSSMMapSourceAddress = _FsIgmpSSMMapSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 8, 1, 3),
    _FsIgmpSSMMapSourceAddress_Type()
)
fsIgmpSSMMapSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIgmpSSMMapSourceAddress.setStatus("current")
_FsIgmpSSMMapRowStatus_Type = RowStatus
_FsIgmpSSMMapRowStatus_Object = MibTableColumn
fsIgmpSSMMapRowStatus = _FsIgmpSSMMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 36, 1, 8, 1, 4),
    _FsIgmpSSMMapRowStatus_Type()
)
fsIgmpSSMMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSSMMapRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-IGMP-MIB",
    **{"fsigmpMIB": fsigmpMIB,
       "fsigmp": fsigmp,
       "fsIgmpGlobalStatus": fsIgmpGlobalStatus,
       "fsIgmpTraceLevel": fsIgmpTraceLevel,
       "fsIgmpDebugLevel": fsIgmpDebugLevel,
       "fsIgmpInterfaceTable": fsIgmpInterfaceTable,
       "fsIgmpInterfaceEntry": fsIgmpInterfaceEntry,
       "fsIgmpInterfaceIfIndex": fsIgmpInterfaceIfIndex,
       "fsIgmpInterfaceAdminStatus": fsIgmpInterfaceAdminStatus,
       "fsIgmpInterfaceFastLeaveStatus": fsIgmpInterfaceFastLeaveStatus,
       "fsIgmpInterfaceOperStatus": fsIgmpInterfaceOperStatus,
       "fsIgmpInterfaceIncomingPkts": fsIgmpInterfaceIncomingPkts,
       "fsIgmpInterfaceIncomingJoins": fsIgmpInterfaceIncomingJoins,
       "fsIgmpInterfaceIncomingLeaves": fsIgmpInterfaceIncomingLeaves,
       "fsIgmpInterfaceIncomingQueries": fsIgmpInterfaceIncomingQueries,
       "fsIgmpInterfaceOutgoingQueries": fsIgmpInterfaceOutgoingQueries,
       "fsIgmpInterfaceRxGenQueries": fsIgmpInterfaceRxGenQueries,
       "fsIgmpInterfaceRxGrpQueries": fsIgmpInterfaceRxGrpQueries,
       "fsIgmpInterfaceRxGrpAndSrcQueries": fsIgmpInterfaceRxGrpAndSrcQueries,
       "fsIgmpInterfaceRxv1v2Reports": fsIgmpInterfaceRxv1v2Reports,
       "fsIgmpInterfaceRxv3Reports": fsIgmpInterfaceRxv3Reports,
       "fsIgmpInterfaceTxGenQueries": fsIgmpInterfaceTxGenQueries,
       "fsIgmpInterfaceTxGrpQueries": fsIgmpInterfaceTxGrpQueries,
       "fsIgmpInterfaceTxGrpAndSrcQueries": fsIgmpInterfaceTxGrpAndSrcQueries,
       "fsIgmpInterfaceTxv1v2Reports": fsIgmpInterfaceTxv1v2Reports,
       "fsIgmpInterfaceTxv3Reports": fsIgmpInterfaceTxv3Reports,
       "fsIgmpInterfaceTxv2Leaves": fsIgmpInterfaceTxv2Leaves,
       "fsIgmpInterfaceChannelTrackStatus": fsIgmpInterfaceChannelTrackStatus,
       "fsIgmpInterfaceGroupListId": fsIgmpInterfaceGroupListId,
       "fsIgmpInterfaceLimit": fsIgmpInterfaceLimit,
       "fsIgmpInterfaceCurGrpCount": fsIgmpInterfaceCurGrpCount,
       "fsIgmpInterfaceCKSumError": fsIgmpInterfaceCKSumError,
       "fsIgmpInterfacePktLenError": fsIgmpInterfacePktLenError,
       "fsIgmpInterfacePktsWithLocalIP": fsIgmpInterfacePktsWithLocalIP,
       "fsIgmpInterfaceSubnetCheckFailure": fsIgmpInterfaceSubnetCheckFailure,
       "fsIgmpInterfaceQryFromNonQuerier": fsIgmpInterfaceQryFromNonQuerier,
       "fsIgmpInterfaceReportVersionMisMatch": fsIgmpInterfaceReportVersionMisMatch,
       "fsIgmpInterfaceQryVersionMisMatch": fsIgmpInterfaceQryVersionMisMatch,
       "fsIgmpInterfaceUnknownMsgType": fsIgmpInterfaceUnknownMsgType,
       "fsIgmpInterfaceInvalidV1Report": fsIgmpInterfaceInvalidV1Report,
       "fsIgmpInterfaceInvalidV2Report": fsIgmpInterfaceInvalidV2Report,
       "fsIgmpInterfaceInvalidV3Report": fsIgmpInterfaceInvalidV3Report,
       "fsIgmpInterfaceRouterAlertCheckFailure": fsIgmpInterfaceRouterAlertCheckFailure,
       "fsIgmpInterfaceIncomingSSMPkts": fsIgmpInterfaceIncomingSSMPkts,
       "fsIgmpInterfaceInvalidSSMPkts": fsIgmpInterfaceInvalidSSMPkts,
       "fsIgmpInterfaceJoinPktRate": fsIgmpInterfaceJoinPktRate,
       "fsIgmpCacheTable": fsIgmpCacheTable,
       "fsIgmpCacheEntry": fsIgmpCacheEntry,
       "fsIgmpCacheAddress": fsIgmpCacheAddress,
       "fsIgmpCacheIfIndex": fsIgmpCacheIfIndex,
       "fsIgmpCacheGroupCompMode": fsIgmpCacheGroupCompMode,
       "fsIgmpGroupListTable": fsIgmpGroupListTable,
       "fsIgmpGroupListEntry": fsIgmpGroupListEntry,
       "fsIgmpGrpListId": fsIgmpGrpListId,
       "fsIgmpGrpIP": fsIgmpGrpIP,
       "fsIgmpGrpPrefixLen": fsIgmpGrpPrefixLen,
       "fsIgmpGrpListRowStatus": fsIgmpGrpListRowStatus,
       "fsIgmpScalarGroup": fsIgmpScalarGroup,
       "fsIgmpGlobalLimit": fsIgmpGlobalLimit,
       "fsIgmpGlobalCurGrpCount": fsIgmpGlobalCurGrpCount,
       "fsIgmpSSMMapStatus": fsIgmpSSMMapStatus,
       "fsIgmpSSMMapGroupTable": fsIgmpSSMMapGroupTable,
       "fsIgmpSSMMapGroupEntry": fsIgmpSSMMapGroupEntry,
       "fsIgmpSSMMapStartGrpAddress": fsIgmpSSMMapStartGrpAddress,
       "fsIgmpSSMMapEndGrpAddress": fsIgmpSSMMapEndGrpAddress,
       "fsIgmpSSMMapSourceAddress": fsIgmpSSMMapSourceAddress,
       "fsIgmpSSMMapRowStatus": fsIgmpSSMMapRowStatus}
)
