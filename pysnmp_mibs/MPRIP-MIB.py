# SNMP MIB module (MPRIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPRIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:03 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mpRipMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RipGlobals_ObjectIdentity = ObjectIdentity
ripGlobals = _RipGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1)
)


class _RipAutoSumm_Type(Integer32):
    """Custom type ripAutoSumm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuto-summary", 1),
          ("auto-summary", 2))
    )


_RipAutoSumm_Type.__name__ = "Integer32"
_RipAutoSumm_Object = MibScalar
ripAutoSumm = _RipAutoSumm_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 1),
    _RipAutoSumm_Type()
)
ripAutoSumm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAutoSumm.setStatus("current")


class _RipDefaultMetric_Type(Unsigned32):
    """Custom type ripDefaultMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RipDefaultMetric_Type.__name__ = "Unsigned32"
_RipDefaultMetric_Object = MibScalar
ripDefaultMetric = _RipDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 2),
    _RipDefaultMetric_Type()
)
ripDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripDefaultMetric.setStatus("current")


class _RipRedisOspfMetric_Type(Integer32):
    """Custom type ripRedisOspfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipRedisOspfMetric_Type.__name__ = "Integer32"
_RipRedisOspfMetric_Object = MibScalar
ripRedisOspfMetric = _RipRedisOspfMetric_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 3),
    _RipRedisOspfMetric_Type()
)
ripRedisOspfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripRedisOspfMetric.setStatus("current")


class _RipRedisStaticMetric_Type(Integer32):
    """Custom type ripRedisStaticMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipRedisStaticMetric_Type.__name__ = "Integer32"
_RipRedisStaticMetric_Object = MibScalar
ripRedisStaticMetric = _RipRedisStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 4),
    _RipRedisStaticMetric_Type()
)
ripRedisStaticMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripRedisStaticMetric.setStatus("current")


class _RipRedisSnspMetic_Type(Integer32):
    """Custom type ripRedisSnspMetic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipRedisSnspMetic_Type.__name__ = "Integer32"
_RipRedisSnspMetic_Object = MibScalar
ripRedisSnspMetic = _RipRedisSnspMetic_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 5),
    _RipRedisSnspMetic_Type()
)
ripRedisSnspMetic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripRedisSnspMetic.setStatus("current")


class _RipRedisBgpMetric_Type(Integer32):
    """Custom type ripRedisBgpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipRedisBgpMetric_Type.__name__ = "Integer32"
_RipRedisBgpMetric_Object = MibScalar
ripRedisBgpMetric = _RipRedisBgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 6),
    _RipRedisBgpMetric_Type()
)
ripRedisBgpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripRedisBgpMetric.setStatus("current")


class _RipRedisConnectedMetric_Type(Integer32):
    """Custom type ripRedisConnectedMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipRedisConnectedMetric_Type.__name__ = "Integer32"
_RipRedisConnectedMetric_Object = MibScalar
ripRedisConnectedMetric = _RipRedisConnectedMetric_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 7),
    _RipRedisConnectedMetric_Type()
)
ripRedisConnectedMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripRedisConnectedMetric.setStatus("current")


class _RipDistance_Type(Unsigned32):
    """Custom type ripDistance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RipDistance_Type.__name__ = "Unsigned32"
_RipDistance_Object = MibScalar
ripDistance = _RipDistance_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 8),
    _RipDistance_Type()
)
ripDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripDistance.setStatus("current")
_RipUpdate_Type = Unsigned32
_RipUpdate_Object = MibScalar
ripUpdate = _RipUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 9),
    _RipUpdate_Type()
)
ripUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripUpdate.setStatus("current")
_RipHolddown_Type = Unsigned32
_RipHolddown_Object = MibScalar
ripHolddown = _RipHolddown_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 10),
    _RipHolddown_Type()
)
ripHolddown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripHolddown.setStatus("current")


class _RipInvalid_Type(Unsigned32):
    """Custom type ripInvalid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RipInvalid_Type.__name__ = "Unsigned32"
_RipInvalid_Object = MibScalar
ripInvalid = _RipInvalid_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 11),
    _RipInvalid_Type()
)
ripInvalid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInvalid.setStatus("current")


class _RipFlush_Type(Unsigned32):
    """Custom type ripFlush based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RipFlush_Type.__name__ = "Unsigned32"
_RipFlush_Object = MibScalar
ripFlush = _RipFlush_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 12),
    _RipFlush_Type()
)
ripFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripFlush.setStatus("current")


class _RipVersion_Type(Integer32):
    """Custom type ripVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ripVer1", 1),
          ("ripVer2", 2))
    )


_RipVersion_Type.__name__ = "Integer32"
_RipVersion_Object = MibScalar
ripVersion = _RipVersion_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 13),
    _RipVersion_Type()
)
ripVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripVersion.setStatus("current")


class _RipMaxPath_Type(Integer32):
    """Custom type ripMaxPath based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_RipMaxPath_Type.__name__ = "Integer32"
_RipMaxPath_Object = MibScalar
ripMaxPath = _RipMaxPath_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 1, 14),
    _RipMaxPath_Type()
)
ripMaxPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripMaxPath.setStatus("current")
_RipNet_ObjectIdentity = ObjectIdentity
ripNet = _RipNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2)
)
_RipNetworkTable_Object = MibTable
ripNetworkTable = _RipNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 1)
)
if mibBuilder.loadTexts:
    ripNetworkTable.setStatus("current")
_RipNetworkEntry_Object = MibTableRow
ripNetworkEntry = _RipNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 1, 1)
)
ripNetworkEntry.setIndexNames(
    (0, "MPRIP-MIB", "ripNetworkNum"),
)
if mibBuilder.loadTexts:
    ripNetworkEntry.setStatus("current")
_RipNetworkNum_Type = IpAddress
_RipNetworkNum_Object = MibTableColumn
ripNetworkNum = _RipNetworkNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 1, 1, 1),
    _RipNetworkNum_Type()
)
ripNetworkNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNetworkNum.setStatus("current")
_RipNetworkStatus_Type = RowStatus
_RipNetworkStatus_Object = MibTableColumn
ripNetworkStatus = _RipNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 1, 1, 2),
    _RipNetworkStatus_Type()
)
ripNetworkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNetworkStatus.setStatus("current")
_RipNeighborTable_Object = MibTable
ripNeighborTable = _RipNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 2)
)
if mibBuilder.loadTexts:
    ripNeighborTable.setStatus("current")
_RipNeighborEntry_Object = MibTableRow
ripNeighborEntry = _RipNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 2, 1)
)
ripNeighborEntry.setIndexNames(
    (0, "MPRIP-MIB", "ripNeighborAddr"),
)
if mibBuilder.loadTexts:
    ripNeighborEntry.setStatus("current")
_RipNeighborAddr_Type = IpAddress
_RipNeighborAddr_Object = MibTableColumn
ripNeighborAddr = _RipNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 2, 1, 1),
    _RipNeighborAddr_Type()
)
ripNeighborAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNeighborAddr.setStatus("current")
_RipNeighborStatus_Type = RowStatus
_RipNeighborStatus_Object = MibTableColumn
ripNeighborStatus = _RipNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 2, 1, 2),
    _RipNeighborStatus_Type()
)
ripNeighborStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNeighborStatus.setStatus("current")
_RipRedisIrmpTable_Object = MibTable
ripRedisIrmpTable = _RipRedisIrmpTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 3)
)
if mibBuilder.loadTexts:
    ripRedisIrmpTable.setStatus("current")
_RipRedisIrmpEntry_Object = MibTableRow
ripRedisIrmpEntry = _RipRedisIrmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 3, 1)
)
ripRedisIrmpEntry.setIndexNames(
    (0, "MPRIP-MIB", "ripRedisIrmpAutoNo"),
)
if mibBuilder.loadTexts:
    ripRedisIrmpEntry.setStatus("current")


class _RipRedisIrmpAutoNo_Type(Integer32):
    """Custom type ripRedisIrmpAutoNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RipRedisIrmpAutoNo_Type.__name__ = "Integer32"
_RipRedisIrmpAutoNo_Object = MibTableColumn
ripRedisIrmpAutoNo = _RipRedisIrmpAutoNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 3, 1, 1),
    _RipRedisIrmpAutoNo_Type()
)
ripRedisIrmpAutoNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripRedisIrmpAutoNo.setStatus("current")


class _RipRedisIrmpMetric_Type(Integer32):
    """Custom type ripRedisIrmpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipRedisIrmpMetric_Type.__name__ = "Integer32"
_RipRedisIrmpMetric_Object = MibTableColumn
ripRedisIrmpMetric = _RipRedisIrmpMetric_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 3, 1, 2),
    _RipRedisIrmpMetric_Type()
)
ripRedisIrmpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripRedisIrmpMetric.setStatus("current")
_RipRedisIrmpStatus_Type = RowStatus
_RipRedisIrmpStatus_Object = MibTableColumn
ripRedisIrmpStatus = _RipRedisIrmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 2, 3, 1, 3),
    _RipRedisIrmpStatus_Type()
)
ripRedisIrmpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripRedisIrmpStatus.setStatus("current")
_RipIf_ObjectIdentity = ObjectIdentity
ripIf = _RipIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3)
)
_RipIfStatTable_Object = MibTable
ripIfStatTable = _RipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1)
)
if mibBuilder.loadTexts:
    ripIfStatTable.setStatus("current")
_RipIfStatEntry_Object = MibTableRow
ripIfStatEntry = _RipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1)
)
ripIfStatEntry.setIndexNames(
    (0, "MPRIP-MIB", "ripIfStatIndex"),
)
if mibBuilder.loadTexts:
    ripIfStatEntry.setStatus("current")
_RipIfStatIndex_Type = Unsigned32
_RipIfStatIndex_Object = MibTableColumn
ripIfStatIndex = _RipIfStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 1),
    _RipIfStatIndex_Type()
)
ripIfStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatIndex.setStatus("current")


class _RipIfStatType_Type(Integer32):
    """Custom type ripIfStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("point-to-point", 1),
          ("lookback", 2),
          ("broadcast", 3))
    )


_RipIfStatType_Type.__name__ = "Integer32"
_RipIfStatType_Object = MibTableColumn
ripIfStatType = _RipIfStatType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 2),
    _RipIfStatType_Type()
)
ripIfStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatType.setStatus("current")


class _RipIfStatStatus_Type(Integer32):
    """Custom type ripIfStatStatus based on Integer32"""
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


_RipIfStatStatus_Type.__name__ = "Integer32"
_RipIfStatStatus_Object = MibTableColumn
ripIfStatStatus = _RipIfStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 3),
    _RipIfStatStatus_Type()
)
ripIfStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatStatus.setStatus("current")
_RipIfStatLocalAddr_Type = IpAddress
_RipIfStatLocalAddr_Object = MibTableColumn
ripIfStatLocalAddr = _RipIfStatLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 4),
    _RipIfStatLocalAddr_Type()
)
ripIfStatLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatLocalAddr.setStatus("current")
_RipIfStatRemoteAddr_Type = IpAddress
_RipIfStatRemoteAddr_Object = MibTableColumn
ripIfStatRemoteAddr = _RipIfStatRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 5),
    _RipIfStatRemoteAddr_Type()
)
ripIfStatRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatRemoteAddr.setStatus("current")
_RipIfStatUniqueAddr_Type = IpAddress
_RipIfStatUniqueAddr_Object = MibTableColumn
ripIfStatUniqueAddr = _RipIfStatUniqueAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 6),
    _RipIfStatUniqueAddr_Type()
)
ripIfStatUniqueAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatUniqueAddr.setStatus("current")
_RipIfStatRecvBadPkts_Type = Counter32
_RipIfStatRecvBadPkts_Object = MibTableColumn
ripIfStatRecvBadPkts = _RipIfStatRecvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 7),
    _RipIfStatRecvBadPkts_Type()
)
ripIfStatRecvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatRecvBadPkts.setStatus("current")
_RipIfStatRecvBadRoutes_Type = Counter32
_RipIfStatRecvBadRoutes_Object = MibTableColumn
ripIfStatRecvBadRoutes = _RipIfStatRecvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 8),
    _RipIfStatRecvBadRoutes_Type()
)
ripIfStatRecvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatRecvBadRoutes.setStatus("current")
_RipIfStatRecvPkts_Type = Counter32
_RipIfStatRecvPkts_Object = MibTableColumn
ripIfStatRecvPkts = _RipIfStatRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 9),
    _RipIfStatRecvPkts_Type()
)
ripIfStatRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatRecvPkts.setStatus("current")
_RipIfStatSendPkts_Type = Counter32
_RipIfStatSendPkts_Object = MibTableColumn
ripIfStatSendPkts = _RipIfStatSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 10),
    _RipIfStatSendPkts_Type()
)
ripIfStatSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatSendPkts.setStatus("current")
_RipIfStatSendErrors_Type = Counter32
_RipIfStatSendErrors_Object = MibTableColumn
ripIfStatSendErrors = _RipIfStatSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 1, 1, 11),
    _RipIfStatSendErrors_Type()
)
ripIfStatSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatSendErrors.setStatus("current")
_RipIfConfTable_Object = MibTable
ripIfConfTable = _RipIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2)
)
if mibBuilder.loadTexts:
    ripIfConfTable.setStatus("current")
_RipIfConfEntry_Object = MibTableRow
ripIfConfEntry = _RipIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1)
)
ripIfConfEntry.setIndexNames(
    (0, "MPRIP-MIB", "ripIfConfIndex"),
)
if mibBuilder.loadTexts:
    ripIfConfEntry.setStatus("current")
_RipIfConfIndex_Type = Unsigned32
_RipIfConfIndex_Object = MibTableColumn
ripIfConfIndex = _RipIfConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1, 1),
    _RipIfConfIndex_Type()
)
ripIfConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfConfIndex.setStatus("current")
_RipIfConfIp_Type = IpAddress
_RipIfConfIp_Object = MibTableColumn
ripIfConfIp = _RipIfConfIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1, 2),
    _RipIfConfIp_Type()
)
ripIfConfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfConfIp.setStatus("current")


class _RipIfConfPassive_Type(Integer32):
    """Custom type ripIfConfPassive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("suppress", 1),
          ("noSuppress", 2))
    )


_RipIfConfPassive_Type.__name__ = "Integer32"
_RipIfConfPassive_Object = MibTableColumn
ripIfConfPassive = _RipIfConfPassive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1, 3),
    _RipIfConfPassive_Type()
)
ripIfConfPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripIfConfPassive.setStatus("current")


class _RipIfConfAuthMode_Type(Integer32):
    """Custom type ripIfConfAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthentication", 1),
          ("simplePassword", 2),
          ("md5", 3))
    )


_RipIfConfAuthMode_Type.__name__ = "Integer32"
_RipIfConfAuthMode_Object = MibTableColumn
ripIfConfAuthMode = _RipIfConfAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1, 4),
    _RipIfConfAuthMode_Type()
)
ripIfConfAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripIfConfAuthMode.setStatus("current")


class _RipIfConfAuthKey_Type(Integer32):
    """Custom type ripIfConfAuthKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noEncrypt", 1),
          ("encrypt", 2))
    )


_RipIfConfAuthKey_Type.__name__ = "Integer32"
_RipIfConfAuthKey_Object = MibTableColumn
ripIfConfAuthKey = _RipIfConfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1, 5),
    _RipIfConfAuthKey_Type()
)
ripIfConfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripIfConfAuthKey.setStatus("current")


class _RipIfConfAuthPwd_Type(OctetString):
    """Custom type ripIfConfAuthPwd based on OctetString"""
    defaultHexValue = ""


_RipIfConfAuthPwd_Type.__name__ = "OctetString"
_RipIfConfAuthPwd_Object = MibTableColumn
ripIfConfAuthPwd = _RipIfConfAuthPwd_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1, 6),
    _RipIfConfAuthPwd_Type()
)
ripIfConfAuthPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripIfConfAuthPwd.setStatus("current")


class _RipIfConfRecvVer_Type(Integer32):
    """Custom type ripIfConfRecvVer based on Integer32"""
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
        *(("rip1", 1),
          ("rip2", 2),
          ("rip1Orrip2", 3))
    )


_RipIfConfRecvVer_Type.__name__ = "Integer32"
_RipIfConfRecvVer_Object = MibTableColumn
ripIfConfRecvVer = _RipIfConfRecvVer_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1, 7),
    _RipIfConfRecvVer_Type()
)
ripIfConfRecvVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripIfConfRecvVer.setStatus("current")


class _RipIfConfSendVer_Type(Integer32):
    """Custom type ripIfConfSendVer based on Integer32"""
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
        *(("rip1", 1),
          ("rip2", 2),
          ("rip1Orrip2", 3),
          ("ripNoSend", 4))
    )


_RipIfConfSendVer_Type.__name__ = "Integer32"
_RipIfConfSendVer_Object = MibTableColumn
ripIfConfSendVer = _RipIfConfSendVer_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1, 8),
    _RipIfConfSendVer_Type()
)
ripIfConfSendVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripIfConfSendVer.setStatus("current")
_RipIfConfStatus_Type = RowStatus
_RipIfConfStatus_Object = MibTableColumn
ripIfConfStatus = _RipIfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 11, 3, 2, 1, 9),
    _RipIfConfStatus_Type()
)
ripIfConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripIfConfStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPRIP-MIB",
    **{"mpRipMib": mpRipMib,
       "ripGlobals": ripGlobals,
       "ripAutoSumm": ripAutoSumm,
       "ripDefaultMetric": ripDefaultMetric,
       "ripRedisOspfMetric": ripRedisOspfMetric,
       "ripRedisStaticMetric": ripRedisStaticMetric,
       "ripRedisSnspMetic": ripRedisSnspMetic,
       "ripRedisBgpMetric": ripRedisBgpMetric,
       "ripRedisConnectedMetric": ripRedisConnectedMetric,
       "ripDistance": ripDistance,
       "ripUpdate": ripUpdate,
       "ripHolddown": ripHolddown,
       "ripInvalid": ripInvalid,
       "ripFlush": ripFlush,
       "ripVersion": ripVersion,
       "ripMaxPath": ripMaxPath,
       "ripNet": ripNet,
       "ripNetworkTable": ripNetworkTable,
       "ripNetworkEntry": ripNetworkEntry,
       "ripNetworkNum": ripNetworkNum,
       "ripNetworkStatus": ripNetworkStatus,
       "ripNeighborTable": ripNeighborTable,
       "ripNeighborEntry": ripNeighborEntry,
       "ripNeighborAddr": ripNeighborAddr,
       "ripNeighborStatus": ripNeighborStatus,
       "ripRedisIrmpTable": ripRedisIrmpTable,
       "ripRedisIrmpEntry": ripRedisIrmpEntry,
       "ripRedisIrmpAutoNo": ripRedisIrmpAutoNo,
       "ripRedisIrmpMetric": ripRedisIrmpMetric,
       "ripRedisIrmpStatus": ripRedisIrmpStatus,
       "ripIf": ripIf,
       "ripIfStatTable": ripIfStatTable,
       "ripIfStatEntry": ripIfStatEntry,
       "ripIfStatIndex": ripIfStatIndex,
       "ripIfStatType": ripIfStatType,
       "ripIfStatStatus": ripIfStatStatus,
       "ripIfStatLocalAddr": ripIfStatLocalAddr,
       "ripIfStatRemoteAddr": ripIfStatRemoteAddr,
       "ripIfStatUniqueAddr": ripIfStatUniqueAddr,
       "ripIfStatRecvBadPkts": ripIfStatRecvBadPkts,
       "ripIfStatRecvBadRoutes": ripIfStatRecvBadRoutes,
       "ripIfStatRecvPkts": ripIfStatRecvPkts,
       "ripIfStatSendPkts": ripIfStatSendPkts,
       "ripIfStatSendErrors": ripIfStatSendErrors,
       "ripIfConfTable": ripIfConfTable,
       "ripIfConfEntry": ripIfConfEntry,
       "ripIfConfIndex": ripIfConfIndex,
       "ripIfConfIp": ripIfConfIp,
       "ripIfConfPassive": ripIfConfPassive,
       "ripIfConfAuthMode": ripIfConfAuthMode,
       "ripIfConfAuthKey": ripIfConfAuthKey,
       "ripIfConfAuthPwd": ripIfConfAuthPwd,
       "ripIfConfRecvVer": ripIfConfRecvVer,
       "ripIfConfSendVer": ripIfConfSendVer,
       "ripIfConfStatus": ripIfConfStatus}
)
