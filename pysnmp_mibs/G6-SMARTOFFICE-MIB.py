# SNMP MIB module (G6-SMARTOFFICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-SMARTOFFICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:14 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Smartoffice_ObjectIdentity = ObjectIdentity
smartoffice = _Smartoffice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99)
)


class _SmartofficeEnableSmartOffice_Type(Integer32):
    """Custom type smartofficeEnableSmartOffice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SmartofficeEnableSmartOffice_Type.__name__ = "Integer32"
_SmartofficeEnableSmartOffice_Object = MibScalar
smartofficeEnableSmartOffice = _SmartofficeEnableSmartOffice_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 1),
    _SmartofficeEnableSmartOffice_Type()
)
smartofficeEnableSmartOffice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartofficeEnableSmartOffice.setStatus("current")
_DirectorConfigTable_Object = MibTable
directorConfigTable = _DirectorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 2)
)
if mibBuilder.loadTexts:
    directorConfigTable.setStatus("current")
_DirectorConfigEntry_Object = MibTableRow
directorConfigEntry = _DirectorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 2, 1)
)
directorConfigEntry.setIndexNames(
    (0, "G6-SMARTOFFICE-MIB", "directorConfigIndex"),
)
if mibBuilder.loadTexts:
    directorConfigEntry.setStatus("current")


class _DirectorConfigIndex_Type(Integer32):
    """Custom type directorConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_DirectorConfigIndex_Type.__name__ = "Integer32"
_DirectorConfigIndex_Object = MibTableColumn
directorConfigIndex = _DirectorConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 2, 1, 1),
    _DirectorConfigIndex_Type()
)
directorConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    directorConfigIndex.setStatus("current")
_DirectorConfigDomainName_Type = DisplayString
_DirectorConfigDomainName_Object = MibTableColumn
directorConfigDomainName = _DirectorConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 2, 1, 2),
    _DirectorConfigDomainName_Type()
)
directorConfigDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    directorConfigDomainName.setStatus("current")


class _DirectorConfigGeneralMode_Type(Integer32):
    """Custom type directorConfigGeneralMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("automatic", 1),
          ("passive", 2))
    )


_DirectorConfigGeneralMode_Type.__name__ = "Integer32"
_DirectorConfigGeneralMode_Object = MibTableColumn
directorConfigGeneralMode = _DirectorConfigGeneralMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 2, 1, 3),
    _DirectorConfigGeneralMode_Type()
)
directorConfigGeneralMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    directorConfigGeneralMode.setStatus("current")


class _DirectorConfigActOnUngroupedSensors_Type(Integer32):
    """Custom type directorConfigActOnUngroupedSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DirectorConfigActOnUngroupedSensors_Type.__name__ = "Integer32"
_DirectorConfigActOnUngroupedSensors_Object = MibTableColumn
directorConfigActOnUngroupedSensors = _DirectorConfigActOnUngroupedSensors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 2, 1, 4),
    _DirectorConfigActOnUngroupedSensors_Type()
)
directorConfigActOnUngroupedSensors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    directorConfigActOnUngroupedSensors.setStatus("current")
_DirectorConfigScanLightControllers_Type = DisplayString
_DirectorConfigScanLightControllers_Object = MibTableColumn
directorConfigScanLightControllers = _DirectorConfigScanLightControllers_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 2, 1, 5),
    _DirectorConfigScanLightControllers_Type()
)
directorConfigScanLightControllers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    directorConfigScanLightControllers.setStatus("current")
_DeviceConfigTable_Object = MibTable
deviceConfigTable = _DeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3)
)
if mibBuilder.loadTexts:
    deviceConfigTable.setStatus("current")
_DeviceConfigEntry_Object = MibTableRow
deviceConfigEntry = _DeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1)
)
deviceConfigEntry.setIndexNames(
    (0, "G6-SMARTOFFICE-MIB", "deviceConfigIndex"),
)
if mibBuilder.loadTexts:
    deviceConfigEntry.setStatus("current")


class _DeviceConfigIndex_Type(Integer32):
    """Custom type deviceConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DeviceConfigIndex_Type.__name__ = "Integer32"
_DeviceConfigIndex_Object = MibTableColumn
deviceConfigIndex = _DeviceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 1),
    _DeviceConfigIndex_Type()
)
deviceConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceConfigIndex.setStatus("current")
_DeviceConfigDeviceName_Type = DisplayString
_DeviceConfigDeviceName_Object = MibTableColumn
deviceConfigDeviceName = _DeviceConfigDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 2),
    _DeviceConfigDeviceName_Type()
)
deviceConfigDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigDeviceName.setStatus("current")
_DeviceConfigLocation_Type = DisplayString
_DeviceConfigLocation_Object = MibTableColumn
deviceConfigLocation = _DeviceConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 3),
    _DeviceConfigLocation_Type()
)
deviceConfigLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigLocation.setStatus("current")
_DeviceConfigLatitude_Type = DisplayString
_DeviceConfigLatitude_Object = MibTableColumn
deviceConfigLatitude = _DeviceConfigLatitude_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 4),
    _DeviceConfigLatitude_Type()
)
deviceConfigLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigLatitude.setStatus("current")
_DeviceConfigLongitude_Type = DisplayString
_DeviceConfigLongitude_Object = MibTableColumn
deviceConfigLongitude = _DeviceConfigLongitude_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 5),
    _DeviceConfigLongitude_Type()
)
deviceConfigLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigLongitude.setStatus("current")
_DeviceConfigAltitude_Type = DisplayString
_DeviceConfigAltitude_Object = MibTableColumn
deviceConfigAltitude = _DeviceConfigAltitude_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 6),
    _DeviceConfigAltitude_Type()
)
deviceConfigAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigAltitude.setStatus("current")


class _DeviceConfigPlacement_Type(Integer32):
    """Custom type deviceConfigPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("floor", 1),
          ("wall", 2),
          ("ceiling", 3),
          ("duct", 4),
          ("outside", 5),
          ("desk", 6))
    )


_DeviceConfigPlacement_Type.__name__ = "Integer32"
_DeviceConfigPlacement_Object = MibTableColumn
deviceConfigPlacement = _DeviceConfigPlacement_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 7),
    _DeviceConfigPlacement_Type()
)
deviceConfigPlacement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigPlacement.setStatus("current")


class _DeviceConfigProductType_Type(Integer32):
    """Custom type deviceConfigProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("virtual", 0),
          ("smartlightController", 1),
          ("directorCascade", 2),
          ("hm", 3),
          ("fhem", 4),
          ("ip500", 5),
          ("enocean", 6),
          ("knx", 7))
    )


_DeviceConfigProductType_Type.__name__ = "Integer32"
_DeviceConfigProductType_Object = MibTableColumn
deviceConfigProductType = _DeviceConfigProductType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 8),
    _DeviceConfigProductType_Type()
)
deviceConfigProductType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigProductType.setStatus("current")
_DeviceConfigDeviceId_Type = DisplayString
_DeviceConfigDeviceId_Object = MibTableColumn
deviceConfigDeviceId = _DeviceConfigDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 9),
    _DeviceConfigDeviceId_Type()
)
deviceConfigDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigDeviceId.setStatus("current")
_DeviceConfigNetworkAddress_Type = DisplayString
_DeviceConfigNetworkAddress_Object = MibTableColumn
deviceConfigNetworkAddress = _DeviceConfigNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 10),
    _DeviceConfigNetworkAddress_Type()
)
deviceConfigNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigNetworkAddress.setStatus("current")
_DeviceConfigAdditionalParameter_Type = DisplayString
_DeviceConfigAdditionalParameter_Object = MibTableColumn
deviceConfigAdditionalParameter = _DeviceConfigAdditionalParameter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 11),
    _DeviceConfigAdditionalParameter_Type()
)
deviceConfigAdditionalParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigAdditionalParameter.setStatus("current")


class _DeviceConfigNetworkFailureAction_Type(Integer32):
    """Custom type deviceConfigNetworkFailureAction based on Integer32"""
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
        *(("keepCurrent", 0),
          ("off", 1),
          ("on", 2),
          ("dimmed", 3))
    )


_DeviceConfigNetworkFailureAction_Type.__name__ = "Integer32"
_DeviceConfigNetworkFailureAction_Object = MibTableColumn
deviceConfigNetworkFailureAction = _DeviceConfigNetworkFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 12),
    _DeviceConfigNetworkFailureAction_Type()
)
deviceConfigNetworkFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigNetworkFailureAction.setStatus("current")
_DeviceConfigIdentify_Type = DisplayString
_DeviceConfigIdentify_Object = MibTableColumn
deviceConfigIdentify = _DeviceConfigIdentify_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 13),
    _DeviceConfigIdentify_Type()
)
deviceConfigIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigIdentify.setStatus("current")
_DeviceConfigRestart_Type = DisplayString
_DeviceConfigRestart_Object = MibTableColumn
deviceConfigRestart = _DeviceConfigRestart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 14),
    _DeviceConfigRestart_Type()
)
deviceConfigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigRestart.setStatus("current")
_DeviceConfigCalibrate_Type = DisplayString
_DeviceConfigCalibrate_Object = MibTableColumn
deviceConfigCalibrate = _DeviceConfigCalibrate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 15),
    _DeviceConfigCalibrate_Type()
)
deviceConfigCalibrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigCalibrate.setStatus("current")
_DeviceConfigPair_Type = DisplayString
_DeviceConfigPair_Object = MibTableColumn
deviceConfigPair = _DeviceConfigPair_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 16),
    _DeviceConfigPair_Type()
)
deviceConfigPair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigPair.setStatus("current")
_DeviceConfigUnpair_Type = DisplayString
_DeviceConfigUnpair_Object = MibTableColumn
deviceConfigUnpair = _DeviceConfigUnpair_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 17),
    _DeviceConfigUnpair_Type()
)
deviceConfigUnpair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigUnpair.setStatus("current")
_DeviceConfigUpdateFirmware_Type = DisplayString
_DeviceConfigUpdateFirmware_Object = MibTableColumn
deviceConfigUpdateFirmware = _DeviceConfigUpdateFirmware_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 3, 1, 18),
    _DeviceConfigUpdateFirmware_Type()
)
deviceConfigUpdateFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceConfigUpdateFirmware.setStatus("current")
_ActorGroupConfigTable_Object = MibTable
actorGroupConfigTable = _ActorGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4)
)
if mibBuilder.loadTexts:
    actorGroupConfigTable.setStatus("current")
_ActorGroupConfigEntry_Object = MibTableRow
actorGroupConfigEntry = _ActorGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1)
)
actorGroupConfigEntry.setIndexNames(
    (0, "G6-SMARTOFFICE-MIB", "actorGroupConfigIndex"),
)
if mibBuilder.loadTexts:
    actorGroupConfigEntry.setStatus("current")


class _ActorGroupConfigIndex_Type(Integer32):
    """Custom type actorGroupConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ActorGroupConfigIndex_Type.__name__ = "Integer32"
_ActorGroupConfigIndex_Object = MibTableColumn
actorGroupConfigIndex = _ActorGroupConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1, 1),
    _ActorGroupConfigIndex_Type()
)
actorGroupConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    actorGroupConfigIndex.setStatus("current")
_ActorGroupConfigGroupName_Type = DisplayString
_ActorGroupConfigGroupName_Object = MibTableColumn
actorGroupConfigGroupName = _ActorGroupConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1, 2),
    _ActorGroupConfigGroupName_Type()
)
actorGroupConfigGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actorGroupConfigGroupName.setStatus("current")
_ActorGroupConfigAttribute_Type = DisplayString
_ActorGroupConfigAttribute_Object = MibTableColumn
actorGroupConfigAttribute = _ActorGroupConfigAttribute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1, 3),
    _ActorGroupConfigAttribute_Type()
)
actorGroupConfigAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actorGroupConfigAttribute.setStatus("current")
_ActorGroupConfigAssociatedDevices_Type = DisplayString
_ActorGroupConfigAssociatedDevices_Object = MibTableColumn
actorGroupConfigAssociatedDevices = _ActorGroupConfigAssociatedDevices_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1, 4),
    _ActorGroupConfigAssociatedDevices_Type()
)
actorGroupConfigAssociatedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actorGroupConfigAssociatedDevices.setStatus("current")
_ActorGroupConfigAdditionalParameter_Type = DisplayString
_ActorGroupConfigAdditionalParameter_Object = MibTableColumn
actorGroupConfigAdditionalParameter = _ActorGroupConfigAdditionalParameter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1, 5),
    _ActorGroupConfigAdditionalParameter_Type()
)
actorGroupConfigAdditionalParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actorGroupConfigAdditionalParameter.setStatus("current")
_ActorGroupConfigDefaultValue_Type = DisplayString
_ActorGroupConfigDefaultValue_Object = MibTableColumn
actorGroupConfigDefaultValue = _ActorGroupConfigDefaultValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1, 6),
    _ActorGroupConfigDefaultValue_Type()
)
actorGroupConfigDefaultValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actorGroupConfigDefaultValue.setStatus("current")


class _ActorGroupConfigValueCaching_Type(Integer32):
    """Custom type actorGroupConfigValueCaching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ActorGroupConfigValueCaching_Type.__name__ = "Integer32"
_ActorGroupConfigValueCaching_Object = MibTableColumn
actorGroupConfigValueCaching = _ActorGroupConfigValueCaching_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1, 7),
    _ActorGroupConfigValueCaching_Type()
)
actorGroupConfigValueCaching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actorGroupConfigValueCaching.setStatus("current")
_ActorGroupConfigAdditionalScriptName_Type = DisplayString
_ActorGroupConfigAdditionalScriptName_Object = MibTableColumn
actorGroupConfigAdditionalScriptName = _ActorGroupConfigAdditionalScriptName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1, 8),
    _ActorGroupConfigAdditionalScriptName_Type()
)
actorGroupConfigAdditionalScriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actorGroupConfigAdditionalScriptName.setStatus("current")
_ActorGroupConfigManualSetValue_Type = DisplayString
_ActorGroupConfigManualSetValue_Object = MibTableColumn
actorGroupConfigManualSetValue = _ActorGroupConfigManualSetValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 4, 1, 9),
    _ActorGroupConfigManualSetValue_Type()
)
actorGroupConfigManualSetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actorGroupConfigManualSetValue.setStatus("current")
_SensorGroupConfigTable_Object = MibTable
sensorGroupConfigTable = _SensorGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5)
)
if mibBuilder.loadTexts:
    sensorGroupConfigTable.setStatus("current")
_SensorGroupConfigEntry_Object = MibTableRow
sensorGroupConfigEntry = _SensorGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1)
)
sensorGroupConfigEntry.setIndexNames(
    (0, "G6-SMARTOFFICE-MIB", "sensorGroupConfigIndex"),
)
if mibBuilder.loadTexts:
    sensorGroupConfigEntry.setStatus("current")


class _SensorGroupConfigIndex_Type(Integer32):
    """Custom type sensorGroupConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SensorGroupConfigIndex_Type.__name__ = "Integer32"
_SensorGroupConfigIndex_Object = MibTableColumn
sensorGroupConfigIndex = _SensorGroupConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 1),
    _SensorGroupConfigIndex_Type()
)
sensorGroupConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorGroupConfigIndex.setStatus("current")
_SensorGroupConfigGroupName_Type = DisplayString
_SensorGroupConfigGroupName_Object = MibTableColumn
sensorGroupConfigGroupName = _SensorGroupConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 2),
    _SensorGroupConfigGroupName_Type()
)
sensorGroupConfigGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigGroupName.setStatus("current")
_SensorGroupConfigAttribute_Type = DisplayString
_SensorGroupConfigAttribute_Object = MibTableColumn
sensorGroupConfigAttribute = _SensorGroupConfigAttribute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 3),
    _SensorGroupConfigAttribute_Type()
)
sensorGroupConfigAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigAttribute.setStatus("current")
_SensorGroupConfigAssociatedDevices_Type = DisplayString
_SensorGroupConfigAssociatedDevices_Object = MibTableColumn
sensorGroupConfigAssociatedDevices = _SensorGroupConfigAssociatedDevices_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 4),
    _SensorGroupConfigAssociatedDevices_Type()
)
sensorGroupConfigAssociatedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigAssociatedDevices.setStatus("current")


class _SensorGroupConfigValueCaching_Type(Integer32):
    """Custom type sensorGroupConfigValueCaching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SensorGroupConfigValueCaching_Type.__name__ = "Integer32"
_SensorGroupConfigValueCaching_Object = MibTableColumn
sensorGroupConfigValueCaching = _SensorGroupConfigValueCaching_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 5),
    _SensorGroupConfigValueCaching_Type()
)
sensorGroupConfigValueCaching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigValueCaching.setStatus("current")


class _SensorGroupConfigRunScriptWhen_Type(Integer32):
    """Custom type sensorGroupConfigRunScriptWhen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("anyChange", 1),
          ("limitCrossed", 2),
          ("avgAbsolute", 3),
          ("avgPercent", 4),
          ("totalAbsolute", 5),
          ("totalPercent", 6),
          ("newPeakLevel", 7),
          ("anyUpdate", 8),
          ("zeroCrossing", 9))
    )


_SensorGroupConfigRunScriptWhen_Type.__name__ = "Integer32"
_SensorGroupConfigRunScriptWhen_Object = MibTableColumn
sensorGroupConfigRunScriptWhen = _SensorGroupConfigRunScriptWhen_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 6),
    _SensorGroupConfigRunScriptWhen_Type()
)
sensorGroupConfigRunScriptWhen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigRunScriptWhen.setStatus("current")
_SensorGroupConfigRunScriptDelta_Type = DisplayString
_SensorGroupConfigRunScriptDelta_Object = MibTableColumn
sensorGroupConfigRunScriptDelta = _SensorGroupConfigRunScriptDelta_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 7),
    _SensorGroupConfigRunScriptDelta_Type()
)
sensorGroupConfigRunScriptDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigRunScriptDelta.setStatus("current")
_SensorGroupConfigScriptName_Type = DisplayString
_SensorGroupConfigScriptName_Object = MibTableColumn
sensorGroupConfigScriptName = _SensorGroupConfigScriptName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 8),
    _SensorGroupConfigScriptName_Type()
)
sensorGroupConfigScriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigScriptName.setStatus("current")
_SensorGroupConfigAdditionalScriptName_Type = DisplayString
_SensorGroupConfigAdditionalScriptName_Object = MibTableColumn
sensorGroupConfigAdditionalScriptName = _SensorGroupConfigAdditionalScriptName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 9),
    _SensorGroupConfigAdditionalScriptName_Type()
)
sensorGroupConfigAdditionalScriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigAdditionalScriptName.setStatus("current")


class _SensorGroupConfigReportMode_Type(Integer32):
    """Custom type sensorGroupConfigReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("passive", 1),
          ("deltaPercent", 2),
          ("deltaAbsolute", 3),
          ("onThreshold", 4),
          ("test", 5))
    )


_SensorGroupConfigReportMode_Type.__name__ = "Integer32"
_SensorGroupConfigReportMode_Object = MibTableColumn
sensorGroupConfigReportMode = _SensorGroupConfigReportMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 10),
    _SensorGroupConfigReportMode_Type()
)
sensorGroupConfigReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigReportMode.setStatus("current")
_SensorGroupConfigAdditionalParameter_Type = DisplayString
_SensorGroupConfigAdditionalParameter_Object = MibTableColumn
sensorGroupConfigAdditionalParameter = _SensorGroupConfigAdditionalParameter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 11),
    _SensorGroupConfigAdditionalParameter_Type()
)
sensorGroupConfigAdditionalParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigAdditionalParameter.setStatus("current")
_SensorGroupConfigLowerBoundary_Type = DisplayString
_SensorGroupConfigLowerBoundary_Object = MibTableColumn
sensorGroupConfigLowerBoundary = _SensorGroupConfigLowerBoundary_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 12),
    _SensorGroupConfigLowerBoundary_Type()
)
sensorGroupConfigLowerBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigLowerBoundary.setStatus("current")
_SensorGroupConfigUpperBoundary_Type = DisplayString
_SensorGroupConfigUpperBoundary_Object = MibTableColumn
sensorGroupConfigUpperBoundary = _SensorGroupConfigUpperBoundary_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 13),
    _SensorGroupConfigUpperBoundary_Type()
)
sensorGroupConfigUpperBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigUpperBoundary.setStatus("current")


class _SensorGroupConfigBoundaryHysteresis_Type(Integer32):
    """Custom type sensorGroupConfigBoundaryHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("low", 1),
          ("high", 2))
    )


_SensorGroupConfigBoundaryHysteresis_Type.__name__ = "Integer32"
_SensorGroupConfigBoundaryHysteresis_Object = MibTableColumn
sensorGroupConfigBoundaryHysteresis = _SensorGroupConfigBoundaryHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 14),
    _SensorGroupConfigBoundaryHysteresis_Type()
)
sensorGroupConfigBoundaryHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigBoundaryHysteresis.setStatus("current")
_SensorGroupConfigUpdateDelta_Type = DisplayString
_SensorGroupConfigUpdateDelta_Object = MibTableColumn
sensorGroupConfigUpdateDelta = _SensorGroupConfigUpdateDelta_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 15),
    _SensorGroupConfigUpdateDelta_Type()
)
sensorGroupConfigUpdateDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigUpdateDelta.setStatus("current")
_SensorGroupConfigRateLimit_Type = Unsigned32
_SensorGroupConfigRateLimit_Object = MibTableColumn
sensorGroupConfigRateLimit = _SensorGroupConfigRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 16),
    _SensorGroupConfigRateLimit_Type()
)
sensorGroupConfigRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigRateLimit.setStatus("current")
_SensorGroupConfigClearValues_Type = DisplayString
_SensorGroupConfigClearValues_Object = MibTableColumn
sensorGroupConfigClearValues = _SensorGroupConfigClearValues_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 5, 1, 17),
    _SensorGroupConfigClearValues_Type()
)
sensorGroupConfigClearValues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorGroupConfigClearValues.setStatus("current")
_DeviceInformationTable_Object = MibTable
deviceInformationTable = _DeviceInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100)
)
if mibBuilder.loadTexts:
    deviceInformationTable.setStatus("current")
_DeviceInformationEntry_Object = MibTableRow
deviceInformationEntry = _DeviceInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1)
)
deviceInformationEntry.setIndexNames(
    (0, "G6-SMARTOFFICE-MIB", "deviceInformationIndex"),
)
if mibBuilder.loadTexts:
    deviceInformationEntry.setStatus("current")


class _DeviceInformationIndex_Type(Integer32):
    """Custom type deviceInformationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DeviceInformationIndex_Type.__name__ = "Integer32"
_DeviceInformationIndex_Object = MibTableColumn
deviceInformationIndex = _DeviceInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 1),
    _DeviceInformationIndex_Type()
)
deviceInformationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceInformationIndex.setStatus("current")
_DeviceInformationName_Type = DisplayString
_DeviceInformationName_Object = MibTableColumn
deviceInformationName = _DeviceInformationName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 2),
    _DeviceInformationName_Type()
)
deviceInformationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationName.setStatus("current")
_DeviceInformationHardwareId_Type = DisplayString
_DeviceInformationHardwareId_Object = MibTableColumn
deviceInformationHardwareId = _DeviceInformationHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 3),
    _DeviceInformationHardwareId_Type()
)
deviceInformationHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationHardwareId.setStatus("current")


class _DeviceInformationDeviceType_Type(Integer32):
    """Custom type deviceInformationDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("sensor", 1),
          ("actor", 2),
          ("actorSensor", 3),
          ("gateway", 4),
          ("other", 5))
    )


_DeviceInformationDeviceType_Type.__name__ = "Integer32"
_DeviceInformationDeviceType_Object = MibTableColumn
deviceInformationDeviceType = _DeviceInformationDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 4),
    _DeviceInformationDeviceType_Type()
)
deviceInformationDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationDeviceType.setStatus("current")


class _DeviceInformationOperationalState_Type(Integer32):
    """Custom type deviceInformationOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("failed", 1),
          ("normal", 2),
          ("testMode", 3),
          ("configError", 4),
          ("unpaired", 5),
          ("notReady", 6),
          ("pairing", 7),
          ("inConfig", 8),
          ("unregistered", 9))
    )


_DeviceInformationOperationalState_Type.__name__ = "Integer32"
_DeviceInformationOperationalState_Object = MibTableColumn
deviceInformationOperationalState = _DeviceInformationOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 5),
    _DeviceInformationOperationalState_Type()
)
deviceInformationOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationOperationalState.setStatus("current")
_DeviceInformationActorAttributes_Type = DisplayString
_DeviceInformationActorAttributes_Object = MibTableColumn
deviceInformationActorAttributes = _DeviceInformationActorAttributes_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 6),
    _DeviceInformationActorAttributes_Type()
)
deviceInformationActorAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationActorAttributes.setStatus("current")
_DeviceInformationSensorAttributes_Type = DisplayString
_DeviceInformationSensorAttributes_Object = MibTableColumn
deviceInformationSensorAttributes = _DeviceInformationSensorAttributes_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 7),
    _DeviceInformationSensorAttributes_Type()
)
deviceInformationSensorAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationSensorAttributes.setStatus("current")
_DeviceInformationVendorName_Type = DisplayString
_DeviceInformationVendorName_Object = MibTableColumn
deviceInformationVendorName = _DeviceInformationVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 8),
    _DeviceInformationVendorName_Type()
)
deviceInformationVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationVendorName.setStatus("current")
_DeviceInformationArticleNumber_Type = DisplayString
_DeviceInformationArticleNumber_Object = MibTableColumn
deviceInformationArticleNumber = _DeviceInformationArticleNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 9),
    _DeviceInformationArticleNumber_Type()
)
deviceInformationArticleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationArticleNumber.setStatus("current")
_DeviceInformationSerialNumber_Type = DisplayString
_DeviceInformationSerialNumber_Object = MibTableColumn
deviceInformationSerialNumber = _DeviceInformationSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 10),
    _DeviceInformationSerialNumber_Type()
)
deviceInformationSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationSerialNumber.setStatus("current")
_DeviceInformationHardwareRevision_Type = DisplayString
_DeviceInformationHardwareRevision_Object = MibTableColumn
deviceInformationHardwareRevision = _DeviceInformationHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 11),
    _DeviceInformationHardwareRevision_Type()
)
deviceInformationHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationHardwareRevision.setStatus("current")
_DeviceInformationSoftwareVersion_Type = DisplayString
_DeviceInformationSoftwareVersion_Object = MibTableColumn
deviceInformationSoftwareVersion = _DeviceInformationSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 12),
    _DeviceInformationSoftwareVersion_Type()
)
deviceInformationSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationSoftwareVersion.setStatus("current")
_DeviceInformationAdditionalInfo_Type = DisplayString
_DeviceInformationAdditionalInfo_Object = MibTableColumn
deviceInformationAdditionalInfo = _DeviceInformationAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 100, 1, 13),
    _DeviceInformationAdditionalInfo_Type()
)
deviceInformationAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationAdditionalInfo.setStatus("current")
_ActorListTable_Object = MibTable
actorListTable = _ActorListTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101)
)
if mibBuilder.loadTexts:
    actorListTable.setStatus("current")
_ActorListEntry_Object = MibTableRow
actorListEntry = _ActorListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101, 1)
)
actorListEntry.setIndexNames(
    (0, "G6-SMARTOFFICE-MIB", "actorListIndex"),
)
if mibBuilder.loadTexts:
    actorListEntry.setStatus("current")


class _ActorListIndex_Type(Integer32):
    """Custom type actorListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ActorListIndex_Type.__name__ = "Integer32"
_ActorListIndex_Object = MibTableColumn
actorListIndex = _ActorListIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101, 1, 1),
    _ActorListIndex_Type()
)
actorListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    actorListIndex.setStatus("current")
_ActorListDevice_Type = DisplayString
_ActorListDevice_Object = MibTableColumn
actorListDevice = _ActorListDevice_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101, 1, 2),
    _ActorListDevice_Type()
)
actorListDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorListDevice.setStatus("current")
_ActorListInstance_Type = DisplayString
_ActorListInstance_Object = MibTableColumn
actorListInstance = _ActorListInstance_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101, 1, 3),
    _ActorListInstance_Type()
)
actorListInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorListInstance.setStatus("current")
_ActorListAttribute_Type = DisplayString
_ActorListAttribute_Object = MibTableColumn
actorListAttribute = _ActorListAttribute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101, 1, 4),
    _ActorListAttribute_Type()
)
actorListAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorListAttribute.setStatus("current")
_ActorListAssociatedGroups_Type = DisplayString
_ActorListAssociatedGroups_Object = MibTableColumn
actorListAssociatedGroups = _ActorListAssociatedGroups_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101, 1, 5),
    _ActorListAssociatedGroups_Type()
)
actorListAssociatedGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorListAssociatedGroups.setStatus("current")
_ActorListValue_Type = DisplayString
_ActorListValue_Object = MibTableColumn
actorListValue = _ActorListValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101, 1, 6),
    _ActorListValue_Type()
)
actorListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorListValue.setStatus("current")


class _ActorListActorState_Type(Integer32):
    """Custom type actorListActorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("unknown", 0),
          ("ok", 1),
          ("requested", 2),
          ("retrying", 3),
          ("confirmed", 4),
          ("denied", 5),
          ("failed", 6),
          ("restored", 7),
          ("manually", 8))
    )


_ActorListActorState_Type.__name__ = "Integer32"
_ActorListActorState_Object = MibTableColumn
actorListActorState = _ActorListActorState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101, 1, 7),
    _ActorListActorState_Type()
)
actorListActorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorListActorState.setStatus("current")
_ActorListLastUpdate_Type = Counter32
_ActorListLastUpdate_Object = MibTableColumn
actorListLastUpdate = _ActorListLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 101, 1, 8),
    _ActorListLastUpdate_Type()
)
actorListLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorListLastUpdate.setStatus("current")
_SensorListTable_Object = MibTable
sensorListTable = _SensorListTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102)
)
if mibBuilder.loadTexts:
    sensorListTable.setStatus("current")
_SensorListEntry_Object = MibTableRow
sensorListEntry = _SensorListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102, 1)
)
sensorListEntry.setIndexNames(
    (0, "G6-SMARTOFFICE-MIB", "sensorListIndex"),
)
if mibBuilder.loadTexts:
    sensorListEntry.setStatus("current")


class _SensorListIndex_Type(Integer32):
    """Custom type sensorListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SensorListIndex_Type.__name__ = "Integer32"
_SensorListIndex_Object = MibTableColumn
sensorListIndex = _SensorListIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102, 1, 1),
    _SensorListIndex_Type()
)
sensorListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorListIndex.setStatus("current")
_SensorListDevice_Type = DisplayString
_SensorListDevice_Object = MibTableColumn
sensorListDevice = _SensorListDevice_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102, 1, 2),
    _SensorListDevice_Type()
)
sensorListDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorListDevice.setStatus("current")
_SensorListInstance_Type = DisplayString
_SensorListInstance_Object = MibTableColumn
sensorListInstance = _SensorListInstance_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102, 1, 3),
    _SensorListInstance_Type()
)
sensorListInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorListInstance.setStatus("current")
_SensorListAttribute_Type = DisplayString
_SensorListAttribute_Object = MibTableColumn
sensorListAttribute = _SensorListAttribute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102, 1, 4),
    _SensorListAttribute_Type()
)
sensorListAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorListAttribute.setStatus("current")
_SensorListAssociatedGroups_Type = DisplayString
_SensorListAssociatedGroups_Object = MibTableColumn
sensorListAssociatedGroups = _SensorListAssociatedGroups_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102, 1, 5),
    _SensorListAssociatedGroups_Type()
)
sensorListAssociatedGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorListAssociatedGroups.setStatus("current")
_SensorListValue_Type = DisplayString
_SensorListValue_Object = MibTableColumn
sensorListValue = _SensorListValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102, 1, 6),
    _SensorListValue_Type()
)
sensorListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorListValue.setStatus("current")


class _SensorListSensorState_Type(Integer32):
    """Custom type sensorListSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ok", 1),
          ("lowBatt", 2),
          ("lowerLimit", 3),
          ("upperLimit", 4),
          ("commFailed", 5),
          ("deviceFailed", 6),
          ("manually", 8))
    )


_SensorListSensorState_Type.__name__ = "Integer32"
_SensorListSensorState_Object = MibTableColumn
sensorListSensorState = _SensorListSensorState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102, 1, 7),
    _SensorListSensorState_Type()
)
sensorListSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorListSensorState.setStatus("current")
_SensorListLastUpdate_Type = Counter32
_SensorListLastUpdate_Object = MibTableColumn
sensorListLastUpdate = _SensorListLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 102, 1, 8),
    _SensorListLastUpdate_Type()
)
sensorListLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorListLastUpdate.setStatus("current")
_ActorGroupStatusTable_Object = MibTable
actorGroupStatusTable = _ActorGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103)
)
if mibBuilder.loadTexts:
    actorGroupStatusTable.setStatus("current")
_ActorGroupStatusEntry_Object = MibTableRow
actorGroupStatusEntry = _ActorGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1)
)
actorGroupStatusEntry.setIndexNames(
    (0, "G6-SMARTOFFICE-MIB", "actorGroupStatusIndex"),
)
if mibBuilder.loadTexts:
    actorGroupStatusEntry.setStatus("current")


class _ActorGroupStatusIndex_Type(Integer32):
    """Custom type actorGroupStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ActorGroupStatusIndex_Type.__name__ = "Integer32"
_ActorGroupStatusIndex_Object = MibTableColumn
actorGroupStatusIndex = _ActorGroupStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 1),
    _ActorGroupStatusIndex_Type()
)
actorGroupStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    actorGroupStatusIndex.setStatus("current")
_ActorGroupStatusGroupName_Type = DisplayString
_ActorGroupStatusGroupName_Object = MibTableColumn
actorGroupStatusGroupName = _ActorGroupStatusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 2),
    _ActorGroupStatusGroupName_Type()
)
actorGroupStatusGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusGroupName.setStatus("current")
_ActorGroupStatusAttribute_Type = DisplayString
_ActorGroupStatusAttribute_Object = MibTableColumn
actorGroupStatusAttribute = _ActorGroupStatusAttribute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 3),
    _ActorGroupStatusAttribute_Type()
)
actorGroupStatusAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusAttribute.setStatus("current")


class _ActorGroupStatusNumAssignedActors_Type(Integer32):
    """Custom type actorGroupStatusNumAssignedActors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ActorGroupStatusNumAssignedActors_Type.__name__ = "Integer32"
_ActorGroupStatusNumAssignedActors_Object = MibTableColumn
actorGroupStatusNumAssignedActors = _ActorGroupStatusNumAssignedActors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 4),
    _ActorGroupStatusNumAssignedActors_Type()
)
actorGroupStatusNumAssignedActors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusNumAssignedActors.setStatus("current")


class _ActorGroupStatusNumFailedActors_Type(Integer32):
    """Custom type actorGroupStatusNumFailedActors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ActorGroupStatusNumFailedActors_Type.__name__ = "Integer32"
_ActorGroupStatusNumFailedActors_Object = MibTableColumn
actorGroupStatusNumFailedActors = _ActorGroupStatusNumFailedActors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 5),
    _ActorGroupStatusNumFailedActors_Type()
)
actorGroupStatusNumFailedActors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusNumFailedActors.setStatus("current")


class _ActorGroupStatusGroupState_Type(Integer32):
    """Custom type actorGroupStatusGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ok", 1),
          ("updating", 2),
          ("unreliable", 3),
          ("manually", 8))
    )


_ActorGroupStatusGroupState_Type.__name__ = "Integer32"
_ActorGroupStatusGroupState_Object = MibTableColumn
actorGroupStatusGroupState = _ActorGroupStatusGroupState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 6),
    _ActorGroupStatusGroupState_Type()
)
actorGroupStatusGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusGroupState.setStatus("current")
_ActorGroupStatusValue_Type = DisplayString
_ActorGroupStatusValue_Object = MibTableColumn
actorGroupStatusValue = _ActorGroupStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 7),
    _ActorGroupStatusValue_Type()
)
actorGroupStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusValue.setStatus("current")
_ActorGroupStatusActivePriority_Type = Unsigned32
_ActorGroupStatusActivePriority_Object = MibTableColumn
actorGroupStatusActivePriority = _ActorGroupStatusActivePriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 8),
    _ActorGroupStatusActivePriority_Type()
)
actorGroupStatusActivePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusActivePriority.setStatus("current")
_ActorGroupStatusPriorityValueChain_Type = DisplayString
_ActorGroupStatusPriorityValueChain_Object = MibTableColumn
actorGroupStatusPriorityValueChain = _ActorGroupStatusPriorityValueChain_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 9),
    _ActorGroupStatusPriorityValueChain_Type()
)
actorGroupStatusPriorityValueChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusPriorityValueChain.setStatus("current")


class _ActorGroupStatusCacheStatus_Type(Integer32):
    """Custom type actorGroupStatusCacheStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disabled", 1),
          ("pending", 2),
          ("saved", 3),
          ("failed", 4))
    )


_ActorGroupStatusCacheStatus_Type.__name__ = "Integer32"
_ActorGroupStatusCacheStatus_Object = MibTableColumn
actorGroupStatusCacheStatus = _ActorGroupStatusCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 10),
    _ActorGroupStatusCacheStatus_Type()
)
actorGroupStatusCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusCacheStatus.setStatus("current")
_ActorGroupStatusLastUpdate_Type = Counter32
_ActorGroupStatusLastUpdate_Object = MibTableColumn
actorGroupStatusLastUpdate = _ActorGroupStatusLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 103, 1, 11),
    _ActorGroupStatusLastUpdate_Type()
)
actorGroupStatusLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorGroupStatusLastUpdate.setStatus("current")
_SensorGroupStatusTable_Object = MibTable
sensorGroupStatusTable = _SensorGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104)
)
if mibBuilder.loadTexts:
    sensorGroupStatusTable.setStatus("current")
_SensorGroupStatusEntry_Object = MibTableRow
sensorGroupStatusEntry = _SensorGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1)
)
sensorGroupStatusEntry.setIndexNames(
    (0, "G6-SMARTOFFICE-MIB", "sensorGroupStatusIndex"),
)
if mibBuilder.loadTexts:
    sensorGroupStatusEntry.setStatus("current")


class _SensorGroupStatusIndex_Type(Integer32):
    """Custom type sensorGroupStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SensorGroupStatusIndex_Type.__name__ = "Integer32"
_SensorGroupStatusIndex_Object = MibTableColumn
sensorGroupStatusIndex = _SensorGroupStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 1),
    _SensorGroupStatusIndex_Type()
)
sensorGroupStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorGroupStatusIndex.setStatus("current")
_SensorGroupStatusGroupName_Type = DisplayString
_SensorGroupStatusGroupName_Object = MibTableColumn
sensorGroupStatusGroupName = _SensorGroupStatusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 2),
    _SensorGroupStatusGroupName_Type()
)
sensorGroupStatusGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusGroupName.setStatus("current")
_SensorGroupStatusAttribute_Type = DisplayString
_SensorGroupStatusAttribute_Object = MibTableColumn
sensorGroupStatusAttribute = _SensorGroupStatusAttribute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 3),
    _SensorGroupStatusAttribute_Type()
)
sensorGroupStatusAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusAttribute.setStatus("current")


class _SensorGroupStatusNumAssignedSensors_Type(Integer32):
    """Custom type sensorGroupStatusNumAssignedSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SensorGroupStatusNumAssignedSensors_Type.__name__ = "Integer32"
_SensorGroupStatusNumAssignedSensors_Object = MibTableColumn
sensorGroupStatusNumAssignedSensors = _SensorGroupStatusNumAssignedSensors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 4),
    _SensorGroupStatusNumAssignedSensors_Type()
)
sensorGroupStatusNumAssignedSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusNumAssignedSensors.setStatus("current")


class _SensorGroupStatusNumFailedSensors_Type(Integer32):
    """Custom type sensorGroupStatusNumFailedSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SensorGroupStatusNumFailedSensors_Type.__name__ = "Integer32"
_SensorGroupStatusNumFailedSensors_Object = MibTableColumn
sensorGroupStatusNumFailedSensors = _SensorGroupStatusNumFailedSensors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 5),
    _SensorGroupStatusNumFailedSensors_Type()
)
sensorGroupStatusNumFailedSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusNumFailedSensors.setStatus("current")


class _SensorGroupStatusGroupState_Type(Integer32):
    """Custom type sensorGroupStatusGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ok", 1),
          ("updating", 2),
          ("unreliable", 3),
          ("manually", 8))
    )


_SensorGroupStatusGroupState_Type.__name__ = "Integer32"
_SensorGroupStatusGroupState_Object = MibTableColumn
sensorGroupStatusGroupState = _SensorGroupStatusGroupState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 6),
    _SensorGroupStatusGroupState_Type()
)
sensorGroupStatusGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusGroupState.setStatus("current")
_SensorGroupStatusMinimumPeakHold_Type = DisplayString
_SensorGroupStatusMinimumPeakHold_Object = MibTableColumn
sensorGroupStatusMinimumPeakHold = _SensorGroupStatusMinimumPeakHold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 7),
    _SensorGroupStatusMinimumPeakHold_Type()
)
sensorGroupStatusMinimumPeakHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusMinimumPeakHold.setStatus("current")
_SensorGroupStatusMinimumValue_Type = DisplayString
_SensorGroupStatusMinimumValue_Object = MibTableColumn
sensorGroupStatusMinimumValue = _SensorGroupStatusMinimumValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 8),
    _SensorGroupStatusMinimumValue_Type()
)
sensorGroupStatusMinimumValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusMinimumValue.setStatus("current")
_SensorGroupStatusAverageValue_Type = DisplayString
_SensorGroupStatusAverageValue_Object = MibTableColumn
sensorGroupStatusAverageValue = _SensorGroupStatusAverageValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 9),
    _SensorGroupStatusAverageValue_Type()
)
sensorGroupStatusAverageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusAverageValue.setStatus("current")
_SensorGroupStatusMaximumValue_Type = DisplayString
_SensorGroupStatusMaximumValue_Object = MibTableColumn
sensorGroupStatusMaximumValue = _SensorGroupStatusMaximumValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 10),
    _SensorGroupStatusMaximumValue_Type()
)
sensorGroupStatusMaximumValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusMaximumValue.setStatus("current")
_SensorGroupStatusMaximumPeakHold_Type = DisplayString
_SensorGroupStatusMaximumPeakHold_Object = MibTableColumn
sensorGroupStatusMaximumPeakHold = _SensorGroupStatusMaximumPeakHold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 11),
    _SensorGroupStatusMaximumPeakHold_Type()
)
sensorGroupStatusMaximumPeakHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusMaximumPeakHold.setStatus("current")
_SensorGroupStatusTotalValue_Type = DisplayString
_SensorGroupStatusTotalValue_Object = MibTableColumn
sensorGroupStatusTotalValue = _SensorGroupStatusTotalValue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 12),
    _SensorGroupStatusTotalValue_Type()
)
sensorGroupStatusTotalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusTotalValue.setStatus("current")


class _SensorGroupStatusLowerBoundaryReached_Type(Integer32):
    """Custom type sensorGroupStatusLowerBoundaryReached based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SensorGroupStatusLowerBoundaryReached_Type.__name__ = "Integer32"
_SensorGroupStatusLowerBoundaryReached_Object = MibTableColumn
sensorGroupStatusLowerBoundaryReached = _SensorGroupStatusLowerBoundaryReached_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 13),
    _SensorGroupStatusLowerBoundaryReached_Type()
)
sensorGroupStatusLowerBoundaryReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusLowerBoundaryReached.setStatus("current")


class _SensorGroupStatusUpperBoundaryReached_Type(Integer32):
    """Custom type sensorGroupStatusUpperBoundaryReached based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SensorGroupStatusUpperBoundaryReached_Type.__name__ = "Integer32"
_SensorGroupStatusUpperBoundaryReached_Object = MibTableColumn
sensorGroupStatusUpperBoundaryReached = _SensorGroupStatusUpperBoundaryReached_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 14),
    _SensorGroupStatusUpperBoundaryReached_Type()
)
sensorGroupStatusUpperBoundaryReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusUpperBoundaryReached.setStatus("current")


class _SensorGroupStatusUpdatingSensorIndex_Type(Integer32):
    """Custom type sensorGroupStatusUpdatingSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SensorGroupStatusUpdatingSensorIndex_Type.__name__ = "Integer32"
_SensorGroupStatusUpdatingSensorIndex_Object = MibTableColumn
sensorGroupStatusUpdatingSensorIndex = _SensorGroupStatusUpdatingSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 15),
    _SensorGroupStatusUpdatingSensorIndex_Type()
)
sensorGroupStatusUpdatingSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusUpdatingSensorIndex.setStatus("current")


class _SensorGroupStatusCacheStatus_Type(Integer32):
    """Custom type sensorGroupStatusCacheStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disabled", 1),
          ("pending", 2),
          ("saved", 3),
          ("failed", 4))
    )


_SensorGroupStatusCacheStatus_Type.__name__ = "Integer32"
_SensorGroupStatusCacheStatus_Object = MibTableColumn
sensorGroupStatusCacheStatus = _SensorGroupStatusCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 16),
    _SensorGroupStatusCacheStatus_Type()
)
sensorGroupStatusCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusCacheStatus.setStatus("current")
_SensorGroupStatusLastUpdate_Type = Counter32
_SensorGroupStatusLastUpdate_Object = MibTableColumn
sensorGroupStatusLastUpdate = _SensorGroupStatusLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 4, 99, 104, 1, 17),
    _SensorGroupStatusLastUpdate_Type()
)
sensorGroupStatusLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorGroupStatusLastUpdate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-SMARTOFFICE-MIB",
    **{"device": device,
       "smartoffice": smartoffice,
       "smartofficeEnableSmartOffice": smartofficeEnableSmartOffice,
       "directorConfigTable": directorConfigTable,
       "directorConfigEntry": directorConfigEntry,
       "directorConfigIndex": directorConfigIndex,
       "directorConfigDomainName": directorConfigDomainName,
       "directorConfigGeneralMode": directorConfigGeneralMode,
       "directorConfigActOnUngroupedSensors": directorConfigActOnUngroupedSensors,
       "directorConfigScanLightControllers": directorConfigScanLightControllers,
       "deviceConfigTable": deviceConfigTable,
       "deviceConfigEntry": deviceConfigEntry,
       "deviceConfigIndex": deviceConfigIndex,
       "deviceConfigDeviceName": deviceConfigDeviceName,
       "deviceConfigLocation": deviceConfigLocation,
       "deviceConfigLatitude": deviceConfigLatitude,
       "deviceConfigLongitude": deviceConfigLongitude,
       "deviceConfigAltitude": deviceConfigAltitude,
       "deviceConfigPlacement": deviceConfigPlacement,
       "deviceConfigProductType": deviceConfigProductType,
       "deviceConfigDeviceId": deviceConfigDeviceId,
       "deviceConfigNetworkAddress": deviceConfigNetworkAddress,
       "deviceConfigAdditionalParameter": deviceConfigAdditionalParameter,
       "deviceConfigNetworkFailureAction": deviceConfigNetworkFailureAction,
       "deviceConfigIdentify": deviceConfigIdentify,
       "deviceConfigRestart": deviceConfigRestart,
       "deviceConfigCalibrate": deviceConfigCalibrate,
       "deviceConfigPair": deviceConfigPair,
       "deviceConfigUnpair": deviceConfigUnpair,
       "deviceConfigUpdateFirmware": deviceConfigUpdateFirmware,
       "actorGroupConfigTable": actorGroupConfigTable,
       "actorGroupConfigEntry": actorGroupConfigEntry,
       "actorGroupConfigIndex": actorGroupConfigIndex,
       "actorGroupConfigGroupName": actorGroupConfigGroupName,
       "actorGroupConfigAttribute": actorGroupConfigAttribute,
       "actorGroupConfigAssociatedDevices": actorGroupConfigAssociatedDevices,
       "actorGroupConfigAdditionalParameter": actorGroupConfigAdditionalParameter,
       "actorGroupConfigDefaultValue": actorGroupConfigDefaultValue,
       "actorGroupConfigValueCaching": actorGroupConfigValueCaching,
       "actorGroupConfigAdditionalScriptName": actorGroupConfigAdditionalScriptName,
       "actorGroupConfigManualSetValue": actorGroupConfigManualSetValue,
       "sensorGroupConfigTable": sensorGroupConfigTable,
       "sensorGroupConfigEntry": sensorGroupConfigEntry,
       "sensorGroupConfigIndex": sensorGroupConfigIndex,
       "sensorGroupConfigGroupName": sensorGroupConfigGroupName,
       "sensorGroupConfigAttribute": sensorGroupConfigAttribute,
       "sensorGroupConfigAssociatedDevices": sensorGroupConfigAssociatedDevices,
       "sensorGroupConfigValueCaching": sensorGroupConfigValueCaching,
       "sensorGroupConfigRunScriptWhen": sensorGroupConfigRunScriptWhen,
       "sensorGroupConfigRunScriptDelta": sensorGroupConfigRunScriptDelta,
       "sensorGroupConfigScriptName": sensorGroupConfigScriptName,
       "sensorGroupConfigAdditionalScriptName": sensorGroupConfigAdditionalScriptName,
       "sensorGroupConfigReportMode": sensorGroupConfigReportMode,
       "sensorGroupConfigAdditionalParameter": sensorGroupConfigAdditionalParameter,
       "sensorGroupConfigLowerBoundary": sensorGroupConfigLowerBoundary,
       "sensorGroupConfigUpperBoundary": sensorGroupConfigUpperBoundary,
       "sensorGroupConfigBoundaryHysteresis": sensorGroupConfigBoundaryHysteresis,
       "sensorGroupConfigUpdateDelta": sensorGroupConfigUpdateDelta,
       "sensorGroupConfigRateLimit": sensorGroupConfigRateLimit,
       "sensorGroupConfigClearValues": sensorGroupConfigClearValues,
       "deviceInformationTable": deviceInformationTable,
       "deviceInformationEntry": deviceInformationEntry,
       "deviceInformationIndex": deviceInformationIndex,
       "deviceInformationName": deviceInformationName,
       "deviceInformationHardwareId": deviceInformationHardwareId,
       "deviceInformationDeviceType": deviceInformationDeviceType,
       "deviceInformationOperationalState": deviceInformationOperationalState,
       "deviceInformationActorAttributes": deviceInformationActorAttributes,
       "deviceInformationSensorAttributes": deviceInformationSensorAttributes,
       "deviceInformationVendorName": deviceInformationVendorName,
       "deviceInformationArticleNumber": deviceInformationArticleNumber,
       "deviceInformationSerialNumber": deviceInformationSerialNumber,
       "deviceInformationHardwareRevision": deviceInformationHardwareRevision,
       "deviceInformationSoftwareVersion": deviceInformationSoftwareVersion,
       "deviceInformationAdditionalInfo": deviceInformationAdditionalInfo,
       "actorListTable": actorListTable,
       "actorListEntry": actorListEntry,
       "actorListIndex": actorListIndex,
       "actorListDevice": actorListDevice,
       "actorListInstance": actorListInstance,
       "actorListAttribute": actorListAttribute,
       "actorListAssociatedGroups": actorListAssociatedGroups,
       "actorListValue": actorListValue,
       "actorListActorState": actorListActorState,
       "actorListLastUpdate": actorListLastUpdate,
       "sensorListTable": sensorListTable,
       "sensorListEntry": sensorListEntry,
       "sensorListIndex": sensorListIndex,
       "sensorListDevice": sensorListDevice,
       "sensorListInstance": sensorListInstance,
       "sensorListAttribute": sensorListAttribute,
       "sensorListAssociatedGroups": sensorListAssociatedGroups,
       "sensorListValue": sensorListValue,
       "sensorListSensorState": sensorListSensorState,
       "sensorListLastUpdate": sensorListLastUpdate,
       "actorGroupStatusTable": actorGroupStatusTable,
       "actorGroupStatusEntry": actorGroupStatusEntry,
       "actorGroupStatusIndex": actorGroupStatusIndex,
       "actorGroupStatusGroupName": actorGroupStatusGroupName,
       "actorGroupStatusAttribute": actorGroupStatusAttribute,
       "actorGroupStatusNumAssignedActors": actorGroupStatusNumAssignedActors,
       "actorGroupStatusNumFailedActors": actorGroupStatusNumFailedActors,
       "actorGroupStatusGroupState": actorGroupStatusGroupState,
       "actorGroupStatusValue": actorGroupStatusValue,
       "actorGroupStatusActivePriority": actorGroupStatusActivePriority,
       "actorGroupStatusPriorityValueChain": actorGroupStatusPriorityValueChain,
       "actorGroupStatusCacheStatus": actorGroupStatusCacheStatus,
       "actorGroupStatusLastUpdate": actorGroupStatusLastUpdate,
       "sensorGroupStatusTable": sensorGroupStatusTable,
       "sensorGroupStatusEntry": sensorGroupStatusEntry,
       "sensorGroupStatusIndex": sensorGroupStatusIndex,
       "sensorGroupStatusGroupName": sensorGroupStatusGroupName,
       "sensorGroupStatusAttribute": sensorGroupStatusAttribute,
       "sensorGroupStatusNumAssignedSensors": sensorGroupStatusNumAssignedSensors,
       "sensorGroupStatusNumFailedSensors": sensorGroupStatusNumFailedSensors,
       "sensorGroupStatusGroupState": sensorGroupStatusGroupState,
       "sensorGroupStatusMinimumPeakHold": sensorGroupStatusMinimumPeakHold,
       "sensorGroupStatusMinimumValue": sensorGroupStatusMinimumValue,
       "sensorGroupStatusAverageValue": sensorGroupStatusAverageValue,
       "sensorGroupStatusMaximumValue": sensorGroupStatusMaximumValue,
       "sensorGroupStatusMaximumPeakHold": sensorGroupStatusMaximumPeakHold,
       "sensorGroupStatusTotalValue": sensorGroupStatusTotalValue,
       "sensorGroupStatusLowerBoundaryReached": sensorGroupStatusLowerBoundaryReached,
       "sensorGroupStatusUpperBoundaryReached": sensorGroupStatusUpperBoundaryReached,
       "sensorGroupStatusUpdatingSensorIndex": sensorGroupStatusUpdatingSensorIndex,
       "sensorGroupStatusCacheStatus": sensorGroupStatusCacheStatus,
       "sensorGroupStatusLastUpdate": sensorGroupStatusLastUpdate}
)
