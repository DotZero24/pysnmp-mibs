# SNMP MIB module (IEEE8023-EtherLike-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/IEEE8023-EtherLike-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:18:42 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 org) = mibBuilder.importSymbols(
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
    "iso",
    "org")

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

ieee8023etherMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 3, 1, 10)
)
if mibBuilder.loadTexts:
    ieee8023etherMIB.setRevisions(
        ("2013-04-11 00:00",
         "2011-02-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8023etherMIBObjects_ObjectIdentity = ObjectIdentity
ieee8023etherMIBObjects = _Ieee8023etherMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 10, 1)
)
_Dot3StatsTable_Object = MibTable
dot3StatsTable = _Dot3StatsTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2)
)
if mibBuilder.loadTexts:
    dot3StatsTable.setStatus("current")
_Dot3StatsEntry_Object = MibTableRow
dot3StatsEntry = _Dot3StatsEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1)
)
dot3StatsEntry.setIndexNames(
    (0, "IEEE8023-EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3StatsEntry.setStatus("current")
_Dot3StatsIndex_Type = InterfaceIndex
_Dot3StatsIndex_Object = MibTableColumn
dot3StatsIndex = _Dot3StatsIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 1),
    _Dot3StatsIndex_Type()
)
dot3StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3StatsIndex.setStatus("current")
_Dot3StatsAlignmentErrors_Type = Counter32
_Dot3StatsAlignmentErrors_Object = MibTableColumn
dot3StatsAlignmentErrors = _Dot3StatsAlignmentErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 2),
    _Dot3StatsAlignmentErrors_Type()
)
dot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsAlignmentErrors.setStatus("current")
_Dot3StatsFCSErrors_Type = Counter32
_Dot3StatsFCSErrors_Object = MibTableColumn
dot3StatsFCSErrors = _Dot3StatsFCSErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 3),
    _Dot3StatsFCSErrors_Type()
)
dot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFCSErrors.setStatus("current")
_Dot3StatsSingleCollisionFrames_Type = Counter32
_Dot3StatsSingleCollisionFrames_Object = MibTableColumn
dot3StatsSingleCollisionFrames = _Dot3StatsSingleCollisionFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 4),
    _Dot3StatsSingleCollisionFrames_Type()
)
dot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setStatus("current")
_Dot3StatsMultipleCollisionFrames_Type = Counter32
_Dot3StatsMultipleCollisionFrames_Object = MibTableColumn
dot3StatsMultipleCollisionFrames = _Dot3StatsMultipleCollisionFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 5),
    _Dot3StatsMultipleCollisionFrames_Type()
)
dot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsMultipleCollisionFrames.setStatus("current")
_Dot3StatsSQETestErrors_Type = Counter32
_Dot3StatsSQETestErrors_Object = MibTableColumn
dot3StatsSQETestErrors = _Dot3StatsSQETestErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 6),
    _Dot3StatsSQETestErrors_Type()
)
dot3StatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSQETestErrors.setStatus("current")
_Dot3StatsDeferredTransmissions_Type = Counter32
_Dot3StatsDeferredTransmissions_Object = MibTableColumn
dot3StatsDeferredTransmissions = _Dot3StatsDeferredTransmissions_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 7),
    _Dot3StatsDeferredTransmissions_Type()
)
dot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDeferredTransmissions.setStatus("current")
_Dot3StatsLateCollisions_Type = Counter32
_Dot3StatsLateCollisions_Object = MibTableColumn
dot3StatsLateCollisions = _Dot3StatsLateCollisions_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 8),
    _Dot3StatsLateCollisions_Type()
)
dot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsLateCollisions.setStatus("current")
_Dot3StatsExcessiveCollisions_Type = Counter32
_Dot3StatsExcessiveCollisions_Object = MibTableColumn
dot3StatsExcessiveCollisions = _Dot3StatsExcessiveCollisions_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 9),
    _Dot3StatsExcessiveCollisions_Type()
)
dot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsExcessiveCollisions.setStatus("current")
_Dot3StatsInternalMacTransmitErrors_Type = Counter32
_Dot3StatsInternalMacTransmitErrors_Object = MibTableColumn
dot3StatsInternalMacTransmitErrors = _Dot3StatsInternalMacTransmitErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 10),
    _Dot3StatsInternalMacTransmitErrors_Type()
)
dot3StatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacTransmitErrors.setStatus("current")
_Dot3StatsCarrierSenseErrors_Type = Counter32
_Dot3StatsCarrierSenseErrors_Object = MibTableColumn
dot3StatsCarrierSenseErrors = _Dot3StatsCarrierSenseErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 11),
    _Dot3StatsCarrierSenseErrors_Type()
)
dot3StatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsCarrierSenseErrors.setStatus("current")
_Dot3StatsFrameTooLongs_Type = Counter32
_Dot3StatsFrameTooLongs_Object = MibTableColumn
dot3StatsFrameTooLongs = _Dot3StatsFrameTooLongs_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 13),
    _Dot3StatsFrameTooLongs_Type()
)
dot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setStatus("current")
_Dot3StatsInternalMacReceiveErrors_Type = Counter32
_Dot3StatsInternalMacReceiveErrors_Object = MibTableColumn
dot3StatsInternalMacReceiveErrors = _Dot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 16),
    _Dot3StatsInternalMacReceiveErrors_Type()
)
dot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacReceiveErrors.setStatus("current")
_Dot3StatsSymbolErrors_Type = Counter32
_Dot3StatsSymbolErrors_Object = MibTableColumn
dot3StatsSymbolErrors = _Dot3StatsSymbolErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 17),
    _Dot3StatsSymbolErrors_Type()
)
dot3StatsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSymbolErrors.setStatus("current")


class _Dot3StatsDuplexStatus_Type(Integer32):
    """Custom type dot3StatsDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("halfDuplex", 2),
          ("fullDuplex", 3))
    )


_Dot3StatsDuplexStatus_Type.__name__ = "Integer32"
_Dot3StatsDuplexStatus_Object = MibTableColumn
dot3StatsDuplexStatus = _Dot3StatsDuplexStatus_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 18),
    _Dot3StatsDuplexStatus_Type()
)
dot3StatsDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDuplexStatus.setStatus("current")
_Dot3StatsRateControlAbility_Type = TruthValue
_Dot3StatsRateControlAbility_Object = MibTableColumn
dot3StatsRateControlAbility = _Dot3StatsRateControlAbility_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 19),
    _Dot3StatsRateControlAbility_Type()
)
dot3StatsRateControlAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsRateControlAbility.setStatus("current")


class _Dot3StatsRateControlStatus_Type(Integer32):
    """Custom type dot3StatsRateControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rateControlOff", 1),
          ("rateControlOn", 2),
          ("unknown", 3))
    )


_Dot3StatsRateControlStatus_Type.__name__ = "Integer32"
_Dot3StatsRateControlStatus_Object = MibTableColumn
dot3StatsRateControlStatus = _Dot3StatsRateControlStatus_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 20),
    _Dot3StatsRateControlStatus_Type()
)
dot3StatsRateControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsRateControlStatus.setStatus("current")


class _Dot3StatsMaxFrameLength_Type(Integer32):
    """Custom type dot3StatsMaxFrameLength based on Integer32"""
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
        *(("unknown", 1),
          ("baseFrame", 2),
          ("qTaggedFrame", 3),
          ("envelopeFrame", 4))
    )


_Dot3StatsMaxFrameLength_Type.__name__ = "Integer32"
_Dot3StatsMaxFrameLength_Object = MibTableColumn
dot3StatsMaxFrameLength = _Dot3StatsMaxFrameLength_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 2, 1, 21),
    _Dot3StatsMaxFrameLength_Type()
)
dot3StatsMaxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsMaxFrameLength.setStatus("current")
_Dot3CollTable_Object = MibTable
dot3CollTable = _Dot3CollTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 5)
)
if mibBuilder.loadTexts:
    dot3CollTable.setStatus("current")
_Dot3CollEntry_Object = MibTableRow
dot3CollEntry = _Dot3CollEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 5, 1)
)
dot3CollEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE8023-EtherLike-MIB", "dot3CollCount"),
)
if mibBuilder.loadTexts:
    dot3CollEntry.setStatus("current")


class _Dot3CollCount_Type(Integer32):
    """Custom type dot3CollCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dot3CollCount_Type.__name__ = "Integer32"
_Dot3CollCount_Object = MibTableColumn
dot3CollCount = _Dot3CollCount_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 5, 1, 2),
    _Dot3CollCount_Type()
)
dot3CollCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3CollCount.setStatus("current")
_Dot3CollFrequencies_Type = Counter32
_Dot3CollFrequencies_Object = MibTableColumn
dot3CollFrequencies = _Dot3CollFrequencies_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 5, 1, 3),
    _Dot3CollFrequencies_Type()
)
dot3CollFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollFrequencies.setStatus("current")
_Dot3ControlTable_Object = MibTable
dot3ControlTable = _Dot3ControlTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 9)
)
if mibBuilder.loadTexts:
    dot3ControlTable.setStatus("current")
_Dot3ControlEntry_Object = MibTableRow
dot3ControlEntry = _Dot3ControlEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 9, 1)
)
dot3ControlEntry.setIndexNames(
    (0, "IEEE8023-EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3ControlEntry.setStatus("current")


class _Dot3ControlFunctionsSupported_Type(Bits):
    """Custom type dot3ControlFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("pause", 0),
          ("mpcp", 1),
          ("pfc", 2))
    )

_Dot3ControlFunctionsSupported_Type.__name__ = "Bits"
_Dot3ControlFunctionsSupported_Object = MibTableColumn
dot3ControlFunctionsSupported = _Dot3ControlFunctionsSupported_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 9, 1, 1),
    _Dot3ControlFunctionsSupported_Type()
)
dot3ControlFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ControlFunctionsSupported.setStatus("current")
_Dot3ControlInUnknownOpcodes_Type = Counter32
_Dot3ControlInUnknownOpcodes_Object = MibTableColumn
dot3ControlInUnknownOpcodes = _Dot3ControlInUnknownOpcodes_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 9, 1, 2),
    _Dot3ControlInUnknownOpcodes_Type()
)
dot3ControlInUnknownOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ControlInUnknownOpcodes.setStatus("current")
_Dot3HCControlInUnknownOpcodes_Type = Counter64
_Dot3HCControlInUnknownOpcodes_Object = MibTableColumn
dot3HCControlInUnknownOpcodes = _Dot3HCControlInUnknownOpcodes_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 9, 1, 3),
    _Dot3HCControlInUnknownOpcodes_Type()
)
dot3HCControlInUnknownOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCControlInUnknownOpcodes.setStatus("current")
_Dot3PauseTable_Object = MibTable
dot3PauseTable = _Dot3PauseTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 10)
)
if mibBuilder.loadTexts:
    dot3PauseTable.setStatus("current")
_Dot3PauseEntry_Object = MibTableRow
dot3PauseEntry = _Dot3PauseEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 10, 1)
)
dot3PauseEntry.setIndexNames(
    (0, "IEEE8023-EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3PauseEntry.setStatus("current")


class _Dot3PauseAdminMode_Type(Integer32):
    """Custom type dot3PauseAdminMode based on Integer32"""
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
        *(("disabled", 1),
          ("enabledXmit", 2),
          ("enabledRcv", 3),
          ("enabledXmitAndRcv", 4))
    )


_Dot3PauseAdminMode_Type.__name__ = "Integer32"
_Dot3PauseAdminMode_Object = MibTableColumn
dot3PauseAdminMode = _Dot3PauseAdminMode_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 10, 1, 1),
    _Dot3PauseAdminMode_Type()
)
dot3PauseAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3PauseAdminMode.setStatus("current")


class _Dot3PauseOperMode_Type(Integer32):
    """Custom type dot3PauseOperMode based on Integer32"""
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
        *(("disabled", 1),
          ("enabledXmit", 2),
          ("enabledRcv", 3),
          ("enabledXmitAndRcv", 4))
    )


_Dot3PauseOperMode_Type.__name__ = "Integer32"
_Dot3PauseOperMode_Object = MibTableColumn
dot3PauseOperMode = _Dot3PauseOperMode_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 10, 1, 2),
    _Dot3PauseOperMode_Type()
)
dot3PauseOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3PauseOperMode.setStatus("current")
_Dot3InPauseFrames_Type = Counter32
_Dot3InPauseFrames_Object = MibTableColumn
dot3InPauseFrames = _Dot3InPauseFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 10, 1, 3),
    _Dot3InPauseFrames_Type()
)
dot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3InPauseFrames.setStatus("current")
_Dot3OutPauseFrames_Type = Counter32
_Dot3OutPauseFrames_Object = MibTableColumn
dot3OutPauseFrames = _Dot3OutPauseFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 10, 1, 4),
    _Dot3OutPauseFrames_Type()
)
dot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OutPauseFrames.setStatus("current")
_Dot3HCInPauseFrames_Type = Counter64
_Dot3HCInPauseFrames_Object = MibTableColumn
dot3HCInPauseFrames = _Dot3HCInPauseFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 10, 1, 5),
    _Dot3HCInPauseFrames_Type()
)
dot3HCInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCInPauseFrames.setStatus("current")
_Dot3HCOutPauseFrames_Type = Counter64
_Dot3HCOutPauseFrames_Object = MibTableColumn
dot3HCOutPauseFrames = _Dot3HCOutPauseFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 10, 1, 6),
    _Dot3HCOutPauseFrames_Type()
)
dot3HCOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCOutPauseFrames.setStatus("current")
_Dot3HCStatsTable_Object = MibTable
dot3HCStatsTable = _Dot3HCStatsTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11)
)
if mibBuilder.loadTexts:
    dot3HCStatsTable.setStatus("current")
_Dot3HCStatsEntry_Object = MibTableRow
dot3HCStatsEntry = _Dot3HCStatsEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1)
)
dot3HCStatsEntry.setIndexNames(
    (0, "IEEE8023-EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3HCStatsEntry.setStatus("current")
_Dot3HCStatsAlignmentErrors_Type = Counter64
_Dot3HCStatsAlignmentErrors_Object = MibTableColumn
dot3HCStatsAlignmentErrors = _Dot3HCStatsAlignmentErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 1),
    _Dot3HCStatsAlignmentErrors_Type()
)
dot3HCStatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsAlignmentErrors.setStatus("current")
_Dot3HCStatsFCSErrors_Type = Counter64
_Dot3HCStatsFCSErrors_Object = MibTableColumn
dot3HCStatsFCSErrors = _Dot3HCStatsFCSErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 2),
    _Dot3HCStatsFCSErrors_Type()
)
dot3HCStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsFCSErrors.setStatus("current")
_Dot3HCStatsInternalMacTransmitErrors_Type = Counter64
_Dot3HCStatsInternalMacTransmitErrors_Object = MibTableColumn
dot3HCStatsInternalMacTransmitErrors = _Dot3HCStatsInternalMacTransmitErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 3),
    _Dot3HCStatsInternalMacTransmitErrors_Type()
)
dot3HCStatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsInternalMacTransmitErrors.setStatus("current")
_Dot3HCStatsFrameTooLongs_Type = Counter64
_Dot3HCStatsFrameTooLongs_Object = MibTableColumn
dot3HCStatsFrameTooLongs = _Dot3HCStatsFrameTooLongs_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 4),
    _Dot3HCStatsFrameTooLongs_Type()
)
dot3HCStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsFrameTooLongs.setStatus("current")
_Dot3HCStatsInternalMacReceiveErrors_Type = Counter64
_Dot3HCStatsInternalMacReceiveErrors_Object = MibTableColumn
dot3HCStatsInternalMacReceiveErrors = _Dot3HCStatsInternalMacReceiveErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 5),
    _Dot3HCStatsInternalMacReceiveErrors_Type()
)
dot3HCStatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsInternalMacReceiveErrors.setStatus("current")
_Dot3HCStatsSymbolErrors_Type = Counter64
_Dot3HCStatsSymbolErrors_Object = MibTableColumn
dot3HCStatsSymbolErrors = _Dot3HCStatsSymbolErrors_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 6),
    _Dot3HCStatsSymbolErrors_Type()
)
dot3HCStatsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsSymbolErrors.setStatus("current")
_Dot3HCStatsTransmitLPIMicroseconds_Type = Counter64
_Dot3HCStatsTransmitLPIMicroseconds_Object = MibTableColumn
dot3HCStatsTransmitLPIMicroseconds = _Dot3HCStatsTransmitLPIMicroseconds_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 7),
    _Dot3HCStatsTransmitLPIMicroseconds_Type()
)
dot3HCStatsTransmitLPIMicroseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsTransmitLPIMicroseconds.setStatus("current")
_Dot3HCStatsReceiveLPIMicroseconds_Type = Counter64
_Dot3HCStatsReceiveLPIMicroseconds_Object = MibTableColumn
dot3HCStatsReceiveLPIMicroseconds = _Dot3HCStatsReceiveLPIMicroseconds_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 8),
    _Dot3HCStatsReceiveLPIMicroseconds_Type()
)
dot3HCStatsReceiveLPIMicroseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsReceiveLPIMicroseconds.setStatus("current")
_Dot3HCStatsTransmitLPITransitions_Type = Counter64
_Dot3HCStatsTransmitLPITransitions_Object = MibTableColumn
dot3HCStatsTransmitLPITransitions = _Dot3HCStatsTransmitLPITransitions_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 9),
    _Dot3HCStatsTransmitLPITransitions_Type()
)
dot3HCStatsTransmitLPITransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsTransmitLPITransitions.setStatus("current")
_Dot3HCStatsReceiveLPITransitions_Type = Counter64
_Dot3HCStatsReceiveLPITransitions_Object = MibTableColumn
dot3HCStatsReceiveLPITransitions = _Dot3HCStatsReceiveLPITransitions_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 11, 1, 10),
    _Dot3HCStatsReceiveLPITransitions_Type()
)
dot3HCStatsReceiveLPITransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsReceiveLPITransitions.setStatus("current")


class _Dot3SlowProtocolFrameLimit_Type(Integer32):
    """Custom type dot3SlowProtocolFrameLimit based on Integer32"""
    defaultValue = 10


_Dot3SlowProtocolFrameLimit_Type.__name__ = "Integer32"
_Dot3SlowProtocolFrameLimit_Object = MibScalar
dot3SlowProtocolFrameLimit = _Dot3SlowProtocolFrameLimit_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 12),
    _Dot3SlowProtocolFrameLimit_Type()
)
dot3SlowProtocolFrameLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3SlowProtocolFrameLimit.setStatus("current")
_Dot3ExtensionTable_Object = MibTable
dot3ExtensionTable = _Dot3ExtensionTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 13)
)
if mibBuilder.loadTexts:
    dot3ExtensionTable.setStatus("current")
_Dot3ExtensionEntry_Object = MibTableRow
dot3ExtensionEntry = _Dot3ExtensionEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 13, 1)
)
dot3ExtensionEntry.setIndexNames(
    (0, "IEEE8023-EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3ExtensionEntry.setStatus("current")
_Dot3HCInExtensionFrames_Type = Counter64
_Dot3HCInExtensionFrames_Object = MibTableColumn
dot3HCInExtensionFrames = _Dot3HCInExtensionFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 13, 1, 1),
    _Dot3HCInExtensionFrames_Type()
)
dot3HCInExtensionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCInExtensionFrames.setStatus("current")
_Dot3HCOutExtensionFrames_Type = Counter64
_Dot3HCOutExtensionFrames_Object = MibTableColumn
dot3HCOutExtensionFrames = _Dot3HCOutExtensionFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 13, 1, 2),
    _Dot3HCOutExtensionFrames_Type()
)
dot3HCOutExtensionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCOutExtensionFrames.setStatus("current")
_Dot3ExtensionMacCtrlStatus_Type = Unsigned32
_Dot3ExtensionMacCtrlStatus_Object = MibTableColumn
dot3ExtensionMacCtrlStatus = _Dot3ExtensionMacCtrlStatus_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 13, 1, 3),
    _Dot3ExtensionMacCtrlStatus_Type()
)
dot3ExtensionMacCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ExtensionMacCtrlStatus.setStatus("current")
_Dot3PFCTable_Object = MibTable
dot3PFCTable = _Dot3PFCTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 14)
)
if mibBuilder.loadTexts:
    dot3PFCTable.setStatus("current")
_Dot3PFCEntry_Object = MibTableRow
dot3PFCEntry = _Dot3PFCEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 14, 1)
)
dot3PFCEntry.setIndexNames(
    (0, "IEEE8023-EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3PFCEntry.setStatus("current")


class _Dot3PFCAdminMode_Type(Integer32):
    """Custom type dot3PFCAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Dot3PFCAdminMode_Type.__name__ = "Integer32"
_Dot3PFCAdminMode_Object = MibTableColumn
dot3PFCAdminMode = _Dot3PFCAdminMode_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 14, 1, 1),
    _Dot3PFCAdminMode_Type()
)
dot3PFCAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3PFCAdminMode.setStatus("current")


class _Dot3PFCOperMode_Type(Integer32):
    """Custom type dot3PFCOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Dot3PFCOperMode_Type.__name__ = "Integer32"
_Dot3PFCOperMode_Object = MibTableColumn
dot3PFCOperMode = _Dot3PFCOperMode_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 14, 1, 2),
    _Dot3PFCOperMode_Type()
)
dot3PFCOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3PFCOperMode.setStatus("current")
_Dot3HCInPFCFrames_Type = Counter64
_Dot3HCInPFCFrames_Object = MibTableColumn
dot3HCInPFCFrames = _Dot3HCInPFCFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 14, 1, 3),
    _Dot3HCInPFCFrames_Type()
)
dot3HCInPFCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCInPFCFrames.setStatus("current")
_Dot3HCOutPFCFrames_Type = Counter64
_Dot3HCOutPFCFrames_Object = MibTableColumn
dot3HCOutPFCFrames = _Dot3HCOutPFCFrames_Object(
    (1, 3, 111, 2, 802, 3, 1, 10, 1, 14, 1, 4),
    _Dot3HCOutPFCFrames_Type()
)
dot3HCOutPFCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCOutPFCFrames.setStatus("current")
_EtherConformance_ObjectIdentity = ObjectIdentity
etherConformance = _EtherConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 10, 2)
)
_EtherGroups_ObjectIdentity = ObjectIdentity
etherGroups = _EtherGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1)
)
_EtherCompliances_ObjectIdentity = ObjectIdentity
etherCompliances = _EtherCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 2)
)

# Managed Objects groups

etherCollisionTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 1)
)
etherCollisionTableGroup.setObjects(
    ("IEEE8023-EtherLike-MIB", "dot3CollFrequencies")
)
if mibBuilder.loadTexts:
    etherCollisionTableGroup.setStatus("current")

etherStatsLowSpeedGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 2)
)
etherStatsLowSpeedGroup.setObjects(
    ("IEEE8023-EtherLike-MIB", "dot3StatsSQETestErrors")
)
if mibBuilder.loadTexts:
    etherStatsLowSpeedGroup.setStatus("current")

etherStatsHighSpeedGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 3)
)
etherStatsHighSpeedGroup.setObjects(
    ("IEEE8023-EtherLike-MIB", "dot3StatsSymbolErrors")
)
if mibBuilder.loadTexts:
    etherStatsHighSpeedGroup.setStatus("current")

etherDuplexGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 4)
)
etherDuplexGroup.setObjects(
    ("IEEE8023-EtherLike-MIB", "dot3StatsDuplexStatus")
)
if mibBuilder.loadTexts:
    etherDuplexGroup.setStatus("current")

etherControlGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 5)
)
etherControlGroup.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3ControlFunctionsSupported"),
        ("IEEE8023-EtherLike-MIB", "dot3ControlInUnknownOpcodes"))
)
if mibBuilder.loadTexts:
    etherControlGroup.setStatus("current")

etherControlPauseGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 6)
)
etherControlPauseGroup.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3PauseAdminMode"),
        ("IEEE8023-EtherLike-MIB", "dot3PauseOperMode"),
        ("IEEE8023-EtherLike-MIB", "dot3InPauseFrames"),
        ("IEEE8023-EtherLike-MIB", "dot3OutPauseFrames"))
)
if mibBuilder.loadTexts:
    etherControlPauseGroup.setStatus("current")

etherStatsBaseGroup2 = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 7)
)
etherStatsBaseGroup2.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3StatsAlignmentErrors"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsFCSErrors"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsFrameTooLongs"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsMaxFrameLength"))
)
if mibBuilder.loadTexts:
    etherStatsBaseGroup2.setStatus("current")

etherStatsHalfDuplexGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 8)
)
etherStatsHalfDuplexGroup.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3StatsSingleCollisionFrames"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsMultipleCollisionFrames"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsDeferredTransmissions"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsLateCollisions"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsExcessiveCollisions"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsCarrierSenseErrors"))
)
if mibBuilder.loadTexts:
    etherStatsHalfDuplexGroup.setStatus("current")

etherHCStatsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 9)
)
etherHCStatsGroup.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3HCStatsAlignmentErrors"),
        ("IEEE8023-EtherLike-MIB", "dot3HCStatsFCSErrors"),
        ("IEEE8023-EtherLike-MIB", "dot3HCStatsInternalMacTransmitErrors"),
        ("IEEE8023-EtherLike-MIB", "dot3HCStatsFrameTooLongs"),
        ("IEEE8023-EtherLike-MIB", "dot3HCStatsInternalMacReceiveErrors"),
        ("IEEE8023-EtherLike-MIB", "dot3HCStatsSymbolErrors"))
)
if mibBuilder.loadTexts:
    etherHCStatsGroup.setStatus("current")

etherHCControlGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 10)
)
etherHCControlGroup.setObjects(
    ("IEEE8023-EtherLike-MIB", "dot3HCControlInUnknownOpcodes")
)
if mibBuilder.loadTexts:
    etherHCControlGroup.setStatus("current")

etherHCControlPauseGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 11)
)
etherHCControlPauseGroup.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3HCInPauseFrames"),
        ("IEEE8023-EtherLike-MIB", "dot3HCOutPauseFrames"))
)
if mibBuilder.loadTexts:
    etherHCControlPauseGroup.setStatus("current")

etherRateControlGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 12)
)
etherRateControlGroup.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3StatsRateControlAbility"),
        ("IEEE8023-EtherLike-MIB", "dot3StatsRateControlStatus"))
)
if mibBuilder.loadTexts:
    etherRateControlGroup.setStatus("current")

etherHCStatsLpiGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 13)
)
etherHCStatsLpiGroup.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3HCStatsTransmitLPIMicroseconds"),
        ("IEEE8023-EtherLike-MIB", "dot3HCStatsReceiveLPIMicroseconds"),
        ("IEEE8023-EtherLike-MIB", "dot3HCStatsTransmitLPITransitions"),
        ("IEEE8023-EtherLike-MIB", "dot3HCStatsReceiveLPITransitions"))
)
if mibBuilder.loadTexts:
    etherHCStatsLpiGroup.setStatus("current")

etherSlowProtocolsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 14)
)
etherSlowProtocolsGroup.setObjects(
    ("IEEE8023-EtherLike-MIB", "dot3SlowProtocolFrameLimit")
)
if mibBuilder.loadTexts:
    etherSlowProtocolsGroup.setStatus("current")

etherExtensionMacCtrlGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 15)
)
etherExtensionMacCtrlGroup.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3HCInExtensionFrames"),
        ("IEEE8023-EtherLike-MIB", "dot3HCOutExtensionFrames"),
        ("IEEE8023-EtherLike-MIB", "dot3ExtensionMacCtrlStatus"))
)
if mibBuilder.loadTexts:
    etherExtensionMacCtrlGroup.setStatus("current")

etherPfcGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 1, 16)
)
etherPfcGroup.setObjects(
      *(("IEEE8023-EtherLike-MIB", "dot3PFCAdminMode"),
        ("IEEE8023-EtherLike-MIB", "dot3PFCOperMode"),
        ("IEEE8023-EtherLike-MIB", "dot3HCInPFCFrames"),
        ("IEEE8023-EtherLike-MIB", "dot3HCOutPFCFrames"))
)
if mibBuilder.loadTexts:
    etherPfcGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dot3Compliance2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 3, 1, 10, 2, 2, 1)
)
dot3Compliance2.setObjects(
      *(("IEEE8023-EtherLike-MIB", "etherStatsBaseGroup2"),
        ("IEEE8023-EtherLike-MIB", "etherDuplexGroup"),
        ("IEEE8023-EtherLike-MIB", "etherRateControlGroup"),
        ("IEEE8023-EtherLike-MIB", "etherStatsLowSpeedGroup"),
        ("IEEE8023-EtherLike-MIB", "etherStatsHighSpeedGroup"),
        ("IEEE8023-EtherLike-MIB", "etherStatsHalfDuplexGroup"),
        ("IEEE8023-EtherLike-MIB", "etherHCStatsGroup"),
        ("IEEE8023-EtherLike-MIB", "etherControlGroup"),
        ("IEEE8023-EtherLike-MIB", "etherHCControlGroup"),
        ("IEEE8023-EtherLike-MIB", "etherControlPauseGroup"),
        ("IEEE8023-EtherLike-MIB", "etherHCControlPauseGroup"),
        ("IEEE8023-EtherLike-MIB", "etherCollisionTableGroup"),
        ("IEEE8023-EtherLike-MIB", "etherHCStatsLpiGroup"),
        ("IEEE8023-EtherLike-MIB", "etherSlowProtocolsGroup"),
        ("IEEE8023-EtherLike-MIB", "etherExtensionMacCtrlGroup"),
        ("IEEE8023-EtherLike-MIB", "etherPfcGroup"))
)
if mibBuilder.loadTexts:
    dot3Compliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8023-EtherLike-MIB",
    **{"ieee8023etherMIB": ieee8023etherMIB,
       "ieee8023etherMIBObjects": ieee8023etherMIBObjects,
       "dot3StatsTable": dot3StatsTable,
       "dot3StatsEntry": dot3StatsEntry,
       "dot3StatsIndex": dot3StatsIndex,
       "dot3StatsAlignmentErrors": dot3StatsAlignmentErrors,
       "dot3StatsFCSErrors": dot3StatsFCSErrors,
       "dot3StatsSingleCollisionFrames": dot3StatsSingleCollisionFrames,
       "dot3StatsMultipleCollisionFrames": dot3StatsMultipleCollisionFrames,
       "dot3StatsSQETestErrors": dot3StatsSQETestErrors,
       "dot3StatsDeferredTransmissions": dot3StatsDeferredTransmissions,
       "dot3StatsLateCollisions": dot3StatsLateCollisions,
       "dot3StatsExcessiveCollisions": dot3StatsExcessiveCollisions,
       "dot3StatsInternalMacTransmitErrors": dot3StatsInternalMacTransmitErrors,
       "dot3StatsCarrierSenseErrors": dot3StatsCarrierSenseErrors,
       "dot3StatsFrameTooLongs": dot3StatsFrameTooLongs,
       "dot3StatsInternalMacReceiveErrors": dot3StatsInternalMacReceiveErrors,
       "dot3StatsSymbolErrors": dot3StatsSymbolErrors,
       "dot3StatsDuplexStatus": dot3StatsDuplexStatus,
       "dot3StatsRateControlAbility": dot3StatsRateControlAbility,
       "dot3StatsRateControlStatus": dot3StatsRateControlStatus,
       "dot3StatsMaxFrameLength": dot3StatsMaxFrameLength,
       "dot3CollTable": dot3CollTable,
       "dot3CollEntry": dot3CollEntry,
       "dot3CollCount": dot3CollCount,
       "dot3CollFrequencies": dot3CollFrequencies,
       "dot3ControlTable": dot3ControlTable,
       "dot3ControlEntry": dot3ControlEntry,
       "dot3ControlFunctionsSupported": dot3ControlFunctionsSupported,
       "dot3ControlInUnknownOpcodes": dot3ControlInUnknownOpcodes,
       "dot3HCControlInUnknownOpcodes": dot3HCControlInUnknownOpcodes,
       "dot3PauseTable": dot3PauseTable,
       "dot3PauseEntry": dot3PauseEntry,
       "dot3PauseAdminMode": dot3PauseAdminMode,
       "dot3PauseOperMode": dot3PauseOperMode,
       "dot3InPauseFrames": dot3InPauseFrames,
       "dot3OutPauseFrames": dot3OutPauseFrames,
       "dot3HCInPauseFrames": dot3HCInPauseFrames,
       "dot3HCOutPauseFrames": dot3HCOutPauseFrames,
       "dot3HCStatsTable": dot3HCStatsTable,
       "dot3HCStatsEntry": dot3HCStatsEntry,
       "dot3HCStatsAlignmentErrors": dot3HCStatsAlignmentErrors,
       "dot3HCStatsFCSErrors": dot3HCStatsFCSErrors,
       "dot3HCStatsInternalMacTransmitErrors": dot3HCStatsInternalMacTransmitErrors,
       "dot3HCStatsFrameTooLongs": dot3HCStatsFrameTooLongs,
       "dot3HCStatsInternalMacReceiveErrors": dot3HCStatsInternalMacReceiveErrors,
       "dot3HCStatsSymbolErrors": dot3HCStatsSymbolErrors,
       "dot3HCStatsTransmitLPIMicroseconds": dot3HCStatsTransmitLPIMicroseconds,
       "dot3HCStatsReceiveLPIMicroseconds": dot3HCStatsReceiveLPIMicroseconds,
       "dot3HCStatsTransmitLPITransitions": dot3HCStatsTransmitLPITransitions,
       "dot3HCStatsReceiveLPITransitions": dot3HCStatsReceiveLPITransitions,
       "dot3SlowProtocolFrameLimit": dot3SlowProtocolFrameLimit,
       "dot3ExtensionTable": dot3ExtensionTable,
       "dot3ExtensionEntry": dot3ExtensionEntry,
       "dot3HCInExtensionFrames": dot3HCInExtensionFrames,
       "dot3HCOutExtensionFrames": dot3HCOutExtensionFrames,
       "dot3ExtensionMacCtrlStatus": dot3ExtensionMacCtrlStatus,
       "dot3PFCTable": dot3PFCTable,
       "dot3PFCEntry": dot3PFCEntry,
       "dot3PFCAdminMode": dot3PFCAdminMode,
       "dot3PFCOperMode": dot3PFCOperMode,
       "dot3HCInPFCFrames": dot3HCInPFCFrames,
       "dot3HCOutPFCFrames": dot3HCOutPFCFrames,
       "etherConformance": etherConformance,
       "etherGroups": etherGroups,
       "etherCollisionTableGroup": etherCollisionTableGroup,
       "etherStatsLowSpeedGroup": etherStatsLowSpeedGroup,
       "etherStatsHighSpeedGroup": etherStatsHighSpeedGroup,
       "etherDuplexGroup": etherDuplexGroup,
       "etherControlGroup": etherControlGroup,
       "etherControlPauseGroup": etherControlPauseGroup,
       "etherStatsBaseGroup2": etherStatsBaseGroup2,
       "etherStatsHalfDuplexGroup": etherStatsHalfDuplexGroup,
       "etherHCStatsGroup": etherHCStatsGroup,
       "etherHCControlGroup": etherHCControlGroup,
       "etherHCControlPauseGroup": etherHCControlPauseGroup,
       "etherRateControlGroup": etherRateControlGroup,
       "etherHCStatsLpiGroup": etherHCStatsLpiGroup,
       "etherSlowProtocolsGroup": etherSlowProtocolsGroup,
       "etherExtensionMacCtrlGroup": etherExtensionMacCtrlGroup,
       "etherPfcGroup": etherPfcGroup,
       "etherCompliances": etherCompliances,
       "dot3Compliance2": dot3Compliance2}
)
