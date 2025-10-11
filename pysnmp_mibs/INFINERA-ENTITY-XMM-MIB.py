# SNMP MIB module (INFINERA-ENTITY-XMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-XMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:04 2025
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

xmmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XmmTable_Object = MibTable
xmmTable = _XmmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1)
)
if mibBuilder.loadTexts:
    xmmTable.setStatus("current")
_XmmEntry_Object = MibTableRow
xmmEntry = _XmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1)
)
xmmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xmmEntry.setStatus("current")
_XmmMoId_Type = DisplayString
_XmmMoId_Object = MibTableColumn
xmmMoId = _XmmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1, 1),
    _XmmMoId_Type()
)
xmmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xmmMoId.setStatus("current")
_XmmProvType_Type = InfnEqptType
_XmmProvType_Object = MibTableColumn
xmmProvType = _XmmProvType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1, 2),
    _XmmProvType_Type()
)
xmmProvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xmmProvType.setStatus("current")
_XmmBrandingFault_Type = TruthValue
_XmmBrandingFault_Object = MibTableColumn
xmmBrandingFault = _XmmBrandingFault_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1, 3),
    _XmmBrandingFault_Type()
)
xmmBrandingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmmBrandingFault.setStatus("current")
_XmmRowStatus_Type = RowStatus
_XmmRowStatus_Object = MibTableColumn
xmmRowStatus = _XmmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1, 4),
    _XmmRowStatus_Type()
)
xmmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xmmRowStatus.setStatus("current")
_XmmConformance_ObjectIdentity = ObjectIdentity
xmmConformance = _XmmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3)
)
_XmmCompliances_ObjectIdentity = ObjectIdentity
xmmCompliances = _XmmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3, 1)
)
_XmmGroups_ObjectIdentity = ObjectIdentity
xmmGroups = _XmmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3, 2)
)

# Managed Objects groups

xmmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3, 2, 1)
)
xmmGroup.setObjects(
      *(("INFINERA-ENTITY-XMM-MIB", "xmmBrandingFault"),
        ("INFINERA-ENTITY-XMM-MIB", "xmmMoId"),
        ("INFINERA-ENTITY-XMM-MIB", "xmmProvType"),
        ("INFINERA-ENTITY-XMM-MIB", "xmmRowStatus"))
)
if mibBuilder.loadTexts:
    xmmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xmmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3, 1, 1)
)
xmmCompliance.setObjects(
    ("INFINERA-ENTITY-XMM-MIB", "xmmGroup")
)
if mibBuilder.loadTexts:
    xmmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-XMM-MIB",
    **{"xmmMIB": xmmMIB,
       "xmmTable": xmmTable,
       "xmmEntry": xmmEntry,
       "xmmMoId": xmmMoId,
       "xmmProvType": xmmProvType,
       "xmmBrandingFault": xmmBrandingFault,
       "xmmRowStatus": xmmRowStatus,
       "xmmConformance": xmmConformance,
       "xmmCompliances": xmmCompliances,
       "xmmCompliance": xmmCompliance,
       "xmmGroups": xmmGroups,
       "xmmGroup": xmmGroup}
)
