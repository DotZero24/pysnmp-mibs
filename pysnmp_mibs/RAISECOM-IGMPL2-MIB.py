# SNMP MIB module (RAISECOM-IGMPL2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-IGMPL2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:47 2025
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

(VlanId,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIndex")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

(EnableVar,
 PortList,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList",
    "Vlanset")


# MODULE-IDENTITY

raisecomIgmpL2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomIgmpL2Notifications_ObjectIdentity = ObjectIdentity
raisecomIgmpL2Notifications = _RaisecomIgmpL2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 1)
)
_RaisecomIgmpL2Objects_ObjectIdentity = ObjectIdentity
raisecomIgmpL2Objects = _RaisecomIgmpL2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2)
)
_RaisecomIgmpBase_ObjectIdentity = ObjectIdentity
raisecomIgmpBase = _RaisecomIgmpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1)
)
_RaisecomIgmpBaseScalar_ObjectIdentity = ObjectIdentity
raisecomIgmpBaseScalar = _RaisecomIgmpBaseScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 1)
)


class _RaisecomIgmpAging_Type(Integer32):
    """Custom type raisecomIgmpAging based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RaisecomIgmpAging_Type.__name__ = "Integer32"
_RaisecomIgmpAging_Object = MibScalar
raisecomIgmpAging = _RaisecomIgmpAging_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 1, 1),
    _RaisecomIgmpAging_Type()
)
raisecomIgmpAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpAging.setStatus("current")
_RaisecomIgmpRingPortList_Type = PortList
_RaisecomIgmpRingPortList_Object = MibScalar
raisecomIgmpRingPortList = _RaisecomIgmpRingPortList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 1, 2),
    _RaisecomIgmpRingPortList_Type()
)
raisecomIgmpRingPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpRingPortList.setStatus("current")
_RaisecomIgmpImmediateLeaveTable_Object = MibTable
raisecomIgmpImmediateLeaveTable = _RaisecomIgmpImmediateLeaveTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomIgmpImmediateLeaveTable.setStatus("current")
_RaisecomIgmpImmediateLeaveEntry_Object = MibTableRow
raisecomIgmpImmediateLeaveEntry = _RaisecomIgmpImmediateLeaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 2, 1)
)
raisecomIgmpImmediateLeaveEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpImmediateLeavePort"),
)
if mibBuilder.loadTexts:
    raisecomIgmpImmediateLeaveEntry.setStatus("current")
_RaisecomIgmpImmediateLeavePort_Type = Integer32
_RaisecomIgmpImmediateLeavePort_Object = MibTableColumn
raisecomIgmpImmediateLeavePort = _RaisecomIgmpImmediateLeavePort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 2, 1, 1),
    _RaisecomIgmpImmediateLeavePort_Type()
)
raisecomIgmpImmediateLeavePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpImmediateLeavePort.setStatus("current")
_RaisecomIgmpImmediateLeaveType_Type = Integer32
_RaisecomIgmpImmediateLeaveType_Object = MibTableColumn
raisecomIgmpImmediateLeaveType = _RaisecomIgmpImmediateLeaveType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 2, 1, 2),
    _RaisecomIgmpImmediateLeaveType_Type()
)
raisecomIgmpImmediateLeaveType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpImmediateLeaveType.setStatus("current")
_RaisecomIgmpImmediateLeaveVlanList_Type = Vlanset
_RaisecomIgmpImmediateLeaveVlanList_Object = MibTableColumn
raisecomIgmpImmediateLeaveVlanList = _RaisecomIgmpImmediateLeaveVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 2, 1, 3),
    _RaisecomIgmpImmediateLeaveVlanList_Type()
)
raisecomIgmpImmediateLeaveVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpImmediateLeaveVlanList.setStatus("current")
_RaisecomIgmpImmediateLeaveRowStatus_Type = RowStatus
_RaisecomIgmpImmediateLeaveRowStatus_Object = MibTableColumn
raisecomIgmpImmediateLeaveRowStatus = _RaisecomIgmpImmediateLeaveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 2, 1, 4),
    _RaisecomIgmpImmediateLeaveRowStatus_Type()
)
raisecomIgmpImmediateLeaveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpImmediateLeaveRowStatus.setStatus("current")
_RaisecomIgmpMrouterTable_Object = MibTable
raisecomIgmpMrouterTable = _RaisecomIgmpMrouterTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 3)
)
if mibBuilder.loadTexts:
    raisecomIgmpMrouterTable.setStatus("current")
_RaisecomIgmpMrouterEntry_Object = MibTableRow
raisecomIgmpMrouterEntry = _RaisecomIgmpMrouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 3, 1)
)
raisecomIgmpMrouterEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpMrouterPort"),
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpMrouterVlan"),
)
if mibBuilder.loadTexts:
    raisecomIgmpMrouterEntry.setStatus("current")
_RaisecomIgmpMrouterPort_Type = Integer32
_RaisecomIgmpMrouterPort_Object = MibTableColumn
raisecomIgmpMrouterPort = _RaisecomIgmpMrouterPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 3, 1, 1),
    _RaisecomIgmpMrouterPort_Type()
)
raisecomIgmpMrouterPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpMrouterPort.setStatus("current")
_RaisecomIgmpMrouterVlan_Type = VlanIndex
_RaisecomIgmpMrouterVlan_Object = MibTableColumn
raisecomIgmpMrouterVlan = _RaisecomIgmpMrouterVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 3, 1, 2),
    _RaisecomIgmpMrouterVlan_Type()
)
raisecomIgmpMrouterVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpMrouterVlan.setStatus("current")


class _RaisecomIgmpMrouterLiveTime_Type(Integer32):
    """Custom type raisecomIgmpMrouterLiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RaisecomIgmpMrouterLiveTime_Type.__name__ = "Integer32"
_RaisecomIgmpMrouterLiveTime_Object = MibTableColumn
raisecomIgmpMrouterLiveTime = _RaisecomIgmpMrouterLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 3, 1, 3),
    _RaisecomIgmpMrouterLiveTime_Type()
)
raisecomIgmpMrouterLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpMrouterLiveTime.setStatus("current")
_RaisecomIgmpMrouterMRStatus_Type = Integer32
_RaisecomIgmpMrouterMRStatus_Object = MibTableColumn
raisecomIgmpMrouterMRStatus = _RaisecomIgmpMrouterMRStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 3, 1, 4),
    _RaisecomIgmpMrouterMRStatus_Type()
)
raisecomIgmpMrouterMRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpMrouterMRStatus.setStatus("current")
_RaisecomIgmpMrouterRowStatus_Type = RowStatus
_RaisecomIgmpMrouterRowStatus_Object = MibTableColumn
raisecomIgmpMrouterRowStatus = _RaisecomIgmpMrouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 3, 1, 5),
    _RaisecomIgmpMrouterRowStatus_Type()
)
raisecomIgmpMrouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpMrouterRowStatus.setStatus("current")
_RaisecomIgmpMemberTable_Object = MibTable
raisecomIgmpMemberTable = _RaisecomIgmpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4)
)
if mibBuilder.loadTexts:
    raisecomIgmpMemberTable.setStatus("current")
_RaisecomIgmpMemberEntry_Object = MibTableRow
raisecomIgmpMemberEntry = _RaisecomIgmpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4, 1)
)
raisecomIgmpMemberEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpMemberPort"),
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpMemberUserVlan"),
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpMemberGroupIpType"),
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpMemberGroup"),
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpMemberMVlan"),
)
if mibBuilder.loadTexts:
    raisecomIgmpMemberEntry.setStatus("current")
_RaisecomIgmpMemberPort_Type = Integer32
_RaisecomIgmpMemberPort_Object = MibTableColumn
raisecomIgmpMemberPort = _RaisecomIgmpMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4, 1, 1),
    _RaisecomIgmpMemberPort_Type()
)
raisecomIgmpMemberPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpMemberPort.setStatus("current")
_RaisecomIgmpMemberUserVlan_Type = VlanIndex
_RaisecomIgmpMemberUserVlan_Object = MibTableColumn
raisecomIgmpMemberUserVlan = _RaisecomIgmpMemberUserVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4, 1, 2),
    _RaisecomIgmpMemberUserVlan_Type()
)
raisecomIgmpMemberUserVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpMemberUserVlan.setStatus("current")
_RaisecomIgmpMemberGroupIpType_Type = InetAddressType
_RaisecomIgmpMemberGroupIpType_Object = MibTableColumn
raisecomIgmpMemberGroupIpType = _RaisecomIgmpMemberGroupIpType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4, 1, 3),
    _RaisecomIgmpMemberGroupIpType_Type()
)
raisecomIgmpMemberGroupIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpMemberGroupIpType.setStatus("current")
_RaisecomIgmpMemberGroup_Type = InetAddress
_RaisecomIgmpMemberGroup_Object = MibTableColumn
raisecomIgmpMemberGroup = _RaisecomIgmpMemberGroup_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4, 1, 4),
    _RaisecomIgmpMemberGroup_Type()
)
raisecomIgmpMemberGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpMemberGroup.setStatus("current")
_RaisecomIgmpMemberMVlan_Type = Integer32
_RaisecomIgmpMemberMVlan_Object = MibTableColumn
raisecomIgmpMemberMVlan = _RaisecomIgmpMemberMVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4, 1, 5),
    _RaisecomIgmpMemberMVlan_Type()
)
raisecomIgmpMemberMVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpMemberMVlan.setStatus("current")


class _RaisecomIgmpMemberLiveTime_Type(Integer32):
    """Custom type raisecomIgmpMemberLiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RaisecomIgmpMemberLiveTime_Type.__name__ = "Integer32"
_RaisecomIgmpMemberLiveTime_Object = MibTableColumn
raisecomIgmpMemberLiveTime = _RaisecomIgmpMemberLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4, 1, 6),
    _RaisecomIgmpMemberLiveTime_Type()
)
raisecomIgmpMemberLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpMemberLiveTime.setStatus("current")
_RaisecomIgmpMemberSource_Type = Integer32
_RaisecomIgmpMemberSource_Object = MibTableColumn
raisecomIgmpMemberSource = _RaisecomIgmpMemberSource_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4, 1, 7),
    _RaisecomIgmpMemberSource_Type()
)
raisecomIgmpMemberSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpMemberSource.setStatus("current")
_RaisecomIgmpMemberRowStatus_Type = RowStatus
_RaisecomIgmpMemberRowStatus_Object = MibTableColumn
raisecomIgmpMemberRowStatus = _RaisecomIgmpMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 4, 1, 8),
    _RaisecomIgmpMemberRowStatus_Type()
)
raisecomIgmpMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpMemberRowStatus.setStatus("current")
_RaisecomIgmpPortStatisticsTable_Object = MibTable
raisecomIgmpPortStatisticsTable = _RaisecomIgmpPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5)
)
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsTable.setStatus("current")
_RaisecomIgmpPortStatisticsEntry_Object = MibTableRow
raisecomIgmpPortStatisticsEntry = _RaisecomIgmpPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1)
)
raisecomIgmpPortStatisticsEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpPortStatisticsPortNum"),
)
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsEntry.setStatus("current")
_RaisecomIgmpPortStatisticsPortNum_Type = Integer32
_RaisecomIgmpPortStatisticsPortNum_Object = MibTableColumn
raisecomIgmpPortStatisticsPortNum = _RaisecomIgmpPortStatisticsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 1),
    _RaisecomIgmpPortStatisticsPortNum_Type()
)
raisecomIgmpPortStatisticsPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsPortNum.setStatus("current")


class _RaisecomIgmpPortStatisticsClear_Type(Integer32):
    """Custom type raisecomIgmpPortStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("read", 0),
          ("clear", 1))
    )


_RaisecomIgmpPortStatisticsClear_Type.__name__ = "Integer32"
_RaisecomIgmpPortStatisticsClear_Object = MibTableColumn
raisecomIgmpPortStatisticsClear = _RaisecomIgmpPortStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 2),
    _RaisecomIgmpPortStatisticsClear_Type()
)
raisecomIgmpPortStatisticsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsClear.setStatus("current")
_RaisecomIgmpPortStatisticsRecvQuery_Type = Counter32
_RaisecomIgmpPortStatisticsRecvQuery_Object = MibTableColumn
raisecomIgmpPortStatisticsRecvQuery = _RaisecomIgmpPortStatisticsRecvQuery_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 3),
    _RaisecomIgmpPortStatisticsRecvQuery_Type()
)
raisecomIgmpPortStatisticsRecvQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsRecvQuery.setStatus("current")
_RaisecomIgmpPortStatisticsRecvReport_Type = Counter32
_RaisecomIgmpPortStatisticsRecvReport_Object = MibTableColumn
raisecomIgmpPortStatisticsRecvReport = _RaisecomIgmpPortStatisticsRecvReport_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 4),
    _RaisecomIgmpPortStatisticsRecvReport_Type()
)
raisecomIgmpPortStatisticsRecvReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsRecvReport.setStatus("current")
_RaisecomIgmpPortStatisticsRecvLeave_Type = Counter32
_RaisecomIgmpPortStatisticsRecvLeave_Object = MibTableColumn
raisecomIgmpPortStatisticsRecvLeave = _RaisecomIgmpPortStatisticsRecvLeave_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 5),
    _RaisecomIgmpPortStatisticsRecvLeave_Type()
)
raisecomIgmpPortStatisticsRecvLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsRecvLeave.setStatus("current")
_RaisecomIgmpPortStatisticsFilterDropQuery_Type = Counter32
_RaisecomIgmpPortStatisticsFilterDropQuery_Object = MibTableColumn
raisecomIgmpPortStatisticsFilterDropQuery = _RaisecomIgmpPortStatisticsFilterDropQuery_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 6),
    _RaisecomIgmpPortStatisticsFilterDropQuery_Type()
)
raisecomIgmpPortStatisticsFilterDropQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsFilterDropQuery.setStatus("current")
_RaisecomIgmpPortStatisticsFilterDropReport_Type = Counter32
_RaisecomIgmpPortStatisticsFilterDropReport_Object = MibTableColumn
raisecomIgmpPortStatisticsFilterDropReport = _RaisecomIgmpPortStatisticsFilterDropReport_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 7),
    _RaisecomIgmpPortStatisticsFilterDropReport_Type()
)
raisecomIgmpPortStatisticsFilterDropReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsFilterDropReport.setStatus("current")
_RaisecomIgmpPortStatisticsFilterDropLeave_Type = Counter32
_RaisecomIgmpPortStatisticsFilterDropLeave_Object = MibTableColumn
raisecomIgmpPortStatisticsFilterDropLeave = _RaisecomIgmpPortStatisticsFilterDropLeave_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 8),
    _RaisecomIgmpPortStatisticsFilterDropLeave_Type()
)
raisecomIgmpPortStatisticsFilterDropLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsFilterDropLeave.setStatus("current")
_RaisecomIgmpPortStatisticsSnoopDealQuery_Type = Counter32
_RaisecomIgmpPortStatisticsSnoopDealQuery_Object = MibTableColumn
raisecomIgmpPortStatisticsSnoopDealQuery = _RaisecomIgmpPortStatisticsSnoopDealQuery_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 9),
    _RaisecomIgmpPortStatisticsSnoopDealQuery_Type()
)
raisecomIgmpPortStatisticsSnoopDealQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsSnoopDealQuery.setStatus("current")
_RaisecomIgmpPortStatisticsSnoopDealReport_Type = Counter32
_RaisecomIgmpPortStatisticsSnoopDealReport_Object = MibTableColumn
raisecomIgmpPortStatisticsSnoopDealReport = _RaisecomIgmpPortStatisticsSnoopDealReport_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 10),
    _RaisecomIgmpPortStatisticsSnoopDealReport_Type()
)
raisecomIgmpPortStatisticsSnoopDealReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsSnoopDealReport.setStatus("current")
_RaisecomIgmpPortStatisticsSnoopDealLeave_Type = Counter32
_RaisecomIgmpPortStatisticsSnoopDealLeave_Object = MibTableColumn
raisecomIgmpPortStatisticsSnoopDealLeave = _RaisecomIgmpPortStatisticsSnoopDealLeave_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 11),
    _RaisecomIgmpPortStatisticsSnoopDealLeave_Type()
)
raisecomIgmpPortStatisticsSnoopDealLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsSnoopDealLeave.setStatus("current")
_RaisecomIgmpPortStatisticsMvrDealQuery_Type = Counter32
_RaisecomIgmpPortStatisticsMvrDealQuery_Object = MibTableColumn
raisecomIgmpPortStatisticsMvrDealQuery = _RaisecomIgmpPortStatisticsMvrDealQuery_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 12),
    _RaisecomIgmpPortStatisticsMvrDealQuery_Type()
)
raisecomIgmpPortStatisticsMvrDealQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsMvrDealQuery.setStatus("current")
_RaisecomIgmpPortStatisticsMvrDealReport_Type = Counter32
_RaisecomIgmpPortStatisticsMvrDealReport_Object = MibTableColumn
raisecomIgmpPortStatisticsMvrDealReport = _RaisecomIgmpPortStatisticsMvrDealReport_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 13),
    _RaisecomIgmpPortStatisticsMvrDealReport_Type()
)
raisecomIgmpPortStatisticsMvrDealReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsMvrDealReport.setStatus("current")
_RaisecomIgmpPortStatisticsMvrDealLeave_Type = Counter32
_RaisecomIgmpPortStatisticsMvrDealLeave_Object = MibTableColumn
raisecomIgmpPortStatisticsMvrDealLeave = _RaisecomIgmpPortStatisticsMvrDealLeave_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 14),
    _RaisecomIgmpPortStatisticsMvrDealLeave_Type()
)
raisecomIgmpPortStatisticsMvrDealLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsMvrDealLeave.setStatus("current")
_RaisecomIgmpPortStatisticsVlanCPDealQuery_Type = Counter32
_RaisecomIgmpPortStatisticsVlanCPDealQuery_Object = MibTableColumn
raisecomIgmpPortStatisticsVlanCPDealQuery = _RaisecomIgmpPortStatisticsVlanCPDealQuery_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 15),
    _RaisecomIgmpPortStatisticsVlanCPDealQuery_Type()
)
raisecomIgmpPortStatisticsVlanCPDealQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsVlanCPDealQuery.setStatus("current")
_RaisecomIgmpPortStatisticsVlanCPDealReport_Type = Counter32
_RaisecomIgmpPortStatisticsVlanCPDealReport_Object = MibTableColumn
raisecomIgmpPortStatisticsVlanCPDealReport = _RaisecomIgmpPortStatisticsVlanCPDealReport_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 16),
    _RaisecomIgmpPortStatisticsVlanCPDealReport_Type()
)
raisecomIgmpPortStatisticsVlanCPDealReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsVlanCPDealReport.setStatus("current")
_RaisecomIgmpPortStatisticsVlanCPDealLeave_Type = Counter32
_RaisecomIgmpPortStatisticsVlanCPDealLeave_Object = MibTableColumn
raisecomIgmpPortStatisticsVlanCPDealLeave = _RaisecomIgmpPortStatisticsVlanCPDealLeave_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 17),
    _RaisecomIgmpPortStatisticsVlanCPDealLeave_Type()
)
raisecomIgmpPortStatisticsVlanCPDealLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsVlanCPDealLeave.setStatus("current")
_RaisecomIgmpPortStatisticsReplaceCount_Type = Counter32
_RaisecomIgmpPortStatisticsReplaceCount_Object = MibTableColumn
raisecomIgmpPortStatisticsReplaceCount = _RaisecomIgmpPortStatisticsReplaceCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 1, 5, 1, 18),
    _RaisecomIgmpPortStatisticsReplaceCount_Type()
)
raisecomIgmpPortStatisticsReplaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpPortStatisticsReplaceCount.setStatus("current")
_RaisecomIgmpSnooping_ObjectIdentity = ObjectIdentity
raisecomIgmpSnooping = _RaisecomIgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 2)
)
_RaisecomIgmpSnoopingScalar_ObjectIdentity = ObjectIdentity
raisecomIgmpSnoopingScalar = _RaisecomIgmpSnoopingScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 2, 1)
)


class _RaisecomIgmpSnoopingEnable_Type(EnableVar):
    """Custom type raisecomIgmpSnoopingEnable based on EnableVar"""
    defaultValue = 2


_RaisecomIgmpSnoopingEnable_Type.__name__ = "EnableVar"
_RaisecomIgmpSnoopingEnable_Object = MibScalar
raisecomIgmpSnoopingEnable = _RaisecomIgmpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 2, 1, 1),
    _RaisecomIgmpSnoopingEnable_Type()
)
raisecomIgmpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpSnoopingEnable.setStatus("current")
_RaisecomIgmpSnoopingEnableVlanList_Type = Vlanset
_RaisecomIgmpSnoopingEnableVlanList_Object = MibScalar
raisecomIgmpSnoopingEnableVlanList = _RaisecomIgmpSnoopingEnableVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 2, 1, 2),
    _RaisecomIgmpSnoopingEnableVlanList_Type()
)
raisecomIgmpSnoopingEnableVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpSnoopingEnableVlanList.setStatus("current")


class _RaisecomIgmpAuthRadiusEnable_Type(EnableVar):
    """Custom type raisecomIgmpAuthRadiusEnable based on EnableVar"""
    defaultValue = 2


_RaisecomIgmpAuthRadiusEnable_Type.__name__ = "EnableVar"
_RaisecomIgmpAuthRadiusEnable_Object = MibScalar
raisecomIgmpAuthRadiusEnable = _RaisecomIgmpAuthRadiusEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 2, 1, 3),
    _RaisecomIgmpAuthRadiusEnable_Type()
)
raisecomIgmpAuthRadiusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpAuthRadiusEnable.setStatus("current")
_RaisecomIgmpAuthRadiusPortEnable_Type = PortList
_RaisecomIgmpAuthRadiusPortEnable_Object = MibScalar
raisecomIgmpAuthRadiusPortEnable = _RaisecomIgmpAuthRadiusPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 2, 1, 4),
    _RaisecomIgmpAuthRadiusPortEnable_Type()
)
raisecomIgmpAuthRadiusPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpAuthRadiusPortEnable.setStatus("current")
_RaisecomIgmpMvr_ObjectIdentity = ObjectIdentity
raisecomIgmpMvr = _RaisecomIgmpMvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3)
)
_RaisecomIgmpMvrScalar_ObjectIdentity = ObjectIdentity
raisecomIgmpMvrScalar = _RaisecomIgmpMvrScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3, 1)
)


class _RaisecomIgmpMvrEnable_Type(EnableVar):
    """Custom type raisecomIgmpMvrEnable based on EnableVar"""
    defaultValue = 2


_RaisecomIgmpMvrEnable_Type.__name__ = "EnableVar"
_RaisecomIgmpMvrEnable_Object = MibScalar
raisecomIgmpMvrEnable = _RaisecomIgmpMvrEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3, 1, 1),
    _RaisecomIgmpMvrEnable_Type()
)
raisecomIgmpMvrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpMvrEnable.setStatus("current")
_RaisecomIgmpMvrEnablePortList_Type = PortList
_RaisecomIgmpMvrEnablePortList_Object = MibScalar
raisecomIgmpMvrEnablePortList = _RaisecomIgmpMvrEnablePortList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3, 1, 2),
    _RaisecomIgmpMvrEnablePortList_Type()
)
raisecomIgmpMvrEnablePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpMvrEnablePortList.setStatus("current")
_RaisecomIgmpMvrMVlanGroupTable_Object = MibTable
raisecomIgmpMvrMVlanGroupTable = _RaisecomIgmpMvrMVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3, 2)
)
if mibBuilder.loadTexts:
    raisecomIgmpMvrMVlanGroupTable.setStatus("current")
_RaisecomIgmpMvrMVlanGroupEntry_Object = MibTableRow
raisecomIgmpMvrMVlanGroupEntry = _RaisecomIgmpMvrMVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3, 2, 1)
)
raisecomIgmpMvrMVlanGroupEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpMvrGroupIpType"),
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpMvrGroup"),
)
if mibBuilder.loadTexts:
    raisecomIgmpMvrMVlanGroupEntry.setStatus("current")
_RaisecomIgmpMvrGroupIpType_Type = InetAddressType
_RaisecomIgmpMvrGroupIpType_Object = MibTableColumn
raisecomIgmpMvrGroupIpType = _RaisecomIgmpMvrGroupIpType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3, 2, 1, 1),
    _RaisecomIgmpMvrGroupIpType_Type()
)
raisecomIgmpMvrGroupIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpMvrGroupIpType.setStatus("current")
_RaisecomIgmpMvrGroup_Type = InetAddress
_RaisecomIgmpMvrGroup_Object = MibTableColumn
raisecomIgmpMvrGroup = _RaisecomIgmpMvrGroup_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3, 2, 1, 2),
    _RaisecomIgmpMvrGroup_Type()
)
raisecomIgmpMvrGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpMvrGroup.setStatus("current")
_RaisecomIgmpMvrMVlan_Type = VlanId
_RaisecomIgmpMvrMVlan_Object = MibTableColumn
raisecomIgmpMvrMVlan = _RaisecomIgmpMvrMVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3, 2, 1, 3),
    _RaisecomIgmpMvrMVlan_Type()
)
raisecomIgmpMvrMVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpMvrMVlan.setStatus("current")
_RaisecomIgmpMvrGroupRowStatus_Type = RowStatus
_RaisecomIgmpMvrGroupRowStatus_Object = MibTableColumn
raisecomIgmpMvrGroupRowStatus = _RaisecomIgmpMvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 3, 2, 1, 4),
    _RaisecomIgmpMvrGroupRowStatus_Type()
)
raisecomIgmpMvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpMvrGroupRowStatus.setStatus("current")
_RaisecomIgmpVlanCopy_ObjectIdentity = ObjectIdentity
raisecomIgmpVlanCopy = _RaisecomIgmpVlanCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4)
)
_RaisecomIgmpVlanCopyScalar_ObjectIdentity = ObjectIdentity
raisecomIgmpVlanCopyScalar = _RaisecomIgmpVlanCopyScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4, 1)
)


class _RaisecomIgmpVlanCopyEnable_Type(EnableVar):
    """Custom type raisecomIgmpVlanCopyEnable based on EnableVar"""
    defaultValue = 2


_RaisecomIgmpVlanCopyEnable_Type.__name__ = "EnableVar"
_RaisecomIgmpVlanCopyEnable_Object = MibScalar
raisecomIgmpVlanCopyEnable = _RaisecomIgmpVlanCopyEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4, 1, 1),
    _RaisecomIgmpVlanCopyEnable_Type()
)
raisecomIgmpVlanCopyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyEnable.setStatus("current")
_RaisecomIgmpVlanCopyEnablePortList_Type = PortList
_RaisecomIgmpVlanCopyEnablePortList_Object = MibScalar
raisecomIgmpVlanCopyEnablePortList = _RaisecomIgmpVlanCopyEnablePortList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4, 1, 2),
    _RaisecomIgmpVlanCopyEnablePortList_Type()
)
raisecomIgmpVlanCopyEnablePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyEnablePortList.setStatus("current")
_RaisecomIgmpVlanCopyVlanGroupTable_Object = MibTable
raisecomIgmpVlanCopyVlanGroupTable = _RaisecomIgmpVlanCopyVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4, 2)
)
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyVlanGroupTable.setStatus("current")
_RaisecomIgmpVlanCopyVlanGroupEntry_Object = MibTableRow
raisecomIgmpVlanCopyVlanGroupEntry = _RaisecomIgmpVlanCopyVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4, 2, 1)
)
raisecomIgmpVlanCopyVlanGroupEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpVlanCopyGroupIpType"),
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpVlanCopyGroup"),
)
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyVlanGroupEntry.setStatus("current")
_RaisecomIgmpVlanCopyGroupIpType_Type = InetAddressType
_RaisecomIgmpVlanCopyGroupIpType_Object = MibTableColumn
raisecomIgmpVlanCopyGroupIpType = _RaisecomIgmpVlanCopyGroupIpType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4, 2, 1, 1),
    _RaisecomIgmpVlanCopyGroupIpType_Type()
)
raisecomIgmpVlanCopyGroupIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyGroupIpType.setStatus("current")
_RaisecomIgmpVlanCopyGroup_Type = InetAddress
_RaisecomIgmpVlanCopyGroup_Object = MibTableColumn
raisecomIgmpVlanCopyGroup = _RaisecomIgmpVlanCopyGroup_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4, 2, 1, 2),
    _RaisecomIgmpVlanCopyGroup_Type()
)
raisecomIgmpVlanCopyGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyGroup.setStatus("current")
_RaisecomIgmpVlanCopyMcastVlan_Type = VlanId
_RaisecomIgmpVlanCopyMcastVlan_Object = MibTableColumn
raisecomIgmpVlanCopyMcastVlan = _RaisecomIgmpVlanCopyMcastVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4, 2, 1, 3),
    _RaisecomIgmpVlanCopyMcastVlan_Type()
)
raisecomIgmpVlanCopyMcastVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyMcastVlan.setStatus("current")
_RaisecomIgmpVlanCopyGroupRowStatus_Type = RowStatus
_RaisecomIgmpVlanCopyGroupRowStatus_Object = MibTableColumn
raisecomIgmpVlanCopyGroupRowStatus = _RaisecomIgmpVlanCopyGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 4, 2, 1, 4),
    _RaisecomIgmpVlanCopyGroupRowStatus_Type()
)
raisecomIgmpVlanCopyGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpVlanCopyGroupRowStatus.setStatus("current")
_RaisecomIgmpProxy_ObjectIdentity = ObjectIdentity
raisecomIgmpProxy = _RaisecomIgmpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5)
)
_RaisecomIgmpProxyScalar_ObjectIdentity = ObjectIdentity
raisecomIgmpProxyScalar = _RaisecomIgmpProxyScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5, 1)
)


class _RaisecomIgmpProxyEnable_Type(EnableVar):
    """Custom type raisecomIgmpProxyEnable based on EnableVar"""
    defaultValue = 2


_RaisecomIgmpProxyEnable_Type.__name__ = "EnableVar"
_RaisecomIgmpProxyEnable_Object = MibScalar
raisecomIgmpProxyEnable = _RaisecomIgmpProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5, 1, 1),
    _RaisecomIgmpProxyEnable_Type()
)
raisecomIgmpProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpProxyEnable.setStatus("current")


class _RaisecomIgmpProxySuppressionEnable_Type(EnableVar):
    """Custom type raisecomIgmpProxySuppressionEnable based on EnableVar"""
    defaultValue = 2


_RaisecomIgmpProxySuppressionEnable_Type.__name__ = "EnableVar"
_RaisecomIgmpProxySuppressionEnable_Object = MibScalar
raisecomIgmpProxySuppressionEnable = _RaisecomIgmpProxySuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5, 1, 2),
    _RaisecomIgmpProxySuppressionEnable_Type()
)
raisecomIgmpProxySuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpProxySuppressionEnable.setStatus("current")


class _RaisecomIgmpProxyQuerierEnable_Type(EnableVar):
    """Custom type raisecomIgmpProxyQuerierEnable based on EnableVar"""
    defaultValue = 2


_RaisecomIgmpProxyQuerierEnable_Type.__name__ = "EnableVar"
_RaisecomIgmpProxyQuerierEnable_Object = MibScalar
raisecomIgmpProxyQuerierEnable = _RaisecomIgmpProxyQuerierEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5, 1, 3),
    _RaisecomIgmpProxyQuerierEnable_Type()
)
raisecomIgmpProxyQuerierEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpProxyQuerierEnable.setStatus("current")


class _RaisecomIgmpProxySourceIpType_Type(InetAddressType):
    """Custom type raisecomIgmpProxySourceIpType based on InetAddressType"""
    defaultValue = 1


_RaisecomIgmpProxySourceIpType_Type.__name__ = "InetAddressType"
_RaisecomIgmpProxySourceIpType_Object = MibScalar
raisecomIgmpProxySourceIpType = _RaisecomIgmpProxySourceIpType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5, 1, 4),
    _RaisecomIgmpProxySourceIpType_Type()
)
raisecomIgmpProxySourceIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpProxySourceIpType.setStatus("current")
_RaisecomIgmpProxySourceIpAddress_Type = InetAddress
_RaisecomIgmpProxySourceIpAddress_Object = MibScalar
raisecomIgmpProxySourceIpAddress = _RaisecomIgmpProxySourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5, 1, 5),
    _RaisecomIgmpProxySourceIpAddress_Type()
)
raisecomIgmpProxySourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpProxySourceIpAddress.setStatus("current")


class _RaisecomIgmpProxyQueryInterval_Type(Integer32):
    """Custom type raisecomIgmpProxyQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_RaisecomIgmpProxyQueryInterval_Type.__name__ = "Integer32"
_RaisecomIgmpProxyQueryInterval_Object = MibScalar
raisecomIgmpProxyQueryInterval = _RaisecomIgmpProxyQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5, 1, 6),
    _RaisecomIgmpProxyQueryInterval_Type()
)
raisecomIgmpProxyQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpProxyQueryInterval.setStatus("current")


class _RaisecomIgmpProxyQueryMaxReponseInterval_Type(Integer32):
    """Custom type raisecomIgmpProxyQueryMaxReponseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_RaisecomIgmpProxyQueryMaxReponseInterval_Type.__name__ = "Integer32"
_RaisecomIgmpProxyQueryMaxReponseInterval_Object = MibScalar
raisecomIgmpProxyQueryMaxReponseInterval = _RaisecomIgmpProxyQueryMaxReponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5, 1, 7),
    _RaisecomIgmpProxyQueryMaxReponseInterval_Type()
)
raisecomIgmpProxyQueryMaxReponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpProxyQueryMaxReponseInterval.setStatus("current")


class _RaisecomIgmpProxyQueryLastMemberInterval_Type(Integer32):
    """Custom type raisecomIgmpProxyQueryLastMemberInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_RaisecomIgmpProxyQueryLastMemberInterval_Type.__name__ = "Integer32"
_RaisecomIgmpProxyQueryLastMemberInterval_Object = MibScalar
raisecomIgmpProxyQueryLastMemberInterval = _RaisecomIgmpProxyQueryLastMemberInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 5, 1, 8),
    _RaisecomIgmpProxyQueryLastMemberInterval_Type()
)
raisecomIgmpProxyQueryLastMemberInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpProxyQueryLastMemberInterval.setStatus("current")
_RaisecomIgmpFilter_ObjectIdentity = ObjectIdentity
raisecomIgmpFilter = _RaisecomIgmpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6)
)
_RaisecomIgmpFilterScalar_ObjectIdentity = ObjectIdentity
raisecomIgmpFilterScalar = _RaisecomIgmpFilterScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 1)
)


class _RaisecomIgmpFilterEnableFilter_Type(EnableVar):
    """Custom type raisecomIgmpFilterEnableFilter based on EnableVar"""
    defaultValue = 2


_RaisecomIgmpFilterEnableFilter_Type.__name__ = "EnableVar"
_RaisecomIgmpFilterEnableFilter_Object = MibScalar
raisecomIgmpFilterEnableFilter = _RaisecomIgmpFilterEnableFilter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 1, 1),
    _RaisecomIgmpFilterEnableFilter_Type()
)
raisecomIgmpFilterEnableFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIgmpFilterEnableFilter.setStatus("current")


class _RaisecomIgmpFilterMaxProfileNum_Type(Integer32):
    """Custom type raisecomIgmpFilterMaxProfileNum based on Integer32"""
    defaultValue = 100


_RaisecomIgmpFilterMaxProfileNum_Type.__name__ = "Integer32"
_RaisecomIgmpFilterMaxProfileNum_Object = MibScalar
raisecomIgmpFilterMaxProfileNum = _RaisecomIgmpFilterMaxProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 1, 2),
    _RaisecomIgmpFilterMaxProfileNum_Type()
)
raisecomIgmpFilterMaxProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpFilterMaxProfileNum.setStatus("current")


class _RaisecomIgmpFilterCurrentProfileNum_Type(Integer32):
    """Custom type raisecomIgmpFilterCurrentProfileNum based on Integer32"""
    defaultValue = 0


_RaisecomIgmpFilterCurrentProfileNum_Type.__name__ = "Integer32"
_RaisecomIgmpFilterCurrentProfileNum_Object = MibScalar
raisecomIgmpFilterCurrentProfileNum = _RaisecomIgmpFilterCurrentProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 1, 3),
    _RaisecomIgmpFilterCurrentProfileNum_Type()
)
raisecomIgmpFilterCurrentProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpFilterCurrentProfileNum.setStatus("current")
_RaisecomIgmpFilterProfileTable_Object = MibTable
raisecomIgmpFilterProfileTable = _RaisecomIgmpFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 2)
)
if mibBuilder.loadTexts:
    raisecomIgmpFilterProfileTable.setStatus("current")
_RaisecomIgmpFilterProfileEntry_Object = MibTableRow
raisecomIgmpFilterProfileEntry = _RaisecomIgmpFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 2, 1)
)
raisecomIgmpFilterProfileEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpFilterProfileIndex"),
)
if mibBuilder.loadTexts:
    raisecomIgmpFilterProfileEntry.setStatus("current")


class _RaisecomIgmpFilterProfileIndex_Type(Integer32):
    """Custom type raisecomIgmpFilterProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RaisecomIgmpFilterProfileIndex_Type.__name__ = "Integer32"
_RaisecomIgmpFilterProfileIndex_Object = MibTableColumn
raisecomIgmpFilterProfileIndex = _RaisecomIgmpFilterProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 2, 1, 1),
    _RaisecomIgmpFilterProfileIndex_Type()
)
raisecomIgmpFilterProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpFilterProfileIndex.setStatus("current")


class _RaisecomIgmpFilterProfileAct_Type(Integer32):
    """Custom type raisecomIgmpFilterProfileAct based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RaisecomIgmpFilterProfileAct_Type.__name__ = "Integer32"
_RaisecomIgmpFilterProfileAct_Object = MibTableColumn
raisecomIgmpFilterProfileAct = _RaisecomIgmpFilterProfileAct_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 2, 1, 2),
    _RaisecomIgmpFilterProfileAct_Type()
)
raisecomIgmpFilterProfileAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterProfileAct.setStatus("current")
_RaisecomIgmpFilterProfileRowStatus_Type = RowStatus
_RaisecomIgmpFilterProfileRowStatus_Object = MibTableColumn
raisecomIgmpFilterProfileRowStatus = _RaisecomIgmpFilterProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 2, 1, 3),
    _RaisecomIgmpFilterProfileRowStatus_Type()
)
raisecomIgmpFilterProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterProfileRowStatus.setStatus("current")
_RaisecomIgmpFilterPortTable_Object = MibTable
raisecomIgmpFilterPortTable = _RaisecomIgmpFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 3)
)
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortTable.setStatus("current")
_RaisecomIgmpFilterPortEntry_Object = MibTableRow
raisecomIgmpFilterPortEntry = _RaisecomIgmpFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 3, 1)
)
raisecomIgmpFilterPortEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpFilterPortIndex"),
)
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortEntry.setStatus("current")
_RaisecomIgmpFilterPortIndex_Type = Integer32
_RaisecomIgmpFilterPortIndex_Object = MibTableColumn
raisecomIgmpFilterPortIndex = _RaisecomIgmpFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 3, 1, 1),
    _RaisecomIgmpFilterPortIndex_Type()
)
raisecomIgmpFilterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortIndex.setStatus("current")


class _RaisecomIgmpFilterPortProfileIndex_Type(Integer32):
    """Custom type raisecomIgmpFilterPortProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RaisecomIgmpFilterPortProfileIndex_Type.__name__ = "Integer32"
_RaisecomIgmpFilterPortProfileIndex_Object = MibTableColumn
raisecomIgmpFilterPortProfileIndex = _RaisecomIgmpFilterPortProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 3, 1, 2),
    _RaisecomIgmpFilterPortProfileIndex_Type()
)
raisecomIgmpFilterPortProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortProfileIndex.setStatus("current")


class _RaisecomIgmpFilterPortMaxGroups_Type(Integer32):
    """Custom type raisecomIgmpFilterPortMaxGroups based on Integer32"""
    defaultValue = 0


_RaisecomIgmpFilterPortMaxGroups_Type.__name__ = "Integer32"
_RaisecomIgmpFilterPortMaxGroups_Object = MibTableColumn
raisecomIgmpFilterPortMaxGroups = _RaisecomIgmpFilterPortMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 3, 1, 3),
    _RaisecomIgmpFilterPortMaxGroups_Type()
)
raisecomIgmpFilterPortMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortMaxGroups.setStatus("current")
_RaisecomIgmpFilterPortCurrentGroups_Type = Integer32
_RaisecomIgmpFilterPortCurrentGroups_Object = MibTableColumn
raisecomIgmpFilterPortCurrentGroups = _RaisecomIgmpFilterPortCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 3, 1, 4),
    _RaisecomIgmpFilterPortCurrentGroups_Type()
)
raisecomIgmpFilterPortCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortCurrentGroups.setStatus("current")


class _RaisecomIgmpFilterPortMaxGroupsAct_Type(Integer32):
    """Custom type raisecomIgmpFilterPortMaxGroupsAct based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("replace", 2))
    )


_RaisecomIgmpFilterPortMaxGroupsAct_Type.__name__ = "Integer32"
_RaisecomIgmpFilterPortMaxGroupsAct_Object = MibTableColumn
raisecomIgmpFilterPortMaxGroupsAct = _RaisecomIgmpFilterPortMaxGroupsAct_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 3, 1, 5),
    _RaisecomIgmpFilterPortMaxGroupsAct_Type()
)
raisecomIgmpFilterPortMaxGroupsAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortMaxGroupsAct.setStatus("current")
_RaisecomIgmpFilterPortRowStatus_Type = RowStatus
_RaisecomIgmpFilterPortRowStatus_Object = MibTableColumn
raisecomIgmpFilterPortRowStatus = _RaisecomIgmpFilterPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 3, 1, 6),
    _RaisecomIgmpFilterPortRowStatus_Type()
)
raisecomIgmpFilterPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortRowStatus.setStatus("current")
_RaisecomIgmpFilterPortVlanTable_Object = MibTable
raisecomIgmpFilterPortVlanTable = _RaisecomIgmpFilterPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 4)
)
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortVlanTable.setStatus("current")
_RaisecomIgmpFilterPortVlanEntry_Object = MibTableRow
raisecomIgmpFilterPortVlanEntry = _RaisecomIgmpFilterPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 4, 1)
)
raisecomIgmpFilterPortVlanEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpFilterPortVlanPortIndex"),
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpFilterPortVlanVlanIndex"),
)
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortVlanEntry.setStatus("current")
_RaisecomIgmpFilterPortVlanPortIndex_Type = Integer32
_RaisecomIgmpFilterPortVlanPortIndex_Object = MibTableColumn
raisecomIgmpFilterPortVlanPortIndex = _RaisecomIgmpFilterPortVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 4, 1, 1),
    _RaisecomIgmpFilterPortVlanPortIndex_Type()
)
raisecomIgmpFilterPortVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortVlanPortIndex.setStatus("current")
_RaisecomIgmpFilterPortVlanVlanIndex_Type = VlanIndex
_RaisecomIgmpFilterPortVlanVlanIndex_Object = MibTableColumn
raisecomIgmpFilterPortVlanVlanIndex = _RaisecomIgmpFilterPortVlanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 4, 1, 2),
    _RaisecomIgmpFilterPortVlanVlanIndex_Type()
)
raisecomIgmpFilterPortVlanVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortVlanVlanIndex.setStatus("current")


class _RaisecomIgmpFilterPortVlanProfileIndex_Type(Integer32):
    """Custom type raisecomIgmpFilterPortVlanProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RaisecomIgmpFilterPortVlanProfileIndex_Type.__name__ = "Integer32"
_RaisecomIgmpFilterPortVlanProfileIndex_Object = MibTableColumn
raisecomIgmpFilterPortVlanProfileIndex = _RaisecomIgmpFilterPortVlanProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 4, 1, 3),
    _RaisecomIgmpFilterPortVlanProfileIndex_Type()
)
raisecomIgmpFilterPortVlanProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortVlanProfileIndex.setStatus("current")


class _RaisecomIgmpFilterPortVlanMaxGroups_Type(Integer32):
    """Custom type raisecomIgmpFilterPortVlanMaxGroups based on Integer32"""
    defaultValue = 0


_RaisecomIgmpFilterPortVlanMaxGroups_Type.__name__ = "Integer32"
_RaisecomIgmpFilterPortVlanMaxGroups_Object = MibTableColumn
raisecomIgmpFilterPortVlanMaxGroups = _RaisecomIgmpFilterPortVlanMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 4, 1, 4),
    _RaisecomIgmpFilterPortVlanMaxGroups_Type()
)
raisecomIgmpFilterPortVlanMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortVlanMaxGroups.setStatus("current")
_RaisecomIgmpFilterPortVlanCurrentGroups_Type = Integer32
_RaisecomIgmpFilterPortVlanCurrentGroups_Object = MibTableColumn
raisecomIgmpFilterPortVlanCurrentGroups = _RaisecomIgmpFilterPortVlanCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 4, 1, 5),
    _RaisecomIgmpFilterPortVlanCurrentGroups_Type()
)
raisecomIgmpFilterPortVlanCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortVlanCurrentGroups.setStatus("current")


class _RaisecomIgmpFilterPortVlanMaxGroupsAct_Type(Integer32):
    """Custom type raisecomIgmpFilterPortVlanMaxGroupsAct based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("replace", 2))
    )


_RaisecomIgmpFilterPortVlanMaxGroupsAct_Type.__name__ = "Integer32"
_RaisecomIgmpFilterPortVlanMaxGroupsAct_Object = MibTableColumn
raisecomIgmpFilterPortVlanMaxGroupsAct = _RaisecomIgmpFilterPortVlanMaxGroupsAct_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 4, 1, 6),
    _RaisecomIgmpFilterPortVlanMaxGroupsAct_Type()
)
raisecomIgmpFilterPortVlanMaxGroupsAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortVlanMaxGroupsAct.setStatus("current")
_RaisecomIgmpFilterPortVlanRowStatus_Type = RowStatus
_RaisecomIgmpFilterPortVlanRowStatus_Object = MibTableColumn
raisecomIgmpFilterPortVlanRowStatus = _RaisecomIgmpFilterPortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 4, 1, 7),
    _RaisecomIgmpFilterPortVlanRowStatus_Type()
)
raisecomIgmpFilterPortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterPortVlanRowStatus.setStatus("current")
_RaisecomIgmpFilterIpProfileTable_Object = MibTable
raisecomIgmpFilterIpProfileTable = _RaisecomIgmpFilterIpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 5)
)
if mibBuilder.loadTexts:
    raisecomIgmpFilterIpProfileTable.setStatus("current")
_RaisecomIgmpFilterIpProfileEntry_Object = MibTableRow
raisecomIgmpFilterIpProfileEntry = _RaisecomIgmpFilterIpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 5, 1)
)
raisecomIgmpFilterIpProfileEntry.setIndexNames(
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpFilterIpProfileIndex"),
    (0, "RAISECOM-IGMPL2-MIB", "raisecomIgmpFilterIpProfileRangeIndex"),
)
if mibBuilder.loadTexts:
    raisecomIgmpFilterIpProfileEntry.setStatus("current")


class _RaisecomIgmpFilterIpProfileIndex_Type(Integer32):
    """Custom type raisecomIgmpFilterIpProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RaisecomIgmpFilterIpProfileIndex_Type.__name__ = "Integer32"
_RaisecomIgmpFilterIpProfileIndex_Object = MibTableColumn
raisecomIgmpFilterIpProfileIndex = _RaisecomIgmpFilterIpProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 5, 1, 1),
    _RaisecomIgmpFilterIpProfileIndex_Type()
)
raisecomIgmpFilterIpProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpFilterIpProfileIndex.setStatus("current")


class _RaisecomIgmpFilterIpProfileRangeIndex_Type(Integer32):
    """Custom type raisecomIgmpFilterIpProfileRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RaisecomIgmpFilterIpProfileRangeIndex_Type.__name__ = "Integer32"
_RaisecomIgmpFilterIpProfileRangeIndex_Object = MibTableColumn
raisecomIgmpFilterIpProfileRangeIndex = _RaisecomIgmpFilterIpProfileRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 5, 1, 2),
    _RaisecomIgmpFilterIpProfileRangeIndex_Type()
)
raisecomIgmpFilterIpProfileRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIgmpFilterIpProfileRangeIndex.setStatus("current")
_RaisecomIgmpFilterIpProfileStartAddress_Type = InetAddress
_RaisecomIgmpFilterIpProfileStartAddress_Object = MibTableColumn
raisecomIgmpFilterIpProfileStartAddress = _RaisecomIgmpFilterIpProfileStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 5, 1, 3),
    _RaisecomIgmpFilterIpProfileStartAddress_Type()
)
raisecomIgmpFilterIpProfileStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterIpProfileStartAddress.setStatus("current")
_RaisecomIgmpFilterIpProfileEndAddress_Type = InetAddress
_RaisecomIgmpFilterIpProfileEndAddress_Object = MibTableColumn
raisecomIgmpFilterIpProfileEndAddress = _RaisecomIgmpFilterIpProfileEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 5, 1, 4),
    _RaisecomIgmpFilterIpProfileEndAddress_Type()
)
raisecomIgmpFilterIpProfileEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterIpProfileEndAddress.setStatus("current")
_RaisecomIgmpFilterIpProfileIpType_Type = InetAddressType
_RaisecomIgmpFilterIpProfileIpType_Object = MibTableColumn
raisecomIgmpFilterIpProfileIpType = _RaisecomIgmpFilterIpProfileIpType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 5, 1, 5),
    _RaisecomIgmpFilterIpProfileIpType_Type()
)
raisecomIgmpFilterIpProfileIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterIpProfileIpType.setStatus("current")
_RaisecomIgmpFilterIpProfileRowStatus_Type = RowStatus
_RaisecomIgmpFilterIpProfileRowStatus_Object = MibTableColumn
raisecomIgmpFilterIpProfileRowStatus = _RaisecomIgmpFilterIpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 2, 6, 5, 1, 6),
    _RaisecomIgmpFilterIpProfileRowStatus_Type()
)
raisecomIgmpFilterIpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIgmpFilterIpProfileRowStatus.setStatus("current")
_RaisecomIgmpL2Conformance_ObjectIdentity = ObjectIdentity
raisecomIgmpL2Conformance = _RaisecomIgmpL2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 28, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-IGMPL2-MIB",
    **{"raisecomIgmpL2": raisecomIgmpL2,
       "raisecomIgmpL2Notifications": raisecomIgmpL2Notifications,
       "raisecomIgmpL2Objects": raisecomIgmpL2Objects,
       "raisecomIgmpBase": raisecomIgmpBase,
       "raisecomIgmpBaseScalar": raisecomIgmpBaseScalar,
       "raisecomIgmpAging": raisecomIgmpAging,
       "raisecomIgmpRingPortList": raisecomIgmpRingPortList,
       "raisecomIgmpImmediateLeaveTable": raisecomIgmpImmediateLeaveTable,
       "raisecomIgmpImmediateLeaveEntry": raisecomIgmpImmediateLeaveEntry,
       "raisecomIgmpImmediateLeavePort": raisecomIgmpImmediateLeavePort,
       "raisecomIgmpImmediateLeaveType": raisecomIgmpImmediateLeaveType,
       "raisecomIgmpImmediateLeaveVlanList": raisecomIgmpImmediateLeaveVlanList,
       "raisecomIgmpImmediateLeaveRowStatus": raisecomIgmpImmediateLeaveRowStatus,
       "raisecomIgmpMrouterTable": raisecomIgmpMrouterTable,
       "raisecomIgmpMrouterEntry": raisecomIgmpMrouterEntry,
       "raisecomIgmpMrouterPort": raisecomIgmpMrouterPort,
       "raisecomIgmpMrouterVlan": raisecomIgmpMrouterVlan,
       "raisecomIgmpMrouterLiveTime": raisecomIgmpMrouterLiveTime,
       "raisecomIgmpMrouterMRStatus": raisecomIgmpMrouterMRStatus,
       "raisecomIgmpMrouterRowStatus": raisecomIgmpMrouterRowStatus,
       "raisecomIgmpMemberTable": raisecomIgmpMemberTable,
       "raisecomIgmpMemberEntry": raisecomIgmpMemberEntry,
       "raisecomIgmpMemberPort": raisecomIgmpMemberPort,
       "raisecomIgmpMemberUserVlan": raisecomIgmpMemberUserVlan,
       "raisecomIgmpMemberGroupIpType": raisecomIgmpMemberGroupIpType,
       "raisecomIgmpMemberGroup": raisecomIgmpMemberGroup,
       "raisecomIgmpMemberMVlan": raisecomIgmpMemberMVlan,
       "raisecomIgmpMemberLiveTime": raisecomIgmpMemberLiveTime,
       "raisecomIgmpMemberSource": raisecomIgmpMemberSource,
       "raisecomIgmpMemberRowStatus": raisecomIgmpMemberRowStatus,
       "raisecomIgmpPortStatisticsTable": raisecomIgmpPortStatisticsTable,
       "raisecomIgmpPortStatisticsEntry": raisecomIgmpPortStatisticsEntry,
       "raisecomIgmpPortStatisticsPortNum": raisecomIgmpPortStatisticsPortNum,
       "raisecomIgmpPortStatisticsClear": raisecomIgmpPortStatisticsClear,
       "raisecomIgmpPortStatisticsRecvQuery": raisecomIgmpPortStatisticsRecvQuery,
       "raisecomIgmpPortStatisticsRecvReport": raisecomIgmpPortStatisticsRecvReport,
       "raisecomIgmpPortStatisticsRecvLeave": raisecomIgmpPortStatisticsRecvLeave,
       "raisecomIgmpPortStatisticsFilterDropQuery": raisecomIgmpPortStatisticsFilterDropQuery,
       "raisecomIgmpPortStatisticsFilterDropReport": raisecomIgmpPortStatisticsFilterDropReport,
       "raisecomIgmpPortStatisticsFilterDropLeave": raisecomIgmpPortStatisticsFilterDropLeave,
       "raisecomIgmpPortStatisticsSnoopDealQuery": raisecomIgmpPortStatisticsSnoopDealQuery,
       "raisecomIgmpPortStatisticsSnoopDealReport": raisecomIgmpPortStatisticsSnoopDealReport,
       "raisecomIgmpPortStatisticsSnoopDealLeave": raisecomIgmpPortStatisticsSnoopDealLeave,
       "raisecomIgmpPortStatisticsMvrDealQuery": raisecomIgmpPortStatisticsMvrDealQuery,
       "raisecomIgmpPortStatisticsMvrDealReport": raisecomIgmpPortStatisticsMvrDealReport,
       "raisecomIgmpPortStatisticsMvrDealLeave": raisecomIgmpPortStatisticsMvrDealLeave,
       "raisecomIgmpPortStatisticsVlanCPDealQuery": raisecomIgmpPortStatisticsVlanCPDealQuery,
       "raisecomIgmpPortStatisticsVlanCPDealReport": raisecomIgmpPortStatisticsVlanCPDealReport,
       "raisecomIgmpPortStatisticsVlanCPDealLeave": raisecomIgmpPortStatisticsVlanCPDealLeave,
       "raisecomIgmpPortStatisticsReplaceCount": raisecomIgmpPortStatisticsReplaceCount,
       "raisecomIgmpSnooping": raisecomIgmpSnooping,
       "raisecomIgmpSnoopingScalar": raisecomIgmpSnoopingScalar,
       "raisecomIgmpSnoopingEnable": raisecomIgmpSnoopingEnable,
       "raisecomIgmpSnoopingEnableVlanList": raisecomIgmpSnoopingEnableVlanList,
       "raisecomIgmpAuthRadiusEnable": raisecomIgmpAuthRadiusEnable,
       "raisecomIgmpAuthRadiusPortEnable": raisecomIgmpAuthRadiusPortEnable,
       "raisecomIgmpMvr": raisecomIgmpMvr,
       "raisecomIgmpMvrScalar": raisecomIgmpMvrScalar,
       "raisecomIgmpMvrEnable": raisecomIgmpMvrEnable,
       "raisecomIgmpMvrEnablePortList": raisecomIgmpMvrEnablePortList,
       "raisecomIgmpMvrMVlanGroupTable": raisecomIgmpMvrMVlanGroupTable,
       "raisecomIgmpMvrMVlanGroupEntry": raisecomIgmpMvrMVlanGroupEntry,
       "raisecomIgmpMvrGroupIpType": raisecomIgmpMvrGroupIpType,
       "raisecomIgmpMvrGroup": raisecomIgmpMvrGroup,
       "raisecomIgmpMvrMVlan": raisecomIgmpMvrMVlan,
       "raisecomIgmpMvrGroupRowStatus": raisecomIgmpMvrGroupRowStatus,
       "raisecomIgmpVlanCopy": raisecomIgmpVlanCopy,
       "raisecomIgmpVlanCopyScalar": raisecomIgmpVlanCopyScalar,
       "raisecomIgmpVlanCopyEnable": raisecomIgmpVlanCopyEnable,
       "raisecomIgmpVlanCopyEnablePortList": raisecomIgmpVlanCopyEnablePortList,
       "raisecomIgmpVlanCopyVlanGroupTable": raisecomIgmpVlanCopyVlanGroupTable,
       "raisecomIgmpVlanCopyVlanGroupEntry": raisecomIgmpVlanCopyVlanGroupEntry,
       "raisecomIgmpVlanCopyGroupIpType": raisecomIgmpVlanCopyGroupIpType,
       "raisecomIgmpVlanCopyGroup": raisecomIgmpVlanCopyGroup,
       "raisecomIgmpVlanCopyMcastVlan": raisecomIgmpVlanCopyMcastVlan,
       "raisecomIgmpVlanCopyGroupRowStatus": raisecomIgmpVlanCopyGroupRowStatus,
       "raisecomIgmpProxy": raisecomIgmpProxy,
       "raisecomIgmpProxyScalar": raisecomIgmpProxyScalar,
       "raisecomIgmpProxyEnable": raisecomIgmpProxyEnable,
       "raisecomIgmpProxySuppressionEnable": raisecomIgmpProxySuppressionEnable,
       "raisecomIgmpProxyQuerierEnable": raisecomIgmpProxyQuerierEnable,
       "raisecomIgmpProxySourceIpType": raisecomIgmpProxySourceIpType,
       "raisecomIgmpProxySourceIpAddress": raisecomIgmpProxySourceIpAddress,
       "raisecomIgmpProxyQueryInterval": raisecomIgmpProxyQueryInterval,
       "raisecomIgmpProxyQueryMaxReponseInterval": raisecomIgmpProxyQueryMaxReponseInterval,
       "raisecomIgmpProxyQueryLastMemberInterval": raisecomIgmpProxyQueryLastMemberInterval,
       "raisecomIgmpFilter": raisecomIgmpFilter,
       "raisecomIgmpFilterScalar": raisecomIgmpFilterScalar,
       "raisecomIgmpFilterEnableFilter": raisecomIgmpFilterEnableFilter,
       "raisecomIgmpFilterMaxProfileNum": raisecomIgmpFilterMaxProfileNum,
       "raisecomIgmpFilterCurrentProfileNum": raisecomIgmpFilterCurrentProfileNum,
       "raisecomIgmpFilterProfileTable": raisecomIgmpFilterProfileTable,
       "raisecomIgmpFilterProfileEntry": raisecomIgmpFilterProfileEntry,
       "raisecomIgmpFilterProfileIndex": raisecomIgmpFilterProfileIndex,
       "raisecomIgmpFilterProfileAct": raisecomIgmpFilterProfileAct,
       "raisecomIgmpFilterProfileRowStatus": raisecomIgmpFilterProfileRowStatus,
       "raisecomIgmpFilterPortTable": raisecomIgmpFilterPortTable,
       "raisecomIgmpFilterPortEntry": raisecomIgmpFilterPortEntry,
       "raisecomIgmpFilterPortIndex": raisecomIgmpFilterPortIndex,
       "raisecomIgmpFilterPortProfileIndex": raisecomIgmpFilterPortProfileIndex,
       "raisecomIgmpFilterPortMaxGroups": raisecomIgmpFilterPortMaxGroups,
       "raisecomIgmpFilterPortCurrentGroups": raisecomIgmpFilterPortCurrentGroups,
       "raisecomIgmpFilterPortMaxGroupsAct": raisecomIgmpFilterPortMaxGroupsAct,
       "raisecomIgmpFilterPortRowStatus": raisecomIgmpFilterPortRowStatus,
       "raisecomIgmpFilterPortVlanTable": raisecomIgmpFilterPortVlanTable,
       "raisecomIgmpFilterPortVlanEntry": raisecomIgmpFilterPortVlanEntry,
       "raisecomIgmpFilterPortVlanPortIndex": raisecomIgmpFilterPortVlanPortIndex,
       "raisecomIgmpFilterPortVlanVlanIndex": raisecomIgmpFilterPortVlanVlanIndex,
       "raisecomIgmpFilterPortVlanProfileIndex": raisecomIgmpFilterPortVlanProfileIndex,
       "raisecomIgmpFilterPortVlanMaxGroups": raisecomIgmpFilterPortVlanMaxGroups,
       "raisecomIgmpFilterPortVlanCurrentGroups": raisecomIgmpFilterPortVlanCurrentGroups,
       "raisecomIgmpFilterPortVlanMaxGroupsAct": raisecomIgmpFilterPortVlanMaxGroupsAct,
       "raisecomIgmpFilterPortVlanRowStatus": raisecomIgmpFilterPortVlanRowStatus,
       "raisecomIgmpFilterIpProfileTable": raisecomIgmpFilterIpProfileTable,
       "raisecomIgmpFilterIpProfileEntry": raisecomIgmpFilterIpProfileEntry,
       "raisecomIgmpFilterIpProfileIndex": raisecomIgmpFilterIpProfileIndex,
       "raisecomIgmpFilterIpProfileRangeIndex": raisecomIgmpFilterIpProfileRangeIndex,
       "raisecomIgmpFilterIpProfileStartAddress": raisecomIgmpFilterIpProfileStartAddress,
       "raisecomIgmpFilterIpProfileEndAddress": raisecomIgmpFilterIpProfileEndAddress,
       "raisecomIgmpFilterIpProfileIpType": raisecomIgmpFilterIpProfileIpType,
       "raisecomIgmpFilterIpProfileRowStatus": raisecomIgmpFilterIpProfileRowStatus,
       "raisecomIgmpL2Conformance": raisecomIgmpL2Conformance}
)
