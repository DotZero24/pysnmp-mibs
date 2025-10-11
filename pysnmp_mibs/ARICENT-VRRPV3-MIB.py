# SNMP MIB module (ARICENT-VRRPV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-VRRPV3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:27 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")

(vrrpv3OperationsEntry,) = mibBuilder.importSymbols(
    "VRRPV3-MIB",
    "vrrpv3OperationsEntry")


# MODULE-IDENTITY

fsvrrpv3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85)
)
if mibBuilder.loadTexts:
    fsvrrpv3.setRevisions(
        ("2013-11-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVrrpv3Objects_ObjectIdentity = ObjectIdentity
fsVrrpv3Objects = _FsVrrpv3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1)
)
_FsVrrpv3System_ObjectIdentity = ObjectIdentity
fsVrrpv3System = _FsVrrpv3System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 1)
)


class _FsVrrpVersionSupported_Type(Integer32):
    """Custom type fsVrrpVersionSupported based on Integer32"""
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
        *(("version2", 1),
          ("version2And3", 2),
          ("version3", 3))
    )


_FsVrrpVersionSupported_Type.__name__ = "Integer32"
_FsVrrpVersionSupported_Object = MibScalar
fsVrrpVersionSupported = _FsVrrpVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 1, 1),
    _FsVrrpVersionSupported_Type()
)
fsVrrpVersionSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpVersionSupported.setStatus("current")


class _FsVrrpv3TraceOption_Type(Integer32):
    """Custom type fsVrrpv3TraceOption based on Integer32"""
    defaultValue = 0


_FsVrrpv3TraceOption_Type.__name__ = "Integer32"
_FsVrrpv3TraceOption_Object = MibScalar
fsVrrpv3TraceOption = _FsVrrpv3TraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 1, 2),
    _FsVrrpv3TraceOption_Type()
)
fsVrrpv3TraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpv3TraceOption.setStatus("current")


class _FsVrrpv3NotificationCntl_Type(Integer32):
    """Custom type fsVrrpv3NotificationCntl based on Integer32"""
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


_FsVrrpv3NotificationCntl_Type.__name__ = "Integer32"
_FsVrrpv3NotificationCntl_Object = MibScalar
fsVrrpv3NotificationCntl = _FsVrrpv3NotificationCntl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 1, 3),
    _FsVrrpv3NotificationCntl_Type()
)
fsVrrpv3NotificationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpv3NotificationCntl.setStatus("current")


class _FsVrrpv3Status_Type(Integer32):
    """Custom type fsVrrpv3Status based on Integer32"""
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


_FsVrrpv3Status_Type.__name__ = "Integer32"
_FsVrrpv3Status_Object = MibScalar
fsVrrpv3Status = _FsVrrpv3Status_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 1, 4),
    _FsVrrpv3Status_Type()
)
fsVrrpv3Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpv3Status.setStatus("current")
_FsVrrpv3MaxOperEntries_Type = Integer32
_FsVrrpv3MaxOperEntries_Object = MibScalar
fsVrrpv3MaxOperEntries = _FsVrrpv3MaxOperEntries_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 1, 5),
    _FsVrrpv3MaxOperEntries_Type()
)
fsVrrpv3MaxOperEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpv3MaxOperEntries.setStatus("current")
_FsVrrpv3MaxAssociatedIpEntries_Type = Integer32
_FsVrrpv3MaxAssociatedIpEntries_Object = MibScalar
fsVrrpv3MaxAssociatedIpEntries = _FsVrrpv3MaxAssociatedIpEntries_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 1, 6),
    _FsVrrpv3MaxAssociatedIpEntries_Type()
)
fsVrrpv3MaxAssociatedIpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpv3MaxAssociatedIpEntries.setStatus("current")
_FsVrrpv3Operations_ObjectIdentity = ObjectIdentity
fsVrrpv3Operations = _FsVrrpv3Operations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2)
)
_FsVrrpv3OperationsTable_Object = MibTable
fsVrrpv3OperationsTable = _FsVrrpv3OperationsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTable.setStatus("current")
_FsVrrpv3OperationsEntry_Object = MibTableRow
fsVrrpv3OperationsEntry = _FsVrrpv3OperationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsVrrpv3OperationsEntry.setStatus("current")


class _FsVrrpv3OperationsTrackGroupId_Type(Unsigned32):
    """Custom type fsVrrpv3OperationsTrackGroupId based on Unsigned32"""
    defaultValue = 0


_FsVrrpv3OperationsTrackGroupId_Type.__name__ = "Unsigned32"
_FsVrrpv3OperationsTrackGroupId_Object = MibTableColumn
fsVrrpv3OperationsTrackGroupId = _FsVrrpv3OperationsTrackGroupId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 1, 1, 1),
    _FsVrrpv3OperationsTrackGroupId_Type()
)
fsVrrpv3OperationsTrackGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackGroupId.setStatus("current")


class _FsVrrpv3OperationsDecrementPriority_Type(Unsigned32):
    """Custom type fsVrrpv3OperationsDecrementPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_FsVrrpv3OperationsDecrementPriority_Type.__name__ = "Unsigned32"
_FsVrrpv3OperationsDecrementPriority_Object = MibTableColumn
fsVrrpv3OperationsDecrementPriority = _FsVrrpv3OperationsDecrementPriority_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 1, 1, 2),
    _FsVrrpv3OperationsDecrementPriority_Type()
)
fsVrrpv3OperationsDecrementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpv3OperationsDecrementPriority.setStatus("current")
_FsVrrpv3OperationsTrackGroupTable_Object = MibTable
fsVrrpv3OperationsTrackGroupTable = _FsVrrpv3OperationsTrackGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackGroupTable.setStatus("current")
_FsVrrpv3OperationsTrackGroupEntry_Object = MibTableRow
fsVrrpv3OperationsTrackGroupEntry = _FsVrrpv3OperationsTrackGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 2, 1)
)
fsVrrpv3OperationsTrackGroupEntry.setIndexNames(
    (0, "ARICENT-VRRPV3-MIB", "fsVrrpv3OperationsTrackGroupIndex"),
)
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackGroupEntry.setStatus("current")
_FsVrrpv3OperationsTrackGroupIndex_Type = Unsigned32
_FsVrrpv3OperationsTrackGroupIndex_Object = MibTableColumn
fsVrrpv3OperationsTrackGroupIndex = _FsVrrpv3OperationsTrackGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 2, 1, 1),
    _FsVrrpv3OperationsTrackGroupIndex_Type()
)
fsVrrpv3OperationsTrackGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackGroupIndex.setStatus("current")
_FsVrrpv3OperationsTrackedGroupTrackedLinks_Type = Unsigned32
_FsVrrpv3OperationsTrackedGroupTrackedLinks_Object = MibTableColumn
fsVrrpv3OperationsTrackedGroupTrackedLinks = _FsVrrpv3OperationsTrackedGroupTrackedLinks_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 2, 1, 2),
    _FsVrrpv3OperationsTrackedGroupTrackedLinks_Type()
)
fsVrrpv3OperationsTrackedGroupTrackedLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackedGroupTrackedLinks.setStatus("current")
_FsVrrpv3OperationsTrackRowStatus_Type = RowStatus
_FsVrrpv3OperationsTrackRowStatus_Object = MibTableColumn
fsVrrpv3OperationsTrackRowStatus = _FsVrrpv3OperationsTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 2, 1, 3),
    _FsVrrpv3OperationsTrackRowStatus_Type()
)
fsVrrpv3OperationsTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackRowStatus.setStatus("current")
_FsVrrpv3OperationsTrackGroupIfTable_Object = MibTable
fsVrrpv3OperationsTrackGroupIfTable = _FsVrrpv3OperationsTrackGroupIfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackGroupIfTable.setStatus("current")
_FsVrrpv3OperationsTrackGroupIfEntry_Object = MibTableRow
fsVrrpv3OperationsTrackGroupIfEntry = _FsVrrpv3OperationsTrackGroupIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 3, 1)
)
fsVrrpv3OperationsTrackGroupIfEntry.setIndexNames(
    (0, "ARICENT-VRRPV3-MIB", "fsVrrpv3OperationsTrackGroupIndex"),
    (0, "ARICENT-VRRPV3-MIB", "fsVrrpv3OperationsTrackGroupIfIndex"),
)
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackGroupIfEntry.setStatus("current")
_FsVrrpv3OperationsTrackGroupIfIndex_Type = InterfaceIndexOrZero
_FsVrrpv3OperationsTrackGroupIfIndex_Object = MibTableColumn
fsVrrpv3OperationsTrackGroupIfIndex = _FsVrrpv3OperationsTrackGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 3, 1, 1),
    _FsVrrpv3OperationsTrackGroupIfIndex_Type()
)
fsVrrpv3OperationsTrackGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackGroupIfIndex.setStatus("current")
_FsVrrpv3OperationsTrackGroupIfRowStatus_Type = RowStatus
_FsVrrpv3OperationsTrackGroupIfRowStatus_Object = MibTableColumn
fsVrrpv3OperationsTrackGroupIfRowStatus = _FsVrrpv3OperationsTrackGroupIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 2, 3, 1, 2),
    _FsVrrpv3OperationsTrackGroupIfRowStatus_Type()
)
fsVrrpv3OperationsTrackGroupIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVrrpv3OperationsTrackGroupIfRowStatus.setStatus("current")
_FsVrrpv3Statistics_ObjectIdentity = ObjectIdentity
fsVrrpv3Statistics = _FsVrrpv3Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 3)
)
_FsVrrpv3StatisticsTable_Object = MibTable
fsVrrpv3StatisticsTable = _FsVrrpv3StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsTable.setStatus("current")
_FsVrrpv3StatisticsEntry_Object = MibTableRow
fsVrrpv3StatisticsEntry = _FsVrrpv3StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsEntry.setStatus("current")
_FsVrrpv3StatisticsTxedAdvertisements_Type = Counter64
_FsVrrpv3StatisticsTxedAdvertisements_Object = MibTableColumn
fsVrrpv3StatisticsTxedAdvertisements = _FsVrrpv3StatisticsTxedAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 3, 1, 1, 1),
    _FsVrrpv3StatisticsTxedAdvertisements_Type()
)
fsVrrpv3StatisticsTxedAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsTxedAdvertisements.setStatus("current")
_FsVrrpv3StatisticsTxedV2Advertisements_Type = Counter64
_FsVrrpv3StatisticsTxedV2Advertisements_Object = MibTableColumn
fsVrrpv3StatisticsTxedV2Advertisements = _FsVrrpv3StatisticsTxedV2Advertisements_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 3, 1, 1, 2),
    _FsVrrpv3StatisticsTxedV2Advertisements_Type()
)
fsVrrpv3StatisticsTxedV2Advertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsTxedV2Advertisements.setStatus("current")
_FsVrrpv3StatisticsV2AdvertiseIgnored_Type = Counter64
_FsVrrpv3StatisticsV2AdvertiseIgnored_Object = MibTableColumn
fsVrrpv3StatisticsV2AdvertiseIgnored = _FsVrrpv3StatisticsV2AdvertiseIgnored_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 3, 1, 1, 3),
    _FsVrrpv3StatisticsV2AdvertiseIgnored_Type()
)
fsVrrpv3StatisticsV2AdvertiseIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsV2AdvertiseIgnored.setStatus("current")
_FsVrrpv3StatisticsMasterAdverInterval_Type = TimeInterval
_FsVrrpv3StatisticsMasterAdverInterval_Object = MibTableColumn
fsVrrpv3StatisticsMasterAdverInterval = _FsVrrpv3StatisticsMasterAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 3, 1, 1, 4),
    _FsVrrpv3StatisticsMasterAdverInterval_Type()
)
fsVrrpv3StatisticsMasterAdverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsMasterAdverInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsMasterAdverInterval.setUnits("centiseconds")
_FsVrrpv3StatisticsSkewTime_Type = TimeInterval
_FsVrrpv3StatisticsSkewTime_Object = MibTableColumn
fsVrrpv3StatisticsSkewTime = _FsVrrpv3StatisticsSkewTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 3, 1, 1, 5),
    _FsVrrpv3StatisticsSkewTime_Type()
)
fsVrrpv3StatisticsSkewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsSkewTime.setStatus("current")
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsSkewTime.setUnits("centiseconds")
_FsVrrpv3StatisticsMasterDownInterval_Type = TimeInterval
_FsVrrpv3StatisticsMasterDownInterval_Object = MibTableColumn
fsVrrpv3StatisticsMasterDownInterval = _FsVrrpv3StatisticsMasterDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 85, 1, 3, 1, 1, 6),
    _FsVrrpv3StatisticsMasterDownInterval_Type()
)
fsVrrpv3StatisticsMasterDownInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsMasterDownInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsVrrpv3StatisticsMasterDownInterval.setUnits("centiseconds")
vrrpv3OperationsEntry.registerAugmentions(
    ("ARICENT-VRRPV3-MIB",
     "fsVrrpv3OperationsEntry")
)
fsVrrpv3OperationsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())
vrrpv3OperationsEntry.registerAugmentions(
    ("ARICENT-VRRPV3-MIB",
     "fsVrrpv3StatisticsEntry")
)
fsVrrpv3StatisticsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-VRRPV3-MIB",
    **{"fsvrrpv3": fsvrrpv3,
       "fsVrrpv3Objects": fsVrrpv3Objects,
       "fsVrrpv3System": fsVrrpv3System,
       "fsVrrpVersionSupported": fsVrrpVersionSupported,
       "fsVrrpv3TraceOption": fsVrrpv3TraceOption,
       "fsVrrpv3NotificationCntl": fsVrrpv3NotificationCntl,
       "fsVrrpv3Status": fsVrrpv3Status,
       "fsVrrpv3MaxOperEntries": fsVrrpv3MaxOperEntries,
       "fsVrrpv3MaxAssociatedIpEntries": fsVrrpv3MaxAssociatedIpEntries,
       "fsVrrpv3Operations": fsVrrpv3Operations,
       "fsVrrpv3OperationsTable": fsVrrpv3OperationsTable,
       "fsVrrpv3OperationsEntry": fsVrrpv3OperationsEntry,
       "fsVrrpv3OperationsTrackGroupId": fsVrrpv3OperationsTrackGroupId,
       "fsVrrpv3OperationsDecrementPriority": fsVrrpv3OperationsDecrementPriority,
       "fsVrrpv3OperationsTrackGroupTable": fsVrrpv3OperationsTrackGroupTable,
       "fsVrrpv3OperationsTrackGroupEntry": fsVrrpv3OperationsTrackGroupEntry,
       "fsVrrpv3OperationsTrackGroupIndex": fsVrrpv3OperationsTrackGroupIndex,
       "fsVrrpv3OperationsTrackedGroupTrackedLinks": fsVrrpv3OperationsTrackedGroupTrackedLinks,
       "fsVrrpv3OperationsTrackRowStatus": fsVrrpv3OperationsTrackRowStatus,
       "fsVrrpv3OperationsTrackGroupIfTable": fsVrrpv3OperationsTrackGroupIfTable,
       "fsVrrpv3OperationsTrackGroupIfEntry": fsVrrpv3OperationsTrackGroupIfEntry,
       "fsVrrpv3OperationsTrackGroupIfIndex": fsVrrpv3OperationsTrackGroupIfIndex,
       "fsVrrpv3OperationsTrackGroupIfRowStatus": fsVrrpv3OperationsTrackGroupIfRowStatus,
       "fsVrrpv3Statistics": fsVrrpv3Statistics,
       "fsVrrpv3StatisticsTable": fsVrrpv3StatisticsTable,
       "fsVrrpv3StatisticsEntry": fsVrrpv3StatisticsEntry,
       "fsVrrpv3StatisticsTxedAdvertisements": fsVrrpv3StatisticsTxedAdvertisements,
       "fsVrrpv3StatisticsTxedV2Advertisements": fsVrrpv3StatisticsTxedV2Advertisements,
       "fsVrrpv3StatisticsV2AdvertiseIgnored": fsVrrpv3StatisticsV2AdvertiseIgnored,
       "fsVrrpv3StatisticsMasterAdverInterval": fsVrrpv3StatisticsMasterAdverInterval,
       "fsVrrpv3StatisticsSkewTime": fsVrrpv3StatisticsSkewTime,
       "fsVrrpv3StatisticsMasterDownInterval": fsVrrpv3StatisticsMasterDownInterval}
)
