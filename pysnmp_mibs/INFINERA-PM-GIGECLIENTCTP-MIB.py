# SNMP MIB module (INFINERA-PM-GIGECLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-GIGECLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:43 2025
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

(HCPerfIntervalCount,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfIntervalCount")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(perfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "perfMon")

(FloatHundredths,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnServiceType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gigeClientCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    gigeClientCtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GigeClientCtpPmRealTable_Object = MibTable
gigeClientCtpPmRealTable = _GigeClientCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTable.setStatus("current")
_GigeClientCtpPmRealEntry_Object = MibTableRow
gigeClientCtpPmRealEntry = _GigeClientCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1)
)
gigeClientCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gigeClientCtpPmRealEntry.setStatus("current")
_GigeClientCtpPmRealRxLU_Type = FloatHundredths
_GigeClientCtpPmRealRxLU_Object = MibTableColumn
gigeClientCtpPmRealRxLU = _GigeClientCtpPmRealRxLU_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 1),
    _GigeClientCtpPmRealRxLU_Type()
)
gigeClientCtpPmRealRxLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxLU.setStatus("current")
_GigeClientCtpPmRealRxPcsICG_Type = Counter64
_GigeClientCtpPmRealRxPcsICG_Object = MibTableColumn
gigeClientCtpPmRealRxPcsICG = _GigeClientCtpPmRealRxPcsICG_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 2),
    _GigeClientCtpPmRealRxPcsICG_Type()
)
gigeClientCtpPmRealRxPcsICG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxPcsICG.setStatus("current")
_GigeClientCtpPmRealRxPcsES_Type = Integer32
_GigeClientCtpPmRealRxPcsES_Object = MibTableColumn
gigeClientCtpPmRealRxPcsES = _GigeClientCtpPmRealRxPcsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 3),
    _GigeClientCtpPmRealRxPcsES_Type()
)
gigeClientCtpPmRealRxPcsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxPcsES.setStatus("current")
_GigeClientCtpPmRealRxPcsSES_Type = Integer32
_GigeClientCtpPmRealRxPcsSES_Object = MibTableColumn
gigeClientCtpPmRealRxPcsSES = _GigeClientCtpPmRealRxPcsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 4),
    _GigeClientCtpPmRealRxPcsSES_Type()
)
gigeClientCtpPmRealRxPcsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxPcsSES.setStatus("current")
_GigeClientCtpPmRealRxPcsSESS_Type = Integer32
_GigeClientCtpPmRealRxPcsSESS_Object = MibTableColumn
gigeClientCtpPmRealRxPcsSESS = _GigeClientCtpPmRealRxPcsSESS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 5),
    _GigeClientCtpPmRealRxPcsSESS_Type()
)
gigeClientCtpPmRealRxPcsSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxPcsSESS.setStatus("current")
_GigeClientCtpPmRealTxPcsICG_Type = Counter64
_GigeClientCtpPmRealTxPcsICG_Object = MibTableColumn
gigeClientCtpPmRealTxPcsICG = _GigeClientCtpPmRealTxPcsICG_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 6),
    _GigeClientCtpPmRealTxPcsICG_Type()
)
gigeClientCtpPmRealTxPcsICG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxPcsICG.setStatus("current")
_GigeClientCtpPmRealTxPcsES_Type = Integer32
_GigeClientCtpPmRealTxPcsES_Object = MibTableColumn
gigeClientCtpPmRealTxPcsES = _GigeClientCtpPmRealTxPcsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 7),
    _GigeClientCtpPmRealTxPcsES_Type()
)
gigeClientCtpPmRealTxPcsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxPcsES.setStatus("current")
_GigeClientCtpPmRealTxPcsSES_Type = Integer32
_GigeClientCtpPmRealTxPcsSES_Object = MibTableColumn
gigeClientCtpPmRealTxPcsSES = _GigeClientCtpPmRealTxPcsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 8),
    _GigeClientCtpPmRealTxPcsSES_Type()
)
gigeClientCtpPmRealTxPcsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxPcsSES.setStatus("current")
_GigeClientCtpPmRealTxPcsSESS_Type = Integer32
_GigeClientCtpPmRealTxPcsSESS_Object = MibTableColumn
gigeClientCtpPmRealTxPcsSESS = _GigeClientCtpPmRealTxPcsSESS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 9),
    _GigeClientCtpPmRealTxPcsSESS_Type()
)
gigeClientCtpPmRealTxPcsSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxPcsSESS.setStatus("current")
_GigeClientCtpPmRealRxPackets_Type = Counter64
_GigeClientCtpPmRealRxPackets_Object = MibTableColumn
gigeClientCtpPmRealRxPackets = _GigeClientCtpPmRealRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 10),
    _GigeClientCtpPmRealRxPackets_Type()
)
gigeClientCtpPmRealRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxPackets.setStatus("current")
_GigeClientCtpPmRealRxOctets_Type = Counter64
_GigeClientCtpPmRealRxOctets_Object = MibTableColumn
gigeClientCtpPmRealRxOctets = _GigeClientCtpPmRealRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 11),
    _GigeClientCtpPmRealRxOctets_Type()
)
gigeClientCtpPmRealRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxOctets.setStatus("current")
_GigeClientCtpPmRealRxErrOctets_Type = Counter64
_GigeClientCtpPmRealRxErrOctets_Object = MibTableColumn
gigeClientCtpPmRealRxErrOctets = _GigeClientCtpPmRealRxErrOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 12),
    _GigeClientCtpPmRealRxErrOctets_Type()
)
gigeClientCtpPmRealRxErrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxErrOctets.setStatus("current")
_GigeClientCtpPmRealRxJabbers_Type = Counter64
_GigeClientCtpPmRealRxJabbers_Object = MibTableColumn
gigeClientCtpPmRealRxJabbers = _GigeClientCtpPmRealRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 13),
    _GigeClientCtpPmRealRxJabbers_Type()
)
gigeClientCtpPmRealRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxJabbers.setStatus("current")
_GigeClientCtpPmRealRxFragments_Type = Counter64
_GigeClientCtpPmRealRxFragments_Object = MibTableColumn
gigeClientCtpPmRealRxFragments = _GigeClientCtpPmRealRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 14),
    _GigeClientCtpPmRealRxFragments_Type()
)
gigeClientCtpPmRealRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxFragments.setStatus("current")
_GigeClientCtpPmRealRxCrcAlignedErr_Type = Counter64
_GigeClientCtpPmRealRxCrcAlignedErr_Object = MibTableColumn
gigeClientCtpPmRealRxCrcAlignedErr = _GigeClientCtpPmRealRxCrcAlignedErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 15),
    _GigeClientCtpPmRealRxCrcAlignedErr_Type()
)
gigeClientCtpPmRealRxCrcAlignedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCrcAlignedErr.setStatus("current")
_GigeClientCtpPmRealRxUndersized_Type = Counter64
_GigeClientCtpPmRealRxUndersized_Object = MibTableColumn
gigeClientCtpPmRealRxUndersized = _GigeClientCtpPmRealRxUndersized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 16),
    _GigeClientCtpPmRealRxUndersized_Type()
)
gigeClientCtpPmRealRxUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxUndersized.setStatus("current")
_GigeClientCtpPmRealRxOversized_Type = Counter64
_GigeClientCtpPmRealRxOversized_Object = MibTableColumn
gigeClientCtpPmRealRxOversized = _GigeClientCtpPmRealRxOversized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 17),
    _GigeClientCtpPmRealRxOversized_Type()
)
gigeClientCtpPmRealRxOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxOversized.setStatus("current")
_GigeClientCtpPmRealRxJabberSecs_Type = Integer32
_GigeClientCtpPmRealRxJabberSecs_Object = MibTableColumn
gigeClientCtpPmRealRxJabberSecs = _GigeClientCtpPmRealRxJabberSecs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 18),
    _GigeClientCtpPmRealRxJabberSecs_Type()
)
gigeClientCtpPmRealRxJabberSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxJabberSecs.setStatus("current")
_GigeClientCtpPmRealRxMacSES_Type = Integer32
_GigeClientCtpPmRealRxMacSES_Object = MibTableColumn
gigeClientCtpPmRealRxMacSES = _GigeClientCtpPmRealRxMacSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 19),
    _GigeClientCtpPmRealRxMacSES_Type()
)
gigeClientCtpPmRealRxMacSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxMacSES.setStatus("current")
_GigeClientCtpPmRealRxBroadcastPkts_Type = Counter64
_GigeClientCtpPmRealRxBroadcastPkts_Object = MibTableColumn
gigeClientCtpPmRealRxBroadcastPkts = _GigeClientCtpPmRealRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 20),
    _GigeClientCtpPmRealRxBroadcastPkts_Type()
)
gigeClientCtpPmRealRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxBroadcastPkts.setStatus("current")
_GigeClientCtpPmRealRxMulticastPkts_Type = Counter64
_GigeClientCtpPmRealRxMulticastPkts_Object = MibTableColumn
gigeClientCtpPmRealRxMulticastPkts = _GigeClientCtpPmRealRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 21),
    _GigeClientCtpPmRealRxMulticastPkts_Type()
)
gigeClientCtpPmRealRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxMulticastPkts.setStatus("current")
_GigeClientCtpPmRealRxInPauseFrames_Type = Counter64
_GigeClientCtpPmRealRxInPauseFrames_Object = MibTableColumn
gigeClientCtpPmRealRxInPauseFrames = _GigeClientCtpPmRealRxInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 22),
    _GigeClientCtpPmRealRxInPauseFrames_Type()
)
gigeClientCtpPmRealRxInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxInPauseFrames.setStatus("current")
_GigeClientCtpPmRealTxLU_Type = FloatHundredths
_GigeClientCtpPmRealTxLU_Object = MibTableColumn
gigeClientCtpPmRealTxLU = _GigeClientCtpPmRealTxLU_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 23),
    _GigeClientCtpPmRealTxLU_Type()
)
gigeClientCtpPmRealTxLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxLU.setStatus("current")
_GigeClientCtpPmRealTxPackets_Type = Counter64
_GigeClientCtpPmRealTxPackets_Object = MibTableColumn
gigeClientCtpPmRealTxPackets = _GigeClientCtpPmRealTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 24),
    _GigeClientCtpPmRealTxPackets_Type()
)
gigeClientCtpPmRealTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxPackets.setStatus("current")
_GigeClientCtpPmRealTxOctets_Type = Counter64
_GigeClientCtpPmRealTxOctets_Object = MibTableColumn
gigeClientCtpPmRealTxOctets = _GigeClientCtpPmRealTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 25),
    _GigeClientCtpPmRealTxOctets_Type()
)
gigeClientCtpPmRealTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxOctets.setStatus("current")
_GigeClientCtpPmRealTxErrOctets_Type = Counter64
_GigeClientCtpPmRealTxErrOctets_Object = MibTableColumn
gigeClientCtpPmRealTxErrOctets = _GigeClientCtpPmRealTxErrOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 26),
    _GigeClientCtpPmRealTxErrOctets_Type()
)
gigeClientCtpPmRealTxErrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxErrOctets.setStatus("current")
_GigeClientCtpPmRealTxJabbers_Type = Counter64
_GigeClientCtpPmRealTxJabbers_Object = MibTableColumn
gigeClientCtpPmRealTxJabbers = _GigeClientCtpPmRealTxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 27),
    _GigeClientCtpPmRealTxJabbers_Type()
)
gigeClientCtpPmRealTxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxJabbers.setStatus("current")
_GigeClientCtpPmRealTxFragments_Type = Counter64
_GigeClientCtpPmRealTxFragments_Object = MibTableColumn
gigeClientCtpPmRealTxFragments = _GigeClientCtpPmRealTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 28),
    _GigeClientCtpPmRealTxFragments_Type()
)
gigeClientCtpPmRealTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxFragments.setStatus("current")
_GigeClientCtpPmRealTxCrcAlignedErr_Type = Counter64
_GigeClientCtpPmRealTxCrcAlignedErr_Object = MibTableColumn
gigeClientCtpPmRealTxCrcAlignedErr = _GigeClientCtpPmRealTxCrcAlignedErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 29),
    _GigeClientCtpPmRealTxCrcAlignedErr_Type()
)
gigeClientCtpPmRealTxCrcAlignedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCrcAlignedErr.setStatus("current")
_GigeClientCtpPmRealTxUndersized_Type = Counter64
_GigeClientCtpPmRealTxUndersized_Object = MibTableColumn
gigeClientCtpPmRealTxUndersized = _GigeClientCtpPmRealTxUndersized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 30),
    _GigeClientCtpPmRealTxUndersized_Type()
)
gigeClientCtpPmRealTxUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxUndersized.setStatus("current")
_GigeClientCtpPmRealTxOversized_Type = Counter64
_GigeClientCtpPmRealTxOversized_Object = MibTableColumn
gigeClientCtpPmRealTxOversized = _GigeClientCtpPmRealTxOversized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 31),
    _GigeClientCtpPmRealTxOversized_Type()
)
gigeClientCtpPmRealTxOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxOversized.setStatus("current")
_GigeClientCtpPmRealTxJabberSecs_Type = Integer32
_GigeClientCtpPmRealTxJabberSecs_Object = MibTableColumn
gigeClientCtpPmRealTxJabberSecs = _GigeClientCtpPmRealTxJabberSecs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 32),
    _GigeClientCtpPmRealTxJabberSecs_Type()
)
gigeClientCtpPmRealTxJabberSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxJabberSecs.setStatus("current")
_GigeClientCtpPmRealTxMacSES_Type = Integer32
_GigeClientCtpPmRealTxMacSES_Object = MibTableColumn
gigeClientCtpPmRealTxMacSES = _GigeClientCtpPmRealTxMacSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 33),
    _GigeClientCtpPmRealTxMacSES_Type()
)
gigeClientCtpPmRealTxMacSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxMacSES.setStatus("current")
_GigeClientCtpPmRealTxBroadcastPkts_Type = Counter64
_GigeClientCtpPmRealTxBroadcastPkts_Object = MibTableColumn
gigeClientCtpPmRealTxBroadcastPkts = _GigeClientCtpPmRealTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 34),
    _GigeClientCtpPmRealTxBroadcastPkts_Type()
)
gigeClientCtpPmRealTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxBroadcastPkts.setStatus("current")
_GigeClientCtpPmRealTxMulticastPkts_Type = Counter64
_GigeClientCtpPmRealTxMulticastPkts_Object = MibTableColumn
gigeClientCtpPmRealTxMulticastPkts = _GigeClientCtpPmRealTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 35),
    _GigeClientCtpPmRealTxMulticastPkts_Type()
)
gigeClientCtpPmRealTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxMulticastPkts.setStatus("current")
_GigeClientCtpPmRealTxOutPauseFrames_Type = Counter64
_GigeClientCtpPmRealTxOutPauseFrames_Object = MibTableColumn
gigeClientCtpPmRealTxOutPauseFrames = _GigeClientCtpPmRealTxOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 36),
    _GigeClientCtpPmRealTxOutPauseFrames_Type()
)
gigeClientCtpPmRealTxOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxOutPauseFrames.setStatus("current")
_GigeClientCtpPmRealRxSize64_Type = Counter64
_GigeClientCtpPmRealRxSize64_Object = MibTableColumn
gigeClientCtpPmRealRxSize64 = _GigeClientCtpPmRealRxSize64_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 37),
    _GigeClientCtpPmRealRxSize64_Type()
)
gigeClientCtpPmRealRxSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxSize64.setStatus("current")
_GigeClientCtpPmRealRxSize65to127_Type = Counter64
_GigeClientCtpPmRealRxSize65to127_Object = MibTableColumn
gigeClientCtpPmRealRxSize65to127 = _GigeClientCtpPmRealRxSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 38),
    _GigeClientCtpPmRealRxSize65to127_Type()
)
gigeClientCtpPmRealRxSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxSize65to127.setStatus("current")
_GigeClientCtpPmRealRxSize128to255_Type = Counter64
_GigeClientCtpPmRealRxSize128to255_Object = MibTableColumn
gigeClientCtpPmRealRxSize128to255 = _GigeClientCtpPmRealRxSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 39),
    _GigeClientCtpPmRealRxSize128to255_Type()
)
gigeClientCtpPmRealRxSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxSize128to255.setStatus("current")
_GigeClientCtpPmRealRxSize256to511_Type = Counter64
_GigeClientCtpPmRealRxSize256to511_Object = MibTableColumn
gigeClientCtpPmRealRxSize256to511 = _GigeClientCtpPmRealRxSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 40),
    _GigeClientCtpPmRealRxSize256to511_Type()
)
gigeClientCtpPmRealRxSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxSize256to511.setStatus("current")
_GigeClientCtpPmRealRxSize512to1023_Type = Counter64
_GigeClientCtpPmRealRxSize512to1023_Object = MibTableColumn
gigeClientCtpPmRealRxSize512to1023 = _GigeClientCtpPmRealRxSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 41),
    _GigeClientCtpPmRealRxSize512to1023_Type()
)
gigeClientCtpPmRealRxSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxSize512to1023.setStatus("current")
_GigeClientCtpPmRealRxSize1024to1518_Type = Counter64
_GigeClientCtpPmRealRxSize1024to1518_Object = MibTableColumn
gigeClientCtpPmRealRxSize1024to1518 = _GigeClientCtpPmRealRxSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 42),
    _GigeClientCtpPmRealRxSize1024to1518_Type()
)
gigeClientCtpPmRealRxSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxSize1024to1518.setStatus("current")
_GigeClientCtpPmRealRxSize1519toJumbo_Type = Counter64
_GigeClientCtpPmRealRxSize1519toJumbo_Object = MibTableColumn
gigeClientCtpPmRealRxSize1519toJumbo = _GigeClientCtpPmRealRxSize1519toJumbo_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 43),
    _GigeClientCtpPmRealRxSize1519toJumbo_Type()
)
gigeClientCtpPmRealRxSize1519toJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxSize1519toJumbo.setStatus("current")
_GigeClientCtpPmRealTxSize64_Type = Counter64
_GigeClientCtpPmRealTxSize64_Object = MibTableColumn
gigeClientCtpPmRealTxSize64 = _GigeClientCtpPmRealTxSize64_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 44),
    _GigeClientCtpPmRealTxSize64_Type()
)
gigeClientCtpPmRealTxSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxSize64.setStatus("current")
_GigeClientCtpPmRealTxSize65to127_Type = Counter64
_GigeClientCtpPmRealTxSize65to127_Object = MibTableColumn
gigeClientCtpPmRealTxSize65to127 = _GigeClientCtpPmRealTxSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 45),
    _GigeClientCtpPmRealTxSize65to127_Type()
)
gigeClientCtpPmRealTxSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxSize65to127.setStatus("current")
_GigeClientCtpPmRealTxSize128to255_Type = Counter64
_GigeClientCtpPmRealTxSize128to255_Object = MibTableColumn
gigeClientCtpPmRealTxSize128to255 = _GigeClientCtpPmRealTxSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 46),
    _GigeClientCtpPmRealTxSize128to255_Type()
)
gigeClientCtpPmRealTxSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxSize128to255.setStatus("current")
_GigeClientCtpPmRealTxSize256to511_Type = Counter64
_GigeClientCtpPmRealTxSize256to511_Object = MibTableColumn
gigeClientCtpPmRealTxSize256to511 = _GigeClientCtpPmRealTxSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 47),
    _GigeClientCtpPmRealTxSize256to511_Type()
)
gigeClientCtpPmRealTxSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxSize256to511.setStatus("current")
_GigeClientCtpPmRealTxSize512to1023_Type = Counter64
_GigeClientCtpPmRealTxSize512to1023_Object = MibTableColumn
gigeClientCtpPmRealTxSize512to1023 = _GigeClientCtpPmRealTxSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 48),
    _GigeClientCtpPmRealTxSize512to1023_Type()
)
gigeClientCtpPmRealTxSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxSize512to1023.setStatus("current")
_GigeClientCtpPmRealTxSize1024to1518_Type = Counter64
_GigeClientCtpPmRealTxSize1024to1518_Object = MibTableColumn
gigeClientCtpPmRealTxSize1024to1518 = _GigeClientCtpPmRealTxSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 49),
    _GigeClientCtpPmRealTxSize1024to1518_Type()
)
gigeClientCtpPmRealTxSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxSize1024to1518.setStatus("current")
_GigeClientCtpPmRealTxSize1519toJumbo_Type = Counter64
_GigeClientCtpPmRealTxSize1519toJumbo_Object = MibTableColumn
gigeClientCtpPmRealTxSize1519toJumbo = _GigeClientCtpPmRealTxSize1519toJumbo_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 50),
    _GigeClientCtpPmRealTxSize1519toJumbo_Type()
)
gigeClientCtpPmRealTxSize1519toJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxSize1519toJumbo.setStatus("current")
_GigeClientCtpPmRealCktId_Type = DisplayString
_GigeClientCtpPmRealCktId_Object = MibTableColumn
gigeClientCtpPmRealCktId = _GigeClientCtpPmRealCktId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 51),
    _GigeClientCtpPmRealCktId_Type()
)
gigeClientCtpPmRealCktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealCktId.setStatus("current")
_GigeClientCtpPmRealLineTestSigSyncErr_Type = Integer32
_GigeClientCtpPmRealLineTestSigSyncErr_Object = MibTableColumn
gigeClientCtpPmRealLineTestSigSyncErr = _GigeClientCtpPmRealLineTestSigSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 52),
    _GigeClientCtpPmRealLineTestSigSyncErr_Type()
)
gigeClientCtpPmRealLineTestSigSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealLineTestSigSyncErr.setStatus("current")
_GigeClientCtpPmRealLineTestSigErr_Type = Integer32
_GigeClientCtpPmRealLineTestSigErr_Object = MibTableColumn
gigeClientCtpPmRealLineTestSigErr = _GigeClientCtpPmRealLineTestSigErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 53),
    _GigeClientCtpPmRealLineTestSigErr_Type()
)
gigeClientCtpPmRealLineTestSigErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealLineTestSigErr.setStatus("current")
_GigeClientCtpPmRealTribTestSigSyncErr_Type = Integer32
_GigeClientCtpPmRealTribTestSigSyncErr_Object = MibTableColumn
gigeClientCtpPmRealTribTestSigSyncErr = _GigeClientCtpPmRealTribTestSigSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 54),
    _GigeClientCtpPmRealTribTestSigSyncErr_Type()
)
gigeClientCtpPmRealTribTestSigSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTribTestSigSyncErr.setStatus("current")
_GigeClientCtpPmRealTribTestSigErr_Type = Integer32
_GigeClientCtpPmRealTribTestSigErr_Object = MibTableColumn
gigeClientCtpPmRealTribTestSigErr = _GigeClientCtpPmRealTribTestSigErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 55),
    _GigeClientCtpPmRealTribTestSigErr_Type()
)
gigeClientCtpPmRealTribTestSigErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTribTestSigErr.setStatus("current")
_GigeClientCtpPmRealRxSize1024to1522_Type = Counter64
_GigeClientCtpPmRealRxSize1024to1522_Object = MibTableColumn
gigeClientCtpPmRealRxSize1024to1522 = _GigeClientCtpPmRealRxSize1024to1522_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 56),
    _GigeClientCtpPmRealRxSize1024to1522_Type()
)
gigeClientCtpPmRealRxSize1024to1522.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxSize1024to1522.setStatus("current")
_GigeClientCtpPmRealRxSize1523toJumbo_Type = Counter64
_GigeClientCtpPmRealRxSize1523toJumbo_Object = MibTableColumn
gigeClientCtpPmRealRxSize1523toJumbo = _GigeClientCtpPmRealRxSize1523toJumbo_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 57),
    _GigeClientCtpPmRealRxSize1523toJumbo_Type()
)
gigeClientCtpPmRealRxSize1523toJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxSize1523toJumbo.setStatus("current")
_GigeClientCtpPmRealTxSize1024to1522_Type = Counter64
_GigeClientCtpPmRealTxSize1024to1522_Object = MibTableColumn
gigeClientCtpPmRealTxSize1024to1522 = _GigeClientCtpPmRealTxSize1024to1522_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 58),
    _GigeClientCtpPmRealTxSize1024to1522_Type()
)
gigeClientCtpPmRealTxSize1024to1522.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxSize1024to1522.setStatus("current")
_GigeClientCtpPmRealTxSize1523toJumbo_Type = Counter64
_GigeClientCtpPmRealTxSize1523toJumbo_Object = MibTableColumn
gigeClientCtpPmRealTxSize1523toJumbo = _GigeClientCtpPmRealTxSize1523toJumbo_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 59),
    _GigeClientCtpPmRealTxSize1523toJumbo_Type()
)
gigeClientCtpPmRealTxSize1523toJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxSize1523toJumbo.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs01_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs01_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs01 = _GigeClientCtpPmRealTxCvsPcs01_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 60),
    _GigeClientCtpPmRealTxCvsPcs01_Type()
)
gigeClientCtpPmRealTxCvsPcs01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs01.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs02_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs02_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs02 = _GigeClientCtpPmRealTxCvsPcs02_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 61),
    _GigeClientCtpPmRealTxCvsPcs02_Type()
)
gigeClientCtpPmRealTxCvsPcs02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs02.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs03_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs03_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs03 = _GigeClientCtpPmRealTxCvsPcs03_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 62),
    _GigeClientCtpPmRealTxCvsPcs03_Type()
)
gigeClientCtpPmRealTxCvsPcs03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs03.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs04_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs04_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs04 = _GigeClientCtpPmRealTxCvsPcs04_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 63),
    _GigeClientCtpPmRealTxCvsPcs04_Type()
)
gigeClientCtpPmRealTxCvsPcs04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs04.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs05_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs05_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs05 = _GigeClientCtpPmRealTxCvsPcs05_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 64),
    _GigeClientCtpPmRealTxCvsPcs05_Type()
)
gigeClientCtpPmRealTxCvsPcs05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs05.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs06_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs06_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs06 = _GigeClientCtpPmRealTxCvsPcs06_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 65),
    _GigeClientCtpPmRealTxCvsPcs06_Type()
)
gigeClientCtpPmRealTxCvsPcs06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs06.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs07_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs07_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs07 = _GigeClientCtpPmRealTxCvsPcs07_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 66),
    _GigeClientCtpPmRealTxCvsPcs07_Type()
)
gigeClientCtpPmRealTxCvsPcs07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs07.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs08_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs08_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs08 = _GigeClientCtpPmRealTxCvsPcs08_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 67),
    _GigeClientCtpPmRealTxCvsPcs08_Type()
)
gigeClientCtpPmRealTxCvsPcs08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs08.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs09_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs09_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs09 = _GigeClientCtpPmRealTxCvsPcs09_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 68),
    _GigeClientCtpPmRealTxCvsPcs09_Type()
)
gigeClientCtpPmRealTxCvsPcs09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs09.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs10_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs10_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs10 = _GigeClientCtpPmRealTxCvsPcs10_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 69),
    _GigeClientCtpPmRealTxCvsPcs10_Type()
)
gigeClientCtpPmRealTxCvsPcs10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs10.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs11_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs11_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs11 = _GigeClientCtpPmRealTxCvsPcs11_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 70),
    _GigeClientCtpPmRealTxCvsPcs11_Type()
)
gigeClientCtpPmRealTxCvsPcs11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs11.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs12_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs12_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs12 = _GigeClientCtpPmRealTxCvsPcs12_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 71),
    _GigeClientCtpPmRealTxCvsPcs12_Type()
)
gigeClientCtpPmRealTxCvsPcs12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs12.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs13_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs13_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs13 = _GigeClientCtpPmRealTxCvsPcs13_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 72),
    _GigeClientCtpPmRealTxCvsPcs13_Type()
)
gigeClientCtpPmRealTxCvsPcs13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs13.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs14_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs14_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs14 = _GigeClientCtpPmRealTxCvsPcs14_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 73),
    _GigeClientCtpPmRealTxCvsPcs14_Type()
)
gigeClientCtpPmRealTxCvsPcs14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs14.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs15_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs15_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs15 = _GigeClientCtpPmRealTxCvsPcs15_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 74),
    _GigeClientCtpPmRealTxCvsPcs15_Type()
)
gigeClientCtpPmRealTxCvsPcs15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs15.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs16_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs16_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs16 = _GigeClientCtpPmRealTxCvsPcs16_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 75),
    _GigeClientCtpPmRealTxCvsPcs16_Type()
)
gigeClientCtpPmRealTxCvsPcs16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs16.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs17_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs17_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs17 = _GigeClientCtpPmRealTxCvsPcs17_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 76),
    _GigeClientCtpPmRealTxCvsPcs17_Type()
)
gigeClientCtpPmRealTxCvsPcs17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs17.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs18_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs18_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs18 = _GigeClientCtpPmRealTxCvsPcs18_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 77),
    _GigeClientCtpPmRealTxCvsPcs18_Type()
)
gigeClientCtpPmRealTxCvsPcs18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs18.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs19_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs19_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs19 = _GigeClientCtpPmRealTxCvsPcs19_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 78),
    _GigeClientCtpPmRealTxCvsPcs19_Type()
)
gigeClientCtpPmRealTxCvsPcs19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs19.setStatus("current")
_GigeClientCtpPmRealTxCvsPcs20_Type = Integer32
_GigeClientCtpPmRealTxCvsPcs20_Object = MibTableColumn
gigeClientCtpPmRealTxCvsPcs20 = _GigeClientCtpPmRealTxCvsPcs20_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 79),
    _GigeClientCtpPmRealTxCvsPcs20_Type()
)
gigeClientCtpPmRealTxCvsPcs20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealTxCvsPcs20.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs01_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs01_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs01 = _GigeClientCtpPmRealRxCvsPcs01_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 80),
    _GigeClientCtpPmRealRxCvsPcs01_Type()
)
gigeClientCtpPmRealRxCvsPcs01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs01.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs02_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs02_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs02 = _GigeClientCtpPmRealRxCvsPcs02_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 81),
    _GigeClientCtpPmRealRxCvsPcs02_Type()
)
gigeClientCtpPmRealRxCvsPcs02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs02.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs03_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs03_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs03 = _GigeClientCtpPmRealRxCvsPcs03_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 82),
    _GigeClientCtpPmRealRxCvsPcs03_Type()
)
gigeClientCtpPmRealRxCvsPcs03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs03.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs04_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs04_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs04 = _GigeClientCtpPmRealRxCvsPcs04_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 83),
    _GigeClientCtpPmRealRxCvsPcs04_Type()
)
gigeClientCtpPmRealRxCvsPcs04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs04.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs05_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs05_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs05 = _GigeClientCtpPmRealRxCvsPcs05_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 84),
    _GigeClientCtpPmRealRxCvsPcs05_Type()
)
gigeClientCtpPmRealRxCvsPcs05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs05.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs06_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs06_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs06 = _GigeClientCtpPmRealRxCvsPcs06_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 85),
    _GigeClientCtpPmRealRxCvsPcs06_Type()
)
gigeClientCtpPmRealRxCvsPcs06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs06.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs07_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs07_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs07 = _GigeClientCtpPmRealRxCvsPcs07_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 86),
    _GigeClientCtpPmRealRxCvsPcs07_Type()
)
gigeClientCtpPmRealRxCvsPcs07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs07.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs08_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs08_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs08 = _GigeClientCtpPmRealRxCvsPcs08_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 87),
    _GigeClientCtpPmRealRxCvsPcs08_Type()
)
gigeClientCtpPmRealRxCvsPcs08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs08.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs09_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs09_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs09 = _GigeClientCtpPmRealRxCvsPcs09_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 88),
    _GigeClientCtpPmRealRxCvsPcs09_Type()
)
gigeClientCtpPmRealRxCvsPcs09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs09.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs10_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs10_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs10 = _GigeClientCtpPmRealRxCvsPcs10_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 89),
    _GigeClientCtpPmRealRxCvsPcs10_Type()
)
gigeClientCtpPmRealRxCvsPcs10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs10.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs11_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs11_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs11 = _GigeClientCtpPmRealRxCvsPcs11_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 90),
    _GigeClientCtpPmRealRxCvsPcs11_Type()
)
gigeClientCtpPmRealRxCvsPcs11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs11.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs12_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs12_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs12 = _GigeClientCtpPmRealRxCvsPcs12_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 91),
    _GigeClientCtpPmRealRxCvsPcs12_Type()
)
gigeClientCtpPmRealRxCvsPcs12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs12.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs13_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs13_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs13 = _GigeClientCtpPmRealRxCvsPcs13_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 92),
    _GigeClientCtpPmRealRxCvsPcs13_Type()
)
gigeClientCtpPmRealRxCvsPcs13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs13.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs14_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs14_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs14 = _GigeClientCtpPmRealRxCvsPcs14_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 93),
    _GigeClientCtpPmRealRxCvsPcs14_Type()
)
gigeClientCtpPmRealRxCvsPcs14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs14.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs15_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs15_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs15 = _GigeClientCtpPmRealRxCvsPcs15_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 94),
    _GigeClientCtpPmRealRxCvsPcs15_Type()
)
gigeClientCtpPmRealRxCvsPcs15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs15.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs16_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs16_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs16 = _GigeClientCtpPmRealRxCvsPcs16_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 95),
    _GigeClientCtpPmRealRxCvsPcs16_Type()
)
gigeClientCtpPmRealRxCvsPcs16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs16.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs17_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs17_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs17 = _GigeClientCtpPmRealRxCvsPcs17_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 96),
    _GigeClientCtpPmRealRxCvsPcs17_Type()
)
gigeClientCtpPmRealRxCvsPcs17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs17.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs18_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs18_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs18 = _GigeClientCtpPmRealRxCvsPcs18_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 97),
    _GigeClientCtpPmRealRxCvsPcs18_Type()
)
gigeClientCtpPmRealRxCvsPcs18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs18.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs19_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs19_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs19 = _GigeClientCtpPmRealRxCvsPcs19_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 98),
    _GigeClientCtpPmRealRxCvsPcs19_Type()
)
gigeClientCtpPmRealRxCvsPcs19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs19.setStatus("current")
_GigeClientCtpPmRealRxCvsPcs20_Type = Integer32
_GigeClientCtpPmRealRxCvsPcs20_Object = MibTableColumn
gigeClientCtpPmRealRxCvsPcs20 = _GigeClientCtpPmRealRxCvsPcs20_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 99),
    _GigeClientCtpPmRealRxCvsPcs20_Type()
)
gigeClientCtpPmRealRxCvsPcs20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCvsPcs20.setStatus("current")
_GigeClientCtpPmRealRxErrPackets_Type = Counter64
_GigeClientCtpPmRealRxErrPackets_Object = MibTableColumn
gigeClientCtpPmRealRxErrPackets = _GigeClientCtpPmRealRxErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 100),
    _GigeClientCtpPmRealRxErrPackets_Type()
)
gigeClientCtpPmRealRxErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxErrPackets.setStatus("current")
_GigeClientCtpPmRealRxDiscarded_Type = Counter64
_GigeClientCtpPmRealRxDiscarded_Object = MibTableColumn
gigeClientCtpPmRealRxDiscarded = _GigeClientCtpPmRealRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 101),
    _GigeClientCtpPmRealRxDiscarded_Type()
)
gigeClientCtpPmRealRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxDiscarded.setStatus("current")
_GigeClientCtpPmRealRxCorrectedWords_Type = Integer32
_GigeClientCtpPmRealRxCorrectedWords_Object = MibTableColumn
gigeClientCtpPmRealRxCorrectedWords = _GigeClientCtpPmRealRxCorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 102),
    _GigeClientCtpPmRealRxCorrectedWords_Type()
)
gigeClientCtpPmRealRxCorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCorrectedWords.setStatus("current")
_GigeClientCtpPmRealRxUncorrectedWords_Type = Integer32
_GigeClientCtpPmRealRxUncorrectedWords_Object = MibTableColumn
gigeClientCtpPmRealRxUncorrectedWords = _GigeClientCtpPmRealRxUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 103),
    _GigeClientCtpPmRealRxUncorrectedWords_Type()
)
gigeClientCtpPmRealRxUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxUncorrectedWords.setStatus("current")
_GigeClientCtpPmRealRxCorrectedBit_Type = Integer32
_GigeClientCtpPmRealRxCorrectedBit_Object = MibTableColumn
gigeClientCtpPmRealRxCorrectedBit = _GigeClientCtpPmRealRxCorrectedBit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 1, 1, 104),
    _GigeClientCtpPmRealRxCorrectedBit_Type()
)
gigeClientCtpPmRealRxCorrectedBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRealRxCorrectedBit.setStatus("current")
_GigeClientCtpPmTable_Object = MibTable
gigeClientCtpPmTable = _GigeClientCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2)
)
if mibBuilder.loadTexts:
    gigeClientCtpPmTable.setStatus("current")
_GigeClientCtpPmEntry_Object = MibTableRow
gigeClientCtpPmEntry = _GigeClientCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1)
)
gigeClientCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmSampleDuration"),
    (0, "INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    gigeClientCtpPmEntry.setStatus("current")


class _GigeClientCtpPmTimestamp_Type(Integer32):
    """Custom type gigeClientCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GigeClientCtpPmTimestamp_Type.__name__ = "Integer32"
_GigeClientCtpPmTimestamp_Object = MibTableColumn
gigeClientCtpPmTimestamp = _GigeClientCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 1),
    _GigeClientCtpPmTimestamp_Type()
)
gigeClientCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gigeClientCtpPmTimestamp.setStatus("current")


class _GigeClientCtpPmSampleDuration_Type(Integer32):
    """Custom type gigeClientCtpPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_GigeClientCtpPmSampleDuration_Type.__name__ = "Integer32"
_GigeClientCtpPmSampleDuration_Object = MibTableColumn
gigeClientCtpPmSampleDuration = _GigeClientCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 2),
    _GigeClientCtpPmSampleDuration_Type()
)
gigeClientCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gigeClientCtpPmSampleDuration.setStatus("current")
_GigeClientCtpPmValidity_Type = TruthValue
_GigeClientCtpPmValidity_Object = MibTableColumn
gigeClientCtpPmValidity = _GigeClientCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 3),
    _GigeClientCtpPmValidity_Type()
)
gigeClientCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmValidity.setStatus("current")
_GigeClientCtpPmRxPcsICG_Type = HCPerfIntervalCount
_GigeClientCtpPmRxPcsICG_Object = MibTableColumn
gigeClientCtpPmRxPcsICG = _GigeClientCtpPmRxPcsICG_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 4),
    _GigeClientCtpPmRxPcsICG_Type()
)
gigeClientCtpPmRxPcsICG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxPcsICG.setStatus("current")
_GigeClientCtpPmRxPcsES_Type = Integer32
_GigeClientCtpPmRxPcsES_Object = MibTableColumn
gigeClientCtpPmRxPcsES = _GigeClientCtpPmRxPcsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 5),
    _GigeClientCtpPmRxPcsES_Type()
)
gigeClientCtpPmRxPcsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxPcsES.setStatus("current")
_GigeClientCtpPmRxPcsSES_Type = Integer32
_GigeClientCtpPmRxPcsSES_Object = MibTableColumn
gigeClientCtpPmRxPcsSES = _GigeClientCtpPmRxPcsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 6),
    _GigeClientCtpPmRxPcsSES_Type()
)
gigeClientCtpPmRxPcsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxPcsSES.setStatus("current")
_GigeClientCtpPmRxPcsSESS_Type = Integer32
_GigeClientCtpPmRxPcsSESS_Object = MibTableColumn
gigeClientCtpPmRxPcsSESS = _GigeClientCtpPmRxPcsSESS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 7),
    _GigeClientCtpPmRxPcsSESS_Type()
)
gigeClientCtpPmRxPcsSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxPcsSESS.setStatus("current")
_GigeClientCtpPmTxPcsICG_Type = HCPerfIntervalCount
_GigeClientCtpPmTxPcsICG_Object = MibTableColumn
gigeClientCtpPmTxPcsICG = _GigeClientCtpPmTxPcsICG_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 8),
    _GigeClientCtpPmTxPcsICG_Type()
)
gigeClientCtpPmTxPcsICG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxPcsICG.setStatus("current")
_GigeClientCtpPmTxPcsES_Type = Integer32
_GigeClientCtpPmTxPcsES_Object = MibTableColumn
gigeClientCtpPmTxPcsES = _GigeClientCtpPmTxPcsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 9),
    _GigeClientCtpPmTxPcsES_Type()
)
gigeClientCtpPmTxPcsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxPcsES.setStatus("current")
_GigeClientCtpPmTxPcsSES_Type = Integer32
_GigeClientCtpPmTxPcsSES_Object = MibTableColumn
gigeClientCtpPmTxPcsSES = _GigeClientCtpPmTxPcsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 10),
    _GigeClientCtpPmTxPcsSES_Type()
)
gigeClientCtpPmTxPcsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxPcsSES.setStatus("current")
_GigeClientCtpPmTxPcsSESS_Type = Integer32
_GigeClientCtpPmTxPcsSESS_Object = MibTableColumn
gigeClientCtpPmTxPcsSESS = _GigeClientCtpPmTxPcsSESS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 11),
    _GigeClientCtpPmTxPcsSESS_Type()
)
gigeClientCtpPmTxPcsSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxPcsSESS.setStatus("current")
_GigeClientCtpPmRxPackets_Type = HCPerfIntervalCount
_GigeClientCtpPmRxPackets_Object = MibTableColumn
gigeClientCtpPmRxPackets = _GigeClientCtpPmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 12),
    _GigeClientCtpPmRxPackets_Type()
)
gigeClientCtpPmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxPackets.setStatus("current")
_GigeClientCtpPmRxOctets_Type = HCPerfIntervalCount
_GigeClientCtpPmRxOctets_Object = MibTableColumn
gigeClientCtpPmRxOctets = _GigeClientCtpPmRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 13),
    _GigeClientCtpPmRxOctets_Type()
)
gigeClientCtpPmRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxOctets.setStatus("current")
_GigeClientCtpPmRxErrOctets_Type = HCPerfIntervalCount
_GigeClientCtpPmRxErrOctets_Object = MibTableColumn
gigeClientCtpPmRxErrOctets = _GigeClientCtpPmRxErrOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 14),
    _GigeClientCtpPmRxErrOctets_Type()
)
gigeClientCtpPmRxErrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxErrOctets.setStatus("current")
_GigeClientCtpPmRxJabbers_Type = HCPerfIntervalCount
_GigeClientCtpPmRxJabbers_Object = MibTableColumn
gigeClientCtpPmRxJabbers = _GigeClientCtpPmRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 15),
    _GigeClientCtpPmRxJabbers_Type()
)
gigeClientCtpPmRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxJabbers.setStatus("current")
_GigeClientCtpPmRxFragments_Type = HCPerfIntervalCount
_GigeClientCtpPmRxFragments_Object = MibTableColumn
gigeClientCtpPmRxFragments = _GigeClientCtpPmRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 16),
    _GigeClientCtpPmRxFragments_Type()
)
gigeClientCtpPmRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxFragments.setStatus("current")
_GigeClientCtpPmRxCrcAlignedErr_Type = HCPerfIntervalCount
_GigeClientCtpPmRxCrcAlignedErr_Object = MibTableColumn
gigeClientCtpPmRxCrcAlignedErr = _GigeClientCtpPmRxCrcAlignedErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 17),
    _GigeClientCtpPmRxCrcAlignedErr_Type()
)
gigeClientCtpPmRxCrcAlignedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCrcAlignedErr.setStatus("current")
_GigeClientCtpPmRxUndersized_Type = HCPerfIntervalCount
_GigeClientCtpPmRxUndersized_Object = MibTableColumn
gigeClientCtpPmRxUndersized = _GigeClientCtpPmRxUndersized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 18),
    _GigeClientCtpPmRxUndersized_Type()
)
gigeClientCtpPmRxUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxUndersized.setStatus("current")
_GigeClientCtpPmRxOversized_Type = HCPerfIntervalCount
_GigeClientCtpPmRxOversized_Object = MibTableColumn
gigeClientCtpPmRxOversized = _GigeClientCtpPmRxOversized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 19),
    _GigeClientCtpPmRxOversized_Type()
)
gigeClientCtpPmRxOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxOversized.setStatus("current")
_GigeClientCtpPmRxJabberSecs_Type = Integer32
_GigeClientCtpPmRxJabberSecs_Object = MibTableColumn
gigeClientCtpPmRxJabberSecs = _GigeClientCtpPmRxJabberSecs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 20),
    _GigeClientCtpPmRxJabberSecs_Type()
)
gigeClientCtpPmRxJabberSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxJabberSecs.setStatus("current")
_GigeClientCtpPmRxMacSES_Type = Integer32
_GigeClientCtpPmRxMacSES_Object = MibTableColumn
gigeClientCtpPmRxMacSES = _GigeClientCtpPmRxMacSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 21),
    _GigeClientCtpPmRxMacSES_Type()
)
gigeClientCtpPmRxMacSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxMacSES.setStatus("current")
_GigeClientCtpPmRxBroadcastPkts_Type = HCPerfIntervalCount
_GigeClientCtpPmRxBroadcastPkts_Object = MibTableColumn
gigeClientCtpPmRxBroadcastPkts = _GigeClientCtpPmRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 22),
    _GigeClientCtpPmRxBroadcastPkts_Type()
)
gigeClientCtpPmRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxBroadcastPkts.setStatus("current")
_GigeClientCtpPmRxMulticastPkts_Type = HCPerfIntervalCount
_GigeClientCtpPmRxMulticastPkts_Object = MibTableColumn
gigeClientCtpPmRxMulticastPkts = _GigeClientCtpPmRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 23),
    _GigeClientCtpPmRxMulticastPkts_Type()
)
gigeClientCtpPmRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxMulticastPkts.setStatus("current")
_GigeClientCtpPmRxInPauseFrames_Type = HCPerfIntervalCount
_GigeClientCtpPmRxInPauseFrames_Object = MibTableColumn
gigeClientCtpPmRxInPauseFrames = _GigeClientCtpPmRxInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 24),
    _GigeClientCtpPmRxInPauseFrames_Type()
)
gigeClientCtpPmRxInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxInPauseFrames.setStatus("current")
_GigeClientCtpPmTxPackets_Type = HCPerfIntervalCount
_GigeClientCtpPmTxPackets_Object = MibTableColumn
gigeClientCtpPmTxPackets = _GigeClientCtpPmTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 25),
    _GigeClientCtpPmTxPackets_Type()
)
gigeClientCtpPmTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxPackets.setStatus("current")
_GigeClientCtpPmTxOctets_Type = HCPerfIntervalCount
_GigeClientCtpPmTxOctets_Object = MibTableColumn
gigeClientCtpPmTxOctets = _GigeClientCtpPmTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 26),
    _GigeClientCtpPmTxOctets_Type()
)
gigeClientCtpPmTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxOctets.setStatus("current")
_GigeClientCtpPmTxErrOctets_Type = HCPerfIntervalCount
_GigeClientCtpPmTxErrOctets_Object = MibTableColumn
gigeClientCtpPmTxErrOctets = _GigeClientCtpPmTxErrOctets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 27),
    _GigeClientCtpPmTxErrOctets_Type()
)
gigeClientCtpPmTxErrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxErrOctets.setStatus("current")
_GigeClientCtpPmTxJabbers_Type = HCPerfIntervalCount
_GigeClientCtpPmTxJabbers_Object = MibTableColumn
gigeClientCtpPmTxJabbers = _GigeClientCtpPmTxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 28),
    _GigeClientCtpPmTxJabbers_Type()
)
gigeClientCtpPmTxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxJabbers.setStatus("current")
_GigeClientCtpPmTxFragments_Type = HCPerfIntervalCount
_GigeClientCtpPmTxFragments_Object = MibTableColumn
gigeClientCtpPmTxFragments = _GigeClientCtpPmTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 29),
    _GigeClientCtpPmTxFragments_Type()
)
gigeClientCtpPmTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxFragments.setStatus("current")
_GigeClientCtpPmTxCrcAlignedErr_Type = HCPerfIntervalCount
_GigeClientCtpPmTxCrcAlignedErr_Object = MibTableColumn
gigeClientCtpPmTxCrcAlignedErr = _GigeClientCtpPmTxCrcAlignedErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 30),
    _GigeClientCtpPmTxCrcAlignedErr_Type()
)
gigeClientCtpPmTxCrcAlignedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCrcAlignedErr.setStatus("current")
_GigeClientCtpPmTxUndersized_Type = HCPerfIntervalCount
_GigeClientCtpPmTxUndersized_Object = MibTableColumn
gigeClientCtpPmTxUndersized = _GigeClientCtpPmTxUndersized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 31),
    _GigeClientCtpPmTxUndersized_Type()
)
gigeClientCtpPmTxUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxUndersized.setStatus("current")
_GigeClientCtpPmTxOversized_Type = HCPerfIntervalCount
_GigeClientCtpPmTxOversized_Object = MibTableColumn
gigeClientCtpPmTxOversized = _GigeClientCtpPmTxOversized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 32),
    _GigeClientCtpPmTxOversized_Type()
)
gigeClientCtpPmTxOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxOversized.setStatus("current")
_GigeClientCtpPmTxJabberSecs_Type = Integer32
_GigeClientCtpPmTxJabberSecs_Object = MibTableColumn
gigeClientCtpPmTxJabberSecs = _GigeClientCtpPmTxJabberSecs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 33),
    _GigeClientCtpPmTxJabberSecs_Type()
)
gigeClientCtpPmTxJabberSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxJabberSecs.setStatus("current")
_GigeClientCtpPmTxMacSES_Type = Integer32
_GigeClientCtpPmTxMacSES_Object = MibTableColumn
gigeClientCtpPmTxMacSES = _GigeClientCtpPmTxMacSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 34),
    _GigeClientCtpPmTxMacSES_Type()
)
gigeClientCtpPmTxMacSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxMacSES.setStatus("current")
_GigeClientCtpPmTxBroadcastPkts_Type = HCPerfIntervalCount
_GigeClientCtpPmTxBroadcastPkts_Object = MibTableColumn
gigeClientCtpPmTxBroadcastPkts = _GigeClientCtpPmTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 35),
    _GigeClientCtpPmTxBroadcastPkts_Type()
)
gigeClientCtpPmTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxBroadcastPkts.setStatus("current")
_GigeClientCtpPmTxMulticastPkts_Type = HCPerfIntervalCount
_GigeClientCtpPmTxMulticastPkts_Object = MibTableColumn
gigeClientCtpPmTxMulticastPkts = _GigeClientCtpPmTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 36),
    _GigeClientCtpPmTxMulticastPkts_Type()
)
gigeClientCtpPmTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxMulticastPkts.setStatus("current")
_GigeClientCtpPmTxOutPauseFrames_Type = HCPerfIntervalCount
_GigeClientCtpPmTxOutPauseFrames_Object = MibTableColumn
gigeClientCtpPmTxOutPauseFrames = _GigeClientCtpPmTxOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 37),
    _GigeClientCtpPmTxOutPauseFrames_Type()
)
gigeClientCtpPmTxOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxOutPauseFrames.setStatus("current")
_GigeClientCtpPmRxSize64_Type = HCPerfIntervalCount
_GigeClientCtpPmRxSize64_Object = MibTableColumn
gigeClientCtpPmRxSize64 = _GigeClientCtpPmRxSize64_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 38),
    _GigeClientCtpPmRxSize64_Type()
)
gigeClientCtpPmRxSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxSize64.setStatus("current")
_GigeClientCtpPmRxSize65to127_Type = HCPerfIntervalCount
_GigeClientCtpPmRxSize65to127_Object = MibTableColumn
gigeClientCtpPmRxSize65to127 = _GigeClientCtpPmRxSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 39),
    _GigeClientCtpPmRxSize65to127_Type()
)
gigeClientCtpPmRxSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxSize65to127.setStatus("current")
_GigeClientCtpPmRxSize128to255_Type = HCPerfIntervalCount
_GigeClientCtpPmRxSize128to255_Object = MibTableColumn
gigeClientCtpPmRxSize128to255 = _GigeClientCtpPmRxSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 40),
    _GigeClientCtpPmRxSize128to255_Type()
)
gigeClientCtpPmRxSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxSize128to255.setStatus("current")
_GigeClientCtpPmRxSize256to511_Type = HCPerfIntervalCount
_GigeClientCtpPmRxSize256to511_Object = MibTableColumn
gigeClientCtpPmRxSize256to511 = _GigeClientCtpPmRxSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 41),
    _GigeClientCtpPmRxSize256to511_Type()
)
gigeClientCtpPmRxSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxSize256to511.setStatus("current")
_GigeClientCtpPmRxSize512to1023_Type = HCPerfIntervalCount
_GigeClientCtpPmRxSize512to1023_Object = MibTableColumn
gigeClientCtpPmRxSize512to1023 = _GigeClientCtpPmRxSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 42),
    _GigeClientCtpPmRxSize512to1023_Type()
)
gigeClientCtpPmRxSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxSize512to1023.setStatus("current")
_GigeClientCtpPmRxSize1024to1518_Type = HCPerfIntervalCount
_GigeClientCtpPmRxSize1024to1518_Object = MibTableColumn
gigeClientCtpPmRxSize1024to1518 = _GigeClientCtpPmRxSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 43),
    _GigeClientCtpPmRxSize1024to1518_Type()
)
gigeClientCtpPmRxSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxSize1024to1518.setStatus("current")
_GigeClientCtpPmRxSize1519toJumbo_Type = HCPerfIntervalCount
_GigeClientCtpPmRxSize1519toJumbo_Object = MibTableColumn
gigeClientCtpPmRxSize1519toJumbo = _GigeClientCtpPmRxSize1519toJumbo_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 44),
    _GigeClientCtpPmRxSize1519toJumbo_Type()
)
gigeClientCtpPmRxSize1519toJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxSize1519toJumbo.setStatus("current")
_GigeClientCtpPmTxSize64_Type = HCPerfIntervalCount
_GigeClientCtpPmTxSize64_Object = MibTableColumn
gigeClientCtpPmTxSize64 = _GigeClientCtpPmTxSize64_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 45),
    _GigeClientCtpPmTxSize64_Type()
)
gigeClientCtpPmTxSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxSize64.setStatus("current")
_GigeClientCtpPmTxSize65to127_Type = HCPerfIntervalCount
_GigeClientCtpPmTxSize65to127_Object = MibTableColumn
gigeClientCtpPmTxSize65to127 = _GigeClientCtpPmTxSize65to127_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 46),
    _GigeClientCtpPmTxSize65to127_Type()
)
gigeClientCtpPmTxSize65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxSize65to127.setStatus("current")
_GigeClientCtpPmTxSize128to255_Type = HCPerfIntervalCount
_GigeClientCtpPmTxSize128to255_Object = MibTableColumn
gigeClientCtpPmTxSize128to255 = _GigeClientCtpPmTxSize128to255_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 47),
    _GigeClientCtpPmTxSize128to255_Type()
)
gigeClientCtpPmTxSize128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxSize128to255.setStatus("current")
_GigeClientCtpPmTxSize256to511_Type = HCPerfIntervalCount
_GigeClientCtpPmTxSize256to511_Object = MibTableColumn
gigeClientCtpPmTxSize256to511 = _GigeClientCtpPmTxSize256to511_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 48),
    _GigeClientCtpPmTxSize256to511_Type()
)
gigeClientCtpPmTxSize256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxSize256to511.setStatus("current")
_GigeClientCtpPmTxSize512to1023_Type = HCPerfIntervalCount
_GigeClientCtpPmTxSize512to1023_Object = MibTableColumn
gigeClientCtpPmTxSize512to1023 = _GigeClientCtpPmTxSize512to1023_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 49),
    _GigeClientCtpPmTxSize512to1023_Type()
)
gigeClientCtpPmTxSize512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxSize512to1023.setStatus("current")
_GigeClientCtpPmTxSize1024to1518_Type = HCPerfIntervalCount
_GigeClientCtpPmTxSize1024to1518_Object = MibTableColumn
gigeClientCtpPmTxSize1024to1518 = _GigeClientCtpPmTxSize1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 50),
    _GigeClientCtpPmTxSize1024to1518_Type()
)
gigeClientCtpPmTxSize1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxSize1024to1518.setStatus("current")
_GigeClientCtpPmTxSize1519toJumbo_Type = HCPerfIntervalCount
_GigeClientCtpPmTxSize1519toJumbo_Object = MibTableColumn
gigeClientCtpPmTxSize1519toJumbo = _GigeClientCtpPmTxSize1519toJumbo_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 51),
    _GigeClientCtpPmTxSize1519toJumbo_Type()
)
gigeClientCtpPmTxSize1519toJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxSize1519toJumbo.setStatus("current")
_GigeClientCtpPmCktId_Type = DisplayString
_GigeClientCtpPmCktId_Object = MibTableColumn
gigeClientCtpPmCktId = _GigeClientCtpPmCktId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 52),
    _GigeClientCtpPmCktId_Type()
)
gigeClientCtpPmCktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmCktId.setStatus("current")
_GigeClientCtpPmTribTestSigSyncErr_Type = Integer32
_GigeClientCtpPmTribTestSigSyncErr_Object = MibTableColumn
gigeClientCtpPmTribTestSigSyncErr = _GigeClientCtpPmTribTestSigSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 53),
    _GigeClientCtpPmTribTestSigSyncErr_Type()
)
gigeClientCtpPmTribTestSigSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTribTestSigSyncErr.setStatus("current")
_GigeClientCtpPmTribTestSigErr_Type = Integer32
_GigeClientCtpPmTribTestSigErr_Object = MibTableColumn
gigeClientCtpPmTribTestSigErr = _GigeClientCtpPmTribTestSigErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 54),
    _GigeClientCtpPmTribTestSigErr_Type()
)
gigeClientCtpPmTribTestSigErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTribTestSigErr.setStatus("current")
_GigeClientCtpPmPayloadType_Type = InfnServiceType
_GigeClientCtpPmPayloadType_Object = MibTableColumn
gigeClientCtpPmPayloadType = _GigeClientCtpPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 55),
    _GigeClientCtpPmPayloadType_Type()
)
gigeClientCtpPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmPayloadType.setStatus("current")
_GigeClientCtpPmRxSize1024to1522_Type = HCPerfIntervalCount
_GigeClientCtpPmRxSize1024to1522_Object = MibTableColumn
gigeClientCtpPmRxSize1024to1522 = _GigeClientCtpPmRxSize1024to1522_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 56),
    _GigeClientCtpPmRxSize1024to1522_Type()
)
gigeClientCtpPmRxSize1024to1522.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxSize1024to1522.setStatus("current")
_GigeClientCtpPmRxSize1523toJumbo_Type = HCPerfIntervalCount
_GigeClientCtpPmRxSize1523toJumbo_Object = MibTableColumn
gigeClientCtpPmRxSize1523toJumbo = _GigeClientCtpPmRxSize1523toJumbo_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 57),
    _GigeClientCtpPmRxSize1523toJumbo_Type()
)
gigeClientCtpPmRxSize1523toJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxSize1523toJumbo.setStatus("current")
_GigeClientCtpPmTxSize1024to1522_Type = HCPerfIntervalCount
_GigeClientCtpPmTxSize1024to1522_Object = MibTableColumn
gigeClientCtpPmTxSize1024to1522 = _GigeClientCtpPmTxSize1024to1522_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 58),
    _GigeClientCtpPmTxSize1024to1522_Type()
)
gigeClientCtpPmTxSize1024to1522.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxSize1024to1522.setStatus("current")
_GigeClientCtpPmTxSize1523toJumbo_Type = HCPerfIntervalCount
_GigeClientCtpPmTxSize1523toJumbo_Object = MibTableColumn
gigeClientCtpPmTxSize1523toJumbo = _GigeClientCtpPmTxSize1523toJumbo_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 59),
    _GigeClientCtpPmTxSize1523toJumbo_Type()
)
gigeClientCtpPmTxSize1523toJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxSize1523toJumbo.setStatus("current")
_GigeClientCtpPmTxCvsPcs01_Type = Integer32
_GigeClientCtpPmTxCvsPcs01_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs01 = _GigeClientCtpPmTxCvsPcs01_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 60),
    _GigeClientCtpPmTxCvsPcs01_Type()
)
gigeClientCtpPmTxCvsPcs01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs01.setStatus("current")
_GigeClientCtpPmTxCvsPcs02_Type = Integer32
_GigeClientCtpPmTxCvsPcs02_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs02 = _GigeClientCtpPmTxCvsPcs02_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 61),
    _GigeClientCtpPmTxCvsPcs02_Type()
)
gigeClientCtpPmTxCvsPcs02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs02.setStatus("current")
_GigeClientCtpPmTxCvsPcs03_Type = Integer32
_GigeClientCtpPmTxCvsPcs03_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs03 = _GigeClientCtpPmTxCvsPcs03_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 62),
    _GigeClientCtpPmTxCvsPcs03_Type()
)
gigeClientCtpPmTxCvsPcs03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs03.setStatus("current")
_GigeClientCtpPmTxCvsPcs04_Type = Integer32
_GigeClientCtpPmTxCvsPcs04_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs04 = _GigeClientCtpPmTxCvsPcs04_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 63),
    _GigeClientCtpPmTxCvsPcs04_Type()
)
gigeClientCtpPmTxCvsPcs04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs04.setStatus("current")
_GigeClientCtpPmTxCvsPcs05_Type = Integer32
_GigeClientCtpPmTxCvsPcs05_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs05 = _GigeClientCtpPmTxCvsPcs05_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 64),
    _GigeClientCtpPmTxCvsPcs05_Type()
)
gigeClientCtpPmTxCvsPcs05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs05.setStatus("current")
_GigeClientCtpPmTxCvsPcs06_Type = Integer32
_GigeClientCtpPmTxCvsPcs06_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs06 = _GigeClientCtpPmTxCvsPcs06_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 65),
    _GigeClientCtpPmTxCvsPcs06_Type()
)
gigeClientCtpPmTxCvsPcs06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs06.setStatus("current")
_GigeClientCtpPmTxCvsPcs07_Type = Integer32
_GigeClientCtpPmTxCvsPcs07_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs07 = _GigeClientCtpPmTxCvsPcs07_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 66),
    _GigeClientCtpPmTxCvsPcs07_Type()
)
gigeClientCtpPmTxCvsPcs07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs07.setStatus("current")
_GigeClientCtpPmTxCvsPcs08_Type = Integer32
_GigeClientCtpPmTxCvsPcs08_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs08 = _GigeClientCtpPmTxCvsPcs08_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 67),
    _GigeClientCtpPmTxCvsPcs08_Type()
)
gigeClientCtpPmTxCvsPcs08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs08.setStatus("current")
_GigeClientCtpPmTxCvsPcs09_Type = Integer32
_GigeClientCtpPmTxCvsPcs09_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs09 = _GigeClientCtpPmTxCvsPcs09_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 68),
    _GigeClientCtpPmTxCvsPcs09_Type()
)
gigeClientCtpPmTxCvsPcs09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs09.setStatus("current")
_GigeClientCtpPmTxCvsPcs10_Type = Integer32
_GigeClientCtpPmTxCvsPcs10_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs10 = _GigeClientCtpPmTxCvsPcs10_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 69),
    _GigeClientCtpPmTxCvsPcs10_Type()
)
gigeClientCtpPmTxCvsPcs10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs10.setStatus("current")
_GigeClientCtpPmTxCvsPcs11_Type = Integer32
_GigeClientCtpPmTxCvsPcs11_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs11 = _GigeClientCtpPmTxCvsPcs11_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 70),
    _GigeClientCtpPmTxCvsPcs11_Type()
)
gigeClientCtpPmTxCvsPcs11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs11.setStatus("current")
_GigeClientCtpPmTxCvsPcs12_Type = Integer32
_GigeClientCtpPmTxCvsPcs12_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs12 = _GigeClientCtpPmTxCvsPcs12_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 71),
    _GigeClientCtpPmTxCvsPcs12_Type()
)
gigeClientCtpPmTxCvsPcs12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs12.setStatus("current")
_GigeClientCtpPmTxCvsPcs13_Type = Integer32
_GigeClientCtpPmTxCvsPcs13_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs13 = _GigeClientCtpPmTxCvsPcs13_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 72),
    _GigeClientCtpPmTxCvsPcs13_Type()
)
gigeClientCtpPmTxCvsPcs13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs13.setStatus("current")
_GigeClientCtpPmTxCvsPcs14_Type = Integer32
_GigeClientCtpPmTxCvsPcs14_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs14 = _GigeClientCtpPmTxCvsPcs14_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 73),
    _GigeClientCtpPmTxCvsPcs14_Type()
)
gigeClientCtpPmTxCvsPcs14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs14.setStatus("current")
_GigeClientCtpPmTxCvsPcs15_Type = Integer32
_GigeClientCtpPmTxCvsPcs15_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs15 = _GigeClientCtpPmTxCvsPcs15_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 74),
    _GigeClientCtpPmTxCvsPcs15_Type()
)
gigeClientCtpPmTxCvsPcs15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs15.setStatus("current")
_GigeClientCtpPmTxCvsPcs16_Type = Integer32
_GigeClientCtpPmTxCvsPcs16_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs16 = _GigeClientCtpPmTxCvsPcs16_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 75),
    _GigeClientCtpPmTxCvsPcs16_Type()
)
gigeClientCtpPmTxCvsPcs16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs16.setStatus("current")
_GigeClientCtpPmTxCvsPcs17_Type = Integer32
_GigeClientCtpPmTxCvsPcs17_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs17 = _GigeClientCtpPmTxCvsPcs17_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 76),
    _GigeClientCtpPmTxCvsPcs17_Type()
)
gigeClientCtpPmTxCvsPcs17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs17.setStatus("current")
_GigeClientCtpPmTxCvsPcs18_Type = Integer32
_GigeClientCtpPmTxCvsPcs18_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs18 = _GigeClientCtpPmTxCvsPcs18_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 77),
    _GigeClientCtpPmTxCvsPcs18_Type()
)
gigeClientCtpPmTxCvsPcs18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs18.setStatus("current")
_GigeClientCtpPmTxCvsPcs19_Type = Integer32
_GigeClientCtpPmTxCvsPcs19_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs19 = _GigeClientCtpPmTxCvsPcs19_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 78),
    _GigeClientCtpPmTxCvsPcs19_Type()
)
gigeClientCtpPmTxCvsPcs19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs19.setStatus("current")
_GigeClientCtpPmTxCvsPcs20_Type = Integer32
_GigeClientCtpPmTxCvsPcs20_Object = MibTableColumn
gigeClientCtpPmTxCvsPcs20 = _GigeClientCtpPmTxCvsPcs20_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 79),
    _GigeClientCtpPmTxCvsPcs20_Type()
)
gigeClientCtpPmTxCvsPcs20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmTxCvsPcs20.setStatus("current")
_GigeClientCtpPmRxCvsPcs01_Type = Integer32
_GigeClientCtpPmRxCvsPcs01_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs01 = _GigeClientCtpPmRxCvsPcs01_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 80),
    _GigeClientCtpPmRxCvsPcs01_Type()
)
gigeClientCtpPmRxCvsPcs01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs01.setStatus("current")
_GigeClientCtpPmRxCvsPcs02_Type = Integer32
_GigeClientCtpPmRxCvsPcs02_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs02 = _GigeClientCtpPmRxCvsPcs02_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 81),
    _GigeClientCtpPmRxCvsPcs02_Type()
)
gigeClientCtpPmRxCvsPcs02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs02.setStatus("current")
_GigeClientCtpPmRxCvsPcs03_Type = Integer32
_GigeClientCtpPmRxCvsPcs03_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs03 = _GigeClientCtpPmRxCvsPcs03_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 82),
    _GigeClientCtpPmRxCvsPcs03_Type()
)
gigeClientCtpPmRxCvsPcs03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs03.setStatus("current")
_GigeClientCtpPmRxCvsPcs04_Type = Integer32
_GigeClientCtpPmRxCvsPcs04_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs04 = _GigeClientCtpPmRxCvsPcs04_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 83),
    _GigeClientCtpPmRxCvsPcs04_Type()
)
gigeClientCtpPmRxCvsPcs04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs04.setStatus("current")
_GigeClientCtpPmRxCvsPcs05_Type = Integer32
_GigeClientCtpPmRxCvsPcs05_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs05 = _GigeClientCtpPmRxCvsPcs05_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 84),
    _GigeClientCtpPmRxCvsPcs05_Type()
)
gigeClientCtpPmRxCvsPcs05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs05.setStatus("current")
_GigeClientCtpPmRxCvsPcs06_Type = Integer32
_GigeClientCtpPmRxCvsPcs06_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs06 = _GigeClientCtpPmRxCvsPcs06_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 85),
    _GigeClientCtpPmRxCvsPcs06_Type()
)
gigeClientCtpPmRxCvsPcs06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs06.setStatus("current")
_GigeClientCtpPmRxCvsPcs07_Type = Integer32
_GigeClientCtpPmRxCvsPcs07_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs07 = _GigeClientCtpPmRxCvsPcs07_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 86),
    _GigeClientCtpPmRxCvsPcs07_Type()
)
gigeClientCtpPmRxCvsPcs07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs07.setStatus("current")
_GigeClientCtpPmRxCvsPcs08_Type = Integer32
_GigeClientCtpPmRxCvsPcs08_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs08 = _GigeClientCtpPmRxCvsPcs08_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 87),
    _GigeClientCtpPmRxCvsPcs08_Type()
)
gigeClientCtpPmRxCvsPcs08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs08.setStatus("current")
_GigeClientCtpPmRxCvsPcs09_Type = Integer32
_GigeClientCtpPmRxCvsPcs09_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs09 = _GigeClientCtpPmRxCvsPcs09_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 88),
    _GigeClientCtpPmRxCvsPcs09_Type()
)
gigeClientCtpPmRxCvsPcs09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs09.setStatus("current")
_GigeClientCtpPmRxCvsPcs10_Type = Integer32
_GigeClientCtpPmRxCvsPcs10_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs10 = _GigeClientCtpPmRxCvsPcs10_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 89),
    _GigeClientCtpPmRxCvsPcs10_Type()
)
gigeClientCtpPmRxCvsPcs10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs10.setStatus("current")
_GigeClientCtpPmRxCvsPcs11_Type = Integer32
_GigeClientCtpPmRxCvsPcs11_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs11 = _GigeClientCtpPmRxCvsPcs11_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 90),
    _GigeClientCtpPmRxCvsPcs11_Type()
)
gigeClientCtpPmRxCvsPcs11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs11.setStatus("current")
_GigeClientCtpPmRxCvsPcs12_Type = Integer32
_GigeClientCtpPmRxCvsPcs12_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs12 = _GigeClientCtpPmRxCvsPcs12_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 91),
    _GigeClientCtpPmRxCvsPcs12_Type()
)
gigeClientCtpPmRxCvsPcs12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs12.setStatus("current")
_GigeClientCtpPmRxCvsPcs13_Type = Integer32
_GigeClientCtpPmRxCvsPcs13_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs13 = _GigeClientCtpPmRxCvsPcs13_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 92),
    _GigeClientCtpPmRxCvsPcs13_Type()
)
gigeClientCtpPmRxCvsPcs13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs13.setStatus("current")
_GigeClientCtpPmRxCvsPcs14_Type = Integer32
_GigeClientCtpPmRxCvsPcs14_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs14 = _GigeClientCtpPmRxCvsPcs14_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 93),
    _GigeClientCtpPmRxCvsPcs14_Type()
)
gigeClientCtpPmRxCvsPcs14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs14.setStatus("current")
_GigeClientCtpPmRxCvsPcs15_Type = Integer32
_GigeClientCtpPmRxCvsPcs15_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs15 = _GigeClientCtpPmRxCvsPcs15_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 94),
    _GigeClientCtpPmRxCvsPcs15_Type()
)
gigeClientCtpPmRxCvsPcs15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs15.setStatus("current")
_GigeClientCtpPmRxCvsPcs16_Type = Integer32
_GigeClientCtpPmRxCvsPcs16_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs16 = _GigeClientCtpPmRxCvsPcs16_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 95),
    _GigeClientCtpPmRxCvsPcs16_Type()
)
gigeClientCtpPmRxCvsPcs16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs16.setStatus("current")
_GigeClientCtpPmRxCvsPcs17_Type = Integer32
_GigeClientCtpPmRxCvsPcs17_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs17 = _GigeClientCtpPmRxCvsPcs17_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 96),
    _GigeClientCtpPmRxCvsPcs17_Type()
)
gigeClientCtpPmRxCvsPcs17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs17.setStatus("current")
_GigeClientCtpPmRxCvsPcs18_Type = Integer32
_GigeClientCtpPmRxCvsPcs18_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs18 = _GigeClientCtpPmRxCvsPcs18_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 97),
    _GigeClientCtpPmRxCvsPcs18_Type()
)
gigeClientCtpPmRxCvsPcs18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs18.setStatus("current")
_GigeClientCtpPmRxCvsPcs19_Type = Integer32
_GigeClientCtpPmRxCvsPcs19_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs19 = _GigeClientCtpPmRxCvsPcs19_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 98),
    _GigeClientCtpPmRxCvsPcs19_Type()
)
gigeClientCtpPmRxCvsPcs19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs19.setStatus("current")
_GigeClientCtpPmRxCvsPcs20_Type = Integer32
_GigeClientCtpPmRxCvsPcs20_Object = MibTableColumn
gigeClientCtpPmRxCvsPcs20 = _GigeClientCtpPmRxCvsPcs20_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 99),
    _GigeClientCtpPmRxCvsPcs20_Type()
)
gigeClientCtpPmRxCvsPcs20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCvsPcs20.setStatus("current")
_GigeClientCtpPmRxErrPackets_Type = HCPerfIntervalCount
_GigeClientCtpPmRxErrPackets_Object = MibTableColumn
gigeClientCtpPmRxErrPackets = _GigeClientCtpPmRxErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 100),
    _GigeClientCtpPmRxErrPackets_Type()
)
gigeClientCtpPmRxErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxErrPackets.setStatus("current")
_GigeClientCtpPmRxDiscarded_Type = HCPerfIntervalCount
_GigeClientCtpPmRxDiscarded_Object = MibTableColumn
gigeClientCtpPmRxDiscarded = _GigeClientCtpPmRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 101),
    _GigeClientCtpPmRxDiscarded_Type()
)
gigeClientCtpPmRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxDiscarded.setStatus("current")
_GigeClientCtpPmRxCorrectedWords_Type = Integer32
_GigeClientCtpPmRxCorrectedWords_Object = MibTableColumn
gigeClientCtpPmRxCorrectedWords = _GigeClientCtpPmRxCorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 102),
    _GigeClientCtpPmRxCorrectedWords_Type()
)
gigeClientCtpPmRxCorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCorrectedWords.setStatus("current")
_GigeClientCtpPmRxUncorrectedWords_Type = Integer32
_GigeClientCtpPmRxUncorrectedWords_Object = MibTableColumn
gigeClientCtpPmRxUncorrectedWords = _GigeClientCtpPmRxUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 103),
    _GigeClientCtpPmRxUncorrectedWords_Type()
)
gigeClientCtpPmRxUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxUncorrectedWords.setStatus("current")
_GigeClientCtpPmRxCorrectedBit_Type = Integer32
_GigeClientCtpPmRxCorrectedBit_Object = MibTableColumn
gigeClientCtpPmRxCorrectedBit = _GigeClientCtpPmRxCorrectedBit_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 2, 1, 104),
    _GigeClientCtpPmRxCorrectedBit_Type()
)
gigeClientCtpPmRxCorrectedBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeClientCtpPmRxCorrectedBit.setStatus("current")
_GigeClientCtpPmConformance_ObjectIdentity = ObjectIdentity
gigeClientCtpPmConformance = _GigeClientCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 3)
)
_GigeClientCtpPmCompliances_ObjectIdentity = ObjectIdentity
gigeClientCtpPmCompliances = _GigeClientCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 3, 1)
)
_GigeClientCtpPmGroups_ObjectIdentity = ObjectIdentity
gigeClientCtpPmGroups = _GigeClientCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 3, 2)
)

# Managed Objects groups

gigeClientCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 3, 2, 1)
)
gigeClientCtpPmGroup.setObjects(
      *(("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmValidity"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxPcsICG"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxPcsES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxPcsSES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxPcsSESS"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxPcsICG"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxPcsES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxPcsSES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxPcsSESS"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxPackets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxOctets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxErrOctets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxJabbers"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxFragments"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCrcAlignedErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxUndersized"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxOversized"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxJabberSecs"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxMacSES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxBroadcastPkts"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxMulticastPkts"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxInPauseFrames"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxPackets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxOctets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxErrOctets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxJabbers"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxFragments"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCrcAlignedErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxUndersized"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxOversized"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxJabberSecs"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxMacSES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxBroadcastPkts"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxMulticastPkts"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxOutPauseFrames"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxSize64"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxSize65to127"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxSize128to255"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxSize256to511"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxSize512to1023"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxSize1024to1518"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxSize1519toJumbo"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxSize64"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxSize65to127"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxSize128to255"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxSize256to511"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxSize512to1023"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxSize1024to1518"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxSize1519toJumbo"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmCktId"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTribTestSigErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTribTestSigErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmPayloadType"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxSize1024to1522"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxSize1523toJumbo"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxSize1024to1522"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxSize1523toJumbo"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs01"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs02"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs03"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs04"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs05"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs06"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs07"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs08"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs09"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs10"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs11"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs12"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs13"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs14"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs15"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs16"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs17"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs18"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs19"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmTxCvsPcs20"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs01"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs02"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs03"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs04"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs05"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs06"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs07"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs08"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs09"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs10"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs11"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs12"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs13"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs14"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs15"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs16"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs17"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs18"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs19"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCvsPcs20"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxErrPackets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxDiscarded"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCorrectedWords"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxUncorrectedWords"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRxCorrectedBit"))
)
if mibBuilder.loadTexts:
    gigeClientCtpPmGroup.setStatus("current")

gigeClientCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 3, 2, 2)
)
gigeClientCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxLU"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxPcsICG"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxPcsES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxPcsSES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxPcsSESS"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxPcsICG"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxPcsES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxPcsSES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxPcsSESS"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxPackets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxOctets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxErrOctets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxJabbers"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxFragments"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCrcAlignedErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxUndersized"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxOversized"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxJabberSecs"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxMacSES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxBroadcastPkts"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxMulticastPkts"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxInPauseFrames"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxLU"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxPackets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxOctets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxErrOctets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxJabbers"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxFragments"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCrcAlignedErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxUndersized"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxOversized"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxJabberSecs"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxMacSES"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxBroadcastPkts"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxMulticastPkts"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxOutPauseFrames"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxSize64"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxSize65to127"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxSize128to255"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxSize256to511"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxSize512to1023"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxSize1024to1518"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxSize1519toJumbo"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxSize64"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxSize65to127"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxSize128to255"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxSize256to511"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxSize512to1023"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxSize1024to1518"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxSize1519toJumbo"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealCktId"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealLineTestSigErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealLineTestSigErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTribTestSigErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTribTestSigErr"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxSize1024to1522"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxSize1523toJumbo"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxSize1024to1522"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxSize1523toJumbo"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs01"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs02"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs03"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs04"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs05"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs06"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs07"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs08"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs09"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs10"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs11"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs12"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs13"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs14"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs15"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs16"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs17"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs18"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs19"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealTxCvsPcs20"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs01"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs02"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs03"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs04"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs05"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs06"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs07"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs08"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs09"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs10"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs11"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs12"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs13"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs14"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs15"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs16"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs17"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs18"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs19"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCvsPcs20"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxErrPackets"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxDiscarded"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCorrectedWords"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxUncorrectedWords"),
        ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealRxCorrectedBit"))
)
if mibBuilder.loadTexts:
    gigeClientCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gigeClientCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 3, 1, 1)
)
gigeClientCtpPmCompliance.setObjects(
    ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmGroup")
)
if mibBuilder.loadTexts:
    gigeClientCtpPmCompliance.setStatus(
        "current"
    )

gigeClientCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 8, 3, 1, 2)
)
gigeClientCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-GIGECLIENTCTP-MIB", "gigeClientCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    gigeClientCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-GIGECLIENTCTP-MIB",
    **{"gigeClientCtpPmMIB": gigeClientCtpPmMIB,
       "gigeClientCtpPmRealTable": gigeClientCtpPmRealTable,
       "gigeClientCtpPmRealEntry": gigeClientCtpPmRealEntry,
       "gigeClientCtpPmRealRxLU": gigeClientCtpPmRealRxLU,
       "gigeClientCtpPmRealRxPcsICG": gigeClientCtpPmRealRxPcsICG,
       "gigeClientCtpPmRealRxPcsES": gigeClientCtpPmRealRxPcsES,
       "gigeClientCtpPmRealRxPcsSES": gigeClientCtpPmRealRxPcsSES,
       "gigeClientCtpPmRealRxPcsSESS": gigeClientCtpPmRealRxPcsSESS,
       "gigeClientCtpPmRealTxPcsICG": gigeClientCtpPmRealTxPcsICG,
       "gigeClientCtpPmRealTxPcsES": gigeClientCtpPmRealTxPcsES,
       "gigeClientCtpPmRealTxPcsSES": gigeClientCtpPmRealTxPcsSES,
       "gigeClientCtpPmRealTxPcsSESS": gigeClientCtpPmRealTxPcsSESS,
       "gigeClientCtpPmRealRxPackets": gigeClientCtpPmRealRxPackets,
       "gigeClientCtpPmRealRxOctets": gigeClientCtpPmRealRxOctets,
       "gigeClientCtpPmRealRxErrOctets": gigeClientCtpPmRealRxErrOctets,
       "gigeClientCtpPmRealRxJabbers": gigeClientCtpPmRealRxJabbers,
       "gigeClientCtpPmRealRxFragments": gigeClientCtpPmRealRxFragments,
       "gigeClientCtpPmRealRxCrcAlignedErr": gigeClientCtpPmRealRxCrcAlignedErr,
       "gigeClientCtpPmRealRxUndersized": gigeClientCtpPmRealRxUndersized,
       "gigeClientCtpPmRealRxOversized": gigeClientCtpPmRealRxOversized,
       "gigeClientCtpPmRealRxJabberSecs": gigeClientCtpPmRealRxJabberSecs,
       "gigeClientCtpPmRealRxMacSES": gigeClientCtpPmRealRxMacSES,
       "gigeClientCtpPmRealRxBroadcastPkts": gigeClientCtpPmRealRxBroadcastPkts,
       "gigeClientCtpPmRealRxMulticastPkts": gigeClientCtpPmRealRxMulticastPkts,
       "gigeClientCtpPmRealRxInPauseFrames": gigeClientCtpPmRealRxInPauseFrames,
       "gigeClientCtpPmRealTxLU": gigeClientCtpPmRealTxLU,
       "gigeClientCtpPmRealTxPackets": gigeClientCtpPmRealTxPackets,
       "gigeClientCtpPmRealTxOctets": gigeClientCtpPmRealTxOctets,
       "gigeClientCtpPmRealTxErrOctets": gigeClientCtpPmRealTxErrOctets,
       "gigeClientCtpPmRealTxJabbers": gigeClientCtpPmRealTxJabbers,
       "gigeClientCtpPmRealTxFragments": gigeClientCtpPmRealTxFragments,
       "gigeClientCtpPmRealTxCrcAlignedErr": gigeClientCtpPmRealTxCrcAlignedErr,
       "gigeClientCtpPmRealTxUndersized": gigeClientCtpPmRealTxUndersized,
       "gigeClientCtpPmRealTxOversized": gigeClientCtpPmRealTxOversized,
       "gigeClientCtpPmRealTxJabberSecs": gigeClientCtpPmRealTxJabberSecs,
       "gigeClientCtpPmRealTxMacSES": gigeClientCtpPmRealTxMacSES,
       "gigeClientCtpPmRealTxBroadcastPkts": gigeClientCtpPmRealTxBroadcastPkts,
       "gigeClientCtpPmRealTxMulticastPkts": gigeClientCtpPmRealTxMulticastPkts,
       "gigeClientCtpPmRealTxOutPauseFrames": gigeClientCtpPmRealTxOutPauseFrames,
       "gigeClientCtpPmRealRxSize64": gigeClientCtpPmRealRxSize64,
       "gigeClientCtpPmRealRxSize65to127": gigeClientCtpPmRealRxSize65to127,
       "gigeClientCtpPmRealRxSize128to255": gigeClientCtpPmRealRxSize128to255,
       "gigeClientCtpPmRealRxSize256to511": gigeClientCtpPmRealRxSize256to511,
       "gigeClientCtpPmRealRxSize512to1023": gigeClientCtpPmRealRxSize512to1023,
       "gigeClientCtpPmRealRxSize1024to1518": gigeClientCtpPmRealRxSize1024to1518,
       "gigeClientCtpPmRealRxSize1519toJumbo": gigeClientCtpPmRealRxSize1519toJumbo,
       "gigeClientCtpPmRealTxSize64": gigeClientCtpPmRealTxSize64,
       "gigeClientCtpPmRealTxSize65to127": gigeClientCtpPmRealTxSize65to127,
       "gigeClientCtpPmRealTxSize128to255": gigeClientCtpPmRealTxSize128to255,
       "gigeClientCtpPmRealTxSize256to511": gigeClientCtpPmRealTxSize256to511,
       "gigeClientCtpPmRealTxSize512to1023": gigeClientCtpPmRealTxSize512to1023,
       "gigeClientCtpPmRealTxSize1024to1518": gigeClientCtpPmRealTxSize1024to1518,
       "gigeClientCtpPmRealTxSize1519toJumbo": gigeClientCtpPmRealTxSize1519toJumbo,
       "gigeClientCtpPmRealCktId": gigeClientCtpPmRealCktId,
       "gigeClientCtpPmRealLineTestSigSyncErr": gigeClientCtpPmRealLineTestSigSyncErr,
       "gigeClientCtpPmRealLineTestSigErr": gigeClientCtpPmRealLineTestSigErr,
       "gigeClientCtpPmRealTribTestSigSyncErr": gigeClientCtpPmRealTribTestSigSyncErr,
       "gigeClientCtpPmRealTribTestSigErr": gigeClientCtpPmRealTribTestSigErr,
       "gigeClientCtpPmRealRxSize1024to1522": gigeClientCtpPmRealRxSize1024to1522,
       "gigeClientCtpPmRealRxSize1523toJumbo": gigeClientCtpPmRealRxSize1523toJumbo,
       "gigeClientCtpPmRealTxSize1024to1522": gigeClientCtpPmRealTxSize1024to1522,
       "gigeClientCtpPmRealTxSize1523toJumbo": gigeClientCtpPmRealTxSize1523toJumbo,
       "gigeClientCtpPmRealTxCvsPcs01": gigeClientCtpPmRealTxCvsPcs01,
       "gigeClientCtpPmRealTxCvsPcs02": gigeClientCtpPmRealTxCvsPcs02,
       "gigeClientCtpPmRealTxCvsPcs03": gigeClientCtpPmRealTxCvsPcs03,
       "gigeClientCtpPmRealTxCvsPcs04": gigeClientCtpPmRealTxCvsPcs04,
       "gigeClientCtpPmRealTxCvsPcs05": gigeClientCtpPmRealTxCvsPcs05,
       "gigeClientCtpPmRealTxCvsPcs06": gigeClientCtpPmRealTxCvsPcs06,
       "gigeClientCtpPmRealTxCvsPcs07": gigeClientCtpPmRealTxCvsPcs07,
       "gigeClientCtpPmRealTxCvsPcs08": gigeClientCtpPmRealTxCvsPcs08,
       "gigeClientCtpPmRealTxCvsPcs09": gigeClientCtpPmRealTxCvsPcs09,
       "gigeClientCtpPmRealTxCvsPcs10": gigeClientCtpPmRealTxCvsPcs10,
       "gigeClientCtpPmRealTxCvsPcs11": gigeClientCtpPmRealTxCvsPcs11,
       "gigeClientCtpPmRealTxCvsPcs12": gigeClientCtpPmRealTxCvsPcs12,
       "gigeClientCtpPmRealTxCvsPcs13": gigeClientCtpPmRealTxCvsPcs13,
       "gigeClientCtpPmRealTxCvsPcs14": gigeClientCtpPmRealTxCvsPcs14,
       "gigeClientCtpPmRealTxCvsPcs15": gigeClientCtpPmRealTxCvsPcs15,
       "gigeClientCtpPmRealTxCvsPcs16": gigeClientCtpPmRealTxCvsPcs16,
       "gigeClientCtpPmRealTxCvsPcs17": gigeClientCtpPmRealTxCvsPcs17,
       "gigeClientCtpPmRealTxCvsPcs18": gigeClientCtpPmRealTxCvsPcs18,
       "gigeClientCtpPmRealTxCvsPcs19": gigeClientCtpPmRealTxCvsPcs19,
       "gigeClientCtpPmRealTxCvsPcs20": gigeClientCtpPmRealTxCvsPcs20,
       "gigeClientCtpPmRealRxCvsPcs01": gigeClientCtpPmRealRxCvsPcs01,
       "gigeClientCtpPmRealRxCvsPcs02": gigeClientCtpPmRealRxCvsPcs02,
       "gigeClientCtpPmRealRxCvsPcs03": gigeClientCtpPmRealRxCvsPcs03,
       "gigeClientCtpPmRealRxCvsPcs04": gigeClientCtpPmRealRxCvsPcs04,
       "gigeClientCtpPmRealRxCvsPcs05": gigeClientCtpPmRealRxCvsPcs05,
       "gigeClientCtpPmRealRxCvsPcs06": gigeClientCtpPmRealRxCvsPcs06,
       "gigeClientCtpPmRealRxCvsPcs07": gigeClientCtpPmRealRxCvsPcs07,
       "gigeClientCtpPmRealRxCvsPcs08": gigeClientCtpPmRealRxCvsPcs08,
       "gigeClientCtpPmRealRxCvsPcs09": gigeClientCtpPmRealRxCvsPcs09,
       "gigeClientCtpPmRealRxCvsPcs10": gigeClientCtpPmRealRxCvsPcs10,
       "gigeClientCtpPmRealRxCvsPcs11": gigeClientCtpPmRealRxCvsPcs11,
       "gigeClientCtpPmRealRxCvsPcs12": gigeClientCtpPmRealRxCvsPcs12,
       "gigeClientCtpPmRealRxCvsPcs13": gigeClientCtpPmRealRxCvsPcs13,
       "gigeClientCtpPmRealRxCvsPcs14": gigeClientCtpPmRealRxCvsPcs14,
       "gigeClientCtpPmRealRxCvsPcs15": gigeClientCtpPmRealRxCvsPcs15,
       "gigeClientCtpPmRealRxCvsPcs16": gigeClientCtpPmRealRxCvsPcs16,
       "gigeClientCtpPmRealRxCvsPcs17": gigeClientCtpPmRealRxCvsPcs17,
       "gigeClientCtpPmRealRxCvsPcs18": gigeClientCtpPmRealRxCvsPcs18,
       "gigeClientCtpPmRealRxCvsPcs19": gigeClientCtpPmRealRxCvsPcs19,
       "gigeClientCtpPmRealRxCvsPcs20": gigeClientCtpPmRealRxCvsPcs20,
       "gigeClientCtpPmRealRxErrPackets": gigeClientCtpPmRealRxErrPackets,
       "gigeClientCtpPmRealRxDiscarded": gigeClientCtpPmRealRxDiscarded,
       "gigeClientCtpPmRealRxCorrectedWords": gigeClientCtpPmRealRxCorrectedWords,
       "gigeClientCtpPmRealRxUncorrectedWords": gigeClientCtpPmRealRxUncorrectedWords,
       "gigeClientCtpPmRealRxCorrectedBit": gigeClientCtpPmRealRxCorrectedBit,
       "gigeClientCtpPmTable": gigeClientCtpPmTable,
       "gigeClientCtpPmEntry": gigeClientCtpPmEntry,
       "gigeClientCtpPmTimestamp": gigeClientCtpPmTimestamp,
       "gigeClientCtpPmSampleDuration": gigeClientCtpPmSampleDuration,
       "gigeClientCtpPmValidity": gigeClientCtpPmValidity,
       "gigeClientCtpPmRxPcsICG": gigeClientCtpPmRxPcsICG,
       "gigeClientCtpPmRxPcsES": gigeClientCtpPmRxPcsES,
       "gigeClientCtpPmRxPcsSES": gigeClientCtpPmRxPcsSES,
       "gigeClientCtpPmRxPcsSESS": gigeClientCtpPmRxPcsSESS,
       "gigeClientCtpPmTxPcsICG": gigeClientCtpPmTxPcsICG,
       "gigeClientCtpPmTxPcsES": gigeClientCtpPmTxPcsES,
       "gigeClientCtpPmTxPcsSES": gigeClientCtpPmTxPcsSES,
       "gigeClientCtpPmTxPcsSESS": gigeClientCtpPmTxPcsSESS,
       "gigeClientCtpPmRxPackets": gigeClientCtpPmRxPackets,
       "gigeClientCtpPmRxOctets": gigeClientCtpPmRxOctets,
       "gigeClientCtpPmRxErrOctets": gigeClientCtpPmRxErrOctets,
       "gigeClientCtpPmRxJabbers": gigeClientCtpPmRxJabbers,
       "gigeClientCtpPmRxFragments": gigeClientCtpPmRxFragments,
       "gigeClientCtpPmRxCrcAlignedErr": gigeClientCtpPmRxCrcAlignedErr,
       "gigeClientCtpPmRxUndersized": gigeClientCtpPmRxUndersized,
       "gigeClientCtpPmRxOversized": gigeClientCtpPmRxOversized,
       "gigeClientCtpPmRxJabberSecs": gigeClientCtpPmRxJabberSecs,
       "gigeClientCtpPmRxMacSES": gigeClientCtpPmRxMacSES,
       "gigeClientCtpPmRxBroadcastPkts": gigeClientCtpPmRxBroadcastPkts,
       "gigeClientCtpPmRxMulticastPkts": gigeClientCtpPmRxMulticastPkts,
       "gigeClientCtpPmRxInPauseFrames": gigeClientCtpPmRxInPauseFrames,
       "gigeClientCtpPmTxPackets": gigeClientCtpPmTxPackets,
       "gigeClientCtpPmTxOctets": gigeClientCtpPmTxOctets,
       "gigeClientCtpPmTxErrOctets": gigeClientCtpPmTxErrOctets,
       "gigeClientCtpPmTxJabbers": gigeClientCtpPmTxJabbers,
       "gigeClientCtpPmTxFragments": gigeClientCtpPmTxFragments,
       "gigeClientCtpPmTxCrcAlignedErr": gigeClientCtpPmTxCrcAlignedErr,
       "gigeClientCtpPmTxUndersized": gigeClientCtpPmTxUndersized,
       "gigeClientCtpPmTxOversized": gigeClientCtpPmTxOversized,
       "gigeClientCtpPmTxJabberSecs": gigeClientCtpPmTxJabberSecs,
       "gigeClientCtpPmTxMacSES": gigeClientCtpPmTxMacSES,
       "gigeClientCtpPmTxBroadcastPkts": gigeClientCtpPmTxBroadcastPkts,
       "gigeClientCtpPmTxMulticastPkts": gigeClientCtpPmTxMulticastPkts,
       "gigeClientCtpPmTxOutPauseFrames": gigeClientCtpPmTxOutPauseFrames,
       "gigeClientCtpPmRxSize64": gigeClientCtpPmRxSize64,
       "gigeClientCtpPmRxSize65to127": gigeClientCtpPmRxSize65to127,
       "gigeClientCtpPmRxSize128to255": gigeClientCtpPmRxSize128to255,
       "gigeClientCtpPmRxSize256to511": gigeClientCtpPmRxSize256to511,
       "gigeClientCtpPmRxSize512to1023": gigeClientCtpPmRxSize512to1023,
       "gigeClientCtpPmRxSize1024to1518": gigeClientCtpPmRxSize1024to1518,
       "gigeClientCtpPmRxSize1519toJumbo": gigeClientCtpPmRxSize1519toJumbo,
       "gigeClientCtpPmTxSize64": gigeClientCtpPmTxSize64,
       "gigeClientCtpPmTxSize65to127": gigeClientCtpPmTxSize65to127,
       "gigeClientCtpPmTxSize128to255": gigeClientCtpPmTxSize128to255,
       "gigeClientCtpPmTxSize256to511": gigeClientCtpPmTxSize256to511,
       "gigeClientCtpPmTxSize512to1023": gigeClientCtpPmTxSize512to1023,
       "gigeClientCtpPmTxSize1024to1518": gigeClientCtpPmTxSize1024to1518,
       "gigeClientCtpPmTxSize1519toJumbo": gigeClientCtpPmTxSize1519toJumbo,
       "gigeClientCtpPmCktId": gigeClientCtpPmCktId,
       "gigeClientCtpPmTribTestSigSyncErr": gigeClientCtpPmTribTestSigSyncErr,
       "gigeClientCtpPmTribTestSigErr": gigeClientCtpPmTribTestSigErr,
       "gigeClientCtpPmPayloadType": gigeClientCtpPmPayloadType,
       "gigeClientCtpPmRxSize1024to1522": gigeClientCtpPmRxSize1024to1522,
       "gigeClientCtpPmRxSize1523toJumbo": gigeClientCtpPmRxSize1523toJumbo,
       "gigeClientCtpPmTxSize1024to1522": gigeClientCtpPmTxSize1024to1522,
       "gigeClientCtpPmTxSize1523toJumbo": gigeClientCtpPmTxSize1523toJumbo,
       "gigeClientCtpPmTxCvsPcs01": gigeClientCtpPmTxCvsPcs01,
       "gigeClientCtpPmTxCvsPcs02": gigeClientCtpPmTxCvsPcs02,
       "gigeClientCtpPmTxCvsPcs03": gigeClientCtpPmTxCvsPcs03,
       "gigeClientCtpPmTxCvsPcs04": gigeClientCtpPmTxCvsPcs04,
       "gigeClientCtpPmTxCvsPcs05": gigeClientCtpPmTxCvsPcs05,
       "gigeClientCtpPmTxCvsPcs06": gigeClientCtpPmTxCvsPcs06,
       "gigeClientCtpPmTxCvsPcs07": gigeClientCtpPmTxCvsPcs07,
       "gigeClientCtpPmTxCvsPcs08": gigeClientCtpPmTxCvsPcs08,
       "gigeClientCtpPmTxCvsPcs09": gigeClientCtpPmTxCvsPcs09,
       "gigeClientCtpPmTxCvsPcs10": gigeClientCtpPmTxCvsPcs10,
       "gigeClientCtpPmTxCvsPcs11": gigeClientCtpPmTxCvsPcs11,
       "gigeClientCtpPmTxCvsPcs12": gigeClientCtpPmTxCvsPcs12,
       "gigeClientCtpPmTxCvsPcs13": gigeClientCtpPmTxCvsPcs13,
       "gigeClientCtpPmTxCvsPcs14": gigeClientCtpPmTxCvsPcs14,
       "gigeClientCtpPmTxCvsPcs15": gigeClientCtpPmTxCvsPcs15,
       "gigeClientCtpPmTxCvsPcs16": gigeClientCtpPmTxCvsPcs16,
       "gigeClientCtpPmTxCvsPcs17": gigeClientCtpPmTxCvsPcs17,
       "gigeClientCtpPmTxCvsPcs18": gigeClientCtpPmTxCvsPcs18,
       "gigeClientCtpPmTxCvsPcs19": gigeClientCtpPmTxCvsPcs19,
       "gigeClientCtpPmTxCvsPcs20": gigeClientCtpPmTxCvsPcs20,
       "gigeClientCtpPmRxCvsPcs01": gigeClientCtpPmRxCvsPcs01,
       "gigeClientCtpPmRxCvsPcs02": gigeClientCtpPmRxCvsPcs02,
       "gigeClientCtpPmRxCvsPcs03": gigeClientCtpPmRxCvsPcs03,
       "gigeClientCtpPmRxCvsPcs04": gigeClientCtpPmRxCvsPcs04,
       "gigeClientCtpPmRxCvsPcs05": gigeClientCtpPmRxCvsPcs05,
       "gigeClientCtpPmRxCvsPcs06": gigeClientCtpPmRxCvsPcs06,
       "gigeClientCtpPmRxCvsPcs07": gigeClientCtpPmRxCvsPcs07,
       "gigeClientCtpPmRxCvsPcs08": gigeClientCtpPmRxCvsPcs08,
       "gigeClientCtpPmRxCvsPcs09": gigeClientCtpPmRxCvsPcs09,
       "gigeClientCtpPmRxCvsPcs10": gigeClientCtpPmRxCvsPcs10,
       "gigeClientCtpPmRxCvsPcs11": gigeClientCtpPmRxCvsPcs11,
       "gigeClientCtpPmRxCvsPcs12": gigeClientCtpPmRxCvsPcs12,
       "gigeClientCtpPmRxCvsPcs13": gigeClientCtpPmRxCvsPcs13,
       "gigeClientCtpPmRxCvsPcs14": gigeClientCtpPmRxCvsPcs14,
       "gigeClientCtpPmRxCvsPcs15": gigeClientCtpPmRxCvsPcs15,
       "gigeClientCtpPmRxCvsPcs16": gigeClientCtpPmRxCvsPcs16,
       "gigeClientCtpPmRxCvsPcs17": gigeClientCtpPmRxCvsPcs17,
       "gigeClientCtpPmRxCvsPcs18": gigeClientCtpPmRxCvsPcs18,
       "gigeClientCtpPmRxCvsPcs19": gigeClientCtpPmRxCvsPcs19,
       "gigeClientCtpPmRxCvsPcs20": gigeClientCtpPmRxCvsPcs20,
       "gigeClientCtpPmRxErrPackets": gigeClientCtpPmRxErrPackets,
       "gigeClientCtpPmRxDiscarded": gigeClientCtpPmRxDiscarded,
       "gigeClientCtpPmRxCorrectedWords": gigeClientCtpPmRxCorrectedWords,
       "gigeClientCtpPmRxUncorrectedWords": gigeClientCtpPmRxUncorrectedWords,
       "gigeClientCtpPmRxCorrectedBit": gigeClientCtpPmRxCorrectedBit,
       "gigeClientCtpPmConformance": gigeClientCtpPmConformance,
       "gigeClientCtpPmCompliances": gigeClientCtpPmCompliances,
       "gigeClientCtpPmCompliance": gigeClientCtpPmCompliance,
       "gigeClientCtpPmRealCompliance": gigeClientCtpPmRealCompliance,
       "gigeClientCtpPmGroups": gigeClientCtpPmGroups,
       "gigeClientCtpPmGroup": gigeClientCtpPmGroup,
       "gigeClientCtpPmRealGroup": gigeClientCtpPmRealGroup}
)
