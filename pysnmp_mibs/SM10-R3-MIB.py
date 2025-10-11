# SNMP MIB module (SM10-R3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netapp/SM10-R3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:07:34 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sm10R3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500)
)
if mibBuilder.loadTexts:
    sm10R3.setRevisions(
        ("2011-08-05 15:03",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netapp_ObjectIdentity = ObjectIdentity
netapp = _Netapp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789)
)
_ESeriesStorageSystem_ObjectIdentity = ObjectIdentity
eSeriesStorageSystem = _ESeriesStorageSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1123)
)
_StorageManager_ObjectIdentity = ObjectIdentity
storageManager = _StorageManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1)
)
_SmConformance_ObjectIdentity = ObjectIdentity
smConformance = _SmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 8)
)
_SmCompliance_ObjectIdentity = ObjectIdentity
smCompliance = _SmCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 8, 1)
)
_SmGroups_ObjectIdentity = ObjectIdentity
smGroups = _SmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 8, 2)
)
_Sm10R3TrapBase_ObjectIdentity = ObjectIdentity
sm10R3TrapBase = _Sm10R3TrapBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 0)
)
_InfoTable_Object = MibTable
infoTable = _InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1)
)
if mibBuilder.loadTexts:
    infoTable.setStatus("current")
_InfoEntry_Object = MibTableRow
infoEntry = _InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1)
)
infoEntry.setIndexNames(
    (0, "SM10-R3-MIB", "deviceHostIPType"),
)
if mibBuilder.loadTexts:
    infoEntry.setStatus("current")
_DeviceHostIPType_Type = InetAddressType
_DeviceHostIPType_Object = MibTableColumn
deviceHostIPType = _DeviceHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1, 1),
    _DeviceHostIPType_Type()
)
deviceHostIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHostIPType.setStatus("current")
_DeviceHostIPAddr_Type = InetAddress
_DeviceHostIPAddr_Object = MibTableColumn
deviceHostIPAddr = _DeviceHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1, 2),
    _DeviceHostIPAddr_Type()
)
deviceHostIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHostIPAddr.setStatus("current")


class _DeviceHostName_Type(DisplayString):
    """Custom type deviceHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_DeviceHostName_Type.__name__ = "DisplayString"
_DeviceHostName_Object = MibTableColumn
deviceHostName = _DeviceHostName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1, 3),
    _DeviceHostName_Type()
)
deviceHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHostName.setStatus("current")


class _DeviceUserLabel_Type(DisplayString):
    """Custom type deviceUserLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DeviceUserLabel_Type.__name__ = "DisplayString"
_DeviceUserLabel_Object = MibTableColumn
deviceUserLabel = _DeviceUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1, 4),
    _DeviceUserLabel_Type()
)
deviceUserLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUserLabel.setStatus("current")


class _DeviceErrorCode_Type(DisplayString):
    """Custom type deviceErrorCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_DeviceErrorCode_Type.__name__ = "DisplayString"
_DeviceErrorCode_Object = MibTableColumn
deviceErrorCode = _DeviceErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1, 5),
    _DeviceErrorCode_Type()
)
deviceErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceErrorCode.setStatus("current")


class _EventTime_Type(DisplayString):
    """Custom type eventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_EventTime_Type.__name__ = "DisplayString"
_EventTime_Object = MibTableColumn
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1, 6),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 69),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibTableColumn
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1, 7),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("current")


class _ComponentType_Type(DisplayString):
    """Custom type componentType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_ComponentType_Type.__name__ = "DisplayString"
_ComponentType_Object = MibTableColumn
componentType = _ComponentType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1, 8),
    _ComponentType_Type()
)
componentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentType.setStatus("current")


class _ComponentLocation_Type(DisplayString):
    """Custom type componentLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_ComponentLocation_Type.__name__ = "DisplayString"
_ComponentLocation_Object = MibTableColumn
componentLocation = _ComponentLocation_Object(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 1, 1, 9),
    _ComponentLocation_Type()
)
componentLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLocation.setStatus("current")
_StorageServer_ObjectIdentity = ObjectIdentity
storageServer = _StorageServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1123, 2)
)

# Managed Objects groups

smObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 8, 2, 1)
)
smObjectGroup.setObjects(
      *(("SM10-R3-MIB", "deviceHostIPType"),
        ("SM10-R3-MIB", "deviceHostIPAddr"),
        ("SM10-R3-MIB", "deviceHostName"),
        ("SM10-R3-MIB", "deviceUserLabel"),
        ("SM10-R3-MIB", "deviceErrorCode"),
        ("SM10-R3-MIB", "eventTime"),
        ("SM10-R3-MIB", "trapDescription"),
        ("SM10-R3-MIB", "componentType"),
        ("SM10-R3-MIB", "componentLocation"))
)
if mibBuilder.loadTexts:
    smObjectGroup.setStatus("current")


# Notification objects

storageArrayCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 500, 0, 2)
)
storageArrayCritical.setObjects(
      *(("SM10-R3-MIB", "deviceHostIPType"),
        ("SM10-R3-MIB", "deviceHostIPAddr"),
        ("SM10-R3-MIB", "deviceHostName"),
        ("SM10-R3-MIB", "deviceUserLabel"),
        ("SM10-R3-MIB", "deviceErrorCode"),
        ("SM10-R3-MIB", "eventTime"),
        ("SM10-R3-MIB", "trapDescription"),
        ("SM10-R3-MIB", "componentType"),
        ("SM10-R3-MIB", "componentLocation"))
)
if mibBuilder.loadTexts:
    storageArrayCritical.setStatus(
        "current"
    )


# Notifications groups

smNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 8, 2, 2)
)
smNotificationGroup.setObjects(
    ("SM10-R3-MIB", "storageArrayCritical")
)
if mibBuilder.loadTexts:
    smNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

smGrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 789, 1123, 1, 8, 1, 1)
)
smGrpCompliance.setObjects(
      *(("SM10-R3-MIB", "smObjectGroup"),
        ("SM10-R3-MIB", "smNotificationGroup"))
)
if mibBuilder.loadTexts:
    smGrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SM10-R3-MIB",
    **{"netapp": netapp,
       "eSeriesStorageSystem": eSeriesStorageSystem,
       "storageManager": storageManager,
       "smConformance": smConformance,
       "smCompliance": smCompliance,
       "smGrpCompliance": smGrpCompliance,
       "smGroups": smGroups,
       "smObjectGroup": smObjectGroup,
       "smNotificationGroup": smNotificationGroup,
       "sm10R3": sm10R3,
       "sm10R3TrapBase": sm10R3TrapBase,
       "storageArrayCritical": storageArrayCritical,
       "infoTable": infoTable,
       "infoEntry": infoEntry,
       "deviceHostIPType": deviceHostIPType,
       "deviceHostIPAddr": deviceHostIPAddr,
       "deviceHostName": deviceHostName,
       "deviceUserLabel": deviceUserLabel,
       "deviceErrorCode": deviceErrorCode,
       "eventTime": eventTime,
       "trapDescription": trapDescription,
       "componentType": componentType,
       "componentLocation": componentLocation,
       "storageServer": storageServer}
)
