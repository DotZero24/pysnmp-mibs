# SNMP MIB module (INFINERA-TP-IDLERPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-IDLERPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:54 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

idlerPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84)
)
if mibBuilder.loadTexts:
    idlerPtpMIB.setRevisions(
        ("2017-05-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IdlerPtpTable_Object = MibTable
idlerPtpTable = _IdlerPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1)
)
if mibBuilder.loadTexts:
    idlerPtpTable.setStatus("current")
_IdlerPtpEntry_Object = MibTableRow
idlerPtpEntry = _IdlerPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1)
)
idlerPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    idlerPtpEntry.setStatus("current")
_IdlerPtpMoId_Type = DisplayString
_IdlerPtpMoId_Object = MibTableColumn
idlerPtpMoId = _IdlerPtpMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 1),
    _IdlerPtpMoId_Type()
)
idlerPtpMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpMoId.setStatus("current")
_IdlerPtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_IdlerPtpPmHistStatsEnable_Object = MibTableColumn
idlerPtpPmHistStatsEnable = _IdlerPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 2),
    _IdlerPtpPmHistStatsEnable_Type()
)
idlerPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpPmHistStatsEnable.setStatus("current")
_IdlerPtpTxAssociatedOtsEqptType_Type = InfnEqptType
_IdlerPtpTxAssociatedOtsEqptType_Object = MibTableColumn
idlerPtpTxAssociatedOtsEqptType = _IdlerPtpTxAssociatedOtsEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 3),
    _IdlerPtpTxAssociatedOtsEqptType_Type()
)
idlerPtpTxAssociatedOtsEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpTxAssociatedOtsEqptType.setStatus("current")
_IdlerPtpRxAssociatedOtsEqptType_Type = InfnEqptType
_IdlerPtpRxAssociatedOtsEqptType_Object = MibTableColumn
idlerPtpRxAssociatedOtsEqptType = _IdlerPtpRxAssociatedOtsEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 4),
    _IdlerPtpRxAssociatedOtsEqptType_Type()
)
idlerPtpRxAssociatedOtsEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpRxAssociatedOtsEqptType.setStatus("current")
_IdlerPtpOptOorLowThreshold_Type = FloatArbitraryPrecision
_IdlerPtpOptOorLowThreshold_Object = MibTableColumn
idlerPtpOptOorLowThreshold = _IdlerPtpOptOorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 5),
    _IdlerPtpOptOorLowThreshold_Type()
)
idlerPtpOptOorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpOptOorLowThreshold.setStatus("current")
_IdlerPtpOptOorHighThreshold_Type = FloatArbitraryPrecision
_IdlerPtpOptOorHighThreshold_Object = MibTableColumn
idlerPtpOptOorHighThreshold = _IdlerPtpOptOorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 6),
    _IdlerPtpOptOorHighThreshold_Type()
)
idlerPtpOptOorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpOptOorHighThreshold.setStatus("current")
_IdlerPtpOprOorLowThreshold_Type = FloatArbitraryPrecision
_IdlerPtpOprOorLowThreshold_Object = MibTableColumn
idlerPtpOprOorLowThreshold = _IdlerPtpOprOorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 7),
    _IdlerPtpOprOorLowThreshold_Type()
)
idlerPtpOprOorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpOprOorLowThreshold.setStatus("current")
_IdlerPtpOprOorHighThreshold_Type = FloatArbitraryPrecision
_IdlerPtpOprOorHighThreshold_Object = MibTableColumn
idlerPtpOprOorHighThreshold = _IdlerPtpOprOorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 8),
    _IdlerPtpOprOorHighThreshold_Type()
)
idlerPtpOprOorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpOprOorHighThreshold.setStatus("current")
_IdlerPtpPowerControlLoop_Type = InfnEnableDisableType
_IdlerPtpPowerControlLoop_Object = MibTableColumn
idlerPtpPowerControlLoop = _IdlerPtpPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 9),
    _IdlerPtpPowerControlLoop_Type()
)
idlerPtpPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpPowerControlLoop.setStatus("current")
_IdlerPtpTargetPower_Type = FloatArbitraryPrecision
_IdlerPtpTargetPower_Object = MibTableColumn
idlerPtpTargetPower = _IdlerPtpTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 10),
    _IdlerPtpTargetPower_Type()
)
idlerPtpTargetPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpTargetPower.setStatus("current")
_IdlerPtpShutterState_Type = InfnShutterState
_IdlerPtpShutterState_Object = MibTableColumn
idlerPtpShutterState = _IdlerPtpShutterState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 11),
    _IdlerPtpShutterState_Type()
)
idlerPtpShutterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpShutterState.setStatus("current")
_IdlerPtpAutoDiscovery_Type = InfnEnableDisableType
_IdlerPtpAutoDiscovery_Object = MibTableColumn
idlerPtpAutoDiscovery = _IdlerPtpAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 12),
    _IdlerPtpAutoDiscovery_Type()
)
idlerPtpAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpAutoDiscovery.setStatus("current")
_IdlerPtpOLOSThreshold_Type = FloatArbitraryPrecision
_IdlerPtpOLOSThreshold_Object = MibTableColumn
idlerPtpOLOSThreshold = _IdlerPtpOLOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 1, 1, 13),
    _IdlerPtpOLOSThreshold_Type()
)
idlerPtpOLOSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlerPtpOLOSThreshold.setStatus("current")
_IdlerPtpConformance_ObjectIdentity = ObjectIdentity
idlerPtpConformance = _IdlerPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 3)
)
_IdlerPtpCompliances_ObjectIdentity = ObjectIdentity
idlerPtpCompliances = _IdlerPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 3, 1)
)
_IdlerPtpGroups_ObjectIdentity = ObjectIdentity
idlerPtpGroups = _IdlerPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 3, 2)
)

# Managed Objects groups

idlerPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 3, 2, 1)
)
idlerPtpGroup.setObjects(
      *(("INFINERA-TP-IDLERPTP-MIB", "idlerPtpMoId"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpPmHistStatsEnable"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpTxAssociatedOtsEqptType"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpRxAssociatedOtsEqptType"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpOptOorLowThreshold"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpOptOorHighThreshold"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpOprOorLowThreshold"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpOprOorHighThreshold"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpPowerControlLoop"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpTargetPower"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpShutterState"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpAutoDiscovery"),
        ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpOLOSThreshold"))
)
if mibBuilder.loadTexts:
    idlerPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

idlerPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 84, 3, 1, 1)
)
idlerPtpCompliance.setObjects(
    ("INFINERA-TP-IDLERPTP-MIB", "idlerPtpGroup")
)
if mibBuilder.loadTexts:
    idlerPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-IDLERPTP-MIB",
    **{"idlerPtpMIB": idlerPtpMIB,
       "idlerPtpTable": idlerPtpTable,
       "idlerPtpEntry": idlerPtpEntry,
       "idlerPtpMoId": idlerPtpMoId,
       "idlerPtpPmHistStatsEnable": idlerPtpPmHistStatsEnable,
       "idlerPtpTxAssociatedOtsEqptType": idlerPtpTxAssociatedOtsEqptType,
       "idlerPtpRxAssociatedOtsEqptType": idlerPtpRxAssociatedOtsEqptType,
       "idlerPtpOptOorLowThreshold": idlerPtpOptOorLowThreshold,
       "idlerPtpOptOorHighThreshold": idlerPtpOptOorHighThreshold,
       "idlerPtpOprOorLowThreshold": idlerPtpOprOorLowThreshold,
       "idlerPtpOprOorHighThreshold": idlerPtpOprOorHighThreshold,
       "idlerPtpPowerControlLoop": idlerPtpPowerControlLoop,
       "idlerPtpTargetPower": idlerPtpTargetPower,
       "idlerPtpShutterState": idlerPtpShutterState,
       "idlerPtpAutoDiscovery": idlerPtpAutoDiscovery,
       "idlerPtpOLOSThreshold": idlerPtpOLOSThreshold,
       "idlerPtpConformance": idlerPtpConformance,
       "idlerPtpCompliances": idlerPtpCompliances,
       "idlerPtpCompliance": idlerPtpCompliance,
       "idlerPtpGroups": idlerPtpGroups,
       "idlerPtpGroup": idlerPtpGroup}
)
