# SNMP MIB module (INFINERA-TP-FBMSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FBMSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:43 2025
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
 InfnAdTpType,
 InfnEnableDisableType,
 InfnEqptType,
 InfnLastPathLossCheckAttemptStatus,
 InfnLastPathLossCheckFailedReason,
 InfnLineOperatingMode,
 InfnPathLossCheckControlStatus,
 InfnPmHistStatsControl,
 InfnWaveInterfaceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths",
    "InfnAdTpType",
    "InfnEnableDisableType",
    "InfnEqptType",
    "InfnLastPathLossCheckAttemptStatus",
    "InfnLastPathLossCheckFailedReason",
    "InfnLineOperatingMode",
    "InfnPathLossCheckControlStatus",
    "InfnPmHistStatsControl",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fbmScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81)
)
if mibBuilder.loadTexts:
    fbmScgPtpMIB.setRevisions(
        ("2016-01-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbmScgPtpTable_Object = MibTable
fbmScgPtpTable = _FbmScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1)
)
if mibBuilder.loadTexts:
    fbmScgPtpTable.setStatus("current")
_FbmScgPtpEntry_Object = MibTableRow
fbmScgPtpEntry = _FbmScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1)
)
fbmScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fbmScgPtpEntry.setStatus("current")
_FbmScgPtpMoId_Type = DisplayString
_FbmScgPtpMoId_Object = MibTableColumn
fbmScgPtpMoId = _FbmScgPtpMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 1),
    _FbmScgPtpMoId_Type()
)
fbmScgPtpMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmScgPtpMoId.setStatus("current")
_FbmScgPtpScgNumber_Type = Integer32
_FbmScgPtpScgNumber_Object = MibTableColumn
fbmScgPtpScgNumber = _FbmScgPtpScgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 2),
    _FbmScgPtpScgNumber_Type()
)
fbmScgPtpScgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpScgNumber.setStatus("current")
_FbmScgPtpScgSupEqptType_Type = InfnEqptType
_FbmScgPtpScgSupEqptType_Object = MibTableColumn
fbmScgPtpScgSupEqptType = _FbmScgPtpScgSupEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 3),
    _FbmScgPtpScgSupEqptType_Type()
)
fbmScgPtpScgSupEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmScgPtpScgSupEqptType.setStatus("current")
_FbmScgPtpMPOAID_Type = DisplayString
_FbmScgPtpMPOAID_Object = MibTableColumn
fbmScgPtpMPOAID = _FbmScgPtpMPOAID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 4),
    _FbmScgPtpMPOAID_Type()
)
fbmScgPtpMPOAID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmScgPtpMPOAID.setStatus("current")
_FbmScgPtpProvisionedFPMPO_Type = DisplayString
_FbmScgPtpProvisionedFPMPO_Object = MibTableColumn
fbmScgPtpProvisionedFPMPO = _FbmScgPtpProvisionedFPMPO_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 5),
    _FbmScgPtpProvisionedFPMPO_Type()
)
fbmScgPtpProvisionedFPMPO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmScgPtpProvisionedFPMPO.setStatus("current")
_FbmScgPtpDiscoveredNeighborTP_Type = DisplayString
_FbmScgPtpDiscoveredNeighborTP_Object = MibTableColumn
fbmScgPtpDiscoveredNeighborTP = _FbmScgPtpDiscoveredNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 6),
    _FbmScgPtpDiscoveredNeighborTP_Type()
)
fbmScgPtpDiscoveredNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpDiscoveredNeighborTP.setStatus("current")
_FbmScgPtpProvisionedNeighborTP_Type = DisplayString
_FbmScgPtpProvisionedNeighborTP_Object = MibTableColumn
fbmScgPtpProvisionedNeighborTP = _FbmScgPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 7),
    _FbmScgPtpProvisionedNeighborTP_Type()
)
fbmScgPtpProvisionedNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpProvisionedNeighborTP.setStatus("current")
_FbmScgPtpProvisionedNeighborAdTpType_Type = InfnAdTpType
_FbmScgPtpProvisionedNeighborAdTpType_Object = MibTableColumn
fbmScgPtpProvisionedNeighborAdTpType = _FbmScgPtpProvisionedNeighborAdTpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 8),
    _FbmScgPtpProvisionedNeighborAdTpType_Type()
)
fbmScgPtpProvisionedNeighborAdTpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpProvisionedNeighborAdTpType.setStatus("current")
_FbmScgPtpInterfaceType_Type = InfnWaveInterfaceType
_FbmScgPtpInterfaceType_Object = MibTableColumn
fbmScgPtpInterfaceType = _FbmScgPtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 9),
    _FbmScgPtpInterfaceType_Type()
)
fbmScgPtpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmScgPtpInterfaceType.setStatus("current")
_FbmScgPtpProvisionedOpenWaveRemotePtp_Type = DisplayString
_FbmScgPtpProvisionedOpenWaveRemotePtp_Object = MibTableColumn
fbmScgPtpProvisionedOpenWaveRemotePtp = _FbmScgPtpProvisionedOpenWaveRemotePtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 10),
    _FbmScgPtpProvisionedOpenWaveRemotePtp_Type()
)
fbmScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmScgPtpProvisionedOpenWaveRemotePtp.setStatus("current")
_FbmScgPtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_FbmScgPtpPmHistStatsEnable_Object = MibTableColumn
fbmScgPtpPmHistStatsEnable = _FbmScgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 11),
    _FbmScgPtpPmHistStatsEnable_Type()
)
fbmScgPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmScgPtpPmHistStatsEnable.setStatus("current")
_FbmScgPtpUsedFreqSlotList_Type = DisplayString
_FbmScgPtpUsedFreqSlotList_Object = MibTableColumn
fbmScgPtpUsedFreqSlotList = _FbmScgPtpUsedFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 12),
    _FbmScgPtpUsedFreqSlotList_Type()
)
fbmScgPtpUsedFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpUsedFreqSlotList.setStatus("current")
_FbmScgPtpAvailableFreqSlotList_Type = DisplayString
_FbmScgPtpAvailableFreqSlotList_Object = MibTableColumn
fbmScgPtpAvailableFreqSlotList = _FbmScgPtpAvailableFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 13),
    _FbmScgPtpAvailableFreqSlotList_Type()
)
fbmScgPtpAvailableFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpAvailableFreqSlotList.setStatus("current")
_FbmScgPtpLineOperatingMode_Type = InfnLineOperatingMode
_FbmScgPtpLineOperatingMode_Object = MibTableColumn
fbmScgPtpLineOperatingMode = _FbmScgPtpLineOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 14),
    _FbmScgPtpLineOperatingMode_Type()
)
fbmScgPtpLineOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmScgPtpLineOperatingMode.setStatus("current")
_FbmScgPtpPathLossCheckControlStatus_Type = InfnPathLossCheckControlStatus
_FbmScgPtpPathLossCheckControlStatus_Object = MibTableColumn
fbmScgPtpPathLossCheckControlStatus = _FbmScgPtpPathLossCheckControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 15),
    _FbmScgPtpPathLossCheckControlStatus_Type()
)
fbmScgPtpPathLossCheckControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpPathLossCheckControlStatus.setStatus("current")
_FbmScgPtpLastSuccessfullPathLossCheckTS_Type = Integer32
_FbmScgPtpLastSuccessfullPathLossCheckTS_Object = MibTableColumn
fbmScgPtpLastSuccessfullPathLossCheckTS = _FbmScgPtpLastSuccessfullPathLossCheckTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 16),
    _FbmScgPtpLastSuccessfullPathLossCheckTS_Type()
)
fbmScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpLastSuccessfullPathLossCheckTS.setStatus("current")
_FbmScgPtpPathLoss_Type = FloatArbitraryPrecision
_FbmScgPtpPathLoss_Object = MibTableColumn
fbmScgPtpPathLoss = _FbmScgPtpPathLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 17),
    _FbmScgPtpPathLoss_Type()
)
fbmScgPtpPathLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpPathLoss.setStatus("current")
_FbmScgPtpPathLossCheckDetectedPort_Type = DisplayString
_FbmScgPtpPathLossCheckDetectedPort_Object = MibTableColumn
fbmScgPtpPathLossCheckDetectedPort = _FbmScgPtpPathLossCheckDetectedPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 18),
    _FbmScgPtpPathLossCheckDetectedPort_Type()
)
fbmScgPtpPathLossCheckDetectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpPathLossCheckDetectedPort.setStatus("current")
_FbmScgPtpLastPathLossCheckAttemptTS_Type = Integer32
_FbmScgPtpLastPathLossCheckAttemptTS_Object = MibTableColumn
fbmScgPtpLastPathLossCheckAttemptTS = _FbmScgPtpLastPathLossCheckAttemptTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 19),
    _FbmScgPtpLastPathLossCheckAttemptTS_Type()
)
fbmScgPtpLastPathLossCheckAttemptTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpLastPathLossCheckAttemptTS.setStatus("current")
_FbmScgPtpLastPathLossCheckAttemptStatus_Type = InfnLastPathLossCheckAttemptStatus
_FbmScgPtpLastPathLossCheckAttemptStatus_Object = MibTableColumn
fbmScgPtpLastPathLossCheckAttemptStatus = _FbmScgPtpLastPathLossCheckAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 20),
    _FbmScgPtpLastPathLossCheckAttemptStatus_Type()
)
fbmScgPtpLastPathLossCheckAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpLastPathLossCheckAttemptStatus.setStatus("current")
_FbmScgPtpLastPathLossCheckFailedReason_Type = InfnLastPathLossCheckFailedReason
_FbmScgPtpLastPathLossCheckFailedReason_Object = MibTableColumn
fbmScgPtpLastPathLossCheckFailedReason = _FbmScgPtpLastPathLossCheckFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 1, 1, 21),
    _FbmScgPtpLastPathLossCheckFailedReason_Type()
)
fbmScgPtpLastPathLossCheckFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgPtpLastPathLossCheckFailedReason.setStatus("current")
_FbmScgPtpConformance_ObjectIdentity = ObjectIdentity
fbmScgPtpConformance = _FbmScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 3)
)
_FbmScgPtpCompliances_ObjectIdentity = ObjectIdentity
fbmScgPtpCompliances = _FbmScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 3, 1)
)
_FbmScgPtpGroups_ObjectIdentity = ObjectIdentity
fbmScgPtpGroups = _FbmScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 3, 2)
)

# Managed Objects groups

fbmScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 3, 2, 1)
)
fbmScgPtpGroup.setObjects(
      *(("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpMoId"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpScgNumber"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpScgSupEqptType"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpMPOAID"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpProvisionedFPMPO"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpDiscoveredNeighborTP"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpInterfaceType"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpProvisionedNeighborTP"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpProvisionedNeighborAdTpType"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpProvisionedOpenWaveRemotePtp"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpPmHistStatsEnable"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpUsedFreqSlotList"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpAvailableFreqSlotList"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpLineOperatingMode"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpPathLossCheckControlStatus"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpLastSuccessfullPathLossCheckTS"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpPathLoss"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpPathLossCheckDetectedPort"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpLastPathLossCheckAttemptTS"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpLastPathLossCheckAttemptStatus"),
        ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpLastPathLossCheckFailedReason"))
)
if mibBuilder.loadTexts:
    fbmScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fbmScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 81, 3, 1, 1)
)
fbmScgPtpCompliance.setObjects(
    ("INFINERA-TP-FBMSCGPTP-MIB", "fbmScgPtpGroup")
)
if mibBuilder.loadTexts:
    fbmScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FBMSCGPTP-MIB",
    **{"fbmScgPtpMIB": fbmScgPtpMIB,
       "fbmScgPtpTable": fbmScgPtpTable,
       "fbmScgPtpEntry": fbmScgPtpEntry,
       "fbmScgPtpMoId": fbmScgPtpMoId,
       "fbmScgPtpScgNumber": fbmScgPtpScgNumber,
       "fbmScgPtpScgSupEqptType": fbmScgPtpScgSupEqptType,
       "fbmScgPtpMPOAID": fbmScgPtpMPOAID,
       "fbmScgPtpProvisionedFPMPO": fbmScgPtpProvisionedFPMPO,
       "fbmScgPtpDiscoveredNeighborTP": fbmScgPtpDiscoveredNeighborTP,
       "fbmScgPtpProvisionedNeighborTP": fbmScgPtpProvisionedNeighborTP,
       "fbmScgPtpProvisionedNeighborAdTpType": fbmScgPtpProvisionedNeighborAdTpType,
       "fbmScgPtpInterfaceType": fbmScgPtpInterfaceType,
       "fbmScgPtpProvisionedOpenWaveRemotePtp": fbmScgPtpProvisionedOpenWaveRemotePtp,
       "fbmScgPtpPmHistStatsEnable": fbmScgPtpPmHistStatsEnable,
       "fbmScgPtpUsedFreqSlotList": fbmScgPtpUsedFreqSlotList,
       "fbmScgPtpAvailableFreqSlotList": fbmScgPtpAvailableFreqSlotList,
       "fbmScgPtpLineOperatingMode": fbmScgPtpLineOperatingMode,
       "fbmScgPtpPathLossCheckControlStatus": fbmScgPtpPathLossCheckControlStatus,
       "fbmScgPtpLastSuccessfullPathLossCheckTS": fbmScgPtpLastSuccessfullPathLossCheckTS,
       "fbmScgPtpPathLoss": fbmScgPtpPathLoss,
       "fbmScgPtpPathLossCheckDetectedPort": fbmScgPtpPathLossCheckDetectedPort,
       "fbmScgPtpLastPathLossCheckAttemptTS": fbmScgPtpLastPathLossCheckAttemptTS,
       "fbmScgPtpLastPathLossCheckAttemptStatus": fbmScgPtpLastPathLossCheckAttemptStatus,
       "fbmScgPtpLastPathLossCheckFailedReason": fbmScgPtpLastPathLossCheckFailedReason,
       "fbmScgPtpConformance": fbmScgPtpConformance,
       "fbmScgPtpCompliances": fbmScgPtpCompliances,
       "fbmScgPtpCompliance": fbmScgPtpCompliance,
       "fbmScgPtpGroups": fbmScgPtpGroups,
       "fbmScgPtpGroup": fbmScgPtpGroup}
)
