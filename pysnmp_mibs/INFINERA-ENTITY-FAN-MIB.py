# SNMP MIB module (INFINERA-ENTITY-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-FAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:14 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 1, 1)
)
fanEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")
_FanMoId_Type = DisplayString
_FanMoId_Object = MibTableColumn
fanMoId = _FanMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 1, 1, 1),
    _FanMoId_Type()
)
fanMoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanMoId.setStatus("current")
_FanProvEqptType_Type = InfnEqptType
_FanProvEqptType_Object = MibTableColumn
fanProvEqptType = _FanProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 1, 1, 2),
    _FanProvEqptType_Type()
)
fanProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProvEqptType.setStatus("current")
_FanConformance_ObjectIdentity = ObjectIdentity
fanConformance = _FanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3)
)
_FanCompliances_ObjectIdentity = ObjectIdentity
fanCompliances = _FanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3, 1)
)
_FanGroups_ObjectIdentity = ObjectIdentity
fanGroups = _FanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3, 2)
)

# Managed Objects groups

fanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3, 2, 1)
)
fanGroup.setObjects(
      *(("INFINERA-ENTITY-FAN-MIB", "fanMoId"),
        ("INFINERA-ENTITY-FAN-MIB", "fanProvEqptType"))
)
if mibBuilder.loadTexts:
    fanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3, 1, 1)
)
fanCompliance.setObjects(
    ("INFINERA-ENTITY-FAN-MIB", "fanGroup")
)
if mibBuilder.loadTexts:
    fanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-FAN-MIB",
    **{"fanMIB": fanMIB,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanMoId": fanMoId,
       "fanProvEqptType": fanProvEqptType,
       "fanConformance": fanConformance,
       "fanCompliances": fanCompliances,
       "fanCompliance": fanCompliance,
       "fanGroups": fanGroups,
       "fanGroup": fanGroup}
)
