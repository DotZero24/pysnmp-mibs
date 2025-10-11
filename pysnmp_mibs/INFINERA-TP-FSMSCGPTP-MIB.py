# SNMP MIB module (INFINERA-TP-FSMSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FSMSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:38 2025
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
 InfnEnableDisable,
 InfnEqptType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnEnableDisable",
    "InfnEqptType")

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

fsmScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44)
)
if mibBuilder.loadTexts:
    fsmScgPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsmScgPtpTable_Object = MibTable
fsmScgPtpTable = _FsmScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1)
)
if mibBuilder.loadTexts:
    fsmScgPtpTable.setStatus("current")
_FsmScgPtpEntry_Object = MibTableRow
fsmScgPtpEntry = _FsmScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1)
)
fsmScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsmScgPtpEntry.setStatus("current")
_FsmScgPtpPowerControlLoop_Type = InfnEnableDisable
_FsmScgPtpPowerControlLoop_Object = MibTableColumn
fsmScgPtpPowerControlLoop = _FsmScgPtpPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 1),
    _FsmScgPtpPowerControlLoop_Type()
)
fsmScgPtpPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmScgPtpPowerControlLoop.setStatus("current")
_FsmScgPtpAvailableFreqSlotList_Type = DisplayString
_FsmScgPtpAvailableFreqSlotList_Object = MibTableColumn
fsmScgPtpAvailableFreqSlotList = _FsmScgPtpAvailableFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 2),
    _FsmScgPtpAvailableFreqSlotList_Type()
)
fsmScgPtpAvailableFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpAvailableFreqSlotList.setStatus("current")
_FsmScgPtpUsedFreqSlotList_Type = DisplayString
_FsmScgPtpUsedFreqSlotList_Object = MibTableColumn
fsmScgPtpUsedFreqSlotList = _FsmScgPtpUsedFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 3),
    _FsmScgPtpUsedFreqSlotList_Type()
)
fsmScgPtpUsedFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpUsedFreqSlotList.setStatus("current")


class _FsmScgPtpPathLossCheckControlStatus_Type(Integer32):
    """Custom type fsmScgPtpPathLossCheckControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("idle", 2))
    )


_FsmScgPtpPathLossCheckControlStatus_Type.__name__ = "Integer32"
_FsmScgPtpPathLossCheckControlStatus_Object = MibTableColumn
fsmScgPtpPathLossCheckControlStatus = _FsmScgPtpPathLossCheckControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 4),
    _FsmScgPtpPathLossCheckControlStatus_Type()
)
fsmScgPtpPathLossCheckControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPathLossCheckControlStatus.setStatus("current")
_FsmScgPtpLastSuccessfullPathLossCheckTS_Type = Integer32
_FsmScgPtpLastSuccessfullPathLossCheckTS_Object = MibTableColumn
fsmScgPtpLastSuccessfullPathLossCheckTS = _FsmScgPtpLastSuccessfullPathLossCheckTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 5),
    _FsmScgPtpLastSuccessfullPathLossCheckTS_Type()
)
fsmScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpLastSuccessfullPathLossCheckTS.setStatus("current")
_FsmScgPtpPathLoss_Type = FloatHundredths
_FsmScgPtpPathLoss_Object = MibTableColumn
fsmScgPtpPathLoss = _FsmScgPtpPathLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 6),
    _FsmScgPtpPathLoss_Type()
)
fsmScgPtpPathLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPathLoss.setStatus("current")
_FsmScgPtpPathLossCheckDetectPort_Type = DisplayString
_FsmScgPtpPathLossCheckDetectPort_Object = MibTableColumn
fsmScgPtpPathLossCheckDetectPort = _FsmScgPtpPathLossCheckDetectPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 7),
    _FsmScgPtpPathLossCheckDetectPort_Type()
)
fsmScgPtpPathLossCheckDetectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPathLossCheckDetectPort.setStatus("current")
_FsmScgPtpLastPathLossCheckAttemptTS_Type = Integer32
_FsmScgPtpLastPathLossCheckAttemptTS_Object = MibTableColumn
fsmScgPtpLastPathLossCheckAttemptTS = _FsmScgPtpLastPathLossCheckAttemptTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 8),
    _FsmScgPtpLastPathLossCheckAttemptTS_Type()
)
fsmScgPtpLastPathLossCheckAttemptTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpLastPathLossCheckAttemptTS.setStatus("current")


class _FsmScgPtpLastPathLossCheckAttemptStatus_Type(Integer32):
    """Custom type fsmScgPtpLastPathLossCheckAttemptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("successfull", 1),
          ("unsuccessfull", 2),
          ("notAttempted", 3))
    )


_FsmScgPtpLastPathLossCheckAttemptStatus_Type.__name__ = "Integer32"
_FsmScgPtpLastPathLossCheckAttemptStatus_Object = MibTableColumn
fsmScgPtpLastPathLossCheckAttemptStatus = _FsmScgPtpLastPathLossCheckAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 9),
    _FsmScgPtpLastPathLossCheckAttemptStatus_Type()
)
fsmScgPtpLastPathLossCheckAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpLastPathLossCheckAttemptStatus.setStatus("current")


class _FsmScgPtpLastPathLossCheckFailedReason_Type(Integer32):
    """Custom type fsmScgPtpLastPathLossCheckFailedReason based on Integer32"""
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
        *(("notAvailable", 1),
          ("timedOut", 2),
          ("interruptedByAD", 3),
          ("interruptedByReset", 4),
          ("portInService", 5))
    )


_FsmScgPtpLastPathLossCheckFailedReason_Type.__name__ = "Integer32"
_FsmScgPtpLastPathLossCheckFailedReason_Object = MibTableColumn
fsmScgPtpLastPathLossCheckFailedReason = _FsmScgPtpLastPathLossCheckFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 10),
    _FsmScgPtpLastPathLossCheckFailedReason_Type()
)
fsmScgPtpLastPathLossCheckFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpLastPathLossCheckFailedReason.setStatus("current")
_FsmScgPtpTxEdfaPowerOffset_Type = FloatHundredths
_FsmScgPtpTxEdfaPowerOffset_Object = MibTableColumn
fsmScgPtpTxEdfaPowerOffset = _FsmScgPtpTxEdfaPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 11),
    _FsmScgPtpTxEdfaPowerOffset_Type()
)
fsmScgPtpTxEdfaPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmScgPtpTxEdfaPowerOffset.setStatus("current")
_FsmScgPtpRxEdfaPowerOffset_Type = FloatHundredths
_FsmScgPtpRxEdfaPowerOffset_Object = MibTableColumn
fsmScgPtpRxEdfaPowerOffset = _FsmScgPtpRxEdfaPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 12),
    _FsmScgPtpRxEdfaPowerOffset_Type()
)
fsmScgPtpRxEdfaPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmScgPtpRxEdfaPowerOffset.setStatus("current")


class _FsmScgPtpTrafficMode_Type(Integer32):
    """Custom type fsmScgPtpTrafficMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("addDrop", 2),
          ("pathLossCheckSource", 3))
    )


_FsmScgPtpTrafficMode_Type.__name__ = "Integer32"
_FsmScgPtpTrafficMode_Object = MibTableColumn
fsmScgPtpTrafficMode = _FsmScgPtpTrafficMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 13),
    _FsmScgPtpTrafficMode_Type()
)
fsmScgPtpTrafficMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmScgPtpTrafficMode.setStatus("current")
_FsmScgPtpScgNumber_Type = Integer32
_FsmScgPtpScgNumber_Object = MibTableColumn
fsmScgPtpScgNumber = _FsmScgPtpScgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 14),
    _FsmScgPtpScgNumber_Type()
)
fsmScgPtpScgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpScgNumber.setStatus("current")
_FsmScgPtpScgSupEqptType_Type = InfnEqptType
_FsmScgPtpScgSupEqptType_Object = MibTableColumn
fsmScgPtpScgSupEqptType = _FsmScgPtpScgSupEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 15),
    _FsmScgPtpScgSupEqptType_Type()
)
fsmScgPtpScgSupEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmScgPtpScgSupEqptType.setStatus("current")
_FsmScgPtpMPOAID_Type = DisplayString
_FsmScgPtpMPOAID_Object = MibTableColumn
fsmScgPtpMPOAID = _FsmScgPtpMPOAID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 16),
    _FsmScgPtpMPOAID_Type()
)
fsmScgPtpMPOAID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmScgPtpMPOAID.setStatus("current")
_FsmScgPtpProvisionedFPMPO_Type = DisplayString
_FsmScgPtpProvisionedFPMPO_Object = MibTableColumn
fsmScgPtpProvisionedFPMPO = _FsmScgPtpProvisionedFPMPO_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 17),
    _FsmScgPtpProvisionedFPMPO_Type()
)
fsmScgPtpProvisionedFPMPO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmScgPtpProvisionedFPMPO.setStatus("current")


class _FsmScgPtpAutoDiscoveryState_Type(Integer32):
    """Custom type fsmScgPtpAutoDiscoveryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("completed", 2),
          ("unknown", 3),
          ("notValid", 4),
          ("failed", 5),
          ("waitToStart", 6),
          ("associated", 7))
    )


_FsmScgPtpAutoDiscoveryState_Type.__name__ = "Integer32"
_FsmScgPtpAutoDiscoveryState_Object = MibTableColumn
fsmScgPtpAutoDiscoveryState = _FsmScgPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 18),
    _FsmScgPtpAutoDiscoveryState_Type()
)
fsmScgPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpAutoDiscoveryState.setStatus("current")
_FsmScgPtpDiscoveredNeighborTP_Type = DisplayString
_FsmScgPtpDiscoveredNeighborTP_Object = MibTableColumn
fsmScgPtpDiscoveredNeighborTP = _FsmScgPtpDiscoveredNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 19),
    _FsmScgPtpDiscoveredNeighborTP_Type()
)
fsmScgPtpDiscoveredNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpDiscoveredNeighborTP.setStatus("current")


class _FsmScgPtpInterfaceType_Type(Integer32):
    """Custom type fsmScgPtpInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optical", 1),
          ("electrical", 2))
    )


_FsmScgPtpInterfaceType_Type.__name__ = "Integer32"
_FsmScgPtpInterfaceType_Object = MibTableColumn
fsmScgPtpInterfaceType = _FsmScgPtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 20),
    _FsmScgPtpInterfaceType_Type()
)
fsmScgPtpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmScgPtpInterfaceType.setStatus("current")
_FsmScgPtpProvisionedOpenWaveRemotePtp_Type = DisplayString
_FsmScgPtpProvisionedOpenWaveRemotePtp_Object = MibTableColumn
fsmScgPtpProvisionedOpenWaveRemotePtp = _FsmScgPtpProvisionedOpenWaveRemotePtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 21),
    _FsmScgPtpProvisionedOpenWaveRemotePtp_Type()
)
fsmScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmScgPtpProvisionedOpenWaveRemotePtp.setStatus("current")


class _FsmScgPtpPmHistStatsEnable_Type(Integer32):
    """Custom type fsmScgPtpPmHistStatsEnable based on Integer32"""
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


_FsmScgPtpPmHistStatsEnable_Type.__name__ = "Integer32"
_FsmScgPtpPmHistStatsEnable_Object = MibTableColumn
fsmScgPtpPmHistStatsEnable = _FsmScgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 22),
    _FsmScgPtpPmHistStatsEnable_Type()
)
fsmScgPtpPmHistStatsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmHistStatsEnable.setStatus("current")
_FsmScgPtpProvisionedNeighborTP_Type = DisplayString
_FsmScgPtpProvisionedNeighborTP_Object = MibTableColumn
fsmScgPtpProvisionedNeighborTP = _FsmScgPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 23),
    _FsmScgPtpProvisionedNeighborTP_Type()
)
fsmScgPtpProvisionedNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpProvisionedNeighborTP.setStatus("current")


class _FsmScgPtpPathLossHigh_Type(Integer32):
    """Custom type fsmScgPtpPathLossHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_FsmScgPtpPathLossHigh_Type.__name__ = "Integer32"
_FsmScgPtpPathLossHigh_Object = MibTableColumn
fsmScgPtpPathLossHigh = _FsmScgPtpPathLossHigh_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 1, 1, 24),
    _FsmScgPtpPathLossHigh_Type()
)
fsmScgPtpPathLossHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPathLossHigh.setStatus("current")
_FsmScgPtpConformance_ObjectIdentity = ObjectIdentity
fsmScgPtpConformance = _FsmScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 3)
)
_FsmScgPtpCompliances_ObjectIdentity = ObjectIdentity
fsmScgPtpCompliances = _FsmScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 3, 1)
)
_FsmScgPtpGroups_ObjectIdentity = ObjectIdentity
fsmScgPtpGroups = _FsmScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 3, 2)
)

# Managed Objects groups

fsmScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 3, 2, 1)
)
fsmScgPtpGroup.setObjects(
      *(("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpPowerControlLoop"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpAvailableFreqSlotList"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpUsedFreqSlotList"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpPathLossCheckControlStatus"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpLastSuccessfullPathLossCheckTS"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpPathLoss"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpPathLossCheckDetectPort"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpLastPathLossCheckAttemptTS"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpLastPathLossCheckAttemptStatus"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpLastPathLossCheckFailedReason"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpTxEdfaPowerOffset"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpRxEdfaPowerOffset"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpTrafficMode"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpScgNumber"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpScgSupEqptType"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpMPOAID"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpProvisionedFPMPO"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpAutoDiscoveryState"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpDiscoveredNeighborTP"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpInterfaceType"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpProvisionedNeighborTP"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpProvisionedOpenWaveRemotePtp"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpPmHistStatsEnable"),
        ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpPathLossHigh"))
)
if mibBuilder.loadTexts:
    fsmScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsmScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 44, 3, 1, 1)
)
fsmScgPtpCompliance.setObjects(
    ("INFINERA-TP-FSMSCGPTP-MIB", "fsmScgPtpGroup")
)
if mibBuilder.loadTexts:
    fsmScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FSMSCGPTP-MIB",
    **{"fsmScgPtpMIB": fsmScgPtpMIB,
       "fsmScgPtpTable": fsmScgPtpTable,
       "fsmScgPtpEntry": fsmScgPtpEntry,
       "fsmScgPtpPowerControlLoop": fsmScgPtpPowerControlLoop,
       "fsmScgPtpAvailableFreqSlotList": fsmScgPtpAvailableFreqSlotList,
       "fsmScgPtpUsedFreqSlotList": fsmScgPtpUsedFreqSlotList,
       "fsmScgPtpPathLossCheckControlStatus": fsmScgPtpPathLossCheckControlStatus,
       "fsmScgPtpLastSuccessfullPathLossCheckTS": fsmScgPtpLastSuccessfullPathLossCheckTS,
       "fsmScgPtpPathLoss": fsmScgPtpPathLoss,
       "fsmScgPtpPathLossCheckDetectPort": fsmScgPtpPathLossCheckDetectPort,
       "fsmScgPtpLastPathLossCheckAttemptTS": fsmScgPtpLastPathLossCheckAttemptTS,
       "fsmScgPtpLastPathLossCheckAttemptStatus": fsmScgPtpLastPathLossCheckAttemptStatus,
       "fsmScgPtpLastPathLossCheckFailedReason": fsmScgPtpLastPathLossCheckFailedReason,
       "fsmScgPtpTxEdfaPowerOffset": fsmScgPtpTxEdfaPowerOffset,
       "fsmScgPtpRxEdfaPowerOffset": fsmScgPtpRxEdfaPowerOffset,
       "fsmScgPtpTrafficMode": fsmScgPtpTrafficMode,
       "fsmScgPtpScgNumber": fsmScgPtpScgNumber,
       "fsmScgPtpScgSupEqptType": fsmScgPtpScgSupEqptType,
       "fsmScgPtpMPOAID": fsmScgPtpMPOAID,
       "fsmScgPtpProvisionedFPMPO": fsmScgPtpProvisionedFPMPO,
       "fsmScgPtpAutoDiscoveryState": fsmScgPtpAutoDiscoveryState,
       "fsmScgPtpDiscoveredNeighborTP": fsmScgPtpDiscoveredNeighborTP,
       "fsmScgPtpInterfaceType": fsmScgPtpInterfaceType,
       "fsmScgPtpProvisionedOpenWaveRemotePtp": fsmScgPtpProvisionedOpenWaveRemotePtp,
       "fsmScgPtpPmHistStatsEnable": fsmScgPtpPmHistStatsEnable,
       "fsmScgPtpProvisionedNeighborTP": fsmScgPtpProvisionedNeighborTP,
       "fsmScgPtpPathLossHigh": fsmScgPtpPathLossHigh,
       "fsmScgPtpConformance": fsmScgPtpConformance,
       "fsmScgPtpCompliances": fsmScgPtpCompliances,
       "fsmScgPtpCompliance": fsmScgPtpCompliance,
       "fsmScgPtpGroups": fsmScgPtpGroups,
       "fsmScgPtpGroup": fsmScgPtpGroup}
)
