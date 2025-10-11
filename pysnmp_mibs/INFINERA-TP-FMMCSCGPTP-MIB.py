# SNMP MIB module (INFINERA-TP-FMMCSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FMMCSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:21 2025
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
 FloatTenths,
 InfnAdTpType,
 InfnAutoDiscoveryState,
 InfnEnableDisable,
 InfnEqptType,
 InfnPmHistStatsControl,
 InfnWaveInterfaceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "FloatTenths",
    "InfnAdTpType",
    "InfnAutoDiscoveryState",
    "InfnEnableDisable",
    "InfnEqptType",
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

fmmCScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63)
)
if mibBuilder.loadTexts:
    fmmCScgPtpMIB.setRevisions(
        ("2015-05-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FmmC5ScgPtpTable_Object = MibTable
fmmC5ScgPtpTable = _FmmC5ScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1)
)
if mibBuilder.loadTexts:
    fmmC5ScgPtpTable.setStatus("current")
_FmmC5ScgPtpEntry_Object = MibTableRow
fmmC5ScgPtpEntry = _FmmC5ScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1)
)
fmmC5ScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fmmC5ScgPtpEntry.setStatus("current")
_FmmC5ScgPtpScgNumber_Type = Integer32
_FmmC5ScgPtpScgNumber_Object = MibTableColumn
fmmC5ScgPtpScgNumber = _FmmC5ScgPtpScgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 1),
    _FmmC5ScgPtpScgNumber_Type()
)
fmmC5ScgPtpScgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC5ScgPtpScgNumber.setStatus("current")
_FmmC5ScgPtpScgSupEqptType_Type = InfnEqptType
_FmmC5ScgPtpScgSupEqptType_Object = MibTableColumn
fmmC5ScgPtpScgSupEqptType = _FmmC5ScgPtpScgSupEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 2),
    _FmmC5ScgPtpScgSupEqptType_Type()
)
fmmC5ScgPtpScgSupEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC5ScgPtpScgSupEqptType.setStatus("current")
_FmmC5ScgPtpAutoDiscoveryState_Type = InfnAutoDiscoveryState
_FmmC5ScgPtpAutoDiscoveryState_Object = MibTableColumn
fmmC5ScgPtpAutoDiscoveryState = _FmmC5ScgPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 3),
    _FmmC5ScgPtpAutoDiscoveryState_Type()
)
fmmC5ScgPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC5ScgPtpAutoDiscoveryState.setStatus("current")
_FmmC5ScgPtpDiscoveredNeighborTP_Type = DisplayString
_FmmC5ScgPtpDiscoveredNeighborTP_Object = MibTableColumn
fmmC5ScgPtpDiscoveredNeighborTP = _FmmC5ScgPtpDiscoveredNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 4),
    _FmmC5ScgPtpDiscoveredNeighborTP_Type()
)
fmmC5ScgPtpDiscoveredNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC5ScgPtpDiscoveredNeighborTP.setStatus("current")
_FmmC5ScgPtpProvisionedNeighborTP_Type = DisplayString
_FmmC5ScgPtpProvisionedNeighborTP_Object = MibTableColumn
fmmC5ScgPtpProvisionedNeighborTP = _FmmC5ScgPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 5),
    _FmmC5ScgPtpProvisionedNeighborTP_Type()
)
fmmC5ScgPtpProvisionedNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC5ScgPtpProvisionedNeighborTP.setStatus("current")
_FmmC5ScgPtpProvisionedNeighborAdTpType_Type = InfnAdTpType
_FmmC5ScgPtpProvisionedNeighborAdTpType_Object = MibTableColumn
fmmC5ScgPtpProvisionedNeighborAdTpType = _FmmC5ScgPtpProvisionedNeighborAdTpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 6),
    _FmmC5ScgPtpProvisionedNeighborAdTpType_Type()
)
fmmC5ScgPtpProvisionedNeighborAdTpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC5ScgPtpProvisionedNeighborAdTpType.setStatus("current")
_FmmC5ScgPtpInterfaceType_Type = InfnWaveInterfaceType
_FmmC5ScgPtpInterfaceType_Object = MibTableColumn
fmmC5ScgPtpInterfaceType = _FmmC5ScgPtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 7),
    _FmmC5ScgPtpInterfaceType_Type()
)
fmmC5ScgPtpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC5ScgPtpInterfaceType.setStatus("current")
_FmmC5ScgPtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_FmmC5ScgPtpPmHistStatsEnable_Object = MibTableColumn
fmmC5ScgPtpPmHistStatsEnable = _FmmC5ScgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 8),
    _FmmC5ScgPtpPmHistStatsEnable_Type()
)
fmmC5ScgPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC5ScgPtpPmHistStatsEnable.setStatus("current")
_FmmC5ScgPtpUsedFreqSlotList_Type = DisplayString
_FmmC5ScgPtpUsedFreqSlotList_Object = MibTableColumn
fmmC5ScgPtpUsedFreqSlotList = _FmmC5ScgPtpUsedFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 9),
    _FmmC5ScgPtpUsedFreqSlotList_Type()
)
fmmC5ScgPtpUsedFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC5ScgPtpUsedFreqSlotList.setStatus("current")
_FmmC5ScgPtpAvailableFreqSlotList_Type = DisplayString
_FmmC5ScgPtpAvailableFreqSlotList_Object = MibTableColumn
fmmC5ScgPtpAvailableFreqSlotList = _FmmC5ScgPtpAvailableFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 10),
    _FmmC5ScgPtpAvailableFreqSlotList_Type()
)
fmmC5ScgPtpAvailableFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC5ScgPtpAvailableFreqSlotList.setStatus("current")
_FmmC5ScgPtpAutoDiscSoakTime_Type = Integer32
_FmmC5ScgPtpAutoDiscSoakTime_Object = MibTableColumn
fmmC5ScgPtpAutoDiscSoakTime = _FmmC5ScgPtpAutoDiscSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 11),
    _FmmC5ScgPtpAutoDiscSoakTime_Type()
)
fmmC5ScgPtpAutoDiscSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC5ScgPtpAutoDiscSoakTime.setStatus("current")
_FmmC5ScgPtpTxPowerOffset_Type = FloatTenths
_FmmC5ScgPtpTxPowerOffset_Object = MibTableColumn
fmmC5ScgPtpTxPowerOffset = _FmmC5ScgPtpTxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 12),
    _FmmC5ScgPtpTxPowerOffset_Type()
)
fmmC5ScgPtpTxPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC5ScgPtpTxPowerOffset.setStatus("current")
_FmmC5ScgPtpAllowedPassBandList_Type = DisplayString
_FmmC5ScgPtpAllowedPassBandList_Object = MibTableColumn
fmmC5ScgPtpAllowedPassBandList = _FmmC5ScgPtpAllowedPassBandList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 13),
    _FmmC5ScgPtpAllowedPassBandList_Type()
)
fmmC5ScgPtpAllowedPassBandList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC5ScgPtpAllowedPassBandList.setStatus("current")
_FmmC5ScgPtpPassiveMirrorProvNeighborTP_Type = DisplayString
_FmmC5ScgPtpPassiveMirrorProvNeighborTP_Object = MibTableColumn
fmmC5ScgPtpPassiveMirrorProvNeighborTP = _FmmC5ScgPtpPassiveMirrorProvNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 14),
    _FmmC5ScgPtpPassiveMirrorProvNeighborTP_Type()
)
fmmC5ScgPtpPassiveMirrorProvNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC5ScgPtpPassiveMirrorProvNeighborTP.setStatus("current")
_FmmC5ScgPtpRxPowerOffset_Type = FloatTenths
_FmmC5ScgPtpRxPowerOffset_Object = MibTableColumn
fmmC5ScgPtpRxPowerOffset = _FmmC5ScgPtpRxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 1, 1, 15),
    _FmmC5ScgPtpRxPowerOffset_Type()
)
fmmC5ScgPtpRxPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC5ScgPtpRxPowerOffset.setStatus("current")
_FmmC12ScgPtpTable_Object = MibTable
fmmC12ScgPtpTable = _FmmC12ScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2)
)
if mibBuilder.loadTexts:
    fmmC12ScgPtpTable.setStatus("current")
_FmmC12ScgPtpEntry_Object = MibTableRow
fmmC12ScgPtpEntry = _FmmC12ScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1)
)
fmmC12ScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fmmC12ScgPtpEntry.setStatus("current")
_FmmC12ScgPtpScgNumber_Type = Integer32
_FmmC12ScgPtpScgNumber_Object = MibTableColumn
fmmC12ScgPtpScgNumber = _FmmC12ScgPtpScgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 1),
    _FmmC12ScgPtpScgNumber_Type()
)
fmmC12ScgPtpScgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC12ScgPtpScgNumber.setStatus("current")
_FmmC12ScgPtpScgSupEqptType_Type = InfnEqptType
_FmmC12ScgPtpScgSupEqptType_Object = MibTableColumn
fmmC12ScgPtpScgSupEqptType = _FmmC12ScgPtpScgSupEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 2),
    _FmmC12ScgPtpScgSupEqptType_Type()
)
fmmC12ScgPtpScgSupEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC12ScgPtpScgSupEqptType.setStatus("current")
_FmmC12ScgPtpAutoDiscoveryState_Type = InfnAutoDiscoveryState
_FmmC12ScgPtpAutoDiscoveryState_Object = MibTableColumn
fmmC12ScgPtpAutoDiscoveryState = _FmmC12ScgPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 3),
    _FmmC12ScgPtpAutoDiscoveryState_Type()
)
fmmC12ScgPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC12ScgPtpAutoDiscoveryState.setStatus("current")
_FmmC12ScgPtpDiscoveredNeighborTP_Type = DisplayString
_FmmC12ScgPtpDiscoveredNeighborTP_Object = MibTableColumn
fmmC12ScgPtpDiscoveredNeighborTP = _FmmC12ScgPtpDiscoveredNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 4),
    _FmmC12ScgPtpDiscoveredNeighborTP_Type()
)
fmmC12ScgPtpDiscoveredNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC12ScgPtpDiscoveredNeighborTP.setStatus("current")
_FmmC12ScgPtpProvisionedNeighborTP_Type = DisplayString
_FmmC12ScgPtpProvisionedNeighborTP_Object = MibTableColumn
fmmC12ScgPtpProvisionedNeighborTP = _FmmC12ScgPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 5),
    _FmmC12ScgPtpProvisionedNeighborTP_Type()
)
fmmC12ScgPtpProvisionedNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC12ScgPtpProvisionedNeighborTP.setStatus("current")
_FmmC12ScgPtpProvisionedNeighborAdTpType_Type = InfnAdTpType
_FmmC12ScgPtpProvisionedNeighborAdTpType_Object = MibTableColumn
fmmC12ScgPtpProvisionedNeighborAdTpType = _FmmC12ScgPtpProvisionedNeighborAdTpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 6),
    _FmmC12ScgPtpProvisionedNeighborAdTpType_Type()
)
fmmC12ScgPtpProvisionedNeighborAdTpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC12ScgPtpProvisionedNeighborAdTpType.setStatus("current")
_FmmC12ScgPtpInterfaceType_Type = InfnWaveInterfaceType
_FmmC12ScgPtpInterfaceType_Object = MibTableColumn
fmmC12ScgPtpInterfaceType = _FmmC12ScgPtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 7),
    _FmmC12ScgPtpInterfaceType_Type()
)
fmmC12ScgPtpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC12ScgPtpInterfaceType.setStatus("current")
_FmmC12ScgPtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_FmmC12ScgPtpPmHistStatsEnable_Object = MibTableColumn
fmmC12ScgPtpPmHistStatsEnable = _FmmC12ScgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 8),
    _FmmC12ScgPtpPmHistStatsEnable_Type()
)
fmmC12ScgPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC12ScgPtpPmHistStatsEnable.setStatus("current")
_FmmC12ScgPtpUsedFreqSlotList_Type = DisplayString
_FmmC12ScgPtpUsedFreqSlotList_Object = MibTableColumn
fmmC12ScgPtpUsedFreqSlotList = _FmmC12ScgPtpUsedFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 9),
    _FmmC12ScgPtpUsedFreqSlotList_Type()
)
fmmC12ScgPtpUsedFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC12ScgPtpUsedFreqSlotList.setStatus("current")
_FmmC12ScgPtpAvailableFreqSlotList_Type = DisplayString
_FmmC12ScgPtpAvailableFreqSlotList_Object = MibTableColumn
fmmC12ScgPtpAvailableFreqSlotList = _FmmC12ScgPtpAvailableFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 10),
    _FmmC12ScgPtpAvailableFreqSlotList_Type()
)
fmmC12ScgPtpAvailableFreqSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC12ScgPtpAvailableFreqSlotList.setStatus("current")
_FmmC12ScgPtpAllowedPassBandList_Type = DisplayString
_FmmC12ScgPtpAllowedPassBandList_Object = MibTableColumn
fmmC12ScgPtpAllowedPassBandList = _FmmC12ScgPtpAllowedPassBandList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 11),
    _FmmC12ScgPtpAllowedPassBandList_Type()
)
fmmC12ScgPtpAllowedPassBandList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC12ScgPtpAllowedPassBandList.setStatus("current")
_FmmC12ScgPtpPassiveMirrorProvNeighborTP_Type = DisplayString
_FmmC12ScgPtpPassiveMirrorProvNeighborTP_Object = MibTableColumn
fmmC12ScgPtpPassiveMirrorProvNeighborTP = _FmmC12ScgPtpPassiveMirrorProvNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 12),
    _FmmC12ScgPtpPassiveMirrorProvNeighborTP_Type()
)
fmmC12ScgPtpPassiveMirrorProvNeighborTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmC12ScgPtpPassiveMirrorProvNeighborTP.setStatus("current")
_FmmC12ScgPtpRxPowerOffset_Type = FloatTenths
_FmmC12ScgPtpRxPowerOffset_Object = MibTableColumn
fmmC12ScgPtpRxPowerOffset = _FmmC12ScgPtpRxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 2, 1, 13),
    _FmmC12ScgPtpRxPowerOffset_Type()
)
fmmC12ScgPtpRxPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmmC12ScgPtpRxPowerOffset.setStatus("current")
_FmmCScgPtpConformance_ObjectIdentity = ObjectIdentity
fmmCScgPtpConformance = _FmmCScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 3)
)
_FmmCScgPtpCompliances_ObjectIdentity = ObjectIdentity
fmmCScgPtpCompliances = _FmmCScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 3, 1)
)
_FmmCScgPtpGroups_ObjectIdentity = ObjectIdentity
fmmCScgPtpGroups = _FmmCScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 3, 2)
)

# Managed Objects groups

fmmC5ScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 3, 2, 1)
)
fmmC5ScgPtpGroup.setObjects(
      *(("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpScgNumber"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpScgSupEqptType"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpAutoDiscoveryState"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpDiscoveredNeighborTP"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpInterfaceType"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpProvisionedNeighborTP"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpProvisionedNeighborAdTpType"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpPmHistStatsEnable"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpUsedFreqSlotList"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpAvailableFreqSlotList"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpAutoDiscSoakTime"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpTxPowerOffset"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpAllowedPassBandList"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpPassiveMirrorProvNeighborTP"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpRxPowerOffset"))
)
if mibBuilder.loadTexts:
    fmmC5ScgPtpGroup.setStatus("current")

fmmC12ScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 3, 2, 2)
)
fmmC12ScgPtpGroup.setObjects(
      *(("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpScgNumber"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpScgSupEqptType"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpAutoDiscoveryState"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpDiscoveredNeighborTP"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpInterfaceType"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpProvisionedNeighborTP"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpProvisionedNeighborAdTpType"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpPmHistStatsEnable"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpUsedFreqSlotList"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpAvailableFreqSlotList"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpPassiveMirrorProvNeighborTP"),
        ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpRxPowerOffset"))
)
if mibBuilder.loadTexts:
    fmmC12ScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmmCScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 3, 1, 1)
)
fmmCScgPtpCompliance.setObjects(
    ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC5ScgPtpGroup")
)
if mibBuilder.loadTexts:
    fmmCScgPtpCompliance.setStatus(
        "current"
    )

fmmC12ScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 63, 3, 1, 2)
)
fmmC12ScgPtpCompliance.setObjects(
    ("INFINERA-TP-FMMCSCGPTP-MIB", "fmmC12ScgPtpGroup")
)
if mibBuilder.loadTexts:
    fmmC12ScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FMMCSCGPTP-MIB",
    **{"fmmCScgPtpMIB": fmmCScgPtpMIB,
       "fmmC5ScgPtpTable": fmmC5ScgPtpTable,
       "fmmC5ScgPtpEntry": fmmC5ScgPtpEntry,
       "fmmC5ScgPtpScgNumber": fmmC5ScgPtpScgNumber,
       "fmmC5ScgPtpScgSupEqptType": fmmC5ScgPtpScgSupEqptType,
       "fmmC5ScgPtpAutoDiscoveryState": fmmC5ScgPtpAutoDiscoveryState,
       "fmmC5ScgPtpDiscoveredNeighborTP": fmmC5ScgPtpDiscoveredNeighborTP,
       "fmmC5ScgPtpProvisionedNeighborTP": fmmC5ScgPtpProvisionedNeighborTP,
       "fmmC5ScgPtpProvisionedNeighborAdTpType": fmmC5ScgPtpProvisionedNeighborAdTpType,
       "fmmC5ScgPtpInterfaceType": fmmC5ScgPtpInterfaceType,
       "fmmC5ScgPtpPmHistStatsEnable": fmmC5ScgPtpPmHistStatsEnable,
       "fmmC5ScgPtpUsedFreqSlotList": fmmC5ScgPtpUsedFreqSlotList,
       "fmmC5ScgPtpAvailableFreqSlotList": fmmC5ScgPtpAvailableFreqSlotList,
       "fmmC5ScgPtpAutoDiscSoakTime": fmmC5ScgPtpAutoDiscSoakTime,
       "fmmC5ScgPtpTxPowerOffset": fmmC5ScgPtpTxPowerOffset,
       "fmmC5ScgPtpAllowedPassBandList": fmmC5ScgPtpAllowedPassBandList,
       "fmmC5ScgPtpPassiveMirrorProvNeighborTP": fmmC5ScgPtpPassiveMirrorProvNeighborTP,
       "fmmC5ScgPtpRxPowerOffset": fmmC5ScgPtpRxPowerOffset,
       "fmmC12ScgPtpTable": fmmC12ScgPtpTable,
       "fmmC12ScgPtpEntry": fmmC12ScgPtpEntry,
       "fmmC12ScgPtpScgNumber": fmmC12ScgPtpScgNumber,
       "fmmC12ScgPtpScgSupEqptType": fmmC12ScgPtpScgSupEqptType,
       "fmmC12ScgPtpAutoDiscoveryState": fmmC12ScgPtpAutoDiscoveryState,
       "fmmC12ScgPtpDiscoveredNeighborTP": fmmC12ScgPtpDiscoveredNeighborTP,
       "fmmC12ScgPtpProvisionedNeighborTP": fmmC12ScgPtpProvisionedNeighborTP,
       "fmmC12ScgPtpProvisionedNeighborAdTpType": fmmC12ScgPtpProvisionedNeighborAdTpType,
       "fmmC12ScgPtpInterfaceType": fmmC12ScgPtpInterfaceType,
       "fmmC12ScgPtpPmHistStatsEnable": fmmC12ScgPtpPmHistStatsEnable,
       "fmmC12ScgPtpUsedFreqSlotList": fmmC12ScgPtpUsedFreqSlotList,
       "fmmC12ScgPtpAvailableFreqSlotList": fmmC12ScgPtpAvailableFreqSlotList,
       "fmmC12ScgPtpAllowedPassBandList": fmmC12ScgPtpAllowedPassBandList,
       "fmmC12ScgPtpPassiveMirrorProvNeighborTP": fmmC12ScgPtpPassiveMirrorProvNeighborTP,
       "fmmC12ScgPtpRxPowerOffset": fmmC12ScgPtpRxPowerOffset,
       "fmmCScgPtpConformance": fmmCScgPtpConformance,
       "fmmCScgPtpCompliances": fmmCScgPtpCompliances,
       "fmmCScgPtpCompliance": fmmCScgPtpCompliance,
       "fmmC12ScgPtpCompliance": fmmC12ScgPtpCompliance,
       "fmmCScgPtpGroups": fmmCScgPtpGroups,
       "fmmC5ScgPtpGroup": fmmC5ScgPtpGroup,
       "fmmC12ScgPtpGroup": fmmC12ScgPtpGroup}
)
