# SNMP MIB module (MELLANOX-ENTITY-STATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mellanox/MELLANOX-ENTITY-STATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:39 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(mellanoxEntState,) = mibBuilder.importSymbols(
    "MELLANOX-SMI-MIB",
    "mellanoxEntState")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

mellanoxEntStateMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 7, 1)
)
if mibBuilder.loadTexts:
    mellanoxEntStateMib.setRevisions(
        ("2017-07-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ModuleStateType(TextualConvention, Integer32):
    status = "current"
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
        *(("ok", 1),
          ("disabled", 2),
          ("reset", 3),
          ("missing", 4),
          ("criticalFault", 5),
          ("nonCriticalFault", 6),
          ("unknown", 7))
    )



# MIB Managed Objects in the order of their OIDs

_MellanoxEntStateMibNotifications_ObjectIdentity = ObjectIdentity
mellanoxEntStateMibNotifications = _MellanoxEntStateMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 7, 1, 0)
)
_MellanoxEntStateMibObjects_ObjectIdentity = ObjectIdentity
mellanoxEntStateMibObjects = _MellanoxEntStateMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 7, 1, 1)
)
_MellanoxEntStateTable_Object = MibTable
mellanoxEntStateTable = _MellanoxEntStateTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mellanoxEntStateTable.setStatus("current")
_MellanoxEntStateEntry_Object = MibTableRow
mellanoxEntStateEntry = _MellanoxEntStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1, 1)
)
mellanoxEntStateEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mellanoxEntStateEntry.setStatus("current")
_MellanoxEntStateModuleCurrentState_Type = ModuleStateType
_MellanoxEntStateModuleCurrentState_Object = MibTableColumn
mellanoxEntStateModuleCurrentState = _MellanoxEntStateModuleCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1, 1, 1),
    _MellanoxEntStateModuleCurrentState_Type()
)
mellanoxEntStateModuleCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxEntStateModuleCurrentState.setStatus("current")
_MellanoxEntStateModulePreviousState_Type = ModuleStateType
_MellanoxEntStateModulePreviousState_Object = MibTableColumn
mellanoxEntStateModulePreviousState = _MellanoxEntStateModulePreviousState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1, 1, 2),
    _MellanoxEntStateModulePreviousState_Type()
)
mellanoxEntStateModulePreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxEntStateModulePreviousState.setStatus("current")
_MellanoxEntStateModuleStateDescr_Type = SnmpAdminString
_MellanoxEntStateModuleStateDescr_Object = MibTableColumn
mellanoxEntStateModuleStateDescr = _MellanoxEntStateModuleStateDescr_Object(
    (1, 3, 6, 1, 4, 1, 33049, 7, 1, 1, 1, 1, 3),
    _MellanoxEntStateModuleStateDescr_Type()
)
mellanoxEntStateModuleStateDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxEntStateModuleStateDescr.setStatus("current")

# Managed Objects groups


# Notification objects

mellanoxEntStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 7, 1, 0, 1)
)
mellanoxEntStateChangeAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("MELLANOX-ENTITY-STATE-MIB", "entPhysicalDescr"),
        ("MELLANOX-ENTITY-STATE-MIB", "entPhysicalName"),
        ("MELLANOX-ENTITY-STATE-MIB", "mellanoxEntStateModuleCurrentState"),
        ("MELLANOX-ENTITY-STATE-MIB", "mellanoxEntStateModulePreviousState"),
        ("MELLANOX-ENTITY-STATE-MIB", "mellanoxEntStateModuleStateDescr"),
        ("MELLANOX-ENTITY-STATE-MIB", "entStateAlarm"))
)
if mibBuilder.loadTexts:
    mellanoxEntStateChangeAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MELLANOX-ENTITY-STATE-MIB",
    **{"ModuleStateType": ModuleStateType,
       "mellanoxEntStateMib": mellanoxEntStateMib,
       "mellanoxEntStateMibNotifications": mellanoxEntStateMibNotifications,
       "mellanoxEntStateChangeAlarm": mellanoxEntStateChangeAlarm,
       "mellanoxEntStateMibObjects": mellanoxEntStateMibObjects,
       "mellanoxEntStateTable": mellanoxEntStateTable,
       "mellanoxEntStateEntry": mellanoxEntStateEntry,
       "mellanoxEntStateModuleCurrentState": mellanoxEntStateModuleCurrentState,
       "mellanoxEntStateModulePreviousState": mellanoxEntStateModulePreviousState,
       "mellanoxEntStateModuleStateDescr": mellanoxEntStateModuleStateDescr}
)
