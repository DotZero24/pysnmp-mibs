# SNMP MIB module (ZTE-DSL-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-STATS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:03 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(zxDsl,) = mibBuilder.importSymbols(
    "ZTE-DSL-MIB",
    "zxDsl")


# MODULE-IDENTITY

zxDslStaticsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxDslStatsObjects_ObjectIdentity = ObjectIdentity
zxDslStatsObjects = _ZxDslStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1)
)
_ZxDslEtherStatsTable_Object = MibTable
zxDslEtherStatsTable = _ZxDslEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1)
)
if mibBuilder.loadTexts:
    zxDslEtherStatsTable.setStatus("current")
_ZxDslEtherStatsEntry_Object = MibTableRow
zxDslEtherStatsEntry = _ZxDslEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1)
)
zxDslEtherStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxDslEtherStatsEntry.setStatus("current")
_ZxDslEtherRxRate_Type = Gauge32
_ZxDslEtherRxRate_Object = MibTableColumn
zxDslEtherRxRate = _ZxDslEtherRxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 1),
    _ZxDslEtherRxRate_Type()
)
zxDslEtherRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherRxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherRxRate.setUnits("BYTES/S")
_ZxDslEtherTxRate_Type = Gauge32
_ZxDslEtherTxRate_Object = MibTableColumn
zxDslEtherTxRate = _ZxDslEtherTxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 2),
    _ZxDslEtherTxRate_Type()
)
zxDslEtherTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherTxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherTxRate.setUnits("BYTES/S")
_ZxDslEtherRxDiscardRatio_Type = Integer32
_ZxDslEtherRxDiscardRatio_Object = MibTableColumn
zxDslEtherRxDiscardRatio = _ZxDslEtherRxDiscardRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 3),
    _ZxDslEtherRxDiscardRatio_Type()
)
zxDslEtherRxDiscardRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherRxDiscardRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherRxDiscardRatio.setUnits("percent")
_ZxDslEtherTxDiscardRatio_Type = Integer32
_ZxDslEtherTxDiscardRatio_Object = MibTableColumn
zxDslEtherTxDiscardRatio = _ZxDslEtherTxDiscardRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 4),
    _ZxDslEtherTxDiscardRatio_Type()
)
zxDslEtherTxDiscardRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherTxDiscardRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherTxDiscardRatio.setUnits("percent")
_ZxDslEtherBroadcastRxRate_Type = Gauge32
_ZxDslEtherBroadcastRxRate_Object = MibTableColumn
zxDslEtherBroadcastRxRate = _ZxDslEtherBroadcastRxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 5),
    _ZxDslEtherBroadcastRxRate_Type()
)
zxDslEtherBroadcastRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherBroadcastRxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherBroadcastRxRate.setUnits("BYTES/S")
_ZxDslEtherBroadcastTxRate_Type = Gauge32
_ZxDslEtherBroadcastTxRate_Object = MibTableColumn
zxDslEtherBroadcastTxRate = _ZxDslEtherBroadcastTxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 6),
    _ZxDslEtherBroadcastTxRate_Type()
)
zxDslEtherBroadcastTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherBroadcastTxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherBroadcastTxRate.setUnits("BYTES/S")
_ZxDslEtherMulticastRxRate_Type = Gauge32
_ZxDslEtherMulticastRxRate_Object = MibTableColumn
zxDslEtherMulticastRxRate = _ZxDslEtherMulticastRxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 7),
    _ZxDslEtherMulticastRxRate_Type()
)
zxDslEtherMulticastRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherMulticastRxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherMulticastRxRate.setUnits("BYTES/S")
_ZxDslEtherMulticastTxRate_Type = Gauge32
_ZxDslEtherMulticastTxRate_Object = MibTableColumn
zxDslEtherMulticastTxRate = _ZxDslEtherMulticastTxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 8),
    _ZxDslEtherMulticastTxRate_Type()
)
zxDslEtherMulticastTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherMulticastTxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherMulticastTxRate.setUnits("BYTES/S")
_ZxDslEtherUnicastRxRate_Type = Gauge32
_ZxDslEtherUnicastRxRate_Object = MibTableColumn
zxDslEtherUnicastRxRate = _ZxDslEtherUnicastRxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 9),
    _ZxDslEtherUnicastRxRate_Type()
)
zxDslEtherUnicastRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherUnicastRxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherUnicastRxRate.setUnits("BYTES/S")
_ZxDslEtherUnicastTxRate_Type = Gauge32
_ZxDslEtherUnicastTxRate_Object = MibTableColumn
zxDslEtherUnicastTxRate = _ZxDslEtherUnicastTxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 1, 1, 10),
    _ZxDslEtherUnicastTxRate_Type()
)
zxDslEtherUnicastTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEtherUnicastTxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEtherUnicastTxRate.setUnits("BYTES/S")
_ZxDslBridgePortStatsTable_Object = MibTable
zxDslBridgePortStatsTable = _ZxDslBridgePortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 2)
)
if mibBuilder.loadTexts:
    zxDslBridgePortStatsTable.setStatus("current")
_ZxDslBridgePortStatsEntry_Object = MibTableRow
zxDslBridgePortStatsEntry = _ZxDslBridgePortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 2, 1)
)
zxDslBridgePortStatsEntry.setIndexNames(
    (0, "ZTE-DSL-STATS-MIB", "zxDslCardIndex"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zxDslBridgePortStatsEntry.setStatus("current")
_ZxDslBridgePortRxRate_Type = Gauge32
_ZxDslBridgePortRxRate_Object = MibTableColumn
zxDslBridgePortRxRate = _ZxDslBridgePortRxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 2, 1, 1),
    _ZxDslBridgePortRxRate_Type()
)
zxDslBridgePortRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslBridgePortRxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslBridgePortRxRate.setUnits("BYTES/S")
_ZxDslBridgePortTxRate_Type = Gauge32
_ZxDslBridgePortTxRate_Object = MibTableColumn
zxDslBridgePortTxRate = _ZxDslBridgePortTxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 2, 1, 2),
    _ZxDslBridgePortTxRate_Type()
)
zxDslBridgePortTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslBridgePortTxRate.setStatus("current")
if mibBuilder.loadTexts:
    zxDslBridgePortTxRate.setUnits("BYTES/S")
_ZxDslBridgePortSelfLoopPkts_Type = Counter32
_ZxDslBridgePortSelfLoopPkts_Object = MibTableColumn
zxDslBridgePortSelfLoopPkts = _ZxDslBridgePortSelfLoopPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 2, 1, 3),
    _ZxDslBridgePortSelfLoopPkts_Type()
)
zxDslBridgePortSelfLoopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslBridgePortSelfLoopPkts.setStatus("current")
_ZxDslCardResourcesPerfTable_Object = MibTable
zxDslCardResourcesPerfTable = _ZxDslCardResourcesPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 3)
)
if mibBuilder.loadTexts:
    zxDslCardResourcesPerfTable.setStatus("current")
_ZxDslCardResourcesPerfEntry_Object = MibTableRow
zxDslCardResourcesPerfEntry = _ZxDslCardResourcesPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 3, 1)
)
zxDslCardResourcesPerfEntry.setIndexNames(
    (0, "ZTE-DSL-STATS-MIB", "zxDslCardIndex"),
)
if mibBuilder.loadTexts:
    zxDslCardResourcesPerfEntry.setStatus("current")
_ZxDslCardIndex_Type = Integer32
_ZxDslCardIndex_Object = MibTableColumn
zxDslCardIndex = _ZxDslCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 3, 1, 1),
    _ZxDslCardIndex_Type()
)
zxDslCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslCardIndex.setStatus("current")
_ZxDslCardCPULoad_Type = Integer32
_ZxDslCardCPULoad_Object = MibTableColumn
zxDslCardCPULoad = _ZxDslCardCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 3, 1, 2),
    _ZxDslCardCPULoad_Type()
)
zxDslCardCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslCardCPULoad.setStatus("current")
if mibBuilder.loadTexts:
    zxDslCardCPULoad.setUnits("percent")
_ZxDslCardMemUsage_Type = Integer32
_ZxDslCardMemUsage_Object = MibTableColumn
zxDslCardMemUsage = _ZxDslCardMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 3, 1, 3),
    _ZxDslCardMemUsage_Type()
)
zxDslCardMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslCardMemUsage.setStatus("current")
_ZxDslCardActivedPortNum_Type = Integer32
_ZxDslCardActivedPortNum_Object = MibTableColumn
zxDslCardActivedPortNum = _ZxDslCardActivedPortNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 3, 1, 4),
    _ZxDslCardActivedPortNum_Type()
)
zxDslCardActivedPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslCardActivedPortNum.setStatus("current")
_ZxDslL2ResourcesStat_ObjectIdentity = ObjectIdentity
zxDslL2ResourcesStat = _ZxDslL2ResourcesStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4)
)


class _ZxDslMacTableUsageMornitorPeriod_Type(Integer32):
    """Custom type zxDslMacTableUsageMornitorPeriod based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_ZxDslMacTableUsageMornitorPeriod_Type.__name__ = "Integer32"
_ZxDslMacTableUsageMornitorPeriod_Object = MibScalar
zxDslMacTableUsageMornitorPeriod = _ZxDslMacTableUsageMornitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 1),
    _ZxDslMacTableUsageMornitorPeriod_Type()
)
zxDslMacTableUsageMornitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslMacTableUsageMornitorPeriod.setStatus("current")
if mibBuilder.loadTexts:
    zxDslMacTableUsageMornitorPeriod.setUnits("second")


class _ZxDslMacTableUsageMornitorTimes_Type(Integer32):
    """Custom type zxDslMacTableUsageMornitorTimes based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ZxDslMacTableUsageMornitorTimes_Type.__name__ = "Integer32"
_ZxDslMacTableUsageMornitorTimes_Object = MibScalar
zxDslMacTableUsageMornitorTimes = _ZxDslMacTableUsageMornitorTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 2),
    _ZxDslMacTableUsageMornitorTimes_Type()
)
zxDslMacTableUsageMornitorTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslMacTableUsageMornitorTimes.setStatus("current")
_ZxDslMacTableUsageMornitorElapsedTime_Type = Integer32
_ZxDslMacTableUsageMornitorElapsedTime_Object = MibScalar
zxDslMacTableUsageMornitorElapsedTime = _ZxDslMacTableUsageMornitorElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 3),
    _ZxDslMacTableUsageMornitorElapsedTime_Type()
)
zxDslMacTableUsageMornitorElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslMacTableUsageMornitorElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    zxDslMacTableUsageMornitorElapsedTime.setUnits("second")
_ZxDslMacTableMaxSize_Type = Integer32
_ZxDslMacTableMaxSize_Object = MibScalar
zxDslMacTableMaxSize = _ZxDslMacTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 4),
    _ZxDslMacTableMaxSize_Type()
)
zxDslMacTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslMacTableMaxSize.setStatus("current")
_ZxDslMacTableCurrentUsage_Type = Integer32
_ZxDslMacTableCurrentUsage_Object = MibScalar
zxDslMacTableCurrentUsage = _ZxDslMacTableCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 5),
    _ZxDslMacTableCurrentUsage_Type()
)
zxDslMacTableCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslMacTableCurrentUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxDslMacTableCurrentUsage.setUnits("percent")


class _ZxDslMacTableUsageThreshold_Type(Integer32):
    """Custom type zxDslMacTableUsageThreshold based on Integer32"""
    defaultValue = 70


_ZxDslMacTableUsageThreshold_Type.__name__ = "Integer32"
_ZxDslMacTableUsageThreshold_Object = MibScalar
zxDslMacTableUsageThreshold = _ZxDslMacTableUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 6),
    _ZxDslMacTableUsageThreshold_Type()
)
zxDslMacTableUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslMacTableUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxDslMacTableUsageThreshold.setUnits("percent")
_ZxDslMacTableStatTable_Object = MibTable
zxDslMacTableStatTable = _ZxDslMacTableStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 7)
)
if mibBuilder.loadTexts:
    zxDslMacTableStatTable.setStatus("current")
_ZxDslMacTableStatEntry_Object = MibTableRow
zxDslMacTableStatEntry = _ZxDslMacTableStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 7, 1)
)
zxDslMacTableStatEntry.setIndexNames(
    (0, "ZTE-DSL-STATS-MIB", "zxDslMacTableStatSampleIndex"),
)
if mibBuilder.loadTexts:
    zxDslMacTableStatEntry.setStatus("current")
_ZxDslMacTableStatSampleIndex_Type = Integer32
_ZxDslMacTableStatSampleIndex_Object = MibTableColumn
zxDslMacTableStatSampleIndex = _ZxDslMacTableStatSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 7, 1, 1),
    _ZxDslMacTableStatSampleIndex_Type()
)
zxDslMacTableStatSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslMacTableStatSampleIndex.setStatus("current")
_ZxDslMacTableCurrentMaxUsage_Type = Integer32
_ZxDslMacTableCurrentMaxUsage_Object = MibTableColumn
zxDslMacTableCurrentMaxUsage = _ZxDslMacTableCurrentMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 7, 1, 2),
    _ZxDslMacTableCurrentMaxUsage_Type()
)
zxDslMacTableCurrentMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslMacTableCurrentMaxUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxDslMacTableCurrentMaxUsage.setUnits("percent")
_ZxDslPortQueueSampleTable_Object = MibTable
zxDslPortQueueSampleTable = _ZxDslPortQueueSampleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 8)
)
if mibBuilder.loadTexts:
    zxDslPortQueueSampleTable.setStatus("current")
_ZxDslPortQueueSampleEntry_Object = MibTableRow
zxDslPortQueueSampleEntry = _ZxDslPortQueueSampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 8, 1)
)
zxDslPortQueueSampleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxDslPortQueueSampleEntry.setStatus("current")


class _ZxDslQueueUsageMornitorPeriod_Type(Integer32):
    """Custom type zxDslQueueUsageMornitorPeriod based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_ZxDslQueueUsageMornitorPeriod_Type.__name__ = "Integer32"
_ZxDslQueueUsageMornitorPeriod_Object = MibTableColumn
zxDslQueueUsageMornitorPeriod = _ZxDslQueueUsageMornitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 8, 1, 1),
    _ZxDslQueueUsageMornitorPeriod_Type()
)
zxDslQueueUsageMornitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslQueueUsageMornitorPeriod.setStatus("current")
if mibBuilder.loadTexts:
    zxDslQueueUsageMornitorPeriod.setUnits("second")
_ZxDslQueueUsageMornitorElapsedTime_Type = Integer32
_ZxDslQueueUsageMornitorElapsedTime_Object = MibTableColumn
zxDslQueueUsageMornitorElapsedTime = _ZxDslQueueUsageMornitorElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 8, 1, 2),
    _ZxDslQueueUsageMornitorElapsedTime_Type()
)
zxDslQueueUsageMornitorElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslQueueUsageMornitorElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    zxDslQueueUsageMornitorElapsedTime.setUnits("second")
_ZxDslPortQueueStatTable_Object = MibTable
zxDslPortQueueStatTable = _ZxDslPortQueueStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 9)
)
if mibBuilder.loadTexts:
    zxDslPortQueueStatTable.setStatus("current")
_ZxDslPortQueueStatEntry_Object = MibTableRow
zxDslPortQueueStatEntry = _ZxDslPortQueueStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 9, 1)
)
zxDslPortQueueStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-STATS-MIB", "zxDslPortQueueId"),
)
if mibBuilder.loadTexts:
    zxDslPortQueueStatEntry.setStatus("current")
_ZxDslPortQueueId_Type = Integer32
_ZxDslPortQueueId_Object = MibTableColumn
zxDslPortQueueId = _ZxDslPortQueueId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 9, 1, 1),
    _ZxDslPortQueueId_Type()
)
zxDslPortQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslPortQueueId.setStatus("current")
if mibBuilder.loadTexts:
    zxDslPortQueueId.setUnits("byte")
_ZxDslPortQueueMaxSize_Type = Integer32
_ZxDslPortQueueMaxSize_Object = MibTableColumn
zxDslPortQueueMaxSize = _ZxDslPortQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 9, 1, 2),
    _ZxDslPortQueueMaxSize_Type()
)
zxDslPortQueueMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslPortQueueMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    zxDslPortQueueMaxSize.setUnits("byte")
_ZxDslPortQueueCurrentUsage_Type = Integer32
_ZxDslPortQueueCurrentUsage_Object = MibTableColumn
zxDslPortQueueCurrentUsage = _ZxDslPortQueueCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 9, 1, 3),
    _ZxDslPortQueueCurrentUsage_Type()
)
zxDslPortQueueCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslPortQueueCurrentUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxDslPortQueueCurrentUsage.setUnits("percent")
_ZxDslPortQueueStatMinUsage_Type = Integer32
_ZxDslPortQueueStatMinUsage_Object = MibTableColumn
zxDslPortQueueStatMinUsage = _ZxDslPortQueueStatMinUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 9, 1, 4),
    _ZxDslPortQueueStatMinUsage_Type()
)
zxDslPortQueueStatMinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslPortQueueStatMinUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxDslPortQueueStatMinUsage.setUnits("percent")
_ZxDslPortQueueStatAverageUsage_Type = Integer32
_ZxDslPortQueueStatAverageUsage_Object = MibTableColumn
zxDslPortQueueStatAverageUsage = _ZxDslPortQueueStatAverageUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 9, 1, 5),
    _ZxDslPortQueueStatAverageUsage_Type()
)
zxDslPortQueueStatAverageUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslPortQueueStatAverageUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxDslPortQueueStatAverageUsage.setUnits("percent")
_ZxDslPortQueueStatMaxUsage_Type = Integer32
_ZxDslPortQueueStatMaxUsage_Object = MibTableColumn
zxDslPortQueueStatMaxUsage = _ZxDslPortQueueStatMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 9, 1, 6),
    _ZxDslPortQueueStatMaxUsage_Type()
)
zxDslPortQueueStatMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslPortQueueStatMaxUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxDslPortQueueStatMaxUsage.setUnits("percent")


class _ZxDslMacTablePeakValue_Type(Integer32):
    """Custom type zxDslMacTablePeakValue based on Integer32"""
    defaultValue = 70


_ZxDslMacTablePeakValue_Type.__name__ = "Integer32"
_ZxDslMacTablePeakValue_Object = MibScalar
zxDslMacTablePeakValue = _ZxDslMacTablePeakValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 1, 4, 10),
    _ZxDslMacTablePeakValue_Type()
)
zxDslMacTablePeakValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslMacTablePeakValue.setStatus("current")
_ZxDslStatsTrapObjects_ObjectIdentity = ObjectIdentity
zxDslStatsTrapObjects = _ZxDslStatsTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 2)
)

# Managed Objects groups


# Notification objects

zxDslMacTableUsageOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 38, 2, 1)
)
zxDslMacTableUsageOverThreshTrap.setObjects(
      *(("ZTE-DSL-STATS-MIB", "zxAnMacTableCurrentUsage"),
        ("ZTE-DSL-STATS-MIB", "zxAnMacTableUsageThreshold"))
)
if mibBuilder.loadTexts:
    zxDslMacTableUsageOverThreshTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-STATS-MIB",
    **{"zxDslStaticsMib": zxDslStaticsMib,
       "zxDslStatsObjects": zxDslStatsObjects,
       "zxDslEtherStatsTable": zxDslEtherStatsTable,
       "zxDslEtherStatsEntry": zxDslEtherStatsEntry,
       "zxDslEtherRxRate": zxDslEtherRxRate,
       "zxDslEtherTxRate": zxDslEtherTxRate,
       "zxDslEtherRxDiscardRatio": zxDslEtherRxDiscardRatio,
       "zxDslEtherTxDiscardRatio": zxDslEtherTxDiscardRatio,
       "zxDslEtherBroadcastRxRate": zxDslEtherBroadcastRxRate,
       "zxDslEtherBroadcastTxRate": zxDslEtherBroadcastTxRate,
       "zxDslEtherMulticastRxRate": zxDslEtherMulticastRxRate,
       "zxDslEtherMulticastTxRate": zxDslEtherMulticastTxRate,
       "zxDslEtherUnicastRxRate": zxDslEtherUnicastRxRate,
       "zxDslEtherUnicastTxRate": zxDslEtherUnicastTxRate,
       "zxDslBridgePortStatsTable": zxDslBridgePortStatsTable,
       "zxDslBridgePortStatsEntry": zxDslBridgePortStatsEntry,
       "zxDslBridgePortRxRate": zxDslBridgePortRxRate,
       "zxDslBridgePortTxRate": zxDslBridgePortTxRate,
       "zxDslBridgePortSelfLoopPkts": zxDslBridgePortSelfLoopPkts,
       "zxDslCardResourcesPerfTable": zxDslCardResourcesPerfTable,
       "zxDslCardResourcesPerfEntry": zxDslCardResourcesPerfEntry,
       "zxDslCardIndex": zxDslCardIndex,
       "zxDslCardCPULoad": zxDslCardCPULoad,
       "zxDslCardMemUsage": zxDslCardMemUsage,
       "zxDslCardActivedPortNum": zxDslCardActivedPortNum,
       "zxDslL2ResourcesStat": zxDslL2ResourcesStat,
       "zxDslMacTableUsageMornitorPeriod": zxDslMacTableUsageMornitorPeriod,
       "zxDslMacTableUsageMornitorTimes": zxDslMacTableUsageMornitorTimes,
       "zxDslMacTableUsageMornitorElapsedTime": zxDslMacTableUsageMornitorElapsedTime,
       "zxDslMacTableMaxSize": zxDslMacTableMaxSize,
       "zxDslMacTableCurrentUsage": zxDslMacTableCurrentUsage,
       "zxDslMacTableUsageThreshold": zxDslMacTableUsageThreshold,
       "zxDslMacTableStatTable": zxDslMacTableStatTable,
       "zxDslMacTableStatEntry": zxDslMacTableStatEntry,
       "zxDslMacTableStatSampleIndex": zxDslMacTableStatSampleIndex,
       "zxDslMacTableCurrentMaxUsage": zxDslMacTableCurrentMaxUsage,
       "zxDslPortQueueSampleTable": zxDslPortQueueSampleTable,
       "zxDslPortQueueSampleEntry": zxDslPortQueueSampleEntry,
       "zxDslQueueUsageMornitorPeriod": zxDslQueueUsageMornitorPeriod,
       "zxDslQueueUsageMornitorElapsedTime": zxDslQueueUsageMornitorElapsedTime,
       "zxDslPortQueueStatTable": zxDslPortQueueStatTable,
       "zxDslPortQueueStatEntry": zxDslPortQueueStatEntry,
       "zxDslPortQueueId": zxDslPortQueueId,
       "zxDslPortQueueMaxSize": zxDslPortQueueMaxSize,
       "zxDslPortQueueCurrentUsage": zxDslPortQueueCurrentUsage,
       "zxDslPortQueueStatMinUsage": zxDslPortQueueStatMinUsage,
       "zxDslPortQueueStatAverageUsage": zxDslPortQueueStatAverageUsage,
       "zxDslPortQueueStatMaxUsage": zxDslPortQueueStatMaxUsage,
       "zxDslMacTablePeakValue": zxDslMacTablePeakValue,
       "zxDslStatsTrapObjects": zxDslStatsTrapObjects,
       "zxDslMacTableUsageOverThreshTrap": zxDslMacTableUsageOverThreshTrap}
)
