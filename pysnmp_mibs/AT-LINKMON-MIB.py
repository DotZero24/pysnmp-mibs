# SNMP MIB module (AT-LINKMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied/AT-LINKMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:23:52 2025
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(InetVersion,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetVersion")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atLinkMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606)
)
if mibBuilder.loadTexts:
    atLinkMon.setRevisions(
        ("2020-09-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AtLinkMonType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("http", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AtLinkMonProbeTable_Object = MibTable
atLinkMonProbeTable = _AtLinkMonProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1)
)
if mibBuilder.loadTexts:
    atLinkMonProbeTable.setStatus("current")
_AtLinkMonProbeEntry_Object = MibTableRow
atLinkMonProbeEntry = _AtLinkMonProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1)
)
atLinkMonProbeEntry.setIndexNames(
    (0, "AT-LINKMON-MIB", "atLinkMonProbeID"),
)
if mibBuilder.loadTexts:
    atLinkMonProbeEntry.setStatus("current")
_AtLinkMonProbeID_Type = Unsigned32
_AtLinkMonProbeID_Object = MibTableColumn
atLinkMonProbeID = _AtLinkMonProbeID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 1),
    _AtLinkMonProbeID_Type()
)
atLinkMonProbeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atLinkMonProbeID.setStatus("current")
_AtLinkMonProbeName_Type = DisplayStringUnsized
_AtLinkMonProbeName_Object = MibTableColumn
atLinkMonProbeName = _AtLinkMonProbeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 2),
    _AtLinkMonProbeName_Type()
)
atLinkMonProbeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeName.setStatus("current")
_AtLinkMonProbeType_Type = AtLinkMonType
_AtLinkMonProbeType_Object = MibTableColumn
atLinkMonProbeType = _AtLinkMonProbeType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 3),
    _AtLinkMonProbeType_Type()
)
atLinkMonProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeType.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonProbeType.setUnits("ICMP: 1, HTTP: 2")
_AtLinkMonProbeIPVersion_Type = InetVersion
_AtLinkMonProbeIPVersion_Object = MibTableColumn
atLinkMonProbeIPVersion = _AtLinkMonProbeIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 4),
    _AtLinkMonProbeIPVersion_Type()
)
atLinkMonProbeIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeIPVersion.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonProbeIPVersion.setUnits("IPv4: 1, IPv6: 2")
_AtLinkMonProbeDestination_Type = DisplayStringUnsized
_AtLinkMonProbeDestination_Object = MibTableColumn
atLinkMonProbeDestination = _AtLinkMonProbeDestination_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 5),
    _AtLinkMonProbeDestination_Type()
)
atLinkMonProbeDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeDestination.setStatus("current")
_AtLinkMonProbeEgressIf_Type = DisplayStringUnsized
_AtLinkMonProbeEgressIf_Object = MibTableColumn
atLinkMonProbeEgressIf = _AtLinkMonProbeEgressIf_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 6),
    _AtLinkMonProbeEgressIf_Type()
)
atLinkMonProbeEgressIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeEgressIf.setStatus("current")
_AtLinkmonProbeEgreesIfValid_Type = TruthValue
_AtLinkmonProbeEgreesIfValid_Object = MibTableColumn
atLinkmonProbeEgreesIfValid = _AtLinkmonProbeEgreesIfValid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 7),
    _AtLinkmonProbeEgreesIfValid_Type()
)
atLinkmonProbeEgreesIfValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkmonProbeEgreesIfValid.setStatus("current")
_AtLinkMonProbeSource_Type = DisplayStringUnsized
_AtLinkMonProbeSource_Object = MibTableColumn
atLinkMonProbeSource = _AtLinkMonProbeSource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 8),
    _AtLinkMonProbeSource_Type()
)
atLinkMonProbeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeSource.setStatus("current")
_AtLinkMonProbeSourceValid_Type = TruthValue
_AtLinkMonProbeSourceValid_Object = MibTableColumn
atLinkMonProbeSourceValid = _AtLinkMonProbeSourceValid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 9),
    _AtLinkMonProbeSourceValid_Type()
)
atLinkMonProbeSourceValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeSourceValid.setStatus("current")


class _AtLinkMonProbeDSCP_Type(Unsigned32):
    """Custom type atLinkMonProbeDSCP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AtLinkMonProbeDSCP_Type.__name__ = "Unsigned32"
_AtLinkMonProbeDSCP_Object = MibTableColumn
atLinkMonProbeDSCP = _AtLinkMonProbeDSCP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 10),
    _AtLinkMonProbeDSCP_Type()
)
atLinkMonProbeDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeDSCP.setStatus("current")


class _AtLinkMonProbePacketSize_Type(Unsigned32):
    """Custom type atLinkMonProbePacketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_AtLinkMonProbePacketSize_Type.__name__ = "Unsigned32"
_AtLinkMonProbePacketSize_Object = MibTableColumn
atLinkMonProbePacketSize = _AtLinkMonProbePacketSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 11),
    _AtLinkMonProbePacketSize_Type()
)
atLinkMonProbePacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbePacketSize.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonProbePacketSize.setUnits("bytes")


class _AtLinkMonProbeInterval_Type(Unsigned32):
    """Custom type atLinkMonProbeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3600000),
    )


_AtLinkMonProbeInterval_Type.__name__ = "Unsigned32"
_AtLinkMonProbeInterval_Object = MibTableColumn
atLinkMonProbeInterval = _AtLinkMonProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 12),
    _AtLinkMonProbeInterval_Type()
)
atLinkMonProbeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonProbeInterval.setUnits("ms")


class _AtLinkMonProbeSampleSize_Type(Unsigned32):
    """Custom type atLinkMonProbeSampleSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtLinkMonProbeSampleSize_Type.__name__ = "Unsigned32"
_AtLinkMonProbeSampleSize_Object = MibTableColumn
atLinkMonProbeSampleSize = _AtLinkMonProbeSampleSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 13),
    _AtLinkMonProbeSampleSize_Type()
)
atLinkMonProbeSampleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeSampleSize.setStatus("current")
_AtLinkMonProbeEnabled_Type = TruthValue
_AtLinkMonProbeEnabled_Object = MibTableColumn
atLinkMonProbeEnabled = _AtLinkMonProbeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 1, 1, 14),
    _AtLinkMonProbeEnabled_Type()
)
atLinkMonProbeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeEnabled.setStatus("current")
_AtLinkMonProbeDetailTable_Object = MibTable
atLinkMonProbeDetailTable = _AtLinkMonProbeDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 2)
)
if mibBuilder.loadTexts:
    atLinkMonProbeDetailTable.setStatus("current")
_AtLinkMonProbeDetailEntry_Object = MibTableRow
atLinkMonProbeDetailEntry = _AtLinkMonProbeDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 2, 1)
)
atLinkMonProbeDetailEntry.setIndexNames(
    (0, "AT-LINKMON-MIB", "atLinkMonProbeID"),
)
if mibBuilder.loadTexts:
    atLinkMonProbeDetailEntry.setStatus("current")
_AtLinkMonProbeDetailProbesSent_Type = Counter64
_AtLinkMonProbeDetailProbesSent_Object = MibTableColumn
atLinkMonProbeDetailProbesSent = _AtLinkMonProbeDetailProbesSent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 2, 1, 1),
    _AtLinkMonProbeDetailProbesSent_Type()
)
atLinkMonProbeDetailProbesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeDetailProbesSent.setStatus("current")
_AtLinkMonProbeDetailLastTxTime_Type = DisplayStringUnsized
_AtLinkMonProbeDetailLastTxTime_Object = MibTableColumn
atLinkMonProbeDetailLastTxTime = _AtLinkMonProbeDetailLastTxTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 2, 1, 2),
    _AtLinkMonProbeDetailLastTxTime_Type()
)
atLinkMonProbeDetailLastTxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeDetailLastTxTime.setStatus("current")
_AtLinkMonProbeDetailLastRxTime_Type = DisplayStringUnsized
_AtLinkMonProbeDetailLastRxTime_Object = MibTableColumn
atLinkMonProbeDetailLastRxTime = _AtLinkMonProbeDetailLastRxTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 2, 1, 3),
    _AtLinkMonProbeDetailLastRxTime_Type()
)
atLinkMonProbeDetailLastRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeDetailLastRxTime.setStatus("current")
_AtLinkMonProbeLatestMetricsTable_Object = MibTable
atLinkMonProbeLatestMetricsTable = _AtLinkMonProbeLatestMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 3)
)
if mibBuilder.loadTexts:
    atLinkMonProbeLatestMetricsTable.setStatus("current")
_AtLinkMonProbeLatestMetricsEntry_Object = MibTableRow
atLinkMonProbeLatestMetricsEntry = _AtLinkMonProbeLatestMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 3, 1)
)
atLinkMonProbeLatestMetricsEntry.setIndexNames(
    (0, "AT-LINKMON-MIB", "atLinkMonProbeID"),
)
if mibBuilder.loadTexts:
    atLinkMonProbeLatestMetricsEntry.setStatus("current")
_AtLinkMonProbeLatestMetricsLatency_Type = Unsigned32
_AtLinkMonProbeLatestMetricsLatency_Object = MibTableColumn
atLinkMonProbeLatestMetricsLatency = _AtLinkMonProbeLatestMetricsLatency_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 3, 1, 1),
    _AtLinkMonProbeLatestMetricsLatency_Type()
)
atLinkMonProbeLatestMetricsLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeLatestMetricsLatency.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonProbeLatestMetricsLatency.setUnits("ms")
_AtLinkMonProbeLatestMetricsJitter_Type = Unsigned32
_AtLinkMonProbeLatestMetricsJitter_Object = MibTableColumn
atLinkMonProbeLatestMetricsJitter = _AtLinkMonProbeLatestMetricsJitter_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 3, 1, 2),
    _AtLinkMonProbeLatestMetricsJitter_Type()
)
atLinkMonProbeLatestMetricsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeLatestMetricsJitter.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonProbeLatestMetricsJitter.setUnits("ms")


class _AtLinkMonProbeLatestMetricsPktLoss_Type(Unsigned32):
    """Custom type atLinkMonProbeLatestMetricsPktLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AtLinkMonProbeLatestMetricsPktLoss_Type.__name__ = "Unsigned32"
_AtLinkMonProbeLatestMetricsPktLoss_Object = MibTableColumn
atLinkMonProbeLatestMetricsPktLoss = _AtLinkMonProbeLatestMetricsPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 3, 1, 3),
    _AtLinkMonProbeLatestMetricsPktLoss_Type()
)
atLinkMonProbeLatestMetricsPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeLatestMetricsPktLoss.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonProbeLatestMetricsPktLoss.setUnits("1/10%")
_AtLinkMonProbeLatestMetricsCnscPktLoss_Type = Integer32
_AtLinkMonProbeLatestMetricsCnscPktLoss_Object = MibTableColumn
atLinkMonProbeLatestMetricsCnscPktLoss = _AtLinkMonProbeLatestMetricsCnscPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 3, 1, 4),
    _AtLinkMonProbeLatestMetricsCnscPktLoss_Type()
)
atLinkMonProbeLatestMetricsCnscPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeLatestMetricsCnscPktLoss.setStatus("current")
_AtLinkMonProbeHistoryTable_Object = MibTable
atLinkMonProbeHistoryTable = _AtLinkMonProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 4)
)
if mibBuilder.loadTexts:
    atLinkMonProbeHistoryTable.setStatus("current")
_AtLinkMonProbeHistoryEntry_Object = MibTableRow
atLinkMonProbeHistoryEntry = _AtLinkMonProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 4, 1)
)
atLinkMonProbeHistoryEntry.setIndexNames(
    (0, "AT-LINKMON-MIB", "atLinkMonProbeHistoryID"),
)
if mibBuilder.loadTexts:
    atLinkMonProbeHistoryEntry.setStatus("current")


class _AtLinkMonProbeHistoryID_Type(Unsigned32):
    """Custom type atLinkMonProbeHistoryID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtLinkMonProbeHistoryID_Type.__name__ = "Unsigned32"
_AtLinkMonProbeHistoryID_Object = MibTableColumn
atLinkMonProbeHistoryID = _AtLinkMonProbeHistoryID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 4, 1, 1),
    _AtLinkMonProbeHistoryID_Type()
)
atLinkMonProbeHistoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeHistoryID.setStatus("current")
_AtLinkMonProbeHistoryProbeName_Type = DisplayStringUnsized
_AtLinkMonProbeHistoryProbeName_Object = MibTableColumn
atLinkMonProbeHistoryProbeName = _AtLinkMonProbeHistoryProbeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 4, 1, 2),
    _AtLinkMonProbeHistoryProbeName_Type()
)
atLinkMonProbeHistoryProbeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeHistoryProbeName.setStatus("current")


class _AtLinkMonProbeHistoryInterval_Type(Unsigned32):
    """Custom type atLinkMonProbeHistoryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2678400),
    )


_AtLinkMonProbeHistoryInterval_Type.__name__ = "Unsigned32"
_AtLinkMonProbeHistoryInterval_Object = MibTableColumn
atLinkMonProbeHistoryInterval = _AtLinkMonProbeHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 4, 1, 3),
    _AtLinkMonProbeHistoryInterval_Type()
)
atLinkMonProbeHistoryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeHistoryInterval.setStatus("current")


class _AtLinkMonProbeHistoryBuckets_Type(Unsigned32):
    """Custom type atLinkMonProbeHistoryBuckets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtLinkMonProbeHistoryBuckets_Type.__name__ = "Unsigned32"
_AtLinkMonProbeHistoryBuckets_Object = MibTableColumn
atLinkMonProbeHistoryBuckets = _AtLinkMonProbeHistoryBuckets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 4, 1, 4),
    _AtLinkMonProbeHistoryBuckets_Type()
)
atLinkMonProbeHistoryBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeHistoryBuckets.setStatus("current")
_AtLinkMonProbeHistoryLastSmplID_Type = Unsigned32
_AtLinkMonProbeHistoryLastSmplID_Object = MibTableColumn
atLinkMonProbeHistoryLastSmplID = _AtLinkMonProbeHistoryLastSmplID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 4, 1, 5),
    _AtLinkMonProbeHistoryLastSmplID_Type()
)
atLinkMonProbeHistoryLastSmplID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeHistoryLastSmplID.setStatus("current")
_AtLinkMonProbeHistoryLastSmplTime_Type = DisplayStringUnsized
_AtLinkMonProbeHistoryLastSmplTime_Object = MibTableColumn
atLinkMonProbeHistoryLastSmplTime = _AtLinkMonProbeHistoryLastSmplTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 4, 1, 6),
    _AtLinkMonProbeHistoryLastSmplTime_Type()
)
atLinkMonProbeHistoryLastSmplTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonProbeHistoryLastSmplTime.setStatus("current")
_AtLinkMonSampleTable_Object = MibTable
atLinkMonSampleTable = _AtLinkMonSampleTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5)
)
if mibBuilder.loadTexts:
    atLinkMonSampleTable.setStatus("current")
_AtLinkMonSampleEntry_Object = MibTableRow
atLinkMonSampleEntry = _AtLinkMonSampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5, 1)
)
atLinkMonSampleEntry.setIndexNames(
    (0, "AT-LINKMON-MIB", "atLinkMonProbeHistoryID"),
    (0, "AT-LINKMON-MIB", "atLinkMonSampleBucket"),
)
if mibBuilder.loadTexts:
    atLinkMonSampleEntry.setStatus("current")
_AtLinkMonSampleBucket_Type = Unsigned32
_AtLinkMonSampleBucket_Object = MibTableColumn
atLinkMonSampleBucket = _AtLinkMonSampleBucket_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5, 1, 1),
    _AtLinkMonSampleBucket_Type()
)
atLinkMonSampleBucket.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atLinkMonSampleBucket.setStatus("current")
_AtLinkMonSampleLatencySum_Type = Unsigned32
_AtLinkMonSampleLatencySum_Object = MibTableColumn
atLinkMonSampleLatencySum = _AtLinkMonSampleLatencySum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5, 1, 2),
    _AtLinkMonSampleLatencySum_Type()
)
atLinkMonSampleLatencySum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonSampleLatencySum.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonSampleLatencySum.setUnits("ms")
_AtLinkMonSampleLatencyCount_Type = Unsigned32
_AtLinkMonSampleLatencyCount_Object = MibTableColumn
atLinkMonSampleLatencyCount = _AtLinkMonSampleLatencyCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5, 1, 3),
    _AtLinkMonSampleLatencyCount_Type()
)
atLinkMonSampleLatencyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonSampleLatencyCount.setStatus("current")
_AtLinkMonSampleJitterSum_Type = Unsigned32
_AtLinkMonSampleJitterSum_Object = MibTableColumn
atLinkMonSampleJitterSum = _AtLinkMonSampleJitterSum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5, 1, 4),
    _AtLinkMonSampleJitterSum_Type()
)
atLinkMonSampleJitterSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonSampleJitterSum.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonSampleJitterSum.setUnits("ms")
_AtLinkMonSampleJitterCount_Type = Unsigned32
_AtLinkMonSampleJitterCount_Object = MibTableColumn
atLinkMonSampleJitterCount = _AtLinkMonSampleJitterCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5, 1, 5),
    _AtLinkMonSampleJitterCount_Type()
)
atLinkMonSampleJitterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonSampleJitterCount.setStatus("current")
_AtLinkMonSamplePktLossSum_Type = Unsigned32
_AtLinkMonSamplePktLossSum_Object = MibTableColumn
atLinkMonSamplePktLossSum = _AtLinkMonSamplePktLossSum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5, 1, 6),
    _AtLinkMonSamplePktLossSum_Type()
)
atLinkMonSamplePktLossSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonSamplePktLossSum.setStatus("current")
if mibBuilder.loadTexts:
    atLinkMonSamplePktLossSum.setUnits("1/10%")
_AtLinkMonSamplePktsTx_Type = Unsigned32
_AtLinkMonSamplePktsTx_Object = MibTableColumn
atLinkMonSamplePktsTx = _AtLinkMonSamplePktsTx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5, 1, 7),
    _AtLinkMonSamplePktsTx_Type()
)
atLinkMonSamplePktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonSamplePktsTx.setStatus("current")
_AtLinkMonSamplePktsRx_Type = Unsigned32
_AtLinkMonSamplePktsRx_Object = MibTableColumn
atLinkMonSamplePktsRx = _AtLinkMonSamplePktsRx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 606, 5, 1, 8),
    _AtLinkMonSamplePktsRx_Type()
)
atLinkMonSamplePktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLinkMonSamplePktsRx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-LINKMON-MIB",
    **{"AtLinkMonType": AtLinkMonType,
       "atLinkMon": atLinkMon,
       "atLinkMonProbeTable": atLinkMonProbeTable,
       "atLinkMonProbeEntry": atLinkMonProbeEntry,
       "atLinkMonProbeID": atLinkMonProbeID,
       "atLinkMonProbeName": atLinkMonProbeName,
       "atLinkMonProbeType": atLinkMonProbeType,
       "atLinkMonProbeIPVersion": atLinkMonProbeIPVersion,
       "atLinkMonProbeDestination": atLinkMonProbeDestination,
       "atLinkMonProbeEgressIf": atLinkMonProbeEgressIf,
       "atLinkmonProbeEgreesIfValid": atLinkmonProbeEgreesIfValid,
       "atLinkMonProbeSource": atLinkMonProbeSource,
       "atLinkMonProbeSourceValid": atLinkMonProbeSourceValid,
       "atLinkMonProbeDSCP": atLinkMonProbeDSCP,
       "atLinkMonProbePacketSize": atLinkMonProbePacketSize,
       "atLinkMonProbeInterval": atLinkMonProbeInterval,
       "atLinkMonProbeSampleSize": atLinkMonProbeSampleSize,
       "atLinkMonProbeEnabled": atLinkMonProbeEnabled,
       "atLinkMonProbeDetailTable": atLinkMonProbeDetailTable,
       "atLinkMonProbeDetailEntry": atLinkMonProbeDetailEntry,
       "atLinkMonProbeDetailProbesSent": atLinkMonProbeDetailProbesSent,
       "atLinkMonProbeDetailLastTxTime": atLinkMonProbeDetailLastTxTime,
       "atLinkMonProbeDetailLastRxTime": atLinkMonProbeDetailLastRxTime,
       "atLinkMonProbeLatestMetricsTable": atLinkMonProbeLatestMetricsTable,
       "atLinkMonProbeLatestMetricsEntry": atLinkMonProbeLatestMetricsEntry,
       "atLinkMonProbeLatestMetricsLatency": atLinkMonProbeLatestMetricsLatency,
       "atLinkMonProbeLatestMetricsJitter": atLinkMonProbeLatestMetricsJitter,
       "atLinkMonProbeLatestMetricsPktLoss": atLinkMonProbeLatestMetricsPktLoss,
       "atLinkMonProbeLatestMetricsCnscPktLoss": atLinkMonProbeLatestMetricsCnscPktLoss,
       "atLinkMonProbeHistoryTable": atLinkMonProbeHistoryTable,
       "atLinkMonProbeHistoryEntry": atLinkMonProbeHistoryEntry,
       "atLinkMonProbeHistoryID": atLinkMonProbeHistoryID,
       "atLinkMonProbeHistoryProbeName": atLinkMonProbeHistoryProbeName,
       "atLinkMonProbeHistoryInterval": atLinkMonProbeHistoryInterval,
       "atLinkMonProbeHistoryBuckets": atLinkMonProbeHistoryBuckets,
       "atLinkMonProbeHistoryLastSmplID": atLinkMonProbeHistoryLastSmplID,
       "atLinkMonProbeHistoryLastSmplTime": atLinkMonProbeHistoryLastSmplTime,
       "atLinkMonSampleTable": atLinkMonSampleTable,
       "atLinkMonSampleEntry": atLinkMonSampleEntry,
       "atLinkMonSampleBucket": atLinkMonSampleBucket,
       "atLinkMonSampleLatencySum": atLinkMonSampleLatencySum,
       "atLinkMonSampleLatencyCount": atLinkMonSampleLatencyCount,
       "atLinkMonSampleJitterSum": atLinkMonSampleJitterSum,
       "atLinkMonSampleJitterCount": atLinkMonSampleJitterCount,
       "atLinkMonSamplePktLossSum": atLinkMonSamplePktLossSum,
       "atLinkMonSamplePktsTx": atLinkMonSamplePktsTx,
       "atLinkMonSamplePktsRx": atLinkMonSamplePktsRx}
)
