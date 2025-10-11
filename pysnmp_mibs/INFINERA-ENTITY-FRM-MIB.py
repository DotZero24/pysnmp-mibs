# SNMP MIB module (INFINERA-ENTITY-FRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-FRM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:36 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatTenths,
 InfnAddDropCount,
 InfnCBandOlosSoakTime,
 InfnEnableDisable,
 InfnEqptType,
 InfnOAOperatingMode,
 InfnSlotOperatingMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnAddDropCount",
    "InfnCBandOlosSoakTime",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnOAOperatingMode",
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

frmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrmTable_Object = MibTable
frmTable = _FrmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1)
)
if mibBuilder.loadTexts:
    frmTable.setStatus("current")
_FrmEntry_Object = MibTableRow
frmEntry = _FrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1)
)
frmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    frmEntry.setStatus("current")
_FrmMoId_Type = DisplayString
_FrmMoId_Object = MibTableColumn
frmMoId = _FrmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 1),
    _FrmMoId_Type()
)
frmMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmMoId.setStatus("current")
_FrmProvEqptType_Type = InfnEqptType
_FrmProvEqptType_Object = MibTableColumn
frmProvEqptType = _FrmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 2),
    _FrmProvEqptType_Type()
)
frmProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmProvEqptType.setStatus("current")
_FrmAutomaticTiltControl_Type = InfnEnableDisable
_FrmAutomaticTiltControl_Object = MibTableColumn
frmAutomaticTiltControl = _FrmAutomaticTiltControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 3),
    _FrmAutomaticTiltControl_Type()
)
frmAutomaticTiltControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmAutomaticTiltControl.setStatus("current")
_FrmSpectrumTiltOffset_Type = FloatTenths
_FrmSpectrumTiltOffset_Object = MibTableColumn
frmSpectrumTiltOffset = _FrmSpectrumTiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 4),
    _FrmSpectrumTiltOffset_Type()
)
frmSpectrumTiltOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmSpectrumTiltOffset.setStatus("current")
_FrmMaxAddDropPorts_Type = InfnAddDropCount
_FrmMaxAddDropPorts_Object = MibTableColumn
frmMaxAddDropPorts = _FrmMaxAddDropPorts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 5),
    _FrmMaxAddDropPorts_Type()
)
frmMaxAddDropPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmMaxAddDropPorts.setStatus("current")
_FrmGainTiltOffset_Type = FloatTenths
_FrmGainTiltOffset_Object = MibTableColumn
frmGainTiltOffset = _FrmGainTiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 6),
    _FrmGainTiltOffset_Type()
)
frmGainTiltOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmGainTiltOffset.setStatus("current")
_FrmEdfaPowerOffset_Type = FloatTenths
_FrmEdfaPowerOffset_Object = MibTableColumn
frmEdfaPowerOffset = _FrmEdfaPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 7),
    _FrmEdfaPowerOffset_Type()
)
frmEdfaPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmEdfaPowerOffset.setStatus("current")
_FrmGainControlLoop_Type = InfnEnableDisable
_FrmGainControlLoop_Object = MibTableColumn
frmGainControlLoop = _FrmGainControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 8),
    _FrmGainControlLoop_Type()
)
frmGainControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmGainControlLoop.setStatus("current")
_FrmRxPowerOffset_Type = FloatTenths
_FrmRxPowerOffset_Object = MibTableColumn
frmRxPowerOffset = _FrmRxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 9),
    _FrmRxPowerOffset_Type()
)
frmRxPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frmRxPowerOffset.setStatus("current")
_FrmRxAmpDeviceSetpoint_Type = FloatTenths
_FrmRxAmpDeviceSetpoint_Object = MibTableColumn
frmRxAmpDeviceSetpoint = _FrmRxAmpDeviceSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 12),
    _FrmRxAmpDeviceSetpoint_Type()
)
frmRxAmpDeviceSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmRxAmpDeviceSetpoint.setStatus("current")
_FrmRxAmpDeviceTarget_Type = FloatTenths
_FrmRxAmpDeviceTarget_Object = MibTableColumn
frmRxAmpDeviceTarget = _FrmRxAmpDeviceTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 13),
    _FrmRxAmpDeviceTarget_Type()
)
frmRxAmpDeviceTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmRxAmpDeviceTarget.setStatus("current")
_FrmRxLastAmpDeviceCommitTs_Type = Integer32
_FrmRxLastAmpDeviceCommitTs_Object = MibTableColumn
frmRxLastAmpDeviceCommitTs = _FrmRxLastAmpDeviceCommitTs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 14),
    _FrmRxLastAmpDeviceCommitTs_Type()
)
frmRxLastAmpDeviceCommitTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmRxLastAmpDeviceCommitTs.setStatus("current")
_FrmTxDampSeqNum_Type = Integer32
_FrmTxDampSeqNum_Object = MibTableColumn
frmTxDampSeqNum = _FrmTxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 15),
    _FrmTxDampSeqNum_Type()
)
frmTxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmTxDampSeqNum.setStatus("current")
_FrmRxDampSeqNum_Type = Integer32
_FrmRxDampSeqNum_Object = MibTableColumn
frmRxDampSeqNum = _FrmRxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 16),
    _FrmRxDampSeqNum_Type()
)
frmRxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmRxDampSeqNum.setStatus("current")
_FrmAdPwrTgtFailPortMask_Type = Integer32
_FrmAdPwrTgtFailPortMask_Object = MibTableColumn
frmAdPwrTgtFailPortMask = _FrmAdPwrTgtFailPortMask_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 17),
    _FrmAdPwrTgtFailPortMask_Type()
)
frmAdPwrTgtFailPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmAdPwrTgtFailPortMask.setStatus("current")
_FrmOlosSoakTime_Type = InfnCBandOlosSoakTime
_FrmOlosSoakTime_Object = MibTableColumn
frmOlosSoakTime = _FrmOlosSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 18),
    _FrmOlosSoakTime_Type()
)
frmOlosSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmOlosSoakTime.setStatus("current")
_FrmIsPathLossCheckInvoked_Type = TruthValue
_FrmIsPathLossCheckInvoked_Object = MibTableColumn
frmIsPathLossCheckInvoked = _FrmIsPathLossCheckInvoked_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 19),
    _FrmIsPathLossCheckInvoked_Type()
)
frmIsPathLossCheckInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmIsPathLossCheckInvoked.setStatus("current")
_FrmPathLossInvokedPortAid_Type = DisplayString
_FrmPathLossInvokedPortAid_Object = MibTableColumn
frmPathLossInvokedPortAid = _FrmPathLossInvokedPortAid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 20),
    _FrmPathLossInvokedPortAid_Type()
)
frmPathLossInvokedPortAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmPathLossInvokedPortAid.setStatus("current")
_FrmDampStatusString_Type = DisplayString
_FrmDampStatusString_Object = MibTableColumn
frmDampStatusString = _FrmDampStatusString_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 21),
    _FrmDampStatusString_Type()
)
frmDampStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmDampStatusString.setStatus("current")
_FrmDampNullSeqReason_Type = DisplayString
_FrmDampNullSeqReason_Object = MibTableColumn
frmDampNullSeqReason = _FrmDampNullSeqReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 22),
    _FrmDampNullSeqReason_Type()
)
frmDampNullSeqReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmDampNullSeqReason.setStatus("current")
_FrmOperatingMode_Type = InfnOAOperatingMode
_FrmOperatingMode_Object = MibTableColumn
frmOperatingMode = _FrmOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 23),
    _FrmOperatingMode_Type()
)
frmOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmOperatingMode.setStatus("current")
_FrmDeploymentLabel1_Type = DisplayString
_FrmDeploymentLabel1_Object = MibTableColumn
frmDeploymentLabel1 = _FrmDeploymentLabel1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 24),
    _FrmDeploymentLabel1_Type()
)
frmDeploymentLabel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmDeploymentLabel1.setStatus("current")
_FrmDeploymentLabel2_Type = DisplayString
_FrmDeploymentLabel2_Object = MibTableColumn
frmDeploymentLabel2 = _FrmDeploymentLabel2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 25),
    _FrmDeploymentLabel2_Type()
)
frmDeploymentLabel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmDeploymentLabel2.setStatus("current")
_FrmDeploymentLabel3_Type = DisplayString
_FrmDeploymentLabel3_Object = MibTableColumn
frmDeploymentLabel3 = _FrmDeploymentLabel3_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 26),
    _FrmDeploymentLabel3_Type()
)
frmDeploymentLabel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmDeploymentLabel3.setStatus("current")
_FrmSlotOperatingMode_Type = InfnSlotOperatingMode
_FrmSlotOperatingMode_Object = MibTableColumn
frmSlotOperatingMode = _FrmSlotOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 27),
    _FrmSlotOperatingMode_Type()
)
frmSlotOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmSlotOperatingMode.setStatus("current")
_FrmLaunchPowerOffset_Type = FloatTenths
_FrmLaunchPowerOffset_Object = MibTableColumn
frmLaunchPowerOffset = _FrmLaunchPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 28),
    _FrmLaunchPowerOffset_Type()
)
frmLaunchPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmLaunchPowerOffset.setStatus("current")
_FrmMaxLaunchPowerOffset_Type = FloatTenths
_FrmMaxLaunchPowerOffset_Object = MibTableColumn
frmMaxLaunchPowerOffset = _FrmMaxLaunchPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 29),
    _FrmMaxLaunchPowerOffset_Type()
)
frmMaxLaunchPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmMaxLaunchPowerOffset.setStatus("current")
_FrmTxAmpDeviceSetpoint_Type = FloatTenths
_FrmTxAmpDeviceSetpoint_Object = MibTableColumn
frmTxAmpDeviceSetpoint = _FrmTxAmpDeviceSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 30),
    _FrmTxAmpDeviceSetpoint_Type()
)
frmTxAmpDeviceSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmTxAmpDeviceSetpoint.setStatus("current")
_FrmTxAmpDeviceTarget_Type = FloatTenths
_FrmTxAmpDeviceTarget_Object = MibTableColumn
frmTxAmpDeviceTarget = _FrmTxAmpDeviceTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 31),
    _FrmTxAmpDeviceTarget_Type()
)
frmTxAmpDeviceTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmTxAmpDeviceTarget.setStatus("current")
_FrmTxLastAmpDeviceCommitTs_Type = Integer32
_FrmTxLastAmpDeviceCommitTs_Object = MibTableColumn
frmTxLastAmpDeviceCommitTs = _FrmTxLastAmpDeviceCommitTs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 32),
    _FrmTxLastAmpDeviceCommitTs_Type()
)
frmTxLastAmpDeviceCommitTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmTxLastAmpDeviceCommitTs.setStatus("current")
_FrmRamanGainSetPoint_Type = FloatTenths
_FrmRamanGainSetPoint_Object = MibTableColumn
frmRamanGainSetPoint = _FrmRamanGainSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 33),
    _FrmRamanGainSetPoint_Type()
)
frmRamanGainSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmRamanGainSetPoint.setStatus("current")
_FrmTxVOASetPoint_Type = FloatTenths
_FrmTxVOASetPoint_Object = MibTableColumn
frmTxVOASetPoint = _FrmTxVOASetPoint_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 34),
    _FrmTxVOASetPoint_Type()
)
frmTxVOASetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmTxVOASetPoint.setStatus("current")
_FrmSuccessfulAGCRunTime_Type = Integer32
_FrmSuccessfulAGCRunTime_Object = MibTableColumn
frmSuccessfulAGCRunTime = _FrmSuccessfulAGCRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 1, 1, 35),
    _FrmSuccessfulAGCRunTime_Type()
)
frmSuccessfulAGCRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmSuccessfulAGCRunTime.setStatus("current")
_FrmConffrmance_ObjectIdentity = ObjectIdentity
frmConffrmance = _FrmConffrmance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 3)
)
_FrmCompliances_ObjectIdentity = ObjectIdentity
frmCompliances = _FrmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 3, 1)
)
_FrmGroups_ObjectIdentity = ObjectIdentity
frmGroups = _FrmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 3, 2)
)

# Managed Objects groups

frmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 3, 2, 1)
)
frmGroup.setObjects(
      *(("INFINERA-ENTITY-FRM-MIB", "frmMoId"),
        ("INFINERA-ENTITY-FRM-MIB", "frmProvEqptType"),
        ("INFINERA-ENTITY-FRM-MIB", "frmAutomaticTiltControl"),
        ("INFINERA-ENTITY-FRM-MIB", "frmSpectrumTiltOffset"),
        ("INFINERA-ENTITY-FRM-MIB", "frmMaxAddDropPorts"),
        ("INFINERA-ENTITY-FRM-MIB", "frmGainTiltOffset"),
        ("INFINERA-ENTITY-FRM-MIB", "frmEdfaPowerOffset"),
        ("INFINERA-ENTITY-FRM-MIB", "frmGainControlLoop"),
        ("INFINERA-ENTITY-FRM-MIB", "frmRxAmpDeviceSetpoint"),
        ("INFINERA-ENTITY-FRM-MIB", "frmRxAmpDeviceTarget"),
        ("INFINERA-ENTITY-FRM-MIB", "frmRxLastAmpDeviceCommitTs"),
        ("INFINERA-ENTITY-FRM-MIB", "frmTxDampSeqNum"),
        ("INFINERA-ENTITY-FRM-MIB", "frmRxDampSeqNum"),
        ("INFINERA-ENTITY-FRM-MIB", "frmAdPwrTgtFailPortMask"),
        ("INFINERA-ENTITY-FRM-MIB", "frmOlosSoakTime"),
        ("INFINERA-ENTITY-FRM-MIB", "frmDampStatusString"),
        ("INFINERA-ENTITY-FRM-MIB", "frmDampNullSeqReason"),
        ("INFINERA-ENTITY-FRM-MIB", "frmRxPowerOffset"),
        ("INFINERA-ENTITY-FRM-MIB", "frmIsPathLossCheckInvoked"),
        ("INFINERA-ENTITY-FRM-MIB", "frmPathLossInvokedPortAid"),
        ("INFINERA-ENTITY-FRM-MIB", "frmOperatingMode"),
        ("INFINERA-ENTITY-FRM-MIB", "frmDeploymentLabel1"),
        ("INFINERA-ENTITY-FRM-MIB", "frmDeploymentLabel2"),
        ("INFINERA-ENTITY-FRM-MIB", "frmDeploymentLabel3"),
        ("INFINERA-ENTITY-FRM-MIB", "frmSlotOperatingMode"),
        ("INFINERA-ENTITY-FRM-MIB", "frmLaunchPowerOffset"),
        ("INFINERA-ENTITY-FRM-MIB", "frmMaxLaunchPowerOffset"),
        ("INFINERA-ENTITY-FRM-MIB", "frmTxAmpDeviceSetpoint"),
        ("INFINERA-ENTITY-FRM-MIB", "frmTxAmpDeviceTarget"),
        ("INFINERA-ENTITY-FRM-MIB", "frmTxLastAmpDeviceCommitTs"),
        ("INFINERA-ENTITY-FRM-MIB", "frmRamanGainSetPoint"),
        ("INFINERA-ENTITY-FRM-MIB", "frmTxVOASetPoint"),
        ("INFINERA-ENTITY-FRM-MIB", "frmSuccessfulAGCRunTime"))
)
if mibBuilder.loadTexts:
    frmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

frmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 33, 3, 1, 1)
)
frmCompliance.setObjects(
    ("INFINERA-ENTITY-FRM-MIB", "frmGroup")
)
if mibBuilder.loadTexts:
    frmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-FRM-MIB",
    **{"frmMIB": frmMIB,
       "frmTable": frmTable,
       "frmEntry": frmEntry,
       "frmMoId": frmMoId,
       "frmProvEqptType": frmProvEqptType,
       "frmAutomaticTiltControl": frmAutomaticTiltControl,
       "frmSpectrumTiltOffset": frmSpectrumTiltOffset,
       "frmMaxAddDropPorts": frmMaxAddDropPorts,
       "frmGainTiltOffset": frmGainTiltOffset,
       "frmEdfaPowerOffset": frmEdfaPowerOffset,
       "frmGainControlLoop": frmGainControlLoop,
       "frmRxPowerOffset": frmRxPowerOffset,
       "frmRxAmpDeviceSetpoint": frmRxAmpDeviceSetpoint,
       "frmRxAmpDeviceTarget": frmRxAmpDeviceTarget,
       "frmRxLastAmpDeviceCommitTs": frmRxLastAmpDeviceCommitTs,
       "frmTxDampSeqNum": frmTxDampSeqNum,
       "frmRxDampSeqNum": frmRxDampSeqNum,
       "frmAdPwrTgtFailPortMask": frmAdPwrTgtFailPortMask,
       "frmOlosSoakTime": frmOlosSoakTime,
       "frmIsPathLossCheckInvoked": frmIsPathLossCheckInvoked,
       "frmPathLossInvokedPortAid": frmPathLossInvokedPortAid,
       "frmDampStatusString": frmDampStatusString,
       "frmDampNullSeqReason": frmDampNullSeqReason,
       "frmOperatingMode": frmOperatingMode,
       "frmDeploymentLabel1": frmDeploymentLabel1,
       "frmDeploymentLabel2": frmDeploymentLabel2,
       "frmDeploymentLabel3": frmDeploymentLabel3,
       "frmSlotOperatingMode": frmSlotOperatingMode,
       "frmLaunchPowerOffset": frmLaunchPowerOffset,
       "frmMaxLaunchPowerOffset": frmMaxLaunchPowerOffset,
       "frmTxAmpDeviceSetpoint": frmTxAmpDeviceSetpoint,
       "frmTxAmpDeviceTarget": frmTxAmpDeviceTarget,
       "frmTxLastAmpDeviceCommitTs": frmTxLastAmpDeviceCommitTs,
       "frmRamanGainSetPoint": frmRamanGainSetPoint,
       "frmTxVOASetPoint": frmTxVOASetPoint,
       "frmSuccessfulAGCRunTime": frmSuccessfulAGCRunTime,
       "frmConffrmance": frmConffrmance,
       "frmCompliances": frmCompliances,
       "frmCompliance": frmCompliance,
       "frmGroups": frmGroups,
       "frmGroup": frmGroup}
)
