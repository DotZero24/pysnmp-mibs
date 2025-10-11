# SNMP MIB module (INFINERA-ENTITY-OMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:59 2025
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

ommMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OmmTable_Object = MibTable
ommTable = _OmmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ommTable.setStatus("current")
_OmmEntry_Object = MibTableRow
ommEntry = _OmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1)
)
ommEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ommEntry.setStatus("current")
_OmmMoId_Type = DisplayString
_OmmMoId_Object = MibTableColumn
ommMoId = _OmmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 1),
    _OmmMoId_Type()
)
ommMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ommMoId.setStatus("current")
_OmmProvType_Type = InfnEqptType
_OmmProvType_Object = MibTableColumn
ommProvType = _OmmProvType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 2),
    _OmmProvType_Type()
)
ommProvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ommProvType.setStatus("current")


class _OmmRedundancyStatus_Type(Integer32):
    """Custom type ommRedundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("single", 2),
          ("active", 3),
          ("standby", 4),
          ("makeStandbyInProgress", 5),
          ("oos", 6),
          ("lock", 7))
    )


_OmmRedundancyStatus_Type.__name__ = "Integer32"
_OmmRedundancyStatus_Object = MibTableColumn
ommRedundancyStatus = _OmmRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 3),
    _OmmRedundancyStatus_Type()
)
ommRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ommRedundancyStatus.setStatus("current")
_OmmBrandingFault_Type = TruthValue
_OmmBrandingFault_Object = MibTableColumn
ommBrandingFault = _OmmBrandingFault_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 4),
    _OmmBrandingFault_Type()
)
ommBrandingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ommBrandingFault.setStatus("current")
_OmmRowStatus_Type = RowStatus
_OmmRowStatus_Object = MibTableColumn
ommRowStatus = _OmmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 5),
    _OmmRowStatus_Type()
)
ommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ommRowStatus.setStatus("current")
_OmmConformance_ObjectIdentity = ObjectIdentity
ommConformance = _OmmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3)
)
_OmmCompliances_ObjectIdentity = ObjectIdentity
ommCompliances = _OmmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3, 1)
)
_OmmGroups_ObjectIdentity = ObjectIdentity
ommGroups = _OmmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3, 2)
)

# Managed Objects groups

ommGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3, 2, 1)
)
ommGroup.setObjects(
      *(("INFINERA-ENTITY-OMM-MIB", "ommBrandingFault"),
        ("INFINERA-ENTITY-OMM-MIB", "ommMoId"),
        ("INFINERA-ENTITY-OMM-MIB", "ommProvType"),
        ("INFINERA-ENTITY-OMM-MIB", "ommRedundancyStatus"),
        ("INFINERA-ENTITY-OMM-MIB", "ommRowStatus"))
)
if mibBuilder.loadTexts:
    ommGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ommCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3, 1, 1)
)
ommCompliance.setObjects(
    ("INFINERA-ENTITY-OMM-MIB", "ommGroup")
)
if mibBuilder.loadTexts:
    ommCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OMM-MIB",
    **{"ommMIB": ommMIB,
       "ommTable": ommTable,
       "ommEntry": ommEntry,
       "ommMoId": ommMoId,
       "ommProvType": ommProvType,
       "ommRedundancyStatus": ommRedundancyStatus,
       "ommBrandingFault": ommBrandingFault,
       "ommRowStatus": ommRowStatus,
       "ommConformance": ommConformance,
       "ommCompliances": ommCompliances,
       "ommCompliance": ommCompliance,
       "ommGroups": ommGroups,
       "ommGroup": ommGroup}
)
