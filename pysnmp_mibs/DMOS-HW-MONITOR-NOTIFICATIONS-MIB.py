# SNMP MIB module (DMOS-HW-MONITOR-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DMOS-HW-MONITOR-NOTIFICATIONS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:48 2025
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

(alarmNotifications,
 notificationAlarmState,
 notificationInfo,
 notificationName,
 notificationSeverity,
 notificationSourceType,
 notificationSourceValue,
 notificationTime) = mibBuilder.importSymbols(
    "DMOS-NOTIFICATIONS-MIB",
    "alarmNotifications",
    "notificationAlarmState",
    "notificationInfo",
    "notificationName",
    "notificationSeverity",
    "notificationSourceType",
    "notificationSourceValue",
    "notificationTime")

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

dmosHwMonNotificationsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2)
)
if mibBuilder.loadTexts:
    dmosHwMonNotificationsMIB.setRevisions(
        ("2017-01-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DmosHwMonNotificationObjects_ObjectIdentity = ObjectIdentity
dmosHwMonNotificationObjects = _DmosHwMonNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 1)
)
_DmosHwMonValue_Type = Integer32
_DmosHwMonValue_Object = MibScalar
dmosHwMonValue = _DmosHwMonValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 1, 1),
    _DmosHwMonValue_Type()
)
dmosHwMonValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmosHwMonValue.setStatus("current")
_DmosHwMonLimitValue_Type = Integer32
_DmosHwMonLimitValue_Object = MibScalar
dmosHwMonLimitValue = _DmosHwMonLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 1, 2),
    _DmosHwMonLimitValue_Type()
)
dmosHwMonLimitValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmosHwMonLimitValue.setStatus("current")
_DmosHwMonNotificationGroups_ObjectIdentity = ObjectIdentity
dmosHwMonNotificationGroups = _DmosHwMonNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 2)
)

# Managed Objects groups

dmosHwMonAlarmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 2, 1)
)
dmosHwMonAlarmInfoGroup.setObjects(
      *(("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonValue"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonLimitValue"))
)
if mibBuilder.loadTexts:
    dmosHwMonAlarmInfoGroup.setStatus("current")


# Notification objects

fanHighAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 3)
)
fanHighAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonValue"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonLimitValue"))
)
if mibBuilder.loadTexts:
    fanHighAlarmTrap.setStatus(
        "current"
    )

fanLowAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 4)
)
fanLowAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonValue"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonLimitValue"))
)
if mibBuilder.loadTexts:
    fanLowAlarmTrap.setStatus(
        "current"
    )

fanFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 5)
)
fanFailAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
)
if mibBuilder.loadTexts:
    fanFailAlarmTrap.setStatus(
        "current"
    )

fanErrorAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 6)
)
fanErrorAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
)
if mibBuilder.loadTexts:
    fanErrorAlarmTrap.setStatus(
        "current"
    )

tempHighAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 7)
)
tempHighAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonValue"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonLimitValue"))
)
if mibBuilder.loadTexts:
    tempHighAlarmTrap.setStatus(
        "current"
    )

tempLowAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 8)
)
tempLowAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonValue"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonLimitValue"))
)
if mibBuilder.loadTexts:
    tempLowAlarmTrap.setStatus(
        "current"
    )

tempErrorAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 9)
)
tempErrorAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
)
if mibBuilder.loadTexts:
    tempErrorAlarmTrap.setStatus(
        "current"
    )

tempCriticalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 10)
)
tempCriticalAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonValue"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "dmosHwMonLimitValue"))
)
if mibBuilder.loadTexts:
    tempCriticalAlarmTrap.setStatus(
        "current"
    )


# Notifications groups

dmosFanAlarmTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 2, 2)
)
dmosFanAlarmTrapsGroup.setObjects(
      *(("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "fanHighAlarmTrap"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "fanLowAlarmTrap"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "fanErrorAlarmTrap"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "fanFailAlarmTrap"))
)
if mibBuilder.loadTexts:
    dmosFanAlarmTrapsGroup.setStatus(
        "current"
    )

dmosTempAlarmTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 2, 2, 3)
)
dmosTempAlarmTrapsGroup.setObjects(
      *(("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "tempHighAlarmTrap"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "tempLowAlarmTrap"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "tempErrorAlarmTrap"),
        ("DMOS-HW-MONITOR-NOTIFICATIONS-MIB", "tempCriticalAlarmTrap"))
)
if mibBuilder.loadTexts:
    dmosTempAlarmTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMOS-HW-MONITOR-NOTIFICATIONS-MIB",
    **{"dmosHwMonNotificationsMIB": dmosHwMonNotificationsMIB,
       "dmosHwMonNotificationObjects": dmosHwMonNotificationObjects,
       "dmosHwMonValue": dmosHwMonValue,
       "dmosHwMonLimitValue": dmosHwMonLimitValue,
       "dmosHwMonNotificationGroups": dmosHwMonNotificationGroups,
       "dmosHwMonAlarmInfoGroup": dmosHwMonAlarmInfoGroup,
       "dmosFanAlarmTrapsGroup": dmosFanAlarmTrapsGroup,
       "dmosTempAlarmTrapsGroup": dmosTempAlarmTrapsGroup,
       "fanHighAlarmTrap": fanHighAlarmTrap,
       "fanLowAlarmTrap": fanLowAlarmTrap,
       "fanFailAlarmTrap": fanFailAlarmTrap,
       "fanErrorAlarmTrap": fanErrorAlarmTrap,
       "tempHighAlarmTrap": tempHighAlarmTrap,
       "tempLowAlarmTrap": tempLowAlarmTrap,
       "tempErrorAlarmTrap": tempErrorAlarmTrap,
       "tempCriticalAlarmTrap": tempCriticalAlarmTrap}
)
