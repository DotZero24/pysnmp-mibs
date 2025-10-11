# SNMP MIB module (INFINERA-ENTITY-XTMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-XTMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:26 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

xtmmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XtmmTable_Object = MibTable
xtmmTable = _XtmmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1)
)
if mibBuilder.loadTexts:
    xtmmTable.setStatus("current")
_XtmmEntry_Object = MibTableRow
xtmmEntry = _XtmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1)
)
xtmmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xtmmEntry.setStatus("current")
_XtmmMoId_Type = DisplayString
_XtmmMoId_Object = MibTableColumn
xtmmMoId = _XtmmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1, 1),
    _XtmmMoId_Type()
)
xtmmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmmMoId.setStatus("current")
_XtmmProvType_Type = InfnEqptType
_XtmmProvType_Object = MibTableColumn
xtmmProvType = _XtmmProvType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1, 2),
    _XtmmProvType_Type()
)
xtmmProvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmmProvType.setStatus("current")
_XtmmBrandingFault_Type = TruthValue
_XtmmBrandingFault_Object = MibTableColumn
xtmmBrandingFault = _XtmmBrandingFault_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1, 3),
    _XtmmBrandingFault_Type()
)
xtmmBrandingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtmmBrandingFault.setStatus("current")
_XtmmRowStatus_Type = RowStatus
_XtmmRowStatus_Object = MibTableColumn
xtmmRowStatus = _XtmmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1, 4),
    _XtmmRowStatus_Type()
)
xtmmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtmmRowStatus.setStatus("current")
_XtmmConformance_ObjectIdentity = ObjectIdentity
xtmmConformance = _XtmmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3)
)
_XtmmCompliances_ObjectIdentity = ObjectIdentity
xtmmCompliances = _XtmmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3, 1)
)
_XtmmGroups_ObjectIdentity = ObjectIdentity
xtmmGroups = _XtmmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3, 2)
)

# Managed Objects groups

xtmmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3, 2, 1)
)
xtmmGroup.setObjects(
      *(("INFINERA-ENTITY-XTMM-MIB", "xtmmBrandingFault"),
        ("INFINERA-ENTITY-XTMM-MIB", "xtmmMoId"),
        ("INFINERA-ENTITY-XTMM-MIB", "xtmmProvType"),
        ("INFINERA-ENTITY-XTMM-MIB", "xtmmRowStatus"))
)
if mibBuilder.loadTexts:
    xtmmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xtmmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3, 1, 1)
)
xtmmCompliance.setObjects(
    ("INFINERA-ENTITY-XTMM-MIB", "xtmmGroup")
)
if mibBuilder.loadTexts:
    xtmmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-XTMM-MIB",
    **{"xtmmMIB": xtmmMIB,
       "xtmmTable": xtmmTable,
       "xtmmEntry": xtmmEntry,
       "xtmmMoId": xtmmMoId,
       "xtmmProvType": xtmmProvType,
       "xtmmBrandingFault": xtmmBrandingFault,
       "xtmmRowStatus": xtmmRowStatus,
       "xtmmConformance": xtmmConformance,
       "xtmmCompliances": xtmmCompliances,
       "xtmmCompliance": xtmmCompliance,
       "xtmmGroups": xtmmGroups,
       "xtmmGroup": xtmmGroup}
)
