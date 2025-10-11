# SNMP MIB module (SAF-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/saf/SAF-ALARM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:25 2025
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

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(tehnika,) = mibBuilder.importSymbols(
    "SAF-ENTERPRISE",
    "tehnika")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

safAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118)
)
if mibBuilder.loadTexts:
    safAlarmMIB.setRevisions(
        ("2016-03-03 00:00",
         "2014-07-03 00:00",
         "2014-07-01 00:00",
         "2008-09-17 00:00",
         "2007-05-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SafPerceivedSeverity(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6),
          ("event", 7))
    )



# MIB Managed Objects in the order of their OIDs

_SafAlarmNotifications_ObjectIdentity = ObjectIdentity
safAlarmNotifications = _SafAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 0)
)
_SafAlarmObjects_ObjectIdentity = ObjectIdentity
safAlarmObjects = _SafAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1)
)
_SafAlarmActive_ObjectIdentity = ObjectIdentity
safAlarmActive = _SafAlarmActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1)
)
_SafAlarmActiveLastChanged_Type = TimeTicks
_SafAlarmActiveLastChanged_Object = MibScalar
safAlarmActiveLastChanged = _SafAlarmActiveLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 1),
    _SafAlarmActiveLastChanged_Type()
)
safAlarmActiveLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveLastChanged.setStatus("current")
_SafAlarmActiveTable_Object = MibTable
safAlarmActiveTable = _SafAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2)
)
if mibBuilder.loadTexts:
    safAlarmActiveTable.setStatus("current")
_SafAlarmActiveEntry_Object = MibTableRow
safAlarmActiveEntry = _SafAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1)
)
safAlarmActiveEntry.setIndexNames(
    (0, "SAF-ALARM-MIB", "safAlarmActiveIndex"),
)
if mibBuilder.loadTexts:
    safAlarmActiveEntry.setStatus("current")


class _SafAlarmActiveIndex_Type(Unsigned32):
    """Custom type safAlarmActiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SafAlarmActiveIndex_Type.__name__ = "Unsigned32"
_SafAlarmActiveIndex_Object = MibTableColumn
safAlarmActiveIndex = _SafAlarmActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 1),
    _SafAlarmActiveIndex_Type()
)
safAlarmActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    safAlarmActiveIndex.setStatus("current")
_SafAlarmActiveManagedObj_Type = ObjectIdentifier
_SafAlarmActiveManagedObj_Object = MibTableColumn
safAlarmActiveManagedObj = _SafAlarmActiveManagedObj_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 2),
    _SafAlarmActiveManagedObj_Type()
)
safAlarmActiveManagedObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveManagedObj.setStatus("current")
_SafAlarmActiveDateAndTime_Type = DateAndTime
_SafAlarmActiveDateAndTime_Object = MibTableColumn
safAlarmActiveDateAndTime = _SafAlarmActiveDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 3),
    _SafAlarmActiveDateAndTime_Type()
)
safAlarmActiveDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveDateAndTime.setStatus("current")
_SafAlarmActiveEventType_Type = IANAItuEventType
_SafAlarmActiveEventType_Object = MibTableColumn
safAlarmActiveEventType = _SafAlarmActiveEventType_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 4),
    _SafAlarmActiveEventType_Type()
)
safAlarmActiveEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveEventType.setStatus("current")
_SafAlarmActiveProbableCause_Type = IANAItuProbableCause
_SafAlarmActiveProbableCause_Object = MibTableColumn
safAlarmActiveProbableCause = _SafAlarmActiveProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 5),
    _SafAlarmActiveProbableCause_Type()
)
safAlarmActiveProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveProbableCause.setStatus("current")
_SafAlarmActivePerceivedSeverity_Type = SafPerceivedSeverity
_SafAlarmActivePerceivedSeverity_Object = MibTableColumn
safAlarmActivePerceivedSeverity = _SafAlarmActivePerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 6),
    _SafAlarmActivePerceivedSeverity_Type()
)
safAlarmActivePerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActivePerceivedSeverity.setStatus("current")
_SafAlarmActiveThresholdTriggered_Type = Integer32
_SafAlarmActiveThresholdTriggered_Object = MibTableColumn
safAlarmActiveThresholdTriggered = _SafAlarmActiveThresholdTriggered_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 7),
    _SafAlarmActiveThresholdTriggered_Type()
)
safAlarmActiveThresholdTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveThresholdTriggered.setStatus("current")
_SafAlarmActiveThresholdValue_Type = Integer32
_SafAlarmActiveThresholdValue_Object = MibTableColumn
safAlarmActiveThresholdValue = _SafAlarmActiveThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 8),
    _SafAlarmActiveThresholdValue_Type()
)
safAlarmActiveThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveThresholdValue.setStatus("current")
_SafAlarmActiveThresholdTTriggered_Type = DisplayString
_SafAlarmActiveThresholdTTriggered_Object = MibTableColumn
safAlarmActiveThresholdTTriggered = _SafAlarmActiveThresholdTTriggered_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 9),
    _SafAlarmActiveThresholdTTriggered_Type()
)
safAlarmActiveThresholdTTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveThresholdTTriggered.setStatus("current")
_SafAlarmActiveThresholdTValue_Type = DisplayString
_SafAlarmActiveThresholdTValue_Object = MibTableColumn
safAlarmActiveThresholdTValue = _SafAlarmActiveThresholdTValue_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 10),
    _SafAlarmActiveThresholdTValue_Type()
)
safAlarmActiveThresholdTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveThresholdTValue.setStatus("current")
_SafAlarmActiveAdditionalText_Type = SnmpAdminString
_SafAlarmActiveAdditionalText_Object = MibTableColumn
safAlarmActiveAdditionalText = _SafAlarmActiveAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 11),
    _SafAlarmActiveAdditionalText_Type()
)
safAlarmActiveAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveAdditionalText.setStatus("current")
_SafAlarmActiveLastChangedDateAndTime_Type = DateAndTime
_SafAlarmActiveLastChangedDateAndTime_Object = MibScalar
safAlarmActiveLastChangedDateAndTime = _SafAlarmActiveLastChangedDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 3),
    _SafAlarmActiveLastChangedDateAndTime_Type()
)
safAlarmActiveLastChangedDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveLastChangedDateAndTime.setStatus("current")
_SafAlarmConformance_ObjectIdentity = ObjectIdentity
safAlarmConformance = _SafAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3)
)
_SafAlarmCompliances_ObjectIdentity = ObjectIdentity
safAlarmCompliances = _SafAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3, 1)
)
_SafAlarmGroups_ObjectIdentity = ObjectIdentity
safAlarmGroups = _SafAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3, 2)
)

# Managed Objects groups

safAlarmActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3, 2, 1)
)
safAlarmActiveGroup.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveLastChanged"),
        ("SAF-ALARM-MIB", "safAlarmActiveLastChangedDateAndTime"),
        ("SAF-ALARM-MIB", "safAlarmActiveManagedObj"),
        ("SAF-ALARM-MIB", "safAlarmActiveDateAndTime"),
        ("SAF-ALARM-MIB", "safAlarmActiveEventType"),
        ("SAF-ALARM-MIB", "safAlarmActiveProbableCause"),
        ("SAF-ALARM-MIB", "safAlarmActivePerceivedSeverity"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTriggered"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdValue"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTTriggered"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTValue"),
        ("SAF-ALARM-MIB", "safAlarmActiveAdditionalText"))
)
if mibBuilder.loadTexts:
    safAlarmActiveGroup.setStatus("current")


# Notification objects

safAlarmActiveState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 0, 2)
)
safAlarmActiveState.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveManagedObj"),
        ("SAF-ALARM-MIB", "safAlarmActiveDateAndTime"),
        ("SAF-ALARM-MIB", "safAlarmActiveEventType"),
        ("SAF-ALARM-MIB", "safAlarmActiveProbableCause"),
        ("SAF-ALARM-MIB", "safAlarmActivePerceivedSeverity"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTriggered"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdValue"),
        ("SAF-ALARM-MIB", "safAlarmActiveAdditionalText"))
)
if mibBuilder.loadTexts:
    safAlarmActiveState.setStatus(
        "current"
    )

safAlarmActiveTState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 0, 3)
)
safAlarmActiveTState.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveManagedObj"),
        ("SAF-ALARM-MIB", "safAlarmActiveDateAndTime"),
        ("SAF-ALARM-MIB", "safAlarmActiveEventType"),
        ("SAF-ALARM-MIB", "safAlarmActiveProbableCause"),
        ("SAF-ALARM-MIB", "safAlarmActivePerceivedSeverity"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTTriggered"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTValue"),
        ("SAF-ALARM-MIB", "safAlarmActiveAdditionalText"))
)
if mibBuilder.loadTexts:
    safAlarmActiveTState.setStatus(
        "current"
    )

safAlarmClearState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 0, 4)
)
safAlarmClearState.setObjects(
    ("SAF-ALARM-MIB", "safAlarmActiveManagedObj")
)
if mibBuilder.loadTexts:
    safAlarmClearState.setStatus(
        "deprecated"
    )


# Notifications groups

safAlarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3, 2, 2)
)
safAlarmNotificationsGroup.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveState"),
        ("SAF-ALARM-MIB", "safAlarmActiveTState"),
        ("SAF-ALARM-MIB", "safAlarmClearState"))
)
if mibBuilder.loadTexts:
    safAlarmNotificationsGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

safAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3, 1, 1)
)
safAlarmCompliance.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveGroup"),
        ("SAF-ALARM-MIB", "safAlarmNotificationsGroup"))
)
if mibBuilder.loadTexts:
    safAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-ALARM-MIB",
    **{"SafPerceivedSeverity": SafPerceivedSeverity,
       "safAlarmMIB": safAlarmMIB,
       "safAlarmNotifications": safAlarmNotifications,
       "safAlarmActiveState": safAlarmActiveState,
       "safAlarmActiveTState": safAlarmActiveTState,
       "safAlarmClearState": safAlarmClearState,
       "safAlarmObjects": safAlarmObjects,
       "safAlarmActive": safAlarmActive,
       "safAlarmActiveLastChanged": safAlarmActiveLastChanged,
       "safAlarmActiveTable": safAlarmActiveTable,
       "safAlarmActiveEntry": safAlarmActiveEntry,
       "safAlarmActiveIndex": safAlarmActiveIndex,
       "safAlarmActiveManagedObj": safAlarmActiveManagedObj,
       "safAlarmActiveDateAndTime": safAlarmActiveDateAndTime,
       "safAlarmActiveEventType": safAlarmActiveEventType,
       "safAlarmActiveProbableCause": safAlarmActiveProbableCause,
       "safAlarmActivePerceivedSeverity": safAlarmActivePerceivedSeverity,
       "safAlarmActiveThresholdTriggered": safAlarmActiveThresholdTriggered,
       "safAlarmActiveThresholdValue": safAlarmActiveThresholdValue,
       "safAlarmActiveThresholdTTriggered": safAlarmActiveThresholdTTriggered,
       "safAlarmActiveThresholdTValue": safAlarmActiveThresholdTValue,
       "safAlarmActiveAdditionalText": safAlarmActiveAdditionalText,
       "safAlarmActiveLastChangedDateAndTime": safAlarmActiveLastChangedDateAndTime,
       "safAlarmConformance": safAlarmConformance,
       "safAlarmCompliances": safAlarmCompliances,
       "safAlarmCompliance": safAlarmCompliance,
       "safAlarmGroups": safAlarmGroups,
       "safAlarmActiveGroup": safAlarmActiveGroup,
       "safAlarmNotificationsGroup": safAlarmNotificationsGroup}
)
