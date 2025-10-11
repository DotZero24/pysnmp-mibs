# SNMP MIB module (MY-GVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-GVRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:25 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

(myVlanMIBObjects,) = mibBuilder.importSymbols(
    "MY-VLAN-MIB",
    "myVlanMIBObjects")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myGvrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25)
)
if mibBuilder.loadTexts:
    myGvrpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyVlanIfStateTable_Object = MibTable
myVlanIfStateTable = _MyVlanIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6)
)
if mibBuilder.loadTexts:
    myVlanIfStateTable.setStatus("current")
_MyVlanIfStateEntry_Object = MibTableRow
myVlanIfStateEntry = _MyVlanIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1)
)
myVlanIfStateEntry.setIndexNames(
    (0, "MY-GVRP-MIB", "myVlanIfStateVid"),
    (0, "MY-GVRP-MIB", "myVlanIfStateIndex"),
)
if mibBuilder.loadTexts:
    myVlanIfStateEntry.setStatus("current")
_MyVlanIfStateVid_Type = VlanId
_MyVlanIfStateVid_Object = MibTableColumn
myVlanIfStateVid = _MyVlanIfStateVid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1, 1),
    _MyVlanIfStateVid_Type()
)
myVlanIfStateVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myVlanIfStateVid.setStatus("current")
_MyVlanIfStateIndex_Type = IfIndex
_MyVlanIfStateIndex_Object = MibTableColumn
myVlanIfStateIndex = _MyVlanIfStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1, 2),
    _MyVlanIfStateIndex_Type()
)
myVlanIfStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myVlanIfStateIndex.setStatus("current")


class _MyVlanIfState_Type(Integer32):
    """Custom type myVlanIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_MyVlanIfState_Type.__name__ = "Integer32"
_MyVlanIfState_Object = MibTableColumn
myVlanIfState = _MyVlanIfState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1, 3),
    _MyVlanIfState_Type()
)
myVlanIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanIfState.setStatus("current")
_MyVlanDynTable_Object = MibTable
myVlanDynTable = _MyVlanDynTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7)
)
if mibBuilder.loadTexts:
    myVlanDynTable.setStatus("current")
_MyVlanDynEntry_Object = MibTableRow
myVlanDynEntry = _MyVlanDynEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1)
)
myVlanDynEntry.setIndexNames(
    (0, "MY-GVRP-MIB", "myVlanDynVID"),
)
if mibBuilder.loadTexts:
    myVlanDynEntry.setStatus("current")
_MyVlanDynVID_Type = VlanId
_MyVlanDynVID_Object = MibTableColumn
myVlanDynVID = _MyVlanDynVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1, 1),
    _MyVlanDynVID_Type()
)
myVlanDynVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanDynVID.setStatus("current")
_MyVlanDynPortMemberAction_Type = MemberMap
_MyVlanDynPortMemberAction_Object = MibTableColumn
myVlanDynPortMemberAction = _MyVlanDynPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1, 2),
    _MyVlanDynPortMemberAction_Type()
)
myVlanDynPortMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanDynPortMemberAction.setStatus("current")
_MyVlanDynApMemberAction_Type = MemberMap
_MyVlanDynApMemberAction_Object = MibTableColumn
myVlanDynApMemberAction = _MyVlanDynApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1, 3),
    _MyVlanDynApMemberAction_Type()
)
myVlanDynApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanDynApMemberAction.setStatus("current")


class _MyVlanDynAlias_Type(DisplayString):
    """Custom type myVlanDynAlias based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyVlanDynAlias_Type.__name__ = "DisplayString"
_MyVlanDynAlias_Object = MibTableColumn
myVlanDynAlias = _MyVlanDynAlias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1, 4),
    _MyVlanDynAlias_Type()
)
myVlanDynAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanDynAlias.setStatus("current")
_MyVlanDynEntryStatus_Type = ConfigStatus
_MyVlanDynEntryStatus_Object = MibTableColumn
myVlanDynEntryStatus = _MyVlanDynEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1, 5),
    _MyVlanDynEntryStatus_Type()
)
myVlanDynEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanDynEntryStatus.setStatus("current")
_MyGvrpMIBObjects_ObjectIdentity = ObjectIdentity
myGvrpMIBObjects = _MyGvrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1)
)


class _MyGvrpStatus_Type(EnabledStatus):
    """Custom type myGvrpStatus based on EnabledStatus"""
    defaultValue = 2


_MyGvrpStatus_Type.__name__ = "EnabledStatus"
_MyGvrpStatus_Object = MibScalar
myGvrpStatus = _MyGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 1),
    _MyGvrpStatus_Type()
)
myGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpStatus.setStatus("current")


class _MyGvrpDynamicVlanCreateStauts_Type(EnabledStatus):
    """Custom type myGvrpDynamicVlanCreateStauts based on EnabledStatus"""
    defaultValue = 2


_MyGvrpDynamicVlanCreateStauts_Type.__name__ = "EnabledStatus"
_MyGvrpDynamicVlanCreateStauts_Object = MibScalar
myGvrpDynamicVlanCreateStauts = _MyGvrpDynamicVlanCreateStauts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 2),
    _MyGvrpDynamicVlanCreateStauts_Type()
)
myGvrpDynamicVlanCreateStauts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpDynamicVlanCreateStauts.setStatus("current")


class _MyGvrpJoinTimer_Type(Integer32):
    """Custom type myGvrpJoinTimer based on Integer32"""
    defaultValue = 200


_MyGvrpJoinTimer_Type.__name__ = "Integer32"
_MyGvrpJoinTimer_Object = MibScalar
myGvrpJoinTimer = _MyGvrpJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 3),
    _MyGvrpJoinTimer_Type()
)
myGvrpJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpJoinTimer.setStatus("current")


class _MyGvrpLeaveTimer_Type(Integer32):
    """Custom type myGvrpLeaveTimer based on Integer32"""
    defaultValue = 600


_MyGvrpLeaveTimer_Type.__name__ = "Integer32"
_MyGvrpLeaveTimer_Object = MibScalar
myGvrpLeaveTimer = _MyGvrpLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 4),
    _MyGvrpLeaveTimer_Type()
)
myGvrpLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpLeaveTimer.setStatus("current")


class _MyGvrpLeaveAllTimer_Type(Integer32):
    """Custom type myGvrpLeaveAllTimer based on Integer32"""
    defaultValue = 10000


_MyGvrpLeaveAllTimer_Type.__name__ = "Integer32"
_MyGvrpLeaveAllTimer_Object = MibScalar
myGvrpLeaveAllTimer = _MyGvrpLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 5),
    _MyGvrpLeaveAllTimer_Type()
)
myGvrpLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpLeaveAllTimer.setStatus("current")
_MyGvrpTable_Object = MibTable
myGvrpTable = _MyGvrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6)
)
if mibBuilder.loadTexts:
    myGvrpTable.setStatus("current")
_MyGvrpEntry_Object = MibTableRow
myGvrpEntry = _MyGvrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6, 1)
)
myGvrpEntry.setIndexNames(
    (0, "MY-GVRP-MIB", "myGvrpIfIndex"),
)
if mibBuilder.loadTexts:
    myGvrpEntry.setStatus("current")
_MyGvrpIfIndex_Type = IfIndex
_MyGvrpIfIndex_Object = MibTableColumn
myGvrpIfIndex = _MyGvrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6, 1, 1),
    _MyGvrpIfIndex_Type()
)
myGvrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myGvrpIfIndex.setStatus("current")


class _MyGvrpRegistrationMode_Type(EnabledStatus):
    """Custom type myGvrpRegistrationMode based on EnabledStatus"""
    defaultValue = 1


_MyGvrpRegistrationMode_Type.__name__ = "EnabledStatus"
_MyGvrpRegistrationMode_Object = MibTableColumn
myGvrpRegistrationMode = _MyGvrpRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6, 1, 2),
    _MyGvrpRegistrationMode_Type()
)
myGvrpRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpRegistrationMode.setStatus("current")


class _MyGvrpApplicantState_Type(EnabledStatus):
    """Custom type myGvrpApplicantState based on EnabledStatus"""
    defaultValue = 1


_MyGvrpApplicantState_Type.__name__ = "EnabledStatus"
_MyGvrpApplicantState_Object = MibTableColumn
myGvrpApplicantState = _MyGvrpApplicantState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6, 1, 3),
    _MyGvrpApplicantState_Type()
)
myGvrpApplicantState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpApplicantState.setStatus("current")
_MyGvrpStatsTable_Object = MibTable
myGvrpStatsTable = _MyGvrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7)
)
if mibBuilder.loadTexts:
    myGvrpStatsTable.setStatus("current")
_MyGvrpStatsEntry_Object = MibTableRow
myGvrpStatsEntry = _MyGvrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1)
)
myGvrpStatsEntry.setIndexNames(
    (0, "MY-GVRP-MIB", "myGvrpStatsIfIndex"),
)
if mibBuilder.loadTexts:
    myGvrpStatsEntry.setStatus("current")
_MyGvrpStatsIfIndex_Type = IfIndex
_MyGvrpStatsIfIndex_Object = MibTableColumn
myGvrpStatsIfIndex = _MyGvrpStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 1),
    _MyGvrpStatsIfIndex_Type()
)
myGvrpStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myGvrpStatsIfIndex.setStatus("current")
_MyGvrpRecValidGvrpPdu_Type = Counter32
_MyGvrpRecValidGvrpPdu_Object = MibTableColumn
myGvrpRecValidGvrpPdu = _MyGvrpRecValidGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 2),
    _MyGvrpRecValidGvrpPdu_Type()
)
myGvrpRecValidGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpRecValidGvrpPdu.setStatus("current")
_MyGvrpRecInvalidGvrpPdu_Type = Counter32
_MyGvrpRecInvalidGvrpPdu_Object = MibTableColumn
myGvrpRecInvalidGvrpPdu = _MyGvrpRecInvalidGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 3),
    _MyGvrpRecInvalidGvrpPdu_Type()
)
myGvrpRecInvalidGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpRecInvalidGvrpPdu.setStatus("current")
_MyGvrpRecJoin_Type = Counter32
_MyGvrpRecJoin_Object = MibTableColumn
myGvrpRecJoin = _MyGvrpRecJoin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 4),
    _MyGvrpRecJoin_Type()
)
myGvrpRecJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpRecJoin.setStatus("current")
_MyGvrpRecJoinIn_Type = Counter32
_MyGvrpRecJoinIn_Object = MibTableColumn
myGvrpRecJoinIn = _MyGvrpRecJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 5),
    _MyGvrpRecJoinIn_Type()
)
myGvrpRecJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpRecJoinIn.setStatus("current")
_MyGvrpRecEmpty_Type = Counter32
_MyGvrpRecEmpty_Object = MibTableColumn
myGvrpRecEmpty = _MyGvrpRecEmpty_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 6),
    _MyGvrpRecEmpty_Type()
)
myGvrpRecEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpRecEmpty.setStatus("current")
_MyGvrpRecLeaveEmpty_Type = Counter32
_MyGvrpRecLeaveEmpty_Object = MibTableColumn
myGvrpRecLeaveEmpty = _MyGvrpRecLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 7),
    _MyGvrpRecLeaveEmpty_Type()
)
myGvrpRecLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpRecLeaveEmpty.setStatus("current")
_MyGvrpRecLeaveIn_Type = Counter32
_MyGvrpRecLeaveIn_Object = MibTableColumn
myGvrpRecLeaveIn = _MyGvrpRecLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 8),
    _MyGvrpRecLeaveIn_Type()
)
myGvrpRecLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpRecLeaveIn.setStatus("current")
_MyGvrpRecLeaveAll_Type = Counter32
_MyGvrpRecLeaveAll_Object = MibTableColumn
myGvrpRecLeaveAll = _MyGvrpRecLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 9),
    _MyGvrpRecLeaveAll_Type()
)
myGvrpRecLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpRecLeaveAll.setStatus("current")
_MyGvrpSentGvrpPdu_Type = Counter32
_MyGvrpSentGvrpPdu_Object = MibTableColumn
myGvrpSentGvrpPdu = _MyGvrpSentGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 10),
    _MyGvrpSentGvrpPdu_Type()
)
myGvrpSentGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpSentGvrpPdu.setStatus("current")
_MyGvrpSentJoin_Type = Counter32
_MyGvrpSentJoin_Object = MibTableColumn
myGvrpSentJoin = _MyGvrpSentJoin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 11),
    _MyGvrpSentJoin_Type()
)
myGvrpSentJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpSentJoin.setStatus("current")
_MyGvrpSentJoinIn_Type = Counter32
_MyGvrpSentJoinIn_Object = MibTableColumn
myGvrpSentJoinIn = _MyGvrpSentJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 12),
    _MyGvrpSentJoinIn_Type()
)
myGvrpSentJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpSentJoinIn.setStatus("current")
_MyGvrpSentEmpty_Type = Counter32
_MyGvrpSentEmpty_Object = MibTableColumn
myGvrpSentEmpty = _MyGvrpSentEmpty_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 13),
    _MyGvrpSentEmpty_Type()
)
myGvrpSentEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpSentEmpty.setStatus("current")
_MyGvrpSentLeaveEmpty_Type = Counter32
_MyGvrpSentLeaveEmpty_Object = MibTableColumn
myGvrpSentLeaveEmpty = _MyGvrpSentLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 14),
    _MyGvrpSentLeaveEmpty_Type()
)
myGvrpSentLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpSentLeaveEmpty.setStatus("current")
_MyGvrpSentLeaveIn_Type = Counter32
_MyGvrpSentLeaveIn_Object = MibTableColumn
myGvrpSentLeaveIn = _MyGvrpSentLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 15),
    _MyGvrpSentLeaveIn_Type()
)
myGvrpSentLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpSentLeaveIn.setStatus("current")
_MyGvrpSentLeaveAll_Type = Counter32
_MyGvrpSentLeaveAll_Object = MibTableColumn
myGvrpSentLeaveAll = _MyGvrpSentLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 16),
    _MyGvrpSentLeaveAll_Type()
)
myGvrpSentLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpSentLeaveAll.setStatus("current")
_MyGvrpJoinIndicated_Type = Counter32
_MyGvrpJoinIndicated_Object = MibTableColumn
myGvrpJoinIndicated = _MyGvrpJoinIndicated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 17),
    _MyGvrpJoinIndicated_Type()
)
myGvrpJoinIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpJoinIndicated.setStatus("current")
_MyGvrpLeaveIndicated_Type = Counter32
_MyGvrpLeaveIndicated_Object = MibTableColumn
myGvrpLeaveIndicated = _MyGvrpLeaveIndicated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 18),
    _MyGvrpLeaveIndicated_Type()
)
myGvrpLeaveIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpLeaveIndicated.setStatus("current")
_MyGvrpJoinPropagated_Type = Counter32
_MyGvrpJoinPropagated_Object = MibTableColumn
myGvrpJoinPropagated = _MyGvrpJoinPropagated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 19),
    _MyGvrpJoinPropagated_Type()
)
myGvrpJoinPropagated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpJoinPropagated.setStatus("current")
_MyGvrpLeavePropagated_Type = Counter32
_MyGvrpLeavePropagated_Object = MibTableColumn
myGvrpLeavePropagated = _MyGvrpLeavePropagated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 20),
    _MyGvrpLeavePropagated_Type()
)
myGvrpLeavePropagated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myGvrpLeavePropagated.setStatus("current")
_MyGvrpStatisticsPortClear_Type = Integer32
_MyGvrpStatisticsPortClear_Object = MibTableColumn
myGvrpStatisticsPortClear = _MyGvrpStatisticsPortClear_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 21),
    _MyGvrpStatisticsPortClear_Type()
)
myGvrpStatisticsPortClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpStatisticsPortClear.setStatus("current")


class _MyGvrpOperVid_Type(VlanId):
    """Custom type myGvrpOperVid based on VlanId"""
    defaultValue = 1


_MyGvrpOperVid_Type.__name__ = "VlanId"
_MyGvrpOperVid_Object = MibScalar
myGvrpOperVid = _MyGvrpOperVid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 8),
    _MyGvrpOperVid_Type()
)
myGvrpOperVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpOperVid.setStatus("current")
_MyGvrpStatisticsClear_Type = Integer32
_MyGvrpStatisticsClear_Object = MibScalar
myGvrpStatisticsClear = _MyGvrpStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 9),
    _MyGvrpStatisticsClear_Type()
)
myGvrpStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpStatisticsClear.setStatus("current")
_MyGvrpResetTimer_Type = VlanId
_MyGvrpResetTimer_Object = MibScalar
myGvrpResetTimer = _MyGvrpResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 10),
    _MyGvrpResetTimer_Type()
)
myGvrpResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myGvrpResetTimer.setStatus("current")
_MyGvrpMIBConformance_ObjectIdentity = ObjectIdentity
myGvrpMIBConformance = _MyGvrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2)
)
_MyGvrpMIBCompliances_ObjectIdentity = ObjectIdentity
myGvrpMIBCompliances = _MyGvrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 1)
)
_MyGvrpMIBGroups_ObjectIdentity = ObjectIdentity
myGvrpMIBGroups = _MyGvrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 2)
)

# Managed Objects groups

myGvrpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 2, 1)
)
myGvrpMIBGroup.setObjects(
      *(("MY-GVRP-MIB", "myGvrpStatus"),
        ("MY-GVRP-MIB", "myGvrpDynamicVlanCreateStauts"),
        ("MY-GVRP-MIB", "myGvrpJoinTimer"),
        ("MY-GVRP-MIB", "myGvrpLeaveTimer"),
        ("MY-GVRP-MIB", "myGvrpLeaveAllTimer"),
        ("MY-GVRP-MIB", "myGvrpIfIndex"),
        ("MY-GVRP-MIB", "myGvrpRegistrationMode"),
        ("MY-GVRP-MIB", "myGvrpApplicantState"),
        ("MY-GVRP-MIB", "myVlanIfStateVid"),
        ("MY-GVRP-MIB", "myVlanIfStateIndex"),
        ("MY-GVRP-MIB", "myVlanIfState"))
)
if mibBuilder.loadTexts:
    myGvrpMIBGroup.setStatus("current")

myGvrpStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 2, 2)
)
myGvrpStatsMIBGroup.setObjects(
      *(("MY-GVRP-MIB", "myGvrpStatsIfIndex"),
        ("MY-GVRP-MIB", "myGvrpRecValidGvrpPdu"),
        ("MY-GVRP-MIB", "myGvrpRecInvalidGvrpPdu"),
        ("MY-GVRP-MIB", "myGvrpRecJoin"),
        ("MY-GVRP-MIB", "myGvrpRecJoinIn"),
        ("MY-GVRP-MIB", "myGvrpRecEmpty"),
        ("MY-GVRP-MIB", "myGvrpRecLeaveEmpty"),
        ("MY-GVRP-MIB", "myGvrpRecLeaveIn"),
        ("MY-GVRP-MIB", "myGvrpRecLeaveAll"),
        ("MY-GVRP-MIB", "myGvrpSentGvrpPdu"),
        ("MY-GVRP-MIB", "myGvrpSentJoin"),
        ("MY-GVRP-MIB", "myGvrpSentJoinIn"),
        ("MY-GVRP-MIB", "myGvrpSentEmpty"),
        ("MY-GVRP-MIB", "myGvrpSentLeaveEmpty"),
        ("MY-GVRP-MIB", "myGvrpSentLeaveIn"),
        ("MY-GVRP-MIB", "myGvrpSentLeaveAll"),
        ("MY-GVRP-MIB", "myGvrpJoinIndicated"),
        ("MY-GVRP-MIB", "myGvrpLeaveIndicated"),
        ("MY-GVRP-MIB", "myGvrpJoinPropagated"),
        ("MY-GVRP-MIB", "myGvrpLeavePropagated"),
        ("MY-GVRP-MIB", "myGvrpStatisticsPortClear"))
)
if mibBuilder.loadTexts:
    myGvrpStatsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myGvrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 1, 1)
)
myGvrpMIBCompliance.setObjects(
      *(("MY-GVRP-MIB", "myGvrpMIBGroup"),
        ("MY-GVRP-MIB", "myGvrpStatsMIBGroup"))
)
if mibBuilder.loadTexts:
    myGvrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-GVRP-MIB",
    **{"myVlanIfStateTable": myVlanIfStateTable,
       "myVlanIfStateEntry": myVlanIfStateEntry,
       "myVlanIfStateVid": myVlanIfStateVid,
       "myVlanIfStateIndex": myVlanIfStateIndex,
       "myVlanIfState": myVlanIfState,
       "myVlanDynTable": myVlanDynTable,
       "myVlanDynEntry": myVlanDynEntry,
       "myVlanDynVID": myVlanDynVID,
       "myVlanDynPortMemberAction": myVlanDynPortMemberAction,
       "myVlanDynApMemberAction": myVlanDynApMemberAction,
       "myVlanDynAlias": myVlanDynAlias,
       "myVlanDynEntryStatus": myVlanDynEntryStatus,
       "myGvrpMIB": myGvrpMIB,
       "myGvrpMIBObjects": myGvrpMIBObjects,
       "myGvrpStatus": myGvrpStatus,
       "myGvrpDynamicVlanCreateStauts": myGvrpDynamicVlanCreateStauts,
       "myGvrpJoinTimer": myGvrpJoinTimer,
       "myGvrpLeaveTimer": myGvrpLeaveTimer,
       "myGvrpLeaveAllTimer": myGvrpLeaveAllTimer,
       "myGvrpTable": myGvrpTable,
       "myGvrpEntry": myGvrpEntry,
       "myGvrpIfIndex": myGvrpIfIndex,
       "myGvrpRegistrationMode": myGvrpRegistrationMode,
       "myGvrpApplicantState": myGvrpApplicantState,
       "myGvrpStatsTable": myGvrpStatsTable,
       "myGvrpStatsEntry": myGvrpStatsEntry,
       "myGvrpStatsIfIndex": myGvrpStatsIfIndex,
       "myGvrpRecValidGvrpPdu": myGvrpRecValidGvrpPdu,
       "myGvrpRecInvalidGvrpPdu": myGvrpRecInvalidGvrpPdu,
       "myGvrpRecJoin": myGvrpRecJoin,
       "myGvrpRecJoinIn": myGvrpRecJoinIn,
       "myGvrpRecEmpty": myGvrpRecEmpty,
       "myGvrpRecLeaveEmpty": myGvrpRecLeaveEmpty,
       "myGvrpRecLeaveIn": myGvrpRecLeaveIn,
       "myGvrpRecLeaveAll": myGvrpRecLeaveAll,
       "myGvrpSentGvrpPdu": myGvrpSentGvrpPdu,
       "myGvrpSentJoin": myGvrpSentJoin,
       "myGvrpSentJoinIn": myGvrpSentJoinIn,
       "myGvrpSentEmpty": myGvrpSentEmpty,
       "myGvrpSentLeaveEmpty": myGvrpSentLeaveEmpty,
       "myGvrpSentLeaveIn": myGvrpSentLeaveIn,
       "myGvrpSentLeaveAll": myGvrpSentLeaveAll,
       "myGvrpJoinIndicated": myGvrpJoinIndicated,
       "myGvrpLeaveIndicated": myGvrpLeaveIndicated,
       "myGvrpJoinPropagated": myGvrpJoinPropagated,
       "myGvrpLeavePropagated": myGvrpLeavePropagated,
       "myGvrpStatisticsPortClear": myGvrpStatisticsPortClear,
       "myGvrpOperVid": myGvrpOperVid,
       "myGvrpStatisticsClear": myGvrpStatisticsClear,
       "myGvrpResetTimer": myGvrpResetTimer,
       "myGvrpMIBConformance": myGvrpMIBConformance,
       "myGvrpMIBCompliances": myGvrpMIBCompliances,
       "myGvrpMIBCompliance": myGvrpMIBCompliance,
       "myGvrpMIBGroups": myGvrpMIBGroups,
       "myGvrpMIBGroup": myGvrpMIBGroup,
       "myGvrpStatsMIBGroup": myGvrpStatsMIBGroup}
)
