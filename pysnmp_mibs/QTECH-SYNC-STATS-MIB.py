# SNMP MIB module (QTECH-SYNC-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SYNC-STATS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:51 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechSyncStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51)
)
if mibBuilder.loadTexts:
    qtechSyncStatsMIB.setRevisions(
        ("2009-05-20 14:56",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechSyncStatsMibObjects_ObjectIdentity = ObjectIdentity
qtechSyncStatsMibObjects = _QtechSyncStatsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1)
)
_QtechStatsSyncGlobal_ObjectIdentity = ObjectIdentity
qtechStatsSyncGlobal = _QtechStatsSyncGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 1)
)
_QtechSyncStatsTable_Object = MibTable
qtechSyncStatsTable = _QtechSyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2)
)
if mibBuilder.loadTexts:
    qtechSyncStatsTable.setStatus("current")
_QtechSyncStatsEntry_Object = MibTableRow
qtechSyncStatsEntry = _QtechSyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1)
)
qtechSyncStatsEntry.setIndexNames(
    (0, "QTECH-SYNC-STATS-MIB", "qtechSyncStatsSlot"),
    (0, "QTECH-SYNC-STATS-MIB", "qtechSyncStatsConn"),
    (0, "QTECH-SYNC-STATS-MIB", "qtechSyncStatsChannel"),
)
if mibBuilder.loadTexts:
    qtechSyncStatsEntry.setStatus("current")
_QtechSyncStatsRowStatus_Type = RowStatus
_QtechSyncStatsRowStatus_Object = MibTableColumn
qtechSyncStatsRowStatus = _QtechSyncStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 1),
    _QtechSyncStatsRowStatus_Type()
)
qtechSyncStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSyncStatsRowStatus.setStatus("current")


class _QtechSyncStatsSlot_Type(Integer32):
    """Custom type qtechSyncStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechSyncStatsSlot_Type.__name__ = "Integer32"
_QtechSyncStatsSlot_Object = MibTableColumn
qtechSyncStatsSlot = _QtechSyncStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 2),
    _QtechSyncStatsSlot_Type()
)
qtechSyncStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsSlot.setStatus("current")


class _QtechSyncStatsConn_Type(Integer32):
    """Custom type qtechSyncStatsConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechSyncStatsConn_Type.__name__ = "Integer32"
_QtechSyncStatsConn_Object = MibTableColumn
qtechSyncStatsConn = _QtechSyncStatsConn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 3),
    _QtechSyncStatsConn_Type()
)
qtechSyncStatsConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsConn.setStatus("current")


class _QtechSyncStatsChannel_Type(Integer32):
    """Custom type qtechSyncStatsChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechSyncStatsChannel_Type.__name__ = "Integer32"
_QtechSyncStatsChannel_Object = MibTableColumn
qtechSyncStatsChannel = _QtechSyncStatsChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 4),
    _QtechSyncStatsChannel_Type()
)
qtechSyncStatsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsChannel.setStatus("current")
_QtechSyncStatsIfIndex_Type = InterfaceIndex
_QtechSyncStatsIfIndex_Object = MibTableColumn
qtechSyncStatsIfIndex = _QtechSyncStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 5),
    _QtechSyncStatsIfIndex_Type()
)
qtechSyncStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsIfIndex.setStatus("current")


class _QtechSyncStatsPortState_Type(Integer32):
    """Custom type qtechSyncStatsPortState based on Integer32"""
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


_QtechSyncStatsPortState_Type.__name__ = "Integer32"
_QtechSyncStatsPortState_Object = MibTableColumn
qtechSyncStatsPortState = _QtechSyncStatsPortState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 6),
    _QtechSyncStatsPortState_Type()
)
qtechSyncStatsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsPortState.setStatus("current")
_QtechSyncStatsRxFrames_Type = Counter32
_QtechSyncStatsRxFrames_Object = MibTableColumn
qtechSyncStatsRxFrames = _QtechSyncStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 7),
    _QtechSyncStatsRxFrames_Type()
)
qtechSyncStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxFrames.setStatus("current")
_QtechSyncStatsRxOctets_Type = Counter32
_QtechSyncStatsRxOctets_Object = MibTableColumn
qtechSyncStatsRxOctets = _QtechSyncStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 8),
    _QtechSyncStatsRxOctets_Type()
)
qtechSyncStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxOctets.setStatus("current")
_QtechSyncStatsRxReplenFails_Type = Counter32
_QtechSyncStatsRxReplenFails_Object = MibTableColumn
qtechSyncStatsRxReplenFails = _QtechSyncStatsRxReplenFails_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 9),
    _QtechSyncStatsRxReplenFails_Type()
)
qtechSyncStatsRxReplenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxReplenFails.setStatus("current")
_QtechSyncStatsRxClockErrors_Type = Counter32
_QtechSyncStatsRxClockErrors_Object = MibTableColumn
qtechSyncStatsRxClockErrors = _QtechSyncStatsRxClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 10),
    _QtechSyncStatsRxClockErrors_Type()
)
qtechSyncStatsRxClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxClockErrors.setStatus("current")
_QtechSyncStatsRxDpllErrors_Type = Counter32
_QtechSyncStatsRxDpllErrors_Object = MibTableColumn
qtechSyncStatsRxDpllErrors = _QtechSyncStatsRxDpllErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 11),
    _QtechSyncStatsRxDpllErrors_Type()
)
qtechSyncStatsRxDpllErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxDpllErrors.setStatus("current")
_QtechSyncStatsRxFrameTooLongErrors_Type = Counter32
_QtechSyncStatsRxFrameTooLongErrors_Object = MibTableColumn
qtechSyncStatsRxFrameTooLongErrors = _QtechSyncStatsRxFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 12),
    _QtechSyncStatsRxFrameTooLongErrors_Type()
)
qtechSyncStatsRxFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxFrameTooLongErrors.setStatus("current")
_QtechSyncStatsRxFrameOctetAlignErrors_Type = Counter32
_QtechSyncStatsRxFrameOctetAlignErrors_Object = MibTableColumn
qtechSyncStatsRxFrameOctetAlignErrors = _QtechSyncStatsRxFrameOctetAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 13),
    _QtechSyncStatsRxFrameOctetAlignErrors_Type()
)
qtechSyncStatsRxFrameOctetAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxFrameOctetAlignErrors.setStatus("current")
_QtechSyncStatsRxAbortErrors_Type = Counter32
_QtechSyncStatsRxAbortErrors_Object = MibTableColumn
qtechSyncStatsRxAbortErrors = _QtechSyncStatsRxAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 14),
    _QtechSyncStatsRxAbortErrors_Type()
)
qtechSyncStatsRxAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxAbortErrors.setStatus("current")
_QtechSyncStatsRxCrcErrors_Type = Counter32
_QtechSyncStatsRxCrcErrors_Object = MibTableColumn
qtechSyncStatsRxCrcErrors = _QtechSyncStatsRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 15),
    _QtechSyncStatsRxCrcErrors_Type()
)
qtechSyncStatsRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxCrcErrors.setStatus("current")
_QtechSyncStatsRxRcvrOverrunErrors_Type = Counter32
_QtechSyncStatsRxRcvrOverrunErrors_Object = MibTableColumn
qtechSyncStatsRxRcvrOverrunErrors = _QtechSyncStatsRxRcvrOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 16),
    _QtechSyncStatsRxRcvrOverrunErrors_Type()
)
qtechSyncStatsRxRcvrOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsRxRcvrOverrunErrors.setStatus("current")
_QtechSyncStatsTxFrames_Type = Counter32
_QtechSyncStatsTxFrames_Object = MibTableColumn
qtechSyncStatsTxFrames = _QtechSyncStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 17),
    _QtechSyncStatsTxFrames_Type()
)
qtechSyncStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsTxFrames.setStatus("current")
_QtechSyncStatsTxOctets_Type = Counter32
_QtechSyncStatsTxOctets_Object = MibTableColumn
qtechSyncStatsTxOctets = _QtechSyncStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 18),
    _QtechSyncStatsTxOctets_Type()
)
qtechSyncStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsTxOctets.setStatus("current")
_QtechSyncStatsTxRingFullDropsErrors_Type = Counter32
_QtechSyncStatsTxRingFullDropsErrors_Object = MibTableColumn
qtechSyncStatsTxRingFullDropsErrors = _QtechSyncStatsTxRingFullDropsErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 19),
    _QtechSyncStatsTxRingFullDropsErrors_Type()
)
qtechSyncStatsTxRingFullDropsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsTxRingFullDropsErrors.setStatus("current")
_QtechSyncStatsTxClockErrors_Type = Counter32
_QtechSyncStatsTxClockErrors_Object = MibTableColumn
qtechSyncStatsTxClockErrors = _QtechSyncStatsTxClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 20),
    _QtechSyncStatsTxClockErrors_Type()
)
qtechSyncStatsTxClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsTxClockErrors.setStatus("current")
_QtechSyncStatsTxFrameTooLongErrors_Type = Counter32
_QtechSyncStatsTxFrameTooLongErrors_Object = MibTableColumn
qtechSyncStatsTxFrameTooLongErrors = _QtechSyncStatsTxFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 21),
    _QtechSyncStatsTxFrameTooLongErrors_Type()
)
qtechSyncStatsTxFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsTxFrameTooLongErrors.setStatus("current")
_QtechSyncStatsTxUnderrunErrors_Type = Counter32
_QtechSyncStatsTxUnderrunErrors_Object = MibTableColumn
qtechSyncStatsTxUnderrunErrors = _QtechSyncStatsTxUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 1, 2, 1, 22),
    _QtechSyncStatsTxUnderrunErrors_Type()
)
qtechSyncStatsTxUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyncStatsTxUnderrunErrors.setStatus("current")
_QtechSyncStatsMibConformance_ObjectIdentity = ObjectIdentity
qtechSyncStatsMibConformance = _QtechSyncStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 2)
)
_QtechSyncStatsMibCompliances_ObjectIdentity = ObjectIdentity
qtechSyncStatsMibCompliances = _QtechSyncStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 2, 1)
)
_QtechSyncStatsMibGroups_ObjectIdentity = ObjectIdentity
qtechSyncStatsMibGroups = _QtechSyncStatsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 2, 2)
)

# Managed Objects groups

qtechSyncStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 2, 2, 1)
)
qtechSyncStatsGroup.setObjects(
      *(("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRowStatus"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsSlot"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsConn"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsChannel"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsIfIndex"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsPortState"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxFrames"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxOctets"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxReplenFails"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxClockErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxDpllErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxFrameTooLongErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxFrameOctetAlignErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxAbortErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxCrcErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsRxRcvrOverrunErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsTxFrames"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsTxOctets"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsTxRingFullDropsErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsTxClockErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsTxFrameTooLongErrors"),
        ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsTxUnderrunErrors"))
)
if mibBuilder.loadTexts:
    qtechSyncStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechSyncStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 51, 2, 1, 1)
)
qtechSyncStatsMibCompliance.setObjects(
    ("QTECH-SYNC-STATS-MIB", "qtechSyncStatsGroup")
)
if mibBuilder.loadTexts:
    qtechSyncStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SYNC-STATS-MIB",
    **{"qtechSyncStatsMIB": qtechSyncStatsMIB,
       "qtechSyncStatsMibObjects": qtechSyncStatsMibObjects,
       "qtechStatsSyncGlobal": qtechStatsSyncGlobal,
       "qtechSyncStatsTable": qtechSyncStatsTable,
       "qtechSyncStatsEntry": qtechSyncStatsEntry,
       "qtechSyncStatsRowStatus": qtechSyncStatsRowStatus,
       "qtechSyncStatsSlot": qtechSyncStatsSlot,
       "qtechSyncStatsConn": qtechSyncStatsConn,
       "qtechSyncStatsChannel": qtechSyncStatsChannel,
       "qtechSyncStatsIfIndex": qtechSyncStatsIfIndex,
       "qtechSyncStatsPortState": qtechSyncStatsPortState,
       "qtechSyncStatsRxFrames": qtechSyncStatsRxFrames,
       "qtechSyncStatsRxOctets": qtechSyncStatsRxOctets,
       "qtechSyncStatsRxReplenFails": qtechSyncStatsRxReplenFails,
       "qtechSyncStatsRxClockErrors": qtechSyncStatsRxClockErrors,
       "qtechSyncStatsRxDpllErrors": qtechSyncStatsRxDpllErrors,
       "qtechSyncStatsRxFrameTooLongErrors": qtechSyncStatsRxFrameTooLongErrors,
       "qtechSyncStatsRxFrameOctetAlignErrors": qtechSyncStatsRxFrameOctetAlignErrors,
       "qtechSyncStatsRxAbortErrors": qtechSyncStatsRxAbortErrors,
       "qtechSyncStatsRxCrcErrors": qtechSyncStatsRxCrcErrors,
       "qtechSyncStatsRxRcvrOverrunErrors": qtechSyncStatsRxRcvrOverrunErrors,
       "qtechSyncStatsTxFrames": qtechSyncStatsTxFrames,
       "qtechSyncStatsTxOctets": qtechSyncStatsTxOctets,
       "qtechSyncStatsTxRingFullDropsErrors": qtechSyncStatsTxRingFullDropsErrors,
       "qtechSyncStatsTxClockErrors": qtechSyncStatsTxClockErrors,
       "qtechSyncStatsTxFrameTooLongErrors": qtechSyncStatsTxFrameTooLongErrors,
       "qtechSyncStatsTxUnderrunErrors": qtechSyncStatsTxUnderrunErrors,
       "qtechSyncStatsMibConformance": qtechSyncStatsMibConformance,
       "qtechSyncStatsMibCompliances": qtechSyncStatsMibCompliances,
       "qtechSyncStatsMibCompliance": qtechSyncStatsMibCompliance,
       "qtechSyncStatsMibGroups": qtechSyncStatsMibGroups,
       "qtechSyncStatsGroup": qtechSyncStatsGroup}
)
