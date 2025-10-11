# SNMP MIB module (INFINERA-ENTITY-GAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-GAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:31 2025
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

gamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GamTable_Object = MibTable
gamTable = _GamTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    gamTable.setStatus("current")
_GamEntry_Object = MibTableRow
gamEntry = _GamEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1)
)
gamEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    gamEntry.setStatus("current")
_GamMoId_Type = DisplayString
_GamMoId_Object = MibTableColumn
gamMoId = _GamMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 1),
    _GamMoId_Type()
)
gamMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gamMoId.setStatus("current")
_GamProvEqptType_Type = InfnEqptType
_GamProvEqptType_Object = MibTableColumn
gamProvEqptType = _GamProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 2),
    _GamProvEqptType_Type()
)
gamProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gamProvEqptType.setStatus("current")
_GamRowStatus_Type = RowStatus
_GamRowStatus_Object = MibTableColumn
gamRowStatus = _GamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 3),
    _GamRowStatus_Type()
)
gamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gamRowStatus.setStatus("current")


class _GamOperatingMode_Type(Integer32):
    """Custom type gamOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("gam", 2),
          ("aseSource", 3),
          ("aseGain", 4))
    )


_GamOperatingMode_Type.__name__ = "Integer32"
_GamOperatingMode_Object = MibTableColumn
gamOperatingMode = _GamOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 4),
    _GamOperatingMode_Type()
)
gamOperatingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gamOperatingMode.setStatus("current")


class _GamInstOperatingMode_Type(Integer32):
    """Custom type gamInstOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("gam", 2),
          ("aseSource", 3),
          ("aseGain", 4))
    )


_GamInstOperatingMode_Type.__name__ = "Integer32"
_GamInstOperatingMode_Object = MibTableColumn
gamInstOperatingMode = _GamInstOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 5),
    _GamInstOperatingMode_Type()
)
gamInstOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamInstOperatingMode.setStatus("current")
_GamConformance_ObjectIdentity = ObjectIdentity
gamConformance = _GamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3)
)
_GamCompliances_ObjectIdentity = ObjectIdentity
gamCompliances = _GamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3, 1)
)
_GamGroups_ObjectIdentity = ObjectIdentity
gamGroups = _GamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3, 2)
)

# Managed Objects groups

gamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3, 2, 1)
)
gamGroup.setObjects(
      *(("INFINERA-ENTITY-GAM-MIB", "gamMoId"),
        ("INFINERA-ENTITY-GAM-MIB", "gamProvEqptType"),
        ("INFINERA-ENTITY-GAM-MIB", "gamRowStatus"),
        ("INFINERA-ENTITY-GAM-MIB", "gamOperatingMode"),
        ("INFINERA-ENTITY-GAM-MIB", "gamInstOperatingMode"))
)
if mibBuilder.loadTexts:
    gamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3, 1, 1)
)
gamCompliance.setObjects(
    ("INFINERA-ENTITY-GAM-MIB", "gamGroup")
)
if mibBuilder.loadTexts:
    gamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-GAM-MIB",
    **{"gamMIB": gamMIB,
       "gamTable": gamTable,
       "gamEntry": gamEntry,
       "gamMoId": gamMoId,
       "gamProvEqptType": gamProvEqptType,
       "gamRowStatus": gamRowStatus,
       "gamOperatingMode": gamOperatingMode,
       "gamInstOperatingMode": gamInstOperatingMode,
       "gamConformance": gamConformance,
       "gamCompliances": gamCompliances,
       "gamCompliance": gamCompliance,
       "gamGroups": gamGroups,
       "gamGroup": gamGroup}
)
