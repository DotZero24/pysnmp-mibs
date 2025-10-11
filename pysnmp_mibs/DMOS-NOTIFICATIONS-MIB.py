# SNMP MIB module (DMOS-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DMOS-NOTIFICATIONS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:55 2025
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

(datacomDevicesMIBs,) = mibBuilder.importSymbols(
    "DATACOM-SMI",
    "datacomDevicesMIBs")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dmosNotificationsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3)
)
if mibBuilder.loadTexts:
    dmosNotificationsMIB.setRevisions(
        ("2016-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NotificationObjects_ObjectIdentity = ObjectIdentity
notificationObjects = _NotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1)
)
_NotificationTime_Type = DateAndTime
_NotificationTime_Object = MibScalar
notificationTime = _NotificationTime_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 1),
    _NotificationTime_Type()
)
notificationTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationTime.setStatus("current")
_NotificationName_Type = DisplayString
_NotificationName_Object = MibScalar
notificationName = _NotificationName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 2),
    _NotificationName_Type()
)
notificationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationName.setStatus("current")
_NotificationSourceType_Type = DisplayString
_NotificationSourceType_Object = MibScalar
notificationSourceType = _NotificationSourceType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 3),
    _NotificationSourceType_Type()
)
notificationSourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationSourceType.setStatus("current")
_NotificationSourceValue_Type = DisplayString
_NotificationSourceValue_Object = MibScalar
notificationSourceValue = _NotificationSourceValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 4),
    _NotificationSourceValue_Type()
)
notificationSourceValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationSourceValue.setStatus("current")
_NotificationSeverity_Type = DisplayString
_NotificationSeverity_Object = MibScalar
notificationSeverity = _NotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 5),
    _NotificationSeverity_Type()
)
notificationSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationSeverity.setStatus("current")
_NotificationInfo_Type = DisplayString
_NotificationInfo_Object = MibScalar
notificationInfo = _NotificationInfo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 6),
    _NotificationInfo_Type()
)
notificationInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationInfo.setStatus("current")


class _NotificationAlarmState_Type(Integer32):
    """Custom type notificationAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 2),
          ("unstable", 3))
    )


_NotificationAlarmState_Type.__name__ = "Integer32"
_NotificationAlarmState_Object = MibScalar
notificationAlarmState = _NotificationAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 7),
    _NotificationAlarmState_Type()
)
notificationAlarmState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationAlarmState.setStatus("current")
_NotificationGroups_ObjectIdentity = ObjectIdentity
notificationGroups = _NotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 2)
)
_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3)
)

# Managed Objects groups

infoNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 2, 1)
)
infoNotificationGroup.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"))
)
if mibBuilder.loadTexts:
    infoNotificationGroup.setStatus("current")

alarmNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 2, 2)
)
alarmNotificationGroup.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
)
if mibBuilder.loadTexts:
    alarmNotificationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMOS-NOTIFICATIONS-MIB",
    **{"dmosNotificationsMIB": dmosNotificationsMIB,
       "notificationObjects": notificationObjects,
       "notificationTime": notificationTime,
       "notificationName": notificationName,
       "notificationSourceType": notificationSourceType,
       "notificationSourceValue": notificationSourceValue,
       "notificationSeverity": notificationSeverity,
       "notificationInfo": notificationInfo,
       "notificationAlarmState": notificationAlarmState,
       "notificationGroups": notificationGroups,
       "infoNotificationGroup": infoNotificationGroup,
       "alarmNotificationGroup": alarmNotificationGroup,
       "alarmNotifications": alarmNotifications}
)
