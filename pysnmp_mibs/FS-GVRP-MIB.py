# SNMP MIB module (FS-GVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-GVRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:46 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsGvrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25)
)
if mibBuilder.loadTexts:
    fsGvrpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsGvrpMIBObjects_ObjectIdentity = ObjectIdentity
fsGvrpMIBObjects = _FsGvrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1)
)


class _FsGvrpStatus_Type(EnabledStatus):
    """Custom type fsGvrpStatus based on EnabledStatus"""
    defaultValue = 2


_FsGvrpStatus_Type.__name__ = "EnabledStatus"
_FsGvrpStatus_Object = MibScalar
fsGvrpStatus = _FsGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 1),
    _FsGvrpStatus_Type()
)
fsGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpStatus.setStatus("current")


class _FsGvrpDynamicVlanCreateStauts_Type(EnabledStatus):
    """Custom type fsGvrpDynamicVlanCreateStauts based on EnabledStatus"""
    defaultValue = 2


_FsGvrpDynamicVlanCreateStauts_Type.__name__ = "EnabledStatus"
_FsGvrpDynamicVlanCreateStauts_Object = MibScalar
fsGvrpDynamicVlanCreateStauts = _FsGvrpDynamicVlanCreateStauts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 2),
    _FsGvrpDynamicVlanCreateStauts_Type()
)
fsGvrpDynamicVlanCreateStauts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpDynamicVlanCreateStauts.setStatus("current")


class _FsGvrpJoinTimer_Type(Integer32):
    """Custom type fsGvrpJoinTimer based on Integer32"""
    defaultValue = 200


_FsGvrpJoinTimer_Type.__name__ = "Integer32"
_FsGvrpJoinTimer_Object = MibScalar
fsGvrpJoinTimer = _FsGvrpJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 3),
    _FsGvrpJoinTimer_Type()
)
fsGvrpJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpJoinTimer.setStatus("current")


class _FsGvrpLeaveTimer_Type(Integer32):
    """Custom type fsGvrpLeaveTimer based on Integer32"""
    defaultValue = 600


_FsGvrpLeaveTimer_Type.__name__ = "Integer32"
_FsGvrpLeaveTimer_Object = MibScalar
fsGvrpLeaveTimer = _FsGvrpLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 4),
    _FsGvrpLeaveTimer_Type()
)
fsGvrpLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpLeaveTimer.setStatus("current")


class _FsGvrpLeaveAllTimer_Type(Integer32):
    """Custom type fsGvrpLeaveAllTimer based on Integer32"""
    defaultValue = 10000


_FsGvrpLeaveAllTimer_Type.__name__ = "Integer32"
_FsGvrpLeaveAllTimer_Object = MibScalar
fsGvrpLeaveAllTimer = _FsGvrpLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 5),
    _FsGvrpLeaveAllTimer_Type()
)
fsGvrpLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpLeaveAllTimer.setStatus("current")
_FsGvrpTable_Object = MibTable
fsGvrpTable = _FsGvrpTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 6)
)
if mibBuilder.loadTexts:
    fsGvrpTable.setStatus("current")
_FsGvrpEntry_Object = MibTableRow
fsGvrpEntry = _FsGvrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 6, 1)
)
fsGvrpEntry.setIndexNames(
    (0, "FS-GVRP-MIB", "fsGvrpIfIndex"),
)
if mibBuilder.loadTexts:
    fsGvrpEntry.setStatus("current")
_FsGvrpIfIndex_Type = IfIndex
_FsGvrpIfIndex_Object = MibTableColumn
fsGvrpIfIndex = _FsGvrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 6, 1, 1),
    _FsGvrpIfIndex_Type()
)
fsGvrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsGvrpIfIndex.setStatus("current")


class _FsGvrpRegistrationMode_Type(EnabledStatus):
    """Custom type fsGvrpRegistrationMode based on EnabledStatus"""
    defaultValue = 1


_FsGvrpRegistrationMode_Type.__name__ = "EnabledStatus"
_FsGvrpRegistrationMode_Object = MibTableColumn
fsGvrpRegistrationMode = _FsGvrpRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 6, 1, 2),
    _FsGvrpRegistrationMode_Type()
)
fsGvrpRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpRegistrationMode.setStatus("current")


class _FsGvrpApplicantState_Type(EnabledStatus):
    """Custom type fsGvrpApplicantState based on EnabledStatus"""
    defaultValue = 1


_FsGvrpApplicantState_Type.__name__ = "EnabledStatus"
_FsGvrpApplicantState_Object = MibTableColumn
fsGvrpApplicantState = _FsGvrpApplicantState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 6, 1, 3),
    _FsGvrpApplicantState_Type()
)
fsGvrpApplicantState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpApplicantState.setStatus("current")
_FsGvrpStatsTable_Object = MibTable
fsGvrpStatsTable = _FsGvrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7)
)
if mibBuilder.loadTexts:
    fsGvrpStatsTable.setStatus("current")
_FsGvrpStatsEntry_Object = MibTableRow
fsGvrpStatsEntry = _FsGvrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1)
)
fsGvrpStatsEntry.setIndexNames(
    (0, "FS-GVRP-MIB", "fsGvrpStatsIfIndex"),
)
if mibBuilder.loadTexts:
    fsGvrpStatsEntry.setStatus("current")
_FsGvrpStatsIfIndex_Type = IfIndex
_FsGvrpStatsIfIndex_Object = MibTableColumn
fsGvrpStatsIfIndex = _FsGvrpStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 1),
    _FsGvrpStatsIfIndex_Type()
)
fsGvrpStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsGvrpStatsIfIndex.setStatus("current")
_FsGvrpRecValidGvrpPdu_Type = Counter32
_FsGvrpRecValidGvrpPdu_Object = MibTableColumn
fsGvrpRecValidGvrpPdu = _FsGvrpRecValidGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 2),
    _FsGvrpRecValidGvrpPdu_Type()
)
fsGvrpRecValidGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpRecValidGvrpPdu.setStatus("current")
_FsGvrpRecInvalidGvrpPdu_Type = Counter32
_FsGvrpRecInvalidGvrpPdu_Object = MibTableColumn
fsGvrpRecInvalidGvrpPdu = _FsGvrpRecInvalidGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 3),
    _FsGvrpRecInvalidGvrpPdu_Type()
)
fsGvrpRecInvalidGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpRecInvalidGvrpPdu.setStatus("current")
_FsGvrpRecJoin_Type = Counter32
_FsGvrpRecJoin_Object = MibTableColumn
fsGvrpRecJoin = _FsGvrpRecJoin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 4),
    _FsGvrpRecJoin_Type()
)
fsGvrpRecJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpRecJoin.setStatus("current")
_FsGvrpRecJoinIn_Type = Counter32
_FsGvrpRecJoinIn_Object = MibTableColumn
fsGvrpRecJoinIn = _FsGvrpRecJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 5),
    _FsGvrpRecJoinIn_Type()
)
fsGvrpRecJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpRecJoinIn.setStatus("current")
_FsGvrpRecEmpty_Type = Counter32
_FsGvrpRecEmpty_Object = MibTableColumn
fsGvrpRecEmpty = _FsGvrpRecEmpty_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 6),
    _FsGvrpRecEmpty_Type()
)
fsGvrpRecEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpRecEmpty.setStatus("current")
_FsGvrpRecLeaveEmpty_Type = Counter32
_FsGvrpRecLeaveEmpty_Object = MibTableColumn
fsGvrpRecLeaveEmpty = _FsGvrpRecLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 7),
    _FsGvrpRecLeaveEmpty_Type()
)
fsGvrpRecLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpRecLeaveEmpty.setStatus("current")
_FsGvrpRecLeaveIn_Type = Counter32
_FsGvrpRecLeaveIn_Object = MibTableColumn
fsGvrpRecLeaveIn = _FsGvrpRecLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 8),
    _FsGvrpRecLeaveIn_Type()
)
fsGvrpRecLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpRecLeaveIn.setStatus("current")
_FsGvrpRecLeaveAll_Type = Counter32
_FsGvrpRecLeaveAll_Object = MibTableColumn
fsGvrpRecLeaveAll = _FsGvrpRecLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 9),
    _FsGvrpRecLeaveAll_Type()
)
fsGvrpRecLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpRecLeaveAll.setStatus("current")
_FsGvrpSentGvrpPdu_Type = Counter32
_FsGvrpSentGvrpPdu_Object = MibTableColumn
fsGvrpSentGvrpPdu = _FsGvrpSentGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 10),
    _FsGvrpSentGvrpPdu_Type()
)
fsGvrpSentGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpSentGvrpPdu.setStatus("current")
_FsGvrpSentJoin_Type = Counter32
_FsGvrpSentJoin_Object = MibTableColumn
fsGvrpSentJoin = _FsGvrpSentJoin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 11),
    _FsGvrpSentJoin_Type()
)
fsGvrpSentJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpSentJoin.setStatus("current")
_FsGvrpSentJoinIn_Type = Counter32
_FsGvrpSentJoinIn_Object = MibTableColumn
fsGvrpSentJoinIn = _FsGvrpSentJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 12),
    _FsGvrpSentJoinIn_Type()
)
fsGvrpSentJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpSentJoinIn.setStatus("current")
_FsGvrpSentEmpty_Type = Counter32
_FsGvrpSentEmpty_Object = MibTableColumn
fsGvrpSentEmpty = _FsGvrpSentEmpty_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 13),
    _FsGvrpSentEmpty_Type()
)
fsGvrpSentEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpSentEmpty.setStatus("current")
_FsGvrpSentLeaveEmpty_Type = Counter32
_FsGvrpSentLeaveEmpty_Object = MibTableColumn
fsGvrpSentLeaveEmpty = _FsGvrpSentLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 14),
    _FsGvrpSentLeaveEmpty_Type()
)
fsGvrpSentLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpSentLeaveEmpty.setStatus("current")
_FsGvrpSentLeaveIn_Type = Counter32
_FsGvrpSentLeaveIn_Object = MibTableColumn
fsGvrpSentLeaveIn = _FsGvrpSentLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 15),
    _FsGvrpSentLeaveIn_Type()
)
fsGvrpSentLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpSentLeaveIn.setStatus("current")
_FsGvrpSentLeaveAll_Type = Counter32
_FsGvrpSentLeaveAll_Object = MibTableColumn
fsGvrpSentLeaveAll = _FsGvrpSentLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 16),
    _FsGvrpSentLeaveAll_Type()
)
fsGvrpSentLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpSentLeaveAll.setStatus("current")
_FsGvrpJoinIndicated_Type = Counter32
_FsGvrpJoinIndicated_Object = MibTableColumn
fsGvrpJoinIndicated = _FsGvrpJoinIndicated_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 17),
    _FsGvrpJoinIndicated_Type()
)
fsGvrpJoinIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpJoinIndicated.setStatus("current")
_FsGvrpLeaveIndicated_Type = Counter32
_FsGvrpLeaveIndicated_Object = MibTableColumn
fsGvrpLeaveIndicated = _FsGvrpLeaveIndicated_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 18),
    _FsGvrpLeaveIndicated_Type()
)
fsGvrpLeaveIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpLeaveIndicated.setStatus("current")
_FsGvrpJoinPropagated_Type = Counter32
_FsGvrpJoinPropagated_Object = MibTableColumn
fsGvrpJoinPropagated = _FsGvrpJoinPropagated_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 19),
    _FsGvrpJoinPropagated_Type()
)
fsGvrpJoinPropagated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpJoinPropagated.setStatus("current")
_FsGvrpLeavePropagated_Type = Counter32
_FsGvrpLeavePropagated_Object = MibTableColumn
fsGvrpLeavePropagated = _FsGvrpLeavePropagated_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 20),
    _FsGvrpLeavePropagated_Type()
)
fsGvrpLeavePropagated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGvrpLeavePropagated.setStatus("current")
_FsGvrpStatisticsPortClear_Type = Integer32
_FsGvrpStatisticsPortClear_Object = MibTableColumn
fsGvrpStatisticsPortClear = _FsGvrpStatisticsPortClear_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 7, 1, 21),
    _FsGvrpStatisticsPortClear_Type()
)
fsGvrpStatisticsPortClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpStatisticsPortClear.setStatus("current")


class _FsGvrpOperVid_Type(VlanId):
    """Custom type fsGvrpOperVid based on VlanId"""
    defaultValue = 1


_FsGvrpOperVid_Type.__name__ = "VlanId"
_FsGvrpOperVid_Object = MibScalar
fsGvrpOperVid = _FsGvrpOperVid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 8),
    _FsGvrpOperVid_Type()
)
fsGvrpOperVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpOperVid.setStatus("current")
_FsGvrpStatisticsClear_Type = Integer32
_FsGvrpStatisticsClear_Object = MibScalar
fsGvrpStatisticsClear = _FsGvrpStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 9),
    _FsGvrpStatisticsClear_Type()
)
fsGvrpStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpStatisticsClear.setStatus("current")
_FsGvrpResetTimer_Type = VlanId
_FsGvrpResetTimer_Object = MibScalar
fsGvrpResetTimer = _FsGvrpResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 1, 10),
    _FsGvrpResetTimer_Type()
)
fsGvrpResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGvrpResetTimer.setStatus("current")
_FsGvrpMIBConformance_ObjectIdentity = ObjectIdentity
fsGvrpMIBConformance = _FsGvrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 2)
)
_FsGvrpMIBCompliances_ObjectIdentity = ObjectIdentity
fsGvrpMIBCompliances = _FsGvrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 2, 1)
)
_FsGvrpMIBGroups_ObjectIdentity = ObjectIdentity
fsGvrpMIBGroups = _FsGvrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 2, 2)
)

# Managed Objects groups

fsGvrpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 2, 2, 1)
)
fsGvrpMIBGroup.setObjects(
      *(("FS-GVRP-MIB", "fsGvrpStatus"),
        ("FS-GVRP-MIB", "fsGvrpDynamicVlanCreateStauts"),
        ("FS-GVRP-MIB", "fsGvrpJoinTimer"),
        ("FS-GVRP-MIB", "fsGvrpLeaveTimer"),
        ("FS-GVRP-MIB", "fsGvrpLeaveAllTimer"),
        ("FS-GVRP-MIB", "fsGvrpRegistrationMode"),
        ("FS-GVRP-MIB", "fsGvrpApplicantState"))
)
if mibBuilder.loadTexts:
    fsGvrpMIBGroup.setStatus("current")

fsGvrpStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 2, 2, 2)
)
fsGvrpStatsMIBGroup.setObjects(
      *(("FS-GVRP-MIB", "fsGvrpRecValidGvrpPdu"),
        ("FS-GVRP-MIB", "fsGvrpRecInvalidGvrpPdu"),
        ("FS-GVRP-MIB", "fsGvrpRecJoin"),
        ("FS-GVRP-MIB", "fsGvrpRecJoinIn"),
        ("FS-GVRP-MIB", "fsGvrpRecEmpty"),
        ("FS-GVRP-MIB", "fsGvrpRecLeaveEmpty"),
        ("FS-GVRP-MIB", "fsGvrpRecLeaveIn"),
        ("FS-GVRP-MIB", "fsGvrpRecLeaveAll"),
        ("FS-GVRP-MIB", "fsGvrpSentGvrpPdu"),
        ("FS-GVRP-MIB", "fsGvrpSentJoin"),
        ("FS-GVRP-MIB", "fsGvrpSentJoinIn"),
        ("FS-GVRP-MIB", "fsGvrpSentEmpty"),
        ("FS-GVRP-MIB", "fsGvrpSentLeaveEmpty"),
        ("FS-GVRP-MIB", "fsGvrpSentLeaveIn"),
        ("FS-GVRP-MIB", "fsGvrpSentLeaveAll"),
        ("FS-GVRP-MIB", "fsGvrpJoinIndicated"),
        ("FS-GVRP-MIB", "fsGvrpLeaveIndicated"),
        ("FS-GVRP-MIB", "fsGvrpJoinPropagated"),
        ("FS-GVRP-MIB", "fsGvrpLeavePropagated"),
        ("FS-GVRP-MIB", "fsGvrpStatisticsPortClear"))
)
if mibBuilder.loadTexts:
    fsGvrpStatsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsGvrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 25, 2, 1, 1)
)
fsGvrpMIBCompliance.setObjects(
      *(("FS-GVRP-MIB", "fsGvrpMIBGroup"),
        ("FS-GVRP-MIB", "fsGvrpStatsMIBGroup"))
)
if mibBuilder.loadTexts:
    fsGvrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-GVRP-MIB",
    **{"fsGvrpMIB": fsGvrpMIB,
       "fsGvrpMIBObjects": fsGvrpMIBObjects,
       "fsGvrpStatus": fsGvrpStatus,
       "fsGvrpDynamicVlanCreateStauts": fsGvrpDynamicVlanCreateStauts,
       "fsGvrpJoinTimer": fsGvrpJoinTimer,
       "fsGvrpLeaveTimer": fsGvrpLeaveTimer,
       "fsGvrpLeaveAllTimer": fsGvrpLeaveAllTimer,
       "fsGvrpTable": fsGvrpTable,
       "fsGvrpEntry": fsGvrpEntry,
       "fsGvrpIfIndex": fsGvrpIfIndex,
       "fsGvrpRegistrationMode": fsGvrpRegistrationMode,
       "fsGvrpApplicantState": fsGvrpApplicantState,
       "fsGvrpStatsTable": fsGvrpStatsTable,
       "fsGvrpStatsEntry": fsGvrpStatsEntry,
       "fsGvrpStatsIfIndex": fsGvrpStatsIfIndex,
       "fsGvrpRecValidGvrpPdu": fsGvrpRecValidGvrpPdu,
       "fsGvrpRecInvalidGvrpPdu": fsGvrpRecInvalidGvrpPdu,
       "fsGvrpRecJoin": fsGvrpRecJoin,
       "fsGvrpRecJoinIn": fsGvrpRecJoinIn,
       "fsGvrpRecEmpty": fsGvrpRecEmpty,
       "fsGvrpRecLeaveEmpty": fsGvrpRecLeaveEmpty,
       "fsGvrpRecLeaveIn": fsGvrpRecLeaveIn,
       "fsGvrpRecLeaveAll": fsGvrpRecLeaveAll,
       "fsGvrpSentGvrpPdu": fsGvrpSentGvrpPdu,
       "fsGvrpSentJoin": fsGvrpSentJoin,
       "fsGvrpSentJoinIn": fsGvrpSentJoinIn,
       "fsGvrpSentEmpty": fsGvrpSentEmpty,
       "fsGvrpSentLeaveEmpty": fsGvrpSentLeaveEmpty,
       "fsGvrpSentLeaveIn": fsGvrpSentLeaveIn,
       "fsGvrpSentLeaveAll": fsGvrpSentLeaveAll,
       "fsGvrpJoinIndicated": fsGvrpJoinIndicated,
       "fsGvrpLeaveIndicated": fsGvrpLeaveIndicated,
       "fsGvrpJoinPropagated": fsGvrpJoinPropagated,
       "fsGvrpLeavePropagated": fsGvrpLeavePropagated,
       "fsGvrpStatisticsPortClear": fsGvrpStatisticsPortClear,
       "fsGvrpOperVid": fsGvrpOperVid,
       "fsGvrpStatisticsClear": fsGvrpStatisticsClear,
       "fsGvrpResetTimer": fsGvrpResetTimer,
       "fsGvrpMIBConformance": fsGvrpMIBConformance,
       "fsGvrpMIBCompliances": fsGvrpMIBCompliances,
       "fsGvrpMIBCompliance": fsGvrpMIBCompliance,
       "fsGvrpMIBGroups": fsGvrpMIBGroups,
       "fsGvrpMIBGroup": fsGvrpMIBGroup,
       "fsGvrpStatsMIBGroup": fsGvrpStatsMIBGroup}
)
