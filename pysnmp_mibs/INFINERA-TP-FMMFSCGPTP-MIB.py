# SNMP MIB module (INFINERA-TP-FMMFSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FMMFSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:14 2025
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
 InfnInterfaceType,
 InfnPmHistStatsControl,
 InfnSpectrumType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnAdTpType",
    "InfnAutoDiscoveryState",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnInterfaceType",
    "InfnPmHistStatsControl",
    "InfnSpectrumType")

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

fmmFScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60)
)
if mibBuilder.loadTexts:
    fmmFScgPtpMIB.setRevisions(
        ("2015-05-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FmmFScgPtpTable_Object = MibTable
fmmFScgPtpTable = _FmmFScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1)
)
if mibBuilder.loadTexts:
    fmmFScgPtpTable.setStatus("current")
_FmmFScgPtpEntry_Object = MibTableRow
fmmFScgPtpEntry = _FmmFScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1)
)
fmmFScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fmmFScgPtpEntry.setStatus("current")
_FmmFScgPtpScgNumber_Type = Integer32
_FmmFScgPtpScgNumber_Object = MibTableColumn
fmmFScgPtpScgNumber = _FmmFScgPtpScgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 1),
    _FmmFScgPtpScgNumber_Type()
)
fmmFScgPtpScgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmFScgPtpScgNumber.setStatus("current")
_FmmFScgPtpScgSupEqptType_Type = InfnEqptType
_FmmFScgPtpScgSupEqptType_Object = MibTableColumn
fmmFScgPtpScgSupEqptType = _FmmFScgPtpScgSupEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 2),
    _FmmFScgPtpScgSupEqptType_Type()
)
fmmFScgPtpScgSupEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmFScgPtpScgSupEqptType.setStatus("current")
_FmmFScgPtpMPOAID_Type = DisplayString
_FmmFScgPtpMPOAID_Object = MibTableColumn
fmmFScgPtpMPOAID = _FmmFScgPtpMPOAID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 3),
    _FmmFScgPtpMPOAID_Type()
)
fmmFScgPtpMPOAID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmFScgPtpMPOAID.setStatus("current")
_FmmFScgPtpProvisionedFPMPO_Type = DisplayString
_FmmFScgPtpProvisionedFPMPO_Object = MibTableColumn
fmmFScgPtpProvisionedFPMPO = _FmmFScgPtpProvisionedFPMPO_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 4),
    _FmmFScgPtpProvisionedFPMPO_Type()
)
fmmFScgPtpProvisionedFPMPO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmFScgPtpProvisionedFPMPO.setStatus("current")
_FmmFScgPtpAutoDiscoveryState_Type = InfnAutoDiscoveryState
_FmmFScgPtpAutoDiscoveryState_Object = MibTableColumn
fmmFScgPtpAutoDiscoveryState = _FmmFScgPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 5),
    _FmmFScgPtpAutoDiscoveryState_Type()
)
fmmFScgPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmFScgPtpAutoDiscoveryState.setStatus("current")
_FmmFScgPtpDiscoveredNeighborTP_Type = DisplayString
_FmmFScgPtpDiscoveredNeighborTP_Object = MibTableColumn
fmmFScgPtpDiscoveredNeighborTP = _FmmFScgPtpDiscoveredNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 6),
    _FmmFScgPtpDiscoveredNeighborTP_Type()
)
fmmFScgPtpDiscoveredNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmFScgPtpDiscoveredNeighborTP.setStatus("current")
_FmmFScgPtpProvisionedNeighborTP_Type = DisplayString
_FmmFScgPtpProvisionedNeighborTP_Object = MibTableColumn
fmmFScgPtpProvisionedNeighborTP = _FmmFScgPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 7),
    _FmmFScgPtpProvisionedNeighborTP_Type()
)
fmmFScgPtpProvisionedNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmFScgPtpProvisionedNeighborTP.setStatus("current")
_FmmFScgPtpProvisionedNeighborAdTpType_Type = InfnAdTpType
_FmmFScgPtpProvisionedNeighborAdTpType_Object = MibTableColumn
fmmFScgPtpProvisionedNeighborAdTpType = _FmmFScgPtpProvisionedNeighborAdTpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 8),
    _FmmFScgPtpProvisionedNeighborAdTpType_Type()
)
fmmFScgPtpProvisionedNeighborAdTpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmFScgPtpProvisionedNeighborAdTpType.setStatus("current")
_FmmFScgPtpInterfaceType_Type = InfnInterfaceType
_FmmFScgPtpInterfaceType_Object = MibTableColumn
fmmFScgPtpInterfaceType = _FmmFScgPtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 9),
    _FmmFScgPtpInterfaceType_Type()
)
fmmFScgPtpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmFScgPtpInterfaceType.setStatus("current")
_FmmFScgPtpProvisionedOpenWaveRemotePtp_Type = DisplayString
_FmmFScgPtpProvisionedOpenWaveRemotePtp_Object = MibTableColumn
fmmFScgPtpProvisionedOpenWaveRemotePtp = _FmmFScgPtpProvisionedOpenWaveRemotePtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 10),
    _FmmFScgPtpProvisionedOpenWaveRemotePtp_Type()
)
fmmFScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmFScgPtpProvisionedOpenWaveRemotePtp.setStatus("current")
_FmmFScgPtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_FmmFScgPtpPmHistStatsEnable_Object = MibTableColumn
fmmFScgPtpPmHistStatsEnable = _FmmFScgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 11),
    _FmmFScgPtpPmHistStatsEnable_Type()
)
fmmFScgPtpPmHistStatsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmFScgPtpPmHistStatsEnable.setStatus("current")
_FmmFScgPtpPowerControlLoop_Type = InfnEnableDisable
_FmmFScgPtpPowerControlLoop_Object = MibTableColumn
fmmFScgPtpPowerControlLoop = _FmmFScgPtpPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 12),
    _FmmFScgPtpPowerControlLoop_Type()
)
fmmFScgPtpPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmFScgPtpPowerControlLoop.setStatus("current")
_FmmFScgPtpUsedFreqSlotList_Type = DisplayString
_FmmFScgPtpUsedFreqSlotList_Object = MibTableColumn
fmmFScgPtpUsedFreqSlotList = _FmmFScgPtpUsedFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 13),
    _FmmFScgPtpUsedFreqSlotList_Type()
)
fmmFScgPtpUsedFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmFScgPtpUsedFreqSlotList.setStatus("current")
_FmmFScgPtpProvisionedSpectrumType_Type = InfnSpectrumType
_FmmFScgPtpProvisionedSpectrumType_Object = MibTableColumn
fmmFScgPtpProvisionedSpectrumType = _FmmFScgPtpProvisionedSpectrumType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 14),
    _FmmFScgPtpProvisionedSpectrumType_Type()
)
fmmFScgPtpProvisionedSpectrumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmFScgPtpProvisionedSpectrumType.setStatus("current")
_FmmFScgPtpProvisionedSuperChannelNumber_Type = DisplayString
_FmmFScgPtpProvisionedSuperChannelNumber_Object = MibTableColumn
fmmFScgPtpProvisionedSuperChannelNumber = _FmmFScgPtpProvisionedSuperChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 15),
    _FmmFScgPtpProvisionedSuperChannelNumber_Type()
)
fmmFScgPtpProvisionedSuperChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmFScgPtpProvisionedSuperChannelNumber.setStatus("current")
_FmmFScgPtpAutoDiscSoakTime_Type = Integer32
_FmmFScgPtpAutoDiscSoakTime_Object = MibTableColumn
fmmFScgPtpAutoDiscSoakTime = _FmmFScgPtpAutoDiscSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 16),
    _FmmFScgPtpAutoDiscSoakTime_Type()
)
fmmFScgPtpAutoDiscSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmFScgPtpAutoDiscSoakTime.setStatus("current")
_FmmFScgPtpTargetRxPower_Type = FloatHundredths
_FmmFScgPtpTargetRxPower_Object = MibTableColumn
fmmFScgPtpTargetRxPower = _FmmFScgPtpTargetRxPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 1, 1, 17),
    _FmmFScgPtpTargetRxPower_Type()
)
fmmFScgPtpTargetRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmFScgPtpTargetRxPower.setStatus("current")
_FmmFScgPtpConformance_ObjectIdentity = ObjectIdentity
fmmFScgPtpConformance = _FmmFScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 3)
)
_FmmFScgPtpCompliances_ObjectIdentity = ObjectIdentity
fmmFScgPtpCompliances = _FmmFScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 3, 1)
)
_FmmFScgPtpGroups_ObjectIdentity = ObjectIdentity
fmmFScgPtpGroups = _FmmFScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 3, 2)
)

# Managed Objects groups

fmmFScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 3, 2, 1)
)
fmmFScgPtpGroup.setObjects(
      *(("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpScgNumber"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpScgSupEqptType"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpMPOAID"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpProvisionedFPMPO"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpAutoDiscoveryState"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpDiscoveredNeighborTP"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpInterfaceType"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpProvisionedNeighborTP"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpProvisionedNeighborAdTpType"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpPmHistStatsEnable"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpProvisionedOpenWaveRemotePtp"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpPowerControlLoop"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpUsedFreqSlotList"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpProvisionedSpectrumType"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpProvisionedSuperChannelNumber"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpAutoDiscSoakTime"),
        ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpTargetRxPower"))
)
if mibBuilder.loadTexts:
    fmmFScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmmFScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 60, 3, 1, 1)
)
fmmFScgPtpCompliance.setObjects(
    ("INFINERA-TP-FMMFSCGPTP-MIB", "fmmFScgPtpGroup")
)
if mibBuilder.loadTexts:
    fmmFScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FMMFSCGPTP-MIB",
    **{"fmmFScgPtpMIB": fmmFScgPtpMIB,
       "fmmFScgPtpTable": fmmFScgPtpTable,
       "fmmFScgPtpEntry": fmmFScgPtpEntry,
       "fmmFScgPtpScgNumber": fmmFScgPtpScgNumber,
       "fmmFScgPtpScgSupEqptType": fmmFScgPtpScgSupEqptType,
       "fmmFScgPtpMPOAID": fmmFScgPtpMPOAID,
       "fmmFScgPtpProvisionedFPMPO": fmmFScgPtpProvisionedFPMPO,
       "fmmFScgPtpAutoDiscoveryState": fmmFScgPtpAutoDiscoveryState,
       "fmmFScgPtpDiscoveredNeighborTP": fmmFScgPtpDiscoveredNeighborTP,
       "fmmFScgPtpProvisionedNeighborTP": fmmFScgPtpProvisionedNeighborTP,
       "fmmFScgPtpProvisionedNeighborAdTpType": fmmFScgPtpProvisionedNeighborAdTpType,
       "fmmFScgPtpInterfaceType": fmmFScgPtpInterfaceType,
       "fmmFScgPtpProvisionedOpenWaveRemotePtp": fmmFScgPtpProvisionedOpenWaveRemotePtp,
       "fmmFScgPtpPmHistStatsEnable": fmmFScgPtpPmHistStatsEnable,
       "fmmFScgPtpPowerControlLoop": fmmFScgPtpPowerControlLoop,
       "fmmFScgPtpUsedFreqSlotList": fmmFScgPtpUsedFreqSlotList,
       "fmmFScgPtpProvisionedSpectrumType": fmmFScgPtpProvisionedSpectrumType,
       "fmmFScgPtpProvisionedSuperChannelNumber": fmmFScgPtpProvisionedSuperChannelNumber,
       "fmmFScgPtpAutoDiscSoakTime": fmmFScgPtpAutoDiscSoakTime,
       "fmmFScgPtpTargetRxPower": fmmFScgPtpTargetRxPower,
       "fmmFScgPtpConformance": fmmFScgPtpConformance,
       "fmmFScgPtpCompliances": fmmFScgPtpCompliances,
       "fmmFScgPtpCompliance": fmmFScgPtpCompliance,
       "fmmFScgPtpGroups": fmmFScgPtpGroups,
       "fmmFScgPtpGroup": fmmFScgPtpGroup}
)
