# SNMP MIB module (RUBYTECH-FGS2528KX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rubytech/RUBYTECH-FGS2528KX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:40 2025
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rubytech = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5205)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2)
)
_Fgs2528kxProductId_ObjectIdentity = ObjectIdentity
fgs2528kxProductId = _Fgs2528kxProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77)
)
_Fgs2528kxSystem_ObjectIdentity = ObjectIdentity
fgs2528kxSystem = _Fgs2528kxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1)
)
_Fgs2528kxSystemInformation_ObjectIdentity = ObjectIdentity
fgs2528kxSystemInformation = _Fgs2528kxSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1)
)
_Fgs2528kxModelName_Type = DisplayString
_Fgs2528kxModelName_Object = MibScalar
fgs2528kxModelName = _Fgs2528kxModelName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 1),
    _Fgs2528kxModelName_Type()
)
fgs2528kxModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxModelName.setStatus("current")
_Fgs2528kxBIOSVersion_Type = DisplayString
_Fgs2528kxBIOSVersion_Object = MibScalar
fgs2528kxBIOSVersion = _Fgs2528kxBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 2),
    _Fgs2528kxBIOSVersion_Type()
)
fgs2528kxBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxBIOSVersion.setStatus("current")
_Fgs2528kxFirmwareVersion_Type = DisplayString
_Fgs2528kxFirmwareVersion_Object = MibScalar
fgs2528kxFirmwareVersion = _Fgs2528kxFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 3),
    _Fgs2528kxFirmwareVersion_Type()
)
fgs2528kxFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxFirmwareVersion.setStatus("current")
_Fgs2528kxHardwareMechanicalVersion_Type = DisplayString
_Fgs2528kxHardwareMechanicalVersion_Object = MibScalar
fgs2528kxHardwareMechanicalVersion = _Fgs2528kxHardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 4),
    _Fgs2528kxHardwareMechanicalVersion_Type()
)
fgs2528kxHardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxHardwareMechanicalVersion.setStatus("current")
_Fgs2528kxSeriesNumber_Type = DisplayString
_Fgs2528kxSeriesNumber_Object = MibScalar
fgs2528kxSeriesNumber = _Fgs2528kxSeriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 5),
    _Fgs2528kxSeriesNumber_Type()
)
fgs2528kxSeriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSeriesNumber.setStatus("current")
_Fgs2528kxHostMACAddress_Type = MacAddress
_Fgs2528kxHostMACAddress_Object = MibScalar
fgs2528kxHostMACAddress = _Fgs2528kxHostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 6),
    _Fgs2528kxHostMACAddress_Type()
)
fgs2528kxHostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxHostMACAddress.setStatus("current")
_Fgs2528kxConsoleBaudrate_Type = DisplayString
_Fgs2528kxConsoleBaudrate_Object = MibScalar
fgs2528kxConsoleBaudrate = _Fgs2528kxConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 7),
    _Fgs2528kxConsoleBaudrate_Type()
)
fgs2528kxConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxConsoleBaudrate.setStatus("current")
_Fgs2528kxRAMSize_Type = DisplayString
_Fgs2528kxRAMSize_Object = MibScalar
fgs2528kxRAMSize = _Fgs2528kxRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 8),
    _Fgs2528kxRAMSize_Type()
)
fgs2528kxRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxRAMSize.setStatus("current")
_Fgs2528kxFlashSize_Type = DisplayString
_Fgs2528kxFlashSize_Object = MibScalar
fgs2528kxFlashSize = _Fgs2528kxFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 9),
    _Fgs2528kxFlashSize_Type()
)
fgs2528kxFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxFlashSize.setStatus("current")
_Fgs2528kxBridgeFBDSize_Type = DisplayString
_Fgs2528kxBridgeFBDSize_Object = MibScalar
fgs2528kxBridgeFBDSize = _Fgs2528kxBridgeFBDSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 10),
    _Fgs2528kxBridgeFBDSize_Type()
)
fgs2528kxBridgeFBDSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxBridgeFBDSize.setStatus("current")
_Fgs2528kxTransmitQueue_Type = DisplayString
_Fgs2528kxTransmitQueue_Object = MibScalar
fgs2528kxTransmitQueue = _Fgs2528kxTransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 11),
    _Fgs2528kxTransmitQueue_Type()
)
fgs2528kxTransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxTransmitQueue.setStatus("current")
_Fgs2528kxMaximumFrameSize_Type = DisplayString
_Fgs2528kxMaximumFrameSize_Object = MibScalar
fgs2528kxMaximumFrameSize = _Fgs2528kxMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 12),
    _Fgs2528kxMaximumFrameSize_Type()
)
fgs2528kxMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxMaximumFrameSize.setStatus("current")
_Fgs2528kxCPULoad_Type = DisplayString
_Fgs2528kxCPULoad_Object = MibScalar
fgs2528kxCPULoad = _Fgs2528kxCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 13),
    _Fgs2528kxCPULoad_Type()
)
fgs2528kxCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxCPULoad.setStatus("current")
_Fgs2528kxFanSpeed_Type = DisplayString
_Fgs2528kxFanSpeed_Object = MibScalar
fgs2528kxFanSpeed = _Fgs2528kxFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 14),
    _Fgs2528kxFanSpeed_Type()
)
fgs2528kxFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxFanSpeed.setStatus("current")
_Fgs2528kxPowers_Type = DisplayString
_Fgs2528kxPowers_Object = MibScalar
fgs2528kxPowers = _Fgs2528kxPowers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 15),
    _Fgs2528kxPowers_Type()
)
fgs2528kxPowers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPowers.setStatus("current")
_Fgs2528kxTemperature1_Type = DisplayString
_Fgs2528kxTemperature1_Object = MibScalar
fgs2528kxTemperature1 = _Fgs2528kxTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 16),
    _Fgs2528kxTemperature1_Type()
)
fgs2528kxTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxTemperature1.setStatus("current")
_Fgs2528kxTemperature2_Type = DisplayString
_Fgs2528kxTemperature2_Object = MibScalar
fgs2528kxTemperature2 = _Fgs2528kxTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 17),
    _Fgs2528kxTemperature2_Type()
)
fgs2528kxTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxTemperature2.setStatus("current")
_Fgs2528kxTemperature3_Type = DisplayString
_Fgs2528kxTemperature3_Object = MibScalar
fgs2528kxTemperature3 = _Fgs2528kxTemperature3_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 18),
    _Fgs2528kxTemperature3_Type()
)
fgs2528kxTemperature3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxTemperature3.setStatus("current")
_Fgs2528kxTemperature4_Type = DisplayString
_Fgs2528kxTemperature4_Object = MibScalar
fgs2528kxTemperature4 = _Fgs2528kxTemperature4_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 1, 19),
    _Fgs2528kxTemperature4_Type()
)
fgs2528kxTemperature4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxTemperature4.setStatus("current")
_Fgs2528kxSystemTime_ObjectIdentity = ObjectIdentity
fgs2528kxSystemTime = _Fgs2528kxSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2)
)
_Fgs2528kxSystemTimeManual_ObjectIdentity = ObjectIdentity
fgs2528kxSystemTimeManual = _Fgs2528kxSystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1)
)


class _Fgs2528kxSystemTimeManualClockSource_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSystemTimeManualClockSource_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualClockSource_Object = MibScalar
fgs2528kxSystemTimeManualClockSource = _Fgs2528kxSystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 1),
    _Fgs2528kxSystemTimeManualClockSource_Type()
)
fgs2528kxSystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualClockSource.setStatus("current")
_Fgs2528kxSystemTimeManualLocaltime_Type = DisplayString
_Fgs2528kxSystemTimeManualLocaltime_Object = MibScalar
fgs2528kxSystemTimeManualLocaltime = _Fgs2528kxSystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 2),
    _Fgs2528kxSystemTimeManualLocaltime_Type()
)
fgs2528kxSystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualLocaltime.setStatus("current")


class _Fgs2528kxSystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Fgs2528kxSystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualTimeZoneOffset_Object = MibScalar
fgs2528kxSystemTimeManualTimeZoneOffset = _Fgs2528kxSystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 3),
    _Fgs2528kxSystemTimeManualTimeZoneOffset_Type()
)
fgs2528kxSystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualTimeZoneOffset.setStatus("current")


class _Fgs2528kxSystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualDaylightSavings_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavings = _Fgs2528kxSystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 4),
    _Fgs2528kxSystemTimeManualDaylightSavings_Type()
)
fgs2528kxSystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavings.setStatus("current")


class _Fgs2528kxSystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Fgs2528kxSystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualTimeSetOffset_Object = MibScalar
fgs2528kxSystemTimeManualTimeSetOffset = _Fgs2528kxSystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 5),
    _Fgs2528kxSystemTimeManualTimeSetOffset_Type()
)
fgs2528kxSystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualTimeSetOffset.setStatus("current")


class _Fgs2528kxSystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualDaylightSavingsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualDaylightSavingsType_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsType = _Fgs2528kxSystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 6),
    _Fgs2528kxSystemTimeManualDaylightSavingsType_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsType.setStatus("current")
_Fgs2528kxSystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Fgs2528kxSystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsBydatesFrom = _Fgs2528kxSystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 7),
    _Fgs2528kxSystemTimeManualDaylightSavingsBydatesFrom_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Fgs2528kxSystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Fgs2528kxSystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsBydatesTo = _Fgs2528kxSystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 8),
    _Fgs2528kxSystemTimeManualDaylightSavingsBydatesTo_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom = _Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 9),
    _Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom = _Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 10),
    _Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom = _Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 11),
    _Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeFrom = _Fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 12),
    _Fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo = _Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 13),
    _Fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo = _Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 14),
    _Fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo = _Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 15),
    _Fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeTo = _Fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 1, 16),
    _Fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Fgs2528kxSystemTimeNTP_ObjectIdentity = ObjectIdentity
fgs2528kxSystemTimeNTP = _Fgs2528kxSystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 2)
)
_Fgs2528kxSystemTimeNTPTable_Object = MibTable
fgs2528kxSystemTimeNTPTable = _Fgs2528kxSystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeNTPTable.setStatus("current")
_Fgs2528kxSystemTimeNTPEntry_Object = MibTableRow
fgs2528kxSystemTimeNTPEntry = _Fgs2528kxSystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 2, 1, 1)
)
fgs2528kxSystemTimeNTPEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxSystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeNTPEntry.setStatus("current")


class _Fgs2528kxSystemTimeNTPIndex_Type(Integer32):
    """Custom type fgs2528kxSystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Fgs2528kxSystemTimeNTPIndex_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeNTPIndex_Object = MibTableColumn
fgs2528kxSystemTimeNTPIndex = _Fgs2528kxSystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 2, 1, 1, 1),
    _Fgs2528kxSystemTimeNTPIndex_Type()
)
fgs2528kxSystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeNTPIndex.setStatus("current")


class _Fgs2528kxSystemTimeNTPServerIPType_Type(Integer32):
    """Custom type fgs2528kxSystemTimeNTPServerIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeNTPServerIPType_Object = MibTableColumn
fgs2528kxSystemTimeNTPServerIPType = _Fgs2528kxSystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 2, 1, 1, 2),
    _Fgs2528kxSystemTimeNTPServerIPType_Type()
)
fgs2528kxSystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeNTPServerIPType.setStatus("current")
_Fgs2528kxSystemTimeNTPServer_Type = DisplayString
_Fgs2528kxSystemTimeNTPServer_Object = MibTableColumn
fgs2528kxSystemTimeNTPServer = _Fgs2528kxSystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 2, 1, 1, 3),
    _Fgs2528kxSystemTimeNTPServer_Type()
)
fgs2528kxSystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeNTPServer.setStatus("current")


class _Fgs2528kxSystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type fgs2528kxSystemTimeNTPCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxSystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Fgs2528kxSystemTimeNTPCurrentMode_Object = MibTableColumn
fgs2528kxSystemTimeNTPCurrentMode = _Fgs2528kxSystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 2, 2, 1, 1, 4),
    _Fgs2528kxSystemTimeNTPCurrentMode_Type()
)
fgs2528kxSystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemTimeNTPCurrentMode.setStatus("current")
_Fgs2528kxSystemAccount_ObjectIdentity = ObjectIdentity
fgs2528kxSystemAccount = _Fgs2528kxSystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3)
)
_Fgs2528kxSystemAccountUsers_ObjectIdentity = ObjectIdentity
fgs2528kxSystemAccountUsers = _Fgs2528kxSystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 1)
)


class _Fgs2528kxSystemAccountUserCreate_Type(Integer32):
    """Custom type fgs2528kxSystemAccountUserCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSystemAccountUserCreate_Type.__name__ = "Integer32"
_Fgs2528kxSystemAccountUserCreate_Object = MibScalar
fgs2528kxSystemAccountUserCreate = _Fgs2528kxSystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 1, 1),
    _Fgs2528kxSystemAccountUserCreate_Type()
)
fgs2528kxSystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemAccountUserCreate.setStatus("current")
_Fgs2528kxSystemAccountUsersTable_Object = MibTable
fgs2528kxSystemAccountUsersTable = _Fgs2528kxSystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxSystemAccountUsersTable.setStatus("current")
_Fgs2528kxSystemAccountUsersEntry_Object = MibTableRow
fgs2528kxSystemAccountUsersEntry = _Fgs2528kxSystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 1, 2, 1)
)
fgs2528kxSystemAccountUsersEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxUserIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxSystemAccountUsersEntry.setStatus("current")


class _Fgs2528kxUserIndex_Type(Integer32):
    """Custom type fgs2528kxUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Fgs2528kxUserIndex_Type.__name__ = "Integer32"
_Fgs2528kxUserIndex_Object = MibTableColumn
fgs2528kxUserIndex = _Fgs2528kxUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 1, 2, 1, 1),
    _Fgs2528kxUserIndex_Type()
)
fgs2528kxUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxUserIndex.setStatus("current")


class _Fgs2528kxUserName_Type(DisplayString):
    """Custom type fgs2528kxUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Fgs2528kxUserName_Type.__name__ = "DisplayString"
_Fgs2528kxUserName_Object = MibTableColumn
fgs2528kxUserName = _Fgs2528kxUserName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 1, 2, 1, 2),
    _Fgs2528kxUserName_Type()
)
fgs2528kxUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxUserName.setStatus("current")


class _Fgs2528kxPassword_Type(DisplayString):
    """Custom type fgs2528kxPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Fgs2528kxPassword_Type.__name__ = "DisplayString"
_Fgs2528kxPassword_Object = MibTableColumn
fgs2528kxPassword = _Fgs2528kxPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 1, 2, 1, 3),
    _Fgs2528kxPassword_Type()
)
fgs2528kxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPassword.setStatus("current")


class _Fgs2528kxUserPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxUserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxUserPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxUserPrivilegeLevel_Object = MibTableColumn
fgs2528kxUserPrivilegeLevel = _Fgs2528kxUserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 1, 2, 1, 4),
    _Fgs2528kxUserPrivilegeLevel_Type()
)
fgs2528kxUserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxUserPrivilegeLevel.setStatus("current")


class _Fgs2528kxAccountUserRowStatus_Type(Integer32):
    """Custom type fgs2528kxAccountUserRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Fgs2528kxAccountUserRowStatus_Type.__name__ = "Integer32"
_Fgs2528kxAccountUserRowStatus_Object = MibTableColumn
fgs2528kxAccountUserRowStatus = _Fgs2528kxAccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 1, 2, 1, 5),
    _Fgs2528kxAccountUserRowStatus_Type()
)
fgs2528kxAccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccountUserRowStatus.setStatus("current")
_Fgs2528kxSystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
fgs2528kxSystemAccountPrivilegeLevel = _Fgs2528kxSystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2)
)


class _Fgs2528kxAccountPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxAccountPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxAccountPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxAccountPrivilegeLevel_Object = MibScalar
fgs2528kxAccountPrivilegeLevel = _Fgs2528kxAccountPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 1),
    _Fgs2528kxAccountPrivilegeLevel_Type()
)
fgs2528kxAccountPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccountPrivilegeLevel.setStatus("current")


class _Fgs2528kxAggregationPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxAggregationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxAggregationPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxAggregationPrivilegeLevel_Object = MibScalar
fgs2528kxAggregationPrivilegeLevel = _Fgs2528kxAggregationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 2),
    _Fgs2528kxAggregationPrivilegeLevel_Type()
)
fgs2528kxAggregationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAggregationPrivilegeLevel.setStatus("current")


class _Fgs2528kxDiagnosticsPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxDiagnosticsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxDiagnosticsPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxDiagnosticsPrivilegeLevel_Object = MibScalar
fgs2528kxDiagnosticsPrivilegeLevel = _Fgs2528kxDiagnosticsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 3),
    _Fgs2528kxDiagnosticsPrivilegeLevel_Type()
)
fgs2528kxDiagnosticsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDiagnosticsPrivilegeLevel.setStatus("current")


class _Fgs2528kxEPSPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxEPSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxEPSPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxEPSPrivilegeLevel_Object = MibScalar
fgs2528kxEPSPrivilegeLevel = _Fgs2528kxEPSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 5),
    _Fgs2528kxEPSPrivilegeLevel_Type()
)
fgs2528kxEPSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxEPSPrivilegeLevel.setStatus("current")


class _Fgs2528kxERPSPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxERPSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxERPSPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxERPSPrivilegeLevel_Object = MibScalar
fgs2528kxERPSPrivilegeLevel = _Fgs2528kxERPSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 6),
    _Fgs2528kxERPSPrivilegeLevel_Type()
)
fgs2528kxERPSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSPrivilegeLevel.setStatus("current")


class _Fgs2528kxETHLinkOAMPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxETHLinkOAMPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxETHLinkOAMPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxETHLinkOAMPrivilegeLevel_Object = MibScalar
fgs2528kxETHLinkOAMPrivilegeLevel = _Fgs2528kxETHLinkOAMPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 7),
    _Fgs2528kxETHLinkOAMPrivilegeLevel_Type()
)
fgs2528kxETHLinkOAMPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxETHLinkOAMPrivilegeLevel.setStatus("current")


class _Fgs2528kxEVCPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxEVCPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxEVCPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxEVCPrivilegeLevel_Object = MibScalar
fgs2528kxEVCPrivilegeLevel = _Fgs2528kxEVCPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 8),
    _Fgs2528kxEVCPrivilegeLevel_Type()
)
fgs2528kxEVCPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxEVCPrivilegeLevel.setStatus("current")


class _Fgs2528kxGARPPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxGARPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxGARPPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxGARPPrivilegeLevel_Object = MibScalar
fgs2528kxGARPPrivilegeLevel = _Fgs2528kxGARPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 10),
    _Fgs2528kxGARPPrivilegeLevel_Type()
)
fgs2528kxGARPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGARPPrivilegeLevel.setStatus("current")


class _Fgs2528kxGVRPPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxGVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxGVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxGVRPPrivilegeLevel_Object = MibScalar
fgs2528kxGVRPPrivilegeLevel = _Fgs2528kxGVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 11),
    _Fgs2528kxGVRPPrivilegeLevel_Type()
)
fgs2528kxGVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGVRPPrivilegeLevel.setStatus("current")


class _Fgs2528kxIPPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxIPPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxIPPrivilegeLevel_Object = MibScalar
fgs2528kxIPPrivilegeLevel = _Fgs2528kxIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 12),
    _Fgs2528kxIPPrivilegeLevel_Type()
)
fgs2528kxIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPPrivilegeLevel.setStatus("current")


class _Fgs2528kxIPMCSnoopingPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxIPMCSnoopingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxIPMCSnoopingPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxIPMCSnoopingPrivilegeLevel_Object = MibScalar
fgs2528kxIPMCSnoopingPrivilegeLevel = _Fgs2528kxIPMCSnoopingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 13),
    _Fgs2528kxIPMCSnoopingPrivilegeLevel_Type()
)
fgs2528kxIPMCSnoopingPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPMCSnoopingPrivilegeLevel.setStatus("current")


class _Fgs2528kxLACPPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxLACPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxLACPPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxLACPPrivilegeLevel_Object = MibScalar
fgs2528kxLACPPrivilegeLevel = _Fgs2528kxLACPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 14),
    _Fgs2528kxLACPPrivilegeLevel_Type()
)
fgs2528kxLACPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxLACPPrivilegeLevel.setStatus("current")


class _Fgs2528kxLLDPPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxLLDPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxLLDPPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxLLDPPrivilegeLevel_Object = MibScalar
fgs2528kxLLDPPrivilegeLevel = _Fgs2528kxLLDPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 15),
    _Fgs2528kxLLDPPrivilegeLevel_Type()
)
fgs2528kxLLDPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxLLDPPrivilegeLevel.setStatus("current")


class _Fgs2528kxLLDPMEDPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxLLDPMEDPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxLLDPMEDPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxLLDPMEDPrivilegeLevel_Object = MibScalar
fgs2528kxLLDPMEDPrivilegeLevel = _Fgs2528kxLLDPMEDPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 16),
    _Fgs2528kxLLDPMEDPrivilegeLevel_Type()
)
fgs2528kxLLDPMEDPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxLLDPMEDPrivilegeLevel.setStatus("current")


class _Fgs2528kxLoopProtectPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxLoopProtectPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxLoopProtectPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxLoopProtectPrivilegeLevel_Object = MibScalar
fgs2528kxLoopProtectPrivilegeLevel = _Fgs2528kxLoopProtectPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 17),
    _Fgs2528kxLoopProtectPrivilegeLevel_Type()
)
fgs2528kxLoopProtectPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxLoopProtectPrivilegeLevel.setStatus("current")


class _Fgs2528kxMACTablePrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxMACTablePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxMACTablePrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxMACTablePrivilegeLevel_Object = MibScalar
fgs2528kxMACTablePrivilegeLevel = _Fgs2528kxMACTablePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 18),
    _Fgs2528kxMACTablePrivilegeLevel_Type()
)
fgs2528kxMACTablePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxMACTablePrivilegeLevel.setStatus("current")


class _Fgs2528kxMEPPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxMEPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxMEPPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxMEPPrivilegeLevel_Object = MibScalar
fgs2528kxMEPPrivilegeLevel = _Fgs2528kxMEPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 20),
    _Fgs2528kxMEPPrivilegeLevel_Type()
)
fgs2528kxMEPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxMEPPrivilegeLevel.setStatus("current")


class _Fgs2528kxMVRPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxMVRPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxMVRPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxMVRPrivilegeLevel_Object = MibScalar
fgs2528kxMVRPrivilegeLevel = _Fgs2528kxMVRPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 22),
    _Fgs2528kxMVRPrivilegeLevel_Type()
)
fgs2528kxMVRPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxMVRPrivilegeLevel.setStatus("current")


class _Fgs2528kxMaintenancePrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxMaintenancePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxMaintenancePrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxMaintenancePrivilegeLevel_Object = MibScalar
fgs2528kxMaintenancePrivilegeLevel = _Fgs2528kxMaintenancePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 24),
    _Fgs2528kxMaintenancePrivilegeLevel_Type()
)
fgs2528kxMaintenancePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxMaintenancePrivilegeLevel.setStatus("current")


class _Fgs2528kxMirroringPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxMirroringPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxMirroringPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxMirroringPrivilegeLevel_Object = MibScalar
fgs2528kxMirroringPrivilegeLevel = _Fgs2528kxMirroringPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 25),
    _Fgs2528kxMirroringPrivilegeLevel_Type()
)
fgs2528kxMirroringPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxMirroringPrivilegeLevel.setStatus("current")


class _Fgs2528kxPTPPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxPTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxPTPPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxPTPPrivilegeLevel_Object = MibScalar
fgs2528kxPTPPrivilegeLevel = _Fgs2528kxPTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 26),
    _Fgs2528kxPTPPrivilegeLevel_Type()
)
fgs2528kxPTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPTPPrivilegeLevel.setStatus("current")


class _Fgs2528kxPortsPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxPortsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxPortsPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxPortsPrivilegeLevel_Object = MibScalar
fgs2528kxPortsPrivilegeLevel = _Fgs2528kxPortsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 27),
    _Fgs2528kxPortsPrivilegeLevel_Type()
)
fgs2528kxPortsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortsPrivilegeLevel.setStatus("current")


class _Fgs2528kxPrivateVLANsPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxPrivateVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxPrivateVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxPrivateVLANsPrivilegeLevel_Object = MibScalar
fgs2528kxPrivateVLANsPrivilegeLevel = _Fgs2528kxPrivateVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 28),
    _Fgs2528kxPrivateVLANsPrivilegeLevel_Type()
)
fgs2528kxPrivateVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPrivateVLANsPrivilegeLevel.setStatus("current")


class _Fgs2528kxQoSPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxQoSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxQoSPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxQoSPrivilegeLevel_Object = MibScalar
fgs2528kxQoSPrivilegeLevel = _Fgs2528kxQoSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 29),
    _Fgs2528kxQoSPrivilegeLevel_Type()
)
fgs2528kxQoSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxQoSPrivilegeLevel.setStatus("current")


class _Fgs2528kxSMTPPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxSMTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxSMTPPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxSMTPPrivilegeLevel_Object = MibScalar
fgs2528kxSMTPPrivilegeLevel = _Fgs2528kxSMTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 31),
    _Fgs2528kxSMTPPrivilegeLevel_Type()
)
fgs2528kxSMTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPPrivilegeLevel.setStatus("current")


class _Fgs2528kxSNMPPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxSNMPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxSNMPPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxSNMPPrivilegeLevel_Object = MibScalar
fgs2528kxSNMPPrivilegeLevel = _Fgs2528kxSNMPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 32),
    _Fgs2528kxSNMPPrivilegeLevel_Type()
)
fgs2528kxSNMPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSNMPPrivilegeLevel.setStatus("current")


class _Fgs2528kxSecurityPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxSecurityPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxSecurityPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxSecurityPrivilegeLevel_Object = MibScalar
fgs2528kxSecurityPrivilegeLevel = _Fgs2528kxSecurityPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 33),
    _Fgs2528kxSecurityPrivilegeLevel_Type()
)
fgs2528kxSecurityPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSecurityPrivilegeLevel.setStatus("current")


class _Fgs2528kxSpanningTreePrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxSpanningTreePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxSpanningTreePrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxSpanningTreePrivilegeLevel_Object = MibScalar
fgs2528kxSpanningTreePrivilegeLevel = _Fgs2528kxSpanningTreePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 35),
    _Fgs2528kxSpanningTreePrivilegeLevel_Type()
)
fgs2528kxSpanningTreePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSpanningTreePrivilegeLevel.setStatus("current")


class _Fgs2528kxSystemPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxSystemPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxSystemPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxSystemPrivilegeLevel_Object = MibScalar
fgs2528kxSystemPrivilegeLevel = _Fgs2528kxSystemPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 36),
    _Fgs2528kxSystemPrivilegeLevel_Type()
)
fgs2528kxSystemPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSystemPrivilegeLevel.setStatus("current")


class _Fgs2528kxTrapEventPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxTrapEventPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxTrapEventPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventPrivilegeLevel_Object = MibScalar
fgs2528kxTrapEventPrivilegeLevel = _Fgs2528kxTrapEventPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 37),
    _Fgs2528kxTrapEventPrivilegeLevel_Type()
)
fgs2528kxTrapEventPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventPrivilegeLevel.setStatus("current")


class _Fgs2528kxVCLPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxVCLPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxVCLPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxVCLPrivilegeLevel_Object = MibScalar
fgs2528kxVCLPrivilegeLevel = _Fgs2528kxVCLPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 39),
    _Fgs2528kxVCLPrivilegeLevel_Type()
)
fgs2528kxVCLPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxVCLPrivilegeLevel.setStatus("current")


class _Fgs2528kxVLANTranslationPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxVLANTranslationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxVLANTranslationPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxVLANTranslationPrivilegeLevel_Object = MibScalar
fgs2528kxVLANTranslationPrivilegeLevel = _Fgs2528kxVLANTranslationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 40),
    _Fgs2528kxVLANTranslationPrivilegeLevel_Type()
)
fgs2528kxVLANTranslationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxVLANTranslationPrivilegeLevel.setStatus("current")


class _Fgs2528kxVLANsPrivilegeLevel_Type(Integer32):
    """Custom type fgs2528kxVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Fgs2528kxVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Fgs2528kxVLANsPrivilegeLevel_Object = MibScalar
fgs2528kxVLANsPrivilegeLevel = _Fgs2528kxVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 3, 2, 41),
    _Fgs2528kxVLANsPrivilegeLevel_Type()
)
fgs2528kxVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxVLANsPrivilegeLevel.setStatus("current")
_Fgs2528kxIP_ObjectIdentity = ObjectIdentity
fgs2528kxIP = _Fgs2528kxIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4)
)
_Fgs2528kxIPv4_ObjectIdentity = ObjectIdentity
fgs2528kxIPv4 = _Fgs2528kxIPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1)
)
_Fgs2528kxIPv4Configured_ObjectIdentity = ObjectIdentity
fgs2528kxIPv4Configured = _Fgs2528kxIPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 1)
)


class _Fgs2528kxIpv4DHCPClient_Type(Integer32):
    """Custom type fgs2528kxIpv4DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxIpv4DHCPClient_Type.__name__ = "Integer32"
_Fgs2528kxIpv4DHCPClient_Object = MibScalar
fgs2528kxIpv4DHCPClient = _Fgs2528kxIpv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 1, 1),
    _Fgs2528kxIpv4DHCPClient_Type()
)
fgs2528kxIpv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIpv4DHCPClient.setStatus("current")
_Fgs2528kxIPv4Address_Type = IpAddress
_Fgs2528kxIPv4Address_Object = MibScalar
fgs2528kxIPv4Address = _Fgs2528kxIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 1, 2),
    _Fgs2528kxIPv4Address_Type()
)
fgs2528kxIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPv4Address.setStatus("current")
_Fgs2528kxIPv4Mask_Type = IpAddress
_Fgs2528kxIPv4Mask_Object = MibScalar
fgs2528kxIPv4Mask = _Fgs2528kxIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 1, 3),
    _Fgs2528kxIPv4Mask_Type()
)
fgs2528kxIPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPv4Mask.setStatus("current")
_Fgs2528kxIPv4Router_Type = IpAddress
_Fgs2528kxIPv4Router_Object = MibScalar
fgs2528kxIPv4Router = _Fgs2528kxIPv4Router_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 1, 4),
    _Fgs2528kxIPv4Router_Type()
)
fgs2528kxIPv4Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPv4Router.setStatus("current")


class _Fgs2528kxIPv4VLANId_Type(Integer32):
    """Custom type fgs2528kxIPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Fgs2528kxIPv4VLANId_Type.__name__ = "Integer32"
_Fgs2528kxIPv4VLANId_Object = MibScalar
fgs2528kxIPv4VLANId = _Fgs2528kxIPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 1, 5),
    _Fgs2528kxIPv4VLANId_Type()
)
fgs2528kxIPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPv4VLANId.setStatus("current")
_Fgs2528kxIPv4DNSServer_Type = IpAddress
_Fgs2528kxIPv4DNSServer_Object = MibScalar
fgs2528kxIPv4DNSServer = _Fgs2528kxIPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 1, 6),
    _Fgs2528kxIPv4DNSServer_Type()
)
fgs2528kxIPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPv4DNSServer.setStatus("current")


class _Fgs2528kxIPv4DNSProxy_Type(Integer32):
    """Custom type fgs2528kxIPv4DNSProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxIPv4DNSProxy_Type.__name__ = "Integer32"
_Fgs2528kxIPv4DNSProxy_Object = MibScalar
fgs2528kxIPv4DNSProxy = _Fgs2528kxIPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 1, 7),
    _Fgs2528kxIPv4DNSProxy_Type()
)
fgs2528kxIPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPv4DNSProxy.setStatus("current")
_Fgs2528kxIPv4Current_ObjectIdentity = ObjectIdentity
fgs2528kxIPv4Current = _Fgs2528kxIPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 2)
)


class _Fgs2528kxIpv4CurrentDHCPClient_Type(Integer32):
    """Custom type fgs2528kxIpv4CurrentDHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxIpv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Fgs2528kxIpv4CurrentDHCPClient_Object = MibScalar
fgs2528kxIpv4CurrentDHCPClient = _Fgs2528kxIpv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 2, 1),
    _Fgs2528kxIpv4CurrentDHCPClient_Type()
)
fgs2528kxIpv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIpv4CurrentDHCPClient.setStatus("current")
_Fgs2528kxIPv4CurrentAddress_Type = IpAddress
_Fgs2528kxIPv4CurrentAddress_Object = MibScalar
fgs2528kxIPv4CurrentAddress = _Fgs2528kxIPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 2, 2),
    _Fgs2528kxIPv4CurrentAddress_Type()
)
fgs2528kxIPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIPv4CurrentAddress.setStatus("current")
_Fgs2528kxIPv4CurrentMask_Type = IpAddress
_Fgs2528kxIPv4CurrentMask_Object = MibScalar
fgs2528kxIPv4CurrentMask = _Fgs2528kxIPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 2, 3),
    _Fgs2528kxIPv4CurrentMask_Type()
)
fgs2528kxIPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIPv4CurrentMask.setStatus("current")
_Fgs2528kxIPv4CurrentRouter_Type = IpAddress
_Fgs2528kxIPv4CurrentRouter_Object = MibScalar
fgs2528kxIPv4CurrentRouter = _Fgs2528kxIPv4CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 2, 4),
    _Fgs2528kxIPv4CurrentRouter_Type()
)
fgs2528kxIPv4CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIPv4CurrentRouter.setStatus("current")


class _Fgs2528kxIPv4CurrentVLANId_Type(Integer32):
    """Custom type fgs2528kxIPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Fgs2528kxIPv4CurrentVLANId_Type.__name__ = "Integer32"
_Fgs2528kxIPv4CurrentVLANId_Object = MibScalar
fgs2528kxIPv4CurrentVLANId = _Fgs2528kxIPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 2, 5),
    _Fgs2528kxIPv4CurrentVLANId_Type()
)
fgs2528kxIPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIPv4CurrentVLANId.setStatus("current")
_Fgs2528kxIPv4CurrentDNSServer_Type = IpAddress
_Fgs2528kxIPv4CurrentDNSServer_Object = MibScalar
fgs2528kxIPv4CurrentDNSServer = _Fgs2528kxIPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 1, 2, 6),
    _Fgs2528kxIPv4CurrentDNSServer_Type()
)
fgs2528kxIPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIPv4CurrentDNSServer.setStatus("current")
_Fgs2528kxIPv6_ObjectIdentity = ObjectIdentity
fgs2528kxIPv6 = _Fgs2528kxIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2)
)
_Fgs2528kxIPv6Configured_ObjectIdentity = ObjectIdentity
fgs2528kxIPv6Configured = _Fgs2528kxIPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 1)
)


class _Fgs2528kxIpv6AutoConfiguration_Type(Integer32):
    """Custom type fgs2528kxIpv6AutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxIpv6AutoConfiguration_Type.__name__ = "Integer32"
_Fgs2528kxIpv6AutoConfiguration_Object = MibScalar
fgs2528kxIpv6AutoConfiguration = _Fgs2528kxIpv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 1, 1),
    _Fgs2528kxIpv6AutoConfiguration_Type()
)
fgs2528kxIpv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIpv6AutoConfiguration.setStatus("current")


class _Fgs2528kxIpv6Address_Type(DisplayString):
    """Custom type fgs2528kxIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Fgs2528kxIpv6Address_Type.__name__ = "DisplayString"
_Fgs2528kxIpv6Address_Object = MibScalar
fgs2528kxIpv6Address = _Fgs2528kxIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 1, 2),
    _Fgs2528kxIpv6Address_Type()
)
fgs2528kxIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIpv6Address.setStatus("current")


class _Fgs2528kxIpv6Prefix_Type(Integer32):
    """Custom type fgs2528kxIpv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Fgs2528kxIpv6Prefix_Type.__name__ = "Integer32"
_Fgs2528kxIpv6Prefix_Object = MibScalar
fgs2528kxIpv6Prefix = _Fgs2528kxIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 1, 3),
    _Fgs2528kxIpv6Prefix_Type()
)
fgs2528kxIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIpv6Prefix.setStatus("current")


class _Fgs2528kxIpv6Router_Type(DisplayString):
    """Custom type fgs2528kxIpv6Router based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Fgs2528kxIpv6Router_Type.__name__ = "DisplayString"
_Fgs2528kxIpv6Router_Object = MibScalar
fgs2528kxIpv6Router = _Fgs2528kxIpv6Router_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 1, 4),
    _Fgs2528kxIpv6Router_Type()
)
fgs2528kxIpv6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIpv6Router.setStatus("current")
_Fgs2528kxIPv6Current_ObjectIdentity = ObjectIdentity
fgs2528kxIPv6Current = _Fgs2528kxIPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 2)
)


class _Fgs2528kxIpv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type fgs2528kxIpv6CurrentAutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxIpv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Fgs2528kxIpv6CurrentAutoConfiguration_Object = MibScalar
fgs2528kxIpv6CurrentAutoConfiguration = _Fgs2528kxIpv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 2, 1),
    _Fgs2528kxIpv6CurrentAutoConfiguration_Type()
)
fgs2528kxIpv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIpv6CurrentAutoConfiguration.setStatus("current")


class _Fgs2528kxIpv6CurrentAddress_Type(DisplayString):
    """Custom type fgs2528kxIpv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Fgs2528kxIpv6CurrentAddress_Type.__name__ = "DisplayString"
_Fgs2528kxIpv6CurrentAddress_Object = MibScalar
fgs2528kxIpv6CurrentAddress = _Fgs2528kxIpv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 2, 2),
    _Fgs2528kxIpv6CurrentAddress_Type()
)
fgs2528kxIpv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIpv6CurrentAddress.setStatus("current")


class _Fgs2528kxIpv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type fgs2528kxIpv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Fgs2528kxIpv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Fgs2528kxIpv6CurrentLinkLocalAddress_Object = MibScalar
fgs2528kxIpv6CurrentLinkLocalAddress = _Fgs2528kxIpv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 2, 3),
    _Fgs2528kxIpv6CurrentLinkLocalAddress_Type()
)
fgs2528kxIpv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIpv6CurrentLinkLocalAddress.setStatus("current")


class _Fgs2528kxIpv6CurrentPrefix_Type(Integer32):
    """Custom type fgs2528kxIpv6CurrentPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Fgs2528kxIpv6CurrentPrefix_Type.__name__ = "Integer32"
_Fgs2528kxIpv6CurrentPrefix_Object = MibScalar
fgs2528kxIpv6CurrentPrefix = _Fgs2528kxIpv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 2, 4),
    _Fgs2528kxIpv6CurrentPrefix_Type()
)
fgs2528kxIpv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIpv6CurrentPrefix.setStatus("current")


class _Fgs2528kxIpv6CurrentRouter_Type(DisplayString):
    """Custom type fgs2528kxIpv6CurrentRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Fgs2528kxIpv6CurrentRouter_Type.__name__ = "DisplayString"
_Fgs2528kxIpv6CurrentRouter_Object = MibScalar
fgs2528kxIpv6CurrentRouter = _Fgs2528kxIpv6CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 4, 2, 2, 5),
    _Fgs2528kxIpv6CurrentRouter_Type()
)
fgs2528kxIpv6CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIpv6CurrentRouter.setStatus("current")
_Fgs2528kxSyslog_ObjectIdentity = ObjectIdentity
fgs2528kxSyslog = _Fgs2528kxSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5)
)
_Fgs2528kxSyslogConf_ObjectIdentity = ObjectIdentity
fgs2528kxSyslogConf = _Fgs2528kxSyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 1)
)


class _Fgs2528kxServerMode_Type(Integer32):
    """Custom type fgs2528kxServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxServerMode_Type.__name__ = "Integer32"
_Fgs2528kxServerMode_Object = MibScalar
fgs2528kxServerMode = _Fgs2528kxServerMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 1, 1),
    _Fgs2528kxServerMode_Type()
)
fgs2528kxServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxServerMode.setStatus("current")
_Fgs2528kxServerAddress1_Type = IpAddress
_Fgs2528kxServerAddress1_Object = MibScalar
fgs2528kxServerAddress1 = _Fgs2528kxServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 1, 2),
    _Fgs2528kxServerAddress1_Type()
)
fgs2528kxServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxServerAddress1.setStatus("current")
_Fgs2528kxServerAddress2_Type = IpAddress
_Fgs2528kxServerAddress2_Object = MibScalar
fgs2528kxServerAddress2 = _Fgs2528kxServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 1, 3),
    _Fgs2528kxServerAddress2_Type()
)
fgs2528kxServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxServerAddress2.setStatus("current")


class _Fgs2528kxSyslogLevel_Type(Integer32):
    """Custom type fgs2528kxSyslogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxSyslogLevel_Type.__name__ = "Integer32"
_Fgs2528kxSyslogLevel_Object = MibScalar
fgs2528kxSyslogLevel = _Fgs2528kxSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 1, 4),
    _Fgs2528kxSyslogLevel_Type()
)
fgs2528kxSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSyslogLevel.setStatus("current")
_Fgs2528kxSyslogDetailedInfo_ObjectIdentity = ObjectIdentity
fgs2528kxSyslogDetailedInfo = _Fgs2528kxSyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 2)
)


class _Fgs2528kxSyslogDetailedInfoClear_Type(Integer32):
    """Custom type fgs2528kxSyslogDetailedInfoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Fgs2528kxSyslogDetailedInfoClear_Object = MibScalar
fgs2528kxSyslogDetailedInfoClear = _Fgs2528kxSyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 2, 1),
    _Fgs2528kxSyslogDetailedInfoClear_Type()
)
fgs2528kxSyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSyslogDetailedInfoClear.setStatus("current")
_Fgs2528kxSyslogDetailedInfoTable_Object = MibTable
fgs2528kxSyslogDetailedInfoTable = _Fgs2528kxSyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxSyslogDetailedInfoTable.setStatus("current")
_Fgs2528kxSyslogDetailedInfoEntry_Object = MibTableRow
fgs2528kxSyslogDetailedInfoEntry = _Fgs2528kxSyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 2, 2, 1)
)
fgs2528kxSyslogDetailedInfoEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxSyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxSyslogDetailedInfoEntry.setStatus("current")


class _Fgs2528kxSyslogDetailedInfoIndex_Type(Integer32):
    """Custom type fgs2528kxSyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Fgs2528kxSyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Fgs2528kxSyslogDetailedInfoIndex_Object = MibTableColumn
fgs2528kxSyslogDetailedInfoIndex = _Fgs2528kxSyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 2, 2, 1, 1),
    _Fgs2528kxSyslogDetailedInfoIndex_Type()
)
fgs2528kxSyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxSyslogDetailedInfoIndex.setStatus("current")
_Fgs2528kxSyslogDetailedInfoLevel_Type = DisplayString
_Fgs2528kxSyslogDetailedInfoLevel_Object = MibTableColumn
fgs2528kxSyslogDetailedInfoLevel = _Fgs2528kxSyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 2, 2, 1, 2),
    _Fgs2528kxSyslogDetailedInfoLevel_Type()
)
fgs2528kxSyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSyslogDetailedInfoLevel.setStatus("current")


class _Fgs2528kxSyslogDetailedInfoTime_Type(DisplayString):
    """Custom type fgs2528kxSyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Fgs2528kxSyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Fgs2528kxSyslogDetailedInfoTime_Object = MibTableColumn
fgs2528kxSyslogDetailedInfoTime = _Fgs2528kxSyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 2, 2, 1, 3),
    _Fgs2528kxSyslogDetailedInfoTime_Type()
)
fgs2528kxSyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSyslogDetailedInfoTime.setStatus("current")
_Fgs2528kxSyslogDetailedInfoMessage_Type = DisplayString
_Fgs2528kxSyslogDetailedInfoMessage_Object = MibTableColumn
fgs2528kxSyslogDetailedInfoMessage = _Fgs2528kxSyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 5, 2, 2, 1, 4),
    _Fgs2528kxSyslogDetailedInfoMessage_Type()
)
fgs2528kxSyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSyslogDetailedInfoMessage.setStatus("current")
_Fgs2528kxSnmp_ObjectIdentity = ObjectIdentity
fgs2528kxSnmp = _Fgs2528kxSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6)
)
_Fgs2528kxSnmpConf_ObjectIdentity = ObjectIdentity
fgs2528kxSnmpConf = _Fgs2528kxSnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1)
)
_Fgs2528kxGetCommunity_Type = DisplayString
_Fgs2528kxGetCommunity_Object = MibScalar
fgs2528kxGetCommunity = _Fgs2528kxGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 1),
    _Fgs2528kxGetCommunity_Type()
)
fgs2528kxGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGetCommunity.setStatus("current")


class _Fgs2528kxSetCommunityMode_Type(Integer32):
    """Custom type fgs2528kxSetCommunityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSetCommunityMode_Type.__name__ = "Integer32"
_Fgs2528kxSetCommunityMode_Object = MibScalar
fgs2528kxSetCommunityMode = _Fgs2528kxSetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 2),
    _Fgs2528kxSetCommunityMode_Type()
)
fgs2528kxSetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSetCommunityMode.setStatus("current")
_Fgs2528kxSetCommunity_Type = DisplayString
_Fgs2528kxSetCommunity_Object = MibScalar
fgs2528kxSetCommunity = _Fgs2528kxSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 3),
    _Fgs2528kxSetCommunity_Type()
)
fgs2528kxSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSetCommunity.setStatus("current")
_Fgs2528kxTrapHostConfTable_Object = MibTable
fgs2528kxTrapHostConfTable = _Fgs2528kxTrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfTable.setStatus("current")
_Fgs2528kxTrapHostConfEntry_Object = MibTableRow
fgs2528kxTrapHostConfEntry = _Fgs2528kxTrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1)
)
fgs2528kxTrapHostConfEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxTrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfEntry.setStatus("current")


class _Fgs2528kxTrapHostConfIndex_Type(Integer32):
    """Custom type fgs2528kxTrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Fgs2528kxTrapHostConfIndex_Type.__name__ = "Integer32"
_Fgs2528kxTrapHostConfIndex_Object = MibTableColumn
fgs2528kxTrapHostConfIndex = _Fgs2528kxTrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 1),
    _Fgs2528kxTrapHostConfIndex_Type()
)
fgs2528kxTrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfIndex.setStatus("current")


class _Fgs2528kxTrapHostConfVersion_Type(Integer32):
    """Custom type fgs2528kxTrapHostConfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3),
    )


_Fgs2528kxTrapHostConfVersion_Type.__name__ = "Integer32"
_Fgs2528kxTrapHostConfVersion_Object = MibTableColumn
fgs2528kxTrapHostConfVersion = _Fgs2528kxTrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 2),
    _Fgs2528kxTrapHostConfVersion_Type()
)
fgs2528kxTrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfVersion.setStatus("current")


class _Fgs2528kxTrapHostConfIPType_Type(Integer32):
    """Custom type fgs2528kxTrapHostConfIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
    )


_Fgs2528kxTrapHostConfIPType_Type.__name__ = "Integer32"
_Fgs2528kxTrapHostConfIPType_Object = MibTableColumn
fgs2528kxTrapHostConfIPType = _Fgs2528kxTrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 3),
    _Fgs2528kxTrapHostConfIPType_Type()
)
fgs2528kxTrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfIPType.setStatus("current")
_Fgs2528kxTrapHostConfIP_Type = DisplayString
_Fgs2528kxTrapHostConfIP_Object = MibTableColumn
fgs2528kxTrapHostConfIP = _Fgs2528kxTrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 4),
    _Fgs2528kxTrapHostConfIP_Type()
)
fgs2528kxTrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfIP.setStatus("current")


class _Fgs2528kxTrapHostConfPort_Type(Integer32):
    """Custom type fgs2528kxTrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Fgs2528kxTrapHostConfPort_Type.__name__ = "Integer32"
_Fgs2528kxTrapHostConfPort_Object = MibTableColumn
fgs2528kxTrapHostConfPort = _Fgs2528kxTrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 5),
    _Fgs2528kxTrapHostConfPort_Type()
)
fgs2528kxTrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfPort.setStatus("current")


class _Fgs2528kxTrapHostConfCommunity_Type(DisplayString):
    """Custom type fgs2528kxTrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Fgs2528kxTrapHostConfCommunity_Type.__name__ = "DisplayString"
_Fgs2528kxTrapHostConfCommunity_Object = MibTableColumn
fgs2528kxTrapHostConfCommunity = _Fgs2528kxTrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 6),
    _Fgs2528kxTrapHostConfCommunity_Type()
)
fgs2528kxTrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfCommunity.setStatus("current")


class _Fgs2528kxTrapHostConfSeverityLevel_Type(Integer32):
    """Custom type fgs2528kxTrapHostConfSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Fgs2528kxTrapHostConfSeverityLevel_Object = MibTableColumn
fgs2528kxTrapHostConfSeverityLevel = _Fgs2528kxTrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 7),
    _Fgs2528kxTrapHostConfSeverityLevel_Type()
)
fgs2528kxTrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfSeverityLevel.setStatus("current")


class _Fgs2528kxTrapHostConfSecurityLevel_Type(Integer32):
    """Custom type fgs2528kxTrapHostConfSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Fgs2528kxTrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Fgs2528kxTrapHostConfSecurityLevel_Object = MibTableColumn
fgs2528kxTrapHostConfSecurityLevel = _Fgs2528kxTrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 8),
    _Fgs2528kxTrapHostConfSecurityLevel_Type()
)
fgs2528kxTrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfSecurityLevel.setStatus("current")


class _Fgs2528kxTrapHostConfAuthPtc_Type(Integer32):
    """Custom type fgs2528kxTrapHostConfAuthPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Fgs2528kxTrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Fgs2528kxTrapHostConfAuthPtc_Object = MibTableColumn
fgs2528kxTrapHostConfAuthPtc = _Fgs2528kxTrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 9),
    _Fgs2528kxTrapHostConfAuthPtc_Type()
)
fgs2528kxTrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfAuthPtc.setStatus("current")
_Fgs2528kxTrapHostConfAuthPassword_Type = DisplayString
_Fgs2528kxTrapHostConfAuthPassword_Object = MibTableColumn
fgs2528kxTrapHostConfAuthPassword = _Fgs2528kxTrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 10),
    _Fgs2528kxTrapHostConfAuthPassword_Type()
)
fgs2528kxTrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfAuthPassword.setStatus("current")


class _Fgs2528kxTrapHostConfPrivPtc_Type(Integer32):
    """Custom type fgs2528kxTrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxTrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Fgs2528kxTrapHostConfPrivPtc_Object = MibTableColumn
fgs2528kxTrapHostConfPrivPtc = _Fgs2528kxTrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 11),
    _Fgs2528kxTrapHostConfPrivPtc_Type()
)
fgs2528kxTrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfPrivPtc.setStatus("current")
_Fgs2528kxTrapHostConfPrivPassword_Type = DisplayString
_Fgs2528kxTrapHostConfPrivPassword_Object = MibTableColumn
fgs2528kxTrapHostConfPrivPassword = _Fgs2528kxTrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 12),
    _Fgs2528kxTrapHostConfPrivPassword_Type()
)
fgs2528kxTrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfPrivPassword.setStatus("current")


class _Fgs2528kxTrapHostConfCurrentMode_Type(Integer32):
    """Custom type fgs2528kxTrapHostConfCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxTrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Fgs2528kxTrapHostConfCurrentMode_Object = MibTableColumn
fgs2528kxTrapHostConfCurrentMode = _Fgs2528kxTrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 1, 6, 1, 4, 1, 13),
    _Fgs2528kxTrapHostConfCurrentMode_Type()
)
fgs2528kxTrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapHostConfCurrentMode.setStatus("current")
_Fgs2528kxConfiguration_ObjectIdentity = ObjectIdentity
fgs2528kxConfiguration = _Fgs2528kxConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2)
)
_Fgs2528kxPort_ObjectIdentity = ObjectIdentity
fgs2528kxPort = _Fgs2528kxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1)
)
_Fgs2528kxPortConfigurationTable_Object = MibTable
fgs2528kxPortConfigurationTable = _Fgs2528kxPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgs2528kxPortConfigurationTable.setStatus("current")
_Fgs2528kxPortConfigurationEntry_Object = MibTableRow
fgs2528kxPortConfigurationEntry = _Fgs2528kxPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1)
)
fgs2528kxPortConfigurationEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxPortConfPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxPortConfigurationEntry.setStatus("current")


class _Fgs2528kxPortConfPort_Type(Integer32):
    """Custom type fgs2528kxPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxPortConfPort_Type.__name__ = "Integer32"
_Fgs2528kxPortConfPort_Object = MibTableColumn
fgs2528kxPortConfPort = _Fgs2528kxPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 1),
    _Fgs2528kxPortConfPort_Type()
)
fgs2528kxPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxPortConfPort.setStatus("current")


class _Fgs2528kxPortConfPortMedia_Type(DisplayString):
    """Custom type fgs2528kxPortConfPortMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Fgs2528kxPortConfPortMedia_Type.__name__ = "DisplayString"
_Fgs2528kxPortConfPortMedia_Object = MibTableColumn
fgs2528kxPortConfPortMedia = _Fgs2528kxPortConfPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 2),
    _Fgs2528kxPortConfPortMedia_Type()
)
fgs2528kxPortConfPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortConfPortMedia.setStatus("current")


class _Fgs2528kxPortConfLink_Type(DisplayString):
    """Custom type fgs2528kxPortConfLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Fgs2528kxPortConfLink_Type.__name__ = "DisplayString"
_Fgs2528kxPortConfLink_Object = MibTableColumn
fgs2528kxPortConfLink = _Fgs2528kxPortConfLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 3),
    _Fgs2528kxPortConfLink_Type()
)
fgs2528kxPortConfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortConfLink.setStatus("current")


class _Fgs2528kxPortConfCurrentSpeed_Type(DisplayString):
    """Custom type fgs2528kxPortConfCurrentSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 12),
    )


_Fgs2528kxPortConfCurrentSpeed_Type.__name__ = "DisplayString"
_Fgs2528kxPortConfCurrentSpeed_Object = MibTableColumn
fgs2528kxPortConfCurrentSpeed = _Fgs2528kxPortConfCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 4),
    _Fgs2528kxPortConfCurrentSpeed_Type()
)
fgs2528kxPortConfCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortConfCurrentSpeed.setStatus("current")


class _Fgs2528kxPortConfSpeed_Type(Integer32):
    """Custom type fgs2528kxPortConfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Fgs2528kxPortConfSpeed_Type.__name__ = "Integer32"
_Fgs2528kxPortConfSpeed_Object = MibTableColumn
fgs2528kxPortConfSpeed = _Fgs2528kxPortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 5),
    _Fgs2528kxPortConfSpeed_Type()
)
fgs2528kxPortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortConfSpeed.setStatus("current")


class _Fgs2528kxPortConfCurrentFlowControlRx_Type(Integer32):
    """Custom type fgs2528kxPortConfCurrentFlowControlRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortConfCurrentFlowControlRx_Type.__name__ = "Integer32"
_Fgs2528kxPortConfCurrentFlowControlRx_Object = MibTableColumn
fgs2528kxPortConfCurrentFlowControlRx = _Fgs2528kxPortConfCurrentFlowControlRx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 6),
    _Fgs2528kxPortConfCurrentFlowControlRx_Type()
)
fgs2528kxPortConfCurrentFlowControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortConfCurrentFlowControlRx.setStatus("current")


class _Fgs2528kxPortConfCurrentFlowControlTx_Type(Integer32):
    """Custom type fgs2528kxPortConfCurrentFlowControlTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortConfCurrentFlowControlTx_Type.__name__ = "Integer32"
_Fgs2528kxPortConfCurrentFlowControlTx_Object = MibTableColumn
fgs2528kxPortConfCurrentFlowControlTx = _Fgs2528kxPortConfCurrentFlowControlTx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 7),
    _Fgs2528kxPortConfCurrentFlowControlTx_Type()
)
fgs2528kxPortConfCurrentFlowControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortConfCurrentFlowControlTx.setStatus("current")


class _Fgs2528kxPortConfFlowControl_Type(Integer32):
    """Custom type fgs2528kxPortConfFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortConfFlowControl_Type.__name__ = "Integer32"
_Fgs2528kxPortConfFlowControl_Object = MibTableColumn
fgs2528kxPortConfFlowControl = _Fgs2528kxPortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 8),
    _Fgs2528kxPortConfFlowControl_Type()
)
fgs2528kxPortConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortConfFlowControl.setStatus("current")


class _Fgs2528kxPortConfMaxFrameSize_Type(Integer32):
    """Custom type fgs2528kxPortConfMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Fgs2528kxPortConfMaxFrameSize_Type.__name__ = "Integer32"
_Fgs2528kxPortConfMaxFrameSize_Object = MibTableColumn
fgs2528kxPortConfMaxFrameSize = _Fgs2528kxPortConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 9),
    _Fgs2528kxPortConfMaxFrameSize_Type()
)
fgs2528kxPortConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortConfMaxFrameSize.setStatus("current")


class _Fgs2528kxPortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type fgs2528kxPortConfExcessiveCollisionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Fgs2528kxPortConfExcessiveCollisionMode_Object = MibTableColumn
fgs2528kxPortConfExcessiveCollisionMode = _Fgs2528kxPortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 10),
    _Fgs2528kxPortConfExcessiveCollisionMode_Type()
)
fgs2528kxPortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortConfExcessiveCollisionMode.setStatus("current")


class _Fgs2528kxPortConfPowerControl_Type(Integer32):
    """Custom type fgs2528kxPortConfPowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxPortConfPowerControl_Type.__name__ = "Integer32"
_Fgs2528kxPortConfPowerControl_Object = MibTableColumn
fgs2528kxPortConfPowerControl = _Fgs2528kxPortConfPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 11),
    _Fgs2528kxPortConfPowerControl_Type()
)
fgs2528kxPortConfPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortConfPowerControl.setStatus("current")
_Fgs2528kxPortConfDescription_Type = DisplayString
_Fgs2528kxPortConfDescription_Object = MibTableColumn
fgs2528kxPortConfDescription = _Fgs2528kxPortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 1, 1, 12),
    _Fgs2528kxPortConfDescription_Type()
)
fgs2528kxPortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortConfDescription.setStatus("current")
_Fgs2528kxPortTrafficStatisticsTable_Object = MibTable
fgs2528kxPortTrafficStatisticsTable = _Fgs2528kxPortTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficStatisticsTable.setStatus("current")
_Fgs2528kxPortTrafficStatisticsEntry_Object = MibTableRow
fgs2528kxPortTrafficStatisticsEntry = _Fgs2528kxPortTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1)
)
fgs2528kxPortTrafficStatisticsEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxPortTrafficStatisticsPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficStatisticsEntry.setStatus("current")


class _Fgs2528kxPortTrafficStatisticsPort_Type(Integer32):
    """Custom type fgs2528kxPortTrafficStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxPortTrafficStatisticsPort_Type.__name__ = "Integer32"
_Fgs2528kxPortTrafficStatisticsPort_Object = MibTableColumn
fgs2528kxPortTrafficStatisticsPort = _Fgs2528kxPortTrafficStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 1),
    _Fgs2528kxPortTrafficStatisticsPort_Type()
)
fgs2528kxPortTrafficStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficStatisticsPort.setStatus("current")


class _Fgs2528kxPortTrafficStatisticsClear_Type(Integer32):
    """Custom type fgs2528kxPortTrafficStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortTrafficStatisticsClear_Type.__name__ = "Integer32"
_Fgs2528kxPortTrafficStatisticsClear_Object = MibTableColumn
fgs2528kxPortTrafficStatisticsClear = _Fgs2528kxPortTrafficStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 2),
    _Fgs2528kxPortTrafficStatisticsClear_Type()
)
fgs2528kxPortTrafficStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficStatisticsClear.setStatus("current")
_Fgs2528kxPortTrafficRxPackets_Type = Counter64
_Fgs2528kxPortTrafficRxPackets_Object = MibTableColumn
fgs2528kxPortTrafficRxPackets = _Fgs2528kxPortTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 3),
    _Fgs2528kxPortTrafficRxPackets_Type()
)
fgs2528kxPortTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxPackets.setStatus("current")
_Fgs2528kxPortTrafficRxOctets_Type = Counter64
_Fgs2528kxPortTrafficRxOctets_Object = MibTableColumn
fgs2528kxPortTrafficRxOctets = _Fgs2528kxPortTrafficRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 4),
    _Fgs2528kxPortTrafficRxOctets_Type()
)
fgs2528kxPortTrafficRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxOctets.setStatus("current")
_Fgs2528kxPortTrafficRxUnicast_Type = Counter64
_Fgs2528kxPortTrafficRxUnicast_Object = MibTableColumn
fgs2528kxPortTrafficRxUnicast = _Fgs2528kxPortTrafficRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 5),
    _Fgs2528kxPortTrafficRxUnicast_Type()
)
fgs2528kxPortTrafficRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxUnicast.setStatus("current")
_Fgs2528kxPortTrafficRxMulticast_Type = Counter64
_Fgs2528kxPortTrafficRxMulticast_Object = MibTableColumn
fgs2528kxPortTrafficRxMulticast = _Fgs2528kxPortTrafficRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 6),
    _Fgs2528kxPortTrafficRxMulticast_Type()
)
fgs2528kxPortTrafficRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxMulticast.setStatus("current")
_Fgs2528kxPortTrafficRxBroadcast_Type = Counter64
_Fgs2528kxPortTrafficRxBroadcast_Object = MibTableColumn
fgs2528kxPortTrafficRxBroadcast = _Fgs2528kxPortTrafficRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 7),
    _Fgs2528kxPortTrafficRxBroadcast_Type()
)
fgs2528kxPortTrafficRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxBroadcast.setStatus("current")
_Fgs2528kxPortTrafficRxPause_Type = Counter64
_Fgs2528kxPortTrafficRxPause_Object = MibTableColumn
fgs2528kxPortTrafficRxPause = _Fgs2528kxPortTrafficRxPause_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 8),
    _Fgs2528kxPortTrafficRxPause_Type()
)
fgs2528kxPortTrafficRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxPause.setStatus("current")
_Fgs2528kxPortTrafficRx64Bytes_Type = Counter64
_Fgs2528kxPortTrafficRx64Bytes_Object = MibTableColumn
fgs2528kxPortTrafficRx64Bytes = _Fgs2528kxPortTrafficRx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 9),
    _Fgs2528kxPortTrafficRx64Bytes_Type()
)
fgs2528kxPortTrafficRx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRx64Bytes.setStatus("current")
_Fgs2528kxPortTrafficRx65to127Bytes_Type = Counter64
_Fgs2528kxPortTrafficRx65to127Bytes_Object = MibTableColumn
fgs2528kxPortTrafficRx65to127Bytes = _Fgs2528kxPortTrafficRx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 10),
    _Fgs2528kxPortTrafficRx65to127Bytes_Type()
)
fgs2528kxPortTrafficRx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRx65to127Bytes.setStatus("current")
_Fgs2528kxPortTrafficRx128to255Bytes_Type = Counter64
_Fgs2528kxPortTrafficRx128to255Bytes_Object = MibTableColumn
fgs2528kxPortTrafficRx128to255Bytes = _Fgs2528kxPortTrafficRx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 11),
    _Fgs2528kxPortTrafficRx128to255Bytes_Type()
)
fgs2528kxPortTrafficRx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRx128to255Bytes.setStatus("current")
_Fgs2528kxPortTrafficRx256to511Bytes_Type = Counter64
_Fgs2528kxPortTrafficRx256to511Bytes_Object = MibTableColumn
fgs2528kxPortTrafficRx256to511Bytes = _Fgs2528kxPortTrafficRx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 12),
    _Fgs2528kxPortTrafficRx256to511Bytes_Type()
)
fgs2528kxPortTrafficRx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRx256to511Bytes.setStatus("current")
_Fgs2528kxPortTrafficRx512to1023Bytes_Type = Counter64
_Fgs2528kxPortTrafficRx512to1023Bytes_Object = MibTableColumn
fgs2528kxPortTrafficRx512to1023Bytes = _Fgs2528kxPortTrafficRx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 13),
    _Fgs2528kxPortTrafficRx512to1023Bytes_Type()
)
fgs2528kxPortTrafficRx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRx512to1023Bytes.setStatus("current")
_Fgs2528kxPortTrafficRx1024to1526Bytes_Type = Counter64
_Fgs2528kxPortTrafficRx1024to1526Bytes_Object = MibTableColumn
fgs2528kxPortTrafficRx1024to1526Bytes = _Fgs2528kxPortTrafficRx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 14),
    _Fgs2528kxPortTrafficRx1024to1526Bytes_Type()
)
fgs2528kxPortTrafficRx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRx1024to1526Bytes.setStatus("current")
_Fgs2528kxPortTrafficRxExceecd1527Bytes_Type = Counter64
_Fgs2528kxPortTrafficRxExceecd1527Bytes_Object = MibTableColumn
fgs2528kxPortTrafficRxExceecd1527Bytes = _Fgs2528kxPortTrafficRxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 15),
    _Fgs2528kxPortTrafficRxExceecd1527Bytes_Type()
)
fgs2528kxPortTrafficRxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxExceecd1527Bytes.setStatus("current")
_Fgs2528kxPortTrafficRxQ0_Type = Counter64
_Fgs2528kxPortTrafficRxQ0_Object = MibTableColumn
fgs2528kxPortTrafficRxQ0 = _Fgs2528kxPortTrafficRxQ0_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 16),
    _Fgs2528kxPortTrafficRxQ0_Type()
)
fgs2528kxPortTrafficRxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxQ0.setStatus("current")
_Fgs2528kxPortTrafficRxQ1_Type = Counter64
_Fgs2528kxPortTrafficRxQ1_Object = MibTableColumn
fgs2528kxPortTrafficRxQ1 = _Fgs2528kxPortTrafficRxQ1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 17),
    _Fgs2528kxPortTrafficRxQ1_Type()
)
fgs2528kxPortTrafficRxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxQ1.setStatus("current")
_Fgs2528kxPortTrafficRxQ2_Type = Counter64
_Fgs2528kxPortTrafficRxQ2_Object = MibTableColumn
fgs2528kxPortTrafficRxQ2 = _Fgs2528kxPortTrafficRxQ2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 18),
    _Fgs2528kxPortTrafficRxQ2_Type()
)
fgs2528kxPortTrafficRxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxQ2.setStatus("current")
_Fgs2528kxPortTrafficRxQ3_Type = Counter64
_Fgs2528kxPortTrafficRxQ3_Object = MibTableColumn
fgs2528kxPortTrafficRxQ3 = _Fgs2528kxPortTrafficRxQ3_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 19),
    _Fgs2528kxPortTrafficRxQ3_Type()
)
fgs2528kxPortTrafficRxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxQ3.setStatus("current")
_Fgs2528kxPortTrafficRxQ4_Type = Counter64
_Fgs2528kxPortTrafficRxQ4_Object = MibTableColumn
fgs2528kxPortTrafficRxQ4 = _Fgs2528kxPortTrafficRxQ4_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 20),
    _Fgs2528kxPortTrafficRxQ4_Type()
)
fgs2528kxPortTrafficRxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxQ4.setStatus("current")
_Fgs2528kxPortTrafficRxQ5_Type = Counter64
_Fgs2528kxPortTrafficRxQ5_Object = MibTableColumn
fgs2528kxPortTrafficRxQ5 = _Fgs2528kxPortTrafficRxQ5_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 21),
    _Fgs2528kxPortTrafficRxQ5_Type()
)
fgs2528kxPortTrafficRxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxQ5.setStatus("current")
_Fgs2528kxPortTrafficRxQ6_Type = Counter64
_Fgs2528kxPortTrafficRxQ6_Object = MibTableColumn
fgs2528kxPortTrafficRxQ6 = _Fgs2528kxPortTrafficRxQ6_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 22),
    _Fgs2528kxPortTrafficRxQ6_Type()
)
fgs2528kxPortTrafficRxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxQ6.setStatus("current")
_Fgs2528kxPortTrafficRxQ7_Type = Counter64
_Fgs2528kxPortTrafficRxQ7_Object = MibTableColumn
fgs2528kxPortTrafficRxQ7 = _Fgs2528kxPortTrafficRxQ7_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 23),
    _Fgs2528kxPortTrafficRxQ7_Type()
)
fgs2528kxPortTrafficRxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxQ7.setStatus("current")
_Fgs2528kxPortTrafficRxDrops_Type = Counter64
_Fgs2528kxPortTrafficRxDrops_Object = MibTableColumn
fgs2528kxPortTrafficRxDrops = _Fgs2528kxPortTrafficRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 24),
    _Fgs2528kxPortTrafficRxDrops_Type()
)
fgs2528kxPortTrafficRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxDrops.setStatus("current")
_Fgs2528kxPortTrafficRxCRCorAlignment_Type = Counter64
_Fgs2528kxPortTrafficRxCRCorAlignment_Object = MibTableColumn
fgs2528kxPortTrafficRxCRCorAlignment = _Fgs2528kxPortTrafficRxCRCorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 25),
    _Fgs2528kxPortTrafficRxCRCorAlignment_Type()
)
fgs2528kxPortTrafficRxCRCorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxCRCorAlignment.setStatus("current")
_Fgs2528kxPortTrafficRxUndersize_Type = Counter64
_Fgs2528kxPortTrafficRxUndersize_Object = MibTableColumn
fgs2528kxPortTrafficRxUndersize = _Fgs2528kxPortTrafficRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 26),
    _Fgs2528kxPortTrafficRxUndersize_Type()
)
fgs2528kxPortTrafficRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxUndersize.setStatus("current")
_Fgs2528kxPortTrafficRxOversize_Type = Counter64
_Fgs2528kxPortTrafficRxOversize_Object = MibTableColumn
fgs2528kxPortTrafficRxOversize = _Fgs2528kxPortTrafficRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 27),
    _Fgs2528kxPortTrafficRxOversize_Type()
)
fgs2528kxPortTrafficRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxOversize.setStatus("current")
_Fgs2528kxPortTrafficRxFragments_Type = Counter64
_Fgs2528kxPortTrafficRxFragments_Object = MibTableColumn
fgs2528kxPortTrafficRxFragments = _Fgs2528kxPortTrafficRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 28),
    _Fgs2528kxPortTrafficRxFragments_Type()
)
fgs2528kxPortTrafficRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxFragments.setStatus("current")
_Fgs2528kxPortTrafficRxJabber_Type = Counter64
_Fgs2528kxPortTrafficRxJabber_Object = MibTableColumn
fgs2528kxPortTrafficRxJabber = _Fgs2528kxPortTrafficRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 29),
    _Fgs2528kxPortTrafficRxJabber_Type()
)
fgs2528kxPortTrafficRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxJabber.setStatus("current")
_Fgs2528kxPortTrafficRxFiltered_Type = Counter64
_Fgs2528kxPortTrafficRxFiltered_Object = MibTableColumn
fgs2528kxPortTrafficRxFiltered = _Fgs2528kxPortTrafficRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 30),
    _Fgs2528kxPortTrafficRxFiltered_Type()
)
fgs2528kxPortTrafficRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficRxFiltered.setStatus("current")
_Fgs2528kxPortTrafficTxPackets_Type = Counter64
_Fgs2528kxPortTrafficTxPackets_Object = MibTableColumn
fgs2528kxPortTrafficTxPackets = _Fgs2528kxPortTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 31),
    _Fgs2528kxPortTrafficTxPackets_Type()
)
fgs2528kxPortTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxPackets.setStatus("current")
_Fgs2528kxPortTrafficTxOctets_Type = Counter64
_Fgs2528kxPortTrafficTxOctets_Object = MibTableColumn
fgs2528kxPortTrafficTxOctets = _Fgs2528kxPortTrafficTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 32),
    _Fgs2528kxPortTrafficTxOctets_Type()
)
fgs2528kxPortTrafficTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxOctets.setStatus("current")
_Fgs2528kxPortTrafficTxUnicast_Type = Counter64
_Fgs2528kxPortTrafficTxUnicast_Object = MibTableColumn
fgs2528kxPortTrafficTxUnicast = _Fgs2528kxPortTrafficTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 33),
    _Fgs2528kxPortTrafficTxUnicast_Type()
)
fgs2528kxPortTrafficTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxUnicast.setStatus("current")
_Fgs2528kxPortTrafficTxMulticast_Type = Counter64
_Fgs2528kxPortTrafficTxMulticast_Object = MibTableColumn
fgs2528kxPortTrafficTxMulticast = _Fgs2528kxPortTrafficTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 34),
    _Fgs2528kxPortTrafficTxMulticast_Type()
)
fgs2528kxPortTrafficTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxMulticast.setStatus("current")
_Fgs2528kxPortTrafficTxBroadcast_Type = Counter64
_Fgs2528kxPortTrafficTxBroadcast_Object = MibTableColumn
fgs2528kxPortTrafficTxBroadcast = _Fgs2528kxPortTrafficTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 35),
    _Fgs2528kxPortTrafficTxBroadcast_Type()
)
fgs2528kxPortTrafficTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxBroadcast.setStatus("current")
_Fgs2528kxPortTrafficTxPause_Type = Counter64
_Fgs2528kxPortTrafficTxPause_Object = MibTableColumn
fgs2528kxPortTrafficTxPause = _Fgs2528kxPortTrafficTxPause_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 36),
    _Fgs2528kxPortTrafficTxPause_Type()
)
fgs2528kxPortTrafficTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxPause.setStatus("current")
_Fgs2528kxPortTrafficTx64Bytes_Type = Counter64
_Fgs2528kxPortTrafficTx64Bytes_Object = MibTableColumn
fgs2528kxPortTrafficTx64Bytes = _Fgs2528kxPortTrafficTx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 37),
    _Fgs2528kxPortTrafficTx64Bytes_Type()
)
fgs2528kxPortTrafficTx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTx64Bytes.setStatus("current")
_Fgs2528kxPortTrafficTx65to127Bytes_Type = Counter64
_Fgs2528kxPortTrafficTx65to127Bytes_Object = MibTableColumn
fgs2528kxPortTrafficTx65to127Bytes = _Fgs2528kxPortTrafficTx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 38),
    _Fgs2528kxPortTrafficTx65to127Bytes_Type()
)
fgs2528kxPortTrafficTx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTx65to127Bytes.setStatus("current")
_Fgs2528kxPortTrafficTx128to255Bytes_Type = Counter64
_Fgs2528kxPortTrafficTx128to255Bytes_Object = MibTableColumn
fgs2528kxPortTrafficTx128to255Bytes = _Fgs2528kxPortTrafficTx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 39),
    _Fgs2528kxPortTrafficTx128to255Bytes_Type()
)
fgs2528kxPortTrafficTx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTx128to255Bytes.setStatus("current")
_Fgs2528kxPortTrafficTx256to511Bytes_Type = Counter64
_Fgs2528kxPortTrafficTx256to511Bytes_Object = MibTableColumn
fgs2528kxPortTrafficTx256to511Bytes = _Fgs2528kxPortTrafficTx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 40),
    _Fgs2528kxPortTrafficTx256to511Bytes_Type()
)
fgs2528kxPortTrafficTx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTx256to511Bytes.setStatus("current")
_Fgs2528kxPortTrafficTx512to1023Bytes_Type = Counter64
_Fgs2528kxPortTrafficTx512to1023Bytes_Object = MibTableColumn
fgs2528kxPortTrafficTx512to1023Bytes = _Fgs2528kxPortTrafficTx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 41),
    _Fgs2528kxPortTrafficTx512to1023Bytes_Type()
)
fgs2528kxPortTrafficTx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTx512to1023Bytes.setStatus("current")
_Fgs2528kxPortTrafficTx1024to1526Bytes_Type = Counter64
_Fgs2528kxPortTrafficTx1024to1526Bytes_Object = MibTableColumn
fgs2528kxPortTrafficTx1024to1526Bytes = _Fgs2528kxPortTrafficTx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 42),
    _Fgs2528kxPortTrafficTx1024to1526Bytes_Type()
)
fgs2528kxPortTrafficTx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTx1024to1526Bytes.setStatus("current")
_Fgs2528kxPortTrafficTxExceecd1527Bytes_Type = Counter64
_Fgs2528kxPortTrafficTxExceecd1527Bytes_Object = MibTableColumn
fgs2528kxPortTrafficTxExceecd1527Bytes = _Fgs2528kxPortTrafficTxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 43),
    _Fgs2528kxPortTrafficTxExceecd1527Bytes_Type()
)
fgs2528kxPortTrafficTxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxExceecd1527Bytes.setStatus("current")
_Fgs2528kxPortTrafficTxQ0_Type = Counter64
_Fgs2528kxPortTrafficTxQ0_Object = MibTableColumn
fgs2528kxPortTrafficTxQ0 = _Fgs2528kxPortTrafficTxQ0_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 44),
    _Fgs2528kxPortTrafficTxQ0_Type()
)
fgs2528kxPortTrafficTxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxQ0.setStatus("current")
_Fgs2528kxPortTrafficTxQ1_Type = Counter64
_Fgs2528kxPortTrafficTxQ1_Object = MibTableColumn
fgs2528kxPortTrafficTxQ1 = _Fgs2528kxPortTrafficTxQ1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 45),
    _Fgs2528kxPortTrafficTxQ1_Type()
)
fgs2528kxPortTrafficTxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxQ1.setStatus("current")
_Fgs2528kxPortTrafficTxQ2_Type = Counter64
_Fgs2528kxPortTrafficTxQ2_Object = MibTableColumn
fgs2528kxPortTrafficTxQ2 = _Fgs2528kxPortTrafficTxQ2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 46),
    _Fgs2528kxPortTrafficTxQ2_Type()
)
fgs2528kxPortTrafficTxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxQ2.setStatus("current")
_Fgs2528kxPortTrafficTxQ3_Type = Counter64
_Fgs2528kxPortTrafficTxQ3_Object = MibTableColumn
fgs2528kxPortTrafficTxQ3 = _Fgs2528kxPortTrafficTxQ3_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 47),
    _Fgs2528kxPortTrafficTxQ3_Type()
)
fgs2528kxPortTrafficTxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxQ3.setStatus("current")
_Fgs2528kxPortTrafficTxQ4_Type = Counter64
_Fgs2528kxPortTrafficTxQ4_Object = MibTableColumn
fgs2528kxPortTrafficTxQ4 = _Fgs2528kxPortTrafficTxQ4_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 48),
    _Fgs2528kxPortTrafficTxQ4_Type()
)
fgs2528kxPortTrafficTxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxQ4.setStatus("current")
_Fgs2528kxPortTrafficTxQ5_Type = Counter64
_Fgs2528kxPortTrafficTxQ5_Object = MibTableColumn
fgs2528kxPortTrafficTxQ5 = _Fgs2528kxPortTrafficTxQ5_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 49),
    _Fgs2528kxPortTrafficTxQ5_Type()
)
fgs2528kxPortTrafficTxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxQ5.setStatus("current")
_Fgs2528kxPortTrafficTxQ6_Type = Counter64
_Fgs2528kxPortTrafficTxQ6_Object = MibTableColumn
fgs2528kxPortTrafficTxQ6 = _Fgs2528kxPortTrafficTxQ6_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 50),
    _Fgs2528kxPortTrafficTxQ6_Type()
)
fgs2528kxPortTrafficTxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxQ6.setStatus("current")
_Fgs2528kxPortTrafficTxQ7_Type = Counter64
_Fgs2528kxPortTrafficTxQ7_Object = MibTableColumn
fgs2528kxPortTrafficTxQ7 = _Fgs2528kxPortTrafficTxQ7_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 51),
    _Fgs2528kxPortTrafficTxQ7_Type()
)
fgs2528kxPortTrafficTxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxQ7.setStatus("current")
_Fgs2528kxPortTrafficTxDrops_Type = Counter64
_Fgs2528kxPortTrafficTxDrops_Object = MibTableColumn
fgs2528kxPortTrafficTxDrops = _Fgs2528kxPortTrafficTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 52),
    _Fgs2528kxPortTrafficTxDrops_Type()
)
fgs2528kxPortTrafficTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxDrops.setStatus("current")
_Fgs2528kxPortTrafficTxLateOrExcColl_Type = Counter64
_Fgs2528kxPortTrafficTxLateOrExcColl_Object = MibTableColumn
fgs2528kxPortTrafficTxLateOrExcColl = _Fgs2528kxPortTrafficTxLateOrExcColl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 2, 1, 53),
    _Fgs2528kxPortTrafficTxLateOrExcColl_Type()
)
fgs2528kxPortTrafficTxLateOrExcColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortTrafficTxLateOrExcColl.setStatus("current")
_Fgs2528kxPortQoSStatistics_ObjectIdentity = ObjectIdentity
fgs2528kxPortQoSStatistics = _Fgs2528kxPortQoSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3)
)


class _Fgs2528kxPortQoSStatisticsClear_Type(Integer32):
    """Custom type fgs2528kxPortQoSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortQoSStatisticsClear_Type.__name__ = "Integer32"
_Fgs2528kxPortQoSStatisticsClear_Object = MibScalar
fgs2528kxPortQoSStatisticsClear = _Fgs2528kxPortQoSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 1),
    _Fgs2528kxPortQoSStatisticsClear_Type()
)
fgs2528kxPortQoSStatisticsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSStatisticsClear.setStatus("current")
_Fgs2528kxPortQoSStatisticsTable_Object = MibTable
fgs2528kxPortQoSStatisticsTable = _Fgs2528kxPortQoSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxPortQoSStatisticsTable.setStatus("current")
_Fgs2528kxPortQoSStatisticsEntry_Object = MibTableRow
fgs2528kxPortQoSStatisticsEntry = _Fgs2528kxPortQoSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1)
)
fgs2528kxPortQoSStatisticsEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxPortQoSStatisticsPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxPortQoSStatisticsEntry.setStatus("current")


class _Fgs2528kxPortQoSStatisticsPort_Type(Integer32):
    """Custom type fgs2528kxPortQoSStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxPortQoSStatisticsPort_Type.__name__ = "Integer32"
_Fgs2528kxPortQoSStatisticsPort_Object = MibTableColumn
fgs2528kxPortQoSStatisticsPort = _Fgs2528kxPortQoSStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 1),
    _Fgs2528kxPortQoSStatisticsPort_Type()
)
fgs2528kxPortQoSStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSStatisticsPort.setStatus("current")
_Fgs2528kxPortQoSQ0Rx_Type = Counter64
_Fgs2528kxPortQoSQ0Rx_Object = MibTableColumn
fgs2528kxPortQoSQ0Rx = _Fgs2528kxPortQoSQ0Rx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 2),
    _Fgs2528kxPortQoSQ0Rx_Type()
)
fgs2528kxPortQoSQ0Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ0Rx.setStatus("current")
_Fgs2528kxPortQoSQ0Tx_Type = Counter64
_Fgs2528kxPortQoSQ0Tx_Object = MibTableColumn
fgs2528kxPortQoSQ0Tx = _Fgs2528kxPortQoSQ0Tx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 3),
    _Fgs2528kxPortQoSQ0Tx_Type()
)
fgs2528kxPortQoSQ0Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ0Tx.setStatus("current")
_Fgs2528kxPortQoSQ1Rx_Type = Counter64
_Fgs2528kxPortQoSQ1Rx_Object = MibTableColumn
fgs2528kxPortQoSQ1Rx = _Fgs2528kxPortQoSQ1Rx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 4),
    _Fgs2528kxPortQoSQ1Rx_Type()
)
fgs2528kxPortQoSQ1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ1Rx.setStatus("current")
_Fgs2528kxPortQoSQ1Tx_Type = Counter64
_Fgs2528kxPortQoSQ1Tx_Object = MibTableColumn
fgs2528kxPortQoSQ1Tx = _Fgs2528kxPortQoSQ1Tx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 5),
    _Fgs2528kxPortQoSQ1Tx_Type()
)
fgs2528kxPortQoSQ1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ1Tx.setStatus("current")
_Fgs2528kxPortQoSQ2Rx_Type = Counter64
_Fgs2528kxPortQoSQ2Rx_Object = MibTableColumn
fgs2528kxPortQoSQ2Rx = _Fgs2528kxPortQoSQ2Rx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 6),
    _Fgs2528kxPortQoSQ2Rx_Type()
)
fgs2528kxPortQoSQ2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ2Rx.setStatus("current")
_Fgs2528kxPortQoSQ2Tx_Type = Counter64
_Fgs2528kxPortQoSQ2Tx_Object = MibTableColumn
fgs2528kxPortQoSQ2Tx = _Fgs2528kxPortQoSQ2Tx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 7),
    _Fgs2528kxPortQoSQ2Tx_Type()
)
fgs2528kxPortQoSQ2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ2Tx.setStatus("current")
_Fgs2528kxPortQoSQ3Rx_Type = Counter64
_Fgs2528kxPortQoSQ3Rx_Object = MibTableColumn
fgs2528kxPortQoSQ3Rx = _Fgs2528kxPortQoSQ3Rx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 8),
    _Fgs2528kxPortQoSQ3Rx_Type()
)
fgs2528kxPortQoSQ3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ3Rx.setStatus("current")
_Fgs2528kxPortQoSQ3Tx_Type = Counter64
_Fgs2528kxPortQoSQ3Tx_Object = MibTableColumn
fgs2528kxPortQoSQ3Tx = _Fgs2528kxPortQoSQ3Tx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 9),
    _Fgs2528kxPortQoSQ3Tx_Type()
)
fgs2528kxPortQoSQ3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ3Tx.setStatus("current")
_Fgs2528kxPortQoSQ4Rx_Type = Counter64
_Fgs2528kxPortQoSQ4Rx_Object = MibTableColumn
fgs2528kxPortQoSQ4Rx = _Fgs2528kxPortQoSQ4Rx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 10),
    _Fgs2528kxPortQoSQ4Rx_Type()
)
fgs2528kxPortQoSQ4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ4Rx.setStatus("current")
_Fgs2528kxPortQoSQ4Tx_Type = Counter64
_Fgs2528kxPortQoSQ4Tx_Object = MibTableColumn
fgs2528kxPortQoSQ4Tx = _Fgs2528kxPortQoSQ4Tx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 11),
    _Fgs2528kxPortQoSQ4Tx_Type()
)
fgs2528kxPortQoSQ4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ4Tx.setStatus("current")
_Fgs2528kxPortQoSQ5Rx_Type = Counter64
_Fgs2528kxPortQoSQ5Rx_Object = MibTableColumn
fgs2528kxPortQoSQ5Rx = _Fgs2528kxPortQoSQ5Rx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 12),
    _Fgs2528kxPortQoSQ5Rx_Type()
)
fgs2528kxPortQoSQ5Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ5Rx.setStatus("current")
_Fgs2528kxPortQoSQ5Tx_Type = Counter64
_Fgs2528kxPortQoSQ5Tx_Object = MibTableColumn
fgs2528kxPortQoSQ5Tx = _Fgs2528kxPortQoSQ5Tx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 13),
    _Fgs2528kxPortQoSQ5Tx_Type()
)
fgs2528kxPortQoSQ5Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ5Tx.setStatus("current")
_Fgs2528kxPortQoSQ6Rx_Type = Counter64
_Fgs2528kxPortQoSQ6Rx_Object = MibTableColumn
fgs2528kxPortQoSQ6Rx = _Fgs2528kxPortQoSQ6Rx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 14),
    _Fgs2528kxPortQoSQ6Rx_Type()
)
fgs2528kxPortQoSQ6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ6Rx.setStatus("current")
_Fgs2528kxPortQoSQ6Tx_Type = Counter64
_Fgs2528kxPortQoSQ6Tx_Object = MibTableColumn
fgs2528kxPortQoSQ6Tx = _Fgs2528kxPortQoSQ6Tx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 15),
    _Fgs2528kxPortQoSQ6Tx_Type()
)
fgs2528kxPortQoSQ6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ6Tx.setStatus("current")
_Fgs2528kxPortQoSQ7Rx_Type = Counter64
_Fgs2528kxPortQoSQ7Rx_Object = MibTableColumn
fgs2528kxPortQoSQ7Rx = _Fgs2528kxPortQoSQ7Rx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 16),
    _Fgs2528kxPortQoSQ7Rx_Type()
)
fgs2528kxPortQoSQ7Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ7Rx.setStatus("current")
_Fgs2528kxPortQoSQ7Tx_Type = Counter64
_Fgs2528kxPortQoSQ7Tx_Object = MibTableColumn
fgs2528kxPortQoSQ7Tx = _Fgs2528kxPortQoSQ7Tx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 3, 2, 1, 17),
    _Fgs2528kxPortQoSQ7Tx_Type()
)
fgs2528kxPortQoSQ7Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortQoSQ7Tx.setStatus("current")
_Fgs2528kxSFPInfoTable_Object = MibTable
fgs2528kxSFPInfoTable = _Fgs2528kxSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4)
)
if mibBuilder.loadTexts:
    fgs2528kxSFPInfoTable.setStatus("current")
_Fgs2528kxSFPInfoEntry_Object = MibTableRow
fgs2528kxSFPInfoEntry = _Fgs2528kxSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1)
)
fgs2528kxSFPInfoEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxSFPInfoEntry.setStatus("current")


class _Fgs2528kxSFPInfoIndex_Type(Integer32):
    """Custom type fgs2528kxSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxSFPInfoIndex_Type.__name__ = "Integer32"
_Fgs2528kxSFPInfoIndex_Object = MibTableColumn
fgs2528kxSFPInfoIndex = _Fgs2528kxSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 1),
    _Fgs2528kxSFPInfoIndex_Type()
)
fgs2528kxSFPInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxSFPInfoIndex.setStatus("current")
_Fgs2528kxSFPInfoPort_Type = DisplayString
_Fgs2528kxSFPInfoPort_Object = MibTableColumn
fgs2528kxSFPInfoPort = _Fgs2528kxSFPInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 2),
    _Fgs2528kxSFPInfoPort_Type()
)
fgs2528kxSFPInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPInfoPort.setStatus("current")
_Fgs2528kxSFPConnectorType_Type = DisplayString
_Fgs2528kxSFPConnectorType_Object = MibTableColumn
fgs2528kxSFPConnectorType = _Fgs2528kxSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 3),
    _Fgs2528kxSFPConnectorType_Type()
)
fgs2528kxSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPConnectorType.setStatus("current")
_Fgs2528kxSFPFiberType_Type = DisplayString
_Fgs2528kxSFPFiberType_Object = MibTableColumn
fgs2528kxSFPFiberType = _Fgs2528kxSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 4),
    _Fgs2528kxSFPFiberType_Type()
)
fgs2528kxSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPFiberType.setStatus("current")
_Fgs2528kxSFPTxCentralWavelength_Type = DisplayString
_Fgs2528kxSFPTxCentralWavelength_Object = MibTableColumn
fgs2528kxSFPTxCentralWavelength = _Fgs2528kxSFPTxCentralWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 5),
    _Fgs2528kxSFPTxCentralWavelength_Type()
)
fgs2528kxSFPTxCentralWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPTxCentralWavelength.setStatus("current")
_Fgs2528kxSFPBaudRate_Type = DisplayString
_Fgs2528kxSFPBaudRate_Object = MibTableColumn
fgs2528kxSFPBaudRate = _Fgs2528kxSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 6),
    _Fgs2528kxSFPBaudRate_Type()
)
fgs2528kxSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPBaudRate.setStatus("current")
_Fgs2528kxSFPVendorOUI_Type = DisplayString
_Fgs2528kxSFPVendorOUI_Object = MibTableColumn
fgs2528kxSFPVendorOUI = _Fgs2528kxSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 7),
    _Fgs2528kxSFPVendorOUI_Type()
)
fgs2528kxSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPVendorOUI.setStatus("current")
_Fgs2528kxSFPVendorName_Type = DisplayString
_Fgs2528kxSFPVendorName_Object = MibTableColumn
fgs2528kxSFPVendorName = _Fgs2528kxSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 8),
    _Fgs2528kxSFPVendorName_Type()
)
fgs2528kxSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPVendorName.setStatus("current")
_Fgs2528kxSFPVendorPN_Type = DisplayString
_Fgs2528kxSFPVendorPN_Object = MibTableColumn
fgs2528kxSFPVendorPN = _Fgs2528kxSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 9),
    _Fgs2528kxSFPVendorPN_Type()
)
fgs2528kxSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPVendorPN.setStatus("current")
_Fgs2528kxSFPVendorRev_Type = DisplayString
_Fgs2528kxSFPVendorRev_Object = MibTableColumn
fgs2528kxSFPVendorRev = _Fgs2528kxSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 10),
    _Fgs2528kxSFPVendorRev_Type()
)
fgs2528kxSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPVendorRev.setStatus("current")
_Fgs2528kxSFPVendorSN_Type = DisplayString
_Fgs2528kxSFPVendorSN_Object = MibTableColumn
fgs2528kxSFPVendorSN = _Fgs2528kxSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 11),
    _Fgs2528kxSFPVendorSN_Type()
)
fgs2528kxSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPVendorSN.setStatus("current")
_Fgs2528kxSFPDateCode_Type = DisplayString
_Fgs2528kxSFPDateCode_Object = MibTableColumn
fgs2528kxSFPDateCode = _Fgs2528kxSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 12),
    _Fgs2528kxSFPDateCode_Type()
)
fgs2528kxSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPDateCode.setStatus("current")
_Fgs2528kxSFPTemperature_Type = DisplayString
_Fgs2528kxSFPTemperature_Object = MibTableColumn
fgs2528kxSFPTemperature = _Fgs2528kxSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 13),
    _Fgs2528kxSFPTemperature_Type()
)
fgs2528kxSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPTemperature.setStatus("current")
_Fgs2528kxSFPVcc_Type = DisplayString
_Fgs2528kxSFPVcc_Object = MibTableColumn
fgs2528kxSFPVcc = _Fgs2528kxSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 14),
    _Fgs2528kxSFPVcc_Type()
)
fgs2528kxSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPVcc.setStatus("current")
_Fgs2528kxSFPMon1Bias_Type = DisplayString
_Fgs2528kxSFPMon1Bias_Object = MibTableColumn
fgs2528kxSFPMon1Bias = _Fgs2528kxSFPMon1Bias_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 15),
    _Fgs2528kxSFPMon1Bias_Type()
)
fgs2528kxSFPMon1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPMon1Bias.setStatus("current")
_Fgs2528kxSFPMon2TxPWR_Type = DisplayString
_Fgs2528kxSFPMon2TxPWR_Object = MibTableColumn
fgs2528kxSFPMon2TxPWR = _Fgs2528kxSFPMon2TxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 16),
    _Fgs2528kxSFPMon2TxPWR_Type()
)
fgs2528kxSFPMon2TxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPMon2TxPWR.setStatus("current")
_Fgs2528kxSFPMon3RxPWR_Type = DisplayString
_Fgs2528kxSFPMon3RxPWR_Object = MibTableColumn
fgs2528kxSFPMon3RxPWR = _Fgs2528kxSFPMon3RxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 1, 4, 1, 17),
    _Fgs2528kxSFPMon3RxPWR_Type()
)
fgs2528kxSFPMon3RxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSFPMon3RxPWR.setStatus("current")
_Fgs2528kxGARP_ObjectIdentity = ObjectIdentity
fgs2528kxGARP = _Fgs2528kxGARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3)
)
_Fgs2528kxGARPConfTable_Object = MibTable
fgs2528kxGARPConfTable = _Fgs2528kxGARPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fgs2528kxGARPConfTable.setStatus("current")
_Fgs2528kxGARPConfEntry_Object = MibTableRow
fgs2528kxGARPConfEntry = _Fgs2528kxGARPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 1, 1)
)
fgs2528kxGARPConfEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxGARPConfPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxGARPConfEntry.setStatus("current")


class _Fgs2528kxGARPConfPort_Type(Integer32):
    """Custom type fgs2528kxGARPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxGARPConfPort_Type.__name__ = "Integer32"
_Fgs2528kxGARPConfPort_Object = MibTableColumn
fgs2528kxGARPConfPort = _Fgs2528kxGARPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 1, 1, 1),
    _Fgs2528kxGARPConfPort_Type()
)
fgs2528kxGARPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxGARPConfPort.setStatus("current")


class _Fgs2528kxGARPJoinTimer_Type(Integer32):
    """Custom type fgs2528kxGARPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Fgs2528kxGARPJoinTimer_Type.__name__ = "Integer32"
_Fgs2528kxGARPJoinTimer_Object = MibTableColumn
fgs2528kxGARPJoinTimer = _Fgs2528kxGARPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 1, 1, 2),
    _Fgs2528kxGARPJoinTimer_Type()
)
fgs2528kxGARPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGARPJoinTimer.setStatus("current")


class _Fgs2528kxGARPLeaveTimer_Type(Integer32):
    """Custom type fgs2528kxGARPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_Fgs2528kxGARPLeaveTimer_Type.__name__ = "Integer32"
_Fgs2528kxGARPLeaveTimer_Object = MibTableColumn
fgs2528kxGARPLeaveTimer = _Fgs2528kxGARPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 1, 1, 3),
    _Fgs2528kxGARPLeaveTimer_Type()
)
fgs2528kxGARPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGARPLeaveTimer.setStatus("current")


class _Fgs2528kxGARPLeaveAllTimer_Type(Integer32):
    """Custom type fgs2528kxGARPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 50000),
    )


_Fgs2528kxGARPLeaveAllTimer_Type.__name__ = "Integer32"
_Fgs2528kxGARPLeaveAllTimer_Object = MibTableColumn
fgs2528kxGARPLeaveAllTimer = _Fgs2528kxGARPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 1, 1, 4),
    _Fgs2528kxGARPLeaveAllTimer_Type()
)
fgs2528kxGARPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGARPLeaveAllTimer.setStatus("current")


class _Fgs2528kxGARPApplicantion_Type(Integer32):
    """Custom type fgs2528kxGARPApplicantion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxGARPApplicantion_Type.__name__ = "Integer32"
_Fgs2528kxGARPApplicantion_Object = MibTableColumn
fgs2528kxGARPApplicantion = _Fgs2528kxGARPApplicantion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 1, 1, 5),
    _Fgs2528kxGARPApplicantion_Type()
)
fgs2528kxGARPApplicantion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGARPApplicantion.setStatus("current")


class _Fgs2528kxGARPAttributeType_Type(Integer32):
    """Custom type fgs2528kxGARPAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxGARPAttributeType_Type.__name__ = "Integer32"
_Fgs2528kxGARPAttributeType_Object = MibTableColumn
fgs2528kxGARPAttributeType = _Fgs2528kxGARPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 1, 1, 6),
    _Fgs2528kxGARPAttributeType_Type()
)
fgs2528kxGARPAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGARPAttributeType.setStatus("current")


class _Fgs2528kxGARPApplicant_Type(Integer32):
    """Custom type fgs2528kxGARPApplicant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxGARPApplicant_Type.__name__ = "Integer32"
_Fgs2528kxGARPApplicant_Object = MibTableColumn
fgs2528kxGARPApplicant = _Fgs2528kxGARPApplicant_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 1, 1, 7),
    _Fgs2528kxGARPApplicant_Type()
)
fgs2528kxGARPApplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGARPApplicant.setStatus("current")
_Fgs2528kxGARPStatisticsTable_Object = MibTable
fgs2528kxGARPStatisticsTable = _Fgs2528kxGARPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxGARPStatisticsTable.setStatus("current")
_Fgs2528kxGARPStatisticsEntry_Object = MibTableRow
fgs2528kxGARPStatisticsEntry = _Fgs2528kxGARPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 2, 1)
)
fgs2528kxGARPStatisticsEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxGARPStatisticsPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxGARPStatisticsEntry.setStatus("current")


class _Fgs2528kxGARPStatisticsPort_Type(Integer32):
    """Custom type fgs2528kxGARPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxGARPStatisticsPort_Type.__name__ = "Integer32"
_Fgs2528kxGARPStatisticsPort_Object = MibTableColumn
fgs2528kxGARPStatisticsPort = _Fgs2528kxGARPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 2, 1, 1),
    _Fgs2528kxGARPStatisticsPort_Type()
)
fgs2528kxGARPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxGARPStatisticsPort.setStatus("current")
_Fgs2528kxGARPStatisticsPeerMAC_Type = DisplayString
_Fgs2528kxGARPStatisticsPeerMAC_Object = MibTableColumn
fgs2528kxGARPStatisticsPeerMAC = _Fgs2528kxGARPStatisticsPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 2, 1, 2),
    _Fgs2528kxGARPStatisticsPeerMAC_Type()
)
fgs2528kxGARPStatisticsPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxGARPStatisticsPeerMAC.setStatus("current")
_Fgs2528kxGARPStatisticsFailedCount_Type = Counter32
_Fgs2528kxGARPStatisticsFailedCount_Object = MibTableColumn
fgs2528kxGARPStatisticsFailedCount = _Fgs2528kxGARPStatisticsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 3, 2, 1, 3),
    _Fgs2528kxGARPStatisticsFailedCount_Type()
)
fgs2528kxGARPStatisticsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxGARPStatisticsFailedCount.setStatus("current")
_Fgs2528kxGVRP_ObjectIdentity = ObjectIdentity
fgs2528kxGVRP = _Fgs2528kxGVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4)
)
_Fgs2528kxGVRPConf_ObjectIdentity = ObjectIdentity
fgs2528kxGVRPConf = _Fgs2528kxGVRPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 1)
)


class _Fgs2528kxGVRPMode_Type(Integer32):
    """Custom type fgs2528kxGVRPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxGVRPMode_Type.__name__ = "Integer32"
_Fgs2528kxGVRPMode_Object = MibScalar
fgs2528kxGVRPMode = _Fgs2528kxGVRPMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 1, 1),
    _Fgs2528kxGVRPMode_Type()
)
fgs2528kxGVRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGVRPMode.setStatus("current")
_Fgs2528kxGVRPConfTable_Object = MibTable
fgs2528kxGVRPConfTable = _Fgs2528kxGVRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxGVRPConfTable.setStatus("current")
_Fgs2528kxGVRPConfEntry_Object = MibTableRow
fgs2528kxGVRPConfEntry = _Fgs2528kxGVRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 1, 2, 1)
)
fgs2528kxGVRPConfEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxGVRPConfPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxGVRPConfEntry.setStatus("current")


class _Fgs2528kxGVRPConfPort_Type(Integer32):
    """Custom type fgs2528kxGVRPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxGVRPConfPort_Type.__name__ = "Integer32"
_Fgs2528kxGVRPConfPort_Object = MibTableColumn
fgs2528kxGVRPConfPort = _Fgs2528kxGVRPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 1, 2, 1, 1),
    _Fgs2528kxGVRPConfPort_Type()
)
fgs2528kxGVRPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxGVRPConfPort.setStatus("current")


class _Fgs2528kxGVRPConfPortMode_Type(Integer32):
    """Custom type fgs2528kxGVRPConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxGVRPConfPortMode_Type.__name__ = "Integer32"
_Fgs2528kxGVRPConfPortMode_Object = MibTableColumn
fgs2528kxGVRPConfPortMode = _Fgs2528kxGVRPConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 1, 2, 1, 2),
    _Fgs2528kxGVRPConfPortMode_Type()
)
fgs2528kxGVRPConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGVRPConfPortMode.setStatus("current")


class _Fgs2528kxGVRPConfPortRRole_Type(Integer32):
    """Custom type fgs2528kxGVRPConfPortRRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxGVRPConfPortRRole_Type.__name__ = "Integer32"
_Fgs2528kxGVRPConfPortRRole_Object = MibTableColumn
fgs2528kxGVRPConfPortRRole = _Fgs2528kxGVRPConfPortRRole_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 1, 2, 1, 3),
    _Fgs2528kxGVRPConfPortRRole_Type()
)
fgs2528kxGVRPConfPortRRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxGVRPConfPortRRole.setStatus("current")
_Fgs2528kxGVRPStatisticsTable_Object = MibTable
fgs2528kxGVRPStatisticsTable = _Fgs2528kxGVRPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxGVRPStatisticsTable.setStatus("current")
_Fgs2528kxGVRPStatisticsEntry_Object = MibTableRow
fgs2528kxGVRPStatisticsEntry = _Fgs2528kxGVRPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 2, 1)
)
fgs2528kxGVRPStatisticsEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxGVRPStatisticsPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxGVRPStatisticsEntry.setStatus("current")


class _Fgs2528kxGVRPStatisticsPort_Type(Integer32):
    """Custom type fgs2528kxGVRPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxGVRPStatisticsPort_Type.__name__ = "Integer32"
_Fgs2528kxGVRPStatisticsPort_Object = MibTableColumn
fgs2528kxGVRPStatisticsPort = _Fgs2528kxGVRPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 2, 1, 1),
    _Fgs2528kxGVRPStatisticsPort_Type()
)
fgs2528kxGVRPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxGVRPStatisticsPort.setStatus("current")
_Fgs2528kxGVRPStatisticsJoinTxCnt_Type = Counter32
_Fgs2528kxGVRPStatisticsJoinTxCnt_Object = MibTableColumn
fgs2528kxGVRPStatisticsJoinTxCnt = _Fgs2528kxGVRPStatisticsJoinTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 2, 1, 2),
    _Fgs2528kxGVRPStatisticsJoinTxCnt_Type()
)
fgs2528kxGVRPStatisticsJoinTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxGVRPStatisticsJoinTxCnt.setStatus("current")
_Fgs2528kxGVRPStatisticsLeaveTxCnt_Type = Counter32
_Fgs2528kxGVRPStatisticsLeaveTxCnt_Object = MibTableColumn
fgs2528kxGVRPStatisticsLeaveTxCnt = _Fgs2528kxGVRPStatisticsLeaveTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 4, 2, 1, 3),
    _Fgs2528kxGVRPStatisticsLeaveTxCnt_Type()
)
fgs2528kxGVRPStatisticsLeaveTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxGVRPStatisticsLeaveTxCnt.setStatus("current")
_Fgs2528kxThermalProtection_ObjectIdentity = ObjectIdentity
fgs2528kxThermalProtection = _Fgs2528kxThermalProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5)
)


class _Fgs2528kxPriority0Temperature_Type(Integer32):
    """Custom type fgs2528kxPriority0Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fgs2528kxPriority0Temperature_Type.__name__ = "Integer32"
_Fgs2528kxPriority0Temperature_Object = MibScalar
fgs2528kxPriority0Temperature = _Fgs2528kxPriority0Temperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 1),
    _Fgs2528kxPriority0Temperature_Type()
)
fgs2528kxPriority0Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPriority0Temperature.setStatus("current")


class _Fgs2528kxPriority1Temperature_Type(Integer32):
    """Custom type fgs2528kxPriority1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fgs2528kxPriority1Temperature_Type.__name__ = "Integer32"
_Fgs2528kxPriority1Temperature_Object = MibScalar
fgs2528kxPriority1Temperature = _Fgs2528kxPriority1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 2),
    _Fgs2528kxPriority1Temperature_Type()
)
fgs2528kxPriority1Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPriority1Temperature.setStatus("current")


class _Fgs2528kxPriority2Temperature_Type(Integer32):
    """Custom type fgs2528kxPriority2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fgs2528kxPriority2Temperature_Type.__name__ = "Integer32"
_Fgs2528kxPriority2Temperature_Object = MibScalar
fgs2528kxPriority2Temperature = _Fgs2528kxPriority2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 3),
    _Fgs2528kxPriority2Temperature_Type()
)
fgs2528kxPriority2Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPriority2Temperature.setStatus("current")


class _Fgs2528kxPriority3Temperature_Type(Integer32):
    """Custom type fgs2528kxPriority3Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fgs2528kxPriority3Temperature_Type.__name__ = "Integer32"
_Fgs2528kxPriority3Temperature_Object = MibScalar
fgs2528kxPriority3Temperature = _Fgs2528kxPriority3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 4),
    _Fgs2528kxPriority3Temperature_Type()
)
fgs2528kxPriority3Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPriority3Temperature.setStatus("current")
_Fgs2528kxThermalProtectionTable_Object = MibTable
fgs2528kxThermalProtectionTable = _Fgs2528kxThermalProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 5)
)
if mibBuilder.loadTexts:
    fgs2528kxThermalProtectionTable.setStatus("current")
_Fgs2528kxThermalProtectionEntry_Object = MibTableRow
fgs2528kxThermalProtectionEntry = _Fgs2528kxThermalProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 5, 1)
)
fgs2528kxThermalProtectionEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxThermalProtectionPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxThermalProtectionEntry.setStatus("current")


class _Fgs2528kxThermalProtectionPort_Type(Integer32):
    """Custom type fgs2528kxThermalProtectionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxThermalProtectionPort_Type.__name__ = "Integer32"
_Fgs2528kxThermalProtectionPort_Object = MibTableColumn
fgs2528kxThermalProtectionPort = _Fgs2528kxThermalProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 5, 1, 1),
    _Fgs2528kxThermalProtectionPort_Type()
)
fgs2528kxThermalProtectionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxThermalProtectionPort.setStatus("current")


class _Fgs2528kxThermalProtectionPortTemperature_Type(Integer32):
    """Custom type fgs2528kxThermalProtectionPortTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fgs2528kxThermalProtectionPortTemperature_Type.__name__ = "Integer32"
_Fgs2528kxThermalProtectionPortTemperature_Object = MibTableColumn
fgs2528kxThermalProtectionPortTemperature = _Fgs2528kxThermalProtectionPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 5, 1, 2),
    _Fgs2528kxThermalProtectionPortTemperature_Type()
)
fgs2528kxThermalProtectionPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxThermalProtectionPortTemperature.setStatus("current")


class _Fgs2528kxThermalProtectionPortPriority_Type(Integer32):
    """Custom type fgs2528kxThermalProtectionPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxThermalProtectionPortPriority_Type.__name__ = "Integer32"
_Fgs2528kxThermalProtectionPortPriority_Object = MibTableColumn
fgs2528kxThermalProtectionPortPriority = _Fgs2528kxThermalProtectionPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 5, 1, 3),
    _Fgs2528kxThermalProtectionPortPriority_Type()
)
fgs2528kxThermalProtectionPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxThermalProtectionPortPriority.setStatus("current")
_Fgs2528kxThermalProtectionPortStatus_Type = DisplayString
_Fgs2528kxThermalProtectionPortStatus_Object = MibTableColumn
fgs2528kxThermalProtectionPortStatus = _Fgs2528kxThermalProtectionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 5, 5, 1, 4),
    _Fgs2528kxThermalProtectionPortStatus_Type()
)
fgs2528kxThermalProtectionPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxThermalProtectionPortStatus.setStatus("current")
_Fgs2528kxMirroring_ObjectIdentity = ObjectIdentity
fgs2528kxMirroring = _Fgs2528kxMirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 6)
)


class _Fgs2528kxPortToMirrorOn_Type(Integer32):
    """Custom type fgs2528kxPortToMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Fgs2528kxPortToMirrorOn_Type.__name__ = "Integer32"
_Fgs2528kxPortToMirrorOn_Object = MibScalar
fgs2528kxPortToMirrorOn = _Fgs2528kxPortToMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 6, 1),
    _Fgs2528kxPortToMirrorOn_Type()
)
fgs2528kxPortToMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortToMirrorOn.setStatus("current")
_Fgs2528kxMirrorTable_Object = MibTable
fgs2528kxMirrorTable = _Fgs2528kxMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 6, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxMirrorTable.setStatus("current")
_Fgs2528kxMirrorEntry_Object = MibTableRow
fgs2528kxMirrorEntry = _Fgs2528kxMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 6, 2, 1)
)
fgs2528kxMirrorEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxMirrorPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxMirrorEntry.setStatus("current")


class _Fgs2528kxMirrorPort_Type(Integer32):
    """Custom type fgs2528kxMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxMirrorPort_Type.__name__ = "Integer32"
_Fgs2528kxMirrorPort_Object = MibTableColumn
fgs2528kxMirrorPort = _Fgs2528kxMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 6, 2, 1, 1),
    _Fgs2528kxMirrorPort_Type()
)
fgs2528kxMirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxMirrorPort.setStatus("current")


class _Fgs2528kxMirrorMode_Type(Integer32):
    """Custom type fgs2528kxMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxMirrorMode_Type.__name__ = "Integer32"
_Fgs2528kxMirrorMode_Object = MibTableColumn
fgs2528kxMirrorMode = _Fgs2528kxMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 6, 2, 1, 2),
    _Fgs2528kxMirrorMode_Type()
)
fgs2528kxMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxMirrorMode.setStatus("current")
_Fgs2528kxTrapEventSeverity_ObjectIdentity = ObjectIdentity
fgs2528kxTrapEventSeverity = _Fgs2528kxTrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7)
)


class _Fgs2528kxTrapEventSeverityACL_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityACL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityACL_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityACL_Object = MibScalar
fgs2528kxTrapEventSeverityACL = _Fgs2528kxTrapEventSeverityACL_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 1),
    _Fgs2528kxTrapEventSeverityACL_Type()
)
fgs2528kxTrapEventSeverityACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityACL.setStatus("current")


class _Fgs2528kxTrapEventSeverityACLLog_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityACLLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityACLLog_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityACLLog_Object = MibScalar
fgs2528kxTrapEventSeverityACLLog = _Fgs2528kxTrapEventSeverityACLLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 2),
    _Fgs2528kxTrapEventSeverityACLLog_Type()
)
fgs2528kxTrapEventSeverityACLLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityACLLog.setStatus("current")


class _Fgs2528kxTrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityAccessMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityAccessMgmt_Object = MibScalar
fgs2528kxTrapEventSeverityAccessMgmt = _Fgs2528kxTrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 3),
    _Fgs2528kxTrapEventSeverityAccessMgmt_Type()
)
fgs2528kxTrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityAccessMgmt.setStatus("current")


class _Fgs2528kxTrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityAuthFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityAuthFailed_Object = MibScalar
fgs2528kxTrapEventSeverityAuthFailed = _Fgs2528kxTrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 4),
    _Fgs2528kxTrapEventSeverityAuthFailed_Type()
)
fgs2528kxTrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityAuthFailed.setStatus("current")


class _Fgs2528kxTrapEventSeverityColdStart_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityColdStart_Object = MibScalar
fgs2528kxTrapEventSeverityColdStart = _Fgs2528kxTrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 5),
    _Fgs2528kxTrapEventSeverityColdStart_Type()
)
fgs2528kxTrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityColdStart.setStatus("current")


class _Fgs2528kxTrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityConfigInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityConfigInfo_Object = MibScalar
fgs2528kxTrapEventSeverityConfigInfo = _Fgs2528kxTrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 6),
    _Fgs2528kxTrapEventSeverityConfigInfo_Type()
)
fgs2528kxTrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityConfigInfo.setStatus("current")


class _Fgs2528kxTrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityFirmwareUpgrade_Object = MibScalar
fgs2528kxTrapEventSeverityFirmwareUpgrade = _Fgs2528kxTrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 7),
    _Fgs2528kxTrapEventSeverityFirmwareUpgrade_Type()
)
fgs2528kxTrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Fgs2528kxTrapEventSeverityImportExport_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityImportExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityImportExport_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityImportExport_Object = MibScalar
fgs2528kxTrapEventSeverityImportExport = _Fgs2528kxTrapEventSeverityImportExport_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 8),
    _Fgs2528kxTrapEventSeverityImportExport_Type()
)
fgs2528kxTrapEventSeverityImportExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityImportExport.setStatus("current")


class _Fgs2528kxTrapEventSeverityLACP_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityLACP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityLACP_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityLACP_Object = MibScalar
fgs2528kxTrapEventSeverityLACP = _Fgs2528kxTrapEventSeverityLACP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 9),
    _Fgs2528kxTrapEventSeverityLACP_Type()
)
fgs2528kxTrapEventSeverityLACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityLACP.setStatus("current")


class _Fgs2528kxTrapEventSeverityLinkStatus_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityLinkStatus_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityLinkStatus_Object = MibScalar
fgs2528kxTrapEventSeverityLinkStatus = _Fgs2528kxTrapEventSeverityLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 10),
    _Fgs2528kxTrapEventSeverityLinkStatus_Type()
)
fgs2528kxTrapEventSeverityLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityLinkStatus.setStatus("current")


class _Fgs2528kxTrapEventSeverityLogin_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityLogin_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityLogin_Object = MibScalar
fgs2528kxTrapEventSeverityLogin = _Fgs2528kxTrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 11),
    _Fgs2528kxTrapEventSeverityLogin_Type()
)
fgs2528kxTrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityLogin.setStatus("current")


class _Fgs2528kxTrapEventSeverityLogout_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityLogout_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityLogout_Object = MibScalar
fgs2528kxTrapEventSeverityLogout = _Fgs2528kxTrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 12),
    _Fgs2528kxTrapEventSeverityLogout_Type()
)
fgs2528kxTrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityLogout.setStatus("current")


class _Fgs2528kxTrapEventSeverityLoopProtect_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityLoopProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityLoopProtect_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityLoopProtect_Object = MibScalar
fgs2528kxTrapEventSeverityLoopProtect = _Fgs2528kxTrapEventSeverityLoopProtect_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 13),
    _Fgs2528kxTrapEventSeverityLoopProtect_Type()
)
fgs2528kxTrapEventSeverityLoopProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityLoopProtect.setStatus("current")


class _Fgs2528kxTrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityMgmtIPChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityMgmtIPChange_Object = MibScalar
fgs2528kxTrapEventSeverityMgmtIPChange = _Fgs2528kxTrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 14),
    _Fgs2528kxTrapEventSeverityMgmtIPChange_Type()
)
fgs2528kxTrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityMgmtIPChange.setStatus("current")


class _Fgs2528kxTrapEventSeverityModuleChange_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityModuleChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityModuleChange_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityModuleChange_Object = MibScalar
fgs2528kxTrapEventSeverityModuleChange = _Fgs2528kxTrapEventSeverityModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 15),
    _Fgs2528kxTrapEventSeverityModuleChange_Type()
)
fgs2528kxTrapEventSeverityModuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityModuleChange.setStatus("current")


class _Fgs2528kxTrapEventSeverityNAS_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityNAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityNAS_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityNAS_Object = MibScalar
fgs2528kxTrapEventSeverityNAS = _Fgs2528kxTrapEventSeverityNAS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 16),
    _Fgs2528kxTrapEventSeverityNAS_Type()
)
fgs2528kxTrapEventSeverityNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityNAS.setStatus("current")


class _Fgs2528kxTrapEventSeverityPasswdChange_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityPasswdChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityPasswdChange_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityPasswdChange_Object = MibScalar
fgs2528kxTrapEventSeverityPasswdChange = _Fgs2528kxTrapEventSeverityPasswdChange_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 17),
    _Fgs2528kxTrapEventSeverityPasswdChange_Type()
)
fgs2528kxTrapEventSeverityPasswdChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityPasswdChange.setStatus("current")


class _Fgs2528kxTrapEventSeverityPortSecurity_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityPortSecurity_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityPortSecurity_Object = MibScalar
fgs2528kxTrapEventSeverityPortSecurity = _Fgs2528kxTrapEventSeverityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 18),
    _Fgs2528kxTrapEventSeverityPortSecurity_Type()
)
fgs2528kxTrapEventSeverityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityPortSecurity.setStatus("current")


class _Fgs2528kxTrapEventSeverityThermalProtect_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityThermalProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityThermalProtect_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityThermalProtect_Object = MibScalar
fgs2528kxTrapEventSeverityThermalProtect = _Fgs2528kxTrapEventSeverityThermalProtect_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 19),
    _Fgs2528kxTrapEventSeverityThermalProtect_Type()
)
fgs2528kxTrapEventSeverityThermalProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityThermalProtect.setStatus("current")


class _Fgs2528kxTrapEventSeverityVLAN_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityVLAN_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityVLAN_Object = MibScalar
fgs2528kxTrapEventSeverityVLAN = _Fgs2528kxTrapEventSeverityVLAN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 20),
    _Fgs2528kxTrapEventSeverityVLAN_Type()
)
fgs2528kxTrapEventSeverityVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityVLAN.setStatus("current")


class _Fgs2528kxTrapEventSeverityWarmStart_Type(Integer32):
    """Custom type fgs2528kxTrapEventSeverityWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxTrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Fgs2528kxTrapEventSeverityWarmStart_Object = MibScalar
fgs2528kxTrapEventSeverityWarmStart = _Fgs2528kxTrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 7, 21),
    _Fgs2528kxTrapEventSeverityWarmStart_Type()
)
fgs2528kxTrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTrapEventSeverityWarmStart.setStatus("current")
_Fgs2528kxSMTP_ObjectIdentity = ObjectIdentity
fgs2528kxSMTP = _Fgs2528kxSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8)
)
_Fgs2528kxSMTPMailServer_Type = DisplayString
_Fgs2528kxSMTPMailServer_Object = MibScalar
fgs2528kxSMTPMailServer = _Fgs2528kxSMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 1),
    _Fgs2528kxSMTPMailServer_Type()
)
fgs2528kxSMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPMailServer.setStatus("current")
_Fgs2528kxSMTPUserName_Type = DisplayString
_Fgs2528kxSMTPUserName_Object = MibScalar
fgs2528kxSMTPUserName = _Fgs2528kxSMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 2),
    _Fgs2528kxSMTPUserName_Type()
)
fgs2528kxSMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPUserName.setStatus("current")
_Fgs2528kxSMTPPassword_Type = DisplayString
_Fgs2528kxSMTPPassword_Object = MibScalar
fgs2528kxSMTPPassword = _Fgs2528kxSMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 3),
    _Fgs2528kxSMTPPassword_Type()
)
fgs2528kxSMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPPassword.setStatus("current")


class _Fgs2528kxSMTPServeriryLevel_Type(Integer32):
    """Custom type fgs2528kxSMTPServeriryLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Fgs2528kxSMTPServeriryLevel_Type.__name__ = "Integer32"
_Fgs2528kxSMTPServeriryLevel_Object = MibScalar
fgs2528kxSMTPServeriryLevel = _Fgs2528kxSMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 4),
    _Fgs2528kxSMTPServeriryLevel_Type()
)
fgs2528kxSMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPServeriryLevel.setStatus("current")
_Fgs2528kxSMTPSender_Type = DisplayString
_Fgs2528kxSMTPSender_Object = MibScalar
fgs2528kxSMTPSender = _Fgs2528kxSMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 5),
    _Fgs2528kxSMTPSender_Type()
)
fgs2528kxSMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPSender.setStatus("current")
_Fgs2528kxSMTPReturnPath_Type = DisplayString
_Fgs2528kxSMTPReturnPath_Object = MibScalar
fgs2528kxSMTPReturnPath = _Fgs2528kxSMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 6),
    _Fgs2528kxSMTPReturnPath_Type()
)
fgs2528kxSMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPReturnPath.setStatus("current")
_Fgs2528kxSMTPEmailAddress1_Type = DisplayString
_Fgs2528kxSMTPEmailAddress1_Object = MibScalar
fgs2528kxSMTPEmailAddress1 = _Fgs2528kxSMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 7),
    _Fgs2528kxSMTPEmailAddress1_Type()
)
fgs2528kxSMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPEmailAddress1.setStatus("current")
_Fgs2528kxSMTPEmailAddress2_Type = DisplayString
_Fgs2528kxSMTPEmailAddress2_Object = MibScalar
fgs2528kxSMTPEmailAddress2 = _Fgs2528kxSMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 8),
    _Fgs2528kxSMTPEmailAddress2_Type()
)
fgs2528kxSMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPEmailAddress2.setStatus("current")
_Fgs2528kxSMTPEmailAddress3_Type = DisplayString
_Fgs2528kxSMTPEmailAddress3_Object = MibScalar
fgs2528kxSMTPEmailAddress3 = _Fgs2528kxSMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 9),
    _Fgs2528kxSMTPEmailAddress3_Type()
)
fgs2528kxSMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPEmailAddress3.setStatus("current")
_Fgs2528kxSMTPEmailAddress4_Type = DisplayString
_Fgs2528kxSMTPEmailAddress4_Object = MibScalar
fgs2528kxSMTPEmailAddress4 = _Fgs2528kxSMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 10),
    _Fgs2528kxSMTPEmailAddress4_Type()
)
fgs2528kxSMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPEmailAddress4.setStatus("current")
_Fgs2528kxSMTPEmailAddress5_Type = DisplayString
_Fgs2528kxSMTPEmailAddress5_Object = MibScalar
fgs2528kxSMTPEmailAddress5 = _Fgs2528kxSMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 11),
    _Fgs2528kxSMTPEmailAddress5_Type()
)
fgs2528kxSMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPEmailAddress5.setStatus("current")
_Fgs2528kxSMTPEmailAddress6_Type = DisplayString
_Fgs2528kxSMTPEmailAddress6_Object = MibScalar
fgs2528kxSMTPEmailAddress6 = _Fgs2528kxSMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 8, 12),
    _Fgs2528kxSMTPEmailAddress6_Type()
)
fgs2528kxSMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSMTPEmailAddress6.setStatus("current")
_Fgs2528kxACL_ObjectIdentity = ObjectIdentity
fgs2528kxACL = _Fgs2528kxACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9)
)
_Fgs2528kxACLPortsConfTable_Object = MibTable
fgs2528kxACLPortsConfTable = _Fgs2528kxACLPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1)
)
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfTable.setStatus("current")
_Fgs2528kxACLPortsConfEntry_Object = MibTableRow
fgs2528kxACLPortsConfEntry = _Fgs2528kxACLPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1)
)
fgs2528kxACLPortsConfEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxACLPortsConfPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfEntry.setStatus("current")


class _Fgs2528kxACLPortsConfPort_Type(Integer32):
    """Custom type fgs2528kxACLPortsConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxACLPortsConfPort_Type.__name__ = "Integer32"
_Fgs2528kxACLPortsConfPort_Object = MibTableColumn
fgs2528kxACLPortsConfPort = _Fgs2528kxACLPortsConfPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1, 1),
    _Fgs2528kxACLPortsConfPort_Type()
)
fgs2528kxACLPortsConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfPort.setStatus("current")


class _Fgs2528kxACLPortsConfPolicyID_Type(Integer32):
    """Custom type fgs2528kxACLPortsConfPolicyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fgs2528kxACLPortsConfPolicyID_Type.__name__ = "Integer32"
_Fgs2528kxACLPortsConfPolicyID_Object = MibTableColumn
fgs2528kxACLPortsConfPolicyID = _Fgs2528kxACLPortsConfPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1, 2),
    _Fgs2528kxACLPortsConfPolicyID_Type()
)
fgs2528kxACLPortsConfPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfPolicyID.setStatus("current")


class _Fgs2528kxACLPortsConfAction_Type(Integer32):
    """Custom type fgs2528kxACLPortsConfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLPortsConfAction_Type.__name__ = "Integer32"
_Fgs2528kxACLPortsConfAction_Object = MibTableColumn
fgs2528kxACLPortsConfAction = _Fgs2528kxACLPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1, 3),
    _Fgs2528kxACLPortsConfAction_Type()
)
fgs2528kxACLPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfAction.setStatus("current")


class _Fgs2528kxACLPortsConfRateLimiterID_Type(Integer32):
    """Custom type fgs2528kxACLPortsConfRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Fgs2528kxACLPortsConfRateLimiterID_Type.__name__ = "Integer32"
_Fgs2528kxACLPortsConfRateLimiterID_Object = MibTableColumn
fgs2528kxACLPortsConfRateLimiterID = _Fgs2528kxACLPortsConfRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1, 4),
    _Fgs2528kxACLPortsConfRateLimiterID_Type()
)
fgs2528kxACLPortsConfRateLimiterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfRateLimiterID.setStatus("current")


class _Fgs2528kxACLPortsConfPortRedirect_Type(Integer32):
    """Custom type fgs2528kxACLPortsConfPortRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Fgs2528kxACLPortsConfPortRedirect_Type.__name__ = "Integer32"
_Fgs2528kxACLPortsConfPortRedirect_Object = MibTableColumn
fgs2528kxACLPortsConfPortRedirect = _Fgs2528kxACLPortsConfPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1, 5),
    _Fgs2528kxACLPortsConfPortRedirect_Type()
)
fgs2528kxACLPortsConfPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfPortRedirect.setStatus("current")


class _Fgs2528kxACLPortsConfLogging_Type(Integer32):
    """Custom type fgs2528kxACLPortsConfLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLPortsConfLogging_Type.__name__ = "Integer32"
_Fgs2528kxACLPortsConfLogging_Object = MibTableColumn
fgs2528kxACLPortsConfLogging = _Fgs2528kxACLPortsConfLogging_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1, 7),
    _Fgs2528kxACLPortsConfLogging_Type()
)
fgs2528kxACLPortsConfLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfLogging.setStatus("current")


class _Fgs2528kxACLPortsConfShutdown_Type(Integer32):
    """Custom type fgs2528kxACLPortsConfShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLPortsConfShutdown_Type.__name__ = "Integer32"
_Fgs2528kxACLPortsConfShutdown_Object = MibTableColumn
fgs2528kxACLPortsConfShutdown = _Fgs2528kxACLPortsConfShutdown_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1, 8),
    _Fgs2528kxACLPortsConfShutdown_Type()
)
fgs2528kxACLPortsConfShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfShutdown.setStatus("current")


class _Fgs2528kxACLPortsConfState_Type(Integer32):
    """Custom type fgs2528kxACLPortsConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLPortsConfState_Type.__name__ = "Integer32"
_Fgs2528kxACLPortsConfState_Object = MibTableColumn
fgs2528kxACLPortsConfState = _Fgs2528kxACLPortsConfState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1, 9),
    _Fgs2528kxACLPortsConfState_Type()
)
fgs2528kxACLPortsConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfState.setStatus("current")
_Fgs2528kxACLPortsConfCounter_Type = Counter32
_Fgs2528kxACLPortsConfCounter_Object = MibTableColumn
fgs2528kxACLPortsConfCounter = _Fgs2528kxACLPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 1, 1, 10),
    _Fgs2528kxACLPortsConfCounter_Type()
)
fgs2528kxACLPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLPortsConfCounter.setStatus("current")
_Fgs2528kxACLRateLimiterTable_Object = MibTable
fgs2528kxACLRateLimiterTable = _Fgs2528kxACLRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxACLRateLimiterTable.setStatus("current")
_Fgs2528kxACLRateLimiterEntry_Object = MibTableRow
fgs2528kxACLRateLimiterEntry = _Fgs2528kxACLRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 2, 1)
)
fgs2528kxACLRateLimiterEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxACLRateLimiterID"),
)
if mibBuilder.loadTexts:
    fgs2528kxACLRateLimiterEntry.setStatus("current")


class _Fgs2528kxACLRateLimiterID_Type(Integer32):
    """Custom type fgs2528kxACLRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Fgs2528kxACLRateLimiterID_Type.__name__ = "Integer32"
_Fgs2528kxACLRateLimiterID_Object = MibTableColumn
fgs2528kxACLRateLimiterID = _Fgs2528kxACLRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 2, 1, 1),
    _Fgs2528kxACLRateLimiterID_Type()
)
fgs2528kxACLRateLimiterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxACLRateLimiterID.setStatus("current")


class _Fgs2528kxACLRateLimiterRate_Type(Integer32):
    """Custom type fgs2528kxACLRateLimiterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_Fgs2528kxACLRateLimiterRate_Type.__name__ = "Integer32"
_Fgs2528kxACLRateLimiterRate_Object = MibTableColumn
fgs2528kxACLRateLimiterRate = _Fgs2528kxACLRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 2, 1, 3),
    _Fgs2528kxACLRateLimiterRate_Type()
)
fgs2528kxACLRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLRateLimiterRate.setStatus("current")
_Fgs2528kxACLACE_ObjectIdentity = ObjectIdentity
fgs2528kxACLACE = _Fgs2528kxACLACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3)
)


class _Fgs2528kxACLACECreate_Type(Integer32):
    """Custom type fgs2528kxACLACECreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLACECreate_Type.__name__ = "Integer32"
_Fgs2528kxACLACECreate_Object = MibScalar
fgs2528kxACLACECreate = _Fgs2528kxACLACECreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 1),
    _Fgs2528kxACLACECreate_Type()
)
fgs2528kxACLACECreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACECreate.setStatus("current")
_Fgs2528kxACLACETable_Object = MibTable
fgs2528kxACLACETable = _Fgs2528kxACLACETable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxACLACETable.setStatus("current")
_Fgs2528kxACLACEEntry_Object = MibTableRow
fgs2528kxACLACEEntry = _Fgs2528kxACLACEEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1)
)
fgs2528kxACLACEEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxACLACEIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxACLACEEntry.setStatus("current")


class _Fgs2528kxACLACEIndex_Type(Integer32):
    """Custom type fgs2528kxACLACEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Fgs2528kxACLACEIndex_Type.__name__ = "Integer32"
_Fgs2528kxACLACEIndex_Object = MibTableColumn
fgs2528kxACLACEIndex = _Fgs2528kxACLACEIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 1),
    _Fgs2528kxACLACEIndex_Type()
)
fgs2528kxACLACEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxACLACEIndex.setStatus("current")


class _Fgs2528kxACLACEID_Type(Integer32):
    """Custom type fgs2528kxACLACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Fgs2528kxACLACEID_Type.__name__ = "Integer32"
_Fgs2528kxACLACEID_Object = MibTableColumn
fgs2528kxACLACEID = _Fgs2528kxACLACEID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 2),
    _Fgs2528kxACLACEID_Type()
)
fgs2528kxACLACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEID.setStatus("current")


class _Fgs2528kxACLACENextID_Type(Integer32):
    """Custom type fgs2528kxACLACENextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Fgs2528kxACLACENextID_Type.__name__ = "Integer32"
_Fgs2528kxACLACENextID_Object = MibTableColumn
fgs2528kxACLACENextID = _Fgs2528kxACLACENextID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 3),
    _Fgs2528kxACLACENextID_Type()
)
fgs2528kxACLACENextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACENextID.setStatus("current")
_Fgs2528kxACLACEIngressPort_Type = DisplayString
_Fgs2528kxACLACEIngressPort_Object = MibTableColumn
fgs2528kxACLACEIngressPort = _Fgs2528kxACLACEIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 4),
    _Fgs2528kxACLACEIngressPort_Type()
)
fgs2528kxACLACEIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEIngressPort.setStatus("current")


class _Fgs2528kxACLACEPortPolicyNumber_Type(Integer32):
    """Custom type fgs2528kxACLACEPortPolicyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fgs2528kxACLACEPortPolicyNumber_Type.__name__ = "Integer32"
_Fgs2528kxACLACEPortPolicyNumber_Object = MibTableColumn
fgs2528kxACLACEPortPolicyNumber = _Fgs2528kxACLACEPortPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 5),
    _Fgs2528kxACLACEPortPolicyNumber_Type()
)
fgs2528kxACLACEPortPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEPortPolicyNumber.setStatus("current")


class _Fgs2528kxACLACEPortPolicyBitmask_Type(Integer32):
    """Custom type fgs2528kxACLACEPortPolicyBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fgs2528kxACLACEPortPolicyBitmask_Type.__name__ = "Integer32"
_Fgs2528kxACLACEPortPolicyBitmask_Object = MibTableColumn
fgs2528kxACLACEPortPolicyBitmask = _Fgs2528kxACLACEPortPolicyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 6),
    _Fgs2528kxACLACEPortPolicyBitmask_Type()
)
fgs2528kxACLACEPortPolicyBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEPortPolicyBitmask.setStatus("current")


class _Fgs2528kxACLACEFrameType_Type(Integer32):
    """Custom type fgs2528kxACLACEFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Fgs2528kxACLACEFrameType_Type.__name__ = "Integer32"
_Fgs2528kxACLACEFrameType_Object = MibTableColumn
fgs2528kxACLACEFrameType = _Fgs2528kxACLACEFrameType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 7),
    _Fgs2528kxACLACEFrameType_Type()
)
fgs2528kxACLACEFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEFrameType.setStatus("current")


class _Fgs2528kxACLACEAction_Type(Integer32):
    """Custom type fgs2528kxACLACEAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLACEAction_Type.__name__ = "Integer32"
_Fgs2528kxACLACEAction_Object = MibTableColumn
fgs2528kxACLACEAction = _Fgs2528kxACLACEAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 8),
    _Fgs2528kxACLACEAction_Type()
)
fgs2528kxACLACEAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEAction.setStatus("current")
_Fgs2528kxACLACEDenyPortRedirect_Type = DisplayString
_Fgs2528kxACLACEDenyPortRedirect_Object = MibTableColumn
fgs2528kxACLACEDenyPortRedirect = _Fgs2528kxACLACEDenyPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 9),
    _Fgs2528kxACLACEDenyPortRedirect_Type()
)
fgs2528kxACLACEDenyPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEDenyPortRedirect.setStatus("current")


class _Fgs2528kxACLACELogging_Type(Integer32):
    """Custom type fgs2528kxACLACELogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLACELogging_Type.__name__ = "Integer32"
_Fgs2528kxACLACELogging_Object = MibTableColumn
fgs2528kxACLACELogging = _Fgs2528kxACLACELogging_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 10),
    _Fgs2528kxACLACELogging_Type()
)
fgs2528kxACLACELogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACELogging.setStatus("current")


class _Fgs2528kxACLACERateLimiter_Type(Integer32):
    """Custom type fgs2528kxACLACERateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Fgs2528kxACLACERateLimiter_Type.__name__ = "Integer32"
_Fgs2528kxACLACERateLimiter_Object = MibTableColumn
fgs2528kxACLACERateLimiter = _Fgs2528kxACLACERateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 12),
    _Fgs2528kxACLACERateLimiter_Type()
)
fgs2528kxACLACERateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACERateLimiter.setStatus("current")


class _Fgs2528kxACLACEShutdown_Type(Integer32):
    """Custom type fgs2528kxACLACEShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLACEShutdown_Type.__name__ = "Integer32"
_Fgs2528kxACLACEShutdown_Object = MibTableColumn
fgs2528kxACLACEShutdown = _Fgs2528kxACLACEShutdown_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 13),
    _Fgs2528kxACLACEShutdown_Type()
)
fgs2528kxACLACEShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEShutdown.setStatus("current")


class _Fgs2528kxACLACEVLANTagPriority_Type(Integer32):
    """Custom type fgs2528kxACLACEVLANTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Fgs2528kxACLACEVLANTagPriority_Type.__name__ = "Integer32"
_Fgs2528kxACLACEVLANTagPriority_Object = MibTableColumn
fgs2528kxACLACEVLANTagPriority = _Fgs2528kxACLACEVLANTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 15),
    _Fgs2528kxACLACEVLANTagPriority_Type()
)
fgs2528kxACLACEVLANTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEVLANTagPriority.setStatus("current")


class _Fgs2528kxACLACEVLANVID_Type(Integer32):
    """Custom type fgs2528kxACLACEVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Fgs2528kxACLACEVLANVID_Type.__name__ = "Integer32"
_Fgs2528kxACLACEVLANVID_Object = MibTableColumn
fgs2528kxACLACEVLANVID = _Fgs2528kxACLACEVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 16),
    _Fgs2528kxACLACEVLANVID_Type()
)
fgs2528kxACLACEVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEVLANVID.setStatus("current")


class _Fgs2528kxACLACEEtherType_Type(Integer32):
    """Custom type fgs2528kxACLACEEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fgs2528kxACLACEEtherType_Type.__name__ = "Integer32"
_Fgs2528kxACLACEEtherType_Object = MibTableColumn
fgs2528kxACLACEEtherType = _Fgs2528kxACLACEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 17),
    _Fgs2528kxACLACEEtherType_Type()
)
fgs2528kxACLACEEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEEtherType.setStatus("current")
_Fgs2528kxACLACESMAC_Type = DisplayString
_Fgs2528kxACLACESMAC_Object = MibTableColumn
fgs2528kxACLACESMAC = _Fgs2528kxACLACESMAC_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 18),
    _Fgs2528kxACLACESMAC_Type()
)
fgs2528kxACLACESMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACESMAC.setStatus("current")


class _Fgs2528kxACLACEDMACType_Type(Integer32):
    """Custom type fgs2528kxACLACEDMACType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Fgs2528kxACLACEDMACType_Type.__name__ = "Integer32"
_Fgs2528kxACLACEDMACType_Object = MibTableColumn
fgs2528kxACLACEDMACType = _Fgs2528kxACLACEDMACType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 19),
    _Fgs2528kxACLACEDMACType_Type()
)
fgs2528kxACLACEDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEDMACType.setStatus("current")
_Fgs2528kxACLACEDMAC_Type = DisplayString
_Fgs2528kxACLACEDMAC_Object = MibTableColumn
fgs2528kxACLACEDMAC = _Fgs2528kxACLACEDMAC_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 20),
    _Fgs2528kxACLACEDMAC_Type()
)
fgs2528kxACLACEDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEDMAC.setStatus("current")


class _Fgs2528kxACLACEArpOpcode_Type(Integer32):
    """Custom type fgs2528kxACLACEArpOpcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxACLACEArpOpcode_Type.__name__ = "Integer32"
_Fgs2528kxACLACEArpOpcode_Object = MibTableColumn
fgs2528kxACLACEArpOpcode = _Fgs2528kxACLACEArpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 21),
    _Fgs2528kxACLACEArpOpcode_Type()
)
fgs2528kxACLACEArpOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEArpOpcode.setStatus("current")


class _Fgs2528kxACLACEArpFlagsRequestReply_Type(Integer32):
    """Custom type fgs2528kxACLACEArpFlagsRequestReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACEArpFlagsRequestReply_Type.__name__ = "Integer32"
_Fgs2528kxACLACEArpFlagsRequestReply_Object = MibTableColumn
fgs2528kxACLACEArpFlagsRequestReply = _Fgs2528kxACLACEArpFlagsRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 22),
    _Fgs2528kxACLACEArpFlagsRequestReply_Type()
)
fgs2528kxACLACEArpFlagsRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEArpFlagsRequestReply.setStatus("current")


class _Fgs2528kxACLACEArpFlagsArpSmac_Type(Integer32):
    """Custom type fgs2528kxACLACEArpFlagsArpSmac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACEArpFlagsArpSmac_Type.__name__ = "Integer32"
_Fgs2528kxACLACEArpFlagsArpSmac_Object = MibTableColumn
fgs2528kxACLACEArpFlagsArpSmac = _Fgs2528kxACLACEArpFlagsArpSmac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 23),
    _Fgs2528kxACLACEArpFlagsArpSmac_Type()
)
fgs2528kxACLACEArpFlagsArpSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEArpFlagsArpSmac.setStatus("current")


class _Fgs2528kxACLACEArpFlagsRarpDmac_Type(Integer32):
    """Custom type fgs2528kxACLACEArpFlagsRarpDmac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACEArpFlagsRarpDmac_Type.__name__ = "Integer32"
_Fgs2528kxACLACEArpFlagsRarpDmac_Object = MibTableColumn
fgs2528kxACLACEArpFlagsRarpDmac = _Fgs2528kxACLACEArpFlagsRarpDmac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 24),
    _Fgs2528kxACLACEArpFlagsRarpDmac_Type()
)
fgs2528kxACLACEArpFlagsRarpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEArpFlagsRarpDmac.setStatus("current")


class _Fgs2528kxACLACEArpFlagsLength_Type(Integer32):
    """Custom type fgs2528kxACLACEArpFlagsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACEArpFlagsLength_Type.__name__ = "Integer32"
_Fgs2528kxACLACEArpFlagsLength_Object = MibTableColumn
fgs2528kxACLACEArpFlagsLength = _Fgs2528kxACLACEArpFlagsLength_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 25),
    _Fgs2528kxACLACEArpFlagsLength_Type()
)
fgs2528kxACLACEArpFlagsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEArpFlagsLength.setStatus("current")


class _Fgs2528kxACLACEArpFlagsIp_Type(Integer32):
    """Custom type fgs2528kxACLACEArpFlagsIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACEArpFlagsIp_Type.__name__ = "Integer32"
_Fgs2528kxACLACEArpFlagsIp_Object = MibTableColumn
fgs2528kxACLACEArpFlagsIp = _Fgs2528kxACLACEArpFlagsIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 26),
    _Fgs2528kxACLACEArpFlagsIp_Type()
)
fgs2528kxACLACEArpFlagsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEArpFlagsIp.setStatus("current")


class _Fgs2528kxACLACEArpFlagsEthernet_Type(Integer32):
    """Custom type fgs2528kxACLACEArpFlagsEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACEArpFlagsEthernet_Type.__name__ = "Integer32"
_Fgs2528kxACLACEArpFlagsEthernet_Object = MibTableColumn
fgs2528kxACLACEArpFlagsEthernet = _Fgs2528kxACLACEArpFlagsEthernet_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 27),
    _Fgs2528kxACLACEArpFlagsEthernet_Type()
)
fgs2528kxACLACEArpFlagsEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEArpFlagsEthernet.setStatus("current")


class _Fgs2528kxACLACESIPType_Type(Integer32):
    """Custom type fgs2528kxACLACESIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLACESIPType_Type.__name__ = "Integer32"
_Fgs2528kxACLACESIPType_Object = MibTableColumn
fgs2528kxACLACESIPType = _Fgs2528kxACLACESIPType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 28),
    _Fgs2528kxACLACESIPType_Type()
)
fgs2528kxACLACESIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACESIPType.setStatus("current")
_Fgs2528kxACLACESIPIPAddress_Type = IpAddress
_Fgs2528kxACLACESIPIPAddress_Object = MibTableColumn
fgs2528kxACLACESIPIPAddress = _Fgs2528kxACLACESIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 29),
    _Fgs2528kxACLACESIPIPAddress_Type()
)
fgs2528kxACLACESIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACESIPIPAddress.setStatus("current")


class _Fgs2528kxACLACESIPNetworkPrefix_Type(Integer32):
    """Custom type fgs2528kxACLACESIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fgs2528kxACLACESIPNetworkPrefix_Type.__name__ = "Integer32"
_Fgs2528kxACLACESIPNetworkPrefix_Object = MibTableColumn
fgs2528kxACLACESIPNetworkPrefix = _Fgs2528kxACLACESIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 30),
    _Fgs2528kxACLACESIPNetworkPrefix_Type()
)
fgs2528kxACLACESIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACESIPNetworkPrefix.setStatus("current")


class _Fgs2528kxACLACEDIPType_Type(Integer32):
    """Custom type fgs2528kxACLACEDIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLACEDIPType_Type.__name__ = "Integer32"
_Fgs2528kxACLACEDIPType_Object = MibTableColumn
fgs2528kxACLACEDIPType = _Fgs2528kxACLACEDIPType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 32),
    _Fgs2528kxACLACEDIPType_Type()
)
fgs2528kxACLACEDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEDIPType.setStatus("current")
_Fgs2528kxACLACEDIPIPAddress_Type = IpAddress
_Fgs2528kxACLACEDIPIPAddress_Object = MibTableColumn
fgs2528kxACLACEDIPIPAddress = _Fgs2528kxACLACEDIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 33),
    _Fgs2528kxACLACEDIPIPAddress_Type()
)
fgs2528kxACLACEDIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEDIPIPAddress.setStatus("current")


class _Fgs2528kxACLACEDIPNetworkPrefix_Type(Integer32):
    """Custom type fgs2528kxACLACEDIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fgs2528kxACLACEDIPNetworkPrefix_Type.__name__ = "Integer32"
_Fgs2528kxACLACEDIPNetworkPrefix_Object = MibTableColumn
fgs2528kxACLACEDIPNetworkPrefix = _Fgs2528kxACLACEDIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 34),
    _Fgs2528kxACLACEDIPNetworkPrefix_Type()
)
fgs2528kxACLACEDIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEDIPNetworkPrefix.setStatus("current")


class _Fgs2528kxACLACEIPProtocol_Type(Integer32):
    """Custom type fgs2528kxACLACEIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Fgs2528kxACLACEIPProtocol_Type.__name__ = "Integer32"
_Fgs2528kxACLACEIPProtocol_Object = MibTableColumn
fgs2528kxACLACEIPProtocol = _Fgs2528kxACLACEIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 36),
    _Fgs2528kxACLACEIPProtocol_Type()
)
fgs2528kxACLACEIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEIPProtocol.setStatus("current")


class _Fgs2528kxACLACEIPFlagsTTL_Type(Integer32):
    """Custom type fgs2528kxACLACEIPFlagsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACEIPFlagsTTL_Type.__name__ = "Integer32"
_Fgs2528kxACLACEIPFlagsTTL_Object = MibTableColumn
fgs2528kxACLACEIPFlagsTTL = _Fgs2528kxACLACEIPFlagsTTL_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 37),
    _Fgs2528kxACLACEIPFlagsTTL_Type()
)
fgs2528kxACLACEIPFlagsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEIPFlagsTTL.setStatus("current")


class _Fgs2528kxACLACEIPFlagsOptions_Type(Integer32):
    """Custom type fgs2528kxACLACEIPFlagsOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACEIPFlagsOptions_Type.__name__ = "Integer32"
_Fgs2528kxACLACEIPFlagsOptions_Object = MibTableColumn
fgs2528kxACLACEIPFlagsOptions = _Fgs2528kxACLACEIPFlagsOptions_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 38),
    _Fgs2528kxACLACEIPFlagsOptions_Type()
)
fgs2528kxACLACEIPFlagsOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEIPFlagsOptions.setStatus("current")


class _Fgs2528kxACLACEIPFlagsFragment_Type(Integer32):
    """Custom type fgs2528kxACLACEIPFlagsFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACEIPFlagsFragment_Type.__name__ = "Integer32"
_Fgs2528kxACLACEIPFlagsFragment_Object = MibTableColumn
fgs2528kxACLACEIPFlagsFragment = _Fgs2528kxACLACEIPFlagsFragment_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 39),
    _Fgs2528kxACLACEIPFlagsFragment_Type()
)
fgs2528kxACLACEIPFlagsFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEIPFlagsFragment.setStatus("current")


class _Fgs2528kxACLACEICMPType_Type(Integer32):
    """Custom type fgs2528kxACLACEICMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Fgs2528kxACLACEICMPType_Type.__name__ = "Integer32"
_Fgs2528kxACLACEICMPType_Object = MibTableColumn
fgs2528kxACLACEICMPType = _Fgs2528kxACLACEICMPType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 40),
    _Fgs2528kxACLACEICMPType_Type()
)
fgs2528kxACLACEICMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEICMPType.setStatus("current")


class _Fgs2528kxACLACEICMPCode_Type(Integer32):
    """Custom type fgs2528kxACLACEICMPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Fgs2528kxACLACEICMPCode_Type.__name__ = "Integer32"
_Fgs2528kxACLACEICMPCode_Object = MibTableColumn
fgs2528kxACLACEICMPCode = _Fgs2528kxACLACEICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 41),
    _Fgs2528kxACLACEICMPCode_Type()
)
fgs2528kxACLACEICMPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEICMPCode.setStatus("current")


class _Fgs2528kxACLACESourcePortMin_Type(Integer32):
    """Custom type fgs2528kxACLACESourcePortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fgs2528kxACLACESourcePortMin_Type.__name__ = "Integer32"
_Fgs2528kxACLACESourcePortMin_Object = MibTableColumn
fgs2528kxACLACESourcePortMin = _Fgs2528kxACLACESourcePortMin_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 42),
    _Fgs2528kxACLACESourcePortMin_Type()
)
fgs2528kxACLACESourcePortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACESourcePortMin.setStatus("current")


class _Fgs2528kxACLACESourcePortMax_Type(Integer32):
    """Custom type fgs2528kxACLACESourcePortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fgs2528kxACLACESourcePortMax_Type.__name__ = "Integer32"
_Fgs2528kxACLACESourcePortMax_Object = MibTableColumn
fgs2528kxACLACESourcePortMax = _Fgs2528kxACLACESourcePortMax_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 43),
    _Fgs2528kxACLACESourcePortMax_Type()
)
fgs2528kxACLACESourcePortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACESourcePortMax.setStatus("current")


class _Fgs2528kxACLACEDestPortMin_Type(Integer32):
    """Custom type fgs2528kxACLACEDestPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fgs2528kxACLACEDestPortMin_Type.__name__ = "Integer32"
_Fgs2528kxACLACEDestPortMin_Object = MibTableColumn
fgs2528kxACLACEDestPortMin = _Fgs2528kxACLACEDestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 44),
    _Fgs2528kxACLACEDestPortMin_Type()
)
fgs2528kxACLACEDestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEDestPortMin.setStatus("current")


class _Fgs2528kxACLACEDestPortMax_Type(Integer32):
    """Custom type fgs2528kxACLACEDestPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fgs2528kxACLACEDestPortMax_Type.__name__ = "Integer32"
_Fgs2528kxACLACEDestPortMax_Object = MibTableColumn
fgs2528kxACLACEDestPortMax = _Fgs2528kxACLACEDestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 45),
    _Fgs2528kxACLACEDestPortMax_Type()
)
fgs2528kxACLACEDestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEDestPortMax.setStatus("current")


class _Fgs2528kxACLACETCPFlagsFin_Type(Integer32):
    """Custom type fgs2528kxACLACETCPFlagsFin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACETCPFlagsFin_Type.__name__ = "Integer32"
_Fgs2528kxACLACETCPFlagsFin_Object = MibTableColumn
fgs2528kxACLACETCPFlagsFin = _Fgs2528kxACLACETCPFlagsFin_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 46),
    _Fgs2528kxACLACETCPFlagsFin_Type()
)
fgs2528kxACLACETCPFlagsFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACETCPFlagsFin.setStatus("current")


class _Fgs2528kxACLACETCPFlagsSyn_Type(Integer32):
    """Custom type fgs2528kxACLACETCPFlagsSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACETCPFlagsSyn_Type.__name__ = "Integer32"
_Fgs2528kxACLACETCPFlagsSyn_Object = MibTableColumn
fgs2528kxACLACETCPFlagsSyn = _Fgs2528kxACLACETCPFlagsSyn_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 47),
    _Fgs2528kxACLACETCPFlagsSyn_Type()
)
fgs2528kxACLACETCPFlagsSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACETCPFlagsSyn.setStatus("current")


class _Fgs2528kxACLACETCPFlagsRst_Type(Integer32):
    """Custom type fgs2528kxACLACETCPFlagsRst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACETCPFlagsRst_Type.__name__ = "Integer32"
_Fgs2528kxACLACETCPFlagsRst_Object = MibTableColumn
fgs2528kxACLACETCPFlagsRst = _Fgs2528kxACLACETCPFlagsRst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 48),
    _Fgs2528kxACLACETCPFlagsRst_Type()
)
fgs2528kxACLACETCPFlagsRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACETCPFlagsRst.setStatus("current")


class _Fgs2528kxACLACETCPFlagsPsh_Type(Integer32):
    """Custom type fgs2528kxACLACETCPFlagsPsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACETCPFlagsPsh_Type.__name__ = "Integer32"
_Fgs2528kxACLACETCPFlagsPsh_Object = MibTableColumn
fgs2528kxACLACETCPFlagsPsh = _Fgs2528kxACLACETCPFlagsPsh_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 49),
    _Fgs2528kxACLACETCPFlagsPsh_Type()
)
fgs2528kxACLACETCPFlagsPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACETCPFlagsPsh.setStatus("current")


class _Fgs2528kxACLACETCPFlagsAck_Type(Integer32):
    """Custom type fgs2528kxACLACETCPFlagsAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACETCPFlagsAck_Type.__name__ = "Integer32"
_Fgs2528kxACLACETCPFlagsAck_Object = MibTableColumn
fgs2528kxACLACETCPFlagsAck = _Fgs2528kxACLACETCPFlagsAck_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 50),
    _Fgs2528kxACLACETCPFlagsAck_Type()
)
fgs2528kxACLACETCPFlagsAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACETCPFlagsAck.setStatus("current")


class _Fgs2528kxACLACETCPFlagsUrg_Type(Integer32):
    """Custom type fgs2528kxACLACETCPFlagsUrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxACLACETCPFlagsUrg_Type.__name__ = "Integer32"
_Fgs2528kxACLACETCPFlagsUrg_Object = MibTableColumn
fgs2528kxACLACETCPFlagsUrg = _Fgs2528kxACLACETCPFlagsUrg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 51),
    _Fgs2528kxACLACETCPFlagsUrg_Type()
)
fgs2528kxACLACETCPFlagsUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACETCPFlagsUrg.setStatus("current")


class _Fgs2528kxACLACERowStatus_Type(Integer32):
    """Custom type fgs2528kxACLACERowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Fgs2528kxACLACERowStatus_Type.__name__ = "Integer32"
_Fgs2528kxACLACERowStatus_Object = MibTableColumn
fgs2528kxACLACERowStatus = _Fgs2528kxACLACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 2, 1, 66),
    _Fgs2528kxACLACERowStatus_Type()
)
fgs2528kxACLACERowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACERowStatus.setStatus("current")


class _Fgs2528kxACLACEClear_Type(Integer32):
    """Custom type fgs2528kxACLACEClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxACLACEClear_Type.__name__ = "Integer32"
_Fgs2528kxACLACEClear_Object = MibScalar
fgs2528kxACLACEClear = _Fgs2528kxACLACEClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 3),
    _Fgs2528kxACLACEClear_Type()
)
fgs2528kxACLACEClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEClear.setStatus("current")


class _Fgs2528kxACLACEMoveACEID_Type(Integer32):
    """Custom type fgs2528kxACLACEMoveACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Fgs2528kxACLACEMoveACEID_Type.__name__ = "Integer32"
_Fgs2528kxACLACEMoveACEID_Object = MibScalar
fgs2528kxACLACEMoveACEID = _Fgs2528kxACLACEMoveACEID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 4),
    _Fgs2528kxACLACEMoveACEID_Type()
)
fgs2528kxACLACEMoveACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEMoveACEID.setStatus("current")


class _Fgs2528kxACLACEMoveNextACEID_Type(Integer32):
    """Custom type fgs2528kxACLACEMoveNextACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Fgs2528kxACLACEMoveNextACEID_Type.__name__ = "Integer32"
_Fgs2528kxACLACEMoveNextACEID_Object = MibScalar
fgs2528kxACLACEMoveNextACEID = _Fgs2528kxACLACEMoveNextACEID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 5),
    _Fgs2528kxACLACEMoveNextACEID_Type()
)
fgs2528kxACLACEMoveNextACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxACLACEMoveNextACEID.setStatus("current")
_Fgs2528kxACLACEStatusTable_Object = MibTable
fgs2528kxACLACEStatusTable = _Fgs2528kxACLACEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusTable.setStatus("current")
_Fgs2528kxACLACEStatusEntry_Object = MibTableRow
fgs2528kxACLACEStatusEntry = _Fgs2528kxACLACEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1)
)
fgs2528kxACLACEStatusEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxACLACEStatusIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusEntry.setStatus("current")


class _Fgs2528kxACLACEStatusIndex_Type(Integer32):
    """Custom type fgs2528kxACLACEStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Fgs2528kxACLACEStatusIndex_Type.__name__ = "Integer32"
_Fgs2528kxACLACEStatusIndex_Object = MibTableColumn
fgs2528kxACLACEStatusIndex = _Fgs2528kxACLACEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 1),
    _Fgs2528kxACLACEStatusIndex_Type()
)
fgs2528kxACLACEStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusIndex.setStatus("current")
_Fgs2528kxACLACEStatusUser_Type = DisplayString
_Fgs2528kxACLACEStatusUser_Object = MibTableColumn
fgs2528kxACLACEStatusUser = _Fgs2528kxACLACEStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 2),
    _Fgs2528kxACLACEStatusUser_Type()
)
fgs2528kxACLACEStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusUser.setStatus("current")


class _Fgs2528kxACLACEStatusID_Type(Integer32):
    """Custom type fgs2528kxACLACEStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Fgs2528kxACLACEStatusID_Type.__name__ = "Integer32"
_Fgs2528kxACLACEStatusID_Object = MibTableColumn
fgs2528kxACLACEStatusID = _Fgs2528kxACLACEStatusID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 3),
    _Fgs2528kxACLACEStatusID_Type()
)
fgs2528kxACLACEStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusID.setStatus("current")
_Fgs2528kxACLACEStatusIngressPort_Type = DisplayString
_Fgs2528kxACLACEStatusIngressPort_Object = MibTableColumn
fgs2528kxACLACEStatusIngressPort = _Fgs2528kxACLACEStatusIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 4),
    _Fgs2528kxACLACEStatusIngressPort_Type()
)
fgs2528kxACLACEStatusIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusIngressPort.setStatus("current")
_Fgs2528kxACLACEStatusFrameType_Type = DisplayString
_Fgs2528kxACLACEStatusFrameType_Object = MibTableColumn
fgs2528kxACLACEStatusFrameType = _Fgs2528kxACLACEStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 5),
    _Fgs2528kxACLACEStatusFrameType_Type()
)
fgs2528kxACLACEStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusFrameType.setStatus("current")
_Fgs2528kxACLACEStatusAction_Type = DisplayString
_Fgs2528kxACLACEStatusAction_Object = MibTableColumn
fgs2528kxACLACEStatusAction = _Fgs2528kxACLACEStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 6),
    _Fgs2528kxACLACEStatusAction_Type()
)
fgs2528kxACLACEStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusAction.setStatus("current")
_Fgs2528kxACLACEStatusRateLimiter_Type = DisplayString
_Fgs2528kxACLACEStatusRateLimiter_Object = MibTableColumn
fgs2528kxACLACEStatusRateLimiter = _Fgs2528kxACLACEStatusRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 7),
    _Fgs2528kxACLACEStatusRateLimiter_Type()
)
fgs2528kxACLACEStatusRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusRateLimiter.setStatus("current")
_Fgs2528kxACLACEStatusPortCopy_Type = DisplayString
_Fgs2528kxACLACEStatusPortCopy_Object = MibTableColumn
fgs2528kxACLACEStatusPortCopy = _Fgs2528kxACLACEStatusPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 8),
    _Fgs2528kxACLACEStatusPortCopy_Type()
)
fgs2528kxACLACEStatusPortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusPortCopy.setStatus("current")
_Fgs2528kxACLACEStatusMirror_Type = DisplayString
_Fgs2528kxACLACEStatusMirror_Object = MibTableColumn
fgs2528kxACLACEStatusMirror = _Fgs2528kxACLACEStatusMirror_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 9),
    _Fgs2528kxACLACEStatusMirror_Type()
)
fgs2528kxACLACEStatusMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusMirror.setStatus("current")
_Fgs2528kxACLACEStatusCPU_Type = DisplayString
_Fgs2528kxACLACEStatusCPU_Object = MibTableColumn
fgs2528kxACLACEStatusCPU = _Fgs2528kxACLACEStatusCPU_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 10),
    _Fgs2528kxACLACEStatusCPU_Type()
)
fgs2528kxACLACEStatusCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusCPU.setStatus("current")
_Fgs2528kxACLACEStatusCounter_Type = Counter32
_Fgs2528kxACLACEStatusCounter_Object = MibTableColumn
fgs2528kxACLACEStatusCounter = _Fgs2528kxACLACEStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 11),
    _Fgs2528kxACLACEStatusCounter_Type()
)
fgs2528kxACLACEStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusCounter.setStatus("current")
_Fgs2528kxACLACEStatusConflict_Type = DisplayString
_Fgs2528kxACLACEStatusConflict_Object = MibTableColumn
fgs2528kxACLACEStatusConflict = _Fgs2528kxACLACEStatusConflict_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 9, 3, 6, 1, 12),
    _Fgs2528kxACLACEStatusConflict_Type()
)
fgs2528kxACLACEStatusConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxACLACEStatusConflict.setStatus("current")
_Fgs2528kxERPS_ObjectIdentity = ObjectIdentity
fgs2528kxERPS = _Fgs2528kxERPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10)
)
_Fgs2528kxERPSConf_ObjectIdentity = ObjectIdentity
fgs2528kxERPSConf = _Fgs2528kxERPSConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1)
)


class _Fgs2528kxERPSConfCreate_Type(Integer32):
    """Custom type fgs2528kxERPSConfCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxERPSConfCreate_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfCreate_Object = MibScalar
fgs2528kxERPSConfCreate = _Fgs2528kxERPSConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 1),
    _Fgs2528kxERPSConfCreate_Type()
)
fgs2528kxERPSConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfCreate.setStatus("current")
_Fgs2528kxERPSConfTable_Object = MibTable
fgs2528kxERPSConfTable = _Fgs2528kxERPSConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxERPSConfTable.setStatus("current")
_Fgs2528kxERPSConfEntry_Object = MibTableRow
fgs2528kxERPSConfEntry = _Fgs2528kxERPSConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1)
)
fgs2528kxERPSConfEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxERPSConfIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxERPSConfEntry.setStatus("current")


class _Fgs2528kxERPSConfIndex_Type(Integer32):
    """Custom type fgs2528kxERPSConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Fgs2528kxERPSConfIndex_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfIndex_Object = MibTableColumn
fgs2528kxERPSConfIndex = _Fgs2528kxERPSConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 1),
    _Fgs2528kxERPSConfIndex_Type()
)
fgs2528kxERPSConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfIndex.setStatus("current")


class _Fgs2528kxERPSConfERPSID_Type(Integer32):
    """Custom type fgs2528kxERPSConfERPSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Fgs2528kxERPSConfERPSID_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfERPSID_Object = MibTableColumn
fgs2528kxERPSConfERPSID = _Fgs2528kxERPSConfERPSID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 2),
    _Fgs2528kxERPSConfERPSID_Type()
)
fgs2528kxERPSConfERPSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfERPSID.setStatus("current")


class _Fgs2528kxERPSConfPort0_Type(Integer32):
    """Custom type fgs2528kxERPSConfPort0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Fgs2528kxERPSConfPort0_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfPort0_Object = MibTableColumn
fgs2528kxERPSConfPort0 = _Fgs2528kxERPSConfPort0_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 3),
    _Fgs2528kxERPSConfPort0_Type()
)
fgs2528kxERPSConfPort0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfPort0.setStatus("current")


class _Fgs2528kxERPSConfPort1_Type(Integer32):
    """Custom type fgs2528kxERPSConfPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_Fgs2528kxERPSConfPort1_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfPort1_Object = MibTableColumn
fgs2528kxERPSConfPort1 = _Fgs2528kxERPSConfPort1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 4),
    _Fgs2528kxERPSConfPort1_Type()
)
fgs2528kxERPSConfPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfPort1.setStatus("current")


class _Fgs2528kxERPSConfPort0SFMEP_Type(Integer32):
    """Custom type fgs2528kxERPSConfPort0SFMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fgs2528kxERPSConfPort0SFMEP_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfPort0SFMEP_Object = MibTableColumn
fgs2528kxERPSConfPort0SFMEP = _Fgs2528kxERPSConfPort0SFMEP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 5),
    _Fgs2528kxERPSConfPort0SFMEP_Type()
)
fgs2528kxERPSConfPort0SFMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfPort0SFMEP.setStatus("current")


class _Fgs2528kxERPSConfPort1SFMEP_Type(Integer32):
    """Custom type fgs2528kxERPSConfPort1SFMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fgs2528kxERPSConfPort1SFMEP_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfPort1SFMEP_Object = MibTableColumn
fgs2528kxERPSConfPort1SFMEP = _Fgs2528kxERPSConfPort1SFMEP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 6),
    _Fgs2528kxERPSConfPort1SFMEP_Type()
)
fgs2528kxERPSConfPort1SFMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfPort1SFMEP.setStatus("current")


class _Fgs2528kxERPSConfPort0APSMEP_Type(Integer32):
    """Custom type fgs2528kxERPSConfPort0APSMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fgs2528kxERPSConfPort0APSMEP_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfPort0APSMEP_Object = MibTableColumn
fgs2528kxERPSConfPort0APSMEP = _Fgs2528kxERPSConfPort0APSMEP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 7),
    _Fgs2528kxERPSConfPort0APSMEP_Type()
)
fgs2528kxERPSConfPort0APSMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfPort0APSMEP.setStatus("current")


class _Fgs2528kxERPSConfPort1APSMEP_Type(Integer32):
    """Custom type fgs2528kxERPSConfPort1APSMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fgs2528kxERPSConfPort1APSMEP_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfPort1APSMEP_Object = MibTableColumn
fgs2528kxERPSConfPort1APSMEP = _Fgs2528kxERPSConfPort1APSMEP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 8),
    _Fgs2528kxERPSConfPort1APSMEP_Type()
)
fgs2528kxERPSConfPort1APSMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfPort1APSMEP.setStatus("current")


class _Fgs2528kxERPSConfRingType_Type(Integer32):
    """Custom type fgs2528kxERPSConfRingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxERPSConfRingType_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfRingType_Object = MibTableColumn
fgs2528kxERPSConfRingType = _Fgs2528kxERPSConfRingType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 9),
    _Fgs2528kxERPSConfRingType_Type()
)
fgs2528kxERPSConfRingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfRingType.setStatus("current")


class _Fgs2528kxERPSConfInterconnectedNode_Type(Integer32):
    """Custom type fgs2528kxERPSConfInterconnectedNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxERPSConfInterconnectedNode_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfInterconnectedNode_Object = MibTableColumn
fgs2528kxERPSConfInterconnectedNode = _Fgs2528kxERPSConfInterconnectedNode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 10),
    _Fgs2528kxERPSConfInterconnectedNode_Type()
)
fgs2528kxERPSConfInterconnectedNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfInterconnectedNode.setStatus("current")


class _Fgs2528kxERPSConfVirtualChannel_Type(Integer32):
    """Custom type fgs2528kxERPSConfVirtualChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxERPSConfVirtualChannel_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfVirtualChannel_Object = MibTableColumn
fgs2528kxERPSConfVirtualChannel = _Fgs2528kxERPSConfVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 11),
    _Fgs2528kxERPSConfVirtualChannel_Type()
)
fgs2528kxERPSConfVirtualChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfVirtualChannel.setStatus("current")


class _Fgs2528kxERPSConfMajorRingID_Type(Integer32):
    """Custom type fgs2528kxERPSConfMajorRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Fgs2528kxERPSConfMajorRingID_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfMajorRingID_Object = MibTableColumn
fgs2528kxERPSConfMajorRingID = _Fgs2528kxERPSConfMajorRingID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 12),
    _Fgs2528kxERPSConfMajorRingID_Type()
)
fgs2528kxERPSConfMajorRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfMajorRingID.setStatus("current")


class _Fgs2528kxERPSConfAlarm_Type(DisplayString):
    """Custom type fgs2528kxERPSConfAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Fgs2528kxERPSConfAlarm_Type.__name__ = "DisplayString"
_Fgs2528kxERPSConfAlarm_Object = MibTableColumn
fgs2528kxERPSConfAlarm = _Fgs2528kxERPSConfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 13),
    _Fgs2528kxERPSConfAlarm_Type()
)
fgs2528kxERPSConfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfAlarm.setStatus("current")


class _Fgs2528kxERPSInstanceConfConfigured_Type(DisplayString):
    """Custom type fgs2528kxERPSInstanceConfConfigured based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Fgs2528kxERPSInstanceConfConfigured_Type.__name__ = "DisplayString"
_Fgs2528kxERPSInstanceConfConfigured_Object = MibTableColumn
fgs2528kxERPSInstanceConfConfigured = _Fgs2528kxERPSInstanceConfConfigured_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 14),
    _Fgs2528kxERPSInstanceConfConfigured_Type()
)
fgs2528kxERPSInstanceConfConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxERPSInstanceConfConfigured.setStatus("current")


class _Fgs2528kxERPSInstanceConfGuardTime_Type(Integer32):
    """Custom type fgs2528kxERPSInstanceConfGuardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_Fgs2528kxERPSInstanceConfGuardTime_Type.__name__ = "Integer32"
_Fgs2528kxERPSInstanceConfGuardTime_Object = MibTableColumn
fgs2528kxERPSInstanceConfGuardTime = _Fgs2528kxERPSInstanceConfGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 15),
    _Fgs2528kxERPSInstanceConfGuardTime_Type()
)
fgs2528kxERPSInstanceConfGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSInstanceConfGuardTime.setStatus("current")


class _Fgs2528kxERPSInstanceConfWTRTime_Type(Integer32):
    """Custom type fgs2528kxERPSInstanceConfWTRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Fgs2528kxERPSInstanceConfWTRTime_Type.__name__ = "Integer32"
_Fgs2528kxERPSInstanceConfWTRTime_Object = MibTableColumn
fgs2528kxERPSInstanceConfWTRTime = _Fgs2528kxERPSInstanceConfWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 16),
    _Fgs2528kxERPSInstanceConfWTRTime_Type()
)
fgs2528kxERPSInstanceConfWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSInstanceConfWTRTime.setStatus("current")


class _Fgs2528kxERPSInstanceConfHoldOffTime_Type(Integer32):
    """Custom type fgs2528kxERPSInstanceConfHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Fgs2528kxERPSInstanceConfHoldOffTime_Type.__name__ = "Integer32"
_Fgs2528kxERPSInstanceConfHoldOffTime_Object = MibTableColumn
fgs2528kxERPSInstanceConfHoldOffTime = _Fgs2528kxERPSInstanceConfHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 17),
    _Fgs2528kxERPSInstanceConfHoldOffTime_Type()
)
fgs2528kxERPSInstanceConfHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSInstanceConfHoldOffTime.setStatus("current")


class _Fgs2528kxERPSInstanceConfVersion_Type(Integer32):
    """Custom type fgs2528kxERPSInstanceConfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxERPSInstanceConfVersion_Type.__name__ = "Integer32"
_Fgs2528kxERPSInstanceConfVersion_Object = MibTableColumn
fgs2528kxERPSInstanceConfVersion = _Fgs2528kxERPSInstanceConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 18),
    _Fgs2528kxERPSInstanceConfVersion_Type()
)
fgs2528kxERPSInstanceConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSInstanceConfVersion.setStatus("current")


class _Fgs2528kxERPSInstanceConfRevertive_Type(Integer32):
    """Custom type fgs2528kxERPSInstanceConfRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxERPSInstanceConfRevertive_Type.__name__ = "Integer32"
_Fgs2528kxERPSInstanceConfRevertive_Object = MibTableColumn
fgs2528kxERPSInstanceConfRevertive = _Fgs2528kxERPSInstanceConfRevertive_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 19),
    _Fgs2528kxERPSInstanceConfRevertive_Type()
)
fgs2528kxERPSInstanceConfRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSInstanceConfRevertive.setStatus("current")


class _Fgs2528kxERPSInstanceConfVLANconfig_Type(DisplayString):
    """Custom type fgs2528kxERPSInstanceConfVLANconfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Fgs2528kxERPSInstanceConfVLANconfig_Type.__name__ = "DisplayString"
_Fgs2528kxERPSInstanceConfVLANconfig_Object = MibTableColumn
fgs2528kxERPSInstanceConfVLANconfig = _Fgs2528kxERPSInstanceConfVLANconfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 20),
    _Fgs2528kxERPSInstanceConfVLANconfig_Type()
)
fgs2528kxERPSInstanceConfVLANconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSInstanceConfVLANconfig.setStatus("current")


class _Fgs2528kxERPSConfRowStatus_Type(Integer32):
    """Custom type fgs2528kxERPSConfRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Fgs2528kxERPSConfRowStatus_Type.__name__ = "Integer32"
_Fgs2528kxERPSConfRowStatus_Object = MibTableColumn
fgs2528kxERPSConfRowStatus = _Fgs2528kxERPSConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 2, 10, 1, 2, 1, 21),
    _Fgs2528kxERPSConfRowStatus_Type()
)
fgs2528kxERPSConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxERPSConfRowStatus.setStatus("current")
_Fgs2528kxSecurity_ObjectIdentity = ObjectIdentity
fgs2528kxSecurity = _Fgs2528kxSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3)
)
_Fgs2528kxIPSourceGuard_ObjectIdentity = ObjectIdentity
fgs2528kxIPSourceGuard = _Fgs2528kxIPSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1)
)
_Fgs2528kxIPSourceGuardConf_ObjectIdentity = ObjectIdentity
fgs2528kxIPSourceGuardConf = _Fgs2528kxIPSourceGuardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 1)
)


class _Fgs2528kxIPSourceGuardMode_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxIPSourceGuardMode_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardMode_Object = MibScalar
fgs2528kxIPSourceGuardMode = _Fgs2528kxIPSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 1, 1),
    _Fgs2528kxIPSourceGuardMode_Type()
)
fgs2528kxIPSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardMode.setStatus("current")
_Fgs2528kxIPSourceGuardPortConfigTable_Object = MibTable
fgs2528kxIPSourceGuardPortConfigTable = _Fgs2528kxIPSourceGuardPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardPortConfigTable.setStatus("current")
_Fgs2528kxIPSourceGuardPortConfigEntry_Object = MibTableRow
fgs2528kxIPSourceGuardPortConfigEntry = _Fgs2528kxIPSourceGuardPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 1, 2, 1)
)
fgs2528kxIPSourceGuardPortConfigEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxIPSourceGuardPortConfigPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardPortConfigEntry.setStatus("current")


class _Fgs2528kxIPSourceGuardPortConfigPort_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxIPSourceGuardPortConfigPort_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardPortConfigPort_Object = MibTableColumn
fgs2528kxIPSourceGuardPortConfigPort = _Fgs2528kxIPSourceGuardPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 1, 2, 1, 1),
    _Fgs2528kxIPSourceGuardPortConfigPort_Type()
)
fgs2528kxIPSourceGuardPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardPortConfigPort.setStatus("current")


class _Fgs2528kxIPSourceGuardPortConfigMode_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxIPSourceGuardPortConfigMode_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardPortConfigMode_Object = MibTableColumn
fgs2528kxIPSourceGuardPortConfigMode = _Fgs2528kxIPSourceGuardPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 1, 2, 1, 2),
    _Fgs2528kxIPSourceGuardPortConfigMode_Type()
)
fgs2528kxIPSourceGuardPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardPortConfigMode.setStatus("current")


class _Fgs2528kxIPSourceGuardPortMaxDynamicClients_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardPortMaxDynamicClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(99, 99),
    )


_Fgs2528kxIPSourceGuardPortMaxDynamicClients_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardPortMaxDynamicClients_Object = MibTableColumn
fgs2528kxIPSourceGuardPortMaxDynamicClients = _Fgs2528kxIPSourceGuardPortMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 1, 2, 1, 3),
    _Fgs2528kxIPSourceGuardPortMaxDynamicClients_Type()
)
fgs2528kxIPSourceGuardPortMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardPortMaxDynamicClients.setStatus("current")
_Fgs2528kxIPSourceGuardStatic_ObjectIdentity = ObjectIdentity
fgs2528kxIPSourceGuardStatic = _Fgs2528kxIPSourceGuardStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2)
)


class _Fgs2528kxIPSourceGuardStaticCreate_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxIPSourceGuardStaticCreate_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardStaticCreate_Object = MibScalar
fgs2528kxIPSourceGuardStaticCreate = _Fgs2528kxIPSourceGuardStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2, 1),
    _Fgs2528kxIPSourceGuardStaticCreate_Type()
)
fgs2528kxIPSourceGuardStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardStaticCreate.setStatus("current")
_Fgs2528kxIPSourceGuardStaticTable_Object = MibTable
fgs2528kxIPSourceGuardStaticTable = _Fgs2528kxIPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardStaticTable.setStatus("current")
_Fgs2528kxIPSourceGuardStaticEntry_Object = MibTableRow
fgs2528kxIPSourceGuardStaticEntry = _Fgs2528kxIPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2, 2, 1)
)
fgs2528kxIPSourceGuardStaticEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxIPSourceGuardStaticIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardStaticEntry.setStatus("current")


class _Fgs2528kxIPSourceGuardStaticIndex_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Fgs2528kxIPSourceGuardStaticIndex_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardStaticIndex_Object = MibTableColumn
fgs2528kxIPSourceGuardStaticIndex = _Fgs2528kxIPSourceGuardStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2, 2, 1, 1),
    _Fgs2528kxIPSourceGuardStaticIndex_Type()
)
fgs2528kxIPSourceGuardStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardStaticIndex.setStatus("current")


class _Fgs2528kxIPSourceGuardStaticPort_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxIPSourceGuardStaticPort_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardStaticPort_Object = MibTableColumn
fgs2528kxIPSourceGuardStaticPort = _Fgs2528kxIPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2, 2, 1, 2),
    _Fgs2528kxIPSourceGuardStaticPort_Type()
)
fgs2528kxIPSourceGuardStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardStaticPort.setStatus("current")


class _Fgs2528kxIPSourceGuardStaticVLANId_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Fgs2528kxIPSourceGuardStaticVLANId_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardStaticVLANId_Object = MibTableColumn
fgs2528kxIPSourceGuardStaticVLANId = _Fgs2528kxIPSourceGuardStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2, 2, 1, 3),
    _Fgs2528kxIPSourceGuardStaticVLANId_Type()
)
fgs2528kxIPSourceGuardStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardStaticVLANId.setStatus("current")
_Fgs2528kxIPSourceGuardStaticIPAddress_Type = IpAddress
_Fgs2528kxIPSourceGuardStaticIPAddress_Object = MibTableColumn
fgs2528kxIPSourceGuardStaticIPAddress = _Fgs2528kxIPSourceGuardStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2, 2, 1, 4),
    _Fgs2528kxIPSourceGuardStaticIPAddress_Type()
)
fgs2528kxIPSourceGuardStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardStaticIPAddress.setStatus("current")
_Fgs2528kxIPSourceGuardStaticMACAddress_Type = MacAddress
_Fgs2528kxIPSourceGuardStaticMACAddress_Object = MibTableColumn
fgs2528kxIPSourceGuardStaticMACAddress = _Fgs2528kxIPSourceGuardStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2, 2, 1, 5),
    _Fgs2528kxIPSourceGuardStaticMACAddress_Type()
)
fgs2528kxIPSourceGuardStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardStaticMACAddress.setStatus("current")


class _Fgs2528kxIPSourceGuardStaticRowStatus_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardStaticRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Fgs2528kxIPSourceGuardStaticRowStatus_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardStaticRowStatus_Object = MibTableColumn
fgs2528kxIPSourceGuardStaticRowStatus = _Fgs2528kxIPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 2, 2, 1, 6),
    _Fgs2528kxIPSourceGuardStaticRowStatus_Type()
)
fgs2528kxIPSourceGuardStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardStaticRowStatus.setStatus("current")
_Fgs2528kxIPSourceGuardDynamicTable_Object = MibTable
fgs2528kxIPSourceGuardDynamicTable = _Fgs2528kxIPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 3)
)
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardDynamicTable.setStatus("current")
_Fgs2528kxIPSourceGuardDynamicEntry_Object = MibTableRow
fgs2528kxIPSourceGuardDynamicEntry = _Fgs2528kxIPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 3, 1)
)
fgs2528kxIPSourceGuardDynamicEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxIPSourceGuardDynamicIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardDynamicEntry.setStatus("current")


class _Fgs2528kxIPSourceGuardDynamicIndex_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxIPSourceGuardDynamicIndex_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardDynamicIndex_Object = MibTableColumn
fgs2528kxIPSourceGuardDynamicIndex = _Fgs2528kxIPSourceGuardDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 3, 1, 1),
    _Fgs2528kxIPSourceGuardDynamicIndex_Type()
)
fgs2528kxIPSourceGuardDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardDynamicIndex.setStatus("current")


class _Fgs2528kxIPSourceGuardDynamicPort_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fgs2528kxIPSourceGuardDynamicPort_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardDynamicPort_Object = MibTableColumn
fgs2528kxIPSourceGuardDynamicPort = _Fgs2528kxIPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 3, 1, 2),
    _Fgs2528kxIPSourceGuardDynamicPort_Type()
)
fgs2528kxIPSourceGuardDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardDynamicPort.setStatus("current")


class _Fgs2528kxIPSourceGuardDynamicVLANId_Type(Integer32):
    """Custom type fgs2528kxIPSourceGuardDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Fgs2528kxIPSourceGuardDynamicVLANId_Type.__name__ = "Integer32"
_Fgs2528kxIPSourceGuardDynamicVLANId_Object = MibTableColumn
fgs2528kxIPSourceGuardDynamicVLANId = _Fgs2528kxIPSourceGuardDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 3, 1, 3),
    _Fgs2528kxIPSourceGuardDynamicVLANId_Type()
)
fgs2528kxIPSourceGuardDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardDynamicVLANId.setStatus("current")
_Fgs2528kxIPSourceGuardDynamicIPAddress_Type = IpAddress
_Fgs2528kxIPSourceGuardDynamicIPAddress_Object = MibTableColumn
fgs2528kxIPSourceGuardDynamicIPAddress = _Fgs2528kxIPSourceGuardDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 3, 1, 4),
    _Fgs2528kxIPSourceGuardDynamicIPAddress_Type()
)
fgs2528kxIPSourceGuardDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardDynamicIPAddress.setStatus("current")
_Fgs2528kxIPSourceGuardDynamicMACAddress_Type = MacAddress
_Fgs2528kxIPSourceGuardDynamicMACAddress_Object = MibTableColumn
fgs2528kxIPSourceGuardDynamicMACAddress = _Fgs2528kxIPSourceGuardDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 1, 3, 1, 5),
    _Fgs2528kxIPSourceGuardDynamicMACAddress_Type()
)
fgs2528kxIPSourceGuardDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxIPSourceGuardDynamicMACAddress.setStatus("current")
_Fgs2528kxARPInspection_ObjectIdentity = ObjectIdentity
fgs2528kxARPInspection = _Fgs2528kxARPInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2)
)
_Fgs2528kxARPInspectionConf_ObjectIdentity = ObjectIdentity
fgs2528kxARPInspectionConf = _Fgs2528kxARPInspectionConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 1)
)


class _Fgs2528kxARPInspectionConfMode_Type(Integer32):
    """Custom type fgs2528kxARPInspectionConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxARPInspectionConfMode_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionConfMode_Object = MibScalar
fgs2528kxARPInspectionConfMode = _Fgs2528kxARPInspectionConfMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 1, 1),
    _Fgs2528kxARPInspectionConfMode_Type()
)
fgs2528kxARPInspectionConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionConfMode.setStatus("current")
_Fgs2528kxARPInspectionConfTable_Object = MibTable
fgs2528kxARPInspectionConfTable = _Fgs2528kxARPInspectionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionConfTable.setStatus("current")
_Fgs2528kxARPInspectionConfEntry_Object = MibTableRow
fgs2528kxARPInspectionConfEntry = _Fgs2528kxARPInspectionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 1, 2, 1)
)
fgs2528kxARPInspectionConfEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxARPInspectionConfPortIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionConfEntry.setStatus("current")


class _Fgs2528kxARPInspectionConfPortIndex_Type(Integer32):
    """Custom type fgs2528kxARPInspectionConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxARPInspectionConfPortIndex_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionConfPortIndex_Object = MibTableColumn
fgs2528kxARPInspectionConfPortIndex = _Fgs2528kxARPInspectionConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 1, 2, 1, 1),
    _Fgs2528kxARPInspectionConfPortIndex_Type()
)
fgs2528kxARPInspectionConfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionConfPortIndex.setStatus("current")


class _Fgs2528kxARPInspectionConfPortMode_Type(Integer32):
    """Custom type fgs2528kxARPInspectionConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxARPInspectionConfPortMode_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionConfPortMode_Object = MibTableColumn
fgs2528kxARPInspectionConfPortMode = _Fgs2528kxARPInspectionConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 1, 2, 1, 2),
    _Fgs2528kxARPInspectionConfPortMode_Type()
)
fgs2528kxARPInspectionConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionConfPortMode.setStatus("current")
_Fgs2528kxARPInspectionStatic_ObjectIdentity = ObjectIdentity
fgs2528kxARPInspectionStatic = _Fgs2528kxARPInspectionStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2)
)


class _Fgs2528kxARPInspectionStaticCreate_Type(Integer32):
    """Custom type fgs2528kxARPInspectionStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxARPInspectionStaticCreate_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionStaticCreate_Object = MibScalar
fgs2528kxARPInspectionStaticCreate = _Fgs2528kxARPInspectionStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2, 1),
    _Fgs2528kxARPInspectionStaticCreate_Type()
)
fgs2528kxARPInspectionStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionStaticCreate.setStatus("current")
_Fgs2528kxARPInspectionStaticTable_Object = MibTable
fgs2528kxARPInspectionStaticTable = _Fgs2528kxARPInspectionStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionStaticTable.setStatus("current")
_Fgs2528kxARPInspectionStaticEntry_Object = MibTableRow
fgs2528kxARPInspectionStaticEntry = _Fgs2528kxARPInspectionStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2, 2, 1)
)
fgs2528kxARPInspectionStaticEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxARPInspectionStaticIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionStaticEntry.setStatus("current")


class _Fgs2528kxARPInspectionStaticIndex_Type(Integer32):
    """Custom type fgs2528kxARPInspectionStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxARPInspectionStaticIndex_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionStaticIndex_Object = MibTableColumn
fgs2528kxARPInspectionStaticIndex = _Fgs2528kxARPInspectionStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2, 2, 1, 1),
    _Fgs2528kxARPInspectionStaticIndex_Type()
)
fgs2528kxARPInspectionStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionStaticIndex.setStatus("current")


class _Fgs2528kxARPInspectionStaticPort_Type(Integer32):
    """Custom type fgs2528kxARPInspectionStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxARPInspectionStaticPort_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionStaticPort_Object = MibTableColumn
fgs2528kxARPInspectionStaticPort = _Fgs2528kxARPInspectionStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2, 2, 1, 2),
    _Fgs2528kxARPInspectionStaticPort_Type()
)
fgs2528kxARPInspectionStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionStaticPort.setStatus("current")


class _Fgs2528kxARPInspectionStaticVLANId_Type(Integer32):
    """Custom type fgs2528kxARPInspectionStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Fgs2528kxARPInspectionStaticVLANId_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionStaticVLANId_Object = MibTableColumn
fgs2528kxARPInspectionStaticVLANId = _Fgs2528kxARPInspectionStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2, 2, 1, 3),
    _Fgs2528kxARPInspectionStaticVLANId_Type()
)
fgs2528kxARPInspectionStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionStaticVLANId.setStatus("current")
_Fgs2528kxARPInspectionStaticIPAddress_Type = IpAddress
_Fgs2528kxARPInspectionStaticIPAddress_Object = MibTableColumn
fgs2528kxARPInspectionStaticIPAddress = _Fgs2528kxARPInspectionStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2, 2, 1, 4),
    _Fgs2528kxARPInspectionStaticIPAddress_Type()
)
fgs2528kxARPInspectionStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionStaticIPAddress.setStatus("current")
_Fgs2528kxARPInspectionStaticMACAddress_Type = MacAddress
_Fgs2528kxARPInspectionStaticMACAddress_Object = MibTableColumn
fgs2528kxARPInspectionStaticMACAddress = _Fgs2528kxARPInspectionStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2, 2, 1, 5),
    _Fgs2528kxARPInspectionStaticMACAddress_Type()
)
fgs2528kxARPInspectionStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionStaticMACAddress.setStatus("current")


class _Fgs2528kxARPInspectionStaticRowStatus_Type(Integer32):
    """Custom type fgs2528kxARPInspectionStaticRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Fgs2528kxARPInspectionStaticRowStatus_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionStaticRowStatus_Object = MibTableColumn
fgs2528kxARPInspectionStaticRowStatus = _Fgs2528kxARPInspectionStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 2, 2, 1, 6),
    _Fgs2528kxARPInspectionStaticRowStatus_Type()
)
fgs2528kxARPInspectionStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionStaticRowStatus.setStatus("current")
_Fgs2528kxARPInspectionDynamicTable_Object = MibTable
fgs2528kxARPInspectionDynamicTable = _Fgs2528kxARPInspectionDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 3)
)
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionDynamicTable.setStatus("current")
_Fgs2528kxARPInspectionDynamicEntry_Object = MibTableRow
fgs2528kxARPInspectionDynamicEntry = _Fgs2528kxARPInspectionDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 3, 1)
)
fgs2528kxARPInspectionDynamicEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxARPInspectionDynamicIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionDynamicEntry.setStatus("current")


class _Fgs2528kxARPInspectionDynamicIndex_Type(Integer32):
    """Custom type fgs2528kxARPInspectionDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxARPInspectionDynamicIndex_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionDynamicIndex_Object = MibTableColumn
fgs2528kxARPInspectionDynamicIndex = _Fgs2528kxARPInspectionDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 3, 1, 1),
    _Fgs2528kxARPInspectionDynamicIndex_Type()
)
fgs2528kxARPInspectionDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionDynamicIndex.setStatus("current")


class _Fgs2528kxARPInspectionDynamicPort_Type(Integer32):
    """Custom type fgs2528kxARPInspectionDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxARPInspectionDynamicPort_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionDynamicPort_Object = MibTableColumn
fgs2528kxARPInspectionDynamicPort = _Fgs2528kxARPInspectionDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 3, 1, 2),
    _Fgs2528kxARPInspectionDynamicPort_Type()
)
fgs2528kxARPInspectionDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionDynamicPort.setStatus("current")


class _Fgs2528kxARPInspectionDynamicVLANId_Type(Integer32):
    """Custom type fgs2528kxARPInspectionDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Fgs2528kxARPInspectionDynamicVLANId_Type.__name__ = "Integer32"
_Fgs2528kxARPInspectionDynamicVLANId_Object = MibTableColumn
fgs2528kxARPInspectionDynamicVLANId = _Fgs2528kxARPInspectionDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 3, 1, 3),
    _Fgs2528kxARPInspectionDynamicVLANId_Type()
)
fgs2528kxARPInspectionDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionDynamicVLANId.setStatus("current")
_Fgs2528kxARPInspectionDynamicIPAddress_Type = IpAddress
_Fgs2528kxARPInspectionDynamicIPAddress_Object = MibTableColumn
fgs2528kxARPInspectionDynamicIPAddress = _Fgs2528kxARPInspectionDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 3, 1, 4),
    _Fgs2528kxARPInspectionDynamicIPAddress_Type()
)
fgs2528kxARPInspectionDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionDynamicIPAddress.setStatus("current")
_Fgs2528kxARPInspectionDynamicMACAddress_Type = MacAddress
_Fgs2528kxARPInspectionDynamicMACAddress_Object = MibTableColumn
fgs2528kxARPInspectionDynamicMACAddress = _Fgs2528kxARPInspectionDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 2, 3, 1, 5),
    _Fgs2528kxARPInspectionDynamicMACAddress_Type()
)
fgs2528kxARPInspectionDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxARPInspectionDynamicMACAddress.setStatus("current")
_Fgs2528kxDHCPSnooping_ObjectIdentity = ObjectIdentity
fgs2528kxDHCPSnooping = _Fgs2528kxDHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3)
)
_Fgs2528kxDHCPSnoopingConf_ObjectIdentity = ObjectIdentity
fgs2528kxDHCPSnoopingConf = _Fgs2528kxDHCPSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 1)
)


class _Fgs2528kxDHCPSnoopingMode_Type(Integer32):
    """Custom type fgs2528kxDHCPSnoopingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDHCPSnoopingMode_Type.__name__ = "Integer32"
_Fgs2528kxDHCPSnoopingMode_Object = MibScalar
fgs2528kxDHCPSnoopingMode = _Fgs2528kxDHCPSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 1, 1),
    _Fgs2528kxDHCPSnoopingMode_Type()
)
fgs2528kxDHCPSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingMode.setStatus("current")
_Fgs2528kxDHCPSnoopingPortModeConfigurationTable_Object = MibTable
fgs2528kxDHCPSnoopingPortModeConfigurationTable = _Fgs2528kxDHCPSnoopingPortModeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingPortModeConfigurationTable.setStatus("current")
_Fgs2528kxDHCPSnoopingPortModeConfigurationEntry_Object = MibTableRow
fgs2528kxDHCPSnoopingPortModeConfigurationEntry = _Fgs2528kxDHCPSnoopingPortModeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 1, 2, 1)
)
fgs2528kxDHCPSnoopingPortModeConfigurationEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxDHCPSnoopingPortModeConfigurationPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingPortModeConfigurationEntry.setStatus("current")


class _Fgs2528kxDHCPSnoopingPortModeConfigurationPort_Type(Integer32):
    """Custom type fgs2528kxDHCPSnoopingPortModeConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxDHCPSnoopingPortModeConfigurationPort_Type.__name__ = "Integer32"
_Fgs2528kxDHCPSnoopingPortModeConfigurationPort_Object = MibTableColumn
fgs2528kxDHCPSnoopingPortModeConfigurationPort = _Fgs2528kxDHCPSnoopingPortModeConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 1, 2, 1, 1),
    _Fgs2528kxDHCPSnoopingPortModeConfigurationPort_Type()
)
fgs2528kxDHCPSnoopingPortModeConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingPortModeConfigurationPort.setStatus("current")


class _Fgs2528kxDHCPSnoopingPortModeConfigurationMode_Type(Integer32):
    """Custom type fgs2528kxDHCPSnoopingPortModeConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDHCPSnoopingPortModeConfigurationMode_Type.__name__ = "Integer32"
_Fgs2528kxDHCPSnoopingPortModeConfigurationMode_Object = MibTableColumn
fgs2528kxDHCPSnoopingPortModeConfigurationMode = _Fgs2528kxDHCPSnoopingPortModeConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 1, 2, 1, 2),
    _Fgs2528kxDHCPSnoopingPortModeConfigurationMode_Type()
)
fgs2528kxDHCPSnoopingPortModeConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingPortModeConfigurationMode.setStatus("current")
_Fgs2528kxDHCPSnoopingStatisticsTable_Object = MibTable
fgs2528kxDHCPSnoopingStatisticsTable = _Fgs2528kxDHCPSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingStatisticsTable.setStatus("current")
_Fgs2528kxDHCPSnoopingStatisticsEntry_Object = MibTableRow
fgs2528kxDHCPSnoopingStatisticsEntry = _Fgs2528kxDHCPSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1)
)
fgs2528kxDHCPSnoopingStatisticsEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxDHCPSnoopingStatisticsPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingStatisticsEntry.setStatus("current")


class _Fgs2528kxDHCPSnoopingStatisticsPort_Type(Integer32):
    """Custom type fgs2528kxDHCPSnoopingStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxDHCPSnoopingStatisticsPort_Type.__name__ = "Integer32"
_Fgs2528kxDHCPSnoopingStatisticsPort_Object = MibTableColumn
fgs2528kxDHCPSnoopingStatisticsPort = _Fgs2528kxDHCPSnoopingStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 1),
    _Fgs2528kxDHCPSnoopingStatisticsPort_Type()
)
fgs2528kxDHCPSnoopingStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingStatisticsPort.setStatus("current")


class _Fgs2528kxDHCPSnoopingStatisticsClear_Type(Integer32):
    """Custom type fgs2528kxDHCPSnoopingStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDHCPSnoopingStatisticsClear_Type.__name__ = "Integer32"
_Fgs2528kxDHCPSnoopingStatisticsClear_Object = MibTableColumn
fgs2528kxDHCPSnoopingStatisticsClear = _Fgs2528kxDHCPSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 2),
    _Fgs2528kxDHCPSnoopingStatisticsClear_Type()
)
fgs2528kxDHCPSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingStatisticsClear.setStatus("current")
_Fgs2528kxDHCPSnoopingRxDiscover_Type = Counter32
_Fgs2528kxDHCPSnoopingRxDiscover_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxDiscover = _Fgs2528kxDHCPSnoopingRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 3),
    _Fgs2528kxDHCPSnoopingRxDiscover_Type()
)
fgs2528kxDHCPSnoopingRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxDiscover.setStatus("current")
_Fgs2528kxDHCPSnoopingRxOffer_Type = Counter32
_Fgs2528kxDHCPSnoopingRxOffer_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxOffer = _Fgs2528kxDHCPSnoopingRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 4),
    _Fgs2528kxDHCPSnoopingRxOffer_Type()
)
fgs2528kxDHCPSnoopingRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxOffer.setStatus("current")
_Fgs2528kxDHCPSnoopingRxRequest_Type = Counter32
_Fgs2528kxDHCPSnoopingRxRequest_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxRequest = _Fgs2528kxDHCPSnoopingRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 5),
    _Fgs2528kxDHCPSnoopingRxRequest_Type()
)
fgs2528kxDHCPSnoopingRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxRequest.setStatus("current")
_Fgs2528kxDHCPSnoopingRxDecline_Type = Counter32
_Fgs2528kxDHCPSnoopingRxDecline_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxDecline = _Fgs2528kxDHCPSnoopingRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 6),
    _Fgs2528kxDHCPSnoopingRxDecline_Type()
)
fgs2528kxDHCPSnoopingRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxDecline.setStatus("current")
_Fgs2528kxDHCPSnoopingRxACK_Type = Counter32
_Fgs2528kxDHCPSnoopingRxACK_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxACK = _Fgs2528kxDHCPSnoopingRxACK_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 7),
    _Fgs2528kxDHCPSnoopingRxACK_Type()
)
fgs2528kxDHCPSnoopingRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxACK.setStatus("current")
_Fgs2528kxDHCPSnoopingRxNAK_Type = Counter32
_Fgs2528kxDHCPSnoopingRxNAK_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxNAK = _Fgs2528kxDHCPSnoopingRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 8),
    _Fgs2528kxDHCPSnoopingRxNAK_Type()
)
fgs2528kxDHCPSnoopingRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxNAK.setStatus("current")
_Fgs2528kxDHCPSnoopingRxRelease_Type = Counter32
_Fgs2528kxDHCPSnoopingRxRelease_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxRelease = _Fgs2528kxDHCPSnoopingRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 9),
    _Fgs2528kxDHCPSnoopingRxRelease_Type()
)
fgs2528kxDHCPSnoopingRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxRelease.setStatus("current")
_Fgs2528kxDHCPSnoopingRxInform_Type = Counter32
_Fgs2528kxDHCPSnoopingRxInform_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxInform = _Fgs2528kxDHCPSnoopingRxInform_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 10),
    _Fgs2528kxDHCPSnoopingRxInform_Type()
)
fgs2528kxDHCPSnoopingRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxInform.setStatus("current")
_Fgs2528kxDHCPSnoopingRxLeaseQuery_Type = Counter32
_Fgs2528kxDHCPSnoopingRxLeaseQuery_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxLeaseQuery = _Fgs2528kxDHCPSnoopingRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 11),
    _Fgs2528kxDHCPSnoopingRxLeaseQuery_Type()
)
fgs2528kxDHCPSnoopingRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxLeaseQuery.setStatus("current")
_Fgs2528kxDHCPSnoopingRxLeaseUnassigned_Type = Counter32
_Fgs2528kxDHCPSnoopingRxLeaseUnassigned_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxLeaseUnassigned = _Fgs2528kxDHCPSnoopingRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 12),
    _Fgs2528kxDHCPSnoopingRxLeaseUnassigned_Type()
)
fgs2528kxDHCPSnoopingRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxLeaseUnassigned.setStatus("current")
_Fgs2528kxDHCPSnoopingRxLeaseUnknown_Type = Counter32
_Fgs2528kxDHCPSnoopingRxLeaseUnknown_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxLeaseUnknown = _Fgs2528kxDHCPSnoopingRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 13),
    _Fgs2528kxDHCPSnoopingRxLeaseUnknown_Type()
)
fgs2528kxDHCPSnoopingRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxLeaseUnknown.setStatus("current")
_Fgs2528kxDHCPSnoopingRxLeaseActive_Type = Counter32
_Fgs2528kxDHCPSnoopingRxLeaseActive_Object = MibTableColumn
fgs2528kxDHCPSnoopingRxLeaseActive = _Fgs2528kxDHCPSnoopingRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 14),
    _Fgs2528kxDHCPSnoopingRxLeaseActive_Type()
)
fgs2528kxDHCPSnoopingRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingRxLeaseActive.setStatus("current")
_Fgs2528kxDHCPSnoopingTxDiscover_Type = Counter32
_Fgs2528kxDHCPSnoopingTxDiscover_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxDiscover = _Fgs2528kxDHCPSnoopingTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 15),
    _Fgs2528kxDHCPSnoopingTxDiscover_Type()
)
fgs2528kxDHCPSnoopingTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxDiscover.setStatus("current")
_Fgs2528kxDHCPSnoopingTxOffer_Type = Counter32
_Fgs2528kxDHCPSnoopingTxOffer_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxOffer = _Fgs2528kxDHCPSnoopingTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 16),
    _Fgs2528kxDHCPSnoopingTxOffer_Type()
)
fgs2528kxDHCPSnoopingTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxOffer.setStatus("current")
_Fgs2528kxDHCPSnoopingTxRequest_Type = Counter32
_Fgs2528kxDHCPSnoopingTxRequest_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxRequest = _Fgs2528kxDHCPSnoopingTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 17),
    _Fgs2528kxDHCPSnoopingTxRequest_Type()
)
fgs2528kxDHCPSnoopingTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxRequest.setStatus("current")
_Fgs2528kxDHCPSnoopingTxDecline_Type = Counter32
_Fgs2528kxDHCPSnoopingTxDecline_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxDecline = _Fgs2528kxDHCPSnoopingTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 18),
    _Fgs2528kxDHCPSnoopingTxDecline_Type()
)
fgs2528kxDHCPSnoopingTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxDecline.setStatus("current")
_Fgs2528kxDHCPSnoopingTxACK_Type = Counter32
_Fgs2528kxDHCPSnoopingTxACK_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxACK = _Fgs2528kxDHCPSnoopingTxACK_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 19),
    _Fgs2528kxDHCPSnoopingTxACK_Type()
)
fgs2528kxDHCPSnoopingTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxACK.setStatus("current")
_Fgs2528kxDHCPSnoopingTxNAK_Type = Counter32
_Fgs2528kxDHCPSnoopingTxNAK_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxNAK = _Fgs2528kxDHCPSnoopingTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 20),
    _Fgs2528kxDHCPSnoopingTxNAK_Type()
)
fgs2528kxDHCPSnoopingTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxNAK.setStatus("current")
_Fgs2528kxDHCPSnoopingTxRelease_Type = Counter32
_Fgs2528kxDHCPSnoopingTxRelease_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxRelease = _Fgs2528kxDHCPSnoopingTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 21),
    _Fgs2528kxDHCPSnoopingTxRelease_Type()
)
fgs2528kxDHCPSnoopingTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxRelease.setStatus("current")
_Fgs2528kxDHCPSnoopingTxInform_Type = Counter32
_Fgs2528kxDHCPSnoopingTxInform_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxInform = _Fgs2528kxDHCPSnoopingTxInform_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 22),
    _Fgs2528kxDHCPSnoopingTxInform_Type()
)
fgs2528kxDHCPSnoopingTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxInform.setStatus("current")
_Fgs2528kxDHCPSnoopingTxLeaseQuery_Type = Counter32
_Fgs2528kxDHCPSnoopingTxLeaseQuery_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxLeaseQuery = _Fgs2528kxDHCPSnoopingTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 23),
    _Fgs2528kxDHCPSnoopingTxLeaseQuery_Type()
)
fgs2528kxDHCPSnoopingTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxLeaseQuery.setStatus("current")
_Fgs2528kxDHCPSnoopingTxLeaseUnassigned_Type = Counter32
_Fgs2528kxDHCPSnoopingTxLeaseUnassigned_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxLeaseUnassigned = _Fgs2528kxDHCPSnoopingTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 24),
    _Fgs2528kxDHCPSnoopingTxLeaseUnassigned_Type()
)
fgs2528kxDHCPSnoopingTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxLeaseUnassigned.setStatus("current")
_Fgs2528kxDHCPSnoopingTxLeaseUnknown_Type = Counter32
_Fgs2528kxDHCPSnoopingTxLeaseUnknown_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxLeaseUnknown = _Fgs2528kxDHCPSnoopingTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 25),
    _Fgs2528kxDHCPSnoopingTxLeaseUnknown_Type()
)
fgs2528kxDHCPSnoopingTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxLeaseUnknown.setStatus("current")
_Fgs2528kxDHCPSnoopingTxLeaseActive_Type = Counter32
_Fgs2528kxDHCPSnoopingTxLeaseActive_Object = MibTableColumn
fgs2528kxDHCPSnoopingTxLeaseActive = _Fgs2528kxDHCPSnoopingTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 3, 2, 1, 26),
    _Fgs2528kxDHCPSnoopingTxLeaseActive_Type()
)
fgs2528kxDHCPSnoopingTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxDHCPSnoopingTxLeaseActive.setStatus("current")
_Fgs2528kxDHCPRelay_ObjectIdentity = ObjectIdentity
fgs2528kxDHCPRelay = _Fgs2528kxDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4)
)
_Fgs2528kxDHCPRelayConfiguration_ObjectIdentity = ObjectIdentity
fgs2528kxDHCPRelayConfiguration = _Fgs2528kxDHCPRelayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 1)
)


class _Fgs2528kxDHCPRelayMode_Type(Integer32):
    """Custom type fgs2528kxDHCPRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDHCPRelayMode_Type.__name__ = "Integer32"
_Fgs2528kxDHCPRelayMode_Object = MibScalar
fgs2528kxDHCPRelayMode = _Fgs2528kxDHCPRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 1, 1),
    _Fgs2528kxDHCPRelayMode_Type()
)
fgs2528kxDHCPRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDHCPRelayMode.setStatus("current")
_Fgs2528kxDHCPRelayServer_Type = IpAddress
_Fgs2528kxDHCPRelayServer_Object = MibScalar
fgs2528kxDHCPRelayServer = _Fgs2528kxDHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 1, 2),
    _Fgs2528kxDHCPRelayServer_Type()
)
fgs2528kxDHCPRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDHCPRelayServer.setStatus("current")


class _Fgs2528kxDHCPRelayInformationMode_Type(Integer32):
    """Custom type fgs2528kxDHCPRelayInformationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDHCPRelayInformationMode_Type.__name__ = "Integer32"
_Fgs2528kxDHCPRelayInformationMode_Object = MibScalar
fgs2528kxDHCPRelayInformationMode = _Fgs2528kxDHCPRelayInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 1, 3),
    _Fgs2528kxDHCPRelayInformationMode_Type()
)
fgs2528kxDHCPRelayInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDHCPRelayInformationMode.setStatus("current")


class _Fgs2528kxDHCPRelayInformationPolicy_Type(Integer32):
    """Custom type fgs2528kxDHCPRelayInformationPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fgs2528kxDHCPRelayInformationPolicy_Type.__name__ = "Integer32"
_Fgs2528kxDHCPRelayInformationPolicy_Object = MibScalar
fgs2528kxDHCPRelayInformationPolicy = _Fgs2528kxDHCPRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 1, 4),
    _Fgs2528kxDHCPRelayInformationPolicy_Type()
)
fgs2528kxDHCPRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDHCPRelayInformationPolicy.setStatus("current")
_Fgs2528kxDHCPRelayStatistics_ObjectIdentity = ObjectIdentity
fgs2528kxDHCPRelayStatistics = _Fgs2528kxDHCPRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2)
)
_Fgs2528kxDHCPRelayServerStatistics_ObjectIdentity = ObjectIdentity
fgs2528kxDHCPRelayServerStatistics = _Fgs2528kxDHCPRelayServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 1)
)
_Fgs2528kxServerStatTransmitToServer_Type = Counter32
_Fgs2528kxServerStatTransmitToServer_Object = MibScalar
fgs2528kxServerStatTransmitToServer = _Fgs2528kxServerStatTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 1, 1),
    _Fgs2528kxServerStatTransmitToServer_Type()
)
fgs2528kxServerStatTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxServerStatTransmitToServer.setStatus("current")
_Fgs2528kxServerStatTransmitError_Type = Counter32
_Fgs2528kxServerStatTransmitError_Object = MibScalar
fgs2528kxServerStatTransmitError = _Fgs2528kxServerStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 1, 2),
    _Fgs2528kxServerStatTransmitError_Type()
)
fgs2528kxServerStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxServerStatTransmitError.setStatus("current")
_Fgs2528kxServerStatReceiveFromServer_Type = Counter32
_Fgs2528kxServerStatReceiveFromServer_Object = MibScalar
fgs2528kxServerStatReceiveFromServer = _Fgs2528kxServerStatReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 1, 3),
    _Fgs2528kxServerStatReceiveFromServer_Type()
)
fgs2528kxServerStatReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxServerStatReceiveFromServer.setStatus("current")
_Fgs2528kxServerStatReceiveMissingAgentOption_Type = Counter32
_Fgs2528kxServerStatReceiveMissingAgentOption_Object = MibScalar
fgs2528kxServerStatReceiveMissingAgentOption = _Fgs2528kxServerStatReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 1, 4),
    _Fgs2528kxServerStatReceiveMissingAgentOption_Type()
)
fgs2528kxServerStatReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxServerStatReceiveMissingAgentOption.setStatus("current")
_Fgs2528kxServerStatReceiveMissingCircuitID_Type = Counter32
_Fgs2528kxServerStatReceiveMissingCircuitID_Object = MibScalar
fgs2528kxServerStatReceiveMissingCircuitID = _Fgs2528kxServerStatReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 1, 5),
    _Fgs2528kxServerStatReceiveMissingCircuitID_Type()
)
fgs2528kxServerStatReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxServerStatReceiveMissingCircuitID.setStatus("current")
_Fgs2528kxServerStatReceiveMissingRemoteID_Type = Counter32
_Fgs2528kxServerStatReceiveMissingRemoteID_Object = MibScalar
fgs2528kxServerStatReceiveMissingRemoteID = _Fgs2528kxServerStatReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 1, 6),
    _Fgs2528kxServerStatReceiveMissingRemoteID_Type()
)
fgs2528kxServerStatReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxServerStatReceiveMissingRemoteID.setStatus("current")
_Fgs2528kxServerStatReceiveBadCircuitID_Type = Counter32
_Fgs2528kxServerStatReceiveBadCircuitID_Object = MibScalar
fgs2528kxServerStatReceiveBadCircuitID = _Fgs2528kxServerStatReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 1, 7),
    _Fgs2528kxServerStatReceiveBadCircuitID_Type()
)
fgs2528kxServerStatReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxServerStatReceiveBadCircuitID.setStatus("current")
_Fgs2528kxServerStatReceiveBadRemoteID_Type = Counter32
_Fgs2528kxServerStatReceiveBadRemoteID_Object = MibScalar
fgs2528kxServerStatReceiveBadRemoteID = _Fgs2528kxServerStatReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 1, 8),
    _Fgs2528kxServerStatReceiveBadRemoteID_Type()
)
fgs2528kxServerStatReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxServerStatReceiveBadRemoteID.setStatus("current")
_Fgs2528kxDHCPRelayClientStatistics_ObjectIdentity = ObjectIdentity
fgs2528kxDHCPRelayClientStatistics = _Fgs2528kxDHCPRelayClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 2)
)
_Fgs2528kxClientStatTransmitToClient_Type = Counter32
_Fgs2528kxClientStatTransmitToClient_Object = MibScalar
fgs2528kxClientStatTransmitToClient = _Fgs2528kxClientStatTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 2, 1),
    _Fgs2528kxClientStatTransmitToClient_Type()
)
fgs2528kxClientStatTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxClientStatTransmitToClient.setStatus("current")
_Fgs2528kxClientStatTransmitError_Type = Counter32
_Fgs2528kxClientStatTransmitError_Object = MibScalar
fgs2528kxClientStatTransmitError = _Fgs2528kxClientStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 2, 2),
    _Fgs2528kxClientStatTransmitError_Type()
)
fgs2528kxClientStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxClientStatTransmitError.setStatus("current")
_Fgs2528kxClientStatReceivefromClient_Type = Counter32
_Fgs2528kxClientStatReceivefromClient_Object = MibScalar
fgs2528kxClientStatReceivefromClient = _Fgs2528kxClientStatReceivefromClient_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 2, 3),
    _Fgs2528kxClientStatReceivefromClient_Type()
)
fgs2528kxClientStatReceivefromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxClientStatReceivefromClient.setStatus("current")
_Fgs2528kxClientStatReceiveAgentOption_Type = Counter32
_Fgs2528kxClientStatReceiveAgentOption_Object = MibScalar
fgs2528kxClientStatReceiveAgentOption = _Fgs2528kxClientStatReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 2, 4),
    _Fgs2528kxClientStatReceiveAgentOption_Type()
)
fgs2528kxClientStatReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxClientStatReceiveAgentOption.setStatus("current")
_Fgs2528kxClientStatReplaceAgentOption_Type = Counter32
_Fgs2528kxClientStatReplaceAgentOption_Object = MibScalar
fgs2528kxClientStatReplaceAgentOption = _Fgs2528kxClientStatReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 2, 5),
    _Fgs2528kxClientStatReplaceAgentOption_Type()
)
fgs2528kxClientStatReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxClientStatReplaceAgentOption.setStatus("current")
_Fgs2528kxClientStatKeepAgentOption_Type = Counter32
_Fgs2528kxClientStatKeepAgentOption_Object = MibScalar
fgs2528kxClientStatKeepAgentOption = _Fgs2528kxClientStatKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 2, 6),
    _Fgs2528kxClientStatKeepAgentOption_Type()
)
fgs2528kxClientStatKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxClientStatKeepAgentOption.setStatus("current")
_Fgs2528kxClientStatDropAgentOption_Type = Counter32
_Fgs2528kxClientStatDropAgentOption_Object = MibScalar
fgs2528kxClientStatDropAgentOption = _Fgs2528kxClientStatDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 4, 2, 2, 7),
    _Fgs2528kxClientStatDropAgentOption_Type()
)
fgs2528kxClientStatDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxClientStatDropAgentOption.setStatus("current")
_Fgs2528kxPortSecurity_ObjectIdentity = ObjectIdentity
fgs2528kxPortSecurity = _Fgs2528kxPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5)
)
_Fgs2528kxPortSecLimitCtrl_ObjectIdentity = ObjectIdentity
fgs2528kxPortSecLimitCtrl = _Fgs2528kxPortSecLimitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1)
)
_Fgs2528kxPortSecLimitCtrlSystemConf_ObjectIdentity = ObjectIdentity
fgs2528kxPortSecLimitCtrlSystemConf = _Fgs2528kxPortSecLimitCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 1)
)


class _Fgs2528kxPortSecurityMode_Type(Integer32):
    """Custom type fgs2528kxPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortSecurityMode_Type.__name__ = "Integer32"
_Fgs2528kxPortSecurityMode_Object = MibScalar
fgs2528kxPortSecurityMode = _Fgs2528kxPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 1, 1),
    _Fgs2528kxPortSecurityMode_Type()
)
fgs2528kxPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortSecurityMode.setStatus("current")


class _Fgs2528kxPortSecurityAging_Type(Integer32):
    """Custom type fgs2528kxPortSecurityAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortSecurityAging_Type.__name__ = "Integer32"
_Fgs2528kxPortSecurityAging_Object = MibScalar
fgs2528kxPortSecurityAging = _Fgs2528kxPortSecurityAging_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 1, 2),
    _Fgs2528kxPortSecurityAging_Type()
)
fgs2528kxPortSecurityAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortSecurityAging.setStatus("current")


class _Fgs2528kxPortSecurityAgingPeriod_Type(Integer32):
    """Custom type fgs2528kxPortSecurityAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_Fgs2528kxPortSecurityAgingPeriod_Type.__name__ = "Integer32"
_Fgs2528kxPortSecurityAgingPeriod_Object = MibScalar
fgs2528kxPortSecurityAgingPeriod = _Fgs2528kxPortSecurityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 1, 3),
    _Fgs2528kxPortSecurityAgingPeriod_Type()
)
fgs2528kxPortSecurityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortSecurityAgingPeriod.setStatus("current")
_Fgs2528kxPortSecLimitCtrlTable_Object = MibTable
fgs2528kxPortSecLimitCtrlTable = _Fgs2528kxPortSecLimitCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxPortSecLimitCtrlTable.setStatus("current")
_Fgs2528kxPortSecLimitCtrlEntry_Object = MibTableRow
fgs2528kxPortSecLimitCtrlEntry = _Fgs2528kxPortSecLimitCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 2, 1)
)
fgs2528kxPortSecLimitCtrlEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxPortSecLimitCtrlPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxPortSecLimitCtrlEntry.setStatus("current")


class _Fgs2528kxPortSecLimitCtrlPort_Type(Integer32):
    """Custom type fgs2528kxPortSecLimitCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxPortSecLimitCtrlPort_Type.__name__ = "Integer32"
_Fgs2528kxPortSecLimitCtrlPort_Object = MibTableColumn
fgs2528kxPortSecLimitCtrlPort = _Fgs2528kxPortSecLimitCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 2, 1, 1),
    _Fgs2528kxPortSecLimitCtrlPort_Type()
)
fgs2528kxPortSecLimitCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxPortSecLimitCtrlPort.setStatus("current")


class _Fgs2528kxPortSecLimitCtrlPortMode_Type(Integer32):
    """Custom type fgs2528kxPortSecLimitCtrlPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortSecLimitCtrlPortMode_Type.__name__ = "Integer32"
_Fgs2528kxPortSecLimitCtrlPortMode_Object = MibTableColumn
fgs2528kxPortSecLimitCtrlPortMode = _Fgs2528kxPortSecLimitCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 2, 1, 2),
    _Fgs2528kxPortSecLimitCtrlPortMode_Type()
)
fgs2528kxPortSecLimitCtrlPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortSecLimitCtrlPortMode.setStatus("current")


class _Fgs2528kxPortSecLimitCtrlPortLimit_Type(Integer32):
    """Custom type fgs2528kxPortSecLimitCtrlPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Fgs2528kxPortSecLimitCtrlPortLimit_Type.__name__ = "Integer32"
_Fgs2528kxPortSecLimitCtrlPortLimit_Object = MibTableColumn
fgs2528kxPortSecLimitCtrlPortLimit = _Fgs2528kxPortSecLimitCtrlPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 2, 1, 3),
    _Fgs2528kxPortSecLimitCtrlPortLimit_Type()
)
fgs2528kxPortSecLimitCtrlPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortSecLimitCtrlPortLimit.setStatus("current")


class _Fgs2528kxPortSecLimitCtrlPortAction_Type(Integer32):
    """Custom type fgs2528kxPortSecLimitCtrlPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxPortSecLimitCtrlPortAction_Type.__name__ = "Integer32"
_Fgs2528kxPortSecLimitCtrlPortAction_Object = MibTableColumn
fgs2528kxPortSecLimitCtrlPortAction = _Fgs2528kxPortSecLimitCtrlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 2, 1, 4),
    _Fgs2528kxPortSecLimitCtrlPortAction_Type()
)
fgs2528kxPortSecLimitCtrlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortSecLimitCtrlPortAction.setStatus("current")
_Fgs2528kxPortSecLimitCtrlPortState_Type = DisplayString
_Fgs2528kxPortSecLimitCtrlPortState_Object = MibTableColumn
fgs2528kxPortSecLimitCtrlPortState = _Fgs2528kxPortSecLimitCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 2, 1, 5),
    _Fgs2528kxPortSecLimitCtrlPortState_Type()
)
fgs2528kxPortSecLimitCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecLimitCtrlPortState.setStatus("current")


class _Fgs2528kxPortSecLimitCtrlPortReOpen_Type(Integer32):
    """Custom type fgs2528kxPortSecLimitCtrlPortReOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxPortSecLimitCtrlPortReOpen_Type.__name__ = "Integer32"
_Fgs2528kxPortSecLimitCtrlPortReOpen_Object = MibTableColumn
fgs2528kxPortSecLimitCtrlPortReOpen = _Fgs2528kxPortSecLimitCtrlPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 1, 2, 1, 6),
    _Fgs2528kxPortSecLimitCtrlPortReOpen_Type()
)
fgs2528kxPortSecLimitCtrlPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortSecLimitCtrlPortReOpen.setStatus("current")
_Fgs2528kxPortSecSwitchStatusTable_Object = MibTable
fgs2528kxPortSecSwitchStatusTable = _Fgs2528kxPortSecSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxPortSecSwitchStatusTable.setStatus("current")
_Fgs2528kxPortSecSwitchStatusEntry_Object = MibTableRow
fgs2528kxPortSecSwitchStatusEntry = _Fgs2528kxPortSecSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 2, 1)
)
fgs2528kxPortSecSwitchStatusEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxPortSecSwitchStatusPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxPortSecSwitchStatusEntry.setStatus("current")


class _Fgs2528kxPortSecSwitchStatusPort_Type(Integer32):
    """Custom type fgs2528kxPortSecSwitchStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxPortSecSwitchStatusPort_Type.__name__ = "Integer32"
_Fgs2528kxPortSecSwitchStatusPort_Object = MibTableColumn
fgs2528kxPortSecSwitchStatusPort = _Fgs2528kxPortSecSwitchStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 2, 1, 1),
    _Fgs2528kxPortSecSwitchStatusPort_Type()
)
fgs2528kxPortSecSwitchStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxPortSecSwitchStatusPort.setStatus("current")
_Fgs2528kxPortSecSwitchStatusUsers_Type = DisplayString
_Fgs2528kxPortSecSwitchStatusUsers_Object = MibTableColumn
fgs2528kxPortSecSwitchStatusUsers = _Fgs2528kxPortSecSwitchStatusUsers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 2, 1, 2),
    _Fgs2528kxPortSecSwitchStatusUsers_Type()
)
fgs2528kxPortSecSwitchStatusUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecSwitchStatusUsers.setStatus("current")
_Fgs2528kxPortSecSwitchStatusState_Type = DisplayString
_Fgs2528kxPortSecSwitchStatusState_Object = MibTableColumn
fgs2528kxPortSecSwitchStatusState = _Fgs2528kxPortSecSwitchStatusState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 2, 1, 3),
    _Fgs2528kxPortSecSwitchStatusState_Type()
)
fgs2528kxPortSecSwitchStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecSwitchStatusState.setStatus("current")


class _Fgs2528kxPortSecSwitchStatusMACCountCurrent_Type(Integer32):
    """Custom type fgs2528kxPortSecSwitchStatusMACCountCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxPortSecSwitchStatusMACCountCurrent_Type.__name__ = "Integer32"
_Fgs2528kxPortSecSwitchStatusMACCountCurrent_Object = MibTableColumn
fgs2528kxPortSecSwitchStatusMACCountCurrent = _Fgs2528kxPortSecSwitchStatusMACCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 2, 1, 4),
    _Fgs2528kxPortSecSwitchStatusMACCountCurrent_Type()
)
fgs2528kxPortSecSwitchStatusMACCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecSwitchStatusMACCountCurrent.setStatus("current")


class _Fgs2528kxPortSecSwitchStatusMACCountLimit_Type(Integer32):
    """Custom type fgs2528kxPortSecSwitchStatusMACCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxPortSecSwitchStatusMACCountLimit_Type.__name__ = "Integer32"
_Fgs2528kxPortSecSwitchStatusMACCountLimit_Object = MibTableColumn
fgs2528kxPortSecSwitchStatusMACCountLimit = _Fgs2528kxPortSecSwitchStatusMACCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 2, 1, 5),
    _Fgs2528kxPortSecSwitchStatusMACCountLimit_Type()
)
fgs2528kxPortSecSwitchStatusMACCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecSwitchStatusMACCountLimit.setStatus("current")
_Fgs2528kxPortSecPortStatus_ObjectIdentity = ObjectIdentity
fgs2528kxPortSecPortStatus = _Fgs2528kxPortSecPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3)
)


class _Fgs2528kxPortSecPortStatusPort_Type(Integer32):
    """Custom type fgs2528kxPortSecPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxPortSecPortStatusPort_Type.__name__ = "Integer32"
_Fgs2528kxPortSecPortStatusPort_Object = MibScalar
fgs2528kxPortSecPortStatusPort = _Fgs2528kxPortSecPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3, 1),
    _Fgs2528kxPortSecPortStatusPort_Type()
)
fgs2528kxPortSecPortStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPortSecPortStatusPort.setStatus("current")
_Fgs2528kxPortSecPortStatusTable_Object = MibTable
fgs2528kxPortSecPortStatusTable = _Fgs2528kxPortSecPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxPortSecPortStatusTable.setStatus("current")
_Fgs2528kxPortSecPortStatusEntry_Object = MibTableRow
fgs2528kxPortSecPortStatusEntry = _Fgs2528kxPortSecPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3, 2, 1)
)
fgs2528kxPortSecPortStatusEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxPortSecPortStatusIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxPortSecPortStatusEntry.setStatus("current")


class _Fgs2528kxPortSecPortStatusIndex_Type(Integer32):
    """Custom type fgs2528kxPortSecPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxPortSecPortStatusIndex_Type.__name__ = "Integer32"
_Fgs2528kxPortSecPortStatusIndex_Object = MibTableColumn
fgs2528kxPortSecPortStatusIndex = _Fgs2528kxPortSecPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3, 2, 1, 1),
    _Fgs2528kxPortSecPortStatusIndex_Type()
)
fgs2528kxPortSecPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxPortSecPortStatusIndex.setStatus("current")
_Fgs2528kxPortSecPortStatusMACAddress_Type = MacAddress
_Fgs2528kxPortSecPortStatusMACAddress_Object = MibTableColumn
fgs2528kxPortSecPortStatusMACAddress = _Fgs2528kxPortSecPortStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3, 2, 1, 2),
    _Fgs2528kxPortSecPortStatusMACAddress_Type()
)
fgs2528kxPortSecPortStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecPortStatusMACAddress.setStatus("current")


class _Fgs2528kxPortSecPortStatusVLANId_Type(Integer32):
    """Custom type fgs2528kxPortSecPortStatusVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Fgs2528kxPortSecPortStatusVLANId_Type.__name__ = "Integer32"
_Fgs2528kxPortSecPortStatusVLANId_Object = MibTableColumn
fgs2528kxPortSecPortStatusVLANId = _Fgs2528kxPortSecPortStatusVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3, 2, 1, 3),
    _Fgs2528kxPortSecPortStatusVLANId_Type()
)
fgs2528kxPortSecPortStatusVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecPortStatusVLANId.setStatus("current")
_Fgs2528kxPortSecPortStatusState_Type = DisplayString
_Fgs2528kxPortSecPortStatusState_Object = MibTableColumn
fgs2528kxPortSecPortStatusState = _Fgs2528kxPortSecPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3, 2, 1, 4),
    _Fgs2528kxPortSecPortStatusState_Type()
)
fgs2528kxPortSecPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecPortStatusState.setStatus("current")
_Fgs2528kxPortSecPortStatusTimeOfAddition_Type = DisplayString
_Fgs2528kxPortSecPortStatusTimeOfAddition_Object = MibTableColumn
fgs2528kxPortSecPortStatusTimeOfAddition = _Fgs2528kxPortSecPortStatusTimeOfAddition_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3, 2, 1, 5),
    _Fgs2528kxPortSecPortStatusTimeOfAddition_Type()
)
fgs2528kxPortSecPortStatusTimeOfAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecPortStatusTimeOfAddition.setStatus("current")
_Fgs2528kxPortSecPortStatusAgeAndHold_Type = DisplayString
_Fgs2528kxPortSecPortStatusAgeAndHold_Object = MibTableColumn
fgs2528kxPortSecPortStatusAgeAndHold = _Fgs2528kxPortSecPortStatusAgeAndHold_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 5, 3, 2, 1, 6),
    _Fgs2528kxPortSecPortStatusAgeAndHold_Type()
)
fgs2528kxPortSecPortStatusAgeAndHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPortSecPortStatusAgeAndHold.setStatus("current")
_Fgs2528kxAccessManagement_ObjectIdentity = ObjectIdentity
fgs2528kxAccessManagement = _Fgs2528kxAccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6)
)
_Fgs2528kxAccessMgtConf_ObjectIdentity = ObjectIdentity
fgs2528kxAccessMgtConf = _Fgs2528kxAccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1)
)


class _Fgs2528kxAccessMgtConfMode_Type(Integer32):
    """Custom type fgs2528kxAccessMgtConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxAccessMgtConfMode_Type.__name__ = "Integer32"
_Fgs2528kxAccessMgtConfMode_Object = MibScalar
fgs2528kxAccessMgtConfMode = _Fgs2528kxAccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 1),
    _Fgs2528kxAccessMgtConfMode_Type()
)
fgs2528kxAccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtConfMode.setStatus("current")


class _Fgs2528kxAccessMgtConfCreate_Type(Integer32):
    """Custom type fgs2528kxAccessMgtConfCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxAccessMgtConfCreate_Type.__name__ = "Integer32"
_Fgs2528kxAccessMgtConfCreate_Object = MibScalar
fgs2528kxAccessMgtConfCreate = _Fgs2528kxAccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 2),
    _Fgs2528kxAccessMgtConfCreate_Type()
)
fgs2528kxAccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtConfCreate.setStatus("current")
_Fgs2528kxAccessMgtConfTable_Object = MibTable
fgs2528kxAccessMgtConfTable = _Fgs2528kxAccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtConfTable.setStatus("current")
_Fgs2528kxAccessMgtConfEntry_Object = MibTableRow
fgs2528kxAccessMgtConfEntry = _Fgs2528kxAccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3, 1)
)
fgs2528kxAccessMgtConfEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxAccessMgtIndex"),
)
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtConfEntry.setStatus("current")


class _Fgs2528kxAccessMgtIndex_Type(Integer32):
    """Custom type fgs2528kxAccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Fgs2528kxAccessMgtIndex_Type.__name__ = "Integer32"
_Fgs2528kxAccessMgtIndex_Object = MibTableColumn
fgs2528kxAccessMgtIndex = _Fgs2528kxAccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3, 1, 1),
    _Fgs2528kxAccessMgtIndex_Type()
)
fgs2528kxAccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtIndex.setStatus("current")


class _Fgs2528kxAccessMgtAddresstype_Type(Integer32):
    """Custom type fgs2528kxAccessMgtAddresstype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxAccessMgtAddresstype_Type.__name__ = "Integer32"
_Fgs2528kxAccessMgtAddresstype_Object = MibTableColumn
fgs2528kxAccessMgtAddresstype = _Fgs2528kxAccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3, 1, 2),
    _Fgs2528kxAccessMgtAddresstype_Type()
)
fgs2528kxAccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtAddresstype.setStatus("current")
_Fgs2528kxAccessMgtStartIpAddress_Type = DisplayString
_Fgs2528kxAccessMgtStartIpAddress_Object = MibTableColumn
fgs2528kxAccessMgtStartIpAddress = _Fgs2528kxAccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3, 1, 3),
    _Fgs2528kxAccessMgtStartIpAddress_Type()
)
fgs2528kxAccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtStartIpAddress.setStatus("current")
_Fgs2528kxAccessMgtEndIpAddress_Type = DisplayString
_Fgs2528kxAccessMgtEndIpAddress_Object = MibTableColumn
fgs2528kxAccessMgtEndIpAddress = _Fgs2528kxAccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3, 1, 4),
    _Fgs2528kxAccessMgtEndIpAddress_Type()
)
fgs2528kxAccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtEndIpAddress.setStatus("current")


class _Fgs2528kxAccessMgtHttpHttps_Type(Integer32):
    """Custom type fgs2528kxAccessMgtHttpHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxAccessMgtHttpHttps_Type.__name__ = "Integer32"
_Fgs2528kxAccessMgtHttpHttps_Object = MibTableColumn
fgs2528kxAccessMgtHttpHttps = _Fgs2528kxAccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3, 1, 5),
    _Fgs2528kxAccessMgtHttpHttps_Type()
)
fgs2528kxAccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtHttpHttps.setStatus("current")


class _Fgs2528kxAccessMgtSNMP_Type(Integer32):
    """Custom type fgs2528kxAccessMgtSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxAccessMgtSNMP_Type.__name__ = "Integer32"
_Fgs2528kxAccessMgtSNMP_Object = MibTableColumn
fgs2528kxAccessMgtSNMP = _Fgs2528kxAccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3, 1, 6),
    _Fgs2528kxAccessMgtSNMP_Type()
)
fgs2528kxAccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtSNMP.setStatus("current")


class _Fgs2528kxAccessMgtTelnetSSH_Type(Integer32):
    """Custom type fgs2528kxAccessMgtTelnetSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxAccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Fgs2528kxAccessMgtTelnetSSH_Object = MibTableColumn
fgs2528kxAccessMgtTelnetSSH = _Fgs2528kxAccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3, 1, 7),
    _Fgs2528kxAccessMgtTelnetSSH_Type()
)
fgs2528kxAccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtTelnetSSH.setStatus("current")


class _Fgs2528kxAccessMgtRowStatus_Type(Integer32):
    """Custom type fgs2528kxAccessMgtRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Fgs2528kxAccessMgtRowStatus_Type.__name__ = "Integer32"
_Fgs2528kxAccessMgtRowStatus_Object = MibTableColumn
fgs2528kxAccessMgtRowStatus = _Fgs2528kxAccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 1, 3, 1, 8),
    _Fgs2528kxAccessMgtRowStatus_Type()
)
fgs2528kxAccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtRowStatus.setStatus("current")
_Fgs2528kxAccessMgtStatistics_ObjectIdentity = ObjectIdentity
fgs2528kxAccessMgtStatistics = _Fgs2528kxAccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2)
)
_Fgs2528kxHttpReceivedPkts_Type = Counter32
_Fgs2528kxHttpReceivedPkts_Object = MibScalar
fgs2528kxHttpReceivedPkts = _Fgs2528kxHttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 1),
    _Fgs2528kxHttpReceivedPkts_Type()
)
fgs2528kxHttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxHttpReceivedPkts.setStatus("current")
_Fgs2528kxHttpAllowedPkts_Type = Counter32
_Fgs2528kxHttpAllowedPkts_Object = MibScalar
fgs2528kxHttpAllowedPkts = _Fgs2528kxHttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 2),
    _Fgs2528kxHttpAllowedPkts_Type()
)
fgs2528kxHttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxHttpAllowedPkts.setStatus("current")
_Fgs2528kxHttpDiscardedPkts_Type = Counter32
_Fgs2528kxHttpDiscardedPkts_Object = MibScalar
fgs2528kxHttpDiscardedPkts = _Fgs2528kxHttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 3),
    _Fgs2528kxHttpDiscardedPkts_Type()
)
fgs2528kxHttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxHttpDiscardedPkts.setStatus("current")
_Fgs2528kxHttpsReceivedPkts_Type = Counter32
_Fgs2528kxHttpsReceivedPkts_Object = MibScalar
fgs2528kxHttpsReceivedPkts = _Fgs2528kxHttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 4),
    _Fgs2528kxHttpsReceivedPkts_Type()
)
fgs2528kxHttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxHttpsReceivedPkts.setStatus("current")
_Fgs2528kxHttpsAllowedPkts_Type = Counter32
_Fgs2528kxHttpsAllowedPkts_Object = MibScalar
fgs2528kxHttpsAllowedPkts = _Fgs2528kxHttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 5),
    _Fgs2528kxHttpsAllowedPkts_Type()
)
fgs2528kxHttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxHttpsAllowedPkts.setStatus("current")
_Fgs2528kxHttpsDiscardedPkts_Type = Counter32
_Fgs2528kxHttpsDiscardedPkts_Object = MibScalar
fgs2528kxHttpsDiscardedPkts = _Fgs2528kxHttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 6),
    _Fgs2528kxHttpsDiscardedPkts_Type()
)
fgs2528kxHttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxHttpsDiscardedPkts.setStatus("current")
_Fgs2528kxSnmpReceivedPkts_Type = Counter32
_Fgs2528kxSnmpReceivedPkts_Object = MibScalar
fgs2528kxSnmpReceivedPkts = _Fgs2528kxSnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 7),
    _Fgs2528kxSnmpReceivedPkts_Type()
)
fgs2528kxSnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSnmpReceivedPkts.setStatus("current")
_Fgs2528kxSnmpAllowedPkts_Type = Counter32
_Fgs2528kxSnmpAllowedPkts_Object = MibScalar
fgs2528kxSnmpAllowedPkts = _Fgs2528kxSnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 8),
    _Fgs2528kxSnmpAllowedPkts_Type()
)
fgs2528kxSnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSnmpAllowedPkts.setStatus("current")
_Fgs2528kxSnmpDiscardedPkts_Type = Counter32
_Fgs2528kxSnmpDiscardedPkts_Object = MibScalar
fgs2528kxSnmpDiscardedPkts = _Fgs2528kxSnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 9),
    _Fgs2528kxSnmpDiscardedPkts_Type()
)
fgs2528kxSnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSnmpDiscardedPkts.setStatus("current")
_Fgs2528kxTelnetReceivedPkts_Type = Counter32
_Fgs2528kxTelnetReceivedPkts_Object = MibScalar
fgs2528kxTelnetReceivedPkts = _Fgs2528kxTelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 10),
    _Fgs2528kxTelnetReceivedPkts_Type()
)
fgs2528kxTelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxTelnetReceivedPkts.setStatus("current")
_Fgs2528kxTelnetAllowedPkts_Type = Counter32
_Fgs2528kxTelnetAllowedPkts_Object = MibScalar
fgs2528kxTelnetAllowedPkts = _Fgs2528kxTelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 11),
    _Fgs2528kxTelnetAllowedPkts_Type()
)
fgs2528kxTelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxTelnetAllowedPkts.setStatus("current")
_Fgs2528kxTelnetDiscardedPkts_Type = Counter32
_Fgs2528kxTelnetDiscardedPkts_Object = MibScalar
fgs2528kxTelnetDiscardedPkts = _Fgs2528kxTelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 12),
    _Fgs2528kxTelnetDiscardedPkts_Type()
)
fgs2528kxTelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxTelnetDiscardedPkts.setStatus("current")
_Fgs2528kxSSHReceivedPkts_Type = Counter32
_Fgs2528kxSSHReceivedPkts_Object = MibScalar
fgs2528kxSSHReceivedPkts = _Fgs2528kxSSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 13),
    _Fgs2528kxSSHReceivedPkts_Type()
)
fgs2528kxSSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSSHReceivedPkts.setStatus("current")
_Fgs2528kxSSHAllowedPkts_Type = Counter32
_Fgs2528kxSSHAllowedPkts_Object = MibScalar
fgs2528kxSSHAllowedPkts = _Fgs2528kxSSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 14),
    _Fgs2528kxSSHAllowedPkts_Type()
)
fgs2528kxSSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSSHAllowedPkts.setStatus("current")
_Fgs2528kxSSHDiscardedPkts_Type = Counter32
_Fgs2528kxSSHDiscardedPkts_Object = MibScalar
fgs2528kxSSHDiscardedPkts = _Fgs2528kxSSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 15),
    _Fgs2528kxSSHDiscardedPkts_Type()
)
fgs2528kxSSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxSSHDiscardedPkts.setStatus("current")


class _Fgs2528kxAccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type fgs2528kxAccessMgtStatisticsClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxAccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Fgs2528kxAccessMgtStatisticsClearAll_Object = MibScalar
fgs2528kxAccessMgtStatisticsClearAll = _Fgs2528kxAccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 6, 2, 16),
    _Fgs2528kxAccessMgtStatisticsClearAll_Type()
)
fgs2528kxAccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxAccessMgtStatisticsClearAll.setStatus("current")
_Fgs2528kxSSH_ObjectIdentity = ObjectIdentity
fgs2528kxSSH = _Fgs2528kxSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 7)
)


class _Fgs2528kxSSHMode_Type(Integer32):
    """Custom type fgs2528kxSSHMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSSHMode_Type.__name__ = "Integer32"
_Fgs2528kxSSHMode_Object = MibScalar
fgs2528kxSSHMode = _Fgs2528kxSSHMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 7, 1),
    _Fgs2528kxSSHMode_Type()
)
fgs2528kxSSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSSHMode.setStatus("current")
_Fgs2528kxHTTPS_ObjectIdentity = ObjectIdentity
fgs2528kxHTTPS = _Fgs2528kxHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 8)
)


class _Fgs2528kxHTTPSMode_Type(Integer32):
    """Custom type fgs2528kxHTTPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxHTTPSMode_Type.__name__ = "Integer32"
_Fgs2528kxHTTPSMode_Object = MibScalar
fgs2528kxHTTPSMode = _Fgs2528kxHTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 8, 1),
    _Fgs2528kxHTTPSMode_Type()
)
fgs2528kxHTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxHTTPSMode.setStatus("current")


class _Fgs2528kxHTTPSAutoRedirect_Type(Integer32):
    """Custom type fgs2528kxHTTPSAutoRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxHTTPSAutoRedirect_Type.__name__ = "Integer32"
_Fgs2528kxHTTPSAutoRedirect_Object = MibScalar
fgs2528kxHTTPSAutoRedirect = _Fgs2528kxHTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 8, 2),
    _Fgs2528kxHTTPSAutoRedirect_Type()
)
fgs2528kxHTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxHTTPSAutoRedirect.setStatus("current")
_Fgs2528kxAuthMethod_ObjectIdentity = ObjectIdentity
fgs2528kxAuthMethod = _Fgs2528kxAuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 9)
)


class _Fgs2528kxConsoleAuthMethod_Type(Integer32):
    """Custom type fgs2528kxConsoleAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxConsoleAuthMethod_Type.__name__ = "Integer32"
_Fgs2528kxConsoleAuthMethod_Object = MibScalar
fgs2528kxConsoleAuthMethod = _Fgs2528kxConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 9, 1),
    _Fgs2528kxConsoleAuthMethod_Type()
)
fgs2528kxConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxConsoleAuthMethod.setStatus("current")


class _Fgs2528kxConsoleFallback_Type(Integer32):
    """Custom type fgs2528kxConsoleFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxConsoleFallback_Type.__name__ = "Integer32"
_Fgs2528kxConsoleFallback_Object = MibScalar
fgs2528kxConsoleFallback = _Fgs2528kxConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 9, 2),
    _Fgs2528kxConsoleFallback_Type()
)
fgs2528kxConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxConsoleFallback.setStatus("current")


class _Fgs2528kxTelnetAuthMethod_Type(Integer32):
    """Custom type fgs2528kxTelnetAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxTelnetAuthMethod_Type.__name__ = "Integer32"
_Fgs2528kxTelnetAuthMethod_Object = MibScalar
fgs2528kxTelnetAuthMethod = _Fgs2528kxTelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 9, 3),
    _Fgs2528kxTelnetAuthMethod_Type()
)
fgs2528kxTelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTelnetAuthMethod.setStatus("current")


class _Fgs2528kxTelnetFallback_Type(Integer32):
    """Custom type fgs2528kxTelnetFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxTelnetFallback_Type.__name__ = "Integer32"
_Fgs2528kxTelnetFallback_Object = MibScalar
fgs2528kxTelnetFallback = _Fgs2528kxTelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 9, 4),
    _Fgs2528kxTelnetFallback_Type()
)
fgs2528kxTelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxTelnetFallback.setStatus("current")


class _Fgs2528kxSshAuthMethod_Type(Integer32):
    """Custom type fgs2528kxSshAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxSshAuthMethod_Type.__name__ = "Integer32"
_Fgs2528kxSshAuthMethod_Object = MibScalar
fgs2528kxSshAuthMethod = _Fgs2528kxSshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 9, 5),
    _Fgs2528kxSshAuthMethod_Type()
)
fgs2528kxSshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSshAuthMethod.setStatus("current")


class _Fgs2528kxSshFallback_Type(Integer32):
    """Custom type fgs2528kxSshFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSshFallback_Type.__name__ = "Integer32"
_Fgs2528kxSshFallback_Object = MibScalar
fgs2528kxSshFallback = _Fgs2528kxSshFallback_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 9, 6),
    _Fgs2528kxSshFallback_Type()
)
fgs2528kxSshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSshFallback.setStatus("current")


class _Fgs2528kxWebAuthMethod_Type(Integer32):
    """Custom type fgs2528kxWebAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fgs2528kxWebAuthMethod_Type.__name__ = "Integer32"
_Fgs2528kxWebAuthMethod_Object = MibScalar
fgs2528kxWebAuthMethod = _Fgs2528kxWebAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 9, 7),
    _Fgs2528kxWebAuthMethod_Type()
)
fgs2528kxWebAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxWebAuthMethod.setStatus("current")


class _Fgs2528kxWebFallback_Type(Integer32):
    """Custom type fgs2528kxWebFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxWebFallback_Type.__name__ = "Integer32"
_Fgs2528kxWebFallback_Object = MibScalar
fgs2528kxWebFallback = _Fgs2528kxWebFallback_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 3, 9, 8),
    _Fgs2528kxWebFallback_Type()
)
fgs2528kxWebFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxWebFallback.setStatus("current")
_Fgs2528kxMaintenance_ObjectIdentity = ObjectIdentity
fgs2528kxMaintenance = _Fgs2528kxMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4)
)


class _Fgs2528kxRestartDevice_Type(Integer32):
    """Custom type fgs2528kxRestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxRestartDevice_Type.__name__ = "Integer32"
_Fgs2528kxRestartDevice_Object = MibScalar
fgs2528kxRestartDevice = _Fgs2528kxRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 1),
    _Fgs2528kxRestartDevice_Type()
)
fgs2528kxRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxRestartDevice.setStatus("current")
_Fgs2528kxFirmware_ObjectIdentity = ObjectIdentity
fgs2528kxFirmware = _Fgs2528kxFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 2)
)
_Fgs2528kxFirmwareIpAddress_Type = IpAddress
_Fgs2528kxFirmwareIpAddress_Object = MibScalar
fgs2528kxFirmwareIpAddress = _Fgs2528kxFirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 2, 1),
    _Fgs2528kxFirmwareIpAddress_Type()
)
fgs2528kxFirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxFirmwareIpAddress.setStatus("current")
_Fgs2528kxFirmwareFileName_Type = DisplayString
_Fgs2528kxFirmwareFileName_Object = MibScalar
fgs2528kxFirmwareFileName = _Fgs2528kxFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 2, 2),
    _Fgs2528kxFirmwareFileName_Type()
)
fgs2528kxFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxFirmwareFileName.setStatus("current")


class _Fgs2528kxDoFirmwareUpgrade_Type(Integer32):
    """Custom type fgs2528kxDoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDoFirmwareUpgrade_Type.__name__ = "Integer32"
_Fgs2528kxDoFirmwareUpgrade_Object = MibScalar
fgs2528kxDoFirmwareUpgrade = _Fgs2528kxDoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 2, 3),
    _Fgs2528kxDoFirmwareUpgrade_Type()
)
fgs2528kxDoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDoFirmwareUpgrade.setStatus("current")
_Fgs2528kxSaveOrRestore_ObjectIdentity = ObjectIdentity
fgs2528kxSaveOrRestore = _Fgs2528kxSaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 3)
)


class _Fgs2528kxFactoryDefaults_Type(Integer32):
    """Custom type fgs2528kxFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxFactoryDefaults_Type.__name__ = "Integer32"
_Fgs2528kxFactoryDefaults_Object = MibScalar
fgs2528kxFactoryDefaults = _Fgs2528kxFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 3, 1),
    _Fgs2528kxFactoryDefaults_Type()
)
fgs2528kxFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxFactoryDefaults.setStatus("current")


class _Fgs2528kxSaveStart_Type(Integer32):
    """Custom type fgs2528kxSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSaveStart_Type.__name__ = "Integer32"
_Fgs2528kxSaveStart_Object = MibScalar
fgs2528kxSaveStart = _Fgs2528kxSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 3, 2),
    _Fgs2528kxSaveStart_Type()
)
fgs2528kxSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSaveStart.setStatus("current")


class _Fgs2528kxSaveUser_Type(Integer32):
    """Custom type fgs2528kxSaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxSaveUser_Type.__name__ = "Integer32"
_Fgs2528kxSaveUser_Object = MibScalar
fgs2528kxSaveUser = _Fgs2528kxSaveUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 3, 3),
    _Fgs2528kxSaveUser_Type()
)
fgs2528kxSaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxSaveUser.setStatus("current")


class _Fgs2528kxRestoreUser_Type(Integer32):
    """Custom type fgs2528kxRestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxRestoreUser_Type.__name__ = "Integer32"
_Fgs2528kxRestoreUser_Object = MibScalar
fgs2528kxRestoreUser = _Fgs2528kxRestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 3, 4),
    _Fgs2528kxRestoreUser_Type()
)
fgs2528kxRestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxRestoreUser.setStatus("current")
_Fgs2528kxExportOrImport_ObjectIdentity = ObjectIdentity
fgs2528kxExportOrImport = _Fgs2528kxExportOrImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 4)
)
_Fgs2528kxExportIpAddress_Type = IpAddress
_Fgs2528kxExportIpAddress_Object = MibScalar
fgs2528kxExportIpAddress = _Fgs2528kxExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 4, 1),
    _Fgs2528kxExportIpAddress_Type()
)
fgs2528kxExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxExportIpAddress.setStatus("current")
_Fgs2528kxExportConfigName_Type = DisplayString
_Fgs2528kxExportConfigName_Object = MibScalar
fgs2528kxExportConfigName = _Fgs2528kxExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 4, 2),
    _Fgs2528kxExportConfigName_Type()
)
fgs2528kxExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxExportConfigName.setStatus("current")


class _Fgs2528kxDoExportConfig_Type(Integer32):
    """Custom type fgs2528kxDoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDoExportConfig_Type.__name__ = "Integer32"
_Fgs2528kxDoExportConfig_Object = MibScalar
fgs2528kxDoExportConfig = _Fgs2528kxDoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 4, 3),
    _Fgs2528kxDoExportConfig_Type()
)
fgs2528kxDoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDoExportConfig.setStatus("current")
_Fgs2528kxImportIpAddress_Type = IpAddress
_Fgs2528kxImportIpAddress_Object = MibScalar
fgs2528kxImportIpAddress = _Fgs2528kxImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 4, 4),
    _Fgs2528kxImportIpAddress_Type()
)
fgs2528kxImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxImportIpAddress.setStatus("current")
_Fgs2528kxImportConfigName_Type = DisplayString
_Fgs2528kxImportConfigName_Object = MibScalar
fgs2528kxImportConfigName = _Fgs2528kxImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 4, 5),
    _Fgs2528kxImportConfigName_Type()
)
fgs2528kxImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxImportConfigName.setStatus("current")


class _Fgs2528kxDoImportConfig_Type(Integer32):
    """Custom type fgs2528kxDoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDoImportConfig_Type.__name__ = "Integer32"
_Fgs2528kxDoImportConfig_Object = MibScalar
fgs2528kxDoImportConfig = _Fgs2528kxDoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 4, 6),
    _Fgs2528kxDoImportConfig_Type()
)
fgs2528kxDoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDoImportConfig.setStatus("current")
_Fgs2528kxDiagnostics_ObjectIdentity = ObjectIdentity
fgs2528kxDiagnostics = _Fgs2528kxDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5)
)
_Fgs2528kxPingIpAddress_Type = IpAddress
_Fgs2528kxPingIpAddress_Object = MibScalar
fgs2528kxPingIpAddress = _Fgs2528kxPingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 1),
    _Fgs2528kxPingIpAddress_Type()
)
fgs2528kxPingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPingIpAddress.setStatus("current")


class _Fgs2528kxPingSize_Type(Integer32):
    """Custom type fgs2528kxPingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Fgs2528kxPingSize_Type.__name__ = "Integer32"
_Fgs2528kxPingSize_Object = MibScalar
fgs2528kxPingSize = _Fgs2528kxPingSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 2),
    _Fgs2528kxPingSize_Type()
)
fgs2528kxPingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPingSize.setStatus("current")


class _Fgs2528kxDoPingConfig_Type(Integer32):
    """Custom type fgs2528kxDoPingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDoPingConfig_Type.__name__ = "Integer32"
_Fgs2528kxDoPingConfig_Object = MibScalar
fgs2528kxDoPingConfig = _Fgs2528kxDoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 3),
    _Fgs2528kxDoPingConfig_Type()
)
fgs2528kxDoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDoPingConfig.setStatus("current")
_Fgs2528kxPingResult_Type = DisplayString
_Fgs2528kxPingResult_Object = MibScalar
fgs2528kxPingResult = _Fgs2528kxPingResult_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 4),
    _Fgs2528kxPingResult_Type()
)
fgs2528kxPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPingResult.setStatus("current")
_Fgs2528kxPing6IpAddress_Type = DisplayString
_Fgs2528kxPing6IpAddress_Object = MibScalar
fgs2528kxPing6IpAddress = _Fgs2528kxPing6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 5),
    _Fgs2528kxPing6IpAddress_Type()
)
fgs2528kxPing6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPing6IpAddress.setStatus("current")


class _Fgs2528kxPing6Size_Type(Integer32):
    """Custom type fgs2528kxPing6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Fgs2528kxPing6Size_Type.__name__ = "Integer32"
_Fgs2528kxPing6Size_Object = MibScalar
fgs2528kxPing6Size = _Fgs2528kxPing6Size_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 6),
    _Fgs2528kxPing6Size_Type()
)
fgs2528kxPing6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxPing6Size.setStatus("current")


class _Fgs2528kxDoPing6Config_Type(Integer32):
    """Custom type fgs2528kxDoPing6Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Fgs2528kxDoPing6Config_Type.__name__ = "Integer32"
_Fgs2528kxDoPing6Config_Object = MibScalar
fgs2528kxDoPing6Config = _Fgs2528kxDoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 7),
    _Fgs2528kxDoPing6Config_Type()
)
fgs2528kxDoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxDoPing6Config.setStatus("current")
_Fgs2528kxPing6Result_Type = DisplayString
_Fgs2528kxPing6Result_Object = MibScalar
fgs2528kxPing6Result = _Fgs2528kxPing6Result_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 8),
    _Fgs2528kxPing6Result_Type()
)
fgs2528kxPing6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxPing6Result.setStatus("current")
_Fgs2528kxVeriPHY_ObjectIdentity = ObjectIdentity
fgs2528kxVeriPHY = _Fgs2528kxVeriPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9)
)


class _Fgs2528kxVeriPHYTest_Type(Integer32):
    """Custom type fgs2528kxVeriPHYTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxVeriPHYTest_Type.__name__ = "Integer32"
_Fgs2528kxVeriPHYTest_Object = MibScalar
fgs2528kxVeriPHYTest = _Fgs2528kxVeriPHYTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 1),
    _Fgs2528kxVeriPHYTest_Type()
)
fgs2528kxVeriPHYTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYTest.setStatus("current")
_Fgs2528kxVeriPHYTable_Object = MibTable
fgs2528kxVeriPHYTable = _Fgs2528kxVeriPHYTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2)
)
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYTable.setStatus("current")
_Fgs2528kxVeriPHYEntry_Object = MibTableRow
fgs2528kxVeriPHYEntry = _Fgs2528kxVeriPHYEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1)
)
fgs2528kxVeriPHYEntry.setIndexNames(
    (0, "RUBYTECH-FGS2528KX-MIB", "fgs2528kxVeriPHYPort"),
)
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYEntry.setStatus("current")


class _Fgs2528kxVeriPHYPort_Type(Integer32):
    """Custom type fgs2528kxVeriPHYPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Fgs2528kxVeriPHYPort_Type.__name__ = "Integer32"
_Fgs2528kxVeriPHYPort_Object = MibTableColumn
fgs2528kxVeriPHYPort = _Fgs2528kxVeriPHYPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1, 1),
    _Fgs2528kxVeriPHYPort_Type()
)
fgs2528kxVeriPHYPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYPort.setStatus("current")
_Fgs2528kxVeriPHYPairA_Type = DisplayString
_Fgs2528kxVeriPHYPairA_Object = MibTableColumn
fgs2528kxVeriPHYPairA = _Fgs2528kxVeriPHYPairA_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1, 2),
    _Fgs2528kxVeriPHYPairA_Type()
)
fgs2528kxVeriPHYPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYPairA.setStatus("current")
_Fgs2528kxVeriPHYLengthA_Type = DisplayString
_Fgs2528kxVeriPHYLengthA_Object = MibTableColumn
fgs2528kxVeriPHYLengthA = _Fgs2528kxVeriPHYLengthA_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1, 3),
    _Fgs2528kxVeriPHYLengthA_Type()
)
fgs2528kxVeriPHYLengthA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYLengthA.setStatus("current")
_Fgs2528kxVeriPHYPairB_Type = DisplayString
_Fgs2528kxVeriPHYPairB_Object = MibTableColumn
fgs2528kxVeriPHYPairB = _Fgs2528kxVeriPHYPairB_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1, 4),
    _Fgs2528kxVeriPHYPairB_Type()
)
fgs2528kxVeriPHYPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYPairB.setStatus("current")
_Fgs2528kxVeriPHYLengthB_Type = DisplayString
_Fgs2528kxVeriPHYLengthB_Object = MibTableColumn
fgs2528kxVeriPHYLengthB = _Fgs2528kxVeriPHYLengthB_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1, 5),
    _Fgs2528kxVeriPHYLengthB_Type()
)
fgs2528kxVeriPHYLengthB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYLengthB.setStatus("current")
_Fgs2528kxVeriPHYPairC_Type = DisplayString
_Fgs2528kxVeriPHYPairC_Object = MibTableColumn
fgs2528kxVeriPHYPairC = _Fgs2528kxVeriPHYPairC_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1, 6),
    _Fgs2528kxVeriPHYPairC_Type()
)
fgs2528kxVeriPHYPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYPairC.setStatus("current")
_Fgs2528kxVeriPHYLengthC_Type = DisplayString
_Fgs2528kxVeriPHYLengthC_Object = MibTableColumn
fgs2528kxVeriPHYLengthC = _Fgs2528kxVeriPHYLengthC_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1, 7),
    _Fgs2528kxVeriPHYLengthC_Type()
)
fgs2528kxVeriPHYLengthC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYLengthC.setStatus("current")
_Fgs2528kxVeriPHYPairD_Type = DisplayString
_Fgs2528kxVeriPHYPairD_Object = MibTableColumn
fgs2528kxVeriPHYPairD = _Fgs2528kxVeriPHYPairD_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1, 8),
    _Fgs2528kxVeriPHYPairD_Type()
)
fgs2528kxVeriPHYPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYPairD.setStatus("current")
_Fgs2528kxVeriPHYLengthD_Type = DisplayString
_Fgs2528kxVeriPHYLengthD_Object = MibTableColumn
fgs2528kxVeriPHYLengthD = _Fgs2528kxVeriPHYLengthD_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 4, 5, 9, 2, 1, 9),
    _Fgs2528kxVeriPHYLengthD_Type()
)
fgs2528kxVeriPHYLengthD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxVeriPHYLengthD.setStatus("current")
_Fgs2528kxTrap_ObjectIdentity = ObjectIdentity
fgs2528kxTrap = _Fgs2528kxTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5)
)
_Fgs2528kxTrapEvent_ObjectIdentity = ObjectIdentity
fgs2528kxTrapEvent = _Fgs2528kxTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 1)
)
_Fgs2528kxTrapVariable_ObjectIdentity = ObjectIdentity
fgs2528kxTrapVariable = _Fgs2528kxTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 2)
)
_Fgs2528kxInformation_Type = DisplayString
_Fgs2528kxInformation_Object = MibScalar
fgs2528kxInformation = _Fgs2528kxInformation_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 2, 1),
    _Fgs2528kxInformation_Type()
)
fgs2528kxInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgs2528kxInformation.setStatus("current")

# Managed Objects groups


# Notification objects

fgs2528kxEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 1, 1)
)
fgs2528kxEmergency.setObjects(
    ("RUBYTECH-FGS2528KX-MIB", "fgs2528kxInformation")
)
if mibBuilder.loadTexts:
    fgs2528kxEmergency.setStatus(
        "current"
    )

fgs2528kxAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 1, 2)
)
fgs2528kxAlert.setObjects(
    ("RUBYTECH-FGS2528KX-MIB", "fgs2528kxInformation")
)
if mibBuilder.loadTexts:
    fgs2528kxAlert.setStatus(
        "current"
    )

fgs2528kxCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 1, 3)
)
fgs2528kxCritical.setObjects(
    ("RUBYTECH-FGS2528KX-MIB", "fgs2528kxInformation")
)
if mibBuilder.loadTexts:
    fgs2528kxCritical.setStatus(
        "current"
    )

fgs2528kxError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 1, 4)
)
fgs2528kxError.setObjects(
    ("RUBYTECH-FGS2528KX-MIB", "fgs2528kxInformation")
)
if mibBuilder.loadTexts:
    fgs2528kxError.setStatus(
        "current"
    )

fgs2528kxWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 1, 5)
)
fgs2528kxWarning.setObjects(
    ("RUBYTECH-FGS2528KX-MIB", "fgs2528kxInformation")
)
if mibBuilder.loadTexts:
    fgs2528kxWarning.setStatus(
        "current"
    )

fgs2528kxNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 1, 6)
)
fgs2528kxNotice.setObjects(
    ("RUBYTECH-FGS2528KX-MIB", "fgs2528kxInformation")
)
if mibBuilder.loadTexts:
    fgs2528kxNotice.setStatus(
        "current"
    )

fgs2528kxInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 1, 7)
)
fgs2528kxInformational.setObjects(
    ("RUBYTECH-FGS2528KX-MIB", "fgs2528kxInformation")
)
if mibBuilder.loadTexts:
    fgs2528kxInformational.setStatus(
        "current"
    )

fgs2528kxDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 77, 5, 1, 8)
)
fgs2528kxDebug.setObjects(
    ("RUBYTECH-FGS2528KX-MIB", "fgs2528kxInformation")
)
if mibBuilder.loadTexts:
    fgs2528kxDebug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUBYTECH-FGS2528KX-MIB",
    **{"rubytech": rubytech,
       "switch": switch,
       "fgs2528kxProductId": fgs2528kxProductId,
       "fgs2528kxSystem": fgs2528kxSystem,
       "fgs2528kxSystemInformation": fgs2528kxSystemInformation,
       "fgs2528kxModelName": fgs2528kxModelName,
       "fgs2528kxBIOSVersion": fgs2528kxBIOSVersion,
       "fgs2528kxFirmwareVersion": fgs2528kxFirmwareVersion,
       "fgs2528kxHardwareMechanicalVersion": fgs2528kxHardwareMechanicalVersion,
       "fgs2528kxSeriesNumber": fgs2528kxSeriesNumber,
       "fgs2528kxHostMACAddress": fgs2528kxHostMACAddress,
       "fgs2528kxConsoleBaudrate": fgs2528kxConsoleBaudrate,
       "fgs2528kxRAMSize": fgs2528kxRAMSize,
       "fgs2528kxFlashSize": fgs2528kxFlashSize,
       "fgs2528kxBridgeFBDSize": fgs2528kxBridgeFBDSize,
       "fgs2528kxTransmitQueue": fgs2528kxTransmitQueue,
       "fgs2528kxMaximumFrameSize": fgs2528kxMaximumFrameSize,
       "fgs2528kxCPULoad": fgs2528kxCPULoad,
       "fgs2528kxFanSpeed": fgs2528kxFanSpeed,
       "fgs2528kxPowers": fgs2528kxPowers,
       "fgs2528kxTemperature1": fgs2528kxTemperature1,
       "fgs2528kxTemperature2": fgs2528kxTemperature2,
       "fgs2528kxTemperature3": fgs2528kxTemperature3,
       "fgs2528kxTemperature4": fgs2528kxTemperature4,
       "fgs2528kxSystemTime": fgs2528kxSystemTime,
       "fgs2528kxSystemTimeManual": fgs2528kxSystemTimeManual,
       "fgs2528kxSystemTimeManualClockSource": fgs2528kxSystemTimeManualClockSource,
       "fgs2528kxSystemTimeManualLocaltime": fgs2528kxSystemTimeManualLocaltime,
       "fgs2528kxSystemTimeManualTimeZoneOffset": fgs2528kxSystemTimeManualTimeZoneOffset,
       "fgs2528kxSystemTimeManualDaylightSavings": fgs2528kxSystemTimeManualDaylightSavings,
       "fgs2528kxSystemTimeManualTimeSetOffset": fgs2528kxSystemTimeManualTimeSetOffset,
       "fgs2528kxSystemTimeManualDaylightSavingsType": fgs2528kxSystemTimeManualDaylightSavingsType,
       "fgs2528kxSystemTimeManualDaylightSavingsBydatesFrom": fgs2528kxSystemTimeManualDaylightSavingsBydatesFrom,
       "fgs2528kxSystemTimeManualDaylightSavingsBydatesTo": fgs2528kxSystemTimeManualDaylightSavingsBydatesTo,
       "fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom": fgs2528kxSystemTimeManualDaylightSavingsRecurringDayFrom,
       "fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom": fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekFrom,
       "fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom": fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthFrom,
       "fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeFrom": fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeFrom,
       "fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo": fgs2528kxSystemTimeManualDaylightSavingsRecurringDayTo,
       "fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo": fgs2528kxSystemTimeManualDaylightSavingsRecurringWeekTo,
       "fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo": fgs2528kxSystemTimeManualDaylightSavingsRecurringMonthTo,
       "fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeTo": fgs2528kxSystemTimeManualDaylightSavingsRecurringTimeTo,
       "fgs2528kxSystemTimeNTP": fgs2528kxSystemTimeNTP,
       "fgs2528kxSystemTimeNTPTable": fgs2528kxSystemTimeNTPTable,
       "fgs2528kxSystemTimeNTPEntry": fgs2528kxSystemTimeNTPEntry,
       "fgs2528kxSystemTimeNTPIndex": fgs2528kxSystemTimeNTPIndex,
       "fgs2528kxSystemTimeNTPServerIPType": fgs2528kxSystemTimeNTPServerIPType,
       "fgs2528kxSystemTimeNTPServer": fgs2528kxSystemTimeNTPServer,
       "fgs2528kxSystemTimeNTPCurrentMode": fgs2528kxSystemTimeNTPCurrentMode,
       "fgs2528kxSystemAccount": fgs2528kxSystemAccount,
       "fgs2528kxSystemAccountUsers": fgs2528kxSystemAccountUsers,
       "fgs2528kxSystemAccountUserCreate": fgs2528kxSystemAccountUserCreate,
       "fgs2528kxSystemAccountUsersTable": fgs2528kxSystemAccountUsersTable,
       "fgs2528kxSystemAccountUsersEntry": fgs2528kxSystemAccountUsersEntry,
       "fgs2528kxUserIndex": fgs2528kxUserIndex,
       "fgs2528kxUserName": fgs2528kxUserName,
       "fgs2528kxPassword": fgs2528kxPassword,
       "fgs2528kxUserPrivilegeLevel": fgs2528kxUserPrivilegeLevel,
       "fgs2528kxAccountUserRowStatus": fgs2528kxAccountUserRowStatus,
       "fgs2528kxSystemAccountPrivilegeLevel": fgs2528kxSystemAccountPrivilegeLevel,
       "fgs2528kxAccountPrivilegeLevel": fgs2528kxAccountPrivilegeLevel,
       "fgs2528kxAggregationPrivilegeLevel": fgs2528kxAggregationPrivilegeLevel,
       "fgs2528kxDiagnosticsPrivilegeLevel": fgs2528kxDiagnosticsPrivilegeLevel,
       "fgs2528kxEPSPrivilegeLevel": fgs2528kxEPSPrivilegeLevel,
       "fgs2528kxERPSPrivilegeLevel": fgs2528kxERPSPrivilegeLevel,
       "fgs2528kxETHLinkOAMPrivilegeLevel": fgs2528kxETHLinkOAMPrivilegeLevel,
       "fgs2528kxEVCPrivilegeLevel": fgs2528kxEVCPrivilegeLevel,
       "fgs2528kxGARPPrivilegeLevel": fgs2528kxGARPPrivilegeLevel,
       "fgs2528kxGVRPPrivilegeLevel": fgs2528kxGVRPPrivilegeLevel,
       "fgs2528kxIPPrivilegeLevel": fgs2528kxIPPrivilegeLevel,
       "fgs2528kxIPMCSnoopingPrivilegeLevel": fgs2528kxIPMCSnoopingPrivilegeLevel,
       "fgs2528kxLACPPrivilegeLevel": fgs2528kxLACPPrivilegeLevel,
       "fgs2528kxLLDPPrivilegeLevel": fgs2528kxLLDPPrivilegeLevel,
       "fgs2528kxLLDPMEDPrivilegeLevel": fgs2528kxLLDPMEDPrivilegeLevel,
       "fgs2528kxLoopProtectPrivilegeLevel": fgs2528kxLoopProtectPrivilegeLevel,
       "fgs2528kxMACTablePrivilegeLevel": fgs2528kxMACTablePrivilegeLevel,
       "fgs2528kxMEPPrivilegeLevel": fgs2528kxMEPPrivilegeLevel,
       "fgs2528kxMVRPrivilegeLevel": fgs2528kxMVRPrivilegeLevel,
       "fgs2528kxMaintenancePrivilegeLevel": fgs2528kxMaintenancePrivilegeLevel,
       "fgs2528kxMirroringPrivilegeLevel": fgs2528kxMirroringPrivilegeLevel,
       "fgs2528kxPTPPrivilegeLevel": fgs2528kxPTPPrivilegeLevel,
       "fgs2528kxPortsPrivilegeLevel": fgs2528kxPortsPrivilegeLevel,
       "fgs2528kxPrivateVLANsPrivilegeLevel": fgs2528kxPrivateVLANsPrivilegeLevel,
       "fgs2528kxQoSPrivilegeLevel": fgs2528kxQoSPrivilegeLevel,
       "fgs2528kxSMTPPrivilegeLevel": fgs2528kxSMTPPrivilegeLevel,
       "fgs2528kxSNMPPrivilegeLevel": fgs2528kxSNMPPrivilegeLevel,
       "fgs2528kxSecurityPrivilegeLevel": fgs2528kxSecurityPrivilegeLevel,
       "fgs2528kxSpanningTreePrivilegeLevel": fgs2528kxSpanningTreePrivilegeLevel,
       "fgs2528kxSystemPrivilegeLevel": fgs2528kxSystemPrivilegeLevel,
       "fgs2528kxTrapEventPrivilegeLevel": fgs2528kxTrapEventPrivilegeLevel,
       "fgs2528kxVCLPrivilegeLevel": fgs2528kxVCLPrivilegeLevel,
       "fgs2528kxVLANTranslationPrivilegeLevel": fgs2528kxVLANTranslationPrivilegeLevel,
       "fgs2528kxVLANsPrivilegeLevel": fgs2528kxVLANsPrivilegeLevel,
       "fgs2528kxIP": fgs2528kxIP,
       "fgs2528kxIPv4": fgs2528kxIPv4,
       "fgs2528kxIPv4Configured": fgs2528kxIPv4Configured,
       "fgs2528kxIpv4DHCPClient": fgs2528kxIpv4DHCPClient,
       "fgs2528kxIPv4Address": fgs2528kxIPv4Address,
       "fgs2528kxIPv4Mask": fgs2528kxIPv4Mask,
       "fgs2528kxIPv4Router": fgs2528kxIPv4Router,
       "fgs2528kxIPv4VLANId": fgs2528kxIPv4VLANId,
       "fgs2528kxIPv4DNSServer": fgs2528kxIPv4DNSServer,
       "fgs2528kxIPv4DNSProxy": fgs2528kxIPv4DNSProxy,
       "fgs2528kxIPv4Current": fgs2528kxIPv4Current,
       "fgs2528kxIpv4CurrentDHCPClient": fgs2528kxIpv4CurrentDHCPClient,
       "fgs2528kxIPv4CurrentAddress": fgs2528kxIPv4CurrentAddress,
       "fgs2528kxIPv4CurrentMask": fgs2528kxIPv4CurrentMask,
       "fgs2528kxIPv4CurrentRouter": fgs2528kxIPv4CurrentRouter,
       "fgs2528kxIPv4CurrentVLANId": fgs2528kxIPv4CurrentVLANId,
       "fgs2528kxIPv4CurrentDNSServer": fgs2528kxIPv4CurrentDNSServer,
       "fgs2528kxIPv6": fgs2528kxIPv6,
       "fgs2528kxIPv6Configured": fgs2528kxIPv6Configured,
       "fgs2528kxIpv6AutoConfiguration": fgs2528kxIpv6AutoConfiguration,
       "fgs2528kxIpv6Address": fgs2528kxIpv6Address,
       "fgs2528kxIpv6Prefix": fgs2528kxIpv6Prefix,
       "fgs2528kxIpv6Router": fgs2528kxIpv6Router,
       "fgs2528kxIPv6Current": fgs2528kxIPv6Current,
       "fgs2528kxIpv6CurrentAutoConfiguration": fgs2528kxIpv6CurrentAutoConfiguration,
       "fgs2528kxIpv6CurrentAddress": fgs2528kxIpv6CurrentAddress,
       "fgs2528kxIpv6CurrentLinkLocalAddress": fgs2528kxIpv6CurrentLinkLocalAddress,
       "fgs2528kxIpv6CurrentPrefix": fgs2528kxIpv6CurrentPrefix,
       "fgs2528kxIpv6CurrentRouter": fgs2528kxIpv6CurrentRouter,
       "fgs2528kxSyslog": fgs2528kxSyslog,
       "fgs2528kxSyslogConf": fgs2528kxSyslogConf,
       "fgs2528kxServerMode": fgs2528kxServerMode,
       "fgs2528kxServerAddress1": fgs2528kxServerAddress1,
       "fgs2528kxServerAddress2": fgs2528kxServerAddress2,
       "fgs2528kxSyslogLevel": fgs2528kxSyslogLevel,
       "fgs2528kxSyslogDetailedInfo": fgs2528kxSyslogDetailedInfo,
       "fgs2528kxSyslogDetailedInfoClear": fgs2528kxSyslogDetailedInfoClear,
       "fgs2528kxSyslogDetailedInfoTable": fgs2528kxSyslogDetailedInfoTable,
       "fgs2528kxSyslogDetailedInfoEntry": fgs2528kxSyslogDetailedInfoEntry,
       "fgs2528kxSyslogDetailedInfoIndex": fgs2528kxSyslogDetailedInfoIndex,
       "fgs2528kxSyslogDetailedInfoLevel": fgs2528kxSyslogDetailedInfoLevel,
       "fgs2528kxSyslogDetailedInfoTime": fgs2528kxSyslogDetailedInfoTime,
       "fgs2528kxSyslogDetailedInfoMessage": fgs2528kxSyslogDetailedInfoMessage,
       "fgs2528kxSnmp": fgs2528kxSnmp,
       "fgs2528kxSnmpConf": fgs2528kxSnmpConf,
       "fgs2528kxGetCommunity": fgs2528kxGetCommunity,
       "fgs2528kxSetCommunityMode": fgs2528kxSetCommunityMode,
       "fgs2528kxSetCommunity": fgs2528kxSetCommunity,
       "fgs2528kxTrapHostConfTable": fgs2528kxTrapHostConfTable,
       "fgs2528kxTrapHostConfEntry": fgs2528kxTrapHostConfEntry,
       "fgs2528kxTrapHostConfIndex": fgs2528kxTrapHostConfIndex,
       "fgs2528kxTrapHostConfVersion": fgs2528kxTrapHostConfVersion,
       "fgs2528kxTrapHostConfIPType": fgs2528kxTrapHostConfIPType,
       "fgs2528kxTrapHostConfIP": fgs2528kxTrapHostConfIP,
       "fgs2528kxTrapHostConfPort": fgs2528kxTrapHostConfPort,
       "fgs2528kxTrapHostConfCommunity": fgs2528kxTrapHostConfCommunity,
       "fgs2528kxTrapHostConfSeverityLevel": fgs2528kxTrapHostConfSeverityLevel,
       "fgs2528kxTrapHostConfSecurityLevel": fgs2528kxTrapHostConfSecurityLevel,
       "fgs2528kxTrapHostConfAuthPtc": fgs2528kxTrapHostConfAuthPtc,
       "fgs2528kxTrapHostConfAuthPassword": fgs2528kxTrapHostConfAuthPassword,
       "fgs2528kxTrapHostConfPrivPtc": fgs2528kxTrapHostConfPrivPtc,
       "fgs2528kxTrapHostConfPrivPassword": fgs2528kxTrapHostConfPrivPassword,
       "fgs2528kxTrapHostConfCurrentMode": fgs2528kxTrapHostConfCurrentMode,
       "fgs2528kxConfiguration": fgs2528kxConfiguration,
       "fgs2528kxPort": fgs2528kxPort,
       "fgs2528kxPortConfigurationTable": fgs2528kxPortConfigurationTable,
       "fgs2528kxPortConfigurationEntry": fgs2528kxPortConfigurationEntry,
       "fgs2528kxPortConfPort": fgs2528kxPortConfPort,
       "fgs2528kxPortConfPortMedia": fgs2528kxPortConfPortMedia,
       "fgs2528kxPortConfLink": fgs2528kxPortConfLink,
       "fgs2528kxPortConfCurrentSpeed": fgs2528kxPortConfCurrentSpeed,
       "fgs2528kxPortConfSpeed": fgs2528kxPortConfSpeed,
       "fgs2528kxPortConfCurrentFlowControlRx": fgs2528kxPortConfCurrentFlowControlRx,
       "fgs2528kxPortConfCurrentFlowControlTx": fgs2528kxPortConfCurrentFlowControlTx,
       "fgs2528kxPortConfFlowControl": fgs2528kxPortConfFlowControl,
       "fgs2528kxPortConfMaxFrameSize": fgs2528kxPortConfMaxFrameSize,
       "fgs2528kxPortConfExcessiveCollisionMode": fgs2528kxPortConfExcessiveCollisionMode,
       "fgs2528kxPortConfPowerControl": fgs2528kxPortConfPowerControl,
       "fgs2528kxPortConfDescription": fgs2528kxPortConfDescription,
       "fgs2528kxPortTrafficStatisticsTable": fgs2528kxPortTrafficStatisticsTable,
       "fgs2528kxPortTrafficStatisticsEntry": fgs2528kxPortTrafficStatisticsEntry,
       "fgs2528kxPortTrafficStatisticsPort": fgs2528kxPortTrafficStatisticsPort,
       "fgs2528kxPortTrafficStatisticsClear": fgs2528kxPortTrafficStatisticsClear,
       "fgs2528kxPortTrafficRxPackets": fgs2528kxPortTrafficRxPackets,
       "fgs2528kxPortTrafficRxOctets": fgs2528kxPortTrafficRxOctets,
       "fgs2528kxPortTrafficRxUnicast": fgs2528kxPortTrafficRxUnicast,
       "fgs2528kxPortTrafficRxMulticast": fgs2528kxPortTrafficRxMulticast,
       "fgs2528kxPortTrafficRxBroadcast": fgs2528kxPortTrafficRxBroadcast,
       "fgs2528kxPortTrafficRxPause": fgs2528kxPortTrafficRxPause,
       "fgs2528kxPortTrafficRx64Bytes": fgs2528kxPortTrafficRx64Bytes,
       "fgs2528kxPortTrafficRx65to127Bytes": fgs2528kxPortTrafficRx65to127Bytes,
       "fgs2528kxPortTrafficRx128to255Bytes": fgs2528kxPortTrafficRx128to255Bytes,
       "fgs2528kxPortTrafficRx256to511Bytes": fgs2528kxPortTrafficRx256to511Bytes,
       "fgs2528kxPortTrafficRx512to1023Bytes": fgs2528kxPortTrafficRx512to1023Bytes,
       "fgs2528kxPortTrafficRx1024to1526Bytes": fgs2528kxPortTrafficRx1024to1526Bytes,
       "fgs2528kxPortTrafficRxExceecd1527Bytes": fgs2528kxPortTrafficRxExceecd1527Bytes,
       "fgs2528kxPortTrafficRxQ0": fgs2528kxPortTrafficRxQ0,
       "fgs2528kxPortTrafficRxQ1": fgs2528kxPortTrafficRxQ1,
       "fgs2528kxPortTrafficRxQ2": fgs2528kxPortTrafficRxQ2,
       "fgs2528kxPortTrafficRxQ3": fgs2528kxPortTrafficRxQ3,
       "fgs2528kxPortTrafficRxQ4": fgs2528kxPortTrafficRxQ4,
       "fgs2528kxPortTrafficRxQ5": fgs2528kxPortTrafficRxQ5,
       "fgs2528kxPortTrafficRxQ6": fgs2528kxPortTrafficRxQ6,
       "fgs2528kxPortTrafficRxQ7": fgs2528kxPortTrafficRxQ7,
       "fgs2528kxPortTrafficRxDrops": fgs2528kxPortTrafficRxDrops,
       "fgs2528kxPortTrafficRxCRCorAlignment": fgs2528kxPortTrafficRxCRCorAlignment,
       "fgs2528kxPortTrafficRxUndersize": fgs2528kxPortTrafficRxUndersize,
       "fgs2528kxPortTrafficRxOversize": fgs2528kxPortTrafficRxOversize,
       "fgs2528kxPortTrafficRxFragments": fgs2528kxPortTrafficRxFragments,
       "fgs2528kxPortTrafficRxJabber": fgs2528kxPortTrafficRxJabber,
       "fgs2528kxPortTrafficRxFiltered": fgs2528kxPortTrafficRxFiltered,
       "fgs2528kxPortTrafficTxPackets": fgs2528kxPortTrafficTxPackets,
       "fgs2528kxPortTrafficTxOctets": fgs2528kxPortTrafficTxOctets,
       "fgs2528kxPortTrafficTxUnicast": fgs2528kxPortTrafficTxUnicast,
       "fgs2528kxPortTrafficTxMulticast": fgs2528kxPortTrafficTxMulticast,
       "fgs2528kxPortTrafficTxBroadcast": fgs2528kxPortTrafficTxBroadcast,
       "fgs2528kxPortTrafficTxPause": fgs2528kxPortTrafficTxPause,
       "fgs2528kxPortTrafficTx64Bytes": fgs2528kxPortTrafficTx64Bytes,
       "fgs2528kxPortTrafficTx65to127Bytes": fgs2528kxPortTrafficTx65to127Bytes,
       "fgs2528kxPortTrafficTx128to255Bytes": fgs2528kxPortTrafficTx128to255Bytes,
       "fgs2528kxPortTrafficTx256to511Bytes": fgs2528kxPortTrafficTx256to511Bytes,
       "fgs2528kxPortTrafficTx512to1023Bytes": fgs2528kxPortTrafficTx512to1023Bytes,
       "fgs2528kxPortTrafficTx1024to1526Bytes": fgs2528kxPortTrafficTx1024to1526Bytes,
       "fgs2528kxPortTrafficTxExceecd1527Bytes": fgs2528kxPortTrafficTxExceecd1527Bytes,
       "fgs2528kxPortTrafficTxQ0": fgs2528kxPortTrafficTxQ0,
       "fgs2528kxPortTrafficTxQ1": fgs2528kxPortTrafficTxQ1,
       "fgs2528kxPortTrafficTxQ2": fgs2528kxPortTrafficTxQ2,
       "fgs2528kxPortTrafficTxQ3": fgs2528kxPortTrafficTxQ3,
       "fgs2528kxPortTrafficTxQ4": fgs2528kxPortTrafficTxQ4,
       "fgs2528kxPortTrafficTxQ5": fgs2528kxPortTrafficTxQ5,
       "fgs2528kxPortTrafficTxQ6": fgs2528kxPortTrafficTxQ6,
       "fgs2528kxPortTrafficTxQ7": fgs2528kxPortTrafficTxQ7,
       "fgs2528kxPortTrafficTxDrops": fgs2528kxPortTrafficTxDrops,
       "fgs2528kxPortTrafficTxLateOrExcColl": fgs2528kxPortTrafficTxLateOrExcColl,
       "fgs2528kxPortQoSStatistics": fgs2528kxPortQoSStatistics,
       "fgs2528kxPortQoSStatisticsClear": fgs2528kxPortQoSStatisticsClear,
       "fgs2528kxPortQoSStatisticsTable": fgs2528kxPortQoSStatisticsTable,
       "fgs2528kxPortQoSStatisticsEntry": fgs2528kxPortQoSStatisticsEntry,
       "fgs2528kxPortQoSStatisticsPort": fgs2528kxPortQoSStatisticsPort,
       "fgs2528kxPortQoSQ0Rx": fgs2528kxPortQoSQ0Rx,
       "fgs2528kxPortQoSQ0Tx": fgs2528kxPortQoSQ0Tx,
       "fgs2528kxPortQoSQ1Rx": fgs2528kxPortQoSQ1Rx,
       "fgs2528kxPortQoSQ1Tx": fgs2528kxPortQoSQ1Tx,
       "fgs2528kxPortQoSQ2Rx": fgs2528kxPortQoSQ2Rx,
       "fgs2528kxPortQoSQ2Tx": fgs2528kxPortQoSQ2Tx,
       "fgs2528kxPortQoSQ3Rx": fgs2528kxPortQoSQ3Rx,
       "fgs2528kxPortQoSQ3Tx": fgs2528kxPortQoSQ3Tx,
       "fgs2528kxPortQoSQ4Rx": fgs2528kxPortQoSQ4Rx,
       "fgs2528kxPortQoSQ4Tx": fgs2528kxPortQoSQ4Tx,
       "fgs2528kxPortQoSQ5Rx": fgs2528kxPortQoSQ5Rx,
       "fgs2528kxPortQoSQ5Tx": fgs2528kxPortQoSQ5Tx,
       "fgs2528kxPortQoSQ6Rx": fgs2528kxPortQoSQ6Rx,
       "fgs2528kxPortQoSQ6Tx": fgs2528kxPortQoSQ6Tx,
       "fgs2528kxPortQoSQ7Rx": fgs2528kxPortQoSQ7Rx,
       "fgs2528kxPortQoSQ7Tx": fgs2528kxPortQoSQ7Tx,
       "fgs2528kxSFPInfoTable": fgs2528kxSFPInfoTable,
       "fgs2528kxSFPInfoEntry": fgs2528kxSFPInfoEntry,
       "fgs2528kxSFPInfoIndex": fgs2528kxSFPInfoIndex,
       "fgs2528kxSFPInfoPort": fgs2528kxSFPInfoPort,
       "fgs2528kxSFPConnectorType": fgs2528kxSFPConnectorType,
       "fgs2528kxSFPFiberType": fgs2528kxSFPFiberType,
       "fgs2528kxSFPTxCentralWavelength": fgs2528kxSFPTxCentralWavelength,
       "fgs2528kxSFPBaudRate": fgs2528kxSFPBaudRate,
       "fgs2528kxSFPVendorOUI": fgs2528kxSFPVendorOUI,
       "fgs2528kxSFPVendorName": fgs2528kxSFPVendorName,
       "fgs2528kxSFPVendorPN": fgs2528kxSFPVendorPN,
       "fgs2528kxSFPVendorRev": fgs2528kxSFPVendorRev,
       "fgs2528kxSFPVendorSN": fgs2528kxSFPVendorSN,
       "fgs2528kxSFPDateCode": fgs2528kxSFPDateCode,
       "fgs2528kxSFPTemperature": fgs2528kxSFPTemperature,
       "fgs2528kxSFPVcc": fgs2528kxSFPVcc,
       "fgs2528kxSFPMon1Bias": fgs2528kxSFPMon1Bias,
       "fgs2528kxSFPMon2TxPWR": fgs2528kxSFPMon2TxPWR,
       "fgs2528kxSFPMon3RxPWR": fgs2528kxSFPMon3RxPWR,
       "fgs2528kxGARP": fgs2528kxGARP,
       "fgs2528kxGARPConfTable": fgs2528kxGARPConfTable,
       "fgs2528kxGARPConfEntry": fgs2528kxGARPConfEntry,
       "fgs2528kxGARPConfPort": fgs2528kxGARPConfPort,
       "fgs2528kxGARPJoinTimer": fgs2528kxGARPJoinTimer,
       "fgs2528kxGARPLeaveTimer": fgs2528kxGARPLeaveTimer,
       "fgs2528kxGARPLeaveAllTimer": fgs2528kxGARPLeaveAllTimer,
       "fgs2528kxGARPApplicantion": fgs2528kxGARPApplicantion,
       "fgs2528kxGARPAttributeType": fgs2528kxGARPAttributeType,
       "fgs2528kxGARPApplicant": fgs2528kxGARPApplicant,
       "fgs2528kxGARPStatisticsTable": fgs2528kxGARPStatisticsTable,
       "fgs2528kxGARPStatisticsEntry": fgs2528kxGARPStatisticsEntry,
       "fgs2528kxGARPStatisticsPort": fgs2528kxGARPStatisticsPort,
       "fgs2528kxGARPStatisticsPeerMAC": fgs2528kxGARPStatisticsPeerMAC,
       "fgs2528kxGARPStatisticsFailedCount": fgs2528kxGARPStatisticsFailedCount,
       "fgs2528kxGVRP": fgs2528kxGVRP,
       "fgs2528kxGVRPConf": fgs2528kxGVRPConf,
       "fgs2528kxGVRPMode": fgs2528kxGVRPMode,
       "fgs2528kxGVRPConfTable": fgs2528kxGVRPConfTable,
       "fgs2528kxGVRPConfEntry": fgs2528kxGVRPConfEntry,
       "fgs2528kxGVRPConfPort": fgs2528kxGVRPConfPort,
       "fgs2528kxGVRPConfPortMode": fgs2528kxGVRPConfPortMode,
       "fgs2528kxGVRPConfPortRRole": fgs2528kxGVRPConfPortRRole,
       "fgs2528kxGVRPStatisticsTable": fgs2528kxGVRPStatisticsTable,
       "fgs2528kxGVRPStatisticsEntry": fgs2528kxGVRPStatisticsEntry,
       "fgs2528kxGVRPStatisticsPort": fgs2528kxGVRPStatisticsPort,
       "fgs2528kxGVRPStatisticsJoinTxCnt": fgs2528kxGVRPStatisticsJoinTxCnt,
       "fgs2528kxGVRPStatisticsLeaveTxCnt": fgs2528kxGVRPStatisticsLeaveTxCnt,
       "fgs2528kxThermalProtection": fgs2528kxThermalProtection,
       "fgs2528kxPriority0Temperature": fgs2528kxPriority0Temperature,
       "fgs2528kxPriority1Temperature": fgs2528kxPriority1Temperature,
       "fgs2528kxPriority2Temperature": fgs2528kxPriority2Temperature,
       "fgs2528kxPriority3Temperature": fgs2528kxPriority3Temperature,
       "fgs2528kxThermalProtectionTable": fgs2528kxThermalProtectionTable,
       "fgs2528kxThermalProtectionEntry": fgs2528kxThermalProtectionEntry,
       "fgs2528kxThermalProtectionPort": fgs2528kxThermalProtectionPort,
       "fgs2528kxThermalProtectionPortTemperature": fgs2528kxThermalProtectionPortTemperature,
       "fgs2528kxThermalProtectionPortPriority": fgs2528kxThermalProtectionPortPriority,
       "fgs2528kxThermalProtectionPortStatus": fgs2528kxThermalProtectionPortStatus,
       "fgs2528kxMirroring": fgs2528kxMirroring,
       "fgs2528kxPortToMirrorOn": fgs2528kxPortToMirrorOn,
       "fgs2528kxMirrorTable": fgs2528kxMirrorTable,
       "fgs2528kxMirrorEntry": fgs2528kxMirrorEntry,
       "fgs2528kxMirrorPort": fgs2528kxMirrorPort,
       "fgs2528kxMirrorMode": fgs2528kxMirrorMode,
       "fgs2528kxTrapEventSeverity": fgs2528kxTrapEventSeverity,
       "fgs2528kxTrapEventSeverityACL": fgs2528kxTrapEventSeverityACL,
       "fgs2528kxTrapEventSeverityACLLog": fgs2528kxTrapEventSeverityACLLog,
       "fgs2528kxTrapEventSeverityAccessMgmt": fgs2528kxTrapEventSeverityAccessMgmt,
       "fgs2528kxTrapEventSeverityAuthFailed": fgs2528kxTrapEventSeverityAuthFailed,
       "fgs2528kxTrapEventSeverityColdStart": fgs2528kxTrapEventSeverityColdStart,
       "fgs2528kxTrapEventSeverityConfigInfo": fgs2528kxTrapEventSeverityConfigInfo,
       "fgs2528kxTrapEventSeverityFirmwareUpgrade": fgs2528kxTrapEventSeverityFirmwareUpgrade,
       "fgs2528kxTrapEventSeverityImportExport": fgs2528kxTrapEventSeverityImportExport,
       "fgs2528kxTrapEventSeverityLACP": fgs2528kxTrapEventSeverityLACP,
       "fgs2528kxTrapEventSeverityLinkStatus": fgs2528kxTrapEventSeverityLinkStatus,
       "fgs2528kxTrapEventSeverityLogin": fgs2528kxTrapEventSeverityLogin,
       "fgs2528kxTrapEventSeverityLogout": fgs2528kxTrapEventSeverityLogout,
       "fgs2528kxTrapEventSeverityLoopProtect": fgs2528kxTrapEventSeverityLoopProtect,
       "fgs2528kxTrapEventSeverityMgmtIPChange": fgs2528kxTrapEventSeverityMgmtIPChange,
       "fgs2528kxTrapEventSeverityModuleChange": fgs2528kxTrapEventSeverityModuleChange,
       "fgs2528kxTrapEventSeverityNAS": fgs2528kxTrapEventSeverityNAS,
       "fgs2528kxTrapEventSeverityPasswdChange": fgs2528kxTrapEventSeverityPasswdChange,
       "fgs2528kxTrapEventSeverityPortSecurity": fgs2528kxTrapEventSeverityPortSecurity,
       "fgs2528kxTrapEventSeverityThermalProtect": fgs2528kxTrapEventSeverityThermalProtect,
       "fgs2528kxTrapEventSeverityVLAN": fgs2528kxTrapEventSeverityVLAN,
       "fgs2528kxTrapEventSeverityWarmStart": fgs2528kxTrapEventSeverityWarmStart,
       "fgs2528kxSMTP": fgs2528kxSMTP,
       "fgs2528kxSMTPMailServer": fgs2528kxSMTPMailServer,
       "fgs2528kxSMTPUserName": fgs2528kxSMTPUserName,
       "fgs2528kxSMTPPassword": fgs2528kxSMTPPassword,
       "fgs2528kxSMTPServeriryLevel": fgs2528kxSMTPServeriryLevel,
       "fgs2528kxSMTPSender": fgs2528kxSMTPSender,
       "fgs2528kxSMTPReturnPath": fgs2528kxSMTPReturnPath,
       "fgs2528kxSMTPEmailAddress1": fgs2528kxSMTPEmailAddress1,
       "fgs2528kxSMTPEmailAddress2": fgs2528kxSMTPEmailAddress2,
       "fgs2528kxSMTPEmailAddress3": fgs2528kxSMTPEmailAddress3,
       "fgs2528kxSMTPEmailAddress4": fgs2528kxSMTPEmailAddress4,
       "fgs2528kxSMTPEmailAddress5": fgs2528kxSMTPEmailAddress5,
       "fgs2528kxSMTPEmailAddress6": fgs2528kxSMTPEmailAddress6,
       "fgs2528kxACL": fgs2528kxACL,
       "fgs2528kxACLPortsConfTable": fgs2528kxACLPortsConfTable,
       "fgs2528kxACLPortsConfEntry": fgs2528kxACLPortsConfEntry,
       "fgs2528kxACLPortsConfPort": fgs2528kxACLPortsConfPort,
       "fgs2528kxACLPortsConfPolicyID": fgs2528kxACLPortsConfPolicyID,
       "fgs2528kxACLPortsConfAction": fgs2528kxACLPortsConfAction,
       "fgs2528kxACLPortsConfRateLimiterID": fgs2528kxACLPortsConfRateLimiterID,
       "fgs2528kxACLPortsConfPortRedirect": fgs2528kxACLPortsConfPortRedirect,
       "fgs2528kxACLPortsConfLogging": fgs2528kxACLPortsConfLogging,
       "fgs2528kxACLPortsConfShutdown": fgs2528kxACLPortsConfShutdown,
       "fgs2528kxACLPortsConfState": fgs2528kxACLPortsConfState,
       "fgs2528kxACLPortsConfCounter": fgs2528kxACLPortsConfCounter,
       "fgs2528kxACLRateLimiterTable": fgs2528kxACLRateLimiterTable,
       "fgs2528kxACLRateLimiterEntry": fgs2528kxACLRateLimiterEntry,
       "fgs2528kxACLRateLimiterID": fgs2528kxACLRateLimiterID,
       "fgs2528kxACLRateLimiterRate": fgs2528kxACLRateLimiterRate,
       "fgs2528kxACLACE": fgs2528kxACLACE,
       "fgs2528kxACLACECreate": fgs2528kxACLACECreate,
       "fgs2528kxACLACETable": fgs2528kxACLACETable,
       "fgs2528kxACLACEEntry": fgs2528kxACLACEEntry,
       "fgs2528kxACLACEIndex": fgs2528kxACLACEIndex,
       "fgs2528kxACLACEID": fgs2528kxACLACEID,
       "fgs2528kxACLACENextID": fgs2528kxACLACENextID,
       "fgs2528kxACLACEIngressPort": fgs2528kxACLACEIngressPort,
       "fgs2528kxACLACEPortPolicyNumber": fgs2528kxACLACEPortPolicyNumber,
       "fgs2528kxACLACEPortPolicyBitmask": fgs2528kxACLACEPortPolicyBitmask,
       "fgs2528kxACLACEFrameType": fgs2528kxACLACEFrameType,
       "fgs2528kxACLACEAction": fgs2528kxACLACEAction,
       "fgs2528kxACLACEDenyPortRedirect": fgs2528kxACLACEDenyPortRedirect,
       "fgs2528kxACLACELogging": fgs2528kxACLACELogging,
       "fgs2528kxACLACERateLimiter": fgs2528kxACLACERateLimiter,
       "fgs2528kxACLACEShutdown": fgs2528kxACLACEShutdown,
       "fgs2528kxACLACEVLANTagPriority": fgs2528kxACLACEVLANTagPriority,
       "fgs2528kxACLACEVLANVID": fgs2528kxACLACEVLANVID,
       "fgs2528kxACLACEEtherType": fgs2528kxACLACEEtherType,
       "fgs2528kxACLACESMAC": fgs2528kxACLACESMAC,
       "fgs2528kxACLACEDMACType": fgs2528kxACLACEDMACType,
       "fgs2528kxACLACEDMAC": fgs2528kxACLACEDMAC,
       "fgs2528kxACLACEArpOpcode": fgs2528kxACLACEArpOpcode,
       "fgs2528kxACLACEArpFlagsRequestReply": fgs2528kxACLACEArpFlagsRequestReply,
       "fgs2528kxACLACEArpFlagsArpSmac": fgs2528kxACLACEArpFlagsArpSmac,
       "fgs2528kxACLACEArpFlagsRarpDmac": fgs2528kxACLACEArpFlagsRarpDmac,
       "fgs2528kxACLACEArpFlagsLength": fgs2528kxACLACEArpFlagsLength,
       "fgs2528kxACLACEArpFlagsIp": fgs2528kxACLACEArpFlagsIp,
       "fgs2528kxACLACEArpFlagsEthernet": fgs2528kxACLACEArpFlagsEthernet,
       "fgs2528kxACLACESIPType": fgs2528kxACLACESIPType,
       "fgs2528kxACLACESIPIPAddress": fgs2528kxACLACESIPIPAddress,
       "fgs2528kxACLACESIPNetworkPrefix": fgs2528kxACLACESIPNetworkPrefix,
       "fgs2528kxACLACEDIPType": fgs2528kxACLACEDIPType,
       "fgs2528kxACLACEDIPIPAddress": fgs2528kxACLACEDIPIPAddress,
       "fgs2528kxACLACEDIPNetworkPrefix": fgs2528kxACLACEDIPNetworkPrefix,
       "fgs2528kxACLACEIPProtocol": fgs2528kxACLACEIPProtocol,
       "fgs2528kxACLACEIPFlagsTTL": fgs2528kxACLACEIPFlagsTTL,
       "fgs2528kxACLACEIPFlagsOptions": fgs2528kxACLACEIPFlagsOptions,
       "fgs2528kxACLACEIPFlagsFragment": fgs2528kxACLACEIPFlagsFragment,
       "fgs2528kxACLACEICMPType": fgs2528kxACLACEICMPType,
       "fgs2528kxACLACEICMPCode": fgs2528kxACLACEICMPCode,
       "fgs2528kxACLACESourcePortMin": fgs2528kxACLACESourcePortMin,
       "fgs2528kxACLACESourcePortMax": fgs2528kxACLACESourcePortMax,
       "fgs2528kxACLACEDestPortMin": fgs2528kxACLACEDestPortMin,
       "fgs2528kxACLACEDestPortMax": fgs2528kxACLACEDestPortMax,
       "fgs2528kxACLACETCPFlagsFin": fgs2528kxACLACETCPFlagsFin,
       "fgs2528kxACLACETCPFlagsSyn": fgs2528kxACLACETCPFlagsSyn,
       "fgs2528kxACLACETCPFlagsRst": fgs2528kxACLACETCPFlagsRst,
       "fgs2528kxACLACETCPFlagsPsh": fgs2528kxACLACETCPFlagsPsh,
       "fgs2528kxACLACETCPFlagsAck": fgs2528kxACLACETCPFlagsAck,
       "fgs2528kxACLACETCPFlagsUrg": fgs2528kxACLACETCPFlagsUrg,
       "fgs2528kxACLACERowStatus": fgs2528kxACLACERowStatus,
       "fgs2528kxACLACEClear": fgs2528kxACLACEClear,
       "fgs2528kxACLACEMoveACEID": fgs2528kxACLACEMoveACEID,
       "fgs2528kxACLACEMoveNextACEID": fgs2528kxACLACEMoveNextACEID,
       "fgs2528kxACLACEStatusTable": fgs2528kxACLACEStatusTable,
       "fgs2528kxACLACEStatusEntry": fgs2528kxACLACEStatusEntry,
       "fgs2528kxACLACEStatusIndex": fgs2528kxACLACEStatusIndex,
       "fgs2528kxACLACEStatusUser": fgs2528kxACLACEStatusUser,
       "fgs2528kxACLACEStatusID": fgs2528kxACLACEStatusID,
       "fgs2528kxACLACEStatusIngressPort": fgs2528kxACLACEStatusIngressPort,
       "fgs2528kxACLACEStatusFrameType": fgs2528kxACLACEStatusFrameType,
       "fgs2528kxACLACEStatusAction": fgs2528kxACLACEStatusAction,
       "fgs2528kxACLACEStatusRateLimiter": fgs2528kxACLACEStatusRateLimiter,
       "fgs2528kxACLACEStatusPortCopy": fgs2528kxACLACEStatusPortCopy,
       "fgs2528kxACLACEStatusMirror": fgs2528kxACLACEStatusMirror,
       "fgs2528kxACLACEStatusCPU": fgs2528kxACLACEStatusCPU,
       "fgs2528kxACLACEStatusCounter": fgs2528kxACLACEStatusCounter,
       "fgs2528kxACLACEStatusConflict": fgs2528kxACLACEStatusConflict,
       "fgs2528kxERPS": fgs2528kxERPS,
       "fgs2528kxERPSConf": fgs2528kxERPSConf,
       "fgs2528kxERPSConfCreate": fgs2528kxERPSConfCreate,
       "fgs2528kxERPSConfTable": fgs2528kxERPSConfTable,
       "fgs2528kxERPSConfEntry": fgs2528kxERPSConfEntry,
       "fgs2528kxERPSConfIndex": fgs2528kxERPSConfIndex,
       "fgs2528kxERPSConfERPSID": fgs2528kxERPSConfERPSID,
       "fgs2528kxERPSConfPort0": fgs2528kxERPSConfPort0,
       "fgs2528kxERPSConfPort1": fgs2528kxERPSConfPort1,
       "fgs2528kxERPSConfPort0SFMEP": fgs2528kxERPSConfPort0SFMEP,
       "fgs2528kxERPSConfPort1SFMEP": fgs2528kxERPSConfPort1SFMEP,
       "fgs2528kxERPSConfPort0APSMEP": fgs2528kxERPSConfPort0APSMEP,
       "fgs2528kxERPSConfPort1APSMEP": fgs2528kxERPSConfPort1APSMEP,
       "fgs2528kxERPSConfRingType": fgs2528kxERPSConfRingType,
       "fgs2528kxERPSConfInterconnectedNode": fgs2528kxERPSConfInterconnectedNode,
       "fgs2528kxERPSConfVirtualChannel": fgs2528kxERPSConfVirtualChannel,
       "fgs2528kxERPSConfMajorRingID": fgs2528kxERPSConfMajorRingID,
       "fgs2528kxERPSConfAlarm": fgs2528kxERPSConfAlarm,
       "fgs2528kxERPSInstanceConfConfigured": fgs2528kxERPSInstanceConfConfigured,
       "fgs2528kxERPSInstanceConfGuardTime": fgs2528kxERPSInstanceConfGuardTime,
       "fgs2528kxERPSInstanceConfWTRTime": fgs2528kxERPSInstanceConfWTRTime,
       "fgs2528kxERPSInstanceConfHoldOffTime": fgs2528kxERPSInstanceConfHoldOffTime,
       "fgs2528kxERPSInstanceConfVersion": fgs2528kxERPSInstanceConfVersion,
       "fgs2528kxERPSInstanceConfRevertive": fgs2528kxERPSInstanceConfRevertive,
       "fgs2528kxERPSInstanceConfVLANconfig": fgs2528kxERPSInstanceConfVLANconfig,
       "fgs2528kxERPSConfRowStatus": fgs2528kxERPSConfRowStatus,
       "fgs2528kxSecurity": fgs2528kxSecurity,
       "fgs2528kxIPSourceGuard": fgs2528kxIPSourceGuard,
       "fgs2528kxIPSourceGuardConf": fgs2528kxIPSourceGuardConf,
       "fgs2528kxIPSourceGuardMode": fgs2528kxIPSourceGuardMode,
       "fgs2528kxIPSourceGuardPortConfigTable": fgs2528kxIPSourceGuardPortConfigTable,
       "fgs2528kxIPSourceGuardPortConfigEntry": fgs2528kxIPSourceGuardPortConfigEntry,
       "fgs2528kxIPSourceGuardPortConfigPort": fgs2528kxIPSourceGuardPortConfigPort,
       "fgs2528kxIPSourceGuardPortConfigMode": fgs2528kxIPSourceGuardPortConfigMode,
       "fgs2528kxIPSourceGuardPortMaxDynamicClients": fgs2528kxIPSourceGuardPortMaxDynamicClients,
       "fgs2528kxIPSourceGuardStatic": fgs2528kxIPSourceGuardStatic,
       "fgs2528kxIPSourceGuardStaticCreate": fgs2528kxIPSourceGuardStaticCreate,
       "fgs2528kxIPSourceGuardStaticTable": fgs2528kxIPSourceGuardStaticTable,
       "fgs2528kxIPSourceGuardStaticEntry": fgs2528kxIPSourceGuardStaticEntry,
       "fgs2528kxIPSourceGuardStaticIndex": fgs2528kxIPSourceGuardStaticIndex,
       "fgs2528kxIPSourceGuardStaticPort": fgs2528kxIPSourceGuardStaticPort,
       "fgs2528kxIPSourceGuardStaticVLANId": fgs2528kxIPSourceGuardStaticVLANId,
       "fgs2528kxIPSourceGuardStaticIPAddress": fgs2528kxIPSourceGuardStaticIPAddress,
       "fgs2528kxIPSourceGuardStaticMACAddress": fgs2528kxIPSourceGuardStaticMACAddress,
       "fgs2528kxIPSourceGuardStaticRowStatus": fgs2528kxIPSourceGuardStaticRowStatus,
       "fgs2528kxIPSourceGuardDynamicTable": fgs2528kxIPSourceGuardDynamicTable,
       "fgs2528kxIPSourceGuardDynamicEntry": fgs2528kxIPSourceGuardDynamicEntry,
       "fgs2528kxIPSourceGuardDynamicIndex": fgs2528kxIPSourceGuardDynamicIndex,
       "fgs2528kxIPSourceGuardDynamicPort": fgs2528kxIPSourceGuardDynamicPort,
       "fgs2528kxIPSourceGuardDynamicVLANId": fgs2528kxIPSourceGuardDynamicVLANId,
       "fgs2528kxIPSourceGuardDynamicIPAddress": fgs2528kxIPSourceGuardDynamicIPAddress,
       "fgs2528kxIPSourceGuardDynamicMACAddress": fgs2528kxIPSourceGuardDynamicMACAddress,
       "fgs2528kxARPInspection": fgs2528kxARPInspection,
       "fgs2528kxARPInspectionConf": fgs2528kxARPInspectionConf,
       "fgs2528kxARPInspectionConfMode": fgs2528kxARPInspectionConfMode,
       "fgs2528kxARPInspectionConfTable": fgs2528kxARPInspectionConfTable,
       "fgs2528kxARPInspectionConfEntry": fgs2528kxARPInspectionConfEntry,
       "fgs2528kxARPInspectionConfPortIndex": fgs2528kxARPInspectionConfPortIndex,
       "fgs2528kxARPInspectionConfPortMode": fgs2528kxARPInspectionConfPortMode,
       "fgs2528kxARPInspectionStatic": fgs2528kxARPInspectionStatic,
       "fgs2528kxARPInspectionStaticCreate": fgs2528kxARPInspectionStaticCreate,
       "fgs2528kxARPInspectionStaticTable": fgs2528kxARPInspectionStaticTable,
       "fgs2528kxARPInspectionStaticEntry": fgs2528kxARPInspectionStaticEntry,
       "fgs2528kxARPInspectionStaticIndex": fgs2528kxARPInspectionStaticIndex,
       "fgs2528kxARPInspectionStaticPort": fgs2528kxARPInspectionStaticPort,
       "fgs2528kxARPInspectionStaticVLANId": fgs2528kxARPInspectionStaticVLANId,
       "fgs2528kxARPInspectionStaticIPAddress": fgs2528kxARPInspectionStaticIPAddress,
       "fgs2528kxARPInspectionStaticMACAddress": fgs2528kxARPInspectionStaticMACAddress,
       "fgs2528kxARPInspectionStaticRowStatus": fgs2528kxARPInspectionStaticRowStatus,
       "fgs2528kxARPInspectionDynamicTable": fgs2528kxARPInspectionDynamicTable,
       "fgs2528kxARPInspectionDynamicEntry": fgs2528kxARPInspectionDynamicEntry,
       "fgs2528kxARPInspectionDynamicIndex": fgs2528kxARPInspectionDynamicIndex,
       "fgs2528kxARPInspectionDynamicPort": fgs2528kxARPInspectionDynamicPort,
       "fgs2528kxARPInspectionDynamicVLANId": fgs2528kxARPInspectionDynamicVLANId,
       "fgs2528kxARPInspectionDynamicIPAddress": fgs2528kxARPInspectionDynamicIPAddress,
       "fgs2528kxARPInspectionDynamicMACAddress": fgs2528kxARPInspectionDynamicMACAddress,
       "fgs2528kxDHCPSnooping": fgs2528kxDHCPSnooping,
       "fgs2528kxDHCPSnoopingConf": fgs2528kxDHCPSnoopingConf,
       "fgs2528kxDHCPSnoopingMode": fgs2528kxDHCPSnoopingMode,
       "fgs2528kxDHCPSnoopingPortModeConfigurationTable": fgs2528kxDHCPSnoopingPortModeConfigurationTable,
       "fgs2528kxDHCPSnoopingPortModeConfigurationEntry": fgs2528kxDHCPSnoopingPortModeConfigurationEntry,
       "fgs2528kxDHCPSnoopingPortModeConfigurationPort": fgs2528kxDHCPSnoopingPortModeConfigurationPort,
       "fgs2528kxDHCPSnoopingPortModeConfigurationMode": fgs2528kxDHCPSnoopingPortModeConfigurationMode,
       "fgs2528kxDHCPSnoopingStatisticsTable": fgs2528kxDHCPSnoopingStatisticsTable,
       "fgs2528kxDHCPSnoopingStatisticsEntry": fgs2528kxDHCPSnoopingStatisticsEntry,
       "fgs2528kxDHCPSnoopingStatisticsPort": fgs2528kxDHCPSnoopingStatisticsPort,
       "fgs2528kxDHCPSnoopingStatisticsClear": fgs2528kxDHCPSnoopingStatisticsClear,
       "fgs2528kxDHCPSnoopingRxDiscover": fgs2528kxDHCPSnoopingRxDiscover,
       "fgs2528kxDHCPSnoopingRxOffer": fgs2528kxDHCPSnoopingRxOffer,
       "fgs2528kxDHCPSnoopingRxRequest": fgs2528kxDHCPSnoopingRxRequest,
       "fgs2528kxDHCPSnoopingRxDecline": fgs2528kxDHCPSnoopingRxDecline,
       "fgs2528kxDHCPSnoopingRxACK": fgs2528kxDHCPSnoopingRxACK,
       "fgs2528kxDHCPSnoopingRxNAK": fgs2528kxDHCPSnoopingRxNAK,
       "fgs2528kxDHCPSnoopingRxRelease": fgs2528kxDHCPSnoopingRxRelease,
       "fgs2528kxDHCPSnoopingRxInform": fgs2528kxDHCPSnoopingRxInform,
       "fgs2528kxDHCPSnoopingRxLeaseQuery": fgs2528kxDHCPSnoopingRxLeaseQuery,
       "fgs2528kxDHCPSnoopingRxLeaseUnassigned": fgs2528kxDHCPSnoopingRxLeaseUnassigned,
       "fgs2528kxDHCPSnoopingRxLeaseUnknown": fgs2528kxDHCPSnoopingRxLeaseUnknown,
       "fgs2528kxDHCPSnoopingRxLeaseActive": fgs2528kxDHCPSnoopingRxLeaseActive,
       "fgs2528kxDHCPSnoopingTxDiscover": fgs2528kxDHCPSnoopingTxDiscover,
       "fgs2528kxDHCPSnoopingTxOffer": fgs2528kxDHCPSnoopingTxOffer,
       "fgs2528kxDHCPSnoopingTxRequest": fgs2528kxDHCPSnoopingTxRequest,
       "fgs2528kxDHCPSnoopingTxDecline": fgs2528kxDHCPSnoopingTxDecline,
       "fgs2528kxDHCPSnoopingTxACK": fgs2528kxDHCPSnoopingTxACK,
       "fgs2528kxDHCPSnoopingTxNAK": fgs2528kxDHCPSnoopingTxNAK,
       "fgs2528kxDHCPSnoopingTxRelease": fgs2528kxDHCPSnoopingTxRelease,
       "fgs2528kxDHCPSnoopingTxInform": fgs2528kxDHCPSnoopingTxInform,
       "fgs2528kxDHCPSnoopingTxLeaseQuery": fgs2528kxDHCPSnoopingTxLeaseQuery,
       "fgs2528kxDHCPSnoopingTxLeaseUnassigned": fgs2528kxDHCPSnoopingTxLeaseUnassigned,
       "fgs2528kxDHCPSnoopingTxLeaseUnknown": fgs2528kxDHCPSnoopingTxLeaseUnknown,
       "fgs2528kxDHCPSnoopingTxLeaseActive": fgs2528kxDHCPSnoopingTxLeaseActive,
       "fgs2528kxDHCPRelay": fgs2528kxDHCPRelay,
       "fgs2528kxDHCPRelayConfiguration": fgs2528kxDHCPRelayConfiguration,
       "fgs2528kxDHCPRelayMode": fgs2528kxDHCPRelayMode,
       "fgs2528kxDHCPRelayServer": fgs2528kxDHCPRelayServer,
       "fgs2528kxDHCPRelayInformationMode": fgs2528kxDHCPRelayInformationMode,
       "fgs2528kxDHCPRelayInformationPolicy": fgs2528kxDHCPRelayInformationPolicy,
       "fgs2528kxDHCPRelayStatistics": fgs2528kxDHCPRelayStatistics,
       "fgs2528kxDHCPRelayServerStatistics": fgs2528kxDHCPRelayServerStatistics,
       "fgs2528kxServerStatTransmitToServer": fgs2528kxServerStatTransmitToServer,
       "fgs2528kxServerStatTransmitError": fgs2528kxServerStatTransmitError,
       "fgs2528kxServerStatReceiveFromServer": fgs2528kxServerStatReceiveFromServer,
       "fgs2528kxServerStatReceiveMissingAgentOption": fgs2528kxServerStatReceiveMissingAgentOption,
       "fgs2528kxServerStatReceiveMissingCircuitID": fgs2528kxServerStatReceiveMissingCircuitID,
       "fgs2528kxServerStatReceiveMissingRemoteID": fgs2528kxServerStatReceiveMissingRemoteID,
       "fgs2528kxServerStatReceiveBadCircuitID": fgs2528kxServerStatReceiveBadCircuitID,
       "fgs2528kxServerStatReceiveBadRemoteID": fgs2528kxServerStatReceiveBadRemoteID,
       "fgs2528kxDHCPRelayClientStatistics": fgs2528kxDHCPRelayClientStatistics,
       "fgs2528kxClientStatTransmitToClient": fgs2528kxClientStatTransmitToClient,
       "fgs2528kxClientStatTransmitError": fgs2528kxClientStatTransmitError,
       "fgs2528kxClientStatReceivefromClient": fgs2528kxClientStatReceivefromClient,
       "fgs2528kxClientStatReceiveAgentOption": fgs2528kxClientStatReceiveAgentOption,
       "fgs2528kxClientStatReplaceAgentOption": fgs2528kxClientStatReplaceAgentOption,
       "fgs2528kxClientStatKeepAgentOption": fgs2528kxClientStatKeepAgentOption,
       "fgs2528kxClientStatDropAgentOption": fgs2528kxClientStatDropAgentOption,
       "fgs2528kxPortSecurity": fgs2528kxPortSecurity,
       "fgs2528kxPortSecLimitCtrl": fgs2528kxPortSecLimitCtrl,
       "fgs2528kxPortSecLimitCtrlSystemConf": fgs2528kxPortSecLimitCtrlSystemConf,
       "fgs2528kxPortSecurityMode": fgs2528kxPortSecurityMode,
       "fgs2528kxPortSecurityAging": fgs2528kxPortSecurityAging,
       "fgs2528kxPortSecurityAgingPeriod": fgs2528kxPortSecurityAgingPeriod,
       "fgs2528kxPortSecLimitCtrlTable": fgs2528kxPortSecLimitCtrlTable,
       "fgs2528kxPortSecLimitCtrlEntry": fgs2528kxPortSecLimitCtrlEntry,
       "fgs2528kxPortSecLimitCtrlPort": fgs2528kxPortSecLimitCtrlPort,
       "fgs2528kxPortSecLimitCtrlPortMode": fgs2528kxPortSecLimitCtrlPortMode,
       "fgs2528kxPortSecLimitCtrlPortLimit": fgs2528kxPortSecLimitCtrlPortLimit,
       "fgs2528kxPortSecLimitCtrlPortAction": fgs2528kxPortSecLimitCtrlPortAction,
       "fgs2528kxPortSecLimitCtrlPortState": fgs2528kxPortSecLimitCtrlPortState,
       "fgs2528kxPortSecLimitCtrlPortReOpen": fgs2528kxPortSecLimitCtrlPortReOpen,
       "fgs2528kxPortSecSwitchStatusTable": fgs2528kxPortSecSwitchStatusTable,
       "fgs2528kxPortSecSwitchStatusEntry": fgs2528kxPortSecSwitchStatusEntry,
       "fgs2528kxPortSecSwitchStatusPort": fgs2528kxPortSecSwitchStatusPort,
       "fgs2528kxPortSecSwitchStatusUsers": fgs2528kxPortSecSwitchStatusUsers,
       "fgs2528kxPortSecSwitchStatusState": fgs2528kxPortSecSwitchStatusState,
       "fgs2528kxPortSecSwitchStatusMACCountCurrent": fgs2528kxPortSecSwitchStatusMACCountCurrent,
       "fgs2528kxPortSecSwitchStatusMACCountLimit": fgs2528kxPortSecSwitchStatusMACCountLimit,
       "fgs2528kxPortSecPortStatus": fgs2528kxPortSecPortStatus,
       "fgs2528kxPortSecPortStatusPort": fgs2528kxPortSecPortStatusPort,
       "fgs2528kxPortSecPortStatusTable": fgs2528kxPortSecPortStatusTable,
       "fgs2528kxPortSecPortStatusEntry": fgs2528kxPortSecPortStatusEntry,
       "fgs2528kxPortSecPortStatusIndex": fgs2528kxPortSecPortStatusIndex,
       "fgs2528kxPortSecPortStatusMACAddress": fgs2528kxPortSecPortStatusMACAddress,
       "fgs2528kxPortSecPortStatusVLANId": fgs2528kxPortSecPortStatusVLANId,
       "fgs2528kxPortSecPortStatusState": fgs2528kxPortSecPortStatusState,
       "fgs2528kxPortSecPortStatusTimeOfAddition": fgs2528kxPortSecPortStatusTimeOfAddition,
       "fgs2528kxPortSecPortStatusAgeAndHold": fgs2528kxPortSecPortStatusAgeAndHold,
       "fgs2528kxAccessManagement": fgs2528kxAccessManagement,
       "fgs2528kxAccessMgtConf": fgs2528kxAccessMgtConf,
       "fgs2528kxAccessMgtConfMode": fgs2528kxAccessMgtConfMode,
       "fgs2528kxAccessMgtConfCreate": fgs2528kxAccessMgtConfCreate,
       "fgs2528kxAccessMgtConfTable": fgs2528kxAccessMgtConfTable,
       "fgs2528kxAccessMgtConfEntry": fgs2528kxAccessMgtConfEntry,
       "fgs2528kxAccessMgtIndex": fgs2528kxAccessMgtIndex,
       "fgs2528kxAccessMgtAddresstype": fgs2528kxAccessMgtAddresstype,
       "fgs2528kxAccessMgtStartIpAddress": fgs2528kxAccessMgtStartIpAddress,
       "fgs2528kxAccessMgtEndIpAddress": fgs2528kxAccessMgtEndIpAddress,
       "fgs2528kxAccessMgtHttpHttps": fgs2528kxAccessMgtHttpHttps,
       "fgs2528kxAccessMgtSNMP": fgs2528kxAccessMgtSNMP,
       "fgs2528kxAccessMgtTelnetSSH": fgs2528kxAccessMgtTelnetSSH,
       "fgs2528kxAccessMgtRowStatus": fgs2528kxAccessMgtRowStatus,
       "fgs2528kxAccessMgtStatistics": fgs2528kxAccessMgtStatistics,
       "fgs2528kxHttpReceivedPkts": fgs2528kxHttpReceivedPkts,
       "fgs2528kxHttpAllowedPkts": fgs2528kxHttpAllowedPkts,
       "fgs2528kxHttpDiscardedPkts": fgs2528kxHttpDiscardedPkts,
       "fgs2528kxHttpsReceivedPkts": fgs2528kxHttpsReceivedPkts,
       "fgs2528kxHttpsAllowedPkts": fgs2528kxHttpsAllowedPkts,
       "fgs2528kxHttpsDiscardedPkts": fgs2528kxHttpsDiscardedPkts,
       "fgs2528kxSnmpReceivedPkts": fgs2528kxSnmpReceivedPkts,
       "fgs2528kxSnmpAllowedPkts": fgs2528kxSnmpAllowedPkts,
       "fgs2528kxSnmpDiscardedPkts": fgs2528kxSnmpDiscardedPkts,
       "fgs2528kxTelnetReceivedPkts": fgs2528kxTelnetReceivedPkts,
       "fgs2528kxTelnetAllowedPkts": fgs2528kxTelnetAllowedPkts,
       "fgs2528kxTelnetDiscardedPkts": fgs2528kxTelnetDiscardedPkts,
       "fgs2528kxSSHReceivedPkts": fgs2528kxSSHReceivedPkts,
       "fgs2528kxSSHAllowedPkts": fgs2528kxSSHAllowedPkts,
       "fgs2528kxSSHDiscardedPkts": fgs2528kxSSHDiscardedPkts,
       "fgs2528kxAccessMgtStatisticsClearAll": fgs2528kxAccessMgtStatisticsClearAll,
       "fgs2528kxSSH": fgs2528kxSSH,
       "fgs2528kxSSHMode": fgs2528kxSSHMode,
       "fgs2528kxHTTPS": fgs2528kxHTTPS,
       "fgs2528kxHTTPSMode": fgs2528kxHTTPSMode,
       "fgs2528kxHTTPSAutoRedirect": fgs2528kxHTTPSAutoRedirect,
       "fgs2528kxAuthMethod": fgs2528kxAuthMethod,
       "fgs2528kxConsoleAuthMethod": fgs2528kxConsoleAuthMethod,
       "fgs2528kxConsoleFallback": fgs2528kxConsoleFallback,
       "fgs2528kxTelnetAuthMethod": fgs2528kxTelnetAuthMethod,
       "fgs2528kxTelnetFallback": fgs2528kxTelnetFallback,
       "fgs2528kxSshAuthMethod": fgs2528kxSshAuthMethod,
       "fgs2528kxSshFallback": fgs2528kxSshFallback,
       "fgs2528kxWebAuthMethod": fgs2528kxWebAuthMethod,
       "fgs2528kxWebFallback": fgs2528kxWebFallback,
       "fgs2528kxMaintenance": fgs2528kxMaintenance,
       "fgs2528kxRestartDevice": fgs2528kxRestartDevice,
       "fgs2528kxFirmware": fgs2528kxFirmware,
       "fgs2528kxFirmwareIpAddress": fgs2528kxFirmwareIpAddress,
       "fgs2528kxFirmwareFileName": fgs2528kxFirmwareFileName,
       "fgs2528kxDoFirmwareUpgrade": fgs2528kxDoFirmwareUpgrade,
       "fgs2528kxSaveOrRestore": fgs2528kxSaveOrRestore,
       "fgs2528kxFactoryDefaults": fgs2528kxFactoryDefaults,
       "fgs2528kxSaveStart": fgs2528kxSaveStart,
       "fgs2528kxSaveUser": fgs2528kxSaveUser,
       "fgs2528kxRestoreUser": fgs2528kxRestoreUser,
       "fgs2528kxExportOrImport": fgs2528kxExportOrImport,
       "fgs2528kxExportIpAddress": fgs2528kxExportIpAddress,
       "fgs2528kxExportConfigName": fgs2528kxExportConfigName,
       "fgs2528kxDoExportConfig": fgs2528kxDoExportConfig,
       "fgs2528kxImportIpAddress": fgs2528kxImportIpAddress,
       "fgs2528kxImportConfigName": fgs2528kxImportConfigName,
       "fgs2528kxDoImportConfig": fgs2528kxDoImportConfig,
       "fgs2528kxDiagnostics": fgs2528kxDiagnostics,
       "fgs2528kxPingIpAddress": fgs2528kxPingIpAddress,
       "fgs2528kxPingSize": fgs2528kxPingSize,
       "fgs2528kxDoPingConfig": fgs2528kxDoPingConfig,
       "fgs2528kxPingResult": fgs2528kxPingResult,
       "fgs2528kxPing6IpAddress": fgs2528kxPing6IpAddress,
       "fgs2528kxPing6Size": fgs2528kxPing6Size,
       "fgs2528kxDoPing6Config": fgs2528kxDoPing6Config,
       "fgs2528kxPing6Result": fgs2528kxPing6Result,
       "fgs2528kxVeriPHY": fgs2528kxVeriPHY,
       "fgs2528kxVeriPHYTest": fgs2528kxVeriPHYTest,
       "fgs2528kxVeriPHYTable": fgs2528kxVeriPHYTable,
       "fgs2528kxVeriPHYEntry": fgs2528kxVeriPHYEntry,
       "fgs2528kxVeriPHYPort": fgs2528kxVeriPHYPort,
       "fgs2528kxVeriPHYPairA": fgs2528kxVeriPHYPairA,
       "fgs2528kxVeriPHYLengthA": fgs2528kxVeriPHYLengthA,
       "fgs2528kxVeriPHYPairB": fgs2528kxVeriPHYPairB,
       "fgs2528kxVeriPHYLengthB": fgs2528kxVeriPHYLengthB,
       "fgs2528kxVeriPHYPairC": fgs2528kxVeriPHYPairC,
       "fgs2528kxVeriPHYLengthC": fgs2528kxVeriPHYLengthC,
       "fgs2528kxVeriPHYPairD": fgs2528kxVeriPHYPairD,
       "fgs2528kxVeriPHYLengthD": fgs2528kxVeriPHYLengthD,
       "fgs2528kxTrap": fgs2528kxTrap,
       "fgs2528kxTrapEvent": fgs2528kxTrapEvent,
       "fgs2528kxEmergency": fgs2528kxEmergency,
       "fgs2528kxAlert": fgs2528kxAlert,
       "fgs2528kxCritical": fgs2528kxCritical,
       "fgs2528kxError": fgs2528kxError,
       "fgs2528kxWarning": fgs2528kxWarning,
       "fgs2528kxNotice": fgs2528kxNotice,
       "fgs2528kxInformational": fgs2528kxInformational,
       "fgs2528kxDebug": fgs2528kxDebug,
       "fgs2528kxTrapVariable": fgs2528kxTrapVariable,
       "fgs2528kxInformation": fgs2528kxInformation}
)
