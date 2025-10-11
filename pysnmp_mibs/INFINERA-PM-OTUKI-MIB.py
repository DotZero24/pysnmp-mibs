# SNMP MIB module (INFINERA-PM-OTUKI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OTUKI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:05 2025
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

(FloatArbitraryPrecision,
 FloatHundredths,
 InfnSampleDuration,
 InfnServiceType,
 InfnValidityBitmap) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths",
    "InfnSampleDuration",
    "InfnServiceType",
    "InfnValidityBitmap")

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

otuKiPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27)
)
if mibBuilder.loadTexts:
    otuKiPmMIB.setRevisions(
        ("2011-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtuKiPmRealTable_Object = MibTable
otuKiPmRealTable = _OtuKiPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1)
)
if mibBuilder.loadTexts:
    otuKiPmRealTable.setStatus("current")
_OtuKiPmRealEntry_Object = MibTableRow
otuKiPmRealEntry = _OtuKiPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1)
)
otuKiPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otuKiPmRealEntry.setStatus("current")
_OtuKiPmRealNumberOfCodeWords_Type = HCPerfIntervalCount
_OtuKiPmRealNumberOfCodeWords_Object = MibTableColumn
otuKiPmRealNumberOfCodeWords = _OtuKiPmRealNumberOfCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 1),
    _OtuKiPmRealNumberOfCodeWords_Type()
)
otuKiPmRealNumberOfCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealNumberOfCodeWords.setStatus("current")
_OtuKiPmRealNumberOfUncorrectedWords_Type = HCPerfIntervalCount
_OtuKiPmRealNumberOfUncorrectedWords_Object = MibTableColumn
otuKiPmRealNumberOfUncorrectedWords = _OtuKiPmRealNumberOfUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 2),
    _OtuKiPmRealNumberOfUncorrectedWords_Type()
)
otuKiPmRealNumberOfUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealNumberOfUncorrectedWords.setStatus("current")
_OtuKiPmRealNumberOfCorrectedZeros_Type = HCPerfIntervalCount
_OtuKiPmRealNumberOfCorrectedZeros_Object = MibTableColumn
otuKiPmRealNumberOfCorrectedZeros = _OtuKiPmRealNumberOfCorrectedZeros_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 3),
    _OtuKiPmRealNumberOfCorrectedZeros_Type()
)
otuKiPmRealNumberOfCorrectedZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealNumberOfCorrectedZeros.setStatus("current")
_OtuKiPmRealNumberOfCorrectedOnes_Type = HCPerfIntervalCount
_OtuKiPmRealNumberOfCorrectedOnes_Object = MibTableColumn
otuKiPmRealNumberOfCorrectedOnes = _OtuKiPmRealNumberOfCorrectedOnes_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 4),
    _OtuKiPmRealNumberOfCorrectedOnes_Type()
)
otuKiPmRealNumberOfCorrectedOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealNumberOfCorrectedOnes.setStatus("current")
_OtuKiPmRealRxErroredBlocks_Type = HCPerfIntervalCount
_OtuKiPmRealRxErroredBlocks_Object = MibTableColumn
otuKiPmRealRxErroredBlocks = _OtuKiPmRealRxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 5),
    _OtuKiPmRealRxErroredBlocks_Type()
)
otuKiPmRealRxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealRxErroredBlocks.setStatus("current")
_OtuKiPmRealRxDefectSeconds_Type = Integer32
_OtuKiPmRealRxDefectSeconds_Object = MibTableColumn
otuKiPmRealRxDefectSeconds = _OtuKiPmRealRxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 6),
    _OtuKiPmRealRxDefectSeconds_Type()
)
otuKiPmRealRxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealRxDefectSeconds.setStatus("current")
_OtuKiPmRealQValue_Type = FloatHundredths
_OtuKiPmRealQValue_Object = MibTableColumn
otuKiPmRealQValue = _OtuKiPmRealQValue_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 7),
    _OtuKiPmRealQValue_Type()
)
otuKiPmRealQValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealQValue.setStatus("current")
_OtuKiPmRealBerPreFec_Type = FloatArbitraryPrecision
_OtuKiPmRealBerPreFec_Object = MibTableColumn
otuKiPmRealBerPreFec = _OtuKiPmRealBerPreFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 8),
    _OtuKiPmRealBerPreFec_Type()
)
otuKiPmRealBerPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealBerPreFec.setStatus("current")
_OtuKiPmRealBerPostFec_Type = FloatArbitraryPrecision
_OtuKiPmRealBerPostFec_Object = MibTableColumn
otuKiPmRealBerPostFec = _OtuKiPmRealBerPostFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 9),
    _OtuKiPmRealBerPostFec_Type()
)
otuKiPmRealBerPostFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealBerPostFec.setStatus("current")
_OtuKiPmRealRxDefectSecondsFEND_Type = Integer32
_OtuKiPmRealRxDefectSecondsFEND_Object = MibTableColumn
otuKiPmRealRxDefectSecondsFEND = _OtuKiPmRealRxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 10),
    _OtuKiPmRealRxDefectSecondsFEND_Type()
)
otuKiPmRealRxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealRxDefectSecondsFEND.setStatus("current")
_OtuKiPmRealCorrectedBits_Type = HCPerfIntervalCount
_OtuKiPmRealCorrectedBits_Object = MibTableColumn
otuKiPmRealCorrectedBits = _OtuKiPmRealCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 11),
    _OtuKiPmRealCorrectedBits_Type()
)
otuKiPmRealCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealCorrectedBits.setStatus("current")
_OtuKiPmRealRxBEICount_Type = HCPerfIntervalCount
_OtuKiPmRealRxBEICount_Object = MibTableColumn
otuKiPmRealRxBEICount = _OtuKiPmRealRxBEICount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 1, 1, 12),
    _OtuKiPmRealRxBEICount_Type()
)
otuKiPmRealRxBEICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRealRxBEICount.setStatus("current")
_OtuKiPmTable_Object = MibTable
otuKiPmTable = _OtuKiPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2)
)
if mibBuilder.loadTexts:
    otuKiPmTable.setStatus("current")
_OtuKiPmEntry_Object = MibTableRow
otuKiPmEntry = _OtuKiPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1)
)
otuKiPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-OTUKI-MIB", "otuKiPmSampleDuration"),
    (0, "INFINERA-PM-OTUKI-MIB", "otuKiPmTimestamp"),
)
if mibBuilder.loadTexts:
    otuKiPmEntry.setStatus("current")


class _OtuKiPmTimestamp_Type(Integer32):
    """Custom type otuKiPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OtuKiPmTimestamp_Type.__name__ = "Integer32"
_OtuKiPmTimestamp_Object = MibTableColumn
otuKiPmTimestamp = _OtuKiPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 1),
    _OtuKiPmTimestamp_Type()
)
otuKiPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    otuKiPmTimestamp.setStatus("current")
_OtuKiPmSampleDuration_Type = InfnSampleDuration
_OtuKiPmSampleDuration_Object = MibTableColumn
otuKiPmSampleDuration = _OtuKiPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 2),
    _OtuKiPmSampleDuration_Type()
)
otuKiPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    otuKiPmSampleDuration.setStatus("current")
_OtuKiPmValidity_Type = InfnValidityBitmap
_OtuKiPmValidity_Object = MibTableColumn
otuKiPmValidity = _OtuKiPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 3),
    _OtuKiPmValidity_Type()
)
otuKiPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmValidity.setStatus("current")
_OtuKiPmNumberOfCodeWords_Type = HCPerfIntervalCount
_OtuKiPmNumberOfCodeWords_Object = MibTableColumn
otuKiPmNumberOfCodeWords = _OtuKiPmNumberOfCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 4),
    _OtuKiPmNumberOfCodeWords_Type()
)
otuKiPmNumberOfCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmNumberOfCodeWords.setStatus("current")
_OtuKiPmNumberOfUncorrectedWords_Type = HCPerfIntervalCount
_OtuKiPmNumberOfUncorrectedWords_Object = MibTableColumn
otuKiPmNumberOfUncorrectedWords = _OtuKiPmNumberOfUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 5),
    _OtuKiPmNumberOfUncorrectedWords_Type()
)
otuKiPmNumberOfUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmNumberOfUncorrectedWords.setStatus("current")
_OtuKiPmNumberOfCorrectedZeros_Type = HCPerfIntervalCount
_OtuKiPmNumberOfCorrectedZeros_Object = MibTableColumn
otuKiPmNumberOfCorrectedZeros = _OtuKiPmNumberOfCorrectedZeros_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 6),
    _OtuKiPmNumberOfCorrectedZeros_Type()
)
otuKiPmNumberOfCorrectedZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmNumberOfCorrectedZeros.setStatus("current")
_OtuKiPmNumberOfCorrectedOnes_Type = HCPerfIntervalCount
_OtuKiPmNumberOfCorrectedOnes_Object = MibTableColumn
otuKiPmNumberOfCorrectedOnes = _OtuKiPmNumberOfCorrectedOnes_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 7),
    _OtuKiPmNumberOfCorrectedOnes_Type()
)
otuKiPmNumberOfCorrectedOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmNumberOfCorrectedOnes.setStatus("current")
_OtuKiPmRxErroredBlocks_Type = HCPerfIntervalCount
_OtuKiPmRxErroredBlocks_Object = MibTableColumn
otuKiPmRxErroredBlocks = _OtuKiPmRxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 8),
    _OtuKiPmRxErroredBlocks_Type()
)
otuKiPmRxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRxErroredBlocks.setStatus("current")
_OtuKiPmRxDefectSeconds_Type = Integer32
_OtuKiPmRxDefectSeconds_Object = MibTableColumn
otuKiPmRxDefectSeconds = _OtuKiPmRxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 9),
    _OtuKiPmRxDefectSeconds_Type()
)
otuKiPmRxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRxDefectSeconds.setStatus("current")
_OtuKiPmCircuitId_Type = DisplayString
_OtuKiPmCircuitId_Object = MibTableColumn
otuKiPmCircuitId = _OtuKiPmCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 10),
    _OtuKiPmCircuitId_Type()
)
otuKiPmCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmCircuitId.setStatus("current")
_OtuKiPmPayloadType_Type = InfnServiceType
_OtuKiPmPayloadType_Object = MibTableColumn
otuKiPmPayloadType = _OtuKiPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 11),
    _OtuKiPmPayloadType_Type()
)
otuKiPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmPayloadType.setStatus("current")
_OtuKiPmQValueMin_Type = FloatHundredths
_OtuKiPmQValueMin_Object = MibTableColumn
otuKiPmQValueMin = _OtuKiPmQValueMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 12),
    _OtuKiPmQValueMin_Type()
)
otuKiPmQValueMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmQValueMin.setStatus("current")
_OtuKiPmQValueMax_Type = FloatHundredths
_OtuKiPmQValueMax_Object = MibTableColumn
otuKiPmQValueMax = _OtuKiPmQValueMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 13),
    _OtuKiPmQValueMax_Type()
)
otuKiPmQValueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmQValueMax.setStatus("current")
_OtuKiPmQValueAve_Type = FloatHundredths
_OtuKiPmQValueAve_Object = MibTableColumn
otuKiPmQValueAve = _OtuKiPmQValueAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 14),
    _OtuKiPmQValueAve_Type()
)
otuKiPmQValueAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmQValueAve.setStatus("current")
_OtuKiPmBerPreFecMin_Type = FloatArbitraryPrecision
_OtuKiPmBerPreFecMin_Object = MibTableColumn
otuKiPmBerPreFecMin = _OtuKiPmBerPreFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 15),
    _OtuKiPmBerPreFecMin_Type()
)
otuKiPmBerPreFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmBerPreFecMin.setStatus("current")
_OtuKiPmBerPreFecMax_Type = FloatArbitraryPrecision
_OtuKiPmBerPreFecMax_Object = MibTableColumn
otuKiPmBerPreFecMax = _OtuKiPmBerPreFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 16),
    _OtuKiPmBerPreFecMax_Type()
)
otuKiPmBerPreFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmBerPreFecMax.setStatus("current")
_OtuKiPmBerPreFecAve_Type = FloatArbitraryPrecision
_OtuKiPmBerPreFecAve_Object = MibTableColumn
otuKiPmBerPreFecAve = _OtuKiPmBerPreFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 17),
    _OtuKiPmBerPreFecAve_Type()
)
otuKiPmBerPreFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmBerPreFecAve.setStatus("current")
_OtuKiPmBerPostFecMin_Type = FloatArbitraryPrecision
_OtuKiPmBerPostFecMin_Object = MibTableColumn
otuKiPmBerPostFecMin = _OtuKiPmBerPostFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 18),
    _OtuKiPmBerPostFecMin_Type()
)
otuKiPmBerPostFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmBerPostFecMin.setStatus("current")
_OtuKiPmBerPostFecMax_Type = FloatArbitraryPrecision
_OtuKiPmBerPostFecMax_Object = MibTableColumn
otuKiPmBerPostFecMax = _OtuKiPmBerPostFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 19),
    _OtuKiPmBerPostFecMax_Type()
)
otuKiPmBerPostFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmBerPostFecMax.setStatus("current")
_OtuKiPmBerPostFecAve_Type = FloatArbitraryPrecision
_OtuKiPmBerPostFecAve_Object = MibTableColumn
otuKiPmBerPostFecAve = _OtuKiPmBerPostFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 20),
    _OtuKiPmBerPostFecAve_Type()
)
otuKiPmBerPostFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmBerPostFecAve.setStatus("current")
_OtuKiPmRxDefectSecondsFEND_Type = Integer32
_OtuKiPmRxDefectSecondsFEND_Object = MibTableColumn
otuKiPmRxDefectSecondsFEND = _OtuKiPmRxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 21),
    _OtuKiPmRxDefectSecondsFEND_Type()
)
otuKiPmRxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRxDefectSecondsFEND.setStatus("current")
_OtuKiPmCorrectedBits_Type = HCPerfIntervalCount
_OtuKiPmCorrectedBits_Object = MibTableColumn
otuKiPmCorrectedBits = _OtuKiPmCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 22),
    _OtuKiPmCorrectedBits_Type()
)
otuKiPmCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmCorrectedBits.setStatus("current")
_OtuKiPmRxBEICount_Type = HCPerfIntervalCount
_OtuKiPmRxBEICount_Object = MibTableColumn
otuKiPmRxBEICount = _OtuKiPmRxBEICount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 2, 1, 23),
    _OtuKiPmRxBEICount_Type()
)
otuKiPmRxBEICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuKiPmRxBEICount.setStatus("current")
_OtuKiPmConformance_ObjectIdentity = ObjectIdentity
otuKiPmConformance = _OtuKiPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 3)
)
_OtuKiPmCompliances_ObjectIdentity = ObjectIdentity
otuKiPmCompliances = _OtuKiPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 3, 1)
)
_OtuKiPmGroups_ObjectIdentity = ObjectIdentity
otuKiPmGroups = _OtuKiPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 3, 2)
)

# Managed Objects groups

otuKiPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 3, 2, 1)
)
otuKiPmGroup.setObjects(
      *(("INFINERA-PM-OTUKI-MIB", "otuKiPmTimestamp"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmSampleDuration"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmValidity"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmNumberOfCodeWords"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmNumberOfUncorrectedWords"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmNumberOfCorrectedZeros"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmNumberOfCorrectedOnes"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRxErroredBlocks"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRxDefectSeconds"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmCircuitId"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmPayloadType"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmQValueMin"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmQValueMax"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmQValueAve"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmBerPreFecMin"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmBerPreFecMax"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmBerPreFecAve"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmBerPostFecMin"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmBerPostFecMax"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmBerPostFecAve"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRxDefectSecondsFEND"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmCorrectedBits"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRxBEICount"))
)
if mibBuilder.loadTexts:
    otuKiPmGroup.setStatus("current")

otuKiPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 3, 2, 2)
)
otuKiPmRealGroup.setObjects(
      *(("INFINERA-PM-OTUKI-MIB", "otuKiPmRealNumberOfCodeWords"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealNumberOfUncorrectedWords"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealNumberOfCorrectedZeros"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealNumberOfCorrectedOnes"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealRxErroredBlocks"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealRxDefectSeconds"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealQValue"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealBerPreFec"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealBerPostFec"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealRxDefectSecondsFEND"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealCorrectedBits"),
        ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealRxBEICount"))
)
if mibBuilder.loadTexts:
    otuKiPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otuKiPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 3, 1, 1)
)
otuKiPmCompliance.setObjects(
    ("INFINERA-PM-OTUKI-MIB", "otuKiPmGroup")
)
if mibBuilder.loadTexts:
    otuKiPmCompliance.setStatus(
        "current"
    )

otuKiPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 27, 3, 1, 2)
)
otuKiPmRealCompliance.setObjects(
    ("INFINERA-PM-OTUKI-MIB", "otuKiPmRealGroup")
)
if mibBuilder.loadTexts:
    otuKiPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OTUKI-MIB",
    **{"otuKiPmMIB": otuKiPmMIB,
       "otuKiPmRealTable": otuKiPmRealTable,
       "otuKiPmRealEntry": otuKiPmRealEntry,
       "otuKiPmRealNumberOfCodeWords": otuKiPmRealNumberOfCodeWords,
       "otuKiPmRealNumberOfUncorrectedWords": otuKiPmRealNumberOfUncorrectedWords,
       "otuKiPmRealNumberOfCorrectedZeros": otuKiPmRealNumberOfCorrectedZeros,
       "otuKiPmRealNumberOfCorrectedOnes": otuKiPmRealNumberOfCorrectedOnes,
       "otuKiPmRealRxErroredBlocks": otuKiPmRealRxErroredBlocks,
       "otuKiPmRealRxDefectSeconds": otuKiPmRealRxDefectSeconds,
       "otuKiPmRealQValue": otuKiPmRealQValue,
       "otuKiPmRealBerPreFec": otuKiPmRealBerPreFec,
       "otuKiPmRealBerPostFec": otuKiPmRealBerPostFec,
       "otuKiPmRealRxDefectSecondsFEND": otuKiPmRealRxDefectSecondsFEND,
       "otuKiPmRealCorrectedBits": otuKiPmRealCorrectedBits,
       "otuKiPmRealRxBEICount": otuKiPmRealRxBEICount,
       "otuKiPmTable": otuKiPmTable,
       "otuKiPmEntry": otuKiPmEntry,
       "otuKiPmTimestamp": otuKiPmTimestamp,
       "otuKiPmSampleDuration": otuKiPmSampleDuration,
       "otuKiPmValidity": otuKiPmValidity,
       "otuKiPmNumberOfCodeWords": otuKiPmNumberOfCodeWords,
       "otuKiPmNumberOfUncorrectedWords": otuKiPmNumberOfUncorrectedWords,
       "otuKiPmNumberOfCorrectedZeros": otuKiPmNumberOfCorrectedZeros,
       "otuKiPmNumberOfCorrectedOnes": otuKiPmNumberOfCorrectedOnes,
       "otuKiPmRxErroredBlocks": otuKiPmRxErroredBlocks,
       "otuKiPmRxDefectSeconds": otuKiPmRxDefectSeconds,
       "otuKiPmCircuitId": otuKiPmCircuitId,
       "otuKiPmPayloadType": otuKiPmPayloadType,
       "otuKiPmQValueMin": otuKiPmQValueMin,
       "otuKiPmQValueMax": otuKiPmQValueMax,
       "otuKiPmQValueAve": otuKiPmQValueAve,
       "otuKiPmBerPreFecMin": otuKiPmBerPreFecMin,
       "otuKiPmBerPreFecMax": otuKiPmBerPreFecMax,
       "otuKiPmBerPreFecAve": otuKiPmBerPreFecAve,
       "otuKiPmBerPostFecMin": otuKiPmBerPostFecMin,
       "otuKiPmBerPostFecMax": otuKiPmBerPostFecMax,
       "otuKiPmBerPostFecAve": otuKiPmBerPostFecAve,
       "otuKiPmRxDefectSecondsFEND": otuKiPmRxDefectSecondsFEND,
       "otuKiPmCorrectedBits": otuKiPmCorrectedBits,
       "otuKiPmRxBEICount": otuKiPmRxBEICount,
       "otuKiPmConformance": otuKiPmConformance,
       "otuKiPmCompliances": otuKiPmCompliances,
       "otuKiPmCompliance": otuKiPmCompliance,
       "otuKiPmRealCompliance": otuKiPmRealCompliance,
       "otuKiPmGroups": otuKiPmGroups,
       "otuKiPmGroup": otuKiPmGroup,
       "otuKiPmRealGroup": otuKiPmRealGroup}
)
