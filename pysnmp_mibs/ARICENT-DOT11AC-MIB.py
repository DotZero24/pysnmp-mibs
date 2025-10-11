# SNMP MIB module (ARICENT-DOT11AC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-DOT11AC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:51 2025
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
 enterprises,
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
    "enterprises",
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

fs11AC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100)
)
if mibBuilder.loadTexts:
    fs11AC.setRevisions(
        ("2015-03-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDot11ACConfig_ObjectIdentity = ObjectIdentity
fsDot11ACConfig = _FsDot11ACConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1)
)
_FsDot11ACConfigTable_Object = MibTable
fsDot11ACConfigTable = _FsDot11ACConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1)
)
if mibBuilder.loadTexts:
    fsDot11ACConfigTable.setStatus("current")
_FsDot11ACConfigEntry_Object = MibTableRow
fsDot11ACConfigEntry = _FsDot11ACConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1)
)
fsDot11ACConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11ACConfigEntry.setStatus("current")


class _FsDot11ACMaxMPDULength_Type(Integer32):
    """Custom type fsDot11ACMaxMPDULength based on Integer32"""
    defaultValue = 3895

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3895,
              7991,
              11454)
        )
    )
    namedValues = NamedValues(
        *(("short", 3895),
          ("medium", 7991),
          ("long", 11454))
    )


_FsDot11ACMaxMPDULength_Type.__name__ = "Integer32"
_FsDot11ACMaxMPDULength_Object = MibTableColumn
fsDot11ACMaxMPDULength = _FsDot11ACMaxMPDULength_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 1),
    _FsDot11ACMaxMPDULength_Type()
)
fsDot11ACMaxMPDULength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACMaxMPDULength.setStatus("current")


class _FsDot11ACMaxMPDULengthConfig_Type(Integer32):
    """Custom type fsDot11ACMaxMPDULengthConfig based on Integer32"""
    defaultValue = 3895

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3895,
              7991,
              11454)
        )
    )
    namedValues = NamedValues(
        *(("short", 3895),
          ("medium", 7991),
          ("long", 11454))
    )


_FsDot11ACMaxMPDULengthConfig_Type.__name__ = "Integer32"
_FsDot11ACMaxMPDULengthConfig_Object = MibTableColumn
fsDot11ACMaxMPDULengthConfig = _FsDot11ACMaxMPDULengthConfig_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 2),
    _FsDot11ACMaxMPDULengthConfig_Type()
)
fsDot11ACMaxMPDULengthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACMaxMPDULengthConfig.setStatus("current")


class _FsDot11ACVHTMaxRxAMPDUFactor_Type(Unsigned32):
    """Custom type fsDot11ACVHTMaxRxAMPDUFactor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsDot11ACVHTMaxRxAMPDUFactor_Type.__name__ = "Unsigned32"
_FsDot11ACVHTMaxRxAMPDUFactor_Object = MibTableColumn
fsDot11ACVHTMaxRxAMPDUFactor = _FsDot11ACVHTMaxRxAMPDUFactor_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 3),
    _FsDot11ACVHTMaxRxAMPDUFactor_Type()
)
fsDot11ACVHTMaxRxAMPDUFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTMaxRxAMPDUFactor.setStatus("current")


class _FsDot11ACVHTMaxRxAMPDUFactorConfig_Type(Unsigned32):
    """Custom type fsDot11ACVHTMaxRxAMPDUFactorConfig based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsDot11ACVHTMaxRxAMPDUFactorConfig_Type.__name__ = "Unsigned32"
_FsDot11ACVHTMaxRxAMPDUFactorConfig_Object = MibTableColumn
fsDot11ACVHTMaxRxAMPDUFactorConfig = _FsDot11ACVHTMaxRxAMPDUFactorConfig_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 4),
    _FsDot11ACVHTMaxRxAMPDUFactorConfig_Type()
)
fsDot11ACVHTMaxRxAMPDUFactorConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTMaxRxAMPDUFactorConfig.setStatus("current")


class _FsDot11ACVHTControlFieldSupported_Type(TruthValue):
    """Custom type fsDot11ACVHTControlFieldSupported based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTControlFieldSupported_Type.__name__ = "TruthValue"
_FsDot11ACVHTControlFieldSupported_Object = MibTableColumn
fsDot11ACVHTControlFieldSupported = _FsDot11ACVHTControlFieldSupported_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 5),
    _FsDot11ACVHTControlFieldSupported_Type()
)
fsDot11ACVHTControlFieldSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTControlFieldSupported.setStatus("current")


class _FsDot11ACVHTTXOPPowerSaveOptionImplemented_Type(TruthValue):
    """Custom type fsDot11ACVHTTXOPPowerSaveOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTTXOPPowerSaveOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11ACVHTTXOPPowerSaveOptionImplemented_Object = MibTableColumn
fsDot11ACVHTTXOPPowerSaveOptionImplemented = _FsDot11ACVHTTXOPPowerSaveOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 6),
    _FsDot11ACVHTTXOPPowerSaveOptionImplemented_Type()
)
fsDot11ACVHTTXOPPowerSaveOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTTXOPPowerSaveOptionImplemented.setStatus("current")


class _FsDot11ACVHTRxMCSMap_Type(OctetString):
    """Custom type fsDot11ACVHTRxMCSMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsDot11ACVHTRxMCSMap_Type.__name__ = "OctetString"
_FsDot11ACVHTRxMCSMap_Object = MibTableColumn
fsDot11ACVHTRxMCSMap = _FsDot11ACVHTRxMCSMap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 7),
    _FsDot11ACVHTRxMCSMap_Type()
)
fsDot11ACVHTRxMCSMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTRxMCSMap.setStatus("current")
_FsDot11ACVHTRxHighestDataRateSupported_Type = Unsigned32
_FsDot11ACVHTRxHighestDataRateSupported_Object = MibTableColumn
fsDot11ACVHTRxHighestDataRateSupported = _FsDot11ACVHTRxHighestDataRateSupported_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 8),
    _FsDot11ACVHTRxHighestDataRateSupported_Type()
)
fsDot11ACVHTRxHighestDataRateSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTRxHighestDataRateSupported.setStatus("current")


class _FsDot11ACVHTTxMCSMap_Type(OctetString):
    """Custom type fsDot11ACVHTTxMCSMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsDot11ACVHTTxMCSMap_Type.__name__ = "OctetString"
_FsDot11ACVHTTxMCSMap_Object = MibTableColumn
fsDot11ACVHTTxMCSMap = _FsDot11ACVHTTxMCSMap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 9),
    _FsDot11ACVHTTxMCSMap_Type()
)
fsDot11ACVHTTxMCSMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTTxMCSMap.setStatus("current")


class _FsDot11ACVHTTxHighestDataRateSupported_Type(Unsigned32):
    """Custom type fsDot11ACVHTTxHighestDataRateSupported based on Unsigned32"""
    defaultValue = 0


_FsDot11ACVHTTxHighestDataRateSupported_Type.__name__ = "Unsigned32"
_FsDot11ACVHTTxHighestDataRateSupported_Object = MibTableColumn
fsDot11ACVHTTxHighestDataRateSupported = _FsDot11ACVHTTxHighestDataRateSupported_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 10),
    _FsDot11ACVHTTxHighestDataRateSupported_Type()
)
fsDot11ACVHTTxHighestDataRateSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTTxHighestDataRateSupported.setStatus("current")


class _FsDot11ACVHTOBSSScanCount_Type(Unsigned32):
    """Custom type fsDot11ACVHTOBSSScanCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_FsDot11ACVHTOBSSScanCount_Type.__name__ = "Unsigned32"
_FsDot11ACVHTOBSSScanCount_Object = MibTableColumn
fsDot11ACVHTOBSSScanCount = _FsDot11ACVHTOBSSScanCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 11),
    _FsDot11ACVHTOBSSScanCount_Type()
)
fsDot11ACVHTOBSSScanCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTOBSSScanCount.setStatus("current")


class _FsDot11ACCurrentChannelBandwidth_Type(Integer32):
    """Custom type fsDot11ACCurrentChannelBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cbw20", 0),
          ("cbw40", 1),
          ("cbw80", 2),
          ("cbw160", 3),
          ("cbw80p80", 4))
    )


_FsDot11ACCurrentChannelBandwidth_Type.__name__ = "Integer32"
_FsDot11ACCurrentChannelBandwidth_Object = MibTableColumn
fsDot11ACCurrentChannelBandwidth = _FsDot11ACCurrentChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 12),
    _FsDot11ACCurrentChannelBandwidth_Type()
)
fsDot11ACCurrentChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACCurrentChannelBandwidth.setStatus("current")


class _FsDot11ACCurrentChannelBandwidthConfig_Type(Integer32):
    """Custom type fsDot11ACCurrentChannelBandwidthConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cbw20", 0),
          ("cbw40", 1),
          ("cbw80", 2),
          ("cbw160", 3),
          ("cbw80p80", 4))
    )


_FsDot11ACCurrentChannelBandwidthConfig_Type.__name__ = "Integer32"
_FsDot11ACCurrentChannelBandwidthConfig_Object = MibTableColumn
fsDot11ACCurrentChannelBandwidthConfig = _FsDot11ACCurrentChannelBandwidthConfig_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 13),
    _FsDot11ACCurrentChannelBandwidthConfig_Type()
)
fsDot11ACCurrentChannelBandwidthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACCurrentChannelBandwidthConfig.setStatus("current")


class _FsDot11ACCurrentChannelCenterFrequencyIndex0_Type(Unsigned32):
    """Custom type fsDot11ACCurrentChannelCenterFrequencyIndex0 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FsDot11ACCurrentChannelCenterFrequencyIndex0_Type.__name__ = "Unsigned32"
_FsDot11ACCurrentChannelCenterFrequencyIndex0_Object = MibTableColumn
fsDot11ACCurrentChannelCenterFrequencyIndex0 = _FsDot11ACCurrentChannelCenterFrequencyIndex0_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 14),
    _FsDot11ACCurrentChannelCenterFrequencyIndex0_Type()
)
fsDot11ACCurrentChannelCenterFrequencyIndex0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACCurrentChannelCenterFrequencyIndex0.setStatus("current")


class _FsDot11ACCurrentChannelCenterFrequencyIndex0Config_Type(Unsigned32):
    """Custom type fsDot11ACCurrentChannelCenterFrequencyIndex0Config based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FsDot11ACCurrentChannelCenterFrequencyIndex0Config_Type.__name__ = "Unsigned32"
_FsDot11ACCurrentChannelCenterFrequencyIndex0Config_Object = MibTableColumn
fsDot11ACCurrentChannelCenterFrequencyIndex0Config = _FsDot11ACCurrentChannelCenterFrequencyIndex0Config_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 15),
    _FsDot11ACCurrentChannelCenterFrequencyIndex0Config_Type()
)
fsDot11ACCurrentChannelCenterFrequencyIndex0Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACCurrentChannelCenterFrequencyIndex0Config.setStatus("current")


class _FsDot11ACCurrentChannelCenterFrequencyIndex1_Type(Unsigned32):
    """Custom type fsDot11ACCurrentChannelCenterFrequencyIndex1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FsDot11ACCurrentChannelCenterFrequencyIndex1_Type.__name__ = "Unsigned32"
_FsDot11ACCurrentChannelCenterFrequencyIndex1_Object = MibTableColumn
fsDot11ACCurrentChannelCenterFrequencyIndex1 = _FsDot11ACCurrentChannelCenterFrequencyIndex1_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 16),
    _FsDot11ACCurrentChannelCenterFrequencyIndex1_Type()
)
fsDot11ACCurrentChannelCenterFrequencyIndex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACCurrentChannelCenterFrequencyIndex1.setStatus("current")


class _FsDot11ACVHTShortGIOptionIn80Implemented_Type(TruthValue):
    """Custom type fsDot11ACVHTShortGIOptionIn80Implemented based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTShortGIOptionIn80Implemented_Type.__name__ = "TruthValue"
_FsDot11ACVHTShortGIOptionIn80Implemented_Object = MibTableColumn
fsDot11ACVHTShortGIOptionIn80Implemented = _FsDot11ACVHTShortGIOptionIn80Implemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 17),
    _FsDot11ACVHTShortGIOptionIn80Implemented_Type()
)
fsDot11ACVHTShortGIOptionIn80Implemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTShortGIOptionIn80Implemented.setStatus("current")


class _FsDot11ACVHTShortGIOptionIn80Activated_Type(TruthValue):
    """Custom type fsDot11ACVHTShortGIOptionIn80Activated based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTShortGIOptionIn80Activated_Type.__name__ = "TruthValue"
_FsDot11ACVHTShortGIOptionIn80Activated_Object = MibTableColumn
fsDot11ACVHTShortGIOptionIn80Activated = _FsDot11ACVHTShortGIOptionIn80Activated_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 18),
    _FsDot11ACVHTShortGIOptionIn80Activated_Type()
)
fsDot11ACVHTShortGIOptionIn80Activated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTShortGIOptionIn80Activated.setStatus("current")


class _FsDot11ACVHTShortGIOptionIn160and80p80Implemented_Type(TruthValue):
    """Custom type fsDot11ACVHTShortGIOptionIn160and80p80Implemented based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTShortGIOptionIn160and80p80Implemented_Type.__name__ = "TruthValue"
_FsDot11ACVHTShortGIOptionIn160and80p80Implemented_Object = MibTableColumn
fsDot11ACVHTShortGIOptionIn160and80p80Implemented = _FsDot11ACVHTShortGIOptionIn160and80p80Implemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 19),
    _FsDot11ACVHTShortGIOptionIn160and80p80Implemented_Type()
)
fsDot11ACVHTShortGIOptionIn160and80p80Implemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTShortGIOptionIn160and80p80Implemented.setStatus("current")


class _FsDot11ACVHTShortGIOptionIn160and80p80Activated_Type(TruthValue):
    """Custom type fsDot11ACVHTShortGIOptionIn160and80p80Activated based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTShortGIOptionIn160and80p80Activated_Type.__name__ = "TruthValue"
_FsDot11ACVHTShortGIOptionIn160and80p80Activated_Object = MibTableColumn
fsDot11ACVHTShortGIOptionIn160and80p80Activated = _FsDot11ACVHTShortGIOptionIn160and80p80Activated_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 20),
    _FsDot11ACVHTShortGIOptionIn160and80p80Activated_Type()
)
fsDot11ACVHTShortGIOptionIn160and80p80Activated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTShortGIOptionIn160and80p80Activated.setStatus("current")


class _FsDot11ACVHTLDPCCodingOptionImplemented_Type(TruthValue):
    """Custom type fsDot11ACVHTLDPCCodingOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTLDPCCodingOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11ACVHTLDPCCodingOptionImplemented_Object = MibTableColumn
fsDot11ACVHTLDPCCodingOptionImplemented = _FsDot11ACVHTLDPCCodingOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 21),
    _FsDot11ACVHTLDPCCodingOptionImplemented_Type()
)
fsDot11ACVHTLDPCCodingOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTLDPCCodingOptionImplemented.setStatus("current")


class _FsDot11ACVHTLDPCCodingOptionActivated_Type(TruthValue):
    """Custom type fsDot11ACVHTLDPCCodingOptionActivated based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTLDPCCodingOptionActivated_Type.__name__ = "TruthValue"
_FsDot11ACVHTLDPCCodingOptionActivated_Object = MibTableColumn
fsDot11ACVHTLDPCCodingOptionActivated = _FsDot11ACVHTLDPCCodingOptionActivated_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 22),
    _FsDot11ACVHTLDPCCodingOptionActivated_Type()
)
fsDot11ACVHTLDPCCodingOptionActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTLDPCCodingOptionActivated.setStatus("current")


class _FsDot11ACVHTTxSTBCOptionImplemented_Type(TruthValue):
    """Custom type fsDot11ACVHTTxSTBCOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTTxSTBCOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11ACVHTTxSTBCOptionImplemented_Object = MibTableColumn
fsDot11ACVHTTxSTBCOptionImplemented = _FsDot11ACVHTTxSTBCOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 23),
    _FsDot11ACVHTTxSTBCOptionImplemented_Type()
)
fsDot11ACVHTTxSTBCOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTTxSTBCOptionImplemented.setStatus("current")


class _FsDot11ACVHTTxSTBCOptionActivated_Type(TruthValue):
    """Custom type fsDot11ACVHTTxSTBCOptionActivated based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTTxSTBCOptionActivated_Type.__name__ = "TruthValue"
_FsDot11ACVHTTxSTBCOptionActivated_Object = MibTableColumn
fsDot11ACVHTTxSTBCOptionActivated = _FsDot11ACVHTTxSTBCOptionActivated_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 24),
    _FsDot11ACVHTTxSTBCOptionActivated_Type()
)
fsDot11ACVHTTxSTBCOptionActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTTxSTBCOptionActivated.setStatus("current")


class _FsDot11ACVHTRxSTBCOptionImplemented_Type(TruthValue):
    """Custom type fsDot11ACVHTRxSTBCOptionImplemented based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTRxSTBCOptionImplemented_Type.__name__ = "TruthValue"
_FsDot11ACVHTRxSTBCOptionImplemented_Object = MibTableColumn
fsDot11ACVHTRxSTBCOptionImplemented = _FsDot11ACVHTRxSTBCOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 25),
    _FsDot11ACVHTRxSTBCOptionImplemented_Type()
)
fsDot11ACVHTRxSTBCOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTRxSTBCOptionImplemented.setStatus("current")


class _FsDot11ACVHTRxSTBCOptionActivated_Type(TruthValue):
    """Custom type fsDot11ACVHTRxSTBCOptionActivated based on TruthValue"""
    defaultValue = 2


_FsDot11ACVHTRxSTBCOptionActivated_Type.__name__ = "TruthValue"
_FsDot11ACVHTRxSTBCOptionActivated_Object = MibTableColumn
fsDot11ACVHTRxSTBCOptionActivated = _FsDot11ACVHTRxSTBCOptionActivated_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 26),
    _FsDot11ACVHTRxSTBCOptionActivated_Type()
)
fsDot11ACVHTRxSTBCOptionActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTRxSTBCOptionActivated.setStatus("current")


class _FsDot11ACVHTMUMaxUsersImplemented_Type(Unsigned32):
    """Custom type fsDot11ACVHTMUMaxUsersImplemented based on Unsigned32"""
    defaultValue = 1


_FsDot11ACVHTMUMaxUsersImplemented_Type.__name__ = "Unsigned32"
_FsDot11ACVHTMUMaxUsersImplemented_Object = MibTableColumn
fsDot11ACVHTMUMaxUsersImplemented = _FsDot11ACVHTMUMaxUsersImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 27),
    _FsDot11ACVHTMUMaxUsersImplemented_Type()
)
fsDot11ACVHTMUMaxUsersImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTMUMaxUsersImplemented.setStatus("current")


class _FsDot11ACVHTMUMaxNSTSPerUserImplemented_Type(Unsigned32):
    """Custom type fsDot11ACVHTMUMaxNSTSPerUserImplemented based on Unsigned32"""
    defaultValue = 1


_FsDot11ACVHTMUMaxNSTSPerUserImplemented_Type.__name__ = "Unsigned32"
_FsDot11ACVHTMUMaxNSTSPerUserImplemented_Object = MibTableColumn
fsDot11ACVHTMUMaxNSTSPerUserImplemented = _FsDot11ACVHTMUMaxNSTSPerUserImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 28),
    _FsDot11ACVHTMUMaxNSTSPerUserImplemented_Type()
)
fsDot11ACVHTMUMaxNSTSPerUserImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTMUMaxNSTSPerUserImplemented.setStatus("current")


class _FsDot11ACVHTMUMaxNSTSTotalImplemented_Type(Unsigned32):
    """Custom type fsDot11ACVHTMUMaxNSTSTotalImplemented based on Unsigned32"""
    defaultValue = 1


_FsDot11ACVHTMUMaxNSTSTotalImplemented_Type.__name__ = "Unsigned32"
_FsDot11ACVHTMUMaxNSTSTotalImplemented_Object = MibTableColumn
fsDot11ACVHTMUMaxNSTSTotalImplemented = _FsDot11ACVHTMUMaxNSTSTotalImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 29),
    _FsDot11ACVHTMUMaxNSTSTotalImplemented_Type()
)
fsDot11ACVHTMUMaxNSTSTotalImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTMUMaxNSTSTotalImplemented.setStatus("current")


class _FsDot11ACSuBeamFormer_Type(Integer32):
    """Custom type fsDot11ACSuBeamFormer based on Integer32"""
    defaultValue = 0


_FsDot11ACSuBeamFormer_Type.__name__ = "Integer32"
_FsDot11ACSuBeamFormer_Object = MibTableColumn
fsDot11ACSuBeamFormer = _FsDot11ACSuBeamFormer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 30),
    _FsDot11ACSuBeamFormer_Type()
)
fsDot11ACSuBeamFormer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACSuBeamFormer.setStatus("current")


class _FsDot11ACSuBeamFormee_Type(Integer32):
    """Custom type fsDot11ACSuBeamFormee based on Integer32"""
    defaultValue = 0


_FsDot11ACSuBeamFormee_Type.__name__ = "Integer32"
_FsDot11ACSuBeamFormee_Object = MibTableColumn
fsDot11ACSuBeamFormee = _FsDot11ACSuBeamFormee_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 31),
    _FsDot11ACSuBeamFormee_Type()
)
fsDot11ACSuBeamFormee.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACSuBeamFormee.setStatus("current")


class _FsDot11ACMuBeamFormer_Type(Integer32):
    """Custom type fsDot11ACMuBeamFormer based on Integer32"""
    defaultValue = 0


_FsDot11ACMuBeamFormer_Type.__name__ = "Integer32"
_FsDot11ACMuBeamFormer_Object = MibTableColumn
fsDot11ACMuBeamFormer = _FsDot11ACMuBeamFormer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 32),
    _FsDot11ACMuBeamFormer_Type()
)
fsDot11ACMuBeamFormer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACMuBeamFormer.setStatus("current")


class _FsDot11ACMuBeamFormee_Type(Integer32):
    """Custom type fsDot11ACMuBeamFormee based on Integer32"""
    defaultValue = 0


_FsDot11ACMuBeamFormee_Type.__name__ = "Integer32"
_FsDot11ACMuBeamFormee_Object = MibTableColumn
fsDot11ACMuBeamFormee = _FsDot11ACMuBeamFormee_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 33),
    _FsDot11ACMuBeamFormee_Type()
)
fsDot11ACMuBeamFormee.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACMuBeamFormee.setStatus("current")


class _FsDot11ACVHTLinkAdaption_Type(Integer32):
    """Custom type fsDot11ACVHTLinkAdaption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FsDot11ACVHTLinkAdaption_Type.__name__ = "Integer32"
_FsDot11ACVHTLinkAdaption_Object = MibTableColumn
fsDot11ACVHTLinkAdaption = _FsDot11ACVHTLinkAdaption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 34),
    _FsDot11ACVHTLinkAdaption_Type()
)
fsDot11ACVHTLinkAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTLinkAdaption.setStatus("current")


class _FsDot11ACRxAntennaPattern_Type(Integer32):
    """Custom type fsDot11ACRxAntennaPattern based on Integer32"""
    defaultValue = 1


_FsDot11ACRxAntennaPattern_Type.__name__ = "Integer32"
_FsDot11ACRxAntennaPattern_Object = MibTableColumn
fsDot11ACRxAntennaPattern = _FsDot11ACRxAntennaPattern_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 35),
    _FsDot11ACRxAntennaPattern_Type()
)
fsDot11ACRxAntennaPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACRxAntennaPattern.setStatus("current")


class _FsDot11ACTxAntennaPattern_Type(Integer32):
    """Custom type fsDot11ACTxAntennaPattern based on Integer32"""
    defaultValue = 1


_FsDot11ACTxAntennaPattern_Type.__name__ = "Integer32"
_FsDot11ACTxAntennaPattern_Object = MibTableColumn
fsDot11ACTxAntennaPattern = _FsDot11ACTxAntennaPattern_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 36),
    _FsDot11ACTxAntennaPattern_Type()
)
fsDot11ACTxAntennaPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACTxAntennaPattern.setStatus("current")


class _FsDot11ACBasicMCSMap_Type(OctetString):
    """Custom type fsDot11ACBasicMCSMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsDot11ACBasicMCSMap_Type.__name__ = "OctetString"
_FsDot11ACBasicMCSMap_Object = MibTableColumn
fsDot11ACBasicMCSMap = _FsDot11ACBasicMCSMap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 37),
    _FsDot11ACBasicMCSMap_Type()
)
fsDot11ACBasicMCSMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACBasicMCSMap.setStatus("current")


class _FsDot11ACVHTRxMCSMapConfig_Type(OctetString):
    """Custom type fsDot11ACVHTRxMCSMapConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsDot11ACVHTRxMCSMapConfig_Type.__name__ = "OctetString"
_FsDot11ACVHTRxMCSMapConfig_Object = MibTableColumn
fsDot11ACVHTRxMCSMapConfig = _FsDot11ACVHTRxMCSMapConfig_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 38),
    _FsDot11ACVHTRxMCSMapConfig_Type()
)
fsDot11ACVHTRxMCSMapConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTRxMCSMapConfig.setStatus("current")


class _FsDot11ACVHTTxMCSMapConfig_Type(OctetString):
    """Custom type fsDot11ACVHTTxMCSMapConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsDot11ACVHTTxMCSMapConfig_Type.__name__ = "OctetString"
_FsDot11ACVHTTxMCSMapConfig_Object = MibTableColumn
fsDot11ACVHTTxMCSMapConfig = _FsDot11ACVHTTxMCSMapConfig_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 39),
    _FsDot11ACVHTTxMCSMapConfig_Type()
)
fsDot11ACVHTTxMCSMapConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACVHTTxMCSMapConfig.setStatus("current")


class _FsDot11ACCurrentChannelCenterFrequencyIndex1Config_Type(Unsigned32):
    """Custom type fsDot11ACCurrentChannelCenterFrequencyIndex1Config based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FsDot11ACCurrentChannelCenterFrequencyIndex1Config_Type.__name__ = "Unsigned32"
_FsDot11ACCurrentChannelCenterFrequencyIndex1Config_Object = MibTableColumn
fsDot11ACCurrentChannelCenterFrequencyIndex1Config = _FsDot11ACCurrentChannelCenterFrequencyIndex1Config_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 40),
    _FsDot11ACCurrentChannelCenterFrequencyIndex1Config_Type()
)
fsDot11ACCurrentChannelCenterFrequencyIndex1Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ACCurrentChannelCenterFrequencyIndex1Config.setStatus("current")
_FsDot11VHTOptionImplemented_Type = TruthValue
_FsDot11VHTOptionImplemented_Object = MibTableColumn
fsDot11VHTOptionImplemented = _FsDot11VHTOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 41),
    _FsDot11VHTOptionImplemented_Type()
)
fsDot11VHTOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11VHTOptionImplemented.setStatus("current")
_FsDot11OperatingModeNotificationImplemented_Type = TruthValue
_FsDot11OperatingModeNotificationImplemented_Object = MibTableColumn
fsDot11OperatingModeNotificationImplemented = _FsDot11OperatingModeNotificationImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 42),
    _FsDot11OperatingModeNotificationImplemented_Type()
)
fsDot11OperatingModeNotificationImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11OperatingModeNotificationImplemented.setStatus("current")


class _FsDot11ExtendedChannelSwitchActivated_Type(TruthValue):
    """Custom type fsDot11ExtendedChannelSwitchActivated based on TruthValue"""
    defaultValue = 2


_FsDot11ExtendedChannelSwitchActivated_Type.__name__ = "TruthValue"
_FsDot11ExtendedChannelSwitchActivated_Object = MibTableColumn
fsDot11ExtendedChannelSwitchActivated = _FsDot11ExtendedChannelSwitchActivated_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 43),
    _FsDot11ExtendedChannelSwitchActivated_Type()
)
fsDot11ExtendedChannelSwitchActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11ExtendedChannelSwitchActivated.setStatus("current")


class _FsDot11FragmentationThreshold_Type(Unsigned32):
    """Custom type fsDot11FragmentationThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 11500),
    )


_FsDot11FragmentationThreshold_Type.__name__ = "Unsigned32"
_FsDot11FragmentationThreshold_Object = MibTableColumn
fsDot11FragmentationThreshold = _FsDot11FragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 1, 1, 1, 44),
    _FsDot11FragmentationThreshold_Type()
)
fsDot11FragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11FragmentationThreshold.setStatus("current")
_FsDot11VHTStationConfig_ObjectIdentity = ObjectIdentity
fsDot11VHTStationConfig = _FsDot11VHTStationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 2)
)
_FsDot11VHTStationConfigTable_Object = MibTable
fsDot11VHTStationConfigTable = _FsDot11VHTStationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 2, 1)
)
if mibBuilder.loadTexts:
    fsDot11VHTStationConfigTable.setStatus("current")
_FsDot11VHTStationConfigEntry_Object = MibTableRow
fsDot11VHTStationConfigEntry = _FsDot11VHTStationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 2, 1, 1)
)
fsDot11VHTStationConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11VHTStationConfigEntry.setStatus("current")


class _FsDot11VHTRxHighestDataRateConfig_Type(Unsigned32):
    """Custom type fsDot11VHTRxHighestDataRateConfig based on Unsigned32"""
    defaultValue = 0


_FsDot11VHTRxHighestDataRateConfig_Type.__name__ = "Unsigned32"
_FsDot11VHTRxHighestDataRateConfig_Object = MibTableColumn
fsDot11VHTRxHighestDataRateConfig = _FsDot11VHTRxHighestDataRateConfig_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 2, 1, 1, 1),
    _FsDot11VHTRxHighestDataRateConfig_Type()
)
fsDot11VHTRxHighestDataRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11VHTRxHighestDataRateConfig.setStatus("current")


class _FsDot11VHTTxHighestDataRateConfig_Type(Unsigned32):
    """Custom type fsDot11VHTTxHighestDataRateConfig based on Unsigned32"""
    defaultValue = 0


_FsDot11VHTTxHighestDataRateConfig_Type.__name__ = "Unsigned32"
_FsDot11VHTTxHighestDataRateConfig_Object = MibTableColumn
fsDot11VHTTxHighestDataRateConfig = _FsDot11VHTTxHighestDataRateConfig_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 2, 1, 1, 2),
    _FsDot11VHTTxHighestDataRateConfig_Type()
)
fsDot11VHTTxHighestDataRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11VHTTxHighestDataRateConfig.setStatus("current")
_FsDot11PhyVHT_ObjectIdentity = ObjectIdentity
fsDot11PhyVHT = _FsDot11PhyVHT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 3)
)
_FsDot11PhyVHTTable_Object = MibTable
fsDot11PhyVHTTable = _FsDot11PhyVHTTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 3, 1)
)
if mibBuilder.loadTexts:
    fsDot11PhyVHTTable.setStatus("current")
_FsDot11PhyVHTEntry_Object = MibTableRow
fsDot11PhyVHTEntry = _FsDot11PhyVHTEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 3, 1, 1)
)
fsDot11PhyVHTEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsDot11PhyVHTEntry.setStatus("current")


class _FsDot11NumberOfSpatialStreamsImplemented_Type(Unsigned32):
    """Custom type fsDot11NumberOfSpatialStreamsImplemented based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FsDot11NumberOfSpatialStreamsImplemented_Type.__name__ = "Unsigned32"
_FsDot11NumberOfSpatialStreamsImplemented_Object = MibTableColumn
fsDot11NumberOfSpatialStreamsImplemented = _FsDot11NumberOfSpatialStreamsImplemented_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 3, 1, 1, 1),
    _FsDot11NumberOfSpatialStreamsImplemented_Type()
)
fsDot11NumberOfSpatialStreamsImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11NumberOfSpatialStreamsImplemented.setStatus("current")


class _FsDot11NumberOfSpatialStreamsActivated_Type(Unsigned32):
    """Custom type fsDot11NumberOfSpatialStreamsActivated based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FsDot11NumberOfSpatialStreamsActivated_Type.__name__ = "Unsigned32"
_FsDot11NumberOfSpatialStreamsActivated_Object = MibTableColumn
fsDot11NumberOfSpatialStreamsActivated = _FsDot11NumberOfSpatialStreamsActivated_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 100, 3, 1, 1, 2),
    _FsDot11NumberOfSpatialStreamsActivated_Type()
)
fsDot11NumberOfSpatialStreamsActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11NumberOfSpatialStreamsActivated.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-DOT11AC-MIB",
    **{"fs11AC": fs11AC,
       "fsDot11ACConfig": fsDot11ACConfig,
       "fsDot11ACConfigTable": fsDot11ACConfigTable,
       "fsDot11ACConfigEntry": fsDot11ACConfigEntry,
       "fsDot11ACMaxMPDULength": fsDot11ACMaxMPDULength,
       "fsDot11ACMaxMPDULengthConfig": fsDot11ACMaxMPDULengthConfig,
       "fsDot11ACVHTMaxRxAMPDUFactor": fsDot11ACVHTMaxRxAMPDUFactor,
       "fsDot11ACVHTMaxRxAMPDUFactorConfig": fsDot11ACVHTMaxRxAMPDUFactorConfig,
       "fsDot11ACVHTControlFieldSupported": fsDot11ACVHTControlFieldSupported,
       "fsDot11ACVHTTXOPPowerSaveOptionImplemented": fsDot11ACVHTTXOPPowerSaveOptionImplemented,
       "fsDot11ACVHTRxMCSMap": fsDot11ACVHTRxMCSMap,
       "fsDot11ACVHTRxHighestDataRateSupported": fsDot11ACVHTRxHighestDataRateSupported,
       "fsDot11ACVHTTxMCSMap": fsDot11ACVHTTxMCSMap,
       "fsDot11ACVHTTxHighestDataRateSupported": fsDot11ACVHTTxHighestDataRateSupported,
       "fsDot11ACVHTOBSSScanCount": fsDot11ACVHTOBSSScanCount,
       "fsDot11ACCurrentChannelBandwidth": fsDot11ACCurrentChannelBandwidth,
       "fsDot11ACCurrentChannelBandwidthConfig": fsDot11ACCurrentChannelBandwidthConfig,
       "fsDot11ACCurrentChannelCenterFrequencyIndex0": fsDot11ACCurrentChannelCenterFrequencyIndex0,
       "fsDot11ACCurrentChannelCenterFrequencyIndex0Config": fsDot11ACCurrentChannelCenterFrequencyIndex0Config,
       "fsDot11ACCurrentChannelCenterFrequencyIndex1": fsDot11ACCurrentChannelCenterFrequencyIndex1,
       "fsDot11ACVHTShortGIOptionIn80Implemented": fsDot11ACVHTShortGIOptionIn80Implemented,
       "fsDot11ACVHTShortGIOptionIn80Activated": fsDot11ACVHTShortGIOptionIn80Activated,
       "fsDot11ACVHTShortGIOptionIn160and80p80Implemented": fsDot11ACVHTShortGIOptionIn160and80p80Implemented,
       "fsDot11ACVHTShortGIOptionIn160and80p80Activated": fsDot11ACVHTShortGIOptionIn160and80p80Activated,
       "fsDot11ACVHTLDPCCodingOptionImplemented": fsDot11ACVHTLDPCCodingOptionImplemented,
       "fsDot11ACVHTLDPCCodingOptionActivated": fsDot11ACVHTLDPCCodingOptionActivated,
       "fsDot11ACVHTTxSTBCOptionImplemented": fsDot11ACVHTTxSTBCOptionImplemented,
       "fsDot11ACVHTTxSTBCOptionActivated": fsDot11ACVHTTxSTBCOptionActivated,
       "fsDot11ACVHTRxSTBCOptionImplemented": fsDot11ACVHTRxSTBCOptionImplemented,
       "fsDot11ACVHTRxSTBCOptionActivated": fsDot11ACVHTRxSTBCOptionActivated,
       "fsDot11ACVHTMUMaxUsersImplemented": fsDot11ACVHTMUMaxUsersImplemented,
       "fsDot11ACVHTMUMaxNSTSPerUserImplemented": fsDot11ACVHTMUMaxNSTSPerUserImplemented,
       "fsDot11ACVHTMUMaxNSTSTotalImplemented": fsDot11ACVHTMUMaxNSTSTotalImplemented,
       "fsDot11ACSuBeamFormer": fsDot11ACSuBeamFormer,
       "fsDot11ACSuBeamFormee": fsDot11ACSuBeamFormee,
       "fsDot11ACMuBeamFormer": fsDot11ACMuBeamFormer,
       "fsDot11ACMuBeamFormee": fsDot11ACMuBeamFormee,
       "fsDot11ACVHTLinkAdaption": fsDot11ACVHTLinkAdaption,
       "fsDot11ACRxAntennaPattern": fsDot11ACRxAntennaPattern,
       "fsDot11ACTxAntennaPattern": fsDot11ACTxAntennaPattern,
       "fsDot11ACBasicMCSMap": fsDot11ACBasicMCSMap,
       "fsDot11ACVHTRxMCSMapConfig": fsDot11ACVHTRxMCSMapConfig,
       "fsDot11ACVHTTxMCSMapConfig": fsDot11ACVHTTxMCSMapConfig,
       "fsDot11ACCurrentChannelCenterFrequencyIndex1Config": fsDot11ACCurrentChannelCenterFrequencyIndex1Config,
       "fsDot11VHTOptionImplemented": fsDot11VHTOptionImplemented,
       "fsDot11OperatingModeNotificationImplemented": fsDot11OperatingModeNotificationImplemented,
       "fsDot11ExtendedChannelSwitchActivated": fsDot11ExtendedChannelSwitchActivated,
       "fsDot11FragmentationThreshold": fsDot11FragmentationThreshold,
       "fsDot11VHTStationConfig": fsDot11VHTStationConfig,
       "fsDot11VHTStationConfigTable": fsDot11VHTStationConfigTable,
       "fsDot11VHTStationConfigEntry": fsDot11VHTStationConfigEntry,
       "fsDot11VHTRxHighestDataRateConfig": fsDot11VHTRxHighestDataRateConfig,
       "fsDot11VHTTxHighestDataRateConfig": fsDot11VHTTxHighestDataRateConfig,
       "fsDot11PhyVHT": fsDot11PhyVHT,
       "fsDot11PhyVHTTable": fsDot11PhyVHTTable,
       "fsDot11PhyVHTEntry": fsDot11PhyVHTEntry,
       "fsDot11NumberOfSpatialStreamsImplemented": fsDot11NumberOfSpatialStreamsImplemented,
       "fsDot11NumberOfSpatialStreamsActivated": fsDot11NumberOfSpatialStreamsActivated}
)
