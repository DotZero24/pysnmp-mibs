# SNMP MIB module (ELTEX-ENTITY-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-ENTITY-SENSOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:03 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(EltexThresholdRelation,) = mibBuilder.importSymbols(
    "ELTEX-TC",
    "EltexThresholdRelation")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(EntitySensorValue,
 entPhySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue",
    "entPhySensorValue")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(SyslogSeverity,) = mibBuilder.importSymbols(
    "SYSLOG-TC-MIB",
    "SyslogSeverity")


# MODULE-IDENTITY

eltexEntitySensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 40)
)
if mibBuilder.loadTexts:
    eltexEntitySensorMIB.setRevisions(
        ("2017-05-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltexEntitySensorMIBObjects_ObjectIdentity = ObjectIdentity
eltexEntitySensorMIBObjects = _EltexEntitySensorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1)
)
_EltexEntitySensorCommon_ObjectIdentity = ObjectIdentity
eltexEntitySensorCommon = _EltexEntitySensorCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 1)
)
_EltexEntitySensorTable_Object = MibTable
eltexEntitySensorTable = _EltexEntitySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltexEntitySensorTable.setStatus("current")
_EltexEntitySensorEntry_Object = MibTableRow
eltexEntitySensorEntry = _EltexEntitySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 1, 2, 1)
)
eltexEntitySensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    eltexEntitySensorEntry.setStatus("current")
_EltexEntitySensorThresholdFreeIndex_Type = Unsigned32
_EltexEntitySensorThresholdFreeIndex_Object = MibTableColumn
eltexEntitySensorThresholdFreeIndex = _EltexEntitySensorThresholdFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 1, 2, 1, 1),
    _EltexEntitySensorThresholdFreeIndex_Type()
)
eltexEntitySensorThresholdFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdFreeIndex.setStatus("current")
_EltexEntitySensorThresholds_ObjectIdentity = ObjectIdentity
eltexEntitySensorThresholds = _EltexEntitySensorThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2)
)


class _EltexEntitySensorThresholdNotificationGlobalEnable_Type(TruthValue):
    """Custom type eltexEntitySensorThresholdNotificationGlobalEnable based on TruthValue"""
    defaultValue = 2


_EltexEntitySensorThresholdNotificationGlobalEnable_Type.__name__ = "TruthValue"
_EltexEntitySensorThresholdNotificationGlobalEnable_Object = MibScalar
eltexEntitySensorThresholdNotificationGlobalEnable = _EltexEntitySensorThresholdNotificationGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 1),
    _EltexEntitySensorThresholdNotificationGlobalEnable_Type()
)
eltexEntitySensorThresholdNotificationGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdNotificationGlobalEnable.setStatus("current")


class _EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Type(TruthValue):
    """Custom type eltexEntitySensorThresholdRecoveryNotificationGlobalEnable based on TruthValue"""
    defaultValue = 2


_EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Type.__name__ = "TruthValue"
_EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Object = MibScalar
eltexEntitySensorThresholdRecoveryNotificationGlobalEnable = _EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 2),
    _EltexEntitySensorThresholdRecoveryNotificationGlobalEnable_Type()
)
eltexEntitySensorThresholdRecoveryNotificationGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdRecoveryNotificationGlobalEnable.setStatus("current")
_EltexEntitySensorThresholdTable_Object = MibTable
eltexEntitySensorThresholdTable = _EltexEntitySensorThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdTable.setStatus("current")
_EltexEntitySensorThresholdEntry_Object = MibTableRow
eltexEntitySensorThresholdEntry = _EltexEntitySensorThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1)
)
eltexEntitySensorThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ELTEX-ENTITY-SENSOR-MIB", "eltexEntitySensorThresholdIndex"),
)
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdEntry.setStatus("current")
_EltexEntitySensorThresholdIndex_Type = Unsigned32
_EltexEntitySensorThresholdIndex_Object = MibTableColumn
eltexEntitySensorThresholdIndex = _EltexEntitySensorThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1, 1),
    _EltexEntitySensorThresholdIndex_Type()
)
eltexEntitySensorThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdIndex.setStatus("current")
_EltexEntitySensorThresholdRowStatus_Type = RowStatus
_EltexEntitySensorThresholdRowStatus_Object = MibTableColumn
eltexEntitySensorThresholdRowStatus = _EltexEntitySensorThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1, 2),
    _EltexEntitySensorThresholdRowStatus_Type()
)
eltexEntitySensorThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdRowStatus.setStatus("current")
_EltexEntitySensorThresholdValue_Type = EntitySensorValue
_EltexEntitySensorThresholdValue_Object = MibTableColumn
eltexEntitySensorThresholdValue = _EltexEntitySensorThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1, 3),
    _EltexEntitySensorThresholdValue_Type()
)
eltexEntitySensorThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdValue.setStatus("current")


class _EltexEntitySensorThresholdFlappingInterval_Type(EntitySensorValue):
    """Custom type eltexEntitySensorThresholdFlappingInterval based on EntitySensorValue"""
    defaultValue = 0


_EltexEntitySensorThresholdFlappingInterval_Type.__name__ = "EntitySensorValue"
_EltexEntitySensorThresholdFlappingInterval_Object = MibTableColumn
eltexEntitySensorThresholdFlappingInterval = _EltexEntitySensorThresholdFlappingInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1, 4),
    _EltexEntitySensorThresholdFlappingInterval_Type()
)
eltexEntitySensorThresholdFlappingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdFlappingInterval.setStatus("current")


class _EltexEntitySensorThresholdSeverity_Type(SyslogSeverity):
    """Custom type eltexEntitySensorThresholdSeverity based on SyslogSeverity"""
    defaultValue = 1


_EltexEntitySensorThresholdSeverity_Type.__name__ = "SyslogSeverity"
_EltexEntitySensorThresholdSeverity_Object = MibTableColumn
eltexEntitySensorThresholdSeverity = _EltexEntitySensorThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1, 5),
    _EltexEntitySensorThresholdSeverity_Type()
)
eltexEntitySensorThresholdSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdSeverity.setStatus("current")
_EltexEntitySensorThresholdRelation_Type = EltexThresholdRelation
_EltexEntitySensorThresholdRelation_Object = MibTableColumn
eltexEntitySensorThresholdRelation = _EltexEntitySensorThresholdRelation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1, 6),
    _EltexEntitySensorThresholdRelation_Type()
)
eltexEntitySensorThresholdRelation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdRelation.setStatus("current")


class _EltexEntitySensorThresholdNotificationEnable_Type(TruthValue):
    """Custom type eltexEntitySensorThresholdNotificationEnable based on TruthValue"""
    defaultValue = 1


_EltexEntitySensorThresholdNotificationEnable_Type.__name__ = "TruthValue"
_EltexEntitySensorThresholdNotificationEnable_Object = MibTableColumn
eltexEntitySensorThresholdNotificationEnable = _EltexEntitySensorThresholdNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1, 7),
    _EltexEntitySensorThresholdNotificationEnable_Type()
)
eltexEntitySensorThresholdNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdNotificationEnable.setStatus("current")


class _EltexEntitySensorThresholdRecoveryNotificationEnable_Type(TruthValue):
    """Custom type eltexEntitySensorThresholdRecoveryNotificationEnable based on TruthValue"""
    defaultValue = 1


_EltexEntitySensorThresholdRecoveryNotificationEnable_Type.__name__ = "TruthValue"
_EltexEntitySensorThresholdRecoveryNotificationEnable_Object = MibTableColumn
eltexEntitySensorThresholdRecoveryNotificationEnable = _EltexEntitySensorThresholdRecoveryNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1, 8),
    _EltexEntitySensorThresholdRecoveryNotificationEnable_Type()
)
eltexEntitySensorThresholdRecoveryNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdRecoveryNotificationEnable.setStatus("current")
_EltexEntitySensorThresholdEvaluation_Type = TruthValue
_EltexEntitySensorThresholdEvaluation_Object = MibTableColumn
eltexEntitySensorThresholdEvaluation = _EltexEntitySensorThresholdEvaluation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 40, 1, 2, 3, 1, 9),
    _EltexEntitySensorThresholdEvaluation_Type()
)
eltexEntitySensorThresholdEvaluation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdEvaluation.setStatus("current")
_EltexEntitySensorMIBNotifications_ObjectIdentity = ObjectIdentity
eltexEntitySensorMIBNotifications = _EltexEntitySensorMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 40, 2)
)
_EltexEntitySensorMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltexEntitySensorMIBNotificationsPrefix = _EltexEntitySensorMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 40, 2, 0)
)

# Managed Objects groups


# Notification objects

eltexEntitySensorThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 40, 2, 0, 1)
)
eltexEntitySensorThresholdNotification.setObjects(
      *(("ELTEX-ENTITY-SENSOR-MIB", "eltexEntitySensorThresholdSeverity"),
        ("ELTEX-ENTITY-SENSOR-MIB", "eltexEntitySensorThresholdRelation"),
        ("ELTEX-ENTITY-SENSOR-MIB", "eltexEntitySensorThresholdValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"))
)
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdNotification.setStatus(
        "current"
    )

eltexEntitySensorThresholdRecoveryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 40, 2, 0, 2)
)
eltexEntitySensorThresholdRecoveryNotification.setObjects(
      *(("ELTEX-ENTITY-SENSOR-MIB", "eltexEntitySensorThresholdSeverity"),
        ("ELTEX-ENTITY-SENSOR-MIB", "eltexEntitySensorThresholdRelation"),
        ("ELTEX-ENTITY-SENSOR-MIB", "eltexEntitySensorThresholdValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"))
)
if mibBuilder.loadTexts:
    eltexEntitySensorThresholdRecoveryNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-ENTITY-SENSOR-MIB",
    **{"eltexEntitySensorMIB": eltexEntitySensorMIB,
       "eltexEntitySensorMIBObjects": eltexEntitySensorMIBObjects,
       "eltexEntitySensorCommon": eltexEntitySensorCommon,
       "eltexEntitySensorTable": eltexEntitySensorTable,
       "eltexEntitySensorEntry": eltexEntitySensorEntry,
       "eltexEntitySensorThresholdFreeIndex": eltexEntitySensorThresholdFreeIndex,
       "eltexEntitySensorThresholds": eltexEntitySensorThresholds,
       "eltexEntitySensorThresholdNotificationGlobalEnable": eltexEntitySensorThresholdNotificationGlobalEnable,
       "eltexEntitySensorThresholdRecoveryNotificationGlobalEnable": eltexEntitySensorThresholdRecoveryNotificationGlobalEnable,
       "eltexEntitySensorThresholdTable": eltexEntitySensorThresholdTable,
       "eltexEntitySensorThresholdEntry": eltexEntitySensorThresholdEntry,
       "eltexEntitySensorThresholdIndex": eltexEntitySensorThresholdIndex,
       "eltexEntitySensorThresholdRowStatus": eltexEntitySensorThresholdRowStatus,
       "eltexEntitySensorThresholdValue": eltexEntitySensorThresholdValue,
       "eltexEntitySensorThresholdFlappingInterval": eltexEntitySensorThresholdFlappingInterval,
       "eltexEntitySensorThresholdSeverity": eltexEntitySensorThresholdSeverity,
       "eltexEntitySensorThresholdRelation": eltexEntitySensorThresholdRelation,
       "eltexEntitySensorThresholdNotificationEnable": eltexEntitySensorThresholdNotificationEnable,
       "eltexEntitySensorThresholdRecoveryNotificationEnable": eltexEntitySensorThresholdRecoveryNotificationEnable,
       "eltexEntitySensorThresholdEvaluation": eltexEntitySensorThresholdEvaluation,
       "eltexEntitySensorMIBNotifications": eltexEntitySensorMIBNotifications,
       "eltexEntitySensorMIBNotificationsPrefix": eltexEntitySensorMIBNotificationsPrefix,
       "eltexEntitySensorThresholdNotification": eltexEntitySensorThresholdNotification,
       "eltexEntitySensorThresholdRecoveryNotification": eltexEntitySensorThresholdRecoveryNotification}
)
