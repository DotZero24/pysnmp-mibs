# SNMP MIB module (NETAPP-STORAGEGRID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netapp/NETAPP-STORAGEGRID-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:07:38 2025
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
 enterprises,
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
    "enterprises",
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

storagegrid = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 789, 28669)
)
if mibBuilder.loadTexts:
    storagegrid.setRevisions(
        ("2020-09-09 15:00",
         "2018-03-21 17:25")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmSeverity(TextualConvention, Integer32):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("notice", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Netapp_ObjectIdentity = ObjectIdentity
netapp = _Netapp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789)
)
_SgNotifications_ObjectIdentity = ObjectIdentity
sgNotifications = _SgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 28669, 0)
)
_SgObjects_ObjectIdentity = ObjectIdentity
sgObjects = _SgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1)
)
_CurrentAlarmTable_Object = MibTable
currentAlarmTable = _CurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 1)
)
if mibBuilder.loadTexts:
    currentAlarmTable.setStatus("deprecated")
_CurrentAlarmEntry_Object = MibTableRow
currentAlarmEntry = _CurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 1, 1)
)
currentAlarmEntry.setIndexNames(
    (0, "NETAPP-STORAGEGRID-MIB", "currentAlarmSourceId"),
    (0, "NETAPP-STORAGEGRID-MIB", "currentAlarmAttrCode"),
    (0, "NETAPP-STORAGEGRID-MIB", "currentAlarmAttrIndex"),
)
if mibBuilder.loadTexts:
    currentAlarmEntry.setStatus("deprecated")


class _CurrentAlarmSourceId_Type(OctetString):
    """Custom type currentAlarmSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CurrentAlarmSourceId_Type.__name__ = "OctetString"
_CurrentAlarmSourceId_Object = MibTableColumn
currentAlarmSourceId = _CurrentAlarmSourceId_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 1, 1, 1),
    _CurrentAlarmSourceId_Type()
)
currentAlarmSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmSourceId.setStatus("deprecated")


class _CurrentAlarmAttrCode_Type(DisplayString):
    """Custom type currentAlarmAttrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CurrentAlarmAttrCode_Type.__name__ = "DisplayString"
_CurrentAlarmAttrCode_Object = MibTableColumn
currentAlarmAttrCode = _CurrentAlarmAttrCode_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 1, 1, 2),
    _CurrentAlarmAttrCode_Type()
)
currentAlarmAttrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmAttrCode.setStatus("deprecated")


class _CurrentAlarmAttrIndex_Type(Integer32):
    """Custom type currentAlarmAttrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CurrentAlarmAttrIndex_Type.__name__ = "Integer32"
_CurrentAlarmAttrIndex_Object = MibTableColumn
currentAlarmAttrIndex = _CurrentAlarmAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 1, 1, 3),
    _CurrentAlarmAttrIndex_Type()
)
currentAlarmAttrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmAttrIndex.setStatus("deprecated")


class _CurrentAlarmNodeName_Type(OctetString):
    """Custom type currentAlarmNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CurrentAlarmNodeName_Type.__name__ = "OctetString"
_CurrentAlarmNodeName_Object = MibTableColumn
currentAlarmNodeName = _CurrentAlarmNodeName_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 1, 1, 4),
    _CurrentAlarmNodeName_Type()
)
currentAlarmNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmNodeName.setStatus("deprecated")
_CurrentAlarmSeverity_Type = AlarmSeverity
_CurrentAlarmSeverity_Object = MibTableColumn
currentAlarmSeverity = _CurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 1, 1, 5),
    _CurrentAlarmSeverity_Type()
)
currentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmSeverity.setStatus("deprecated")
_CurrentAlarmTriggerValue_Type = DisplayString
_CurrentAlarmTriggerValue_Object = MibTableColumn
currentAlarmTriggerValue = _CurrentAlarmTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 1, 1, 6),
    _CurrentAlarmTriggerValue_Type()
)
currentAlarmTriggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmTriggerValue.setStatus("deprecated")
_CurrentAlarmTriggerTime_Type = DateAndTime
_CurrentAlarmTriggerTime_Object = MibTableColumn
currentAlarmTriggerTime = _CurrentAlarmTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 1, 1, 7),
    _CurrentAlarmTriggerTime_Type()
)
currentAlarmTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmTriggerTime.setStatus("deprecated")
_CurrentAlarmCount_Type = Integer32
_CurrentAlarmCount_Object = MibScalar
currentAlarmCount = _CurrentAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 2),
    _CurrentAlarmCount_Type()
)
currentAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmCount.setStatus("deprecated")
_ActiveAlertCount_Type = Integer32
_ActiveAlertCount_Object = MibScalar
activeAlertCount = _ActiveAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 3),
    _ActiveAlertCount_Type()
)
activeAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlertCount.setStatus("current")
_ActiveAlertTable_Object = MibTable
activeAlertTable = _ActiveAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 4)
)
if mibBuilder.loadTexts:
    activeAlertTable.setStatus("current")
_ActiveAlertEntry_Object = MibTableRow
activeAlertEntry = _ActiveAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 4, 1)
)
activeAlertEntry.setIndexNames(
    (0, "NETAPP-STORAGEGRID-MIB", "activeAlertId"),
)
if mibBuilder.loadTexts:
    activeAlertEntry.setStatus("current")


class _ActiveAlertId_Type(OctetString):
    """Custom type activeAlertId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ActiveAlertId_Type.__name__ = "OctetString"
_ActiveAlertId_Object = MibTableColumn
activeAlertId = _ActiveAlertId_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 4, 1, 1),
    _ActiveAlertId_Type()
)
activeAlertId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlertId.setStatus("current")
_ActiveAlertName_Type = OctetString
_ActiveAlertName_Object = MibTableColumn
activeAlertName = _ActiveAlertName_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 4, 1, 2),
    _ActiveAlertName_Type()
)
activeAlertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlertName.setStatus("current")
_ActiveAlertInstance_Type = OctetString
_ActiveAlertInstance_Object = MibTableColumn
activeAlertInstance = _ActiveAlertInstance_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 4, 1, 3),
    _ActiveAlertInstance_Type()
)
activeAlertInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlertInstance.setStatus("current")
_ActiveAlertSeverity_Type = OctetString
_ActiveAlertSeverity_Object = MibTableColumn
activeAlertSeverity = _ActiveAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 4, 1, 4),
    _ActiveAlertSeverity_Type()
)
activeAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlertSeverity.setStatus("current")
_ActiveAlertStartTime_Type = DateAndTime
_ActiveAlertStartTime_Object = MibTableColumn
activeAlertStartTime = _ActiveAlertStartTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 28669, 1, 4, 1, 5),
    _ActiveAlertStartTime_Type()
)
activeAlertStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlertStartTime.setStatus("current")
_SgGroups_ObjectIdentity = ObjectIdentity
sgGroups = _SgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 28669, 2)
)

# Managed Objects groups

currentAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 789, 28669, 2, 1)
)
currentAlarmGroup.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "currentAlarmSourceId"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrCode"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrIndex"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmNodeName"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerTime"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerValue"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmCount"))
)
if mibBuilder.loadTexts:
    currentAlarmGroup.setStatus("deprecated")

activeAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 789, 28669, 2, 3)
)
activeAlertGroup.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "activeAlertCount"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertId"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertName"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertInstance"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertStartTime"))
)
if mibBuilder.loadTexts:
    activeAlertGroup.setStatus("current")


# Notification objects

currentNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 28669, 0, 1)
)
currentNormalAlarm.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "currentAlarmSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmSourceId"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrCode"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerTime"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerValue"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrIndex"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmNodeName"))
)
if mibBuilder.loadTexts:
    currentNormalAlarm.setStatus(
        "deprecated"
    )

currentNoticeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 28669, 0, 2)
)
currentNoticeAlarm.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "currentAlarmSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmSourceId"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrCode"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerTime"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerValue"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrIndex"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmNodeName"))
)
if mibBuilder.loadTexts:
    currentNoticeAlarm.setStatus(
        "deprecated"
    )

currentMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 28669, 0, 3)
)
currentMinorAlarm.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "currentAlarmSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmSourceId"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrCode"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerTime"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerValue"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrIndex"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmNodeName"))
)
if mibBuilder.loadTexts:
    currentMinorAlarm.setStatus(
        "deprecated"
    )

currentMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 28669, 0, 4)
)
currentMajorAlarm.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "currentAlarmSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmSourceId"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrCode"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerTime"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerValue"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrIndex"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmNodeName"))
)
if mibBuilder.loadTexts:
    currentMajorAlarm.setStatus(
        "deprecated"
    )

currentCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 28669, 0, 5)
)
currentCriticalAlarm.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "currentAlarmSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmSourceId"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrCode"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerTime"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmTriggerValue"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmAttrIndex"),
        ("NETAPP-STORAGEGRID-MIB", "currentAlarmNodeName"))
)
if mibBuilder.loadTexts:
    currentCriticalAlarm.setStatus(
        "deprecated"
    )

activeMinorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 28669, 0, 6)
)
activeMinorAlert.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "activeAlertStartTime"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertInstance"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertId"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertName"))
)
if mibBuilder.loadTexts:
    activeMinorAlert.setStatus(
        "current"
    )

activeMajorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 28669, 0, 7)
)
activeMajorAlert.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "activeAlertStartTime"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertInstance"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertId"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertName"))
)
if mibBuilder.loadTexts:
    activeMajorAlert.setStatus(
        "current"
    )

activeCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 28669, 0, 8)
)
activeCriticalAlert.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "activeAlertStartTime"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertInstance"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertId"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertSeverity"),
        ("NETAPP-STORAGEGRID-MIB", "activeAlertName"))
)
if mibBuilder.loadTexts:
    activeCriticalAlert.setStatus(
        "current"
    )


# Notifications groups

currentAlarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 789, 28669, 2, 2)
)
currentAlarmNotificationsGroup.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "currentNormalAlarm"),
        ("NETAPP-STORAGEGRID-MIB", "currentNoticeAlarm"),
        ("NETAPP-STORAGEGRID-MIB", "currentMinorAlarm"),
        ("NETAPP-STORAGEGRID-MIB", "currentMajorAlarm"),
        ("NETAPP-STORAGEGRID-MIB", "currentCriticalAlarm"))
)
if mibBuilder.loadTexts:
    currentAlarmNotificationsGroup.setStatus(
        "deprecated"
    )

activeAlertNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 789, 28669, 2, 4)
)
activeAlertNotificationsGroup.setObjects(
      *(("NETAPP-STORAGEGRID-MIB", "activeMinorAlert"),
        ("NETAPP-STORAGEGRID-MIB", "activeMajorAlert"),
        ("NETAPP-STORAGEGRID-MIB", "activeCriticalAlert"))
)
if mibBuilder.loadTexts:
    activeAlertNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETAPP-STORAGEGRID-MIB",
    **{"AlarmSeverity": AlarmSeverity,
       "netapp": netapp,
       "storagegrid": storagegrid,
       "sgNotifications": sgNotifications,
       "currentNormalAlarm": currentNormalAlarm,
       "currentNoticeAlarm": currentNoticeAlarm,
       "currentMinorAlarm": currentMinorAlarm,
       "currentMajorAlarm": currentMajorAlarm,
       "currentCriticalAlarm": currentCriticalAlarm,
       "activeMinorAlert": activeMinorAlert,
       "activeMajorAlert": activeMajorAlert,
       "activeCriticalAlert": activeCriticalAlert,
       "sgObjects": sgObjects,
       "currentAlarmTable": currentAlarmTable,
       "currentAlarmEntry": currentAlarmEntry,
       "currentAlarmSourceId": currentAlarmSourceId,
       "currentAlarmAttrCode": currentAlarmAttrCode,
       "currentAlarmAttrIndex": currentAlarmAttrIndex,
       "currentAlarmNodeName": currentAlarmNodeName,
       "currentAlarmSeverity": currentAlarmSeverity,
       "currentAlarmTriggerValue": currentAlarmTriggerValue,
       "currentAlarmTriggerTime": currentAlarmTriggerTime,
       "currentAlarmCount": currentAlarmCount,
       "activeAlertCount": activeAlertCount,
       "activeAlertTable": activeAlertTable,
       "activeAlertEntry": activeAlertEntry,
       "activeAlertId": activeAlertId,
       "activeAlertName": activeAlertName,
       "activeAlertInstance": activeAlertInstance,
       "activeAlertSeverity": activeAlertSeverity,
       "activeAlertStartTime": activeAlertStartTime,
       "sgGroups": sgGroups,
       "currentAlarmGroup": currentAlarmGroup,
       "currentAlarmNotificationsGroup": currentAlarmNotificationsGroup,
       "activeAlertGroup": activeAlertGroup,
       "activeAlertNotificationsGroup": activeAlertNotificationsGroup}
)
