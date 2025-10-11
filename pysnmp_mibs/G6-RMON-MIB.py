# SNMP MIB module (G6-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-RMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:15 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rmon_ObjectIdentity = ObjectIdentity
rmon = _Rmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85)
)
_RmonClearAllCounter_Type = DisplayString
_RmonClearAllCounter_Object = MibScalar
rmonClearAllCounter = _RmonClearAllCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 1),
    _RmonClearAllCounter_Type()
)
rmonClearAllCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonClearAllCounter.setStatus("current")
_IngressTable_Object = MibTable
ingressTable = _IngressTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100)
)
if mibBuilder.loadTexts:
    ingressTable.setStatus("current")
_IngressEntry_Object = MibTableRow
ingressEntry = _IngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1)
)
ingressEntry.setIndexNames(
    (0, "G6-RMON-MIB", "ingressPortIndex"),
)
if mibBuilder.loadTexts:
    ingressEntry.setStatus("current")


class _IngressPortIndex_Type(Integer32):
    """Custom type ingressPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IngressPortIndex_Type.__name__ = "Integer32"
_IngressPortIndex_Object = MibTableColumn
ingressPortIndex = _IngressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 1),
    _IngressPortIndex_Type()
)
ingressPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ingressPortIndex.setStatus("current")


class _IngressEntryStatus_Type(Integer32):
    """Custom type ingressEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_IngressEntryStatus_Type.__name__ = "Integer32"
_IngressEntryStatus_Object = MibTableColumn
ingressEntryStatus = _IngressEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 2),
    _IngressEntryStatus_Type()
)
ingressEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressEntryStatus.setStatus("current")
_IngressInGoodOctetsLo_Type = Unsigned32
_IngressInGoodOctetsLo_Object = MibTableColumn
ingressInGoodOctetsLo = _IngressInGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 3),
    _IngressInGoodOctetsLo_Type()
)
ingressInGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInGoodOctetsLo.setStatus("current")
_IngressInGoodOctetsHi_Type = Unsigned32
_IngressInGoodOctetsHi_Object = MibTableColumn
ingressInGoodOctetsHi = _IngressInGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 4),
    _IngressInGoodOctetsHi_Type()
)
ingressInGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInGoodOctetsHi.setStatus("current")
_IngressInBadOctets_Type = Unsigned32
_IngressInBadOctets_Object = MibTableColumn
ingressInBadOctets = _IngressInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 5),
    _IngressInBadOctets_Type()
)
ingressInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInBadOctets.setStatus("current")
_IngressInTotalPackets_Type = Unsigned32
_IngressInTotalPackets_Object = MibTableColumn
ingressInTotalPackets = _IngressInTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 6),
    _IngressInTotalPackets_Type()
)
ingressInTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInTotalPackets.setStatus("current")
_IngressInUnicasts_Type = Unsigned32
_IngressInUnicasts_Object = MibTableColumn
ingressInUnicasts = _IngressInUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 7),
    _IngressInUnicasts_Type()
)
ingressInUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInUnicasts.setStatus("current")
_IngressInNonUnicasts_Type = Unsigned32
_IngressInNonUnicasts_Object = MibTableColumn
ingressInNonUnicasts = _IngressInNonUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 8),
    _IngressInNonUnicasts_Type()
)
ingressInNonUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInNonUnicasts.setStatus("current")
_IngressInBroadcasts_Type = Unsigned32
_IngressInBroadcasts_Object = MibTableColumn
ingressInBroadcasts = _IngressInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 9),
    _IngressInBroadcasts_Type()
)
ingressInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInBroadcasts.setStatus("current")
_IngressInMulticasts_Type = Unsigned32
_IngressInMulticasts_Object = MibTableColumn
ingressInMulticasts = _IngressInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 10),
    _IngressInMulticasts_Type()
)
ingressInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInMulticasts.setStatus("current")
_IngressInPause_Type = Unsigned32
_IngressInPause_Object = MibTableColumn
ingressInPause = _IngressInPause_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 11),
    _IngressInPause_Type()
)
ingressInPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInPause.setStatus("current")
_IngressInTotalReceiveErrors_Type = Unsigned32
_IngressInTotalReceiveErrors_Object = MibTableColumn
ingressInTotalReceiveErrors = _IngressInTotalReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 12),
    _IngressInTotalReceiveErrors_Type()
)
ingressInTotalReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInTotalReceiveErrors.setStatus("current")
_IngressInUndersize_Type = Unsigned32
_IngressInUndersize_Object = MibTableColumn
ingressInUndersize = _IngressInUndersize_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 13),
    _IngressInUndersize_Type()
)
ingressInUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInUndersize.setStatus("current")
_IngressInOversize_Type = Unsigned32
_IngressInOversize_Object = MibTableColumn
ingressInOversize = _IngressInOversize_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 14),
    _IngressInOversize_Type()
)
ingressInOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInOversize.setStatus("current")
_IngressInFragments_Type = Unsigned32
_IngressInFragments_Object = MibTableColumn
ingressInFragments = _IngressInFragments_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 15),
    _IngressInFragments_Type()
)
ingressInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInFragments.setStatus("current")
_IngressInJabber_Type = Unsigned32
_IngressInJabber_Object = MibTableColumn
ingressInJabber = _IngressInJabber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 16),
    _IngressInJabber_Type()
)
ingressInJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInJabber.setStatus("current")
_IngressInFcsErrors_Type = Unsigned32
_IngressInFcsErrors_Object = MibTableColumn
ingressInFcsErrors = _IngressInFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 17),
    _IngressInFcsErrors_Type()
)
ingressInFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInFcsErrors.setStatus("current")
_IngressInDiscarded_Type = Unsigned32
_IngressInDiscarded_Object = MibTableColumn
ingressInDiscarded = _IngressInDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 100, 1, 18),
    _IngressInDiscarded_Type()
)
ingressInDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressInDiscarded.setStatus("current")
_EgressTable_Object = MibTable
egressTable = _EgressTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101)
)
if mibBuilder.loadTexts:
    egressTable.setStatus("current")
_EgressEntry_Object = MibTableRow
egressEntry = _EgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1)
)
egressEntry.setIndexNames(
    (0, "G6-RMON-MIB", "egressPortIndex"),
)
if mibBuilder.loadTexts:
    egressEntry.setStatus("current")


class _EgressPortIndex_Type(Integer32):
    """Custom type egressPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_EgressPortIndex_Type.__name__ = "Integer32"
_EgressPortIndex_Object = MibTableColumn
egressPortIndex = _EgressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 1),
    _EgressPortIndex_Type()
)
egressPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    egressPortIndex.setStatus("current")
_EgressOutGoodOctetsLo_Type = Unsigned32
_EgressOutGoodOctetsLo_Object = MibTableColumn
egressOutGoodOctetsLo = _EgressOutGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 2),
    _EgressOutGoodOctetsLo_Type()
)
egressOutGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutGoodOctetsLo.setStatus("current")
_EgressOutGoodOctetsHi_Type = Unsigned32
_EgressOutGoodOctetsHi_Object = MibTableColumn
egressOutGoodOctetsHi = _EgressOutGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 3),
    _EgressOutGoodOctetsHi_Type()
)
egressOutGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutGoodOctetsHi.setStatus("current")
_EgressOutUnicasts_Type = Unsigned32
_EgressOutUnicasts_Object = MibTableColumn
egressOutUnicasts = _EgressOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 4),
    _EgressOutUnicasts_Type()
)
egressOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutUnicasts.setStatus("current")
_EgressOutNonUnicasts_Type = Unsigned32
_EgressOutNonUnicasts_Object = MibTableColumn
egressOutNonUnicasts = _EgressOutNonUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 5),
    _EgressOutNonUnicasts_Type()
)
egressOutNonUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutNonUnicasts.setStatus("current")
_EgressOutBroadcasts_Type = Unsigned32
_EgressOutBroadcasts_Object = MibTableColumn
egressOutBroadcasts = _EgressOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 6),
    _EgressOutBroadcasts_Type()
)
egressOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutBroadcasts.setStatus("current")
_EgressOutMulticasts_Type = Unsigned32
_EgressOutMulticasts_Object = MibTableColumn
egressOutMulticasts = _EgressOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 7),
    _EgressOutMulticasts_Type()
)
egressOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutMulticasts.setStatus("current")
_EgressOutPause_Type = Unsigned32
_EgressOutPause_Object = MibTableColumn
egressOutPause = _EgressOutPause_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 8),
    _EgressOutPause_Type()
)
egressOutPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutPause.setStatus("current")
_EgressOutDeferred_Type = Unsigned32
_EgressOutDeferred_Object = MibTableColumn
egressOutDeferred = _EgressOutDeferred_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 9),
    _EgressOutDeferred_Type()
)
egressOutDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutDeferred.setStatus("current")
_EgressOutTotalCollisions_Type = Unsigned32
_EgressOutTotalCollisions_Object = MibTableColumn
egressOutTotalCollisions = _EgressOutTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 10),
    _EgressOutTotalCollisions_Type()
)
egressOutTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutTotalCollisions.setStatus("current")
_EgressOutSingleCollisions_Type = Unsigned32
_EgressOutSingleCollisions_Object = MibTableColumn
egressOutSingleCollisions = _EgressOutSingleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 11),
    _EgressOutSingleCollisions_Type()
)
egressOutSingleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutSingleCollisions.setStatus("current")
_EgressOutMultipleCollisions_Type = Unsigned32
_EgressOutMultipleCollisions_Object = MibTableColumn
egressOutMultipleCollisions = _EgressOutMultipleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 12),
    _EgressOutMultipleCollisions_Type()
)
egressOutMultipleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutMultipleCollisions.setStatus("current")
_EgressOutExcessiveCollisions_Type = Unsigned32
_EgressOutExcessiveCollisions_Object = MibTableColumn
egressOutExcessiveCollisions = _EgressOutExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 13),
    _EgressOutExcessiveCollisions_Type()
)
egressOutExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutExcessiveCollisions.setStatus("current")
_EgressOutLateCollisions_Type = Unsigned32
_EgressOutLateCollisions_Object = MibTableColumn
egressOutLateCollisions = _EgressOutLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 14),
    _EgressOutLateCollisions_Type()
)
egressOutLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutLateCollisions.setStatus("current")
_EgressOutFcsErrors_Type = Unsigned32
_EgressOutFcsErrors_Object = MibTableColumn
egressOutFcsErrors = _EgressOutFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 15),
    _EgressOutFcsErrors_Type()
)
egressOutFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutFcsErrors.setStatus("current")
_EgressOutDroppedPackets_Type = Unsigned32
_EgressOutDroppedPackets_Object = MibTableColumn
egressOutDroppedPackets = _EgressOutDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 101, 1, 16),
    _EgressOutDroppedPackets_Type()
)
egressOutDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressOutDroppedPackets.setStatus("current")
_HistogramTable_Object = MibTable
histogramTable = _HistogramTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 102)
)
if mibBuilder.loadTexts:
    histogramTable.setStatus("current")
_HistogramEntry_Object = MibTableRow
histogramEntry = _HistogramEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 102, 1)
)
histogramEntry.setIndexNames(
    (0, "G6-RMON-MIB", "histogramPortIndex"),
)
if mibBuilder.loadTexts:
    histogramEntry.setStatus("current")


class _HistogramPortIndex_Type(Integer32):
    """Custom type histogramPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HistogramPortIndex_Type.__name__ = "Integer32"
_HistogramPortIndex_Object = MibTableColumn
histogramPortIndex = _HistogramPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 102, 1, 1),
    _HistogramPortIndex_Type()
)
histogramPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    histogramPortIndex.setStatus("current")
_HistogramIn64Octets_Type = Unsigned32
_HistogramIn64Octets_Object = MibTableColumn
histogramIn64Octets = _HistogramIn64Octets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 102, 1, 2),
    _HistogramIn64Octets_Type()
)
histogramIn64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histogramIn64Octets.setStatus("current")
_HistogramIn65To127Octets_Type = Unsigned32
_HistogramIn65To127Octets_Object = MibTableColumn
histogramIn65To127Octets = _HistogramIn65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 102, 1, 3),
    _HistogramIn65To127Octets_Type()
)
histogramIn65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histogramIn65To127Octets.setStatus("current")
_HistogramIn128To255Octets_Type = Unsigned32
_HistogramIn128To255Octets_Object = MibTableColumn
histogramIn128To255Octets = _HistogramIn128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 102, 1, 4),
    _HistogramIn128To255Octets_Type()
)
histogramIn128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histogramIn128To255Octets.setStatus("current")
_HistogramIn256To511Octets_Type = Unsigned32
_HistogramIn256To511Octets_Object = MibTableColumn
histogramIn256To511Octets = _HistogramIn256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 102, 1, 5),
    _HistogramIn256To511Octets_Type()
)
histogramIn256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histogramIn256To511Octets.setStatus("current")
_HistogramIn512To1023Octets_Type = Unsigned32
_HistogramIn512To1023Octets_Object = MibTableColumn
histogramIn512To1023Octets = _HistogramIn512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 102, 1, 6),
    _HistogramIn512To1023Octets_Type()
)
histogramIn512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histogramIn512To1023Octets.setStatus("current")
_HistogramIn1024ToMaxOctets_Type = Unsigned32
_HistogramIn1024ToMaxOctets_Object = MibTableColumn
histogramIn1024ToMaxOctets = _HistogramIn1024ToMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 102, 1, 7),
    _HistogramIn1024ToMaxOctets_Type()
)
histogramIn1024ToMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histogramIn1024ToMaxOctets.setStatus("current")
_UtilizationTable_Object = MibTable
utilizationTable = _UtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 103)
)
if mibBuilder.loadTexts:
    utilizationTable.setStatus("current")
_UtilizationEntry_Object = MibTableRow
utilizationEntry = _UtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 103, 1)
)
utilizationEntry.setIndexNames(
    (0, "G6-RMON-MIB", "utilizationPortIndex"),
)
if mibBuilder.loadTexts:
    utilizationEntry.setStatus("current")


class _UtilizationPortIndex_Type(Integer32):
    """Custom type utilizationPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_UtilizationPortIndex_Type.__name__ = "Integer32"
_UtilizationPortIndex_Object = MibTableColumn
utilizationPortIndex = _UtilizationPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 103, 1, 1),
    _UtilizationPortIndex_Type()
)
utilizationPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utilizationPortIndex.setStatus("current")


class _UtilizationIngressNow_Type(Integer32):
    """Custom type utilizationIngressNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UtilizationIngressNow_Type.__name__ = "Integer32"
_UtilizationIngressNow_Object = MibTableColumn
utilizationIngressNow = _UtilizationIngressNow_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 103, 1, 2),
    _UtilizationIngressNow_Type()
)
utilizationIngressNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utilizationIngressNow.setStatus("current")


class _UtilizationIngress30s_Type(Integer32):
    """Custom type utilizationIngress30s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UtilizationIngress30s_Type.__name__ = "Integer32"
_UtilizationIngress30s_Object = MibTableColumn
utilizationIngress30s = _UtilizationIngress30s_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 103, 1, 3),
    _UtilizationIngress30s_Type()
)
utilizationIngress30s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utilizationIngress30s.setStatus("current")


class _UtilizationIngress5min_Type(Integer32):
    """Custom type utilizationIngress5min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UtilizationIngress5min_Type.__name__ = "Integer32"
_UtilizationIngress5min_Object = MibTableColumn
utilizationIngress5min = _UtilizationIngress5min_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 103, 1, 4),
    _UtilizationIngress5min_Type()
)
utilizationIngress5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utilizationIngress5min.setStatus("current")


class _UtilizationEgressNow_Type(Integer32):
    """Custom type utilizationEgressNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UtilizationEgressNow_Type.__name__ = "Integer32"
_UtilizationEgressNow_Object = MibTableColumn
utilizationEgressNow = _UtilizationEgressNow_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 103, 1, 5),
    _UtilizationEgressNow_Type()
)
utilizationEgressNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utilizationEgressNow.setStatus("current")


class _UtilizationEgress30s_Type(Integer32):
    """Custom type utilizationEgress30s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UtilizationEgress30s_Type.__name__ = "Integer32"
_UtilizationEgress30s_Object = MibTableColumn
utilizationEgress30s = _UtilizationEgress30s_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 103, 1, 6),
    _UtilizationEgress30s_Type()
)
utilizationEgress30s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utilizationEgress30s.setStatus("current")


class _UtilizationEgress5min_Type(Integer32):
    """Custom type utilizationEgress5min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UtilizationEgress5min_Type.__name__ = "Integer32"
_UtilizationEgress5min_Object = MibTableColumn
utilizationEgress5min = _UtilizationEgress5min_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 85, 103, 1, 7),
    _UtilizationEgress5min_Type()
)
utilizationEgress5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utilizationEgress5min.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-RMON-MIB",
    **{"device": device,
       "rmon": rmon,
       "rmonClearAllCounter": rmonClearAllCounter,
       "ingressTable": ingressTable,
       "ingressEntry": ingressEntry,
       "ingressPortIndex": ingressPortIndex,
       "ingressEntryStatus": ingressEntryStatus,
       "ingressInGoodOctetsLo": ingressInGoodOctetsLo,
       "ingressInGoodOctetsHi": ingressInGoodOctetsHi,
       "ingressInBadOctets": ingressInBadOctets,
       "ingressInTotalPackets": ingressInTotalPackets,
       "ingressInUnicasts": ingressInUnicasts,
       "ingressInNonUnicasts": ingressInNonUnicasts,
       "ingressInBroadcasts": ingressInBroadcasts,
       "ingressInMulticasts": ingressInMulticasts,
       "ingressInPause": ingressInPause,
       "ingressInTotalReceiveErrors": ingressInTotalReceiveErrors,
       "ingressInUndersize": ingressInUndersize,
       "ingressInOversize": ingressInOversize,
       "ingressInFragments": ingressInFragments,
       "ingressInJabber": ingressInJabber,
       "ingressInFcsErrors": ingressInFcsErrors,
       "ingressInDiscarded": ingressInDiscarded,
       "egressTable": egressTable,
       "egressEntry": egressEntry,
       "egressPortIndex": egressPortIndex,
       "egressOutGoodOctetsLo": egressOutGoodOctetsLo,
       "egressOutGoodOctetsHi": egressOutGoodOctetsHi,
       "egressOutUnicasts": egressOutUnicasts,
       "egressOutNonUnicasts": egressOutNonUnicasts,
       "egressOutBroadcasts": egressOutBroadcasts,
       "egressOutMulticasts": egressOutMulticasts,
       "egressOutPause": egressOutPause,
       "egressOutDeferred": egressOutDeferred,
       "egressOutTotalCollisions": egressOutTotalCollisions,
       "egressOutSingleCollisions": egressOutSingleCollisions,
       "egressOutMultipleCollisions": egressOutMultipleCollisions,
       "egressOutExcessiveCollisions": egressOutExcessiveCollisions,
       "egressOutLateCollisions": egressOutLateCollisions,
       "egressOutFcsErrors": egressOutFcsErrors,
       "egressOutDroppedPackets": egressOutDroppedPackets,
       "histogramTable": histogramTable,
       "histogramEntry": histogramEntry,
       "histogramPortIndex": histogramPortIndex,
       "histogramIn64Octets": histogramIn64Octets,
       "histogramIn65To127Octets": histogramIn65To127Octets,
       "histogramIn128To255Octets": histogramIn128To255Octets,
       "histogramIn256To511Octets": histogramIn256To511Octets,
       "histogramIn512To1023Octets": histogramIn512To1023Octets,
       "histogramIn1024ToMaxOctets": histogramIn1024ToMaxOctets,
       "utilizationTable": utilizationTable,
       "utilizationEntry": utilizationEntry,
       "utilizationPortIndex": utilizationPortIndex,
       "utilizationIngressNow": utilizationIngressNow,
       "utilizationIngress30s": utilizationIngress30s,
       "utilizationIngress5min": utilizationIngress5min,
       "utilizationEgressNow": utilizationEgressNow,
       "utilizationEgress30s": utilizationEgress30s,
       "utilizationEgress5min": utilizationEgress5min}
)
