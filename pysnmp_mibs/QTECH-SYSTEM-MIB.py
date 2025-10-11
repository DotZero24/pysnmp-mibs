# SNMP MIB module (QTECH-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:39 2025
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

(qtechApMacAddr,) = mibBuilder.importSymbols(
    "QTECH-AC-MGMT-MIB",
    "qtechApMacAddr")

(qtechMemoryPoolCurrentUtilization,) = mibBuilder.importSymbols(
    "QTECH-MEMORY-MIB",
    "qtechMemoryPoolCurrentUtilization")

(Percent,
 qtechCPUUtilization1Min) = mibBuilder.importSymbols(
    "QTECH-PROCESS-MIB",
    "Percent",
    "qtechCPUUtilization1Min")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    qtechSystemMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechSystemMIBObjects_ObjectIdentity = ObjectIdentity
qtechSystemMIBObjects = _QtechSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1)
)


class _QtechSystemHwVersion_Type(DisplayString):
    """Custom type qtechSystemHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSystemHwVersion_Type.__name__ = "DisplayString"
_QtechSystemHwVersion_Object = MibScalar
qtechSystemHwVersion = _QtechSystemHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 1),
    _QtechSystemHwVersion_Type()
)
qtechSystemHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemHwVersion.setStatus("current")


class _QtechSystemSwVersion_Type(DisplayString):
    """Custom type qtechSystemSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSystemSwVersion_Type.__name__ = "DisplayString"
_QtechSystemSwVersion_Object = MibScalar
qtechSystemSwVersion = _QtechSystemSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 2),
    _QtechSystemSwVersion_Type()
)
qtechSystemSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemSwVersion.setStatus("current")


class _QtechSystemBootVersion_Type(DisplayString):
    """Custom type qtechSystemBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSystemBootVersion_Type.__name__ = "DisplayString"
_QtechSystemBootVersion_Object = MibScalar
qtechSystemBootVersion = _QtechSystemBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 3),
    _QtechSystemBootVersion_Type()
)
qtechSystemBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemBootVersion.setStatus("current")


class _QtechSystemSysCtrlVersion_Type(DisplayString):
    """Custom type qtechSystemSysCtrlVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSystemSysCtrlVersion_Type.__name__ = "DisplayString"
_QtechSystemSysCtrlVersion_Object = MibScalar
qtechSystemSysCtrlVersion = _QtechSystemSysCtrlVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 4),
    _QtechSystemSysCtrlVersion_Type()
)
qtechSystemSysCtrlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemSysCtrlVersion.setStatus("current")
_QtechSystemParametersSave_Type = Integer32
_QtechSystemParametersSave_Object = MibScalar
qtechSystemParametersSave = _QtechSystemParametersSave_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 5),
    _QtechSystemParametersSave_Type()
)
qtechSystemParametersSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemParametersSave.setStatus("current")


class _QtechSystemOutBandRate_Type(Integer32):
    """Custom type qtechSystemOutBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud9600", 1),
          ("baud19200", 2),
          ("baud38400", 3),
          ("baud57600", 4),
          ("baud115200", 5))
    )


_QtechSystemOutBandRate_Type.__name__ = "Integer32"
_QtechSystemOutBandRate_Object = MibScalar
qtechSystemOutBandRate = _QtechSystemOutBandRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 6),
    _QtechSystemOutBandRate_Type()
)
qtechSystemOutBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemOutBandRate.setStatus("current")


class _QtechSystemReset_Type(Integer32):
    """Custom type qtechSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("restart", 1))
    )


_QtechSystemReset_Type.__name__ = "Integer32"
_QtechSystemReset_Object = MibScalar
qtechSystemReset = _QtechSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 7),
    _QtechSystemReset_Type()
)
qtechSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemReset.setStatus("current")


class _QtechSwitchLayer_Type(Integer32):
    """Custom type qtechSwitchLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2),
          ("router", 3))
    )


_QtechSwitchLayer_Type.__name__ = "Integer32"
_QtechSwitchLayer_Object = MibScalar
qtechSwitchLayer = _QtechSwitchLayer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 8),
    _QtechSwitchLayer_Type()
)
qtechSwitchLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSwitchLayer.setStatus("current")


class _QtechSystemHwPower_Type(Integer32):
    """Custom type qtechSystemHwPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rpsNoLink", 1),
          ("rpsLinkAndNoPower", 2),
          ("rpsLinkAndReadyForPower", 3),
          ("rpsLinkAndPower", 4))
    )


_QtechSystemHwPower_Type.__name__ = "Integer32"
_QtechSystemHwPower_Object = MibScalar
qtechSystemHwPower = _QtechSystemHwPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 9),
    _QtechSystemHwPower_Type()
)
qtechSystemHwPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemHwPower.setStatus("current")


class _QtechSystemHwFan_Type(Integer32):
    """Custom type qtechSystemHwFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("work", 1),
          ("stop", 2))
    )


_QtechSystemHwFan_Type.__name__ = "Integer32"
_QtechSystemHwFan_Object = MibScalar
qtechSystemHwFan = _QtechSystemHwFan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 10),
    _QtechSystemHwFan_Type()
)
qtechSystemHwFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemHwFan.setStatus("current")


class _QtechSystemOutBandTimeout_Type(Integer32):
    """Custom type qtechSystemOutBandTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_QtechSystemOutBandTimeout_Type.__name__ = "Integer32"
_QtechSystemOutBandTimeout_Object = MibScalar
qtechSystemOutBandTimeout = _QtechSystemOutBandTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 11),
    _QtechSystemOutBandTimeout_Type()
)
qtechSystemOutBandTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemOutBandTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    qtechSystemOutBandTimeout.setUnits("seconds")


class _QtechSystemTelnetTimeout_Type(Integer32):
    """Custom type qtechSystemTelnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_QtechSystemTelnetTimeout_Type.__name__ = "Integer32"
_QtechSystemTelnetTimeout_Object = MibScalar
qtechSystemTelnetTimeout = _QtechSystemTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 12),
    _QtechSystemTelnetTimeout_Type()
)
qtechSystemTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemTelnetTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    qtechSystemTelnetTimeout.setUnits("seconds")


class _QtechSystemMainFile_Type(DisplayString):
    """Custom type qtechSystemMainFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechSystemMainFile_Type.__name__ = "DisplayString"
_QtechSystemMainFile_Object = MibScalar
qtechSystemMainFile = _QtechSystemMainFile_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 13),
    _QtechSystemMainFile_Type()
)
qtechSystemMainFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemMainFile.setStatus("current")
_QtechSystemCurrentPower_Type = Integer32
_QtechSystemCurrentPower_Object = MibScalar
qtechSystemCurrentPower = _QtechSystemCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 14),
    _QtechSystemCurrentPower_Type()
)
qtechSystemCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemCurrentPower.setStatus("current")
_QtechSystemRemainPower_Type = Integer32
_QtechSystemRemainPower_Object = MibScalar
qtechSystemRemainPower = _QtechSystemRemainPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 15),
    _QtechSystemRemainPower_Type()
)
qtechSystemRemainPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemRemainPower.setStatus("current")
_QtechSystemTemperature_Type = Integer32
_QtechSystemTemperature_Object = MibScalar
qtechSystemTemperature = _QtechSystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 16),
    _QtechSystemTemperature_Type()
)
qtechSystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemTemperature.setStatus("current")
_QtechSystemElectricalSourceNum_Type = Integer32
_QtechSystemElectricalSourceNum_Object = MibScalar
qtechSystemElectricalSourceNum = _QtechSystemElectricalSourceNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 17),
    _QtechSystemElectricalSourceNum_Type()
)
qtechSystemElectricalSourceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalSourceNum.setStatus("current")
_QtechSystemElectricalSourceIsNormalTable_Object = MibTable
qtechSystemElectricalSourceIsNormalTable = _QtechSystemElectricalSourceIsNormalTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 18)
)
if mibBuilder.loadTexts:
    qtechSystemElectricalSourceIsNormalTable.setStatus("current")
_QtechSystemElectricalSourceIsNormalEntry_Object = MibTableRow
qtechSystemElectricalSourceIsNormalEntry = _QtechSystemElectricalSourceIsNormalEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 18, 1)
)
qtechSystemElectricalSourceIsNormalEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemElectricalSourceIsNormalIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemElectricalSourceIsNormalEntry.setStatus("current")
_QtechSystemElectricalSourceIsNormalIndex_Type = Integer32
_QtechSystemElectricalSourceIsNormalIndex_Object = MibTableColumn
qtechSystemElectricalSourceIsNormalIndex = _QtechSystemElectricalSourceIsNormalIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 18, 1, 1),
    _QtechSystemElectricalSourceIsNormalIndex_Type()
)
qtechSystemElectricalSourceIsNormalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalSourceIsNormalIndex.setStatus("current")


class _QtechSystemElectricalSourceIsNormal_Type(Integer32):
    """Custom type qtechSystemElectricalSourceIsNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6))
    )


_QtechSystemElectricalSourceIsNormal_Type.__name__ = "Integer32"
_QtechSystemElectricalSourceIsNormal_Object = MibTableColumn
qtechSystemElectricalSourceIsNormal = _QtechSystemElectricalSourceIsNormal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 18, 1, 2),
    _QtechSystemElectricalSourceIsNormal_Type()
)
qtechSystemElectricalSourceIsNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalSourceIsNormal.setStatus("current")
_QtechSystemElectricalSourceName_Type = DisplayString
_QtechSystemElectricalSourceName_Object = MibTableColumn
qtechSystemElectricalSourceName = _QtechSystemElectricalSourceName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 18, 1, 3),
    _QtechSystemElectricalSourceName_Type()
)
qtechSystemElectricalSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalSourceName.setStatus("current")
_QtechSystemCurrentVoltage_Type = Integer32
_QtechSystemCurrentVoltage_Object = MibScalar
qtechSystemCurrentVoltage = _QtechSystemCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 19),
    _QtechSystemCurrentVoltage_Type()
)
qtechSystemCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemCurrentVoltage.setStatus("current")
_QtechSystemFanNUM_Type = Integer32
_QtechSystemFanNUM_Object = MibScalar
qtechSystemFanNUM = _QtechSystemFanNUM_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 20),
    _QtechSystemFanNUM_Type()
)
qtechSystemFanNUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanNUM.setStatus("current")
_QtechSystemFanIsNormalTable_Object = MibTable
qtechSystemFanIsNormalTable = _QtechSystemFanIsNormalTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 21)
)
if mibBuilder.loadTexts:
    qtechSystemFanIsNormalTable.setStatus("current")
_QtechSystemFanIsNormalEntry_Object = MibTableRow
qtechSystemFanIsNormalEntry = _QtechSystemFanIsNormalEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 21, 1)
)
qtechSystemFanIsNormalEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemFanIsNormalIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemFanIsNormalEntry.setStatus("current")
_QtechSystemFanIsNormalIndex_Type = Integer32
_QtechSystemFanIsNormalIndex_Object = MibTableColumn
qtechSystemFanIsNormalIndex = _QtechSystemFanIsNormalIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 21, 1, 1),
    _QtechSystemFanIsNormalIndex_Type()
)
qtechSystemFanIsNormalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanIsNormalIndex.setStatus("current")


class _QtechSystemFanIsNormal_Type(Integer32):
    """Custom type qtechSystemFanIsNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6))
    )


_QtechSystemFanIsNormal_Type.__name__ = "Integer32"
_QtechSystemFanIsNormal_Object = MibTableColumn
qtechSystemFanIsNormal = _QtechSystemFanIsNormal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 21, 1, 2),
    _QtechSystemFanIsNormal_Type()
)
qtechSystemFanIsNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanIsNormal.setStatus("current")
_QtechSystemFanName_Type = DisplayString
_QtechSystemFanName_Object = MibTableColumn
qtechSystemFanName = _QtechSystemFanName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 21, 1, 3),
    _QtechSystemFanName_Type()
)
qtechSystemFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanName.setStatus("current")
_QtechSystemFanSpeed_Type = Integer32
_QtechSystemFanSpeed_Object = MibTableColumn
qtechSystemFanSpeed = _QtechSystemFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 21, 1, 4),
    _QtechSystemFanSpeed_Type()
)
qtechSystemFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanSpeed.setStatus("current")
_QtechSystemReloadTimeRemain_Type = Integer32
_QtechSystemReloadTimeRemain_Object = MibScalar
qtechSystemReloadTimeRemain = _QtechSystemReloadTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 22),
    _QtechSystemReloadTimeRemain_Type()
)
qtechSystemReloadTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemReloadTimeRemain.setStatus("current")
_QtechSystemTemperatureTable_Object = MibTable
qtechSystemTemperatureTable = _QtechSystemTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 23)
)
if mibBuilder.loadTexts:
    qtechSystemTemperatureTable.setStatus("current")
_QtechSystemTemperatureEntry_Object = MibTableRow
qtechSystemTemperatureEntry = _QtechSystemTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 23, 1)
)
qtechSystemTemperatureEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemTemperatureIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemTemperatureEntry.setStatus("current")
_QtechSystemTemperatureIndex_Type = Integer32
_QtechSystemTemperatureIndex_Object = MibTableColumn
qtechSystemTemperatureIndex = _QtechSystemTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 23, 1, 1),
    _QtechSystemTemperatureIndex_Type()
)
qtechSystemTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemTemperatureIndex.setStatus("current")
_QtechSystemTemperatureName_Type = DisplayString
_QtechSystemTemperatureName_Object = MibTableColumn
qtechSystemTemperatureName = _QtechSystemTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 23, 1, 2),
    _QtechSystemTemperatureName_Type()
)
qtechSystemTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemTemperatureName.setStatus("current")
_QtechSystemTemperatureCurrent_Type = Integer32
_QtechSystemTemperatureCurrent_Object = MibTableColumn
qtechSystemTemperatureCurrent = _QtechSystemTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 23, 1, 3),
    _QtechSystemTemperatureCurrent_Type()
)
qtechSystemTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemTemperatureCurrent.setStatus("current")
_QtechSystemTemperatureWarningVaule_Type = Integer32
_QtechSystemTemperatureWarningVaule_Object = MibTableColumn
qtechSystemTemperatureWarningVaule = _QtechSystemTemperatureWarningVaule_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 23, 1, 4),
    _QtechSystemTemperatureWarningVaule_Type()
)
qtechSystemTemperatureWarningVaule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemTemperatureWarningVaule.setStatus("current")
_QtechSystemTemperatureCritialVaule_Type = Integer32
_QtechSystemTemperatureCritialVaule_Object = MibTableColumn
qtechSystemTemperatureCritialVaule = _QtechSystemTemperatureCritialVaule_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 23, 1, 5),
    _QtechSystemTemperatureCritialVaule_Type()
)
qtechSystemTemperatureCritialVaule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemTemperatureCritialVaule.setStatus("current")
_QtechSystemSerialno_Type = DisplayString
_QtechSystemSerialno_Object = MibScalar
qtechSystemSerialno = _QtechSystemSerialno_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 24),
    _QtechSystemSerialno_Type()
)
qtechSystemSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemSerialno.setStatus("current")
_QtechSystemVersionTable_Object = MibTable
qtechSystemVersionTable = _QtechSystemVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 25)
)
if mibBuilder.loadTexts:
    qtechSystemVersionTable.setStatus("current")
_QtechSystemVersionEntry_Object = MibTableRow
qtechSystemVersionEntry = _QtechSystemVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 25, 1)
)
qtechSystemVersionEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemVersionIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemVersionEntry.setStatus("current")
_QtechSystemVersionIndex_Type = Unsigned32
_QtechSystemVersionIndex_Object = MibTableColumn
qtechSystemVersionIndex = _QtechSystemVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 25, 1, 1),
    _QtechSystemVersionIndex_Type()
)
qtechSystemVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemVersionIndex.setStatus("current")
_QtechSystemVersionName_Type = DisplayString
_QtechSystemVersionName_Object = MibTableColumn
qtechSystemVersionName = _QtechSystemVersionName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 25, 1, 2),
    _QtechSystemVersionName_Type()
)
qtechSystemVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemVersionName.setStatus("current")
_QtechSystemVersionSwBoot_Type = DisplayString
_QtechSystemVersionSwBoot_Object = MibTableColumn
qtechSystemVersionSwBoot = _QtechSystemVersionSwBoot_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 25, 1, 3),
    _QtechSystemVersionSwBoot_Type()
)
qtechSystemVersionSwBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemVersionSwBoot.setStatus("current")
_QtechSystemVersionSwCtrl_Type = DisplayString
_QtechSystemVersionSwCtrl_Object = MibTableColumn
qtechSystemVersionSwCtrl = _QtechSystemVersionSwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 25, 1, 4),
    _QtechSystemVersionSwCtrl_Type()
)
qtechSystemVersionSwCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemVersionSwCtrl.setStatus("current")
_QtechSystemVersionSwMain_Type = DisplayString
_QtechSystemVersionSwMain_Object = MibTableColumn
qtechSystemVersionSwMain = _QtechSystemVersionSwMain_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 25, 1, 5),
    _QtechSystemVersionSwMain_Type()
)
qtechSystemVersionSwMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemVersionSwMain.setStatus("current")
_QtechSystemVersionHw_Type = DisplayString
_QtechSystemVersionHw_Object = MibTableColumn
qtechSystemVersionHw = _QtechSystemVersionHw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 25, 1, 6),
    _QtechSystemVersionHw_Type()
)
qtechSystemVersionHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemVersionHw.setStatus("current")
_QtechSystemVersionSerialno_Type = DisplayString
_QtechSystemVersionSerialno_Object = MibTableColumn
qtechSystemVersionSerialno = _QtechSystemVersionSerialno_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 25, 1, 7),
    _QtechSystemVersionSerialno_Type()
)
qtechSystemVersionSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemVersionSerialno.setStatus("current")
_QtechSystemSysModel_Type = DisplayString
_QtechSystemSysModel_Object = MibScalar
qtechSystemSysModel = _QtechSystemSysModel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 26),
    _QtechSystemSysModel_Type()
)
qtechSystemSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemSysModel.setStatus("current")
_QtechSystemUptime_Type = Integer32
_QtechSystemUptime_Object = MibScalar
qtechSystemUptime = _QtechSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 27),
    _QtechSystemUptime_Type()
)
qtechSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemUptime.setStatus("current")
_QtechSystemSampleTime_Type = Integer32
_QtechSystemSampleTime_Object = MibScalar
qtechSystemSampleTime = _QtechSystemSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 28),
    _QtechSystemSampleTime_Type()
)
qtechSystemSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemSampleTime.setStatus("current")
_QtechSystemStatWindowTime_Type = Integer32
_QtechSystemStatWindowTime_Object = MibScalar
qtechSystemStatWindowTime = _QtechSystemStatWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 29),
    _QtechSystemStatWindowTime_Type()
)
qtechSystemStatWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemStatWindowTime.setStatus("current")
_QtechSystemManufacturer_Type = DisplayString
_QtechSystemManufacturer_Object = MibScalar
qtechSystemManufacturer = _QtechSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 30),
    _QtechSystemManufacturer_Type()
)
qtechSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemManufacturer.setStatus("current")
_QtechSystemCurrentTime_Type = DisplayString
_QtechSystemCurrentTime_Object = MibScalar
qtechSystemCurrentTime = _QtechSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 31),
    _QtechSystemCurrentTime_Type()
)
qtechSystemCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemCurrentTime.setStatus("current")
_QtechSystemWarnResendTime_Type = Integer32
_QtechSystemWarnResendTime_Object = MibScalar
qtechSystemWarnResendTime = _QtechSystemWarnResendTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 32),
    _QtechSystemWarnResendTime_Type()
)
qtechSystemWarnResendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemWarnResendTime.setStatus("current")
_QtechSystemSoftwareName_Type = DisplayString
_QtechSystemSoftwareName_Object = MibScalar
qtechSystemSoftwareName = _QtechSystemSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 33),
    _QtechSystemSoftwareName_Type()
)
qtechSystemSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemSoftwareName.setStatus("current")
_QtechSystemSoftwareManufacturer_Type = DisplayString
_QtechSystemSoftwareManufacturer_Object = MibScalar
qtechSystemSoftwareManufacturer = _QtechSystemSoftwareManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 34),
    _QtechSystemSoftwareManufacturer_Type()
)
qtechSystemSoftwareManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemSoftwareManufacturer.setStatus("current")
_QtechSystemCpuType_Type = DisplayString
_QtechSystemCpuType_Object = MibScalar
qtechSystemCpuType = _QtechSystemCpuType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 35),
    _QtechSystemCpuType_Type()
)
qtechSystemCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemCpuType.setStatus("current")
_QtechSystemMemoryType_Type = DisplayString
_QtechSystemMemoryType_Object = MibScalar
qtechSystemMemoryType = _QtechSystemMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 36),
    _QtechSystemMemoryType_Type()
)
qtechSystemMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemMemoryType.setStatus("current")
_QtechSystemMemorySize_Type = Gauge32
_QtechSystemMemorySize_Object = MibScalar
qtechSystemMemorySize = _QtechSystemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 37),
    _QtechSystemMemorySize_Type()
)
qtechSystemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemMemorySize.setStatus("current")
_QtechSystemFlashSize_Type = Gauge32
_QtechSystemFlashSize_Object = MibScalar
qtechSystemFlashSize = _QtechSystemFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 38),
    _QtechSystemFlashSize_Type()
)
qtechSystemFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFlashSize.setStatus("current")
_QtechSystemLankApTable_Object = MibTable
qtechSystemLankApTable = _QtechSystemLankApTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39)
)
if mibBuilder.loadTexts:
    qtechSystemLankApTable.setStatus("current")
_QtechSystemLankApEntry_Object = MibTableRow
qtechSystemLankApEntry = _QtechSystemLankApEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1)
)
qtechSystemLankApEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemLankApMacAddr"),
)
if mibBuilder.loadTexts:
    qtechSystemLankApEntry.setStatus("current")
_QtechSystemLankApMacAddr_Type = MacAddress
_QtechSystemLankApMacAddr_Object = MibTableColumn
qtechSystemLankApMacAddr = _QtechSystemLankApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 1),
    _QtechSystemLankApMacAddr_Type()
)
qtechSystemLankApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApMacAddr.setStatus("current")
_QtechSystemLankApStatWindowTime_Type = Integer32
_QtechSystemLankApStatWindowTime_Object = MibTableColumn
qtechSystemLankApStatWindowTime = _QtechSystemLankApStatWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 2),
    _QtechSystemLankApStatWindowTime_Type()
)
qtechSystemLankApStatWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemLankApStatWindowTime.setStatus("current")
_QtechSystemLankApSampleTime_Type = Integer32
_QtechSystemLankApSampleTime_Object = MibTableColumn
qtechSystemLankApSampleTime = _QtechSystemLankApSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 3),
    _QtechSystemLankApSampleTime_Type()
)
qtechSystemLankApSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemLankApSampleTime.setStatus("current")


class _QtechSystemLankApReset_Type(Integer32):
    """Custom type qtechSystemLankApReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("restart", 1))
    )


_QtechSystemLankApReset_Type.__name__ = "Integer32"
_QtechSystemLankApReset_Object = MibTableColumn
qtechSystemLankApReset = _QtechSystemLankApReset_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 4),
    _QtechSystemLankApReset_Type()
)
qtechSystemLankApReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemLankApReset.setStatus("current")
_QtechSystemLankApSoftwareName_Type = DisplayString
_QtechSystemLankApSoftwareName_Object = MibTableColumn
qtechSystemLankApSoftwareName = _QtechSystemLankApSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 5),
    _QtechSystemLankApSoftwareName_Type()
)
qtechSystemLankApSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApSoftwareName.setStatus("current")


class _QtechSystemLankApSwVersion_Type(DisplayString):
    """Custom type qtechSystemLankApSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSystemLankApSwVersion_Type.__name__ = "DisplayString"
_QtechSystemLankApSwVersion_Object = MibTableColumn
qtechSystemLankApSwVersion = _QtechSystemLankApSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 6),
    _QtechSystemLankApSwVersion_Type()
)
qtechSystemLankApSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApSwVersion.setStatus("current")
_QtechSystemLankApSoftwareManufacturer_Type = DisplayString
_QtechSystemLankApSoftwareManufacturer_Object = MibTableColumn
qtechSystemLankApSoftwareManufacturer = _QtechSystemLankApSoftwareManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 7),
    _QtechSystemLankApSoftwareManufacturer_Type()
)
qtechSystemLankApSoftwareManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApSoftwareManufacturer.setStatus("current")
_QtechSystemLankApCpuType_Type = DisplayString
_QtechSystemLankApCpuType_Object = MibTableColumn
qtechSystemLankApCpuType = _QtechSystemLankApCpuType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 8),
    _QtechSystemLankApCpuType_Type()
)
qtechSystemLankApCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApCpuType.setStatus("current")
_QtechSystemLankApMemoryType_Type = DisplayString
_QtechSystemLankApMemoryType_Object = MibTableColumn
qtechSystemLankApMemoryType = _QtechSystemLankApMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 9),
    _QtechSystemLankApMemoryType_Type()
)
qtechSystemLankApMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApMemoryType.setStatus("current")
_QtechSystemLankApMemorySize_Type = Gauge32
_QtechSystemLankApMemorySize_Object = MibTableColumn
qtechSystemLankApMemorySize = _QtechSystemLankApMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 10),
    _QtechSystemLankApMemorySize_Type()
)
qtechSystemLankApMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApMemorySize.setStatus("current")
_QtechSystemLankAPFlashSize_Type = Gauge32
_QtechSystemLankAPFlashSize_Object = MibTableColumn
qtechSystemLankAPFlashSize = _QtechSystemLankAPFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 11),
    _QtechSystemLankAPFlashSize_Type()
)
qtechSystemLankAPFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankAPFlashSize.setStatus("current")
_QtechSystemLankApManufacturer_Type = DisplayString
_QtechSystemLankApManufacturer_Object = MibTableColumn
qtechSystemLankApManufacturer = _QtechSystemLankApManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 12),
    _QtechSystemLankApManufacturer_Type()
)
qtechSystemLankApManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApManufacturer.setStatus("current")
_QtechSystemLankApSerialno_Type = DisplayString
_QtechSystemLankApSerialno_Object = MibTableColumn
qtechSystemLankApSerialno = _QtechSystemLankApSerialno_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 13),
    _QtechSystemLankApSerialno_Type()
)
qtechSystemLankApSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApSerialno.setStatus("current")
_QtechSystemLankApSysModel_Type = DisplayString
_QtechSystemLankApSysModel_Object = MibTableColumn
qtechSystemLankApSysModel = _QtechSystemLankApSysModel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 14),
    _QtechSystemLankApSysModel_Type()
)
qtechSystemLankApSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApSysModel.setStatus("current")
_QtechSystemLankApUptime_Type = Integer32
_QtechSystemLankApUptime_Object = MibTableColumn
qtechSystemLankApUptime = _QtechSystemLankApUptime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 15),
    _QtechSystemLankApUptime_Type()
)
qtechSystemLankApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApUptime.setStatus("current")
_QtechSystemLankApAccurateUptime_Type = TimeTicks
_QtechSystemLankApAccurateUptime_Object = MibTableColumn
qtechSystemLankApAccurateUptime = _QtechSystemLankApAccurateUptime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 16),
    _QtechSystemLankApAccurateUptime_Type()
)
qtechSystemLankApAccurateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApAccurateUptime.setStatus("current")


class _QtechSystemLankApHwVersion_Type(DisplayString):
    """Custom type qtechSystemLankApHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSystemLankApHwVersion_Type.__name__ = "DisplayString"
_QtechSystemLankApHwVersion_Object = MibTableColumn
qtechSystemLankApHwVersion = _QtechSystemLankApHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 39, 1, 17),
    _QtechSystemLankApHwVersion_Type()
)
qtechSystemLankApHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemLankApHwVersion.setStatus("current")
_QtechSystemBoardTemperatureTable_Object = MibTable
qtechSystemBoardTemperatureTable = _QtechSystemBoardTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 40)
)
if mibBuilder.loadTexts:
    qtechSystemBoardTemperatureTable.setStatus("current")
_QtechSystemBoardTemperatureEntry_Object = MibTableRow
qtechSystemBoardTemperatureEntry = _QtechSystemBoardTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 40, 1)
)
qtechSystemBoardTemperatureEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemBoardTemperatureIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemBoardTemperatureEntry.setStatus("current")
_QtechSystemBoardTemperatureIndex_Type = Integer32
_QtechSystemBoardTemperatureIndex_Object = MibTableColumn
qtechSystemBoardTemperatureIndex = _QtechSystemBoardTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 40, 1, 1),
    _QtechSystemBoardTemperatureIndex_Type()
)
qtechSystemBoardTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemBoardTemperatureIndex.setStatus("current")
_QtechSystemBoardTemperatureName_Type = DisplayString
_QtechSystemBoardTemperatureName_Object = MibTableColumn
qtechSystemBoardTemperatureName = _QtechSystemBoardTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 40, 1, 2),
    _QtechSystemBoardTemperatureName_Type()
)
qtechSystemBoardTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemBoardTemperatureName.setStatus("current")
_QtechSystemBoardTemperatureCurrent_Type = Integer32
_QtechSystemBoardTemperatureCurrent_Object = MibTableColumn
qtechSystemBoardTemperatureCurrent = _QtechSystemBoardTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 40, 1, 3),
    _QtechSystemBoardTemperatureCurrent_Type()
)
qtechSystemBoardTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemBoardTemperatureCurrent.setStatus("current")
_QtechSystemElectricalInformationTable_Object = MibTable
qtechSystemElectricalInformationTable = _QtechSystemElectricalInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41)
)
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationTable.setStatus("current")
_QtechSystemElectricalInformationEntry_Object = MibTableRow
qtechSystemElectricalInformationEntry = _QtechSystemElectricalInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1)
)
qtechSystemElectricalInformationEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemElectricalInformationDeviceIndex"),
    (0, "QTECH-SYSTEM-MIB", "qtechSystemElectricalInformationIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationEntry.setStatus("current")
_QtechSystemElectricalInformationDeviceIndex_Type = Integer32
_QtechSystemElectricalInformationDeviceIndex_Object = MibTableColumn
qtechSystemElectricalInformationDeviceIndex = _QtechSystemElectricalInformationDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 1),
    _QtechSystemElectricalInformationDeviceIndex_Type()
)
qtechSystemElectricalInformationDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationDeviceIndex.setStatus("current")
_QtechSystemElectricalInformationIndex_Type = Integer32
_QtechSystemElectricalInformationIndex_Object = MibTableColumn
qtechSystemElectricalInformationIndex = _QtechSystemElectricalInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 2),
    _QtechSystemElectricalInformationIndex_Type()
)
qtechSystemElectricalInformationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationIndex.setStatus("current")


class _QtechSystemElectricalInformationStatus_Type(Integer32):
    """Custom type qtechSystemElectricalInformationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6))
    )


_QtechSystemElectricalInformationStatus_Type.__name__ = "Integer32"
_QtechSystemElectricalInformationStatus_Object = MibTableColumn
qtechSystemElectricalInformationStatus = _QtechSystemElectricalInformationStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 3),
    _QtechSystemElectricalInformationStatus_Type()
)
qtechSystemElectricalInformationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationStatus.setStatus("current")
_QtechSystemElectricalInformationType_Type = DisplayString
_QtechSystemElectricalInformationType_Object = MibTableColumn
qtechSystemElectricalInformationType = _QtechSystemElectricalInformationType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 4),
    _QtechSystemElectricalInformationType_Type()
)
qtechSystemElectricalInformationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationType.setStatus("current")
_QtechSystemElectricalInformationAttribute_Type = DisplayString
_QtechSystemElectricalInformationAttribute_Object = MibTableColumn
qtechSystemElectricalInformationAttribute = _QtechSystemElectricalInformationAttribute_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 5),
    _QtechSystemElectricalInformationAttribute_Type()
)
qtechSystemElectricalInformationAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationAttribute.setStatus("current")
_QtechSystemElectricalInformationSofeVersion_Type = DisplayString
_QtechSystemElectricalInformationSofeVersion_Object = MibTableColumn
qtechSystemElectricalInformationSofeVersion = _QtechSystemElectricalInformationSofeVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 6),
    _QtechSystemElectricalInformationSofeVersion_Type()
)
qtechSystemElectricalInformationSofeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationSofeVersion.setStatus("current")
_QtechSystemElectricalInformationHardwareVersion_Type = DisplayString
_QtechSystemElectricalInformationHardwareVersion_Object = MibTableColumn
qtechSystemElectricalInformationHardwareVersion = _QtechSystemElectricalInformationHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 7),
    _QtechSystemElectricalInformationHardwareVersion_Type()
)
qtechSystemElectricalInformationHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationHardwareVersion.setStatus("current")
_QtechSystemElectricalInformationSerial_Type = DisplayString
_QtechSystemElectricalInformationSerial_Object = MibTableColumn
qtechSystemElectricalInformationSerial = _QtechSystemElectricalInformationSerial_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 8),
    _QtechSystemElectricalInformationSerial_Type()
)
qtechSystemElectricalInformationSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationSerial.setStatus("current")
_QtechSystemElectricalInformationProductionDate_Type = DisplayString
_QtechSystemElectricalInformationProductionDate_Object = MibTableColumn
qtechSystemElectricalInformationProductionDate = _QtechSystemElectricalInformationProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 9),
    _QtechSystemElectricalInformationProductionDate_Type()
)
qtechSystemElectricalInformationProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationProductionDate.setStatus("current")
_QtechSystemElectricalInformationRatedPower_Type = Integer32
_QtechSystemElectricalInformationRatedPower_Object = MibTableColumn
qtechSystemElectricalInformationRatedPower = _QtechSystemElectricalInformationRatedPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 10),
    _QtechSystemElectricalInformationRatedPower_Type()
)
qtechSystemElectricalInformationRatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationRatedPower.setStatus("current")
_QtechSystemElectricalInformationInVoltage_Type = Integer32
_QtechSystemElectricalInformationInVoltage_Object = MibTableColumn
qtechSystemElectricalInformationInVoltage = _QtechSystemElectricalInformationInVoltage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 11),
    _QtechSystemElectricalInformationInVoltage_Type()
)
qtechSystemElectricalInformationInVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationInVoltage.setStatus("current")
_QtechSystemElectricalInformationInCurrent_Type = Integer32
_QtechSystemElectricalInformationInCurrent_Object = MibTableColumn
qtechSystemElectricalInformationInCurrent = _QtechSystemElectricalInformationInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 12),
    _QtechSystemElectricalInformationInCurrent_Type()
)
qtechSystemElectricalInformationInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationInCurrent.setStatus("current")
_QtechSystemElectricalInformationOutVoltage_Type = Integer32
_QtechSystemElectricalInformationOutVoltage_Object = MibTableColumn
qtechSystemElectricalInformationOutVoltage = _QtechSystemElectricalInformationOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 13),
    _QtechSystemElectricalInformationOutVoltage_Type()
)
qtechSystemElectricalInformationOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationOutVoltage.setStatus("current")
_QtechSystemElectricalInformationOutCurrent_Type = Integer32
_QtechSystemElectricalInformationOutCurrent_Object = MibTableColumn
qtechSystemElectricalInformationOutCurrent = _QtechSystemElectricalInformationOutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 14),
    _QtechSystemElectricalInformationOutCurrent_Type()
)
qtechSystemElectricalInformationOutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationOutCurrent.setStatus("current")
_QtechSystemElectricalInformationOutPower_Type = Integer32
_QtechSystemElectricalInformationOutPower_Object = MibTableColumn
qtechSystemElectricalInformationOutPower = _QtechSystemElectricalInformationOutPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 15),
    _QtechSystemElectricalInformationOutPower_Type()
)
qtechSystemElectricalInformationOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationOutPower.setStatus("current")
_QtechSystemElectricalInformationTemperature_Type = Integer32
_QtechSystemElectricalInformationTemperature_Object = MibTableColumn
qtechSystemElectricalInformationTemperature = _QtechSystemElectricalInformationTemperature_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 16),
    _QtechSystemElectricalInformationTemperature_Type()
)
qtechSystemElectricalInformationTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationTemperature.setStatus("current")
_QtechSystemElectricalInformationAirflowCoexist_Type = DisplayString
_QtechSystemElectricalInformationAirflowCoexist_Object = MibTableColumn
qtechSystemElectricalInformationAirflowCoexist = _QtechSystemElectricalInformationAirflowCoexist_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 17),
    _QtechSystemElectricalInformationAirflowCoexist_Type()
)
qtechSystemElectricalInformationAirflowCoexist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationAirflowCoexist.setStatus("current")
_QtechSystemElectricalInformationWarningStatus_Type = DisplayString
_QtechSystemElectricalInformationWarningStatus_Object = MibTableColumn
qtechSystemElectricalInformationWarningStatus = _QtechSystemElectricalInformationWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 41, 1, 18),
    _QtechSystemElectricalInformationWarningStatus_Type()
)
qtechSystemElectricalInformationWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemElectricalInformationWarningStatus.setStatus("current")
_QtechSystemFanInformationTable_Object = MibTable
qtechSystemFanInformationTable = _QtechSystemFanInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42)
)
if mibBuilder.loadTexts:
    qtechSystemFanInformationTable.setStatus("current")
_QtechSystemFanInformationEntry_Object = MibTableRow
qtechSystemFanInformationEntry = _QtechSystemFanInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1)
)
qtechSystemFanInformationEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemFanInformationDeviceIndex"),
    (0, "QTECH-SYSTEM-MIB", "qtechSystemFanInformationFanIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemFanInformationEntry.setStatus("current")
_QtechSystemFanInformationDeviceIndex_Type = Integer32
_QtechSystemFanInformationDeviceIndex_Object = MibTableColumn
qtechSystemFanInformationDeviceIndex = _QtechSystemFanInformationDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 1),
    _QtechSystemFanInformationDeviceIndex_Type()
)
qtechSystemFanInformationDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationDeviceIndex.setStatus("current")
_QtechSystemFanInformationFanIndex_Type = Integer32
_QtechSystemFanInformationFanIndex_Object = MibTableColumn
qtechSystemFanInformationFanIndex = _QtechSystemFanInformationFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 2),
    _QtechSystemFanInformationFanIndex_Type()
)
qtechSystemFanInformationFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationFanIndex.setStatus("current")


class _QtechSystemFanInformationStatus_Type(Integer32):
    """Custom type qtechSystemFanInformationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6))
    )


_QtechSystemFanInformationStatus_Type.__name__ = "Integer32"
_QtechSystemFanInformationStatus_Object = MibTableColumn
qtechSystemFanInformationStatus = _QtechSystemFanInformationStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 3),
    _QtechSystemFanInformationStatus_Type()
)
qtechSystemFanInformationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationStatus.setStatus("current")
_QtechSystemFanInformationType_Type = DisplayString
_QtechSystemFanInformationType_Object = MibTableColumn
qtechSystemFanInformationType = _QtechSystemFanInformationType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 4),
    _QtechSystemFanInformationType_Type()
)
qtechSystemFanInformationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationType.setStatus("current")
_QtechSystemFanInformationAttribute_Type = DisplayString
_QtechSystemFanInformationAttribute_Object = MibTableColumn
qtechSystemFanInformationAttribute = _QtechSystemFanInformationAttribute_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 5),
    _QtechSystemFanInformationAttribute_Type()
)
qtechSystemFanInformationAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationAttribute.setStatus("current")
_QtechSystemFanInformationSofeVersion_Type = DisplayString
_QtechSystemFanInformationSofeVersion_Object = MibTableColumn
qtechSystemFanInformationSofeVersion = _QtechSystemFanInformationSofeVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 6),
    _QtechSystemFanInformationSofeVersion_Type()
)
qtechSystemFanInformationSofeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationSofeVersion.setStatus("current")
_QtechSystemFanInformationFirmwareVersion_Type = DisplayString
_QtechSystemFanInformationFirmwareVersion_Object = MibTableColumn
qtechSystemFanInformationFirmwareVersion = _QtechSystemFanInformationFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 7),
    _QtechSystemFanInformationFirmwareVersion_Type()
)
qtechSystemFanInformationFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationFirmwareVersion.setStatus("current")
_QtechSystemFanInformationHardwareVersion_Type = DisplayString
_QtechSystemFanInformationHardwareVersion_Object = MibTableColumn
qtechSystemFanInformationHardwareVersion = _QtechSystemFanInformationHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 8),
    _QtechSystemFanInformationHardwareVersion_Type()
)
qtechSystemFanInformationHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationHardwareVersion.setStatus("current")
_QtechSystemFanInformationSerial_Type = DisplayString
_QtechSystemFanInformationSerial_Object = MibTableColumn
qtechSystemFanInformationSerial = _QtechSystemFanInformationSerial_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 9),
    _QtechSystemFanInformationSerial_Type()
)
qtechSystemFanInformationSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationSerial.setStatus("current")
_QtechSystemFanInformationProductionDate_Type = DisplayString
_QtechSystemFanInformationProductionDate_Object = MibTableColumn
qtechSystemFanInformationProductionDate = _QtechSystemFanInformationProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 10),
    _QtechSystemFanInformationProductionDate_Type()
)
qtechSystemFanInformationProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationProductionDate.setStatus("current")
_QtechSystemFanInformationTemperature_Type = Integer32
_QtechSystemFanInformationTemperature_Object = MibTableColumn
qtechSystemFanInformationTemperature = _QtechSystemFanInformationTemperature_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 11),
    _QtechSystemFanInformationTemperature_Type()
)
qtechSystemFanInformationTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationTemperature.setStatus("current")
_QtechSystemFanInformationNumber_Type = Integer32
_QtechSystemFanInformationNumber_Object = MibTableColumn
qtechSystemFanInformationNumber = _QtechSystemFanInformationNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 12),
    _QtechSystemFanInformationNumber_Type()
)
qtechSystemFanInformationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationNumber.setStatus("current")
_QtechSystemFanInformationAirflowCoexist_Type = DisplayString
_QtechSystemFanInformationAirflowCoexist_Object = MibTableColumn
qtechSystemFanInformationAirflowCoexist = _QtechSystemFanInformationAirflowCoexist_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 13),
    _QtechSystemFanInformationAirflowCoexist_Type()
)
qtechSystemFanInformationAirflowCoexist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationAirflowCoexist.setStatus("current")
_QtechSystemFanInformationWarningStatus_Type = DisplayString
_QtechSystemFanInformationWarningStatus_Object = MibTableColumn
qtechSystemFanInformationWarningStatus = _QtechSystemFanInformationWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 42, 1, 14),
    _QtechSystemFanInformationWarningStatus_Type()
)
qtechSystemFanInformationWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanInformationWarningStatus.setStatus("current")
_QtechSystemFanStatusTable_Object = MibTable
qtechSystemFanStatusTable = _QtechSystemFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 43)
)
if mibBuilder.loadTexts:
    qtechSystemFanStatusTable.setStatus("current")
_QtechSystemFanStatusEntry_Object = MibTableRow
qtechSystemFanStatusEntry = _QtechSystemFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 43, 1)
)
qtechSystemFanStatusEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemFanStatusDeviceIndex"),
    (0, "QTECH-SYSTEM-MIB", "qtechSystemFanStatusFanIndex"),
    (0, "QTECH-SYSTEM-MIB", "qtechSystemFanStatusIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemFanStatusEntry.setStatus("current")
_QtechSystemFanStatusDeviceIndex_Type = Integer32
_QtechSystemFanStatusDeviceIndex_Object = MibTableColumn
qtechSystemFanStatusDeviceIndex = _QtechSystemFanStatusDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 43, 1, 1),
    _QtechSystemFanStatusDeviceIndex_Type()
)
qtechSystemFanStatusDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanStatusDeviceIndex.setStatus("current")
_QtechSystemFanStatusFanIndex_Type = Integer32
_QtechSystemFanStatusFanIndex_Object = MibTableColumn
qtechSystemFanStatusFanIndex = _QtechSystemFanStatusFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 43, 1, 2),
    _QtechSystemFanStatusFanIndex_Type()
)
qtechSystemFanStatusFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanStatusFanIndex.setStatus("current")
_QtechSystemFanStatusIndex_Type = Integer32
_QtechSystemFanStatusIndex_Object = MibTableColumn
qtechSystemFanStatusIndex = _QtechSystemFanStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 43, 1, 3),
    _QtechSystemFanStatusIndex_Type()
)
qtechSystemFanStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanStatusIndex.setStatus("current")


class _QtechSystemFanStatus_Type(Integer32):
    """Custom type qtechSystemFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6))
    )


_QtechSystemFanStatus_Type.__name__ = "Integer32"
_QtechSystemFanStatus_Object = MibTableColumn
qtechSystemFanStatus = _QtechSystemFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 43, 1, 4),
    _QtechSystemFanStatus_Type()
)
qtechSystemFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanStatus.setStatus("current")
_QtechSystemFanStatusLevel_Type = Integer32
_QtechSystemFanStatusLevel_Object = MibTableColumn
qtechSystemFanStatusLevel = _QtechSystemFanStatusLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 43, 1, 5),
    _QtechSystemFanStatusLevel_Type()
)
qtechSystemFanStatusLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanStatusLevel.setStatus("current")
_QtechSystemFanStatusSpeed_Type = Integer32
_QtechSystemFanStatusSpeed_Object = MibTableColumn
qtechSystemFanStatusSpeed = _QtechSystemFanStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 43, 1, 6),
    _QtechSystemFanStatusSpeed_Type()
)
qtechSystemFanStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanStatusSpeed.setStatus("current")
_QtechSystemMultipleTemperatureTable_Object = MibTable
qtechSystemMultipleTemperatureTable = _QtechSystemMultipleTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 44)
)
if mibBuilder.loadTexts:
    qtechSystemMultipleTemperatureTable.setStatus("current")
_QtechSystemMultipleTemperatureEntry_Object = MibTableRow
qtechSystemMultipleTemperatureEntry = _QtechSystemMultipleTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 44, 1)
)
qtechSystemMultipleTemperatureEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemMultipleTemperatureDeviceIndex"),
    (0, "QTECH-SYSTEM-MIB", "qtechSystemMultipleTemperatureSlotIndex"),
    (0, "QTECH-SYSTEM-MIB", "qtechSystemMultipleTemperatureIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemMultipleTemperatureEntry.setStatus("current")
_QtechSystemMultipleTemperatureDeviceIndex_Type = Integer32
_QtechSystemMultipleTemperatureDeviceIndex_Object = MibTableColumn
qtechSystemMultipleTemperatureDeviceIndex = _QtechSystemMultipleTemperatureDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 44, 1, 1),
    _QtechSystemMultipleTemperatureDeviceIndex_Type()
)
qtechSystemMultipleTemperatureDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemMultipleTemperatureDeviceIndex.setStatus("current")
_QtechSystemMultipleTemperatureSlotIndex_Type = Integer32
_QtechSystemMultipleTemperatureSlotIndex_Object = MibTableColumn
qtechSystemMultipleTemperatureSlotIndex = _QtechSystemMultipleTemperatureSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 44, 1, 2),
    _QtechSystemMultipleTemperatureSlotIndex_Type()
)
qtechSystemMultipleTemperatureSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemMultipleTemperatureSlotIndex.setStatus("current")
_QtechSystemMultipleTemperatureIndex_Type = Integer32
_QtechSystemMultipleTemperatureIndex_Object = MibTableColumn
qtechSystemMultipleTemperatureIndex = _QtechSystemMultipleTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 44, 1, 3),
    _QtechSystemMultipleTemperatureIndex_Type()
)
qtechSystemMultipleTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemMultipleTemperatureIndex.setStatus("current")
_QtechSystemMultipleTemperatureName_Type = DisplayString
_QtechSystemMultipleTemperatureName_Object = MibTableColumn
qtechSystemMultipleTemperatureName = _QtechSystemMultipleTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 44, 1, 4),
    _QtechSystemMultipleTemperatureName_Type()
)
qtechSystemMultipleTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemMultipleTemperatureName.setStatus("current")
_QtechSystemMultipleTemperatureCurrent_Type = Integer32
_QtechSystemMultipleTemperatureCurrent_Object = MibTableColumn
qtechSystemMultipleTemperatureCurrent = _QtechSystemMultipleTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 44, 1, 5),
    _QtechSystemMultipleTemperatureCurrent_Type()
)
qtechSystemMultipleTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemMultipleTemperatureCurrent.setStatus("current")
_QtechSystemMultipleTemperatureWarning_Type = Integer32
_QtechSystemMultipleTemperatureWarning_Object = MibTableColumn
qtechSystemMultipleTemperatureWarning = _QtechSystemMultipleTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 44, 1, 6),
    _QtechSystemMultipleTemperatureWarning_Type()
)
qtechSystemMultipleTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemMultipleTemperatureWarning.setStatus("current")
_QtechSystemMultipleTemperatureCritical_Type = Integer32
_QtechSystemMultipleTemperatureCritical_Object = MibTableColumn
qtechSystemMultipleTemperatureCritical = _QtechSystemMultipleTemperatureCritical_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 44, 1, 7),
    _QtechSystemMultipleTemperatureCritical_Type()
)
qtechSystemMultipleTemperatureCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSystemMultipleTemperatureCritical.setStatus("current")
_QtechSystemAccurateUptime_Type = TimeTicks
_QtechSystemAccurateUptime_Object = MibScalar
qtechSystemAccurateUptime = _QtechSystemAccurateUptime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 45),
    _QtechSystemAccurateUptime_Type()
)
qtechSystemAccurateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemAccurateUptime.setStatus("current")
_QtechSystemPowerIndex_Type = Integer32
_QtechSystemPowerIndex_Object = MibScalar
qtechSystemPowerIndex = _QtechSystemPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 46),
    _QtechSystemPowerIndex_Type()
)
qtechSystemPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemPowerIndex.setStatus("current")
_QtechSystemSwitchID_Type = Integer32
_QtechSystemSwitchID_Object = MibScalar
qtechSystemSwitchID = _QtechSystemSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 47),
    _QtechSystemSwitchID_Type()
)
qtechSystemSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemSwitchID.setStatus("current")
_QtechSystemApDeviceDescriptionTable_Object = MibTable
qtechSystemApDeviceDescriptionTable = _QtechSystemApDeviceDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48)
)
if mibBuilder.loadTexts:
    qtechSystemApDeviceDescriptionTable.setStatus("current")
_QtechSystemApDeviceDescriptionEntry_Object = MibTableRow
qtechSystemApDeviceDescriptionEntry = _QtechSystemApDeviceDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48, 1)
)
qtechSystemApDeviceDescriptionEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemApDescMacAddr"),
)
if mibBuilder.loadTexts:
    qtechSystemApDeviceDescriptionEntry.setStatus("current")
_QtechSystemApDescMacAddr_Type = MacAddress
_QtechSystemApDescMacAddr_Object = MibTableColumn
qtechSystemApDescMacAddr = _QtechSystemApDescMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48, 1, 1),
    _QtechSystemApDescMacAddr_Type()
)
qtechSystemApDescMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApDescMacAddr.setStatus("current")


class _QtechSystemApMemoryType_Type(Integer32):
    """Custom type qtechSystemApMemoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("sdram", 1),
          ("ddram", 2))
    )


_QtechSystemApMemoryType_Type.__name__ = "Integer32"
_QtechSystemApMemoryType_Object = MibTableColumn
qtechSystemApMemoryType = _QtechSystemApMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48, 1, 2),
    _QtechSystemApMemoryType_Type()
)
qtechSystemApMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApMemoryType.setStatus("current")
_QtechSystemApMemorySize_Type = Gauge32
_QtechSystemApMemorySize_Object = MibTableColumn
qtechSystemApMemorySize = _QtechSystemApMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48, 1, 3),
    _QtechSystemApMemorySize_Type()
)
qtechSystemApMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApMemorySize.setStatus("current")


class _QtechSystemAPFlashType_Type(Integer32):
    """Custom type qtechSystemAPFlashType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("nor", 1),
          ("non-nor", 2))
    )


_QtechSystemAPFlashType_Type.__name__ = "Integer32"
_QtechSystemAPFlashType_Object = MibTableColumn
qtechSystemAPFlashType = _QtechSystemAPFlashType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48, 1, 4),
    _QtechSystemAPFlashType_Type()
)
qtechSystemAPFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemAPFlashType.setStatus("current")
_QtechSystemAPFlashSize_Type = Gauge32
_QtechSystemAPFlashSize_Object = MibTableColumn
qtechSystemAPFlashSize = _QtechSystemAPFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48, 1, 5),
    _QtechSystemAPFlashSize_Type()
)
qtechSystemAPFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemAPFlashSize.setStatus("current")
_QtechSystemApNVRAMSize_Type = Gauge32
_QtechSystemApNVRAMSize_Object = MibTableColumn
qtechSystemApNVRAMSize = _QtechSystemApNVRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48, 1, 6),
    _QtechSystemApNVRAMSize_Type()
)
qtechSystemApNVRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApNVRAMSize.setStatus("current")
_QtechSystemApCFSize_Type = Gauge32
_QtechSystemApCFSize_Object = MibTableColumn
qtechSystemApCFSize = _QtechSystemApCFSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48, 1, 7),
    _QtechSystemApCFSize_Type()
)
qtechSystemApCFSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApCFSize.setStatus("current")
_QtechSystemApCPUType_Type = DisplayString
_QtechSystemApCPUType_Object = MibTableColumn
qtechSystemApCPUType = _QtechSystemApCPUType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 48, 1, 8),
    _QtechSystemApCPUType_Type()
)
qtechSystemApCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApCPUType.setStatus("current")
_QtechSystemApDeviceStatisticsTable_Object = MibTable
qtechSystemApDeviceStatisticsTable = _QtechSystemApDeviceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49)
)
if mibBuilder.loadTexts:
    qtechSystemApDeviceStatisticsTable.setStatus("current")
_QtechSystemApDeviceStatisticsEntry_Object = MibTableRow
qtechSystemApDeviceStatisticsEntry = _QtechSystemApDeviceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1)
)
qtechSystemApDeviceStatisticsEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemApStatMacAddr"),
)
if mibBuilder.loadTexts:
    qtechSystemApDeviceStatisticsEntry.setStatus("current")
_QtechSystemApStatMacAddr_Type = MacAddress
_QtechSystemApStatMacAddr_Object = MibTableColumn
qtechSystemApStatMacAddr = _QtechSystemApStatMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1, 1),
    _QtechSystemApStatMacAddr_Type()
)
qtechSystemApStatMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApStatMacAddr.setStatus("current")
_QtechSystemApInterfaceNum_Type = Integer32
_QtechSystemApInterfaceNum_Object = MibTableColumn
qtechSystemApInterfaceNum = _QtechSystemApInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1, 2),
    _QtechSystemApInterfaceNum_Type()
)
qtechSystemApInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApInterfaceNum.setStatus("current")
_QtechSystemApUptime_Type = TimeTicks
_QtechSystemApUptime_Object = MibTableColumn
qtechSystemApUptime = _QtechSystemApUptime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1, 3),
    _QtechSystemApUptime_Type()
)
qtechSystemApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApUptime.setStatus("current")
_QtechSystemApCPUUtilizationCurrent_Type = Percent
_QtechSystemApCPUUtilizationCurrent_Object = MibTableColumn
qtechSystemApCPUUtilizationCurrent = _QtechSystemApCPUUtilizationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1, 4),
    _QtechSystemApCPUUtilizationCurrent_Type()
)
qtechSystemApCPUUtilizationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApCPUUtilizationCurrent.setStatus("current")
_QtechSystemApCPUUtilizationAverage_Type = Percent
_QtechSystemApCPUUtilizationAverage_Object = MibTableColumn
qtechSystemApCPUUtilizationAverage = _QtechSystemApCPUUtilizationAverage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1, 5),
    _QtechSystemApCPUUtilizationAverage_Type()
)
qtechSystemApCPUUtilizationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApCPUUtilizationAverage.setStatus("current")
_QtechSystemApMemoryPoolCurrentUtilization_Type = Percent
_QtechSystemApMemoryPoolCurrentUtilization_Object = MibTableColumn
qtechSystemApMemoryPoolCurrentUtilization = _QtechSystemApMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1, 6),
    _QtechSystemApMemoryPoolCurrentUtilization_Type()
)
qtechSystemApMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApMemoryPoolCurrentUtilization.setStatus("current")
_QtechSystemApMemoryPoolAverageUtilization_Type = Percent
_QtechSystemApMemoryPoolAverageUtilization_Object = MibTableColumn
qtechSystemApMemoryPoolAverageUtilization = _QtechSystemApMemoryPoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1, 7),
    _QtechSystemApMemoryPoolAverageUtilization_Type()
)
qtechSystemApMemoryPoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApMemoryPoolAverageUtilization.setStatus("current")
_QtechSystemApFlashFreeSize_Type = Unsigned32
_QtechSystemApFlashFreeSize_Object = MibTableColumn
qtechSystemApFlashFreeSize = _QtechSystemApFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1, 8),
    _QtechSystemApFlashFreeSize_Type()
)
qtechSystemApFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemApFlashFreeSize.setStatus("current")
_QtechSystemAPDeviceTemperature_Type = Integer32
_QtechSystemAPDeviceTemperature_Object = MibTableColumn
qtechSystemAPDeviceTemperature = _QtechSystemAPDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 49, 1, 9),
    _QtechSystemAPDeviceTemperature_Type()
)
qtechSystemAPDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemAPDeviceTemperature.setStatus("current")
_QtechSystemUptimeMsLow_Type = Unsigned32
_QtechSystemUptimeMsLow_Object = MibScalar
qtechSystemUptimeMsLow = _QtechSystemUptimeMsLow_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 50),
    _QtechSystemUptimeMsLow_Type()
)
qtechSystemUptimeMsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemUptimeMsLow.setStatus("current")
_QtechSystemUptimeMsHigh_Type = Unsigned32
_QtechSystemUptimeMsHigh_Object = MibScalar
qtechSystemUptimeMsHigh = _QtechSystemUptimeMsHigh_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 51),
    _QtechSystemUptimeMsHigh_Type()
)
qtechSystemUptimeMsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemUptimeMsHigh.setStatus("current")
_QtechSystemFanSNTable_Object = MibTable
qtechSystemFanSNTable = _QtechSystemFanSNTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 52)
)
if mibBuilder.loadTexts:
    qtechSystemFanSNTable.setStatus("current")
_QtechSystemFanSNEntry_Object = MibTableRow
qtechSystemFanSNEntry = _QtechSystemFanSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 52, 1)
)
qtechSystemFanSNEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemFanPadIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemFanSNEntry.setStatus("current")
_QtechSystemFanPadIndex_Type = Integer32
_QtechSystemFanPadIndex_Object = MibTableColumn
qtechSystemFanPadIndex = _QtechSystemFanPadIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 52, 1, 1),
    _QtechSystemFanPadIndex_Type()
)
qtechSystemFanPadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPadIndex.setStatus("current")
_QtechSystemFanPadName_Type = DisplayString
_QtechSystemFanPadName_Object = MibTableColumn
qtechSystemFanPadName = _QtechSystemFanPadName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 52, 1, 2),
    _QtechSystemFanPadName_Type()
)
qtechSystemFanPadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPadName.setStatus("current")
_QtechSystemFanPadSN_Type = DisplayString
_QtechSystemFanPadSN_Object = MibTableColumn
qtechSystemFanPadSN = _QtechSystemFanPadSN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 52, 1, 3),
    _QtechSystemFanPadSN_Type()
)
qtechSystemFanPadSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPadSN.setStatus("current")
_QtechSystemDsfSNTable_Object = MibTable
qtechSystemDsfSNTable = _QtechSystemDsfSNTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 53)
)
if mibBuilder.loadTexts:
    qtechSystemDsfSNTable.setStatus("current")
_QtechSystemDsfSNEntry_Object = MibTableRow
qtechSystemDsfSNEntry = _QtechSystemDsfSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 53, 1)
)
qtechSystemDsfSNEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemDsfIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemDsfSNEntry.setStatus("current")
_QtechSystemDsfIndex_Type = Integer32
_QtechSystemDsfIndex_Object = MibTableColumn
qtechSystemDsfIndex = _QtechSystemDsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 53, 1, 1),
    _QtechSystemDsfIndex_Type()
)
qtechSystemDsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemDsfIndex.setStatus("current")
_QtechSystemDsfName_Type = DisplayString
_QtechSystemDsfName_Object = MibTableColumn
qtechSystemDsfName = _QtechSystemDsfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 53, 1, 2),
    _QtechSystemDsfName_Type()
)
qtechSystemDsfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemDsfName.setStatus("current")
_QtechSystemDsfSN_Type = DisplayString
_QtechSystemDsfSN_Object = MibTableColumn
qtechSystemDsfSN = _QtechSystemDsfSN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 53, 1, 3),
    _QtechSystemDsfSN_Type()
)
qtechSystemDsfSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemDsfSN.setStatus("current")
_QtechSystemPowerSNTable_Object = MibTable
qtechSystemPowerSNTable = _QtechSystemPowerSNTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 54)
)
if mibBuilder.loadTexts:
    qtechSystemPowerSNTable.setStatus("current")
_QtechSystemPowerSNEntry_Object = MibTableRow
qtechSystemPowerSNEntry = _QtechSystemPowerSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 54, 1)
)
qtechSystemPowerSNEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemPowerSNIndex"),
)
if mibBuilder.loadTexts:
    qtechSystemPowerSNEntry.setStatus("current")
_QtechSystemPowerSNIndex_Type = Integer32
_QtechSystemPowerSNIndex_Object = MibTableColumn
qtechSystemPowerSNIndex = _QtechSystemPowerSNIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 54, 1, 1),
    _QtechSystemPowerSNIndex_Type()
)
qtechSystemPowerSNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemPowerSNIndex.setStatus("current")
_QtechSystemPowerSNName_Type = DisplayString
_QtechSystemPowerSNName_Object = MibTableColumn
qtechSystemPowerSNName = _QtechSystemPowerSNName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 54, 1, 2),
    _QtechSystemPowerSNName_Type()
)
qtechSystemPowerSNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemPowerSNName.setStatus("current")
_QtechSystemPowerSN_Type = DisplayString
_QtechSystemPowerSN_Object = MibTableColumn
qtechSystemPowerSN = _QtechSystemPowerSN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 54, 1, 3),
    _QtechSystemPowerSN_Type()
)
qtechSystemPowerSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemPowerSN.setStatus("current")
_QtechSystemFanPad1SpeedTable_Object = MibTable
qtechSystemFanPad1SpeedTable = _QtechSystemFanPad1SpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55)
)
if mibBuilder.loadTexts:
    qtechSystemFanPad1SpeedTable.setStatus("current")
_QtechSystemFanPad1SpeedEntry_Object = MibTableRow
qtechSystemFanPad1SpeedEntry = _QtechSystemFanPad1SpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1)
)
qtechSystemFanPad1SpeedEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemOamFanPad1Index"),
)
if mibBuilder.loadTexts:
    qtechSystemFanPad1SpeedEntry.setStatus("current")
_QtechSystemOamFanPad1Index_Type = Integer32
_QtechSystemOamFanPad1Index_Object = MibTableColumn
qtechSystemOamFanPad1Index = _QtechSystemOamFanPad1Index_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 1),
    _QtechSystemOamFanPad1Index_Type()
)
qtechSystemOamFanPad1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemOamFanPad1Index.setStatus("current")
_QtechSystemOamFanPad1Name_Type = DisplayString
_QtechSystemOamFanPad1Name_Object = MibTableColumn
qtechSystemOamFanPad1Name = _QtechSystemOamFanPad1Name_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 2),
    _QtechSystemOamFanPad1Name_Type()
)
qtechSystemOamFanPad1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemOamFanPad1Name.setStatus("current")
_QtechSystemFanPad1Speed1_Type = Integer32
_QtechSystemFanPad1Speed1_Object = MibTableColumn
qtechSystemFanPad1Speed1 = _QtechSystemFanPad1Speed1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 3),
    _QtechSystemFanPad1Speed1_Type()
)
qtechSystemFanPad1Speed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad1Speed1.setStatus("current")
_QtechSystemFanPad1Speed2_Type = Integer32
_QtechSystemFanPad1Speed2_Object = MibTableColumn
qtechSystemFanPad1Speed2 = _QtechSystemFanPad1Speed2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 4),
    _QtechSystemFanPad1Speed2_Type()
)
qtechSystemFanPad1Speed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad1Speed2.setStatus("current")
_QtechSystemFanPad1Speed3_Type = Integer32
_QtechSystemFanPad1Speed3_Object = MibTableColumn
qtechSystemFanPad1Speed3 = _QtechSystemFanPad1Speed3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 5),
    _QtechSystemFanPad1Speed3_Type()
)
qtechSystemFanPad1Speed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad1Speed3.setStatus("current")
_QtechSystemFanPad1Speed4_Type = Integer32
_QtechSystemFanPad1Speed4_Object = MibTableColumn
qtechSystemFanPad1Speed4 = _QtechSystemFanPad1Speed4_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 6),
    _QtechSystemFanPad1Speed4_Type()
)
qtechSystemFanPad1Speed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad1Speed4.setStatus("current")
_QtechSystemFanPad1Speed5_Type = Integer32
_QtechSystemFanPad1Speed5_Object = MibTableColumn
qtechSystemFanPad1Speed5 = _QtechSystemFanPad1Speed5_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 7),
    _QtechSystemFanPad1Speed5_Type()
)
qtechSystemFanPad1Speed5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad1Speed5.setStatus("current")
_QtechSystemFanPad1Speed6_Type = Integer32
_QtechSystemFanPad1Speed6_Object = MibTableColumn
qtechSystemFanPad1Speed6 = _QtechSystemFanPad1Speed6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 8),
    _QtechSystemFanPad1Speed6_Type()
)
qtechSystemFanPad1Speed6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad1Speed6.setStatus("current")
_QtechSystemFanPad1Speed7_Type = Integer32
_QtechSystemFanPad1Speed7_Object = MibTableColumn
qtechSystemFanPad1Speed7 = _QtechSystemFanPad1Speed7_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 9),
    _QtechSystemFanPad1Speed7_Type()
)
qtechSystemFanPad1Speed7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad1Speed7.setStatus("current")
_QtechSystemFanPad1Speed8_Type = Integer32
_QtechSystemFanPad1Speed8_Object = MibTableColumn
qtechSystemFanPad1Speed8 = _QtechSystemFanPad1Speed8_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 10),
    _QtechSystemFanPad1Speed8_Type()
)
qtechSystemFanPad1Speed8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad1Speed8.setStatus("current")
_QtechSystemFanPad1Speed9_Type = Integer32
_QtechSystemFanPad1Speed9_Object = MibTableColumn
qtechSystemFanPad1Speed9 = _QtechSystemFanPad1Speed9_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 55, 1, 11),
    _QtechSystemFanPad1Speed9_Type()
)
qtechSystemFanPad1Speed9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad1Speed9.setStatus("current")
_QtechSystemFanPad2SpeedTable_Object = MibTable
qtechSystemFanPad2SpeedTable = _QtechSystemFanPad2SpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 56)
)
if mibBuilder.loadTexts:
    qtechSystemFanPad2SpeedTable.setStatus("current")
_QtechSystemFanPad2SpeedEntry_Object = MibTableRow
qtechSystemFanPad2SpeedEntry = _QtechSystemFanPad2SpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 56, 1)
)
qtechSystemFanPad2SpeedEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemOamFanPad2Index"),
)
if mibBuilder.loadTexts:
    qtechSystemFanPad2SpeedEntry.setStatus("current")
_QtechSystemOamFanPad2Index_Type = Integer32
_QtechSystemOamFanPad2Index_Object = MibTableColumn
qtechSystemOamFanPad2Index = _QtechSystemOamFanPad2Index_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 56, 1, 1),
    _QtechSystemOamFanPad2Index_Type()
)
qtechSystemOamFanPad2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemOamFanPad2Index.setStatus("current")
_QtechSystemOamFanPad2Name_Type = DisplayString
_QtechSystemOamFanPad2Name_Object = MibTableColumn
qtechSystemOamFanPad2Name = _QtechSystemOamFanPad2Name_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 56, 1, 2),
    _QtechSystemOamFanPad2Name_Type()
)
qtechSystemOamFanPad2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemOamFanPad2Name.setStatus("current")
_QtechSystemFanPad2Speed1_Type = Integer32
_QtechSystemFanPad2Speed1_Object = MibTableColumn
qtechSystemFanPad2Speed1 = _QtechSystemFanPad2Speed1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 56, 1, 3),
    _QtechSystemFanPad2Speed1_Type()
)
qtechSystemFanPad2Speed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad2Speed1.setStatus("current")
_QtechSystemFanPad2Speed2_Type = Integer32
_QtechSystemFanPad2Speed2_Object = MibTableColumn
qtechSystemFanPad2Speed2 = _QtechSystemFanPad2Speed2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 56, 1, 4),
    _QtechSystemFanPad2Speed2_Type()
)
qtechSystemFanPad2Speed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad2Speed2.setStatus("current")
_QtechSystemFanPad2Speed3_Type = Integer32
_QtechSystemFanPad2Speed3_Object = MibTableColumn
qtechSystemFanPad2Speed3 = _QtechSystemFanPad2Speed3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 56, 1, 5),
    _QtechSystemFanPad2Speed3_Type()
)
qtechSystemFanPad2Speed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad2Speed3.setStatus("current")
_QtechSystemFanPad3SpeedTable_Object = MibTable
qtechSystemFanPad3SpeedTable = _QtechSystemFanPad3SpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 57)
)
if mibBuilder.loadTexts:
    qtechSystemFanPad3SpeedTable.setStatus("current")
_QtechSystemFanPad3SpeedEntry_Object = MibTableRow
qtechSystemFanPad3SpeedEntry = _QtechSystemFanPad3SpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 57, 1)
)
qtechSystemFanPad3SpeedEntry.setIndexNames(
    (0, "QTECH-SYSTEM-MIB", "qtechSystemOamFanPad3Index"),
)
if mibBuilder.loadTexts:
    qtechSystemFanPad3SpeedEntry.setStatus("current")
_QtechSystemOamFanPad3Index_Type = Integer32
_QtechSystemOamFanPad3Index_Object = MibTableColumn
qtechSystemOamFanPad3Index = _QtechSystemOamFanPad3Index_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 57, 1, 1),
    _QtechSystemOamFanPad3Index_Type()
)
qtechSystemOamFanPad3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemOamFanPad3Index.setStatus("current")
_QtechSystemOamFanPad3Name_Type = DisplayString
_QtechSystemOamFanPad3Name_Object = MibTableColumn
qtechSystemOamFanPad3Name = _QtechSystemOamFanPad3Name_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 57, 1, 2),
    _QtechSystemOamFanPad3Name_Type()
)
qtechSystemOamFanPad3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemOamFanPad3Name.setStatus("current")
_QtechSystemFanPad3Speed1_Type = Integer32
_QtechSystemFanPad3Speed1_Object = MibTableColumn
qtechSystemFanPad3Speed1 = _QtechSystemFanPad3Speed1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 57, 1, 3),
    _QtechSystemFanPad3Speed1_Type()
)
qtechSystemFanPad3Speed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad3Speed1.setStatus("current")
_QtechSystemFanPad3Speed2_Type = Integer32
_QtechSystemFanPad3Speed2_Object = MibTableColumn
qtechSystemFanPad3Speed2 = _QtechSystemFanPad3Speed2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 57, 1, 4),
    _QtechSystemFanPad3Speed2_Type()
)
qtechSystemFanPad3Speed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad3Speed2.setStatus("current")
_QtechSystemFanPad3Speed3_Type = Integer32
_QtechSystemFanPad3Speed3_Object = MibTableColumn
qtechSystemFanPad3Speed3 = _QtechSystemFanPad3Speed3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 57, 1, 5),
    _QtechSystemFanPad3Speed3_Type()
)
qtechSystemFanPad3Speed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad3Speed3.setStatus("current")
_QtechSystemFanPad3Speed4_Type = Integer32
_QtechSystemFanPad3Speed4_Object = MibTableColumn
qtechSystemFanPad3Speed4 = _QtechSystemFanPad3Speed4_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 57, 1, 6),
    _QtechSystemFanPad3Speed4_Type()
)
qtechSystemFanPad3Speed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad3Speed4.setStatus("current")
_QtechSystemFanPad3Speed5_Type = Integer32
_QtechSystemFanPad3Speed5_Object = MibTableColumn
qtechSystemFanPad3Speed5 = _QtechSystemFanPad3Speed5_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 1, 57, 1, 7),
    _QtechSystemFanPad3Speed5_Type()
)
qtechSystemFanPad3Speed5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemFanPad3Speed5.setStatus("current")
_QtechSystemMIBTraps_ObjectIdentity = ObjectIdentity
qtechSystemMIBTraps = _QtechSystemMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2)
)
_QtechSystemHardChangeDesc_Type = DisplayString
_QtechSystemHardChangeDesc_Object = MibScalar
qtechSystemHardChangeDesc = _QtechSystemHardChangeDesc_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 1),
    _QtechSystemHardChangeDesc_Type()
)
qtechSystemHardChangeDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSystemHardChangeDesc.setStatus("current")
_QtechSystemMIBConformance_ObjectIdentity = ObjectIdentity
qtechSystemMIBConformance = _QtechSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 3)
)
_QtechSystemMIBCompliances_ObjectIdentity = ObjectIdentity
qtechSystemMIBCompliances = _QtechSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 3, 1)
)
_QtechSystemMIBGroups_ObjectIdentity = ObjectIdentity
qtechSystemMIBGroups = _QtechSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 3, 2)
)

# Managed Objects groups

qtechSystemMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 3, 2, 1)
)
qtechSystemMIBGroup.setObjects(
      *(("QTECH-SYSTEM-MIB", "qtechSystemHwVersion"),
        ("QTECH-SYSTEM-MIB", "qtechSystemSwVersion"),
        ("QTECH-SYSTEM-MIB", "qtechSystemBootVersion"),
        ("QTECH-SYSTEM-MIB", "qtechSystemSysCtrlVersion"),
        ("QTECH-SYSTEM-MIB", "qtechSystemParametersSave"),
        ("QTECH-SYSTEM-MIB", "qtechSystemReset"),
        ("QTECH-SYSTEM-MIB", "qtechSystemOutBandRate"),
        ("QTECH-SYSTEM-MIB", "qtechSwitchLayer"))
)
if mibBuilder.loadTexts:
    qtechSystemMIBGroup.setStatus("current")


# Notification objects

qtechSystemHardChangeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 2)
)
qtechSystemHardChangeDetected.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemHardChangeDesc")
)
if mibBuilder.loadTexts:
    qtechSystemHardChangeDetected.setStatus(
        "current"
    )

qtechSystemPowerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 3)
)
qtechSystemPowerStateChange.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemHwPower")
)
if mibBuilder.loadTexts:
    qtechSystemPowerStateChange.setStatus(
        "current"
    )

qtechSystemFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 4)
)
qtechSystemFanStateChange.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemHwFan")
)
if mibBuilder.loadTexts:
    qtechSystemFanStateChange.setStatus(
        "current"
    )

qtechSystemCPUusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 5)
)
qtechSystemCPUusageTooHighTrap.setObjects(
    ("QTECH-PROCESS-MIB", "qtechCPUUtilization1Min")
)
if mibBuilder.loadTexts:
    qtechSystemCPUusageTooHighTrap.setStatus(
        "current"
    )

qtechSystemCPUusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 6)
)
qtechSystemCPUusageTooHighRecovTrap.setObjects(
    ("QTECH-PROCESS-MIB", "qtechCPUUtilization1Min")
)
if mibBuilder.loadTexts:
    qtechSystemCPUusageTooHighRecovTrap.setStatus(
        "current"
    )

qtechSystemTmpTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 7)
)
qtechSystemTmpTooHighTrap.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemTemperatureCurrent")
)
if mibBuilder.loadTexts:
    qtechSystemTmpTooHighTrap.setStatus(
        "current"
    )

qtechSystemTmpTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 8)
)
qtechSystemTmpTooHighRecovTrap.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemTemperatureCurrent")
)
if mibBuilder.loadTexts:
    qtechSystemTmpTooHighRecovTrap.setStatus(
        "current"
    )

qtechSystemMemusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 9)
)
qtechSystemMemusageTooHighTrap.setObjects(
    ("QTECH-MEMORY-MIB", "qtechMemoryPoolCurrentUtilization")
)
if mibBuilder.loadTexts:
    qtechSystemMemusageTooHighTrap.setStatus(
        "current"
    )

qtechSystemMemusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 10)
)
qtechSystemMemusageTooHighRecovTrap.setObjects(
    ("QTECH-MEMORY-MIB", "qtechMemoryPoolCurrentUtilization")
)
if mibBuilder.loadTexts:
    qtechSystemMemusageTooHighRecovTrap.setStatus(
        "current"
    )

qtechSystemLankApCPUusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 11)
)
qtechSystemLankApCPUusageTooHighTrap.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
        ("QTECH-PROCESS-MIB", "qtechCPUUtilization1Min"))
)
if mibBuilder.loadTexts:
    qtechSystemLankApCPUusageTooHighTrap.setStatus(
        "current"
    )

qtechSystemLankApCPUusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 12)
)
qtechSystemLankApCPUusageTooHighRecovTrap.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
        ("QTECH-PROCESS-MIB", "qtechCPUUtilization1Min"))
)
if mibBuilder.loadTexts:
    qtechSystemLankApCPUusageTooHighRecovTrap.setStatus(
        "current"
    )

qtechSystemLankApMemusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 13)
)
qtechSystemLankApMemusageTooHighTrap.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolCurrentUtilization"))
)
if mibBuilder.loadTexts:
    qtechSystemLankApMemusageTooHighTrap.setStatus(
        "current"
    )

qtechSystemLankApMemusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 14)
)
qtechSystemLankApMemusageTooHighRecovTrap.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechApMacAddr"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolCurrentUtilization"))
)
if mibBuilder.loadTexts:
    qtechSystemLankApMemusageTooHighRecovTrap.setStatus(
        "current"
    )

qtechSystemResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    qtechSystemResetTrap.setStatus(
        "current"
    )

qtechSystemLankApResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 16)
)
qtechSystemLankApResetTrap.setObjects(
    ("QTECH-AC-MGMT-MIB", "qtechApMacAddr")
)
if mibBuilder.loadTexts:
    qtechSystemLankApResetTrap.setStatus(
        "current"
    )

qtechSystemPowerOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 17)
)
qtechSystemPowerOnTrap.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemPowerIndex")
)
if mibBuilder.loadTexts:
    qtechSystemPowerOnTrap.setStatus(
        "current"
    )

qtechSystemPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 18)
)
qtechSystemPowerOffTrap.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemPowerIndex")
)
if mibBuilder.loadTexts:
    qtechSystemPowerOffTrap.setStatus(
        "current"
    )

qtechSystemPowerOnTrapInVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 19)
)
qtechSystemPowerOnTrapInVSU.setObjects(
      *(("QTECH-SYSTEM-MIB", "qtechSystemSwitchID"),
        ("QTECH-SYSTEM-MIB", "qtechSystemPowerIndex"))
)
if mibBuilder.loadTexts:
    qtechSystemPowerOnTrapInVSU.setStatus(
        "current"
    )

qtechSystemPowerOffTrapInVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 20)
)
qtechSystemPowerOffTrapInVSU.setObjects(
      *(("QTECH-SYSTEM-MIB", "qtechSystemSwitchID"),
        ("QTECH-SYSTEM-MIB", "qtechSystemPowerIndex"))
)
if mibBuilder.loadTexts:
    qtechSystemPowerOffTrapInVSU.setStatus(
        "current"
    )

qtechSystemTmpTableTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 21)
)
qtechSystemTmpTableTooHighTrap.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemMultipleTemperatureSlotIndex")
)
if mibBuilder.loadTexts:
    qtechSystemTmpTableTooHighTrap.setStatus(
        "current"
    )

qtechSystemTmpTableTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 22)
)
qtechSystemTmpTableTooHighRecovTrap.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemMultipleTemperatureSlotIndex")
)
if mibBuilder.loadTexts:
    qtechSystemTmpTableTooHighRecovTrap.setStatus(
        "current"
    )

qtechSystemTmpTableTooHighTrapVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 23)
)
qtechSystemTmpTableTooHighTrapVSU.setObjects(
      *(("QTECH-SYSTEM-MIB", "qtechSystemMultipleTemperatureDeviceIndex"),
        ("QTECH-SYSTEM-MIB", "qtechSystemMultipleTemperatureSlotIndex"))
)
if mibBuilder.loadTexts:
    qtechSystemTmpTableTooHighTrapVSU.setStatus(
        "current"
    )

qtechSystemTmpTableTooHighRecovTrapVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 24)
)
qtechSystemTmpTableTooHighRecovTrapVSU.setObjects(
      *(("QTECH-SYSTEM-MIB", "qtechSystemMultipleTemperatureDeviceIndex"),
        ("QTECH-SYSTEM-MIB", "qtechSystemMultipleTemperatureSlotIndex"))
)
if mibBuilder.loadTexts:
    qtechSystemTmpTableTooHighRecovTrapVSU.setStatus(
        "current"
    )

qtechSystemFanTableStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 25)
)
qtechSystemFanTableStateChange.setObjects(
      *(("QTECH-SYSTEM-MIB", "qtechSystemFanStatusFanIndex"),
        ("QTECH-SYSTEM-MIB", "qtechSystemFanStatusIndex"),
        ("QTECH-SYSTEM-MIB", "qtechSystemFanStatus"))
)
if mibBuilder.loadTexts:
    qtechSystemFanTableStateChange.setStatus(
        "current"
    )

qtechSystemFanTableStateChangeVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 2, 26)
)
qtechSystemFanTableStateChangeVSU.setObjects(
      *(("QTECH-SYSTEM-MIB", "qtechSystemFanStatusDeviceIndex"),
        ("QTECH-SYSTEM-MIB", "qtechSystemFanStatusFanIndex"),
        ("QTECH-SYSTEM-MIB", "qtechSystemFanStatusIndex"),
        ("QTECH-SYSTEM-MIB", "qtechSystemFanStatus"))
)
if mibBuilder.loadTexts:
    qtechSystemFanTableStateChangeVSU.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechSystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 1, 3, 1, 1)
)
qtechSystemMIBCompliance.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemMIBGroup")
)
if mibBuilder.loadTexts:
    qtechSystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SYSTEM-MIB",
    **{"qtechSystemMIB": qtechSystemMIB,
       "qtechSystemMIBObjects": qtechSystemMIBObjects,
       "qtechSystemHwVersion": qtechSystemHwVersion,
       "qtechSystemSwVersion": qtechSystemSwVersion,
       "qtechSystemBootVersion": qtechSystemBootVersion,
       "qtechSystemSysCtrlVersion": qtechSystemSysCtrlVersion,
       "qtechSystemParametersSave": qtechSystemParametersSave,
       "qtechSystemOutBandRate": qtechSystemOutBandRate,
       "qtechSystemReset": qtechSystemReset,
       "qtechSwitchLayer": qtechSwitchLayer,
       "qtechSystemHwPower": qtechSystemHwPower,
       "qtechSystemHwFan": qtechSystemHwFan,
       "qtechSystemOutBandTimeout": qtechSystemOutBandTimeout,
       "qtechSystemTelnetTimeout": qtechSystemTelnetTimeout,
       "qtechSystemMainFile": qtechSystemMainFile,
       "qtechSystemCurrentPower": qtechSystemCurrentPower,
       "qtechSystemRemainPower": qtechSystemRemainPower,
       "qtechSystemTemperature": qtechSystemTemperature,
       "qtechSystemElectricalSourceNum": qtechSystemElectricalSourceNum,
       "qtechSystemElectricalSourceIsNormalTable": qtechSystemElectricalSourceIsNormalTable,
       "qtechSystemElectricalSourceIsNormalEntry": qtechSystemElectricalSourceIsNormalEntry,
       "qtechSystemElectricalSourceIsNormalIndex": qtechSystemElectricalSourceIsNormalIndex,
       "qtechSystemElectricalSourceIsNormal": qtechSystemElectricalSourceIsNormal,
       "qtechSystemElectricalSourceName": qtechSystemElectricalSourceName,
       "qtechSystemCurrentVoltage": qtechSystemCurrentVoltage,
       "qtechSystemFanNUM": qtechSystemFanNUM,
       "qtechSystemFanIsNormalTable": qtechSystemFanIsNormalTable,
       "qtechSystemFanIsNormalEntry": qtechSystemFanIsNormalEntry,
       "qtechSystemFanIsNormalIndex": qtechSystemFanIsNormalIndex,
       "qtechSystemFanIsNormal": qtechSystemFanIsNormal,
       "qtechSystemFanName": qtechSystemFanName,
       "qtechSystemFanSpeed": qtechSystemFanSpeed,
       "qtechSystemReloadTimeRemain": qtechSystemReloadTimeRemain,
       "qtechSystemTemperatureTable": qtechSystemTemperatureTable,
       "qtechSystemTemperatureEntry": qtechSystemTemperatureEntry,
       "qtechSystemTemperatureIndex": qtechSystemTemperatureIndex,
       "qtechSystemTemperatureName": qtechSystemTemperatureName,
       "qtechSystemTemperatureCurrent": qtechSystemTemperatureCurrent,
       "qtechSystemTemperatureWarningVaule": qtechSystemTemperatureWarningVaule,
       "qtechSystemTemperatureCritialVaule": qtechSystemTemperatureCritialVaule,
       "qtechSystemSerialno": qtechSystemSerialno,
       "qtechSystemVersionTable": qtechSystemVersionTable,
       "qtechSystemVersionEntry": qtechSystemVersionEntry,
       "qtechSystemVersionIndex": qtechSystemVersionIndex,
       "qtechSystemVersionName": qtechSystemVersionName,
       "qtechSystemVersionSwBoot": qtechSystemVersionSwBoot,
       "qtechSystemVersionSwCtrl": qtechSystemVersionSwCtrl,
       "qtechSystemVersionSwMain": qtechSystemVersionSwMain,
       "qtechSystemVersionHw": qtechSystemVersionHw,
       "qtechSystemVersionSerialno": qtechSystemVersionSerialno,
       "qtechSystemSysModel": qtechSystemSysModel,
       "qtechSystemUptime": qtechSystemUptime,
       "qtechSystemSampleTime": qtechSystemSampleTime,
       "qtechSystemStatWindowTime": qtechSystemStatWindowTime,
       "qtechSystemManufacturer": qtechSystemManufacturer,
       "qtechSystemCurrentTime": qtechSystemCurrentTime,
       "qtechSystemWarnResendTime": qtechSystemWarnResendTime,
       "qtechSystemSoftwareName": qtechSystemSoftwareName,
       "qtechSystemSoftwareManufacturer": qtechSystemSoftwareManufacturer,
       "qtechSystemCpuType": qtechSystemCpuType,
       "qtechSystemMemoryType": qtechSystemMemoryType,
       "qtechSystemMemorySize": qtechSystemMemorySize,
       "qtechSystemFlashSize": qtechSystemFlashSize,
       "qtechSystemLankApTable": qtechSystemLankApTable,
       "qtechSystemLankApEntry": qtechSystemLankApEntry,
       "qtechSystemLankApMacAddr": qtechSystemLankApMacAddr,
       "qtechSystemLankApStatWindowTime": qtechSystemLankApStatWindowTime,
       "qtechSystemLankApSampleTime": qtechSystemLankApSampleTime,
       "qtechSystemLankApReset": qtechSystemLankApReset,
       "qtechSystemLankApSoftwareName": qtechSystemLankApSoftwareName,
       "qtechSystemLankApSwVersion": qtechSystemLankApSwVersion,
       "qtechSystemLankApSoftwareManufacturer": qtechSystemLankApSoftwareManufacturer,
       "qtechSystemLankApCpuType": qtechSystemLankApCpuType,
       "qtechSystemLankApMemoryType": qtechSystemLankApMemoryType,
       "qtechSystemLankApMemorySize": qtechSystemLankApMemorySize,
       "qtechSystemLankAPFlashSize": qtechSystemLankAPFlashSize,
       "qtechSystemLankApManufacturer": qtechSystemLankApManufacturer,
       "qtechSystemLankApSerialno": qtechSystemLankApSerialno,
       "qtechSystemLankApSysModel": qtechSystemLankApSysModel,
       "qtechSystemLankApUptime": qtechSystemLankApUptime,
       "qtechSystemLankApAccurateUptime": qtechSystemLankApAccurateUptime,
       "qtechSystemLankApHwVersion": qtechSystemLankApHwVersion,
       "qtechSystemBoardTemperatureTable": qtechSystemBoardTemperatureTable,
       "qtechSystemBoardTemperatureEntry": qtechSystemBoardTemperatureEntry,
       "qtechSystemBoardTemperatureIndex": qtechSystemBoardTemperatureIndex,
       "qtechSystemBoardTemperatureName": qtechSystemBoardTemperatureName,
       "qtechSystemBoardTemperatureCurrent": qtechSystemBoardTemperatureCurrent,
       "qtechSystemElectricalInformationTable": qtechSystemElectricalInformationTable,
       "qtechSystemElectricalInformationEntry": qtechSystemElectricalInformationEntry,
       "qtechSystemElectricalInformationDeviceIndex": qtechSystemElectricalInformationDeviceIndex,
       "qtechSystemElectricalInformationIndex": qtechSystemElectricalInformationIndex,
       "qtechSystemElectricalInformationStatus": qtechSystemElectricalInformationStatus,
       "qtechSystemElectricalInformationType": qtechSystemElectricalInformationType,
       "qtechSystemElectricalInformationAttribute": qtechSystemElectricalInformationAttribute,
       "qtechSystemElectricalInformationSofeVersion": qtechSystemElectricalInformationSofeVersion,
       "qtechSystemElectricalInformationHardwareVersion": qtechSystemElectricalInformationHardwareVersion,
       "qtechSystemElectricalInformationSerial": qtechSystemElectricalInformationSerial,
       "qtechSystemElectricalInformationProductionDate": qtechSystemElectricalInformationProductionDate,
       "qtechSystemElectricalInformationRatedPower": qtechSystemElectricalInformationRatedPower,
       "qtechSystemElectricalInformationInVoltage": qtechSystemElectricalInformationInVoltage,
       "qtechSystemElectricalInformationInCurrent": qtechSystemElectricalInformationInCurrent,
       "qtechSystemElectricalInformationOutVoltage": qtechSystemElectricalInformationOutVoltage,
       "qtechSystemElectricalInformationOutCurrent": qtechSystemElectricalInformationOutCurrent,
       "qtechSystemElectricalInformationOutPower": qtechSystemElectricalInformationOutPower,
       "qtechSystemElectricalInformationTemperature": qtechSystemElectricalInformationTemperature,
       "qtechSystemElectricalInformationAirflowCoexist": qtechSystemElectricalInformationAirflowCoexist,
       "qtechSystemElectricalInformationWarningStatus": qtechSystemElectricalInformationWarningStatus,
       "qtechSystemFanInformationTable": qtechSystemFanInformationTable,
       "qtechSystemFanInformationEntry": qtechSystemFanInformationEntry,
       "qtechSystemFanInformationDeviceIndex": qtechSystemFanInformationDeviceIndex,
       "qtechSystemFanInformationFanIndex": qtechSystemFanInformationFanIndex,
       "qtechSystemFanInformationStatus": qtechSystemFanInformationStatus,
       "qtechSystemFanInformationType": qtechSystemFanInformationType,
       "qtechSystemFanInformationAttribute": qtechSystemFanInformationAttribute,
       "qtechSystemFanInformationSofeVersion": qtechSystemFanInformationSofeVersion,
       "qtechSystemFanInformationFirmwareVersion": qtechSystemFanInformationFirmwareVersion,
       "qtechSystemFanInformationHardwareVersion": qtechSystemFanInformationHardwareVersion,
       "qtechSystemFanInformationSerial": qtechSystemFanInformationSerial,
       "qtechSystemFanInformationProductionDate": qtechSystemFanInformationProductionDate,
       "qtechSystemFanInformationTemperature": qtechSystemFanInformationTemperature,
       "qtechSystemFanInformationNumber": qtechSystemFanInformationNumber,
       "qtechSystemFanInformationAirflowCoexist": qtechSystemFanInformationAirflowCoexist,
       "qtechSystemFanInformationWarningStatus": qtechSystemFanInformationWarningStatus,
       "qtechSystemFanStatusTable": qtechSystemFanStatusTable,
       "qtechSystemFanStatusEntry": qtechSystemFanStatusEntry,
       "qtechSystemFanStatusDeviceIndex": qtechSystemFanStatusDeviceIndex,
       "qtechSystemFanStatusFanIndex": qtechSystemFanStatusFanIndex,
       "qtechSystemFanStatusIndex": qtechSystemFanStatusIndex,
       "qtechSystemFanStatus": qtechSystemFanStatus,
       "qtechSystemFanStatusLevel": qtechSystemFanStatusLevel,
       "qtechSystemFanStatusSpeed": qtechSystemFanStatusSpeed,
       "qtechSystemMultipleTemperatureTable": qtechSystemMultipleTemperatureTable,
       "qtechSystemMultipleTemperatureEntry": qtechSystemMultipleTemperatureEntry,
       "qtechSystemMultipleTemperatureDeviceIndex": qtechSystemMultipleTemperatureDeviceIndex,
       "qtechSystemMultipleTemperatureSlotIndex": qtechSystemMultipleTemperatureSlotIndex,
       "qtechSystemMultipleTemperatureIndex": qtechSystemMultipleTemperatureIndex,
       "qtechSystemMultipleTemperatureName": qtechSystemMultipleTemperatureName,
       "qtechSystemMultipleTemperatureCurrent": qtechSystemMultipleTemperatureCurrent,
       "qtechSystemMultipleTemperatureWarning": qtechSystemMultipleTemperatureWarning,
       "qtechSystemMultipleTemperatureCritical": qtechSystemMultipleTemperatureCritical,
       "qtechSystemAccurateUptime": qtechSystemAccurateUptime,
       "qtechSystemPowerIndex": qtechSystemPowerIndex,
       "qtechSystemSwitchID": qtechSystemSwitchID,
       "qtechSystemApDeviceDescriptionTable": qtechSystemApDeviceDescriptionTable,
       "qtechSystemApDeviceDescriptionEntry": qtechSystemApDeviceDescriptionEntry,
       "qtechSystemApDescMacAddr": qtechSystemApDescMacAddr,
       "qtechSystemApMemoryType": qtechSystemApMemoryType,
       "qtechSystemApMemorySize": qtechSystemApMemorySize,
       "qtechSystemAPFlashType": qtechSystemAPFlashType,
       "qtechSystemAPFlashSize": qtechSystemAPFlashSize,
       "qtechSystemApNVRAMSize": qtechSystemApNVRAMSize,
       "qtechSystemApCFSize": qtechSystemApCFSize,
       "qtechSystemApCPUType": qtechSystemApCPUType,
       "qtechSystemApDeviceStatisticsTable": qtechSystemApDeviceStatisticsTable,
       "qtechSystemApDeviceStatisticsEntry": qtechSystemApDeviceStatisticsEntry,
       "qtechSystemApStatMacAddr": qtechSystemApStatMacAddr,
       "qtechSystemApInterfaceNum": qtechSystemApInterfaceNum,
       "qtechSystemApUptime": qtechSystemApUptime,
       "qtechSystemApCPUUtilizationCurrent": qtechSystemApCPUUtilizationCurrent,
       "qtechSystemApCPUUtilizationAverage": qtechSystemApCPUUtilizationAverage,
       "qtechSystemApMemoryPoolCurrentUtilization": qtechSystemApMemoryPoolCurrentUtilization,
       "qtechSystemApMemoryPoolAverageUtilization": qtechSystemApMemoryPoolAverageUtilization,
       "qtechSystemApFlashFreeSize": qtechSystemApFlashFreeSize,
       "qtechSystemAPDeviceTemperature": qtechSystemAPDeviceTemperature,
       "qtechSystemUptimeMsLow": qtechSystemUptimeMsLow,
       "qtechSystemUptimeMsHigh": qtechSystemUptimeMsHigh,
       "qtechSystemFanSNTable": qtechSystemFanSNTable,
       "qtechSystemFanSNEntry": qtechSystemFanSNEntry,
       "qtechSystemFanPadIndex": qtechSystemFanPadIndex,
       "qtechSystemFanPadName": qtechSystemFanPadName,
       "qtechSystemFanPadSN": qtechSystemFanPadSN,
       "qtechSystemDsfSNTable": qtechSystemDsfSNTable,
       "qtechSystemDsfSNEntry": qtechSystemDsfSNEntry,
       "qtechSystemDsfIndex": qtechSystemDsfIndex,
       "qtechSystemDsfName": qtechSystemDsfName,
       "qtechSystemDsfSN": qtechSystemDsfSN,
       "qtechSystemPowerSNTable": qtechSystemPowerSNTable,
       "qtechSystemPowerSNEntry": qtechSystemPowerSNEntry,
       "qtechSystemPowerSNIndex": qtechSystemPowerSNIndex,
       "qtechSystemPowerSNName": qtechSystemPowerSNName,
       "qtechSystemPowerSN": qtechSystemPowerSN,
       "qtechSystemFanPad1SpeedTable": qtechSystemFanPad1SpeedTable,
       "qtechSystemFanPad1SpeedEntry": qtechSystemFanPad1SpeedEntry,
       "qtechSystemOamFanPad1Index": qtechSystemOamFanPad1Index,
       "qtechSystemOamFanPad1Name": qtechSystemOamFanPad1Name,
       "qtechSystemFanPad1Speed1": qtechSystemFanPad1Speed1,
       "qtechSystemFanPad1Speed2": qtechSystemFanPad1Speed2,
       "qtechSystemFanPad1Speed3": qtechSystemFanPad1Speed3,
       "qtechSystemFanPad1Speed4": qtechSystemFanPad1Speed4,
       "qtechSystemFanPad1Speed5": qtechSystemFanPad1Speed5,
       "qtechSystemFanPad1Speed6": qtechSystemFanPad1Speed6,
       "qtechSystemFanPad1Speed7": qtechSystemFanPad1Speed7,
       "qtechSystemFanPad1Speed8": qtechSystemFanPad1Speed8,
       "qtechSystemFanPad1Speed9": qtechSystemFanPad1Speed9,
       "qtechSystemFanPad2SpeedTable": qtechSystemFanPad2SpeedTable,
       "qtechSystemFanPad2SpeedEntry": qtechSystemFanPad2SpeedEntry,
       "qtechSystemOamFanPad2Index": qtechSystemOamFanPad2Index,
       "qtechSystemOamFanPad2Name": qtechSystemOamFanPad2Name,
       "qtechSystemFanPad2Speed1": qtechSystemFanPad2Speed1,
       "qtechSystemFanPad2Speed2": qtechSystemFanPad2Speed2,
       "qtechSystemFanPad2Speed3": qtechSystemFanPad2Speed3,
       "qtechSystemFanPad3SpeedTable": qtechSystemFanPad3SpeedTable,
       "qtechSystemFanPad3SpeedEntry": qtechSystemFanPad3SpeedEntry,
       "qtechSystemOamFanPad3Index": qtechSystemOamFanPad3Index,
       "qtechSystemOamFanPad3Name": qtechSystemOamFanPad3Name,
       "qtechSystemFanPad3Speed1": qtechSystemFanPad3Speed1,
       "qtechSystemFanPad3Speed2": qtechSystemFanPad3Speed2,
       "qtechSystemFanPad3Speed3": qtechSystemFanPad3Speed3,
       "qtechSystemFanPad3Speed4": qtechSystemFanPad3Speed4,
       "qtechSystemFanPad3Speed5": qtechSystemFanPad3Speed5,
       "qtechSystemMIBTraps": qtechSystemMIBTraps,
       "qtechSystemHardChangeDesc": qtechSystemHardChangeDesc,
       "qtechSystemHardChangeDetected": qtechSystemHardChangeDetected,
       "qtechSystemPowerStateChange": qtechSystemPowerStateChange,
       "qtechSystemFanStateChange": qtechSystemFanStateChange,
       "qtechSystemCPUusageTooHighTrap": qtechSystemCPUusageTooHighTrap,
       "qtechSystemCPUusageTooHighRecovTrap": qtechSystemCPUusageTooHighRecovTrap,
       "qtechSystemTmpTooHighTrap": qtechSystemTmpTooHighTrap,
       "qtechSystemTmpTooHighRecovTrap": qtechSystemTmpTooHighRecovTrap,
       "qtechSystemMemusageTooHighTrap": qtechSystemMemusageTooHighTrap,
       "qtechSystemMemusageTooHighRecovTrap": qtechSystemMemusageTooHighRecovTrap,
       "qtechSystemLankApCPUusageTooHighTrap": qtechSystemLankApCPUusageTooHighTrap,
       "qtechSystemLankApCPUusageTooHighRecovTrap": qtechSystemLankApCPUusageTooHighRecovTrap,
       "qtechSystemLankApMemusageTooHighTrap": qtechSystemLankApMemusageTooHighTrap,
       "qtechSystemLankApMemusageTooHighRecovTrap": qtechSystemLankApMemusageTooHighRecovTrap,
       "qtechSystemResetTrap": qtechSystemResetTrap,
       "qtechSystemLankApResetTrap": qtechSystemLankApResetTrap,
       "qtechSystemPowerOnTrap": qtechSystemPowerOnTrap,
       "qtechSystemPowerOffTrap": qtechSystemPowerOffTrap,
       "qtechSystemPowerOnTrapInVSU": qtechSystemPowerOnTrapInVSU,
       "qtechSystemPowerOffTrapInVSU": qtechSystemPowerOffTrapInVSU,
       "qtechSystemTmpTableTooHighTrap": qtechSystemTmpTableTooHighTrap,
       "qtechSystemTmpTableTooHighRecovTrap": qtechSystemTmpTableTooHighRecovTrap,
       "qtechSystemTmpTableTooHighTrapVSU": qtechSystemTmpTableTooHighTrapVSU,
       "qtechSystemTmpTableTooHighRecovTrapVSU": qtechSystemTmpTableTooHighRecovTrapVSU,
       "qtechSystemFanTableStateChange": qtechSystemFanTableStateChange,
       "qtechSystemFanTableStateChangeVSU": qtechSystemFanTableStateChangeVSU,
       "qtechSystemMIBConformance": qtechSystemMIBConformance,
       "qtechSystemMIBCompliances": qtechSystemMIBCompliances,
       "qtechSystemMIBCompliance": qtechSystemMIBCompliance,
       "qtechSystemMIBGroups": qtechSystemMIBGroups,
       "qtechSystemMIBGroup": qtechSystemMIBGroup}
)
