# SNMP MIB module (CHECKPOINT-GAIA-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/checkpoint/CHECKPOINT-GAIA-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:21:43 2025
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

(fanSpeedSensorName,
 fanSpeedSensorValue,
 powerSupplyIndex,
 powerSupplyStatus,
 raidVolumeFlags,
 raidVolumeState,
 tempertureSensorName,
 tempertureSensorValue,
 voltageSensorName,
 voltageSensorValue) = mibBuilder.importSymbols(
    "CHECKPOINT-MIB",
    "fanSpeedSensorName",
    "fanSpeedSensorValue",
    "powerSupplyIndex",
    "powerSupplyStatus",
    "raidVolumeFlags",
    "raidVolumeState",
    "tempertureSensorName",
    "tempertureSensorValue",
    "voltageSensorName",
    "voltageSensorValue")

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

chkpntGaiaTrapMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0, 0)
)
if mibBuilder.loadTexts:
    chkpntGaiaTrapMibModule.setRevisions(
        ("2010-05-10 14:31",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Checkpoint_ObjectIdentity = ObjectIdentity
checkpoint = _Checkpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1)
)
_Svn_ObjectIdentity = ObjectIdentity
svn = _Svn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6)
)
_SvnPerf_ObjectIdentity = ObjectIdentity
svnPerf = _SvnPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7)
)
_RaidInfo_ObjectIdentity = ObjectIdentity
raidInfo = _RaidInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6)
)
_RaidVolumeTable_ObjectIdentity = ObjectIdentity
raidVolumeTable = _RaidVolumeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1)
)
_RaidVolumeEntry_ObjectIdentity = ObjectIdentity
raidVolumeEntry = _RaidVolumeEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 1)
)
_RaidVolumeState_Type = DisplayString
_RaidVolumeState_Object = MibScalar
raidVolumeState = _RaidVolumeState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 1, 6),
    _RaidVolumeState_Type()
)
raidVolumeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeState.setStatus("current")
_RaidVolumeFlags_Type = DisplayString
_RaidVolumeFlags_Object = MibScalar
raidVolumeFlags = _RaidVolumeFlags_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 1, 7),
    _RaidVolumeFlags_Type()
)
raidVolumeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeFlags.setStatus("current")
_SensorInfo_ObjectIdentity = ObjectIdentity
sensorInfo = _SensorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8)
)
_TempertureSensorTable_ObjectIdentity = ObjectIdentity
tempertureSensorTable = _TempertureSensorTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1)
)
_TempertureSensorEntry_ObjectIdentity = ObjectIdentity
tempertureSensorEntry = _TempertureSensorEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1)
)
_TempertureSensorName_Type = DisplayString
_TempertureSensorName_Object = MibScalar
tempertureSensorName = _TempertureSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 2),
    _TempertureSensorName_Type()
)
tempertureSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorName.setStatus("current")
_TempertureSensorValue_Type = DisplayString
_TempertureSensorValue_Object = MibScalar
tempertureSensorValue = _TempertureSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 3),
    _TempertureSensorValue_Type()
)
tempertureSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorValue.setStatus("current")
_FanSpeedSensorTable_ObjectIdentity = ObjectIdentity
fanSpeedSensorTable = _FanSpeedSensorTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2)
)
_FanSpeedSensorEntry_ObjectIdentity = ObjectIdentity
fanSpeedSensorEntry = _FanSpeedSensorEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1)
)
_FanSpeedSensorName_Type = DisplayString
_FanSpeedSensorName_Object = MibScalar
fanSpeedSensorName = _FanSpeedSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 2),
    _FanSpeedSensorName_Type()
)
fanSpeedSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorName.setStatus("current")
_FanSpeedSensorValue_Type = DisplayString
_FanSpeedSensorValue_Object = MibScalar
fanSpeedSensorValue = _FanSpeedSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 3),
    _FanSpeedSensorValue_Type()
)
fanSpeedSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorValue.setStatus("current")
_VoltageSensorTable_ObjectIdentity = ObjectIdentity
voltageSensorTable = _VoltageSensorTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3)
)
_VoltageSensorEntry_ObjectIdentity = ObjectIdentity
voltageSensorEntry = _VoltageSensorEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1)
)
_VoltageSensorName_Type = DisplayString
_VoltageSensorName_Object = MibScalar
voltageSensorName = _VoltageSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 2),
    _VoltageSensorName_Type()
)
voltageSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorName.setStatus("current")
_VoltageSensorValue_Type = DisplayString
_VoltageSensorValue_Object = MibScalar
voltageSensorValue = _VoltageSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 3),
    _VoltageSensorValue_Type()
)
voltageSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValue.setStatus("current")
_PowerSupplyInfo_ObjectIdentity = ObjectIdentity
powerSupplyInfo = _PowerSupplyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9)
)
_PowerSupplyTable_ObjectIdentity = ObjectIdentity
powerSupplyTable = _PowerSupplyTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1)
)
_PowerSupplyEntry_ObjectIdentity = ObjectIdentity
powerSupplyEntry = _PowerSupplyEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1, 1)
)
_PowerSupplyIndex_Type = DisplayString
_PowerSupplyIndex_Object = MibScalar
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1, 1, 2),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("current")
_PowerSupplyStatus_Type = DisplayString
_PowerSupplyStatus_Object = MibScalar
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1, 1, 3),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("current")
_ChkpntGaiaTrap_ObjectIdentity = ObjectIdentity
chkpntGaiaTrap = _ChkpntGaiaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000)
)
_ChkpntGaiaTrapInfo_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapInfo = _ChkpntGaiaTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0)
)
_ChkpntGaiaTrapOID_Type = DisplayString
_ChkpntGaiaTrapOID_Object = MibScalar
chkpntGaiaTrapOID = _ChkpntGaiaTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0, 10),
    _ChkpntGaiaTrapOID_Type()
)
chkpntGaiaTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntGaiaTrapOID.setStatus("current")
_ChkpntGaiaTrapMsgText_Type = DisplayString
_ChkpntGaiaTrapMsgText_Object = MibScalar
chkpntGaiaTrapMsgText = _ChkpntGaiaTrapMsgText_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0, 12),
    _ChkpntGaiaTrapMsgText_Type()
)
chkpntGaiaTrapMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntGaiaTrapMsgText.setStatus("current")


class _ChkpntGaiaTrapChassisId_Type(Integer32):
    """Custom type chkpntGaiaTrapChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChkpntGaiaTrapChassisId_Type.__name__ = "Integer32"
_ChkpntGaiaTrapChassisId_Object = MibScalar
chkpntGaiaTrapChassisId = _ChkpntGaiaTrapChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0, 15),
    _ChkpntGaiaTrapChassisId_Type()
)
chkpntGaiaTrapChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntGaiaTrapChassisId.setStatus("current")


class _ChkpntGaiaTrapBladeId_Type(Integer32):
    """Custom type chkpntGaiaTrapBladeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChkpntGaiaTrapBladeId_Type.__name__ = "Integer32"
_ChkpntGaiaTrapBladeId_Object = MibScalar
chkpntGaiaTrapBladeId = _ChkpntGaiaTrapBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0, 16),
    _ChkpntGaiaTrapBladeId_Type()
)
chkpntGaiaTrapBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntGaiaTrapBladeId.setStatus("current")
_ChkpntGaiaTrapDisk_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapDisk = _ChkpntGaiaTrapDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 2)
)
_ChkpntGaiaTrapRAID_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapRAID = _ChkpntGaiaTrapRAID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 2, 1)
)
_ChkpntGaiaTrapHWSensor_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapHWSensor = _ChkpntGaiaTrapHWSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5)
)
_ChkpntGaiaTrapTempertureSensor_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapTempertureSensor = _ChkpntGaiaTrapTempertureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 1)
)
_ChkpntGaiaTrapFanSpeedSensor_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapFanSpeedSensor = _ChkpntGaiaTrapFanSpeedSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 2)
)
_ChkpntGaiaTrapVoltageSensor_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapVoltageSensor = _ChkpntGaiaTrapVoltageSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 3)
)
_ChkpntGaiaTrapPowerSupplySensor_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapPowerSupplySensor = _ChkpntGaiaTrapPowerSupplySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 4)
)
_ChkpntGaiaTrapConfiguration_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapConfiguration = _ChkpntGaiaTrapConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 10)
)
_ChkpntGaiaTrapSystemConfiguration_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapSystemConfiguration = _ChkpntGaiaTrapSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 10, 1)
)
_ChkpntBios_ObjectIdentity = ObjectIdentity
chkpntBios = _ChkpntBios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 20)
)
_ChkpntGaiaTrapMIBConformance_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapMIBConformance = _ChkpntGaiaTrapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 2)
)
_ChkpntGaiaTrapMIBCompliances_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapMIBCompliances = _ChkpntGaiaTrapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 2, 1)
)
_ChkpntGaiaTrapMIBGroups_ObjectIdentity = ObjectIdentity
chkpntGaiaTrapMIBGroups = _ChkpntGaiaTrapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 2, 2)
)
_ChkpntGaiaNotificationGroups_ObjectIdentity = ObjectIdentity
chkpntGaiaNotificationGroups = _ChkpntGaiaNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 2, 3)
)

# Managed Objects groups

chkpntGaiaTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2620, 2, 2, 1)
)
chkpntGaiaTrapGroup.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapOID"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapMsgText"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapChassisId"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapBladeId"),
        ("CHECKPOINT-MIB", "tempertureSensorName"),
        ("CHECKPOINT-MIB", "tempertureSensorValue"),
        ("CHECKPOINT-MIB", "fanSpeedSensorName"),
        ("CHECKPOINT-MIB", "fanSpeedSensorValue"),
        ("CHECKPOINT-MIB", "voltageSensorName"),
        ("CHECKPOINT-MIB", "voltageSensorValue"),
        ("CHECKPOINT-MIB", "powerSupplyIndex"),
        ("CHECKPOINT-MIB", "powerSupplyStatus"),
        ("CHECKPOINT-MIB", "raidVolumeState"),
        ("CHECKPOINT-MIB", "raidVolumeFlags"))
)
if mibBuilder.loadTexts:
    chkpntGaiaTrapGroup.setStatus("current")


# Notification objects

chkpntRAIDVolumeStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 2, 1, 1)
)
chkpntRAIDVolumeStateTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapOID"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapMsgText"),
        ("CHECKPOINT-MIB", "raidVolumeState"),
        ("CHECKPOINT-MIB", "raidVolumeFlags"))
)
if mibBuilder.loadTexts:
    chkpntRAIDVolumeStateTrap.setStatus(
        "current"
    )

chkpntTempertureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 1, 1)
)
chkpntTempertureTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapOID"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapMsgText"),
        ("CHECKPOINT-MIB", "tempertureSensorName"),
        ("CHECKPOINT-MIB", "tempertureSensorValue"))
)
if mibBuilder.loadTexts:
    chkpntTempertureTrap.setStatus(
        "current"
    )

chkpntFanSpeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 2, 1)
)
chkpntFanSpeedTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapOID"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapMsgText"),
        ("CHECKPOINT-MIB", "fanSpeedSensorName"),
        ("CHECKPOINT-MIB", "fanSpeedSensorValue"))
)
if mibBuilder.loadTexts:
    chkpntFanSpeedTrap.setStatus(
        "current"
    )

chkpntVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 3, 1)
)
chkpntVoltageTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapOID"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapMsgText"),
        ("CHECKPOINT-MIB", "voltageSensorName"),
        ("CHECKPOINT-MIB", "voltageSensorValue"))
)
if mibBuilder.loadTexts:
    chkpntVoltageTrap.setStatus(
        "current"
    )

chkpntPowerSupplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 4, 1)
)
chkpntPowerSupplyTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapOID"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapMsgText"),
        ("CHECKPOINT-MIB", "powerSupplyIndex"),
        ("CHECKPOINT-MIB", "powerSupplyStatus"))
)
if mibBuilder.loadTexts:
    chkpntPowerSupplyTrap.setStatus(
        "current"
    )

chkpntSystemConfigurationChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 10, 1, 1)
)
chkpntSystemConfigurationChangeTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapOID"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapMsgText"))
)
if mibBuilder.loadTexts:
    chkpntSystemConfigurationChangeTrap.setStatus(
        "current"
    )

chkpntSystemConfigurationSaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 10, 1, 2)
)
chkpntSystemConfigurationSaveTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapOID"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapMsgText"))
)
if mibBuilder.loadTexts:
    chkpntSystemConfigurationSaveTrap.setStatus(
        "current"
    )

chkpntBiosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 20, 1)
)
chkpntBiosTrap.setObjects(
    ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapMsgText")
)
if mibBuilder.loadTexts:
    chkpntBiosTrap.setStatus(
        "current"
    )


# Notifications groups

chkpntGaiaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2620, 2, 3, 1)
)
chkpntGaiaNotificationGroup.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntTempertureTrap"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntFanSpeedTrap"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntVoltageTrap"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntPowerSupplyTrap"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntSystemConfigurationChangeTrap"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntSystemConfigurationSaveTrap"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntBiosTrap"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntRAIDVolumeStateTrap"))
)
if mibBuilder.loadTexts:
    chkpntGaiaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

chkpntGaiaTrapBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2620, 2, 1, 1)
)
chkpntGaiaTrapBasicCompliance.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaTrapGroup"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntGaiaNotificationGroup"))
)
if mibBuilder.loadTexts:
    chkpntGaiaTrapBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHECKPOINT-GAIA-TRAP-MIB",
    **{"checkpoint": checkpoint,
       "products": products,
       "svn": svn,
       "svnPerf": svnPerf,
       "raidInfo": raidInfo,
       "raidVolumeTable": raidVolumeTable,
       "raidVolumeEntry": raidVolumeEntry,
       "raidVolumeState": raidVolumeState,
       "raidVolumeFlags": raidVolumeFlags,
       "sensorInfo": sensorInfo,
       "tempertureSensorTable": tempertureSensorTable,
       "tempertureSensorEntry": tempertureSensorEntry,
       "tempertureSensorName": tempertureSensorName,
       "tempertureSensorValue": tempertureSensorValue,
       "fanSpeedSensorTable": fanSpeedSensorTable,
       "fanSpeedSensorEntry": fanSpeedSensorEntry,
       "fanSpeedSensorName": fanSpeedSensorName,
       "fanSpeedSensorValue": fanSpeedSensorValue,
       "voltageSensorTable": voltageSensorTable,
       "voltageSensorEntry": voltageSensorEntry,
       "voltageSensorName": voltageSensorName,
       "voltageSensorValue": voltageSensorValue,
       "powerSupplyInfo": powerSupplyInfo,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyStatus": powerSupplyStatus,
       "chkpntGaiaTrap": chkpntGaiaTrap,
       "chkpntGaiaTrapInfo": chkpntGaiaTrapInfo,
       "chkpntGaiaTrapMibModule": chkpntGaiaTrapMibModule,
       "chkpntGaiaTrapOID": chkpntGaiaTrapOID,
       "chkpntGaiaTrapMsgText": chkpntGaiaTrapMsgText,
       "chkpntGaiaTrapChassisId": chkpntGaiaTrapChassisId,
       "chkpntGaiaTrapBladeId": chkpntGaiaTrapBladeId,
       "chkpntGaiaTrapDisk": chkpntGaiaTrapDisk,
       "chkpntGaiaTrapRAID": chkpntGaiaTrapRAID,
       "chkpntRAIDVolumeStateTrap": chkpntRAIDVolumeStateTrap,
       "chkpntGaiaTrapHWSensor": chkpntGaiaTrapHWSensor,
       "chkpntGaiaTrapTempertureSensor": chkpntGaiaTrapTempertureSensor,
       "chkpntTempertureTrap": chkpntTempertureTrap,
       "chkpntGaiaTrapFanSpeedSensor": chkpntGaiaTrapFanSpeedSensor,
       "chkpntFanSpeedTrap": chkpntFanSpeedTrap,
       "chkpntGaiaTrapVoltageSensor": chkpntGaiaTrapVoltageSensor,
       "chkpntVoltageTrap": chkpntVoltageTrap,
       "chkpntGaiaTrapPowerSupplySensor": chkpntGaiaTrapPowerSupplySensor,
       "chkpntPowerSupplyTrap": chkpntPowerSupplyTrap,
       "chkpntGaiaTrapConfiguration": chkpntGaiaTrapConfiguration,
       "chkpntGaiaTrapSystemConfiguration": chkpntGaiaTrapSystemConfiguration,
       "chkpntSystemConfigurationChangeTrap": chkpntSystemConfigurationChangeTrap,
       "chkpntSystemConfigurationSaveTrap": chkpntSystemConfigurationSaveTrap,
       "chkpntBios": chkpntBios,
       "chkpntBiosTrap": chkpntBiosTrap,
       "chkpntGaiaTrapMIBConformance": chkpntGaiaTrapMIBConformance,
       "chkpntGaiaTrapMIBCompliances": chkpntGaiaTrapMIBCompliances,
       "chkpntGaiaTrapBasicCompliance": chkpntGaiaTrapBasicCompliance,
       "chkpntGaiaTrapMIBGroups": chkpntGaiaTrapMIBGroups,
       "chkpntGaiaTrapGroup": chkpntGaiaTrapGroup,
       "chkpntGaiaNotificationGroups": chkpntGaiaNotificationGroups,
       "chkpntGaiaNotificationGroup": chkpntGaiaNotificationGroup}
)
