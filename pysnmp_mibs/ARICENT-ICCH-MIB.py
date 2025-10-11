# SNMP MIB module (ARICENT-ICCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-ICCH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:24 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsIcchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94)
)
if mibBuilder.loadTexts:
    fsIcchMIB.setRevisions(
        ("2014-12-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsIcchState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("master", 1),
          ("slave", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FsIcch_ObjectIdentity = ObjectIdentity
fsIcch = _FsIcch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 1)
)


class _FsIcchTrcLevel_Type(Unsigned32):
    """Custom type fsIcchTrcLevel based on Unsigned32"""
    defaultValue = 0


_FsIcchTrcLevel_Type.__name__ = "Unsigned32"
_FsIcchTrcLevel_Object = MibScalar
fsIcchTrcLevel = _FsIcchTrcLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 1, 1),
    _FsIcchTrcLevel_Type()
)
fsIcchTrcLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcchTrcLevel.setStatus("current")


class _FsIcchStatsEnable_Type(Integer32):
    """Custom type fsIcchStatsEnable based on Integer32"""
    defaultValue = 1

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


_FsIcchStatsEnable_Type.__name__ = "Integer32"
_FsIcchStatsEnable_Object = MibScalar
fsIcchStatsEnable = _FsIcchStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 1, 2),
    _FsIcchStatsEnable_Type()
)
fsIcchStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcchStatsEnable.setStatus("current")


class _FsIcchClearStats_Type(TruthValue):
    """Custom type fsIcchClearStats based on TruthValue"""
    defaultValue = 2


_FsIcchClearStats_Type.__name__ = "TruthValue"
_FsIcchClearStats_Object = MibScalar
fsIcchClearStats = _FsIcchClearStats_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 1, 3),
    _FsIcchClearStats_Type()
)
fsIcchClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcchClearStats.setStatus("current")


class _FsIcchEnableProtoSync_Type(Unsigned32):
    """Custom type fsIcchEnableProtoSync based on Unsigned32"""
    defaultValue = 0


_FsIcchEnableProtoSync_Type.__name__ = "Unsigned32"
_FsIcchEnableProtoSync_Object = MibScalar
fsIcchEnableProtoSync = _FsIcchEnableProtoSync_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 1, 4),
    _FsIcchEnableProtoSync_Type()
)
fsIcchEnableProtoSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcchEnableProtoSync.setStatus("current")


class _FsIcchFetchRemoteFdb_Type(TruthValue):
    """Custom type fsIcchFetchRemoteFdb based on TruthValue"""
    defaultValue = 2


_FsIcchFetchRemoteFdb_Type.__name__ = "TruthValue"
_FsIcchFetchRemoteFdb_Object = MibScalar
fsIcchFetchRemoteFdb = _FsIcchFetchRemoteFdb_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 1, 5),
    _FsIcchFetchRemoteFdb_Type()
)
fsIcchFetchRemoteFdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcchFetchRemoteFdb.setStatus("current")
_FsIcchPeerNodeIpAddress_Type = IpAddress
_FsIcchPeerNodeIpAddress_Object = MibScalar
fsIcchPeerNodeIpAddress = _FsIcchPeerNodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 1, 6),
    _FsIcchPeerNodeIpAddress_Type()
)
fsIcchPeerNodeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcchPeerNodeIpAddress.setStatus("current")
_FsIcchPeerNodeState_Type = FsIcchState
_FsIcchPeerNodeState_Object = MibScalar
fsIcchPeerNodeState = _FsIcchPeerNodeState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 1, 7),
    _FsIcchPeerNodeState_Type()
)
fsIcchPeerNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcchPeerNodeState.setStatus("current")
_FsIcchStatistics_ObjectIdentity = ObjectIdentity
fsIcchStatistics = _FsIcchStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 2)
)
_FsIcchStatsSyncMsgTxCount_Type = ZeroBasedCounter32
_FsIcchStatsSyncMsgTxCount_Object = MibScalar
fsIcchStatsSyncMsgTxCount = _FsIcchStatsSyncMsgTxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 2, 1),
    _FsIcchStatsSyncMsgTxCount_Type()
)
fsIcchStatsSyncMsgTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcchStatsSyncMsgTxCount.setStatus("current")
_FsIcchStatsSyncMsgTxFailedCount_Type = ZeroBasedCounter32
_FsIcchStatsSyncMsgTxFailedCount_Object = MibScalar
fsIcchStatsSyncMsgTxFailedCount = _FsIcchStatsSyncMsgTxFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 2, 2),
    _FsIcchStatsSyncMsgTxFailedCount_Type()
)
fsIcchStatsSyncMsgTxFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcchStatsSyncMsgTxFailedCount.setStatus("current")
_FsIcchStatsSyncMsgRxCount_Type = ZeroBasedCounter32
_FsIcchStatsSyncMsgRxCount_Object = MibScalar
fsIcchStatsSyncMsgRxCount = _FsIcchStatsSyncMsgRxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 2, 3),
    _FsIcchStatsSyncMsgRxCount_Type()
)
fsIcchStatsSyncMsgRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcchStatsSyncMsgRxCount.setStatus("current")
_FsIcchStatsSyncMsgProcCount_Type = ZeroBasedCounter32
_FsIcchStatsSyncMsgProcCount_Object = MibScalar
fsIcchStatsSyncMsgProcCount = _FsIcchStatsSyncMsgProcCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 2, 4),
    _FsIcchStatsSyncMsgProcCount_Type()
)
fsIcchStatsSyncMsgProcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcchStatsSyncMsgProcCount.setStatus("current")
_FsIcchStatsSyncMsgMissedCount_Type = ZeroBasedCounter32
_FsIcchStatsSyncMsgMissedCount_Object = MibScalar
fsIcchStatsSyncMsgMissedCount = _FsIcchStatsSyncMsgMissedCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 2, 5),
    _FsIcchStatsSyncMsgMissedCount_Type()
)
fsIcchStatsSyncMsgMissedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcchStatsSyncMsgMissedCount.setStatus("current")
_FsIcchNotification_ObjectIdentity = ObjectIdentity
fsIcchNotification = _FsIcchNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 3)
)
_FsIcchTrap_ObjectIdentity = ObjectIdentity
fsIcchTrap = _FsIcchTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 3, 0)
)
_FsIcclSession_ObjectIdentity = ObjectIdentity
fsIcclSession = _FsIcclSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4)
)
_FsIcclSessionTable_Object = MibTable
fsIcclSessionTable = _FsIcclSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4, 1)
)
if mibBuilder.loadTexts:
    fsIcclSessionTable.setStatus("current")
_FsIcclSessionEntry_Object = MibTableRow
fsIcclSessionEntry = _FsIcclSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4, 1, 1)
)
fsIcclSessionEntry.setIndexNames(
    (0, "ARICENT-ICCH-MIB", "fsIcclSessionInstanceId"),
)
if mibBuilder.loadTexts:
    fsIcclSessionEntry.setStatus("current")


class _FsIcclSessionInstanceId_Type(Unsigned32):
    """Custom type fsIcclSessionInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsIcclSessionInstanceId_Type.__name__ = "Unsigned32"
_FsIcclSessionInstanceId_Object = MibTableColumn
fsIcclSessionInstanceId = _FsIcclSessionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4, 1, 1, 1),
    _FsIcclSessionInstanceId_Type()
)
fsIcclSessionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIcclSessionInstanceId.setStatus("current")


class _FsIcclSessionInterface_Type(DisplayString):
    """Custom type fsIcclSessionInterface based on DisplayString"""
    defaultValue = OctetString("po4094")


_FsIcclSessionInterface_Type.__name__ = "DisplayString"
_FsIcclSessionInterface_Object = MibTableColumn
fsIcclSessionInterface = _FsIcclSessionInterface_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4, 1, 1, 2),
    _FsIcclSessionInterface_Type()
)
fsIcclSessionInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcclSessionInterface.setStatus("current")


class _FsIcclSessionIpAddress_Type(IpAddress):
    """Custom type fsIcclSessionIpAddress based on IpAddress"""
    defaultHexValue = "A9FE0101"


_FsIcclSessionIpAddress_Type.__name__ = "IpAddress"
_FsIcclSessionIpAddress_Object = MibTableColumn
fsIcclSessionIpAddress = _FsIcclSessionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4, 1, 1, 3),
    _FsIcclSessionIpAddress_Type()
)
fsIcclSessionIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcclSessionIpAddress.setStatus("current")


class _FsIcclSessionSubnetMask_Type(IpAddress):
    """Custom type fsIcclSessionSubnetMask based on IpAddress"""
    defaultHexValue = "FF000000"


_FsIcclSessionSubnetMask_Type.__name__ = "IpAddress"
_FsIcclSessionSubnetMask_Object = MibTableColumn
fsIcclSessionSubnetMask = _FsIcclSessionSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4, 1, 1, 4),
    _FsIcclSessionSubnetMask_Type()
)
fsIcclSessionSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcclSessionSubnetMask.setStatus("current")


class _FsIcclSessionVlan_Type(VlanId):
    """Custom type fsIcclSessionVlan based on VlanId"""
    defaultValue = 4094


_FsIcclSessionVlan_Type.__name__ = "VlanId"
_FsIcclSessionVlan_Object = MibTableColumn
fsIcclSessionVlan = _FsIcclSessionVlan_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4, 1, 1, 5),
    _FsIcclSessionVlan_Type()
)
fsIcclSessionVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcclSessionVlan.setStatus("current")
_FsIcclSessionNodeState_Type = FsIcchState
_FsIcclSessionNodeState_Object = MibTableColumn
fsIcclSessionNodeState = _FsIcclSessionNodeState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4, 1, 1, 6),
    _FsIcclSessionNodeState_Type()
)
fsIcclSessionNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcclSessionNodeState.setStatus("current")
_FsIcclSessionRowStatus_Type = RowStatus
_FsIcclSessionRowStatus_Object = MibTableColumn
fsIcclSessionRowStatus = _FsIcclSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 4, 1, 1, 7),
    _FsIcclSessionRowStatus_Type()
)
fsIcclSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcclSessionRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

fsIcchTrapNodeStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 3, 0, 1)
)
fsIcchTrapNodeStatusChange.setObjects(
      *(("ARICENT-ICCH-MIB", "fsIcclSessionNodeState"),
        ("ARICENT-ICCH-MIB", "fsIcclSessionInstanceId"),
        ("ARICENT-ICCH-MIB", "fsIcclSessionInterface"),
        ("ARICENT-ICCH-MIB", "fsIcclSessionIpAddress"),
        ("ARICENT-ICCH-MIB", "fsIcclSessionSubnetMask"),
        ("ARICENT-ICCH-MIB", "fsIcclSessionVlan"))
)
if mibBuilder.loadTexts:
    fsIcchTrapNodeStatusChange.setStatus(
        "current"
    )

fsIcchTrapPeerNodeStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 94, 3, 0, 2)
)
fsIcchTrapPeerNodeStatusChange.setObjects(
      *(("ARICENT-ICCH-MIB", "fsIcchPeerNodeIpAddress"),
        ("ARICENT-ICCH-MIB", "fsIcchPeerNodeState"))
)
if mibBuilder.loadTexts:
    fsIcchTrapPeerNodeStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ICCH-MIB",
    **{"FsIcchState": FsIcchState,
       "fsIcchMIB": fsIcchMIB,
       "fsIcch": fsIcch,
       "fsIcchTrcLevel": fsIcchTrcLevel,
       "fsIcchStatsEnable": fsIcchStatsEnable,
       "fsIcchClearStats": fsIcchClearStats,
       "fsIcchEnableProtoSync": fsIcchEnableProtoSync,
       "fsIcchFetchRemoteFdb": fsIcchFetchRemoteFdb,
       "fsIcchPeerNodeIpAddress": fsIcchPeerNodeIpAddress,
       "fsIcchPeerNodeState": fsIcchPeerNodeState,
       "fsIcchStatistics": fsIcchStatistics,
       "fsIcchStatsSyncMsgTxCount": fsIcchStatsSyncMsgTxCount,
       "fsIcchStatsSyncMsgTxFailedCount": fsIcchStatsSyncMsgTxFailedCount,
       "fsIcchStatsSyncMsgRxCount": fsIcchStatsSyncMsgRxCount,
       "fsIcchStatsSyncMsgProcCount": fsIcchStatsSyncMsgProcCount,
       "fsIcchStatsSyncMsgMissedCount": fsIcchStatsSyncMsgMissedCount,
       "fsIcchNotification": fsIcchNotification,
       "fsIcchTrap": fsIcchTrap,
       "fsIcchTrapNodeStatusChange": fsIcchTrapNodeStatusChange,
       "fsIcchTrapPeerNodeStatusChange": fsIcchTrapPeerNodeStatusChange,
       "fsIcclSession": fsIcclSession,
       "fsIcclSessionTable": fsIcclSessionTable,
       "fsIcclSessionEntry": fsIcclSessionEntry,
       "fsIcclSessionInstanceId": fsIcclSessionInstanceId,
       "fsIcclSessionInterface": fsIcclSessionInterface,
       "fsIcclSessionIpAddress": fsIcclSessionIpAddress,
       "fsIcclSessionSubnetMask": fsIcclSessionSubnetMask,
       "fsIcclSessionVlan": fsIcclSessionVlan,
       "fsIcclSessionNodeState": fsIcclSessionNodeState,
       "fsIcclSessionRowStatus": fsIcclSessionRowStatus}
)
