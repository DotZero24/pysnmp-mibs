# SNMP MIB module (INFINERA-ENTITY-MPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-MPC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:10 2025
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

mpcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpcTable_Object = MibTable
mpcTable = _MpcTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1)
)
if mibBuilder.loadTexts:
    mpcTable.setStatus("current")
_MpcEntry_Object = MibTableRow
mpcEntry = _MpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1)
)
mpcEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpcEntry.setStatus("current")
_MpcProvEqptType_Type = InfnEqptType
_MpcProvEqptType_Object = MibTableColumn
mpcProvEqptType = _MpcProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1, 1),
    _MpcProvEqptType_Type()
)
mpcProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpcProvEqptType.setStatus("current")
_MpcProvSerialNumber_Type = DisplayString
_MpcProvSerialNumber_Object = MibTableColumn
mpcProvSerialNumber = _MpcProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1, 2),
    _MpcProvSerialNumber_Type()
)
mpcProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcProvSerialNumber.setStatus("current")
_MpcLabel_Type = DisplayString
_MpcLabel_Object = MibTableColumn
mpcLabel = _MpcLabel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1, 3),
    _MpcLabel_Type()
)
mpcLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcLabel.setStatus("current")
_MpcConnectedPassiveEqptList_Type = DisplayString
_MpcConnectedPassiveEqptList_Object = MibTableColumn
mpcConnectedPassiveEqptList = _MpcConnectedPassiveEqptList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1, 4),
    _MpcConnectedPassiveEqptList_Type()
)
mpcConnectedPassiveEqptList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcConnectedPassiveEqptList.setStatus("current")
_MpcConformance_ObjectIdentity = ObjectIdentity
mpcConformance = _MpcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3)
)
_MpcCompliances_ObjectIdentity = ObjectIdentity
mpcCompliances = _MpcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3, 1)
)
_MpcGroups_ObjectIdentity = ObjectIdentity
mpcGroups = _MpcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3, 2)
)

# Managed Objects groups

mpcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3, 2, 1)
)
mpcGroup.setObjects(
      *(("INFINERA-ENTITY-MPC-MIB", "mpcProvEqptType"),
        ("INFINERA-ENTITY-MPC-MIB", "mpcProvSerialNumber"),
        ("INFINERA-ENTITY-MPC-MIB", "mpcLabel"),
        ("INFINERA-ENTITY-MPC-MIB", "mpcConnectedPassiveEqptList"))
)
if mibBuilder.loadTexts:
    mpcGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mpcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3, 1, 1)
)
mpcCompliance.setObjects(
    ("INFINERA-ENTITY-MPC-MIB", "mpcGroup")
)
if mibBuilder.loadTexts:
    mpcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-MPC-MIB",
    **{"mpcMIB": mpcMIB,
       "mpcTable": mpcTable,
       "mpcEntry": mpcEntry,
       "mpcProvEqptType": mpcProvEqptType,
       "mpcProvSerialNumber": mpcProvSerialNumber,
       "mpcLabel": mpcLabel,
       "mpcConnectedPassiveEqptList": mpcConnectedPassiveEqptList,
       "mpcConformance": mpcConformance,
       "mpcCompliances": mpcCompliances,
       "mpcCompliance": mpcCompliance,
       "mpcGroups": mpcGroups,
       "mpcGroup": mpcGroup}
)
