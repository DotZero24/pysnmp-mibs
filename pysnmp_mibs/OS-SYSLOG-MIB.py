# SNMP MIB module (OS-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:56 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

osSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32)
)
if mibBuilder.loadTexts:
    osSyslog.setRevisions(
        ("2014-07-06 13:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogSeverity(TextualConvention, Integer32):
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaOptiSwitch_ObjectIdentity = ObjectIdentity
oaOptiSwitch = _OaOptiSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2)
)
_OsSyslogNotifications_ObjectIdentity = ObjectIdentity
osSyslogNotifications = _OsSyslogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 0)
)
_OsSyslogObjects_ObjectIdentity = ObjectIdentity
osSyslogObjects = _OsSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1)
)
_OsLogGen_ObjectIdentity = ObjectIdentity
osLogGen = _OsLogGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 1)
)


class _OsLogHistTableMaxLength_Type(Integer32):
    """Custom type osLogHistTableMaxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_OsLogHistTableMaxLength_Type.__name__ = "Integer32"
_OsLogHistTableMaxLength_Object = MibScalar
osLogHistTableMaxLength = _OsLogHistTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 1, 1),
    _OsLogHistTableMaxLength_Type()
)
osLogHistTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osLogHistTableMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    osLogHistTableMaxLength.setUnits("entries")


class _OsLogNotificationsEnabled_Type(TruthValue):
    """Custom type osLogNotificationsEnabled based on TruthValue"""
    defaultValue = 2


_OsLogNotificationsEnabled_Type.__name__ = "TruthValue"
_OsLogNotificationsEnabled_Object = MibScalar
osLogNotificationsEnabled = _OsLogNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 1, 2),
    _OsLogNotificationsEnabled_Type()
)
osLogNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osLogNotificationsEnabled.setStatus("current")


class _OsLogMaxSeverity_Type(SyslogSeverity):
    """Custom type osLogMaxSeverity based on SyslogSeverity"""
    defaultValue = 7


_OsLogMaxSeverity_Type.__name__ = "SyslogSeverity"
_OsLogMaxSeverity_Object = MibScalar
osLogMaxSeverity = _OsLogMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 1, 3),
    _OsLogMaxSeverity_Type()
)
osLogMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osLogMaxSeverity.setStatus("current")


class _OsLogDataClear_Type(TruthValue):
    """Custom type osLogDataClear based on TruthValue"""
    defaultValue = 2


_OsLogDataClear_Type.__name__ = "TruthValue"
_OsLogDataClear_Object = MibScalar
osLogDataClear = _OsLogDataClear_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 1, 4),
    _OsLogDataClear_Type()
)
osLogDataClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osLogDataClear.setStatus("current")
_OsLogNotificationsSent_Type = Counter32
_OsLogNotificationsSent_Object = MibScalar
osLogNotificationsSent = _OsLogNotificationsSent_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 1, 7),
    _OsLogNotificationsSent_Type()
)
osLogNotificationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLogNotificationsSent.setStatus("current")
if mibBuilder.loadTexts:
    osLogNotificationsSent.setUnits("notifications")
_OsLogMsgIgnored_Type = Counter32
_OsLogMsgIgnored_Object = MibScalar
osLogMsgIgnored = _OsLogMsgIgnored_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 1, 8),
    _OsLogMsgIgnored_Type()
)
osLogMsgIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLogMsgIgnored.setStatus("current")
if mibBuilder.loadTexts:
    osLogMsgIgnored.setUnits("messages")
_OsLogTables_ObjectIdentity = ObjectIdentity
osLogTables = _OsLogTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2)
)
_OsLogHistoryTable_Object = MibTable
osLogHistoryTable = _OsLogHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 3)
)
if mibBuilder.loadTexts:
    osLogHistoryTable.setStatus("current")
_OsLogHistoryEntry_Object = MibTableRow
osLogHistoryEntry = _OsLogHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 3, 1)
)
osLogHistoryEntry.setIndexNames(
    (0, "OS-SYSLOG-MIB", "osLogHistIndex"),
)
if mibBuilder.loadTexts:
    osLogHistoryEntry.setStatus("current")


class _OsLogHistIndex_Type(Integer32):
    """Custom type osLogHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsLogHistIndex_Type.__name__ = "Integer32"
_OsLogHistIndex_Object = MibTableColumn
osLogHistIndex = _OsLogHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 3, 1, 1),
    _OsLogHistIndex_Type()
)
osLogHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osLogHistIndex.setStatus("current")


class _OsLogHistFacility_Type(DisplayString):
    """Custom type osLogHistFacility based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_OsLogHistFacility_Type.__name__ = "DisplayString"
_OsLogHistFacility_Object = MibTableColumn
osLogHistFacility = _OsLogHistFacility_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 3, 1, 2),
    _OsLogHistFacility_Type()
)
osLogHistFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLogHistFacility.setStatus("current")
_OsLogHistSeverity_Type = SyslogSeverity
_OsLogHistSeverity_Object = MibTableColumn
osLogHistSeverity = _OsLogHistSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 3, 1, 3),
    _OsLogHistSeverity_Type()
)
osLogHistSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLogHistSeverity.setStatus("current")


class _OsLogHistMessage_Type(DisplayString):
    """Custom type osLogHistMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OsLogHistMessage_Type.__name__ = "DisplayString"
_OsLogHistMessage_Object = MibTableColumn
osLogHistMessage = _OsLogHistMessage_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 3, 1, 5),
    _OsLogHistMessage_Type()
)
osLogHistMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLogHistMessage.setStatus("current")
_OsLogHistUpTime_Type = TimeStamp
_OsLogHistUpTime_Object = MibTableColumn
osLogHistUpTime = _OsLogHistUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 3, 1, 6),
    _OsLogHistUpTime_Type()
)
osLogHistUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLogHistUpTime.setStatus("current")
_OsLogLastSevTable_Object = MibTable
osLogLastSevTable = _OsLogLastSevTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 5)
)
if mibBuilder.loadTexts:
    osLogLastSevTable.setStatus("current")
_OsLogLastSevEntry_Object = MibTableRow
osLogLastSevEntry = _OsLogLastSevEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 5, 1)
)
osLogLastSevEntry.setIndexNames(
    (0, "OS-SYSLOG-MIB", "osLogHistSeverity"),
)
if mibBuilder.loadTexts:
    osLogLastSevEntry.setStatus("current")


class _OsLogLastSevIndex_Type(Integer32):
    """Custom type osLogLastSevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsLogLastSevIndex_Type.__name__ = "Integer32"
_OsLogLastSevIndex_Object = MibTableColumn
osLogLastSevIndex = _OsLogLastSevIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 5, 1, 1),
    _OsLogLastSevIndex_Type()
)
osLogLastSevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osLogLastSevIndex.setStatus("current")


class _OsLogLastSevFacility_Type(DisplayString):
    """Custom type osLogLastSevFacility based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_OsLogLastSevFacility_Type.__name__ = "DisplayString"
_OsLogLastSevFacility_Object = MibTableColumn
osLogLastSevFacility = _OsLogLastSevFacility_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 5, 1, 2),
    _OsLogLastSevFacility_Type()
)
osLogLastSevFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLogLastSevFacility.setStatus("current")


class _OsLogLastSevMessage_Type(DisplayString):
    """Custom type osLogLastSevMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OsLogLastSevMessage_Type.__name__ = "DisplayString"
_OsLogLastSevMessage_Object = MibTableColumn
osLogLastSevMessage = _OsLogLastSevMessage_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 5, 1, 5),
    _OsLogLastSevMessage_Type()
)
osLogLastSevMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLogLastSevMessage.setStatus("current")
_OsLogLastSevUpTime_Type = TimeStamp
_OsLogLastSevUpTime_Object = MibTableColumn
osLogLastSevUpTime = _OsLogLastSevUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 1, 2, 5, 1, 6),
    _OsLogLastSevUpTime_Type()
)
osLogLastSevUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLogLastSevUpTime.setStatus("current")
_OsSyslogConformance_ObjectIdentity = ObjectIdentity
osSyslogConformance = _OsSyslogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 100)
)
_OsLogCompliances_ObjectIdentity = ObjectIdentity
osLogCompliances = _OsLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 100, 1)
)
_OsLogGroups_ObjectIdentity = ObjectIdentity
osLogGroups = _OsLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 100, 2)
)

# Managed Objects groups

osSyslogMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 100, 2, 1)
)
osSyslogMandatoryGroup.setObjects(
      *(("OS-SYSLOG-MIB", "osLogHistTableMaxLength"),
        ("OS-SYSLOG-MIB", "osLogNotificationsEnabled"),
        ("OS-SYSLOG-MIB", "osLogMaxSeverity"),
        ("OS-SYSLOG-MIB", "osLogDataClear"),
        ("OS-SYSLOG-MIB", "osLogNotificationsSent"),
        ("OS-SYSLOG-MIB", "osLogMsgIgnored"),
        ("OS-SYSLOG-MIB", "osLogHistFacility"),
        ("OS-SYSLOG-MIB", "osLogHistSeverity"),
        ("OS-SYSLOG-MIB", "osLogHistMessage"),
        ("OS-SYSLOG-MIB", "osLogHistUpTime"),
        ("OS-SYSLOG-MIB", "osLogLastSevFacility"),
        ("OS-SYSLOG-MIB", "osLogLastSevMessage"),
        ("OS-SYSLOG-MIB", "osLogLastSevUpTime"))
)
if mibBuilder.loadTexts:
    osSyslogMandatoryGroup.setStatus("current")


# Notification objects

osLogMsgAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 0, 1)
)
osLogMsgAlarm.setObjects(
      *(("OS-SYSLOG-MIB", "osLogHistFacility"),
        ("OS-SYSLOG-MIB", "osLogHistSeverity"),
        ("OS-SYSLOG-MIB", "osLogHistMessage"),
        ("OS-SYSLOG-MIB", "osLogHistUpTime"))
)
if mibBuilder.loadTexts:
    osLogMsgAlarm.setStatus(
        "current"
    )


# Notifications groups

osSyslogNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 100, 2, 2)
)
osSyslogNotificationsGroup.setObjects(
    ("OS-SYSLOG-MIB", "osLogMsgAlarm")
)
if mibBuilder.loadTexts:
    osSyslogNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

osLogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 32, 100, 1, 1)
)
osLogCompliance.setObjects(
      *(("OS-SYSLOG-MIB", "osSyslogMandatoryGroup"),
        ("OS-SYSLOG-MIB", "osSyslogNotificationsGroup"))
)
if mibBuilder.loadTexts:
    osLogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-SYSLOG-MIB",
    **{"SyslogSeverity": SyslogSeverity,
       "oaccess": oaccess,
       "oaOptiSwitch": oaOptiSwitch,
       "osSyslog": osSyslog,
       "osSyslogNotifications": osSyslogNotifications,
       "osLogMsgAlarm": osLogMsgAlarm,
       "osSyslogObjects": osSyslogObjects,
       "osLogGen": osLogGen,
       "osLogHistTableMaxLength": osLogHistTableMaxLength,
       "osLogNotificationsEnabled": osLogNotificationsEnabled,
       "osLogMaxSeverity": osLogMaxSeverity,
       "osLogDataClear": osLogDataClear,
       "osLogNotificationsSent": osLogNotificationsSent,
       "osLogMsgIgnored": osLogMsgIgnored,
       "osLogTables": osLogTables,
       "osLogHistoryTable": osLogHistoryTable,
       "osLogHistoryEntry": osLogHistoryEntry,
       "osLogHistIndex": osLogHistIndex,
       "osLogHistFacility": osLogHistFacility,
       "osLogHistSeverity": osLogHistSeverity,
       "osLogHistMessage": osLogHistMessage,
       "osLogHistUpTime": osLogHistUpTime,
       "osLogLastSevTable": osLogLastSevTable,
       "osLogLastSevEntry": osLogLastSevEntry,
       "osLogLastSevIndex": osLogLastSevIndex,
       "osLogLastSevFacility": osLogLastSevFacility,
       "osLogLastSevMessage": osLogLastSevMessage,
       "osLogLastSevUpTime": osLogLastSevUpTime,
       "osSyslogConformance": osSyslogConformance,
       "osLogCompliances": osLogCompliances,
       "osLogCompliance": osLogCompliance,
       "osLogGroups": osLogGroups,
       "osSyslogMandatoryGroup": osSyslogMandatoryGroup,
       "osSyslogNotificationsGroup": osSyslogNotificationsGroup}
)
