# SNMP MIB module (INFINERA-ENTITY-TIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-TIM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:28 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(InfnEqptType,
 InfnFPGAOperatingMode,
 InfnPortMappingMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEqptType",
    "InfnFPGAOperatingMode",
    "InfnPortMappingMode")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

timMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TimTable_Object = MibTable
timTable = _TimTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1)
)
if mibBuilder.loadTexts:
    timTable.setStatus("current")
_TimEntry_Object = MibTableRow
timEntry = _TimEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1)
)
timEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    timEntry.setStatus("current")
_TimMoId_Type = DisplayString
_TimMoId_Object = MibTableColumn
timMoId = _TimMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1, 1),
    _TimMoId_Type()
)
timMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timMoId.setStatus("current")
_TimProvEqptType_Type = InfnEqptType
_TimProvEqptType_Object = MibTableColumn
timProvEqptType = _TimProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1, 2),
    _TimProvEqptType_Type()
)
timProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timProvEqptType.setStatus("current")
_TimRowStatus_Type = RowStatus
_TimRowStatus_Object = MibTableColumn
timRowStatus = _TimRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1, 3),
    _TimRowStatus_Type()
)
timRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timRowStatus.setStatus("current")


class _TimOperatingModeStatus_Type(Integer32):
    """Custom type timOperatingModeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("changeinprogress", 2),
          ("preProvisioned", 3),
          ("notDetermined", 4))
    )


_TimOperatingModeStatus_Type.__name__ = "Integer32"
_TimOperatingModeStatus_Object = MibTableColumn
timOperatingModeStatus = _TimOperatingModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1, 4),
    _TimOperatingModeStatus_Type()
)
timOperatingModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timOperatingModeStatus.setStatus("current")


class _TimOperatingMode_Type(InfnFPGAOperatingMode):
    """Custom type timOperatingMode based on InfnFPGAOperatingMode"""
    defaultValue = 4


_TimOperatingMode_Type.__name__ = "InfnFPGAOperatingMode"
_TimOperatingMode_Object = MibTableColumn
timOperatingMode = _TimOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1, 5),
    _TimOperatingMode_Type()
)
timOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timOperatingMode.setStatus("current")


class _TimPortMappingModeGroup1_Type(InfnPortMappingMode):
    """Custom type timPortMappingModeGroup1 based on InfnPortMappingMode"""
    defaultValue = 2


_TimPortMappingModeGroup1_Type.__name__ = "InfnPortMappingMode"
_TimPortMappingModeGroup1_Object = MibTableColumn
timPortMappingModeGroup1 = _TimPortMappingModeGroup1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1, 6),
    _TimPortMappingModeGroup1_Type()
)
timPortMappingModeGroup1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timPortMappingModeGroup1.setStatus("current")


class _TimPortMappingModeGroup2_Type(InfnPortMappingMode):
    """Custom type timPortMappingModeGroup2 based on InfnPortMappingMode"""
    defaultValue = 2


_TimPortMappingModeGroup2_Type.__name__ = "InfnPortMappingMode"
_TimPortMappingModeGroup2_Object = MibTableColumn
timPortMappingModeGroup2 = _TimPortMappingModeGroup2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1, 7),
    _TimPortMappingModeGroup2_Type()
)
timPortMappingModeGroup2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timPortMappingModeGroup2.setStatus("current")


class _TimPortMappingModeGroup3_Type(InfnPortMappingMode):
    """Custom type timPortMappingModeGroup3 based on InfnPortMappingMode"""
    defaultValue = 2


_TimPortMappingModeGroup3_Type.__name__ = "InfnPortMappingMode"
_TimPortMappingModeGroup3_Object = MibTableColumn
timPortMappingModeGroup3 = _TimPortMappingModeGroup3_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1, 8),
    _TimPortMappingModeGroup3_Type()
)
timPortMappingModeGroup3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timPortMappingModeGroup3.setStatus("current")


class _TimPortMappingModeGroup4_Type(InfnPortMappingMode):
    """Custom type timPortMappingModeGroup4 based on InfnPortMappingMode"""
    defaultValue = 2


_TimPortMappingModeGroup4_Type.__name__ = "InfnPortMappingMode"
_TimPortMappingModeGroup4_Object = MibTableColumn
timPortMappingModeGroup4 = _TimPortMappingModeGroup4_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 1, 1, 9),
    _TimPortMappingModeGroup4_Type()
)
timPortMappingModeGroup4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timPortMappingModeGroup4.setStatus("current")
_TimConformance_ObjectIdentity = ObjectIdentity
timConformance = _TimConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 3)
)
_TimCompliances_ObjectIdentity = ObjectIdentity
timCompliances = _TimCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 3, 1)
)
_TimGroups_ObjectIdentity = ObjectIdentity
timGroups = _TimGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 3, 2)
)

# Managed Objects groups

timGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 3, 2, 1)
)
timGroup.setObjects(
      *(("INFINERA-ENTITY-TIM-MIB", "timMoId"),
        ("INFINERA-ENTITY-TIM-MIB", "timProvEqptType"),
        ("INFINERA-ENTITY-TIM-MIB", "timRowStatus"),
        ("INFINERA-ENTITY-TIM-MIB", "timOperatingModeStatus"),
        ("INFINERA-ENTITY-TIM-MIB", "timOperatingMode"),
        ("INFINERA-ENTITY-TIM-MIB", "timPortMappingModeGroup1"),
        ("INFINERA-ENTITY-TIM-MIB", "timPortMappingModeGroup2"),
        ("INFINERA-ENTITY-TIM-MIB", "timPortMappingModeGroup3"),
        ("INFINERA-ENTITY-TIM-MIB", "timPortMappingModeGroup4"))
)
if mibBuilder.loadTexts:
    timGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

timCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 23, 3, 1, 1)
)
timCompliance.setObjects(
    ("INFINERA-ENTITY-TIM-MIB", "timGroup")
)
if mibBuilder.loadTexts:
    timCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-TIM-MIB",
    **{"timMIB": timMIB,
       "timTable": timTable,
       "timEntry": timEntry,
       "timMoId": timMoId,
       "timProvEqptType": timProvEqptType,
       "timRowStatus": timRowStatus,
       "timOperatingModeStatus": timOperatingModeStatus,
       "timOperatingMode": timOperatingMode,
       "timPortMappingModeGroup1": timPortMappingModeGroup1,
       "timPortMappingModeGroup2": timPortMappingModeGroup2,
       "timPortMappingModeGroup3": timPortMappingModeGroup3,
       "timPortMappingModeGroup4": timPortMappingModeGroup4,
       "timConformance": timConformance,
       "timCompliances": timCompliances,
       "timCompliance": timCompliance,
       "timGroups": timGroups,
       "timGroup": timGroup}
)
