# SNMP MIB module (INFINERA-ENTITY-IAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-IAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:07 2025
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

(FloatTenths,
 InfnALSDisableMode,
 InfnDeploymentConfig,
 InfnEnableDisable,
 InfnEqptType,
 InfnMidStageAccess,
 InfnOAOperatingMode,
 InfnOASlotOperatingMode,
 InfnOTSGainType,
 InfnOlosSoakTime) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnALSDisableMode",
    "InfnDeploymentConfig",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnMidStageAccess",
    "InfnOAOperatingMode",
    "InfnOASlotOperatingMode",
    "InfnOTSGainType",
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

iamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IamTable_Object = MibTable
iamTable = _IamTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1)
)
if mibBuilder.loadTexts:
    iamTable.setStatus("current")
_IamEntry_Object = MibTableRow
iamEntry = _IamEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1)
)
iamEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    iamEntry.setStatus("current")
_IamMoId_Type = DisplayString
_IamMoId_Object = MibTableColumn
iamMoId = _IamMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 1),
    _IamMoId_Type()
)
iamMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iamMoId.setStatus("current")
_IamProvEqptType_Type = InfnEqptType
_IamProvEqptType_Object = MibTableColumn
iamProvEqptType = _IamProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 2),
    _IamProvEqptType_Type()
)
iamProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iamProvEqptType.setStatus("current")
_IamRxDampSeqNum_Type = Integer32
_IamRxDampSeqNum_Object = MibTableColumn
iamRxDampSeqNum = _IamRxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 3),
    _IamRxDampSeqNum_Type()
)
iamRxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamRxDampSeqNum.setStatus("current")
_IamTxDampSeqNum_Type = Integer32
_IamTxDampSeqNum_Object = MibTableColumn
iamTxDampSeqNum = _IamTxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 4),
    _IamTxDampSeqNum_Type()
)
iamTxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamTxDampSeqNum.setStatus("current")
_IamStaticVoaAttenuation_Type = FloatTenths
_IamStaticVoaAttenuation_Object = MibTableColumn
iamStaticVoaAttenuation = _IamStaticVoaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 5),
    _IamStaticVoaAttenuation_Type()
)
iamStaticVoaAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iamStaticVoaAttenuation.setStatus("current")
_IamOlosSoakTime_Type = InfnOlosSoakTime
_IamOlosSoakTime_Object = MibTableColumn
iamOlosSoakTime = _IamOlosSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 6),
    _IamOlosSoakTime_Type()
)
iamOlosSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamOlosSoakTime.setStatus("current")
_IamALSDisableMode_Type = InfnALSDisableMode
_IamALSDisableMode_Object = MibTableColumn
iamALSDisableMode = _IamALSDisableMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 7),
    _IamALSDisableMode_Type()
)
iamALSDisableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamALSDisableMode.setStatus("current")
_IamRxEDFATargetOpt_Type = FloatTenths
_IamRxEDFATargetOpt_Object = MibTableColumn
iamRxEDFATargetOpt = _IamRxEDFATargetOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 8),
    _IamRxEDFATargetOpt_Type()
)
iamRxEDFATargetOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamRxEDFATargetOpt.setStatus("current")
_IamTargetLineOutputPower_Type = FloatTenths
_IamTargetLineOutputPower_Object = MibTableColumn
iamTargetLineOutputPower = _IamTargetLineOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 9),
    _IamTargetLineOutputPower_Type()
)
iamTargetLineOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamTargetLineOutputPower.setStatus("current")
_IamTxVOA_Type = FloatTenths
_IamTxVOA_Object = MibTableColumn
iamTxVOA = _IamTxVOA_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 10),
    _IamTxVOA_Type()
)
iamTxVOA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamTxVOA.setStatus("current")
_IamAssociatedDegree_Type = DisplayString
_IamAssociatedDegree_Object = MibTableColumn
iamAssociatedDegree = _IamAssociatedDegree_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 11),
    _IamAssociatedDegree_Type()
)
iamAssociatedDegree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamAssociatedDegree.setStatus("current")
_IamLaunchPowerOffset_Type = FloatTenths
_IamLaunchPowerOffset_Object = MibTableColumn
iamLaunchPowerOffset = _IamLaunchPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 12),
    _IamLaunchPowerOffset_Type()
)
iamLaunchPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamLaunchPowerOffset.setStatus("current")
_IamGain_Type = FloatTenths
_IamGain_Object = MibTableColumn
iamGain = _IamGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 13),
    _IamGain_Type()
)
iamGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamGain.setStatus("current")
_IamOperatingMode_Type = InfnOAOperatingMode
_IamOperatingMode_Object = MibTableColumn
iamOperatingMode = _IamOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 14),
    _IamOperatingMode_Type()
)
iamOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamOperatingMode.setStatus("current")
_IamGainType_Type = InfnOTSGainType
_IamGainType_Object = MibTableColumn
iamGainType = _IamGainType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 15),
    _IamGainType_Type()
)
iamGainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamGainType.setStatus("current")
_IamMidStageAccess_Type = InfnMidStageAccess
_IamMidStageAccess_Object = MibTableColumn
iamMidStageAccess = _IamMidStageAccess_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 16),
    _IamMidStageAccess_Type()
)
iamMidStageAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamMidStageAccess.setStatus("current")
_IamGainRangeLow_Type = FloatTenths
_IamGainRangeLow_Object = MibTableColumn
iamGainRangeLow = _IamGainRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 17),
    _IamGainRangeLow_Type()
)
iamGainRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamGainRangeLow.setStatus("current")
_IamGainRangeHigh_Type = FloatTenths
_IamGainRangeHigh_Object = MibTableColumn
iamGainRangeHigh = _IamGainRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 18),
    _IamGainRangeHigh_Type()
)
iamGainRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamGainRangeHigh.setStatus("current")
_IamisEqptMisMatchStateIsSet_Type = TruthValue
_IamisEqptMisMatchStateIsSet_Object = MibTableColumn
iamisEqptMisMatchStateIsSet = _IamisEqptMisMatchStateIsSet_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 19),
    _IamisEqptMisMatchStateIsSet_Type()
)
iamisEqptMisMatchStateIsSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamisEqptMisMatchStateIsSet.setStatus("current")
_IamSlotOperatingMode_Type = InfnOASlotOperatingMode
_IamSlotOperatingMode_Object = MibTableColumn
iamSlotOperatingMode = _IamSlotOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 20),
    _IamSlotOperatingMode_Type()
)
iamSlotOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamSlotOperatingMode.setStatus("current")
_IamRxAmpDeviceSetpoint_Type = FloatTenths
_IamRxAmpDeviceSetpoint_Object = MibTableColumn
iamRxAmpDeviceSetpoint = _IamRxAmpDeviceSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 21),
    _IamRxAmpDeviceSetpoint_Type()
)
iamRxAmpDeviceSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamRxAmpDeviceSetpoint.setStatus("current")
_IamRxAmpDeviceTarget_Type = FloatTenths
_IamRxAmpDeviceTarget_Object = MibTableColumn
iamRxAmpDeviceTarget = _IamRxAmpDeviceTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 22),
    _IamRxAmpDeviceTarget_Type()
)
iamRxAmpDeviceTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamRxAmpDeviceTarget.setStatus("current")
_IamRxLastAmpDeviceCommitTs_Type = FloatTenths
_IamRxLastAmpDeviceCommitTs_Object = MibTableColumn
iamRxLastAmpDeviceCommitTs = _IamRxLastAmpDeviceCommitTs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 23),
    _IamRxLastAmpDeviceCommitTs_Type()
)
iamRxLastAmpDeviceCommitTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamRxLastAmpDeviceCommitTs.setStatus("current")
_IamIlRxLineInToEdfa_Type = FloatTenths
_IamIlRxLineInToEdfa_Object = MibTableColumn
iamIlRxLineInToEdfa = _IamIlRxLineInToEdfa_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 24),
    _IamIlRxLineInToEdfa_Type()
)
iamIlRxLineInToEdfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamIlRxLineInToEdfa.setStatus("current")
_IamGainTiltOffset_Type = FloatTenths
_IamGainTiltOffset_Object = MibTableColumn
iamGainTiltOffset = _IamGainTiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 25),
    _IamGainTiltOffset_Type()
)
iamGainTiltOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamGainTiltOffset.setStatus("current")
_IamCBandSoakCapableFW_Type = TruthValue
_IamCBandSoakCapableFW_Object = MibTableColumn
iamCBandSoakCapableFW = _IamCBandSoakCapableFW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 26),
    _IamCBandSoakCapableFW_Type()
)
iamCBandSoakCapableFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iamCBandSoakCapableFW.setStatus("current")
_IamDeploymentConfig_Type = InfnDeploymentConfig
_IamDeploymentConfig_Object = MibTableColumn
iamDeploymentConfig = _IamDeploymentConfig_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 27),
    _IamDeploymentConfig_Type()
)
iamDeploymentConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamDeploymentConfig.setStatus("current")
_IamOSCState_Type = InfnEnableDisable
_IamOSCState_Object = MibTableColumn
iamOSCState = _IamOSCState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 1, 1, 28),
    _IamOSCState_Type()
)
iamOSCState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iamOSCState.setStatus("current")
_IamConformance_ObjectIdentity = ObjectIdentity
iamConformance = _IamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 3)
)
_IamCompliances_ObjectIdentity = ObjectIdentity
iamCompliances = _IamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 3, 1)
)
_IamGroups_ObjectIdentity = ObjectIdentity
iamGroups = _IamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 3, 2)
)

# Managed Objects groups

iamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 3, 2, 1)
)
iamGroup.setObjects(
      *(("INFINERA-ENTITY-IAM-MIB", "iamMoId"),
        ("INFINERA-ENTITY-IAM-MIB", "iamProvEqptType"),
        ("INFINERA-ENTITY-IAM-MIB", "iamLaunchPowerOffset"),
        ("INFINERA-ENTITY-IAM-MIB", "iamRxDampSeqNum"),
        ("INFINERA-ENTITY-IAM-MIB", "iamStaticVoaAttenuation"),
        ("INFINERA-ENTITY-IAM-MIB", "iamTxDampSeqNum"),
        ("INFINERA-ENTITY-IAM-MIB", "iamOperatingMode"),
        ("INFINERA-ENTITY-IAM-MIB", "iamOlosSoakTime"),
        ("INFINERA-ENTITY-IAM-MIB", "iamALSDisableMode"),
        ("INFINERA-ENTITY-IAM-MIB", "iamRxEDFATargetOpt"),
        ("INFINERA-ENTITY-IAM-MIB", "iamTargetLineOutputPower"),
        ("INFINERA-ENTITY-IAM-MIB", "iamTxVOA"),
        ("INFINERA-ENTITY-IAM-MIB", "iamAssociatedDegree"),
        ("INFINERA-ENTITY-IAM-MIB", "iamGain"),
        ("INFINERA-ENTITY-IAM-MIB", "iamOperatingMode"),
        ("INFINERA-ENTITY-IAM-MIB", "iamGainType"),
        ("INFINERA-ENTITY-IAM-MIB", "iamMidStageAccess"),
        ("INFINERA-ENTITY-IAM-MIB", "iamGainRangeLow"),
        ("INFINERA-ENTITY-IAM-MIB", "iamGainRangeHigh"),
        ("INFINERA-ENTITY-IAM-MIB", "iamisEqptMisMatchStateIsSet"),
        ("INFINERA-ENTITY-IAM-MIB", "iamSlotOperatingMode"),
        ("INFINERA-ENTITY-IAM-MIB", "iamRxAmpDeviceSetpoint"),
        ("INFINERA-ENTITY-IAM-MIB", "iamRxAmpDeviceTarget"),
        ("INFINERA-ENTITY-IAM-MIB", "iamRxLastAmpDeviceCommitTs"),
        ("INFINERA-ENTITY-IAM-MIB", "iamIlRxLineInToEdfa"),
        ("INFINERA-ENTITY-IAM-MIB", "iamGainTiltOffset"),
        ("INFINERA-ENTITY-IAM-MIB", "iamCBandSoakCapableFW"),
        ("INFINERA-ENTITY-IAM-MIB", "iamDeploymentConfig"),
        ("INFINERA-ENTITY-IAM-MIB", "iamOSCState"))
)
if mibBuilder.loadTexts:
    iamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

iamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 28, 3, 1, 1)
)
iamCompliance.setObjects(
    ("INFINERA-ENTITY-IAM-MIB", "iamGroup")
)
if mibBuilder.loadTexts:
    iamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-IAM-MIB",
    **{"iamMIB": iamMIB,
       "iamTable": iamTable,
       "iamEntry": iamEntry,
       "iamMoId": iamMoId,
       "iamProvEqptType": iamProvEqptType,
       "iamRxDampSeqNum": iamRxDampSeqNum,
       "iamTxDampSeqNum": iamTxDampSeqNum,
       "iamStaticVoaAttenuation": iamStaticVoaAttenuation,
       "iamOlosSoakTime": iamOlosSoakTime,
       "iamALSDisableMode": iamALSDisableMode,
       "iamRxEDFATargetOpt": iamRxEDFATargetOpt,
       "iamTargetLineOutputPower": iamTargetLineOutputPower,
       "iamTxVOA": iamTxVOA,
       "iamAssociatedDegree": iamAssociatedDegree,
       "iamLaunchPowerOffset": iamLaunchPowerOffset,
       "iamGain": iamGain,
       "iamOperatingMode": iamOperatingMode,
       "iamGainType": iamGainType,
       "iamMidStageAccess": iamMidStageAccess,
       "iamGainRangeLow": iamGainRangeLow,
       "iamGainRangeHigh": iamGainRangeHigh,
       "iamisEqptMisMatchStateIsSet": iamisEqptMisMatchStateIsSet,
       "iamSlotOperatingMode": iamSlotOperatingMode,
       "iamRxAmpDeviceSetpoint": iamRxAmpDeviceSetpoint,
       "iamRxAmpDeviceTarget": iamRxAmpDeviceTarget,
       "iamRxLastAmpDeviceCommitTs": iamRxLastAmpDeviceCommitTs,
       "iamIlRxLineInToEdfa": iamIlRxLineInToEdfa,
       "iamGainTiltOffset": iamGainTiltOffset,
       "iamCBandSoakCapableFW": iamCBandSoakCapableFW,
       "iamDeploymentConfig": iamDeploymentConfig,
       "iamOSCState": iamOSCState,
       "iamConformance": iamConformance,
       "iamCompliances": iamCompliances,
       "iamCompliance": iamCompliance,
       "iamGroups": iamGroups,
       "iamGroup": iamGroup}
)
