# SNMP MIB module (INFINERA-TP-CMMOCHPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-CMMOCHPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:46 2025
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
 InfnEnableDisableType,
 InfnModulationCategory,
 InfnPmHistStatsControl,
 InfnServiceType,
 InfnWaveInterfaceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnEnableDisableType",
    "InfnModulationCategory",
    "InfnPmHistStatsControl",
    "InfnServiceType",
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

cmmOchPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29)
)
if mibBuilder.loadTexts:
    cmmOchPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmmOchPtpTable_Object = MibTable
cmmOchPtpTable = _CmmOchPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1)
)
if mibBuilder.loadTexts:
    cmmOchPtpTable.setStatus("current")
_CmmOchPtpEntry_Object = MibTableRow
cmmOchPtpEntry = _CmmOchPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1)
)
cmmOchPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmmOchPtpEntry.setStatus("current")
_CmmOchPtpProvisionedOchOWPortId_Type = Integer32
_CmmOchPtpProvisionedOchOWPortId_Object = MibTableColumn
cmmOchPtpProvisionedOchOWPortId = _CmmOchPtpProvisionedOchOWPortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 1),
    _CmmOchPtpProvisionedOchOWPortId_Type()
)
cmmOchPtpProvisionedOchOWPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOchPtpProvisionedOchOWPortId.setStatus("current")


class _CmmOchPtpPmHistStatsEnable_Type(InfnPmHistStatsControl):
    """Custom type cmmOchPtpPmHistStatsEnable based on InfnPmHistStatsControl"""
    defaultValue = 1


_CmmOchPtpPmHistStatsEnable_Type.__name__ = "InfnPmHistStatsControl"
_CmmOchPtpPmHistStatsEnable_Object = MibTableColumn
cmmOchPtpPmHistStatsEnable = _CmmOchPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 2),
    _CmmOchPtpPmHistStatsEnable_Type()
)
cmmOchPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmOchPtpPmHistStatsEnable.setStatus("current")
_CmmOchPtpProvisionedOchPort_Type = DisplayString
_CmmOchPtpProvisionedOchPort_Object = MibTableColumn
cmmOchPtpProvisionedOchPort = _CmmOchPtpProvisionedOchPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 3),
    _CmmOchPtpProvisionedOchPort_Type()
)
cmmOchPtpProvisionedOchPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmOchPtpProvisionedOchPort.setStatus("current")
_CmmOchPtpDiscoveredOchPortId_Type = DisplayString
_CmmOchPtpDiscoveredOchPortId_Object = MibTableColumn
cmmOchPtpDiscoveredOchPortId = _CmmOchPtpDiscoveredOchPortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 4),
    _CmmOchPtpDiscoveredOchPortId_Type()
)
cmmOchPtpDiscoveredOchPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOchPtpDiscoveredOchPortId.setStatus("current")
_CmmOchPtpDiscoveredWavelength_Type = FloatHundredths
_CmmOchPtpDiscoveredWavelength_Object = MibTableColumn
cmmOchPtpDiscoveredWavelength = _CmmOchPtpDiscoveredWavelength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 5),
    _CmmOchPtpDiscoveredWavelength_Type()
)
cmmOchPtpDiscoveredWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOchPtpDiscoveredWavelength.setStatus("current")


class _CmmOchPtpWavelengthDetectedState_Type(Integer32):
    """Custom type cmmOchPtpWavelengthDetectedState based on Integer32"""
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
        *(("unknown", 1),
          ("notStarted", 2),
          ("failed", 3),
          ("notValid", 4),
          ("shutdown", 5),
          ("inprogress", 6),
          ("completed", 7))
    )


_CmmOchPtpWavelengthDetectedState_Type.__name__ = "Integer32"
_CmmOchPtpWavelengthDetectedState_Object = MibTableColumn
cmmOchPtpWavelengthDetectedState = _CmmOchPtpWavelengthDetectedState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 6),
    _CmmOchPtpWavelengthDetectedState_Type()
)
cmmOchPtpWavelengthDetectedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOchPtpWavelengthDetectedState.setStatus("current")
_CmmOchPtpInterfaceType_Type = InfnWaveInterfaceType
_CmmOchPtpInterfaceType_Object = MibTableColumn
cmmOchPtpInterfaceType = _CmmOchPtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 7),
    _CmmOchPtpInterfaceType_Type()
)
cmmOchPtpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmOchPtpInterfaceType.setStatus("current")


class _CmmOchPtpTargetPowerOffset_Type(FloatHundredths):
    """Custom type cmmOchPtpTargetPowerOffset based on FloatHundredths"""
    defaultValue = 0


_CmmOchPtpTargetPowerOffset_Type.__name__ = "FloatHundredths"
_CmmOchPtpTargetPowerOffset_Object = MibTableColumn
cmmOchPtpTargetPowerOffset = _CmmOchPtpTargetPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 8),
    _CmmOchPtpTargetPowerOffset_Type()
)
cmmOchPtpTargetPowerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOchPtpTargetPowerOffset.setStatus("current")


class _CmmOchPtpPowerControlLoop_Type(InfnEnableDisableType):
    """Custom type cmmOchPtpPowerControlLoop based on InfnEnableDisableType"""
    defaultValue = 2


_CmmOchPtpPowerControlLoop_Type.__name__ = "InfnEnableDisableType"
_CmmOchPtpPowerControlLoop_Object = MibTableColumn
cmmOchPtpPowerControlLoop = _CmmOchPtpPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 9),
    _CmmOchPtpPowerControlLoop_Type()
)
cmmOchPtpPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmOchPtpPowerControlLoop.setStatus("current")


class _CmmOchPtpModulationCatagory_Type(InfnModulationCategory):
    """Custom type cmmOchPtpModulationCatagory based on InfnModulationCategory"""
    defaultValue = 1


_CmmOchPtpModulationCatagory_Type.__name__ = "InfnModulationCategory"
_CmmOchPtpModulationCatagory_Object = MibTableColumn
cmmOchPtpModulationCatagory = _CmmOchPtpModulationCatagory_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 1, 1, 10),
    _CmmOchPtpModulationCatagory_Type()
)
cmmOchPtpModulationCatagory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmOchPtpModulationCatagory.setStatus("current")
_CmmOchPtpConformance_ObjectIdentity = ObjectIdentity
cmmOchPtpConformance = _CmmOchPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 3)
)
_CmmOchPtpCompliances_ObjectIdentity = ObjectIdentity
cmmOchPtpCompliances = _CmmOchPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 3, 1)
)
_CmmOchPtpGroups_ObjectIdentity = ObjectIdentity
cmmOchPtpGroups = _CmmOchPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 3, 2)
)

# Managed Objects groups

cmmOchPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 3, 2, 1)
)
cmmOchPtpGroup.setObjects(
      *(("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpProvisionedOchOWPortId"),
        ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpPmHistStatsEnable"),
        ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpProvisionedOchPort"),
        ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpDiscoveredOchPortId"),
        ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpDiscoveredWavelength"),
        ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpWavelengthDetectedState"),
        ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpInterfaceType"),
        ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpTargetPowerOffset"),
        ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpPowerControlLoop"),
        ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpModulationCatagory"))
)
if mibBuilder.loadTexts:
    cmmOchPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmmOchPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 29, 3, 1, 1)
)
cmmOchPtpCompliance.setObjects(
    ("INFINERA-TP-CMMOCHPTP-MIB", "cmmOchPtpGroup")
)
if mibBuilder.loadTexts:
    cmmOchPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-CMMOCHPTP-MIB",
    **{"cmmOchPtpMIB": cmmOchPtpMIB,
       "cmmOchPtpTable": cmmOchPtpTable,
       "cmmOchPtpEntry": cmmOchPtpEntry,
       "cmmOchPtpProvisionedOchOWPortId": cmmOchPtpProvisionedOchOWPortId,
       "cmmOchPtpPmHistStatsEnable": cmmOchPtpPmHistStatsEnable,
       "cmmOchPtpProvisionedOchPort": cmmOchPtpProvisionedOchPort,
       "cmmOchPtpDiscoveredOchPortId": cmmOchPtpDiscoveredOchPortId,
       "cmmOchPtpDiscoveredWavelength": cmmOchPtpDiscoveredWavelength,
       "cmmOchPtpWavelengthDetectedState": cmmOchPtpWavelengthDetectedState,
       "cmmOchPtpInterfaceType": cmmOchPtpInterfaceType,
       "cmmOchPtpTargetPowerOffset": cmmOchPtpTargetPowerOffset,
       "cmmOchPtpPowerControlLoop": cmmOchPtpPowerControlLoop,
       "cmmOchPtpModulationCatagory": cmmOchPtpModulationCatagory,
       "cmmOchPtpConformance": cmmOchPtpConformance,
       "cmmOchPtpCompliances": cmmOchPtpCompliances,
       "cmmOchPtpCompliance": cmmOchPtpCompliance,
       "cmmOchPtpGroups": cmmOchPtpGroups,
       "cmmOchPtpGroup": cmmOchPtpGroup}
)
