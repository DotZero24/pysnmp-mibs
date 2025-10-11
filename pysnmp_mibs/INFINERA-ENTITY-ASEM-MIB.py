# SNMP MIB module (INFINERA-ENTITY-ASEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-ASEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:48 2025
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

(InfnEqptType,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEqptType")

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

asemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsemTable_Object = MibTable
asemTable = _AsemTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 1)
)
if mibBuilder.loadTexts:
    asemTable.setStatus("current")
_AsemEntry_Object = MibTableRow
asemEntry = _AsemEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 1, 1)
)
asemEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    asemEntry.setStatus("current")
_AsemMoId_Type = DisplayString
_AsemMoId_Object = MibTableColumn
asemMoId = _AsemMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 1, 1, 1),
    _AsemMoId_Type()
)
asemMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asemMoId.setStatus("current")
_AsemProvEqptType_Type = InfnEqptType
_AsemProvEqptType_Object = MibTableColumn
asemProvEqptType = _AsemProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 1, 1, 2),
    _AsemProvEqptType_Type()
)
asemProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asemProvEqptType.setStatus("current")
_AsemConformance_ObjectIdentity = ObjectIdentity
asemConformance = _AsemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3)
)
_AsemCompliances_ObjectIdentity = ObjectIdentity
asemCompliances = _AsemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3, 1)
)
_AsemGroups_ObjectIdentity = ObjectIdentity
asemGroups = _AsemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3, 2)
)

# Managed Objects groups

asemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3, 2, 1)
)
asemGroup.setObjects(
      *(("INFINERA-ENTITY-ASEM-MIB", "asemMoId"),
        ("INFINERA-ENTITY-ASEM-MIB", "asemProvEqptType"))
)
if mibBuilder.loadTexts:
    asemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

asemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3, 1, 1)
)
asemCompliance.setObjects(
    ("INFINERA-ENTITY-ASEM-MIB", "asemGroup")
)
if mibBuilder.loadTexts:
    asemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-ASEM-MIB",
    **{"asemMIB": asemMIB,
       "asemTable": asemTable,
       "asemEntry": asemEntry,
       "asemMoId": asemMoId,
       "asemProvEqptType": asemProvEqptType,
       "asemConformance": asemConformance,
       "asemCompliances": asemCompliances,
       "asemCompliance": asemCompliance,
       "asemGroups": asemGroups,
       "asemGroup": asemGroup}
)
