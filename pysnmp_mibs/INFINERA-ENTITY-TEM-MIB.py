# SNMP MIB module (INFINERA-ENTITY-TEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-TEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:39 2025
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

temMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TemTable_Object = MibTable
temTable = _TemTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    temTable.setStatus("current")
_TemEntry_Object = MibTableRow
temEntry = _TemEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 1, 1)
)
temEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    temEntry.setStatus("current")
_TemMoId_Type = DisplayString
_TemMoId_Object = MibTableColumn
temMoId = _TemMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 1, 1, 1),
    _TemMoId_Type()
)
temMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    temMoId.setStatus("current")
_TemProvEqptType_Type = InfnEqptType
_TemProvEqptType_Object = MibTableColumn
temProvEqptType = _TemProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 1, 1, 2),
    _TemProvEqptType_Type()
)
temProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    temProvEqptType.setStatus("current")
_TemRowStatus_Type = RowStatus
_TemRowStatus_Object = MibTableColumn
temRowStatus = _TemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 1, 1, 3),
    _TemRowStatus_Type()
)
temRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    temRowStatus.setStatus("current")
_TemConformance_ObjectIdentity = ObjectIdentity
temConformance = _TemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 3)
)
_TemCompliances_ObjectIdentity = ObjectIdentity
temCompliances = _TemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 3, 1)
)
_TemGroups_ObjectIdentity = ObjectIdentity
temGroups = _TemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 3, 2)
)

# Managed Objects groups

temGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 3, 2, 1)
)
temGroup.setObjects(
      *(("INFINERA-ENTITY-TEM-MIB", "temMoId"),
        ("INFINERA-ENTITY-TEM-MIB", "temProvEqptType"),
        ("INFINERA-ENTITY-TEM-MIB", "temRowStatus"))
)
if mibBuilder.loadTexts:
    temGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

temCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 6, 3, 1, 1)
)
temCompliance.setObjects(
    ("INFINERA-ENTITY-TEM-MIB", "temGroup")
)
if mibBuilder.loadTexts:
    temCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-TEM-MIB",
    **{"temMIB": temMIB,
       "temTable": temTable,
       "temEntry": temEntry,
       "temMoId": temMoId,
       "temProvEqptType": temProvEqptType,
       "temRowStatus": temRowStatus,
       "temConformance": temConformance,
       "temCompliances": temCompliances,
       "temCompliance": temCompliance,
       "temGroups": temGroups,
       "temGroup": temGroup}
)
