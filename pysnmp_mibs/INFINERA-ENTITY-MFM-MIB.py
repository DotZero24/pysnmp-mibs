# SNMP MIB module (INFINERA-ENTITY-MFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-MFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:39 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(InfnASEIdlerMuxOprMode,
 InfnEnableDisableType,
 InfnEqptType,
 InfnOPMScanGranularity,
 InfnOPMSwitchPosition) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnASEIdlerMuxOprMode",
    "InfnEnableDisableType",
    "InfnEqptType",
    "InfnOPMScanGranularity",
    "InfnOPMSwitchPosition")

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

mfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MfmTable_Object = MibTable
mfmTable = _MfmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1)
)
if mibBuilder.loadTexts:
    mfmTable.setStatus("current")
_MfmEntry_Object = MibTableRow
mfmEntry = _MfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1)
)
mfmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mfmEntry.setStatus("current")
_MfmMoId_Type = DisplayString
_MfmMoId_Object = MibTableColumn
mfmMoId = _MfmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1, 1),
    _MfmMoId_Type()
)
mfmMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfmMoId.setStatus("current")
_MfmProvEqptType_Type = InfnEqptType
_MfmProvEqptType_Object = MibTableColumn
mfmProvEqptType = _MfmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1, 2),
    _MfmProvEqptType_Type()
)
mfmProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfmProvEqptType.setStatus("current")
_MfmAssociatedDegree_Type = DisplayString
_MfmAssociatedDegree_Object = MibTableColumn
mfmAssociatedDegree = _MfmAssociatedDegree_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1, 3),
    _MfmAssociatedDegree_Type()
)
mfmAssociatedDegree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfmAssociatedDegree.setStatus("current")
_MfmOPMSwitchSelector_Type = InfnOPMSwitchPosition
_MfmOPMSwitchSelector_Object = MibTableColumn
mfmOPMSwitchSelector = _MfmOPMSwitchSelector_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1, 4),
    _MfmOPMSwitchSelector_Type()
)
mfmOPMSwitchSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfmOPMSwitchSelector.setStatus("current")
_MfmOPMScanGranularity_Type = InfnOPMScanGranularity
_MfmOPMScanGranularity_Object = MibTableColumn
mfmOPMScanGranularity = _MfmOPMScanGranularity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1, 5),
    _MfmOPMScanGranularity_Type()
)
mfmOPMScanGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfmOPMScanGranularity.setStatus("current")
_MfmScheduledOPMScan_Type = InfnEnableDisableType
_MfmScheduledOPMScan_Object = MibTableColumn
mfmScheduledOPMScan = _MfmScheduledOPMScan_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1, 6),
    _MfmScheduledOPMScan_Type()
)
mfmScheduledOPMScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfmScheduledOPMScan.setStatus("current")
_MfmScheduledOPMScanTime_Type = Unsigned32
_MfmScheduledOPMScanTime_Object = MibTableColumn
mfmScheduledOPMScanTime = _MfmScheduledOPMScanTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1, 7),
    _MfmScheduledOPMScanTime_Type()
)
mfmScheduledOPMScanTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfmScheduledOPMScanTime.setStatus("current")
_MfmScheduledOPMScanGranularity_Type = InfnOPMScanGranularity
_MfmScheduledOPMScanGranularity_Object = MibTableColumn
mfmScheduledOPMScanGranularity = _MfmScheduledOPMScanGranularity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1, 8),
    _MfmScheduledOPMScanGranularity_Type()
)
mfmScheduledOPMScanGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfmScheduledOPMScanGranularity.setStatus("current")
_MfmASEIdlerMuxOprMode_Type = InfnASEIdlerMuxOprMode
_MfmASEIdlerMuxOprMode_Object = MibTableColumn
mfmASEIdlerMuxOprMode = _MfmASEIdlerMuxOprMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 1, 1, 9),
    _MfmASEIdlerMuxOprMode_Type()
)
mfmASEIdlerMuxOprMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfmASEIdlerMuxOprMode.setStatus("current")
_MfmConformance_ObjectIdentity = ObjectIdentity
mfmConformance = _MfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 3)
)
_MfmCompliances_ObjectIdentity = ObjectIdentity
mfmCompliances = _MfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 3, 1)
)
_MfmGroups_ObjectIdentity = ObjectIdentity
mfmGroups = _MfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 3, 2)
)

# Managed Objects groups

mfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 3, 2, 1)
)
mfmGroup.setObjects(
      *(("INFINERA-ENTITY-MFM-MIB", "mfmMoId"),
        ("INFINERA-ENTITY-MFM-MIB", "mfmProvEqptType"),
        ("INFINERA-ENTITY-MFM-MIB", "mfmAssociatedDegree"),
        ("INFINERA-ENTITY-MFM-MIB", "mfmOPMSwitchSelector"),
        ("INFINERA-ENTITY-MFM-MIB", "mfmOPMScanGranularity"),
        ("INFINERA-ENTITY-MFM-MIB", "mfmScheduledOPMScan"),
        ("INFINERA-ENTITY-MFM-MIB", "mfmScheduledOPMScanTime"),
        ("INFINERA-ENTITY-MFM-MIB", "mfmScheduledOPMScanGranularity"),
        ("INFINERA-ENTITY-MFM-MIB", "mfmASEIdlerMuxOprMode"))
)
if mibBuilder.loadTexts:
    mfmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mfmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 58, 3, 1, 1)
)
mfmCompliance.setObjects(
    ("INFINERA-ENTITY-MFM-MIB", "mfmGroup")
)
if mibBuilder.loadTexts:
    mfmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-MFM-MIB",
    **{"mfmMIB": mfmMIB,
       "mfmTable": mfmTable,
       "mfmEntry": mfmEntry,
       "mfmMoId": mfmMoId,
       "mfmProvEqptType": mfmProvEqptType,
       "mfmAssociatedDegree": mfmAssociatedDegree,
       "mfmOPMSwitchSelector": mfmOPMSwitchSelector,
       "mfmOPMScanGranularity": mfmOPMScanGranularity,
       "mfmScheduledOPMScan": mfmScheduledOPMScan,
       "mfmScheduledOPMScanTime": mfmScheduledOPMScanTime,
       "mfmScheduledOPMScanGranularity": mfmScheduledOPMScanGranularity,
       "mfmASEIdlerMuxOprMode": mfmASEIdlerMuxOprMode,
       "mfmConformance": mfmConformance,
       "mfmCompliances": mfmCompliances,
       "mfmCompliance": mfmCompliance,
       "mfmGroups": mfmGroups,
       "mfmGroup": mfmGroup}
)
