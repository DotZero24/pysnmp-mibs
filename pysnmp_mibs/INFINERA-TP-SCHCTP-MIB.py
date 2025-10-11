# SNMP MIB module (INFINERA-TP-SCHCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-SCHCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:01 2025
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
 InfnCarrierType,
 InfnChannelPlanType,
 InfnEnableDisable,
 InfnEncoding,
 InfnFrequencySlotPlanType,
 InfnModulation,
 InfnMonitoringMode,
 InfnOpticalRate,
 InfnOpticalSignal,
 InfnProvBaudRate,
 InfnReporting,
 InfnShutterState,
 InfnSuperChannelNumber,
 InfnTimReptMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths",
    "FloatTenths",
    "InfnCarrierType",
    "InfnChannelPlanType",
    "InfnEnableDisable",
    "InfnEncoding",
    "InfnFrequencySlotPlanType",
    "InfnModulation",
    "InfnMonitoringMode",
    "InfnOpticalRate",
    "InfnOpticalSignal",
    "InfnProvBaudRate",
    "InfnReporting",
    "InfnShutterState",
    "InfnSuperChannelNumber",
    "InfnTimReptMode")

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

schCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50)
)
if mibBuilder.loadTexts:
    schCtpMIB.setRevisions(
        ("2013-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SchCtpTable_Object = MibTable
schCtpTable = _SchCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1)
)
if mibBuilder.loadTexts:
    schCtpTable.setStatus("current")
_SchCtpEntry_Object = MibTableRow
schCtpEntry = _SchCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1)
)
schCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    schCtpEntry.setStatus("current")
_SchCtpCarrierGroupMode_Type = InfnCarrierType
_SchCtpCarrierGroupMode_Object = MibTableColumn
schCtpCarrierGroupMode = _SchCtpCarrierGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 1),
    _SchCtpCarrierGroupMode_Type()
)
schCtpCarrierGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpCarrierGroupMode.setStatus("current")
_SchCtpAssociatedClientSCHCTP_Type = DisplayString
_SchCtpAssociatedClientSCHCTP_Object = MibTableColumn
schCtpAssociatedClientSCHCTP = _SchCtpAssociatedClientSCHCTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 2),
    _SchCtpAssociatedClientSCHCTP_Type()
)
schCtpAssociatedClientSCHCTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpAssociatedClientSCHCTP.setStatus("current")


class _SchCtpPmHistStatsEnable_Type(Integer32):
    """Custom type schCtpPmHistStatsEnable based on Integer32"""
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


_SchCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_SchCtpPmHistStatsEnable_Object = MibTableColumn
schCtpPmHistStatsEnable = _SchCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 3),
    _SchCtpPmHistStatsEnable_Type()
)
schCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpPmHistStatsEnable.setStatus("current")
_SchCtpProvSuperChannelNum_Type = InfnSuperChannelNumber
_SchCtpProvSuperChannelNum_Object = MibTableColumn
schCtpProvSuperChannelNum = _SchCtpProvSuperChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 4),
    _SchCtpProvSuperChannelNum_Type()
)
schCtpProvSuperChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpProvSuperChannelNum.setStatus("current")
_SchCtpProvModulation_Type = InfnModulation
_SchCtpProvModulation_Object = MibTableColumn
schCtpProvModulation = _SchCtpProvModulation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 5),
    _SchCtpProvModulation_Type()
)
schCtpProvModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpProvModulation.setStatus("current")
_SchCtpProvEncoding_Type = InfnEncoding
_SchCtpProvEncoding_Object = MibTableColumn
schCtpProvEncoding = _SchCtpProvEncoding_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 6),
    _SchCtpProvEncoding_Type()
)
schCtpProvEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpProvEncoding.setStatus("current")
_SchCtpSpectralBandWidth_Type = Integer32
_SchCtpSpectralBandWidth_Object = MibTableColumn
schCtpSpectralBandWidth = _SchCtpSpectralBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 7),
    _SchCtpSpectralBandWidth_Type()
)
schCtpSpectralBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpSpectralBandWidth.setStatus("current")
_SchCtpAggregrateRate_Type = InfnOpticalRate
_SchCtpAggregrateRate_Object = MibTableColumn
schCtpAggregrateRate = _SchCtpAggregrateRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 8),
    _SchCtpAggregrateRate_Type()
)
schCtpAggregrateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpAggregrateRate.setStatus("current")
_SchCtpChannelPlanType_Type = InfnChannelPlanType
_SchCtpChannelPlanType_Object = MibTableColumn
schCtpChannelPlanType = _SchCtpChannelPlanType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 9),
    _SchCtpChannelPlanType_Type()
)
schCtpChannelPlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpChannelPlanType.setStatus("current")
_SchCtpFrequencySlotPlanType_Type = InfnFrequencySlotPlanType
_SchCtpFrequencySlotPlanType_Object = MibTableColumn
schCtpFrequencySlotPlanType = _SchCtpFrequencySlotPlanType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 10),
    _SchCtpFrequencySlotPlanType_Type()
)
schCtpFrequencySlotPlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schCtpFrequencySlotPlanType.setStatus("current")
_SchCtpInstalledSuperChannelNum_Type = InfnSuperChannelNumber
_SchCtpInstalledSuperChannelNum_Object = MibTableColumn
schCtpInstalledSuperChannelNum = _SchCtpInstalledSuperChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 11),
    _SchCtpInstalledSuperChannelNum_Type()
)
schCtpInstalledSuperChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpInstalledSuperChannelNum.setStatus("current")
_SchCtpInstalledModulation_Type = InfnModulation
_SchCtpInstalledModulation_Object = MibTableColumn
schCtpInstalledModulation = _SchCtpInstalledModulation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 12),
    _SchCtpInstalledModulation_Type()
)
schCtpInstalledModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpInstalledModulation.setStatus("current")
_SchCtpInstalledEncoding_Type = InfnEncoding
_SchCtpInstalledEncoding_Object = MibTableColumn
schCtpInstalledEncoding = _SchCtpInstalledEncoding_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 13),
    _SchCtpInstalledEncoding_Type()
)
schCtpInstalledEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpInstalledEncoding.setStatus("current")
_SchCtpOffset_Type = FloatHundredths
_SchCtpOffset_Object = MibTableColumn
schCtpOffset = _SchCtpOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 14),
    _SchCtpOffset_Type()
)
schCtpOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpOffset.setStatus("current")
_SchCtpOffsetOverride_Type = InfnEnableDisable
_SchCtpOffsetOverride_Object = MibTableColumn
schCtpOffsetOverride = _SchCtpOffsetOverride_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 15),
    _SchCtpOffsetOverride_Type()
)
schCtpOffsetOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpOffsetOverride.setStatus("current")
_SchCtpPowerOffset_Type = FloatArbitraryPrecision
_SchCtpPowerOffset_Object = MibTableColumn
schCtpPowerOffset = _SchCtpPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 16),
    _SchCtpPowerOffset_Type()
)
schCtpPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpPowerOffset.setStatus("current")
_SchCtpSupportingCircuitIdList_Type = DisplayString
_SchCtpSupportingCircuitIdList_Object = MibTableColumn
schCtpSupportingCircuitIdList = _SchCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 17),
    _SchCtpSupportingCircuitIdList_Type()
)
schCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpSupportingCircuitIdList.setStatus("current")
_SchCtpExpectedTTI_Type = DisplayString
_SchCtpExpectedTTI_Object = MibTableColumn
schCtpExpectedTTI = _SchCtpExpectedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 18),
    _SchCtpExpectedTTI_Type()
)
schCtpExpectedTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpExpectedTTI.setStatus("current")
_SchCtpTransmitTTI_Type = DisplayString
_SchCtpTransmitTTI_Object = MibTableColumn
schCtpTransmitTTI = _SchCtpTransmitTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 19),
    _SchCtpTransmitTTI_Type()
)
schCtpTransmitTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpTransmitTTI.setStatus("current")
_SchCtpRecievedTTI_Type = DisplayString
_SchCtpRecievedTTI_Object = MibTableColumn
schCtpRecievedTTI = _SchCtpRecievedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 20),
    _SchCtpRecievedTTI_Type()
)
schCtpRecievedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpRecievedTTI.setStatus("current")
_SchCtpMonitoringMode_Type = InfnMonitoringMode
_SchCtpMonitoringMode_Object = MibTableColumn
schCtpMonitoringMode = _SchCtpMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 21),
    _SchCtpMonitoringMode_Type()
)
schCtpMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpMonitoringMode.setStatus("current")
_SchCtpTargetOpr_Type = FloatTenths
_SchCtpTargetOpr_Object = MibTableColumn
schCtpTargetOpr = _SchCtpTargetOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 22),
    _SchCtpTargetOpr_Type()
)
schCtpTargetOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpTargetOpr.setStatus("current")
_SchCtpIntraSchCarrierRippleThreshold_Type = FloatTenths
_SchCtpIntraSchCarrierRippleThreshold_Object = MibTableColumn
schCtpIntraSchCarrierRippleThreshold = _SchCtpIntraSchCarrierRippleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 23),
    _SchCtpIntraSchCarrierRippleThreshold_Type()
)
schCtpIntraSchCarrierRippleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpIntraSchCarrierRippleThreshold.setStatus("current")
_SchCtpShutterState_Type = InfnShutterState
_SchCtpShutterState_Object = MibTableColumn
schCtpShutterState = _SchCtpShutterState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 24),
    _SchCtpShutterState_Type()
)
schCtpShutterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpShutterState.setStatus("current")
_SchCtpIntraSchCarRipple_Type = InfnReporting
_SchCtpIntraSchCarRipple_Object = MibTableColumn
schCtpIntraSchCarRipple = _SchCtpIntraSchCarRipple_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 25),
    _SchCtpIntraSchCarRipple_Type()
)
schCtpIntraSchCarRipple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpIntraSchCarRipple.setStatus("current")
_SchCtpFreqSlotList_Type = DisplayString
_SchCtpFreqSlotList_Object = MibTableColumn
schCtpFreqSlotList = _SchCtpFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 26),
    _SchCtpFreqSlotList_Type()
)
schCtpFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpFreqSlotList.setStatus("current")
_SchCtpSupportingCarrierList_Type = DisplayString
_SchCtpSupportingCarrierList_Object = MibTableColumn
schCtpSupportingCarrierList = _SchCtpSupportingCarrierList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 27),
    _SchCtpSupportingCarrierList_Type()
)
schCtpSupportingCarrierList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpSupportingCarrierList.setStatus("current")
_SchCtpProvBaudRate_Type = InfnProvBaudRate
_SchCtpProvBaudRate_Object = MibTableColumn
schCtpProvBaudRate = _SchCtpProvBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 28),
    _SchCtpProvBaudRate_Type()
)
schCtpProvBaudRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schCtpProvBaudRate.setStatus("current")
_SchCtpSupportingCarrGrpList_Type = DisplayString
_SchCtpSupportingCarrGrpList_Object = MibTableColumn
schCtpSupportingCarrGrpList = _SchCtpSupportingCarrGrpList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 29),
    _SchCtpSupportingCarrGrpList_Type()
)
schCtpSupportingCarrGrpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpSupportingCarrGrpList.setStatus("current")
_SchCtpOpticalSignal_Type = InfnOpticalSignal
_SchCtpOpticalSignal_Object = MibTableColumn
schCtpOpticalSignal = _SchCtpOpticalSignal_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 30),
    _SchCtpOpticalSignal_Type()
)
schCtpOpticalSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpOpticalSignal.setStatus("current")
_SchCtpAssocTeIntfList_Type = DisplayString
_SchCtpAssocTeIntfList_Object = MibTableColumn
schCtpAssocTeIntfList = _SchCtpAssocTeIntfList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 31),
    _SchCtpAssocTeIntfList_Type()
)
schCtpAssocTeIntfList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpAssocTeIntfList.setStatus("current")
_SchCtpRxSchPowerOffset_Type = FloatArbitraryPrecision
_SchCtpRxSchPowerOffset_Object = MibTableColumn
schCtpRxSchPowerOffset = _SchCtpRxSchPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 32),
    _SchCtpRxSchPowerOffset_Type()
)
schCtpRxSchPowerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpRxSchPowerOffset.setStatus("current")
_SchCtpFlexOptChnlList_Type = DisplayString
_SchCtpFlexOptChnlList_Object = MibTableColumn
schCtpFlexOptChnlList = _SchCtpFlexOptChnlList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 33),
    _SchCtpFlexOptChnlList_Type()
)
schCtpFlexOptChnlList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpFlexOptChnlList.setStatus("current")
_SchCtpCarrierList_Type = DisplayString
_SchCtpCarrierList_Object = MibTableColumn
schCtpCarrierList = _SchCtpCarrierList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 34),
    _SchCtpCarrierList_Type()
)
schCtpCarrierList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpCarrierList.setStatus("current")
_SchCtpPassBandList_Type = DisplayString
_SchCtpPassBandList_Object = MibTableColumn
schCtpPassBandList = _SchCtpPassBandList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 35),
    _SchCtpPassBandList_Type()
)
schCtpPassBandList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpPassBandList.setStatus("current")
_SchCtpPassBandStatusList_Type = DisplayString
_SchCtpPassBandStatusList_Object = MibTableColumn
schCtpPassBandStatusList = _SchCtpPassBandStatusList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 1, 1, 36),
    _SchCtpPassBandStatusList_Type()
)
schCtpPassBandStatusList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schCtpPassBandStatusList.setStatus("current")
_SchCtpConformance_ObjectIdentity = ObjectIdentity
schCtpConformance = _SchCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 3)
)
_SchCtpCompliances_ObjectIdentity = ObjectIdentity
schCtpCompliances = _SchCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 3, 1)
)
_SchCtpGroups_ObjectIdentity = ObjectIdentity
schCtpGroups = _SchCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 3, 2)
)

# Managed Objects groups

schCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 3, 2, 1)
)
schCtpGroup.setObjects(
      *(("INFINERA-TP-SCHCTP-MIB", "schCtpPmHistStatsEnable"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpProvSuperChannelNum"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpProvModulation"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpProvEncoding"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpSpectralBandWidth"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpAggregrateRate"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpCarrierGroupMode"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpInstalledModulation"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpInstalledEncoding"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpChannelPlanType"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpFrequencySlotPlanType"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpInstalledSuperChannelNum"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpOffset"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpOffsetOverride"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpSupportingCircuitIdList"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpAssociatedClientSCHCTP"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpPowerOffset"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpExpectedTTI"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpTransmitTTI"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpRecievedTTI"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpMonitoringMode"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpTargetOpr"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpIntraSchCarrierRippleThreshold"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpShutterState"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpIntraSchCarRipple"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpFreqSlotList"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpSupportingCarrierList"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpProvBaudRate"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpSupportingCarrGrpList"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpProvBaudRate"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpOpticalSignal"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpAssocTeIntfList"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpRxSchPowerOffset"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpFlexOptChnlList"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpCarrierList"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpPassBandList"),
        ("INFINERA-TP-SCHCTP-MIB", "schCtpPassBandStatusList"))
)
if mibBuilder.loadTexts:
    schCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

schCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 50, 3, 1, 1)
)
schCtpCompliance.setObjects(
    ("INFINERA-TP-SCHCTP-MIB", "schCtpGroup")
)
if mibBuilder.loadTexts:
    schCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-SCHCTP-MIB",
    **{"schCtpMIB": schCtpMIB,
       "schCtpTable": schCtpTable,
       "schCtpEntry": schCtpEntry,
       "schCtpCarrierGroupMode": schCtpCarrierGroupMode,
       "schCtpAssociatedClientSCHCTP": schCtpAssociatedClientSCHCTP,
       "schCtpPmHistStatsEnable": schCtpPmHistStatsEnable,
       "schCtpProvSuperChannelNum": schCtpProvSuperChannelNum,
       "schCtpProvModulation": schCtpProvModulation,
       "schCtpProvEncoding": schCtpProvEncoding,
       "schCtpSpectralBandWidth": schCtpSpectralBandWidth,
       "schCtpAggregrateRate": schCtpAggregrateRate,
       "schCtpChannelPlanType": schCtpChannelPlanType,
       "schCtpFrequencySlotPlanType": schCtpFrequencySlotPlanType,
       "schCtpInstalledSuperChannelNum": schCtpInstalledSuperChannelNum,
       "schCtpInstalledModulation": schCtpInstalledModulation,
       "schCtpInstalledEncoding": schCtpInstalledEncoding,
       "schCtpOffset": schCtpOffset,
       "schCtpOffsetOverride": schCtpOffsetOverride,
       "schCtpPowerOffset": schCtpPowerOffset,
       "schCtpSupportingCircuitIdList": schCtpSupportingCircuitIdList,
       "schCtpExpectedTTI": schCtpExpectedTTI,
       "schCtpTransmitTTI": schCtpTransmitTTI,
       "schCtpRecievedTTI": schCtpRecievedTTI,
       "schCtpMonitoringMode": schCtpMonitoringMode,
       "schCtpTargetOpr": schCtpTargetOpr,
       "schCtpIntraSchCarrierRippleThreshold": schCtpIntraSchCarrierRippleThreshold,
       "schCtpShutterState": schCtpShutterState,
       "schCtpIntraSchCarRipple": schCtpIntraSchCarRipple,
       "schCtpFreqSlotList": schCtpFreqSlotList,
       "schCtpSupportingCarrierList": schCtpSupportingCarrierList,
       "schCtpProvBaudRate": schCtpProvBaudRate,
       "schCtpSupportingCarrGrpList": schCtpSupportingCarrGrpList,
       "schCtpOpticalSignal": schCtpOpticalSignal,
       "schCtpAssocTeIntfList": schCtpAssocTeIntfList,
       "schCtpRxSchPowerOffset": schCtpRxSchPowerOffset,
       "schCtpFlexOptChnlList": schCtpFlexOptChnlList,
       "schCtpCarrierList": schCtpCarrierList,
       "schCtpPassBandList": schCtpPassBandList,
       "schCtpPassBandStatusList": schCtpPassBandStatusList,
       "schCtpConformance": schCtpConformance,
       "schCtpCompliances": schCtpCompliances,
       "schCtpCompliance": schCtpCompliance,
       "schCtpGroups": schCtpGroups,
       "schCtpGroup": schCtpGroup}
)
