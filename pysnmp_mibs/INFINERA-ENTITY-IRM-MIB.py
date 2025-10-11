# SNMP MIB module (INFINERA-ENTITY-IRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-IRM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:43 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatArbitraryPrecision,
 FloatHundredths,
 InfnALSDetectionMode,
 InfnALSDisableMode,
 InfnDeploymentConfig,
 InfnEnableDisable,
 InfnEqptType,
 InfnFiberType,
 InfnOAOperatingMode,
 InfnOlosSoakTime) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths",
    "InfnALSDetectionMode",
    "InfnALSDisableMode",
    "InfnDeploymentConfig",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnFiberType",
    "InfnOAOperatingMode",
    "InfnOlosSoakTime")

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

irmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IrmTable_Object = MibTable
irmTable = _IrmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1)
)
if mibBuilder.loadTexts:
    irmTable.setStatus("current")
_IrmEntry_Object = MibTableRow
irmEntry = _IrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1)
)
irmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    irmEntry.setStatus("current")
_IrmMoId_Type = DisplayString
_IrmMoId_Object = MibTableColumn
irmMoId = _IrmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 1),
    _IrmMoId_Type()
)
irmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmMoId.setStatus("current")
_IrmProvEqptType_Type = InfnEqptType
_IrmProvEqptType_Object = MibTableColumn
irmProvEqptType = _IrmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 2),
    _IrmProvEqptType_Type()
)
irmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmProvEqptType.setStatus("current")
_IrmPointLossOffset_Type = FloatHundredths
_IrmPointLossOffset_Object = MibTableColumn
irmPointLossOffset = _IrmPointLossOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 3),
    _IrmPointLossOffset_Type()
)
irmPointLossOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmPointLossOffset.setStatus("current")
_IrmLaunchPowerOffset_Type = FloatHundredths
_IrmLaunchPowerOffset_Object = MibTableColumn
irmLaunchPowerOffset = _IrmLaunchPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 4),
    _IrmLaunchPowerOffset_Type()
)
irmLaunchPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmLaunchPowerOffset.setStatus("current")
_IrmRxDampSeqNum_Type = Integer32
_IrmRxDampSeqNum_Object = MibTableColumn
irmRxDampSeqNum = _IrmRxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 5),
    _IrmRxDampSeqNum_Type()
)
irmRxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irmRxDampSeqNum.setStatus("current")
_IrmTxDampSeqNum_Type = Integer32
_IrmTxDampSeqNum_Object = MibTableColumn
irmTxDampSeqNum = _IrmTxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 6),
    _IrmTxDampSeqNum_Type()
)
irmTxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irmTxDampSeqNum.setStatus("current")
_IrmPilotLaserDisable_Type = TruthValue
_IrmPilotLaserDisable_Object = MibTableColumn
irmPilotLaserDisable = _IrmPilotLaserDisable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 7),
    _IrmPilotLaserDisable_Type()
)
irmPilotLaserDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmPilotLaserDisable.setStatus("current")
_IrmEnhPMRept_Type = InfnEnableDisable
_IrmEnhPMRept_Object = MibTableColumn
irmEnhPMRept = _IrmEnhPMRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 8),
    _IrmEnhPMRept_Type()
)
irmEnhPMRept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmEnhPMRept.setStatus("current")
_IrmALSDetectionMode_Type = InfnALSDetectionMode
_IrmALSDetectionMode_Object = MibTableColumn
irmALSDetectionMode = _IrmALSDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 9),
    _IrmALSDetectionMode_Type()
)
irmALSDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmALSDetectionMode.setStatus("current")
_IrmAutomaticPLOAdjustmen_Type = InfnEnableDisable
_IrmAutomaticPLOAdjustmen_Object = MibTableColumn
irmAutomaticPLOAdjustmen = _IrmAutomaticPLOAdjustmen_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 10),
    _IrmAutomaticPLOAdjustmen_Type()
)
irmAutomaticPLOAdjustmen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmAutomaticPLOAdjustmen.setStatus("current")
_IrmAsePowerBetaCoeffX_Type = FloatHundredths
_IrmAsePowerBetaCoeffX_Object = MibTableColumn
irmAsePowerBetaCoeffX = _IrmAsePowerBetaCoeffX_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 11),
    _IrmAsePowerBetaCoeffX_Type()
)
irmAsePowerBetaCoeffX.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmAsePowerBetaCoeffX.setStatus("current")
_IrmAsePowerBetaCoeffY_Type = FloatHundredths
_IrmAsePowerBetaCoeffY_Object = MibTableColumn
irmAsePowerBetaCoeffY = _IrmAsePowerBetaCoeffY_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 12),
    _IrmAsePowerBetaCoeffY_Type()
)
irmAsePowerBetaCoeffY.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmAsePowerBetaCoeffY.setStatus("current")
_IrmAsePowerBetaCoeffZ_Type = FloatHundredths
_IrmAsePowerBetaCoeffZ_Object = MibTableColumn
irmAsePowerBetaCoeffZ = _IrmAsePowerBetaCoeffZ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 13),
    _IrmAsePowerBetaCoeffZ_Type()
)
irmAsePowerBetaCoeffZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmAsePowerBetaCoeffZ.setStatus("current")
_IrmPumpPowerBetaCoeffX_Type = FloatHundredths
_IrmPumpPowerBetaCoeffX_Object = MibTableColumn
irmPumpPowerBetaCoeffX = _IrmPumpPowerBetaCoeffX_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 14),
    _IrmPumpPowerBetaCoeffX_Type()
)
irmPumpPowerBetaCoeffX.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmPumpPowerBetaCoeffX.setStatus("current")
_IrmPumpPowerBetaCoeffY_Type = FloatHundredths
_IrmPumpPowerBetaCoeffY_Object = MibTableColumn
irmPumpPowerBetaCoeffY = _IrmPumpPowerBetaCoeffY_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 15),
    _IrmPumpPowerBetaCoeffY_Type()
)
irmPumpPowerBetaCoeffY.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmPumpPowerBetaCoeffY.setStatus("current")
_IrmPumpPowerBetaCoeffZ_Type = FloatHundredths
_IrmPumpPowerBetaCoeffZ_Object = MibTableColumn
irmPumpPowerBetaCoeffZ = _IrmPumpPowerBetaCoeffZ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 16),
    _IrmPumpPowerBetaCoeffZ_Type()
)
irmPumpPowerBetaCoeffZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmPumpPowerBetaCoeffZ.setStatus("current")
_IrmPumpRatioPump1_Type = FloatHundredths
_IrmPumpRatioPump1_Object = MibTableColumn
irmPumpRatioPump1 = _IrmPumpRatioPump1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 17),
    _IrmPumpRatioPump1_Type()
)
irmPumpRatioPump1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmPumpRatioPump1.setStatus("current")
_IrmPumpRatioPump2_Type = FloatHundredths
_IrmPumpRatioPump2_Object = MibTableColumn
irmPumpRatioPump2 = _IrmPumpRatioPump2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 18),
    _IrmPumpRatioPump2_Type()
)
irmPumpRatioPump2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmPumpRatioPump2.setStatus("current")
_IrmPumpRatioPump3_Type = FloatHundredths
_IrmPumpRatioPump3_Object = MibTableColumn
irmPumpRatioPump3 = _IrmPumpRatioPump3_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 19),
    _IrmPumpRatioPump3_Type()
)
irmPumpRatioPump3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmPumpRatioPump3.setStatus("current")
_IrmPumpRatioPump4_Type = FloatHundredths
_IrmPumpRatioPump4_Object = MibTableColumn
irmPumpRatioPump4 = _IrmPumpRatioPump4_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 20),
    _IrmPumpRatioPump4_Type()
)
irmPumpRatioPump4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmPumpRatioPump4.setStatus("current")
_IrmStaticRamanGain_Type = FloatHundredths
_IrmStaticRamanGain_Object = MibTableColumn
irmStaticRamanGain = _IrmStaticRamanGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 21),
    _IrmStaticRamanGain_Type()
)
irmStaticRamanGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmStaticRamanGain.setStatus("current")
_IrmStaticEdfaGain_Type = FloatHundredths
_IrmStaticEdfaGain_Object = MibTableColumn
irmStaticEdfaGain = _IrmStaticEdfaGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 22),
    _IrmStaticEdfaGain_Type()
)
irmStaticEdfaGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmStaticEdfaGain.setStatus("current")
_IrmStaticPostEdfaVoaAttenuation_Type = FloatHundredths
_IrmStaticPostEdfaVoaAttenuation_Object = MibTableColumn
irmStaticPostEdfaVoaAttenuation = _IrmStaticPostEdfaVoaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 23),
    _IrmStaticPostEdfaVoaAttenuation_Type()
)
irmStaticPostEdfaVoaAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmStaticPostEdfaVoaAttenuation.setStatus("current")
_IrmFiberType_Type = InfnFiberType
_IrmFiberType_Object = MibTableColumn
irmFiberType = _IrmFiberType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 24),
    _IrmFiberType_Type()
)
irmFiberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmFiberType.setStatus("current")
_IrmGainTiltOffset_Type = FloatHundredths
_IrmGainTiltOffset_Object = MibTableColumn
irmGainTiltOffset = _IrmGainTiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 25),
    _IrmGainTiltOffset_Type()
)
irmGainTiltOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irmGainTiltOffset.setStatus("current")
_IrmOlosSoakTime_Type = InfnOlosSoakTime
_IrmOlosSoakTime_Object = MibTableColumn
irmOlosSoakTime = _IrmOlosSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 26),
    _IrmOlosSoakTime_Type()
)
irmOlosSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmOlosSoakTime.setStatus("current")
_IrmOperatingMode_Type = InfnOAOperatingMode
_IrmOperatingMode_Object = MibTableColumn
irmOperatingMode = _IrmOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 27),
    _IrmOperatingMode_Type()
)
irmOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmOperatingMode.setStatus("current")
_IrmDeploymentConfig_Type = InfnDeploymentConfig
_IrmDeploymentConfig_Object = MibTableColumn
irmDeploymentConfig = _IrmDeploymentConfig_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 28),
    _IrmDeploymentConfig_Type()
)
irmDeploymentConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmDeploymentConfig.setStatus("current")
_IrmRamanGain_Type = FloatArbitraryPrecision
_IrmRamanGain_Object = MibTableColumn
irmRamanGain = _IrmRamanGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 29),
    _IrmRamanGain_Type()
)
irmRamanGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmRamanGain.setStatus("current")
_IrmRamanTiltOffset_Type = FloatArbitraryPrecision
_IrmRamanTiltOffset_Object = MibTableColumn
irmRamanTiltOffset = _IrmRamanTiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 30),
    _IrmRamanTiltOffset_Type()
)
irmRamanTiltOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmRamanTiltOffset.setStatus("current")
_IrmTxVOA_Type = FloatArbitraryPrecision
_IrmTxVOA_Object = MibTableColumn
irmTxVOA = _IrmTxVOA_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 31),
    _IrmTxVOA_Type()
)
irmTxVOA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmTxVOA.setStatus("current")
_IrmLimitPower_Type = InfnEnableDisable
_IrmLimitPower_Object = MibTableColumn
irmLimitPower = _IrmLimitPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 32),
    _IrmLimitPower_Type()
)
irmLimitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmLimitPower.setStatus("current")
_IrmSingleSlotMode_Type = InfnEnableDisable
_IrmSingleSlotMode_Object = MibTableColumn
irmSingleSlotMode = _IrmSingleSlotMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 33),
    _IrmSingleSlotMode_Type()
)
irmSingleSlotMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmSingleSlotMode.setStatus("current")
_IrmALSDisableMode_Type = InfnALSDisableMode
_IrmALSDisableMode_Object = MibTableColumn
irmALSDisableMode = _IrmALSDisableMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 34),
    _IrmALSDisableMode_Type()
)
irmALSDisableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmALSDisableMode.setStatus("current")
_IrmRxEDFAGain_Type = FloatArbitraryPrecision
_IrmRxEDFAGain_Object = MibTableColumn
irmRxEDFAGain = _IrmRxEDFAGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 1, 1, 35),
    _IrmRxEDFAGain_Type()
)
irmRxEDFAGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irmRxEDFAGain.setStatus("current")
_IrmConformance_ObjectIdentity = ObjectIdentity
irmConformance = _IrmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 3)
)
_IrmCompliances_ObjectIdentity = ObjectIdentity
irmCompliances = _IrmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 3, 1)
)
_IrmGroups_ObjectIdentity = ObjectIdentity
irmGroups = _IrmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 3, 2)
)

# Managed Objects groups

irmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 3, 2, 1)
)
irmGroup.setObjects(
      *(("INFINERA-ENTITY-IRM-MIB", "irmMoId"),
        ("INFINERA-ENTITY-IRM-MIB", "irmProvEqptType"),
        ("INFINERA-ENTITY-IRM-MIB", "irmPointLossOffset"),
        ("INFINERA-ENTITY-IRM-MIB", "irmLaunchPowerOffset"),
        ("INFINERA-ENTITY-IRM-MIB", "irmRxDampSeqNum"),
        ("INFINERA-ENTITY-IRM-MIB", "irmEnhPMRept"),
        ("INFINERA-ENTITY-IRM-MIB", "irmAutomaticPLOAdjustmen"),
        ("INFINERA-ENTITY-IRM-MIB", "irmFiberType"),
        ("INFINERA-ENTITY-IRM-MIB", "irmAsePowerBetaCoeffX"),
        ("INFINERA-ENTITY-IRM-MIB", "irmAsePowerBetaCoeffY"),
        ("INFINERA-ENTITY-IRM-MIB", "irmAsePowerBetaCoeffZ"),
        ("INFINERA-ENTITY-IRM-MIB", "irmPumpPowerBetaCoeffX"),
        ("INFINERA-ENTITY-IRM-MIB", "irmPumpPowerBetaCoeffY"),
        ("INFINERA-ENTITY-IRM-MIB", "irmPumpPowerBetaCoeffZ"),
        ("INFINERA-ENTITY-IRM-MIB", "irmPumpRatioPump1"),
        ("INFINERA-ENTITY-IRM-MIB", "irmPumpRatioPump2"),
        ("INFINERA-ENTITY-IRM-MIB", "irmPumpRatioPump3"),
        ("INFINERA-ENTITY-IRM-MIB", "irmPumpRatioPump4"),
        ("INFINERA-ENTITY-IRM-MIB", "irmStaticRamanGain"),
        ("INFINERA-ENTITY-IRM-MIB", "irmStaticEdfaGain"),
        ("INFINERA-ENTITY-IRM-MIB", "irmStaticPostEdfaVoaAttenuation"),
        ("INFINERA-ENTITY-IRM-MIB", "irmTxDampSeqNum"),
        ("INFINERA-ENTITY-IRM-MIB", "irmALSDetectionMode"),
        ("INFINERA-ENTITY-IRM-MIB", "irmPilotLaserDisable"),
        ("INFINERA-ENTITY-IRM-MIB", "irmGainTiltOffset"),
        ("INFINERA-ENTITY-IRM-MIB", "irmOlosSoakTime"),
        ("INFINERA-ENTITY-IRM-MIB", "irmOperatingMode"),
        ("INFINERA-ENTITY-IRM-MIB", "irmDeploymentConfig"),
        ("INFINERA-ENTITY-IRM-MIB", "irmRamanGain"),
        ("INFINERA-ENTITY-IRM-MIB", "irmRamanTiltOffset"),
        ("INFINERA-ENTITY-IRM-MIB", "irmTxVOA"),
        ("INFINERA-ENTITY-IRM-MIB", "irmLimitPower"),
        ("INFINERA-ENTITY-IRM-MIB", "irmSingleSlotMode"),
        ("INFINERA-ENTITY-IRM-MIB", "irmALSDisableMode"),
        ("INFINERA-ENTITY-IRM-MIB", "irmRxEDFAGain"))
)
if mibBuilder.loadTexts:
    irmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

irmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 29, 3, 1, 1)
)
irmCompliance.setObjects(
    ("INFINERA-ENTITY-IRM-MIB", "irmGroup")
)
if mibBuilder.loadTexts:
    irmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-IRM-MIB",
    **{"irmMIB": irmMIB,
       "irmTable": irmTable,
       "irmEntry": irmEntry,
       "irmMoId": irmMoId,
       "irmProvEqptType": irmProvEqptType,
       "irmPointLossOffset": irmPointLossOffset,
       "irmLaunchPowerOffset": irmLaunchPowerOffset,
       "irmRxDampSeqNum": irmRxDampSeqNum,
       "irmTxDampSeqNum": irmTxDampSeqNum,
       "irmPilotLaserDisable": irmPilotLaserDisable,
       "irmEnhPMRept": irmEnhPMRept,
       "irmALSDetectionMode": irmALSDetectionMode,
       "irmAutomaticPLOAdjustmen": irmAutomaticPLOAdjustmen,
       "irmAsePowerBetaCoeffX": irmAsePowerBetaCoeffX,
       "irmAsePowerBetaCoeffY": irmAsePowerBetaCoeffY,
       "irmAsePowerBetaCoeffZ": irmAsePowerBetaCoeffZ,
       "irmPumpPowerBetaCoeffX": irmPumpPowerBetaCoeffX,
       "irmPumpPowerBetaCoeffY": irmPumpPowerBetaCoeffY,
       "irmPumpPowerBetaCoeffZ": irmPumpPowerBetaCoeffZ,
       "irmPumpRatioPump1": irmPumpRatioPump1,
       "irmPumpRatioPump2": irmPumpRatioPump2,
       "irmPumpRatioPump3": irmPumpRatioPump3,
       "irmPumpRatioPump4": irmPumpRatioPump4,
       "irmStaticRamanGain": irmStaticRamanGain,
       "irmStaticEdfaGain": irmStaticEdfaGain,
       "irmStaticPostEdfaVoaAttenuation": irmStaticPostEdfaVoaAttenuation,
       "irmFiberType": irmFiberType,
       "irmGainTiltOffset": irmGainTiltOffset,
       "irmOlosSoakTime": irmOlosSoakTime,
       "irmOperatingMode": irmOperatingMode,
       "irmDeploymentConfig": irmDeploymentConfig,
       "irmRamanGain": irmRamanGain,
       "irmRamanTiltOffset": irmRamanTiltOffset,
       "irmTxVOA": irmTxVOA,
       "irmLimitPower": irmLimitPower,
       "irmSingleSlotMode": irmSingleSlotMode,
       "irmALSDisableMode": irmALSDisableMode,
       "irmRxEDFAGain": irmRxEDFAGain,
       "irmConformance": irmConformance,
       "irmCompliances": irmCompliances,
       "irmCompliance": irmCompliance,
       "irmGroups": irmGroups,
       "irmGroup": irmGroup}
)
