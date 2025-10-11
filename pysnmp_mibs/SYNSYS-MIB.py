# SNMP MIB module (SYNSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synaccess/SYNSYS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:14:20 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

synSys = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 3)
)
if mibBuilder.loadTexts:
    synSys.setRevisions(
        ("2020-03-20 00:00",
         "2015-05-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synaccess_ObjectIdentity = ObjectIdentity
synaccess = _Synaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728)
)
_SystemDescr_ObjectIdentity = ObjectIdentity
systemDescr = _SystemDescr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1)
)


class _SystemModel_Type(DisplayString):
    """Custom type systemModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SystemModel_Type.__name__ = "DisplayString"
_SystemModel_Object = MibScalar
systemModel = _SystemModel_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1, 1),
    _SystemModel_Type()
)
systemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemModel.setStatus("current")


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1, 2),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _PowerOutletNum_Type(Integer32):
    """Custom type powerOutletNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PowerOutletNum_Type.__name__ = "Integer32"
_PowerOutletNum_Object = MibScalar
powerOutletNum = _PowerOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1, 3),
    _PowerOutletNum_Type()
)
powerOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOutletNum.setStatus("current")


class _SerialPortNum_Type(Integer32):
    """Custom type serialPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SerialPortNum_Type.__name__ = "Integer32"
_SerialPortNum_Object = MibScalar
serialPortNum = _SerialPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1, 4),
    _SerialPortNum_Type()
)
serialPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortNum.setStatus("current")
_SystemUpTime_Type = Integer32
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1, 5),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("current")


class _SwVersion_Type(DisplayString):
    """Custom type swVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwVersion_Type.__name__ = "DisplayString"
_SwVersion_Object = MibScalar
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1, 6),
    _SwVersion_Type()
)
swVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersion.setStatus("current")


class _AcCurrentSensorNumber_Type(Integer32):
    """Custom type acCurrentSensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AcCurrentSensorNumber_Type.__name__ = "Integer32"
_AcCurrentSensorNumber_Object = MibScalar
acCurrentSensorNumber = _AcCurrentSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1, 7),
    _AcCurrentSensorNumber_Type()
)
acCurrentSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acCurrentSensorNumber.setStatus("current")


class _TemperatureProbe_Type(Integer32):
    """Custom type temperatureProbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TemperatureProbe_Type.__name__ = "Integer32"
_TemperatureProbe_Object = MibScalar
temperatureProbe = _TemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1, 8),
    _TemperatureProbe_Type()
)
temperatureProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbe.setStatus("current")


class _AcMPIModNumber_Type(Integer32):
    """Custom type acMPIModNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AcMPIModNumber_Type.__name__ = "Integer32"
_AcMPIModNumber_Object = MibScalar
acMPIModNumber = _AcMPIModNumber_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 1, 9),
    _AcMPIModNumber_Type()
)
acMPIModNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMPIModNumber.setStatus("current")
_OutletOpTables_ObjectIdentity = ObjectIdentity
outletOpTables = _OutletOpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 3, 2)
)
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 2, 1)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 2, 1, 1)
)
outletEntry.setIndexNames(
    (0, "SYNSYS-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletEntry.setStatus("current")


class _OutletIndex_Type(Integer32):
    """Custom type outletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_OutletIndex_Type.__name__ = "Integer32"
_OutletIndex_Object = MibTableColumn
outletIndex = _OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 2, 1, 1, 1),
    _OutletIndex_Type()
)
outletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletIndex.setStatus("current")


class _OutletName_Type(DisplayString):
    """Custom type outletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_OutletName_Type.__name__ = "DisplayString"
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 2, 1, 1, 2),
    _OutletName_Type()
)
outletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletName.setStatus("current")


class _OutletStatus_Type(Integer32):
    """Custom type outletStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_OutletStatus_Type.__name__ = "Integer32"
_OutletStatus_Object = MibTableColumn
outletStatus = _OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 2, 1, 1, 3),
    _OutletStatus_Type()
)
outletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatus.setStatus("current")


class _OutletAction_Type(Integer32):
    """Custom type outletAction based on Integer32"""
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
        *(("none", 0),
          ("on", 1),
          ("off", 2),
          ("reboot", 3))
    )


_OutletAction_Type.__name__ = "Integer32"
_OutletAction_Object = MibTableColumn
outletAction = _OutletAction_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 2, 1, 1, 4),
    _OutletAction_Type()
)
outletAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletAction.setStatus("current")


class _OutletCurrentDraw_Type(DisplayString):
    """Custom type outletCurrentDraw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OutletCurrentDraw_Type.__name__ = "DisplayString"
_OutletCurrentDraw_Object = MibTableColumn
outletCurrentDraw = _OutletCurrentDraw_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 2, 1, 1, 5),
    _OutletCurrentDraw_Type()
)
outletCurrentDraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrentDraw.setStatus("current")
_EnviroTable_ObjectIdentity = ObjectIdentity
enviroTable = _EnviroTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 3, 3)
)


class _CurrentAlarmThreshold_Type(Integer32):
    """Custom type currentAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35),
    )


_CurrentAlarmThreshold_Type.__name__ = "Integer32"
_CurrentAlarmThreshold_Object = MibScalar
currentAlarmThreshold = _CurrentAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 3, 1),
    _CurrentAlarmThreshold_Type()
)
currentAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentAlarmThreshold.setStatus("current")


class _CurrentDrawStatus1_Type(DisplayString):
    """Custom type currentDrawStatus1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_CurrentDrawStatus1_Type.__name__ = "DisplayString"
_CurrentDrawStatus1_Object = MibScalar
currentDrawStatus1 = _CurrentDrawStatus1_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 3, 2),
    _CurrentDrawStatus1_Type()
)
currentDrawStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDrawStatus1.setStatus("current")


class _CurrentDrawStatus2_Type(DisplayString):
    """Custom type currentDrawStatus2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_CurrentDrawStatus2_Type.__name__ = "DisplayString"
_CurrentDrawStatus2_Object = MibScalar
currentDrawStatus2 = _CurrentDrawStatus2_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 3, 3),
    _CurrentDrawStatus2_Type()
)
currentDrawStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDrawStatus2.setStatus("current")


class _CurrentDrawMax1_Type(DisplayString):
    """Custom type currentDrawMax1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_CurrentDrawMax1_Type.__name__ = "DisplayString"
_CurrentDrawMax1_Object = MibScalar
currentDrawMax1 = _CurrentDrawMax1_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 3, 4),
    _CurrentDrawMax1_Type()
)
currentDrawMax1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDrawMax1.setStatus("current")


class _CurrentDrawMax2_Type(DisplayString):
    """Custom type currentDrawMax2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_CurrentDrawMax2_Type.__name__ = "DisplayString"
_CurrentDrawMax2_Object = MibScalar
currentDrawMax2 = _CurrentDrawMax2_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 3, 5),
    _CurrentDrawMax2_Type()
)
currentDrawMax2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDrawMax2.setStatus("current")


class _TemperatureUpThreshold_Type(Integer32):
    """Custom type temperatureUpThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 100),
    )


_TemperatureUpThreshold_Type.__name__ = "Integer32"
_TemperatureUpThreshold_Object = MibScalar
temperatureUpThreshold = _TemperatureUpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 3, 6),
    _TemperatureUpThreshold_Type()
)
temperatureUpThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureUpThreshold.setStatus("current")


class _TemperatureLowThreshold_Type(Integer32):
    """Custom type temperatureLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 100),
    )


_TemperatureLowThreshold_Type.__name__ = "Integer32"
_TemperatureLowThreshold_Object = MibScalar
temperatureLowThreshold = _TemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 3, 7),
    _TemperatureLowThreshold_Type()
)
temperatureLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureLowThreshold.setStatus("current")


class _TemperatureReading_Type(Integer32):
    """Custom type temperatureReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 100),
    )


_TemperatureReading_Type.__name__ = "Integer32"
_TemperatureReading_Object = MibScalar
temperatureReading = _TemperatureReading_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 3, 8),
    _TemperatureReading_Type()
)
temperatureReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureReading.setStatus("current")
_TrapSetting_ObjectIdentity = ObjectIdentity
trapSetting = _TrapSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 3, 4)
)


class _TrapEnable_Type(Integer32):
    """Custom type trapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TrapEnable_Type.__name__ = "Integer32"
_TrapEnable_Object = MibScalar
trapEnable = _TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 4, 1),
    _TrapEnable_Type()
)
trapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnable.setStatus("current")
_TrapRcvIP_Type = IpAddress
_TrapRcvIP_Object = MibScalar
trapRcvIP = _TrapRcvIP_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 4, 2),
    _TrapRcvIP_Type()
)
trapRcvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRcvIP.setStatus("current")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibScalar
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 4, 3),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("current")
_EnergyStatus_ObjectIdentity = ObjectIdentity
energyStatus = _EnergyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 3, 5)
)


class _MpiCurrent_Type(DisplayString):
    """Custom type mpiCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MpiCurrent_Type.__name__ = "DisplayString"
_MpiCurrent_Object = MibScalar
mpiCurrent = _MpiCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 5, 1),
    _MpiCurrent_Type()
)
mpiCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpiCurrent.setStatus("current")


class _MpiVolt_Type(DisplayString):
    """Custom type mpiVolt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MpiVolt_Type.__name__ = "DisplayString"
_MpiVolt_Object = MibScalar
mpiVolt = _MpiVolt_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 5, 2),
    _MpiVolt_Type()
)
mpiVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpiVolt.setStatus("current")


class _MpiActivePower_Type(DisplayString):
    """Custom type mpiActivePower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MpiActivePower_Type.__name__ = "DisplayString"
_MpiActivePower_Object = MibScalar
mpiActivePower = _MpiActivePower_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 5, 3),
    _MpiActivePower_Type()
)
mpiActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpiActivePower.setStatus("current")


class _MpiApparentPower_Type(DisplayString):
    """Custom type mpiApparentPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MpiApparentPower_Type.__name__ = "DisplayString"
_MpiApparentPower_Object = MibScalar
mpiApparentPower = _MpiApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 5, 4),
    _MpiApparentPower_Type()
)
mpiApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpiApparentPower.setStatus("current")


class _MpiPowerFactor_Type(DisplayString):
    """Custom type mpiPowerFactor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MpiPowerFactor_Type.__name__ = "DisplayString"
_MpiPowerFactor_Object = MibScalar
mpiPowerFactor = _MpiPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 5, 5),
    _MpiPowerFactor_Type()
)
mpiPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpiPowerFactor.setStatus("current")


class _MpiAcFrequency_Type(DisplayString):
    """Custom type mpiAcFrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MpiAcFrequency_Type.__name__ = "DisplayString"
_MpiAcFrequency_Object = MibScalar
mpiAcFrequency = _MpiAcFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 5, 6),
    _MpiAcFrequency_Type()
)
mpiAcFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpiAcFrequency.setStatus("current")


class _MpiAcKwh_Type(DisplayString):
    """Custom type mpiAcKwh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MpiAcKwh_Type.__name__ = "DisplayString"
_MpiAcKwh_Object = MibScalar
mpiAcKwh = _MpiAcKwh_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 5, 7),
    _MpiAcKwh_Type()
)
mpiAcKwh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpiAcKwh.setStatus("current")


class _MpiAcKwhStartEPOCH_Type(DisplayString):
    """Custom type mpiAcKwhStartEPOCH based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MpiAcKwhStartEPOCH_Type.__name__ = "DisplayString"
_MpiAcKwhStartEPOCH_Object = MibScalar
mpiAcKwhStartEPOCH = _MpiAcKwhStartEPOCH_Object(
    (1, 3, 6, 1, 4, 1, 21728, 3, 5, 8),
    _MpiAcKwhStartEPOCH_Type()
)
mpiAcKwhStartEPOCH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpiAcKwhStartEPOCH.setStatus("current")
_TrapEvent_ObjectIdentity = ObjectIdentity
trapEvent = _TrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 3, 100)
)
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21728, 3, 100, 0)
)

# Managed Objects groups


# Notification objects

outletStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 3, 100, 0, 1)
)
outletStatusEvent.setObjects(
      *(("SYNSYS-MIB", "systemName"),
        ("SYNSYS-MIB", "outletName"),
        ("SYNSYS-MIB", "outletStatus"))
)
if mibBuilder.loadTexts:
    outletStatusEvent.setStatus(
        "current"
    )

outletGroupStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 3, 100, 0, 2)
)
outletGroupStatusEvent.setObjects(
      *(("SYNSYS-MIB", "systemName"),
        ("SYNSYS-MIB", "outletStatus"))
)
if mibBuilder.loadTexts:
    outletGroupStatusEvent.setStatus(
        "current"
    )

autoPingRebootEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 3, 100, 0, 3)
)
autoPingRebootEvent.setObjects(
      *(("SYNSYS-MIB", "systemName"),
        ("SYNSYS-MIB", "outletName"))
)
if mibBuilder.loadTexts:
    autoPingRebootEvent.setStatus(
        "current"
    )

temperatureAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 3, 100, 0, 4)
)
temperatureAlarmEvent.setObjects(
    ("SYNSYS-MIB", "systemName")
)
if mibBuilder.loadTexts:
    temperatureAlarmEvent.setStatus(
        "current"
    )

temperatureControlledOutletEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 3, 100, 0, 5)
)
temperatureControlledOutletEvent.setObjects(
      *(("SYNSYS-MIB", "systemName"),
        ("SYNSYS-MIB", "outletName"))
)
if mibBuilder.loadTexts:
    temperatureControlledOutletEvent.setStatus(
        "current"
    )

systemPowerUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 3, 100, 0, 6)
)
systemPowerUpEvent.setObjects(
    ("SYNSYS-MIB", "systemName")
)
if mibBuilder.loadTexts:
    systemPowerUpEvent.setStatus(
        "current"
    )

kwhOverLimitEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 21728, 3, 100, 0, 7)
)
kwhOverLimitEvent.setObjects(
      *(("SYNSYS-MIB", "systemName"),
        ("SYNSYS-MIB", "outletName"),
        ("SYNSYS-MIB", "mpiAcKwh"),
        ("SYNSYS-MIB", "mpiAcKwhStartEPOCH"))
)
if mibBuilder.loadTexts:
    kwhOverLimitEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNSYS-MIB",
    **{"synaccess": synaccess,
       "synSys": synSys,
       "systemDescr": systemDescr,
       "systemModel": systemModel,
       "systemName": systemName,
       "powerOutletNum": powerOutletNum,
       "serialPortNum": serialPortNum,
       "systemUpTime": systemUpTime,
       "swVersion": swVersion,
       "acCurrentSensorNumber": acCurrentSensorNumber,
       "temperatureProbe": temperatureProbe,
       "acMPIModNumber": acMPIModNumber,
       "outletOpTables": outletOpTables,
       "outletTable": outletTable,
       "outletEntry": outletEntry,
       "outletIndex": outletIndex,
       "outletName": outletName,
       "outletStatus": outletStatus,
       "outletAction": outletAction,
       "outletCurrentDraw": outletCurrentDraw,
       "enviroTable": enviroTable,
       "currentAlarmThreshold": currentAlarmThreshold,
       "currentDrawStatus1": currentDrawStatus1,
       "currentDrawStatus2": currentDrawStatus2,
       "currentDrawMax1": currentDrawMax1,
       "currentDrawMax2": currentDrawMax2,
       "temperatureUpThreshold": temperatureUpThreshold,
       "temperatureLowThreshold": temperatureLowThreshold,
       "temperatureReading": temperatureReading,
       "trapSetting": trapSetting,
       "trapEnable": trapEnable,
       "trapRcvIP": trapRcvIP,
       "trapCommunity": trapCommunity,
       "energyStatus": energyStatus,
       "mpiCurrent": mpiCurrent,
       "mpiVolt": mpiVolt,
       "mpiActivePower": mpiActivePower,
       "mpiApparentPower": mpiApparentPower,
       "mpiPowerFactor": mpiPowerFactor,
       "mpiAcFrequency": mpiAcFrequency,
       "mpiAcKwh": mpiAcKwh,
       "mpiAcKwhStartEPOCH": mpiAcKwhStartEPOCH,
       "trapEvent": trapEvent,
       "event": event,
       "outletStatusEvent": outletStatusEvent,
       "outletGroupStatusEvent": outletGroupStatusEvent,
       "autoPingRebootEvent": autoPingRebootEvent,
       "temperatureAlarmEvent": temperatureAlarmEvent,
       "temperatureControlledOutletEvent": temperatureControlledOutletEvent,
       "systemPowerUpEvent": systemPowerUpEvent,
       "kwhOverLimitEvent": kwhOverLimitEvent}
)
