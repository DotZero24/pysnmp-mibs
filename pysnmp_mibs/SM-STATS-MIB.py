# SNMP MIB module (SM-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siaemic/SM-STATS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:14:10 2025
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

(etherHistoryEntry,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "etherHistoryEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

smStatMibs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1)
)
if mibBuilder.loadTexts:
    smStatMibs.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OwnerString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class EntryStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )



# MIB Managed Objects in the order of their OIDs

_SmStats_ObjectIdentity = ObjectIdentity
smStats = _SmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1)
)
_PmQueueStatsTable_Object = MibTable
pmQueueStatsTable = _PmQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pmQueueStatsTable.setStatus("current")
_PmQueueStatsEntry_Object = MibTableRow
pmQueueStatsEntry = _PmQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1)
)
pmQueueStatsEntry.setIndexNames(
    (0, "SM-STATS-MIB", "pmQueueStatsIndex"),
)
if mibBuilder.loadTexts:
    pmQueueStatsEntry.setStatus("current")


class _PmQueueStatsIndex_Type(Integer32):
    """Custom type pmQueueStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PmQueueStatsIndex_Type.__name__ = "Integer32"
_PmQueueStatsIndex_Object = MibTableColumn
pmQueueStatsIndex = _PmQueueStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1, 1),
    _PmQueueStatsIndex_Type()
)
pmQueueStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueStatsIndex.setStatus("current")
_PmQueueStatsDataSource_Type = ObjectIdentifier
_PmQueueStatsDataSource_Object = MibTableColumn
pmQueueStatsDataSource = _PmQueueStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1, 2),
    _PmQueueStatsDataSource_Type()
)
pmQueueStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueStatsDataSource.setStatus("current")


class _PmQueueStatsQueue_Type(Unsigned32):
    """Custom type pmQueueStatsQueue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PmQueueStatsQueue_Type.__name__ = "Unsigned32"
_PmQueueStatsQueue_Object = MibTableColumn
pmQueueStatsQueue = _PmQueueStatsQueue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1, 3),
    _PmQueueStatsQueue_Type()
)
pmQueueStatsQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueStatsQueue.setStatus("current")
_PmQueueStatsTxPkts_Type = Counter64
_PmQueueStatsTxPkts_Object = MibTableColumn
pmQueueStatsTxPkts = _PmQueueStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1, 4),
    _PmQueueStatsTxPkts_Type()
)
pmQueueStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueStatsTxPkts.setStatus("current")
_PmQueueStatsTxBytes_Type = Counter64
_PmQueueStatsTxBytes_Object = MibTableColumn
pmQueueStatsTxBytes = _PmQueueStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1, 5),
    _PmQueueStatsTxBytes_Type()
)
pmQueueStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueStatsTxBytes.setStatus("current")
_PmQueueStatsTxDiscardPkts_Type = Counter64
_PmQueueStatsTxDiscardPkts_Object = MibTableColumn
pmQueueStatsTxDiscardPkts = _PmQueueStatsTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1, 6),
    _PmQueueStatsTxDiscardPkts_Type()
)
pmQueueStatsTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueStatsTxDiscardPkts.setStatus("current")
_PmQueueStatsTxDiscardBytes_Type = Counter64
_PmQueueStatsTxDiscardBytes_Object = MibTableColumn
pmQueueStatsTxDiscardBytes = _PmQueueStatsTxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1, 7),
    _PmQueueStatsTxDiscardBytes_Type()
)
pmQueueStatsTxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueStatsTxDiscardBytes.setStatus("current")
_PmQueueStatsOwner_Type = OwnerString
_PmQueueStatsOwner_Object = MibTableColumn
pmQueueStatsOwner = _PmQueueStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1, 8),
    _PmQueueStatsOwner_Type()
)
pmQueueStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueStatsOwner.setStatus("current")
_PmQueueStatsStatus_Type = EntryStatus
_PmQueueStatsStatus_Object = MibTableColumn
pmQueueStatsStatus = _PmQueueStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 1, 1, 9),
    _PmQueueStatsStatus_Type()
)
pmQueueStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueStatsStatus.setStatus("current")
_PmQueueHistoryControlTable_Object = MibTable
pmQueueHistoryControlTable = _PmQueueHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pmQueueHistoryControlTable.setStatus("current")
_PmQueueHistoryControlEntry_Object = MibTableRow
pmQueueHistoryControlEntry = _PmQueueHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1)
)
pmQueueHistoryControlEntry.setIndexNames(
    (0, "SM-STATS-MIB", "pmQueueHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    pmQueueHistoryControlEntry.setStatus("current")


class _PmQueueHistoryControlIndex_Type(Integer32):
    """Custom type pmQueueHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PmQueueHistoryControlIndex_Type.__name__ = "Integer32"
_PmQueueHistoryControlIndex_Object = MibTableColumn
pmQueueHistoryControlIndex = _PmQueueHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1, 1),
    _PmQueueHistoryControlIndex_Type()
)
pmQueueHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueHistoryControlIndex.setStatus("current")
_PmQueueHistoryControlQueue_Type = Unsigned32
_PmQueueHistoryControlQueue_Object = MibTableColumn
pmQueueHistoryControlQueue = _PmQueueHistoryControlQueue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1, 2),
    _PmQueueHistoryControlQueue_Type()
)
pmQueueHistoryControlQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueHistoryControlQueue.setStatus("current")
_PmQueueHistoryControlDataSource_Type = ObjectIdentifier
_PmQueueHistoryControlDataSource_Object = MibTableColumn
pmQueueHistoryControlDataSource = _PmQueueHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1, 3),
    _PmQueueHistoryControlDataSource_Type()
)
pmQueueHistoryControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueHistoryControlDataSource.setStatus("current")


class _PmQueueHistoryControlBucketsRequested_Type(Integer32):
    """Custom type pmQueueHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PmQueueHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_PmQueueHistoryControlBucketsRequested_Object = MibTableColumn
pmQueueHistoryControlBucketsRequested = _PmQueueHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1, 4),
    _PmQueueHistoryControlBucketsRequested_Type()
)
pmQueueHistoryControlBucketsRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueHistoryControlBucketsRequested.setStatus("current")


class _PmQueueHistoryControlBucketsGranted_Type(Integer32):
    """Custom type pmQueueHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PmQueueHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_PmQueueHistoryControlBucketsGranted_Object = MibTableColumn
pmQueueHistoryControlBucketsGranted = _PmQueueHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1, 5),
    _PmQueueHistoryControlBucketsGranted_Type()
)
pmQueueHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueHistoryControlBucketsGranted.setStatus("current")


class _PmQueueHistoryControlInterval_Type(Integer32):
    """Custom type pmQueueHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PmQueueHistoryControlInterval_Type.__name__ = "Integer32"
_PmQueueHistoryControlInterval_Object = MibTableColumn
pmQueueHistoryControlInterval = _PmQueueHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1, 6),
    _PmQueueHistoryControlInterval_Type()
)
pmQueueHistoryControlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueHistoryControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    pmQueueHistoryControlInterval.setUnits("Seconds")
_PmQueueHistoryControlOwner_Type = OwnerString
_PmQueueHistoryControlOwner_Object = MibTableColumn
pmQueueHistoryControlOwner = _PmQueueHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1, 7),
    _PmQueueHistoryControlOwner_Type()
)
pmQueueHistoryControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueHistoryControlOwner.setStatus("current")


class _PmQueueHistoryControlPersistence_Type(Integer32):
    """Custom type pmQueueHistoryControlPersistence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 2))
    )


_PmQueueHistoryControlPersistence_Type.__name__ = "Integer32"
_PmQueueHistoryControlPersistence_Object = MibTableColumn
pmQueueHistoryControlPersistence = _PmQueueHistoryControlPersistence_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1, 8),
    _PmQueueHistoryControlPersistence_Type()
)
pmQueueHistoryControlPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueHistoryControlPersistence.setStatus("current")
_PmQueueHistoryControlStatus_Type = EntryStatus
_PmQueueHistoryControlStatus_Object = MibTableColumn
pmQueueHistoryControlStatus = _PmQueueHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 2, 1, 9),
    _PmQueueHistoryControlStatus_Type()
)
pmQueueHistoryControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmQueueHistoryControlStatus.setStatus("current")
_PmQueueEtherHistoryTable_Object = MibTable
pmQueueEtherHistoryTable = _PmQueueEtherHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pmQueueEtherHistoryTable.setStatus("current")
_PmQueueEtherHistoryEntry_Object = MibTableRow
pmQueueEtherHistoryEntry = _PmQueueEtherHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 3, 1)
)
pmQueueEtherHistoryEntry.setIndexNames(
    (0, "SM-STATS-MIB", "pmQueueEtherHistoryIndex"),
    (0, "SM-STATS-MIB", "pmQueueEtherHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    pmQueueEtherHistoryEntry.setStatus("current")


class _PmQueueEtherHistoryIndex_Type(Integer32):
    """Custom type pmQueueEtherHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PmQueueEtherHistoryIndex_Type.__name__ = "Integer32"
_PmQueueEtherHistoryIndex_Object = MibTableColumn
pmQueueEtherHistoryIndex = _PmQueueEtherHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 3, 1, 1),
    _PmQueueEtherHistoryIndex_Type()
)
pmQueueEtherHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueEtherHistoryIndex.setStatus("current")


class _PmQueueEtherHistorySampleIndex_Type(Integer32):
    """Custom type pmQueueEtherHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmQueueEtherHistorySampleIndex_Type.__name__ = "Integer32"
_PmQueueEtherHistorySampleIndex_Object = MibTableColumn
pmQueueEtherHistorySampleIndex = _PmQueueEtherHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 3, 1, 2),
    _PmQueueEtherHistorySampleIndex_Type()
)
pmQueueEtherHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueEtherHistorySampleIndex.setStatus("current")
_PmQueueEtherHistoryIntervalStart_Type = TimeTicks
_PmQueueEtherHistoryIntervalStart_Object = MibTableColumn
pmQueueEtherHistoryIntervalStart = _PmQueueEtherHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 3, 1, 3),
    _PmQueueEtherHistoryIntervalStart_Type()
)
pmQueueEtherHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueEtherHistoryIntervalStart.setStatus("current")
_PmQueueHistoryTxPkts_Type = Counter64
_PmQueueHistoryTxPkts_Object = MibTableColumn
pmQueueHistoryTxPkts = _PmQueueHistoryTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 3, 1, 4),
    _PmQueueHistoryTxPkts_Type()
)
pmQueueHistoryTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueHistoryTxPkts.setStatus("current")
_PmQueueHistoryTxBytes_Type = Counter64
_PmQueueHistoryTxBytes_Object = MibTableColumn
pmQueueHistoryTxBytes = _PmQueueHistoryTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 3, 1, 5),
    _PmQueueHistoryTxBytes_Type()
)
pmQueueHistoryTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueHistoryTxBytes.setStatus("current")
_PmQueueHistoryTxDiscardPkts_Type = Counter64
_PmQueueHistoryTxDiscardPkts_Object = MibTableColumn
pmQueueHistoryTxDiscardPkts = _PmQueueHistoryTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 3, 1, 6),
    _PmQueueHistoryTxDiscardPkts_Type()
)
pmQueueHistoryTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueHistoryTxDiscardPkts.setStatus("current")
_PmQueueHistoryTxDiscardBytes_Type = Counter64
_PmQueueHistoryTxDiscardBytes_Object = MibTableColumn
pmQueueHistoryTxDiscardBytes = _PmQueueHistoryTxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 1, 3, 1, 7),
    _PmQueueHistoryTxDiscardBytes_Type()
)
pmQueueHistoryTxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmQueueHistoryTxDiscardBytes.setStatus("current")
_SmExtHistory_ObjectIdentity = ObjectIdentity
smExtHistory = _SmExtHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 2)
)
_ExtEtherHistoryTable_Object = MibTable
extEtherHistoryTable = _ExtEtherHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    extEtherHistoryTable.setStatus("current")
_ExtEtherHistoryEntry_Object = MibTableRow
extEtherHistoryEntry = _ExtEtherHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    extEtherHistoryEntry.setStatus("current")


class _EtherHistoryMinUtilization_Type(Integer32):
    """Custom type etherHistoryMinUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EtherHistoryMinUtilization_Type.__name__ = "Integer32"
_EtherHistoryMinUtilization_Object = MibTableColumn
etherHistoryMinUtilization = _EtherHistoryMinUtilization_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 2, 1, 1, 1),
    _EtherHistoryMinUtilization_Type()
)
etherHistoryMinUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryMinUtilization.setStatus("current")


class _EtherHistoryMaxUtilization_Type(Integer32):
    """Custom type etherHistoryMaxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EtherHistoryMaxUtilization_Type.__name__ = "Integer32"
_EtherHistoryMaxUtilization_Object = MibTableColumn
etherHistoryMaxUtilization = _EtherHistoryMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 2, 1, 1, 2),
    _EtherHistoryMaxUtilization_Type()
)
etherHistoryMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryMaxUtilization.setStatus("current")


class _EtherHistoryTxMinUtilization_Type(Integer32):
    """Custom type etherHistoryTxMinUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EtherHistoryTxMinUtilization_Type.__name__ = "Integer32"
_EtherHistoryTxMinUtilization_Object = MibTableColumn
etherHistoryTxMinUtilization = _EtherHistoryTxMinUtilization_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 2, 1, 1, 3),
    _EtherHistoryTxMinUtilization_Type()
)
etherHistoryTxMinUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryTxMinUtilization.setStatus("current")


class _EtherHistoryTxMaxUtilization_Type(Integer32):
    """Custom type etherHistoryTxMaxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EtherHistoryTxMaxUtilization_Type.__name__ = "Integer32"
_EtherHistoryTxMaxUtilization_Object = MibTableColumn
etherHistoryTxMaxUtilization = _EtherHistoryTxMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 29601, 100, 1, 1, 2, 1, 1, 4),
    _EtherHistoryTxMaxUtilization_Type()
)
etherHistoryTxMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryTxMaxUtilization.setStatus("current")
etherHistoryEntry.registerAugmentions(
    ("SM-STATS-MIB",
     "extEtherHistoryEntry")
)
extEtherHistoryEntry.setIndexNames(*etherHistoryEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SM-STATS-MIB",
    **{"OwnerString": OwnerString,
       "EntryStatus": EntryStatus,
       "smStatMibs": smStatMibs,
       "smStats": smStats,
       "pmQueueStatsTable": pmQueueStatsTable,
       "pmQueueStatsEntry": pmQueueStatsEntry,
       "pmQueueStatsIndex": pmQueueStatsIndex,
       "pmQueueStatsDataSource": pmQueueStatsDataSource,
       "pmQueueStatsQueue": pmQueueStatsQueue,
       "pmQueueStatsTxPkts": pmQueueStatsTxPkts,
       "pmQueueStatsTxBytes": pmQueueStatsTxBytes,
       "pmQueueStatsTxDiscardPkts": pmQueueStatsTxDiscardPkts,
       "pmQueueStatsTxDiscardBytes": pmQueueStatsTxDiscardBytes,
       "pmQueueStatsOwner": pmQueueStatsOwner,
       "pmQueueStatsStatus": pmQueueStatsStatus,
       "pmQueueHistoryControlTable": pmQueueHistoryControlTable,
       "pmQueueHistoryControlEntry": pmQueueHistoryControlEntry,
       "pmQueueHistoryControlIndex": pmQueueHistoryControlIndex,
       "pmQueueHistoryControlQueue": pmQueueHistoryControlQueue,
       "pmQueueHistoryControlDataSource": pmQueueHistoryControlDataSource,
       "pmQueueHistoryControlBucketsRequested": pmQueueHistoryControlBucketsRequested,
       "pmQueueHistoryControlBucketsGranted": pmQueueHistoryControlBucketsGranted,
       "pmQueueHistoryControlInterval": pmQueueHistoryControlInterval,
       "pmQueueHistoryControlOwner": pmQueueHistoryControlOwner,
       "pmQueueHistoryControlPersistence": pmQueueHistoryControlPersistence,
       "pmQueueHistoryControlStatus": pmQueueHistoryControlStatus,
       "pmQueueEtherHistoryTable": pmQueueEtherHistoryTable,
       "pmQueueEtherHistoryEntry": pmQueueEtherHistoryEntry,
       "pmQueueEtherHistoryIndex": pmQueueEtherHistoryIndex,
       "pmQueueEtherHistorySampleIndex": pmQueueEtherHistorySampleIndex,
       "pmQueueEtherHistoryIntervalStart": pmQueueEtherHistoryIntervalStart,
       "pmQueueHistoryTxPkts": pmQueueHistoryTxPkts,
       "pmQueueHistoryTxBytes": pmQueueHistoryTxBytes,
       "pmQueueHistoryTxDiscardPkts": pmQueueHistoryTxDiscardPkts,
       "pmQueueHistoryTxDiscardBytes": pmQueueHistoryTxDiscardBytes,
       "smExtHistory": smExtHistory,
       "extEtherHistoryTable": extEtherHistoryTable,
       "extEtherHistoryEntry": extEtherHistoryEntry,
       "etherHistoryMinUtilization": etherHistoryMinUtilization,
       "etherHistoryMaxUtilization": etherHistoryMaxUtilization,
       "etherHistoryTxMinUtilization": etherHistoryTxMinUtilization,
       "etherHistoryTxMaxUtilization": etherHistoryTxMaxUtilization}
)
