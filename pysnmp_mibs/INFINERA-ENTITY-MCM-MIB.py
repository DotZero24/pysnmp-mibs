# SNMP MIB module (INFINERA-ENTITY-MCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-MCM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:42 2025
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

mcmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_McmTable_Object = MibTable
mcmTable = _McmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mcmTable.setStatus("current")
_McmEntry_Object = MibTableRow
mcmEntry = _McmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1)
)
mcmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mcmEntry.setStatus("current")
_McmMoId_Type = DisplayString
_McmMoId_Object = MibTableColumn
mcmMoId = _McmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 1),
    _McmMoId_Type()
)
mcmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcmMoId.setStatus("current")
_McmProvType_Type = InfnEqptType
_McmProvType_Object = MibTableColumn
mcmProvType = _McmProvType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 2),
    _McmProvType_Type()
)
mcmProvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcmProvType.setStatus("current")


class _McmRedundancyStatus_Type(Integer32):
    """Custom type mcmRedundancyStatus based on Integer32"""
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


_McmRedundancyStatus_Type.__name__ = "Integer32"
_McmRedundancyStatus_Object = MibTableColumn
mcmRedundancyStatus = _McmRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 3),
    _McmRedundancyStatus_Type()
)
mcmRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmRedundancyStatus.setStatus("current")
_McmBrandingFault_Type = TruthValue
_McmBrandingFault_Object = MibTableColumn
mcmBrandingFault = _McmBrandingFault_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 4),
    _McmBrandingFault_Type()
)
mcmBrandingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmBrandingFault.setStatus("current")
_McmRowStatus_Type = RowStatus
_McmRowStatus_Object = MibTableColumn
mcmRowStatus = _McmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 5),
    _McmRowStatus_Type()
)
mcmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcmRowStatus.setStatus("current")
_McmConformance_ObjectIdentity = ObjectIdentity
mcmConformance = _McmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3)
)
_McmCompliances_ObjectIdentity = ObjectIdentity
mcmCompliances = _McmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3, 1)
)
_McmGroups_ObjectIdentity = ObjectIdentity
mcmGroups = _McmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3, 2)
)

# Managed Objects groups

mcmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3, 2, 1)
)
mcmGroup.setObjects(
      *(("INFINERA-ENTITY-MCM-MIB", "mcmBrandingFault"),
        ("INFINERA-ENTITY-MCM-MIB", "mcmMoId"),
        ("INFINERA-ENTITY-MCM-MIB", "mcmProvType"),
        ("INFINERA-ENTITY-MCM-MIB", "mcmRedundancyStatus"),
        ("INFINERA-ENTITY-MCM-MIB", "mcmRowStatus"))
)
if mibBuilder.loadTexts:
    mcmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mcmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3, 1, 1)
)
mcmCompliance.setObjects(
    ("INFINERA-ENTITY-MCM-MIB", "mcmGroup")
)
if mibBuilder.loadTexts:
    mcmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-MCM-MIB",
    **{"mcmMIB": mcmMIB,
       "mcmTable": mcmTable,
       "mcmEntry": mcmEntry,
       "mcmMoId": mcmMoId,
       "mcmProvType": mcmProvType,
       "mcmRedundancyStatus": mcmRedundancyStatus,
       "mcmBrandingFault": mcmBrandingFault,
       "mcmRowStatus": mcmRowStatus,
       "mcmConformance": mcmConformance,
       "mcmCompliances": mcmCompliances,
       "mcmCompliance": mcmCompliance,
       "mcmGroups": mcmGroups,
       "mcmGroup": mcmGroup}
)
