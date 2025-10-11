# SNMP MIB module (INFINERA-ENTITY-IMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-IMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:26 2025
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

(InfnEqptType,
 InfnFlashStatus) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEqptType",
    "InfnFlashStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

immMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ImmTable_Object = MibTable
immTable = _ImmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1)
)
if mibBuilder.loadTexts:
    immTable.setStatus("current")
_ImmEntry_Object = MibTableRow
immEntry = _ImmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1)
)
immEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    immEntry.setStatus("current")
_ImmMoId_Type = DisplayString
_ImmMoId_Object = MibTableColumn
immMoId = _ImmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1, 1),
    _ImmMoId_Type()
)
immMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    immMoId.setStatus("current")
_ImmProvEqptType_Type = InfnEqptType
_ImmProvEqptType_Object = MibTableColumn
immProvEqptType = _ImmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1, 2),
    _ImmProvEqptType_Type()
)
immProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    immProvEqptType.setStatus("current")


class _ImmInterfaceTypeNCT_Type(Integer32):
    """Custom type immInterfaceTypeNCT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_ImmInterfaceTypeNCT_Type.__name__ = "Integer32"
_ImmInterfaceTypeNCT_Object = MibTableColumn
immInterfaceTypeNCT = _ImmInterfaceTypeNCT_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1, 3),
    _ImmInterfaceTypeNCT_Type()
)
immInterfaceTypeNCT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    immInterfaceTypeNCT.setStatus("current")
_ImmFlashStatus_Type = InfnFlashStatus
_ImmFlashStatus_Object = MibTableColumn
immFlashStatus = _ImmFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1, 4),
    _ImmFlashStatus_Type()
)
immFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    immFlashStatus.setStatus("current")
_ImmConformance_ObjectIdentity = ObjectIdentity
immConformance = _ImmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3)
)
_ImmCompliances_ObjectIdentity = ObjectIdentity
immCompliances = _ImmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3, 1)
)
_ImmGroups_ObjectIdentity = ObjectIdentity
immGroups = _ImmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3, 2)
)

# Managed Objects groups

immGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3, 2, 1)
)
immGroup.setObjects(
      *(("INFINERA-ENTITY-IMM-MIB", "immMoId"),
        ("INFINERA-ENTITY-IMM-MIB", "immProvEqptType"),
        ("INFINERA-ENTITY-IMM-MIB", "immInterfaceTypeNCT"),
        ("INFINERA-ENTITY-IMM-MIB", "immFlashStatus"))
)
if mibBuilder.loadTexts:
    immGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

immCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3, 1, 1)
)
immCompliance.setObjects(
    ("INFINERA-ENTITY-IMM-MIB", "immGroup")
)
if mibBuilder.loadTexts:
    immCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-IMM-MIB",
    **{"immMIB": immMIB,
       "immTable": immTable,
       "immEntry": immEntry,
       "immMoId": immMoId,
       "immProvEqptType": immProvEqptType,
       "immInterfaceTypeNCT": immInterfaceTypeNCT,
       "immFlashStatus": immFlashStatus,
       "immConformance": immConformance,
       "immCompliances": immCompliances,
       "immCompliance": immCompliance,
       "immGroups": immGroups,
       "immGroup": immGroup}
)
