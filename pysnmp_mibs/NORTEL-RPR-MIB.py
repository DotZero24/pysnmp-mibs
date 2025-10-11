# SNMP MIB module (NORTEL-RPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-RPR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:23 2025
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

nnRPRMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 2)
)
if mibBuilder.loadTexts:
    nnRPRMIB.setRevisions(
        ("2005-11-18 15:41",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NnRPRSpan(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("west", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NnRPRObjects_ObjectIdentity = ObjectIdentity
nnRPRObjects = _NnRPRObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2)
)
_NnRPRSpanCounters_ObjectIdentity = ObjectIdentity
nnRPRSpanCounters = _NnRPRSpanCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1)
)
_NnRPRSpanCountersStatsTable_Object = MibTable
nnRPRSpanCountersStatsTable = _NnRPRSpanCountersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nnRPRSpanCountersStatsTable.setStatus("current")
_NnRPRSpanCountersStatsEntry_Object = MibTableRow
nnRPRSpanCountersStatsEntry = _NnRPRSpanCountersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1)
)
nnRPRSpanCountersStatsEntry.setIndexNames(
    (0, "NORTEL-RPR-MIB", "nnRPRSpanStatsIfIndex"),
    (0, "NORTEL-RPR-MIB", "nnRPRSpanStatsSpan"),
)
if mibBuilder.loadTexts:
    nnRPRSpanCountersStatsEntry.setStatus("current")
_NnRPRSpanStatsIfIndex_Type = InterfaceIndex
_NnRPRSpanStatsIfIndex_Object = MibTableColumn
nnRPRSpanStatsIfIndex = _NnRPRSpanStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 1),
    _NnRPRSpanStatsIfIndex_Type()
)
nnRPRSpanStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRPRSpanStatsIfIndex.setStatus("current")
_NnRPRSpanStatsSpan_Type = NnRPRSpan
_NnRPRSpanStatsSpan_Object = MibTableColumn
nnRPRSpanStatsSpan = _NnRPRSpanStatsSpan_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 2),
    _NnRPRSpanStatsSpan_Type()
)
nnRPRSpanStatsSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRPRSpanStatsSpan.setStatus("current")
_NnRPRSpanStatsInClassAFrames_Type = Counter64
_NnRPRSpanStatsInClassAFrames_Object = MibTableColumn
nnRPRSpanStatsInClassAFrames = _NnRPRSpanStatsInClassAFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 3),
    _NnRPRSpanStatsInClassAFrames_Type()
)
nnRPRSpanStatsInClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsInClassAFrames.setStatus("current")
_NnRPRSpanStatsInClassAOctets_Type = Counter64
_NnRPRSpanStatsInClassAOctets_Object = MibTableColumn
nnRPRSpanStatsInClassAOctets = _NnRPRSpanStatsInClassAOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 4),
    _NnRPRSpanStatsInClassAOctets_Type()
)
nnRPRSpanStatsInClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsInClassAOctets.setStatus("current")
_NnRPRSpanStatsInClassBCirFrames_Type = Counter64
_NnRPRSpanStatsInClassBCirFrames_Object = MibTableColumn
nnRPRSpanStatsInClassBCirFrames = _NnRPRSpanStatsInClassBCirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 5),
    _NnRPRSpanStatsInClassBCirFrames_Type()
)
nnRPRSpanStatsInClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsInClassBCirFrames.setStatus("current")
_NnRPRSpanStatsInClassBCirOctets_Type = Counter64
_NnRPRSpanStatsInClassBCirOctets_Object = MibTableColumn
nnRPRSpanStatsInClassBCirOctets = _NnRPRSpanStatsInClassBCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 6),
    _NnRPRSpanStatsInClassBCirOctets_Type()
)
nnRPRSpanStatsInClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsInClassBCirOctets.setStatus("current")
_NnRPRSpanStatsInClassBEirFrames_Type = Counter64
_NnRPRSpanStatsInClassBEirFrames_Object = MibTableColumn
nnRPRSpanStatsInClassBEirFrames = _NnRPRSpanStatsInClassBEirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 7),
    _NnRPRSpanStatsInClassBEirFrames_Type()
)
nnRPRSpanStatsInClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsInClassBEirFrames.setStatus("current")
_NnRPRSpanStatsInClassBEirOctets_Type = Counter64
_NnRPRSpanStatsInClassBEirOctets_Object = MibTableColumn
nnRPRSpanStatsInClassBEirOctets = _NnRPRSpanStatsInClassBEirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 8),
    _NnRPRSpanStatsInClassBEirOctets_Type()
)
nnRPRSpanStatsInClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsInClassBEirOctets.setStatus("current")
_NnRPRSpanStatsInClassCFrames_Type = Counter64
_NnRPRSpanStatsInClassCFrames_Object = MibTableColumn
nnRPRSpanStatsInClassCFrames = _NnRPRSpanStatsInClassCFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 9),
    _NnRPRSpanStatsInClassCFrames_Type()
)
nnRPRSpanStatsInClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsInClassCFrames.setStatus("current")
_NnRPRSpanStatsInClassCOctets_Type = Counter64
_NnRPRSpanStatsInClassCOctets_Object = MibTableColumn
nnRPRSpanStatsInClassCOctets = _NnRPRSpanStatsInClassCOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 10),
    _NnRPRSpanStatsInClassCOctets_Type()
)
nnRPRSpanStatsInClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsInClassCOctets.setStatus("current")
_NnRPRSpanStatsOutClassAFrames_Type = Counter64
_NnRPRSpanStatsOutClassAFrames_Object = MibTableColumn
nnRPRSpanStatsOutClassAFrames = _NnRPRSpanStatsOutClassAFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 11),
    _NnRPRSpanStatsOutClassAFrames_Type()
)
nnRPRSpanStatsOutClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsOutClassAFrames.setStatus("current")
_NnRPRSpanStatsOutClassAOctets_Type = Counter64
_NnRPRSpanStatsOutClassAOctets_Object = MibTableColumn
nnRPRSpanStatsOutClassAOctets = _NnRPRSpanStatsOutClassAOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 12),
    _NnRPRSpanStatsOutClassAOctets_Type()
)
nnRPRSpanStatsOutClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsOutClassAOctets.setStatus("current")
_NnRPRSpanStatsOutClassBCirFrames_Type = Counter64
_NnRPRSpanStatsOutClassBCirFrames_Object = MibTableColumn
nnRPRSpanStatsOutClassBCirFrames = _NnRPRSpanStatsOutClassBCirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 13),
    _NnRPRSpanStatsOutClassBCirFrames_Type()
)
nnRPRSpanStatsOutClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsOutClassBCirFrames.setStatus("current")
_NnRPRSpanStatsOutClassBCirOctets_Type = Counter64
_NnRPRSpanStatsOutClassBCirOctets_Object = MibTableColumn
nnRPRSpanStatsOutClassBCirOctets = _NnRPRSpanStatsOutClassBCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 14),
    _NnRPRSpanStatsOutClassBCirOctets_Type()
)
nnRPRSpanStatsOutClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsOutClassBCirOctets.setStatus("current")
_NnRPRSpanStatsOutClassBEirFrames_Type = Counter64
_NnRPRSpanStatsOutClassBEirFrames_Object = MibTableColumn
nnRPRSpanStatsOutClassBEirFrames = _NnRPRSpanStatsOutClassBEirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 15),
    _NnRPRSpanStatsOutClassBEirFrames_Type()
)
nnRPRSpanStatsOutClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsOutClassBEirFrames.setStatus("current")
_NnRPRSpanStatsOutClassBEirOctets_Type = Counter64
_NnRPRSpanStatsOutClassBEirOctets_Object = MibTableColumn
nnRPRSpanStatsOutClassBEirOctets = _NnRPRSpanStatsOutClassBEirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 16),
    _NnRPRSpanStatsOutClassBEirOctets_Type()
)
nnRPRSpanStatsOutClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsOutClassBEirOctets.setStatus("current")
_NnRPRSpanStatsOutClassCFrames_Type = Counter64
_NnRPRSpanStatsOutClassCFrames_Object = MibTableColumn
nnRPRSpanStatsOutClassCFrames = _NnRPRSpanStatsOutClassCFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 17),
    _NnRPRSpanStatsOutClassCFrames_Type()
)
nnRPRSpanStatsOutClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsOutClassCFrames.setStatus("current")
_NnRPRSpanStatsOutClassCOctets_Type = Counter64
_NnRPRSpanStatsOutClassCOctets_Object = MibTableColumn
nnRPRSpanStatsOutClassCOctets = _NnRPRSpanStatsOutClassCOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 1, 1, 1, 18),
    _NnRPRSpanStatsOutClassCOctets_Type()
)
nnRPRSpanStatsOutClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsOutClassCOctets.setStatus("current")
_NnRPRSpanPassThruCounters_ObjectIdentity = ObjectIdentity
nnRPRSpanPassThruCounters = _NnRPRSpanPassThruCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2)
)
_NnRPRSpanPassThruCountersStatsTable_Object = MibTable
nnRPRSpanPassThruCountersStatsTable = _NnRPRSpanPassThruCountersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nnRPRSpanPassThruCountersStatsTable.setStatus("current")
_NnRPRSpanPassThruCountersStatsEntry_Object = MibTableRow
nnRPRSpanPassThruCountersStatsEntry = _NnRPRSpanPassThruCountersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1)
)
nnRPRSpanPassThruCountersStatsEntry.setIndexNames(
    (0, "NORTEL-RPR-MIB", "nnRPRSpanStatsPtIfIndex"),
    (0, "NORTEL-RPR-MIB", "nnRPRSpanPtSpan"),
)
if mibBuilder.loadTexts:
    nnRPRSpanPassThruCountersStatsEntry.setStatus("current")
_NnRPRSpanStatsPtIfIndex_Type = InterfaceIndex
_NnRPRSpanStatsPtIfIndex_Object = MibTableColumn
nnRPRSpanStatsPtIfIndex = _NnRPRSpanStatsPtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 1),
    _NnRPRSpanStatsPtIfIndex_Type()
)
nnRPRSpanStatsPtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtIfIndex.setStatus("current")
_NnRPRSpanPtSpan_Type = NnRPRSpan
_NnRPRSpanPtSpan_Object = MibTableColumn
nnRPRSpanPtSpan = _NnRPRSpanPtSpan_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 2),
    _NnRPRSpanPtSpan_Type()
)
nnRPRSpanPtSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRPRSpanPtSpan.setStatus("current")
_NnRPRSpanStatsPtClassAFrames_Type = Counter64
_NnRPRSpanStatsPtClassAFrames_Object = MibTableColumn
nnRPRSpanStatsPtClassAFrames = _NnRPRSpanStatsPtClassAFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 3),
    _NnRPRSpanStatsPtClassAFrames_Type()
)
nnRPRSpanStatsPtClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassAFrames.setStatus("current")
_NnRPRSpanStatsPtClassAOctets_Type = Counter64
_NnRPRSpanStatsPtClassAOctets_Object = MibTableColumn
nnRPRSpanStatsPtClassAOctets = _NnRPRSpanStatsPtClassAOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 4),
    _NnRPRSpanStatsPtClassAOctets_Type()
)
nnRPRSpanStatsPtClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassAOctets.setStatus("current")
_NnRPRSpanStatsPtClassBCirFrames_Type = Counter64
_NnRPRSpanStatsPtClassBCirFrames_Object = MibTableColumn
nnRPRSpanStatsPtClassBCirFrames = _NnRPRSpanStatsPtClassBCirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 5),
    _NnRPRSpanStatsPtClassBCirFrames_Type()
)
nnRPRSpanStatsPtClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassBCirFrames.setStatus("current")
_NnRPRSpanStatsPtClassBCirOctets_Type = Counter64
_NnRPRSpanStatsPtClassBCirOctets_Object = MibTableColumn
nnRPRSpanStatsPtClassBCirOctets = _NnRPRSpanStatsPtClassBCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 6),
    _NnRPRSpanStatsPtClassBCirOctets_Type()
)
nnRPRSpanStatsPtClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassBCirOctets.setStatus("current")
_NnRPRSpanStatsPtClassBEirFrames_Type = Counter64
_NnRPRSpanStatsPtClassBEirFrames_Object = MibTableColumn
nnRPRSpanStatsPtClassBEirFrames = _NnRPRSpanStatsPtClassBEirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 7),
    _NnRPRSpanStatsPtClassBEirFrames_Type()
)
nnRPRSpanStatsPtClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassBEirFrames.setStatus("current")
_NnRPRSpanStatsPtClassBEirOctets_Type = Counter64
_NnRPRSpanStatsPtClassBEirOctets_Object = MibTableColumn
nnRPRSpanStatsPtClassBEirOctets = _NnRPRSpanStatsPtClassBEirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 8),
    _NnRPRSpanStatsPtClassBEirOctets_Type()
)
nnRPRSpanStatsPtClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassBEirOctets.setStatus("current")
_NnRPRSpanStatsPtClassCFrames_Type = Counter64
_NnRPRSpanStatsPtClassCFrames_Object = MibTableColumn
nnRPRSpanStatsPtClassCFrames = _NnRPRSpanStatsPtClassCFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 9),
    _NnRPRSpanStatsPtClassCFrames_Type()
)
nnRPRSpanStatsPtClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassCFrames.setStatus("current")
_NnRPRSpanStatsPtClassCOctets_Type = Counter64
_NnRPRSpanStatsPtClassCOctets_Object = MibTableColumn
nnRPRSpanStatsPtClassCOctets = _NnRPRSpanStatsPtClassCOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 10),
    _NnRPRSpanStatsPtClassCOctets_Type()
)
nnRPRSpanStatsPtClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassCOctets.setStatus("current")
_NnRPRSpanStatsPtClassAFramesDiscards_Type = Counter64
_NnRPRSpanStatsPtClassAFramesDiscards_Object = MibTableColumn
nnRPRSpanStatsPtClassAFramesDiscards = _NnRPRSpanStatsPtClassAFramesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 11),
    _NnRPRSpanStatsPtClassAFramesDiscards_Type()
)
nnRPRSpanStatsPtClassAFramesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassAFramesDiscards.setStatus("current")
_NnRPRSpanStatsPtClassBCirFramesDiscards_Type = Counter64
_NnRPRSpanStatsPtClassBCirFramesDiscards_Object = MibTableColumn
nnRPRSpanStatsPtClassBCirFramesDiscards = _NnRPRSpanStatsPtClassBCirFramesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 12),
    _NnRPRSpanStatsPtClassBCirFramesDiscards_Type()
)
nnRPRSpanStatsPtClassBCirFramesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassBCirFramesDiscards.setStatus("current")
_NnRPRSpanStatsPtClassBEirFramesDiscards_Type = Counter64
_NnRPRSpanStatsPtClassBEirFramesDiscards_Object = MibTableColumn
nnRPRSpanStatsPtClassBEirFramesDiscards = _NnRPRSpanStatsPtClassBEirFramesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 13),
    _NnRPRSpanStatsPtClassBEirFramesDiscards_Type()
)
nnRPRSpanStatsPtClassBEirFramesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassBEirFramesDiscards.setStatus("current")
_NnRPRSpanStatsPtClassCFramesDiscards_Type = Counter64
_NnRPRSpanStatsPtClassCFramesDiscards_Object = MibTableColumn
nnRPRSpanStatsPtClassCFramesDiscards = _NnRPRSpanStatsPtClassCFramesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 2, 1, 1, 14),
    _NnRPRSpanStatsPtClassCFramesDiscards_Type()
)
nnRPRSpanStatsPtClassCFramesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanStatsPtClassCFramesDiscards.setStatus("current")
_NnRPRSpanErrorCounters_ObjectIdentity = ObjectIdentity
nnRPRSpanErrorCounters = _NnRPRSpanErrorCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3)
)
_NnRPRSpanErrorCountersStatsTable_Object = MibTable
nnRPRSpanErrorCountersStatsTable = _NnRPRSpanErrorCountersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nnRPRSpanErrorCountersStatsTable.setStatus("current")
_NnRPRSpanErrorCountersStatsEntry_Object = MibTableRow
nnRPRSpanErrorCountersStatsEntry = _NnRPRSpanErrorCountersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1)
)
nnRPRSpanErrorCountersStatsEntry.setIndexNames(
    (0, "NORTEL-RPR-MIB", "nnRPRSpanErrorStatsIfIndex"),
    (0, "NORTEL-RPR-MIB", "nnRPRSpanErrorStatsSpan"),
)
if mibBuilder.loadTexts:
    nnRPRSpanErrorCountersStatsEntry.setStatus("current")
_NnRPRSpanErrorStatsIfIndex_Type = InterfaceIndex
_NnRPRSpanErrorStatsIfIndex_Object = MibTableColumn
nnRPRSpanErrorStatsIfIndex = _NnRPRSpanErrorStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 1),
    _NnRPRSpanErrorStatsIfIndex_Type()
)
nnRPRSpanErrorStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsIfIndex.setStatus("current")
_NnRPRSpanErrorStatsSpan_Type = NnRPRSpan
_NnRPRSpanErrorStatsSpan_Object = MibTableColumn
nnRPRSpanErrorStatsSpan = _NnRPRSpanErrorStatsSpan_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 2),
    _NnRPRSpanErrorStatsSpan_Type()
)
nnRPRSpanErrorStatsSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsSpan.setStatus("current")
_NnRPRSpanErrorStatsTtlExpFrames_Type = Counter64
_NnRPRSpanErrorStatsTtlExpFrames_Object = MibTableColumn
nnRPRSpanErrorStatsTtlExpFrames = _NnRPRSpanErrorStatsTtlExpFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 3),
    _NnRPRSpanErrorStatsTtlExpFrames_Type()
)
nnRPRSpanErrorStatsTtlExpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsTtlExpFrames.setStatus("current")
_NnRPRSpanErrorStatsTooLongFrames_Type = Counter64
_NnRPRSpanErrorStatsTooLongFrames_Object = MibTableColumn
nnRPRSpanErrorStatsTooLongFrames = _NnRPRSpanErrorStatsTooLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 4),
    _NnRPRSpanErrorStatsTooLongFrames_Type()
)
nnRPRSpanErrorStatsTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsTooLongFrames.setStatus("current")
_NnRPRSpanErrorStatsTooShortFrames_Type = Counter64
_NnRPRSpanErrorStatsTooShortFrames_Object = MibTableColumn
nnRPRSpanErrorStatsTooShortFrames = _NnRPRSpanErrorStatsTooShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 5),
    _NnRPRSpanErrorStatsTooShortFrames_Type()
)
nnRPRSpanErrorStatsTooShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsTooShortFrames.setStatus("current")
_NnRPRSpanErrorStatsBadHecFrames_Type = Counter64
_NnRPRSpanErrorStatsBadHecFrames_Object = MibTableColumn
nnRPRSpanErrorStatsBadHecFrames = _NnRPRSpanErrorStatsBadHecFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 6),
    _NnRPRSpanErrorStatsBadHecFrames_Type()
)
nnRPRSpanErrorStatsBadHecFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsBadHecFrames.setStatus("current")
_NnRPRSpanErrorStatsBadFcsFrames_Type = Counter64
_NnRPRSpanErrorStatsBadFcsFrames_Object = MibTableColumn
nnRPRSpanErrorStatsBadFcsFrames = _NnRPRSpanErrorStatsBadFcsFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 7),
    _NnRPRSpanErrorStatsBadFcsFrames_Type()
)
nnRPRSpanErrorStatsBadFcsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsBadFcsFrames.setStatus("current")
_NnRPRSpanErrorStatsSelfSrcUcastFrames_Type = Counter64
_NnRPRSpanErrorStatsSelfSrcUcastFrames_Object = MibTableColumn
nnRPRSpanErrorStatsSelfSrcUcastFrames = _NnRPRSpanErrorStatsSelfSrcUcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 8),
    _NnRPRSpanErrorStatsSelfSrcUcastFrames_Type()
)
nnRPRSpanErrorStatsSelfSrcUcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsSelfSrcUcastFrames.setStatus("current")
_NnRPRSpanErrorStatsPmdAbortFrames_Type = Counter64
_NnRPRSpanErrorStatsPmdAbortFrames_Object = MibTableColumn
nnRPRSpanErrorStatsPmdAbortFrames = _NnRPRSpanErrorStatsPmdAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 9),
    _NnRPRSpanErrorStatsPmdAbortFrames_Type()
)
nnRPRSpanErrorStatsPmdAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsPmdAbortFrames.setStatus("current")
_NnRPRSpanErrorStatsBadAddrFrames_Type = Counter64
_NnRPRSpanErrorStatsBadAddrFrames_Object = MibTableColumn
nnRPRSpanErrorStatsBadAddrFrames = _NnRPRSpanErrorStatsBadAddrFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 10),
    _NnRPRSpanErrorStatsBadAddrFrames_Type()
)
nnRPRSpanErrorStatsBadAddrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsBadAddrFrames.setStatus("current")
_NnRPRSpanErrorStatsBadParityFrames_Type = Counter64
_NnRPRSpanErrorStatsBadParityFrames_Object = MibTableColumn
nnRPRSpanErrorStatsBadParityFrames = _NnRPRSpanErrorStatsBadParityFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 11),
    _NnRPRSpanErrorStatsBadParityFrames_Type()
)
nnRPRSpanErrorStatsBadParityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsBadParityFrames.setStatus("current")
_NnRPRSpanErrorStatsScffErrors_Type = Counter64
_NnRPRSpanErrorStatsScffErrors_Object = MibTableColumn
nnRPRSpanErrorStatsScffErrors = _NnRPRSpanErrorStatsScffErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 3, 1, 1, 12),
    _NnRPRSpanErrorStatsScffErrors_Type()
)
nnRPRSpanErrorStatsScffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRSpanErrorStatsScffErrors.setStatus("current")
_NnRPRClientCounters_ObjectIdentity = ObjectIdentity
nnRPRClientCounters = _NnRPRClientCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4)
)
_NnRPRClientCountersStatsTable_Object = MibTable
nnRPRClientCountersStatsTable = _NnRPRClientCountersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    nnRPRClientCountersStatsTable.setStatus("current")
_NnRPRClientCountersStatsEntry_Object = MibTableRow
nnRPRClientCountersStatsEntry = _NnRPRClientCountersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1)
)
nnRPRClientCountersStatsEntry.setIndexNames(
    (0, "NORTEL-RPR-MIB", "nnRPRClientStatsIfIndex"),
)
if mibBuilder.loadTexts:
    nnRPRClientCountersStatsEntry.setStatus("current")
_NnRPRClientStatsIfIndex_Type = InterfaceIndex
_NnRPRClientStatsIfIndex_Object = MibTableColumn
nnRPRClientStatsIfIndex = _NnRPRClientStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 1),
    _NnRPRClientStatsIfIndex_Type()
)
nnRPRClientStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRPRClientStatsIfIndex.setStatus("current")
_NnRPRClientStatsInUcastClassAFrames_Type = Counter64
_NnRPRClientStatsInUcastClassAFrames_Object = MibTableColumn
nnRPRClientStatsInUcastClassAFrames = _NnRPRClientStatsInUcastClassAFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 2),
    _NnRPRClientStatsInUcastClassAFrames_Type()
)
nnRPRClientStatsInUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInUcastClassAFrames.setStatus("current")
_NnRPRClientStatsInUcastClassAOctets_Type = Counter64
_NnRPRClientStatsInUcastClassAOctets_Object = MibTableColumn
nnRPRClientStatsInUcastClassAOctets = _NnRPRClientStatsInUcastClassAOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 3),
    _NnRPRClientStatsInUcastClassAOctets_Type()
)
nnRPRClientStatsInUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInUcastClassAOctets.setStatus("current")
_NnRPRClientStatsInUcastClassBCirFrames_Type = Counter64
_NnRPRClientStatsInUcastClassBCirFrames_Object = MibTableColumn
nnRPRClientStatsInUcastClassBCirFrames = _NnRPRClientStatsInUcastClassBCirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 4),
    _NnRPRClientStatsInUcastClassBCirFrames_Type()
)
nnRPRClientStatsInUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInUcastClassBCirFrames.setStatus("current")
_NnRPRClientStatsInUcastClassBCirOctets_Type = Counter64
_NnRPRClientStatsInUcastClassBCirOctets_Object = MibTableColumn
nnRPRClientStatsInUcastClassBCirOctets = _NnRPRClientStatsInUcastClassBCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 5),
    _NnRPRClientStatsInUcastClassBCirOctets_Type()
)
nnRPRClientStatsInUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInUcastClassBCirOctets.setStatus("current")
_NnRPRClientStatsInUcastClassBEirFrames_Type = Counter64
_NnRPRClientStatsInUcastClassBEirFrames_Object = MibTableColumn
nnRPRClientStatsInUcastClassBEirFrames = _NnRPRClientStatsInUcastClassBEirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 6),
    _NnRPRClientStatsInUcastClassBEirFrames_Type()
)
nnRPRClientStatsInUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInUcastClassBEirFrames.setStatus("current")
_NnRPRClientStatsInUcastClassBEirOctets_Type = Counter64
_NnRPRClientStatsInUcastClassBEirOctets_Object = MibTableColumn
nnRPRClientStatsInUcastClassBEirOctets = _NnRPRClientStatsInUcastClassBEirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 7),
    _NnRPRClientStatsInUcastClassBEirOctets_Type()
)
nnRPRClientStatsInUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInUcastClassBEirOctets.setStatus("current")
_NnRPRClientStatsInUcastClassCFrames_Type = Counter64
_NnRPRClientStatsInUcastClassCFrames_Object = MibTableColumn
nnRPRClientStatsInUcastClassCFrames = _NnRPRClientStatsInUcastClassCFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 8),
    _NnRPRClientStatsInUcastClassCFrames_Type()
)
nnRPRClientStatsInUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInUcastClassCFrames.setStatus("current")
_NnRPRClientStatsInUcastClassCOctets_Type = Counter64
_NnRPRClientStatsInUcastClassCOctets_Object = MibTableColumn
nnRPRClientStatsInUcastClassCOctets = _NnRPRClientStatsInUcastClassCOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 9),
    _NnRPRClientStatsInUcastClassCOctets_Type()
)
nnRPRClientStatsInUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInUcastClassCOctets.setStatus("current")
_NnRPRClientStatsInMcastClassAFrames_Type = Counter64
_NnRPRClientStatsInMcastClassAFrames_Object = MibTableColumn
nnRPRClientStatsInMcastClassAFrames = _NnRPRClientStatsInMcastClassAFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 10),
    _NnRPRClientStatsInMcastClassAFrames_Type()
)
nnRPRClientStatsInMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInMcastClassAFrames.setStatus("current")
_NnRPRClientStatsInMcastClassAOctets_Type = Counter64
_NnRPRClientStatsInMcastClassAOctets_Object = MibTableColumn
nnRPRClientStatsInMcastClassAOctets = _NnRPRClientStatsInMcastClassAOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 11),
    _NnRPRClientStatsInMcastClassAOctets_Type()
)
nnRPRClientStatsInMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInMcastClassAOctets.setStatus("current")
_NnRPRClientStatsInMcastClassBCirFrames_Type = Counter64
_NnRPRClientStatsInMcastClassBCirFrames_Object = MibTableColumn
nnRPRClientStatsInMcastClassBCirFrames = _NnRPRClientStatsInMcastClassBCirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 12),
    _NnRPRClientStatsInMcastClassBCirFrames_Type()
)
nnRPRClientStatsInMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInMcastClassBCirFrames.setStatus("current")
_NnRPRClientStatsInMcastClassBCirOctets_Type = Counter64
_NnRPRClientStatsInMcastClassBCirOctets_Object = MibTableColumn
nnRPRClientStatsInMcastClassBCirOctets = _NnRPRClientStatsInMcastClassBCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 13),
    _NnRPRClientStatsInMcastClassBCirOctets_Type()
)
nnRPRClientStatsInMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInMcastClassBCirOctets.setStatus("current")
_NnRPRClientStatsInMcastClassBEirFrames_Type = Counter64
_NnRPRClientStatsInMcastClassBEirFrames_Object = MibTableColumn
nnRPRClientStatsInMcastClassBEirFrames = _NnRPRClientStatsInMcastClassBEirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 14),
    _NnRPRClientStatsInMcastClassBEirFrames_Type()
)
nnRPRClientStatsInMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInMcastClassBEirFrames.setStatus("current")
_NnRPRClientStatsInMcastClassBEirOctets_Type = Counter64
_NnRPRClientStatsInMcastClassBEirOctets_Object = MibTableColumn
nnRPRClientStatsInMcastClassBEirOctets = _NnRPRClientStatsInMcastClassBEirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 15),
    _NnRPRClientStatsInMcastClassBEirOctets_Type()
)
nnRPRClientStatsInMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInMcastClassBEirOctets.setStatus("current")
_NnRPRClientStatsInMcastClassCFrames_Type = Counter64
_NnRPRClientStatsInMcastClassCFrames_Object = MibTableColumn
nnRPRClientStatsInMcastClassCFrames = _NnRPRClientStatsInMcastClassCFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 16),
    _NnRPRClientStatsInMcastClassCFrames_Type()
)
nnRPRClientStatsInMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInMcastClassCFrames.setStatus("current")
_NnRPRClientStatsInMcastClassCOctets_Type = Counter64
_NnRPRClientStatsInMcastClassCOctets_Object = MibTableColumn
nnRPRClientStatsInMcastClassCOctets = _NnRPRClientStatsInMcastClassCOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 17),
    _NnRPRClientStatsInMcastClassCOctets_Type()
)
nnRPRClientStatsInMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsInMcastClassCOctets.setStatus("current")
_NnRPRClientStatsOutUcastClassAFrames_Type = Counter64
_NnRPRClientStatsOutUcastClassAFrames_Object = MibTableColumn
nnRPRClientStatsOutUcastClassAFrames = _NnRPRClientStatsOutUcastClassAFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 18),
    _NnRPRClientStatsOutUcastClassAFrames_Type()
)
nnRPRClientStatsOutUcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutUcastClassAFrames.setStatus("current")
_NnRPRClientStatsOutUcastClassAOctets_Type = Counter64
_NnRPRClientStatsOutUcastClassAOctets_Object = MibTableColumn
nnRPRClientStatsOutUcastClassAOctets = _NnRPRClientStatsOutUcastClassAOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 19),
    _NnRPRClientStatsOutUcastClassAOctets_Type()
)
nnRPRClientStatsOutUcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutUcastClassAOctets.setStatus("current")
_NnRPRClientStatsOutUcastClassBCirFrames_Type = Counter64
_NnRPRClientStatsOutUcastClassBCirFrames_Object = MibTableColumn
nnRPRClientStatsOutUcastClassBCirFrames = _NnRPRClientStatsOutUcastClassBCirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 20),
    _NnRPRClientStatsOutUcastClassBCirFrames_Type()
)
nnRPRClientStatsOutUcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutUcastClassBCirFrames.setStatus("current")
_NnRPRClientStatsOutUcastClassBCirOctets_Type = Counter64
_NnRPRClientStatsOutUcastClassBCirOctets_Object = MibTableColumn
nnRPRClientStatsOutUcastClassBCirOctets = _NnRPRClientStatsOutUcastClassBCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 21),
    _NnRPRClientStatsOutUcastClassBCirOctets_Type()
)
nnRPRClientStatsOutUcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutUcastClassBCirOctets.setStatus("current")
_NnRPRClientStatsOutUcastClassBEirFrames_Type = Counter64
_NnRPRClientStatsOutUcastClassBEirFrames_Object = MibTableColumn
nnRPRClientStatsOutUcastClassBEirFrames = _NnRPRClientStatsOutUcastClassBEirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 22),
    _NnRPRClientStatsOutUcastClassBEirFrames_Type()
)
nnRPRClientStatsOutUcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutUcastClassBEirFrames.setStatus("current")
_NnRPRClientStatsOutUcastClassBEirOctets_Type = Counter64
_NnRPRClientStatsOutUcastClassBEirOctets_Object = MibTableColumn
nnRPRClientStatsOutUcastClassBEirOctets = _NnRPRClientStatsOutUcastClassBEirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 23),
    _NnRPRClientStatsOutUcastClassBEirOctets_Type()
)
nnRPRClientStatsOutUcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutUcastClassBEirOctets.setStatus("current")
_NnRPRClientStatsOutUcastClassCFrames_Type = Counter64
_NnRPRClientStatsOutUcastClassCFrames_Object = MibTableColumn
nnRPRClientStatsOutUcastClassCFrames = _NnRPRClientStatsOutUcastClassCFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 24),
    _NnRPRClientStatsOutUcastClassCFrames_Type()
)
nnRPRClientStatsOutUcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutUcastClassCFrames.setStatus("current")
_NnRPRClientStatsOutUcastClassCOctets_Type = Counter64
_NnRPRClientStatsOutUcastClassCOctets_Object = MibTableColumn
nnRPRClientStatsOutUcastClassCOctets = _NnRPRClientStatsOutUcastClassCOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 25),
    _NnRPRClientStatsOutUcastClassCOctets_Type()
)
nnRPRClientStatsOutUcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutUcastClassCOctets.setStatus("current")
_NnRPRClientStatsOutMcastClassAFrames_Type = Counter64
_NnRPRClientStatsOutMcastClassAFrames_Object = MibTableColumn
nnRPRClientStatsOutMcastClassAFrames = _NnRPRClientStatsOutMcastClassAFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 26),
    _NnRPRClientStatsOutMcastClassAFrames_Type()
)
nnRPRClientStatsOutMcastClassAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutMcastClassAFrames.setStatus("current")
_NnRPRClientStatsOutMcastClassAOctets_Type = Counter64
_NnRPRClientStatsOutMcastClassAOctets_Object = MibTableColumn
nnRPRClientStatsOutMcastClassAOctets = _NnRPRClientStatsOutMcastClassAOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 27),
    _NnRPRClientStatsOutMcastClassAOctets_Type()
)
nnRPRClientStatsOutMcastClassAOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutMcastClassAOctets.setStatus("current")
_NnRPRClientStatsOutMcastClassBCirFrames_Type = Counter64
_NnRPRClientStatsOutMcastClassBCirFrames_Object = MibTableColumn
nnRPRClientStatsOutMcastClassBCirFrames = _NnRPRClientStatsOutMcastClassBCirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 28),
    _NnRPRClientStatsOutMcastClassBCirFrames_Type()
)
nnRPRClientStatsOutMcastClassBCirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutMcastClassBCirFrames.setStatus("current")
_NnRPRClientStatsOutMcastClassBCirOctets_Type = Counter64
_NnRPRClientStatsOutMcastClassBCirOctets_Object = MibTableColumn
nnRPRClientStatsOutMcastClassBCirOctets = _NnRPRClientStatsOutMcastClassBCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 29),
    _NnRPRClientStatsOutMcastClassBCirOctets_Type()
)
nnRPRClientStatsOutMcastClassBCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutMcastClassBCirOctets.setStatus("current")
_NnRPRClientStatsOutMcastClassBEirFrames_Type = Counter64
_NnRPRClientStatsOutMcastClassBEirFrames_Object = MibTableColumn
nnRPRClientStatsOutMcastClassBEirFrames = _NnRPRClientStatsOutMcastClassBEirFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 30),
    _NnRPRClientStatsOutMcastClassBEirFrames_Type()
)
nnRPRClientStatsOutMcastClassBEirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutMcastClassBEirFrames.setStatus("current")
_NnRPRClientStatsOutMcastClassBEirOctets_Type = Counter64
_NnRPRClientStatsOutMcastClassBEirOctets_Object = MibTableColumn
nnRPRClientStatsOutMcastClassBEirOctets = _NnRPRClientStatsOutMcastClassBEirOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 31),
    _NnRPRClientStatsOutMcastClassBEirOctets_Type()
)
nnRPRClientStatsOutMcastClassBEirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutMcastClassBEirOctets.setStatus("current")
_NnRPRClientStatsOutMcastClassCFrames_Type = Counter64
_NnRPRClientStatsOutMcastClassCFrames_Object = MibTableColumn
nnRPRClientStatsOutMcastClassCFrames = _NnRPRClientStatsOutMcastClassCFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 32),
    _NnRPRClientStatsOutMcastClassCFrames_Type()
)
nnRPRClientStatsOutMcastClassCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutMcastClassCFrames.setStatus("current")
_NnRPRClientStatsOutMcastClassCOctets_Type = Counter64
_NnRPRClientStatsOutMcastClassCOctets_Object = MibTableColumn
nnRPRClientStatsOutMcastClassCOctets = _NnRPRClientStatsOutMcastClassCOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 4, 1, 1, 33),
    _NnRPRClientStatsOutMcastClassCOctets_Type()
)
nnRPRClientStatsOutMcastClassCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientStatsOutMcastClassCOctets.setStatus("current")
_NnRPRClientCtrlCounters_ObjectIdentity = ObjectIdentity
nnRPRClientCtrlCounters = _NnRPRClientCtrlCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5)
)
_NnRPRClientCtrlCountersStatsTable_Object = MibTable
nnRPRClientCtrlCountersStatsTable = _NnRPRClientCtrlCountersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    nnRPRClientCtrlCountersStatsTable.setStatus("current")
_NnRPRClientCtrlCountersStatsEntry_Object = MibTableRow
nnRPRClientCtrlCountersStatsEntry = _NnRPRClientCtrlCountersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1)
)
nnRPRClientCtrlCountersStatsEntry.setIndexNames(
    (0, "NORTEL-RPR-MIB", "nnRPRClientCtrlStatsIfIndex"),
)
if mibBuilder.loadTexts:
    nnRPRClientCtrlCountersStatsEntry.setStatus("current")
_NnRPRClientCtrlStatsIfIndex_Type = InterfaceIndex
_NnRPRClientCtrlStatsIfIndex_Object = MibTableColumn
nnRPRClientCtrlStatsIfIndex = _NnRPRClientCtrlStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 1),
    _NnRPRClientCtrlStatsIfIndex_Type()
)
nnRPRClientCtrlStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsIfIndex.setStatus("current")
_NnRPRClientCtrlStatsInCtrlFrames_Type = Counter64
_NnRPRClientCtrlStatsInCtrlFrames_Object = MibTableColumn
nnRPRClientCtrlStatsInCtrlFrames = _NnRPRClientCtrlStatsInCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 2),
    _NnRPRClientCtrlStatsInCtrlFrames_Type()
)
nnRPRClientCtrlStatsInCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsInCtrlFrames.setStatus("current")
_NnRPRClientCtrlStatsInOamEchoFrames_Type = Counter64
_NnRPRClientCtrlStatsInOamEchoFrames_Object = MibTableColumn
nnRPRClientCtrlStatsInOamEchoFrames = _NnRPRClientCtrlStatsInOamEchoFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 3),
    _NnRPRClientCtrlStatsInOamEchoFrames_Type()
)
nnRPRClientCtrlStatsInOamEchoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsInOamEchoFrames.setStatus("current")
_NnRPRClientCtrlStatsInOamOrgFrames_Type = Counter64
_NnRPRClientCtrlStatsInOamOrgFrames_Object = MibTableColumn
nnRPRClientCtrlStatsInOamOrgFrames = _NnRPRClientCtrlStatsInOamOrgFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 4),
    _NnRPRClientCtrlStatsInOamOrgFrames_Type()
)
nnRPRClientCtrlStatsInOamOrgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsInOamOrgFrames.setStatus("current")
_NnRPRClientCtrlStatsInTopoAtdFrames_Type = Counter64
_NnRPRClientCtrlStatsInTopoAtdFrames_Object = MibTableColumn
nnRPRClientCtrlStatsInTopoAtdFrames = _NnRPRClientCtrlStatsInTopoAtdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 5),
    _NnRPRClientCtrlStatsInTopoAtdFrames_Type()
)
nnRPRClientCtrlStatsInTopoAtdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsInTopoAtdFrames.setStatus("current")
_NnRPRClientCtrlStatsInTopoTpFrames_Type = Counter64
_NnRPRClientCtrlStatsInTopoTpFrames_Object = MibTableColumn
nnRPRClientCtrlStatsInTopoTpFrames = _NnRPRClientCtrlStatsInTopoTpFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 6),
    _NnRPRClientCtrlStatsInTopoTpFrames_Type()
)
nnRPRClientCtrlStatsInTopoTpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsInTopoTpFrames.setStatus("current")
_NnRPRClientCtrlStatsOutCtrlFrames_Type = Counter64
_NnRPRClientCtrlStatsOutCtrlFrames_Object = MibTableColumn
nnRPRClientCtrlStatsOutCtrlFrames = _NnRPRClientCtrlStatsOutCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 7),
    _NnRPRClientCtrlStatsOutCtrlFrames_Type()
)
nnRPRClientCtrlStatsOutCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsOutCtrlFrames.setStatus("current")
_NnRPRClientCtrlStatsOutOamEchoFrames_Type = Counter64
_NnRPRClientCtrlStatsOutOamEchoFrames_Object = MibTableColumn
nnRPRClientCtrlStatsOutOamEchoFrames = _NnRPRClientCtrlStatsOutOamEchoFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 8),
    _NnRPRClientCtrlStatsOutOamEchoFrames_Type()
)
nnRPRClientCtrlStatsOutOamEchoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsOutOamEchoFrames.setStatus("current")
_NnRPRClientCtrlStatsOutOamOrgFrames_Type = Counter64
_NnRPRClientCtrlStatsOutOamOrgFrames_Object = MibTableColumn
nnRPRClientCtrlStatsOutOamOrgFrames = _NnRPRClientCtrlStatsOutOamOrgFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 9),
    _NnRPRClientCtrlStatsOutOamOrgFrames_Type()
)
nnRPRClientCtrlStatsOutOamOrgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsOutOamOrgFrames.setStatus("current")
_NnRPRClientCtrlStatsOutTopoAtdFrames_Type = Counter64
_NnRPRClientCtrlStatsOutTopoAtdFrames_Object = MibTableColumn
nnRPRClientCtrlStatsOutTopoAtdFrames = _NnRPRClientCtrlStatsOutTopoAtdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 10),
    _NnRPRClientCtrlStatsOutTopoAtdFrames_Type()
)
nnRPRClientCtrlStatsOutTopoAtdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsOutTopoAtdFrames.setStatus("current")
_NnRPRClientCtrlStatsOutTopoTpFrames_Type = Counter64
_NnRPRClientCtrlStatsOutTopoTpFrames_Object = MibTableColumn
nnRPRClientCtrlStatsOutTopoTpFrames = _NnRPRClientCtrlStatsOutTopoTpFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 2, 2, 5, 1, 1, 11),
    _NnRPRClientCtrlStatsOutTopoTpFrames_Type()
)
nnRPRClientCtrlStatsOutTopoTpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRPRClientCtrlStatsOutTopoTpFrames.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-RPR-MIB",
    **{"NnRPRSpan": NnRPRSpan,
       "nnRPRMIB": nnRPRMIB,
       "nnRPRObjects": nnRPRObjects,
       "nnRPRSpanCounters": nnRPRSpanCounters,
       "nnRPRSpanCountersStatsTable": nnRPRSpanCountersStatsTable,
       "nnRPRSpanCountersStatsEntry": nnRPRSpanCountersStatsEntry,
       "nnRPRSpanStatsIfIndex": nnRPRSpanStatsIfIndex,
       "nnRPRSpanStatsSpan": nnRPRSpanStatsSpan,
       "nnRPRSpanStatsInClassAFrames": nnRPRSpanStatsInClassAFrames,
       "nnRPRSpanStatsInClassAOctets": nnRPRSpanStatsInClassAOctets,
       "nnRPRSpanStatsInClassBCirFrames": nnRPRSpanStatsInClassBCirFrames,
       "nnRPRSpanStatsInClassBCirOctets": nnRPRSpanStatsInClassBCirOctets,
       "nnRPRSpanStatsInClassBEirFrames": nnRPRSpanStatsInClassBEirFrames,
       "nnRPRSpanStatsInClassBEirOctets": nnRPRSpanStatsInClassBEirOctets,
       "nnRPRSpanStatsInClassCFrames": nnRPRSpanStatsInClassCFrames,
       "nnRPRSpanStatsInClassCOctets": nnRPRSpanStatsInClassCOctets,
       "nnRPRSpanStatsOutClassAFrames": nnRPRSpanStatsOutClassAFrames,
       "nnRPRSpanStatsOutClassAOctets": nnRPRSpanStatsOutClassAOctets,
       "nnRPRSpanStatsOutClassBCirFrames": nnRPRSpanStatsOutClassBCirFrames,
       "nnRPRSpanStatsOutClassBCirOctets": nnRPRSpanStatsOutClassBCirOctets,
       "nnRPRSpanStatsOutClassBEirFrames": nnRPRSpanStatsOutClassBEirFrames,
       "nnRPRSpanStatsOutClassBEirOctets": nnRPRSpanStatsOutClassBEirOctets,
       "nnRPRSpanStatsOutClassCFrames": nnRPRSpanStatsOutClassCFrames,
       "nnRPRSpanStatsOutClassCOctets": nnRPRSpanStatsOutClassCOctets,
       "nnRPRSpanPassThruCounters": nnRPRSpanPassThruCounters,
       "nnRPRSpanPassThruCountersStatsTable": nnRPRSpanPassThruCountersStatsTable,
       "nnRPRSpanPassThruCountersStatsEntry": nnRPRSpanPassThruCountersStatsEntry,
       "nnRPRSpanStatsPtIfIndex": nnRPRSpanStatsPtIfIndex,
       "nnRPRSpanPtSpan": nnRPRSpanPtSpan,
       "nnRPRSpanStatsPtClassAFrames": nnRPRSpanStatsPtClassAFrames,
       "nnRPRSpanStatsPtClassAOctets": nnRPRSpanStatsPtClassAOctets,
       "nnRPRSpanStatsPtClassBCirFrames": nnRPRSpanStatsPtClassBCirFrames,
       "nnRPRSpanStatsPtClassBCirOctets": nnRPRSpanStatsPtClassBCirOctets,
       "nnRPRSpanStatsPtClassBEirFrames": nnRPRSpanStatsPtClassBEirFrames,
       "nnRPRSpanStatsPtClassBEirOctets": nnRPRSpanStatsPtClassBEirOctets,
       "nnRPRSpanStatsPtClassCFrames": nnRPRSpanStatsPtClassCFrames,
       "nnRPRSpanStatsPtClassCOctets": nnRPRSpanStatsPtClassCOctets,
       "nnRPRSpanStatsPtClassAFramesDiscards": nnRPRSpanStatsPtClassAFramesDiscards,
       "nnRPRSpanStatsPtClassBCirFramesDiscards": nnRPRSpanStatsPtClassBCirFramesDiscards,
       "nnRPRSpanStatsPtClassBEirFramesDiscards": nnRPRSpanStatsPtClassBEirFramesDiscards,
       "nnRPRSpanStatsPtClassCFramesDiscards": nnRPRSpanStatsPtClassCFramesDiscards,
       "nnRPRSpanErrorCounters": nnRPRSpanErrorCounters,
       "nnRPRSpanErrorCountersStatsTable": nnRPRSpanErrorCountersStatsTable,
       "nnRPRSpanErrorCountersStatsEntry": nnRPRSpanErrorCountersStatsEntry,
       "nnRPRSpanErrorStatsIfIndex": nnRPRSpanErrorStatsIfIndex,
       "nnRPRSpanErrorStatsSpan": nnRPRSpanErrorStatsSpan,
       "nnRPRSpanErrorStatsTtlExpFrames": nnRPRSpanErrorStatsTtlExpFrames,
       "nnRPRSpanErrorStatsTooLongFrames": nnRPRSpanErrorStatsTooLongFrames,
       "nnRPRSpanErrorStatsTooShortFrames": nnRPRSpanErrorStatsTooShortFrames,
       "nnRPRSpanErrorStatsBadHecFrames": nnRPRSpanErrorStatsBadHecFrames,
       "nnRPRSpanErrorStatsBadFcsFrames": nnRPRSpanErrorStatsBadFcsFrames,
       "nnRPRSpanErrorStatsSelfSrcUcastFrames": nnRPRSpanErrorStatsSelfSrcUcastFrames,
       "nnRPRSpanErrorStatsPmdAbortFrames": nnRPRSpanErrorStatsPmdAbortFrames,
       "nnRPRSpanErrorStatsBadAddrFrames": nnRPRSpanErrorStatsBadAddrFrames,
       "nnRPRSpanErrorStatsBadParityFrames": nnRPRSpanErrorStatsBadParityFrames,
       "nnRPRSpanErrorStatsScffErrors": nnRPRSpanErrorStatsScffErrors,
       "nnRPRClientCounters": nnRPRClientCounters,
       "nnRPRClientCountersStatsTable": nnRPRClientCountersStatsTable,
       "nnRPRClientCountersStatsEntry": nnRPRClientCountersStatsEntry,
       "nnRPRClientStatsIfIndex": nnRPRClientStatsIfIndex,
       "nnRPRClientStatsInUcastClassAFrames": nnRPRClientStatsInUcastClassAFrames,
       "nnRPRClientStatsInUcastClassAOctets": nnRPRClientStatsInUcastClassAOctets,
       "nnRPRClientStatsInUcastClassBCirFrames": nnRPRClientStatsInUcastClassBCirFrames,
       "nnRPRClientStatsInUcastClassBCirOctets": nnRPRClientStatsInUcastClassBCirOctets,
       "nnRPRClientStatsInUcastClassBEirFrames": nnRPRClientStatsInUcastClassBEirFrames,
       "nnRPRClientStatsInUcastClassBEirOctets": nnRPRClientStatsInUcastClassBEirOctets,
       "nnRPRClientStatsInUcastClassCFrames": nnRPRClientStatsInUcastClassCFrames,
       "nnRPRClientStatsInUcastClassCOctets": nnRPRClientStatsInUcastClassCOctets,
       "nnRPRClientStatsInMcastClassAFrames": nnRPRClientStatsInMcastClassAFrames,
       "nnRPRClientStatsInMcastClassAOctets": nnRPRClientStatsInMcastClassAOctets,
       "nnRPRClientStatsInMcastClassBCirFrames": nnRPRClientStatsInMcastClassBCirFrames,
       "nnRPRClientStatsInMcastClassBCirOctets": nnRPRClientStatsInMcastClassBCirOctets,
       "nnRPRClientStatsInMcastClassBEirFrames": nnRPRClientStatsInMcastClassBEirFrames,
       "nnRPRClientStatsInMcastClassBEirOctets": nnRPRClientStatsInMcastClassBEirOctets,
       "nnRPRClientStatsInMcastClassCFrames": nnRPRClientStatsInMcastClassCFrames,
       "nnRPRClientStatsInMcastClassCOctets": nnRPRClientStatsInMcastClassCOctets,
       "nnRPRClientStatsOutUcastClassAFrames": nnRPRClientStatsOutUcastClassAFrames,
       "nnRPRClientStatsOutUcastClassAOctets": nnRPRClientStatsOutUcastClassAOctets,
       "nnRPRClientStatsOutUcastClassBCirFrames": nnRPRClientStatsOutUcastClassBCirFrames,
       "nnRPRClientStatsOutUcastClassBCirOctets": nnRPRClientStatsOutUcastClassBCirOctets,
       "nnRPRClientStatsOutUcastClassBEirFrames": nnRPRClientStatsOutUcastClassBEirFrames,
       "nnRPRClientStatsOutUcastClassBEirOctets": nnRPRClientStatsOutUcastClassBEirOctets,
       "nnRPRClientStatsOutUcastClassCFrames": nnRPRClientStatsOutUcastClassCFrames,
       "nnRPRClientStatsOutUcastClassCOctets": nnRPRClientStatsOutUcastClassCOctets,
       "nnRPRClientStatsOutMcastClassAFrames": nnRPRClientStatsOutMcastClassAFrames,
       "nnRPRClientStatsOutMcastClassAOctets": nnRPRClientStatsOutMcastClassAOctets,
       "nnRPRClientStatsOutMcastClassBCirFrames": nnRPRClientStatsOutMcastClassBCirFrames,
       "nnRPRClientStatsOutMcastClassBCirOctets": nnRPRClientStatsOutMcastClassBCirOctets,
       "nnRPRClientStatsOutMcastClassBEirFrames": nnRPRClientStatsOutMcastClassBEirFrames,
       "nnRPRClientStatsOutMcastClassBEirOctets": nnRPRClientStatsOutMcastClassBEirOctets,
       "nnRPRClientStatsOutMcastClassCFrames": nnRPRClientStatsOutMcastClassCFrames,
       "nnRPRClientStatsOutMcastClassCOctets": nnRPRClientStatsOutMcastClassCOctets,
       "nnRPRClientCtrlCounters": nnRPRClientCtrlCounters,
       "nnRPRClientCtrlCountersStatsTable": nnRPRClientCtrlCountersStatsTable,
       "nnRPRClientCtrlCountersStatsEntry": nnRPRClientCtrlCountersStatsEntry,
       "nnRPRClientCtrlStatsIfIndex": nnRPRClientCtrlStatsIfIndex,
       "nnRPRClientCtrlStatsInCtrlFrames": nnRPRClientCtrlStatsInCtrlFrames,
       "nnRPRClientCtrlStatsInOamEchoFrames": nnRPRClientCtrlStatsInOamEchoFrames,
       "nnRPRClientCtrlStatsInOamOrgFrames": nnRPRClientCtrlStatsInOamOrgFrames,
       "nnRPRClientCtrlStatsInTopoAtdFrames": nnRPRClientCtrlStatsInTopoAtdFrames,
       "nnRPRClientCtrlStatsInTopoTpFrames": nnRPRClientCtrlStatsInTopoTpFrames,
       "nnRPRClientCtrlStatsOutCtrlFrames": nnRPRClientCtrlStatsOutCtrlFrames,
       "nnRPRClientCtrlStatsOutOamEchoFrames": nnRPRClientCtrlStatsOutOamEchoFrames,
       "nnRPRClientCtrlStatsOutOamOrgFrames": nnRPRClientCtrlStatsOutOamOrgFrames,
       "nnRPRClientCtrlStatsOutTopoAtdFrames": nnRPRClientCtrlStatsOutTopoAtdFrames,
       "nnRPRClientCtrlStatsOutTopoTpFrames": nnRPRClientCtrlStatsOutTopoTpFrames}
)
