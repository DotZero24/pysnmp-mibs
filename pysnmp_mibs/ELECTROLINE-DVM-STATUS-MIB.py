# SNMP MIB module (ELECTROLINE-DVM-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DVM-STATUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:49 2025
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

(dvmStatus,
 electrolineDVM) = mibBuilder.importSymbols(
    "ELECTROLINE-DVM-ROOT-MIB",
    "dvmStatus",
    "electrolineDVM")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class TenthdBmV(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class TenthdB(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HundredthsVolts(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_DvmNetworkAddress_Type = IpAddress
_DvmNetworkAddress_Object = MibScalar
dvmNetworkAddress = _DvmNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 1),
    _DvmNetworkAddress_Type()
)
dvmNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmNetworkAddress.setStatus("current")


class _DvmInternalTemperature_Type(Integer32):
    """Custom type dvmInternalTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 130),
    )


_DvmInternalTemperature_Type.__name__ = "Integer32"
_DvmInternalTemperature_Object = MibScalar
dvmInternalTemperature = _DvmInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 2),
    _DvmInternalTemperature_Type()
)
dvmInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmInternalTemperature.setStatus("current")
_DvmIfDownstreamChannelTable_Object = MibTable
dvmIfDownstreamChannelTable = _DvmIfDownstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    dvmIfDownstreamChannelTable.setStatus("current")
_DvmIfDownstreamChannelEntry_Object = MibTableRow
dvmIfDownstreamChannelEntry = _DvmIfDownstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1)
)
dvmIfDownstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dvmIfDownstreamChannelEntry.setStatus("current")


class _DvmIfDownChannelId_Type(Integer32):
    """Custom type dvmIfDownChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmIfDownChannelId_Type.__name__ = "Integer32"
_DvmIfDownChannelId_Object = MibTableColumn
dvmIfDownChannelId = _DvmIfDownChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1, 1),
    _DvmIfDownChannelId_Type()
)
dvmIfDownChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfDownChannelId.setStatus("current")


class _DvmIfDownChannelFrequency_Type(Integer32):
    """Custom type dvmIfDownChannelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DvmIfDownChannelFrequency_Type.__name__ = "Integer32"
_DvmIfDownChannelFrequency_Object = MibTableColumn
dvmIfDownChannelFrequency = _DvmIfDownChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1, 2),
    _DvmIfDownChannelFrequency_Type()
)
dvmIfDownChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfDownChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfDownChannelFrequency.setUnits("hertz")


class _DvmIfDownChannelWidth_Type(Integer32):
    """Custom type dvmIfDownChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_DvmIfDownChannelWidth_Type.__name__ = "Integer32"
_DvmIfDownChannelWidth_Object = MibTableColumn
dvmIfDownChannelWidth = _DvmIfDownChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1, 3),
    _DvmIfDownChannelWidth_Type()
)
dvmIfDownChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfDownChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfDownChannelWidth.setUnits("hertz")


class _DvmIfDownChannelModulation_Type(Integer32):
    """Custom type dvmIfDownChannelModulation based on Integer32"""
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
          ("other", 2),
          ("qam64", 3),
          ("qam256", 4))
    )


_DvmIfDownChannelModulation_Type.__name__ = "Integer32"
_DvmIfDownChannelModulation_Object = MibTableColumn
dvmIfDownChannelModulation = _DvmIfDownChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1, 4),
    _DvmIfDownChannelModulation_Type()
)
dvmIfDownChannelModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfDownChannelModulation.setStatus("current")


class _DvmIfDownChannelInterleave_Type(Integer32):
    """Custom type dvmIfDownChannelInterleave based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("taps8Increment16", 3),
          ("taps16Increment8", 4),
          ("taps32Increment4", 5),
          ("taps64Increment2", 6),
          ("taps128Increment1", 7),
          ("taps12increment17", 8))
    )


_DvmIfDownChannelInterleave_Type.__name__ = "Integer32"
_DvmIfDownChannelInterleave_Object = MibTableColumn
dvmIfDownChannelInterleave = _DvmIfDownChannelInterleave_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1, 5),
    _DvmIfDownChannelInterleave_Type()
)
dvmIfDownChannelInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfDownChannelInterleave.setStatus("current")
_DvmIfDownChannelPower_Type = TenthdBmV
_DvmIfDownChannelPower_Object = MibTableColumn
dvmIfDownChannelPower = _DvmIfDownChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1, 6),
    _DvmIfDownChannelPower_Type()
)
dvmIfDownChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfDownChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfDownChannelPower.setUnits("dBmV")


class _DvmIfDownChannelAnnex_Type(Integer32):
    """Custom type dvmIfDownChannelAnnex based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("annexA", 3),
          ("annexB", 4),
          ("annexC", 5))
    )


_DvmIfDownChannelAnnex_Type.__name__ = "Integer32"
_DvmIfDownChannelAnnex_Object = MibTableColumn
dvmIfDownChannelAnnex = _DvmIfDownChannelAnnex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1, 7),
    _DvmIfDownChannelAnnex_Type()
)
dvmIfDownChannelAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfDownChannelAnnex.setStatus("current")


class _DvmIfDownChannelSymbolRate_Type(Integer32):
    """Custom type dvmIfDownChannelSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DvmIfDownChannelSymbolRate_Type.__name__ = "Integer32"
_DvmIfDownChannelSymbolRate_Object = MibTableColumn
dvmIfDownChannelSymbolRate = _DvmIfDownChannelSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1, 8),
    _DvmIfDownChannelSymbolRate_Type()
)
dvmIfDownChannelSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfDownChannelSymbolRate.setStatus("current")


class _DvmIfDownChannelTunerModule_Type(Integer32):
    """Custom type dvmIfDownChannelTunerModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 6),
    )


_DvmIfDownChannelTunerModule_Type.__name__ = "Integer32"
_DvmIfDownChannelTunerModule_Object = MibTableColumn
dvmIfDownChannelTunerModule = _DvmIfDownChannelTunerModule_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 3, 1, 9),
    _DvmIfDownChannelTunerModule_Type()
)
dvmIfDownChannelTunerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfDownChannelTunerModule.setStatus("current")
_DvmIfUpstreamChannelTable_Object = MibTable
dvmIfUpstreamChannelTable = _DvmIfUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    dvmIfUpstreamChannelTable.setStatus("current")
_DvmIfUpstreamChannelEntry_Object = MibTableRow
dvmIfUpstreamChannelEntry = _DvmIfUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 4, 1)
)
dvmIfUpstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dvmIfUpstreamChannelEntry.setStatus("current")


class _DvmIfUpChannelId_Type(Integer32):
    """Custom type dvmIfUpChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmIfUpChannelId_Type.__name__ = "Integer32"
_DvmIfUpChannelId_Object = MibTableColumn
dvmIfUpChannelId = _DvmIfUpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 4, 1, 1),
    _DvmIfUpChannelId_Type()
)
dvmIfUpChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfUpChannelId.setStatus("current")


class _DvmIfUpChannelFrequency_Type(Integer32):
    """Custom type dvmIfUpChannelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DvmIfUpChannelFrequency_Type.__name__ = "Integer32"
_DvmIfUpChannelFrequency_Object = MibTableColumn
dvmIfUpChannelFrequency = _DvmIfUpChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 4, 1, 2),
    _DvmIfUpChannelFrequency_Type()
)
dvmIfUpChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfUpChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfUpChannelFrequency.setUnits("hertz")


class _DvmIfUpChannelWidth_Type(Integer32):
    """Custom type dvmIfUpChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000000),
    )


_DvmIfUpChannelWidth_Type.__name__ = "Integer32"
_DvmIfUpChannelWidth_Object = MibTableColumn
dvmIfUpChannelWidth = _DvmIfUpChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 4, 1, 3),
    _DvmIfUpChannelWidth_Type()
)
dvmIfUpChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfUpChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfUpChannelWidth.setUnits("hertz")
_DvmIfUpChannelTxPower_Type = TenthdBmV
_DvmIfUpChannelTxPower_Object = MibTableColumn
dvmIfUpChannelTxPower = _DvmIfUpChannelTxPower_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 4, 1, 4),
    _DvmIfUpChannelTxPower_Type()
)
dvmIfUpChannelTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfUpChannelTxPower.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfUpChannelTxPower.setUnits("dBmV")


class _DvmIfUpChannelSymbolRate_Type(Integer32):
    """Custom type dvmIfUpChannelSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DvmIfUpChannelSymbolRate_Type.__name__ = "Integer32"
_DvmIfUpChannelSymbolRate_Object = MibTableColumn
dvmIfUpChannelSymbolRate = _DvmIfUpChannelSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 4, 1, 5),
    _DvmIfUpChannelSymbolRate_Type()
)
dvmIfUpChannelSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfUpChannelSymbolRate.setStatus("current")
_DvmIfSignalQualityTable_Object = MibTable
dvmIfSignalQualityTable = _DvmIfSignalQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    dvmIfSignalQualityTable.setStatus("current")
_DvmIfSignalQualityEntry_Object = MibTableRow
dvmIfSignalQualityEntry = _DvmIfSignalQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 5, 1)
)
dvmIfSignalQualityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dvmIfSignalQualityEntry.setStatus("current")
_DvmIfSigQUnerroreds_Type = Counter32
_DvmIfSigQUnerroreds_Object = MibTableColumn
dvmIfSigQUnerroreds = _DvmIfSigQUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 5, 1, 1),
    _DvmIfSigQUnerroreds_Type()
)
dvmIfSigQUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfSigQUnerroreds.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfSigQUnerroreds.setUnits("codewords")
_DvmIfSigQCorrecteds_Type = Counter32
_DvmIfSigQCorrecteds_Object = MibTableColumn
dvmIfSigQCorrecteds = _DvmIfSigQCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 5, 1, 2),
    _DvmIfSigQCorrecteds_Type()
)
dvmIfSigQCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfSigQCorrecteds.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfSigQCorrecteds.setUnits("codewords")
_DvmIfSigQUncorrectables_Type = Counter32
_DvmIfSigQUncorrectables_Object = MibTableColumn
dvmIfSigQUncorrectables = _DvmIfSigQUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 5, 1, 3),
    _DvmIfSigQUncorrectables_Type()
)
dvmIfSigQUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfSigQUncorrectables.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfSigQUncorrectables.setUnits("codewords")
_DvmIfSigQSignalNoise_Type = TenthdB
_DvmIfSigQSignalNoise_Object = MibTableColumn
dvmIfSigQSignalNoise = _DvmIfSigQSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 5, 1, 4),
    _DvmIfSigQSignalNoise_Type()
)
dvmIfSigQSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfSigQSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfSigQSignalNoise.setUnits("TenthdB")


class _DvmIfSigQMicroreflections_Type(Integer32):
    """Custom type dvmIfSigQMicroreflections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmIfSigQMicroreflections_Type.__name__ = "Integer32"
_DvmIfSigQMicroreflections_Object = MibTableColumn
dvmIfSigQMicroreflections = _DvmIfSigQMicroreflections_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 5, 1, 5),
    _DvmIfSigQMicroreflections_Type()
)
dvmIfSigQMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmIfSigQMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    dvmIfSigQMicroreflections.setUnits("-dBc")
_DvmRxAttenuatorPad_Type = TenthdB
_DvmRxAttenuatorPad_Object = MibScalar
dvmRxAttenuatorPad = _DvmRxAttenuatorPad_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 6),
    _DvmRxAttenuatorPad_Type()
)
dvmRxAttenuatorPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmRxAttenuatorPad.setStatus("current")
if mibBuilder.loadTexts:
    dvmRxAttenuatorPad.setUnits("dB")
_DvmTxAttenuatorPad_Type = TenthdB
_DvmTxAttenuatorPad_Object = MibScalar
dvmTxAttenuatorPad = _DvmTxAttenuatorPad_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 7),
    _DvmTxAttenuatorPad_Type()
)
dvmTxAttenuatorPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmTxAttenuatorPad.setStatus("current")
if mibBuilder.loadTexts:
    dvmTxAttenuatorPad.setUnits("dB")


class _DvmRxEqualyzerPlugin_Type(Integer32):
    """Custom type dvmRxEqualyzerPlugin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1,
              2,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -2),
          ("noEqualyzer", -1),
          ("cableSim0ft", 0),
          ("cableSim75ft", 1),
          ("cableSim150ft", 2),
          ("equalyzer4dB", 20),
          ("equalyzer8dB", 21))
    )


_DvmRxEqualyzerPlugin_Type.__name__ = "Integer32"
_DvmRxEqualyzerPlugin_Object = MibScalar
dvmRxEqualyzerPlugin = _DvmRxEqualyzerPlugin_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 8),
    _DvmRxEqualyzerPlugin_Type()
)
dvmRxEqualyzerPlugin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmRxEqualyzerPlugin.setStatus("current")


class _DvmAcInputVoltage_Type(Integer32):
    """Custom type dvmAcInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DvmAcInputVoltage_Type.__name__ = "Integer32"
_DvmAcInputVoltage_Object = MibScalar
dvmAcInputVoltage = _DvmAcInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 9),
    _DvmAcInputVoltage_Type()
)
dvmAcInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmAcInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dvmAcInputVoltage.setUnits("1VAC")


class _DvmNumberDCPowerSupply_Type(Integer32):
    """Custom type dvmNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DvmNumberDCPowerSupply_Type.__name__ = "Integer32"
_DvmNumberDCPowerSupply_Object = MibScalar
dvmNumberDCPowerSupply = _DvmNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 10),
    _DvmNumberDCPowerSupply_Type()
)
dvmNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmNumberDCPowerSupply.setStatus("current")
_DvmDCPowerTable_Object = MibTable
dvmDCPowerTable = _DvmDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 11)
)
if mibBuilder.loadTexts:
    dvmDCPowerTable.setStatus("current")
_DvmDCPowerEntry_Object = MibTableRow
dvmDCPowerEntry = _DvmDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 11, 1)
)
dvmDCPowerEntry.setIndexNames(
    (0, "ELECTROLINE-DVM-STATUS-MIB", "dvmDCPowerIndex"),
)
if mibBuilder.loadTexts:
    dvmDCPowerEntry.setStatus("current")
_DvmDCPowerIndex_Type = Integer32
_DvmDCPowerIndex_Object = MibTableColumn
dvmDCPowerIndex = _DvmDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 11, 1, 1),
    _DvmDCPowerIndex_Type()
)
dvmDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmDCPowerIndex.setStatus("current")
_DvmDCPowerVoltage_Type = HundredthsVolts
_DvmDCPowerVoltage_Object = MibTableColumn
dvmDCPowerVoltage = _DvmDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 11, 1, 2),
    _DvmDCPowerVoltage_Type()
)
dvmDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmDCPowerVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dvmDCPowerVoltage.setUnits("0.01Vdc")
_DvmDCPowerName_Type = DisplayString
_DvmDCPowerName_Object = MibTableColumn
dvmDCPowerName = _DvmDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 11, 1, 3),
    _DvmDCPowerName_Type()
)
dvmDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmDCPowerName.setStatus("current")


class _DvmTunerHeaterStatus_Type(Integer32):
    """Custom type dvmTunerHeaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_DvmTunerHeaterStatus_Type.__name__ = "Integer32"
_DvmTunerHeaterStatus_Object = MibScalar
dvmTunerHeaterStatus = _DvmTunerHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3, 12),
    _DvmTunerHeaterStatus_Type()
)
dvmTunerHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmTunerHeaterStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DVM-STATUS-MIB",
    **{"TenthdBmV": TenthdBmV,
       "TenthdB": TenthdB,
       "HundredthsVolts": HundredthsVolts,
       "dvmNetworkAddress": dvmNetworkAddress,
       "dvmInternalTemperature": dvmInternalTemperature,
       "dvmIfDownstreamChannelTable": dvmIfDownstreamChannelTable,
       "dvmIfDownstreamChannelEntry": dvmIfDownstreamChannelEntry,
       "dvmIfDownChannelId": dvmIfDownChannelId,
       "dvmIfDownChannelFrequency": dvmIfDownChannelFrequency,
       "dvmIfDownChannelWidth": dvmIfDownChannelWidth,
       "dvmIfDownChannelModulation": dvmIfDownChannelModulation,
       "dvmIfDownChannelInterleave": dvmIfDownChannelInterleave,
       "dvmIfDownChannelPower": dvmIfDownChannelPower,
       "dvmIfDownChannelAnnex": dvmIfDownChannelAnnex,
       "dvmIfDownChannelSymbolRate": dvmIfDownChannelSymbolRate,
       "dvmIfDownChannelTunerModule": dvmIfDownChannelTunerModule,
       "dvmIfUpstreamChannelTable": dvmIfUpstreamChannelTable,
       "dvmIfUpstreamChannelEntry": dvmIfUpstreamChannelEntry,
       "dvmIfUpChannelId": dvmIfUpChannelId,
       "dvmIfUpChannelFrequency": dvmIfUpChannelFrequency,
       "dvmIfUpChannelWidth": dvmIfUpChannelWidth,
       "dvmIfUpChannelTxPower": dvmIfUpChannelTxPower,
       "dvmIfUpChannelSymbolRate": dvmIfUpChannelSymbolRate,
       "dvmIfSignalQualityTable": dvmIfSignalQualityTable,
       "dvmIfSignalQualityEntry": dvmIfSignalQualityEntry,
       "dvmIfSigQUnerroreds": dvmIfSigQUnerroreds,
       "dvmIfSigQCorrecteds": dvmIfSigQCorrecteds,
       "dvmIfSigQUncorrectables": dvmIfSigQUncorrectables,
       "dvmIfSigQSignalNoise": dvmIfSigQSignalNoise,
       "dvmIfSigQMicroreflections": dvmIfSigQMicroreflections,
       "dvmRxAttenuatorPad": dvmRxAttenuatorPad,
       "dvmTxAttenuatorPad": dvmTxAttenuatorPad,
       "dvmRxEqualyzerPlugin": dvmRxEqualyzerPlugin,
       "dvmAcInputVoltage": dvmAcInputVoltage,
       "dvmNumberDCPowerSupply": dvmNumberDCPowerSupply,
       "dvmDCPowerTable": dvmDCPowerTable,
       "dvmDCPowerEntry": dvmDCPowerEntry,
       "dvmDCPowerIndex": dvmDCPowerIndex,
       "dvmDCPowerVoltage": dvmDCPowerVoltage,
       "dvmDCPowerName": dvmDCPowerName,
       "dvmTunerHeaterStatus": dvmTunerHeaterStatus}
)
