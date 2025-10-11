# SNMP MIB module (QTECH-GVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-GVRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:57 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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

qtechGvrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25)
)
if mibBuilder.loadTexts:
    qtechGvrpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechGvrpMIBObjects_ObjectIdentity = ObjectIdentity
qtechGvrpMIBObjects = _QtechGvrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1)
)


class _QtechGvrpStatus_Type(EnabledStatus):
    """Custom type qtechGvrpStatus based on EnabledStatus"""
    defaultValue = 2


_QtechGvrpStatus_Type.__name__ = "EnabledStatus"
_QtechGvrpStatus_Object = MibScalar
qtechGvrpStatus = _QtechGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 1),
    _QtechGvrpStatus_Type()
)
qtechGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpStatus.setStatus("current")


class _QtechGvrpDynamicVlanCreateStauts_Type(EnabledStatus):
    """Custom type qtechGvrpDynamicVlanCreateStauts based on EnabledStatus"""
    defaultValue = 2


_QtechGvrpDynamicVlanCreateStauts_Type.__name__ = "EnabledStatus"
_QtechGvrpDynamicVlanCreateStauts_Object = MibScalar
qtechGvrpDynamicVlanCreateStauts = _QtechGvrpDynamicVlanCreateStauts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 2),
    _QtechGvrpDynamicVlanCreateStauts_Type()
)
qtechGvrpDynamicVlanCreateStauts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpDynamicVlanCreateStauts.setStatus("current")


class _QtechGvrpJoinTimer_Type(Integer32):
    """Custom type qtechGvrpJoinTimer based on Integer32"""
    defaultValue = 200


_QtechGvrpJoinTimer_Type.__name__ = "Integer32"
_QtechGvrpJoinTimer_Object = MibScalar
qtechGvrpJoinTimer = _QtechGvrpJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 3),
    _QtechGvrpJoinTimer_Type()
)
qtechGvrpJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpJoinTimer.setStatus("current")


class _QtechGvrpLeaveTimer_Type(Integer32):
    """Custom type qtechGvrpLeaveTimer based on Integer32"""
    defaultValue = 600


_QtechGvrpLeaveTimer_Type.__name__ = "Integer32"
_QtechGvrpLeaveTimer_Object = MibScalar
qtechGvrpLeaveTimer = _QtechGvrpLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 4),
    _QtechGvrpLeaveTimer_Type()
)
qtechGvrpLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpLeaveTimer.setStatus("current")


class _QtechGvrpLeaveAllTimer_Type(Integer32):
    """Custom type qtechGvrpLeaveAllTimer based on Integer32"""
    defaultValue = 10000


_QtechGvrpLeaveAllTimer_Type.__name__ = "Integer32"
_QtechGvrpLeaveAllTimer_Object = MibScalar
qtechGvrpLeaveAllTimer = _QtechGvrpLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 5),
    _QtechGvrpLeaveAllTimer_Type()
)
qtechGvrpLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpLeaveAllTimer.setStatus("current")
_QtechGvrpTable_Object = MibTable
qtechGvrpTable = _QtechGvrpTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 6)
)
if mibBuilder.loadTexts:
    qtechGvrpTable.setStatus("current")
_QtechGvrpEntry_Object = MibTableRow
qtechGvrpEntry = _QtechGvrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 6, 1)
)
qtechGvrpEntry.setIndexNames(
    (0, "QTECH-GVRP-MIB", "qtechGvrpIfIndex"),
)
if mibBuilder.loadTexts:
    qtechGvrpEntry.setStatus("current")
_QtechGvrpIfIndex_Type = IfIndex
_QtechGvrpIfIndex_Object = MibTableColumn
qtechGvrpIfIndex = _QtechGvrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 6, 1, 1),
    _QtechGvrpIfIndex_Type()
)
qtechGvrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechGvrpIfIndex.setStatus("current")


class _QtechGvrpRegistrationMode_Type(EnabledStatus):
    """Custom type qtechGvrpRegistrationMode based on EnabledStatus"""
    defaultValue = 1


_QtechGvrpRegistrationMode_Type.__name__ = "EnabledStatus"
_QtechGvrpRegistrationMode_Object = MibTableColumn
qtechGvrpRegistrationMode = _QtechGvrpRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 6, 1, 2),
    _QtechGvrpRegistrationMode_Type()
)
qtechGvrpRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpRegistrationMode.setStatus("current")


class _QtechGvrpApplicantState_Type(EnabledStatus):
    """Custom type qtechGvrpApplicantState based on EnabledStatus"""
    defaultValue = 1


_QtechGvrpApplicantState_Type.__name__ = "EnabledStatus"
_QtechGvrpApplicantState_Object = MibTableColumn
qtechGvrpApplicantState = _QtechGvrpApplicantState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 6, 1, 3),
    _QtechGvrpApplicantState_Type()
)
qtechGvrpApplicantState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpApplicantState.setStatus("current")
_QtechGvrpStatsTable_Object = MibTable
qtechGvrpStatsTable = _QtechGvrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7)
)
if mibBuilder.loadTexts:
    qtechGvrpStatsTable.setStatus("current")
_QtechGvrpStatsEntry_Object = MibTableRow
qtechGvrpStatsEntry = _QtechGvrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1)
)
qtechGvrpStatsEntry.setIndexNames(
    (0, "QTECH-GVRP-MIB", "qtechGvrpStatsIfIndex"),
)
if mibBuilder.loadTexts:
    qtechGvrpStatsEntry.setStatus("current")
_QtechGvrpStatsIfIndex_Type = IfIndex
_QtechGvrpStatsIfIndex_Object = MibTableColumn
qtechGvrpStatsIfIndex = _QtechGvrpStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 1),
    _QtechGvrpStatsIfIndex_Type()
)
qtechGvrpStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechGvrpStatsIfIndex.setStatus("current")
_QtechGvrpRecValidGvrpPdu_Type = Counter32
_QtechGvrpRecValidGvrpPdu_Object = MibTableColumn
qtechGvrpRecValidGvrpPdu = _QtechGvrpRecValidGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 2),
    _QtechGvrpRecValidGvrpPdu_Type()
)
qtechGvrpRecValidGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpRecValidGvrpPdu.setStatus("current")
_QtechGvrpRecInvalidGvrpPdu_Type = Counter32
_QtechGvrpRecInvalidGvrpPdu_Object = MibTableColumn
qtechGvrpRecInvalidGvrpPdu = _QtechGvrpRecInvalidGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 3),
    _QtechGvrpRecInvalidGvrpPdu_Type()
)
qtechGvrpRecInvalidGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpRecInvalidGvrpPdu.setStatus("current")
_QtechGvrpRecJoin_Type = Counter32
_QtechGvrpRecJoin_Object = MibTableColumn
qtechGvrpRecJoin = _QtechGvrpRecJoin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 4),
    _QtechGvrpRecJoin_Type()
)
qtechGvrpRecJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpRecJoin.setStatus("current")
_QtechGvrpRecJoinIn_Type = Counter32
_QtechGvrpRecJoinIn_Object = MibTableColumn
qtechGvrpRecJoinIn = _QtechGvrpRecJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 5),
    _QtechGvrpRecJoinIn_Type()
)
qtechGvrpRecJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpRecJoinIn.setStatus("current")
_QtechGvrpRecEmpty_Type = Counter32
_QtechGvrpRecEmpty_Object = MibTableColumn
qtechGvrpRecEmpty = _QtechGvrpRecEmpty_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 6),
    _QtechGvrpRecEmpty_Type()
)
qtechGvrpRecEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpRecEmpty.setStatus("current")
_QtechGvrpRecLeaveEmpty_Type = Counter32
_QtechGvrpRecLeaveEmpty_Object = MibTableColumn
qtechGvrpRecLeaveEmpty = _QtechGvrpRecLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 7),
    _QtechGvrpRecLeaveEmpty_Type()
)
qtechGvrpRecLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpRecLeaveEmpty.setStatus("current")
_QtechGvrpRecLeaveIn_Type = Counter32
_QtechGvrpRecLeaveIn_Object = MibTableColumn
qtechGvrpRecLeaveIn = _QtechGvrpRecLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 8),
    _QtechGvrpRecLeaveIn_Type()
)
qtechGvrpRecLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpRecLeaveIn.setStatus("current")
_QtechGvrpRecLeaveAll_Type = Counter32
_QtechGvrpRecLeaveAll_Object = MibTableColumn
qtechGvrpRecLeaveAll = _QtechGvrpRecLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 9),
    _QtechGvrpRecLeaveAll_Type()
)
qtechGvrpRecLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpRecLeaveAll.setStatus("current")
_QtechGvrpSentGvrpPdu_Type = Counter32
_QtechGvrpSentGvrpPdu_Object = MibTableColumn
qtechGvrpSentGvrpPdu = _QtechGvrpSentGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 10),
    _QtechGvrpSentGvrpPdu_Type()
)
qtechGvrpSentGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpSentGvrpPdu.setStatus("current")
_QtechGvrpSentJoin_Type = Counter32
_QtechGvrpSentJoin_Object = MibTableColumn
qtechGvrpSentJoin = _QtechGvrpSentJoin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 11),
    _QtechGvrpSentJoin_Type()
)
qtechGvrpSentJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpSentJoin.setStatus("current")
_QtechGvrpSentJoinIn_Type = Counter32
_QtechGvrpSentJoinIn_Object = MibTableColumn
qtechGvrpSentJoinIn = _QtechGvrpSentJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 12),
    _QtechGvrpSentJoinIn_Type()
)
qtechGvrpSentJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpSentJoinIn.setStatus("current")
_QtechGvrpSentEmpty_Type = Counter32
_QtechGvrpSentEmpty_Object = MibTableColumn
qtechGvrpSentEmpty = _QtechGvrpSentEmpty_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 13),
    _QtechGvrpSentEmpty_Type()
)
qtechGvrpSentEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpSentEmpty.setStatus("current")
_QtechGvrpSentLeaveEmpty_Type = Counter32
_QtechGvrpSentLeaveEmpty_Object = MibTableColumn
qtechGvrpSentLeaveEmpty = _QtechGvrpSentLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 14),
    _QtechGvrpSentLeaveEmpty_Type()
)
qtechGvrpSentLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpSentLeaveEmpty.setStatus("current")
_QtechGvrpSentLeaveIn_Type = Counter32
_QtechGvrpSentLeaveIn_Object = MibTableColumn
qtechGvrpSentLeaveIn = _QtechGvrpSentLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 15),
    _QtechGvrpSentLeaveIn_Type()
)
qtechGvrpSentLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpSentLeaveIn.setStatus("current")
_QtechGvrpSentLeaveAll_Type = Counter32
_QtechGvrpSentLeaveAll_Object = MibTableColumn
qtechGvrpSentLeaveAll = _QtechGvrpSentLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 16),
    _QtechGvrpSentLeaveAll_Type()
)
qtechGvrpSentLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpSentLeaveAll.setStatus("current")
_QtechGvrpJoinIndicated_Type = Counter32
_QtechGvrpJoinIndicated_Object = MibTableColumn
qtechGvrpJoinIndicated = _QtechGvrpJoinIndicated_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 17),
    _QtechGvrpJoinIndicated_Type()
)
qtechGvrpJoinIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpJoinIndicated.setStatus("current")
_QtechGvrpLeaveIndicated_Type = Counter32
_QtechGvrpLeaveIndicated_Object = MibTableColumn
qtechGvrpLeaveIndicated = _QtechGvrpLeaveIndicated_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 18),
    _QtechGvrpLeaveIndicated_Type()
)
qtechGvrpLeaveIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpLeaveIndicated.setStatus("current")
_QtechGvrpJoinPropagated_Type = Counter32
_QtechGvrpJoinPropagated_Object = MibTableColumn
qtechGvrpJoinPropagated = _QtechGvrpJoinPropagated_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 19),
    _QtechGvrpJoinPropagated_Type()
)
qtechGvrpJoinPropagated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpJoinPropagated.setStatus("current")
_QtechGvrpLeavePropagated_Type = Counter32
_QtechGvrpLeavePropagated_Object = MibTableColumn
qtechGvrpLeavePropagated = _QtechGvrpLeavePropagated_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 20),
    _QtechGvrpLeavePropagated_Type()
)
qtechGvrpLeavePropagated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechGvrpLeavePropagated.setStatus("current")
_QtechGvrpStatisticsPortClear_Type = Integer32
_QtechGvrpStatisticsPortClear_Object = MibTableColumn
qtechGvrpStatisticsPortClear = _QtechGvrpStatisticsPortClear_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 7, 1, 21),
    _QtechGvrpStatisticsPortClear_Type()
)
qtechGvrpStatisticsPortClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpStatisticsPortClear.setStatus("current")


class _QtechGvrpOperVid_Type(VlanId):
    """Custom type qtechGvrpOperVid based on VlanId"""
    defaultValue = 1


_QtechGvrpOperVid_Type.__name__ = "VlanId"
_QtechGvrpOperVid_Object = MibScalar
qtechGvrpOperVid = _QtechGvrpOperVid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 8),
    _QtechGvrpOperVid_Type()
)
qtechGvrpOperVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpOperVid.setStatus("current")
_QtechGvrpStatisticsClear_Type = Integer32
_QtechGvrpStatisticsClear_Object = MibScalar
qtechGvrpStatisticsClear = _QtechGvrpStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 9),
    _QtechGvrpStatisticsClear_Type()
)
qtechGvrpStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpStatisticsClear.setStatus("current")
_QtechGvrpResetTimer_Type = VlanId
_QtechGvrpResetTimer_Object = MibScalar
qtechGvrpResetTimer = _QtechGvrpResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 1, 10),
    _QtechGvrpResetTimer_Type()
)
qtechGvrpResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGvrpResetTimer.setStatus("current")
_QtechGvrpMIBConformance_ObjectIdentity = ObjectIdentity
qtechGvrpMIBConformance = _QtechGvrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 2)
)
_QtechGvrpMIBCompliances_ObjectIdentity = ObjectIdentity
qtechGvrpMIBCompliances = _QtechGvrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 2, 1)
)
_QtechGvrpMIBGroups_ObjectIdentity = ObjectIdentity
qtechGvrpMIBGroups = _QtechGvrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 2, 2)
)

# Managed Objects groups

qtechGvrpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 2, 2, 1)
)
qtechGvrpMIBGroup.setObjects(
      *(("QTECH-GVRP-MIB", "qtechGvrpStatus"),
        ("QTECH-GVRP-MIB", "qtechGvrpDynamicVlanCreateStauts"),
        ("QTECH-GVRP-MIB", "qtechGvrpJoinTimer"),
        ("QTECH-GVRP-MIB", "qtechGvrpLeaveTimer"),
        ("QTECH-GVRP-MIB", "qtechGvrpLeaveAllTimer"),
        ("QTECH-GVRP-MIB", "qtechGvrpRegistrationMode"),
        ("QTECH-GVRP-MIB", "qtechGvrpApplicantState"))
)
if mibBuilder.loadTexts:
    qtechGvrpMIBGroup.setStatus("current")

qtechGvrpStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 2, 2, 2)
)
qtechGvrpStatsMIBGroup.setObjects(
      *(("QTECH-GVRP-MIB", "qtechGvrpRecValidGvrpPdu"),
        ("QTECH-GVRP-MIB", "qtechGvrpRecInvalidGvrpPdu"),
        ("QTECH-GVRP-MIB", "qtechGvrpRecJoin"),
        ("QTECH-GVRP-MIB", "qtechGvrpRecJoinIn"),
        ("QTECH-GVRP-MIB", "qtechGvrpRecEmpty"),
        ("QTECH-GVRP-MIB", "qtechGvrpRecLeaveEmpty"),
        ("QTECH-GVRP-MIB", "qtechGvrpRecLeaveIn"),
        ("QTECH-GVRP-MIB", "qtechGvrpRecLeaveAll"),
        ("QTECH-GVRP-MIB", "qtechGvrpSentGvrpPdu"),
        ("QTECH-GVRP-MIB", "qtechGvrpSentJoin"),
        ("QTECH-GVRP-MIB", "qtechGvrpSentJoinIn"),
        ("QTECH-GVRP-MIB", "qtechGvrpSentEmpty"),
        ("QTECH-GVRP-MIB", "qtechGvrpSentLeaveEmpty"),
        ("QTECH-GVRP-MIB", "qtechGvrpSentLeaveIn"),
        ("QTECH-GVRP-MIB", "qtechGvrpSentLeaveAll"),
        ("QTECH-GVRP-MIB", "qtechGvrpJoinIndicated"),
        ("QTECH-GVRP-MIB", "qtechGvrpLeaveIndicated"),
        ("QTECH-GVRP-MIB", "qtechGvrpJoinPropagated"),
        ("QTECH-GVRP-MIB", "qtechGvrpLeavePropagated"),
        ("QTECH-GVRP-MIB", "qtechGvrpStatisticsPortClear"))
)
if mibBuilder.loadTexts:
    qtechGvrpStatsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechGvrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 25, 2, 1, 1)
)
qtechGvrpMIBCompliance.setObjects(
      *(("QTECH-GVRP-MIB", "qtechGvrpMIBGroup"),
        ("QTECH-GVRP-MIB", "qtechGvrpStatsMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechGvrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-GVRP-MIB",
    **{"qtechGvrpMIB": qtechGvrpMIB,
       "qtechGvrpMIBObjects": qtechGvrpMIBObjects,
       "qtechGvrpStatus": qtechGvrpStatus,
       "qtechGvrpDynamicVlanCreateStauts": qtechGvrpDynamicVlanCreateStauts,
       "qtechGvrpJoinTimer": qtechGvrpJoinTimer,
       "qtechGvrpLeaveTimer": qtechGvrpLeaveTimer,
       "qtechGvrpLeaveAllTimer": qtechGvrpLeaveAllTimer,
       "qtechGvrpTable": qtechGvrpTable,
       "qtechGvrpEntry": qtechGvrpEntry,
       "qtechGvrpIfIndex": qtechGvrpIfIndex,
       "qtechGvrpRegistrationMode": qtechGvrpRegistrationMode,
       "qtechGvrpApplicantState": qtechGvrpApplicantState,
       "qtechGvrpStatsTable": qtechGvrpStatsTable,
       "qtechGvrpStatsEntry": qtechGvrpStatsEntry,
       "qtechGvrpStatsIfIndex": qtechGvrpStatsIfIndex,
       "qtechGvrpRecValidGvrpPdu": qtechGvrpRecValidGvrpPdu,
       "qtechGvrpRecInvalidGvrpPdu": qtechGvrpRecInvalidGvrpPdu,
       "qtechGvrpRecJoin": qtechGvrpRecJoin,
       "qtechGvrpRecJoinIn": qtechGvrpRecJoinIn,
       "qtechGvrpRecEmpty": qtechGvrpRecEmpty,
       "qtechGvrpRecLeaveEmpty": qtechGvrpRecLeaveEmpty,
       "qtechGvrpRecLeaveIn": qtechGvrpRecLeaveIn,
       "qtechGvrpRecLeaveAll": qtechGvrpRecLeaveAll,
       "qtechGvrpSentGvrpPdu": qtechGvrpSentGvrpPdu,
       "qtechGvrpSentJoin": qtechGvrpSentJoin,
       "qtechGvrpSentJoinIn": qtechGvrpSentJoinIn,
       "qtechGvrpSentEmpty": qtechGvrpSentEmpty,
       "qtechGvrpSentLeaveEmpty": qtechGvrpSentLeaveEmpty,
       "qtechGvrpSentLeaveIn": qtechGvrpSentLeaveIn,
       "qtechGvrpSentLeaveAll": qtechGvrpSentLeaveAll,
       "qtechGvrpJoinIndicated": qtechGvrpJoinIndicated,
       "qtechGvrpLeaveIndicated": qtechGvrpLeaveIndicated,
       "qtechGvrpJoinPropagated": qtechGvrpJoinPropagated,
       "qtechGvrpLeavePropagated": qtechGvrpLeavePropagated,
       "qtechGvrpStatisticsPortClear": qtechGvrpStatisticsPortClear,
       "qtechGvrpOperVid": qtechGvrpOperVid,
       "qtechGvrpStatisticsClear": qtechGvrpStatisticsClear,
       "qtechGvrpResetTimer": qtechGvrpResetTimer,
       "qtechGvrpMIBConformance": qtechGvrpMIBConformance,
       "qtechGvrpMIBCompliances": qtechGvrpMIBCompliances,
       "qtechGvrpMIBCompliance": qtechGvrpMIBCompliance,
       "qtechGvrpMIBGroups": qtechGvrpMIBGroups,
       "qtechGvrpMIBGroup": qtechGvrpMIBGroup,
       "qtechGvrpStatsMIBGroup": qtechGvrpStatsMIBGroup}
)
