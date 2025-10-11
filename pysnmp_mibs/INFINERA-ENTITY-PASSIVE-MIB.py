# SNMP MIB module (INFINERA-ENTITY-PASSIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-PASSIVE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:16 2025
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

(commonEquipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "commonEquipment")

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

passiveMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    passiveMIB.setRevisions(
        ("2017-01-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PassiveTable_Object = MibTable
passiveTable = _PassiveTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    passiveTable.setStatus("current")
_PassiveEntry_Object = MibTableRow
passiveEntry = _PassiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1)
)
passiveEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    passiveEntry.setStatus("current")
_PassiveMoId_Type = DisplayString
_PassiveMoId_Object = MibTableColumn
passiveMoId = _PassiveMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 1),
    _PassiveMoId_Type()
)
passiveMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    passiveMoId.setStatus("current")
_PassiveProvEqptType_Type = InfnEqptType
_PassiveProvEqptType_Object = MibTableColumn
passiveProvEqptType = _PassiveProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 2),
    _PassiveProvEqptType_Type()
)
passiveProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    passiveProvEqptType.setStatus("current")
_PassiveLabel_Type = DisplayString
_PassiveLabel_Object = MibTableColumn
passiveLabel = _PassiveLabel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 3),
    _PassiveLabel_Type()
)
passiveLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passiveLabel.setStatus("current")
_PassiveProvSerialNumber_Type = DisplayString
_PassiveProvSerialNumber_Object = MibTableColumn
passiveProvSerialNumber = _PassiveProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 4),
    _PassiveProvSerialNumber_Type()
)
passiveProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passiveProvSerialNumber.setStatus("current")
_PassiveNumSystemPorts_Type = Integer32
_PassiveNumSystemPorts_Object = MibTableColumn
passiveNumSystemPorts = _PassiveNumSystemPorts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 5),
    _PassiveNumSystemPorts_Type()
)
passiveNumSystemPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passiveNumSystemPorts.setStatus("current")
_PassiveNumLinePorts_Type = Integer32
_PassiveNumLinePorts_Object = MibTableColumn
passiveNumLinePorts = _PassiveNumLinePorts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 6),
    _PassiveNumLinePorts_Type()
)
passiveNumLinePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passiveNumLinePorts.setStatus("current")
_PassiveConformance_ObjectIdentity = ObjectIdentity
passiveConformance = _PassiveConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3)
)
_PassiveCompliances_ObjectIdentity = ObjectIdentity
passiveCompliances = _PassiveCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3, 1)
)
_PassiveGroups_ObjectIdentity = ObjectIdentity
passiveGroups = _PassiveGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3, 2)
)

# Managed Objects groups

passiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3, 2, 1)
)
passiveGroup.setObjects(
      *(("INFINERA-ENTITY-PASSIVE-MIB", "passiveMoId"),
        ("INFINERA-ENTITY-PASSIVE-MIB", "passiveProvEqptType"),
        ("INFINERA-ENTITY-PASSIVE-MIB", "passiveLabel"),
        ("INFINERA-ENTITY-PASSIVE-MIB", "passiveProvSerialNumber"),
        ("INFINERA-ENTITY-PASSIVE-MIB", "passiveNumSystemPorts"),
        ("INFINERA-ENTITY-PASSIVE-MIB", "passiveNumLinePorts"))
)
if mibBuilder.loadTexts:
    passiveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

passiveCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3, 1, 1)
)
passiveCompliance.setObjects(
    ("INFINERA-ENTITY-PASSIVE-MIB", "passiveGroup")
)
if mibBuilder.loadTexts:
    passiveCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-PASSIVE-MIB",
    **{"passiveMIB": passiveMIB,
       "passiveTable": passiveTable,
       "passiveEntry": passiveEntry,
       "passiveMoId": passiveMoId,
       "passiveProvEqptType": passiveProvEqptType,
       "passiveLabel": passiveLabel,
       "passiveProvSerialNumber": passiveProvSerialNumber,
       "passiveNumSystemPorts": passiveNumSystemPorts,
       "passiveNumLinePorts": passiveNumLinePorts,
       "passiveConformance": passiveConformance,
       "passiveCompliances": passiveCompliances,
       "passiveCompliance": passiveCompliance,
       "passiveGroups": passiveGroups,
       "passiveGroup": passiveGroup}
)
