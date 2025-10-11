# SNMP MIB module (INFINERA-TP-ASEPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-ASEPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:46 2025
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
 InfnEnableDisableType,
 InfnEqptType,
 InfnPmHistStatsControl,
 InfnShutterState) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "InfnEnableDisableType",
    "InfnEqptType",
    "InfnPmHistStatsControl",
    "InfnShutterState")

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

asePtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83)
)
if mibBuilder.loadTexts:
    asePtpMIB.setRevisions(
        ("2017-05-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsePtpTable_Object = MibTable
asePtpTable = _AsePtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1)
)
if mibBuilder.loadTexts:
    asePtpTable.setStatus("current")
_AsePtpEntry_Object = MibTableRow
asePtpEntry = _AsePtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1)
)
asePtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    asePtpEntry.setStatus("current")
_AsePtpMoId_Type = DisplayString
_AsePtpMoId_Object = MibTableColumn
asePtpMoId = _AsePtpMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 1),
    _AsePtpMoId_Type()
)
asePtpMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpMoId.setStatus("current")
_AsePtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_AsePtpPmHistStatsEnable_Object = MibTableColumn
asePtpPmHistStatsEnable = _AsePtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 2),
    _AsePtpPmHistStatsEnable_Type()
)
asePtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpPmHistStatsEnable.setStatus("current")
_AsePtpRxProvNbrTP_Type = DisplayString
_AsePtpRxProvNbrTP_Object = MibTableColumn
asePtpRxProvNbrTP = _AsePtpRxProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 3),
    _AsePtpRxProvNbrTP_Type()
)
asePtpRxProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpRxProvNbrTP.setStatus("current")
_AsePtpTxProvNbrTP_Type = DisplayString
_AsePtpTxProvNbrTP_Object = MibTableColumn
asePtpTxProvNbrTP = _AsePtpTxProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 4),
    _AsePtpTxProvNbrTP_Type()
)
asePtpTxProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpTxProvNbrTP.setStatus("current")
_AsePtpTxProvEqptType_Type = InfnEqptType
_AsePtpTxProvEqptType_Object = MibTableColumn
asePtpTxProvEqptType = _AsePtpTxProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 5),
    _AsePtpTxProvEqptType_Type()
)
asePtpTxProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpTxProvEqptType.setStatus("current")
_AsePtpRxProvEqptType_Type = InfnEqptType
_AsePtpRxProvEqptType_Object = MibTableColumn
asePtpRxProvEqptType = _AsePtpRxProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 6),
    _AsePtpRxProvEqptType_Type()
)
asePtpRxProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpRxProvEqptType.setStatus("current")
_AsePtpTargetPower_Type = FloatArbitraryPrecision
_AsePtpTargetPower_Object = MibTableColumn
asePtpTargetPower = _AsePtpTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 7),
    _AsePtpTargetPower_Type()
)
asePtpTargetPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpTargetPower.setStatus("current")
_AsePtpOptOorLowThreshold_Type = FloatArbitraryPrecision
_AsePtpOptOorLowThreshold_Object = MibTableColumn
asePtpOptOorLowThreshold = _AsePtpOptOorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 8),
    _AsePtpOptOorLowThreshold_Type()
)
asePtpOptOorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpOptOorLowThreshold.setStatus("current")
_AsePtpOptOorHighThreshold_Type = FloatArbitraryPrecision
_AsePtpOptOorHighThreshold_Object = MibTableColumn
asePtpOptOorHighThreshold = _AsePtpOptOorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 9),
    _AsePtpOptOorHighThreshold_Type()
)
asePtpOptOorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpOptOorHighThreshold.setStatus("current")
_AsePtpOprOorLowThreshold_Type = FloatArbitraryPrecision
_AsePtpOprOorLowThreshold_Object = MibTableColumn
asePtpOprOorLowThreshold = _AsePtpOprOorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 10),
    _AsePtpOprOorLowThreshold_Type()
)
asePtpOprOorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpOprOorLowThreshold.setStatus("current")
_AsePtpOprOorHighThreshold_Type = FloatArbitraryPrecision
_AsePtpOprOorHighThreshold_Object = MibTableColumn
asePtpOprOorHighThreshold = _AsePtpOprOorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 11),
    _AsePtpOprOorHighThreshold_Type()
)
asePtpOprOorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpOprOorHighThreshold.setStatus("current")
_AsePtpPowerControlLoop_Type = InfnEnableDisableType
_AsePtpPowerControlLoop_Object = MibTableColumn
asePtpPowerControlLoop = _AsePtpPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 12),
    _AsePtpPowerControlLoop_Type()
)
asePtpPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpPowerControlLoop.setStatus("current")
_AsePtpOLOSThreshold_Type = FloatArbitraryPrecision
_AsePtpOLOSThreshold_Object = MibTableColumn
asePtpOLOSThreshold = _AsePtpOLOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 13),
    _AsePtpOLOSThreshold_Type()
)
asePtpOLOSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asePtpOLOSThreshold.setStatus("current")
_AsePtpShutterState_Type = InfnShutterState
_AsePtpShutterState_Object = MibTableColumn
asePtpShutterState = _AsePtpShutterState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 1, 1, 14),
    _AsePtpShutterState_Type()
)
asePtpShutterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpShutterState.setStatus("current")
_AsePtpConformance_ObjectIdentity = ObjectIdentity
asePtpConformance = _AsePtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 3)
)
_AsePtpCompliances_ObjectIdentity = ObjectIdentity
asePtpCompliances = _AsePtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 3, 1)
)
_AsePtpGroups_ObjectIdentity = ObjectIdentity
asePtpGroups = _AsePtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 3, 2)
)

# Managed Objects groups

asePtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 3, 2, 1)
)
asePtpGroup.setObjects(
      *(("INFINERA-TP-ASEPTP-MIB", "asePtpMoId"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpPmHistStatsEnable"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpRxProvNbrTP"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpTxProvNbrTP"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpTxProvEqptType"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpRxProvEqptType"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpTargetPower"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpOptOorLowThreshold"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpOptOorHighThreshold"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpOprOorLowThreshold"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpOprOorHighThreshold"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpPowerControlLoop"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpOLOSThreshold"),
        ("INFINERA-TP-ASEPTP-MIB", "asePtpShutterState"))
)
if mibBuilder.loadTexts:
    asePtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

asePtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 83, 3, 1, 1)
)
asePtpCompliance.setObjects(
    ("INFINERA-TP-ASEPTP-MIB", "asePtpGroup")
)
if mibBuilder.loadTexts:
    asePtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-ASEPTP-MIB",
    **{"asePtpMIB": asePtpMIB,
       "asePtpTable": asePtpTable,
       "asePtpEntry": asePtpEntry,
       "asePtpMoId": asePtpMoId,
       "asePtpPmHistStatsEnable": asePtpPmHistStatsEnable,
       "asePtpRxProvNbrTP": asePtpRxProvNbrTP,
       "asePtpTxProvNbrTP": asePtpTxProvNbrTP,
       "asePtpTxProvEqptType": asePtpTxProvEqptType,
       "asePtpRxProvEqptType": asePtpRxProvEqptType,
       "asePtpTargetPower": asePtpTargetPower,
       "asePtpOptOorLowThreshold": asePtpOptOorLowThreshold,
       "asePtpOptOorHighThreshold": asePtpOptOorHighThreshold,
       "asePtpOprOorLowThreshold": asePtpOprOorLowThreshold,
       "asePtpOprOorHighThreshold": asePtpOprOorHighThreshold,
       "asePtpPowerControlLoop": asePtpPowerControlLoop,
       "asePtpOLOSThreshold": asePtpOLOSThreshold,
       "asePtpShutterState": asePtpShutterState,
       "asePtpConformance": asePtpConformance,
       "asePtpCompliances": asePtpCompliances,
       "asePtpCompliance": asePtpCompliance,
       "asePtpGroups": asePtpGroups,
       "asePtpGroup": asePtpGroup}
)
