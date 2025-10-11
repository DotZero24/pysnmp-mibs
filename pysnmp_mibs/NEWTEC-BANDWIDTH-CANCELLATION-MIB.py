# SNMP MIB module (NEWTEC-BANDWIDTH-CANCELLATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-BANDWIDTH-CANCELLATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:15 2025
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

(Float32TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float32TC")

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcBandwidthCancellation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100)
)
if mibBuilder.loadTexts:
    ntcBandwidthCancellation.setRevisions(
        ("2016-02-01 11:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcBwCObjects_ObjectIdentity = ObjectIdentity
ntcBwCObjects = _NtcBwCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1)
)
if mibBuilder.loadTexts:
    ntcBwCObjects.setStatus("current")
_NtcBwCAlarm_ObjectIdentity = ObjectIdentity
ntcBwCAlarm = _NtcBwCAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 1)
)
if mibBuilder.loadTexts:
    ntcBwCAlarm.setStatus("current")
_NtcBwCAlarmNoLock_Type = NtcAlarmState
_NtcBwCAlarmNoLock_Object = MibScalar
ntcBwCAlarmNoLock = _NtcBwCAlarmNoLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 1, 1),
    _NtcBwCAlarmNoLock_Type()
)
ntcBwCAlarmNoLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCAlarmNoLock.setStatus("current")
_NtcBwCCfgTable_Object = MibTable
ntcBwCCfgTable = _NtcBwCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2)
)
if mibBuilder.loadTexts:
    ntcBwCCfgTable.setStatus("current")
_NtcBwCCfgEntry_Object = MibTableRow
ntcBwCCfgEntry = _NtcBwCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2, 1)
)
ntcBwCCfgEntry.setIndexNames(
    (0, "NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCCfgName"),
)
if mibBuilder.loadTexts:
    ntcBwCCfgEntry.setStatus("current")


class _NtcBwCCfgName_Type(DisplayString):
    """Custom type ntcBwCCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtcBwCCfgName_Type.__name__ = "DisplayString"
_NtcBwCCfgName_Object = MibTableColumn
ntcBwCCfgName = _NtcBwCCfgName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2, 1, 1),
    _NtcBwCCfgName_Type()
)
ntcBwCCfgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcBwCCfgName.setStatus("current")


class _NtcBwCCfgEnable_Type(NtcEnable):
    """Custom type ntcBwCCfgEnable based on NtcEnable"""
    defaultValue = 0


_NtcBwCCfgEnable_Type.__name__ = "NtcEnable"
_NtcBwCCfgEnable_Object = MibTableColumn
ntcBwCCfgEnable = _NtcBwCCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2, 1, 2),
    _NtcBwCCfgEnable_Type()
)
ntcBwCCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBwCCfgEnable.setStatus("current")


class _NtcBwCCfgExpRoundTripDelay_Type(Unsigned32):
    """Custom type ntcBwCCfgExpRoundTripDelay based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_NtcBwCCfgExpRoundTripDelay_Type.__name__ = "Unsigned32"
_NtcBwCCfgExpRoundTripDelay_Object = MibTableColumn
ntcBwCCfgExpRoundTripDelay = _NtcBwCCfgExpRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2, 1, 3),
    _NtcBwCCfgExpRoundTripDelay_Type()
)
ntcBwCCfgExpRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBwCCfgExpRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCCfgExpRoundTripDelay.setUnits("ms")


class _NtcBwCCfgRoundTripDelayUncert_Type(Unsigned32):
    """Custom type ntcBwCCfgRoundTripDelayUncert based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NtcBwCCfgRoundTripDelayUncert_Type.__name__ = "Unsigned32"
_NtcBwCCfgRoundTripDelayUncert_Object = MibTableColumn
ntcBwCCfgRoundTripDelayUncert = _NtcBwCCfgRoundTripDelayUncert_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2, 1, 4),
    _NtcBwCCfgRoundTripDelayUncert_Type()
)
ntcBwCCfgRoundTripDelayUncert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBwCCfgRoundTripDelayUncert.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCCfgRoundTripDelayUncert.setUnits("ms")


class _NtcBwCCfgLocalCenterFreqOffset_Type(Integer32):
    """Custom type ntcBwCCfgLocalCenterFreqOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000000, 100000000),
    )


_NtcBwCCfgLocalCenterFreqOffset_Type.__name__ = "Integer32"
_NtcBwCCfgLocalCenterFreqOffset_Object = MibTableColumn
ntcBwCCfgLocalCenterFreqOffset = _NtcBwCCfgLocalCenterFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2, 1, 5),
    _NtcBwCCfgLocalCenterFreqOffset_Type()
)
ntcBwCCfgLocalCenterFreqOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBwCCfgLocalCenterFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCCfgLocalCenterFreqOffset.setUnits("Hz")


class _NtcBwCCfgLocalCenterFreqUncert_Type(Unsigned32):
    """Custom type ntcBwCCfgLocalCenterFreqUncert based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50000, 7500000),
    )


_NtcBwCCfgLocalCenterFreqUncert_Type.__name__ = "Unsigned32"
_NtcBwCCfgLocalCenterFreqUncert_Object = MibTableColumn
ntcBwCCfgLocalCenterFreqUncert = _NtcBwCCfgLocalCenterFreqUncert_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2, 1, 6),
    _NtcBwCCfgLocalCenterFreqUncert_Type()
)
ntcBwCCfgLocalCenterFreqUncert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBwCCfgLocalCenterFreqUncert.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCCfgLocalCenterFreqUncert.setUnits("Hz")


class _NtcBwCCfgLocalSpectralInversion_Type(Integer32):
    """Custom type ntcBwCCfgLocalSpectralInversion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 0),
          ("inverted", 1),
          ("automatic", 2))
    )


_NtcBwCCfgLocalSpectralInversion_Type.__name__ = "Integer32"
_NtcBwCCfgLocalSpectralInversion_Object = MibTableColumn
ntcBwCCfgLocalSpectralInversion = _NtcBwCCfgLocalSpectralInversion_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2, 1, 7),
    _NtcBwCCfgLocalSpectralInversion_Type()
)
ntcBwCCfgLocalSpectralInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBwCCfgLocalSpectralInversion.setStatus("current")


class _NtcBwCCfgBandwidthMode_Type(Integer32):
    """Custom type ntcBwCCfgBandwidthMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("robust", 1),
          ("fine", 2))
    )


_NtcBwCCfgBandwidthMode_Type.__name__ = "Integer32"
_NtcBwCCfgBandwidthMode_Object = MibTableColumn
ntcBwCCfgBandwidthMode = _NtcBwCCfgBandwidthMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 2, 1, 8),
    _NtcBwCCfgBandwidthMode_Type()
)
ntcBwCCfgBandwidthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBwCCfgBandwidthMode.setStatus("current")
_NtcBwCMonTable_Object = MibTable
ntcBwCMonTable = _NtcBwCMonTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3)
)
if mibBuilder.loadTexts:
    ntcBwCMonTable.setStatus("current")
_NtcBwCMonEntry_Object = MibTableRow
ntcBwCMonEntry = _NtcBwCMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ntcBwCMonEntry.setStatus("current")


class _NtcBwCMonState_Type(Integer32):
    """Custom type ntcBwCMonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("searching", 1),
          ("locked", 2))
    )


_NtcBwCMonState_Type.__name__ = "Integer32"
_NtcBwCMonState_Object = MibTableColumn
ntcBwCMonState = _NtcBwCMonState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3, 1, 1),
    _NtcBwCMonState_Type()
)
ntcBwCMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCMonState.setStatus("current")
_NtcBwCMonRoundTripDelay_Type = Float32TC
_NtcBwCMonRoundTripDelay_Object = MibTableColumn
ntcBwCMonRoundTripDelay = _NtcBwCMonRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3, 1, 2),
    _NtcBwCMonRoundTripDelay_Type()
)
ntcBwCMonRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCMonRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCMonRoundTripDelay.setUnits("ms")
_NtcBwCMonLocalToTotalPowerRatio_Type = Float32TC
_NtcBwCMonLocalToTotalPowerRatio_Object = MibTableColumn
ntcBwCMonLocalToTotalPowerRatio = _NtcBwCMonLocalToTotalPowerRatio_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3, 1, 3),
    _NtcBwCMonLocalToTotalPowerRatio_Type()
)
ntcBwCMonLocalToTotalPowerRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCMonLocalToTotalPowerRatio.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCMonLocalToTotalPowerRatio.setUnits("dB")
_NtcBwCMonLocalToRemotePowerRatio_Type = Float32TC
_NtcBwCMonLocalToRemotePowerRatio_Object = MibTableColumn
ntcBwCMonLocalToRemotePowerRatio = _NtcBwCMonLocalToRemotePowerRatio_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3, 1, 4),
    _NtcBwCMonLocalToRemotePowerRatio_Type()
)
ntcBwCMonLocalToRemotePowerRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCMonLocalToRemotePowerRatio.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCMonLocalToRemotePowerRatio.setUnits("dB")
_NtcBwCMonLocalLevel_Type = Float32TC
_NtcBwCMonLocalLevel_Object = MibTableColumn
ntcBwCMonLocalLevel = _NtcBwCMonLocalLevel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3, 1, 5),
    _NtcBwCMonLocalLevel_Type()
)
ntcBwCMonLocalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCMonLocalLevel.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCMonLocalLevel.setUnits("dBm")


class _NtcBwCMonLocalSymbolRate_Type(Unsigned32):
    """Custom type ntcBwCMonLocalSymbolRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 133000000),
    )


_NtcBwCMonLocalSymbolRate_Type.__name__ = "Unsigned32"
_NtcBwCMonLocalSymbolRate_Object = MibTableColumn
ntcBwCMonLocalSymbolRate = _NtcBwCMonLocalSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3, 1, 6),
    _NtcBwCMonLocalSymbolRate_Type()
)
ntcBwCMonLocalSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCMonLocalSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCMonLocalSymbolRate.setUnits("baud")
_NtcBwCMonLocalFreqOffset_Type = Float32TC
_NtcBwCMonLocalFreqOffset_Object = MibTableColumn
ntcBwCMonLocalFreqOffset = _NtcBwCMonLocalFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3, 1, 7),
    _NtcBwCMonLocalFreqOffset_Type()
)
ntcBwCMonLocalFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCMonLocalFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    ntcBwCMonLocalFreqOffset.setUnits("Hz")


class _NtcBwCMonLocalSpectralInversion_Type(Integer32):
    """Custom type ntcBwCMonLocalSpectralInversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 0),
          ("inverted", 1),
          ("unknown", 2))
    )


_NtcBwCMonLocalSpectralInversion_Type.__name__ = "Integer32"
_NtcBwCMonLocalSpectralInversion_Object = MibTableColumn
ntcBwCMonLocalSpectralInversion = _NtcBwCMonLocalSpectralInversion_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 3, 1, 8),
    _NtcBwCMonLocalSpectralInversion_Type()
)
ntcBwCMonLocalSpectralInversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCMonLocalSpectralInversion.setStatus("current")
_NtcBwCAlarmStateTable_Object = MibTable
ntcBwCAlarmStateTable = _NtcBwCAlarmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 4)
)
if mibBuilder.loadTexts:
    ntcBwCAlarmStateTable.setStatus("current")
_NtcBwCAlarmStateEntry_Object = MibTableRow
ntcBwCAlarmStateEntry = _NtcBwCAlarmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ntcBwCAlarmStateEntry.setStatus("current")
_NtcBwCASNoLock_Type = NtcAlarmState
_NtcBwCASNoLock_Object = MibTableColumn
ntcBwCASNoLock = _NtcBwCASNoLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 1, 4, 1, 1),
    _NtcBwCASNoLock_Type()
)
ntcBwCASNoLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBwCASNoLock.setStatus("current")
_NtcBwCConformance_ObjectIdentity = ObjectIdentity
ntcBwCConformance = _NtcBwCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 2)
)
if mibBuilder.loadTexts:
    ntcBwCConformance.setStatus("current")
_NtcBwCConfCompliance_ObjectIdentity = ObjectIdentity
ntcBwCConfCompliance = _NtcBwCConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 2, 1)
)
if mibBuilder.loadTexts:
    ntcBwCConfCompliance.setStatus("current")
_NtcBwCConfGroup_ObjectIdentity = ObjectIdentity
ntcBwCConfGroup = _NtcBwCConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 2, 2)
)
if mibBuilder.loadTexts:
    ntcBwCConfGroup.setStatus("current")
ntcBwCCfgEntry.registerAugmentions(
    ("NEWTEC-BANDWIDTH-CANCELLATION-MIB",
     "ntcBwCMonEntry")
)
ntcBwCMonEntry.setIndexNames(*ntcBwCCfgEntry.getIndexNames())
ntcBwCCfgEntry.registerAugmentions(
    ("NEWTEC-BANDWIDTH-CANCELLATION-MIB",
     "ntcBwCAlarmStateEntry")
)
ntcBwCAlarmStateEntry.setIndexNames(*ntcBwCCfgEntry.getIndexNames())

# Managed Objects groups

ntcBwCConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 2, 2, 1)
)
ntcBwCConfGrpV1Standard.setObjects(
      *(("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCAlarmNoLock"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCCfgEnable"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCCfgExpRoundTripDelay"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCCfgRoundTripDelayUncert"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCCfgLocalCenterFreqOffset"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCCfgLocalCenterFreqUncert"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCCfgLocalSpectralInversion"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCCfgBandwidthMode"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCMonState"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCMonRoundTripDelay"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCMonLocalToTotalPowerRatio"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCMonLocalToRemotePowerRatio"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCMonLocalLevel"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCMonLocalSymbolRate"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCMonLocalFreqOffset"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCMonLocalSpectralInversion"),
        ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCASNoLock"))
)
if mibBuilder.loadTexts:
    ntcBwCConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcBwCConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9100, 2, 1, 1)
)
ntcBwCConfCompV1Standard.setObjects(
    ("NEWTEC-BANDWIDTH-CANCELLATION-MIB", "ntcBwCConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcBwCConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-BANDWIDTH-CANCELLATION-MIB",
    **{"ntcBandwidthCancellation": ntcBandwidthCancellation,
       "ntcBwCObjects": ntcBwCObjects,
       "ntcBwCAlarm": ntcBwCAlarm,
       "ntcBwCAlarmNoLock": ntcBwCAlarmNoLock,
       "ntcBwCCfgTable": ntcBwCCfgTable,
       "ntcBwCCfgEntry": ntcBwCCfgEntry,
       "ntcBwCCfgName": ntcBwCCfgName,
       "ntcBwCCfgEnable": ntcBwCCfgEnable,
       "ntcBwCCfgExpRoundTripDelay": ntcBwCCfgExpRoundTripDelay,
       "ntcBwCCfgRoundTripDelayUncert": ntcBwCCfgRoundTripDelayUncert,
       "ntcBwCCfgLocalCenterFreqOffset": ntcBwCCfgLocalCenterFreqOffset,
       "ntcBwCCfgLocalCenterFreqUncert": ntcBwCCfgLocalCenterFreqUncert,
       "ntcBwCCfgLocalSpectralInversion": ntcBwCCfgLocalSpectralInversion,
       "ntcBwCCfgBandwidthMode": ntcBwCCfgBandwidthMode,
       "ntcBwCMonTable": ntcBwCMonTable,
       "ntcBwCMonEntry": ntcBwCMonEntry,
       "ntcBwCMonState": ntcBwCMonState,
       "ntcBwCMonRoundTripDelay": ntcBwCMonRoundTripDelay,
       "ntcBwCMonLocalToTotalPowerRatio": ntcBwCMonLocalToTotalPowerRatio,
       "ntcBwCMonLocalToRemotePowerRatio": ntcBwCMonLocalToRemotePowerRatio,
       "ntcBwCMonLocalLevel": ntcBwCMonLocalLevel,
       "ntcBwCMonLocalSymbolRate": ntcBwCMonLocalSymbolRate,
       "ntcBwCMonLocalFreqOffset": ntcBwCMonLocalFreqOffset,
       "ntcBwCMonLocalSpectralInversion": ntcBwCMonLocalSpectralInversion,
       "ntcBwCAlarmStateTable": ntcBwCAlarmStateTable,
       "ntcBwCAlarmStateEntry": ntcBwCAlarmStateEntry,
       "ntcBwCASNoLock": ntcBwCASNoLock,
       "ntcBwCConformance": ntcBwCConformance,
       "ntcBwCConfCompliance": ntcBwCConfCompliance,
       "ntcBwCConfCompV1Standard": ntcBwCConfCompV1Standard,
       "ntcBwCConfGroup": ntcBwCConfGroup,
       "ntcBwCConfGrpV1Standard": ntcBwCConfGrpV1Standard}
)
