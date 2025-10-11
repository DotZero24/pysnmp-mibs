# SNMP MIB module (FS-SYNC-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-SYNC-STATS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:22 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

fsSyncStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51)
)
if mibBuilder.loadTexts:
    fsSyncStatsMIB.setRevisions(
        ("2009-05-20 14:56",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSyncStatsMibObjects_ObjectIdentity = ObjectIdentity
fsSyncStatsMibObjects = _FsSyncStatsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1)
)
_FsStatsSyncGlobal_ObjectIdentity = ObjectIdentity
fsStatsSyncGlobal = _FsStatsSyncGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 1)
)
_FsSyncStatsTable_Object = MibTable
fsSyncStatsTable = _FsSyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2)
)
if mibBuilder.loadTexts:
    fsSyncStatsTable.setStatus("current")
_FsSyncStatsEntry_Object = MibTableRow
fsSyncStatsEntry = _FsSyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1)
)
fsSyncStatsEntry.setIndexNames(
    (0, "FS-SYNC-STATS-MIB", "fsSyncStatsSlot"),
    (0, "FS-SYNC-STATS-MIB", "fsSyncStatsConn"),
    (0, "FS-SYNC-STATS-MIB", "fsSyncStatsChannel"),
)
if mibBuilder.loadTexts:
    fsSyncStatsEntry.setStatus("current")
_FsSyncStatsRowStatus_Type = RowStatus
_FsSyncStatsRowStatus_Object = MibTableColumn
fsSyncStatsRowStatus = _FsSyncStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 1),
    _FsSyncStatsRowStatus_Type()
)
fsSyncStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSyncStatsRowStatus.setStatus("current")


class _FsSyncStatsSlot_Type(Integer32):
    """Custom type fsSyncStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsSyncStatsSlot_Type.__name__ = "Integer32"
_FsSyncStatsSlot_Object = MibTableColumn
fsSyncStatsSlot = _FsSyncStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 2),
    _FsSyncStatsSlot_Type()
)
fsSyncStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsSlot.setStatus("current")


class _FsSyncStatsConn_Type(Integer32):
    """Custom type fsSyncStatsConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsSyncStatsConn_Type.__name__ = "Integer32"
_FsSyncStatsConn_Object = MibTableColumn
fsSyncStatsConn = _FsSyncStatsConn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 3),
    _FsSyncStatsConn_Type()
)
fsSyncStatsConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsConn.setStatus("current")


class _FsSyncStatsChannel_Type(Integer32):
    """Custom type fsSyncStatsChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsSyncStatsChannel_Type.__name__ = "Integer32"
_FsSyncStatsChannel_Object = MibTableColumn
fsSyncStatsChannel = _FsSyncStatsChannel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 4),
    _FsSyncStatsChannel_Type()
)
fsSyncStatsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsChannel.setStatus("current")
_FsSyncStatsIfIndex_Type = InterfaceIndex
_FsSyncStatsIfIndex_Object = MibTableColumn
fsSyncStatsIfIndex = _FsSyncStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 5),
    _FsSyncStatsIfIndex_Type()
)
fsSyncStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsIfIndex.setStatus("current")


class _FsSyncStatsPortState_Type(Integer32):
    """Custom type fsSyncStatsPortState based on Integer32"""
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
        *(("init", 1),
          ("running", 2),
          ("up", 3),
          ("down", 4))
    )


_FsSyncStatsPortState_Type.__name__ = "Integer32"
_FsSyncStatsPortState_Object = MibTableColumn
fsSyncStatsPortState = _FsSyncStatsPortState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 6),
    _FsSyncStatsPortState_Type()
)
fsSyncStatsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsPortState.setStatus("current")
_FsSyncStatsRxFrames_Type = Counter32
_FsSyncStatsRxFrames_Object = MibTableColumn
fsSyncStatsRxFrames = _FsSyncStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 7),
    _FsSyncStatsRxFrames_Type()
)
fsSyncStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxFrames.setStatus("current")
_FsSyncStatsRxOctets_Type = Counter32
_FsSyncStatsRxOctets_Object = MibTableColumn
fsSyncStatsRxOctets = _FsSyncStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 8),
    _FsSyncStatsRxOctets_Type()
)
fsSyncStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxOctets.setStatus("current")
_FsSyncStatsRxReplenFails_Type = Counter32
_FsSyncStatsRxReplenFails_Object = MibTableColumn
fsSyncStatsRxReplenFails = _FsSyncStatsRxReplenFails_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 9),
    _FsSyncStatsRxReplenFails_Type()
)
fsSyncStatsRxReplenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxReplenFails.setStatus("current")
_FsSyncStatsRxClockErrors_Type = Counter32
_FsSyncStatsRxClockErrors_Object = MibTableColumn
fsSyncStatsRxClockErrors = _FsSyncStatsRxClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 10),
    _FsSyncStatsRxClockErrors_Type()
)
fsSyncStatsRxClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxClockErrors.setStatus("current")
_FsSyncStatsRxDpllErrors_Type = Counter32
_FsSyncStatsRxDpllErrors_Object = MibTableColumn
fsSyncStatsRxDpllErrors = _FsSyncStatsRxDpllErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 11),
    _FsSyncStatsRxDpllErrors_Type()
)
fsSyncStatsRxDpllErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxDpllErrors.setStatus("current")
_FsSyncStatsRxFrameTooLongErrors_Type = Counter32
_FsSyncStatsRxFrameTooLongErrors_Object = MibTableColumn
fsSyncStatsRxFrameTooLongErrors = _FsSyncStatsRxFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 12),
    _FsSyncStatsRxFrameTooLongErrors_Type()
)
fsSyncStatsRxFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxFrameTooLongErrors.setStatus("current")
_FsSyncStatsRxFrameOctetAlignErrors_Type = Counter32
_FsSyncStatsRxFrameOctetAlignErrors_Object = MibTableColumn
fsSyncStatsRxFrameOctetAlignErrors = _FsSyncStatsRxFrameOctetAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 13),
    _FsSyncStatsRxFrameOctetAlignErrors_Type()
)
fsSyncStatsRxFrameOctetAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxFrameOctetAlignErrors.setStatus("current")
_FsSyncStatsRxAbortErrors_Type = Counter32
_FsSyncStatsRxAbortErrors_Object = MibTableColumn
fsSyncStatsRxAbortErrors = _FsSyncStatsRxAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 14),
    _FsSyncStatsRxAbortErrors_Type()
)
fsSyncStatsRxAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxAbortErrors.setStatus("current")
_FsSyncStatsRxCrcErrors_Type = Counter32
_FsSyncStatsRxCrcErrors_Object = MibTableColumn
fsSyncStatsRxCrcErrors = _FsSyncStatsRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 15),
    _FsSyncStatsRxCrcErrors_Type()
)
fsSyncStatsRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxCrcErrors.setStatus("current")
_FsSyncStatsRxRcvrOverrunErrors_Type = Counter32
_FsSyncStatsRxRcvrOverrunErrors_Object = MibTableColumn
fsSyncStatsRxRcvrOverrunErrors = _FsSyncStatsRxRcvrOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 16),
    _FsSyncStatsRxRcvrOverrunErrors_Type()
)
fsSyncStatsRxRcvrOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsRxRcvrOverrunErrors.setStatus("current")
_FsSyncStatsTxFrames_Type = Counter32
_FsSyncStatsTxFrames_Object = MibTableColumn
fsSyncStatsTxFrames = _FsSyncStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 17),
    _FsSyncStatsTxFrames_Type()
)
fsSyncStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsTxFrames.setStatus("current")
_FsSyncStatsTxOctets_Type = Counter32
_FsSyncStatsTxOctets_Object = MibTableColumn
fsSyncStatsTxOctets = _FsSyncStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 18),
    _FsSyncStatsTxOctets_Type()
)
fsSyncStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsTxOctets.setStatus("current")
_FsSyncStatsTxRingFullDropsErrors_Type = Counter32
_FsSyncStatsTxRingFullDropsErrors_Object = MibTableColumn
fsSyncStatsTxRingFullDropsErrors = _FsSyncStatsTxRingFullDropsErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 19),
    _FsSyncStatsTxRingFullDropsErrors_Type()
)
fsSyncStatsTxRingFullDropsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsTxRingFullDropsErrors.setStatus("current")
_FsSyncStatsTxClockErrors_Type = Counter32
_FsSyncStatsTxClockErrors_Object = MibTableColumn
fsSyncStatsTxClockErrors = _FsSyncStatsTxClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 20),
    _FsSyncStatsTxClockErrors_Type()
)
fsSyncStatsTxClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsTxClockErrors.setStatus("current")
_FsSyncStatsTxFrameTooLongErrors_Type = Counter32
_FsSyncStatsTxFrameTooLongErrors_Object = MibTableColumn
fsSyncStatsTxFrameTooLongErrors = _FsSyncStatsTxFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 21),
    _FsSyncStatsTxFrameTooLongErrors_Type()
)
fsSyncStatsTxFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsTxFrameTooLongErrors.setStatus("current")
_FsSyncStatsTxUnderrunErrors_Type = Counter32
_FsSyncStatsTxUnderrunErrors_Object = MibTableColumn
fsSyncStatsTxUnderrunErrors = _FsSyncStatsTxUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 1, 2, 1, 22),
    _FsSyncStatsTxUnderrunErrors_Type()
)
fsSyncStatsTxUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatsTxUnderrunErrors.setStatus("current")
_FsSyncStatsMibConformance_ObjectIdentity = ObjectIdentity
fsSyncStatsMibConformance = _FsSyncStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 2)
)
_FsSyncStatsMibCompliances_ObjectIdentity = ObjectIdentity
fsSyncStatsMibCompliances = _FsSyncStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 2, 1)
)
_FsSyncStatsMibGroups_ObjectIdentity = ObjectIdentity
fsSyncStatsMibGroups = _FsSyncStatsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 2, 2)
)

# Managed Objects groups

fsSyncStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 2, 2, 1)
)
fsSyncStatsGroup.setObjects(
      *(("FS-SYNC-STATS-MIB", "fsSyncStatsRowStatus"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsSlot"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsConn"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsChannel"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsIfIndex"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsPortState"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxFrames"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxOctets"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxReplenFails"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxClockErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxDpllErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxFrameTooLongErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxFrameOctetAlignErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxAbortErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxCrcErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsRxRcvrOverrunErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsTxFrames"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsTxOctets"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsTxRingFullDropsErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsTxClockErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsTxFrameTooLongErrors"),
        ("FS-SYNC-STATS-MIB", "fsSyncStatsTxUnderrunErrors"))
)
if mibBuilder.loadTexts:
    fsSyncStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsSyncStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 51, 2, 1, 1)
)
fsSyncStatsMibCompliance.setObjects(
    ("FS-SYNC-STATS-MIB", "fsSyncStatsGroup")
)
if mibBuilder.loadTexts:
    fsSyncStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-SYNC-STATS-MIB",
    **{"fsSyncStatsMIB": fsSyncStatsMIB,
       "fsSyncStatsMibObjects": fsSyncStatsMibObjects,
       "fsStatsSyncGlobal": fsStatsSyncGlobal,
       "fsSyncStatsTable": fsSyncStatsTable,
       "fsSyncStatsEntry": fsSyncStatsEntry,
       "fsSyncStatsRowStatus": fsSyncStatsRowStatus,
       "fsSyncStatsSlot": fsSyncStatsSlot,
       "fsSyncStatsConn": fsSyncStatsConn,
       "fsSyncStatsChannel": fsSyncStatsChannel,
       "fsSyncStatsIfIndex": fsSyncStatsIfIndex,
       "fsSyncStatsPortState": fsSyncStatsPortState,
       "fsSyncStatsRxFrames": fsSyncStatsRxFrames,
       "fsSyncStatsRxOctets": fsSyncStatsRxOctets,
       "fsSyncStatsRxReplenFails": fsSyncStatsRxReplenFails,
       "fsSyncStatsRxClockErrors": fsSyncStatsRxClockErrors,
       "fsSyncStatsRxDpllErrors": fsSyncStatsRxDpllErrors,
       "fsSyncStatsRxFrameTooLongErrors": fsSyncStatsRxFrameTooLongErrors,
       "fsSyncStatsRxFrameOctetAlignErrors": fsSyncStatsRxFrameOctetAlignErrors,
       "fsSyncStatsRxAbortErrors": fsSyncStatsRxAbortErrors,
       "fsSyncStatsRxCrcErrors": fsSyncStatsRxCrcErrors,
       "fsSyncStatsRxRcvrOverrunErrors": fsSyncStatsRxRcvrOverrunErrors,
       "fsSyncStatsTxFrames": fsSyncStatsTxFrames,
       "fsSyncStatsTxOctets": fsSyncStatsTxOctets,
       "fsSyncStatsTxRingFullDropsErrors": fsSyncStatsTxRingFullDropsErrors,
       "fsSyncStatsTxClockErrors": fsSyncStatsTxClockErrors,
       "fsSyncStatsTxFrameTooLongErrors": fsSyncStatsTxFrameTooLongErrors,
       "fsSyncStatsTxUnderrunErrors": fsSyncStatsTxUnderrunErrors,
       "fsSyncStatsMibConformance": fsSyncStatsMibConformance,
       "fsSyncStatsMibCompliances": fsSyncStatsMibCompliances,
       "fsSyncStatsMibCompliance": fsSyncStatsMibCompliance,
       "fsSyncStatsMibGroups": fsSyncStatsMibGroups,
       "fsSyncStatsGroup": fsSyncStatsGroup}
)
