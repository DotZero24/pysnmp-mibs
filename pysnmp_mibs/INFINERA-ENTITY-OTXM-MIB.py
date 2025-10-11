# SNMP MIB module (INFINERA-ENTITY-OTXM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OTXM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:55 2025
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

otxmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtxmTable_Object = MibTable
otxmTable = _OtxmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1)
)
if mibBuilder.loadTexts:
    otxmTable.setStatus("current")
_OtxmEntry_Object = MibTableRow
otxmEntry = _OtxmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1, 1)
)
otxmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    otxmEntry.setStatus("current")
_OtxmMoId_Type = DisplayString
_OtxmMoId_Object = MibTableColumn
otxmMoId = _OtxmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1, 1, 1),
    _OtxmMoId_Type()
)
otxmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otxmMoId.setStatus("current")
_OtxmProvEqptType_Type = InfnEqptType
_OtxmProvEqptType_Object = MibTableColumn
otxmProvEqptType = _OtxmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1, 1, 2),
    _OtxmProvEqptType_Type()
)
otxmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otxmProvEqptType.setStatus("current")
_OtxmRowStatus_Type = RowStatus
_OtxmRowStatus_Object = MibTableColumn
otxmRowStatus = _OtxmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1, 1, 3),
    _OtxmRowStatus_Type()
)
otxmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otxmRowStatus.setStatus("current")
_OtxmConformance_ObjectIdentity = ObjectIdentity
otxmConformance = _OtxmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3)
)
_OtxmCompliances_ObjectIdentity = ObjectIdentity
otxmCompliances = _OtxmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3, 1)
)
_OtxmGroups_ObjectIdentity = ObjectIdentity
otxmGroups = _OtxmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3, 2)
)

# Managed Objects groups

otxmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3, 2, 1)
)
otxmGroup.setObjects(
      *(("INFINERA-ENTITY-OTXM-MIB", "otxmMoId"),
        ("INFINERA-ENTITY-OTXM-MIB", "otxmProvEqptType"),
        ("INFINERA-ENTITY-OTXM-MIB", "otxmRowStatus"))
)
if mibBuilder.loadTexts:
    otxmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otxmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3, 1, 1)
)
otxmCompliance.setObjects(
    ("INFINERA-ENTITY-OTXM-MIB", "otxmGroup")
)
if mibBuilder.loadTexts:
    otxmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OTXM-MIB",
    **{"otxmMIB": otxmMIB,
       "otxmTable": otxmTable,
       "otxmEntry": otxmEntry,
       "otxmMoId": otxmMoId,
       "otxmProvEqptType": otxmProvEqptType,
       "otxmRowStatus": otxmRowStatus,
       "otxmConformance": otxmConformance,
       "otxmCompliances": otxmCompliances,
       "otxmCompliance": otxmCompliance,
       "otxmGroups": otxmGroups,
       "otxmGroup": otxmGroup}
)
