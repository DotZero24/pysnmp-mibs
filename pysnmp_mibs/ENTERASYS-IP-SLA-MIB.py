# SNMP MIB module (ENTERASYS-IP-SLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-IP-SLA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:49 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

etsysIpSlaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94)
)
if mibBuilder.loadTexts:
    etsysIpSlaMIB.setRevisions(
        ("2013-02-06 18:26",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysIpSla_ObjectIdentity = ObjectIdentity
etsysIpSla = _EtsysIpSla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1)
)
_EtsysIpSlaGlobals_ObjectIdentity = ObjectIdentity
etsysIpSlaGlobals = _EtsysIpSlaGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 1)
)
_EtsysIpSlaMaxEntries_Type = Unsigned32
_EtsysIpSlaMaxEntries_Object = MibScalar
etsysIpSlaMaxEntries = _EtsysIpSlaMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 1, 1),
    _EtsysIpSlaMaxEntries_Type()
)
etsysIpSlaMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaMaxEntries.setStatus("current")
_EtsysIpSlaEntriesInUse_Type = Gauge32
_EtsysIpSlaEntriesInUse_Object = MibScalar
etsysIpSlaEntriesInUse = _EtsysIpSlaEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 1, 2),
    _EtsysIpSlaEntriesInUse_Type()
)
etsysIpSlaEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaEntriesInUse.setStatus("current")
_EtsysIpSlaMaxDataEntries_Type = Unsigned32
_EtsysIpSlaMaxDataEntries_Object = MibScalar
etsysIpSlaMaxDataEntries = _EtsysIpSlaMaxDataEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 1, 3),
    _EtsysIpSlaMaxDataEntries_Type()
)
etsysIpSlaMaxDataEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaMaxDataEntries.setStatus("current")
_EtsysIpSlaDataEntriesInUse_Type = Gauge32
_EtsysIpSlaDataEntriesInUse_Object = MibScalar
etsysIpSlaDataEntriesInUse = _EtsysIpSlaDataEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 1, 4),
    _EtsysIpSlaDataEntriesInUse_Type()
)
etsysIpSlaDataEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaDataEntriesInUse.setStatus("current")
_EtsysIpSlaTables_ObjectIdentity = ObjectIdentity
etsysIpSlaTables = _EtsysIpSlaTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2)
)
_EtsysIpSlaConfigTable_Object = MibTable
etsysIpSlaConfigTable = _EtsysIpSlaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysIpSlaConfigTable.setStatus("current")
_EtsysIpSlaConfigEntry_Object = MibTableRow
etsysIpSlaConfigEntry = _EtsysIpSlaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1)
)
etsysIpSlaConfigEntry.setIndexNames(
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigIndex"),
)
if mibBuilder.loadTexts:
    etsysIpSlaConfigEntry.setStatus("current")
_EtsysIpSlaConfigIndex_Type = Unsigned32
_EtsysIpSlaConfigIndex_Object = MibTableColumn
etsysIpSlaConfigIndex = _EtsysIpSlaConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 1),
    _EtsysIpSlaConfigIndex_Type()
)
etsysIpSlaConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIpSlaConfigIndex.setStatus("current")


class _EtsysIpSlaConfigType_Type(Integer32):
    """Custom type etsysIpSlaConfigType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("echo", 1),
          ("jitter", 2))
    )


_EtsysIpSlaConfigType_Type.__name__ = "Integer32"
_EtsysIpSlaConfigType_Object = MibTableColumn
etsysIpSlaConfigType = _EtsysIpSlaConfigType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 2),
    _EtsysIpSlaConfigType_Type()
)
etsysIpSlaConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigType.setStatus("current")


class _EtsysIpSlaConfigDestType_Type(InetAddressType):
    """Custom type etsysIpSlaConfigDestType based on InetAddressType"""
    defaultValue = 0


_EtsysIpSlaConfigDestType_Type.__name__ = "InetAddressType"
_EtsysIpSlaConfigDestType_Object = MibTableColumn
etsysIpSlaConfigDestType = _EtsysIpSlaConfigDestType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 3),
    _EtsysIpSlaConfigDestType_Type()
)
etsysIpSlaConfigDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigDestType.setStatus("current")


class _EtsysIpSlaConfigDestAddr_Type(InetAddress):
    """Custom type etsysIpSlaConfigDestAddr based on InetAddress"""
    defaultValue = OctetString("")


_EtsysIpSlaConfigDestAddr_Type.__name__ = "InetAddress"
_EtsysIpSlaConfigDestAddr_Object = MibTableColumn
etsysIpSlaConfigDestAddr = _EtsysIpSlaConfigDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 4),
    _EtsysIpSlaConfigDestAddr_Type()
)
etsysIpSlaConfigDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigDestAddr.setStatus("current")


class _EtsysIpSlaConfigDestPort_Type(InetPortNumber):
    """Custom type etsysIpSlaConfigDestPort based on InetPortNumber"""
    defaultValue = 0


_EtsysIpSlaConfigDestPort_Type.__name__ = "InetPortNumber"
_EtsysIpSlaConfigDestPort_Object = MibTableColumn
etsysIpSlaConfigDestPort = _EtsysIpSlaConfigDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 5),
    _EtsysIpSlaConfigDestPort_Type()
)
etsysIpSlaConfigDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigDestPort.setStatus("current")


class _EtsysIpSlaConfigProbeName_Type(SnmpAdminString):
    """Custom type etsysIpSlaConfigProbeName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EtsysIpSlaConfigProbeName_Type.__name__ = "SnmpAdminString"
_EtsysIpSlaConfigProbeName_Object = MibTableColumn
etsysIpSlaConfigProbeName = _EtsysIpSlaConfigProbeName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 6),
    _EtsysIpSlaConfigProbeName_Type()
)
etsysIpSlaConfigProbeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigProbeName.setStatus("current")


class _EtsysIpSlaConfigPathCount_Type(Unsigned32):
    """Custom type etsysIpSlaConfigPathCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_EtsysIpSlaConfigPathCount_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigPathCount_Object = MibTableColumn
etsysIpSlaConfigPathCount = _EtsysIpSlaConfigPathCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 7),
    _EtsysIpSlaConfigPathCount_Type()
)
etsysIpSlaConfigPathCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigPathCount.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaConfigPathCount.setUnits("paths")


class _EtsysIpSlaConfigHopCount_Type(Unsigned32):
    """Custom type etsysIpSlaConfigHopCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_EtsysIpSlaConfigHopCount_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigHopCount_Object = MibTableColumn
etsysIpSlaConfigHopCount = _EtsysIpSlaConfigHopCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 8),
    _EtsysIpSlaConfigHopCount_Type()
)
etsysIpSlaConfigHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHopCount.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHopCount.setUnits("hops")


class _EtsysIpSlaConfigHistoryCollections_Type(Unsigned32):
    """Custom type etsysIpSlaConfigHistoryCollections based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EtsysIpSlaConfigHistoryCollections_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigHistoryCollections_Object = MibTableColumn
etsysIpSlaConfigHistoryCollections = _EtsysIpSlaConfigHistoryCollections_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 9),
    _EtsysIpSlaConfigHistoryCollections_Type()
)
etsysIpSlaConfigHistoryCollections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHistoryCollections.setStatus("current")


class _EtsysIpSlaConfigHistoryBuckets_Type(Unsigned32):
    """Custom type etsysIpSlaConfigHistoryBuckets based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_EtsysIpSlaConfigHistoryBuckets_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigHistoryBuckets_Object = MibTableColumn
etsysIpSlaConfigHistoryBuckets = _EtsysIpSlaConfigHistoryBuckets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 10),
    _EtsysIpSlaConfigHistoryBuckets_Type()
)
etsysIpSlaConfigHistoryBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHistoryBuckets.setStatus("current")


class _EtsysIpSlaConfigHistoryBucketType_Type(Integer32):
    """Custom type etsysIpSlaConfigHistoryBucketType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("timed", 2))
    )


_EtsysIpSlaConfigHistoryBucketType_Type.__name__ = "Integer32"
_EtsysIpSlaConfigHistoryBucketType_Object = MibTableColumn
etsysIpSlaConfigHistoryBucketType = _EtsysIpSlaConfigHistoryBucketType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 11),
    _EtsysIpSlaConfigHistoryBucketType_Type()
)
etsysIpSlaConfigHistoryBucketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHistoryBucketType.setStatus("current")


class _EtsysIpSlaConfigHistorySamples_Type(Unsigned32):
    """Custom type etsysIpSlaConfigHistorySamples based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 512),
    )


_EtsysIpSlaConfigHistorySamples_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigHistorySamples_Object = MibTableColumn
etsysIpSlaConfigHistorySamples = _EtsysIpSlaConfigHistorySamples_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 12),
    _EtsysIpSlaConfigHistorySamples_Type()
)
etsysIpSlaConfigHistorySamples.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHistorySamples.setStatus("current")


class _EtsysIpSlaConfigHistoryInterval_Type(Unsigned32):
    """Custom type etsysIpSlaConfigHistoryInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_EtsysIpSlaConfigHistoryInterval_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigHistoryInterval_Object = MibTableColumn
etsysIpSlaConfigHistoryInterval = _EtsysIpSlaConfigHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 13),
    _EtsysIpSlaConfigHistoryInterval_Type()
)
etsysIpSlaConfigHistoryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHistoryInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHistoryInterval.setUnits("seconds")


class _EtsysIpSlaConfigHistoryAgeout_Type(Unsigned32):
    """Custom type etsysIpSlaConfigHistoryAgeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(15, 7200),
    )


_EtsysIpSlaConfigHistoryAgeout_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigHistoryAgeout_Object = MibTableColumn
etsysIpSlaConfigHistoryAgeout = _EtsysIpSlaConfigHistoryAgeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 14),
    _EtsysIpSlaConfigHistoryAgeout_Type()
)
etsysIpSlaConfigHistoryAgeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHistoryAgeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHistoryAgeout.setUnits("minutes")


class _EtsysIpSlaConfigHistoryWrap_Type(Integer32):
    """Custom type etsysIpSlaConfigHistoryWrap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wrap", 1),
          ("noWrap", 2))
    )


_EtsysIpSlaConfigHistoryWrap_Type.__name__ = "Integer32"
_EtsysIpSlaConfigHistoryWrap_Object = MibTableColumn
etsysIpSlaConfigHistoryWrap = _EtsysIpSlaConfigHistoryWrap_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 15),
    _EtsysIpSlaConfigHistoryWrap_Type()
)
etsysIpSlaConfigHistoryWrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigHistoryWrap.setStatus("current")


class _EtsysIpSlaConfigDistributionCount_Type(Unsigned32):
    """Custom type etsysIpSlaConfigDistributionCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 5),
    )


_EtsysIpSlaConfigDistributionCount_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigDistributionCount_Object = MibTableColumn
etsysIpSlaConfigDistributionCount = _EtsysIpSlaConfigDistributionCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 16),
    _EtsysIpSlaConfigDistributionCount_Type()
)
etsysIpSlaConfigDistributionCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigDistributionCount.setStatus("current")


class _EtsysIpSlaConfigDistributionInterval_Type(Unsigned32):
    """Custom type etsysIpSlaConfigDistributionInterval based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_EtsysIpSlaConfigDistributionInterval_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigDistributionInterval_Object = MibTableColumn
etsysIpSlaConfigDistributionInterval = _EtsysIpSlaConfigDistributionInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 17),
    _EtsysIpSlaConfigDistributionInterval_Type()
)
etsysIpSlaConfigDistributionInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigDistributionInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaConfigDistributionInterval.setUnits("milliseconds")


class _EtsysIpSlaConfigStatisticsCollections_Type(Unsigned32):
    """Custom type etsysIpSlaConfigStatisticsCollections based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EtsysIpSlaConfigStatisticsCollections_Type.__name__ = "Unsigned32"
_EtsysIpSlaConfigStatisticsCollections_Object = MibTableColumn
etsysIpSlaConfigStatisticsCollections = _EtsysIpSlaConfigStatisticsCollections_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 18),
    _EtsysIpSlaConfigStatisticsCollections_Type()
)
etsysIpSlaConfigStatisticsCollections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigStatisticsCollections.setStatus("current")
_EtsysIpSlaConfigStatus_Type = RowStatus
_EtsysIpSlaConfigStatus_Object = MibTableColumn
etsysIpSlaConfigStatus = _EtsysIpSlaConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 1, 1, 19),
    _EtsysIpSlaConfigStatus_Type()
)
etsysIpSlaConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysIpSlaConfigStatus.setStatus("current")
_EtsysIpSlaScheduleTable_Object = MibTable
etsysIpSlaScheduleTable = _EtsysIpSlaScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysIpSlaScheduleTable.setStatus("current")
_EtsysIpSlaScheduleEntry_Object = MibTableRow
etsysIpSlaScheduleEntry = _EtsysIpSlaScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 2, 1)
)
etsysIpSlaScheduleEntry.setIndexNames(
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigIndex"),
)
if mibBuilder.loadTexts:
    etsysIpSlaScheduleEntry.setStatus("current")


class _EtsysIpSlaScheduleStartTime_Type(Unsigned32):
    """Custom type etsysIpSlaScheduleStartTime based on Unsigned32"""
    defaultValue = 0


_EtsysIpSlaScheduleStartTime_Type.__name__ = "Unsigned32"
_EtsysIpSlaScheduleStartTime_Object = MibTableColumn
etsysIpSlaScheduleStartTime = _EtsysIpSlaScheduleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 2, 1, 1),
    _EtsysIpSlaScheduleStartTime_Type()
)
etsysIpSlaScheduleStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleStartTime.setStatus("current")


class _EtsysIpSlaScheduleRecurrence_Type(Unsigned32):
    """Custom type etsysIpSlaScheduleRecurrence based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 7776000),
    )


_EtsysIpSlaScheduleRecurrence_Type.__name__ = "Unsigned32"
_EtsysIpSlaScheduleRecurrence_Object = MibTableColumn
etsysIpSlaScheduleRecurrence = _EtsysIpSlaScheduleRecurrence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 2, 1, 2),
    _EtsysIpSlaScheduleRecurrence_Type()
)
etsysIpSlaScheduleRecurrence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleRecurrence.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleRecurrence.setUnits("seconds")


class _EtsysIpSlaScheduleTestRepetitions_Type(Unsigned32):
    """Custom type etsysIpSlaScheduleTestRepetitions based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EtsysIpSlaScheduleTestRepetitions_Type.__name__ = "Unsigned32"
_EtsysIpSlaScheduleTestRepetitions_Object = MibTableColumn
etsysIpSlaScheduleTestRepetitions = _EtsysIpSlaScheduleTestRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 2, 1, 3),
    _EtsysIpSlaScheduleTestRepetitions_Type()
)
etsysIpSlaScheduleTestRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleTestRepetitions.setStatus("current")


class _EtsysIpSlaScheduleTestDuration_Type(Unsigned32):
    """Custom type etsysIpSlaScheduleTestDuration based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_EtsysIpSlaScheduleTestDuration_Type.__name__ = "Unsigned32"
_EtsysIpSlaScheduleTestDuration_Object = MibTableColumn
etsysIpSlaScheduleTestDuration = _EtsysIpSlaScheduleTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 2, 1, 4),
    _EtsysIpSlaScheduleTestDuration_Type()
)
etsysIpSlaScheduleTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleTestDuration.setUnits("seconds")


class _EtsysIpSlaScheduleTestFrequency_Type(Unsigned32):
    """Custom type etsysIpSlaScheduleTestFrequency based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_EtsysIpSlaScheduleTestFrequency_Type.__name__ = "Unsigned32"
_EtsysIpSlaScheduleTestFrequency_Object = MibTableColumn
etsysIpSlaScheduleTestFrequency = _EtsysIpSlaScheduleTestFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 2, 1, 5),
    _EtsysIpSlaScheduleTestFrequency_Type()
)
etsysIpSlaScheduleTestFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleTestFrequency.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleTestFrequency.setUnits("seconds")


class _EtsysIpSlaScheduleTestState_Type(Integer32):
    """Custom type etsysIpSlaScheduleTestState based on Integer32"""
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
        *(("inactive", 1),
          ("complete", 2),
          ("running", 3),
          ("queued", 4))
    )


_EtsysIpSlaScheduleTestState_Type.__name__ = "Integer32"
_EtsysIpSlaScheduleTestState_Object = MibTableColumn
etsysIpSlaScheduleTestState = _EtsysIpSlaScheduleTestState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 2, 1, 6),
    _EtsysIpSlaScheduleTestState_Type()
)
etsysIpSlaScheduleTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleTestState.setStatus("current")


class _EtsysIpSlaScheduleTestStatus_Type(SnmpAdminString):
    """Custom type etsysIpSlaScheduleTestStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EtsysIpSlaScheduleTestStatus_Type.__name__ = "SnmpAdminString"
_EtsysIpSlaScheduleTestStatus_Object = MibTableColumn
etsysIpSlaScheduleTestStatus = _EtsysIpSlaScheduleTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 2, 1, 7),
    _EtsysIpSlaScheduleTestStatus_Type()
)
etsysIpSlaScheduleTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaScheduleTestStatus.setStatus("current")
_EtsysIpSlaCollectionTable_Object = MibTable
etsysIpSlaCollectionTable = _EtsysIpSlaCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 3)
)
if mibBuilder.loadTexts:
    etsysIpSlaCollectionTable.setStatus("current")
_EtsysIpSlaCollectionEntry_Object = MibTableRow
etsysIpSlaCollectionEntry = _EtsysIpSlaCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 3, 1)
)
etsysIpSlaCollectionEntry.setIndexNames(
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionType"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionIndex"),
)
if mibBuilder.loadTexts:
    etsysIpSlaCollectionEntry.setStatus("current")


class _EtsysIpSlaCollectionType_Type(Integer32):
    """Custom type etsysIpSlaCollectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("summary", 1),
          ("distribution", 2),
          ("history", 3))
    )


_EtsysIpSlaCollectionType_Type.__name__ = "Integer32"
_EtsysIpSlaCollectionType_Object = MibTableColumn
etsysIpSlaCollectionType = _EtsysIpSlaCollectionType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 3, 1, 1),
    _EtsysIpSlaCollectionType_Type()
)
etsysIpSlaCollectionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIpSlaCollectionType.setStatus("current")
_EtsysIpSlaCollectionIndex_Type = Unsigned32
_EtsysIpSlaCollectionIndex_Object = MibTableColumn
etsysIpSlaCollectionIndex = _EtsysIpSlaCollectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 3, 1, 2),
    _EtsysIpSlaCollectionIndex_Type()
)
etsysIpSlaCollectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIpSlaCollectionIndex.setStatus("current")
_EtsysIpSlaCollectionStartTime_Type = Unsigned32
_EtsysIpSlaCollectionStartTime_Object = MibTableColumn
etsysIpSlaCollectionStartTime = _EtsysIpSlaCollectionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 3, 1, 3),
    _EtsysIpSlaCollectionStartTime_Type()
)
etsysIpSlaCollectionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaCollectionStartTime.setStatus("current")
_EtsysIpSlaCollectionNumPaths_Type = Gauge32
_EtsysIpSlaCollectionNumPaths_Object = MibTableColumn
etsysIpSlaCollectionNumPaths = _EtsysIpSlaCollectionNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 3, 1, 4),
    _EtsysIpSlaCollectionNumPaths_Type()
)
etsysIpSlaCollectionNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaCollectionNumPaths.setStatus("current")
_EtsysIpslaCollectionNumHops_Type = Gauge32
_EtsysIpslaCollectionNumHops_Object = MibTableColumn
etsysIpslaCollectionNumHops = _EtsysIpslaCollectionNumHops_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 3, 1, 5),
    _EtsysIpslaCollectionNumHops_Type()
)
etsysIpslaCollectionNumHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpslaCollectionNumHops.setStatus("current")
_EtsysIpSlaPathTable_Object = MibTable
etsysIpSlaPathTable = _EtsysIpSlaPathTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 4)
)
if mibBuilder.loadTexts:
    etsysIpSlaPathTable.setStatus("current")
_EtsysIpSlaPathEntry_Object = MibTableRow
etsysIpSlaPathEntry = _EtsysIpSlaPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 4, 1)
)
etsysIpSlaPathEntry.setIndexNames(
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionType"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaPathIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaHopIndex"),
)
if mibBuilder.loadTexts:
    etsysIpSlaPathEntry.setStatus("current")
_EtsysIpSlaPathIndex_Type = Unsigned32
_EtsysIpSlaPathIndex_Object = MibTableColumn
etsysIpSlaPathIndex = _EtsysIpSlaPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 4, 1, 1),
    _EtsysIpSlaPathIndex_Type()
)
etsysIpSlaPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIpSlaPathIndex.setStatus("current")
_EtsysIpSlaHopIndex_Type = Unsigned32
_EtsysIpSlaHopIndex_Object = MibTableColumn
etsysIpSlaHopIndex = _EtsysIpSlaHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 4, 1, 2),
    _EtsysIpSlaHopIndex_Type()
)
etsysIpSlaHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIpSlaHopIndex.setStatus("current")
_EtsysIpSlaHopDestType_Type = InetAddressType
_EtsysIpSlaHopDestType_Object = MibTableColumn
etsysIpSlaHopDestType = _EtsysIpSlaHopDestType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 4, 1, 3),
    _EtsysIpSlaHopDestType_Type()
)
etsysIpSlaHopDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaHopDestType.setStatus("current")
_EtsysIpSlaHopDestAddr_Type = InetAddress
_EtsysIpSlaHopDestAddr_Object = MibTableColumn
etsysIpSlaHopDestAddr = _EtsysIpSlaHopDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 4, 1, 4),
    _EtsysIpSlaHopDestAddr_Type()
)
etsysIpSlaHopDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaHopDestAddr.setStatus("current")
_EtsysIpSlaRttDataTable_Object = MibTable
etsysIpSlaRttDataTable = _EtsysIpSlaRttDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5)
)
if mibBuilder.loadTexts:
    etsysIpSlaRttDataTable.setStatus("current")
_EtsysIpSlaRttDataEntry_Object = MibTableRow
etsysIpSlaRttDataEntry = _EtsysIpSlaRttDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1)
)
etsysIpSlaRttDataEntry.setIndexNames(
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionType"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaPathIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaHopIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaBucketIndex"),
)
if mibBuilder.loadTexts:
    etsysIpSlaRttDataEntry.setStatus("current")
_EtsysIpSlaBucketIndex_Type = Unsigned32
_EtsysIpSlaBucketIndex_Object = MibTableColumn
etsysIpSlaBucketIndex = _EtsysIpSlaBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 1),
    _EtsysIpSlaBucketIndex_Type()
)
etsysIpSlaBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysIpSlaBucketIndex.setStatus("current")
_EtsysIpSlaBucketTime_Type = Unsigned32
_EtsysIpSlaBucketTime_Object = MibTableColumn
etsysIpSlaBucketTime = _EtsysIpSlaBucketTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 2),
    _EtsysIpSlaBucketTime_Type()
)
etsysIpSlaBucketTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaBucketTime.setStatus("current")
_EtsysIpSlaRttDataSamples_Type = Gauge32
_EtsysIpSlaRttDataSamples_Object = MibTableColumn
etsysIpSlaRttDataSamples = _EtsysIpSlaRttDataSamples_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 3),
    _EtsysIpSlaRttDataSamples_Type()
)
etsysIpSlaRttDataSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataSamples.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataSamples.setUnits("packets")
_EtsysIpSlaRttDataMinDelay_Type = Gauge32
_EtsysIpSlaRttDataMinDelay_Object = MibTableColumn
etsysIpSlaRttDataMinDelay = _EtsysIpSlaRttDataMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 4),
    _EtsysIpSlaRttDataMinDelay_Type()
)
etsysIpSlaRttDataMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataMinDelay.setUnits("microseconds")
_EtsysIpSlaRttDataAvgDelay_Type = Gauge32
_EtsysIpSlaRttDataAvgDelay_Object = MibTableColumn
etsysIpSlaRttDataAvgDelay = _EtsysIpSlaRttDataAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 5),
    _EtsysIpSlaRttDataAvgDelay_Type()
)
etsysIpSlaRttDataAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataAvgDelay.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataAvgDelay.setUnits("microseconds")
_EtsysIpSlaRttDataMaxDelay_Type = Gauge32
_EtsysIpSlaRttDataMaxDelay_Object = MibTableColumn
etsysIpSlaRttDataMaxDelay = _EtsysIpSlaRttDataMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 6),
    _EtsysIpSlaRttDataMaxDelay_Type()
)
etsysIpSlaRttDataMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataMaxDelay.setUnits("microseconds")
_EtsysIpSlaRttDataSum_Type = Gauge32
_EtsysIpSlaRttDataSum_Object = MibTableColumn
etsysIpSlaRttDataSum = _EtsysIpSlaRttDataSum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 7),
    _EtsysIpSlaRttDataSum_Type()
)
etsysIpSlaRttDataSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataSum.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataSum.setUnits("microseconds")
_EtsysIpSlaRttDataSumSquareLow_Type = Gauge32
_EtsysIpSlaRttDataSumSquareLow_Object = MibTableColumn
etsysIpSlaRttDataSumSquareLow = _EtsysIpSlaRttDataSumSquareLow_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 8),
    _EtsysIpSlaRttDataSumSquareLow_Type()
)
etsysIpSlaRttDataSumSquareLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataSumSquareLow.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataSumSquareLow.setUnits("microseconds")
_EtsysIpSlaRttDataSumSquareHigh_Type = Gauge32
_EtsysIpSlaRttDataSumSquareHigh_Object = MibTableColumn
etsysIpSlaRttDataSumSquareHigh = _EtsysIpSlaRttDataSumSquareHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 9),
    _EtsysIpSlaRttDataSumSquareHigh_Type()
)
etsysIpSlaRttDataSumSquareHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataSumSquareHigh.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataSumSquareHigh.setUnits("microseconds")
_EtsysIpSlaRttDataPktOutOfOrder_Type = Gauge32
_EtsysIpSlaRttDataPktOutOfOrder_Object = MibTableColumn
etsysIpSlaRttDataPktOutOfOrder = _EtsysIpSlaRttDataPktOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 10),
    _EtsysIpSlaRttDataPktOutOfOrder_Type()
)
etsysIpSlaRttDataPktOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktOutOfOrder.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktOutOfOrder.setUnits("packets")
_EtsysIpSlaRttDataPktLateArrival_Type = Gauge32
_EtsysIpSlaRttDataPktLateArrival_Object = MibTableColumn
etsysIpSlaRttDataPktLateArrival = _EtsysIpSlaRttDataPktLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 11),
    _EtsysIpSlaRttDataPktLateArrival_Type()
)
etsysIpSlaRttDataPktLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktLateArrival.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktLateArrival.setUnits("packets")
_EtsysIpSlaRttDataPktMissing_Type = Gauge32
_EtsysIpSlaRttDataPktMissing_Object = MibTableColumn
etsysIpSlaRttDataPktMissing = _EtsysIpSlaRttDataPktMissing_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 12),
    _EtsysIpSlaRttDataPktMissing_Type()
)
etsysIpSlaRttDataPktMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktMissing.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktMissing.setUnits("packets")
_EtsysIpSlaRttDataPktIpTosMismatch_Type = Gauge32
_EtsysIpSlaRttDataPktIpTosMismatch_Object = MibTableColumn
etsysIpSlaRttDataPktIpTosMismatch = _EtsysIpSlaRttDataPktIpTosMismatch_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 13),
    _EtsysIpSlaRttDataPktIpTosMismatch_Type()
)
etsysIpSlaRttDataPktIpTosMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktIpTosMismatch.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktIpTosMismatch.setUnits("packets")
_EtsysIpSlaRttDataPktVlanPcpMismatch_Type = Gauge32
_EtsysIpSlaRttDataPktVlanPcpMismatch_Object = MibTableColumn
etsysIpSlaRttDataPktVlanPcpMismatch = _EtsysIpSlaRttDataPktVlanPcpMismatch_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 14),
    _EtsysIpSlaRttDataPktVlanPcpMismatch_Type()
)
etsysIpSlaRttDataPktVlanPcpMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktVlanPcpMismatch.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataPktVlanPcpMismatch.setUnits("packets")
_EtsysIpSlaRttDataTxErrors_Type = Gauge32
_EtsysIpSlaRttDataTxErrors_Object = MibTableColumn
etsysIpSlaRttDataTxErrors = _EtsysIpSlaRttDataTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 5, 1, 15),
    _EtsysIpSlaRttDataTxErrors_Type()
)
etsysIpSlaRttDataTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaRttDataTxErrors.setStatus("current")
_EtsysIpSlaPdvDataTable_Object = MibTable
etsysIpSlaPdvDataTable = _EtsysIpSlaPdvDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6)
)
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataTable.setStatus("current")
_EtsysIpSlaPdvDataEntry_Object = MibTableRow
etsysIpSlaPdvDataEntry = _EtsysIpSlaPdvDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1)
)
etsysIpSlaPdvDataEntry.setIndexNames(
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionType"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaPathIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaHopIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaBucketIndex"),
)
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataEntry.setStatus("current")
_EtsysIpSlaPdvDataSamples_Type = Gauge32
_EtsysIpSlaPdvDataSamples_Object = MibTableColumn
etsysIpSlaPdvDataSamples = _EtsysIpSlaPdvDataSamples_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 1),
    _EtsysIpSlaPdvDataSamples_Type()
)
etsysIpSlaPdvDataSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSamples.setStatus("current")
_EtsysIpSlaPdvDataMinPositiveSD_Type = Gauge32
_EtsysIpSlaPdvDataMinPositiveSD_Object = MibTableColumn
etsysIpSlaPdvDataMinPositiveSD = _EtsysIpSlaPdvDataMinPositiveSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 2),
    _EtsysIpSlaPdvDataMinPositiveSD_Type()
)
etsysIpSlaPdvDataMinPositiveSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMinPositiveSD.setStatus("current")
_EtsysIpSlaPdvDataMaxPositiveSD_Type = Gauge32
_EtsysIpSlaPdvDataMaxPositiveSD_Object = MibTableColumn
etsysIpSlaPdvDataMaxPositiveSD = _EtsysIpSlaPdvDataMaxPositiveSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 3),
    _EtsysIpSlaPdvDataMaxPositiveSD_Type()
)
etsysIpSlaPdvDataMaxPositiveSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMaxPositiveSD.setStatus("current")
_EtsysIpSlaPdvDataNumPositiveSD_Type = Gauge32
_EtsysIpSlaPdvDataNumPositiveSD_Object = MibTableColumn
etsysIpSlaPdvDataNumPositiveSD = _EtsysIpSlaPdvDataNumPositiveSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 4),
    _EtsysIpSlaPdvDataNumPositiveSD_Type()
)
etsysIpSlaPdvDataNumPositiveSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataNumPositiveSD.setStatus("current")
_EtsysIpSlaPdvDataSumPositiveSD_Type = Gauge32
_EtsysIpSlaPdvDataSumPositiveSD_Object = MibTableColumn
etsysIpSlaPdvDataSumPositiveSD = _EtsysIpSlaPdvDataSumPositiveSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 5),
    _EtsysIpSlaPdvDataSumPositiveSD_Type()
)
etsysIpSlaPdvDataSumPositiveSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumPositiveSD.setStatus("current")
_EtsysIpSlaPdvDataSumSquarePositiveSD_Type = Gauge32
_EtsysIpSlaPdvDataSumSquarePositiveSD_Object = MibTableColumn
etsysIpSlaPdvDataSumSquarePositiveSD = _EtsysIpSlaPdvDataSumSquarePositiveSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 6),
    _EtsysIpSlaPdvDataSumSquarePositiveSD_Type()
)
etsysIpSlaPdvDataSumSquarePositiveSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumSquarePositiveSD.setStatus("current")
_EtsysIpSlaPdvDataMinNegativeSD_Type = Gauge32
_EtsysIpSlaPdvDataMinNegativeSD_Object = MibTableColumn
etsysIpSlaPdvDataMinNegativeSD = _EtsysIpSlaPdvDataMinNegativeSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 7),
    _EtsysIpSlaPdvDataMinNegativeSD_Type()
)
etsysIpSlaPdvDataMinNegativeSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMinNegativeSD.setStatus("current")
_EtsysIpSlaPdvDataMaxNegativeSD_Type = Gauge32
_EtsysIpSlaPdvDataMaxNegativeSD_Object = MibTableColumn
etsysIpSlaPdvDataMaxNegativeSD = _EtsysIpSlaPdvDataMaxNegativeSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 8),
    _EtsysIpSlaPdvDataMaxNegativeSD_Type()
)
etsysIpSlaPdvDataMaxNegativeSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMaxNegativeSD.setStatus("current")
_EtsysIpSlaPdvDataNumNegativeSD_Type = Gauge32
_EtsysIpSlaPdvDataNumNegativeSD_Object = MibTableColumn
etsysIpSlaPdvDataNumNegativeSD = _EtsysIpSlaPdvDataNumNegativeSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 9),
    _EtsysIpSlaPdvDataNumNegativeSD_Type()
)
etsysIpSlaPdvDataNumNegativeSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataNumNegativeSD.setStatus("current")
_EtsysIpSlaPdvDataSumNegativeSD_Type = Gauge32
_EtsysIpSlaPdvDataSumNegativeSD_Object = MibTableColumn
etsysIpSlaPdvDataSumNegativeSD = _EtsysIpSlaPdvDataSumNegativeSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 10),
    _EtsysIpSlaPdvDataSumNegativeSD_Type()
)
etsysIpSlaPdvDataSumNegativeSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumNegativeSD.setStatus("current")
_EtsysIpSlaPdvDataSumSquareNegativeSD_Type = Gauge32
_EtsysIpSlaPdvDataSumSquareNegativeSD_Object = MibTableColumn
etsysIpSlaPdvDataSumSquareNegativeSD = _EtsysIpSlaPdvDataSumSquareNegativeSD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 11),
    _EtsysIpSlaPdvDataSumSquareNegativeSD_Type()
)
etsysIpSlaPdvDataSumSquareNegativeSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumSquareNegativeSD.setStatus("current")
_EtsysIpSlaPdvDataMinPositiveDS_Type = Gauge32
_EtsysIpSlaPdvDataMinPositiveDS_Object = MibTableColumn
etsysIpSlaPdvDataMinPositiveDS = _EtsysIpSlaPdvDataMinPositiveDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 12),
    _EtsysIpSlaPdvDataMinPositiveDS_Type()
)
etsysIpSlaPdvDataMinPositiveDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMinPositiveDS.setStatus("current")
_EtsysIpSlaPdvDataMaxPositiveDS_Type = Gauge32
_EtsysIpSlaPdvDataMaxPositiveDS_Object = MibTableColumn
etsysIpSlaPdvDataMaxPositiveDS = _EtsysIpSlaPdvDataMaxPositiveDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 13),
    _EtsysIpSlaPdvDataMaxPositiveDS_Type()
)
etsysIpSlaPdvDataMaxPositiveDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMaxPositiveDS.setStatus("current")
_EtsysIpSlaPdvDataNumPositiveDS_Type = Gauge32
_EtsysIpSlaPdvDataNumPositiveDS_Object = MibTableColumn
etsysIpSlaPdvDataNumPositiveDS = _EtsysIpSlaPdvDataNumPositiveDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 14),
    _EtsysIpSlaPdvDataNumPositiveDS_Type()
)
etsysIpSlaPdvDataNumPositiveDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataNumPositiveDS.setStatus("current")
_EtsysIpSlaPdvDataSumPositiveDS_Type = Gauge32
_EtsysIpSlaPdvDataSumPositiveDS_Object = MibTableColumn
etsysIpSlaPdvDataSumPositiveDS = _EtsysIpSlaPdvDataSumPositiveDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 15),
    _EtsysIpSlaPdvDataSumPositiveDS_Type()
)
etsysIpSlaPdvDataSumPositiveDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumPositiveDS.setStatus("current")
_EtsysIpSlaPdvDataSumSquarePositiveDS_Type = Gauge32
_EtsysIpSlaPdvDataSumSquarePositiveDS_Object = MibTableColumn
etsysIpSlaPdvDataSumSquarePositiveDS = _EtsysIpSlaPdvDataSumSquarePositiveDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 16),
    _EtsysIpSlaPdvDataSumSquarePositiveDS_Type()
)
etsysIpSlaPdvDataSumSquarePositiveDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumSquarePositiveDS.setStatus("current")
_EtsysIpSlaPdvDataMinNegativeDS_Type = Gauge32
_EtsysIpSlaPdvDataMinNegativeDS_Object = MibTableColumn
etsysIpSlaPdvDataMinNegativeDS = _EtsysIpSlaPdvDataMinNegativeDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 17),
    _EtsysIpSlaPdvDataMinNegativeDS_Type()
)
etsysIpSlaPdvDataMinNegativeDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMinNegativeDS.setStatus("current")
_EtsysIpSlaPdvDataMaxNegativeDS_Type = Gauge32
_EtsysIpSlaPdvDataMaxNegativeDS_Object = MibTableColumn
etsysIpSlaPdvDataMaxNegativeDS = _EtsysIpSlaPdvDataMaxNegativeDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 18),
    _EtsysIpSlaPdvDataMaxNegativeDS_Type()
)
etsysIpSlaPdvDataMaxNegativeDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMaxNegativeDS.setStatus("current")
_EtsysIpSlaPdvDataNumNegativeDS_Type = Gauge32
_EtsysIpSlaPdvDataNumNegativeDS_Object = MibTableColumn
etsysIpSlaPdvDataNumNegativeDS = _EtsysIpSlaPdvDataNumNegativeDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 19),
    _EtsysIpSlaPdvDataNumNegativeDS_Type()
)
etsysIpSlaPdvDataNumNegativeDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataNumNegativeDS.setStatus("current")
_EtsysIpSlaPdvDataSumNegativeDS_Type = Gauge32
_EtsysIpSlaPdvDataSumNegativeDS_Object = MibTableColumn
etsysIpSlaPdvDataSumNegativeDS = _EtsysIpSlaPdvDataSumNegativeDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 20),
    _EtsysIpSlaPdvDataSumNegativeDS_Type()
)
etsysIpSlaPdvDataSumNegativeDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumNegativeDS.setStatus("current")
_EtsysIpSlaPdvDataSumSquareNegativeDS_Type = Gauge32
_EtsysIpSlaPdvDataSumSquareNegativeDS_Object = MibTableColumn
etsysIpSlaPdvDataSumSquareNegativeDS = _EtsysIpSlaPdvDataSumSquareNegativeDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 21),
    _EtsysIpSlaPdvDataSumSquareNegativeDS_Type()
)
etsysIpSlaPdvDataSumSquareNegativeDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumSquareNegativeDS.setStatus("current")
_EtsysIpSlaPdvDataNumOneWaySD_Type = Gauge32
_EtsysIpSlaPdvDataNumOneWaySD_Object = MibTableColumn
etsysIpSlaPdvDataNumOneWaySD = _EtsysIpSlaPdvDataNumOneWaySD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 22),
    _EtsysIpSlaPdvDataNumOneWaySD_Type()
)
etsysIpSlaPdvDataNumOneWaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataNumOneWaySD.setStatus("current")
_EtsysIpSlaPdvDataMinOneWaySD_Type = Gauge32
_EtsysIpSlaPdvDataMinOneWaySD_Object = MibTableColumn
etsysIpSlaPdvDataMinOneWaySD = _EtsysIpSlaPdvDataMinOneWaySD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 23),
    _EtsysIpSlaPdvDataMinOneWaySD_Type()
)
etsysIpSlaPdvDataMinOneWaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMinOneWaySD.setStatus("current")
_EtsysIpSlaPdvDataMaxOneWaySD_Type = Gauge32
_EtsysIpSlaPdvDataMaxOneWaySD_Object = MibTableColumn
etsysIpSlaPdvDataMaxOneWaySD = _EtsysIpSlaPdvDataMaxOneWaySD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 24),
    _EtsysIpSlaPdvDataMaxOneWaySD_Type()
)
etsysIpSlaPdvDataMaxOneWaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMaxOneWaySD.setStatus("current")
_EtsysIpSlaPdvDataSumOneWaySD_Type = Gauge32
_EtsysIpSlaPdvDataSumOneWaySD_Object = MibTableColumn
etsysIpSlaPdvDataSumOneWaySD = _EtsysIpSlaPdvDataSumOneWaySD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 25),
    _EtsysIpSlaPdvDataSumOneWaySD_Type()
)
etsysIpSlaPdvDataSumOneWaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumOneWaySD.setStatus("current")
_EtsysIpSlaPdvDataSumSquareOneWaySD_Type = Gauge32
_EtsysIpSlaPdvDataSumSquareOneWaySD_Object = MibTableColumn
etsysIpSlaPdvDataSumSquareOneWaySD = _EtsysIpSlaPdvDataSumSquareOneWaySD_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 26),
    _EtsysIpSlaPdvDataSumSquareOneWaySD_Type()
)
etsysIpSlaPdvDataSumSquareOneWaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumSquareOneWaySD.setStatus("current")
_EtsysIpSlaPdvDataNumOneWayDS_Type = Gauge32
_EtsysIpSlaPdvDataNumOneWayDS_Object = MibTableColumn
etsysIpSlaPdvDataNumOneWayDS = _EtsysIpSlaPdvDataNumOneWayDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 27),
    _EtsysIpSlaPdvDataNumOneWayDS_Type()
)
etsysIpSlaPdvDataNumOneWayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataNumOneWayDS.setStatus("current")
_EtsysIpSlaPdvDataMinOneWayDS_Type = Gauge32
_EtsysIpSlaPdvDataMinOneWayDS_Object = MibTableColumn
etsysIpSlaPdvDataMinOneWayDS = _EtsysIpSlaPdvDataMinOneWayDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 28),
    _EtsysIpSlaPdvDataMinOneWayDS_Type()
)
etsysIpSlaPdvDataMinOneWayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMinOneWayDS.setStatus("current")
_EtsysIpSlaPdvDataMaxOneWayDS_Type = Gauge32
_EtsysIpSlaPdvDataMaxOneWayDS_Object = MibTableColumn
etsysIpSlaPdvDataMaxOneWayDS = _EtsysIpSlaPdvDataMaxOneWayDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 29),
    _EtsysIpSlaPdvDataMaxOneWayDS_Type()
)
etsysIpSlaPdvDataMaxOneWayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataMaxOneWayDS.setStatus("current")
_EtsysIpSlaPdvDataSumOneWayDS_Type = Gauge32
_EtsysIpSlaPdvDataSumOneWayDS_Object = MibTableColumn
etsysIpSlaPdvDataSumOneWayDS = _EtsysIpSlaPdvDataSumOneWayDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 30),
    _EtsysIpSlaPdvDataSumOneWayDS_Type()
)
etsysIpSlaPdvDataSumOneWayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumOneWayDS.setStatus("current")
_EtsysIpSlaPdvDataSumSquareOneWayDS_Type = Gauge32
_EtsysIpSlaPdvDataSumSquareOneWayDS_Object = MibTableColumn
etsysIpSlaPdvDataSumSquareOneWayDS = _EtsysIpSlaPdvDataSumSquareOneWayDS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 6, 1, 31),
    _EtsysIpSlaPdvDataSumSquareOneWayDS_Type()
)
etsysIpSlaPdvDataSumSquareOneWayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaPdvDataSumSquareOneWayDS.setStatus("current")
_EtsysIpSlaDistDataTable_Object = MibTable
etsysIpSlaDistDataTable = _EtsysIpSlaDistDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 7)
)
if mibBuilder.loadTexts:
    etsysIpSlaDistDataTable.setStatus("current")
_EtsysIpSlaDistDataEntry_Object = MibTableRow
etsysIpSlaDistDataEntry = _EtsysIpSlaDistDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 7, 1)
)
etsysIpSlaDistDataEntry.setIndexNames(
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionType"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaPathIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaHopIndex"),
    (0, "ENTERASYS-IP-SLA-MIB", "etsysIpSlaBucketIndex"),
)
if mibBuilder.loadTexts:
    etsysIpSlaDistDataEntry.setStatus("current")
_EtsysIpSlaDistMinRange_Type = Unsigned32
_EtsysIpSlaDistMinRange_Object = MibTableColumn
etsysIpSlaDistMinRange = _EtsysIpSlaDistMinRange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 7, 1, 1),
    _EtsysIpSlaDistMinRange_Type()
)
etsysIpSlaDistMinRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaDistMinRange.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaDistMinRange.setUnits("milliseconds")
_EtsysIpSlaDistMaxRange_Type = Unsigned32
_EtsysIpSlaDistMaxRange_Object = MibTableColumn
etsysIpSlaDistMaxRange = _EtsysIpSlaDistMaxRange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 1, 2, 7, 1, 2),
    _EtsysIpSlaDistMaxRange_Type()
)
etsysIpSlaDistMaxRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIpSlaDistMaxRange.setStatus("current")
if mibBuilder.loadTexts:
    etsysIpSlaDistMaxRange.setUnits("milliseconds")
_EtsysIpSlaConformance_ObjectIdentity = ObjectIdentity
etsysIpSlaConformance = _EtsysIpSlaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2)
)
_EtsysIpSlaGroups_ObjectIdentity = ObjectIdentity
etsysIpSlaGroups = _EtsysIpSlaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 1)
)
_EtsysIpSlaCompliances_ObjectIdentity = ObjectIdentity
etsysIpSlaCompliances = _EtsysIpSlaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 2)
)

# Managed Objects groups

etsysIpSlaGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 1, 1)
)
etsysIpSlaGlobalGroup.setObjects(
      *(("ENTERASYS-IP-SLA-MIB", "etsysIpSlaMaxEntries"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaEntriesInUse"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaMaxDataEntries"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaDataEntriesInUse"))
)
if mibBuilder.loadTexts:
    etsysIpSlaGlobalGroup.setStatus("current")

etsysIpSlaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 1, 2)
)
etsysIpSlaConfigGroup.setObjects(
      *(("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigType"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigDestType"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigDestAddr"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigDestPort"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigProbeName"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigPathCount"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigHopCount"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigHistoryCollections"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigHistoryBuckets"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigHistoryBucketType"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigHistorySamples"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigHistoryInterval"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigHistoryAgeout"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigHistoryWrap"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigDistributionCount"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigDistributionInterval"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigStatisticsCollections"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigStatus"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaScheduleStartTime"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaScheduleRecurrence"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaScheduleTestRepetitions"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaScheduleTestDuration"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaScheduleTestFrequency"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaScheduleTestState"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaScheduleTestStatus"))
)
if mibBuilder.loadTexts:
    etsysIpSlaConfigGroup.setStatus("current")

etsysIpSlaCollectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 1, 3)
)
etsysIpSlaCollectionGroup.setObjects(
      *(("ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionStartTime"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionNumPaths"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpslaCollectionNumHops"))
)
if mibBuilder.loadTexts:
    etsysIpSlaCollectionGroup.setStatus("current")

etsysIpSlaPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 1, 4)
)
etsysIpSlaPathGroup.setObjects(
      *(("ENTERASYS-IP-SLA-MIB", "etsysIpSlaHopDestType"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaHopDestAddr"))
)
if mibBuilder.loadTexts:
    etsysIpSlaPathGroup.setStatus("current")

etsysIpSlaRttGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 1, 5)
)
etsysIpSlaRttGroup.setObjects(
      *(("ENTERASYS-IP-SLA-MIB", "etsysIpSlaBucketTime"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataSamples"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataMinDelay"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataAvgDelay"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataMaxDelay"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataSum"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataSumSquareLow"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataSumSquareHigh"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataPktOutOfOrder"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataPktLateArrival"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataPktMissing"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataPktIpTosMismatch"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataPktVlanPcpMismatch"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttDataTxErrors"))
)
if mibBuilder.loadTexts:
    etsysIpSlaRttGroup.setStatus("current")

etsysIpSlaPdvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 1, 6)
)
etsysIpSlaPdvGroup.setObjects(
      *(("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSamples"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMinPositiveSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMaxPositiveSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataNumPositiveSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumPositiveSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumSquarePositiveSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMinNegativeSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMaxNegativeSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataNumNegativeSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumNegativeSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumSquareNegativeSD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMinPositiveDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMaxPositiveDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataNumPositiveDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumPositiveDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumSquarePositiveDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMinNegativeDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMaxNegativeDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataNumNegativeDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumNegativeDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumSquareNegativeDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataNumOneWaySD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMinOneWaySD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMaxOneWaySD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumOneWaySD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumSquareOneWaySD"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataNumOneWayDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMinOneWayDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataMaxOneWayDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumOneWayDS"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPdvDataSumSquareOneWayDS"))
)
if mibBuilder.loadTexts:
    etsysIpSlaPdvGroup.setStatus("current")

etsysIpSlaDistribGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 1, 7)
)
etsysIpSlaDistribGroup.setObjects(
      *(("ENTERASYS-IP-SLA-MIB", "etsysIpSlaDistMinRange"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaDistMaxRange"))
)
if mibBuilder.loadTexts:
    etsysIpSlaDistribGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysIpSlaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 94, 2, 2, 1)
)
etsysIpSlaCompliance.setObjects(
      *(("ENTERASYS-IP-SLA-MIB", "etsysIpSlaConfigGroup"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaCollectionGroup"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaPathGroup"),
        ("ENTERASYS-IP-SLA-MIB", "etsysIpSlaRttGroup"))
)
if mibBuilder.loadTexts:
    etsysIpSlaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IP-SLA-MIB",
    **{"etsysIpSlaMIB": etsysIpSlaMIB,
       "etsysIpSla": etsysIpSla,
       "etsysIpSlaGlobals": etsysIpSlaGlobals,
       "etsysIpSlaMaxEntries": etsysIpSlaMaxEntries,
       "etsysIpSlaEntriesInUse": etsysIpSlaEntriesInUse,
       "etsysIpSlaMaxDataEntries": etsysIpSlaMaxDataEntries,
       "etsysIpSlaDataEntriesInUse": etsysIpSlaDataEntriesInUse,
       "etsysIpSlaTables": etsysIpSlaTables,
       "etsysIpSlaConfigTable": etsysIpSlaConfigTable,
       "etsysIpSlaConfigEntry": etsysIpSlaConfigEntry,
       "etsysIpSlaConfigIndex": etsysIpSlaConfigIndex,
       "etsysIpSlaConfigType": etsysIpSlaConfigType,
       "etsysIpSlaConfigDestType": etsysIpSlaConfigDestType,
       "etsysIpSlaConfigDestAddr": etsysIpSlaConfigDestAddr,
       "etsysIpSlaConfigDestPort": etsysIpSlaConfigDestPort,
       "etsysIpSlaConfigProbeName": etsysIpSlaConfigProbeName,
       "etsysIpSlaConfigPathCount": etsysIpSlaConfigPathCount,
       "etsysIpSlaConfigHopCount": etsysIpSlaConfigHopCount,
       "etsysIpSlaConfigHistoryCollections": etsysIpSlaConfigHistoryCollections,
       "etsysIpSlaConfigHistoryBuckets": etsysIpSlaConfigHistoryBuckets,
       "etsysIpSlaConfigHistoryBucketType": etsysIpSlaConfigHistoryBucketType,
       "etsysIpSlaConfigHistorySamples": etsysIpSlaConfigHistorySamples,
       "etsysIpSlaConfigHistoryInterval": etsysIpSlaConfigHistoryInterval,
       "etsysIpSlaConfigHistoryAgeout": etsysIpSlaConfigHistoryAgeout,
       "etsysIpSlaConfigHistoryWrap": etsysIpSlaConfigHistoryWrap,
       "etsysIpSlaConfigDistributionCount": etsysIpSlaConfigDistributionCount,
       "etsysIpSlaConfigDistributionInterval": etsysIpSlaConfigDistributionInterval,
       "etsysIpSlaConfigStatisticsCollections": etsysIpSlaConfigStatisticsCollections,
       "etsysIpSlaConfigStatus": etsysIpSlaConfigStatus,
       "etsysIpSlaScheduleTable": etsysIpSlaScheduleTable,
       "etsysIpSlaScheduleEntry": etsysIpSlaScheduleEntry,
       "etsysIpSlaScheduleStartTime": etsysIpSlaScheduleStartTime,
       "etsysIpSlaScheduleRecurrence": etsysIpSlaScheduleRecurrence,
       "etsysIpSlaScheduleTestRepetitions": etsysIpSlaScheduleTestRepetitions,
       "etsysIpSlaScheduleTestDuration": etsysIpSlaScheduleTestDuration,
       "etsysIpSlaScheduleTestFrequency": etsysIpSlaScheduleTestFrequency,
       "etsysIpSlaScheduleTestState": etsysIpSlaScheduleTestState,
       "etsysIpSlaScheduleTestStatus": etsysIpSlaScheduleTestStatus,
       "etsysIpSlaCollectionTable": etsysIpSlaCollectionTable,
       "etsysIpSlaCollectionEntry": etsysIpSlaCollectionEntry,
       "etsysIpSlaCollectionType": etsysIpSlaCollectionType,
       "etsysIpSlaCollectionIndex": etsysIpSlaCollectionIndex,
       "etsysIpSlaCollectionStartTime": etsysIpSlaCollectionStartTime,
       "etsysIpSlaCollectionNumPaths": etsysIpSlaCollectionNumPaths,
       "etsysIpslaCollectionNumHops": etsysIpslaCollectionNumHops,
       "etsysIpSlaPathTable": etsysIpSlaPathTable,
       "etsysIpSlaPathEntry": etsysIpSlaPathEntry,
       "etsysIpSlaPathIndex": etsysIpSlaPathIndex,
       "etsysIpSlaHopIndex": etsysIpSlaHopIndex,
       "etsysIpSlaHopDestType": etsysIpSlaHopDestType,
       "etsysIpSlaHopDestAddr": etsysIpSlaHopDestAddr,
       "etsysIpSlaRttDataTable": etsysIpSlaRttDataTable,
       "etsysIpSlaRttDataEntry": etsysIpSlaRttDataEntry,
       "etsysIpSlaBucketIndex": etsysIpSlaBucketIndex,
       "etsysIpSlaBucketTime": etsysIpSlaBucketTime,
       "etsysIpSlaRttDataSamples": etsysIpSlaRttDataSamples,
       "etsysIpSlaRttDataMinDelay": etsysIpSlaRttDataMinDelay,
       "etsysIpSlaRttDataAvgDelay": etsysIpSlaRttDataAvgDelay,
       "etsysIpSlaRttDataMaxDelay": etsysIpSlaRttDataMaxDelay,
       "etsysIpSlaRttDataSum": etsysIpSlaRttDataSum,
       "etsysIpSlaRttDataSumSquareLow": etsysIpSlaRttDataSumSquareLow,
       "etsysIpSlaRttDataSumSquareHigh": etsysIpSlaRttDataSumSquareHigh,
       "etsysIpSlaRttDataPktOutOfOrder": etsysIpSlaRttDataPktOutOfOrder,
       "etsysIpSlaRttDataPktLateArrival": etsysIpSlaRttDataPktLateArrival,
       "etsysIpSlaRttDataPktMissing": etsysIpSlaRttDataPktMissing,
       "etsysIpSlaRttDataPktIpTosMismatch": etsysIpSlaRttDataPktIpTosMismatch,
       "etsysIpSlaRttDataPktVlanPcpMismatch": etsysIpSlaRttDataPktVlanPcpMismatch,
       "etsysIpSlaRttDataTxErrors": etsysIpSlaRttDataTxErrors,
       "etsysIpSlaPdvDataTable": etsysIpSlaPdvDataTable,
       "etsysIpSlaPdvDataEntry": etsysIpSlaPdvDataEntry,
       "etsysIpSlaPdvDataSamples": etsysIpSlaPdvDataSamples,
       "etsysIpSlaPdvDataMinPositiveSD": etsysIpSlaPdvDataMinPositiveSD,
       "etsysIpSlaPdvDataMaxPositiveSD": etsysIpSlaPdvDataMaxPositiveSD,
       "etsysIpSlaPdvDataNumPositiveSD": etsysIpSlaPdvDataNumPositiveSD,
       "etsysIpSlaPdvDataSumPositiveSD": etsysIpSlaPdvDataSumPositiveSD,
       "etsysIpSlaPdvDataSumSquarePositiveSD": etsysIpSlaPdvDataSumSquarePositiveSD,
       "etsysIpSlaPdvDataMinNegativeSD": etsysIpSlaPdvDataMinNegativeSD,
       "etsysIpSlaPdvDataMaxNegativeSD": etsysIpSlaPdvDataMaxNegativeSD,
       "etsysIpSlaPdvDataNumNegativeSD": etsysIpSlaPdvDataNumNegativeSD,
       "etsysIpSlaPdvDataSumNegativeSD": etsysIpSlaPdvDataSumNegativeSD,
       "etsysIpSlaPdvDataSumSquareNegativeSD": etsysIpSlaPdvDataSumSquareNegativeSD,
       "etsysIpSlaPdvDataMinPositiveDS": etsysIpSlaPdvDataMinPositiveDS,
       "etsysIpSlaPdvDataMaxPositiveDS": etsysIpSlaPdvDataMaxPositiveDS,
       "etsysIpSlaPdvDataNumPositiveDS": etsysIpSlaPdvDataNumPositiveDS,
       "etsysIpSlaPdvDataSumPositiveDS": etsysIpSlaPdvDataSumPositiveDS,
       "etsysIpSlaPdvDataSumSquarePositiveDS": etsysIpSlaPdvDataSumSquarePositiveDS,
       "etsysIpSlaPdvDataMinNegativeDS": etsysIpSlaPdvDataMinNegativeDS,
       "etsysIpSlaPdvDataMaxNegativeDS": etsysIpSlaPdvDataMaxNegativeDS,
       "etsysIpSlaPdvDataNumNegativeDS": etsysIpSlaPdvDataNumNegativeDS,
       "etsysIpSlaPdvDataSumNegativeDS": etsysIpSlaPdvDataSumNegativeDS,
       "etsysIpSlaPdvDataSumSquareNegativeDS": etsysIpSlaPdvDataSumSquareNegativeDS,
       "etsysIpSlaPdvDataNumOneWaySD": etsysIpSlaPdvDataNumOneWaySD,
       "etsysIpSlaPdvDataMinOneWaySD": etsysIpSlaPdvDataMinOneWaySD,
       "etsysIpSlaPdvDataMaxOneWaySD": etsysIpSlaPdvDataMaxOneWaySD,
       "etsysIpSlaPdvDataSumOneWaySD": etsysIpSlaPdvDataSumOneWaySD,
       "etsysIpSlaPdvDataSumSquareOneWaySD": etsysIpSlaPdvDataSumSquareOneWaySD,
       "etsysIpSlaPdvDataNumOneWayDS": etsysIpSlaPdvDataNumOneWayDS,
       "etsysIpSlaPdvDataMinOneWayDS": etsysIpSlaPdvDataMinOneWayDS,
       "etsysIpSlaPdvDataMaxOneWayDS": etsysIpSlaPdvDataMaxOneWayDS,
       "etsysIpSlaPdvDataSumOneWayDS": etsysIpSlaPdvDataSumOneWayDS,
       "etsysIpSlaPdvDataSumSquareOneWayDS": etsysIpSlaPdvDataSumSquareOneWayDS,
       "etsysIpSlaDistDataTable": etsysIpSlaDistDataTable,
       "etsysIpSlaDistDataEntry": etsysIpSlaDistDataEntry,
       "etsysIpSlaDistMinRange": etsysIpSlaDistMinRange,
       "etsysIpSlaDistMaxRange": etsysIpSlaDistMaxRange,
       "etsysIpSlaConformance": etsysIpSlaConformance,
       "etsysIpSlaGroups": etsysIpSlaGroups,
       "etsysIpSlaGlobalGroup": etsysIpSlaGlobalGroup,
       "etsysIpSlaConfigGroup": etsysIpSlaConfigGroup,
       "etsysIpSlaCollectionGroup": etsysIpSlaCollectionGroup,
       "etsysIpSlaPathGroup": etsysIpSlaPathGroup,
       "etsysIpSlaRttGroup": etsysIpSlaRttGroup,
       "etsysIpSlaPdvGroup": etsysIpSlaPdvGroup,
       "etsysIpSlaDistribGroup": etsysIpSlaDistribGroup,
       "etsysIpSlaCompliances": etsysIpSlaCompliances,
       "etsysIpSlaCompliance": etsysIpSlaCompliance}
)
