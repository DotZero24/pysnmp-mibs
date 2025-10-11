# SNMP MIB module (INFINERA-ENTITY-BPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-BPP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:53 2025
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

bppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BppTable_Object = MibTable
bppTable = _BppTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1)
)
if mibBuilder.loadTexts:
    bppTable.setStatus("current")
_BppEntry_Object = MibTableRow
bppEntry = _BppEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1, 1)
)
bppEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    bppEntry.setStatus("current")
_BppMoId_Type = DisplayString
_BppMoId_Object = MibTableColumn
bppMoId = _BppMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1, 1, 1),
    _BppMoId_Type()
)
bppMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bppMoId.setStatus("current")
_BppProvEqptType_Type = InfnEqptType
_BppProvEqptType_Object = MibTableColumn
bppProvEqptType = _BppProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1, 1, 2),
    _BppProvEqptType_Type()
)
bppProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bppProvEqptType.setStatus("current")
_BppProvSerialNumber_Type = DisplayString
_BppProvSerialNumber_Object = MibTableColumn
bppProvSerialNumber = _BppProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1, 1, 3),
    _BppProvSerialNumber_Type()
)
bppProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bppProvSerialNumber.setStatus("current")
_BppConformance_ObjectIdentity = ObjectIdentity
bppConformance = _BppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3)
)
_BppCompliances_ObjectIdentity = ObjectIdentity
bppCompliances = _BppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3, 1)
)
_BppGroups_ObjectIdentity = ObjectIdentity
bppGroups = _BppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3, 2)
)

# Managed Objects groups

bppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3, 2, 1)
)
bppGroup.setObjects(
      *(("INFINERA-ENTITY-BPP-MIB", "bppMoId"),
        ("INFINERA-ENTITY-BPP-MIB", "bppProvEqptType"),
        ("INFINERA-ENTITY-BPP-MIB", "bppProvSerialNumber"))
)
if mibBuilder.loadTexts:
    bppGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3, 1, 1)
)
bppCompliance.setObjects(
    ("INFINERA-ENTITY-BPP-MIB", "bppGroup")
)
if mibBuilder.loadTexts:
    bppCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-BPP-MIB",
    **{"bppMIB": bppMIB,
       "bppTable": bppTable,
       "bppEntry": bppEntry,
       "bppMoId": bppMoId,
       "bppProvEqptType": bppProvEqptType,
       "bppProvSerialNumber": bppProvSerialNumber,
       "bppConformance": bppConformance,
       "bppCompliances": bppCompliances,
       "bppCompliance": bppCompliance,
       "bppGroups": bppGroups,
       "bppGroup": bppGroup}
)
