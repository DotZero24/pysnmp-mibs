# SNMP MIB module (INFINERA-ENTITY-CMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-CMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:57 2025
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

cmmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmmTable_Object = MibTable
cmmTable = _CmmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1)
)
if mibBuilder.loadTexts:
    cmmTable.setStatus("current")
_CmmEntry_Object = MibTableRow
cmmEntry = _CmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1, 1)
)
cmmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cmmEntry.setStatus("current")
_CmmMoId_Type = DisplayString
_CmmMoId_Object = MibTableColumn
cmmMoId = _CmmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1, 1, 1),
    _CmmMoId_Type()
)
cmmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmmMoId.setStatus("current")
_CmmProvEqptType_Type = InfnEqptType
_CmmProvEqptType_Object = MibTableColumn
cmmProvEqptType = _CmmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1, 1, 2),
    _CmmProvEqptType_Type()
)
cmmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmmProvEqptType.setStatus("current")
_CmmRowStatus_Type = RowStatus
_CmmRowStatus_Object = MibTableColumn
cmmRowStatus = _CmmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1, 1, 3),
    _CmmRowStatus_Type()
)
cmmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmmRowStatus.setStatus("current")
_CmmConformance_ObjectIdentity = ObjectIdentity
cmmConformance = _CmmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14)
)
_CmmCompliances_ObjectIdentity = ObjectIdentity
cmmCompliances = _CmmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14, 1)
)
_CmmGroups_ObjectIdentity = ObjectIdentity
cmmGroups = _CmmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14, 2)
)

# Managed Objects groups

cmmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14, 2, 1)
)
cmmGroup.setObjects(
      *(("INFINERA-ENTITY-CMM-MIB", "cmmMoId"),
        ("INFINERA-ENTITY-CMM-MIB", "cmmProvEqptType"),
        ("INFINERA-ENTITY-CMM-MIB", "cmmRowStatus"))
)
if mibBuilder.loadTexts:
    cmmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14, 1, 1)
)
cmmCompliance.setObjects(
    ("INFINERA-ENTITY-CMM-MIB", "cmmGroup")
)
if mibBuilder.loadTexts:
    cmmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-CMM-MIB",
    **{"cmmMIB": cmmMIB,
       "cmmTable": cmmTable,
       "cmmEntry": cmmEntry,
       "cmmMoId": cmmMoId,
       "cmmProvEqptType": cmmProvEqptType,
       "cmmRowStatus": cmmRowStatus,
       "cmmConformance": cmmConformance,
       "cmmCompliances": cmmCompliances,
       "cmmCompliance": cmmCompliance,
       "cmmGroups": cmmGroups,
       "cmmGroup": cmmGroup}
)
