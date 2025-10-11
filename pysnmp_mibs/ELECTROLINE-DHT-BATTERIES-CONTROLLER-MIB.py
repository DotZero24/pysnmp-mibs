# SNMP MIB module (ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:01 2025
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

(dhtExtensionsMibObjects,) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-EXTENSIONS-MIB",
    "dhtExtensionsMibObjects")

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


# MODULE-IDENTITY

battManIdentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16)
)
if mibBuilder.loadTexts:
    battManIdentMIB.setRevisions(
        ("2015-03-19 00:00",
         "2015-04-20 00:00",
         "2015-08-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class HundredthmOhm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


class HundredthkS(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_BattManIdentObjects_ObjectIdentity = ObjectIdentity
battManIdentObjects = _BattManIdentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1)
)
_BattManMonitored_Type = Integer32
_BattManMonitored_Object = MibScalar
battManMonitored = _BattManMonitored_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 1),
    _BattManMonitored_Type()
)
battManMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManMonitored.setStatus("mandatory")
_BattManDeviceTable_Object = MibTable
battManDeviceTable = _BattManDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    battManDeviceTable.setStatus("mandatory")
_BattManDeviceEntry_Object = MibTableRow
battManDeviceEntry = _BattManDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1)
)
battManDeviceEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManDeviceAddress"),
)
if mibBuilder.loadTexts:
    battManDeviceEntry.setStatus("mandatory")


class _BattManDeviceAddress_Type(Integer32):
    """Custom type battManDeviceAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 127),
    )


_BattManDeviceAddress_Type.__name__ = "Integer32"
_BattManDeviceAddress_Object = MibTableColumn
battManDeviceAddress = _BattManDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 1),
    _BattManDeviceAddress_Type()
)
battManDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManDeviceAddress.setStatus("mandatory")


class _BattManProtocolVersion_Type(Integer32):
    """Custom type battManProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_BattManProtocolVersion_Type.__name__ = "Integer32"
_BattManProtocolVersion_Object = MibTableColumn
battManProtocolVersion = _BattManProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 2),
    _BattManProtocolVersion_Type()
)
battManProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManProtocolVersion.setStatus("mandatory")


class _BattManSoftwareVersion_Type(OctetString):
    """Custom type battManSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_BattManSoftwareVersion_Type.__name__ = "OctetString"
_BattManSoftwareVersion_Object = MibTableColumn
battManSoftwareVersion = _BattManSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 3),
    _BattManSoftwareVersion_Type()
)
battManSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManSoftwareVersion.setStatus("mandatory")


class _BattManDeviceId_Type(OctetString):
    """Custom type battManDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_BattManDeviceId_Type.__name__ = "OctetString"
_BattManDeviceId_Object = MibTableColumn
battManDeviceId = _BattManDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 4),
    _BattManDeviceId_Type()
)
battManDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManDeviceId.setStatus("mandatory")


class _BattManVendorIdentity_Type(DisplayString):
    """Custom type battManVendorIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_BattManVendorIdentity_Type.__name__ = "DisplayString"
_BattManVendorIdentity_Object = MibTableColumn
battManVendorIdentity = _BattManVendorIdentity_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 5),
    _BattManVendorIdentity_Type()
)
battManVendorIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManVendorIdentity.setStatus("mandatory")
_BattManStringVoltage_Type = Integer32
_BattManStringVoltage_Object = MibTableColumn
battManStringVoltage = _BattManStringVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 6),
    _BattManStringVoltage_Type()
)
battManStringVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManStringVoltage.setStatus("mandatory")
_BattManBatteries_Type = Integer32
_BattManBatteries_Object = MibTableColumn
battManBatteries = _BattManBatteries_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 7),
    _BattManBatteries_Type()
)
battManBatteries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteries.setStatus("mandatory")
_BattManBatteryStrings_Type = Integer32
_BattManBatteryStrings_Object = MibTableColumn
battManBatteryStrings = _BattManBatteryStrings_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 8),
    _BattManBatteryStrings_Type()
)
battManBatteryStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryStrings.setStatus("mandatory")
_BattManBatteriesPerStrings_Type = Integer32
_BattManBatteriesPerStrings_Object = MibTableColumn
battManBatteriesPerStrings = _BattManBatteriesPerStrings_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 9),
    _BattManBatteriesPerStrings_Type()
)
battManBatteriesPerStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteriesPerStrings.setStatus("mandatory")


class _BattManVoltageSupport_Type(Integer32):
    """Custom type battManVoltageSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_BattManVoltageSupport_Type.__name__ = "Integer32"
_BattManVoltageSupport_Object = MibTableColumn
battManVoltageSupport = _BattManVoltageSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 10),
    _BattManVoltageSupport_Type()
)
battManVoltageSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManVoltageSupport.setStatus("mandatory")


class _BattManTemperatureSupport_Type(Integer32):
    """Custom type battManTemperatureSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_BattManTemperatureSupport_Type.__name__ = "Integer32"
_BattManTemperatureSupport_Object = MibTableColumn
battManTemperatureSupport = _BattManTemperatureSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 11),
    _BattManTemperatureSupport_Type()
)
battManTemperatureSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManTemperatureSupport.setStatus("mandatory")


class _BattManImpedanceSupport_Type(Integer32):
    """Custom type battManImpedanceSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_BattManImpedanceSupport_Type.__name__ = "Integer32"
_BattManImpedanceSupport_Object = MibTableColumn
battManImpedanceSupport = _BattManImpedanceSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 12),
    _BattManImpedanceSupport_Type()
)
battManImpedanceSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManImpedanceSupport.setStatus("mandatory")


class _BattManEqualPercentSupport_Type(Integer32):
    """Custom type battManEqualPercentSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_BattManEqualPercentSupport_Type.__name__ = "Integer32"
_BattManEqualPercentSupport_Object = MibTableColumn
battManEqualPercentSupport = _BattManEqualPercentSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 13),
    _BattManEqualPercentSupport_Type()
)
battManEqualPercentSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManEqualPercentSupport.setStatus("mandatory")


class _BattManBatteryStatusSupport_Type(Integer32):
    """Custom type battManBatteryStatusSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_BattManBatteryStatusSupport_Type.__name__ = "Integer32"
_BattManBatteryStatusSupport_Object = MibTableColumn
battManBatteryStatusSupport = _BattManBatteryStatusSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 14),
    _BattManBatteryStatusSupport_Type()
)
battManBatteryStatusSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryStatusSupport.setStatus("mandatory")


class _BattManDiagSupport_Type(Integer32):
    """Custom type battManDiagSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_BattManDiagSupport_Type.__name__ = "Integer32"
_BattManDiagSupport_Object = MibTableColumn
battManDiagSupport = _BattManDiagSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 15),
    _BattManDiagSupport_Type()
)
battManDiagSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManDiagSupport.setStatus("mandatory")


class _BattManEnvDataSupport_Type(Integer32):
    """Custom type battManEnvDataSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_BattManEnvDataSupport_Type.__name__ = "Integer32"
_BattManEnvDataSupport_Object = MibTableColumn
battManEnvDataSupport = _BattManEnvDataSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 16),
    _BattManEnvDataSupport_Type()
)
battManEnvDataSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManEnvDataSupport.setStatus("mandatory")


class _BattManManualMeasurementSupport_Type(Integer32):
    """Custom type battManManualMeasurementSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_BattManManualMeasurementSupport_Type.__name__ = "Integer32"
_BattManManualMeasurementSupport_Object = MibTableColumn
battManManualMeasurementSupport = _BattManManualMeasurementSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 2, 1, 17),
    _BattManManualMeasurementSupport_Type()
)
battManManualMeasurementSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManManualMeasurementSupport.setStatus("mandatory")
_BattManStringTable_Object = MibTable
battManStringTable = _BattManStringTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 3)
)
if mibBuilder.loadTexts:
    battManStringTable.setStatus("mandatory")
_BattManStringEntry_Object = MibTableRow
battManStringEntry = _BattManStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 3, 1)
)
battManStringEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManStringDeviceAddress"),
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManString"),
)
if mibBuilder.loadTexts:
    battManStringEntry.setStatus("mandatory")
_BattManStringDeviceAddress_Type = Integer32
_BattManStringDeviceAddress_Object = MibTableColumn
battManStringDeviceAddress = _BattManStringDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 3, 1, 1),
    _BattManStringDeviceAddress_Type()
)
battManStringDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManStringDeviceAddress.setStatus("mandatory")
_BattManString_Type = Integer32
_BattManString_Object = MibTableColumn
battManString = _BattManString_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 3, 1, 2),
    _BattManString_Type()
)
battManString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManString.setStatus("mandatory")
_BattManStringBatteries_Type = Integer32
_BattManStringBatteries_Object = MibTableColumn
battManStringBatteries = _BattManStringBatteries_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 3, 1, 3),
    _BattManStringBatteries_Type()
)
battManStringBatteries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManStringBatteries.setStatus("mandatory")
_BattManStringTotalVoltage_Type = Integer32
_BattManStringTotalVoltage_Object = MibTableColumn
battManStringTotalVoltage = _BattManStringTotalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 3, 1, 4),
    _BattManStringTotalVoltage_Type()
)
battManStringTotalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManStringTotalVoltage.setStatus("mandatory")
_BattManBatteryTable_Object = MibTable
battManBatteryTable = _BattManBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4)
)
if mibBuilder.loadTexts:
    battManBatteryTable.setStatus("mandatory")
_BattManBatteryEntry_Object = MibTableRow
battManBatteryEntry = _BattManBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1)
)
battManBatteryEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManBatteryDeviceAddress"),
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManBatteryStringID"),
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManBattery"),
)
if mibBuilder.loadTexts:
    battManBatteryEntry.setStatus("mandatory")
_BattManBatteryDeviceAddress_Type = Integer32
_BattManBatteryDeviceAddress_Object = MibTableColumn
battManBatteryDeviceAddress = _BattManBatteryDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 1),
    _BattManBatteryDeviceAddress_Type()
)
battManBatteryDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryDeviceAddress.setStatus("mandatory")
_BattManBattery_Type = Integer32
_BattManBattery_Object = MibTableColumn
battManBattery = _BattManBattery_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 2),
    _BattManBattery_Type()
)
battManBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattery.setStatus("mandatory")
_BattManBatteryStringID_Type = Integer32
_BattManBatteryStringID_Object = MibTableColumn
battManBatteryStringID = _BattManBatteryStringID_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 3),
    _BattManBatteryStringID_Type()
)
battManBatteryStringID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryStringID.setStatus("mandatory")
_BattManBatteryVersion_Type = Integer32
_BattManBatteryVersion_Object = MibTableColumn
battManBatteryVersion = _BattManBatteryVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 4),
    _BattManBatteryVersion_Type()
)
battManBatteryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryVersion.setStatus("mandatory")
_BattManBatteryHwVersion_Type = OctetString
_BattManBatteryHwVersion_Object = MibTableColumn
battManBatteryHwVersion = _BattManBatteryHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 5),
    _BattManBatteryHwVersion_Type()
)
battManBatteryHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryHwVersion.setStatus("mandatory")
_BattManBatterySwVersion_Type = OctetString
_BattManBatterySwVersion_Object = MibTableColumn
battManBatterySwVersion = _BattManBatterySwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 6),
    _BattManBatterySwVersion_Type()
)
battManBatterySwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatterySwVersion.setStatus("mandatory")
_BattManBatteryVoltage_Type = Integer32
_BattManBatteryVoltage_Object = MibTableColumn
battManBatteryVoltage = _BattManBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 7),
    _BattManBatteryVoltage_Type()
)
battManBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryVoltage.setStatus("mandatory")
_BattManBatteryTemperature_Type = Integer32
_BattManBatteryTemperature_Object = MibTableColumn
battManBatteryTemperature = _BattManBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 8),
    _BattManBatteryTemperature_Type()
)
battManBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryTemperature.setStatus("mandatory")
_BattManBatteryImpedance_Type = Integer32
_BattManBatteryImpedance_Object = MibTableColumn
battManBatteryImpedance = _BattManBatteryImpedance_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 9),
    _BattManBatteryImpedance_Type()
)
battManBatteryImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryImpedance.setStatus("mandatory")
_BattManBatteryEqualizationPercent_Type = Integer32
_BattManBatteryEqualizationPercent_Object = MibTableColumn
battManBatteryEqualizationPercent = _BattManBatteryEqualizationPercent_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 10),
    _BattManBatteryEqualizationPercent_Type()
)
battManBatteryEqualizationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryEqualizationPercent.setStatus("mandatory")


class _BattManBatteryStatus_Type(Integer32):
    """Custom type battManBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_BattManBatteryStatus_Type.__name__ = "Integer32"
_BattManBatteryStatus_Object = MibTableColumn
battManBatteryStatus = _BattManBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 11),
    _BattManBatteryStatus_Type()
)
battManBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryStatus.setStatus("mandatory")
_BattManBatteryDatasetID_Type = Unsigned32
_BattManBatteryDatasetID_Object = MibTableColumn
battManBatteryDatasetID = _BattManBatteryDatasetID_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 4, 1, 12),
    _BattManBatteryDatasetID_Type()
)
battManBatteryDatasetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryDatasetID.setStatus("mandatory")
_BattManBatteryDiagTable_Object = MibTable
battManBatteryDiagTable = _BattManBatteryDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 5)
)
if mibBuilder.loadTexts:
    battManBatteryDiagTable.setStatus("mandatory")
_BattManBatteryDiagEntry_Object = MibTableRow
battManBatteryDiagEntry = _BattManBatteryDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 5, 1)
)
battManBatteryDiagEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManBatteryDiagDeviceAddress"),
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManBatteryDiagModuleID"),
)
if mibBuilder.loadTexts:
    battManBatteryDiagEntry.setStatus("mandatory")
_BattManBatteryDiagDeviceAddress_Type = Integer32
_BattManBatteryDiagDeviceAddress_Object = MibTableColumn
battManBatteryDiagDeviceAddress = _BattManBatteryDiagDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 5, 1, 1),
    _BattManBatteryDiagDeviceAddress_Type()
)
battManBatteryDiagDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryDiagDeviceAddress.setStatus("mandatory")
_BattManBatteryDiagModuleID_Type = Integer32
_BattManBatteryDiagModuleID_Object = MibTableColumn
battManBatteryDiagModuleID = _BattManBatteryDiagModuleID_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 5, 1, 2),
    _BattManBatteryDiagModuleID_Type()
)
battManBatteryDiagModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryDiagModuleID.setStatus("mandatory")
_BattManBatteryDiagPageNumber_Type = Integer32
_BattManBatteryDiagPageNumber_Object = MibTableColumn
battManBatteryDiagPageNumber = _BattManBatteryDiagPageNumber_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 5, 1, 3),
    _BattManBatteryDiagPageNumber_Type()
)
battManBatteryDiagPageNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battManBatteryDiagPageNumber.setStatus("mandatory")


class _BattManBatteryDiagPageData_Type(OctetString):
    """Custom type battManBatteryDiagPageData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_BattManBatteryDiagPageData_Type.__name__ = "OctetString"
_BattManBatteryDiagPageData_Object = MibTableColumn
battManBatteryDiagPageData = _BattManBatteryDiagPageData_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 5, 1, 4),
    _BattManBatteryDiagPageData_Type()
)
battManBatteryDiagPageData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBatteryDiagPageData.setStatus("mandatory")
_BattManControlTable_Object = MibTable
battManControlTable = _BattManControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 6)
)
if mibBuilder.loadTexts:
    battManControlTable.setStatus("mandatory")
_BattManControlEntry_Object = MibTableRow
battManControlEntry = _BattManControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 6, 1)
)
battManControlEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManControlDeviceAddress"),
)
if mibBuilder.loadTexts:
    battManControlEntry.setStatus("mandatory")
_BattManControlDeviceAddress_Type = Integer32
_BattManControlDeviceAddress_Object = MibTableColumn
battManControlDeviceAddress = _BattManControlDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 6, 1, 1),
    _BattManControlDeviceAddress_Type()
)
battManControlDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManControlDeviceAddress.setStatus("mandatory")


class _BattManControlEqualizationSetting_Type(Integer32):
    """Custom type battManControlEqualizationSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )


_BattManControlEqualizationSetting_Type.__name__ = "Integer32"
_BattManControlEqualizationSetting_Object = MibTableColumn
battManControlEqualizationSetting = _BattManControlEqualizationSetting_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 6, 1, 2),
    _BattManControlEqualizationSetting_Type()
)
battManControlEqualizationSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battManControlEqualizationSetting.setStatus("mandatory")
_BattManControlAutoInterval_Type = Integer32
_BattManControlAutoInterval_Object = MibTableColumn
battManControlAutoInterval = _BattManControlAutoInterval_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 6, 1, 3),
    _BattManControlAutoInterval_Type()
)
battManControlAutoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battManControlAutoInterval.setStatus("mandatory")


class _BattManControlSensorsRestart_Type(Integer32):
    """Custom type battManControlSensorsRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_BattManControlSensorsRestart_Type.__name__ = "Integer32"
_BattManControlSensorsRestart_Object = MibTableColumn
battManControlSensorsRestart = _BattManControlSensorsRestart_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 6, 1, 4),
    _BattManControlSensorsRestart_Type()
)
battManControlSensorsRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battManControlSensorsRestart.setStatus("current")
_BattManStatusTable_Object = MibTable
battManStatusTable = _BattManStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 7)
)
if mibBuilder.loadTexts:
    battManStatusTable.setStatus("mandatory")
_BattManStatusEntry_Object = MibTableRow
battManStatusEntry = _BattManStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 7, 1)
)
battManStatusEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManStatusDeviceAddress"),
)
if mibBuilder.loadTexts:
    battManStatusEntry.setStatus("mandatory")
_BattManStatusDeviceAddress_Type = Integer32
_BattManStatusDeviceAddress_Object = MibTableColumn
battManStatusDeviceAddress = _BattManStatusDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 7, 1, 1),
    _BattManStatusDeviceAddress_Type()
)
battManStatusDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManStatusDeviceAddress.setStatus("mandatory")
_BattManStatusTimeToMeasurement_Type = Unsigned32
_BattManStatusTimeToMeasurement_Object = MibTableColumn
battManStatusTimeToMeasurement = _BattManStatusTimeToMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 7, 1, 2),
    _BattManStatusTimeToMeasurement_Type()
)
battManStatusTimeToMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManStatusTimeToMeasurement.setStatus("mandatory")
_BattManEnvStatusTable_Object = MibTable
battManEnvStatusTable = _BattManEnvStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 8)
)
if mibBuilder.loadTexts:
    battManEnvStatusTable.setStatus("mandatory")
_BattManEnvStatusEntry_Object = MibTableRow
battManEnvStatusEntry = _BattManEnvStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 8, 1)
)
battManEnvStatusEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManEnvStatusDeviceAddress"),
)
if mibBuilder.loadTexts:
    battManEnvStatusEntry.setStatus("mandatory")
_BattManEnvStatusDeviceAddress_Type = Integer32
_BattManEnvStatusDeviceAddress_Object = MibTableColumn
battManEnvStatusDeviceAddress = _BattManEnvStatusDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 8, 1, 1),
    _BattManEnvStatusDeviceAddress_Type()
)
battManEnvStatusDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManEnvStatusDeviceAddress.setStatus("mandatory")
_BattManEnvStatusTemperature_Type = Integer32
_BattManEnvStatusTemperature_Object = MibTableColumn
battManEnvStatusTemperature = _BattManEnvStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 8, 1, 2),
    _BattManEnvStatusTemperature_Type()
)
battManEnvStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManEnvStatusTemperature.setStatus("mandatory")
_BattManEnvStatusHumidity_Type = Integer32
_BattManEnvStatusHumidity_Object = MibTableColumn
battManEnvStatusHumidity = _BattManEnvStatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 8, 1, 3),
    _BattManEnvStatusHumidity_Type()
)
battManEnvStatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManEnvStatusHumidity.setStatus("mandatory")
_BattManEnvStatusDryContact_Type = Integer32
_BattManEnvStatusDryContact_Object = MibTableColumn
battManEnvStatusDryContact = _BattManEnvStatusDryContact_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 8, 1, 4),
    _BattManEnvStatusDryContact_Type()
)
battManEnvStatusDryContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManEnvStatusDryContact.setStatus("mandatory")
_BattManManualMeasTable_Object = MibTable
battManManualMeasTable = _BattManManualMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 9)
)
if mibBuilder.loadTexts:
    battManManualMeasTable.setStatus("mandatory")
_BattManManualMeasEntry_Object = MibTableRow
battManManualMeasEntry = _BattManManualMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 9, 1)
)
battManManualMeasEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManManualMeasDeviceAddress"),
)
if mibBuilder.loadTexts:
    battManManualMeasEntry.setStatus("mandatory")
_BattManManualMeasDeviceAddress_Type = Integer32
_BattManManualMeasDeviceAddress_Object = MibTableColumn
battManManualMeasDeviceAddress = _BattManManualMeasDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 9, 1, 1),
    _BattManManualMeasDeviceAddress_Type()
)
battManManualMeasDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManManualMeasDeviceAddress.setStatus("mandatory")


class _BattManManualMeasStatusText_Type(OctetString):
    """Custom type battManManualMeasStatusText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_BattManManualMeasStatusText_Type.__name__ = "OctetString"
_BattManManualMeasStatusText_Object = MibTableColumn
battManManualMeasStatusText = _BattManManualMeasStatusText_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 9, 1, 2),
    _BattManManualMeasStatusText_Type()
)
battManManualMeasStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManManualMeasStatusText.setStatus("mandatory")
_BattManManualMeasStatusCode_Type = Unsigned32
_BattManManualMeasStatusCode_Object = MibTableColumn
battManManualMeasStatusCode = _BattManManualMeasStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 9, 1, 3),
    _BattManManualMeasStatusCode_Type()
)
battManManualMeasStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManManualMeasStatusCode.setStatus("mandatory")
_BattManManualMeasDatasetID_Type = Unsigned32
_BattManManualMeasDatasetID_Object = MibTableColumn
battManManualMeasDatasetID = _BattManManualMeasDatasetID_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 9, 1, 4),
    _BattManManualMeasDatasetID_Type()
)
battManManualMeasDatasetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManManualMeasDatasetID.setStatus("mandatory")
_BattManManualMeasTimeToMeasurement_Type = Unsigned32
_BattManManualMeasTimeToMeasurement_Object = MibTableColumn
battManManualMeasTimeToMeasurement = _BattManManualMeasTimeToMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 9, 1, 5),
    _BattManManualMeasTimeToMeasurement_Type()
)
battManManualMeasTimeToMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManManualMeasTimeToMeasurement.setStatus("mandatory")


class _BattManManualMeasurementTrigger_Type(Integer32):
    """Custom type battManManualMeasurementTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_BattManManualMeasurementTrigger_Type.__name__ = "Integer32"
_BattManManualMeasurementTrigger_Object = MibTableColumn
battManManualMeasurementTrigger = _BattManManualMeasurementTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 9, 1, 6),
    _BattManManualMeasurementTrigger_Type()
)
battManManualMeasurementTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battManManualMeasurementTrigger.setStatus("current")
_BattManDeviceSettings_ObjectIdentity = ObjectIdentity
battManDeviceSettings = _BattManDeviceSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 10)
)
_BattManDevStringVoltsSetting_Type = Integer32
_BattManDevStringVoltsSetting_Object = MibScalar
battManDevStringVoltsSetting = _BattManDevStringVoltsSetting_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 10, 1),
    _BattManDevStringVoltsSetting_Type()
)
battManDevStringVoltsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battManDevStringVoltsSetting.setStatus("mandatory")
_BattManDevStringCountSetting_Type = Integer32
_BattManDevStringCountSetting_Object = MibScalar
battManDevStringCountSetting = _BattManDevStringCountSetting_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 10, 2),
    _BattManDevStringCountSetting_Type()
)
battManDevStringCountSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battManDevStringCountSetting.setStatus("mandatory")


class _BattManDevDiagnoscticsSetting_Type(Integer32):
    """Custom type battManDevDiagnoscticsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_BattManDevDiagnoscticsSetting_Type.__name__ = "Integer32"
_BattManDevDiagnoscticsSetting_Object = MibScalar
battManDevDiagnoscticsSetting = _BattManDevDiagnoscticsSetting_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 10, 3),
    _BattManDevDiagnoscticsSetting_Type()
)
battManDevDiagnoscticsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battManDevDiagnoscticsSetting.setStatus("current")
_BattManBatteryLogTable_Object = MibTable
battManBatteryLogTable = _BattManBatteryLogTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11)
)
if mibBuilder.loadTexts:
    battManBatteryLogTable.setStatus("mandatory")
_BattManBatteryLogEntry_Object = MibTableRow
battManBatteryLogEntry = _BattManBatteryLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1)
)
battManBatteryLogEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManBattLogDeviceAddress"),
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManBattLogDatasetID"),
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManBattLogStringID"),
    (0, "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB", "battManBattLogBatteryID"),
)
if mibBuilder.loadTexts:
    battManBatteryLogEntry.setStatus("mandatory")
_BattManBattLogDeviceAddress_Type = Integer32
_BattManBattLogDeviceAddress_Object = MibTableColumn
battManBattLogDeviceAddress = _BattManBattLogDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1, 1),
    _BattManBattLogDeviceAddress_Type()
)
battManBattLogDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattLogDeviceAddress.setStatus("mandatory")
_BattManBattLogDatasetID_Type = Unsigned32
_BattManBattLogDatasetID_Object = MibTableColumn
battManBattLogDatasetID = _BattManBattLogDatasetID_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1, 2),
    _BattManBattLogDatasetID_Type()
)
battManBattLogDatasetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattLogDatasetID.setStatus("mandatory")
_BattManBattLogBatteryID_Type = Integer32
_BattManBattLogBatteryID_Object = MibTableColumn
battManBattLogBatteryID = _BattManBattLogBatteryID_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1, 3),
    _BattManBattLogBatteryID_Type()
)
battManBattLogBatteryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattLogBatteryID.setStatus("mandatory")
_BattManBattLogStringID_Type = Integer32
_BattManBattLogStringID_Object = MibTableColumn
battManBattLogStringID = _BattManBattLogStringID_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1, 4),
    _BattManBattLogStringID_Type()
)
battManBattLogStringID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattLogStringID.setStatus("mandatory")
_BattManBattLogVoltage_Type = Integer32
_BattManBattLogVoltage_Object = MibTableColumn
battManBattLogVoltage = _BattManBattLogVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1, 5),
    _BattManBattLogVoltage_Type()
)
battManBattLogVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattLogVoltage.setStatus("mandatory")
_BattManBattLogTemperature_Type = Integer32
_BattManBattLogTemperature_Object = MibTableColumn
battManBattLogTemperature = _BattManBattLogTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1, 6),
    _BattManBattLogTemperature_Type()
)
battManBattLogTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattLogTemperature.setStatus("mandatory")
_BattManBattLogImpedance_Type = HundredthmOhm
_BattManBattLogImpedance_Object = MibTableColumn
battManBattLogImpedance = _BattManBattLogImpedance_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1, 7),
    _BattManBattLogImpedance_Type()
)
battManBattLogImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattLogImpedance.setStatus("mandatory")
_BattManBattLogConductance_Type = HundredthkS
_BattManBattLogConductance_Object = MibTableColumn
battManBattLogConductance = _BattManBattLogConductance_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1, 8),
    _BattManBattLogConductance_Type()
)
battManBattLogConductance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattLogConductance.setStatus("mandatory")
_BattManBattLogTimestamp_Type = DateAndTime
_BattManBattLogTimestamp_Object = MibTableColumn
battManBattLogTimestamp = _BattManBattLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 16, 1, 11, 1, 9),
    _BattManBattLogTimestamp_Type()
)
battManBattLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battManBattLogTimestamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB",
    **{"HundredthmOhm": HundredthmOhm,
       "HundredthkS": HundredthkS,
       "battManIdentMIB": battManIdentMIB,
       "battManIdentObjects": battManIdentObjects,
       "battManMonitored": battManMonitored,
       "battManDeviceTable": battManDeviceTable,
       "battManDeviceEntry": battManDeviceEntry,
       "battManDeviceAddress": battManDeviceAddress,
       "battManProtocolVersion": battManProtocolVersion,
       "battManSoftwareVersion": battManSoftwareVersion,
       "battManDeviceId": battManDeviceId,
       "battManVendorIdentity": battManVendorIdentity,
       "battManStringVoltage": battManStringVoltage,
       "battManBatteries": battManBatteries,
       "battManBatteryStrings": battManBatteryStrings,
       "battManBatteriesPerStrings": battManBatteriesPerStrings,
       "battManVoltageSupport": battManVoltageSupport,
       "battManTemperatureSupport": battManTemperatureSupport,
       "battManImpedanceSupport": battManImpedanceSupport,
       "battManEqualPercentSupport": battManEqualPercentSupport,
       "battManBatteryStatusSupport": battManBatteryStatusSupport,
       "battManDiagSupport": battManDiagSupport,
       "battManEnvDataSupport": battManEnvDataSupport,
       "battManManualMeasurementSupport": battManManualMeasurementSupport,
       "battManStringTable": battManStringTable,
       "battManStringEntry": battManStringEntry,
       "battManStringDeviceAddress": battManStringDeviceAddress,
       "battManString": battManString,
       "battManStringBatteries": battManStringBatteries,
       "battManStringTotalVoltage": battManStringTotalVoltage,
       "battManBatteryTable": battManBatteryTable,
       "battManBatteryEntry": battManBatteryEntry,
       "battManBatteryDeviceAddress": battManBatteryDeviceAddress,
       "battManBattery": battManBattery,
       "battManBatteryStringID": battManBatteryStringID,
       "battManBatteryVersion": battManBatteryVersion,
       "battManBatteryHwVersion": battManBatteryHwVersion,
       "battManBatterySwVersion": battManBatterySwVersion,
       "battManBatteryVoltage": battManBatteryVoltage,
       "battManBatteryTemperature": battManBatteryTemperature,
       "battManBatteryImpedance": battManBatteryImpedance,
       "battManBatteryEqualizationPercent": battManBatteryEqualizationPercent,
       "battManBatteryStatus": battManBatteryStatus,
       "battManBatteryDatasetID": battManBatteryDatasetID,
       "battManBatteryDiagTable": battManBatteryDiagTable,
       "battManBatteryDiagEntry": battManBatteryDiagEntry,
       "battManBatteryDiagDeviceAddress": battManBatteryDiagDeviceAddress,
       "battManBatteryDiagModuleID": battManBatteryDiagModuleID,
       "battManBatteryDiagPageNumber": battManBatteryDiagPageNumber,
       "battManBatteryDiagPageData": battManBatteryDiagPageData,
       "battManControlTable": battManControlTable,
       "battManControlEntry": battManControlEntry,
       "battManControlDeviceAddress": battManControlDeviceAddress,
       "battManControlEqualizationSetting": battManControlEqualizationSetting,
       "battManControlAutoInterval": battManControlAutoInterval,
       "battManControlSensorsRestart": battManControlSensorsRestart,
       "battManStatusTable": battManStatusTable,
       "battManStatusEntry": battManStatusEntry,
       "battManStatusDeviceAddress": battManStatusDeviceAddress,
       "battManStatusTimeToMeasurement": battManStatusTimeToMeasurement,
       "battManEnvStatusTable": battManEnvStatusTable,
       "battManEnvStatusEntry": battManEnvStatusEntry,
       "battManEnvStatusDeviceAddress": battManEnvStatusDeviceAddress,
       "battManEnvStatusTemperature": battManEnvStatusTemperature,
       "battManEnvStatusHumidity": battManEnvStatusHumidity,
       "battManEnvStatusDryContact": battManEnvStatusDryContact,
       "battManManualMeasTable": battManManualMeasTable,
       "battManManualMeasEntry": battManManualMeasEntry,
       "battManManualMeasDeviceAddress": battManManualMeasDeviceAddress,
       "battManManualMeasStatusText": battManManualMeasStatusText,
       "battManManualMeasStatusCode": battManManualMeasStatusCode,
       "battManManualMeasDatasetID": battManManualMeasDatasetID,
       "battManManualMeasTimeToMeasurement": battManManualMeasTimeToMeasurement,
       "battManManualMeasurementTrigger": battManManualMeasurementTrigger,
       "battManDeviceSettings": battManDeviceSettings,
       "battManDevStringVoltsSetting": battManDevStringVoltsSetting,
       "battManDevStringCountSetting": battManDevStringCountSetting,
       "battManDevDiagnoscticsSetting": battManDevDiagnoscticsSetting,
       "battManBatteryLogTable": battManBatteryLogTable,
       "battManBatteryLogEntry": battManBatteryLogEntry,
       "battManBattLogDeviceAddress": battManBattLogDeviceAddress,
       "battManBattLogDatasetID": battManBattLogDatasetID,
       "battManBattLogBatteryID": battManBattLogBatteryID,
       "battManBattLogStringID": battManBattLogStringID,
       "battManBattLogVoltage": battManBattLogVoltage,
       "battManBattLogTemperature": battManBattLogTemperature,
       "battManBattLogImpedance": battManBattLogImpedance,
       "battManBattLogConductance": battManBattLogConductance,
       "battManBattLogTimestamp": battManBattLogTimestamp}
)
