# SNMP MIB module (INFINERA-TP-PXPW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXPW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:51 2025
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
 InfnCreationType,
 InfnFlapActionClear,
 InfnPWSetupMode,
 InfnPmHistStatsControl) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "FloatTenths",
    "InfnCreationType",
    "InfnFlapActionClear",
    "InfnPWSetupMode",
    "InfnPmHistStatsControl")

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

pxmPwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75)
)
if mibBuilder.loadTexts:
    pxmPwMIB.setRevisions(
        ("2016-05-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmPwTable_Object = MibTable
pxmPwTable = _PxmPwTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1)
)
if mibBuilder.loadTexts:
    pxmPwTable.setStatus("current")
_PxmPwEntry_Object = MibTableRow
pxmPwEntry = _PxmPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1)
)
pxmPwEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmPwEntry.setStatus("current")
_PxmPwMTUSize_Type = Integer32
_PxmPwMTUSize_Object = MibTableColumn
pxmPwMTUSize = _PxmPwMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1, 1),
    _PxmPwMTUSize_Type()
)
pxmPwMTUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwMTUSize.setStatus("current")
_PxmPwSetupMode_Type = InfnPWSetupMode
_PxmPwSetupMode_Object = MibTableColumn
pxmPwSetupMode = _PxmPwSetupMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1, 2),
    _PxmPwSetupMode_Type()
)
pxmPwSetupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmPwSetupMode.setStatus("current")
_PxmPwIncomingLabel_Type = Integer32
_PxmPwIncomingLabel_Object = MibTableColumn
pxmPwIncomingLabel = _PxmPwIncomingLabel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1, 3),
    _PxmPwIncomingLabel_Type()
)
pxmPwIncomingLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwIncomingLabel.setStatus("current")
_PxmPwOutgoingLabel_Type = Integer32
_PxmPwOutgoingLabel_Object = MibTableColumn
pxmPwOutgoingLabel = _PxmPwOutgoingLabel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1, 4),
    _PxmPwOutgoingLabel_Type()
)
pxmPwOutgoingLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwOutgoingLabel.setStatus("current")
_PxmPwCreationType_Type = InfnCreationType
_PxmPwCreationType_Object = MibTableColumn
pxmPwCreationType = _PxmPwCreationType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1, 5),
    _PxmPwCreationType_Type()
)
pxmPwCreationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwCreationType.setStatus("current")
_PxmPwPmHistStatsEnable_Type = InfnPmHistStatsControl
_PxmPwPmHistStatsEnable_Object = MibTableColumn
pxmPwPmHistStatsEnable = _PxmPwPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1, 6),
    _PxmPwPmHistStatsEnable_Type()
)
pxmPwPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmPwPmHistStatsEnable.setStatus("current")
_PxmPwSplitHorizonGroupID_Type = Integer32
_PxmPwSplitHorizonGroupID_Object = MibTableColumn
pxmPwSplitHorizonGroupID = _PxmPwSplitHorizonGroupID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1, 7),
    _PxmPwSplitHorizonGroupID_Type()
)
pxmPwSplitHorizonGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmPwSplitHorizonGroupID.setStatus("current")
_PxmPwFlapActionClear_Type = InfnFlapActionClear
_PxmPwFlapActionClear_Object = MibTableColumn
pxmPwFlapActionClear = _PxmPwFlapActionClear_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1, 8),
    _PxmPwFlapActionClear_Type()
)
pxmPwFlapActionClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmPwFlapActionClear.setStatus("current")
_PxmPwAssociatedMPLSTunnel_Type = DisplayString
_PxmPwAssociatedMPLSTunnel_Object = MibTableColumn
pxmPwAssociatedMPLSTunnel = _PxmPwAssociatedMPLSTunnel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 1, 1, 9),
    _PxmPwAssociatedMPLSTunnel_Type()
)
pxmPwAssociatedMPLSTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmPwAssociatedMPLSTunnel.setStatus("current")
_PxmPwConformance_ObjectIdentity = ObjectIdentity
pxmPwConformance = _PxmPwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 3)
)
_PxmPwCompliances_ObjectIdentity = ObjectIdentity
pxmPwCompliances = _PxmPwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 3, 1)
)
_PxmPwGroups_ObjectIdentity = ObjectIdentity
pxmPwGroups = _PxmPwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 3, 2)
)

# Managed Objects groups

pxmPwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 3, 2, 1)
)
pxmPwGroup.setObjects(
      *(("INFINERA-TP-PXPW-MIB", "pxmPwMTUSize"),
        ("INFINERA-TP-PXPW-MIB", "pxmPwSetupMode"),
        ("INFINERA-TP-PXPW-MIB", "pxmPwIncomingLabel"),
        ("INFINERA-TP-PXPW-MIB", "pxmPwOutgoingLabel"),
        ("INFINERA-TP-PXPW-MIB", "pxmPwCreationType"),
        ("INFINERA-TP-PXPW-MIB", "pxmPwPmHistStatsEnable"),
        ("INFINERA-TP-PXPW-MIB", "pxmPwSplitHorizonGroupID"),
        ("INFINERA-TP-PXPW-MIB", "pxmPwFlapActionClear"),
        ("INFINERA-TP-PXPW-MIB", "pxmPwAssociatedMPLSTunnel"))
)
if mibBuilder.loadTexts:
    pxmPwGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmPwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 75, 3, 1, 1)
)
pxmPwCompliance.setObjects(
    ("INFINERA-TP-PXPW-MIB", "pxmPwGroup")
)
if mibBuilder.loadTexts:
    pxmPwCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXPW-MIB",
    **{"pxmPwMIB": pxmPwMIB,
       "pxmPwTable": pxmPwTable,
       "pxmPwEntry": pxmPwEntry,
       "pxmPwMTUSize": pxmPwMTUSize,
       "pxmPwSetupMode": pxmPwSetupMode,
       "pxmPwIncomingLabel": pxmPwIncomingLabel,
       "pxmPwOutgoingLabel": pxmPwOutgoingLabel,
       "pxmPwCreationType": pxmPwCreationType,
       "pxmPwPmHistStatsEnable": pxmPwPmHistStatsEnable,
       "pxmPwSplitHorizonGroupID": pxmPwSplitHorizonGroupID,
       "pxmPwFlapActionClear": pxmPwFlapActionClear,
       "pxmPwAssociatedMPLSTunnel": pxmPwAssociatedMPLSTunnel,
       "pxmPwConformance": pxmPwConformance,
       "pxmPwCompliances": pxmPwCompliances,
       "pxmPwCompliance": pxmPwCompliance,
       "pxmPwGroups": pxmPwGroups,
       "pxmPwGroup": pxmPwGroup}
)
