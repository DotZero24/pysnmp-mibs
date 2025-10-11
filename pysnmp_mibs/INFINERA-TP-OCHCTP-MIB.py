# SNMP MIB module (INFINERA-TP-OCHCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OCHCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:22 2025
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

(FloatTenths,
 InfnCDCompType,
 InfnCDRange,
 InfnCarrierType,
 InfnEnableDisable,
 InfnEncoding,
 InfnFFCRMode,
 InfnModulation,
 InfnPmHistStatsControl,
 InfnReporting,
 InfnTxDisableActionOnAdminLock,
 InfnUsageState,
 InfnXYAlignment) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnCDCompType",
    "InfnCDRange",
    "InfnCarrierType",
    "InfnEnableDisable",
    "InfnEncoding",
    "InfnFFCRMode",
    "InfnModulation",
    "InfnPmHistStatsControl",
    "InfnReporting",
    "InfnTxDisableActionOnAdminLock",
    "InfnUsageState",
    "InfnXYAlignment")

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

ochCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33)
)
if mibBuilder.loadTexts:
    ochCtpMIB.setRevisions(
        ("2011-09-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OchCtpTable_Object = MibTable
ochCtpTable = _OchCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1)
)
if mibBuilder.loadTexts:
    ochCtpTable.setStatus("current")
_OchCtpEntry_Object = MibTableRow
ochCtpEntry = _OchCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1)
)
ochCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ochCtpEntry.setStatus("current")
_OchCtpSignalDegradeReporting_Type = InfnReporting
_OchCtpSignalDegradeReporting_Object = MibTableColumn
ochCtpSignalDegradeReporting = _OchCtpSignalDegradeReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 1),
    _OchCtpSignalDegradeReporting_Type()
)
ochCtpSignalDegradeReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpSignalDegradeReporting.setStatus("current")


class _OchCtpPmHistStatsEnable_Type(InfnPmHistStatsControl):
    """Custom type ochCtpPmHistStatsEnable based on InfnPmHistStatsControl"""
    defaultValue = 1


_OchCtpPmHistStatsEnable_Type.__name__ = "InfnPmHistStatsControl"
_OchCtpPmHistStatsEnable_Object = MibTableColumn
ochCtpPmHistStatsEnable = _OchCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 2),
    _OchCtpPmHistStatsEnable_Type()
)
ochCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpPmHistStatsEnable.setStatus("current")
_OchCtpCarrierGroupMode_Type = InfnCarrierType
_OchCtpCarrierGroupMode_Object = MibTableColumn
ochCtpCarrierGroupMode = _OchCtpCarrierGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 3),
    _OchCtpCarrierGroupMode_Type()
)
ochCtpCarrierGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpCarrierGroupMode.setStatus("current")
_OchCtpModulation_Type = InfnModulation
_OchCtpModulation_Object = MibTableColumn
ochCtpModulation = _OchCtpModulation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 4),
    _OchCtpModulation_Type()
)
ochCtpModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpModulation.setStatus("current")
_OchCtpRate_Type = Integer32
_OchCtpRate_Object = MibTableColumn
ochCtpRate = _OchCtpRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 5),
    _OchCtpRate_Type()
)
ochCtpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpRate.setStatus("current")
_OchCtpDataUsageState_Type = InfnUsageState
_OchCtpDataUsageState_Object = MibTableColumn
ochCtpDataUsageState = _OchCtpDataUsageState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 6),
    _OchCtpDataUsageState_Type()
)
ochCtpDataUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpDataUsageState.setStatus("current")
_OchCtpCDCompMode_Type = InfnCDCompType
_OchCtpCDCompMode_Object = MibTableColumn
ochCtpCDCompMode = _OchCtpCDCompMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 7),
    _OchCtpCDCompMode_Type()
)
ochCtpCDCompMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpCDCompMode.setStatus("current")
_OchCtpChromaticDispersionSet_Type = FloatTenths
_OchCtpChromaticDispersionSet_Object = MibTableColumn
ochCtpChromaticDispersionSet = _OchCtpChromaticDispersionSet_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 8),
    _OchCtpChromaticDispersionSet_Type()
)
ochCtpChromaticDispersionSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpChromaticDispersionSet.setStatus("current")
_OchCtpFFCRMode_Type = InfnFFCRMode
_OchCtpFFCRMode_Object = MibTableColumn
ochCtpFFCRMode = _OchCtpFFCRMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 9),
    _OchCtpFFCRMode_Type()
)
ochCtpFFCRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpFFCRMode.setStatus("current")
_OchCtpFFCRBlockSize_Type = FloatTenths
_OchCtpFFCRBlockSize_Object = MibTableColumn
ochCtpFFCRBlockSize = _OchCtpFFCRBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 10),
    _OchCtpFFCRBlockSize_Type()
)
ochCtpFFCRBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpFFCRBlockSize.setStatus("current")
_OchCtpFFCRXYAveraging_Type = Integer32
_OchCtpFFCRXYAveraging_Object = MibTableColumn
ochCtpFFCRXYAveraging = _OchCtpFFCRXYAveraging_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 11),
    _OchCtpFFCRXYAveraging_Type()
)
ochCtpFFCRXYAveraging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpFFCRXYAveraging.setStatus("current")
_OchCtpLaneShuffling_Type = InfnEnableDisable
_OchCtpLaneShuffling_Object = MibTableColumn
ochCtpLaneShuffling = _OchCtpLaneShuffling_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 12),
    _OchCtpLaneShuffling_Type()
)
ochCtpLaneShuffling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpLaneShuffling.setStatus("current")
_OchCtpTxDisableActionOnAdminLock_Type = InfnTxDisableActionOnAdminLock
_OchCtpTxDisableActionOnAdminLock_Object = MibTableColumn
ochCtpTxDisableActionOnAdminLock = _OchCtpTxDisableActionOnAdminLock_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 13),
    _OchCtpTxDisableActionOnAdminLock_Type()
)
ochCtpTxDisableActionOnAdminLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpTxDisableActionOnAdminLock.setStatus("current")
_OchCtpTxShutdown_Type = TruthValue
_OchCtpTxShutdown_Object = MibTableColumn
ochCtpTxShutdown = _OchCtpTxShutdown_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 14),
    _OchCtpTxShutdown_Type()
)
ochCtpTxShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpTxShutdown.setStatus("current")
_OchCtpEncodingMode_Type = InfnEncoding
_OchCtpEncodingMode_Object = MibTableColumn
ochCtpEncodingMode = _OchCtpEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 15),
    _OchCtpEncodingMode_Type()
)
ochCtpEncodingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpEncodingMode.setStatus("current")
_OchCtpTxXYAlignment_Type = InfnXYAlignment
_OchCtpTxXYAlignment_Object = MibTableColumn
ochCtpTxXYAlignment = _OchCtpTxXYAlignment_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 16),
    _OchCtpTxXYAlignment_Type()
)
ochCtpTxXYAlignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpTxXYAlignment.setStatus("current")
_OchCtpPmdHighThreshold_Type = FloatTenths
_OchCtpPmdHighThreshold_Object = MibTableColumn
ochCtpPmdHighThreshold = _OchCtpPmdHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 17),
    _OchCtpPmdHighThreshold_Type()
)
ochCtpPmdHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpPmdHighThreshold.setStatus("current")
_OchCtpPmdHighTCAReporting_Type = InfnEnableDisable
_OchCtpPmdHighTCAReporting_Object = MibTableColumn
ochCtpPmdHighTCAReporting = _OchCtpPmdHighTCAReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 18),
    _OchCtpPmdHighTCAReporting_Type()
)
ochCtpPmdHighTCAReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpPmdHighTCAReporting.setStatus("current")
_OchCtpPreFecQSigDegThreshold_Type = FloatTenths
_OchCtpPreFecQSigDegThreshold_Object = MibTableColumn
ochCtpPreFecQSigDegThreshold = _OchCtpPreFecQSigDegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 19),
    _OchCtpPreFecQSigDegThreshold_Type()
)
ochCtpPreFecQSigDegThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpPreFecQSigDegThreshold.setStatus("current")
_OchCtpPreFecQSigDegHysteresis_Type = FloatTenths
_OchCtpPreFecQSigDegHysteresis_Object = MibTableColumn
ochCtpPreFecQSigDegHysteresis = _OchCtpPreFecQSigDegHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 20),
    _OchCtpPreFecQSigDegHysteresis_Type()
)
ochCtpPreFecQSigDegHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpPreFecQSigDegHysteresis.setStatus("current")
_OchCtpPreFecQSigDegTCAReporting_Type = InfnEnableDisable
_OchCtpPreFecQSigDegTCAReporting_Object = MibTableColumn
ochCtpPreFecQSigDegTCAReporting = _OchCtpPreFecQSigDegTCAReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 21),
    _OchCtpPreFecQSigDegTCAReporting_Type()
)
ochCtpPreFecQSigDegTCAReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpPreFecQSigDegTCAReporting.setStatus("current")
_OchCtpPreFecBERSigDegThreshold_Type = FloatTenths
_OchCtpPreFecBERSigDegThreshold_Object = MibTableColumn
ochCtpPreFecBERSigDegThreshold = _OchCtpPreFecBERSigDegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 22),
    _OchCtpPreFecBERSigDegThreshold_Type()
)
ochCtpPreFecBERSigDegThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPreFecBERSigDegThreshold.setStatus("current")
_OchCtpPreFecBERSigDegHysteresis_Type = FloatTenths
_OchCtpPreFecBERSigDegHysteresis_Object = MibTableColumn
ochCtpPreFecBERSigDegHysteresis = _OchCtpPreFecBERSigDegHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 23),
    _OchCtpPreFecBERSigDegHysteresis_Type()
)
ochCtpPreFecBERSigDegHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPreFecBERSigDegHysteresis.setStatus("current")
_OchCtpPreFecBERSigDegTCAReporting_Type = InfnEnableDisable
_OchCtpPreFecBERSigDegTCAReporting_Object = MibTableColumn
ochCtpPreFecBERSigDegTCAReporting = _OchCtpPreFecBERSigDegTCAReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 24),
    _OchCtpPreFecBERSigDegTCAReporting_Type()
)
ochCtpPreFecBERSigDegTCAReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPreFecBERSigDegTCAReporting.setStatus("current")
_OchCtpSupportingCarrierList_Type = DisplayString
_OchCtpSupportingCarrierList_Object = MibTableColumn
ochCtpSupportingCarrierList = _OchCtpSupportingCarrierList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 25),
    _OchCtpSupportingCarrierList_Type()
)
ochCtpSupportingCarrierList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpSupportingCarrierList.setStatus("current")
_OchCtpChromaticDispersionRange_Type = InfnCDRange
_OchCtpChromaticDispersionRange_Object = MibTableColumn
ochCtpChromaticDispersionRange = _OchCtpChromaticDispersionRange_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 26),
    _OchCtpChromaticDispersionRange_Type()
)
ochCtpChromaticDispersionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpChromaticDispersionRange.setStatus("current")
_OchCtpFineGranularPreFecQ_Type = InfnEnableDisable
_OchCtpFineGranularPreFecQ_Object = MibTableColumn
ochCtpFineGranularPreFecQ = _OchCtpFineGranularPreFecQ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 27),
    _OchCtpFineGranularPreFecQ_Type()
)
ochCtpFineGranularPreFecQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpFineGranularPreFecQ.setStatus("current")
_OchCtpFineGranularPreFecQSampling_Type = Integer32
_OchCtpFineGranularPreFecQSampling_Object = MibTableColumn
ochCtpFineGranularPreFecQSampling = _OchCtpFineGranularPreFecQSampling_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 28),
    _OchCtpFineGranularPreFecQSampling_Type()
)
ochCtpFineGranularPreFecQSampling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpFineGranularPreFecQSampling.setStatus("current")
_OchCtpRapidRecovery_Type = InfnEnableDisable
_OchCtpRapidRecovery_Object = MibTableColumn
ochCtpRapidRecovery = _OchCtpRapidRecovery_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 29),
    _OchCtpRapidRecovery_Type()
)
ochCtpRapidRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpRapidRecovery.setStatus("current")
_OchCtpAggresivePolarizationTracking_Type = InfnEnableDisable
_OchCtpAggresivePolarizationTracking_Object = MibTableColumn
ochCtpAggresivePolarizationTracking = _OchCtpAggresivePolarizationTracking_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 30),
    _OchCtpAggresivePolarizationTracking_Type()
)
ochCtpAggresivePolarizationTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpAggresivePolarizationTracking.setStatus("current")
_OchCtpBwResilientSsLoopControl_Type = InfnEnableDisable
_OchCtpBwResilientSsLoopControl_Object = MibTableColumn
ochCtpBwResilientSsLoopControl = _OchCtpBwResilientSsLoopControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 31),
    _OchCtpBwResilientSsLoopControl_Type()
)
ochCtpBwResilientSsLoopControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpBwResilientSsLoopControl.setStatus("current")
_OchCtpBwResilientCtLoopControl_Type = InfnEnableDisable
_OchCtpBwResilientCtLoopControl_Object = MibTableColumn
ochCtpBwResilientCtLoopControl = _OchCtpBwResilientCtLoopControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 1, 1, 32),
    _OchCtpBwResilientCtLoopControl_Type()
)
ochCtpBwResilientCtLoopControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ochCtpBwResilientCtLoopControl.setStatus("current")
_OchCtpConformance_ObjectIdentity = ObjectIdentity
ochCtpConformance = _OchCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 3)
)
_OchCtpCompliances_ObjectIdentity = ObjectIdentity
ochCtpCompliances = _OchCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 3, 1)
)
_OchCtpGroups_ObjectIdentity = ObjectIdentity
ochCtpGroups = _OchCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 3, 2)
)

# Managed Objects groups

ochCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 3, 2, 1)
)
ochCtpGroup.setObjects(
      *(("INFINERA-TP-OCHCTP-MIB", "ochCtpSignalDegradeReporting"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpPmHistStatsEnable"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpCarrierGroupMode"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpModulation"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpRate"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpDataUsageState"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpCDCompMode"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpChromaticDispersionSet"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpFFCRMode"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpFFCRBlockSize"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpFFCRXYAveraging"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpLaneShuffling"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpTxDisableActionOnAdminLock"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpTxShutdown"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpEncodingMode"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpTxXYAlignment"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpPmdHighThreshold"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpPmdHighTCAReporting"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpPreFecQSigDegThreshold"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpPreFecQSigDegHysteresis"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpPreFecQSigDegTCAReporting"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpPreFecBERSigDegThreshold"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpPreFecBERSigDegHysteresis"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpPreFecBERSigDegTCAReporting"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpSupportingCarrierList"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpChromaticDispersionRange"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpFineGranularPreFecQ"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpFineGranularPreFecQSampling"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpRapidRecovery"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpAggresivePolarizationTracking"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpBwResilientSsLoopControl"),
        ("INFINERA-TP-OCHCTP-MIB", "ochCtpBwResilientCtLoopControl"))
)
if mibBuilder.loadTexts:
    ochCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ochCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 33, 3, 1, 1)
)
ochCtpCompliance.setObjects(
    ("INFINERA-TP-OCHCTP-MIB", "ochCtpGroup")
)
if mibBuilder.loadTexts:
    ochCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OCHCTP-MIB",
    **{"ochCtpMIB": ochCtpMIB,
       "ochCtpTable": ochCtpTable,
       "ochCtpEntry": ochCtpEntry,
       "ochCtpSignalDegradeReporting": ochCtpSignalDegradeReporting,
       "ochCtpPmHistStatsEnable": ochCtpPmHistStatsEnable,
       "ochCtpCarrierGroupMode": ochCtpCarrierGroupMode,
       "ochCtpModulation": ochCtpModulation,
       "ochCtpRate": ochCtpRate,
       "ochCtpDataUsageState": ochCtpDataUsageState,
       "ochCtpCDCompMode": ochCtpCDCompMode,
       "ochCtpChromaticDispersionSet": ochCtpChromaticDispersionSet,
       "ochCtpFFCRMode": ochCtpFFCRMode,
       "ochCtpFFCRBlockSize": ochCtpFFCRBlockSize,
       "ochCtpFFCRXYAveraging": ochCtpFFCRXYAveraging,
       "ochCtpLaneShuffling": ochCtpLaneShuffling,
       "ochCtpTxDisableActionOnAdminLock": ochCtpTxDisableActionOnAdminLock,
       "ochCtpTxShutdown": ochCtpTxShutdown,
       "ochCtpEncodingMode": ochCtpEncodingMode,
       "ochCtpTxXYAlignment": ochCtpTxXYAlignment,
       "ochCtpPmdHighThreshold": ochCtpPmdHighThreshold,
       "ochCtpPmdHighTCAReporting": ochCtpPmdHighTCAReporting,
       "ochCtpPreFecQSigDegThreshold": ochCtpPreFecQSigDegThreshold,
       "ochCtpPreFecQSigDegHysteresis": ochCtpPreFecQSigDegHysteresis,
       "ochCtpPreFecQSigDegTCAReporting": ochCtpPreFecQSigDegTCAReporting,
       "ochCtpPreFecBERSigDegThreshold": ochCtpPreFecBERSigDegThreshold,
       "ochCtpPreFecBERSigDegHysteresis": ochCtpPreFecBERSigDegHysteresis,
       "ochCtpPreFecBERSigDegTCAReporting": ochCtpPreFecBERSigDegTCAReporting,
       "ochCtpSupportingCarrierList": ochCtpSupportingCarrierList,
       "ochCtpChromaticDispersionRange": ochCtpChromaticDispersionRange,
       "ochCtpFineGranularPreFecQ": ochCtpFineGranularPreFecQ,
       "ochCtpFineGranularPreFecQSampling": ochCtpFineGranularPreFecQSampling,
       "ochCtpRapidRecovery": ochCtpRapidRecovery,
       "ochCtpAggresivePolarizationTracking": ochCtpAggresivePolarizationTracking,
       "ochCtpBwResilientSsLoopControl": ochCtpBwResilientSsLoopControl,
       "ochCtpBwResilientCtLoopControl": ochCtpBwResilientCtLoopControl,
       "ochCtpConformance": ochCtpConformance,
       "ochCtpCompliances": ochCtpCompliances,
       "ochCtpCompliance": ochCtpCompliance,
       "ochCtpGroups": ochCtpGroups,
       "ochCtpGroup": ochCtpGroup}
)
