# SNMP MIB module (ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:32 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(EntitySensorValue,
 entPhySensorOperStatus,
 entPhySensorPrecision,
 entPhySensorScale,
 entPhySensorUnitsDisplay,
 entPhySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue",
    "entPhySensorOperStatus",
    "entPhySensorPrecision",
    "entPhySensorScale",
    "entPhySensorUnitsDisplay",
    "entPhySensorValue")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

etsysEntitySensorExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85)
)
if mibBuilder.loadTexts:
    etsysEntitySensorExtMIB.setRevisions(
        ("2014-05-13 12:06",
         "2011-10-14 14:49")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysEntitySensorExtObjects_ObjectIdentity = ObjectIdentity
etsysEntitySensorExtObjects = _EtsysEntitySensorExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1)
)
_EtsysEntitySensorExtNotifications_ObjectIdentity = ObjectIdentity
etsysEntitySensorExtNotifications = _EtsysEntitySensorExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 0)
)
_EtsysEntityTempSensorExt_ObjectIdentity = ObjectIdentity
etsysEntityTempSensorExt = _EtsysEntityTempSensorExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 1)
)
_EtsysEntityTempSensorExtTable_Object = MibTable
etsysEntityTempSensorExtTable = _EtsysEntityTempSensorExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysEntityTempSensorExtTable.setStatus("current")
_EtsysEntityTempSensorExtEntry_Object = MibTableRow
etsysEntityTempSensorExtEntry = _EtsysEntityTempSensorExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 1, 1, 1)
)
etsysEntityTempSensorExtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    etsysEntityTempSensorExtEntry.setStatus("current")


class _EtsysEntityTempSensorState_Type(Integer32):
    """Custom type etsysEntityTempSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("cold", 2),
          ("cool", 3),
          ("normal", 4),
          ("warm", 5),
          ("hot", 6))
    )


_EtsysEntityTempSensorState_Type.__name__ = "Integer32"
_EtsysEntityTempSensorState_Object = MibTableColumn
etsysEntityTempSensorState = _EtsysEntityTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 1, 1, 1, 1),
    _EtsysEntityTempSensorState_Type()
)
etsysEntityTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntityTempSensorState.setStatus("current")
_EtsysEntityTempSensorHotTemp_Type = EntitySensorValue
_EtsysEntityTempSensorHotTemp_Object = MibTableColumn
etsysEntityTempSensorHotTemp = _EtsysEntityTempSensorHotTemp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 1, 1, 1, 2),
    _EtsysEntityTempSensorHotTemp_Type()
)
etsysEntityTempSensorHotTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntityTempSensorHotTemp.setStatus("current")
_EtsysEntityTempSensorWarmTemp_Type = EntitySensorValue
_EtsysEntityTempSensorWarmTemp_Object = MibTableColumn
etsysEntityTempSensorWarmTemp = _EtsysEntityTempSensorWarmTemp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 1, 1, 1, 3),
    _EtsysEntityTempSensorWarmTemp_Type()
)
etsysEntityTempSensorWarmTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntityTempSensorWarmTemp.setStatus("current")
_EtsysEntityTempSensorCoolTemp_Type = EntitySensorValue
_EtsysEntityTempSensorCoolTemp_Object = MibTableColumn
etsysEntityTempSensorCoolTemp = _EtsysEntityTempSensorCoolTemp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 1, 1, 1, 4),
    _EtsysEntityTempSensorCoolTemp_Type()
)
etsysEntityTempSensorCoolTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntityTempSensorCoolTemp.setStatus("current")
_EtsysEntityTempSensorColdTemp_Type = EntitySensorValue
_EtsysEntityTempSensorColdTemp_Object = MibTableColumn
etsysEntityTempSensorColdTemp = _EtsysEntityTempSensorColdTemp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 1, 1, 1, 5),
    _EtsysEntityTempSensorColdTemp_Type()
)
etsysEntityTempSensorColdTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntityTempSensorColdTemp.setStatus("current")


class _EtsysEntityTempSensorTrapEnable_Type(EnabledStatus):
    """Custom type etsysEntityTempSensorTrapEnable based on EnabledStatus"""
    defaultValue = 1


_EtsysEntityTempSensorTrapEnable_Type.__name__ = "EnabledStatus"
_EtsysEntityTempSensorTrapEnable_Object = MibTableColumn
etsysEntityTempSensorTrapEnable = _EtsysEntityTempSensorTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 1, 1, 1, 6),
    _EtsysEntityTempSensorTrapEnable_Type()
)
etsysEntityTempSensorTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEntityTempSensorTrapEnable.setStatus("current")
_EtsysEntitySfpSensorExt_ObjectIdentity = ObjectIdentity
etsysEntitySfpSensorExt = _EtsysEntitySfpSensorExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 2)
)
_EtsysEntitySfpSensorExtTable_Object = MibTable
etsysEntitySfpSensorExtTable = _EtsysEntitySfpSensorExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysEntitySfpSensorExtTable.setStatus("current")
_EtsysEntitySfpSensorExtEntry_Object = MibTableRow
etsysEntitySfpSensorExtEntry = _EtsysEntitySfpSensorExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 2, 1, 1)
)
etsysEntitySfpSensorExtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    etsysEntitySfpSensorExtEntry.setStatus("current")


class _EtsysEntitySfpSensorState_Type(Integer32):
    """Custom type etsysEntitySfpSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("normal", 4),
          ("highWarning", 5),
          ("highAlarm", 6))
    )


_EtsysEntitySfpSensorState_Type.__name__ = "Integer32"
_EtsysEntitySfpSensorState_Object = MibTableColumn
etsysEntitySfpSensorState = _EtsysEntitySfpSensorState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 2, 1, 1, 1),
    _EtsysEntitySfpSensorState_Type()
)
etsysEntitySfpSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntitySfpSensorState.setStatus("current")
_EtsysEntitySfpSensorHighAlarm_Type = EntitySensorValue
_EtsysEntitySfpSensorHighAlarm_Object = MibTableColumn
etsysEntitySfpSensorHighAlarm = _EtsysEntitySfpSensorHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 2, 1, 1, 2),
    _EtsysEntitySfpSensorHighAlarm_Type()
)
etsysEntitySfpSensorHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntitySfpSensorHighAlarm.setStatus("current")
_EtsysEntitySfpSensorHighWarning_Type = EntitySensorValue
_EtsysEntitySfpSensorHighWarning_Object = MibTableColumn
etsysEntitySfpSensorHighWarning = _EtsysEntitySfpSensorHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 2, 1, 1, 3),
    _EtsysEntitySfpSensorHighWarning_Type()
)
etsysEntitySfpSensorHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntitySfpSensorHighWarning.setStatus("current")
_EtsysEntitySfpSensorLowWarning_Type = EntitySensorValue
_EtsysEntitySfpSensorLowWarning_Object = MibTableColumn
etsysEntitySfpSensorLowWarning = _EtsysEntitySfpSensorLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 2, 1, 1, 4),
    _EtsysEntitySfpSensorLowWarning_Type()
)
etsysEntitySfpSensorLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntitySfpSensorLowWarning.setStatus("current")
_EtsysEntitySfpSensorLowAlarm_Type = EntitySensorValue
_EtsysEntitySfpSensorLowAlarm_Object = MibTableColumn
etsysEntitySfpSensorLowAlarm = _EtsysEntitySfpSensorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 2, 1, 1, 5),
    _EtsysEntitySfpSensorLowAlarm_Type()
)
etsysEntitySfpSensorLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEntitySfpSensorLowAlarm.setStatus("current")


class _EtsysEntitySfpSensorTrapEnable_Type(EnabledStatus):
    """Custom type etsysEntitySfpSensorTrapEnable based on EnabledStatus"""
    defaultValue = 1


_EtsysEntitySfpSensorTrapEnable_Type.__name__ = "EnabledStatus"
_EtsysEntitySfpSensorTrapEnable_Object = MibScalar
etsysEntitySfpSensorTrapEnable = _EtsysEntitySfpSensorTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 2, 2),
    _EtsysEntitySfpSensorTrapEnable_Type()
)
etsysEntitySfpSensorTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEntitySfpSensorTrapEnable.setStatus("current")
_EtsysEntitySensorExtConformance_ObjectIdentity = ObjectIdentity
etsysEntitySensorExtConformance = _EtsysEntitySensorExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 2)
)
_EtsysEntitySensorExtGroups_ObjectIdentity = ObjectIdentity
etsysEntitySensorExtGroups = _EtsysEntitySensorExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 2, 1)
)
_EtsysEntitySensorExtCompliances_ObjectIdentity = ObjectIdentity
etsysEntitySensorExtCompliances = _EtsysEntitySensorExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 2, 2)
)

# Managed Objects groups

etsysEntityTempSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 2, 1, 1)
)
etsysEntityTempSensorGroup.setObjects(
      *(("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorState"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorHotTemp"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorWarmTemp"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorCoolTemp"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorColdTemp"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorTrapEnable"))
)
if mibBuilder.loadTexts:
    etsysEntityTempSensorGroup.setStatus("current")

etsysEntitySfpSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 2, 1, 3)
)
etsysEntitySfpSensorGroup.setObjects(
      *(("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorState"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorHighAlarm"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorHighWarning"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorLowWarning"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorLowAlarm"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorTrapEnable"))
)
if mibBuilder.loadTexts:
    etsysEntitySfpSensorGroup.setStatus("current")


# Notification objects

etsysEntityTempSensorStateChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 0, 1)
)
etsysEntityTempSensorStateChng.setObjects(
      *(("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorState"),
        ("ENTITY-SENSOR-MIB", "entPhySensorOperStatus"),
        ("ENTITY-SENSOR-MIB", "entPhySensorScale"),
        ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorUnitsDisplay"))
)
if mibBuilder.loadTexts:
    etsysEntityTempSensorStateChng.setStatus(
        "current"
    )

etsysEntitySfpSensorStateChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 1, 0, 2)
)
etsysEntitySfpSensorStateChng.setObjects(
      *(("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorState"),
        ("ENTITY-SENSOR-MIB", "entPhySensorOperStatus"),
        ("ENTITY-SENSOR-MIB", "entPhySensorScale"),
        ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorUnitsDisplay"))
)
if mibBuilder.loadTexts:
    etsysEntitySfpSensorStateChng.setStatus(
        "current"
    )


# Notifications groups

etsysEntityTempSensorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 2, 1, 2)
)
etsysEntityTempSensorNotificationGroup.setObjects(
    ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorStateChng")
)
if mibBuilder.loadTexts:
    etsysEntityTempSensorNotificationGroup.setStatus(
        "current"
    )

etsysEntitySfpSensorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 2, 1, 4)
)
etsysEntitySfpSensorNotificationGroup.setObjects(
    ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorStateChng")
)
if mibBuilder.loadTexts:
    etsysEntitySfpSensorNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysEntitySensorExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 2, 2, 1)
)
etsysEntitySensorExtCompliance.setObjects(
      *(("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorGroup"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntityTempSensorNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysEntitySensorExtCompliance.setStatus(
        "current"
    )

etsysEntitySensorSfpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 85, 2, 2, 2)
)
etsysEntitySensorSfpExtCompliance.setObjects(
      *(("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorGroup"),
        ("ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB", "etsysEntitySfpSensorNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysEntitySensorSfpExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-ENTITY-SENSOR-MIB-EXT-MIB",
    **{"etsysEntitySensorExtMIB": etsysEntitySensorExtMIB,
       "etsysEntitySensorExtObjects": etsysEntitySensorExtObjects,
       "etsysEntitySensorExtNotifications": etsysEntitySensorExtNotifications,
       "etsysEntityTempSensorStateChng": etsysEntityTempSensorStateChng,
       "etsysEntitySfpSensorStateChng": etsysEntitySfpSensorStateChng,
       "etsysEntityTempSensorExt": etsysEntityTempSensorExt,
       "etsysEntityTempSensorExtTable": etsysEntityTempSensorExtTable,
       "etsysEntityTempSensorExtEntry": etsysEntityTempSensorExtEntry,
       "etsysEntityTempSensorState": etsysEntityTempSensorState,
       "etsysEntityTempSensorHotTemp": etsysEntityTempSensorHotTemp,
       "etsysEntityTempSensorWarmTemp": etsysEntityTempSensorWarmTemp,
       "etsysEntityTempSensorCoolTemp": etsysEntityTempSensorCoolTemp,
       "etsysEntityTempSensorColdTemp": etsysEntityTempSensorColdTemp,
       "etsysEntityTempSensorTrapEnable": etsysEntityTempSensorTrapEnable,
       "etsysEntitySfpSensorExt": etsysEntitySfpSensorExt,
       "etsysEntitySfpSensorExtTable": etsysEntitySfpSensorExtTable,
       "etsysEntitySfpSensorExtEntry": etsysEntitySfpSensorExtEntry,
       "etsysEntitySfpSensorState": etsysEntitySfpSensorState,
       "etsysEntitySfpSensorHighAlarm": etsysEntitySfpSensorHighAlarm,
       "etsysEntitySfpSensorHighWarning": etsysEntitySfpSensorHighWarning,
       "etsysEntitySfpSensorLowWarning": etsysEntitySfpSensorLowWarning,
       "etsysEntitySfpSensorLowAlarm": etsysEntitySfpSensorLowAlarm,
       "etsysEntitySfpSensorTrapEnable": etsysEntitySfpSensorTrapEnable,
       "etsysEntitySensorExtConformance": etsysEntitySensorExtConformance,
       "etsysEntitySensorExtGroups": etsysEntitySensorExtGroups,
       "etsysEntityTempSensorGroup": etsysEntityTempSensorGroup,
       "etsysEntityTempSensorNotificationGroup": etsysEntityTempSensorNotificationGroup,
       "etsysEntitySfpSensorGroup": etsysEntitySfpSensorGroup,
       "etsysEntitySfpSensorNotificationGroup": etsysEntitySfpSensorNotificationGroup,
       "etsysEntitySensorExtCompliances": etsysEntitySensorExtCompliances,
       "etsysEntitySensorExtCompliance": etsysEntitySensorExtCompliance,
       "etsysEntitySensorSfpExtCompliance": etsysEntitySensorSfpExtCompliance}
)
