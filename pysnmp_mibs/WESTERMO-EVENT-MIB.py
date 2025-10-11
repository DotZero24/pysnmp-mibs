# SNMP MIB module (WESTERMO-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-EVENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:31 2025
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

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(entPhySensorPrecision,
 entPhySensorScale,
 entPhySensorType,
 entPhySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "entPhySensorPrecision",
    "entPhySensorScale",
    "entPhySensorType",
    "entPhySensorValue")

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

(common,) = mibBuilder.importSymbols(
    "WESTERMO-OID-MIB",
    "common")


# MODULE-IDENTITY

event = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3)
)
if mibBuilder.loadTexts:
    event.setRevisions(
        ("2019-09-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EventStatus_ObjectIdentity = ObjectIdentity
eventStatus = _EventStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 1)
)
_EventStatusTable_Object = MibTable
eventStatusTable = _EventStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    eventStatusTable.setStatus("current")
_EventStatusEntry_Object = MibTableRow
eventStatusEntry = _EventStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 1, 1, 1)
)
eventStatusEntry.setIndexNames(
    (0, "WESTERMO-EVENT-MIB", "eventStatusTriggerId"),
)
if mibBuilder.loadTexts:
    eventStatusEntry.setStatus("current")


class _EventStatusTriggerId_Type(Integer32):
    """Custom type eventStatusTriggerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EventStatusTriggerId_Type.__name__ = "Integer32"
_EventStatusTriggerId_Object = MibTableColumn
eventStatusTriggerId = _EventStatusTriggerId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 1, 1, 1, 1),
    _EventStatusTriggerId_Type()
)
eventStatusTriggerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventStatusTriggerId.setStatus("current")
_EventConfig_ObjectIdentity = ObjectIdentity
eventConfig = _EventConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 2)
)
_EventNotifications_ObjectIdentity = ObjectIdentity
eventNotifications = _EventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3)
)
_PingNotifications_ObjectIdentity = ObjectIdentity
pingNotifications = _PingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 2)
)
_PingNotificationPrefix_ObjectIdentity = ObjectIdentity
pingNotificationPrefix = _PingNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 2, 0)
)
_PowerNotifications_ObjectIdentity = ObjectIdentity
powerNotifications = _PowerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 3)
)
_PowerNotificationPrefix_ObjectIdentity = ObjectIdentity
powerNotificationPrefix = _PowerNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 3, 0)
)
_TemperatureNotifications_ObjectIdentity = ObjectIdentity
temperatureNotifications = _TemperatureNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 4)
)
_TemperatureNotificationPrefix_ObjectIdentity = ObjectIdentity
temperatureNotificationPrefix = _TemperatureNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 4, 0)
)
_EventConformance_ObjectIdentity = ObjectIdentity
eventConformance = _EventConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 4)
)
_EventGroups_ObjectIdentity = ObjectIdentity
eventGroups = _EventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 4, 1)
)
_EventCompliances_ObjectIdentity = ObjectIdentity
eventCompliances = _EventCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 4, 2)
)

# Managed Objects groups

eventStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 4, 1, 1)
)
eventStatusGroup.setObjects(
    ("WESTERMO-EVENT-MIB", "eventStatusTriggerId")
)
if mibBuilder.loadTexts:
    eventStatusGroup.setStatus("current")


# Notification objects

pingNotificationOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 2, 0, 1)
)
pingNotificationOK.setObjects(
    ("WESTERMO-EVENT-MIB", "eventStatusTriggerId")
)
if mibBuilder.loadTexts:
    pingNotificationOK.setStatus(
        "current"
    )

pingNotificationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 2, 0, 2)
)
pingNotificationWarning.setObjects(
    ("WESTERMO-EVENT-MIB", "eventStatusTriggerId")
)
if mibBuilder.loadTexts:
    pingNotificationWarning.setStatus(
        "current"
    )

powerSupplyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 3, 0, 1)
)
powerSupplyHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"))
)
if mibBuilder.loadTexts:
    powerSupplyHigh.setStatus(
        "current"
    )

powerSupplyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 3, 0, 2)
)
powerSupplyLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"))
)
if mibBuilder.loadTexts:
    powerSupplyLow.setStatus(
        "current"
    )

temperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 4, 0, 1)
)
temperatureHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorScale"),
        ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"))
)
if mibBuilder.loadTexts:
    temperatureHigh.setStatus(
        "current"
    )

temperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 3, 4, 0, 2)
)
temperatureLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorScale"),
        ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"))
)
if mibBuilder.loadTexts:
    temperatureLow.setStatus(
        "current"
    )


# Notifications groups

pingStatusGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 4, 1, 2)
)
pingStatusGroup.setObjects(
      *(("WESTERMO-EVENT-MIB", "pingNotificationOK"),
        ("WESTERMO-EVENT-MIB", "pingNotificationWarning"))
)
if mibBuilder.loadTexts:
    pingStatusGroup.setStatus(
        "current"
    )

powerStatusGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 4, 1, 3)
)
powerStatusGroup.setObjects(
      *(("WESTERMO-EVENT-MIB", "powerSupplyHigh"),
        ("WESTERMO-EVENT-MIB", "powerSupplyLow"))
)
if mibBuilder.loadTexts:
    powerStatusGroup.setStatus(
        "current"
    )

temperatureStatusGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 4, 1, 4)
)
temperatureStatusGroup.setObjects(
      *(("WESTERMO-EVENT-MIB", "temperatureHigh"),
        ("WESTERMO-EVENT-MIB", "temperatureLow"))
)
if mibBuilder.loadTexts:
    temperatureStatusGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eventCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 2, 3, 4, 2, 1)
)
eventCompliance.setObjects(
      *(("WESTERMO-EVENT-MIB", "eventStatusGroup"),
        ("WESTERMO-EVENT-MIB", "pingStatusGroup"),
        ("WESTERMO-EVENT-MIB", "powerStatusGroup"),
        ("WESTERMO-EVENT-MIB", "temperatureStatusGroup"))
)
if mibBuilder.loadTexts:
    eventCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-EVENT-MIB",
    **{"event": event,
       "eventStatus": eventStatus,
       "eventStatusTable": eventStatusTable,
       "eventStatusEntry": eventStatusEntry,
       "eventStatusTriggerId": eventStatusTriggerId,
       "eventConfig": eventConfig,
       "eventNotifications": eventNotifications,
       "pingNotifications": pingNotifications,
       "pingNotificationPrefix": pingNotificationPrefix,
       "pingNotificationOK": pingNotificationOK,
       "pingNotificationWarning": pingNotificationWarning,
       "powerNotifications": powerNotifications,
       "powerNotificationPrefix": powerNotificationPrefix,
       "powerSupplyHigh": powerSupplyHigh,
       "powerSupplyLow": powerSupplyLow,
       "temperatureNotifications": temperatureNotifications,
       "temperatureNotificationPrefix": temperatureNotificationPrefix,
       "temperatureHigh": temperatureHigh,
       "temperatureLow": temperatureLow,
       "eventConformance": eventConformance,
       "eventGroups": eventGroups,
       "eventStatusGroup": eventStatusGroup,
       "pingStatusGroup": pingStatusGroup,
       "powerStatusGroup": powerStatusGroup,
       "temperatureStatusGroup": temperatureStatusGroup,
       "eventCompliances": eventCompliances,
       "eventCompliance": eventCompliance}
)
