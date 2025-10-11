# SNMP MIB module (DMOS-CPU-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DMOS-CPU-NOTIFICATIONS-MIB
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

dmosCpuNotificationsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0)
)
if mibBuilder.loadTexts:
    dmosCpuNotificationsMIB.setRevisions(
        ("2016-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DmosCpuNotificationObjects_ObjectIdentity = ObjectIdentity
dmosCpuNotificationObjects = _DmosCpuNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1)
)
_DmosCpuNotificationThreshold_Type = UnsignedPercent
_DmosCpuNotificationThreshold_Object = MibScalar
dmosCpuNotificationThreshold = _DmosCpuNotificationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1, 1),
    _DmosCpuNotificationThreshold_Type()
)
dmosCpuNotificationThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmosCpuNotificationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dmosCpuNotificationThreshold.setUnits("%")
_DmosCpuNotificationInterval_Type = Gauge32
_DmosCpuNotificationInterval_Object = MibScalar
dmosCpuNotificationInterval = _DmosCpuNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1, 2),
    _DmosCpuNotificationInterval_Type()
)
dmosCpuNotificationInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmosCpuNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    dmosCpuNotificationInterval.setUnits("seconds")
_DmosCpuNotificationValue_Type = UnsignedPercent
_DmosCpuNotificationValue_Object = MibScalar
dmosCpuNotificationValue = _DmosCpuNotificationValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1, 3),
    _DmosCpuNotificationValue_Type()
)
dmosCpuNotificationValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmosCpuNotificationValue.setStatus("current")
if mibBuilder.loadTexts:
    dmosCpuNotificationValue.setUnits("%")
_DmosCpuNotificationCoreId_Type = Gauge32
_DmosCpuNotificationCoreId_Object = MibScalar
dmosCpuNotificationCoreId = _DmosCpuNotificationCoreId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1, 4),
    _DmosCpuNotificationCoreId_Type()
)
dmosCpuNotificationCoreId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmosCpuNotificationCoreId.setStatus("current")
if mibBuilder.loadTexts:
    dmosCpuNotificationCoreId.setUnits("ID")
_DmosCpuNotificationGroups_ObjectIdentity = ObjectIdentity
dmosCpuNotificationGroups = _DmosCpuNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 2)
)

# Managed Objects groups

dmosCpuAlarmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 2, 1)
)
dmosCpuAlarmInfoGroup.setObjects(
      *(("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationThreshold"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationInterval"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationCoreId"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationValue"))
)
if mibBuilder.loadTexts:
    dmosCpuAlarmInfoGroup.setStatus("current")


# Notification objects

cpuLoadHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 3)
)
cpuLoadHighTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationThreshold"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationInterval"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationValue"))
)
if mibBuilder.loadTexts:
    cpuLoadHighTrap.setStatus(
        "current"
    )

cpuCoreHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 4)
)
cpuCoreHighTrap.setObjects(
      *(("DMOS-NOTIFICATIONS-MIB", "notificationTime"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationName"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"),
        ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationThreshold"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationInterval"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationCoreId"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationValue"))
)
if mibBuilder.loadTexts:
    cpuCoreHighTrap.setStatus(
        "current"
    )


# Notifications groups

dmosCpuAlarmTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 2, 2)
)
dmosCpuAlarmTrapsGroup.setObjects(
      *(("DMOS-CPU-NOTIFICATIONS-MIB", "cpuLoadHighTrap"),
        ("DMOS-CPU-NOTIFICATIONS-MIB", "cpuCoreHighTrap"))
)
if mibBuilder.loadTexts:
    dmosCpuAlarmTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMOS-CPU-NOTIFICATIONS-MIB",
    **{"dmosCpuNotificationsMIB": dmosCpuNotificationsMIB,
       "dmosCpuNotificationObjects": dmosCpuNotificationObjects,
       "dmosCpuNotificationThreshold": dmosCpuNotificationThreshold,
       "dmosCpuNotificationInterval": dmosCpuNotificationInterval,
       "dmosCpuNotificationValue": dmosCpuNotificationValue,
       "dmosCpuNotificationCoreId": dmosCpuNotificationCoreId,
       "dmosCpuNotificationGroups": dmosCpuNotificationGroups,
       "dmosCpuAlarmInfoGroup": dmosCpuAlarmInfoGroup,
       "dmosCpuAlarmTrapsGroup": dmosCpuAlarmTrapsGroup,
       "cpuLoadHighTrap": cpuLoadHighTrap,
       "cpuCoreHighTrap": cpuCoreHighTrap}
)
