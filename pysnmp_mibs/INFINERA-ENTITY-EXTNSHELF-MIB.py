# SNMP MIB module (INFINERA-ENTITY-EXTNSHELF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-EXTNSHELF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:41 2025
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

extnShelfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtnShelfTable_Object = MibTable
extnShelfTable = _ExtnShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1)
)
if mibBuilder.loadTexts:
    extnShelfTable.setStatus("current")
_ExtnShelfEntry_Object = MibTableRow
extnShelfEntry = _ExtnShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1, 1)
)
extnShelfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    extnShelfEntry.setStatus("current")
_ExtnShelfMoId_Type = DisplayString
_ExtnShelfMoId_Object = MibTableColumn
extnShelfMoId = _ExtnShelfMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1, 1, 1),
    _ExtnShelfMoId_Type()
)
extnShelfMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extnShelfMoId.setStatus("current")
_ExtnShelfProvEqptType_Type = InfnEqptType
_ExtnShelfProvEqptType_Object = MibTableColumn
extnShelfProvEqptType = _ExtnShelfProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1, 1, 2),
    _ExtnShelfProvEqptType_Type()
)
extnShelfProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extnShelfProvEqptType.setStatus("current")
_ExtnShelfProvSerialNumber_Type = DisplayString
_ExtnShelfProvSerialNumber_Object = MibTableColumn
extnShelfProvSerialNumber = _ExtnShelfProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1, 1, 3),
    _ExtnShelfProvSerialNumber_Type()
)
extnShelfProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extnShelfProvSerialNumber.setStatus("current")
_ExtnShelfConformance_ObjectIdentity = ObjectIdentity
extnShelfConformance = _ExtnShelfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3)
)
_ExtnShelfCompliances_ObjectIdentity = ObjectIdentity
extnShelfCompliances = _ExtnShelfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3, 1)
)
_ExtnShelfGroups_ObjectIdentity = ObjectIdentity
extnShelfGroups = _ExtnShelfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3, 2)
)

# Managed Objects groups

extnShelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3, 2, 1)
)
extnShelfGroup.setObjects(
      *(("INFINERA-ENTITY-EXTNSHELF-MIB", "extnShelfMoId"),
        ("INFINERA-ENTITY-EXTNSHELF-MIB", "extnShelfProvEqptType"),
        ("INFINERA-ENTITY-EXTNSHELF-MIB", "extnShelfProvSerialNumber"))
)
if mibBuilder.loadTexts:
    extnShelfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

extnShelfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3, 1, 1)
)
extnShelfCompliance.setObjects(
    ("INFINERA-ENTITY-EXTNSHELF-MIB", "extnShelfGroup")
)
if mibBuilder.loadTexts:
    extnShelfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-EXTNSHELF-MIB",
    **{"extnShelfMIB": extnShelfMIB,
       "extnShelfTable": extnShelfTable,
       "extnShelfEntry": extnShelfEntry,
       "extnShelfMoId": extnShelfMoId,
       "extnShelfProvEqptType": extnShelfProvEqptType,
       "extnShelfProvSerialNumber": extnShelfProvSerialNumber,
       "extnShelfConformance": extnShelfConformance,
       "extnShelfCompliances": extnShelfCompliances,
       "extnShelfCompliance": extnShelfCompliance,
       "extnShelfGroups": extnShelfGroups,
       "extnShelfGroup": extnShelfGroup}
)
