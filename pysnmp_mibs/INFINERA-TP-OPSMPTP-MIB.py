# SNMP MIB module (INFINERA-TP-OPSMPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OPSMPTP-MIB
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatTenths,
 InfnAdTpType,
 InfnEnableDisable,
 InfnEqptType,
 InfnPmHistStatsControl,
 InfnReporting,
 InfnSpanLossRange) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnAdTpType",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnPmHistStatsControl",
    "InfnReporting",
    "InfnSpanLossRange")

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

opsmPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61)
)
if mibBuilder.loadTexts:
    opsmPtpMIB.setRevisions(
        ("2015-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OpsmPtpTable_Object = MibTable
opsmPtpTable = _OpsmPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1)
)
if mibBuilder.loadTexts:
    opsmPtpTable.setStatus("current")
_OpsmPtpEntry_Object = MibTableRow
opsmPtpEntry = _OpsmPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1)
)
opsmPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    opsmPtpEntry.setStatus("current")
_OpsmPtpProvisionedNeighborTP_Type = DisplayString
_OpsmPtpProvisionedNeighborTP_Object = MibTableColumn
opsmPtpProvisionedNeighborTP = _OpsmPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 1),
    _OpsmPtpProvisionedNeighborTP_Type()
)
opsmPtpProvisionedNeighborTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpProvisionedNeighborTP.setStatus("current")
_OpsmPtpExpectedSpanLossRange_Type = InfnSpanLossRange
_OpsmPtpExpectedSpanLossRange_Object = MibTableColumn
opsmPtpExpectedSpanLossRange = _OpsmPtpExpectedSpanLossRange_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 2),
    _OpsmPtpExpectedSpanLossRange_Type()
)
opsmPtpExpectedSpanLossRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpExpectedSpanLossRange.setStatus("current")
_OpsmPtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_OpsmPtpPmHistStatsEnable_Object = MibTableColumn
opsmPtpPmHistStatsEnable = _OpsmPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 3),
    _OpsmPtpPmHistStatsEnable_Type()
)
opsmPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpPmHistStatsEnable.setStatus("current")
_OpsmPtpRxAssociatedPtp_Type = DisplayString
_OpsmPtpRxAssociatedPtp_Object = MibTableColumn
opsmPtpRxAssociatedPtp = _OpsmPtpRxAssociatedPtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 4),
    _OpsmPtpRxAssociatedPtp_Type()
)
opsmPtpRxAssociatedPtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpRxAssociatedPtp.setStatus("current")
_OpsmPtpRxAssociatedPtpType_Type = InfnAdTpType
_OpsmPtpRxAssociatedPtpType_Object = MibTableColumn
opsmPtpRxAssociatedPtpType = _OpsmPtpRxAssociatedPtpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 5),
    _OpsmPtpRxAssociatedPtpType_Type()
)
opsmPtpRxAssociatedPtpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmPtpRxAssociatedPtpType.setStatus("current")
_OpsmPtpTxAssociatedEqptType_Type = InfnEqptType
_OpsmPtpTxAssociatedEqptType_Object = MibTableColumn
opsmPtpTxAssociatedEqptType = _OpsmPtpTxAssociatedEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 6),
    _OpsmPtpTxAssociatedEqptType_Type()
)
opsmPtpTxAssociatedEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmPtpTxAssociatedEqptType.setStatus("current")
_OpsmPtpTxAssociatedPtp_Type = DisplayString
_OpsmPtpTxAssociatedPtp_Object = MibTableColumn
opsmPtpTxAssociatedPtp = _OpsmPtpTxAssociatedPtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 7),
    _OpsmPtpTxAssociatedPtp_Type()
)
opsmPtpTxAssociatedPtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpTxAssociatedPtp.setStatus("current")
_OpsmPtpTxAssociatedPtpType_Type = InfnAdTpType
_OpsmPtpTxAssociatedPtpType_Object = MibTableColumn
opsmPtpTxAssociatedPtpType = _OpsmPtpTxAssociatedPtpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 8),
    _OpsmPtpTxAssociatedPtpType_Type()
)
opsmPtpTxAssociatedPtpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpTxAssociatedPtpType.setStatus("current")
_OpsmPtpRxAssociatedEqptType_Type = InfnEqptType
_OpsmPtpRxAssociatedEqptType_Object = MibTableColumn
opsmPtpRxAssociatedEqptType = _OpsmPtpRxAssociatedEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 9),
    _OpsmPtpRxAssociatedEqptType_Type()
)
opsmPtpRxAssociatedEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmPtpRxAssociatedEqptType.setStatus("current")
_OpsmPtpSpanDistance_Type = FloatTenths
_OpsmPtpSpanDistance_Object = MibTableColumn
opsmPtpSpanDistance = _OpsmPtpSpanDistance_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 10),
    _OpsmPtpSpanDistance_Type()
)
opsmPtpSpanDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpSpanDistance.setStatus("current")
_OpsmPtpOlosThreshold_Type = FloatTenths
_OpsmPtpOlosThreshold_Object = MibTableColumn
opsmPtpOlosThreshold = _OpsmPtpOlosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 11),
    _OpsmPtpOlosThreshold_Type()
)
opsmPtpOlosThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpOlosThreshold.setStatus("current")
_OpsmPtpOlosSoakTimer_Type = Integer32
_OpsmPtpOlosSoakTimer_Object = MibTableColumn
opsmPtpOlosSoakTimer = _OpsmPtpOlosSoakTimer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 12),
    _OpsmPtpOlosSoakTimer_Type()
)
opsmPtpOlosSoakTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpOlosSoakTimer.setStatus("current")
_OpsmPtpOlosClearHysteresis_Type = FloatTenths
_OpsmPtpOlosClearHysteresis_Object = MibTableColumn
opsmPtpOlosClearHysteresis = _OpsmPtpOlosClearHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 13),
    _OpsmPtpOlosClearHysteresis_Type()
)
opsmPtpOlosClearHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpOlosClearHysteresis.setStatus("current")
_OpsmPtpRxPowerLevelLowThreshold_Type = FloatTenths
_OpsmPtpRxPowerLevelLowThreshold_Object = MibTableColumn
opsmPtpRxPowerLevelLowThreshold = _OpsmPtpRxPowerLevelLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 14),
    _OpsmPtpRxPowerLevelLowThreshold_Type()
)
opsmPtpRxPowerLevelLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpRxPowerLevelLowThreshold.setStatus("current")
_OpsmPtpRxPowerLevelLowThldReporting_Type = InfnReporting
_OpsmPtpRxPowerLevelLowThldReporting_Object = MibTableColumn
opsmPtpRxPowerLevelLowThldReporting = _OpsmPtpRxPowerLevelLowThldReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 15),
    _OpsmPtpRxPowerLevelLowThldReporting_Type()
)
opsmPtpRxPowerLevelLowThldReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpRxPowerLevelLowThldReporting.setStatus("current")
_OpsmPtpRxPowerLevelHighThreshold_Type = FloatTenths
_OpsmPtpRxPowerLevelHighThreshold_Object = MibTableColumn
opsmPtpRxPowerLevelHighThreshold = _OpsmPtpRxPowerLevelHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 16),
    _OpsmPtpRxPowerLevelHighThreshold_Type()
)
opsmPtpRxPowerLevelHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpRxPowerLevelHighThreshold.setStatus("current")
_OpsmPtpRxPowerLevelHighThldReporting_Type = InfnReporting
_OpsmPtpRxPowerLevelHighThldReporting_Object = MibTableColumn
opsmPtpRxPowerLevelHighThldReporting = _OpsmPtpRxPowerLevelHighThldReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 1, 1, 17),
    _OpsmPtpRxPowerLevelHighThldReporting_Type()
)
opsmPtpRxPowerLevelHighThldReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmPtpRxPowerLevelHighThldReporting.setStatus("current")
_OpsmPtpConformance_ObjectIdentity = ObjectIdentity
opsmPtpConformance = _OpsmPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 3)
)
_OpsmPtpCompliances_ObjectIdentity = ObjectIdentity
opsmPtpCompliances = _OpsmPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 3, 1)
)
_OpsmPtpGroups_ObjectIdentity = ObjectIdentity
opsmPtpGroups = _OpsmPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 3, 2)
)

# Managed Objects groups

opsmPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 3, 2, 1)
)
opsmPtpGroup.setObjects(
      *(("INFINERA-TP-OPSMPTP-MIB", "opsmPtpProvisionedNeighborTP"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpExpectedSpanLossRange"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpPmHistStatsEnable"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpRxAssociatedPtp"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpRxAssociatedPtpType"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpTxAssociatedEqptType"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpTxAssociatedPtp"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpTxAssociatedPtpType"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpRxAssociatedEqptType"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpSpanDistance"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpOlosThreshold"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpOlosSoakTimer"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpOlosClearHysteresis"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpRxPowerLevelLowThreshold"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpRxPowerLevelLowThldReporting"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpRxPowerLevelHighThreshold"),
        ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpRxPowerLevelHighThldReporting"))
)
if mibBuilder.loadTexts:
    opsmPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

opsmPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 61, 3, 1, 1)
)
opsmPtpCompliance.setObjects(
    ("INFINERA-TP-OPSMPTP-MIB", "opsmPtpGroup")
)
if mibBuilder.loadTexts:
    opsmPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OPSMPTP-MIB",
    **{"opsmPtpMIB": opsmPtpMIB,
       "opsmPtpTable": opsmPtpTable,
       "opsmPtpEntry": opsmPtpEntry,
       "opsmPtpProvisionedNeighborTP": opsmPtpProvisionedNeighborTP,
       "opsmPtpExpectedSpanLossRange": opsmPtpExpectedSpanLossRange,
       "opsmPtpPmHistStatsEnable": opsmPtpPmHistStatsEnable,
       "opsmPtpRxAssociatedPtp": opsmPtpRxAssociatedPtp,
       "opsmPtpRxAssociatedPtpType": opsmPtpRxAssociatedPtpType,
       "opsmPtpTxAssociatedEqptType": opsmPtpTxAssociatedEqptType,
       "opsmPtpTxAssociatedPtp": opsmPtpTxAssociatedPtp,
       "opsmPtpTxAssociatedPtpType": opsmPtpTxAssociatedPtpType,
       "opsmPtpRxAssociatedEqptType": opsmPtpRxAssociatedEqptType,
       "opsmPtpSpanDistance": opsmPtpSpanDistance,
       "opsmPtpOlosThreshold": opsmPtpOlosThreshold,
       "opsmPtpOlosSoakTimer": opsmPtpOlosSoakTimer,
       "opsmPtpOlosClearHysteresis": opsmPtpOlosClearHysteresis,
       "opsmPtpRxPowerLevelLowThreshold": opsmPtpRxPowerLevelLowThreshold,
       "opsmPtpRxPowerLevelLowThldReporting": opsmPtpRxPowerLevelLowThldReporting,
       "opsmPtpRxPowerLevelHighThreshold": opsmPtpRxPowerLevelHighThreshold,
       "opsmPtpRxPowerLevelHighThldReporting": opsmPtpRxPowerLevelHighThldReporting,
       "opsmPtpConformance": opsmPtpConformance,
       "opsmPtpCompliances": opsmPtpCompliances,
       "opsmPtpCompliance": opsmPtpCompliance,
       "opsmPtpGroups": opsmPtpGroups,
       "opsmPtpGroup": opsmPtpGroup}
)
