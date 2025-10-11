# SNMP MIB module (INFINERA-ENTITY-RBP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-RBP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:44 2025
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

rbpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbpTable_Object = MibTable
rbpTable = _RbpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1)
)
if mibBuilder.loadTexts:
    rbpTable.setStatus("current")
_RbpEntry_Object = MibTableRow
rbpEntry = _RbpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1, 1)
)
rbpEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    rbpEntry.setStatus("current")
_RbpMoId_Type = DisplayString
_RbpMoId_Object = MibTableColumn
rbpMoId = _RbpMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1, 1, 1),
    _RbpMoId_Type()
)
rbpMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbpMoId.setStatus("current")
_RbpProvEqptType_Type = InfnEqptType
_RbpProvEqptType_Object = MibTableColumn
rbpProvEqptType = _RbpProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1, 1, 2),
    _RbpProvEqptType_Type()
)
rbpProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbpProvEqptType.setStatus("current")
_RbpProvSerialNumber_Type = DisplayString
_RbpProvSerialNumber_Object = MibTableColumn
rbpProvSerialNumber = _RbpProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1, 1, 3),
    _RbpProvSerialNumber_Type()
)
rbpProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbpProvSerialNumber.setStatus("current")
_RbpConformance_ObjectIdentity = ObjectIdentity
rbpConformance = _RbpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3)
)
_RbpCompliances_ObjectIdentity = ObjectIdentity
rbpCompliances = _RbpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3, 1)
)
_RbpGroups_ObjectIdentity = ObjectIdentity
rbpGroups = _RbpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3, 2)
)

# Managed Objects groups

rbpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3, 2, 1)
)
rbpGroup.setObjects(
      *(("INFINERA-ENTITY-RBP-MIB", "rbpMoId"),
        ("INFINERA-ENTITY-RBP-MIB", "rbpProvEqptType"),
        ("INFINERA-ENTITY-RBP-MIB", "rbpProvSerialNumber"))
)
if mibBuilder.loadTexts:
    rbpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3, 1, 1)
)
rbpCompliance.setObjects(
    ("INFINERA-ENTITY-RBP-MIB", "rbpGroup")
)
if mibBuilder.loadTexts:
    rbpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-RBP-MIB",
    **{"rbpMIB": rbpMIB,
       "rbpTable": rbpTable,
       "rbpEntry": rbpEntry,
       "rbpMoId": rbpMoId,
       "rbpProvEqptType": rbpProvEqptType,
       "rbpProvSerialNumber": rbpProvSerialNumber,
       "rbpConformance": rbpConformance,
       "rbpCompliances": rbpCompliances,
       "rbpCompliance": rbpCompliance,
       "rbpGroups": rbpGroups,
       "rbpGroup": rbpGroup}
)
