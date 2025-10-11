# SNMP MIB module (INFINERA-TP-XSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-XSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:03 2025
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
 InfnAdTpType,
 InfnAutoDiscoveryState,
 InfnEnableDisable,
 InfnEncoding,
 InfnEqptType,
 InfnFECOverHeadPercent,
 InfnLicenseModulationType,
 InfnLineSystemMode,
 InfnOpticalSignal,
 InfnOpticalSignalStatus,
 InfnPCLOperatingMode,
 InfnPicStatus,
 InfnPmHistStatsControl,
 InfnPowerControlLoop,
 InfnWaveInterfaceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths",
    "FloatTenths",
    "InfnAdTpType",
    "InfnAutoDiscoveryState",
    "InfnEnableDisable",
    "InfnEncoding",
    "InfnEqptType",
    "InfnFECOverHeadPercent",
    "InfnLicenseModulationType",
    "InfnLineSystemMode",
    "InfnOpticalSignal",
    "InfnOpticalSignalStatus",
    "InfnPCLOperatingMode",
    "InfnPicStatus",
    "InfnPmHistStatsControl",
    "InfnPowerControlLoop",
    "InfnWaveInterfaceType")

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

xScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57)
)
if mibBuilder.loadTexts:
    xScgPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XScgPtpTable_Object = MibTable
xScgPtpTable = _XScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1)
)
if mibBuilder.loadTexts:
    xScgPtpTable.setStatus("current")
_XScgPtpEntry_Object = MibTableRow
xScgPtpEntry = _XScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1)
)
xScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xScgPtpEntry.setStatus("current")
_XScgPtpOpenwaveTargetTxScgPower_Type = FloatTenths
_XScgPtpOpenwaveTargetTxScgPower_Object = MibTableColumn
xScgPtpOpenwaveTargetTxScgPower = _XScgPtpOpenwaveTargetTxScgPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 1),
    _XScgPtpOpenwaveTargetTxScgPower_Type()
)
xScgPtpOpenwaveTargetTxScgPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpOpenwaveTargetTxScgPower.setStatus("current")
_XScgPtpMPOAID_Type = DisplayString
_XScgPtpMPOAID_Object = MibTableColumn
xScgPtpMPOAID = _XScgPtpMPOAID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 2),
    _XScgPtpMPOAID_Type()
)
xScgPtpMPOAID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpMPOAID.setStatus("current")
_XScgPtpProvisionedFPMPO_Type = DisplayString
_XScgPtpProvisionedFPMPO_Object = MibTableColumn
xScgPtpProvisionedFPMPO = _XScgPtpProvisionedFPMPO_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 3),
    _XScgPtpProvisionedFPMPO_Type()
)
xScgPtpProvisionedFPMPO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpProvisionedFPMPO.setStatus("current")
_XScgPtpAutoDiscoveryState_Type = InfnAutoDiscoveryState
_XScgPtpAutoDiscoveryState_Object = MibTableColumn
xScgPtpAutoDiscoveryState = _XScgPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 4),
    _XScgPtpAutoDiscoveryState_Type()
)
xScgPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpAutoDiscoveryState.setStatus("current")
_XScgPtpDiscoveredNeighborTP_Type = DisplayString
_XScgPtpDiscoveredNeighborTP_Object = MibTableColumn
xScgPtpDiscoveredNeighborTP = _XScgPtpDiscoveredNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 5),
    _XScgPtpDiscoveredNeighborTP_Type()
)
xScgPtpDiscoveredNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpDiscoveredNeighborTP.setStatus("current")
_XScgPtpProvisionedNeighborTP_Type = DisplayString
_XScgPtpProvisionedNeighborTP_Object = MibTableColumn
xScgPtpProvisionedNeighborTP = _XScgPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 6),
    _XScgPtpProvisionedNeighborTP_Type()
)
xScgPtpProvisionedNeighborTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpProvisionedNeighborTP.setStatus("current")
_XScgPtpProvisionedNeighborAdTpType_Type = InfnAdTpType
_XScgPtpProvisionedNeighborAdTpType_Object = MibTableColumn
xScgPtpProvisionedNeighborAdTpType = _XScgPtpProvisionedNeighborAdTpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 7),
    _XScgPtpProvisionedNeighborAdTpType_Type()
)
xScgPtpProvisionedNeighborAdTpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpProvisionedNeighborAdTpType.setStatus("current")
_XScgPtpInterfaceType_Type = InfnWaveInterfaceType
_XScgPtpInterfaceType_Object = MibTableColumn
xScgPtpInterfaceType = _XScgPtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 8),
    _XScgPtpInterfaceType_Type()
)
xScgPtpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpInterfaceType.setStatus("current")
_XScgPtpProvisionedOpenWaveRemotePtp_Type = DisplayString
_XScgPtpProvisionedOpenWaveRemotePtp_Object = MibTableColumn
xScgPtpProvisionedOpenWaveRemotePtp = _XScgPtpProvisionedOpenWaveRemotePtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 9),
    _XScgPtpProvisionedOpenWaveRemotePtp_Type()
)
xScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpProvisionedOpenWaveRemotePtp.setStatus("current")
_XScgPtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_XScgPtpPmHistStatsEnable_Object = MibTableColumn
xScgPtpPmHistStatsEnable = _XScgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 10),
    _XScgPtpPmHistStatsEnable_Type()
)
xScgPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpPmHistStatsEnable.setStatus("current")
_XScgPtpMaxFruGain_Type = FloatHundredths
_XScgPtpMaxFruGain_Object = MibTableColumn
xScgPtpMaxFruGain = _XScgPtpMaxFruGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 11),
    _XScgPtpMaxFruGain_Type()
)
xScgPtpMaxFruGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpMaxFruGain.setStatus("current")
_XScgPtpRecommendedGain_Type = FloatTenths
_XScgPtpRecommendedGain_Object = MibTableColumn
xScgPtpRecommendedGain = _XScgPtpRecommendedGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 12),
    _XScgPtpRecommendedGain_Type()
)
xScgPtpRecommendedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpRecommendedGain.setStatus("current")
_XScgPtpRxEdfaOutputPowerTarget_Type = FloatTenths
_XScgPtpRxEdfaOutputPowerTarget_Object = MibTableColumn
xScgPtpRxEdfaOutputPowerTarget = _XScgPtpRxEdfaOutputPowerTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 13),
    _XScgPtpRxEdfaOutputPowerTarget_Type()
)
xScgPtpRxEdfaOutputPowerTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpRxEdfaOutputPowerTarget.setStatus("current")
_XScgPtpGain_Type = FloatTenths
_XScgPtpGain_Object = MibTableColumn
xScgPtpGain = _XScgPtpGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 14),
    _XScgPtpGain_Type()
)
xScgPtpGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpGain.setStatus("current")
_XScgPtpAvailableTunableSchNumbers_Type = DisplayString
_XScgPtpAvailableTunableSchNumbers_Object = MibTableColumn
xScgPtpAvailableTunableSchNumbers = _XScgPtpAvailableTunableSchNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 15),
    _XScgPtpAvailableTunableSchNumbers_Type()
)
xScgPtpAvailableTunableSchNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpAvailableTunableSchNumbers.setStatus("current")


class _XScgPtpPowerControlLoop_Type(InfnPowerControlLoop):
    """Custom type xScgPtpPowerControlLoop based on InfnPowerControlLoop"""
    defaultValue = 1


_XScgPtpPowerControlLoop_Type.__name__ = "InfnPowerControlLoop"
_XScgPtpPowerControlLoop_Object = MibTableColumn
xScgPtpPowerControlLoop = _XScgPtpPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 16),
    _XScgPtpPowerControlLoop_Type()
)
xScgPtpPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpPowerControlLoop.setStatus("current")


class _XScgPtpProvisionedEncodingMode_Type(InfnEncoding):
    """Custom type xScgPtpProvisionedEncodingMode based on InfnEncoding"""
    defaultValue = 1


_XScgPtpProvisionedEncodingMode_Type.__name__ = "InfnEncoding"
_XScgPtpProvisionedEncodingMode_Object = MibTableColumn
xScgPtpProvisionedEncodingMode = _XScgPtpProvisionedEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 17),
    _XScgPtpProvisionedEncodingMode_Type()
)
xScgPtpProvisionedEncodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpProvisionedEncodingMode.setStatus("current")


class _XScgPtpInstalledEncodingMode_Type(InfnEncoding):
    """Custom type xScgPtpInstalledEncodingMode based on InfnEncoding"""
    defaultValue = 1


_XScgPtpInstalledEncodingMode_Type.__name__ = "InfnEncoding"
_XScgPtpInstalledEncodingMode_Object = MibTableColumn
xScgPtpInstalledEncodingMode = _XScgPtpInstalledEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 18),
    _XScgPtpInstalledEncodingMode_Type()
)
xScgPtpInstalledEncodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpInstalledEncodingMode.setStatus("current")


class _XScgPtpLineSystemMode_Type(InfnLineSystemMode):
    """Custom type xScgPtpLineSystemMode based on InfnLineSystemMode"""
    defaultValue = 2


_XScgPtpLineSystemMode_Type.__name__ = "InfnLineSystemMode"
_XScgPtpLineSystemMode_Object = MibTableColumn
xScgPtpLineSystemMode = _XScgPtpLineSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 19),
    _XScgPtpLineSystemMode_Type()
)
xScgPtpLineSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpLineSystemMode.setStatus("current")
_XScgPtpTargetTxPowerOffset_Type = FloatTenths
_XScgPtpTargetTxPowerOffset_Object = MibTableColumn
xScgPtpTargetTxPowerOffset = _XScgPtpTargetTxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 20),
    _XScgPtpTargetTxPowerOffset_Type()
)
xScgPtpTargetTxPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpTargetTxPowerOffset.setStatus("current")
_XScgPtpTargetTxPower_Type = FloatTenths
_XScgPtpTargetTxPower_Object = MibTableColumn
xScgPtpTargetTxPower = _XScgPtpTargetTxPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 21),
    _XScgPtpTargetTxPower_Type()
)
xScgPtpTargetTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpTargetTxPower.setStatus("current")
_XScgPtpRxPowerOffset_Type = FloatTenths
_XScgPtpRxPowerOffset_Object = MibTableColumn
xScgPtpRxPowerOffset = _XScgPtpRxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 22),
    _XScgPtpRxPowerOffset_Type()
)
xScgPtpRxPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpRxPowerOffset.setStatus("current")
_XScgPtpProvisionedPeerTp_Type = DisplayString
_XScgPtpProvisionedPeerTp_Object = MibTableColumn
xScgPtpProvisionedPeerTp = _XScgPtpProvisionedPeerTp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 23),
    _XScgPtpProvisionedPeerTp_Type()
)
xScgPtpProvisionedPeerTp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpProvisionedPeerTp.setStatus("current")
_XScgPtpBwQmax_Type = FloatTenths
_XScgPtpBwQmax_Object = MibTableColumn
xScgPtpBwQmax = _XScgPtpBwQmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 24),
    _XScgPtpBwQmax_Type()
)
xScgPtpBwQmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBwQmax.setStatus("current")
_XScgPtpBwQused_Type = FloatTenths
_XScgPtpBwQused_Object = MibTableColumn
xScgPtpBwQused = _XScgPtpBwQused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 25),
    _XScgPtpBwQused_Type()
)
xScgPtpBwQused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBwQused.setStatus("current")
_XScgPtpBwQlicensed_Type = FloatTenths
_XScgPtpBwQlicensed_Object = MibTableColumn
xScgPtpBwQlicensed = _XScgPtpBwQlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 26),
    _XScgPtpBwQlicensed_Type()
)
xScgPtpBwQlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBwQlicensed.setStatus("current")
_XScgPtpTxPicState_Type = InfnPicStatus
_XScgPtpTxPicState_Object = MibTableColumn
xScgPtpTxPicState = _XScgPtpTxPicState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 27),
    _XScgPtpTxPicState_Type()
)
xScgPtpTxPicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpTxPicState.setStatus("current")
_XScgPtpRxPicState_Type = InfnPicStatus
_XScgPtpRxPicState_Object = MibTableColumn
xScgPtpRxPicState = _XScgPtpRxPicState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 28),
    _XScgPtpRxPicState_Type()
)
xScgPtpRxPicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpRxPicState.setStatus("current")
_XScgPtpCarrierCount_Type = FloatTenths
_XScgPtpCarrierCount_Object = MibTableColumn
xScgPtpCarrierCount = _XScgPtpCarrierCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 29),
    _XScgPtpCarrierCount_Type()
)
xScgPtpCarrierCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpCarrierCount.setStatus("current")
_XScgPtpLoopback_Type = TruthValue
_XScgPtpLoopback_Object = MibTableColumn
xScgPtpLoopback = _XScgPtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 30),
    _XScgPtpLoopback_Type()
)
xScgPtpLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpLoopback.setStatus("current")
_XScgPtpDefFlexLicModFormat_Type = InfnLicenseModulationType
_XScgPtpDefFlexLicModFormat_Object = MibTableColumn
xScgPtpDefFlexLicModFormat = _XScgPtpDefFlexLicModFormat_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 31),
    _XScgPtpDefFlexLicModFormat_Type()
)
xScgPtpDefFlexLicModFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpDefFlexLicModFormat.setStatus("current")
_XScgPtpBwUsgWaterMarkGranularity_Type = FloatTenths
_XScgPtpBwUsgWaterMarkGranularity_Object = MibTableColumn
xScgPtpBwUsgWaterMarkGranularity = _XScgPtpBwUsgWaterMarkGranularity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 32),
    _XScgPtpBwUsgWaterMarkGranularity_Type()
)
xScgPtpBwUsgWaterMarkGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBwUsgWaterMarkGranularity.setStatus("current")
_XScgPtpFECOverheadRatio_Type = InfnFECOverHeadPercent
_XScgPtpFECOverheadRatio_Object = MibTableColumn
xScgPtpFECOverheadRatio = _XScgPtpFECOverheadRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 33),
    _XScgPtpFECOverheadRatio_Type()
)
xScgPtpFECOverheadRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpFECOverheadRatio.setStatus("current")
_XScgPtpBw16Qmax_Type = FloatTenths
_XScgPtpBw16Qmax_Object = MibTableColumn
xScgPtpBw16Qmax = _XScgPtpBw16Qmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 34),
    _XScgPtpBw16Qmax_Type()
)
xScgPtpBw16Qmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBw16Qmax.setStatus("current")
_XScgPtpBw16Qused_Type = FloatTenths
_XScgPtpBw16Qused_Object = MibTableColumn
xScgPtpBw16Qused = _XScgPtpBw16Qused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 35),
    _XScgPtpBw16Qused_Type()
)
xScgPtpBw16Qused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBw16Qused.setStatus("current")
_XScgPtpBw16Qlicensed_Type = FloatTenths
_XScgPtpBw16Qlicensed_Object = MibTableColumn
xScgPtpBw16Qlicensed = _XScgPtpBw16Qlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 36),
    _XScgPtpBw16Qlicensed_Type()
)
xScgPtpBw16Qlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBw16Qlicensed.setStatus("current")
_XScgPtpBw8Qmax_Type = FloatTenths
_XScgPtpBw8Qmax_Object = MibTableColumn
xScgPtpBw8Qmax = _XScgPtpBw8Qmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 37),
    _XScgPtpBw8Qmax_Type()
)
xScgPtpBw8Qmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBw8Qmax.setStatus("current")
_XScgPtpBw8Qused_Type = FloatTenths
_XScgPtpBw8Qused_Object = MibTableColumn
xScgPtpBw8Qused = _XScgPtpBw8Qused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 38),
    _XScgPtpBw8Qused_Type()
)
xScgPtpBw8Qused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBw8Qused.setStatus("current")
_XScgPtpBw8Qlicensed_Type = FloatTenths
_XScgPtpBw8Qlicensed_Object = MibTableColumn
xScgPtpBw8Qlicensed = _XScgPtpBw8Qlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 39),
    _XScgPtpBw8Qlicensed_Type()
)
xScgPtpBw8Qlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBw8Qlicensed.setStatus("current")
_XScgPtpBw3Qmax_Type = FloatTenths
_XScgPtpBw3Qmax_Object = MibTableColumn
xScgPtpBw3Qmax = _XScgPtpBw3Qmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 40),
    _XScgPtpBw3Qmax_Type()
)
xScgPtpBw3Qmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBw3Qmax.setStatus("current")
_XScgPtpBw3Qused_Type = FloatTenths
_XScgPtpBw3Qused_Object = MibTableColumn
xScgPtpBw3Qused = _XScgPtpBw3Qused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 41),
    _XScgPtpBw3Qused_Type()
)
xScgPtpBw3Qused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBw3Qused.setStatus("current")
_XScgPtpBw3Qlicensed_Type = FloatTenths
_XScgPtpBw3Qlicensed_Object = MibTableColumn
xScgPtpBw3Qlicensed = _XScgPtpBw3Qlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 42),
    _XScgPtpBw3Qlicensed_Type()
)
xScgPtpBw3Qlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBw3Qlicensed.setStatus("current")
_XScgPtpBwBmax_Type = FloatTenths
_XScgPtpBwBmax_Object = MibTableColumn
xScgPtpBwBmax = _XScgPtpBwBmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 43),
    _XScgPtpBwBmax_Type()
)
xScgPtpBwBmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBwBmax.setStatus("current")
_XScgPtpBwBused_Type = FloatTenths
_XScgPtpBwBused_Object = MibTableColumn
xScgPtpBwBused = _XScgPtpBwBused_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 44),
    _XScgPtpBwBused_Type()
)
xScgPtpBwBused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBwBused.setStatus("current")
_XScgPtpBwBlicensed_Type = FloatTenths
_XScgPtpBwBlicensed_Object = MibTableColumn
xScgPtpBwBlicensed = _XScgPtpBwBlicensed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 45),
    _XScgPtpBwBlicensed_Type()
)
xScgPtpBwBlicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpBwBlicensed.setStatus("current")
_XScgPtpUnAssignedCarrierList_Type = DisplayString
_XScgPtpUnAssignedCarrierList_Object = MibTableColumn
xScgPtpUnAssignedCarrierList = _XScgPtpUnAssignedCarrierList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 46),
    _XScgPtpUnAssignedCarrierList_Type()
)
xScgPtpUnAssignedCarrierList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpUnAssignedCarrierList.setStatus("current")
_XScgPtpInstalledFECOHRatio_Type = InfnFECOverHeadPercent
_XScgPtpInstalledFECOHRatio_Object = MibTableColumn
xScgPtpInstalledFECOHRatio = _XScgPtpInstalledFECOHRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 47),
    _XScgPtpInstalledFECOHRatio_Type()
)
xScgPtpInstalledFECOHRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpInstalledFECOHRatio.setStatus("current")
_XScgPtpRxPCLOprMode_Type = InfnPCLOperatingMode
_XScgPtpRxPCLOprMode_Object = MibTableColumn
xScgPtpRxPCLOprMode = _XScgPtpRxPCLOprMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 48),
    _XScgPtpRxPCLOprMode_Type()
)
xScgPtpRxPCLOprMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpRxPCLOprMode.setStatus("current")
_XScgPtpInstalledRxPCLOprMode_Type = InfnPCLOperatingMode
_XScgPtpInstalledRxPCLOprMode_Object = MibTableColumn
xScgPtpInstalledRxPCLOprMode = _XScgPtpInstalledRxPCLOprMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 49),
    _XScgPtpInstalledRxPCLOprMode_Type()
)
xScgPtpInstalledRxPCLOprMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpInstalledRxPCLOprMode.setStatus("current")
_XScgPtpCarrierCount33Gbaud_Type = FloatArbitraryPrecision
_XScgPtpCarrierCount33Gbaud_Object = MibTableColumn
xScgPtpCarrierCount33Gbaud = _XScgPtpCarrierCount33Gbaud_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 50),
    _XScgPtpCarrierCount33Gbaud_Type()
)
xScgPtpCarrierCount33Gbaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpCarrierCount33Gbaud.setStatus("current")
_XScgPtpCarrierCount22Gbaud_Type = FloatArbitraryPrecision
_XScgPtpCarrierCount22Gbaud_Object = MibTableColumn
xScgPtpCarrierCount22Gbaud = _XScgPtpCarrierCount22Gbaud_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 51),
    _XScgPtpCarrierCount22Gbaud_Type()
)
xScgPtpCarrierCount22Gbaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpCarrierCount22Gbaud.setStatus("current")
_XScgPtpCarrierCount17Gbaud_Type = FloatArbitraryPrecision
_XScgPtpCarrierCount17Gbaud_Object = MibTableColumn
xScgPtpCarrierCount17Gbaud = _XScgPtpCarrierCount17Gbaud_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 52),
    _XScgPtpCarrierCount17Gbaud_Type()
)
xScgPtpCarrierCount17Gbaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpCarrierCount17Gbaud.setStatus("current")
_XScgPtpOpticalSignal_Type = InfnOpticalSignal
_XScgPtpOpticalSignal_Object = MibTableColumn
xScgPtpOpticalSignal = _XScgPtpOpticalSignal_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 53),
    _XScgPtpOpticalSignal_Type()
)
xScgPtpOpticalSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpOpticalSignal.setStatus("current")
_XScgPtpOpticalSignalStatus_Type = InfnOpticalSignalStatus
_XScgPtpOpticalSignalStatus_Object = MibTableColumn
xScgPtpOpticalSignalStatus = _XScgPtpOpticalSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 54),
    _XScgPtpOpticalSignalStatus_Type()
)
xScgPtpOpticalSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpOpticalSignalStatus.setStatus("current")
_XScgPtpPerCarrierTargetTxPower_Type = FloatArbitraryPrecision
_XScgPtpPerCarrierTargetTxPower_Object = MibTableColumn
xScgPtpPerCarrierTargetTxPower = _XScgPtpPerCarrierTargetTxPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 55),
    _XScgPtpPerCarrierTargetTxPower_Type()
)
xScgPtpPerCarrierTargetTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xScgPtpPerCarrierTargetTxPower.setStatus("current")
_XScgPtpExpTotalTxPower_Type = FloatArbitraryPrecision
_XScgPtpExpTotalTxPower_Object = MibTableColumn
xScgPtpExpTotalTxPower = _XScgPtpExpTotalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 1, 1, 56),
    _XScgPtpExpTotalTxPower_Type()
)
xScgPtpExpTotalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpExpTotalTxPower.setStatus("current")
_XScgPtpConformance_ObjectIdentity = ObjectIdentity
xScgPtpConformance = _XScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 3)
)
_XScgPtpCompliances_ObjectIdentity = ObjectIdentity
xScgPtpCompliances = _XScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 3, 1)
)
_XScgPtpGroups_ObjectIdentity = ObjectIdentity
xScgPtpGroups = _XScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 3, 2)
)

# Managed Objects groups

xScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 3, 2, 1)
)
xScgPtpGroup.setObjects(
      *(("INFINERA-TP-XSCGPTP-MIB", "xScgPtpOpenwaveTargetTxScgPower"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpMPOAID"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpProvisionedFPMPO"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpAutoDiscoveryState"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpDiscoveredNeighborTP"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpProvisionedNeighborTP"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpProvisionedNeighborAdTpType"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpInterfaceType"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpProvisionedOpenWaveRemotePtp"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpPmHistStatsEnable"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpMaxFruGain"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpRecommendedGain"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpRxEdfaOutputPowerTarget"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpGain"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpAvailableTunableSchNumbers"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpPowerControlLoop"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpProvisionedEncodingMode"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpInstalledEncodingMode"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpLineSystemMode"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpTargetTxPowerOffset"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpTargetTxPower"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpRxPowerOffset"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpProvisionedPeerTp"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBwQmax"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBwQused"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBwQlicensed"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpTxPicState"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpRxPicState"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpCarrierCount"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpLoopback"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpDefFlexLicModFormat"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBwUsgWaterMarkGranularity"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpFECOverheadRatio"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBw16Qmax"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBw16Qused"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBw16Qlicensed"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBw8Qmax"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBw8Qused"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBw8Qlicensed"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBw3Qmax"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBw3Qused"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBw3Qlicensed"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBwBmax"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBwBused"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpBwBlicensed"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpUnAssignedCarrierList"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpInstalledFECOHRatio"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpRxPCLOprMode"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpCarrierCount33Gbaud"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpCarrierCount22Gbaud"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpCarrierCount17Gbaud"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpOpticalSignal"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpOpticalSignalStatus"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpInstalledRxPCLOprMode"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpPerCarrierTargetTxPower"),
        ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpExpTotalTxPower"))
)
if mibBuilder.loadTexts:
    xScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 57, 3, 1, 1)
)
xScgPtpCompliance.setObjects(
    ("INFINERA-TP-XSCGPTP-MIB", "xScgPtpGroup")
)
if mibBuilder.loadTexts:
    xScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-XSCGPTP-MIB",
    **{"xScgPtpMIB": xScgPtpMIB,
       "xScgPtpTable": xScgPtpTable,
       "xScgPtpEntry": xScgPtpEntry,
       "xScgPtpOpenwaveTargetTxScgPower": xScgPtpOpenwaveTargetTxScgPower,
       "xScgPtpMPOAID": xScgPtpMPOAID,
       "xScgPtpProvisionedFPMPO": xScgPtpProvisionedFPMPO,
       "xScgPtpAutoDiscoveryState": xScgPtpAutoDiscoveryState,
       "xScgPtpDiscoveredNeighborTP": xScgPtpDiscoveredNeighborTP,
       "xScgPtpProvisionedNeighborTP": xScgPtpProvisionedNeighborTP,
       "xScgPtpProvisionedNeighborAdTpType": xScgPtpProvisionedNeighborAdTpType,
       "xScgPtpInterfaceType": xScgPtpInterfaceType,
       "xScgPtpProvisionedOpenWaveRemotePtp": xScgPtpProvisionedOpenWaveRemotePtp,
       "xScgPtpPmHistStatsEnable": xScgPtpPmHistStatsEnable,
       "xScgPtpMaxFruGain": xScgPtpMaxFruGain,
       "xScgPtpRecommendedGain": xScgPtpRecommendedGain,
       "xScgPtpRxEdfaOutputPowerTarget": xScgPtpRxEdfaOutputPowerTarget,
       "xScgPtpGain": xScgPtpGain,
       "xScgPtpAvailableTunableSchNumbers": xScgPtpAvailableTunableSchNumbers,
       "xScgPtpPowerControlLoop": xScgPtpPowerControlLoop,
       "xScgPtpProvisionedEncodingMode": xScgPtpProvisionedEncodingMode,
       "xScgPtpInstalledEncodingMode": xScgPtpInstalledEncodingMode,
       "xScgPtpLineSystemMode": xScgPtpLineSystemMode,
       "xScgPtpTargetTxPowerOffset": xScgPtpTargetTxPowerOffset,
       "xScgPtpTargetTxPower": xScgPtpTargetTxPower,
       "xScgPtpRxPowerOffset": xScgPtpRxPowerOffset,
       "xScgPtpProvisionedPeerTp": xScgPtpProvisionedPeerTp,
       "xScgPtpBwQmax": xScgPtpBwQmax,
       "xScgPtpBwQused": xScgPtpBwQused,
       "xScgPtpBwQlicensed": xScgPtpBwQlicensed,
       "xScgPtpTxPicState": xScgPtpTxPicState,
       "xScgPtpRxPicState": xScgPtpRxPicState,
       "xScgPtpCarrierCount": xScgPtpCarrierCount,
       "xScgPtpLoopback": xScgPtpLoopback,
       "xScgPtpDefFlexLicModFormat": xScgPtpDefFlexLicModFormat,
       "xScgPtpBwUsgWaterMarkGranularity": xScgPtpBwUsgWaterMarkGranularity,
       "xScgPtpFECOverheadRatio": xScgPtpFECOverheadRatio,
       "xScgPtpBw16Qmax": xScgPtpBw16Qmax,
       "xScgPtpBw16Qused": xScgPtpBw16Qused,
       "xScgPtpBw16Qlicensed": xScgPtpBw16Qlicensed,
       "xScgPtpBw8Qmax": xScgPtpBw8Qmax,
       "xScgPtpBw8Qused": xScgPtpBw8Qused,
       "xScgPtpBw8Qlicensed": xScgPtpBw8Qlicensed,
       "xScgPtpBw3Qmax": xScgPtpBw3Qmax,
       "xScgPtpBw3Qused": xScgPtpBw3Qused,
       "xScgPtpBw3Qlicensed": xScgPtpBw3Qlicensed,
       "xScgPtpBwBmax": xScgPtpBwBmax,
       "xScgPtpBwBused": xScgPtpBwBused,
       "xScgPtpBwBlicensed": xScgPtpBwBlicensed,
       "xScgPtpUnAssignedCarrierList": xScgPtpUnAssignedCarrierList,
       "xScgPtpInstalledFECOHRatio": xScgPtpInstalledFECOHRatio,
       "xScgPtpRxPCLOprMode": xScgPtpRxPCLOprMode,
       "xScgPtpInstalledRxPCLOprMode": xScgPtpInstalledRxPCLOprMode,
       "xScgPtpCarrierCount33Gbaud": xScgPtpCarrierCount33Gbaud,
       "xScgPtpCarrierCount22Gbaud": xScgPtpCarrierCount22Gbaud,
       "xScgPtpCarrierCount17Gbaud": xScgPtpCarrierCount17Gbaud,
       "xScgPtpOpticalSignal": xScgPtpOpticalSignal,
       "xScgPtpOpticalSignalStatus": xScgPtpOpticalSignalStatus,
       "xScgPtpPerCarrierTargetTxPower": xScgPtpPerCarrierTargetTxPower,
       "xScgPtpExpTotalTxPower": xScgPtpExpTotalTxPower,
       "xScgPtpConformance": xScgPtpConformance,
       "xScgPtpCompliances": xScgPtpCompliances,
       "xScgPtpCompliance": xScgPtpCompliance,
       "xScgPtpGroups": xScgPtpGroups,
       "xScgPtpGroup": xScgPtpGroup}
)
