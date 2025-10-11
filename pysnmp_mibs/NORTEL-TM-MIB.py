# SNMP MIB module (NORTEL-TM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-TM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:58 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(nortelGenericMIBs,) = mibBuilder.importSymbols(
    "NORTEL-GENERIC-MIB",
    "nortelGenericMIBs")

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

nnTMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 3)
)
if mibBuilder.loadTexts:
    nnTMMIB.setRevisions(
        ("2005-11-15 15:22",
         "2008-07-30 10:12")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NnTMClassOfService(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              15)
        )
    )
    namedValues = NamedValues(
        *(("cosStandard", 0),
          ("cosBronze", 1),
          ("cosSilver", 2),
          ("cosGold", 3),
          ("cosPlatinum", 4),
          ("cosPremium", 5),
          ("cosNetworkNT", 6),
          ("cosCritical", 7),
          ("cosNetworkNW", 8),
          ("cosUnknown", 15))
    )



class NnTMQueueGroup(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eQGRPUNKNOWN", 0),
          ("eQGRPNA", 1),
          ("eQGRP1", 2),
          ("eQGRP2", 3))
    )



# MIB Managed Objects in the order of their OIDs

_NnTMObjects_ObjectIdentity = ObjectIdentity
nnTMObjects = _NnTMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1)
)
_NnTMStatsTable_Object = MibTable
nnTMStatsTable = _NnTMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nnTMStatsTable.setStatus("current")
_NnTMStatsEntry_Object = MibTableRow
nnTMStatsEntry = _NnTMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1)
)
nnTMStatsEntry.setIndexNames(
    (0, "NORTEL-TM-MIB", "trafficMgmtIfIndex"),
    (0, "NORTEL-TM-MIB", "queueGroupIndex"),
    (0, "NORTEL-TM-MIB", "cosIndex"),
)
if mibBuilder.loadTexts:
    nnTMStatsEntry.setStatus("current")
_TrafficMgmtIfIndex_Type = InterfaceIndex
_TrafficMgmtIfIndex_Object = MibTableColumn
trafficMgmtIfIndex = _TrafficMgmtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 1),
    _TrafficMgmtIfIndex_Type()
)
trafficMgmtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trafficMgmtIfIndex.setStatus("current")
_QueueGroupIndex_Type = NnTMQueueGroup
_QueueGroupIndex_Object = MibTableColumn
queueGroupIndex = _QueueGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 2),
    _QueueGroupIndex_Type()
)
queueGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queueGroupIndex.setStatus("current")
_CosIndex_Type = NnTMClassOfService
_CosIndex_Object = MibTableColumn
cosIndex = _CosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 3),
    _CosIndex_Type()
)
cosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cosIndex.setStatus("current")
_NnTMStatsInFrames_Type = Counter64
_NnTMStatsInFrames_Object = MibTableColumn
nnTMStatsInFrames = _NnTMStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 4),
    _NnTMStatsInFrames_Type()
)
nnTMStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsInFrames.setStatus("current")
_NnTMStatsInOctets_Type = Counter64
_NnTMStatsInOctets_Object = MibTableColumn
nnTMStatsInOctets = _NnTMStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 5),
    _NnTMStatsInOctets_Type()
)
nnTMStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsInOctets.setStatus("current")
_NnTMStatsInFramesDiscards_Type = Counter64
_NnTMStatsInFramesDiscards_Object = MibTableColumn
nnTMStatsInFramesDiscards = _NnTMStatsInFramesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 6),
    _NnTMStatsInFramesDiscards_Type()
)
nnTMStatsInFramesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsInFramesDiscards.setStatus("current")
_NnTMStatsInFramesDiscardsOctets_Type = Counter64
_NnTMStatsInFramesDiscardsOctets_Object = MibTableColumn
nnTMStatsInFramesDiscardsOctets = _NnTMStatsInFramesDiscardsOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 7),
    _NnTMStatsInFramesDiscardsOctets_Type()
)
nnTMStatsInFramesDiscardsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsInFramesDiscardsOctets.setStatus("current")
_NnTMStatsInFramesNonConforming_Type = Counter64
_NnTMStatsInFramesNonConforming_Object = MibTableColumn
nnTMStatsInFramesNonConforming = _NnTMStatsInFramesNonConforming_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 8),
    _NnTMStatsInFramesNonConforming_Type()
)
nnTMStatsInFramesNonConforming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsInFramesNonConforming.setStatus("current")
_NnTMStatsOutFrames_Type = Counter64
_NnTMStatsOutFrames_Object = MibTableColumn
nnTMStatsOutFrames = _NnTMStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 9),
    _NnTMStatsOutFrames_Type()
)
nnTMStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsOutFrames.setStatus("current")
_NnTMStatsOutOctets_Type = Counter64
_NnTMStatsOutOctets_Object = MibTableColumn
nnTMStatsOutOctets = _NnTMStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 10),
    _NnTMStatsOutOctets_Type()
)
nnTMStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsOutOctets.setStatus("current")
_NnTMStatsOutFramesDiscards_Type = Counter64
_NnTMStatsOutFramesDiscards_Object = MibTableColumn
nnTMStatsOutFramesDiscards = _NnTMStatsOutFramesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 11),
    _NnTMStatsOutFramesDiscards_Type()
)
nnTMStatsOutFramesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsOutFramesDiscards.setStatus("current")
_NnTMStatsOutFramesDiscardsOctets_Type = Counter64
_NnTMStatsOutFramesDiscardsOctets_Object = MibTableColumn
nnTMStatsOutFramesDiscardsOctets = _NnTMStatsOutFramesDiscardsOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 12),
    _NnTMStatsOutFramesDiscardsOctets_Type()
)
nnTMStatsOutFramesDiscardsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsOutFramesDiscardsOctets.setStatus("current")
_NnTMStatsOutFramesConformingDiscards_Type = Counter64
_NnTMStatsOutFramesConformingDiscards_Object = MibTableColumn
nnTMStatsOutFramesConformingDiscards = _NnTMStatsOutFramesConformingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 13),
    _NnTMStatsOutFramesConformingDiscards_Type()
)
nnTMStatsOutFramesConformingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsOutFramesConformingDiscards.setStatus("current")


class _NnTMStatsTxQueueUtilization_Type(Gauge32):
    """Custom type nnTMStatsTxQueueUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NnTMStatsTxQueueUtilization_Type.__name__ = "Gauge32"
_NnTMStatsTxQueueUtilization_Object = MibTableColumn
nnTMStatsTxQueueUtilization = _NnTMStatsTxQueueUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 14),
    _NnTMStatsTxQueueUtilization_Type()
)
nnTMStatsTxQueueUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsTxQueueUtilization.setStatus("current")


class _NnTMStatsTxQueueUtilizationMaxPeak_Type(Gauge32):
    """Custom type nnTMStatsTxQueueUtilizationMaxPeak based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NnTMStatsTxQueueUtilizationMaxPeak_Type.__name__ = "Gauge32"
_NnTMStatsTxQueueUtilizationMaxPeak_Object = MibTableColumn
nnTMStatsTxQueueUtilizationMaxPeak = _NnTMStatsTxQueueUtilizationMaxPeak_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 3, 1, 1, 1, 15),
    _NnTMStatsTxQueueUtilizationMaxPeak_Type()
)
nnTMStatsTxQueueUtilizationMaxPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnTMStatsTxQueueUtilizationMaxPeak.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-TM-MIB",
    **{"NnTMClassOfService": NnTMClassOfService,
       "NnTMQueueGroup": NnTMQueueGroup,
       "nnTMMIB": nnTMMIB,
       "nnTMObjects": nnTMObjects,
       "nnTMStatsTable": nnTMStatsTable,
       "nnTMStatsEntry": nnTMStatsEntry,
       "trafficMgmtIfIndex": trafficMgmtIfIndex,
       "queueGroupIndex": queueGroupIndex,
       "cosIndex": cosIndex,
       "nnTMStatsInFrames": nnTMStatsInFrames,
       "nnTMStatsInOctets": nnTMStatsInOctets,
       "nnTMStatsInFramesDiscards": nnTMStatsInFramesDiscards,
       "nnTMStatsInFramesDiscardsOctets": nnTMStatsInFramesDiscardsOctets,
       "nnTMStatsInFramesNonConforming": nnTMStatsInFramesNonConforming,
       "nnTMStatsOutFrames": nnTMStatsOutFrames,
       "nnTMStatsOutOctets": nnTMStatsOutOctets,
       "nnTMStatsOutFramesDiscards": nnTMStatsOutFramesDiscards,
       "nnTMStatsOutFramesDiscardsOctets": nnTMStatsOutFramesDiscardsOctets,
       "nnTMStatsOutFramesConformingDiscards": nnTMStatsOutFramesConformingDiscards,
       "nnTMStatsTxQueueUtilization": nnTMStatsTxQueueUtilization,
       "nnTMStatsTxQueueUtilizationMaxPeak": nnTMStatsTxQueueUtilizationMaxPeak}
)
