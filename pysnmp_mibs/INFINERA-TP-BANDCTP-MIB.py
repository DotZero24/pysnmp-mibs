# SNMP MIB module (INFINERA-TP-BANDCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-BANDCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:21 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatArbitraryPrecision,
 FloatTenths,
 InfnALSDisableMode,
 InfnReporting,
 InfnRxEDFAGainMode,
 InfnSlotOperatingMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatTenths",
    "InfnALSDisableMode",
    "InfnReporting",
    "InfnRxEDFAGainMode",
    "InfnSlotOperatingMode")

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

bandCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    bandCtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BandCtpTable_Object = MibTable
bandCtpTable = _BandCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    bandCtpTable.setStatus("current")
_BandCtpEntry_Object = MibTableRow
bandCtpEntry = _BandCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1)
)
bandCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bandCtpEntry.setStatus("current")


class _BandCtpMaxOCGs_Type(Integer32):
    """Custom type bandCtpMaxOCGs based on Integer32"""
    defaultValue = 0


_BandCtpMaxOCGs_Type.__name__ = "Integer32"
_BandCtpMaxOCGs_Object = MibTableColumn
bandCtpMaxOCGs = _BandCtpMaxOCGs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 1),
    _BandCtpMaxOCGs_Type()
)
bandCtpMaxOCGs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpMaxOCGs.setStatus("current")


class _BandCtpChannelPlan_Type(Integer32):
    """Custom type bandCtpChannelPlan based on Integer32"""
    defaultValue = 2

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
          ("odd", 2),
          ("even", 3),
          ("all", 4))
    )


_BandCtpChannelPlan_Type.__name__ = "Integer32"
_BandCtpChannelPlan_Object = MibTableColumn
bandCtpChannelPlan = _BandCtpChannelPlan_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 2),
    _BandCtpChannelPlan_Type()
)
bandCtpChannelPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpChannelPlan.setStatus("current")


class _BandCtpRxExpectedPowerNominal_Type(FloatTenths):
    """Custom type bandCtpRxExpectedPowerNominal based on FloatTenths"""
    defaultValue = -400

    subtypeSpec = FloatTenths.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, -10),
    )


_BandCtpRxExpectedPowerNominal_Type.__name__ = "FloatTenths"
_BandCtpRxExpectedPowerNominal_Object = MibTableColumn
bandCtpRxExpectedPowerNominal = _BandCtpRxExpectedPowerNominal_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 3),
    _BandCtpRxExpectedPowerNominal_Type()
)
bandCtpRxExpectedPowerNominal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpRxExpectedPowerNominal.setStatus("current")
if mibBuilder.loadTexts:
    bandCtpRxExpectedPowerNominal.setUnits("0.1 dBm")


class _BandCtpSpanLoss1LowThreshold_Type(FloatTenths):
    """Custom type bandCtpSpanLoss1LowThreshold based on FloatTenths"""
    defaultValue = 15


_BandCtpSpanLoss1LowThreshold_Type.__name__ = "FloatTenths"
_BandCtpSpanLoss1LowThreshold_Object = MibTableColumn
bandCtpSpanLoss1LowThreshold = _BandCtpSpanLoss1LowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 4),
    _BandCtpSpanLoss1LowThreshold_Type()
)
bandCtpSpanLoss1LowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpSpanLoss1LowThreshold.setStatus("current")


class _BandCtpSpanLoss1HighThreshold_Type(FloatTenths):
    """Custom type bandCtpSpanLoss1HighThreshold based on FloatTenths"""
    defaultValue = 15


_BandCtpSpanLoss1HighThreshold_Type.__name__ = "FloatTenths"
_BandCtpSpanLoss1HighThreshold_Object = MibTableColumn
bandCtpSpanLoss1HighThreshold = _BandCtpSpanLoss1HighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 5),
    _BandCtpSpanLoss1HighThreshold_Type()
)
bandCtpSpanLoss1HighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpSpanLoss1HighThreshold.setStatus("current")


class _BandCtpSpanLoss1ThldReporting_Type(Integer32):
    """Custom type bandCtpSpanLoss1ThldReporting based on Integer32"""
    defaultValue = 1

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


_BandCtpSpanLoss1ThldReporting_Type.__name__ = "Integer32"
_BandCtpSpanLoss1ThldReporting_Object = MibTableColumn
bandCtpSpanLoss1ThldReporting = _BandCtpSpanLoss1ThldReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 6),
    _BandCtpSpanLoss1ThldReporting_Type()
)
bandCtpSpanLoss1ThldReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpSpanLoss1ThldReporting.setStatus("current")


class _BandCtpExpectedSpanLoss_Type(FloatTenths):
    """Custom type bandCtpExpectedSpanLoss based on FloatTenths"""
    defaultValue = 25

    subtypeSpec = FloatTenths.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_BandCtpExpectedSpanLoss_Type.__name__ = "FloatTenths"
_BandCtpExpectedSpanLoss_Object = MibTableColumn
bandCtpExpectedSpanLoss = _BandCtpExpectedSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 7),
    _BandCtpExpectedSpanLoss_Type()
)
bandCtpExpectedSpanLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpExpectedSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    bandCtpExpectedSpanLoss.setUnits("0.1 db")


class _BandCtpSpanLossReporting_Type(Integer32):
    """Custom type bandCtpSpanLossReporting based on Integer32"""
    defaultValue = 1

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


_BandCtpSpanLossReporting_Type.__name__ = "Integer32"
_BandCtpSpanLossReporting_Object = MibTableColumn
bandCtpSpanLossReporting = _BandCtpSpanLossReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 8),
    _BandCtpSpanLossReporting_Type()
)
bandCtpSpanLossReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpSpanLossReporting.setStatus("current")


class _BandCtpMaxEngineeredSpanLoss_Type(FloatTenths):
    """Custom type bandCtpMaxEngineeredSpanLoss based on FloatTenths"""
    defaultValue = 50

    subtypeSpec = FloatTenths.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_BandCtpMaxEngineeredSpanLoss_Type.__name__ = "FloatTenths"
_BandCtpMaxEngineeredSpanLoss_Object = MibTableColumn
bandCtpMaxEngineeredSpanLoss = _BandCtpMaxEngineeredSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 9),
    _BandCtpMaxEngineeredSpanLoss_Type()
)
bandCtpMaxEngineeredSpanLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpMaxEngineeredSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    bandCtpMaxEngineeredSpanLoss.setUnits("0.1 db")


class _BandCtpALSAction_Type(Integer32):
    """Custom type bandCtpALSAction based on Integer32"""
    defaultValue = 2

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


_BandCtpALSAction_Type.__name__ = "Integer32"
_BandCtpALSAction_Object = MibTableColumn
bandCtpALSAction = _BandCtpALSAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 10),
    _BandCtpALSAction_Type()
)
bandCtpALSAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpALSAction.setStatus("current")


class _BandCtpALSDisableTime_Type(Integer32):
    """Custom type bandCtpALSDisableTime based on Integer32"""
    defaultValue = 15


_BandCtpALSDisableTime_Type.__name__ = "Integer32"
_BandCtpALSDisableTime_Object = MibTableColumn
bandCtpALSDisableTime = _BandCtpALSDisableTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 11),
    _BandCtpALSDisableTime_Type()
)
bandCtpALSDisableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpALSDisableTime.setStatus("current")


class _BandCtpPmHistStatsEnable_Type(Integer32):
    """Custom type bandCtpPmHistStatsEnable based on Integer32"""
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


_BandCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_BandCtpPmHistStatsEnable_Object = MibTableColumn
bandCtpPmHistStatsEnable = _BandCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 12),
    _BandCtpPmHistStatsEnable_Type()
)
bandCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpPmHistStatsEnable.setStatus("current")


class _BandCtpOprLowThreshold_Type(FloatTenths):
    """Custom type bandCtpOprLowThreshold based on FloatTenths"""
    defaultValue = 0


_BandCtpOprLowThreshold_Type.__name__ = "FloatTenths"
_BandCtpOprLowThreshold_Object = MibTableColumn
bandCtpOprLowThreshold = _BandCtpOprLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 13),
    _BandCtpOprLowThreshold_Type()
)
bandCtpOprLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpOprLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    bandCtpOprLowThreshold.setUnits("0.1 db")


class _BandCtpOprHighThreshold_Type(FloatTenths):
    """Custom type bandCtpOprHighThreshold based on FloatTenths"""
    defaultValue = 0


_BandCtpOprHighThreshold_Type.__name__ = "FloatTenths"
_BandCtpOprHighThreshold_Object = MibTableColumn
bandCtpOprHighThreshold = _BandCtpOprHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 14),
    _BandCtpOprHighThreshold_Type()
)
bandCtpOprHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpOprHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    bandCtpOprHighThreshold.setUnits("0.1 db")


class _BandCtpCBandOlosSoakTime_Type(Integer32):
    """Custom type bandCtpCBandOlosSoakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("medium", 2),
          ("long", 3))
    )


_BandCtpCBandOlosSoakTime_Type.__name__ = "Integer32"
_BandCtpCBandOlosSoakTime_Object = MibTableColumn
bandCtpCBandOlosSoakTime = _BandCtpCBandOlosSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 15),
    _BandCtpCBandOlosSoakTime_Type()
)
bandCtpCBandOlosSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpCBandOlosSoakTime.setStatus("current")
_BandCtpSpanLoss2LowThreshold_Type = FloatTenths
_BandCtpSpanLoss2LowThreshold_Object = MibTableColumn
bandCtpSpanLoss2LowThreshold = _BandCtpSpanLoss2LowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 16),
    _BandCtpSpanLoss2LowThreshold_Type()
)
bandCtpSpanLoss2LowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpSpanLoss2LowThreshold.setStatus("current")
_BandCtpSpanLoss2HighThreshold_Type = FloatTenths
_BandCtpSpanLoss2HighThreshold_Object = MibTableColumn
bandCtpSpanLoss2HighThreshold = _BandCtpSpanLoss2HighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 17),
    _BandCtpSpanLoss2HighThreshold_Type()
)
bandCtpSpanLoss2HighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpSpanLoss2HighThreshold.setStatus("current")
_BandCtpSpanLoss2ThldReporting_Type = InfnReporting
_BandCtpSpanLoss2ThldReporting_Object = MibTableColumn
bandCtpSpanLoss2ThldReporting = _BandCtpSpanLoss2ThldReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 18),
    _BandCtpSpanLoss2ThldReporting_Type()
)
bandCtpSpanLoss2ThldReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpSpanLoss2ThldReporting.setStatus("current")
_BandCtpCustomMargin_Type = FloatTenths
_BandCtpCustomMargin_Object = MibTableColumn
bandCtpCustomMargin = _BandCtpCustomMargin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 19),
    _BandCtpCustomMargin_Type()
)
bandCtpCustomMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpCustomMargin.setStatus("current")
_BandCtpALSDisableMode_Type = InfnALSDisableMode
_BandCtpALSDisableMode_Object = MibTableColumn
bandCtpALSDisableMode = _BandCtpALSDisableMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 20),
    _BandCtpALSDisableMode_Type()
)
bandCtpALSDisableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpALSDisableMode.setStatus("current")
_BandCtpSlotOperatingMode_Type = InfnSlotOperatingMode
_BandCtpSlotOperatingMode_Object = MibTableColumn
bandCtpSlotOperatingMode = _BandCtpSlotOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 21),
    _BandCtpSlotOperatingMode_Type()
)
bandCtpSlotOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpSlotOperatingMode.setStatus("current")
_BandCtpTeInterfaceList_Type = DisplayString
_BandCtpTeInterfaceList_Object = MibTableColumn
bandCtpTeInterfaceList = _BandCtpTeInterfaceList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 22),
    _BandCtpTeInterfaceList_Type()
)
bandCtpTeInterfaceList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpTeInterfaceList.setStatus("current")
_BandCtpRxEDFAGainMode_Type = InfnRxEDFAGainMode
_BandCtpRxEDFAGainMode_Object = MibTableColumn
bandCtpRxEDFAGainMode = _BandCtpRxEDFAGainMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 23),
    _BandCtpRxEDFAGainMode_Type()
)
bandCtpRxEDFAGainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpRxEDFAGainMode.setStatus("current")
_BandCtpRxEDFAGainModeValue_Type = InfnRxEDFAGainMode
_BandCtpRxEDFAGainModeValue_Object = MibTableColumn
bandCtpRxEDFAGainModeValue = _BandCtpRxEDFAGainModeValue_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 24),
    _BandCtpRxEDFAGainModeValue_Type()
)
bandCtpRxEDFAGainModeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpRxEDFAGainModeValue.setStatus("current")
_BandCtpRxEDFAGain_Type = FloatArbitraryPrecision
_BandCtpRxEDFAGain_Object = MibTableColumn
bandCtpRxEDFAGain = _BandCtpRxEDFAGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 25),
    _BandCtpRxEDFAGain_Type()
)
bandCtpRxEDFAGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpRxEDFAGain.setStatus("current")
_BandCtpRxEDFATilt_Type = FloatTenths
_BandCtpRxEDFATilt_Object = MibTableColumn
bandCtpRxEDFATilt = _BandCtpRxEDFATilt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 26),
    _BandCtpRxEDFATilt_Type()
)
bandCtpRxEDFATilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpRxEDFATilt.setStatus("current")
_BandCtpTxEDFAInputPowerOffset_Type = FloatTenths
_BandCtpTxEDFAInputPowerOffset_Object = MibTableColumn
bandCtpTxEDFAInputPowerOffset = _BandCtpTxEDFAInputPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 27),
    _BandCtpTxEDFAInputPowerOffset_Type()
)
bandCtpTxEDFAInputPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpTxEDFAInputPowerOffset.setStatus("current")
_BandCtpMuxFreqSlotAttenProfile_Type = DisplayString
_BandCtpMuxFreqSlotAttenProfile_Object = MibTableColumn
bandCtpMuxFreqSlotAttenProfile = _BandCtpMuxFreqSlotAttenProfile_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 28),
    _BandCtpMuxFreqSlotAttenProfile_Type()
)
bandCtpMuxFreqSlotAttenProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpMuxFreqSlotAttenProfile.setStatus("current")
_BandCtpDemuxFreqSlotAttenProfile_Type = DisplayString
_BandCtpDemuxFreqSlotAttenProfile_Object = MibTableColumn
bandCtpDemuxFreqSlotAttenProfile = _BandCtpDemuxFreqSlotAttenProfile_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 29),
    _BandCtpDemuxFreqSlotAttenProfile_Type()
)
bandCtpDemuxFreqSlotAttenProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpDemuxFreqSlotAttenProfile.setStatus("current")
_BandCtpTxVOA_Type = FloatTenths
_BandCtpTxVOA_Object = MibTableColumn
bandCtpTxVOA = _BandCtpTxVOA_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 30),
    _BandCtpTxVOA_Type()
)
bandCtpTxVOA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpTxVOA.setStatus("current")
_BandCtpTargetLineOutputPower_Type = FloatTenths
_BandCtpTargetLineOutputPower_Object = MibTableColumn
bandCtpTargetLineOutputPower = _BandCtpTargetLineOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 1, 1, 31),
    _BandCtpTargetLineOutputPower_Type()
)
bandCtpTargetLineOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandCtpTargetLineOutputPower.setStatus("current")
_BandCtpConformance_ObjectIdentity = ObjectIdentity
bandCtpConformance = _BandCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 3)
)
_BandCtpCompliances_ObjectIdentity = ObjectIdentity
bandCtpCompliances = _BandCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 3, 1)
)
_BandCtpGroups_ObjectIdentity = ObjectIdentity
bandCtpGroups = _BandCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 3, 2)
)

# Managed Objects groups

bandCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 3, 2, 1)
)
bandCtpGroup.setObjects(
      *(("INFINERA-TP-BANDCTP-MIB", "bandCtpMaxOCGs"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpChannelPlan"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpRxExpectedPowerNominal"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpSpanLoss1LowThreshold"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpSpanLoss1HighThreshold"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpSpanLoss1ThldReporting"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpExpectedSpanLoss"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpSpanLossReporting"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpMaxEngineeredSpanLoss"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpALSAction"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpALSDisableTime"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpPmHistStatsEnable"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpOprLowThreshold"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpOprHighThreshold"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpCBandOlosSoakTime"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpSpanLoss2LowThreshold"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpSpanLoss2HighThreshold"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpSpanLoss2ThldReporting"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpCustomMargin"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpALSDisableMode"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpSlotOperatingMode"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpTeInterfaceList"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpRxEDFAGainMode"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpRxEDFAGainModeValue"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpRxEDFAGain"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpRxEDFATilt"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpTxEDFAInputPowerOffset"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpMuxFreqSlotAttenProfile"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpDemuxFreqSlotAttenProfile"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpTxVOA"),
        ("INFINERA-TP-BANDCTP-MIB", "bandCtpTargetLineOutputPower"))
)
if mibBuilder.loadTexts:
    bandCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bandCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 2, 3, 1, 1)
)
bandCtpCompliance.setObjects(
    ("INFINERA-TP-BANDCTP-MIB", "bandCtpGroup")
)
if mibBuilder.loadTexts:
    bandCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-BANDCTP-MIB",
    **{"bandCtpMIB": bandCtpMIB,
       "bandCtpTable": bandCtpTable,
       "bandCtpEntry": bandCtpEntry,
       "bandCtpMaxOCGs": bandCtpMaxOCGs,
       "bandCtpChannelPlan": bandCtpChannelPlan,
       "bandCtpRxExpectedPowerNominal": bandCtpRxExpectedPowerNominal,
       "bandCtpSpanLoss1LowThreshold": bandCtpSpanLoss1LowThreshold,
       "bandCtpSpanLoss1HighThreshold": bandCtpSpanLoss1HighThreshold,
       "bandCtpSpanLoss1ThldReporting": bandCtpSpanLoss1ThldReporting,
       "bandCtpExpectedSpanLoss": bandCtpExpectedSpanLoss,
       "bandCtpSpanLossReporting": bandCtpSpanLossReporting,
       "bandCtpMaxEngineeredSpanLoss": bandCtpMaxEngineeredSpanLoss,
       "bandCtpALSAction": bandCtpALSAction,
       "bandCtpALSDisableTime": bandCtpALSDisableTime,
       "bandCtpPmHistStatsEnable": bandCtpPmHistStatsEnable,
       "bandCtpOprLowThreshold": bandCtpOprLowThreshold,
       "bandCtpOprHighThreshold": bandCtpOprHighThreshold,
       "bandCtpCBandOlosSoakTime": bandCtpCBandOlosSoakTime,
       "bandCtpSpanLoss2LowThreshold": bandCtpSpanLoss2LowThreshold,
       "bandCtpSpanLoss2HighThreshold": bandCtpSpanLoss2HighThreshold,
       "bandCtpSpanLoss2ThldReporting": bandCtpSpanLoss2ThldReporting,
       "bandCtpCustomMargin": bandCtpCustomMargin,
       "bandCtpALSDisableMode": bandCtpALSDisableMode,
       "bandCtpSlotOperatingMode": bandCtpSlotOperatingMode,
       "bandCtpTeInterfaceList": bandCtpTeInterfaceList,
       "bandCtpRxEDFAGainMode": bandCtpRxEDFAGainMode,
       "bandCtpRxEDFAGainModeValue": bandCtpRxEDFAGainModeValue,
       "bandCtpRxEDFAGain": bandCtpRxEDFAGain,
       "bandCtpRxEDFATilt": bandCtpRxEDFATilt,
       "bandCtpTxEDFAInputPowerOffset": bandCtpTxEDFAInputPowerOffset,
       "bandCtpMuxFreqSlotAttenProfile": bandCtpMuxFreqSlotAttenProfile,
       "bandCtpDemuxFreqSlotAttenProfile": bandCtpDemuxFreqSlotAttenProfile,
       "bandCtpTxVOA": bandCtpTxVOA,
       "bandCtpTargetLineOutputPower": bandCtpTargetLineOutputPower,
       "bandCtpConformance": bandCtpConformance,
       "bandCtpCompliances": bandCtpCompliances,
       "bandCtpCompliance": bandCtpCompliance,
       "bandCtpGroups": bandCtpGroups,
       "bandCtpGroup": bandCtpGroup}
)
