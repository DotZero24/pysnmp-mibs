# SNMP MIB module (ELTEK_GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltek/ELTEK_GENERIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:17:01 2025
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

(eltek,) = mibBuilder.importSymbols(
    "ELTEK-COMMON-MIB",
    "eltek")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltekPlant_ObjectIdentity = ObjectIdentity
eltekPlant = _EltekPlant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7)
)
_ControlSystem_ObjectIdentity = ObjectIdentity
controlSystem = _ControlSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 1)
)
_SystemTime_ObjectIdentity = ObjectIdentity
systemTime = _SystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 1, 1)
)


class _SystemTimeTime_Type(DisplayString):
    """Custom type systemTimeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemTimeTime_Type.__name__ = "DisplayString"
_SystemTimeTime_Object = MibScalar
systemTimeTime = _SystemTimeTime_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 1, 1, 1),
    _SystemTimeTime_Type()
)
systemTimeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTimeTime.setStatus("current")


class _SystemInfoRefresh_Type(Integer32):
    """Custom type systemInfoRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("refreshdata", 1))
    )


_SystemInfoRefresh_Type.__name__ = "Integer32"
_SystemInfoRefresh_Object = MibScalar
systemInfoRefresh = _SystemInfoRefresh_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 1, 2),
    _SystemInfoRefresh_Type()
)
systemInfoRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemInfoRefresh.setStatus("current")


class _SystemTrapRepeatRate_Type(Integer32):
    """Custom type systemTrapRepeatRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SystemTrapRepeatRate_Type.__name__ = "Integer32"
_SystemTrapRepeatRate_Object = MibScalar
systemTrapRepeatRate = _SystemTrapRepeatRate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 1, 3),
    _SystemTrapRepeatRate_Type()
)
systemTrapRepeatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTrapRepeatRate.setStatus("current")


class _SystemSendOffTrap_Type(Integer32):
    """Custom type systemSendOffTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemSendOffTrap_Type.__name__ = "Integer32"
_SystemSendOffTrap_Object = MibScalar
systemSendOffTrap = _SystemSendOffTrap_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 1, 4),
    _SystemSendOffTrap_Type()
)
systemSendOffTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSendOffTrap.setStatus("current")
_DcSystem_ObjectIdentity = ObjectIdentity
dcSystem = _DcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2)
)
_DcPlant_ObjectIdentity = ObjectIdentity
dcPlant = _DcPlant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1)
)
_SystemSiteInfo_ObjectIdentity = ObjectIdentity
systemSiteInfo = _SystemSiteInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 3)
)


class _SystemSiteInfoCustomer_Type(DisplayString):
    """Custom type systemSiteInfoCustomer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemSiteInfoCustomer_Type.__name__ = "DisplayString"
_SystemSiteInfoCustomer_Object = MibScalar
systemSiteInfoCustomer = _SystemSiteInfoCustomer_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 3, 1),
    _SystemSiteInfoCustomer_Type()
)
systemSiteInfoCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoCustomer.setStatus("current")


class _SystemSiteInfoLocation_Type(DisplayString):
    """Custom type systemSiteInfoLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemSiteInfoLocation_Type.__name__ = "DisplayString"
_SystemSiteInfoLocation_Object = MibScalar
systemSiteInfoLocation = _SystemSiteInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 3, 2),
    _SystemSiteInfoLocation_Type()
)
systemSiteInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoLocation.setStatus("current")


class _SystemSiteInfoMessage1_Type(DisplayString):
    """Custom type systemSiteInfoMessage1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemSiteInfoMessage1_Type.__name__ = "DisplayString"
_SystemSiteInfoMessage1_Object = MibScalar
systemSiteInfoMessage1 = _SystemSiteInfoMessage1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 3, 3),
    _SystemSiteInfoMessage1_Type()
)
systemSiteInfoMessage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoMessage1.setStatus("current")


class _SystemSiteInfoMessage2_Type(DisplayString):
    """Custom type systemSiteInfoMessage2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemSiteInfoMessage2_Type.__name__ = "DisplayString"
_SystemSiteInfoMessage2_Object = MibScalar
systemSiteInfoMessage2 = _SystemSiteInfoMessage2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 3, 4),
    _SystemSiteInfoMessage2_Type()
)
systemSiteInfoMessage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoMessage2.setStatus("current")


class _SystemSiteInfoInstalledDate_Type(DisplayString):
    """Custom type systemSiteInfoInstalledDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemSiteInfoInstalledDate_Type.__name__ = "DisplayString"
_SystemSiteInfoInstalledDate_Object = MibScalar
systemSiteInfoInstalledDate = _SystemSiteInfoInstalledDate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 3, 5),
    _SystemSiteInfoInstalledDate_Type()
)
systemSiteInfoInstalledDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoInstalledDate.setStatus("current")


class _SystemSiteInfoControllerType_Type(Integer32):
    """Custom type systemSiteInfoControllerType based on Integer32"""
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
        *(("al175", 0),
          ("al4000", 1),
          ("al6000", 2),
          ("enexus", 3))
    )


_SystemSiteInfoControllerType_Type.__name__ = "Integer32"
_SystemSiteInfoControllerType_Object = MibScalar
systemSiteInfoControllerType = _SystemSiteInfoControllerType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 3, 6),
    _SystemSiteInfoControllerType_Type()
)
systemSiteInfoControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoControllerType.setStatus("current")


class _SystemSiteInfoSystemSeriaNum_Type(DisplayString):
    """Custom type systemSiteInfoSystemSeriaNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemSiteInfoSystemSeriaNum_Type.__name__ = "DisplayString"
_SystemSiteInfoSystemSeriaNum_Object = MibScalar
systemSiteInfoSystemSeriaNum = _SystemSiteInfoSystemSeriaNum_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 3, 7),
    _SystemSiteInfoSystemSeriaNum_Type()
)
systemSiteInfoSystemSeriaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoSystemSeriaNum.setStatus("current")


class _SystemSiteInfoControllerSeriaNum_Type(DisplayString):
    """Custom type systemSiteInfoControllerSeriaNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemSiteInfoControllerSeriaNum_Type.__name__ = "DisplayString"
_SystemSiteInfoControllerSeriaNum_Object = MibScalar
systemSiteInfoControllerSeriaNum = _SystemSiteInfoControllerSeriaNum_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 3, 8),
    _SystemSiteInfoControllerSeriaNum_Type()
)
systemSiteInfoControllerSeriaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoControllerSeriaNum.setStatus("current")


class _SystemNominalVoltage_Type(Integer32):
    """Custom type systemNominalVoltage based on Integer32"""
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
        *(("prs48v", 0),
          ("prs24v", 1),
          ("prs12v", 2),
          ("prs26v", 3),
          ("prs60v", 4))
    )


_SystemNominalVoltage_Type.__name__ = "Integer32"
_SystemNominalVoltage_Object = MibScalar
systemNominalVoltage = _SystemNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 1, 4),
    _SystemNominalVoltage_Type()
)
systemNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNominalVoltage.setStatus("current")


class _SystemOperationalStatus_Type(Integer32):
    """Custom type systemOperationalStatus based on Integer32"""
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
        *(("floatvoltreg", 0),
          ("floattempcomp", 1),
          ("batteryboost", 2),
          ("batterytest", 3))
    )


_SystemOperationalStatus_Type.__name__ = "Integer32"
_SystemOperationalStatus_Object = MibScalar
systemOperationalStatus = _SystemOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 2, 2),
    _SystemOperationalStatus_Type()
)
systemOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOperationalStatus.setStatus("current")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3)
)


class _BatteryName_Type(DisplayString):
    """Custom type batteryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryName_Type.__name__ = "DisplayString"
_BatteryName_Object = MibScalar
batteryName = _BatteryName_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 1),
    _BatteryName_Type()
)
batteryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryName.setStatus("current")


class _BatteryVoltage_Type(Integer32):
    """Custom type batteryVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_BatteryVoltage_Type.__name__ = "Integer32"
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 2),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryCurrent_Type = Integer32
_BatteryCurrent_Object = MibScalar
batteryCurrent = _BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 3),
    _BatteryCurrent_Type()
)
batteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    batteryCurrent.setUnits("Amperes; i.e. 20 = 20 Amperes")


class _BatteryTemp_Type(Integer32):
    """Custom type batteryTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_BatteryTemp_Type.__name__ = "Integer32"
_BatteryTemp_Object = MibScalar
batteryTemp = _BatteryTemp_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 4),
    _BatteryTemp_Type()
)
batteryTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemp.setStatus("current")
if mibBuilder.loadTexts:
    batteryTemp.setUnits("1/10 Deg. C; i.e. 250 = 25.0 Deg. C.")


class _BatteryBreakerStatus_Type(Integer32):
    """Custom type batteryBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_BatteryBreakerStatus_Type.__name__ = "Integer32"
_BatteryBreakerStatus_Object = MibScalar
batteryBreakerStatus = _BatteryBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 5),
    _BatteryBreakerStatus_Type()
)
batteryBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBreakerStatus.setStatus("current")


class _BatteryChargeCurrentLimitCtrl_Type(Integer32):
    """Custom type batteryChargeCurrentLimitCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deactivate", 0),
          ("activate", 1))
    )


_BatteryChargeCurrentLimitCtrl_Type.__name__ = "Integer32"
_BatteryChargeCurrentLimitCtrl_Object = MibScalar
batteryChargeCurrentLimitCtrl = _BatteryChargeCurrentLimitCtrl_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 6),
    _BatteryChargeCurrentLimitCtrl_Type()
)
batteryChargeCurrentLimitCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitCtrl.setStatus("current")


class _BatteryChargeCurrentLimitValue_Type(Integer32):
    """Custom type batteryChargeCurrentLimitValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2100),
    )


_BatteryChargeCurrentLimitValue_Type.__name__ = "Integer32"
_BatteryChargeCurrentLimitValue_Object = MibScalar
batteryChargeCurrentLimitValue = _BatteryChargeCurrentLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 7),
    _BatteryChargeCurrentLimitValue_Type()
)
batteryChargeCurrentLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitValue.setStatus("current")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitValue.setUnits("Amperes; i.e. 20 = 20 Amperes")


class _BatteryTempCompEnable_Type(Integer32):
    """Custom type batteryTempCompEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryTempCompEnable_Type.__name__ = "Integer32"
_BatteryTempCompEnable_Object = MibScalar
batteryTempCompEnable = _BatteryTempCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 8),
    _BatteryTempCompEnable_Type()
)
batteryTempCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompEnable.setStatus("current")


class _BatteryFloatVoltConfig_Type(Integer32):
    """Custom type batteryFloatVoltConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4300, 6000),
    )


_BatteryFloatVoltConfig_Type.__name__ = "Integer32"
_BatteryFloatVoltConfig_Object = MibScalar
batteryFloatVoltConfig = _BatteryFloatVoltConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 9),
    _BatteryFloatVoltConfig_Type()
)
batteryFloatVoltConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryFloatVoltConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryFloatVoltConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _BatteryEqualizeVoltConfig_Type(Integer32):
    """Custom type batteryEqualizeVoltConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4300, 6000),
    )


_BatteryEqualizeVoltConfig_Type.__name__ = "Integer32"
_BatteryEqualizeVoltConfig_Object = MibScalar
batteryEqualizeVoltConfig = _BatteryEqualizeVoltConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 10),
    _BatteryEqualizeVoltConfig_Type()
)
batteryEqualizeVoltConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryEqualizeVoltConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryEqualizeVoltConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryHighMajorAlarmVoltageConfig_Type = Integer32
_BatteryHighMajorAlarmVoltageConfig_Object = MibScalar
batteryHighMajorAlarmVoltageConfig = _BatteryHighMajorAlarmVoltageConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 11),
    _BatteryHighMajorAlarmVoltageConfig_Type()
)
batteryHighMajorAlarmVoltageConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryHighMajorAlarmVoltageConfig.setStatus("current")
_BatteryHighMinorAlarmVoltageConfig_Type = Integer32
_BatteryHighMinorAlarmVoltageConfig_Object = MibScalar
batteryHighMinorAlarmVoltageConfig = _BatteryHighMinorAlarmVoltageConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 12),
    _BatteryHighMinorAlarmVoltageConfig_Type()
)
batteryHighMinorAlarmVoltageConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryHighMinorAlarmVoltageConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryHighMinorAlarmVoltageConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryLowMajorAlarmVoltageConfig_Type = Integer32
_BatteryLowMajorAlarmVoltageConfig_Object = MibScalar
batteryLowMajorAlarmVoltageConfig = _BatteryLowMajorAlarmVoltageConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 13),
    _BatteryLowMajorAlarmVoltageConfig_Type()
)
batteryLowMajorAlarmVoltageConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLowMajorAlarmVoltageConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryLowMajorAlarmVoltageConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryLowMinorAlarmVoltageConfig_Type = Integer32
_BatteryLowMinorAlarmVoltageConfig_Object = MibScalar
batteryLowMinorAlarmVoltageConfig = _BatteryLowMinorAlarmVoltageConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 14),
    _BatteryLowMinorAlarmVoltageConfig_Type()
)
batteryLowMinorAlarmVoltageConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLowMinorAlarmVoltageConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryLowMinorAlarmVoltageConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _BatteryStartManualTest_Type(Integer32):
    """Custom type batteryStartManualTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("starttest", 1),
          ("stoptest", 2))
    )


_BatteryStartManualTest_Type.__name__ = "Integer32"
_BatteryStartManualTest_Object = MibScalar
batteryStartManualTest = _BatteryStartManualTest_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 15),
    _BatteryStartManualTest_Type()
)
batteryStartManualTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryStartManualTest.setStatus("current")


class _BatteryStartManualBoost_Type(Integer32):
    """Custom type batteryStartManualBoost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("startboost", 1),
          ("stopboost", 2))
    )


_BatteryStartManualBoost_Type.__name__ = "Integer32"
_BatteryStartManualBoost_Object = MibScalar
batteryStartManualBoost = _BatteryStartManualBoost_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 16),
    _BatteryStartManualBoost_Type()
)
batteryStartManualBoost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryStartManualBoost.setStatus("current")
_BatteryLVD_ObjectIdentity = ObjectIdentity
batteryLVD = _BatteryLVD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 17)
)


class _BatteryLVDStatus_Type(Integer32):
    """Custom type batteryLVDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 0),
          ("disconnect", 1),
          ("disable", 2))
    )


_BatteryLVDStatus_Type.__name__ = "Integer32"
_BatteryLVDStatus_Object = MibScalar
batteryLVDStatus = _BatteryLVDStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 17, 1),
    _BatteryLVDStatus_Type()
)
batteryLVDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLVDStatus.setStatus("current")


class _BatteryLVDDisconnectVoltage_Type(Integer32):
    """Custom type batteryLVDDisconnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_BatteryLVDDisconnectVoltage_Type.__name__ = "Integer32"
_BatteryLVDDisconnectVoltage_Object = MibScalar
batteryLVDDisconnectVoltage = _BatteryLVDDisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 17, 2),
    _BatteryLVDDisconnectVoltage_Type()
)
batteryLVDDisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVDDisconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryLVDDisconnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _BatteryLVDConnectVoltage_Type(Integer32):
    """Custom type batteryLVDConnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_BatteryLVDConnectVoltage_Type.__name__ = "Integer32"
_BatteryLVDConnectVoltage_Object = MibScalar
batteryLVDConnectVoltage = _BatteryLVDConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 17, 3),
    _BatteryLVDConnectVoltage_Type()
)
batteryLVDConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVDConnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryLVDConnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryMidpoint_ObjectIdentity = ObjectIdentity
batteryMidpoint = _BatteryMidpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18)
)
_BatteryMidpointDeltaLimitVoltage_Type = Integer32
_BatteryMidpointDeltaLimitVoltage_Object = MibScalar
batteryMidpointDeltaLimitVoltage = _BatteryMidpointDeltaLimitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 1),
    _BatteryMidpointDeltaLimitVoltage_Type()
)
batteryMidpointDeltaLimitVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMidpointDeltaLimitVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryMidpointDeltaLimitVoltage.setUnits("1/100 Volt; i.e. 25 = 2.50V")


class _BatteryMidpointIndex_Type(Integer32):
    """Custom type batteryMidpointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryMidpointIndex_Type.__name__ = "Integer32"
_BatteryMidpointIndex_Object = MibScalar
batteryMidpointIndex = _BatteryMidpointIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 2),
    _BatteryMidpointIndex_Type()
)
batteryMidpointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMidpointIndex.setStatus("current")
_BatteryMidpointControlTable_Object = MibTable
batteryMidpointControlTable = _BatteryMidpointControlTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 3)
)
if mibBuilder.loadTexts:
    batteryMidpointControlTable.setStatus("current")
_BatteryMidpointControlEntry_Object = MibTableRow
batteryMidpointControlEntry = _BatteryMidpointControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 3, 1)
)
batteryMidpointControlEntry.setIndexNames(
    (0, "ELTEK_GENERIC-MIB", "batteryMidpointIndex"),
)
if mibBuilder.loadTexts:
    batteryMidpointControlEntry.setStatus("current")


class _MidpointEnableID_Type(Integer32):
    """Custom type midpointEnableID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MidpointEnableID_Type.__name__ = "Integer32"
_MidpointEnableID_Object = MibTableColumn
midpointEnableID = _MidpointEnableID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 3, 1, 1),
    _MidpointEnableID_Type()
)
midpointEnableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midpointEnableID.setStatus("current")


class _MidpointEnable_Type(Integer32):
    """Custom type midpointEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MidpointEnable_Type.__name__ = "Integer32"
_MidpointEnable_Object = MibTableColumn
midpointEnable = _MidpointEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 3, 1, 2),
    _MidpointEnable_Type()
)
midpointEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midpointEnable.setStatus("current")
_BatteryMidpointStatusTable_Object = MibTable
batteryMidpointStatusTable = _BatteryMidpointStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 4)
)
if mibBuilder.loadTexts:
    batteryMidpointStatusTable.setStatus("current")
_BatteryMidpointStatusEntry_Object = MibTableRow
batteryMidpointStatusEntry = _BatteryMidpointStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 4, 1)
)
batteryMidpointStatusEntry.setIndexNames(
    (0, "ELTEK_GENERIC-MIB", "batteryMidpointIndex"),
)
if mibBuilder.loadTexts:
    batteryMidpointStatusEntry.setStatus("current")


class _MidpointStatusID_Type(Integer32):
    """Custom type midpointStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MidpointStatusID_Type.__name__ = "Integer32"
_MidpointStatusID_Object = MibTableColumn
midpointStatusID = _MidpointStatusID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 4, 1, 1),
    _MidpointStatusID_Type()
)
midpointStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midpointStatusID.setStatus("current")


class _MidpointStatus_Type(Integer32):
    """Custom type midpointStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("alarm", 1),
          ("disable", 2))
    )


_MidpointStatus_Type.__name__ = "Integer32"
_MidpointStatus_Object = MibTableColumn
midpointStatus = _MidpointStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 4, 1, 2),
    _MidpointStatus_Type()
)
midpointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midpointStatus.setStatus("current")
_MidpointDeltaVoltage_Type = Integer32
_MidpointDeltaVoltage_Object = MibTableColumn
midpointDeltaVoltage = _MidpointDeltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 3, 18, 4, 1, 3),
    _MidpointDeltaVoltage_Type()
)
midpointDeltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midpointDeltaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    midpointDeltaVoltage.setUnits("1/100 Volt; i.e. 25 = 2.5V.")
_LoadDistribution_ObjectIdentity = ObjectIdentity
loadDistribution = _LoadDistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4)
)
_LoadDistributionCurrent_Type = Integer32
_LoadDistributionCurrent_Object = MibScalar
loadDistributionCurrent = _LoadDistributionCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 1),
    _LoadDistributionCurrent_Type()
)
loadDistributionCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadDistributionCurrent.setStatus("current")
if mibBuilder.loadTexts:
    loadDistributionCurrent.setUnits("Amperes; i.e. 20 = 20 Amperes")


class _LoadDistributionBreakerStatus_Type(Integer32):
    """Custom type loadDistributionBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_LoadDistributionBreakerStatus_Type.__name__ = "Integer32"
_LoadDistributionBreakerStatus_Object = MibScalar
loadDistributionBreakerStatus = _LoadDistributionBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 2),
    _LoadDistributionBreakerStatus_Type()
)
loadDistributionBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadDistributionBreakerStatus.setStatus("current")
_LoadDistributionLVDStatus_ObjectIdentity = ObjectIdentity
loadDistributionLVDStatus = _LoadDistributionLVDStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3)
)


class _LoadLVD1EnableStatus_Type(Integer32):
    """Custom type loadLVD1EnableStatus based on Integer32"""
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


_LoadLVD1EnableStatus_Type.__name__ = "Integer32"
_LoadLVD1EnableStatus_Object = MibScalar
loadLVD1EnableStatus = _LoadLVD1EnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 1),
    _LoadLVD1EnableStatus_Type()
)
loadLVD1EnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD1EnableStatus.setStatus("current")


class _LoadLVD1Status_Type(Integer32):
    """Custom type loadLVD1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 0),
          ("disconnect", 1),
          ("disable", 2))
    )


_LoadLVD1Status_Type.__name__ = "Integer32"
_LoadLVD1Status_Object = MibScalar
loadLVD1Status = _LoadLVD1Status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 2),
    _LoadLVD1Status_Type()
)
loadLVD1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD1Status.setStatus("current")


class _LoadLVD1ConnectVoltage_Type(Integer32):
    """Custom type loadLVD1ConnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD1ConnectVoltage_Type.__name__ = "Integer32"
_LoadLVD1ConnectVoltage_Object = MibScalar
loadLVD1ConnectVoltage = _LoadLVD1ConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 3),
    _LoadLVD1ConnectVoltage_Type()
)
loadLVD1ConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD1ConnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD1ConnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD1DisconnectVoltage_Type(Integer32):
    """Custom type loadLVD1DisconnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD1DisconnectVoltage_Type.__name__ = "Integer32"
_LoadLVD1DisconnectVoltage_Object = MibScalar
loadLVD1DisconnectVoltage = _LoadLVD1DisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 4),
    _LoadLVD1DisconnectVoltage_Type()
)
loadLVD1DisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD1DisconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD1DisconnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD2EnableStatus_Type(Integer32):
    """Custom type loadLVD2EnableStatus based on Integer32"""
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


_LoadLVD2EnableStatus_Type.__name__ = "Integer32"
_LoadLVD2EnableStatus_Object = MibScalar
loadLVD2EnableStatus = _LoadLVD2EnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 5),
    _LoadLVD2EnableStatus_Type()
)
loadLVD2EnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD2EnableStatus.setStatus("current")


class _LoadLVD2Status_Type(Integer32):
    """Custom type loadLVD2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 0),
          ("disconnect", 1),
          ("disable", 2))
    )


_LoadLVD2Status_Type.__name__ = "Integer32"
_LoadLVD2Status_Object = MibScalar
loadLVD2Status = _LoadLVD2Status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 6),
    _LoadLVD2Status_Type()
)
loadLVD2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD2Status.setStatus("current")


class _LoadLVD2ConnectVoltage_Type(Integer32):
    """Custom type loadLVD2ConnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD2ConnectVoltage_Type.__name__ = "Integer32"
_LoadLVD2ConnectVoltage_Object = MibScalar
loadLVD2ConnectVoltage = _LoadLVD2ConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 7),
    _LoadLVD2ConnectVoltage_Type()
)
loadLVD2ConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD2ConnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD2ConnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD2DisconnectVoltage_Type(Integer32):
    """Custom type loadLVD2DisconnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD2DisconnectVoltage_Type.__name__ = "Integer32"
_LoadLVD2DisconnectVoltage_Object = MibScalar
loadLVD2DisconnectVoltage = _LoadLVD2DisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 8),
    _LoadLVD2DisconnectVoltage_Type()
)
loadLVD2DisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD2DisconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD2DisconnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD3EnableStatus_Type(Integer32):
    """Custom type loadLVD3EnableStatus based on Integer32"""
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


_LoadLVD3EnableStatus_Type.__name__ = "Integer32"
_LoadLVD3EnableStatus_Object = MibScalar
loadLVD3EnableStatus = _LoadLVD3EnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 9),
    _LoadLVD3EnableStatus_Type()
)
loadLVD3EnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD3EnableStatus.setStatus("current")


class _LoadLVD3Status_Type(Integer32):
    """Custom type loadLVD3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 0),
          ("disconnect", 1),
          ("disable", 2))
    )


_LoadLVD3Status_Type.__name__ = "Integer32"
_LoadLVD3Status_Object = MibScalar
loadLVD3Status = _LoadLVD3Status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 10),
    _LoadLVD3Status_Type()
)
loadLVD3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD3Status.setStatus("current")


class _LoadLVD3ConnectVoltage_Type(Integer32):
    """Custom type loadLVD3ConnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD3ConnectVoltage_Type.__name__ = "Integer32"
_LoadLVD3ConnectVoltage_Object = MibScalar
loadLVD3ConnectVoltage = _LoadLVD3ConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 11),
    _LoadLVD3ConnectVoltage_Type()
)
loadLVD3ConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD3ConnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD3ConnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD3DisconnectVoltage_Type(Integer32):
    """Custom type loadLVD3DisconnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD3DisconnectVoltage_Type.__name__ = "Integer32"
_LoadLVD3DisconnectVoltage_Object = MibScalar
loadLVD3DisconnectVoltage = _LoadLVD3DisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 4, 3, 12),
    _LoadLVD3DisconnectVoltage_Type()
)
loadLVD3DisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD3DisconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD3DisconnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_Rectifier_ObjectIdentity = ObjectIdentity
rectifier = _Rectifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5)
)


class _RectifierInstalledRectifiers_Type(Integer32):
    """Custom type rectifierInstalledRectifiers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )


_RectifierInstalledRectifiers_Type.__name__ = "Integer32"
_RectifierInstalledRectifiers_Object = MibScalar
rectifierInstalledRectifiers = _RectifierInstalledRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 1),
    _RectifierInstalledRectifiers_Type()
)
rectifierInstalledRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierInstalledRectifiers.setStatus("current")


class _RectifierRectifiersActive_Type(Integer32):
    """Custom type rectifierRectifiersActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )


_RectifierRectifiersActive_Type.__name__ = "Integer32"
_RectifierRectifiersActive_Object = MibScalar
rectifierRectifiersActive = _RectifierRectifiersActive_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 2),
    _RectifierRectifiersActive_Type()
)
rectifierRectifiersActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierRectifiersActive.setStatus("current")
_RectifierTotalCurrent_Type = Integer32
_RectifierTotalCurrent_Object = MibScalar
rectifierTotalCurrent = _RectifierTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 3),
    _RectifierTotalCurrent_Type()
)
rectifierTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rectifierTotalCurrent.setUnits("Amperes; i.e. 20 = 20 Amperes")


class _RectifierUtilization_Type(Integer32):
    """Custom type rectifierUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RectifierUtilization_Type.__name__ = "Integer32"
_RectifierUtilization_Object = MibScalar
rectifierUtilization = _RectifierUtilization_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 4),
    _RectifierUtilization_Type()
)
rectifierUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierUtilization.setStatus("current")
_RectifierStatus_ObjectIdentity = ObjectIdentity
rectifierStatus = _RectifierStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5)
)


class _RectifierStatusNoIndex_Type(Integer32):
    """Custom type rectifierStatusNoIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RectifierStatusNoIndex_Type.__name__ = "Integer32"
_RectifierStatusNoIndex_Object = MibScalar
rectifierStatusNoIndex = _RectifierStatusNoIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 1),
    _RectifierStatusNoIndex_Type()
)
rectifierStatusNoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierStatusNoIndex.setStatus("current")
_RectifierStatusTable_Object = MibTable
rectifierStatusTable = _RectifierStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2)
)
if mibBuilder.loadTexts:
    rectifierStatusTable.setStatus("current")
_RectifierStatusEntry_Object = MibTableRow
rectifierStatusEntry = _RectifierStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1)
)
rectifierStatusEntry.setIndexNames(
    (0, "ELTEK_GENERIC-MIB", "rectifierStatusID"),
)
if mibBuilder.loadTexts:
    rectifierStatusEntry.setStatus("current")


class _RectifierStatusID_Type(Integer32):
    """Custom type rectifierStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RectifierStatusID_Type.__name__ = "Integer32"
_RectifierStatusID_Object = MibTableColumn
rectifierStatusID = _RectifierStatusID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1, 1),
    _RectifierStatusID_Type()
)
rectifierStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusID.setStatus("current")


class _RectifierStatusStatus_Type(Integer32):
    """Custom type rectifierStatusStatus based on Integer32"""
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
        *(("absent", 0),
          ("active", 1),
          ("failed", 2),
          ("walkin", 3),
          ("disabledbycommand", 4))
    )


_RectifierStatusStatus_Type.__name__ = "Integer32"
_RectifierStatusStatus_Object = MibTableColumn
rectifierStatusStatus = _RectifierStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1, 2),
    _RectifierStatusStatus_Type()
)
rectifierStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusStatus.setStatus("current")


class _RectifierStatusOutputCurrent_Type(Integer32):
    """Custom type rectifierStatusOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RectifierStatusOutputCurrent_Type.__name__ = "Integer32"
_RectifierStatusOutputCurrent_Object = MibTableColumn
rectifierStatusOutputCurrent = _RectifierStatusOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1, 3),
    _RectifierStatusOutputCurrent_Type()
)
rectifierStatusOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rectifierStatusOutputCurrent.setUnits("1/10 Amperes; i.e. 200 = 20 Amperes")


class _RectifierStatusOutputVoltage_Type(Integer32):
    """Custom type rectifierStatusOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RectifierStatusOutputVoltage_Type.__name__ = "Integer32"
_RectifierStatusOutputVoltage_Object = MibTableColumn
rectifierStatusOutputVoltage = _RectifierStatusOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1, 4),
    _RectifierStatusOutputVoltage_Type()
)
rectifierStatusOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    rectifierStatusOutputVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _RectifierStatusTemp_Type(Integer32):
    """Custom type rectifierStatusTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RectifierStatusTemp_Type.__name__ = "Integer32"
_RectifierStatusTemp_Object = MibTableColumn
rectifierStatusTemp = _RectifierStatusTemp_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1, 5),
    _RectifierStatusTemp_Type()
)
rectifierStatusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusTemp.setStatus("current")
if mibBuilder.loadTexts:
    rectifierStatusTemp.setUnits("Deg. C/10; i.e. 350 = 35.0 Deg. C")


class _RectifierStatusType_Type(DisplayString):
    """Custom type rectifierStatusType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierStatusType_Type.__name__ = "DisplayString"
_RectifierStatusType_Object = MibTableColumn
rectifierStatusType = _RectifierStatusType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1, 6),
    _RectifierStatusType_Type()
)
rectifierStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusType.setStatus("current")


class _RectifierStatusSKU_Type(DisplayString):
    """Custom type rectifierStatusSKU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierStatusSKU_Type.__name__ = "DisplayString"
_RectifierStatusSKU_Object = MibTableColumn
rectifierStatusSKU = _RectifierStatusSKU_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1, 7),
    _RectifierStatusSKU_Type()
)
rectifierStatusSKU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusSKU.setStatus("current")


class _RectifierStatusSerialNo_Type(DisplayString):
    """Custom type rectifierStatusSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierStatusSerialNo_Type.__name__ = "DisplayString"
_RectifierStatusSerialNo_Object = MibTableColumn
rectifierStatusSerialNo = _RectifierStatusSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1, 8),
    _RectifierStatusSerialNo_Type()
)
rectifierStatusSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusSerialNo.setStatus("current")


class _RectifierStatusRevisionLevel_Type(DisplayString):
    """Custom type rectifierStatusRevisionLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierStatusRevisionLevel_Type.__name__ = "DisplayString"
_RectifierStatusRevisionLevel_Object = MibTableColumn
rectifierStatusRevisionLevel = _RectifierStatusRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 5, 5, 2, 1, 9),
    _RectifierStatusRevisionLevel_Type()
)
rectifierStatusRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusRevisionLevel.setStatus("current")
_AcDistribution_ObjectIdentity = ObjectIdentity
acDistribution = _AcDistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 6)
)
_AcVoltage1_Type = Integer32
_AcVoltage1_Object = MibScalar
acVoltage1 = _AcVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 6, 1),
    _AcVoltage1_Type()
)
acVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVoltage1.setStatus("current")
if mibBuilder.loadTexts:
    acVoltage1.setUnits("Volts AC")
_AcVoltage2_Type = Integer32
_AcVoltage2_Object = MibScalar
acVoltage2 = _AcVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 6, 2),
    _AcVoltage2_Type()
)
acVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVoltage2.setStatus("current")
if mibBuilder.loadTexts:
    acVoltage2.setUnits("Volts AC")
_AcVoltage3_Type = Integer32
_AcVoltage3_Object = MibScalar
acVoltage3 = _AcVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 6, 3),
    _AcVoltage3_Type()
)
acVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVoltage3.setStatus("current")
if mibBuilder.loadTexts:
    acVoltage3.setUnits("Volts AC")
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7)
)
_AlarmWellknownAlarms_ObjectIdentity = ObjectIdentity
alarmWellknownAlarms = _AlarmWellknownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1)
)


class _AlarmMajorHighBattVolt_Type(Integer32):
    """Custom type alarmMajorHighBattVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMajorHighBattVolt_Type.__name__ = "Integer32"
_AlarmMajorHighBattVolt_Object = MibScalar
alarmMajorHighBattVolt = _AlarmMajorHighBattVolt_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 1),
    _AlarmMajorHighBattVolt_Type()
)
alarmMajorHighBattVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorHighBattVolt.setStatus("current")


class _AlarmMinorHighBattVolt_Type(Integer32):
    """Custom type alarmMinorHighBattVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMinorHighBattVolt_Type.__name__ = "Integer32"
_AlarmMinorHighBattVolt_Object = MibScalar
alarmMinorHighBattVolt = _AlarmMinorHighBattVolt_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 2),
    _AlarmMinorHighBattVolt_Type()
)
alarmMinorHighBattVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorHighBattVolt.setStatus("current")


class _AlarmMajorLowBattVolt_Type(Integer32):
    """Custom type alarmMajorLowBattVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMajorLowBattVolt_Type.__name__ = "Integer32"
_AlarmMajorLowBattVolt_Object = MibScalar
alarmMajorLowBattVolt = _AlarmMajorLowBattVolt_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 3),
    _AlarmMajorLowBattVolt_Type()
)
alarmMajorLowBattVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorLowBattVolt.setStatus("current")


class _AlarmMinorLowBattVolt_Type(Integer32):
    """Custom type alarmMinorLowBattVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMinorLowBattVolt_Type.__name__ = "Integer32"
_AlarmMinorLowBattVolt_Object = MibScalar
alarmMinorLowBattVolt = _AlarmMinorLowBattVolt_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 4),
    _AlarmMinorLowBattVolt_Type()
)
alarmMinorLowBattVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorLowBattVolt.setStatus("current")


class _AlarmMajorBatteryHighTemp_Type(Integer32):
    """Custom type alarmMajorBatteryHighTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMajorBatteryHighTemp_Type.__name__ = "Integer32"
_AlarmMajorBatteryHighTemp_Object = MibScalar
alarmMajorBatteryHighTemp = _AlarmMajorBatteryHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 5),
    _AlarmMajorBatteryHighTemp_Type()
)
alarmMajorBatteryHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorBatteryHighTemp.setStatus("current")


class _AlarmMinorBatteryHighTemp_Type(Integer32):
    """Custom type alarmMinorBatteryHighTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMinorBatteryHighTemp_Type.__name__ = "Integer32"
_AlarmMinorBatteryHighTemp_Object = MibScalar
alarmMinorBatteryHighTemp = _AlarmMinorBatteryHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 6),
    _AlarmMinorBatteryHighTemp_Type()
)
alarmMinorBatteryHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorBatteryHighTemp.setStatus("current")


class _AlarmBatteryDisconnectOpen_Type(Integer32):
    """Custom type alarmBatteryDisconnectOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmBatteryDisconnectOpen_Type.__name__ = "Integer32"
_AlarmBatteryDisconnectOpen_Object = MibScalar
alarmBatteryDisconnectOpen = _AlarmBatteryDisconnectOpen_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 7),
    _AlarmBatteryDisconnectOpen_Type()
)
alarmBatteryDisconnectOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryDisconnectOpen.setStatus("current")


class _AlarmLVD1open_Type(Integer32):
    """Custom type alarmLVD1open based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmLVD1open_Type.__name__ = "Integer32"
_AlarmLVD1open_Object = MibScalar
alarmLVD1open = _AlarmLVD1open_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 8),
    _AlarmLVD1open_Type()
)
alarmLVD1open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLVD1open.setStatus("current")


class _AlarmLVD2open_Type(Integer32):
    """Custom type alarmLVD2open based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmLVD2open_Type.__name__ = "Integer32"
_AlarmLVD2open_Object = MibScalar
alarmLVD2open = _AlarmLVD2open_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 9),
    _AlarmLVD2open_Type()
)
alarmLVD2open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLVD2open.setStatus("current")


class _AlarmLVD3open_Type(Integer32):
    """Custom type alarmLVD3open based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmLVD3open_Type.__name__ = "Integer32"
_AlarmLVD3open_Object = MibScalar
alarmLVD3open = _AlarmLVD3open_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 10),
    _AlarmLVD3open_Type()
)
alarmLVD3open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLVD3open.setStatus("current")


class _AlarmACmains_Type(Integer32):
    """Custom type alarmACmains based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmACmains_Type.__name__ = "Integer32"
_AlarmACmains_Object = MibScalar
alarmACmains = _AlarmACmains_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 11),
    _AlarmACmains_Type()
)
alarmACmains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmACmains.setStatus("current")


class _AlarmBatteryBreakerOpen_Type(Integer32):
    """Custom type alarmBatteryBreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmBatteryBreakerOpen_Type.__name__ = "Integer32"
_AlarmBatteryBreakerOpen_Object = MibScalar
alarmBatteryBreakerOpen = _AlarmBatteryBreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 12),
    _AlarmBatteryBreakerOpen_Type()
)
alarmBatteryBreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryBreakerOpen.setStatus("current")


class _AlarmDistributionBreakerOpen_Type(Integer32):
    """Custom type alarmDistributionBreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmDistributionBreakerOpen_Type.__name__ = "Integer32"
_AlarmDistributionBreakerOpen_Object = MibScalar
alarmDistributionBreakerOpen = _AlarmDistributionBreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 13),
    _AlarmDistributionBreakerOpen_Type()
)
alarmDistributionBreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDistributionBreakerOpen.setStatus("current")


class _AlarmMajorRectifier_Type(Integer32):
    """Custom type alarmMajorRectifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMajorRectifier_Type.__name__ = "Integer32"
_AlarmMajorRectifier_Object = MibScalar
alarmMajorRectifier = _AlarmMajorRectifier_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 14),
    _AlarmMajorRectifier_Type()
)
alarmMajorRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorRectifier.setStatus("current")


class _AlarmMinorRectifier_Type(Integer32):
    """Custom type alarmMinorRectifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMinorRectifier_Type.__name__ = "Integer32"
_AlarmMinorRectifier_Object = MibScalar
alarmMinorRectifier = _AlarmMinorRectifier_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 15),
    _AlarmMinorRectifier_Type()
)
alarmMinorRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorRectifier.setStatus("current")


class _AlarmMajorBatteryMidpoint_Type(Integer32):
    """Custom type alarmMajorBatteryMidpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMajorBatteryMidpoint_Type.__name__ = "Integer32"
_AlarmMajorBatteryMidpoint_Object = MibScalar
alarmMajorBatteryMidpoint = _AlarmMajorBatteryMidpoint_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 16),
    _AlarmMajorBatteryMidpoint_Type()
)
alarmMajorBatteryMidpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorBatteryMidpoint.setStatus("current")


class _AlarmMinorBatteryMidpoint_Type(Integer32):
    """Custom type alarmMinorBatteryMidpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmMinorBatteryMidpoint_Type.__name__ = "Integer32"
_AlarmMinorBatteryMidpoint_Object = MibScalar
alarmMinorBatteryMidpoint = _AlarmMinorBatteryMidpoint_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 17),
    _AlarmMinorBatteryMidpoint_Type()
)
alarmMinorBatteryMidpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorBatteryMidpoint.setStatus("current")


class _AlarmBatteryLifeEnded_Type(Integer32):
    """Custom type alarmBatteryLifeEnded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmBatteryLifeEnded_Type.__name__ = "Integer32"
_AlarmBatteryLifeEnded_Object = MibScalar
alarmBatteryLifeEnded = _AlarmBatteryLifeEnded_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 18),
    _AlarmBatteryLifeEnded_Type()
)
alarmBatteryLifeEnded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryLifeEnded.setStatus("current")


class _AlarmBatteryTestmodeEntered_Type(Integer32):
    """Custom type alarmBatteryTestmodeEntered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmBatteryTestmodeEntered_Type.__name__ = "Integer32"
_AlarmBatteryTestmodeEntered_Object = MibScalar
alarmBatteryTestmodeEntered = _AlarmBatteryTestmodeEntered_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 19),
    _AlarmBatteryTestmodeEntered_Type()
)
alarmBatteryTestmodeEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryTestmodeEntered.setStatus("current")


class _AlarmBatteryBoostmodeEntered_Type(Integer32):
    """Custom type alarmBatteryBoostmodeEntered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmBatteryBoostmodeEntered_Type.__name__ = "Integer32"
_AlarmBatteryBoostmodeEntered_Object = MibScalar
alarmBatteryBoostmodeEntered = _AlarmBatteryBoostmodeEntered_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 20),
    _AlarmBatteryBoostmodeEntered_Type()
)
alarmBatteryBoostmodeEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryBoostmodeEntered.setStatus("current")


class _AlarmUserConfigurable1_Type(Integer32):
    """Custom type alarmUserConfigurable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable1_Type.__name__ = "Integer32"
_AlarmUserConfigurable1_Object = MibScalar
alarmUserConfigurable1 = _AlarmUserConfigurable1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 21),
    _AlarmUserConfigurable1_Type()
)
alarmUserConfigurable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable1.setStatus("current")


class _AlarmUserConfigurable2_Type(Integer32):
    """Custom type alarmUserConfigurable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable2_Type.__name__ = "Integer32"
_AlarmUserConfigurable2_Object = MibScalar
alarmUserConfigurable2 = _AlarmUserConfigurable2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 22),
    _AlarmUserConfigurable2_Type()
)
alarmUserConfigurable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable2.setStatus("current")


class _AlarmUserConfigurable3_Type(Integer32):
    """Custom type alarmUserConfigurable3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable3_Type.__name__ = "Integer32"
_AlarmUserConfigurable3_Object = MibScalar
alarmUserConfigurable3 = _AlarmUserConfigurable3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 23),
    _AlarmUserConfigurable3_Type()
)
alarmUserConfigurable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable3.setStatus("current")


class _AlarmUserConfigurable4_Type(Integer32):
    """Custom type alarmUserConfigurable4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable4_Type.__name__ = "Integer32"
_AlarmUserConfigurable4_Object = MibScalar
alarmUserConfigurable4 = _AlarmUserConfigurable4_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 24),
    _AlarmUserConfigurable4_Type()
)
alarmUserConfigurable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable4.setStatus("current")


class _AlarmUserConfigurable5_Type(Integer32):
    """Custom type alarmUserConfigurable5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable5_Type.__name__ = "Integer32"
_AlarmUserConfigurable5_Object = MibScalar
alarmUserConfigurable5 = _AlarmUserConfigurable5_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 25),
    _AlarmUserConfigurable5_Type()
)
alarmUserConfigurable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable5.setStatus("current")


class _AlarmUserConfigurable6_Type(Integer32):
    """Custom type alarmUserConfigurable6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable6_Type.__name__ = "Integer32"
_AlarmUserConfigurable6_Object = MibScalar
alarmUserConfigurable6 = _AlarmUserConfigurable6_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 26),
    _AlarmUserConfigurable6_Type()
)
alarmUserConfigurable6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable6.setStatus("current")


class _AlarmUserConfigurable7_Type(Integer32):
    """Custom type alarmUserConfigurable7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable7_Type.__name__ = "Integer32"
_AlarmUserConfigurable7_Object = MibScalar
alarmUserConfigurable7 = _AlarmUserConfigurable7_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 27),
    _AlarmUserConfigurable7_Type()
)
alarmUserConfigurable7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable7.setStatus("current")


class _AlarmUserConfigurable8_Type(Integer32):
    """Custom type alarmUserConfigurable8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable8_Type.__name__ = "Integer32"
_AlarmUserConfigurable8_Object = MibScalar
alarmUserConfigurable8 = _AlarmUserConfigurable8_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 28),
    _AlarmUserConfigurable8_Type()
)
alarmUserConfigurable8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable8.setStatus("current")


class _AlarmUserConfigurable9_Type(Integer32):
    """Custom type alarmUserConfigurable9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable9_Type.__name__ = "Integer32"
_AlarmUserConfigurable9_Object = MibScalar
alarmUserConfigurable9 = _AlarmUserConfigurable9_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 29),
    _AlarmUserConfigurable9_Type()
)
alarmUserConfigurable9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable9.setStatus("current")


class _AlarmUserConfigurable10_Type(Integer32):
    """Custom type alarmUserConfigurable10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable10_Type.__name__ = "Integer32"
_AlarmUserConfigurable10_Object = MibScalar
alarmUserConfigurable10 = _AlarmUserConfigurable10_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 30),
    _AlarmUserConfigurable10_Type()
)
alarmUserConfigurable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable10.setStatus("current")


class _AlarmUserConfigurable11_Type(Integer32):
    """Custom type alarmUserConfigurable11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable11_Type.__name__ = "Integer32"
_AlarmUserConfigurable11_Object = MibScalar
alarmUserConfigurable11 = _AlarmUserConfigurable11_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 31),
    _AlarmUserConfigurable11_Type()
)
alarmUserConfigurable11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable11.setStatus("current")


class _AlarmUserConfigurable12_Type(Integer32):
    """Custom type alarmUserConfigurable12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable12_Type.__name__ = "Integer32"
_AlarmUserConfigurable12_Object = MibScalar
alarmUserConfigurable12 = _AlarmUserConfigurable12_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 32),
    _AlarmUserConfigurable12_Type()
)
alarmUserConfigurable12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable12.setStatus("current")


class _AlarmUserConfigurable13_Type(Integer32):
    """Custom type alarmUserConfigurable13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable13_Type.__name__ = "Integer32"
_AlarmUserConfigurable13_Object = MibScalar
alarmUserConfigurable13 = _AlarmUserConfigurable13_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 33),
    _AlarmUserConfigurable13_Type()
)
alarmUserConfigurable13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable13.setStatus("current")


class _AlarmUserConfigurable14_Type(Integer32):
    """Custom type alarmUserConfigurable14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmUserConfigurable14_Type.__name__ = "Integer32"
_AlarmUserConfigurable14_Object = MibScalar
alarmUserConfigurable14 = _AlarmUserConfigurable14_Object(
    (1, 3, 6, 1, 4, 1, 12148, 7, 7, 1, 34),
    _AlarmUserConfigurable14_Type()
)
alarmUserConfigurable14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserConfigurable14.setStatus("current")

# Managed Objects groups


# Notification objects

alarmMajorHighBattVoltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 1)
)
alarmMajorHighBattVoltTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMajorHighBattVolt")
)
if mibBuilder.loadTexts:
    alarmMajorHighBattVoltTrap.setStatus(
        "current"
    )

alarmMinorHighBattVoltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 2)
)
alarmMinorHighBattVoltTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMinorHighBattVolt")
)
if mibBuilder.loadTexts:
    alarmMinorHighBattVoltTrap.setStatus(
        "current"
    )

alarmMajorLowBattVoltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 3)
)
alarmMajorLowBattVoltTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMajorLowBattVolt")
)
if mibBuilder.loadTexts:
    alarmMajorLowBattVoltTrap.setStatus(
        "current"
    )

alarmMinorLowBattVoltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 4)
)
alarmMinorLowBattVoltTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMinorLowBattVolt")
)
if mibBuilder.loadTexts:
    alarmMinorLowBattVoltTrap.setStatus(
        "current"
    )

alarmMajorBatteryHighTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 5)
)
alarmMajorBatteryHighTempTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMajorBatteryHighTemp")
)
if mibBuilder.loadTexts:
    alarmMajorBatteryHighTempTrap.setStatus(
        "current"
    )

alarmMinorBatteryHighTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 6)
)
alarmMinorBatteryHighTempTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMinorBatteryHighTemp")
)
if mibBuilder.loadTexts:
    alarmMinorBatteryHighTempTrap.setStatus(
        "current"
    )

alarmBatteryDisconnectOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 7)
)
alarmBatteryDisconnectOpenTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmBatteryDisconnectOpen")
)
if mibBuilder.loadTexts:
    alarmBatteryDisconnectOpenTrap.setStatus(
        "current"
    )

alarmLVD1openTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 8)
)
alarmLVD1openTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmLVD1open")
)
if mibBuilder.loadTexts:
    alarmLVD1openTrap.setStatus(
        "current"
    )

alarmLVD2openTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 9)
)
alarmLVD2openTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmLVD2open")
)
if mibBuilder.loadTexts:
    alarmLVD2openTrap.setStatus(
        "current"
    )

alarmLVD3openTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 10)
)
alarmLVD3openTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmLVD3open")
)
if mibBuilder.loadTexts:
    alarmLVD3openTrap.setStatus(
        "current"
    )

alarmACmainsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 11)
)
alarmACmainsTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmACmains")
)
if mibBuilder.loadTexts:
    alarmACmainsTrap.setStatus(
        "current"
    )

alarmBatteryBreakerOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 12)
)
alarmBatteryBreakerOpenTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmBatteryBreakerOpen")
)
if mibBuilder.loadTexts:
    alarmBatteryBreakerOpenTrap.setStatus(
        "current"
    )

alarmDistributionBreakerOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 13)
)
alarmDistributionBreakerOpenTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmDistributionBreakerOpen")
)
if mibBuilder.loadTexts:
    alarmDistributionBreakerOpenTrap.setStatus(
        "current"
    )

alarmMajorRectifierTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 14)
)
alarmMajorRectifierTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMajorRectifier")
)
if mibBuilder.loadTexts:
    alarmMajorRectifierTrap.setStatus(
        "current"
    )

alarmMinorRectifierTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 15)
)
alarmMinorRectifierTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMinorRectifier")
)
if mibBuilder.loadTexts:
    alarmMinorRectifierTrap.setStatus(
        "current"
    )

alarmMajorBatteryMidpointTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 16)
)
alarmMajorBatteryMidpointTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMajorBatteryMidpoint")
)
if mibBuilder.loadTexts:
    alarmMajorBatteryMidpointTrap.setStatus(
        "current"
    )

alarmMinorBatteryMidpointTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 17)
)
alarmMinorBatteryMidpointTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmMinorBatteryMidpoint")
)
if mibBuilder.loadTexts:
    alarmMinorBatteryMidpointTrap.setStatus(
        "current"
    )

alarmBatteryLifeEndedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 18)
)
alarmBatteryLifeEndedTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmBatteryLifeEnded")
)
if mibBuilder.loadTexts:
    alarmBatteryLifeEndedTrap.setStatus(
        "current"
    )

alarmBatteryTestmodeEnteredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 19)
)
alarmBatteryTestmodeEnteredTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmBatteryTestmodeEntered")
)
if mibBuilder.loadTexts:
    alarmBatteryTestmodeEnteredTrap.setStatus(
        "current"
    )

alarmBatteryBoostmodeEnteredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 20)
)
alarmBatteryBoostmodeEnteredTrap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmBatteryBoostmodeEntered")
)
if mibBuilder.loadTexts:
    alarmBatteryBoostmodeEnteredTrap.setStatus(
        "current"
    )

alarmUserConfigurable1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 21)
)
alarmUserConfigurable1Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable1")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable1Trap.setStatus(
        "current"
    )

alarmUserConfigurable2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 22)
)
alarmUserConfigurable2Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable2")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable2Trap.setStatus(
        "current"
    )

alarmUserConfigurable3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 23)
)
alarmUserConfigurable3Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable3")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable3Trap.setStatus(
        "current"
    )

alarmUserConfigurable4Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 24)
)
alarmUserConfigurable4Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable4")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable4Trap.setStatus(
        "current"
    )

alarmUserConfigurable5Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 25)
)
alarmUserConfigurable5Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable5")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable5Trap.setStatus(
        "current"
    )

alarmUserConfigurable6Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 26)
)
alarmUserConfigurable6Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable6")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable6Trap.setStatus(
        "current"
    )

alarmUserConfigurable7Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 27)
)
alarmUserConfigurable7Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable7")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable7Trap.setStatus(
        "current"
    )

alarmUserConfigurable8Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 28)
)
alarmUserConfigurable8Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable8")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable8Trap.setStatus(
        "current"
    )

alarmUserConfigurable9Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 29)
)
alarmUserConfigurable9Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable9")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable9Trap.setStatus(
        "current"
    )

alarmUserConfigurable10Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 30)
)
alarmUserConfigurable10Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable10")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable10Trap.setStatus(
        "current"
    )

alarmUserConfigurable11Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 31)
)
alarmUserConfigurable11Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable11")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable11Trap.setStatus(
        "current"
    )

alarmUserConfigurable12Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 32)
)
alarmUserConfigurable12Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable12")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable12Trap.setStatus(
        "current"
    )

alarmUserConfigurable13Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 33)
)
alarmUserConfigurable13Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable13")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable13Trap.setStatus(
        "current"
    )

alarmUserConfigurable14Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8, 34)
)
alarmUserConfigurable14Trap.setObjects(
    ("ELTEK_GENERIC-MIB", "alarmUserConfigurable14")
)
if mibBuilder.loadTexts:
    alarmUserConfigurable14Trap.setStatus(
        "current"
    )


# Notifications groups

dcSystemTraps = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12148, 7, 8)
)
dcSystemTraps.setObjects(
      *(("ELTEK_GENERIC-MIB", "alarmMajorHighBattVoltTrap"),
        ("ELTEK_GENERIC-MIB", "alarmMinorHighBattVoltTrap"),
        ("ELTEK_GENERIC-MIB", "alarmMajorLowBattVoltTrap"),
        ("ELTEK_GENERIC-MIB", "alarmMinorLowBattVoltTrap"),
        ("ELTEK_GENERIC-MIB", "alarmMajorBatteryHighTempTrap"),
        ("ELTEK_GENERIC-MIB", "alarmMinorBatteryHighTempTrap"),
        ("ELTEK_GENERIC-MIB", "alarmBatteryDisconnectOpenTrap"),
        ("ELTEK_GENERIC-MIB", "alarmLVD1openTrap"),
        ("ELTEK_GENERIC-MIB", "alarmLVD2openTrap"),
        ("ELTEK_GENERIC-MIB", "alarmLVD3openTrap"),
        ("ELTEK_GENERIC-MIB", "alarmACmainsTrap"),
        ("ELTEK_GENERIC-MIB", "alarmBatteryBreakerOpenTrap"),
        ("ELTEK_GENERIC-MIB", "alarmDistributionBreakerOpenTrap"),
        ("ELTEK_GENERIC-MIB", "alarmMajorRectifierTrap"),
        ("ELTEK_GENERIC-MIB", "alarmMinorRectifierTrap"),
        ("ELTEK_GENERIC-MIB", "alarmMajorBatteryMidpointTrap"),
        ("ELTEK_GENERIC-MIB", "alarmMinorBatteryMidpointTrap"),
        ("ELTEK_GENERIC-MIB", "alarmBatteryLifeEndedTrap"),
        ("ELTEK_GENERIC-MIB", "alarmBatteryTestmodeEnteredTrap"),
        ("ELTEK_GENERIC-MIB", "alarmBatteryBoostmodeEnteredTrap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable1Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable2Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable3Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable4Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable5Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable6Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable7Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable8Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable9Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable10Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable11Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable12Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable13Trap"),
        ("ELTEK_GENERIC-MIB", "alarmUserConfigurable14Trap"))
)
if mibBuilder.loadTexts:
    dcSystemTraps.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEK_GENERIC-MIB",
    **{"eltekPlant": eltekPlant,
       "controlSystem": controlSystem,
       "systemTime": systemTime,
       "systemTimeTime": systemTimeTime,
       "systemInfoRefresh": systemInfoRefresh,
       "systemTrapRepeatRate": systemTrapRepeatRate,
       "systemSendOffTrap": systemSendOffTrap,
       "dcSystem": dcSystem,
       "dcPlant": dcPlant,
       "systemSiteInfo": systemSiteInfo,
       "systemSiteInfoCustomer": systemSiteInfoCustomer,
       "systemSiteInfoLocation": systemSiteInfoLocation,
       "systemSiteInfoMessage1": systemSiteInfoMessage1,
       "systemSiteInfoMessage2": systemSiteInfoMessage2,
       "systemSiteInfoInstalledDate": systemSiteInfoInstalledDate,
       "systemSiteInfoControllerType": systemSiteInfoControllerType,
       "systemSiteInfoSystemSeriaNum": systemSiteInfoSystemSeriaNum,
       "systemSiteInfoControllerSeriaNum": systemSiteInfoControllerSeriaNum,
       "systemNominalVoltage": systemNominalVoltage,
       "systemOperationalStatus": systemOperationalStatus,
       "battery": battery,
       "batteryName": batteryName,
       "batteryVoltage": batteryVoltage,
       "batteryCurrent": batteryCurrent,
       "batteryTemp": batteryTemp,
       "batteryBreakerStatus": batteryBreakerStatus,
       "batteryChargeCurrentLimitCtrl": batteryChargeCurrentLimitCtrl,
       "batteryChargeCurrentLimitValue": batteryChargeCurrentLimitValue,
       "batteryTempCompEnable": batteryTempCompEnable,
       "batteryFloatVoltConfig": batteryFloatVoltConfig,
       "batteryEqualizeVoltConfig": batteryEqualizeVoltConfig,
       "batteryHighMajorAlarmVoltageConfig": batteryHighMajorAlarmVoltageConfig,
       "batteryHighMinorAlarmVoltageConfig": batteryHighMinorAlarmVoltageConfig,
       "batteryLowMajorAlarmVoltageConfig": batteryLowMajorAlarmVoltageConfig,
       "batteryLowMinorAlarmVoltageConfig": batteryLowMinorAlarmVoltageConfig,
       "batteryStartManualTest": batteryStartManualTest,
       "batteryStartManualBoost": batteryStartManualBoost,
       "batteryLVD": batteryLVD,
       "batteryLVDStatus": batteryLVDStatus,
       "batteryLVDDisconnectVoltage": batteryLVDDisconnectVoltage,
       "batteryLVDConnectVoltage": batteryLVDConnectVoltage,
       "batteryMidpoint": batteryMidpoint,
       "batteryMidpointDeltaLimitVoltage": batteryMidpointDeltaLimitVoltage,
       "batteryMidpointIndex": batteryMidpointIndex,
       "batteryMidpointControlTable": batteryMidpointControlTable,
       "batteryMidpointControlEntry": batteryMidpointControlEntry,
       "midpointEnableID": midpointEnableID,
       "midpointEnable": midpointEnable,
       "batteryMidpointStatusTable": batteryMidpointStatusTable,
       "batteryMidpointStatusEntry": batteryMidpointStatusEntry,
       "midpointStatusID": midpointStatusID,
       "midpointStatus": midpointStatus,
       "midpointDeltaVoltage": midpointDeltaVoltage,
       "loadDistribution": loadDistribution,
       "loadDistributionCurrent": loadDistributionCurrent,
       "loadDistributionBreakerStatus": loadDistributionBreakerStatus,
       "loadDistributionLVDStatus": loadDistributionLVDStatus,
       "loadLVD1EnableStatus": loadLVD1EnableStatus,
       "loadLVD1Status": loadLVD1Status,
       "loadLVD1ConnectVoltage": loadLVD1ConnectVoltage,
       "loadLVD1DisconnectVoltage": loadLVD1DisconnectVoltage,
       "loadLVD2EnableStatus": loadLVD2EnableStatus,
       "loadLVD2Status": loadLVD2Status,
       "loadLVD2ConnectVoltage": loadLVD2ConnectVoltage,
       "loadLVD2DisconnectVoltage": loadLVD2DisconnectVoltage,
       "loadLVD3EnableStatus": loadLVD3EnableStatus,
       "loadLVD3Status": loadLVD3Status,
       "loadLVD3ConnectVoltage": loadLVD3ConnectVoltage,
       "loadLVD3DisconnectVoltage": loadLVD3DisconnectVoltage,
       "rectifier": rectifier,
       "rectifierInstalledRectifiers": rectifierInstalledRectifiers,
       "rectifierRectifiersActive": rectifierRectifiersActive,
       "rectifierTotalCurrent": rectifierTotalCurrent,
       "rectifierUtilization": rectifierUtilization,
       "rectifierStatus": rectifierStatus,
       "rectifierStatusNoIndex": rectifierStatusNoIndex,
       "rectifierStatusTable": rectifierStatusTable,
       "rectifierStatusEntry": rectifierStatusEntry,
       "rectifierStatusID": rectifierStatusID,
       "rectifierStatusStatus": rectifierStatusStatus,
       "rectifierStatusOutputCurrent": rectifierStatusOutputCurrent,
       "rectifierStatusOutputVoltage": rectifierStatusOutputVoltage,
       "rectifierStatusTemp": rectifierStatusTemp,
       "rectifierStatusType": rectifierStatusType,
       "rectifierStatusSKU": rectifierStatusSKU,
       "rectifierStatusSerialNo": rectifierStatusSerialNo,
       "rectifierStatusRevisionLevel": rectifierStatusRevisionLevel,
       "acDistribution": acDistribution,
       "acVoltage1": acVoltage1,
       "acVoltage2": acVoltage2,
       "acVoltage3": acVoltage3,
       "alarmGroup": alarmGroup,
       "alarmWellknownAlarms": alarmWellknownAlarms,
       "alarmMajorHighBattVolt": alarmMajorHighBattVolt,
       "alarmMinorHighBattVolt": alarmMinorHighBattVolt,
       "alarmMajorLowBattVolt": alarmMajorLowBattVolt,
       "alarmMinorLowBattVolt": alarmMinorLowBattVolt,
       "alarmMajorBatteryHighTemp": alarmMajorBatteryHighTemp,
       "alarmMinorBatteryHighTemp": alarmMinorBatteryHighTemp,
       "alarmBatteryDisconnectOpen": alarmBatteryDisconnectOpen,
       "alarmLVD1open": alarmLVD1open,
       "alarmLVD2open": alarmLVD2open,
       "alarmLVD3open": alarmLVD3open,
       "alarmACmains": alarmACmains,
       "alarmBatteryBreakerOpen": alarmBatteryBreakerOpen,
       "alarmDistributionBreakerOpen": alarmDistributionBreakerOpen,
       "alarmMajorRectifier": alarmMajorRectifier,
       "alarmMinorRectifier": alarmMinorRectifier,
       "alarmMajorBatteryMidpoint": alarmMajorBatteryMidpoint,
       "alarmMinorBatteryMidpoint": alarmMinorBatteryMidpoint,
       "alarmBatteryLifeEnded": alarmBatteryLifeEnded,
       "alarmBatteryTestmodeEntered": alarmBatteryTestmodeEntered,
       "alarmBatteryBoostmodeEntered": alarmBatteryBoostmodeEntered,
       "alarmUserConfigurable1": alarmUserConfigurable1,
       "alarmUserConfigurable2": alarmUserConfigurable2,
       "alarmUserConfigurable3": alarmUserConfigurable3,
       "alarmUserConfigurable4": alarmUserConfigurable4,
       "alarmUserConfigurable5": alarmUserConfigurable5,
       "alarmUserConfigurable6": alarmUserConfigurable6,
       "alarmUserConfigurable7": alarmUserConfigurable7,
       "alarmUserConfigurable8": alarmUserConfigurable8,
       "alarmUserConfigurable9": alarmUserConfigurable9,
       "alarmUserConfigurable10": alarmUserConfigurable10,
       "alarmUserConfigurable11": alarmUserConfigurable11,
       "alarmUserConfigurable12": alarmUserConfigurable12,
       "alarmUserConfigurable13": alarmUserConfigurable13,
       "alarmUserConfigurable14": alarmUserConfigurable14,
       "dcSystemTraps": dcSystemTraps,
       "alarmMajorHighBattVoltTrap": alarmMajorHighBattVoltTrap,
       "alarmMinorHighBattVoltTrap": alarmMinorHighBattVoltTrap,
       "alarmMajorLowBattVoltTrap": alarmMajorLowBattVoltTrap,
       "alarmMinorLowBattVoltTrap": alarmMinorLowBattVoltTrap,
       "alarmMajorBatteryHighTempTrap": alarmMajorBatteryHighTempTrap,
       "alarmMinorBatteryHighTempTrap": alarmMinorBatteryHighTempTrap,
       "alarmBatteryDisconnectOpenTrap": alarmBatteryDisconnectOpenTrap,
       "alarmLVD1openTrap": alarmLVD1openTrap,
       "alarmLVD2openTrap": alarmLVD2openTrap,
       "alarmLVD3openTrap": alarmLVD3openTrap,
       "alarmACmainsTrap": alarmACmainsTrap,
       "alarmBatteryBreakerOpenTrap": alarmBatteryBreakerOpenTrap,
       "alarmDistributionBreakerOpenTrap": alarmDistributionBreakerOpenTrap,
       "alarmMajorRectifierTrap": alarmMajorRectifierTrap,
       "alarmMinorRectifierTrap": alarmMinorRectifierTrap,
       "alarmMajorBatteryMidpointTrap": alarmMajorBatteryMidpointTrap,
       "alarmMinorBatteryMidpointTrap": alarmMinorBatteryMidpointTrap,
       "alarmBatteryLifeEndedTrap": alarmBatteryLifeEndedTrap,
       "alarmBatteryTestmodeEnteredTrap": alarmBatteryTestmodeEnteredTrap,
       "alarmBatteryBoostmodeEnteredTrap": alarmBatteryBoostmodeEnteredTrap,
       "alarmUserConfigurable1Trap": alarmUserConfigurable1Trap,
       "alarmUserConfigurable2Trap": alarmUserConfigurable2Trap,
       "alarmUserConfigurable3Trap": alarmUserConfigurable3Trap,
       "alarmUserConfigurable4Trap": alarmUserConfigurable4Trap,
       "alarmUserConfigurable5Trap": alarmUserConfigurable5Trap,
       "alarmUserConfigurable6Trap": alarmUserConfigurable6Trap,
       "alarmUserConfigurable7Trap": alarmUserConfigurable7Trap,
       "alarmUserConfigurable8Trap": alarmUserConfigurable8Trap,
       "alarmUserConfigurable9Trap": alarmUserConfigurable9Trap,
       "alarmUserConfigurable10Trap": alarmUserConfigurable10Trap,
       "alarmUserConfigurable11Trap": alarmUserConfigurable11Trap,
       "alarmUserConfigurable12Trap": alarmUserConfigurable12Trap,
       "alarmUserConfigurable13Trap": alarmUserConfigurable13Trap,
       "alarmUserConfigurable14Trap": alarmUserConfigurable14Trap}
)
