# SNMP MIB module (INFINERA-TP-CARRIERCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-CARRIERCTP-MIB
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatArbitraryPrecision,
 FloatHundredths,
 FloatTenths,
 InfnCDCompType,
 InfnCDRange,
 InfnCarrierType,
 InfnEnableDisable,
 InfnEnableDisableType,
 InfnEncoding,
 InfnEqptType,
 InfnFFCRAveraging,
 InfnFFCRMode,
 InfnLatencyMode,
 InfnOperationalState,
 InfnOpticalSignal,
 InfnProvBaudRate,
 InfnTuningStatus) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths",
    "FloatTenths",
    "InfnCDCompType",
    "InfnCDRange",
    "InfnCarrierType",
    "InfnEnableDisable",
    "InfnEnableDisableType",
    "InfnEncoding",
    "InfnEqptType",
    "InfnFFCRAveraging",
    "InfnFFCRMode",
    "InfnLatencyMode",
    "InfnOperationalState",
    "InfnOpticalSignal",
    "InfnProvBaudRate",
    "InfnTuningStatus")

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

carrierCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CarrierCtpTable_Object = MibTable
carrierCtpTable = _CarrierCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1)
)
if mibBuilder.loadTexts:
    carrierCtpTable.setStatus("current")
_CarrierCtpEntry_Object = MibTableRow
carrierCtpEntry = _CarrierCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1)
)
carrierCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    carrierCtpEntry.setStatus("current")


class _CarrierCtpPmHistStatsEnable_Type(Integer32):
    """Custom type carrierCtpPmHistStatsEnable based on Integer32"""
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


_CarrierCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_CarrierCtpPmHistStatsEnable_Object = MibTableColumn
carrierCtpPmHistStatsEnable = _CarrierCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 1),
    _CarrierCtpPmHistStatsEnable_Type()
)
carrierCtpPmHistStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierCtpPmHistStatsEnable.setStatus("current")


class _CarrierCtpModulation_Type(Integer32):
    """Custom type carrierCtpModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              101)
        )
    )
    namedValues = NamedValues(
        *(("pmQPSK", 1),
          ("pmBPSK", 2),
          ("pmEnhancedBPSK", 3),
          ("pm3QAM", 4),
          ("pm8QAM", 5),
          ("pm16QAM", 6),
          ("pmNONE", 101))
    )


_CarrierCtpModulation_Type.__name__ = "Integer32"
_CarrierCtpModulation_Object = MibTableColumn
carrierCtpModulation = _CarrierCtpModulation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 2),
    _CarrierCtpModulation_Type()
)
carrierCtpModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpModulation.setStatus("current")
_CarrierCtpCarrierRate_Type = FloatTenths
_CarrierCtpCarrierRate_Object = MibTableColumn
carrierCtpCarrierRate = _CarrierCtpCarrierRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 3),
    _CarrierCtpCarrierRate_Type()
)
carrierCtpCarrierRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpCarrierRate.setStatus("current")
_CarrierCtpEncodingMode_Type = InfnEncoding
_CarrierCtpEncodingMode_Object = MibTableColumn
carrierCtpEncodingMode = _CarrierCtpEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 4),
    _CarrierCtpEncodingMode_Type()
)
carrierCtpEncodingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpEncodingMode.setStatus("current")
_CarrierCtpPMDHighThreshold_Type = FloatTenths
_CarrierCtpPMDHighThreshold_Object = MibTableColumn
carrierCtpPMDHighThreshold = _CarrierCtpPMDHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 5),
    _CarrierCtpPMDHighThreshold_Type()
)
carrierCtpPMDHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpPMDHighThreshold.setStatus("current")
_CarrierCtpPMDHighTCAReporting_Type = InfnEnableDisable
_CarrierCtpPMDHighTCAReporting_Object = MibTableColumn
carrierCtpPMDHighTCAReporting = _CarrierCtpPMDHighTCAReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 6),
    _CarrierCtpPMDHighTCAReporting_Type()
)
carrierCtpPMDHighTCAReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpPMDHighTCAReporting.setStatus("current")
_CarrierCtpCDCompMode_Type = InfnCDCompType
_CarrierCtpCDCompMode_Object = MibTableColumn
carrierCtpCDCompMode = _CarrierCtpCDCompMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 7),
    _CarrierCtpCDCompMode_Type()
)
carrierCtpCDCompMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpCDCompMode.setStatus("current")
_CarrierCtpCDSet_Type = Integer32
_CarrierCtpCDSet_Object = MibTableColumn
carrierCtpCDSet = _CarrierCtpCDSet_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 8),
    _CarrierCtpCDSet_Type()
)
carrierCtpCDSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpCDSet.setStatus("current")
_CarrierCtpCDRange_Type = InfnCDRange
_CarrierCtpCDRange_Object = MibTableColumn
carrierCtpCDRange = _CarrierCtpCDRange_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 9),
    _CarrierCtpCDRange_Type()
)
carrierCtpCDRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpCDRange.setStatus("current")
_CarrierCtpFFCRMode_Type = InfnFFCRMode
_CarrierCtpFFCRMode_Object = MibTableColumn
carrierCtpFFCRMode = _CarrierCtpFFCRMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 10),
    _CarrierCtpFFCRMode_Type()
)
carrierCtpFFCRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpFFCRMode.setStatus("current")
_CarrierCtpFFCRBlockSize_Type = FloatTenths
_CarrierCtpFFCRBlockSize_Object = MibTableColumn
carrierCtpFFCRBlockSize = _CarrierCtpFFCRBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 11),
    _CarrierCtpFFCRBlockSize_Type()
)
carrierCtpFFCRBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpFFCRBlockSize.setStatus("current")
_CarrierCtpFFCRXYAveraging_Type = Integer32
_CarrierCtpFFCRXYAveraging_Object = MibTableColumn
carrierCtpFFCRXYAveraging = _CarrierCtpFFCRXYAveraging_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 12),
    _CarrierCtpFFCRXYAveraging_Type()
)
carrierCtpFFCRXYAveraging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpFFCRXYAveraging.setStatus("current")
_CarrierCtpPreFecBerSigDegTcaRept_Type = InfnEnableDisable
_CarrierCtpPreFecBerSigDegTcaRept_Object = MibTableColumn
carrierCtpPreFecBerSigDegTcaRept = _CarrierCtpPreFecBerSigDegTcaRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 13),
    _CarrierCtpPreFecBerSigDegTcaRept_Type()
)
carrierCtpPreFecBerSigDegTcaRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpPreFecBerSigDegTcaRept.setStatus("current")
_CarrierCtpPreFecQSigDegTcaRept_Type = InfnEnableDisable
_CarrierCtpPreFecQSigDegTcaRept_Object = MibTableColumn
carrierCtpPreFecQSigDegTcaRept = _CarrierCtpPreFecQSigDegTcaRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 14),
    _CarrierCtpPreFecQSigDegTcaRept_Type()
)
carrierCtpPreFecQSigDegTcaRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpPreFecQSigDegTcaRept.setStatus("current")
_CarrierCtpPreFecBerSigDegTh_Type = FloatArbitraryPrecision
_CarrierCtpPreFecBerSigDegTh_Object = MibTableColumn
carrierCtpPreFecBerSigDegTh = _CarrierCtpPreFecBerSigDegTh_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 15),
    _CarrierCtpPreFecBerSigDegTh_Type()
)
carrierCtpPreFecBerSigDegTh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPreFecBerSigDegTh.setStatus("current")
_CarrierCtpPreFecQSigDegTh_Type = FloatArbitraryPrecision
_CarrierCtpPreFecQSigDegTh_Object = MibTableColumn
carrierCtpPreFecQSigDegTh = _CarrierCtpPreFecQSigDegTh_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 16),
    _CarrierCtpPreFecQSigDegTh_Type()
)
carrierCtpPreFecQSigDegTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpPreFecQSigDegTh.setStatus("current")
_CarrierCtpPreFecQSigDegHysteresis_Type = FloatTenths
_CarrierCtpPreFecQSigDegHysteresis_Object = MibTableColumn
carrierCtpPreFecQSigDegHysteresis = _CarrierCtpPreFecQSigDegHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 17),
    _CarrierCtpPreFecQSigDegHysteresis_Type()
)
carrierCtpPreFecQSigDegHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpPreFecQSigDegHysteresis.setStatus("current")
_CarrierCtpPreFecBERSigDegHysteresis_Type = FloatTenths
_CarrierCtpPreFecBERSigDegHysteresis_Object = MibTableColumn
carrierCtpPreFecBERSigDegHysteresis = _CarrierCtpPreFecBERSigDegHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 18),
    _CarrierCtpPreFecBERSigDegHysteresis_Type()
)
carrierCtpPreFecBERSigDegHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPreFecBERSigDegHysteresis.setStatus("current")
_CarrierCtpFineGranularPreFecQ_Type = InfnEnableDisable
_CarrierCtpFineGranularPreFecQ_Object = MibTableColumn
carrierCtpFineGranularPreFecQ = _CarrierCtpFineGranularPreFecQ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 19),
    _CarrierCtpFineGranularPreFecQ_Type()
)
carrierCtpFineGranularPreFecQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpFineGranularPreFecQ.setStatus("current")
_CarrierCtpFineGranularPreFecQSampling_Type = Integer32
_CarrierCtpFineGranularPreFecQSampling_Object = MibTableColumn
carrierCtpFineGranularPreFecQSampling = _CarrierCtpFineGranularPreFecQSampling_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 20),
    _CarrierCtpFineGranularPreFecQSampling_Type()
)
carrierCtpFineGranularPreFecQSampling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpFineGranularPreFecQSampling.setStatus("current")
_CarrierCtpRapidRecovery_Type = InfnEnableDisable
_CarrierCtpRapidRecovery_Object = MibTableColumn
carrierCtpRapidRecovery = _CarrierCtpRapidRecovery_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 21),
    _CarrierCtpRapidRecovery_Type()
)
carrierCtpRapidRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpRapidRecovery.setStatus("current")
_CarrierCtpAggresivePolarizationTracking_Type = InfnEnableDisable
_CarrierCtpAggresivePolarizationTracking_Object = MibTableColumn
carrierCtpAggresivePolarizationTracking = _CarrierCtpAggresivePolarizationTracking_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 22),
    _CarrierCtpAggresivePolarizationTracking_Type()
)
carrierCtpAggresivePolarizationTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpAggresivePolarizationTracking.setStatus("current")
_CarrierCtpFrequency_Type = DisplayString
_CarrierCtpFrequency_Object = MibTableColumn
carrierCtpFrequency = _CarrierCtpFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 23),
    _CarrierCtpFrequency_Type()
)
carrierCtpFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpFrequency.setStatus("current")
_CarrierCtpFFCRAveraging_Type = InfnFFCRAveraging
_CarrierCtpFFCRAveraging_Object = MibTableColumn
carrierCtpFFCRAveraging = _CarrierCtpFFCRAveraging_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 24),
    _CarrierCtpFFCRAveraging_Type()
)
carrierCtpFFCRAveraging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpFFCRAveraging.setStatus("current")
_CarrierCtpBaudRate_Type = InfnProvBaudRate
_CarrierCtpBaudRate_Object = MibTableColumn
carrierCtpBaudRate = _CarrierCtpBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 25),
    _CarrierCtpBaudRate_Type()
)
carrierCtpBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpBaudRate.setStatus("current")
_CarrierCtpProvGainSharing_Type = InfnOperationalState
_CarrierCtpProvGainSharing_Object = MibTableColumn
carrierCtpProvGainSharing = _CarrierCtpProvGainSharing_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 26),
    _CarrierCtpProvGainSharing_Type()
)
carrierCtpProvGainSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpProvGainSharing.setStatus("current")
_CarrierCtpGainSharing_Type = InfnOperationalState
_CarrierCtpGainSharing_Object = MibTableColumn
carrierCtpGainSharing = _CarrierCtpGainSharing_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 27),
    _CarrierCtpGainSharing_Type()
)
carrierCtpGainSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpGainSharing.setStatus("current")
_CarrierCtpProvFecIterations_Type = Integer32
_CarrierCtpProvFecIterations_Object = MibTableColumn
carrierCtpProvFecIterations = _CarrierCtpProvFecIterations_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 28),
    _CarrierCtpProvFecIterations_Type()
)
carrierCtpProvFecIterations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpProvFecIterations.setStatus("current")
_CarrierCtpFecIterations_Type = Integer32
_CarrierCtpFecIterations_Object = MibTableColumn
carrierCtpFecIterations = _CarrierCtpFecIterations_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 29),
    _CarrierCtpFecIterations_Type()
)
carrierCtpFecIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpFecIterations.setStatus("current")
_CarrierCtpTxCD_Type = Integer32
_CarrierCtpTxCD_Object = MibTableColumn
carrierCtpTxCD = _CarrierCtpTxCD_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 30),
    _CarrierCtpTxCD_Type()
)
carrierCtpTxCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpTxCD.setStatus("current")
_CarrierCtpProvTxCD_Type = Integer32
_CarrierCtpProvTxCD_Object = MibTableColumn
carrierCtpProvTxCD = _CarrierCtpProvTxCD_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 31),
    _CarrierCtpProvTxCD_Type()
)
carrierCtpProvTxCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpProvTxCD.setStatus("current")
_CarrierCtpLatency_Type = InfnLatencyMode
_CarrierCtpLatency_Object = MibTableColumn
carrierCtpLatency = _CarrierCtpLatency_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 32),
    _CarrierCtpLatency_Type()
)
carrierCtpLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpLatency.setStatus("current")
_CarrierCtpOpticalSignal_Type = InfnOpticalSignal
_CarrierCtpOpticalSignal_Object = MibTableColumn
carrierCtpOpticalSignal = _CarrierCtpOpticalSignal_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 33),
    _CarrierCtpOpticalSignal_Type()
)
carrierCtpOpticalSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpOpticalSignal.setStatus("current")
_CarrierCtpTuningStatus_Type = InfnTuningStatus
_CarrierCtpTuningStatus_Object = MibTableColumn
carrierCtpTuningStatus = _CarrierCtpTuningStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 34),
    _CarrierCtpTuningStatus_Type()
)
carrierCtpTuningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpTuningStatus.setStatus("current")
_CarrierCtpBwResilientSsLoopControl_Type = InfnEnableDisableType
_CarrierCtpBwResilientSsLoopControl_Object = MibTableColumn
carrierCtpBwResilientSsLoopControl = _CarrierCtpBwResilientSsLoopControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 35),
    _CarrierCtpBwResilientSsLoopControl_Type()
)
carrierCtpBwResilientSsLoopControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpBwResilientSsLoopControl.setStatus("current")
_CarrierCtpBwResilientCtLoopControl_Type = InfnEnableDisableType
_CarrierCtpBwResilientCtLoopControl_Object = MibTableColumn
carrierCtpBwResilientCtLoopControl = _CarrierCtpBwResilientCtLoopControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 36),
    _CarrierCtpBwResilientCtLoopControl_Type()
)
carrierCtpBwResilientCtLoopControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpBwResilientCtLoopControl.setStatus("current")
_CarrierCtpProvLatency_Type = InfnLatencyMode
_CarrierCtpProvLatency_Object = MibTableColumn
carrierCtpProvLatency = _CarrierCtpProvLatency_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 37),
    _CarrierCtpProvLatency_Type()
)
carrierCtpProvLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpProvLatency.setStatus("current")
_CarrierCtpInstCDSet_Type = Integer32
_CarrierCtpInstCDSet_Object = MibTableColumn
carrierCtpInstCDSet = _CarrierCtpInstCDSet_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 38),
    _CarrierCtpInstCDSet_Type()
)
carrierCtpInstCDSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpInstCDSet.setStatus("current")
_CarrierCtpClockMode_Type = Unsigned32
_CarrierCtpClockMode_Object = MibTableColumn
carrierCtpClockMode = _CarrierCtpClockMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 39),
    _CarrierCtpClockMode_Type()
)
carrierCtpClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpClockMode.setStatus("current")
_CarrierCtpNLCSetting_Type = Unsigned32
_CarrierCtpNLCSetting_Object = MibTableColumn
carrierCtpNLCSetting = _CarrierCtpNLCSetting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 40),
    _CarrierCtpNLCSetting_Type()
)
carrierCtpNLCSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierCtpNLCSetting.setStatus("current")
_CarrierCtpNLCStatus_Type = Unsigned32
_CarrierCtpNLCStatus_Object = MibTableColumn
carrierCtpNLCStatus = _CarrierCtpNLCStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 1, 1, 41),
    _CarrierCtpNLCStatus_Type()
)
carrierCtpNLCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpNLCStatus.setStatus("current")
_CarrierCtpConformance_ObjectIdentity = ObjectIdentity
carrierCtpConformance = _CarrierCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 37)
)
_CarrierCtpCompliances_ObjectIdentity = ObjectIdentity
carrierCtpCompliances = _CarrierCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 37, 1)
)
_CarrierCtpGroups_ObjectIdentity = ObjectIdentity
carrierCtpGroups = _CarrierCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 37, 2)
)

# Managed Objects groups

carrierCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 37, 2, 1)
)
carrierCtpGroup.setObjects(
      *(("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpPmHistStatsEnable"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpModulation"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpCarrierRate"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpEncodingMode"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpPMDHighThreshold"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpPMDHighTCAReporting"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpCDCompMode"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpCDRange"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpFFCRMode"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpFFCRBlockSize"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpPreFecBerSigDegTcaRept"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpPreFecQSigDegTcaRept"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpPreFecBerSigDegTh"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpPreFecQSigDegTh"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpPreFecQSigDegHysteresis"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpPreFecBERSigDegHysteresis"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpFFCRXYAveraging"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpCDSet"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpFineGranularPreFecQ"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpFineGranularPreFecQSampling"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpRapidRecovery"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpAggresivePolarizationTracking"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpFrequency"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpFFCRAveraging"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpBaudRate"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpProvGainSharing"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpGainSharing"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpProvFecIterations"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpFecIterations"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpTxCD"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpProvTxCD"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpLatency"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpOpticalSignal"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpTuningStatus"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpBwResilientSsLoopControl"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpBwResilientCtLoopControl"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpProvLatency"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpInstCDSet"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpClockMode"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpNLCSetting"),
        ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpNLCStatus"))
)
if mibBuilder.loadTexts:
    carrierCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

carrierCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 38, 37, 1, 1)
)
carrierCtpCompliance.setObjects(
    ("INFINERA-TP-CARRIERCTP-MIB", "carrierCtpGroup")
)
if mibBuilder.loadTexts:
    carrierCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-CARRIERCTP-MIB",
    **{"carrierCtpMIB": carrierCtpMIB,
       "carrierCtpTable": carrierCtpTable,
       "carrierCtpEntry": carrierCtpEntry,
       "carrierCtpPmHistStatsEnable": carrierCtpPmHistStatsEnable,
       "carrierCtpModulation": carrierCtpModulation,
       "carrierCtpCarrierRate": carrierCtpCarrierRate,
       "carrierCtpEncodingMode": carrierCtpEncodingMode,
       "carrierCtpPMDHighThreshold": carrierCtpPMDHighThreshold,
       "carrierCtpPMDHighTCAReporting": carrierCtpPMDHighTCAReporting,
       "carrierCtpCDCompMode": carrierCtpCDCompMode,
       "carrierCtpCDSet": carrierCtpCDSet,
       "carrierCtpCDRange": carrierCtpCDRange,
       "carrierCtpFFCRMode": carrierCtpFFCRMode,
       "carrierCtpFFCRBlockSize": carrierCtpFFCRBlockSize,
       "carrierCtpFFCRXYAveraging": carrierCtpFFCRXYAveraging,
       "carrierCtpPreFecBerSigDegTcaRept": carrierCtpPreFecBerSigDegTcaRept,
       "carrierCtpPreFecQSigDegTcaRept": carrierCtpPreFecQSigDegTcaRept,
       "carrierCtpPreFecBerSigDegTh": carrierCtpPreFecBerSigDegTh,
       "carrierCtpPreFecQSigDegTh": carrierCtpPreFecQSigDegTh,
       "carrierCtpPreFecQSigDegHysteresis": carrierCtpPreFecQSigDegHysteresis,
       "carrierCtpPreFecBERSigDegHysteresis": carrierCtpPreFecBERSigDegHysteresis,
       "carrierCtpFineGranularPreFecQ": carrierCtpFineGranularPreFecQ,
       "carrierCtpFineGranularPreFecQSampling": carrierCtpFineGranularPreFecQSampling,
       "carrierCtpRapidRecovery": carrierCtpRapidRecovery,
       "carrierCtpAggresivePolarizationTracking": carrierCtpAggresivePolarizationTracking,
       "carrierCtpFrequency": carrierCtpFrequency,
       "carrierCtpFFCRAveraging": carrierCtpFFCRAveraging,
       "carrierCtpBaudRate": carrierCtpBaudRate,
       "carrierCtpProvGainSharing": carrierCtpProvGainSharing,
       "carrierCtpGainSharing": carrierCtpGainSharing,
       "carrierCtpProvFecIterations": carrierCtpProvFecIterations,
       "carrierCtpFecIterations": carrierCtpFecIterations,
       "carrierCtpTxCD": carrierCtpTxCD,
       "carrierCtpProvTxCD": carrierCtpProvTxCD,
       "carrierCtpLatency": carrierCtpLatency,
       "carrierCtpOpticalSignal": carrierCtpOpticalSignal,
       "carrierCtpTuningStatus": carrierCtpTuningStatus,
       "carrierCtpBwResilientSsLoopControl": carrierCtpBwResilientSsLoopControl,
       "carrierCtpBwResilientCtLoopControl": carrierCtpBwResilientCtLoopControl,
       "carrierCtpProvLatency": carrierCtpProvLatency,
       "carrierCtpInstCDSet": carrierCtpInstCDSet,
       "carrierCtpClockMode": carrierCtpClockMode,
       "carrierCtpNLCSetting": carrierCtpNLCSetting,
       "carrierCtpNLCStatus": carrierCtpNLCStatus,
       "carrierCtpConformance": carrierCtpConformance,
       "carrierCtpCompliances": carrierCtpCompliances,
       "carrierCtpCompliance": carrierCtpCompliance,
       "carrierCtpGroups": carrierCtpGroups,
       "carrierCtpGroup": carrierCtpGroup}
)
