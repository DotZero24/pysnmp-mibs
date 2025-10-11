# SNMP MIB module (ARICENT-HB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-HB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:49 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsHb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93)
)
if mibBuilder.loadTexts:
    fsHb.setRevisions(
        ("2014-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsHbScalar_ObjectIdentity = ObjectIdentity
fsHbScalar = _FsHbScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 0)
)


class _FsHbInterval_Type(Unsigned32):
    """Custom type fsHbInterval based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 5000),
    )


_FsHbInterval_Type.__name__ = "Unsigned32"
_FsHbInterval_Object = MibScalar
fsHbInterval = _FsHbInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 0, 1),
    _FsHbInterval_Type()
)
fsHbInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHbInterval.setStatus("current")


class _FsHbPeerDeadIntMultiplier_Type(Unsigned32):
    """Custom type fsHbPeerDeadIntMultiplier based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 10),
    )


_FsHbPeerDeadIntMultiplier_Type.__name__ = "Unsigned32"
_FsHbPeerDeadIntMultiplier_Object = MibScalar
fsHbPeerDeadIntMultiplier = _FsHbPeerDeadIntMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 0, 2),
    _FsHbPeerDeadIntMultiplier_Type()
)
fsHbPeerDeadIntMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHbPeerDeadIntMultiplier.setStatus("current")


class _FsHbTrcLevel_Type(Unsigned32):
    """Custom type fsHbTrcLevel based on Unsigned32"""
    defaultValue = 0


_FsHbTrcLevel_Type.__name__ = "Unsigned32"
_FsHbTrcLevel_Object = MibScalar
fsHbTrcLevel = _FsHbTrcLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 0, 3),
    _FsHbTrcLevel_Type()
)
fsHbTrcLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHbTrcLevel.setStatus("current")


class _FsHbStatsEnable_Type(Integer32):
    """Custom type fsHbStatsEnable based on Integer32"""
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


_FsHbStatsEnable_Type.__name__ = "Integer32"
_FsHbStatsEnable_Object = MibScalar
fsHbStatsEnable = _FsHbStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 0, 4),
    _FsHbStatsEnable_Type()
)
fsHbStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHbStatsEnable.setStatus("current")


class _FsHbClearStats_Type(TruthValue):
    """Custom type fsHbClearStats based on TruthValue"""
    defaultValue = 2


_FsHbClearStats_Type.__name__ = "TruthValue"
_FsHbClearStats_Object = MibScalar
fsHbClearStats = _FsHbClearStats_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 0, 5),
    _FsHbClearStats_Type()
)
fsHbClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHbClearStats.setStatus("current")
_FsHbStatistics_ObjectIdentity = ObjectIdentity
fsHbStatistics = _FsHbStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 1)
)
_FsHbStatsMsgTxCount_Type = ZeroBasedCounter32
_FsHbStatsMsgTxCount_Object = MibScalar
fsHbStatsMsgTxCount = _FsHbStatsMsgTxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 1, 1),
    _FsHbStatsMsgTxCount_Type()
)
fsHbStatsMsgTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHbStatsMsgTxCount.setStatus("current")
_FsHbStatsMsgTxFailedCount_Type = ZeroBasedCounter32
_FsHbStatsMsgTxFailedCount_Object = MibScalar
fsHbStatsMsgTxFailedCount = _FsHbStatsMsgTxFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 1, 2),
    _FsHbStatsMsgTxFailedCount_Type()
)
fsHbStatsMsgTxFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHbStatsMsgTxFailedCount.setStatus("current")
_FsHbStatsMsgRxCount_Type = ZeroBasedCounter32
_FsHbStatsMsgRxCount_Object = MibScalar
fsHbStatsMsgRxCount = _FsHbStatsMsgRxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 1, 3),
    _FsHbStatsMsgRxCount_Type()
)
fsHbStatsMsgRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHbStatsMsgRxCount.setStatus("current")
_FsHbStatsMsgRxProcCount_Type = ZeroBasedCounter32
_FsHbStatsMsgRxProcCount_Object = MibScalar
fsHbStatsMsgRxProcCount = _FsHbStatsMsgRxProcCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 1, 4),
    _FsHbStatsMsgRxProcCount_Type()
)
fsHbStatsMsgRxProcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHbStatsMsgRxProcCount.setStatus("current")
_FsHbStatsRxFailedCount_Type = ZeroBasedCounter32
_FsHbStatsRxFailedCount_Object = MibScalar
fsHbStatsRxFailedCount = _FsHbStatsRxFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 93, 1, 5),
    _FsHbStatsRxFailedCount_Type()
)
fsHbStatsRxFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHbStatsRxFailedCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-HB-MIB",
    **{"fsHb": fsHb,
       "fsHbScalar": fsHbScalar,
       "fsHbInterval": fsHbInterval,
       "fsHbPeerDeadIntMultiplier": fsHbPeerDeadIntMultiplier,
       "fsHbTrcLevel": fsHbTrcLevel,
       "fsHbStatsEnable": fsHbStatsEnable,
       "fsHbClearStats": fsHbClearStats,
       "fsHbStatistics": fsHbStatistics,
       "fsHbStatsMsgTxCount": fsHbStatsMsgTxCount,
       "fsHbStatsMsgTxFailedCount": fsHbStatsMsgTxFailedCount,
       "fsHbStatsMsgRxCount": fsHbStatsMsgRxCount,
       "fsHbStatsMsgRxProcCount": fsHbStatsMsgRxProcCount,
       "fsHbStatsRxFailedCount": fsHbStatsRxFailedCount}
)
