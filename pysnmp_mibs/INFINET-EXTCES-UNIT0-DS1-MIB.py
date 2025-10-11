# SNMP MIB module (INFINET-EXTCES-UNIT0-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/INFINET-EXTCES-UNIT0-DS1-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:02 2025
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

(cesOverWlanUnit0,) = mibBuilder.importSymbols(
    "INFINET-EXTCES-MIB",
    "cesOverWlanUnit0")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cesOverWlanUnit0Ds1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Ds1.setRevisions(
        ("2004-08-16 19:10",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CesOverWlanUnit0Dsx1ConfigTable_Object = MibTable
cesOverWlanUnit0Dsx1ConfigTable = _CesOverWlanUnit0Dsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1ConfigTable.setStatus("current")
_CesOverWlanUnit0Dsx1ConfigEntry_Object = MibTableRow
cesOverWlanUnit0Dsx1ConfigEntry = _CesOverWlanUnit0Dsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1)
)
cesOverWlanUnit0Dsx1ConfigEntry.setIndexNames(
    (0, "INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1ConfigEntry.setStatus("current")
_CesOverWlanUnit0Dsx1LineIndex_Type = InterfaceIndex
_CesOverWlanUnit0Dsx1LineIndex_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineIndex = _CesOverWlanUnit0Dsx1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 1),
    _CesOverWlanUnit0Dsx1LineIndex_Type()
)
cesOverWlanUnit0Dsx1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineIndex.setStatus("current")
_CesOverWlanUnit0Dsx1IfIndex_Type = InterfaceIndex
_CesOverWlanUnit0Dsx1IfIndex_Object = MibTableColumn
cesOverWlanUnit0Dsx1IfIndex = _CesOverWlanUnit0Dsx1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 2),
    _CesOverWlanUnit0Dsx1IfIndex_Type()
)
cesOverWlanUnit0Dsx1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IfIndex.setStatus("deprecated")


class _CesOverWlanUnit0Dsx1TimeElapsed_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1TimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_CesOverWlanUnit0Dsx1TimeElapsed_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1TimeElapsed_Object = MibTableColumn
cesOverWlanUnit0Dsx1TimeElapsed = _CesOverWlanUnit0Dsx1TimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 3),
    _CesOverWlanUnit0Dsx1TimeElapsed_Type()
)
cesOverWlanUnit0Dsx1TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TimeElapsed.setStatus("current")


class _CesOverWlanUnit0Dsx1ValidIntervals_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CesOverWlanUnit0Dsx1ValidIntervals_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1ValidIntervals_Object = MibTableColumn
cesOverWlanUnit0Dsx1ValidIntervals = _CesOverWlanUnit0Dsx1ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 4),
    _CesOverWlanUnit0Dsx1ValidIntervals_Type()
)
cesOverWlanUnit0Dsx1ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1ValidIntervals.setStatus("current")


class _CesOverWlanUnit0Dsx1LineType_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dsx1ESF", 2),
          ("dsx1D4", 3),
          ("dsx1E1", 4),
          ("dsx1E1CRC", 5),
          ("dsx1E1MF", 6),
          ("dsx1E1CRCMF", 7),
          ("dsx1Unframed", 8),
          ("dsx1E1Unframed", 9),
          ("dsx1DS2M12", 10),
          ("dsx1E2", 11),
          ("dsx1E1Q50", 12),
          ("dsx1E1Q50CRC", 13),
          ("dsx1J1ESF", 14),
          ("dsx1J1Unframed", 16))
    )


_CesOverWlanUnit0Dsx1LineType_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LineType_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineType = _CesOverWlanUnit0Dsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 5),
    _CesOverWlanUnit0Dsx1LineType_Type()
)
cesOverWlanUnit0Dsx1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineType.setStatus("current")


class _CesOverWlanUnit0Dsx1LineCoding_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dsx1JBZS", 1),
          ("dsx1B8ZS", 2),
          ("dsx1HDB3", 3),
          ("dsx1ZBTSI", 4),
          ("dsx1AMI", 5),
          ("other", 6),
          ("dsx1B6ZS", 7))
    )


_CesOverWlanUnit0Dsx1LineCoding_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LineCoding_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineCoding = _CesOverWlanUnit0Dsx1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 6),
    _CesOverWlanUnit0Dsx1LineCoding_Type()
)
cesOverWlanUnit0Dsx1LineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineCoding.setStatus("current")


class _CesOverWlanUnit0Dsx1SendCode_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1SendCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dsx1SendNoCode", 1),
          ("dsx1SendLineCode", 2),
          ("dsx1SendPayloadCode", 3),
          ("dsx1SendResetCode", 4),
          ("dsx1SendQRS", 5),
          ("dsx1Send511Pattern", 6),
          ("dsx1Send3in24Pattern", 7),
          ("dsx1SendOtherTestPattern", 8))
    )


_CesOverWlanUnit0Dsx1SendCode_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1SendCode_Object = MibTableColumn
cesOverWlanUnit0Dsx1SendCode = _CesOverWlanUnit0Dsx1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 7),
    _CesOverWlanUnit0Dsx1SendCode_Type()
)
cesOverWlanUnit0Dsx1SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1SendCode.setStatus("current")


class _CesOverWlanUnit0Dsx1CircuitIdentifier_Type(DisplayString):
    """Custom type cesOverWlanUnit0Dsx1CircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CesOverWlanUnit0Dsx1CircuitIdentifier_Type.__name__ = "DisplayString"
_CesOverWlanUnit0Dsx1CircuitIdentifier_Object = MibTableColumn
cesOverWlanUnit0Dsx1CircuitIdentifier = _CesOverWlanUnit0Dsx1CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 8),
    _CesOverWlanUnit0Dsx1CircuitIdentifier_Type()
)
cesOverWlanUnit0Dsx1CircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CircuitIdentifier.setStatus("current")


class _CesOverWlanUnit0Dsx1LoopbackConfig_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dsx1NoLoop", 1),
          ("dsx1PayloadLoop", 2),
          ("dsx1LineLoop", 3),
          ("dsx1OtherLoop", 4),
          ("dsx1InwardLoop", 5),
          ("dsx1DualLoop", 6))
    )


_CesOverWlanUnit0Dsx1LoopbackConfig_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LoopbackConfig_Object = MibTableColumn
cesOverWlanUnit0Dsx1LoopbackConfig = _CesOverWlanUnit0Dsx1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 9),
    _CesOverWlanUnit0Dsx1LoopbackConfig_Type()
)
cesOverWlanUnit0Dsx1LoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LoopbackConfig.setStatus("current")


class _CesOverWlanUnit0Dsx1LineStatus_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131071),
    )


_CesOverWlanUnit0Dsx1LineStatus_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LineStatus_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineStatus = _CesOverWlanUnit0Dsx1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 10),
    _CesOverWlanUnit0Dsx1LineStatus_Type()
)
cesOverWlanUnit0Dsx1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineStatus.setStatus("current")


class _CesOverWlanUnit0Dsx1SignalMode_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1SignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("robbedBit", 2),
          ("bitOriented", 3),
          ("messageOriented", 4),
          ("other", 5))
    )


_CesOverWlanUnit0Dsx1SignalMode_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1SignalMode_Object = MibTableColumn
cesOverWlanUnit0Dsx1SignalMode = _CesOverWlanUnit0Dsx1SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 11),
    _CesOverWlanUnit0Dsx1SignalMode_Type()
)
cesOverWlanUnit0Dsx1SignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1SignalMode.setStatus("current")


class _CesOverWlanUnit0Dsx1TransmitClockSource_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1TransmitClockSource based on Integer32"""
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
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("adaptive", 4))
    )


_CesOverWlanUnit0Dsx1TransmitClockSource_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1TransmitClockSource_Object = MibTableColumn
cesOverWlanUnit0Dsx1TransmitClockSource = _CesOverWlanUnit0Dsx1TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 12),
    _CesOverWlanUnit0Dsx1TransmitClockSource_Type()
)
cesOverWlanUnit0Dsx1TransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TransmitClockSource.setStatus("current")


class _CesOverWlanUnit0Dsx1Fdl_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1Fdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CesOverWlanUnit0Dsx1Fdl_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1Fdl_Object = MibTableColumn
cesOverWlanUnit0Dsx1Fdl = _CesOverWlanUnit0Dsx1Fdl_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 13),
    _CesOverWlanUnit0Dsx1Fdl_Type()
)
cesOverWlanUnit0Dsx1Fdl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1Fdl.setStatus("current")


class _CesOverWlanUnit0Dsx1InvalidIntervals_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1InvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CesOverWlanUnit0Dsx1InvalidIntervals_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1InvalidIntervals_Object = MibTableColumn
cesOverWlanUnit0Dsx1InvalidIntervals = _CesOverWlanUnit0Dsx1InvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 14),
    _CesOverWlanUnit0Dsx1InvalidIntervals_Type()
)
cesOverWlanUnit0Dsx1InvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1InvalidIntervals.setStatus("current")


class _CesOverWlanUnit0Dsx1LineLength_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CesOverWlanUnit0Dsx1LineLength_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LineLength_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineLength = _CesOverWlanUnit0Dsx1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 15),
    _CesOverWlanUnit0Dsx1LineLength_Type()
)
cesOverWlanUnit0Dsx1LineLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineLength.setStatus("current")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineLength.setUnits("meters")
_CesOverWlanUnit0Dsx1LineStatusLastChange_Type = TimeStamp
_CesOverWlanUnit0Dsx1LineStatusLastChange_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineStatusLastChange = _CesOverWlanUnit0Dsx1LineStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 16),
    _CesOverWlanUnit0Dsx1LineStatusLastChange_Type()
)
cesOverWlanUnit0Dsx1LineStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineStatusLastChange.setStatus("current")


class _CesOverWlanUnit0Dsx1LineStatusChangeTrapEnable_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LineStatusChangeTrapEnable based on Integer32"""
    defaultValue = 2

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


_CesOverWlanUnit0Dsx1LineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LineStatusChangeTrapEnable_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineStatusChangeTrapEnable = _CesOverWlanUnit0Dsx1LineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 17),
    _CesOverWlanUnit0Dsx1LineStatusChangeTrapEnable_Type()
)
cesOverWlanUnit0Dsx1LineStatusChangeTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineStatusChangeTrapEnable.setStatus("current")


class _CesOverWlanUnit0Dsx1LoopbackStatus_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CesOverWlanUnit0Dsx1LoopbackStatus_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LoopbackStatus_Object = MibTableColumn
cesOverWlanUnit0Dsx1LoopbackStatus = _CesOverWlanUnit0Dsx1LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 18),
    _CesOverWlanUnit0Dsx1LoopbackStatus_Type()
)
cesOverWlanUnit0Dsx1LoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LoopbackStatus.setStatus("current")


class _CesOverWlanUnit0Dsx1Ds1ChannelNumber_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1Ds1ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_CesOverWlanUnit0Dsx1Ds1ChannelNumber_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1Ds1ChannelNumber_Object = MibTableColumn
cesOverWlanUnit0Dsx1Ds1ChannelNumber = _CesOverWlanUnit0Dsx1Ds1ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 19),
    _CesOverWlanUnit0Dsx1Ds1ChannelNumber_Type()
)
cesOverWlanUnit0Dsx1Ds1ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1Ds1ChannelNumber.setStatus("current")


class _CesOverWlanUnit0Dsx1Channelization_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1Channelization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledDs0", 2),
          ("enabledDs1", 3))
    )


_CesOverWlanUnit0Dsx1Channelization_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1Channelization_Object = MibTableColumn
cesOverWlanUnit0Dsx1Channelization = _CesOverWlanUnit0Dsx1Channelization_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 20),
    _CesOverWlanUnit0Dsx1Channelization_Type()
)
cesOverWlanUnit0Dsx1Channelization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1Channelization.setStatus("current")


class _CesOverWlanUnit0Dsx1LineMode_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 1),
          ("dsu", 2))
    )


_CesOverWlanUnit0Dsx1LineMode_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LineMode_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineMode = _CesOverWlanUnit0Dsx1LineMode_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 21),
    _CesOverWlanUnit0Dsx1LineMode_Type()
)
cesOverWlanUnit0Dsx1LineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineMode.setStatus("current")


class _CesOverWlanUnit0Dsx1LineBuildOut_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("neg75dB", 2),
          ("neg15dB", 3),
          ("neg225dB", 4),
          ("zerodB", 5))
    )


_CesOverWlanUnit0Dsx1LineBuildOut_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LineBuildOut_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineBuildOut = _CesOverWlanUnit0Dsx1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 22),
    _CesOverWlanUnit0Dsx1LineBuildOut_Type()
)
cesOverWlanUnit0Dsx1LineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineBuildOut.setStatus("current")


class _CesOverWlanUnit0Dsx1LineImpedance_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1LineImpedance based on Integer32"""
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
        *(("notApplicable", 1),
          ("unbalanced75ohms", 2),
          ("balanced100ohms", 3),
          ("balanced120ohms", 4))
    )


_CesOverWlanUnit0Dsx1LineImpedance_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1LineImpedance_Object = MibTableColumn
cesOverWlanUnit0Dsx1LineImpedance = _CesOverWlanUnit0Dsx1LineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 6, 1, 23),
    _CesOverWlanUnit0Dsx1LineImpedance_Type()
)
cesOverWlanUnit0Dsx1LineImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineImpedance.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentTable_Object = MibTable
cesOverWlanUnit0Dsx1CurrentTable = _CesOverWlanUnit0Dsx1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentTable.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentEntry_Object = MibTableRow
cesOverWlanUnit0Dsx1CurrentEntry = _CesOverWlanUnit0Dsx1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1)
)
cesOverWlanUnit0Dsx1CurrentEntry.setIndexNames(
    (0, "INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentIndex"),
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentEntry.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentIndex_Type = InterfaceIndex
_CesOverWlanUnit0Dsx1CurrentIndex_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentIndex = _CesOverWlanUnit0Dsx1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 1),
    _CesOverWlanUnit0Dsx1CurrentIndex_Type()
)
cesOverWlanUnit0Dsx1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentIndex.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentESs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentESs = _CesOverWlanUnit0Dsx1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 2),
    _CesOverWlanUnit0Dsx1CurrentESs_Type()
)
cesOverWlanUnit0Dsx1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentESs.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentSESs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentSESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentSESs = _CesOverWlanUnit0Dsx1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 3),
    _CesOverWlanUnit0Dsx1CurrentSESs_Type()
)
cesOverWlanUnit0Dsx1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentSESs.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentSEFSs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentSEFSs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentSEFSs = _CesOverWlanUnit0Dsx1CurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 4),
    _CesOverWlanUnit0Dsx1CurrentSEFSs_Type()
)
cesOverWlanUnit0Dsx1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentSEFSs.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentUASs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentUASs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentUASs = _CesOverWlanUnit0Dsx1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 5),
    _CesOverWlanUnit0Dsx1CurrentUASs_Type()
)
cesOverWlanUnit0Dsx1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentUASs.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentCSSs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentCSSs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentCSSs = _CesOverWlanUnit0Dsx1CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 6),
    _CesOverWlanUnit0Dsx1CurrentCSSs_Type()
)
cesOverWlanUnit0Dsx1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentCSSs.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentPCVs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentPCVs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentPCVs = _CesOverWlanUnit0Dsx1CurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 7),
    _CesOverWlanUnit0Dsx1CurrentPCVs_Type()
)
cesOverWlanUnit0Dsx1CurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentPCVs.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentLESs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentLESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentLESs = _CesOverWlanUnit0Dsx1CurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 8),
    _CesOverWlanUnit0Dsx1CurrentLESs_Type()
)
cesOverWlanUnit0Dsx1CurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentLESs.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentBESs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentBESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentBESs = _CesOverWlanUnit0Dsx1CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 9),
    _CesOverWlanUnit0Dsx1CurrentBESs_Type()
)
cesOverWlanUnit0Dsx1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentBESs.setStatus("current")
_CesOverWlanUnit0Dsx1CurrentDMs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentDMs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentDMs = _CesOverWlanUnit0Dsx1CurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 10),
    _CesOverWlanUnit0Dsx1CurrentDMs_Type()
)
cesOverWlanUnit0Dsx1CurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentDMs.setStatus("deprecated")
_CesOverWlanUnit0Dsx1CurrentLCVs_Type = PerfCurrentCount
_CesOverWlanUnit0Dsx1CurrentLCVs_Object = MibTableColumn
cesOverWlanUnit0Dsx1CurrentLCVs = _CesOverWlanUnit0Dsx1CurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 7, 1, 11),
    _CesOverWlanUnit0Dsx1CurrentLCVs_Type()
)
cesOverWlanUnit0Dsx1CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1CurrentLCVs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalTable_Object = MibTable
cesOverWlanUnit0Dsx1IntervalTable = _CesOverWlanUnit0Dsx1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalTable.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalEntry_Object = MibTableRow
cesOverWlanUnit0Dsx1IntervalEntry = _CesOverWlanUnit0Dsx1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1)
)
cesOverWlanUnit0Dsx1IntervalEntry.setIndexNames(
    (0, "INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalIndex"),
    (0, "INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalNumber"),
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalEntry.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalIndex_Type = InterfaceIndex
_CesOverWlanUnit0Dsx1IntervalIndex_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalIndex = _CesOverWlanUnit0Dsx1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 1),
    _CesOverWlanUnit0Dsx1IntervalIndex_Type()
)
cesOverWlanUnit0Dsx1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalIndex.setStatus("current")


class _CesOverWlanUnit0Dsx1IntervalNumber_Type(Integer32):
    """Custom type cesOverWlanUnit0Dsx1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CesOverWlanUnit0Dsx1IntervalNumber_Type.__name__ = "Integer32"
_CesOverWlanUnit0Dsx1IntervalNumber_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalNumber = _CesOverWlanUnit0Dsx1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 2),
    _CesOverWlanUnit0Dsx1IntervalNumber_Type()
)
cesOverWlanUnit0Dsx1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalNumber.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalESs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalESs = _CesOverWlanUnit0Dsx1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 3),
    _CesOverWlanUnit0Dsx1IntervalESs_Type()
)
cesOverWlanUnit0Dsx1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalESs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalSESs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalSESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalSESs = _CesOverWlanUnit0Dsx1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 4),
    _CesOverWlanUnit0Dsx1IntervalSESs_Type()
)
cesOverWlanUnit0Dsx1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalSESs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalSEFSs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalSEFSs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalSEFSs = _CesOverWlanUnit0Dsx1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 5),
    _CesOverWlanUnit0Dsx1IntervalSEFSs_Type()
)
cesOverWlanUnit0Dsx1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalSEFSs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalUASs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalUASs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalUASs = _CesOverWlanUnit0Dsx1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 6),
    _CesOverWlanUnit0Dsx1IntervalUASs_Type()
)
cesOverWlanUnit0Dsx1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalUASs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalCSSs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalCSSs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalCSSs = _CesOverWlanUnit0Dsx1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 7),
    _CesOverWlanUnit0Dsx1IntervalCSSs_Type()
)
cesOverWlanUnit0Dsx1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalCSSs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalPCVs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalPCVs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalPCVs = _CesOverWlanUnit0Dsx1IntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 8),
    _CesOverWlanUnit0Dsx1IntervalPCVs_Type()
)
cesOverWlanUnit0Dsx1IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalPCVs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalLESs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalLESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalLESs = _CesOverWlanUnit0Dsx1IntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 9),
    _CesOverWlanUnit0Dsx1IntervalLESs_Type()
)
cesOverWlanUnit0Dsx1IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalLESs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalBESs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalBESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalBESs = _CesOverWlanUnit0Dsx1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 10),
    _CesOverWlanUnit0Dsx1IntervalBESs_Type()
)
cesOverWlanUnit0Dsx1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalBESs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalDMs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalDMs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalDMs = _CesOverWlanUnit0Dsx1IntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 11),
    _CesOverWlanUnit0Dsx1IntervalDMs_Type()
)
cesOverWlanUnit0Dsx1IntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalDMs.setStatus("deprecated")
_CesOverWlanUnit0Dsx1IntervalLCVs_Type = PerfIntervalCount
_CesOverWlanUnit0Dsx1IntervalLCVs_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalLCVs = _CesOverWlanUnit0Dsx1IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 12),
    _CesOverWlanUnit0Dsx1IntervalLCVs_Type()
)
cesOverWlanUnit0Dsx1IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalLCVs.setStatus("current")
_CesOverWlanUnit0Dsx1IntervalValidData_Type = TruthValue
_CesOverWlanUnit0Dsx1IntervalValidData_Object = MibTableColumn
cesOverWlanUnit0Dsx1IntervalValidData = _CesOverWlanUnit0Dsx1IntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 8, 1, 13),
    _CesOverWlanUnit0Dsx1IntervalValidData_Type()
)
cesOverWlanUnit0Dsx1IntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1IntervalValidData.setStatus("current")
_CesOverWlanUnit0Dsx1TotalTable_Object = MibTable
cesOverWlanUnit0Dsx1TotalTable = _CesOverWlanUnit0Dsx1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalTable.setStatus("current")
_CesOverWlanUnit0Dsx1TotalEntry_Object = MibTableRow
cesOverWlanUnit0Dsx1TotalEntry = _CesOverWlanUnit0Dsx1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1)
)
cesOverWlanUnit0Dsx1TotalEntry.setIndexNames(
    (0, "INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalIndex"),
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalEntry.setStatus("current")
_CesOverWlanUnit0Dsx1TotalIndex_Type = InterfaceIndex
_CesOverWlanUnit0Dsx1TotalIndex_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalIndex = _CesOverWlanUnit0Dsx1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 1),
    _CesOverWlanUnit0Dsx1TotalIndex_Type()
)
cesOverWlanUnit0Dsx1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalIndex.setStatus("current")
_CesOverWlanUnit0Dsx1TotalESs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalESs = _CesOverWlanUnit0Dsx1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 2),
    _CesOverWlanUnit0Dsx1TotalESs_Type()
)
cesOverWlanUnit0Dsx1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalESs.setStatus("current")
_CesOverWlanUnit0Dsx1TotalSESs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalSESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalSESs = _CesOverWlanUnit0Dsx1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 3),
    _CesOverWlanUnit0Dsx1TotalSESs_Type()
)
cesOverWlanUnit0Dsx1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalSESs.setStatus("current")
_CesOverWlanUnit0Dsx1TotalSEFSs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalSEFSs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalSEFSs = _CesOverWlanUnit0Dsx1TotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 4),
    _CesOverWlanUnit0Dsx1TotalSEFSs_Type()
)
cesOverWlanUnit0Dsx1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalSEFSs.setStatus("current")
_CesOverWlanUnit0Dsx1TotalUASs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalUASs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalUASs = _CesOverWlanUnit0Dsx1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 5),
    _CesOverWlanUnit0Dsx1TotalUASs_Type()
)
cesOverWlanUnit0Dsx1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalUASs.setStatus("current")
_CesOverWlanUnit0Dsx1TotalCSSs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalCSSs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalCSSs = _CesOverWlanUnit0Dsx1TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 6),
    _CesOverWlanUnit0Dsx1TotalCSSs_Type()
)
cesOverWlanUnit0Dsx1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalCSSs.setStatus("current")
_CesOverWlanUnit0Dsx1TotalPCVs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalPCVs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalPCVs = _CesOverWlanUnit0Dsx1TotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 7),
    _CesOverWlanUnit0Dsx1TotalPCVs_Type()
)
cesOverWlanUnit0Dsx1TotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalPCVs.setStatus("current")
_CesOverWlanUnit0Dsx1TotalLESs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalLESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalLESs = _CesOverWlanUnit0Dsx1TotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 8),
    _CesOverWlanUnit0Dsx1TotalLESs_Type()
)
cesOverWlanUnit0Dsx1TotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalLESs.setStatus("current")
_CesOverWlanUnit0Dsx1TotalBESs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalBESs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalBESs = _CesOverWlanUnit0Dsx1TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 9),
    _CesOverWlanUnit0Dsx1TotalBESs_Type()
)
cesOverWlanUnit0Dsx1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalBESs.setStatus("current")
_CesOverWlanUnit0Dsx1TotalDMs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalDMs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalDMs = _CesOverWlanUnit0Dsx1TotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 10),
    _CesOverWlanUnit0Dsx1TotalDMs_Type()
)
cesOverWlanUnit0Dsx1TotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalDMs.setStatus("deprecated")
_CesOverWlanUnit0Dsx1TotalLCVs_Type = PerfTotalCount
_CesOverWlanUnit0Dsx1TotalLCVs_Object = MibTableColumn
cesOverWlanUnit0Dsx1TotalLCVs = _CesOverWlanUnit0Dsx1TotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 9, 1, 11),
    _CesOverWlanUnit0Dsx1TotalLCVs_Type()
)
cesOverWlanUnit0Dsx1TotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1TotalLCVs.setStatus("current")
_CesOverWlanUnit0Ds1TrapsPrefix_ObjectIdentity = ObjectIdentity
cesOverWlanUnit0Ds1TrapsPrefix = _CesOverWlanUnit0Ds1TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 15)
)
_CesOverWlanUnit0Ds1Traps_ObjectIdentity = ObjectIdentity
cesOverWlanUnit0Ds1Traps = _CesOverWlanUnit0Ds1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 15, 0)
)
_CesOverWlanUnit0MIBConformance_ObjectIdentity = ObjectIdentity
cesOverWlanUnit0MIBConformance = _CesOverWlanUnit0MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 16)
)

# Managed Objects groups

cesOverWlanUnit0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 16, 2)
)
cesOverWlanUnit0Group.setObjects(
      *(("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineIndex"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IfIndex"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TimeElapsed"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1ValidIntervals"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineType"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineCoding"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1SendCode"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CircuitIdentifier"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LoopbackConfig"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineStatus"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1SignalMode"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TransmitClockSource"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1Fdl"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1InvalidIntervals"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineLength"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineStatusLastChange"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineStatusChangeTrapEnable"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LoopbackStatus"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1Ds1ChannelNumber"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1Channelization"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineMode"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineBuildOut"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineImpedance"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentIndex"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentSESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentSEFSs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentUASs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentCSSs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentPCVs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentLESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentBESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentDMs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1CurrentLCVs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalIndex"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalNumber"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalSESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalSEFSs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalUASs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalCSSs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalPCVs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalLESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalBESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalDMs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalLCVs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1IntervalValidData"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalIndex"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalSESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalSEFSs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalUASs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalCSSs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalPCVs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalLESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalBESs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalDMs"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1TotalLCVs"))
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Group.setStatus("current")


# Notification objects

cesOverWlanUnit0Dsx1LineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 15, 0, 1)
)
cesOverWlanUnit0Dsx1LineStatusChange.setObjects(
      *(("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineStatus"),
        ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineStatusLastChange"))
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Dsx1LineStatusChange.setStatus(
        "current"
    )


# Notifications groups

cesOverWlanUnit0Notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 2, 16, 1)
)
cesOverWlanUnit0Notifications.setObjects(
    ("INFINET-EXTCES-UNIT0-DS1-MIB", "cesOverWlanUnit0Dsx1LineStatusChange")
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINET-EXTCES-UNIT0-DS1-MIB",
    **{"cesOverWlanUnit0Ds1": cesOverWlanUnit0Ds1,
       "cesOverWlanUnit0Dsx1ConfigTable": cesOverWlanUnit0Dsx1ConfigTable,
       "cesOverWlanUnit0Dsx1ConfigEntry": cesOverWlanUnit0Dsx1ConfigEntry,
       "cesOverWlanUnit0Dsx1LineIndex": cesOverWlanUnit0Dsx1LineIndex,
       "cesOverWlanUnit0Dsx1IfIndex": cesOverWlanUnit0Dsx1IfIndex,
       "cesOverWlanUnit0Dsx1TimeElapsed": cesOverWlanUnit0Dsx1TimeElapsed,
       "cesOverWlanUnit0Dsx1ValidIntervals": cesOverWlanUnit0Dsx1ValidIntervals,
       "cesOverWlanUnit0Dsx1LineType": cesOverWlanUnit0Dsx1LineType,
       "cesOverWlanUnit0Dsx1LineCoding": cesOverWlanUnit0Dsx1LineCoding,
       "cesOverWlanUnit0Dsx1SendCode": cesOverWlanUnit0Dsx1SendCode,
       "cesOverWlanUnit0Dsx1CircuitIdentifier": cesOverWlanUnit0Dsx1CircuitIdentifier,
       "cesOverWlanUnit0Dsx1LoopbackConfig": cesOverWlanUnit0Dsx1LoopbackConfig,
       "cesOverWlanUnit0Dsx1LineStatus": cesOverWlanUnit0Dsx1LineStatus,
       "cesOverWlanUnit0Dsx1SignalMode": cesOverWlanUnit0Dsx1SignalMode,
       "cesOverWlanUnit0Dsx1TransmitClockSource": cesOverWlanUnit0Dsx1TransmitClockSource,
       "cesOverWlanUnit0Dsx1Fdl": cesOverWlanUnit0Dsx1Fdl,
       "cesOverWlanUnit0Dsx1InvalidIntervals": cesOverWlanUnit0Dsx1InvalidIntervals,
       "cesOverWlanUnit0Dsx1LineLength": cesOverWlanUnit0Dsx1LineLength,
       "cesOverWlanUnit0Dsx1LineStatusLastChange": cesOverWlanUnit0Dsx1LineStatusLastChange,
       "cesOverWlanUnit0Dsx1LineStatusChangeTrapEnable": cesOverWlanUnit0Dsx1LineStatusChangeTrapEnable,
       "cesOverWlanUnit0Dsx1LoopbackStatus": cesOverWlanUnit0Dsx1LoopbackStatus,
       "cesOverWlanUnit0Dsx1Ds1ChannelNumber": cesOverWlanUnit0Dsx1Ds1ChannelNumber,
       "cesOverWlanUnit0Dsx1Channelization": cesOverWlanUnit0Dsx1Channelization,
       "cesOverWlanUnit0Dsx1LineMode": cesOverWlanUnit0Dsx1LineMode,
       "cesOverWlanUnit0Dsx1LineBuildOut": cesOverWlanUnit0Dsx1LineBuildOut,
       "cesOverWlanUnit0Dsx1LineImpedance": cesOverWlanUnit0Dsx1LineImpedance,
       "cesOverWlanUnit0Dsx1CurrentTable": cesOverWlanUnit0Dsx1CurrentTable,
       "cesOverWlanUnit0Dsx1CurrentEntry": cesOverWlanUnit0Dsx1CurrentEntry,
       "cesOverWlanUnit0Dsx1CurrentIndex": cesOverWlanUnit0Dsx1CurrentIndex,
       "cesOverWlanUnit0Dsx1CurrentESs": cesOverWlanUnit0Dsx1CurrentESs,
       "cesOverWlanUnit0Dsx1CurrentSESs": cesOverWlanUnit0Dsx1CurrentSESs,
       "cesOverWlanUnit0Dsx1CurrentSEFSs": cesOverWlanUnit0Dsx1CurrentSEFSs,
       "cesOverWlanUnit0Dsx1CurrentUASs": cesOverWlanUnit0Dsx1CurrentUASs,
       "cesOverWlanUnit0Dsx1CurrentCSSs": cesOverWlanUnit0Dsx1CurrentCSSs,
       "cesOverWlanUnit0Dsx1CurrentPCVs": cesOverWlanUnit0Dsx1CurrentPCVs,
       "cesOverWlanUnit0Dsx1CurrentLESs": cesOverWlanUnit0Dsx1CurrentLESs,
       "cesOverWlanUnit0Dsx1CurrentBESs": cesOverWlanUnit0Dsx1CurrentBESs,
       "cesOverWlanUnit0Dsx1CurrentDMs": cesOverWlanUnit0Dsx1CurrentDMs,
       "cesOverWlanUnit0Dsx1CurrentLCVs": cesOverWlanUnit0Dsx1CurrentLCVs,
       "cesOverWlanUnit0Dsx1IntervalTable": cesOverWlanUnit0Dsx1IntervalTable,
       "cesOverWlanUnit0Dsx1IntervalEntry": cesOverWlanUnit0Dsx1IntervalEntry,
       "cesOverWlanUnit0Dsx1IntervalIndex": cesOverWlanUnit0Dsx1IntervalIndex,
       "cesOverWlanUnit0Dsx1IntervalNumber": cesOverWlanUnit0Dsx1IntervalNumber,
       "cesOverWlanUnit0Dsx1IntervalESs": cesOverWlanUnit0Dsx1IntervalESs,
       "cesOverWlanUnit0Dsx1IntervalSESs": cesOverWlanUnit0Dsx1IntervalSESs,
       "cesOverWlanUnit0Dsx1IntervalSEFSs": cesOverWlanUnit0Dsx1IntervalSEFSs,
       "cesOverWlanUnit0Dsx1IntervalUASs": cesOverWlanUnit0Dsx1IntervalUASs,
       "cesOverWlanUnit0Dsx1IntervalCSSs": cesOverWlanUnit0Dsx1IntervalCSSs,
       "cesOverWlanUnit0Dsx1IntervalPCVs": cesOverWlanUnit0Dsx1IntervalPCVs,
       "cesOverWlanUnit0Dsx1IntervalLESs": cesOverWlanUnit0Dsx1IntervalLESs,
       "cesOverWlanUnit0Dsx1IntervalBESs": cesOverWlanUnit0Dsx1IntervalBESs,
       "cesOverWlanUnit0Dsx1IntervalDMs": cesOverWlanUnit0Dsx1IntervalDMs,
       "cesOverWlanUnit0Dsx1IntervalLCVs": cesOverWlanUnit0Dsx1IntervalLCVs,
       "cesOverWlanUnit0Dsx1IntervalValidData": cesOverWlanUnit0Dsx1IntervalValidData,
       "cesOverWlanUnit0Dsx1TotalTable": cesOverWlanUnit0Dsx1TotalTable,
       "cesOverWlanUnit0Dsx1TotalEntry": cesOverWlanUnit0Dsx1TotalEntry,
       "cesOverWlanUnit0Dsx1TotalIndex": cesOverWlanUnit0Dsx1TotalIndex,
       "cesOverWlanUnit0Dsx1TotalESs": cesOverWlanUnit0Dsx1TotalESs,
       "cesOverWlanUnit0Dsx1TotalSESs": cesOverWlanUnit0Dsx1TotalSESs,
       "cesOverWlanUnit0Dsx1TotalSEFSs": cesOverWlanUnit0Dsx1TotalSEFSs,
       "cesOverWlanUnit0Dsx1TotalUASs": cesOverWlanUnit0Dsx1TotalUASs,
       "cesOverWlanUnit0Dsx1TotalCSSs": cesOverWlanUnit0Dsx1TotalCSSs,
       "cesOverWlanUnit0Dsx1TotalPCVs": cesOverWlanUnit0Dsx1TotalPCVs,
       "cesOverWlanUnit0Dsx1TotalLESs": cesOverWlanUnit0Dsx1TotalLESs,
       "cesOverWlanUnit0Dsx1TotalBESs": cesOverWlanUnit0Dsx1TotalBESs,
       "cesOverWlanUnit0Dsx1TotalDMs": cesOverWlanUnit0Dsx1TotalDMs,
       "cesOverWlanUnit0Dsx1TotalLCVs": cesOverWlanUnit0Dsx1TotalLCVs,
       "cesOverWlanUnit0Ds1TrapsPrefix": cesOverWlanUnit0Ds1TrapsPrefix,
       "cesOverWlanUnit0Ds1Traps": cesOverWlanUnit0Ds1Traps,
       "cesOverWlanUnit0Dsx1LineStatusChange": cesOverWlanUnit0Dsx1LineStatusChange,
       "cesOverWlanUnit0MIBConformance": cesOverWlanUnit0MIBConformance,
       "cesOverWlanUnit0Notifications": cesOverWlanUnit0Notifications,
       "cesOverWlanUnit0Group": cesOverWlanUnit0Group}
)
