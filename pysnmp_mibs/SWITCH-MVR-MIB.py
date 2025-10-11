# SNMP MIB module (SWITCH-MVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-MVR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:07 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

rcMvr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcMvrConfig_ObjectIdentity = ObjectIdentity
rcMvrConfig = _RcMvrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1)
)


class _RcMvrEnable_Type(EnableVar):
    """Custom type rcMvrEnable based on EnableVar"""
    defaultValue = 2


_RcMvrEnable_Type.__name__ = "EnableVar"
_RcMvrEnable_Object = MibScalar
rcMvrEnable = _RcMvrEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 1),
    _RcMvrEnable_Type()
)
rcMvrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrEnable.setStatus("current")
_RcMvrVlan_Type = Vlanset
_RcMvrVlan_Object = MibScalar
rcMvrVlan = _RcMvrVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 2),
    _RcMvrVlan_Type()
)
rcMvrVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrVlan.setStatus("current")
_RcMvrMaxGroups_Type = Integer32
_RcMvrMaxGroups_Object = MibScalar
rcMvrMaxGroups = _RcMvrMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 3),
    _RcMvrMaxGroups_Type()
)
rcMvrMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrMaxGroups.setStatus("current")
_RcMvrCurrentGroups_Type = Integer32
_RcMvrCurrentGroups_Object = MibScalar
rcMvrCurrentGroups = _RcMvrCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 4),
    _RcMvrCurrentGroups_Type()
)
rcMvrCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrCurrentGroups.setStatus("current")


class _RcMvrQureyTime_Type(Integer32):
    """Custom type rcMvrQureyTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_RcMvrQureyTime_Type.__name__ = "Integer32"
_RcMvrQureyTime_Object = MibScalar
rcMvrQureyTime = _RcMvrQureyTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 5),
    _RcMvrQureyTime_Type()
)
rcMvrQureyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrQureyTime.setStatus("current")
if mibBuilder.loadTexts:
    rcMvrQureyTime.setUnits("tenths of second")


class _RcMvrOperMode_Type(Integer32):
    """Custom type rcMvrOperMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("compatible", 2))
    )


_RcMvrOperMode_Type.__name__ = "Integer32"
_RcMvrOperMode_Object = MibScalar
rcMvrOperMode = _RcMvrOperMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 6),
    _RcMvrOperMode_Type()
)
rcMvrOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrOperMode.setStatus("current")
_RcMvrGroupTable_Object = MibTable
rcMvrGroupTable = _RcMvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 7)
)
if mibBuilder.loadTexts:
    rcMvrGroupTable.setStatus("current")
_RcMvrGroupEntry_Object = MibTableRow
rcMvrGroupEntry = _RcMvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 7, 1)
)
rcMvrGroupEntry.setIndexNames(
    (0, "SWITCH-MVR-MIB", "rcMvrGroupVlan"),
    (0, "SWITCH-MVR-MIB", "rcMvrGroupAddress"),
)
if mibBuilder.loadTexts:
    rcMvrGroupEntry.setStatus("current")
_RcMvrGroupVlan_Type = Integer32
_RcMvrGroupVlan_Object = MibTableColumn
rcMvrGroupVlan = _RcMvrGroupVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 7, 1, 1),
    _RcMvrGroupVlan_Type()
)
rcMvrGroupVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMvrGroupVlan.setStatus("current")
_RcMvrGroupAddress_Type = IpAddress
_RcMvrGroupAddress_Object = MibTableColumn
rcMvrGroupAddress = _RcMvrGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 7, 1, 2),
    _RcMvrGroupAddress_Type()
)
rcMvrGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMvrGroupAddress.setStatus("current")
_RcMvrGroupRowStatus_Type = RowStatus
_RcMvrGroupRowStatus_Object = MibTableColumn
rcMvrGroupRowStatus = _RcMvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 7, 1, 3),
    _RcMvrGroupRowStatus_Type()
)
rcMvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMvrGroupRowStatus.setStatus("current")
_RcMvrIFTable_Object = MibTable
rcMvrIFTable = _RcMvrIFTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 8)
)
if mibBuilder.loadTexts:
    rcMvrIFTable.setStatus("current")
_RcMvrIFEntry_Object = MibTableRow
rcMvrIFEntry = _RcMvrIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 8, 1)
)
rcMvrIFEntry.setIndexNames(
    (0, "SWITCH-MVR-MIB", "rcMvrPortIndex"),
)
if mibBuilder.loadTexts:
    rcMvrIFEntry.setStatus("current")
_RcMvrPortIndex_Type = Integer32
_RcMvrPortIndex_Object = MibTableColumn
rcMvrPortIndex = _RcMvrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 8, 1, 1),
    _RcMvrPortIndex_Type()
)
rcMvrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMvrPortIndex.setStatus("current")
_RcMvrPortEnable_Type = EnableVar
_RcMvrPortEnable_Object = MibTableColumn
rcMvrPortEnable = _RcMvrPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 8, 1, 2),
    _RcMvrPortEnable_Type()
)
rcMvrPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrPortEnable.setStatus("current")


class _RcMvrType_Type(Integer32):
    """Custom type rcMvrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-mvr", 0),
          ("source", 1),
          ("receiver", 2))
    )


_RcMvrType_Type.__name__ = "Integer32"
_RcMvrType_Object = MibTableColumn
rcMvrType = _RcMvrType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 8, 1, 3),
    _RcMvrType_Type()
)
rcMvrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrType.setStatus("current")
_RcMvrImmediate_Type = EnableVar
_RcMvrImmediate_Object = MibTableColumn
rcMvrImmediate = _RcMvrImmediate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 8, 1, 4),
    _RcMvrImmediate_Type()
)
rcMvrImmediate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrImmediate.setStatus("current")


class _RcMvrPortStatus_Type(Integer32):
    """Custom type rcMvrPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RcMvrPortStatus_Type.__name__ = "Integer32"
_RcMvrPortStatus_Object = MibTableColumn
rcMvrPortStatus = _RcMvrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 8, 1, 5),
    _RcMvrPortStatus_Type()
)
rcMvrPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortStatus.setStatus("current")
_RcMvrMemberTable_Object = MibTable
rcMvrMemberTable = _RcMvrMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 9)
)
if mibBuilder.loadTexts:
    rcMvrMemberTable.setStatus("current")
_RcMvrMemberEntry_Object = MibTableRow
rcMvrMemberEntry = _RcMvrMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 9, 1)
)
rcMvrMemberEntry.setIndexNames(
    (0, "SWITCH-MVR-MIB", "rcMvrMemberPort"),
    (0, "SWITCH-MVR-MIB", "rcMvrMemberVlan"),
    (0, "SWITCH-MVR-MIB", "rcMvrMemberGroupAddress"),
)
if mibBuilder.loadTexts:
    rcMvrMemberEntry.setStatus("current")
_RcMvrMemberPort_Type = Integer32
_RcMvrMemberPort_Object = MibTableColumn
rcMvrMemberPort = _RcMvrMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 9, 1, 1),
    _RcMvrMemberPort_Type()
)
rcMvrMemberPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMvrMemberPort.setStatus("current")


class _RcMvrMemberVlan_Type(Integer32):
    """Custom type rcMvrMemberVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcMvrMemberVlan_Type.__name__ = "Integer32"
_RcMvrMemberVlan_Object = MibTableColumn
rcMvrMemberVlan = _RcMvrMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 9, 1, 2),
    _RcMvrMemberVlan_Type()
)
rcMvrMemberVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMvrMemberVlan.setStatus("current")
_RcMvrMemberGroupAddress_Type = IpAddress
_RcMvrMemberGroupAddress_Object = MibTableColumn
rcMvrMemberGroupAddress = _RcMvrMemberGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 9, 1, 3),
    _RcMvrMemberGroupAddress_Type()
)
rcMvrMemberGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMvrMemberGroupAddress.setStatus("current")


class _RcMvrMemberGroupType_Type(Integer32):
    """Custom type rcMvrMemberGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_RcMvrMemberGroupType_Type.__name__ = "Integer32"
_RcMvrMemberGroupType_Object = MibTableColumn
rcMvrMemberGroupType = _RcMvrMemberGroupType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 9, 1, 4),
    _RcMvrMemberGroupType_Type()
)
rcMvrMemberGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrMemberGroupType.setStatus("current")
_RcMvrMemberRowStatus_Type = RowStatus
_RcMvrMemberRowStatus_Object = MibTableColumn
rcMvrMemberRowStatus = _RcMvrMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 9, 1, 5),
    _RcMvrMemberRowStatus_Type()
)
rcMvrMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMvrMemberRowStatus.setStatus("current")
_RcMvrMemberReplicableVlans_Type = Vlanset
_RcMvrMemberReplicableVlans_Object = MibTableColumn
rcMvrMemberReplicableVlans = _RcMvrMemberReplicableVlans_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 9, 1, 6),
    _RcMvrMemberReplicableVlans_Type()
)
rcMvrMemberReplicableVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrMemberReplicableVlans.setStatus("current")
_RcMvrPortStatisticsTable_Object = MibTable
rcMvrPortStatisticsTable = _RcMvrPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10)
)
if mibBuilder.loadTexts:
    rcMvrPortStatisticsTable.setStatus("current")
_RcMvrPortStatisticsEntry_Object = MibTableRow
rcMvrPortStatisticsEntry = _RcMvrPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1)
)
rcMvrPortStatisticsEntry.setIndexNames(
    (0, "SWITCH-MVR-MIB", "rcMvrPortStatisticsPortid"),
)
if mibBuilder.loadTexts:
    rcMvrPortStatisticsEntry.setStatus("current")
_RcMvrPortStatisticsPortid_Type = Integer32
_RcMvrPortStatisticsPortid_Object = MibTableColumn
rcMvrPortStatisticsPortid = _RcMvrPortStatisticsPortid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 1),
    _RcMvrPortStatisticsPortid_Type()
)
rcMvrPortStatisticsPortid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMvrPortStatisticsPortid.setStatus("current")


class _RcMvrPortStatisticsClear_Type(Integer32):
    """Custom type rcMvrPortStatisticsClear based on Integer32"""
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


_RcMvrPortStatisticsClear_Type.__name__ = "Integer32"
_RcMvrPortStatisticsClear_Object = MibTableColumn
rcMvrPortStatisticsClear = _RcMvrPortStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 2),
    _RcMvrPortStatisticsClear_Type()
)
rcMvrPortStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrPortStatisticsClear.setStatus("current")
_RcMvrPortStatisticsRecvQueryPkts_Type = Counter32
_RcMvrPortStatisticsRecvQueryPkts_Object = MibTableColumn
rcMvrPortStatisticsRecvQueryPkts = _RcMvrPortStatisticsRecvQueryPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 3),
    _RcMvrPortStatisticsRecvQueryPkts_Type()
)
rcMvrPortStatisticsRecvQueryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortStatisticsRecvQueryPkts.setStatus("current")
_RcMvrPortStatisticsRecvReportPkts_Type = Counter32
_RcMvrPortStatisticsRecvReportPkts_Object = MibTableColumn
rcMvrPortStatisticsRecvReportPkts = _RcMvrPortStatisticsRecvReportPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 4),
    _RcMvrPortStatisticsRecvReportPkts_Type()
)
rcMvrPortStatisticsRecvReportPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortStatisticsRecvReportPkts.setStatus("current")
_RcMvrPortStatisticsRecvLeavePkts_Type = Counter32
_RcMvrPortStatisticsRecvLeavePkts_Object = MibTableColumn
rcMvrPortStatisticsRecvLeavePkts = _RcMvrPortStatisticsRecvLeavePkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 5),
    _RcMvrPortStatisticsRecvLeavePkts_Type()
)
rcMvrPortStatisticsRecvLeavePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortStatisticsRecvLeavePkts.setStatus("current")
_RcMvrPortStatisticsDropQueryPkts_Type = Counter32
_RcMvrPortStatisticsDropQueryPkts_Object = MibTableColumn
rcMvrPortStatisticsDropQueryPkts = _RcMvrPortStatisticsDropQueryPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 6),
    _RcMvrPortStatisticsDropQueryPkts_Type()
)
rcMvrPortStatisticsDropQueryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortStatisticsDropQueryPkts.setStatus("current")
_RcMvrPortStatisticsDropReportPkts_Type = Counter32
_RcMvrPortStatisticsDropReportPkts_Object = MibTableColumn
rcMvrPortStatisticsDropReportPkts = _RcMvrPortStatisticsDropReportPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 7),
    _RcMvrPortStatisticsDropReportPkts_Type()
)
rcMvrPortStatisticsDropReportPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortStatisticsDropReportPkts.setStatus("current")
_RcMvrPortStatisticsDropLeavePkts_Type = Counter32
_RcMvrPortStatisticsDropLeavePkts_Object = MibTableColumn
rcMvrPortStatisticsDropLeavePkts = _RcMvrPortStatisticsDropLeavePkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 8),
    _RcMvrPortStatisticsDropLeavePkts_Type()
)
rcMvrPortStatisticsDropLeavePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortStatisticsDropLeavePkts.setStatus("current")
_RcMvrPortLastReplaceNewMulticast_Type = IpAddress
_RcMvrPortLastReplaceNewMulticast_Object = MibTableColumn
rcMvrPortLastReplaceNewMulticast = _RcMvrPortLastReplaceNewMulticast_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 9),
    _RcMvrPortLastReplaceNewMulticast_Type()
)
rcMvrPortLastReplaceNewMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortLastReplaceNewMulticast.setStatus("current")
_RcMvrPortLastReplaceOldMulticast_Type = IpAddress
_RcMvrPortLastReplaceOldMulticast_Object = MibTableColumn
rcMvrPortLastReplaceOldMulticast = _RcMvrPortLastReplaceOldMulticast_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 10),
    _RcMvrPortLastReplaceOldMulticast_Type()
)
rcMvrPortLastReplaceOldMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortLastReplaceOldMulticast.setStatus("current")
_RcMvrPortReplaceTotalCount_Type = Counter32
_RcMvrPortReplaceTotalCount_Object = MibTableColumn
rcMvrPortReplaceTotalCount = _RcMvrPortReplaceTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 10, 1, 11),
    _RcMvrPortReplaceTotalCount_Type()
)
rcMvrPortReplaceTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMvrPortReplaceTotalCount.setStatus("current")


class _RcMvrProxySuppressionEnable_Type(EnableVar):
    """Custom type rcMvrProxySuppressionEnable based on EnableVar"""
    defaultValue = 2


_RcMvrProxySuppressionEnable_Type.__name__ = "EnableVar"
_RcMvrProxySuppressionEnable_Object = MibScalar
rcMvrProxySuppressionEnable = _RcMvrProxySuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 11),
    _RcMvrProxySuppressionEnable_Type()
)
rcMvrProxySuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrProxySuppressionEnable.setStatus("current")


class _RcIgmpQuerierEnable_Type(EnableVar):
    """Custom type rcIgmpQuerierEnable based on EnableVar"""
    defaultValue = 2


_RcIgmpQuerierEnable_Type.__name__ = "EnableVar"
_RcIgmpQuerierEnable_Object = MibScalar
rcIgmpQuerierEnable = _RcIgmpQuerierEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 12),
    _RcIgmpQuerierEnable_Type()
)
rcIgmpQuerierEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpQuerierEnable.setStatus("current")
_RcMvrProxySourceIpAddress_Type = IpAddress
_RcMvrProxySourceIpAddress_Object = MibScalar
rcMvrProxySourceIpAddress = _RcMvrProxySourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 13),
    _RcMvrProxySourceIpAddress_Type()
)
rcMvrProxySourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrProxySourceIpAddress.setStatus("current")


class _RcIgmpQueryInterval_Type(Integer32):
    """Custom type rcIgmpQueryInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_RcIgmpQueryInterval_Type.__name__ = "Integer32"
_RcIgmpQueryInterval_Object = MibScalar
rcIgmpQueryInterval = _RcIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 14),
    _RcIgmpQueryInterval_Type()
)
rcIgmpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rcIgmpQueryInterval.setUnits("Seconds")


class _RcMvrProxyQueryMaxReponseInterval_Type(Integer32):
    """Custom type rcMvrProxyQueryMaxReponseInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_RcMvrProxyQueryMaxReponseInterval_Type.__name__ = "Integer32"
_RcMvrProxyQueryMaxReponseInterval_Object = MibScalar
rcMvrProxyQueryMaxReponseInterval = _RcMvrProxyQueryMaxReponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 15),
    _RcMvrProxyQueryMaxReponseInterval_Type()
)
rcMvrProxyQueryMaxReponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrProxyQueryMaxReponseInterval.setStatus("current")
if mibBuilder.loadTexts:
    rcMvrProxyQueryMaxReponseInterval.setUnits("Seconds")


class _RcMvrProxyQueryLastMemberInterval_Type(Integer32):
    """Custom type rcMvrProxyQueryLastMemberInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_RcMvrProxyQueryLastMemberInterval_Type.__name__ = "Integer32"
_RcMvrProxyQueryLastMemberInterval_Object = MibScalar
rcMvrProxyQueryLastMemberInterval = _RcMvrProxyQueryLastMemberInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 16),
    _RcMvrProxyQueryLastMemberInterval_Type()
)
rcMvrProxyQueryLastMemberInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrProxyQueryLastMemberInterval.setStatus("current")
if mibBuilder.loadTexts:
    rcMvrProxyQueryLastMemberInterval.setUnits("Seconds")


class _RcMvrIpmcReplicationEnable_Type(EnableVar):
    """Custom type rcMvrIpmcReplicationEnable based on EnableVar"""
    defaultValue = 2


_RcMvrIpmcReplicationEnable_Type.__name__ = "EnableVar"
_RcMvrIpmcReplicationEnable_Object = MibScalar
rcMvrIpmcReplicationEnable = _RcMvrIpmcReplicationEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 1, 17),
    _RcMvrIpmcReplicationEnable_Type()
)
rcMvrIpmcReplicationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMvrIpmcReplicationEnable.setStatus("current")
_RcIgmpFilterConfig_ObjectIdentity = ObjectIdentity
rcIgmpFilterConfig = _RcIgmpFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2)
)


class _RcIgmpFilterEnable_Type(EnableVar):
    """Custom type rcIgmpFilterEnable based on EnableVar"""
    defaultValue = 1


_RcIgmpFilterEnable_Type.__name__ = "EnableVar"
_RcIgmpFilterEnable_Object = MibScalar
rcIgmpFilterEnable = _RcIgmpFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 1),
    _RcIgmpFilterEnable_Type()
)
rcIgmpFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpFilterEnable.setStatus("current")
_RcIgmpFilterMaxProfiles_Type = Integer32
_RcIgmpFilterMaxProfiles_Object = MibScalar
rcIgmpFilterMaxProfiles = _RcIgmpFilterMaxProfiles_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 2),
    _RcIgmpFilterMaxProfiles_Type()
)
rcIgmpFilterMaxProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIgmpFilterMaxProfiles.setStatus("current")
if mibBuilder.loadTexts:
    rcIgmpFilterMaxProfiles.setUnits("profiles")


class _RcIgmpFilterAddEntry_Type(Integer32):
    """Custom type rcIgmpFilterAddEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RcIgmpFilterAddEntry_Type.__name__ = "Integer32"
_RcIgmpFilterAddEntry_Object = MibScalar
rcIgmpFilterAddEntry = _RcIgmpFilterAddEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 3),
    _RcIgmpFilterAddEntry_Type()
)
rcIgmpFilterAddEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpFilterAddEntry.setStatus("current")


class _RcIgmpFilterDelEntry_Type(Integer32):
    """Custom type rcIgmpFilterDelEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RcIgmpFilterDelEntry_Type.__name__ = "Integer32"
_RcIgmpFilterDelEntry_Object = MibScalar
rcIgmpFilterDelEntry = _RcIgmpFilterDelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 4),
    _RcIgmpFilterDelEntry_Type()
)
rcIgmpFilterDelEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpFilterDelEntry.setStatus("current")
_RcIgmpFilterTable_Object = MibTable
rcIgmpFilterTable = _RcIgmpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 5)
)
if mibBuilder.loadTexts:
    rcIgmpFilterTable.setStatus("current")
_RcIgmpFilterEntry_Object = MibTableRow
rcIgmpFilterEntry = _RcIgmpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 5, 1)
)
rcIgmpFilterEntry.setIndexNames(
    (0, "SWITCH-MVR-MIB", "rcIgmpFilterProfileIndex"),
    (0, "SWITCH-MVR-MIB", "rcIgmpFilterStartAddress"),
)
if mibBuilder.loadTexts:
    rcIgmpFilterEntry.setStatus("current")


class _RcIgmpFilterProfileIndex_Type(Integer32):
    """Custom type rcIgmpFilterProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RcIgmpFilterProfileIndex_Type.__name__ = "Integer32"
_RcIgmpFilterProfileIndex_Object = MibTableColumn
rcIgmpFilterProfileIndex = _RcIgmpFilterProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 5, 1, 1),
    _RcIgmpFilterProfileIndex_Type()
)
rcIgmpFilterProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIgmpFilterProfileIndex.setStatus("current")
_RcIgmpFilterStartAddress_Type = IpAddress
_RcIgmpFilterStartAddress_Object = MibTableColumn
rcIgmpFilterStartAddress = _RcIgmpFilterStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 5, 1, 2),
    _RcIgmpFilterStartAddress_Type()
)
rcIgmpFilterStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIgmpFilterStartAddress.setStatus("current")
_RcIgmpFilterEndAddress_Type = IpAddress
_RcIgmpFilterEndAddress_Object = MibTableColumn
rcIgmpFilterEndAddress = _RcIgmpFilterEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 5, 1, 3),
    _RcIgmpFilterEndAddress_Type()
)
rcIgmpFilterEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIgmpFilterEndAddress.setStatus("current")


class _RcIgmpFilterProfileAction_Type(Integer32):
    """Custom type rcIgmpFilterProfileAction based on Integer32"""
    defaultValue = 1

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


_RcIgmpFilterProfileAction_Type.__name__ = "Integer32"
_RcIgmpFilterProfileAction_Object = MibTableColumn
rcIgmpFilterProfileAction = _RcIgmpFilterProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 5, 1, 4),
    _RcIgmpFilterProfileAction_Type()
)
rcIgmpFilterProfileAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIgmpFilterProfileAction.setStatus("current")
_RcIgmpFilterRowStatus_Type = RowStatus
_RcIgmpFilterRowStatus_Object = MibTableColumn
rcIgmpFilterRowStatus = _RcIgmpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 5, 1, 5),
    _RcIgmpFilterRowStatus_Type()
)
rcIgmpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIgmpFilterRowStatus.setStatus("current")
_RcIgmpFilterIFTable_Object = MibTable
rcIgmpFilterIFTable = _RcIgmpFilterIFTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 6)
)
if mibBuilder.loadTexts:
    rcIgmpFilterIFTable.setStatus("current")
_RcIgmpFilterIFEntry_Object = MibTableRow
rcIgmpFilterIFEntry = _RcIgmpFilterIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 6, 1)
)
rcIgmpFilterIFEntry.setIndexNames(
    (0, "SWITCH-MVR-MIB", "rcIgmpFilterIFPortIndex"),
)
if mibBuilder.loadTexts:
    rcIgmpFilterIFEntry.setStatus("current")
_RcIgmpFilterIFPortIndex_Type = Integer32
_RcIgmpFilterIFPortIndex_Object = MibTableColumn
rcIgmpFilterIFPortIndex = _RcIgmpFilterIFPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 6, 1, 1),
    _RcIgmpFilterIFPortIndex_Type()
)
rcIgmpFilterIFPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIgmpFilterIFPortIndex.setStatus("current")


class _RcIgmpFilterIFProfileIndex_Type(Integer32):
    """Custom type rcIgmpFilterIFProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RcIgmpFilterIFProfileIndex_Type.__name__ = "Integer32"
_RcIgmpFilterIFProfileIndex_Object = MibTableColumn
rcIgmpFilterIFProfileIndex = _RcIgmpFilterIFProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 6, 1, 2),
    _RcIgmpFilterIFProfileIndex_Type()
)
rcIgmpFilterIFProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpFilterIFProfileIndex.setStatus("current")


class _RcIgmpFilterIFMaxGroups_Type(Integer32):
    """Custom type rcIgmpFilterIFMaxGroups based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIgmpFilterIFMaxGroups_Type.__name__ = "Integer32"
_RcIgmpFilterIFMaxGroups_Object = MibTableColumn
rcIgmpFilterIFMaxGroups = _RcIgmpFilterIFMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 6, 1, 3),
    _RcIgmpFilterIFMaxGroups_Type()
)
rcIgmpFilterIFMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpFilterIFMaxGroups.setStatus("current")


class _RcIgmpFilterIFCurrentGroups_Type(Integer32):
    """Custom type rcIgmpFilterIFCurrentGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIgmpFilterIFCurrentGroups_Type.__name__ = "Integer32"
_RcIgmpFilterIFCurrentGroups_Object = MibTableColumn
rcIgmpFilterIFCurrentGroups = _RcIgmpFilterIFCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 6, 1, 4),
    _RcIgmpFilterIFCurrentGroups_Type()
)
rcIgmpFilterIFCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIgmpFilterIFCurrentGroups.setStatus("current")


class _RcIgmpFilterIFMaxGroupsAction_Type(Integer32):
    """Custom type rcIgmpFilterIFMaxGroupsAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("replace", 2))
    )


_RcIgmpFilterIFMaxGroupsAction_Type.__name__ = "Integer32"
_RcIgmpFilterIFMaxGroupsAction_Object = MibTableColumn
rcIgmpFilterIFMaxGroupsAction = _RcIgmpFilterIFMaxGroupsAction_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 6, 1, 5),
    _RcIgmpFilterIFMaxGroupsAction_Type()
)
rcIgmpFilterIFMaxGroupsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpFilterIFMaxGroupsAction.setStatus("current")
_RcIgmpFilterVlanTable_Object = MibTable
rcIgmpFilterVlanTable = _RcIgmpFilterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 7)
)
if mibBuilder.loadTexts:
    rcIgmpFilterVlanTable.setStatus("current")
_RcIgmpFilterVlanEntry_Object = MibTableRow
rcIgmpFilterVlanEntry = _RcIgmpFilterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 7, 1)
)
rcIgmpFilterVlanEntry.setIndexNames(
    (0, "SWITCH-MVR-MIB", "rcIgmpFilterIFPortIndex"),
)
if mibBuilder.loadTexts:
    rcIgmpFilterVlanEntry.setStatus("current")
_RcIgmpFilterVLANIndex_Type = Integer32
_RcIgmpFilterVLANIndex_Object = MibTableColumn
rcIgmpFilterVLANIndex = _RcIgmpFilterVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 7, 1, 1),
    _RcIgmpFilterVLANIndex_Type()
)
rcIgmpFilterVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIgmpFilterVLANIndex.setStatus("current")


class _RcIgmpFilterVlanProfileIndex_Type(Integer32):
    """Custom type rcIgmpFilterVlanProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RcIgmpFilterVlanProfileIndex_Type.__name__ = "Integer32"
_RcIgmpFilterVlanProfileIndex_Object = MibTableColumn
rcIgmpFilterVlanProfileIndex = _RcIgmpFilterVlanProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 7, 1, 2),
    _RcIgmpFilterVlanProfileIndex_Type()
)
rcIgmpFilterVlanProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpFilterVlanProfileIndex.setStatus("current")


class _RcIgmpFilterVlanMaxGroups_Type(Integer32):
    """Custom type rcIgmpFilterVlanMaxGroups based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIgmpFilterVlanMaxGroups_Type.__name__ = "Integer32"
_RcIgmpFilterVlanMaxGroups_Object = MibTableColumn
rcIgmpFilterVlanMaxGroups = _RcIgmpFilterVlanMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 7, 1, 3),
    _RcIgmpFilterVlanMaxGroups_Type()
)
rcIgmpFilterVlanMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpFilterVlanMaxGroups.setStatus("current")


class _RcIgmpFilterVlanCurrentGroups_Type(Integer32):
    """Custom type rcIgmpFilterVlanCurrentGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIgmpFilterVlanCurrentGroups_Type.__name__ = "Integer32"
_RcIgmpFilterVlanCurrentGroups_Object = MibTableColumn
rcIgmpFilterVlanCurrentGroups = _RcIgmpFilterVlanCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 7, 1, 4),
    _RcIgmpFilterVlanCurrentGroups_Type()
)
rcIgmpFilterVlanCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIgmpFilterVlanCurrentGroups.setStatus("current")


class _RcIgmpFilterVlanMaxGroupsAction_Type(Integer32):
    """Custom type rcIgmpFilterVlanMaxGroupsAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("replace", 2))
    )


_RcIgmpFilterVlanMaxGroupsAction_Type.__name__ = "Integer32"
_RcIgmpFilterVlanMaxGroupsAction_Object = MibTableColumn
rcIgmpFilterVlanMaxGroupsAction = _RcIgmpFilterVlanMaxGroupsAction_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 21, 2, 7, 1, 5),
    _RcIgmpFilterVlanMaxGroupsAction_Type()
)
rcIgmpFilterVlanMaxGroupsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpFilterVlanMaxGroupsAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-MVR-MIB",
    **{"rcMvr": rcMvr,
       "rcMvrConfig": rcMvrConfig,
       "rcMvrEnable": rcMvrEnable,
       "rcMvrVlan": rcMvrVlan,
       "rcMvrMaxGroups": rcMvrMaxGroups,
       "rcMvrCurrentGroups": rcMvrCurrentGroups,
       "rcMvrQureyTime": rcMvrQureyTime,
       "rcMvrOperMode": rcMvrOperMode,
       "rcMvrGroupTable": rcMvrGroupTable,
       "rcMvrGroupEntry": rcMvrGroupEntry,
       "rcMvrGroupVlan": rcMvrGroupVlan,
       "rcMvrGroupAddress": rcMvrGroupAddress,
       "rcMvrGroupRowStatus": rcMvrGroupRowStatus,
       "rcMvrIFTable": rcMvrIFTable,
       "rcMvrIFEntry": rcMvrIFEntry,
       "rcMvrPortIndex": rcMvrPortIndex,
       "rcMvrPortEnable": rcMvrPortEnable,
       "rcMvrType": rcMvrType,
       "rcMvrImmediate": rcMvrImmediate,
       "rcMvrPortStatus": rcMvrPortStatus,
       "rcMvrMemberTable": rcMvrMemberTable,
       "rcMvrMemberEntry": rcMvrMemberEntry,
       "rcMvrMemberPort": rcMvrMemberPort,
       "rcMvrMemberVlan": rcMvrMemberVlan,
       "rcMvrMemberGroupAddress": rcMvrMemberGroupAddress,
       "rcMvrMemberGroupType": rcMvrMemberGroupType,
       "rcMvrMemberRowStatus": rcMvrMemberRowStatus,
       "rcMvrMemberReplicableVlans": rcMvrMemberReplicableVlans,
       "rcMvrPortStatisticsTable": rcMvrPortStatisticsTable,
       "rcMvrPortStatisticsEntry": rcMvrPortStatisticsEntry,
       "rcMvrPortStatisticsPortid": rcMvrPortStatisticsPortid,
       "rcMvrPortStatisticsClear": rcMvrPortStatisticsClear,
       "rcMvrPortStatisticsRecvQueryPkts": rcMvrPortStatisticsRecvQueryPkts,
       "rcMvrPortStatisticsRecvReportPkts": rcMvrPortStatisticsRecvReportPkts,
       "rcMvrPortStatisticsRecvLeavePkts": rcMvrPortStatisticsRecvLeavePkts,
       "rcMvrPortStatisticsDropQueryPkts": rcMvrPortStatisticsDropQueryPkts,
       "rcMvrPortStatisticsDropReportPkts": rcMvrPortStatisticsDropReportPkts,
       "rcMvrPortStatisticsDropLeavePkts": rcMvrPortStatisticsDropLeavePkts,
       "rcMvrPortLastReplaceNewMulticast": rcMvrPortLastReplaceNewMulticast,
       "rcMvrPortLastReplaceOldMulticast": rcMvrPortLastReplaceOldMulticast,
       "rcMvrPortReplaceTotalCount": rcMvrPortReplaceTotalCount,
       "rcMvrProxySuppressionEnable": rcMvrProxySuppressionEnable,
       "rcIgmpQuerierEnable": rcIgmpQuerierEnable,
       "rcMvrProxySourceIpAddress": rcMvrProxySourceIpAddress,
       "rcIgmpQueryInterval": rcIgmpQueryInterval,
       "rcMvrProxyQueryMaxReponseInterval": rcMvrProxyQueryMaxReponseInterval,
       "rcMvrProxyQueryLastMemberInterval": rcMvrProxyQueryLastMemberInterval,
       "rcMvrIpmcReplicationEnable": rcMvrIpmcReplicationEnable,
       "rcIgmpFilterConfig": rcIgmpFilterConfig,
       "rcIgmpFilterEnable": rcIgmpFilterEnable,
       "rcIgmpFilterMaxProfiles": rcIgmpFilterMaxProfiles,
       "rcIgmpFilterAddEntry": rcIgmpFilterAddEntry,
       "rcIgmpFilterDelEntry": rcIgmpFilterDelEntry,
       "rcIgmpFilterTable": rcIgmpFilterTable,
       "rcIgmpFilterEntry": rcIgmpFilterEntry,
       "rcIgmpFilterProfileIndex": rcIgmpFilterProfileIndex,
       "rcIgmpFilterStartAddress": rcIgmpFilterStartAddress,
       "rcIgmpFilterEndAddress": rcIgmpFilterEndAddress,
       "rcIgmpFilterProfileAction": rcIgmpFilterProfileAction,
       "rcIgmpFilterRowStatus": rcIgmpFilterRowStatus,
       "rcIgmpFilterIFTable": rcIgmpFilterIFTable,
       "rcIgmpFilterIFEntry": rcIgmpFilterIFEntry,
       "rcIgmpFilterIFPortIndex": rcIgmpFilterIFPortIndex,
       "rcIgmpFilterIFProfileIndex": rcIgmpFilterIFProfileIndex,
       "rcIgmpFilterIFMaxGroups": rcIgmpFilterIFMaxGroups,
       "rcIgmpFilterIFCurrentGroups": rcIgmpFilterIFCurrentGroups,
       "rcIgmpFilterIFMaxGroupsAction": rcIgmpFilterIFMaxGroupsAction,
       "rcIgmpFilterVlanTable": rcIgmpFilterVlanTable,
       "rcIgmpFilterVlanEntry": rcIgmpFilterVlanEntry,
       "rcIgmpFilterVLANIndex": rcIgmpFilterVLANIndex,
       "rcIgmpFilterVlanProfileIndex": rcIgmpFilterVlanProfileIndex,
       "rcIgmpFilterVlanMaxGroups": rcIgmpFilterVlanMaxGroups,
       "rcIgmpFilterVlanCurrentGroups": rcIgmpFilterVlanCurrentGroups,
       "rcIgmpFilterVlanMaxGroupsAction": rcIgmpFilterVlanMaxGroupsAction}
)
