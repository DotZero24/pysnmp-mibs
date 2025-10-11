# SNMP MIB module (DMOS-MEM-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DMOS-MEM-NOTIFICATIONS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:47 2025
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

(UnsignedPercent,) = mibBuilder.importSymbols(
    "DMOS-TC-MIB",
    "UnsignedPercent")

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

dmosMemNotificationsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dmosMemNotificationsMIB.setRevisions(
        ("2016-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DmosMemNotificationObjects_ObjectIdentity = ObjectIdentity
dmosMemNotificationObjects = _DmosMemNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 1)
)
_DmosMemNotificationThreshold_Type = Gauge32
_DmosMemNotificationThreshold_Object = MibScalar
dmosMemNotificationThreshold = _DmosMemNotificationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 1, 1),
    _DmosMemNotificationThreshold_Type()
)
dmosMemNotificationThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmosMemNotificationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dmosMemNotificationThreshold.setUnits("Bytes")
_DmosMemNotificationInterval_Type = Gauge32
_DmosMemNotificationInterval_Object = MibScalar
dmosMemNotificationInterval = _DmosMemNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 1, 2),
    _DmosMemNotificationInterval_Type()
)
dmosMemNotificationInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmosMemNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    dmosMemNotificationInterval.setUnits("seconds")
_DmosMemNotificationGroups_ObjectIdentity = ObjectIdentity
dmosMemNotificationGroups = _DmosMemNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 2)
)

# Managed Objects groups

dmosMemAlarmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 2, 1)
)
dmosMemAlarmInfoGroup.setObjects(
      *(("DMOS-MEM-NOTIFICATIONS-MIB", "dmosMemNotificationThreshold"),
        ("DMOS-MEM-NOTIFICATIONS-MIB", "dmosMemNotificationInterval"))
)
if mibBuilder.loadTexts:
    dmosMemAlarmInfoGroup.setStatus("current")


# Notification objects

memAvailableLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 3)
)
memAvailableLowTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"),
        ("DMOS-MEM-NOTIFICATIONS-MIB", "dmosMemNotificationThreshold"),
        ("DMOS-MEM-NOTIFICATIONS-MIB", "dmosMemNotificationInterval"))
)
if mibBuilder.loadTexts:
    memAvailableLowTrap.setStatus(
        "current"
    )


# Notifications groups

dmosMemAlarmTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 2, 2)
)
dmosMemAlarmTrapsGroup.setObjects(
    ("DMOS-MEM-NOTIFICATIONS-MIB", "memAvailableLowTrap")
)
if mibBuilder.loadTexts:
    dmosMemAlarmTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMOS-MEM-NOTIFICATIONS-MIB",
    **{"dmosMemNotificationsMIB": dmosMemNotificationsMIB,
       "dmosMemNotificationObjects": dmosMemNotificationObjects,
       "dmosMemNotificationThreshold": dmosMemNotificationThreshold,
       "dmosMemNotificationInterval": dmosMemNotificationInterval,
       "dmosMemNotificationGroups": dmosMemNotificationGroups,
       "dmosMemAlarmInfoGroup": dmosMemAlarmInfoGroup,
       "dmosMemAlarmTrapsGroup": dmosMemAlarmTrapsGroup,
       "memAvailableLowTrap": memAvailableLowTrap}
)
