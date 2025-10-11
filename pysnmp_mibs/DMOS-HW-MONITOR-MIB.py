# SNMP MIB module (DMOS-HW-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DMOS-HW-MONITOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:47 2025
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

(datacomDevicesMIBs,) = mibBuilder.importSymbols(
    "DATACOM-SMI",
    "datacomDevicesMIBs")

(UnsignedPercent,) = mibBuilder.importSymbols(
    "DMOS-TC-MIB",
    "UnsignedPercent")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dmosHwMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6)
)
if mibBuilder.loadTexts:
    dmosHwMonitorMIB.setRevisions(
        ("2017-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnvironmentSensorTemperature(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class EnvironmentSensorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", -2),
          ("error", -1),
          ("normal", 0),
          ("high", 1),
          ("low", 2),
          ("critical", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Environment_ObjectIdentity = ObjectIdentity
environment = _Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1)
)
_EnvironmentChassisTable_Object = MibTable
environmentChassisTable = _EnvironmentChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 1)
)
if mibBuilder.loadTexts:
    environmentChassisTable.setStatus("current")
_EnvironmentChassisEntry_Object = MibTableRow
environmentChassisEntry = _EnvironmentChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 1, 1)
)
environmentChassisEntry.setIndexNames(
    (0, "DMOS-HW-MONITOR-MIB", "environmentChassisId"),
)
if mibBuilder.loadTexts:
    environmentChassisEntry.setStatus("current")
_EnvironmentChassisId_Type = Unsigned32
_EnvironmentChassisId_Object = MibTableColumn
environmentChassisId = _EnvironmentChassisId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 1, 1, 1),
    _EnvironmentChassisId_Type()
)
environmentChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentChassisId.setStatus("current")
_EnvironmentSlotTable_Object = MibTable
environmentSlotTable = _EnvironmentSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 2)
)
if mibBuilder.loadTexts:
    environmentSlotTable.setStatus("current")
_EnvironmentSlotEntry_Object = MibTableRow
environmentSlotEntry = _EnvironmentSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 2, 1)
)
environmentSlotEntry.setIndexNames(
    (0, "DMOS-HW-MONITOR-MIB", "environmentChassisId"),
    (0, "DMOS-HW-MONITOR-MIB", "environmentSlotId"),
)
if mibBuilder.loadTexts:
    environmentSlotEntry.setStatus("current")
_EnvironmentSlotId_Type = DisplayString
_EnvironmentSlotId_Object = MibTableColumn
environmentSlotId = _EnvironmentSlotId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 2, 1, 1),
    _EnvironmentSlotId_Type()
)
environmentSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentSlotId.setStatus("current")
_TemperatureSensorTable_Object = MibTable
temperatureSensorTable = _TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3)
)
if mibBuilder.loadTexts:
    temperatureSensorTable.setStatus("current")
_TemperatureSensorEntry_Object = MibTableRow
temperatureSensorEntry = _TemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3, 1)
)
temperatureSensorEntry.setIndexNames(
    (0, "DMOS-HW-MONITOR-MIB", "environmentChassisId"),
    (0, "DMOS-HW-MONITOR-MIB", "environmentSlotId"),
    (0, "DMOS-HW-MONITOR-MIB", "temperatureSensorId"),
)
if mibBuilder.loadTexts:
    temperatureSensorEntry.setStatus("current")
_TemperatureSensorId_Type = DisplayString
_TemperatureSensorId_Object = MibTableColumn
temperatureSensorId = _TemperatureSensorId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3, 1, 1),
    _TemperatureSensorId_Type()
)
temperatureSensorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temperatureSensorId.setStatus("current")
_TemperatureSensorDescription_Type = DisplayString
_TemperatureSensorDescription_Object = MibTableColumn
temperatureSensorDescription = _TemperatureSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3, 1, 2),
    _TemperatureSensorDescription_Type()
)
temperatureSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorDescription.setStatus("current")
_TemperatureSensorMaxTemperature_Type = EnvironmentSensorTemperature
_TemperatureSensorMaxTemperature_Object = MibTableColumn
temperatureSensorMaxTemperature = _TemperatureSensorMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3, 1, 3),
    _TemperatureSensorMaxTemperature_Type()
)
temperatureSensorMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    temperatureSensorMaxTemperature.setUnits("C")
_TemperatureSensorMinTemperature_Type = EnvironmentSensorTemperature
_TemperatureSensorMinTemperature_Object = MibTableColumn
temperatureSensorMinTemperature = _TemperatureSensorMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3, 1, 4),
    _TemperatureSensorMinTemperature_Type()
)
temperatureSensorMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    temperatureSensorMinTemperature.setUnits("C")
_TemperatureSensorHysteresis_Type = EnvironmentSensorTemperature
_TemperatureSensorHysteresis_Object = MibTableColumn
temperatureSensorHysteresis = _TemperatureSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3, 1, 5),
    _TemperatureSensorHysteresis_Type()
)
temperatureSensorHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    temperatureSensorHysteresis.setUnits("C")
_TemperatureSensorCurrentTemperature_Type = EnvironmentSensorTemperature
_TemperatureSensorCurrentTemperature_Object = MibTableColumn
temperatureSensorCurrentTemperature = _TemperatureSensorCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3, 1, 6),
    _TemperatureSensorCurrentTemperature_Type()
)
temperatureSensorCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorCurrentTemperature.setStatus("current")
if mibBuilder.loadTexts:
    temperatureSensorCurrentTemperature.setUnits("C")
_TemperatureSensorTemperatureReadError_Type = TruthValue
_TemperatureSensorTemperatureReadError_Object = MibTableColumn
temperatureSensorTemperatureReadError = _TemperatureSensorTemperatureReadError_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3, 1, 7),
    _TemperatureSensorTemperatureReadError_Type()
)
temperatureSensorTemperatureReadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorTemperatureReadError.setStatus("current")
_TemperatureSensorTemperatureStatus_Type = EnvironmentSensorStatus
_TemperatureSensorTemperatureStatus_Object = MibTableColumn
temperatureSensorTemperatureStatus = _TemperatureSensorTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 3, 1, 8),
    _TemperatureSensorTemperatureStatus_Type()
)
temperatureSensorTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorTemperatureStatus.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 4)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 4, 1)
)
fanEntry.setIndexNames(
    (0, "DMOS-HW-MONITOR-MIB", "environmentChassisId"),
    (0, "DMOS-HW-MONITOR-MIB", "environmentSlotId"),
    (0, "DMOS-HW-MONITOR-MIB", "fanId"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")
_FanId_Type = DisplayString
_FanId_Object = MibTableColumn
fanId = _FanId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 4, 1, 1),
    _FanId_Type()
)
fanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanId.setStatus("current")
_FanDescription_Type = DisplayString
_FanDescription_Object = MibTableColumn
fanDescription = _FanDescription_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 4, 1, 2),
    _FanDescription_Type()
)
fanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDescription.setStatus("current")
_FanControl_Type = UnsignedPercent
_FanControl_Object = MibTableColumn
fanControl = _FanControl_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 4, 1, 3),
    _FanControl_Type()
)
fanControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanControl.setStatus("current")
if mibBuilder.loadTexts:
    fanControl.setUnits("%")
_FanSpeed_Type = Unsigned32
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 4, 1, 4),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fanSpeed.setUnits("RPM")
_FanSpeedReadError_Type = TruthValue
_FanSpeedReadError_Object = MibTableColumn
fanSpeedReadError = _FanSpeedReadError_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 4, 1, 5),
    _FanSpeedReadError_Type()
)
fanSpeedReadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedReadError.setStatus("current")
_FanSpeedStatus_Type = EnvironmentSensorStatus
_FanSpeedStatus_Object = MibTableColumn
fanSpeedStatus = _FanSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 4, 1, 6),
    _FanSpeedStatus_Type()
)
fanSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedStatus.setStatus("current")
_PsuTable_Object = MibTable
psuTable = _PsuTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 5)
)
if mibBuilder.loadTexts:
    psuTable.setStatus("current")
_PsuEntry_Object = MibTableRow
psuEntry = _PsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 5, 1)
)
psuEntry.setIndexNames(
    (1, "DMOS-HW-MONITOR-MIB", "psuId"),
)
if mibBuilder.loadTexts:
    psuEntry.setStatus("current")
_PsuId_Type = DisplayString
_PsuId_Object = MibTableColumn
psuId = _PsuId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 5, 1, 1),
    _PsuId_Type()
)
psuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psuId.setStatus("current")


class _PsuStatus_Type(Integer32):
    """Custom type psuStatus based on Integer32"""
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
        *(("ok", 0),
          ("powerInputFailure", 1),
          ("fuseFailure", 2),
          ("error", 3))
    )


_PsuStatus_Type.__name__ = "Integer32"
_PsuStatus_Object = MibTableColumn
psuStatus = _PsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 6, 1, 5, 1, 2),
    _PsuStatus_Type()
)
psuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMOS-HW-MONITOR-MIB",
    **{"EnvironmentSensorTemperature": EnvironmentSensorTemperature,
       "EnvironmentSensorStatus": EnvironmentSensorStatus,
       "dmosHwMonitorMIB": dmosHwMonitorMIB,
       "environment": environment,
       "environmentChassisTable": environmentChassisTable,
       "environmentChassisEntry": environmentChassisEntry,
       "environmentChassisId": environmentChassisId,
       "environmentSlotTable": environmentSlotTable,
       "environmentSlotEntry": environmentSlotEntry,
       "environmentSlotId": environmentSlotId,
       "temperatureSensorTable": temperatureSensorTable,
       "temperatureSensorEntry": temperatureSensorEntry,
       "temperatureSensorId": temperatureSensorId,
       "temperatureSensorDescription": temperatureSensorDescription,
       "temperatureSensorMaxTemperature": temperatureSensorMaxTemperature,
       "temperatureSensorMinTemperature": temperatureSensorMinTemperature,
       "temperatureSensorHysteresis": temperatureSensorHysteresis,
       "temperatureSensorCurrentTemperature": temperatureSensorCurrentTemperature,
       "temperatureSensorTemperatureReadError": temperatureSensorTemperatureReadError,
       "temperatureSensorTemperatureStatus": temperatureSensorTemperatureStatus,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanId": fanId,
       "fanDescription": fanDescription,
       "fanControl": fanControl,
       "fanSpeed": fanSpeed,
       "fanSpeedReadError": fanSpeedReadError,
       "fanSpeedStatus": fanSpeedStatus,
       "psuTable": psuTable,
       "psuEntry": psuEntry,
       "psuId": psuId,
       "psuStatus": psuStatus}
)
