# SNMP MIB module (INFINERA-TP-FRMSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FRMSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:25 2025
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

(FloatHundredths,
 InfnAdTpType,
 InfnAutoDiscoveryState,
 InfnEnableDisable,
 InfnEqptType,
 InfnLastPathLossCheckAttemptStatus,
 InfnLastPathLossCheckFailedReason,
 InfnPathLossCheckControlStatus,
 InfnPmHistStatsControl,
 InfnTrafficMode,
 InfnWaveInterfaceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnAdTpType",
    "InfnAutoDiscoveryState",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnLastPathLossCheckAttemptStatus",
    "InfnLastPathLossCheckFailedReason",
    "InfnPathLossCheckControlStatus",
    "InfnPmHistStatsControl",
    "InfnTrafficMode",
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

frmScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45)
)
if mibBuilder.loadTexts:
    frmScgPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrmScgPtpTable_Object = MibTable
frmScgPtpTable = _FrmScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1)
)
if mibBuilder.loadTexts:
    frmScgPtpTable.setStatus("current")
_FrmScgPtpEntry_Object = MibTableRow
frmScgPtpEntry = _FrmScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1)
)
frmScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    frmScgPtpEntry.setStatus("current")
_FrmScgPtpScgNumber_Type = Integer32
_FrmScgPtpScgNumber_Object = MibTableColumn
frmScgPtpScgNumber = _FrmScgPtpScgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 1),
    _FrmScgPtpScgNumber_Type()
)
frmScgPtpScgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpScgNumber.setStatus("current")
_FrmScgPtpScgSupEqptType_Type = InfnEqptType
_FrmScgPtpScgSupEqptType_Object = MibTableColumn
frmScgPtpScgSupEqptType = _FrmScgPtpScgSupEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 2),
    _FrmScgPtpScgSupEqptType_Type()
)
frmScgPtpScgSupEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpScgSupEqptType.setStatus("current")
_FrmScgPtpMPOAID_Type = DisplayString
_FrmScgPtpMPOAID_Object = MibTableColumn
frmScgPtpMPOAID = _FrmScgPtpMPOAID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 3),
    _FrmScgPtpMPOAID_Type()
)
frmScgPtpMPOAID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpMPOAID.setStatus("current")
_FrmScgPtpProvisionedFPMPO_Type = DisplayString
_FrmScgPtpProvisionedFPMPO_Object = MibTableColumn
frmScgPtpProvisionedFPMPO = _FrmScgPtpProvisionedFPMPO_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 4),
    _FrmScgPtpProvisionedFPMPO_Type()
)
frmScgPtpProvisionedFPMPO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpProvisionedFPMPO.setStatus("current")
_FrmScgPtpAutoDiscoveryState_Type = InfnAutoDiscoveryState
_FrmScgPtpAutoDiscoveryState_Object = MibTableColumn
frmScgPtpAutoDiscoveryState = _FrmScgPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 5),
    _FrmScgPtpAutoDiscoveryState_Type()
)
frmScgPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpAutoDiscoveryState.setStatus("current")
_FrmScgPtpDiscoveredNeighborTP_Type = DisplayString
_FrmScgPtpDiscoveredNeighborTP_Object = MibTableColumn
frmScgPtpDiscoveredNeighborTP = _FrmScgPtpDiscoveredNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 6),
    _FrmScgPtpDiscoveredNeighborTP_Type()
)
frmScgPtpDiscoveredNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpDiscoveredNeighborTP.setStatus("current")
_FrmScgPtpProvisionedNeighborTP_Type = DisplayString
_FrmScgPtpProvisionedNeighborTP_Object = MibTableColumn
frmScgPtpProvisionedNeighborTP = _FrmScgPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 7),
    _FrmScgPtpProvisionedNeighborTP_Type()
)
frmScgPtpProvisionedNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpProvisionedNeighborTP.setStatus("current")
_FrmScgPtpProvisionedNeighborAdTpType_Type = InfnAdTpType
_FrmScgPtpProvisionedNeighborAdTpType_Object = MibTableColumn
frmScgPtpProvisionedNeighborAdTpType = _FrmScgPtpProvisionedNeighborAdTpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 8),
    _FrmScgPtpProvisionedNeighborAdTpType_Type()
)
frmScgPtpProvisionedNeighborAdTpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpProvisionedNeighborAdTpType.setStatus("current")
_FrmScgPtpInterfaceType_Type = InfnWaveInterfaceType
_FrmScgPtpInterfaceType_Object = MibTableColumn
frmScgPtpInterfaceType = _FrmScgPtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 9),
    _FrmScgPtpInterfaceType_Type()
)
frmScgPtpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpInterfaceType.setStatus("current")
_FrmScgPtpProvisionedOpenWaveRemotePtp_Type = DisplayString
_FrmScgPtpProvisionedOpenWaveRemotePtp_Object = MibTableColumn
frmScgPtpProvisionedOpenWaveRemotePtp = _FrmScgPtpProvisionedOpenWaveRemotePtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 10),
    _FrmScgPtpProvisionedOpenWaveRemotePtp_Type()
)
frmScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpProvisionedOpenWaveRemotePtp.setStatus("current")
_FrmScgPtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_FrmScgPtpPmHistStatsEnable_Object = MibTableColumn
frmScgPtpPmHistStatsEnable = _FrmScgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 11),
    _FrmScgPtpPmHistStatsEnable_Type()
)
frmScgPtpPmHistStatsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmHistStatsEnable.setStatus("current")
_FrmScgPtpTrafficMode_Type = InfnTrafficMode
_FrmScgPtpTrafficMode_Object = MibTableColumn
frmScgPtpTrafficMode = _FrmScgPtpTrafficMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 12),
    _FrmScgPtpTrafficMode_Type()
)
frmScgPtpTrafficMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpTrafficMode.setStatus("current")
_FrmScgPtpPathLossCheckControlStatus_Type = InfnPathLossCheckControlStatus
_FrmScgPtpPathLossCheckControlStatus_Object = MibTableColumn
frmScgPtpPathLossCheckControlStatus = _FrmScgPtpPathLossCheckControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 13),
    _FrmScgPtpPathLossCheckControlStatus_Type()
)
frmScgPtpPathLossCheckControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPathLossCheckControlStatus.setStatus("current")
_FrmScgPtpLastSuccessfullPathLossCheckTS_Type = Integer32
_FrmScgPtpLastSuccessfullPathLossCheckTS_Object = MibTableColumn
frmScgPtpLastSuccessfullPathLossCheckTS = _FrmScgPtpLastSuccessfullPathLossCheckTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 14),
    _FrmScgPtpLastSuccessfullPathLossCheckTS_Type()
)
frmScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpLastSuccessfullPathLossCheckTS.setStatus("current")
_FrmScgPtpPathLoss_Type = FloatHundredths
_FrmScgPtpPathLoss_Object = MibTableColumn
frmScgPtpPathLoss = _FrmScgPtpPathLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 15),
    _FrmScgPtpPathLoss_Type()
)
frmScgPtpPathLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPathLoss.setStatus("current")
_FrmScgPtpLastPathLossCheckAttemptTS_Type = Integer32
_FrmScgPtpLastPathLossCheckAttemptTS_Object = MibTableColumn
frmScgPtpLastPathLossCheckAttemptTS = _FrmScgPtpLastPathLossCheckAttemptTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 16),
    _FrmScgPtpLastPathLossCheckAttemptTS_Type()
)
frmScgPtpLastPathLossCheckAttemptTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpLastPathLossCheckAttemptTS.setStatus("current")
_FrmScgPtpLastPathLossCheckAttemptStatus_Type = InfnLastPathLossCheckAttemptStatus
_FrmScgPtpLastPathLossCheckAttemptStatus_Object = MibTableColumn
frmScgPtpLastPathLossCheckAttemptStatus = _FrmScgPtpLastPathLossCheckAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 17),
    _FrmScgPtpLastPathLossCheckAttemptStatus_Type()
)
frmScgPtpLastPathLossCheckAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpLastPathLossCheckAttemptStatus.setStatus("current")
_FrmScgPtpLastPathLossCheckFailedReason_Type = InfnLastPathLossCheckFailedReason
_FrmScgPtpLastPathLossCheckFailedReason_Object = MibTableColumn
frmScgPtpLastPathLossCheckFailedReason = _FrmScgPtpLastPathLossCheckFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 18),
    _FrmScgPtpLastPathLossCheckFailedReason_Type()
)
frmScgPtpLastPathLossCheckFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpLastPathLossCheckFailedReason.setStatus("current")
_FrmScgPtpPathLossHigh_Type = TruthValue
_FrmScgPtpPathLossHigh_Object = MibTableColumn
frmScgPtpPathLossHigh = _FrmScgPtpPathLossHigh_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 19),
    _FrmScgPtpPathLossHigh_Type()
)
frmScgPtpPathLossHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPathLossHigh.setStatus("current")
_FrmScgPtpPowerContolLoop_Type = InfnEnableDisable
_FrmScgPtpPowerContolLoop_Object = MibTableColumn
frmScgPtpPowerContolLoop = _FrmScgPtpPowerContolLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 20),
    _FrmScgPtpPowerContolLoop_Type()
)
frmScgPtpPowerContolLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpPowerContolLoop.setStatus("current")
_FrmScgPtpAutoDiscSoakTime_Type = Integer32
_FrmScgPtpAutoDiscSoakTime_Object = MibTableColumn
frmScgPtpAutoDiscSoakTime = _FrmScgPtpAutoDiscSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 21),
    _FrmScgPtpAutoDiscSoakTime_Type()
)
frmScgPtpAutoDiscSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpAutoDiscSoakTime.setStatus("current")
_FrmScgPtpPathLossCheckDetectPort_Type = DisplayString
_FrmScgPtpPathLossCheckDetectPort_Object = MibTableColumn
frmScgPtpPathLossCheckDetectPort = _FrmScgPtpPathLossCheckDetectPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 22),
    _FrmScgPtpPathLossCheckDetectPort_Type()
)
frmScgPtpPathLossCheckDetectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPathLossCheckDetectPort.setStatus("current")
_FrmScgPtpMuxedProvisionedNeighborTPList_Type = DisplayString
_FrmScgPtpMuxedProvisionedNeighborTPList_Object = MibTableColumn
frmScgPtpMuxedProvisionedNeighborTPList = _FrmScgPtpMuxedProvisionedNeighborTPList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 23),
    _FrmScgPtpMuxedProvisionedNeighborTPList_Type()
)
frmScgPtpMuxedProvisionedNeighborTPList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpMuxedProvisionedNeighborTPList.setStatus("current")
_FrmScgPtpPassiveProvisionedNeighborTP_Type = DisplayString
_FrmScgPtpPassiveProvisionedNeighborTP_Object = MibTableColumn
frmScgPtpPassiveProvisionedNeighborTP = _FrmScgPtpPassiveProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 24),
    _FrmScgPtpPassiveProvisionedNeighborTP_Type()
)
frmScgPtpPassiveProvisionedNeighborTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpPassiveProvisionedNeighborTP.setStatus("current")
_FrmScgPtpMuxedProvisionedNeighborMotList_Type = DisplayString
_FrmScgPtpMuxedProvisionedNeighborMotList_Object = MibTableColumn
frmScgPtpMuxedProvisionedNeighborMotList = _FrmScgPtpMuxedProvisionedNeighborMotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 25),
    _FrmScgPtpMuxedProvisionedNeighborMotList_Type()
)
frmScgPtpMuxedProvisionedNeighborMotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpMuxedProvisionedNeighborMotList.setStatus("current")
_FrmScgPtpTxProvNbrTP_Type = DisplayString
_FrmScgPtpTxProvNbrTP_Object = MibTableColumn
frmScgPtpTxProvNbrTP = _FrmScgPtpTxProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 26),
    _FrmScgPtpTxProvNbrTP_Type()
)
frmScgPtpTxProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpTxProvNbrTP.setStatus("current")
_FrmScgPtpRxProvNbrTP_Type = DisplayString
_FrmScgPtpRxProvNbrTP_Object = MibTableColumn
frmScgPtpRxProvNbrTP = _FrmScgPtpRxProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 27),
    _FrmScgPtpRxProvNbrTP_Type()
)
frmScgPtpRxProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frmScgPtpRxProvNbrTP.setStatus("current")
_FrmScgPtpTxProvEqptType_Type = InfnEqptType
_FrmScgPtpTxProvEqptType_Object = MibTableColumn
frmScgPtpTxProvEqptType = _FrmScgPtpTxProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 28),
    _FrmScgPtpTxProvEqptType_Type()
)
frmScgPtpTxProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpTxProvEqptType.setStatus("current")
_FrmScgPtpRxProvEqptType_Type = InfnEqptType
_FrmScgPtpRxProvEqptType_Object = MibTableColumn
frmScgPtpRxProvEqptType = _FrmScgPtpRxProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 1, 1, 29),
    _FrmScgPtpRxProvEqptType_Type()
)
frmScgPtpRxProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpRxProvEqptType.setStatus("current")
_FrmScgPtpConformance_ObjectIdentity = ObjectIdentity
frmScgPtpConformance = _FrmScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 3)
)
_FrmScgPtpCompliances_ObjectIdentity = ObjectIdentity
frmScgPtpCompliances = _FrmScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 3, 1)
)
_FrmScgPtpGroups_ObjectIdentity = ObjectIdentity
frmScgPtpGroups = _FrmScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 3, 2)
)

# Managed Objects groups

frmScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 3, 2, 1)
)
frmScgPtpGroup.setObjects(
      *(("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpTrafficMode"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpPathLossCheckControlStatus"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpLastSuccessfullPathLossCheckTS"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpPathLoss"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpPathLossCheckDetectPort"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpLastPathLossCheckAttemptTS"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpLastPathLossCheckAttemptStatus"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpLastPathLossCheckFailedReason"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpPowerContolLoop"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpScgNumber"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpScgSupEqptType"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpMPOAID"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpProvisionedFPMPO"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpAutoDiscoveryState"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpDiscoveredNeighborTP"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpInterfaceType"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpProvisionedNeighborTP"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpAutoDiscSoakTime"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpMuxedProvisionedNeighborTPList"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpProvisionedOpenWaveRemotePtp"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpPmHistStatsEnable"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpPathLossHigh"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpProvisionedNeighborAdTpType"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpPassiveProvisionedNeighborTP"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpMuxedProvisionedNeighborMotList"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpTxProvNbrTP"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpRxProvNbrTP"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpTxProvEqptType"),
        ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpRxProvEqptType"))
)
if mibBuilder.loadTexts:
    frmScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

frmScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 45, 3, 1, 1)
)
frmScgPtpCompliance.setObjects(
    ("INFINERA-TP-FRMSCGPTP-MIB", "frmScgPtpGroup")
)
if mibBuilder.loadTexts:
    frmScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FRMSCGPTP-MIB",
    **{"frmScgPtpMIB": frmScgPtpMIB,
       "frmScgPtpTable": frmScgPtpTable,
       "frmScgPtpEntry": frmScgPtpEntry,
       "frmScgPtpScgNumber": frmScgPtpScgNumber,
       "frmScgPtpScgSupEqptType": frmScgPtpScgSupEqptType,
       "frmScgPtpMPOAID": frmScgPtpMPOAID,
       "frmScgPtpProvisionedFPMPO": frmScgPtpProvisionedFPMPO,
       "frmScgPtpAutoDiscoveryState": frmScgPtpAutoDiscoveryState,
       "frmScgPtpDiscoveredNeighborTP": frmScgPtpDiscoveredNeighborTP,
       "frmScgPtpProvisionedNeighborTP": frmScgPtpProvisionedNeighborTP,
       "frmScgPtpProvisionedNeighborAdTpType": frmScgPtpProvisionedNeighborAdTpType,
       "frmScgPtpInterfaceType": frmScgPtpInterfaceType,
       "frmScgPtpProvisionedOpenWaveRemotePtp": frmScgPtpProvisionedOpenWaveRemotePtp,
       "frmScgPtpPmHistStatsEnable": frmScgPtpPmHistStatsEnable,
       "frmScgPtpTrafficMode": frmScgPtpTrafficMode,
       "frmScgPtpPathLossCheckControlStatus": frmScgPtpPathLossCheckControlStatus,
       "frmScgPtpLastSuccessfullPathLossCheckTS": frmScgPtpLastSuccessfullPathLossCheckTS,
       "frmScgPtpPathLoss": frmScgPtpPathLoss,
       "frmScgPtpLastPathLossCheckAttemptTS": frmScgPtpLastPathLossCheckAttemptTS,
       "frmScgPtpLastPathLossCheckAttemptStatus": frmScgPtpLastPathLossCheckAttemptStatus,
       "frmScgPtpLastPathLossCheckFailedReason": frmScgPtpLastPathLossCheckFailedReason,
       "frmScgPtpPathLossHigh": frmScgPtpPathLossHigh,
       "frmScgPtpPowerContolLoop": frmScgPtpPowerContolLoop,
       "frmScgPtpAutoDiscSoakTime": frmScgPtpAutoDiscSoakTime,
       "frmScgPtpPathLossCheckDetectPort": frmScgPtpPathLossCheckDetectPort,
       "frmScgPtpMuxedProvisionedNeighborTPList": frmScgPtpMuxedProvisionedNeighborTPList,
       "frmScgPtpPassiveProvisionedNeighborTP": frmScgPtpPassiveProvisionedNeighborTP,
       "frmScgPtpMuxedProvisionedNeighborMotList": frmScgPtpMuxedProvisionedNeighborMotList,
       "frmScgPtpTxProvNbrTP": frmScgPtpTxProvNbrTP,
       "frmScgPtpRxProvNbrTP": frmScgPtpRxProvNbrTP,
       "frmScgPtpTxProvEqptType": frmScgPtpTxProvEqptType,
       "frmScgPtpRxProvEqptType": frmScgPtpRxProvEqptType,
       "frmScgPtpConformance": frmScgPtpConformance,
       "frmScgPtpCompliances": frmScgPtpCompliances,
       "frmScgPtpCompliance": frmScgPtpCompliance,
       "frmScgPtpGroups": frmScgPtpGroups,
       "frmScgPtpGroup": frmScgPtpGroup}
)
