# SNMP MIB module (INFINERA-ENTITY-TAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-TAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:42 2025
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

tamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TamTable_Object = MibTable
tamTable = _TamTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tamTable.setStatus("current")
_TamEntry_Object = MibTableRow
tamEntry = _TamEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 1, 1)
)
tamEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tamEntry.setStatus("current")
_TamMoId_Type = DisplayString
_TamMoId_Object = MibTableColumn
tamMoId = _TamMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 1, 1, 1),
    _TamMoId_Type()
)
tamMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tamMoId.setStatus("current")
_TamProvEqptType_Type = InfnEqptType
_TamProvEqptType_Object = MibTableColumn
tamProvEqptType = _TamProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 1, 1, 2),
    _TamProvEqptType_Type()
)
tamProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tamProvEqptType.setStatus("current")
_TamRowStatus_Type = RowStatus
_TamRowStatus_Object = MibTableColumn
tamRowStatus = _TamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 1, 1, 3),
    _TamRowStatus_Type()
)
tamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tamRowStatus.setStatus("current")
_TamConformance_ObjectIdentity = ObjectIdentity
tamConformance = _TamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 3)
)
_TamCompliances_ObjectIdentity = ObjectIdentity
tamCompliances = _TamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 3, 1)
)
_TamGroups_ObjectIdentity = ObjectIdentity
tamGroups = _TamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 3, 2)
)

# Managed Objects groups

tamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 3, 2, 1)
)
tamGroup.setObjects(
      *(("INFINERA-ENTITY-TAM-MIB", "tamMoId"),
        ("INFINERA-ENTITY-TAM-MIB", "tamProvEqptType"),
        ("INFINERA-ENTITY-TAM-MIB", "tamRowStatus"))
)
if mibBuilder.loadTexts:
    tamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 7, 3, 1, 1)
)
tamCompliance.setObjects(
    ("INFINERA-ENTITY-TAM-MIB", "tamGroup")
)
if mibBuilder.loadTexts:
    tamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-TAM-MIB",
    **{"tamMIB": tamMIB,
       "tamTable": tamTable,
       "tamEntry": tamEntry,
       "tamMoId": tamMoId,
       "tamProvEqptType": tamProvEqptType,
       "tamRowStatus": tamRowStatus,
       "tamConformance": tamConformance,
       "tamCompliances": tamCompliances,
       "tamCompliance": tamCompliance,
       "tamGroups": tamGroups,
       "tamGroup": tamGroup}
)
