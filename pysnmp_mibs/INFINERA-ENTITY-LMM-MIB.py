# SNMP MIB module (INFINERA-ENTITY-LMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-LMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:17 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lmmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LmmTable_Object = MibTable
lmmTable = _LmmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1)
)
if mibBuilder.loadTexts:
    lmmTable.setStatus("current")
_LmmEntry_Object = MibTableRow
lmmEntry = _LmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1)
)
lmmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    lmmEntry.setStatus("current")
_LmmMoId_Type = DisplayString
_LmmMoId_Object = MibTableColumn
lmmMoId = _LmmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1, 1),
    _LmmMoId_Type()
)
lmmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmmMoId.setStatus("current")
_LmmProvEqptType_Type = InfnEqptType
_LmmProvEqptType_Object = MibTableColumn
lmmProvEqptType = _LmmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1, 2),
    _LmmProvEqptType_Type()
)
lmmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmmProvEqptType.setStatus("current")
_LmmProvSerialNumber_Type = DisplayString
_LmmProvSerialNumber_Object = MibTableColumn
lmmProvSerialNumber = _LmmProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1, 3),
    _LmmProvSerialNumber_Type()
)
lmmProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmmProvSerialNumber.setStatus("current")
_LmmAssociatedDegree_Type = DisplayString
_LmmAssociatedDegree_Object = MibTableColumn
lmmAssociatedDegree = _LmmAssociatedDegree_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1, 4),
    _LmmAssociatedDegree_Type()
)
lmmAssociatedDegree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmmAssociatedDegree.setStatus("current")
_LmmConformance_ObjectIdentity = ObjectIdentity
lmmConformance = _LmmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3)
)
_LmmCompliances_ObjectIdentity = ObjectIdentity
lmmCompliances = _LmmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3, 1)
)
_LmmGroups_ObjectIdentity = ObjectIdentity
lmmGroups = _LmmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3, 2)
)

# Managed Objects groups

lmmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3, 2, 1)
)
lmmGroup.setObjects(
      *(("INFINERA-ENTITY-LMM-MIB", "lmmMoId"),
        ("INFINERA-ENTITY-LMM-MIB", "lmmProvEqptType"),
        ("INFINERA-ENTITY-LMM-MIB", "lmmProvSerialNumber"),
        ("INFINERA-ENTITY-LMM-MIB", "lmmAssociatedDegree"))
)
if mibBuilder.loadTexts:
    lmmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lmmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3, 1, 1)
)
lmmCompliance.setObjects(
    ("INFINERA-ENTITY-LMM-MIB", "lmmGroup")
)
if mibBuilder.loadTexts:
    lmmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-LMM-MIB",
    **{"lmmMIB": lmmMIB,
       "lmmTable": lmmTable,
       "lmmEntry": lmmEntry,
       "lmmMoId": lmmMoId,
       "lmmProvEqptType": lmmProvEqptType,
       "lmmProvSerialNumber": lmmProvSerialNumber,
       "lmmAssociatedDegree": lmmAssociatedDegree,
       "lmmConformance": lmmConformance,
       "lmmCompliances": lmmCompliances,
       "lmmCompliance": lmmCompliance,
       "lmmGroups": lmmGroups,
       "lmmGroup": lmmGroup}
)
