# SNMP MIB module (PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/PPP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:17:21 2025
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

(nnbundleId,) = mibBuilder.importSymbols(
    "BUNDLE-MIB",
    "nnbundleId")

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nnpppMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    nnpppMib.setRevisions(
        ("1900-02-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnpppTable_Object = MibTable
nnpppTable = _NnpppTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    nnpppTable.setStatus("current")
_NnpppTableEntry_Object = MibTableRow
nnpppTableEntry = _NnpppTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1)
)
nnpppTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
)
if mibBuilder.loadTexts:
    nnpppTableEntry.setStatus("current")


class _NnpppMtu_Type(DisplayString):
    """Custom type nnpppMtu based on DisplayString"""
    defaultValue = OctetString("64-1500-4096")


_NnpppMtu_Type.__name__ = "DisplayString"
_NnpppMtu_Object = MibTableColumn
nnpppMtu = _NnpppMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 1),
    _NnpppMtu_Type()
)
nnpppMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnpppMtu.setStatus("current")


class _NnpppMru_Type(DisplayString):
    """Custom type nnpppMru based on DisplayString"""
    defaultValue = OctetString("46-1500-4096")


_NnpppMru_Type.__name__ = "DisplayString"
_NnpppMru_Object = MibTableColumn
nnpppMru = _NnpppMru_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 2),
    _NnpppMru_Type()
)
nnpppMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnpppMru.setStatus("current")


class _NnmlpppMrru_Type(DisplayString):
    """Custom type nnmlpppMrru based on DisplayString"""
    defaultValue = OctetString("1500-1524-8192")


_NnmlpppMrru_Type.__name__ = "DisplayString"
_NnmlpppMrru_Object = MibTableColumn
nnmlpppMrru = _NnmlpppMrru_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 3),
    _NnmlpppMrru_Type()
)
nnmlpppMrru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmlpppMrru.setStatus("current")


class _NnmlpppSeq_Type(Integer32):
    """Custom type nnmlpppSeq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("long", 2))
    )


_NnmlpppSeq_Type.__name__ = "Integer32"
_NnmlpppSeq_Object = MibTableColumn
nnmlpppSeq = _NnmlpppSeq_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 4),
    _NnmlpppSeq_Type()
)
nnmlpppSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmlpppSeq.setStatus("current")


class _NnmlpppSegmentThreshold_Type(Integer32):
    """Custom type nnmlpppSegmentThreshold based on Integer32"""
    defaultValue = 512


_NnmlpppSegmentThreshold_Type.__name__ = "Integer32"
_NnmlpppSegmentThreshold_Object = MibTableColumn
nnmlpppSegmentThreshold = _NnmlpppSegmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 5),
    _NnmlpppSegmentThreshold_Type()
)
nnmlpppSegmentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmlpppSegmentThreshold.setStatus("current")


class _NnmlpppDiffDelay_Type(Integer32):
    """Custom type nnmlpppDiffDelay based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_NnmlpppDiffDelay_Type.__name__ = "Integer32"
_NnmlpppDiffDelay_Object = MibTableColumn
nnmlpppDiffDelay = _NnmlpppDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 6),
    _NnmlpppDiffDelay_Type()
)
nnmlpppDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmlpppDiffDelay.setStatus("current")
_NnmlpppDiscriminator_Type = DisplayString
_NnmlpppDiscriminator_Object = MibTableColumn
nnmlpppDiscriminator = _NnmlpppDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 7),
    _NnmlpppDiscriminator_Type()
)
nnmlpppDiscriminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmlpppDiscriminator.setStatus("current")
_NnpppNegotiatePeerIpAddr_Type = IpAddress
_NnpppNegotiatePeerIpAddr_Object = MibTableColumn
nnpppNegotiatePeerIpAddr = _NnpppNegotiatePeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 8),
    _NnpppNegotiatePeerIpAddr_Type()
)
nnpppNegotiatePeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnpppNegotiatePeerIpAddr.setStatus("current")
_NnpppSrcIpAddr_Type = IpAddress
_NnpppSrcIpAddr_Object = MibTableColumn
nnpppSrcIpAddr = _NnpppSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 9),
    _NnpppSrcIpAddr_Type()
)
nnpppSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnpppSrcIpAddr.setStatus("current")
_NnpppPeerIpAddr_Type = IpAddress
_NnpppPeerIpAddr_Object = MibTableColumn
nnpppPeerIpAddr = _NnpppPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 1, 1, 10),
    _NnpppPeerIpAddr_Type()
)
nnpppPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppPeerIpAddr.setStatus("current")
_NnpppStatsTable_Object = MibTable
nnpppStatsTable = _NnpppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    nnpppStatsTable.setStatus("current")
_NnpppStatsTableEntry_Object = MibTableRow
nnpppStatsTableEntry = _NnpppStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1)
)
nnpppStatsTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
)
if mibBuilder.loadTexts:
    nnpppStatsTableEntry.setStatus("current")
_NnpppStatsBytesRxLastBootOrClear_Type = Counter32
_NnpppStatsBytesRxLastBootOrClear_Object = MibTableColumn
nnpppStatsBytesRxLastBootOrClear = _NnpppStatsBytesRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 1),
    _NnpppStatsBytesRxLastBootOrClear_Type()
)
nnpppStatsBytesRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsBytesRxLastBootOrClear.setStatus("current")
_NnpppStatsBytesTxLastBootOrClear_Type = Counter32
_NnpppStatsBytesTxLastBootOrClear_Object = MibTableColumn
nnpppStatsBytesTxLastBootOrClear = _NnpppStatsBytesTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 2),
    _NnpppStatsBytesTxLastBootOrClear_Type()
)
nnpppStatsBytesTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsBytesTxLastBootOrClear.setStatus("current")
_NnpppStatsPktsRxLastBootOrClear_Type = Counter32
_NnpppStatsPktsRxLastBootOrClear_Object = MibTableColumn
nnpppStatsPktsRxLastBootOrClear = _NnpppStatsPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 3),
    _NnpppStatsPktsRxLastBootOrClear_Type()
)
nnpppStatsPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsPktsRxLastBootOrClear.setStatus("current")
_NnpppStatsPktsTxLastBootOrClear_Type = Counter32
_NnpppStatsPktsTxLastBootOrClear_Object = MibTableColumn
nnpppStatsPktsTxLastBootOrClear = _NnpppStatsPktsTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 4),
    _NnpppStatsPktsTxLastBootOrClear_Type()
)
nnpppStatsPktsTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsPktsTxLastBootOrClear.setStatus("current")
_NnpppStatsErrPktsRxLastBootOrClear_Type = Counter32
_NnpppStatsErrPktsRxLastBootOrClear_Object = MibTableColumn
nnpppStatsErrPktsRxLastBootOrClear = _NnpppStatsErrPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 5),
    _NnpppStatsErrPktsRxLastBootOrClear_Type()
)
nnpppStatsErrPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsErrPktsRxLastBootOrClear.setStatus("current")
_NnpppStatsUpDownStatesLastBootOrClear_Type = Counter32
_NnpppStatsUpDownStatesLastBootOrClear_Object = MibTableColumn
nnpppStatsUpDownStatesLastBootOrClear = _NnpppStatsUpDownStatesLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 6),
    _NnpppStatsUpDownStatesLastBootOrClear_Type()
)
nnpppStatsUpDownStatesLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsUpDownStatesLastBootOrClear.setStatus("current")
_NnpppStatsBytesRxLastFiveMins_Type = Counter32
_NnpppStatsBytesRxLastFiveMins_Object = MibTableColumn
nnpppStatsBytesRxLastFiveMins = _NnpppStatsBytesRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 7),
    _NnpppStatsBytesRxLastFiveMins_Type()
)
nnpppStatsBytesRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsBytesRxLastFiveMins.setStatus("current")
_NnpppStatsBytesTxLastFiveMins_Type = Counter32
_NnpppStatsBytesTxLastFiveMins_Object = MibTableColumn
nnpppStatsBytesTxLastFiveMins = _NnpppStatsBytesTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 8),
    _NnpppStatsBytesTxLastFiveMins_Type()
)
nnpppStatsBytesTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsBytesTxLastFiveMins.setStatus("current")
_NnpppStatsPktsRxLastFiveMins_Type = Counter32
_NnpppStatsPktsRxLastFiveMins_Object = MibTableColumn
nnpppStatsPktsRxLastFiveMins = _NnpppStatsPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 9),
    _NnpppStatsPktsRxLastFiveMins_Type()
)
nnpppStatsPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsPktsRxLastFiveMins.setStatus("current")
_NnpppStatsPktsTxLastFiveMins_Type = Counter32
_NnpppStatsPktsTxLastFiveMins_Object = MibTableColumn
nnpppStatsPktsTxLastFiveMins = _NnpppStatsPktsTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 10),
    _NnpppStatsPktsTxLastFiveMins_Type()
)
nnpppStatsPktsTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsPktsTxLastFiveMins.setStatus("current")
_NnpppStatsErrPktsRxLastFiveMins_Type = Counter32
_NnpppStatsErrPktsRxLastFiveMins_Object = MibTableColumn
nnpppStatsErrPktsRxLastFiveMins = _NnpppStatsErrPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 11),
    _NnpppStatsErrPktsRxLastFiveMins_Type()
)
nnpppStatsErrPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsErrPktsRxLastFiveMins.setStatus("current")
_NnpppStatsUpDownStatesLastFiveMins_Type = Counter32
_NnpppStatsUpDownStatesLastFiveMins_Object = MibTableColumn
nnpppStatsUpDownStatesLastFiveMins = _NnpppStatsUpDownStatesLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 14, 2, 1, 12),
    _NnpppStatsUpDownStatesLastFiveMins_Type()
)
nnpppStatsUpDownStatesLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnpppStatsUpDownStatesLastFiveMins.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PPP-MIB",
    **{"nnpppMib": nnpppMib,
       "nnpppTable": nnpppTable,
       "nnpppTableEntry": nnpppTableEntry,
       "nnpppMtu": nnpppMtu,
       "nnpppMru": nnpppMru,
       "nnmlpppMrru": nnmlpppMrru,
       "nnmlpppSeq": nnmlpppSeq,
       "nnmlpppSegmentThreshold": nnmlpppSegmentThreshold,
       "nnmlpppDiffDelay": nnmlpppDiffDelay,
       "nnmlpppDiscriminator": nnmlpppDiscriminator,
       "nnpppNegotiatePeerIpAddr": nnpppNegotiatePeerIpAddr,
       "nnpppSrcIpAddr": nnpppSrcIpAddr,
       "nnpppPeerIpAddr": nnpppPeerIpAddr,
       "nnpppStatsTable": nnpppStatsTable,
       "nnpppStatsTableEntry": nnpppStatsTableEntry,
       "nnpppStatsBytesRxLastBootOrClear": nnpppStatsBytesRxLastBootOrClear,
       "nnpppStatsBytesTxLastBootOrClear": nnpppStatsBytesTxLastBootOrClear,
       "nnpppStatsPktsRxLastBootOrClear": nnpppStatsPktsRxLastBootOrClear,
       "nnpppStatsPktsTxLastBootOrClear": nnpppStatsPktsTxLastBootOrClear,
       "nnpppStatsErrPktsRxLastBootOrClear": nnpppStatsErrPktsRxLastBootOrClear,
       "nnpppStatsUpDownStatesLastBootOrClear": nnpppStatsUpDownStatesLastBootOrClear,
       "nnpppStatsBytesRxLastFiveMins": nnpppStatsBytesRxLastFiveMins,
       "nnpppStatsBytesTxLastFiveMins": nnpppStatsBytesTxLastFiveMins,
       "nnpppStatsPktsRxLastFiveMins": nnpppStatsPktsRxLastFiveMins,
       "nnpppStatsPktsTxLastFiveMins": nnpppStatsPktsTxLastFiveMins,
       "nnpppStatsErrPktsRxLastFiveMins": nnpppStatsErrPktsRxLastFiveMins,
       "nnpppStatsUpDownStatesLastFiveMins": nnpppStatsUpDownStatesLastFiveMins}
)
