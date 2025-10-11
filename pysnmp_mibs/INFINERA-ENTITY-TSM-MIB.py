# SNMP MIB module (INFINERA-ENTITY-TSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-TSM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:12 2025
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

tsmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TsmTable_Object = MibTable
tsmTable = _TsmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1)
)
if mibBuilder.loadTexts:
    tsmTable.setStatus("current")
_TsmEntry_Object = MibTableRow
tsmEntry = _TsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1)
)
tsmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tsmEntry.setStatus("current")
_TsmMoId_Type = DisplayString
_TsmMoId_Object = MibTableColumn
tsmMoId = _TsmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1, 1),
    _TsmMoId_Type()
)
tsmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsmMoId.setStatus("current")
_TsmProvEqptType_Type = InfnEqptType
_TsmProvEqptType_Object = MibTableColumn
tsmProvEqptType = _TsmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1, 2),
    _TsmProvEqptType_Type()
)
tsmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsmProvEqptType.setStatus("current")
_TsmRowStatus_Type = RowStatus
_TsmRowStatus_Object = MibTableColumn
tsmRowStatus = _TsmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1, 3),
    _TsmRowStatus_Type()
)
tsmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tsmRowStatus.setStatus("current")


class _CardRedundancyState_Type(Integer32):
    """Custom type cardRedundancyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("standby", 3))
    )


_CardRedundancyState_Type.__name__ = "Integer32"
_CardRedundancyState_Object = MibTableColumn
cardRedundancyState = _CardRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1, 4),
    _CardRedundancyState_Type()
)
cardRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardRedundancyState.setStatus("current")
_TsmConformance_ObjectIdentity = ObjectIdentity
tsmConformance = _TsmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3)
)
_TsmCompliances_ObjectIdentity = ObjectIdentity
tsmCompliances = _TsmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3, 1)
)
_TsmGroups_ObjectIdentity = ObjectIdentity
tsmGroups = _TsmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3, 2)
)

# Managed Objects groups

tsmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3, 2, 1)
)
tsmGroup.setObjects(
      *(("INFINERA-ENTITY-TSM-MIB", "tsmMoId"),
        ("INFINERA-ENTITY-TSM-MIB", "tsmProvEqptType"),
        ("INFINERA-ENTITY-TSM-MIB", "tsmRowStatus"),
        ("INFINERA-ENTITY-TSM-MIB", "cardRedundancyState"))
)
if mibBuilder.loadTexts:
    tsmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tsmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3, 1, 1)
)
tsmCompliance.setObjects(
    ("INFINERA-ENTITY-TSM-MIB", "tsmGroup")
)
if mibBuilder.loadTexts:
    tsmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-TSM-MIB",
    **{"tsmMIB": tsmMIB,
       "tsmTable": tsmTable,
       "tsmEntry": tsmEntry,
       "tsmMoId": tsmMoId,
       "tsmProvEqptType": tsmProvEqptType,
       "tsmRowStatus": tsmRowStatus,
       "cardRedundancyState": cardRedundancyState,
       "tsmConformance": tsmConformance,
       "tsmCompliances": tsmCompliances,
       "tsmCompliance": tsmCompliance,
       "tsmGroups": tsmGroups,
       "tsmGroup": tsmGroup}
)
