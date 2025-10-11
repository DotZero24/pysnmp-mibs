# SNMP MIB module (INFINERA-ENTITY-OTDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OTDM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:37 2025
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

otdmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtdmTable_Object = MibTable
otdmTable = _OtdmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 1)
)
if mibBuilder.loadTexts:
    otdmTable.setStatus("current")
_OtdmEntry_Object = MibTableRow
otdmEntry = _OtdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 1, 1)
)
otdmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    otdmEntry.setStatus("current")
_OtdmMoId_Type = DisplayString
_OtdmMoId_Object = MibTableColumn
otdmMoId = _OtdmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 1, 1, 1),
    _OtdmMoId_Type()
)
otdmMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmMoId.setStatus("current")
_OtdmProvEqptType_Type = InfnEqptType
_OtdmProvEqptType_Object = MibTableColumn
otdmProvEqptType = _OtdmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 1, 1, 2),
    _OtdmProvEqptType_Type()
)
otdmProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmProvEqptType.setStatus("current")
_OtdmConformance_ObjectIdentity = ObjectIdentity
otdmConformance = _OtdmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3)
)
_OtdmCompliances_ObjectIdentity = ObjectIdentity
otdmCompliances = _OtdmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3, 1)
)
_OtdmGroups_ObjectIdentity = ObjectIdentity
otdmGroups = _OtdmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3, 2)
)

# Managed Objects groups

otdmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3, 2, 1)
)
otdmGroup.setObjects(
      *(("INFINERA-ENTITY-OTDM-MIB", "otdmMoId"),
        ("INFINERA-ENTITY-OTDM-MIB", "otdmProvEqptType"))
)
if mibBuilder.loadTexts:
    otdmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otdmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3, 1, 1)
)
otdmCompliance.setObjects(
    ("INFINERA-ENTITY-OTDM-MIB", "otdmGroup")
)
if mibBuilder.loadTexts:
    otdmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OTDM-MIB",
    **{"otdmMIB": otdmMIB,
       "otdmTable": otdmTable,
       "otdmEntry": otdmEntry,
       "otdmMoId": otdmMoId,
       "otdmProvEqptType": otdmProvEqptType,
       "otdmConformance": otdmConformance,
       "otdmCompliances": otdmCompliances,
       "otdmCompliance": otdmCompliance,
       "otdmGroups": otdmGroups,
       "otdmGroup": otdmGroup}
)
