# SNMP MIB module (INFINERA-ENTITY-OPSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OPSM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:17 2025
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

opsmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OpsmTable_Object = MibTable
opsmTable = _OpsmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1)
)
if mibBuilder.loadTexts:
    opsmTable.setStatus("current")
_OpsmEntry_Object = MibTableRow
opsmEntry = _OpsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1, 1)
)
opsmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    opsmEntry.setStatus("current")
_OpsmMoId_Type = DisplayString
_OpsmMoId_Object = MibTableColumn
opsmMoId = _OpsmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1, 1, 1),
    _OpsmMoId_Type()
)
opsmMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmMoId.setStatus("current")
_OpsmProvEqptType_Type = InfnEqptType
_OpsmProvEqptType_Object = MibTableColumn
opsmProvEqptType = _OpsmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1, 1, 2),
    _OpsmProvEqptType_Type()
)
opsmProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmProvEqptType.setStatus("current")
_OpsmNodeId_Type = DisplayString
_OpsmNodeId_Object = MibTableColumn
opsmNodeId = _OpsmNodeId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1, 1, 3),
    _OpsmNodeId_Type()
)
opsmNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmNodeId.setStatus("current")
_OpsmConformance_ObjectIdentity = ObjectIdentity
opsmConformance = _OpsmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3)
)
_OpsmCompliances_ObjectIdentity = ObjectIdentity
opsmCompliances = _OpsmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3, 1)
)
_OpsmGroups_ObjectIdentity = ObjectIdentity
opsmGroups = _OpsmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3, 2)
)

# Managed Objects groups

opsmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3, 2, 1)
)
opsmGroup.setObjects(
      *(("INFINERA-ENTITY-OPSM-MIB", "opsmMoId"),
        ("INFINERA-ENTITY-OPSM-MIB", "opsmProvEqptType"),
        ("INFINERA-ENTITY-OPSM-MIB", "opsmNodeId"))
)
if mibBuilder.loadTexts:
    opsmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

opsmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3, 1, 1)
)
opsmCompliance.setObjects(
    ("INFINERA-ENTITY-OPSM-MIB", "opsmGroup")
)
if mibBuilder.loadTexts:
    opsmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OPSM-MIB",
    **{"opsmMIB": opsmMIB,
       "opsmTable": opsmTable,
       "opsmEntry": opsmEntry,
       "opsmMoId": opsmMoId,
       "opsmProvEqptType": opsmProvEqptType,
       "opsmNodeId": opsmNodeId,
       "opsmConformance": opsmConformance,
       "opsmCompliances": opsmCompliances,
       "opsmCompliance": opsmCompliance,
       "opsmGroups": opsmGroups,
       "opsmGroup": opsmGroup}
)
