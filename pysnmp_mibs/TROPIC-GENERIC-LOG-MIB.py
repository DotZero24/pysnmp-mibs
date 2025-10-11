# SNMP MIB module (TROPIC-GENERIC-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-GENERIC-LOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:00:20 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TropicGenericTrapObjectValueType,) = mibBuilder.importSymbols(
    "TROPIC-GENERIC-NOTIFICATION-MIB",
    "TropicGenericTrapObjectValueType")

(tnGenericLogMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnGenericLogMIB",
    "tnSystemModules")

(TnCondition,
 TnEntityType,
 TnTrapCategory) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnCondition",
    "TnEntityType",
    "TnTrapCategory")


# MODULE-IDENTITY

tnGenericLogMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 13)
)
if mibBuilder.loadTexts:
    tnGenericLogMibModule.setRevisions(
        ("2018-05-25 12:00",
         "2018-02-23 12:00",
         "2017-07-07 12:00",
         "2017-03-06 12:00",
         "2017-01-31 12:00",
         "2016-12-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnGenericActiveAlarm_ObjectIdentity = ObjectIdentity
tnGenericActiveAlarm = _TnGenericActiveAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1)
)
_TnGenericActiveAlarmObjects_ObjectIdentity = ObjectIdentity
tnGenericActiveAlarmObjects = _TnGenericActiveAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1)
)
_TnGenericActiveAlarmTable_Object = MibTable
tnGenericActiveAlarmTable = _TnGenericActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnGenericActiveAlarmTable.setStatus("current")
_TnGenericActiveAlarmEntry_Object = MibTableRow
tnGenericActiveAlarmEntry = _TnGenericActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1)
)
tnGenericActiveAlarmEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericActiveAlarmEntry.setStatus("current")


class _TnGenericActiveAlarmSerialNumber_Type(Unsigned32):
    """Custom type tnGenericActiveAlarmSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericActiveAlarmSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericActiveAlarmSerialNumber_Object = MibTableColumn
tnGenericActiveAlarmSerialNumber = _TnGenericActiveAlarmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 1),
    _TnGenericActiveAlarmSerialNumber_Type()
)
tnGenericActiveAlarmSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmSerialNumber.setStatus("current")
_TnGenericActiveAlarmType_Type = ObjectIdentifier
_TnGenericActiveAlarmType_Object = MibTableColumn
tnGenericActiveAlarmType = _TnGenericActiveAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 2),
    _TnGenericActiveAlarmType_Type()
)
tnGenericActiveAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmType.setStatus("current")
_TnGenericActiveAlarmObject_Type = ObjectIdentifier
_TnGenericActiveAlarmObject_Object = MibTableColumn
tnGenericActiveAlarmObject = _TnGenericActiveAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 3),
    _TnGenericActiveAlarmObject_Type()
)
tnGenericActiveAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmObject.setStatus("current")
_TnGenericActiveAlarmObjectInstance_Type = SnmpAdminString
_TnGenericActiveAlarmObjectInstance_Object = MibTableColumn
tnGenericActiveAlarmObjectInstance = _TnGenericActiveAlarmObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 4),
    _TnGenericActiveAlarmObjectInstance_Type()
)
tnGenericActiveAlarmObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmObjectInstance.setStatus("current")
_TnGenericActiveAlarmTime_Type = Unsigned32
_TnGenericActiveAlarmTime_Object = MibTableColumn
tnGenericActiveAlarmTime = _TnGenericActiveAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 5),
    _TnGenericActiveAlarmTime_Type()
)
tnGenericActiveAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmTime.setStatus("current")
_TnGenericActiveAlarmCategory_Type = TnTrapCategory
_TnGenericActiveAlarmCategory_Object = MibTableColumn
tnGenericActiveAlarmCategory = _TnGenericActiveAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 6),
    _TnGenericActiveAlarmCategory_Type()
)
tnGenericActiveAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmCategory.setStatus("current")


class _TnGenericActiveAlarmDescr_Type(SnmpAdminString):
    """Custom type tnGenericActiveAlarmDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericActiveAlarmDescr_Type.__name__ = "SnmpAdminString"
_TnGenericActiveAlarmDescr_Object = MibTableColumn
tnGenericActiveAlarmDescr = _TnGenericActiveAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 7),
    _TnGenericActiveAlarmDescr_Type()
)
tnGenericActiveAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmDescr.setStatus("current")


class _TnGenericActiveAlarmData_Type(SnmpAdminString):
    """Custom type tnGenericActiveAlarmData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericActiveAlarmData_Type.__name__ = "SnmpAdminString"
_TnGenericActiveAlarmData_Object = MibTableColumn
tnGenericActiveAlarmData = _TnGenericActiveAlarmData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 8),
    _TnGenericActiveAlarmData_Type()
)
tnGenericActiveAlarmData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmData.setStatus("current")
_TnGenericActiveAlarmServiceAffecting_Type = TruthValue
_TnGenericActiveAlarmServiceAffecting_Object = MibTableColumn
tnGenericActiveAlarmServiceAffecting = _TnGenericActiveAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 9),
    _TnGenericActiveAlarmServiceAffecting_Type()
)
tnGenericActiveAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmServiceAffecting.setStatus("current")
_TnGenericActiveAlarmCondition_Type = TnCondition
_TnGenericActiveAlarmCondition_Object = MibTableColumn
tnGenericActiveAlarmCondition = _TnGenericActiveAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 10),
    _TnGenericActiveAlarmCondition_Type()
)
tnGenericActiveAlarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmCondition.setStatus("current")
_TnGenericActiveAlarmDateAndTime_Type = DateAndTime
_TnGenericActiveAlarmDateAndTime_Object = MibTableColumn
tnGenericActiveAlarmDateAndTime = _TnGenericActiveAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 11),
    _TnGenericActiveAlarmDateAndTime_Type()
)
tnGenericActiveAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmDateAndTime.setStatus("current")
_TnGenericActiveAlarmEntityType_Type = TnEntityType
_TnGenericActiveAlarmEntityType_Object = MibTableColumn
tnGenericActiveAlarmEntityType = _TnGenericActiveAlarmEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 1, 1, 1, 12),
    _TnGenericActiveAlarmEntityType_Type()
)
tnGenericActiveAlarmEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericActiveAlarmEntityType.setStatus("current")
_TnGenericActiveAlarmConformance_ObjectIdentity = ObjectIdentity
tnGenericActiveAlarmConformance = _TnGenericActiveAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 2)
)
_TnGenericActiveAlarmCompliances_ObjectIdentity = ObjectIdentity
tnGenericActiveAlarmCompliances = _TnGenericActiveAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 2, 1)
)
_TnGenericActiveAlarmGroups_ObjectIdentity = ObjectIdentity
tnGenericActiveAlarmGroups = _TnGenericActiveAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 2, 2)
)
_TnGenericLog_ObjectIdentity = ObjectIdentity
tnGenericLog = _TnGenericLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2)
)
_TnGenericLogObjects_ObjectIdentity = ObjectIdentity
tnGenericLogObjects = _TnGenericLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1)
)
_TnGenericCriticalAlarmLogBufferTable_Object = MibTable
tnGenericCriticalAlarmLogBufferTable = _TnGenericCriticalAlarmLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogBufferTable.setStatus("current")
_TnGenericCriticalAlarmLogBufferEntry_Object = MibTableRow
tnGenericCriticalAlarmLogBufferEntry = _TnGenericCriticalAlarmLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1)
)
tnGenericCriticalAlarmLogBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogBufferEntry.setStatus("current")


class _TnGenericCriticalAlarmLogSerialNumber_Type(Unsigned32):
    """Custom type tnGenericCriticalAlarmLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericCriticalAlarmLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericCriticalAlarmLogSerialNumber_Object = MibTableColumn
tnGenericCriticalAlarmLogSerialNumber = _TnGenericCriticalAlarmLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 1),
    _TnGenericCriticalAlarmLogSerialNumber_Type()
)
tnGenericCriticalAlarmLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogSerialNumber.setStatus("current")
_TnGenericCriticalAlarmLogType_Type = ObjectIdentifier
_TnGenericCriticalAlarmLogType_Object = MibTableColumn
tnGenericCriticalAlarmLogType = _TnGenericCriticalAlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 2),
    _TnGenericCriticalAlarmLogType_Type()
)
tnGenericCriticalAlarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogType.setStatus("current")
_TnGenericCriticalAlarmLogObject_Type = ObjectIdentifier
_TnGenericCriticalAlarmLogObject_Object = MibTableColumn
tnGenericCriticalAlarmLogObject = _TnGenericCriticalAlarmLogObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 3),
    _TnGenericCriticalAlarmLogObject_Type()
)
tnGenericCriticalAlarmLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogObject.setStatus("current")
_TnGenericCriticalAlarmLogObjectInstance_Type = SnmpAdminString
_TnGenericCriticalAlarmLogObjectInstance_Object = MibTableColumn
tnGenericCriticalAlarmLogObjectInstance = _TnGenericCriticalAlarmLogObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 4),
    _TnGenericCriticalAlarmLogObjectInstance_Type()
)
tnGenericCriticalAlarmLogObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogObjectInstance.setStatus("current")
_TnGenericCriticalAlarmLogTime_Type = Unsigned32
_TnGenericCriticalAlarmLogTime_Object = MibTableColumn
tnGenericCriticalAlarmLogTime = _TnGenericCriticalAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 5),
    _TnGenericCriticalAlarmLogTime_Type()
)
tnGenericCriticalAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogTime.setStatus("current")


class _TnGenericCriticalAlarmLogDescr_Type(SnmpAdminString):
    """Custom type tnGenericCriticalAlarmLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericCriticalAlarmLogDescr_Type.__name__ = "SnmpAdminString"
_TnGenericCriticalAlarmLogDescr_Object = MibTableColumn
tnGenericCriticalAlarmLogDescr = _TnGenericCriticalAlarmLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 6),
    _TnGenericCriticalAlarmLogDescr_Type()
)
tnGenericCriticalAlarmLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogDescr.setStatus("current")


class _TnGenericCriticalAlarmLogData_Type(SnmpAdminString):
    """Custom type tnGenericCriticalAlarmLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericCriticalAlarmLogData_Type.__name__ = "SnmpAdminString"
_TnGenericCriticalAlarmLogData_Object = MibTableColumn
tnGenericCriticalAlarmLogData = _TnGenericCriticalAlarmLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 7),
    _TnGenericCriticalAlarmLogData_Type()
)
tnGenericCriticalAlarmLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogData.setStatus("current")
_TnGenericCriticalAlarmLogServiceAffecting_Type = TruthValue
_TnGenericCriticalAlarmLogServiceAffecting_Object = MibTableColumn
tnGenericCriticalAlarmLogServiceAffecting = _TnGenericCriticalAlarmLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 8),
    _TnGenericCriticalAlarmLogServiceAffecting_Type()
)
tnGenericCriticalAlarmLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogServiceAffecting.setStatus("current")
_TnGenericCriticalAlarmLogCondition_Type = TnCondition
_TnGenericCriticalAlarmLogCondition_Object = MibTableColumn
tnGenericCriticalAlarmLogCondition = _TnGenericCriticalAlarmLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 9),
    _TnGenericCriticalAlarmLogCondition_Type()
)
tnGenericCriticalAlarmLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogCondition.setStatus("current")
_TnGenericCriticalAlarmLogDateAndTime_Type = DateAndTime
_TnGenericCriticalAlarmLogDateAndTime_Object = MibTableColumn
tnGenericCriticalAlarmLogDateAndTime = _TnGenericCriticalAlarmLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 10),
    _TnGenericCriticalAlarmLogDateAndTime_Type()
)
tnGenericCriticalAlarmLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogDateAndTime.setStatus("current")
_TnGenericCriticalAlarmLogEntityType_Type = TnEntityType
_TnGenericCriticalAlarmLogEntityType_Object = MibTableColumn
tnGenericCriticalAlarmLogEntityType = _TnGenericCriticalAlarmLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 1, 1, 11),
    _TnGenericCriticalAlarmLogEntityType_Type()
)
tnGenericCriticalAlarmLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmLogEntityType.setStatus("current")
_TnGenericMajorAlarmLogBufferTable_Object = MibTable
tnGenericMajorAlarmLogBufferTable = _TnGenericMajorAlarmLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogBufferTable.setStatus("current")
_TnGenericMajorAlarmLogBufferEntry_Object = MibTableRow
tnGenericMajorAlarmLogBufferEntry = _TnGenericMajorAlarmLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1)
)
tnGenericMajorAlarmLogBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogBufferEntry.setStatus("current")


class _TnGenericMajorAlarmLogSerialNumber_Type(Unsigned32):
    """Custom type tnGenericMajorAlarmLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericMajorAlarmLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericMajorAlarmLogSerialNumber_Object = MibTableColumn
tnGenericMajorAlarmLogSerialNumber = _TnGenericMajorAlarmLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 1),
    _TnGenericMajorAlarmLogSerialNumber_Type()
)
tnGenericMajorAlarmLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogSerialNumber.setStatus("current")
_TnGenericMajorAlarmLogType_Type = ObjectIdentifier
_TnGenericMajorAlarmLogType_Object = MibTableColumn
tnGenericMajorAlarmLogType = _TnGenericMajorAlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 2),
    _TnGenericMajorAlarmLogType_Type()
)
tnGenericMajorAlarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogType.setStatus("current")
_TnGenericMajorAlarmLogObject_Type = ObjectIdentifier
_TnGenericMajorAlarmLogObject_Object = MibTableColumn
tnGenericMajorAlarmLogObject = _TnGenericMajorAlarmLogObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 3),
    _TnGenericMajorAlarmLogObject_Type()
)
tnGenericMajorAlarmLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogObject.setStatus("current")
_TnGenericMajorAlarmLogObjectInstance_Type = SnmpAdminString
_TnGenericMajorAlarmLogObjectInstance_Object = MibTableColumn
tnGenericMajorAlarmLogObjectInstance = _TnGenericMajorAlarmLogObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 4),
    _TnGenericMajorAlarmLogObjectInstance_Type()
)
tnGenericMajorAlarmLogObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogObjectInstance.setStatus("current")
_TnGenericMajorAlarmLogTime_Type = Unsigned32
_TnGenericMajorAlarmLogTime_Object = MibTableColumn
tnGenericMajorAlarmLogTime = _TnGenericMajorAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 5),
    _TnGenericMajorAlarmLogTime_Type()
)
tnGenericMajorAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogTime.setStatus("current")


class _TnGenericMajorAlarmLogDescr_Type(SnmpAdminString):
    """Custom type tnGenericMajorAlarmLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericMajorAlarmLogDescr_Type.__name__ = "SnmpAdminString"
_TnGenericMajorAlarmLogDescr_Object = MibTableColumn
tnGenericMajorAlarmLogDescr = _TnGenericMajorAlarmLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 6),
    _TnGenericMajorAlarmLogDescr_Type()
)
tnGenericMajorAlarmLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogDescr.setStatus("current")


class _TnGenericMajorAlarmLogData_Type(SnmpAdminString):
    """Custom type tnGenericMajorAlarmLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericMajorAlarmLogData_Type.__name__ = "SnmpAdminString"
_TnGenericMajorAlarmLogData_Object = MibTableColumn
tnGenericMajorAlarmLogData = _TnGenericMajorAlarmLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 7),
    _TnGenericMajorAlarmLogData_Type()
)
tnGenericMajorAlarmLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogData.setStatus("current")
_TnGenericMajorAlarmLogServiceAffecting_Type = TruthValue
_TnGenericMajorAlarmLogServiceAffecting_Object = MibTableColumn
tnGenericMajorAlarmLogServiceAffecting = _TnGenericMajorAlarmLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 8),
    _TnGenericMajorAlarmLogServiceAffecting_Type()
)
tnGenericMajorAlarmLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogServiceAffecting.setStatus("current")
_TnGenericMajorAlarmLogCondition_Type = TnCondition
_TnGenericMajorAlarmLogCondition_Object = MibTableColumn
tnGenericMajorAlarmLogCondition = _TnGenericMajorAlarmLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 9),
    _TnGenericMajorAlarmLogCondition_Type()
)
tnGenericMajorAlarmLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogCondition.setStatus("current")
_TnGenericMajorAlarmLogDateAndTime_Type = DateAndTime
_TnGenericMajorAlarmLogDateAndTime_Object = MibTableColumn
tnGenericMajorAlarmLogDateAndTime = _TnGenericMajorAlarmLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 10),
    _TnGenericMajorAlarmLogDateAndTime_Type()
)
tnGenericMajorAlarmLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogDateAndTime.setStatus("current")
_TnGenericMajorAlarmLogEntityType_Type = TnEntityType
_TnGenericMajorAlarmLogEntityType_Object = MibTableColumn
tnGenericMajorAlarmLogEntityType = _TnGenericMajorAlarmLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 2, 1, 11),
    _TnGenericMajorAlarmLogEntityType_Type()
)
tnGenericMajorAlarmLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMajorAlarmLogEntityType.setStatus("current")
_TnGenericMinorAlarmLogBufferTable_Object = MibTable
tnGenericMinorAlarmLogBufferTable = _TnGenericMinorAlarmLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogBufferTable.setStatus("current")
_TnGenericMinorAlarmLogBufferEntry_Object = MibTableRow
tnGenericMinorAlarmLogBufferEntry = _TnGenericMinorAlarmLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1)
)
tnGenericMinorAlarmLogBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogBufferEntry.setStatus("current")


class _TnGenericMinorAlarmLogSerialNumber_Type(Unsigned32):
    """Custom type tnGenericMinorAlarmLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericMinorAlarmLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericMinorAlarmLogSerialNumber_Object = MibTableColumn
tnGenericMinorAlarmLogSerialNumber = _TnGenericMinorAlarmLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 1),
    _TnGenericMinorAlarmLogSerialNumber_Type()
)
tnGenericMinorAlarmLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogSerialNumber.setStatus("current")
_TnGenericMinorAlarmLogType_Type = ObjectIdentifier
_TnGenericMinorAlarmLogType_Object = MibTableColumn
tnGenericMinorAlarmLogType = _TnGenericMinorAlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 2),
    _TnGenericMinorAlarmLogType_Type()
)
tnGenericMinorAlarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogType.setStatus("current")
_TnGenericMinorAlarmLogObject_Type = ObjectIdentifier
_TnGenericMinorAlarmLogObject_Object = MibTableColumn
tnGenericMinorAlarmLogObject = _TnGenericMinorAlarmLogObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 3),
    _TnGenericMinorAlarmLogObject_Type()
)
tnGenericMinorAlarmLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogObject.setStatus("current")
_TnGenericMinorAlarmLogObjectInstance_Type = SnmpAdminString
_TnGenericMinorAlarmLogObjectInstance_Object = MibTableColumn
tnGenericMinorAlarmLogObjectInstance = _TnGenericMinorAlarmLogObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 4),
    _TnGenericMinorAlarmLogObjectInstance_Type()
)
tnGenericMinorAlarmLogObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogObjectInstance.setStatus("current")
_TnGenericMinorAlarmLogTime_Type = Unsigned32
_TnGenericMinorAlarmLogTime_Object = MibTableColumn
tnGenericMinorAlarmLogTime = _TnGenericMinorAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 5),
    _TnGenericMinorAlarmLogTime_Type()
)
tnGenericMinorAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogTime.setStatus("current")


class _TnGenericMinorAlarmLogDescr_Type(SnmpAdminString):
    """Custom type tnGenericMinorAlarmLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericMinorAlarmLogDescr_Type.__name__ = "SnmpAdminString"
_TnGenericMinorAlarmLogDescr_Object = MibTableColumn
tnGenericMinorAlarmLogDescr = _TnGenericMinorAlarmLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 6),
    _TnGenericMinorAlarmLogDescr_Type()
)
tnGenericMinorAlarmLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogDescr.setStatus("current")


class _TnGenericMinorAlarmLogData_Type(SnmpAdminString):
    """Custom type tnGenericMinorAlarmLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericMinorAlarmLogData_Type.__name__ = "SnmpAdminString"
_TnGenericMinorAlarmLogData_Object = MibTableColumn
tnGenericMinorAlarmLogData = _TnGenericMinorAlarmLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 7),
    _TnGenericMinorAlarmLogData_Type()
)
tnGenericMinorAlarmLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogData.setStatus("current")
_TnGenericMinorAlarmLogServiceAffecting_Type = TruthValue
_TnGenericMinorAlarmLogServiceAffecting_Object = MibTableColumn
tnGenericMinorAlarmLogServiceAffecting = _TnGenericMinorAlarmLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 8),
    _TnGenericMinorAlarmLogServiceAffecting_Type()
)
tnGenericMinorAlarmLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogServiceAffecting.setStatus("current")
_TnGenericMinorAlarmLogCondition_Type = TnCondition
_TnGenericMinorAlarmLogCondition_Object = MibTableColumn
tnGenericMinorAlarmLogCondition = _TnGenericMinorAlarmLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 9),
    _TnGenericMinorAlarmLogCondition_Type()
)
tnGenericMinorAlarmLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogCondition.setStatus("current")
_TnGenericMinorAlarmLogDateAndTime_Type = DateAndTime
_TnGenericMinorAlarmLogDateAndTime_Object = MibTableColumn
tnGenericMinorAlarmLogDateAndTime = _TnGenericMinorAlarmLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 10),
    _TnGenericMinorAlarmLogDateAndTime_Type()
)
tnGenericMinorAlarmLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogDateAndTime.setStatus("current")
_TnGenericMinorAlarmLogEntityType_Type = TnEntityType
_TnGenericMinorAlarmLogEntityType_Object = MibTableColumn
tnGenericMinorAlarmLogEntityType = _TnGenericMinorAlarmLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 3, 1, 11),
    _TnGenericMinorAlarmLogEntityType_Type()
)
tnGenericMinorAlarmLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericMinorAlarmLogEntityType.setStatus("current")
_TnGenericStateChangeLogBufferTable_Object = MibTable
tnGenericStateChangeLogBufferTable = _TnGenericStateChangeLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnGenericStateChangeLogBufferTable.setStatus("current")
_TnGenericStateChangeLogBufferEntry_Object = MibTableRow
tnGenericStateChangeLogBufferEntry = _TnGenericStateChangeLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1)
)
tnGenericStateChangeLogBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericStateChangeLogBufferEntry.setStatus("current")


class _TnGenericStateChangeLogSerialNumber_Type(Unsigned32):
    """Custom type tnGenericStateChangeLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericStateChangeLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericStateChangeLogSerialNumber_Object = MibTableColumn
tnGenericStateChangeLogSerialNumber = _TnGenericStateChangeLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 1),
    _TnGenericStateChangeLogSerialNumber_Type()
)
tnGenericStateChangeLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogSerialNumber.setStatus("current")
_TnGenericStateChangeLogType_Type = ObjectIdentifier
_TnGenericStateChangeLogType_Object = MibTableColumn
tnGenericStateChangeLogType = _TnGenericStateChangeLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 2),
    _TnGenericStateChangeLogType_Type()
)
tnGenericStateChangeLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogType.setStatus("current")
_TnGenericStateChangeLogObject_Type = ObjectIdentifier
_TnGenericStateChangeLogObject_Object = MibTableColumn
tnGenericStateChangeLogObject = _TnGenericStateChangeLogObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 3),
    _TnGenericStateChangeLogObject_Type()
)
tnGenericStateChangeLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObject.setStatus("current")
_TnGenericStateChangeLogObjectInstance_Type = SnmpAdminString
_TnGenericStateChangeLogObjectInstance_Object = MibTableColumn
tnGenericStateChangeLogObjectInstance = _TnGenericStateChangeLogObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 4),
    _TnGenericStateChangeLogObjectInstance_Type()
)
tnGenericStateChangeLogObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectInstance.setStatus("current")
_TnGenericStateChangeLogTime_Type = Unsigned32
_TnGenericStateChangeLogTime_Object = MibTableColumn
tnGenericStateChangeLogTime = _TnGenericStateChangeLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 5),
    _TnGenericStateChangeLogTime_Type()
)
tnGenericStateChangeLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogTime.setStatus("current")
_TnGenericStateChangeLogObjectValueType_Type = TropicGenericTrapObjectValueType
_TnGenericStateChangeLogObjectValueType_Object = MibTableColumn
tnGenericStateChangeLogObjectValueType = _TnGenericStateChangeLogObjectValueType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 6),
    _TnGenericStateChangeLogObjectValueType_Type()
)
tnGenericStateChangeLogObjectValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectValueType.setStatus("current")
_TnGenericStateChangeLogObjectCounter32Val_Type = Counter32
_TnGenericStateChangeLogObjectCounter32Val_Object = MibTableColumn
tnGenericStateChangeLogObjectCounter32Val = _TnGenericStateChangeLogObjectCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 7),
    _TnGenericStateChangeLogObjectCounter32Val_Type()
)
tnGenericStateChangeLogObjectCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectCounter32Val.setStatus("current")
_TnGenericStateChangeLogObjectUnsigned32Val_Type = Unsigned32
_TnGenericStateChangeLogObjectUnsigned32Val_Object = MibTableColumn
tnGenericStateChangeLogObjectUnsigned32Val = _TnGenericStateChangeLogObjectUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 8),
    _TnGenericStateChangeLogObjectUnsigned32Val_Type()
)
tnGenericStateChangeLogObjectUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectUnsigned32Val.setStatus("current")
_TnGenericStateChangeLogObjectTimeTicksVal_Type = TimeTicks
_TnGenericStateChangeLogObjectTimeTicksVal_Object = MibTableColumn
tnGenericStateChangeLogObjectTimeTicksVal = _TnGenericStateChangeLogObjectTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 9),
    _TnGenericStateChangeLogObjectTimeTicksVal_Type()
)
tnGenericStateChangeLogObjectTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectTimeTicksVal.setStatus("current")
_TnGenericStateChangeLogObjectInteger32Val_Type = Integer32
_TnGenericStateChangeLogObjectInteger32Val_Object = MibTableColumn
tnGenericStateChangeLogObjectInteger32Val = _TnGenericStateChangeLogObjectInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 10),
    _TnGenericStateChangeLogObjectInteger32Val_Type()
)
tnGenericStateChangeLogObjectInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectInteger32Val.setStatus("current")
_TnGenericStateChangeLogObjectOctetStringVal_Type = OctetString
_TnGenericStateChangeLogObjectOctetStringVal_Object = MibTableColumn
tnGenericStateChangeLogObjectOctetStringVal = _TnGenericStateChangeLogObjectOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 11),
    _TnGenericStateChangeLogObjectOctetStringVal_Type()
)
tnGenericStateChangeLogObjectOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectOctetStringVal.setStatus("current")
_TnGenericStateChangeLogObjectIpAddressVal_Type = IpAddress
_TnGenericStateChangeLogObjectIpAddressVal_Object = MibTableColumn
tnGenericStateChangeLogObjectIpAddressVal = _TnGenericStateChangeLogObjectIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 12),
    _TnGenericStateChangeLogObjectIpAddressVal_Type()
)
tnGenericStateChangeLogObjectIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectIpAddressVal.setStatus("current")
_TnGenericStateChangeLogObjectOidVal_Type = ObjectIdentifier
_TnGenericStateChangeLogObjectOidVal_Object = MibTableColumn
tnGenericStateChangeLogObjectOidVal = _TnGenericStateChangeLogObjectOidVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 13),
    _TnGenericStateChangeLogObjectOidVal_Type()
)
tnGenericStateChangeLogObjectOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectOidVal.setStatus("current")
_TnGenericStateChangeLogObjectCounter64Val_Type = Counter64
_TnGenericStateChangeLogObjectCounter64Val_Object = MibTableColumn
tnGenericStateChangeLogObjectCounter64Val = _TnGenericStateChangeLogObjectCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 14),
    _TnGenericStateChangeLogObjectCounter64Val_Type()
)
tnGenericStateChangeLogObjectCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogObjectCounter64Val.setStatus("current")
_TnGenericStateChangeLogDateAndTime_Type = DateAndTime
_TnGenericStateChangeLogDateAndTime_Object = MibTableColumn
tnGenericStateChangeLogDateAndTime = _TnGenericStateChangeLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 4, 1, 15),
    _TnGenericStateChangeLogDateAndTime_Type()
)
tnGenericStateChangeLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericStateChangeLogDateAndTime.setStatus("current")
_TnGenericUserActionLogBufferTable_Object = MibTable
tnGenericUserActionLogBufferTable = _TnGenericUserActionLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnGenericUserActionLogBufferTable.setStatus("current")
_TnGenericUserActionLogBufferEntry_Object = MibTableRow
tnGenericUserActionLogBufferEntry = _TnGenericUserActionLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1)
)
tnGenericUserActionLogBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericUserActionLogBufferEntry.setStatus("current")


class _TnGenericUserActionLogSerialNumber_Type(Unsigned32):
    """Custom type tnGenericUserActionLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericUserActionLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericUserActionLogSerialNumber_Object = MibTableColumn
tnGenericUserActionLogSerialNumber = _TnGenericUserActionLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 1),
    _TnGenericUserActionLogSerialNumber_Type()
)
tnGenericUserActionLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericUserActionLogSerialNumber.setStatus("current")
_TnGenericUserActionLogType_Type = ObjectIdentifier
_TnGenericUserActionLogType_Object = MibTableColumn
tnGenericUserActionLogType = _TnGenericUserActionLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 2),
    _TnGenericUserActionLogType_Type()
)
tnGenericUserActionLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogType.setStatus("current")
_TnGenericUserActionLogObject_Type = ObjectIdentifier
_TnGenericUserActionLogObject_Object = MibTableColumn
tnGenericUserActionLogObject = _TnGenericUserActionLogObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 3),
    _TnGenericUserActionLogObject_Type()
)
tnGenericUserActionLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObject.setStatus("current")
_TnGenericUserActionLogObjectInstance_Type = SnmpAdminString
_TnGenericUserActionLogObjectInstance_Object = MibTableColumn
tnGenericUserActionLogObjectInstance = _TnGenericUserActionLogObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 4),
    _TnGenericUserActionLogObjectInstance_Type()
)
tnGenericUserActionLogObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectInstance.setStatus("current")
_TnGenericUserActionLogTime_Type = Unsigned32
_TnGenericUserActionLogTime_Object = MibTableColumn
tnGenericUserActionLogTime = _TnGenericUserActionLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 5),
    _TnGenericUserActionLogTime_Type()
)
tnGenericUserActionLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogTime.setStatus("current")
_TnGenericUserActionLogObjectValueType_Type = TropicGenericTrapObjectValueType
_TnGenericUserActionLogObjectValueType_Object = MibTableColumn
tnGenericUserActionLogObjectValueType = _TnGenericUserActionLogObjectValueType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 6),
    _TnGenericUserActionLogObjectValueType_Type()
)
tnGenericUserActionLogObjectValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectValueType.setStatus("current")
_TnGenericUserActionLogObjectCounter32Val_Type = Counter32
_TnGenericUserActionLogObjectCounter32Val_Object = MibTableColumn
tnGenericUserActionLogObjectCounter32Val = _TnGenericUserActionLogObjectCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 7),
    _TnGenericUserActionLogObjectCounter32Val_Type()
)
tnGenericUserActionLogObjectCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectCounter32Val.setStatus("current")
_TnGenericUserActionLogObjectUnsigned32Val_Type = Unsigned32
_TnGenericUserActionLogObjectUnsigned32Val_Object = MibTableColumn
tnGenericUserActionLogObjectUnsigned32Val = _TnGenericUserActionLogObjectUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 8),
    _TnGenericUserActionLogObjectUnsigned32Val_Type()
)
tnGenericUserActionLogObjectUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectUnsigned32Val.setStatus("current")
_TnGenericUserActionLogObjectTimeTicksVal_Type = TimeTicks
_TnGenericUserActionLogObjectTimeTicksVal_Object = MibTableColumn
tnGenericUserActionLogObjectTimeTicksVal = _TnGenericUserActionLogObjectTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 9),
    _TnGenericUserActionLogObjectTimeTicksVal_Type()
)
tnGenericUserActionLogObjectTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectTimeTicksVal.setStatus("current")
_TnGenericUserActionLogObjectInteger32Val_Type = Integer32
_TnGenericUserActionLogObjectInteger32Val_Object = MibTableColumn
tnGenericUserActionLogObjectInteger32Val = _TnGenericUserActionLogObjectInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 10),
    _TnGenericUserActionLogObjectInteger32Val_Type()
)
tnGenericUserActionLogObjectInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectInteger32Val.setStatus("current")
_TnGenericUserActionLogObjectOctetStringVal_Type = OctetString
_TnGenericUserActionLogObjectOctetStringVal_Object = MibTableColumn
tnGenericUserActionLogObjectOctetStringVal = _TnGenericUserActionLogObjectOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 11),
    _TnGenericUserActionLogObjectOctetStringVal_Type()
)
tnGenericUserActionLogObjectOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectOctetStringVal.setStatus("current")
_TnGenericUserActionLogObjectIpAddressVal_Type = IpAddress
_TnGenericUserActionLogObjectIpAddressVal_Object = MibTableColumn
tnGenericUserActionLogObjectIpAddressVal = _TnGenericUserActionLogObjectIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 12),
    _TnGenericUserActionLogObjectIpAddressVal_Type()
)
tnGenericUserActionLogObjectIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectIpAddressVal.setStatus("current")
_TnGenericUserActionLogObjectOidVal_Type = ObjectIdentifier
_TnGenericUserActionLogObjectOidVal_Object = MibTableColumn
tnGenericUserActionLogObjectOidVal = _TnGenericUserActionLogObjectOidVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 13),
    _TnGenericUserActionLogObjectOidVal_Type()
)
tnGenericUserActionLogObjectOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectOidVal.setStatus("current")
_TnGenericUserActionLogObjectCounter64Val_Type = Counter64
_TnGenericUserActionLogObjectCounter64Val_Object = MibTableColumn
tnGenericUserActionLogObjectCounter64Val = _TnGenericUserActionLogObjectCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 14),
    _TnGenericUserActionLogObjectCounter64Val_Type()
)
tnGenericUserActionLogObjectCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogObjectCounter64Val.setStatus("current")
_TnGenericUserActionLogDateAndTime_Type = DateAndTime
_TnGenericUserActionLogDateAndTime_Object = MibTableColumn
tnGenericUserActionLogDateAndTime = _TnGenericUserActionLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 15),
    _TnGenericUserActionLogDateAndTime_Type()
)
tnGenericUserActionLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogDateAndTime.setStatus("current")
_TnGenericUserActionLogConfigurationChangeCounter_Type = Unsigned32
_TnGenericUserActionLogConfigurationChangeCounter_Object = MibTableColumn
tnGenericUserActionLogConfigurationChangeCounter = _TnGenericUserActionLogConfigurationChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 16),
    _TnGenericUserActionLogConfigurationChangeCounter_Type()
)
tnGenericUserActionLogConfigurationChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogConfigurationChangeCounter.setStatus("current")
_TnGenericUserActionLogUserID_Type = SnmpAdminString
_TnGenericUserActionLogUserID_Object = MibTableColumn
tnGenericUserActionLogUserID = _TnGenericUserActionLogUserID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 5, 1, 17),
    _TnGenericUserActionLogUserID_Type()
)
tnGenericUserActionLogUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericUserActionLogUserID.setStatus("current")
_TnGenericGeneralEventLogBufferTable_Object = MibTable
tnGenericGeneralEventLogBufferTable = _TnGenericGeneralEventLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogBufferTable.setStatus("current")
_TnGenericGeneralEventLogBufferEntry_Object = MibTableRow
tnGenericGeneralEventLogBufferEntry = _TnGenericGeneralEventLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6, 1)
)
tnGenericGeneralEventLogBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericGeneralEventLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogBufferEntry.setStatus("current")


class _TnGenericGeneralEventLogSerialNumber_Type(Unsigned32):
    """Custom type tnGenericGeneralEventLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericGeneralEventLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericGeneralEventLogSerialNumber_Object = MibTableColumn
tnGenericGeneralEventLogSerialNumber = _TnGenericGeneralEventLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6, 1, 1),
    _TnGenericGeneralEventLogSerialNumber_Type()
)
tnGenericGeneralEventLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogSerialNumber.setStatus("current")
_TnGenericGeneralEventLogType_Type = ObjectIdentifier
_TnGenericGeneralEventLogType_Object = MibTableColumn
tnGenericGeneralEventLogType = _TnGenericGeneralEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6, 1, 2),
    _TnGenericGeneralEventLogType_Type()
)
tnGenericGeneralEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogType.setStatus("current")
_TnGenericGeneralEventLogObject_Type = ObjectIdentifier
_TnGenericGeneralEventLogObject_Object = MibTableColumn
tnGenericGeneralEventLogObject = _TnGenericGeneralEventLogObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6, 1, 3),
    _TnGenericGeneralEventLogObject_Type()
)
tnGenericGeneralEventLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogObject.setStatus("current")
_TnGenericGeneralEventLogObjectInstance_Type = SnmpAdminString
_TnGenericGeneralEventLogObjectInstance_Object = MibTableColumn
tnGenericGeneralEventLogObjectInstance = _TnGenericGeneralEventLogObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6, 1, 4),
    _TnGenericGeneralEventLogObjectInstance_Type()
)
tnGenericGeneralEventLogObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogObjectInstance.setStatus("current")
_TnGenericGeneralEventLogTime_Type = Unsigned32
_TnGenericGeneralEventLogTime_Object = MibTableColumn
tnGenericGeneralEventLogTime = _TnGenericGeneralEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6, 1, 5),
    _TnGenericGeneralEventLogTime_Type()
)
tnGenericGeneralEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogTime.setStatus("current")


class _TnGenericGeneralEventLogDescr_Type(SnmpAdminString):
    """Custom type tnGenericGeneralEventLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericGeneralEventLogDescr_Type.__name__ = "SnmpAdminString"
_TnGenericGeneralEventLogDescr_Object = MibTableColumn
tnGenericGeneralEventLogDescr = _TnGenericGeneralEventLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6, 1, 6),
    _TnGenericGeneralEventLogDescr_Type()
)
tnGenericGeneralEventLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogDescr.setStatus("current")


class _TnGenericGeneralEventLogData_Type(SnmpAdminString):
    """Custom type tnGenericGeneralEventLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericGeneralEventLogData_Type.__name__ = "SnmpAdminString"
_TnGenericGeneralEventLogData_Object = MibTableColumn
tnGenericGeneralEventLogData = _TnGenericGeneralEventLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6, 1, 7),
    _TnGenericGeneralEventLogData_Type()
)
tnGenericGeneralEventLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogData.setStatus("current")
_TnGenericGeneralEventLogDateAndTime_Type = DateAndTime
_TnGenericGeneralEventLogDateAndTime_Object = MibTableColumn
tnGenericGeneralEventLogDateAndTime = _TnGenericGeneralEventLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 6, 1, 8),
    _TnGenericGeneralEventLogDateAndTime_Type()
)
tnGenericGeneralEventLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericGeneralEventLogDateAndTime.setStatus("current")
_TnGenericNotAlarmedLogBufferTable_Object = MibTable
tnGenericNotAlarmedLogBufferTable = _TnGenericNotAlarmedLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogBufferTable.setStatus("current")
_TnGenericNotAlarmedLogBufferEntry_Object = MibTableRow
tnGenericNotAlarmedLogBufferEntry = _TnGenericNotAlarmedLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1)
)
tnGenericNotAlarmedLogBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogBufferEntry.setStatus("current")


class _TnGenericNotAlarmedLogSerialNumber_Type(Unsigned32):
    """Custom type tnGenericNotAlarmedLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericNotAlarmedLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericNotAlarmedLogSerialNumber_Object = MibTableColumn
tnGenericNotAlarmedLogSerialNumber = _TnGenericNotAlarmedLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 1),
    _TnGenericNotAlarmedLogSerialNumber_Type()
)
tnGenericNotAlarmedLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogSerialNumber.setStatus("current")
_TnGenericNotAlarmedLogType_Type = ObjectIdentifier
_TnGenericNotAlarmedLogType_Object = MibTableColumn
tnGenericNotAlarmedLogType = _TnGenericNotAlarmedLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 2),
    _TnGenericNotAlarmedLogType_Type()
)
tnGenericNotAlarmedLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogType.setStatus("current")
_TnGenericNotAlarmedLogObject_Type = ObjectIdentifier
_TnGenericNotAlarmedLogObject_Object = MibTableColumn
tnGenericNotAlarmedLogObject = _TnGenericNotAlarmedLogObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 3),
    _TnGenericNotAlarmedLogObject_Type()
)
tnGenericNotAlarmedLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogObject.setStatus("current")
_TnGenericNotAlarmedLogObjectInstance_Type = SnmpAdminString
_TnGenericNotAlarmedLogObjectInstance_Object = MibTableColumn
tnGenericNotAlarmedLogObjectInstance = _TnGenericNotAlarmedLogObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 4),
    _TnGenericNotAlarmedLogObjectInstance_Type()
)
tnGenericNotAlarmedLogObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogObjectInstance.setStatus("current")
_TnGenericNotAlarmedLogTime_Type = Unsigned32
_TnGenericNotAlarmedLogTime_Object = MibTableColumn
tnGenericNotAlarmedLogTime = _TnGenericNotAlarmedLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 5),
    _TnGenericNotAlarmedLogTime_Type()
)
tnGenericNotAlarmedLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogTime.setStatus("current")


class _TnGenericNotAlarmedLogDescr_Type(SnmpAdminString):
    """Custom type tnGenericNotAlarmedLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericNotAlarmedLogDescr_Type.__name__ = "SnmpAdminString"
_TnGenericNotAlarmedLogDescr_Object = MibTableColumn
tnGenericNotAlarmedLogDescr = _TnGenericNotAlarmedLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 6),
    _TnGenericNotAlarmedLogDescr_Type()
)
tnGenericNotAlarmedLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogDescr.setStatus("current")


class _TnGenericNotAlarmedLogData_Type(SnmpAdminString):
    """Custom type tnGenericNotAlarmedLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericNotAlarmedLogData_Type.__name__ = "SnmpAdminString"
_TnGenericNotAlarmedLogData_Object = MibTableColumn
tnGenericNotAlarmedLogData = _TnGenericNotAlarmedLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 7),
    _TnGenericNotAlarmedLogData_Type()
)
tnGenericNotAlarmedLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogData.setStatus("current")
_TnGenericNotAlarmedLogServiceAffecting_Type = TruthValue
_TnGenericNotAlarmedLogServiceAffecting_Object = MibTableColumn
tnGenericNotAlarmedLogServiceAffecting = _TnGenericNotAlarmedLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 8),
    _TnGenericNotAlarmedLogServiceAffecting_Type()
)
tnGenericNotAlarmedLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogServiceAffecting.setStatus("current")
_TnGenericNotAlarmedLogCondition_Type = TnCondition
_TnGenericNotAlarmedLogCondition_Object = MibTableColumn
tnGenericNotAlarmedLogCondition = _TnGenericNotAlarmedLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 9),
    _TnGenericNotAlarmedLogCondition_Type()
)
tnGenericNotAlarmedLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogCondition.setStatus("current")
_TnGenericNotAlarmedLogDateAndTime_Type = DateAndTime
_TnGenericNotAlarmedLogDateAndTime_Object = MibTableColumn
tnGenericNotAlarmedLogDateAndTime = _TnGenericNotAlarmedLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 10),
    _TnGenericNotAlarmedLogDateAndTime_Type()
)
tnGenericNotAlarmedLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogDateAndTime.setStatus("current")
_TnGenericNotAlarmedLogEntityType_Type = TnEntityType
_TnGenericNotAlarmedLogEntityType_Object = MibTableColumn
tnGenericNotAlarmedLogEntityType = _TnGenericNotAlarmedLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 7, 1, 11),
    _TnGenericNotAlarmedLogEntityType_Type()
)
tnGenericNotAlarmedLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericNotAlarmedLogEntityType.setStatus("current")
_TnGenericSecurityLogBufferTable_Object = MibTable
tnGenericSecurityLogBufferTable = _TnGenericSecurityLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnGenericSecurityLogBufferTable.setStatus("current")
_TnGenericSecurityLogBufferEntry_Object = MibTableRow
tnGenericSecurityLogBufferEntry = _TnGenericSecurityLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8, 1)
)
tnGenericSecurityLogBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericSecurityLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericSecurityLogBufferEntry.setStatus("current")


class _TnGenericSecurityLogSerialNumber_Type(Unsigned32):
    """Custom type tnGenericSecurityLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericSecurityLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericSecurityLogSerialNumber_Object = MibTableColumn
tnGenericSecurityLogSerialNumber = _TnGenericSecurityLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8, 1, 1),
    _TnGenericSecurityLogSerialNumber_Type()
)
tnGenericSecurityLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericSecurityLogSerialNumber.setStatus("current")
_TnGenericSecurityLogType_Type = ObjectIdentifier
_TnGenericSecurityLogType_Object = MibTableColumn
tnGenericSecurityLogType = _TnGenericSecurityLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8, 1, 2),
    _TnGenericSecurityLogType_Type()
)
tnGenericSecurityLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericSecurityLogType.setStatus("current")
_TnGenericSecurityLogObject_Type = ObjectIdentifier
_TnGenericSecurityLogObject_Object = MibTableColumn
tnGenericSecurityLogObject = _TnGenericSecurityLogObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8, 1, 3),
    _TnGenericSecurityLogObject_Type()
)
tnGenericSecurityLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericSecurityLogObject.setStatus("current")
_TnGenericSecurityLogObjectInstance_Type = SnmpAdminString
_TnGenericSecurityLogObjectInstance_Object = MibTableColumn
tnGenericSecurityLogObjectInstance = _TnGenericSecurityLogObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8, 1, 4),
    _TnGenericSecurityLogObjectInstance_Type()
)
tnGenericSecurityLogObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericSecurityLogObjectInstance.setStatus("current")
_TnGenericSecurityLogTime_Type = Unsigned32
_TnGenericSecurityLogTime_Object = MibTableColumn
tnGenericSecurityLogTime = _TnGenericSecurityLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8, 1, 5),
    _TnGenericSecurityLogTime_Type()
)
tnGenericSecurityLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericSecurityLogTime.setStatus("current")


class _TnGenericSecurityLogDescr_Type(SnmpAdminString):
    """Custom type tnGenericSecurityLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericSecurityLogDescr_Type.__name__ = "SnmpAdminString"
_TnGenericSecurityLogDescr_Object = MibTableColumn
tnGenericSecurityLogDescr = _TnGenericSecurityLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8, 1, 6),
    _TnGenericSecurityLogDescr_Type()
)
tnGenericSecurityLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericSecurityLogDescr.setStatus("current")


class _TnGenericSecurityLogData_Type(SnmpAdminString):
    """Custom type tnGenericSecurityLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericSecurityLogData_Type.__name__ = "SnmpAdminString"
_TnGenericSecurityLogData_Object = MibTableColumn
tnGenericSecurityLogData = _TnGenericSecurityLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8, 1, 7),
    _TnGenericSecurityLogData_Type()
)
tnGenericSecurityLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericSecurityLogData.setStatus("current")
_TnGenericSecurityLogDateAndTime_Type = DateAndTime
_TnGenericSecurityLogDateAndTime_Object = MibTableColumn
tnGenericSecurityLogDateAndTime = _TnGenericSecurityLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 8, 1, 8),
    _TnGenericSecurityLogDateAndTime_Type()
)
tnGenericSecurityLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericSecurityLogDateAndTime.setStatus("current")
_TnGenericWarningAlarmLogBufferTable_Object = MibTable
tnGenericWarningAlarmLogBufferTable = _TnGenericWarningAlarmLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogBufferTable.setStatus("current")
_TnGenericWarningAlarmLogBufferEntry_Object = MibTableRow
tnGenericWarningAlarmLogBufferEntry = _TnGenericWarningAlarmLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1)
)
tnGenericWarningAlarmLogBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogBufferEntry.setStatus("current")


class _TnGenericWarningAlarmLogSerialNumber_Type(Unsigned32):
    """Custom type tnGenericWarningAlarmLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericWarningAlarmLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGenericWarningAlarmLogSerialNumber_Object = MibTableColumn
tnGenericWarningAlarmLogSerialNumber = _TnGenericWarningAlarmLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 1),
    _TnGenericWarningAlarmLogSerialNumber_Type()
)
tnGenericWarningAlarmLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogSerialNumber.setStatus("current")
_TnGenericWarningAlarmLogType_Type = ObjectIdentifier
_TnGenericWarningAlarmLogType_Object = MibTableColumn
tnGenericWarningAlarmLogType = _TnGenericWarningAlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 2),
    _TnGenericWarningAlarmLogType_Type()
)
tnGenericWarningAlarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogType.setStatus("current")
_TnGenericWarningAlarmLogObject_Type = ObjectIdentifier
_TnGenericWarningAlarmLogObject_Object = MibTableColumn
tnGenericWarningAlarmLogObject = _TnGenericWarningAlarmLogObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 3),
    _TnGenericWarningAlarmLogObject_Type()
)
tnGenericWarningAlarmLogObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogObject.setStatus("current")
_TnGenericWarningAlarmLogObjectInstance_Type = SnmpAdminString
_TnGenericWarningAlarmLogObjectInstance_Object = MibTableColumn
tnGenericWarningAlarmLogObjectInstance = _TnGenericWarningAlarmLogObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 4),
    _TnGenericWarningAlarmLogObjectInstance_Type()
)
tnGenericWarningAlarmLogObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogObjectInstance.setStatus("current")
_TnGenericWarningAlarmLogTime_Type = Unsigned32
_TnGenericWarningAlarmLogTime_Object = MibTableColumn
tnGenericWarningAlarmLogTime = _TnGenericWarningAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 5),
    _TnGenericWarningAlarmLogTime_Type()
)
tnGenericWarningAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogTime.setStatus("current")


class _TnGenericWarningAlarmLogDescr_Type(SnmpAdminString):
    """Custom type tnGenericWarningAlarmLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericWarningAlarmLogDescr_Type.__name__ = "SnmpAdminString"
_TnGenericWarningAlarmLogDescr_Object = MibTableColumn
tnGenericWarningAlarmLogDescr = _TnGenericWarningAlarmLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 6),
    _TnGenericWarningAlarmLogDescr_Type()
)
tnGenericWarningAlarmLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogDescr.setStatus("current")


class _TnGenericWarningAlarmLogData_Type(SnmpAdminString):
    """Custom type tnGenericWarningAlarmLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericWarningAlarmLogData_Type.__name__ = "SnmpAdminString"
_TnGenericWarningAlarmLogData_Object = MibTableColumn
tnGenericWarningAlarmLogData = _TnGenericWarningAlarmLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 7),
    _TnGenericWarningAlarmLogData_Type()
)
tnGenericWarningAlarmLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogData.setStatus("current")
_TnGenericWarningAlarmLogServiceAffecting_Type = TruthValue
_TnGenericWarningAlarmLogServiceAffecting_Object = MibTableColumn
tnGenericWarningAlarmLogServiceAffecting = _TnGenericWarningAlarmLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 8),
    _TnGenericWarningAlarmLogServiceAffecting_Type()
)
tnGenericWarningAlarmLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogServiceAffecting.setStatus("current")
_TnGenericWarningAlarmLogCondition_Type = TnCondition
_TnGenericWarningAlarmLogCondition_Object = MibTableColumn
tnGenericWarningAlarmLogCondition = _TnGenericWarningAlarmLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 9),
    _TnGenericWarningAlarmLogCondition_Type()
)
tnGenericWarningAlarmLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogCondition.setStatus("current")
_TnGenericWarningAlarmLogDateAndTime_Type = DateAndTime
_TnGenericWarningAlarmLogDateAndTime_Object = MibTableColumn
tnGenericWarningAlarmLogDateAndTime = _TnGenericWarningAlarmLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 10),
    _TnGenericWarningAlarmLogDateAndTime_Type()
)
tnGenericWarningAlarmLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogDateAndTime.setStatus("current")
_TnGenericWarningAlarmLogEntityType_Type = TnEntityType
_TnGenericWarningAlarmLogEntityType_Object = MibTableColumn
tnGenericWarningAlarmLogEntityType = _TnGenericWarningAlarmLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 1, 9, 1, 11),
    _TnGenericWarningAlarmLogEntityType_Type()
)
tnGenericWarningAlarmLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericWarningAlarmLogEntityType.setStatus("current")
_TnGenericLogConformance_ObjectIdentity = ObjectIdentity
tnGenericLogConformance = _TnGenericLogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2)
)
_TnGenericLogCompliances_ObjectIdentity = ObjectIdentity
tnGenericLogCompliances = _TnGenericLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 1)
)
_TnGenericLogGroups_ObjectIdentity = ObjectIdentity
tnGenericLogGroups = _TnGenericLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2)
)

# Managed Objects groups

tnGenericActiveAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 2, 2, 1)
)
tnGenericActiveAlarmGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmCategory"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmDescr"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmData"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmServiceAffecting"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmCondition"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmDateAndTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericActiveAlarmGroup.setStatus("current")

tnGenericCriticalAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 1)
)
tnGenericCriticalAlarmGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogDescr"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogData"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogServiceAffecting"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogCondition"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogDateAndTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmLogEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCriticalAlarmGroup.setStatus("current")

tnGenericMajorAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 2)
)
tnGenericMajorAlarmGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogDescr"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogData"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogServiceAffecting"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogCondition"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogDateAndTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmLogEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMajorAlarmGroup.setStatus("current")

tnGenericMinorAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 3)
)
tnGenericMinorAlarmGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogDescr"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogData"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogServiceAffecting"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogCondition"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogDateAndTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmLogEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMinorAlarmGroup.setStatus("current")

tnGenericStateChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 4)
)
tnGenericStateChangeGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectValueType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectCounter32Val"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectUnsigned32Val"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectTimeTicksVal"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectInteger32Val"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectOctetStringVal"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectIpAddressVal"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectOidVal"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogObjectCounter64Val"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeLogDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericStateChangeGroup.setStatus("current")

tnGenericUserActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 5)
)
tnGenericUserActionGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectValueType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectCounter32Val"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectUnsigned32Val"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectTimeTicksVal"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectInteger32Val"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectOctetStringVal"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectIpAddressVal"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectOidVal"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogObjectCounter64Val"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogDateAndTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericUserActionGroup.setStatus("current")

tnGenericGeneralEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 6)
)
tnGenericGeneralEventGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericGeneralEventLogType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericGeneralEventLogObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericGeneralEventLogObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericGeneralEventLogTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericGeneralEventLogDescr"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericGeneralEventLogData"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericGeneralEventLogDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericGeneralEventGroup.setStatus("current")

tnGenericNotAlarmedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 7)
)
tnGenericNotAlarmedGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogDescr"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogData"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogServiceAffecting"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogCondition"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogDateAndTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedLogEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericNotAlarmedGroup.setStatus("current")

tnGenericSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 8)
)
tnGenericSecurityGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericSecurityLogType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericSecurityLogObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericSecurityLogObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericSecurityLogTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericSecurityLogDescr"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericSecurityLogData"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericSecurityLogDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityGroup.setStatus("current")

tnGenericWarningAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 9)
)
tnGenericWarningAlarmGroup.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogType"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogObject"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogObjectInstance"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogDescr"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogData"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogServiceAffecting"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogCondition"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogDateAndTime"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmLogEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericWarningAlarmGroup.setStatus("current")

tnGenericUserActionGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 2, 10)
)
tnGenericUserActionGroup2.setObjects(
    ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionLogUserID")
)
if mibBuilder.loadTexts:
    tnGenericUserActionGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnGenericActiveAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 1, 2, 1, 1)
)
tnGenericActiveAlarmCompliance.setObjects(
    ("TROPIC-GENERIC-LOG-MIB", "tnGenericActiveAlarmGroup")
)
if mibBuilder.loadTexts:
    tnGenericActiveAlarmCompliance.setStatus(
        "current"
    )

tnGenericLogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13, 2, 2, 1, 1)
)
tnGenericLogCompliance.setObjects(
      *(("TROPIC-GENERIC-LOG-MIB", "tnGenericCriticalAlarmGroup"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMajorAlarmGroup"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericMinorAlarmGroup"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericStateChangeGroup"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionGroup"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericUserActionGroup2"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericGeneralEventGroup"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericNotAlarmedGroup"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericSecurityGroup"),
        ("TROPIC-GENERIC-LOG-MIB", "tnGenericWarningAlarmGroup"))
)
if mibBuilder.loadTexts:
    tnGenericLogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-GENERIC-LOG-MIB",
    **{"tnGenericLogMibModule": tnGenericLogMibModule,
       "tnGenericActiveAlarm": tnGenericActiveAlarm,
       "tnGenericActiveAlarmObjects": tnGenericActiveAlarmObjects,
       "tnGenericActiveAlarmTable": tnGenericActiveAlarmTable,
       "tnGenericActiveAlarmEntry": tnGenericActiveAlarmEntry,
       "tnGenericActiveAlarmSerialNumber": tnGenericActiveAlarmSerialNumber,
       "tnGenericActiveAlarmType": tnGenericActiveAlarmType,
       "tnGenericActiveAlarmObject": tnGenericActiveAlarmObject,
       "tnGenericActiveAlarmObjectInstance": tnGenericActiveAlarmObjectInstance,
       "tnGenericActiveAlarmTime": tnGenericActiveAlarmTime,
       "tnGenericActiveAlarmCategory": tnGenericActiveAlarmCategory,
       "tnGenericActiveAlarmDescr": tnGenericActiveAlarmDescr,
       "tnGenericActiveAlarmData": tnGenericActiveAlarmData,
       "tnGenericActiveAlarmServiceAffecting": tnGenericActiveAlarmServiceAffecting,
       "tnGenericActiveAlarmCondition": tnGenericActiveAlarmCondition,
       "tnGenericActiveAlarmDateAndTime": tnGenericActiveAlarmDateAndTime,
       "tnGenericActiveAlarmEntityType": tnGenericActiveAlarmEntityType,
       "tnGenericActiveAlarmConformance": tnGenericActiveAlarmConformance,
       "tnGenericActiveAlarmCompliances": tnGenericActiveAlarmCompliances,
       "tnGenericActiveAlarmCompliance": tnGenericActiveAlarmCompliance,
       "tnGenericActiveAlarmGroups": tnGenericActiveAlarmGroups,
       "tnGenericActiveAlarmGroup": tnGenericActiveAlarmGroup,
       "tnGenericLog": tnGenericLog,
       "tnGenericLogObjects": tnGenericLogObjects,
       "tnGenericCriticalAlarmLogBufferTable": tnGenericCriticalAlarmLogBufferTable,
       "tnGenericCriticalAlarmLogBufferEntry": tnGenericCriticalAlarmLogBufferEntry,
       "tnGenericCriticalAlarmLogSerialNumber": tnGenericCriticalAlarmLogSerialNumber,
       "tnGenericCriticalAlarmLogType": tnGenericCriticalAlarmLogType,
       "tnGenericCriticalAlarmLogObject": tnGenericCriticalAlarmLogObject,
       "tnGenericCriticalAlarmLogObjectInstance": tnGenericCriticalAlarmLogObjectInstance,
       "tnGenericCriticalAlarmLogTime": tnGenericCriticalAlarmLogTime,
       "tnGenericCriticalAlarmLogDescr": tnGenericCriticalAlarmLogDescr,
       "tnGenericCriticalAlarmLogData": tnGenericCriticalAlarmLogData,
       "tnGenericCriticalAlarmLogServiceAffecting": tnGenericCriticalAlarmLogServiceAffecting,
       "tnGenericCriticalAlarmLogCondition": tnGenericCriticalAlarmLogCondition,
       "tnGenericCriticalAlarmLogDateAndTime": tnGenericCriticalAlarmLogDateAndTime,
       "tnGenericCriticalAlarmLogEntityType": tnGenericCriticalAlarmLogEntityType,
       "tnGenericMajorAlarmLogBufferTable": tnGenericMajorAlarmLogBufferTable,
       "tnGenericMajorAlarmLogBufferEntry": tnGenericMajorAlarmLogBufferEntry,
       "tnGenericMajorAlarmLogSerialNumber": tnGenericMajorAlarmLogSerialNumber,
       "tnGenericMajorAlarmLogType": tnGenericMajorAlarmLogType,
       "tnGenericMajorAlarmLogObject": tnGenericMajorAlarmLogObject,
       "tnGenericMajorAlarmLogObjectInstance": tnGenericMajorAlarmLogObjectInstance,
       "tnGenericMajorAlarmLogTime": tnGenericMajorAlarmLogTime,
       "tnGenericMajorAlarmLogDescr": tnGenericMajorAlarmLogDescr,
       "tnGenericMajorAlarmLogData": tnGenericMajorAlarmLogData,
       "tnGenericMajorAlarmLogServiceAffecting": tnGenericMajorAlarmLogServiceAffecting,
       "tnGenericMajorAlarmLogCondition": tnGenericMajorAlarmLogCondition,
       "tnGenericMajorAlarmLogDateAndTime": tnGenericMajorAlarmLogDateAndTime,
       "tnGenericMajorAlarmLogEntityType": tnGenericMajorAlarmLogEntityType,
       "tnGenericMinorAlarmLogBufferTable": tnGenericMinorAlarmLogBufferTable,
       "tnGenericMinorAlarmLogBufferEntry": tnGenericMinorAlarmLogBufferEntry,
       "tnGenericMinorAlarmLogSerialNumber": tnGenericMinorAlarmLogSerialNumber,
       "tnGenericMinorAlarmLogType": tnGenericMinorAlarmLogType,
       "tnGenericMinorAlarmLogObject": tnGenericMinorAlarmLogObject,
       "tnGenericMinorAlarmLogObjectInstance": tnGenericMinorAlarmLogObjectInstance,
       "tnGenericMinorAlarmLogTime": tnGenericMinorAlarmLogTime,
       "tnGenericMinorAlarmLogDescr": tnGenericMinorAlarmLogDescr,
       "tnGenericMinorAlarmLogData": tnGenericMinorAlarmLogData,
       "tnGenericMinorAlarmLogServiceAffecting": tnGenericMinorAlarmLogServiceAffecting,
       "tnGenericMinorAlarmLogCondition": tnGenericMinorAlarmLogCondition,
       "tnGenericMinorAlarmLogDateAndTime": tnGenericMinorAlarmLogDateAndTime,
       "tnGenericMinorAlarmLogEntityType": tnGenericMinorAlarmLogEntityType,
       "tnGenericStateChangeLogBufferTable": tnGenericStateChangeLogBufferTable,
       "tnGenericStateChangeLogBufferEntry": tnGenericStateChangeLogBufferEntry,
       "tnGenericStateChangeLogSerialNumber": tnGenericStateChangeLogSerialNumber,
       "tnGenericStateChangeLogType": tnGenericStateChangeLogType,
       "tnGenericStateChangeLogObject": tnGenericStateChangeLogObject,
       "tnGenericStateChangeLogObjectInstance": tnGenericStateChangeLogObjectInstance,
       "tnGenericStateChangeLogTime": tnGenericStateChangeLogTime,
       "tnGenericStateChangeLogObjectValueType": tnGenericStateChangeLogObjectValueType,
       "tnGenericStateChangeLogObjectCounter32Val": tnGenericStateChangeLogObjectCounter32Val,
       "tnGenericStateChangeLogObjectUnsigned32Val": tnGenericStateChangeLogObjectUnsigned32Val,
       "tnGenericStateChangeLogObjectTimeTicksVal": tnGenericStateChangeLogObjectTimeTicksVal,
       "tnGenericStateChangeLogObjectInteger32Val": tnGenericStateChangeLogObjectInteger32Val,
       "tnGenericStateChangeLogObjectOctetStringVal": tnGenericStateChangeLogObjectOctetStringVal,
       "tnGenericStateChangeLogObjectIpAddressVal": tnGenericStateChangeLogObjectIpAddressVal,
       "tnGenericStateChangeLogObjectOidVal": tnGenericStateChangeLogObjectOidVal,
       "tnGenericStateChangeLogObjectCounter64Val": tnGenericStateChangeLogObjectCounter64Val,
       "tnGenericStateChangeLogDateAndTime": tnGenericStateChangeLogDateAndTime,
       "tnGenericUserActionLogBufferTable": tnGenericUserActionLogBufferTable,
       "tnGenericUserActionLogBufferEntry": tnGenericUserActionLogBufferEntry,
       "tnGenericUserActionLogSerialNumber": tnGenericUserActionLogSerialNumber,
       "tnGenericUserActionLogType": tnGenericUserActionLogType,
       "tnGenericUserActionLogObject": tnGenericUserActionLogObject,
       "tnGenericUserActionLogObjectInstance": tnGenericUserActionLogObjectInstance,
       "tnGenericUserActionLogTime": tnGenericUserActionLogTime,
       "tnGenericUserActionLogObjectValueType": tnGenericUserActionLogObjectValueType,
       "tnGenericUserActionLogObjectCounter32Val": tnGenericUserActionLogObjectCounter32Val,
       "tnGenericUserActionLogObjectUnsigned32Val": tnGenericUserActionLogObjectUnsigned32Val,
       "tnGenericUserActionLogObjectTimeTicksVal": tnGenericUserActionLogObjectTimeTicksVal,
       "tnGenericUserActionLogObjectInteger32Val": tnGenericUserActionLogObjectInteger32Val,
       "tnGenericUserActionLogObjectOctetStringVal": tnGenericUserActionLogObjectOctetStringVal,
       "tnGenericUserActionLogObjectIpAddressVal": tnGenericUserActionLogObjectIpAddressVal,
       "tnGenericUserActionLogObjectOidVal": tnGenericUserActionLogObjectOidVal,
       "tnGenericUserActionLogObjectCounter64Val": tnGenericUserActionLogObjectCounter64Val,
       "tnGenericUserActionLogDateAndTime": tnGenericUserActionLogDateAndTime,
       "tnGenericUserActionLogConfigurationChangeCounter": tnGenericUserActionLogConfigurationChangeCounter,
       "tnGenericUserActionLogUserID": tnGenericUserActionLogUserID,
       "tnGenericGeneralEventLogBufferTable": tnGenericGeneralEventLogBufferTable,
       "tnGenericGeneralEventLogBufferEntry": tnGenericGeneralEventLogBufferEntry,
       "tnGenericGeneralEventLogSerialNumber": tnGenericGeneralEventLogSerialNumber,
       "tnGenericGeneralEventLogType": tnGenericGeneralEventLogType,
       "tnGenericGeneralEventLogObject": tnGenericGeneralEventLogObject,
       "tnGenericGeneralEventLogObjectInstance": tnGenericGeneralEventLogObjectInstance,
       "tnGenericGeneralEventLogTime": tnGenericGeneralEventLogTime,
       "tnGenericGeneralEventLogDescr": tnGenericGeneralEventLogDescr,
       "tnGenericGeneralEventLogData": tnGenericGeneralEventLogData,
       "tnGenericGeneralEventLogDateAndTime": tnGenericGeneralEventLogDateAndTime,
       "tnGenericNotAlarmedLogBufferTable": tnGenericNotAlarmedLogBufferTable,
       "tnGenericNotAlarmedLogBufferEntry": tnGenericNotAlarmedLogBufferEntry,
       "tnGenericNotAlarmedLogSerialNumber": tnGenericNotAlarmedLogSerialNumber,
       "tnGenericNotAlarmedLogType": tnGenericNotAlarmedLogType,
       "tnGenericNotAlarmedLogObject": tnGenericNotAlarmedLogObject,
       "tnGenericNotAlarmedLogObjectInstance": tnGenericNotAlarmedLogObjectInstance,
       "tnGenericNotAlarmedLogTime": tnGenericNotAlarmedLogTime,
       "tnGenericNotAlarmedLogDescr": tnGenericNotAlarmedLogDescr,
       "tnGenericNotAlarmedLogData": tnGenericNotAlarmedLogData,
       "tnGenericNotAlarmedLogServiceAffecting": tnGenericNotAlarmedLogServiceAffecting,
       "tnGenericNotAlarmedLogCondition": tnGenericNotAlarmedLogCondition,
       "tnGenericNotAlarmedLogDateAndTime": tnGenericNotAlarmedLogDateAndTime,
       "tnGenericNotAlarmedLogEntityType": tnGenericNotAlarmedLogEntityType,
       "tnGenericSecurityLogBufferTable": tnGenericSecurityLogBufferTable,
       "tnGenericSecurityLogBufferEntry": tnGenericSecurityLogBufferEntry,
       "tnGenericSecurityLogSerialNumber": tnGenericSecurityLogSerialNumber,
       "tnGenericSecurityLogType": tnGenericSecurityLogType,
       "tnGenericSecurityLogObject": tnGenericSecurityLogObject,
       "tnGenericSecurityLogObjectInstance": tnGenericSecurityLogObjectInstance,
       "tnGenericSecurityLogTime": tnGenericSecurityLogTime,
       "tnGenericSecurityLogDescr": tnGenericSecurityLogDescr,
       "tnGenericSecurityLogData": tnGenericSecurityLogData,
       "tnGenericSecurityLogDateAndTime": tnGenericSecurityLogDateAndTime,
       "tnGenericWarningAlarmLogBufferTable": tnGenericWarningAlarmLogBufferTable,
       "tnGenericWarningAlarmLogBufferEntry": tnGenericWarningAlarmLogBufferEntry,
       "tnGenericWarningAlarmLogSerialNumber": tnGenericWarningAlarmLogSerialNumber,
       "tnGenericWarningAlarmLogType": tnGenericWarningAlarmLogType,
       "tnGenericWarningAlarmLogObject": tnGenericWarningAlarmLogObject,
       "tnGenericWarningAlarmLogObjectInstance": tnGenericWarningAlarmLogObjectInstance,
       "tnGenericWarningAlarmLogTime": tnGenericWarningAlarmLogTime,
       "tnGenericWarningAlarmLogDescr": tnGenericWarningAlarmLogDescr,
       "tnGenericWarningAlarmLogData": tnGenericWarningAlarmLogData,
       "tnGenericWarningAlarmLogServiceAffecting": tnGenericWarningAlarmLogServiceAffecting,
       "tnGenericWarningAlarmLogCondition": tnGenericWarningAlarmLogCondition,
       "tnGenericWarningAlarmLogDateAndTime": tnGenericWarningAlarmLogDateAndTime,
       "tnGenericWarningAlarmLogEntityType": tnGenericWarningAlarmLogEntityType,
       "tnGenericLogConformance": tnGenericLogConformance,
       "tnGenericLogCompliances": tnGenericLogCompliances,
       "tnGenericLogCompliance": tnGenericLogCompliance,
       "tnGenericLogGroups": tnGenericLogGroups,
       "tnGenericCriticalAlarmGroup": tnGenericCriticalAlarmGroup,
       "tnGenericMajorAlarmGroup": tnGenericMajorAlarmGroup,
       "tnGenericMinorAlarmGroup": tnGenericMinorAlarmGroup,
       "tnGenericStateChangeGroup": tnGenericStateChangeGroup,
       "tnGenericUserActionGroup": tnGenericUserActionGroup,
       "tnGenericGeneralEventGroup": tnGenericGeneralEventGroup,
       "tnGenericNotAlarmedGroup": tnGenericNotAlarmedGroup,
       "tnGenericSecurityGroup": tnGenericSecurityGroup,
       "tnGenericWarningAlarmGroup": tnGenericWarningAlarmGroup,
       "tnGenericUserActionGroup2": tnGenericUserActionGroup2}
)
