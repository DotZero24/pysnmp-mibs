# SNMP MIB module (ZXDS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXDS1-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:42 2025
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(zxPwCTDM,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxPwCTDM")


# MODULE-IDENTITY

zxDs1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxDsx1ConfigTable_Object = MibTable
zxDsx1ConfigTable = _ZxDsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zxDsx1ConfigTable.setStatus("current")
_ZxDsx1ConfigEntry_Object = MibTableRow
zxDsx1ConfigEntry = _ZxDsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1)
)
zxDsx1ConfigEntry.setIndexNames(
    (0, "ZXDS1-MIB", "zxDsx1LineIndex"),
)
if mibBuilder.loadTexts:
    zxDsx1ConfigEntry.setStatus("current")
_ZxDsx1LineIndex_Type = InterfaceIndex
_ZxDsx1LineIndex_Object = MibTableColumn
zxDsx1LineIndex = _ZxDsx1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 1),
    _ZxDsx1LineIndex_Type()
)
zxDsx1LineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDsx1LineIndex.setStatus("current")
_ZxDsx1IfIndex_Type = InterfaceIndex
_ZxDsx1IfIndex_Object = MibTableColumn
zxDsx1IfIndex = _ZxDsx1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 2),
    _ZxDsx1IfIndex_Type()
)
zxDsx1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1IfIndex.setStatus("deprecated")


class _ZxDsx1TimeElapsed_Type(Integer32):
    """Custom type zxDsx1TimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_ZxDsx1TimeElapsed_Type.__name__ = "Integer32"
_ZxDsx1TimeElapsed_Object = MibTableColumn
zxDsx1TimeElapsed = _ZxDsx1TimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 3),
    _ZxDsx1TimeElapsed_Type()
)
zxDsx1TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1TimeElapsed.setStatus("current")


class _ZxDsx1ValidIntervals_Type(Integer32):
    """Custom type zxDsx1ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZxDsx1ValidIntervals_Type.__name__ = "Integer32"
_ZxDsx1ValidIntervals_Object = MibTableColumn
zxDsx1ValidIntervals = _ZxDsx1ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 4),
    _ZxDsx1ValidIntervals_Type()
)
zxDsx1ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1ValidIntervals.setStatus("current")


class _ZxDsx1LineType_Type(Integer32):
    """Custom type zxDsx1LineType based on Integer32"""
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
              13)
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
          ("dsx1E1Q50CRC", 13))
    )


_ZxDsx1LineType_Type.__name__ = "Integer32"
_ZxDsx1LineType_Object = MibTableColumn
zxDsx1LineType = _ZxDsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 5),
    _ZxDsx1LineType_Type()
)
zxDsx1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1LineType.setStatus("current")


class _ZxDsx1LineCoding_Type(Integer32):
    """Custom type zxDsx1LineCoding based on Integer32"""
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


_ZxDsx1LineCoding_Type.__name__ = "Integer32"
_ZxDsx1LineCoding_Object = MibTableColumn
zxDsx1LineCoding = _ZxDsx1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 6),
    _ZxDsx1LineCoding_Type()
)
zxDsx1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1LineCoding.setStatus("current")


class _ZxDsx1SendCode_Type(Integer32):
    """Custom type zxDsx1SendCode based on Integer32"""
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


_ZxDsx1SendCode_Type.__name__ = "Integer32"
_ZxDsx1SendCode_Object = MibTableColumn
zxDsx1SendCode = _ZxDsx1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 7),
    _ZxDsx1SendCode_Type()
)
zxDsx1SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1SendCode.setStatus("current")


class _ZxDsx1CircuitIdentifier_Type(DisplayString):
    """Custom type zxDsx1CircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxDsx1CircuitIdentifier_Type.__name__ = "DisplayString"
_ZxDsx1CircuitIdentifier_Object = MibTableColumn
zxDsx1CircuitIdentifier = _ZxDsx1CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 8),
    _ZxDsx1CircuitIdentifier_Type()
)
zxDsx1CircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1CircuitIdentifier.setStatus("current")


class _ZxDsx1LoopbackConfig_Type(Integer32):
    """Custom type zxDsx1LoopbackConfig based on Integer32"""
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


_ZxDsx1LoopbackConfig_Type.__name__ = "Integer32"
_ZxDsx1LoopbackConfig_Object = MibTableColumn
zxDsx1LoopbackConfig = _ZxDsx1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 9),
    _ZxDsx1LoopbackConfig_Type()
)
zxDsx1LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1LoopbackConfig.setStatus("current")


class _ZxDsx1LineStatus_Type(Integer32):
    """Custom type zxDsx1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131071),
    )


_ZxDsx1LineStatus_Type.__name__ = "Integer32"
_ZxDsx1LineStatus_Object = MibTableColumn
zxDsx1LineStatus = _ZxDsx1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 10),
    _ZxDsx1LineStatus_Type()
)
zxDsx1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1LineStatus.setStatus("current")


class _ZxDsx1SignalMode_Type(Integer32):
    """Custom type zxDsx1SignalMode based on Integer32"""
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


_ZxDsx1SignalMode_Type.__name__ = "Integer32"
_ZxDsx1SignalMode_Object = MibTableColumn
zxDsx1SignalMode = _ZxDsx1SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 11),
    _ZxDsx1SignalMode_Type()
)
zxDsx1SignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1SignalMode.setStatus("current")


class _ZxDsx1TransmitClockSource_Type(Integer32):
    """Custom type zxDsx1TransmitClockSource based on Integer32"""
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
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("adaptive", 4),
          ("enhancedAdaptive", 5),
          ("defferential", 6))
    )


_ZxDsx1TransmitClockSource_Type.__name__ = "Integer32"
_ZxDsx1TransmitClockSource_Object = MibTableColumn
zxDsx1TransmitClockSource = _ZxDsx1TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 12),
    _ZxDsx1TransmitClockSource_Type()
)
zxDsx1TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1TransmitClockSource.setStatus("current")


class _ZxDsx1Fdl_Type(Integer32):
    """Custom type zxDsx1Fdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ZxDsx1Fdl_Type.__name__ = "Integer32"
_ZxDsx1Fdl_Object = MibTableColumn
zxDsx1Fdl = _ZxDsx1Fdl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 13),
    _ZxDsx1Fdl_Type()
)
zxDsx1Fdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1Fdl.setStatus("current")


class _ZxDsx1InvalidIntervals_Type(Integer32):
    """Custom type zxDsx1InvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZxDsx1InvalidIntervals_Type.__name__ = "Integer32"
_ZxDsx1InvalidIntervals_Object = MibTableColumn
zxDsx1InvalidIntervals = _ZxDsx1InvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 14),
    _ZxDsx1InvalidIntervals_Type()
)
zxDsx1InvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1InvalidIntervals.setStatus("current")


class _ZxDsx1LineLength_Type(Integer32):
    """Custom type zxDsx1LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_ZxDsx1LineLength_Type.__name__ = "Integer32"
_ZxDsx1LineLength_Object = MibTableColumn
zxDsx1LineLength = _ZxDsx1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 15),
    _ZxDsx1LineLength_Type()
)
zxDsx1LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1LineLength.setStatus("current")
if mibBuilder.loadTexts:
    zxDsx1LineLength.setUnits("meters")
_ZxDsx1LineStatusLastChange_Type = TimeStamp
_ZxDsx1LineStatusLastChange_Object = MibTableColumn
zxDsx1LineStatusLastChange = _ZxDsx1LineStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 16),
    _ZxDsx1LineStatusLastChange_Type()
)
zxDsx1LineStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1LineStatusLastChange.setStatus("current")


class _ZxDsx1LineStatusChangeTrapEnable_Type(Integer32):
    """Custom type zxDsx1LineStatusChangeTrapEnable based on Integer32"""
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


_ZxDsx1LineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_ZxDsx1LineStatusChangeTrapEnable_Object = MibTableColumn
zxDsx1LineStatusChangeTrapEnable = _ZxDsx1LineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 17),
    _ZxDsx1LineStatusChangeTrapEnable_Type()
)
zxDsx1LineStatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1LineStatusChangeTrapEnable.setStatus("current")


class _ZxDsx1LoopbackStatus_Type(Integer32):
    """Custom type zxDsx1LoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZxDsx1LoopbackStatus_Type.__name__ = "Integer32"
_ZxDsx1LoopbackStatus_Object = MibTableColumn
zxDsx1LoopbackStatus = _ZxDsx1LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 18),
    _ZxDsx1LoopbackStatus_Type()
)
zxDsx1LoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1LoopbackStatus.setStatus("current")


class _ZxDsx1Ds1ChannelNumber_Type(Integer32):
    """Custom type zxDsx1Ds1ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_ZxDsx1Ds1ChannelNumber_Type.__name__ = "Integer32"
_ZxDsx1Ds1ChannelNumber_Object = MibTableColumn
zxDsx1Ds1ChannelNumber = _ZxDsx1Ds1ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 19),
    _ZxDsx1Ds1ChannelNumber_Type()
)
zxDsx1Ds1ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1Ds1ChannelNumber.setStatus("current")


class _ZxDsx1Channelization_Type(Integer32):
    """Custom type zxDsx1Channelization based on Integer32"""
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


_ZxDsx1Channelization_Type.__name__ = "Integer32"
_ZxDsx1Channelization_Object = MibTableColumn
zxDsx1Channelization = _ZxDsx1Channelization_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 20),
    _ZxDsx1Channelization_Type()
)
zxDsx1Channelization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1Channelization.setStatus("current")


class _ZxDsx1LineMode_Type(Integer32):
    """Custom type zxDsx1LineMode based on Integer32"""
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


_ZxDsx1LineMode_Type.__name__ = "Integer32"
_ZxDsx1LineMode_Object = MibTableColumn
zxDsx1LineMode = _ZxDsx1LineMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 21),
    _ZxDsx1LineMode_Type()
)
zxDsx1LineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1LineMode.setStatus("current")


class _ZxDsx1LineBuildOut_Type(Integer32):
    """Custom type zxDsx1LineBuildOut based on Integer32"""
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


_ZxDsx1LineBuildOut_Type.__name__ = "Integer32"
_ZxDsx1LineBuildOut_Object = MibTableColumn
zxDsx1LineBuildOut = _ZxDsx1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 22),
    _ZxDsx1LineBuildOut_Type()
)
zxDsx1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1LineBuildOut.setStatus("current")


class _ZxDsx1AdminStatus_Type(Integer32):
    """Custom type zxDsx1AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_ZxDsx1AdminStatus_Type.__name__ = "Integer32"
_ZxDsx1AdminStatus_Object = MibTableColumn
zxDsx1AdminStatus = _ZxDsx1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 23),
    _ZxDsx1AdminStatus_Type()
)
zxDsx1AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1AdminStatus.setStatus("current")


class _ZxDsx1OperStatus_Type(Integer32):
    """Custom type zxDsx1OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_ZxDsx1OperStatus_Type.__name__ = "Integer32"
_ZxDsx1OperStatus_Object = MibTableColumn
zxDsx1OperStatus = _ZxDsx1OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 24),
    _ZxDsx1OperStatus_Type()
)
zxDsx1OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1OperStatus.setStatus("current")


class _ZxDsx1ClockStatus_Type(Integer32):
    """Custom type zxDsx1ClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZxDsx1ClockStatus_Type.__name__ = "Integer32"
_ZxDsx1ClockStatus_Object = MibTableColumn
zxDsx1ClockStatus = _ZxDsx1ClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 25),
    _ZxDsx1ClockStatus_Type()
)
zxDsx1ClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1ClockStatus.setStatus("current")
_ZxDsx1CfgInfoSend_Type = TruthValue
_ZxDsx1CfgInfoSend_Object = MibTableColumn
zxDsx1CfgInfoSend = _ZxDsx1CfgInfoSend_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 26),
    _ZxDsx1CfgInfoSend_Type()
)
zxDsx1CfgInfoSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1CfgInfoSend.setStatus("current")
_ZxDsx1Retiming_Type = TruthValue
_ZxDsx1Retiming_Object = MibTableColumn
zxDsx1Retiming = _ZxDsx1Retiming_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 27),
    _ZxDsx1Retiming_Type()
)
zxDsx1Retiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1Retiming.setStatus("current")
_ZxDsx1Impedance_Type = Integer32
_ZxDsx1Impedance_Object = MibTableColumn
zxDsx1Impedance = _ZxDsx1Impedance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 28),
    _ZxDsx1Impedance_Type()
)
zxDsx1Impedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1Impedance.setStatus("current")


class _ZxDsx1FrameType_Type(Integer32):
    """Custom type zxDsx1FrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unframe", 1),
          ("doubleframe", 2),
          ("multiframe", 3))
    )


_ZxDsx1FrameType_Type.__name__ = "Integer32"
_ZxDsx1FrameType_Object = MibTableColumn
zxDsx1FrameType = _ZxDsx1FrameType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 29),
    _ZxDsx1FrameType_Type()
)
zxDsx1FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1FrameType.setStatus("current")


class _ZxDsx1BER_Type(Integer32):
    """Custom type zxDsx1BER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ZxDsx1BER_Type.__name__ = "Integer32"
_ZxDsx1BER_Object = MibTableColumn
zxDsx1BER = _ZxDsx1BER_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 30),
    _ZxDsx1BER_Type()
)
zxDsx1BER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDsx1BER.setStatus("current")


class _ZxDsx1ClockStatusTrapEnable_Type(Integer32):
    """Custom type zxDsx1ClockStatusTrapEnable based on Integer32"""
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


_ZxDsx1ClockStatusTrapEnable_Type.__name__ = "Integer32"
_ZxDsx1ClockStatusTrapEnable_Object = MibTableColumn
zxDsx1ClockStatusTrapEnable = _ZxDsx1ClockStatusTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 1, 1, 1, 31),
    _ZxDsx1ClockStatusTrapEnable_Type()
)
zxDsx1ClockStatusTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDsx1ClockStatusTrapEnable.setStatus("current")
_ZxDsx1TrapObjects_ObjectIdentity = ObjectIdentity
zxDsx1TrapObjects = _ZxDsx1TrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 100)
)

# Managed Objects groups


# Notification objects

zxDsx1ClockStatusUnlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 100, 1)
)
zxDsx1ClockStatusUnlock.setObjects(
      *(("ZXDS1-MIB", "zxDsx1LineIndex"),
        ("ZXDS1-MIB", "zxDsx1ClockStatus"))
)
if mibBuilder.loadTexts:
    zxDsx1ClockStatusUnlock.setStatus(
        "current"
    )

zxDsx1ClockStatusLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 100, 2)
)
zxDsx1ClockStatusLock.setObjects(
      *(("ZXDS1-MIB", "zxDsx1LineIndex"),
        ("ZXDS1-MIB", "zxDsx1ClockStatus"))
)
if mibBuilder.loadTexts:
    zxDsx1ClockStatusLock.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXDS1-MIB",
    **{"zxDs1": zxDs1,
       "zxDsx1ConfigTable": zxDsx1ConfigTable,
       "zxDsx1ConfigEntry": zxDsx1ConfigEntry,
       "zxDsx1LineIndex": zxDsx1LineIndex,
       "zxDsx1IfIndex": zxDsx1IfIndex,
       "zxDsx1TimeElapsed": zxDsx1TimeElapsed,
       "zxDsx1ValidIntervals": zxDsx1ValidIntervals,
       "zxDsx1LineType": zxDsx1LineType,
       "zxDsx1LineCoding": zxDsx1LineCoding,
       "zxDsx1SendCode": zxDsx1SendCode,
       "zxDsx1CircuitIdentifier": zxDsx1CircuitIdentifier,
       "zxDsx1LoopbackConfig": zxDsx1LoopbackConfig,
       "zxDsx1LineStatus": zxDsx1LineStatus,
       "zxDsx1SignalMode": zxDsx1SignalMode,
       "zxDsx1TransmitClockSource": zxDsx1TransmitClockSource,
       "zxDsx1Fdl": zxDsx1Fdl,
       "zxDsx1InvalidIntervals": zxDsx1InvalidIntervals,
       "zxDsx1LineLength": zxDsx1LineLength,
       "zxDsx1LineStatusLastChange": zxDsx1LineStatusLastChange,
       "zxDsx1LineStatusChangeTrapEnable": zxDsx1LineStatusChangeTrapEnable,
       "zxDsx1LoopbackStatus": zxDsx1LoopbackStatus,
       "zxDsx1Ds1ChannelNumber": zxDsx1Ds1ChannelNumber,
       "zxDsx1Channelization": zxDsx1Channelization,
       "zxDsx1LineMode": zxDsx1LineMode,
       "zxDsx1LineBuildOut": zxDsx1LineBuildOut,
       "zxDsx1AdminStatus": zxDsx1AdminStatus,
       "zxDsx1OperStatus": zxDsx1OperStatus,
       "zxDsx1ClockStatus": zxDsx1ClockStatus,
       "zxDsx1CfgInfoSend": zxDsx1CfgInfoSend,
       "zxDsx1Retiming": zxDsx1Retiming,
       "zxDsx1Impedance": zxDsx1Impedance,
       "zxDsx1FrameType": zxDsx1FrameType,
       "zxDsx1BER": zxDsx1BER,
       "zxDsx1ClockStatusTrapEnable": zxDsx1ClockStatusTrapEnable,
       "zxDsx1TrapObjects": zxDsx1TrapObjects,
       "zxDsx1ClockStatusUnlock": zxDsx1ClockStatusUnlock,
       "zxDsx1ClockStatusLock": zxDsx1ClockStatusLock}
)
