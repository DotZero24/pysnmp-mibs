# SNMP MIB module (DMOS-CARDMGR-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DMOS-CARDMGR-NOTIFICATIONS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:54 2025
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

dmosCardmgrNotificationsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3)
)
if mibBuilder.loadTexts:
    dmosCardmgrNotificationsMIB.setRevisions(
        ("2017-11-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DmosCardmgrNotificationGroups_ObjectIdentity = ObjectIdentity
dmosCardmgrNotificationGroups = _DmosCardmgrNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 1)
)

# Managed Objects groups


# Notification objects

cardNotProvisionedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 2)
)
cardNotProvisionedAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
)
if mibBuilder.loadTexts:
    cardNotProvisionedAlarmTrap.setStatus(
        "current"
    )

cardNotPresentAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 3)
)
cardNotPresentAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
)
if mibBuilder.loadTexts:
    cardNotPresentAlarmTrap.setStatus(
        "current"
    )

cardRemovedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 4)
)
cardRemovedAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
)
if mibBuilder.loadTexts:
    cardRemovedAlarmTrap.setStatus(
        "current"
    )

cardMismatchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 5)
)
cardMismatchAlarmTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
)
if mibBuilder.loadTexts:
    cardMismatchAlarmTrap.setStatus(
        "current"
    )

cardInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 6)
)
cardInsertedTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"))
)
if mibBuilder.loadTexts:
    cardInsertedTrap.setStatus(
        "current"
    )

cardRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 7)
)
cardRemovedTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"))
)
if mibBuilder.loadTexts:
    cardRemovedTrap.setStatus(
        "current"
    )


# Notifications groups

dmosCardmgrAlarmTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 1, 1)
)
dmosCardmgrAlarmTrapsGroup.setObjects(
      *(("DMOS-CARDMGR-NOTIFICATIONS-MIB", "cardNotProvisionedAlarmTrap"),
        ("DMOS-CARDMGR-NOTIFICATIONS-MIB", "cardNotPresentAlarmTrap"),
        ("DMOS-CARDMGR-NOTIFICATIONS-MIB", "cardRemovedAlarmTrap"),
        ("DMOS-CARDMGR-NOTIFICATIONS-MIB", "cardMismatchAlarmTrap"))
)
if mibBuilder.loadTexts:
    dmosCardmgrAlarmTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMOS-CARDMGR-NOTIFICATIONS-MIB",
    **{"dmosCardmgrNotificationsMIB": dmosCardmgrNotificationsMIB,
       "dmosCardmgrNotificationGroups": dmosCardmgrNotificationGroups,
       "dmosCardmgrAlarmTrapsGroup": dmosCardmgrAlarmTrapsGroup,
       "cardNotProvisionedAlarmTrap": cardNotProvisionedAlarmTrap,
       "cardNotPresentAlarmTrap": cardNotPresentAlarmTrap,
       "cardRemovedAlarmTrap": cardRemovedAlarmTrap,
       "cardMismatchAlarmTrap": cardMismatchAlarmTrap,
       "cardInsertedTrap": cardInsertedTrap,
       "cardRemovedTrap": cardRemovedTrap}
)
