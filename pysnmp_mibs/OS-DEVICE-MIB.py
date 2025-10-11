# SNMP MIB module (OS-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-DEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:08 2025
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

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

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

osDevice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40)
)
if mibBuilder.loadTexts:
    osDevice.setRevisions(
        ("2019-04-04 00:00",
         "2016-09-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DevModuleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("lte0", 2),
          ("vdsl0", 3))
    )



class SerialBaudRate(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(115200, 115200),
    )



# MIB Managed Objects in the order of their OIDs

_OsDevNotifications_ObjectIdentity = ObjectIdentity
osDevNotifications = _OsDevNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 0)
)
_OsDevModule_ObjectIdentity = ObjectIdentity
osDevModule = _OsDevModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 1)
)
_OsDevModuleType_Type = DevModuleType
_OsDevModuleType_Object = MibScalar
osDevModuleType = _OsDevModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 1, 1),
    _OsDevModuleType_Type()
)
osDevModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osDevModuleType.setStatus("current")


class _OsDevModuleSlotNumber_Type(Integer32):
    """Custom type osDevModuleSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_OsDevModuleSlotNumber_Type.__name__ = "Integer32"
_OsDevModuleSlotNumber_Object = MibScalar
osDevModuleSlotNumber = _OsDevModuleSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 1, 2),
    _OsDevModuleSlotNumber_Type()
)
osDevModuleSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osDevModuleSlotNumber.setStatus("current")
_OsDevParams_ObjectIdentity = ObjectIdentity
osDevParams = _OsDevParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 2)
)
_OsDevSerial_ObjectIdentity = ObjectIdentity
osDevSerial = _OsDevSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1)
)
_OsDevSerialNumber_Type = Integer32
_OsDevSerialNumber_Object = MibScalar
osDevSerialNumber = _OsDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 1),
    _OsDevSerialNumber_Type()
)
osDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osDevSerialNumber.setStatus("current")
_OsDevSerialTable_Object = MibTable
osDevSerialTable = _OsDevSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2)
)
if mibBuilder.loadTexts:
    osDevSerialTable.setStatus("current")
_OsDevSerialEntry_Object = MibTableRow
osDevSerialEntry = _OsDevSerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2, 1)
)
osDevSerialEntry.setIndexNames(
    (0, "OS-DEVICE-MIB", "osDevSerialIndex"),
)
if mibBuilder.loadTexts:
    osDevSerialEntry.setStatus("current")
_OsDevSerialIndex_Type = Unsigned32
_OsDevSerialIndex_Object = MibTableColumn
osDevSerialIndex = _OsDevSerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2, 1, 1),
    _OsDevSerialIndex_Type()
)
osDevSerialIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osDevSerialIndex.setStatus("current")
_OsDevSerialOperBaudrate_Type = SerialBaudRate
_OsDevSerialOperBaudrate_Object = MibTableColumn
osDevSerialOperBaudrate = _OsDevSerialOperBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2, 1, 2),
    _OsDevSerialOperBaudrate_Type()
)
osDevSerialOperBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osDevSerialOperBaudrate.setStatus("current")
_OsDevSerialAdminBaudrate_Type = SerialBaudRate
_OsDevSerialAdminBaudrate_Object = MibTableColumn
osDevSerialAdminBaudrate = _OsDevSerialAdminBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2, 1, 3),
    _OsDevSerialAdminBaudrate_Type()
)
osDevSerialAdminBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osDevSerialAdminBaudrate.setStatus("current")
_OsDevConformance_ObjectIdentity = ObjectIdentity
osDevConformance = _OsDevConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 101)
)
_OsDevMIBCompliances_ObjectIdentity = ObjectIdentity
osDevMIBCompliances = _OsDevMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 1)
)
_OsDevMIBGroups_ObjectIdentity = ObjectIdentity
osDevMIBGroups = _OsDevMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 2)
)

# Managed Objects groups

osDevMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 2, 1)
)
osDevMandatoryGroup.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleSlotNumber"),
        ("OS-DEVICE-MIB", "osDevModuleType"),
        ("OS-DEVICE-MIB", "osDevSerialNumber"),
        ("OS-DEVICE-MIB", "osDevSerialOperBaudrate"),
        ("OS-DEVICE-MIB", "osDevSerialAdminBaudrate"))
)
if mibBuilder.loadTexts:
    osDevMandatoryGroup.setStatus("current")


# Notification objects

osDevModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 1)
)
osDevModuleInserted.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleSlotNumber"),
        ("OS-DEVICE-MIB", "osDevModuleType"))
)
if mibBuilder.loadTexts:
    osDevModuleInserted.setStatus(
        "current"
    )

osDevModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 2)
)
osDevModuleRemoved.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleSlotNumber"),
        ("OS-DEVICE-MIB", "osDevModuleType"))
)
if mibBuilder.loadTexts:
    osDevModuleRemoved.setStatus(
        "current"
    )

osDevModuleLedPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 3)
)
osDevModuleLedPowerOn.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleSlotNumber"),
        ("OS-DEVICE-MIB", "osDevModuleType"))
)
if mibBuilder.loadTexts:
    osDevModuleLedPowerOn.setStatus(
        "current"
    )

osDevModuleLedPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 4)
)
osDevModuleLedPowerOff.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleSlotNumber"),
        ("OS-DEVICE-MIB", "osDevModuleType"))
)
if mibBuilder.loadTexts:
    osDevModuleLedPowerOff.setStatus(
        "current"
    )

osDevModuleLedWanOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 5)
)
osDevModuleLedWanOn.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleSlotNumber"),
        ("OS-DEVICE-MIB", "osDevModuleType"))
)
if mibBuilder.loadTexts:
    osDevModuleLedWanOn.setStatus(
        "current"
    )

osDevModuleLedWanOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 6)
)
osDevModuleLedWanOff.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleSlotNumber"),
        ("OS-DEVICE-MIB", "osDevModuleType"))
)
if mibBuilder.loadTexts:
    osDevModuleLedWanOff.setStatus(
        "current"
    )

osDevModuleLedConnOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 7)
)
osDevModuleLedConnOn.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleSlotNumber"),
        ("OS-DEVICE-MIB", "osDevModuleType"))
)
if mibBuilder.loadTexts:
    osDevModuleLedConnOn.setStatus(
        "current"
    )

osDevModuleLedConnOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 8)
)
osDevModuleLedConnOff.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleSlotNumber"),
        ("OS-DEVICE-MIB", "osDevModuleType"))
)
if mibBuilder.loadTexts:
    osDevModuleLedConnOff.setStatus(
        "current"
    )


# Notifications groups

osDevNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 2, 2)
)
osDevNotificationsGroup.setObjects(
      *(("OS-DEVICE-MIB", "osDevModuleInserted"),
        ("OS-DEVICE-MIB", "osDevModuleRemoved"),
        ("OS-DEVICE-MIB", "osDevModuleLedPowerOn"),
        ("OS-DEVICE-MIB", "osDevModuleLedPowerOff"),
        ("OS-DEVICE-MIB", "osDevModuleLedWanOn"),
        ("OS-DEVICE-MIB", "osDevModuleLedWanOff"),
        ("OS-DEVICE-MIB", "osDevModuleLedConnOn"),
        ("OS-DEVICE-MIB", "osDevModuleLedConnOff"))
)
if mibBuilder.loadTexts:
    osDevNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

osDevMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 1, 1)
)
osDevMIBCompliance.setObjects(
      *(("OS-DEVICE-MIB", "osDevMandatoryGroup"),
        ("OS-DEVICE-MIB", "osDevNotificationsGroup"))
)
if mibBuilder.loadTexts:
    osDevMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-DEVICE-MIB",
    **{"DevModuleType": DevModuleType,
       "SerialBaudRate": SerialBaudRate,
       "osDevice": osDevice,
       "osDevNotifications": osDevNotifications,
       "osDevModuleInserted": osDevModuleInserted,
       "osDevModuleRemoved": osDevModuleRemoved,
       "osDevModuleLedPowerOn": osDevModuleLedPowerOn,
       "osDevModuleLedPowerOff": osDevModuleLedPowerOff,
       "osDevModuleLedWanOn": osDevModuleLedWanOn,
       "osDevModuleLedWanOff": osDevModuleLedWanOff,
       "osDevModuleLedConnOn": osDevModuleLedConnOn,
       "osDevModuleLedConnOff": osDevModuleLedConnOff,
       "osDevModule": osDevModule,
       "osDevModuleType": osDevModuleType,
       "osDevModuleSlotNumber": osDevModuleSlotNumber,
       "osDevParams": osDevParams,
       "osDevSerial": osDevSerial,
       "osDevSerialNumber": osDevSerialNumber,
       "osDevSerialTable": osDevSerialTable,
       "osDevSerialEntry": osDevSerialEntry,
       "osDevSerialIndex": osDevSerialIndex,
       "osDevSerialOperBaudrate": osDevSerialOperBaudrate,
       "osDevSerialAdminBaudrate": osDevSerialAdminBaudrate,
       "osDevConformance": osDevConformance,
       "osDevMIBCompliances": osDevMIBCompliances,
       "osDevMIBCompliance": osDevMIBCompliance,
       "osDevMIBGroups": osDevMIBGroups,
       "osDevMandatoryGroup": osDevMandatoryGroup,
       "osDevNotificationsGroup": osDevNotificationsGroup}
)
