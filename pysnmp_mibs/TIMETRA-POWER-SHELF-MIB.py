# SNMP MIB module (TIMETRA-POWER-SHELF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-POWER-SHELF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:03:29 2025
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")

(TmnxHwIndex,
 tmnxCpmPowerShelfCommsFail,
 tmnxHwClass) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxHwIndex",
    "tmnxCpmPowerShelfCommsFail",
    "tmnxHwClass")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TNamedItemOrEmpty) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItemOrEmpty")


# MODULE-IDENTITY

timetraPowerShelfMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 118)
)
if mibBuilder.loadTexts:
    timetraPowerShelfMIBModule.setRevisions(
        ("2017-09-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPowerShelfType(TextualConvention, Unsigned32):
    status = "current"


class TmnxPowerShelfSuppType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("invalidPowerShelfType", 0),
          ("unassigned", 1),
          ("suppPowerShelfType2", 2),
          ("suppPowerShelfType3", 3),
          ("suppPowerShelfType4", 4),
          ("suppPowerShelfType5", 5),
          ("suppPowerShelfType6", 6),
          ("suppPowerShelfType7", 7),
          ("suppPowerShelfType8", 8),
          ("suppPowerShelfType9", 9),
          ("suppPowerShelfType10", 10),
          ("suppPowerShelfType11", 11),
          ("suppPowerShelfType12", 12),
          ("suppPowerShelfType13", 13),
          ("suppPowerShelfType14", 14),
          ("suppPowerShelfType15", 15))
    )


# MIB Managed Objects in the order of their OIDs

_TmnxPowerShelfConformance_ObjectIdentity = ObjectIdentity
tmnxPowerShelfConformance = _TmnxPowerShelfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 118)
)
_TmnxPowerShelfCompliances_ObjectIdentity = ObjectIdentity
tmnxPowerShelfCompliances = _TmnxPowerShelfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 118, 1)
)
_TmnxPowerShelfGroups_ObjectIdentity = ObjectIdentity
tmnxPowerShelfGroups = _TmnxPowerShelfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 118, 2)
)
_TmnxPowerShelfObjects_ObjectIdentity = ObjectIdentity
tmnxPowerShelfObjects = _TmnxPowerShelfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118)
)
_TmnxPowerShelfConfigTimestamps_ObjectIdentity = ObjectIdentity
tmnxPowerShelfConfigTimestamps = _TmnxPowerShelfConfigTimestamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 1)
)
_TmnxPowerShelfTableLastChanged_Type = TimeStamp
_TmnxPowerShelfTableLastChanged_Object = MibScalar
tmnxPowerShelfTableLastChanged = _TmnxPowerShelfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 1, 1),
    _TmnxPowerShelfTableLastChanged_Type()
)
tmnxPowerShelfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPowerShelfTableLastChanged.setStatus("current")
_TmnxPowerShelfTypeTable_Object = MibTable
tmnxPowerShelfTypeTable = _TmnxPowerShelfTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 2)
)
if mibBuilder.loadTexts:
    tmnxPowerShelfTypeTable.setStatus("current")
_TmnxPowerShelfTypeEntry_Object = MibTableRow
tmnxPowerShelfTypeEntry = _TmnxPowerShelfTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 2, 1)
)
tmnxPowerShelfTypeEntry.setIndexNames(
    (0, "TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxPowerShelfTypeEntry.setStatus("current")
_TmnxPowerShelfTypeIndex_Type = TmnxPowerShelfType
_TmnxPowerShelfTypeIndex_Object = MibTableColumn
tmnxPowerShelfTypeIndex = _TmnxPowerShelfTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 2, 1, 1),
    _TmnxPowerShelfTypeIndex_Type()
)
tmnxPowerShelfTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPowerShelfTypeIndex.setStatus("current")
_TmnxPowerShelfTypeName_Type = TNamedItemOrEmpty
_TmnxPowerShelfTypeName_Object = MibTableColumn
tmnxPowerShelfTypeName = _TmnxPowerShelfTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 2, 1, 2),
    _TmnxPowerShelfTypeName_Type()
)
tmnxPowerShelfTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPowerShelfTypeName.setStatus("current")
_TmnxPowerShelfTypeDescription_Type = TItemDescription
_TmnxPowerShelfTypeDescription_Object = MibTableColumn
tmnxPowerShelfTypeDescription = _TmnxPowerShelfTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 2, 1, 3),
    _TmnxPowerShelfTypeDescription_Type()
)
tmnxPowerShelfTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPowerShelfTypeDescription.setStatus("current")
_TmnxPowerShelfConfigurations_ObjectIdentity = ObjectIdentity
tmnxPowerShelfConfigurations = _TmnxPowerShelfConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3)
)
_TmnxPowerShelfTable_Object = MibTable
tmnxPowerShelfTable = _TmnxPowerShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxPowerShelfTable.setStatus("current")
_TmnxPowerShelfEntry_Object = MibTableRow
tmnxPowerShelfEntry = _TmnxPowerShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1, 1)
)
tmnxPowerShelfEntry.setIndexNames(
    (0, "TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfHwIndex"),
)
if mibBuilder.loadTexts:
    tmnxPowerShelfEntry.setStatus("current")
_TmnxPowerShelfHwIndex_Type = TmnxHwIndex
_TmnxPowerShelfHwIndex_Object = MibTableColumn
tmnxPowerShelfHwIndex = _TmnxPowerShelfHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1, 1, 1),
    _TmnxPowerShelfHwIndex_Type()
)
tmnxPowerShelfHwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPowerShelfHwIndex.setStatus("current")
_TmnxPowerShelfEntryLastChanged_Type = TimeStamp
_TmnxPowerShelfEntryLastChanged_Object = MibTableColumn
tmnxPowerShelfEntryLastChanged = _TmnxPowerShelfEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1, 1, 2),
    _TmnxPowerShelfEntryLastChanged_Type()
)
tmnxPowerShelfEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPowerShelfEntryLastChanged.setStatus("current")


class _TmnxPowerShelfAssignedType_Type(TmnxPowerShelfType):
    """Custom type tmnxPowerShelfAssignedType based on TmnxPowerShelfType"""
    defaultValue = 1


_TmnxPowerShelfAssignedType_Type.__name__ = "TmnxPowerShelfType"
_TmnxPowerShelfAssignedType_Object = MibTableColumn
tmnxPowerShelfAssignedType = _TmnxPowerShelfAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1, 1, 3),
    _TmnxPowerShelfAssignedType_Type()
)
tmnxPowerShelfAssignedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPowerShelfAssignedType.setStatus("current")
_TmnxPowerShelfEquippedType_Type = TmnxPowerShelfType
_TmnxPowerShelfEquippedType_Object = MibTableColumn
tmnxPowerShelfEquippedType = _TmnxPowerShelfEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1, 1, 4),
    _TmnxPowerShelfEquippedType_Type()
)
tmnxPowerShelfEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPowerShelfEquippedType.setStatus("current")
_TmnxPowerShelfSupportedTypes_Type = TmnxPowerShelfSuppType
_TmnxPowerShelfSupportedTypes_Object = MibTableColumn
tmnxPowerShelfSupportedTypes = _TmnxPowerShelfSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1, 1, 5),
    _TmnxPowerShelfSupportedTypes_Type()
)
tmnxPowerShelfSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPowerShelfSupportedTypes.setStatus("current")


class _TmnxPowerShelfDescription_Type(TItemDescription):
    """Custom type tmnxPowerShelfDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxPowerShelfDescription_Type.__name__ = "TItemDescription"
_TmnxPowerShelfDescription_Object = MibTableColumn
tmnxPowerShelfDescription = _TmnxPowerShelfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1, 1, 6),
    _TmnxPowerShelfDescription_Type()
)
tmnxPowerShelfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPowerShelfDescription.setStatus("current")


class _TmnxPowerShelfInputPowerMode_Type(Unsigned32):
    """Custom type tmnxPowerShelfInputPowerMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(80, 80),
    )


_TmnxPowerShelfInputPowerMode_Type.__name__ = "Unsigned32"
_TmnxPowerShelfInputPowerMode_Object = MibTableColumn
tmnxPowerShelfInputPowerMode = _TmnxPowerShelfInputPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1, 1, 7),
    _TmnxPowerShelfInputPowerMode_Type()
)
tmnxPowerShelfInputPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPowerShelfInputPowerMode.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPowerShelfInputPowerMode.setUnits("amperes")


class _TmnxPowerShelfOutputStatus_Type(Integer32):
    """Custom type tmnxPowerShelfOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("on", 1),
          ("off", 2),
          ("notEquipped", 3))
    )


_TmnxPowerShelfOutputStatus_Type.__name__ = "Integer32"
_TmnxPowerShelfOutputStatus_Object = MibTableColumn
tmnxPowerShelfOutputStatus = _TmnxPowerShelfOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 118, 3, 1, 1, 8),
    _TmnxPowerShelfOutputStatus_Type()
)
tmnxPowerShelfOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPowerShelfOutputStatus.setStatus("current")
_TmnxPowerShelfNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPowerShelfNotifyPrefix = _TmnxPowerShelfNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 120)
)
_TmnxPowerShelfNotification_ObjectIdentity = ObjectIdentity
tmnxPowerShelfNotification = _TmnxPowerShelfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 120, 0)
)
_TmnxPowerShelfNotifications_ObjectIdentity = ObjectIdentity
tmnxPowerShelfNotifications = _TmnxPowerShelfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 120, 0, 1)
)

# Managed Objects groups

tmnxPowerShelfGroupV16v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 118, 2, 1)
)
tmnxPowerShelfGroupV16v0.setObjects(
      *(("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfTableLastChanged"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfTypeName"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfTypeDescription"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfEntryLastChanged"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfAssignedType"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfEquippedType"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfSupportedTypes"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfDescription"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfInputPowerMode"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfOutputStatus"))
)
if mibBuilder.loadTexts:
    tmnxPowerShelfGroupV16v0.setStatus("current")


# Notification objects

tmnxPowerShelfInputPwrModeSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 120, 0, 1, 1)
)
tmnxPowerShelfInputPwrModeSwitch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfInputPowerMode"))
)
if mibBuilder.loadTexts:
    tmnxPowerShelfInputPwrModeSwitch.setStatus(
        "current"
    )

tmnxPowerShelfCommsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 120, 0, 1, 2)
)
tmnxPowerShelfCommsDown.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmPowerShelfCommsFail"))
)
if mibBuilder.loadTexts:
    tmnxPowerShelfCommsDown.setStatus(
        "current"
    )

tmnxPowerShelfCommsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 120, 0, 1, 3)
)
tmnxPowerShelfCommsUp.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxPowerShelfCommsUp.setStatus(
        "current"
    )

tmnxPowerShelfOutputStatusSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 120, 0, 1, 4)
)
tmnxPowerShelfOutputStatusSwitch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfOutputStatus"))
)
if mibBuilder.loadTexts:
    tmnxPowerShelfOutputStatusSwitch.setStatus(
        "current"
    )

tmnxPowerShelfOutputStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 120, 0, 1, 5)
)
tmnxPowerShelfOutputStatusDown.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfOutputStatus"))
)
if mibBuilder.loadTexts:
    tmnxPowerShelfOutputStatusDown.setStatus(
        "current"
    )

tmnxPowerShelfOutputStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 120, 0, 1, 6)
)
tmnxPowerShelfOutputStatusUp.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfOutputStatus"))
)
if mibBuilder.loadTexts:
    tmnxPowerShelfOutputStatusUp.setStatus(
        "current"
    )


# Notifications groups

tmnxPowerShelfNotifGroupV16v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 118, 2, 2)
)
tmnxPowerShelfNotifGroupV16v0.setObjects(
      *(("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfInputPwrModeSwitch"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfCommsDown"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfCommsUp"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfOutputStatusSwitch"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfOutputStatusDown"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfOutputStatusUp"))
)
if mibBuilder.loadTexts:
    tmnxPowerShelfNotifGroupV16v0.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxPowerShelfComplianceV16v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 118, 1, 1)
)
tmnxPowerShelfComplianceV16v0.setObjects(
      *(("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfGroupV16v0"),
        ("TIMETRA-POWER-SHELF-MIB", "tmnxPowerShelfNotifGroupV16v0"))
)
if mibBuilder.loadTexts:
    tmnxPowerShelfComplianceV16v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-POWER-SHELF-MIB",
    **{"TmnxPowerShelfType": TmnxPowerShelfType,
       "TmnxPowerShelfSuppType": TmnxPowerShelfSuppType,
       "timetraPowerShelfMIBModule": timetraPowerShelfMIBModule,
       "tmnxPowerShelfConformance": tmnxPowerShelfConformance,
       "tmnxPowerShelfCompliances": tmnxPowerShelfCompliances,
       "tmnxPowerShelfComplianceV16v0": tmnxPowerShelfComplianceV16v0,
       "tmnxPowerShelfGroups": tmnxPowerShelfGroups,
       "tmnxPowerShelfGroupV16v0": tmnxPowerShelfGroupV16v0,
       "tmnxPowerShelfNotifGroupV16v0": tmnxPowerShelfNotifGroupV16v0,
       "tmnxPowerShelfObjects": tmnxPowerShelfObjects,
       "tmnxPowerShelfConfigTimestamps": tmnxPowerShelfConfigTimestamps,
       "tmnxPowerShelfTableLastChanged": tmnxPowerShelfTableLastChanged,
       "tmnxPowerShelfTypeTable": tmnxPowerShelfTypeTable,
       "tmnxPowerShelfTypeEntry": tmnxPowerShelfTypeEntry,
       "tmnxPowerShelfTypeIndex": tmnxPowerShelfTypeIndex,
       "tmnxPowerShelfTypeName": tmnxPowerShelfTypeName,
       "tmnxPowerShelfTypeDescription": tmnxPowerShelfTypeDescription,
       "tmnxPowerShelfConfigurations": tmnxPowerShelfConfigurations,
       "tmnxPowerShelfTable": tmnxPowerShelfTable,
       "tmnxPowerShelfEntry": tmnxPowerShelfEntry,
       "tmnxPowerShelfHwIndex": tmnxPowerShelfHwIndex,
       "tmnxPowerShelfEntryLastChanged": tmnxPowerShelfEntryLastChanged,
       "tmnxPowerShelfAssignedType": tmnxPowerShelfAssignedType,
       "tmnxPowerShelfEquippedType": tmnxPowerShelfEquippedType,
       "tmnxPowerShelfSupportedTypes": tmnxPowerShelfSupportedTypes,
       "tmnxPowerShelfDescription": tmnxPowerShelfDescription,
       "tmnxPowerShelfInputPowerMode": tmnxPowerShelfInputPowerMode,
       "tmnxPowerShelfOutputStatus": tmnxPowerShelfOutputStatus,
       "tmnxPowerShelfNotifyPrefix": tmnxPowerShelfNotifyPrefix,
       "tmnxPowerShelfNotification": tmnxPowerShelfNotification,
       "tmnxPowerShelfNotifications": tmnxPowerShelfNotifications,
       "tmnxPowerShelfInputPwrModeSwitch": tmnxPowerShelfInputPwrModeSwitch,
       "tmnxPowerShelfCommsDown": tmnxPowerShelfCommsDown,
       "tmnxPowerShelfCommsUp": tmnxPowerShelfCommsUp,
       "tmnxPowerShelfOutputStatusSwitch": tmnxPowerShelfOutputStatusSwitch,
       "tmnxPowerShelfOutputStatusDown": tmnxPowerShelfOutputStatusDown,
       "tmnxPowerShelfOutputStatusUp": tmnxPowerShelfOutputStatusUp}
)
